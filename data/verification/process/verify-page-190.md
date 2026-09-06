# Verification process log — verify-page-190


## [2026-09-06T02:13:16.069Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 190 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-190.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-190.json. Write /home/sfmqrb/git/rishe/data/verification/page-190.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 190` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T02:13:17.358Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T02:13:18.228Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T02:13:18.245Z] TOOL RESULT

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
226	```json
227	{
228	  "pdf_page": 126,
229	  "book_page": 96,
230	  "verified_by": "claude-opus-5",
231	  "verified_on": "2026-09-05",
232	  "entries": [
233	    {
234	      "entry": 0,
235	      "root": "Dheigh, Dhigha",
236	      "verdict": "confirmed",
237	      "modern_form": "PIE *dʰeyǵʰ- 'to knead, form (clay)'",
238	      "note": "Pokorny 244 dheiĝh-; AHD dheigh-. Root, language label and gloss all correct.",
239	      "note_fa": "ریشهٔ هندواروپایی آغازین *dʰeyǵʰ- «خمیر کردن، شکل دادن (گِل)» … ادعای نورایی درست است.",
240	      "sources": ["https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dʰeyǵʰ-"],
241	      "ref_check": [{"ref": "POK:244", "status": "supports", "note": "…"}],
242	      "consulted": [{"src": "WLD", "where": "Bd. I 833", "stance": "supports", "note": "…"}],
243	      "nodes": [
244	        {
245	          "id": 6,
246	          "lang": "Avestan",
247	          "words": "pairi-daeza",
248	          "verdict": "confirmed",
249	          "derivation": "Av. pairi-daēza- 'walled enclosure' = pairi 'around' (PIE *per-) + daēza- 'wall' …",
250	          "derivation_fa": "«پردیس» … اوستایی pairi-daēza- «دیوارکشیده، باغِ محصور» از pairi «پیرامون» و daēza- «دیوار» …",
251	          "sources": ["https://en.wiktionary.org/wiki/pairidaēza"],
252	          "ref_check": [{"ref": "POK:244", "status": "supports", "note": "…"}],
253	          "consulted": [{"src": "BRT", "where": "col. 866", "stance": "supports", "note": "…"}]
254	        }
255	      ]
256	    }
257	  ]
258	}
259	```
260	
261	Rules:
262	- Include EVERY node of every non-redirect entry on the page (even empty-word pass-through
263	  nodes like `[Latin] refs=None |` — give them a one-line derivation and a verdict).
264	- `words` = the transliterations of the node joined by "; " (copy from the chart).
265	- `derivation` must be specific: forms, sound changes, dates/eras, texts or peoples,
266	  semantic shifts. 1–5 sentences. No hand-waving like "derived regularly".
267	- Keep `note` on the entry for root-level comments and for anything cross-cutting.
268	- If a node lists several words, cover each word; if they differ in verdict, use the worst
269	  verdict for the node and explain per word in `derivation`.
270	- Where the chart's own NOTE already records a dispute, evaluate it: say which side modern
271	  scholarship takes.
272	- Every node has `ref_check` (array, may contain a single `not_checked` item) AND `consulted`
273	  (array) AND `derivation_fa` (string); every entry has `note_fa`.
274	- Valid JSON only. Test it with `python3 -m json.tool` before finishing, then run
275	  `python3 /home/sfmqrb/git/rishe/tools/verify_check.py <pdf page>` — it must show 0 PROBLEM lines.
276	- When done, reply with a SHORT summary (≤ 15 lines): counts of verdicts per page, and a
277	  bullet per `disputed` / `transcription_suspect` item (root, word, one-line reason), plus
278	  any extraction errors (JSON differs from the printed page) the owner must fix.
279	  Do not paste the JSON back into your reply.
280	
```


## [2026-09-06T02:13:18.783Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-190.txt"
}
```


### [2026-09-06T02:13:18.802Z] TOOL RESULT

```
1	=== PDF page 190 (book page 160) ===
2	--- entry 0 ---
3	ROOT Gherd -> redirect to Gher 1
4	--- entry 1 ---
5	ROOT [Indo-European] Ghers : to be horrified, to stare  (refs POK:445)
6	#1 (parent #0) [Avestan] refs=POK:445; KLN:744 | zrš, zarš : to be horrified ; zaršayamna : ruffling one's feathers
7	#2 (parent #0) [Latin] refs=POK:445 | horrĕre : to be horrified
8	  #3 (parent #2) [English] refs=None | horror
9	--- entry 2 ---
10	ROOT [Indo-European] Gherto : milk, butter  (refs POK:446)
11	#1 (parent #0) [Sanskrit] refs=POK:446; AEF:40 | ğar : milk, also anything wet ; â-gar : to soak, also to swallow | NOTE: AEF:40 lists the Latin word "Vorâre:to swallow" as a cognate. See root "Gwer 3:to swallow".
12	  #2 (parent #1) [Persian] refs=POK:446; HRN:9; AEF:41; BQT:47 | âğâr «آغار» : wetness, humidity ; âğârîdan «آغاریدن» : to soak ; âğeštan «آغشتن» : to soak in (mix with) ; âğar «آغر» : water puddles in a dried river | extra: آغاردن ، آغردن
13	  #3 (parent #1) [Persian] refs=BQT:1465; FRS:98; MON:2520 | farğârîdan «فرغاریدن ، فرغردن» : to soak ☞Per 1 ; farğâr «فرغار» : soaked ; farğar «فرغر» : little puddles of water in a dried river ; farğan «فرغن» : new river ; farğandeh «فرغنده» : rotten
14	--- entry 3 ---
15	ROOT Ghes -> redirect to Ghdies
16	
```


## [2026-09-06T02:13:23.479Z] TOOL CALL #3: Bash

```json
{
 "command": "python3 -m json.tool data/extracted/batch/page-190.json | head -200"
}
```


## [2026-09-06T02:13:23.880Z] TOOL CALL #4: Bash

```json
{
 "command": "ls data/verification/ | head -40 && echo \"---\" && cat data/verification/sources/SOURCE_MATRIX.md | head -120"
}
```


### [2026-09-06T02:13:25.013Z] TOOL RESULT

```
{
    "pdf_page": 190,
    "book_page": 160,
    "entries": [
        {
            "root": {
                "name": "Gherd",
                "redirect": "Gher 1"
            },
            "nodes": []
        },
        {
            "root": {
                "name": "Ghers",
                "lang": "Indo-European",
                "refs": "POK:445",
                "gloss": "to be horrified, to stare"
            },
            "nodes": [
                {
                    "id": 1,
                    "parent": 0,
                    "lang": "Avestan",
                    "refs": "POK:445; KLN:744",
                    "words": [
                        {
                            "translit": "zr\u0161, zar\u0161",
                            "gloss": "to be horrified",
                            "script": null
                        },
                        {
                            "translit": "zar\u0161ayamna",
                            "gloss": "ruffling one's feathers",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 2,
                    "parent": 0,
                    "lang": "Latin",
                    "refs": "POK:445",
                    "words": [
                        {
                            "translit": "horr\u0115re",
                            "gloss": "to be horrified",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 3,
                    "parent": 2,
                    "lang": "English",
                    "refs": null,
                    "words": [
                        {
                            "translit": "horror",
                            "gloss": null,
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                }
            ]
        },
        {
            "root": {
                "name": "Gherto",
                "lang": "Indo-European",
                "refs": "POK:446",
                "gloss": "milk, butter"
            },
            "nodes": [
                {
                    "id": 1,
                    "parent": 0,
                    "lang": "Sanskrit",
                    "refs": "POK:446; AEF:40",
                    "words": [
                        {
                            "translit": "\u011far",
                            "gloss": "milk, also anything wet",
                            "script": null
                        },
                        {
                            "translit": "\u00e2-gar",
                            "gloss": "to soak, also to swallow",
                            "script": null
                        }
                    ],
                    "note": "AEF:40 lists the Latin word \"Vor\u00e2re:to swallow\" as a cognate. See root \"Gwer 3:to swallow\".",
                    "quote": null
                },
                {
                    "id": 2,
                    "parent": 1,
                    "lang": "Persian",
                    "refs": "POK:446; HRN:9; AEF:41; BQT:47",
                    "words": [
                        {
                            "translit": "\u00e2\u011f\u00e2r",
                            "gloss": "wetness, humidity",
                            "script": "\u0622\u063a\u0627\u0631"
                        },
                        {
                            "translit": "\u00e2\u011f\u00e2r\u00eedan",
                            "gloss": "to soak",
                            "script": "\u0622\u063a\u0627\u0631\u06cc\u062f\u0646"
                        },
                        {
                            "translit": "\u00e2\u011fe\u0161tan",
                            "gloss": "to soak in (mix with)",
                            "script": "\u0622\u063a\u0634\u062a\u0646"
                        },
                        {
                            "translit": "\u00e2\u011far",
                            "gloss": "water puddles in a dried river",
                            "script": "\u0622\u063a\u0631"
                        }
                    ],
                    "script_extra": "\u0622\u063a\u0627\u0631\u062f\u0646 \u060c \u0622\u063a\u0631\u062f\u0646",
                    "note": null,
                    "quote": {
                        "text": "\u0627\u0632 \u0647\u0631 \u0686\u0647 \u0633\u0628\u0648 \u067e\u0631 \u06a9\u0646\u06cc \u0627\u0632 \u0632\u06cc\u0631 \u0648 \u0632\u067e\u0647\u0644\u0648\u0634 - \u0632\u0627\u0646 \u0686\u06cc\u0632 \u0628\u0631\u0648\u0646 \u0622\u06cc\u062f \u0648 \u0628\u06cc\u0631\u0648\u0646 \u062f\u0647\u062f \u0622\u063a\u0627\u0631",
                        "poet": "N\u00e2ser-Khosrow"
                    }
                },
                {
                    "id": 3,
                    "parent": 1,
                    "lang": "Persian",
                    "refs": "BQT:1465; FRS:98; MON:2520",
                    "words": [
                        {
                            "translit": "far\u011f\u00e2r\u00eedan",
                            "gloss": "to soak",
                            "script": "\u0641\u0631\u063a\u0627\u0631\u06cc\u062f\u0646 \u060c \u0641\u0631\u063a\u0631\u062f\u0646",
                            "see": [
                                "Per 1"
                            ]
                        },
                        {
                            "translit": "far\u011f\u00e2r",
                            "gloss": "soaked",
                            "script": "\u0641\u0631\u063a\u0627\u0631"
                        },
                        {
                            "translit": "far\u011far",
                            "gloss": "little puddles of water in a dried river",
                            "script": "\u0641\u0631\u063a\u0631"
                        },
                        {
                            "translit": "far\u011fan",
                            "gloss": "new river",
                            "script": "\u0641\u0631\u063a\u0646"
                        },
                        {
                            "translit": "far\u011fandeh",
                            "gloss": "rotten",
                            "script": "\u0641\u0631\u063a\u0646\u062f\u0647"
                        }
                    ],
                    "note": null,
                    "quote": {
                        "text": "\u0627\u0632 \u0622\u0628 \u062f\u0631\u06cc\u0627 \u06af\u0641\u062a\u06cc \u0647\u0645\u06cc \u0628\u06af\u0648\u0634 \u0622\u0645\u062f - \u06a9\u0647 \u0634\u0647\u0631\u06cc\u0627\u0631\u0627 \u062f\u0631\u06cc\u0627 \u062a\u0648\u0626\u06cc \u0648 \u0645\u0646 \u0641\u0631\u063a\u0631",
                        "poet": "Farrokh\u00ee"
                    }
                }
            ]
        },
        {
            "root": {
                "name": "Ghes",
                "redirect": "Ghdies"
            },
            "nodes": []
        }
    ]
}
```


### [2026-09-06T02:13:25.057Z] TOOL RESULT

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
---
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
```


## [2026-09-06T02:13:30.124Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KLN','AEF','HRN','BQT','FRS','MON','WLD','AHD','BRT','IEC','SYN','LEW','LAT','ARY','SKT','FSD','WEB','HUB','CHEUNG','FFD','ISS']:\n    print(k, json.dumps(d.get(k),ensure_ascii=False)[:600])\n    print()\n\""
}
```


### [2026-09-06T02:13:31.992Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

AEF {"title": "Jalal Khaleqi Motlaq, Asas-e Eshteqaq-e Farsi, vol. I (آ–خ), Bonyad-e Farhang-e Iran 1356/1977 — this is the Persian TRANSLATION of Paul Horn's Grundriss der neupersischen Etymologie (HRN) with Hübschmann's Persische Studien (HUB) notes and added Persian/Pahlavi evidence", "kind": "catalog", "url": "https://openlibrary.org/works/OL38785552W (vol. 1, 1356) ; 2015 complete ed. «فرهنگ ریشه‌شناسی فارسی» (مهرافروز) print-only: https://www.gisoom.com/book/11154690/ ; German original: https://archive.org/details/grundrissderneu00horngoog", "lookup_hint": "Not online (searched archive.org, 

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

FRS {"title": "Asadi Tusi, Loghat-e Fors, ed. Mojtaba'i & Sadeqi, Kharazmi 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/LughatEFurs-AbuMansurAliBinAhmadAsadiTusiFarsi (Abbas Eqbal's 1319/1940 Tehran edition); also dli.ernet.439493 / dli.ernet.437743 (Horn's 1897 Göttingen edition, 'Lughat Faras')", "lookup_hint": "Look up the headword (entries grouped by final letter); FRS_pages.txt has \\f page breaks (567 leaves). Pagination differs from the 1365 Kharazmi edition Nourai cites — verify the entry, not the page.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/s

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves

LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt", "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f b

LAT {"title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951", "edition_found": "1951 (3rd ed.) - matches Nourai", "kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "identifier": "ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine (4th ed. 1959 lending-only: dictionnairetymo0000unse; another open copy: DictionnaireEtymologiqueDeLaLangueLatine)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt", "page_offset": "leaf = printed + 18 for mos

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 

SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves

FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt

WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/W

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol

CHEUNG null

FFD {"title": "Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ماده-های-فعلهای-فارسی-دری-محسن-اب/ -> https://dl.eliteraturebook.com/app/public/attachments/6925d29630b83.PDF (free PDF site; grey)", "lookup_hint": "Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/download): nothing; only a related paid e-book 'واژگان زبان فارسی دری' (fidibo). ketabnak.com/book/45024 is a different book (فهرست فعلهای فارسی).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/s

ISS {"title": "H. W. Bailey, Indo-Scythian Studies: Khotanese Texts VI (Prolexis to the Book of Zambasta), Cambridge 1967", "edition_found": "not found; Bailey's Dictionary of Khotan Saka (1979) downloaded as the closest substitute", "kind": "google_books_preview+archive_restricted", "url": "https://books.google.com/books?id=4upthUgWo9YC (CUP 2009 reprint, partial preview) ; HathiTrust mdp.39015034317936 (v.6, search-only) ; archive.org khotanesetexts0103bail (vols I-III only, lending)", "identifier": "dictionary-of-khotan-saka (substitute); khotanesetexts0103bail is vols I-III, lending-only", "lo
```


## [2026-09-06T02:13:35.962Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in POK_01.txt POK_02.txt POK_03.txt; do echo \"== $f\"; python3 -c \"\nimport sys\nt=open('$f',encoding='utf-8',errors='replace').read().split('\\f')\nprint(len(t),'leaves')\n\"; done"
}
```


## [2026-09-06T02:13:37.109Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"ĝhers\\|ghers-\\|ĝher-s\\|horrēre\\|horrere\" POK_full.txt | head -30"
}
```


### [2026-09-06T02:13:37.781Z] TOOL RESULT

```
== POK_01.txt
364 leaves
== POK_02.txt
434 leaves
== POK_03.txt
430 leaves
```


### [2026-09-06T02:13:37.834Z] TOOL RESULT

```
33084:under ghers-. 
33134:Root / lemma: ghers-1, ghres- 
33159:Root / lemma: ghers-2 
36987:root extension gheres-, ghres-, ghers-: 
37001:See also: s. ghers- 
37004:Root / lemma: ghers- and partly gher- 
37014:eater)' derived Root/ lemma: ghers-, gher-\ "rigid, *pig' > Root/ lemma: portto-s\ pig' : 
37034:"struppig, rough'; based on parallel to *ghers-k"'os {as Oscan-Umbrian loanword) hispidus 
37035:"rough'; mars, sabin. hernau. PI. ' rocks ' {*ghers-no); 
37122:g/rsa " darnel ' here place (see below ghers-2). 
42430:Root / lemmai^b/^fr- : a kind of roebuck : Root / lemma: ghers-, gher-\ rigid : alb. o'er/r pig' 
68633:ghers-, gher-\ "rigid, *pig' > Root/ lemma: porRo-s\ "pig' : lllyrian-italic-celtic g'^h- > p-.
```


## [2026-09-06T02:13:40.306Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '36990,37060p' POK_full.txt"
}
```


### [2026-09-06T02:13:40.368Z] TOOL RESULT

```
hrasati^ abate, reduce, become shorter ', Kaus. hrasayati^ decreases', Avestan zara- 
heh/s'the small, weak' (for zra . .); 

Middle Irish gerr' short', gerra/ml shorten, abscise, remove, cut off, gerran'{ 
castrated) horse'. 

References: WP. I 604f., SchwyzerGr. Gr. I 538 under Anm. 10, 539, 675 under Anm. 8. 
Page(s): 443 

Root / lemma: gher-7 
Meaning: " gaze, stare ' 
See also: s. ghers- 
Page(s): 443 

Root / lemma: ghers- and partly gher- 

Meaning: rigid, *pig 

Note: (see also gher-3) 

Note: 

From an extended zero grade of Root/ lemma: eghi- {* eghi-no-s)\ "hedgehog (*serpent 

eater)' derived Root/ lemma: ghers-, gher-\ "rigid, *pig' > Root/ lemma: portto-s\ pig' : 

lllyrian-italic-celtic g"h- > p-; also {*egh/-no-s) > {* ghers) abbreviation and rhotacism n/r. 

Note: 

Root/ lemma: eghi-{* eghi-no-s)\ "hedgehog (*serpent eater)' derived from Root/ lemma: 

ang''(h)i- {* eg^hi-, og'^hi- and egh/-): "snake, worm, (*hedgehog = snake eater)' 

Material: 



Old Indie harsate, hrsyatr becomes stiff, ruffles, shudders, is excited, is glad, is 
aroused '; Latin horreo, -ere^ to stand on end, stand erect, bristle, be rough, tremble, 
shudder, quake, shudder at, tremble at, be afraid of, dread ' (= Avestan zarsaya-); in 
*gher-k"o-yN\Vc\ dial, /from e before r+ gutturals (e.g. stircus: stercus) based on Latin 
hircus, sabin. /^/r^5 "he-goaf {hirquTnus, h/rc/hus ^ oi \r\e-goat, billy goat ') = Oscan-sab. 
h/rpuslupus' (whereof the people's name Hirpini); in addition also /7//Vt/s 'bristly', hirsOtus 
"struppig, rough'; based on parallel to *ghers-k"'os {as Oscan-Umbrian loanword) hispidus 
"rough'; mars, sabin. hernau. PI. ' rocks ' {*ghers-no); 

Note: 

Common Old Indie : Latin gh-> h-. 

Maybe Latin horreo, -ere' dread ' > alb. n. urrejtja, v. urrej' hate ': Sardinian 
Campidanesu n. tirriu; tirria, v. tirhai: Romanian n. ura, v. ur?\ urgisi: French n. horreur, 
V. horreur' hate '. 

Probably Latin Latin horreo, -ere' dread ' {*ghorred) : Basque n. gorroto, v. gorrotatu: 
Hungarian n. gyulolet, v. gyuldl' hate ' as in: Proto-Altaic: *gali Meaning: to hate, wild 
: Turkic: *K(i)al : l\^ongolian: *gal3aYU : Tungus-I\^ancliu: *galu- : Japanese: *k[rap-. 

Avestan zarsayamna- ' die Federn aufstraubend ' {zars- = zrs- = Latin horred); zarstva- 
n. ' stone '; 

Armenian y5/'(-/; -i\) ' mane of horse ' {*gheri-)\ 

Maybe from Armenian ya/'(-/; -iv) " mane of horse ' > turk. yele) ' mane of horse ' > alb. 
Jele " mane of horse '. 

gr. x£pcfO(; (Attic x£PPO<;) f. " mainland, continent or the main part of a continent as 
distinguished from islands or peninsulas', nachhom. also Adj. " barren, dry, tight, firm'; 

Maybe alb. {*ghei) djerre' barren, dry land '.
```


## [2026-09-06T02:13:42.714Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '37060,37140p' POK_full.txt"
}
```


### [2026-09-06T02:13:42.764Z] TOOL RESULT

```
Maybe alb. {*ghei) djerre' barren, dry land '. 

gr. perhaps lengthened grade noun from the s- loose root form gher-{ox gher-)\ xnp XIPO*^ 
"hedgehog' (= Latin er, er/s6s., erfcius, erinaceus, herinaceus 6s.)\ 

Maybe Latin erlcTus , ii, m. [er] , " a hedgehog, urchin ' : Romanian {*erTcius) arid 
"hedgehog': Albanian {* erfcius) //7(7/"hedgehog' [conservative singular definite form (alb. 
phonetic trait)]. 



gr. xoTpo(; (< *ghorios) "piglet' (as pig), xoipa<; " inflated gland in the neck; cliff' (or to gher-3 
" project, protrude', see there); 

alb. ofe/r'swine' (< *ghdr-n- with lengthened grade as in XHP). ofer/r "piglet, sow' (< 
*ghdr-n-l<); 

Note: 

Common alb. shift gh- > d-\ also alb. {*derk-us) o'e/'/ri/c "piglet', {*ghork-os) cfose'so\N' : 
Latin hircus, sabin. fircus "he-goaf proves that solidified -us : -os ending was attested also 
in proto alb. 

Unique similarity Albanian derri: Basque txerri^'^'v^ 

Old Irish garb, cymr. ^a/'M/"rough' {ghr-uo-)\ Note: common lllyrian g"- > b-. 

Old English gorsf gorse ' and the etymological cognate group gherzd-^bar\ey\ 

compare in allg. Pick 1^219, 435, IH 107, 111^ 130 (and Falk-Torp under ^/l^z-sm. 
Lithuanian about the fish names Norwegian gjors^ Pike Perch ', Swedish gers^ ruffe, 
perch, chub', prakrit. y/7asa-"a kind offish'). 

References: WP. I 610, WH. I 413 f., 650, 659. 
Page(s): 445-446 

Root / lemma: gherzd(h), Gen. ghfzd(h)-es, gherzda 

Meaning: barley, grain, spike 

Material: Gr. KpT n. (conservative stem, as alb. drith) "barley', probably from Indo Germanic 

*ghrzA^, from which proto gr. *k~rth\ KpTOr), mostly PI. "barley', Sg. (later covered) "barley'; 

alb. drith i^ghrzA^), drithem. n. "barley, corn, grain '; 

Maybe alb. drize^ bush'. 

Latin bordeum {6\a\. fordeum) n. "barley' (from *gbrzd{b)eiom^ grain awn ', substantive 
adjective); 

zero grade: Old High German ^ers/a "barley' {*gberzda). 



In addition perliaps gr. {* akherdos) a-x£p5o(;f. "wild pear tree, hawthorn', maked. a- 
Y£p5a, gr. a-xpac; "wild pear tree' (a < *sm-), alb. darc/he^ pear, pear tree' {*ghor-6^-) and 
the antike VN Aap5avoi; 

alb. dardhe'pear, pear tree' = Armenian tandz' pear' 

only under assumption a of guttural change (above S. 18, Anm. 1) has made Lithuanian 
g/rsa " darnel ' here place (see below ghers-2). 

References: WP. I 611, WH. I 414, 657, Specht Indog. Dekl. 
Page(s): 446 

Root / lemma: gheslo- 

Meaning: thousand 

Note: 

Root / lemma: gheslo- : thousand' derived from Root / lemma: ghesor-1, ghesr- : "hand, 

*hand count' [///allophones] 

Material: Old Indie sa-hasramn. " thousand ' {sm -gheslom, to sem- " one '), sa-hasriya- 

"tausendfach', Avestan hazanr9mr\. "thousand', npers. hazar, from which borrowed
```


## [2026-09-06T02:13:52.356Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"gher-to\\|gherto\\|ghert-\\|Root / lemma: gher-\" POK_full.txt | head -30"
}
```


### [2026-09-06T02:13:52.412Z] TOOL RESULT

```
18272:Root / lemma: deii(- : to look derived from Root / lemma: gher-3 und ghere-, ghre- : to 
33008:Root / lemma: gher-1 
33052:Root / lemma: gher-2 
33078:Root / lemma: gher-3, ghre- : ghro- : ghra- 
33175:Root / lemma: gherto- 
36766:Root / lemma: gher-1 
36823:Root / lemma: gher-2 
36838:Root / lemma: gher-Sand ghera-, ghre- 
36881:Root / lemma: gher-4 
36925:Root / lemma: gher-5, ghor-na 
36968:Root / lemma: gher-6 [ghera- : ghre-1) 
36999:Root / lemma: gher-7
```


## [2026-09-06T02:13:54.962Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '33170,33200p' POK_full.txt; echo \"=== index area ===\"; sed -n '33000,33010p' POK_full.txt"
}
```


### [2026-09-06T02:13:55.051Z] TOOL RESULT

```
"barley'; compare Mijhlenbach-Endzelin I 555, 618 f.). 

References: WP. 1611, Trautmann 79 f. 
Page(s): 445 

Root / lemma: gherto- 

Meaning: milk, butter 

Note: only Aryan and Celtic 

Material: Old Indie ^/7/fa/77" skimmings, butter, melting butter'; 

after Uhlenbeck io Jfgharti {gharati) " sprays, sprinkles ', npers. a-yardan^ blend, mix, 
soak'; 

Middle Irish ^e/f "milk'. 

References: WP. I 607, II 166. 
Page(s): 446 

Root / lemma: gheub(h)- 

Meaning: to bend, move 

Material: Norwegian dial, guva^ sit sunk down ', S^edUsh jordgubbe^ Fragaria ananassa; 

strawberry ', Old Danish gubbe^\avjv\x, breast', ndd. (Estland) gubbe^ small haycock. 



=== index area ===
References: WP. I 584 f., WH. I 783, Trautmann 93. 



Page(s): 436-437 



Root / lemma: gher-1 

Meaning: expr. root
```


## [2026-09-06T02:13:55.950Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"ghrta\\|ghrtam\\|ghar-\\b\\|Schmalz\\|clarified butter\" POK_full.txt | sed -n '1,40p'"
}
```


### [2026-09-06T02:13:56.022Z] TOOL RESULT

```
63553:eyes and mouth)' ( *proti, *eni+ ok"-\ compare Slavic nicb under *ni- 'low, mean'), ghrtacTt
```


## [2026-09-06T02:14:07.583Z] TOOL CALL #13: Bash

```json
{
 "command": "ls data/verification/ | grep -E \"page-18[0-9]|page-19[0-9]\" "
}
```


### [2026-09-06T02:14:07.630Z] TOOL RESULT

```
page-180.json
page-181.json
page-182.json
page-183.json
page-184.json
page-187.json
page-189.json
```


