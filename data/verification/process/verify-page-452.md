# Verification process log — verify-page-452


## [2026-09-14T01:56:16.003Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 452 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-452.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-452.json. Write /home/sfmqrb/git/rishe/data/verification/page-452.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 452` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T01:56:17.079Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T01:56:17.946Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T01:56:17.963Z] TOOL RESULT

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


## [2026-09-14T01:56:18.430Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-452.txt"
}
```


### [2026-09-14T01:56:18.458Z] TOOL RESULT

```
1	=== PDF page 452 (book page 422) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Skand, Skend, Sqand, Kand 2 : to climb, leap  (refs WLD:540; AHD:1539)
4	#1 (parent #0) [Indo-European] refs=None | Skand-slâ : step, ladder
5	#2 (parent #0) [Latin] refs=WLD:540 | scandere : to climb ; scâlae : step, ladder
6	  #3 (parent #2) [Italian] refs=None | scalo : ladder, platform, wharf
7	    #4 (parent #3) [Arabic] refs=TAD:4 | eskeleh : ladder, wharf
8	      #5 (parent #4) [Persian] refs=MON:271 | eskeleh «اسکله» : wharf
9	  #6 (parent #2) [French] refs=None | ascenseur : elevator ; eschelle : ladder
10	    #7 (parent #6) [Persian] refs=MON:51,288 | âsânsor «آسانسور» : elevator ; ešel «اشل» : scale
11	  #8 (parent #2) [English] refs=AHD | scan, ascend, descend, escalator, scale
12	#9 (parent #0) [Sanskrit] refs=WLD:540 | skandati : jumps, speeds
13	#10 (parent #0) [Greek] refs=WLD:540 | skandalon : stumbling block, trap
14	  #11 (parent #10) [English] refs=AHD | scandal
15	--- entry 1 ---
16	ROOT Skand-slâ -> redirect to Skand
17	--- entry 2 ---
18	ROOT Skarna -> redirect to Sukurna
19	--- entry 3 ---
20	ROOT Sked 1 -> redirect to Sek
21	--- entry 4 ---
22	ROOT [Indo-European] Sked 2 : to cover  (refs POK:919)
23	#1 (parent #0) [Sanskrit] refs=POK:919 | čadaiti : to cover ; čattra : cover, umbrella
24	  #2 (parent #1) [Persian] refs=BQT:609,622 | čâdor «چادر» : veil ; čatr «چتر» : umbrella
25	#3 (parent #0) [Avestan] refs=POK:919 | sâdayantî : an article of clothing
26	  #4 (parent #3) [None] refs=None | 
27	--- entry 5 ---
28	ROOT Skei -> redirect to Sek
29	--- entry 6 ---
30	ROOT Skěl -> redirect to Sek
31	
```


## [2026-09-14T01:56:21.650Z] TOOL CALL #3: Bash

```json
{
 "command": "python3 -m json.tool data/extracted/batch/page-452.json | head -200",
 "description": "Read source JSON for page 452"
}
```


### [2026-09-14T01:56:22.748Z] TOOL RESULT

```
{
    "pdf_page": 452,
    "book_page": 422,
    "entries": [
        {
            "root": {
                "name": "Skand, Skend, Sqand, Kand 2",
                "lang": "Indo-European",
                "refs": "WLD:540; AHD:1539",
                "gloss": "to climb, leap"
            },
            "nodes": [
                {
                    "id": 1,
                    "parent": 0,
                    "lang": "Indo-European",
                    "refs": null,
                    "words": [
                        {
                            "translit": "Skand-sl\u00e2",
                            "gloss": "step, ladder",
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 2,
                    "parent": 0,
                    "lang": "Latin",
                    "refs": "WLD:540",
                    "words": [
                        {
                            "translit": "scandere",
                            "gloss": "to climb",
                            "script": null
                        },
                        {
                            "translit": "sc\u00e2lae",
                            "gloss": "step, ladder",
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
                    "lang": "Italian",
                    "refs": null,
                    "words": [
                        {
                            "translit": "scalo",
                            "gloss": "ladder, platform, wharf",
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
                    "lang": "Arabic",
                    "refs": "TAD:4",
                    "words": [
                        {
                            "translit": "eskeleh",
                            "gloss": "ladder, wharf",
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
                    "lang": "Persian",
                    "refs": "MON:271",
                    "words": [
                        {
                            "translit": "eskeleh",
                            "gloss": "wharf",
                            "script": "\u0627\u0633\u06a9\u0644\u0647"
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 6,
                    "parent": 2,
                    "lang": "French",
                    "refs": null,
                    "words": [
                        {
                            "translit": "ascenseur",
                            "gloss": "elevator",
                            "script": null
                        },
                        {
                            "translit": "eschelle",
                            "gloss": "ladder",
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
                    "lang": "Persian",
                    "refs": "MON:51,288",
                    "words": [
                        {
                            "translit": "\u00e2s\u00e2nsor",
                            "gloss": "elevator",
                            "script": "\u0622\u0633\u0627\u0646\u0633\u0648\u0631"
                        },
                        {
                            "translit": "e\u0161el",
                            "gloss": "scale",
                            "script": "\u0627\u0634\u0644"
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 8,
                    "parent": 2,
                    "lang": "English",
                    "refs": "AHD",
                    "words": [
                        {
                            "translit": "scan, ascend, descend, escalator, scale",
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
                    "lang": "Sanskrit",
                    "refs": "WLD:540",
                    "words": [
                        {
                            "translit": "skandati",
                            "gloss": "jumps, speeds",
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 10,
                    "parent": 0,
                    "lang": "Greek",
                    "refs": "WLD:540",
                    "words": [
                        {
                            "translit": "skandalon",
                            "gloss": "stumbling block, trap",
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 11,
                    "parent": 10,
                    "lang": "English",
                    "refs": "AHD",
                    "words": [
                        {
                            "translit": "scandal",
                            "gloss": null,
                            "script": null
                        }
                    ],
                    "script_extra": null,
```


## [2026-09-14T01:56:24.149Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['WLD','AHD','POK','TAD','MON','BQT','KLN','HRN','HUB','PHD','NYB','BRT','SKT','IEC','SYN','ARY','PLA','AFM','FVQ','LKT','WEB','FSD','DEV','PHN']:\n    v=d.get(k)\n    print(k, json.dumps(v,ensure_ascii=False)[:400])\n\""
}
```


### [2026-09-14T01:56:25.561Z] TOOL RESULT

```
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
TAD {"title": "Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-hurufihi (2nd ed. Cairo 1932, ed. Yusuf Tuma al-Bustani; later Library of Lebanon reprint) — Nourai lists it under Arabic authors ('Unaysi T.'); its Table IV line was lost in the OCR", "kind": "archive_djvu", "url": "https://archive.org/details/TOB1932ARAR (1932 ed.); also https://a
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/
AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_page
FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.t
LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 =
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
DEV {"title": "L. M. Devic, Dictionnaire étymologique des mots français d'origine orientale, Paris 1876", "edition_found": "1876", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairety00devi", "identifier": "dictionnairety00devi (also dictionnairetym02devigoog, fr105comparative41)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/DEV.txt", "page_offset": "leaf
PHN {"title": "A. P. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du turc, Paris 1866", "edition_found": "1866", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairetym01pihagoog", "identifier": "dictionnairetym01pihagoog (others: bub_gb_QnsSAAAAIAAJ, dictionnairetym00pihagoog)", "local_file": "/home/sfmqrb/git/rishe/data/verific
```


## [2026-09-14T01:56:30.517Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -m json.tool data/extracted/batch/page-452.json | sed -n '200,400p'"
}
```


### [2026-09-14T01:56:31.562Z] TOOL RESULT

```
                    "script_extra": null,
                    "note": null,
                    "quote": null
                }
            ]
        },
        {
            "root": {
                "name": "Skand-sl\u00e2",
                "redirect": "Skand"
            },
            "nodes": []
        },
        {
            "root": {
                "name": "Skarna",
                "redirect": "Sukurna"
            },
            "nodes": []
        },
        {
            "root": {
                "name": "Sked 1",
                "redirect": "Sek"
            },
            "nodes": []
        },
        {
            "root": {
                "name": "Sked 2",
                "lang": "Indo-European",
                "refs": "POK:919",
                "gloss": "to cover"
            },
            "nodes": [
                {
                    "id": 1,
                    "parent": 0,
                    "lang": "Sanskrit",
                    "refs": "POK:919",
                    "words": [
                        {
                            "translit": "\u010dadaiti",
                            "gloss": "to cover",
                            "script": null
                        },
                        {
                            "translit": "\u010dattra",
                            "gloss": "cover, umbrella",
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
                    "refs": "BQT:609,622",
                    "words": [
                        {
                            "translit": "\u010d\u00e2dor",
                            "gloss": "veil",
                            "script": "\u0686\u0627\u062f\u0631"
                        },
                        {
                            "translit": "\u010datr",
                            "gloss": "umbrella",
                            "script": "\u0686\u062a\u0631"
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 3,
                    "parent": 0,
                    "lang": "Avestan",
                    "refs": "POK:919",
                    "words": [
                        {
                            "translit": "s\u00e2dayant\u00ee",
                            "gloss": "an article of clothing",
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
                    "lang": null,
                    "refs": null,
                    "words": [],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                }
            ]
        },
        {
            "root": {
                "name": "Skei",
                "redirect": "Sek"
            },
            "nodes": []
        },
        {
            "root": {
                "name": "Sk\u011bl",
                "redirect": "Sek"
            },
            "nodes": []
        }
    ]
}
```


## [2026-09-14T01:56:31.705Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['WLD','AHD','POK','TAD','MON','BQT']:\n    print('=====',k)\n    print(json.dumps(d[k],ensure_ascii=False,indent=1))\n\""
}
```


### [2026-09-14T01:56:32.827Z] TOOL RESULT

```
===== WLD
{
 "title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32",
 "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.39015066210397 (browser only from this host)",
 "identifier": "in.gov.ignca.20339 (Band 3); also in.ernet.dli.2015.106625 (Band 3 duplicate)",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt"
 ],
 "page_offset": "Band 3: leaf = printed + 6. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696).",
 "lookup_hint": "Band 3 is the index (Wortregister by language) - it maps a word to 'Band, page' in vols 1-2, so it can at least confirm that a word is treated at the cited WP volume/page. For the actual entry text, use Pokorny 1959 (POK), whose entries cite 'WP. I 177' etc. and are essentially a revision of WP.",
 "notes": "Tried IA (several queries), Google Books API (quota exceeded / not full view), HathiTrust (blocks automated access, 403). Band 2 (1927) is US public domain; Band 1 (1930) became US PD in 2026, so HathiTrust full view may exist - check manually at https://catalog.hathitrust.org/Search/Home?lookfor=walde+pokorny+vergleichendes. || UPDATE 2026-09: Bände I and II obtained in full from the Digital Library of India scans on archive.org (open, OCR layer in the _text.pdf).",
 "cites": "volume (WLD1 / WLD2) and page of Walde–Pokorny"
}
===== AHD
{
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
===== POK
{
 "title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)",
 "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/indogermanisches01pokouoft",
 "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt",
 "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\\data\\ie\\pokorny&root=config",
 "notes": "Nourai's page numbers are Band I 1959 pages, which match these scans. Band II (1969 index) is at pokorny-indogermanisches-etymologisches-worterbuch-band-ii-1969 (djvu 200). local_files: /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt (pp. 1-348), /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_02.txt (pp. 349-770), /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_03.txt (pp. 771-1183); /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_full.txt (unpaginated database text with 'Page(s): N' per root)",
 "local_files": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_02.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_03.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_full.txt"
 ],
 "cites": "page number of Pokorny, Indogermanisches etymologisches Wörterbuch, Band I (1959)"
}
===== TAD
{
 "title": "Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-hurufihi (2nd ed. Cairo 1932, ed. Yusuf Tuma al-Bustani; later Library of Lebanon reprint) — Nourai lists it under Arabic authors ('Unaysi T.'); its Table IV line was lost in the OCR",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/TOB1932ARAR (1932 ed.); also https://archive.org/details/ar113lang79 and https://archive.org/details/elshandawily14640",
 "lookup_hint": "Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; inside.php search works.",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD.txt"
 ],
 "page_offset": "86 leaves (small book, ~80 printed pages); offset ≈ leaf − 4..6, verify against the printed numeral on the page image",
 "covers_etymology": true,
 "notes": "Arabic OCR fair. Nourai's exact edition unknown; the Beirut reprint reproduces the 1932 pagination."
}
===== MON
{
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
===== BQT
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


## [2026-09-14T01:57:04.563Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"lemma: .*skand\\|lemma: .*skend\\|lemma: .*sqand\" POK_full.txt | head -20; echo ---; grep -n \"Page(s): 919\\|Page(s): 929\\|Page(s): 930\" POK_full.txt | head -20"
}
```


### [2026-09-14T01:57:04.648Z] TOOL RESULT

```
43488:Root/ lemma: kand-, skand- and (Old Indie) (s)kend- 
43495:Root / lemma: kand- skand-and (Old Indie) (s)kend-\ "to glow; bright, *moon' derived 
75442:Root / lemma: skend^- 
---
75455:Page(s): 930 
75493:Page(s): 929-930 
75527:Page(s): 930 
75542:Page(s): 930 
77196:Page(s): 919-922 
77326:Page(s): 930-933 
77545:Page(s): 929 
77777:Page(s): 929 
77801:Page(s): 929
```


## [2026-09-14T01:57:06.214Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport re\nt=open('POK_full.txt',encoding='utf-8',errors='replace').read()\nblocks=t.split('Root / lemma:')\nfor b in blocks:\n    if re.search(r'Page\\(s\\):\\s*(919|929|930)\\b',b):\n        print('Root / lemma:'+b[:1200])\n        print('==========')\nEOF"
}
```


### [2026-09-14T01:57:07.464Z] TOOL RESULT

```
Root / lemma: skend^- 

Meaning: to plunge 

Note: only gr. and Baltic 

Material: Gr. okivGoc; "untertauchend'; Lithuanian sk^stu, 5/r#5//"untersinken, drown ', 

causative skandinu, -dinti^ drown '; Old Prussian auskiendlai^er qo under'. 

Maybe alb. {^skendh-) /7eo'/7 'plunge, throw' [common alb. sk- > h-]. 

References: WP. II 565, Trautmann 265. 
Page(s): 930 


==========
Root / lemma: (s)ken-(d-) 

Meaning: to rift; to flay 

Note: probably extension from seAr-'cut, clip'; only Celtic under german. 

Material: A. Bret, s/ra/?/ collective "Schuppen' {*sknto-), abret. anscantocionP\. 

"insquamosos', cymr. ys^y/^/i/'Schnitzen' {* sken-tr-)\ 

Old Icelandic skinnu. "skin, fell, fur' {*sken-to-, proto Germanic *skinl=>a-, compare lapp. 
loanword sk/dde and runisch ski[n]t^a-leubaR, Old English scinn, (under the influence of 
common Celtic -ns-, -nt- > -nn-), engl. sk/n6s. is loanword from Nord., also Middle Low 
German schin^a kind of russisches Ledergeld'), Middle High German schinti. " fruit bowl ', 
Modern High German Schind-mahre, -aas, Dutch dial. sch/nde'sk\n, fell, fur; bast, bark', 
abgel. verb Old Saxon b/sc/nd/an ^abnnden, peel ', Old High German scinten. Middle High 
German Middle Low Germansc/7/>7o'e/7"enthauten, auspliJndern, maltreat' (Modern High 
German sch/nden stem V.); Old Icelandic skant " bark ', nisi, also 'Hautchen', Middle Low 
German sc/7//7 'dandruff in Haar' (out of it Modern High German Schinn, Schinne), (under 
the influence of common Celtic -ns-, -nt- > -nn-), Middle Dutch sc/7e/7e"thin skin, bast'; 

B. besides Indo Germanic (s)kend-\
==========
Root / lemma: (s)keng- 

Meaning: lame; slant 

Material: Old Indie sakthi- n. (= Avestan haxti-) " thigh ' ( *skak-thi-, Indo Germanic *skng-ti- 

; das -th'h after Old Indie asth'h "bone', above S. 783); /r/75/ya//"hinkt' (Middle Indie for 

*skanj-), /r/75/^5-"hinkend', khanjana^m. " wagtail '; 

gr. OKa^oj (only present and Imp.) " limp ' {*skng^id)\ Middle Irish 5C//7^//77 "spring' is 
probably reshuffling from Old Irish sce/7o'- "spring' (see be\o\N ghengh-^ march, step, 
stride, strut'); 

Old Icelandic s/r5AAr"hinkend, slant, skew', Swedish dial, sk/nka' limp '; without ani. s-: 
Old High German hinkan^ limp ', Denomin. Middle High German hanken6s.\ 

Germanic *skanka-\n Norwegian skonk, skanki. " thigh, shinbone'. Old English scanca 
f. " shank, leg, shin bone ', Middle Low German schenke^ thigh ' (Demin. Middle High 
German Modern High German SchenkeF thigh '), ablaut. Old High German scinker thigh 
', scinchorw., scincai. "Beinrohre, thigh ', Modern High German Schinken, on the other 
hand Old Frisian skunka. Modern High German Dialectal schunke {* skng-) ds.; without s- 
Middle High German hanke' thigh, hip, haunch', Tirol HenkeF thigh '; also Late Middle 
High German schankm. " rac
==========
Root / lemma: (s)kep-1 

Meaning: to cover 

Note: only gr. and Balto-Slavic 



Material: Gr. oKsnaq, -aoq n. 'cover, sleeve, wrapping, shelter', Ionian Attic aKsirn f. 
"cover, protection, shelter', OKsna^u), GKETrau), OKsnu) "bedecke, verhijlle, schijtze'; 
Lithuanian kepure^U\j{ze\ Latvian cepure ^Mutze, hat; Bedeckung the Kornhaufen auf 
dem Felde', russ. cepec' bonnet' etc. 
References: WP. II 559. 
Page(s): 930 


==========
Root / lemma: skei-\ (to cut, separate) is detrimental for alb. language because 
alb. people chose it to design clear speech: alb. {*skei-b-), shq/p' c\ear speech, separated 
words', {*skipta) shq/pto^speak clearly', {*skipta) shq/ptar' peop\e who speak clearly'. Alb. 
people employed these cognates during Turkish long occupation to preserve their 
language. Hence people who didn't speak clearly were ostracized by the majority of alb. so 
important became the clear Indo European language to alb. that they finally switched from 
the name Arban (Alban) to {*skipta) shq/ptar' peop\e who speak clearly'. Other alb. 
derivatives: {*Schabe) shkabe'eag\e (with sharp talons)', alb. Geg {*scipioni) Shq/pn/'\and 
of eagles'. Obviously alb. association of {*skipta) shq/ptar' peop\e who speak clearly' and 
{*skipion) shqiponje^eaq\e' was distorted by lllyrian soldiers serving in the Roman army. 
Illyrians who didn't speak Latin translated the Roman military ensign with the eagle as: 
scipio -onis, m. "a staff, wand' = alb. {*scipion}) shqiponje^ihe eagle (itself)', also alb. 
{*scipioni) Shq/pn/land of eagles'. When Gergj Kastrioti "king of Epirus' presented his 
heraldic emblem of the eagle (the double he
==========
Root / lemma: skhel- 

Meaning: to stumble 

Note: (?) only Old Indie and armen. 

Material: Old Indie s/r/7a/5/e'stolpert, sways, gehtfehl', sA/75///5-'taumelnd fehlgegangen; 

whereof etwas fehit, to little '; Armenian sxalem, SA'5///77'strauchle, irre, sijndige, verfehle; 

werde verfehit, vermiftt, frail; tue eine Fehlgeburt', sxa^^a\^\\., error, mistake, lack; 

fehlerhaft, lacking, to little ', SA-a/a/r 'taumeind (in intoxication)'. 

References: WP. II 599; 

See also: whether expressive formation to (s)kel-41 

Page(s): 929 




==========
Root / lemma: sRed- 

Meaning: to cover 

Material: Old Indie chadati {uncovered), chadayat/" bedeck, verbirgt', chattra-m' shelter', 

chad/s-n. "cover, roof; Avestan sadayantf-^a garment' (skyth. trouser?), afghan. pso/s/'to 

put on, wear' {*pati-u pa-sad-); Old High German hazrw.. Middle High German haezen. 

"Rock, clothing'. Old English hseteru Hom. PI. n. "dress'. 

Note: 

common lllyrian-alb. sk- > h-. 

References: WP. II 558, Holthausen Altengl. Wb. 146. 

Page(s):919 


==========
Root / lemma: (s)Rel- 

Meaning: to spring 

Material: Old Indie salabha-xx\. " locust, grasshopper', sa/una-m. "a certain insect', salura- 

m. "frog'; 

Note: 

The inanimate suffix -ur- . Old Indie sa/ura-m. "frog' : UAupioi , oi, lllyrians, UAupia , n, 
lllyria, alsoUAupi? , n. Adj. UAupiKO? , n, 6v, lllyrian: -kpi, the region or province of lllyria, 
'lAAupi^U) , speak the lllyrian language, 'IAAupia:--hence Adv. 'lAAupiaii. 

Middle High German scher jumping, auffahrend, angry, furious ', schellec^ jumping, 
angry, irate, wild', Old High German sce/o "Schellhengsf ("Bespringer'), Modern High 



German schalen^ spring, jump ', Middle Higli German sc/7e/c/7"Bockhirscli'; Old Icelandic 
ske/krlear' as '*erschreckt auffahrend'; for Gothic etc. skalks 'servant' one assumes a 
basic meaning " jumper, Laufbursche' and dissimilation from * skal-[s]kas-\ 

Lithuanian si/o/ys'Galopp', Latvian su6//s' footstep '. 

Maybe alb. (ske/-) *shke/'to step'. 

References: WP. II 600. 
Page(s): 929 


==========
Root / lemma: (s)Rem- 

Meaning: disabled 

Material: Old Indie sama/a-n. 'fault, error, damage, pity'; Old Icelandic PN. Hamall, Old 

English hamola. Old High German /75/775/'mutilated' (Modern High German Hammel ' 

wether, castrated ram '); Old Icelandic hamla. Old High German hamalon e\.c. ' mutilate '; 

with expressive -mm-:0\6 Icelandic skammr. Old English Old High German sca/77/77 'short'; 

Old High German hamm, hammer^ rc\\}W\a\.e6\ 

Note: 

common lllyrian-alb. sk- > h-. 

References: WP. II 560, Holthausen Awn. Wb. 105; 

See also: in addition also kern- above S. 556. 

Page(s): 929 


==========
```


## [2026-09-14T01:57:22.109Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport re\nt=open('POK_full.txt',encoding='utf-8',errors='replace').read()\nblocks=t.split('Root / lemma:')\nfor b in blocks:\n    if re.search(r'WP\\.\\s*II\\s*54[01]',b) or re.search(r'skandat|scando|scandere|skandalon',b,re.I):\n        print('Root / lemma:'+b[:1600]); print('==========')\nEOF"
}
```


## [2026-09-14T01:57:22.897Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"skand\" POK_02.txt POK_03.txt | head -30"
}
```


### [2026-09-14T01:57:23.375Z] TOOL RESULT

```
Root / lemma: skei-\ (to cut, separate) is detrimental for alb. language because 
alb. people chose it to design clear speech: alb. {*skei-b-), shq/p' c\ear speech, separated 
words', {*skipta) shq/pto^speak clearly', {*skipta) shq/ptar' peop\e who speak clearly'. Alb. 
people employed these cognates during Turkish long occupation to preserve their 
language. Hence people who didn't speak clearly were ostracized by the majority of alb. so 
important became the clear Indo European language to alb. that they finally switched from 
the name Arban (Alban) to {*skipta) shq/ptar' peop\e who speak clearly'. Other alb. 
derivatives: {*Schabe) shkabe'eag\e (with sharp talons)', alb. Geg {*scipioni) Shq/pn/'\and 
of eagles'. Obviously alb. association of {*skipta) shq/ptar' peop\e who speak clearly' and 
{*skipion) shqiponje^eaq\e' was distorted by lllyrian soldiers serving in the Roman army. 
Illyrians who didn't speak Latin translated the Roman military ensign with the eagle as: 
scipio -onis, m. "a staff, wand' = alb. {*scipion}) shqiponje^ihe eagle (itself)', also alb. 
{*scipioni) Shq/pn/land of eagles'. When Gergj Kastrioti "king of Epirus' presented his 
heraldic emblem of the eagle (the double headed imperial eagle) he inadvertently changed 
the name of his people, lllyrian emperors had introduced the double headed eagle of their 
Hittite heritage. 

References: WP. II 541 ff., WH. II 493 f., 495 f., 503, Trautmann 263 f. 
Page(s): 919-922 

Root /lemma: (s)kep-2, (sjkop- and (s)kap- (s)keb(h)-, skob(h)- and skab(h)- 
Meaning: to work with a sharp instrument 

Material: A. Forms in -k (th
==========
Root / lemma: (sj/ca/o-s 

Meaning: a large fish 

Note: or rather /cra/o-s? 

Material: Latin squalus^e'xu grofterer Meerfisch'; das 5- could but previously secondary 

from squatus ds., squama^ scale, husk ' attributed sein; 

Old Icelandic hvalrm. (besides -hveliu.) "whale' (/-stem). Old English hwael, engl. 
whale. Old Saxon Old High German hwalds., besides Old High German hwelira 
(Germanic *hvali-s-dn-). Modern High German Waller, i/Velleran6 Middle High German 
'H/e/s'(Germanic *hvali-s), wherefore also Old Prussian /ra/zis "Wels'; the mythische fish 
Avestan kora- is die Iran. Wiedergabe eines urmordwin. */ro/5 "fish', later kal, to tscherem. 
kol, lapp. guole, Finnish kalaetc; die ganze family also probably finno-ugr. origin. 

References: WP. II 541, WH. II 581 f.. Hoops, Engl. Stud. 28, 1 ff., Jacobsohn, Arierand 
Ugrofinnen 241 f. 
Page(s): 958 


==========
```


### [2026-09-14T01:57:23.434Z] TOOL RESULT

```
POK_02.txt:1407:got.  hi-gitan  ^finden',  aisl.  geta  ^erreichen;  hervorbringen,  vermuten' ags.  be-gietan  ^erhalten,  erzeugen',  for-gietan  ^vergessen'  (engl,  get,  heget forget  skand.  Lw.),  ahd.  pi-gezzan  ,ev\3ingen',  fir-gezzan  ^vergessen'  (dazu  alj^ Faktitiv  mhd.  ergetzen  ^vergessen  machen,  entschädigen'),  nhd.  ergötzetüi as.  bi-getan  ^ergreiien',  far-getan  ,vergessen' ;  mnd.  gissen,  schwed.  norwj gissa  ,raten,  vermuten'  (engl,  guess  ndd.  oder  nord.  Lw.) ;
POK_02.txt:2794:kand-,  skand-  und  (ai.)  {s)kend-  ,leuchten,  glühen,  hell'.
POK_02.txt:2797:alb.  ^e^^.  hdne,  tosk.  hene  ,Mond'  (*skandnä) ;
POK_02.txt:6515:Auf  mouro-'.  aisl.  maurr^  daneben  *meur-  in  dän.  myre^  schwed.  myi^a {*meu'i'iön-),  mndl.  Fl.  mure  (einmal  belegt)  miere,  nndl.  mier,  mnd.  mlre (zum  l  s.  van  Wijk),  mengl.  mire,  myre  (skand.  Lw.),  ags.  myre,  engl,  mire, heute  nur  noch  fis-mire  (vom  Ausspritzen  ihrer  Säure),   krimgot.  miera.
POK_03.txt:2224:Gr.  axivd-ÖQ  ,untertauchend* ;  lit.  skestüj  sk^sti  ,untersinken,  ertrinke Kausat.  skandinüj  -dmti  ,ertränken';  apr.  auskimdlai  ,er  gehe  unter*. WP.  n  565,  Trautmann  265.
POK_03.txt:2709:Nd.   slük   ,schlaff*,   ndl.    sluih  ,mager,   hager,   glatt*,   engl,   slouch  ^] Kopf  hängen,  träge  und  nachlässig  gehen';  aisl.  slohinn  ,erloschen*,  fiWi , erlöschen,  sterben*;  slekkva  ,löschen,  töten^;   norw.   sloka  ,faul  sein*, slokeren  ,schlaff  sein,   schlottern*,   mit   kk:  slukkern  ds.   (nhd.   Schluckt^ slukk   ,traurig',   slokh  ,schlaff,   schwach',  norw.   slauk   ,schlaffer   Men8< slauka   ,sich   schleppen',   ags.   sleac  ,schlaff';   ohne  s-:   aisl.   loka  ,scl herabhängen    lassen',    norw.    lukr,    lugr   ,lose,   schlotternd';    daneben  mit expressiver   Media   geminata   norw.    schwed.   slugga   ,sch werfällig  gehj (engl,  slug,  slug-gish  ,schläfrig,  träge'  ist  skand.  Lw.),  mnd.   luggich vermutlich  lit.  slügstu,  slügau,  slügti  , abnehmen,  kleiner  werden*.
POK_03.txt:2920:-iehenS  ahd.  snar(a)ha  , Schlinge*,  aisl.  snara  (*snarhö7i)  »schlingen,  knüpfen, ^indenS  snara  f.  ,Schlinge'  (skand.  Lw.  ist  ags.  sneare  f.  , Schlinge^),  snarr rasch,  scharf^  mnd.  snarllken  Adv.  ,schnell,  bald',  ags.  snierian  ,eilen^  aus 0gjiarhian  (,schnelP  aus  ,was  sich  dreht,  schnell  wendet'). WP.  II  699  ff.,  WH.  II  165,  Trautmann  197,  Vasmer  2,  213  f.
```


## [2026-09-14T01:57:28.459Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"emporspringen\\|scando\\|skänd\\|skdnd\\|skdndati\\|skandati\" POK_03.txt | head -20; echo ===; grep -n \"Root / lemma: skand\\|lemma: skand\" POK_full.txt"
}
```


### [2026-09-14T01:57:28.564Z] TOOL RESULT

```
(eval):1: == not found
```


## [2026-09-14T01:57:30.014Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; ls incoming/WLD/; echo ===; awk 'BEGIN{RS=\"\\f\"} NR>=530 && NR<=560' incoming/WLD/WLD_Bd2_pages.txt | grep -n \"skand\\|scando\\|scala\\|540\" | head"
}
```


### [2026-09-14T01:57:31.218Z] TOOL RESULT

```
Exit code 1
WLD_Bd1_1930_dli_70244_djvu.txt
WLD_Bd1_1930_dli_70244_text.pdf
WLD_Bd1_pages.txt
WLD_Bd2_1927_dli_106624_djvu.txt
WLD_Bd2_1927_dli_106624_text.pdf
WLD_Bd2_pages.txt
(eval):1: == not found
```


## [2026-09-14T01:57:34.131Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"emporspringen\\|scando\\|skandati\" POK_03.txt | head -20; echo \"---\"; grep -n \"lemma: skand\" POK_full.txt"
}
```


### [2026-09-14T01:57:34.202Z] TOOL RESULT

```
---
```


## [2026-09-14T01:57:34.943Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==545' incoming/WLD/WLD_Bd2_pages.txt | head -60"
}
```


### [2026-09-14T01:57:36.041Z] TOOL RESULT

```
540                                             sqand-


     Arm. ham         in   hamahor „perYersus,        tortuosns^*,       Bugge KZ. 32, 51    bleibt
fern,    Pedersen KZ. 39, 379. Mit ^-Vokalismus: hellenistisch xojLt^og
           s.

„Band, Schleife‘‘, xofi^oco „knupfe“ {kmi- in oxxa^og „Armband“ Hes. als
aol. Entw. ans "^ov-xa^ogl    Fick BB. 6, 214. Bezzenberger BB. 16, 251),
norw. hempa „Kieiderstrippe, Scbiinge, Henkel“ (auch „Zeug yon Hanf‘,
in welcber Bed. sicher von hamp „IIanf‘^; ob die andern daraus entwickelt?
s.   Bugge BB. 3, 103, Zupitza Gutt. 22, 113).
     Yon einer Gdbed. ,,krumm gehn“ aus reiht man (vgl. Zupitza KZ. 36,
73,  Fick ni^ 453, Persson Beitr. 156) an: gr.               ,.hinke‘‘ erschlossen

aus dem Kamen 2Jx6ju^og       (Bechtel  KZ.  44, 358   iiber  oxiju^og s. dagegen
                                                                     ;


u. sqeihh-j sqi-m-h-), schwed. shnmpa „hinken“, shimpa „hupfen, tanzen“
ahd. scimpfan „Scherz treiben, spielen, verspotten*^, nhd. schimpfen, Schimpf
(usw., 8. Fick III     453, Falk-Torp u. shamfere; von Schroder Abl. hin-
gegen auf eine versch. germ. Wz. shenah- bezogen), nhd. (nd.) Jiumpen^ htim-
peJn (oder zu qeub-1 s. einerseits Zup. Gutt. 23, andrerseits Falk-Torp u.
Immpe, Koch anders Schroder Abl. 37).
   '^{s)hami- erinnert an qamp- „biegen“, auch qam ds. (s. noch qantho-^
qopena); sein Yerhaltnis zu {s)hemb- ist noch unklar; ebenso das zur nasal-
losen Wz. fiir „biegen“(?) oder „haken"‘ von lit. himhu, kibti „hangenbleiben,
sich festhaken‘‘, hah\         „hangen“, hahlnti „hangen“, kablys „Haken“,
hab^ jjHeftel, Haken‘" (aber auch e-Formen wie hebeklis „Haken'‘ s. Les-
kien Abl. 330), abg. shoba „fibula'^, russ. skoba „Klammer‘" (Zupitza Gutt.
22); iiber die Yermutung, daB mit habet i nsw, auch *qoh- „sich gut fiigen"
ursprungsgleich sei, s. unter diesem fiir das von Solmsen Beitr. I 205 mit
                                                  ;


himhu^ skoba verb, xopivog „Korb, Tragkorb“ („*Anhanger'‘?) und messen.
xipog „Kranz'‘ s. Boisacq u. xvq)ivog^ der darin ein Mittelmeerwort ver-
mutet), wozu viell. aisl. hop n. „kleine Buchf'j ags. hop „Riog“ (oder diese
als qo(u)b- zu qeu-, -b- „biegen“), aisl. hespa „Eisenkrampen“         ags. hoepse^—
h<Bsp^ mhd. haspe^ hespe^ nhd. Haspe^ Hdspe^ holl. hespe „Huftgelenk“,
mndl. auch „Hacke“ Bugge BB. 3, 103; Falk-Torp u. hop^ hasps I). Immer-
hin steht auch neben qamp- ein nasalloses            in ai. cdpa- m. n. „Bogen“,
 capdld- .jbeweglich, schwankend, unstet^^, np. cap „link“, eigentlich „krumm“.


sqand- „aufschnellen, in die Hohe gehn^‘.
     Ai. skdndati „schnellt, springt, spritzt“, a-skandati „fallt an“;
     gr.  axavddXy^Qov „Stellholz in der Falle“ („*losschnellend“; Bed.-Paral-
lele bei Osthoff EP. I 355f.),       oxdvdakov „Fall8trick; AnstoB, Argernis";
     lat. scando^ -ere „steigen, sich erheben“, scala (^scand-sla) ,jStiege, Treppe,

Leiter'";
     mir.       sescaind   Pf.   „er sprang^,    Praes.     scennim „ich        springe'",   sceinm
„Spmng“, cymr. cy-chwynnu j.auffahren, aufbrechen".
  Curtins 166, Fick 566, Gegen die Yerb. von gr. oxibvaodai mit scando
8. Persson Beitr. 149 a 3.
  Schwierig ist die Beurteilung des kelt. c-Yokalismus: R. Schmidt IF. 1, 75
halt ihn fur sekundar gegeniiber dem a des Perfekts, Pedersen KG. I 77
denkt zweifelnd (Reichelt KZ. 46, 311 zuversichtlich) an idg. Wechsel an
```


## [2026-09-14T01:57:47.808Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i \"skand\" AHD_watkins1985.txt | head -20; echo \"---POK_full\"; grep -n -i \"skandale\\|scand-sla\\|scala\" POK_full.txt | head -20"
}
```


### [2026-09-14T01:57:47.882Z] TOOL RESULT

```
934:*sua-yo-, contracted to *si-yo- in Greek huein, to rain, and huetos, rain: ISOHYET. II. Possible extended zero-grade form *sib-. 1.Germanic *sip- in: a. Old English sipan, sipian, to drink, sip: suP!; b. Old French soup(e), soup: SOUP, (SUP2). 2. Germanic “supp- in: a. Old English sopp, bread dipped in liquid: sop; b. possibly Low German sippen, to sip, probably akin to the source of Middle English sippen, to sip: stp. III. Possible ex- tended zero-grade form “sig-. 1. Germanic *sik- in Old English sican, to suck: sucK. 2. Germanic shortened form *sukdn in Old English socian, to steep: SOAK. 3. Latin siigere, to suck: SUCTION, SUCTORIAL. 4, Variant form *sik- in Latin siicus, succus, juice: SUCCULENT. [Pok. 1. seu- 912.] seut-. To seethe, boil. 1. Germanic *seuthan in Old English séothan, to boil: SEETHE, (SODDEN). 2. Germanic *suth- in: a. Middle Dutch sudde, sudse, marsh, swamp: sups; b. suffixed form *suth-l- in Middle High German sudelen, to soil, do sloppy work, akin to Middle Dutch soetler, sutler: SUTLER. [Pok. 4. seu- 914.] si-lo-. Silent. Suffixed (stative) form *si/-é- in Latin silére, to be silent: SILENT. [In Pok. 2. sé(i)- 889.] skabh-. To prop up, support. Suffixed form *skabh-no- in Latin scamnum, a bench (> Old English sceamel, table, stool): SHAMBLES. [Pok. skabh- 916.] skai-. Also kai-. Bright, shining. 1. Extended form *kaid- in Germanic *haiduz, “bright appearance,” manner, quality, in Old English -hdd, quality, condition: -Hoop. 2. Suffixed form *ki-t-ro- in Sanskrit citra-, variegated, many-colored: CHEETAH, CHINTZ. [Pok. (s)kdi- 916.] [skalkaz. Servant, slave. Germanic noun of unknown origin. 1. Old High German compound marahscalc, “horse-servant” (see marko-). 2. Germanic compound *sini-skalkaz, “old servant” (see sen-'). [In Pok. (s)kel- 929.]] skamb-. Also kamb-. To curve, bend. Suffixed form *kamb-o- in Celtic *kambo-, crooked, and denominative verb *k(a)mb-yo-, to turn, exchange, whence Gallo-Latin cambidre, to exchange: CAMBIST, CAMBIUM, CHANGE. [Pok. (s)kamb- 918.] skand-. Also skend-. To leap, climb. 1. Latin scandere, to climb: SCAN, SCANDENT, SCANSION, SCANSORIAL; AS- CEND, (CONDESCEND), DESCEND, TRANSCEND. 2. Suffixed form *skand-alo- in Greek skandalon, a snare, trap, stumbling block: SCANDAL. 3. Suffixed form *skand-sld- in Latin scdlae, steps, ladder: ECHELON, ESCALADE, SCALE?. sked-. To split, scatter. Extension of sek-. 1. O-grade form *skod- in Germanic *skaé- in Old English *sc(e)ater- ian, to scatter: SHATTER. 2. Variant nasalized form *ska-n-d- in Latin scandula, a shingle for roofing (< “split piece”): SHINGLE}. [Pok. (s)k(hjed- 918.] skeei-. To gleam. 1. Suffixed form “ske(ji-no- in Ger- manic *skinan, to gleam, shine, in: a. Old English scinan, to shine: SHINE; b. Old High German scinan, to shine: GEGENSCHEIN. 2. Germanic extended form *ski-m- in Old English scimerian, scymrian, to shine brightly: SHIM- MER. 3. Possibly suffixed form *ski-nto-, shining, in Latin scintilla, a spark: SCINTILLA, SCINTILLATE, STEN- CIL, (TINSEL). 4. Suffixed zero-grade form *skia-G-, *skiy-d- in Greek skia, shadow: SKIAGRAM, SKIASCOPE, SQUIRREL. [Pok. skai- 917.] skei-. To cut, split. Extension of sek-. 1. Germanic suffixed form *ski-nd- in: a. Old English scinu, shin, shinbone (< “piece cut off’): SHIN!-; b. Old French eschine, backbone, piece of meat with part of the back- bone: CHINE, 2, Latin scire, to know (< “to separate one thing from another,” “discern”): SCIENCE, SCILICET, SCIOLISM, SCIRE FACIAS; ADSCITITIOUS, CONSCIENCE, CONSCIOUS, NESCIENCE, (NICE), OMNISCIENT, PLEBI- SCITE, PRESCIENT. 3. Suffixed zero-grade form *skiy-end in Old Irish scian, knife: SKEAN. 4. Extended root *skeid- in: a. Germanic *skitan, to separate, defecate, in Old English *scitan, to defecate: SHIT; b. suffixed zero-grade
1262:ART? er-1 ARTEL ar- ARTERIO- wer-2 ARTERIOLE wer-2 ARTERY wer-2 ARTHRO- ar- ARTHUR rtko- ARTICLE ar- ARTIFACT dhé-1 ARTIFICE dhé-1 ARTIODACTYL ar- ARTISAN ar- ARTIST ar- ARYAN aryo- ASBESTOS gWes- ASCEND skand- ASCRIBE skribh- ASH! as-
1389:cons deuk- CONATION ken-1 CONCAVE keue-2 CONCEAL kel-2 CONCEDE ked- CONCEIVE kap- CONCERN krei- CONCESSION ked- CONCH konk(h)o- CONCHA konk(h)o- CONCHO- konk(h)o- CONCIERGE servus CONCILIATE kela-2 CONCISE kae-id- CONCLAVE kleu-3 CONCLUDE kleu-3 CONCOCT pekw- CONCOMITANT ei-1 CONCORD kerd-1 CONCOURSE kers-2 CONCRESCENCE ker-3 CONCRETE ker-3 CONCUBINE keu-2 CONCUPISCENCE kwép- CONCUR kers-2 CONCUSS kwét- CONDEMN dap- CONDENSE dens-2 CONDESCEND skand- CONDIGN dek-1 CONDIMENT dhé-1 CONDITION deik- CONDOLE del-3 CONDONE do- CONDOTTIERE deuk- CONDUCE deuk- CONDUCT deuk- CONDUPLICATE dwo- CONE k6-
1420:DEODAR deiw-, deru DEONTOLOGY deu-1 DEPEND (s)pen- DEPICT peig-1 DEPILATE pilo- DEPLOY plek- DEPLUME pleus- DEPONE apo- DEPOPULATE populus DEPORT per-2 DEPOSIT apo- DEPRECATE prek- DEPRECIATE per-6 DEPREDATE ghend- DEPRESS per-5 DEPRIVE pert DEPTH dheub- DEPURATE peue- DEPUTE peu- DERACINATE wrad- DERANGE sker-3 DERELICT leikw- DERIVE rei-3 -DERM der-2 DERMA! der-2 DERMA? tera-1 -DERMA der-2 DERMATO- der-2 DEROGATE reg-! DERRIS der-2 DESCANT kan- DESCEND skand- DESCRIBE skribh- DESERTS = ser-3 DESERVE servus DESICCATE selkw- DESIGNATE sekw-1 DESIRE sweid-1 DESIST sta- DESMID dé- DESOLATE s(w)e- DESPAIR spé-1 DESPICABLE spek- DESPISE spek- DESPOIL spel-! DESPOND spend- DESPOT deme-! DESTINE sta- DESTITUTE sta- DESTRIER deks- DESTROY ster-2 DESUETUDE s(w)e- DESULTORY sel-4 DETAIN  ten- DETECT (s)teg- DETENT ten- DETER tres- DETERIORATE de- DETERMINE ter- DETEST trei- DETONATE (s)tene- DETOUR tera-1 DETRACT tragh- DETRIMENT tera-1 DETUMESCENCE teue- DEUCE! dwo- DEUTERAGONIST deu-? DEUTERIUM deu-!
1441:EsLis gWela-1 EBULLIENCE beu-! ECBOLIC gWele-1 ECCENTRIC kent- ECCHYMOSIS gheu- ECCLESIA kela-2 ECCRINE krei- ECEsIsS weik-1 ECHARD segh- ECHELON skand- ECHIDNA ang¥hi- ECHINO- ang¥hi- ECHINUS angVhi- ECHO (s)wagh- ECHOLALIA 1a- ECLAIR kelo-2 ECLAIRISSEMENT kelo-2 ECLAMPSIA [ap- ECLECTIC leg-! ECLIPSE leikw- ECLOSION kleu-3 ECOLOGY weik-1 ECONOMY weik-1 ECRU kreue-1 ECSTASY sta- ECTO- eghs ECTOSARC twerk- ECU skei- ECUMENICAL welk-1 ECZEMA yes- EDACIOUS ed- EDAPHIC sed-! EDDY eti EDELWEISS _athal-, kweit- EDEMA oid- EDENTATE dent- EDGE ak-
1477:ERYTHEMA reudh-! ERYTHRO- reudh-1 ESCALADE skand- ESCAROLE ed- ESCHATOLOGY eghs ESCHEAT kad- ESCUDO skei- ESCULENT ed- ESCUTCHEON skei- ESOTERIC en ESPARTO sper-2 ESPECIAL spek- ESPERANCE spé-! ESPIONAGE spek- ESPOUSE spend- ESPY spek- ESQUIRE skei- ESSAY ag- ESSENCE es- ESSONITE sék- ESTABLISH sta- ESTANCIA sta- ESTER ak- EsTHER  ster-3 ESTRONE eis-1 ESTRUS eis-1 ESTUARY aidh- ESURIENT ed- ETCETERA eti, ko- ETCH ed- ETERNAL aiw- ETESIAN wet-2 ETHER aidh- ETHIC s(w)e- ETHMOID sé-3 ETHNIC s(w)e- ETHNO- s(w)e- ETHOS s(w)e- ETIOLOGY ai-! ETIQUETTE steig- EU- esu- EUCALYPTUS kel-2 EUCARYOTE kar-1 EUCHARIST gher-5 EUGLENA gel-2 EUMENIDES men-1 EUNUCH segh- EUONYMUS n6-men- EUPATRID peter- EUPEPTIC pekw- EUPHEMISM bha-2 EUPHONY bha-2 EUPHORIA bher-1 EUPHROSYNE gWhren- EUPNEA pneu- EUREKA were-2 EuRUS eus- EURY- were-1 EUuRYDICE deik-, were-1
2222:SCAB skep- SCABBARD sker-1 SCABBLE skep- SCABIES skep- SCABROUS_ skep- SCAGLIOLA skel-1 SCALD! kele-1 SCALE! skel-1 SCALE? skand- SCALE’ skel-1 SCALENE skel-! SCALL_ skel-!
2223:SCALP skel-1 SCALPEL skel-1 SCAN skand- SCANDAL skand- SCANDENT skand- SCANSION skand- SCANSORIAL skand- SCANT kem-1 SCAPHOID skep- SCAPULA skep-, sker-1 SCAR? sker-1 SCARCE kerp- SCARIFY!  skribh- SCARP_ sker-! SCATHE skét(o)- SCATO- sker-4 SCAVENGER keu-! SCENT sent- SCHADENFREUDE preu-, skét(e)- SCHEME segh- SCHERZO sker-2 SCHILLER skel-3 SCHIPPERKE skipam
2400:TRAIN OIL dakru- TRAIT tragh- TRAITOR d6- TRAJECT yé TRAMMEL macula, trei- TRAMP der-! TRAMPOLINE der-1 TRANCE ei-1 TRANQUIL kweie-2 TRANS- tere-2 TRANSACT ag- TRANSCEND skand- TRANSCRIBE  skribh- TRANSDUCER deuk- TRANSECT sek- TRANSFER bher-1 TRANSFIGURE dheigh- TRANSFIX dhig¥- TRANSFUSE gheu- TRANSGRESS ghredh-
---POK_full
75192:Muschelschale', Middle Low German schellet 'bowl, fish scale '; Old High German scala
```


## [2026-09-14T01:57:49.230Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i \"skandalon\\|skandal\" POK_02.txt POK_03.txt | head; echo \"---IEC\"; grep -n -i \"skandō\\|skandami\\|skandati\\|skand-\" IEC.txt | head -20"
}
```


### [2026-09-14T01:57:49.320Z] TOOL RESULT

```
---IEC
15466:skand- (skandos, à) “fall, breakdown, ruin’. (skond-? Cf. skend-, skond, skid- and WP II, 564. Alternative vocalism of types skál-: skel- and skár-: sker-, q.v. EM confused on Lat. scando; WH inconclusive) Skt. skandah, m. destruction; disease- demon’; Av. skondo, m. ‘ruin’; Arm. (ambig. *skand- or *sknd-) xanti, adj. (Cindigent'. But for xant ‘lewd’, see sknt-: Gk. skat-: G Schund, etc.); Gk. cf. skándalon, n. (fsnare; offence, disgrace’. For sense cf. G Falle ‘snare’: fallen ‘fall’. Gk. type *skndol-?); Olr. cf. scannar, scaindir, m. ‘defeat’; Ir. scannar, m. (Caffray; slander but for Olr. aor. sescaind “he jumped”, see skend-); Olr. cf. scaindrim, v. “scatter” beside Ir. scannruighim, v. (scare; scatter. E scant, adj. is of ambig. origin, cf. skam-); OCS skodü, adj. ‘puny, poor, defec- tive’; skoda, f.; Li. skandinti, tr. ‘drown, sink” Variant in Skt. skannáh, pp. “fallen”
15563:skendoó, ið “dash, rise, fall. (Cf. the seman- tics of type pad-). (Variant w. *-o- in Av. and Lat. Cf. skand-, with shva-variant also in Ir.). Cf. WP II, 565 Skt. skándami, v. “dash, bound, spurt, drop’; a-skandami, v. ‘attack’; Av. cf. skond-, v. “smash”; skendo, m. (fruin', lit. "allt: a-skon- da, adj. f. ‘virgin’; (Lat. -e- in dé-scendo is
15565:secondary. See skand- but possibly a form *sknd- is implied for scando); Olr. scendim, aor. 3s: sescaind; mod. Ir. sceinnim, scinnim, v. ‘leap, start, bud, shoot'; Li. skendiu, eti & Skestu, skgsti, pf: skendau, v. ‘sink, drown’ beside skandinti, inf. tr. id. (o-gde); OCS cf. (Ð stedije, n. (generation, tribe’, lit. *des- cent^?); cf. Ukr. naSCad-ok, m. “origin”. (For a possible long-zero grade to account for Lat. scando, cf. planta, plantago, prandium, fr. *plm-tà, *prm-edio-, etc. The background of Gk. skinthós, adj. (diving! is problematical. Cf. písures, piítnemi, skídnamai)
15615:skheud- in Skt.) Skt. Codami, v. “egg on; hurry’; Alb. hudh, v. ‘fling’; MIr. cf..brot-scuad, s. ‘rubbish’; OHG skiozan, OS skiotan, OE scéotan, sv. 2 'shoot'; sceot, adj. ‘ready, quick’; ON skjóta, sv. 2 as OHG; skjótr, adj. as OE; (m. also “vehicle; horse); Sw. skjuta, sv. 2. ‘thrust, smite’ skeulos, om, is, à ‘cover, shelter’. Cf. skül-. (Skt. variant: skhoul-) Skt. cf. kholah, m. 'rainhat, helmet; Arm. (vowel ambig.) xuy, gs: xyi, ab. s. xyiv, s. ‘hut’; ON skjól, n. ‘shelter, cover’; Sw. skjul, n. ‘dutch barn’; N. E. shiel, shieling 'shepherd's huť; Norw. cf. skjule, v. ‘hide’. WP II, 547 skeup- ‘poke, stab, grope’. (Skt. variant: skhiup- or skhup-). Gmc. ambig. Skt. čhupāmi, v. “touch'; Go. (ambig. *skeubh-?) skiuban, sv. 2. ‘thrust; MHG schieben, sv. 2. id.; OE sceofan, sv. id. (beside sküfan, sv. 2. with instant aspect as lücan, sv. 2 ‘lock’, and a-sprütan, sv. 2. ‘sprout’; Du. schuiven, sv.; spruiten, id.); R SCup, m. “probe, lancet'; po-SCüpat, inf. “feel, grope’. Nominal type in Skt. chupah, m. “touch; hand-to-hand fight". Isophonic in OCS Stupli, adj. “weak, lean, ailing’; Pol. szczupły, Slovak, Stüply, id. skeut- ‘shred, tatter; shredded, torn’. (Vari- ant in Skt?) Skt. cf. a-Chotitab, pp. “torn off (butisophonic pra-$Cotami, v. = 'drip); ON skjóða, f. “skin bag’; Li. skiautis, gs: ies, f. ‘shred, snippet"; Latv. cf. Sautrs, adj. (loose, hanging’, from a variant *sKeut-?). (Isophonic in OCS Stusto, Stutiti, v. ‘perceive’, radical in Av. sku- look") skéuð, ið (sKeu-) “jump, start, go’. Cf. sKeuo as separate entry Skt. cf. (radical only) chyu- ‘go’; Gk. cf. skeüos, n. ‘equipment’; Alb. hov, v. jump’; Ir. cf. sceabha, m. ‘eagerness’; Go. skewjan, v. go’. LW in Fr. esquivier, It. schivare, Alb. shkoj & E eschew, via Romance); ON skæva, v. ‘hurry, clear off; (o-gde in) Du. schooien, v. ‘go away, clear off”; Fris. skoaje, v. ‘arrange’ (factitive: “make go"); OCz. ščuju, SCváti, v. fegg on: Pol. szczuC, v. ‘incite’; Ukr. SCuty (w. instr.), id. skond-, r-gde formula to accommodate some forms of type skend- (skand-); cf. sküd-
16080:sKand- (sKhand-) ‘glistening, white’. WP I, 352 Skt. Chandab, adj. ‘pleasant’; m. ‘shape; joy’; Chandayami, v. ‘appear’; cf. also (variants) $Candrah & cCandrah, adj. “bright; Candah, adj. ‘burning’; Canda, Candih (name of a god- dess); Alb. cf. hàn&, hënë, f. ‘moon’; Lat. candeo, ére, v. ‘glisten’; Br. cann, adj. “bright, white’; Ir. cf. (?) scead (? scéad), m. ‘blaze on forehead’
```


## [2026-09-14T01:58:01.778Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for n in 164 165 166 167 168; do echo \"===== leaf $n\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N' POK_03.txt | head -50; done"
}
```


### [2026-09-14T01:58:02.703Z] TOOL RESULT

```
===== leaf 164
 Schulter^  {*skl-dhrä  , Schulterblatt  als Schaufel,  als  Grab  Werkzeug') ;
mit  Formans  -mo-  und  den  Bed.  , Schneidewerkzeug;  geschnittenes  Holz; ausgehöhlter  Einbaum,  Kahn':  aisl.  skglm  f.  ,Zinke  einer  Gabel,  Schote', PI.  ,SchereS  nd.  ostfries  ndl.  schalm  ,dünnes  Brett',  aisl.  skalma-tre  ,ge- spaltener  Baum',  ahd.  scalm  ,navis';  auch  wohl  ahd.  scalmo  ,Pest,  Seuche, Leichnam^;  mhd.  schalm(e)  ds. ;  dazu  skelmo  ,Todeswürdiger^  (*skalmian-), mhd.  mnd.  schelm{e)  , Bösewicht';  vgl.  alb.  heim  ,Trauer,  Gift^;  ohne  anlaut. S-:  ags.  helma^  engl,  heim  ,Griff  des  Steuerruders,  Steuer',  mhd.  halm(e), heim  ,AxtstielS  ahd.  helmo,  halmo  , Ruderpinne',  ndl.  helmstock  ds.,  mnd. holm  , Querbalken,  Jochträger^,  aisl.  hjglm  f.  , Steuer',  hjalm-vglr  ,Ruder- pinne' ;
"^skol-dhä  , (abgeschnittene)  Stange'  ist  wohl  die  Grundlage  von  ahd.  scalta , Stoßstange,  Bootshaken',  scaltan  ,mit  einer  Stange  schieben',  nhd.  schalten auch  ,einschalten  (=  dazwischen  hineinstoßen)^  und  übertr.  , walten',  dial. auch  ,spalten',  as.  skaldan  ,ein  Fahrzeug  vorwärts  schieben',  mhd.  schalte^ aisl.  skalda  , Fähre',  mhd.  Schalter,  schelter  , Riegel',  nhd.  Schalter  ,Schieb- fenster,  Stange,  Bootshaken';
mit  Formans  -go-:  mnd.  schalk  , Sparrenstütze'  ostfries.  schalk  , Holz- klötzchen als  Unterlage',  bair.  schalken  ,zerspalten';  schwed.  skulk  ,ab- gesägter  Stumpf;
lit.  skeliitj  skelti  , spalten'  (der  Akzent  nach  sküti?),  skilü,  skilti  ,sich spalten';  , Feuer  schlagen'  (Intonation  der  schweren  Basis,  wie  keines))  skalä ,Holzspan,  Lichtspan',  Iterat.  skeldeti  ,platzen,  bersten' ;  lett.  §kelt  ,spalten', Ekelet  ds.,  skele  ,abgeschnittenes  Stück',  usw.;  über  lit.  kelmas  s.  oben  S.  546;
926
aksl.  Skala  ,Fels,  Stein^  (die   Bed.   ,Schale'   durch   Entlehnung  aus  abd. scäla  ds.),  sloven.  skdla  ,assula  tenuis;  Lichtspan*,  russ.  skalina  ^abgelöste      ] Birkenrinde';  sJcohka  ^Muschelschale'  (s.  oben  lat.  siliqua),  russ.  sceh  »Spalte«  V sloven.  Ualja  ,Splitter^,  poln.  skalic  sig  ,sich  spalten,  bersten';  \'.
hitt.  ükalläi-  ,zerreissen,  aufschlitzen'.  V;^'
Wurzelerweiterung  skel{G)'-p-:
vielleicht  in  ai.  kdlpaU  ,wird   geordnet,  wird  zuteil',    kalpdyati  ,ordnet an*,  klptd  ,fertig,  gerüstet'  =  av.   hu-kdrd'pta-  ,schöngeformt^,  das  jedoch  ~ auch  zu  kdhrp-  , Gestalt'  (oben  S.  620)  gehören  könnte;
gr.  a'A&lotp  , Maulwurf  (als  ,Gräber');  av.6lo\p  m.  ,Spitzpfahl' ;
lat.  scalpö,  -ere  ,kratzen,  ritzen,  scharren,  mit  spitzem  Werkzeug  schnei-  • den,  meißeln'  (scalprum,  scalper  , scharf  es  Werkzeug  zum  Schneiden  ' Meißeln'),  sculpö,  -ere  (ursprglün.  in  Kompositis  aus  scalpö)  ds. ;
ahd.  scelifa,  mhd.  nhd.  dial.  schelfe  ,häutige  Schale',  mnd.  scJielver  ,abge- blättertes   St
===== leaf 165
ück',   schulvern   , abblättern';   aisl.   skjglf  ,Bank',  ags.  scielfe jFlur,    Stockwerk,    Bretterverschlag',    scielf  m.    , Felsspitze',    mnd.   schelf jBrettgerüst,  Regal';
ohne  s:  got.  halbs,  aisl.   halfrj  ags.  healf,  as.  half,  ahd.  nhd.  halb  (ejo-. ,geteilt');  ags.   hielfe.  , Griff,  Schaft'  (engl,   helve),  ahd.   mhd.   halb  , Hand- habe', nhd.  dial.  halb,  helb  ,Stiel';  ahd.  halftra  ,Zaum*,  ags.  hcdfire  ,Halfter',  \ (aus  *, Handhabe');  |
lit.  kdlpa  , Querholz  am  Schlitten',  kxlpa  ,Steigbügel,  Schlinge',  kllpini$  ^ ,Armbrust',  apr.  kalpus  ,Rungenstock';
lit.  sklempiü,  sklempti  , glatt  behauen,  polieren'.
Wurzel  er  Weiterung  skel(e)-b-:
aisl.  skalpr  ,Schiff ',  dän.  dial.  skalp  ,Samenschote,  Hülse',  mnd.  schulpe, scholpe  , Muschel,  Schuppe',  dän.  skulp,  skulpe  ,Schote,  Fruchtbalg',  norw. skolp  ,Schote,  Hülse',  engl,  skalp  (nord.  Lw.)  ,Schädel,  Hirnschale',  aisl. skelpa  f.  , Grimasse',  skolpr  , Hohlmeißel';  aksl.  sklabiti  se  ,den  Mund  auf- machen, lächeln',  cech.  skleb  ,Zähnefletschen';
i-Erweiterung:  sklei-,  sklei-d-,  sklei-k-,  sklei-p-:
aisl.  slita  , zerreißen,   zerstören,   verbringen'   {slitna   intr.    ,rumpi'),   ags.  "* slitan  ,zerreißen',  as.  slltan  ,schleißen,  spalten',  ahd.  slizan  ,spalten,  reißen,
aufbrauchen',   nhd.   verschleißen,   schleißen,  aisl.   slit  ,Schlitz,  Riß,   Abnüt-  'J zung',  a.gs.  geslit  ,das  Bersten',   ahd.   sliz,   nhd.   Schlitz,   mhd.   sleize,  nhd.
Schleiße  , Leuchtspan';  aisl.  slidrar  f.  PL,  sliär  n.  PL  ,Schwert-  oder  Messer-  ^
scheide'  als  *s{k)lei-tro-,  -tra-  von  der  unerweit.  Wzf.  sklei-]  %
lit.  skleidiiii,  sklelsti,  lett.  skliest  , ausbreiten,   umblättern',  lit.   sklaidaü,  -^
-yti  ,hin  und  her   blättern',   reü.   ,sich  zerstreuen',  i§-sklaidyti  ,zerstreuen,  l
vertreiben',  sklisti  ,auseinanderfließen' ;  lit.  sklaidüs  ,zerstreut',  lett.  sklaidis  f
f
927
ein  Herumtreiber,  Taugenichts^;  ohne  anlaut.  s-:  klaidit  ,sich  herumtreiben', JclistUj  klidu,  klist  ,irren*,  lit.  klystUj  khjdau,  klysti  ,sich  verirren'  (ohne  d: lit.  klajöju,  -öti  jherumirren'^,  lett.  klaijdt,  -uot  ds.  eine  ursprüngl.  versch. Sippe?);  apr.  sclaity  schläit,  schklait  ,sondern;  ohne^,  schkläits  Adv.  ;,sonder- lich;  besonders;  sonst',  Adj.  ^schlicht,  einfach';
ags.  sllfan  ^spleißen',  engl,  slive,  ags.  to-slcefan  ,spalten',  mnd.  sUf,  norw. sle
===== leaf 166
iv  »großer  Löffel'.
WP.  II  590  f.,  WH.  I  165,  II  536  f.,  Trautmann  264.
3,  {s)kel~  , schuldig  sein,  schulden,  sollen':  nur  germ.  und  balto-slav.
Got.  skulan,  aisl.  skulu,  ags.  sculan,  ahd.  scolan  ,schuldig  sein^  müssen, sollen',  jünger  auch  solan,  nhd.  sollen,  ags.  scyld  f.  , Schuld',  ahd.  aisl. skuld  ds. ;  got.  skula  m.  ^Schuldner';
alit.  skelü  und  lit.  skeliü^  -hi  , schuldig  sein',  skylü^  (*skilil),  sktlti  ,in Schulden  geraten',  skolä  , Schuld';  apr.  skellänts  , schuldig',  ablaut.  skalltsnan f.  Akk.  , Pflicht',  poskulU  (paskollet)  , ermahnen';
ohne  S-:  lit.  kalt^  , Schuld',  kaltas  , schuldig'.
WP.  II  596,  Trautmann  264 f.;  vgl.  4.  [sjkel-"?
3,  {s)kel-  ,austrocknen,  dörren'.
(jT.  G%EXk(x)  ,trockne  aus,  dörre'  (trans.,  Fut.  g-abIo),  Aor.  8a%rjXa\  intr. Aor.  eaydrjVj  Perf.  io-xAi^xa),  cxfAfirdg  ^ausgetrocknet',  m.  , Skelett',  n.  ,Mumie', O'/lriQÖq  ,trocken,  hart,  rauh,  unbeugsam',  OY.BlL(pq6q  , ausgetrocknet,  abge- magert', GYlr^cpQog  ,klein  und  flink',  cJ-crxsyliyg  1.  ,ohne  Widerstandskraft' (ohne  (TxAT/^oTTjg) ;  2.  , unablässig,  vom  Zorn,  vom  Weinen'  (eig.  ,unversieg- lich');  TtBQL-G^sXrig  ,sehr  trocken,  spröde,  hartnäckig',  rcsQi-GycsXsia  L  , Hart- näckigkeit' ;
schwed.  skäll  , mager,  dünn,  fade,  säuerlich',  nd.  schal  ,trocken,  dürr', mnd.  mhd.  schal  ,schal  von  Geschmack;  trüb,  unklar,  schaln  ,trüb  werden', mengl.  schalowe  , schal,  matt,  seicht',  engl,  shalloio  (auch  wohl  ags.  sceald ,seicht,  nicht  tief,  nd.  scholl  ,seichtes  Wasser');
ohne  anlaut.  s-:  aisl.  hall-ärl  ,Mißjahr',  ags.  hall-heort  , erschrocken';  mhd. hei  (-11-)  , schwach',  hellec  ,müde',  nhd.  heilig  ,matt,  erschöpft  von  Durst', mhd.  ÄeZ^e^en, ermüden,  behelligen',  nd.  hal  , trocken,  mager';  dehnstufig(?) nd.  häly  ndl.  haal  , trocken',  mndl.  hael  ,ausgetrocknet,  dürr,  schal' ;  dän. dial.  hcelm  ,still',  dän.  helme  ,aufhören'  (,*ermatten',  ursprüngl.  vor  Hitze oder  Durst);
lett.  kälss  , mager',  käUtu,  kälst  ,vertrocknen,  verdorren',  kältet  ,trocknen'.
WP.  II597.
928
^1
4.  {s)kel-,  (erweitert  klä-,  klö-)  ^biegen;  anlehnen;  krumm  (auch  sittlich;
,verkehrt,  unrecht^,  verkrümmt*;  bes.  in  Körperteilbezeichnungen: ,biegsames  Gelenk,  Ferse,  Knie,  Hüfte*  (vgl.  auch  S.  611t  höh-  ,spiu. nenO;  skelos-  n.  ,Bieg'ungS  skel-no-  ,krumm'.
Gr.  ayJXog  m.  ,SchenkeF  ayieXlg,  -Idog  »Hinterfuß,  Hüfte'  (att.  ax«A/g) GxeUög  ,krummbeinig',  axoXiög  ,krumm;  improbus^  ayialrjvög  »höckerig^ sch
===== leaf 167
ief,  krumm',  axcolrj^,  -rj-aog  m.  ,WurmS  G%ü}lvTCXEG^ai  ,krümmen,  hin  und her  winden^,  yLsllöv  oTQsßlöv,  nlctyiov  Hes.,  redukt.-stuf.  -Avllog  , gekrümmt, gelähmt',  ^ivXXo-n^oöiwv  Beiw.  des  Hephaistos  (*x£A-,  '^yivX-vög),  'KvUvdta,  -ew ,rolle,  wälze'  (ion.  att.  y.alLvdeü)),  ywXivÖQog  , Walze,  Rolle,  Zylinder';  xwAoy , Glieds  y.coXsG,  att.  yicoXrj  , Hüftknochen,  Schinken',  ^wXrjV,  -fjvog,  'AcoXsög  ds., TKbXrjip  f.  ,Kniekehle,  Knöchel'  (zu  1.  -ap-  oben  S.  50 f.);  xwXwTryg,  -ov  m. ,Eidechse'  (,rait  Gliedern  versehen');  dyiXd^ü)  ,hocke  nieder^  (Frisk  IF.  49^ 99 f.);  über  'Mng  ,Steißbein'  s.  oben  S.  608;
alb.  tshale  ,lahm'  {*s]celno-)',
lat.  scelus,  -eris  »Bosheit,  Verruchtheit,  Verbrechen'  (formal  =  (xx^Aoc;); coluher,  -brl  ,Schlange*  (,sich  windend',  *]celo-dhro-,  *]colo'dhro-)]  calx (s.  unten);
ahd.  (mit  Formans  -ho-)  scelah  (^sJcelha-)  , schief,  krumm^  nhd.  scheel (Denom.  mhd.  schuhen^  nhd.  scMelen)^  ags.  sceolh  ds.,  aisl.  (m.  gramm. Wechsel)  skjalgr  (^slcelkö-)  , schief,  scheeläugig' ;  isl.  sJc^ll  ,schiefer  Mund^ aisl.  sTcäla  silc  ,den  Mund  verziehen^;  mit  labiales  Erweiterung:  aisl. skjalfa  , zittern,  beben'  =  ags.  scielfan  ds.,  engl,  to  shelve  , abschüssig  sein', aisl.  slcjalfr,  skelfr  ,zitternd'?;
ohne  anlaut.  s-:  bsl.  *haliö  {^'holiö)  , lehne  an'  in  lit.  at-si-Jcalti  ,sich  an- lehnen', ät-kalas  , angelehnt';  zu  bsl.  "^klana-  m.  (*kh-no-)  ^Neigung'  in  lit. klänas  ,Pfütze',  ablaut.  klonis  m.  ,Tal'  (Hlä-ni-),  Moni  ,Niederung';  mit idg.  ö:  lit.  kluönas,  lett.  kluons  m.  ,Dreschtenne';  dazu  ferner  oben  S.  509 '^klä-  ,hinlegen';
mit  bsl.  -ul-  =  lat.  -al-  (ind.  -o^[9-]):  mit  £-Suffix:  lit.  kiilU,  külsis  ,Hüfte' (mit  Ä:-Einschub:  kulkBs,  kulk§ms  ,Knöchel,  Sprunggelenk'),  apr.  culczi ,Hüfte';  mit  -Ä:-Suffix:  lit.  kulnas  m.,  kulnis  f.  ,Hacke,  Ferse'  (*kulk-n-), urslav.  *kulkä  f.  ,Hüfte'  in  spätksl.  khka  ,poples',  bg.  kilka  ,Hüfte,  Ober- schenkel' (^s•k^Ui  ,verrenke') ;  skr.  kük  ds.  usw. ;
lat.  calx  ,Ferse'  (calcö,  -äre  ,treten,  stampfen',  calciträre  ,heftig  aus- schlagen',  calcar  ,Sporn',  calceus  ,Schuh',  tarent.  xuXtIov  ds.  aus  osk. *calc-tio-)',  nach  Trautmann  145  idg.  Wurzelnomen  *kolk-  neben  kolk-.
WP.  II  597  ff.,  WH.  I  144  f.,  248,  II  492,  Trautmann  114,  135  f.,  145.
5.  (s)kHei-,  {s)kel-  ,töüen,  rufen'  s.  oben  S.  550.
929
(5)iei-  ;springeii^
Ai.  salabha-  m.  ^Heuschrecke^;  saluna-  m.  ,ein  bestimmtes  Insekt^,  sä- lüra-  m.  ^Frosch^;
mhd.  schel  ^spring-end;  auffahrend^  aufgebracht^^  schellec  , springend, zornig;  wild',  ahd.  scelo  jScheUhengst'  (,Bespringer');  nhd.  schälen  ;be- springen^,  mhd.  schelch  ;Bockhirsch^;  aisl.  skelkr  ;Furcht'  als  ;*erschreekt auffahrend^;  für  got.  usw.  skalks  ;Diener''  vermutet  man  eine  Grundbed. ^Springer;  Laufbursche*"  und  Dissimil.  aus  *skal-[s]kas-',
lit.  suo^ys  ;Galopp^;  lett.  suölis  ;Schritt^
WP.  II  600.
skhel-  ;Strauchehi;  fehltreten' (?); 
===== leaf 168
 nur  altind.  und  armen.
Ai.  skhdlate  ;Stolpert,  schwankt;  geht  fehl^;  skhalita-  ;taumelnd  fehl- gegangen; woran  etwas  fehlt,  zu  wenige*  arm.  sxalem,  sxalim  ;Strauchle, irre;  sündige;  verfehle;  werde  verfehlt,  vermißt;  hinfällig;  tue  eine  Fehl- geburt'; sxal  ;Fehler;  Irrtum,  Mangel;  fehlerhaft,  mangelnd;  zu  wenig^, sxalak  ;taumelnd  (im  Rausch)'.
WF.  II  599;  ob  expressive  Bildung  zu  4.  (s)kel-?
{s)keni-  ;Verstümmelt';  auch  ;hornlos'.
Ai.  ^dmala-  n.  ;Fehler;  Schade';  aisl.  PN.  Hamall,  ags.  hamola,  ahd. hamal  ;A^erstümmelt'  (nhd.  ,HammeP)]  aisl.  hamla,  ahd.  hamalön  usw. ;Verstümmeln^;  mit  expressivem  -mm-:  aisl.  skammr^  ags.  ahd.  scamm ;kurz';  ahd.   hamm,  Kammer  ;Verstümmelt'.
WP.  II  560;  Holthausen  Awn.  Wb.  105;  dazu  auch  kem-   oben  S.  556.
{s)ken-{d-)  ;abspalten;   abgespaltene   Haut;   Schuppe,   Rinde';   (s)kend-no- ;Haut';  wohl  Erweiterung  von  sek-  ;Schneiden';   nur  kelt.  u.  german.
A.  Bret.  skant  KoUekt.  , Schuppen'  (*sk7}to-)j  abret.  anscantocion  PI.  ,in- squamösos*,  cymr.  ysgythru  , Schnitzen*  (*sken-tr-) ;
aisl.  skinn  n.  ,Haut,  Fell'  (*sken-to-j  urgerm.  *skinpa-j  vgl.  läpp.  Lw. skidde  und  runisch  ski[n]pa-leubaR ]  ags.  scinn,  engl,  skin  ds.  ist  Lw.  aus dem  Nord.,  ebenso  mnd.  schin  ,eine  Art  russisches  Ledergeld'),  mhd. schint  f.  ;Obstschale/  nhd.  Schind-mälire,  -aas,  ndl.  dial.  schinde  ,Haut, Fell;  Bast;  Rinde',  abgel.  Verbum  as.  hiscindian  , abrinden,  schälen',  ahd. scinten,  mhd.  mnd.  schinden  , enthäuten,  ausplündern,  mißhandeln'  (nhd. schinden  st.  V.);  aisl.  skän  f.  , Borke',  nisl.  auch  ,Häutchen',  mnd.  schin ,Schuppen  im  Haar'  (daraus  nhd.  Schinn,  Schinne),  mndl.  scheue,  dünne Haut;  Bast';
B.  daneben  idg.  (s)kend-  in:
air.  ceinn  , Schuppe,  Schale',  cymr.  cenn  (*kend-n-),  acorn.  cenn-en,  Häut-
59
930  f
chen,  Haut',  ysgenn  ,SchinnenS  mbret.  q^uenn  ,Haut*,  bret.  kenn  m.  ,Sclun^ nenS  -ken  ,Haut'  in  bu-gen  ,Rindshaut*  usw. ;  bret.  (Vannes)  skignan  ,FroscK^_. (*skenniano-)',  aisl.   hi7ina  f.  ,dünne  Haut,  Membrane'  (*skend-n-)'^
vgl.  mit  a-Vokalismus:  mir.  scaindrim  ,zerspalteS  scandrad,  scaindt^ jdispersion',  scainder  ,Gefecbt^
WP.  n  563 f.;  Lotb  RC.  41,  405 f.
skendh-  ,untertauchen' ;  nur  griech.  und  balt.
Gr.  axivd-ÖQ  ,untertauchend* ;  lit.  skestüj  sk^sti  ,untersinken,  ertrinke Kausat.  skandinüj  -dmti  ,ertränken';  apr.  auskimdlai  ,er  gehe  unter*. WP.  n  565,  Trautmann  265.
{s)keng-  ,hinken;  schief,  schräg'.
Ai.  sdkthi-  n.  (=  av.  Jiaxti-)  , Schenkel^  (*skak-thi-^  idg.  ^skT^g-ti-'^ -thi-  nach  ai.  dsthi-  ,Knocheu',  oben  S,  783);  khaüjati  ,hinkt'  (mind. *skanj-)j  khafija-  ,hinkend^,  khaüjana-  m.  , Bachstelze' ;
gr.  ay.d^o)  (nur  Präs.  und  Imp.)  ,hinke'  {*skngio)\  mir.  scingim  ,spring( ist  wohl  Umbildung  von  air.  scend-  _,springen^  (
```


## [2026-09-14T01:58:21.811Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"Stellholz\\|sescaind\\|Treppe,  Leiter\\|scäla\\|scala (\\*\" POK_03.txt | head; echo \"--- pages 916-921\"; for n in 154 155 156; do echo \"== leaf $n\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N' POK_03.txt | grep -n \"skand\\|91[6-9]\\|92[01]\" | head -6; done"
}
```


### [2026-09-14T01:58:22.921Z] TOOL RESULT

```
2138:got.  skalja  , Ziegel',  aisl.  skel  f.  , Schale',  ags.  sciell  f.  ,Hülse,  Muschel- schale', mnd.  schelle  L  , Schale,  Fischschuppe';  ahd.  scäla  ,Hülse,  Schale^,
2152:aksl.  Skala  ,Fels,  Stein^  (die   Bed.   ,Schale'   durch   Entlehnung  aus  abd. scäla  ds.),  sloven.  skdla  ,assula  tenuis;  Lichtspan*,  russ.  skalina  ^abgelöste      ] Birkenrinde';  sJcohka  ^Muschelschale'  (s.  oben  lat.  siliqua),  russ.  sceh  »Spalte«  V sloven.  Ualja  ,Splitter^,  poln.  skalic  sig  ,sich  spalten,  bersten';  \'.
3196:phd.  Sommersprosse-,  mnd.  sprüte,  md.  sprüze  ds. ;  ags.  spreo^  , Stange',  ndl. gpfiet  (daraus  nhd.  Spriet)-  norw.  spraut,  sprauta  , Stellholz  in  der  Falle*, ^proyta  , Fenstersprosse,  Spannstock  in  einem  Webstuhl;  ahd.  spriuzen gpreizen,  stützen,  stemmen^,  spriuza  ßpreize.  Stütze,  Strebe* ;
3540:ahd.  Steg  m.  ßteg,  kleine  Brücke';  aisl.  stigi  m.  , Stiege,  Leiter',  stig n.  , Schritt,  Stufe',  ags.  stige  ,das  Hinauf-  oder  Herabsteigen',  ahd.  stega ,Stufe, Treppe,  Leiter' (ahd.  stiega,  nhd.  Stiege  mit  e^,  also  wohl  aus  *st^ighä); ags.  sfceger  f.   ,Treppe'  (engl,  stair),  mnd.  Steiger  ,steil',  nid.   ,Ladeplatz'
5679:gr.  QÜitTü)  (*ßQa7riw,  *urp-)  ,nälie  zusammen,  flicke*,  ganlg  ,Nadel*  f»  k qacplg,  wie  Qaq)i^  ,Naht*  mit  cp  wohl  durch  Entgleisung);  ^inu)  ,bieo-e  mlek schlage  nach  einer  Seite  aus*,  Qorrrj  , Ausschlag,  Neigung',  druiQQortoc  «rlei  k! wiegend*,  dißcpiQqenrig  ,sich  auf  beide  Seiten  neigend*,  y.ala-vqo\b  (%cla fQOTC-)  , Hirtenstab*,  ösvqo  {^de-fQorc)  eig.  ,hierher  gewendet!*  66nala^ ,Wurfstab,  Knüttel',  qötctqov  ,Keule,  Türklopfer,  Stellholz  in  einer  Ftll  » ga^tlg  ,Rute,  Stab'  (vielleicht  3iuch.~  qocßSog  mit  ß  aus  p,  s.  oben  *v«rÄ.^* dehnstufig  QcJrtsg  PL  , Zweige,  Gesträuch,  Gebüsch*,  ^wnrjiov  ,Gebll«cli' Dickicht*;
--- pages 916-921
== leaf 154
13:916  ♦
== leaf 155
13:917
15:lit.  skaidrüs,  skdidrus  ,hell,  klar^;  lett.  skaldrs  ds.,  ,rein^;  lit.  skdistas, gjcaistüs  ,h.e\V  ]  anders  (zu  skeid-  unten  S.  921)  Trautmann  263.
== leaf 156
8:918  9
```


## [2026-09-14T01:58:34.180Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR>=155 && NR<=157' POK_03.txt | grep -n -i \"skamb\\|skand\\|sked\\|skai\\|918\\|919\" | head -20"
}
```


## [2026-09-14T01:58:34.940Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==156' POK_03.txt | sed -n '1,60p'"
}
```


### [2026-09-14T01:58:35.448Z] TOOL RESULT

```
4:Ai.  skabhnäti,  skabhnöti  , stützt',  Perf.  cäskdmbha ;  skabhäyati  ,hefestigt, stützt';  skambhd-  m.,  skdmbhana-m  , Stütze,  Pfeiler*,  av.  ujpaskambdm  ,unter Fesimsichen^ ^  fraskdmba-,  frascimbana-  , Tragbalken,  Pfeiler';  npers.  paSkam ,porticus',  sogd.  Sk'np-  (*skamb)  ,etage  de  Tunivers';
10:lat.  wahrscheinlich  caesius  ,yXavy.6g,  von  den  Augen'  (von  *kait-  oder *kaid-to-  aus,  vgl.  lit.  skdistas)  und  caelum  jHimmel'  {^kaid-lo-  oder  *kaid', *kait-slo-,  vgl.  mit  -r-Formans  dt.  heiter,  lit.  skaid-rils,  skdidrus)]
15:lit.  skaidrüs,  skdidrus  ,hell,  klar^;  lett.  skaldrs  ds.,  ,rein^;  lit.  skdistas, gjcaistüs  ,h.e\V  ]  anders  (zu  skeid-  unten  S.  921)  Trautmann  263.
28:918  9
29:ohne  s-  wohl  norw.   hlm,   hlma,  wie   skim  ^dünne  Decke,  Häutcheu'  fo .durchscheinend',  vgl.:)  aisl.  skjar  m.  ,durchsichtige  Haut,  Fensterrahaej^i, got.  sJceirs  ,klar',  aisl.  sklrr,  ags.  sclr  , durchsichtig,  hell,  rein*,  mhd.  (jj^A scMr  ,lauter^  nhd.  schier]  aisl.  skarr  ,rein,  klar^  {*skair{-r\  afries.  tkiril ,reinigen' ;
43:919
48:alb.  tshanj,  tsJiaj  , spalte,  zerreiße,  pflüge'  {*sked-nio)]  lat.  scindula,  scan- dula  f.  , Schindel' 5
50:lit.  skedervä  , Splitter^,  lett.  skedens  , kleines,  abgespaltenes  Holzstück' ; lit.  kedeti  ,berstenS  kedenti  ,zupfen.  Wolle  krämpeln';
53:I    sked'  , bedecken'?
```


### [2026-09-14T01:58:36.828Z] TOOL RESULT

```
ai-t~  in  arm.  xait''  ,stechen.  Stich*,  xait^em  , steche',  xit'^am  ,bin  ängst- lich', xit''  ,Betrübtheit,  heftiger  Schmerz';  dagegen  xio-t  ,stutzig,  ängstlich, argwöhnisch'  aus  *khid-ro-]
WP.  n  538,  WH.  I  44,  45,  129,  130,  131;  über  ai.  kUddti  ,reißt,  drückt* (9),  sekundär  khSdä  f.  ,Druck,  Last*  s.  J.  Wackernagel  Stud.  A.  Grierson, 826—28.
skäi-f  skQi-  :  ski-  ,gedämpft  schimmern ;  Schatten  (Abglanz)' ;  skiiä- ,Schatten';  ski-ro-  ,klar*.
Ai.  chäyä  , Glanz,  Schimmer,  Schatten*,  av.  a-saya-  ^wer  keinen  Schatten wirft',  np.  säya  , Schatten,  Schutz';
gr.  OKiä  f.  (shii-a)  , Schatten',  (7xt«^dg,  hom.  G%i6eLg  ,schattig,  dunkel*, GMQOv  ,Sonnenschirm'  (formal  =  alb.  hir,  mit  Länge  got.  skeirs);  mit der  Stufe  skä[i]-:ay,r]vrj,  dor.  ay,Civd  ,Zelt,  Bühne,  Szene',  a'/.rjvog,  dor.  oy.ä- vogn.  ,Zelt;  Leib  (als  Hülle  der  Seele)';  cx^v  ,Schmetterling,  Motte'  Hes.; amvaQ  n.  ,Leib';
alb.  he,  hie  , Schatten'  (*skiia),  hir  , Gnade'  (=  gr.  G'/Jqov),  {h)ona , Schatten'  (*5Ä;ei-7i- ?),  ^q^.  hüj  ,Gott*;
aisl.  ski  n.  ,Heuchelei'  (:  gr.  axid),  got.  skeinan  , scheinen,  leuchten, glänzen',  aisl.  sklna  ds.,  ahd.  ags.  sclnan  ds.,  nhd.  scheinen  (w-Präs.,  vgl. aksl.  singti]  ob  auch  in  lat.  scintilla  , Funke'  eine  Bildung  von  einem ähnlichen  Ausgangspunkt  aus  vorliegt,  ist  fraglich  (Ableitung  eines  *ski-nto- ,glänzend' ?) ;  aisl.  skln  n.,  as.  skln,  ahd.  sein  m.  ,Schein,  Glanz';  ags.  as. scima^  mhd.  scheme  ,Schatten',  nhd.  Schemen  , schattenhafte  Gestalt',  aisl. sJcimi  m.  , Glanz',  nhd.  schimmern,  Schimmel  usw. ;  got.  skeima  , Leuchte, Fackel*,  ahd.   as.   sclmo,   ags.   sclma  m.   , Licht,   Glanz';   mhd.   scheim  ds.;
918  9
ohne  s-  wohl  norw.   hlm,   hlma,  wie   skim  ^dünne  Decke,  Häutcheu'  fo .durchscheinend',  vgl.:)  aisl.  skjar  m.  ,durchsichtige  Haut,  Fensterrahaej^i, got.  sJceirs  ,klar',  aisl.  sklrr,  ags.  sclr  , durchsichtig,  hell,  rein*,  mhd.  (jj^A scMr  ,lauter^  nhd.  schier]  aisl.  skarr  ,rein,  klar^  {*skair{-r\  afries.  tkiril ,reinigen' ;
lett.  seja  (*keiä)  ,Schatten,  Spiegelbild,  Gesicht^;
aksl.   sijati,  singti  ,glänzen,  hell  werden^,   sem   , Schatten'   (neben  a^ für  *scSm)',   dech.  ciry  ,lauter^   russ.   sHryj  .wahrhaft,  echt'  (got.  Lw.j ksl.  *iiVT)  , offen',  Adv.  siry  usw. ;
toch.  B  skiyo  , Schatten*  (=  gr.  a^nd).
WP.  II  535  f.,  WH.  I  131,  Jokl  L.-U.  60  ff.,  Trautmann  304.
{s)kamh-  ,krümmen,  biegen'  und  (s)kemb-  ds.;  (s)kambo-  ,krumm'.   '
Gr.  aTidfißög  ,krumm,  krummbeinig' ;  air.  camb  ,krumm*,  cymr.  com. bret.  kämm  ds.,  gall.  in  Cambio-dünum  , Kempten*,  bret.  camhet  an  rot  , feige'   (*camb{ta)'j   schwundstufiges   *k7p,b-   , drehen   =   wenden,   wechsi tauschen*  und  , zusammendrehen,   fesseln'  in  gall.-lat.   cambiäre  ,wechs taus
```


## [2026-09-14T01:58:43.992Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==156' POK_03.txt | sed -n '40,75p'"
}
```


### [2026-09-14T01:58:45.118Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T01:58:47.160Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==156' POK_03.txt | tr '\\r' '\\n' | sed -n '25,60p'"
}
```


### [2026-09-14T01:58:48.262Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T01:58:52.815Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==156' POK_03.txt | grep -A8 \"bedecken\""
}
```


### [2026-09-14T01:58:54.045Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T01:58:56.512Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"bedecken\" POK_03.txt | head; echo \"---\"; sed -n '/sked.  , bedecken/,+12p' POK_03.txt | head -20"
}
```


### [2026-09-14T01:58:57.599Z] TOOL RESULT

```
442:V  -fo-Nomina  und  Verba:  ai.  putati  , umhüllt  mit',  puia-,  m.  n.  , Falte, Tüte,  Tasche'  (*puUa-),  mir.  alt  ,junctura,  artus'  (a  Redukt.  von  idg.  o, ^ie  vielleicht  auch  ai.  puta-),  redupl.  stark.  V.  got.  fal'pan  , falten',  aisl. falda  ,den  Kopf  bedecken',  ags.  fealdan,  ahd.  f alt  an  , falten',  schwach.  V. aisl.  falda  , falten',  ags.  fealdian,  ahd.  falton  ds.,  aisl.  faldr  m.  , Falte, Zipfel,  Kopfputz  der  Frau',  feldr  m.  (*faldi-)  , Mantel',  mhd.  valte  , Falte, "Windung,  Winkel' ;  got.  ain-falps,  ahd.  einfald,  -t,  aisl.  einfaldr,  ags. änfeald  ,  einfach'  u.  dgl.
1161:toch.  A  räk-,  rak-  ,hinbreiten,  bedecken',   B  7'äk-  ds.,  A  rkäl  , Decke'.
2060:I    sked'  , bedecken'?
2515:^,  {s)keu-,  (s)keu9  :(s)kü-  , bedecken,  umhüllen^,  auch  mit  zahlreichen Erweiterungen;  (s)kiI-lo-  .Versteck,  Hinterteil,  skü-ro-  , Schutz, Hülle^,  (s)kü-ti-  ,Haut',  ku-z-dho-  , Versteck,  Höhlung^
2946:Av.  snaoda-  , Gewölk',  südbaluci  nöd  ,leichtes  Gewölk,  Nebel,  Regj wölke*;  gr.  vv&öv  ^qtwvov.  oy.oxslv6v,  wd^wdsg'  a^iOTeivoJösg  Kes.]  lat ,Wolke',  dazu  ohnübö,  -ere  ,verhüllen'  (durchs  Perf.  obnühl  auch  fa von  nübö,  nupsl  ,heiraten*  scharf  geschieden),  u.  zw.  wohl  als  denomliii. tives  Verbum :  ,(sich)  bewölken'  =  ,(sich)  bedecken*,  zunächst  vom  HimmiL dann  allgemein;  cymr.  nudd  ,Nebel'  (zum  GN  Nudd  s.  oben  S.  768) ;Xi
3466:Ai.  sthagati  (umbelegt),  stJiagayati  ,verhüllt,  verbirgt';  gr.  arsyco  , decke, schütze  usw.',  arsyog,  leyog  n.  (=  air.  tecJi),  oreyr],  Tsyrj  f.  ,Dach,  Haus', CTsyavög  , deckend,  schirmend;  bedeckt,  versteckt',  areyrög  ,bedeckend, schützend;  bedeckt,  verschlossen;  kompakt,  fest,  dicht*  (s.  wegen  dieser Bed.  auch  *tegu-  ,dick'),  aTsy,TLy,ög  ,bedeckend,  schützend';
3467:lat.  tegöj  -ere  , decken,  bedecken',  tectum  ,Dach'  (=  arexrög),  tegulum ,Decke,  Dach,  Hülle',  teges,  -etis  , Decke,  Matte',  tegula  , Dachziegel',  toga ,Toga';  umbr.   tehtefim  ,tegimentum,  tectorium';
3471:aisl.  pekja  , decken',  ags.  peccan  , bedecken*,  ahd.  decchen^  ydeckenl^i^ rativ  Hogeiö  =  air.  tuigiur,  unter  Verdrängung  von  idg.  *tegö)',  aisL* *  ags.  dcec,  ahd.  dah  n.  ,Dach* ;  aisl.  pekja  ,DachS  ahd.  decchi  ,Z)ec^  D, ags.  Jbecen,  as.  thecina  ds.,  dazu  aisl.  staka,  stakka  f.  ,Fell*;  (ohne  t  qq^^ dial.  ^aÄ:a  , Schweinshaut');
4573:teu-  ,in  freudlichem  Sinne  die  Aufmerksamkeit  zuwenden,  aufmerken'. Lat.  tueovj  -eri,  tuitus  und.  tütätus  sum  ^betrachten,  beobachten,  schützen', \ntu[e)or  , betrachte',  ursprünglicher  in-,  ob-,  con-tuor  con-tuö',  tütus  ,sicher'; tir.  cumtüth  , Schutz'  (^kom-ud-touitus),  mcymr.  tud  , bedecken',  tuded,  Hülle, Kleid,'  bret.  dial.  tiiec  (abret.  *tudoc)  ,Kissenbezug' ;  air.  tüas-cert  ,nörd- lich',  bret.  tus  ,links'  (*teu-sto-) ;  kelt.  *teu-to-  in  mcymr.  tut  , Zauberer', Diir.  tüathaid  ds.,  air.  tüaith  , nördlich',  mir.  tüath  , links,  nördlich,  böse' (aus  ,*günstig,  gut'  als  Antiphrasis  zur  Bezeichnung  der  unglückbringenden Linken);  dazu  got.  piup  ,das  Gute',  aisl.  pydr  ,mild,  freundlich', ^^(fa , Freund- schaft', ags.  gedlede  ,gut,  tugendhaft',  gedledan  ,sich  (freundlich)  anschließen'; ^ohl  auch  ags.  deaio  ,Brauch,  Sitte',  as.  tJiau,  ahd.  gethau  , Disziplin'  als
5722:ndl.  wreeg  ,steif',  Subst.  ,Fußbeuge^,  aisl.  reigiask  ,den  Kopf  zurückwerfen, heftig  werden*,  aisl.  riga  f.  ,Biegung-,  riga  , bewegen*,  nisl.  rig  n.,  rigr  m. , Steifheit  in  den  Gliedern'  (aus  ,*yerrenkt*),  mhd.  rigen,  widerrigen  ,wo- gegen  ankämpfen,  widerstreben*,  nd.  iorigge{le)n  ^seitwärts  oder  hin-  und her  drehen^,  engl,  tonggle  ,sich  krümmen*,  nd.  uriggel  ,Eigensinn*,  norw. rigga  ,verbinden,  umwickeln;  erschüttern;  unsicher  gehend  rigla  ,wackeln, unsicher  gehen';  mhd.  Wc,  rickes  ,Band,  Fessel,  Knoten;  Geschlinge  der Eingeweide,  enger  Weg',  Schweiz,  rikch  , Heftel  von  Faden',  mhd.  ric  ,Hals* (wohl  als  ,*Dreher'),  mit  expressiver  Konsonantendehnung  der  Intensivität mengl.  nd.  ndl.  wrikken  ,hin  und  her  drehen,  rütteln,  wackeln^,  mnd.  vor- wrikken  ,verrenken',  norw.  (vjrikka,  schwed.  vrikka  ,verrenken,  wriggeln'; ndl.  gewricht  , Gelenk';  mnd.  lorist,  ags.  loristy  tvyrst,  aschw.  vrist,  aisl.  rist , Fußgelenk*,  mhd.  rist  ,Hand-,  Fußgelenk'  (*wri}ist-)]  ahd.  rlho  m.  ,sura, poples,  locus  corrigiae',  mhd.  rihe  ,Rist  des  Fußes',  nhd.  Reihen  ds.,  mndl. wrlghe,  ndl.  im^eeg  , Fußbiege';  mit  der  Bed.  ,umwickeln'  (:  lat.  rlcd):  ags. turlon,  wreon  {*wrllian)  , einhüllen,  bedecken,  schützen^,  wrigels  , Hülle',  ahd. int-rlhhen,  -rlhan,  Partiz.  intrigan  , enthüllen*,  mhd.  rigel  m.  ,eine  Kopf- bedeckung, die  man  umwindet';
---
I    sked'  , bedecken'?
I  Ai.  chadati  (unbelegt),  chäddyati  , bedeck,  verbirgt*,  chattra-m  , Schirm',
chadis-    n.    , Decke,    Dach' ;    av.    sädayantl-    ,ein    Kleidungsstück'    (skyth. Hose?),   afghan.   jpsöhl   ,to   put   on,   wear'   (*pati-upa-sad-)]   ahd.   häz  m., mhd.  häze  n.  ,Rock,  Kleidung',  ags.  liceteru  Nom.  PI.  n.  , Kleider'. WP.  II  558,  Holthausen  Altengl.  Wb.  146.
skei-  , schneiden,  trennen,  scheiden',  Erweiterung  von  sek-]  Anlaut  z.  T.  auch sk-,  skh-,  skh-,  wie  auch  in  den  Weiterbildungen  skai-to-,  skoi-to- ,Brett,  Schild';  skid{oi)-ro-,  skid-to-  ,gespalten'.
I.  Ai.  chyati  , schneidet  ab',  Partiz.  chäta-,  chitd-  , abgeschnitten',  Kaus. chäyayati  (mit  sä:-,  wie :) ;
av.  fra-sändm  , Zerstörung',  sä-,  sya-  , wehren' ;
gr.  (T%aw  (*skhdiö,  Impf.  IV^o»',  Inf.  xaror-d^av),  c^atw  (Neubildung, Schwyzer  Gr.  Gr.  1,  716)  ,ritze,  schlitze  auf^  und  ,lasse  fallen,  schlaff herabhangen,  hemme,  stehe  offen',  ox^^^^G  A^^  Ritzen,  Schröpfen;  Los- lassen*, GxciOf-iCi  n.,  GxaGiiog  m.  , Einschnitt',  GxaotrjQiov  ,Lanzette,  Riegel', GXaGTrjQla  ,das  (zur  Abtrennung  der  Zuschauer  dienende)  Seil  vor  der Rennbahn';
lat.  sciö,  sclre  ,in  Erfahrung  gebracht  haben,  wissen'  (,scheiden,  unter- scheiden'), desciscö,  -ere  , abtrünnig  werden,  sich  lossagen',  sciscö,  ere ,(durch  Abstimmung)  entscheiden,  beschließen,  verordnen'  und  ,zu  erfahren suchen',  plebucltum  ,vom  Volke  gefällte  Entscheidung',  scUus  , gescheit^ (wie  mhd.  geschlde,  nhd.  gescheit  zu  *skei-t-) ;
in  der  Bedeutung  , ausscheiden'  (vgl.  aisl.  sklta  unten  S.  921)
920  •
mir.  sceid  ^erbricht'  (*skei-{e-ti,  idg.  *skei-),  Verbaln.  sceith  f.  (aus  *scetl idg.  *s]ci-tä,  davon:)  cymr.  chwydu,  bret.  c^houeda,  mcorn.  htoeza  sj^v erbrechen^;  aus  ir.  scethach  ,zum  Brechen  reizend*  stammt  aisl.  skjadah  n ^Tauraellolch^  ;
mir.  scian  L  ,Messer*,  {*shiiena)  daraus  cymr.  ysgien  , Messer,  Schweif  • mir.  scallid  ,läßt  los,  zerstreut'  {*skdi-l-),  air.  erscatUud  ,Zerteilung*  j       ?-
aisl.  skeina  ,leicht  verwunden*;  als  ,*abgespaltenes  Holzstück,  u.  d»!.«. mhd.  schle  m.  f.  ,ZaunpfahP,  ags.  scia  m.  _,SchienbeinS  woneben  (vgl.  ah^  — - hiaibini  , Biene')  germ.  *ski-nö{n)  in  ags.  scinu  f.,  scine-hän  n.  , Schienbein*  '^ ahd.  scina  »Schienbein^  auch  ,NadelS  norw.  skina  ,kleine  Scheibe^;  afrie$ skidel  , Armknochen^  (-dla  Formans);  westfläm.  schier  , Holzblock*  {*ski-r(y)* von  ,*unterscheiden'  aus:  ahd.  skßrl  ,scharf,  scharfsinnig'  (*skeiro-)'^  ^hk, schier  , schnell',  Adv.  ahd.  skero,  skioro  ,schnell';  mhd.  schier (e)  ds.,  ,fast*'
```


## [2026-09-14T01:59:18.494Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; pdftoppm -f 452 -l 452 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg452 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg452.png"
}
```


## [2026-09-14T01:59:19.708Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== BQT v2 leaf 69 (p.609)\"; awk 'BEGIN{RS=\"\\f\"} NR==69' BQT_v2_pages.txt | head -40"
}
```


### [2026-09-14T01:59:20.318Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 63836 Sep 13 21:59 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg452.png
```


### [2026-09-14T01:59:21.592Z] TOOL RESULT

```
=== BQT v2 leaf 69 (p.609)
    ‫سس‬                                                                                             ‫چار تکبیرزدن‬

‫چار دیو ار صمرذات؟ ‪ -‬وکنابه‬                                                                        ‫‪١‬‏ ‪.‬‬       ‫هم هت‬
                    ‫‪. °‬‬    ‫از چهار حد دنا هم هت‬             ‫کنایه از ترك‬            ‫چار تکبیرردن ‏‬
‫جار دیو‌ار نف« کنانه از دلبا ‪-‬‬                             ‫کلی کردنوتبرای مطلق ازماوی نمودن‌باشد ‪.۴‬‬
                          ‫وقالب وجد ادمی باشد ‪.‬‬            ‫و کناه از نماز جذازه هم هت که بعد از آن‬
                                                                                             ‫میت را وداع کنند ‪۳‬‬
‫چارسو ‪ -‬بساین بی لقطه (‪ )۱‬بواو‬
‫رسیده » هر چیز را کوبند که چهار پپلو داشته‬                  ‫چار جو هر کنابه از عناصر اربع ‪-‬‬
‫فته اند که چهار بازار از‬‫وایرا نگیز‬‫باشد ‪ -‬ج‬                          ‫و چهار ستار لمش است از بنات النعش‪.‬‬
‫ناجامنشعب شوند ‪ - ۱‬وکناءه از انتظار کشیدن‬                   ‫چار دوال‪ -‬بنتح‌ارل وواوبالف کشید‪.‬‬
                                          ‫‪۰‬‬   ‫هت‬   ‫«م‬
                                                           ‫و بلام زده » چوبی باشد بمقدار بك فبشه که‬
‫چارطاق » باطای حطیبالفکشید‪.‬‬                                 ‫چاروا داران برسرآن سیخی کوچك بقدره‌همیزی‬
‫وبقاف زده » معروف است ‪ - ۷‬ولوعی از خیمةٌ‬                     ‫نصب لمایند وزنجیری با چند حلقه وچهار تمه‬
 ‫چهار کوشه هم هت که آنرا در عراق شروالی‬                     ‫بآرن تعبیه کنند والاغ وچاروا را بدان برانند‪.‬‬


                                                                               ‫‪.‬‬    ‫رت‪:‬ا‬
                                                                                       ‫چارک‬
                                                                                          ‫‪۱‬‬
                                              ‫‪ ۴‬من همان دم که وضو ساختم ازچشمةٌ عشق‬
       ‫«حافظ شرازی ‪.*۸۱‬‬              ‫ته‪.‬‬
                                       ‫س ک‬
                                         ‫هرچه‬
                                            ‫چار تکبیر زدم یکره بره‬
‫‪ - ۴‬ممنی اولی و اصلی همین است زبرا در مذهب اهل سنت در لماز میت چهار بار‬
       ‫تکبیر کویند ‪ .‬رك‪ :‬حافظ شیرین‪-‬خن بقلم نگارنده ج ‪ ۱‬ص‪۱۰۳‬و‪ ۹۰۳‬درشرح همین‌بیت‪.‬‬
      ‫دیوار جهان ‪.‬‬          ‫ر‬
                            ‫ا‪:‬‬‫چ_هرك‬                ‫که کردا کرد آن دبوار باشف‪.‬‬           ‫محوطه‌ای‬   ‫ك‬      ‫‪۴‬‬


                                     ‫‪.‬نانه از دنیا هم هت ‪:‬‬
                                                         ‫ک‬            ‫ند‬
                                                                       ‫گ‪0‬و‪726‬‬
                                                                            ‫‪ - ۱‬امروز ‪09‬‬
                ‫شکم چار سو کرده چون چاریای‪.‬‬                        ‫دربن چار سو چند سازيم جای‬
  ‫نظامی کنجوی‪ .‬ک«نجینه ‪44٩‬‏ ‪.‬‬
                               ‫‪ - ۷‬اطافی که در بالای صرای ها بر چهار ستون بنا کنند ‪.‬‬
```


## [2026-09-14T01:59:27.350Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport re\nt=open('BQT_v2_pages.txt',encoding='utf-8').read().split('\\f')\nfor i,p in enumerate(t):\n    if 'چادر' in p or 'چتر' in p:\n        print('leaf',i,'printed≈',i+540, p.count('چادر'), p.count('چتر'))\nEOF"
}
```


### [2026-09-14T01:59:28.502Z] TOOL RESULT

```
leaf 41 printed≈ 581 1 0
leaf 66 printed≈ 606 2 0
leaf 67 printed≈ 607 0 2
leaf 80 printed≈ 620 0 5
leaf 81 printed≈ 621 0 2
leaf 113 printed≈ 653 1 0
leaf 129 printed≈ 669 0 1
leaf 156 printed≈ 696 0 2
leaf 207 printed≈ 747 1 0
leaf 277 printed≈ 817 1 0
leaf 287 printed≈ 827 1 0
leaf 388 printed≈ 928 0 2
leaf 398 printed≈ 938 2 0
leaf 419 printed≈ 959 1 0
leaf 420 printed≈ 960 2 0
leaf 491 printed≈ 1031 0 2
leaf 501 printed≈ 1041 1 0
leaf 514 printed≈ 1054 0 1
leaf 532 printed≈ 1072 1 0
leaf 540 printed≈ 1080 1 1
leaf 557 printed≈ 1097 1 0
leaf 625 printed≈ 1165 1 0
leaf 627 printed≈ 1167 0 1
leaf 668 printed≈ 1208 0 1
leaf 679 printed≈ 1219 1 0
```


## [2026-09-14T01:59:34.410Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== leaf 66\"; awk 'BEGIN{RS=\"\\f\"} NR==67' BQT_v2_pages.txt | head -50"
}
```


### [2026-09-14T01:59:35.461Z] TOOL RESULT

```
=== leaf 66
  ‫‪ ۵‬ات‬   ‫مت‬
                                                                                                                ‫چاپلوی‬
 ‫جداگردیده را بکیوزبند ‪ ۵‬و آنرا بعریی صبره‬        ‫را یز کون دکه اکر‬                   ‫اسب رهواری‬               ‫و‬   ‫باشد =‬

                      ‫خوالند بضم صاد بی‌نقطه ‪.‬‬               ‫را غلط نکند ‪# ۱‬‬                     ‫راه‬
                                                                                                   ‫ننهن پدراو‬
                                                                                                            ‫ززبا‬
                                                                                                               ‫تا‬

 ‫چاچله ‪ -‬تمچی رمس وام ‪.‬کش‬
              ‫‪۶.‬‬
               ‫و بای افزار چرمی راگویند ‪٩‬‏ ‪#‬‬
                                                   ‫چاپلوس ‪ ۴۰‬بکون بای فارسی‬
                                                   ‫ولام بواومجهول کشیده و(‪ )۱‬بین بی‌اقطة زده؛‬
‫چادر ترسا = وطا وجامه ای باشدزرد‬                       ‫شخصیرا گوبند کهبچرب زبانی وسخنهای‌شیرین‬
‫و کبود درهم بافته ‪ -‬و کنابه از شفق و روشنابی‬      ‫وا بای‬
                                                       ‫و فروتئی کردن مردم را فریب دهد ؛ ب‬
                             ‫انتاب هم هت ‪.‬‬                                             ‫|جد هم آمده امت ‪.‬‬
                                                                                                       ‫ب‬

 ‫جادر کاقودی ‏ کنابه از سفیدی‬                           ‫کناوافو‪.‬‬
                                                               ‫وکو‬
                                                                 ‫‪ ۰‬چاہوك د بنم ثالث زس‬
                             ‫صبح صادق باشد ‪.‬‬                         ‫چست وچالاك وجلد راکوبند ‪. ۴‬‬
 ‫جادر کحلی = کتابه ازآسمان ‪-‬‬                       ‫‪۰‬‬    ‫بواو کشده‬     ‫با تای فرشت‬                ‫‪-‬‬     ‫جاتو‬

                         ‫وب تاريك است ‪*.‬‬
                                       ‫ش‬          ‫دزدانرا از حلق | ویزند‪.‬‬                   ‫ان‬    ‫رسمائی با‬
                                                                                             ‫بشددکه‬
‫جاذر لاجوره ‪ -‬کن‌ابه از آسمان‬
                                                       ‫‪۰‬م‬
                                                        ‫چاچ ‪ ۰‬بسکون جیمفارسی ن‬
  ‫است ‪ -‬و سبزه زار وموغزار را نگیوزنند ‪.‬‬
 ‫وین کرو‬                  ‫ار‬
                                                   ‫اشتهاردارد»‬   ‫که بتاشکند‬           ‫از ماوراءالنهر‬               ‫شهرست‬

                                                   ‫آجا‬
                                                     ‫یشغر گرفاته‌اند وکمان خوب از ن‬
                                                                                  ‫و کا‬
‫ووزه وامثال‬
          ‫آحك وکاسه ک‬
                    ‫که در آن خشت و‬                 ‫آورند ‪ -‬ومتسوب بناجا را چاچی گوبند عموما‬
‫آن پزاد ‪ -‬و مخفف چهار هم هت که بعربی‬              ‫و نوده غله پاك کرده وازکاه‬                     ‫وکمانرا وتا‬

                                                                         ‫‪.‬‬       ‫و‬    ‫‪- :‬‬    ‫چك‬      ‫(‪)۱‬‬



  ‫بکوهی در انداختن‪ .‬نظامیکنجوی‪.‬‬           ‫کمندی‬    ‫‪ - ۱‬ده چابك شد ابن چایکی تاختن‬
                       ‫‪ « 501086 _ ۴‬امفا ‪ ۲ :۱‬ص ‪ = ۵۷‬چابلوی = چالیوس ‪:‬‬
```


## [2026-09-14T01:59:45.172Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport re\nt=open('BQT_v2_pages.txt',encoding='utf-8').read().split('\\f')\nfor i in (65,66,67,79,80,81,82):\n    p=t[i]\n    lat=[l for l in p.split('\\n') if re.search(r'[A-Za-z]{3,}',l)]\n    print('=== leaf',i,'printed≈',i+543)\n    for l in lat: print('   ',l.strip()[:200])\nEOF"
}
```


### [2026-09-14T01:59:46.279Z] TOOL RESULT

```
=== leaf 65 printed≈ 608
    ‫‪aaa‬‬
=== leaf 66 printed≈ 609
=== leaf 67 printed≈ 610
    ‫منای‬         ‫بهلوی ‪rdc‬‏ (واسطه» راه ‪٠‬‏ كومك) لیر کف ‪۲‬‬    ‫‪ ۳‬ت‬          ‫‪:‬هار ‪.‬‬
=== leaf 79 printed≈ 622
    ‫=يلك (حم‪).‬‬‫‪ ۴‬چ‬             ‫در ارااء (لطانآ باد) ‪hsopãc‬‏ سن ممنی (مکی بواد)‪.‬‬
=== leaf 80 printed≈ 623
    ‫‪ = ۴‬چبین( ه‪.‬م‪ » ).‬طبری ‪ipac‬‏‬               ‫جاکرفتن و بافشار بدیگران جابی را اشغال کردن است ‪.‬‬
=== leaf 81 printed≈ 624
=== leaf 82 printed≈ 625
```


## [2026-09-14T01:59:53.588Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; timeout 300 python3 tools/ref_page.py BQT:609 --image 2>&1 | tail -40"
}
```


### [2026-09-14T01:59:54.732Z] TOOL RESULT

```
no scan of BQT covers printed page 609 (see 'scans' in refs_online.json)
```


## [2026-09-14T02:00:04.567Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8').read().split('\\f')\nprint(t[79][:4000])\nEOF"
}
```


### [2026-09-14T02:00:05.542Z] TOOL RESULT

```
 ‫یه‬                                                                                     ‫‪14‬‬


‫با کسی خود را یکی‬         ‫بچسبانشد ‪-‬‬     ‫بچیزی‬    ‫چیدار = با زای هوز بروزن مقراض »‬
                                                  ‫سر موزه راگوبند » وکآفنشی باشدکه مردم‬
                                                  ‫ماوراء النهر از بالای موزه پوشنده ؛ و با رای‬
‫‪ - ۴‬بفتح اول بر وزن کشش ‪۰‬‬          ‫چیش‬
                                                  ‫قرشت بروزن مقدار هم بنظر آهده است وبعربی‬
                                                                              ‫حرموق خوانند ‪.‬‬

                        ‫ونقیض گرفتن باشد ‪۰.‬‬       ‫حید آن = یکسر اول بروزن احسان ؛‬
‫چھل ‪ ۴‬ب=روزن کچل ک»سی راکوبند‬                            ‫بهمتی چیداز امت که سرموژه باشد ‪.‬‬
 ‫کرهاخبوجدیزهای ناشاسته| لوده کند ویوسته‬          ‫<مر د بروزن خطر ‪ ,‬خاله و دبواری‬
‫چر کن و نکبتی باشد چنانکه دسن او غثان‬             ‫باشد که ازچوب وعلف‌سازندا ‪ -‬وحلفه‌ودایره‌ای‬
                                                  ‫که از مردم وحیوانات دیگ رکشده شده باشل‬



                                                                          ‫ا‬
‫حیلاگه = بكر اول بروزن خشتك ‪.‬‬
      ‫یلید ومردار و بثاشابست آ لوده را گویند ‪3‬‬                        ‫که بند بافان و نواربافان‬
‫» مخقف‬    ‫موی‬     ‫جیلو سص‪ -‬بر وزن‬                                    ‫ابر شم و رسمان را‬       ‫تار‬

‫| چاپلوس است که زبان‌آور وفرببنده باشد ‪٩‬‏ ‪#.‬‬           ‫چهر‬           ‫بر آن کشند و هرمرتبه‬
‫و انی مشدد » کسی‌را‬   ‫= بفتح اول‬   ‫چیه‬
                                                   ‫ون‬
                                                    ‫اب‬
                                                     ‫که پود را بگنرانند آنها رابگردانند »‬
                                                              ‫قمم بند ونوار را چپربای گوبند ‪.‬‬
‫ومخفیف انی تخته‌ای باشد دستهدار بهأت سل‬
                                      ‫س‬            ‫چپسیدن ‪ = ۲‬باسین بی‌نقطه ‏ بروزن‬
            ‫کشتی بانان بدان کشتی رانند ‪.‬‬


  ‫‪ - ۱‬طبری ‪(282‬برچین) «سابطبری ‪ ۸۷۲۲۰‬گیلکی‌نیز ‪ 20۵0‬ه‪,‬چیر» درترکی‬
                      ‫بمعنی پرچیئیکه اگزون وچوب ساخته شده باشد » آمده «جفتابی ‪. ۳۸۲۰‬‬
                        ‫چضیدن‪.‬‬      ‫‪ = ۴‬چییدن («‪.‬م‪« ).‬اسفا! ‪ ۲ :‬ص ‪ 4۷‬و ‪۹۲۱۰‬‬
  ‫‪ « 056۳20 ۴‬اسفا ‪ ۷: ۱‬س ‪ ۰ ۷۰‬طبری ‪( 56۳۵6‬يزغالةٌ بکاله) «صاب طبری‬
  ‫=يلك (حم‪).‬‬‫‪ ۴‬چ‬             ‫در ارااء (لطانآ باد) ‪hsopãc‬‏ سن ممنی (مکی بواد)‪.‬‬

                                           ‫‪ ۵‬رك ‪ :‬چیل(ه‪.‬م‪: ).‬‬             ‫«اسفا ‪ ۲ : ۱‬ص ‪.۵۷‬‬
           ‫بیداد گرست و چیلك» بخرد ومت‪.‬‬            ‫بنشست‬     ‫دواری‬
                                                                 ‫ا انز ن‬
                                                                       ‫پجز‬
                                                                         ‫جو ب‬
                                                                            ‫هبر ک‬
    ‫«منوچهری بنقل جهانگیری ورشیدی»‪.‬‬
  ‫‪ « 20020 _ ¥‬هوشمان ‪ »0۳‬؛ چیه شدن؛‬                     ‫‪ - ۱‬رك ‪ :‬چاپلوی » چابلوی ‪.‬‬
               ‫یکو افتادن اتومبیل درحین حر کت ( اصطلاح رانند کان) ؛ رك‪ :‬چپسدن‪.‬‬

   ‫‪ #‬چپق ‪ -‬سم اول و دوم ازترکی«چوبوق»» درجغتابی بمعنی لولة چپق ‪ ,‬قطمه چوب‬
                                ‫فابل انمطاف » شاخ کوچك س‪«.‬بجفتابی‪121001010 .)۱۹۲‬‬

               ‫ی‬                    ‫فراسه از همینکلمة ترکیمأخون است‪ .‬آتلدتخین م رکب‬
                                                                             ‫از حقه‌ای ک‬
                                       ‫نلکیه در آن توتون ریزند بداسته ای چویین‬
                ‫جیق‬          ‫ومجوف کهاتهای آن بحقه متصل است و سر آنرا دردهان گذارند ‪.‬‬

                                                             ‫رك ‪ :‬چیق ‪.‬‬   ‫‪ #‬جو ق ‪-‬‬
```


## [2026-09-14T02:00:15.450Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8').read().split('\\f')\nprint(t[80][:4500])\nEOF"
}
```


### [2026-09-14T02:00:16.567Z] TOOL RESULT

```
 ‫‪YY‬‬                                                                                             ‫چیدن‪‎‬‬

‫وثالی مشدد بتحتانی‬     ‫طاول‬      ‫‪= ۴‬‬   ‫چیین‬           ‫بروزن کسدن‪ .‬میلکردن‬         ‫‪۲‬‬   ‫<ییلن‬


 ‫بجانب چپ ‪ -‬وکنابه از طرفی بطرفی دییگر | کشیده وبنون زده ‪ .‬طبقی‌را کویند که ازچوب‬
                              ‫بید وامثال آن بافند ‪.‬‬                              ‫کردیدن باشد ‪. ۴‬‬


                                              ‫بیان چهارم‬

               ‫در جیم فارسی باتای قفرشت‪ ,‬مشتمل بردوازده لغت کونایت‬
                   ‫کنابه از خورشید باشد‪.‬‬              ‫‪۱‬‬
                                                      ‫ی بفتح اول وسکون ثانی ورای‬             ‫جر‬
 ‫چتر سنمالی ‪ -‬کنابه از ماه شب‬                              ‫‪1‬‬          ‫‪۳‬‬
                                                                                            ‫قرشت» چتری‬
                             ‫چهارده (‪ )۱‬است (‪- )۲‬‬                                             ‫بشدرکاهی‬
                                                                                                     ‫با‬
 ‫جقر سیهیی ‪ -‬بمعنی چثر سدمابی‌است‬                                                      ‫محافظت آفتاب‬

 ‫چمر عثیر فن = کنابه از شب است که‬                                                      ‫نگاهدار ند ‪۵‬‬

                                ‫يیل خواننك ‪.‬‬
                                           ‫لرب‬
                                             ‫بع‬                                       ‫و موی کوتاهی‬
 ‫جتر کحلی د کنایه ازآسمان ات تج‬                                      ‫که مردان مرفرق سر گذارند ‪.‬‬
                  ‫برگ]ون کنایه ازآسان است‪ | .‬دابرسیاه را گیوزیند ‪.‬‬     ‫حت‬
‫چتر نور ک=نابه اازآناوبر است ‪.‬‬                                          ‫‪1‬‬
                                          ‫جتررور © کنانه از آفتاب عالمتاب‬
  ‫<چمو ‪ -‬بفتح اول و ضم انی سوکون‬                                                                  ‫‪.‬‬    ‫ت‬
                     ‫پرده‌ای باشد که مر روی‬   ‫وأو »‬                                     ‫‪,‬‬
  ‫‪۰‬‬    ‫چر‌ها پوشتث‬


        ‫‪e‬‏‬               ‫‪.‬‬         ‫زو‬                 ‫جر ر ر لن = بممنی چترروز است که‬
          ‫‪SG‬‏‬
‫چغوك(‪ )۳‬است که گنشکه باشده وبعر بیعسقور ‪.‬‬
                                                                              ‫کتابهابهااززآفت بهاب ابسافشد"‬

           ‫(‪)e‬‏ چش‪ :‬جفوك ‪.‬‬               ‫(‪ )۲‬چش ‪ :‬باشد ‪.‬‬           ‫(‪ )۱‬خم ‪ : ۳‬چهاردهم ‪.‬‬


 ‫‪ - ۴‬امروز چپیدن ‪ ,‬بععنی بزور‬              ‫‪٣‬‏ بدن (یسوند مصدری) ‪.‬‏‬        ‫‪.‬چ‬
                                                                       ‫مپ‪).‬‬  ‫‪( ۱‬از‬
                                                                            ‫ه‪:‬‬
 ‫‪ = ۴‬چبین( ه‪.‬م‪ » ).‬طبری ‪ipac‬‏‬               ‫جاکرفتن و بافشار بدیگران جابی را اشغال کردن است ‪.‬‬
                                                                        ‫(سبد) «ساب طبری ‪۰۸۲٩‬‏ ‪:‬‬
              ‫همان‌نان کشکین به‌یش‌اندرشی‪.‬‬                     ‫مجیین‪ .‬در افکند فا گه‪:‬سرش‬
   ‫فردوسی طوسی‪.‬دلفت فرس ‪.*۹۷۳‬‬
  ‫‪ - ۴‬مانسکریت ‪ 4۳0020126‬ازرتة ‪( 020‬پوشاندن) ‪ ( ۲-2۲1‬پسوند پمعنی وسیله‪ ,‬کننده) ؛‬
      ‫وحلهٌ یوتاندن» حفاطت؛ چترآفتابی» آفتاب گیر؛ ‪6‬و‪( 5201201‬درفش‌شاهی) «وبلیامز ‪٤٩٤:۱‬‏ *‪.‬‬
          ‫(برهان قاطع ‪)۳۸‬‬                                                      ‫مه در مفعةٌ ‪۳۱٩‬‏‬
```


## [2026-09-14T02:00:31.310Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8').read().split('\\f')\nfor i in (65,66,67):\n    print('##### idx',i)\n    print(t[i][-2500:])\nEOF"
}
```


### [2026-09-14T02:00:32.633Z] TOOL RESULT

```
##### idx 65
         ‫که خمیرآ را با‬                ‫وآن برکی است که از چين وخطا آورند و در‬
                                           ‫پر لد‬    ‫آب جوشانده مانند قهوه خورند‪ ,‬وخاصت آن‬
 ‫چا بك ‪ = ۲‬بصم بای ابجد و سکون‬                     ‫روت شراب رادف عکند ‪ .‬گوبند‬    ‫ضست‬
                                                                                   ‫مار ا‬
                                                                                       ‫بسب‬
    ‫ت‬
    ‫چو‬‫چفافبوك است که جلد‬
                       ‫کاف » مخ‬                    ‫مردم تبت ببب آنکه شراب بيار میخورند‬
‫تازبانه همآمده‬      ‫ع‪-‬‬
                   ‫نی‬ ‫ماشد‬
                         ‫یب‬‫وردف‬
                              ‫ولاك وظ‬
                                    ‫ا‬              ‫وعرب آن صا ‪۴‬‬ ‫ند م‬     ‫رشك‬
                                                                           ‫خت م‬
                                                                              ‫یقیم‬
                                                                                 ‫مرا ب‬
                                                                                     ‫آن‬
                                           ‫ات‬                                         ‫باشد ‪.‬‬

 ‫چابکی ؟ ‪ -‬بمعنی جلدی وچالاکی‬                      ‫جابانی » با بای فارسی و نای‬
                                             ‫‪aaa‬‬



                                                                    ‫‪ :‬و ٿا‪.‬‬   ‫(‪)۱‬چك‬



  ‫٭‪(- €#‬ج بکس » جیم فارسی) حرف هفتم از الفبای فارسی است ‪ .‬در زبان عرب‬
  ‫دارند ‪ .‬وآن‌گاه به ”ش‪٣‬‏ و گاه به « ز >‬     ‫وجودندارد ودر حاب جمل ماد جم آبرا سه مصوب‬

   ‫به «» » ودرتعریب ب«هص» و «ش» تبدبل کردد‬          ‫)ه‬
                                                     ‫گا‬‫ولف‬
                                                         ‫بدل شود ( رك ‪ :‬ص بح دبباچة مۇ‬
                                                              ‫مانند چغانی » صغانی و شفالی ‪.‬‬
          ‫‪ - ۴‬معرب چای «صای» و «شای» امت ‪ .‬رك ‪ :‬چای ‪.‬‬     ‫رك‪ :‬چای ‪.‬‬  ‫‪۱‬‬

   ‫؟ ‪ -‬پهلوی ‪ 60۳86‬ابرانی‌باستان‪ ۵ 26-1۳26-‬ارمنی ‪ ۰‬ع کلقا‪(8‬قابل‌انستاء‬
   ‫نرم » زرنگك) ‏ دیز ارمنیع ‪( ۳60‬شتاب) «ییبرك ‪۲٤٩‬‏ « مسینا ‪ « ۷۳۱۷‬افا ‪ ۱ :۱‬ص‪ ۹۷۲‬؛ ‪۷‬‬
  ‫ص ‪ ۱۸۱‬ورك‪ :‬چابوکه ‪« :‬منافم سفر ‪ ...‬يطناجیفه راست ‪ :‬لضتین بازر گانیکه باوجود‬
       ‫نعمت و مکنت غلامان کونیزکان دارد دلاویز وشاکردان چابك ‪« ».‬کلتان ‪. ۳۱۱-۸۱‬‬
                                   ‫‪ . ۴‬ازچ‪:‬ايك (هم‪ + ).‬ی (مصدری) ‪.‬‬

##### idx 66
.‬‬
 ‫وین کرو‬                  ‫ار‬
                                                   ‫اشتهاردارد»‬   ‫که بتاشکند‬           ‫از ماوراءالنهر‬               ‫شهرست‬

                                                   ‫آجا‬
                                                     ‫یشغر گرفاته‌اند وکمان خوب از ن‬
                                                                                  ‫و کا‬
‫ووزه وامثال‬
          ‫آحك وکاسه ک‬
                    ‫که در آن خشت و‬                 ‫آورند ‪ -‬ومتسوب بناجا را چاچی گوبند عموما‬
‫آن پزاد ‪ -‬و مخفف چهار هم هت که بعربی‬              ‫و نوده غله پاك کرده وازکاه‬                     ‫وکمانرا وتا‬

                                                                         ‫‪.‬‬       ‫و‬    ‫‪- :‬‬    ‫چك‬      ‫(‪)۱‬‬



  ‫بکوهی در انداختن‪ .‬نظامیکنجوی‪.‬‬           ‫کمندی‬    ‫‪ - ۱‬ده چابك شد ابن چایکی تاختن‬
                       ‫‪ « 501086 _ ۴‬امفا ‪ ۲ :۱‬ص ‪ = ۵۷‬چابلوی = چالیوس ‪:‬‬
              ‫که بته بود چاپلوی از فسوس‪.‬‬      ‫مکن خوبشتن سهمگن چاپلوی‬
        ‫ابوشکور بلخی‪« .‬لفت فرس ‪4۹۱‬؟‪.‬‬
  ‫« چاج » احبتی‌است بزرك وآبادان ومردمانی غازی‌پیشه‬              ‫‪۴‬‬               ‫‪.‬‬   ‫چابك‬    ‫‪:‬‬    ‫رك‬       ‫‪۴‬‬


  ‫» وار وی کمان وتر خدنگو چوب‌خلنج بار افند ‪« ».‬حدود‬                 ‫وجنگ فگر وتوانگر وسار تعمت‬

                                ‫بدان چاچی أست‪:‬‬     ‫و موب‬         ‫و معرب آن الشاش |‬                             ‫العالم ‪۶‬‬

              ‫بخم چون کمان کوشة چاچیان‪.‬‬
         ‫نکظانمجیوی‪« .‬گنجینه ‪.64‬‬                                             ‫‪۰‬‬       ‫چش‪‎‬‬    ‫رك‪:‬‬        ‫*‬


              ‫که زرین کی سندل و چاچله ‪.‬‬                ‫‪ ۱‬گ‪-‬رفتم که جابی رسیدی زمال‪‎‬‬
      ‫عنصری بلخی«لفت فری ‪.>۱۳۳‬‬
‫چ‪#‬اپ ‪-‬کالزمةٌ هندی ‪ »8‬مأخوذ است ؟‬
    ‫طبع ‪.‬کشت با وسم و صوبری وسطچ*اماپتاینر متتصوی ‪ -‬هیا ‪ -‬دروغ[ وکی‬
                                                           ‫‪#‬ایلوس ‪ -‬رك ‪ :‬چایلوی ‪.‬‬
                                                                                ‫چ‬

  ‫‪-‬رکی ؛ يبك ‪ .‬فاصد نامه بر ؛‬                            ‫ایزبدین ممنی است) ‪ « .‬جفتابی ‪.> ۰۷۲‬‬
                       ‫‪ #‬چاچی ‪ -‬منسوب به« چاج » ( « ‪ .‬م ‪).‬‬                                  ‫‪ :‬یام ‪.‬‬        ‫برید ‪ .‬رك‬

 ‫تح ‪ 3‬کسردال (وامروزضم‌دال تلفظکننداس چانر( بفتح‌ذال)‪ .‬روسى ‪t2 6‬‏ ‪hS‬‬
                                                                     ‫‪ #‬چادر = ش‬
  ‫حرهٌ ‪4۰٩‬‏‬
          ‫فد‬‫صبه‬
              ‫بق‬

##### idx 67
زدها‪ -‬بمعثی اول چارآ خراست‬
‫جار بند ۔ بروزن آبکند‪ .‬کنابه ازدیا‬
                                                                              ‫که عناصر اریعه باشد ‪.‬‬
                                  ‫‪#‬‬   ‫وعالم باشد‬
                                                      ‫چار استاد = کنابه از چپار عنصر‬
 ‫جار بهلو شدن ‪ -‬کنانه از دزی‬
                                                                                                 ‫سنج‬
             ‫بسیار خوردن و بر پشت خوابیدن باشد ‪.‬‬     ‫یا بای فارسی بالف کش ده»‬      ‫چار با‪۳‬‬

‫چار لیخ» بروزن چارمیخ » بیخ‌کاسنی‬                     ‫بروزن و معنی چاروا است که مر کب سواری‬
‫و بیخ رآزبانه و بیخکبر و بخ کرفس را گوباد‬            ‫باشد هم‌جو اسب و استر و خر و شتر و امثال‬
‫ویعربی اصول‌الاریمه خوانند ‪ -‬و کنابه ازچهار‬

‫چار تا‪ -‬با فوقالیبالف کشیده ‪ .‬طنبور‬
 ‫پارعنصر‬
       ‫چز‬‫و رباب چهارتار راگونند ‪ ۹‬و کنانه ا‬

‫وا‬‫ت باعتبار چهار ر کن ؛ ب‬‫هیاسهم‬
                              ‫وعالم ودن‬
‫زبادتی رای‌فرشت بروزن خکاار لیزهمین حعنی‬
                                      ‫جد‬    ‫دارد ‪۸‬‬
 ‫بر وزن ماه باره ‪ .‬می‬        ‫جار تاره =‬

‫ور سازی که‬
         ‫چارنار است که طنبور و رباب ه‬
‫برآن چهار تار بندند‪ -‬کونابه از عناصر‪ -‬و دنا‬
  ‫منای‬         ‫بهلوی ‪rdc‬‏ (واسطه» راه ‪٠‬‏ كومك) لیر کف ‪۲‬‬    ‫‪ ۳‬ت‬          ‫‪:‬هار ‪.‬‬
                                                                             ‫چ‬
                ‫‪٩46‬‏ از اوستا ‪ « 81۵0‬بارتولمه ‪ . »6۸۵‬رک ‪ :‬چاره ‪:‬‬      ‫ودس‪.‬ت‬
                                                                          ‫‪« »۲: ۰‬میلو خر‬
             ‫زن جوبد که اوراجت بايد تیزچار‪,‬‬
                                          ‫چاره آ‬          ‫بلبل دستان زن چاره همی‌جوید زمن‬
  ‫‪۰۱٩‬‏‬        ‫حرهً‬
                 ‫صهف د‬
                     ‫ی‬                           ‫‪.‬‬   ‫‪ ۵‬لفت فری ‪۹۵۱‬‬


                                                                                 ‫حه ‪۸۰٩‬‏‬‫صبهفاز‬‫بق‬
  ‫فریز دی ‪۲‬ا‪ 40‬برنی ‪ ,۲8086‬نطنزی‪2.۱« ۲11۷26‬ص‪ .۱۹۲‬اسمنانی‬                        ‫«اسفا ‪۱ :۱‬ص ‪۵۷۲۲‬‬
  ‫» سرخه‌بی ‪ , ۲10426‬لاسگردی ‪ , 76026‬شهمیرزادی ‪۲ .« 0020‬ص ‪ » ۲۸۱‬لیز‬                                ‫‪۳‬‬
   ‫شهمیر زادی ‪٣‬لا‏ ك ‪ ۲ .‬ص ‪ ۹۷۱۰‬ک»یلکی ‪.۲8086‬ساس کرت ‪٩( ۲21200‬‏ چترشاهی‪,‬درفش‬
  ‫شاحی) ‪ (۰2۳04821‬چتر)از ‪( 042016‬پوشاندن) « وبلیامز ‪٤۰٤:۱‬‏ » « دکترراجا » ورك‪ :‬شادروان‪.‬‬
         ‫‪۱‬‬                 ‫معرب آن‌شوذر (بفتح‌ارلوسوم) «نفی»؛ خیمه ‪ ۰‬سایان » بالاپوش زنان» ردا‪.‬‬
```


## [2026-09-14T02:00:49.524Z] TOOL CALL #34: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 3
}
```


### [2026-09-14T02:00:49.531Z] TOOL RESULT

```


```


## [2026-09-14T02:00:52.801Z] TOOL CALL #35: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A7%D8%B3%DA%A9%D9%84%D9%87",
 "prompt": "Give the full Persian etymology section for اسکله (eskele) — what language it is borrowed from (Turkish? Arabic? Italian?), and the chain back to Italian/Latin scala."
}
```


## [2026-09-14T02:00:54.272Z] TOOL CALL #36: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/iskele",
 "prompt": "Give the Turkish etymology of iskele: source language (Italian scala? Greek?), meaning, and any note about Arabic إسكلة and Persian اسکله borrowings."
}
```


### [2026-09-14T02:00:56.329Z] TOOL RESULT

```
# Persian Etymology for اسکله

Based on the Wiktionary entry, here's the etymological chain:

The word اسکله (iskala/eskele) was "Borrowed from Ottoman Turkish اسكله (iskele), from Italian scala."

So the etymological path is: **Italian scala → Ottoman Turkish iskele → Persian اسکله**

The entry does not provide information about Latin origins or any intermediate steps beyond these three languages. The ultimate source is the Italian word for "ladder" or "scale," which entered Persian through Ottoman Turkish as a loanword.
```


### [2026-09-14T02:00:57.464Z] TOOL RESULT

```
# Turkish Etymology of "iskele"

**Source Language:** Italian

**Origin:** The word "iskele" is "inherited from Ottoman Turkish _iskele_, from Italian _scala_."

**Meaning:** Italian "scala" means "ladder" or "staircase," which evolved into the Turkish term for a wharf, pier, or dock—essentially a structure for accessing ships.

**Note on Other Borrowings:** The provided Wiktionary article does not discuss Arabic إسكلة or Persian اسکله borrowings. The etymology section only traces the word back to Italian through Ottoman Turkish, with no mention of potential Semitic or Persian language connections.
```


## [2026-09-14T02:01:04.629Z] TOOL CALL #37: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/scandalum",
 "prompt": "Latin scandalum etymology: from Ancient Greek skandalon; and what does it say about the Greek word's origin (root *skand-)? Also list descendants (Old French escandle/scandale, English scandal)."
}
```


## [2026-09-14T02:01:06.282Z] TOOL CALL #38: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/scandal",
 "prompt": "Etymonline on scandal: full chain Greek skandalon 'trap, snare, stumbling block' → Late Latin scandalum → Old French escandle/scandale → English; and the PIE root given (*skand- 'to leap'?). Quote the key sentences."
}
```


### [2026-09-14T02:01:09.566Z] TOOL RESULT

```
# Etymology of Latin "scandalum"

**Origin:** Latin *scandalum* derives from Ancient Greek *σκάνδαλον* (skándalon), meaning "a trap laid for an enemy, a cause of moral stumbling."

**Greek Root:** The Greek term may derive from the Proto-Indo-European root *\*skend-*, though this connection is marked as uncertain in the etymological record.

**Key Definitions:** The Latin noun carried meanings including scandal (moral sense), temptation to sin, stumbling block, and trap.

**Notable Descendants:**

- **Old French:** *esclandre* → evolved into English *slander*
- **French:** *scandale* → spread to numerous European languages
- **English:** *scandal* (directly from French influence)
- **German:** *Skandal*
- **Spanish/Portuguese:** *escándalo/escândalo*
- **Russian/Bulgarian/Ukrainian:** *скандал* (skandál)

The word demonstrates extensive linguistic diffusion across European languages, primarily through French mediation after the Norman period.
```


### [2026-09-14T02:01:11.685Z] TOOL RESULT

```
# Etymology of Scandal

The word "scandal" traces through several languages with a consistent core meaning related to offense and transgression.

**Greek Origin:**
"From Greek _skandalon_ 'a stumbling block, offense; a trap or snare laid for an enemy.'"

**Proposed PIE Root:**
The text suggests it may derive from "PIE _\*skand-_ 'to leap, climb,'" though scholars remain uncertain about this connection.

**Romance Language Path:**
The term traveled from Late Latin through Old French: "from Late Latin _scandalum_ 'cause for offense, stumbling block, temptation'" to Old French forms before entering English in the 1580s meaning "damage to one's reputation."

**Biblical Significance:**
The Greek noun appears prominently in religious texts as "cause of moral stumblings," suggesting the metaphorical sense of a spiritual obstacle developed early in Christian usage.

The progression shows how a concrete image (a physical trap or snare) evolved into an abstract concept denoting reputational harm and moral offense—a semantic shift reflected across multiple language families.
```


## [2026-09-14T02:01:17.930Z] TOOL CALL #39: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/escalator",
 "prompt": "Etymonline on escalator: origin (trademark 1900, from escalade / Latin scala), and what it says about escalade and scale (n.3 'ladder'). Quote key sentences."
}
```


## [2026-09-14T02:01:19.646Z] TOOL CALL #40: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/ascenseur",
 "prompt": "French ascenseur: etymology (from ascendre / Latin ascensor, ascendere), meaning 'elevator/lift', and any listed descendants in other languages (Persian, Turkish, etc.)."
}
```


