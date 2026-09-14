# Verification process log — verify-page-414


## [2026-09-14T01:08:52.352Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 414 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-414.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-414.json. Write /home/sfmqrb/git/rishe/data/verification/page-414.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 414` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T01:08:53.448Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T01:08:54.276Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T01:08:54.293Z] TOOL RESULT

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


## [2026-09-14T01:08:54.790Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-414.txt"
}
```


### [2026-09-14T01:08:54.815Z] TOOL RESULT

```
1	=== PDF page 414 (book page 384) ===
2	--- entry 0 ---
3	ROOT [Old Persian / Avestan] Ragâ, Rağâ : city of "Ray" south of Tehran.  (refs MON5:636)
4	#1 (parent #0) [Persian] refs=BQT:985; FVF:278 | Ray «ری» : a city south of Tehran ; râzî «رازی» : from Ray ; râzegî «رازگی» : a famous type of grape from Ray | NOTE: "râzegî" was not found in MON.
5	  #2 (parent #1) [Arabic] refs=FVF:278 | râzeqî : a type of grape
6	    #3 (parent #2) [Persian] refs=FVF:278 | râzeqî «رازقی» : a type of grape
7	#4 (parent #0) [Greek] refs=MON5:636 | Râzex : city of Ray ; râzakěne : from Ray
8	--- entry 1 ---
9	ROOT Rağâ -> redirect to Ragâ
10	--- entry 2 ---
11	ROOT [Akkadian] Ragâmu : to call  (refs KLN:1573; AHD:396)
12	#1 (parent #0) [Akkadian] refs=KLN:1573; AHD:396 | Targumânu : interpreter
13	#2 (parent #0) [Aramaic] refs=AHD:396; KLN:1573 | tŭrgemânâ : interpreter
14	  #3 (parent #2) [Arabic] refs=KLN:1573; DOZ:35 | tarjama, tardjama : he translated
15	    #4 (parent #3) [Middle Greek] refs=AHD:396 | dragoumanos
16	      #5 (parent #4) [Latin] refs=AHD:396 | dragumanus
17	        #6 (parent #5) [Old French] refs=AHD:396 | drugeman
18	          #7 (parent #6) [English] refs=AHD:396 | dragoman : an interpreter
19	    #8 (parent #3) [Persian] refs=MON:1064; SOR:37 | tarjomeh «ترجمه» : translation ; motarjem «مترجم» : translator ; tarjom «ترجم (ترجمان)» : speech, statement
20	  #9 (parent #2) [Hebrew] refs=KLN:1573 | targum : translation (of the old testament)
21	    #10 (parent #9) [English] refs=KLN:1573; AHD:1316 | Targum : Aramaic translations of the Old Testament ; Targumist
22	
```


## [2026-09-14T01:08:58.240Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-414.json && echo \"=== MATRIX ===\" && cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source JSON and source matrix"
}
```


### [2026-09-14T01:08:58.331Z] TOOL RESULT

```
{
  "pdf_page": 414,
  "book_page": 384,
  "entries": [
    {
      "root": {
        "name": "Ragâ, Rağâ",
        "lang": "Old Persian / Avestan",
        "refs": "MON5:636",
        "gloss": "city of \"Ray\" south of Tehran."
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "BQT:985; FVF:278",
          "words": [
            {"translit": "Ray", "gloss": "a city south of Tehran", "script": "ری"},
            {"translit": "râzî", "gloss": "from Ray", "script": "رازی"},
            {"translit": "râzegî", "gloss": "a famous type of grape from Ray", "script": "رازگی"}
          ],
          "script_extra": null,
          "note": "\"râzegî\" was not found in MON.",
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Arabic",
          "refs": "FVF:278",
          "words": [
            {"translit": "râzeqî", "gloss": "a type of grape", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "FVF:278",
          "words": [
            {"translit": "râzeqî", "gloss": "a type of grape", "script": "رازقی"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Greek",
          "refs": "MON5:636",
          "words": [
            {"translit": "Râzex", "gloss": "city of Ray", "script": null},
            {"translit": "râzakěne", "gloss": "from Ray", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {"root": {"name": "Rağâ", "redirect": "Ragâ"}, "nodes": []},
    {
      "root": {
        "name": "Ragâmu",
        "lang": "Akkadian",
        "refs": "KLN:1573; AHD:396",
        "gloss": "to call"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Akkadian",
          "refs": "KLN:1573; AHD:396",
          "words": [
            {"translit": "Targumânu", "gloss": "interpreter", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Aramaic",
          "refs": "AHD:396; KLN:1573",
          "words": [
            {"translit": "tŭrgemânâ", "gloss": "interpreter", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Arabic",
          "refs": "KLN:1573; DOZ:35",
          "words": [
            {"translit": "tarjama, tardjama", "gloss": "he translated", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Middle Greek",
          "refs": "AHD:396",
          "words": [
            {"translit": "dragoumanos", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Latin",
          "refs": "AHD:396",
          "words": [
            {"translit": "dragumanus", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Old French",
          "refs": "AHD:396",
          "words": [
            {"translit": "drugeman", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "English",
          "refs": "AHD:396",
          "words": [
            {"translit": "dragoman", "gloss": "an interpreter", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 3,
          "lang": "Persian",
          "refs": "MON:1064; SOR:37",
          "words": [
            {"translit": "tarjomeh", "gloss": "translation", "script": "ترجمه"},
            {"translit": "motarjem", "gloss": "translator", "script": "مترجم"},
            {"translit": "tarjom", "gloss": "speech, statement", "script": "ترجم (ترجمان)"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "غیر حرف و غیر ایما و سجلّ - صد هزاران ترجمان خیزد ز دل",
            "poet": "Molavî"
          }
        },
        {
          "id": 9,
          "parent": 2,
          "lang": "Hebrew",
          "refs": "KLN:1573",
          "words": [
            {"translit": "targum", "gloss": "translation (of the old testament)", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 9,
          "lang": "English",
          "refs": "KLN:1573; AHD:1316",
          "words": [
            {"translit": "Targum", "gloss": "Aramaic translations of the Old Testament", "script": null},
            {"translit": "Targumist", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
=== MATRIX ===
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


## [2026-09-14T01:09:01.638Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['MON','BQT','FVF','KLN','AHD','DOZ','SOR','FVQ']:\n    print('===',k, json.dumps(d.get(k),ensure_ascii=False,indent=1))\n\""
}
```


### [2026-09-14T01:09:02.753Z] TOOL RESULT

```
=== MON {
 "title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)",
 "kind": "website+archive_djvu",
 "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)",
 "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks).",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt"
 ],
 "page_offset": null,
 "covers_etymology": true,
 "notes": "covers_etymology = partial: origin-language tag visible online, Latin etyma missing. The a'lam volumes (MON5/MON6 citations, e.g. MON5:528) are NOT online: vajehyab's Mo'in has no proper-name entries (tested افراسیاب — only compounds returned); abadis shows Dehkhoda and 'فرهنگ اسم‌ها' instead, which do give Avestan forms (e.g. Frangrasyan) and can serve as a cross-check. noorlib has no Mo'in 6-vol entry found. The 6-vol edition itself was not found on archive.org, Google Books or HathiTrust full view. || RE-SEARCH 2026-09: still no scan of the 6-vol Amir Kabir edition (incl. vols 5-6 اعلام) on archive.org, Google Books (API quota-limited; WebSearch found no record with preview), HathiTrust (no record surfaced), noorlib, ketabnak (author page persons/6040 lists 34 Mo'in titles, none the 6-vol فرهنگ), tarikhema, picofile, scribd, Commons/Wikisource. Only the 2-vol Adena condensation exists (archive.org, mirrored on ketabnak 65980/65981, picofile, persianpdf, scribd); its image PDFs were downloaded to incoming/MON/ (the _text.pdf variants with OCR layer are at the same archive.org identifiers). The 6-vol set is purchase-only (in print: iketab.com, bookroom.ir/book/97022, 30book.com/Book/32100).",
 "cites": "page number of Mo'in's six-volume Farhang-e Farsi; MON5:… / MON6:… = volume 5 / 6 (proper names)"
}
=== BQT {
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
=== FVF {
 "title": "S.M.A. Emam Shushtari, Farhang-e Vazheha-ye Farsi dar Zaban-e Arabi, Anjoman-e Asar-e Melli 58, Tehran 1347/1968",
 "kind": "website",
 "url": "https://noorlib.ir/book/info/105056 (page viewer: https://noorlib.ir/book/view/105056?pageNumber=<N>&viewType=pdf) ; https://ketabnak.com/book/48613 (818 pp. PDF, login) ; http://parsianjoman.org/?p=1265 (download post)",
 "lookup_hint": "Alphabetical by Persian headword; noorlib page number N is the scan page — browser needed to read. Not on archive.org.",
 "local_file": null,
 "page_offset": null,
 "covers_etymology": true,
 "notes": "PDF exists on several Iranian sites (ketabnak/parsianjoman) but could not be fetched here (login/JS)."
}
=== KLN {
 "title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67",
 "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein",
 "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt",
 "page_offset": "KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.",
 "notes": "Other 1966 IA copies (comprehensiveety01klei/02klei etc.) are lending-only (401/403). local_files: /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt (paginated by leaf); /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1971.txt (plain djvu.txt, no page marks)",
 "local_files": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1971.txt"
 ],
 "cites": "page number, continuous across the two volumes (1966–67)"
}
=== AHD {
 "title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)",
 "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)",
 "kind": "archive_djvu+website+archive_restricted",
 "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only",
 "identifier": "watkins-american-heritage-dictionary-of-indo-european-roots-1985",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt",
 "page_offset": "1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.",
 "lookup_hint": "Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves = original 1969 ed.).",
 "notes": "AHD is by far the most cited source (1906). Root order is alphabetical in all versions, so root-name lookup is reliable; page numbers can only be checked against a borrowed copy of the 1976 New College Edition. || RE-SEARCH 2026-09: no open scan of the New College Edition; three borrowable copies on archive.org (avoid the ~840-pp Dell abridgements, which lack the appendix). Local proxy remains AHD_watkins1985.txt.",
 "cites": "page number of the 1975/76 New College Edition; pp. 1505–1550 are the Indo-European roots appendix (look the root up by name)"
}
=== DOZ {
 "title": "R. Dozy, Oosterlingen: Verklarende lijst der Nederlandsche woorden die uit het Arabisch, Hebreeuwsch, Chaldeeuwsch, Perzisch en Turksch afkomstig zijn, Leiden 1867",
 "edition_found": "1867",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/oosterlingenver00dozygoog",
 "identifier": "oosterlingenver00dozygoog (also ...01dozygoog, ...02dozygoog)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/DOZ.txt",
 "page_offset": "leaf = printed + 11..13 (e.g. leaf 15 = p.2, leaf 43 = p.32). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Dutch headword in caps at line start.",
 "notes": "Built from djvu.xml."
}
=== SOR {
 "title": "K. Akhavan Zanjani — title unknown (Table IV entry for SOR lost in OCR; listed under Persian authors)",
 "kind": "none",
 "url": null,
 "lookup_hint": "Author search on archive.org/web found nothing.",
 "local_file": null,
 "page_offset": null,
 "covers_etymology": false,
 "notes": "none online; title unidentified."
}
=== FVQ {
 "title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)",
 "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ.txt"
 ],
 "page_offset": "printed page = leaf − 17 (0-based \\f blocks in FVQ_pages.txt; 335 leaves)",
 "covers_etymology": true,
 "notes": "Good English OCR (Arabic script garbled). Same 1938 edition Nourai cites.",
 "cites": "page number of Jeffery, The Foreign Vocabulary of the Qurʾān (1938)"
}
```


## [2026-09-14T01:09:51.870Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN dragoman ===\"; grep -n -i \"dragoman\\|drugeman\\|dragoumanos\\|targum\\|turgeman\\|ragamu\" KLN_1966.txt | head -40\necho \"=== SKT ===\"; grep -n -i \"dragoman\\|targum\" SKT.txt | head -20\necho \"=== AKD (Zimmern) ===\"; grep -n -i \"targum\\|ragamu\\|rag[aā]mu\\|turgem\" AKD.txt | head -30\necho \"=== AFA (Fraenkel) ===\"; grep -n -i \"targum\\|turgem\\|tardschum\\|tarǧum\" AFA.txt | head -20\necho \"=== LKT ===\"; grep -n -i \"dragoman\\|drogman\\|targum\" LKT.txt | head -20"
}
```


### [2026-09-14T01:09:52.013Z] TOOL RESULT

```
=== KLN dragoman ===
12209:Derivative :  dragg-ly,  adv. dragoman,  n.,  guide  and  interpreter.  —  F.  drago¬ man,  drogman,  fr.  It.  dragomano,  fr.  MGk. Spayoupavo^,  fr.  targumdn,  Egypt,  pronuncia¬ tion  of  Arab,  tarjumdn,  fr.  Aram.  turghlmanA,  ult. fr.  Akkad,  largumdnu,  ‘interpreter’.  See  Targum. dragon,  n.  —  OF.  (=  F.),  fr.  L.  draconem,  acc. of  draco,  ‘a  kind  of  a  serpent ;  dragon’,  fr.  Gk. Spaxcov,  which  prob.  means  lit.  ‘the  sharp- sighted  one’,  and  is  rel.  to  S^pxeaHai,  ‘to  look at’,  fr.  I.-E.  base  *derk-,  *dpk-,  ‘to  see,  look  at’, whence  also  01.  dars-,  ‘to  see’,  da-darsa,  ‘I  have seen’,  darsatah,  ‘visible’,  dps-,  ‘seeing,  sight’, Avestic  darshti-,  ‘sight’.  Alb.  drite  (for  *dpkta-), ‘light’,  Goth.  ( ga)tarhjan ,  ‘to  make  distinct’, OE.  torht,  ‘bright’,  OHG.  zoraht,  ‘clear’,  OIr. derc,  ‘eye’,  W.  drych,  ‘aspect’,  drem,  Bret. dremm  (for  *dpk-sma),  ‘face’.  Cp.  darshana, Dracaena,  Dracontium,  dracunculus,  dragoon, drake,  ‘dragon’,  rancle,  tarragon.
23034:Mary,  fem.  PN.  —  ME.  Marie,  fr.  OE.  Maria, Marie,  fr.  L.  Maria,  fr.  Gk.  Mapiap,  Mapta, fr.  Aram.  (Targum)  Maryam,  fr.  Heb.  Miryam, which  is  of  uncertain  origin.  See  Miriam,  and cp.  Marianne,  Marion,  marionette, marzipan,  n.  —  See  marchpane.
23783:-metry,  combining  form  denoting  the  process  oj measuring  (as  specified  by  the  first  element  of the  compound  ending  in  -metry).  —  ME.  -me- trie,  fr.  MF.  (=  F.)  -me trie,  fr.  L.  -metria,  Gk. -jAExpfa,  ‘ameasuring  of’,  fr.-pixpT);,  ‘measurer of’,  fr.  pixpov  ‘measure’.  See  meter,  ‘poetical rhythm’,  and  cp.  -meter,  ‘measuring  instrument’, mettle,  n.,  disposition,  spirit.  —  A  var.  of  metal. Derivatives:  mettl-ed,  adj.,  mettlesome,  adj., mettle-some-ly,  adv.,  mettle-some-ness,  n. meturgeman,  n.,  an  official  of  the  early  Jewish synagogue  who  translated  into  Aramaic  the verses  read  from  the  Scriptures  in  Hebrew.  — Aram.  m6thurgeman,  inexact  spelling  of  m  thor- geman,  ‘interpreter’,  which  is  a  blend  of  targ  - man  and  Heb.  mlthargem;  see  Targum.  See Bacher,  Exegetische  Terminologie,  vol.  1 ,  p.  206, note  2.
25117:necrosis,  n.,  the  death  of  bodily  tissue.  —  Gk. vExpcocic,  ‘a  becoming  dead,  state  of  death’,  fr. vExpouv,  ‘to  make  dead,  to  mortify’,  fr.  vexpoc, ‘dead’.  See  necro-  and  -osis. necrotic,  adj.  —  See  prec.  word  and  -otic, nect-,  form  of  necto-  before  a  vowel, nectar,  n.,  the  drink  of  the  gods  (Greek  mythoi) —  L.,  fr.  Gk.  vEx-rap,  ‘drink  of  the  gods’,  esp. ‘wine’,  which  prob.  derives  fr.  Heb.  (yayin)  niq- tar,  ‘smoked  (wine),  perfumed  (wine)’,  Niph‘al (=  passive  form)  of  the  Sem.  base  q-t-r,  ‘to make  sacrifices,  smoke’;  qitter  and  hiqtir ,  ‘he made  sacrifices,  smoked’,  are  Pi’el  (=  intensive form),  resp.  Hiph‘il  (=  causative  form)  of  the same  base,  whence  also  ql/Oreth,  ‘sweet  smoke of  sacrifice,  incense’,  Talmudic  and  Targumic Aram,  qitra,  ‘(thick)  smoke’,  Ethiop.  qetare.
31568:Derivatives :  rag,  n.,  ‘joke’,  ragg-er,  n.,  ragging,  n. ragamuffin,  n.,  a  stupid  person.  — -  Fr.  Ragamof- fyn,  name  of  a  demon  in  old  mystery  plays, which  is  prob.  a  compound  of  rag,  ‘tatter’,  and moffyn,  a  word  of  uncertain  origin  and  meaning, rage,  n.  —  ME.,  fr.  OF.  (=  F.)  rage,  fr.  VL.  rabia, fr.  L.  rabies,  ‘rage,  madness’,  fr.  rabere,  ‘to  be mad,  to  rave’.  See  rabid  and  cp.  rabies. Derivatives:  rage,  intr.  v.,  rag-er,  n.,  rag-ing-ly , adv.
32598:Derivatives:  retaliat-ion,  n.,  retaliat-ion-ist,  n., retaliat-ive ,  adj.,  retaliat-or,  n.,  retaliat-ory,  adj. retama,  n.,  genista.  —  ModL.,  fr.  Sp.  retama,  fr. Arab.  rdtamah,  in  vulgar  pronunciation  retama, ‘a  shrub  of  the  genus  Genista’,  nomen  unitatis (=  noun  of  individuality),  fr.  ratam,  ‘the  genus Genista,  the  broom  plant’,  which  is  rel.  to  Heb. rothem,  Aram.  (Targum)  rathma,  rithma, ‘broom  plant’.
34605:Sephardim,  n.  pi.,  descendants  of  the  Jews  who lived  in  Spain  and  Portugal.  —  Inexact  render¬ ing  of  ModHeb.  S6 pharaddim,  ‘Spaniards;  Jews of  Spain’,  pi.  of  Sepharaddf,  fr.  Heb.  Sephdrddh, mentioned  in  Obadiah,  v.  20,  and  prob.  mean¬ ing  ‘Asia  Minor’  or  a  country  in  it  (perhaps Lydia  or  Phrygia),  but  identified  by  the  Jona¬ than  Targum  with  Spain.
34872:Shamash,  n.,  the  chief  sun  god  of  Assyria  and Babylon.  —  Akkad,  shamash,  shamshu,  ‘sun; the  god  of  the  sun’,  rel.  to  Heb.  shemesh,  ‘sun’, Aram.shimsha,  Syr.  shemshd,Vgar.  sh-p-sh,  Arab. shams  (dissimilated  fr.  *shamsh),  of  s.m.;  prob. from  the  Semitic  base  s-m-s-m,  ‘to  be  swift’  (said of  the  quivering  sunrays).  Aram,  shumshdna, Arab,  sumsum,  Aram.  shumsh6mdna  (whence through  syncope  shumshdna,  whence  through metathesis  shushmana),  ‘ant ,  are  of  the  same base.  See  Fleischer,  Beitrage  zu  Jacob  Levy’s Worterbuch  iiber  die  Targumim,  II,  pp.  577f. Cp.  Samson.
34955:eighth  day  of  this  festival,  observed  on  the  22nd day  of  Tishre.  —  Heb.  shemini 'atzereth  (so  call¬ ed  after  Num.  29  :  35),  fr.  shemini,  ‘the  eighth (scil.  day)’,  fr.  shembna1',  ‘eight’  (see  tomin),  and 'atzereth,  ‘festive  assembly’,  which  derives  from the  verb  atzar,  ‘he  restrained,  kept  back,  stop¬ ped’,  and  prob.  means  lit.  ‘stoppage  (of  work)’, in  reference  to  the  abstention  from  hard  work prescribed  for  this  day;  see  Num.  29 :  35.  Heb. ‘atzar  is  rel.  to  Mishnaic  Heb.  'atzar,  ‘he  pressed, squeezed’,  and  to  Aram.  (Targum)  and  Syr. ‘atzar,  ‘he  squeezed,  pressed  out,  crushed’,  Arab. asara,  Ethiop.  'asara,  ‘he  pressed’,  Akkad,  eferu, ‘to  retain,  restrain’.
38215:Targum,  n.,  Aramaic  translation  of  the  Bible.  — Mishnaic  Heb.  targum,  ‘interpretation,  transla¬ tion’,  fr.  Heb.  tirgem,  ‘he interpreted,  translated’, which  is  rel.  to  Aram,  targem,  Arab,  tarjama,  of s.m.  All  these  verbs  are  denominated  fr.  Akkad. targumanu,  ‘interpreter’  (fr.  ragamu,  ‘to  call'), whence  also  Aram.  turgi mdna,  ‘interpreter, translated.  Cp.  meturgeman.  Cp.  also  dragoman. Derivatives:  Targum-ic,  adj.,  Targumist  ( q.v.)
38216:Targumist,  n.,  1)  writer  of  a  Targum;  2)  student of  the  Targums.  —  Formed  fr.  Targum  with suff.  -ist.
38217:Derivative:  Targumist-ic,  adj.
=== SKT ===
5380:Drayman,  an  interpreter.  (Span.  -• Gk.  — Arab.)  Span,  dragoman.  ••  Kote  Gk. Zpa'^vtiavo^,  an  interpreter,  «•  Arab,  tar- tmm^fU  an  interpreter,  translator ;  ace Targum.
11005:Uammon.  (L.-Gk.— S>Tiac.)  L.  wiaw- motm.  a>  Gk.  fiatnavax,  Mnlt.  vi.  34.  ■>  Syr* mam*}ft4.  which  occurs  in  Chaldee  Targums, and  in  the  Syriac  version  of  St.  Matthew, atxl  means  '  riches.*  Cf.  Hcb.  matfntfri,  a hidden  treasure,  from  tdman,  to  bide.
19201:Targum,  a  ChaUIcc  paraphrase  of  the Old  Testament  (Chaldee.)  Chaldee  tar- gdm^  an  interpretation.  — Chal.  targhn,\.o interpret.  Cf.  Arab,  tarjum^,  an  inter- preter; see  Dragoman.
=== AKD (Zimmern) ===
58:an  den  Grenzen  der  klassischen  Welt  nicht  Halt  gemacht  hat,  sondern auf  gewissen  Gebieten  auch  nach  Griechenland  und  weiter  nach  Rom  hin- über gegriffen  hat,  dafür  sind  an  ihrem  Teile  die  ins  Griechische  und Lateinische  eingedrungenen  babylonischen  Fremdwörter  mehrfach  beredte Zeugen.  Auf  diesem  Wege,  über  Hellas  und  Rom,  andererseits  aber  auch durch  das  Arabische  und  den  Islam,  ferner  durch  die  Bibelsprache,  endlich durch  den  jüdischen  Jargon  und  die  Gaunersprache  hindurch,  haben  sicli mm  auch  eine  ganze  Anzahl  solcher  urspmnglich  akkadischer,  ja  vereinzelt sogar  auch  sumerischer  Wörter  bis  in  die  heutigen  europäischen  Sprachen, speziell  auch  bis  ins  Deutsche  erhalten.  Aus  den  folgenden  Listen,  die liierin  freilich  Vollständigkeit  keineswegs  beanspruchen,  kann  ja  leicht  ent- nommen werden,  in  welchem,  naturgemäß  immer  nur  bescheidenen,  Maße ui-sprüngiich  babylonische  Bestandteile  sich  sogar  in  unseren  modernen Sprachen  noch  vorfinden,  sei  es  in  der  Gestalt  von  wirklichen  Lelmwöi-tern, sei  es  in  der  Form  von  Übersetzungen  ursprünglich  babylonischer  Aus- drücke. Der  Löwenanteil  bei  der  folgenden  Aufzählung  von  akkadischen Lehnwörtern  wird  aber  aus  leicht  begreiflichen  Gründen  denjenigen  Sprachen zufallen,  deren  Ti'äger  als  nächste  Nachbarn  jahrhundertelang  unter  dem unmittelbaren  Einfluß  der  babylonisch-assyrischen  Kultur  gestanden  liaben, d.  h.  insbesondere  dem  Kanaanäischen  (in  der  Hauptsache  vertreten  durch das  Hebräische  und  das  Phönizische)  und  dem  Aramäischen  (wovon  das  Sy- rische einen  Hauptvertreter  bildet).  Aus  dem  Aramäischen  sind  die  gleichen, dem  Babylonischen  entlehnten,  Kulturwöiier  dann  vielfach  weiter  ins  Ara- bische als  Lehnwörter  übergegangen,  sodaß  die  „aramäischen  Fremdwörter im  Arabischen"  sich  jetzt  in  vielen  Fällen  im  letzten  Grande  als  entlehnte babylonische,  akkadische  Wörter  herausstellen.
88:akk.  targumänu,  turgumütm  Dolmetscher  :  >  aram.  targamänä, turgdmänä  O  arab.  targamän,  targuman,  turgumän,  woraus  auch  unser Dragoman);  dazu  neuhebr.  targüm  Übersetzung,  „Targum".
=== AFA (Fraenkel) ===
1190:im Targumischen noch mit der griechischen Endung N^D/ilOI
1604:Der naturgemäss zu erwartende Gegensatz zwischen der
2667:Glasgeßlsse können aber naturgemfiss für den Beduinen
2779:findet sich ausser dem Targum in einigen ganz aramäischen
7737:Negä'im 12, 1 »targumisch f&r D^^niT*) und dasHäi LL
8188:selbst, sind dem Beduinen naturgemäss fremde Dinge. Eine
8401:turgeMchiekU I. p. 219 andeutet Ma^ erwartet zunächst ^
8804:als ^iJäXfi erkannt, yermittelt durch /QTK (targumisch und tal-
9006:als ^A^Ajf erkannt, vermittelt durch /QTK (targumisch und tal-
9954:139) Mii^arr. 05 ist entlehnt aus XpV (targumische Über-
=== LKT ===
4574:'Ausleger,  Dolmetscher'  [Vb.  targama 'dolmetschen'  aus  syr.  targem  'erläutern', vgl.  targüm  'Erläuterung,  Erklärung'; beachte  assyr.  ragämu  'sprechen',  rigmu 'Wort',  eigentlich  'schreien,  rufen';  'Ge- schrei, Ruf,  DelHWB  612  a,  sowie  assyr. targumänu  'Dolmetsch',  ebenda  713  a]; hieraus  it.  dragomanno,  turcimanno  [mit Anlehnung  au  turco  'Türke'],  prov. drogoman,  frz.  drogoman,  drogman, trucheman,  kat.  sp.  drogoman,  trujaman, pg.  dragomano,  trugimäo;  engl,  drogo- man, druggerman,  ndl.  drogoman,  drog- man, dtsch.  Dragoman,  (älter)  Dnitzel- mann,  Trutschelmann;  russ.  dragoman. [DE  351.  Eguilaz  508.  ML  8580. Kluge  96.
5495:takwlm  1999 'ta'lab  12001 talak  "lOO'A taläk  2U04 'talbls  ;200ü taira  5>007 ta'lim  !2008 tama'  !2009 /awäm  2010 tamannä  "iOll towr  2013 fawiwr  483.  2015 tannln  2018 tannür  2019 tantana  2020 teraf  2023 ia;-«Ä«  2024 tarahsakün  2025 taranguhvn  2028 <ar6  1344.  2030 terÖMS  2031 iarfä'  2032 targama  2033 targumän  2033 ia>7i  2024 torÄM»  2034 iarfrfa  2036 taV?/'  2037 tarllta  2038 tarirna  2039 iarsl'  170ß iartifo  2041 ^ösr«;  2044 tasannug  579 tasblk  1970 iasßm  2008 te^6lÄ;a  2046 iawr  2048 tausija  2050 tawätur  2053 <ay»n  1994 ßft  2074 i«ör  2075 tilasm  2077
5518:targumänu  2033 tinüru  2019.
5770:Dragoman  2033 Dragun  2034 Dro^ffi  549 Drutzelmann  2033 Dschagi  2169 Dschiggetai  639 Dschiu- Dschitsu  963 Dschungel  933 Dschunke  753 D.scÄ»fe  693 Dm«;-  502 D?^W»e  St.  535 dudeln  536 Dudelsack  536 rfM/^i  j.  2084 Dtigong  541 Dumdum  476 Dmws  1927
7046:dragomanno  2033
7298:I  darqa  485 I  dmc^t  909 i  dragoman  2033
8003:dragomano  2033
```


## [2026-09-14T01:10:03.556Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== leaf of KLN line 38215 ===\"; awk 'NR<=38215' KLN_1966.txt | tr -cd '\\f' | wc -c\necho \"=== leaf of KLN line 12209 ===\"; awk 'NR<=12209' KLN_1966.txt | tr -cd '\\f' | wc -c\necho \"=== DOZ ===\"; grep -n -i \"drogman\\|dragoman\\|tardjem\\|targum\" DOZ.txt | head -20\necho \"=== FVQ tarjama ===\"; grep -n -i \"tarjama\\|turgeman\\|targum\\|tarjumān\\|tarjuman\" FVQ_pages.txt | head -20\necho \"=== PHN/DEV ===\"; grep -n -i \"drogman\\|truchement\\|dragoman\" PHN.txt DEV.txt | head -20"
}
```


### [2026-09-14T01:10:04.728Z] TOOL RESULT

```
=== leaf of KLN line 38215 ===
834
=== leaf of KLN line 12209 ===
263
=== DOZ ===
1127:DRAGOMAN of DBOGMAN.
1128:In het Arab. tardjemdn, tardjomdn en tordjamdn,
1131:Onze vormen hebben wg van de Fr. (dragoman ook
1701:het het hoofddeksel der drogmans, der geneesheeren.56
=== FVQ tarjama ===
215:Krauss, S. Grifchische und lateinische Lehnworter im Talmud, Midrasch und Targum,
229:Levy, J. Chalddisches Worterbuch -liber die Targumim, 2 vols. Leipzig, 1837.
366:TW Targumisches Worterbuch, ed. Levy.
1924:of the Targums is the equivalent of Heb. 3K from 33X to be green
1926:Arabia word was a direct borrowing from the Targumic fcO^X but tin*
2829:doctrine, 4 though the word would seem to have arisen from the Targumic
3367:sponds with the Aram. NT13 used, e.g., in the Targums on Prov. xii,
3449:used in the Targums and Rabbinic literature for HSn. Geiger has been
3638:oven, i.e. the Gk. jcA/jSapo?, and the form in the Aram. Targums is
3811:"112, but the Targums read &OJ or &Q13, and the Peshitta has
4062:Christian tradition. As early as the Targums we find that the
4194:to be hard, rough. In the Targums N30TI is a store or warehouse,
4570:dTrocrToAijs, where the Peshitta reads ]loA>j. The Targumic HQ^nn
5167:or pafitS&vei, which seems to be formed from the Targumic 113"] , l
5264:and as Hirschfeld, Beitrage, 38, notes, it is also so used in the Targums
5267:equivalent of the Targumic ]QmQ and in Lk. vi, 36, translates
5389:1 Cf. the Targumic KIWI Dpi.
5876:Targums and Rabbinical writings for both a short time x and an hour,
6346:and in the Talmud and Targums WSO and XWEJO are commonly
6542:Targums (Ahrens, Christliches, 25).
=== PHN/DEV ===
DEV.txt:767:Barat.  tt Patente  de  drogman  délivrée  parles  consuls européens  à  des  sujets  du  Grand-Seigneur.  ??  (Douillet, Dict.  scienc.)  C'est  le  turc  e:>pîw  barât,  lettre,  diplôme royal,  qui   accorde  un  privilège;   de  l'arabe   «U   barda,
DEV.txt:1230:Drogman  ou  Dragoivian.  Ce  mot  et  son  équivalent  tru- chement représentent  l'arabe  (ji^y  lardjaman,  tardjouman, tourdjouman.  Esp.  trujaman,  ital.  drogmano,  dragomano, turcmanno;  bas  lat.  dragumanus ,  drocmandus ,  turchimannus ; bas  grec  Spayovixotvo?,  vieux  français  (xn^  et  xiif  siècles) driighemant,  drugcmcnt;  on  a  dit  /r^fc/zemen^  dès  le  xv'' siècle. La  racine  sémitique  du  mot  (jl^yj  tardjamân  se  retrouve dans  le  nom  de  targiim  qu'on  donne  à  la  paraphrase  clial- daïque  de  la  Bible  et  qui  signifie  interpréta  lion  ^.
DEV.txt:3368:Apayov(xixvos ,  voy.  Drogman.
DEV.txt:3370:Dragoman,  voy.  Drogman.
DEV.txt:3371:Dragomano,  ital.  voy.  Drogman.
DEV.txt:3372:Dragumanus,  b.  lat.  voy.  Drogman.
DEV.txt:3376:Drocmahdus,  b.  lat.  voy.  Drogman.
DEV.txt:3377:Drogman.
DEV.txt:3378:Drogmano,  ital.  voy.  Drogman.
DEV.txt:3379:Drugement,  voy.  Drogman.
DEV.txt:3380:Drughemant,  voy.  Drogman.
DEV.txt:4409:Targone,ùa/.  voy.  Estragon. Targum,  voy.  Drogman. Tari,  vov.  Téréniabin. Tarif.
DEV.txt:4428:Trinca ,  langued.  voy.  Matraca ,  note. Tringibin,  voy.  Téréniabin. Tripan,  voy.  Trépang. Trique,  troquer,  voy.  Matraca ,  noie. Truca,  langued.  voy.  Matraca,  note. Truchement,  voy.  Drogman. Trujaman,  esp.  voy.  Drogman. Trunjibin,  voy.  Téréniabin. Tumbaga,  esp.  voy.  Tombac. Tv(n:avov,  voy.  Timbale. Turbich,  b.  lat.  voy.  Turbilh. Turbit,  esp.  voy.  Turbith.
DEV.txt:4431:Turcasia,  b.  lat.  voy.  Carquois. Turcasso ,  ital.  voy.  Carquois. Turchimannus,  b.  lat.  voy.  Drog- man. Turcimanno,  ital.  voy.  Drogman. Turcoman,  voy.  Turc. Turpethum,  lat.  bot.  voy.  Turbith. Turquois,  voy.  Carquois. Tutonaga ,  pg.  voy.  Toutenague. Tutia,  hisp.  voy.  Tutie.
DEV.txt:4691:□3 in  voy.  Drogman.
DEV.txt:4692:(jlyr-j  voy.  Drogman.
PHN.txt:3863:quie , avec plusieurs modifications, par les drogmans, les méde-
PHN.txt:4433:DROGMAN, 8. m. (a.)
PHN.txt:4435:prêter, traduire. — Le mot drogman ne se dit guère que d'un
PHN.txt:4439:français , les variantes trucheman et truchement; mais , comme elles
```


## [2026-09-14T01:10:16.906Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== DOZ leaf for line 1127 ===\"; awk 'NR<=1127' DOZ.txt | tr -cd '\\f' | wc -c\necho \"--- DOZ dragoman entry ---\"; sed -n '1125,1140p' DOZ.txt\necho \"=== KLN leaf 798 head ===\"; awk 'BEGIN{RS=\"\\f\"} NR==799' KLN_1966.txt | head -5\necho \"=== KLN leaf 835 head ===\"; awk 'BEGIN{RS=\"\\f\"} NR==835' KLN_1966.txt | head -3\necho \"=== KLN leaf 264 (dragoman) head ===\"; awk 'BEGIN{RS=\"\\f\"} NR==264' KLN_1966.txt | head -3"
}
```


### [2026-09-14T01:10:18.370Z] TOOL RESULT

```
=== DOZ leaf for line 1127 ===
46
--- DOZ dragoman entry ---
DOUANE.
Zie Divan.
DRAGOMAN of DBOGMAN.
In het Arab. tardjemdn, tardjomdn en tordjamdn,
tolky van tardjama {éJ^y)> vertolken, dat de Arab.
van de Joden (Chéld. targeem) hebben overgenomen.
Onze vormen hebben wg van de Fr. (dragoman ook
bg de Eng.); de Ital. en Sp. (It. turcimanno, Sp.tru-
jaman (truchimana bg Yangnas, Dicdon. de antigj
del Reyno de Navarra, II, p. 325, document van
1395), Cat. torcimany) zgn minder bedorven; in Tvo-
yage van Mher Joos van Ghistele leest men truceman
of trucheman.
ELIXIB.
Het Arab. el-iksir (j^i)), samengesteld uit het
lidwoord en iksïr, dat in de goudmakerskunst den steen36
=== KLN leaf 798 head ===
  Formed  with adj.  suff.  -ate  fr.  L.  stamen,  gen.  staminis.  See stamen.
staminea),  adj.,  pertaining  to  stamens.  —  Formed with  adj .  suff.  -al  fr.  L.  stamineus,  an  adjective  de¬ rived  fr.  stamen,  gen.  staminis.  See  stamen  and cp.  staminal.
stamineous,  adj.,  pertaining  to  stamens.  —  See prec.  word  and  -eous.
stamini-,  before  a  vowel  stamin-,  combining  form denoting  the  stamen.  —  L.  stamini-,  stamin-,  fr. stamen,  gen.  staminis.  See  stamen, staminiferous,  adj.,  producing  stamens.  —  Com¬ pounded  of  stamini-  and  -ferous. staminodium,  n.,  an  abortive  stamen  (bot.)  — ModL.,  formed  fr.  stamini-  and  ModL.  -odium, a  suff.  denoting  ‘likeness’,  fr.  Gk.  -ci>&7]i;,  ‘like’. See  -ode,  ‘like’.
stammel,  n.,  linsey-woolsey.  —  F.  estamel,  form¬ ed — with  change  of  suffix — fr.  OF.  estamine. See  stamin.
=== KLN leaf 835 head ===
 see  dram  and  cp.  target.  ML. targ(i)a,  OProvenq.  targa  (whence  It.  targa),  Sp. tarja,  ‘shield’,  are  also  Teut.  loan  words.  G. Tartsche,  ‘small  round  shield;  target’,  has  been re-borrowed  fr.  OF.  targa.