## [2026-09-06T02:14:10.161Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"âgârdan\\|agardan\\|ā́γārdan\\|aġārdan\\|agârdan\\|âgâridan\\|agârîdan\" HRN.txt | head -20; echo \"--- leaf for p9 = leaf 30\"; python3 -c \"\nt=open('HRN.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(t[30][:3000])\n\""
}
```


### [2026-09-06T02:14:11.662Z] TOOL RESULT

```
--- leaf for p9 = leaf 30
- 9 ~
34(2). äänä, äsnäh 'Öchwinuner, Schwimmerei', üsnäh^ dsnäiv,
aw. ai. ä -f- [/'snä-, nur in der Bedeutung Vaschen' ;
vergl. aber aw. asnätar-, skr. äsnäna- (*Bad').
Vergl. sina (No. 792).
35. äsyäne, äsyän 'Nest'.
a + aw. Ksö- bezw. gäi>. syä- ruhen' ^), oder wohl
bereits wohnen'^). (Nöldeke, mündliche Mitteilung).
Aber das y ist auffällig, vergl. np. süd,
36. üyärden, ayäriden Verschlingen*.
ai. ä + l/^gar- {jacjdrd) verschlingen' ; lat. coräre,
wa;^. nez-yar-am verschlingen*.
In der Bedeutung Verschlingen' vermag ich das Wort
nicht zu belegen. Bei AM., wo es sehr häufig vor-
kommt, bedeutet es immer vermischen, einweichen in'.
In der letzten Bedeutung könnte es zu skr. l/^ghar-,
ghdrati 'besprengen, beträufeln* gehören^).
37. äftäh *Sonne, ixDS'X (jüd.-pers.).
skr. "^ahha + tapa- (vergl. No. 3).
kurd. LW. a^taw (Houtum-Schindler), ätätv etc.
(Jaba-Justi).
38. äfdutn 'letzter', nur im Mujmil ettevärT;^ (ed. Mohl,
Journ. asiat. 1841, S. 178)^), vergl. hafdum zuletzt*^).
«) Hübschmann, ZDMG. 38, 431.
') Bartholomae, Arische Forsch ungren II, 102.
*) Dazu wohl auch äyisten, z. B. AM. 14 Zeile 16, 193 Zeile 11.
do Lagarde, Ges. Abh. 290 ist natürlich unmöglich.
*) Vergl. Spiegel, Grammatik der- Huzväresch-Sprache, 76.
^) Für bäfdum (d. i. be äfdum) haben die Wörterbücher folgende
Belegstellen: SF (S. 95 Vers 53), Metrum Remel:
kär-i dänä nek^ gerded bäf^dum
FR, Metrum Muteqärib:
ci bäyedf kerden kenün bäf^dum
meger -j^äne-röbl cü robeh bMum
Abu SukUr.
FR, FJ, Metrum Muteqärib:
b^r esb-i gümän ez reh-i räst^ x^m
q^räret bedöze-^ büved bäj^dum
Esedl.
```


## [2026-09-06T02:14:28.100Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\ni=t.find('horror')\nfor m in re.finditer(r'horror',t):\n    s=t[m.start()-200:m.start()+700]\n    if 'Latin' in s or 'L. ' in s or 'horrere' in s or 'horrëre' in s:\n        print(s); print('======'); break\nEOF\ngrep -n \"horrid\\|horreo\\|horrere\\|horrëre\" KLN_1966.txt | head -20"
}
```


### [2026-09-06T02:14:29.848Z] TOOL RESULT

```
o  gape’.  See  bay,  ‘part  in  the  wall’, sod  cp.  words  there  referred  to.
■bhor,  tr.  v.  —  L.  abhorrire,  ‘to  shrink  away
from’,  fr.  ab-  and  horrere,  ‘to  bristle,  shudder’. See  horror.
abhorrence,  n.  —  Formed  fr.  next  word  with suff.  -ce.
abhorrent,  adj.  —  L.  abhorrens,  gen,  -entis,  pres, part,  of  abhorrere,  ‘to  shrink  away  from’.  See abhor  and  -ent.
Derivative:  abhorrent-ly,  adv. abide,  intr.  and  tr.  v.  —  OE.  abidan ,  formed  fr. intensive  pref.  a-  and  bidan,  ‘to  remain,  await’. See  bide.
Derivatives:  abid-ing,  adj.,  abid-ing-ly,  adv. Abies,  n.,  a  genus  of  trees,  the  true  fir  (bot.)  — L.  abies,  ‘silver  fir’,  cogn.  with  Gk.  fiffiv  (acc.), ‘silver  fir’,  ’Affix)),  name  of  Southern  Russia, lit.  ‘a  region  of  firs’.  Cp.  abeto. abietic,  adj.,  pertaining  to  the  crystalline  acid C20H30O2  (ch
======
1158:from’,  fr.  ab-  and  horrere,  ‘to  bristle,  shudder’. See  horror.
1160:abhorrent,  adj.  —  L.  abhorrens,  gen,  -entis,  pres, part,  of  abhorrere,  ‘to  shrink  away  from’.  See abhor  and  -ent.
7345:Chersonese,  n.,  a  peninsula.  —  L.  chersonesus,  fr. Gk.  xepo6vT)ao?,  ‘peninsula’,  which  is  com¬ pounded  of  yipooc,,  ‘dry,  hard,  barren’,  and V7 jao?,  ‘island’.  The  first  element  is  cogn.  with OI.  harsate ,  hfsyati,  ‘becomes  stiff,  bristles’, L.  horrere,  ‘to  stand  on  end,  bristle,  shudder, tremble’.  See  horror  and  cp.  -chocrus.  For  the second  element  see  ncso-.
7494:-choerus,  combining  form  meaning  ‘pig’,  as  in Hydrochoerus  ( zool .)  —  ModL.,  fr.  Gk.  yo tpog, ’pig’,  which  stands  for  *ghor-yos  and  lit.  means ‘the  bristle-bearing  animal’,  fr.  I.-E.  base  *gher-, ‘to  bristle’,  whence  also  Gk.  yry,  ‘hedgehog’, L.  horrere,  ‘to  stand  on  end,  bristle,  shudder, tremble’.  See  horror  and  cp.  Chersonese, choice,  n.  ME.  chois,  choys,  fr.  OF.  chats  (F. choix),  fr.  choisir,  ‘to  choose’,  fr.  Goth,  kausjan, ‘to  prove,  test’  (whence  also  OProveng.  causir, ‘to  look  at’),  which  is  rel.  to  Goth,  kiusan,  OE. ceosan,  'to  choose’.  See  choose.
17855:Derivative:  hirrient,  n.,  a  trilled  sound, hirsute,  adj.,  shaggy,  bristly.  —  L.  hir-sutus, ‘shaggy,  prickly,  bristly’,  rel.  to  hir-tus,  ‘rough, shaggy,  hairy’,  and  in  gradational  relationship to  horrere,  ‘to  stand  on  end,  bristle,  shake, shudder,  shiver,  tremble’.  See  horror  and  cp. hearse,  hispid.
18071:—  L.  hordeum,  ‘barley’,  which  prob.  stands  for *horzdeyom  (I.-E.  *ghpzdeyom)  and  is  cogn. with  OS.,  OHG.  gersta,  MDu.  gherste,  Du. gerst,  MHG.,  G.  gerste  (for  pre-Teut.  *gherz- da-),  ‘barley’,  Gk.  xpt  (for  *xptff),  ‘barley’, xpIffYj,  pi.  ‘barley’,  sing,  ‘barleycorn’  (prob.  for ghpzda).  Alb.  drib,  dribs  (for  ghrzd-),  ‘corn; barley’.  All  these  words  prob.  mean  lit.  ‘the bearded  plant’  and  derive  fr.  I.-E.  base  *ghers-, ‘to  bristle’,  whence  also  L.  horrere,  ‘to  stand on  end,  bristle’,  horror,  ‘bristling,  roughness’. See  horror  and  cp.  crith,  orgeat.  Cp.  also  gorse.
18088:horrendous,  adj.,  dreadful.  —  L.  horrendus ,  to be  regarded  with  horror’,  gerundive  of  horrere, ‘to  shudder,  tremble’.  See  horror.  For  the  ger¬ undive  suff.  cp.  agenda  and  words  there  refer¬ red  to.  For  E.  -ous,  as  equivalent  to  L.  -us,  see -ous.
18089:horrent,  adj.,  bristling.  —  L.  horrens,  gen.  -ends. pres.  part,  of  horrere,  ‘to  stand  on  end,  bristle, shake,  shudder,  tremble’.  See  horror  and  -ent. borrescent,  adj.,  expressing  horror;  shuddering. —  L.  horrescens,  gen.  -entis,  pres.  part,  of  hor- rescere,  ‘to  shudder’,  inchoative  of  horrere.  See horror  and  -escent.
18094:horriblete ,  fr.  horrible.  See  next  word  and  -ity. horrible,  adj.  —  ME.,  fr.  OF.  orrible,  horrible (F.  horrible),  fr.  L.  horribilis,  fr.  horrere,  ‘to shudder,  tremble’.  See  horror  and  -ible. Derivatives:  horrible-ness,  n.,  horribl-y,  adv. horrid,  adj.,  repulsive,  abominable.  —  L.  horri- dus,  ‘bristly,  prickly,  rough,  horrid,  frightful’, fr.  horrere.  See  horror  and  cp.  ordure. Derivatives:  horrid-ly,  adv.,  horrid-ness,  n. horrific,  adj.,  horrifying.  —  Formed  fr.  L.  horri- ficus,  ‘terrible,  dreadful’  (either  directly  or through  the  medium  of  F.  horrifique),  lit. ‘making  the  hair  to  stand  on  end’,  fr.  horrere, ‘to  stand  on  end’,  and  -ficus,  from  the  stem  of -ficere,  unstressed  form  of  facere,  ‘to  make,  do’. See  horror  and  -fic.
18097:horripilate,  tr.  v.,  to  cause  (the  hair)  to  bristle; intr.  v.,  to  bristle.  —  L.  horripilat  {- um )  pp.  stem of  horripilare,  ‘to  bristle  with  hair,  be  shaggy’, compounded  of  horrere,  ‘to  stand  on  end, bristle’,  and  pilus,  ‘hair’.  See  pile,  ‘hair’,  and verbal  suff.  -ate.
18098:horripilation,  n.,  bristling  of  the  hair.  —  L.  horri- pilatio,  gen.  -dnis,  fr.  horripilat  {-um),  pp.  stem of  horripilare.  See  prec.  word  and  -ion. horror,  n.  —  ME.  honour,  fr.  OF.  orror,  horror, horrour  (F.  horreur),  fr.  L.  horrorem,  acc.  of horror,  ‘bristling,  roughness,  rudeness,  shaking, trembling’,  fr.  horrere,  ‘to  stand  on  end,  bristle, shake,  shudder,  shiver,  tremble’,  fr.  I.-E.  base *ghers-,  ‘to  bristle’,  whence  also  L.  hirsutus, ‘shaggy,  prickly,  bristly’,  OI.  hdrsate,  hfsyati, ‘bristles’,  Avestic  zarshayamna-,  ‘ruffling  one’s feathers’.  Base  *ghers-  is  an  enlarged  form  of base  *gher-,  which  appears  in  Gk.  xhP>  gen. X'r)p6<;,  L.  er  (for  *hers),  gen.  eris,  ‘hedgehog’, lit.  ‘the  prickly  creature’.  See  urchin  and  cp. Chersonese,  -choerus,  hideous,  hircine,  hirsute, hispid,  Hordeum  and  the  second  element  in Hypochaeris.  Cp.  also  hearse, horror-stricken,  horror-struck,  adj.  —  Compound¬ ed  of  horror  and  the  pp.  of  strike, hors  de  combat,  out  of  the  combat;  disabled.  —
24211:Moloch,  n.,  1)  a  Semitic  god  propitiated  by  the sacrifice  of  children ;  hence  2)  anything  requiring a  dreadful  sacrifice;  3)  name  of  a  spiny  Austra¬ lian  lizard  (Moloch  horridus).  —  L.  (Vulgate), fr.  Gk.  MoX6*  (Septuagint),  fr.  Heb.  molekh,  a word  formed  fr.  Heb.  melekh,  ‘king’,  by  giving it  the  vowels  of  bSsheth,  ‘shame’  (to  show Israel’s  horror  of  this  hideous  practice  of  the heathen  Semites).  See  Mameluke, molt,  moult,  intr.  and  tr.  v.  —  ME.  mouten,  fr. OE.  *mutian,  ‘to  change’  (cp.  OE.  bi-mutian, ‘to  exchange’),  fr.  L.  mutdre,  ‘to  change’.  See mutable.
26072:odious,  adj.,  hateful;  disgusting.  —  ME.,  fr.  MF. odieus  (F.  odieux),  fr.  L.  odiosus,  ‘hateful,  offen¬ sive,  unpleasant’,  fr.  odium.  See  odium. Derivatives:  odious-ly,  adv.,  odious-ness,  n. odium,  n.,  hatred,  opprobrium,  disgust.  —  L. odium,  ‘hatred,  offense,  annoyance,  disgust’,  rel. to  odi,  odisse,  ‘to  hate’,  cogn.  with  Arm.  ateam, ‘I  hate’,  ateli,  ‘hateful,  odious’,  ON.  atall,  OE. atol,  ‘dire,  horrid,  loathsome’,  perh.  also  with Gk.  686aax<7&x'.,  ‘to  be  grieved  at,  be  angry  at’; fr.  I.-E.  base  *od-,  ‘to  hate’,  which  is  perh.  orig. identical  with  *od-,  ‘to  smell’.  See  odor  and  cp. Odysseus.  Cp.  also  noisome,  annoy.
26524:Ordovician,  adj.,  pertaining  to  the  period  follow¬ ing  the  Cambrian  and  preceding  the  Silurian (geol.)  —  Coined  by  the  English  geologist Charles  Lapworth  (1842-1920)  from  Ordovices, the  Latin  name  of  an  ancient  British  tribe  in¬ habiting  Wales.  For  the  ending  see  suff.  -ian. ordure,  n.,  dung,  filth,  manure.  —  ME.,  fr.  OF. (=  F.)  ordure,  fr.  OF.  (=  F.)  ord,  ‘filthy’,  fr.  L. horridus,  ‘rough,  rude,  causing  horror,  terrible’. See  horrid  and  -ure.
```


## [2026-09-06T02:14:39.523Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\ni=t.find(\"horror,  n.  —  ME.  honour\")\nimport re\n# find nearest page markers\nseg=t[:i]\nms=list(re.finditer(r'\\n\\s*(\\d{3})\\s*\\n',seg))\nprint([m.group(1) for m in ms[-6:]])\nseg2=t[i:i+20000]\nms2=list(re.finditer(r'\\n\\s*(\\d{3})\\s*\\n',seg2))\nprint([m.group(1) for m in ms2[:6]])\nprint('formfeeds before:', seg.count('\\f'))\nEOF"
}
```


## [2026-09-06T02:14:40.617Z] TOOL CALL #17: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nprint(json.dumps(d['BQT'],ensure_ascii=False,indent=1))\nprint(json.dumps(d['MON'],ensure_ascii=False,indent=1))\nprint(json.dumps(d['FRS'],ensure_ascii=False,indent=1))\n\""
}
```


### [2026-09-06T02:14:41.178Z] TOOL RESULT

```
['738', '739', '740', '741', '742', '743']
['746', '747']
formfeeds before: 400
```


### [2026-09-06T02:14:42.701Z] TOOL RESULT

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
{
 "title": "Asadi Tusi, Loghat-e Fors, ed. Mojtaba'i & Sadeqi, Kharazmi 1365/1986",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/LughatEFurs-AbuMansurAliBinAhmadAsadiTusiFarsi (Abbas Eqbal's 1319/1940 Tehran edition); also dli.ernet.439493 / dli.ernet.437743 (Horn's 1897 Göttingen edition, 'Lughat Faras')",
 "lookup_hint": "Look up the headword (entries grouped by final letter); FRS_pages.txt has \\f page breaks (567 leaves). Pagination differs from the 1365 Kharazmi edition Nourai cites — verify the entry, not the page.",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/FRS_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/FRS.txt"
 ],
 "page_offset": "different edition — no mapping",
 "covers_etymology": false,
 "notes": "Persian OCR fair. Ganjoor does not host Loghat-e Fors."
}
```


## [2026-09-06T02:14:52.249Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BQT v1 آغار ===\"; grep -n \"آغار\\|اغار\\|آغردن\\|آغشتن\" BQT_v1_pages.txt | head -20"
}
```


### [2026-09-06T02:14:52.312Z] TOOL RESULT

```
=== BQT v1 آغار ===
8136:آغارد بفتح را وسکون دال بی‌نقطه,
8144:آغاردن اس ت که سرشتن و تحربك نمودن وغبره
8158:آغار بدن بروزن آشامدن » ,سنی
9126:وبا لماب خطمی ومانندآن که جامه وکاغذ و جزآنرا بدان آغارند تا شخ و مک شود با حیقل و
12891:اغار - بفتح اول بر وزن شرار » بمعنی
12895:اغارد « بفتح اول و رای‌فرشت‌بروزن
12898:اغار س با زای هوز بروزن نماز, بمعنی
22176:پیاغارد ید - با ین نقطه دار و رای
22177:بی نقطه بر وزن بیاشامید » ماضی آغاربدن باشد
22202:۱ _ رف : آغاردن وآختتن .
29418:تخم میپند را در س رکه کهنه باغار نف مدتینا طبع
```


## [2026-09-06T02:14:53.887Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BQT v3 فرغار ===\"; grep -n \"فرغار\\|فرغر\\|فرغن\" incoming/BQT/BQT_v3_pages.txt | head -20; echo \"=== FRS ===\"; grep -n \"فرغار\\|فرغر\" FRS_pages.txt | head; echo \"=== MON ===\"; grep -n \"فرغار\\|فرغر\" MON_part1.txt MON_part2.txt | head"
}
```


### [2026-09-06T02:14:53.983Z] TOOL RESULT

```
=== BQT v3 فرغار ===
17812:لترنج ‎(ta)‏ کوید : در میان شهرهای ختل . یکی فرغان با فرغار است که در کنار رودی
18566:‏فرغار ‎aad‏ بر وزن سرشار ۰ ‎we‏
18606:‏۴ - ر: فرغاردن,رك: فرغر.
18621:- و بهم سرشتن وآغشته کردن باشد. فرغرده ۴ - بر وزن پرورده . ‎aT‏
18642:فرغر = بفتح اول ‎My‏ بروزن‌صرسر, فرغور « بر وزن (۳) زنبور » بمعنی
18649:‏۱ - فرغردن و رك : فرغر . ۴ - رك : ممجم‌البلدان .
18651:۷۹ :۳ و ۳۷۸ :۲ » رد : فرغردن » فرغرده ۰ فرغار » فرغاردن .
18652:‎le JL‏ بادبه ‎tay‏ فرغری ."زان سا نکهه که گفت فکردند ‎Fark‏
18655:۴ — اسم مفعول از « فرغردن > :
18656:‎ole‏ اندر نور چون فرغرده شد . پس زعلت لور بابد قوم لد ۰ مثنوی‌مولوی «فرهنگهظام».
18658:‏۱ - ابا سرو نو در تك و پوی آنم که فرغند آسا (واری) ‎seme‏ بر .
18662:۷ - استاد هنینگه ‎ag‏ : قژغند ‎IY‏ بممنی پلید وچ رکین مصحف < فرغند‌است.
18663:‎A 8305, vol X. 1,۲۰ 102, note [ : 4,‏ : فرغند » وحاشيةٌ ‎٩‏ .
18665:6 فرفردی- ‎dite‏ وسوم وپنجم؛ از: فرغر(هم.)؛ ‎PII S SF Oss‏
18725:‎op 8‏ بنتح اول بر وزن فرغره .
18972:‎٩‏ - قرکن > فرغن.«فر کند. جای گذرآب‌باشدبردیواری با زمینی» بوالمبیرعنبر گفت:
20283:بمعنی پلید وچر کین » ناثی از ضحیف «فرغند» است .
23320:‎ge‏ کند < فرغن .
=== FRS ===
6800:       ‫که بادشاها درب توبی ومن فرغر‬
6817:‫‪ - ۲‬فرغر آبی که از رود جدا شود و آبدانی گردد ‪ ۰‬س ‪ :‬فرغر‬         ‫‪:‬من‬    ‫‪ - ۱‬س‬
6822:                 ‫عومع‬  ‫درست باتعرف ع مطابقت ندارد و ظاهراً لفت فرغر به‬
17672: ‫سر که یک‌هفته فرغار کرده باشند ودرمیان چندین دارونهند آنگه دهند‬
=== MON ===
MON_part2.txt:6372:فر غار: ۰02 [فرغر» فرغاریدن] (ص‌مف.) 
MON_part2.txt:6379:فرغر: ۵0۵۲] [- فرغر» فرغود» نفرغاردن» 
MON_part2.txt:6380:فرغاریدن) جوی آب. جایی که آب از آن 
MON_part2.txt:6389:فرغرده: (6-)120۵۲-۸ (امف.) خبسانیده»
```


## [2026-09-06T02:14:59.158Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport io\nlines=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\n')\n# find leaf index for line 8136\ntxt='\\n'.join(lines)\n# count formfeeds up to line 8136\npre='\\n'.join(lines[:8136])\nprint('leaf idx approx', pre.count('\\f'))\nprint('\\n'.join(lines[8125:8175]))\nEOF"
}
```


### [2026-09-06T02:15:00.721Z] TOOL RESULT

```
leaf idx approx 257
را استعمال کنند و آن‌ببزرگی تخم کرفی‌است »
وکبود رنگ میباشد» و بغایت تلخ بود ۰ بهق و
برس را تافع است . و اکر بکوبند و دد بینی
زن آیتن بدمند بچه بندازد ؛ و بعضی گویند
غاد - با غن تقطه‌رار بر وزن نالچار »
هر چیزینم کشده و خسیده از آب با از خون
بود - و فرو شدن نم باشد بزمین و آمیخته - و
بهم پیوسته و سرشته را نیز گویند - و بمعنی‌بر
انگخته و تحريك کرده هم آعده است که بعربی
اغراء خوانند .
آغارد بفتح را وسکون دال بی‌نقطه,
بعنی بهم بيامیزد وسرشته کند و بر انگیزاند و
تحريك نماید - و سکون را بعنی سرشته کرد
وبهم بر آمیخت و تحرزيك نمود و برانگیزانید .
] غار۵ن س فتح دا و سکون نون .
یعنی سرشتن وبرانگیزانیدن و تحريك نمودن -
وفرو شدن و فروکردن هم باشد بزمین و غیره .
غار بدن - بروزن پاشایدن. بمعنی
آغاردن اس ت که سرشتن و تحربك نمودن وغبره
باشد - و فرء کردن نم بود بزمین با بر جای
۳
آغاز ب,بازای نقطه‌دار بروزن آواز .
بىمنی صدا و ندا باشد - و ابتدای کارها را نیز
گویند - و بمنی ضصد واراده هم آعدماست ۳ -
و امربایین عمتی هم هست نی قصد کن و ارادء
نمای . 3
آ غاه - بروزن‌آوازه ‏ دست‌افزارست
کفش دوزانرا - و دوالی را نیز گوین که مابن
چرم و روی کفش دوزندنا آب و خاكبدرون کفش
نوّود .
] غاز یف - - بکسر زا وسکون تعتانی
و دال ؛ بعنی ابتدا کرد و قصد و اراده نمود .
آغار بدن بروزن آشامدن » ,سنی
قصد و اراده نمودن - و اتداء کردن.
آغال - بسکون لام » پیشی آشفته
کردایدن و برآشفته ساختن باشد شخسی را بر
۴ - ۷۵۲۱۱۵۱۵۸۵ 5ز۳۱۷۵۳۵۵.
نی نوخود کی‌مرء آن‌باش ی کهخودرا چون‌خلیلشخصی دییگر - وبمعنی تحريك‌نمودن وبرشورانیدن
بجنگه هم هست که جربی اغراء گویند - وامر
باين معنی هم آمده است یمنی تحريك کن و
بشوران وناجاویده(۱) فروبردن رانیز گویندوبمبی
«بام» خوانند - و جابی باشد که در صحرا رکوه
بجهن. خوایدن کوسفندان‌وچارپابان دبگربکنند.
وخانهٌ زنبوررا نیز گفته‌اند - و بمعنی گرقتار کردن
چیزی باشد بر چیزی همچو چثم را بگرستن-
و بمعنی خیسیدن هم گفته‌اند ۱
غال بشه عم تام‌درختی‌است بیاریزر کی
و آنرا «سده» گویند . و پرآن چیز ها بودمانند
خربطه که براز بشه باشد وآنرا بشه خاته گویند
و آن‌درخت را بمربی «شجرالیق» خواتند ٩‏ .
```


## [2026-09-06T02:15:11.627Z] TOOL CALL #21: Bash

```json
{
 "command": "sed -n '1,50p' tools/ref_page.py"
}
```


### [2026-09-06T02:15:11.665Z] TOOL RESULT

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
```


## [2026-09-06T02:15:12.455Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '18555,18680p' incoming/BQT/BQT_v3_pages.txt"
}
```


### [2026-09-06T02:15:12.509Z] TOOL RESULT