### [2026-09-14T02:01:22.289Z] TOOL RESULT

```
# Etymology of Escalator

**Origin as Trademark (1900):**
"1900, American English, trade name of an Otis Elevator Co. moving staircase, coined from escalade + -ator in elevator."

The word combines "escalade" (meaning to climb using ladders) with the suffix "-ator" (as in elevator) to create this trademarked brand name.

**Connection to Escalade:**
Escalade derives from French and Italian roots meaning "to climb by means of a ladder," ultimately tracing back to Latin *scala* meaning "ladder" and *scandere* meaning "to climb."

**Key Related Term:**
The entry notes that "escalate" was later created as "a back-formation from escalator" in 1922, originally meaning "to use an escalator," before evolving into its modern figurative sense of raising or intensifying something (attested by 1959).
```


### [2026-09-14T02:01:25.515Z] TOOL RESULT

```
# Ascenseur: Definition and Etymology

**Ascenseur** is a French noun (masculine, plural: ascenseurs) with two primary meanings:

1. An elevator or lift
2. A scroll bar (in computing contexts)

## Etymology

The word derives from Latin *ascēnsor*, itself built from *ascendō* (to climb). As the entry notes, this represents "a learned borrowing from Latin." The Latin root traces back through Proto-Italic *skandō* to the Proto-Indo-European root *skend-* (meaning to climb or ascend).

## Global Influence

The French term has spawned numerous descendants across languages, demonstrating its widespread adoption:

- **Turkish**: asansör
- **Spanish & Romanian**: ascensor
- **Persian**: آسانسور (âsânsor)
- **Khmer**: អាស់សង់ស័រ
- **Arabic variants**: Including Moroccan Arabic *sansūr*

The word's journey from Latin through French into dozens of languages reflects the French influence on modern elevator terminology worldwide.
```


