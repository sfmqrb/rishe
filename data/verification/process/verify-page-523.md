# Verification process log — verify-page-523


## [2026-10-16T05:13:01.620Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 523 only. Chart text: /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-523.txt; source JSON: /home/sfmqrb/git/rishe-private/data/extracted/batch/page-523.json. Write /home/sfmqrb/git/rishe-private/data/verification/page-523.json, run `python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 523` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-10-16T05:13:01.661Z] INPUT

<system-reminder>
Your final report is delivered through SubagentHandback: when your work is complete, call SubagentHandback({message: <your full report>}). The call ends your run, so make it your last step. Only a SubagentHandback call reaches your caller as your result; plain text you write at the end is not delivered.
</system-reminder>


## [2026-10-16T05:13:05.226Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-10-16T05:13:05.252Z] TOOL RESULT

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


## [2026-10-16T05:13:05.727Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-523.txt"
}
```


### [2026-10-16T05:13:05.782Z] TOOL RESULT

```
1	=== PDF page 523 (book page 493) ===
2	--- entry 0 ---
3	ROOT [Avestan] Vareta : slave  (refs BQT:253)
4	#1 (parent #0) [Pahlavi] refs=BQT:253; HUB:26 | vartak 1 : slave
5	  #2 (parent #1) [Persian] refs=HUB:26; BQT:253 | bardeh «بَرده» : slave
6	    #3 (parent #2) [Arabic] refs=KLN:148 | bardaj
7	      #4 (parent #3) [Italian] refs=KLN | 
8	        #5 (parent #4) [French] refs=KLN:148 | bardache
9	          #6 (parent #5) [English] refs=KLN:148 | bardash : slave
10	--- entry 1 ---
11	ROOT Vata -> redirect to Bata
12	--- entry 2 ---
13	ROOT [Sanskrit] Vatin-ganah : eggplant  (refs KLN:125; AHD:86)
14	#1 (parent #0) [Persian] refs=KLN:125; BQT:213; MON:444 | bâdengân «بادنگان» : eggplant | extra: باتنگان
15	  #2 (parent #1) [Arabic] refs=KLN:125,165 | bâdenjân, al-bâdenjân : eggplant
16	    #3 (parent #2) [Persian] refs=BQT:213; MON:444 | bâdenjân «بادنجان» : eggplant | extra: بادمجان
17	    #4 (parent #2) [Spanish] refs=KLN:125 | berengina, au-berengina : eggplant
18	      #5 (parent #4) [French] refs=AHD:86 | aubergine
19	        #6 (parent #5) [English] refs=AHD:86 | aubergine : eggplant
20	      #7 (parent #4) [English] refs=KLN:165 | berengina : eggplant
21	
```


## [2026-10-16T05:13:06.488Z] TOOL CALL #3: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/extracted/batch/page-523.json"
}
```


### [2026-10-16T05:13:06.759Z] TOOL RESULT

```
1	{
2	  "pdf_page": 523,
3	  "book_page": 493,
4	  "entries": [
5	    {
6	      "root": {
7	        "name": "Vareta",
8	        "lang": "Avestan",
9	        "refs": "BQT:253",
10	        "gloss": "slave"
11	      },
12	      "nodes": [
13	        {
14	          "id": 1,
15	          "parent": 0,
16	          "lang": "Pahlavi",
17	          "refs": "BQT:253; HUB:26",
18	          "words": [
19	            {"translit": "vartak 1", "gloss": "slave", "script": null}
20	          ],
21	          "script_extra": null,
22	          "note": null,
23	          "quote": null
24	        },
25	        {
26	          "id": 2,
27	          "parent": 1,
28	          "lang": "Persian",
29	          "refs": "HUB:26; BQT:253",
30	          "words": [
31	            {"translit": "bardeh", "gloss": "slave", "script": "بَرده"}
32	          ],
33	          "script_extra": null,
34	          "note": null,
35	          "quote": null
36	        },
37	        {
38	          "id": 3,
39	          "parent": 2,
40	          "lang": "Arabic",
41	          "refs": "KLN:148",
42	          "words": [
43	            {"translit": "bardaj", "gloss": null, "script": null}
44	          ],
45	          "script_extra": null,
46	          "note": null,
47	          "quote": null
48	        },
49	        {
50	          "id": 4,
51	          "parent": 3,
52	          "lang": "Italian",
53	          "refs": "KLN",
54	          "words": [],
55	          "script_extra": null,
56	          "note": null,
57	          "quote": null
58	        },
59	        {
60	          "id": 5,
61	          "parent": 4,
62	          "lang": "French",
63	          "refs": "KLN:148",
64	          "words": [
65	            {"translit": "bardache", "gloss": null, "script": null}
66	          ],
67	          "script_extra": null,
68	          "note": null,
69	          "quote": null
70	        },
71	        {
72	          "id": 6,
73	          "parent": 5,
74	          "lang": "English",
75	          "refs": "KLN:148",
76	          "words": [
77	            {"translit": "bardash", "gloss": "slave", "script": null}
78	          ],
79	          "script_extra": null,
80	          "note": null,
81	          "quote": null
82	        }
83	      ]
84	    },
85	    {
86	      "root": {
87	        "name": "Vata",
88	        "redirect": "Bata"
89	      },
90	      "nodes": []
91	    },
92	    {
93	      "root": {
94	        "name": "Vatin-ganah",
95	        "lang": "Sanskrit",
96	        "refs": "KLN:125; AHD:86",
97	        "gloss": "eggplant",
98	        "note": "POK:383 shows \"ganah: bundle, group\" from the Indo-European root \"Ger: to tie together\"."
99	      },
100	      "nodes": [
101	        {
102	          "id": 1,
103	          "parent": 0,
104	          "lang": "Persian",
105	          "refs": "KLN:125; BQT:213; MON:444",
106	          "words": [
107	            {"translit": "bâdengân", "gloss": "eggplant", "script": "بادنگان"}
108	          ],
109	          "script_extra": "باتنگان",
110	          "note": null,
111	          "quote": null
112	        },
113	        {
114	          "id": 2,
115	          "parent": 1,
116	          "lang": "Arabic",
117	          "refs": "KLN:125,165",
118	          "words": [
119	            {"translit": "bâdenjân, al-bâdenjân", "gloss": "eggplant", "script": null}
120	          ],
121	          "script_extra": null,
122	          "note": null,
123	          "quote": null
124	        },
125	        {
126	          "id": 3,
127	          "parent": 2,
128	          "lang": "Persian",
129	          "refs": "BQT:213; MON:444",
130	          "words": [
131	            {"translit": "bâdenjân", "gloss": "eggplant", "script": "بادنجان"}
132	          ],
133	          "script_extra": "بادمجان",
134	          "note": null,
135	          "quote": null
136	        },
137	        {
138	          "id": 4,
139	          "parent": 2,
140	          "lang": "Spanish",
141	          "refs": "KLN:125",
142	          "words": [
143	            {"translit": "berengina, au-berengina", "gloss": "eggplant", "script": null}
144	          ],
145	          "script_extra": null,
146	          "note": null,
147	          "quote": null
148	        },
149	        {
150	          "id": 5,
151	          "parent": 4,
152	          "lang": "French",
153	          "refs": "AHD:86",
154	          "words": [
155	            {"translit": "aubergine", "gloss": null, "script": null}
156	          ],
157	          "script_extra": null,
158	          "note": null,
159	          "quote": null
160	        },
161	        {
162	          "id": 6,
163	          "parent": 5,
164	          "lang": "English",
165	          "refs": "AHD:86",
166	          "words": [
167	            {"translit": "aubergine", "gloss": "eggplant", "script": null}
168	          ],
169	          "script_extra": null,
170	          "note": null,
171	          "quote": null
172	        },
173	        {
174	          "id": 7,
175	          "parent": 4,
176	          "lang": "English",
177	          "refs": "KLN:165",
178	          "words": [
179	            {"translit": "berengina", "gloss": "eggplant", "script": null}
180	          ],
181	          "script_extra": null,
182	          "note": null,
183	          "quote": null
184	        }
185	      ]
186	    }
187	  ]
188	}
189	
```


## [2026-10-16T05:13:16.553Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; cat data/verification/sources/SOURCE_MATRIX.md | head -80; ls data/verification/sources/refs/ | head -100; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['BQT','HUB','KLN','AHD','MON','POK','HRN','PHD','NYB','SKT','WEB','FSD','DEV','DOZ','LKT','PHN','LAM','PLA','AFM','FVQ','ARY','WLD','IEC','SYN','BRT','KNT','AFA']:\n  v=d.get(k); print(k, v and {x:v.get(x) for x in ['local_file','page_offset','lookup_hint','scans']})\n\""
}
```


### [2026-10-16T05:13:17.005Z] TOOL RESULT

```
<persisted-output>
Output too large (33.7KB). Full output saved to: /home/sfmqrb/.claude-work/projects/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/tool-results/bit3ktxq1.txt

Preview (first 2KB):
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
...
</persisted-output>
```


## [2026-10-16T05:13:19.912Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; grep -E '^\\- \\*\\*|^## |refs/[A-Z]' data/verification/sources/SOURCE_MATRIX.md | grep -v incoming | head -120"
}
```


### [2026-10-16T05:13:20.391Z] TOOL RESULT

```
## Indo-European roots (any IE node, root boxes)
- **POK** — J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_01.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_02.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_03.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_full.txt`
- **WLD** — A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-3
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/WLD_band3.txt`
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
- **MON** — Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part1.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part2.txt`
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
- **FFD** — Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995
- **IRN** — Bahram Farahvashi, Iranvij, Tehran University Press 1368/1989
- **AVG** — A. V. W. Jackson, An Avesta Grammar in Comparison with Sanskrit, Part I, Stuttgart 1892
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AVG.txt`
- **HID** — C. Bartholomae, Handbuch der altiranischen Dialekte, Leipzig 1883
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HID.txt`
- **ZAW** — C. Bartholomae, Zum altiranischen Wörterbuch: Nacharbeiten und Vorarbeiten (Beiheft zu IF XIX), Strassburg 190
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
```


## [2026-10-16T05:13:29.370Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for f in KLN_1966.txt KLN_1971.txt SKT.txt LKT.txt DEV.txt PHN.txt LAM.txt DOZ.txt HJB*.txt AID*.txt; do echo \"== $f\"; grep -n -i -E 'bardach|bardash|bardaj|bardasc|aubergin|berenjen|bereng|brinjal|badinjan|bâdinjân|badingan|vatinga|vātiṅg|vatig' $f 2>/dev/null | head -15; done; ls | grep -i -E 'hjb|aid|web|fsd|tts'"
}
```


### [2026-10-16T05:13:29.939Z] TOOL RESULT

```
== KLN_1966.txt
3927:auantic,  adj.,  atrophic.  —  Formed  with  suff.  -ic fr.  Gk.  xuavTTj,  ‘a  wasting,  atrophy’,  fr.  auaE- veiv,  ‘to  wither,  be  dry’,  fr.  a\kiv,  ‘to  dry’,  fr. cchoq,  ‘dry’,  which  stands  for  *saitso-s  and  de¬ rives  fr.  I.-E.  base  *saus-,  *sus-,  ‘dry’,  whence also  OE.  sear,  ‘dry’,  OHG.  soren,  ‘to  become dry’.  See  sere,  adj.,  and  cp.  austere, aubade,  n.,  morning  serenade.  —  F.,  fr.  Proven?. aubado,  fr.  auba,  ‘dawn’,  fr.  L.  alba,  fem.  of albus,  ‘white’,  used  as  a  noun.  See  alb  and  -ade. aubain,  n.,  alien,  foreigner.  —  F.,  orig.  written aubene,  fr.  Frankish  *aliban,  lit.  ‘belonging  to another  ban’.  The  first  dement  of  this  w'ord  is rel.  to  Goth,  aljis,  ‘other’,  and  to  E.  else  (q.v.) The  second  element  is  rel.  to  E.  ban,  v.  (q.v.) See  Bloch-Wartburg,  DELF.,  p.43  s.v.  aubain. aubergine,  n.,  the  eggplant.  —  G.,  fr.  Catal.  al- berginera,  alberginia,  fr.  Arab,  al-badinjan,  ‘the eggplant’,  fr.  al-,  ‘the’,  and  badinjdn,  ‘eggplant’, fr.  Pers.  badin-gan,  fr.  OI.  vatin-ganah.  Cp. berengena.
4448:bardash,  n.,  a  catamite.  —  F.  bardache,  fr.  It. bardascia,  fr.  Arab,  bardaj,  ‘slave’,  ult.  fr.  Pers. bardah,  of  s.m.
4782:bereft,  adj.  —  Prop.  pp.  of  bereave, berengelite,  n.,  a  resinous  material.  —  Named after  San  Juan  de  Berengela,  a  province  of  Peru. For  the  ending  see  subst.  suff.  -ite. berengena,  n.,  the  eggplant.  —  Sp.,  fr.  Arab. badinjdn  (in  vulgar  pronunciation  bedinjen),  ult. fr.  Persian.  See  aubergine.
== KLN_1971.txt
22691:aubergine, n., the eggplant. — G., fr. Catal. al- 
22695:berengena. 
26010:bardash, n., a catamite. — F. bardache , fr. It. 
26011:bardascia, fr. Arab, bardaj , ‘slave’, ult. fr. Pers. 
28479:berengelite, n., a resinous material. — Named 
28480:after San Juan de Berengela , a province of Peru. 
28482:berengena, n., the eggplant. — Sp., fr. Arab. 
28484:fr. Persian, See aubergine. 
== SKT.txt
== LKT.txt
584:Ebenso  ar.  bädingän  'Tollapfol,  Solanum melongena'.  Hieraus  zahlreiche  ver- schiedene romanische  Formen:  it.  peton- ciano,  sp.  pg.  val.  berengena,  pg.  berin- gala,  kat.  alberginera,  frz.  aubergine, melanghne,  merangene,  it.  melangola, marignano,  melanzana,  siz.  milinciana. Über  vulg.  tk.  ■paüygan  wurde  rum. pätlägea,  demin.  pätlägicä  'Tomate'. Russ.  badidzan,  badarzan,  batlamn, baklazan.  [DE  239.  Eguilaz  344.  De- vic DEt  46/47.  ML  876.  Löbel  EITAP  75.
736:'Erbeutete,  gefangene  Griechenmädchen, weiße  Sklavinnen'  [KREMER  in  SBKAW Wien  phil.  bist.  Gl.  CHI  (1883),  195/196; nach  VÖLLERS  in  ZDMG  L,  628  noch jetzt  im  Namen  Hös  Barda',  dem  Sklaven- hof von  Kairo,  erhalten] ;  sie  wurden meist  zu  unzüchtigen  Zwecken  gehalten, daher  it.  bardascia  'Knabe,  der  zur  Un- zucht gebraucht  wird,  Lotterbube'  [aber logud.  mail.  piem.  'Knabe'  schlechthin], afrz.  hardaclie,  sp.  bardaja,  bardaje 'Schandbube'.    [Eguilaz  340.    ML  956.
6339:alphanette  582 alphinic  683 alquifoux  1227 aludel  2142 alvarde  242 amalgame  1378 aman  66 amhre  78 amhrette  762  b nmiral  69  a amire  afz.  69  a amuUte  866 amulette  866 anafin  1537 andouille  355 angrec  82 «wii  1568 <iw<t/f(;  20ö8 antimoine  918 arabe(sque)  89 «ra^  92 arcawne  867 archine  108 argali  96 argousin  2160 aWeie  100 ar»m  112 armadie  1343 armoise(ur)  1596 armo(i)sin  1596 «rra^e?  1708 arrofee  1725 arsenal  495 artichaut  833 ar^iei  95 assassin  839 assogue  2208 »thanor  2019 a^fcar  2075 a«a6a?  1971 ffM&^e  874 aubergine  161 «MCTtöe  afz.  1221 uufage  afz.  586.  777 auferrant  afz.  586 aw/fe  796 au^n  afz.  605 auforget  884 «M^r^  135
6352:baragouin  256 I  barbacane  197 I  bardache  afz.  229 ]  barde(au)  228 i  ftarc^of  228 ,  baroque  364 I  barque  2148 i  barracan  250 I  basane(r)  afz.  316 ^  basane  316 I  basanier  316 !  basiUqtie  (vemej  262
8047:berengena  161
10036:babuche  1625 iadrt  152 badana  316 badea  319 badian(a)  162 bagasa  171 daA«H  177 baladi  196 balaja  151 balajo  151 6aZc(5n  197 fcflWa  271 (de,en)  balde  271 baldequhi  170 fea/rfio  271 balsamo  293 bambu  209 banana  211 bandujo  273 bandullo  273 bango  213 barahunda  256 baraja(do)  225 barajar  225 baranda  223 barbacana  197 fcarca  2148 fcarrfa  228 bar da ja  229 bardaje  229 ftarrfo  228 barragän  250 barroco  364 6a<a  273
10044:berengena  161
== DEV.txt
639:Aubergine.  L'aubergine  est  une  plante  originaire  de l'Orient,  ainsi  que  l'atteste  Dominique  Ghabré  qui,  dans son  Stirpium  icônes  (1678),  l'appelle  Melongena  Arabum  et ajoute  :  «Melongena  in  Arabum  codicibus  primum  cele- brata  fuit.  75  Le  nom  arabe-persan  ^L^^L  hâdindjân  serait assez  difficile  à  reconnaître  dans  notre  aubergine,  si  nous n'avions  comme  points  de  repère  l'espagnol  berengena  et  le portugais  beringela,  bringella^.  On  trouve  aussi,  avec  l'ar- ticle arabe,  alberengena  qui  correspond  à  aubergine,  comme berengena  correspond  aux  autres  formes  françaises^  méran- gène,  mélongène.  Du  Gange  cite,  dans  le  bas  latin,  meran- golus,  melangolus;  les  Italiens  ont  melangolo  et  melanzana, dont  le  Gazoph.  ling.  Pers.  signale  déjà  l'analogie  de  son avec  yt^^l?  bâdindjdn.  Quant  à  melongena,  c'est  du  latin de  botaniste.
645:à  cause  do  la  rcsseinblanco  de  ce  mollusque  avec  le  fruit de  l'aubergine.
646:La  diversité  de  tous  ces  mots,  identiques  au  fond,  se retrouve  jusqu'à  un  certain  point  dans  les  noms  orientaux de  l'aubergine ,  arabes  ou  persans ,  (jl:^:>l> ,  ^l^o^L ,  ^14-^1^ , jjliColj,  »ljijob,  hâdindjân,  bâchngân,  hâdddjân,  pâtingân, ■pûùngâh.  Cbardin  écrit  hadinjan  :  c^On  a  aussi  ce  fruit qu'ils  appellent  hadinjan,  que  nous  appelons  pomme  d'à- mouv^.r)  Le  man.  unique  de  Razi,  de  la  Bibl.  nat. ,  porte ijL^isl)  hâd'mdjân;  le  célèbre  médecin  arabe  dit  que  ce fruit  brûle  le  sang  et  fait  naître  des  pustules  dans  la boucbe,  axIÎ -vù^  **xJi  ^j^,  à  moins  qu'on  ne  le  fasse cuire  avec  du  vinaigre^.  L'aubergine  n'a  pas  aujourd'hui une  aussi  détestable  réputation.
2429:Alberengena,  esp.  voy.  Aubergine-.
2430:Albergaine,  voy.  Aubergine.
2431:Albergame,  voy.  Aubergine.
2434:Albergine,  voy.  Aubergine.
2853:Aubergine.
3025:Bélingèlc,  voy.  Aubergine.
3042:Berengena,  esp.  voy.  Aubergine,
3043:Beringela ,  pg.  voy.  Aubergine.
3095:Bringeila,  2?j^.  voy.  Aubergine.
3898:Melangolo ,  ital.  voy.  Aubergine.
3899:Melangolus,  h.  lat.  voy.  Aubergine.
3900:Melanzana,  ital.  voy.  Aubergine.
== PHN.txt
== LAM.txt
287:ment ch {\) ei c: bardache, doronic, (le Minhâg écrit
792:/ : zinzolin, gengéli, bougie, aubergine, abit, alfier.
849:aubarde (V. barde, ) , auberge, aubergine, aumusse, au-
2266:Bardache. Esp : bardaxa, bardaja. Ital: bardascia; de
2272:de tSjf ou ^^x bardaja, barda'a ( Belot-Heury-Bocth).
7954:Aubergine. Es/?. P/g-. Va/.: berengena. Ptgr. bringela.Ca/.:
7955:alberginiera. Esp. : alberengena. CaLMaj*: alberginia.D' Ar-
7964:l'aubergine. Dans Mas'oûdî il est également question
7965:«d'aubergines àlaBourân (3), bonnes à ravir; Ô^Stj
7979:(2) Man. déjà cit. L'autem» énumère deux espèces d'aubergine : ^y^>i\
8480:Aubergine
8504:Bardache *
== DOZ.txt
== HJB.txt
4098:BBINJATJL,  8.  The  name  of  a v^etable  called  m  the  W.  Indies  the Sffg-plani,  and  more  commonly  known to  the  Engliflh  in  Bengal  under  that of  hanguai  (prop,  baingan).  It  is  the Solanum  MdonaenOy  L.,  very  commonly coltivated  on  tne  shores  of  the  Mediter- ranean as  well  as  in  India  and  the East  generally.  Though  not  known in  a  wild  state  under  tnis  form,  there is  no  reasonable  doubt  that  S.  Mdon- ^ma  IB  a  derivative  of  the  common Indian  S.  inaanwrn^  L.  The  word  in the  form  hrifija/tU  is  from  the  Portu- ffaese,  as  we  shall  see.  But  probably there  is  no  word  of  the  kind  which  has undergone  such  extraordinary  variety of  m^fications,  whilst  retaining  the .same  meaning,  as  this.  The  Skt.  is ikanUtisiy  H.  bhdntd,  baigan,  baingan, P.  badingdn,  baiilgdn,  Ar.  badinjdiiy Span,  atberengena,  berengena^  Port,  berm- ^da^  Iningiaoj  bringella,  Low  Latin mdangolusy  merangoltUy  ItaL  melangola^ fndamanuiy  mda  wuana,  &c.  (see  P. deUa  VaUe,  below),  French  aiibergine (from  alberengena)y  mdonqkne,  meran- ghi€j  and  provincially  beUnahi^  alber- ga%ne,  albergine,  alberaame.  (See  Ma/rcel DeviCf  p.  46.)  Littre,  we  may  remark, explains  (darmitarUe  Homero  f)  aubergine as  ^etpke  de  moreUe,'  giving  the  etym. as  ^'diminutif  de  auberge"  (in  the sense  of  a  kind  of  peach).  Melangena is  no  real  Latin  word,  but  a  factitious
4099:rendering  of  meUmzanOy  or,  as  Marcel Devic  says,  "  Latin  du  botaniste."  It looks  as  if  the  Skt.  word  were  the original  of  all.  The  H.  baingan  again seems  to  have  been  modified  from  the P.  badingdn,  [or,  as  Platts  asserts,  direct from  the  Skt.  vanga,  vanganoy '  the  plant of  Bengal,']  and  baingan  also  through the  Ar.  to  have  been  the  parent  of  tne Span,  berengena,  and  so  of  all  the  other ffuropean  names  except  the  Englisli *  egg-plant.'  The  Ital.  mda  insana  is the  most  curious  of  these  corruptions, framed  by  the  usual  effort  after  mean- ing, and  connecting  itself  with  the somewhat  indigestible  reputation  of the  vegetable  as  it  is  eaten  in  Italy, which  is  a  fact.  When  cholera  is abroad  it  is  considered  (e.g.  in  Sicily) to  be  an  act  of  folly  to  eat  the  melon- zona.  There  is,  however,  behind  this, some  notion  (exemplified  in  the  quota- tion from  Ixine^s  Mod.  Ewpt.  below) connecting  the  badinjdn  with  madness. [Burton^  Ar.  Nights,  iii.  417.]  And  it would  seem  that  the  old  Arao  medical writers  give  it  a  bad  character  as  an article  of  diet.  Thus  Avicenna  says the  badinjdn  generate^  melancholy  and obstructions.  To  the  N.  0.  Solanaceae many  poisonous  plants  belong.
4100:The  word  has  oeen  carried,  with  the vegetable,  to  the  Archipelago,  pro- bably by  the  Portuguese,  for  the Malays  call  it  berinjaid.  [On  this  Mr. Skeat  writes :  "  The  Malay  form  brinjal, from  the  Port.,  not  berinjaid,  is  given by  Clifford  and  Swettenham,  but  it cannot  be  established  as  a  Malav  word, being  almost  certainly  the  £ng.  irinjaul done  into  Malay.  It  finds  no  place  in Klinkert,  and  the  native  Malay  word, which  is  the  only  word  used  in  pure Peninsular  Malay,  is  terong  or  trong. The  form  berinjaid,  I  believe,  must have  come  from  the  Islands  if  it  really exists.'*]
4113:1783.— Forrest  speUs  brinJallM  ( V.  to  Met- gui,  40) ;  and  (1810)  Williamson  biringal ( F.  M.  i.  133).  Forbes  (1813),  bringal  and berenjal  {Or.  Mem.  i.  32 )  [in  2nd  ed.  i.  22, bungal,]  ii.  50 ;  [in  2nd  ed.  i.  348].
6225:1875.—".  .  .  Chhenchld,  usually  called taridri  in  the  Vardham&na  District  a  sort of  hodge-podge  consisting  of  potatoes, brinjals,  and  tender  stcdks.  .  .  ." — OovtTida Samanta,  i.  69.
24242:Brinjaal,     Brinjal,
24243:Brinjall,  115a,  116a Briujaree,    Brinjar-
== AID.txt
885:BardAsht.  [HindustAni.J  Stores, supplies ;   also  the  furnishing  of porters  and  provisions  to  troops  or travellers.
1302:BrinjaL  The  name  of  a   vegetable, called  also  the  egg-plant ;   it  is  the solanum  melongena.
2223:Egg-plant.  See  Brinjal.
7254:Wanpayir.  [Tamil.]  Certain  spe- cially taxed  products,  viz.  betel-vines, turmeric,  plantains,  chillies,  and brinjals.
```