```
‏فرع خوران ‎gost IE‏
‎abe‏ کنایه ازآدمیان است .

‏فرعون۱ © بکسراولوفتح عین‌وسکون
ثالی وواو ونون : پزبان عبری ‎cl‏ ولیدینمصعب
است واو اول فراعت مصربوده۷ - وبمعنی‌عتکیر
وس رکش باشد ۸ -

‎oF ‏و‎ gilt ‏بفتخ اول و سکون‎ - és
MSU SG ‏مرغ‎ Lany ‏قطمدار ؛ جوجه‎

‏فرغار ‎aad‏ بر وزن سرشار ۰ ‎we‏
‎ls‏ و نيك‌ترشده - وسرشته کردیدهوآغشته
باشد - و نام ترکی که اقراسیابش بجاسوسی
فرستاده ‎boy‏ معلوم ‎STAT‏ رستم چه‌مقدارلشکر

‏دارد .

‏دوم - (۳) چك : و شم طا .

‏مپذب الاسباء گوید : « الغوره .

‏فرشك ۰ ای ‎Sh‏ سه چهار انگور در هم بسته. » السامی فی‌الاسامی کوید : « الغورة » فرشك -
الخصلة , کوخك » در دستورالانه‌ممنی‌خصله را خوشة انگورنوشته » > فرهنگه نظام 4

‏۴ < فرش (هم) .

‏۴ مخفف «فرشیدورد © ‎Cpe)‏ رك : فهرست ولف .

‏۴ - (عر) > فرصاد (بکسراول ‎A‏ نود ‎(og)‏ با بارآن» ناتوت سرخ- ورنگی‌است سرخ»

‎.> ‏الارب‎ ate?

‎Pharaon= ۱‏ (فر) . دربونانی ‎Phara6n‏ سربانی

‎Fartés _ ©‏ ( پهلوان تورانی ) رك : فهرست ولف .

‏۵رنه) حبعی

‏_ محتمل است که‌کلمه ازسربانی وارد عربی ‎at‏ باشد. درقر آن نیز آمده مثلارلد:سورء

‎6۲۲۵ ‏«جغری‎ . 4٩ GT
‏ترجمه‌هژیر.تهران ۲۵۱۳۰۹ ببعد.‎

‏۷ راجم ‎Lele‏ مصرء رل: تاریخ‌ملل‌شرق. آلبرماله وژول ‎ANGI‏
‏۸ - ماخون ازعربی از: فرعنة بععتی‌تکبرورزیدن .

‎Lal? su SoM Lip - ٩‏ فرح بخایممجمه‌را بفین‌خوانده و آنلفظعربی‌است

‎.) ‏کور» ( فرهنگه نظلم ج‌هصلح بنقل ازسراج‎ deine

‏۴ - ر: فرغاردن,رك: فرغر.

‏فرشیدور ۰ فرفیدورد - بقتح اول و ‎ptt‏ در ‎-Frashavart syle‏ دراوتا

‏2 , و آن نام پسرکی کشتاسب و برادر اسفندبار است . رك : پشتها اص
‎Ae‏ ح و ۲۸۸ ؛ ‎Lp‏ ۳۳۷ و۳۹۳ - دیگر تلم ‎ay he aly‏ « قهرست ولف »- دیگر
نام دهقانی بزمان بهرام گور « فپرست ولف * .
[pdf page 258]
سووع و فرغور

فرغاد یدن ۱ = بوزن سر خاربدن + ۱
‎Loe‏ خوب تر کردن و خیسالیدن درآببوفیره | وش را بیز گویند که ‎hy‏ غدیرخوانند :*

باشد ۴ - و ‎gases‏ چوی آپ هم آجده ا ت-

- و بهم سرشتن وآغشته کردن باشد. فرغرده ۴ - بر وزن پرورده . ‎aT‏
‎ca - GES‏ اول وسکون تای‌ونالت | ‎oer‏ سرشته را کویتد .
پالف کشیده و بنون و جیم زدهء ماده کاوفربه پر .| ‎FP‏ * - بروزنکردن » جوی ‎last‏

گوشت راگویند - ومادمالاغ‌فربه ‎pal,‏ گفته‌اند؛ | کوبندکه تازه احدات کرده باشند و آب حرآن

و با جیم فارسی هم بلظر ‎etal‏ است ؛ و بسنی روان کنند .

گوبند این لفت ترکی است . ‎MES‏ » بروزن ‎Soll wip‏
‎GES‏ -بر وزن پرواله . نم ولابتی | بردرخت پیچد وبسبی مشقه کوند ‎٩‏ - وجیزی

است از ملك ماوراءالشهر ۴ مان سمرقند وچین | پلید و کندیده و بدبوی و متعفن و باخوش را

که آترا اندکان کویشد وممرب ‎OT‏ انسجانامت | ‎ps‏ کفته‌اند ۷ ؛ و ‎oth‏ ممنی با زای فارسی حم

- و نام کوهی هم‌هت که مردم ‎OTe lS‏ کوه | آمده است -

میشود وآن رستنیی ‎ath‏ که عربان ببروج (۱) گر ‎OE‏ - بروزن شرمنده» بممنی‌فرخنه
‎sls eal‏ ونام‌شمبه‌ایست ازموسیقی کهآ ترا است ‎ASS‏ عشفه ‎A‏ - وچیزی بدبوق وناخوش
‎gl‏ ند میخوانند . وکنده باشد ‎٩‏ .

فرغر = بفتح اول ‎My‏ بروزن‌صرسر, فرغور « بر وزن (۳) زنبور » بمعنی

‎eles‏ رودیرا کوبند که( » ) سیلاب از آنجا | تبهو ‎ath‏ و آن پرنده‌ایست مانندکبك لیکن‌از
گذشته باشد و درهرجایی از آن قدریآب‌ایستاده | کبك کوچکتر است *۱- و بمعنی جل هم‌آمده

‏(۱) صحیح : پیروح . ‎(x)‏ چش : که . (۳) چك : بوزن .

‏۱ - فرغردن و رك : فرغر . ۴ - رك : ممجم‌البلدان .
۴ - از : قر ‎ool) s+ (aye)‏ 01-8987 ( تر کردن ) * ولیامز
۷۹ :۳ و ۳۷۸ :۲ » رد : فرغردن » فرغرده ۰ فرغار » فرغاردن .
‎le JL‏ بادبه ‎tay‏ فرغری ."زان سا نکهه که گفت فکردند ‎Fark‏
‏باو ر کنیا کهبدبدمبچشم خویش ‎JEM‏ چون فرات ‎Why‏ چندفرخرش ۰
«خاقانی شروانی ۲۲۳-۲۲۲ (دروصف‌مناسككحج)».
۴ — اسم مفعول از « فرغردن > :
‎ole‏ اندر نور چون فرغرده شد . پس زعلت لور بابد قوم لد ۰ مثنوی‌مولوی «فرهنگهظام».
و رك ؛ فژغرده ‏ ® فرکن ‎Con)‏ . ورك : لفت فری ص ۳۹۸ ح ‎۰٩‏
‏۱ - ابا سرو نو در تك و پوی آنم که فرغند آسا (واری) ‎seme‏ بر .
« رودکی سمرفندی ۱۰۰۰ چاپ افسی * .
استاد هنینگه احتمال میدهدکه اصل > فژغندآسا » باشد . رك :
‎Henning, Two Central Asian words.p . 154, note ۰‏
۷ - استاد هنینگه ‎ag‏ : قژغند ‎IY‏ بممنی پلید وچ رکین مصحف < فرغند‌است.
‎A 8305, vol X. 1,۲۰ 102, note [ : 4,‏ : فرغند » وحاشيةٌ ‎٩‏ .
‎٩‏ -رك ‎dy -* Ww haley wig:‏ : جپانگیری « فرفور * .
6 فرفردی- ‎dite‏ وسوم وپنجم؛ از: فرغر(هم.)؛ ‎PII S SF Oss‏
[pdf page 259]
_ __ iat
: ‏است وآن پردده‌ای باشدکا کل‌دارشییه بگتجعكث‎
by ‏و‎ ٩ ‏بزرکتر است‎ een ‏از‎ Sal,
‏خوانند.‎ Gude ‏گوبند کموزق‌باشد وجریی‎ 5s ‏را‎
‎Adie ‏با واو مجپولبروزن‎ S98
‏خاموش و تن زده باشد - و تأخیر وتکاسل‎ ioe
. ۴ ‏وکاهلی در کارها را نیز گویند‎
‏فرغول ۴ - با واو مجنهول بر وزث‎
‏معقول» بمعنی غفلت وغافل شدن وتأخیرودرنگگ‎
. ‏و کاهلی در کارها باشد‎
gt ‏اول وسکون‎ KG © ۴ ‏فرغوی‎
‏بروزن دلجوی , مرغی است کوچك از جنس‌باشه‎
‏که‌بدان شکار کنند وبترکی قرغ وکویند.‎
‏دروش,بمعنی کهنه‎ Vinge ees
```


## [2026-09-06T02:15:36.451Z] TOOL CALL #23: Bash

```json
{
 "command": "python3 tools/ref_page.py BQT:1465 --image 2>&1 | tail -20"
}
```


### [2026-09-06T02:15:38.068Z] TOOL RESULT

```
گذشته باشد و درهرجاٍبی ازآن قدری آب‌استاده كبك کوچکتر است *۱- و بمعنی جل هم آمده
(۱) صحیح : ببروج - (۲) چش :که - (۳) چك : بوزن .
‎٩‏ * فرغردن و رك : قرغ . ۴ - رك : ممیم‌البلدان .
۴ - از : فر ( پیشوند )+ غر ( ساسکربت 8108۳ ۳ 810/1 ( تر کردن ) « وبلیامز
۹ :و ۳۷۸ :۲ رك : فرغردن » فرغرده » فرغار » فرغاردن -
سالی میان بادیه دیدند فرغری زان سان که‌هر که گفت نکردند پاورش
باور کنی‌مر[ که‌بد بدم بچشم‌خوش امسال چون فرات روان» چندفرفرش :
«خاقانی شروانی ۲۲۳-۲۲۲ (دروصف‌مناسلكحج)».
۴ - اسم مفعول از « فرغردن > :
علم اندر نور چون فرغرده شد ‏ پس زعلت نور یاید قوم لد . امثنوی‌مولوی «فرهنگه‌نظام».
و رك ؛ فزژغرده : ۵ -فرکن (هم.) . ورك : لفت فری ص ۳۹۸ ح ‎۰٩‏
‎٩‏ - ایا سرو نو در تك واپوی آتم که فرغند آسا (واری) پپیچم بتو بر .
رودکی سمرقندی ص۱۰*۰ چاپ لفی > .
استاد هنینگه احتمال میدهد که اصل « فزژغندآسا > باشد . رك :
.۰ 2016 , 154 . ۷۵۲۵۶۰۵ صقاقش 00۸۸۳۵1 1۳۵ موقامد 110
۷ - استاد هنینگه نود : #ژغند » لااقل بمعنی پلید وچر کین مصحف « فرغند»است.
رك : 1 2016 ,102 1,0۰ .26 |۷۵ ,82505 ۸ -ر4 : فرغند » وحاشية ‎٩‏ .
‎٩‏ -رك : فرفند. وحاشية ۷. *- رك : جهانگیری « قرقور» .
فرفردن- بختح‌اول وسوم وینجم؛ از: فرغر(هام.)؛ خیانیدن, تن کردن.ر4:فرغرده.
```


## [2026-09-06T02:15:38.073Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nlines=open('FRS_pages.txt',encoding='utf-8',errors='replace').read().split('\\n')\npre='\\n'.join(lines[:6800])\nprint('FRS leaf', pre.count('\\f'))\nprint('\\n'.join(lines[6790:6830]))\nEOF\necho \"=== MON ===\"; sed -n '6365,6400p' MON_part2.txt"
}
```


### [2026-09-06T02:15:39.676Z] TOOL RESULT

```
FRS leaf 163
                                     ‫‪۱‬‬

  ‫چون رخ منکشت آبگیر پرازچین‬                    ‫باد بهاری بآبکیر بر ‪ ۱‬آمد‬
                                      ‫‪۳۱‬‬
                                 ‫نی کی ‪۶‬‬                   ‫‪۱‬‬
‫جایی باشدکه از آنجا آب‌رفته باشد و هر جایی پارهٌ مانده باشده‬
                                                               ‫فرخی کوید‪:‬‬
                                ‫زرآیباگفتی همیبکوش آمد‬
                                                     ‫د‬
       ‫که بادشاها درب توبی ومن فرغر‬

                                      ‫‪۳‬ام‪۰‬ا‬
‫چیزی باشد کهدر جامه مالند تا رنگ وصبقل کیرد » عماره گوید‪:‬‬


                            ‫سوار بود براسبان چو شیر بر سر کوه‬
       ‫پیاده ‪ ۹۳‬بخون داده جامه ‪ ۳‬آهار‬

                                 ‫‪۶‬‬       ‫‪2۰‬‬

                                     ‫مندور‬
                                                ‫گوید ‪:‬‬   ‫غحکین بود [جلاب*‬
   ‫بشادکامی نزديك شونه"مندوری]‬                ‫بهارخرم نزديكآمداز دوری ‏‬


                                                                      ‫کت‬
‫‪ - ۲‬فرغر آبی که از رود جدا شود و آبدانی گردد ‪ ۰‬س ‪ :‬فرغر‬         ‫‪:‬من‬    ‫‪ - ۱‬س‬

‫زد باز گیرند ( بدون مثال) » تریفاتی کهدر انو س هست‬
                                                 ‫جوی آبباشد کهارو‬
   ‫است ‪.‬‬      ‫ه‬‫دنی‬
                 ‫عومع‬  ‫درست باتعرف ع مطابقت ندارد و ظاهراً لفت فرغر به‬
                    ‫آر د‬
‫(در حاشبه )‬    ‫س (مثل متن ) ‪۰‬‬     ‫‪4‬‬      ‫‪ - ۴‬اینلت نقط در ع و س هست ‪.‬‬
  ‫ر‬
  ‫‪۲‬د‪-‬‬      ‫‪-‬یدی‪ :‬جلاب نجاری‬
                          ‫رش‬           ‫ال )‬       ‫ددهو(ن‬
                                                       ‫بمان‬
                                                          ‫مندور متحیر بود ودر‬
                      ‫‪ - ۷‬اینلفت فقط در ع هست ( بدون مثال ) ‪.‬‬         ‫اصل ‪ :‬ز‬
=== MON ===
شرعود: (2۷)0 ۲6۲ [معر. سر.] (ا.) 
عنوان هر یکت از پادشاهان مصر؛ ج. فراعنه. 
هر شخص ستمکار و تباهکار. 

فرعی: 9۳-1 [غ. ف.] (ص‌نسب.) منسوب به 
فرع. آنچه که فرع باشد؛ مق. اصلی. 

فر غار: ۰02 [فرغر» فرغاریدن] (ص‌مف.) 
خیسانیده» نیک تر شده. سرشته گردیده؛ 
آغشته. 

فرغانج: لمورزود؟ [تر. < فرغانج] (.) مادة 
(گاو» خر) فربه پر گوشت. 

فرغر: ۵0۵۲] [- فرغر» فرغود» نفرغاردن» 
فرغاریدن) جوی آب. جایی که آب از آن 


۱ ۱ ٩ 
گذشته و مقدار کمی آب بجا مانده باشد؛‎ 
خشک رودی که سیلاب از آنجا گذشته‎ 
باشد و در هر جایی از آن قدری آب ایستاده‎ 
باشد. آیگیر غدیر» شمر.‎ 

فرغرده: (6-)120۵۲-۸ (امف.) خبسانیده» 
نیکك تر کرده. آغشته. خمیر کرده» بهم 
فرعن: 2 [- فرکن] (.) جوبی که تازه 
احداث کر ده و آب در آن روان کنند. 

فر غند: ۵ [- فرغنده] (ص.) پلید؛ بد. 


فرغول: ال [- فرغل] (.) تخیر 
درنگ. غفلت..
```


## [2026-09-06T02:16:04.124Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT zarš ===\"; grep -n \"zarš\\|zarəš\\|zarsayamna\\|zarshayamna\\|zarštva\\|zarstva\" BRT.txt | head -20"
}
```


### [2026-09-06T02:16:04.225Z] TOOL RESULT

```
=== BRT zarš ===
11360:—  jvasHt  nSit  bvat  asava  vnsasHp  tüSti bax/aiti (sd.)  vahistahe  at3kSusY.^,6i;  — fraia  fraydit  . .  ä  sangaäbyasa^  apn  ä inubyoicit  .  .  3  matiyqnas^t . .  ä  ripr^m- zasät  äpS  Y.6.aj;  —  isavasHt  al^qm  .. ar/tayascit  .  .  zarstvaat  . .  kantacit . .  va- zracit  . .  Yt.  10.  39  f.  a)  das  zweite  ^ steht  unregelmässig:  kasSusÜli  nä  ..  isvä- (sd.)(?i/'*  hqs  paraos  Y.  47.  4.  Anhang, lU  wechselt  mit  iS:  tä^^.,vasfml  anyäüä vTduyl  Y.  44. 4.         2)  wie   bei   I ;    aber
```


## [2026-09-06T02:16:04.989Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD ghers ===\"; grep -n -i \"ghers\\|gher-to\\|ghertom\\|horror\\|bristle\" AHD_watkins1985.txt | head -30"
}
```


### [2026-09-06T02:16:05.071Z] TOOL RESULT

```
=== AHD ghers ===
219:ghers-. 2. Lengthened-grade form
323:outlaw”), in: a. Old English bannan, to summon, pro- claim, and Old Norse banna, to prohibit, curse: BAN}; b. Old French ban, feudal jurisdiction, summons to military service, proclamation, Old French bandon, power, and Old English gebann, proclamation: BANAL, BANNS; ABANDON; C. Old French banir, to banish: BAN- ISH; d. Late Latin bannus, bannum, proclamation: Ccon- TRABAND; @. Italian bandire, to muster, band together (< “to have been summoned”): BANDIT. 4. Suffixed form *bha-ni in Germanic *b6dni- in Old Norse b6n, prayer, request: BOON!. 5. Suffixed form *bhd-ma in: a. Latin fama, talk, reputation, fame: FAME, FAMOUS; DEFAME, INFAMOUS; b. Greek phémé, saying, speech: EUPHEMISM. 6. Suffixed o-grade form *bhd-nd in Greek phéné, voice, sound, and phénein, to speak: PHONE, -PHONE, PHO- NEME, PHONETIC, PHONO-, -PHONY; ANTHEM, (ANTI- PHON), APHONIA, CACOPHONOUS, EUPHONY, SYMPHONY. 7. Suffixed zero-grade form *bha-to- in Latin fatéri, to acknowledge, admit: CONFESS, PROFESS. 8. Greek blas- phémos, evil-speaking, blasphemous (first element ob- scure): (BLAME), (BLASPHEME), BLASPHEMOUS. [Pok. 2. bha- 105.] bha-bha-. Broad bean. 1. Latin faba, broad bean: FAVA BEAN. 2. Variant form *bha-un- in Germanic *bauné in Old English béan, broad bean, bean of any kind: BEAN. [Pok. bhabhé 106.] bhad-. Good. 1. Germanic (comparative) *batiz6 in Old English betera, better: BETTER. 2. Germanic (superla- tive) *batistaz in Old English bet(e)st, best: BEST. 3. Ger- manic noun *b6¢6 in Old English bét, remedy, aid: BooT?. 4. Germanic verb *batnan, to become better, in Old Norse batna, to improve: BATTEN!. [Pok. bhdd- 106.] bhag-'. To share out, apportion, also to get a share. 1. Greek phagein, to eat (< “to have a share of food”): -PHAGE, -PHAGIA, PHAGO-, -PHAGOUS. 2. Extended form *bhags- in Avestan bakhsh- in Persian bakhshidan, to give: BAKSHEESH, (BUCKSHEE). [Pok. 1. bhag- 107.] bhag-. Sharp. Suffixed form *bhag-ro- in Greek phag- ros, whetstone, also a name for the sea bream: PORGY. [Pok. 2. bhag- 107.] bhaghu-. Arm. Germanic *bdguz in Old English bdg, boh, bough: BouGu. [Pok. bhdghii-s 108.] bhago-. Beech tree. 1. Germanic *b6k6, beech, also “beech staff for carving runes on” (an early Germanic graphic device), in: a. Old English bdc, written docu- ment, composition: BOOK; b. Middle Dutch boek, beech: BUCKWHEAT. 2. Germanic *bdkjdn- in Old English béce, beech: BEECH. [Pok. bhdgo-s 107.] bhar-. Also bhor-. Projection, bristle, point. 1. Suffixed o-grade form *bhor-so- in Germanic *barsaz in Old English bzrs, perch, bass (a fish that has a spiny dorsal fin): BASs!. 2. Suffixed zero-grade form *bhAr-sti- in Germanic *bursti- in Old English byrst (> Middle Eng- lish bristel), bristle: BRISTLE. 3. Extended zero-grade form *bhrs- in: a. Germanic *bur- in Swedish borre, bur, perhaps akin to the Scandinavian source of Middle English burre, bur: BUR}; b. suffixed form *bhrs-dh- in Germanic *bruzd-, point, needle, in Old Norse broddr, spike: BRAD; C. suffixed form *bhrs-ti- in Latin fastig- ium, summit, top, extremity: FASTIGIATE, FASTIGIUM; d. possibly suffixed form *bhrs-tu- in Latin fastus, fasti- dium, disdain (from the notion of prickliness): FASTIDI- ous; e. suffixed form *bhrs-tio- in Russian borshch, cow parsley: BORSCHT. [Pok. bhar- 108.] bhardha. Beard. Possibly related to bhar-. 1. Germanic *bardaz in Old English beard, beard: BEARD. 2. Ger- manic *bard6, beard, also hatchet, broadax (the associ- ation of beard and ax is attested elsewhere in the Indo-European family; both were symbols of patriarchal authority), in Old High German barta, beard, ax: HAL- BERD. 3. Latin barba, beard: BARB!, BARBEL, BARBEL- LATE, BARBER, BARBETTE, BARBICEL, BARBULE; REBARBATIVE. [Pok. bhardhé 110.] bhares-. Also bhars-. Barley. 1. Germanic *barz- in Old
524:gher-’. To shine, glow; gray. Hypothetical base of various Germanic forms. 1. Germanic *gréwaz, gray, in: a. Old English greg, gray: GRAY; b. probably Old English grighund, greyhound: GREYHOUND. 2. Germanic *gris- Jaz, gray, in: a. Old French gris (> French gris), gray: GRISAILLE, (GRISETTE), (GRISON), GRIZZLE; AMBERGRIS; b. Medieval Latin griseus, gray, grayish: GRISEOUS. [Pok. 3. gher- 441.] gher-4. To scrape, scratch. 1. Extended zero-grade form *ghr(e)-k- in: a. Greek kharax, a pointed stake, also a kind of sea bream: CHARACIN; b. Greek kharassein, to sharpen, notch, carve, cut: CHARACTER, GASH. 2. Ex- tended form *ghers-.in suffixed zero-grade form *ghrs-to- perhaps (but unlikely) in Sanskrit ghattah, ghat: GHAT. See also extensions ghréi- and ghréu-. [Pok. 2. gher- 439.] gher-5. To like, want. 1. Suffixed form *gher-n- in Ger- manic “*gernjan in Old English giernan, gyrnan, to strive, desire, yearn: YEARN. 2. Extended form *ghré- possibly in: a. Germanic *gréduz, hunger, forming *grédagaz, hungry, in Old English grédig, hungry, covetous, greedy: GREEDY; b. Greek khré, it is necessary, whence krésthai, to lack, want, use: CATACHRESIS, CHRESARD, CHRESTOM- ATHY. 3. Suffixed zero-grade form *ghr-td- in Latin hortari, to urge on, encourage (< “to cause to strive or desire”): HORTATIVE; EXHORT. 4. Suffixed zero-grade form “ghr-i- in Greek kharis, grace, favor: CHARISMA; Eucnarist. [Pok. 1. gher- 440.] ghere-. Gut, entrail. 1. Suffixed form *ghero-no- in Ger- manic *garn6, string, in Old English gearn, yarn: YARN. 2. Suffixed form *ghero-n- in Latin hernia, “protruded viscus,” rupture, hernia: HERNIA. 3. Suffixed o-grade form *ghoro-d- in Greek khordé, gut, string: (CHORD?), CORD, (CORDON); HARPSICHORD, TETRACHORD. 4. O-grade form *ghors- in Greek khorion, intestinal membrane, afterbirth: CHORION. 5. Possible suffixed zero-grade form *ghr-u- in Latin haruspex (-spex, “he who sees” < *spek-, “to see”; see spek-), “he who inspects entrails,” diviner (but perhaps borrowed from Etruscan): HARUSPEX. [Pok. 5. gher- 443.] ghers-. To bristle. 1. Extended zero-grade form *ghrzd-, prickly plant, in: a. Germanic *gorst- in Old English gorst, furze, gorse: GORSE; b. Latin hordeum, barley: ORGEAT. 2. Lengthened-grade form *ghér(s)- in Latin hér, ér, hedgehog: URCHIN. 3. Suffixed lengthened-grade form *ghér(s)-ika in Latin ériica, caterpillar: ROCKET?. 4. Suffixed full-grade form *gher-tu-, remade to *hirsu- in Latin hirsitus, bristly, shaggy, hairy: HIRSUTE. 5. Suf- fixed full-grade form *ghers-ko- in Latin hispidus (prob- ably a dialectal borrowing), bristly, shaggy, prickly: HISPID. 6. Suffixed o-grade form “ghors-eyo- in Latin horrére, to bristle, shudder, be terrified, look frightful: HORROR; ABHOR, ORDURE. 7. Suffixed full-grade form *ghers-o- in Greek khersos, dry land: CHERSONESE. [Pok. Bhers- 445.] gheslo-. Seen by some as a base for words meaning “thousand.” 1, Suffixed form *ghesl-yo- in Greek khilioi, thousand: CHILIAD, KILO-. 2. Latin mille, thousand, which has been analyzed as *smi-, “one” + a form *ghsli-, is of obscure origin: MIL!, MIL2, MILE, MILLE- NARY, MILLESIMAL, MILLI-, MILLIEME, MILLION; MIL- FOIL, MILLENNIUM, MILLEPORE, MILLIARY, MILLIPEDE. [Pok. ghéslo- 446.] ghesor-. Hand. Reduced form “ghesr- in Greek kheir, hand: CHIRO-; (CHIRURGEON), ENCHIRIDION, (SURGEON), SURGERY. [Pok. 1. 8hesor- 447.] gheu-. To pour, pour a libation. I. Extended form *gheud-. 1. Zero-grade form *ghud- in Germanic *gut- in Old English guttas, intestines: GuT. 2. Nasalized zero-grade form *ghu-n-d- in Latin fundere, to pour: FOISON, FONDANT, FONDUE, FONT, FOUND2, FUNNEL, FUSE?, FUSILE, FUSION; AFFUSION, CIRCUMFUSE, CON- FOUND, CONFUSE, DIFFUSE, EFFUSE, INFUSE, PERFUSE, PROFUSE, REFUND!, (REFUSE!), (REFUSE?), SUFFUSE,
1208:ABAFT apo- ABANDON bha-2 ABASE bassus ABASH bat- ABASIA gWa- ABATE battuere ABBREVIATE mregh-u- ABDICATE deik- ABDUCENS deuk- ABDUCT deuk- ABELE albho- ABERRATION ers-1 ABET bheid- ABEYANCE bat- ABHOR ghers- ABIDE bheidh- ABJECT yé- ABJURE yewes- ABLATION  tele- ABLAUT apo-, kleu-1 ABLE ghabh- ABLUTION leu(@)- ABNEGATE ne ABNORMAL gné- ABODE bheidh- ABOLISH al-3 ABORT er-! ABOUND wed-1 ABOUT ud- ABOVE upo ABRADE réd- ABRIDGE mregh-u- ABROGATE reg-1 ABROSIA gWere-4 ABRUPT reup- ABSCESS ked- ABSCISE kae-id- ABSCOND dhé-1 ABSENT eS- ABSOLUTE leu-1 ABSOLVE feu-1 ABSORB srebh- ABSTAIN ten- ABSTRACT tragh- ABSTRUSE treud- ABSURD swer-2 ABULIA gWele-1 ABUT bhau- ABYSS gWadh- ACANTHO- ak- ACANTHOPTERYGIAN pet- ACANTHUS ak- ACAPNIA kwép- ACCEDE ked- ACCELERATE kel-3 ACCENT kan- ACCEPT kap- ACCESS ked- ACCIDENT kad- ACCIPITER Oku- ACCLAIM kele-2 ACCLIVITY klel- ACCOLADE kwel-1 ACCOMMODATE med- ACCOMPLISH pele-1 ACCORD kerd-1 accosT kost- ACCOUNT peu- ACCRUE_ ker-3 ACCUMBENT keu-2 ACCUMULATE keue-2 ACCURATE cira ACERATE ak- ACERB ak- ACETABULUM ak- ACETIC ak- ACETUM = ak- ACHALASIA ghé-
1324:BRIO gWere-2 BRIOCHE bhreg- BRISANCE bhréi- BRISTLE bhar- BRITTLE bhreu-1 BRONCHIECTASIS  ten- BRONCHO- gWere-4 BRONCHUS gWere-4 BRONTOSAUR bhrem-! BROOD bhreu-2 BROOK? bhriig- BROOM bhrem-2 BROTH bhreu-2 BROTHEL bhreu-' BROTHER bhrater- BROW bhri- BROWN bher-3 BROWSE bhreus-1 BRUIN bher-3 BRUISE bhreus-2 BRUMAL mregh-u- BRUNET bher-3 BRUT gWere-2 BRUTE gWere-2 BUBO beu-! BUCCAL beu-1 BUCEPHALUS gWou- BUCK! bhugo- BUCKAROO wak- BUCKBOARD beu-! BUCKLE! beu-! BUCKLE? beu-1 BUCKSHEE bhag-' BUCKWHEAT bhago- BUCOLIC gou-, kWel-1 BuppHA bheudh- BUDGET bhelgh- BUDGE! beu-1 BUGLE! gWou- BUGLOss gldgh- BUILD bheue- BULGE bhelgh- BULIMIA gWou-, leia- BULK! bhel-2 BULL! bhel-2 BULL? beu-1 BULLA beu-1 BULLATE beu-1 BULLET beu-! BULLETIN beu-1 BULLION beu-1 BULLY? beu-1 BULWARK bhel-2, werg- BUNCO bheg- BUND! bhendh- BUND? bhendh- BUNDESRAT ar- BUNDLE bhendh- BUNG peuk- BUNGLE bheg- BUPRESTID gWou- BUR! bhar- BURDEN! bher-1 BURG bhergh-2 BURGESS bhergh-2 BURGHER bhergh-2 BURGLAR bhergh-2 BURGOMASTER bhergh-2 BURIAL bhergh-! BURIN bher-2 BURN! gWher- BURN? bhreu-2 BURNET bher-3 BURNISH bher-3 BURSA bursa BURSAR bursa BURSE bursa BURST bhres- BURY bhergh-1 BUSHEL? bhau- BUSK! busk- BUSK? s(w)e-
1348:CHASM ghai- CHASSIS kap- CHASTE kes-2 CHAUDFROID kele-1 CHEAP caupd CHECK tké- CHECKMATE tké- CHEER ker-! CHEESE? kWo- CHEETAH kWeij-2, skai- CHEILOSIS ghel-una CHELICERA ker-1 CHELONIAN gheli- CHEMOTROPHY threph- CHENILLE kwon- CHENOPOD ghans- CHERISH ka- CHERNOZEM kers-1 CHERRY ker-6 CHERSONESE ghers-, sna- CHESS’ kap-
1565:GOAD ghei-1 GOAT ghaido- GOD gheu(e)- GODSEND sent- GOFFER webh- GOLD ghel-2 GOLIARD gWel-3 GOMPHOSIS gembh- -GON genu-! GONAD gene- GONFALON gWhen-1 GONIOMETER genu-1 GONIOMETRY genu-! GONION genu-! GONO- gena- coop ghedh- GOOSE! ghans- GORE! ghaiso- GORE? ghaiso- GORGE gWere-4 GORGET gWera-4 GORSE ghers- GOSHAWK ghans- GOSLING ghans- GOSPEL spel-3 GOSSIP s(w)e- GOUACHE akWa- GOWAN ghel-2 GRAB! ghrebh-1 GRABEN ghrebh-2 GRACE gWera-3 GRACKLE gera-2 GRADE ghredh- GRAFFITO gerbh- GRAIN gre-no- GRAM! § gerbh- GRAM? gre-no- -GRAM gerbh- GRAMA gras- GRAMINEOUS_ gras- GRAMMAR gerbh- GRAMPUS_peisk- GRANADILLA gfe-no- GRANARY gre-no- GRANDILOQUENCE tolkw- GRANGE gre-no- GRANITE gr@-no- GRANT kerd-1 GRANULE gre-no- GRAPE ger-2 GRAPH gerbh- -GRAPH gerbh- -GRAPHER gerbh- GRAPHIC gerbh- GRAPHITE gerbh- -GRAPHY gerbh- GRAPNEL ger-2 GRAPPA ger-2 GRAPPLE ger-2 GRASP ghrebh-1 GRAss_ ghré- GRATE! grat- GRATE? kert- GRATEFUL gWere-3 GRATIFY gWere-3 GRATIS gWera-3 GRATITUDE gWero-3 GRATUITY gWera-3 GRAUPEL kreup- GRAVE! ghrebh-2 GRAVE? gwWera-2 GRAVES ghrebh-2 GRAVEL ghréu- GRAVID gWera-2 GRAVURE ghrebh-2 GRAY gher-3 GRAYWACKE wegh-
1621:HIRSUTE ghers-
1623:HISPID ghers- HISTIOCYTE sta- HISTO- sta-
1648:HORN ker-1 HORNBEAM ker-1 HORNBLENDE ker-1 HORNET ker-1 HORNITO gWher- HOROLOGE yér- HOROLOGY yér- HOROSCOPE spek-, yér- HORROR ghers- HORST kert- HORTATIVE gher-5 HORTICULTURE gher-1 HOSE (s)keu- HOSPICE ghos-ti- HOSPITAL ghos-ti- HOSPITALITY ghos-ti- HosT! ghos-ti-
1996:ORDURE ghers- ORE aurum
1997:ORGAN werg- ORGANOLEPTIC (s)lag¥- ORGANON werg- ORGASM wrdg- ORGEAT ghers- ORGY werg- ORIENT er-1 ORIFICE 6s- ORIFLAMME aurum ORIGIN er-1 ORIGINAL er-! ORINASAL 6S- ORIOLE aurum ORLOP klou-, uper OrMaAzD ansu-, men-1 ORMER mori-, ous- ORMOLU aurum, mele- ORNAMENT ar- ORNATE ar- ORNITHO- oF OROIDE aurum OROTUND 6s- ORPHAN orbh- ORPHREY aurum ORPIMENT aurum ORT ed-, ud- ORTHO- wrddh- ORTHODOX dek-1 ORTHOGONAL genu-1 ORTHOPEDICS pau- ORTHOSTICHOUS _steigh- ORTHOTICS wrddh- ORTOLAN gher-! os! Os-
2197:ROBE reup- ROBLE reudh-1 ROBORANT reudh-1 ROBOT orbh- ROBUST reudh-1 ROCAMBOLE bhel-2, ruk-1 ROCHET ruk-1 ROCKET! = ruk-1 ROCKET? ghers- ROCKETSONDE swem- ROD reudh-2 RODENT réd- RODEO ret-
2437:UNITY oi-no- UNIVERSE 0i-no-, wer-3 UNIVOCAL wekw- UNKEMPT gembh- UNTIL ant- UNWITTING weid- UP upo UPANISHAD sed-1, upo UPBRAID bherek- UPROAR kere-, upO UPSILON bhes-! URCHIN ghers- UREDO eus- URETER wers-2 URETHRA wers-2 URETIC wers-2 URGE wreg- -URGY werg- -URIA wers-2 URINE wér- URO-! wers-2 URO-2 ors- URONIC wers-2 -UROUS ors- URSINE rtko-
```


## [2026-09-06T02:16:14.488Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"aufstr.ubend\\|aufstraubend\\|Federn\" BRT.txt | head -20; echo \"---zars---\"; grep -n \"zars\\|zarS\\|zarš\" BRT.txt | head -20"
}
```