targe,  tr.  v.,  to  harass  with  questions  (Scot.)  — Of  uncertain  origin.
target,  n.  —  ME.,  fr.  MF.  targete  (F.  targette),  ‘a small  shield,  target’,  dimin.  of  targe.  See  targe, ‘shield’,  and  -et.
=== KLN leaf 264 (dragoman) head ===
oth.  ( ga)tarhjan ,  ‘to  make  distinct’, OE.  torht,  ‘bright’,  OHG.  zoraht,  ‘clear’,  OIr. derc,  ‘eye’,  W.  drych,  ‘aspect’,  drem,  Bret. dremm  (for  *dpk-sma),  ‘face’.  Cp.  darshana, Dracaena,  Dracontium,  dracunculus,  dragoon, drake,  ‘dragon’,  rancle,  tarragon.
480
Derivatives:  dragon-ess,  n.,  dragonet  (q.v.),  dra- gonnade  (q.v.)
```


## [2026-09-14T01:10:29.037Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor n in 834 835 836; do echo \"--- block $n ---\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N' KLN_1966.txt | grep -oE '^ *1[0-9]{3} *$' ; done\necho \"=== full block 835 numbers ===\"; awk 'BEGIN{RS=\"\\f\"} NR==835' KLN_1966.txt | grep -nE '\\b1[5-7][0-9]{2}\\b' | head"
}
```


### [2026-09-14T01:10:30.158Z] TOOL RESULT

```
--- block 834 ---
1572
--- block 835 ---
--- block 836 ---
1577
=== full block 835 numbers ===
```


## [2026-09-14T01:10:43.215Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BQT v2 leaf 445 (printed 985) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==446' BQT_v2_pages.txt | head -60"
}
```


### [2026-09-14T01:10:44.350Z] TOOL RESULT

```
=== BQT v2 leaf 445 (printed 985) ===
 ‫ره آورد‬                                                                                                     ‫ها‬    ‫سا‬

‫روبین خم است کهکوس و نقارة بزرکه باشد ‪.‬‬                       ‫روبین تن است که لقب اسفندبار ‪-‬‏ وکنابه از‬
 ‫یریونه (‪ » ۴ 32 )۱‬بممنی روبین‌دز‬
                ‫است که نام قلمه‌ای باشد از توران ‪۰‬‬            ‫یزیونه (‪ )۱‬خم ‪ - ۱‬بنتح‌دون‪,‬سنی‬
                                                 ‫بیان بيست ودوم‬

                ‫در رای بی نقطه باها مشتمل بربیست وینج لغت کنات‬

 ‫ره انحام = بروزن سرالجام ‪ ۰‬بمعنی‬                             ‫مخفف‬       ‫بفتح اول و سکون ثالی »‬              ‫و ‪۵‬‬

 ‫زاد رواحله واسباب سفر باشد ازم رکب وغیرهه‬                    ‫طرق کویند ‪ - ۴‬و بمعنی‬                   ‫رکبهی‬
                                                                                                          ‫عست‬
                                                                                                            ‫به ا‬
                                                                                                               ‫را‬
‫ید‌مر کب امسطتلقاچه معنی‬       ‫نبن‬
                                 ‫بعمضیعکو‬
                                        ‫وب‬                    ‫مرتبه و بارهم هت چنانکه گوند ‪«۶‬يك ره »‬
 ‫انجام‌بنهایت زساننده وبآخر آورنده است ومو کب‬                 ‫بعنی بك مرتبه وبك بار‪ -‬ورسم وقاعده وقالوترا‬
 ‫راہ را بنهایت میرساند پس این معنی بهترباشلب‬                   ‫نگیفزته‌اند ‪ -‬ونفمه وآهنگه را هم خواننن ‪-‬‬
               ‫وبمعنی پيك وقاصد هم آمده است ‪.‬‬                  ‫وبمعنی‌هوش وشمورباشد‪ -‬وبضم‌اول» بیکی‌وسیرت‬
‫ره انحام روحانی ک‪-‬نابه از‬                                     ‫زهاد وعباد ویارسابان باشد و رهبان مر کب ازین‬
‫براق است که مر کب سواری‌شب معراج پیغمیر‬                                   ‫است وآنرا روهبان هم میکوبند ‏ ‪#.‬‬
‫صلوات‌اه عليه باشد (‪ - )۲‬ونضی مطمئنه رالیز‬                    ‫کنابه از رختن دزدان‬           ‫=‬   ‫‏‪ oJ‬افتادن‬

                                                               ‫‪-‬‬    ‫بر سر مردم و غارت کردن مال آیشان باشد‬

‫ھآ ودد ‪ ۰ ۷‬بفتح اول یمعنی راء‬                                        ‫و بمعنی زبان نوقصان رسیدن کهفمته‌اند ‪.‬‬
 ‫آورد است که سوغات و هرچیز که کسی ازجایی‬                      ‫رهام ‪ -‬بم اول بروزن غلام » نامیس‬
 ‫بیاید ویرای کسی بیاورد (‪ )۳۴‬اکر همه چندیت‬                    ‫کودرز است که در جنگه دوازده رخ بارماترا‬
 ‫از نظمو شر باشد وآنرا بعربی عراضه گوبند »‬                    ‫شت ‪ -‬وبکر اول درعربی باران قطرة ریزه‬
         ‫و راهآ ور بحذف دال ابجد هم کفته‌اند‪.‬‬

         ‫‪.‬‬     ‫‪:‬د‬
                ‫ار‬‫ب)بچش‬
                      ‫(‪۳‬‬                     ‫(‪ )۲‬جك " چش ‪ :‬صلمم ‪.‬‬                ‫‪.‬‬    ‫ئشی‪:‬نه‬
                                                                                           ‫وچ‬‫(ر‪)۱‬‬
                         ‫‪ ¬ ۴‬رك ‪ :‬روین دز ‪.‬‬                        ‫‏‪ - ٩‬رك ‪ :‬روبین خم ؛ رینه خم ‪۲‬‬
  ‫رحام‬       ‫درشاهنامه‬   ‫‪-‬‬     ‫‪۵‬‬             ‫‪ - ۴‬رك ‪ :‬راهب؛ ورهبان ‪.‬‬                     ‫رك ‪ :‬راه ‪.‬‬      ‫‪۴‬‬
                                                                                                ‫آعده ‪:‬‬   ‫پتشدید دوم‬


                 ‫که با بارمان او لبرد آزمود ‪.‬‬                            ‫به پنجم چو رهام کودرز بود‬
   ‫همیشه‌است‬       ‫اول‪ .‬باران‌ست‬         ‫یک‬     ‫ارهمه‬     ‫‪۹‬‬          ‫‪.‬‬    ‫رك ‪ :‬شاهنامه بخ ج ه ص ‪۷۳۲۱-۸۳‬‬
                         ‫وجمم‌ان رهم بر وزن عنب و رهام بروزن جبال میا بد ‪ * ۴‬شرح قاموس > ‪.‬‬
                                                                                 ‫‪۰‬‬   ‫رك ‪ ۰‬اه وود‬         ‫‪۷‬‬


  ‫چ ر ها ‪ -‬بفتح اول» از ‪ :‬ره (رهیدن) ‪( ۱ +۳‬صفت مشبهه) [رك ‪ :‬رهیدن ‪ .‬رستن ] ؛‬
   ‫آهنگه خدمتش‬           ‫‪« :‬‬       ‫‪,‬گذاشتن‬   ‫» بله کردن‬   ‫رها کردن » اجازه دادن‬      ‫‪-‬‬    ‫شده‬   ‫و خلاص‬       ‫آزاد شده‬


                                   ‫(کی از بزرکان ) کردم » درالم رهانکرد وجفاکرد ‪ ».‬ک«لستان ‪.> ۹۳‬‬
                                                                                               ‫ی‬
```


## [2026-09-14T01:10:52.936Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BQT v2 رازق ===\"; grep -n \"رازق\\|رازك\\|رازگ\\|رازکی\" BQT_v2_pages.txt | head -20\necho \"=== BQT v1 ===\"; grep -n \"رازق\\|رازگ\" BQT_v1_pages.txt | head -10\necho \"=== MON parts ===\"; grep -n \"رازقی\\|رازکی\\|رازگی\" MON_part1.txt MON_part2.txt | head -20\necho \"=== ARY ===\"; grep -n \"رازقی\\|رازگی\" incoming/ARY/ARY_pages.txt | head -10"
}
```


### [2026-09-14T01:10:53.088Z] TOOL RESULT

```
=== BQT v2 رازق ===
=== BQT v1 ===
=== MON parts ===
MON_part2.txt:93303:گلدانی شم سجن عربی : (گیا.) رازقی. 
MON_part2.txt:94446:حساسیت است» زکام علوفه. يونجة رازکی: 
MON_part1.txt:65664:رازقی: ۲22۵ آغ. ف.| (ص‌نست.) منسوت 
MON_part1.txt:65671:رازقیه: (220[2)0: [ع.] (.) جامهة کتانی 
MON_part1.txt:96861:درخت نارنج گیرند. عطر رازقی: (گیا.) 
MON_part1.txt:96862:عطری را گویند که از گل رازقی فش 
=== ARY ===
```


## [2026-09-14T01:10:54.941Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '65655,65685p' MON_part1.txt"
}
```


### [2026-09-14T01:10:55.044Z] TOOL RESULT

```
می‌رسانید. 

رازق: 2 (ع.] (اف) روزی دهنده؛ 


روزی رسان (صفت خدای متعادل). 
رازشی: 122067 [ع. ف.] (حامص.) رازق 
بودن» روزی رسانیدن» رزاقیت 