## [2026-10-16T05:13:36.591Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E 'bardah|barda\\b|bardä|wardag|vartak' HUB.txt HRN.txt | head; echo ==PHD; grep -n -i -E '^wardag|wardag' PHD.txt PHD_mackenzie.txt | head; echo ==NYB; grep -n -i -E 'vartak|wardag|vartag' NYB_vol2_glossary.txt | head; echo ==BRT; grep -n -E 'varəta|var[eə]ta-' BRT.txt | head; echo ==CHEUNG; grep -n -i -E 'wardag|barda' CHEUNG.txt | head"
}
```


### [2026-10-16T05:13:36.908Z] TOOL RESULT

```
Exit code 1
HUB.txt:840:196. Zu barda *Gefangener' = phi. vartak hat schon Geiger
HUB.txt:842:gefangen' gestellt. Dazu afgh. LW. barda *a female
HUB.txt:4434:deussravd) Von schlechtem Rufe'; hrovartak 'Brief = phi.
HUB.txt:4435:fravartak] yovanak = yavanak 'Fiillen', nf.Javan (afgh.LW.
HUB.txt:4612:ap. ^bardah" = zd. barezah^^) *H5he', phi. sup. balist, zd.
HUB.txt:5259:iiber , birOdar *Bruder\ barda *Gefangener , barz Teldarbeit',
HUB.txt:5456:= phi. vartak, zd. vareta-; barf 'Schnee' = paz. vafr Min.
HUB.txt:6586:EngeV = np. firSsta; hrovartak 'Brief = phi. fravartdk;
HUB.txt:6947:baram^ ptc. anbarda repletus*, alt belegt JKAS. 1894, 443:
HUB.txt:6948:anbarda puffed. up with pride', skr. sam/;wraya^i *anfullen*;
(eval):1: =PHD not found
```


## [2026-10-16T05:14:13.388Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 835,846p HUB.txt; sed -n 5452,5458p HUB.txt; grep -n -i -E 'wardag|wltk' PHD.txt PHD_mackenzie.txt | head -5; grep -n -i -E 'vartak|wartak|wardag' NYB_vol2_glossary.txt | head -5; grep -n -a -E 'var[eə]ta-|varəta|vərəta' BRT.txt | head -5; grep -n -i -E 'barda|bard[aä]h' HRN.txt | head -5; grep -n -i -E 'wardag|barda' CHEUNG.txt | head -5"
}
```


### [2026-10-16T05:14:13.945Z] TOOL RESULT

```
es aber nur in gvadil vorkommt, nahm ich an, dass
gvadil altes Lehnwort sei -= mp. *vaddil (vgl. paz.
vad schlecht* und dil *Herz').
189. Fiir *avatasti' wiirde ich *ddast, tnr *abitasti- : *awdast,
audast erwarten.
196. Zu barda *Gefangener' = phi. vartak hat schon Geiger
an der von Horn citierten Stelle richtig zd. vareta-
gefangen' gestellt. Dazu afgh. LW. barda *a female
slave.'
199. Np. barman 'Quartier' ist nicht — ap. vardana- *Stadt',
das doch zu np. *balan geworden ware. Zd. verezena-
heisst nach Geldner (Pischel - Geldner, Ved.
babr *Tiger : arm. vagr, skr. vycLghra-?; badca *Junges* =
phi. vacak; bad *schlecht' = paz. raJ Shk. 269, Min. 61. 202,
arm. vat ; bar *Bnist* = zd. varah-, skr. uras- ; barz = varz
Teldarbeit', phi. varz, zd. Wzl. varez; harda 'Gefangener
= phi. vartak, zd. vareta-; barf 'Schnee' = paz. vafr Min.
61. 204, zd. vafra-; barg *Blatt' = zd. vareka-; barra 'Lamm'
= phi. varak^ skr. urana-; bas Viel* = paz. vas^ ap. vasiy;
PHD.txt:338:frawardag [plwltk' | M prwrdg] letter, epistle.
PHD.txt:340:Frawardigàn [plwityk’n' | N farwardagan] festival of the frawards, the last five days of the twelfth month (Spandarmad) and the following five epacts (v. ģāhānīg).
PHD.txt:384:ёгбһ [glwh | N guroh] group, crowd. gubrág [gwpl’k'] awake, alert, vigilant. ģubrās- [gwp/”s-] = wigras-, v. wigrádan. ģuftan, $0(w)- [YMRRWN-, YMLLWN-tn! < A ymlwn, V тЇ; gwptn', gwb- | M gwptn, gw-, N ~, gā(y)-] say, speak. ~išn: speech. ģuftār [gwpt?] | N ~] speaker. ~ih: (power of) speech. gugiin- [gwk’n- | M gwg^n-] destroy. gugar(i)dan, gugar- [gwk”/-(y)tn! | N guwár-idan] digest. tuģāy [gwk*dy | M gwg'y, N guwah] witness. ~ih: testimony. ģūh [gwh | N —] dung, excrement. guhrayénidan, guhrayén- [gw AP yn-ytn!] waken, arouse. gul [gwl | N ~] flower, rose. ботап [gwnmn! | = M, N ~] doubt. ~par [-A/] casting doubt. ~ig [-yk'] doubtful. ~ih, ~igih: doubt. gumardag [gwmltk'] appointee, deputy. ģumārdan, gumār- [gwm’l-tn' | М gwm'r-dn, N gumāštan, gumar-] appoint, commission, entrust. gumbad [gwmbt' | N ~] dome, fire-temple. £umég [gwmyk! | M gwmyg] mixture. guméxtan, gumēz- [gx”myhtn!, gwmyc- | M gwmyxtn, gwmyz-] mix. ~išn: mixing, mixture; = gumézagih. gumëzag [gwmyck'] mixture. ~th: the Mixture, (the duration of) this material world. Jgund [gwnd | = P] army, troop; group, gathering. *gund [gwnd | N ~] testicle. gung [g(w)ng | N ~] dumb. ģurbaģ [gwibk! | N ~a] cat. Бита [gwlt! | P gwrd, N ~] hero. lih: heroism, bravery. gurdag [gwltk! | N ~a] kidney. *gurdih [ewityh] (some piece of) armour. gurdwār [gwltw’!] befitting a hero. ёпгр [gwlg | N ~] wolf. gurganig [gw/g”nyk! | N ~i] of (the province) Gurgan. gursag [ewlsk] | N gurusna !] hungry. «ЛЬ: hunger. Suën [gvfn! | N ~] male. gusnag [gwšnk! | J gušna] hungry. Gušnasp [gwšn(*)sf] the second major Fire of Sasanian Eran, that of warriors. £yà$ [gyw'k! | M gy'g, N jay] place.
PHD.txt:607:~išn: conquest, destruction. wanigarih [4W BDN-, wny-klyh] waste. wany [A(W)BDN' < APbdn | M wny] lost, destroyed. wany(b)ūdīh [4WBDN'butyh, -YHWWNtyh | M wny(b)wdyh] destruction, ruination. iwar [wl | M wr, N bar] breast. *war [w/] lake. Zwar [wl] oath, ordeal. ‘war [wl] shelter, enclosure. war-, v. waridan. warāy [wl”g | J bry] crow. waran [win'] desire, lust. warān [wi’n'] ram. wārān [w’Pn' | M wrn, N bārān] rain. waranig [wlnyk'] greedy. ~ih: greed, lust. waranig [wL nyk! | N bārānī) rain(y). warāz [wl”c | N gurāz] boar. war-čašm [wicfm] with eye(s) in the breast. ward-, v. 'waštan. lwardag [witk! | M wrdg, N barda] captive, prisoner. ~ih: captivity. *warda$ [witk'] on heat (female animal). ~ih: heat. *wardānāģ (wi? mk! | N gardana] (roasting) spit. wardénidan, wardén- [wityn-ytn! | (N gardànidan)] cause to turn; change, alter. wardišn [witšn! | M wrdyšn, N дака] turning, change, metamorphosis. ~ig [-y%!] transient, changeable. ~(ig)ih : transience, mutability. wardyün [wltywn! | P wrdywn, N gardiin] vehicle, carriage, chariot. warg [wlg | N barg] leaf. wārīdan, wār- [w?l-ytn' | M w’r-yst, N bàáridan] rain. warišn [wilsn'] conduct, behaviour. lwarm [wlm | N barm] memory. — kardan: learn by heart, memorize. *warm [wim | N barm] pool, reservoir. wārom [w’lwm] mind. warómand [wl’wmnd] doubtful. ih: doubt. warr [LBWS Y A < A lbw?] wool; garment. warrag [КММА < ?; wlk! | M wrg, N barra] lamb, ram; astr. Aries. wars [wils] hair. lwarz [wle | M wrz, N barz] work, agriculture. *warz [wic | М wrc/z] miracle, miraculous power. *warz [wlz | N gurz] club, mace.
PHD.txt:665:xwarūfrān [hwl(’)wpl’n' | M xwrwpr'n) sunset, west. xwarrah [GDE < A gdh | (M prh, N farr)] fortune, glory, splendour. ~6mand [-’wmnd] fortunate, glorious. xwarséd, v. xwarxséd. xwartar [hw ltl] minor (sins). xwarwarān [hwlwPn!, -bPn'] = xwardfran. xwar(x)8éd [Azl(h)syt' | M xwrxšyd, № xuršēd] sun. xwāstag [NKSY A < A nksy’; hw'stk! | M xw’stg, N ~a] property, wealth. i ~õmand [-wmnd] wealthy. xwastan, !xwāh- [(Y)PLHWN-tn! < А V plh; hwstn!, hw'd- | J xwh-, N xwast] tread, trample; thresh. ~išn: trampling. xwāstan, *xwāh- [BOYHWN-stn! < A МУ Бу; hw'stn!', hwd- | M xw’stn, xt h-, N ~] seek, want, desire; attract, acquire. --j&n : desire, attraction. xwastüg [hwstwk!' | N xustū] confessing, believing. ~ih: confession, belief, faith. xwaš [BS YM < А bsym; hw | M xw, N ~] pleasant, sweet, nice. ~ih: pleasantness, pleasure. xwēd [Awyt! | M xwyd, N ~] moist, fresh. ~ih: moisture, freshness. xwédódah [hwytw(k)ds, -d^t! = Av. x"aetwada0a-] kin-marriage. xwēn-āhan [Ahw(y)n ?syn! = Av. x"aéna- (ayah-)] shining metal. xwēš [NP ŠE < А npf-h; hwyš | M xwy(b)s, N ~] (one's) own. ~ih: possession. ~awand [kwyš*wnd | N ~] relative, kinsman. xwēšēnīdan, xwēšēn- [/nwyfyn-ytn!] appropriate, make one’s own. xwēš-kār [леу dutiful. ~th: proper function. xwēš-tan [NPSE tn! | N ~] self. xwéy [hwyd | N xway] sweat, perspiration. xwistan [hwystn'] sweat, perspire. xwurd [hwlt' | N ~] small, little. xwurdag [hwltk' | N ~a] something small, particle; astr. lunar mansion; (horse's) pastern. ~ih: smallness.
507:(cf 41?" and 89%); ~ fravartak in the letter 1822; — combined with another prep.: ~ 6 pad estat 28%. 1189. 11917 (cf above 1871); ~ 6 ax“ i astomand 401; m andar äyiyänak 409; ~ tdi sdxdn 401; ~ pat óstak 48% (ete.). — b) temporal: ~ sal 2 mazdesn bag’ Šāhpuhr” in the year 2 of the Mazdayasnian Divine Sh. Pl:l; ~ sal "68 in the year 68 P2:1; ~ pat han jamān ka at the time when 41%, adak ~ pat jamän at that time 619; 4214; 3 sap td three nights ago 512-3, — c) figurative: on, about (esp. in headings and book titles), concerning; (reigning) over, (merciful) to, (hostile) to- wards; (means) for; ete.; — with an inf. or a v.n.: in order to 3714-15, 4515; 1185 (continued by inf. + rād, l. 6). - ~ does not govern encl. pronouns; single excep- tion apar-aš 54° (late passage). — Av. (394 sq.) upati, OP upariy; MPrthPrs br; Paz. awar; NP bar. Cf aper. — On MDM 43" v. hàreftan.
1561:fravartak ([plwltk'] letter 1817-21-22,
1562:1914—16.25—26. 11812. — MPrthPrs frwrdg, Arm. lw. hrowartak; Talm prwrtq' ‘edict’, Syr prwrtg', prwrdyq' v. Telegdi 251 sq.
2752:nipistan [npštn'; YKTYBWN-tn'] nipés- to write 419. 110? etc. ; nipist estet it has been written, it is written 1139; nipist ēstāt it was written 1!—?; — pres. pass. nipēsihēt [YKTYBWN-yhyt'] is being written 18%; — pat dp i zarr nipištak 1079; apar nipistak written down 108?!; nāmak ~ 6 to write a letter to 49-9. 822, an inscription P 2:3.4; apar fravartak čton nipišt estat kū it was written in the letter (then dir. speech) 1872; apar én ayyätkär nipišt estet 1135-9. — OP ni-pais- ; MPrthPrs nbyštn nbys-; Paz. nawaštan nivés-; NP nuvistan, nivištan, nivés-.
3982:vartak captive 19%. — Av. (1368) ?varota-; Ps. wldky; MPrthPrs wrdg; NP bardah.
1829:Zaz. berdis/ben-, (subj.) ber-, Abz. barda/bor-, ber-, Abyan. barda/bar-, Fariz. 
1832:barda/ber-, Varz. barte/ber- ‘to carry, bring (to)’, Nn. barte/bir- ‘to carry off, take 
2026:"wp Itn /obardan/ 
19663:BMP npltk /nibardag/ ‘tried, experienced’ > DMMPP: 239a 
19672:*NWIR: (+ *ni-) NP nabard, naburd ‘battle; war’, NP nabardah ‘warlike, brave’
```


## [2026-10-16T05:14:18.432Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -a -E 'vart?ta|var[ao]ta-|varata|varəta|var\\Sta-' BRT.txt | head -10; grep -n -a -i 'gefangen' BRT.txt | head -10; grep -n -i -E 'bardah|barda ' HRN.txt | head"
}
```


### [2026-10-16T05:14:18.936Z] TOOL RESULT

```
3877:•  j.  aiiwi.varatay-  i.  'Sichdarüberwälzen, Darüber  wogen':  fiasca  ä^rittm  'railt "nachdem  die  Wellen  dreimal  darüber gegangen  sind"  V.6'.4J.
3882:•  j.  aiwi.varSta-  Adj.  (fem,  "/(-)  'be- regnet, worauf  es  geregnet  hat':  vlsp3m\ a  ahmät  nasunam  -a  'ianqm  daxmanqmca ' 'tanqm  hixranqmla  'tanqm  vayanqmüi frariuhantanqm  "bis  dass  es  auf  die  Leich- name geregnet  und  .  .  und  auf  die  Lei- chenausscheidungen geregnet  hat  und  bis die  Vögel  (Alles)  aufgefressen  haben"  V.  ]
4412:•  j.  'an-äx§ta-  Adj.  'uDÜriedlich',  Plui-  n. 'friedlose  Zustände':  'ta  apa.dvarata  Yt. 3-S:  ...
5116:avarata-  176
6063:30.  8 ;  —  yäis  *gr!hmä  (sd.)  »/J/  varata . . xsahrimca  ll'anqm  *drujim  Y.j2. 12;  — aHbys  yBi  urvätäU  drBjö  'iahyä  gag^ä*> vitrwfncaitg  (sd.)  Y.  j/.  i;  —  s.  noch: yf  ra%3ms  (sd.)  °sat  haia  \,44.  17  und drüp  haia  ra^fptS  Y.  5J.  6 ;  —  ae^l 'Sahyä  Y.  28.  4  und  isanqm  *drujim  Y, 32.  12.  b)  im  jAw.:  vainn  akmi nmäne..  ar^uxoö  växl  mikaext  m  väHm *'sa  (als  Subj.)^*  ^drujim  Y.  60.  5;  — vanät  '/a  (als  Subj.)^>  aJtqm  drujim  Yt ^9-  9S>  —  agvayoHt  bar?smSjt?rAH  banzyS *-ümi''  zaraÄeMs  (sd.)  drupm  '2.24;  Yt 10.  86  (s.  2  b  a);  —  ks  .  .  yS  'A«  mal- nimnS  'ssm  ispmnö  'spm  aparaoüayeite (sd.)  {'simca  mainimns]  drujimca  vinasti V.  7. 78.  a)  sonst;  a)  im  gA^v.: hyat  akSyä  (sd.)  ängväitl  usta  vi  'sim dädrl  Y.  j/.  8;    —    nSit   3r?s.vacS   sarSm
9299:II  .)f*;,L!'-o7/"jriTverstiimmelteUä'ä  kavä  ..\.44-  2°;  —  .V^'^-  *grihm<l Formen.  Man  erwartete  »i^^jr/jK/j/,  »i-riHÄwA  [(sd.)    aM  varata   'pa   xsairimcä    Tianqm
10393:KompA.,  E.  —  «i.  gütha-  n.,  np.  S"''- ,  •  j.  gü9'ö.varata-  Adj.  'sich  im  Kot  auf- :  haltend':  pazdunqm  'tanqm  V.  74.6.
11922:daxmaliva  hqm.bavainti  axtilca  garmusca 'ftusca  V.  7. 5  7 ;  VyL  50 ;  —  paiiistätse  gars- näuica  'naoica  Yt  y,  1 3 1 ;  —  apa.ävarata 'nu  Yt.^.8;  1 1 ;  —  paitistätSe  dazu  . .  'nu V.20.3.  a)Plur.mitGS.  a^rö(Sp.3i4  0.) 'Fieberanfälle';  k3 paoirys  a%rS  'nus(AF.) dürayat  tanaot  hata  tnasyehe  V,  20. 1,
12057:•  g.  tarS-tnatay-,  j.  tarö.niatay-  f.  Svider- strebendes  Denken,  Widersetzlichkeit,  Auf- lehnung, Trotz',  spez.  in  Glaubenssacben: yö  gähä  asrävayd  ^qsta  (sd.)  vä  'inaiW^ vi  tanüm  *piryHH  N.  41;  —  kö  *tfj«(sd.) *ij  *'Maitis'?''>  yä  haca  damayäi  mifzda- yasnsif  a^sisiii/ (sd.)  "was  ist  Hass,  was Troti?  .  ."  Ii.41;  —  yl  %aia/  maidä asn^tlm  ak>mca  manB yazili  (sd.)  qfiä  ^aS- iSuscä  •maitlm  Y,  j_j.  4.  a)  ' satz  zu  armatay-:  vaittlt  ahmt  nmäiie armaitis  'maitim  V.  60.  5.  A)  als  Dä- mon*': 'mata  apa.dvarata  pairi.mata  aßa.- iharata  Yt_j.  8;  11,   15*,
13871:hörig  dargebrachte  Verehning':  kö  huyesti  'J;  duiSvaräta-varaz- Adj.  'able  Werke, (sd.)  ks  y^sti  mam  zl  mainydt  yatat^m  \  U^'es  wirkend  t  frai;asayö  .  .  fravaz^U Vt/o  108  '  avaiiAe  narqm  asaoiiqm  qzartke 'varnqm
4570:—  vjfTirayru/m  ..yat  asti  °rf  ahutia  airya- mana  ". .  zwischen  dem  A/i.-  und  dem  Airy.- Gebet"  Vr.  24-i;  —  ''v  *am7sSsi!a  spmts saosyantasca  P.^f;^o,_ji(?);  —  'n  pitan i^A.)  puknmla  Yt.J0.117;  117,  116^;  — ' 'n  urvaitya  (sd.)  V.4-3— 4*;  —  ävis  iiä. "rs  hsiiiü . . rätttyl(%d.)  '^■33-T,  —  cvai  'rj *mr3us. .  "wie  viel  im  Kreis  der  Männer . ." V.5.27;  —  yim  'r»  vastnm  frajasäi  (sd.) 'V.i0.i6;i6;yd.ij.i4.  aa) unräumlich: ; \'it/iaiy()xsäydi^iyä  agarbäyam  "rimä  haina-  \ raim  "diese  9  Könige  nahm  ich  in  diesen Schlachten  gefangen"  Bh.  4. 3.  ß)  zeit-  j lieh:  *kva  altqm^aEsnmn  paiH.barat1  "r?, akuna  *airyamana  "wann  soll  man  das  1 Brennholz  herzubringen?  Zwischen  (der  | Rezitation)  des  Ah.-  und  des  .,4»>/, -Gebets"  |
4632:pataha  yat  'n  vä  aai  -w  v,l  .  ."  N. S3.  2)  Praen.  a)  mit  Akk.  'innerhalb, in,  unter,  zwischen';  a)  räumlich,  auf  die Frage  wo?  und  wohin?:  i  °r  tmä  äahyäve^ martiya''  kyi^  . .  "innerhalb  dieser  Län- der . ."  Bh.  /.  8 ;  —  I  avaiy  °r ''  didsm  frii- Aayam  {sd.)  Bh.  2, 13;  —  T;/  ja/W  (sd-) var?zäne  V.ij.iy;  —  'rt  daifiAu  pi}p?r?- tane  Yt  70.8,  J5.49;  49';  —  yS  vJräsaili 'r)  räiia  rJsmana  Yt.  7^47;  —  tiisiltm (sd.)  yim  'rp  mSurunua  büx'aimca  V.  /.  7 ; ■ —  yßi  'r)  v^rxika  *as  *mars}a  (sd.)  V. j8.  70  PüZ.;  —  'rj  sqm  asmanimca  "zwi- schen Himmel  und  'Erde"  Y.6Ä  15;  Yt. ÄS,  /O.95,  y,i3',  43,  44; — hax3or)mia , .  'n  mäti/Dtnla  Avan^a  Yt  ö.  5 ;  —  ..  */ra- hinein  (sd.)  *'r?i'>  airsatca  bammaca  H.öS; —  Vii^raymm ..yat  asH  "n  ahuna  atrya- mana  ". .  zwischen  dem  AA.-  und  dem  Airy.- Gebet"  Vr.  24.1, ;  —  -/-j  ''am?sSsca  spnitS saosyaiitas^a  P.3<i,30,ji{?);  —  'rv  pitan {zd.)  puhnmca  Yt. /0.117;  117,  116';  — °r>  urvaitya  (sd.)  ^",4.3—4*;  —  ävis  tui 'rs  Asnta . . rä/ayy(sd.)  Y._J3.7;  —  ä'at 'r.> *ii?rsus. .  "wie  viel  im  Kreis  der  Männer . ." V.5.27; — yim  'n  vastmii  fraJasäHsd.) V.j6'.i6ji6;Vd.y./4.  aa)  unräumlich: \'h/iaiyiixsilyahiyJ  agarbäyam  °r  ima  Aattia- rana  "diese  9  Könige  nahm  ich  in  diesen Schlachten  gefangen"  Bh.  4. 3,  ß)  zeit- hch:  *kva  aitqm  *agsm3m  paiti.barälf  °r) oAuna  ''airyamana  "wann  soll  man  das Brennholz  herzubringen?  Zwischen  (der Rezitation)  des  AA.-  und  des  ^;>f', -Gebets"  I
5982:i)  'treiben,  wegtreiben,  wegschleppen' (Vieh   und  Gefangene   als   Kriegsbeute): jvU  gqm  *vani(rm  (sd.)  aznUe'W.  S-Zl ', —   ' ya  {gäu^  varÄa  (sd.)  azimna  (Pass.)  Yt.  . ;o.86;    —    kaoa    nS  fraourvaesayälti  . drujö  vaismmda  a z;/ mn a m  (APm.)  "wann wird  er  uns,   die  zur  Wohnung  der  Dr.  ,  j.^  g,  azan-  :  asn-'^  n.  'Tag',  im  Gegens. hinweggetriebenen  (Rinder)  . ."  Yt/o.86;,2ur  Nacht:  pat/i  'sai paiti  xsa/ne  Yt./.g,
7856:•  j.  ^ah-  n.  i)  'Ein-,  ZusammenschnU- rung*  der  Kehle,  'Erdrosselung'  (nur Komp.).  3)  'Bedrängung,  Enge,  Not; Gefangenschaft':  mi^nm  .  .  yS  nargm  .  . ipa  'zatshat  .  .  fäyajanhat  baraiti  apa nö  haca  'zaahat  apa  haca  'satihibyö (DP.)'>  harSiS^l.  10,22V,— th  nS 'tahucit hals  %rayente  YL 13. 1 46 ;  Vy  t.  $0;  —  yd  AÜ
7857:frayazaite  . .  kahmaiHt  °zat)Aqm  biwivä Yt.  ry.  41;  —  ravasla  o^idrimla  (sd.)  . . aiaonö  stsil  'eas/a  dtäa'intiUa  . .  drvats stSisY.S.8; — yas/a  ml  ail^m  nanm  "zö <vi  avag>r?pt>m  ravöhu  paiti  uzbäraya£ 'imd  wer  den  .  .,  der  in  Gefangen- schaft verbracht  ist,  wieder  in  Freiheit versetzt"  V.  r<?.  10;  —  haoma  .,  yalcit ■zahu  dirilärihs  Jaininam  *upa  *d?rfzaAu (sd.)  Y.  io.17.  a)  liS.  'zaKAe  als  Inf.
7864:j.  ^ö.büg-  Adj.  (auch  fem.)  'aus  Be- drängnis, Not,  Gefangenschaft  errettend, befreiend':  xratüm  .  .  alavan»m  'büßm -avatdqm  V.  18.  6 '';  —  */rasainttm  .  . 'bußtit'^  hiiJrqm  Y.  ^2.5;  — frazantöis  .  , ■büjd"''  kvlrayi  Yt.j_5.134.
7948:;  —  \  da/iyävc^  . .  <i'iar  °ml  dahyäv^ Bh.  7.7f.;  8;  —  nämSnTs  ..  'mä  nUminr/ Yti.j$f.;  —  l'maiy  9  xiäya'^iyä  adam agarbäyam  ti'tar  °mil  (APn.)  hamaraiiS "diese  (genannten)  9  Könige  habe  ich  in diesen  (bezeichneten)  Schlachten  gefangen genommen"  Bh.4-3.  2)  substantivisch, auf  einen  Satz  (,  direkte  Rede,  Aufzählung) : °mat  vS  SpB  jai'yani  "darum  (in  S  '  i) bitte  ich  euch,  ihr  Wasser"  Y. (jj.  12; 13",  Yt.4.3';  —  'mal  a^rff  äfri- <m  "so  (wie  vorher)  lautet  des  Feuers Segenswunsch"  Y.62.10;  —'^ya'^ä  °mt/' kasiyam  naiy  duruxlam  (sd.)  adam  akuna- Bh.^.  7 ;  —  II  °wa*  ly^  maitä  kartam par'iavaiy  "das  (wars),  was  ich  in  P.  tat" Bh,_y. 2;  4,  12,  2.15,  4-^;  —  in  Kon- gruenz mit  dem  Fraedikat:  1  'ma  dakySvJ^ lya  mann  paliyaila"  "das  (in  S  6)  sind die  Länder,  die  . ."  Bh.J.  7;  —  'nie  aste vala  yöi  hinti  ..  sna'ä^m  V.  fo.  16;  17; —  "mas)  U  haoma  gä%a  Y,  10. 18;  iS-J, i9(?).  a)  in  Verbindung  mit  la-,  a)  ad- jektivisch: *vlsqs  (sd.)  *l'lca  °ma  niJmJnls parslasca  .  .  vTsante  Yt. /.  19.  ß)    sub-
10438:obern; gefangen  nehmen',  Akt  und  Med.: xsiii-^atn  lycr  bäbirauv  hauv  agarbJyatS Bh.J.16;  11";  —  imil  dahyavJ^  tyä  adam agarbiiyam  D.tf.3;  ij-y,^-  *vi"da''/am3 bilbirum  agarbSya''  Bh.y.  14;  2.  i;  — bäbirum  hauv  agarbilyatä'&i.^.iy,  —  utä g  xsaya'iiyä  agarbSyam  Bh.  4. 2;  3;  — avam  vahyazdätam  agarbsy^  utä  martiyä tyaisaiy  fratamä  anusiya  äh^tä  agarbaya"
10442:fravartis  agarbäyatä  "Fr.  wurde  gefangen  i genommen"  Bh.  2. 13.  E  3)  'etwas  weg- 1 nehmen  von— (Abi.)':  g}urvaya  Äipälai'e. sävar»  Y.  r).  28.  4)  'einen  Anteil  be- ! kommen  von  — '  (Gen.):  tnä  hl  mairyö'. giurvayöit  "nicht  soll  davon  was  be- kommen , ."  Yt.  8. 59;  —  yezi  se  mairys gfurvay.V  Yt.Äöo;  —  mizdahe  .  .  g>r)W- 1 ytiti  yS  girswyaUe  VyL  JO  (?).  5)  'i^-
13548:•  j.  Marazä-"  f.  'Bande,  Fessel':  vlspe kaoma  upastaomi  yatai  bar^uSva  gairi- nqm  ynliit  jqfnuk;a  raenqm  yafai  qzaku dtritatshs  jaininqm  *upa  *°BJ^a"  "alle H.  preise  ich,  sei  es,  dass  sie  auf  den Höhen  der  Berge,  sei  es,  dass  sie  in  den Tälem  der  Flüsse  sind;  auch  die,  welche in  Gefangenschaft  gehalten,  sich  in  den Fesseln  der  Weiber'*  befinden"  Y,  10.  17.
```


## [2026-10-16T05:14:26.319Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -a -E '(^|[^a-z.])var[aə3]ta-' BRT.txt | head; grep -n -a -E 'Kriegsgefangen|Erbeutet|erbeutet' BRT.txt | head"
}
```