## [2026-09-14T02:01:30.314Z] TOOL CALL #41: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A7%D8%B4%D9%84",
 "prompt": "Is there a Persian entry اشل (ešel)? Give its etymology (French échelle?) and meaning (scale, pay scale)."
}
```


## [2026-09-14T02:01:31.727Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%C3%A9chelle",
 "prompt": "French échelle: etymology (Old French eschele/eschelle, from Latin scala), meanings (ladder, scale), and descendants borrowed into other languages (Persian اشل? Turkish? English echelon?)."
}
```


### [2026-09-14T02:01:32.201Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-14T02:01:37.245Z] TOOL RESULT

```
# Échelle: French Word Overview

**Échelle** is a French noun (feminine) with multiple related meanings:

1. **Ladder** — the physical object used for climbing
2. **Scale** — referring to proportion, size, or measurement
3. **Figurative ladder** — as in a hierarchical structure (e.g., "corporate ladder")
4. **Musical scale** — in musical contexts

## Etymology

The word traces back through Old French _eschale_ to Latin _scāla_. It shares a linguistic relationship with the French word _escale_, making them doublets of the same origin.

## Notable Usage

According to a 1961 Georges Simenon passage, the term can describe runs in stockings: "she should have asked her companion to wait for her for a moment so she could go down to the toilet" to address this fashion concern.

The word appears in several compound expressions, including _à grande échelle_ (on a large scale) and references to scientific scales like the Richter scale (_échelle de Richter_).
```