### [2026-09-06T02:16:14.560Z] TOOL RESULT

```
7722:Pa.;  xrSs  parr  'mit  Hahnenfedern'.
9251:srayä  voumkaiaya  Y,  65. 4;  —  ys  haaiay-j  S/-'^v^'^'jU^'ond''zD"'"w',/irLter ...va  uruassayat  '«o»  Yt,5.  131;  —  ^-i  HriÄ^-^  No^T).  -  mp,  fl'ü.  Tu  V.'s  49" rasmanS  hqm.ststse  (sd.)  ^5  ^'na  ">  J'  karkäi,  vgl.  np.  (Npa,)  kargas. iHndayänti  Yt,  jj.  39;  —  yaoz)nH  »aA'«j.*kahrkäs5.parana-"  Adj. 'mit  Federn •«ff  (NP.)'>  rasmans  Ytio.36.  2)  zeitlich  ^  des  (Vogels)  Kakrklsa  versehen':  isunqm (nur  Komp.).  ^-paranum'^  Yt/o.isg.
13957:mit  a  'auf-,  mit>J  'fort-',  mit  vi  "hin  '"ai'hs  *maxUJt7hrpa  tr^aitya'K.^owm. und  herflattem':  dva  *alwi>S>n  dva  *vf^B.-  herzugeflogen  von  Norden  her  in  abscheu- i»n  dva  *frd^5i>n  "die  zwei  (Federn)  ^  ""^lier  Fliegengestalt"  V.  7. 2;  —  cvantim sollen  auf,  die  zwei  sollen  hin  und  her, '  ^«J'"''^'*  ^rväiitm  . .  as'a  druxl .  .  upa.- die  zwei  sollen  fortflattem"  Yt  1.^.45.        .dvasaiH  V.7.3;  1,4.  a)   mit  Angabe
16128:•  j.  paradiLvarah-  Adj.  'mit  breiter '  °ni '*  vtoärayöis  avi  fa^am  kaiarascit Brust,  breitbriistig':  pay»/,.''z'iir^(NSm)""vier  Federn  sollst  du  verteilen  auf  den YLJ5.54.  ]Weg'*  nach  beiden  Seiten  hin"  Yt/4-44;
16201:•  '].  pflSö-parana-  Adj.  'des  Federn  weit
20089:fliegen':  dz'a  ämarvtsn  dva  vJmamin  äva framanssn  (statt  Du.)  "die  zwei  (Federn) sollen  auf,  , .  hin  und  her, . .  fortfliegen" Yt.  14.  4S-
27989:•  j.  zarSayamna-')  Adj.  'die  Federn  auf- stikubend':  tmnyahe  . .  väryynaAe  . .  yS vazaite  °nB  ayrqm  usaitim  usaahtnt  "des Vogels  K,  der  ums  erste  Morgenrot  fliegt, seine  Federn  aufsträubend"  Yt  i4-  ao.
---zars---
2472:dalvil  . .  atibyö  kam  Y.44.20;  46.12;  — li  narS..aeiqm  nmäna  Yt.i~.yC;  g— 14.^, J0.39f.s,  33,Y./j.3,j7.37,Vr.//.i9,V.2, 43-J.i4,Ä4i,  12.1, 13.50,  i5.22,FrV/. 10. 40,  N.<S'5; — g3ui..ya  dar>nlhu  mi^rS.- drujqm  ..frazarsta  (sd.)  aglqm  rai'iya  .. hiit»nte  Yt. /o.  38;  —  vTspanqmca  , .  asae- nqm  aiaoninqmca  .,  vUpanqmca  allqm  za- ra'iuStnm  ..  *susruma ikatsim  Yt.Jj.148; —  a^qm  anyS  N.  61,  62;  —  aifam  aOiai»- kam  .  .  adqmcH  S  ahmt  .  .  vicC^ei  (sd.) aipT\.32.i;  30.1,  8,55.9;  —  haxays .. astvat.gr3take  .  .  assu  paro  fräntmlite aismü  Ytiff.g$;  — gä^a  . .  yezi  argAqm *Syutnpe  väUm  framaraiti  N.  42;  —  xi paiti  apqm  .  .  a^ra  atthqm  V.  y.  5 1 ,  Y. 6Ä7;  Yl/j.68;  —  duzvarmanhS  .  .  rä- mqmcä  J//'"'  dadätu  V.  ^3.  8 ;  —  yaia  ta r  ,  ,  minghäeä  .  .  yH  vohü  .  ,  a'iä  %WJ Si/'"'  yazamaide  Y.  j(?.4;  —  karapsAsaJ (sd.)  kfvitäsca  . .  töi  abyH  (AbL)  bairyänts (sd.)  .,  Y.52. 15; — spuda..kuir3  ayä.. Y.44-I5;  30.6,  3t.io;  —  /J  mainyn  .  . ascä  (GD.)  .  .  Y.30.3;  —  Gen.  in  Ver- bindung mit  hava-i  zasta  hl . .  frasniöa- v paityesii  V.22.7  — 13;  /.z;- — \y"t  aSahe  yat  apirmäyükahe  ahe  hava- aiwySr3hafi?m,.äat  aiijhi  ahi  aiwyästö  Y.  _v(7«  tütroö  "die  Hände  ..  des  Kindes  an ij.zb;  — ahur>m  ..  ahyä  x!a~i:räc3  ..  *hva- 1  dessen  Leib"  V.itf,  7  (?)  "';  —  dgL,  zugleich paphsiica  (sd.)  lim  .  .  yasämaidi  Y.  J7.  vorausweisend:  astvatjr3iö  ..  kB  ..  aiike if.;  —  sraosim  ..yazamaide  ahe  raya  . .  j  haxayB  /räyente  astvat.iritahe  Yt.  ip.  95: aiÄke  ama  ,.  ahe  yasna  ..  t?m  yai3i  "den '  - —  dalnqm  .  .  yao:dai%xSa  ai:a  sT  aiAka Sr.  .  .;  ob  seiner  Pracht  .  ."  Y.  57.3;  Yt.  yaoidaitii  ..  havaya  .  .  dainayä  Y.io. J-i^i  5i  9  (statt  fem.!);  —  noii  kl  anyö\i9.  a)  spez.  auf  das  Subjekt  des  gleichen urva  kaum  urvämm  paiti  irista  (sd.)  ^a-|Satzes,  Reflexivum:  ka%S  .  .  gqm  Ha- zaiti  xraosyü(a{%t^voyaca*a>»he^^.*at3hr^^  sSil  y}  kirn  ahmai  ..  stsi  usyaj  (sd.) Y.  13.9;  —  fravasayS  . .  ankam  raya  . .  Yt  ".  .  qui  eam  sibj  .  .  esse  cupiat"  Y.  ^o.  2 ; 13.2, 14—18"';  — gunäayäi  ..  za/an  ta/-  ^  —  nsit  sp>ntqm  d3r?st  (sd).  akmai  stöi San  (sd)  aya^'*  masJY.3.32;  —  vac?  ..\armaitlm  Y.4^.2;  —  hvJ  tat  n3  ..  ak- yii  . ,  akmai  straohm  dqn  Y.  45. 5 ;  —  |  mai  "'  dazdl  (sd.)  Y.  5/.  1 9 ;  —  aada  (sd.) ustä  ahmst  yahmai  .  .  kakmaicTt  . .  atca  \  vinzyötüca  It  akmai  fracä  vatöyBtü  (sd) <ihmai  Y.  43. 1  f ;  —  gavöi  . .  ha  %X  to\lt  alibyB  yöi  .  .  "..  sibi  (ipse)  . ."  Y.  J5.  6; huisii»m3  .  .  dal  .  .  at  ahyäi  .  .  masda  \- —  at  hT . .  /ravanll  (sd.)  vasirim  ahyai orvara  vaxsat  Y.4S-6;  31-9;  —  raya  ..\fntyant3m  Y.jj.  10;  —  nSit  ta  Im  x^3ui koya  aiiiAä  raiavö  Y.iff.iS;  *YyX.  50; — {vaipyö  .,  zara'iuhrtm  ..  Ayat  akml'^ paoiryö  gairis  . .  akmat  haca  garayO  tu- 1  urüraost  astö  hyat  , .  v3z3  (sd,)  Y.  31. uxiyqHYt.ig.\i.;  34,80;  —  hö  nBit..*/r3-\  12.  aa)  Der  Gen,  vertritt  dann  die  ent- nJmaite  ,.  /rä  ahmst  parö  ..  «jÄion/i;  j  sprechendeFormdeslat  suus:  airj  *i'jiri»i Y. 57-18,  ungeschickt  benutzt  Ytp.4;  lo.  baraiti  mi>akvac3  vä  irvivaca  (sd.)  vä.. 117;- —  *haltuma  . .  kacaiti  dim  . .  astica  akyl  zaridaca  manat»kac3  ", .  ex  suo  (uter- ahmi  avavat;^arin6  yäi:a  yat..Yx.ig.(>Z;\c^^)  corde  et  animo"  Y.ji.ti; —  akya —  :^aitu/  . .  vtrizifum  mat  airyamnä  . .  \xrata  frö  ma  sastB  (sd.)  vakistä  Y.  45. 6  ;
5121:•  j.  nSit  aitahe  uzarsnS  nai6a  varS  ava- väite  (3S.)  P.5^:-?-.
5993:azarsäant-
7477:•  g.  a-skitay-  f.  'Sichanschliessen,  An- schluss  (an  — )'t  ka%a  masdn  .  .  zarsm (sd.)  carärii  kacä  xlmat  *'-slai(im ''  xhna- kam  hyatiä  . .  "mein  Ziel  .  . :  das  Sich- anschliessen an  euch''  und  dass  .  ."  Y. 44- 17-
8845:yäil  pmsäi  (sd)  dngvä  vä  Y.  44.  u; jo.i;  —  ks  kvS  yS  .  ,  \.46.g;  —  koste asavä  urva^sY. 46.14;  —  kat  tSi  räzarS Y.34.\i;  —  kat  tat  dqma  ..  Y.ij.i,  5;
10910:masista  xsnaoma  x'nävayäliV.3.iz;g.^2^; —  äai  tum  nishti>ail..ttar»m^a  asavamm kuxsnvqnS  H.2.13,  Vyt55(wo  ^kjt/h- vänB)-,  —  yS  neu  narsm  aiavamm  .. xsnaosta  vä  xsnävayeite  va  '2.4g;  —  ya- '^raca  x^nätS  asavaYi-i^.^C;  —  xi'nüta- htcit  atbislaAe  i&A.)  ..  manS  yaezayäti'^X. /O.iii;  —  xsnüiS  (NPm.)'*  asdonqm urväfßs  pärayeinli  V. /p.31;  —  yat  alsS nä  .  .  haca  alibyS  nmanaHbyS  xsnütS aUii'ß parayäl  V.5.39;  —  ka%a  ^wa mazää  xsnaosäi  aAurä  "wie  kann  ich  dich zufrieden  stellen,  o  AfAA.f"  Y.46,1;  — ndii  xhtSvayeili  ahurim  mazäqm  .  .  ys mazdqm  tarS  manyete  \t  lO.i^q;  6.4;  — yagcä  xsnaespn  (3PKA.)  ahursm  Aaihyäii /y/joianäi/  fraorit  mazdqm  "und  die, welche  gern  mit  rechtem  Tun  AcAÄhM. zufrieden  stellen"  Y,_jo.  5;  —  tistrjm  .. yj  äa\äiti  kuxlnvqnäi  .  .  ayapta  jaio- yantäi  . .  maiyai  ".  .  dem,  der  (ihn)  zu- frieden stellt  .  ."  Yt  &  49;  7J.  24;  — HstrJm  .  .  yezi  . .  bavaitt  yaltö  xSnaiß frihs  paiti.zanlS  Yt.8.4z;  10.120,  Y.ig. 40;  — yaAmäi  xsnütS  bavaiti  mikrS  ,  . yakmäi  IbistB  bavatti  (sd.)  Yt  JO.87;  28, Y.  62.  9;  —  yä^a  . .  anäzarstä  xsnütA  . . a/bisti  yBbm  (näml.  fravasayö)  . .  /ra- cara'iwe\ti3.ZA;  S^  63.  'S^',  iS7';  — xlnuta  F.5;  —  vaT3h3uS xratüm  manaahS yä  xsnyvTsa  g^s^ä*urvqmm  "aufdass  ich den  Willen  des  VM.  befriedige  und  die Seele  des  Rinds"  Y.  28.  \;  —  mazdä  asä xsmüksm  vilnm  xsnaohmnB  "o  M.  und A.,  indem  ich  es  eurem  Willen  recht machen  will"  Y.  ^.  18.  a)  Des.  'zu- frieden stellen,  zu  Gefallen  sein  wollen': nsit  nä  pouräs  (sd.)  drpgvatö  Ayäi  ^ixs- n  uiS  Y.43.11;  —  ys  masying  Hxsn  uiö .  .  gäul  bagä  x^ürsmnS  (sd.)  Y,  J2,  8;  — y}  dusprJ^rJi  (sd.)  Bxsnusä  (iS.)  Y.  4g. I.  a)  mit  Dat  comm.  'Jemands  Zu- friedenheit gewinnen  wollen  für  — ':  tSm nS  vokB  mal  manavhcl  axiriusö  "des  Zu- friedenheit sollst  du  uns  zu  gewinnen suchen,  sammt  der  des   VM."  Y.  45. 9.
11360:—  jvasHt  nSit  bvat  asava  vnsasHp  tüSti bax/aiti (sd.)  vahistahe  at3kSusY.^,6i;  — fraia  fraydit  . .  ä  sangaäbyasa^  apn  ä inubyoicit  .  .  3  matiyqnas^t . .  ä  ripr^m- zasät  äpS  Y.6.aj;  —  isavasHt  al^qm  .. ar/tayascit  .  .  zarstvaat  . .  kantacit . .  va- zracit  . .  Yt.  10.  39  f.  a)  das  zweite  ^ steht  unregelmässig:  kasSusÜli  nä  ..  isvä- (sd.)(?i/'*  hqs  paraos  Y.  47.  4.  Anhang, lU  wechselt  mit  iS:  tä^^.,vasfml  anyäüä vTduyl  Y.  44. 4.         2)  wie   bei   I ;    aber
16761:zarsta    Yt  7_J.  63;     —     asista    .  .    gau/
24575:iaili  ir.'vi*  ansetie.     vizars,  viiarls  (Bd.  T;
25078:•  j.  'ra^-a-  m.  'Wagen'*':  gäui  frazarSta (sd.)  aiSqm  "i'äj'fl  (LS.)  YL70,38;  — paiti.- stayata  'ihya  aül  vat>uhi  "es  luelt  an  auf dem  Wagen  A.  . ."  YLr7. 17;  —  akmya 'äa  hvasäna  \yX.48;  —  nöit  ihra  ../ras hyat  .  .  halnyS  '%ö  nsit  uspnpts  draßs YlÄsö;  —  yat  janäni  kitäsptm  'i^e paiti  vagaihyai  (sd.)  YLi^.aS;  —  tarn caxnm  (sd.)  . .  asmatam  ''h3in  ktnnavane . . ti  mg  väitm  ^anjaySnte  spirdasca  mainyui' attrasca  Yt.J(j.  43f.
25419:•  g.  räzan- :  räsn-,  j.,  g.  räzar-,  j.  rataA- n.  i)  'Gebot,  Satzung,  Anordnung':  kat tei  °zarS  "was  ist  deine  (des  AA^  Satzung?" Y.J^ia'';  —  data  ..  'SStigiSS.)  voAb sahU  (sd.)  manaaAä  Y.  ^o.  6,  a)  im Gegensatz  zu  staoma-  (sd.)  "vom  Ritus gebotene,  vorgeschriebene  Handlung,  reli- giöser Brauch':  staemaca  'zar>ca  (AP.) barsntu  da^uJS  aAurai  matdai  .  .  "die rituellen  Gesänge  und  Bräuche  .  ."  Yt. 17.157.  3)  'festgesetzte  Gebühr,  Ent- lohnung (im  Jenseits)':  sraidyai  (sd.)  matda fravaecä  ya  vidayat  asi/  •htam  "tu  kund . .  was  von  Gebühren  A.  verteilen  wird" Y.,j^.ia«.
27781:erzürnen,  zornig,  ergrimmt  werden':  drvi zantS  zaranumanö*'*  zazarSnB'''  Yt II.  5;  —  mihrym  yim  ..  zaranimmm p3r3%ujafai3hs  vazmti  avi  kamayh  "M., den,  wenn  er  zUmt,  die  breithufigen  (Rosse) fahren  gegen  .  ."  Yt.  10. 47.
27964:•  j.  zarsnu'mant-,  zaranu'mant-"  Adj. 'Gold  enthaltend,  goldhaltig":  •manism bavähi  ya%a  yat  asti  'matö  tnaSytinake Vyt4''-  A)  mit  *süra-  m.  fsd.)  'aurata lacuna',  Name  eines  Sees  oder  Teichs*': 'manttm  saT7m  Ny.i.  8;  —  •manlB  surake FrW.5. 1.
27969:•  j.  *zaranya-'>  Adj.  'golden':  arfdvf  . . 'nya  ao'hra  (sd.)  *f>3iti.smaxta  Yt.5. 78; —  vatnm  .  .  zarSt/  (sd.)  ayan?td  fra- hixfym  .  .  *'n}-ehe  Yt.  10.  13z;  96,  I
27981:mit  frä  'fortzerren':  gäul  yä  .  .  fra- zarsta  aisqmfyäxDLmiirlljin/jqm)  rai^ya "das  Rind,  das  . .  an  ihrem  Wagen  fort- gezerrt wird"  Yt  JO.  38**.
27989:•  j.  zarSayamna-')  Adj.  'die  Federn  auf- stikubend':  tmnyahe  . .  väryynaAe  . .  yS vazaite  °nB  ayrqm  usaitim  usaahtnt  "des Vogels  K,  der  ums  erste  Morgenrot  fliegt, seine  Federn  aufsträubend"  Yt  i4-  ao.
27991:■  j.  zarStva-  n.  'Stein':   dva   dim  nara
28120:•  j.  zamöiStva-  n.  'Lehmaegcl':  dva  dim iiara  isli\ie  . .  'tve  vä  zarstve  vä  upa.- skamb^m  (sd.)  V.S.  10.
28599:Undeutlich:  mnbyS  kS  dqdraxti  Y.4. 10 PüZ.;  —  ha  drvatqm  *ayqm  (sd.)  urvanS timB.Ava  nizarsaite  V.  ;p,  30;  30;  —  ha druxs  .  .  FrW.  8.  a';  —  '"näuiti  Aa aite  yüi  maSyaka  ^ar^nti  Jramanyete  V. 7- SS-  Wertlos:  yd^a  Ab  nS  altalsqm
28663:ra  '(Wasser)  weggiessen,  aus-' und  weggiessen':  aiAhi  äps ■■y»n  yat  vä  naiitum  .  ,  pasca iixtUsd.)  ..  V.O. 37. 1)  'etwas  vergiessen,  verspritzen': iuttim  vä  tJ^ayeinti  fralaik?in ''ralUanli^^  Yt  14.  54;  —  *a'^a *frahinHn  *'antarv'>  atanmla a  "ebenso  wenn  sie  sie  (die verspritzen  zwischen  .  ."  N. '  'etwas  durch  Guss  (aus  Metall, stellen':  vasnm  . .  zarsis  ayanhs w  Yl;o.  96».
```