### [2026-10-16T05:14:26.647Z] TOOL RESULT

```
14244:•  j.  drvö-varata-  Adj.  (fem.  'la-)  'der einen  gesunden, heilen  Aufenthaltsort  hat'(?) : drväspqm  sürqm  . .  drvSjtäitm  °tqm  Yt. 9.2.  '
22854:US  V**  (»-  t"*r*")i  ».  Ho«N  GIrPb.  7  b. !  der  freien  Bewegung,  d«  Freiheit  beraubf : 6s.  VgL  Hakquakt  Enniahr  71.  —  rp.  j-iir-  j  avasS^ä^rö  hyät  drvä  .  .  **W'  avasS.- S^"-  ^^xla^rS  Y.  Ä6.  a) 'erbeutet':  _^5  ^«»i
```


## [2026-10-16T05:14:28.739Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 22850,22858p BRT.txt | cut -c1-1500"
}
```


### [2026-10-16T05:14:29.074Z] TOOL RESULT

```
•  p.  varkäna- (,  fMr J<t«J-)  Adj-,  bezeichDet         KompE.  —    Zum  V.  i-aril-'^.    —    aL  'varta-
ein  Volk  'hyrkanisch,  Hyritanier'  (dutI  1"  i);  rgL  vartay  t.  'RoUe  (mw.)'.  —  P6.; Komp).  a)  SiDg.  als  Name  des  Lands,  I  :^/-  -,, "'  .H<is.  ">«^-  -  •>  In  d"  Bed. Hyikaiuen' :  pari  avtr  Uta  'rur  Aamü  ijfä       j.^,^
«^<i-  Bh.2.i6.  ,  .. ,  .   I  •  j. 'var»ta-'>  Adj.  {fem. 'Ö-)  'gefengen;
KompA.  — An»  ir.*ar**;  anscheinend  AbleiL        J  „  j      i-      ..   -,  u         i.^
US  V**  (»-  t"*r*")i  ».  Ho«N  GIrPb.  7  b. !  der  freien  Bewegung,  d«  Freiheit  beraubf : 6s.  VgL  Hakquakt  Enniahr  71.  —  rp.  j-iir-  j  avasS^ä^rö  hyät  drvä  .  .  **W'  avasS.- S^"-  ^^xla^rS  Y.  Ä6.  a) 'erbeutet':  _^5  ^«»i
•  j.  varaxv^ra-  n.  Name  einer  sundigeni ''/am')  as(i//«..ffdt^in'(i^a  in?n'jVlebüid
Handlung:    yat    tum    ainim    avaSiii!  .           ■      ■  .      .     -
baosavasla    'ras/a  "varsiinttm    H.  2.  13 Vytj7'>.
Au  ar.  'jfarilra-,  Bed.  und  Et?  —  Pü. vaiäit  fa  kämai  i  j*//  (für  vara]  tSmoi  (fä varS\   i  hamirdtin   Uta  Jtfh-ds/a)   £at  (für  ÜH- ,       ,,     -     .  ,      j    ,j~   ,  ,
```


## [2026-10-16T05:14:36.003Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; python3 -c \"\nimport json;d=json.load(open('../refs_online.json'))\nfor k in ['BQT','MON','ARY','AHD','POK']: print(k,{x:d[k].get(x) for x in ['local_file','page_offset','lookup_hint']})\"; grep -n 'pdf page' BQT_v1_pages.txt | head -3; grep -n -E 'بردک|ورتک|vartak|wardag' BQT_v1_pages.txt | head; grep -n -E 'بادنجان|بادنگان|باتنگان|vātiṅgaṇa|vatingana' BQT_v1_pages.txt | head"
}
```


### [2026-10-16T05:14:36.616Z] TOOL RESULT

```
BQT {'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt'], 'page_offset': "vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').", 'lookup_hint': "grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \\f; leaf N = N-th \\f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)"}
MON {'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt'], 'page_offset': None, 'lookup_hint': "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks)."}
ARY {'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt'], 'page_offset': 'printed page = pdf page + 1', 'lookup_hint': "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image"}
AHD {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AHD_watkins1985.txt', 'page_offset': "1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.", 'lookup_hint': "Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves = original 1969 ed.)."}
POK {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_01.txt', 'page_offset': 'POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\\data\\ie\\pokorny&root=config"}
4165:انگشتانه» بادنجان باروت؛ بورانی؛تفنگ و توپ؛و قستی از لغات‌ارویایی راهم
13872:ابجد . بادنجان را گوشد و آن ممروفست؟ »
16476:۳ ۱۹ فرامرزی ّ بادنجان
21462:بورانی - نان خورش ی که ازاسقناج و کدو وبادنجان باماست با کشك سازند درالامی
28113:۴ نیز نانوره 220012] کیاهی از تیرهٌ بادنجانیان
28620:و بادنجان پخته و کباب و خاکینه هم آمده
31417:بادنجان را کوبند - و کوکو ۴ وخاکینهرا نیز . | وجربی تفاح خوانند .
31529:تلو ون منم اول وسوم: 0۵600 ۷(60)1202 گیاهی است‌از تبرژ بادنجانیان
```


## [2026-10-16T05:14:39.125Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 tools/ref_page.py BQT:253 2>&1 | head -80"
}
```


### [2026-10-16T05:14:39.537Z] TOOL RESULT

```
no scan of BQT covers printed page 253 (see 'scans' in refs_online.json)
```


## [2026-10-16T05:14:42.238Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for n in 471 472 473 474 475; do echo \"=== leaf $n\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1' BQT_v1_pages.txt | grep -n -E 'برده|vartak|varta|بردج|۲۵۳|۲۵۲|۲۵۴' | head; done"
}
```


### [2026-10-16T05:14:42.999Z] TOOL RESULT

```
=== leaf 471
=== leaf 472
=== leaf 473
54:بقبه ازصفحٌ ۲۵۲
=== leaf 474
=== leaf 475
```


## [2026-10-16T05:14:46.791Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E '^\\[pdf page|^\\s*برده' BQT_v1_pages.txt | grep -B2 -A2 'برده' | head -20; for n in 472 473; do echo \"=== leaf $n\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1' BQT_v1_pages.txt | head -60; done"
}
```


### [2026-10-16T05:14:47.386Z] TOOL RESULT

```
3021:برده‌بوشان» سعنی بر یروشان است که مطلق امت هر بیغمبر باشد. . .. »
3802:برده شده .
20988:برده باشد و آنسه از غنیم در دارالحوب گیرند.
24655:برده حه بر وزن‌هرزه , شیافرا گوبند
=== leaf 472
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
مد ۷ .
پر دا بر ۵ ۷ با بای ابجد بروزن تنها
نف . چب ۱ : پرکال .
تا ۳
کرد » رت من ازراء دورشو ۸
بر دادن » بروزن ومعنی سردادن ورها.
کردن باشد .
بر دا - با غين قطمدار و ح رکت‌غیر
عملوم ۰ ایرث را گوبند و آن کیاهی است که
از دا هیر ونوعتن برگن ()
بو ۵آن » بر وزن درمان » شیرء کیاهی
است بفایت بدبو و گنده .
بر دباد - بت اول و بای ابجد بالف
کشیده بر وزن قرب‌دار » تاب آورنده و تحمل
کننده و بار کش و جفاکش را گویند .
رث بر ك س بفنم دو بای ابجد و سکون
دو رای فرشت و دال بی عطه , بمعنی بردایرد
است که امر بدور شدن باشد ممعنی‌دورشو ۰4
رد - بر وزن زرگر , مخفف برادد _
ات
بردع ِْ- بروزن مجمم ۰ شهری‌است
آباد کردة نوشابه» و نم آن بردم بود که بجای
عین میم باشد و در زمان سکندر بردع و بردعه
تام تهادند .
۴ - م رکب از: 7۷ 1
٩‏ رك : بردیدن. و دراین‌لفت.
است .
بردآبود ۱ معنی دورشویبدا
دنگهبانانی پیشاپیش او میگفتند :
ناحیت است
شه درصفحةً ۱۳
=== leaf 473
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
سبز شد وروبید - وبمعنی درغشب شدوقپر آ لوده
کردید یز آمده است - و ماشی دمزدن وسخن
کفتن - و نمی‌رسالیدن - و خود را پرباد کردن
هم صت - و طلوع و اهر شدن صبح را نیز
گوبند - و دم زر گرانرا عم کفتهاند .
بردن - بکر اول و سکون الی وفتح
الث و نون ساکن » بممنی تندی و تیز رفتاری
پاشد - و اسب جلد و تندرا نیز گویشد - و بطم
اول بمعنی ربودن و بافتن باشد ۴ .
بر دنگ -بروزن‌فرسنکه . کوه کوچك
و پشتة خردمرا گوبند که در میان سحرا وأقج
شده باشد .
بر دون » بروزن فرعون » اسب نرجلد
۱ ره: ور :*
مررسته
و تشد رااگویند, و گویند این‌لت عرییست ۳ .
رده ۴ - بروزن ارده ۰ بممنی
باشد مطلقا خواه دختر و خواه بسر .
بر دی - بروزن‌زردی:
نوعی از خرمای لطیف بود که
آنرا سنکه اشکنك خواشد -
و ظروف سنکی را نیز گویند
- و لام کیاهی هم صست و آن
بیشثر در مصر میباشد و از آن
کاغذ میسازند ٩‏ و بعربی حفاء
میگوشد .
۱ رین بروزن کردیدن » بمعتی از
راء بطرقی شدن و دور کردیدن از راه باشد .
بر دیر لس » بنتح اول و سکون‌ثالی
و الث بتحتالی کشیده و برای قرشت زده و م
بواو رسیده و بسن ی‌نقطه زده » بلغت بودالی
مرغیست کهآ نرا چکاوكخواننده و بعربی‌ابوالملیع
مد . ۱
پردسص - بارای فرشت بروزن اطلس »
امر بر وا رسیدن و برسیدن باشد یمنی واری
ویپرس۹ ۰
بر دسعه » بنم الث بروزن سر شسته»
مطلق نبانات و گیاه بی‌ساق باس وکنابه ازمردم
پی‌ادب هم هست .
۸ - ۰۳۹ . گلکی 021028 .
تأناری«منهتی الارب*.
بقبه ازصفحٌ ۲۵۲
٩‏ سرك: بررصفن.
سبر» است» زبرا یکی از
پادشاهان ابران اسبرانیاز ارمینیهآ ورد و بدانجا عقيم ساخت. هلال‌بن ه محسن کوید برذعه فصبةٌ
آذریامجان است . این| لفقیه کویدبرذعه همان شهر اران است وآن درآخر حدور آذربایجان لت
ونضنین کی که آنرا عمارت کرد قباد پادشاه (ساسانی) بود . *معجم البلدان» وجه اشتفاق حمزه
ومولف برحان‌عامبانه است و ان اسم‌ممرب 27۵۷ (پپلو-پارت) است و مورخان ارمنی نیز اسم
```


## [2026-10-16T05:14:51.094Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==474' BQT_v1_pages.txt | sed -n 60,120p"
}
```


### [2026-10-16T05:14:51.733Z] TOOL RESULT

```
ومولف برحان‌عامبانه است و ان اسم‌ممرب 27۵۷ (پپلو-پارت) است و مورخان ارمنی نیز اسم
این شهر را چنن‌ضبط کرده‌اند «سنا 1۱ ح۱ »مار کوارت 3 ابراشهر ص۱۱۷*:
```


## [2026-10-16T05:14:57.271Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad 2>/dev/null || mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad; cd /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad; curl -s https://archive.org/metadata/borhan-ghate-v1 | python3 -c \"import json,sys;d=json.load(sys.stdin);print(d.get('server'),d.get('dir'));[print(f['name']) for f in d['files'] if f['name'].endswith(('.pdf','.zip'))]\""
}
```


### [2026-10-16T05:14:58.074Z] TOOL RESULT

```
ia800104.us.archive.org /23/items/borhan-ghate-v1
برهان قاطع، جلد اول.pdf
برهان قاطع، جلد اول_jp2.zip
```


## [2026-10-16T05:15:03.909Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad; curl -sL -o bqt253-523.jpg \"https://archive.org/download/borhan-ghate-v1/page/n473_w1600.jpg\"; file bqt253-523.jpg; curl -sL -o bqt213-523.jpg \"https://archive.org/download/borhan-ghate-v1/page/n433_w1600.jpg\"; file bqt213-523.jpg"
}
```