## [2026-09-14T02:01:45.981Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%A7%D8%B4%D9%84/",
 "prompt": "Quote the فرهنگ معین (Mo'in) entry for اشل — including the origin tag in brackets (e.g. [فر.]) and the definition. Also any Dehkhoda note on its origin."
}
```


## [2026-09-14T02:01:48.005Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%A7%D8%B3%DA%A9%D9%84%D9%87/",
 "prompt": "Quote the فرهنگ معین (Mo'in) entry for اسکله — including the bracketed origin tag (e.g. [ایت.] Italian, [فر.] French, [تر.] Turkish, [ع.] Arabic) and the definition. Also quote any Dehkhoda etymological note."
}
```


### [2026-09-14T02:01:52.139Z] TOOL RESULT

```
# Mo'in Dictionary Entry for اشل

According to the فرهنگ معین (Mo'in Dictionary), اشل has two main definitions:

**First meaning** (marked with [ع.] for Arabic origin):
"(اَ شَ ) مردی است که دست او شل باشد، آن که دستش معیوب و از کار افتاده باشد" — referring to a person whose hand is paralyzed or disabled.

**Second meaning** (marked with [فر.] for French origin):
1. "امتیاز کارمند از نظر درجه و مقام اداری و دریافت حقوق، پایه، رتبه" — the rank or grade of a government employee regarding salary classification.
2. "رابطة میان اندازة واقعی چیزی با اندازة نقشه و نمودار آن، مقیاس" — the proportional relationship between actual measurements and their representation on plans or diagrams.

The **Dehkhoda note** on origin explains that the French term *échelle* entered Persian usage and became employed in Persian with these meanings, derived from the French source.
```


### [2026-09-14T02:01:53.811Z] TOOL RESULT

