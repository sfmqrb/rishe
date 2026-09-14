# Verification process log — verify-page-459


## [2026-09-14T02:27:28.889Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 459 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-459.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-459.json. Write /home/sfmqrb/git/rishe/data/verification/page-459.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 459` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T02:27:29.865Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T02:27:31.006Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T02:27:31.104Z] TOOL RESULT

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


## [2026-09-14T02:27:31.267Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-459.txt"
}
```


### [2026-09-14T02:27:31.298Z] TOOL RESULT

```
1	=== PDF page 459 (book page 429) ===
2	--- entry 0 ---
3	ROOT [Semitic] S.l.m, Š.l.m : to be healthy and intact  (refs KLN:1430; AHD:1541)
4	#1 (parent #0) [Arabic] refs=KLN:1430; SAP:726; AHD:1541 | salâm : good health, peace (greetings) ; taslîm : surrendering (for peace) ; Islâm : surrendering (to will of God)
5	  #2 (parent #1) [Persian] refs=MON; FVA:196 | salâm «سلام» : peace (greetings) | extra: تسلیم ، اسلام ، سلمیٰ ، سالم ، سلامت سلیمان ، سلیم ، مسلم ، مُسَلَّم
6	  #3 (parent #1) [English] refs=AHD | Islam, Moslem
7	#4 (parent #0) [Malaysian] refs=OEW:451 | salang : peace, greetings, fare well
8	  #5 (parent #4) [English] refs=OEW:451; FSD:2316 | so long : fare well | NOTE: Started as a colloquial among British soldiers.
9	#6 (parent #0) [Hebrew] refs=KLN:828,1430,1471; AHD:1541 | šalôm : peace, good health (greetings) ; yrrŭ-šâlôm : city of peace (Jerusalem) ☞Yârâh ; Ab-šalôm : father is peace (Absalom) ☞Ab 2
10	  #7 (parent #6) [French] refs=None | 
11	    #8 (parent #7) [Persian] refs=MON5:195 | Űršalîm «اورشلیم» : "city of peace"
12	  #9 (parent #6) [English] refs=KLN:828 | šalom, Jerusalem, Absalom, Solomon
13	#10 (parent #0) [Greek] refs=AHD:1541 | salômě : peace ; Salome : a female name
14	  #11 (parent #10) [English] refs=AHD:1145 | Salome : an old female name
15	--- entry 1 ---
16	ROOT Š.l.m -> redirect to S.l.m
17	--- entry 2 ---
18	ROOT Sm -> redirect to Sem 1
19	
```


## [2026-09-14T02:27:32.618Z] AGENT

I'll read the source JSON and reference infrastructure.


## [2026-09-14T02:27:34.149Z] TOOL CALL #3: Bash

```json
{
 "command": "python3 -m json.tool data/extracted/batch/page-459.json | head -200",
 "description": "Read source JSON for page 459"
}
```


### [2026-09-14T02:27:35.951Z] TOOL RESULT

```
{
    "pdf_page": 459,
    "book_page": 429,
    "entries": [
        {
            "root": {
                "name": "S.l.m, \u0160.l.m",
                "lang": "Semitic",
                "refs": "KLN:1430; AHD:1541",
                "gloss": "to be healthy and intact"
            },
            "nodes": [
                {
                    "id": 1,
                    "parent": 0,
                    "lang": "Arabic",
                    "refs": "KLN:1430; SAP:726; AHD:1541",
                    "words": [
                        {
                            "translit": "sal\u00e2m",
                            "gloss": "good health, peace (greetings)",
                            "script": null
                        },
                        {
                            "translit": "tasl\u00eem",
                            "gloss": "surrendering (for peace)",
                            "script": null
                        },
                        {
                            "translit": "Isl\u00e2m",
                            "gloss": "surrendering (to will of God)",
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
                    "refs": "MON; FVA:196",
                    "words": [
                        {
                            "translit": "sal\u00e2m",
                            "gloss": "peace (greetings)",
                            "script": "\u0633\u0644\u0627\u0645"
                        }
                    ],
                    "script_extra": "\u062a\u0633\u0644\u06cc\u0645 \u060c \u0627\u0633\u0644\u0627\u0645 \u060c \u0633\u0644\u0645\u06cc\u0670 \u060c \u0633\u0627\u0644\u0645 \u060c \u0633\u0644\u0627\u0645\u062a \u0633\u0644\u06cc\u0645\u0627\u0646 \u060c \u0633\u0644\u06cc\u0645 \u060c \u0645\u0633\u0644\u0645 \u060c \u0645\u064f\u0633\u064e\u0644\u064e\u0651\u0645",
                    "note": null,
                    "quote": {
                        "text": "\u0642\u0627\u0635\u062f \u0645\u0646\u0632\u0644 \u0633\u0644\u0645\u06cc\u0670 \u06a9\u0647 \u0633\u0644\u0627\u0645\u062a \u0628\u0627\u062f\u0634 - \u0686\u0647 \u0634\u0648\u062f \u06af\u0631 \u0628\u0633\u0644\u0627\u0645\u06cc \u062f\u0644 \u0645\u0627 \u0634\u0627\u062f \u06a9\u0646\u062f",
                        "poet": "H\u00e2fez"
                    }
                },
                {
                    "id": 3,
                    "parent": 1,
                    "lang": "English",
                    "refs": "AHD",
                    "words": [
                        {
                            "translit": "Islam, Moslem",
                            "gloss": null,
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 4,
                    "parent": 0,
                    "lang": "Malaysian",
                    "refs": "OEW:451",
                    "words": [
                        {
                            "translit": "salang",
                            "gloss": "peace, greetings, fare well",
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
                    "refs": "OEW:451; FSD:2316",
                    "words": [
                        {
                            "translit": "so long",
                            "gloss": "fare well",
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": "Started as a colloquial among British soldiers.",
                    "quote": null
                },
                {
                    "id": 6,
                    "parent": 0,
                    "lang": "Hebrew",
                    "refs": "KLN:828,1430,1471; AHD:1541",
                    "words": [
                        {
                            "translit": "\u0161al\u00f4m",
                            "gloss": "peace, good health (greetings)",
                            "script": null
                        },
                        {
                            "translit": "yrr\u016d-\u0161\u00e2l\u00f4m",
                            "gloss": "city of peace (Jerusalem)",
                            "script": null,
                            "see": [
                                "Y\u00e2r\u00e2h"
                            ]
                        },
                        {
                            "translit": "Ab-\u0161al\u00f4m",
                            "gloss": "father is peace (Absalom)",
                            "script": null,
                            "see": [
                                "Ab 2"
                            ]
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 7,
                    "parent": 6,
                    "lang": "French",
                    "refs": null,
                    "words": [],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 8,
                    "parent": 7,
                    "lang": "Persian",
                    "refs": "MON5:195",
                    "words": [
                        {
                            "translit": "\u0170r\u0161al\u00eem",
                            "gloss": "\"city of peace\"",
                            "script": "\u0627\u0648\u0631\u0634\u0644\u06cc\u0645"
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 9,
                    "parent": 6,
                    "lang": "English",
                    "refs": "KLN:828",
                    "words": [
                        {
                            "translit": "\u0161alom, Jerusalem, Absalom, Solomon",
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
                    "parent": 0,
                    "lang": "Greek",
                    "refs": "AHD:1541",
                    "words": [
                        {
                            "translit": "sal\u00f4m\u011b",
                            "gloss": "peace",
                            "script": null
                        },
                        {
                            "translit": "Salome",
                            "gloss": "a female name",
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
```


## [2026-09-14T02:27:36.094Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['KLN','AHD','SAP','MON','FVA','OEW','FSD','WEB','SKT','PLA','AFM','FVQ','AFA','LKT','MON5','BQT','ARY']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:400])\n\""
}
```


### [2026-09-14T02:27:37.294Z] TOOL RESULT

```
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
SAP {"title": "Ahmad Sayyah, Farhang-e Sayyah / Farhang-e Bozorg-e Jame'-e Novin (Persian translation of al-Munjid), 3 vols, Eslam 1368/1989", "kind": "purchase", "url": "https://fidibo.com/book/142427 (vol.1, 1152 pp) ; https://fidibo.com/book/142430 (vol.2, 1206 pp) — PDF ebook, ~300,000 toman each, free sample", "lookup_hint": "Not found (archive.org has Bandar-Rigi's منجد الطلاب translation, abo_a
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
FVA {"title": "S.M. Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (dakhil), Tohi/Azadi 1368/1989", "kind": "catalog", "url": "https://openlibrary.org/works/OL4602367W (edition OL2012991M: Intisharat-i Islami 1368/1989, 582 pp)", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: no digital copy found.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 202
OEW {"title": "J. T. Shipley, The Origins of English Words: A Discursive Dictionary of Indo-European Roots, Baltimore 1984", "edition_found": "1984 (lending-only)", "kind": "archive_restricted", "url": "https://archive.org/details/originsofenglish0000ship ; https://archive.org/details/originsofenglish00jose (both JHU 1984, borrowable) ; HathiTrust mdp.49015002910322 search-only ; Google ELSm5zUgP_wC n
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/
AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_page
FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.t
AFA {"title": "S. Fraenkel, Die aramäischen Fremdwörter im Arabischen, Leiden 1886 (repr. Hildesheim 1962, same pagination)", "edition_found": "1886", "kind": "archive_djvu", "url": "https://archive.org/details/diearamischenfr00fraegoog", "identifier": "diearamischenfr00fraegoog (also bub_gb_SzdbAAAAQAAJ)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AFA.txt", "page_offset": "
LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 =
MON5 null
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root,
```


## [2026-09-14T02:27:40.458Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -m json.tool data/extracted/batch/page-459.json | tail -60; echo ===; ls data/verification/sources/refs/ | head -80"
}
```


### [2026-09-14T02:27:41.618Z] TOOL RESULT

```
Exit code 1
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 10,
                    "parent": 0,
                    "lang": "Greek",
                    "refs": "AHD:1541",
                    "words": [
                        {
                            "translit": "sal\u00f4m\u011b",
                            "gloss": "peace",
                            "script": null
                        },
                        {
                            "translit": "Salome",
                            "gloss": "a female name",
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
                    "refs": "AHD:1145",
                    "words": [
                        {
                            "translit": "Salome",
                            "gloss": "an old female name",
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
                "name": "\u0160.l.m",
                "redirect": "S.l.m"
            },
            "nodes": []
        },
        {
            "root": {
                "name": "Sm",
                "redirect": "Sem 1"
            },
            "nodes": []
        }
    ]
}
(eval):1: == not found
```


## [2026-09-14T02:27:42.365Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['KLN','AHD','OEW','FSD','FVQ','AFM','PLA','LKT','AFA','SAP','MON','FVA']:\n    v=d.get(k)\n    if v: print(k,'|local:',v.get('local_file'),'|offset:',v.get('page_offset'),'|hint:',str(v.get('lookup_hint'))[:200])\n\""
}
```


### [2026-09-14T02:27:43.492Z] TOOL RESULT

```
KLN |local: /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt |offset: KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |hint: Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume p
AHD |local: /home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt |offset: 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page. |hint: Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the 
OEW |local: None |offset: None |hint: Borrow via IA lending (djvu.txt returns 401/403). Entries are IE roots in alphabetical order; use IA's in-book search: https://archive.org/details/originsofenglish00jose?q=<root>
FSD |local: /home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt |offset: vol1: leaf = p + 41..56 (drifts; e.g. leaf 87 = p.46, leaf 612 = p.556); vol3: leaf = p - 1466 (e.g. leaf 215 = p.1681); vol4: leaf = p - 2144..2148 (e.g. leaf 229 = p.2373); vol2 offset not reliably detected (pages ~ 700-1640) - grep the headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |hint: Headword in bold at line start with pronunciation; etymology in brackets at entry end '[< L. ...]'. Very large OCR (16 MB per vol); grep -n '^word' vol file.
FVQ |local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ.txt'] |offset: printed page = leaf − 17 (0-based \f blocks in FVQ_pages.txt; 335 leaves) |hint: Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).
AFM |local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM.txt'] |offset: 198 leaves; page numerals OCR'd unreliably — offset approx leaf − 8 (front matter); confirm on page image |hint: Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أ
PLA |local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt'] |offset: 301 leaves (pdftotext -layout, \f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276). |hint: HathiTrust search-only; Google Books id q_ErAAAAMAAJ snippet view; DDB has only the table of contents. No full text online. | For pages in a scanned volume use: python3 tools/ref_page.py PLA:<page> --
LKT |local: /home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt |offset: leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |hint: Numbered entries: 'NNNN. word (language) meaning' - Lokotsch is usually cited by entry number, but Nourai cites pages. grep the oriental source word in transliteration or the number.
AFA |local: /home/sfmqrb/git/rishe/data/verification/sources/refs/AFA.txt |offset: leaf = printed + 30 (e.g. leaf 38 = p.8). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |hint: Arabic/Aramaic in script (not OCRed) with German glosses; grep the German meaning or transliteration.
SAP |local: None |offset: None |hint: Not found (archive.org has Bandar-Rigi's منجد الطلاب translation, abo_abdrahman_kordi_barid_20150501_1718, and the Arabic al-Munjid on noorlib.ir/book/info/32878 — usable to check the Arabic-side cont
MON |local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt'] |offset: None |hint: Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Aves
FVA |local: None |offset: None |hint: Searched archive.org, ketabnak, noorlib, web: no digital copy found.
```


## [2026-09-14T02:28:22.022Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i '^salaam\\|^salam\\|^shalom\\|^islam\\|^moslem\\|^muslim\\|^jerusalem\\|^absalom\\|^solomon\\|^so long\\|^so-long\\|^salome' KLN_1966.txt | head -40"
}
```


### [2026-09-14T02:28:22.099Z] TOOL RESULT

```
1236:Absalom,  masc.  PN. ;  in  the  Bible,  King  David  s son;  fig.  a  favorite  son.  —  Heb.  Abhshaldm,  lit. ‘father  is  peace’,  fr.  abh,  ‘father’,  and  shaldm, ‘peace’.  See  Aboth  and  shalom. abscess,  n„  a  swelling  in  body  tissues  (med.).  — L.  abscessus,  ‘a  going  away,  departure,  abscess  , fr.  abcedere,  ‘to  go  away’,  fr.  abs-,  ab-,  ‘away from,  from’,  and  cedere,  ‘to  go’.  See  ab-  and cede  and  cp.  cease.
19966:Islam,  n.  —  Arab,  islim,  ‘submitting  oneself  to God,  surrender,  obedience’,  infin.  of  aslama, ‘he  surrendered,  submitted*,  TV  (=  causative) conjugation  of  salima,  ‘he  was  safe’.  See  salaam and  cp.  selamlik,  Moslem,  Mussulman.  Cp.  also shalom.  Derivatives:  Islam-ic,  adj.,  Islam-ism, n.,  Islam-ite,  n.
20245:Jerusalem,  n.  —  Gk.  'IspouaaXfip.,  fr.  Heb.  Y*rQ- shaldyim,  lit.  ‘foundation  of  peace’,  fr.  base  of yardh,  ‘he  threw,  cast’,  and  shaldm,  ‘peace’.
20247:Jerusalem  artichoke.  —  Folk  etymological  alter¬ ation  of  It.  girasole,  ‘sun  flower’.  See  girasol. Jeshurun,  n.,  poetic  name  of  Israel.  —  Heb. Ylshurdn,  prop,  ‘the  righteous  people’,  deno¬ minated  fr.  yashdr  =  yashdr,  ‘straight,  right, upright’,  which  derives  fr.  yashdr,  ‘was  smooth, straight,  right’,  whence  also  ydsher,  ‘straight¬ ness,  uprightness’,  meshdr,  ‘evenness,  upright¬ ness,  equity’,  mishSr,  ‘uprightness,  level  place, plains’;  rel.  to  Aram,  meshrd,  ‘level  place’, Arab,  yasara,  ‘was  gentle,  tractable,  easy’, ydsar,  ‘tractable,  easy’,  Akkad,  esheru,  ‘to  be straight  or  right,’  mesharu,  ‘justice’;  cp.  Sharon. The  defective  writing  of  the  first  u  in  Y*shurun (with  qubbutz  inst.  of  with  shureq)  does  not affect  its  quantity,  and  is  due  to  the  tendency to  avoid  the  scriptio  plena  in  two  successive syllables.
24476:Moslem,  n.,  a  Mohammedan.  —  Arab,  muslim,
24748:Muslim,  n.  —  See  Moslem, muslin,  n.,  a  fine  soft  cotton  fabric.  F.  mous¬ seline,  fr.  It.  mussotina,  dimin.  formed  from Mussolo,  Italian  name  of  Mosul,  town  in  Meso¬ potamia  (now  Iraq),  where  this  material  was originally  made.  Cp.  mousseline. muslinet,  n.  —  Dimin.  of  prec.  word.  For  the ending  see  suff.  -et.
33518:salaam,  salam,  n.,  —  Arab,  salam,  ‘peace;  salut¬ ing,  salutation’,  from  the  base  of  salima,  ‘he was  safe’,  whence  also  silm,  salam,  ‘safety,  secu¬ rity,  peace’,  salima,  ‘he  was  safe’ ;  rel.  to  Ethiop. salam,  ‘peace,  welfare’,  Heb.  shdlam,  ‘he  was  in¬ tact,  was  at  peace,  was  in  good  health’,  shalom, ‘completeness,  welfare,  peace’.  See  shalom  and cp.  Islam,  Moslem,  Musulman,  selamlik. Derivative:  salaam,  salam,  intr.  and  tr.  v. salable,  adj.  —  Formed  fr.  sale  with  suff.  -able. Derivatives:  salabil-ity ,  n.,  salable-ness,  n., salabl-y,  adv.
33521:salamander,  n.  —  ME.  salamandre,  fr.  MF.  (=  F.) satamandre,  fr.  L.  salamandra,  fr.  Gk.  <rocXa|i.av- Spa,  which  is  of  uncertain  origin.
33523:salami,  also  salame,  n.,  a  highly  seasoned,  orig. Italian,  sausage.  —  It.  salami,  fr.  L.  sal,  gen. salis,  ‘salt’.  See  salt,  n.
33562:Salome,  fern.  PN.  —  Late  L.,  fr.  Gk.  SaXcopT], which  is  rel.  to  SaXtoptiv,  ‘Solomon’.  See
33563:Solomon.
34869:shalom,  n.,  the  usual  Jewish  form  of  greeting.  — Heb.  shalom,  ‘peace’,  prop,  ‘completeness, soundness,  welfare’,  from  the  stem  of  shaldm, ‘he  was  intact,  was  complete,  was  in  good health’,  whence  also  shalem,  ‘complete,  sound’, shelem,  ‘peace  offering’;  rel.  to  Aram,  sh  lam, sh^lama,  ‘welfare,  peace’,  Arab,  sdlima ,  ‘he  was safe’,  aslama,  ‘he  surrendered,  submitted’,  sa- lam,  Ethiop.  saldm,  ’welfare,  peace’,  Akkad. shaldmu,  ‘to  be  complete,  be  safe',  shalamu, shulmu,  ‘welfare,  peace’.  Cp.  Solomon  and  the second  element  in  Absalom,  Jerusalem.  Cp.  also salaam  and  words  there  referred  to.  Cp.  also skeleton.
```


## [2026-09-14T02:28:22.588Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; cat data/verification/sources/SOURCE_MATRIX.md | head -120"
}
```


### [2026-09-14T02:28:22.654Z] TOOL RESULT

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
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt` (truncated before the lexicon's h–z section, ~p. 208 on)
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT_full.txt` (complete archive.org djvu text — use this for lexicon pages 208–215: haumavarga-, siyamam, etc.)
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
```


## [2026-09-14T02:28:31.068Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport re\ntxt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nlines=txt.split('\\n')\n# build leaf index per line\nleaf=0\nleafof=[]\nfor l in lines:\n    leafof.append(leaf)\n    leaf+=l.count('\\f')\nfor n in [1236,19966,20245,24476,33518,33562,34869]:\n    print(n, 'leaf',leafof[n-1], 'est printed p', (leafof[n-1]-12)*2)\nEOF"
}
```


## [2026-09-14T02:28:31.942Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '24476,24480p' KLN_1966.txt; echo ---SOLOMON---; grep -n -i 'Solomon,' KLN_1966.txt | head -5"
}
```


### [2026-09-14T02:28:32.308Z] TOOL RESULT

```
1236 leaf 15 est printed p 6
19966 leaf 442 est printed p 860
20245 leaf 447 est printed p 870
24476 leaf 540 est printed p 1056
33518 leaf 730 est printed p 1436
33562 leaf 731 est printed p 1438
34869 leaf 759 est printed p 1494
```


### [2026-09-14T02:28:32.383Z] TOOL RESULT

```
Moslem,  n.,  a  Mohammedan.  —  Arab,  muslim,
‘a  believer  in  Islam’,  lit.  ‘one  who  has  submitted himself  to  God’,  part,  of  dslama,  ‘he  surrender¬ ed,  submitted’,  IV  (=  causative)  form  of  salama, ‘he  was  safe’.  See  salaam  and  cp.  Islam.
mosque,  n.,  a  Mohammedan  place  of  worship.  — F.  mosquee,  fr.  It.  moschea,  fr.  earlier  moscheta, fr.  Sp.  mesquita  (whence  ModSp.  mezquita),  fr. Arab,  masjid,  ‘place  of  worship,  mosque’,  which is  either  borrowed  fr.  Nabatean  masgedha, ‘place  of  worship’,  or  formed  independently, with  ma-,  a  pref.  denoting  place,  fr.  sdjada,  ‘he was  submissive,  prostrated  himself  in  prayer’, which  is  rel.  to,  or — more  prob. — borrowed from  Aram,  s^ghedh,  of  s.m.  Cp.  masjid,  mes- quite.
mosquito,  n.,  gnat.  —  Sp.,  dimin.  of  mosca,  ‘fly’, fr.  L.  musca,  ‘fly’,  which  derives  from  the  I. -E. imitative  base*m»s-,  ‘to  buzz’.  See  midge  and  cp. words  there  referred  to.
moss,  n.  —  ME.  mos,  fr.  OE.  mos,  ‘marsh,  moor  , rel.  to  OE.  meos,  ‘moss’,  ON.  mosi,  Dan.  mos, ‘moss’,  Swed.  mossa,  ‘moss’,  mosse,  ‘moor’, MDu.  mosse,  Du.  mos,  ‘moss',  OHG.,  MHG. mos,  ‘moss,  swamp,  moor’,  OHG.  mios,  MHG. mies,  ‘moss’,  G.  Moos,  ‘moss’,  ON.  myrr,  ‘bog, swamp’,  fr.  I.-E ,*meu-s-,  whence  also  L.  museus, ‘moss’,  Lith.  miisaX,  ‘mold,  mildew’,  OSlav. mucha,  ‘moss’  and  perh.  L.  mustus,  ‘fresh,  new’ (if  fr.  *mus-tos,  ‘wet,  moist’),  whence  mustum (short  for  mustum  vinum),  ‘new  wine’.  F.  mousse, ‘moss’,  is  a  Teut.  loan  word.  I.-E.  *meu-s-  is  an -s-enlargement  of  base  *meu-,  ‘moist;  marsh; moss’.  Cp.  mire,  muscoid,  muscology,  mushroom, must,  ‘new  wine’,  mustard.  For  derivatives  of base  *meu-d-,  a  -(/-enlargement  of  base  *meu-, see  mother,  ‘dregs’,  and  cp.  words  there  referred to.
---SOLOMON---
35872:solo,  n.,  piece  sung  or  played  by  a  single  person. —  It.,  lit.  ‘alone’,  fr.  L.  solus.  See  sole, ‘alone’. Derivatives:  solo,  adj.  and  intr.  v.,  soloist  (q.v.) soloist,  n.,  singer  or  player  of  a  solo.  —  A  hybrid coined  fr.  solo  with  -ist,  a  suff.  of  Greek  origin. , Solomon,  masc.  PN, ;  name  of  David’s  son,  king of  Judah  and  Israel,  the  wisest  of  all  men.  Hence the  name  Solomon  is  often  used  to  denote  a  very wise  man.  —  Gk.  So Xopcov,  also  SaXo tp.d>v,  fr. Heb.  Shilomoh,  which  is  rel.  to  shalSm,  ‘peace’. See  shalom  and  cp.  Salome.  The  Arabic  PN.s Soliman,  Suleiman  derive  fr.  Heb.  Shildmoh. Solon,  n.,  a  wise  Athenian  statesman  and  law¬ giver.  His  name  is  sometimes  used  metaphoric¬ ally  to  denote  a  wise  man.  — •  Gk.  S6X<ov. Solpugida,  n.,  an  order  of  spiders  (zool.)  — ModL.,  formed  with  suff.  -ida  fr.  L.  solipiiga, solpiiga,  alt.  of  salpuga,  ‘a  kind  of  venomous  ant or  spider’,  which  is  of  uncertain  origin.  The forms  solipiiga,  solpiiga  are  due  to  a  folk-etymo¬ logical  association  of  the  word  with  sol,  ‘sun’, solstice,  n.  —  ME.,  fr.  OF.  (=  F.),  fr.  L.  solsti- tium  (for  *sol-statiom),  lit.  ‘the  standing  still  of the  sun’,  compounded  of  sol,  ‘the  sun’,  and  the stem  of  stare,  ‘to  stand’.  See  Sol  and  state,  n., and  cp.  interstice.
```


## [2026-09-14T02:28:50.781Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for n in 425 426 749 750 715 716; do echo \"=== leaf $n ===\"; awk 'BEGIN{RS=\"\\f\"} NR=='$((n+1))' {print substr($0,1,300)}' KLN_1966.txt; done"
}
```


### [2026-09-14T02:28:51.856Z] TOOL RESULT

```
=== leaf 425 ===
ggle  out  of,  to  surmount’, fr.  e-  and  luctari,  ‘to  struggle,  wrestle’,  which  is cogn.  with  Gk.  Xuyos,  ‘any  pliant  twig’,  Xuy££eiv ‘to  twist,  bend’,  OE.  loee,  ‘lock’.  See  lock,  ‘tuft’, and  cp.  reluctance.
Derivatives:  ineluctabil-ity,  n.,  ineluc
=== leaf 426 ===
nquiet,  hostile’, lit.  ‘seized’,  rel.  to  manifestus,  ‘evident’,  lit.  ‘that which  can  be  seized  by  the  hand’,  and  prob. cogn.  with  OI.  dharsati,  ‘dares’,  Gk.  ffdpoo?, ffpdcro?,  ‘courage,  audacity’,  OE.  ic  dearr,  ‘I dare’.  See  dare  and  words  t
=== leaf 749 ===
second'.  See  second,  adj. securable,  adj.  —  Formed  fr.  the  verb  secure  (see next  word)  with  suff.  -able, secure,  adj.,  safe.  —  L.  securus,  ‘free  from  care’, fr.  se-  and  cura,  ‘care’.  See  cure,  ‘care’,  and  cp. sure  and  sicker,  which  are  doublets  o
=== leaf 750 ===
hol,  n.,  name  of  the  Heb. -Aram,  vowel  sign  ’.' —  Aram.  s(ghbl,  lit.  ‘cluster  of  grapes' ;  so  call¬ ed  from  its  form.
segholate,  adj.  and  n.  (Heb.  gram.)  —  ModL. segholdtus,  ‘provided with  a  seghol’;  so  called because  the  segholates  always  have  a  seg
=== leaf 715 ===
��word’,  lit.  ‘that which  is  spoken’,  p?jm.;,  ‘speech’,  and  to  Eipm (for  *flpi6>),  ‘1  say,  speak’,  sfpwv  (for  *ft- ptcov),  ‘dissembler’,  lit.  ‘sayer’  (i.e.  one  who speaks  in  order  to  hide  his  thoughts),  Eipomaa, ‘irony’,  and  cogn.  with  O
=== leaf 716 ===
G.  and
OE.  rim,  ‘number’;  for  the  cognates  of  these Teut.  words  see  arithmetic  and  rite.  The  spelling of  E.  rhyme  (for  rime )  is  due  to  a  confusion  with Gk.  puffp.6;,  ‘rhythm’,  with  which  it  has  nothing in  common.  Cp.  rime,  ‘rhyme’.  Cp.  also  the  se
```


## [2026-09-14T02:29:04.664Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for n in 447 730 759; do echo \"=== leaf $n first/last 200 ===\"; awk 'BEGIN{RS=\"\\f\"} NR=='$((n+1))' {print substr($0,1,200); print \"...LAST...\"; print substr($0,length($0)-200)}' KLN_1966.txt; done"
}
```


### [2026-09-14T02:29:05.753Z] TOOL RESULT

```
=== leaf 447 first/last 200 ===
its  horsemen, jenneting,  n.,  a  kind  of  early  apple.  —  Formed with  subst.  suff.  -ing  fr.  F.  Jeannet,  dimin.  of Jean  (see  Jean,  masc.  PN.);  so  called  because supposed  to  be  
...LAST...
edan  law  on  unbelievers.  —  Arab.  jizyah,  fr. Syr.  gezithd,  ‘poll  tax’.  See  Fraenkel,  Die  ara- maischen  Fremdworter  im  Arabischen,  p.  283, and  cp.  Arthur  Jeffery,  Ph.  D.,  
=== leaf 730 first/last 200 ===
:  Sahar-an,  Sahar-ian,  Sahar-ic,  adjs. sahib,  n.,  a  title  used  in  India.  —  Hind,  sdhih,  fr. Arab,  sahib,  ‘companion,  lord,  master’,  fern. $afiibah,  prop.  part.  Of  fdhiba, 
...LAST...
e,  adj. salina,  n.,  pool,  pond,  —  Sp.,  fr.  L.  salinae,  ‘salt¬ works’.  —  See  next  word, saline,  adj.,  salty.  —  F.,  fr.  L.  *salinus,  fr.  sal, gen.  salis,  ‘salt’.  
=== leaf 759 first/last 200 ===
darkness’,  Olr.  scath,  OW.  scod, Bret,  squeut,  ‘darkness’.  Cp.  shadow  and  shed, n.  (which  is  a  doublet  of  shade).
Derivatives:  shade,  tr.  and  intr.  v.,  shad-ed,  adj., shad
...LAST...
cond  element  in nuncheon.
Derivatives:  shank,  tr.  and  intr.  v.,  shank-ed, adj.
shantung,  n.,  a  coarse  silk.  —  Named  after  the Chinese  province  Shan-Tung. shanty,  n.,  hut.  —  Ca
```


## [2026-09-14T02:29:22.577Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; ls | grep -i -E 'FSD|AHD|WEB|SKT|LKT|HJB|AID|MON|ARY' "
}
```


### [2026-09-14T02:29:22.635Z] TOOL RESULT

```
AHD_watkins1985.txt
AID.txt
FSD_vol1.txt
FSD_vol2.txt
FSD_vol3.txt
FSD_vol4.txt
HJB.txt
LKT.txt
MON_part1.txt
MON_part2.txt
NYB_vol2_glossary.txt
SKT_dli_revised.txt
SKT.txt
WEB_vol1.txt
```


## [2026-09-14T02:29:24.145Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i 'salem\\|shalom\\|šalām\\|slm' AHD_watkins1985.txt | head -20; echo \"=== sal- roots ===\"; grep -n '^sal-\\|^sal[-0-9]' AHD_watkins1985.txt | head"
}
```


### [2026-09-14T02:29:24.218Z] TOOL RESULT

```
=== sal- roots ===
899:sal-'
901:sal-2
```


## [2026-09-14T02:29:42.073Z] TOOL CALL #15: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 3
}
```


### [2026-09-14T02:29:42.083Z] TOOL RESULT

```


```


## [2026-09-14T02:29:43.430Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n '1,40p' tools/fetch_source.py; echo ===; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'));print(json.dumps(d['AHD'],ensure_ascii=False,indent=1));print(json.dumps(d['OEW'],ensure_ascii=False,indent=1))\""
}
```


### [2026-09-14T02:29:44.473Z] TOOL RESULT

```
Exit code 1
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
(eval):1: == not found
```


## [2026-09-14T02:29:48.433Z] TOOL CALL #17: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B3%D9%84%D8%A7%D9%85",
 "prompt": "Give the full Arabic and Persian etymology sections for سلام (salām): Arabic root س ل م, Proto-Semitic reconstruction, cognates (Hebrew shalom, Akkadian, Aramaic), and the Persian entry's statement that it is borrowed from Arabic. Quote exactly."
}
```


## [2026-09-14T02:29:50.014Z] TOOL CALL #18: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A5%D8%B3%D9%84%D8%A7%D9%85",
 "prompt": "Give the etymology of Arabic إسلام (ʔislām): verbal noun of which form/verb, root, and meaning. Quote exactly."
}
```


### [2026-09-14T02:29:54.876Z] TOOL RESULT

```
# Etymology of Arabic إسلام (ʔislām)

According to the Wiktionary entry, إسلام is the **verbal noun of the verb أَسْلَمَ (ʔaslama) in Form IV**.

The exact quote states: "Verbal noun of _[أَسْلَمَ](/wiki/%D8%A3%D8%B3%D9%84%D9%85#Arabic "أسلم")_ (ʔaslama)."

The root is **س ل م** (s l m), which encompasses 25 related Arabic terms. The word carries meanings related to submission and resignation, deriving from the root concept of peace and submission.
```


### [2026-09-14T02:29:57.037Z] TOOL RESULT

```
# Etymology of سلام (salām)

## Arabic Section

**Root:** The page lists the Semitic root as س ل م (s l m), with "25 terms" belonging to this root.

**Etymology 1 Etymology Statement:** "Semantic loan from Aramaic שְׁלָמָא / ܫܠܵܡܵܐ (šəlāmā, 'wholeness, welfare; peace', used as a greeting). Cognate with Hebrew שלום (shalóm)."

The entry does not provide a Proto-Semitic reconstruction or Akkadian cognates on this page.

## Persian Section

**Etymology Statement:** "Borrowed from Arabic سَلَام (salām, 'peace')."

The Persian section confirms the direction of borrowing but does not elaborate on deeper etymological layers or provide Proto-Semitic information.

**Note:** The complete historical-comparative Semitic etymology you're requesting—including Proto-Semitic reconstruction and Akkadian parallels—is not present in the supplied Wiktionary article content.
```


## [2026-09-14T02:29:59.716Z] TOOL CALL #19: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/so-long",
 "prompt": "Give the full Etymonline entry for \"so long\" (farewell), including the proposed origins (Hebrew shalom, Arabic salaam, Irish slan, German so lange), dates of first attestation, and OED's stance. Quote exactly."
}
```


## [2026-09-14T02:30:01.138Z] TOOL CALL #20: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/so_long",
 "prompt": "Give the etymology section of the English interjection \"so long\" (goodbye) — what origins are proposed (Hebrew shalom, Arabic salaam, Malay, German, Irish), and what the entry says is uncertain. Quote exactly."
}
```


### [2026-09-14T02:30:02.883Z] TOOL RESULT

```
I appreciate your detailed question, but I must be transparent: the web page content provided does not contain an Etymonline entry for "so long." 

The page shows only the website's header, navigation menu, footer information, and general site structure—no actual dictionary entries are visible in the content shared with me.

To access the full entry you're requesting, including proposed origins and attestation dates, you would need to visit etymonline.com directly and search for "so long."
```


### [2026-09-14T02:30:05.921Z] TOOL RESULT

```
# Etymology of "So Long"

According to the Wiktionary entry, the etymology is **uncertain**. The entry states:

> "Uncertain. Compare to Swedish _hej så länge_ and Russian _пока_ (poka)."

The entry does not propose Hebrew, Arabic, Malay, German, or Irish origins. Instead, it only mentions comparisons to Swedish and Russian expressions, while noting that the ultimate origin remains unknown. The entry references the Online Etymology Dictionary for further information but does not detail specific alternative origin theories in the section provided.
```


## [2026-09-14T02:30:11.245Z] TOOL CALL #21: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D7%A9%D7%9C%D7%95%D7%9D",
 "prompt": "Give the Hebrew etymology of שלום (shalom): root ש־ל־ם, Proto-Semitic reconstruction if any, meanings (peace, completeness, welfare), and cognates listed (Arabic salām, Aramaic, Akkadian šalāmu). Quote exactly."
}
```


## [2026-09-14T02:30:13.319Z] TOOL CALL #22: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Jerusalem",
 "prompt": "Give the full etymology of Jerusalem: Hebrew Yerushalayim, the proposed meanings (\"foundation of Shalem\", \"city of peace\"), the god Shalem, Ugaritic/Amarna forms (Urusalim), and the route via Greek Hierousalēm / Latin. Quote exactly what the entry says."
}
```


### [2026-09-14T02:30:17.423Z] TOOL RESULT

```
# Hebrew Etymology of שלום (Shalom)

**Root:** ש־ל־ם (sh-l-m)

**Etymology:** The word is "etymologically related to _שָׁלָה_ (šālâ, 'to be quiet, tranquil')" and shares connections with _שָׁלַו_ (šālaw, "to be quiet, at ease").

**Primary Meaning:** Peace (uncountable noun in modern usage)

**Secondary Meanings:** The entry notes archaic senses including rest and quietude, plus a formal sense of well-being or welfare (commonly seen in expressions like "How are you?").

**Cognates Across Semitic Languages:**
- Arabic: سلام (salām)
- Aramaic: שְׁלָמָא (šlāmā)
- Phoenician: 𐤔𐤋𐤌 (šlm /šalōm/)
- Ugaritic: 𐎌𐎍𐎎 (šlm /šalāmu/)

**Note:** The Wiktionary entry does not include Proto-Semitic reconstructions or Akkadian cognates, only these Northwest Semitic and related languages.
```


### [2026-09-14T02:30:20.238Z] TOOL RESULT

```
# Etymology of Jerusalem

The Wiktionary entry provides a straightforward etymological chain but does not include the detailed semantic analysis you've requested.

**What the entry states exactly:**

"From Old English _Hierusalem_ or Old French _Jherusalem_ or Late Latin _Ierusalem_, _Hierusalem_, from Latin _Hierosolyma_, from Ancient Greek _Ἰερουσαλήμ_ (Ierousalḗm), from Biblical Hebrew _יְרוּשָׁלַיִם_ (Yərūšālayim)."

The entry traces the word backward through European languages to its Hebrew root but does not discuss proposed meanings like "foundation of Shalem," the deity Shalem, or alternate ancient forms such as those found in Ugaritic or Amarna correspondence. These etymological interpretations, while historically significant, are absent from this particular dictionary entry.
```


## [2026-09-14T02:30:27.592Z] TOOL CALL #23: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D7%99%D7%A8%D7%95%D7%A9%D7%9C%D7%99%D7%9D",
 "prompt": "Give the etymology of Hebrew ירושלים (Yerushalayim): what elements it is analysed into (yry/yrw \"to found\" + Shalem the deity?), the Amarna form Urusalim, and whether \"city of peace\" is called a folk etymology. Quote exactly."
}
```


## [2026-09-14T02:30:29.165Z] TOOL CALL #24: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Salome",
 "prompt": "Give the etymology of the name Salome: Ancient Greek Σαλώμη, from Hebrew shalom / Shlomit, and any statement about Latin/Late Latin transmission. Quote exactly."
}
```


### [2026-09-14T02:30:34.625Z] TOOL RESULT

```
# Etymology of Salome

Based on the Wiktionary entry, here is the documented etymology:

The name Salome derives from **Ancient Greek *Σαλώμη* (Salṓmē), which came from Hebrew *שְׁלוֹמִית* (sh'lomít)**. The Hebrew root connects to *שָׁלוֹם* (shalóm), meaning "peace."

The entry states: "From Ancient Greek _Σαλώμη_ (Salṓmē), from Hebrew _שְׁלוֹמִית_ (sh'lomít) (belonging to the same root as _שָׁלוֹם_ (shalóm, 'peace'))."

**Note on Latin transmission:** The Wiktionary article provided makes no mention of Latin or Late Latin as a transmission point in the etymology. The path documented is directly Hebrew → Ancient Greek → English.
```


### [2026-09-14T02:30:36.015Z] TOOL RESULT

```
# Etymology of Hebrew ירושלים (Yerushalayim)

According to the Wiktionary entry, the etymology is disputed. The source identifies two main proposed analyses:

**Possible compound origin:** "Possibly of ultimate origin _[יָרוּ](/wiki/%D7%99%D7%A8%D7%94#Hebrew "ירה")_ (yarú, 'he lays down') +‎ _[שָׁלֵם](/wiki/%D7%A9%D7%9C%D7%9D#Hebrew "שלם")_ (Shalém, 'the Canaanite god [Shalem]')"

**Folk etymology:** The entry explicitly labels an alternative explanation as popular rather than etymologically sound: "Popular etymological explanation _[יִרְאֶה](/wiki/%D7%A8%D7%90%D7%94#Hebrew "ראה")_ (yir'é, 'he sees') +‎ _[שָׁלוֹם](/wiki/%D7%A9%D7%9C%D7%95%D7%9D#Hebrew "שלום")_ (shalóm, 'peace')."

**Ancient attestations:** The entry notes the name is "Akin to [Akkadian](https://en.wikipedia.org/wiki/Akkadian_language "w:Akkadian language") _[𒌑𒊒𒊓𒅆𒆠](/wiki/Uru%C5%A1alim#Akkadian "Urušalim")_ (Urušalim)" and references a form in Ancient Egyptian, confirming pre-Hebrew Semitic roots rather than deriving from Hebrew components alone.
```


## [2026-09-14T02:30:42.129Z] TOOL CALL #25: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/selamat",
 "prompt": "Give the Malay/Indonesian etymology of selamat: borrowed from Arabic سلامة (salāma)? Quote exactly, and list the greeting uses (selamat jalan, selamat tinggal)."
}
```


## [2026-09-14T02:30:43.430Z] TOOL CALL #26: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/salang",
 "prompt": "List every language section for the word \"salang\" and the meaning given in each (especially Malay/Indonesian). Quote exactly. Does any sense mean \"peace, greetings, farewell\"?"
}
```


### [2026-09-14T02:30:48.087Z] TOOL RESULT

```
# Etymology of Selamat

**Malay Etymology:**
"Borrowed from Arabic سَلَامَة (salāma)."

**Indonesian Etymology:**
"Inherited from Malay selamat, from Arabic سَلَامَات (salāmāt), plural of سَلَام (salām)."

## Greeting Uses

The word appears in multiple salutations:

- **selamat jalan** – "May you go safely!/Goodbye!"
- **selamat tinggal** – (listed as a compound greeting)
- **selamat pagi** – "Good morning"
- **selamat malam** – "Good evening/night"
- **selamat datang** – "Welcome"
- **selamat makan** – "Enjoy your meal"

These expressions use selamat as an adverb meaning "may there be..." in Malay, functioning as a blessing formula preceding the main word describing the situation.
```


### [2026-09-14T02:30:49.168Z] TOOL RESULT

```
# Language Sections and Meanings for "Salang"

**Brunei Malay**: "resin (secretion of plants)" and "resin (viscous liquid of plant origin)"

**Central Bikol**: "jaw; jawbone"

**Kavalan**: "soup"

**Malay (Noun)**: "a method of execution where a keris is impaled through the collarbone and into the heart"

**Malay (Verb)**: "to execute by the keris"

**Tagalog (First Noun)**: "something being cooked on a pot" and "act of putting a pot on fire or stove"

**Tagalog (Second Noun)**: "very light touch (with a finger or hand)" and "unintentional mention or reference"

**Answer to your question**: No. None of these definitions mean "peace, greetings, or farewell." The word "salang" carries meanings related to resin, anatomy, cooking, execution methods, and gentle touch across these languages, but contains no sense relating to salutations or peaceful sentiments.
```


## [2026-09-14T02:30:55.594Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; ls site/pages/459.jpg 2>/dev/null; pdftoppm -f 459 -l 459 -r 300 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg459 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg459.png"
}
```


## [2026-09-14T02:30:56.232Z] TOOL CALL #28: WebSearch

```json
{
 "query": "\"so long\" farewell etymology OED Malay salang Shipley \"Origins of English Words\" salaam shalom"
}
```


### [2026-09-14T02:30:57.723Z] TOOL RESULT

```
site/pages/459.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb 68729 Sep 13 22:30 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg459.png
```


### [2026-09-14T02:31:07.700Z] TOOL RESULT

```
Web search results for query: ""so long" farewell etymology OED Malay salang Shipley "Origins of English Words" salaam shalom"

Links: [{"title":"The origin of so long - OUP Blog - Oxford University Press","url":"https://blog.oup.com/2018/03/the-origin-of-so-long/"},{"title":"The Origin of so long. : languagehat.com","url":"https://languagehat.com/the-origin-of-so-long/"},{"title":"So long - Origin & Meaning of the Phrase","url":"https://www.etymonline.com/word/so%20long"},{"title":"'So Long': A Common But Mysterious Goodbye | Merriam-Webster","url":"https://www.merriam-webster.com/wordplay/so-long-origin"},{"title":"So Long - phrase meaning and origin","url":"https://www.phrases.org.uk/bulletin_board/35/messages/194.html"},{"title":"so long meaning, origin, example, sentence, etymology","url":"https://www.theidioms.com/so-long/"},{"title":"The Grammarphobia Blog: So long, farewell, auf Wiedersehen, goodbye","url":"https://grammarphobia.com/blog/2009/01/so-long-goodbye.html"}]

Based on the search results, I found information about the etymology of "so long" and various proposed connections to other languages:

## Main Etymology Theories

The phrase is a parting salutation from 1860, of unknown origin, perhaps from a German idiom (compare German parting salutation adieu so lange) or influenced by Hebrew shalom (via Yiddish sholom). Scandinavian leave-taking phrases have been noted as similar, such as Norwegian Adjø så lenge and Swedish Hej så länge, meaning "goodbye for now".

## Malay Connection

One theory proposes that so long is a transformed shortening of the Malay formulas of parting, selamat tinggal ('stay safe', said by the one who is leaving) and selamat jalan ('walk safe', said by the one who remains behind). Etymologically, selamat comes from Arabic salāmāt, the plural of salām, and in Malay the literal meaning 'peace' is extended to 'safety, security'.

## Consensus on Origins

Earlier guesses that it was a sailors' corruption of a South Pacific form of Arabic salaam are not now convincing. By the 20th century, so long became a common expression of farewell—and no one knows how it happened. Its origins are surprisingly murky.

Note: The search did not return specific information from Shipley's "Origins of English Words," though various similar etymologies are discussed in the sources found.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-14T02:31:12.531Z] TOOL CALL #29: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg459.png"
}
```


### [2026-09-14T02:31:13.286Z] TOOL RESULT

```

```


## [2026-09-14T02:31:13.277Z] INPUT

[Image: original 2550x3300, displayed at 1546x2000. Multiply coordinates by 1.65 to map to original image.]


## [2026-09-14T02:31:34.004Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== FSD vol4 so long ===\"; grep -n -i 'so.long' FSD_vol4.txt | head -20; echo \"=== FSD vol4 salaam/salam ===\"; grep -n -i '^salaam\\|^salam\\b' FSD_vol4.txt FSD_vol3.txt | head"
}
```


### [2026-09-14T02:31:34.118Z] TOOL RESULT

```
=== FSD vol4 so long ===
=== FSD vol4 salaam/salam ===
```


## [2026-09-14T02:31:35.964Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== MON اورشلیم ===\"; grep -n 'اورشلیم\\|أورشليم' MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt 2>/dev/null | head; echo \"=== MON سلام ===\"; grep -n 'سلام' MON_part1.txt MON_part2.txt 2>/dev/null | head -5"
}
```


### [2026-09-14T02:31:36.077Z] TOOL RESULT

```
=== MON اورشلیم ===
incoming/MON/MON_2vol_Adena_v1_djvu.txt:28381:که در نخستین پاک نتوانسته‌اند در اورشلیم 
MON_part1.txt:28381:که در نخستین پاک نتوانسته‌اند در اورشلیم 
=== MON سلام ===
MON_part1.txt:85:محمد معین دورة ابتدائی را در دبستان اسلامی و دور اول متوسطه را در 
MON_part1.txt:150:در ژانویةٌ همان سال در (موتمر اسلامی) جدننوه‌انمی عنسداهة که در لاهور 
MON_part1.txt:346:مقالات وی در موضوعات ادب؛ تاریخ ادیان» ایران دورة قبل از اسلام و 
MON_part1.txt:347:عهد اسلامی» تار بخ ادبیات» آثار باستانی» علوم تربیتی و غبره در محله‌های: 
MON_part1.txt:2919:مشغولی. تاب» طاقت. سلامت» راحت.
```


## [2026-09-14T02:31:41.517Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for n in 168 170 172; do echo \"=== FSD_vol4 leaf $n (approx p $((n+2146))) ===\"; awk 'BEGIN{RS=\"\\f\"} NR=='$((n+1))' {print substr($0,1,400)}' FSD_vol4.txt; done"
}
```


## [2026-09-14T02:31:42.135Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '28370,28395p' MON_part1.txt"
}
```


### [2026-09-14T02:31:42.587Z] TOOL RESULT

```
=== FSD_vol4 leaf 168 (approx p 2314) ===
  others  furnish  articles  of  food 5   Is  the  potato  [<I>L  jofanwm,  nightshade  ]
so'lar,  1   so'l&r,  2   solar,  a   1.  Of,  pertaining  to,  or connected  with  the  sun,  proceeding  from  the  sun,  de-
SogQ*  1   sSngn  2   sOn^,  n   Ice  Sa^as  The  name  of  the fylke  over  which  Skate.  Bele  and  Bele  s   sons,  Helge  and
lyiae  over  wmeo  osate.  Meie  ana  aeie  s   son
=== FSD_vol4 leaf 170 (approx p 2316) ===
n  the Isle  of  Wight  and  Hampshire  England,  2   to  5   m.  wide BoTe-oId,  1   sdTi-eld,  2   65  le-6Id  i.  a   Of  or  pertaining  to the  So^eids  ILn  Oneof  theSofrief^  (<  Solea -i- -OU)  I Bol'cTt,  n   A   sollar. sol^er-et',  n   Same  as  souxeet sole'shlpt,  n   Excluslv  e   ownership,  control,  o- right.
anxiety*  or  concern,  as  for  the  attainment  of  Eomething sought 
=== FSD_vol4 leaf 172 (approx p 2318) ===
rial  segments  of  which  the  body  of  a   verte- brate Is  theoretically  composed  a   somite
Professor  Goodsir  s   terms  of  Somatome*  for  the  segments  and Metasomstomes  for  their  interspaces  apiicar  to  mo  to  be  well worthy  of  adoption  Huxlet  m   AnnaU  and  Maoasxne  of  hat. Hut  third  senes  p   433
\<  Gr  sbma,  body,  -f*  -tome  1— so'^ma-tom'lc,  a
soivs'bcrg-l
```


### [2026-09-14T02:31:42.642Z] TOOL RESULT

```
پا کان خطهٌ اول: (کد.) ملایکه و کروبیان و 
حاملان عرش معلی. با ک و بوست کنده: 
صریح و روشن,» بی‌کنایه» بی‌پرده» پاک و 
پوست کنده. زر با کك: زر خالص. 

پا ک: ۲25 (.) عید بزرگ بهود که هر سال 
در چهاردهمین روز از نخستین ماه قمری به 
یاد خروج قوم بنی‌اسرائیل از مصر برپا 
می‌دارند و در چهاردهمین روز از دومین ماه 
قمری هر سال نیز بهودیان جشن پا ک را بنام 
دومین پاک می‌گیرند تا بیماران یا مسافرانی 
که در نخستین پاک نتوانسته‌اند در اورشلیم 
حضور یابند از آن برخوردار شوند؛ عید 
پااکك» عید فصح, پاسکاء باغوث» عید فطیر. 
بکرتز اعا رک اسان کار بان » 
یاد برخاستن مسیح از میان مردگان بر پا کنند» 
مد ای مستح؛ هد اضتم نمارا با غو 
پاکار: 7 (- پای‌کار] (ص‌مر. امر.) 
کسی را گویند که چون تحصیلداری بجایی 
بسياید او زر از سردم تحصیل کند و به 
تحصیلدار دهد شخصی که در شهرها و 
7 
دیوانی نماید؛ کا رگذاره عربف. کسی که 
برای محافظت کشت و زرع دهقانان در 
دهکده‌ها مدت یک سال استخدام شود. 
خدمتکار) بادو» جاکر» نوک خادم. آنکه
```


## [2026-09-14T02:31:55.067Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i \"so.long\" FSD_vol4.txt | head -20; echo \"=== good-by ===\"; grep -n -i \"good-by\" FSD_vol4.txt | head -20"
}
```


### [2026-09-14T02:31:55.170Z] TOOL RESULT

```
=== good-by ===
14071:8.  At  all  events,  m   any  case,  at  all  now  only  in  the compounds  whosoever,  whichsoever,  etc  0.  Accord- ing to  the  truth  of  what  is  sworn  to  or  averred  said  in oaths  or  asseverations,  as,  so  help  me  God,  t   e ,   God help  me  according  as  my  statements  are  true  10. (Colloq  1   To  each  an  extent  used  clliptically  for  so much,  as,  I   loved  him  so,  I   could  not  do  it  11  (Colloq  I Indeed '   elliptical  for  is  it  sof  as,  are  you  going?  So  f 12.  [Rare  ]   So  as  to  follow  immediately,  then,  there- fore, as,  there  was  an  insult,  and  fio  a   blow’  13.  (Rare] After  that,  then,  as,  say  “good-by,"  and  so  be  off  14. (Archaic  1   Let  it  be  that  way,  verj  well,  as,  if  jou  are agreed,  so,  if  not,  so  [   <   AS  swd,  so  ]   saej  [Scot  ]
31154:The  jadement  of /otf«  simply  expresses  a   felt  harmony  m   ^   lu'-tu'  2   ta'-ia'  interj  1   [Colloq  1   Good-by  m   Uondon  for  the  sale  and  exchange  of  horses  so  called
46271:farewell,  good-by;  adieu  (L  ,   imper  of  zaleo,  be  well  1 TaP'odlc'tlou,  1   valT-dik’^en,  2   vSre-dlc’shon,  n   A saying  of  vale,  a   bidding  farewell  [<  L   raledictus, pp  of  rafedico,  <   zale  (see  vale,  tnfer^  )   +   dico,  say  1 S3T1Z  see  adieu
66287:the  thing  See  realism,  1   (2),  universal,  n ,   2   (1)  auf  WIedersehen  [G  )   Till  we  meet  again,  good-by,
```


## [2026-09-14T02:31:59.851Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\ntxt=open('FSD_vol4.txt',encoding='utf-8',errors='replace').read()\nlines=txt.split('\\n')\nleaf=0\nfor i,l in enumerate(lines,1):\n    if i==14071:\n        print('line 14071 leaf',leaf,'approx printed p',leaf+2146)\n        break\n    leaf+=l.count('\\f')\n# print that leaf\nblocks=txt.split('\\f')\nprint(blocks[leaf][:2500])\nEOF"
}
```


### [2026-09-14T02:32:01.179Z] TOOL RESULT

```
line 14071 leaf 163 approx printed p 2309
als  2.  A   bird,  the  snow- buntmg  snow'fleck"t.  3   Bot  Any  one  of  several bulbous  plants  of  the  genus  Leucojum,  resembling  the snow  drop,  but  w   ith  the  flow  ers  larger,  sev  eral  on  a   scape, and  the  permnth'segments  of  the  same  size  Three  spe- cies. the  spring  snowflake  (Z,  rernum),  the  summer S.  (C,  xstivum),  and  the  autumn  s.  (L  autumnale), are  in  cultivation  4.  A   cloth  pattern  hav  mg  on  the  sur- face small  knots  that  resemble  snowflakes  —   luminous snowflakes,  snowflakes  floating  high  In  the  air  and  glit- tering In  the  sunlight,  so  as  to  be  v   Islble  In  a   telescope Enow'»Qea'',  etc  See  snow*,  n
Bnow'flow"cr,  1   sno'flau'er,  2   sno'flow'er  n   1.  The
1.  Abounding  m   or  full  of  snow,  as,  a   snowy  day  character  of  being  snuffy
2.  White  like  snow,  snow-white,  hence,  figuratively,  snuff'ing,  1   snuf'ip,  2   sniif'ing,  n   1   The  act  of  one
pure,  unblemished,  spotless,  as,  snowy  Unen  who  or  that  which  snuffs  2.  Tonmny  The  splitting  of
—   snowy  egret  or  heron,  an  entirely'  v^fle  egret  (Ardea  jjjg  cjiticie  of  a   hide  in  the  process  of  finishing  — -!y ,   odv candidlssima)  ranging  from  New  York  to  Chile  now  nearly  snujj/jfjnt,  n   A   muff  snuft'klnf
exterminated  by  plum^hunters  acting  for  the  mnilnery-  gnuf'fle,  )   1   snuf'l,  2   snuf'].  v   [snttt'fled,  snuf'ld**,
(Nyctea  nydea)  of  northern  regloM States  and  Europe  In  winter  It  Is  white, black— s.  plover,  a   ring-plover  (^gialites  ntcosa)  of western  North  America  It  Is  Iight^gmy,  with  dark  patches on  the  top  and  sides  of  the  head  and  sides  of  the  breast,  with white  underbody..
snubb  1   snub,  2   snub,  rf  [snubbed,  ssubd*,  sntjb'- BiNG  ]   1.  To  rebuff,  check,  or  repress  by  a   cuttmg  or satirical  reply  or  remark
It  19  by  the  lofinite  9Tiu6&ina«of  ezrcnence  that  men  have their  pndo  broucht  down  to  its  proper  proportion
H   W   BrECHCS  Plymouth  Pulpit  vol  *   p   24S  b   b   r   1873  1 2   To  treat  with  debberate,  studied,  or  contemptuous neglect,  slight  intentionally,  as,  to  snub  an  old  ac-
II  t   1.  To  breathe  wTth  difficulty  and  somewhat noisily  through  the  nose,  as  when  the  nasal  passages  are obstructed,  draw  with  effort  short  catches  of  breath, also,  to  talk  through  the  nose,  and  hence  to  talk  in
```


## [2026-09-14T02:32:14.004Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -iE \"so.?long,? +[0-9]? *(interj|adv|a\\b)\" FSD_vol4.txt | head; echo \"=== all so.long occurrences ===\"; grep -c -iE \"so.?long\" FSD_vol4.txt; grep -n -iE \"sd.?long|so'long|so-long\" FSD_vol4.txt | head"
}
```


### [2026-09-14T02:32:14.147Z] TOOL RESULT

```
=== all so.long occurrences ===
1
```


## [2026-09-14T02:32:21.262Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i \"so.long\" FSD_vol4.txt; echo \"---\"; sed -n '14060,14090p' FSD_vol4.txt | grep -n -i \"long\" "
}
```


### [2026-09-14T02:32:21.380Z] TOOL RESULT

```
---
7:A   Flemish  painter  of  fruit-pieces,  animals,  etc snj'ing,  1   snarip,  2   any'ing,  n   Naut  A   curved  plank worked  edgewise  into  a   vessel's  frames  at  the  bow  or  stern So,  1   85,  2   85,  n   Bib  2   Kinos  xvli,  4   {Hcb  1 SO,  1   BO,  2   so,  adp  I.  To  this  or  that  or  such  a   degree; to  this  or  that  extent,  in  the  same  degree,  quantity,  or proportion  Used  (1)  alone,  the  degree  being  Implied  or understood  as,  why  do  you  hesitate  so  long?
13:So  Is  used  In  attnbutiic  compound  adjectives,  as,  so- called  roses,  so-named,  so-styled,  etc —   and  so  on,  and  so  forth  See  under  forth,  adv  —   by so  (that)t.  1.  If  only,  provided  that  2.  In  tho  degree or  to  the  extent  that  — quite  so,  just  as  you  have  said, exactly  an  expression  of  assent  —   so-and-so,  n   An  unde- termined or  Imaginary  person,  as,  Dr  5o-amf-so  — so  as. 1   In  such  a   manner  or  degree  as  with  such  a   result  or  pur- po<?e  as  as,  he  shouted  so  as  to  be  heard  a   mile  away  2 (Colloq  1   If  only,  on  condition  that,  as,  he  Is  willing  to  do any  work,  so  as  It  is  honorable  3t.  Such  as  —   so  called, called  as  stated  generally  styled  thus  usually  implying  a doubtful,  questioned,  or  Improper  form,  as,  certain  roses,  so called ,   so-called  roses  —   so  far  1   To  that  extent,  degree,  or point  as,  so /ar  5   ou  are  right  2   As  yet ,   as,  I   ha\  e   not  seen him  so /or  —   bO  fashion  [Colloq  ,   U   S   ),  in  that  (right)  way, as,  the  knot  should  be  tied  so  fashion  —   so  long,  see  so- LONG  — somuch  1.  As  much  us  is  implied  or  mentioned, as,  his  talk  was  so  much  foolishness  2   Such  an  amount or  quantity  not  determined  or  stited  as,  to  work  lor  so much  a   j   ear  — so  much  as,  to  whatever  extent  — so  so (Colloq  1,  tolerablj ,   fairly,  as,  How  are  >ou  getting  along? Oh,  so  so  —   so  that.  1   With  the  purpose  or  to  the  end that  as  we  eat  so  f/jof  we  may  live  2   With  the  result  that, as,  she  screamed  so  that  she  could  be  heard  across  the  street 3   If  onl> ,   on  condition  or  provided  that,  as,  he  Is  Indiffer- ent to  tho  means  so  that  he  accomplishes  his  purpose  — so  then,  the  fact  is  thus,  then  as  a   consequence,  as,  so then  you  are  going  away —   so  to  sa>,  so  to  speak,  if  one may  say  or  speak  thus,  saying  or  speaking  In  these  terms SO,  conj  1.  Provided  that,  on  condition  that,  as,  he Will  stop  at  nothing  dishonorable,  so  he  is  successful  a special  use  of  tho  adverb  2.  In  such  a   way  that,  as  a consequence  of  which,  as,  he  gave  his  promise,  so  they went  aw aj  3t.  As
20:the  water  soaks  its  way  through  the  soil  C.  (Rare  ] To  drain,  as,  a   purse  soaked  of  its  contents  7.  (U  S &   Prov  Eng  ]   To  bake  for  a   long  time,  as  bread  8. [Slang  ]   To  pawn,  as,  he  soaked  his  overcoat  9.  To heat  thoroughly  and  continuously  said  of  a   metal  10. [Slang,  U   SI  (1)  To  throw  swiftly  said  of  a   baseball  (2) To  charge  oxorbltantb  (3)  To  beat,  punch,  maltreat <4>  (College  Slang]  To  Impose  dKffcult  tasks  upon 11.  To  put  (steel  ingots)  into  a   soakmg-pit  to  prepare them  for  rolling  I2t.  To  render  soft,  weak,  or  ef- feminate, enfeeble
24:2   To  penetrate  through  pores  or  interstices,  perme- ate w   ith  in,  into,  or  through,  as,  the  ram  soaked  through the  walls  3.  To  drink  to  excess,  keep  oneself  satu- rated with  drink  4   To  bc  subjected  for  a   long  time to  tho  treatment  of  heat  said  of  mctnls  5   (Prov Eng  ]   To  become  drj  ,   drain  6.  (Southern  U   S   ]   To be  thoroughly  baked  7t«  To  flow  ( <   AS  socian,  < sflean,  suck  1   Syn  see  drench  — soak'*bar"rDl,  n   A   bar- rel In  which  fresh  fish  are  soaked  previous  to  salting  — s   *holo,  n   ( \ustral )   An  enclosed  space  in  a   stream,  In which  sheep  arc  washed  —   lo  s.  up  bait,  to  eat  bait,  as  fish, without  being  caught
```


## [2026-09-14T02:32:29.320Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -iE \"(so.?long|EO.?long|BO.?long|so.?LONG)\" FSD_vol4.txt | head; echo \"=== LONG+farewell ===\"; grep -nE \"long[^a-zA-Z]{1,6}(interj|1 +so)\" FSD_vol4.txt | head; echo \"=== search 'Malay' + 'salam' in vol4 ===\"; grep -n -i \"Malay.*sal\\|salam\" FSD_vol4.txt | head"
}
```


### [2026-09-14T02:32:30.480Z] TOOL RESULT

```
109159:1862  Military  Department  of  the  Ohio  1823:  Marcos  Bozzarls,  Greek  patriot, formed  killed  at  Karpenlsl  near  MIssolonghI
=== LONG+farewell ===
10580:Blde'long^,  1   soid'Ieg',  2 sld'ldng',  rf  [Prov  Eng]  To hobble  by  means  of  aide-hnes ,   side-Une slde'Iong'',  a   Inclining  or  tending  to  one  side,  lateral, obhque
=== search 'Malay' + 'salam' in vol4 ===
569:2-  Any  tree  from  which  sago  is  derived  [   <   Malay  I —   Portland  sago,  a   farinaceous  meal  obtained  from the  corm  of  the  European  wakc-robm  so  called  from the  Isle  of  Portland,  England,  where  It  was  formerly  pre- pared for  sale— 8a'go*palm",  n   1.  Either  of  two  East* Indian  monocarplc  palms  of  the  ’ genus  Metroxylon  (formerly  5a- gus) ,   the  spineless  sago-palm  i^f  vX
876:Salamlel  KetS  art,  ape,  fat,  fare,  fist,  what,  all;  me,  ggt,  prey,  fern;  hJt,  Ice,  1   =   6;  1   =   6;  gO,  nOt,  Or,  won,  wolf,  do,
959:Saint  Catharines Salamlel
1042:form  iSa/aTnandra maculosa  Is  the  com- mon European spotted  salaman- der; Ambystoma  tiOTi- num  Is  the  tiger  s.  of the  western  U   s
1059:Megalobatrachus  ja-  Spotted  Salamander  Vi
1060:Blant  s.  of  Japan,  which  attains  a   length  of or  more  The  salamanders  were  formerly  fabled to  llie  In  ani  extinqu'sh  Are  muieu
1064:passedover  and  near  their  surfaces  (2)  A   metal  drum  or hot  coals,  etc  ,   used  in  drying  plaster b'  rcolloo rennon.  a   loggerhead, term  He.  ^   fire'Pre°f  onginally  a   trade ^   four-footed  beast  represented  pas- sant, breathing  or  surrounded  by  fiames  7.  Alelal metal  or  siag  remaining  m   the /orewoo  “ftor  the  fires  are  drawn  [   <   r   sata- ”p  Pe?’s™an5arT“"*“'  "‘■'amohdre,  salamander.
1068:« -Sal"a-raan-drl'na,  n   vl .fferp  The  ^aZamandreftfea  —   Sal"a-m3n-drl'n<o.  n   vi Herp  1,  The  iSaZamandrfda;  as  a   subfamily  2   The  g/iZ/i mamfrofdca-saI"d-man'drln(e3.  I   a   1.  of  uertfin- Ing  to,  or  like  a   salamander,  enduring  fire  ’2  Ot  or pertaining  to  the  Safomandrin^  II  n   Oneof  the5a/aman- drin®  sal  a-man'drold  I.  a   Of  or  pertaining  to  the Salamandridx  -SaF'a- A   super/amlly  or  suborder ^   amphibians,  especially  those  having  two  pairs  of and  stapes  unconnected  with  the  quadrate r”.Bhl"a-man-drol'de-an,  a   &   n
1079:Salamina  Eet  V   artistic,  Crt;  fat,  fire,  fast;  gctiprey;  hit,  police;  obey,  gO;  not.  Or;  full,  rOle;  but,  bOm;  d   =   final;  1   =   habit,  renew;
1083:An  Island  oft  the  coast  of  Attica  Greece  30  sq  m   birth- place of  Solon  and  Euripides  Here  the  Greeks  under  The- mlstocles  defeated  the  Persians  under  Xerxes  in  a   naval battle  Oci  20.  480  B   C   -   Sa!"a-mln'l-an,  « sa^lam'stone",  1   se-lam'ston*, 2   sa-lam'atou  ,n  ilitncrut A   variety  of  sapphire  usually  m   small,  transparent, hexagonal  prisms  of  pale  red  or  blue,  found  in  Ceylon f<G  salamstein,  <   salam,  salaam,  +   slein,  stone  ] sal'an-gane,  1   sal'en-ggn,  2   sil'an-Sdn,  n   [FI  AnOilental swift  of  the  genus  Coltocatia,  whose  nests  are  edible,  espe- cially C   esculenta  See  Ulus  under  edible  bird  b»nest saPa-ganet;  sal"an-ga'nat,  saPan-glnfe^f Sa-lan'gl-dai,  1   sa-lan'ji-dl.  2   sa-lin'gl-dC,  n   pi  Ich  A family  of  salmonoldean  fishes  xvlili  head  depressed  and
```


## [2026-09-14T02:32:44.390Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\ntxt=open('FSD_vol4.txt',encoding='utf-8',errors='replace').read()\nblocks=txt.split('\\f')\nimport re\nfor i in range(160,182):\n    b=blocks[i]\n    hits=[m for m in re.findall(r'[Ss][o0][- \\'’]?[Ll][o0]n[gq]', b)]\n    if hits: print(i, i+2146, hits[:5])\n    # also print first 80 chars\nprint('---')\nfor i in range(168,178):\n    print(i, i+2146, repr(blocks[i][:120]))\nEOF"
}
```


### [2026-09-14T02:32:45.601Z] TOOL RESULT

```
---
168 2314 "  others  furnish  articles  of  food 5   Is  the  potato  [<I>L  jofanwm,  nightshade  ]\nso'lar,  1   so'l&r,  2   sola"
169 2315 'imber  used  for  staying  the  opening  of  a   mine\n1.  A   soleoid  flatfish  Solea  solea  or  vulgaris  is\nthe  com'
170 2316 'n  the Isle  of  Wight  and  Hampshire  England,  2   to  5   m.  wide BoTe-oId,  1   sdTi-eld,  2   65  le-6Id  i.  a  '
171 2317 't  of  the  genus  Vagnera, having  white  flowers  in  terminal  racemes  V   ractmosa, common  la  the  United  States'
172 2318 'rial  segments  of  which  the  body  of  a   verte- brate Is  theoretically  composed  a   somite\nProfessor  Goodsir  s'
173 2319 ' especially  of  an  articulate  ora  verto- brate,  asomatome;  metamere  (<  Gr.  s5r*q,bodvJ  — mesoblastlc  somite  '
174 2320 "uously,  a   half- fledged  poet  son'nct-er  or-lstt.— son'net-Izc,  p   I.  r To  apostrophize  In  a   sonnet  II.  1"
175 2321 "^nd^  <soph\nnople  4.  lB0f'i-8,  2s6n-a  In  occultism  and  theosophy,  °/lp6eymveraity,I^gond,forjumorsopm^^\nHeavenly"
176 2322 'd  dnzunishing  the  number,  till  either  >   ou  admit  that ho  who  was  not  bald  with  a   certam  number  of  h'
177 2323 ' A   whispered  rumor,  report  (2)  The  tone in  which  the  psalm  and  other  services  were  droned  in old  Scotch'
```


## [2026-09-14T02:32:55.928Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== HJB salaam ===\"; grep -n -i \"salaam\" HJB.txt | head -5; echo \"=== AID salaam ===\"; grep -n -i \"salaam\\|islam\" AID.txt | head -5; echo \"=== SKT Moslem/Islam ===\"; grep -n -i \"^moslem\\|^islam\\|^salaam\\|^salam\" SKT.txt SKT_dli_revised.txt | head; echo \"=== LKT islam/salam ===\"; grep -n -i \"salām\\|salam\\b\\|Islam\" LKT.txt | head -8"
}
```


### [2026-09-14T02:32:56.034Z] TOOL RESULT

```
=== HJB salaam ===
14266:1563.— *' And  these  regents  .  .  .  concerted among  themselves  .  .  .  that  they  should aeize  the  Kin^  of  Daquem  in  Bedar,  which is  the  chief  city  and  capital  of  the  Decan ; )Bo  the^  took  him  and  committed  him  to  one of  their  number,  by  name  Veirido ;  and  then he  and  the  rest,  either  in  person  or  by  their representatives,  make  him  a  salaam  {calema) at  certain  days  of  the  year.  .  .  .  The  verido who  died  in  the  year  1510  was  a  Hungarian by  birth,  and  originally  a  Christian,  as  I have  heard  on  sure  authority." — Oarcicij  f. 85  and  859.
19055:SALAAM,  s.  A  salutation; properly  oral  salutation  of  Mahom- meoana  to  each  other.    Arab,  mlam^
19068:1694.  —  "  The  Town  Oonlcopolies,  and chief  inhabitants  of  Egmore,  came  to  make their  Salaam  to  the  President."— W^A<«r/«-, i.  281.
19070:1809.—"  The  old  priest  was  at  the  door, and  with  his  head  uncovered,  to  make  his salaams."- Z^.  Valetuioy  i.  273.
=== AID salaam ===
741:The  name  of  a   caste  ;   they  are actors  and  ventriloquists,  and  have a   special  knack  of  dressing  one  side of  the  face  like  a   man,  and  the  other like  a   woman,  and  moving  the  head about  so  sharply  as  to  appear  to  be two  persons.  Some  have  adopted islAm.
890:Bargujur.  The  name  of  a   division  of the  RAjputs,  accounted  one  of  the thirty-six  royal  races,  and  claiming descent  from  RAma’s  second  son  ; they  are  numerous  in  Rohilkhand. A   branch  of  the  tribe  adopted  islAm in  the  time  of  Alauddin  Khilji,  but retains  many  Hindu  customs.  The name  has  been  adopted  also  by subdivisions  of  BrAhmans,  BhuksAs, and  Meos.
5896:SAbaliA.  [GujarAti.]  The  name  of  a low  caste  ;   they  tend  cattle.  Some are  converts  to  islAm.
6382:converted  to  islAm  during  the  rule of  the  Ummayide  dynasty  of  khalifs ; they  are  taller  and  more  robust  than the  natives  of  India ;   they  are  quiet and  inoffensive,  but  excessively  in- dolent ;   they  are  Sunnis  by  religion, but  some  traces  of  the  caste  system remain  among  them  {Hughes).
7518:BLUNT  (Wilfrid  S.) — The  Future  of  Islam.  Crown  8vo.  6s. BODDY  (Alexander  A.) — To  Kairwan  the  Holy.  Scenes  in  Muham-
=== SKT Moslem/Islam ===
SKT_dli_revised.txt:39904:Islam, the religious system of Miiham- 
SKT_dli_revised.txt:49746:Moslem, a Mussulman. (Arab.') Arab 
SKT_dli_revised.txt:67360:Salaam, Salam. (Arab ) Arab. 
SKT_dli_revised.txt:67371:Salamander, a reptile. (F. - L. - 
SKT_dli_revised.txt:67376:salamander. 
SKT_dli_revised.txt:67453:salami, pi. of salame, salt-meal, fiom L. 
SKT_dli_revised.txt:73306:Moslem mystic ; from Arab, suftyy intel* 
SKT_dli_revised.txt:94751:Islam, jerboa, jinn, koran, raahdi, Maho- 
SKT_dli_revised.txt:94753:moslem, muezzin, mufti, omrah, otto, 
SKT.txt:11915:Moslem,  a  Mussulman.  (Arab.)  Arab. moslim,  *a  mnsulmao,  a  true  believer  in the  Mohammedan  faith ; '  Richardson.  Cf. Arab.  mtualUm,  oat  who  aoqniesces.  A mussuiman  is  one  who  professes  ii/dm, i.  e.  submission  to  the  will  of  God  and  to the  orthodox  faith. —  Arab,  sa/ama,  to  sub- mit %  The  E.  words  mosUm,  mussuiman, islam,  and  talaam  are  all  from  the  &ame Arab,  root  satama,  to  submit.
=== LKT islam/salam ===
30:Was  die  Ausgangssprachen  angeht,  so  kommen  in  erster  Linie  die Sprachen  des  islamischen  Kulturkreises  in  Betracht,  insbesondere  das Arabische,  Persische  und  Türkische;  daneben  lieferten  von  den  semitischen Sprachen  das  Hebräische  und  das  Aramäische,  ferner  das  Sanskrit  und seine  modernen  Entwicklungen  dem  Abendlande  manches  neue  Wort. Weniger  zahlreich  sind  die  Entlehnungen  aus  den  anderen  indischen  Sprachen [Drawidasprachen],  dem  Chinesischen  und  Japanischen  sowie  dem  Malay- ischen.  Gewöhnlich  wird  ein  orientalicher  Abkömmling  nicht  gleichzeitig in  alle  europäischen  Sprachen  aufgenommen,  vielmehr  von  einer  Einzelsprache ihrem  nationalen  Lautbestande  angeglichen  und  so  an  die  Nachbarsprachen weitergegeben.  Im  Altertum  sind  es  natürhch  vorwiegend  das  Griechische und  Lateinische,  die  diese  Durchgangsstation  bilden.  Ich  konnte  mir  nicht die  Aufgabe  stellen,  alle  griechisclien  und  lateinischen  Wörter,  die  seit  den
41:Die  weitaus  bedeutsamste  Verbindung  des  Morgen-  und  Abendlandes im  Altertum  wurde,  wenn  von  einer  Besprechung  der  Wirkung  der  Perser- kriege in  sprachlicher  Hinsicht  abgesehen  werden  darf,  durch  den  Zug Alexanders  des  Großen  hervorgerufen.  Bis  auf  diese  Zeiten  läßt  sich  der erste  reichlichere  Abfluß  orientalischer  Begriffe  und  Wörter  in  die  griechische Sprache  und  in  den  darauf  folgenden  Jahrhunderten  ins  Latemische  zurück- führen; seitdem  erstreckt  sich  die  Wirkung  in  ununterbrochenem  Flusse bis  auf  die  heutigen  modernen  Sprachen  und  Dialekte  Europas.  Das  folgende hellenistische  Zeitalter  begünstigte  aus  hier  nicht  zu  erörternden  Gründen die  Entlehnung  orientalischen  Sprachgutes  in  hervorragendem  Maße:  die Verbreitung  des  Judentums  und  die  Entstehung  des  Christentums  gaben Anlaß  zur  Übernahme  vieler  hebräischer  und  aramäischer  Wörter  ins Griechische  und  Lateinische  [besonders  in  die  als  Kichenlatein  bezeichnete Färbung].  Mit  dem  Mittelalter  beginnt  der  Einfluß  des  Arabischen.  Nach- dem sich  der  Islam  von  den  malayisclien  Inseln  bis  zu  den  Gestaden  des Atlantischen  Ozeans  verbreitet  hatte,  war  eine  riesige  Berührungslinie  des arabischen  Sprachgebiets  mit  dem  Abendlande  geschaffen.  Der  Wortschatz der  Sprachen  der  Pyrenäenhalbinsel,  des  Spanischen,  Portugiesischen  und Katalanischen,  und  in  geringerem  Umfange  anch  der  des  ProvenzaHschen, Französischen  und  Italienischen  werden   mit  arabischen   Wörtern  derart
45:(iurchtränkt,  daß  B.  das  Spanische  nach  Ausscheidung  der  arabischen Elemente  nicht  mehr  fähig  wäre,  seine  Funktion  als  moderne  Sprache auszuüben.  Fast  tausend  Jahre  arabisclier  oder  islamischer  Herrschaft  und Kultur  haben  deren  Stempel  den  Sprachen  des  westlichen  Mittelmeerbeckens unauslöschlich  aufgeprägt.  Dagegen  setzt  die  Wirkung  auf  die  Sprachen  des ('istlichen  Beckens  des  mittelländischen  Meeres  erst  später  ein;  bis  zum Falle  Konstantinopels  schützt  das  griechische  Sprachgebiet  den  Osten  Euro- pas vor  orientalischer  Sprachüberflutung.  Nur  die  Inseln,  besonders  Malta, Sizilien  und  Sardinien,  wie  aucli  Unteritalien  sind  mehrere  Jahrhunderte hindurch  arabischer  Sprach-  und  Kulturwirkung  ausgesetzt,  deren  Förde- rung durch  Friedrich  II.  und  vielleicht  schon  durch  seine  Vorgänger  aus dem  Geschlechte  der  Hohenstaufen  nicht  zu  unterschätzen  ist.  Die  Wirkung der  direkten  Berührung  der  Abendländer  mit  dem  Orient,  wie  sie  im vorhergehenden  Zeitalter  der  Kreuzzüge  vor  sich  gegangen  war,  wird  auf diese  W^eise  nachhaltig  verstärkt;  auch  der  Aufschwung  der  arabischen Lehrtätigkeit  in  den  südeuropäischen  Zentren  der  Gelehrsamkeit  ist  nicht ohne  dauernden  Einfluß  auf  die  Gestaltung  des  Wortschatzes  der  romani- schen Sprachen  geblieben.  Hervorgehoben  sei  besonders  das  damals  ein- gedrungene arabische  Element  im  Wortschatz  der  Anatomie  und  Mathematik. Bei  der  im  Mittelalter  noch  größeren  Freizügigkeit  der  Gelehrten  und Ungelehrten  und  praktischeren  Internationalität  der  Wissenschaft,  als  wir sie  heute  besitzen,  verbreiteten  sich  die  arabischen  Elemente  rasch  bis  in  die nordischen  Länder  gemanischer  Zunge.  Gewiß  haben  zu  dieser  schnellen Verbreitung  auch  die  Juden  beigetragen,  die  seit  dem  frühen  Mittelalter sämtliche  europäische  Sprachen  mit  Wörtern  ihrer  Muttersprache  oder  des verwandten  Arabischen  bereicherten.  Besonders  im  Deutschen  ist  dieser Einfluß  sehr  lebendig  gewesen  und  hat  ja  zur  Bildung  eines  weit  ver- breiteten Dialektes,  des  Jiddischen,  geführt.
100:Isl  =  Der  Islam.  Zeits<  hrift  für  Geschichte  un(t  Kultur  des  islamischen  Orients. Berlin-Leipzig.    (Früher:  Straßburg.)
352:d)  Ar.  lä  iläh  illaHläh  'es  gibt  keinen Gott  außer  Alläh'  [Kur'än,  Sure  2,  256] ist  das  islamische  Bekenntnis  zur  Ein- heit Gottes,  der  sog.  tauhid,  der  als Kriegs-  u.  Schlachtruf  gedient  haben mag.  Daraus  wurde  einerseits  sp.  leli- lies  'der  Ruf  der  Mauren,  wenn  sie  den Kampf  beginnen'  [bei  Don  Ouijote II.  Teil,  34.  Kap.,  in  der  oben  genannten Ausgabe  S.  189,  letzte  Zeile],  anderer- seits vielleicht  sp.  alarido  'Geschrei,  Ge- heul', wohl  auch  frz.  hallali,  dlsch. Halali.  [Rom  Forsch  IV,  374.  ML  4974. Löbel  EITAP  56.  ZDMG  XL,  258,  De- vic  DEt  135.
2085:[Vom  ar.  Vb.  hagara  'verlassen,  freund- schaftliche Beziehungen  abbrechen'] 'Auswanderung,  Abbruch  der  Beziehun- gen', insbesondere  der  W^egzug  des  Pro- pheten MUHAMMAD  von  Mekka  nach Medina,  der  nach  der  üblichen  Rech- nung am  16.  Juli  622  n.  Chr.  stattfand; die  muhammedanische  Zeitrechnung  be- ginnt mit  dieser  sog.  „Flucht",  die  aber gar  keine  Flucht  war  [s.  auch  C.  H. Becker,  Islamstudien  I:  Vom  Werden und  Wesen  der  islamischen  W^elt.  Leip- zig 1924.  S.  340];  hieraus  rum.  hegirä, frz.  hegire,  it.  egira,  sp.  hegira,  pg.  he- jira;  engl.  ndl.  hegira,  dtsch.  Hedschra  ; russ.  gidzra
2180:[Vom  Vb.  amma  'vorhergehen']  'Vor- gesetzter, Vorsteher',  insbesondere  die- jenige Person,  die  einer  Versammlung vorsieht,  um  das  Zeremoniell  bei  den öffenthchen  Gebeten  am  Freitag  und an  den  Beiramsfesten  zu  leiten.  Da  dies in  den  ersten  Zeiten  des  Islams  von  den Kalifen  selbst  geschah,  so  nahmen  sie den  Titel  imäm  an;  dieser  Titel  wurde sodann  auch  erteilt  1.  den  Lehrern  der ersten  islamischen  Jahrhunderle  als  den ersten  Auslegern  des  Korans,  2.  den Rehgionsdienern,  die  an  den  Moscheen die  Obliegenheiten  des  Priestertums  im Namen  des  obersten  Imäms  ausübten. Tk.  ebenso  iniam;  hieraus  rum.  imam, engl,  imam,  ungenau  iman;  ebenso  frz. iman,  imam,  dessen  Funktionen  imamat, imanat  heißen;  russ.  imam  'Ik.  Schrift- gelehrter'. [Devic  DEt  142.  Lammens Rem  136.
2203:Eigentlich  Infin.  des  Vbs.  salama  IV 'sich  unterwerfen',  nämlich  dem  Willen Gottes,  also  'Ergebung  in  Allahs  Willen'. Es  ist  der  Name  für  die  Religion  Mu- hammads geworden:  dtsch.  Islam,  engl. islam,  islamism  ;  frz.  islain,  islamisme,  it. islaniismo;  russ.  islam  [s.  hier  Nr.  1516  a].
```


## [2026-09-14T02:32:57.391Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== FVQ islam/salam ===\"; grep -n -i \"islām\\|islam\\|salām\" FVQ_pages.txt | head -10; echo \"=== AFM سلام ===\"; grep -n \"( سلام\\|سلام )\" AFM_pages.txt | head -5"
}
```


### [2026-09-14T02:32:57.466Z] TOOL RESULT

```
=== FVQ islam/salam ===
31:how recent work at Islamic origins, such as that done by the late
131:Bell, R. Origin of Islam in its Christian Environment. London, 1926.
135:Caetani, L. Annali dell* Islam, vols. i and ii. Milano, 1905, 1907.
151:Encyclopaedia of Islam. Ed. Houtsma, etc. Leiden, 1913 ff.
171:Goldziher, I. Die Richtungen der islamischen Koranauslegung. Leiden, 1920.
208:Jacob, G. Das Leben der vorislamischen Beduinen, nach den Quellen gzschildert.
226:Les Sancluaires preislamites dans VArabie occidentale. Beirut, 1926.BIBLIOGRAPHY Xlll
310:The Jewish Foundation of Islam. New York, 1933.
337:El Encyclopedia of Islam.
380:Islam had its roots deep down in this old Arabian paganism. Tt
=== AFM سلام ===
```


## [2026-09-14T02:33:05.718Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== HJB 19055 ===\"; sed -n '19055,19067p' HJB.txt | cut -c1-900; echo; echo \"=== SKT salaam ===\"; sed -n '67360,67370p' SKT_dli_revised.txt; echo \"=== SKT.txt salaam ===\"; grep -n -i \"Salaam,\" SKT.txt | head -3"
}
```


### [2026-09-14T02:33:05.807Z] TOOL RESULT

```
=== HJB 19055 ===
SALAAM,  s.  A  salutation; properly  oral  salutation  of  Mahom- meoana  to  each  other.    Arab,  mlam^
*  peace.'    Used  for  any  act  of  saluta- tion ;  or  for  *  compliments.'
[c.  60  B.C.— "  'AW  €1  fUw  Zipoiifffrl  "SaXA/i,"  €i  S'
"  Nai«tof,"  el  «*  'EXXiyr  "  Xatpe"-  t»  S'
a^b  0p(i<ror.** — MeUagroif  in  Antholbgia  PalcUina,  vii.  149.
The  point  is  that  he  has  been  a  bird  of passage,  and  says  good-bye  now  to  his various  resting-places  in  their  own  tongue.]
1518.— "The  ambassador  (of  Bisnagar) entering  the  door  of  the  chamber,  the  €k>- vemor  rose  from  the  chair  on  which  he  was seated,  and  stood  up  while  the  ambassador made  him  great  oalema."— Correez,  Lendae, II.  i.  377.    See  also  p.  431.
1552.— "The  present  having  been  seen  he took  the  letter  of  the  Governor,  and  read  it to  him,  and  having  read  it  told  him  how  the (governor  sent  him  his  ^ema,  and  was  at his  command  with  all  his  fleet,  and  with  all the  Portuguese.  .  .  ."—CcutaiUieday  iii.  445.
1611.— "Calema.  The  salutation  of  an inferior." — uobarruviat,  Sp,  Did.  8.v.
1626.—"  Hee(Selim  i.e.  Jahanglr)  tumeth ouer  his  Beadee,  and  saith  so  many  words, to  wit  three  thousand  and  two  hundred, and  then  presenteth  himself  to  the  people  to receive  their  salames  or  good  morrow.  ..." — PurchcLSf  Pilgrimage^  51».
1638. — "  En  entrant  ils  se  salUent  de  leur Salom  qu'ils  accompagnent  d'vne  profonde inclination."— Jfan</«/jf/o,  Pari.s,  1659,  223.
1648.—"  ...  this  salutation  they  call salam  ;  and  it  is  made  with  bending  of  the body,  and  laying  of  the  right  hand  upon the  head."— Kaa  TwiU,  55.
1689.  —  "  The  Salem  of  the  Religious Bramins,  is  to  join  their  Hands  together, and  spreading  them  flrst,  make  a  motion towards  their  Head,  and  then  stretch  them out." — Ovinfftoriy  183.

=== SKT salaam ===
Salaam, Salam. (Arab ) Arab. 
saldm, saluting, wishing peace ; a saluta- 
tion. — Arab s a////, saluting. 4 hIeb.j/^<7/i?;//, 
peace, from shdlam, to be safe. 

Salad. (F. — Itak — L.) F. salade.^ 
M. Jtak salata, a salad of herbs ; lit. 
‘salted;’ lem. of salato, salted, pickled, 
pp of salare, to salt. — Ital. sale, salt. — 
L. sal, salt. See Salt. 

=== SKT.txt salaam ===
```


## [2026-09-14T02:33:07.571Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\ntxt=open('LKT.txt',encoding='utf-8',errors='replace').read()\nlines=txt.split('\\n')\nleaf=0\nfor i,l in enumerate(lines,1):\n    if i>=2195 and i<=2215:\n        pass\n    if i==2203:\n        print('leaf',leaf,'printed p',leaf-26)\n        break\n    leaf+=l.count('\\f')\nprint('\\n'.join(lines[2195:2210])[:1500])\nEOF"
}
```


### [2026-09-14T02:33:08.581Z] TOOL RESULT

```
leaf 100 printed p 74
912.  Ar.  isfaiiärija:
'Pastinake'  [lat.  pastinaca,  woraus  wahr- scheinlich auch  das  ar.  Wort  entstanden istj,  vulg.  wie  auch  sanärija;  hieraus sp.  zahanoria  'Mohrrübe,  Karotte'.  [DE 224.
913.  Pers.  iskänbä:
'Eingeweide,  Kaldauuen',  tk.  iskembe 'dass.',  dazu  iSkembe  corbasy  'Kaidaunen- suppe'; hieraus  rum.  schimbea  'dass.' [Löiiel  EITAP  84].
914.  Pers.  iskängfä:
'Folter,  Qual',  tk.  iskenge;  hieraus  rum. schingiü  'dass.'.
915.  Ar.  isläm:
Eigentlich  Infin.  des  Vbs.  salama  IV 'sich  unterwerfen',  nämlich  dem  Willen Gottes,  also  'Ergebung  in  Allahs  Willen'. Es  ist  der  Name  für  die  Religion  Mu- hammads geworden:  dtsch.  Islam,  engl. islam,  islamism  ;  frz.  islain,  islamisme,  it. islaniismo;  russ.  islam  [s.  hier  Nr.  1516  a].
916.  Ar.  istiftäh:
'Anfang,  erster  Verkauf  eines  Kaufmanns am  Tage'  [Infin.  des  Vbs.  fataha  'öff- nen' VIII],  ebenso  tk.  zu  syftaii  [Kele- kian  Kämus  680  b]  vereinfacht ;  hieraus rum.  seftea,  saftea  'erste  Einnahme, glücklicher  Beginn'  [Löbel  EITAP  80].
917.  Ar.  itbä':
'Gefolge,  Dienerschaft'  [Infin.  des  Vbs. taWa  'folgen'  IV],  ebenso  tk.  etba; hieraus  rum.  ecpaea  'Gefolge'.
918.  Ar.  itmid:
[Aus  äg.  kopt.  stün,  altäg.  sdm,  woraus auch  gr.  oti|U|ui,  lat.  sfibium]  'Antimon'; hieraus  mit  starker  Verstümmelung  [viel- leicht aus  der  ar.  Vokalisation  utmud heraus]  mlat.  antimonium,  frz.  antinwine [woraus  die  spafähafte  Vo
```


## [2026-09-14T02:33:16.022Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://www.ahdictionary.com/word/semitic.html",
 "prompt": "Find the Semitic root entry for šlm / ślm (\"to be sound, safe, whole; peace\"). Quote the entry, listing the derivatives it gives (salaam, Islam, Moslem/Muslim, shalom, Absalom, Jerusalem, Solomon, Salome)."
}
```


## [2026-09-14T02:33:17.086Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://archive.org/advancedsearch.php?q=identifier%3Aoriginsofenglish00jose&fl%5B%5D=identifier&rows=1&output=json",
 "prompt": "Just report whether the item exists."
}
```


### [2026-09-14T02:33:19.357Z] TOOL RESULT

```
Yes, the item exists. The search query found one document with the identifier "originsofenglish00jose" in the database.
```


### [2026-09-14T02:33:20.269Z] TOOL RESULT

```
# Semitic Root Entry: šlm / ślm

I was unable to locate the specific entry for šlm / ślm in the provided web page content. The document appears to be truncated mid-entry at the "pṭr" root, ending before reaching the "š" section where this root would appear alphabetically.

To find this entry with the derivatives you mentioned (salaam, Islam, Moslem/Muslim, shalom, Absalom, Jerusalem, Solomon, Salome), you would need to access the complete dictionary page or scroll further down in the original source material.
```


## [2026-09-14T02:33:28.837Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 tools/fetch_source.py 'https://www.ahdictionary.com/word/semitic.html' --note 'page 459, root S.l.m: AHD Semitic roots appendix (online updated version of Nourai AHD:1541)' ; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%B3%D9%84%D8%A7%D9%85' --note 'page 459 node 1,2: Arabic/Persian salam' ; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/salang' --note 'page 459 node 4: Malay salang = keris execution, not peace'"
}
```


## [2026-09-14T02:33:29.977Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; curl -s 'https://archive.org/metadata/originsofenglish00jose' | python3 -c \"import json,sys; d=json.load(sys.stdin); print(d.get('server'), d.get('dir'), len(d.get('files',[])))\""
}
```


### [2026-09-14T02:33:30.885Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/75b739fc6c2698d2.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/7b721e1f00162ce7.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c20c692021293696.txt
```


### [2026-09-14T02:33:33.039Z] TOOL RESULT

```
ia600508.us.archive.org /0/items/originsofenglish00jose 37
```


## [2026-09-14T02:33:35.103Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; grep -n -i \"šlm\\|ślm\\|shalom\\|Absalom\\|salaam\" 75b739fc6c2698d2.txt | head -20; echo; wc -c 75b739fc6c2698d2.txt"
}
```


### [2026-09-14T02:33:35.159Z] TOOL RESULT

```
57: Absalom , from Hebrew ʾ abšālōm , short for ʾ ăbîšālōm , my father (is) peace ( šālōm , peace; see šlm ). Both a and b from Hebrew ʾ ăbî , shortened form of ʾ ābî , my father, from ʾ āb , father. 
209: shalom aleichem , from Hebrew ʿ ălêkem , to you, from ʿ al, ʿ ălê , to, toward, upon (a preposition akin to ʿ ālâ , to ascend) + -kem , you (plural). 
1508: ‌ šlm 
1510:To be whole, sound; Common Semitic noun *šalām‑ , well-being, welfare, peace. shalom; ; shalom aleichem , from Hebrew šālōm , well-being, peace, from šālēm , to be safe, sound;
1511: Absalom , from Hebrew ʾ abšālōm , my father (is) peace (see ʾ b ). 
1516: salaam , from Arabic salām , well-being, peace, from salima , to be safe, sound. 

117763 75b739fc6c2698d2.txt
```


## [2026-09-14T02:33:36.406Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; for q in salang \"so+long\" salaam; do echo \"=== $q ===\"; curl -s \"https://ia600508.us.archive.org/fulltext/inside.php?item_id=originsofenglish00jose&doc=originsofenglish00jose&path=/0/items/originsofenglish00jose&q=$q\" | head -c 1500; echo; done"
}
```


### [2026-09-14T02:33:38.482Z] TOOL RESULT

```
=== salang ===
<!DOCTYPE html>
<html lang="en">
<!-- __ _ _ _ __| |_ (_)__ _____
    / _` | '_/ _| ' \| |\ V / -_)
    \__,_|_| \__|_||_|_| \_/\___| -->
  <head>
    <title>Item not available</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <link href="/about/css/ia.css?v=1" rel="stylesheet" type="text/css"/>
    <link rel="SHORTCUT ICON" href="https://archive.org/images/glogo.jpg"/>
  </head>
  <body class="navia">
    <a href="#maincontent" class="hidden-for-screen-readers">Skip to main content</a>

    <!-- Wraps all page content -->
    <div id="wrap">
      <div id="navwrap1">
        <div id="navwrap2">
          <div class="navbar navbar-inverse navbar-static-top1" role="navigation">
            <ul class="nav navbar-nav navbar-main">
              <li class="pull-left">
                <a title="Home" class="navia-link home" href="https://archive.org/" target="_top">
                  <span class="iconochive-logo"></span>
                  <span><img src="https://archive.org/images/wordmark-stacked.svg" alt="IA wordmark-stacked-logo" height="30px" style="margin-left: 10px;"/></span>
                </a>
              </li>
              <li class="dropdown dropdown-ia pull-left">
                <a title="Web" class="navia-link web"  href="https://web.archive.org" target="_top"><span class="iconochive-web" aria-hidden="true"></span><span>Web</span></a>
              </li>
              <li class="dropdown dropdown-ia pull-left">
               
=== so+long ===
<!DOCTYPE html>
<html lang="en">
<!-- __ _ _ _ __| |_ (_)__ _____
    / _` | '_/ _| ' \| |\ V / -_)
    \__,_|_| \__|_||_|_| \_/\___| -->
  <head>
    <title>Item not available</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <link href="/about/css/ia.css?v=1" rel="stylesheet" type="text/css"/>
    <link rel="SHORTCUT ICON" href="https://archive.org/images/glogo.jpg"/>
  </head>
  <body class="navia">
    <a href="#maincontent" class="hidden-for-screen-readers">Skip to main content</a>

    <!-- Wraps all page content -->
    <div id="wrap">
      <div id="navwrap1">
        <div id="navwrap2">
          <div class="navbar navbar-inverse navbar-static-top1" role="navigation">
            <ul class="nav navbar-nav navbar-main">
              <li class="pull-left">
                <a title="Home" class="navia-link home" href="https://archive.org/" target="_top">
                  <span class="iconochive-logo"></span>
                  <span><img src="https://archive.org/images/wordmark-stacked.svg" alt="IA wordmark-stacked-logo" height="30px" style="margin-left: 10px;"/></span>
                </a>
              </li>
              <li class="dropdown dropdown-ia pull-left">
                <a title="Web" class="navia-link web"  href="https://web.archive.org" target="_top"><span class="iconochive-web" aria-hidden="true"></span><span>Web</span></a>
              </li>
              <li class="dropdown dropdown-ia pull-left">
               
=== salaam ===
<!DOCTYPE html>
<html lang="en">
<!-- __ _ _ _ __| |_ (_)__ _____
    / _` | '_/ _| ' \| |\ V / -_)
    \__,_|_| \__|_||_|_| \_/\___| -->
  <head>
    <title>Item not available</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <link href="/about/css/ia.css?v=1" rel="stylesheet" type="text/css"/>
    <link rel="SHORTCUT ICON" href="https://archive.org/images/glogo.jpg"/>
  </head>
  <body class="navia">
    <a href="#maincontent" class="hidden-for-screen-readers">Skip to main content</a>

    <!-- Wraps all page content -->
    <div id="wrap">
      <div id="navwrap1">
        <div id="navwrap2">
          <div class="navbar navbar-inverse navbar-static-top1" role="navigation">
            <ul class="nav navbar-nav navbar-main">
              <li class="pull-left">
                <a title="Home" class="navia-link home" href="https://archive.org/" target="_top">
                  <span class="iconochive-logo"></span>
                  <span><img src="https://archive.org/images/wordmark-stacked.svg" alt="IA wordmark-stacked-logo" height="30px" style="margin-left: 10px;"/></span>
                </a>
              </li>
              <li class="dropdown dropdown-ia pull-left">
                <a title="Web" class="navia-link web"  href="https://web.archive.org" target="_top"><span class="iconochive-web" aria-hidden="true"></span><span>Web</span></a>
              </li>
              <li class="dropdown dropdown-ia pull-left">
```


## [2026-09-14T02:33:44.765Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; sed -n '1505,1525p' 75b739fc6c2698d2.txt"
}
```


### [2026-09-14T02:33:44.812Z] TOOL RESULT

```
 ‌ škr 

Common Semitic noun *šikar‑ , intoxicating drink. cider , from Greek sikera , from a Semitic source akin to Hebrew šēkār , Akkadian šikaru , intoxicating drink. 
 ‌ šlm 

To be whole, sound; Common Semitic noun *šalām‑ , well-being, welfare, peace. shalom; ; shalom aleichem , from Hebrew šālōm , well-being, peace, from šālēm , to be safe, sound;
 Absalom , from Hebrew ʾ abšālōm , my father (is) peace (see ʾ b ). 

 schlemiel , perhaps from the Hebrew personal name šəlūmî ʾ ēl , my well-being (is) God, from šəlūm , well-being, variant bound form of šālôm (see above; ʾ ēl , God; see ʾ l ). 
 Solomon , from Hebrew šəlōmōh , his (God's) peace, from šəlōm , bound form of šālôm (see above). 
 Salome , from a Hebrew personal name akin to šəlōmît , Shelomith (biblical name), from šālôm (see above). 
 salaam , from Arabic salām , well-being, peace, from salima , to be safe, sound. 
 Islam , from Arabic ʾ islām , submission, from ʾ aslama , to surrender, resign oneself;
 Muslim , Mussulman , from Arabic muslim , one who surrenders, active participle of ʾ aslama (see above). Both a and b from Aramaic (Syriac) ʾ ašlem , to make peace, surrender, derived stem of šlem , to be whole.

 ‌ šlp 

West Semitic root, to precede, line up. Salafi , from Arabic salafī , of the forbears, of the predecessors, from salaf , forbear, predecessor. 
 ‌ šlṭ 

To dominate, rule, have power over. soldan , sultan , from Arabic sulṭān , power, authority, ruler, sultan, from Aramaic šulṭānā , power, authority, rule, ruler, from šəlaṭ , to dominate, rule, prevail;
```


## [2026-09-14T02:33:46.358Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; curl -s 'https://archive.org/metadata/originsofenglish0000ship' | python3 -c \"import json,sys; d=json.load(sys.stdin); print(d.get('server'), d.get('dir')); print([f['name'] for f in d.get('files',[]) if 'txt' in f['name'] or 'search' in f['name']][:10])\""
}
```


### [2026-09-14T02:33:49.318Z] TOOL RESULT

```
ia803209.us.archive.org /5/items/originsofenglish0000ship
['originsofenglish0000ship_djvu.txt', 'originsofenglish0000ship_hocr_searchtext.txt.gz']
```


## [2026-09-14T02:33:58.038Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; grep -n -i \"jerusalem\" data/verification/sources/web/75b739fc6c2698d2.txt | head -5; echo \"=== try OEW djvu ===\"; curl -s -o /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/oew459.txt -w \"%{http_code}\\n\" 'https://ia803209.us.archive.org/5/items/originsofenglish0000ship/originsofenglish0000ship_djvu.txt'; ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/oew459.txt"
}
```


### [2026-09-14T02:33:59.411Z] TOOL RESULT

```
=== try OEW djvu ===
403
-rw-rw-r-- 1 sfmqrb sfmqrb 4868 Sep 13 22:33 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/oew459.txt
```


## [2026-09-14T02:34:08.327Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== BQT سلام headword ===\"; grep -n \"سلام\" BQT_v3_pages.txt incoming/BQT/BQT_v3_pages.txt 2>/dev/null | head -8; echo \"=== ARY سلام/اورشلیم ===\"; grep -n \"سلام\\b\" incoming/ARY/ARY_pages.txt | head -5; echo \"=== ARY latin index salam ===\"; grep -n -i \"SALAM\\|SALAAM\" incoming/ARY/ARY_latin_index_pages.txt | head -5"
}
```


### [2026-09-14T02:34:08.422Z] TOOL RESULT

```
=== BQT سلام headword ===
1979:داثرة الممارف اسلام. کلمه‌مخون ‎(GUE opt) Shabatus‏ منطق‌بر ‎dye gl‏ فرنگی‌است:
3299:شجام ۴ - بنتح اولبروزنسلام ‎os‏
3433:‏وشیریزدان علی‌بن ابی‌طالب علیه السلام استگ‎
6796:‏ابنيةٌاسلامی وا‎
8888:وشیر بزدان علی بن‌ابی‌طالب علیه‌السلام ۴ است.
9470:حضرت موسی علیه‌السلام است.
9823:‏بدور لرکس مستت سلامت را دعا گفتيم .
10411:‎ged‏ هرد و کنابه ازجبرئیل علیه‌السلام است.
=== ARY سلام/اورشلیم ===
187:اسلامبولی و ترکی ترکمنی و آذری و غیره).
728:ساسانی و چند دهه‌ی اول و دوران اسلامی بود. در اثر آمیزش شمار زیادی از واژه‌های عربی (و بعداً ۱
3551:887 بسپار شبیه به نظر می‌رسد. در دوران پیش از اسلام عرب‌های عربستان دارای برج و بارو نبودند و می‌دانیم که
12920:چم این واژه در زبان‌فأَ) فرزی کهن و آلمانی و انگلیسی و هلندی: سلام کردن» خوش آمد گفتن.
=== ARY latin index salam ===
```


## [2026-09-14T02:34:09.544Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; curl -s \"https://api.archivelab.org/books/originsofenglish0000ship/searchinside?q=salang\" | head -c 800; echo; curl -s \"https://ia-fts.archive.org/api/v1/search/hits_inside?item_id=originsofenglish0000ship&q=salang\" | head -c 500"
}
```


### [2026-09-14T02:36:10.705Z] TOOL RESULT

```
Command did not complete within its 120s timeout and was moved to the background (ID: bvzazdpxd). Output is being written to: /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/tasks/bvzazdpxd.output. You will be notified when it completes. To check interim output, use Read on that file path.
Session cwd remains /home/sfmqrb/git/rishe; directory changes made by the backgrounded command do not apply to subsequent commands.
```


## [2026-09-14T02:36:16.801Z] TOOL CALL #55: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%B3%D9%84%D8%A7%D9%85/",
 "prompt": "Quote the فرهنگ معین (Mo'in) and لغت‌نامه دهخدا sections for سلام: the origin tag (e.g. [ع.]) and the definitions given. Reply in Persian script as printed."
}
```


## [2026-09-14T02:36:19.634Z] TOOL CALL #56: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%A7%D9%88%D8%B1%D8%B4%D9%84%DB%8C%D9%85/",
 "prompt": "Quote whatever the dictionaries (دهخدا، معین، فرهنگ فارسی) say about اورشلیم: its origin language (Hebrew/Syriac/Aramaic), meaning (\"شهر سلامتی/ مدینة السلام\"?), and the forms cited. Reply with the Persian text."
}
```


### [2026-09-14T02:36:24.392Z] TOOL RESULT

```
# سلام - معنی‌شناسی

## منابع اصلی

**لغت‌نامه دهخدا:**
"کلمه‌ی دعایی مأخوذ از تازی، به معنی بهی که در درود بر کسی گویند؛ یعنی سلامت و بی‌گزند باشید"

**فرهنگ معین:**
واژه‌ای عربی [ع.] با معانی: (۱) درود گفتن (۲) بی‌گزند شدن (۳) گردن نهادن

## تعریف‌های اساسی

سلام به عنوان یک تحیت، آرزوی سلامتی و تندرستی برای طرف مقابل است. این واژه در اسلام برای ایجاد صلح و امنیت میان مردم به کار می‌رود و از مستحبات مؤکد به شمار می‌آید.

## معادل‌های دیگر زبان‌ها

- **انگلیسی:** Hello, Hi, Peace
- **فارسی:** درود، نیک‌روز
- **اسپانیایی:** Hola
```


### [2026-09-14T02:36:25.979Z] TOOL RESULT

```
# اورشلیم - اطلاعات فرهنگ‌نامه‌ای

بر اساس محتوای دیکشنری آبادیس:

## منشأ و معنی

**لغت‌نامه دهخدا:** این منبع صرفاً به "قدس" ارجاع می‌دهد بدون تفصیل بیشتر.

**فرهنگ فارسی:** "اورشلیم" شهری است که "عرب آن را بیت المقدس می نامد" و این واژه به شهر مقدس اشاره دارد.

## ریشه‌شناسی

طبق بخش دانشنامه اسلامی، این نام از **دو جزء تشکیل شده:**

- **اور** (Ur): به معنای شهر و جایگاه
- **شلیم/سلیم**: به معنای سلام و سلامت

بنابراین ترجمه تقریبی: **"شهر سلام" یا "شهر سلامت"** - معادل عربی آن **"دار السلام"** است.

**منشأ زبان:** عبری و آرامی (یا سریانی)
```


## [2026-09-14T02:36:38.558Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for n in 436 438 440; do echo \"=== leaf $n ===\"; awk 'BEGIN{RS=\"\\f\"} NR=='$((n+1))' {print substr($0,1,150)}' KLN_1966.txt; done"
}
```


### [2026-09-14T02:36:39.831Z] TOOL RESULT

```
=== leaf 436 ===
  L.  inundans,  gen. -antis,  pres.  part,  of  inundare.  See  next  word and  -ant.
inundate,  tr.  v.,  to  flood;  to  overflow.  —  L.  in- un
=== leaf 438 ===
 —  ModL.,  fr.  Gk.  eEpeauovr),  ‘a wreath  of  olive  wound  round  with  wool’,  fr. slpo q,  ‘wool’,  which  is  rel.  to  gpiov,  ‘w
=== leaf 440 ===
te,  ‘to  anger’,  and -able.  Derivatives :  irritabl-y,  adv.,  irritabil-ity,  n. irritancy,  n. ,  the  state  of  being  irritating.  —  Fo
```


## [2026-09-14T02:36:41.451Z] TOOL CALL #58: Bash

```json
{
 "command": "cat /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/tasks/bvzazdpxd.output | head -c 600"
}
```


### [2026-09-14T02:36:41.507Z] TOOL RESULT

```
[exited with code 0]
```


## [2026-09-14T02:37:28.666Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; for u in 'https://www.etymonline.com/word/so%20long' 'https://en.wiktionary.org/wiki/so_long' 'https://en.wiktionary.org/wiki/selamat' 'https://en.wiktionary.org/wiki/Jerusalem' 'https://en.wiktionary.org/wiki/%D7%99%D7%A8%D7%95%D7%A9%D7%9C%D7%99%D7%9D' 'https://en.wiktionary.org/wiki/Salome' 'https://en.wiktionary.org/wiki/%D7%A9%D7%9C%D7%95%D7%9D' 'https://en.wiktionary.org/wiki/%D8%A5%D8%B3%D9%84%D8%A7%D9%85' 'https://abadis.ir/fatofa/%D8%A7%D9%88%D8%B1%D8%B4%D9%84%DB%8C%D9%85/' 'https://abadis.ir/fatofa/%D8%B3%D9%84%D8%A7%D9%85/'; do python3 tools/fetch_source.py \"$u\" --note 'page 459 root S.l.m verification' ; done"
}
```


### [2026-09-14T02:37:37.055Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/8c42ffe6e5716127.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/718130554ee4d8b7.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0837530d5ddb3426.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d0346ac75bbdfe90.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/32b1a20301d3ec05.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6dd647caf738ddd1.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9e8af088a321145a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d33b0487901b193a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3b54b5a6a7053b64.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1d9e9a4e53adaf49.txt
```


## [2026-09-14T02:37:39.038Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; echo \"=== etymonline so long ===\"; grep -n -i -A5 \"parting salutation\" 8c42ffe6e5716127.txt | head -40"
}
```


### [2026-09-14T02:37:39.095Z] TOOL RESULT

```
=== etymonline so long ===
25: parting salutation, 1860, of unknown origin, perhaps from a German idiom (compare German parting salutation adieu so lange , the full sense of which probably is something like "farewell, whilst (we're apart)"); or perhaps from or influenced by Hebrew shalom (via Yiddish sholom ). Some have noted a similarity to Scandinavian leave-taking phrases, such as Norwegian Adjø så lenge, Farvel så lenge, Mor'n så lenge , literally "bye so long, farewell so long, morning so long;" and Swedish Hej så länge "good-bye for now," with så länge "for now" attested since 1850 according to Swedish sources, with sense as in the German phrase. Etymology sources seem to lean toward the German origin. The adverbial so long "for such a long time" is from late Old English ( swa lange ); see so .
26-
27- Earlier guesses that it was a sailors' corruption of a South Pacific form of Arabic salaam are not now convincing. "Dictionary of American Slang" also adds to the list of candidates Irish slán "safe," said to be used as a salutation in parting.
28-
29- The phrase seems to have turned up simultaneously in America, Britain, and perhaps Canada, originally among lower classes. The first attested use is in title and text of the last poem in Whitman's "Leaves of Grass" in the 1860 edition.
30-
```


## [2026-09-14T02:37:53.669Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i \"^so.long\\|so-long,\" KLN_1966.txt | head -3; echo \"(klein so long: none above = absent)\"; echo \"=== Klein selamlik ===\"; grep -n -i \"^selamlik\" KLN_1966.txt | head -2"
}
```


### [2026-09-14T02:37:53.750Z] TOOL RESULT

```
(klein so long: none above = absent)
=== Klein selamlik ===
34483:selamlik,  n.,  the  men’s  quarters  in  a  Turkish house.  —  Turk,  seiamliq,  a  hybrid  coined  fr. Arab,  salam,  ‘peace’,  and  the  Turkish  suff.  -lik. See  salaam.
```


## [2026-09-14T02:38:15.640Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n '1,120p' tools/verify_check.py"
}
```


### [2026-09-14T02:38:15.683Z] TOOL RESULT

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


## [2026-09-14T02:38:30.380Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; mkdir -p data/verification/sources/refs/ocr/BOOK; cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg459.png data/verification/sources/refs/ocr/BOOK/459.png; python3 tools/fetch_source.py 'https://blog.oup.com/2018/03/the-origin-of-so-long/' --note 'page 459 node 5: Liberman on the origin of \"so long\" (Malay selamat / Hebrew shalom theories)'; ls -la data/verification/sources/refs/ocr/BOOK/459.png"
}
```


### [2026-09-14T02:38:32.205Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/5cf89d03149292e0.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 68729 Sep 13 22:38 data/verification/sources/refs/ocr/BOOK/459.png
```


## [2026-09-14T02:38:34.255Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; grep -n -i \"selamat\\|salang\\|Malay\" data/verification/sources/web/5cf89d03149292e0.txt | head -10"
}
```


### [2026-09-14T02:38:34.310Z] TOOL RESULT

```
216: Well, I will put forth my own irresponsible guess: that so long is a transformed shortening of the Malay formulas of parting, selamat tinggal au revoir’ (lit. ‘stay safe’, said by the one who is leaving) and selamat jalan ‘bon voyage’ (lit. ‘walk safe’, said by the one who remains behind). Etymologically, selamat < Arabic salāmāt , the plural of salām , and in Malay the literal meaning ‘peace’ is extended to ‘safety, security’. The stress on selamat is penultimate, agreeing with the final stress of so long , and the first vowel is schwa, again agreeing with the first vowel of so long , at least in my pronunciation. Most importantly, there is a plausible pathway: from Malay to Dutch to Afrikaans to English.
244: If we are forced to look to a loan translation as the source, Joachim Grzega (in a 2005 article in Onomasiology Online) has suggested Norwegian phrases such as “Adjø så lenge! Farvel så lenge! Mor’n så lenge!,” which he translates as “Bye so long! Farewell so long! Morning so long.!” And a native speaker tells me that there are very similar expressions in Swedish as well. Scandinavian sailors seem a more likely source than Arabs or Malays!
```


## [2026-09-14T02:43:23.800Z] TOOL CALL #65: Bash

```json
{
 "command": "python3 - <<'PYEOF'\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\nAHD_SEM = \"https://www.ahdictionary.com/word/semitic.html\"\nETYM_SL = \"https://www.etymonline.com/word/so%20long\"\nOUP = \"https://blog.oup.com/2018/03/the-origin-of-so-long/\"\nABADIS_SALAM = \"https://abadis.ir/fatofa/%D8%B3%D9%84%D8%A7%D9%85/\"\nABADIS_URS = \"https://abadis.ir/fatofa/%D8%A7%D9%88%D8%B1%D8%B4%D9%84%DB%8C%D9%85/\"\n\nKLN_SALAAM = (\"Klein 1966 s.v. 'salaam, salam': \\\"Arab. salam, 'peace; saluting, salutation', from the base of \"\n              \"salima, 'he was safe' ... rel. to Ethiop. salam, 'peace, welfare', Heb. shalam, 'he was intact, was at \"\n              \"peace, was in good health', shalom, 'completeness, welfare, peace'\\\" (KLN_1966.txt line 33518, OCR leaf 730 \"\n              \"= printed p. ~1430).\")\nKLN_SHALOM = (\"Klein 1966 s.v. 'shalom': \\\"Heb. shalom, 'peace', prop. 'completeness, soundness, welfare', from the stem of \"\n              \"shalam ... rel. to Aram. sh'lam, sh'lama, Arab. salima, 'he was safe', aslama, 'he surrendered, submitted', \"\n              \"salam, Ethiop. salam, Akkad. shalamu, 'to be complete, be safe', shulmu, 'welfare, peace'. Cp. Solomon and the \"\n              \"second element in Absalom, Jerusalem\\\" (KLN_1966.txt line 34869, OCR leaf 759 = printed p. ~1471).\")\nKLN_JERUS = (\"Klein 1966 s.v. 'Jerusalem': \\\"Gk. Ἰερουσαλήμ, fr. Heb. Y'rushalayim, lit. 'foundation of peace', fr. base of \"\n             \"yarah, 'he threw, cast', and shalom, 'peace'\\\" (KLN_1966.txt line 20245, OCR leaf 447; Klein vol. I ends at \"\n             \"p. 853 with the K words, so the J section is indeed at p. ~828 as Nourai cites).\")\n\ndata = {\n  \"pdf_page\": 459,\n  \"book_page\": 429,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-13\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"S.l.m, Š.l.m\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"Proto-Semitic root *š-l-m 'to be whole, sound, intact'; Common Semitic noun *šalām- 'well-being, welfare, peace'\",\n      \"note\": (\"The root box is right. AHD's Semitic-roots appendix (the modern successor of the list Nourai cites as \"\n               \"AHD:1541) gives 'šlm — To be whole, sound; Common Semitic noun *šalām-, well-being, welfare, peace', with \"\n               \"exactly the derivatives Nourai charts (shalom, Absalom, Solomon, Salome, salaam, Islam, Muslim). Nourai's \"\n               \"double heading 'S.l.m, Š.l.m' correctly records the regular Proto-Semitic *š > Arabic s split (Hebrew, \"\n               \"Aramaic, Ugaritic, Akkadian keep š-: šālōm, šəlāmā, šalāmu; Arabic has s-: salima, salām). His gloss 'to be \"\n               \"healthy and intact' matches 'be whole, sound' well. Two links in the tree are wrong, however, and both hang \"\n               \"directly off the root instead of off a daughter language: the 'Malaysian salang' → English 'so long' branch \"\n               \"(the Malay word for the greeting is selamat/salam, borrowed from Arabic, and the origin of 'so long' is in \"\n               \"fact unknown), and the 'Greek salômě: peace' box (Greek for 'peace' is eirēnē; Σαλώμη is only the Hellenised \"\n               \"Hebrew personal name). The Persian اورشلیم is also not French-mediated.\"),\n      \"note_fa\": (\"ریشهٔ سامی آغازین *š-l-m «تندرست و بی‌گزند بودن، تمام بودن» و نام‌واژهٔ مشترک سامی *šalām- «سلامت، \"\n                  \"آشتی». آنچه نورایی در جعبهٔ ریشه آورده درست است: پیوست ریشه‌های سامیِ فرهنگ AHD همین ریشه را با همین \"\n                  \"معنا و با همین مشتقات (shalom، Absalom، Solomon، Salome، salaam، Islam، Muslim) می‌آورد. دوگانه‌نویسی \"\n                  \"«S.l.m ، Š.l.m» نیز به‌جاست، زیرا š سامی آغازین در عربی به s بدل شده (salima) ولی در عبری و آرامی و \"\n                  \"اکدی همچنان š مانده است (šālōm، šəlāmā، šalāmu). با این حال سه شاخهٔ نمودار پذیرفتنی نیست: «مالایی \"\n                  \"salang»، «یونانی salômě به معنی صلح» و میانجی‌گری فرانسه برای «اورشلیم».\"),\n      \"sources\": [AHD_SEM, W + \"%D8%B3%D9%84%D8%A7%D9%85\", W + \"%D7%A9%D7%9C%D7%95%D7%9D\"],\n      \"ref_check\": [\n        {\"ref\": \"KLN:1430\", \"status\": \"supports\", \"note\": KLN_SALAAM + \" This is the page Nourai cites and it gives precisely the Semitic comparison (Arabic ~ Ethiopic ~ Hebrew ~ Akkadian) on which the root box rests.\"},\n        {\"ref\": \"AHD:1541\", \"status\": \"supports\", \"note\": (\"Nourai's 1976 AHD appendix page is not open online, but the current online AHD Semitic-roots appendix \"\n                                                            \"(ahdictionary.com/word/semitic.html) has: 'šlm — To be whole, sound; Common Semitic noun *šalām-, well-being, \"\n                                                            \"welfare, peace', listing shalom, Absalom, schlemiel, Solomon, Salome, salaam, Islam, Muslim/Mussulman. \"\n                                                            \"Same list, same gloss.\")}\n      ],\n      \"consulted\": [\n        {\"src\": \"KLN\", \"where\": \"p. ~1471 s.v. shalom; p. ~1430 s.v. salaam\", \"stance\": \"supports\", \"note\": KLN_SHALOM},\n        {\"src\": \"AHD\", \"where\": \"Semitic roots appendix, root šlm (online ed.)\", \"stance\": \"supports\", \"note\": \"'To be whole, sound; Common Semitic noun *šalām-, well-being, welfare, peace.'\"},\n        {\"src\": \"SKT\", \"where\": \"s.v. Moslem (SKT.txt line 11915)\", \"stance\": \"supports\", \"note\": \"\\\"The E. words moslem, mussulman, islam, and salaam are all from the same Arab. root salama, to submit.\\\"\"},\n        {\"src\": \"POK\", \"where\": \"—\", \"stance\": \"silent\", \"note\": \"Pokorny is an Indo-European dictionary; a Semitic root is out of its scope (checked: no *slm entry).\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Arabic\",\n          \"words\": \"salâm; taslîm; Islâm\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": (\"All three are regular derivatives of the Arabic triliteral س ل م (s-l-m), whose base verb is salima \"\n                         \"'he was safe, sound' (Proto-Semitic *š-l-m, with the regular Arabic *š > s). salām is the verbal noun \"\n                         \"'well-being, peace', used since pre-Islamic times as the greeting as-salāmu ʿalaykum; taslīm is the \"\n                         \"verbal noun of form II sallama 'to hand over, deliver up; to greet', hence both 'greeting' and \"\n                         \"'surrendering, handing over'; islām is the verbal noun of form IV ʾaslama 'he surrendered, resigned \"\n                         \"himself (to God)'. Klein and AHD both give exactly this. One refinement Nourai does not mention: \"\n                         \"Wiktionary (with citations) and the AHD Semitic appendix treat the religious senses of ʾaslama/islām/\"\n                         \"muslim as a semantic calque on Aramaic-Syriac ʾašlem 'to make peace, surrender', i.e. the theological \"\n                         \"meaning was shaped by Christian Aramaic usage even though the Arabic forms themselves are inherited.\"),\n          \"derivation_fa\": (\"هر سه واژه از ریشهٔ سه‌حرفی عربی «س‌ل‌م» ساخته شده‌اند که فعل پایهٔ آن سَلِمَ «بی‌گزند بود» است؛ این \"\n                            \"ریشه بازماندهٔ *š-l-m سامی آغازین است و š آن در عربی به s بدل شده. «سلام» مصدر/اسم‌مصدر به معنی \"\n                            \"«تندرستی، آشتی» است و از روزگار پیش از اسلام در درودِ «السلام علیکم» به کار می‌رفته؛ «تسلیم» مصدرِ \"\n                            \"باب تفعیل (سَلَّمَ) است و هم «درود گفتن» و هم «واگذاشتن» معنی می‌دهد؛ «اسلام» مصدرِ باب افعال \"\n                            \"(أَسْلَمَ «گردن نهاد») است. کلاین و AHD همین را می‌گویند. تنها نکتهٔ افزوده آنکه ویکی‌واژه و پیوست \"\n                            \"سامیِ AHD معنای دینیِ أسلم/إسلام/مسلم را گرته‌برداری معنایی از آرامی–سریانیِ ʾašlem «آشتی کردن، \"\n                            \"تسلیم شدن» می‌دانند. ادعای نورایی درست است.\"),\n          \"sources\": [W + \"%D8%B3%D9%84%D8%A7%D9%85\", W + \"%D8%A5%D8%B3%D9%84%D8%A7%D9%85\", AHD_SEM],\n          \"ref_check\": [\n            {\"ref\": \"KLN:1430\", \"status\": \"supports\", \"note\": KLN_SALAAM + \" Klein s.v. 'Islam' (line 19966) adds: \\\"Arab. islam, 'submitting oneself to God, surrender, obedience', infin. of aslama ... IV (= causative) conjugation of salima, 'he was safe'.\\\"\"},\n            {\"ref\": \"AHD:1541\", \"status\": \"supports\", \"note\": \"Online AHD Semitic appendix, root šlm: 'salaam, from Arabic salām, well-being, peace, from salima, to be safe, sound. Islam, from Arabic ʾislām, submission, from ʾaslama, to surrender, resign oneself.'\"},\n            {\"ref\": \"SAP:726\", \"status\": \"not_checked\", \"note\": \"Sayyah's Persian al-Munjid (Farhang-e Sayyah) is not digitised (refs_online: 'purchase', no copy found); could not open p. 726.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"s.v. salaam (p. ~1430), Islam (p. ~860), Moslem (p. ~1056)\", \"stance\": \"supports\", \"note\": \"\\\"Arab. muslim, 'a believer in Islam', lit. 'one who has submitted himself to God', part. of aslama ... IV (= causative) form of salama, 'he was safe'.\\\"\"},\n            {\"src\": \"LKT\", \"where\": \"no. 915, p. 74\", \"stance\": \"supports\", \"note\": \"Lokotsch: \\\"Ar. islām: Eigentlich Infin. des Vbs. salama IV 'sich unterwerfen', nämlich dem Willen Gottes, also 'Ergebung in Allahs Willen'.\\\"\"},\n            {\"src\": \"SKT\", \"where\": \"s.v. Salaam (SKT_dli_revised.txt line 67360)\", \"stance\": \"supports\", \"note\": \"\\\"Arab. salām, saluting, wishing peace; a salutation. — Arab. salām, saluting. + Heb. shālōm, peace, from shālam, to be safe.\\\"\"},\n            {\"src\": \"FVQ\", \"where\": \"grepped FVQ_pages.txt for islām/salām\", \"stance\": \"silent\", \"note\": \"Jeffery's Foreign Vocabulary of the Qur'an has no entry for سلام/إسلام — as expected, since he lists only loanwords and these are native Arabic formations.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"salâm «سلام»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": (\"New Persian سلام salām is a straightforward Arabic loan taken over with the Islamic conquest and the \"\n                         \"Arabic greeting formula; Wiktionary's Persian section says simply 'Borrowed from Arabic سَلَام (salām)', \"\n                         \"Dehkhoda calls it 'کلمه‌ی دعایی مأخوذ از تازی' ('a benedictive word taken from Arabic') and Mo'in tags it \"\n                         \"[ع.] (= Arabic). The same is true of every word in the box's extra line, all built on the same Arabic \"\n                         \"root: تسلیم taslīm (form II verbal noun), اسلام islām (form IV verbal noun), سالم sālem (active \"\n                         \"participle 'sound'), سلامت salāmat (abstract noun), سلیم salīm ('sound, unimpaired'), مُسلِم moslem and \"\n                         \"مُسَلَّم mosallam (participles of forms IV and II), سلمیٰ Salmā (a woman's name, used by Hāfez in the \"\n                         \"quoted verse), and سلیمان Soleymān — the last being a round trip, Hebrew Šəlōmōh → Arabic Sulaymān → \"\n                         \"Persian سلیمان (Klein s.v. Solomon: 'The Arabic PN.s Soliman, Suleiman derive fr. Heb. Shlomoh'). \"\n                         \"Phonetically nothing happens: Arabic /salām/ is kept intact in Persian, the only change being the \"\n                         \"Persian stress and the loss of the Arabic emphatic-free ā-quality.\"),\n          \"derivation_fa\": (\"«سلام» وام‌واژه‌ای عربی است که با ورود اسلام و صیغهٔ درودِ «السلام علیکم» به فارسی راه یافته است؛ \"\n                            \"دهخدا آن را «کلمهٔ دعایی مأخوذ از تازی» می‌خواند و معین آن را با نشانِ [ع.] می‌آورد و ویکی‌واژه نیز \"\n                            \"می‌نویسد «وام‌گرفته از عربی سَلَام». واژه بی هیچ دگرگونی آوایی به فارسی آمده است. دیگر واژه‌های همین \"\n                            \"جعبه نیز همگی از همین ریشهٔ عربی‌اند: تسلیم (مصدر باب تفعیل)، اسلام (مصدر باب افعال)، سالم (اسم \"\n                            \"فاعل)، سلامت، سلیم، مُسلِم و مُسَلَّم، و سلمیٰ که نام زنانه است و حافظ در بیت نقل‌شده آورده. «سلیمان» \"\n                            \"نمونهٔ یک رفت‌وبرگشت است: عبریِ Šəlōmōh ← عربیِ سُلَیمان ← فارسیِ سلیمان. ادعای نورایی درست است.\"),\n          \"sources\": [W + \"%D8%B3%D9%84%D8%A7%D9%85\", ABADIS_SALAM],\n          \"ref_check\": [\n            {\"ref\": \"MON\", \"status\": \"supports\", \"note\": \"Mo'in via abadis.ir (فرهنگ معین section for سلام): tagged [ع.] with the senses '۱. درود گفتن ۲. بی‌گزند شدن ۳. گردن نهادن' — i.e. Arabic origin, exactly Nourai's arrow. (Nourai gives no volume/page, so the dictionary entry itself was checked.)\"},\n            {\"ref\": \"FVA:196\", \"status\": \"not_checked\", \"note\": \"Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi has no digital copy anywhere (refs_online: 'catalog', searched archive.org/ketabnak/noorlib).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"abadis.ir فرهنگ معین s.v. سلام\", \"stance\": \"supports\", \"note\": \"'[ع.] (اِمص.) ۱. درود گفتن ۲. بی‌گزند شدن' — the [ع.] tag marks it as an Arabic loan.\"},\n            {\"src\": \"BQT\", \"where\": \"grepped BQT_v3_pages.txt for سلام\", \"stance\": \"silent\", \"note\": \"Borhan-e Qate' has no headword سلام (it is a dictionary of Persian, and Mo'in's footnotes do not treat this common Arabic loan); the hits are only inside other entries (e.g. 'علیه‌السلام').\"},\n            {\"src\": \"ARY\", \"where\": \"grepped ARY_pages.txt / ARY_latin_index_pages.txt\", \"stance\": \"silent\", \"note\": \"Aryanpur's Indo-European roots dictionary has no سلام entry — expected, since the word is Semitic, not Indo-European.\"},\n            {\"src\": \"KLN\", \"where\": \"s.v. Solomon (p. ~1476)\", \"stance\": \"supports\", \"note\": \"For سلیمان in the extra line: \\\"Gk. Σολομών, also Σαλομών, fr. Heb. Sh'lomoh ... The Arabic PN.s Soliman, Suleiman derive fr. Heb. Sh'lomoh.\\\"\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"English\",\n          \"words\": \"Islam, Moslem\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": (\"English Islam is a direct learned borrowing of Arabic إسلام ʾislām, first recorded in English in 1818 \"\n                         \"(earlier writers used 'Islamism', 'Mahometanism'); Moslem is Arabic مسلم muslim, the form-IV active \"\n                         \"participle of ʾaslama, borrowed through Ottoman Turkish müslim/müslüman and the older European \"\n                         \"Mussulman, and attested in English from 1615. Klein s.v. Moslem: 'Arab. muslim, \\\"a believer in \"\n                         \"Islam\\\", lit. \\\"one who has submitted himself to God\\\", part. of aslama'. Lokotsch no. 915 traces the \"\n                         \"same word into German, English, French, Italian and Russian. The arrow Arabic → English is thus exactly \"\n                         \"right; the only nuance is that the immediate transmitters into western European languages were often \"\n                         \"Turkish and Persian usage rather than Arabic directly.\"),\n          \"derivation_fa\": (\"واژه‌های انگلیسیِ Islam و Moslem وام‌واژه‌های مستقیم از عربی‌اند: Islam از «إسلام» (نخستین کاربرد \"\n                            \"انگلیسی ۱۸۱۸م) و Moslem از «مُسلِم»، اسم فاعل باب افعال، که از راه ترکی عثمانی و صورت کهن‌ترِ \"\n                            \"Mussulman از سدهٔ ۱۷م وارد انگلیسی شده است. کلاین و لوکوچ (شمارهٔ ۹۱۵) همین مسیر را می‌دهند. \"\n                            \"ادعای نورایی درست است؛ تنها باید افزود که میانجیِ عملی در بسیاری از زبان‌های اروپایی، ترکی و فارسی \"\n                            \"بوده است، نه همیشه عربیِ بی‌واسطه.\"),\n          \"sources\": [AHD_SEM, W + \"%D8%A5%D8%B3%D9%84%D8%A7%D9%85\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Online AHD Semitic appendix, root šlm: 'Islam, from Arabic ʾislām, submission, from ʾaslama, to surrender, resign oneself; Muslim, Mussulman, from Arabic muslim, one who surrenders, active participle of ʾaslama.' (Nourai gives no page for this node.)\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"s.v. Islam (line 19966) and Moslem (line 24476)\", \"stance\": \"supports\", \"note\": \"\\\"Moslem, n., a Mohammedan. — Arab. muslim ... part. of aslama, 'he surrendered, submitted', IV (= causative) form of salama, 'he was safe'. See salaam and cp. Islam.\\\"\"},\n            {\"src\": \"LKT\", \"where\": \"no. 915, p. 74\", \"stance\": \"supports\", \"note\": \"\\\"Es ist der Name für die Religion Muhammads geworden: dtsch. Islam, engl. islam, islamism; frz. islam, islamisme, it. islamismo; russ. islam.\\\"\"},\n            {\"src\": \"SKT\", \"where\": \"s.v. Moslem (SKT.txt line 11915)\", \"stance\": \"supports\", \"note\": \"\\\"Arab. moslim, 'a musulman, a true believer in the Mohammedan faith' ... A mussulman is one who professes islām, i.e. submission to the will of God.\\\"\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Malaysian\",\n          \"words\": \"salang\",\n          \"verdict\": \"transcription_suspect\",\n          \"error_in\": \"book\",\n          \"book_prints\": \"salang\",\n          \"correct_form\": \"selamat (also salam)\",\n          \"derivation\": (\"The printed page really does read 'salang : peace, greetings, fare well' (see the page image), so the \"\n                         \"extraction is faithful and the error is Nourai's own. Malay/Indonesian salang does exist but means \"\n                         \"something quite different — 'execution by driving a keris through the collarbone into the heart' (verb \"\n                         \"'to execute by the keris'); Brunei Malay salang is 'resin'. The Malay word for a greeting/farewell is \"\n                         \"selamat, borrowed from Arabic سلامات salāmāt (plural of salām), used in selamat jalan 'go safely', \"\n                         \"selamat tinggal 'stay safely', selamat pagi 'good morning'; the bare loan salam also exists. So the box \"\n                         \"should read selamat/salam, and it should hang from the Arabic node (#1), not straight off the Semitic \"\n                         \"root — Malay is Austronesian and has the word only as an Islamic-era loan (13th-16th c., through the \"\n                         \"Muslim trading network of the Straits).\"),\n          \"derivation_fa\": (\"در صفحهٔ چاپی نیز همان «salang» آمده است، پس خطا از خوانشِ اسکن نیست بلکه خطای خودِ کتاب است. واژهٔ \"\n                            \"مالاییِ salang هست، اما معنایش «کشتن با خنجر کریس از استخوان ترقوه تا قلب» است، نه «درود». واژه‌ای \"\n                            \"که نورایی در نظر داشته selamat است، وام‌واژه‌ای از عربیِ «سلامات» (جمع سلام)، در ترکیب‌هایی چون \"\n                            \"selamat jalan و selamat pagi؛ صورت کوتاهِ salam نیز در مالایی هست. افزون بر این، این جعبه باید \"\n                            \"زیرشاخهٔ عربی (#۱) باشد نه زیرشاخهٔ مستقیمِ ریشهٔ سامی، زیرا مالایی زبانی آسترونزیایی است و این واژه \"\n                            \"را تنها پس از گسترش اسلام (سده‌های ۷–۱۰ ق) وام گرفته است.\"),\n          \"sources\": [W + \"salang\", W + \"selamat\", OUP],\n          \"ref_check\": [\n            {\"ref\": \"OEW:451\", \"status\": \"not_checked\", \"note\": \"Shipley, The Origins of English Words (1984) is lending-only on archive.org; djvu.txt returns HTTP 403 and the search-inside API returns nothing for either copy (originsofenglish00jose, originsofenglish0000ship). Page 451 could not be opened.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/salang\", \"stance\": \"contradicts\", \"note\": \"Malay salang: 'a method of execution where a keris is impaled through the collarbone and into the heart'; verb 'to execute by the keris'. No sense 'peace, greeting, farewell' in any of the listed languages (Brunei Malay 'resin', Central Bikol 'jaw', Kavalan 'soup', Tagalog senses).\"},\n            {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/selamat\", \"stance\": \"partial\", \"note\": \"Malay selamat: 'Borrowed from Arabic سَلَامَة (salāma)'; Indonesian: 'from Arabic سَلَامَات (salāmāt), plural of سَلَام (salām)' — this is the word Nourai wanted, and it comes from Arabic, not straight from the Semitic root.\"},\n            {\"src\": \"LKT\", \"where\": \"Einleitung p. 2 and no. 915\", \"stance\": \"partial\", \"note\": \"Lokotsch notes Malay as one of the source languages of orientalisms but registers no Malay salang; his islām entry (no. 915) lists no Malay descendant.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"English\",\n          \"words\": \"so long\",\n          \"verdict\": \"disputed\",\n          \"derivation\": (\"The chart presents 'so long' as a documented borrowing of a Malay greeting; modern authorities say its \"\n                         \"origin is unknown. Etymonline: 'parting salutation, 1860, of unknown origin, perhaps from a German \"\n                         \"idiom (compare German parting salutation adieu so lange) ... or perhaps from or influenced by Hebrew \"\n                         \"shalom (via Yiddish sholom)', with Norwegian adjø så lenge and Swedish hej så länge as further \"\n                         \"candidates, and explicitly: 'Earlier guesses that it was a sailors\\\\' corruption of a South Pacific form \"\n                         \"of Arabic salaam are not now convincing.' Wiktionary likewise says 'Uncertain. Compare Swedish hej så \"\n                         \"länge'. The Malay route Nourai follows is precisely one of those rejected guesses; A. Liberman (OUP \"\n                         \"blog 2018) floats selamat tinggal / selamat jalan as his own 'irresponsible guess' and then concludes \"\n                         \"'Scandinavian sailors seem a more likely source than Arabs or Malays'. Nourai's NOTE ('started as a \"\n                         \"colloquial among British soldiers') is also wrong on the record: the first attestation is the title and \"\n                         \"text of the last poem of the 1860 edition of Whitman's Leaves of Grass, and the phrase surfaced \"\n                         \"simultaneously in America and Britain among the lower classes, not in the army.\"),\n          \"derivation_fa\": (\"نورایی «so long» را وام‌گیریِ روشنِ یک درودِ مالایی می‌داند، اما ریشه‌شناسیِ امروزی آن را ناشناخته \"\n                            \"می‌شمارد. اتیمانلاین می‌نویسد: «درودِ جدایی، ۱۸۶۰م، با خاستگاه ناشناخته؛ شاید از اصطلاح آلمانیِ \"\n                            \"adieu so lange یا به تأثیر عبریِ shalom از راه ییدیش»، و صریحاً می‌افزاید که «گمان‌های پیشین مبنی بر \"\n                            \"تحریف ملوانانهٔ صورتی از سلامِ عربی امروز پذیرفتنی نیست». صورت‌های اسکاندیناویاییِ hej så länge و \"\n                            \"adjø så lenge محتمل‌ترین الگو دانسته می‌شوند. یادداشتِ کتاب («آغاز آن گفتار عامیانهٔ سربازان \"\n                            \"بریتانیایی بوده») نیز درست نیست: کهن‌ترین کاربرد در آخرین شعر چاپ ۱۸۶۰ «برگ‌های علف» والت ویتمن \"\n                            \"است. پژوهش امروزی ادعای نورایی را رد می‌کند.\"),\n          \"sources\": [ETYM_SL, W + \"so_long\", OUP],\n          \"ref_check\": [\n            {\"ref\": \"OEW:451\", \"status\": \"not_checked\", \"note\": \"Shipley 1984 is lending-only; djvu.txt 403, search-inside API empty for both IA copies. Nourai's claim is presumably Shipley's, but p. 451 could not be read.\"},\n            {\"ref\": \"FSD:2316\", \"status\": \"not_found\", \"note\": \"Funk & Wagnalls New Standard vol. 4: the entry 'so' (FSD_vol4.txt line 14071, leaf ~163) carries the cross-reference '— so long, see SO-LONG', so the headword exists; p. 2316 falls exactly in the sol-/Solomon stretch (leaf 170 = soleship/solar, leaf 171 = Solomon's-seal) where 'so-long' would be printed, but the OCR of that page has lost the entry, so its etymology could not be read.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/so long\", \"stance\": \"contradicts\", \"note\": \"\\\"Earlier guesses that it was a sailors' corruption of a South Pacific form of Arabic salaam are not now convincing.\\\" First attested 1860 (Whitman).\"},\n            {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/so_long\", \"stance\": \"contradicts\", \"note\": \"\\\"Uncertain. Compare to Swedish hej så länge and Russian пока.\\\" — no Malay/Arabic derivation.\"},\n            {\"src\": \"KLN\", \"where\": \"grepped KLN_1966.txt for 'so long' / 'so-long'\", \"stance\": \"silent\", \"note\": \"Klein has no entry for the phrase (he does have selamlik 'Turk. selamliq ... fr. Arab. salam'), so he offers no support for the Semitic route.\"},\n            {\"src\": \"FSD\", \"where\": \"vol. 4, entry 'so' (leaf ~163 ≈ p. 2309)\", \"stance\": \"partial\", \"note\": \"\\\"— so long, see SO-LONG\\\" confirms the dictionary has the headword Nourai cites, but the OCR of p. 2316 is illegible at that point.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Hebrew\",\n          \"words\": \"šalôm; yrrŭ-šâlôm; Ab-šalôm\",\n          \"verdict\": \"transcription_suspect\",\n          \"error_in\": \"book\",\n          \"book_prints\": \"yrrŭ-šâlôm\",\n          \"correct_form\": \"yərū-šālēm / Yərūšālayim\",\n          \"derivation\": (\"Word 1, šālôm 'peace, completeness, welfare', is confirmed: Klein s.v. shalom derives it from the stem \"\n                         \"of šālam 'he was intact, was complete, was in good health', cognate with Aramaic šəlām(ā), Arabic \"\n                         \"salima/salām, Akkadian šalāmu/šulmu; AHD's Semitic appendix reconstructs Common Semitic *šalām-. \"\n                         \"Word 3, Ab-šālôm, is confirmed: Klein s.v. Absalom, 'Heb. Abhshalom, lit. \\\"father is peace\\\", fr. abh, \"\n                         \"\\\"father\\\", and shalom, \\\"peace\\\"'; AHD gives 'ʾabšālōm, my father (is) peace', a shortening of \"\n                         \"ʾăbîšālōm. Word 2 is the problem. The book prints 'yrrŭ-šâlôm' (confirmed on the page image), which is \"\n                         \"no Hebrew form: the name is יְרוּשָׁלַיִם Yərūšālayim, older/poetic יְרוּשָׁלֵם Yərūšālēm, and Nourai's \"\n                         \"string looks like a typesetting corruption of 'y'rū-šālēm'. The extraction copied the page faithfully, \"\n                         \"so this is the author's misprint. The gloss is also only half right: Nourai's own cross-reference \"\n                         \"☞Yârâh in fact points to the correct analysis (Klein: 'fr. base of yarah, \\\"he threw, cast\\\", and \"\n                         \"shalom' = 'foundation of peace'), and today's standard account, reflected in Wiktionary, is 'yarú, he \"\n                         \"lays down' + Šālēm, the Canaanite god Shalem — i.e. 'foundation of (the god) Shalem', supported by the \"\n                         \"14th-c. BCE Amarna/Akkadian Urušalim; 'city of peace' (and the midrashic yirʾé + šālôm) is labelled a \"\n                         \"popular etymology.\"),\n          \"derivation_fa\": (\"واژهٔ نخست، šālôm «آشتی، تندرستی، تمامیت»، درست است؛ کلاین آن را از ستاک šālam «بی‌گزند و تمام \"\n                            \"بود» می‌گیرد و با آرامیِ šəlāmā، عربیِ سَلِمَ/سلام و اکدیِ šalāmu هم‌ریشه می‌داند. واژهٔ سوم، \"\n                            \"Ab-šālôm «پدر آشتی است»، نیز درست است. اما واژهٔ دوم خطای چاپی کتاب است: صفحهٔ چاپی «yrrŭ-šâlôm» \"\n                            \"دارد که صورتی ناممکن در عبری است؛ نام درست יְרוּשָׁלַיִם Yərūšālayim و صورت کهن‌ترِ Yərūšālēm است. \"\n                            \"معنای «شهر سلام» نیز ریشه‌شناسی عامیانه است: تحلیل پذیرفتهٔ امروزی «yarú (بنا نهاد) + شالیم (نام \"\n                            \"ایزد کنعانی)» یعنی «بنیادنهادهٔ شالیم» است و صورت اکدیِ Urušalim در الواح العمارنه (سدهٔ ۱۴ پ.م) \"\n                            \"آن را تأیید می‌کند؛ خودِ نورایی نیز با ارجاع ☞Yârâh به همین تحلیل اشاره کرده است.\"),\n          \"sources\": [W + \"%D7%A9%D7%9C%D7%95%D7%9D\", W + \"%D7%99%D7%A8%D7%95%D7%A9%D7%9C%D7%99%D7%9D\", AHD_SEM],\n          \"ref_check\": [\n            {\"ref\": \"KLN:828\", \"status\": \"supports\", \"note\": KLN_JERUS + \" Klein's 'foundation of peace' (not 'city of peace') is what Nourai's ☞Yârâh cross-reference encodes.\"},\n            {\"ref\": \"KLN:1430\", \"status\": \"supports\", \"note\": KLN_SALAAM},\n            {\"ref\": \"KLN:1471\", \"status\": \"supports\", \"note\": KLN_SHALOM},\n            {\"ref\": \"AHD:1541\", \"status\": \"partial\", \"note\": \"Online AHD Semitic appendix, root šlm: 'shalom ... from Hebrew šālōm, well-being, peace, from šālēm, to be safe, sound'; 'Absalom, from Hebrew ʾabšālōm, my father (is) peace'. Jerusalem is NOT listed under šlm in the appendix — AHD does not endorse the 'city/foundation of peace' analysis.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"s.v. shalom (p. ~1471), Absalom (p. ~4), Jerusalem (p. ~828)\", \"stance\": \"supports\", \"note\": \"\\\"Absalom ... Heb. Abhshalom, lit. 'father is peace', fr. abh, 'father', and shalom, 'peace'.\\\"\"},\n            {\"src\": \"AHD\", \"where\": \"Semitic appendix root šlm\", \"stance\": \"partial\", \"note\": \"Confirms šālōm and ʾabšālōm; silent on Jerusalem.\"},\n            {\"src\": \"Wiktionary\", \"where\": \"ירושלים\", \"stance\": \"contradicts\", \"note\": \"\\\"Possibly of ultimate origin יָרוּ (yarú, 'he lays down') + שָׁלֵם (Shalém, 'the Canaanite god Shalem')\\\"; the 'peace' reading is given as the \\\"Popular etymological explanation\\\"; 'Akin to Akkadian 𒌑𒊒𒊓𒅆𒆠 (Urušalim)'.\"},\n            {\"src\": \"SKT\", \"where\": \"s.v. Salaam\", \"stance\": \"supports\", \"note\": \"\\\"+ Heb. shālōm, peace, from shālam, to be safe.\\\"\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"French\",\n          \"words\": \"\",\n          \"verdict\": \"disputed\",\n          \"derivation\": (\"An empty pass-through box (the printed page shows the header 'French' with no word and no reference — \"\n                         \"the extraction is faithful), inserted only to route Hebrew šālôm to Persian اورشلیم. The route is wrong. \"\n                         \"French Jérusalem (Old French Jherusalem, from Late Latin Ierusalem/Hierusalem, from Greek Ἰερουσαλήμ) \"\n                         \"could only have yielded a Persian *ژروزالم; it cannot produce Uršalīm, which preserves the Semitic \"\n                         \"consonant frame ʾ-r-š-l-m. Persian اورشلیم comes from the Syriac/Aramaic form ʾŪrišlem and its Arabic \"\n                         \"reflex أُورَشَلِيم, the form used by eastern Christians and taken over in the Persian Bible translations; \"\n                         \"abadis/encyclopaedic sources give the origin as 'عبری و آرامی (یا سریانی)'. No intermediary French stage \"\n                         \"is documented.\"),\n          \"derivation_fa\": (\"این جعبه تهی است (در صفحهٔ چاپی نیز فقط عنوان «French» بدون واژه و بدون مأخذ آمده، پس خطای خوانش \"\n                            \"نیست) و تنها برای رساندنِ šālôm عبری به «اورشلیم» فارسی گذاشته شده است. این مسیر نادرست است: \"\n                            \"Jérusalem فرانسوی (از فرانسویِ کهن Jherusalem، از لاتینِ متأخر Ierusalem، از یونانیِ Ἰερουσαλήμ) \"\n                            \"هرگز نمی‌توانست «اورشلیم» بدهد. صورت فارسی از سریانیِ ʾŪrišlem و معرّبِ آن «أُورَشَلِيم» گرفته شده \"\n                            \"که صورتِ رایج نزد مسیحیان شرقی و در ترجمه‌های فارسیِ کتاب مقدس است. پژوهش امروزی میانجیِ فرانسه را \"\n                            \"رد می‌کند.\"),\n          \"sources\": [W + \"Jerusalem\", ABADIS_URS],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai cites no reference for this box (the page image confirms the header carries no book icon), so there is nothing to check; the claim is unsupported in his own apparatus.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/Jerusalem\", \"stance\": \"partial\", \"note\": \"\\\"From Old English Hierusalem or Old French Jherusalem or Late Latin Ierusalem, Hierusalem, from Latin Hierosolyma, from Ancient Greek Ἰερουσαλήμ, from Biblical Hebrew יְרוּשָׁלַיִם\\\" — French is a link in the ENGLISH chain, not in a Persian one.\"},\n            {\"src\": \"MON\", \"where\": \"abadis.ir s.v. اورشلیم (دهخدا/فرهنگ فارسی)\", \"stance\": \"contradicts\", \"note\": \"Persian dictionaries give the origin as Hebrew/Aramaic-Syriac ('عبری و آرامی (یا سریانی)'), analysed اور 'city' + شلیم 'peace'; no French intermediary.\"},\n            {\"src\": \"KLN\", \"where\": \"s.v. Jerusalem (p. ~828)\", \"stance\": \"partial\", \"note\": \"Klein routes the name Hebrew → Greek → (Latin) → European languages; he mentions no French source for any oriental form.\"}\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"Persian\",\n          \"words\": \"Űršalîm «اورشلیم»\",\n          \"verdict\": \"disputed\",\n          \"derivation\": (\"The Persian word is real — اورشلیم Uršalīm is the standard Persian name of Jerusalem beside عربized \"\n                         \"بیت‌المقدس/قدس, and it does ultimately belong to this root — but not by the route drawn. It reflects \"\n                         \"Syriac ʾŪrišlem / Aramaic Yərūšlem, taken into Arabic as أُورَشَلِيم and into Persian through Christian \"\n                         \"Arabic and Syriac usage (and, in its modern currency, through the 19th-century Persian Bible \"\n                         \"translations); Dehkhoda simply refers اورشلیم to قدس, and the encyclopaedic note in abadis analyses it \"\n                         \"as اور 'city, place' + شلیم/سلیم 'peace, safety', 'شهر سلام', equating it with Arabic دار السلام. The \"\n                         \"initial ū- (Ur-) is the Aramaic/Syriac prosthetic treatment of the first syllable, exactly as in \"\n                         \"Akkadian Urušalim of the Amarna letters; a French Jérusalem could not produce it. Verdict: the word and \"\n                         \"its gloss are right, the parent (#7 French) is wrong, so the edge as drawn is rejected.\"),\n          \"derivation_fa\": (\"«اورشلیم» واژه‌ای راستین در فارسی است و در نهایت به همین ریشهٔ سامی بازمی‌گردد، اما نه از راهی که \"\n                            \"نمودار نشان می‌دهد. این صورت بازتابِ سریانیِ ʾŪrišlem / آرامیِ Yərūšlem است که به عربی «أُورَشَلِيم» \"\n                            \"شده و از راه کاربرد مسیحیانِ عرب و سریانی، و در دورهٔ نو از راه ترجمه‌های فارسیِ کتاب مقدس (سدهٔ \"\n                            \"۱۹م) در فارسی جا افتاده است. دهخدا آن را به «قدس» ارجاع می‌دهد و منابع فارسی آن را «اور (شهر) + \"\n                            \"شلیم (سلام)» یعنی «شهر سلام» و برابرِ «دار السلام» می‌دانند. آغازهٔ اور- همان صورت آرامی–اکدی \"\n                            \"(Urušalim در الواح العمارنه) است و از Jérusalem فرانسوی به دست نمی‌آید؛ پس پیوندِ رسم‌شده پذیرفتنی \"\n                            \"نیست، هرچند خودِ واژه درست است.\"),\n          \"sources\": [ABADIS_URS, W + \"%D7%99%D7%A8%D7%95%D7%A9%D7%9C%D7%99%D7%9D\", W + \"Jerusalem\"],\n          \"ref_check\": [\n            {\"ref\": \"MON5:195\", \"status\": \"not_checked\", \"note\": \"Mo'in vol. 5 (اعلام / proper names) is not in the local library and is not on vajehyab/abadis (only the lexicon volumes are); refs_online has no MON5 entry. The Dehkhoda/Farhang-e Farsi text for اورشلیم was read instead via abadis.ir.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"abadis.ir s.v. اورشلیم (لغت‌نامه دهخدا + فرهنگ فارسی)\", \"stance\": \"partial\", \"note\": \"'اورشلیم ... عرب آن را بیت المقدس می‌نامد'; origin 'عبری و آرامی (یا سریانی)', analysed اور 'شهر' + شلیم 'سلام' = 'شهر سلام' — supports the Semitic origin and the gloss, contradicts the French parent.\"},\n            {\"src\": \"KLN\", \"where\": \"s.v. Jerusalem (p. ~828)\", \"stance\": \"partial\", \"note\": \"\\\"Gk. Ἰερουσαλήμ, fr. Heb. Y'rushalayim, lit. 'foundation of peace'\\\" — the Hebrew source is confirmed, the transmission to Persian is not Klein's subject.\"},\n            {\"src\": \"BQT\", \"where\": \"grepped BQT volumes for اورشلیم\", \"stance\": \"silent\", \"note\": \"Borhan-e Qate' has no entry for اورشلیم (it is not a Persian common noun), and Mo'in's footnotes therefore say nothing.\"}\n          ]\n        },\n        {\n          \"id\": 9,\n          \"lang\": \"English\",\n          \"words\": \"šalom, Jerusalem, Absalom, Solomon\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": (\"All four English words go back to the Hebrew branch, as drawn, though two of them travelled through \"\n                         \"Greek and Latin rather than being taken from Hebrew directly. shalom is a direct modern borrowing of \"\n                         \"Hebrew šālôm as the Jewish greeting (Klein s.v. shalom). Jerusalem: Hebrew Yərūšālayim → Greek \"\n                         \"Ἰερουσαλήμ (Septuagint/NT) → Late Latin Ierusalem/Hierusalem (and Latin Hierosolyma) → Old French \"\n                         \"Jherusalem / Old English Hierusalem → Middle English Jerusalem. Absalom: Hebrew ʾAbšālōm 'father is \"\n                         \"peace' → Greek Ἀβεσσαλώμ → Latin → English, as the biblical name of David's son. Solomon: Hebrew \"\n                         \"Šəlōmōh 'his (God's) peace' → Greek Σολομών/Σαλομών → Latin Solomon → English (Klein s.v. Solomon; AHD \"\n                         \"Semitic appendix s.v. šlm).\"),\n          \"derivation_fa\": (\"هر چهار واژهٔ انگلیسی به شاخهٔ عبری بازمی‌گردند، چنان‌که نمودار نشان می‌دهد، هرچند دو تای آن‌ها از \"\n                            \"راه یونانی و لاتین رسیده‌اند: shalom وام‌گیریِ مستقیمِ نو از عبریِ šālôm است؛ Jerusalem از عبریِ \"\n                            \"Yərūšālayim به یونانیِ Ἰερουσαλήμ (ترجمهٔ سبعینیه و عهد جدید)، سپس لاتینِ متأخر Ierusalem و \"\n                            \"فرانسویِ کهن Jherusalem و انگلیسیِ کهن Hierusalem؛ Absalom از عبریِ ʾAbšālōm «پدر آشتی است»؛ و \"\n                            \"Solomon از عبریِ Šəlōmōh «آشتیِ او (خدا)» از راه یونانیِ Σολομών و لاتین. کلاین و AHD همین را \"\n                            \"می‌گویند؛ ادعای نورایی درست است.\"),\n          \"sources\": [W + \"Jerusalem\", AHD_SEM, W + \"%D7%A9%D7%9C%D7%95%D7%9D\"],\n          \"ref_check\": [\n            {\"ref\": \"KLN:828\", \"status\": \"supports\", \"note\": KLN_JERUS + \" Klein also has Absalom (p. ~4) and Solomon (p. ~1476) with the same Hebrew sources, and shalom at p. ~1471.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"s.vv. shalom, Jerusalem, Absalom, Solomon\", \"stance\": \"supports\", \"note\": \"\\\"Solomon ... Gk. Σολομών, also Σαλομών, fr. Heb. Sh'lomoh, which is rel. to shalom, 'peace'. See shalom and cp. Salome.\\\"\"},\n            {\"src\": \"AHD\", \"where\": \"Semitic appendix root šlm\", \"stance\": \"supports\", \"note\": \"'Solomon, from Hebrew šəlōmōh, his (God's) peace, from šəlōm, bound form of šālôm'; 'Absalom, from Hebrew ʾabšālōm, my father (is) peace'; 'shalom ... from Hebrew šālōm'.\"},\n            {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/Jerusalem\", \"stance\": \"supports\", \"note\": \"\\\"From Old English Hierusalem or Old French Jherusalem or Late Latin Ierusalem ... from Ancient Greek Ἰερουσαλήμ, from Biblical Hebrew יְרוּשָׁלַיִם.\\\"\"}\n          ]\n        },\n        {\n          \"id\": 10,\n          \"lang\": \"Greek\",\n          \"words\": \"salômě; Salome\",\n          \"verdict\": \"disputed\",\n          \"derivation\": (\"The second word is right, the first is not, and the parent is wrong. Greek has no common noun σαλώμη \"\n                         \"'peace' — the Greek word for peace is εἰρήνη (eirēnē); Σαλώμη is only a personal name, the Hellenised \"\n                         \"form of a Hebrew name of the Second-Temple period (Klein: 'Late L., fr. Gk. Σαλώμη, which is rel. to \"\n                         \"Σαλωμών, \\\"Solomon\\\"'; AHD: 'Salome, from a Hebrew personal name akin to šəlōmît, Shelomith (biblical \"\n                         \"name), from šālôm'; Wiktionary: 'From Ancient Greek Σαλώμη, from Hebrew שְׁלוֹמִית (sh'lomít)'). Greek \"\n                         \"borrowed it not from the Semitic root at large but from Hebrew/Aramaic in the Hellenistic period, \"\n                         \"through the Jewish onomasticon of Palestine (the name is borne by Herod's sister and by the women at \"\n                         \"the tomb in Mark 15:40), so the box should hang from the Hebrew node #6, not from the root. The -ω- \"\n                         \"of Σαλώμη renders the Hebrew ō of šālôm and the ending -η is the Greek feminine adaptation.\"),\n          \"derivation_fa\": (\"واژهٔ دوم درست است و واژهٔ نخست نادرست، و پیوندِ پدر نیز جای دیگری باید باشد. در یونانی هیچ اسم عامِ \"\n                            \"σαλώμη به معنی «صلح» وجود ندارد؛ واژهٔ یونانی برای صلح εἰρήνη است و Σαλώμη تنها نامی خاص است، \"\n                            \"صورت یونانی‌شدهٔ نامی عبری از دورهٔ معبد دوم (کلاین: «از یونانیِ Σαλώμη، هم‌ریشه با Σαλωμών \"\n                            \"‘سلیمان’»؛ AHD: «از نامی عبری همانند šəlōmît»). یونانی این نام را در دورهٔ هلنیستی از عبری/آرامیِ \"\n                            \"فلسطین وام گرفته است (نام خواهر هیرودیس و یکی از زنانِ کنار گور در انجیل مرقس)، پس این جعبه باید \"\n                            \"زیرشاخهٔ عبری (#۶) باشد نه زیرشاخهٔ مستقیم ریشه. ō عبری با ω یونانی نمایانده شده و پایانهٔ -η \"\n                            \"نشانهٔ مؤنث یونانی است.\"),\n          \"sources\": [W + \"Salome\", AHD_SEM],\n          \"ref_check\": [\n            {\"ref\": \"AHD:1541\", \"status\": \"partial\", \"note\": \"Online AHD Semitic appendix, root šlm: 'Salome, from a Hebrew personal name akin to šəlōmît, Shelomith (biblical name), from šālôm (see above).' AHD makes it a Hebrew name, gives no Greek common noun 'salōmē = peace', and routes it through Hebrew, not straight from the root.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"s.v. Salome (p. ~1435, line 33562)\", \"stance\": \"contradicts\", \"note\": \"\\\"Salome, fem. PN. — Late L., fr. Gk. Σαλώμη, which is rel. to Σαλωμών, 'Solomon'. See Solomon.\\\" — a personal name only; Klein records no Greek noun meaning 'peace'.\"},\n            {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/Salome\", \"stance\": \"contradicts\", \"note\": \"\\\"From Ancient Greek Σαλώμη (Salṓmē), from Hebrew שְׁלוֹמִית (sh'lomít) (belonging to the same root as שָׁלוֹם (shalóm, 'peace')).\\\" — Hebrew → Greek, and a name, not a common noun.\"},\n            {\"src\": \"AHD\", \"where\": \"Semitic appendix root šlm\", \"stance\": \"partial\", \"note\": \"Lists Salome under šlm but as a Hebrew personal name.\"}\n          ]\n        },\n        {\n          \"id\": 11,\n          \"lang\": \"English\",\n          \"words\": \"Salome\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": (\"English Salome is taken from the Greek of the New Testament (Σαλώμη, Mark 15:40, 16:1) through Late \"\n                         \"Latin Salome, entering English as a biblical/ecclesiastical name; it was revived as a given name and \"\n                         \"made famous in the 19th century by the conflation with the unnamed dancing daughter of Herodias \"\n                         \"(Josephus supplies the name Salome) and by Wilde's and Strauss's Salome. The chart's Greek → English \"\n                         \"arrow is therefore right, with Latin as the unstated intermediary; Nourai's gloss 'an old female name' \"\n                         \"is accurate.\"),\n          \"derivation_fa\": (\"نام انگلیسیِ Salome از یونانیِ عهد جدید (Σαλώμη، مرقس ۱۵:۴۰) و از راه لاتینِ متأخر Salome به \"\n                            \"انگلیسی رسیده و همچون نامی کتاب‌مقدسی به کار رفته است؛ در سدهٔ ۱۹م با آمیختنِ آن با دخترِ \"\n                            \"بی‌نامِ هیرودیا (که نامش را یوسفوس آورده) و با نمایشنامهٔ وایلد و اپرای اشتراوس آوازه یافت. \"\n                            \"پیکانِ «یونانی ← انگلیسی» درست است، هرچند میانجیِ لاتین در نمودار نیامده. ادعای نورایی درست است.\"),\n          \"sources\": [W + \"Salome\", AHD_SEM],\n          \"ref_check\": [\n            {\"ref\": \"AHD:1145\", \"status\": \"not_checked\", \"note\": \"The 1975/76 AHD New College main dictionary (where p. 1145 would carry the entry Salome) is not open online; the online AHD Semitic-roots appendix has the same derivation ('Salome, from a Hebrew personal name akin to šəlōmît ... from šālôm'), which is consistent with Nourai's arrow.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"s.v. Salome (line 33562)\", \"stance\": \"supports\", \"note\": \"\\\"Salome, fem. PN. — Late L., fr. Gk. Σαλώμη\\\" — Greek → Late Latin → English, exactly this node plus the Latin step.\"},\n            {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/Salome\", \"stance\": \"supports\", \"note\": \"\\\"From Ancient Greek Σαλώμη (Salṓmē)\\\" as the source of the English name.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\n\nwith io.open('data/verification/page-459.json','w',encoding='utf-8') as f:\n    json.dump(data,f,ensure_ascii=False,indent=2)\n    f.write('\\n')\nprint('written')\nPYEOF\npython3 -m json.tool data/verification/page-459.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 459"
}
```


### [2026-09-14T02:43:25.125Z] TOOL RESULT

```
written
JSON OK
nodes verified: 11/11
node verdicts: {'confirmed': 5, 'transcription_suspect': 2, 'disputed': 4}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 8, 'not_checked': 7, 'not_found': 1, 'partial': 2}
books consulted: {'supports': 15, 'silent': 5, 'contradicts': 7, 'partial': 9} | by book: {'KLN': 10, 'Wiktionary': 8, 'LKT': 3, 'SKT': 3, 'MON': 3, 'AHD': 3, 'BQT': 2, 'FVQ': 1, 'ARY': 1, 'Etymonline': 1, 'FSD': 1}
```


## [2026-09-14T02:43:27.742Z] TOOL CALL #66: Bash

```json
{
 "command": "ls -la /home/sfmqrb/git/rishe/data/verification/page-459.json"
}
```


### [2026-09-14T02:43:27.787Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 51264 Sep 13 22:43 /home/sfmqrb/git/rishe/data/verification/page-459.json
```


## [2026-09-14T02:43:44.493Z] AGENT

Page 459 (book p. 429), root **S.l.m / Š.l.m** [Semitic] — one non-redirect entry, 11 nodes. `verify_check.py 459`: 11/11 nodes, **0 PROBLEM lines**.

Verdicts: root confirmed · nodes 5 confirmed, 4 disputed, 2 transcription_suspect.

Flagged items:
- **#4 Malaysian `salang`** — transcription_suspect (`error_in: book`; the page really prints "salang"). Malay *salang* means "execution by driving a keris through the collarbone"; the greeting word is *selamat* (< Ar. سلامات), and it should hang from the Arabic node, not from the root.
- **#5 English `so long`** — disputed. Etymonline: "of unknown origin… Earlier guesses that it was a sailors' corruption of a South Pacific form of Arabic salaam are not now convincing"; first attested 1860 (Whitman), so the chart's NOTE ("colloquial among British soldiers") is also wrong.
- **#6 Hebrew `yrrŭ-šâlôm`** — transcription_suspect (`error_in: book`); no such Hebrew form, misprint for yərū-šālēm / Yərūšālayim. Gloss "city of peace" is a popular etymology; standard view = *yarú* "he lays down" + Šālēm (Canaanite god), cf. Amarna Urušalim. (šalôm and Ab-šalôm themselves confirmed.)
- **#7 French (empty box)** — disputed. No French intermediary; French *Jérusalem* cannot yield اورشلیم.
- **#8 Persian `اورشلیم`** — disputed edge: word genuine but from Syriac ʾŪrišlem / Arabic أورشليم (and 19th-c. Persian Bible usage), not from French.
- **#10 Greek `salômě "peace"`** — disputed. Greek has no common noun σαλώμη; Σαλώμη is only the Hellenised Hebrew name (Klein, AHD, Wiktionary), so the box belongs under Hebrew #6.

Extraction errors for the owner: **none of substance** — the JSON matches the printed page (page image saved to `data/verification/sources/refs/ocr/BOOK/459.png`). Only trivial diacritic loss in the Persian extras line (`سلیم`/`مسلم` for printed `سَلیم`/`مُسلِم`).

References: KLN:1430/828/1471 all check out against the local Klein OCR (his page numbers are accurate — vol. I ends at 853 with the K words, so Jerusalem at 828 fits). AHD:1541 verified against the online AHD Semitic-roots appendix (root šlm), which carries Nourai's whole derivative list. Not accessible: OEW:451 (Shipley, IA lending-only, djvu 403 and search-inside empty), FSD:2316 (headword exists — "so long, see SO-LONG" — but that page's OCR is lost), SAP:726, FVA:196, MON5:195 (Mo'in vol. 5 not digitised; used Dehkhoda/abadis instead). 14 web pages archived via `fetch_source.py`.