## [2026-09-06T02:16:15.198Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== WLD Bd1 ghers ===\"; grep -n \"horreo\\|zarsayamna\\|zar.ayamna\\|ghers\" incoming/WLD/WLD_Bd1_pages.txt | head -20"
}
```


### [2026-09-06T02:16:15.300Z] TOOL RESULT

```
=== WLD Bd1 ghers ===
57195:mochte, vgl. unter *ghers- „starren“).
57404:     ags. gierran Y. (* ghers-1 „krachen. knarren, scliwatzen", nlid. girren
57476:oder aus *ghorasos ). Yielleicht hierher auch die unter ghers- besprochenen
57503:Klippe im Meer" ( *ghorfo                              Persson Beitr. 222 f. doch siehe auch ghers-
57913:€10                                                    ghers-       — ghers-, ghres-
57920:ghers- und z. T. kiirzeres glier- „starren“ (daneben ein nur in den Satem-
57922:         neben ghers- kein ghers- nachgewiesen ist). Yerwandtsch. m. gher-
57926:      av.      zarsayamna- „die Federn aufstraubend                                      :
57959: m. Lit.) auf parallelem *ghers-q'i.os von der Wzf. auf s beruht (als o.-u.
57977:     ghers-, ghres- „Widerwille, Abscheu, Ekel".
57979:     mann Arm. Gr. I 432; von Meillet brieflich zu horreo. ai. hrsyati usw. ge-
57980:     stellt,       s       u. ghers-,          welcher Ansatz          natiirlich       arm. garsim ausscblieBt)
57984:                                              ghers-    — gherzd                                         611
57995:   Bechtel BB. 1, 1 74 f., Vf. LEWb. 2 u. fasticlium und horreo Trautmann                   ,
58000:3.ghers- in Unkrautbezeicbnungen.
58047:treide“, ebenso lit. girsa „Trespe“ usw. (s. ghers- „Unkraut“). Auch russ.
58051:   Glatt hingegen ist Anknfipfung an ghers- „starren“ (Lit. bei Yf. LEWb. 2
61275:Unter derselben Gdbed. wollte Zup. G. 2o2f. an ghers- .,horrere" ankniipfen,
```


## [2026-09-06T02:16:29.970Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nlines=open('BRT.txt',encoding='utf-8',errors='replace').read().split('\\n')\nfor i in range(27920,28010):\n    l=lines[i]\n    if re.match(r'^\\s*\\d{3,4}\\s*$', l) or re.search(r'\\b1[6-7]\\d\\d\\b', l[:20]):\n        print(i, repr(l))\nprint('---')\nprint('\\n'.join(lines[27985:27995]))\npre='\\n'.join(lines[:27989]); print('leaf', pre.count('\\f'))\nEOF"
}
```


### [2026-09-06T02:16:31.786Z] TOOL RESULT

```
27938 '1682'
27956 '1684'
28002 '1685  zasta-'
---
schleppen    die   abiiehenden  Horden    in   der
Weise  fort,  dass  sie  es  hinten  an  ihie  Wagen
binden.
•  j.  zarSayamna-')  Adj.  'die  Federn  auf- stikubend':  tmnyahe  . .  väryynaAe  . .  yS vazaite  °nB  ayrqm  usaitim  usaahtnt  "des Vogels  K,  der  ums  erste  Morgenrot  fliegt, seine  Federn  aufsträubend"  Yt  i4-  ao.
PP(l4)M. ');  lum  V.  u.  karfote,  lat  korrti-, s.  noch  np.  äst  unter  awJa-.  —  Npü.  (für  :' a-p-qm):  zarm  sar.  —  ")  isri'  aus  ir.  ^ifP -=  laL  harf,  1.  IF.  5.  161.
■  j.  zarStva-  n.  'Stein':   dva   dim  nara
isBtiie  . .  zfmsistve  vä  've  vä  ufa^kamhtnt
(sd.).. V. cV.  10;  —  iHydie  vä  'vahe  vä..
pqsnBm    V.  <?.  8 ;  —  °f  a(NP.)i^  aXsqm  /ra-
daxHanya  (sd.)  Yt.  10. 39.
leaf 916
```


## [2026-09-06T02:16:41.611Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"ghrta\\|ghṛta\\|ghrtam\\|gert .Milch\\|Milch.*gert\\|ayardan\\|a-yardan\\|āγārdan\\|agardan\" incoming/WLD/WLD_Bd1_pages.txt | head -20; echo \"--- near p607 ---\"; grep -n \"^.\\{0,6\\}60[6-9]\\b\" incoming/WLD/WLD_Bd1_pages.txt | head"
}
```


### [2026-09-06T02:16:43.191Z] TOOL RESULT

```
15525:*ni- „nieder“), ghrtaci                             f.   „fettig taussehend);                         Opferl6ffel“, qvitict                  f.    „gliin-
--- near p607 ---
57482:606                                                     gher-      — gerbh-
63388:Torp 606 aus kwhva = got. qius. Wood KZ. 45, 68 reiht an nord. kuikr
```


## [2026-09-06T02:16:46.122Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '57482,57560p' incoming/WLD/WLD_Bd1_pages.txt | grep -n \"gher\" ; echo \"======\"; awk 'NR>=57482 && NR<=57620' incoming/WLD/WLD_Bd1_pages.txt | grep -n -i \"milch\\|butter\\|gert\\|ghrt\\|yard\" "
}
```


### [2026-09-06T02:16:48.080Z] TOOL RESULT

```
1:606                                                     gher-      — gerbh-
6:. gher- „hervorstechen", von Pflanzentrieben oder -stacheln, Borsten,
15:         s  d.). Scheidung von gher- ,.reiben‘' empfiehlt sich, da eine Bed.-
22:Klippe im Meer" ( *ghorfo                              Persson Beitr. 222 f. doch siehe auch ghers-
27:,,starren“)  auch ydga^'t (s. unter gher- kratzen");
39:kann           als           dehnst.   Wznomen         hierher oder zu gher(s)- „starren" gehoren
41:   Besser belegt die schwere Basis (vgl. Zup. G. 203, wo aber gher(s)- zu-
======
```


## [2026-09-06T02:16:52.092Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=57500 && NR<=57620' incoming/WLD/WLD_Bd1_pages.txt | sed -n '1,120p'"
}
```


### [2026-09-06T02:16:53.910Z] TOOL RESULT

```
t l]v      Hes, yoiga g
             alyjirjv                             ,
                                                      emporstehend, hervorragend; hervorragende
Klippe im Meer" ( *ghorfo                              Persson Beitr. 222 f. doch siehe auch ghers-
                                                                                           ;



,,starren“)  auch ydga^'t (s. unter gher- kratzen");
                     ;
                                                                         ,,


   cymr. garth „Yorgebirge, Berg" /auch mhd. grat bed. u. a. „Bergriicken"
B. bei Fick II 4 107).
   Allenfalls ("doch ganz unsicher) hierher norw. mdartl. gare Spitze“, gara                                ,


..stechen, stoBen" (von Wood Min. 24, 48 mit lett. zars „Zweig“ verbunden,
gleich         fragwurdig).              Gr. ygo,      ygoog, lat. er, -is, ericius, erinaceus „Igel"
kann           als           dehnst.   Wznomen         hierher oder zu gher(s)- „starren" gehoren
(s.     auch        u. eghi).
   Besser belegt die schwere Basis (vgl. Zup. G. 203, wo aber gher(s)- zu-
grunde gelegt wird, und bes. Solmsen KZ. 34, 580, Berneker 346 m. Lit.;
auch Fick III 4 138 f., Falk-Torp u. gran I, grand Adj.)      mhd. grat, pi.                            :




greet m. „Fischgrate, Ahrenspitze, Bergspitze, Berggrat    nhd. Grat, Grate
                                                        ‘,

            formed entspricht ags. greed m. „Gras ‘, s. u. ghre- „wachsen“),
(*gln r-t - ;
tvoneben m. Red.-Stufe poln. grot, cech. hrot „Pfeilspitze, WurfspieB";
  mit -(/-Suffix ahd. mhd. gray, n. „Schobling, Zweig von Nadelholzern" (auch
wohl aufs Seelische gewendet ahd. grayyo Adv. ..heftig, streng                                                      1
                                                                                                                        ,
                                                                                                                            mhd. gray,
gray         ,.Wut“. gray „wiitend, zornig" u. dgl.,                                               4
                                                                                  s.   Fick III        138f.,               Falk-Torp
. grand Adj.);
    mit w-Suffix got. * grand (bezeugt Isidor Orig. XIX 23, 7), ahd. grana,
ags. gronu   grana), aisl. grqn „Sehnurrbart; Nadel, Fichte", mhd. gran, grane
                         (




  Spitze des Haares, Barthaar, Grate", nhd. Granne Ahrenstachel", mdartl.                      ,


 .Riickenborste des Schweins/ und ..Grate", schwed. mdartl. gran „Fiehte“;
   slav. *gram> „scharfe Ecke, Kante", z. B. in russ. gram f. „Grenze; Mark-
stein; Fazette", c. lirana „Ecke, Kante" usw. (s. Berneker 346; dazu auch
russ. granku „Buschel", klr. hranok „Ast, Ztveig", bg. skr. grana ,, Zweig",
trotz Wood KZ. 45, 63, s. unter *ger- „fassen“;
   alb. krqnde „Weinrebe, Strohhalm", geg. krane „Stachel, Dorn" (vgl.
G. Meyer Wb. 204).
   mir. grend „Bart", cymr. gran ,,Augenlid", bret. grann „Braue, Augen-
haare" aus ghrn-dhn (Fick II 4 118, Pedersen KG. 46) stellt zur Erwagung,
daB die n-Formen                       idg. als   (   ghr-en       :j   ghr-un-    :   ghrv- vokalisiert waren.

gerbh- .ritzen' und Verwandtes.
  Gr. ygdif a> ,.ritze ein, schreibe", yga/tjua ..Buchstabe             Linie",
                                                            ‘, yganfir)                                                         ,

yoaq'evg „Schreiber“, yganxvg ..Ritzung der Haut" (daneben dem Zentral-
griechischen entstammende Formen mit -go- fiir ~Qa~)j ags. ceorfan (Ptc.
                                                                gherto-                                                             607

corfen) „schneiden, kerben     ahd. kerbnn ,.Einschnitte machen, schneidenA
nhd. krrben , mhd. kerbe ,.Einschnitt, Kerbe‘% ags. cyrf f. Schmid" (Fick 4                              ,                              1



404); aksl. Lr-ha, zrehbjb ,.Los" (,,*gekerbtes Stabchen“), apr. glrhiu ,.Zahl"
(„*Kerbung“, Kern, Zitat bei Boisacq 155; anders Trautmann Apr. 33Sf.
zu gerbt „sprechen‘                ;
                                       lett.       grebju „hohle aus" gehort zu                          */jJtrebli-).

  Ygl. mit der Yokalfolge *grebh- (also einstige Basis *gerebh-), mnd. krab-
ben „kratzen, ritzen, schaben", dan. norw. krabbe „scharren, grapsen" (und
,,krabbeln, kriechen“, ursprgl. ,,kriechen,   indem man sich festhakt ), wozu                                                  11




anord. krabbi ags. crabba nd. krabbe „Krabbe und ahd. kreba^ip), krebi3         ‘
                     ,                         ,


mnd. krevd, kreft nhd. Krebs (Fick III 4 52, Falk-Torp u. krabbe, krebs).
                               ,
                                                                                                                                        —   ,




Ganz fraglich gr. ygoptpag .,Sau (.die wiihlende, grabende ?) als Nasalform
                                                        ‘




(Prellwitz 2 s. v. lett. grumbt „Runzeln bekommen‘ s. unter ger- ,,drehen‘).
                          ;


   Daneben *g(e)reibh- gr. ygigAadar ygdrpeiv. Adxcove s. ol ds £veiv y.a'i
dpvaaetv Hes. (Fick I 4 404; vgl. von sker- gr. ay.aglgpdouai lat. scribo                                              ,                    ,


Prellwitz 2 99), ayglcpr], aygeitpia ..Harke, Rechen“ (a- aus *n- ep', „ein-                                               ,

ritzen' ); boll, knbben, kribbelen   kritzelnA mhd. kribt ln ,.kitzeln (von der
        1
                                                            .
```


## [2026-09-06T02:16:58.915Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"gherto\\|ghertom\\|gher-to\" incoming/WLD/WLD_Bd1_pages.txt | head; echo \"---\"; grep -n \"gherto\" WLD_band3.txt incoming/WLD/WLD_Bd2_pages.txt | head"
}
```


### [2026-09-06T02:16:58.989Z] TOOL RESULT

```
57569:                                                                gherto-                                                             607
57681:gherto- „Milch, ButterA
---
```


## [2026-09-06T02:17:00.678Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '57675,57700p' incoming/WLD/WLD_Bd1_pages.txt"
}
```


### [2026-09-06T02:17:00.737Z] TOOL RESULT

```
(vgl. z. B. Siebs KZ 37, 313, Lewy KZ. 40, 420, Falk-Torp aaO.), die aber
ebensowenig eine lautliche Yereinigung erheischen wie etwa germ. *krit-
mit *urit-,         *rit-.



gherto- „Milch, ButterA
  Ai.       ghriam ,.Rahm, Butter, Schmelzbutter“, ir. gcrt (i. lacht) „Milch".
  Nach Uhlenbeck zu jigharti                            (
                                                            gharati ) ,.besprengt, betraufelt , np. a-ynr-
dan „vermischen, einweichen".
  Fick II 4 112           .
60S                                                     gherd               gherdh-


1.   glierd-    .,      wilder Birnbaum -- ?
                                                                                '

     Gr. dyeodo; ..wilder Birnbaum                        ;
                                                               Hagedorn
                                                aygd ?, - ado ..wilder Birnbaum,- -
                                                                                   ',



Birne     alb. darde ( *ghord -) Birnbaum" ? Bugge BB. 18, 164. Unsicher.
```


## [2026-09-06T02:17:16.286Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD gherto ===\"; grep -n \"gherto\\|ghero-\\|ghrto\" AHD_watkins1985.txt | head; echo \"=== IEC ===\"; grep -n \"ghrtom\\|ghrto\\|ghersō\\|gherso\" IEC.txt | head; echo \"=== CHEUNG ===\"; grep -n -i \"āɣārdan\\|agardan\\|āɣuštan\\|aɣišt\\|āγārdan\\|\\*gar\\b\\|GARH\" CHEUNG.txt | head -30"
}
```


### [2026-09-06T02:17:16.382Z] TOOL RESULT

```
=== AHD gherto ===
421:eghero-. Lake. Possibly a suffixed variant form *agher-
524:gher-’. To shine, glow; gray. Hypothetical base of various Germanic forms. 1. Germanic *gréwaz, gray, in: a. Old English greg, gray: GRAY; b. probably Old English grighund, greyhound: GREYHOUND. 2. Germanic *gris- Jaz, gray, in: a. Old French gris (> French gris), gray: GRISAILLE, (GRISETTE), (GRISON), GRIZZLE; AMBERGRIS; b. Medieval Latin griseus, gray, grayish: GRISEOUS. [Pok. 3. gher- 441.] gher-4. To scrape, scratch. 1. Extended zero-grade form *ghr(e)-k- in: a. Greek kharax, a pointed stake, also a kind of sea bream: CHARACIN; b. Greek kharassein, to sharpen, notch, carve, cut: CHARACTER, GASH. 2. Ex- tended form *ghers-.in suffixed zero-grade form *ghrs-to- perhaps (but unlikely) in Sanskrit ghattah, ghat: GHAT. See also extensions ghréi- and ghréu-. [Pok. 2. gher- 439.] gher-5. To like, want. 1. Suffixed form *gher-n- in Ger- manic “*gernjan in Old English giernan, gyrnan, to strive, desire, yearn: YEARN. 2. Extended form *ghré- possibly in: a. Germanic *gréduz, hunger, forming *grédagaz, hungry, in Old English grédig, hungry, covetous, greedy: GREEDY; b. Greek khré, it is necessary, whence krésthai, to lack, want, use: CATACHRESIS, CHRESARD, CHRESTOM- ATHY. 3. Suffixed zero-grade form *ghr-td- in Latin hortari, to urge on, encourage (< “to cause to strive or desire”): HORTATIVE; EXHORT. 4. Suffixed zero-grade form “ghr-i- in Greek kharis, grace, favor: CHARISMA; Eucnarist. [Pok. 1. gher- 440.] ghere-. Gut, entrail. 1. Suffixed form *ghero-no- in Ger- manic *garn6, string, in Old English gearn, yarn: YARN. 2. Suffixed form *ghero-n- in Latin hernia, “protruded viscus,” rupture, hernia: HERNIA. 3. Suffixed o-grade form *ghoro-d- in Greek khordé, gut, string: (CHORD?), CORD, (CORDON); HARPSICHORD, TETRACHORD. 4. O-grade form *ghors- in Greek khorion, intestinal membrane, afterbirth: CHORION. 5. Possible suffixed zero-grade form *ghr-u- in Latin haruspex (-spex, “he who sees” < *spek-, “to see”; see spek-), “he who inspects entrails,” diviner (but perhaps borrowed from Etruscan): HARUSPEX. [Pok. 5. gher- 443.] ghers-. To bristle. 1. Extended zero-grade form *ghrzd-, prickly plant, in: a. Germanic *gorst- in Old English gorst, furze, gorse: GORSE; b. Latin hordeum, barley: ORGEAT. 2. Lengthened-grade form *ghér(s)- in Latin hér, ér, hedgehog: URCHIN. 3. Suffixed lengthened-grade form *ghér(s)-ika in Latin ériica, caterpillar: ROCKET?. 4. Suffixed full-grade form *gher-tu-, remade to *hirsu- in Latin hirsitus, bristly, shaggy, hairy: HIRSUTE. 5. Suf- fixed full-grade form *ghers-ko- in Latin hispidus (prob- ably a dialectal borrowing), bristly, shaggy, prickly: HISPID. 6. Suffixed o-grade form “ghors-eyo- in Latin horrére, to bristle, shudder, be terrified, look frightful: HORROR; ABHOR, ORDURE. 7. Suffixed full-grade form *ghers-o- in Greek khersos, dry land: CHERSONESE. [Pok. Bhers- 445.] gheslo-. Seen by some as a base for words meaning “thousand.” 1, Suffixed form *ghesl-yo- in Greek khilioi, thousand: CHILIAD, KILO-. 2. Latin mille, thousand, which has been analyzed as *smi-, “one” + a form *ghsli-, is of obscure origin: MIL!, MIL2, MILE, MILLE- NARY, MILLESIMAL, MILLI-, MILLIEME, MILLION; MIL- FOIL, MILLENNIUM, MILLEPORE, MILLIARY, MILLIPEDE. [Pok. ghéslo- 446.] ghesor-. Hand. Reduced form “ghesr- in Greek kheir, hand: CHIRO-; (CHIRURGEON), ENCHIRIDION, (SURGEON), SURGERY. [Pok. 1. 8hesor- 447.] gheu-. To pour, pour a libation. I. Extended form *gheud-. 1. Zero-grade form *ghud- in Germanic *gut- in Old English guttas, intestines: GuT. 2. Nasalized zero-grade form *ghu-n-d- in Latin fundere, to pour: FOISON, FONDANT, FONDUE, FONT, FOUND2, FUNNEL, FUSE?, FUSILE, FUSION; AFFUSION, CIRCUMFUSE, CON- FOUND, CONFUSE, DIFFUSE, EFFUSE, INFUSE, PERFUSE, PROFUSE, REFUND!, (REFUSE!), (REFUSE?), SUFFUSE,
1209:ACHE ag-es- ACHENE ghai- ACHERON eghero- ACHOLIA ghel-2 ACHROMATIC ghréu- ACICULA ak- ACID ak-
=== IEC ===
=== CHEUNG ===
350:° Т only recently discovered that the root *gar” ‘to be/make warm’ has been preserved as verb in Oss. 
3408:kindle, light a fire’, cited by Abaev, Le: 158 f. They rather contain the root *gar’ ‘to 
7652:*gar! ‘to rejoice’ 
7676:*gar? ‘to turn, wind’ 
7698:*gart and *gar£". 
7721:основы *jara- от корня *gar- ‘гореть, xxeup'". 
7725:The verbal forms of *gar’ are only found in some modern Iranian dialects. The old 
7739:*gar^ ? ‘to coagulate, stiffen’ 
7749:9 In view of the very limited evidence, the existence of an Ir. root *gar- ‘to 
7779:*MISC: (?) Par. jar-/jari (јбг ?) ‘to say’. 0 Perhaps not from *garH! ‘to greet’ (as 
7817:*garH! ‘to greet, call’ 
7874:108 *garH2 
7948:* garH* *to swallow" 
8027:© The root seems to be an "enlarged" root, i.e. *so-formation, of *gar? *to turn, wind'. 
8035:*garš2 ? ‘to knead, rub (?)’ 
8100:*gar”. It has probably been influenced by *yart. 
8145:*SANSKRIT: garh ‘to complain’ (RV+) = EWAia I: 475, 495 
30378:separated from *garH!, Skt. gar ‘to greet, praise’, which rather refers to the 
51564:garh, 112 
55366:*gar', *gäz (s.v.), *Hram 
55495:*garH? (s.v.), *haic, *nab 
55517:*gar* (s.v.), *gauz (s.v.), 
55735:*gar’, *starH’, *stamb(H), 
55889:*garH!, *gauH, *huanH, 
55897:*garH? (s.v.), *Haz (s.v.), 
56017:*garH!, *gauH, *huanH, 
56026:*gar*, *Hané (s.v.), *mad’, 
56153:*gar’, *pac, *paxš 
56468:*gar', *gäz (s.v.), *Hram 
56757:*garH' (sv.), *Haz (s.v.),
```


## [2026-09-06T02:17:18.848Z] TOOL CALL #36: Bash