```
# Mo'in Dictionary Entry for اسکله

According to Farhangi Mo'in:

"(اِ کَ یا کِ لِ ) [ معر. ] (اِ. ) در اصل ایتالیایی به معنای بندر، بارانداز کشتی"

**Translation:** The entry indicates this is a borrowed term [معر. = mu'arab/borrowed] from Italian, meaning "port" or "ship's cargo dock."

**Dehkhoda Etymology Note:**

The Dehkhoda dictionary traces the word to Italian origin: "( از ایتالیایی اسکالا )" — from Italian "scala" — and provides alternative Persian forms including اسقاله, سقاله, and اصقالة, while cross-referencing related maritime terminology.
```


## [2026-09-14T02:02:04.828Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== TAD اسكلة\"; grep -n \"سكلة\\|اسكل\\|إسكل\" TAD_pages.txt | head -10; echo \"=== TAD leaf count\"; grep -c $'\\f' TAD_pages.txt"
}
```


### [2026-09-14T02:02:05.882Z] TOOL RESULT

```
=== TAD اسكلة
222: ‫إسكلة ‪ -‬ايطالي مادء‪ 5‬وهو معدول عن ‪ 38‬أى دراج وبراد به طالسةن‬
225:‫أ وفى اللاتينية ‪151010111‬قن‪ 5‬معناء مقعد‬   ‫إسكمله ‪7-3‬رى د اسكله »> فنا‬
=== TAD leaf count
85
```


## [2026-09-14T02:02:06.376Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== LKT skala/iskele\"; grep -n -i \"iskele\\|scala\\b\" LKT.txt | head -10; echo \"=== DEV echelle\"; grep -n -i \"échelle\\|eschelle\" DEV.txt | head -5; echo \"=== PHN\"; grep -n -i \"échelle\\|escale\" PHN.txt | head -5"
}
```


### [2026-09-14T02:02:06.460Z] TOOL RESULT

```
=== LKT skala/iskele
=== DEV echelle
1700:De  ce  mot  vient  l'espagnol  mazmorra,  cachot,  fosse, prison.  On  peut  voir,  dans  la  Relation  du  sieur  Mouette"^, qui  fut  captif  au  Maroc  de  16-70  à  1681,  la  description de  la  mazmorra  où  on  le  renfermait  la  nuit  avec  les  autres esclaves  :  ^^  C'étaient  de  vrais  silos  creusés  sous  terre  .  .  . on  faisait  descendre  les  esclaves  dans  ce  trou  par  une échelle  de  corde.  ??
=== PHN
2661:en usage dans les échelles du Levant pour désigner Yexequatur
3396:les échelles du Levant. Les Provençaux font un usage fréquent
4221:'j^ [daradjal] prf^rression; marche d'un escalier; échelle; degré
4437:dans les échelles du Levant, pour l'interprétation des diverses
```


## [2026-09-14T02:02:11.174Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('TAD_pages.txt',encoding='utf-8').read().split('\\f')\nfor i,p in enumerate(t):\n    if 'إسكلة' in p or 'اسكلة' in p:\n        print('leaf',i)\n        print(p[:1500])\n        break\nEOF"
}
```


### [2026-09-14T02:02:12.568Z] TOOL RESULT

```
leaf 6
‫معاه أخبار تارمحية وقد استعمابا العرب ععى‬           ‫اساطير ‏ بوناني ‪8‬‬
                                                            ‫خرافات وحكابات‬
                                     ‫استبرق ‪ -‬فارسي معناه الديباج الغديظ‬
                                   ‫اسرب ‪ -‬فارسي «سيرب» معناه رصاص‬
        ‫إسطيل واصطيل ‪ -‬لاتيني ‪#‬دااناطهاة معناه مأوى الخيل والدواب‬
‫خا لان | رانم كن من ‪ 807653‬أى ك كب وهلاةطه‪:‬ذا أُخذ وكان‬
 ‫الفلكيون القدماء يعرفون حركة الكوكب مبذه الآلة ويعينورن موضعه‬
                                                             ‫ويعيسون ارتقاعه‬

                       ‫يونالي تاواع ‪ 1015‬معئاه عنصر وأعيل‬     ‫ب‬
                                                                      ‫د‪5‬ي‬
                                                                        ‫‪95‬‬

                    ‫معتأد عله حربية وطائفة سفن‬      ‫اسطول ‪ 8-3‬وناني ‪8‬‬


‫ملدابةمرادفهمودوقابمة‬
                    ‫اسطوانة ‪ 5-3‬فارسي ‪ 0‬أستون « هماه دعامة وقوات ا‬


                                                            ‫ايضا فيالطبيعيات‬
‫نحري جسمه متخلخل‬          ‫اون‬
                            ‫و وه‬
                               ‫ينعصر‬
                                   ‫حه م‬
                                      ‫معنا‬          ‫إمفنج ‪ -‬يوناني ‪5‬‬



‫يوناني وومزمء ‪5‬أمء معناه فى الاصل الملاحظ والمدير وفى عرف‬          ‫انيف‬

                                                 ‫الكنيسة الذي له كل الكبنوت‬
 ‫إسكلة ‪ -‬ايطالي مادء‪ 5‬وهو معدول عن ‪ 38‬أى
```


## [2026-09-14T02:02:21.488Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%86%D8%A7%D8%AF%D8%B1",
 "prompt": "Persian چادر (čādor): full etymology — Middle Persian form, any Sanskrit chattra connection, Proto-Iranian reconstruction, cited scholars (Hasandust, MacKenzie), and descendants (Russian чадра, Urdu, Arabic)."
}
```


## [2026-09-14T02:02:22.861Z] TOOL CALL #49: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%86%D8%AA%D8%B1",
 "prompt": "Persian چتر (čatr): etymology — borrowed from Sanskrit छत्र (chattra)? Middle Persian form? Give the full etymology text and meaning."
}
```


### [2026-09-14T02:02:26.830Z] TOOL RESULT

```
# Summary of چادر (Chador/Tent)

The word **چادر** is a multi-language noun found across Persian, Turkish, Urdu, Kurdish, and other languages. 

## Primary Meanings

According to the Wiktionary entry, the term refers to:
- A "portable lodge made of skin or canvas" (tent)
- "A large single piece of cloth worn as a covering over the clothing" (chador garment)
- In some contexts: awning or bedsheet

## Etymology

The word originates from "Middle Persian čādur (sheet, veil)" and traces back to Sanskrit *chattra*. The entry notes the term has been "attested in Turkic from the 11th century," appearing in historical dictionaries and linguistic records throughout the region.

## Linguistic Spread

This term spawned numerous descendants across European and Asian languages, including Russian (шатёр), Hungarian (sátor), English (chador), and many others, demonstrating significant historical influence through Ottoman Turkish and Persian cultural transmission.
```


### [2026-09-14T02:02:27.320Z] TOOL RESULT

```
# Etymology of Persian چتر (čatr)

**Borrowed origin:** The Persian word چتر is "Borrowed from Sanskrit _छत्त्र_ (chattra)."

**Full etymology:** According to Wiktionary, this term entered Persian through a Sanskrit source word meaning the same concept. The entry notes it is a "Doublet of _چادر_ (čâdor) and _چتری_ (čatri)," indicating related Persian forms derived from the same ultimate origin.

**Meaning:** The word denotes an umbrella or parasol—a portable shade device. In classical Persian literature, it carried royal connotations, as evidenced in a 14th-century poem where it symbolizes protection and majesty.

The article does not provide information about a Middle Persian intermediate form in its etymology section.
```


## [2026-09-14T02:02:33.552Z] TOOL CALL #50: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg452.png"
}
```


### [2026-09-14T02:02:34.148Z] TOOL RESULT

```

```


## [2026-09-14T02:02:34.121Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-14T02:03:00.964Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; ls | head -60"
}
```


### [2026-09-14T02:03:01.019Z] TOOL RESULT

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
```


## [2026-09-14T02:03:04.263Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"### KLN scandal\"; grep -n -i \"skandalon\" KLN_1966.txt | head -5; echo \"### KLN scale/scala\"; grep -n \"scandere\\|scand-sla\\|scandō\" KLN_1966.txt | head -8"
}
```


### [2026-09-14T02:03:04.339Z] TOOL RESULT

```
### KLN scandal
### KLN scale/scala
3583:Ascaridae,  n.  pi.,  a  genus  of  Nematoda  or  thread¬ worms.  —  ModL.,  fr.  Gk.  amcaplp,  hen.  -1809, ‘worm  in  the  intestines’,  which  is  rel.  to  axa- pli^Eiv,  Att.  acxapi^siv,  ‘to  jump’,  axaipetv,  ‘to skip,  dance’,  oxiprav  (freq.  of  oxoapstv),  ‘to leap,  bound’,  oxApo?,  ‘the  parrot  fish’  (lit.  ‘the leaping  one’),  fr.  I.-E.  base  *sqer-,  ‘to  leap, bound’.  See  Scarus  and  -idae. ascend,  tr.  and  intr.  v.  —  L.  ascendere,  ‘to  climb up,  mount’,  fr.  ad-  and  scandere,  ‘to  climb’.  See scan  and  cp.  descend.  For  the  change  of  Latin a  (in  scandere)  to  e  (in  as-edndere)  see  accent and  cp.  words  there  referred  to. ascendance,  ascendence,  n.  —  Formed  fr.  ascend¬ ant  resp.  ascendent,  with  suff.  -ce. ascendancy,  ascendency,  n.  —  Formed  from  next word  with  suff.  -cy.
10998:descend,  intr.  and  tr.  v.  —  F.  descendre,  fr.  L.  de¬ scender  e,  ‘to  come  down,  descend,  sink’,  fr.  de- and  scandere,  ‘to  climb'.  See  scan  and  cp.  as¬ cend,  condescend.  For  the  change  of  Latin  & (in  scandere)  to  e  (in  de-scendere )  see  accent  and cp.  words  there  referred  to.
33904:* scand-sld ,  a  derivative  of  scandere,  ‘to  climb’. See  scan  and  cp.  escalade,  escalator.
33919:Derivatives:  scamper,  n.,  scamper-er,  n. scan,  tr.  v.,  1)  to  analyze  (verse)  as  to  its  metrical structure;  2)  to  examine  carefully;  intr.  v.,  to verse.  —  L.  scandere,  ‘to  climb,  mount,  scan’ (whence  ascendere,  ‘to  climb  up,  mount’,  de- scendere,  ‘to  come  down,  descend’),  fr.  I.-E. base  *skartd-,  ‘to  spring,  leap’,  whence  also  OI. skandati,  ‘hastens,  leaps,  jumps’,  Gk.  oxdvSaXov (whence  L.  scandalum),  ‘stumbling  block offense’,  Mir.  sescaind,  ‘he  sprang,  jumped’, scendim,  ‘I  spring,  jump',  sceinm,  ‘a  bound, jump’,  W.  cy-chwynnu,  ‘to  jump  up,  start  up". The  omission  of  the  -d  in  E.  scan  (for  scan-d )  is prob.  due  to  its  having  been  confused  with  the
33926:scandent,  adj.,  climbing  (said  esp.  of  a  plant).  — L.  scandens,  gen.  -entis,  pres.  part,  of  scandere, ‘to  climb’.  See  scan  and  -ent. scandia,  n.,  the  oxide  of  scandium,  Sc203  ( chem .) —  ModL.,  coined  by  its  discoverer,  the  Swedish physicist  Lara  Fredrik  Nilson  (1840-99)  in  1879 fr.  ML.  Scandia,  ‘Scandinavia’  (fr.  L.  Scandia, name  of  an  island  in  Northern  Europe).  See Scandian,  Scandinavia  and  cp.  scandium. Derivative:  scandic,  adj.
33933:scansion,  n.,  act  or  mode  of  scanning.  —  L.  scdn- sid,  gen.  -onis,  ‘a  climbing;  scanning’,  fr.  scans- (um),  pp.  stem  of  scandere,  ‘to  climb’.  See  scan and  -ion.
33935:scansoriai,  adj.,  adapted  for  climbing  (said  of birds).  —  Formed  with  adj.  suff.  -al  fr.  L.  scan- sorius,  fr.  scdns-(um),  pp.  stem  of  scandere ,  ‘to climb’.  See  scan.
33937:scantling,  n.,  1)  a  small  quantity;  2)  a  small timber;  3)  small  timbers  collectively.  —  Corrup¬ tion  of  OF.  escantillon  (F.  echantillon),  ‘sample, pattern',  fr.  earlier  eschandillon,  a  dimin.  whose primitive  form  occurs  in  OProven?.  escandil, ‘measure  of  capacity’,  fr.  L.  scandere,  ‘to  climb’, used  in  the  sense  ‘to  measure  the  scale  of  some¬ thing’.  Cp.  ML.  scandilia,  ‘rungs  of  a  ladder’, scandalium,  ‘measure  of  capacity’,  and  see  scan. See  Bloch-Wartburg,  DELF.,  p.  200  s.v. Echantillon.
```


## [2026-09-14T02:03:05.480Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"### SKT\"; grep -n -i \"scandal\\b\" SKT.txt | head -5; echo \"### BRT sadayanti\"; grep -n -i \"sadayant\\|sāδayant\" BRT.txt | head -5"
}
```


### [2026-09-14T02:03:05.575Z] TOOL RESULT

```
### SKT
16595:SCANDAL.
16596:CF.-L.-C.k.)  F.  scandate. eundahm.^Cik.  citd¥laXo%\  a  snare  ; L  scandal,  oflfence.  itumbling-block. the  B[^ng  of  a  trap,  the  !>tick  which I  up  when  the  trap  was  shut,  and  on the  bait  was  placed ;  nsnally  called U]70^or.*V^^ANI),  to  gpriug  up, >&Bion.  (L.)  From  L.  scanua,  a ng.«»L.  KdMSHs,  pp.  oi  scanJfrt. Oder,  scandal.  (,F.-L.-Gk.)  M.  E. 'nr,  sctaunJre.  —  O.  F.  tsilandrt, iL  The  oldest  O.  F.  form  was 7/,  whence  tscandU,  escandrg,  and etfi'anJrt,  with  Insertwl  /,  It  is f  another  fonn  of  scandal  (above). iiBoend.  (L.)  L.  transanJirt,  to over,  to  vurpass.  —  L.  trart'^  for be)ond  ;  uats.Ut^,  to  climb. adAl.  Scansion ;  kc  Scui. at,  adi.  (Scasd.)  M.  E,  ikant,  in- i!aL«>Icet  skamt.  ncut.  of  skammr, brief;  whence  siamfa,  to  dole  out t  to  ficant  dr  stint) ;  Icel.  sMamtr,  a lij  Noi  wcgian,  ni  appears  for  mt, tkani.  a  dole,  skatua^  to  measure Der.  scanty.
23313:scandal— slander.
### BRT sadayanti
```


## [2026-09-14T02:03:14.818Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"### BRT Kleidungsstück\"; grep -n \"Kleidungsstück\" BRT.txt | head -20"
}
```


### [2026-09-14T02:03:14.874Z] TOOL RESULT

```
### BRT Kleidungsstück
3880:•  J.  ainrLvarana-  m.  'Bedeckung,  Beklei- dung': up^mii  [aite]  statri^ta),  anlama  °na also  druxs  yä  nasus  fräsnaoili  "zu  oberst das  Lager,  das  äusserste  Kleidungsstück erreicht  .  ."  V.j.ioC?)'*.
4614:•  j.  antama-  Adj.  i)  'der  innerste':  'ma aiwi.varma  "das  innerste  Kleidungsstück" (d.  i.  das  Hemd)  V.  7.10;  —  'ma  aiwyi- fthänS  Vd.  /2  '*.  —  2)  'der  vertrauteste, intimste':  *°m3mcit'''^  sanhs-n  "auch  das vertrauteste  Wort"  F.  j  eJ'.
8633:Vä.:  ösän  kc  fa  i;irt  TUfdiin  ape  diafend' (tfarak  sniarak  .  .  viiiyötmäh  räiijKiii  ..  d.  i. "die  mit  dem  baaschigen  (Kleidungsstück) sich  bekleiden.  A.  (versteht  darunter)  d: lieind,  M.  die  Hose".  Es  ist  :rw..i«  .  .  ; lesen;  Schluss  unklar.    Vgl.  ÜTtll-  IF.  IO.  S.
9256:.  j.  »karana-  n.  ein  Kleidungsstück  mite- '  f '■^'''«■'  "^  ^^^^t""  =  k>nnv-'\  12b lererGrösse, 'Hose'');  v«.«.r?y^.^«..««^,,r'f''-'«-'':  9+^4  -f^^«va-,  n  k.r.>ya-i\ "eine  Hose,  die  die  beiden  Schenkel  be-'~  \^[^-°'''.^f"^'-     .  ,    .    -,      .
21699:mit  aiwi  i)  'etwas  sich  umtun,  anlegen, anziehen'  (den  Gürtel,  Kleidungsstücke): aiwyäahantm  va  aiwyanhayamnS  aiw- yäffhamm  vS  ia/ayamnä (sd.)  Yt  i.  i  ?;  — ya  hama  *aiwyär9Aana  (sd.)  aiwyanha- .yänti  N.g4;  —  aat  aiähe  (näml.  aiwyata- hanahe)  ahi  aiwyUstS  *banlnuS  paiH  . . Y.  p.  26;  —  aiwi  vastra  yäwAayanuha "zieh  deine  Kleider  an"  V.iS.iq;  — ,  vastra  .  .  aiwyänhayaäa  V.p.  32;  —  yS vastra  vastrim  *aiwyarfhaya7iti^'>  N.55(?);
22840:mit  aipi  '(ein  Kleidungsstück)  darüber anziehen':  yy  aiwyii^hayanti  "nis(sd.)ü nmanai  nmänayqsca^  yezi  tarasca  aiwysip- hana  aipi.var>cainH  ratufryö  N.55.
```


## [2026-09-14T02:03:15.414Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '33900,33912p' KLN_1966.txt"
}
```


### [2026-09-14T02:03:15.482Z] TOOL RESULT

```
scale,  n.,  a  weighing  instrument.  —  ME.  scale,  fr. ON.  skal,  ‘shell,  dish,  scale  of  a  balance’ (whence  Dan.  and  Swed.  skal,  ‘scale  of  a  bal¬ ance’,  Dan.  skaal,  Swed.  skal,  ‘drinking  cup, bowl’),  which  is  rel.  to  OE.  scalu,  OS.  skala, OHG.  scala,  MHG.  schdle,  G.  Schale,  ‘drinking cup,  bowl;  shell,  scale  of  a  balance’,  MLG. schale,  MDu.  scale,  Du.  schaal,  ‘drinking  cup, bowl,  scale  of  a  balance’;  fr.  Teut.  *skelo-, which — according  to  Paulus  Diaconus — orig. denoted  ‘a  drinking  cup  made  from  a  skull’; fr.  I.-E.  base  *(s)qel-,  ‘to  cut,  cleave,  split’  (so called  in  allusion  to  the  skull  as  separated  from the  other  bones  of  the  head).  See  Kluge- Mitzka, EWDS.,  p.  633  s.v.  Schale.  See  shelf,  ‘slab  of wood’,  and  cp.  words  there  referred  to.  Cp.  also scale  of  fish  and  skull.  Cp.  also  scall,  scallop, scalp,  school  of  fishes,  shale,  shell,  shellac,  shield, shoal,  ‘crowd’,  skill.  Cp.  also  Scylla.
Derivatives:  scale,  tr.  v.,  to  weigh  in  scales; intr.  v.,  to  be  weighed.
scale,  n.,  membraneous  outgrowth  of  the  skin  of fish,  etc.  —  ME.  scale,  fr.  OF.  escale,  ‘cup, scale,  shell  pod,  husk’  (whence  F.  ecale,  ‘shell, hull,  husk’),  fr.  Frankish  skala,  which  is  rel.  to OHG.  scala,  MHG.  schal,  G.  Schale,  OE.  scea- lu,  ‘shell,  husk’,  Goth,  skalja,  ‘tile’,  orig,  ‘any¬ thing  scalelike,  shingles',  and  cogn.  with  OSlav. skolika,  ‘mussel,  shell’,  Russ,  skala,  ‘rind, bark’;  fr.  I.-E.  base  *(s)qel-,  ‘to  cut,  cleave, split’.  See  scale,  ‘weighing  instrument’,  and  cp. words  there  referred  to.  Cp.  also  scaglia. Derivatives:  scale,  tr.  v.,  to  clear  of  scales, scale-less,  adj.,  scal-er,  n.,  scal-ing,  n.,  scal-y, adj.,  scal-i-ness,  n.
scale,  n.,  measure.  —  ME.,  ‘ladder,  staircase’,  fr. L.  scalae  (pi.)  (either  directly  or  through  the medium  of  It.  scala),  ‘ladder,  staircase’,  fr.
* scand-sld ,  a  derivative  of  scandere,  ‘to  climb’. See  scan  and  cp.  escalade,  escalator.
Derivatives  :  scale,  tr.  v.,  to  climb  up  by  a  ladder, scal-er,  n.,  scal-ing,  n.
scalene,  adj.,  having  unequal  sides  ( geom .)  — Late  L.  scalenus,  fr.  Gk.  oxaX^vo;,  ‘limping, halting,  uneven-,  which  is  rel.  to  ox£Xo?,  ‘leg’ (lit.  ‘bending’),  crxoXio?,  ‘crooked,  bent',  erxeb- Xr,i,  ‘worm',  fr.  I.-E.  base  *(s)qel-,  ‘crooked, curved,  bent,  perverted’.  See  colon,  ‘punctuation mark’,  and  cp.  scelerat,  scolex,  scolion,  scoliosis and  the  second  element  in  isoceles,  triskelion. Derivatives:  scalene,  n.,  scalen-ous,  adj.
scalenus,  n.,  name  of  each  of  the  muscles  situated on  either  side  of  the  neck  (anat.)  —  Medical  L.,  fr Gk.  oxotXvjvoi;,  ‘uneven ;  triangle  having  unequal sides’;  see  prec.  word.  —  In  its  anatomical sense  the  word  scalenus  was  first  used  by  the French  anatomist  Jean  Riolan  (Secundus) (1577-1657),  who  gave  this  name  to  the  whole  of
1391
these  muscles,  because  they  have  the  shape  of  a scalene  triangle.  See  Joseph  Hyrtl,  Onomatolo- gia  Anatomica,  pp.  462-463. scall,  n.,  scurf,  esp.  of  the  scalp.  —  ME.,  fr.  ON. skalli,  ‘a  bald  head’,  whence  also  Swed.  skallig, ‘bald’ ;  rel.  to  scale  of  balance  and  scale  of  fish. Cp.  scald,  ‘scabby’.
scallion,  n.,  shallot.  —  ME.  scalyon,  fr.  ONF.  es- calogne,  fr.  L.  Ascalonia  (caepa),  ‘(onion)  of  As- calon’.  See  shallot.
scallop,  n.,  a  bivalve  mollusk  (genus  Pecten). — ME.  scalop,  fr.  OF.  escalope,  ‘shell’,  rel.  to escale,  ‘cup,  scale  of  fish,  shell,  husk’.  See  scale of  fish  and  cp.  scaglia,  esealop.
Derivatives:  scallop,  tr.  v.,  scallop-er,  n., scallop-ing,  n.  and  adj.
```


## [2026-09-14T02:03:25.055Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i \"dayant\" BRT.txt | head -20"
}
```


### [2026-09-14T02:03:25.109Z] TOOL RESULT

```
3885:■  j.  aiwi.vöi^dayant-  Adj.,  PPA.:  s.  1 vöiidaya:  \
6012:ni/antlni  Ytß.  54;  18,  22',  26,  30,  42,  50, 54,  lOS,  117,  130,  p.4,  9f.s,  18,  22,  26, 72.2,  74- 58',  75.3,  28,  32,  Vytao»,  21, 4ß;  —  da%äni  ti .  ,  kazannm  .  .  uta  Ig 'S3m  äfrinäni  ..  Y.22.4L;  YL5.63;  — j/ai  mam  iura  paedayanta  .  .  äai  'stm tanüm  aguze  .  .  äai  tnam  fraguzayania  . . Yti^-SS;  56;  —  kü^a  tl  'um  varsm i?rjnavane  V.  2.  $t ;  lff.12,  22.6',  Ytij. 57;  —  't?m  II  g<K%ä  frähoyeni  'z?m  .  . 'Z3m  V. 2.5;  27.6,  7,  Vr.j.7;  —  \valnä a''ur(^mazdäha''  'dam  xsäya%iya^  amiy . . 'damsäm  xs'äya^iyi^  aham  Bh.  7. 5!;  — iyam  gaumätJ'  ,  .  avahä  a%ak(r  'dam baräiy^  amiy  . ,  'dam  xl3ya%iye^  amiy Bh.b;  c-j",  7.11,  13,  i6',  2.3,  s,  14,  J-S. 13;  1^2^;  —  ima'  tya'  'dam  akunavatn vasnä  J'ur^mazdäha'  ah/^ ..pasavJ' ya%ä x^aydiiiyJ'  abavam  'dam  19  hamaranä akunavam  vasnä  t^un^mazdäht^  'dam- säm ajanatn  uta  9  xssyaHyä  agarbäyam Bh..^.  2;  — pasäv^  'dam  t^urt^tnazdäm patiyävahaiy  a^urJ'matdämaiy  upastsm abar(^  .  .  avähä  'dam  . .  gaumätam  .  . aväjanam  . .  avadasim  aväjanam  x/a- %''amHm  °dam  adrnam  vasnä  a^urc^maz- dähc^  'dam  xsilya'^iyaf'  abavam  J'ur^- mazdä  x/ä^^am  manS  Jrsbara^  Bh.  J.  13; 14';  —  'damsaiy  uta  ftaham  .  .  frajanam ,  .  pasävJ'  'dam  .  .  uzmayapaiiy  akuna- vam Bh.  2. 13;  — pasävtrsaiy  'dam  ulä näham  .  .  fräjanam  ,  .  pasäve^sim  ,  ,  ut- mayäpatiy  akunavam  fih.2. 14;  —  °dam (s.  I  b)  xläya%iy^  amiy  vasna  c^urt^- mazdäha/"  'damsim  *g'a^avä  niya/ädayam tya^/äm  'dam  a%akam  avc^  .  .  D.  ö.  4 ; 3'.  5>  4-1,  5-2.  ^7-3^  Bh.  j.is,  16,  17', 18I,  19',  2.1',  2,  4,  6',  7,  9,  10,  II,  12*, 13,  Bh.^.  I,  2,  6,  8,  13,  14,  4.4,  6,  8, 12,  IS,  18,  5.1%  X.7.3,  ^.311.  Die Übrigen  Siog.-Kasus  des  Fron.  i.  Fers. s.  unter  ^ma-.  [¥.4:^.14;  lies  a&;  — Yt.  7.29:  lies  zamarf.'j
7465:•  j.  Isu.aspa-  Adj.  'der  schnelle  Rosse hat':  laxtnim  staotänm  .  .  "pfm  Yt.  ij. 12;  —  yat  mqm  Iura  pazdayanta  °fia naotaraca'1  Yt.  77.55;  S^.
7468:•  j.  äsu.aspt-  Adj.  'im  Besitz  schneller Stuten':  yatät  mqm  (näml.  aTliii)  tura pazdayanta  'paim  (ASf) ''  naotaraca  Yt. 77.56.
12329:•  j.,  g.  'tura-''  Adj.,  bezeichnet  ein  Volk '/arisch,  TürtT  ( TJOranier)' :  y^  mqm  (näml. ailm)  'ra  paxdayanta  asu.atpa  naotaraia
15930:5.  3)  'verscheuchen':  yai  mqm  iura (sd.)  pasdayanta  .  .  naotaraca  Yt  J".  55;
17921:•  j.  fra-8£andayant-  Adj,  (fem.  yeinti-), PPA.:  s.  sianä:
19399:\pfr?satca  ma  ä/  akl  . .  Y.43.  J;  —  at ahya  ma  bTndvahyä  (sd.)  manayätc  lialis Y.4g.2;  —  nüij  ahya  ma  a%rii  {^.)  . . frSsyatY.46-^-  B 11)  imjAw.;  zu  a  1): "  mam  stavät?  Yt5.  8;  Ä  15,  10.108; ana  mam  yasna  yazaiSa  Yt.5.  91;  — yat  mam  iura  pazdayanta  Ytjj.  55;  — ^.82; —yai  ma  hau  na  ..aot  avi  ashaväj P.  27;  —  yezi  mam  p^nsa^Ae  Y.iS.j; Vt,  /f.  56,  ig.  44;  '—  aoi  mam  .  .  ttütci yd^a  ma  aparacit  saoiyan^  siavqn  Y. g.z; — yS  mam  alvS  JäraayätiYt,iy.3o; 5.  so,  Y.  //.  I,'  a,  3,  5;  —  As  ahi  yS  mam zbayehiY\,ij.  17;  V.J.  a6;  —  aat  ma  riBit masyaka  .  .yazmie  Yt.  10.  54;  —  aat  mam tarn  ^baisazyöis  Y .22.2,  9;  2  i.St.,  R2,i4, Yt/7. 19,  SS;  —  yezi  ahi  paurva.nalmat aat  mam  avi  nmSnaya  YtJÖ.  a;  2,  Y.j/.i;
21216:vorausgehendem  farä  'antequam':  *ut- inidyäi  pars  hy"  möi  a.jimal  siraois  Y. 4_j.i2;  —  vaola  mSi  ,.parS  hy  mä yS  mSng pprfhä{%A.)jimaitlY.48.2.  4)dasVer- bum  {'ah-)  ist  weggelassen:  ya'ha  ii  anhm hmkinta  (sd.)  hy  ('wenn')  V,^7. 14.  b)  im j  Awr. ;  I )  mit  dem  Praeteritum  oder  Perfekt; /)  mit  dem  Praeteritum :  tqm  yazata  j3- mäspd  y  ('als')  spätem  pairi.avamat  Yt. 5.68;  61;  — y'  bitlm  a^artnS  apatamata . .  aom  afarfnS  hang^urvayata  . .  %raltaonl! Yt  ig.  36;  38;  —  vaäam  .  .  yim  barat  .  . %raifaonS  y  asis  dahlks  Jaiiti  Yt.  ig.  92 ; 93'.  77;  — y  titaral  anrS  mainyu?  dählm asahe  . .  antar»  pairi.avait>m  (sd.)  vohuca manS  -  .  Yt.  /^.  77;  —  frava^ayS  .  .  yä ta%a  ar^mih  kiliania  y  *mainyu  däman dai^Uem  YtJj.  76;  — y-  mqm  iura  (sd.) pazdayanta  ..aal  az3m  aguze  ..Ytiy.  $$; 10.  \;  —  y  tum  .  .  var^sSs(sd.)ia  *hqm.' rätayatiha  .  .  srvai'a  ^upa.^winsanha äat  tum  pascaUa  .  .  V,  /j.  4;  —  y  tum ainim  avafnSis  (sd.)  ..äat  tum  m/hiAöt/. . H.  2. 1 3.  a)  mit  vorhergehendem /<w«7Ä(i 'postquam':  yS  nüil  pas^agta  huix^afa  y mainya  damqn  daiZit^mY.^j.ij'K  b)mil vorhergehendem  para  ahmät  'antequam': ye^he  xlährata  nSit  aot?m  änha  .  .  para ahmät y..väam  anhai><lm  cittmäne (sd.) paiti.barata  Yt.  ig.  33.  c)  mit  vorher- gehendem vTsp»m  ä  ahmät  'donec,  bis':  ä dim  paskat  anu.marizatpm  ..vtspim  ä  ahmäi y  a^m  paiti.apayat .  .YlS-^B.  2)  mit dem  Perfekt:  taMu.mazS  (sd.)  ..  aiayqm *pa/re  *y  ^'  nöit  yava  miiiB  mamm  ,  . P.  iS.  3)  mit  dem  Praesens:  y  ('dann wenn')  asava  para.irihyeili  kva  .  .  havS urva  vaahaite  H.2,  i;  19,  V,/y.5o;  — äat  y  duidi  fradvaratti  ,  .  'hwaüm *yujyeite  väl^m  tnihrS  Yt.  70.  52;  48,  loi, (?.  9;  —  äat  y  aps  usbannte  ..  äat frahlSittti  .  .  fravaSayd  Yty.  65;  I4.(>Z',
21254:•  j-  yat-£it  Konjn.  i }  konzessiv  'auch  wenn, wenn  schon';  das  Verbum  {'aA-)  ist  weg- gelassen: y  usas/aire  Aimivs(sd.)  *ag»urva- yeiti  Y.57.  29;  29,  Yt /o.  104';  —  mit Praes.:  hs ..  iiva.vasmai^A^  apayeifi  ..y° vazaite  hvastim  YLJ4.20.  a)  im  Nach- satz steht  o)  Hl;  das  Verbum  i^ah-)  ist we^elassen:  y°  vimaSiim  aiAhA  umö tfmcit  mi%rB  kangr>fs3mnS . .  Yt/o.io4f.; 104.  ß)  atH},  mit  Praes.:  y  Avast?m (sd.)  *aiihyäti  y  tanüm  apayäti  atßt  dim nOii  räsayaiU {sd.)  Yt. /o.  zi.  2)  tem- poral; 'als',  mit  Praes.,  im  Nachsatz  steht atai  'da':  y°  mam  tura  (sd.)  pazdayanta aiiii  atitn  tanüm  aguze  .  .  a0i  . .  Yl  sj. 56'';  56.  3)  kondizional  'wenn,  so- fern'; mit  Praes.:  y  *pascaaa  aH'qm raiufrittm  ava.raooayäti  tanüm  *pirydli N.  4"^,  3)  wiederholt  'sei  es  dass  .  . oder  dass';  mit  Praes.:  y  ahi  raihvd .  .  upa  karlvars  yat  ar>sahi  zbayamaki . . y^  ..  Yt.  12,9-37;  —  das  zweite  Mal mit  Tmesis:  y  n^mavAa  väcim  baraiti yat  gai>s{sd.)cii  Yt.  10.  S$.  b)  das  Ver- bum (,'aA-)  ist  weggelassen:  vTspe  haoma upastaomi  y°  barisnuna  gairinam  y'  jaf- nu&a  raonqm  yaicit  azahu  ,  ,  V,  /o.  17.
23789:mit  aiwi  '(das  Haupt)  erheben,  hoch tragen':  malyehe  . .  aiwi.vsizdayantakt*^ kamirio>m  ". .  der  das  Haupt  hoch  trägt" Y.p.31.
25834:•  j.  "saodayanta  aiti  niräxayant^ Vyt.36.
```


## [2026-09-14T02:03:31.024Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"sä%ayant\\|säSayant\\|saSayant\\|sadayant\\|säd̮\" BRT.txt | head; echo \"--- Hose\"; grep -n \"'Hose'\\|„Hose\" BRT.txt | head -10"
}
```


### [2026-09-14T02:03:31.104Z] TOOL RESULT

```
26176:•  j.  säSayanti-  f.  Name  eines  Kleidungs- stücks: yl^  vanhaiti  natssca  -tisca  N.p5.
--- Hose
9256:.  j.  »karana-  n.  ein  Kleidungsstück  mite- '  f '■^'''«■'  "^  ^^^^t""  =  k>nnv-'\  12b lererGrösse, 'Hose'');  v«.«.r?y^.^«..««^,,r'f''-'«-'':  9+^4  -f^^«va-,  n  k.r.>ya-i\ "eine  Hose,  die  die  beiden  Schenkel  be-'~  \^[^-°'''.^f"^'-     .  ,    .    -,      .
```