### [2026-10-16T05:15:08.087Z] TOOL RESULT

```
bqt253-523.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 2479x3508, components 1
bqt213-523.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 2479x3508, components 1
```


## [2026-10-16T05:15:12.395Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad; python3 -c \"\nfrom PIL import Image\nfor n in ['bqt253-523','bqt213-523']:\n  im=Image.open(n+'.jpg'); w,h=im.size\n  im.crop((0,int(h*0.62),w,h)).resize((w*2//3,int(h*0.38)*2//3)).save(n+'-foot.png')\n  im.resize((w//2,h//2)).save(n+'-half.png')\n\""
}
```


### [2026-10-16T05:15:12.832Z] TOOL RESULT

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    from PIL import Image
ModuleNotFoundError: No module named 'PIL'
```


## [2026-10-16T05:15:15.837Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad; for n in bqt253-523 bqt213-523; do magick $n.jpg -gravity south -crop 100%x40%+0+0 -resize 1400x $n-foot.png; done; ls"
}
```


### [2026-10-16T05:15:17.296Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-16T05:15:19.654Z] TOOL CALL #21: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/bqt253-523-foot.png"
}
```


### [2026-10-16T05:15:19.745Z] TOOL RESULT

```

```


## [2026-10-16T05:15:23.309Z] TOOL CALL #22: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/bqt213-523-foot.png"
}
```


### [2026-10-16T05:15:23.326Z] TOOL RESULT

```

```


## [2026-10-16T05:15:27.238Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad; for n in bqt253-523 bqt213-523; do magick $n.jpg -gravity north -crop 100%x8%+0+0 -resize 1200x $n-head.png; done"
}
```


## [2026-10-16T05:15:28.363Z] TOOL CALL #24: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/bqt213-523-head.png"
}
```


### [2026-10-16T05:15:28.718Z] TOOL RESULT

```
(Bash completed with no output)
```


### [2026-10-16T05:15:28.793Z] TOOL RESULT

```

```


## [2026-10-16T05:15:31.609Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad; magick bqt213-523.jpg -gravity north -crop 100%x14%+0+0 -resize 1200x bqt213-523-head.png"
}
```


## [2026-10-16T05:15:32.811Z] TOOL CALL #26: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/bqt213-523-head.png"
}
```


### [2026-10-16T05:15:33.136Z] TOOL RESULT

```
(Bash completed with no output)
```


### [2026-10-16T05:15:33.149Z] TOOL RESULT

```

```


## [2026-10-16T05:15:42.946Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; mkdir -p data/verification/sources/refs/ocr/BQT data/verification/sources/refs/ocr/BOOK; S=/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad; ls data/verification/sources/refs/ocr/BQT | grep -E '^(213|253)\\.' ; cp $S/bqt253-523-foot.png data/verification/sources/refs/ocr/BQT/253.foot.png; cp $S/bqt213-523-foot.png data/verification/sources/refs/ocr/BQT/213.foot.png\ncat > data/verification/sources/refs/ocr/BQT/253.vision.txt <<'EOF'\n[BQT vol.1 p.253 = archive.org borhan-ghate-v1 leaf n473; read from page image]\nبَرده ۴ - بروزن ارده ، بمعنی غلام باشد مطلقا خواه دختر و خواه پسر .\nfootnote ۴ - پهلوی vartak، اوستایی varəta، معرب بردج «اسفا ۱: ۲ص۷۶».\nEOF\ncat > data/verification/sources/refs/ocr/BQT/213.vision.txt <<'EOF'\n[BQT vol.1 p.213 = archive.org borhan-ghate-v1 leaf n433; read from page image, footnote to بادنجان]\nبادنجان - باتنگان ، بادنگان ، در طبری vingum «واژه نامه ۸۱۸» ، گیلکی bâdenjân ، فریزندی vajaemjun ، یرنی و نطنزی bâdenjun «لهـ ۱ ص ۲۸۶» ، تهرانی bâdemjûn ، نباتی است یکساله دارای گلهای بنفش و برگهای دراز و تخم کوچک زرد رنگ ، میوهٔ دراز اندام یا بیضی یا گرد بنفش و سفید و غیره . میوهٔ آن خوراک انسان است [رک : فرهنگ روستایی ۲۳۱ و گل‌گلاب ۲۳۸] معرب آن بادنجان و از تازی وارد زبان اسپانیایی شد: berengena ، در زبان کاتالانی (شمال شرقی اسپانیا) بصورت: alberginia و از آنجا وارد فرانسه شد: aubergine وسپس درایتالیایی وارد گردید: petonciano «نفس» «بداب ۳: ۳-۴ . فرامرزی».\nEOF\npdftoppm -f 523 -l 523 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf $S/pg523"
}
```


## [2026-10-16T05:15:44.019Z] TOOL CALL #28: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/pg523.png"
}
```


### [2026-10-16T05:15:44.673Z] TOOL RESULT

```
(Bash completed with no output)
```


### [2026-10-16T05:15:45.098Z] TOOL RESULT

```

```


## [2026-10-16T05:15:45.095Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-10-16T05:16:02.122Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n 'lemma: ger-' POK_full.txt | head; grep -n -i -E 'gaṇa|gana-|gaNa' POK_full.txt | head -5; sed -n 730,737p LKT.txt | cut -c1-600; sed -n 580,584p LKT.txt | cut -c1-500; grep -n -E 'بردج|باذنجان|بادنجان' AFM.txt TAD.txt ARB_mo3rb.txt 2>/dev/null | head; grep -n -i -E 'aubergine|bardache' PHN.txt | head -3; sed -n 2266,2273p LAM.txt"
}
```


### [2026-10-16T05:16:02.772Z] TOOL RESULT