```json
{
 "command": "pdftoppm -f 190 -l 190 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg190 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


### [2026-09-06T02:17:21.086Z] TOOL RESULT

```
total 25932
drwx------ 2 sfmqrb sfmqrb   12288 Sep  5 17:18 .
drwx------ 4 sfmqrb sfmqrb    4096 Sep  5 16:02 ..
-rw-rw-r-- 1 sfmqrb sfmqrb   68775 Sep  5 16:43 ary440.png
-rw-rw-r-- 1 sfmqrb sfmqrb  752374 Sep  5 16:12 bqt362_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  624515 Sep  5 16:12 bqt362.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb 1032029 Sep  5 16:13 bqt362_mid.png
-rw-rw-r-- 1 sfmqrb sfmqrb  385716 Sep  5 16:13 bqt363_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  338175 Sep  5 16:13 bqt363_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb  692415 Sep  5 16:13 bqt363.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  956665 Sep  5 16:11 bqt553_foot2.png
-rw-rw-r-- 1 sfmqrb sfmqrb  746413 Sep  5 16:11 bqt553_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  512022 Sep  5 16:10 bqt553.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  154316 Sep  5 16:07 bqt_bot389.png
-rw-rw-r-- 1 sfmqrb sfmqrb  168738 Sep  5 16:07 bqt_bot390.png
-rw-rw-r-- 1 sfmqrb sfmqrb  520653 Sep  5 16:07 bqt_n389.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  527392 Sep  5 16:07 bqt_n390.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  100925 Sep  5 16:52 bqt_pdf600.png
-rw-rw-r-- 1 sfmqrb sfmqrb   67648 Sep  5 16:29 build128.py
-rw-rw-r-- 1 sfmqrb sfmqrb  105345 Sep  5 16:30 build132.py
-rw-rw-r-- 1 sfmqrb sfmqrb   62948 Sep  5 16:36 build134.py
-rw-rw-r-- 1 sfmqrb sfmqrb   56126 Sep  5 16:29 build136b.py
-rw-rw-r-- 1 sfmqrb sfmqrb   13830 Sep  5 16:22 build136.py
-rw-rw-r-- 1 sfmqrb sfmqrb   66341 Sep  5 16:28 build139.py
-rw-rw-r-- 1 sfmqrb sfmqrb   53260 Sep  5 16:29 build142.py
-rw-rw-r-- 1 sfmqrb sfmqrb   76989 Sep  5 16:32 build145.py
-rw-rw-r-- 1 sfmqrb sfmqrb   50861 Sep  5 16:34 build148b.py
-rw-rw-r-- 1 sfmqrb sfmqrb   21485 Sep  5 16:29 build148.py
-rw-rw-r-- 1 sfmqrb sfmqrb   17908 Sep  5 16:44 build151a.py
-rw-rw-r-- 1 sfmqrb sfmqrb   15986 Sep  5 16:46 build151b.py
-rw-rw-r-- 1 sfmqrb sfmqrb   11172 Sep  5 16:47 build151c.py
-rw-rw-r-- 1 sfmqrb sfmqrb   19592 Sep  5 16:50 build151d.py
-rw-rw-r-- 1 sfmqrb sfmqrb    6433 Sep  5 16:50 build151z.py
-rw-rw-r-- 1 sfmqrb sfmqrb   51529 Sep  5 16:51 build152.py
-rw-rw-r-- 1 sfmqrb sfmqrb   51266 Sep  5 16:51 build154.py
-rw-rw-r-- 1 sfmqrb sfmqrb   61639 Sep  5 16:53 build155.py
-rw-rw-r-- 1 sfmqrb sfmqrb   70485 Sep  5 16:53 build156.py
-rw-rw-r-- 1 sfmqrb sfmqrb   72953 Sep  5 16:48 build158.py
-rw-rw-r-- 1 sfmqrb sfmqrb   74140 Sep  5 16:56 build160.py
-rw-rw-r-- 1 sfmqrb sfmqrb   53286 Sep  5 16:55 build161.py
-rw-rw-r-- 1 sfmqrb sfmqrb   67253 Sep  5 16:56 build162.py
-rw-rw-r-- 1 sfmqrb sfmqrb   45662 Sep  5 16:49 build164.py
-rw-rw-r-- 1 sfmqrb sfmqrb   82221 Sep  5 16:56 build168.py
-rw-rw-r-- 1 sfmqrb sfmqrb   53542 Sep  5 16:57 build169.py
-rw-rw-r-- 1 sfmqrb sfmqrb   58105 Sep  5 17:02 build171.py
-rw-rw-r-- 1 sfmqrb sfmqrb   51583 Sep  5 17:08 build173.py
-rw-rw-r-- 1 sfmqrb sfmqrb   59926 Sep  5 17:11 build174.py
-rw-rw-r-- 1 sfmqrb sfmqrb   64448 Sep  5 17:12 build175.py
-rw-rw-r-- 1 sfmqrb sfmqrb   69033 Sep  5 17:13 build177.py
-rw-rw-r-- 1 sfmqrb sfmqrb   75374 Sep  5 17:12 build180.py
-rw-rw-r-- 1 sfmqrb sfmqrb   43965 Sep  5 17:11 build181.py
-rw-rw-r-- 1 sfmqrb sfmqrb   64481 Sep  5 17:11 build182.py
-rw-rw-r-- 1 sfmqrb sfmqrb   47920 Sep  5 17:11 build183.py
-rw-rw-r-- 1 sfmqrb sfmqrb   62604 Sep  5 17:16 build184.py
-rw-rw-r-- 1 sfmqrb sfmqrb   63773 Sep  5 17:17 build186.py
-rw-rw-r-- 1 sfmqrb sfmqrb   62923 Sep  5 22:13 build189.py
-rw-rw-r-- 1 sfmqrb sfmqrb    7816 Sep  5 16:35 c_am2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   14765 Sep  5 16:35 c_am3.png
-rw-rw-r-- 1 sfmqrb sfmqrb   10038 Sep  5 16:35 c_empty2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4123 Sep  5 16:34 crop_am.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4986 Sep  5 16:34 crop_arabic_refs.png
-rw-rw-r-- 1 sfmqrb sfmqrb    7702 Sep  5 16:34 crop_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb   16978 Sep  5 16:34 crop_morocco.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5391 Sep  5 17:02 g2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2929 Sep  5 17:02 g3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5607 Sep  5 17:02 g4.png
-rw-rw-r-- 1 sfmqrb sfmqrb  163996 Sep  5 16:46 gar2.png
-rw-rw-r-- 1 sfmqrb sfmqrb  124975 Sep  5 16:47 gar3.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77205 Sep  5 16:46 gar.png
-rw-rw-r-- 1 sfmqrb sfmqrb   14924 Sep  5 17:01 geus_left.png
-rw-rw-r-- 1 sfmqrb sfmqrb   10247 Sep  5 17:01 ghaido_left.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4197 Sep  5 17:01 ghaido_low.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3536 Sep  5 17:04 jang.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  944060 Sep  5 16:18 kent.txt
-rw-rw-r-- 1 sfmqrb sfmqrb     310 Sep  5 22:16 leaf.py
-rw-rw-r-- 1 sfmqrb sfmqrb   57617 Sep  5 16:20 mk129.py
-rw-rw-r-- 1 sfmqrb sfmqrb   74680 Sep  5 16:26 mk131.py
-rw-rw-r-- 1 sfmqrb sfmqrb   33365 Sep  5 16:25 mk133.py
-rw-rw-r-- 1 sfmqrb sfmqrb   42635 Sep  5 16:29 mk140.py
-rw-rw-r-- 1 sfmqrb sfmqrb   51288 Sep  5 16:30 mk143.py
-rw-rw-r-- 1 sfmqrb sfmqrb   57696 Sep  5 16:46 mk153.py
-rw-rw-r-- 1 sfmqrb sfmqrb   49505 Sep  5 16:50 mk157.py
-rw-rw-r-- 1 sfmqrb sfmqrb   56703 Sep  5 16:54 mk166.py
-rw-rw-r-- 1 sfmqrb sfmqrb   61790 Sep  5 16:57 mk167.py
-rw-rw-r-- 1 sfmqrb sfmqrb   30384 Sep  5 16:51 mk170.py
-rw-rw-r-- 1 sfmqrb sfmqrb   84301 Sep  5 17:17 mk176.py
-rw-rw-r-- 1 sfmqrb sfmqrb   68808 Sep  5 17:15 mk178.py
-rw-rw-r-- 1 sfmqrb sfmqrb    4344 Sep  5 16:49 n12b.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3969 Sep  5 16:49 n12.png
-rw-rw-r-- 1 sfmqrb sfmqrb   24939 Sep  5 17:01 n14.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2692 Sep  5 16:49 n16.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3293 Sep  5 17:01 n17b.png
-rw-rw-r-- 1 sfmqrb sfmqrb   17771 Sep  5 17:01 n17c.png
-rw-rw-r-- 1 sfmqrb sfmqrb    6463 Sep  5 17:01 n17.png
-rw-rw-r-- 1 sfmqrb sfmqrb    7472 Sep  5 17:01 n19.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3278 Sep  5 17:01 n5b.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2334 Sep  5 17:01 n5c.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3215 Sep  5 17:01 n5.png
-rw-rw-r-- 1 sfmqrb sfmqrb   11831 Sep  5 16:32 node4.png
-rw-rw-r-- 1 sfmqrb sfmqrb    7427 Sep  5 16:32 node7.png
-rw-rw-r-- 1 sfmqrb sfmqrb  944060 Sep  5 16:13 oldpers_djvu.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    6054 Sep  5 16:36 p152_e0left.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2672 Sep  5 16:36 p152_node2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   35268 Sep  5 16:59 p162a.png
-rw-rw-r-- 1 sfmqrb sfmqrb   14337 Sep  5 16:59 p162b.png
-rw-rw-r-- 1 sfmqrb sfmqrb   76438 Sep  5 16:59 p162.png
-rw-rw-r-- 1 sfmqrb sfmqrb   41788 Sep  5 16:53 p173_ital.png
-rw-rw-r-- 1 sfmqrb sfmqrb   32898 Sep  5 16:53 p173_op.png
-rw-rw-r-- 1 sfmqrb sfmqrb  161412 Sep  5 17:01 p174hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  173427 Sep  5 17:01 p176hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2762 Sep  5 17:02 p189_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb   24596 Sep  5 17:02 p189_greek2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   20222 Sep  5 17:02 p189_khoris.png
-rw-rw-r-- 1 sfmqrb sfmqrb   33994 Sep  5 17:02 p189_n12.png
-rw-rw-r-- 1 sfmqrb sfmqrb  671488 Sep  5 16:52 p600_350.png
-rw-rw-r-- 1 sfmqrb sfmqrb  139701 Sep  5 16:52 p600_foot2.png
-rw-rw-r-- 1 sfmqrb sfmqrb  183909 Sep  5 16:52 p600_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1717 Sep  5 16:52 p600_head2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5162 Sep  5 16:52 p600_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1189 Sep  5 16:57 p600_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   22067 Sep  5 16:29 part0.json
-rw-rw-r-- 1 sfmqrb sfmqrb   14156 Sep  5 16:22 part1.json
-rw-rw-r-- 1 sfmqrb sfmqrb   17147 Sep  5 16:44 part_a.json
-rw-rw-r-- 1 sfmqrb sfmqrb   15703 Sep  5 16:46 part_b.json
-rw-rw-r-- 1 sfmqrb sfmqrb   10974 Sep  5 16:47 part_c.json
-rw-rw-r-- 1 sfmqrb sfmqrb   19420 Sep  5 16:50 part_d.json
-rw-rw-r-- 1 sfmqrb sfmqrb   53212 Sep  5 16:08 pg130_bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74748 Sep  5 16:08 pg130.png
-rw-rw-r-- 1 sfmqrb sfmqrb  107108 Sep  5 16:08 pg130_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   80793 Sep  5 16:15 pg131.png
-rw-rw-r-- 1 sfmqrb sfmqrb   46793 Sep  5 16:20 pg133.png
-rw-rw-r-- 1 sfmqrb sfmqrb   87739 Sep  5 16:10 pg134.png
-rw-rw-r-- 1 sfmqrb sfmqrb   66991 Sep  5 16:16 pg135.png
-rw-rw-r-- 1 sfmqrb sfmqrb   68320 Sep  5 16:08 pg136_300.png
-rw-rw-r-- 1 sfmqrb sfmqrb   63248 Sep  5 16:08 pg136.png
-rw-rw-r-- 1 sfmqrb sfmqrb   45014 Sep  5 16:12 pg137.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74330 Sep  5 16:11 pg138.png
-rw-rw-r-- 1 sfmqrb sfmqrb   70436 Sep  5 16:10 pg140.png
-rw-rw-r-- 1 sfmqrb sfmqrb   63658 Sep  5 16:13 pg144.png
-rw-rw-r-- 1 sfmqrb sfmqrb   89133 Sep  5 16:09 pg145.png
-rw-rw-r-- 1 sfmqrb sfmqrb   60631 Sep  5 16:11 pg147.png
-rw-rw-r-- 1 sfmqrb sfmqrb   81770 Sep  5 16:20 pg148.png
-rw-rw-r-- 1 sfmqrb sfmqrb   72186 Sep  5 16:30 pg149.png
-rw-rw-r-- 1 sfmqrb sfmqrb  131595 Sep  5 16:32 pg151_hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   96854 Sep  5 16:29 pg151.png
-rw-rw-r-- 1 sfmqrb sfmqrb  154426 Sep  5 16:36 pg152_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb   62516 Sep  5 16:35 pg152.png
-rw-rw-r-- 1 sfmqrb sfmqrb   39131 Sep  5 16:28 pg153.png
-rw-rw-r-- 1 sfmqrb sfmqrb   63033 Sep  5 16:30 pg154.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77057 Sep  5 16:32 pg155.png
-rw-rw-r-- 1 sfmqrb sfmqrb  101504 Sep  5 16:43 pg156.png
-rw-rw-r-- 1 sfmqrb sfmqrb  169880 Sep  5 16:34 pg158_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb   80624 Sep  5 16:34 pg158.png
-rw-rw-r-- 1 sfmqrb sfmqrb  124379 Sep  5 16:31 pg159_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb   27814 Sep  5 16:31 pg159.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4694 Sep  5 16:31 pg159_word.png
-rw-rw-r-- 1 sfmqrb sfmqrb  168057 Sep  5 16:34 pg161_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb   76745 Sep  5 16:34 pg161.png
-rw-rw-r-- 1 sfmqrb sfmqrb  110270 Sep  5 16:42 pg162_400.png
-rw-rw-r-- 1 sfmqrb sfmqrb   76438 Sep  5 16:42 pg162.png
-rw-rw-r-- 1 sfmqrb sfmqrb    8523 Sep  5 16:42 pg162_verse.png
-rw-rw-r-- 1 sfmqrb sfmqrb   25911 Sep  5 16:32 pg163.png
-rw-rw-r-- 1 sfmqrb sfmqrb   59398 Sep  5 16:33 pg164.png
-rw-rw-r-- 1 sfmqrb sfmqrb   61265 Sep  5 16:40 pg165.png
-rw-rw-r-- 1 sfmqrb sfmqrb  116877 Sep  5 16:46 pg167.png
-rw-rw-r-- 1 sfmqrb sfmqrb   86005 Sep  5 16:39 pg168.png
-rw-rw-r-- 1 sfmqrb sfmqrb   68420 Sep  5 16:42 pg169.png
-rw-rw-r-- 1 sfmqrb sfmqrb   37351 Sep  5 16:44 pg170.png
-rw-rw-r-- 1 sfmqrb sfmqrb  120612 Sep  5 16:49 pg171_450.png
-rw-rw-r-- 1 sfmqrb sfmqrb   73551 Sep  5 16:43 pg171.png
-rw-rw-r-- 1 sfmqrb sfmqrb   73400 Sep  5 16:56 pg172.png
-rw-rw-r-- 1 sfmqrb sfmqrb   52970 Sep  5 16:53 pg173.png
-rw-rw-r-- 1 sfmqrb sfmqrb   70664 Sep  5 17:00 pg174.png
-rw-rw-r-- 1 sfmqrb sfmqrb   54907 Sep  5 16:54 pg175.png
-rw-rw-r-- 1 sfmqrb sfmqrb   83583 Sep  5 17:00 pg176.png
-rw-rw-r-- 1 sfmqrb sfmqrb   88207 Sep  5 17:02 pg177.png
-rw-rw-r-- 1 sfmqrb sfmqrb   98352 Sep  5 17:01 pg178_hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   64024 Sep  5 17:01 pg178.png
-rw-rw-r-- 1 sfmqrb sfmqrb   57139 Sep  5 16:54 pg179.png
-rw-rw-r-- 1 sfmqrb sfmqrb   81598 Sep  5 16:58 pg180.png
-rw-rw-r-- 1 sfmqrb sfmqrb   56794 Sep  5 17:00 pg181.png
-rw-rw-r-- 1 sfmqrb sfmqrb   66020 Sep  5 17:01 pg182.png
-rw-rw-r-- 1 sfmqrb sfmqrb   53414 Sep  5 17:03 pg183.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77310 Sep  5 16:58 pg184.png
-rw-rw-r-- 1 sfmqrb sfmqrb   79537 Sep  5 17:09 pg185.png
-rw-rw-r-- 1 sfmqrb sfmqrb   72425 Sep  5 17:08 pg186.png
-rw-rw-r-- 1 sfmqrb sfmqrb   53749 Sep  5 17:02 pg187.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77516 Sep  5 17:01 pg189.png
-rw-rw-r-- 1 sfmqrb sfmqrb   65970 Sep  5 22:17 pg190.png
-rw-rw-r-- 1 sfmqrb sfmqrb   44812 Sep  5 16:34 pg532.png
-rw-rw-r-- 1 sfmqrb sfmqrb  153161 Sep  5 16:34 pg532_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4868 Sep  5 16:14 prt.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  333088 Sep  5 16:16 sod135_c.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1817364 Sep  5 16:16 sod135.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  101641 Sep  5 16:15 sod136_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1892712 Sep  5 16:15 sod136.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  561602 Sep  5 16:57 t598.png
-rw-rw-r-- 1 sfmqrb sfmqrb  632359 Sep  5 16:57 t599.png
-rw-rw-r-- 1 sfmqrb sfmqrb  671488 Sep  5 16:57 t600.png
-rw-rw-r-- 1 sfmqrb sfmqrb  545905 Sep  5 16:57 t601.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1268 Sep  5 16:57 top598.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1268 Sep  5 16:57 top599.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1268 Sep  5 16:57 top600.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1268 Sep  5 16:57 top601.png
-rw-rw-r-- 1 sfmqrb sfmqrb   24918 Sep  5 16:58 tops2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4812 Sep  5 16:57 tops.png
-rw-rw-r-- 1 sfmqrb sfmqrb   56398 Sep  5 16:26 write144.py
-rw-rw-r-- 1 sfmqrb sfmqrb     738 Sep  5 17:04 xang.txt
```


## [2026-09-06T02:17:26.457Z] TOOL CALL #37: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg190.png"
}
```


### [2026-09-06T02:17:26.907Z] TOOL RESULT

```

```


## [2026-09-06T02:17:26.905Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-06T02:17:41.742Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && pdftoppm -f 190 -l 190 -r 400 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf p190hi && python3 -c \"\nfrom PIL import Image\nim=Image.open('p190hi.png'); print(im.size)\n# empty box region: in 1700x2200 coords approx x 845..1190, y 350..440 -> scale 400/200=2 from the 200dpi render (1700 wide)\nw,h=im.size; s=w/1700.0\nim.crop((int(830*s),int(340*s),int(1210*s),int(450*s))).save('p190_emptybox.png')\nim.crop((int(360*s),int(650*s),int(660*s),int(820*s))).save('p190_skt.png')\n\""
}
```


### [2026-09-06T02:17:45.481Z] TOOL RESULT

```
(3400, 4400)
```


## [2026-09-06T02:17:48.489Z] TOOL CALL #39: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p190_emptybox.png"
}
```


### [2026-09-06T02:17:48.510Z] TOOL RESULT

```

```


## [2026-09-06T02:17:48.610Z] TOOL CALL #40: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p190_skt.png"
}
```


### [2026-09-06T02:17:48.628Z] TOOL RESULT

```

```


## [2026-09-06T02:17:55.348Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('p190hi.png'); w,h=im.size; s=w/1700.0\nim.crop((int(680*s),int(330*s),int(1250*s),int(460*s))).save('p190_eb2.png')\n\""
}
```


### [2026-09-06T02:17:57.737Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T02:17:59.989Z] TOOL CALL #42: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p190_eb2.png"
}
```


### [2026-09-06T02:18:00.003Z] TOOL RESULT

```

```


## [2026-09-06T02:18:10.034Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== CHEUNG garH3 ===\"; sed -n '7948,8000p' CHEUNG.txt; echo \"=== CHEUNG agar? ===\"; grep -n \"āɣār\\|aɣār\\|āɣišt\\|aɣišt\\|āgār\\|agišt\\|āɣuštan\" CHEUNG.txt | head"
}
```


### [2026-09-06T02:18:10.133Z] TOOL RESULT

```
=== CHEUNG garH3 ===
* garH* *to swallow" 

*AVESTAN: YAv. garð (f. pl.) ‘throats’ (Yt 17.56), YAv. aspo.garom noro.garom 
‘who swallows horses (and) who swallows men’ (Y 9.11).. 6 YAv. "jar- ‘to swallow’ 
(Y Av. "jarois P22), as cited by Bartholomae, AIW: 512, does not exist, on which see 
Jamaspa — Humbach 1971: 45, fn. a. 

*NWIR: Gz. Zara/Zar-, Tr. Zarta/Zar- ‘to chew’, NP Zard ‘gluttony’ (LW) || (+ *aua-) ? 
Bal. ugarit/ugar- ‘to chew the cud, swallow, devour, devastate, misspend’. © The 
etymology of Bal. ugarit/ugar- is unclear: Sims-Williams apud Shahbakhsh suggests 
a connection with MP ogar- (BMP wkl /ögär-/) ‘to remove, expel’, but contamina- 
tion with Si. ugaranu ‘to chew the cud’ seems quite likely, as observed by Shah- 
bakhsh. The older Bal. form might have been *ögär- ? 

*NEIR: Pash. yaráy ‘greedy, gluttonous’, ? Pash. yur (m.) ‘goitre’ || (+ *a-) Pash. ayér 
(m.) ‘indigestion’ || (+ *uz-) M. zoyóriy ‘thirsty’ || (+ *ni-) Pash. nyar(d)-/nyar- ‘to 
swallow’ (with sec. -r-) || (+ *niZ-) Oss. I. nyqq.yryn/nyqqoyrd, D. niq(q)warun 
/niq(q)ward ‘to swallow’ (contaminated with q.yr/qur throat), Wa. noZ(y)or-/ 
noZ(y)ord-, noZ(y)or-/noZ(y)ord ‘to swallow’ 

*SANSKRIT: gar’ ‘to devour, swallow’ (RV+)  EWAia I: 469 

«PIE *g”erH;- ‘to devour, consume (wholly)? = LIV: 211 f. | Pok.: 474 ff. 

*IE COGNATES: Gr. В.Вроско “I eat, digest’, Lat. voräre ‘to devour, to eat greedily’, 
OCS po-Zréti ‘to eat (of animals), to devour’, Lith. gérti ‘to drink’, etc. 

*REFERENCES: EVP: 26, 51; IIFL II: 533a, 275a; Morgenstierne 1942: 266; Abaev, Slovar’ II: 268 f., 205 


f.; Abaev, Slovar’ III: 205 Ё; EVS: 52a; WIM ПЛ: 87; Werba 1997: 180; Steblin-Kamenskij 1999: 251; 
Lecoq 2002: 128; NEVP: 8, 32, 56; Shahbakhsh: s.v. ugar- 


*раг]! ? ‘to thunder, roar’ 

*KHOTANESE: OKh. ggalj- ‘to thunder’ = SGS: 28 

*NEIR: Sh. yury-/yuryd, Orosh. yury-/yuryd ‘to grumble, scold’, ? Rosh. jiriyd, 
Jireyd, Khf. jirtyd, jiréyd ‘to squeak, scream, hiss, whine, etc’, ? Sangl. yeZ-/yezoó, 
Ishk. yeiZ-/yeiZeó ‘to say, speak’ 

*SANSKRIT: ? garj ‘to roar’ (Ep.+) = EWAia III: 154 

© The root is onomatopoetic. 


*PIE — > LIV: — | Pok.: 
*REFERENCES: IIFL II: 395b; EVS: 37a, 39b; Werba 1997: 458; Steblin-Kamenskij 1999: 185 


110 *garj2 ? 

=== CHEUNG agar? ===
```


## [2026-09-06T02:18:12.954Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HUB ===\"; grep -n \"āγārdan\\|agardan\\|ayarden\\|äyärden\\|äyarden\\|agisten\\|äyisten\" HUB.txt | head; echo \"=== ARY ===\"; grep -n \"آغشتن\\|آغاردن\\|آغار\" incoming/ARY/ARY_pages.txt | head; echo \"=== LEW horreo ===\"; grep -n \"horreo\" LEW_1910.txt | head; echo \"=== LAT horreo ===\"; grep -n \"horreo\" LAT.txt | head; echo \"=== SKT horror ===\"; grep -n \"horror\" SKT.txt | head"
}
```


### [2026-09-06T02:18:13.065Z] TOOL RESULT

```
=== HUB ===
=== ARY ===
=== LEW horreo ===
=== LAT horreo ===
17282:( horreo), pecuniam id crumenam a 1 est developp^ le sena de "enfermer,
28159:Un rapprochement ayec horreo ou ayec hircus est difficile. En tout
28496:(avec rapprochement de horreo et hordeum par dtym.pop.); fctre herissd;
28530:Derivas: horreolum n. (Val.Max. ), horrearius m.:gardien des greniers de
=== SKT horror ===
461:Aghast,  horror-struck,  (£.)  Misspelt  for a^poj/,  which  is  short  for  agattid,  pp.  of M.  E.  agaittn,  to  terrify;  Ch.  C.  T.  134,1; Leg.  of  Good  Women,  Dido,  J45.  — A.  S. <f-.  prefix;  and  gth/au.  to  terrify,  torment. p.  A.  S.g^tUn,  is  from  the  b.ise  r<i'-  =  (Jot.*!. ^ais-  in  uf-gaij-'j<j»,  to  terrify.  (^GHAU>.)
8023:terrible.  Formed  with  suffix  -He  ^ike (rom  grosen  •  «■  grprcn,  pp.  of  gre6san, '.« afflict  with  hoiror.  AIHm  lo  G.grttusi^ causing  horror,  and  to  QruMome.
8094:Gruesome,  horril'le.  (Scand.)  Dan./TM. horror  ;  with  suffix  -tont,  as  in  virk  torn, active.  <-f.  Dan.  g*'uc,  lo  dread,  gt-u^/ig^ horrid,  .f  Du.  gruwioam^  G.  grausam. Allied  to  O.  SAx.gfuri,  A.  S.gryrg,  horror. Olid  to  K.  Otialj'.
```


## [2026-09-06T02:18:23.115Z] TOOL CALL #45: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-06T02:18:23.123Z] TOOL RESULT

```


```


## [2026-09-06T02:18:25.335Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HUB tries ===\"; for p in \"agar\" \"ayar\" \"âgâr\" \"agist\" \"ayist\" \"gharati\" \"besprengen\"; do echo \"-- $p\"; grep -n -i \"$p\" HUB.txt | head -3; done; echo \"=== ARY latin GHER ===\"; grep -n \"GHER\\|Gher\" incoming/ARY/ARY_latin_index_pages.txt | head"
}
```


### [2026-09-06T02:18:27.108Z] TOOL RESULT

```
=== HUB tries ===
-- agar
309:entlehnt, ebenso das syr. Wort, vgl. de Lagarde, G. A.
662:148. Lies Jtori^^iq und vgl. de Lagarde, G. A. p. 73,
993:*mskart (vgl. de Lagarde, Pers. Stud. p. 75) zu-
-- ayar
3765:ayar *Helfer 2). Zu np. Isfandyar vgl. phi. Spand-
4239:mit paz. ayar Shk. 235, doch ist die Lesung der Pehlevi-
4468:(unter Mitwii^kung des i der ersten Silbe); hiayar Viel* =
-- âgâr
-- agist
1263:bei 6reg. Magistros: Jemand fand einen Frosch
8557:stan = np. SagistCLn, gr. ^axadravfj bei I si dor von
-- ayist
8304:*K5iiig = ap. xsaya^iya-; sayistan *sich ziemen, kSnnen,
10327:bayistan 25.
10732:Sayistan 134.
-- gharati
-- besprengen
1430:(vgl. skr. abhi'Sindafi *begiessen, besprengen , ni$incati
1433:*patisindatiy 'begiessen, besprengen*, med. *patisincataii/
2634:Zu srasd {tySsrasdat/en *sie sollen besprengen) gehSrt
=== ARY latin GHER ===
6673:(GHERS) 754, (URCHIN) 681, (ail jIMOLD ENGLISH) oS gS
12763:OBRATIT RUSSIAN) .o+3, GHERUAN (KURDISH) «53,5
```


## [2026-09-06T02:18:32.611Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '6660,6685p' incoming/ARY/ARY_latin_index_pages.txt"
}
```


### [2026-09-06T02:18:32.666Z] TOOL RESULT

```
ove seb oly
GARB OLD IRISH) 95 543 2 XAR, XARPUSHT — (PAHLAVI) 5
GARW (WELSH) 3) (SANSKRIT) 4 Sade
HARSATE, HRSYATI
REFERENCES beth GREEK) gig
OKO SOSO™~S HEROS, CHER, KHER
BARNHART: (URCHIN) 1188 ALATIN) 3
DELAMARRE: (HERISSON) 133 HORREO, HORRERE, HER, ERECIUS
MACKENZIE: . HERISSON (FRENCH) il
(THORN) 136, (HEDGEHOG) 163 ERIZO H(SPANISH)  gliteel
ONIONS: RICCIO HUTALIAN) pls!
(URCHIN) 964, (CHRACTER) 163 ARICIU -ARUMANIAN) ay
SKEAT: OURICO :(PORTUGUESE) sity,
(GHERS) 754, (URCHIN) 681, (ail jIMOLD ENGLISH) oS gS
(CHARACTER) 103 YRICHON
ayy chicas abcd URCHIN ENGLISH) AS
VEY 9 PAV ebb oby GERS (SWEDISH) 6 y
GJORS (NORWEGIAN) 5335
se Me Sept 5d 9 ee ee ASI 9 SHIA y ig, 9 eV 4 eo Sole Ob 22 HN atl
De ale 515335. 9 6H YS PY a
ae PERN |
[pdf page 232]
mise
AMARGO PORTUGUESE) 5 *AMAD «(OLD PERSIAN) dU «4
oM HOLD IRISH) oS 543 2\ XAM (PAHLAVI) 54a
OF AGAULISH) JS XAV, XAVI, XAM_ (KURDISH) 53,
```


## [2026-09-06T02:18:33.083Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/horror",
 "prompt": "Give the full etymology entry for \"horror\", including the Latin horrere and the PIE root cited."
}
```


### [2026-09-06T02:18:38.745Z] TOOL RESULT

```
# Etymology of "Horror"

The word "horror" entered English in the early 14c. meaning "feeling of disgust," evolving by the late 14c. to denote "emotion of horror or dread." It derives from Old French *horror* and directly from Latin *horror*, literally meaning "a shaking, trembling (as with cold or fear), shudder, chill."

The Latin verb *horrere* means "to bristle with fear, shudder," tracing back to the Proto-Indo-European root ***ghers-***, which signifies "to bristle." This same PIE root also produces related words like Sanskrit *harsate* ("bristles"), Latin *eris* ("hedgehog"), and Welsh *garw* ("rough").

Historically, the English noun also referred to "a shivering" as a symptom of disease (1530s), "erection of the hairs on the skin" (1650s), and "a ruffling as of water surface" (1630s). The term entered film terminology as a genre designation in 1934.
```


## [2026-09-06T02:18:47.864Z] TOOL CALL #49: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A2%D8%BA%D8%B4%D8%AA%D9%86",
 "prompt": "Give the Persian entry for آغشتن: etymology (Middle Persian / Proto-Iranian / PIE forms cited), meaning, and any related forms such as آغاردن."
}
```


## [2026-09-06T02:18:49.518Z] TOOL CALL #50: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E0%A4%98%E0%A5%83%E0%A4%A4",
 "prompt": "Give the Sanskrit entry for घृत (ghṛta): meaning and etymology (which root it comes from, PIE reconstruction)."
}
```


### [2026-09-06T02:18:53.188Z] TOOL RESULT

```
# Persian Entry: آغشتن (âġeštan)

## Meaning
This is a transitive verb with multiple related senses: "to soak, steep; to infuse; to imbrue; to smear; to indoctrinate; to inoculate; to saturate; to impregnate."

## Forms
- **Present stem:** آغار (âġâr)
- **Past stem:** آگشت (âġešt)
- **Present participle:** آغارنده (âġârandé)
- **Past participle:** آگشته (âġešté)

## Related Form
The page notes a synonym: گشنیدن (gošnidan), meaning "to saturate" or "to impregnate."

## Etymology
The Wiktionary entry provided does not include etymological information tracing the word to Middle Persian, Proto-Iranian, or Proto-Indo-European forms. Etymology details are absent from the source material.
```


### [2026-09-06T02:18:56.433Z] TOOL RESULT

```
# Sanskrit Entry: घृत (ghṛta)

## Meaning
The word has three etymological paths with distinct meanings:

1. **"Sprinkled"** - from the root घृ (ghṛ, "to rub, ceremonially anoint, sprinkle")
2. **"Illumined"** - from gharṛ (ghṛ, "to shine, burn")
3. **"Ghee" or "fat"** - the most common modern sense, referring to clarified butter

## Etymology & Root Origins

### Primary Etymology (Ghee):
Derived from Sanskrit घृ (ghṛ) plus the verbal adjective suffix -त (-ta). The traditional view connects it to "to rub/sprinkle," though scholars propose an alternative: the word likely derives from Proto-Indo-European *gʷʰr̥-tós, from the root *gʷʰer- meaning "warm, hot," reflecting that ghee is "melted (heated) butter."

### PIE Reconstruction:
**Proto-Indo-European: *gʷʰer-** ("warm, hot")

This root is cognate with Middle Irish gert ("dairy products, milk or manure").
```


## [2026-09-06T02:19:11.905Z] TOOL CALL #51: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%C7%B5%CA%B0ers-",
 "prompt": "Does this reconstruction page exist? Give the root's meaning, and the descendants listed (Latin, Sanskrit, Avestan, Greek, Germanic)."
}
```


## [2026-09-06T02:19:13.119Z] TOOL CALL #52: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/gert",
 "prompt": "Give the Old Irish / Middle Irish entry for \"gert\": meaning and etymology (which PIE root, and any mention of Sanskrit ghṛta)."
}
```