## [2026-09-14T02:03:41.457Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '26170,26180p' BRT.txt; echo \"=== nearest page tags\"; awk 'NR>=26100 && NR<=26200 && /^[0-9]{3,4}$|\\[pdf page|^\\f/' BRT.txt | head"
}
```


### [2026-09-14T02:03:42.416Z] TOOL RESULT

```
-  Vgl.  .
^r-).    -
Falsch  SPreus»AW.
•  j.  säi°,  say'^,  nur  KompA.  'ungleich- massig  gefärbt,  Scheck  ig*.
Aui   ar.  *sä>,i)i;   %  8r.  —  Vgl.  ai.  iäri-  Adj.
'bunt,  scheckig';  femer  unter  j^r^v'  und  Bthl. Baitholomae.  Alünn-Wb.
•  j.  säSayanti-  f.  Name  eines  Kleidungs- stücks: yl^  vanhaiti  natssca  -tisca  N.p5.
Unsicher.  —  Pü.:  dddnakadk.
•  j.,  g.  8ädra<  n,  "Leid,  Qual,  Wehe': 'r)m  urviitr>m(sA.)ca  nimrüite  tiStryS  .  . °mn  trii , .  urviänm  aps  Yt.8.iy, —  usta ahntai  naire  . .  °rpm  ahmai  naire  Yt.  10. 1 3  7  f-  i  —  auch  Plur, :  ysi . .  rasxmä  aspSnäl 'raHt  caxrayS{%A^  '^■34-  7;  —  °ra  mal  sqs (Sp.  issSu.)  *graid3iti/Y. 43.11.  a)mit Akk.:  utayoia  ya  narqi  'ra  dr^vatS "immerdar  (aber  werden)  die  Qualen  der /?ri(?genossen  (währen)"  Y.  45. 7;  ver- wendet Vr.iÄ2,P.2Ä,  G.^.6  ("r-a).
Zum  gr.  V,  jt^«  'kränke';  Tgl.  GnN.  KZ.  27. 342,  FicK  VglWb.i  2.  68.  —  np.  ™r,  — Vgl. sästa..  —  Pü. :  lon^,  langik,
SO
=== nearest page tags
```


## [2026-09-14T02:03:53.675Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"### HRN chadar/chatr\"; grep -n -i \"čādar\\|cadar\\|tschadar\\|čatr\\|Schirm.*chatr\" HRN.txt | head -10; echo \"### HUB\"; grep -n -i \"čādar\\|cadar\\|čatr\" HUB.txt | head -10"
}
```


### [2026-09-14T02:03:53.746Z] TOOL RESULT

```
### HRN chadar/chatr
### HUB
```


## [2026-09-14T02:03:55.091Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"### DOZ iskele\"; grep -n -i \"skele\\|escala\\b\" DOZ.txt | head -10; echo \"### ARY\"; grep -n \"چادر\\|چتر\\|اسکله\\|آسانسور\" ARY.txt 2>/dev/null | head -10; ls | grep -i ary"
}
```


### [2026-09-14T02:03:55.190Z] TOOL RESULT

```
### DOZ iskele
### ARY
NYB_vol2_glossary.txt
```


## [2026-09-14T02:04:01.895Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i \"catr\\|chatr\\|adar.*Zelt\\|Zelt.*ādar\" HRN.txt | head -10; echo \"### ARY path\"; python3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'));print(json.dumps(d['ARY'],ensure_ascii=False,indent=1))\""
}
```


### [2026-09-14T02:04:03.119Z] TOOL RESULT

```
### ARY path
{
 "title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.",
 "kind": "local_scan_ocr",
 "url": "",
 "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt"
 ],
 "page_offset": "printed page = pdf page + 1",
 "scans": [
  {
   "file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_aryanpur_kashani_rishehaye_hend_o_orupayi.pdf",
   "first_printed": 1,
   "last_printed": 546,
   "pdf_offset": -1,
   "lang": "fas+eng",
   "ocr_text": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt"
  }
 ],
 "notes": "Image-only PDF provided by the owner (2026-09-04). Use as an additional modern source alongside Wiktionary/Cheung/Hasandust when judging Persian arrows; cite as ARY:<page>. | full OCR text fas+eng (headwords in Persian and Latin caps), printed = pdf+1 | Latin-only OCR (cleaner for transliterated headwords, root names, Pokorny numbers)"
}
```


## [2026-09-14T02:04:06.478Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY; python3 - <<'EOF'\nimport re\nt=open('ARY_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,p in enumerate(t):\n    for w in ('چادر','چتر','اسکله','آسانسور','اشل'):\n        if w in p:\n            print('pdfpage',i+1,'printed',i+2,'word',w)\nEOF"
}
```


### [2026-09-14T02:04:07.611Z] TOOL RESULT

```
pdfpage 53 printed 54 word اشل
pdfpage 165 printed 166 word اشل
pdfpage 327 printed 328 word اشل
pdfpage 334 printed 335 word اشل
pdfpage 450 printed 451 word اشل
```


## [2026-09-14T02:04:13.176Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY; grep -n -i \"ČATR\\|CATR\\|CADOR\\|ČĀDOR\\|CHATR\" ARY_latin_index_pages.txt | head; echo \"---\"; python3 - <<'EOF'\nt=open('ARY_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\np=t[164]\ni=p.find('اشل'); print(p[max(0,i-200):i+200])\nEOF"
}
```


### [2026-09-14T02:04:14.531Z] TOOL RESULT

```
---
انس این فهرست را از واجریشه‌ی هند و اروپایی ۴811۸۰ مي‌دانند.
(105 :۳016033) ۰
۱
اد
۱ اوستایی (4۲251۸2): ۳۸۸
-۸8۸ ,۰۳۸۸871 ,2۸8۰ آلمانی (057۸/۸(۷): قددد انا
پهلری (۲7ماتلهه): ۸7 انگلیسی کهن (5 2۸0 012 اشل۲۸
سانسکر یت (5۸۸9777): انگلیسی (تلولاه/(): ی
- و8181 ,818۸11 دانمارکی (0۸78): ۷
آرمنی (/47۷/14): 1100۸77 سوئدی ([8150/5): 7۸۸
یرنانی (06880): ۰ 208817810 ,80۳08 ۰ نروژی (انما۵/08۳0: ۷
لاتین (7[07م
```


## [2026-09-14T02:04:18.776Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for w in اسکله آسانسور اشل; do echo \"### $w\"; grep -o \".\\{0,120\\}$w.\\{0,160\\}\" MON_part1.txt | head -3; done"
}
```


### [2026-09-14T02:04:29.798Z] TOOL RESULT

```
### اسکله
ugrep: error: error at position 88
80-\xbf][\x80-\xbf]*){0,160}
                            \___exceeds complexity limits


### آسانسور
ugrep: error: error at position 92
\n\x80-\xbf][\x80-\xbf]*){0,160}
   exceeds complexity limits___/


### اشل
ugrep: error: error at position 84
xbf][\x80-\xbf]*){0,160}
                        \___exceeds complexity limits
```


## [2026-09-14T02:04:32.813Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport re\nfor f in ('MON_part1.txt','MON_part2.txt'):\n    t=open(f,encoding='utf-8',errors='replace').read()\n    for w in ('اسکله','آسانسور','اشل','چادر','چتر'):\n        for m in list(re.finditer(re.escape(w),t))[:2]:\n            print(f,w,'>>>',t[max(0,m.start()-100):m.start()+180].replace('\\n',' '))\n        print('---')\nEOF"
}
```


### [2026-09-14T02:04:34.492Z] TOOL RESULT

```
MON_part1.txt اسکله >>> دازه گیری دارو.   اسکفه: 2 (معر. ارمی اسقو فتا] (.)  آستانه» آستان‌در.   اسکلت: 6۱ استخو ان‌بندی.   اسکله: عاعتای رداف‌اه آمکعر. و متر] (ا.)  بندرء لنگ رگاه» بارانداز کشتی‌ها.  اسکناس: عقجعمه (.) نوعی کاغذ بهادار  که بهای وی بر روی آن نوشته شده و برای  خرید و فروش بکار می‌رود؛ پو
---
---
MON_part1.txt اشل >>> منكد. () شأن  شوکت» عظمت.  اشگفت: [- شگفت] (.) عجب»    اشگ‌فیدن: -(6)0ع03 (مص‌ل.) در  عجب افتادن.   اشل: 8 (.) واحدی است برای طول  معادل ۰۰ ذراع یا ٩۰‏ گز.   اشل: (28210 [ع.] (ص.) مردی که دست او    افتاده باشد.   اشل: اه [نردبان مقیاس» پایه] (.) رتب؟  کارمندان دولتی؛ پایه. دون اش
MON_part1.txt اشل >>> ‌فیدن: -(6)0ع03 (مص‌ل.) در  عجب افتادن.   اشل: 8 (.) واحدی است برای طول  معادل ۰۰ ذراع یا ٩۰‏ گز.   اشل: (28210 [ع.] (ص.) مردی که دست او    افتاده باشد.   اشل: اه [نردبان مقیاس» پایه] (.) رتب؟  کارمندان دولتی؛ پایه. دون اشل: کارمندی  که رتبه ندارد و کمتر از اشل مستخدمان  رسمی حقو
---
MON_part1.txt چادر >>> گاهان. پسوند دال بر  مکان و موطن: گیلان؛ بونان» ایران» دیلمان.  پسوند حاصل مصدر است در آخر رش  فعل: چادردران کردن» چادر دری» راه  جامه‌دران» راه جامه‌دریدن. سوند دال بر  کثرت و استمرار در آخر اسم فاعل (مرخم):  درم‌ریزان؛ گلریزان. پسوند صفت فاعلی در  آخر ريشة فعل - مفرد امر حاضر: 
MON_part1.txt چادر >>> ل بر  مکان و موطن: گیلان؛ بونان» ایران» دیلمان.  پسوند حاصل مصدر است در آخر رش  فعل: چادردران کردن» چادر دری» راه  جامه‌دران» راه جامه‌دریدن. سوند دال بر  کثرت و استمرار در آخر اسم فاعل (مرخم):  درم‌ریزان؛ گلریزان. پسوند صفت فاعلی در  آخر ريشة فعل - مفرد امر حاضر: خرامان»  روان» 
---
MON_part1.txt چتر >>> داده  یوار 7 (جان.) آفتاب پرست؛ حربا»  آفتاب گردش. آفتاب گر دکك.  آفتاب‌گردان: 2.0 (ص‌فا.) سایبان.  چتر. . قطعه‌ای از چرم؛ پارچة ضخیم با مقوا  3 پیشانی  کلاه که منع تن آتاب به چهره گردد.  افتابگیر: -.2 (افا. امر.) جایی که هر روز  آفتاب در آن تابد) آفتاب‌رو. سایبان) چتر.  آفتاب لق
MON_part1.txt چتر >>> ن آتاب به چهره گردد.  افتابگیر: -.2 (افا. امر.) جایی که هر روز  آفتاب در آن تابد) آفتاب‌رو. سایبان) چتر.  آفتاب لقا: 2.02 آف. (ص‌مر.) آنکه  چهره‌اش مانند آفتاب باشدء سخت ز ببا.  مود 2.0 (امر.) قسمی  تش‌بازی که به هنگام سوختن به چند رنگ  و نماید. یکی از فنون کشتی گیری در  حقتا کست
---
---
---
MON_part2.txt اشل >>> ؛ قدید. میوة  خشک که هستة آن را در آورده بخشکانند.  (ص.) خشکك. اسبی که در مسابقه عقب  می‌ماند؛ مق. باشلق. قاق بودن: بی‌نصیب  بودن» محروم بودن. عقسر از همه بودن.  (قاب‌بازی) کسی که آخر از همه باید بازی  کند. (۱.) آب باران را کد در یک محل.  قاقا: مر2ر[- کا کا] (.) (تد. اطفال) شیر پ
MON_part2.txt اشل >>> نابادی؛ شتر نر ]  (.) نوعی شتر کم موی بارکش.  لوک: (قد.۱0۱۵۲ [ - لک | (ص.) ) آنکه  دستش معبوب باشد؛ اشل» اقطع. کسی که با  هر دو زانو و کف‌های دست راه رود. عاجز»    ربون.    ل و کومو تبو    فرهنک فارسی معین    ۱ ۷    لوکس: تا (.) تجمل بسیار در جامه و  ائانه منزل و غیره. (ص.) (ف.) 
---
MON_part2.txt چادر >>>  مانده.   فشخم: 07 (< پخم] (۱.) جادری که  نثارچینان بر سر دو چوب بندند تا بدان از  هوا نثار ستانند. چادر شبی که در زیر درخت  میوه‌دار گیرند و درخت را بتکانند تا میوه در    1 جمع شو د.  فخم: ۳۹۹ [ع. (.) شریتی از ابت.  فخم: (ع.] (ص.) بلند. قدرء گرامی؛  بزرگوار. کلام فصیح» سخن جزل. 
MON_part2.txt چادر >>> ه  فروشد؛ پنبه فروش.   قطایف: ۵۱5۷6۶« [ع. قطائف] (.) ج. قطیفه,  الف- جامه‌های پرزدار خوابناگک. ب -  چادرهای ببجیده. لوزینه. رشته‌ای که از مبوه  گندم سازند. نوعی حلوا.   قطب: «ماهر [ع.] (ا.) ( گیا.) حنا.   تسس طب‌نما: ۵9-38 [ع. فا. -  قطب‌نماینده] (امر.) آلتی است مرکب از  صفحه‌ای 
---
MON_part2.txt چتر >>> ن جزو ردة ها که قرنی آن  را فطر و کماه خوانند. ( کیا ۰ در تداول عامه  به قارچ‌های خوراکی و قارچ‌های چتری و  کلاهک‌داری اطلاق شود که در اما کن  نمنا ک می‌روید. قارج چمنی: (گیا.) غریقون  بلوط. قارچ خوراکی: (گیا.) سمارو غ. (گیا.)  فارچسی بنام بولتوس که جزو رده  همینومیست‌ها می‌باشد؛
MON_part2.txt چتر >>>  را انجام می‌دهند.  گونه‌های مختلف کبوتر بنام‌های کبوتر  صحرایی؛ کبوتر چاهی» کبوتر پر کاغذی»  کبوتر چتری» کبوتر قاصدء کبوتر طوقی»    کبوتر کاکلی؛ کبوتر مرغی» کبوتر حضر تی؛  کبوتر غبغبی» کبوتر پاپره کبوتر سینه‌نامیده  می‌شوند. حمام» کفتر» کبوتر» کستر؛ ج.  کوترهاء کوتران. ترکیبات ا
---
```


## [2026-09-14T02:04:44.329Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport re\nt=open('MON_part1.txt',encoding='utf-8',errors='replace').read()\nfor w in ('چادر:','چتر:','چادر ','آسانسور'):\n    ms=list(re.finditer(re.escape(w),t))\n    print('###',w,len(ms))\n    for m in ms[:3]:\n        print('   ',t[max(0,m.start()-80):m.start()+200].replace('\\n',' '))\nEOF"
}
```


### [2026-09-14T02:04:45.634Z] TOOL RESULT

```
### چادر: 2
     شده در  شهر چاچ. کمان سیار خوب.   جاخان: |تر. - جخان] ص.)  حقه‌از» شارلاتان.   چادر: ۲ | < شادر دِ چتر | 01 الا یوشی  که زنان روی سر اندازند و همه اندام آنان را    یو شاند. خیمه؛ رده قزر کف سابان. چادر  ترسا: چادر زرد و کبود درهم بافته. ( .کنیه)  شفق و سرخی افق به هنگام غروب افت
    معشوق» محبوب. بر شاخ آهو آشیان داشتن:  بی‌حاصل و بی‌نتیجه بودن. به شاخ انداختن  چادر: یکسو کردن زنان خودنما چادر را  برای نشان دادن حسن ترکیب و تناسب  اعضای خو د. شاخ پر شاخ زدن: سر شاخ و  برگ چیزی افزون و فروع پی در پی بر  یک اصل مترتب کردن. شاخ را از شت  کنمین: برداشتن: (  کشید
### چتر: 1
     دستار بزرگی که عربان  بجای کلاه بر سر گذارند و بر روی آن  عگال (عقال) بندند.   چتر: ۲ (.) سایبان کو چک دسته‌دار که  برای حفظ خود از آفتاب و با باران و برف  بالای سر نگاه دارند. موی کو تاه که مردان  بر فرق گذارند. چتر نجات. چتر آبگون:  (کد.) آسمان. چتر روز: (کذ.) آفتاب»  خورشید. 
### چادر  23
    یلان؛ بونان» ایران» دیلمان.  پسوند حاصل مصدر است در آخر رش  فعل: چادردران کردن» چادر دری» راه  جامه‌دران» راه جامه‌دریدن. سوند دال بر  کثرت و استمرار در آخر اسم فاعل (مرخم):  درم‌ریزان؛ گلریزان. پسوند صفت فاعلی در  آخر ريشة فعل - مفرد امر حاضر: خرامان»  روان» نگران. پسوند دال بر 
    حلال و مباح  را در هنگام زیارت کعبه و مراسم حیج بر  خود حرام کردن. (مج.) (.) دو چادر  نادوخته که در ایام احرام یکی را لنگ و ته  بند کنند و دیگری را بر دوش پوشند.  احری: ۱3 [ع.] (ص تفض.) سزاوار تر»  شاسته‌تر» اولی» اصلح؛ درخور ترء سراتر    ۹۸ فرهنگ فارسی معین احزاب    احسزاب: 0قتا
    می‌سازند. (نج.) فرس» یکی از اندام‌های  اسطرلاب (التفهیم بیرونی). خيمةً بز رگد»  چادر کلان. اسپکث بازی: اسب چوبین و  گلین که کودکان برای بازی می‌سازند.  اسپکترسکپ: 0 (.) (فز.)  دستگاهی است که برای تجزيةٌ نور و تحقیق  در طیف بکار می‌رود؛ طیف‌نما.   اسپنتمد: 060 [- اسپنتمد» خرد  مس 
### آسانسور 0
```


## [2026-09-14T02:04:54.022Z] TOOL CALL #67: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/scala#Latin",
 "prompt": "Latin scala/scalae: etymology (from *scandsla, scandere + -sla), meaning, and descendants (Italian scala, Old French eschiele/eschelle > échelle, English scale). Quote the etymology line."
}
```


## [2026-09-14T02:04:55.038Z] TOOL CALL #68: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/scalo",
 "prompt": "Italian scalo: etymology (from scala?) and meanings (slipway, wharf, stopover, landing place). Quote."
}
```


### [2026-09-14T02:04:58.876Z] TOOL RESULT

```
# Etymology of Latin "scala"

**Etymology line from the source:**
"From _\*skand-slā_, from [Proto-Indo-European](https://en.wikipedia.org/wiki/Proto-Indo-European_language "w:Proto-Indo-European language") _[\*skend-](/wiki/Reconstruction:Proto-Indo-European/skend- "Reconstruction:Proto-Indo-European/skend-")_."

**Explanation:**
The Latin word *scala* (meaning ladder or stairs) derives from a Proto-Indo-European root that originally related to climbing or mounting. This ancient root developed into numerous Romance language descendants, including Italian *scala*, Old French *eschiele* and *eschelle* (which evolved into modern French *échelle*), and English *scale*.

The word demonstrates how a single Latin term spread across multiple language families through both direct inheritance and borrowing, maintaining semantic connections to concepts of ascending or measuring across centuries of linguistic evolution.
```


### [2026-09-14T02:04:59.577Z] TOOL RESULT

```
# Scalo: Italian Word Definition

**Scalo** is an Italian masculine noun with multiple related meanings. According to Wiktionary, it refers to:

1. A slipway designed for small boats
2. A stop or stopover point
3. A port of call
4. An airstrip or runway for aircraft

The word is pronounced /ˈska.lo/ and belongs to the two-syllable category in Italian. Its plural form is "scali."

Additionally, **scalo** functions as a verb form—specifically the "first-person singular present indicative" of the Italian verb *scalare*.

In Occitan (particularly Gascon), **scalo** is a feminine noun meaning "stairs."

The term appears in several compound forms in Italian maritime and transportation contexts, such as *scalo portuale* (port facility) and *capo scalo* (port authority official).
```


## [2026-09-14T02:05:06.068Z] TOOL CALL #69: WebFetch

```json
{
 "url": "https://www.nisanyansozluk.com/kelime/iskele",
 "prompt": "Nişanyan on iskele: source (Italian scala?), first attestation date in Turkish, meaning development ('ladder' → 'landing stage'), and any mention of Arabic إسكلة."
}
```


## [2026-09-14T02:05:09.142Z] TOOL CALL #70: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E0%A4%B8%E0%A5%8D%E0%A4%95%E0%A4%A8%E0%A5%8D%E0%A4%A6%E0%A4%A4%E0%A4%BF",
 "prompt": "Sanskrit स्कन्दति (skandati): meaning and etymology (root स्कन्द् skand- 'to leap, jump, spurt'), and the PIE reconstruction given."
}
```


### [2026-09-14T02:05:10.277Z] TOOL RESULT

```
# Response

Based on the webpage content provided, I can only confirm that this is a page from the Nişanyan Sözlük (Nişanyan Dictionary), a Turkish etymological dictionary maintained by Sevan Nişanyan since 2002.

The actual dictionary entry for "iskele" is not included in the content you've shared—only the website's header, navigation elements, and footer information appear. To provide information about the etymology of "iskele," I would need access to the full entry content, which would include the details about potential Italian origins, attestation dates, and any Arabic connections you've referenced in your query.
```


### [2026-09-14T02:05:15.008Z] TOOL RESULT

```
# Sanskrit: स्कन्दति (skándati)

**Definition:** This Sanskrit verb means "to leap, jump, hop, spring" or "to drop, fall down." It can also mean "to perish" or specifically refer to the emission of seminal fluid.

**Etymology:** The term derives from Proto-Indo-European *skénd-e-ti, based on the root *skend-. Related cognates include Latin *scandō* ("to jump") and Middle Welsh *kychwyn*.

**Grammatical Classification:** This is a class 1, type P verb in the active voice, with the conjugated third-singular indicative form shown as the headword.

**Linguistic Note:** The word appears across multiple scripts, from Devanagari to less commonly used writing systems like Zanabazar Square and Soyombo, reflecting its importance in Sanskrit linguistic tradition.
```


## [2026-09-14T02:05:22.607Z] TOOL CALL #71: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CF%83%CE%BA%CE%AC%CE%BD%CE%B4%CE%B1%CE%BB%CE%BF%CE%BD",
 "prompt": "Ancient Greek σκάνδαλον: meaning, etymology (relation to σκανδάληθρον 'stick of a trap' and PIE *skend-), any note on Beekes or uncertainty, and Septuagint/New Testament usage."
}
```


## [2026-09-14T02:05:24.320Z] TOOL CALL #72: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/eschele",
 "prompt": "Old French eschele / eschelle: is it attested with the meaning 'ladder' from Latin scala? Give the etymology and the forms listed (eschiele, eschelle), and descendants (French échelle, English)."
}
```


### [2026-09-14T02:05:28.380Z] TOOL RESULT

```
# Old French "eschele" - Etymology and Forms

**Etymology:**
The word is "Inherited from Latin _scāla_," according to the Wiktionary entry.

**Forms Listed:**
The article identifies alternative forms as "eschale" and "eskele," though the main entry shows "eschele" as the oblique singular feminine noun.

**Meaning:**
Yes, it is attested with the meaning "ladder."

**Notable Descendants:**
The entry documents several Romance language descendants, including "French: échelle" (the modern French term for ladder). However, the source does not mention English descendants of this Old French term.

The entry confirms the Latin origin and provides evidence of the word's evolution across multiple Romance dialects through its documented descendant forms.
```


### [2026-09-14T02:05:28.494Z] TOOL RESULT

```
# σκάνδαλον: Ancient Greek Etymology and Meaning

## Primary Meanings
The Ancient Greek noun σκάνδαλον (skándālon) carries four distinct senses: "trap," "snare," "enticement" or "temptation," "offense" or "scandal," and "stumbling block."

## Etymology
Scholars traditionally link this term to Proto-Indo-European *skend- ("to jump"), comparing it with Latin scandō ("to ascend") and Sanskrit skandati ("to jump, hop, hurry"). The original sense likely referred to "a piece of wood hanging on ropes, used by acrobats as well as trap-setters."

## Related Terms
The derived word σκανδάληθρον (skandálēthron) appears in ancient texts, suggesting a connection to trap mechanisms.

## Scholarly Debate
Robert Beekes expresses skepticism about the Indo-European derivation, citing problematic semantics and unexplained phonetic features. He proposes instead a Pre-Greek origin, though he acknowledges the possibility of borrowing from another lost Indo-European language.

## Legacy
This word generated extensive descendants across European languages—from Latin scandalum through Romance and Germanic languages to modern English "scandal" and its equivalents worldwide.
```


## [2026-09-14T02:05:39.239Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; for u in \\\n \"https://en.wiktionary.org/wiki/اسکله\" \\\n \"https://en.wiktionary.org/wiki/iskele\" \\\n \"https://en.wiktionary.org/wiki/scandalum\" \\\n \"https://www.etymonline.com/word/scandal\" \\\n \"https://www.etymonline.com/word/escalator\" \\\n \"https://en.wiktionary.org/wiki/ascenseur\" ; do\n timeout 120 python3 tools/fetch_source.py \"$u\" --note \"page 452, roots Skand / Sked 2 verification\" 2>&1 | tail -2; done"
}
```


### [2026-09-14T02:05:42.966Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/05f08b36956a833b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/dd81202e200fb8d0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/261636ce99ab9e52.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/54e9812add778fe5.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/616f423268494cb2.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9c0df1b8697d29b9.txt
```


## [2026-09-14T02:05:47.011Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; for u in \\\n \"https://en.wiktionary.org/wiki/échelle\" \\\n \"https://abadis.ir/fatofa/اشل/\" \\\n \"https://abadis.ir/fatofa/اسکله/\" \\\n \"https://en.wiktionary.org/wiki/چادر\" \\\n \"https://en.wiktionary.org/wiki/چتر\" \\\n \"https://en.wiktionary.org/wiki/scala\" \\\n \"https://en.wiktionary.org/wiki/scalo\" \\\n \"https://en.wiktionary.org/wiki/स्कन्दति\" \\\n \"https://en.wiktionary.org/wiki/σκάνδαλον\" \\\n \"https://en.wiktionary.org/wiki/eschele\" ; do\n timeout 120 python3 tools/fetch_source.py \"$u\" --note \"page 452, roots Skand / Sked 2 verification\" 2>&1 | tail -1; done"
}
```


### [2026-09-14T02:05:54.354Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/40575ad67f720a85.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4ec4230dc9a33d33.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/19e2d63a558c9052.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/70a239cdf6d8cbf4.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b4e9e54f325e7d01.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c27bc16e621ebc80.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0bd48fe85e8466cd.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/eb632d519a4597cf.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/2d4d66c0bce6cdbd.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/49b3703312c7691c.txt
```


## [2026-09-14T02:05:58.925Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; mkdir -p data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg452.png data/verification/sources/refs/ocr/BOOK/452.png && ls -la data/verification/sources/refs/ocr/BOOK/452.png; sed -n '1,80p' tools/verify_check.py"
}
```


### [2026-09-14T02:05:59.009Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 63836 Sep 13 22:05 data/verification/sources/refs/ocr/BOOK/452.png
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


## [2026-09-14T02:06:01.598Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n '80,160p' tools/verify_check.py"
}
```


### [2026-09-14T02:06:01.709Z] TOOL RESULT

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


## [2026-09-14T02:06:06.089Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -c \"\nimport json;d=json.load(open('data/verification/page-385.json'));print(json.dumps(d['entries'][0],ensure_ascii=False,indent=1)[:2500])\""
}
```


### [2026-09-14T02:06:07.270Z] TOOL RESULT

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
```


## [2026-09-14T02:06:26.521Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification; python3 - <<'EOF'\nimport json,glob\nfor f in sorted(glob.glob('page-38*.json')):\n    d=json.load(open(f))\n    for e in d['entries']:\n        for rc in e.get('ref_check',[]):\n            if rc['ref'].startswith('AHD'):\n                print(f,json.dumps(rc,ensure_ascii=False)[:400])\nEOF"
}
```


### [2026-09-14T02:06:27.638Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T02:06:31.464Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification; grep -ho '\"ref\": \"AHD[^\"]*\", \"status\": \"[a-z_]*\"' page-*.json 2>/dev/null | sort | uniq -c | head; python3 - <<'EOF'\nimport json,glob\nn=0\nfor f in sorted(glob.glob('page-*.json')):\n    d=json.load(open(f))\n    for e in d['entries']:\n        for node in e.get('nodes',[]):\n            for rc in node.get('ref_check',[]):\n                if rc.get('ref','').startswith('AHD') and n<4:\n                    print(f, json.dumps(rc,ensure_ascii=False)[:350]); n+=1\nEOF"
}
```


### [2026-09-14T02:06:33.185Z] TOOL RESULT

```
      1 "ref": "AHD:1070", "status": "partial"
      1 "ref": "AHD:1086", "status": "supports"
      1 "ref": "AHD:1140", "status": "not_checked"
      2 "ref": "AHD:1141", "status": "partial"
      1 "ref": "AHD:1287", "status": "not_checked"
      1 "ref": "AHD:149", "status": "not_checked"
      1 "ref": "AHD:1506", "status": "supports"
      1 "ref": "AHD:1507", "status": "partial"
      1 "ref": "AHD:1517", "status": "supports"
      1 "ref": "AHD:1519", "status": "supports"
page-100.json {"ref": "AHD", "status": "supports", "note": "AHD Appendix of Semitic Roots s.v. 'bn' (ahdictionary.com/word/semitic.html): 'Benjamin, from Hebrew binyāmîn, son of the right hand' — the English name filed under the Semitic root exactly as the arrow does."}
page-100.json {"ref": "AHD:99", "status": "contradicts", "note": "The New College Edition page could not be opened (archive.org copies are lending-only), but the same dictionary online (ahdictionary.com/word/search.html?q=baggage) reads: '[Middle English bagage, from Old French bague, bundle, perhaps of Germanic origin; akin to Old Norse baggi, bag, bundle. Sens
page-101.json {"ref": "AHD:579", "status": "partial", "note": "AHD:579 is the 1976 dictionary page (griffin); the current AHD griffin entry (archived, https://ahdictionary.com/word/search.html?q=griffin) derives griffin only 'from Greek grūps' with no Semitic link, but the AHD Semitic-roots appendix (archived, https://ahdictionary.com/word/semitic.html) s.v. krb
page-101.json {"ref": "AHD:231", "status": "supports", "note": "AHD online s.v. cherub (archived, https://ahdictionary.com/word/search.html?q=cherub): '[Middle English, from Late Latin, from Hebrew kərûb; see krb in the Appendix of Semitic roots.]' — Hebrew → (Latin →) English as in the chart; AHD:231 is the 1976 page of this entry."}
```


## [2026-09-14T02:06:42.474Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification; python3 - <<'EOF'\nimport json,glob\nn=0\nfor f in sorted(glob.glob('page-3*.json')):\n    d=json.load(open(f))\n    for e in d['entries']:\n        for node in e.get('nodes',[]):\n            for rc in node.get('ref_check',[]):\n                r=rc.get('ref','')\n                if 'none' in r.lower() or r in ('','None') or 'no ref' in r.lower():\n                    if n<5: print(f, json.dumps(rc,ensure_ascii=False)[:250]); n+=1\nEOF"
}
```


### [2026-09-14T02:06:43.866Z] TOOL RESULT

```
page-300.json {"ref": "(none cited)", "status": "not_checked", "note": "Nourai gives no reference for this pass-through box; the claim was checked against Klein, AHD and Wiktionary instead (see consulted)."}
page-300.json {"ref": "(none cited)", "status": "not_checked", "note": "Nourai gives no reference for this box; checked against Etymonline and AHD (see consulted)."}
page-301.json {"ref": "None", "status": "not_checked", "note": "The box carries no reference in the printed chart."}
page-303.json {"ref": "None", "status": "not_checked", "note": "The node carries no reference in the book."}
page-303.json {"ref": "None", "status": "not_checked", "note": "The node carries no reference in the book."}
```


## [2026-09-14T02:08:26.225Z] TOOL CALL #81: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== WLD Bd2 leaf 563 (p.558)\"; awk 'BEGIN{RS=\"\\f\"} NR==563' incoming/WLD/WLD_Bd2_pages.txt | grep -n -A12 -i \"sqed\\|sked\\|chadati\\|chattra\" | head -40"
}
```


### [2026-09-14T02:08:27.372Z] TOOL RESULT

```
=== WLD Bd2 leaf 563 (p.558)
1:558                                  sked    — sq(h)ed-
2-  got. sJcapjan, shop „schadigen^^, anord. shada, -ada und shedja, ags. seed-
3-dan und shadian, ahd. scaddn^ scaden „schaden“, got. shapis n. „Schaden“
4-(vgl. den gr. 5-St.), anord.             ,Schaden, Yerlust**, ags.
5-                                         5                                     scado
6-„Schaden“, If omen agentis ags. scada „Schadiger, Missetater, Feind‘‘, as.
7-scatJiOj ahd.        „Schadiger, Feind'^; mit Abtonung o wie im Praeteritum
8-anord. shod „Ungemach, Elend'^, shpdr „schadlich^'.
9-    Zweifelhaft arm. xaiTiarem „zerst6re, vernichte^' (Bugge IF. 1, 447).
10-    S. Osthoflf PBrB. 13,459, Pick 11^ 308, Falk-Torp 978 und 1540.                               —
11-Recht frag wur dig stellt Pedersen KGr. I 176 hieher mir. scUh „mude“, escid
12-„unermudlich“ (cymr. esgiid „flink, rege“ usw. mit nock unklarem Yoc.),
13-woneben mit 5^-Suffix (ibd. II 19) mir. scis „Ermudung“ (die kelt. Gruppe
--
30:sked- „bedecken‘‘?
31-   Ai. chddati (unbelegt), cliaddyati „bedroht, verbirgt“, chdttra-m „Schirm“,
32-cJiadis- n. „Decke, Dach''; mhd. ha^ „Kleid, Rock, Kleidung“ ags. hesteru
33-n. pi. n. jJOeider'^       Z. B. Uhlenbeck Ai. Wb. 94 zw., Pick III^ 69.                 Unsicher.
34-
35-
36-sq(h)ed- „zerspalten, zerstreuen^ (wohl Erw. von seq- „schneiden^‘).
37-  Ai. shhadate          (unbelegt; ware auch als ^sqhnd- mit av. scanday-
38-eiti „zerbricht, vernichtet^*     usw, verkniipfbar,      s.   sqen- „abspalten“; fur eine
39-idg.   Umstellungsform halt Uhlenbeck Ai. Wb. 70 ai. hsadate „zerlegt, ver-
40- teilt, schneidet vor%* nicht iiberzeugend), mp. shastan ^.zerbrechen” (Horn
41-
42-Ifp. Et. 175)   :
--
46:    arm. serf „Span, Holzscheit'^ {sqedri- oder eher sqhedri-; s. Bugge KZ.
47- 32, 57; Hiibschmann Arm. Gr. I 480, gegen welchen Persson Beitr. 148;
48- znm LautL Pedersen KZ. 38, 205; 39, 396);
49-   gr. oyeddvvvjbii (A or.     auch ohne s- Ixedaooaj eyJdao'^ev) ^zersplittere, zer-
50- sprenge, zerstreue^^, oyidvr^Lii     ds,,   ayAdvaf.iai^ xldvajuai „sich zerstreuen          (von
51-                                                                                                  ®
52- Menschenmengen)“ (Yok. wie in 7itTV7]/Lii:7i£rdvvv/^ii u. dgl., s. Brgm.-Thumb
53- 106 m. Lit., nicht nach Persson aaO. auf die Wz. sq{h)eid- zu beziehen).
54-   Das spate oyedr] „Tafel, Blatt% oysddgiov „Tafelchen“ ist nach Prell-
55- witz^ s. V.   —s. auch Hiibschmann aaO.              —
56-                                                  aus lat. scJieda entlehnt, das
57- seinerseits   — vgl. die Form scida — aus gr. oyidr]                  ( :   oyJCoji)   stammt.
```