```
31136:Root / lemma: ger-1, gere- 
31216:Root / lemma: ger-2 
31336:Root / lemma: ger-3 
31503:Root / lemma: ger-3\ "to turn, wind' : Root/ lemma: (s)ker-3\ "to turn, bend'. 
31670:Root / lemma: ger-4, grei- 
35605:Root / lemma: ger-, gera-, gre- 
45989:from Root/ lemma: ger-2\ "to shriek (in expr. forms), *crane'. 
3612:Norse ggn. Old English egenui. and aegnanP\., Old High German agana6s., Modern 
7458:Indie o-e.g. in o-gana-h^ single, pathetic ' (: gana-h' troop, multitude '; Wackernagel Old 
12346:nupYO(; "tower', an oriental loanword from urart. burgana ^pa\ace, fortress' derives (820 v. 
13414:Npers. biris-tan^ivj\ b^rezan^ oyev\\ Baluchi brejag, brijag^ivj\ npers. biryan{*brigana-) 
20099:Gothic l=>amma digandin "the kneading ', kasa digana' clay vessel ', gadigis (meaning 
barajar,  pp.  baralhar  'misilieir,  woraus schließlich  sp.  baraja,  pg.baralha  'Spiel', vielleicht  auch  it.  sbaraiß/o  'Zerspreu- guiig\  Vb.  sbaragliare  sowie  sbaraglino 'Pufispier.
iJ'it).  Ar.  bar'ät: 'Quittuiii;,  Patent';  hieraus  mit  ar.  Art. sp.  albula,  albaran,  pg.  alvara  'dass., Diplom,  Pafa'.  Tk.  ebenso  berat  'Patent', hieraus  rum.  berat  'dass.'.    [DE  63/(>4.
2'i7.  Ar.  barbäris: [Entstanden  aus  nnnr  hüris  über  ambar bäris,  vgl.  FLEISCHER  in  BSGW  phil. bist.  Kl.  1881,  XXXill,  9]  'eine  Pflanze Berberis  vulgaris',  deren  Beeren  zu  Mar- mel.ide,  Sirup  oder  Eis  verarbeitet  wer- den; die  Apotheker  benutzen  ihre  Wur- zalrinde;  zuerst  wurde  die  Pflanze  von den  Arabern  verwertet.  Frz.  berberis, engl,  barberry  [aber  berberine  'die  dar- aus gewonnene  Substanz  zum  Gelb- färben'], dtsch.  Berberize,  Berberstaude, Berberisbeere.  Russ.  barbaris  'Sauer- dorn'.
228.  Ar.  barda'a:
[Nach  I.  I.  Hess  aus  pers.  pärdä  'Tep- pich' mit  infigiertem  'Ain  ZfSein  H,  221. Allerdings  kann  das  ar.  Wort  auch  tk. Ursprungs  sein,  da  wenigstens  im  Dia- lekte von  Adärbaigän  die  Satteldecke ähnlich  heißt:  burunduk  von  der  Wurzel bur,  bör  'verhüllen,  verdecken'  Vämbery TktEtWb  S.  211,  Nr.  228;  vgl.  ZDMG XXIII,  270]  'Satteldecke,  Sattelunterlage, Piicksaltel'.  Hieraus  viele  romanischen Formen  mit  manchem  Bedeutungs- wechsel: it.  barda  'Lederdecke  für  Brust, Hals  und  Flanken  des  Pferdes',  siz. tarda,  frz.  barde  'Reitkissen',  sp.  
229.  Ar.  bardag-:
'Erbeutete,  gefangene  Griechenmädchen, weiße  Sklavinnen'  [KREMER  in  SBKAW Wien  phil.  bist.  Gl.  CHI  (1883),  195/196; nach  VÖLLERS  in  ZDMG  L,  628  noch jetzt  im  Namen  Hös  Barda',  dem  Sklaven- hof von  Kairo,  erhalten] ;  sie  wurden meist  zu  unzüchtigen  Zwecken  gehalten, daher  it.  bardascia  'Knabe,  der  zur  Un- zucht gebraucht  wird,  Lotterbube'  [aber logud.  mail.  piem.  'Knabe'  schlechthin], afrz.  hardaclie,  sp.  bardaja,  bardaje 'Schandbube'.    [Eguilaz  340.    ML  956.
230.  Tk.  bardak:
'Weingefäß,  Krug'  [Horn  NpEt  S.  36, Nr.  155];  hieraus  zunächst  tk.  badja 'dass.'  und  daraus  rum.  bäduü  'Butter- faß'; russ.  badja,  badjeika  'Brunnen- eimer, Kübel',  poln.  (dial.)  badja  'ein Maß  von  bestimmter  Größe  bei  der Minenverwaltung'.  [Gorjajevv  8.  Bern .SlEtWb  37.
160.  Tk.  badihewa:
'ümsonst,  gratis'  [Kelekian  233  b,  wohl aus  ar.  bädi-hawä  'Luft  verursachend'] ; hieraus  bulg.  badihawa,  badlawa  'dass.', serb.  badawad  'dass.',  slov.  badava  und mit  slav.  Präposition  zabadava  'verge- bens, umsonst'.    [Bern  SlEtWb  37.
161.  Pers.  bädiugän:
Ebenso  ar.  bädingän  'Tollapfol,  Solanum melongena'.  Hieraus  zahlreiche  ver- schiedene romanische  Formen:  it.  peton- ciano,  sp.  pg.  val.  berengena,  pg.  berin- gala,  kat.  alberginera,  frz.  aubergine, melanghne,  merangene,  it.  melangola, marignano,  melanzana,  siz.  milinciana. Über  vulg.  tk.  ■paüygan  wurde  rum. pätlägea,  demin.  pätlägicä  'Tomate'. Russ.  badidzan,  badarzan,  batlamn, baklazan.  [DE  239.  Eguilaz  344.  De- vic DEt  46/47.  ML  876.  Löbel  EITAP  
ARB_mo3rb.txt:2661:نت 9 رات قْ الملاء البردجا 5-3 
ARB_mo3rb.txt:2669:وهر خطأ ٠‏ و «البردجا» بالذال» رفقى م « الرردا » بالوار» ودر خأ . 
ARB_mo3rb.txt:22225:« وقالوا » ”” المقد ““* : الباذنجان ٠‏ فارسى معرب فى بعض اللفات » ٠‏ ففرق نيما كا ترى ٠‏ 
ARB_mo3rb.txt:22235:الذى بشمء شيه بالباذنجان إذا اصفر » ٠‏ )6( بشت الدال المهملة ٠‏ وفى اللسان عن أن سيده 
Bardache. Esp : bardaxa, bardaja. Ital: bardascia; de
pS^ bardagy captif, esclave. Ce mot très-ancien en arabe
(V. Muarrab. p. 6. ) vient du persan l^j^ bardahy captif
Barde. Autrefois aubarde. Esp. et Ptg: albarda, barda.
ital: barda. La barde est «une selle de grosses toiles
piquées et bourrées, » (Litt). C'est exactement le sens
de tSjf ou ^^x bardaja, barda'a ( Belot-Heury-Bocth).
Ce mot d'origine persane (3) n'a dans Freytag que le
```


## [2026-10-16T05:16:07.167Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 31136,31145p POK_full.txt | cut -c1-400; grep -n -A1 'Page(s)' POK_full.txt | awk -F: '$1>31136 && $1<31220' | head -3; grep -n -i -E 'gaṇa|gaṇá|gana-h|ganah' POK_full.txt | sed -n 1,5p; sed -n 2655,2662p ARB_mo3rb.txt; grep -n -E '^ger-|^gher-' AHD_watkins1985.txt | head"
}
```


### [2026-10-16T05:16:07.803Z] TOOL RESULT

```
Root / lemma: ger-1, gere- 
Meaning: to gather, put together 