رازقی: ۲22۵ آغ. ف.| (ص‌نست.) منسوت 
به رازق. (امر.) (گیا.) نوعی انگور دارای 
دانه‌های کو چکك. (گیا.) گیاهی است زمینی 
از خانواده باسمن‌ها جزو تبرة زیتونیان که 
برگ‌هایش کشیده و براق و گل‌هایش سفید 
و پر پر و ضخیم و پر عطر است. گل آن در 
تاستان باز می‌شود و بر دوام است؛ فل. 
رازقیه: (220[2)0: [ع.] (.) جامهة کتانی 
سفید. باده» می» شرات. 

رازک: همع« (.) (گی.) گیاهی است از تيرة 
گرنه‌ها از دستهةٌ شاهدانه‌ها. نباتی است دو 
پایه و بالارونده و پیچنده که برگ‌هایش 
متقابل و مر کب از ۳ تا ۵ قسمت دانه‌دار 
می‌باشد. بوی گل‌هایش معطر و مطبوع و 
شبیه بوی سنبل الطیب و طعم آنها تلخ و با 
احساس سوزش و گرما همراه است» حشيشة 
الد بنار» جنجل؛ همل. 

راز و نیاز: 52رن-ه- (امر.) گفتن مافی 
الض مر (با معشوق)» درد دل. (مت.) 
گوشه‌ای است در همایون.
```


## [2026-09-14T01:11:14.887Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor n in 447 448 449 450 451; do echo \"=== leaf $((n-1)) = printed $((n-1+540)) ===\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N' BQT_v2_pages.txt | head -25; done"
}
```


### [2026-09-14T01:11:16.161Z] TOOL RESULT

```
=== leaf 446 = printed 986 ===
  ‫‪7‬‬                                                                                                          ‫رهاوی‬


 ‫رهثه ‪ °‬۔ بفتح اول و ثالث بر وزن‬                         ‫دهاوی ‪ -‬بروزن سماوی ‪ .‬نام مقامی‬
 ‫رعشه" ارده گروایند وآن کنجد آسباکرده‌است‬                                                        ‫است از موسیقیلا ‪.‬‬
              ‫که باعل وشره ودوشاب خورند ‪.‬‬
                                                         ‫رهبان = م اول و بای ابجد (‪)۱‬‬
 ‫رهشی ‪ - ۱‬بورزن وحشی ‪ ۰‬بمعنی‬                             ‫بالف کشیده بروزن بهتان ‪ ,‬زاهد ویرهیز کارباشد‬
‫است و آن گرم و تر‬   ‫جود‬‫نه ار‬
                           ‫کد ک‬
                              ‫رهشه باش‬                   ‫و وجه تسمیه‌اش محافظت کنند؛‪ :‬نیکی و سیرت‬
                                             ‫ا‬           ‫نيك باشد چه ره بء‌منی نك (‪ )۲‬و بان بمعنی‬
 ‫د باکاف فارسی بر وزن ره‬            ‫گهشای‬
                                        ‫ر‬                ‫محافظت کننده است چنانکه(‪ )۳‬باغدان‌و گله‌بان‬
 ‫نمای» نام روزهفدهم ازماههای ملکی بزدجردی‬                     ‫وبفتح اول خداوند راء ‪. ۴‬‬                 ‫و امثاد آن ‪۴‬‬
                                   ‫باشد ‪.‬‬               ‫رهیر ‪ - ۴‬بروزن شهیر ‪ ۰‬بمعنی دلبل‬
                                                                                                       ‫وبرهان باشد ‪.‬‬
 ‫ره گوی = ‪,‬اکاف‌فارسی‌بروزن مفروی؛‬
 ‫مطرب وخواننده و خذیاگر و تفمه سرای‬                       ‫ره جامه دران = بکسر‌انی‪,‬سوتی‬
                                         ‫است (‪. )4‬‬       ‫است از صنیفات نکیای چنگی ‪ .‬کوبند این‬
‫سر راه‬       ‫دنابه اگزدای‬
                        ‫ره نشن ‪ ۲‬ک‬                       ‫صوت را چنان نواخت که حمار مجلی جامها‬
                                                                   ‫برئن باره باره کردند ومدهوش گردیدند ‪:‬‬
‫بمان‪ -‬ومسافر‪ -‬وقاصدی‬        ‫‌و‬‫ن‌غر‬
                                 ‫ادم‬
=== leaf 447 = printed 987 ===
 ‫ری‬                                                                                  ‫هوت‬
                                                                                       ‫‪-‬‬
‫ه بررزن شهپر » مخفف رهوار‬      ‫ھور‬
                                 ‫ر‬              ‫نام کوهی است در سرأئدب ‪ .‬گوبند آدم صفی‬

               ‫است که اسب خوش راه باشد ‪.‬‬         ‫چون از بپشت بر آمد بکانوه افتاد ‪ -‬و طرز‬
‫رهی ‪ - ۱‬بفتحاول کورثالی وسکون‬                    ‫وروش وقاعده و قانونرا نیز گویند‪ -‬ویی وشان‪-‬‬
‫تحتانی؛ روند ‪ -‬وفلام وبنده وچاکر ‪ ۴‬باشد‬         ‫زته اند ؛ و بمعنی اول‬ ‫سویاهی ادزور را کنف‬
                                                                    ‫بفتح اول هم آقفه امت‪:‬‬
                ‫‪ -‬ویمعنی این کس هم هت‪۴‬‬
‫بر وزن رسیدن» بمعنی‬        ‫ر هیدن ‪۴‬‬              ‫ر هو ار = پروزن رفتار» مر کب رونده‬
             ‫خلاص شدن ونجات بافتن باشد ‪.‬‬                      ‫فراح کام وخوش راه گروابند ‪.‬‬


                                    ‫بیان بیست وسيم‬
      ‫بر هشتاد و بك لغت و کنات‬             ‫در رای بی‌نقطه بابای حطی مشتهل‬


‫هم‌نزاع شدچه هربك میخواستندبنام خود کنند‪.‬‬        ‫دق ‪ ۰‬بفتح اول وسکون انی ا)شهری‬
‫بزرگان آن زمان برای دفع راع شهر را بنام‬          ‫است در عراق ‪ -‬و نام پادشاه زاده أی‌هم بوده‪.‬‬
 ‫پررا‬
    ‫ری واحل شهررا بنام راز کردند وحالا دشنز‬
                                                 ‫کو نف اورا برادری بود «راز» نام داشت‪ .‬هردو‬
‫ند و اهل شهر را رازی ‪ -‬و بزبان‬           ‫‪۳‬‬
                ‫پادشاه راگوبند ‪#. ۱‬‬       ‫فر‬    ‫باتفاق شهری بناکردند‪ .‬در تسمية‌آن ابشانرا با‬
=== leaf 448 = printed 988 ===
 ‫‪۳‬‬                                                                                            ‫ربیای‬

‫نز گویند که از شیر کوسفند یزندبهر نحو که‬       ‫ریباس ‪ - ۲‬بائالی مجهول وبای ابجد‬
                                      ‫باشد ‏‬    ‫رستنیی باشد خودروی و عردم‬            ‫بر وزن گیلای‬

‫یرچال* ‪ -‬بروزن‌فیفال » بمعنی ربچار‬             ‫آمراخورند‪ .‬طعمآن میخوش است وبفایت از که‬
 ‫است که مربای دوشابی ‪ -‬وآنچه از شیر وماست‬                      ‫مشود وآارا ربوای هم میگویند ‪.‬‬
                       ‫گوسفند وغسره مر ند ‪۰‬‬
                                                ‫رليك = بفتح اول و بای ابجد وسکون"‬
‫زرن بیچاره ‪.‬‬   ‫ومب‬
                 ‫ریچاله ‪ - ۱‬با لا‬               ‫تانی ودال بی‌نقطه ‪ .‬نام صحرابی است کهجنکه‬
    ‫بممتی ربیمال است که مربای دوشابی باشد ‪.‬‬     ‫ره رخ که بیازده رخ مشهور است ميان‬
                                                                ‫ایرانی وتورانی در انجا وافع شد ‪.‬‬
 ‫ریحان تاتادی سبکرنون‪ .‬بمعنی‬
     ‫خوش نظر است وآ ارابترکی قلفه گویند ‪.‬‬       ‫ریتانج " ‪ -‬بااول بتانی رسیده وفوفالی‬
 ‫ربحان داود ‪ -‬رستنی باشد که‬                     ‫رباانلف کشیده و لون مفتوح بجیم زده ‪ ۰‬بمعذی‬
                                                         ‫درخت‬      ‫از صم‬     ‫که نوعی‬      ‫ینج ات‬
                                                ‫صنویس‬
 ‫آنرا مرزنگوش خوانند ‪ .‬و بعربی آذان‌القار‬                                                      ‫باشد ‪.‬‬
                                    ‫کم‬
                                                ‫رشه »‬         ‫زربت ‪ -‬بفتح موفانی بر وزن‬
‫رجان ررد کنایه از شماعآفتاب‬
                          ‫ی‬                     ‫است درهندوستان شیه بفادق لیکن‬
                                                                              ‫بار درختی‬

=== leaf 449 = printed 989 ===
  ‫زر‬                                                                                                       ‫‪۷‬‬

‫اول زای‬     ‫مردی هم بوده است؟ ‪ -‬ویجای حرف‬               ‫ر جر = با ثالی مجهول بروزن دمگره‬
               ‫قطه‌دار (‪ )۲‬هم بنظر‌آمده است ‪.‬‬           ‫نوعی از پازهر باشد ومعرب آن فادزهر است ‪.‬‬
‫رید کان ‪ = ۴‬بر وزن کردکان ‪ .‬غلام‬                         ‫رین ‪ - ۲‬بكر اول وثالكث و سکون‬
                                                        ‫حبوانات دنگ رکه اسهال‬        ‫» آدمی و‬            ‫ثالی ونون‬
                  ‫بچگان و پسرکالرا گوبند ‪¥.‬‬
                                                               ‫کاری کند ‪۰‬‬    ‫داشته باشد و آلوده‬          ‫وشکم رو‬

‫رار هیکر اول و سکون ثانی محجهول‬
‫وکام‬      ‫وزای قطه‌دار » جرعه وییمانه ‪ -‬ونعمت ‏‬          ‫= ریاکولوثالت‌بروزن بی‌چیزه‬                 ‫بر‬
                                                                                                      ‫ر‬
 ‫‪ -‬ورحمت باشد ‪ ۱‬و‪-‬خرده‬                ‫اد‬
                                       ‫را و‬
                                          ‫مهو‬
                                            ‫و‬            ‫را‬    ‫کنند و‬   ‫چوبی که کاوآهن را بر آن نص‬


 ‫وریزه را نکیوزیندا ‪ -‬وامر بریختن هم هست‬                        ‫برخیش بندند بجهت زمین شیار کردن ‪.‬‬
                                      ‫بعنی بریز‪. ۷‬‬       ‫ید‪ ۲‬یک راول وفتح‌دال ابجد(‪)۱‬‬      ‫ر‬
 ‫ریژ ص بکر اول وسکون انی و زای‬                           ‫مروزن زیبراه‪ .‬یران امرد بی‌رش وغلامان ترك‬
‫پشته پشته باشد ‪ - ۸‬وکامو مراد‬               ‫»ن‬
                                             ‫می‬‫زرسی‬
                                                  ‫فا‬    ‫و ام‬    ‫مقبول باشد ‪ ۴‬؛ ویفتح اول نبز کفته اند‬

=== leaf 450 = printed 990 ===
    ‫اس‬                                                                                                  ‫رىژك‬
             ‫ماضی ریدن و لجاست کردن باشد ‪.‬‬                          ‫وآرزو و هوا وهوس را بیز گفته‌اند ‪٩‬‏ ‪.‬‬
‫= بروزن زستن» فرورفتن بچاه‬              ‫ی‬‫ل‬                   ‫ریژ ك ‪ -‬بکر اول وفتح زای فارسی‬
 ‫باحوض وامثال أن باشد‪-‬ویمعنی موبیدن ونوحه‬                    ‫وکناه کردن و از جای‬         ‫»ن‬
                                                                                          ‫یكا‬
                                                                                            ‫سيش‬
                                                                                              ‫عن ش‬
                                                                                                 ‫بر وز‬
‫سفتن و کربه‬
          ‫یخف‬
            ‫کردن همهت ‪٩‬ک‏‪-‬روم‬                                                    ‫فرو لغزبدن باشد ‪.‬‬
‫وجاست کردارا نیز‬
               ‫کردن بود ‪ - ۷‬وریدن ت‬                          ‫ريز هةسیهیی ک=نابه از ستارگان‬
                                        ‫کوند ‪. ۸‬‬                                                        ‫باشفد ‪.‬‬

 ‫= با اول بثانی مجهول رسیده‬             ‫سی‬
                                         ‫ر‬                   ‫دیزی راز = بعنی رحمتی بکن ‪۰‬‬
                                                                   ‫هم مده است ‪۰ ۳‬‬          ‫چه رىز بمعدی رحمت‬

                                             ‫است ‪.‬‬         ‫ریس = بکر اول وسکون‌ثانی وسین‬
 ‫ر پسیدن ‪٩‬‏ س بروزن لسیدن » رشتن‬
                                                         ‫بی‌نقطه » غضب وقهر وخشم راگویند ‪ -‬وباثالی‬
    ‫پنبه و تافتن پشم وابرشم وامثال آن باشد ‪.‬‬
                                                         ‫مجهول ‪ .‬شوربای غلیظی کهبربالای شله پولاد‬
 ‫است‬       ‫رشو»ف‬
```


## [2026-09-14T01:11:38.950Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BQT v2 ازق/ازک ===\"; grep -n \"ازقی\\|ازکی\\|ازگی\" BQT_v2_pages.txt | head -20\necho \"=== ARB jawaliqi رازق ===\"; grep -n \"رازق\" ARB_mo3rb.txt ARB_abdulraheem.txt 2>/dev/null | head -10\necho \"=== AFM Addi Shir ===\"; grep -n \"رازق\\|رازك\" AFM.txt AFM_pages.txt 2>/dev/null | head -10\necho \"=== TAD ===\"; grep -n \"رازق\" TAD.txt TAD_pages.txt 2>/dev/null | head -10\necho \"=== PLA Asbaghi ===\"; grep -n -i \"razeq\\|rāziqī\\|raziqi\\|rāzeqī\" incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt | head -10\necho \"=== RCH Richardson ===\"; grep -n -i \"razaki\\|razeki\\|razakl\" RCH.txt | head"
}
```


### [2026-09-14T01:11:39.146Z] TOOL RESULT

```
=== BQT v2 ازق/ازک ===
2026:‫ساحران ‪ -‬و کنایه ازکی است که رنج کش‬                           ‫و‬
11832:  ‫«‪۲۲‬خر‪:‬یش بعنی پوستش از اندام بناخن بازگیر‪.‎‬‬
16358:                                                                ‫وبخشیدن کناهی است که بهو ازکی صادرشده‬
17673: ‫خوردن ازکی ‪ -‬ودرعین شادی غم‌پیش آمدن‌را‬                                                             ‫می زسد ‪.‬‬
20419: ‫و لوقع داشتن باشد ‪ -‬کونابه ازکینه ورزیدن‪-‬‬
22768: ‫نازگیب‪:‬اری‬
25030:                  ‫وبممنی خرامیدن بناز وکتبفختر‬                           ‫رند دهل ديرده ‪-‬کنابه ازکی‬
35771:                    ‫ستیازقی ‪٩‬‏ ‪.‬‬
37883:   ‫شکل تشکیل میدهدوروی دانهارا پوستة نازکی فرمز رن" بامواداسیدی‬
=== ARB jawaliqi رازق ===
ARB_mo3rb.txt:5803:أنه قد تحذف الياء فى المع قيقال « البرازق» وهو الذى اقتصرعليه فى اجمهرة : 06م) وظهر 
ARB_mo3rb.txt:36792:م عمس شرح القاموص لاز يي دى ٠‏ أبو الفيض 2م سد بن شد بن عياد الرازق ال يداارتضى 2 ١١‏ 
=== AFM Addi Shir ===
AFM.txt:2974:(الرازق ) السب املاحي 390 6 ( والخمر: 
AFM.txt:2975:ܝܚܪ من رازى وهو لتو 0( ܒ ( راجع ܫܝܐ 1 >( ٠ورازقي‏ 
AFM.txt:7341:رازق 7 
AFM_pages.txt:1836:(الرازق ) السب املاحي 390 6 ( والخمر:
AFM_pages.txt:1837:ܝܚܪ من رازى وهو لتو 0( ܒ ( راجع ܫܝܐ 1 >( ٠ورازقي‏
AFM_pages.txt:4698:رازق 7
=== TAD ===
=== PLA Asbaghi ===
=== RCH Richardson ===
```


## [2026-09-14T01:11:45.040Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '1830,1845p' AFM_pages.txt\necho \"=== leaf ===\"; awk 'NR<=1836' AFM_pages.txt | tr -cd '\\f' | wc -c\necho \"=== page tag nearby ===\"; awk 'NR<=1836' AFM_pages.txt | grep -o '\\[pdf page [0-9]*\\]' | tail -3\necho \"=== index line 4698 ===\"; sed -n '4694,4702p' AFM_pages.txt"
}
```


### [2026-09-14T01:11:46.234Z] TOOL RESULT

```
0( 1 ون الئاس والسظن ܘܟ )ܚܐ ܟܙ 256
عد «الرؤغة) الوحل ود( اروغة) الماء والطين والوحل الشديد معر بان عن
رده وهو الملين ܠܝܟ به التبن لنسبيع ܐܠܐ ܚܐ ووه ٠وقالوا‏ فيهها 2 ܠ
وأرذغت وارتدغ الرجللالط 77 ܓ
¥ (الرِزق) تعر يبب روزي وما يمعنى واصل. روزى نسبة الى روز وهو النهار.
وقالت فيه العرب رزق وارتزق الى غير ذلك
(الرازق ) السب املاحي 390 6 ( والخمر:
ܝܚܪ من رازى وهو لتو 0( ܒ ( راجع ܫܝܐ 1 >( ٠ورازقي‏
بالفارسيّة يطاق ايضاً على العنب الملاحي ܕܟ وقال في البرهان القاطع :« زتموا ان
ܣܨ ܝ سم احده 09 00 الاننو راز 930 هذه المدئة (اى ܘܙ 4 الري ٠)»‏ ولا
مت اراد كل” منها 0 ܓ ܨ بأسمه 3 من جراء ذلك 2 ܚܠ ܙܠ ܝ ٠فاشّار‏
اليهها احد |( ْ ܣܨ 11 ܐܝ ܐܢ )| ܙܠ ܧ 3 ܐ الاخر. ند
ܣܣ 93 ثما رازيين >
( الروزنة ) تعريب روزنه وهي الكوة ٠‏ والكوة نفسها ارامسة ܟܘܬܐ ( راجع
ܢܬܐ ص 1١:‏ )
+ رن ) فير بجر ضَلت تعد 22 4 ܐܢܟ معرب ارزن وهو ܡܨ
=== leaf ===
73
=== page tag nearby ===
=== index line 4698 ===
رابو ٠ه‏
راتياج ١7‏
راد ܀ ܙ
راز ܘ
رازق 7
رازى باب
رازيانه 7٠‏
راست عب
راسن "اب
```


## [2026-09-14T01:12:01.448Z] TOOL CALL #15: Bash

```json
{
 "command": "pdftoppm -f 414 -l 414 -r 300 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg414 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg414.png"
}
```


### [2026-09-14T01:12:03.780Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 74486 Sep 13 21:12 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg414.png
```


## [2026-09-14T01:12:06.470Z] TOOL CALL #16: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg414.png"
}
```


### [2026-09-14T01:12:07.328Z] TOOL RESULT

```

```


## [2026-09-14T01:12:07.322Z] INPUT

[Image: original 2550x3300, displayed at 1546x2000. Multiply coordinates by 1.65 to map to original image.]


## [2026-09-14T01:12:39.235Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg414.png')\nprint(im.size)\nim.crop((520,1080,1000,1260)).resize((1440,540)).save('pg414-greek.png')\n\""
}
```


### [2026-09-14T01:12:40.702Z] TOOL RESULT

```
(2550, 3300)
```


## [2026-09-14T01:12:42.889Z] TOOL CALL #18: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg414-greek.png"
}
```


### [2026-09-14T01:12:42.911Z] TOOL RESULT

```

```


## [2026-09-14T01:13:10.674Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KNT Raga ===\"; grep -n -i \"Ragā\\|Raga-\\|Ragâ\\|Rhagae\" KNT.txt | head -20\necho \"=== BRT raγa ===\"; grep -n \"raγa\\|raγā\\|Raγa\\|Ragha\\|Ragā\" BRT.txt | head -20\necho \"=== PHD Ray ===\"; grep -n -i \"^ray\\|Rag(\\|Ray,\\| Ray \" PHD.txt PHD_mackenzie.txt | head -20\necho \"=== HUB/HRN ===\"; grep -n -i \"Rages\\|Rhagae\\|Rag[āa]\\b\\|Raj\\b\" HUB.txt HRN.txt | head -20"
}
```


### [2026-09-14T01:13:10.818Z] TOOL RESULT

```
=== KNT Raga ===
585:By the Avestan and Skt. cognates: afar, Skt. атат; garma- in Garmapadahya, Skt. gharmá-; дата-, Av. sarad-; darga-, Av. daraga-, Skt. dirghd-; baršnā, Av. instr. barasna; martiya, Skt. mártya- .
1776:І. Attached to a verbal root, the ablaut grade of the root varying: kara- in compounds, u-céra-, küma-, Катёа-, gausa-, raga-, adv. daríam, drauga-, baga-, bara- and bāra- in compounds, zana- in compounds; less certain formations in d-baha- in daha-vaja, casa-, U-t&na-, u-tava-, gara- in batu-gara-, Vi-vdna-, varga- in hauma-varga-.
3887:which must be reinterpreted to Auramazdaha : ragam : vartaiyaiy (gen-dat. of goal, §250.1; and see Lex. s.vv, raga-, vart-). * iya]maiy RI; apijmaty WB, ap]imaiy KT; ut]imaiy Bthl. AiW 83, Gray AJP 30.457; ulàmaiy (all characters visible) Cameron. “ 081... КІ. ; (ada|yátiy WB; éa[dutiy, with traces of the third character still visible, KT; a”dafyätaiy HK 1.28; бойду} Bthl. AiW 1559; байшуй legible, Cameron: The second charac- ter was d? rather than КТ? a, Jn.; and KT's traces of the third character fit y* as well as they do d”. Elsewhere (except in DNa 58) forms of this verb are all middle, and as the subjunctive always has primary endings in OP (8222), the restoration is 6adayá[taiy], the necessary space being the same as for KT’s restoration.
5531:darga- adj. ‘long’: GAv. daraga-, LAv. daroya-, NPers. dër, Skt. dirghd-, pIE *dlgho-, ef. Ck. dodexés, Lt. longus (881, $68, $101, $148.11, VI). dargam asn. as adv. ‘for a long time’ DB 4.56, 15.
5851:Raga- sb. ‘Rhages’, a district in Media: Elam. rak-qa-an, АКК. ra-ga-’, Gk. ‘Payys, now Rai near Teheran. kagä nsf. DB 2.71f. Ваду absf. DB 8.2.
=== BRT raγa ===
=== PHD Ray ===
PHD.txt:122:/abāz dādan б: 1. attribute, ascribe to; 2. appoint to. br ... add M fr! va-čār add helpless. delete á-distag ... (read ayidtag) add ‚тах |°р1°с | N farāz] acclivity. Afson ... add M ?pswn. Vagar ..., add useless. vāgēš [kw | (M "^ wa, P ?gwc), N aqóš] embrace, armful. add vājištag | gyštk' | P * gyšt, N ayišta] mixed, defiled. add \Ahliswang |*hlygwng] = Ard. delete Khriswang ... for alum ... read „alum |? № | N <] millet. Vāsnūd(ag) ... delete noble. aswür [|PR/LSYA < A pršy';.. āšnāg ... add acquainted with. āštīh ... add concord. ayad ... read |" byd^t' |... for bahr... and bahrag ... read bahr(ag) |b hl(k') | M bhr, N ~(a)] part, portion, share, lot; reason. (az) an bahrag ray : on that account, therefore. for  bahrwar ... read bahr(ag)war [b'hl(k)wl | N bahrawar| partaking, parti- cipator, partner. ~th : participation, advantage. balay add M by. add balgam |[blgm | N balyam] phlegm. baxtan ... add divide. bayaspān [by?sp^n' | = M]... bélür ... for M read P bylwr.
PHD.txt:321:ë ру | (M hyb)] particle giving the present tense optative sense. é, v, éd, éw. ēbāraģ [*dyp'lk', ^dwlk! | N éwàr] evening. ébgat(ih) ['ybgt!, -yh = Av. aifi.gati-] (onslaught of) Evil; the Adver- sary. ēbsrūsrim [>ур-, ?ybslwslym = Av. atBisrūdrima-) the gah from sunset to midnight. ébyünghan [>ур-, ?ywby?nghn!, etc. = Av. aiBydshana-] sacred girdle, = kustig. ёё Pye | (P ?ушус), N héc] (with a negative) not any. ēčand, v. éw-Cand. éd (HN A < A hr? | M? yd] this; v. dāštan. ~ ray ёё [cf. N z-é-rá] because, since. édar [LTME < À I-tnh | M?ydr, N ~] here. édin [ytwn'! | N ēdūn] thus, so. ~ih: (correct) manner. ëg [ADYN' < А *dyn | М ?yg] then, thereupon. ëk Pywk' | M yk, N yak] one. ëkanag [Pywk’nk! | N yagana) submissive, obedient. ^h : submission, obedience. ēk-dād [ywkd’t'] sole-created. ēmēd [*dmyt'] hope. ēn [ZNE < A znh | M *yn, N in] this. -ën [-yz! | = M, N -in] suffix forming adjectives of material or quality. -endag [-ndk! | M -yndg, N -anda] suffix forming present participles. -én-idan [-yn-ytn' | M -yn-ydn, (N -àn-)] suffixes forming causative and transitive denominative verbs. *énókén Pynw(k)kyn' = Av. *aēnē.kaēnā-) heiress (under the obligation of continuing her father's line). enya рулу | (M ?n’y)] otherwise, moreover. lër [d] | M Zur, v. azér] down, below; low; under. — ud abar: upside down. tēr Pyl] noble; hero, ~ih: nobility, good conduct. Eran [y”x! | N ~] Eran, (land of) the Aryans. ~ag [-k'] an Eranian, Aryan. érang [”y/ng] blame, condemnation; error, heresy. ~ih: = érang. éranj-, v.  * éraxtan. Ērān|-šahr (yPnitr! | N ~] land of the Aryans. —-wëz [-wyc] (original) home of the Aryans. 1ёгахќап, ёгапј- Pylhtn!, ?уЇпс- | J ?yrxt] blame, condemn, damn.
PHD.txt:555:rabih [/pyh | M rbyh] noon, midday (heat). rad [/t! | N —] (spiritual) chief, master. АҺ: office of rad. rad [Pu | P rd, N ~] generous, liberal. ~ih: generosity, liberality. radag [itk! | M rdg, N rada] line, rank, row. radómand [/t?^wmnd] having a rad. rad-passag [/tps’k'] ceremonies of the gáhanbar festivals. radunay [/twny = Av. ratunaya-] one under the guidance of a rad. raftan, raw- [SGY TWN-tn! < А V sg’; lwb- | M rptn, rw-, N ~] go, move, proceed. ~išn, v. rawišn. raftār [/pt?] | N ~] goer. rag А! | M rg, N ~] vein. «ЛЬ: disposition, character. ray [/gy | P rg] quick, swift. ray [Pg | N —] meadow, plain. rah [/s, lh, [hy | M rh(y)] chariot, wagon. rah-, у. rastan. rah [Ps | M rh, N ~] road, way. rahag [/hk! | P rhg] = rag. rāh-dār [lsd] | N ~] brigand, highway robber. ~ih: brigandage. rahig [/syk!, Ikyk' | M rhyg, N rahi] child, page. ~ih: childhood. rāh-nimāy [Psnm?d | (M r’-hnmwd’r), № ~numa] guide. ram [Pm | М әт, N ~] peace; cal. 21st day. ram(ag) [/m(k') | P rm, N ram(a)] herd, flock. ráménidan, rāmēn- [Pmyn-ytn! | M ?myn-] give peace, pleasure. rāmišn [P min! | M rmyfn, N rāmi$] peace, ease, pleasure. ~ig [-vk! | N —z#] peaceful, at ease. ran [Рп! | N ~] thigh. P rān- [/^n-] fight. randidan, rand- [/nd-ytn! | N —] scratch, grate, abrade. rang [/ng | M rng, N —] colour, dye. ranj [Inc | P rnj, (M rnz), N ~] toil, trouble. ~ag [-k' | N —a] troubled. ranjénidan, ranjén- [/ncyn-ytn'] trouble.
PHD.txt:557:ranjwar [Incwl | (M rnzwr), N ranjūr] troubled, distressed. rapihwin [/pys-, Ipyt-pyn!, -wyn' = Av. rapiüfina-] the afternoon gah; south. ~tar [-tl] southern. rasan [/sn' | N ~] rope. rasénidan, rasén- [/syn-yin'] bring. rasidan, ras- [YHMTWN-tn' < А yhmtwn, V mt^; ls-ytn! | M rs-ydn, N ~] arrive, mature. raspig [Pspyk!] second officiating priest. rast [Pst! | M rst, N ~] true, straight, direct. ~ih: truth, rastaģ [lstk! | N rasta] series, row, progression; element, газап, rah- [Istn', Ї(?)А- | N ~] escape. rastarih [/st?/y%] escape. rasüg [/swk! | (N rāsū)] weasel. Rašn [/@! | M ri, N ~] god of Justice; cal. 18th day. ra&tan, *raz- [/ftn'] colour, dye. raw-, v. raftan. rawag [/wP^k! | N rawá] current. ~ih: currency. rawügenidan, rawagén- [/zob)hyn-ytn!] set in motion, propagate. rawénidan, rawén- [SGYTWNyn-ytn', v. raftan] cause to go, extend. rawišn [lwbin', SGYTWNsn', v. raftan | N rawif] going, motion. ^h : behaviour; as a suffix, forms abstract nouns. ray [Pd | M ry, N ra] postposition, for, for the sake of. rāyēnāģ [Pdym bi | M r’yn’g] arranger. rayénidan, rāyēn- [Pdyn-ytn! | M r'yn-ydn] lead, direct, arrange, organize. ~išn: action, function; arrangement. rāyēnīdārīh [/”*dynyt?lyh | M r!ynyd?ryh] direction, organization, rāyišn [”dsn'] order, arrangement. rāyomand [Pd^wmnd] rich, majestic. raz [/c, lz | N ~] vine; vineyard. raz [Pc | M Pz, N ~] secret, mystery. ~ig [-yk'] secret. rāz-kirrēģ [Pc kylwk' | M г qrwg] architect, builder. razm [/cm | M rzm, N —] battle. —--$àh [-g's | P -g’h, (M rzm?h), N ~] battlefield. razor [lcw] | M rzwr] forest. rédak [lytk' | N ~] lad, page. тёр [/yā! | N ~] sand. rëm [lym | M rym, N —] dirt, filth, purulence. réman [lymn' | M rymn, N ~] dirty, filthy, purulent. ^b : filth. 1r€§ []yf | N ~] wound, sore. *rēš [/yf | N —] beard.
PHD.txt:655:wistardan, wistar- [wstl-tn! | N gustardan] spread. wistāx [wst??hw! | M wyst?h, N gustāx, bistāx] confident, bold. ~ih: confidence, boldness. wis [w(y)$ | M wyš, N gus] poison, venom, bile. wišād [SLYTWNt', Р! | M wid, N gušād] open, wide, loose. wišādan, *wišāy- [SLYTWN-tn! < A У šrh; wPtn! | M шурап, (wys?h-), N gušādan, gušāy-) open, loose, free. wišād-dar [.SL Y TWNt! BBA] hospitable. wišād-dwārišnīh [zP??! dzb?lšnyh) going about ‘open’, i.e. without kustīg, or šabīg. | wišān- [w®n- | = P] shake down. *wišāy-, v. wišādan. wiškar [zo£hl | N bisgar(d)] hunting-ground, wilderness. wiškīdan, wiškin(n)- [wfkytn!, wškn-] divide, separate. ~išn: separation. wiskofag [wskwpk' | N biškēfa] blossom. wiškuftan, wiSk6f- [vvškup-tn! | J guškuftn, gwškwß-] blossom; hatch. wišūb-, —išn(-īģ), v. wišuftan. wišoūmand [w%wmnd] poisonous, venomous. wišūdag [wiwtk' | (M ghwdg)] abortion, daevic creature. wišūdan [wswtn'] bear daevic offspring. wišuftan, wišūb- (zfwp-tn! | M wiwb-, N *gusuftan] disturb, destroy. ~isn: destruction. ~1&п16 : destructible. *wixSay- [whsd-} forgive, forbear. ~iSn(ih): forbearance. ~išnīg : forbearing. lwiyaban [20(у) р?п! | Р шуп, N bīābān] desert. *wiyābān [wyd’p’n'] astray, wandering; deluded. ~ih: delusion, deception. wiyaban|garih [wyd"Pnklyh] deception. ~ig [-vk'] wandering, itinerant. wiyāftan, *wiyüb- [wd ptn! | M wy’b-] open (the mouth). wiyan [wyd?n! | M wy’n, N giyān] tent. wiyiz- [wydwe-] loosen, undo. *wiyufs- [wdwps-] make merry. ~išn: merry-making. ~iìšnīg : merry. wizandag [wzndk'] quaking. wizandidan, wizand- [wznd-ytn'] tremble, quake. -išn: quaking. wizar [wc] | M wer] separation; explanation. wizārdan, wizār- [wel-tn' | M wyc'rd, wyc^r-, J bz?rd-, N guzardan] separate; explain, interpret; perform, fulfil, redeem. ~išn: decision; redemption.
PHD.txt:663:xwāb [hw’b | N ~] sleep. xwābar [hw’l | M xwbr] beneficent. ~ig [-yk!] beneficial. —ih: beneficence, benefit. xwad [BNPSE < A b-nps-h; hwt' | M xwd, N ~] self; indeed. САҢ: selfhood, essence. xwaday [лору | M xwd'y, N ~] lord. ~th: lordship, sovereignty. ~war [-w’/] lordly. xwad-dósag [hwtdwsk'] self-indulgent. 7h : self-indulgence. xwah [AH TE < A *hth | N ~] sister. 1, ?x wüh-, ~išn, v. xwastan, xwāstan. xwahar [AH TEL v. xwah ; hw'hl | (M xwr), N xwdhar] sister. xwahl [eo hl | (M xwhr), № ~] bent, crooked. xwā(h)rīh [hw (h)yh | M xw'ryy] happiness, bliss. xwālist [hw’lyst' | (M xw’ryst)] sweetest. xwamn [hwmn', hmn' | M xwmn] sleep, dream. ~-wizar [-wc'/] interpreter of dreams, oneirocritic. xwān [hw!n! | M xw’n, N ~] tray, table. xwandan, xwān- [KRY TWN-, KLY TWN-tn! < А У д | M xwnd, xw'n-, N xwāndan) call, summon. Xwanirah [hwnyls = Av. x"aniraüa-] the central, inhabited continent of the earth. !xwar [kwl | M xwr, N ~] sun; cal. 11th day. Zwar [kwl = Av. x"ara-] a degree of sin. xwar-, —išn, v. xwardan. lxwàr [kw] | M xwr, N ~] light, easy; mean, abject. ~ih: ease; v. also x wührih. *xwar [%w/ | M xwr] food. xwür-, —išn, v. xwārīdan. xwaran [%w/n! | M xwrn] banquet. xwarāsān [hwlsn! | M xwr'?n, N ~] sunrise, east. xwār-bār [how?1b?l | M xwr w Pr, N ~] food and drink. xwardan, xwar- [OS TEN-tn! < Ath, V fth; hwltn! | M xwrdn, xwr-, N ~] eat, consume. ~išn: food. ~ignig : edible. ~išnīh: eating, consumption. xwardār [hwit?I] (legally) edible, not murdār. xwardig [hwityk' | M xwrdyg, N ~i] food. xwārēn [hw’lyn'] edible. xwārēn- [hw’lyn-] cause to eat, drink; feed; irrigate. xwarģ [wig | J xwwrg] ember. xwārīdan, xwār- [heo?1-ytnt] drink. —išn: drink, drinking.
PHD.txt:1996:for (cj.) &; (pr.) ray, P wasnad.
PHD.txt:2844:more fray, freh, wēš.
PHD.txt:3307:quick ray, téz, züd.
PHD.txt:3327:ray tëx.
PHD.txt:3663:since (cj.) čē, éd ray &, ka; (pr.) az... ӧгӧп.
PHD.txt:3917:swift arwand, ray, šēbāg, tagīg, tüzig, zibal.
PHD.txt:4952:ray, rah, (225) rah
PHD.txt:4969:rah, (23%) ray, тау rāyūmand rāh
PHD_mackenzie.txt:2189:  -- ray ~e [ef. N z-e-ra] because, since.
PHD_mackenzie.txt:4313:ray [lgy I P rg] quick, swift.
PHD_mackenzie.txt:4314:ray [pg IN ......] meadow, plain.
PHD_mackenzie.txt:4366:ray Wd I M r'y, N ra] postposition, for, for the sake of.
PHD_mackenzie.txt:4367:rayenag [l'dyn'k l I M r'yn'g] arranger.
PHD_mackenzie.txt:4368:rayenidan, rayen- Wdyn-ytn l I M r'yn-ydn] lead, direct, arrange,
=== HUB/HRN ===
HUB.txt:3223:vraj fest.
HUB.txt:5276:27, 111. Entspreohend Prga- (fur Paraga- Spiegel p. 228) = arab.
HUB.txt:5453:phi. vacak; bad *schlecht' = paz. raJ Shk. 269, Min. 61. 202,
HUB.txt:5568:vraj 'schreiten, gehn ; birinj = gurinj (Muwaffaq p. 6,
HUB.txt:6160:einherschreiten' aus *viraz — skr. vraj zu stammen.
HUB.txt:8904:Die Form Rai (fiir ap. raga-) ist im Syr. sclion im
HUB.txt:9298:TuUen, Fohlen', arab. kurraj, arm. Surak 'Fiillen' (Leb* der
HRN.txt:610:Vergl. aw. radni- in frara&nidrajö^); phlv. eratn (?);
HRN.txt:4899:aw. drajah' 'Länge'; phlv. draj (vd. 5 (159) Gl.),
HRN.txt:5595:kurJ. ruz; aty. vraj ; bei. röc, n. ros 'Tag, Tages-
HRN.txt:7107:ap. ^frajäma- {{^gani- 'gehen*); \)\\\v, frajäm bezw.
HRN.txt:7108:farjam 'Ende', frajämtnltany vergl. fraj(a)ftan (AV.,
HRN.txt:9781:113. Statt ferjaftm (Zeile 7) lies phlv. fraj(a)ftan.
HRN.txt:10437:82. frajäftan Vollenden* (AV., in späten Kolophonen).
HRN.txt:10458:mutung in den unorganischen phlv. frajäftati, jüd.-
HRN.txt:16751:rajög^ 619.
HRN.txt:17456:rajöstiin 227.
HRN.txt:18072:raj-K«. 68.
HRN.txt:19883:mayoArw.raJ 995.
```


## [2026-09-14T01:13:25.403Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HUB context ===\"; sed -n '8895,8915p' HUB.txt\necho \"=== BRT Raga ===\"; grep -n \"Raga\\|Ragā\\|Rayā\\|Ra&a\\|ragā\" BRT.txt | head -20\necho \"=== KNT leaf/page for 5851 ===\"; awk 'NR<=5851' KNT.txt | tr -cd '\\f' | wc -c"
}
```


### [2026-09-14T01:13:26.605Z] TOOL RESULT

```
=== HUB context ===
11 (naoh Noldeke), Vis o Ramin 131, 10 v. u. (nach v. Stackel-
berg) Von Merv gebiirdg' = marvazl bei Barbier de Meynard,
Diction, p. 525, Anm. 4, 8yr. J^^TI'ID (?) Noldeke, syr. Chron. 33.
•) Salemann, Shams i Fachri p. 101, 11 = *Goldlaok'.— 249 —
Auch -yr ist zu /yr geworden in i%v 'PfeiF = zd. iiyri- ;
phi. np. an^ran der dreissigste Tag des Monats = zd. ana-
yranqm (gen. pi.) Bdh. 61. 76. Dazu dSr lange aus *dayr
=■ *dayr = ap. darga-, zd. dareya^"^ Aber ap. rg (== ry)
ist sonst = np. ry.
Die Form Rai (fiir ap. raga-) ist im Syr. sclion im
Jahr 430 bezeugt, ZDMG. 48, 413.
§ 142. Fiir ap. g erscheint h in:
Bahistun {Y9Lq\x{), gr. to Bayiavavov iigog (Diodor II,
13, 1) in Medien, urspr. = *bayastana' 65tterort\ Das
Wort ist also medisch. Ueber nuhuftan siehe oben p. 103.
8 143. Geschwunden ist y = y in den Konsonanten-
verbindungen :
a) gm = ym (nach Vokalen): amadan *kommen*, phi.
matan, ptc. mat Gl. and Ind. 210, gd.
dgemat, zd. fraymat, ap. ha(n)gmat(l,
paragmata; scheinbar auch in np. Hama-
=== BRT Raga ===
=== KNT leaf/page for 5851 ===
230
```


## [2026-09-14T01:13:36.818Z] TOOL CALL #21: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-14T01:13:36.829Z] TOOL RESULT

```


```


## [2026-09-14T01:13:39.940Z] TOOL CALL #22: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/dragoman",
 "prompt": "Give the full etymology section for the English noun dragoman, including all intermediate forms (Middle Greek, Latin, Old French, Arabic, Aramaic, Akkadian) and any notes about the Akkadian targumannu origin."
}
```


## [2026-09-14T01:13:42.176Z] TOOL CALL #23: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AA%D8%B1%D8%AC%D9%85",
 "prompt": "Give the Arabic entry ترجم: etymology of the verb tarjama and the noun ترجمة tarjama(h), ترجمان turjumān; is it a borrowing from Aramaic/Akkadian? Also any Persian section."
}
```


### [2026-09-14T01:13:45.288Z] TOOL RESULT

```
# Etymology of English "Dragoman"

The word "dragoman" traces back through multiple linguistic layers:

**Origin Chain:**
From Middle English *dragman*, derived from Old French *drugeman*, which came from Medieval Latin *dragumannus*. This Latin form drew from Byzantine Greek *δραγομάνος* (dragomános).

**Semitic Roots:**
The Greek term ultimately derives from Arabic *تُرْجُمَان* (turjumān), which borrowed from Classical Syriac *ܬܰܪܓܡܳܢܳܐ* (targmānā). These Semitic languages traced the word to its deepest root in Akkadian *𒅴𒁄* (targumannum), meaning "interpreter."

**Additional Note:**
The English plural underwent reinterpretation as suffixed with *-man*, creating the form "dragomans" alongside the traditional "dragomen." The term is noted as a doublet of "truchman," sharing the same etymological lineage through the Semitic language family.
```


### [2026-09-14T01:13:47.930Z] TOOL RESULT

```
# Etymology of Arabic ترجم (tarjama)

Based on the Wiktionary entry, the verb **tarjama** (to translate) has a complex etymological history:

## Origin Theory

The entry indicates it's "Possibly from Classical Syriac ܬܰܪܓܶܡ, or possibly a back-formation from تَرْجُمَان (tarjumān)."

## Etymological Chain

The word traces back through multiple ancient languages:

1. **Akkadian** - The root originates in Akkadian *targumannum*
2. **Classical Syriac** - The term *targmānā* (interpreter) developed in Syriac, derived from the Akkadian root
3. **Arabic** - The word entered Arabic, potentially as a back-formation from the noun *tarjumān* (interpreter/translator)

## Related Forms

- **ترجمة** (tarjama) - verbal noun meaning "translation"
- **ترجمان** (tarjumān) - noun meaning "interpreter"

The entry confirms this represents "a borrowing" pattern across ancient Near Eastern languages, with Akkadian and Syriac as the primary source languages. No Persian section appears in this Wiktionary entry.
```


## [2026-09-14T01:13:52.894Z] TOOL CALL #24: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/targumannu",
 "prompt": "Akkadian targumannu / targumannum: what does Wiktionary say about its etymology — derived from ragāmu 'to shout/call', or a loan from Hittite/Anatolian? Quote the etymology."
}
```


## [2026-09-14T01:13:53.928Z] TOOL CALL #25: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/dragoman",
 "prompt": "Full Etymonline entry for dragoman, plus anything on Targum and Akkadian ragamu."
}
```


### [2026-09-14T01:13:54.126Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-14T01:13:58.842Z] TOOL RESULT

```
# Dragoman Etymology

Based on the Etymonline entry, **dragoman** means "an interpreter, a guide for travelers" and dates to around 1300.

## Etymology Chain

The word traveled through multiple languages before reaching English:

- **Arabic origin**: The root is Arabic *targuman* meaning "interpreter," derived from *targama* ("interpret")
- **Greek intermediary**: Late Greek *dragoumanos* adopted the Arabic term
- **Medieval Latin**: This became *dragumanus* in Medieval Latin
- **Old French**: Appears as *drugemen* in Old French
- **English**: Entered English circa 1300 as *drugeman*

## Linguistic Treatment

In English, the word was "treated as a compound from *man* (n.), with plural *-men*," making dragoman/dragomen the standard singular/plural forms.

The entry notes this represents a fascinating example of how trade and cultural contact—particularly between European and Middle Eastern civilizations—influenced vocabulary development across multiple language families.
```


## [2026-09-14T01:14:02.987Z] TOOL CALL #26: WebSearch

```json
{
 "query": "Akkadian targumannu etymology Hittite tarkummai ragāmu interpreter loanword"
}
```


### [2026-09-14T01:14:10.912Z] TOOL RESULT

```
Web search results for query: "Akkadian targumannu etymology Hittite tarkummai ragāmu interpreter loanword"

Links: [{"title":"(PDF) 2010 (with I. Yakubovich). Semitic Word for Iron as Anatolian Loanword","url":"https://www.researchgate.net/publication/251232139_2010_with_I_Yakubovich_Semitic_Word_for_Iron_as_Anatolian_Loanword"},{"title":"MARZENA CHROBAK FOR A TIN INGOT: THE ARCHAEOLOGY OF ORAL INTERPRETATION","url":"https://ejournals.eu/pliki_artykulu_czasopisma/pelny_tekst/3fa9b150-9972-4048-b12b-4c10d2b59235/pobierz"},{"title":"The Dawn of Translation in Ancient Mesopotamia","url":"https://www.linkedin.com/pulse/dawn-translation-ancient-mesopotamia-pieter-uys?trk=public_profile_article_view"},{"title":"Dragoman - Wikipedia","url":"https://en.wikipedia.org/wiki/Drogoman"},{"title":"Appendix:Arabic roots/ت ر ج م - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Appendix:Arabic_roots/%D8%AA_%D8%B1_%D8%AC_%D9%85"},{"title":"On Anatolian Loanwords in Akkadian Texts From Kültepe | PDF | Hittites | Anatolia","url":"https://www.scribd.com/document/74619724/On-Anatolian-Loanwords-in-Akkadian-Texts-from-Kultepe"},{"title":"(PDF) The Etymology of Some Language- and Translation-Related Terms in Arabic","url":"https://www.academia.edu/64234983/The_Etymology_of_Some_Language_and_Translation_Related_Terms_in_Arabic"},{"title":"targumannum - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/targumannum"},{"title":"Taru (god)","url":"https://en.wikipedia.org/wiki/Taru_(god)"}]

Based on the search results, here's what I found regarding the etymology of these terms:

## Akkadian targumannu and its Origins

The term targumannu, a word of unclear origin first recorded in Old Assyrian, is possibly derived from the Hittite tarkummai: "to announce, interpret, translate".

However, there are alternative theories about the origin of targumannu. Akkadian targumannum ("interpreter") was possibly borrowed or alternatively derived natively from ragāmum ("to shout, to exclaim, to cast forth a prophecy; hence also, to speak for the gods, to speak for another, to interpret").

## Semitic and Anatolian Connections

Correspondences have been noted between the Arabic-Semitic root (t-r-g-m) and the Hittite and Luwian verb tarkummāi/tarkummiya meaning "to announce" and "to explain". The Luvian origin of targumannu- 'interpreter' is commonly accepted.

## Linguistic Descendants

From the Akkadian term targumannu comes the Hebrew meturgeman; the Arabic tarjuman; trujaman, truchement, turcimanno in Romance languages; the Greek dragoumanos; dragoman in English and many other European languages.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-14T01:14:18.538Z] TOOL CALL #27: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/targumannum",
 "prompt": "Quote the Akkadian entry targumannum: etymology (Hittite tarkummai? ragāmu?), meaning, and descendants list."
}
```


## [2026-09-14T01:14:20.262Z] TOOL CALL #28: WebFetch

```json
{
 "url": "https://en.wikipedia.org/wiki/Dragoman",
 "prompt": "Quote the Etymology section verbatim as far as possible: Akkadian targumannu, Hittite tarkummai, Aramaic targemana, Arabic tarjuman, Greek dragoumanos, Latin dragumanus, Old French drugeman."
}
```


### [2026-09-14T01:14:23.883Z] TOOL RESULT

```
# Akkadian Entry: targumannum

**Etymology:**
The entry states the origin is "Unknown. It could be either a borrowing from another unattested language or a derivation from the verb _ragāmum_, 'to exclaim, shout to'." There is no mention of Hittite *tarkummai* in this article.

**Meaning:**
The word functions as a masculine noun meaning "interpreter" or "dragoman" (a professional translator/interpreter), attested from Old Akkadian onward.

**Descendants:**
The term spawned an extensive family of descendant words across multiple language families:
- Syriac *targmānā*
- Arabic *turjumān* (leading to Maltese, Greek, and Medieval Latin variants)
- Persian *tarjumān* (reaching Hindi and Urdu)
- Spanish forms like *dragomán* and *truchimán*
- Turkish *tercüman*
- Armenian *tʻargman*
- And numerous European language borrowings (French, German, Italian, Polish, Russian, etc.)
```


### [2026-09-14T01:14:26.268Z] TOOL RESULT

```
# Etymology of "Dragoman"

Based on the Wikipedia article's Etymology section, here are the key linguistic origins:

**Ancient languages:**
- "Akkadian as 'targumannu,'" 
- Ge'ez (Classical Ethiopic) as "ትርጓም"
- "Aramaic as _targemana_"
- "Arabic the word is ترجمان (_tarjumān_)"

**Medieval European transmission:**
The term entered European languages through a chain of linguistic borrowing: "Medieval Greek δραγομάνος, _dragoumanos_" became "Medieval Latin as _dragumannus_," which then evolved into "Old French _drugeman_" and "Middle English as _dragman_."

**Later European variants:**
The article notes "German _trutzelmann_, the French _trucheman_ or _truchement_" and "Italian _turcimanno_," along with various Spanish forms.

**Linguistic roots:**
The word derives from "the Semitic quadriliteral root _t-r-g-m_," with speculation about possible "Hittite origin" alongside documented appearances in ancient Near Eastern languages.

The modern English plural is "dragomans" rather than the Greek-style "dragomen."
```


## [2026-09-14T01:14:45.539Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON ترجمه ===\"; grep -n \"ترجمه\\|ترجمان\\|مترجم\" MON_part1.txt | head -10\necho \"=== PLA رازق ===\"; grep -n \"رازق\\|razeqi\\|Räziqi\\|raziqi\" incoming/PLA/PLA_pages.txt 2>/dev/null | head -10\necho \"=== PLA tarjama ===\"; grep -n -i \"tarǧama\\|tarjama\\|turǧumān\" incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt | head -5\necho \"=== RCH tarjuman ===\"; grep -n -i \"tarjuman\\|turjuman\\|tarjamah\" RCH.txt | head -5\necho \"=== FSD dragoman ===\"; grep -n -i \"dragoman\" FSD_vol1.txt FSD_vol2.txt | head -5\necho \"=== WEB dragoman/targum ===\"; grep -n -i \"dragoman\\|targum,\" WEB_vol1.txt | head -5"
}
```


### [2026-09-14T01:14:45.716Z] TOOL RESULT

```
=== MON ترجمه ===
300:ترجمه و طبع رسید). 
308:۳ - مجموعهٌ اشعار علامه دهخدا با مقدمةٌ مشروح در ترجمهة احوال و آثار 
322:دانشگاه تهران ۱۳۳۵ (اين مجلد از طرف آکادمی لنینگراد ترجمه شد). 
328:ج - ترجمه‌ها : 
336:۲ کتیبه‌های پهلوی. (ترجمه از انگلیسی) به قلم و.ب. هنینگ وونه«ه812 ۷ 
341:ترجمه و نشر کتب. تهران ۲ ۱۳۳. 
8256:تاریخ و ترجمهً احوال. منسوب به فرقة 
32947:غایب گشتن؛ استخفاء (ترجمان القرآن ۸). 
39403:کتابی که در آن ترجمهً احوال شاعران و 
39467:تراجم: وله [ع. ۰[ (مص م ( 3 ترجمه. 
=== PLA رازق ===
=== PLA tarjama ===
=== RCH tarjuman ===
23293:A   tarjamah  or  tarjumahy  Interpretation,  translation.
=== FSD dragoman ===
FSD_vol2.txt:60082:Till  an  opoan  inlerpases  its  miKhty  barrier,  no  citadel  of  free-  translates  Oiallv;  espceially,  on dom  or  truth  has  faecn  long  maintained.  Evm.ETT  Orations  and  the  communications  of  persona Spe«A«s,  liec.  2-.  fS22  P- «.  U.  s.  CO.  1836.1  guage.s;  a   dragoman,  3t.  [I-]  ,
FSD_vol2.txt:60093:10.1836.1  guage.s:  a   dragoman,  sf.  [H  A   messen^of  the  go<ls:  ,/°8atWe  manner;  by^^
=== WEB dragoman/targum ===
58842:drag’6-man, 7.; pl. drag’o-mains, drag’ō- men, (Fr. dragoman; Late Gr. dragoumanos; Ar. fargumdn, an interpreter, from largama, to interpret, explain.] in the Near East, an in- terpreter or traveler's guide or agent.
59473:on head and a nearly straight face. ing notes, in music, syncopated notes. riv/ing rein, a rein attached to the bit rings and held by the driver of the vehicle. | | driv/ing shaft, the shaft upon which a driving wheel rests. : driv/ing spring, a spring resting upon the box of a driving axle of a locomotive, which bears -the weight and aids in deadening shocks. driving wheel (hwēl), 1. in machinery, a wheel that communicates motion to another wheel or wheels, 2 2. one of the large wheels in a locomotive 3 engine fixed upon the crank axle or main- i shaft; called also driver. driz/zle, v.i.; drizzled, pł., pp.: drizzling, ppr. {AS. dreosan, to fall.] to rain in fine, mistlike drops. driz’zle, v.t. to shed in small drops or particles. driz’/zle, n. rain falling in fine, mistlike drops. driz/zly, a. drizzling; characterized by a drizzle. drof/land, dryf’land, ». driftland. [Obs.] dré/gér, n. same as drogher. = drd’ghér (-gér), ». [prob. native name.] 1. a small West Indian coasting craft, built for carrying goods, having long, light masts and lateen sails. _ 2. any slow-moving coasting vessel. drog’min, drog’6-min, n. dragoman. [Obs.] drdgue (drög), n. a buoy attached to the end of a harpoon line. droil, v.t. to work sluggishly or slowly; to plod.
```


## [2026-09-14T01:14:52.057Z] TOOL CALL #30: WebFetch

```json
{
 "url": "https://www.ahdictionary.com/word/search.html?q=dragoman",
 "prompt": "Give the AHD entry for dragoman including the full bracketed etymology and any Semitic root reference."
}
```


## [2026-09-14T01:14:54.456Z] TOOL CALL #31: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%B1%D8%A7%D8%B2%D9%82%DB%8C/",
 "prompt": "What do Dehkhoda and Mo'in say about رازقی? Quote the definitions and any statement about its origin (منسوب به رازق، ری، انگور)."
}
```


### [2026-09-14T01:14:56.018Z] TOOL RESULT

```
# Dragoman Entry from American Heritage Dictionary

**Definition:** "An interpreter or guide in countries where Arabic, Turkish, or Persian is spoken."

**Etymology:** The bracketed etymology traces the word from Middle English _dragman_ through Old French _drugeman_, Medieval Latin _dragumannus_, and Medieval Greek _dragoumanos_, ultimately deriving from Arabic _tarjumān_. The chain continues back through Aramaic _targəmānā_ and Akkadian _targumannu_, meaning "interpreter."

**Semitic Root Reference:** The entry directs readers to the "Appendix of Semitic roots" for additional information about the word's origins, indicating the Arabic and Aramaic components are documented in that appendix.
```


### [2026-09-14T01:14:58.899Z] TOOL RESULT

```
# Dehkhoda and Mo'in on رازقی

**Dehkhoda's Definition:**
According to Dehkhoda's lexicon, رازقی refers to "a white flower, small, fragrant, from which perfume is extracted" and also "a type of grape with small seeds."

**Mo'in's Definition:**
Mo'in's dictionary states: "the name of a white, small, full, fragrant flower from which perfume is obtained" and "a type of grape with fine seeds."

**Origin Statement:**
The text notes that رازقی is "منسوب به رازق" (attributed/related to Razaq), though the specific meaning of this etymological connection is not explicitly detailed in the provided excerpts. Both lexicographers describe the word as referring to botanical specimens—particularly the jasmine flower and a grape variety—without further elaborating on its linguistic origins beyond this attribution.
```


## [2026-09-14T01:15:08.139Z] TOOL CALL #32: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B1%DB%8C",
 "prompt": "Persian ری (Rey): give the etymology — Middle Persian, Old Persian Ragā, Avestan Raγā, Greek Rhagai/Rhages — and any cognates."
}
```


## [2026-09-14T01:15:10.290Z] TOOL CALL #33: WebFetch

```json
{
 "url": "https://en.wikipedia.org/wiki/Rhages",
 "prompt": "What Greek and Latin names are attested for the city of Ray/Rhagae? Quote forms: Ῥάγαι, Ῥάγα, Ῥάγης, Rhagae, Rhagiana, Europos, Arsacia, and the Old Persian/Avestan names."
}
```


### [2026-09-14T01:15:13.231Z] TOOL RESULT

```
# Etymology of Persian ری (Rey)

## Origins and Development

According to the Wiktionary entry, ری descends from **"Middle Persian [Inscriptional Pahlavi needed] (ldy /⁠Ray⁠/), from Old Persian 𐎼𐎥𐎠 (Ragā)"** which originated as a Median district.

## Cognates

The word shares linguistic connections across ancient languages:

- **Akkadian**: 𒊏𒂵𒀪 (ra-ga-')
- **Elamite**: 𒊩𒋡𒀭 (rák-ka4-an) in locative form
- **Ancient Greek**: Ῥάγαι (Rhágai)
- **Latin**: Rhagae, Rhaganae

These represent Iranian borrowings into surrounding language families, reflecting the historical significance of the Ray region in the ancient Near East. The consistency across multiple ancient sources indicates this was an established geographical and administrative designation in antiquity.
```


### [2026-09-14T01:15:15.305Z] TOOL RESULT

```
# Ancient Names of Ray/Rhagae

Based on the Wikipedia article, the attested Greek and Latin names for Ray include:

**Greek forms:** "Rhágai (Ῥάγαι) and Rháges (Ῥάγες)"

**Latin forms:** "Rhagae and Rhaganae"

The article also notes the city "was once renamed Europos (Ευρωπός) under the Seleucid Empire" and that "Following the Parthian conquest of Ray, the city was renamed Arsacia."

**Old Persian:** The text indicates the name derives from "Old Persian Ragā (𐎼𐎥𐎠)," and the city is mentioned in the Avesta (Zoroastrian scriptures), though specific Avestan forms are not detailed in this passage.

The document confirms these names were used across classical antiquity and the Parthian period to identify this ancient Iranian city.
```


## [2026-09-14T01:15:26.964Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"raga-\\|rag[aā]\\b\\|Ragha\\|raγ\\|ra9a\\|rays\\|Rai'\\|Rai,\" BRT.txt | head -20\necho \"--- try zantu ---\"; grep -n \"rizantu\\|zantu\" BRT.txt | head -10\necho \"--- AHM ---\"; grep -n -i \"Raga\\|Rhagae\\|Ray\\b\" AHM.txt | head -10\necho \"--- IRN Farahvashi ---\"; grep -n \"ری\\b\" incoming/IRN/IRN_pages.txt | head -5"
}
```


### [2026-09-14T01:15:27.076Z] TOOL RESULT

```
4567:•  j.,  g,  antarl,  p.a'^ar  i)  Adv.(?)  Innen, innerhalb;  dazwischen':  "ämyS yiin  °r>  vTta (sd.)  °r^''  ärJyff  maya  /rakäraysH  \ .  <). 11;  —  '"%rigämi    °ri   anantar)   a%a    °r?
4828:mit  frS^''^  i)  'hervorgehen,  -Ireten': aiiihe  haxayB  fräyente  astva(.»r>take  Yt. ■'5-9SJ  — yü'ia  .,  hvanxsaet^m  tarasca harqtn..fraca  iii/i  aiwica  vazaite  ava^a  . . Yt  /0.118.  2)  'vorwärts,  weiter  gehen': fräyantö  tarö  pilüm  ..yim  cinvats  Vyt. 42.  a)  &oiysX  mA  ß-a^a: /rain /raysiii^ irUtim  uzbaröti  äpö  V.6.2T,  — /ra/a  fra- yaniu  n  maoö  (sA)  Y. /O.  14,  ig;  19;  — /rasa  /raya  (aSIA.)!'  vahisDm  a  ahüm binjayanti  (sd.)  ie  ..  V,  7.52;  —  vgl.  Inf. Jrayäi.  3)  'einhergehen'  iyio? paiti  mit Akk.):  yat  ÖS  paiii  ml  asava  frayaf^  .  . aismssastö  .  .  V.J.  i ;  —  äat  liama  yh paiti  frayat^^  tä paiii, .Yi.  lOjiJ).  4)  'be- gehen', mit  Akk.,  a)  einen  Weg:  kaf  tä pa>ä  (sd.)  Jrayqn^  pasvqm  vil  staorqm va  narqm  vä  Y.S.iy,  ii^23,  3.  15;  — likrava  paoirlm  aHa  pa%ä/rayanlu{s\.3Xl Sing.)  V.  Ä19.  b)  eine  Tat:  (aili  tä ^ao^aa  varsta  , .  fralta^''^  apati(a{&i.) anuzvars/a  . .  V.i^.i.
5904:•  j.  asnvant-  m.  Name  eines  Bergs  oder Gebiigs":  ahmat  haca garays  fraoxsyqn.. 'väsca  Yt.  //).  5;  —  "vanlitn  gairJm  masda- <iSt)m  S.2.9;  —  'vaniahe'^  garSts  mazda- oätahe  Ny.5.5.
6349:garBis  uHJarinahe  .  ,  °rahe  Y.  /.14,  22. 26;  "Tt  J(j.o'';  —  vJsph  garays  'räfouru.- ^ä^rS  V.2.14;  7J.10,  V.ig.28.
6996:(sd)  a  manafiAs  \.4S-9-  T)  des  Be- treffs 'von  wegen':  tat  "kwa  p)r3sa  .  . mmanAs  a  ydha  n^m}  (sd.)  xlmavats  Y. 44.1,  S)  ahmst  *a  adv.-artige  Verb,, sbes.  b)  '(bis)  hin  zu  — ,  usque  ad  —'; a)  fäxioi&f^:  frasa  fraysit..a  zangaafyas- äj  äp3  a  inuiyasal  V.  6.27;  27*;  —  ajvT? a  ir/sas  (sd)  pa'kS  Y.J^-S-  a)  s  mit
7883:1)  'hin  zu  gehen  zu -',  mit  Dat. ■>  (statt  ,_(,aj«,j,-  Vr.;5.2;  V.jff.i^s'  (wo  "0,7),  2;. Akk.):  husiti  ..  äanyuMti  (sd.)  ite  vJse  (,^  Yti-agS;  —  aim  mSt  'äS  iw/y  (sd.) afrXnümi  yahmat  haca  . .  ".  .  in  (dessen) ' yj  „5  a?i-ö  . .  Y.  2(J.8;  —  iv//tt  -ö«  . .  hvar- Haus  zu  gehen,  von  dem  .  .'■  ^.6S.^lt)m  lyaoi:ni>m  S-s^i^i; —ya>a  yat '<.a 14.  a)'einzugehenauf-':iJOTff^^ä^W/|ana/rj'rf  daiühus  hakat  m^a  us./raraysil moi  data  danga/tya  *yaoi  ySm  vä  *nagas  (sd.)  YL  75.68;  V. 5.56,  y.55;  —  ime  nö däfMt  its  vairya  stdt/isd.)  "..ihn  sollt  ihr|.  .  aspa  para  *miira  *'c,a'>  iiaymU  (sd.) mir  gewähren,  auf  den  einzugehen  keiner  yt.io.  42;  60;  —ha  hl  asti  ä>a  ..aipi.- euch  zwingen  kann,  (den  Wunsch) .."  Y.  panmnäi  'oa  aSaone  V.Ä107;  —  ktj'M 43-^'h-  'ffff(sd.)''oa  alsum  agate  Y.ig.^i;  —  'oa
8214:u.  «dära-  n.  'Bauch';  *%rq!a-  m.  'I-nuf,  Tgl. gr.  tpitu  (woiu  Bgm.  Grdr.' /.  690)'). —  Pü.; undeutlich;  ttV:  fa  askam  davarel.—  >) Lesung nicht  sicher;  L4,  K  I  haben  '^nisfanifm.  — ')  Vgl.  ai.  araga-  m.  —  ')  Zur  Nasalirung  »gl. %rq/>ia-.
9449:ii:jr-<j  frakavB  .  .  ml  'vis  (NS.)  mä  -braune  Teufel'.  —  .)  Zs.  15.  1  macbt  das Z'izbärii  V.2. 29.  a)  als  Dal!'a  perso-'  Wort  lum  EN.  —  3)  Vgl.  zu  kaxuii-. nifizirt:  -i-U  d„ni  p^llitl  äati'ü  .  .  V. ! .  ,  kax'arajainya-  Adj.  (fem.  -w-)  'üir J5.43.  2)  Adj.,  von  dem  damit  be- 1 ^toe  der  &A«oo  (sd.)  gehörig':  jM hafteten:  ml  m  alujä  mo^rays /rania- 1^,„„„„„-  .  y^^,  .5^,-,„  yt.  1. 9,  12,  i6'. r>ntlt   *t»3  *'vW^   (NS.)   Yt5.  92.  Ableit.  aus  kaiFartla..
10129:'aipJ.za^>m  .  .  °avSi  vjnzyalqm  (sd.)  tqm tis  ifan'käi  ßityS  (sd.)  \.4S.S;  —  iim OsBtffis'isd.)  oAurS  m<ptr»m  talal  .  .  'avSi xsvld^mcä  *Avö.uruia^6yB  Y,  29.  7;  — narqm  aiwi.xssi^ne  .  .  'avqm  gävayatum V.  2.  2  S ;  —  x^arfhfmca  naire  alaone västnmca  'ave  hwiaiiAe^^;  V.5. 20;  20, Vr.  2. 1 1 ;  —  asii  .  .  süra  °7ulca  västra- Ae^a  YtJ5.S4;  ij.ioo'; — yahmya garays
10517:mit  J  Kaus.  'aufButen  lassen':  ks  zrays äyiärayeiti  Yt. A3:
10731:Monatstag:  'Gräfte  vairyehe  aySxlustahe . . S.  1. 4;  vgl.  2. 4,  Y.  i6. 3.  aa)  als  Be- zeichnung des  unter  Xs.%  Obhut  stehenden Metalls,  mit  vairya-  Adj.:  kariasät  fra- käraysil  liyra  '^ra  *vairya  V.g.io;  — °ir3i  vairyli  pairiAarim  pairi^araysil V.ij.ß;  —  ayao/ia&um  vä  srum  vä mfyma(sd.)  '^ra  vairyaV,  16,6;  —  *Aqm.- ivqmca  .  .  (sd.)  *upairispata  aka  bastqm ''kr?m  vainm  Yt/0.135.
11373:—  daryyaäi"'>  bäzava  Yt  70,104;  — pourucil  ü^aAe  N.  6^;  —  *vanaite  akimat man3  Yt.  ig.  g6;  —  aspaat  ysi  mi%rö.- drujqm  .  .  Yl  10.  20;  Aog.  4^;  —  karsas- Ht  frakaraysis  Y.g.  10;  zit  *Y.y,  — autark  *kä%rwtHi  N.  /09;  —  tarS  p>rp- tümcit  Y.ig.6;  —  Aandarpzaat  /landar?- zaym  V.(?.  49;  —  urvähqmät  zbayant avi  . .  Yl  12.  3;  —  ianvasAf  :^ahya  uita- n?m  Y.  jj.  14;  verwendet  Y.  1/.18,  /j.4;
12859:ant/ra  —  ?  — :  fraäarii'ta',s,A.)(it  täiri- tiam  fradaraysit  N.  Ö7,
12880:—  ')  S  411-  3  d. •  p.  darga-,  g.  daraga-,  j.  dar«}-a-  Adj. (fem.  °7J-)  'lang';  i)  räumlich:  Ufa  tarn car^am  yqm  'yqm  YtJp.  77;  5.50;  — mi^rtm  . .  yeAha  'yäat  bäeava  .  .  Yt.  10. 104.  z)  zeitlich:  M<?i«(sd.)  tat  äs  nsit 'y?m  Yt.5. 65;  —  "iimal  aipi  zrvätum Y.62.3,\tig.a6;  13.53;  —  °f^^  ^yo (sd.)  t^mattks  Y.31. 20;  —  'yayäsca  paiti danyjjltdis  YL  /y.  1 3  j ;  Y.68.11;  —  tsm (nämL  kämtm)  msi  data  'gahys  *yaos{^^^ vairyS  stSis  Y.  43.  13;  —  hyatcä  -gSm *Jr3gvö.d»dyS  rasö  {sd.)  Y.jo.ii; — ptn- fum/a  (sd.)  barjsma  starane  °y?mca  yasram ..yaaJnS'Vt.iO.iiSi—ya^a  Sicä  *aiivi- iayama  'ya  amiiayana  . .  hr^yrnya^^aSum (sd.)  Yt  70.  7  7 ;  —  °gäi  Tsyai  bfzvait!  hax- maim  (sd.)  Y.  40.  3;  —  'yai  hax^räi  Vt 10.  T),  17.6;  — fravaiayS . .  hulhaxmanS . .  'yaa'fyj  Aax^oralifyff  Vt  13.  30;  —  'y^m Aaxma  V.  60.  j;  —  dättm  tS tanuye  :^ar»nB ' urvnaläi  •y?m  havanfum  (sd.)  Yt77.  22; F.^b;  —  urunaica  'ye  havanhe  A.  i.ii; —  'yäi  AaosravaAAsi  .  .  -yai  AavafiAäi Vjtjs;  —  a  'yät  ^ä.bairyilt  (sd.)  Y. öo.  6;  —  'yqfi  upayanayä  (Stverz.)  Y, /.  13  usw.;  —  'ya  (APn.)  data  .  .  sara- >uäraAe  T.  ^6  {?);  —  iaia  tl  'yim  ävSya (sd.)  aakal  H.2. 34;  16.  a)  Adj.  an Stelle  unsres  Adv.'':  :^afsa  'yd  tna^äka "schlaf  lang,  o  Mensch"  V.  rÄ  16;  — earäiti  .  .  yä  'ya  apu%ra  aHti  V.  3.  34; 34.  b)  ASn.  als  Adv.:  H  utä,  'gam  jlvä
13561:•  j.  d3r9zLra9a-  Adj.  'der  einen  festen, staiken  Wagen  hat":  taxm^m  ttaotär?m  .  . '■:iwi  YtJ7.i2.
13962:•  j.  dvadasa-  Adj.  'der  zwölfte':  aAmat  j  mit  us  Kaus.  'hinauf,  in  die  Höhe  fliegen Aaca  garays  fraoxfyan  .  .  'sff  wrift'^aa}  machen':  päurvö  (sd.)  .  .  yat  dim  usca YtJO.2;  /.8,  V./4.9;—  's^m  asan/iamta  \"^'^>;'^"i  ■■  ^raitaonö  narrfahe  hArpa -  ~  ■■         -  •  YL5. 61.
14401:V._J.42; — fra  raruyö ..'^warstaAe  xraAtaA  hineingeraten,  einbrechen  in  — ' ayu  (sd.)  mh^qm  .  .  upa  "hwarstahe  (Akk.):  yat  .  .  yuxtanqm  asam  fratfiram jaymyqm{Si).^^¥,o.)\t.8.ii; — ^wars'täi  "kan/ayati  . .  nava  ^frähwfr^suma  raturTm «rswYt  5.129.  a)  mit  Gen.  (statt  Dat.)  (sd.)  ¥15.50;  *ig.J7- des  wem?:  a/ramannt^m  (Sp.  loi  o.)  mit  ni  'etwas  (AJck.)  durch  Graben aital^qm  ratufri!  ratufrltim  *%w3nsaiii  mit  einem  schneidenden  Instruroent  her- N.5^^;  52  (wo  *%Wfnsäfti)*^.  stellen,    ausstechen':     %rays   anya    maya
14500:•  j.  ftray-  Zw.,  fem.  tisr-  'drei',  Plur.: nSit  atvd  nSii  dva  nsit  %rayB  (Nm,)  nSit\ fräyanhs  T.44',  —  aivahe  pasvS  .  .  dvä ..  iryam'^  .  .  caturqm  N.  65;  —  aSva lirUva  ,.  dva  %riiha  . ,  %ribyS  %risvaiiöyö V.  2.  ii£;  —  aevahe  ..  *as)maeyahe  .. dvayä  .  .  %rayqm  ,  ,  caiiWärS  V.  iS.ii; F./,  P.2^,  V.  1$.  49,  iS.  17';  —  %rays zavainti  gäusca  aspasca  haomOscaY.ll.i; 20,3,  21.  i,  Az.  5J,  Vyt_5;  —  aitbyö  ratu- byS yöi  hinti  %rayasca'^  %risqsca  "..33.." Y. /.  10;  —  "ibräyd  (als  Am.)  anya  maya nihw?r»sBii  V.p.  9;  ti^,  5. 10,  Vd.  12;  — är(/(Ain.)  mätahs  ußa.baolayan  .  .  xAias mänhs  V.  7.  i4f.i  N.  66,  67,  '88.  57^;  — ^ris  mayam^^  ava.kanaym  V.  Ä37,  16. 12;  j.  51;  —  %rJ  (An.)  *malima.safnqn asamäj  P. g;  — -  %rlvä  azsiti  (sd)  sraois.-
14810:•  j.  'paesa-  i)  Adj.  'aussätzig':  ma  mg aiiayä  zao'hrays  /ranhar?ntu  *mä  *°sa'^ yS  vUiritsJanus". .  ein  Aussätziger,  dessen Person  isolirt  ist"  Yt.5.  92.  2)  ra. 'Aus- satz': ma  ähra  .  ,  'sS  yS  vJt3r7tS.tanu! mäZa.Bm  anyqm  daxstanqm  .  ,  aarahe mainySus  "nicht  .  .  AussaU,  womit  die Isolirung  der  (betroffenen)  Person  ver- bunden ist,  . ."  V,  2.  29.
14840:mit  ara  i)  'herabfallen':  s.  Inf.  2)  in rftfßdscher  Art  Tiinab-,  hinzugehen  zu  — ' {avi  mit  Akk.):  äat  ava.paiat  Jraarase  . , avi  xrays  veurukahm  Yt  ig.  58,
--- try zantu ---
12727:. .  santunamca  dahyunamca   .  .  zantusänS '/ans  (als"  AP.)  YL/j.'isi. Komp.:  dairiAa!'-'i-*'A/iii-.
13119:und  GP.  mit  äaitihupalay-  (Stverz.,  unter I  a,  2  a):  nmünahe  vä  nmänS.paitiS  vTsS vä  vispaitii' tantJus  vä  zantufaitii  "itihSui vä  dair^hupaitisYtiO.18;  usw.;  —  nmäna- iiam  nmänS.paitis . . 'Äyunam  datAhupatti} Yt/0. 18.
13122:j.  'dahyu'ma-,  "dähymna-'*  Adj.  'der I  Provinz,  dem  Land  an-,  zugehörig,  Land-': kaya  ratavS?  nmänyS  vlsyU  zantumS  'mB zardhuärö ptixlöY-ig-iB.  A)  m.Name der  Gottheit  der  Länder*':  "mtm/a  aia- vamm  asahe  ratam  G.3. 7 ;  —  'mähe  ra%wS 0.3.7;  —  uzayeirin^m  .  ,  frädaLvirtm 'trmnca  asavanim  Y.  2,  5;  —  laayeirinai .  .  ß-ädat.vTrai  'mäica  asaone  Y,  /.  5 ;  — ähurBiS  °mahe  Vr.  1. 9.
13124:•  j.  Mahyuma-,  'dähyuma-''  Adj.  (fem. 'mä-)  'zur  Gottheit  Dähyuma  gehörig,  mit ihr  in  Bedehimg  stehend':  mi^ra  .  . nmänya    ratvB  vlsya  zantuma   'ma  sara-
17821:yemi  , ,  imat  am>ia  spptita  .  .  imat  asäu- nqm  varguAls  °iays  (VP.)  Wjra  aiiuihüra Y.  65. 1 2 ;  Ny.  /.  I ;  —  aora  varmkis  upa.- sa^a  .  .  äps  .  .  urvarä  .  .  tüäunqm  fra- vasays  Yt  13. 147;  1. 9,  10. 100,  H.  34,  y, 79,  FrW. /.  3;  —  jamyqn  i^ra  asäunqm .  ,  'iaylf  asöis  basfaza  hacimnä  . .  istSe *vadhar»Aqm  paitiHätSe  ätaranqm  Y.  60. 4;  —  qpqmea  .  .  urvaranqmca  .  ,  asao- nqmla  'hnqm  yasnsm  Vr. 21.  \;  —  yS nä  his  hubinta  *barat  jva  a?aonqtn *says  (als  AP.)  sästa  .  .  hö  anhaiti  za- sulttmS  Yt  /J.  1 8 ;  —  fravasayS  .  .  yä a/raourvisvat  k?r»navainti  irsm  yahmya jaanti  Yt.  y.  26;  —  -says  . .  ya  ahurahe xsayats  dasinqm  upa  yü&yänti  yezi  aim bavaiti  ^alavaxsnuiW.  13. 63  ;  — frasüSTnii uyrä  asäunqm  'fayS  paoirij'  pouru^sata .  .  pouruAatanra  .  .  pouruiasvanS  apitii ashntnä  haväi  käcil  näfäi  . .  tä  yü^yeinti pfianähu  have  asahi  Yt  l^.  65if.;  —  "sayS .  .ya  avai  trayS  aiwyaxsayänti  yat  vouru- kahm  ..yä  ave  strjui  atwyäxsayeinti yqm ^haptöiringS  ..ya  avqm  k^hrpim  aiwyäxsa- yänti  yqm  .  .  hnsäspahe  .  .  ya  avqm *x^rqm  (sd)  aiwyäxSayänti  yqm . .  tara- 'huStrahe  navaca  navaitlsla  navaca  sota nava^a  hatattra  navasSs^a  baevqn  Yt  13. 59—62;  —  "iayS  .  .  yä  vts^&a  ävayänli hamaspa>:maedaim  paiti  ratüm  äat  a^ra vtcar?nii  dasa  pairi  xsa/nö  Yt/J.  49;  — asSunqmcä  'HbyS  yä  nS  iltä  urvSibys  Y. 5Ö.  2 ;  —  asäunqm  '/is  narqmcä  näiri- nqmcä  yazamaidl  Y.^7. 3;  —  °fayS  yä paeirya  (sd.)  anhan  Y.  23.  \;  —  äyeseyesti "vTspaya  asavane  'se"  Y,  2_j.  3;  —  vTspä °iayS  (als  AP.)  asäunqm  yazamaide  ädah- *yunqmca ..  'say5 ..*u%dahyunqmla . .  °iayS.. narqmca  ..'^ayD  ..näirinqmfa  ..  °sayS  yaza- maide  Vr.l6.  2;  7.  i,  10.2,  16.  i;  —  nabä- nazdiäanqm  para.iristanqm  aliirapaitinqm a!>iryanqm  narqm..näirinqm  'iayff  yaza- maide  Y.  26.  T,  8  ff.";  —  a/äunam  "sayd .  .  nmänyä  visya  zantumä  däAyumä  zara- ^ustrSJpmä  Y.  ly.  18;  —  airyanqm'  .  . /ßityanqm'  .  .  sairimanqm'  .  .  säininqm' . .  dahfnqm' . .  vTspanqm'  dakyunqm  narqm .  .  näirinqm  .  .  °sayö"  yasamaide  Yt  13. 143—145;  —  fä  'sayU  .  .  aoßstA  hittti  .  . ya  paoiryanqm  tkaihnam  ya  vä  narqm azätanqm  /rais.car>^rqM  saoiyantqm  Yt. y.i7;'Y./.i8',  23.2,  24.5;  —'  vjipä .  .  'Iay3  .  .  yä    haca   gayät    mariihnai   ä
19314:—  paiHp?r3nt  annm  mainyüm  hala  "na . .  Visa  . .  zatäu  . .  *daAku  V.  JO.  s  j  — paoiryqn  ihalü , .  'nanamüt  vTsqmia  zantu- nqmca  dahyunqmla  Ytfj,  150;  10.18,  Y. äV,  2j.  I.  a)j.  GS.  oderGP.  mit«Ma«Ä- patay-  (sd.""',  Stverz.)  und  nmanS.pa%ni- (sd.'"',  Stverz.) :  'nahe  nmanS.paitfm . .  'nahe nmanspahnlm  VT.3. a  £;  usw.  b)  j.,  g,  mit GS.  ^arff(sd."'',  Sp.  512  f.;' Stverz,),  vom Paradies:    'nl  garS  Y..,#5.8;  50.  4,  57. 15;
19346:•  j.  "nmänya-  Adj.  'dem  Haus  an-,  zu- gehörig, Haus-':  kaya  ratavSf  'yS  vTsyS zantumü  dähyumS  tarakuilrS  pu:^e  Y. /(>.  18;  —  kaya  ai^hh  (näml  rajüif) ratavsi  'yasla  vJsyas^a  zantumasca  (sd.)  . . Y.  ig.  18.  A)  m.  Name  der  Gottheit  der Häuser*':  'nrmca  asavaram  aiaht  ratum G.5.6;  —  'nyche  raSa'^G.5,6;  —  btnjJm 'nXmla  Y.  2.  7;   —  hryjyäi  'yäila  Y. /.  7.
19348:•  j.  "nmänya-  Adj.  (fem.  'yä-)  Adj.  'zur Gottheit  Nmänya  gehörig,  mit  ihr  in  Be- ziehung stehend':  mihra..'ya  ratvSvTsya zantuma  dahyuma  zara%u^trB.t3ma  Yt  lO. "5;  —  fravasayS  -yä  vlsyi  ..Y.17.18.
24419:•  j,  vis-patay-''  m.  'Herr,  Gebieter  eines Dorfes,  einer  Gemeine;  Gemeindeherr'; a)  im  eig.  Sinn,  mit  Gen.  von  vis-''' :  nmanahe va  nmanö.paitii  vTsB  vä  'paitis  zantSu^  vä zantupaitis  daiähSui  vü  daitihupaiti/  Yt. io.  18;  84;  —  vTsö  •paitim  Vr.j.  2,  V. 7- 41, 9-ZT,  —  viss  'isi/  V. !o.  5,  Y.  13.  i, Vyt/o;  —  vTsU'tJe  Yt/0. 17;  —  visqm 'paitis  {KV.)  Yl/0.  18;  —  vujs 'pttihm ftilirikqm  V.  7.  42  3'.  b)  von  Göttern : kaoma  nmStUS.paitt  'patte  .  .  Y.p.27;  — mihnm  ..  taxnam  'pattlm^'  YLJO.112.
24550:•  j.  'visya-  Adj.  'dem  Dorf,  der  Ge- meinde an-,  zugehörig,  Gemeinde-':  kaya ratavSi  nmänyS  'yS  zanlumS  dähyumS  zara- 'hustrS  puxis  Y.jp.  18;  —  kaya  airihi (näml.  rajsU)  ratavsl  nmänyasca  'yasca zantumas{^^.)ca  . .  Y.  ig.  18.  A)  m.  Name der  Gottheit  der  Gemeinden**:  'simca asavamm  afa/ie  ratBm  G.  /.  7 ;  —  'syeke rakwS  G.i.T,  —  süvatihaSm  'sTmca  Y. 2-3,  13;  —  sävarshSe  'syäiia  Y./.3,  23.
--- AHM ---
326:famous throughout Western Asia, and soon penetrated to the Greeks, If we array our facts and theory around the year 441 as the date when the religious mixture was so prominently advertised as to induce the ZarathuStrian priests to provide it with a scripture, we may expect that by the end of the fifth century the Magi will have been driven to acknowledging Zoroaster as their prophet. This dating squares well with the familiarity of fourth-century Greeks with Zoroaster’s name, and Herodotus’ failure to mention it.} To Persian Mazdayasnians, of course, the prophet’s name was well known long before the Magi usurped it, as the use of the name Spitamas in the time of Artaxerxes I shows (see Henning, Zor. 28, n. I). But foreign odservers could not be expected to penetrate to the remote origins of what was merely one of the numerous Persian cults, To them the Persian religion quite rightly consisted in what the Magi did and said, and they became aware of Zoroaster’s importance only after the Magi cared to assure them of it.
541:If we only had Y 42.2 one might have thought that the second line we have quoted contained a chiastic gloss to the dvandva jaya dworastara,§ the ‘fashioner’ being Mazdah, and the ‘protector’ Zarathustra. This interpretation is excluded by Y 57.2, where Mazdah is clearly distinguished from either member of the dvandva. The Pahlavi commentator of Y 57, having failed to recognize the dual endings, explained the dvandva by. panak brinkar mihr ‘the protector and fashioner, Mithra’. Although his ignorance of Avestan grammar led him astray, it is very likely that the tradition which made him look for Mithra in this expression is correct. As Darmesteter said (24, i, 369, n. 5), after referring to
566:heresy. Hence they had no occasion to discover through Sponta Mainyu demiurgic qualities in Mithra, and did not pass on any demiurzic notions to the Zoroastrian author of the Mithra Ya&t. Here is further indication, if any more is needed, that the so-called ‘Zoroastrianization” of non-ZarathuStrian gods is very far fram implying the imposition of ZarathuStrian notions on the gods of pantheistic Mazdahism. If the author of the Mithra Ya8t had had any intention of ‘ZarathuStrianizing’ Mithra, he could have turned to his own ZarathuStrian school of thought, and develaped the association of Mithra with Spenta Mainyu into joint subordination to Mazdah, assigned to Mithra demiurgic functions, replaced the dvandva mifra ahura by the dvandva payé 9warastarda, and so forth. Instead, he disrezarded this line of thought almost completely, and glorified Mithra on lines which he can only have found in non- Zarathu8trian sources. His aim, which he pursued with scrupulous honesty, was to portray Mithra not as ZarathuStrians might wish him to be, but as he was in the eyes of men who had behind them a long tradition of Mithraic worship, and knew what to expect from an authoritative hymn, such as the Mithra Ya8t was intended to be. Several centuries later, however, we may assume that a Persian Zoroastrian school evolved from the dvandva payi dworastara and its use as sudject of Gwarasats ‘they fashioned’ in Y 57.2, the idea of a demiurgic Mithra, thus preparing the ground for the Persian Manichean wentification of the Spiritus Vivens with Mihr-yazd (see above, p. 41).
700:5. May he jain us for assistance, may he join us for (the granting of} spaciousness, may he join us for support, may he join us for mercy, may he join us for therapy, may he join us for ability to defeat the opponent,! may he jain us for a comfortable existence, may he join us for gwnership of Truth,? he who is strong and victorious, he whom the whole? material world must needs worship, pray t, and refrain from deceiving, grass-land magnate Mithra.
755:atGit® dim ndit ragayente® fr3na ayangm ma9rangm
896:magnate Mithra: ‘Ah grass-land magnate Mithra! It is to (Ht. before) Mithra these fast horses are taking us!? These strong-armed (viz. Mithra, RaSnu, Sraga), O Mithra, are destroying us with the knife!’?
1025:It is you who destroy the enmities of the enemies, it is you who destroy the enmities of the inimical: do destray the slayers of Truth-awning men!
1352:} Other suggestions on the origin of the names Cautes and Cautsdates, to which H. W. Bailey kindly drew my attention, have no Sasis in reality: Louis H. Gray, Muséon, 1915, 139 sgq., connected Caut- with Gr: xaiw, and understood the names as meaning ‘the burning’ and ‘he who drops the burning (torch)’; H. H. Schaeder, ZDMG, 1923, xcv1, imagined that Turk. gut, which translates MIr, derivatives of Olr. x"aranah- (cf. Bailey, Zor. Prod. 54 3q., 226 57.), Zaes back to a Mir, word derived from Ols. *Rauta-, an unexplained synonym, of x*aronah-; hence Cautes<*kauta-dé- was for him identical with Mithru’s epithet x*arand.d@- in Yt 12.16. 1. Scheftelswitz, Acta Orientalia, x1, 339, n., interpreted Cauzes as ‘plenty’ (comparing Arm. dost (etc.) heap’), and Cautopates as ‘decline of plenty’.
1456:From this commentary we learn that in the prayer the words hatgm... ya~ham ‘entium,,.quarum’, hence also tds(éa) ‘eas(que)’, refer ta the female Amo3a Spantas Armaiti, Amsratat, and Haurvatat. Inevitably, then, both hatgm and tasd@ tasc@ ‘easque easque’ each refer to all the Ampsa Spantas together. From the question and answer at the end af (4) we learn that the prayer is dedicated to the Amo%a Spentas, who in the prayer are called ‘Entities’ (a@tam).{ This is unmistakably canfirmed by the last sentence of Y 4.25, which, as Geldner in his edition made clear both in a note and Sy the spacing af the printed lines, introduces the yebhé hatam prayer of which Y 4.26 consists:
1477:$1, ‘Battlefield’ seems to be the meaninz of aragah-, a3 against araza- ‘hatthe’. gatd arazahe in Yt 19.42 is probably gen. of a compound gatd .araza-.
--- IRN Farahvashi ---
45:۰ ریال :964-03-3604-1 18817
48:چاپ ششم: ۱۳۸۲: ۰ ۱۳۹۰۰ ریال.
49:۱ ایران - - تمدن - -مقاله‌ها وخطابه‌ها. ۲. آریاییان. ۳. کورش هخامنشی, شاه ایران؛ -
58:تاریخ انتشار : پاییز ۱۳۸۲ (چاپ ششم)
62:بها: ۱۳۰۰۰ ریال
```


## [2026-09-14T01:15:40.032Z] TOOL CALL #35: WebFetch

```json
{
 "url": "https://www.iranicaonline.org/articles/ray-i-ancient",
 "prompt": "What are the ancient names of Ray: Old Persian Ragā, Avestan Raγā, Greek Rhagai/Rhages, Median district, Seleucid Europos, Parthian Arsacia? Quote the relevant sentences."
}
```


### [2026-09-14T01:15:41.158Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-14T01:15:42.213Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Ray'\\|'Rai\\|Medien.*Rag\\|Raga\" BRT.txt | head -5; echo \"--- HJB ---\"; grep -n -i \"dragoman\\|Rages\\|Rhagae\" HJB.txt | head -5"
}
```


### [2026-09-14T01:15:42.286Z] TOOL RESULT

```
--- HJB ---
9030:DRUOGERMAN,  s.  Neither  this word  for  an  *  interpreter,*  nor  the Levantine  dragoman^  of  which  it  was  a quaint  old  English  corruption,  is  used in  Anglo-Indian  colloquial ;  nor  is  the Arab  tarjwnuZn^  which  is  the  correct form,  a  word  usual  in  Hindustani.  But the  character  of  the  two  former  words seemfl  to  entitle  them  not  to  be  passed over  in  this  Glossary.  The  Arabic  is  a loan-word  from  Aramaic  targimdnj  me- Uurgihndnj  *an  interpreter' ;  the  Jewish TarpunUy  or  Chaldee  paraphrases  of  the Scriptures,  being  named  from  the  same root.  The  ori^al  force  of  the  Aramaic root  is  seen  in  the  Assyrian  ragdmu^ ♦to  speak,'  rigmu,  *the  word.'  See Proe.  Soc.  BibL  Arch.,  1883,  p.  73,  and DMxh,  The  Hebrew  L<mg,  viewed  in ike  Light  of  Assyrian  Research,  p.  (VO. In  old  Italian  we  find  a  form  some- what nearer  to  the  Arabic.  (See  quota- tion from  Pegolotti  below.)
9034:ViUehardonin,  early  in  the  18th  century, mee  dmgbaiiMit,  [and  for  other  early  forma aee  N.EJ>.  8.Y.  Dragoman.']
9036:o.  1848.  — "And  at  Tana  you  should furnish  yourself  with  dragomans  (tnzei- jOJuaAy—PegolottCe  Handbook,  in  Catkay, &c.,  ii.  291,  and  App.  iii.
9388:o.  1665.— "On  m'avoit  fait  a  Sourat fljande  estime  des  Paffodes  d*Elora  .  .  . (and  after  describinjg^  tnem)  .  .  .  Quoiqu'il en  soit,  si  Ton  consid^re  cette  quantite  de Temples  spacieux,  remplis  de  pilastres  et  de oolonnes,  et  tant  de  railliers  de  figures,  et le  tout  taill€  dans  le  roc  vif,  on  pent  dire aveo  verity  que  ces  ouvrages  surpassent  la force  humaine ;  et  qu'au  moins  les  grens  du si^de  dans  leouel  ils  ont  4t6  faits,  irtftoient pastout-2k-fait  barbares."— T^&SMTioe,  v.  p.  222.
13048:Laridii,  which  they  told  ma  was  in  mat rogue  in  Java,  and  in  all  those  other  lalandB of  the  Far  East.  This  said  beverage  seemed to  me  in  truth  an  admirable  thing, — ^not  for use  at  every  meal  (it  is  too  strong  for  that), — ^but  as  a  tonio  in  case  of  debifity,  and  to make  tasty  possets,  much  better  tnan  those we  make  with  Muscatel  wines  or  Cretan malmseys.  So  I  asked  for  the  recipe ;  and am  talnng  it  to  Italy  with  me.  ...  It seemed  odd  to  me  that  those  hot  southern regions,  as  well  as  in  the  environs  of Hormuc  here,  where  also  the  heat  is  greal they  should  use  both  spice  in  their  food  ana spirits  in  their  drink,  as  well  as  sundry other  hot  beverages  like  this  larkin."— P. della  VaOe,  ii.  475.
```


## [2026-09-14T01:15:50.619Z] TOOL CALL #37: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Targum",
 "prompt": "Etymology of English Targum and the Hebrew/Aramaic תרגום targum — quote it, plus Targumist if present."
}
```


## [2026-09-14T01:15:52.387Z] TOOL CALL #38: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AA%D8%B1%D8%AC%D9%85%D9%87",
 "prompt": "Persian ترجمه: etymology (borrowed from Arabic ترجمة?) and meaning. Also anything about ترجمان in Persian."
}
```


### [2026-09-14T01:15:55.908Z] TOOL RESULT

```
# Targum Definition and Etymology

Based on the Wiktionary entry, **Targum** is "Alternative letter-case form of targum," with plural forms **Targums** or **Targumim**.

## Key Information

**English Usage:** The noun refers to what is defined in the lowercase "targum" entry (the page indicates you should consult that entry for the full definition).

**Pluralization:** The word has irregular plurals—"Targums" (English-style) or "Targumim" (Hebrew-style, reflecting its Aramaic-Hebrew origin).

**Derived Term:** Targumist (one who works with targums)

**Spanish:** In Spanish, *Targum* functions as a masculine proper noun meaning "targum."

## Etymology Context

The page references Hebrew/Aramaic **תרגום** (*targum*) as the etymological source, indicating this term originates from Semitic languages. A targum traditionally refers to an Aramaic paraphrase or translation of Hebrew biblical texts, though the full etymological explanation appears in the lowercase entry.
```


### [2026-09-14T01:15:57.763Z] TOOL RESULT

```
# Persian ترجمه (tarjuma/tarjome)

## Etymology
The Persian word ترجمه is "borrowed from Arabic تَرْجَمَة (tarjama)," according to the Wiktionary entry. The Arabic term itself has deeper roots, potentially tracing back through Classical Syriac and Akkadian linguistic traditions.

## Meaning
ترجمه means "translation" in Persian. The entry lists the plural forms as ترجمه‌ها (tarjuma-hā/tarjome-hâ) or تراجم (tarājim/tarâjem).

## Usage and Derived Terms
The noun appears in several compound expressions, including:
- ترجمه کردن (to translate/perform a translation)
- ترجمه‌ٔ حال (a brief biographical note)
- ترجمه‌ٔ ماشینی (machine translation)

## Note on ترجمان
The web page does not contain information specifically about ترجمان in Persian, though the etymology tree shows ترجمان (tarjumān) as an Arabic term that may relate to the word's broader etymological family.
```


## [2026-09-14T01:15:59.263Z] AGENT

Now let me archive the sources.


## [2026-09-14T01:16:04.407Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n \"https://en.wiktionary.org/wiki/dragoman\" \\\n \"https://en.wiktionary.org/wiki/%D8%AA%D8%B1%D8%AC%D9%85\" \\\n \"https://en.wiktionary.org/wiki/targumannum\" \\\n \"https://www.etymonline.com/word/dragoman\" \\\n \"https://www.ahdictionary.com/word/search.html?q=dragoman\" \\\n \"https://en.wiktionary.org/wiki/%D8%B1%DB%8C\" \\\n \"https://en.wikipedia.org/wiki/Rhages\" \\\n \"https://en.wikipedia.org/wiki/Dragoman\" \\\n \"https://en.wiktionary.org/wiki/Targum\" \\\n \"https://en.wiktionary.org/wiki/%D8%AA%D8%B1%D8%AC%D9%85%D9%87\" \\\n \"https://abadis.ir/fatofa/%D8%B1%D8%A7%D8%B2%D9%82%DB%8C/\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 414, roots Raga / Ragamu: Ray, razeqi grape, dragoman/targum chain\" 2>&1 | tail -2\ndone"
}
```


### [2026-09-14T01:16:11.808Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/606261edd832a8af.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/697e7b4719477dac.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e57e6c2bb95384d8.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/693934558ae95a8d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/96d6d0f0b893be53.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/677da57cedfb0866.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f4b52087f46306cb.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0fa2f518f7674447.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/50d73089c57efc70.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c2336b3075a9efd3.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c1b0352ba2a6916e.txt
```


## [2026-09-14T01:16:16.221Z] TOOL CALL #40: Bash

```json
{
 "command": "mkdir -p data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg414.png data/verification/sources/refs/ocr/BOOK/414.png && echo ok && sed -n '1,80p' tools/verify_check.py"
}
```


### [2026-09-14T01:16:16.305Z] TOOL RESULT

```
ok
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
```


## [2026-09-14T01:16:18.868Z] TOOL CALL #41: Bash

```json
{
 "command": "sed -n '80,140p' /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-14T01:16:18.918Z] TOOL RESULT

```
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


## [2026-09-14T01:17:14.980Z] AGENT

Now I'll write the verification file.


## [2026-09-14T01:23:20.279Z] TOOL CALL #42: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-414.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW_RY   = \"https://en.wiktionary.org/wiki/%D8%B1%DB%8C\"\nW_RHAG = \"https://en.wikipedia.org/wiki/Rhages\"\nW_ABAD = \"https://abadis.ir/fatofa/%D8%B1%D8%A7%D8%B2%D9%82%DB%8C/\"\nW_DRAG = \"https://en.wiktionary.org/wiki/dragoman\"\nW_TRJM = \"https://en.wiktionary.org/wiki/%D8%AA%D8%B1%D8%AC%D9%85\"\nW_TARG = \"https://en.wiktionary.org/wiki/targumannum\"\nW_ETY  = \"https://www.etymonline.com/word/dragoman\"\nW_AHD  = \"https://www.ahdictionary.com/word/search.html?q=dragoman\"\nW_WPD  = \"https://en.wikipedia.org/wiki/Dragoman\"\nW_TGM  = \"https://en.wiktionary.org/wiki/Targum\"\nW_PTRJ = \"https://en.wiktionary.org/wiki/%D8%AA%D8%B1%D8%AC%D9%85%D9%87\"\n\ndata = {\n \"pdf_page\": 414,\n \"book_page\": 384,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-13\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"Ragâ, Rağâ\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"Old Persian Ragā- (𐎼𐎥𐎠) / Avestan Raγā- 'Ragha, a district and city of Media, mod. Ray'\",\n   \"note\": \"The root box is right on all three counts. Old Persian Ragā- is attested in the Bisotun inscription (DB 2.71 f. Ragā nom.sg.f.; DB 3.2 Ragāyā abl.), Avestan Raγā- in Vd. 1.15 f. and Y. 19.18 (raγa- zaraθuštriš). Nourai's two spellings 'Ragâ, Rağâ' correspond exactly to the OP (g) and Avestan (γ, transcribed ğ by him) variants, so the double headword is not an error. Kent s.v. Raga- gives the whole ancient dossier — Elamite rák-ka4-an, Akkadian ra-ga-ʾ, Greek Ῥάγης — and says 'now Rai near Teheran'. The only thing to flag on the whole entry is the Greek box (#4).\",\n   \"note_fa\": \"نام باستانی «ری» در پارسی باستان Ragā- (𐎼𐎥𐎠، در کتیبهٔ بیستون، بند ۲ سطر ۷۱ و بند ۳ سطر ۲) و در اوستایی raγā- (وندیداد ۱:۱۵ و یسنا ۱۹:۱۸) است؛ پس هر دو صورتی که نورایی در سرریشه آورده («Ragâ» پارسی باستان و «Rağâ» اوستایی) درست‌اند و برچسب زبانی و معنای آن نیز درست است. کنت در واژه‌نامهٔ پارسی باستان ذیل Raga- صورت‌های عیلامی rák-ka4-an، اکدی ra-ga-ʾ و یونانی Ῥάγης را می‌آورد و می‌نویسد «امروز رِی نزدیک تهران». ادعای نورایی در این جعبهٔ ریشه پذیرفتنی و درست است؛ تنها جعبهٔ یونانی (گرهٔ ۴) اشکال دارد.\",\n   \"sources\": [W_RY, W_RHAG],\n   \"ref_check\": [\n    {\"ref\": \"MON5:636\", \"status\": \"not_checked\", \"note\": \"Mo'in's Farhang-e Farsi vol. 5 (a'lam/proper names) is the one part of the set with no scan anywhere online (refs_online.json: 'The a'lam volumes (MON5/MON6 citations) are NOT online'); vajehyab/abadis carry no Mo'in proper-name entries. The claim itself (Ray < OP Ragā) is independently confirmed by Kent and Hübschmann.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"KNT\", \"where\": \"KNT.txt leaf 230, Lexicon s.v. Raga-\", \"stance\": \"supports\", \"note\": \"\\\"Raga- sb. 'Rhages', a district in Media: Elam. rak-qa-an, Akk. ra-ga-', Gk. 'Payys [= Ῥάγης], now Rai near Teheran. Ragā nsf. DB 2.71f. Ragāyā absf. DB 3.2.\\\" (grep -n 'Raga' KNT.txt)\"},\n    {\"src\": \"HUB\", \"where\": \"Persische Studien p. 249, §141\", \"stance\": \"supports\", \"note\": \"\\\"Aber ap. rg (= ry) ist sonst = np. ry. Die Form Rai (für ap. raga-) ist im Syr. schon im Jahr 430 bezeugt, ZDMG. 48, 413.\\\" — Hübschmann derives NP Rai directly from OP raga- and dates the contracted form to the 5th c. (grep -n 'Rai' HUB.txt, line 8904)\"},\n    {\"src\": \"BRT\", \"where\": \"BRT.txt, searched for raγa-/Raga-/Ragha\", \"stance\": \"silent\", \"note\": \"Bartholomae's Altiranisches Wörterbuch certainly has raγā- (col. 1508 f.), but the local OCR renders Avestan γ unreliably (as y, ^, 9) and no grep pattern ('raγ', 'Raga', 'Ragha', 'rag[aā]') retrieved the entry; recorded as not usable rather than absent.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Persian\",\n     \"words\": \"Ray; râzî; râzegî\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"Ray «ری» is the regular New Persian outcome of OP Ragā- / Av. raγā-: intervocalic OP -g- before the ending was lost and the group contracted, OP raga- > MP Ray (Pahlavi ldy /Ray/) > NP ری; Hübschmann (Pers. Stud. 249) notes that the contracted form Rai is already attested in a Syriac source of AD 430, i.e. the change was complete by late Sasanian times. The nisba râzî «رازی» 'of Ray' (as in Moḥammad b. Zakariyyā al-Rāzī, Faḵr-al-Dīn Rāzī) preserves the older stem in -z-, which goes back to the Middle Persian/Arabicised adjective rāzī built on rāz-, the older base surviving in the ethnicon while the city name itself contracted — Borhān-e Qāṭeʿ knows exactly this pair and explains it with a legend of two brothers Ray and Rāz. The third word râzegî «رازگی» 'grape of Ray' is the weak link: Nourai himself notes it 'was not found in MON', and I could not find رازگی or رازکی in the sense 'grape' in Mo'in, in Borhān-e Qāṭeʿ or in Dehkhoda (رازک in Mo'in is the hop plant, Humulus, a different word). The attested Persian grape word is رازقی (node #3), which is formally an Arabic nisba; *rāzegī is therefore best regarded as Nourai's (or Emām Šuštarī's) reconstructed pre-form rather than a recorded word.\",\n     \"derivation_fa\": \"«ری» دنبالهٔ منظم Ragā- پارسی باستان و raγā- اوستایی است: g میان‌واکه‌ای افتاده و هجاها در هم فشرده شده‌اند (پارسی باستان raga- > فارسی میانه Ray [نوشتار کتیبه‌ای ldy] > فارسی نو ری)؛ هوبشمان (مطالعات فارسی، ص ۲۴۹) یادآور می‌شود که صورت کوتاه‌شدهٔ Rai همان سال ۴۳۰ میلادی در یک متن سریانی گواهی شده است. صفت نسبی «رازی» همان ستاک کهن‌تر با ز را نگه داشته و در نام‌هایی چون محمد بن زکریای رازی و فخر رازی زنده مانده است؛ برهان قاطع نیز همین جفت ری/رازی را می‌آورد، هرچند با ریشه‌شناسی عامیانهٔ دو برادر به نام‌های «ری» و «راز». اما «رازگی» به معنی انگور در معین، برهان قاطع و دهخدا یافت نشد (خود نورایی هم در یادداشتش به این نکته اشاره کرده) و «رازک» در معین نام گیاه دیگری (رازک، Humulus) است؛ بنابراین دو واژهٔ نخست درست‌اند و سومی گواهی‌ناشده است.\",\n     \"sources\": [W_RY, W_RHAG],\n     \"ref_check\": [\n      {\"ref\": \"BQT:985\", \"status\": \"partial\", \"note\": \"BQT_v2_pages.txt leaf 447 (printed ≈ leaf+540 = 987, i.e. within the ±2 drift of Nourai's 985) carries the ری entry: «ری - بفتح اول وسکون ثانی: شهری است در عراق ... گویند او را برادری بود «راز» نام داشت ... شهر را بنام ری و اهل شهر را بنام راز کردند ... و اهل شهر را رازی - و بزبان پهلوی راز پادشاه را گویند». So Borhān has Ray and رازی, as Nourai says, but only as a folk-etymological legend, and it says nothing about a grape رازگی.\"},\n      {\"ref\": \"FVF:278\", \"status\": \"not_checked\", \"note\": \"Emām Šuštarī, Farhang-e vāžehā-ye fārsi dar zabān-e ʿarabi: refs_online.json records no accessible copy (noorlib/ketabnak need login/JS, not on archive.org).\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BQT\", \"where\": \"vol. 2, leaf 447 ≈ printed p. 987, s.v. ری\", \"stance\": \"partial\", \"note\": \"gives ری and رازی but with the Ray/Rāz brothers legend; no رازگی.\"},\n      {\"src\": \"MON\", \"where\": \"MON_part1.txt lines 65655-65680 (ر ا ز block)\", \"stance\": \"silent\", \"note\": \"Mo'in's abridgement has رازق، رازقی، رازقیه، رازک but no رازگی at all — matching Nourai's own note '«râzegî» was not found in MON'.\"},\n      {\"src\": \"HUB\", \"where\": \"p. 249\", \"stance\": \"supports\", \"note\": \"\\\"Die Form Rai (für ap. raga-) ist im Syr. schon im Jahr 430 bezeugt\\\".\"},\n      {\"src\": \"HRN\", \"where\": \"HRN.txt, grep 'Rai'/'Rag'\", \"stance\": \"silent\", \"note\": \"Horn's Grundriss is a lexicon of common nouns; no entry for the toponym Ray.\"}\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"Arabic\",\n     \"words\": \"râzeqî\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"Arabic الرازقيّ (al-rāziqī) is a real word: in the classical lexica it denotes a kind of white grape (al-ʿinab al-mulāḥī) and white linen cloth (al-rāziqiyya), and Addī Šīr's Kitāb al-alfāẓ al-fārisiyya al-muʿarraba enters it among the Persian loans, glossing it 'the mulāḥī grape (and the wine made from it)' and deriving it «من رازی» — i.e. from the nisba to al-Rayy — explicitly quoting Borhān-e Qāṭeʿ's Ray/Rāz story in support. Phonetically the Arabisation is regular: a Persian adjective in -gī/-kī built on Rāz- is taken over with Arabic qāf for Persian g/k and the Arabic nisba ending -iyy, giving rāziqī. This is exactly Nourai's arrow, and Addī Šīr — an independent authority he does not cite here — backs it. It stays 'plausible' rather than 'confirmed' because the native Arabic lexicographers themselves usually derive الرازقي as a nisba to a name رازق rather than to الرَّيّ, and because the Persian pre-form rāzegī (node #1) is not itself attested.\",\n     \"derivation_fa\": \"«رازقی» در عربی واژه‌ای واقعی است: در فرهنگ‌های کهن عربی به معنی گونه‌ای انگور سفید (العنب الملاحی) و نیز جامهٔ کتانی سپید (الرازقیة) آمده است. ادّی شیر در «الألفاظ الفارسیة المعرّبة» آن را در شمار معرّبات فارسی آورده و می‌نویسد «(الرازق) ... العنب الملاحی ... من رازی» و برای تأیید، همان حکایت برهان قاطع دربارهٔ «ری» و «راز» را نقل می‌کند. از نظر آوایی نیز معرّب‌شدن قاعده‌مند است: صفت نسبی فارسی بر ستاک راز- با ابدال گ/ک فارسی به قاف عربی و افزودن یای نسبت عربی به رازقی بدل شده است. پس ادعای نورایی با احتیاط پذیرفتنی است؛ احتیاط از آن روست که لغویان عرب خودِ «رازقی» را معمولاً منسوب به نامِ «رازق» می‌دانند و صورت فارسی «رازگی» هم گواهی‌ناشده است.\",\n     \"sources\": [W_ABAD],\n     \"ref_check\": [\n      {\"ref\": \"FVF:278\", \"status\": \"not_checked\", \"note\": \"Emām Šuštarī not available in any form here (refs_online.json: no local file, noorlib/ketabnak behind login).\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"AFM\", \"where\": \"Addī Šīr, AFM_pages.txt leaf 73, s.v. (الرازق)\", \"stance\": \"supports\", \"note\": \"\\\"(الرازق) ... العنب الملاحي ... والخمر ... من رازى ... ورازقي بالفارسيّة يطلق ايضاً على العنب الملاحي، وقال في البرهان القاطع: «زعموا ان ... اسم احده[ما] ... راز ... هذه المدينة (اى ... الري)»\\\" — i.e. the Arabic grape-name is derived from the nisba of Rayy, citing Borhān exactly as Nourai's arrow requires.\"},\n      {\"src\": \"PLA\", \"where\": \"Asbaghi, Persische Lehnwörter im Arabischen (PLA_pages.txt / djvu text), grep رازق, rāziqī\", \"stance\": \"silent\", \"note\": \"no entry for rāziqī among Asbaghi's Persian loans in Arabic.\"},\n      {\"src\": \"ARB\", \"where\": \"al-Jawālīqī, al-Muʿarrab (ARB_mo3rb.txt), grep رازق\", \"stance\": \"silent\", \"note\": \"only unrelated hits (البرازق; a personal name); al-Jawālīqī does not list رازقي among the muʿarrab.\"}\n     ]\n    },\n    {\n     \"id\": 3,\n     \"lang\": \"Persian\",\n     \"words\": \"râzeqî\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Persian رازقی (rāzeqī) 'a small-berried grape; also the fragrant white jasmine and the perfume made from it' is, in its present shape, an Arabic word taken back into Persian: Moʿin tags it «[ع. ف.] (ص نسب.) منسوب به رازق» — an Arabic-Persian nisba — and the qāf spelling is the give-away, since Persian has no native q. The route is therefore the Persian→Arabic→Persian round trip Nourai draws: an adjective of Ray was Arabised as رازقي and re-entered Persian with Arabic phonology and orthography, after which the connection with Ray was no longer felt (hence Moʿin's and Dehkhodā's synchronic analysis 'nisba to رازق'). Dehkhodā and Moʿin both record the two senses (the grape and the jasmine), so the word and gloss are right.\",\n     \"derivation_fa\": \"«رازقی» در فارسی امروز واژه‌ای معرّب است که دوباره به فارسی بازگشته؛ معین آن را «[ع. ف.] (ص نسب.) منسوب به رازق» می‌نامد و همین قاف، نشانهٔ گذر واژه از عربی است، چون فارسی قاف بومی ندارد. بنابراین همان چرخهٔ فارسی ← عربی ← فارسی که نورایی رسم کرده درست است: صفت نسبی «ری» در عربی به رازقي بدل شد و با آوا و املای عربی به فارسی بازگشت و پیوندش با «ری» فراموش شد، چندان‌که معین و دهخدا آن را همزمانی «منسوب به رازق» تحلیل می‌کنند. معنی‌ها (انگور ریزدانه و نیز گل یاسمن سفید خوشبو و عطر آن) در هر دو فرهنگ ثبت است.\",\n     \"sources\": [W_ABAD],\n     \"ref_check\": [\n      {\"ref\": \"FVF:278\", \"status\": \"not_checked\", \"note\": \"same as node #2: Emām Šuštarī inaccessible.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"MON\", \"where\": \"MON_part1.txt line 65664, s.v. رازقی\", \"stance\": \"partial\", \"note\": \"«رازقی: [ع. ف.] (ص‌نسب.) منسوب به رازق. (گیا.) نوعی انگور دارای دانه‌های کوچک. (گیا.) گیاهی ... از خانوادهٔ یاسمن‌ها ... گل‌هایش سفید ... و پر عطر» — confirms the word, the Arabic route ([ع.]) and the 'small-berried grape' gloss, but analyses it as a nisba to رازق, not to Ray.\"},\n      {\"src\": \"BQT\", \"where\": \"BQT_v1/v2_pages.txt, grep رازق/رازک\", \"stance\": \"silent\", \"note\": \"no رازقی headword retrieved from the Borhān OCR.\"},\n      {\"src\": \"AFM\", \"where\": \"leaf 73\", \"stance\": \"supports\", \"note\": \"«ورازقي بالفارسيّة يطلق ايضاً على العنب الملاحي» — Addī Šīr explicitly records رازقی as a Persian word for the same grape, i.e. the form does exist on the Persian side of the loan.\"}\n     ]\n    },\n    {\n     \"id\": 4,\n     \"lang\": \"Greek\",\n     \"words\": \"Râzex; râzakěne\",\n     \"verdict\": \"transcription_suspect\",\n     \"derivation\": \"The idea is right — Greek did take the name of Ray over from Old Iranian — but neither printed form is a Greek word. The attested Greek names of the city are Ῥάγαι (Rhágai, Polybius, Strabo, Isidore of Charax), Ῥάγα, and Ῥάγης / Ῥάγοι (Rhágēs, Rhágoi — the form of the Book of Tobit, whence Latin Rhagae, Rhaganae and the Vulgate 'Rages'); the district is Ῥαγιανή (Rhagianē) beside Χοαρηνή and Κομισηνή. Kent's lexicon s.v. Raga- gives precisely 'Gk. Ῥάγης'. A Greek rendering of OP Ragā- must have γ; a -ζ- is impossible, since Greek transcribed the Iranian stop, not the later Persian -z- of the nisba رازی. 'Râzex' is therefore a garbling of Ῥάγης (Rhágēs) and 'râzakěne' of the toponymic adjective in -ηνή (Ῥαγιανή / *Ῥαγηνή). The printed page (pdf 414, copied to data/verification/sources/refs/ocr/BOOK/414.png) shows 'Râzex : city of Ray' and 'râzakěne : from Ray' exactly as the JSON has them, so the extraction is faithful and the odd forms are the book's — most likely Nourai re-transliterating Moʿin's Persian-script rendering of the Greek back into Latin letters and mistaking گ for ز.\",\n     \"derivation_fa\": \"اصل ادعا درست است — یونانیان نام «ری» را از ایرانی باستان گرفته‌اند — اما هیچ‌یک از دو صورت چاپ‌شده یونانی نیست. نام‌های گواهی‌شدهٔ یونانی این شهر Ῥάγαι (راگای، نزد پولوبیوس و استرابون)، Ῥάγα و Ῥάγης/Ῥάγοι (راگس، صورت کتاب طوبیت که لاتینی Rhagae و «Rages» وولگات از آن آمده) است و نام ناحیه Ῥαγιανή (راگیانه) در کنار خوارنه و کومیسنه. کنت نیز ذیل Raga- همان «Gk. Ῥάγης» را می‌آورد. برگردان یونانی Ragā- ناگزیر باید گاما داشته باشد و «ز» در آن ناممکن است. پس «Râzex» گونهٔ مغشوش Ῥάγης و «râzakěne» گونهٔ مغشوش صفت مکانی با پسوند ‑ηνή است. تصویر صفحهٔ چاپی (پی‌دی‌اف ۴۱۴) نشان می‌دهد که استخراج داده درست و امانت‌دارانه بوده و خطا از خود کتاب است — احتمالاً نورایی صورت یونانی را از خطّ فارسیِ فرهنگ معین بازنویسی کرده و «گ» را «ز» خوانده است.\",\n     \"error_in\": \"book\",\n     \"book_prints\": \"Râzex : city of Ray / râzakěne : from Ray\",\n     \"correct_form\": \"Ῥάγης / Ῥάγαι (Rhágēs, Rhágai), adj. Ῥαγιανή (Rhagianē)\",\n     \"sources\": [W_RHAG, W_RY],\n     \"ref_check\": [\n      {\"ref\": \"MON5:636\", \"status\": \"not_checked\", \"note\": \"Moʿin vol. 5 (aʿlām) has no scan online at all (refs_online.json), so it cannot be checked whether the garbling is Moʿin's or Nourai's; Moʿin's aʿlām entries normally give such foreign forms in Persian script, which is the likeliest source of the confusion.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KNT\", \"where\": \"KNT.txt leaf 230, s.v. Raga-\", \"stance\": \"contradicts\", \"note\": \"\\\"Gk. 'Payys\\\" = Ῥάγης — a γ, not a ζ; no form with -z- exists.\"},\n      {\"src\": \"HJB\", \"where\": \"Hobson-Jobson, grep 'Rhagae'/'Rages'\", \"stance\": \"silent\", \"note\": \"no entry for the toponym.\"},\n      {\"src\": \"MON\", \"where\": \"MON_part1/part2 (2-vol abridgement)\", \"stance\": \"silent\", \"note\": \"the abridgement omits the aʿlām volumes, so the ری proper-name entry with the Greek forms is not in the text available here.\"}\n     ]\n    }\n   ]\n  },\n  {\n   \"entry\": 2,\n   \"root\": \"Ragâmu\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"Akkadian ragāmu(m) 'to shout, call out; to summon, to sue, to prophesy'\",\n   \"note\": \"The Akkadian verb and its gloss are correct: ragāmu 'to shout, call out, exclaim; (in legal use) to bring suit', with the noun rigmu 'voice, cry, word'. Klein p. 1573 s.v. Targum states the whole of Nourai's tree in one line, and Hobson-Jobson s.v. DRUGGERMAN says the same ('The original force of the Aramaic root is seen in the Assyrian ragāmu, \\\"to speak\\\", rigmu, \\\"the word\\\"'). What is NOT certain is the step ragāmu → targumānu that the root box asserts by putting Targumânu in the same box (see node #1): modern Assyriology treats targumannu as of unknown origin, possibly an Anatolian (Hittite/Luwian tarkummāi- 'to announce, explain') loan. Note also that in the printed chart Targumânu stands inside the root box together with Ragâmu; the JSON has promoted it to a separate node #1 with parent #0 — a structural normalisation, not a misreading.\",\n   \"note_fa\": \"فعل اکدی ragāmu «فریاد زدن، بانگ کردن، خواندن؛ (در کاربرد حقوقی) دادخواهی کردن» و اسم rigmu «بانگ، سخن» واقعی‌اند و معنایی که نورایی داده درست است. کلاین در ص ۱۵۷۳ ذیل Targum همین زنجیره را یک‌جا می‌آورد و «هابسن‑جابسن» نیز ذیل DRUGGERMAN می‌نویسد که نیروی اصلی ریشهٔ آرامی را در آشوری ragāmu «سخن گفتن» و rigmu «واژه» می‌توان دید. آنچه قطعی نیست پیوند ragāmu ← targumannu است (نگاه کنید به گرهٔ ۱): آشورشناسی امروز targumannu را با خاستگاه نامعلوم و چه‌بسا وام‌واژه‌ای آناتولیایی (هیتی/لووی tarkummāi- «اعلام کردن، شرح دادن») می‌داند. یادآوری: در چاپ کتاب، Targumânu درون همان جعبهٔ ریشه با Ragâmu آمده و در داده‌های استخراج‌شده به گرهٔ جداگانهٔ ۱ تبدیل شده است؛ این یک هنجارسازی ساختاری است نه خطای خوانش.\",\n   \"sources\": [W_DRAG, W_TARG, W_ETY, W_AHD, W_WPD],\n   \"ref_check\": [\n    {\"ref\": \"KLN:1573\", \"status\": \"supports\", \"note\": \"Verified: KLN_1966.txt form-feed block 835 (the block containing printed page numbers 1573/1574, between the '1572' of block 834 and the '1577' of block 836), s.v. Targum: \\\"Mishnaic Heb. targum ... rel. to Aram. targem, Arab. tarjama, of s.m. All these verbs are denominated fr. Akkad. targumanu, 'interpreter' (fr. ragamu, 'to call'), whence also Aram. turgimana, 'interpreter, translator'. Cp. meturgeman. Cp. also dragoman.\\\" — literally Nourai's whole tree, ragāmu gloss included.\"},\n    {\"ref\": \"AHD:396\", \"status\": \"not_checked\", \"note\": \"AHD:396 is a page of the 1975/76 New College Edition (the main dictionary, not the IE appendix), which is lending-only on archive.org; the local proxy AHD_watkins1985.txt contains only Indo-European roots and is silent on Semitic. The online AHD entry for dragoman, however, gives the identical chain (ME dragman < OF drugeman < ML dragumannus < MGk dragoumanos < Arabic tarjumān < Aramaic targəmānā < Akkadian targumannu), so the citation is substantively right.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"p. 1573 s.v. Targum; p. ~479 s.v. dragoman\", \"stance\": \"supports\", \"note\": \"dragoman entry: \\\"F. dragoman, drogman, fr. It. dragomano, fr. MGk. δραγουμάνος, fr. targuman, Egypt. pronunciation of Arab. tarjuman, fr. Aram. turghmana, ult. fr. Akkad. targumanu, 'interpreter'. See Targum.\\\"\"},\n    {\"src\": \"AKD\", \"where\": \"Zimmern, Akkadische Fremdwörter, p. 26 (AKD.txt line 88)\", \"stance\": \"supports\", \"note\": \"\\\"akk. targumānu, turgumānu Dolmetscher : > aram. targamānā, turgāmānā > arab. targamān, targuman, turgumān, woraus auch unser Dragoman); dazu neuhebr. targūm Übersetzung, 'Targum'.\\\" — the whole Akkadian→Aramaic→Arabic→European chain, plus Hebrew targum.\"},\n    {\"src\": \"HJB\", \"where\": \"Hobson-Jobson s.v. DRUGGERMAN (HJB.txt line 9030)\", \"stance\": \"supports\", \"note\": \"\\\"The Arabic is a loan-word from Aramaic targūmān, meturgemān, 'an interpreter'; the Jewish Targums ... being named from the same root. The original force of the Aramaic root is seen in the Assyrian ragāmu, 'to speak,' rigmu, 'the word.'\\\"\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Akkadian\",\n     \"words\": \"Targumânu\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"Akkadian targumannu(m) / turgumannu 'interpreter, dragoman' is well attested from Old Assyrian (Kültepe) onwards — the geminate -nn- of the standard form should be noted against Nourai's single -n-. The derivation from ragāmu that Nourai (following Klein and AHD) draws works morphologically: a t-prefixed noun of the type taPRuS plus the professional/appurtenance suffix -ān(n)u, giving *ta-rgum-ānu 'the one who speaks (for another)', which suits ragāmu's own semantic range ('to call out, to speak for the gods, to speak for another'). But it is not the only view and probably no longer the majority one: Wiktionary's Akkadian entry says flatly \\\"Unknown. It could be either a borrowing from another unattested language or a derivation from the verb ragāmum\\\", and many Anatolianists take targumannu as a loan from Hittite/Luwian tarkummāi-/tarkummiya- 'to announce, explain, translate', which would make the quadriliteral Semitic root t-r-g-m itself a back-formation from the loanword. Hence 'plausible' rather than 'confirmed': Nourai reports one of two live hypotheses without flagging the alternative.\",\n     \"derivation_fa\": \"واژهٔ اکدی targumannu(m)/turgumannu «مترجم، ترجمان» از دورهٔ آشوری کهن (کول‌تپه) به بعد گواهی شده است؛ توجه شود که صورت متعارف «نون» مشدّد دارد و نورایی آن را با یک نون نوشته است. اشتقاق آن از ragāmu که نورایی به پیروی از کلاین و AHD رسم کرده از نظر ساخت‌واژه ممکن است: پیشوند ta- بر ستاک و پسوند شغلی ‑ān(n)u، یعنی «کسی که به‌جای دیگری سخن می‌گوید»، که با دامنهٔ معنایی خود ragāmu («بانگ زدن، به‌جای خدایان سخن گفتن») هم می‌خواند. اما این تنها فرضیه نیست: ویکی‌واژه خاستگاه را «نامعلوم» می‌داند و بسیاری از آناتولی‌شناسان آن را وام‌واژه‌ای از هیتی/لووی tarkummāi- «اعلام کردن، شرح دادن» می‌شمارند که در آن صورت ریشهٔ چهارحرفی سامی t-r-g-m خودْ اشتقاق پسین از همین وام‌واژه است. پس ادعای نورایی با احتیاط پذیرفتنی است، نه قطعی.\",\n     \"sources\": [W_TARG, W_DRAG, W_WPD],\n     \"ref_check\": [\n      {\"ref\": \"KLN:1573\", \"status\": \"supports\", \"note\": \"KLN_1966.txt block 835 s.v. Targum: \\\"...denominated fr. Akkad. targumanu, 'interpreter' (fr. ragamu, 'to call')\\\" — Klein states the ragāmu derivation as fact, exactly as Nourai draws it.\"},\n      {\"ref\": \"AHD:396\", \"status\": \"not_checked\", \"note\": \"1976 New College page not open online; the current online AHD entry stops at 'Akkadian targumannu, interpreter' and does not carry it back to ragāmu, so the AHD support is for the word, not for the internal Akkadian etymology.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"AKD\", \"where\": \"Zimmern p. 26\", \"stance\": \"supports\", \"note\": \"\\\"akk. targumānu, turgumānu Dolmetscher\\\" heads the entry, with the note (DelHWB 713a; cf. 612a for ragāmu 'sprechen', rigmu 'Wort') — Zimmern likewise groups the noun with the verb.\"},\n      {\"src\": \"LKT\", \"where\": \"Lokotsch no. 2033 (LKT.txt line 4574)\", \"stance\": \"supports\", \"note\": \"\\\"[Vb. targama 'dolmetschen' aus syr. targem 'erläutern' ... beachte assyr. ragāmu 'sprechen', rigmu 'Wort', eigentlich 'schreien, rufen' ... sowie assyr. targumānu 'Dolmetsch'\\\".\"},\n      {\"src\": \"HJB\", \"where\": \"s.v. DRUGGERMAN\", \"stance\": \"supports\", \"note\": \"\\\"The original force of the Aramaic root is seen in the Assyrian ragāmu, 'to speak'\\\" (citing Delitzsch).\"}\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"Aramaic\",\n     \"words\": \"tŭrgemânâ\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Aramaic targəmānā / turgəmānā (emphatic state, Syriac ܬܰܪܓܡܳܢܳܐ targmānā) 'interpreter' is the direct Aramaic take-over of Akkadian targumannu during the long period of Akkadian–Aramaic bilingualism in Babylonia (roughly 8th–5th c. BCE), the same channel that gave Aramaic dozens of Akkadian technical terms; the Aramaic reshaping consists only in adding the emphatic-state ending -ā and (in the Jewish Babylonian form) rounding the first vowel, turgəmānā. Nourai's vocalisation 'tŭrgemânâ' matches Klein's 'turghmānā' (Jewish Aramaic); Syriac and AHD prefer targəmānā. From this noun Aramaic back-formed the verb targem 'he translated' and the noun targum (node #9).\",\n     \"derivation_fa\": \"صورت آرامی targəmānā/turgəmānā (حالت مؤکّد؛ در سریانی ܬܰܪܓܡܳܢܳܐ) «مترجم» وام مستقیم از اکدی targumannu است و در دورهٔ دوزبانگی اکدی–آرامی در بابل (تقریباً سدهٔ هشتم تا پنجم پیش از میلاد) وارد آرامی شده، همان راهی که ده‌ها اصطلاح فنی اکدی از آن به آرامی رفته است؛ دگرگونی آرامی تنها افزودن پایانهٔ حالت مؤکّد ‑ā و (در آرامی بابلی یهودی) گرد شدن واکهٔ نخست است. تلفظی که نورایی آورده (tŭrgemânâ) با صورت کلاین (turghmānā) می‌خواند، حال آنکه سریانی و AHD صورت targəmānā را ترجیح می‌دهند. از همین اسم، فعل آرامی targem «ترجمه کرد» و اسم targum ساخته شده است.\",\n     \"sources\": [W_DRAG, W_AHD, W_TARG],\n     \"ref_check\": [\n      {\"ref\": \"AHD:396\", \"status\": \"not_checked\", \"note\": \"printed page not accessible; the online AHD dragoman entry has \\\"from Aramaic targəmānā, from Akkadian targumannu\\\", i.e. the same arrow.\"},\n      {\"ref\": \"KLN:1573\", \"status\": \"supports\", \"note\": \"KLN_1966.txt block 835 s.v. Targum: \\\"...whence also Aram. turgimana [turghmānā], 'interpreter, translator'\\\"; and s.v. dragoman \\\"fr. Aram. turghmana, ult. fr. Akkad. targumanu\\\".\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"AKD\", \"where\": \"Zimmern p. 26\", \"stance\": \"supports\", \"note\": \"\\\"akk. targumānu ... : > aram. targamānā, turgāmānā\\\" — the loan direction Akkadian → Aramaic is Zimmern's own heading.\"},\n      {\"src\": \"KLN\", \"where\": \"p. 1573 and s.v. meturgeman\", \"stance\": \"supports\", \"note\": \"meturgeman entry: \\\"Aram. məthurgeman ... 'interpreter', which is a blend of targ[ə]mān and Heb. məthargem; see Targum\\\" — the Aramaic noun is the base of the whole family.\"},\n      {\"src\": \"AFA\", \"where\": \"Fraenkel, Die aramäischen Fremdwörter im Arabischen (AFA.txt), grep targum/turgem/tardschum\", \"stance\": \"silent\", \"note\": \"only 'targumisch' as a label for Targum Aramaic; Fraenkel has no entry for tarjumān among his Aramaic loans in Arabic.\"}\n     ]\n    },\n    {\n     \"id\": 3,\n     \"lang\": \"Arabic\",\n     \"words\": \"tarjama, tardjama\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Arabic ترجم tarjama 'he translated, interpreted' (verbal noun ترجمة tarjama) is a quadriliteral verb of the type faʿlala built on the borrowed noun ترجمان turjumān/tarjumān 'interpreter', which Arabic took from Aramaic/Syriac targmānā; Wiktionary puts it as \\\"Possibly from Classical Syriac ܬܰܪܓܶܡ, or possibly a back-formation from تَرْجُمَان\\\", and Klein calls the verbs of the whole family 'denominated fr. Akkad. targumanu'. The Arabic g of the Aramaic form is regularly rendered by ج (j), giving the root t-r-g-m; Dozy's spelling variants tardjemān/tardjomān/tordjomān show the unstable vowels typical of a loan. Nourai's arrow (Aramaic → Arabic verb) is right in substance; strictly the noun turjumān was borrowed first and the verb derived from it inside Arabic, which is a nuance rather than a disagreement. 'tardjama' is simply the French/Dutch transliteration of the same word, which is why Nourai lists it beside tarjama — it comes from his source Dozy.\",\n     \"derivation_fa\": \"فعل عربی «ترجم» (مصدر «ترجمة») فعلی رباعی از گونهٔ فعلَلَ است که بر پایهٔ اسم وام‌گرفتهٔ «ترجمان» ساخته شده؛ عربی این اسم را از آرامی/سریانی targmānā گرفته است. ویکی‌واژه می‌نویسد «احتمالاً از سریانی کلاسیک ܬܰܪܓܶܡ یا اشتقاق پسین از تَرجُمان» و کلاین همهٔ فعل‌های این خانواده را «مشتق از اسم اکدی targumanu» می‌داند. گ آرامی به‌قاعده به جیم عربی بدل شده و ریشهٔ چهارحرفی ت‑ر‑ج‑م پدید آمده است؛ گونه‌های آوایی که دوزی می‌آورد (tardjemān، tardjomān، tordjomān) نشانهٔ بی‌ثباتی واکه‌ها در وام‌واژه است. پیکان نورایی (آرامی ← فعل عربی) در اصل درست است، با این ظرافت که نخست اسم «ترجمان» وام گرفته شده و سپس فعل از آن ساخته شده است. «tardjama» هم صرفاً آوانگاری فرانسوی/هلندی همان واژه است که نورایی از دوزی گرفته.\",\n     \"sources\": [W_TRJM, W_DRAG, W_WPD],\n     \"ref_check\": [\n      {\"ref\": \"KLN:1573\", \"status\": \"supports\", \"note\": \"KLN_1966.txt block 835 s.v. Targum: \\\"...rel. to Aram. targem, Arab. tarjama, of s.m. All these verbs are denominated fr. Akkad. targumanu\\\".\"},\n      {\"ref\": \"DOZ:35\", \"status\": \"supports\", \"note\": \"DOZ.txt form-feed block 46 (printed = leaf − 11..13, i.e. p. 33-35; the running number '36' appears two entries later), s.v. DRAGOMAN of DROGMAN: \\\"In het Arab. tardjemān, tardjomān en tordjamān, tolk, van tardjama (ترجم), vertolken, dat de Arab. van de Joden (Chald. targeem) hebben overgenomen.\\\" — the Arabic verb, and its Jewish-Aramaic source, exactly as Nourai's arrow has it.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"LKT\", \"where\": \"Lokotsch no. 2033\", \"stance\": \"supports\", \"note\": \"\\\"Vb. targama 'dolmetschen' aus syr. targem 'erläutern', vgl. targūm 'Erläuterung, Erklärung'\\\".\"},\n      {\"src\": \"DEV\", \"where\": \"Devic, Dict. étym. des mots français d'origine orientale, s.v. Drogman (DEV.txt line 1230)\", \"stance\": \"supports\", \"note\": \"\\\"La racine sémitique du mot تَرجمان tardjamân se retrouve dans le nom de targûm qu'on donne à la paraphrase chaldaïque de la Bible et qui signifie interprétation.\\\"\"},\n      {\"src\": \"PLA\", \"where\": \"Asbaghi (grep tarǧama / turǧumān)\", \"stance\": \"silent\", \"note\": \"not listed — consistent with the word being an Aramaic, not a Persian, loan in Arabic.\"}\n     ]\n    },\n    {\n     \"id\": 4,\n     \"lang\": \"Middle Greek\",\n     \"words\": \"dragoumanos\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"Byzantine/Medieval Greek δραγομάνος, δραγουμάνος 'interpreter' was taken from the Arabic NOUN ترجمان turjumān (Klein notes the immediate model was the Egyptian pronunciation targumān), during Byzantine–Muslim diplomatic and commercial contact from about the 9th–11th c.; the changes are the voicing of the initial t- to d-, the loss of the first vowel with the resulting cluster resolved as dra-, and the Greek masculine ending -ος. Nourai's arrow runs from the Arabic VERB tarjama instead of from the noun — a small inaccuracy, since every source (Klein, AHD, Etymonline, Wiktionary, Wikipedia) derives the Greek from tarjumān/turjumān. Hence plausible rather than confirmed: the language and the direction of borrowing are right, the immediate Arabic etymon is misidentified.\",\n     \"derivation_fa\": \"یونانیِ میانه/بیزانسی δραγομάνος، δραγουμάνος «مترجم» از اسمِ عربی «ترجمان» گرفته شده است — کلاین می‌افزاید که الگوی مستقیم، تلفظ مصری targumān بوده — و این وام‌گیری در جریان روابط سیاسی و بازرگانی بیزانس با جهان اسلام از حدود سدهٔ نهم تا یازدهم میلادی رخ داده است. دگرگونی‌ها عبارت‌اند از واکدار شدن ت آغازین به د، افتادن واکهٔ نخست و ساده شدن خوشهٔ همخوانی به dra-، و افزودن پایانهٔ مذکر یونانی ‑ος. نورایی پیکان را از فعل «ترجم» کشیده است نه از اسم «ترجمان»، حال آنکه همهٔ منابع (کلاین، AHD، اتیمانلاین، ویکی‌واژه) صورت یونانی را از «ترجمان» می‌گیرند؛ از این‌رو حکم «با احتیاط پذیرفتنی» است: زبان و جهت وام‌گیری درست، ولی ریشهٔ عربیِ بی‌واسطه نادرست تعیین شده.\",\n     \"sources\": [W_ETY, W_AHD, W_DRAG, W_WPD],\n     \"ref_check\": [\n      {\"ref\": \"AHD:396\", \"status\": \"not_checked\", \"note\": \"1976 printed page unavailable; the online AHD dragoman entry gives \\\"Medieval Greek dragoumanos, from Arabic tarjumān\\\" — supporting the Greek step but from the noun, not the verb.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"p. ~479 s.v. dragoman\", \"stance\": \"partial\", \"note\": \"\\\"fr. MGk. δραγουμάνος, fr. targumān, Egypt. pronunciation of Arab. tarjumān\\\" — from the noun.\"},\n      {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century, s.v. dragoman (WEB_vol1.txt line 58842)\", \"stance\": \"partial\", \"note\": \"\\\"[Fr. dragoman; Late Gr. dragoumanos; Ar. targumān, an interpreter, from targama, to interpret]\\\" — Webster too routes the Greek through the noun targumān, though it derives that noun from the verb.\"},\n      {\"src\": \"DEV\", \"where\": \"s.v. Drogman\", \"stance\": \"supports\", \"note\": \"\\\"bas grec δραγουμάνος\\\" listed among the reflexes of Arabic tardjamân/tardjoumân.\"}\n     ]\n    },\n    {\n     \"id\": 5,\n     \"lang\": \"Latin\",\n     \"words\": \"dragumanus\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Medieval Latin dragumanus / dragumannus (also drocmandus, turchimannus) is the Latinisation of Byzantine Greek δραγουμάνος, current in the Latin of the Crusader states and of the Italian maritime republics from the 12th c., where the dragumannus was the official interpreter attached to a consul or an embassy. Nourai's bare label 'Latin' should be read as Medieval Latin — the word has nothing to do with classical Latin, which is why it is absent from Lewis-Short and from Walde-Hofmann.\",\n     \"derivation_fa\": \"صورت لاتینی میانه (قرون‌وسطایی) dragumanus/dragumannus — و نیز drocmandus و turchimannus — لاتینی‌شدهٔ δραγουμάνος یونانی بیزانسی است و از سدهٔ دوازدهم میلادی در لاتینِ دولت‌های صلیبی و جمهوری‌های دریایی ایتالیا رواج داشته، جایی که dragumannus عنوان رسمی مترجمِ وابسته به کنسول یا سفارت بوده است. برچسب «لاتین» در نمودار را باید «لاتین قرون‌وسطایی» خواند؛ این واژه با لاتین کلاسیک هیچ پیوندی ندارد و در فرهنگ‌های لاتین کلاسیک نیامده است.\",\n     \"sources\": [W_AHD, W_ETY, W_WPD],\n     \"ref_check\": [\n      {\"ref\": \"AHD:396\", \"status\": \"not_checked\", \"note\": \"printed page unavailable; online AHD has \\\"from Medieval Latin dragumannus\\\", confirming the step and specifying that it is Medieval, not classical, Latin.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"DEV\", \"where\": \"s.v. Drogman\", \"stance\": \"supports\", \"note\": \"\\\"bas lat. dragumanus, drocmandus, turchimannus\\\" — 'bas latin' = Medieval Latin, exactly this node.\"},\n      {\"src\": \"LEW\", \"where\": \"Walde-Hofmann, Lateinisches etym. Wörterbuch (LEW_1910.txt)\", \"stance\": \"silent\", \"note\": \"no entry — as expected for a medieval borrowing, which supports reading Nourai's 'Latin' as Medieval Latin.\"},\n      {\"src\": \"LKT\", \"where\": \"Lokotsch no. 2033\", \"stance\": \"supports\", \"note\": \"lists the Romance chain it. dragomanno, turcimanno, prov. drogoman, frz. drogoman, drogman, trucheman etc. all under the one Arabic etymon.\"}\n     ]\n    },\n    {\n     \"id\": 6,\n     \"lang\": \"Old French\",\n     \"words\": \"drugeman\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Old French drugeman / drughemant / drugement 'interpreter' (12th–13th c.; Villehardouin has drugemant early in the 13th c.) continues Medieval Latin dragumanus with the usual Old French reduction of the unstressed medial vowel and -anus > -an. The same Arabic word reached French a second time by another road, giving trucheman / truchement (15th c., via Italian turcimanno with its folk-etymological link to turco), so French ended up with a doublet.\",\n     \"derivation_fa\": \"فرانسوی کهن drugeman/drughemant/drugement «مترجم» (سده‌های دوازدهم و سیزدهم؛ ویلاردوئن در آغاز سدهٔ سیزدهم drugemant دارد) دنبالهٔ dragumanus لاتین قرون‌وسطایی است، با کاهش معمول واکهٔ بی‌تکیهٔ میانی و تبدیل ‑anus به ‑an. همین واژهٔ عربی بار دیگر از راهی دیگر به فرانسوی رسید و trucheman/truchement (سدهٔ پانزدهم، از راه ایتالیایی turcimanno که با turco «ترک» ریشه‌شناسی عامیانه شده بود) را پدید آورد؛ چنین است که فرانسوی دو صورت دوگانه از یک واژه دارد.\",\n     \"sources\": [W_ETY, W_AHD, W_DRAG],\n     \"ref_check\": [\n      {\"ref\": \"AHD:396\", \"status\": \"not_checked\", \"note\": \"printed page unavailable; online AHD: \\\"from Old French drugeman\\\" — the exact form Nourai prints.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"DEV\", \"where\": \"s.v. Drogman (DEV.txt line 1230)\", \"stance\": \"supports\", \"note\": \"\\\"vieux français (XIIe et XIIIe siècles) drughemant, drugement; on a dit truchement dès le XVe siècle.\\\"\"},\n      {\"src\": \"HJB\", \"where\": \"s.v. DRUGGERMAN (HJB.txt line 9034)\", \"stance\": \"supports\", \"note\": \"\\\"Villehardouin, early in the 13th century, [has] drugemant\\\".\"},\n      {\"src\": \"PHN\", \"where\": \"Pihan, s.v. DROGMAN (PHN.txt line 4433)\", \"stance\": \"supports\", \"note\": \"treats drogman with the variants trucheman/truchement as one Arabic-derived family in French.\"}\n     ]\n    },\n    {\n     \"id\": 7,\n     \"lang\": \"English\",\n     \"words\": \"dragoman\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"English dragoman 'interpreter and guide in Arabic-, Turkish- or Persian-speaking countries' entered from Old French drugeman about 1300 (Middle English dragman, drugeman); Etymonline dates it c. 1300 and Pegolotti's Handbook (c. 1343) already uses 'dragomans' of the interpreters hired at Tana. The later spelling with -o- follows the Italian/Byzantine forms. English then reanalysed the final syllable as the noun man, producing the folk-etymological plural dragomen beside the correct dragomans — a good example of reinterpretation of a loanword, and the reason Skeat files the word under 'Drayman'.\",\n     \"derivation_fa\": \"واژهٔ انگلیسی dragoman «مترجم و راهنما در سرزمین‌های عربی‌زبان، ترکی‌زبان و فارسی‌زبان» حدود سال ۱۳۰۰ میلادی از فرانسوی کهن drugeman وارد انگلیسی شد (انگلیسی میانه dragman، drugeman)؛ اتیمانلاین تاریخ آن را حدود ۱۳۰۰ می‌داند و در «راهنمای» پگولوتی (حدود ۱۳۴۳) صورت جمع dragomans برای مترجمانی که در تانا اجیر می‌شدند به کار رفته است. املای متأخر با o از صورت‌های ایتالیایی و بیزانسی گرفته شده. سپس انگلیسی‌زبانان هجای پایانی را با واژهٔ man «مرد» یکی گرفتند و جمع عامیانهٔ dragomen در کنار جمع درست dragomans پدید آمد — نمونه‌ای روشن از ریشه‌شناسی عامیانه در وام‌واژه‌ها.\",\n     \"sources\": [W_ETY, W_DRAG, W_AHD],\n     \"ref_check\": [\n      {\"ref\": \"AHD:396\", \"status\": \"not_checked\", \"note\": \"printed page unavailable; the online AHD entry defines dragoman as \\\"An interpreter or guide in countries where Arabic, Turkish, or Persian is spoken\\\" and gives the ME dragman < OF drugeman route — Nourai's gloss and arrow.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"p. ~479 s.v. dragoman\", \"stance\": \"supports\", \"note\": \"\\\"dragoman, n., guide and interpreter. — F. dragoman, drogman, fr. It. dragomano, fr. MGk. δραγουμάνος ...\\\"\"},\n      {\"src\": \"SKT\", \"where\": \"Skeat, s.v. Drayman [= Dragoman] (SKT.txt line 5380)\", \"stance\": \"supports\", \"note\": \"\\\"an interpreter. (Span. — Gk. — Arab.) Span. dragoman. — Late Gk. δραγουμάνος, an interpreter. — Arab. tarjumān, an interpreter, translator; see Targum.\\\" — same chain, Spanish rather than French as the immediate donor.\"},\n      {\"src\": \"WEB\", \"where\": \"Webster's, s.v. dragoman\", \"stance\": \"supports\", \"note\": \"\\\"drag'o-man, n.; pl. drag'o-mans, drag'o-men ... in the Near East, an interpreter or traveler's guide\\\" — records the folk-etymological plural.\"},\n      {\"src\": \"HJB\", \"where\": \"s.v. DRUGGERMAN\", \"stance\": \"supports\", \"note\": \"\\\"Neither this word for an 'interpreter,' nor the Levantine dragoman, of which it was a quaint old English corruption, is used in Anglo-Indian colloquial\\\".\"}\n     ]\n    },\n    {\n     \"id\": 8,\n     \"lang\": \"Persian\",\n     \"words\": \"tarjomeh; motarjem; tarjom\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"ترجمه tarjome 'translation' is the Arabic verbal noun tarjama of the quadriliteral verb ترجم, borrowed into New Persian with the regular Persian reading of final -a(t) as -e; مترجم motarjem 'translator' is the Arabic active participle mutarjim of the same verb (Persian broken plural تراجم tarājem is also used). Both are therefore Arabic loans in Persian, and since the Arabic verb itself rests on Aramaic targmānā < Akkadian targumannu, Nourai's placing of them under the Akkadian root is correct — there is no Persian element anywhere in the chain, and this is NOT one of his Persian→Arabic→Persian round trips. The third item is the weak one: 'tarjom «ترجم (ترجمان)» : speech, statement'. Bare ترجم is the Arabic verb stem, not a Persian noun meaning 'speech'; the sense and the Rumi line Nourai quotes (صد هزاران ترجمان خیزد ز دل, 'a hundred thousand interpreters rise from the heart') belong to ترجمان tarjomān 'interpreter, spokesman', which is why the book itself puts (ترجمان) in brackets. Read as ترجمان the word and gloss are right; read as ترجم they are not.\",\n     \"derivation_fa\": \"«ترجمه» مصدرِ عربیِ فعل رباعی «ترجم» است که با خوانش معمول تای پایانی به «ـه» وارد فارسی نو شده، و «مترجم» اسم فاعل باب تفعّل‌گونهٔ همان فعل (مُتَرجِم) است؛ جمع مکسر «تراجم» نیز در فارسی به کار می‌رود. هر دو وام‌واژهٔ عربی‌اند و چون خود فعل عربی بر آرامی targmānā و آن بر اکدی targumannu استوار است، جای دادن آنها زیر ریشهٔ اکدی درست است؛ توجه شود که این زنجیره هیچ عنصر فارسی ندارد و از گونهٔ «فارسی ← عربی ← فارسی» نیست. اما مورد سوم سست است: «ترجم» تنها ستاک فعل عربی است و در فارسی اسمی به معنی «سخن، گفتار» نیست؛ این معنی و بیت مولوی که نورایی آورده («صد هزاران ترجمان خیزد ز دل») از آنِ «ترجمان» است، چنان‌که خود کتاب هم (ترجمان) را در کمانک آورده است.\",\n     \"sources\": [W_PTRJ, W_TRJM],\n     \"ref_check\": [\n      {\"ref\": \"MON:1064\", \"status\": \"not_checked\", \"note\": \"Moʿin's 6-volume Farhang-e Fārsi is not online in any form (refs_online.json: only the 2-vol Adena abridgement exists, with different pagination), so page 1064 cannot be verified; the abridgement's ت‑ر‑ج block does carry ترجمه and تراجم («تراجم: [ع.] (مص م.) ج. ترجمه»), consistent with the claim.\"},\n      {\"ref\": \"SOR:37\", \"status\": \"not_checked\", \"note\": \"SOR (K. Akhavan Zanjani) is unidentified — refs_online.json: 'Table IV entry for SOR lost in OCR ... none online; title unidentified'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"MON\", \"where\": \"MON_part1.txt line 39467 (ت‑ر‑ا block)\", \"stance\": \"supports\", \"note\": \"«تراجم: [ع.] (مص م.) ج. ترجمه» — Moʿin tags the family [ع.], i.e. Arabic, matching the Arabic-loan analysis.\"},\n      {\"src\": \"RCH\", \"where\": \"Richardson, Persian-Arabic-English Dictionary (RCH.txt line 23293)\", \"stance\": \"supports\", \"note\": \"\\\"A. tarjamah or tarjumah, Interpretation, translation.\\\" — the 'A.' marks it as Arabic in a Persian dictionary.\"},\n      {\"src\": \"LKT\", \"where\": \"Lokotsch no. 2033\", \"stance\": \"supports\", \"note\": \"gives targama/targumān as the Arabic base from which all the Eastern and European forms come; Persian is one of the recipients.\"}\n     ]\n    },\n    {\n     \"id\": 9,\n     \"lang\": \"Hebrew\",\n     \"words\": \"targum\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Mishnaic Hebrew תרגום targum 'interpretation, translation', specifically the Aramaic rendering of Scripture recited in the synagogue after the Hebrew reading, is the verbal noun of Hebrew tirgem 'he interpreted, translated' — itself a denominative of the same borrowed Aramaic stem targem / targəmānā that node #2 describes; the synagogue functionary who delivered it was the meturgeman (Aramaic məthurgəmān). So the Hebrew word is not an independent creation but the Hebrew end of the Aramaic branch, exactly as Nourai's arrow from the Aramaic node has it. Zimmern likewise lists 'neuhebr. targūm Übersetzung, \\\"Targum\\\"' as a further development of the Akkadian word.\",\n     \"derivation_fa\": \"«תרגום» (targum) در عبری میشنایی به معنی «تفسیر، ترجمه» و به‌ویژه برگردان آرامی کتاب مقدس است که در کنیسه پس از قرائت عبری خوانده می‌شد. این واژه مصدرِ فعل عبری tirgem «ترجمه کرد» است و آن خود از همان ستاک آرامیِ وام‌گرفتهٔ targem/targəmānā ساخته شده که در گرهٔ ۲ آمد؛ کارگزارِ کنیسه که این برگردان را می‌خواند «مِتورگِمان» (آرامی məthurgəmān) نام داشت. پس واژهٔ عبری آفرینش مستقلی نیست بلکه شاخهٔ عبریِ همان مسیر آرامی است و پیکان نورایی درست است. تسیمرن نیز «targūm عبری نو» را دنبالهٔ همان واژهٔ اکدی می‌شمارد.\",\n     \"sources\": [W_TGM, W_DRAG],\n     \"ref_check\": [\n      {\"ref\": \"KLN:1573\", \"status\": \"supports\", \"note\": \"KLN_1966.txt block 835: \\\"Targum, n., Aramaic translation of the Bible. — Mishnaic Heb. targum, 'interpretation, translation', fr. Heb. tirgem, 'he interpreted, translated', which is rel. to Aram. targem, Arab. tarjama ... All these verbs are denominated fr. Akkad. targumanu.\\\"\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"AKD\", \"where\": \"Zimmern p. 26\", \"stance\": \"supports\", \"note\": \"\\\"dazu neuhebr. targūm Übersetzung, 'Targum'\\\" — appended directly to the Akkadian/Aramaic entry.\"},\n      {\"src\": \"SKT\", \"where\": \"Skeat s.v. Targum (SKT.txt line 19201)\", \"stance\": \"partial\", \"note\": \"\\\"Targum, a Chaldee paraphrase of the Old Testament (Chaldee.) Chaldee targūm, an interpretation. — Chald. targem, to interpret. Cf. Arab. tarjumān, an interpreter; see Dragoman.\\\" — Skeat labels the immediate source Aramaic ('Chaldee') rather than Hebrew, i.e. the Aramaic step of Nourai's chart.\"},\n      {\"src\": \"DEV\", \"where\": \"s.v. Drogman\", \"stance\": \"supports\", \"note\": \"\\\"La racine sémitique du mot tardjamân se retrouve dans le nom de targûm ... et qui signifie interprétation.\\\"\"}\n     ]\n    },\n    {\n     \"id\": 10,\n     \"lang\": \"English\",\n     \"words\": \"Targum; Targumist\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"English Targum (pl. Targums or, with the Hebrew plural, Targumim) 'an Aramaic translation or paraphrase of a part of the Hebrew Bible' is a learned 16th-century borrowing of Mishnaic Hebrew targum, taken over by Christian Hebraists with the rise of rabbinic studies in Europe (the Targums were printed in the Complutensian and the Antwerp Polyglots); Targumist 'writer of, or scholar of, a Targum' is the same noun plus the English agent suffix -ist, and Targumic is the adjective. No sound change is involved — the word is taken over unaltered, capitalised as a title.\",\n     \"derivation_fa\": \"واژهٔ انگلیسی Targum (جمع Targums یا با جمع عبری Targumim) «ترجمه یا تفسیر آرامی بخشی از کتاب مقدس عبری» وام‌واژه‌ای عالمانه از عبریِ میشنایی targum است که در سدهٔ شانزدهم میلادی، با رونق گرفتن عبری‌پژوهی در اروپا و چاپ ترگوم‌ها در کتاب مقدس‌های چندزبانه (کمپلوتنسی و آنتورپ)، وارد انگلیسی شد. Targumist از همان اسم با پسوند فاعلی انگلیسی ‑ist ساخته شده و صفت آن Targumic است. هیچ دگرگونی آوایی در کار نیست و واژه دست‌نخورده و با حرف بزرگ آغازین به انگلیسی رفته است.\",\n     \"sources\": [W_TGM],\n     \"ref_check\": [\n      {\"ref\": \"KLN:1573\", \"status\": \"supports\", \"note\": \"KLN_1966.txt block 835: \\\"Derivatives: Targum-ic, adj., Targumist (q.v.)\\\" and the next entry \\\"Targumist, n., 1) writer of a Targum; 2) student of the Targums. — Formed fr. Targum with suff. -ist.\\\" — both of Nourai's words, with his glosses.\"},\n      {\"ref\": \"AHD:1316\", \"status\": \"not_checked\", \"note\": \"page 1316 of the 1976 New College Edition (the main dictionary); that edition is lending-only on archive.org and the local AHD file is the IE-roots appendix only. The word and sense are independently confirmed by Klein and Wiktionary.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"SKT\", \"where\": \"Skeat s.v. Targum\", \"stance\": \"supports\", \"note\": \"\\\"Targum, a Chaldee paraphrase of the Old Testament\\\" — the English word with Nourai's gloss.\"},\n      {\"src\": \"KLN\", \"where\": \"p. 1573 s.v. Targum, Targumist\", \"stance\": \"supports\", \"note\": \"as quoted in ref_check.\"},\n      {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls (FSD_vol1-4), grep Targum\", \"stance\": \"silent\", \"note\": \"no usable hit retrieved from the OCR for the Targum headword.\"}\n     ]\n    }\n   ]\n  }\n ]\n}\n\nwith open(\"/home/sfmqrb/git/rishe/data/verification/page-414.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(data, f, ensure_ascii=False, indent=1)\nprint(\"written\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-414.py && python3 -m json.tool data/verification/page-414.json > /dev/null && echo \"valid json\" && python3 tools/verify_check.py 414"
}
```


### [2026-09-14T01:23:21.666Z] TOOL RESULT

```
written
valid json
nodes verified: 14/14
node verdicts: {'plausible': 5, 'confirmed': 8, 'transcription_suspect': 1}
root verdicts: {'confirmed': 2}
ref checks: {'partial': 1, 'not_checked': 13, 'supports': 6}
books consulted: {'partial': 5, 'silent': 11, 'supports': 27, 'contradicts': 1} | by book: {'DEV': 5, 'MON': 4, 'HJB': 4, 'LKT': 4, 'KLN': 4, 'AKD': 3, 'SKT': 3, 'BQT': 2, 'AFM': 2, 'PLA': 2, 'WEB': 2, 'HUB': 1, 'HRN': 1, 'ARB': 1, 'KNT': 1, 'AFA': 1, 'LEW': 1, 'PHN': 1, 'RCH': 1, 'FSD': 1}
```


## [2026-09-14T01:23:40.812Z] AGENT

Done — `data/verification/page-414.json` written, valid JSON, `verify_check.py 414` shows **0 PROBLEM lines** (14/14 nodes).

**Page 414 (book p. 384) — verdicts**
- Roots: 2 confirmed (`Ragâ/Rağâ`, `Ragâmu`); 1 redirect skipped.
- Nodes: 8 confirmed, 5 plausible, 1 transcription_suspect, 0 disputed.

**Flagged items**
- `Ragâ` #4 [Greek] **Râzex; râzakěne** — transcription_suspect, `error_in: book`. No Greek form with -z- exists; the attested names are Ῥάγαι / Ῥάγης (Kent s.v. *Raga-*: "Gk. Ῥάγης"), Latin Rhagae, district Ῥαγιανή. The printed page shows exactly "Râzex"/"râzakěne", so the extraction is faithful; likely Nourai re-transliterating Moʿin's Persian-script Greek and reading گ as ز. Page PNG saved to `data/verification/sources/refs/ocr/BOOK/414.png`.
- `Ragâ` #1 **râzegî** (plausible): unattested — not in Moʿin, Borhān or Dehkhodā (Nourai's own note says so); Ray and rāzī are solid.
- `Ragâmu` #1 **Targumânu** (plausible): Klein/AHD/Zimmern derive it from *ragāmu*, but Wiktionary calls the origin unknown and many take it as a Hittite/Luwian *tarkummāi-* loan; also the standard form has geminate -nn-.
- `Ragâmu` #4 **dragoumanos** (plausible): all sources derive Greek from the *noun* tarjumān, not from the verb tarjama as the chart draws.
- `Ragâmu` #8 **tarjom** (plausible): bare ترجم isn't a Persian noun "speech"; the sense and the Rumi line belong to ترجمان (the book itself brackets it).

**Ref checks**: KLN:1573 verified in the local scan (block 835 = printed pp. 1573/74, s.v. *Targum* — states Nourai's whole tree verbatim); DOZ:35 verified (leaf 46, s.v. DRAGOMAN); BQT:985 partial (ری entry at printed ≈987, Ray/رازی folk legend, no grape). Not checkable: MON5:636, MON:1064 (6-vol Moʿin has no scan anywhere), FVF:278 (Emām Šuštarī, login-only), SOR:37 (title unidentified), AHD:396/1316 (1976 New College pages, lending-only — but the online AHD entry confirms the whole dragoman chain). Best independent find: **Addī Šīr (AFM, leaf 73)** derives Arabic الرازقي «من رازی» citing Borhān — supports Nourai's Ray→Arabic grape arrow, a reference he does not cite.

**No extraction errors** in the word forms. One structural note for the owner: on the printed page `Targumânu` sits *inside* the Akkadian root box next to `Ragâmu`; the JSON promotes it to node #1 with parent #0. That's a normalisation, not a misread, but worth knowing if root boxes with two words are handled elsewhere.

11 web sources archived via `fetch_source.py`.