## [2026-09-14T02:08:28.066Z] TOOL CALL #82: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== KLN scandal\"; grep -n \"scandal,\" KLN_1966.txt | head -3; echo \"=== AFM/FVQ/DOZ اسكلة\"; grep -c \"سكلة\" AFM_pages.txt FVQ_pages.txt DOZ.txt LKT.txt 2>/dev/null; echo \"=== PLA\"; ls incoming/PLA 2>/dev/null | head"
}
```


### [2026-09-14T02:08:28.154Z] TOOL RESULT

```
=== KLN scandal
13619:Derivatives:  eschew-al,  n.,  eschew-er,  n. Eschscholtzia,  n.,  a  genus  of  herbs  of  the  Pa- paveraceae.  —  ModL.,  named  after  the  German botanist  Johann  Friedrich  von  Eschscholtz (1793-1831).  For  the  ending  see  suff.  -ia. esclandre,  n.,  a  scandal,  scandalous  scene.  —  F., fr.  OF.  escandle,  fr.  earlier  escandele,  fr.  L.  scan- dalum.  See  scandal  and  cp.  slander, esclavage,  n.,  necklace.  —  F.,  fit.  ‘slavery’,  fr.
33920:suff.  -ed.  For  a  similar  omission  of  the  final  -d cp.  lawn,  ‘stretch  of  grass’.  Cp.  ascend,  condes¬ cend,  descend,  descent,  escalade,  escalator,  scale, ‘measure’,  scandal,  scandent,  scansion,  scant¬ ling,  slander,  transcend.
33922:scandal,  n.  —  F.  scandale,  fr.  Late  L.  scandalum, ‘cause  of  offense  or  stumbling',  fr.  Gk.  oxctvSa- Xov,  ‘stumbling  block  offense’.  See  scan  and  cp. slander,  which  is  a  doublet  of  scandal.  Cp.  also esclandre.
=== AFM/FVQ/DOZ اسكلة
DOZ.txt:0
FVQ_pages.txt:0
LKT.txt:0
AFM_pages.txt:0
=== PLA
PLA_asbaghi_1988_ia_djvu.txt
PLA_asbaghi_1988_ia.pdf
PLA_pages.txt
```


## [2026-09-14T02:08:34.950Z] TOOL CALL #83: WebSearch

```json
{
 "query": "چادر ریشه‌شناسی فارسی میانه čādur سنسکریت chattra حسن‌دوست"
}
```


### [2026-09-14T02:08:42.732Z] TOOL RESULT

```
Web search results for query: "چادر ریشه‌شناسی فارسی میانه čādur سنسکریت chattra حسن‌دوست"

Links: [{"title":"چادر - معنی در دیکشنری آبادیس","url":"https://abadis.ir/fatofa/%DA%86%D8%A7%D8%AF%D8%B1/"},{"title":"چادر به انگلیسی - معنی در دیکشنری آبادیس","url":"https://abadis.ir/fatoen/%DA%86%D8%A7%D8%AF%D8%B1/"},{"title":"تفاوت میان نسخه‌های «چادر» - دانشنامه الکترونیکی زنان","url":"https://portals.nlai.ir/zanan/index.php?title=%DA%86%D8%A7%D8%AF%D8%B1&diff=prev&oldid=5267"},{"title":"چتر به انگلیسی - معنی در دیکشنری آبادیس","url":"https://abadis.ir/fatoen/%DA%86%D8%AA%D8%B1/"},{"title":"چادر (پوشش زنان) - دانشنامه‌ی اسلامی","url":"https://wiki.ahlolbait.com/%DA%86%D8%A7%D8%AF%D8%B1_(%D9%BE%D9%88%D8%B4%D8%B4_%D8%B2%D9%86%D8%A7%D9%86)"},{"title":"فرهنگ ریشه شناختی فارسی، دکتر محمد حسندوست","url":"https://ariabod.blogfa.com/post/92"},{"title":"دانشنامه فرهنگ مردم ایران - مرکز دائرة المعارف بزرگ اسلامی - کتابخانه مدرسه فقاهت","url":"https://lib.eshia.ir/12294/2/373"}]

Based on the search results, here's what I found regarding the etymological connections you queried:

## Etymology of چادر (Chādr)

The word چادر is derived from Middle Persian čādur. In Pahlavi (Middle Persian), the word čātar or čādur meant "umbrella" or "covering".

## Connection to Sanskrit

There are different views about the root of this word, including the possibility that it may be from the Sanskrit root "chad" meaning "to cover". The word is related to Sanskrit terms like छत्र (chatra) meaning "umbrella, mushroom, shelter".

## Historical Evidence

The earliest written Persian evidence of the word چادر meaning "tent" and "covering" is found in Firdawsi's Shahnameh and texts from the 4th-5th centuries AH.

## Reference Work

Your search query mentions حسن‌دوست (Hasan-Doust). Indeed, Dr. Mohammad Hasandoost authored an etymological dictionary of Persian (Farhang-e Riśe-śenāsī-ye Fārsī) published in 1393 (2014) by the Academy of Persian Language and Literature in a five-volume edition.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-14T02:08:49.408Z] AGENT

Now I'll write the verification file.