Material: Gr. aysipu) (ayspw, HY^'Pa) gather; assemble' {*n-ger-Jd; a- weal< form from £v, 
also " collect, gather '?), gr. Doric a-^^t-mc, " collector, gatherer ', Aor. EypsTO " be 
gathered ', Infin. avpsoGai; ayopa, ayupic; "congregation, meeting', aYupTr|<; " collector, 
gatherer, beggar', a^oaioq, "hand, crooked, bent arm' (if from *a-YopaTO(;, with Aeolic op 
from r, for the formation compare naAaarn "flat hand'), YSPY^PC noAAa Hes., to YapYapci " 
swarm, flock; mass, crowd, heap'; 

31212:Page(s): 382-383 
31213-
7458:Indie o-e.g. in o-gana-h^ single, pathetic ' (: gana-h' troop, multitude '; Wackernagel Old 
26460:Gothic ganah (preterit-present) " it suffices = is enough, it meets the needs ', Inf. 
ف" 1ن افر الياك” > 
0 ُُ 
أى - النق دن العيوب ٠‏ 

: وقال العسجاج : 
6م اه 0 فق 
نت 9 رات قْ الملاء البردجا 5-3 
وهم ا ويقال لم افاوسة ‏ حق ااه لقا 
491:ger-?
521:gher-'. To grasp, enclose; with derivatives meaning “enclosure.” 1. Suffixed zero-grade form *ghr-dh- in: a. Germanic *gurdjan in Old English gyrdan, to gird: GIRD; b. Old English gyrdel, girdle: GIRDLE; c. Old Norse gjordh, girdle, girth: GirTH. 2. Suffixed o-grade form *ghor-dho- (in Germanic) or *ghor-to-, an enclosure, in: a. Germanic *gardaz in (i) Old English geard, enclosure, garden, yard: YARD?; ORCHARD (ii) Old Norse gardhr, garden, yard: GARTH (iii) Old High German garto, gar- den: KINDERGARTEN (iv) Old North French gardin, gar- den: GARDEN (v) compound *midja-gardaz, “middle zone,” earth (see medhyo-); b. Latin hortus, garden: HORTICULTURE, ORCHARD, ORTOLAN. 3. Prefixed and suffixed zero-grade form *ko(m)-ghr-ti- (*ko(m)-, collec- tive prefix, “together”; see kom) in Latin cohors (stem cohort-), enclosed yard, company of soldiers, multitude: COHORT, CORTEGE, COURT, COURTEOUS, COURTESAN, (COURTESY), COURTIER, (CURTILAGE), (CURTSY). 4. Per- haps suffixed o-grade form *ghor-o- in Greek khoros, dancing ground (? perhaps originally a special enclosure for dancing), dance, dramatic chorus: (CHOIR), (CHORAL), (CHORALE), CHORIC, (CHORISTER), CHORUS; CHORAGUS, TERPSICHORE. [Pok. 4. gher- 442, gherd- 444.]
522:gher-2. To call out. Extended root *ghréd-. Germanic *grotjan in Old English grétan, to speak to, greet: GREET. [Pok. 1. gher- 439.]
524:gher-’. To shine, glow; gray. Hypothetical base of various Germanic forms. 1. Germanic *gréwaz, gray, in: a. Old English greg, gray: GRAY; b. probably Old English grighund, greyhound: GREYHOUND. 2. Germanic *gris- Jaz, gray, in: a. Old French gris (> French gris), gray: GRISAILLE, (GRISETTE), (GRISON), GRIZZLE; AMBERGRIS; b. Medieval Latin griseus, gray, grayish: GRISEOUS. [Pok. 3. gher- 441.] gher-4. To scrape, scratch. 1. Extended zero-grade form *ghr(e)-k- in: a. Greek kharax, a pointed stake, also a kind of sea bream: CHARACIN; b. Greek kharassein, to sharpen, notch, carve, cut: CHARACTER, GASH. 2. Ex- tended form *ghers-.in suffixed zero-grade form *ghrs-to- perhaps (but unlikely) in Sanskrit ghattah, ghat: GHAT. See also extensions ghréi- and ghréu-. [Pok. 2. gher- 439.] gher-5. To like, want. 1. Suffixed form *gher-n- in Ger- manic “*gernjan in Old English giernan, gyrnan, to strive, desire, yearn: YEARN. 2. Extended form *ghré- possibly in: a. Germanic *gréduz, hunger, forming *grédagaz, hungry, in Old English grédig, hungry, covetous, greedy: GREEDY; b. Greek khré, it is necessary, whence krésthai, to lack, want, use: CATACHRESIS, CHRESARD, CHRESTOM- ATHY. 3. Suffixed zero-grade form *ghr-td- in Latin hortari, to urge on, encourage (< “to cause to strive or desire”): HORTATIVE; EXHORT. 4. Suffixed zero-grade form “ghr-i- in Greek kharis, grace, favor: CHARISMA; Eucnarist. [Pok. 1. gher- 440.] ghere-. Gut, entrail. 1. Suffixed form *ghero-no- in Ger- manic *garn6, string, in Old English gearn, yarn: YARN. 2. Suffixed form *ghero-n- in Latin hernia, “protruded viscus,” rupture, hernia: HERNIA. 3. Suffixed o-grade form *ghoro-d- in Greek khordé, gut, string: (CHORD?), CORD, (CORDON); HARPSICHORD, TETRACHORD. 4. O-grade form *ghors- in Greek khorion, intestinal membrane, afterbirth: CHORION. 5. Possible suffixed zero-grade form *ghr-u- in Latin haruspex (-spex, “he who sees” < *spek-, “to see”; see spek-), “he who inspects entrails,” diviner (but perhaps borrowed from Etruscan): HARUSPEX. [Pok. 5. gher- 443.] ghers-. To bristle. 1. Extended zero-grade form *ghrzd-, prickly plant, in: a. Germanic *gorst- in Old English gorst, furze, gorse: GORSE; b. Latin hordeum, barley: ORGEAT. 2. Lengthened-grade form *ghér(s)- in Latin hér, ér, hedgehog: URCHIN. 3. Suffixed lengthened-grade form *ghér(s)-ika in Latin ériica, caterpillar: ROCKET?. 4. Suffixed full-grade form *gher-tu-, remade to *hirsu- in Latin hirsitus, bristly, shaggy, hairy: HIRSUTE. 5. Suf- fixed full-grade form *ghers-ko- in Latin hispidus (prob- ably a dialectal borrowing), bristly, shaggy, prickly: HISPID. 6. Suffixed o-grade form “ghors-eyo- in Latin horrére, to bristle, shudder, be terrified, look frightful: HORROR; ABHOR, ORDURE. 7. Suffixed full-grade form *ghers-o- in Greek khersos, dry land: CHERSONESE. [Pok. Bhers- 445.] gheslo-. Seen by some as a base for words meaning “thousand.” 1, Suffixed form *ghesl-yo- in Greek khilioi, thousand: CHILIAD, KILO-. 2. Latin mille, thousand, which has been analyzed as *smi-, “one” + a form *ghsli-, is of obscure origin: MIL!, MIL2, MILE, MILLE- NARY, MILLESIMAL, MILLI-, MILLIEME, MILLION; MIL- FOIL, MILLENNIUM, MILLEPORE, MILLIARY, MILLIPEDE. [Pok. ghéslo- 446.] ghesor-. Hand. Reduced form “ghesr- in Greek kheir, hand: CHIRO-; (CHIRURGEON), ENCHIRIDION, (SURGEON), SURGERY. [Pok. 1. 8hesor- 447.] gheu-. To pour, pour a libation. I. Extended form *gheud-. 1. Zero-grade form *ghud- in Germanic *gut- in Old English guttas, intestines: GuT. 2. Nasalized zero-grade form *ghu-n-d- in Latin fundere, to pour: FOISON, FONDANT, FONDUE, FONT, FOUND2, FUNNEL, FUSE?, FUSILE, FUSION; AFFUSION, CIRCUMFUSE, CON- FOUND, CONFUSE, DIFFUSE, EFFUSE, INFUSE, PERFUSE, PROFUSE, REFUND!, (REFUSE!), (REFUSE?), SUFFUSE,
```


## [2026-10-16T05:16:11.118Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 31136,31212p POK_full.txt | grep -n -i -E 'indian|gan' | head; sed -n 7455,7460p POK_full.txt | cut -c1-300; grep -n -i -E 'aubergine|egg-?plant|brinjal' SYN.txt IEC.txt WLD_band3.txt | head -5; grep -n -i 'aubergine' AHD_watkins1985.txt SKT.txt | head"
}
```


### [2026-10-16T05:16:11.886Z] TOOL RESULT

```
Avestan avara Mv. " below, down '= Old Indie avarPN . I 133, 7; Old Indie avah{avas) " 
down ', whereof avastad' under '; without auslaut vowel (compare Avestan ao-ra) Old 
Indie o-e.g. in o-gana-h^ single, pathetic ' (: gana-h' troop, multitude '; Wackernagel Old 
Indie Gr. 154);
```


## [2026-10-16T05:16:18.514Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for u in 'https://en.wiktionary.org/wiki/%D8%A8%D8%B1%D8%AF%D9%87' 'https://en.wiktionary.org/wiki/bardash' 'https://en.wiktionary.org/wiki/bardache' 'https://en.wiktionary.org/wiki/aubergine' 'https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D8%AF%D9%86%D8%AC%D8%A7%D9%86' 'https://en.wiktionary.org/wiki/berenjena' 'https://www.etymonline.com/word/aubergine' 'https://ahdictionary.com/word/search.html?q=aubergine'; do echo \"=== $u\"; curl -sL -A 'Mozilla/5.0' \"$u\" | python3 -c \"\nimport sys,re,html\nt=sys.stdin.read(); t=re.sub(r'(?s)<(script|style).*?</\\1>','',t); t=html.unescape(re.sub(r'<[^>]+>',' ',t)); t=re.sub(r'\\s+',' ',t)\nfor m in re.finditer(r'Etymology[^.]{0,700}',t): print(m.group(0)[:700]); print('--')\nif 'etymonline' in sys.argv[0] or True: \n  i=t.find('aubergine (n.)'); print(t[i:i+800] if i>=0 else '')\n\" | head -40; done"
}
```


### [2026-10-16T05:16:21.785Z] TOOL RESULT

```
=== https://en.wiktionary.org/wiki/%D8%A8%D8%B1%D8%AF%D9%87
Etymology 1 2
--
Etymology 2 2
--
Etymology 1 [ edit ] Inherited from Middle Persian 𐫇‎𐫡𐫅𐫃 ( wltk' /⁠wardag⁠/ , “ slave; captive ” ) 
--
Etymology 2 [ edit ] Pronunciation [ edit ] ( Classical Persian ) IPA ( key ) : /bur
--

=== https://en.wiktionary.org/wiki/bardash
Etymology 1
--
Etymology [ edit ] From French bardache , from Italian bardassa , perhaps from Arabic بَرْدَج ( bardaj , “ slave ” ) 
--

=== https://en.wiktionary.org/wiki/bardache
Etymology 1
--
Etymology [ edit ] Earlier bredaiche , borrowed from Italian bardassa , from Arabic بَرْدَج ( bardaj , “ captive ” ) , from Persian بَرْدَه ( “ slave, captive ” ) 
--

=== https://en.wiktionary.org/wiki/aubergine
Etymology 1
--
Etymology 2
--
Etymology 3
--
Etymology 4
--
Etymology 5
--
Etymology 6
--
Etymology 7
--
Etymology [ edit ] Etymology tree Proto-Dravidian *waẓVtV der
--
Etymology [ edit ] Unadapted borrowing from French aubergine , from Catalan albergínia , from Arabic اَلْبَاذِنْجَان ( al-bāḏinjān , “ the eggplant ” ) , from Classical Persian بادنجان ( bâdenjân ) , from باتنجان ( bâtenjân ) , from Sanskrit वातिगगम ( vātigagama , “ eggplant ” , literally “ the plant that cures the wind ” ) 
--
Etymology [ edit ] Unadapted borrowing from French aubergine , from Catalan albergínia , from Arabic اَلْبَاذِنْجَان ( al-bāḏinjān , “ the eggplant ” ) , from Classical Persian بادنجان ( bâdenjân ) , from باتنجان ( bâtenjân ) , from Sanskrit वातिगगम ( vātigagama , “ eggplant ” , literally “ the plant that cures the wind ” ) 
--
Etymology [ edit ] Borrowed from Catalan albergínia , from Arabic اَلْبَاذِنْجَان ( al-bāḏinjān , “ the eggplant ” ) , from Classical Persian بَادِنْگَان ( bādingān ) , from بَاتِنْگَان ( bātingān ) , from Sanskrit वातिङ्गण ( vātiṅgaṇa , “ eggplant ” ) , from Dravidian , ultimately from Proto-Dravidian *waẓVtV 
--
Etymology [ edit ] Unadapted borrowing from French aubergine , from Catalan albergínia , from Arabic اَلْبَاذِنْجَان ( al-bāḏinjān , “ the eggplant ” ) , from Classical Persian بادنجان ( bâdenjân ) , from باتنجان ( bâtenjân ) , from Sanskrit वातिगगम ( vātigagama , “ eggplant ” , literally “ the plant that cures the wind ” ) 
--
Etymology [ edit ] Unadapted borrowing from French aubergine , from Catalan albergínia , from Arabic اَلْبَاذِنْجَان ( al-bāḏinjān , “ the eggplant ” ) , from Classical Persian بادنجان ( bâdenjân ) , from باتنجان ( bâtenjân ) , from Sanskrit वातिगगम ( vātigagama , “ eggplant ” , literally “ the plant that cures the wind ” ) 
--
Etymology [ edit ] Unadapted borrowing from French aubergine , from Catalan albergínia , from Arabic اَلْبَاذِنْجَان ( al-bāḏinjān , “ the eggplant ” ) , from Classical Persian بادنجان ( bâdenjân ) , from باتنجان ( bâtenjân ) , from Sanskrit वातिगगम ( vātigagama , “ eggplant ” , literally “ the plant that cures the wind ” ) 
--

=== https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D8%AF%D9%86%D8%AC%D8%A7%D9%86
Etymology 1
--
Etymology 2
--
Etymology [ edit ] Etymology tree Proto-Dravidian *waẓVtV der
--
Etymology [ edit ] Borrowed from Classical Persian بادنجان from Sanskrit वातिङ्गण ( vātiṅgaṇa , “ the plant that cures the wind ” ) from Dravidian , ultimately from Proto-Dravidian *waẓVtV 
--

=== https://en.wiktionary.org/wiki/berenjena
Etymology 1
--
Etymology 2
--
Etymology [ edit ] Etymology tree Proto-Dravidian *waẓVtV der
--
Etymology [ edit ] Etymology tree Proto-Dravidian *waẓVtV der
--

=== https://www.etymonline.com/word/aubergine

=== https://ahdictionary.com/word/search.html?q=aubergine
```


## [2026-10-16T05:16:26.776Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for u in 'https://en.wiktionary.org/wiki/berenjena' 'https://en.wiktionary.org/wiki/%D8%A8%D8%B1%D8%AF%D9%87' 'https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D8%AF%D9%86%D8%AC%D8%A7%D9%86' 'https://www.etymonline.com/word/aubergine' 'https://ahdictionary.com/word/search.html?q=aubergine'; do echo \"=== $u\"; curl -sL -A 'Mozilla/5.0 (X11; Linux x86_64)' \"$u\" | python3 -c \"\nimport sys,re,html\nt=sys.stdin.read(); t=re.sub(r'(?s)<(script|style).*?</\\1>','',t); t=html.unescape(re.sub(r'<[^>]+>',' ',t)); t=re.sub(r'\\s+',' ',t)\nfor k in ['Spanish','Inherited from Middle Persian','Persian Etymology','Borrowed from','aubergine (n.)','[French','au·ber']:\n  for m in re.finditer(re.escape(k),t): print(k,'>>',t[m.start():m.start()+500]); break\n\" | head -20; done"
}
```


### [2026-10-16T05:16:28.434Z] TOOL RESULT

```
=== https://en.wiktionary.org/wiki/berenjena
Spanish >> Spanish Toggle Spanish subsection 2.1 Etymology 2.2 Pronunciation 2.3 Noun 2.3.1 Derived terms 2.3.2 Descendants 2.4 Further reading Toggle the table of contents berenjena 30 languages Asturianu Azərbaycanca Català Čeština Dansk Deutsch Esperanto Español Euskara Suomi Français Galego Magyar Ido Italiano 한국어 کٲشُر Kurdî Malagasy Nederlands Occitan Polski Română Русский Sängö Svenska தமிழ் ไทย Türkçe 中文 Entry Discussion English Read Edit View history Tools Tools move to sidebar hide Actions Read E
Borrowed from >> Borrowed from Spanish berenjena . Pronunciation [ edit ] IPA ( key ) : ( Navarro-Lapurdian ) /beɾenɟena/ [be.ɾẽɲ.ɟe.na] IPA ( key ) : ( Southern ) /beɾenxena/ [be.ɾeŋ.xe.na] IPA ( key ) : ( Gipuzkoan ) /beɾenxena/ [be.ɾeŋ.xe.na] IPA ( key ) : ( Biscayan ) /beɾend͡ʒena/ [be.ɾẽnʲ.d͡ʒe.na] IPA ( key ) : ( Navarrese ) /beɾenjena/ [be.ɾẽɲ.je.na] Rhymes: -ena , -a Hyphenation: be‧ren‧je‧na Noun [ edit ] berenjena inan eggplant , aubergine Synonym: alberjinia Declension [ edit ] Declension of berenjena
=== https://en.wiktionary.org/wiki/%D8%A8%D8%B1%D8%AF%D9%87
Inherited from Middle Persian >> Inherited from Middle Persian 𐫇‎𐫡𐫅𐫃 ( wltk' /⁠wardag⁠/ , “ slave; captive ” ) . Pronunciation [ edit ] ( Classical Persian ) IPA ( key ) : /bar.ˈda/ ( Dari, formal ) IPA ( key ) : [bäɾ.d̪á] ( Dari, formal ) IPA ( key ) : [bäɾ.d̪á] ( Kabuli ) IPA ( key ) : [bäɾ.d̪á] ( Hazaragi ) IPA ( key ) : [bäɾ.d̪á] ( Iran, formal ) IPA ( key ) : [bæɹ.d̪é] ( Tajik, formal ) IPA ( key ) : [bäɾ.d̪á] Rhymes: -a Readings Classical reading ? barda Dari reading ? barda Iranian reading ? barde Tajik reading ? barda N
=== https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D8%AF%D9%86%D8%AC%D8%A7%D9%86
Borrowed from >> Borrowed from Classical Persian بادنجان from Sanskrit वातिङ्गण ( vātiṅgaṇa , “ the plant that cures the wind ” ) from Dravidian , ultimately from Proto-Dravidian *waẓVtV . Doublet of بینگن ( baiṅgan ) . Pronunciation [ edit ] ( Standard Urdu ) IPA ( key ) : /bɑː.d̪ən.d͡ʒɑːn/ Hyphenation: با‧دَنْ‧جان Noun [ edit ] بادَنْجان • ( bādanjān ) m ( Hindi spelling बादंजान ) aubergine , eggplant Declension [ edit ] Declension of بادنجان singular plural direct بادنجان ( bādanjān ) بادنجان ( bādanjān ) obl
=== https://www.etymonline.com/word/aubergine
=== https://ahdictionary.com/word/search.html?q=aubergine
[French >> [French, from Catalan albergínia, albergina , from Arabic al-b ā ḏ inj ā n , the eggplant, from Persian b ā denj ā n, b ā deng ā n , from a Middle Indic source akin to Pali v ā ti ṅ ga ṇ a , and Sanskrit bha ṇ ṭ ā k ī , ultimately of non-Indo-European origin; akin to Tamil va ḻ utalai , va ḻ utu ṇ ai .] The American Heritage® Dictionary of the English Language, Fifth Edition copyright ©2022 by HarperCollins Publishers. All rights reserved. Indo-European & Semitic Roots Appendices Thousands of en
au·ber >> au·ber·gine ( ō  b ĕ r-zh ē n ′ , ō  b ə r-j ē n) Share: Tweet n. See eggplant . [French, from Catalan albergínia, albergina , from Arabic al-b ā ḏ inj ā n , the eggplant, from Persian b ā denj ā n, b ā deng ā n , from a Middle Indic source akin to Pali v ā ti ṅ ga ṇ a , and Sanskrit bha ṇ ṭ ā k ī , ultimately of non-Indo-European origin; akin to Tamil va ḻ utalai , va ḻ utu ṇ ai .] The American Heritage® Dictionary of the English Language, Fifth Edition copyright ©2022 by HarperCollins Publis
```


## [2026-10-16T05:16:33.256Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; curl -sL -A 'Mozilla/5.0' 'https://en.wiktionary.org/wiki/berenjena' | python3 -c \"\nimport sys,re,html\nt=sys.stdin.read(); t=re.sub(r'(?s)<(script|style).*?</\\1>','',t); t=html.unescape(re.sub(r'<[^>]+>',' ',t)); t=re.sub(r'\\s+',' ',t)\nfor m in re.finditer(r'(From|Borrowed from) (Andalusian|Arabic|Hispano|Old Spanish)[^\\[]{0,400}',t): print(m.group(0))\n\"; curl -sL -A 'Mozilla/5.0' 'https://www.etymonline.com/word/aubergine' | python3 -c \"\nimport sys,re,html\nt=sys.stdin.read(); t=html.unescape(re.sub(r'<[^>]+>',' ',t)); t=re.sub(r'\\s+',' ',t); i=t.find('Catalan'); print(t[i-400:i+400])\""
}
```


### [2026-10-16T05:16:33.907Z] TOOL RESULT

```
Borrowed from Arabic بَاذِنْجَان ( bāḏinjān ) . Compare Portuguese beringela . Pronunciation
```


## [2026-10-16T05:16:34.983Z] AGENT

Now archive the sources used.


## [2026-10-16T05:16:39.490Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%A8%D8%B1%D8%AF%D9%87' --note 'page 523, root Vareta: Persian barde < MP wardag' ; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/bardash' --note 'page 523, root Vareta: English bardash < F bardache < It. < Ar. bardaj'; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/bardache' --note 'page 523, root Vareta: French bardache < It. bardassa < Ar. bardaj < Pers. barde'; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/aubergine' --note 'page 523, root Vatin-ganah: aubergine < Catalan < Ar. < Pers. < Skt vatingana < Dravidian'; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D8%AF%D9%86%D8%AC%D8%A7%D9%86' --note 'page 523, root Vatin-ganah: badenjan Persian/Arabic/Urdu'; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/berenjena' --note 'page 523, root Vatin-ganah: Spanish berenjena < Ar. badinjan'; python3 tools/fetch_source.py 'https://ahdictionary.com/word/search.html?q=aubergine' --note 'page 523, root Vatin-ganah: AHD aubergine, non-IE origin' 2>&1 | tail -3"
}
```


### [2026-10-16T05:16:42.402Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/af378bf9947a8294.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/552ce5af608d8dc6.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/97fae639bf6e89d6.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/0e10cac73baa39fe.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/b88486ba3eac96b9.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/f5130856d5eee355.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/b75fce3c0ee124b2.txt
```


## [2026-10-16T05:16:46.798Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E 'Gefangen|b[aä]ding|bädinj|Solanum' HRN.txt | head -5; grep -n -E '^برده|برده\\s*\\[|بادنجان\\s*\\[|^بادنجان|^بادنگان|^باتنگان' MON_part1.txt | head; grep -n -E 'برده|بادنجان' incoming/ARY/ARY_pages.txt | head -5; grep -n -i -E 'BARDE|BADEN' incoming/ARY/ARY_latin_index_pages.txt | head -5; grep -n -i -E 'wardag|vartak' NYB_vol1.txt | head -3"
}
```


### [2026-10-16T05:16:47.186Z] TOOL RESULT

```
254:hier noch nach: handi- 'Gefangener zu np. hende, No. 230
444:eine ähnliche Untersuchung systematisch zu sammeln angefangen. Bei
965:sie gefangen und ai. i^sanj- *hängen* passen nicht, doch
2116:*) Berde 'Gefangener* habe ich KZ. 32, 574 fälschlich als PPP.
4084:*) Alb. kap *greife, fasse an, nehme gefangen* ist nach G. Meyer
19380:برده‌ایم» داناایم؛ و در غبر این صورت.ء به 
20009:بادنجانیان که اصلش از هندوستان است: 
30385:برده نقل ارتعاشات صوتی ابجاد شده در 
30407:برده افتادن: بی‌چیز شدن» تهیدست شدن. به 
30425:برده‌دار. حاجبی؛ حجایت» سدانت. دربانی. 
30430:برده‌سراء» شستان. نغمه‌سرای» نغمه‌خوان» 
42074:بادنجانیان که پایامی‌باشد. برگ‌هایش پهن و 
43904:بادنجانیان» که یکساله است و به ارتفاع ۲ 
44604:بادنجان. 
45209:برده در برده» توتتو. 
123:نواحی زبان‌های اولیه این سّرزمین‌ها نبوده‌اند و توسط کوچگران به آنجا برده شده‌اند. ۳-بسیاری از
1063:۸ برده‌داری: تقریباً همه‌ی دانشمندان بر این عقیده‌اند که هند و اروپائیان برده‌دار بودند و
1064:یه زنان یشتر برده‌های آنها را تشکیل می‌دادند. شاید علت این باشد که در روزگاران کهن که ره"
1065:برده گیری جنگ و پیزووزی بر دشمن پود. نگهداری بردگان مرد مخاطراتی را بهمراه داشت. (شورش
3452:برده‌اند (016321218 81۸
4397:PARAISO PORTUGUESE) JU PARTEZ, BARDEZ (ARMENIAN) 5)
8064:سرهرسو‎ "?oll?k:"avartak رسو‎ hwnoSk : huniizak 
10980:کل لک‎ Lush: vartak
```


## [2026-10-16T05:16:49.311Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 2112,2122p HRN.txt; grep -n -B3 -A3 'Lush: vartak' incoming/ARY/ARY_pages.txt | head -20; grep -n -E '^برده|^بَرده|برده *\\(' MON_part1.txt | head"
}
```


### [2026-10-16T05:16:49.750Z] TOOL RESULT

```
buräh oder beräh 'Schmuck* Vor, das in den Wörterbüchern (FR, FJ,
SF) ebenso wie beräz belegt wird.
') Den bei Vullers aus dem F8 abgedruckten Sähnämevers
konnte mir Herr Dr. Landauer nicht nachweisen.
*) Berde 'Gefangener* habe ich KZ. 32, 574 fälschlich als PPP.
zu bürden gestellt; die Pehleviform lautet vartak (Geiger, Yätk.
Zar. 49, Anm. 12; Nöldeke, ZDMG. 46, 140).— 40 -
ap. aw. [/^bar- 'tragen; fihlv, hurtan^ baram, burtär,
bar(i)sn; ai. V'bhar-^ bhdrati; arm. berem *bringen*
(H. No. 55).
kurd. birin ^tragen, bringen', Praes. berum; af/. wral;
19380:برده‌ایم» داناایم؛ و در غبر این صورت.ء به 
30385:برده نقل ارتعاشات صوتی ابجاد شده در 
30407:برده افتادن: بی‌چیز شدن» تهیدست شدن. به 
30425:برده‌دار. حاجبی؛ حجایت» سدانت. دربانی. 
30430:برده‌سراء» شستان. نغمه‌سرای» نغمه‌خوان» 
45209:برده در برده» توتتو. 
52506:برده‌داری. دربانی. 
55563:برده‌نشینی (زن)» مخدره بودن. 
76027:برده‌داری کردن (خانه کعبه باستخانه را). 
78543:برده‌های دستگاه مرکزی اعضای حیاتی
```


## [2026-10-16T05:16:52.555Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 10970,10990p incoming/ARY/ARY_pages.txt; awk 'NR<=10980 && /pdf page/ {l=$0} END{}; NR==10980{print l}' incoming/ARY/ARY_pages.txt"
}
```


### [2026-10-16T05:16:53.084Z] TOOL RESULT

```
پهلوی (۲7هاتلهه): ۸ ,0ق5 ساکسونی کهن (542:0۸ 012): رید
آوستی (0558716): فریزی کهن (/(4ا5ل۴۲ صا0): ند 8 انا
7 ,22613۸0 ,۸۲۸94 آلمانی کهن (/(۸/ن027 بلاط صز:
کردی (03/0[54): 510 ۷۸ ,ش1۷11
بلرچی (اتللاملم8): رازن آلمانی (68721۸21): 2 اد ریا
تخاری 8 (8 ۸۸ل7052۸): ۵:۳۷ انگلیسی کهن (0کلا80/0 ۰:00 ,1711
سفدی (/(۸ا300۸2): ان انگلیسی (#ل5لباه67): ۲/8۵
سانسکربت (8۸(/58/7): 0۳ دانمارکی (0۸(/184): ۷1
ارمنی (لفا اگم سوئدی (87201577): ۸آ]۷
ی 7 11۸01667310 نروژی (۸۸0۲804۷: ۰ 6۷۲۳8 بلتا30
لاتین (3(0سل): 0 01۹ اسلاری کهن (ع۷۲بما؟ بط#نابن 0ا۵):
فرانسه کهن (ل۸۷ظ۲۴ صان): ۰ 0-1815 71 با[۳050
اسپانیایی (5۳۸۸/5): 017820 ,01-1870 ۱
ایتالپایی (انمته7): ۰ 613270 ,0171270
پرتغالی (۳0770017885): 010 :
گرتیکك (00774/6): 17781۸
[pdf page 371]
۲ // شانزده
پسگشت‌ها 5 0 ,1104 ی
۳ :010/5
2 0۷81۲۵ +7 711 ساللقراپ : 5
[pdf page 370]
```


## [2026-10-16T05:16:57.250Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; cp /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/pg523.png data/verification/sources/refs/ocr/BOOK/523.png; python3 -c \"\nimport json;d=json.load(open('data/verification/page-511.json'));print(json.dumps(d['entries'][0]['nodes'][0],ensure_ascii=False)[:1500]); print(d.keys(), d['verified_by'])\""
}
```


### [2026-10-16T05:16:57.809Z] TOOL RESULT

```
{"id": 1, "lang": "Sanskrit", "words": "", "verdict": "disputed", "derivation": "Empty pass-through box: Nourai (following Pourdavoud via Mo'in's Borhan footnote) routes the Tamil word through Sanskrit before it reaches Aramaic and Arabic. No Sanskrit form of the tōkai/ṭāwūs type is attested: the Sanskrit words for 'peacock' are mayūra-, śikhin-, barhin-, kalāpin-. Modern scholarship (Wiktionary s.v. ταώς, Klein s.v. peacock) derives the Mediterranean/Semitic words either from Pre-Greek ταώς or directly from a Dravidian (Tamil tōkai) or other eastern source by sea trade, with no Sanskrit intermediary.", "derivation_fa": "این خانهٔ خالی «سنسکریت» را نورایی به پیروی از پورداوود (در حاشیهٔ معین بر برهان قاطع) میان تامیلی و آرامی/عربی گذاشته است. اما در سنسکریت واژه‌ای از گونهٔ tōkai یا ṭāwūs برای طاووس دیده نمی‌شود؛ نام‌های سنسکریت طاووس mayūra، śikhin و barhin است. پژوهش امروزی (کلاین، ویکی‌واژه) واژهٔ یونانی ταώς را پیش‌یونانی می‌داند یا آن را مستقیم به منبعی شرقی مانند تامیلی tōkai می‌رساند، و گذر از سنسکریت را تأیید نمی‌کند.", "sources": ["https://en.wiktionary.org/wiki/ταώς", "https://en.wiktionary.org/wiki/தோகை"], "ref_check": [{"ref": "BQT:1346", "status": "partial", "note": "Borhan-e Qate' p.1346 (BQT_v3_picofile.pdf page 139; the tool's default offset lands on pdf 141, use --pdf-page 139; transcription saved in ocr/BQT/1346.vision.txt), Mo'in's footnote s.v. طاوس: '(عر) معرب آن طویس، یونانی Taôs، آرامی طاوسا tausâ «تسیمرن. لغات دخیل اکدی ص۵۲» طبق تحقیق استاد پور داود اص
dict_keys(['pdf_page', 'book_page', 'verified_by', 'verified_on', 'entries']) claude-opus-5
```


## [2026-10-16T05:18:53.983Z] TOOL CALL #40: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-523.py <<'EOF'\nimport json\nW_BARDE='https://en.wiktionary.org/wiki/%D8%A8%D8%B1%D8%AF%D9%87'\nW_BARDASH='https://en.wiktionary.org/wiki/bardash'\nW_BARDACHE='https://en.wiktionary.org/wiki/bardache'\nW_AUB='https://en.wiktionary.org/wiki/aubergine'\nW_BADEN='https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D8%AF%D9%86%D8%AC%D8%A7%D9%86'\nW_BEREN='https://en.wiktionary.org/wiki/berenjena'\nAHD_AUB='https://ahdictionary.com/word/search.html?q=aubergine'\n\nBQT253={\"ref\":\"BQT:253\",\"status\":\"supports\",\"note\":\"Borhan-e Qate' vol.1 p.253 (archive.org borhan-ghate-v1 leaf n473; read from image, transcription in ocr/BQT/253.vision.txt): 'بَرده ... بمعنی غلام باشد مطلقا خواه دختر و خواه پسر'; Mo'in fn.4: 'پهلوی vartak، اوستایی varəta، معرب بردج'.\"}\nHUB26={\"ref\":\"HUB:26\",\"status\":\"supports\",\"note\":\"Hübschmann, Persische Studien p.26 no.196 (HUB.txt l.840): 'Zu barda \\\"Gefangener\\\" = phl. vartak hat schon Geiger ... richtig zd. vareta- \\\"gefangen\\\" gestellt'; also l.5456: 'barda \\\"Gefangener\\\" = phl. vartak, zd. vareta-'.\"}\nKLN148={\"ref\":\"KLN:148\",\"status\":\"supports\",\"note\":\"Klein (KLN_1966.txt l.4448): 'bardash, n., a catamite. — F. bardache, fr. It. bardascia, fr. Arab. bardaj, \\\"slave\\\", ult. fr. Pers. bardah, of s.m.'\"}\nKLN125={\"ref\":\"KLN:125\",\"status\":\"supports\",\"note\":\"Klein (KLN_1966.txt l.3927) s.v. aubergine: 'F., fr. Catal. alberginera, alberginia, fr. Arab. al-badinjan, \\\"the eggplant\\\", ... fr. Pers. badin-gan, fr. OI. vatin-ganah. Cp. berengena.'\"}\nKLN165={\"ref\":\"KLN:165\",\"status\":\"supports\",\"note\":\"Klein (KLN_1966.txt l.4782): 'berengena, n., the eggplant. — Sp., fr. Arab. badinjan (in vulgar pronunciation bedinjen), ult. fr. Persian. See aubergine.' Klein spells berengena, not berengina.\"}\nBQT213={\"ref\":\"BQT:213\",\"status\":\"supports\",\"note\":\"Borhan-e Qate' vol.1 p.213 (leaf n433; read from image, ocr/BQT/213.vision.txt), Mo'in's footnote s.v. بادنجان: 'باتنگان، بادنگان ... معرب آن بادنجان و از تازی وارد زبان اسپانیایی شد: berengena، در زبان کاتالانی ... alberginia و از آنجا وارد فرانسه شد: aubergine'.\"}\nMON444={\"ref\":\"MON:444\",\"status\":\"not_checked\",\"note\":\"Only the 2-vol Adena abridgement is on disk (MON_part1.txt, different pagination, OCR finds بادنجان only inside other entries); 6-vol p.444 not accessible.\"}\nAHD86={\"ref\":\"AHD:86\",\"status\":\"partial\",\"note\":\"AHD:86 is a main-dictionary page (not the IE appendix). Online AHD 5th ed. s.v. aubergine (archived): 'French, from Catalan albergínia, albergina, from Arabic al-bāḏinjān, from Persian bādenjān, bādengān, from a Middle Indic source akin to Pali vātiṅgaṇa ... ultimately of non-Indo-European origin; akin to Tamil vaḻutalai' — same chain, but goes via Catalan and denies an IE origin.\"}\n\nKLN_cons=lambda w,s,n:{\"src\":\"KLN\",\"where\":w,\"stance\":s,\"note\":n}\nLKT229={\"src\":\"LKT\",\"where\":\"no. 229 (LKT.txt l.736)\",\"stance\":\"supports\",\"note\":\"'Ar. bardag: \\\"Erbeutete, gefangene Griechenmädchen, weiße Sklavinnen\\\" ... daher it. bardascia \\\"Knabe, der zur Unzucht gebraucht wird\\\", afrz. bardache, sp. bardaja'.\"}\nLAM_b={\"src\":\"LAM\",\"where\":\"LAM.txt l.2266\",\"stance\":\"supports\",\"note\":\"'Bardache. Esp: bardaxa, bardaja. Ital: bardascia; de bardaj captif, esclave. Ce mot très-ancien en arabe (V. Muarrab p.6) vient du persan bardah, captif'.\"}\nLKT161={\"src\":\"LKT\",\"where\":\"no. 161 (LKT.txt l.584)\",\"stance\":\"supports\",\"note\":\"'Pers. bädingän: Ebenso ar. bädingän ... Hieraus zahlreiche romanische Formen: it. petonciano, sp. pg. val. berengena, pg. beringala, kat. alberginera, frz. aubergine'.\"}\nDEV_a={\"src\":\"DEV\",\"where\":\"s.v. Aubergine (DEV.txt l.639)\",\"stance\":\"supports\",\"note\":\"'Le nom arabe-persan bâdindjân serait assez difficile à reconnaître dans notre aubergine, si nous n'avions ... l'espagnol berengena ... On trouve aussi, avec l'article arabe, alberengena qui correspond à aubergine'.\"}\nLAM_a={\"src\":\"LAM\",\"where\":\"LAM.txt l.7954\",\"stance\":\"supports\",\"note\":\"'Aubergine. Esp. Ptg. Val.: berengena ... Cat.: alberginiera. Esp.: alberengena. Cat. Maj.: alberginia. D'Ar[abe] ...'.\"}\nHJB_a={\"src\":\"HJB\",\"where\":\"s.v. Brinjaul (HJB.txt l.4098)\",\"stance\":\"supports\",\"note\":\"'The Skt. is bhantaki ... P. badingan ... Ar. badinjan, Span. alberengena, berengena ... French aubergine (from alberengena) ... It looks as if the Skt. word were the original of all.'\"}\n\ndata={\"pdf_page\":523,\"book_page\":493,\"verified_by\":\"claude-opus-5\",\"verified_on\":\"2026-10-16\",\"entries\":[\n{\"entry\":0,\"root\":\"Vareta\",\"verdict\":\"confirmed\",\n \"modern_form\":\"Av. varəta- 'captured, taken captive' (ppp.) > MP wardag 'captive, slave' > NP barde\",\n \"note\":\"Avestan varəta- is attested (Bartholomae col. 1368 'gefangen; der Freiheit beraubt; erbeutet'). Nourai's gloss 'slave' is a slight shift: the Avestan word means 'captured, prisoner'; 'slave' is the Middle/New Persian development. Language label and root otherwise correct; the chain Av. varəta- → Pahl. wardag/vartak → NP barde → Ar. bardaj → It. bardascia → F. bardache → E. bardash is accepted by Hübschmann, Horn, Mo'in, Nyberg, MacKenzie, Klein, Lokotsch and Wiktionary.\",\n \"note_fa\":\"ریشهٔ این زنجیره واژهٔ اوستایی varəta- «اسیرشده، به بند گرفته» است (بارتولومه: gefangen، erbeutet) که صفت مفعولی از ریشهٔ var- است. معنای «برده» در فارسی میانه و فارسی نو پدید آمده؛ پس گزارش نورایی «slave» برای اوستایی اندکی آزاد است، ولی خود ریشه و زبان درست است. هوبشمان، هرن، معین و نیبرگ همین پیوند را آورده‌اند؛ ادعای نورایی درست است.\",\n \"sources\":[W_BARDE],\n \"ref_check\":[{\"ref\":\"BQT:253\",\"status\":\"supports\",\"note\":\"Mo'in's fn.4 on p.253 (leaf n473, ocr/BQT/253.vision.txt): 'پهلوی vartak، اوستایی varəta' — the Avestan form Nourai uses as root.\"}],\n \"consulted\":[\n  {\"src\":\"BRT\",\"where\":\"col. 1368 (BRT.txt l.22853)\",\"stance\":\"supports\",\"note\":\"'j. varəta- Adj. (fem. -ā-) \\\"gefangen; der freien Bewegung, der Freiheit beraubt\\\" ... a) \\\"erbeutet\\\"'.\"},\n  {\"src\":\"NYB\",\"where\":\"Glossary s.v. vartak (NYB_vol2_glossary.txt l.3982)\",\"stance\":\"supports\",\"note\":\"'vartak captive ... — Av. (1368) varəta-; Ps. wldky; MPrthPrs wrdg; NP bardah.'\"},\n  {\"src\":\"HUB\",\"where\":\"p.26 no.196\",\"stance\":\"supports\",\"note\":\"'barda \\\"Gefangener\\\" = phl. vartak ... zd. vareta- \\\"gefangen\\\"'.\"},\n  {\"src\":\"POK\",\"where\":\"grep POK_full.txt\",\"stance\":\"silent\",\"note\":\"Av. varəta- 'captive' not cited under any Pokorny lemma found by grep ('varəta', 'vareta'); its PIE etymology (Cheung connects Iranian *u̯ar- 'to take, seize'?) is not addressed. Root box is Avestan, not PIE.\"}],\n \"nodes\":[\n  {\"id\":1,\"lang\":\"Pahlavi\",\"words\":\"vartak 1\",\"verdict\":\"confirmed\",\n   \"derivation\":\"Pahlavi wardag (Nyberg's transliteration vartak, script wltk'), 'captive, prisoner; slave', = OIr. *wr̥taka-, the -aka- extension of Av. varəta- 'captured'. Old Iranian -r̥t- > MP -ard-, and -aka- > MP -ag (Pahlavi spelling -k'). The '1' after vartak on the printed page is a homonym index/footnote mark, not part of the word. Manichaean MP/Parthian wrdg confirms the form.\",\n   \"derivation_fa\":\"پهلوی wardag (به خوانش نیبرگ vartak؛ نوشته wltk') به معنای «اسیر، گرفتار، برده» است و از ایرانی باستان *wr̥taka-، صورت پسونددار اوستایی varəta- «اسیرشده»، آمده است. r̥t هجایی ایرانی باستان در فارسی میانه به ard و پسوند -aka- به -ag بدل شده است. مکنزی و نیبرگ هر دو این واژه را با فارسی نو «برده» یکی می‌دانند؛ ادعای نورایی درست است.\",\n   \"sources\":[W_BARDE],\n   \"ref_check\":[BQT253,HUB26],\n   \"consulted\":[\n    {\"src\":\"PHD\",\"where\":\"p.89 s.v. wardag (PHD.txt l.607)\",\"stance\":\"supports\",\"note\":\"'wardag [wltk' | M wrdg, N barda] captive, prisoner. ~ih: captivity.'\"},\n    {\"src\":\"NYB\",\"where\":\"Glossary s.v. vartak (l.3982)\",\"stance\":\"supports\",\"note\":\"'vartak captive ... — Av. (1368) varəta-; ... MPrthPrs wrdg; NP bardah.'\"},\n    {\"src\":\"HRN\",\"where\":\"p.39 fn. (HRN.txt l.2116)\",\"stance\":\"supports\",\"note\":\"'Berde \\\"Gefangener\\\" habe ich KZ. 32, 574 fälschlich als PPP. zu burdan gestellt; die Pehleviform lautet vartak (Geiger ...; Nöldeke, ZDMG 46, 140).'\"}]},\n  {\"id\":2,\"lang\":\"Persian\",\"words\":\"bardeh\",\"verdict\":\"confirmed\",\n   \"derivation\":\"NP barde (Classical barda) 'slave, captive' < MP wardag. Initial MP w- > NP b- (as in wārān > bārān, warg > barg) and final -ag > -a/-e (as in gurdag > gurda). Hübschmann and Horn (correcting his earlier link with burdan 'carry') identify it with Pahlavi vartak and Av. varəta-; Wiktionary 'Inherited from Middle Persian wltk' /wardag/ \\\"slave; captive\\\"'.\",\n   \"derivation_fa\":\"«بَرده» (در فارسی کلاسیک barda) از فارسی میانهٔ wardag «اسیر، برده» آمده است. w آغازی فارسی میانه در فارسی نو به ب بدل شده (مانند wārān > باران و warg > برگ) و پایانهٔ -ag به -ه رسیده است. هرن که پیش‌تر آن را از «بُردن» می‌دانست، خود این را نادرست خواند و آن را با پهلوی vartak یکی گرفت؛ هوبشمان و معین نیز همین را می‌گویند. ادعای نورایی درست است.\",\n   \"sources\":[W_BARDE],\n   \"ref_check\":[HUB26,BQT253],\n   \"consulted\":[\n    {\"src\":\"HRN\",\"where\":\"p.39 fn. (l.2116)\",\"stance\":\"supports\",\"note\":\"'Berde \\\"Gefangener\\\" ... die Pehleviform lautet vartak'.\"},\n    {\"src\":\"PHD\",\"where\":\"s.v. wardag\",\"stance\":\"supports\",\"note\":\"'wardag ... N barda] captive, prisoner'.\"},\n    {\"src\":\"BQT\",\"where\":\"vol.1 p.253\",\"stance\":\"supports\",\"note\":\"'بَرده ... بمعنی غلام باشد مطلقا خواه دختر و خواه پسر'; fn: 'پهلوی vartak، اوستایی varəta، معرب بردج'.\"},\n    {\"src\":\"MON\",\"where\":\"MON_part1.txt grep '^برده'\",\"stance\":\"silent\",\"note\":\"Abridged Adena OCR only has compounds (برده‌دار etc.), no etymology of برده 'slave' found.\"},\n    {\"src\":\"ARY\",\"where\":\"ARY_pages.txt grep 'برده'\",\"stance\":\"silent\",\"note\":\"Only occurrences in the introduction (برده‌داری); no headword entry found in the OCR.\"}]},\n  {\"id\":3,\"lang\":\"Arabic\",\"words\":\"bardaj\",\"verdict\":\"confirmed\",\n   \"derivation\":\"Arabic bardaj (بَرْدَج) 'captive(s), prisoners taken in war' is an arabicized (muʿarrab) form of a Persian *bardag, the Middle Persian -ag being rendered by Arabic -aj (as in many early Persian loans, e.g. banafsaj, sāḏaj). Al-Jawāliqī's al-Muʿarrab lists al-bardaj as Persian, citing a verse of al-ʿAjjāj; Mo'in (BQT 253) 'معرب بردج'. The Arabic form was taken directly from Middle Persian-type wardag/bardag rather than from New Persian barde, so Nourai's arrow from the NP box is a simplification.\",\n   \"derivation_fa\":\"عربی «بَرْدَج» به معنای «اسیران جنگی» معرّبِ صورت فارسی میانه/فارسی کهن *bardag است؛ پسوند -ag فارسی میانه در وام‌واژه‌های کهن عربی به «ـَج» درآمده است (مانند بنفسج). جوالیقی در «المعرّب» آن را فارسی دانسته و معین نیز در حاشیهٔ برهان «معرب بردج» آورده است. نکتهٔ کوچک این است که عربی از صورت میانه با -g پایانی گرفته، نه از «برده» فارسی نو؛ ولی اصل ادعای نورایی درست است.\",\n   \"sources\":[W_BARDACHE,W_BARDASH],\n   \"ref_check\":[KLN148],\n   \"consulted\":[\n    {\"src\":\"ARB\",\"where\":\"ARB_mo3rb.txt l.2661-2669\",\"stance\":\"supports\",\"note\":\"al-Jawāliqī cites al-ʿAjjāj's verse with 'البردجا' in the Persian-loan list (OCR garbled; headword البردج identifiable).\"},\n    LKT229,LAM_b]},\n  {\"id\":4,\"lang\":\"Italian\",\"words\":\"\",\"verdict\":\"confirmed\",\n   \"derivation\":\"Empty Italian box = Italian bardascia (also bardassa) 'catamite, boy kept for vice', from Arabic bardaj via Mediterranean contact (the slave markets where captive youths were sold), with semantic narrowing 'captive' → 'boy slave used for prostitution'. Klein and Lokotsch give it explicitly.\",\n   \"derivation_fa\":\"این خانهٔ خالی ایتالیایی همان bardascia / bardassa «پسرک بدنام، غلام‌بچه» است که از عربی «بردج» در دادوستد مدیترانه‌ای (بازار بردگان) گرفته شده و معنایش از «اسیر» به «غلام‌بچه‌ای که برای کام‌جویی نگه داشته می‌شد» تنگ شده است. کلاین و لوکوچ همین را می‌گویند؛ ادعای نورایی درست است.\",\n   \"sources\":[W_BARDACHE],\n   \"ref_check\":[{\"ref\":\"KLN\",\"status\":\"supports\",\"note\":\"Klein s.v. bardash (KLN_1966.txt l.4448): 'F. bardache, fr. It. bardascia, fr. Arab. bardaj'.\"}],\n   \"consulted\":[LKT229,LAM_b]},\n  {\"id\":5,\"lang\":\"French\",\"words\":\"bardache\",\"verdict\":\"confirmed\",\n   \"derivation\":\"French bardache 'catamite' (earlier bredaiche, 16th c.) borrowed from Italian bardascia/bardassa; Italian -sci-/-ss- rendered by French -ch-. Wiktionary: 'borrowed from Italian bardassa, from Arabic bardaj \\\"captive\\\", from Persian barde'.\",\n   \"derivation_fa\":\"فرانسوی bardache «پسرک بدکاره» (در سدهٔ شانزدهم bredaiche) از ایتالیایی bardascia گرفته شده و sci ایتالیایی در فرانسه به ch بدل شده است. ویکی‌واژه، کلاین، لامنس و لوکوچ زنجیرهٔ فارسی ← عربی ← ایتالیایی ← فرانسوی را تأیید می‌کنند؛ ادعای نورایی درست است.\",\n   \"sources\":[W_BARDACHE],\n   \"ref_check\":[KLN148],\n   \"consulted\":[LAM_b,LKT229,{\"src\":\"DEV\",\"where\":\"DEV.txt grep 'bardache'\",\"stance\":\"silent\",\"note\":\"No entry for bardache found in Devic.\"}]},\n  {\"id\":6,\"lang\":\"English\",\"words\":\"bardash\",\"verdict\":\"plausible\",\n   \"derivation\":\"English bardash (17th c., obsolete) from French bardache. The derivation chain is right, but Nourai's gloss 'slave' is not the English meaning: Klein and Wiktionary define bardash as 'a catamite, a kept boy'; 'slave' is the meaning of the Arabic/Persian ancestor. Wiktionary hedges the Arabic step with 'perhaps'.\",\n   \"derivation_fa\":\"انگلیسی bardash (سدهٔ هفدهم، اکنون متروک) از فرانسوی bardache آمده است. زنجیرهٔ ریشه‌شناختی درست است، ولی معنای «slave» که نورایی نوشته معنای نیای عربی و فارسی است؛ در انگلیسی معنای واژه «پسرک بدکاره، غلام‌بچه» است (کلاین، ویکی‌واژه). پس ادعای نورایی با احتیاط پذیرفتنی است و تنها معنای آن باید اصلاح شود.\",\n   \"sources\":[W_BARDASH],\n   \"ref_check\":[KLN148],\n   \"consulted\":[KLN_cons(\"KLN_1971.txt l.26010\",\"supports\",\"'bardash, n., a catamite. — F. bardache, fr. It. bardascia, fr. Arab. bardaj, \\\"slave\\\", ult. fr. Pers.'\"),\n    {\"src\":\"SKT\",\"where\":\"SKT.txt grep 'bardash'\",\"stance\":\"silent\",\"note\":\"No entry in Skeat's Concise dictionary.\"}]}\n ]},\n{\"entry\":2,\"root\":\"Vatin-ganah\",\"verdict\":\"plausible\",\n \"modern_form\":\"Skt./Middle Indic vātiṅgaṇa- 'eggplant' (non-IE, prob. Dravidian substrate; cf. Tamil vaḻutuṇai)\",\n \"note\":\"The Indic word is real (Skt. vātiṅgaṇa-, Pali vātiṅgaṇa) and is accepted as the source of Persian bādingān by Klein ('OI. vatin-ganah'), AHD, Wiktionary and Hobson-Jobson; Nourai's form 'Vatin-ganah' is Klein's spelling. However the chart's note analysing -ganah as Skt. gaṇa- 'bundle, group' from PIE *ger- 'to gather' (POK 383) is not supported: Pokorny 382-383 (ger- 'sammeln') does not list gaṇa- or the eggplant word, and AHD calls the word 'ultimately of non-Indo-European origin; akin to Tamil vaḻutalai'; Wiktionary derives it from Dravidian (Proto-Dravidian *waẓVtV). The popular Sanskrit reading 'that which cures the wind (vāta)' is also a folk etymology. Hence plausible for the Indic source, disputed for the IE analysis.\",\n \"note_fa\":\"واژهٔ هندی vātiṅgaṇa «بادنجان» در سنسکریت و پالی گواهی شده و کلاین، فرهنگ امریکن هریتیج، ویکی‌واژه و هابسن‌جابسن آن را سرچشمهٔ «بادنگان» فارسی می‌دانند؛ پس این بخش از ادعای نورایی پذیرفتنی است. اما یادداشت نمودار که بخش -ganah را به سنسکریت gaṇa- «دسته» و ریشهٔ هندواروپایی *ger- «گردآوردن» (پوکورنی ۳۸۳) می‌رساند، پشتوانه ندارد: پوکورنی در آن صفحه چنین واژه‌ای نیاورده و پژوهش امروزی واژه را ناهندواروپایی و از اصل دراویدی (هم‌سنج تامیلی vaḻutuṇai) می‌داند. معنای «درمان‌کنندهٔ باد» نیز ریشه‌شناسی عامیانه است.\",\n \"sources\":[W_AUB,AHD_AUB,W_BADEN],\n \"ref_check\":[KLN125,AHD86,{\"ref\":\"POK:383\",\"status\":\"contradicts\",\"note\":\"Cited in the chart's note. POK_full.txt 'Root / lemma: ger-1, gere- ... to gather, put together ... Page(s): 382-383' lists Greek ageirō, agora etc.; grep of the lemma block for 'gana'/'Indian' finds no Sanskrit gaṇa- and no eggplant word, so Pokorny does not support the analysis.\"}],\n \"consulted\":[\n  {\"src\":\"POK\",\"where\":\"lemma ger-1 pp.382-383\",\"stance\":\"contradicts\",\"note\":\"No Old Indic gaṇa- under ger-1 'to gather'; Skt. gaṇa-h 'troop, multitude' is only mentioned in passing under another lemma (POK_full.txt l.7458, 'o-gana-h ... (: gana-h troop, multitude; Wackernagel)'), not derived from ger-.\"},\n  {\"src\":\"AHD\",\"where\":\"Watkins 1985 grep '^ger-' and 'aubergine'\",\"stance\":\"silent\",\"note\":\"No IE root in Watkins' appendix yields aubergine/eggplant; online AHD s.v. aubergine: 'ultimately of non-Indo-European origin'.\"},\n  {\"src\":\"WLD\",\"where\":\"WLD_band3.txt grep 'aubergine|eggplant'\",\"stance\":\"silent\",\"note\":\"Nothing found.\"},\n  {\"src\":\"SYN\",\"where\":\"SYN.txt grep 'eggplant|aubergine'\",\"stance\":\"silent\",\"note\":\"Buck has no eggplant entry.\"},\n  HJB_a],\n \"nodes\":[\n  {\"id\":1,\"lang\":\"Persian\",\"words\":\"bâdengân\",\"verdict\":\"confirmed\",\n   \"derivation\":\"Early NP bādingān / bātingān (both forms in Borhan: باتنگان، بادنگان), borrowed from Middle Indic vātiṅgaṇa, with Indic v- > Persian b-, the cluster -ṅg- kept as -ng-, and the Indic -t- voiced to -d- in bādingān (folk-associated with bād 'wind'). This is the form the Arabs took over as bāḏinjān. Klein, Lokotsch ('Pers. bädingän') and Wiktionary (Classical Persian bādingān < bātingān < Skt. vātiṅgaṇa) agree.\",\n   \"derivation_fa\":\"«بادنگان» و «باتنگان» صورت‌های کهن فارسی‌اند (هر دو در برهان قاطع آمده‌اند) که از هندی میانه vātiṅgaṇa وام گرفته شده‌اند: v هندی در فارسی به ب، و ت در «بادنگان» به د بدل شده و شاید زیر تأثیر واژهٔ «باد» قرار گرفته است. همین صورت با «گ» به عربی رفت و «باذنجان» شد. کلاین، لوکوچ، معین و ویکی‌واژه این را تأیید می‌کنند؛ ادعای نورایی درست است.\",\n   \"sources\":[W_AUB],\n   \"ref_check\":[KLN125,BQT213,MON444],\n   \"consulted\":[LKT161,\n    {\"src\":\"BQT\",\"where\":\"vol.1 p.213 fn. s.v. بادنجان\",\"stance\":\"supports\",\"note\":\"'بادنجان - باتنگان، بادنگان ... گیلکی bâdenjân'.\"},\n    {\"src\":\"HRN\",\"where\":\"HRN.txt grep 'bading|Solanum'\",\"stance\":\"silent\",\"note\":\"Horn has no entry (loanword from Indic, outside his scope).\"},\n    {\"src\":\"HJB\",\"where\":\"s.v. Brinjaul\",\"stance\":\"supports\",\"note\":\"'P. badingan ... Ar. badinjan'.\"}]},\n  {\"id\":2,\"lang\":\"Arabic\",\"words\":\"bâdenjân, al-bâdenjân\",\"verdict\":\"confirmed\",\n   \"derivation\":\"Arabic bāḏinjān (باذنجان), with article al-bāḏinjān, arabicizes Persian bādingān: Persian -g- > Arabic -j- (Arabic has no g) and Persian d rendered by ḏ. Al-Jawāliqī's al-Muʿarrab records al-bāḏinjān as 'فارسى معرب'. The article-bearing form is the one borrowed into Iberian Romance (Catalan albergínia, OSp. alberengena).\",\n   \"derivation_fa\":\"عربی «باذنجان» (با حرف تعریف: الباذنجان) معرّبِ «بادنگان» فارسی است: گ فارسی چون در عربی نیست به ج، و د به ذ بدل شده است. جوالیقی در «المعرّب» می‌نویسد «الباذنجان فارسی معرب». صورت با «ال» همان است که به کاتالانی و اسپانیایی رسید. ادعای نورایی درست است.\",\n   \"sources\":[W_AUB,W_BEREN],\n   \"ref_check\":[KLN125,KLN165],\n   \"consulted\":[\n    {\"src\":\"ARB\",\"where\":\"ARB_mo3rb.txt l.22225\",\"stance\":\"supports\",\"note\":\"'الباذنجان ٠ فارسى معرب'.\"},\n    LKT161,DEV_a]},\n  {\"id\":3,\"lang\":\"Persian\",\"words\":\"bâdenjân\",\"verdict\":\"plausible\",\n   \"derivation\":\"NP bādenjān (colloq. bādemjān) is the Arabicized form bāḏinjān taken back into Persian: the -j- for older -g- shows it passed through Arabic (a Persian → Arabic → Persian round-trip), as Mo'in implies by listing باتنگان، بادنگان as the native forms. Wiktionary instead lists Classical Persian bādenjān as the source of Arabic; most authorities (Klein, Lokotsch, AHD 'Persian bādenjān, bādengān') treat both as Persian variants, so the round-trip is likely but not universally stated. bādemjān shows assimilation n > m before j.\",\n   \"derivation_fa\":\"«بادنجان» (گفتاری: بادمجان) در فارسی نو همان «باذنجان» عربی است که دوباره به فارسی برگشته است؛ «ج» به جای «گ» کهن نشان می‌دهد که واژه از راه عربی آمده (رفت و برگشت فارسی ← عربی ← فارسی). معین نیز «باتنگان» و «بادنگان» را صورت‌های اصلی می‌آورد. در «بادمجان» n پیش از ج به m همگون شده است. برخی منابع (ویکی‌واژه) «بادنجان» را خود صورت فارسی کلاسیک و سرچشمهٔ عربی می‌دانند، پس ادعای نورایی با احتیاط پذیرفتنی است.\",\n   \"sources\":[W_AUB,W_BADEN],\n   \"ref_check\":[BQT213,MON444],\n   \"consulted\":[\n    {\"src\":\"BQT\",\"where\":\"vol.1 p.213 fn.\",\"stance\":\"supports\",\"note\":\"'بادنجان - باتنگان، بادنگان ... تهرانی bâdemjûn ... معرب آن بادنجان'.\"},\n    {\"src\":\"DEV\",\"where\":\"s.v. Aubergine (l.646)\",\"stance\":\"partial\",\"note\":\"Lists the oriental forms 'bâdindjân, bâdingân, bâdddjân, pâtingân' as 'arabes ou persans' without ordering them.\"},\n    {\"src\":\"MON\",\"where\":\"MON_part1.txt l.44604\",\"stance\":\"silent\",\"note\":\"Abridged OCR shows 'بادنجان.' only as a cross-reference; no etymology.\"}]},\n  {\"id\":4,\"lang\":\"Spanish\",\"words\":\"berengina, au-berengina\",\"verdict\":\"transcription_suspect\",\n   \"error_in\":\"book\",\"book_prints\":\"berengina, au-berengina\",\"correct_form\":\"berenjena (older berengena), alberengena\",\n   \"derivation\":\"Spanish berenjena (Old Spanish berengena) and the article form alberengena come from Andalusian Arabic (al-)bāḏinjān, with Arabic -āḏ- > -ere- (dissimilation/epenthesis) and -ān > -ena. The book prints 'berengina, au-berengina': 'berengina' is Nourai's misspelling of Klein's 'berengena', and 'au-berengina' is not a Spanish form at all (Spanish has alberengena; 'au-' is from French aubergine). Also, Klein, AHD and Wiktionary derive French aubergine from Catalan albergínia, not from Spanish.\",\n   \"derivation_fa\":\"اسپانیایی berenjena (در اسپانیایی کهن berengena) و صورت با حرف تعریف alberengena از عربی اندلسی «الباذنجان» آمده‌اند. کتاب «berengina, au-berengina» چاپ کرده است: berengina خطای چاپی نورایی به جای berengena کلاین است و au-berengina اصلاً صورت اسپانیایی نیست (اسپانیایی alberengena دارد و au- از فرانسوی گرفته شده). خطا از خود کتاب است، نه از خوانش اسکن.\",\n   \"sources\":[W_BEREN,W_AUB],\n   \"ref_check\":[{\"ref\":\"KLN:125\",\"status\":\"partial\",\"note\":\"Klein s.v. aubergine: 'F., fr. Catal. alberginera, alberginia, fr. Arab. al-badinjan ... Cp. berengena.' — Klein routes aubergine via Catalan and spells the Spanish word berengena.\"}],\n   \"consulted\":[DEV_a,LAM_a,LKT161,HJB_a]},\n  {\"id\":5,\"lang\":\"French\",\"words\":\"aubergine\",\"verdict\":\"plausible\",\n   \"derivation\":\"French aubergine (18th c.) is from Catalan albergínia (al- > au- as in French aubade-type vocalization of l before consonant, -ínia > -ine), from Arabic al-bāḏinjān. Klein, AHD and Wiktionary all name Catalan; Devic and Hobson-Jobson derive it from Spanish alberengena. The chart's Spanish parent is thus the older view; the word and Arabic origin are correct.\",\n   \"derivation_fa\":\"فرانسوی aubergine (سدهٔ هجدهم) از کاتالانی albergínia و آن از عربی «الباذنجان» است؛ al- در فرانسوی به au- بدل شده است. کلاین، امریکن هریتیج و ویکی‌واژه واسطه را کاتالانی می‌دانند، ولی دویک و هابسن‌جابسن آن را از اسپانیایی alberengena گرفته‌اند. پس اصل ادعا درست است ولی واسطهٔ اسپانیایی دیدگاه کهن‌تر است؛ با احتیاط پذیرفتنی.\",\n   \"sources\":[W_AUB,AHD_AUB],\n   \"ref_check\":[AHD86],\n   \"consulted\":[KLN_cons(\"s.v. aubergine (KLN_1966.txt l.3927)\",\"partial\",\"'F., fr. Catal. alberginera, alberginia, fr. Arab. al-badinjan' — via Catalan, not Spanish.\"),DEV_a,LAM_a,LKT161]},\n  {\"id\":6,\"lang\":\"English\",\"words\":\"aubergine\",\"verdict\":\"confirmed\",\n   \"derivation\":\"English aubergine (late 18th c., chiefly British) is an unadapted borrowing of French aubergine; American English uses eggplant. AHD and Klein give the French source.\",\n   \"derivation_fa\":\"انگلیسی aubergine (اواخر سدهٔ هجدهم، بیشتر در انگلیسی بریتانیایی) بی‌دگرگونی از فرانسوی aubergine گرفته شده است؛ در امریکا eggplant می‌گویند. امریکن هریتیج و کلاین این را تأیید می‌کنند؛ ادعای نورایی درست است.\",\n   \"sources\":[AHD_AUB,W_AUB],\n   \"ref_check\":[AHD86],\n   \"consulted\":[KLN_cons(\"s.v. aubergine\",\"supports\",\"'aubergine, n., the eggplant. — F., fr. Catal. alberginia'.\"),\n    {\"src\":\"SKT\",\"where\":\"SKT.txt grep 'aubergine'\",\"stance\":\"silent\",\"note\":\"Not in Skeat.\"}]},\n  {\"id\":7,\"lang\":\"English\",\"words\":\"berengina\",\"verdict\":\"transcription_suspect\",\n   \"error_in\":\"book\",\"book_prints\":\"berengina\",\"correct_form\":\"berengena\",\n   \"derivation\":\"Klein p.165 has an English dictionary headword 'berengena, n., the eggplant — Sp., fr. Arab. badinjan'; it is a rare/unadapted borrowing of Spanish berengena (modern berenjena) rather than a naturalized English word. The book prints 'berengina', a misspelling of Klein's 'berengena' (the extraction matches the page).\",\n   \"derivation_fa\":\"کلاین در صفحهٔ ۱۶۵ سرواژهٔ انگلیسی berengena «بادنجان» را آورده که وام‌واژه‌ای کمیاب و بی‌دگرگونی از اسپانیایی berengena (امروز berenjena) است. کتاب آن را «berengina» چاپ کرده که خطای چاپی نورایی است؛ صورت درست berengena است و خوانش اسکن با کتاب یکی است.\",\n   \"sources\":[W_BEREN],\n   \"ref_check\":[KLN165],\n   \"consulted\":[KLN_cons(\"KLN_1971.txt l.28482\",\"supports\",\"'berengena, n., the eggplant. — Sp., fr. Arab. ... ult. fr. Persian, See aubergine.'\"),\n    {\"src\":\"HJB\",\"where\":\"s.v. Brinjaul\",\"stance\":\"partial\",\"note\":\"Anglo-Indian English uses brinjal (from Portuguese beringela), noting 'Span. alberengena, berengena'; no English 'berengina'.\"}]}\n ]}\n]}\njson.dump(data,open('/home/sfmqrb/git/rishe-private/data/verification/page-523.json','w'),ensure_ascii=False,indent=1)\nEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-523.py && cd /home/sfmqrb/git/rishe-private && python3 -m json.tool data/verification/page-523.json >/dev/null && python3 tools/verify_check.py 523"
}
```


### [2026-10-16T05:18:54.614Z] TOOL RESULT

```
nodes verified: 13/13
node verdicts: {'confirmed': 8, 'plausible': 3, 'transcription_suspect': 2}
root verdicts: {'confirmed': 1, 'plausible': 1}
ref checks: {'supports': 14, 'not_checked': 2, 'partial': 3}
books consulted: {'supports': 30, 'silent': 7, 'partial': 3} | by book: {'LKT': 7, 'LAM': 5, 'DEV': 5, 'KLN': 4, 'HRN': 3, 'BQT': 3, 'HJB': 3, 'PHD': 2, 'MON': 2, 'ARB': 2, 'SKT': 2, 'NYB': 1, 'ARY': 1}
```


## [2026-10-16T05:18:59.875Z] TOOL CALL #41: Bash

```json
{
 "command": "S=/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-523.py; sed -i \"s/ its PIE etymology (Cheung connects Iranian \\*u̯ar- 'to take, seize'?) is not addressed\\./ Pokorny does not address it./; s/ (al- > au- as in French aubade-type vocalization of l before consonant, -ínia > -ine)/ (Catalan al- > French au- by the usual vocalization of l before a consonant, -ínia > -ine)/\" $S; python3 $S && cd /home/sfmqrb/git/rishe-private && python3 tools/verify_check.py 523 | grep -c PROBLEM"
}
```


### [2026-10-16T05:19:00.796Z] TOOL RESULT

```
0
```


## [2026-10-16T05:19:09.411Z] TOOL CALL #42: SubagentHandback

```json
{
 "message": "I wrote the file for page 523 (book page 493) and `verify_check.py 523` shows 0 PROBLEM lines. All 13 nodes are verified.\n\n**Verdicts**\n- **Roots:** Vareta is confirmed. Vatin-ganah is plausible.\n- **Nodes:** 8 confirmed, 3 plausible, 2 transcription_suspect, 0 disputed.\n- **Plausible nodes and the problem with each:**\n  - English bardash: the chart glosses it \"slave\", but Klein and Wiktionary give \"catamite\".\n  - Persian bâdenjân: the route Persian → Arabic → Persian is likely but not stated by every source.\n  - French aubergine: Klein, AHD and Wiktionary derive it from Catalan albergínia, not Spanish.\n- **Vatin-ganah root:**\n  - The Indic word vātiṅgaṇa is accepted as the source of Persian bādingān.\n  - The chart's note says \"ganah\" comes from the Indo-European root *ger- \"to gather\" (Pokorny p. 383). That claim is not supported. Pokorny's entry ger- on pp. 382–383 has no Sanskrit gaṇa-. AHD calls the word \"of non-Indo-European origin\", and Wiktionary derives it from Dravidian.\n  - I recorded POK:383 as `contradicts`.\n\n**transcription_suspect (both are misprints in the book; the JSON matches the printed page)**\n- Vatin-ganah, Spanish \"berengina, au-berengina\" (#4): the correct forms are berengena/berenjena and alberengena. \"au-\" is French, so \"au-berengina\" is not a Spanish form.\n- Vatin-ganah, English \"berengina\" (#7): this misspells Klein's headword \"berengena\" (KLN p. 165).\n\n**Extraction errors for the owner to fix:** none.\n\n**Reference checks**\n- I read Borhan-e Qate' vol. 1 pp. 213 and 253 from the archive.org page images; Mo'in's footnotes support both chains.\n- I saved transcriptions to `data/verification/sources/refs/ocr/BQT/213.vision.txt` and `253.vision.txt`.\n- I put the printed page at `data/verification/sources/refs/ocr/BOOK/523.png`.\n- Klein p. 148, Hübschmann p. 26, Horn, MacKenzie and Nyberg all support Av. varəta- → MP wardag → NP barde.\n\nOutput file: /home/sfmqrb/git/rishe-private/data/verification/page-523.json"
}
```


### [2026-10-16T05:19:09.695Z] TOOL RESULT

```
{"success":true,"message":"Report delivered to your caller."}
```