### [2026-09-06T02:19:17.554Z] TOOL RESULT

```
# Response

I cannot provide the requested information based on the webpage content supplied. The Wiktionary article for "gert" only covers **English** and **Icelandic** entries. There is no Old Irish or Middle Irish section present in this document.

The English entry traces the word's origin to "Middle English _girt_, _gert_," but does not extend the etymology further back to PIE roots or Sanskrit cognates like ghṛta. To obtain this comparative linguistic information, you would need to consult additional etymological resources or a more comprehensive historical dictionary.
```


### [2026-09-06T02:19:17.779Z] TOOL RESULT

```
# Proto-Indo-European Root *ǵʰers-

Yes, this reconstruction page exists on Wiktionary.

**Root Meaning:**
The root has two related meanings: "(to be) stiff" and "(to be) surprised."

**Listed Descendants:**

- **Latin:** *horreō* ("to bristle, shudder"), *horror*, *hīrtus* ("hairy, shaggy")
- **Sanskrit:** *hṛṣ-*, *ghṛ́ṣu*
- **Greek:** *khérsos* (χέρσος, "dry land")
- **Armenian:** *jaṙ* (ձառ)
- **Iranian languages:** Khotanese and Pashto forms meaning "rough" or "stiff"

Note: The page does not list Avestan or Germanic descendants explicitly, though it documents various Proto-Indo-Iranian developments that produced Sanskrit and Iranian reflexes.
```