## [2026-09-14T02:15:46.768Z] TOOL CALL #84: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-452.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\n\ne0 = {\n \"entry\": 0,\n \"root\": \"Skand, Skend, Sqand, Kand 2\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *skend- / *skand- 'to leap, climb' (Walde–Pokorny II 540 'sqand- aufschnellen, in die Höhe gehn'; Watkins/AHD 'skand-. Also skend-. To leap, climb'; Wiktionary Reconstruction:Proto-Indo-European/skend-)\",\n \"note\": \"The root is real, the language label (Indo-European) is right and the gloss 'to climb, leap' is exactly what the two references Nourai cites print. The four headword spellings are not four separate roots: 'Skand'/'Skend' are the normal ablaut pair (full grade *skend- in Latin de-scendere, o/a-grade *skand- in scandere, skandati); 'Sqand' is simply Walde–Pokorny's 1927 notation, where q writes IE k (WP II 540 heads the entry 'sqand-'); 'Kand 2' is Nourai's own numbering for the s-less by-form and is not documented under this root in WP, Pokorny or Watkins (Pokorny's kand-/skand- 'to glow, shine', IEW 526, is a different root — Nourai's 'Kand 1'). Note that Pokorny 1959 dropped this root as a headword altogether: it is absent both between (s)kamb- (p. 918) and sḱed- (p. 919) and in the skel-/sken- run at pp. 929-930, which is why Nourai correctly cites WLD and AHD here rather than POK.\",\n \"note_fa\": \"ریشهٔ هندواروپاییِ آغازینِ *skend-/*skand- به معنای «بالا رفتن، جستن» ریشه‌ای واقعی است و برچسب زبانی و معنای آن در چارت درست است. چهار صورتی که نورایی در سرواژه آورده چهار ریشهٔ جدا نیستند: Skand و Skend دو گونهٔ آواگردانِ (ablaut) یک ریشه‌اند و Sqand همان صورتی است که والده-پوکورنی در سال ۱۹۲۷ با نویسهٔ q (به‌جای k هندواروپایی) در جلد دوم ص ۵۴۰ چاپ کرده است؛ اما «Kand 2»، یعنی گونهٔ بدون s آغازی، در هیچ‌یک از منابع (والده-پوکورنی، پوکورنی، واتکینز) برای این ریشه گواهی ندارد و تنها شماره‌گذاری درونی خود نورایی است. نکتهٔ درخور توجه آنکه پوکورنی در چاپ ۱۳۳۸/۱۹۵۹ این ریشه را به‌کلی از فهرست سرواژه‌ها حذف کرده است و از همین رو نورایی به‌درستی به WLD و AHD ارجاع داده نه به POK. حاصل: ادعای نورایی دربارهٔ خودِ ریشه درست است.\",\n \"sources\": [W+\"scala\", W+\"%CF%83%CE%BA%CE%AC%CE%BD%CE%B4%CE%B1%CE%BB%CE%BF%CE%BD\", W+\"%E0%A4%B8%E0%A5%8D%E0%A4%95%E0%A4%A8%E0%A5%8D%E0%A4%A6%E0%A4%A4%E0%A4%BF\"],\n \"ref_check\": [\n   {\"ref\": \"WLD:540\", \"status\": \"supports\",\n    \"note\": \"Walde–Pokorny Bd. II p. 540 (local incoming/WLD/WLD_Bd2_pages.txt, form-feed leaf 545; the running head of that leaf literally reads '540 sqand-'): 'sqand- \\\"aufschnellen, in die Höhe gehn\\\". Ai. skándati \\\"schnellt, springt, spritzt\\\", a-skandati \\\"fällt an\\\"; gr. σκανδάληθρον \\\"Stellholz in der Falle\\\", σκάνδαλον \\\"Fallstrick; Anstoß, Ärgernis\\\"; lat. scando, -ere \\\"steigen, sich erheben\\\", scala (*scand-sla) \\\"Stiege, Treppe, Leiter\\\"; mir. sescaind …'. Every box of Nourai's chart that carries WLD:540 (Latin, Sanskrit, Greek) and the *skand-slā form stand on this one page.\"},\n   {\"ref\": \"AHD:1539\", \"status\": \"supports\",\n    \"note\": \"The 1976 New College Edition appendix (pp. 1505-1550) is not open online; its text is the same root list as Watkins 1985 (local AHD_watkins1985.txt), which reads: 'skand-. Also skend-. To leap, climb. 1. Latin scandere, to climb: SCAN, SCANDENT, SCANSION, SCANSORIAL; ASCEND, (CONDESCEND), DESCEND, TRANSCEND. 2. Suffixed form *skand-alo- in Greek skandalon, a snare, trap, stumbling block: SCANDAL. 3. Suffixed form *skand-slā- in Latin scālae, steps, ladder: ECHELON, ESCALADE, SCALE².' Root name, gloss and all three branches of the chart are AHD's; p. 1539 is in the s- stretch of the appendix, so the page reference is consistent.\"}],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. II p. 540 (leaf 545)\", \"stance\": \"supports\", \"note\": \"Heads the entry 'sqand- \\\"aufschnellen, in die Höhe gehn\\\"' — the source of Nourai's 'Sqand' spelling.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. skand-\", \"stance\": \"supports\", \"note\": \"'skand-. Also skend-. To leap, climb.' — no [Pok. …] bracket, consistent with the root's absence from Pokorny 1959.\"},\n   {\"src\": \"POK\", \"where\": \"IEW pp. 916-922 and 929-930 (POK_03.txt leaves 154-168)\", \"stance\": \"silent\", \"note\": \"Pokorny runs skabh- (916), (s)kāi- (916), (s)kamb- (918), (s)k(h)ed- (918), sḱed- (919), skei- (919) and later (s)kel-, skhel-, (s)kem-, (s)ken(d)-, skendh-, (s)keng- (929-930): no skand-/skend- 'to leap' headword at all.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann, cols. s.v. skand- and skendō\", \"stance\": \"partial\", \"note\": \"Mann separates two roots: 'skand- (skandos, ā) \\\"fall, breakdown, ruin\\\" … Gk. cf. skándalon' and 'skendō, iō \\\"dash, rise, fall\\\" … Skt. skándāmi \\\"dash, bound, spurt, drop\\\"; Olr. scendim; Li. skendžiu \\\"sink, drown\\\"' — same material, but the semantics are anchored on 'fall/spring' rather than 'climb'.\"},\n   {\"src\": \"KLN\", \"where\": \"s.v. scan\", \"stance\": \"supports\", \"note\": \"'L. scandere \\\"to climb, mount, scan\\\" … fr. I.-E. base *skand-, \\\"to spring, leap\\\", whence also OI. skandati, \\\"hastens, leaps, jumps\\\", Gk. σκάνδαλον (whence L. scandalum), Mir. sescaind …' — the root and all three of Nourai's branches in one Klein entry.\"}],\n \"nodes\": []\n}\n\nn = e0[\"nodes\"]\n\nn.append({\n \"id\": 1, \"lang\": \"Indo-European\", \"words\": \"Skand-slâ\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Not a daughter language but a suffixed derivative of the root, printed inside the root box itself: *skand-slā- 'instrument for climbing' = the root + the IE instrument-noun suffix *-slo-/*-slā (as in Latin *ped-slā > pēlla?, more securely in *sed-lā > sella, *pō-tlom > pōculum). In Latin the cluster -ndsl- was simplified with compensatory lengthening: *skandslā > *skanslā > *skāslā > scāla, hence the plural scālae 'steps, ladder'. Wiktionary's Latin scala entry gives exactly 'From *skand-slā, from Proto-Indo-European *skend-'; Klein s.v. scale 'measure' gives 'fr. *scand-slā, a derivative of scandere'; Watkins gives 'Suffixed form *skand-slā- in Latin scālae'. Every Western word in this chart's Italian/French/Arabic/Persian chain descends from this one form.\",\n \"derivation_fa\": \"این جعبه زبان جداگانه‌ای نیست، بلکه صورتِ پسوندی خودِ ریشه است که در کتاب درون جعبهٔ ریشه چاپ شده: *skand-slā- از ریشه + پسوند ابزارسازِ هندواروپایی *-slo-/*-slā (همان پسوندی که در sella < *sed-lā لاتین دیده می‌شود). در لاتین خوشهٔ همخوانی -ndsl- ساده شده و با کشش جبرانیِ واکه به scāla بدل گشته است: *skandslā > *skanslā > scāla «نردبان، پله». ویکی‌واژه ذیل scala لاتین همین را می‌آورد و کلاین و واتکینز نیز عیناً *scand-slā را بازسازی کرده‌اند. تمام زنجیرهٔ ایتالیایی-فرانسوی-عربی-فارسیِ این چارت از همین صورت سرچشمه می‌گیرد؛ ادعای نورایی درست است.\",\n \"sources\": [W+\"scala\"],\n \"ref_check\": [{\"ref\": \"(none cited)\", \"status\": \"not_checked\", \"note\": \"The form stands inside the root box and carries no reference of its own; the root's own references (WLD:540, AHD:1539) both print it — WP II 540 'scala (*scand-sla)', Watkins 'Suffixed form *skand-slā- in Latin scālae'.\"}],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. II p. 540\", \"stance\": \"supports\", \"note\": \"'lat. scando, -ere \\\"steigen, sich erheben\\\", scala (*scand-sla) \\\"Stiege, Treppe, Leiter\\\"'.\"},\n   {\"src\": \"KLN\", \"where\": \"s.v. scale, n., measure (KLN_1966.txt l. 33904)\", \"stance\": \"supports\", \"note\": \"'ME. \\\"ladder, staircase\\\", fr. L. scalae (pl.) (either directly or through the medium of It. scala), \\\"ladder, staircase\\\", fr. *scand-slā, a derivative of scandere, \\\"to climb\\\". See scan and cp. escalade, escalator.'\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. skand- §3\", \"stance\": \"supports\", \"note\": \"'Suffixed form *skand-slā- in Latin scālae, steps, ladder: ECHELON, ESCALADE, SCALE².'\"}]})\n\nn.append({\n \"id\": 2, \"lang\": \"Latin\", \"words\": \"scandere; scâlae\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Latin scandō, scandere 'to climb, mount' continues the thematic present *skénd-e-ti, the very formation that Sanskrit skandati continues; the a-vocalism of scandō is the regular Latin outcome of the syllabic/zero-grade before a nasal (*skṇd- > scand-), with the e-grade surviving in the compounds ascendere, descendere, trānscendere (a > e by medial vowel weakening, as Klein notes s.v. ascend: 'For the change of Latin a (in scandere) to e (in as-cendere) see accent'). scālae (plural only, 'steps, ladder, staircase') is the instrument noun *skand-slā, whence Italian scala, Old French eschele/eschale > French échelle, and English scale 'ladder, measure'. In post-classical usage scāla singular replaces the plural, and that singular is what the Mediterranean trade languages borrowed.\",\n \"derivation_fa\": \"فعل scandō/scandere لاتین «بالا رفتن» دنبالهٔ همان ستاک حال *skénd-e-ti است که skandati سنسکریت نیز از آن آمده؛ واکهٔ a در scandō بازتاب منظم صورت بی‌درجهٔ ریشه پیش از خیشوم است (*skṇd- > scand-) و درجهٔ e در ترکیب‌های ascendere و descendere برجای مانده که در آنها a به e بدل شده است (ضعیف‌شدگی واکه در هجای میانی). اسم ابزارِ scālae (جمع، «پله، نردبان») از *skand-slā ساخته شده و در لاتین متأخر صورت مفرد scāla جای جمع را گرفته؛ همین مفرد است که به ایتالیایی scala و فرانسوی échelle و از راه دریانوردی مدیترانه به ترکی و عربی و فارسی رسیده است. ادعای نورایی درست است.\",\n \"sources\": [W+\"scala\"],\n \"ref_check\": [{\"ref\": \"WLD:540\", \"status\": \"supports\", \"note\": \"WP II 540 s.v. sqand-: 'lat. scando, -ere \\\"steigen, sich erheben\\\", scala (*scand-sla) \\\"Stiege, Treppe, Leiter\\\"' — both Latin words of the box, with the same glosses Nourai gives.\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.vv. scan, ascend, descend, scale 'measure'\", \"stance\": \"supports\", \"note\": \"'L. scandere, \\\"to climb, mount, scan\\\" (whence ascendere … descendere), fr. I.-E. base *skand-'; and scale 'measure' fr. L. scalae fr. *scand-slā.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. skand- §§1,3\", \"stance\": \"supports\", \"note\": \"'1. Latin scandere, to climb … 3. Suffixed form *skand-slā- in Latin scālae, steps, ladder.'\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. II p. 540\", \"stance\": \"supports\", \"note\": \"See ref_check; the Latin forms are cited there verbatim.\"}]})\n\nn.append({\n \"id\": 3, \"lang\": \"Italian\", \"words\": \"scalo\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Italian scala 'ladder, staircase' is the direct continuation of Latin scāla; scalo, its masculine deverbal partner (from scalare 'to scale, to put in at a port'), means 'slipway, landing place, port of call, stopover' — precisely the 'ladder, platform, wharf' of the box. The semantic bridge is the boarding-ladder let down at a landing stage: from the 12th c. the Genoese and Venetian trading stations of the eastern Mediterranean were the scale (French échelles du Levant, 'the Levant landing-places'), and it is that mercantile sense that was carried into Ottoman Turkish and Arabic. The one refinement the chart needs is that the form actually exported east is the feminine scala, not scalo (see node #4).\",\n \"derivation_fa\": \"واژهٔ scala ایتالیایی «نردبان، پلکان» دنبالهٔ مستقیم scāla لاتین است و scalo صورت مذکرِ برگرفته از فعل scalare («بالا رفتن؛ در بندری پهلو گرفتن») است به معنای «شیب فرودِ کشتی، لنگرگاه، بندرِ توقف» — همان «نردبان، سکو، اسکله»ای که نورایی آورده است. پیوند معنایی از نردبانِ سوارشدن به کشتی پدید آمده: از سدهٔ ششم هجری، تجارتخانه‌های جنووا و ونیز در سواحل شرقی مدیترانه را scale (در فرانسوی échelles du Levant) می‌نامیدند و همین کاربردِ بازرگانی بود که به ترکی عثمانی و عربی راه یافت. تنها نکتهٔ اصلاحی آنکه صورتی که به شرق رفت مؤنثِ scala بود نه scalo (نگاه کنید به گرهٔ ۴).\",\n \"sources\": [W+\"scalo\", W+\"scala\"],\n \"ref_check\": [{\"ref\": \"(none cited)\", \"status\": \"not_checked\", \"note\": \"No reference in the printed box; checked against Wiktionary (scalo, scala) and Klein (see consulted).\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.v. scale, n., measure\", \"stance\": \"supports\", \"note\": \"Klein lets the Romance word carry the Latin one on: English scale 'ladder' comes from L. scalae 'either directly or through the medium of It. scala' — i.e. It. scala continues L. scāla.\"},\n   {\"src\": \"WEB\", \"where\": \"—\", \"stance\": \"silent\", \"note\": \"Webster's New Twentieth Century (vol. 1 only, A–…) has no Italian scalo entry; nothing usable.\"},\n   {\"src\": \"LKT\", \"where\": \"grep 'scala', 'iskele' in LKT.txt\", \"stance\": \"silent\", \"note\": \"Lokotsch (European words of Oriental origin) has no entry — expected, since this word travelled in the opposite direction, from Europe into the Orient.\"}]})\n\nn.append({\n \"id\": 4, \"lang\": \"Arabic\", \"words\": \"eskeleh\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Arabic إسكلة (iskala/iskila) 'landing stage, wharf; ladder' is indeed a Mediterranean-trade loan from Italian — al-Unaysi's TAD p. 4 says so in as many words — but the Italian etymon is the feminine scala, not the masculine scalo of the parent box: إسكلة keeps the feminine ending (-a rendered as -ة) and the sense 'ladder → landing stage' of scala. The prothetic i- is the regular Arabic (and Turkish) repair of an impossible initial sk- cluster (cf. إسطبل < stabulum, إسكندر < Alexandros). The word belongs to the Ottoman-Levantine trade vocabulary of the 16th-19th c. and is in most ports indistinguishable from Ottoman Turkish iskele, which has the same source; Wiktionary treats Turkish iskele as inherited from Ottoman Turkish اسكله, from Italian scala. Verdict plausible rather than confirmed only because of the scalo/scala slip in the immediate parent.\",\n \"derivation_fa\": \"واژهٔ عربی «إسكلة» به معنای «بارانداز، لنگرگاه؛ نردبان» به‌راستی وام‌واژه‌ای از ایتالیایی است — طوبیا العنیسی در ص ۴ همین را می‌گوید — اما صورتِ مأخوذ، مؤنثِ scala است نه مذکرِ scalo که نورایی در جعبهٔ بالادست آورده: «إسكلة» پایانهٔ مؤنثِ -a را به‌صورت ة نگاه داشته و معنای «نردبان ← بارانداز» را نیز از scala گرفته است. همزهٔ آغازی (إ-) همان درمانِ همیشگیِ عربی (و ترکی) برای خوشهٔ ناممکنِ sk- در آغاز واژه است، چنان‌که در «إسطبل» از stabulum و «إسكندر» از Alexandros. این واژه به واژگانِ بازرگانیِ عثمانی-شامی سده‌های دهم تا سیزدهم هجری تعلق دارد و در بیشتر بنادر از iskele ترکی عثمانی (با همان خاستگاه) تفکیک‌پذیر نیست. داوری «با احتیاط پذیرفتنی» تنها به سبب همان لغزشِ scalo به‌جای scala است.\",\n \"sources\": [W+\"iskele\"],\n \"ref_check\": [{\"ref\": \"TAD:4\", \"status\": \"supports\", \"note\": \"Tobia al-Unaysi, Tafsir al-alfaz al-dakhila, local TAD_pages.txt form-feed leaf 6 (the alif section, printed p. 4): 'إسكلة - ايطالي scala وهو معدول عن … أى دراج ويراد به …' — 'iskila: Italian scala, it is a modification of …, i.e. a ladder/stairs, and what is meant by it is …'. Exactly Nourai's claim that the Arabic word is a loan from Italian, though the Italian form named is scala, not scalo.\"}],\n \"consulted\": [\n   {\"src\": \"AFM\", \"where\": \"grep 'سكلة' in AFM_pages.txt → 0 hits\", \"stance\": \"silent\", \"note\": \"Addi Shir lists only Persian words Arabicized; a European loan of this kind is outside his scope.\"},\n   {\"src\": \"FVQ\", \"where\": \"grep 'سكلة' in FVQ_pages.txt → 0 hits\", \"stance\": \"silent\", \"note\": \"Jeffery covers Qur'anic foreign vocabulary only; the word is post-classical.\"},\n   {\"src\": \"DOZ\", \"where\": \"grep 'سكلة'/'escala' in DOZ.txt → 0 hits\", \"stance\": \"silent\", \"note\": \"Dozy's Spanish-Arabic glossary has no matching entry.\"},\n   {\"src\": \"PLA\", \"where\": \"Asbaghi, Persische Lehnwörter im Arabischen\", \"stance\": \"silent\", \"note\": \"Not a Persian loan in Arabic, so absent — relevant only to show the direction of borrowing is not Persian → Arabic here.\"},\n   {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/iskele\", \"stance\": \"partial\", \"note\": \"'Inherited from Ottoman Turkish iskele, from Italian scala' — same ultimate source, but the Levantine chain usually runs through Ottoman Turkish, and the entry names scala, not scalo.\"}]})\n\nn.append({\n \"id\": 5, \"lang\": \"Persian\", \"words\": \"eskeleh «اسکله»\",\n \"verdict\": \"plausible\",\n \"derivation\": \"New Persian اسکله eskele 'wharf, quay, landing stage' is certainly the same Mediterranean word, and Mo'in tags it exactly as Nourai draws it: '[معر.] (اِ.) در اصل ایتالیایی' — 'Arabicized, originally Italian, meaning port, ship's landing place', while Dehkhoda writes 'از ایتالیایی اسکالا' and records the by-forms اسقاله، سقاله، اصقالة. The competing modern account (Wiktionary) takes the Persian word from Ottoman Turkish اسكله iskele rather than from Arabic; since Persian Gulf and Caspian port vocabulary came in both through Arabic-speaking ports and through Ottoman/Azerbaijani channels, and since the Arabic and Turkish forms are homographic (إسكلة / اسكله), the mediation cannot be decided on form alone — the vowel of the Persian word (eskele, not iskele) slightly favours the Arabic route Nourai and Mo'in give. Ultimate source Italian scala in every account; only the middleman is uncertain, hence plausible.\",\n \"derivation_fa\": \"«اسکله» در فارسی نو همان واژهٔ مدیترانه‌ای است و معین دقیقاً همان مسیری را نشان می‌دهد که نورایی رسم کرده است: «[معر.] (اِ.) در اصل ایتالیایی به معنای بندر، بارانداز کشتی»؛ دهخدا نیز می‌نویسد «از ایتالیایی اسکالا» و صورت‌های دیگرِ اسقاله، سقاله و اصقالة را ثبت کرده است. در برابر، ویکی‌واژه آن را وام‌واژه‌ای از ترکی عثمانیِ اسكله می‌داند نه از عربی. چون واژگان بندریِ خلیج فارس و دریای مازندران هم از راه بنادر عرب‌زبان و هم از مجرای عثمانی/آذربایجانی وارد شده و صورت نوشتاری عربی و ترکی یکی است، میانجی را از روی خودِ واژه نمی‌توان قطعی کرد؛ تنها واکهٔ آغازی فارسی (eskele نه iskele) اندکی به سود مسیر عربیِ مورد نظر نورایی و معین است. خاستگاه نهایی در هر دو روایت scala ایتالیایی است، پس داوری: با احتیاط پذیرفتنی.\",\n \"sources\": [\"https://abadis.ir/fatofa/%D8%A7%D8%B3%DA%A9%D9%84%D9%87/\", W+\"%D8%A7%D8%B3%DA%A9%D9%84%D9%87\", W+\"iskele\"],\n \"ref_check\": [{\"ref\": \"MON:271\", \"status\": \"supports\", \"note\": \"The six-volume Farhang-e Farsi is not online, so the page number itself cannot be checked; the entry text is on abadis.ir/fatofa/اسکله (archived): 'فرهنگ معین — اسکله: (اِ کَ یا کِ لِ) [معر.] (اِ.) در اصل ایتالیایی به معنای بندر، بارانداز کشتی' — Mo'in marks it 'Arabicized' and 'originally Italian', which is precisely the Italian → Arabic → Persian chain Nourai draws. p. 271 falls in the الف section of vol. 1, consistent with اسکله.\"}],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"2-vol. Adena abridgement, MON_part1.txt s.v. اسکله\", \"stance\": \"supports\", \"note\": \"'اسکله: … (ا.) بندر، لنگرگاه، بارانداز کشتی‌ها' with a (badly OCRed) Latin-script European etymon before the definition.\"},\n   {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' (17th c.)\", \"stance\": \"silent\", \"note\": \"A modern maritime loan; not in the Borhan, as expected.\"},\n   {\"src\": \"HRN\", \"where\": \"grep in HRN.txt\", \"stance\": \"silent\", \"note\": \"Horn's Grundriss (1893) has no entry — it treats inherited Iranian vocabulary, not modern European loans.\"},\n   {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/اسکله\", \"stance\": \"partial\", \"note\": \"'Borrowed from Ottoman Turkish اسكله (iskele), from Italian scala' — same origin, different middleman from Nourai's Arabic.\"}]})\n\nn.append({\n \"id\": 6, \"lang\": \"French\", \"words\": \"ascenseur; eschelle\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Two French words from two different Latin derivatives of the same verb. (a) ascenseur 'lift, elevator' is a learned 19th-c. formation on Latin ascēnsor (ad- + scandere, past participle stem ascēns-), coined in French for the new machine (Wiktionary: 'learned borrowing from Latin ascēnsor … from ascendō'); it is not an inherited word, which is why it shows -sc- and -eur rather than a popular outcome. (b) eschelle is the Old/Middle French spelling of modern échelle 'ladder, scale', inherited from Latin scāla (Old French eschele, also eschale, eskele; initial e- is the regular French prothesis before s + consonant, as in escole, estable; -s- was later lost and marked by the accent: eschelle > échelle). English echelon (French échelon 'rung of a ladder') is the same word, and Watkins files ECHELON under skand- §3.\",\n \"derivation_fa\": \"دو واژهٔ فرانسوی از دو مشتق لاتینِ یک فعل. نخست ascenseur «آسانسور» که واژه‌ای عالمانه و ساختهٔ سدهٔ نوزدهم میلادی بر پایهٔ ascēnsor لاتین (از ad- + scandere) است و برای دستگاه تازه‌اختراعِ بالابر وضع شده؛ چون وام‌واژه‌ای کتابی است، خوشهٔ -sc- و پایانهٔ -eur در آن دست‌نخورده مانده است. دوم eschelle که املای فرانسوی کهن و میانهٔ échelle امروزی است و به‌طور موروثی از scāla لاتین آمده: در فرانسوی کهن eschele/eschale، با e آغازیِ افزوده (پیشوندِ کمکی پیش از خوشهٔ s + همخوان، مانند escole و estable) و سپس افتادن s که با علامت é نشان داده شده است. واژهٔ échelon («پلهٔ نردبان») و انگلیسیِ echelon نیز از همین ریشه‌اند و واتکینز ECHELON را ذیل *skand-slā آورده است. ادعای نورایی درست است.\",\n \"sources\": [W+\"ascenseur\", W+\"%C3%A9chelle\", W+\"eschele\"],\n \"ref_check\": [{\"ref\": \"(none cited)\", \"status\": \"not_checked\", \"note\": \"No reference in the printed box; checked against Wiktionary (ascenseur, échelle, eschele), Klein and Watkins — see consulted.\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.v. ascend\", \"stance\": \"supports\", \"note\": \"'L. ascendere, \\\"to climb up, mount\\\", fr. ad- and scandere, \\\"to climb\\\"' — the base of ascēnsor > ascenseur.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. skand- §3\", \"stance\": \"supports\", \"note\": \"ECHELON (i.e. Fr. échelle/échelon) and ESCALADE are filed under the *skand-slā branch, exactly as the chart puts eschelle under Latin scālae.\"},\n   {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/eschele\", \"stance\": \"supports\", \"note\": \"Old French eschele 'ladder', 'Inherited from Latin scāla', alternative forms eschale, eskele; descendant French échelle.\"}]})\n\nn.append({\n \"id\": 7, \"lang\": \"Persian\", \"words\": \"âsânsor «آسانسور»; ešel «اشل»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Both are 20th-century French loans, taken in during the Qajar-to-Pahlavi period of French-language technical and administrative borrowing. آسانسور âsânsor 'lift, elevator' is French ascenseur with the usual Persian treatment of French nasal + -eur (ascenseur → âsânsor); Wiktionary lists Persian آسانسور explicitly among the descendants of French ascenseur. Its shape is reinforced by folk etymology with Persian آسان 'easy', which is why it is spelt with آسان- and not اسان-, but the word is not Persian in formation. اشل ešel is French échelle in its figurative administrative sense 'scale (of salaries), grade' (échelle des traitements) and in the draughtsman's sense 'scale of a drawing': Mo'in gives '[فر.] ۱- امتیاز کارمند از نظر درجه و مقام اداری …، پایه، رتبه ۲- رابطهٔ میان اندازهٔ واقعی چیزی با اندازهٔ نقشه و نمودار آن، مقیاس'. Since échelle continues Latin scāla, the box hangs correctly under the French node.\",\n \"derivation_fa\": \"هر دو وام‌واژهٔ فرانسویِ سدهٔ چهاردهم خورشیدی‌اند و در دورهٔ وام‌گیری گستردهٔ اصطلاحات فنی و اداری از فرانسه وارد فارسی شده‌اند. «آسانسور» همان ascenseur فرانسوی است با تطبیق آواییِ معمولِ فارسی برای واکهٔ خیشومی و پایانهٔ -eur؛ ویکی‌واژه نیز «آسانسور» فارسی را در فهرست بازماندگان ascenseur آورده است. املای آن با «آسان-» نتیجهٔ ریشه‌شناسی عامیانه با واژهٔ فارسی «آسان» است، وگرنه ساختِ واژه فارسی نیست. «اشل» نیز همان échelle فرانسوی است در معنای مجازیِ اداری «پایه و رتبهٔ حقوقی» (échelle des traitements) و در معنای نقشه‌کشیِ «مقیاس»؛ معین می‌نویسد: «[فر.] ۱- امتیاز کارمند از نظر درجه و مقام اداری…، پایه، رتبه ۲- رابطهٔ میان اندازهٔ واقعی چیزی با اندازهٔ نقشه و نمودار آن، مقیاس». چون échelle دنبالهٔ scāla لاتین است، جای این جعبه زیر گرهٔ فرانسوی درست است.\",\n \"sources\": [W+\"ascenseur\", \"https://abadis.ir/fatofa/%D8%A7%D8%B4%D9%84/\", W+\"%C3%A9chelle\"],\n \"ref_check\": [{\"ref\": \"MON:51,288\", \"status\": \"supports\", \"note\": \"Page numbers in the 6-vol. Mo'in cannot be checked (not online), but they are consistent: p. 51 is in the آ- stretch of vol. 1 (آسانسور) and p. 288 in the ا-ش stretch (اشل). The entries themselves, on abadis.ir (archived): فرهنگ معین 'اشل: … [فر.] ۱- امتیاز کارمند از نظر درجه و مقام اداری و دریافت حقوق، پایه، رتبه ۲- … مقیاس' — Mo'in's tag [فر.] = French, exactly Nourai's arrow.\"}],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"2-vol. Adena abridgement, MON_part1.txt s.v. اشل\", \"stance\": \"supports\", \"note\": \"'اشل: … [نردبان مقیاس، پایه] (.) رتبهٔ کارمندان دولتی؛ پایه. دون اشل: کارمندی که رتبه ندارد …' — the French 'ladder/scale' sense glossed in Persian.\"},\n   {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/ascenseur (descendants)\", \"stance\": \"supports\", \"note\": \"Persian آسانسور (âsânsor) is listed among the borrowings from French ascenseur, beside Turkish asansör and Spanish ascensor.\"},\n   {\"src\": \"HUB\", \"where\": \"grep in HUB.txt\", \"stance\": \"silent\", \"note\": \"Hübschmann's Persische Studien (1895) predates both loans; silent, as expected.\"}]})\n\nn.append({\n \"id\": 8, \"lang\": \"English\", \"words\": \"scan, ascend, descend, escalator, scale\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"All five are in AHD's list under skand-. scan < Latin scandere, first in the prosodist's sense 'to scan verse' (to mark its 'climbing' feet), whence 'examine closely'; the -d was lost by confusion with the past-participle suffix -ed (Klein). ascend < Latin ascendere (ad- + scandere), descend < Old French descendre < Latin descendere. escalator is an 1900 Otis Elevator Co. trade name 'coined from escalade + -ator in elevator' (Etymonline), escalade itself being French/Italian scalata < scala < Latin scāla. scale 'ladder, graduated measure' is Middle English scale 'ladder, staircase' from Latin scālae, directly or through Italian scala. One caution the box does not give: English has three homonymous nouns scale, and only this one belongs here — scale 'weighing pan' (from Old Norse skál) and scale 'of a fish' (from Frankish/Old French escale) both belong to PIE *(s)kel- 'to cut, cleave' (Klein), which is why Watkins writes SCALE² and not plain SCALE.\",\n \"derivation_fa\": \"هر پنج واژه در فهرست واتکینز ذیل *skand- آمده‌اند. scan از scandere لاتین است، نخست در معنای عروضیِ «تقطیع کردن شعر» و سپس «به‌دقت نگریستن»؛ حرف -d پایانی به سببِ اشتباه‌شدن با پسوند -ed افتاده است (کلاین). ascend از ascendere و descend از طریق فرانسوی کهن descendre از descendere لاتین آمده‌اند. escalator نام تجاریِ ساختهٔ شرکت اوتیس در ۱۹۰۰ م است، برساخته از escalade + پایانهٔ -ator (به قیاس elevator)، و خودِ escalade از scalata ایتالیایی و scala لاتین است. scale به معنای «نردبان، مقیاس مدرج» از scālae لاتین (مستقیم یا از راه scala ایتالیایی) آمده. یک هشدار که در جعبهٔ کتاب نیامده: در انگلیسی سه واژهٔ هم‌نگارهٔ scale هست و تنها همین یکی به این ریشه تعلق دارد؛ scale «کفهٔ ترازو» (از نورس کهن skál) و scale «فلس ماهی» (از فرانسوی کهن escale) هر دو از ریشهٔ هندواروپایی *(s)kel- «بریدن، شکافتن»اند — از همین روست که واتکینز SCALE² می‌نویسد نه SCALE.\",\n \"sources\": [\"https://www.etymonline.com/word/escalator\"],\n \"ref_check\": [{\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. skand-: '1. Latin scandere, to climb: SCAN, SCANDENT, SCANSION, SCANSORIAL; ASCEND, (CONDESCEND), DESCEND, TRANSCEND … 3. Suffixed form *skand-slā- in Latin scālae, steps, ladder: ECHELON, ESCALADE, SCALE².' Four of Nourai's five words appear verbatim; escalator is not in Watkins' list but is a derivative of ESCALADE, which is.\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.vv. scan, ascend, descend, scale 'measure', scale 'weighing instrument', scale 'of fish'\", \"stance\": \"partial\", \"note\": \"Supports scan/ascend/descend/scale 'measure' ('fr. *scand-slā'), but expressly derives the other two scale nouns from I.-E. base *(s)qel- 'to cut, cleave, split' — so the bare 'scale' of the box is ambiguous.\"},\n   {\"src\": \"ETYM\", \"where\": \"etymonline.com/word/escalator\", \"stance\": \"supports\", \"note\": \"'1900, American English, trade name of an Otis Elevator Co. moving staircase, coined from escalade + -ator in elevator' — and escalade traces to Latin scala/scandere.\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat, s.v. transcend/scansion\", \"stance\": \"supports\", \"note\": \"'Scansion. (L.) From L. scansio … scandere'; 'Transcend. L. transcendere … scandere, to climb.'\"}]})\n\nn.append({\n \"id\": 9, \"lang\": \"Sanskrit\", \"words\": \"skandati\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Vedic/Sanskrit skándati '(he) leaps, springs, spurts, drops' is the thematic present *skénd-e-ti of the root, the exact formal match of Latin scandō; the Sanskrit a is the regular Indo-Aryan outcome of IE e (and of o), so skánd- : scand- : Greek skand- all reflect one paradigm. The semantic range of the Sanskrit verb ('to leap, hop, spring' and, in the opposite direction, 'to drop, fall down; to spurt, emit') is what led Mann to set up a second root skand- 'fall, ruin' (Skt. skandaḥ 'destruction'); Nourai's gloss 'jumps, speeds' follows WP's 'schnellt, springt, spritzt' closely. The compound ā-skandati 'attacks, falls upon' cited by WP shows the same double-facing semantics.\",\n \"derivation_fa\": \"فعل skándati در سنسکریت ودایی و کلاسیک «می‌جهد، می‌پرد، می‌ریزد» ستاک حالِ درون‌مایه‌ایِ *skénd-e-ti است و از نظر صرفی دقیقاً برابر scandō لاتین؛ واکهٔ a در سنسکریت بازتاب منظمِ e (و o) هندواروپایی است، پس skánd- و scand- و skand- یونانی هر سه یک صیغهٔ واحدند. دامنهٔ معناییِ این فعل («جستن، پریدن» و در سوی مقابل «افتادن، فروچکیدن، پاشیدن») سبب شده مان (Mann) ریشهٔ دومی با معنای «افتادن، ویرانی» (skandaḥ سنسکریت «نابودی») بازسازی کند. معنایی که نورایی داده («می‌جهد، می‌شتابد») نزدیک به همان «schnellt, springt, spritzt» والده-پوکورنی است. ادعای نورایی درست است.\",\n \"sources\": [W+\"%E0%A4%B8%E0%A5%8D%E0%A4%95%E0%A4%A8%E0%A5%8D%E0%A4%A6%E0%A4%A4%E0%A4%BF\"],\n \"ref_check\": [{\"ref\": \"WLD:540\", \"status\": \"supports\", \"note\": \"WP II 540 s.v. sqand-, first item: 'Ai. skándati \\\"schnellt, springt, spritzt\\\", a-skandati \\\"fällt an\\\"' — the form, the language and effectively the gloss of Nourai's box.\"}],\n \"consulted\": [\n   {\"src\": \"IEC\", \"where\": \"Mann s.v. skendō\", \"stance\": \"supports\", \"note\": \"'Skt. skándāmi, v. \\\"dash, bound, spurt, drop\\\"; a-skandami, v. \\\"attack\\\"' — with Av. skand-/skend- 'smash, ruin' beside it.\"},\n   {\"src\": \"KLN\", \"where\": \"s.v. scan\", \"stance\": \"supports\", \"note\": \"'OI. skandati, \\\"hastens, leaps, jumps\\\"' cited as the Indic member of the same base *skand-.\"},\n   {\"src\": \"POK\", \"where\": \"IEW\", \"stance\": \"silent\", \"note\": \"Pokorny 1959 has no headword for this root, so skandati is not treated there (see the root-level note).\"},\n   {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/स्कन्दति\", \"stance\": \"supports\", \"note\": \"'to leap, jump, hop, spring; to drop, fall down … From Proto-Indo-European *skénd-e-ti, from the root *skend-', cognate Latin scandō.\"}]})\n\nn.append({\n \"id\": 10, \"lang\": \"Greek\", \"words\": \"skandalon\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Ancient Greek σκάνδαλον 'trap, snare; stumbling block, cause of offence' is traditionally a suffixed *skand-alo- beside σκανδάληθρον, the trigger-stick of a trap ('the piece that springs up'), and that is how Walde-Pokorny, Klein and Watkins all take it: WP II 540 files both Greek words under sqand- and gives the semantic parallel 'the thing that snaps up'. Modern Greek etymology is much less sure: Beekes (via Wiktionary) rejects the Indo-European derivation on formal and semantic grounds — the suffix -αλ- is not a Greek instrument suffix, the sense 'trap' does not follow from 'leap', and he proposes a Pre-Greek substrate word, allowing at most a loan from some lost IE language. Mann, for his part, puts σκάνδαλον under a different root skand- 'fall, breakdown', comparing German Falle 'snare' : fallen 'to fall'. So the derivation is respectable and is what Nourai's own reference prints, but it is no longer the consensus — hence plausible rather than confirmed.\",\n \"derivation_fa\": \"واژهٔ یونانی باستان σκάνδαλον «دام، تله؛ سنگِ لغزش، مایهٔ آزار» بنا بر تحلیل سنتی صورت پسوندیِ *skand-alo- است، در کنار σκανδάληθρον «چوبِ ماشهٔ دام» («آنچه ناگهان می‌جهد»)؛ والده-پوکورنی، کلاین و واتکینز هر سه همین را می‌گویند و WP در جلد دوم ص ۵۴۰ هر دو واژهٔ یونانی را ذیل sqand- آورده است. اما ریشه‌شناسی امروزی چندان مطمئن نیست: بیکس (به نقل ویکی‌واژه) این اشتقاق را از نظر صوری و معنایی رد می‌کند — پسوند -αλ- در یونانی پسوند ابزارساز نیست و معنای «دام» از «جستن» برنمی‌آید — و آن را واژه‌ای از بستر پیش‌یونانی می‌داند. مان نیز σκάνδαλον را ذیل ریشهٔ دیگری با معنای «افتادن، ویرانی» نهاده و آن را با جفتِ آلمانیِ Falle «دام» : fallen «افتادن» سنجیده است. پس اشتقاق نورایی محترم و برگرفته از منبع خود اوست، ولی دیگر اجماعی نیست: با احتیاط پذیرفتنی.\",\n \"sources\": [W+\"%CF%83%CE%BA%CE%AC%CE%BD%CE%B4%CE%B1%CE%BB%CE%BF%CE%BD\", W+\"scandalum\"],\n \"ref_check\": [{\"ref\": \"WLD:540\", \"status\": \"supports\", \"note\": \"WP II 540 s.v. sqand-: 'gr. σκανδάληθρον \\\"Stellholz in der Falle\\\" (\\\"*losschnellend\\\"; Bed.-Parallele bei Osthoff …), σκάνδαλον \\\"Fallstrick; Anstoß, Ärgernis\\\"' — both the form and the 'stumbling block, trap' gloss of the box.\"}],\n \"consulted\": [\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. skand- §2\", \"stance\": \"supports\", \"note\": \"'Suffixed form *skand-alo- in Greek skandalon, a snare, trap, stumbling block: SCANDAL.'\"},\n   {\"src\": \"IEC\", \"where\": \"Mann s.v. skand- 'fall, breakdown, ruin'\", \"stance\": \"partial\", \"note\": \"'Gk. cf. skándalon, n. \\\"snare; offence, disgrace\\\". For sense cf. G Falle \\\"snare\\\": fallen \\\"fall\\\"' — kept in the family, but under the 'fall' root, not the 'climb' one.\"},\n   {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/σκάνδαλον (Beekes)\", \"stance\": \"contradicts\", \"note\": \"Beekes 'expresses skepticism about the Indo-European derivation, citing problematic semantics and unexplained phonetic features', proposing a Pre-Greek origin.\"},\n   {\"src\": \"KLN\", \"where\": \"s.v. scan\", \"stance\": \"supports\", \"note\": \"Klein cites 'Gk. σκάνδαλον (whence L. scandalum), \\\"stumbling block, offense\\\"' as a witness of base *skand-.\"}]})\n\nn.append({\n \"id\": 11, \"lang\": \"English\", \"words\": \"scandal\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Greek σκάνδαλον was taken over by Hellenistic Jewish Greek: in the Septuagint it renders Hebrew mōqēš 'snare' and mikšōl 'stumbling block', and from there passes into the New Testament as the 'stumbling block' of the Gospels, which is how it entered Christian Latin as Late Latin scandalum 'cause of offence, temptation' (Vulgate). French scandale (a learned reshaping of the older popular Old French escandle/escandele) gave English scandal in the 1580s, first 'discredit to religion by a religious person', then 'damage to one's reputation'. Klein: 'scandal, n. — F. scandale, fr. Late L. scandalum … fr. Gk. σκάνδαλον … cp. slander, which is a doublet of scandal' — slander coming through the popular Old French esclandre. Since the node's own link (Greek → English) is uncontroversial, it is confirmed even though the Greek word's deeper origin is disputed (node #10).\",\n \"derivation_fa\": \"واژهٔ یونانی σκάνδαλον در یونانیِ یهودیِ دورهٔ هلنیستی کاربرد تازه یافت: در ترجمهٔ سبعینیه (سپتواگینت) برابرِ عبریِ mōqēš «دام» و mikšōl «سنگِ لغزش» نهاده شد و از همان‌جا به عهد جدید و سپس به لاتینِ کلیسایی راه یافت: scandalum در لاتین متأخر «مایهٔ لغزش و وسوسه» (ترجمهٔ ولگات). از فرانسوی scandale — که بازسازیِ عالمانهٔ صورت مردمیِ فرانسوی کهن escandle است — واژهٔ انگلیسی scandal در دههٔ ۱۵۸۰ م وارد شد، نخست به معنای «بدنام کردن دین» و سپس «لطمه به آبرو». کلاین می‌نویسد: «scandal از فرانسوی scandale، از لاتین متأخر scandalum، از یونانی σκάνδαλον … و slander دوگانهٔ (doublet) آن است» که از راه صورت مردمیِ esclandre آمده است. چون خودِ این پیوند (یونانی ← انگلیسی) بی‌مناقشه است، داوری «درست» است، هرچند خاستگاه ژرف‌ترِ واژهٔ یونانی محل بحث است (گرهٔ ۱۰).\",\n \"sources\": [\"https://www.etymonline.com/word/scandal\", W+\"scandalum\"],\n \"ref_check\": [{\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. skand- §2 ends the entry with the English derivative in caps: 'Greek skandalon, a snare, trap, stumbling block: SCANDAL.'\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.v. scandal (KLN_1966.txt l. 33922)\", \"stance\": \"supports\", \"note\": \"'scandal, n. — F. scandale, fr. Late L. scandalum, \\\"cause of offense or stumbling\\\", fr. Gk. σκάνδαλον, \\\"stumbling block offense\\\". See scan and cp. slander, which is a doublet of scandal.'\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat s.v. scandal/slander\", \"stance\": \"supports\", \"note\": \"'Scandal. (F.-L.-Gk.) F. scandale … Gk. σκάνδαλον, a snare … the spring of a trap, the stick which flew up when the trap was shut'; 'Slander … O.F. esclandre … another form of scandal (above).'\"},\n   {\"src\": \"ETYM\", \"where\": \"etymonline.com/word/scandal\", \"stance\": \"supports\", \"note\": \"'from Late Latin scandalum \\\"cause for offense, stumbling block, temptation\\\" … from Greek skandalon \\\"a stumbling block, offense; a trap or snare laid for an enemy\\\"' … English sense 'damage to one's reputation' from the 1580s.\"}]})\n\ne4 = {\n \"entry\": 4,\n \"root\": \"Sked 2\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *sḱed- 'to cover' (Pokorny IEW 919, headed 'sḱed- \\\"bedecken\\\"?'; Walde–Pokorny II 558 'sked- \\\"bedecken\\\"? … Unsicher')\",\n \"note\": \"Pokorny p. 919 does have exactly this root with exactly this gloss, immediately after (s)k(h)ed- 'to split' (p. 918) — which is Nourai's 'Sked 1', so even his numbering follows Pokorny's own pair of homonyms. What the chart does not show is that both Pokorny and Walde–Pokorny mark the root with a question mark and WP adds 'Unsicher': it rests on only three witnesses — Skt. chad-/chattra-, Av. sāδayantī-, and OHG hāz 'garment' — with Pashto psōlә́l 'to put on' (*pati-upa-sad-) as a fourth. The chart's tree is otherwise a faithful reduction of Pokorny's entry (the Indic and the Avestan branch), so the root is confirmed as a root of this dictionary tradition, with the caveat that it is one of the weaker reconstructions in Pokorny.\",\n \"note_fa\": \"پوکورنی در ص ۹۱۹ فرهنگ خود همین ریشه را با همین معنا («پوشاندن») آورده است، درست پس از ریشهٔ (s)k(h)ed- «شکافتن» در ص ۹۱۸ که همان «Sked 1» نورایی است؛ پس حتی شماره‌گذاری نورایی نیز از جفتِ هم‌نگارهٔ خودِ پوکورنی پیروی می‌کند. آنچه در چارت نیامده این است که هم پوکورنی و هم والده-پوکورنی این ریشه را با علامت پرسش آورده‌اند و WP می‌افزاید «نامطمئن» (Unsicher): تمام شواهد آن سه واژه است — chad-/chattra- سنسکریت، sāδayantī- اوستایی و hāz در آلمانی علیای کهن — به‌علاوهٔ psōlә́l پشتو (*pati-upa-sad-). درخت چارت جز این، تلخیصی وفادار از مدخل پوکورنی است. پس ریشه در چارچوب همین سنت فرهنگ‌نویسی تأیید می‌شود، با این یادآوری که از بازسازی‌های سست‌تر پوکورنی است.\",\n \"sources\": [W+\"%DA%86%D8%AA%D8%B1\", W+\"%DA%86%D8%A7%D8%AF%D8%B1\"],\n \"ref_check\": [{\"ref\": \"POK:919\", \"status\": \"supports\", \"note\": \"Pokorny IEW p. 919 (local POK_03.txt, leaf 156; also POK_full.txt 'Root / lemma: sḱed-, Meaning: to cover … Page(s): 919'): 'sked- \\\"bedecken\\\"? Ai. chadati (unbelegt), chādáyati \\\"bedeckt, verbirgt\\\", chattra-m \\\"Schirm\\\", chadis- n. \\\"Decke, Dach\\\"; av. sāδayantī- \\\"ein Kleidungsstück\\\" (skyth. Hose?), afghan. psōlә́l \\\"to put on, wear\\\" (*pati-upa-sad-); ahd. hāz … WP. II 558.' Page number and gloss are exact.\"}],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. II p. 558 (incoming/WLD/WLD_Bd2_pages.txt leaf 563)\", \"stance\": \"partial\", \"note\": \"'sked- \\\"bedecken\\\"? Ai. chādati (unbelegt), chādáyati …, chāttra-m \\\"Schirm\\\", chadis- n. \\\"Decke, Dach\\\"; mhd. haz \\\"Kleid, Rock, Kleidung\\\", ags. hæteru … Unsicher.' Same root, but WP does not yet cite the Avestan form and calls the whole thing uncertain.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985, root list\", \"stance\": \"silent\", \"note\": \"Watkins' appendix has sked- 'to split, scatter' (the other root) but no 'to cover' root — the Indic word has no English derivative, so it is outside his scope.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann\", \"stance\": \"silent\", \"note\": \"No sked-/sḱed- 'cover' headword found in Mann's dictionary.\"}],\n \"nodes\": []\n}\n\nm = e4[\"nodes\"]\n\nm.append({\n \"id\": 1, \"lang\": \"Sanskrit\", \"words\": \"čadaiti; čattra\",\n \"verdict\": \"transcription_suspect\",\n \"derivation\": \"The second word is right: Sanskrit chattra- (Nourai's č = Skt. ch) 'parasol, umbrella, royal canopy' = chad- 'to cover' + the instrument suffix -tra, Pokorny's 'chattra-m \\\"Schirm\\\"'. The first word is not a Sanskrit form: Sanskrit has chadati (unattested, reconstructed by Pokorny: 'chadati (unbelegt)') and the causative chādáyati 'covers, conceals'. A 3sg. in -aiti is an Avestan/Old Iranian ending, not an Indic one (Indic would be -ati); the printed page really does read 'čadaiti', so this is the book's own error — either Nourai Iranianized Pokorny's chadati, or he conflated it with the Avestan branch in the same entry. Checked on the page image (pdftoppm -r 200 of pdf p. 452, copied to data/verification/sources/refs/ocr/BOOK/452.png): the extraction is faithful, the misprint is Nourai's.\",\n \"derivation_fa\": \"واژهٔ دوم درست است: chattra- سنسکریت (č در نویسه‌گردانی نورایی همان ch سنسکریت است) به معنای «چتر، سایبان شاهی» از chad- «پوشاندن» + پسوند ابزارسازِ -tra؛ پوکورنی نیز «chattra-m \\\"Schirm\\\"» آورده است. اما واژهٔ نخست صورتی سنسکریت نیست: در سنسکریت chadati (که پوکورنی خود آن را «بی‌شاهد/بازسازی‌شده» می‌نامد) و صورت سببیِ chādáyati «می‌پوشاند، پنهان می‌کند» داریم. پایانهٔ -aiti برای سوم‌شخص مفرد، پایانه‌ای اوستایی/ایرانی باستان است نه هندی (در هندی -ati می‌آید). تصویر صفحهٔ چاپی را دیدم و در کتاب نیز «čadaiti» چاپ شده است؛ پس خطا از خودِ کتاب است نه از استخراج داده — گویا نورایی صورت سنسکریت را به قیاسِ شاخهٔ اوستاییِ همان مدخل، ایرانی‌مآب نوشته است. خطای چاپی کتاب.\",\n \"error_in\": \"book\",\n \"book_prints\": \"čadaiti\",\n \"correct_form\": \"čadati (Skt. chadati, caus. chādáyati)\",\n \"sources\": [W+\"%DA%86%D8%AA%D8%B1\"],\n \"ref_check\": [{\"ref\": \"POK:919\", \"status\": \"partial\", \"note\": \"Pokorny p. 919 prints 'Ai. chadati (unbelegt), chādáyati \\\"bedeckt, verbirgt\\\", chattra-m \\\"Schirm\\\"' — it supports čattra exactly and supports the verb only in the shape chadati/chādayati, never *chadaiti.\"}],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. II p. 558\", \"stance\": \"partial\", \"note\": \"'Ai. chādati (unbelegt), chādáyati …, chāttra-m \\\"Schirm\\\"' — same two words, same shapes; no -aiti form anywhere.\"},\n   {\"src\": \"BQT\", \"where\": \"Mo'in's footnote to چتر, printed p. 622/623 (BQT_v2_pages.txt leaf 80)\", \"stance\": \"supports\", \"note\": \"'سانسکریت chattra- از ریشهٔ chad (پوشاندن) + tra (پسوند بمعنی وسیله، کننده)؛ وسیلهٔ پوشاندن، حفاظت، چتر آفتابی، آفتاب‌گیر … «ویلیامز ۱:۴۹۴»' — Mo'in's own analysis of chattra, citing Monier-Williams.\"},\n   {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/چتر\", \"stance\": \"supports\", \"note\": \"Persian چتر 'Borrowed from Sanskrit छत्त्र (chattra)' — confirms the Sanskrit word and its shape.\"}]})\n\nm.append({\n \"id\": 2, \"lang\": \"Persian\", \"words\": \"čâdor «چادر»; čatr «چتر»\",\n \"verdict\": \"plausible\",\n \"derivation\": \"چتر čatr 'umbrella, parasol; royal canopy' is a straightforward loan from Sanskrit chattra-, brought in with the Indian royal parasol: in Ghaznavid and later Persian the چتر is the emblem of kingship, and Mo'in's footnote in the Borhan (p. 622) derives it just so, 'سانسکریت chattra- از ریشهٔ chad (پوشاندن) + tra', citing Monier-Williams. چادر čādor 'tent; veil, chador' is the harder case: it goes back to Middle Persian čādur/čātar 'sheet, veil, canopy', and the standard handbooks (Mo'in's footnote at BQT p. 609, Wiktionary) treat it as the same Indic word, but the phonetics are not regular — Skt. -ttr- should not give Persian -d- — so the borrowing must have passed through a Middle Indic form (Prakrit chatta-) or, as some hold, چادر is an inherited Iranian word only secondarily associated with چتر. Persian چادر then travelled on: Ottoman Turkish çadır, Russian чадра/шатёр, Hungarian sátor, Arabic شوذر (Mo'in: 'معرب آن شوذر'), English chador. Verdict: چتر confirmed, چادر plausible (missing Middle Persian step and an irregular correspondence), so the node takes the weaker verdict.\",\n \"derivation_fa\": \"«چتر» وام‌واژه‌ای است بی‌گمان از chattra- سنسکریت که همراه با چترِ شاهیِ هندی به ایران آمد؛ در دورهٔ غزنوی و پس از آن، چتر نشانهٔ پادشاهی است و معین در حاشیهٔ برهان قاطع (ص ۶۲۲) همین را می‌نویسد: «سانسکریت chattra- از ریشهٔ chad (پوشاندن) + tra»، به استناد فرهنگ مونیه-ویلیامز. اما «چادر» دشوارتر است: این واژه به فارسی میانهٔ čādur/čātar «پارچه، روپوش، سایبان» بازمی‌گردد و منابع معیار (حاشیهٔ معین در ص ۶۰۹ برهان، و ویکی‌واژه) آن را همان واژهٔ هندی می‌دانند؛ ولی تحول آوایی منظم نیست، زیرا -ttr- سنسکریت نباید در فارسی به -د- بدل شود. پس یا وام‌گیری از صورتی میانهٔ هندی (پراکریتِ chatta-) صورت گرفته یا — چنان‌که برخی گفته‌اند — «چادر» واژه‌ای ایرانی و موروثی است که تنها بعدها با «چتر» هم‌سنگ انگاشته شده. سپس خودِ «چادر» به زبان‌های دیگر رفته است: çadır ترکی عثمانی، чадра و шатёр روسی، sátor مجاری، معرّبِ آن «شوذر» (به گفتهٔ معین) و chador انگلیسی. داوری: «چتر» درست، «چادر» با احتیاط پذیرفتنی؛ پس داوری گره همان ضعیف‌تر است.\",\n \"sources\": [W+\"%DA%86%D8%A7%D8%AF%D8%B1\", W+\"%DA%86%D8%AA%D8%B1\"],\n \"ref_check\": [\n   {\"ref\": \"BQT:609\", \"status\": \"supports\", \"note\": \"Borhan-e Qate', Mo'in ed., the چادر page (BQT_v2_pages.txt leaf 66, footnote running onto leaf 67): dialect forms (فریزندی، نطنزی، سمنانی، سرخه‌ای، لاسگردی، شهمیرزادی، گیلکی čādor) followed by 'سانسکریت chattra (چتر شاهی، درفش شاهی)، chattra (چتر) از chad (پوشاندن) «ویلیامز ۱:۴۰۴» … رک: شادروان. معرب آن شوذر … خیمه، سایبان، بالاپوش زنان، ردا' — exactly Nourai's Sanskrit → Persian arrow for چادر.\"},\n   {\"ref\": \"BQT:622\", \"status\": \"supports\", \"note\": \"Same volume, the چتر page (leaf 80; the page opens 'بیان چهارم در جیم فارسی با تای قرشت' and defines چتر as 'سایبانی که برای محافظت از آفتاب نگاه دارند'), footnote 5: 'سانسکریت chattra- از ریشهٔ chad (پوشاندن) + tra (پسوند بمعنی وسیله، کننده)؛ … «ویلیامز ۱:۴۹۴»'. Note the OCR leaf/printed offset here is +543, so Nourai's two page numbers land on exactly these two entries.\"}],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"2-vol. Adena abridgement, MON_part1.txt s.vv. چادر, چتر\", \"stance\": \"supports\", \"note\": \"'چادر: ۲ [< شادر ← چتر] … پوششی که زنان روی سر اندازند …؛ خیمه' — Mo'in links چادر to چتر in the headword itself; 'چتر: (.) سایبان کوچک دسته‌دار …'.\"},\n   {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/چادر and /چتر\", \"stance\": \"partial\", \"note\": \"چادر 'from Middle Persian čādur (sheet, veil)', traced back to Sanskrit chattra, 'attested in Turkic from the 11th century'; چتر 'Borrowed from Sanskrit छत्त्र (chattra)', 'Doublet of چادر'. Supports the Indic source but inserts the Middle Persian stage the chart omits.\"},\n   {\"src\": \"HRN\", \"where\": \"grep čādar/čatr in HRN.txt\", \"stance\": \"silent\", \"note\": \"No entry found in Horn's Grundriss for either word under these spellings.\"},\n   {\"src\": \"ARY\", \"where\": \"grep چادر/چتر in incoming/ARY/ARY_pages.txt\", \"stance\": \"silent\", \"note\": \"Aryanpur's Indo-European roots of Persian has no entry for either word (only OCR noise matches).\"}]})\n\nm.append({\n \"id\": 3, \"lang\": \"Avestan\", \"words\": \"sâdayantî\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Young Avestan sāδayantī- f., the name of an article of clothing, is a hapax of the Nērangestān (§95): Bartholomae's Altiranisches Wörterbuch prints 'j. sāδayantī- f. Name eines Kleidungsstücks: yā° vaŋhaiti naēsca -tīsca N.95. Unsicher. — Pü.: dādanakadk'. Formally it is the feminine present participle of a causative *sāδaya- 'to cover, to clothe' from the same root as Skt. chādáyati, with Iranian s- against Indic ch- (the regular outcome of IE *sḱ-) and intervocalic *d > δ. Pokorny's own p. 919 adds the guess '(skyth. Hose?)' — 'a Scythian trouser?' — which is where Nourai's neutral 'an article of clothing' comes from. The chart writes d for δ, a normal simplification, not an error.\",\n \"derivation_fa\": \"صورت اوستایی نو sāδayantī- (مؤنث) نام یک جامه است و تنها یک بار در نیرنگستان (بند ۹۵) آمده؛ بارتولمه در فرهنگ ایرانی باستان می‌نویسد: «sāδayantī- مؤنث، نام یک قطعه لباس: … N.95. نامطمئن. — در پهلوی: dādanakadk». از نظر ساخت، اسم فاعلِ مؤنثِ ستاک سببیِ *sāδaya- «پوشاندن» است از همان ریشه‌ای که chādáyati سنسکریت از آن آمده؛ s- ایرانی در برابر ch- هندی بازتاب منظم *sḱ- هندواروپایی است و *d میان دو واکه به δ بدل شده است. پوکورنی در همان ص ۹۱۹ حدس «شلوار سکایی؟» را افزوده و همین سبب شده نورایی معنای خنثای «یک قطعه لباس» را بیاورد. نوشتن d به‌جای δ در چارت ساده‌سازی نویسه‌گردانی است نه خطا. ادعای نورایی درست است.\",\n \"sources\": [],\n \"ref_check\": [{\"ref\": \"POK:919\", \"status\": \"supports\", \"note\": \"Pokorny p. 919 s.v. sḱed-: 'av. sāδayantī- \\\"ein Kleidungsstück\\\" (skyth. Hose?)' — the form, the language and the gloss of Nourai's box, on the cited page.\"}],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"Bartholomae, AiW s.v. sāδayantī- (BRT.txt line 26176)\", \"stance\": \"supports\", \"note\": \"'j. sāδayantī- f. Name eines Kleidungsstücks: yā° vaŋhaiti naēsca -tīsca N.95. Unsicher. — Pü.: dādanakadk' — the word is genuine Young Avestan (Nērangestān 95), though Bartholomae marks its interpretation 'uncertain'.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. II p. 558\", \"stance\": \"silent\", \"note\": \"The 1927 Walde–Pokorny entry for sked- 'bedecken' cites only the Indic and Germanic words; the Avestan form was added later, in Pokorny 1959.\"},\n   {\"src\": \"KNT\", \"where\": \"Kent, Old Persian\", \"stance\": \"silent\", \"note\": \"Not an Old Persian word; Kent's lexicon has nothing.\"}]})\n\nm.append({\n \"id\": 4, \"lang\": \"None\", \"words\": \"\",\n \"verdict\": \"unverified\",\n \"derivation\": \"An empty box: on the printed page (pdf p. 452, image copied to data/verification/sources/refs/ocr/BOOK/452.png) an arrow runs from the Avestan sāδayantī- box to a box that carries no language label and no word at all — the frame is drawn but nothing is set inside it. The extraction is therefore faithful, and there is nothing to verify. Most likely Nourai meant to fill it with the next reflex of Pokorny's entry after the Avestan form, i.e. Pashto psōlә́l 'to put on, wear' (*pati-upa-sad-), or with a New Persian descendant, and the box was left blank at typesetting.\",\n \"derivation_fa\": \"جعبه‌ای تهی است: در صفحهٔ چاپی (ص ۴۵۲ پی‌دی‌اف؛ تصویر آن در data/verification/sources/refs/ocr/BOOK/452.png نگهداری شده) پیکانی از جعبهٔ اوستاییِ sāδayantī- به جعبه‌ای می‌رود که نه نام زبان دارد و نه واژه‌ای در آن چاپ شده؛ تنها کادر آن رسم شده است. پس خوانشِ داده‌ها درست بوده و چیزی برای راستی‌آزمایی نیست. به‌احتمال زیاد قرار بوده صورت بعدیِ همان مدخل پوکورنی پس از واژهٔ اوستایی در آن بنشیند، یعنی psōlә́l پشتو «پوشیدن» (از *pati-upa-sad-) یا بازماندهٔ فارسی نو، ولی جعبه در حروف‌چینی خالی مانده است.\",\n \"sources\": [],\n \"ref_check\": [{\"ref\": \"(none cited)\", \"status\": \"not_checked\", \"note\": \"The box is empty in the book and carries no reference.\"}],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"IEW p. 919\", \"stance\": \"silent\", \"note\": \"The only further reflex Pokorny gives after the Avestan word is 'afghan. psōlә́l \\\"to put on, wear\\\" (*pati-upa-sad-)' plus OHG hāz; nothing identifies what the blank box was meant to hold.\"}]})\n\nout = {\n \"pdf_page\": 452,\n \"book_page\": 422,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-13\",\n \"entries\": [e0, e4]\n}\n\nwith io.open(\"/home/sfmqrb/git/rishe/data/verification/page-452.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(out, f, ensure_ascii=False, indent=1)\nprint(\"ok\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-452.py"
}
```


### [2026-09-14T02:15:48.171Z] TOOL RESULT

```
ok
```


## [2026-09-14T02:15:50.405Z] TOOL CALL #85: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -m json.tool data/verification/page-452.json > /dev/null && echo \"JSON OK\"; python3 tools/verify_check.py 452"
}
```


### [2026-09-14T02:15:51.628Z] TOOL RESULT

```
JSON OK
nodes verified: 15/15
node verdicts: {'confirmed': 9, 'plausible': 4, 'transcription_suspect': 1, 'unverified': 1}
root verdicts: {'confirmed': 2}
ref checks: {'not_checked': 4, 'supports': 11, 'partial': 1}
books consulted: {'supports': 27, 'silent': 15, 'partial': 6, 'contradicts': 1} | by book: {'KLN': 8, 'Wiktionary': 8, 'WLD': 4, 'AHD': 4, 'MON': 3, 'BQT': 2, 'HRN': 2, 'ETYM': 2, 'SKT': 2, 'IEC': 2, 'POK': 2, 'WEB': 1, 'LKT': 1, 'AFM': 1, 'FVQ': 1, 'DOZ': 1, 'PLA': 1, 'HUB': 1, 'ARY': 1, 'BRT': 1, 'KNT': 1}
```


## [2026-09-14T02:16:09.550Z] AGENT

Verification of PDF page 452 (book p. 422) complete — `/home/sfmqrb/git/rishe/data/verification/page-452.json`, `verify_check.py 452` reports 15/15 nodes, 0 PROBLEM lines.

**Counts:** roots 2 confirmed (Skand; Sked 2). Nodes: 9 confirmed, 4 plausible, 1 transcription_suspect, 1 unverified. Ref checks: 11 supports, 1 partial, 4 not_checked (boxes with no reference).

**Flagged items**
- `transcription_suspect` — Sked 2 #1 Sanskrit **čadaiti**: the printed page really shows "čadaiti", but Sanskrit is *chadati* / caus. *chādáyati* (Pokorny 919); the `-aiti` ending is Avestan, not Indic. `error_in: book` (Nourai Iranianized the form); extraction is faithful. Page image saved to `data/verification/sources/refs/ocr/BOOK/452.png`.
- `plausible` — Skand #4 Arabic *eskeleh*: TAD:4 confirms an Italian loan but names **scala**, not the chart's parent *scalo*.
- `plausible` — Skand #5 Persian **اسکله**: Mo'in (and Dehkhoda) back Nourai's Italian→Arabic→Persian route ("معر. … در اصل ایتالیایی"), but Wiktionary routes it via Ottoman Turkish *iskele*; middleman undecidable.
- `plausible` — Skand #10 Greek *skandalon*: WP II 540, Klein and Watkins support *skand-alo-, but Beekes rejects the IE derivation (Pre-Greek); Mann files it under a separate "fall" root.
- `plausible` — Sked 2 #2 Persian: چتر ← Skt. *chattra* is solid (Mo'in's Borhan footnote p. 622 quotes Monier-Williams), but چادر needs the Middle Persian *čādur* step and shows an irregular -ttr- > -d-.
- `unverified` — Sked 2 #4: the book prints a **completely empty box** hanging off the Avestan node (verified on the page image); extraction faithful, nothing to verify.

**No extraction errors found** — the JSON matches the printed page throughout (including the empty box and "čadaiti").

Notes for the owner: Pokorny 1959 has **no** headword for the Skand root (it is absent at pp. 918–919 and 929–930), so Nourai correctly cites WLD:540 ("sqand-", whence his "Sqand" spelling) and AHD:1539; the variant "Kand 2" is unsupported. BQT vol-2 leaf→printed offset here is **+543** (leaf 66 = p. 609 چادر, leaf 80 = p. 622 چتر), three more than the +540 recorded in `refs_online.json` for the later part of the volume. 16 web pages archived via `fetch_source.py`.