## [2026-09-06T02:20:03.424Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"آغار\\|آغشتن\\|آغاردن\" MON_part1.txt | head -20"
}
```


### [2026-09-06T02:20:03.493Z] TOOL RESULT

```
3635:آغار: : :38 ((.) اغرء آغال: بد آغار (شوم» 
3638:آغاردن: 221-1 [ - آغار بدن] (مسص مع.) 
3639:(آغارد» آغازد» خواهد آغارد» بیاغاره 
3640:آغارنده» آغارده) آغاربدن. 
3642:آغاریدن: 2721-120 [ - آغاردن ] (آغار بد» 
3643:آغارد» خواهد آغارید؛ بباغار» آغارنده؛ 
3644:آغار بده) (مصعم.) خساندن» تر کردن» نم 
3662:آغال: اقبة (- آغار - اغر | اغره شگون بد 
3686:اغردن: 2۷72۲-0 [- آغاربدن ِ آغشتن ] 
3698:آغشتن: 272)6(۹-0 | < آغزدن - آغاردن] 
4098:ماه بنگالی» آغار بقون. 
14689:اغر: ۲ (- اغور» قس. آغار آغال] (ا.) 
28652:نمنا کك کردن» آغشتن. بالودن رنگ و از 
81007:آغشتن در آب. اندودن. فرسودن» کهنه
```


## [2026-09-06T02:20:07.973Z] TOOL CALL #54: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://www.etymonline.com/word/horror' --note 'page 190, root Ghers, Latin horrere > English horror' ; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%C7%B5%CA%B0ers-' --note 'page 190, root Ghers: PIE *ǵʰers- (to be) stiff / surprised'; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%E0%A4%98%E0%A5%83%E0%A4%A4' --note 'page 190, root Gherto: Sanskrit ghṛta, modern derivation from PIE *gʷʰer- warm'; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%A2%D8%BA%D8%B4%D8%AA%D9%86' --note 'page 190, Persian âgeštan/âgâr present stem' 2>&1 | tail -20"
}
```


### [2026-09-06T02:20:10.107Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/32d4c3ec4d664f2b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a3f809becefd9185.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/7870b4d242de19d0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/65f9e841e03c60e4.txt
```


## [2026-09-06T02:20:15.620Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '28490,28535p' LAT.txt"
}
```


### [2026-09-06T02:20:15.697Z] TOOL RESULT

```
temps"). Le mot rappelle v.h.a.Aturu (de *hiujarH) "cette annde". - Le
-y- initial de ce mot, se trouvant en position intervocalique dans
le compose, s 1 est amui en latin. Pour le suffixe -no-, cf.uernus,
hodiernus, etc.
horreS, -Ss, -ui, -ere: se dresser (en pariant des poils du corps):
in corpore pili, ut arista in spica hordei, horrent, Yarr., L.L.6,4.5
(avec rapprochement de horreo et hordeum par dtym.pop.); fctre herissd;
frissonner [d'effroi], souvent joint k tremO. Avec un conplenent,
"frissonner devant quelque chose, k la pens 4 e de, avoir horreur de"
(cf. cppiCTao)); de IA horrendus "qui fait frissonner". Du sens de "etre
h£riss£", on passe au sens (rare) de "etre effroyable", CaL 1,49 quaedam
loca frigoribus hiemis intolerabiliter horrent. - Ancien, usuel.
- Non roman.
D^riv^s et composes: horror n.: h^rissement, frisson, horreur. M.L.
4190; horridus: hAriss^; de IA "A 1 'aspect sauvage, horrible", M.L.
4188 et 4187 *horridor; horridulus (familier, Plaute); horrSscO,-is :
avoir le poil qui dresse, se hdrisser; frissonner, M.L.4185; horri¬
bilis: horrible; horrent ia,-ae (Tert.); horrifer, horrificus,-ficO,
-ficabilis (tous po^tiques); horricomis (= opQoQpiB,, Apul.), horri¬
pilo,-as, cf. gr. opGoTpkX^ (de *horri-pilus non attestd, semble-t-il)
M.L.4189, horripilStii, mots de la 1 .ecclds.(avec des graphies obri-,
obbri-, orri-, d'aprbs obrepere?)} horrisonus (po^t.); abhorrei:
s' 4 carter avec horreur de; avoir horreur de; et par affaibliasement
"etre ^tranger ou opposd A, en contradiction avec". Jusqu'A Sndtone,
le verbe est construit avec ab, mais A partir de cet auteur, on le
rencontre avec 1'accusatif: abhorrere alqm, ou alqd, ce qui devient
la construction r^gulibre. Bn bas latin apparant abhorrSsci qui est
deneurd dans les 1 . romanes, M.L.33; cohorresci (Cic.); exhorrei
(rare, Coi. Juv.); exhorresci (classique, usuel); inhorrisco, per-
horrei (rare, tardif); perhorresci} perhorridus (T.L.); subhorridus
(Cic. Sest. 9,31).
Pas d'£tymologie sfire. Toutefois, on est tentd de rapprocher arm.
gariim "j'ai horreur de" et skr .ghrsuh "excitd", hdrsate "il a une
horripilation de joie".
horreum, -I n. ( horreus b.lat.; horrea Calid. ap.Non.308,37):
grenier, grange; h. publicum "grenier public"; par suite "magasin.535
hospes
entrepfit, garde-Aeuble". La glose de Festas, horreum antiqui farreum
dicebant a farre, P.F.91,6, n'est appuyee par ancon exemple, et seable
n'etre qu'une Etymologie popalaire. - Ancien, asuel. M.L.4186.
Derivas: horreolum n. (Val.Max. ), horrearius m.:gardien des greniers de
1'fitat (epoq. iap.), horreSt icus: cortcernant les greniers (Dig.).
Pas d'etyaologie.
hSrsum adv.: de ce c 6 t 4 -ci. Archafque (Pl. et T 4 r. de hs-uor-
sum).V. seorsum.
V. hic.
```


## [2026-09-06T02:20:22.647Z] TOOL CALL #56: Bash

```json
{
 "command": "sed -n '1,120p' tools/verify_check.py"
}
```


### [2026-09-06T02:20:22.696Z] TOOL RESULT

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


## [2026-09-06T02:21:27.477Z] TOOL CALL #57: Bash

```json
{
 "command": "ls /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/ 2>/dev/null | head"
}
```


### [2026-09-06T02:21:27.526Z] TOOL RESULT

```
0001.png
0001.txt
0049.png
0049.txt
103.vision.txt
1225.png
1225.txt
1225.vision.txt
1275.png
1275.txt
```


## [2026-09-06T02:25:51.513Z] TOOL CALL #58: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build190.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\ndata = {\n \"pdf_page\": 190,\n \"book_page\": 160,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-05\",\n \"entries\": [\n  {\n   \"entry\": 1,\n   \"root\": \"Ghers\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *ǵʰers- 'to bristle, stand stiff (of hair/feathers)', secondarily 'to shudder, be horrified'\",\n   \"note\": \"Pokorny p.445-446 has the lemma exactly: 'ghers- and partly gher-', Meaning 'rigid' (German 'starren'), References WP. I 610, WH. I 413f. Watkins/AHD: 'ghers-. To bristle. … [Pok. ghers- 445]'. Wiktionary's Reconstruction:Proto-Indo-European/ǵʰers- glosses it '(to be) stiff; (to be) surprised'. Nourai's language label (Indo-European) and page reference are right; his gloss 'to be horrified, to stare' renders the ambiguity of Pokorny's German 'starren' (which means both 'to be stiff/bristle' and 'to stare') and imports the secondary Latin sense — the primary sense is 'to bristle'. The chart's two children (Avestan zarš-, Latin horrēre) are precisely the two forms Pokorny equates with each other on that page.\",\n   \"note_fa\": \"ریشهٔ هندواروپایی آغازین *ǵʰers- «سیخ شدن، برافراشته شدن مو و پر» است؛ پوکورنی (ص ۴۴۵–۴۴۶) آن را با واژهٔ آلمانی starren آورده و واتکینز در پیوست فرهنگ American Heritage آن را «to bristle» معنی کرده است. معنایی که نورایی داده («وحشت‌زده شدن، خیره شدن») از دوپهلویی همان واژهٔ starren (هم «سیخ شدن» هم «خیره شدن») و از معنای ثانویِ فعل لاتینی horrēre برخاسته است؛ پس گلاس اندکی جابه‌جا شده ولی خودِ ریشه، برچسب زبانی و ارجاع درست است. ویکی‌واژه نیز این ریشه را «سفت/سیخ شدن؛ شگفت‌زده شدن» معنی می‌کند. ادعای نورایی در کل درست است.\",\n   \"sources\": [\n    \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%C7%B5%CA%B0ers-\",\n    \"https://www.etymonline.com/word/horror\"\n   ],\n   \"ref_check\": [\n    {\"ref\": \"POK:445\", \"status\": \"supports\", \"note\": \"POK_full.txt (database dump) 'Root / lemma: ghers- and partly gher-; Meaning: rigid … References: WP. I 610, WH. I 413 f., 650, 659. Page(s): 445-446'. The page cited is exactly where the lemma stands, and it contains both Latin horreo and Avestan zaršayamna-.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"IEW 445-446, lemma ghers-\", \"stance\": \"supports\", \"note\": \"'Old Indic harṣate, hṛṣyati \\\"becomes stiff, ruffles, shudders\\\"; Latin horreo, -ere … (= Avestan zarṣaya-)' — grep 'Root / lemma: ghers-' in POK_full.txt\"},\n    {\"src\": \"WLD\", \"where\": \"Bd. I 610\", \"stance\": \"supports\", \"note\": \"'ghers- und z. T. kürzeres gher- „starren“ … av. zaršayamna- „die Federn aufsträubend“' (WLD_Bd1_pages.txt line 57920-57926); Pokorny's own reference WP. I 610 checks out.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. ghers-\", \"stance\": \"supports\", \"note\": \"'ghers-. To bristle. … 6. Suffixed o-grade form *ghors-eyo- in Latin horrēre, to bristle, shudder, be terrified, look frightful: HORROR; ABHOR, ORDURE. [Pok. ghers- 445.]'\"},\n    {\"src\": \"ARY\", \"where\": \"ARY_latin_index_pages.txt, entry indexed pdf p.231 (خار / خارپشت)\", \"stance\": \"supports\", \"note\": \"Aryanpur's cognate list for this root gives SANSKRIT HARSATE, HRSYATI; LATIN HORREO, HORRERE, HER, ERECIUS; PAHLAVI XAR, XARPUSHT; ENGLISH URCHIN — i.e. the same root, with Persian خار/خارپشت as its Iranian reflex (a reflex Nourai does not draw).\"},\n    {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. horreō (LAT.txt l. 28496 ff.)\", \"stance\": \"partial\", \"note\": \"'Pas d'étymologie sûre. Toutefois, on est tenté de rapprocher arm. garšim \\\"j'ai horreur de\\\" et skr. ghṛṣuḥ \\\"excité\\\", hárṣate…' — the same comparison, but Ernout-Meillet call it only tempting, not certain.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Avestan\",\n     \"words\": \"zrš, zarš; zaršayamna\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Young Avestan zarəšayamna- is a real, attested form: Bartholomae, AiW col. 1684-85, '*j. zarəšayamna- Adj. \\\"die Federn aufsträubend\\\": mərəγahe … vārəγnahe … yō vazaite °nō ayrəm ušastəm ušaŋhəntəm \\\"of the bird Vārəγna, who flies at the first dawn, ruffling his feathers\\\" Yt. 14.20', with Bartholomae's footnote 'zarš- aus ir. *žṛš- = lat. horrē-, s. IF 5.161'. The citation forms zarš- / zṛš- that Nourai puts first are the abstracted verbal root, exactly as Pokorny writes it ('Avestan zarš- = zṛš- = Latin horreō'); the middle participle in -ayamna- is built on a causative/iterative stem *zarš-aya-. Phonetically PIE *ǵʰ > Proto-Indo-Iranian *ǰʰ > Iranian z-, and PIE *-rs- is preserved as Avestan -rš-; the Sanskrit match is hárṣate / hṛṣyáti 'bristles, is excited'. The one caveat: 'to be horrified' is not an Avestan meaning — the Avestan attestation means only 'making the feathers stand up'; the sense 'shudder with fear' is Latin's, and Nourai has carried it back onto the Avestan headword. The second word, zaršayamna 'ruffling one's feathers', is glossed word-for-word as in Klein.\",\n     \"derivation_fa\": \"صورت اوستایی zarəšayamna- واقعی و در یشت ۱۴ بند ۲۰ به‌کار رفته است: بارتولومه در فرهنگ ایرانی باستان (ستون ۱۶۸۴–۱۶۸۵) آن را «پرها را سیخ‌کننده» (die Federn aufsträubend) معنی کرده، در وصف مرغ وارغنه که سپیده‌دم پرافشان می‌پرد؛ و در پانوشت همان مدخل zarš- را از ایرانی *žṛš- و برابرِ لاتینی horrē- دانسته است. دگرگونی آوایی منظم است: *ǵʰ هندواروپایی در هندوایرانی به *ǰʰ و در ایرانی به z بدل شده و خوشهٔ -rš- بر جای مانده؛ هم‌ریشهٔ سنسکریت آن hárṣate/hṛṣyáti «سیخ می‌شود، برانگیخته می‌شود» است. تنها نکتهٔ محل تأمل معنی است: در اوستا این ستاک تنها «پر برافراشتن» معنی می‌دهد و معنی «هراسیدن» از فعل لاتینی به آن بازتابانده شده است. در مجموع ادعای نورایی درست است.\",\n     \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%C7%B5%CA%B0ers-\"],\n     \"ref_check\": [\n      {\"ref\": \"POK:445\", \"status\": \"supports\", \"note\": \"POK_full.txt, lemma ghers- (Page(s): 445-446): 'Avestan zarṣayamna- \\\"die Federn aufsträubend\\\" (zarṣ- = zṛṣ- = Latin horreō)' — literally Nourai's two Avestan words and the equation with the Latin child.\"},\n      {\"ref\": \"KLN:744\", \"status\": \"supports\", \"note\": \"Klein 1966, s.v. horror (between the page markers 743 and 746 in KLN_1966.txt, i.e. p.744/745): '… fr. I.-E. base *ghers-, \\\"to bristle\\\", whence also L. hirsutus …, OI. hárṣate, hṛṣyati, \\\"bristles\\\", Avestic zarshayamna-, \\\"ruffling one's feathers\\\"'. Nourai's English gloss is Klein's verbatim.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BRT\", \"where\": \"AiW col. 1684-1685 s.v. zarəšayamna- (BRT.txt line 27989; column headers 1682/1684/1685 nearby)\", \"stance\": \"supports\", \"note\": \"'j. zarəšayamna- Adj. \\\"die Federn aufsträubend\\\" … Yt. 14.20', footnote 'zarš- aus ir. *žṛš- = lat. horrē-, s. IF 5.161'. Bartholomae has no independent verb entry zarš- 'to be horrified' — only this participle.\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. I 610\", \"stance\": \"supports\", \"note\": \"'av. zaršayamna- „die Federn aufsträubend“' listed under ghers- „starren“.\"},\n      {\"src\": \"CHEUNG\", \"where\": \"Etym. Dict. of the Iranian Verb, grep 'zarš'\", \"stance\": \"silent\", \"note\": \"Cheung has no Iranian verbal root *zarš-/*garš- 'to bristle' (only *garš² ? 'to knead, rub (?)' at a different place); the Avestan form survives only as the hapax participle, so it never became a verb root entry.\"},\n      {\"src\": \"KLN\", \"where\": \"s.v. horror, p.744\", \"stance\": \"supports\", \"note\": \"cited above; Klein is the source of the gloss 'ruffling one's feathers'.\"}\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"Latin\",\n     \"words\": \"horrĕre\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Latin horrēre, horreō 'to stand on end, bristle; to shudder, tremble, dread' continues *ǵʰors-eye- (o-grade stative/iterative *ghors-eyo-, Watkins), with regular Latin *ǵʰ > h- initially and *-rs- > -rr- by assimilation (cf. also *ghers-ko- > hispidus, hirsūtus). Semantically the Latin verb is the bridge from 'bristle' to 'shudder with fear', hence Nourai's gloss 'to be horrified'. Ernout-Meillet document exactly this range: 'se dresser (en parlant des poils du corps) … être hérissé; frissonner [d'effroi]'. The chart's arrow root → Latin is thus the standard derivation, though Ernout-Meillet caution 'pas d'étymologie sûre' and call the Armenian/Sanskrit comparison only tempting.\",\n     \"derivation_fa\": \"فعل لاتینی horrēre / horreō «سیخ شدن مو، برافراشته شدن؛ لرزیدن از ترس، هراسیدن» بازماندهٔ صورت *ǵʰors-eye- (درجهٔ o با پسوند *-eye-) است؛ *ǵʰ آغازین در لاتین به h و خوشهٔ *-rs- بر اثر همگونی به -rr- بدل شده است (همچنان که در hirsūtus و hispidus از همین ریشه). گذر معنایی «سیخ شدن مو» ← «لرزیدن از ترس» در خودِ لاتین رخ داده و همان است که نورایی «هراسیدن» ترجمه کرده است. ارنو و مِیه در فرهنگ ریشه‌شناسی لاتین همین دامنهٔ معنایی را می‌آورند اما ریشه‌شناسی را «نه‌چندان قطعی» می‌دانند. ادعای نورایی درست است.\",\n     \"sources\": [\"https://www.etymonline.com/word/horror\"],\n     \"ref_check\": [\n      {\"ref\": \"POK:445\", \"status\": \"supports\", \"note\": \"POK_full.txt lemma ghers- (Page(s) 445-446): 'Latin horreo, -ere \\\"to stand on end, stand erect, bristle, be rough, tremble, shudder…\\\" (= Avestan zaršaya-)'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. horreō (LAT.txt l. 28494-28527)\", \"stance\": \"partial\", \"note\": \"'horreō, -ēs, -uī, -ēre: se dresser (en parlant des poils du corps) … être hérissé; frissonner [d'effroi]' + 'Pas d'étymologie sûre. Toutefois, on est tenté de rapprocher arm. garšim … et skr. ghṛṣuḥ, hárṣate.' Same comparison, weaker commitment.\"},\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. ghers- §6\", \"stance\": \"supports\", \"note\": \"'Suffixed o-grade form *ghors-eyo- in Latin horrēre, to bristle, shudder, be terrified, look frightful: HORROR'.\"},\n      {\"src\": \"KLN\", \"where\": \"s.v. horror, p.744\", \"stance\": \"supports\", \"note\": \"'fr. L. horrōrem, acc. of horror … fr. horrēre, \\\"to stand on end, bristle, shake, shudder, shiver, tremble\\\", fr. I.-E. base *ghers-, \\\"to bristle\\\"'.\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. I 610\", \"stance\": \"supports\", \"note\": \"lat. horreō is the head witness of the article ghers- „starren“.\"}\n     ]\n    },\n    {\n     \"id\": 3,\n     \"lang\": \"English\",\n     \"words\": \"horror\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"English horror is a borrowing, not a native reflex: Latin horror, -ōris 'a bristling, shuddering, chill' (an -or abstract of horrēre) > Old French horror/orror/horrour (Modern French horreur) > Middle English horrour, attested from the early 14th c. in the sense 'feeling of disgust', by the late 14th c. 'emotion of horror, dread'. Nourai's arrow Latin horrēre → English horror is therefore right in substance, with the one refinement that English took over the derived noun horror (via Old French) rather than the verb; the intermediate French stage is not shown in the chart. Later English senses ('shivering as a symptom', 1530s; 'erection of the hairs on the skin', 1650s) preserve the original Latin sense.\",\n     \"derivation_fa\": \"واژهٔ انگلیسی horror وام‌واژه است نه بازماندهٔ مستقیم: از اسم لاتینی horror «سیخ شدن مو، لرزه، هراس» (اسم‌ساز -or از فعل horrēre) به فرانسهٔ باستان horror/orror (فرانسهٔ امروز horreur) و از آنجا به انگلیسی میانه horrour در آغاز سدهٔ چهاردهم میلادی، نخست به معنی «بیزاری» و از پایان همان سده به معنی «هراس». پس پیکان نورایی از horrēre لاتینی به horror انگلیسی درست است، جز آنکه انگلیسی خودِ اسم مشتق را از راه فرانسه گرفته و این حلقهٔ میانی در نمودار نیامده است. ادعای نورایی درست است.\",\n     \"sources\": [\"https://www.etymonline.com/word/horror\"],\n     \"ref_check\": [\n      {\"ref\": \"none\", \"status\": \"not_checked\", \"note\": \"the node carries no reference of its own in the book (refs=None); the chain is covered by the Latin parent's POK:445 and by Klein s.v. horror (KLN:744, cited on the Avestan node).\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"s.v. horror, p.744\", \"stance\": \"supports\", \"note\": \"'horror, n. — ME. horrour, fr. OF. orror, horror, horrour (F. horreur), fr. L. horrōrem, acc. of horror … fr. horrēre'.\"},\n      {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict., grep 'horror'\", \"stance\": \"silent\", \"note\": \"Skeat's concise edition has no separate headword 'horror' (only incidental uses under Aghast, Grisly, Gruesome); no contradiction, just no entry.\"},\n      {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. horreō, Dérivés\", \"stance\": \"supports\", \"note\": \"'Dérivés et composés: horror n.: hérissement, frisson, horreur. M.L. 4190' — the Romance descendants (Meyer-Lübke 4190) are the route into Old French.\"}\n     ]\n    }\n   ]\n  },\n  {\n   \"entry\": 2,\n   \"root\": \"Gherto\",\n   \"verdict\": \"plausible\",\n   \"modern_form\": \"Pokorny's *ǵʰer-to- 'milk, butter' (Aryan + Celtic only); modern handbooks instead take Skt. ghṛtá- to PIE *gʷʰer- 'warm' (*gʷʰr̥-tós 'melted [butter]')\",\n   \"note\": \"Nourai reproduces Pokorny faithfully: IEW p.446 has 'Root / lemma: gherto-, Meaning: milk, butter, Note: only Aryan and Celtic. Material: Old Indic ghṛtám \\\"skimmings, butter, melting butter\\\"; after Uhlenbeck to jígharti (gharati) \\\"sprays, sprinkles\\\", npers. a-γārdan \\\"blend, mix, soak\\\"; Middle Irish gert \\\"milk\\\". References: WP. I 607, II 166.' So the root, the language label, the gloss and the page are all correct AS A CITATION OF POKORNY, and the Persian branch is Pokorny's own. What has changed is the modern assessment: the lemma rests on just two witnesses (Skt. ghṛtá-, MIr. gert), and current scholarship (Mayrhofer EWAia, reported by Wiktionary) derives ghṛtá- from PIE *gʷʰr̥-tós, root *gʷʰer- 'warm, hot' — i.e. 'melted (heated) butter' — and takes MIr. gert with it, so a PIE noun *ǵʰer-to- 'milk, butter' is no longer generally maintained. Note also that within the article Pokorny keeps two things apart that Nourai's chart merges: the noun ghṛtám 'butter', and the verb ghar-/jígharti 'to sprinkle', which is what the Persian words actually attach to. Verdict 'plausible': correctly cited from the standard handbook, but superseded on the Sanskrit side.\",\n   \"note_fa\": \"نورایی این ریشه را درست از پوکورنی نقل کرده است: در فرهنگ ریشه‌شناسی هندواروپایی پوکورنی، ص ۴۴۶، مدخل gherto- «شیر، کره» آمده با این یادداشت که تنها در آریایی و سلتی گواه دارد، و مواد آن سنسکریت ghṛtám «کره، روغن گداخته»، ایرلندی میانه gert «شیر»، و ــ به گفتهٔ اولنبک ــ فارسی نو āγārdan «آمیختن، خیساندن» است. پس ریشه، برچسب زبانی، معنی و شمارهٔ صفحه به‌عنوان نقل از پوکورنی درست است. اما پژوهش امروزی این مدخل را نگه نداشته: مایرهوفر (و به پیروی او ویکی‌واژه) ghṛtá- سنسکریت را از *gʷʰr̥-tós و ریشهٔ *gʷʰer- «گرم» می‌گیرد، یعنی «کرهٔ گداخته»، و gert ایرلندی را نیز به همان می‌پیوندد؛ بنابراین نامواژهٔ هندواروپایی *ǵʰer-to- «شیر، کره» دیگر پذیرفتهٔ همگان نیست. افزون بر این، پوکورنی نامِ ghṛtám «کره» را از فعلِ ghar-/jígharti «پاشیدن، نم زدن» جدا نگه می‌دارد، حال آنکه نمودار نورایی این دو را در یک جعبه درهم آمیخته است؛ واژه‌های فارسی در واقع به فعل دوم می‌پیوندند. حکم: با احتیاط پذیرفتنی است.\",\n   \"sources\": [\n    \"https://en.wiktionary.org/wiki/%E0%A4%98%E0%A5%83%E0%A4%A4\"\n   ],\n   \"ref_check\": [\n    {\"ref\": \"POK:446\", \"status\": \"supports\", \"note\": \"POK_full.txt: 'Root / lemma: gherto-; Meaning: milk, butter; Note: only Aryan and Celtic; Material: Old Indic ghṛtám \\\"skimmings, butter, melting butter\\\"; after Uhlenbeck to jígharti (gharati) \\\"sprays, sprinkles\\\", npers. a-γārdan \\\"blend, mix, soak\\\"; Middle Irish gert \\\"milk\\\". References: WP. I 607, II 166. Page(s): 446' — the cited page is exactly the lemma, gloss included.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"IEW 446 s.v. gherto-\", \"stance\": \"supports\", \"note\": \"quoted above; note Pokorny's own restriction 'only Aryan and Celtic'.\"},\n    {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. I 607\", \"stance\": \"supports\", \"note\": \"WLD_Bd1_pages.txt l. 57681: 'gherto- „Milch, Butter“. Ai. ghṛtám „Rahm, Butter, Schmelzbutter“, ir. gert (i. lacht) „Milch“. Nach Uhlenbeck zu jígharti (gharati) „besprengt, beträufelt“, np. a-γārdan „vermischen, einweichen“. Fick II⁴ 112.' This is Pokorny's source and the ultimate source of Nourai's whole chart.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985, IE roots appendix\", \"stance\": \"silent\", \"note\": \"grep 'gherto' in AHD_watkins1985.txt: no entry — Watkins drops the lemma (there is no English reflex, and he does not list it among the gher- roots).\"},\n    {\"src\": \"IEC\", \"where\": \"Mann, IE Comparative Dictionary, grep 'ghrtom/ghrto'\", \"stance\": \"silent\", \"note\": \"no hit for a lemma *ǵʰr̥to- in IEC.txt.\"},\n    {\"src\": \"CHEUNG\", \"where\": \"Etym. Dict. of the Iranian Verb\", \"stance\": \"silent\", \"note\": \"Cheung has no Iranian verbal root *gar- 'to wet/sprinkle'; his *gar¹…*garš² series covers 'rejoice', 'turn', 'be warm', 'coagulate', 'greet', 'swallow' — none of them the 'moisten' root Pokorny needs for the Persian branch.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Sanskrit\",\n     \"words\": \"ğar; â-gar\",\n     \"verdict\": \"disputed\",\n     \"derivation\": \"Two different Sanskrit items are merged here, and neither carries the gloss the chart gives it. (a) 'ğar : milk, also anything wet': there is no Sanskrit word ghar- meaning 'milk'. What exists is the verbal root GHAR / ghṛ, 3sg. jígharti, gharati 'to sprinkle, besprinkle, moisten' (so Walde-Pokorny I 607 and Pokorny 446, both quoting Uhlenbeck) and the deverbal noun ghṛtá- 'ghee, clarified butter' (lit. 'sprinkled/melted'). Nourai has collapsed the root ghar- and the noun ghṛtá- into one headword and given the root the noun's (approximate) meaning; 'anything wet' is a fair rendering of the verb, 'milk' is not. Moreover, modern Indology (Mayrhofer EWAia, followed by Wiktionary) separates ghṛtá- from ghṛ 'sprinkle' altogether and derives it from *gʷʰr̥-tós, root *gʷʰer- 'warm, hot', i.e. 'melted butter'. (b) 'â-gar : to soak, also to swallow' is Sanskrit ā + √gṝ (gar-) 'to swallow, devour' — a completely different root, PIE *gʷerh₃-, cf. Cheung's *garH³ 'to swallow' with Lat. vorāre, Gk. bibrṓskō, OCS požrěti. Nourai's own NOTE flags this ('AEF:40 lists the Latin word Vorâre:to swallow as a cognate. See root Gwer 3:to swallow'), and the note is correct: that word does not belong under Gherto. The NOTE's attribution is also accurate — Horn no. 36 (the German original of AEF) does cite lat. vorāre there. The 'to soak' sense that Nourai attaches to ā-gar- is really Horn's observation about the PERSIAN verb, not about Sanskrit.\",\n     \"derivation_fa\": \"در این جعبه دو چیز جداگانهٔ سنسکریت درهم آمیخته و هیچ‌کدام معنایی را که نمودار می‌دهد ندارد. نخست، در سنسکریت واژه‌ای به‌صورت ghar به معنی «شیر» نداریم؛ آنچه هست ریشهٔ فعلی GHAR/ghṛ با صورت‌های jígharti و gharati «پاشیدن، نم زدن، تر کردن» است (والده-پوکورنی، ج ۱ ص ۶۰۷ و پوکورنی ص ۴۴۶، به نقل از اولنبک) و نامواژهٔ ghṛtá- «روغن گداخته، کره». نورایی این دو را یکی کرده و معنی نامواژه را به ریشهٔ فعلی داده است؛ «هر چیز تر» ترجمهٔ پذیرفتنی فعل است، ولی «شیر» نه. افزون بر آن، هندشناسی امروزی (مایرهوفر) ghṛtá- را از ghṛ «پاشیدن» جدا و از *gʷʰr̥-tós ریشهٔ *gʷʰer- «گرم» می‌گیرد. دوم، â-gar همان ā + √gṝ «بلعیدن» است، از ریشهٔ هندواروپایی دیگری (*gʷerh₃-)، هم‌ریشه با vorāre لاتینی و در فهرست چونگ زیر *garH³ «بلعیدن»؛ خود نورایی هم در یادداشت به ریشهٔ «Gwer 3» ارجاع داده و این ارجاع درست است. پژوهش امروزی این جعبه را چنان‌که کشیده شده نمی‌پذیرد.\",\n     \"sources\": [\"https://en.wiktionary.org/wiki/%E0%A4%98%E0%A5%83%E0%A4%A4\"],\n     \"ref_check\": [\n      {\"ref\": \"POK:446\", \"status\": \"partial\", \"note\": \"Pokorny p.446 does give 'Old Indic ghṛtám \\\"skimmings, butter, melting butter\\\"; after Uhlenbeck to jígharti (gharati) \\\"sprays, sprinkles\\\"' — so the root ghar- and the noun are both there, but as two distinct things, and Pokorny nowhere glosses ghar- as 'milk'. Nothing on p.446 supports ā-gar- 'to swallow' under this lemma.\"},\n      {\"ref\": \"AEF:40\", \"status\": \"supports\", \"note\": \"AEF (Khaleqi-Motlaq's Persian version of Horn) is not online, so the page number cannot be verified; but the corresponding entry in the German original, Horn, Grundriss no. 36 (p. 9, HRN.txt leaf 30), reads 'āγārden, aγāriden „Verschlingen“. ai. ā + √gar- (jagāra) „verschlingen“; lat. vorāre, waχ. nez-γar-am „verschlingen“.' — exactly the Latin cognate Nourai's NOTE attributes to AEF:40.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"WLD\", \"where\": \"Bd. I 607 s.v. gherto-\", \"stance\": \"partial\", \"note\": \"'Ai. ghṛtám „Rahm, Butter, Schmelzbutter“ … Nach Uhlenbeck zu jígharti (gharati) „besprengt, beträufelt“' — supports ghar- 'sprinkle', not ghar- 'milk'.\"},\n      {\"src\": \"CHEUNG\", \"where\": \"s.v. *garH³ 'to swallow' (CHEUNG.txt l. 7948 ff.)\", \"stance\": \"contradicts\", \"note\": \"'*garH³ \\\"to swallow\\\" … *SANSKRIT: gar \\\"to devour, swallow\\\" (RV+) … *PIE *gʷerH₃- \\\"to devour, consume (wholly)\\\" … *IE COGNATES: Gr. bibrṓskō, Lat. vorāre …' — the 'swallow' word belongs to *gʷerh₃-, not to Gherto.\"},\n      {\"src\": \"POK\", \"where\": \"IEW 446\", \"stance\": \"partial\", \"note\": \"as in ref_check.\"},\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985\", \"stance\": \"silent\", \"note\": \"no lemma gherto-; Watkins' gʷerə-4 (the 'swallow' root) covers vorāre/-vorous separately, agreeing with Cheung.\"}\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"Persian\",\n     \"words\": \"âğâr «آغار»; âğârîdan «آغاریدن»; âğeštan «آغشتن»; âğar «آغر»\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"All four Persian words are real and well documented. Borhan-e Qateʿ p.47 (BQT_v1_pages.txt leaf 257) has, in sequence, آغار 'هر چیزی نم‌کشیده و خیسیده از آب یا از خون … و فرو شدن نم باشد بزمین و آمیخته و بهم پیوسته و سرشته', آغارد, آغاردن 'سرشتن و برانگیزانیدن و تحریک نمودن، و فرو شدن … بزمین' and آغاریدن 'بمعنی آغاردن است … و فرو کردن نم بود بزمین' — i.e. exactly Nourai's glosses 'wetness/humidity' and 'to soak'. Moʿin's Farhang links the whole family (آغاردن ← آغاریدن; آغردن = آغاریدن، آغشتن; آغشتن < آغردن ← آغاردن), so آغشتن 'to soak in, mix with' is the same verb with the past stem in -št- (present stem آغار-, past stem آغشت-, as Wiktionary's paradigm confirms). Morphologically these are ā- (preverb, Old Iranian *ā-) + a stem γār-/γašt-, whence the two Persian formations: a denominal-looking present stem āγār- with the New Persian infinitive -īdan, and the older -tan infinitive with the -št- past. As to the ETYMOLOGY the chart draws: the connection to Sanskrit ghar-/jígharti 'to sprinkle' is not Nourai's own — it is Uhlenbeck's, taken over verbatim by Walde-Pokorny I 607 ('np. a-γārdan „vermischen, einweichen“') and by Pokorny 446 ('npers. a-γārdan „blend, mix, soak\\\"'), so the arrow is the handbook view. But two reservations keep this from 'confirmed': (i) as drawn the Persian hangs UNDER Sanskrit, whereas the relation is cognacy, not descent — a New Persian verb cannot derive from Sanskrit; the real chain would be Old Iranian *ā-gar- / *ā-garH- > MP > NP, and no Middle Persian intermediate is attested (MacKenzie and Nyberg have none, Cheung has no such Iranian root at all); (ii) Horn himself, at the very page Nourai cites, is tentative — after rejecting the 'swallow' sense he writes 'In der letzten Bedeutung könnte es zu skr. √ghar-, ghárati \\\"besprengen, beträufeln\\\" gehören' ('could belong to'). Nourai's fourth word آغر 'water puddles in a dried river' is the rarer variant that Borhan/Moʿin record as آغر/اغر (Moʿin: 'اغر [= اغور، قس. آغار، آغال]'); it is the same family. The Nāser-Khosrow šāhed printed in the box was not independently located in a divan.\",\n     \"derivation_fa\": \"هر چهار واژه در فارسی گواه دارند. برهان قاطع (چاپ معین) ص ۴۷ به ترتیب می‌آورد: «آغار: هر چیزی نم‌کشیده و خیسیده از آب یا از خون بود، و فرو شدن نم باشد بزمین، و آمیخته و بهم پیوسته و سرشته را نیز گویند»؛ «آغاردن: سرشتن و برانگیزانیدن و تحریک نمودن، و فرو شدن … بزمین»؛ «آغاریدن: بمعنی آغاردن است». فرهنگ معین نیز همهٔ این خانواده را به هم می‌پیوندد (آغاردن ← آغاریدن؛ آغردن = آغاریدن، آغشتن؛ آغشتن < آغردن ← آغاردن)، پس «آغشتن» با ستاک حال «آغار-» و ستاک گذشتهٔ «آغشت-» همان فعل است و پیشوند ā- (ایرانی باستان *ā-) بر ستاک γār- افزوده شده. اما دربارهٔ ریشه‌شناسی: پیوند دادن این واژه‌ها به ghar-/jígharti سنسکریت «پاشیدن، نم زدن» از آنِ اولنبک است که والده-پوکورنی (ج ۱ ص ۶۰۷) و پوکورنی (ص ۴۴۶) هر دو با همان صورت a-γārdan نقل کرده‌اند؛ پس پیکان نورایی همان دیدگاه کتاب‌های مرجع است. دو ملاحظه مانع از «تأیید کامل» است: نخست آنکه در نمودار، فارسی زیرِ سنسکریت کشیده شده، حال آنکه این دو هم‌ریشه‌اند نه پدر و فرزند و فارسی نو نمی‌تواند از سنسکریت بیاید؛ صورت میانجی فارسی میانه هم گواه ندارد (نه مکنزی، نه نیبرگ، نه چونگ). دوم آنکه خودِ هرن در همان صفحهٔ ۹ محتاطانه می‌نویسد این واژه «می‌تواند» به ghar- سنسکریت بپیوندد. حکم: با احتیاط پذیرفتنی است.\",\n     \"sources\": [\"https://en.wiktionary.org/wiki/%D8%A2%D8%BA%D8%B4%D8%AA%D9%86\"],\n     \"ref_check\": [\n      {\"ref\": \"POK:446\", \"status\": \"supports\", \"note\": \"Pokorny p.446 s.v. gherto- prints the Persian word himself: 'npers. a-γardan \\\"blend, mix, soak\\\"' — Nourai's arrow is Pokorny's.\"},\n      {\"ref\": \"HRN:9\", \"status\": \"partial\", \"note\": \"Horn, Grundriss no. 36, p. 9 (HRN.txt leaf 30): 'āγārden, aγāriden „Verschlingen“. ai. ā + √gar- … In der Bedeutung „Verschlingen“ vermag ich das Wort nicht zu belegen. Bei AM. … bedeutet es immer „vermischen, einweichen in“. In der letzten Bedeutung könnte es zu skr. √ghar-, ghárati „besprengen, beträufeln“ gehören' (footnote: 'Dazu wohl auch āγisten'). Horn supports the meaning 'to soak/mix' and the ghar- connection, but only as a possibility, and he files the word primarily under the 'swallow' root.\"},\n      {\"ref\": \"AEF:41\", \"status\": \"supports\", \"note\": \"AEF is the Persian translation of Horn; p.41 of the translation corresponds to Horn's no.36/37 area. The Persian edition is not online, so the page number itself is unverifiable, but the content check was done on the German original (above).\"},\n      {\"ref\": \"BQT:47\", \"status\": \"supports\", \"note\": \"Borhan-e Qateʿ, Moʿin's ed., printed p.47 = BQT_v1_pages.txt leaf 257 (offset printed ≈ leaf − 210): 'آغار … هر چیزی نم کشیده و خیسیده از آب یا از خون بود؛ و فرو شدن نم باشد بزمین …' followed by آغارد / آغاردن / آغاریدن. Exactly the words and glosses of the node.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BQT\", \"where\": \"vol. 1, printed p.47 (leaf 257)\", \"stance\": \"supports\", \"note\": \"quoted above; Borhan carries آغار، آغارد، آغاردن، آغاریدن on one page, as the node has them.\"},\n      {\"src\": \"MON\", \"where\": \"Farhang-e Farsi (2-vol. Adena condensation), MON_part1.txt ll. 3635-3698\", \"stance\": \"supports\", \"note\": \"'آغاردن [ - آغاریدن]'، 'آغاریدن … خیساندن، تر کردن، نم…'، 'آغردن [- آغاریدن، آغشتن]'، 'آغشتن [< آغردن - آغاردن]' — Moʿin explicitly makes آغشتن and آغاردن/آغاریدن/آغردن one family, which is what the node assumes.\"},\n      {\"src\": \"HRN\", \"where\": \"no. 36, p. 1-9\", \"stance\": \"partial\", \"note\": \"as in ref_check: 'könnte … gehören' — a possibility, not a settled derivation.\"},\n      {\"src\": \"HUB\", \"where\": \"Persische Studien, greps for āγār-/āγist-/gharati/besprengen\", \"stance\": \"silent\", \"note\": \"Hübschmann has no entry for this verb (repeated greps in HUB.txt on agar/ayar/agist/ayist/gharati returned only unrelated matches).\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. I 607\", \"stance\": \"supports\", \"note\": \"'np. a-γārdan „vermischen, einweichen“' cited by Uhlenbeck's authority — the source of Pokorny's line.\"},\n      {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary\", \"stance\": \"silent\", \"note\": \"no Middle Persian *āgār-/āgašt- is listed, so the Old/Middle Iranian stage of the verb is undocumented.\"}\n     ]\n    },\n    {\n     \"id\": 3,\n     \"lang\": \"Persian\",\n     \"words\": \"farğârîdan «فرغاریدن ، فرغردن»; farğâr «فرغار»; farğar «فرغر»; farğan «فرغن»; farğandeh «فرغنده»\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"This second Persian box is the prefixed doublet of the first: far-/fra- (Old Iranian preverb *fra- 'forth') + the same γar- stem, beside ā- + γar-. All five words are attested. Borhan-e Qateʿ printed p.1465 (vol. 3, pdf p.258 of the picofile scan; fetched with tools/ref_page.py BQT:1465) gives فرغاردن/فرغاریدن 'تر کردن و خیساندن در آب و غیره … و بهم سرشتن و آغشته کردن باشد'; فرغر 'رودی را گویند که سیلاب از آنجا گذشته باشد و در هر جایی از آن قدری آب ایستاده … که آن را غدیر خوانند'; فرغن 'جوی [آب] که تازه احداث کرده باشند و آب در آن روان کنند'; فرغند 'بمعنی فرخنده … و چیزی بدبوی و ناخوش و گنده باشد'. Moʿin's Farhang repeats all of them (فرغار 'خیسانیده، نیک تر شده، سرشته گردیده، آغشته'; فرغر 'جوی آب … خشک رودی که سیلاب از آنجا گذشته'; فرغن 'جویی که تازه احداث کرده و آب در آن روان کنند'; فرغند [= فرغنده] 'پلید؛ بد'). Decisively for Nourai's arrow, Moʿin's OWN etymological footnote on that Borhan page reads 'از: فر (پیشوند) + غر (سانسکریت ghar/ghṛ «تر کردن»)، ویلیامز ۳:۷۹ و ۲:۳۷۸؛ رک: فرغردن، فرغرده، فرغار، فرغاردن' — i.e. Moʿin derives the whole set from the preverb far- plus the very Sanskrit root ghar- that the chart's parent node names, citing Monier-Williams. Two caveats: (i) again the arrow is drawn out of Sanskrit rather than as a cognate — the Persian is an inherited Iranian formation *fra-gar-, not a loan from Indic; (ii) farγandeh 'rotten' is the weakest member — Borhan's headword is فرغند (not فرغنده) and its first meaning there is 'فرخنده' (auspicious), the 'foul, stinking' sense resting on Rudaki's فرغندآسا, which Henning (Two Central Asian Words, p.154; BSOAS X/1 p.102 n.4) read as فژغند 'filthy', a different word. Nourai's translation 'to soak' for farγārīdan and 'little puddles of water in a dried river' for farγar are otherwise accurate.\",\n     \"derivation_fa\": \"این جعبه دوگانهٔ پیشونددارِ جعبهٔ پیشین است: پیشوند ایرانی باستان *fra- «پیش، فرا» بر همان ستاک γar-، در برابر ā- + γar-. هر پنج واژه گواه دارند. برهان قاطع، ص ۱۴۶۵ (ج ۳ اسکن، با ابزار ref_page.py گرفته شد): «فرغاردن/فرغاریدن: تر کردن و خیساندن در آب و غیره … و بهم سرشتن و آغشته کردن»؛ «فرغر: رودی را گویند که سیلاب از آنجا گذشته باشد و در هر جایی از آن قدری آب ایستاده … که آن را غدیر خوانند»؛ «فرغن: جویی که تازه احداث کرده باشند و آب در آن روان کنند»؛ «فرغند: بمعنی فرخنده … و چیزی بدبوی و ناخوش و گنده». فرهنگ معین نیز همه را می‌آورد. مهم‌تر آنکه حاشیهٔ ریشه‌شناسی خودِ معین در همان صفحهٔ برهان می‌گوید: «از: فر (پیشوند) + غر (سانسکریت ghar «تر کردن»)، به نقل از ویلیامز» ــ یعنی همان پیوندی که نمودار نورایی می‌کشد. دو نکته: نخست آنکه باز هم پیکان از سنسکریت کشیده شده حال آنکه ساخت *fra-gar- ارثی ایرانی است نه وام از هندی؛ دوم آنکه «فرغنده: گندیده» سست‌ترین حلقه است، زیرا سرواژهٔ برهان «فرغند» است و معنی نخست آن «فرخنده»، و هنینگ صورت رودکی را «فژغند» به معنی پلید خوانده که واژه‌ای دیگر است. حکم: با احتیاط پذیرفتنی است.\",\n     \"sources\": [],\n     \"ref_check\": [\n      {\"ref\": \"BQT:1465\", \"status\": \"supports\", \"note\": \"Verified via python3 tools/ref_page.py BQT:1465 --image (vol. 3 scan, pdf p.258; the [pdf page 258] block of BQT_v3_pages.txt). The page carries فرغاردن/فرغاریدن، فرغر، فرغرده، فرغن، فرغند in that order, plus Moʿin's footnote 'از: فر (پیشوند) + غر (سانسکریت ghar … «تر کردن») ویلیامز ۳:۷۹ و ۲:۳۷۸؛ رک: فرغردن، فرغرده، فرغار، فرغاردن'. The page number is exact and the footnote states Nourai's own etymology.\"},\n      {\"ref\": \"FRS:98\", \"status\": \"partial\", \"note\": \"Loghat-e Fors has the word: FRS_pages.txt leaf 163, 'فرغر: جایی باشد که از آنجا آب رفته باشد و هر جایی پاره[ای] مانده باشد' with Farrokhi's verse '… که شهریارا دریا تویی و من فرغر' — the very šāhed Nourai prints. But the local copy is Eqbal's 1319 edition, whose pagination differs from the Kharazmi 1365 edition Nourai cites, so p.98 itself could not be confirmed. Asadi gives no etymology (FRS is a lexicon of rare words).\"},\n      {\"ref\": \"MON:2520\", \"status\": \"supports\", \"note\": \"Content confirmed in MON_part2.txt ll. 6372-6392 (2-vol. Adena condensation): فرغار، فرغر، فرغرده، فرغن، فرغند [= فرغنده] with the glosses the node gives. The 6-vol. Amir Kabir edition Nourai paginates is not online, so page 2520 itself is unverifiable.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BQT\", \"where\": \"vol. 3, printed p.1465\", \"stance\": \"supports\", \"note\": \"text and Moʿin's footnote quoted above; note also Moʿin's n.7 on فرغند citing Henning, 'Two Central Asian Words' p.154 and BSOAS X/1 p.102 n.4, reading فژغند 'filthy' — which undercuts farγandeh 'rotten' as a member of this family.\"},\n      {\"src\": \"MON\", \"where\": \"MON_part2.txt ll. 6372-6392\", \"stance\": \"supports\", \"note\": \"'فرغار … خیسانیده، نیک تر شده، سرشته گردیده، آغشته'; 'فرغر … جوی آب. جایی که آب از آن گذشته و مقدار کمی آب بجا مانده باشد'; 'فرغن [- فرکن] جویی که تازه احداث کرده و آب در آن روان کنند'; 'فرغند [- فرغنده] پلید؛ بد'.\"},\n      {\"src\": \"FRS\", \"where\": \"Loghat-e Fors, leaf 163 (Eqbal ed.)\", \"stance\": \"supports\", \"note\": \"the فرغر entry with Farrokhi's line; the oldest attestation of the word (5th/11th c.).\"},\n      {\"src\": \"HRN\", \"where\": \"Grundriss, grep far-γar/farγārīdan\", \"stance\": \"silent\", \"note\": \"Horn has no entry for the fra- prefixed doublet; he treats only āγārden (no.36).\"},\n      {\"src\": \"CHEUNG\", \"where\": \"Etym. Dict. of the Iranian Verb\", \"stance\": \"silent\", \"note\": \"no Iranian root *gar- 'to moisten' and no *fra-gar- entry, so the Old Iranian stage of فرغاردن is not independently reconstructed.\"}\n     ]\n    }\n   ]\n  }\n ]\n}\n\nwith open('/home/sfmqrb/git/rishe/data/verification/page-190.json','w',encoding='utf-8') as f:\n    json.dump(data,f,ensure_ascii=False,indent=2)\n    f.write('\\n')\nprint('ok')\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build190.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-190.json > /dev/null && echo \"JSON OK\" && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 190"
}
```


### [2026-09-06T02:25:53.790Z] TOOL RESULT

```
ok
JSON OK
nodes verified: 6/6
node verdicts: {'confirmed': 3, 'disputed': 1, 'plausible': 2}
root verdicts: {'confirmed': 1, 'plausible': 1}
ref checks: {'supports': 9, 'not_checked': 1, 'partial': 3}
books consulted: {'supports': 14, 'silent': 7, 'partial': 4, 'contradicts': 1} | by book: {'WLD': 4, 'CHEUNG': 3, 'KLN': 3, 'LAT': 2, 'AHD': 2, 'BQT': 2, 'MON': 2, 'HRN': 2, 'BRT': 1, 'SKT': 1, 'POK': 1, 'HUB': 1, 'PHD': 1, 'FRS': 1}
```


## [2026-09-06T02:25:59.493Z] TOOL CALL #59: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg190.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/190.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/190.png && head -c 3 /home/sfmqrb/git/rishe/data/verification/page-190.json | xxd"
}
```


### [2026-09-06T02:26:01.234Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 65970 Sep  5 22:26 /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/190.png
00000000: 7b0a 20                                  {.
```


## [2026-09-06T02:26:22.028Z] AGENT

Page 190 (book p. 160) verified. `verify_check.py 190`: 6/6 nodes, **0 PROBLEM lines**.

**Verdicts** — roots: 1 confirmed, 1 plausible. Nodes: 3 confirmed, 2 plausible, 1 disputed.
Ref checks: 9 supports, 3 partial, 1 not_checked. Books consulted: 14 supports, 4 partial, 1 contradicts, 7 silent (POK, WLD I 607/610, AHD/Watkins, KLN, BRT, LAT, SKT, HRN, HUB, BQT v1+v3, MON, FRS, PHD, CHEUNG, ARY, Wiktionary, Etymonline).

**Entry 1 — Ghers (confirmed).** POK 445-446 has the lemma verbatim; Nourai's gloss "to be horrified, to stare" is a loose rendering of Pokorny's German *starren* (really "to bristle"). Avestan `zaršayamna-` checked in Bartholomae AiW col. 1684-85 (Yt 14.20) with his footnote "zarš- aus ir. \*žṛš- = lat. horrē-"; KLN:744 is the exact source of the English gloss. Latin/English chain standard.

**Entry 2 — Gherto (plausible).** Nourai copies POK 446 faithfully (including Pokorny's own "npers. a-γārdan"), but the lemma rests on two witnesses and modern work (Mayrhofer/Wiktionary) takes Skt. *ghṛtá-* to *\*gʷʰer-* "warm" instead.

**Disputed item:**
- Gherto, node #1 Sanskrit `ğar; â-gar` — no Sanskrit word *ghar* "milk"; the box merges the verb root *ghar-/jígharti* "to sprinkle" with the noun *ghṛtá-* "ghee", and its second word *ā-gar-* "to swallow" belongs to PIE *\*gʷerh₃-* (Cheung *\*garH³*, Lat. *vorāre*) — as Nourai's own NOTE concedes.

**Notable finds:** Moʿin's etymological footnote on BQT p.1465 independently gives "فر (پیشوند) + غر (سانسکریت ghar «تر کردن»)، ویلیامز" — i.e. Nourai's arrow for the *farγār-* set is Moʿin's own. Both Persian nodes are plausible rather than confirmed mainly because they are drawn as descending *from* Sanskrit (they are cognates; no MP intermediate in MacKenzie/Nyberg/Cheung), and Horn p.9 only says the *ghar-* link "könnte" hold. `farγandeh` "rotten" is the weakest word: Borhan's headword is فرغند, first sense "فرخنده", and Henning read Rudaki's form as فژغند "filthy".

**Extraction error for the owner to fix:** the printed chart has a fourth box in entry 1 — a blank double-bordered box that the Avestan node arrows into (top right, verified on the 400 dpi render). `data/extracted/batch/page-190.json` omits it entirely; it should appear as a pass-through node with no language and no words. No transcription flags otherwise: `ğar` / `â-gar` (differing diacritics), `آغر`, `فرغنده` and both verse quotations all match the printed page. Page image saved to `data/verification/sources/refs/ocr/BOOK/190.png`; 4 web pages archived via `fetch_source.py`.
