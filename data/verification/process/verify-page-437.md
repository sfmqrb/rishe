# Verification process log — verify-page-437


## [2026-09-14T01:30:29.030Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 437 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-437.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-437.json. Write /home/sfmqrb/git/rishe/data/verification/page-437.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 437` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T01:30:30.183Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T01:30:31.003Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T01:30:31.023Z] TOOL RESULT

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


## [2026-09-14T01:30:31.502Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-437.txt"
}
```


### [2026-09-14T01:30:31.522Z] TOOL RESULT

```
1	=== PDF page 437 (book page 407) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Seiku, Seikw : to flow  (refs OEW:340; POK:893)
4	#1 (parent #0) [Avestan] refs=POK:893 | haek 2, hinčaiti, hičaiti : flows from ; hixra : liquid increment ; fra-šaĕkam : spilling ☞Per 1
5	  #2 (parent #1) [Persian] refs=AEF:391; MON:799 | pašanjîdan «پشنجیدن» : sprinkle | extra: پشنگ ، پشنگه
6	#3 (parent #0) [Sogdian] refs=SOD:303 | pšync : to sprinkle
7	#4 (parent #0) [Latin] refs=AHD | siccus : flowed out, dry
8	  #5 (parent #4) [French] refs=AHD:1141 | sec : without water
9	    #6 (parent #5) [Persian] refs=VOP:213 | sek «سک» : non-diluted drink
10	    #7 (parent #5) [English] refs=AHD:1141; OEW:346 | sack : a dry strong wine
11	  #8 (parent #4) [English] refs=AHD; OEW | desiccate : to dry out
12	#9 (parent #0) [Sanskrit] refs=POK:893 | sincati : flows from
13	--- entry 1 ---
14	ROOT Seikw -> redirect to Seiku
15	--- entry 2 ---
16	ROOT [Indo-European] Seip : to pour out, drip  (refs POK:894)
17	#1 (parent #0) [Latin] refs=POK:894; AHD | sâpô : soap
18	  #2 (parent #1) [Greek] refs=BQT:1330 | sapôn : soap
19	    #3 (parent #2) [Arabic] refs=TAD:43 | sâboun : soap
20	      #4 (parent #3) [Persian] refs=MON:2118 | sâbŭn «صابون» : soap
21	#5 (parent #0) [Germanic] refs=AHD | 
22	  #6 (parent #5) [English] refs=None | soap, sip, sieve
23	
```


## [2026-09-14T01:30:33.220Z] AGENT

I'll work through Bash where possible. Let me start by examining the source JSON and reference infrastructure.


## [2026-09-14T01:30:34.685Z] TOOL CALL #3: Bash

```json
{
 "command": "python3 -m json.tool data/extracted/batch/page-437.json | head -200",
 "description": "Read source JSON for page 437"
}
```


## [2026-09-14T01:30:35.403Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-14T01:30:35.952Z] TOOL RESULT

```
{
    "pdf_page": 437,
    "book_page": 407,
    "entries": [
        {
            "root": {
                "name": "Seiku, Seikw",
                "lang": "Indo-European",
                "refs": "OEW:340; POK:893",
                "gloss": "to flow"
            },
            "nodes": [
                {
                    "id": 1,
                    "parent": 0,
                    "lang": "Avestan",
                    "refs": "POK:893",
                    "words": [
                        {
                            "translit": "haek 2, hin\u010daiti, hi\u010daiti",
                            "gloss": "flows from",
                            "script": null
                        },
                        {
                            "translit": "hixra",
                            "gloss": "liquid increment",
                            "script": null
                        },
                        {
                            "translit": "fra-\u0161a\u0115kam",
                            "gloss": "spilling",
                            "script": null,
                            "see": [
                                "Per 1"
                            ]
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 2,
                    "parent": 1,
                    "lang": "Persian",
                    "refs": "AEF:391; MON:799",
                    "words": [
                        {
                            "translit": "pa\u0161anj\u00eedan",
                            "gloss": "sprinkle",
                            "script": "\u067e\u0634\u0646\u062c\u06cc\u062f\u0646"
                        }
                    ],
                    "script_extra": "\u067e\u0634\u0646\u06af \u060c \u067e\u0634\u0646\u06af\u0647",
                    "note": null,
                    "quote": {
                        "text": "\u0628\u0647 \u062e\u0646\u062c\u0631 \u0647\u0645\u0647 \u062a\u0646\u0634 \u0627\u0646\u062c\u06cc\u062f\u0647 \u0627\u0646\u062f - \u0628\u0631 \u0622\u0646 \u062e\u0627\u06a9 \u0648 \u062e\u0648\u0646\u0634 \u067e\u0634\u0646\u062c\u06cc\u062f\u0647 \u0627\u0646\u062f",
                        "poet": "Lab\u00eeb\u00ee"
                    }
                },
                {
                    "id": 3,
                    "parent": 0,
                    "lang": "Sogdian",
                    "refs": "SOD:303",
                    "words": [
                        {
                            "translit": "p\u0161ync",
                            "gloss": "to sprinkle",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 4,
                    "parent": 0,
                    "lang": "Latin",
                    "refs": "AHD",
                    "words": [
                        {
                            "translit": "siccus",
                            "gloss": "flowed out, dry",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 5,
                    "parent": 4,
                    "lang": "French",
                    "refs": "AHD:1141",
                    "words": [
                        {
                            "translit": "sec",
                            "gloss": "without water",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 6,
                    "parent": 5,
                    "lang": "Persian",
                    "refs": "VOP:213",
                    "words": [
                        {
                            "translit": "sek",
                            "gloss": "non-diluted drink",
                            "script": "\u0633\u06a9"
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 7,
                    "parent": 5,
                    "lang": "English",
                    "refs": "AHD:1141; OEW:346",
                    "words": [
                        {
                            "translit": "sack",
                            "gloss": "a dry strong wine",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 8,
                    "parent": 4,
                    "lang": "English",
                    "refs": "AHD; OEW",
                    "words": [
                        {
                            "translit": "desiccate",
                            "gloss": "to dry out",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 9,
                    "parent": 0,
                    "lang": "Sanskrit",
                    "refs": "POK:893",
                    "words": [
                        {
                            "translit": "sincati",
                            "gloss": "flows from",
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
                "name": "Seikw",
                "redirect": "Seiku"
            },
            "nodes": []
        },
        {
            "root": {
                "name": "Seip",
                "lang": "Indo-European",
                "refs": "POK:894",
                "gloss": "to pour out, drip"
            },
            "nodes": [
                {
                    "id": 1,
                    "parent": 0,
                    "lang": "Latin",
                    "refs": "POK:894; AHD",
                    "words": [
                        {
                            "translit": "s\u00e2p\u00f4",
                            "gloss": "soap",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 2,
                    "parent": 1,
                    "lang": "Greek",
```


### [2026-09-14T01:30:36.031Z] TOOL RESULT

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


## [2026-09-14T01:30:40.730Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/extracted/batch/page-437.json'))\nprint(json.dumps(d['entries'][2],ensure_ascii=False,indent=1))\n\"",
 "description": "Print entry 2 JSON"
}
```


### [2026-09-14T01:30:41.872Z] TOOL RESULT

```
{
 "root": {
  "name": "Seip",
  "lang": "Indo-European",
  "refs": "POK:894",
  "gloss": "to pour out, drip"
 },
 "nodes": [
  {
   "id": 1,
   "parent": 0,
   "lang": "Latin",
   "refs": "POK:894; AHD",
   "words": [
    {
     "translit": "sâpô",
     "gloss": "soap",
     "script": null
    }
   ],
   "note": null,
   "quote": null
  },
  {
   "id": 2,
   "parent": 1,
   "lang": "Greek",
   "refs": "BQT:1330",
   "words": [
    {
     "translit": "sapôn",
     "gloss": "soap",
     "script": null
    }
   ],
   "note": null,
   "quote": null
  },
  {
   "id": 3,
   "parent": 2,
   "lang": "Arabic",
   "refs": "TAD:43",
   "words": [
    {
     "translit": "sâboun",
     "gloss": "soap",
     "script": null
    }
   ],
   "note": null,
   "quote": null
  },
  {
   "id": 4,
   "parent": 3,
   "lang": "Persian",
   "refs": "MON:2118",
   "words": [
    {
     "translit": "sâbŭn",
     "gloss": "soap",
     "script": "صابون"
    }
   ],
   "note": null,
   "quote": null
  },
  {
   "id": 5,
   "parent": 0,
   "lang": "Germanic",
   "refs": "AHD",
   "words": [],
   "note": null,
   "quote": null
  },
  {
   "id": 6,
   "parent": 5,
   "lang": "English",
   "refs": null,
   "words": [
    {
     "translit": "soap, sip, sieve",
     "gloss": null,
     "script": null
    }
   ],
   "note": null,
   "quote": null
  }
 ]
}
```


## [2026-09-14T01:30:42.313Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['OEW','POK','AEF','MON','SOD','AHD','VOP','BQT','TAD']:\n    print(k, json.dumps(d.get(k),ensure_ascii=False)[:700])\n    print()\n\"",
 "description": "Look up ref metadata"
}
```


### [2026-09-14T01:30:43.422Z] TOOL RESULT

```
OEW {"title": "J. T. Shipley, The Origins of English Words: A Discursive Dictionary of Indo-European Roots, Baltimore 1984", "edition_found": "1984 (lending-only)", "kind": "archive_restricted", "url": "https://archive.org/details/originsofenglish0000ship ; https://archive.org/details/originsofenglish00jose (both JHU 1984, borrowable) ; HathiTrust mdp.49015002910322 search-only ; Google ELSm5zUgP_wC no view", "identifier": "originsofenglish00jose (also originsofenglish0000ship)", "local_file": null, "page_offset": null, "lookup_hint": "Borrow via IA lending (djvu.txt returns 401/403). Entries are IE roots in alphabetical order; use IA's in-book search: https://archive.org/details/originsofenglis

POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index 

AEF {"title": "Jalal Khaleqi Motlaq, Asas-e Eshteqaq-e Farsi, vol. I (آ–خ), Bonyad-e Farhang-e Iran 1356/1977 — this is the Persian TRANSLATION of Paul Horn's Grundriss der neupersischen Etymologie (HRN) with Hübschmann's Persische Studien (HUB) notes and added Persian/Pahlavi evidence", "kind": "catalog", "url": "https://openlibrary.org/works/OL38785552W (vol. 1, 1356) ; 2015 complete ed. «فرهنگ ریشه‌شناسی فارسی» (مهرافروز) print-only: https://www.gisoom.com/book/11154690/ ; German original: https://archive.org/details/grundrissderneu00horngoog", "lookup_hint": "Not online (searched archive.org, ketabnak, noorlib, web; only bookshop listings). Because it is a translation of Horn/Hübschmann, ver

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol 

SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get s

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifie

VOP {"title": "Mahshid Moshiri, Farhang-e Vazheha-ye Orupayi dar Farsi, Alborz 1371/1992", "kind": "none", "url": null, "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: not found (only unrelated similar-title books, e.g. Zomorrodian's فرهنگ ریشه‌شناختی واژه‌های دخیل اروپایی, ketabnak 132354).", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: nothing — no catalogue record with a scan, no ebook. Decoys: ketabnak 132354 (Zomorrodian), Google Books RwdkAAAAMAAJ (Nahid Shahidi 1997, no view). Purchase second-hand only."}

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.c

TAD {"title": "Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-hurufihi (2nd ed. Cairo 1932, ed. Yusuf Tuma al-Bustani; later Library of Lebanon reprint) — Nourai lists it under Arabic authors ('Unaysi T.'); its Table IV line was lost in the OCR", "kind": "archive_djvu", "url": "https://archive.org/details/TOB1932ARAR (1932 ed.); also https://archive.org/details/ar113lang79 and https://archive.org/details/elshandawily14640", "lookup_hint": "Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; inside.php search works.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD_pag
```


## [2026-09-14T01:30:49.809Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i 'seiku\\|seikʷ\\|seiqʷ\\|seikų\\|sei-k' POK_full.txt | head -30; echo ---; grep -n 'siccus' POK_full.txt | head -20; echo ---SEIP; grep -n -i 'seip-\\|sēip\\|seib-' POK_full.txt | head -20",
 "description": "Grep Pokorny for seikw and seip"
}
```


### [2026-09-14T01:30:49.897Z] TOOL RESULT

```
---
72691:Latin 5/5/"oup£T'; siare\s probably from *s/(75/'e after /77e5/'e"mingere' reshaped; siccus 
---SEIP
48832:Root / lemma: kseip-, kseib- 
72727:because of seip- lies probably *sei- "drip, trickle, rinnen' the basic. 
72732:Root / lemma: seip-, seib-
```


## [2026-09-14T01:30:50.958Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==549' POK_02.txt | head -60",
 "description": "Print POK page 893 candidate"
}
```


### [2026-09-14T01:30:51.994Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T01:30:54.703Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '72640,72790p' POK_full.txt",
 "description": "Print Pokorny seikw / seip context"
}
```


### [2026-09-14T01:30:54.775Z] TOOL RESULT

```
'weitaus', 6xo(; ' holder, Bewahrer', 6x£U) 'hold, stijtze; hold from, (er)trage', 6x£U(; 'strap, 
the den helmet festhalt, clasp, hairpin, bar, bolt'; 

with a'£uu)X£w 'tische auf, bewirte rich' (lengthening after dem example the 
compounds); av-, 5i-, kqt-, auv-OKCoxH (in connection in Perf. -formations, as OTTwrrn 
produktiv gewordene lengthening); 

zero grade: laxw {*si-zgh-d) 'hold an, have', iaxac;f. 'anchor', ax£Tv (see above), ax£6- 
££iv, -£Tv, -t\xzy 'hold, stop', a-axzioc, 'unaufhaltsam; unertraglich (affliction)', axto\Q,i. 
'Haltung, state, status', ay^t^hoc, ' fatigueless, hartnackig' ('*withstanding '), aKzQ^bc, 
'concise, genau' ('*narrowly aniiegend'), ax£56v ' near, beinahe' ('*sich eng whereof 



holding '), axspot; 'ununterbrochen', sniaxspw Adv. ds., axnMa 'Haltung, shape, form', 
GXoAn "Einhalten, tranquility, leisure; (wissenschaftliche) occupation in Muftestunden' (ein 
with it the changing by ablaut *aGxaAo(; 'wer sich nicht halten kann' assumes man as base 
from aaxaAau), aaxaAAu) "bin unwilling, ungehalten, angry, irate'); iaxOq, -uo(; " strength 
'(*Fi-axu-(;) to Old Indie v/-sah-^\n the Gewalt have'; 

Celtic PN Segisu(*-d), Sego-maros, GN Segomd(n), f. Segeta, PN Sego-dunon, Sego- 
briga, Segontion, Middle Irish segvn. " strength ', cymr. /7y'bold'; cymr. haeddel. Middle 
Breton haezi, nbret. hea/t, ' 

plough handle, plough stilt ' (= exstAh "plough-handle', see above; a from e, also (?) in :) 
cymr. haer' entete, pressant ', Haer' woman's name ', haeru^ insure, affirm '; cymr. 
Middle Breton /75e/'cordial, genereux '; cymr. /7c»e/"clavus' {*soghla)\ 

lllyrian PN Segesta'm Pannonia, Liguria, Sicily; 

Gothic s/g/'sn. "victory'. Old High German s/g/'m. ds., german. PN Sigi-merus, Segi- 
mundus e\.c. (Indo Germanic neutr.-/5-or -es-stem). Old High German s/g/'ron'mn, 
triumph'; Old High German s/gum., Old English s/gorWctory', Old High German PN Sigur- 
mar{\v\6o Germanic neutr. -^s^stem). 

References: WP. II 481 f. 
Page(s): 888-889 

Root / lemma: seik"- 

Meaning: to spill, pour, draft 

Material: Old Indie secate, sincati {asicat) "giefttfrom, begieftt', seka-m. " downpour, 

Erguft, Besprengung', praseka-m. "Erguft, Ausguft'; Avestan haek-, hincaiti {hicaiti) "gieftt 

from', fra-saekam kbso\uWy "beimVergieften', hixra-v\. "fliJssiges Exkrement'; 

gr. T^ai 5ir|0ncfC(i Hes., Ionian iKpag " dampness ', iKpaA£0(; "humid, wet', iKpaivw " wet ', 
Tpuyoino(; "Mostsieb'; 

Latin 5/5/"oup£T'; siare\s probably from *s/(75/'e after /77e5/'e"mingere' reshaped; siccus 
"dry'; 

gall, (goidel. orVenetic-lllyrian) FIN Sequana ^Se\ne', GN Sinquatis, FIN *S/par/s^Se\/re' 
= Irish FIN Sechair, 



Old High German sJhan 'strain ', Old English seon ds., intr. "ausflieften'; Old High 
German Old Saxon Old English 5/^a/7 "tropfeind fall, sink, flow'. Old Icelandic s/galow, 
base or vorwarts glide, slide' (Modern High German vers/egen ior o\der verse/gen aiter 
dem Ptc. Middle High German versigen). Old High German ^/s/ig'palus, stagnum', 
Norwegian-Swedish sil {*sThila-) "side' (5//a" strain ', wherewith Norwegian sila 
"unaufhorlich rain' probably identical is). East Frisian 5/7'Schleuse', Middle Low German 
s/7"Schleuse, Ablaufkanal', s/7e/7"dranieren'; Old English seohtrei. {*sihtrdn-). Middle Low 
German sichter, sechter' drainage ditch '; Old Icelandic 5/5'Seihe' (schw. Verb s/5" strain 
'), Old English seohhei.. Old High German 5/77a"Seihe' {*s7h-udn-)\ 

Middle Low German se^e'triefend, blear eyed, bleareyed ', Middle Low German Middle 
High German se/ger" slowly or tenacious tropfeind, faint, languid, schal'. Old Icelandic 
se/g'/'"tough'; 

in Germanic also forms with Germanic k. Old High German Middle High German seich 
"urine' (Old High German seihhen. Middle High German seichen. Low German seken 
"urinate, to make water'). Old English 5/ice/75/7 "einsickern'. Low German sTkern, Modern 
High German sickern, Norwegian sikia, Swedish sikkla^ drool, drivel, slaver; trickle ' = Low 
German sikkelen, Norwegian dial. 5//r/5 "small stream, brook', sTka^ strain ', Old Icelandic 
sTku. "stehendes water'. Old English 5/c" watercourse ' etc.; 

nasallos serb. osye/ra "Ebbe' {*seka)\ Church Slavic sbcg, 5i.ca//" urinate, to make water 
', Iter. slov. s//ra// "hervorspritzen'; 

besides eine root seik"-^ dvj' , die probably about "abrinnen, versiegen = austrocken' 
mitse/Zr"'- "diffuse' to unite is: Avestan haecaye/t/wWh ^s "trocknet from' (trans.), haecah-u. 
" dryness, aridity ', hiku-^dxy'; 

because of seip- lies probably *sei- "drip, trickle, rinnen' the basic. 

References: WP. II 466 f., WH. II 531, Trautmann 260. 
Page(s): 893-894 

Root / lemma: seip-, seib- 

Meaning: to pour, rain, sift, *sieve, stream, trickle, dribble 

Material: Old High German sib, Dutch zeef. Middle Low German seven.. Old English sife 

n. " sieve ', in addition Old English siftan. Middle Low German siften, sichten. Modern High 

German (from dem Low German) sichten, and Old Icelandic se/n. "juncus' (because of 

porous stalks); Middle Low German Old Frisian sever xr\. "mucus, slobber'. Old High 



German seivar, Middle High German se/ferm. ds. (Middle High German seifelxr\. "saliva' 
perhaps with Germanic p, see below); md. 5/Te "marshy Bodenstelle'; serb. sfpiti^ trickle, 
fine rain'; 

in Germanic also forms with Germanic p (die den end auf Indo Germanic b 
rechtfertigen): Old English sTpian, Middle Low German s/77e/7"drip, trickle', Middle High 
German s/Te/? (stem V.) ds., Swedish dial. 5/pa "slow flow, seep, drip'. Middle Low German 
s/p'Bachlein', here also the Germanic name the 5e/ife.' Germanic *saip(i)d: F\v\v\\s\\ 
saip(p)io. Old High German sei(p)fa^ soap '; also "resin'. Middle Low German sepe^ soap 
', Old English sapei. (out of it nord. sapa) " soap ', Latin s^oo (Germanic loanword); 
maybe beside Germanic *sa/p(/)dn- a\so *sepon- ^taWow, suet (also to Haarfarbemittein 
verwendet)', das with Latin sebum "tallow, suet' (probably genuine Latin) was obtainable 
from Indo Germanic *se[i]bo- "dripping fat' (Latin /? would be then the origin of a root form 
in Indo Germanic b)\ Tocharian A sip-, sep- "anoint', sepaF ointment '. 

Maybe alb. ( *sepon-) sapun "soap', but older cognate zero grade alb. {*seifen) finje 
"soapsuds, lye' [the common drop of initial se- sounds in alb. as in alb. {*svasura-) vjeherr 
"father-in-law'] 

References: WP. II 467 f., WH. II 478, 504; 
See also: s. S. 889 under sei- 
Page(s): 894 

Root / lemma: sei-, soi- 

Meaning: to be damp, to drip 

Material: With /-formants: FIN: venet. Siiis, Siiarus, Ligurian Siiarus, lllyrian Silarus 

(Lukanien), hispan. Sit, Middle Irish s/M" drips, flows, allows to flow ', contaminated 

partially by 5e/-"to move, stir' (see below suel^. Old English sioiof^^sea'; Lithuanian seiie 

"saliva, slobber'; 

with /7^formants: cymr. bufen' skimmings' {*soimeno-)\ Old High German Modern High 
German seim^ honey ', Old Icelandic seimr^ honeycomb ', ablaut, simixw. "sea', Danish 
sima av^ dribble from ', westfal. sismern' seep, drip' (Old Saxon *simardn). 

References: WP. II 464 f.; 

See also: perhaps the base from se/fr^-and se//?- "diffuse'. 

Page(s): 889
```


## [2026-09-14T01:31:17.006Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== AHD seik ===\"; grep -n -i 'seik\\|seip\\|seib' AHD_watkins1985.txt | head -30; echo \"=== AHD siccus/desiccate/sapo ===\"; grep -n -i 'desiccate\\|siccus' AHD_watkins1985.txt | head; grep -n -i 'sāpo\\|sapo \\|soap' AHD_watkins1985.txt | head -20",
 "description": "Grep AHD Watkins"
}
```


### [2026-09-14T01:31:17.122Z] TOOL RESULT

```
=== AHD seik ===
912:grade form *séd-yo- in Germanic *(ge)sétjam, seat (*ge-, *ga-, collective prefix; see kom), in Old Norse szti, seat: SEAT. 7. Form *sed-é- in Latin sedére, (third person plural perfect indicative sédérunt), to sit: SEANCE, SED- ENTARY, SEDERUNT, SEDILIA, SEDIMENT, SESSILE, SES- SION, SEWER?, SIEGE; ASSESS, ASSIDUOUS, DISSIDENT, HOSTAGE, (INSESSORIAL), OBSESS, POSSESS, PRESIDE, RESIDE, (SUBSIDY), SUPERSEDE. 8. Reduplicated form *si-zd- in: a. Latin sidere, to sit down, settle: SUBSIDE; b. Greek hizein, to sit down, settle down: SYNIZESIS. 9. Lengthened-grade form séd- in Latin sédés, seat, residence: SEE?. 10. Lengthened-grade form *séd-d- in Latin séddre, to settle, calm down: SEDATE!. 11. Suffixed o-grade form *sod-yo- in Latin solium, throne, seat: SOIL}. 12. Suffixed form *sed-rd- in Greek hedra, seat, chair, face of a geometric solid: -HEDRON; CATHEDRA, (CHAIR), EPHEDRINE, EXEDRA, SANHEDRIN, TETRAHE- DRON. 13. Prefixed and suffixed form *pi-sed-yo-, to sit upon (*pi-, on; see epi), in Greek piezein, to press tight: PIEZO-; ISOPIESTIC. 14. Basic form *sed- in: a. Greek edaphos, ground, foundation (with Greek suffix -aphos): EDAPHIC; b. Sanskrit sad- in upanigad, Upanishad: UPANISHAD. 15. Suffixed form *sed-G-, seat, in Welsh sedd, seat: EISTEDDFOD. See also compound root nizdo-. [Pok. sed- 884.] sed-?. To go. Suffixed o-grade form *sod-o- in Greek hodos, way, journey: -ODE; ANODE, CATHODE, EPISODE, EXODUS, HYATHODE, METHOD, ODOGRAPH, ODOMETER, PERIOD, STOMODEUM, SYNOD. [Pok. sed- 887.] segh-. To hold. 1. Suffixed form *segh-es- in Germanic *sigiz, victory (< “a holding or conquest in battle”), in Old High German sigu, sigo, victory: SIEGFRIED. 2. Greek ekhein, to hold, possess, be in a certain condi- tion (> hexis, habit): HECTIC; CACHEXIA, ECHARD, EN- TELECHY, EUNUCH, OPHIUCHUS. 3. O-grade form *sogh- in Greek epokhé, “a holding back,” pause, cessation, position in time (epi-, on, at; see epi): EPOCH. 4. Zero-grade form “sgh- in: a. Greek skhéma, “a hold- ing,” form, figure: SCHEME; b. Greek skhoié, “a holding back,” stop, rest, leisure, employment of leisure in dispu- tation, school: (SCHOLAR), SCHOLASTIC, SCHOLIUM, SCHOOL/. 5. Reduplicated form *si-sgh- in Greek iskhein, to keep back: ISCHEMIA. [Pok. segh- 888.] seib-. To pour out, sieve, drip, trickle. 1. Basic form in Germanic “sipon in Old English sipian, sypian, to drip, seep: SEEP. 2. Suffixed o-grade form *soib-on- in Ger- manic *saipén-, “dripping thing,” resin, in: a. Old Eng- lish sdpe, soap (originally a reddish hair dye used by Germanic warriors to give a frightening appearance): SOAP; b. Latin sdp6, soap: SAPONATE, SAPONIFY, SAPO- NIN, SAPONITE; SAPONACEOUS. 3. Variant Germanic form *sib- in: a. Old English sife, a filter, sieve: SIEVE. b. Old English siftan, to sieve, drain: sirt. [Pok. seip- 894.] seikw-. To flow. Extended expressive zero-grade form *sikko- in Latin siccus, dry (probably < “flowed out”): SACK3, SECCO, SICCATIVE; DESICCATE, EXSICCATE. [Pok. seiku- 893.] sek-. To cut. 1. Germanic *segithd, sickle, in Old English sithe, sigthe, sickle: SCYTHE. 2. Suffixed o-grade form *sok-d- in Germanic *sag6, a cutting tool, saw, in Old English sagu, sage, saw: SAW. 3. Suffixed o-grade form *sok-yo- in Germanic *sagjaz, “sword,” plant with a cutting edge, in Old English secg, sedge: SEDGE. 4. Suf- fixed o-grade form *sok-so- in Germanic *sahsam, knife, sword, traditionally (but quite doubtfully) regarded as the source of West Germanic tribal name *Saxon-, Saxon (as if “warrior with knives”), in Late Latin Sax6 (plural Saxonés), a Saxon: Saxon. 5. Extended root *skend-, to peel off, flay, in Germanic *skinth- in Old Norse skinn, skin: SKIN. 6. Basic form “sek- in Latin secdre, to cut: SECANT, -SECT, SECTILE, SECTION, SECTOR, SEGMENT; DISSECT, EXSECT, INSECT, INTERSECT, NOTCH, RESECT, (TRANSECT). 7. Lengthened-grade form *sék- in Latin
1137:derivatives violdre, to treat with force, and violentus, vehement: VIM, VIOLATE, VIOLENT. [In Pok. 3. wei- 1123.] weik-', Clan (social unit above the household). 1. Suf- fixed form *weik-slé in Latin villa, country house, farm: VILLA, VILLAGE, VILLAIN, VILLANELLE, (VILLEIN); (BI- DONVILLE). 2. Suffixed o-grade form *woik-o- in: a. La- tin vicus, quarter or district of a town, neighborhood: (VICINAGE), VICINITY; b. Greek oikos, house, and its derivative oikia, dwelling: ANDROECIUM, AUTOECIOUS, DIOCESE, DIOECIOUS, DIOICOUS, ECESIS, ECOLOGY, ECON- OMY, ECUMENICAL, HETEROECIOUS, MONOECIOUS, PAR- IsH, TRIOECIOUS. 3. Zero-grade form *wik- in Sanskrit vis-, dwelling, house, with derivative vaisyah, settler: Vaisya. [Pok. weik- 1131.] weik-2. In words connected with magic and religious notions (in Germanic and Latin). 1. Germanic suffixed form *wih-l- in Old English wigle, divination, sorcery, akin to the Germanic source of Old French guile, cun- ning, trickery: GUILE. 2. Germanic expressive form *wikk- in: a. Old English wicca, wizard, and wicce, witch: WITCH; b. Old English wiccian, to cast a spell: BEWITCH. 3. Possible suffixed zero-grade form *wik-t- imé in Latin victima, animal used as sacrifice, victim (although this may belong to another root *(a)wek- not otherwise represented in English): vicTiM. [Pok. 1. weik- 1128.] weik-3, To be like. 1. Suffixed variant form ‘*eik-on- in Greek eikdn, likeness, image: ICON, (ICONIC), ICONO-; ANISEIKONIA. 2. Prefixed and suffixed zero-grade form *n-wik-és, not like (*n-, not; see ne), in Greek aikés, unseemly: AECIUM. [Pok. 3. weik- 1129.] weik-4. Also weig-. To bend, wind. I. Form weig-. 1. Ger- manic *wik- in: a. Old English wice, wych elm (having pliant branches): wyCH ELM; b. Swedish viker, willow twig, wand, akin to the Scandinavian source of Middle English wiker, wicker: WICKER; C. Old Norse vikja, to bend, turn, probably akin to the Scandinavian source of Old North French wiket, wicket (< “door that turns”): WICKET. 2. Germanic *waikwaz in: a. Old Norse veikr, pliant: WEAK; b. Dutch week, weak, soft: WEAKFISH. 3. Germanic *wik6n-, “a turning,” series, in Old English wicu, wice, week: WEEK. II. Form *weik-. Zero-grade form *wik- in: a. Latin vix (genitive vicis), turn, situ- ation, change: VICAR, (VICARIOUS), VICE; VICISSITUDE; b. Latin vicia, vetch (< “twining plant”): veTCH. [Pok. 4. ueik- 1130.] weik-5, To fight, conquer. 1. Germanic “wik- in Old Norse vigr, able in battle: WIGHT2. 2. Nasalized zero-grade form *wi-n-k- in Latin vincere (past participle victus), to conquer: VANQUISH, VICTOR, VINCIBLE; CONVINCE, EVICT. [Pok. 2. weik- 1128.] weip-. To turn, vacillate, tremble ecstatically. 1. O-grade form *woip- in Germanic *waif- in Old Norse veif, waving thing, flag, probably akin to the Scandinavian source of Anglo-Norman waif, ownerless property: WAIF!, (WAIVE), (WAIVER). 2. Variant form *weib- in Germanic *wipjan, to move back and forth, in: a. Old English wipian, to wipe: WIPE; b. Old French guiper, to cover with silk: GUIPURE; c. Middle Dutch and Middle Low German wippen, to swing: WHIP. 3. Perhaps suffixed nasalized zero-grade form *wi-m-p-ila- in: a. Old English wimpel, covering for the neck (< “something that winds around”): WIMPLE; b. perhaps Middle Dutch wimmel, auger (< “that which turns in boring”): WIMBLE. 4. Suf- fixed zero-grade variant form *wib-ro- in Latin vibrdre, to vibrate: VIBRATE. [Pok. weip- 1131.] weis-. To flow. I. 1. Germanic *wisdn-, waisén- in Old English wdse, mire, mud: 00ZE?. 2. Taken by many as a derivative of this root, but probably an independent Indo-European word, is the suffixed form *wis-o- in Latin virus, slime, poison: VIRUS. 3. Extended zero-grade form *wisk- possibly in Latin viscum, mistletoe, birdlime: VISCID, VISCOUS. II. Attributed by some to this root, but more likely of obscure origin, are some Germanic words
1246:ANILE an-! ANILINGUS 4no-, leigh- ANIMA ane ANIMADVERT ane- ANIMAL ane- ANIMATE ane ANIMATO ane- ANIMISM ane- ANIMOSITY ane- ANIMUS ane- ANION ei-1 ANISEIKONIA weik-3 ANKLE ank- ANKYLOSIS ank- ANLAGE an}, legh- ANNALS at- ANNEAL aidh- ANNEX ned- ANNIHILATE ne ANNIVERSARY at-, wer-3 ANNOTATE gno- ANNOUNCE neu-! ANNOY od-2 ANNUAL at ANNUITY at- ANNUL ne ANNULAR 4no- ANNULET 4no- ANNULUS 4no- ANODE sed-2 ANODYNE ed- ANOINT ong¥- ANOMALOUS sem-! ANOMIE nem- ANON ol-no- ANONYMOUS né-men- ANOPHELES obhel- ANORECTIC reg-1 ANOREXIA reg-1 ANORTHITE wrddh- ANOSMIA od-! ANSATE ans- ANSERINE ghans- ANSWER swer-1 ANT mai-1
1487:EXPOSTULATE prek- EXPOUND apo- EXPRESS per-5 EXPUNGE peuk- EXPURGATE peue- EXQUISITE quaerere EXSCIND skei- EXSECT sek- EXSICCATE seikw- EXTANT sta- EXTEND ten- EXTENUATE ten- EXTERIOR eghs EXTERMINATE ter- EXTERNAL eghs EXTINGUISH  steig-
2207:SABULOUS bhes-1 SACERDOTAL sak- SACK? = seikw- SACKBUT bhau- SACRED Sak- SACRIFICE dhé-1 SACRILEGE leg-1 SACROSANCT sak- SAD sa- SADDLE sed-1 SAFE sol-
2212:SAPID sep-1 SAPIENT sep-1 SAPONACEOUS _ seib- SAPONATE seib- SAPONIFY seib- SAPONIN seib- SAPONITE seib- SAPOR sep-! SAPROBE gWei- SAPSAGO skep- SARCASM twerk- SARCO-  twerk- SARCOCARP twerk- SARCOID twerk- SARCOLEMMA lep-1 SARCOMA twerk- SARCOPHAGUS twerk- SARCOPTIC MANGE skep-, twerk- SARCOUS twerk- SARDONIC sward- SARDONYX nogh- SARMENTOSE serp-1 SARTORIUS serk- SASTRUGA ghd, ster-2 SATE! sa-
2230:sEccO seikw- SECEDE ked-, s(w)e- SECERN krel-, s(w)e- SECLUDE kleu-%, s(w)e- SECOND2 sekw.-1 SECONDO sekw-1 SECRET krel-, s(w)e- -SECT sek-, sekw-1 SECTILE sek- SECTION sek- SECTOR sek- SECUND sekw-1 SECUNDINES sekw-1 SECURE cilirra, s(w)e- SEDATE! sed-1 SEDENTARY sed-1 SEDERUNT sed-1 SEDGE sek- SEDILIA sed-1 SEDIMENT sed-1 SEDITION ei-1, s(w)e- SEDUCE deuk-, s(w)e- SEE] sekw.2
2235:SEEM sem-! SEEMLY sem-! SEEP seib-
2254:SHRED skreu- SHREW skreu- SHREWD skreu- SHRIKE ker-2 SHRIMP skerbh- SHRINK sker-3 SHRIVE skribh- SHROUD skreu- SHRUB! sker-1 SHTETL sta- SHTICK (s)teu- SHUDDER skut- SHUFFLE skeubh- SHUT skeud- SHUTTLE skeud- SIALADENITIS eng’- SIB s(w)e- SIBILATE swei-1 sic! so- SICCATIVE seikw- SICKLE _sek-
2255:SIDE sé-2 SIDEREAL sweid-1 SIEGE sed-1 SIEGFRIED pri-, segh- SIEROZEM dhghem- SIEVE seib-
2256:SIFT seib-
2273:SNIFF snu- SNIP snu- SNIVEL snu- SNOOP snu- SNORE sner- SNORKEL sner- SNORT sner- SNOT snu- SNOUT snu- SNOW sneig’h- SNUB snu- SNUFF! snu- SNUFFLE snu- SNUG! kes-1 sO swo- SOAK seua-2 sOAP_ seib- SOAVE swad- SOBER s(w)e- SOCIABLE sekw-1 SOCIAL sekw-1 SOCIETY sekw-1 SOCIO- sekw-1 SOCKET sU- SODALITY s(w)e- SODDEN seut- SOIL! sed-1 som? si- SOIREE sé@-2 SOJOURN deiw- SOKE sag- sol’ sawel-
=== AHD siccus/desiccate/sapo ===
912:grade form *séd-yo- in Germanic *(ge)sétjam, seat (*ge-, *ga-, collective prefix; see kom), in Old Norse szti, seat: SEAT. 7. Form *sed-é- in Latin sedére, (third person plural perfect indicative sédérunt), to sit: SEANCE, SED- ENTARY, SEDERUNT, SEDILIA, SEDIMENT, SESSILE, SES- SION, SEWER?, SIEGE; ASSESS, ASSIDUOUS, DISSIDENT, HOSTAGE, (INSESSORIAL), OBSESS, POSSESS, PRESIDE, RESIDE, (SUBSIDY), SUPERSEDE. 8. Reduplicated form *si-zd- in: a. Latin sidere, to sit down, settle: SUBSIDE; b. Greek hizein, to sit down, settle down: SYNIZESIS. 9. Lengthened-grade form séd- in Latin sédés, seat, residence: SEE?. 10. Lengthened-grade form *séd-d- in Latin séddre, to settle, calm down: SEDATE!. 11. Suffixed o-grade form *sod-yo- in Latin solium, throne, seat: SOIL}. 12. Suffixed form *sed-rd- in Greek hedra, seat, chair, face of a geometric solid: -HEDRON; CATHEDRA, (CHAIR), EPHEDRINE, EXEDRA, SANHEDRIN, TETRAHE- DRON. 13. Prefixed and suffixed form *pi-sed-yo-, to sit upon (*pi-, on; see epi), in Greek piezein, to press tight: PIEZO-; ISOPIESTIC. 14. Basic form *sed- in: a. Greek edaphos, ground, foundation (with Greek suffix -aphos): EDAPHIC; b. Sanskrit sad- in upanigad, Upanishad: UPANISHAD. 15. Suffixed form *sed-G-, seat, in Welsh sedd, seat: EISTEDDFOD. See also compound root nizdo-. [Pok. sed- 884.] sed-?. To go. Suffixed o-grade form *sod-o- in Greek hodos, way, journey: -ODE; ANODE, CATHODE, EPISODE, EXODUS, HYATHODE, METHOD, ODOGRAPH, ODOMETER, PERIOD, STOMODEUM, SYNOD. [Pok. sed- 887.] segh-. To hold. 1. Suffixed form *segh-es- in Germanic *sigiz, victory (< “a holding or conquest in battle”), in Old High German sigu, sigo, victory: SIEGFRIED. 2. Greek ekhein, to hold, possess, be in a certain condi- tion (> hexis, habit): HECTIC; CACHEXIA, ECHARD, EN- TELECHY, EUNUCH, OPHIUCHUS. 3. O-grade form *sogh- in Greek epokhé, “a holding back,” pause, cessation, position in time (epi-, on, at; see epi): EPOCH. 4. Zero-grade form “sgh- in: a. Greek skhéma, “a hold- ing,” form, figure: SCHEME; b. Greek skhoié, “a holding back,” stop, rest, leisure, employment of leisure in dispu- tation, school: (SCHOLAR), SCHOLASTIC, SCHOLIUM, SCHOOL/. 5. Reduplicated form *si-sgh- in Greek iskhein, to keep back: ISCHEMIA. [Pok. segh- 888.] seib-. To pour out, sieve, drip, trickle. 1. Basic form in Germanic “sipon in Old English sipian, sypian, to drip, seep: SEEP. 2. Suffixed o-grade form *soib-on- in Ger- manic *saipén-, “dripping thing,” resin, in: a. Old Eng- lish sdpe, soap (originally a reddish hair dye used by Germanic warriors to give a frightening appearance): SOAP; b. Latin sdp6, soap: SAPONATE, SAPONIFY, SAPO- NIN, SAPONITE; SAPONACEOUS. 3. Variant Germanic form *sib- in: a. Old English sife, a filter, sieve: SIEVE. b. Old English siftan, to sieve, drain: sirt. [Pok. seip- 894.] seikw-. To flow. Extended expressive zero-grade form *sikko- in Latin siccus, dry (probably < “flowed out”): SACK3, SECCO, SICCATIVE; DESICCATE, EXSICCATE. [Pok. seiku- 893.] sek-. To cut. 1. Germanic *segithd, sickle, in Old English sithe, sigthe, sickle: SCYTHE. 2. Suffixed o-grade form *sok-d- in Germanic *sag6, a cutting tool, saw, in Old English sagu, sage, saw: SAW. 3. Suffixed o-grade form *sok-yo- in Germanic *sagjaz, “sword,” plant with a cutting edge, in Old English secg, sedge: SEDGE. 4. Suf- fixed o-grade form *sok-so- in Germanic *sahsam, knife, sword, traditionally (but quite doubtfully) regarded as the source of West Germanic tribal name *Saxon-, Saxon (as if “warrior with knives”), in Late Latin Sax6 (plural Saxonés), a Saxon: Saxon. 5. Extended root *skend-, to peel off, flay, in Germanic *skinth- in Old Norse skinn, skin: SKIN. 6. Basic form “sek- in Latin secdre, to cut: SECANT, -SECT, SECTILE, SECTION, SECTOR, SEGMENT; DISSECT, EXSECT, INSECT, INTERSECT, NOTCH, RESECT, (TRANSECT). 7. Lengthened-grade form *sék- in Latin
1420:DEODAR deiw-, deru DEONTOLOGY deu-1 DEPEND (s)pen- DEPICT peig-1 DEPILATE pilo- DEPLOY plek- DEPLUME pleus- DEPONE apo- DEPOPULATE populus DEPORT per-2 DEPOSIT apo- DEPRECATE prek- DEPRECIATE per-6 DEPREDATE ghend- DEPRESS per-5 DEPRIVE pert DEPTH dheub- DEPURATE peue- DEPUTE peu- DERACINATE wrad- DERANGE sker-3 DERELICT leikw- DERIVE rei-3 -DERM der-2 DERMA! der-2 DERMA? tera-1 -DERMA der-2 DERMATO- der-2 DEROGATE reg-! DERRIS der-2 DESCANT kan- DESCEND skand- DESCRIBE skribh- DESERTS = ser-3 DESERVE servus DESICCATE selkw- DESIGNATE sekw-1 DESIRE sweid-1 DESIST sta- DESMID dé- DESOLATE s(w)e- DESPAIR spé-1 DESPICABLE spek- DESPISE spek- DESPOIL spel-! DESPOND spend- DESPOT deme-! DESTINE sta- DESTITUTE sta- DESTRIER deks- DESTROY ster-2 DESUETUDE s(w)e- DESULTORY sel-4 DETAIN  ten- DETECT (s)teg- DETENT ten- DETER tres- DETERIORATE de- DETERMINE ter- DETEST trei- DETONATE (s)tene- DETOUR tera-1 DETRACT tragh- DETRIMENT tera-1 DETUMESCENCE teue- DEUCE! dwo- DEUTERAGONIST deu-? DEUTERIUM deu-!
912:grade form *séd-yo- in Germanic *(ge)sétjam, seat (*ge-, *ga-, collective prefix; see kom), in Old Norse szti, seat: SEAT. 7. Form *sed-é- in Latin sedére, (third person plural perfect indicative sédérunt), to sit: SEANCE, SED- ENTARY, SEDERUNT, SEDILIA, SEDIMENT, SESSILE, SES- SION, SEWER?, SIEGE; ASSESS, ASSIDUOUS, DISSIDENT, HOSTAGE, (INSESSORIAL), OBSESS, POSSESS, PRESIDE, RESIDE, (SUBSIDY), SUPERSEDE. 8. Reduplicated form *si-zd- in: a. Latin sidere, to sit down, settle: SUBSIDE; b. Greek hizein, to sit down, settle down: SYNIZESIS. 9. Lengthened-grade form séd- in Latin sédés, seat, residence: SEE?. 10. Lengthened-grade form *séd-d- in Latin séddre, to settle, calm down: SEDATE!. 11. Suffixed o-grade form *sod-yo- in Latin solium, throne, seat: SOIL}. 12. Suffixed form *sed-rd- in Greek hedra, seat, chair, face of a geometric solid: -HEDRON; CATHEDRA, (CHAIR), EPHEDRINE, EXEDRA, SANHEDRIN, TETRAHE- DRON. 13. Prefixed and suffixed form *pi-sed-yo-, to sit upon (*pi-, on; see epi), in Greek piezein, to press tight: PIEZO-; ISOPIESTIC. 14. Basic form *sed- in: a. Greek edaphos, ground, foundation (with Greek suffix -aphos): EDAPHIC; b. Sanskrit sad- in upanigad, Upanishad: UPANISHAD. 15. Suffixed form *sed-G-, seat, in Welsh sedd, seat: EISTEDDFOD. See also compound root nizdo-. [Pok. sed- 884.] sed-?. To go. Suffixed o-grade form *sod-o- in Greek hodos, way, journey: -ODE; ANODE, CATHODE, EPISODE, EXODUS, HYATHODE, METHOD, ODOGRAPH, ODOMETER, PERIOD, STOMODEUM, SYNOD. [Pok. sed- 887.] segh-. To hold. 1. Suffixed form *segh-es- in Germanic *sigiz, victory (< “a holding or conquest in battle”), in Old High German sigu, sigo, victory: SIEGFRIED. 2. Greek ekhein, to hold, possess, be in a certain condi- tion (> hexis, habit): HECTIC; CACHEXIA, ECHARD, EN- TELECHY, EUNUCH, OPHIUCHUS. 3. O-grade form *sogh- in Greek epokhé, “a holding back,” pause, cessation, position in time (epi-, on, at; see epi): EPOCH. 4. Zero-grade form “sgh- in: a. Greek skhéma, “a hold- ing,” form, figure: SCHEME; b. Greek skhoié, “a holding back,” stop, rest, leisure, employment of leisure in dispu- tation, school: (SCHOLAR), SCHOLASTIC, SCHOLIUM, SCHOOL/. 5. Reduplicated form *si-sgh- in Greek iskhein, to keep back: ISCHEMIA. [Pok. segh- 888.] seib-. To pour out, sieve, drip, trickle. 1. Basic form in Germanic “sipon in Old English sipian, sypian, to drip, seep: SEEP. 2. Suffixed o-grade form *soib-on- in Ger- manic *saipén-, “dripping thing,” resin, in: a. Old Eng- lish sdpe, soap (originally a reddish hair dye used by Germanic warriors to give a frightening appearance): SOAP; b. Latin sdp6, soap: SAPONATE, SAPONIFY, SAPO- NIN, SAPONITE; SAPONACEOUS. 3. Variant Germanic form *sib- in: a. Old English sife, a filter, sieve: SIEVE. b. Old English siftan, to sieve, drain: sirt. [Pok. seip- 894.] seikw-. To flow. Extended expressive zero-grade form *sikko- in Latin siccus, dry (probably < “flowed out”): SACK3, SECCO, SICCATIVE; DESICCATE, EXSICCATE. [Pok. seiku- 893.] sek-. To cut. 1. Germanic *segithd, sickle, in Old English sithe, sigthe, sickle: SCYTHE. 2. Suffixed o-grade form *sok-d- in Germanic *sag6, a cutting tool, saw, in Old English sagu, sage, saw: SAW. 3. Suffixed o-grade form *sok-yo- in Germanic *sagjaz, “sword,” plant with a cutting edge, in Old English secg, sedge: SEDGE. 4. Suf- fixed o-grade form *sok-so- in Germanic *sahsam, knife, sword, traditionally (but quite doubtfully) regarded as the source of West Germanic tribal name *Saxon-, Saxon (as if “warrior with knives”), in Late Latin Sax6 (plural Saxonés), a Saxon: Saxon. 5. Extended root *skend-, to peel off, flay, in Germanic *skinth- in Old Norse skinn, skin: SKIN. 6. Basic form “sek- in Latin secdre, to cut: SECANT, -SECT, SECTILE, SECTION, SECTOR, SEGMENT; DISSECT, EXSECT, INSECT, INTERSECT, NOTCH, RESECT, (TRANSECT). 7. Lengthened-grade form *sék- in Latin
2273:SNIFF snu- SNIP snu- SNIVEL snu- SNOOP snu- SNORE sner- SNORKEL sner- SNORT sner- SNOT snu- SNOUT snu- SNOW sneig’h- SNUB snu- SNUFF! snu- SNUFFLE snu- SNUG! kes-1 sO swo- SOAK seua-2 sOAP_ seib- SOAVE swad- SOBER s(w)e- SOCIABLE sekw-1 SOCIAL sekw-1 SOCIETY sekw-1 SOCIO- sekw-1 SOCKET sU- SODALITY s(w)e- SODDEN seut- SOIL! sed-1 som? si- SOIREE sé@-2 SOJOURN deiw- SOKE sag- sol’ sawel-
```


## [2026-09-14T01:31:19.382Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== BRT haek ===\"; grep -n 'hae k\\|haēk\\|haek' BRT.txt | head -30; echo \"=== BRT hixra ===\"; grep -n 'hixra' BRT.txt | head -10; echo \"=== BRT fra-saeka ===\"; grep -n 'saēkam\\|saekam\\|fraṣaēk\\|fra-saēk' BRT.txt | head -10",
 "description": "Grep Bartholomae"
}
```


### [2026-09-14T01:31:19.478Z] TOOL RESULT

```
=== BRT haek ===
28650:■haek-
28658:•  j.  'haek- V.  'giessen'.  Praes.  3  hi'a-, 9  hinla-. —  PPfP.  °Aixta-;  Inf.  Aixtayai-ca, •Aincäi;  Absol.  'lalhm.  [S.  noch  "^haf- c<U.aspa-:[
28665:•  j,  'haek-  V.,  nur  mit  us  'exarescere'. Praes.  30  (Kaus.)  ha^aya-  'arefacere'.
=== BRT hixra ===
3882:•  j.  aiwi.varSta-  Adj.  (fem,  "/(-)  'be- regnet, worauf  es  geregnet  hat':  vlsp3m\ a  ahmät  nasunam  -a  'ianqm  daxmanqmca ' 'tanqm  hixranqmla  'tanqm  vayanqmüi frariuhantanqm  "bis  dass  es  auf  die  Leich- name geregnet  und  .  .  und  auf  die  Lei- chenausscheidungen geregnet  hat  und  bis die  Vögel  (Alles)  aufgefressen  haben"  V.  ]
30048:•  j.  hixra-  n.  'flüssiges  Exkrement,  flüssige Ausscheidung  des  Körpers':  vispim  ä ahmat  nasunqmca  .  .  äaxmanqmca  .  , •ranamio    aiwi.varstanqm  (sd.)    V.  5.  14;
=== BRT fra-saeka ===
```


## [2026-09-14T01:31:29.060Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '28640,28675p' BRT.txt; echo \"=== fra saek ===\"; grep -n 'fra\\.saēk\\|fra.saek\\|saēkam\\|saekam\\|fraaeka' BRT.txt | head; echo \"=== search saeka ===\"; grep -n -i 'saeka' BRT.txt | head",
 "description": "Bartholomae haek context"
}
```


### [2026-09-14T01:31:29.154Z] TOOL RESULT

```
zu  Ic.  hi,  /f  bezieht  sich  auf  das  Subjekt des  gleichen  Satzes  (Reflcxivum);  nur Sing.;  ha  (n'äml.  andvt)  ^/(fem.)  maiäim nyStata  Vt.5.  ia7;  —  yat  hl  (mask.) *manS  *ahe patti  barät  V.^S-j^fi;  — yesi sl  »aoHrä  baraiti  (Sp.  935  m.}  avi  ii maiharum  YtiO.  136;  —  ya%a  yal  hl (zu  ß)  '^'  pqstü/ra'i:at3h>m  (sd.)  kain?r»him k}r»nuy3t  V.iS.  10;  —  paourva  hl  nsmd baraiti  (Sp.  936  m.)  Yt.j^.36;  —  nava- napiyal(,sä.yii  hl  (zu  a)  urvätum  para.- mirjncaite  V.  13.  y,  —  pasca  *hähra *a/rasruiti  !i  (zu  ß )  paiti  tanüm  *piryeite  j N. 7.  A)  der  Gen.-DaL  vertritt  den! Akk.'^',  nur  im  jAw.;  Sing,  und  Piur.;| zurückweisend:  3al  vohu  manS  nidat6ls\ yal  hl  stärqm . .  aiwi.raocayimeV .ig.^y,  I
—  nasupähm  . .  ava  hl  janay»n  V.  tf.  74;!
—  aha  imq  vacS  dnnjaysÜ  ,  .  paiti  sl\ (Plur.)  äZayiii ..Y.g.12;  —  aya  datnaya  | ■  .  /ra  hl  (fem.)  amilä  spmta  .  .  vfnnta  \ Yt.  /O.  92 ;  —  yezi  ttairyö  anhat  pasüa  ki\ pourum  (Sp.  873  o.)  paiti.hincSis  paiHsa\ apanm  yezi  strl  aahat  paitisa  hl  (fem.)  1 pourum  ..  V.  <y.  58;  —  druxs  upaJvära m»r)ncar)uha  . .  zarahustra  (statt  Akk.),- druxi  hl  pairi.dvarat  V.ig.i;  —  y3\ haintrum  upaiti  pu%rqm{sA.)ca  hl  (fem.;' zu  a)  da^äili  V.  75. 9 ;  —  azdibis. .  hvar^.- dansya  hl  zime  paiti  nidaihlia  V.  ö'.  51;
—  zugleich  vorausweisend:  m3  al barB\ alDö  yat  irist»m;  äat  yezi  !l  barät  alvB yai  iristim  V._j.  14;  —  apa.stavarguha^ vanuhlm  dainqm  .  .  nöii  hl  (fem.)    apa.-\
staväne  vanuhim  dainqm  V.  ig.  6  f.  Un- deutliche oder  wertlose  Stellen  mit  hl, hei,  sl:  nsil  hl..  P.5Ö;  N.jff;  —  mä  hl . . IV.  ig.  \<j;  —  hva  hl..W.  75.4;  —  aliat  hl |Nik.2;  —  yat  hl ..  W.16.  14',  7.52  piiZ., j  18. 44  PÜZ. ;  —yezi  sl  N.  55 ;  —frä  ^  f . .  Yt I  JO. 93;  —  yavata  *hl..ti.ii;  — yqm  hl.. ''Yti4- 13  (s.  Sp.  751  u.No.  i); —  bansma hl . .  V.79. 19;  —  '^afraäifi  hdi  urune P.45;  —  vaye  vä  hl  (zu  a)  .  .  FrW.//;
—  femer  N.j',  Vyt.p,  23,  28,31,  4y,  Vd. 2  ff.  (oft).  [N.  43  aE.:  lies  yär).drä- jehim.]  hl  als  Part  sbes.  II)  Gen.- Abl.  p.  /a*,  j.  hB;  a)  im  Ap.;  nur (zuiück weisend)  in:  hatä  avadasa^,  sd. (Sp,  1 70  u.).  b)  im  jAw.;  nur  (zurück- weisend) in:  ja/.,  malyäka  ..  usi  pairi.- därayeiitli  dalma  hs  (näml.  gSul;_  fem.) pairi.urvtTisayei'iti  Yt.  14-  5Ö.  III)  nur im  Ap.  Gen.-Dat  Plur.  säm'^^\  zurück- weisend: avahs  hamaranam  akunatis hadä  hamih^iyaibii  .  .  avahäsäm  hama- ranam karfam  Bh.j.  i;  3,  6,  7,  9,  10, 2.6—10',  14,  16;  —  imä  dahyäva*  .. tyJ'säm  (fem.)  hacäm^  ahahyer  Bh./.?, D,  5.  3,  4;  Bh. /,  8  (wo  ydhäsäm);  — h(tram  . .  Uta  sä  m  '*'  /  martiyam  ma'histam akunaus    avahäiäm^''''    ahahc^    Bh._J.  9;
—  adam  karam  frSisayam  . .  avähasSm '°' ähaham  Bh-_J.  14;  2.  6;  —  ''uvajtyS  avam martiyam  agarbaya"  hya^i/lm  mahista* 3ha*  uiäsim  av3jan<f  Bh.  2,  4; —  käram ..fräiiayam  taxmasp3dc^  . .  avamlam^"'' mahiiiam  akunavam  avahäsätn  ahahain Bh.  2. 14;^.  6,  5.  i;  —  ima  dahyavc^  .. adam/äm  (fem,)  x/aya'hiya*  3ham  Bh.  i.  6; D.6'.  3.  A)  der  Gen.-Dat  vertritt  den Akk.Ml;  das  Nomen  ist  zuvor  nicht  genannt, aber  es  ist  aus  dem  Zusammenhang  er- kenntlich; adam  ig  hamarana  akunavam vaina  a''ura''matd3he^  adamiäm  (zu  ß) ajanam  uta  9  xsaya%iya  agarbayam  Bh. 4.2.
mü  u,  np.  (a)/,  gr.  «.  Vgl.  daru  Wn.  KZ. 34.  600,  Cld.  Pronomina  60,  Dbr.  VglS.  /.  470, Bgm.  KurieVglGr.  401, 408-  In  idfi-  *ioi  waren die  Gen.-Dat.  >ds  dem  Fron.  3.  Pers.  •«-  und aus  dem  Fron.  refl.  'ijfB-  lu sammeng« flössen. Wo  Aw.  hi,  höi  reflexiv  ist,  gehört  e«  streng- genommen lu  'kva-.  —  Pü. :  öi,  an,  i,  ai;  s, noch  No.  4  f.  —  ')  Im  Ap,  ist  die  /-Fonn  - normal  hinter  i,  h,  r  -,  im  gAw.  die  J-Form verollgemeinerl;  das  jAw.  braucht  die /-Form hinler  i  -  ausser  N.  104  -,  sonst  -  ausser Y.  i).  j8;  s.  No.   10  -  die  A-Form.  —  »)  Die
dby  Google
1737
■haek-
haetumant-
i7»8
Stellen rind:  V,p.33,  t6.S.  i8.  io(s.No.  13), Y.  ig.  6,  N,  4S{f:  s-  No.  n\  N.7;  s.  noch No.  H.  —  J)  Nur  P.  4S  """1  N.  /04.  —  *)  Pii.  r e  an  i  j^is.  —  5)  Hds.  ahiaki;  Pü.:  ffön.  — *)  Hdi.  äki,  ähi;  i.  ä  No.  18.  —  7)  Im  Aind. «liide  allerdingi  das  hinter  dem  Relalivum ttehende  Wort  belont  sein  1  d»  ist  aber  - ncDD  anders  die  Überlierening  Glauben  ver- dient -  jnng,  wie  lal.  quicumque,  ubicamque uiw.  zeigen.  —  8)  So  bei  der  Annahme,  dass dal  nachgesetite  JrM  enklitisch  war;  s.  Sp. 687  0.  —  9)  Hds.  'halnaimäl.  Prolilise  ist doch  schwerlich  aninnehmen.  —  <o)  le  aus dem  vorhetgehenden  Sati  wiederholt ;  s.  No.  1.
—  m  Hds.  j^arül  kl.  —  •')  Vorher  geht  ro {itMtyai)..  elt^iu;  s.  Sp.  1724  m.  —  ■D^'oS.j yai  vrerden  wohl  unter  einem  Hochton  lu- sammengeharen.  —  '4)  Vgl.  lu  'Sica-  No.  10  ff.
—  15)  Neubildung;  %  3Si-  —  '"'  Geht  auf Aära-i  Konstruktion  nach  dem  Sinn.
}-•  g'i  p-  ^f'  in  Komp.  und  Ableit.:  E.  unter
j.    hol**  Yt.  ig.  67:  lies  haelumS.
•  j.  'haek- V.  'giessen'.  Praes.  3  hi'a-, 9  hinla-. —  PPfP.  °Aixta-;  Inf.  Aixtayai-ca, •Aincäi;  Absol.  'lalhm.  [S.  noch  "^haf- c<U.aspa-:[
i)  '(Wasser)  ausgiessen,  laufen  lassen über—',  mit  avi  und  Akk.:  nä  tat  ap>m hincäiti  avi  yavs.caränTm  (sA)  V.  5.  5;  — kincat  'S.  24.  3)  'etwas  begiessen,   be-
wässern': s.  In£
mit  paiti  'etwas  Jemanden  an-,  be- giessen'  nait  Wasser  oder  Rindsurin,  bei der  rituellen  Reinigung:  bansnüm  hi vaylarum  pourum  paitiMn^Bis''>  V.  5.  40; . 7of.',  5. 16-24'*;  —  y^'  nairys  aahat pas^a  hl  pourum  (Sp.  872  o.)  paitLhinMs V.  (?.  58;    58,   ().  ai'.  a)    absolut    'die
rituelle  Reinigung  mittelst  Begiessen  vor-  j nehmen':  yesica    ho   nä  paiti.hincöil'^  ys\ ataite  dainayh  . .  V,  p.  47;    — i Aiticaiti'^ . .  \.g.  5».        S,  noch  |
ra  '(Wasser)  weggiessen,  aus-' und  weggiessen':  aiAhi  äps ■■y»n  yat  vä  naiitum  .  ,  pasca iixtUsd.)  ..  V.O. 37. 1)  'etwas  vergiessen,  verspritzen': iuttim  vä  tJ^ayeinti  fralaik?in ''ralUanli^^  Yt  14.  54;  —  *a'^a *frahinHn  *'antarv'>  atanmla a  "ebenso  wenn  sie  sie  (die verspritzen  zwischen  .  ."  N. '  'etwas  durch  Guss  (aus  Metall, stellen':  vasnm  . .  zarsis  ayanhs w  Yl;o.  96».
ai.  sihcää,  asical  %  siitik,  'sikam ;  np.  pasanjU dan  (tiozii  Hbu.  PSL  43].  —  Pü.:  äsutjUan, (lu  N.) :  ia  . .  afi  B  tamTk  tecit.  —  1)  S  49.  — >)  Hds.  frahincinlari,  aber  Pü.;  aadark  .  . rtff/;  t.  iSt.  BTHL.  IF.  5.  369,  —  J>  Vgl.  vä/ram isiüiala  AV.  //.   10.   12.
•  j,  'haek-  V.,  nur  mit  us  'exarescere'. Praes.  30  (Kaus.)  ha^aya-  'arefacere'.
yat  .  .  US    vatB  tarn    haicaySt   ",  ,  der Wind  die  Erde  austrocknet"  V.  5, 12. lett.  slku  'ich  versiege' (?)i),   —  Vgl.  haelah; hiiao-.  —  Pü.:  ia  .  .  us  vöi  tanük  höUail.  — ')  Unsicher,  da  lett.  X  mehrdeutig  ist.
•  j.  hä  druxs  asaojista  anhat  "haefiä Si,aiei  FrW.  S.  2.
Ob  ^<iÄN5f.  EU  'ha-)^t  Also  'und  lie  geht zu  Grund"?
•  g.  'haecat.aspa-  m.  EN.  des  vierten Vorfahrens  Zara^uäras,  Nachkommens des  Spitama  im  fünften  Glied.
Ableit.  —  Eig.  etwa  'Rosse  (mit  Wasser)  be- spiengend,  badend' ;  'haiiani-  Adj.,  PPzA.  lom V.    ikalk:
•  g.  'haecataspa-  patr.  Adj.  von  Haicat.- aspa  abstammend,  dessen  Nachkomme': •pä  (VP.)  vaxsyl  vJ  spUamänAs  "ihr Haecai.asp\Ata,  ich  will  euch  Kunde  geben, ihr  Spitam'iden"  Y.46.15.
Ableit.  (mit  blosser  Verschiebung  des  Woit- akients)  aus  "hailal.aspa-  m.  EN.  —  Vgl. haHaUaspäiia-.  —  Pä. :  hcüiaLaifqn  (in  Aw.- Buchst,),  Sü.  1  haicalaspiyiA.
•  g,  baeöataspäna-  patr.  Adj.  (fem.  *«J-) 'von  Haicataspa  abstammend,  dessen Nachkomme':  iimcä  tu  pouruasta  'änJ (NSf.  als  VSf.)  spitami  yaivl  dugxiraiH (sd)  . .  "Und  den  hier,  o  P.,  von  H., von  Sp.  entsprossene  .  ."  Y.  5J.  3.
Ableit.  aus  *iae;al.aspa-  m.  EN.  —  VgL  katial.' asfa-.  —  Pü.;  ha^Ml.as/mit  (in  Aw. -Buchst.).'
•  j.  hae£ah-  n. 'Trockenheit, Dürre':  udrahe avaynanS  'cö  kfrmaoiii  yat  avastrvm  V. 13.  $1;  —  'lajvhs  avästrahe  V,  7.  »6;  — ainistsis  . .  'canhasca  avastrahe  i^yajaa- hasca  Yt,  13. 130.
=== fra saek ===
=== search saeka ===
```


## [2026-09-14T01:31:30.302Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== CHEUNG saic ===\"; grep -n -i 'saič\\|\\*saik\\|saic' CHEUNG.txt | head -30",
 "description": "Grep Cheung for saič"
}
```


### [2026-09-14T01:31:30.390Z] TOOL RESULT

```
=== CHEUNG saic ===
```


## [2026-09-14T01:31:47.922Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== HUB pasanj ===\"; grep -n -i 'pasanj\\|pašanǰ\\|pašanj\\|paSang' HUB.txt | head -20; echo \"=== HRN ===\"; grep -n -i 'pasanj\\|pašanǰ\\|pašanj' HRN.txt | head -20; echo \"=== CHEUNG ===\"; grep -n -i 'pasanj\\|pašanǰ\\|pašanj\\|hinca\\|hiča' CHEUNG.txt | head -20",
 "description": "Grep HUB HRN CHEUNG for pašanjīdan"
}
```


### [2026-09-14T01:31:48.016Z] TOOL RESULT

```
=== HUB pasanj ===
1434:— phi. "^patsincat = np. pasanjad. Sehr friih er-
4464:jfidan = pasanjldan 'besprengt werden, aus "^pal-sinc-Uan
4787:pasanjidan 'besprengt werden' aus ^paUsind-ltan zu skr.
6762:= ap. '^patidayana-; np. pasanjfdan *besprengt werden,
8021:pancum Min. 61. 155 ist panjum zu lesen) ; pasanjidan
10642:pasanjldan 42, 191.
=== HRN ===
=== CHEUNG ===
9052:Pres. n-: IND. 3sg. YAv. hincaiti (V 5.5), med. YAv. “fra.hincaite (N 68 = Kotwal — Kreyenbroek: N 
9053:50.7), 3pl. YAv. frasicinti (Yt 14.54), INJ. 3sg. YAv. hincat (F 673), SUBJ. 3sg. YAv. hincäiti (N 83), 
9055:para.hincaiion (V 6.32); Perf.: IND. 35р. ? YAv. "frahisaeca (Yt 10.138); Partic.: pres. them. ? OAv.
```


## [2026-09-14T01:31:49.408Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== SOD pSync ===\"; grep -n -i 'pšync\\|psync\\|pšynz\\|sprinkle' SOD_pages.txt | head -20",
 "description": "Grep Sogdian dictionary"
}
```


### [2026-09-14T01:31:49.509Z] TOOL RESULT

```
=== SOD pSync ===
22342:      C2, 1V5                                                                   pasenc ©impf. =#psync-
22343:6488 pVzn       B «» p>zn                                                       (to)sprinkle
25294:     pasayd ©pt. St. =*psync-
25295:     (fo)sprinkle, (rcOspill                                  7508 psn-     S, M, C                                 4: <(b
25406:7537 psync- C                   (p j-^'.^j^j *6^l
25409:     Oo)sprinkle, (/o)pour
25415:7538 psyncn        C                                      ajuil         STi 7.5; STii 6.8, 10, 24; Frag. Len. 85.11; MSP J**ji
25417:      sprinkler                                                           572
34875:                                                               10761 xwrny psyncny C              j'y-u>- < jljoj*-
35870:        ywt'c C                              ^jj^ifjj                 yuxna-pasik =^xwrny psyncny
39485:    sometimes       2442, 2445                spade   9696                            Go)sprinkle    6500, 7496, 7537
39487:                                              span   10341                            sprinkler    7538
```


## [2026-09-14T01:32:05.457Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '25390,25420p' SOD_pages.txt; echo \"=== page tag ===\"; awk 'NR<=25420 && /\\[pdf page/ {l=$0; n=NR} END{}' SOD_pages.txt; grep -n '\\[pdf page' SOD_pages.txt | awk -F: '$1<25420' | tail -3",
 "description": "Sogdian psync entry and page"
}
```


### [2026-09-14T01:32:06.549Z] TOOL RESULT

```
                                                                        patafc ?, patapc ?                                 k*j!
     (to)sit down
                                                                        (a kind of)di\xg
     STi 52.10; Sund. AoFi 1974, 8V 12 p242; Hen.
                                                                        TSP 19.18n p232
       BSOAS 11, 1946, 715 apud. GMS 877 n 2

7536 psyn-     M         o>lsff b* ijzZhjl <o>jjTji^o <j^LuUb*     7547 ptVn'k B
                                                                        pattawne ©pres. part. =^pt>w-
      pasen ©<Skt. ksan ©impf. p*sy(y)n =*psn-
      (fo)trap, (ro)be trapped                                           SCE  68; GMS 893
                                                                         patient
      GMS 6l6n 1; Benv. Eti 329 n 60; AHM 192,
                                                                   7548 ptwwyn>k       B                            JJr* 'Ji^ji
        san-,S W, C2p51 n5
                                                                         pattawene ©pres. part. ^pt1wn,k
7537 psync- C                   (p j-^'.^j^j *6^l
     pas^c ©Shaek; Av. hincati ^p's'ync-                                 Vim. 172, 194; BSTBL
                                                                         patient
     Oo)sprinkle, (/o)pour
                                                                   7549 pt*w- S, M, C         ^jjT^l-o^^j^^os^jl^"
     GMS 600; BBB 531; BSTi 318; C2, 11V19; Bailey.
                                                                        pattaw ©Parth. ptt}w-,<*pati-taw
       Prolexis. 417; AVS 123
                                                                        (ro)endure
7538 psyncn        C                                      ajuil         STi 7.5; STii 6.8, 10, 24; Frag. Len. 85.11; MSP J**ji
      pascncan      ©voc. -}                                              b200, 180, 143, 197; Sund. AoFi 251.5; GMS
      sprinkler                                                           572
      STii 6.10
                                                                   7550 pt'w'nt    B
7539 psynty C                                       c^-i <» j*-          pattawand
=== page tag ===
```


## [2026-09-14T01:32:06.989Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== TAD صابون ===\"; grep -n 'صابون' TAD_pages.txt | head -10; echo \"=== TAD sapon ===\"; grep -n 'ساپون\\|صابون' TAD.txt | head -10",
 "description": "Grep TAD for sabun"
}
```


### [2026-09-14T01:32:07.058Z] TOOL RESULT

```
=== TAD صابون ===
1660:‫لاتيي دز‪:‬ه‪-‬ومهه ذ كره بلينيوس وكان خليطا رممناد وشحم‬                     ‫صابون ©‬
=== TAD sapon ===
1719:صابون © لاتيي دز:ه-ومهه ذ كره بلينيوس وكان خليطا من رماد وشحم
```


## [2026-09-14T01:32:18.679Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"--- SOD page tag near 25406\"; grep -n '\\[pdf page' SOD_pages.txt | awk -F: '$1<25406' | tail -2; grep -n '\\[pdf page' SOD_pages.txt | awk -F: '$1>25406' | head -2; echo \"--- TAD page tag near 1660\"; grep -n '\\[pdf page' TAD_pages.txt | awk -F: '$1<1665' | tail -2; sed -n '1650,1670p' TAD_pages.txt",
 "description": "Find page tags for SOD and TAD hits"
}
```


### [2026-09-14T01:32:19.793Z] TOOL RESULT

```
--- SOD page tag near 25406
--- TAD page tag near 1660

‫‪-‬تينية واصطلح عابها في اصكثر اللغات الاجثبية‬
                                           ‫شكيوولاري (© لا‬
                                                            ‫ساركلار ومعناها دار‬


                                     ‫‪4‬‬     ‫ص‬     ‫د‬



‫لاتيي دز‪:‬ه‪-‬ومهه ذ كره بلينيوس وكان خليطا رممناد وشحم‬                     ‫صابون ©‬
 ‫ومقانا عوة‪.‬مر كني مونفزلييت وهو نايلجمليغعات بهذا ا'لا‪#‬سنمادمم‬
                                                 ‫و ‪ 80725‬و تزدمة مرادقه الغاسول‬

                             ‫صاج ‪ -‬تركي « ساجوصاج م»عناه لوحمن حديد‬
‫صاروج ‪ --‬فارسي « سارو » وهو الدورة اي حجر الكلس مخلط بالزرنيخ‬
                                             ‫ومنه الصهر يجلحوض الماء لانه يطلل به‬
            ‫معنام الفأس‬      ‫ولا'يتي ‪5‬‬          ‫صاقور وصوقر ‪ -‬بوناني ‪5‬‬

               ‫صالون وصالية ‪9‬؟ ‪ -‬ايطالي ‪3‬اد‪ 5‬معناه الاعة والردهة والهو‬
```


## [2026-09-14T01:32:21.206Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== AFM sabun ===\"; grep -n 'صابون' AFM_pages.txt | head; echo \"=== KLN soap/saponaceous ===\"; grep -n -i 'soap (' KLN_1966.txt | head; grep -n -i 'sapo,\\|saponaceous\\|sapon-' KLN_1966.txt KLN_1971.txt | head -10",
 "description": "Grep AFM and Klein"
}
```


### [2026-09-14T01:32:21.308Z] TOOL RESULT

```
=== AFM sabun ===
2408:ل 1 غنات بالصابون ٠‏ وذه|ب قوم الى ܕ ܒ الوزع ܗ من
2719:03 مطوخ مركي من الزيت او من الشحم وغيرثما والقلى ٠‏ وهو صابون
2729:الصابون صغة ارامية ٠‏ والعليم عند "اللهل ابت
5047:صابون ܀ ܙ
5589:صابون 5
5786:٠١5 صابون‎
=== KLN soap/saponaceous ===
KLN_1971.txt:212514:Indicus, ‘Indian’, fr. India. See saponaceous and 
KLN_1971.txt:212521:saponaceous, adj., soapy. — Formed with suff. 
KLN_1971.txt:212525:Derivative: saponaceous-ness, n. 
KLN_1971.txt:212530:(see saponaceous and -aria); so called because 
KLN_1971.txt:225368:‘ointment’, sep-, sip-, ‘to anoint’. L. sapo, ‘soap’, 
KLN_1971.txt:225369:is a Teut. loan word. Cp. saponaceous, sebace- 
KLN_1966.txt:33715:Sapindaceae,  n.  pi.,  the  soapberry  family  (hot.)  — ModL.,  formed  fr.  Sapindus  with  suff.  -aceae. sapindaceous,  adj.  —  See  prec.  word  and  -aceous. Sapindus,  n.,  a  genus  of  plants,  the  soapberry (bot.)  —  ModL.,  contraction  of  L.  sapo  Indicus, 'Indian  soap’,  fr.  sapo,  gen.  - dnis ,  ‘soap’,  and Indicus,  ‘Indian’,  fr.  India.  See  saponaceous  and India.
KLN_1966.txt:33718:saponaceous,  adj.,  soapy.  —  Formed  with  suff. -aceous  fr.  L.  sapo,  gen.  saponis,  ‘soap’,  which  is a  Teut.  loan  word.  See  soap.
KLN_1966.txt:33719:Derivative:  saponaceous-ness,  n.
KLN_1966.txt:33720:Saponaria,  n.,  a  genus  of  plants  of  the  pink  fam¬ ily  (bot.)  —  ModL.,  fr.  ML.  saponarius,  ‘per¬ taining  to  soap',  fr.  L.  sapo,  gen.  saponis,  ‘soap’ (see  saponaceous  and  -aria);  so  called  because the  juice  forms  a  lather  with  water, saponification,  n.,  chemical  conversion  of  tats into  soap.  —  F.,  fr.  saponifier,  ‘to  saponify’. See  next  word  and  -ation. saponify,  tr.  and  intr.  v.  —  F.  saponifier,  ‘to  sa¬ ponify’,  fr.  L.  sapo,  gen.  saponis,  ‘soap’,  and -ficare,  fr.  facere ,  'to  make,  do'.  See  soap  and suff.  -fy.
```


## [2026-09-14T01:32:27.724Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== KLN soap ===\"; grep -n \"^soap\" KLN_1966.txt | head; grep -n \"soap,  n\\.\\|soap, n\\.\" KLN_1966.txt KLN_1971.txt | head",
 "description": "Klein soap entry"
}
```


### [2026-09-14T01:32:27.796Z] TOOL RESULT

```
=== KLN soap ===
KLN_1971.txt:225362:soap, n. — ME. sope, fr. OE. sdpe, which is rel. to 
KLN_1966.txt:35756:so,  n.,  the  fifth  note  (=  G.)  in  the  scale  of  C major  ( mus .)  —  The  same  as  sol. soak,  tr.  and  intr.  v.  —  ME.  soken,  fr.  OE.  socian, in  gradational  relationship  to  OE.  sucan,  ‘to suck’.  See  suck  and  cp.  soggy,  sowens. Derivatives:  soak,  n.,  soak-age,  n.,  soak-er,  n., soak-ing,  adj.,  soak-ing-ly,  adv.,  soak-y,  adj. soap,  n.  —  ME.  sope,  fr.  OE.  sape,  which  is  rel.  to MLG.  sepe,  Du.  zeep,  OHG .  seiffa,seifa,  MHG., G.  seife,  ‘soap’,  OHG.  seifar,  ‘foam’,  and  prob. also  to  OE.  sap,  ‘resin’;  fr.  I.-E.  base  *se(i)b-, ‘tallow,  resin’,  whence  also  L.  sebum,  ‘tallow, suet,  grease’,  and  prob.  also  Toch.  A  sepal, ‘ointment’,  sep-,  sip-,  ‘to  anoint’.  L.  sapd,  ‘soap’, is  a  Teut.  loan  word.  Cp.  saponaceous,  sebace¬ ous.
```


## [2026-09-14T01:32:29.721Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"--- TAD tags\"; grep -c 'pdf page' TAD_pages.txt; head -5 TAD_pages.txt; echo \"--- AFM ctx\"; sed -n '2715,2735p' AFM_pages.txt; echo \"--- AFM tags\"; grep -n 'pdf page' AFM_pages.txt | awk -F: '$1<2735' | tail -2",
 "description": "Inspect TAD and AFM page structure"
}
```


### [2026-09-14T01:32:30.840Z] TOOL RESULT

```
--- TAD tags
0
                                     ‫الف‬
           ‫ياكابىاللبناك‬  ‫‪َ8‬‬
                       ‫نببى‬


--- AFM ctx
(3الغاف ) غنت على وه مارك
ܒ̈ 2 .(م 25م )جرع
ܐܝ الصاد
* ( @ : الثمر )© 693 3
03 مطوخ مركي من الزيت او من الشحم وغيرثما والقلى ٠‏ وهو صابون
0 ® والتركة والكرد نه . 01.97 ® و0215 , 9220 0297 ܕ @$611
بالرمانة و5903 بالاتكايرنة ܀ @$2](0116 بالايطا لمامة ܖ $2¥011 ® ܕ ܨܦܘܢ
باللغة ® ܡܐ ± .فلا بد انْ لغة من هذه اللغات أعارت اخواتها
هذه الافظة ٠‏ فذهب قوم الى 5 فارسسة ( راجع فرتكل : \ \ ¥ ) *وقيل !5 اصلها
3 00 من 5651112 أو <اتاحاء؟ ܝ || م ٠‏ وقيل ܗܡ منستوف 'الى:مدرئة
سافون 1 العم فنهينا ܨ اول 3 01 ( القاموس الفرذي <
5 7 متتل ان يكون 0 1 +فات الاوك ܩ لتنظليف
كل" ܘܐ سخ من الثياب ܕܫܐ 3 0 من 8 ( صنى 0 اومن
ܝܢ كمد ومعناه ܝ الى فوق يككون قد ܗ به من رغوته ܀ هذا فضلا 38 0 صبعة
الصابون صغة ارامية ٠‏ والعليم عند "اللهل ابت
+ من دراهم العراق. ان اسبهبد بالفارسيّة معناهُ قاد
العسكر وهو ايضأ | سم وعلم ܙ 2:0 ٠فلعل‏ الاصهمذانة نسبة الى اسيهيد
* (الصنّة ) الذة 2
(الصَت ) 33 باللماعة من الناس موآدة من صد اي المائة
* (الصخن ) القصعة الصغيدة تعريب سيني ٠واما‏ فرتكل .38 فال
3 تعر بإب ܝ 5011
--- AFM tags
```


## [2026-09-14T01:32:46.468Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== AFA sabun ===\"; grep -n 'صابون\\|Sâbûn\\|sâbûn\\|sabûn' AFA.txt | head -10; echo \"=== LKT sapo ===\"; grep -n -i 'sabun\\|ṣābūn\\|sapon\\|seife' LKT.txt | head -15",
 "description": "Grep Fraenkel and Lokotsch"
}
```


### [2026-09-14T01:32:46.539Z] TOOL RESULT

```
=== AFA sabun ===
=== LKT sapo ===
1404:549.  Ar.  dürawä: 'Getreidesplitter,  Spreu,  die  beim  Worfeln des  Getreides  abstiebenden  Hülsen'; hieraus  Ober  *dräwa,  *dröwa  die  roma- nischen Formen  sp.  it.di-oga,  irz.drogue; engl,  drugs,  dtsch.  Droge.  [Zahlreiche andere  Ableitungen  sind  vor  allem  be- deutungsgeschichthch  unhaltbar,  so  aus pers.  därü  'Arznei'  Horn  NpEt  S.  116, Nr.  523:  pehl.  därük;  aus  lat.  irochiscus, gr.  TpoxiöKO^  'Pille,  Seifenkugel';  aus ndl.  droog  'trocken';  aus  slav.  doi-gz 'teuer'  Bern  SlEtWb  213;  vgl.  vor  allem BAIST  in  ZffrzSpr  XXXII,  298/39 1.| [Kluge  98.  KLUYVER  in  ZfdWf  XI,  7/10. SEYBOLD  in  ZfdWf  X,  218f.  ZfdU  XV, 335.
3635:1585.  Tk.  öd  agagy: 'Wohlriechendes  Holz'  [von  öd  'Galle' vom  Stamme  ol,  ög  'Zorn,  Eifer'  <^ 'Feuer,  brennen'  in  flg.  Bedeutuug, Vämbery  TktEtWb  S.  51,  S.  56,  und  agag 'Baum'  in  genitivischer  Verbindung]; hieraus  rum.  odogacm  'Seifenkraut,  Aloe- holz'. —  [Es  liegt  wohl  schon  im  tk. Grundwort  Kontamination  mit  ar.  'üd, s.  hier  Nr.  2127,  vor.]
```


## [2026-09-14T01:32:47.341Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; timeout 600 python3 tools/ref_page.py BQT:1330 --image 2>&1 | tail -40",
 "description": "Fetch BQT page 1330"
}
```


### [2026-09-14T01:32:53.934Z] TOOL RESULT

```
(no exact page map; using offset -1205 -> pdf page 125; check the printed number and re-run with --pdf-page if off)
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1330.png
REF: BQT:1330  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 125  OCR-lang: fas

بیان دوم.(۱)
در صاد ی نقطه با بای انحد مشمّمل بر سمزده لت و کنات
صباح کنان ه کنایه از سباحالخیر راست است که کنایه از صبح صادق باشد ؛
گوبان‌است بعنی مردمالیکه بسباح الخیر کفتن | و بجای نون میم هم بنظر آمده است که راست
عادت کرده باشند . خامه باشد .
صباد < بنم اول و ثانی بالف کشیده ۱ صبح روان - کنایه از جوانان‌است
و برای قرشت زده » خرمای هندی راگوبند که که نقیض پبران باشد + ومافرالر! یز کویند.
سوه ۴ تا : :
تمرهندی ,اشد ‎٩‏ - وبفتح اول در عربی سنگکه ص ملمع اس < کنایه از
سخت باشد . صبح کاذب است که صبح اول باشد ۴ .
صباع ۲ تنگار « کنایه از ماء است صبح نحست - بمعنی صبح‌ما.ع تفاب
که قمر باشد . است که کنابه از صبح کاب باشد .
۰ واه ۰ ۰ ۹9
صباع ۲ جواهر « کنابه از آفتاب صبح نشینان «کنایه از سبح خیزان
عالمتات است . است که مردمان عاید سحر خبز باشد.
صبح دل - بنکرن حای بی نقطه : صبو ده * - بروزن تنورهحیزومخنت
۱ ِ و پشت پایی وپلید راگونند ‏
مردم صاف دل وروشن ضمیر ومتّقی و پرهیزکار
باشد . صبی « بفتح اول و ثانی بتحتانی‌رسيده.
۱ گیاهی است کهآ نرا سنا گوبند وبهترین‌آن
صبح راست - کنایه از صبح صادق یاهی کهآ در گوبند وبهترین‌آن مکی
۰ است » و بعضی گوبند عصارهة سنا است » و در
است که صدح دوم (۲) باشد. ۱ ۹
دوم /۱۹ باس ختیارات عصارة آشنان نوشته‌اند - و درعربی طفل
صبح راست خانه - پیمنی سبح راگوبند .
[69 چش ؛ دوم ۰ )۹( خم۱ : دوم .۰
‎٩‏ < 13020 دنك اس رد۳ که فلز لاس789 یی ۰۹۱۹۹
- (عی) بفتح اول وتشدید دوم » رنگه رز » رنگك ساز ۰
۴ - (عر) بضم اول وفتح دوم و سوم مشدد روشن ودرخشان کرده شده وآنچه بورق طلا
روشن کنند «عباث؟ ۰
۴ - زدنفی سربمهرسبح ملمع نقاب خيمةٌ روحاایان کشت معنبر طناب.
, «خاقانی شروالی ۰۴۸۲
- مصحف «صبوزه, مخنت پلید بود . قریع کوید:
مادرش گشته سمر همجو صبوزه بجهان از طراز آندر تا شام وختَنٌ تا در زنگه.»
« لغت فری ۹۱۹
```


## [2026-09-14T01:32:58.577Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; timeout 600 python3 tools/ref_page.py BQT:1328 --image 2>&1 | tail -35",
 "description": "Fetch BQT page 1328"
}
```


### [2026-09-14T01:33:04.295Z] TOOL RESULT

```
(no exact page map; using offset -1205 -> pdf page 123; check the printed number and re-run with --pdf-page if off)
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1328.png
REF: BQT:1328  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 123  OCR-lang: fas

فتار برد
گفتار , ار هم
از کناب برهان قاطع در حروف ماد بی قطه پا حروف
تمجی مبتلی بر ده بیان و محتوی بر هفناد و هفت
لغت و گنایت و يك انجام که آ نیم «شنمل است برهشت لت
که اول آنپا ضاد نقطه دار باشد
بیان اول
در صأاد ی نقومله با الف مشتّمل پر هجده لغت و کنات
* صاب « بسکون بای ابجد هرلباتی صاپون * -» با ناك بوا و کشیدهربنون
را کوبند کهآ ترا شیری باشدیمنی در وقت‌بریدن | زده , معزوف‌است وآن‌چیزی باشد که بدان‌جامه
و شکستن ازآن چیزی برآید سفید مانندشیر ‎٩‏ | و امثال آن شویند وصهل خام است.
- و جفاهانی سیب راکه تفاح باشد صاب‌خوانند صاحب ؟ - با حای بی نقطه بر وزن
- و درعربی حنظل راگونند ۰ کاتب » وزیر را گوبند-وبمعنی خداوند هم آمده
صا پو فه ؟ - با نالك بواو رسیده وفتح | است. و عربی است .
(۱) چش :کردن () ۰
ص (ساد) - حرف هفدهم از الفبای فارسی وحرف چهاردهم از الفبای عربی(ابتت)
و در حاب +مل آیرا نود گیرند.این<رف در زبان فارسصی لیست ودرلغات دخیل آمده . دریعضش
کلمات فارسی ماندد شست و صد واصفم‌ان که با صاد نوشته مرشوند اصل آ نها سین بوده » ودر هر
حال‌ایرانیان صادراسین» تلفظ کنند تلفظ آن در عربی صوتی است نزديك بین وکشش آواز
بیشتراز آن است. وازگذاشتن دو طرف زبان بسقف دهان ودمیدن لفی ادا میشود .
۱ - ر4 : لك ۲ سس ۳۹۱. ۲ - ر4: سابوته .
۴ - (عر) صابون » از بونانی 52808 ۰ لائینی 5200 و0819 بهمین معنی ۶ لغب
س 4۳ ح ۰*4 فرادوی ۰52۷08 انگلیسی 8020 , آلمانی 50[]6 رل : لك اس ۳۰۹
ولخب ص ۹4. ارچ آسم فاعل از صحابةوصحبت "صاحب بک رها یار صحیت > مستهی؛لارب».
```


## [2026-09-14T01:33:23.992Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT; python3 -c \"\nfrom PIL import Image\nim=Image.open('1328.png'); print(im.size)\nw,h=im.size\nim.crop((0,0,w,int(h*0.06))).save('/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/bqt1328-hdr-437.png')\nim.crop((0,int(h*0.94),w,h)).save('/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/bqt1328-ftr-437.png')\n\"",
 "description": "Crop BQT page header/footer"
}
```


### [2026-09-14T01:33:26.532Z] TOOL RESULT

```
(1650, 2546)
```


## [2026-09-14T01:33:28.685Z] TOOL CALL #26: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/bqt1328-hdr-437.png"
}
```


### [2026-09-14T01:33:28.705Z] TOOL RESULT

```

```


## [2026-09-14T01:33:32.505Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT; python3 -c \"\nfrom PIL import Image\nS='/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/'\nfor p in ['1328','1330']:\n    im=Image.open(p+'.png'); w,h=im.size\n    im.crop((0,int(h*0.04),w,int(h*0.14))).save(S+'bqt'+p+'-top-437.png')\n\"",
 "description": "Crop upper band of BQT pages"
}
```


### [2026-09-14T01:33:33.941Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T01:33:36.161Z] TOOL CALL #28: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/bqt1330-top-437.png"
}
```


### [2026-09-14T01:33:36.176Z] TOOL RESULT

```

```


## [2026-09-14T01:33:44.150Z] TOOL CALL #29: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/bqt1328-ftr-437.png"
}
```


### [2026-09-14T01:33:44.171Z] TOOL RESULT

```

```


## [2026-09-14T01:33:54.241Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== MON sabun ===\"; grep -n 'صابون' MON_part1.txt MON_part2.txt | head -10; echo \"=== MON incoming ===\"; grep -n 'صابون' incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt | head -10",
 "description": "Grep Mo'in for sabun"
}
```


### [2026-09-14T01:33:54.333Z] TOOL RESULT

```
=== MON sabun ===
MON_part1.txt:1675:آب از جایی بجایی. شستن جامهٌ صابون‌زده 
MON_part1.txt:80405:بکار می‌رود در صابون‌پزی نیز مورد استفاده 
MON_part1.txt:83156:شامیو: 0 (ا.) نوعی صابون مایع که 
MON_part1.txt:83473:صابون‌های نرم و سوخت می‌رسد. از نظر 
MON_part1.txt:84561:و در صابون‌پزی بکار می‌رود. (شیم.) 
MON_part1.txt:85441:جهت در صابون‌سازی بکار می‌رود؛ سنگ 
MON_part1.txt:86062:کردن: خوردن. شکم خود را صابون زدن: به 
MON_part1.txt:88405:صابون: ۰2050 (- صابون» معر.] (ا.) 
MON_part1.txt:88408:لباس بکار برند. ضح.- (شیم.) صابون‌ها 
MON_part1.txt:88413:برای تهیةٌ صابون اسیدهای چربی‌دار را با 
=== MON incoming ===
incoming/MON/MON_2vol_Adena_v2_djvu.txt:5942:(جانوران) چسبانیده‌اند و بدان کف صابون 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:23832:از حل صابون در آب که بنام کف صابون 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:24070:مچ: ۷۵15 [- کفک ] (1.) کف صابون و شیر 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:24217:صابون و غبره) . کف (آب؛ صابون و غبره). 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:28829:فایده داشتن از آن . کیسهٌ به صابون زدن: 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:31200:مورد استعمال دارد و بعلاوه در صابون‌سازی 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:34887:محرق می‌جوشانند» مسخلوطی از صابون و 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:34909:صٍِ۳ کش ل صابون 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:41428:از پارچهٌ نازک که صابون در آن نهند و بدن 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:41429:را با آن شویند؛ کيسةٌ صابون. قسمی کدو که
```


## [2026-09-14T01:33:57.179Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== ARY latin sec/siccus ===\"; grep -n -i 'siccus\\|SEIKW\\|SEIK' incoming/ARY/ARY_latin_index_pages.txt | head -10; echo \"=== ARY pashang ===\"; grep -n 'پشنگ\\|پشنجیدن' incoming/ARY/ARY_pages.txt | head -10; echo \"=== IEC seik ===\"; grep -n -i 'seiquo\\|seikuo\\|sikkos\\|siccus' IEC.txt | head -10",
 "description": "Grep Aryanpur and Mann"
}
```


### [2026-09-14T01:33:57.274Z] TOOL RESULT

```
=== ARY latin sec/siccus ===
=== ARY pashang ===
=== IEC seik ===
2204:dé-siqusos ‘dried up’. See dë, siqusos Lat. *desiccus (in desiccare); Ir. díosc “dried up, barren’
15131:seiquos, à (seikos, a?) 'sifting-basket, seed- lip’. Cf. seiqu-, soiqu- OHG cf. siha, f. ‘sieve’; LG Sih, f. id.; Li. siekas, saikas, m. “basket; a grain-measure'; cf. seikiu, e. v. ‘measure by capacity’; Latv. sieks, m. (a capacity measure). (Hybridism is possible between a type *seik- and a type *seiqu-)
15364:siqu- (variant of type sik-, q.v.) ‘run dry; drain, seep’. Cf. seiquo, sinquó OE cf. seohhe, f. & sife, n. ‘sieve’; seohhian, v. ‘sift’; Ukr. sect, s. ‘urine’; Latv. sikt, inf. ‘run dry. Extn. of type *siquró- in Av. hixrom, n. ‘fluid’; G Seiber, LG Seifer, m. ‘spittle’; isophonic w. Ir. seachraim, v. ‘pollute’
15366:siqusos, sisquos ‘drained, dry’. Cf. siqu-, sinqu-, (sik-, sink-) and next. WP I, 506 and II, 467 Av. hikus, hikvaó, hiskus, husko & hiynus,adj. ‘dry’; Oss. xusk; Per. xušk, id.; Lat. siccus, id.; Olr. secc & sesc, id.; Ir. sic & seasc, id., seach- in cpds. id.; W hysp, f: hesp, id.; Br. hésk, hésp, id.; Cor. hesk, id.; OE cf. siwen- in siwen-1ege, adj. Árheum-eyed"; (uncertainly) Arm. hek, gs: hiKo, ab. s. -ov, & gs: hiki, ab. s. -av, adj. “sad?
16638:(soik-, cf. soiqu- and seik- (1), seiquo, siqu-. Ambig. in Skt. & Li.) MHG seihen, v. “strain, filter’; Skt. cf. sekah, m. 'outpour; libation'; sektram, n. ‘ladle’; Li. saikaü, ýti, v. and saikuoju, uoti, v. ‘bale out?
16644:soiquos ‘container, vessel, bucket’. Cf. siqu- (singu-), seiquð. WP II, 465. (Balt. ambig. cf. seiquos, and cf. seik-, soik-) OE så, m. *tub'; Sw. så, m. id.; ON sár, gs: sás, npl. sáir, m. ‘cask’; Blg. sék, m. (1) ‘tank- ard'; Li. saikas and (ambig.) siekas, m. (a
```


## [2026-09-14T01:34:07.085Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '88400,88420p' MON_part1.txt; echo \"=== pashanjidan MON ===\"; grep -n 'پشنجیدن\\|پشنگ' MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt | head -20",
 "description": "Mo'in sabun entry and pashanjidan"
}
```


### [2026-09-14T01:34:07.182Z] TOOL RESULT

```
خدای تعالی. (تص.) کسی که بر خدا و برای 
خدا صبر کند و جزع و شکایت نکند. 
صایو ته: (0-)2ان2ه [- سسایو ته» آسی 
(استی)] (.) زن ببر. 

صابون: ۰2050 (- صابون» معر.] (ا.) 
(شیم.) جسمی است که از ماده‌ای چرب 
ساخته شود و آن را در شستشوی بدن و 
لباس بکار برند. ضح.- (شیم.) صابون‌ها 
مخلوطی از نمک‌های سه اسید آلی بعنی 
اولئات» پالمیتات و استارات سدیم هستند. 


برای تهیةٌ صابون اسیدهای چربی‌دار را با 
سود سوزآور در دیگ‌های بزرک - که به 
وسیلة بخار آب گرم می‌شود - حرارت 
می‌دهند و بس از ۲۴ ساعت در قالب‌های 
چوبی بزرگ وارد می‌کنند و سپس به 
شمش‌های کوچکتر می‌برند و عاقبت بر اثر 
جریان هوای گرم خشکك می‌کنند و 
بصورت قالب‌های کوچک که علامت 
=== pashanjidan MON ===
incoming/MON/MON_2vol_Adena_v1_djvu.txt:32180:ردن» پشنگک ردن. 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:32183:افشاندن آب. آب مترشح: یک پشنگ آب. 
MON_part1.txt:32180:ردن» پشنگک ردن. 
MON_part1.txt:32183:افشاندن آب. آب مترشح: یک پشنگ آب.
```


## [2026-09-14T01:34:12.694Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '32170,32195p' MON_part1.txt",
 "description": "Mo'in pashang context"
}
```


### [2026-09-14T01:34:12.748Z] TOOL RESULT

```
(ص‌فا.) آنکه جامه پشمینه پوشد»ه لماس 
پشمین در بر کننده. (مج.) صوفی. (مج.) 
زاهد. 
او از اروت مان 
از موی پا گیاه و مانند آن که بدان آهار بر 
حامه و تانه افشانند. 
پش‌نجید د. 22 - فد [- شنجیدن] 
(مص‌م.) آب و امثال آن پاشیدن» گل نم 


ردن» پشنگک ردن. 

پشنک: 5 [ - - پشنج - بشنگ] (.) 
افشاندن آب. آب مترشح: یک پشنگ آب. 
پشسنگک: -021272 (ا.مسصف.) ژاله. 
نگرگ. 

پشودد. 025-2 (مصع.) بانگ زدن و 
زجر کردن. 

پشور: ۲080۲ [- پشول] (.) نفرین» دعای 
بد» لعنت» شول. 

پشه. (مدککهج ,(ع-)025 (.) (جان.) حشره‌ای 
از راستة دو بالان جزو رده بندپاییان که 
دارای اقسام و کٌونه‌های متعدد است. پشه
```


## [2026-09-14T01:34:14.166Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== BQT pashanjidan ===\"; grep -n 'پشنجیدن\\|پشنگ\\|پشنجید' BQT_v1_pages.txt BQT_v2_pages.txt | head -20",
 "description": "Borhan pashang"
}
```


### [2026-09-14T01:34:14.241Z] TOOL RESULT

```
=== BQT pashanjidan ===
BQT_v1_pages.txt:12889:برادر اقراسیاب‌بن پشنگه‌ین ورین آفرربدون‌است
BQT_v1_pages.txt:26005:لادن وس جنگ یش نگویند و مشفف پشنگه هم
BQT_v1_pages.txt:26057:بر آن خاك و خوش پشنجید‌اند .
```


## [2026-09-14T01:34:22.758Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '26040,26070p' BQT_v1_pages.txt; echo \"--- tag\"; grep -n 'pdf page' BQT_v1_pages.txt | awk -F: '$1<26060' | tail -2",
 "description": "Borhan v1 pashanjidan entry"
}
```


### [2026-09-14T01:34:23.994Z] TOOL RESULT

```
لشه - بفتح اول
۴1 ثانی هشن ء حانوری
است ممروف گونند چهل
روزعمر کند وبعضی گویند
بته خانه. با خای نقطه دار بالف
کشبده وفتح نون» نام‌درخت صده است که سربی
شجرقالیق (۱) خوانند ۷ .
بشه جورد » بفتح خای نفطه دار
و سکون واو ممدوله و را ودال بی‌تقطه » ریشی
و جراحتی باشد که بیشتر در ملك بلخ بهم رسد
و دیر خوب شود و کمان مردم اينکه از گزیدن
پثه بهم میرسد و آن را بعربی فرحة بلخی
گونند .
بشه‌ذاد ۸ ۰ بادال ابجد بالف کشیده
و برای قرشت زده . پثه خانه را گویند و آن
درختی است که بعربی شجرتالیق خوانند .
پشه‌غال » با ین نله دار و لام :
بر آن خاك و خوش پشنجید‌اند .
لمیبی . «لفت نامه».
بت ۴ رك : یشور .
طرة دوست پشولیده خوش است ۰
شرف شفروه. «لغت نامه».
دوم هردو آهثبه :
. پشه‌کی داند که عمرش تاکی است
۲ ره : بشمدار -
دربهاران زاد ومر کش در دی است.
مثنوی‌مولوی‌بلخی.بشی
بر وژن و ممنی بشه دار است که شجرء البق
باشه ٩‏ .
فشی س بکراول وانی وسکون تحتانی»
مخفف پشیزاست. و آن یرل ریز؛ کرچك بفابت
--- tag
```


## [2026-09-14T01:34:28.574Z] TOOL CALL #36: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-14T01:34:28.581Z] TOOL RESULT

```


```


## [2026-09-14T01:34:31.840Z] TOOL CALL #37: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/sey%E1%B8%B5%CA%B7-",
 "prompt": "What is the root, its meaning, and its descendants (Latin siccus, Avestan, Sanskrit siñcati)? Quote the entry."
}
```


## [2026-09-14T01:34:33.049Z] TOOL CALL #38: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/sack",
 "prompt": "What does Etymonline say about \"sack\" meaning a dry white wine — its origin from French sec / Spanish seco and Latin siccus?"
}
```


### [2026-09-14T01:34:33.282Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-14T01:34:37.369Z] TOOL RESULT

```
# Sack (Wine) Etymology

According to Etymonline, the word "sack" when referring to a dry white wine originates from the 1530s. The entry explains:

**Origin:** The term is "an alteration of French (_vin) sec_ 'dry (wine),'" which comes from Latin _siccus_ meaning "dry."

**Historical context:** The word originally referred to "strong, light-colored wine from Spain and the Canaries."

**Linguistic note:** Etymonline observes that the vowel development "is 'not a normal development from the original _seck_.'"

The entry traces the path: Latin _siccus_ (dry) → French _sec_ → English _sack_, showing how the Romance language word for "dry" became the English term for this category of wine.
```


## [2026-09-14T01:34:40.817Z] TOOL CALL #39: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/siccus",
 "prompt": "What is the etymology of Latin siccus? Which PIE root and cognates (Avestan hiku-, Persian xušk, Greek)? Quote it."
}
```


## [2026-09-14T01:34:42.679Z] TOOL CALL #40: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B5%D8%A7%D8%A8%D9%88%D9%86",
 "prompt": "Give the etymology sections for Arabic صابون and Persian صابون: what is the source language chain (Greek σάπων, Latin sapo, Germanic)? Quote."
}
```


### [2026-09-14T01:34:47.692Z] TOOL RESULT

```
# Etymology of Latin *siccus*

Based on the Wiktionary content, the etymology is:

**PIE Root:** The word derives from Proto-Indo-European *\*siskus* ("dry"), presumably from the root *[\*sek-](/wiki/Reconstruction:Proto-Indo-European/sek- "Reconstruction:Proto-Indo-European/sek-")* ("to dry up").

**Cognates Listed:** The page identifies these cognates:
- Ancient Greek *ἰσχνός* (iskhnós)
- Proto-Celtic *\*siskʷos*
- Lithuanian *sèkti* ("to lower oneself, sink, dry out")
- Sanskrit *असश्चुषी* (asaścuṣī, "not drying up")

**Note on Your Requested Cognates:** The document does not mention Avestan *hiku-*, Persian *xušk*, or provide the Greek term you referenced. The only Greek cognate cited is *iskhnós*. The etymology section notes "the phonetic details are unclear" regarding some comparisons.
```


### [2026-09-14T01:34:53.718Z] TOOL RESULT

```
# Etymology Chain for صابون (Sabun)

## Arabic Etymology

The Arabic word traces back through multiple languages: **Proto-Germanic *saipǭ → Latin sāpō → Ancient Greek σάπων (sápōn) → Classical Syriac ܨܲܦ݁ܘܿܢܵܐ (ṣappōnā) → Arabic صَابُون (ṣābūn)**.

The source document states: "from [Aramaic](https://en.wikipedia.org/wiki/Aramaic) _[צַפּוֹן](/wiki/%D7%A6%D7%A4%D7%95%D7%9F#Aramaic)_ / _[ܨܦܘܢ](/wiki/%DC%A8%DC%A6%DC%98%DC%A2%DC%90#Classical_Syriac)_ (ṣappōn), from [Ancient Greek](https://en.wikipedia.org/wiki/Ancient_Greek) _[σάπων](/wiki/%CF%83%CE%AC%CF%80%CF%89%CE%BD#Ancient_Greek)_ (sápōn), from [Latin](https://en.wikipedia.org/wiki/Latin) _[sāpōnem](/wiki/saponem#Latin)_...from [Proto-Germanic](https://en.wikipedia.org/wiki/Proto-Germanic_language) _[\*saipǭ](/wiki/Reconstruction:Proto-Germanic/saip%C7%AD)_."

## Persian Etymology

Persian borrowed directly from Arabic: "Ultimately from [Arabic](https://en.wikipedia.org/wiki/Arabic) _[صَابُون](#Arabic)_ (ṣābūn)."

Both languages share the same underlying etymological path, with Persian acquiring the word secondarily from Classical Arabic rather than directly from earlier languages.
```


## [2026-09-14T01:35:08.584Z] TOOL CALL #41: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E0%A4%B8%E0%A4%BF%E0%A4%9E%E0%A5%8D%E0%A4%9A%E0%A4%A4%E0%A4%BF",
 "prompt": "Sanskrit सिञ्चति (siñcati): meaning and etymology, root सिच् sic-, PIE root. Quote."
}
```


## [2026-09-14T01:35:09.238Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/sec",
 "prompt": "French sec: etymology and meaning (from Latin siccus). Quote the French section."
}
```


### [2026-09-14T01:35:14.039Z] TOOL RESULT

```
# French "sec": Etymology and Meaning

**Etymology:** The word "sec" comes from Latin *siccus* ("dry"), which itself derives from Proto-Indo-European *\*seyk-*.

**Direct Quote from the French Section:**
"Inherited from Old French *sec*, from Latin *siccus* ("dry"), from Proto-Indo-European *[\*seyk-](/wiki/Reconstruction:Proto-Indo-European/seyk- "Reconstruction:Proto-Indo-European/seyk-")*."

**Meaning:** In French, "sec" primarily means "dry" and can describe various conditions—from lacking moisture, to dried fruits, to describing thin/lean persons, to unsweetened alcoholic beverages. The term can also characterize someone as curt or abrupt in manner.
```


### [2026-09-14T01:35:14.566Z] TOOL RESULT

```
# सिञ्चति (Siñcati)

**Definition**: This Sanskrit verb means "to pour out, discharge, emit, shed" or alternatively "to sprinkle, moisten" and "to dip, soak."

**Etymology**: The word derives from the root सिच् (sic), ultimately tracing back to Proto-Indo-European *seykʷ-, meaning "to spill, pour; moisten, filter." It shares cognates with Ancient Greek ἰκμάς (moisture) and English "sea."

**Grammatical Details**: Siñcati functions as a third-singular indicative verb in class 6, with both active and middle voice forms documented in both Vedic and Classical Sanskrit.

**Historical Reference**: An example appears in the Ṛgveda (10.21.3, circa 1500-1000 BCE), where the phrase reads: "Those having (you) as their foundation flames sit upon you, **pouring out** with their tongues like women pouring with their ladles."
```


## [2026-09-14T01:35:19.788Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/desiccate",
 "prompt": "Etymology of desiccate: Latin desiccare, siccus. Quote."
}
```


## [2026-09-14T01:35:21.609Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%BE%D8%B4%D9%86%D8%AC%DB%8C%D8%AF%D9%86",
 "prompt": "Is there a Persian entry پشنجیدن? Give its meaning and etymology if present."
}
```


### [2026-09-14T01:35:23.676Z] TOOL RESULT

```
# Etymology of Desiccate

The word **desiccate** originated in the 1570s from Latin *desiccare*, meaning "to make very dry." The term combines the prefix *de-* (thoroughly) with *siccare* (to dry).

The root *siccare* traces back to Latin *siccus* (dry), which itself derives from the Proto-Indo-European root *seikw-*, meaning "to flow out." This ancient root also produced related words in Greek, Sanskrit, and other languages expressing the concept of dryness.

The intransitive sense—"become dry"—emerged later in the 1670s. The adjective form *desiccated* (deprived of moisture) became established by the same period.
```


### [2026-09-14T01:35:24.885Z] TOOL RESULT

```
# Persian Entry: پشنجیدن

Yes, there is a Persian entry for **پشنجیدن** (pašanjidan).

**Meaning:** According to the Wiktionary entry, this verb means "to sprinkle," though the source notes this sense is marked as obsolete.

**Etymology:** The entry does not provide etymological information. It only indicates the present stem is **پشنج** (pašanj), but no origin or historical development of the word is documented.
```


## [2026-09-14T01:35:30.523Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%B3%DA%A9/",
 "prompt": "What do Dehkhoda/Mo'in/Amid say about the Persian word سک (sek)? Is there a sense \"undiluted drink / neat (of drink)\" and is it marked as a French loanword (فر. sec)?"
}
```


## [2026-09-14T01:35:31.599Z] TOOL CALL #46: WebSearch

```json
{
 "query": "\"سک\" فارسی وام‌واژه فرانسوی sec نوشیدنی خالص بدون آب"
}
```


### [2026-09-14T01:35:36.970Z] TOOL RESULT

```
# Meanings of سک (sek) in Persian Dictionaries

Based on the Abadis dictionary content, the three major Persian lexicographers provide these definitions:

**Dehkhoda** lists multiple senses including a sharpened stick for driving animals, a medicinal preparation (an extract of myrobalan), vinegar, and various other meanings related to holes, nails, and fragrances.

**Mo'in (Moein)** provides: "چوبی نوک تیز که با آن چارپایان را برانند" (a sharpened stick for driving quadrupeds) and "سرکه" (vinegar).

**Amid (Emid)** defines it as a medicinal preparation made from myrobalan, date syrup, and musk, and also as "میله ای نوک تیز برای راندن چهارپایان" (a pointed rod for driving animals).

**Regarding your question:** The provided content does not indicate any sense meaning "undiluted drink/neat (of drink)" nor does it mark سک as a French loanword (sec). The entries show Persian, Arabic, and Sanskrit etymological connections, but no reference to French origins.
```


### [2026-09-14T01:35:38.523Z] TOOL RESULT

```
Web search results for query: ""سک" فارسی وام‌واژه فرانسوی sec نوشیدنی خالص بدون آب"

Links: [{"title":"مادام الملوک on X: \"من گمون می‌کردم «سک» در مشروب رو سِک خوردن که در فارسی میگیم، واژه دخیل فرانسویست. sec نوشیدن در فرانسوی یعنی الکل رو خالص خوردن و با چیزی یا مخصوصا آب قاتیش نکردن. اما اینطور که از توییت دوستمون برمیاد این دو faux amis هستند.\" / X","url":"https://x.com/Madameolmolouk/status/1964246074345808155"},{"title":"سک - ویکی‌واژه","url":"https://fa.wiktionary.org/wiki/%D8%B3%DA%A9"},{"title":"ترجمه - Google Translate","url":"https://translate.google.com/?hl=fa&langpair=en%7Cen"},{"title":"فهرست وام‌واژه‌های فرانسوی در فارسی - ویکی‌پدیا، دانشنامهٔ آزاد","url":"https://fa.wikipedia.org/wiki/%D9%81%D9%87%D8%B1%D8%B3%D8%AA_%D9%88%D8%A7%D9%85%E2%80%8C%D9%88%D8%A7%DA%98%D9%87%E2%80%8C%D9%87%D8%A7%DB%8C_%D9%81%D8%B1%D8%A7%D9%86%D8%B3%D9%88%DB%8C_%D8%AF%D8%B1_%D9%81%D8%A7%D8%B1%D8%B3%DB%8C"},{"title":"فهرست وام‌واژه‌های انگلیسی در فارسی - ویکی‌پدیا، دانشنامهٔ آزاد","url":"https://fa.wikipedia.org/wiki/%D9%81%D9%87%D8%B1%D8%B3%D8%AA_%D9%88%D8%A7%D9%85%E2%80%8C%D9%88%D8%A7%DA%98%D9%87%E2%80%8C%D9%87%D8%A7%DB%8C_%D8%A7%D9%86%DA%AF%D9%84%DB%8C%D8%B3%DB%8C_%D8%AF%D8%B1_%D9%81%D8%A7%D8%B1%D8%B3%DB%8C"},{"title":"پراستفاده‌ترین کلمات و اصطلاحات فرانسوی که در زبان فارسی رایج شده‌اند! - بهار نیوز","url":"https://www.baharnews.ir/news/516658/%D9%BE%D8%B1%D8%A7%D8%B3%D8%AA%D9%81%D8%A7%D8%AF%D9%87-%D8%AA%D8%B1%DB%8C%D9%86-%DA%A9%D9%84%D9%85%D8%A7%D8%AA-%D8%A7%D8%B5%D8%B7%D9%84%D8%A7%D8%AD%D8%A7%D8%AA-%D9%81%D8%B1%D8%A7%D9%86%D8%B3%D9%88%DB%8C-%D8%B2%D8%A8%D8%A7%D9%86-%D9%81%D8%A7%D8%B1%D8%B3%DB%8C-%D8%B1%D8%A7%DB%8C%D8%AC-%D8%B4%D8%AF%D9%87-%D8%A7%D9%86%D8%AF"},{"title":"ترگمان - ترجمه sec- به فارسی | معنی sec- به فارسی","url":"https://targoman.ir/d/en/sec-/"},{"title":"کلمات و اصطلاحات مربوط به خوراکی‌ها به زبان فرانسوی با ...","url":"https://tikkaa.ir/blog/edibles-in-french"},{"title":"13 اشتباه بی تربیتانه در زبان فرانسه - آموزش زبان فرانسه","url":"https://hifrench.com/13-%D8%A7%D8%B4%D8%AA%D8%A8%D8%A7%D9%87-%D8%A8%DB%8C-%D8%AA%D8%B1%D8%A8%DB%8C%D8%AA%D8%A7%D9%86%D9%87-%D8%AF%D8%B1-%D8%B2%D8%A8%D8%A7%D9%86-%D9%81%D8%B1%D8%A7%D9%86%D8%B3%D9%87/"}]

I found relevant results for your search query about "سک" (sek) as a Persian loanword from French. Here are the key findings:

"سک" (sek) in Persian refers to drinking alcohol pure without mixing it with anything, especially water, and this word is a loanword from the French word "sec".

However, according to the source, these two terms ("سک" in Persian and "sec" in French) are considered "faux amis" (false friends), meaning they appear related but have different connotations or uses between the two languages.

The search results also confirm that Persian has many French loanwords stemming from the Qajar period when Iran's relations with the Western world were primarily through France, with many of these words relating to sciences, technology, arts, and administrative fields.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-14T01:35:45.353Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://fa.wiktionary.org/wiki/%D8%B3%DA%A9",
 "prompt": "What senses and etymology does fa.wiktionary give for سک? Any sense \"خالص/بدون آب\" (neat drink) and any French origin?"
}
```


## [2026-09-14T01:35:48.532Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== SKT soap/sack/desiccate ===\"; grep -n -i '^Soap\\|Soap, ' SKT.txt | head -5; grep -n -i 'Sack (3)\\|Sack(3)\\|sack, a dry' SKT.txt | head -5; echo \"=== WEB sack wine ===\"; grep -n -i 'sack.*dry.*wine\\|vin sec' WEB_vol1.txt FSD_vol4.txt | head -5",
 "description": "Grep Skeat/Webster for soap and sack"
}
```


### [2026-09-14T01:35:48.652Z] TOOL RESULT

```
=== SKT soap/sack/desiccate ===
=== WEB sack wine ===
```


### [2026-09-14T01:35:51.355Z] TOOL RESULT

```
# Wiktionary Entry for سک

Based on the Persian Wiktionary page provided, here are the documented senses:

## Documented Senses

The entry lists two noun definitions:

1. **Vinegar** ("سرکه")
2. **A pointed wooden stick used to drive livestock** - described as "چوبی نوک تیز که با آن چارپایان را برانند"

Additionally, there's a dialectal sense from Gonabadi dialect meaning "to hide, conceal, lurk, or keep watch."

## Regarding Your Questions

**No "neat drink" sense**: The page does not include any definition relating to undiluted or water-free beverages (خالص/بدون آب).

**No French etymology noted**: The entry provides no etymology information whatsoever, let alone any French origin. The page simply lists the definitions and their sources (primarily *Farhang-e Loqat-e Moʿin*, a Persian dictionary).

The English translations provided are: goad, yerk, prod, prickle, and jab—all relating to the livestock-driving implement sense.
```


## [2026-09-14T01:35:54.248Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== SKT soap ===\"; grep -n -i 'soap' SKT.txt | head -8; echo \"=== SKT sack ===\"; grep -n -i 'SACK' SKT.txt | head -8; echo \"=== KLN sack wine ===\"; grep -n -i 'sack.*wine\\|dry wine' KLN_1966.txt KLN_1971.txt | head -8",
 "description": "Skeat/Klein soap and sack"
}
```


### [2026-09-14T01:35:54.361Z] TOOL RESULT

```
=== SKT soap ===
4256:rnfc\  ah.  1  L  c.  crab  like,  soappi^  or  awk- ward. Cr  Du.  ^luM^M,  to  ftcr&tcfa.  kriHm, lo  I*  peevUh  ;  Icel.  *»»A\i,  to  scrawl
10004:Lather.  (E.)  M.E. /fiM^r.  A.S /rf-rfKor, lather;  whence  WSrian,  lo  anoint.  +  Icel iavf>r,  froth,  foam,  soap.  Allied  to  Lre and  Lava.     (Case  LU.)
16484:savour.  (F.  -  L.)    O.  F.  savomr,  bt9 javfMr.  —  L.  saporern,  ace  ol  sapor,  taste-* L.  sapere,  to  be  aware. Saponaceous :  see  Soap. Sapphic,    a    kind    of  metre. L.    sapphicus,    belonging    to    .'- Gk.  Xa>^,  Sappho  of  Lesbos,  uic-i  ^v^j^
17380:Bkeptla ;  see  Soaptio.
17671:sapoimceous.  soapy.  (L)  Coined,  as if  from  L.  suponactHs*,  from  L.  tapotumt dec.  of /(iA».  soap  I.Pliny). Soar.  (F. - L.)  M.  E. xoreH,  —  F. «w/rr, i&  cx|x*sc  lo  air ;  also,  '  to  sore  up,*  Col.  * itiw  i«  radr«raiT*  ^not  fouod),  to  expose
19423:terreen,  tureen,  a  I  urge  bowl  fur  soap. (F.  — L.)  Both  spellings  are  bad;  territu would  be  belter.  — F.  UrHnt,  an  earthen pan.  —  L.  terra,  cuth ;  with sufttx  inus.
21945:art.    Thii  nlsoappcan  as
23250:sop — soap.                      <
=== SKT sack ===
8172:Hnberdasher,  a  seller  of  smnll  warca. [,F.*Scan<.1.l  So  oamcl  from  bis  selling a  bluff  callcil  haftriaj  in  O.  F. ,  see  Liber AUua,  ed.  Riley,  pp  235,  331. *0.  led. hapuriaxk,  ihiogs  oif  small  v-alue  (Gud- muiiHus  Andrea:).  I  suspect  that  the  true Bcuse  was  •  pedlan' w&re$/  named  from  the havcr^'Ack  In  which  they  were  cnrried  ;  from Icel.  haprtaik,  ha/rtask,  a  haveisnck:  oiig. a  Img  lor  oals.  —  Icel.  Ma/r,  oais;  tas^, a  pouch  (cf.  G.  ttuchi,  a  pouch).  See Haversack.
8436:Haveraack,    tuMic/^    ,  .^ (F,  —  G.t     F.    Aavrrsfw.  —  G. haftrsoik.  lit.  '  oa(-bng.'  — G.  AdAfr^ OBIS  ;  saik.  a  sack,     ^e  Uaberdaahar
9738:knapsack,  lit.  a  provision-bag.  »Du.  knaf, eatii'g.  kNapf^n,  to  crush,  eat  (a  word  of Celtic  origin^  as  above) ;  sak,  a  sack  (a word  of  Hebicw  origin! ;  see  Saolc.
15567:Baneack.  (Scaod.)  Icel.  rannsaka.  to search  a  house,  ransack;  Swed.  ransaka, Don.  ransag/.  -•  Icel.  rann,  a  hou>e,  abode : tak,  base  of  lakja,  to  seek.  Tht  Icel.  rann stands  for  rosn  *,  and  is  the  same  as  \.  S.
16085:Rifle  II),  to  spoil,  plunder.  (F.-Tcut.) F.  rifltr^  '  to  rifle,  spoilc  ; '  Col.  Formnl, with  frequentative  -/-,  from  Icel.  Mr^/a, rifa,  to  catch,  grapple,  grasp,  allied  to which  is  Icel.  hrifi,  plunder.  (^  KAKP.) riff-raff,  refuse.  (F.-Teut)  M.E.r*/ and  raf,  things  of  small  value,  hence  eveiy bit.»F.  rif  tt  raft  every  bit;  aUo  spelt rijie  et  rafit.  *  II  nc  lui  lairra  ri/  m/  raf, he  will  strip  him  of  all ;  *  Cot,  Here  ri/ or  ri^f  is  a  thing  of  small  value,  from ri/ttr,  to  rifle,  ransack ;  and  ra^t  it  from O.  F.  mffltr^  to  rifle,  ravage.  Both  are words  of  Tcut.  origin,  drawn  tocher  by their  sound,  though  of  different  ungin  F. nfitr  is  from  Ictl.  ht-ifa  ^above) ;  F.  raffitr isfrnm  G.  rajfen,  to  >eire;  see  Rape  (1).
16323:SACK.
16343:Sack  (I),  a  bag.  (L.  -  Gk  -  Heb.  - Egyptian?)  M.E.  sak.  AS.  laee.  -  Lu mtimi. «  Gk  vittmot. »  Heb.  taq,  nck-doth.
16344:a  sack  for  com.  Prob.  of  Egyptian  oij cf.  Coptic  jui.  fack-clolh  (Pe)roo>.  r Heb.  sa^  are  borrowed  Da.  Mk,  G. &c.
=== KLN sack wine ===
KLN_1971.txt:210678:sack, n, ( strong wine. — Formerly spelled seek, 
KLN_1971.txt:210679:fr. F. (vi/i) sec, ‘dry wine’, fr. L. siccus, ‘dry’. 
KLN_1966.txt:33445:sack,  n.,  strong  wine.  —  Formerly  spelled  seek, fr.  F.  (v/n)  sec,  ‘dry  wine’,  fr.  L.  siccus,  ‘dry’. See  siccative  and  cp.  sec,  secco. sackbut,  n.,  1)  a  medieval  wind  instrument,  fore¬ runner  of  the  trombone;  2)  a  stringed  instru¬ ment  resembling  the  guitar,  in  Dan  3:5  used wrongly  to  translate  Aram.  sabb*kha.  —  MF. (=  F.)  saquebute,  fr.  OF.  saqueboute,  com¬ pounded  of  saquer,  ‘to  pull,  draw  out  ,  and bouter,  ‘to  thrust'.  See  saccade  and  butt,  ‘to strike’.
KLN_1966.txt:34370:seek,  adj.,  dry,  barren,  unprofitable.  —  F.  sec, ‘dry’,  fr.  L.  siccus.  See  siccative  and  cp.  sack, ‘strong  wine’,  sec,  secco.
KLN_1966.txt:35121:siccative,  adj.  —  Late  L.  siccativus,  ‘drying,  sicca¬ tive’,  fr.  L.  siccatus,  pp.  of  siecare,  ‘to  dry’,  fr. siccus,  ‘dry’,  which  is  cogn.  with  Avestic  hiku-, ‘dry’,  Gk  icryyic,,  ‘dry,  withered’,  Lith.  seklus, ‘shallow’,  Lett,  sekls,  of  s.m.,  Lith.  senku,  sekti, ‘to  fall’  (said  of  the  water  level),  nu-sekti,  ‘be¬ come  dry’,  Lett,  siku,  sikt,  ‘to  dry  up",  Mir. sesc,  ‘dry’,  and  with  OI.  siheati,  ‘makes  dry’.  Cp. desiccate,  exsiccate,  bortus  siccus,  sack,  ‘strong wine’,  sec,  secco.  Cp.  also  phthisis.  For  the  end¬ ing  see  suff.  -ative.
```


## [2026-09-14T01:36:06.434Z] TOOL CALL #50: Bash

```json
{
 "command": "ls site/pages/437.jpg 2>/dev/null; pdftoppm -f 437 -l 437 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg437-437 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg437-437.png",
 "description": "Render PDF page 437"
}
```


### [2026-09-14T01:36:08.159Z] TOOL RESULT

```
site/pages/437.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb 60815 Sep 13 21:36 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg437-437.png
```


## [2026-09-14T01:36:10.403Z] TOOL CALL #51: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg437-437.png"
}
```


### [2026-09-14T01:36:11.067Z] TOOL RESULT

```

```


## [2026-09-14T01:36:11.064Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-14T01:36:26.634Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; S=/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad; pdftoppm -f 437 -l 437 -r 600 -png -singlefile EtymologicalDictionary-persian-english.pdf $S/pg437hi-437 && python3 -c \"\nfrom PIL import Image\nim=Image.open('$S/pg437hi-437.png'); w,h=im.size; print(w,h)\n# fra-saekam around x 370/1545, y 377/2000 in displayed\nx0=int(0.225*w); x1=int(0.40*w); y0=int(0.180*h); y1=int(0.196*h)\nim.crop((x0,y0,x1,y1)).resize(((x1-x0)*2,(y1-y0)*2)).save('$S/crop-437.png')\n\"",
 "description": "High-res crop of fra-saekam"
}
```


### [2026-09-14T01:36:31.426Z] TOOL RESULT

```
5100 6600
```


## [2026-09-14T01:36:33.487Z] TOOL CALL #53: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/crop-437.png"
}
```


### [2026-09-14T01:36:33.509Z] TOOL RESULT

```

```


## [2026-09-14T01:37:24.741Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"--- TAD ff pages\"; python3 -c \"\nt=open('TAD_pages.txt',encoding='utf-8',errors='replace').read()\npp=t.split('\\f'); print('pages',len(pp))\nfor i,p in enumerate(pp):\n    if 'صابون' in p: print('leaf idx',i, 'first 80:', p[:80].replace(chr(10),' '))\n\"; echo \"--- SOD ff\"; python3 -c \"\nt=open('SOD_pages.txt',encoding='utf-8',errors='replace').read()\npp=t.split('\\f'); print('pages',len(pp))\nfor i,p in enumerate(pp):\n    if '7537 psync' in p: print('leaf idx',i)\n\"",
 "description": "Locate TAD and SOD page indices"
}
```


## [2026-09-14T01:37:25.569Z] TOOL CALL #55: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/sip",
 "prompt": "Etymology of English \"sip\": is it related to sup/soap/PIE seib-? Quote."
}
```


### [2026-09-14T01:37:25.961Z] TOOL RESULT

```
--- TAD ff pages
pages 87
leaf idx 46 first 80:                                      ‫سوج اه‬                                   
--- SOD ff
pages 645
leaf idx 369
```


### [2026-09-14T01:37:31.275Z] TOOL RESULT

```
# Etymology of "Sip"

Based on the Online Etymology Dictionary, "sip" has uncertain origins but is likely connected to "sup" through Germanic roots.

The verb "sip" comes from "late 14c., _sippen_, 'drink little by little, drink in small mouthfuls'" and may derive from Continental Germanic sources or Old English _sypian_, which relates to _supan_ meaning "to take into the mouth a little at a time."

Regarding your specific question: **Yes, sip and sup are related.** The OED notes that sip is "possibly a modification of _sup_ intended to express a slighter action."

Both words trace back to Proto-Germanic *supanan, which ultimately derives from the PIE root *sub- (or possibly an extended form of *seue-), meaning "to take liquid." This root family also connects to words like "succus" (Latin for juice), "sugere" (Latin for suck), and Sanskrit "sunoti" (presses out juice).

However, the etymology provided does **not** mention "soap" or the PIE root "seib-" as related to "sip."
```


## [2026-09-14T01:37:40.527Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nprint(json.dumps(d['TAD'],ensure_ascii=False,indent=1))\nprint(json.dumps(d['SOD'].get('page_offset'),ensure_ascii=False))\n\"",
 "description": "TAD offset info"
}
```


### [2026-09-14T01:37:41.601Z] TOOL RESULT

```
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
"printed page ≈ leaf − 66 in SOD_pages.txt (0-based \\f blocks; 645 leaves; English intro precedes)"
```


## [2026-09-14T01:37:51.230Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; for u in \\\n \"https://www.etymonline.com/word/sack\" \\\n \"https://www.etymonline.com/word/desiccate\" \\\n \"https://www.etymonline.com/word/sip\" \\\n \"https://en.wiktionary.org/wiki/siccus\" \\\n \"https://en.wiktionary.org/wiki/sec\" \\\n \"https://en.wiktionary.org/wiki/%D8%B5%D8%A7%D8%A8%D9%88%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%E0%A4%B8%E0%A4%BF%E0%A4%9E%E0%A5%8D%E0%A4%9A%E0%A4%A4%E0%A4%BF\" \\\n \"https://en.wiktionary.org/wiki/%D9%BE%D8%B4%D9%86%D8%AC%DB%8C%D8%AF%D9%86\" \\\n \"https://fa.wiktionary.org/wiki/%D8%B3%DA%A9\" \\\n \"https://abadis.ir/fatofa/%D8%B3%DA%A9/\" ; do\n  timeout 120 python3 tools/fetch_source.py \"$u\" --note \"pdf page 437 (book 407), roots Seiku/Seip: verification of siccus/sec/sack/desiccate/sip, Skt sincati, pasanjidan, Arabic-Persian sabun, Persian sek\" 2>&1 | tail -2\ndone",
 "description": "Archive web sources"
}
```


### [2026-09-14T01:37:57.283Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/c005b6f0e81b9d12.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c48ae04de76aef4d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d638e4329200e7bf.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c57bfdc8bc0367ed.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1d7c617f0508e2a6.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0dd41a8d6f406977.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/226db5510803a905.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3d90ebf6bb71f5c0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d4c8ccbf30977ec4.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/518380864695310a.txt
```


## [2026-09-14T01:38:05.844Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== WLD Bd2 seiq/seip ===\"; grep -n 'seiq\\|sinq\\|seip-\\|seib-\\|sāpo\\|sapo,' incoming/WLD/WLD_Bd2_pages.txt | head -20",
 "description": "Grep Walde-Pokorny Bd II"
}
```


### [2026-09-14T01:38:05.903Z] TOOL RESULT

```
=== WLD Bd2 seiq/seip ===
31007:(auch ein *seib- neben *seip- (s. d.) ist schwach begriindet, andrerseits ist
31015:   Vgl. Curtius^ 137, Pick 1^ 137, 323, 558 (ohne Scheidung von '^seip-)y
31571:      Keben seq- steht sparliches (seiq-)                     :   soiq~ : siq- in:
35619:nan ds., nhd. scheinen (^-Praes ygl. abg. sinqti^ Hirt BB. 24, 263, PBrB.
35659:     Abg.   sijati^ sinqti „glanzen, scheinen, hell werden", sMh „Schatten“
35679:Slav, sim: sinqti,     — Ygl. das ahnliche {s)qai{^-t-,^ d-\ das aber auf belles
```


## [2026-09-14T01:38:07.400Z] TOOL CALL #59: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CF%83%CE%AC%CF%80%CF%89%CE%BD",
 "prompt": "Ancient Greek σάπων: meaning, etymology (borrowed from Latin sapo?), earliest attestation. Quote."
}
```


### [2026-09-14T01:38:13.120Z] TOOL RESULT

```
# σάπων (Ancient Greek)

**Meaning:** Soap, attested in Koine Greek texts.

**Etymology:** The word's origin is debated. It is "usually said to be from Latin _sāpō_," though borrowing from Galatian is also possible. Ultimately traced to Proto-Germanic *saipǭ and Proto-Indo-European roots meaning "to pour, strain, trickle."

**Earliest Attestation:** The documented uses include references from Aretaeus of Cappadocia's medical work and Pliny the Elder's _Natural History_ (77 CE), as well as Serenus Sammonicus.
```


## [2026-09-14T01:38:15.677Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '30995,31020p' incoming/WLD/WLD_Bd2_pages.txt; echo \"......\"; sed -n '31565,31585p' incoming/WLD/WLD_Bd2_pages.txt",
 "description": "Read Walde-Pokorny seip/seiq contexts"
}
```


### [2026-09-14T01:38:15.757Z] TOOL RESULT

```
des Wasser'^, ags. sic „Wasserlauf^, mnd. slk „medriges und sumpfiges
Land, Wasserpfiitze*^, bes. Palk-Torp u. sikle^ der germ. k(k) aus idg. kn-
vermutet; die Worte sichern keinesfalls eine idg. Wzf. auf -g                                        (s. o.   uber
lat.   siat
  tiber got. siggan „sinken^^          s.   *seng^   ;
                                                          nicht sekundarer Ablaut zu einem
idg, s'l-n-g^- (Reichelt       KZ. 39, 78);     ein       idg.    *seig^       als   Grundlage von gr.
                                         seigh           seip                                     467

poet, ei^oy „traufle,     vergieBe           tropfenweise^^,          xaTsl^co   „lasse   herabflieBen
(TraneTi)“,   -o/nai „rinne herab''           (Brugmann         P 610, 630), l^dvr}* xddog, dv-
tXtjti^qiovHes. (usw., s. Solmsen Beitr. 67) hat keine anderweitige Stutze
(auch ein *seib- neben *seip- (s. d.) ist schwach begriindet, andrerseits ist
freilich auch die Vereinigung mit Xsl^o) unter einer Gdf. *lieib- oder dgl.,
Lit, bei Boisacq 220, 565 nicht iiberzeugead: Kreuzung von ^seiJco. ’^eh'co
mit Xst^col).   — tiber dt. seichf und lett. s^kit s. "^selc- und            Uber             —
gall Sequana „Seine^‘ s. Loth Rc. 15, 98 f., 368, Schulze Eigennamen 10,
Osthoff IF. 27, 173, Pedersen KG, 1 4. Vf. tiber alteste sprachl. Beziehungen
zw. Kelten und Italikern 57 Anm. 1, Pokorny lA. 38/39, S. 12 (Philipon Rc.
30, 255 erklarfc den Kamen als iberisch; nicht xiberzeugend).
   Vgl. Curtius^ 137, Pick 1^ 137, 323, 558 (ohne Scheidung von '^seip-)y
111^ 439, Zupitza Gutt. 68f., Falk-Torp u. seij si, sigfi II, silde, sil t, so,
   Daneben eine Wz. seik- „trocken“, die wohl tiber „abrinnen, versiegen
= austrocknen'^ mit seih- „ausgieBen“ zu vereinigen ist (vgl. dieselbe Doppel-
heit bei sak-^ senk- „abrinnen“) av. kaecaydti mit iis „trocknet aus^* (trans.),
                                         :
......
                                                    erw^t Leskien Abl. 341),
   Lit. i-sekti „eingraben", iszsekti „sculpere'" (c?
  Abg. sekq, Sfisti „schneiden‘‘, scch'O „Axt“ (: lat. secl>euni), sekyra „Axt",
woneben "^sekyra in skr. sjekira nach sekq wohl nur sekundar umgestaltet;
wruss.                    „carex‘‘ (?        wegen o-; eher formal             =   lit.   aszakd „Pischgrate“,
AYz. akl);              zur Prage von slav. socJia „Knuppel, Pflug usw." s. u. Mk~ „A8t“.
      Keben seq- steht sparliches (seiq-)                     :   soiq~ : siq- in:
      lat.   s7ca „Dolch“, sicVis „Lanzenspitze'*;                      lit.   sykis „Hieb, Mai"            (Wiede-
mann Lit. Praet. 32, G. Meyer Alb. St. Ill 34 f.), wohl klr. syc m. „der nach
dem Abbrechen des Astes hinterbleibende Teil des Stammes" (v. d. Osten-
Sacken IP. 33, 257); ags. sagol m. „Stock, Keule"=mhd. seigel „Leiter-
sprosse, Stufe“; nhd. mdartl. saich „Schilf‘                  (s.   Zupitza Gutt. 137, Falk-Torp
u. sigd)\
                     nach Brgm. IF. 3, 260 f. zu ai. sayalza-h „zuiia Schleudern
     sTca, syhis nicht
bestimmt'*, n. „Wurfgescho6, Pfeil“,      m. „Schwert‘', sayika „Dolcli^‘ (s. u.
jjentsenden^^) ; ^ca auch nicht „8abiiiisches Lw/* mit i aus e nach Bthl. IF.
3, 28a 1.   — Abg. sekq aus *s9iqo herzuleiten, verwehrt abg. sekyra (gegen
Wiedemann aaO., Solmsen KZ. 34, If,).
   DaB se\i\q- das allein urspriingliche, seq- und saq- (lat. saxum; ahd. sahs^t)
auf Grand von seq- neugebildete Vokaistufen seien (Wiedemann, Solmsen),
```


## [2026-09-14T01:38:21.270Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n 'Seife' incoming/WLD/WLD_Bd2_pages.txt | head -10",
 "description": "Grep WLD Bd2 for Seife"
}
```


### [2026-09-14T01:38:21.330Z] TOOL RESULT

```
7046:Seifenblase,  Blaschen, Pustel“. Uhlenbeck PBrB, 18, 238, Berneker 79.
16382:-dhlo-) ,,Seife'';
29354:  aisl.laudr „Lauge, Seifenschaum, Schaum”, ags. leapor ,,Seifenschaum*"
30750:dt.    Seife),
31073:auch der germ. Name der Seife: ahd. seifa^ seiffa^ seipfa „Seife, auch
31074:Harz‘S, mnd. sepe „Seife“, ags. sape f, (daraus nord. sCtpa) „Seife" (sap
```


## [2026-09-14T01:38:23.656Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '31055,31095p' incoming/WLD/WLD_Bd2_pages.txt",
 "description": "WLD seip- entry with Seife/sapo"
}
```


### [2026-09-14T01:38:23.718Z] TOOL RESULT

```
sirJiten^ und anord. sef n. ,juncus“ (wegen des „durchl6cherten'‘, porosen

Stengels, vgl. aksl. sito „Sieb‘‘, sih „juncus“, Fick IIH 440); mnd. sever m,
„Schleim,     Geifer“,   afries. sever,        saver n.        ds.,   ahd. seivar, mhd. seifer m.
ds. (mhd. seifel m. „Speicheh' vielleicht mit germ,                                md. sZ/b„sumpfige
                                                                      p, s. u.);
Bodenstelle^, serb. stpifi „rieseln, fein ^egnen‘^
  Im Germ, auch Formen mit germ, p (die an sich ebenso wenig den Schlu&
auf idg. h rechtfertigen, wie die unter Vii- „ausgie6en‘‘ angeftihrten Formen
mit germ, k den auf idg. ^): ags. sJpian, mnd. slpen „tropfenweise                             fallen,
468                                              seu-



sickern^',      ndl.   Bijpplen „tr6pfeln'^,    mhd. slfen   (st. V.)    ds.,    schwed. mdartl.
sipa „langsam          fiiefien,   sickern*^ dan. Mter sibe „tropfenweis flieBen", norw.
mdartl. sTpa „ weinen“, mnd. sip „Bachlein“, slpe „iiiedrige und feuchte
Wiese“, mhd. slfe ,;langsam rinnender Wasserlauf, niedrige *Wiese‘‘; hieher
auch der germ. Name der Seife: ahd. seifa^ seiffa^ seipfa „Seife, auch
Harz‘S, mnd. sepe „Seife“, ags. sape f, (daraus nord. sCtpa) „Seife" (sap
„Harz, Pomade'"), vgl. Yf. LEWb.^ u. sapo (germ, Lw.), Schrader RL. 761,
 H. Schroder ZfdPh. 38, 519, Uhlenbeck IF. 25, 145, Falk-Torp u. sashe
hber die Frage, ob das Wort ursprgl. „TJrin‘" als Waschmittel (vgl. ahd.
seicJi „Harn“ von Wz. seiJc) oder ein „Eesinat“ (vgl. as. drupil „Harz‘' dt.                :



tropfeln) bezeichnet habe, ferner, ob neben germ, ^saip(^on- auch ein germ.
^sepon- „Ta1g (auch zu Haarfarbemitteln verwendet)" anzusetzen sei, das
mit lat. sebum „Talg‘" (wohl echt lat.) auf ein idg. *5e[^]6o- „tropfbares
    1.
Fett""  beziehbar ware (das lat. b ware dann Zeuge fur eine Wzf. auf
idg. b).
     Ygl. Fick BB. 7, 270, Wb.    137, 558, L. Meyer II 837, Persson Wzerw.
7,   176, Pick III ^ 440, Falk-Torp u. sigteHl,^ siv, sive, scebe^ und s. ^seik-
„ausgie6en"".

I.   sen- „Saft, Feuchtes“; verbal: „Saft ausdrucken" und „regnen; rinnen",
          in Weiterbildungen „(Saft) schliirfen, saugen"". scheint urspriinglich
          den Laut wiedergegeben zu haben, mit dem man flussiges aufschliirft.
          Gr.     „es regnet'", voy „lasse regnen""                  vexo^ ^starker Regen"
```


## [2026-09-14T01:38:30.505Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== LEW sapo ===\"; grep -n 'sapo:\\|sapo,\\|sāpo' LEW_1910.txt | head -6; echo \"=== LEW siccus ===\"; grep -n 'siccus' LEW_1910.txt | head -6; echo \"=== LAT ===\"; grep -n 'siccus\\|sapo' LAT.txt | head -8",
 "description": "Grep Walde LEW and Ernout-Meillet"
}
```


### [2026-09-14T01:38:30.598Z] TOOL RESULT

```
=== LEW sapo ===
=== LEW siccus ===
=== LAT ===
1187:saporum genera... dulcis suauis pinguis amarus austerus acer acutus
4625:gelidus atque siccus et sine pluuia, qui non discutit nubes sed strin¬
4938:et a AtA concurrencA par une foraation plus expressive, siccus, pan¬
5623:D 4 formation de struthium i-thion) "saponaire'.', cf. Celse 5,33,8, ou
6395:distingue un auster siccus, serenus d'un auster umidusj 3° la r 6 gion
23250:la saveur foedus sapor, de 1 'odeur herba odoris foedi. Assez fr^quent
27188:cret, gofit d'une chose ( = sapor)} puis, bchantillon, spbcinen pour
31942:(Caton oppose ager laetus a ager siccus, Agr.6i,s), des moissons, du
```


## [2026-09-14T01:38:34.059Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n '1,120p' tools/verify_check.py",
 "description": "Read verify_check.py"
}
```


### [2026-09-14T01:38:34.111Z] TOOL RESULT

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


## [2026-09-14T01:39:06.334Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '9035,9075p' CHEUNG.txt",
 "description": "Cheung entry context"
}
```


### [2026-09-14T01:39:06.395Z] TOOL RESULT

```
*SANSKRIT: sas ‘to sleep’ (RV+) = EWAia II: 716 
9 Further Ir. cognates are unknown. 
«PIE *ses- to sleep’ = LIV: 536 f. | Pok.: — 


*IE COGNATES: Hitt. 3e-es-zi ‘sleeps’, Luw. /sassa-' ‘to sleep’ 
*REFERENCES: Werba 1997: 252 


*haié ‘to pour (out), moisten’ 
*AVESTAN: Y Av. haéc- ‘to pour (out); to irrigate’ || (+ *pati-) ‘to besprinkle, pour on 
(ritually with water or cow’s urine)’ || (+ *para-) ‘to pour, flow out, away’ || (+ *fra-) 


‘to sprinkle, pour out’ — Liste: 72 

Pres. n-: IND. 3sg. YAv. hincaiti (V 5.5), med. YAv. “fra.hincaite (N 68 = Kotwal — Kreyenbroek: N 
50.7), 3pl. YAv. frasicinti (Yt 14.54), INJ. 3sg. YAv. hincat (F 673), SUBJ. 3sg. YAv. hincäiti (N 83), 
OPT. 2sg. YAv. paiti.hincdis (V 8.40, V 8.58, V 8.70 f., etc.), 3sg. YAv. paiti.hincöit (V 9.47), 3pl. YAv. 
para.hincaiion (V 6.32); Perf.: IND. 35р. ? YAv. "frahisaeca (Yt 10.138); Partic.: pres. them. ? OAv. 
haécat.aspa- (Y 46.15, Y 53.3); Inf.: YAv. hixtaiiae(-ca) ‘to moisten, [BMP transl.] /namb kardan/’ (V 
6.6); Caus.: SUBJ. 3sg. YAv. haecaiiat (V 5.12 f., V 8.10 £), perf. pass. perf. pass. YAv. frahixta- (Yt 
10.96). © On the name OAv. haécat.aspa- see Mayrhofer 1979: по. 164. 


*MIDDLE PERSIAN: BMP wysync- /wis-Sinj-/ ‘venom-spurting’ (cf. Nyberg II: 216a) 
|| (+ *pati-) BMP psnc- /passinj-/ ‘to sprinkle’ || (+ *pari-) MMP prsynz- ‘to flow 
through’ = DMMPP: 280a 

(+ *pati-) Pres.: IND. 3sg. BMP psncyt /passinjéd/; Partic.: perf. pass. BMP pshtk /passixtag/ || (+ *pari-) 
Pres.: IND. 3sg. MMP prsynzyd 

*PARTHIAN: (+ *ä-) ’Syxt (pret. stem) ‘to pour, flow, overflow; sprinkle’ 
c DMMPP: 58a 

Partic.: perf. pass. ’Syxt, *’Syxt 

*KHOTANESE: häs- ‘to wet, besprinkle’? > SGS: — 

*SOGDIAN: (+ *а-) MSogd. "Sync ‘to pour’ (-s- from *pati-formation) || (+ *pati-)
```


## [2026-09-14T01:39:09.502Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '9075,9115p' CHEUNG.txt",
 "description": "Cheung entry continued (Sogdian, NP)"
}
```


### [2026-09-14T01:39:09.554Z] TOOL RESULT

```
*SOGDIAN: (+ *а-) MSogd. "Sync ‘to pour’ (-s- from *pati-formation) || (+ *pati-) 
CSogd. pSync- ‘to pour’ 

(+ *a-) Impf.: IND. 3sg. MSogd. m’Sync; Partic.: perf. pass. (Ё) BSogd. ’’Sych || (+ *pati-) "z-Impf.: IND. 
159. CSogd. pSync’zw; Partic.: pres. CSogd. psyncn’ ‘oh spiller !’ 

*CHORESMIAN: (+ *apa-) bync- ‘to pour out, scoop (water)? = Samadi: 33a f. 

*NWIR: NP xesandan/xesan- (inch.-caus. ?) ‘to soak, moisten’, Gz. enjue ‘he pours’, 
Gz. yüsn- (inch. ?) ‘to soak’, NP hes, xés, Gz. yüs ‘wet, moist’ || (+ *pati-) NP 
pisanjidan ‘to sprinkle’, Khor. pšing ‘spraying, explosion’ 

*NEIR: ? Wa. Xonz-, Xan3-/Xayn- ‘to pour over, into’ || (+ *abi-) (inch. ?) Sh. biyis-/ 
biyid, (Baj.) biwis-/biwéd, Rosh. buways-/buwayd, Sariq. bilis-/bileyd, bülis-/ 
büleyd ‘to swell, inflate’, Sariq. balis-/baleid ‘to ferment, rise (dough); to foam 
(water in a torrent)’ || (+ *ui-) Sariq. waluys-/walud, (perf.) walusc ‘to spread, 
expand, swell, inflate, spill’, (Shaw) walis-/waltiyd ‘to flood, spread out’. 9 As for 
the initial X- of Wa. Xonz-, Xonz-/Xoyn-, it is from *h- before *-(a)i (?), cf. Oss. I. 
xid, D. xed ‘bridge’ (< *haitu-, Av. haetu-). 


128 *haiš ? 


*SANSKRIT: sec ‘to pour (out)’ (RV+) = EWAia II: 744 
«PIE *seik"- ‘to рош” © LIV: 523 | Pok.: 893 f. 
*IE COGNATES: OHG sihan ‘to sift’, OE séon ‘to flow away, to sift’, OCS sscati ‘to 


urinate’ 
*REFERENCES: IIFL II: 553; EVS: 19a, 89b; DKS: 488b; WIM II/1: 79; WIM W/2: 698; Monchi-Zadeh 
1990: 146; Werba 1997: 254; Steblin-Kamenskij 1999: 418 


*haiS ? ‘to see, watch ?' 

*AVESTAN: OAv. his- ‘to see, watch ?’ — Liste: 73 

Partic.: pres. OAV. vispa.hisas (Y 45.4). 9 On the basis of the Pahlavi translation: hlwsp nkylyd'l /harwisp 
nigeridär/ ‘all-watching’.
```


## [2026-09-14T01:39:44.998Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== ARY sek ===\"; grep -n 'سِک\\|«سک»' incoming/ARY/ARY_pages.txt | head -5; grep -n -i '^SEC\\b\\|SICCUS' incoming/ARY/ARY_latin_index_pages.txt | head -5; echo \"=== BQT v2 sek ===\"; grep -n 'خالص و بی‌آب\\|سک ' BQT_v2_pages.txt | head -5; echo \"=== AFA sabun latin ===\"; grep -n -i 'sapo\\|Seife' AFA.txt | head -5",
 "description": "Grep for Persian sek and Fraenkel sapo"
}
```


### [2026-09-14T01:39:45.109Z] TOOL RESULT

```
=== ARY sek ===
=== BQT v2 sek ===
889: ‫جاور سک بروزن باور » بمعنی حال‬                                                          ‫بودن باشد ‪.‬‬
9190:                                                                ‫وان سک ار عنام آزعه ات و ری‬                 ‫ات‬
11107: ‫ان‬     ‫مژیدالفضلا یمعنی سک انگور هم ا‬
11937:  ‫تش‌هم‌باشد » وی‬       ‫سوزنده را گودند که درآنآ‬         ‫جند بیدستر باشد ‪ .‬گوبند خایة سک آبی‬
16324:           ‫ابن کریباش کیرد آن دامن‪.‬‬                            ‫سک ودربان چوافتند غریب‬
=== AFA sabun latin ===
10139:letgegenstiinden muss noch der Name der Seife j^^jLö
10142:tätwv sapo (keltischen Ursprungs) zurück, sondern auf
```


## [2026-09-14T01:39:47.131Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '10130,10155p' AFA.txt",
 "description": "Fraenkel on sabun"
}
```


### [2026-09-14T01:39:47.187Z] TOOL RESULT

```
A291
Märtyrer Note 2132 hat Beispiele für die Traascriptioa
durch <-▲ gegeben. Dazu kaun noch gefügt werden tal-
mudisch Vyjr\Ü (noch unerkliirt) 'firubin 29^,^ (Riisi nLöf-
fei") = jJ^-J^Lä. Vull. I. 553. Daneben noch die Tran-
scription durch *-i-i vgl. |J.«^=1-)'«a] PSm. 406 wofür wohl
iliy^i'^A .1 zu schreiben ist = * ,jÜj«^ = arab. ^LäJ*^
(Griechisch wird es durch t^ transcribiert ; vgl. T^ovnxvtff-
Tvipiov Sophocles Lexicon p. 537). — 98 ». Bei diesen Toi-
letgegenstiinden muss noch der Name der Seife j^^jLö
erwähnt werden. Schon die Araber wussteu, dass er fremd
ist (Mu^arrab 98). Natürlich geht er aber nicht direct auf
tätwv sapo (keltischen Ursprungs) zurück, sondern auf
dessen aramäische Aequivalente. Bemerkenswerth ist das
^JO als Anlaut; aber auch dies findet sich schon im ara-
mäischen |Js^> (Cast. 764) jüd. p3S (welches als genauere
Schreibung neben dem sonst üblichen p33 noch bei ^Arüch
s. V. f3V II erhalten ist). In der Verwandlung des griech.
lat. S in den emphatischen Laut sehe ich eine Einwirkung
des folgenden griechischen P. — HSio« ^' ZDMG. XXX«
771. Doch hat Nöldeke dort über die Echtheit kein ür-
theil abgegeben. Mir selbst ist die Ableitung aus dem
Persischen wegen des Suffixes und auch aus sachlichen
Momenten wieder fraglich geworden. — 122j,. 1. Jäküt I. —
125}}. Die Ableitung der aramäischen Wörter aus dem
Persischen ist mir doch sehr bedenkllich geworden. Der
```


## [2026-09-14T01:39:57.976Z] TOOL CALL #69: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg437-437.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/437.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/437.png",
 "description": "Archive page image"
}
```


### [2026-09-14T01:39:58.053Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 60815 Sep 13 21:39 /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/437.png
```


## [2026-09-14T01:39:59.466Z] AGENT

Now I'll write the verification file.


## [2026-09-14T01:47:25.909Z] TOOL CALL #70: Write

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/page-437.json",
 "content": "{\n  \"pdf_page\": 437,\n  \"book_page\": 407,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-13\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Seiku, Seikw\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *seykʷ- 'to pour out, spill; to flow, trickle'\",\n      \"note\": \"Pokorny 893-894 lemma 'seik\\\"-' (= seikʷ-), Meaning: 'to spill, pour, draft'; Watkins/AHD 'seikw-. To flow. [Pok. seiku- 893]'; Cheung EDIV s.v. *haič cites 'PIE *seikʷ- to pour, LIV: 523 | Pok.: 893 f.'. Nourai's double spelling Seiku / Seikw is just two ways of writing the labiovelar kʷ (his 'u' = the labial off-glide), so the entry-1 redirect 'Seikw -> Seiku' is internally consistent. One caveat that matters for the Latin branch: Pokorny sets up beside it a homophonous seikʷ- 'dry' (Av. haēcayeiti 'dries out', haēcah- 'dryness', hiku- 'dry', NP xušk) and himself unites the two ('probably via abrinnen, versiegen = austrocknen'); Latin siccus belongs to that 'dry' side. Language label (Indo-European) and gloss ('to flow') are both right.\",\n      \"note_fa\": \"ریشهٔ هندواروپایی آغازین *seykʷ- به معنی «ریختن، پاشیدن، روان شدن» است؛ پوکورنی در صفحهٔ ۸۹۳ـ۸۹۴ فرهنگ ریشه‌شناختی هندواروپایی خود آن را با همین معنا آورده و واتکینز در پیوستِ ریشه‌های هندواروپاییِ فرهنگ American Heritage نیز «seikw- to flow» ثبت کرده است. دو نگارشِ نورایی (Seiku و Seikw) تنها دو شیوهٔ نمایش همان همخوانِ لبی‌کامیِ kʷ است و از همین رو ارجاع Seikw به Seiku درست است. یادآوری مهم: پوکورنی در کنار این ریشه ریشهٔ همنامی به معنی «خشکیدن» می‌نهد (اوستایی haēcah- «خشکی»، hiku- «خشک»، فارسیِ «خشک») و خود این دو را با تحول معناییِ «فروکش‌کردن ← خشک‌شدن» یکی می‌شمارد؛ شاخهٔ لاتینیِ siccus به همین سوی «خشک» تعلق دارد. در مجموع ادعای نورایی دربارهٔ ریشه، زبان و معنا درست است.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/siccus\",\n        \"https://www.etymonline.com/word/desiccate\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:893\", \"status\": \"supports\", \"note\": \"POK_full.txt lines 72666-72730: 'Root / lemma: seik\\\"- | Meaning: to spill, pour, draft ... References: WP. II 466 f., WH. II 531, Trautmann 260. Page(s): 893-894'. Exactly Nourai's root and page.\"},\n        {\"ref\": \"OEW:340\", \"status\": \"not_checked\", \"note\": \"Shipley, The Origins of English Words, is lending-only on archive.org (refs_online.json: kind 'archive_restricted', djvu.txt returns 401/403); no local copy.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"POK\", \"where\": \"POK_full.txt l.72666-72730 (IEW pp. 893-894)\", \"stance\": \"supports\", \"note\": \"'Root / lemma: seik\\\"- Meaning: to spill, pour, draft'; and at the end 'besides eine root seik\\\"- dry ... die probably about abrinnen, versiegen = austrocknen mit seikʷ- diffuse to unite is: Avestan haecayeiti us trocknet from, haecah- dryness, hiku- dry'.\"},\n        {\"src\": \"WLD\", \"where\": \"WLD_Bd2_pages.txt l.30995-31020 (WP II 466-467, running head 'seigh seip 467')\", \"stance\": \"supports\", \"note\": \"the seiqʷ- article; 'Daneben eine Wz. seik- trocken, die wohl über abrinnen, versiegen = austrocknen mit seik- ausgießen zu vereinigen ist ... av. haecayeiti mit us trocknet aus (trans.)'.\"},\n        {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt l.912 s.v. seikw-\", \"stance\": \"supports\", \"note\": \"'seikw-. To flow. Extended expressive zero-grade form *sikko- in Latin siccus, dry (probably < \\\"flowed out\\\"): SACK3, SECCO, SICCATIVE; DESICCATE, EXSICCATE. [Pok. seiku- 893.]' — Nourai's gloss 'to flow' is verbatim Watkins.\"},\n        {\"src\": \"IEC\", \"where\": \"IEC.txt l.15364, 15366 (Mann s.v. siqu-, siqusos)\", \"stance\": \"supports\", \"note\": \"'siqu- (variant of type sik-) run dry; drain, seep. Cf. seiquo, sinquó ... Extn. of type *siquró- in Av. hixrom, n. fluid'; 'siqusos, sisquos drained, dry ... Av. hikus ... Per. xušk, id.; Lat. siccus, id.' (WP I 506, II 467).\"},\n        {\"src\": \"CHEUNG\", \"where\": \"CHEUNG.txt l.9042-9100, s.v. *haič 'to pour (out), moisten'\", \"stance\": \"supports\", \"note\": \"'«PIE *seik\\\"- to pour © LIV: 523 | Pok.: 893 f.' — the current standard Iranian-verb handbook puts the whole Iranian family under exactly this root.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"haek 2, hinčaiti, hičaiti; hixra; fra-šaĕkam\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Proto-Indo-Iranian *saić- > Proto-Iranian *haič- by the regular Iranian change of initial *s- to h- before a vowel (and *ḱ > *ć > Av. c [č]). Bartholomae AiW cols. 1737-1738 gives 'j. ¹haēk- V. \\\"giessen\\\"; Praes. 3 hica-, 9 hinca-; PPfP. °hixta-; Inf. hixtayaē-ca; Absol. °šaēkam', i.e. an athematic present hičaiti beside the nasal-infix present *si-n-kʷ-e-ti > hinčaiti — the same pair as Sanskrit sécate / siñcáti. Attestations: hincaiti Vd. 5.5 'pours water onto a field', paiti.hinčōiṯ Vd. 9.47 (ritual besprinkling with water or cow's urine), frasicinti Yt. 14.54 'they spill'. hixra- n. is Bartholomae col. 1817 'flüssiges Exkrement, flüssige Ausscheidung des Körpers' (Vd. 5.14) — a -ra- derivative of the zero grade *hik-, i.e. 'what flows out'; Nourai's gloss 'liquid increment' is a misprint-like paraphrase for 'liquid excrement/excretion'. fra-šaēkam is the absolutive (gerund) in -am of fra + haēk- 'to pour away, spill', with *s > š after the preverb fra- by the ruki rule; Cheung lists Av. haēc- '(+ *fra-) to sprinkle, pour out'. Two small caveats: (a) the book prints the absolutive with a breve, 'fra-šaĕkam', where Bartholomae and Cheung have long ē (fra-šaēkam) — the extraction is faithful to the page (see refs/ocr/BOOK/437.png); (b) the tag 'haek 2' is misleading: Bartholomae's ²haēk- is the homonym 'exarescere' (caus. haēcayaṯ 'dries out', whence haēcah- 'dryness', hiku- 'dry'), whereas all three words in this box belong to ¹haēk- 'giessen'.\",\n          \"derivation_fa\": \"صورت‌های اوستایی از ایرانی باستان *haič- می‌آیند که خود دنبالهٔ هندوایرانی *saić- و هندواروپایی *seykʷ- است؛ س آغازینِ هندوایرانی در ایرانی پیش از واکه به ه بدل شده و *ḱ به č رسیده است. بارتولومه در فرهنگ ایرانی باستان (ستون ۱۷۳۷ـ۱۷۳۸) ذیل ¹haēk- «ریختن» ستاک‌های hica- و hinca- را می‌آورد؛ hinčaiti صورتِ دارای میان‌وندِ خیشومی (*si-n-kʷ-e-ti) است در برابر hičaiti، درست همانند سنسکریت siñcáti در برابر sécate. واژهٔ hixra- (ستون ۱۸۱۷) «ترشحِ آبکیِ بدن، مادهٔ دفعیِ روان» است و مشتقِ -ra- از پایهٔ صفرِ *hik- به شمار می‌رود؛ برگردانِ نورایی («liquid increment») گویا لغزشی به‌جای «liquid excrement» است. fra-šaēkam صورتِ وجهِ وصفیِ مطلق (absolutive) از fra-haēk- «فروریختن، پاشیدن» است و ش آن حاصلِ قاعدهٔ ruki پس از پیشوندِ fra- است. دو نکتهٔ جزئی: کتاب «fra-šaĕkam» با نشانهٔ کوتاه چاپ کرده حال آنکه بارتولومه و چونگ ē کشیده دارند، و شمارهٔ «۲» در haek 2 گمراه‌کننده است زیرا در بارتولومه ²haēk- ریشهٔ «خشک‌شدن» است نه «ریختن». در کل ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%E0%A4%B8%E0%A4%BF%E0%A4%9E%E0%A5%8D%E0%A4%9A%E0%A4%A4%E0%A4%BF\"],\n          \"ref_check\": [\n            {\"ref\": \"POK:893\", \"status\": \"supports\", \"note\": \"POK_full.txt l.72674: 'Avestan haek-, hincaiti (hicaiti) \\\"giesst from\\\", fra-saekam absolutely \\\"beim Vergiessen\\\", hixra- n. \\\"flüssiges Exkrement\\\"' — all three of Nourai's words, on the very page he cites.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"BRT.txt l.28658 + l.30048 (AiW cols. 1737-1738, 1817)\", \"stance\": \"supports\", \"note\": \"'j. ¹haēk- V. \\\"giessen\\\". Praes. 3 hica-, 9 hinca-. — PPfP. °hixta-; Inf. hixtayaē-ca; Absol. °šaēkam'; and 'j. hixra- n. \\\"flüssiges Exkrement, flüssige Ausscheidung des Körpers\\\" ... V. 5. 14'. The etymology line adds 'ai. siñcati, asicat ... np. pasanjīdan (dazu Hbn. PSt. 43)'.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"CHEUNG.txt l.9042-9055, EDIV s.v. *haič\", \"stance\": \"supports\", \"note\": \"'*haič \\\"to pour (out), moisten\\\". AVESTAN: Y Av. haēc- \\\"to pour (out); to irrigate\\\" || (+ *pati-) \\\"to besprinkle\\\" || (+ *para-) || (+ *fra-) \\\"to sprinkle, pour out\\\". Pres. n-: IND. 3sg. YAv. hincaiti (V 5.5) ... 3pl. YAv. frasicinti (Yt 14.54)'.\"},\n            {\"src\": \"POK\", \"where\": \"POK_full.txt l.72674 (IEW 893)\", \"stance\": \"supports\", \"note\": \"see ref_check; Pokorny lists haek-, hincaiti/hicaiti, fra-saekam and hixra- together under seikʷ-.\"},\n            {\"src\": \"IEC\", \"where\": \"IEC.txt l.15364 (Mann s.v. siqu-)\", \"stance\": \"supports\", \"note\": \"'Extn. of type *siquró- in Av. hixrom, n. \\\"fluid\\\"' — independent confirmation of hixra- and its formation.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"pašanjîdan «پشنجیدن»\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The word and the ultimate root are right, but the parent form drawn in the chart is not. NP پشنجیدن pašanjīdan 'to sprinkle (water etc.)' continues Middle Persian passinj- (Book Pahlavi psnc-, 3sg. psncyt /passinjēd/, past participle pshtk /passixtag/), from Old Iranian *pati-hinč- — the *pati- prefixed stem of the same verb, not the *fra- stem. Hübschmann, Persische Studien 42/191, states it explicitly: 'pasanjīdan \\\"besprengt werden\\\" aus *pat-sinč-ītan', and 'phl. *pat-sincat = np. pasanjad'; Cheung EDIV s.v. *haič likewise lists '(+ *pati-) NP pišanjīdan \\\"to sprinkle\\\", Khorasani pšing'. Phonetically *pati-sinč- > MP *pat-sinj- > pas-sinj- (assimilation of -ts- to -ss-, then simplification) > NP pašanj-, with the infinitive suffix -īdan; the present stem پشنج pašanj is still Mo'in's lemma. The attached nouns پشنگ pašang / پشنگه pašange 'splash, sprinkled water' are deverbal from the same stem (pašanj ~ pašang with -nj/-ng alternation). Nourai's own chart makes the pointer (☞Per 1) hang off fra-šaēkam, which would give a **fra-** prefix; the sources are unanimous for **pati-**. The Labībī couplet in the box ('به خنجر همه تنش انجیده‌اند / بر آن خاک و خونش پشنجیده‌اند') is genuine — it stands in Borhan-e Qāṭeʿ's notes citing Loghatnāme.\",\n          \"derivation_fa\": \"واژه و ریشهٔ نهایی درست است، اما پیشوندِ صورتِ مادر در نمودار نادرست نشان داده شده. «پشنجیدن» (پاشیدن آب) دنبالهٔ فارسی میانهٔ passinj- (پهلویِ کتابی psnc-، سوم‌شخصِ مضارع psncyt، صفت مفعولی pshtk /passixtag/) است و آن از ایرانی باستانِ *pati-hinč-، یعنی ستاکِ همین فعل با پیشوندِ pati-، نه fra-. هوبشمان در «پژوهش‌های فارسی» (ص ۴۲ و ۱۹۱) صریحاً می‌نویسد: «pasanjīdan از *pat-sinč-ītan» و «pahl. *pat-sincat = np. pasanjad»؛ چونگ نیز در فرهنگِ فعل‌های ایرانی ذیل *haič می‌آورد «(+ *pati-) NP pišanjīdan». از نظر آوایی *pati-sinč- در فارسی میانه به *pat-sinj- و سپس با همگونیِ ts به ss و ساده‌شدنِ آن به pašanj رسیده و با پسوندِ مصدریِ -یدن «پشنجیدن» ساخته شده است؛ اسم‌های «پشنگ» و «پشنگه» نیز از همین ستاک‌اند. معین در فرهنگ فارسی «پشنجیدن [= شنجیدن] (مص‌م.) آب و امثال آن پاشیدن، پشنگ کردن» و «پشنگ: افشاندن آب، آب مترشح» را آورده است. چون نورایی نشانهٔ ارجاع را به fra-šaēkam چسبانده، ادعای او با احتیاط پذیرفتنی است: ریشه درست، ولی پیشوند باید pati- باشد.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D9%BE%D8%B4%D9%86%D8%AC%DB%8C%D8%AF%D9%86\"],\n          \"ref_check\": [\n            {\"ref\": \"MON:799\", \"status\": \"supports\", \"note\": \"MON_part1.txt l.32177-32184: 'پش‌نجیدن [= شنجیدن] (مص‌م.) آب و امثال آن پاشیدن، گل نم کردن، پشنگ کردن' and the next lemma 'پشنگ [= پشنج ~ پشنگ] (ا.) افشاندن آب، آب مترشح: یک پشنگ آب'. Word, meaning and the script_extra پشنگ/پشنگه all confirmed; Mo'in gives no etymology, so it supports the Persian data, not the arrow.\"},\n            {\"ref\": \"AEF:391\", \"status\": \"not_checked\", \"note\": \"Khaleqi Motlaq's Asās-e Eštteqāq-e Fārsi (the Persian translation of Horn+Hübschmann) is not online (refs_online.json: 'Not online … only bookshop listings'). Checked its German original instead: Hübschmann PSt 42/191 (see consulted), which is the source AEF translates.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HUB\", \"where\": \"HUB.txt l.1434, 4464, 4787, index l.10642 (Persische Studien pp. 42, 191)\", \"stance\": \"partial\", \"note\": \"'pasanjidan \\\"besprengt werden\\\" aus *pat-sinč-ītan zu skr. …' and 'phl. *pat-sincat = np. pasanjad'. Same verbal root as the chart, but Hübschmann's prefix is pati-, not fra-.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"CHEUNG.txt l.9066-9082, EDIV s.v. *haič\", \"stance\": \"partial\", \"note\": \"'MIDDLE PERSIAN: … (+ *pati-) BMP psnc- /passinj-/ \\\"to sprinkle\\\" … Pres.: IND. 3sg. BMP psncyt /passinjēd/; Partic.: perf. pass. BMP pshtk /passixtag/' and 'NWIR: … (+ *pati-) NP pišanjidan \\\"to sprinkle\\\", Khor. pšing'. Confirms the descent, corrects the prefix.\"},\n            {\"src\": \"BRT\", \"where\": \"BRT.txt l.28658 (AiW col. 1738, etymology line of ¹haēk-)\", \"stance\": \"supports\", \"note\": \"'ai. siñcati, asicat … np. pasanjīdan (dazu Hbn. PSt. 43)' — Bartholomae himself files NP pasanjīdan under this Avestan root.\"},\n            {\"src\": \"MON\", \"where\": \"MON_part1.txt l.32177-32184\", \"stance\": \"supports\", \"note\": \"see ref_check: lemma and glosses as in the chart.\"},\n            {\"src\": \"BQT\", \"where\": \"BQT_v1_pages.txt l.26057\", \"stance\": \"partial\", \"note\": \"'بر آن خاک و خونش پشنجیده‌اند . لبیبی. «لغت‌نامه»' — the Labībī verse of Nourai's box is genuine, quoted in Borhan's apparatus from Dehkhoda; Borhan has no etymology for it.\"},\n            {\"src\": \"HRN\", \"where\": \"HRN.txt, grep 'pasanj|pašanj'\", \"stance\": \"silent\", \"note\": \"no hit; Horn's Grundriss has no separate number for pasanjīdan (Hübschmann's Persische Studien covers it instead).\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Sogdian\",\n          \"words\": \"pšync\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Christian Sogdian pšync- /pəšinč-/ 'to sprinkle, pour', written pšync in Syriac script, is the *pati-prefixed present of the same Iranian verb *haič- < PIE *seykʷ-: *pati-hinč- > Sogd. pšinč-, the *pati- preverb reduced to p(ə)- as regularly in Sogdian. It stands in the same formal relation to Avestan hinčaiti as MP passinj- does, and the derived agent noun pšyncn' 'sprinkler, o spiller!' (STii 6.10) shows the stem was productive. So Nourai's arrow root → Sogdian is right; strictly the Sogdian form, like the Persian one, carries the pati- preverb that the chart does not show.\",\n          \"derivation_fa\": \"صورتِ سغدیِ مسیحی pšync- «پاشیدن، ریختن» ستاکِ مضارعِ همین فعلِ ایرانیِ *haič- (از هندواروپاییِ *seykʷ-) است با پیشوندِ *pati-: یعنی *pati-hinč- که در سغدی به pšinč- رسیده و پیشوندِ pati- طبق قاعده به p- کوتاه شده است. این صورت دقیقاً هم‌ساختِ فارسی میانهٔ passinj- و اوستاییِ hinčaiti است و اسم فاعلِ pšyncn' «پاشنده» نیز از همان ستاک است. قریب در فرهنگ سغدی (مدخل ۷۵۳۷، ص ۳۰۳) خودِ اوستاییِ hincati را به‌عنوان هم‌ریشه یاد می‌کند. ادعای نورایی درست است، فقط پیشوندِ pati- در نمودار نیامده است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"SOD:303\", \"status\": \"supports\", \"note\": \"SOD_pages.txt \\\\f-block 370 (0-based leaf 369; printed page = leaf − 66 = 303, exactly Nourai's citation): '7537 psync- C | pasēnč ©Shaek; Av. hincati *p\\\\'s\\\\'ync- | (to)sprinkle, (to)pour | GMS 600; BBB 531; BSTi 318; C2, 11V19; Bailey, Prolexis 417; AVS 123'. Gharib gives both the gloss and the Avestan connection Nourai draws.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"SOD\", \"where\": \"SOD_pages.txt leaf 369 = printed p. 303, entry 7537 (and 7538 psyncn 'sprinkler')\", \"stance\": \"supports\", \"note\": \"see ref_check; entry 7538 'psyncn C | pascncan ©voc. | sprinkler | STii 6.10'.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"CHEUNG.txt l.9075-9078, EDIV s.v. *haič\", \"stance\": \"supports\", \"note\": \"'SOGDIAN: (+ *ā-) MSogd. \\\\'\\\\'šync \\\"to pour\\\" (-š- from *pati-formation) || (+ *pati-) CSogd. pšync- \\\"to pour\\\"' — the preverb is *pati-.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Latin\",\n          \"words\": \"siccus\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Latin siccus 'dry' is traditionally an expressive geminated zero grade *sik-ko- of this root, the semantics being 'having flowed out, drained' > 'dry'; Watkins states it exactly as Nourai does: 'seikw-. To flow. Extended expressive zero-grade form *sikko- in Latin siccus, dry (probably < \\\"flowed out\\\")'. Klein s.v. siccative adds the Iranian comparanda: siccus 'is cogn. with Avestic hiku-, \\\"dry\\\", Gk. ἰσχνός, \\\"dry, withered\\\", … Mir. sesc, \\\"dry\\\"'. Mann (IEC) sets up siqusos, sisquos 'drained, dry' with Av. hikuš/huško, Oss. xusk, Pers. xušk, Lat. siccus. So on the received (Pokorny/Walde-Pokorny/Watkins/Klein) view the node is right, and Nourai's gloss 'flowed out, dry' is Watkins' own wording. The caveat: this branch is really Pokorny's secondary root seikʷ- 'dry', which he only 'probably' unites with seikʷ- 'pour'; and current Latin etymology (de Vaan, followed by Wiktionary) reconstructs *sisk(ʷ)os / *siskus 'dry' beside Proto-Celtic *siskʷos and Gk. ἰσχνός and files it under a root 'to dry up', noting 'the phonetic details are unclear'. Hence plausible rather than confirmed: the word, the language and the meaning are right, but the direct arrow from a root glossed 'to flow' is a simplification of a still-contested question.\",\n          \"derivation_fa\": \"لاتینیِ siccus «خشک» بنا بر دیدگاهِ سنتی از پایهٔ صفرِ مضاعف‌شدهٔ *sik-ko- همین ریشه است و تحول معنایی‌اش «آبْ‌رفته، تهی‌شده» ← «خشک» بوده؛ واتکینز عیناً می‌نویسد «seikw- to flow … *sikko- in Latin siccus, dry (probably < flowed out)» و کلاین نیز siccus را هم‌ریشهٔ اوستاییِ hiku- «خشک» و یونانیِ ἰσχνός می‌داند، و مان (فرهنگ تطبیقی هندواروپایی) آن را با اوستاییِ huško و فارسیِ «خشک» در یک مدخل می‌آورد. با این حال باید توجه داشت که این شاخه در حقیقت به ریشهٔ دومِ پوکورنی یعنی seikʷ- «خشکیدن» تعلق دارد که پوکورنی خود تنها «احتمالاً» آن را با seikʷ- «ریختن» یکی می‌شمارد، و ریشه‌شناسیِ امروزیِ لاتین (دِ فان، و به پیروی او ویکی‌واژه) صورتِ *sisk(ʷ)os را بازسازی می‌کند و می‌گوید جزئیاتِ آوایی روشن نیست. بنابراین ادعای نورایی با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/siccus\",\n            \"https://www.etymonline.com/word/desiccate\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt l.912 s.v. seikw-: 'Extended expressive zero-grade form *sikko- in Latin siccus, dry (probably < \\\"flowed out\\\")'. Nourai's gloss 'flowed out, dry' is copied from here.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"POK_full.txt l.72691 (IEW 893)\", \"stance\": \"supports\", \"note\": \"under seikʷ-: 'Latin siat \\\"oupɛȋ\\\" … siccus \\\"dry\\\"'.\"},\n            {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt l.912; index l.1487, 2230, 2254\", \"stance\": \"supports\", \"note\": \"SICCATIVE, SECCO, EXSICCATE, DESICCATE, SACK3 all indexed to seikw-.\"},\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt l.35121 s.v. siccative\", \"stance\": \"supports\", \"note\": \"'L. siccus, \\\"dry\\\", which is cogn. with Avestic hiku-, \\\"dry\\\", Gk ἰσχνός, \\\"dry, withered\\\", Lith. seklus … Mir. sesc, \\\"dry\\\", and with OI. siheati [= śiṣyati] \\\"makes dry\\\"'.\"},\n            {\"src\": \"IEC\", \"where\": \"IEC.txt l.15366 (Mann s.v. siqusos)\", \"stance\": \"partial\", \"note\": \"'siqusos, sisquos \\\"drained, dry\\\". WP I, 506 and II, 467. Av. hikus, hiskus, huško … Per. xušk, id.; Lat. siccus, id.' — Mann keeps the 'dry' set as its own lemma rather than deriving it straight from the 'pour' root.\"},\n            {\"src\": \"WLD\", \"where\": \"WLD_Bd2_pages.txt l.31013-31015 (WP II 467)\", \"stance\": \"partial\", \"note\": \"'Daneben eine Wz. seik- \\\"trocken\\\", die wohl über \\\"abrinnen, versiegen = austrocknen\\\" mit seik- \\\"ausgießen\\\" zu vereinigen ist' — the union is expressly a 'wohl'.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"French\",\n          \"words\": \"sec\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Latin siccus > Vulgar Latin *siccu > Old French sec (fem. seche/sèche), by the regular loss of the final syllable and of the geminate: /sikkus/ > /sek/. Attested in Old French from the 11th-12th c. and in the wine sense ('unsweetened, not sweet') from the later Middle Ages, whence vin sec. Wiktionary: 'Inherited from Old French sec, from Latin siccus (\\\"dry\\\"), from Proto-Indo-European *seyk-'; Klein s.v. seck 'F. sec, \\\"dry\\\", fr. L. siccus'. Nourai's gloss 'without water' is a loose but not wrong rendering of the oenological sense that feeds the two child nodes.\",\n          \"derivation_fa\": \"فرانسویِ sec دنبالهٔ طبیعیِ لاتینیِ siccus است: در لاتینِ عامیانه *siccu، سپس با افتادنِ هجای پایانی و ساده‌شدنِ همخوانِ مشدد به /sek/ فرانسویِ کهن رسیده و از فرانسویِ کهن به فرانسویِ نو به ارث رسیده است. معنای آن «خشک» است و در زبانِ می‌شناسی «بی‌شیرینی، بدونِ قند» — همان معنایی که نورایی «بی‌آب» ترجمه کرده و همان است که در دو گرهِ فرزند (سکِ فارسی و sack انگلیسی) به‌کار آمده. ویکی‌واژه و کلاین هر دو همین زنجیره را تأیید می‌کنند. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/sec\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD:1141\", \"status\": \"partial\", \"note\": \"The 1975 New College Edition p. 1141 is the dictionary body (the 'sec/sack' page), not the IE appendix, and is lending-only; the appendix entry seikw- (AHD_watkins1985.txt l.912) does list SACK3 and SECCO under this root, which is the substance of Nourai's claim.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt l.34370 s.v. seck\", \"stance\": \"supports\", \"note\": \"'seck, adj., dry, barren, unprofitable. — F. sec, \\\"dry\\\", fr. L. siccus. See siccative and cp. sack, \\\"strong wine\\\", sec, secco.'\"},\n            {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt l.912 and index l.2230 (SECCO seikw-)\", \"stance\": \"supports\", \"note\": \"Romance sec/secco filed under seikw- via siccus.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Persian\",\n          \"words\": \"sek «سک»\",\n          \"verdict\": \"unverified\",\n          \"derivation\": \"Modern colloquial Persian «سِک» in «سِک خوردن» = to drink spirits neat, undiluted, is real in speech, and the usual folk account is exactly Nourai's — a 20th-c. loan of French sec 'dry (of wine/spirits)' taken over during the Qajar-to-Pahlavi period when French was the channel for European vocabulary in Iran. But no lexicographic source I could reach records it: Dehkhoda, Moʿin and Amid (via abadis.ir) give for سک only 'a pointed stick for driving cattle', 'vinegar' and a myrobalan electuary; fa.wiktionary gives the same two senses with no etymology; Moʿin's printed lexicon (MON_part1/part2) and Aryanpur's IE-roots dictionary have nothing for the drink sense; Borhan-e Qateʿ's سک entries are unrelated. Nourai's single authority, Moshiri's Farhang-e Vāžehā-ye Orupāyi dar Fārsi (VOP), has no scan or online text anywhere (refs_online.json: kind 'none'). Compounding the doubt, Persian speakers themselves dispute the link (one widely-read thread argues Persian سِک and French sec are faux amis). I therefore cannot confirm or refute the arrow; the semantic and chronological fit is good, the documentation is absent.\",\n          \"derivation_fa\": \"«سِک» در ترکیبِ گفتاریِ «سِک خوردن» (نوشیدنِ مشروبِ خالص و بی‌آب) در فارسیِ امروز به‌کار می‌رود و روایتِ رایج همان است که نورایی می‌گوید: وام‌واژه‌ای از فرانسویِ sec «خشک، بی‌شیرینی» از دورهٔ نفوذِ زبان فرانسه در ایران. اما هیچ فرهنگِ در دسترسی این معنا یا این ریشه را ثبت نکرده است: دهخدا، معین و عمید ذیل «سک» تنها «چوبِ نوک‌تیزِ راندنِ چارپایان»، «سرکه» و معجونی از هلیله را می‌آورند؛ ویکی‌واژهٔ فارسی نیز همان دو معنا را بدونِ ریشه‌شناسی دارد؛ در متنِ فرهنگِ معین و در فرهنگِ ریشه‌هایِ آریان‌پور چیزی نیست و برهان قاطع هم مدخلِ بی‌ربط دارد. تنها مأخذِ نورایی، «فرهنگ واژه‌های اروپایی در فارسی» مشیری، نه نسخهٔ اسکن‌شده دارد و نه متنِ برخط. افزون بر این، خودِ فارسی‌زبانان بر سرِ این پیوند اختلاف دارند و برخی «سِک» فارسی و sec فرانسوی را «دوستانِ دروغین» می‌دانند. بنابراین این گره تأییدنشده می‌ماند: نه می‌توان آن را پذیرفت و نه رد کرد.\",\n          \"sources\": [\n            \"https://abadis.ir/fatofa/%D8%B3%DA%A9/\",\n            \"https://fa.wiktionary.org/wiki/%D8%B3%DA%A9\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"VOP:213\", \"status\": \"not_checked\", \"note\": \"Moshiri, Farhang-e Vāžehā-ye Orupāyi dar Fārsi (Alborz 1371): refs_online.json records kind 'none' — 'Searched archive.org, ketabnak, noorlib, web: not found'. Re-checked 2026-09: still no copy; Nourai's only support for this node is unreadable.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"abadis.ir/fatofa/سک (فرهنگ معین section) and MON_part1.txt/MON_part2.txt\", \"stance\": \"silent\", \"note\": \"Moʿin's سک is 'چوبی نوک تیز که با آن چارپایان را برانند' and 'سرکه'; no drink sense, no French tag.\"},\n            {\"src\": \"BQT\", \"where\": \"BQT_v2_pages.txt l.889, 11107, 11937, 16324 (grep 'سک ')\", \"stance\": \"silent\", \"note\": \"all hits are unrelated words (سک انگور, خایهٔ سگ آبی, etc.); Borhan has no سک 'undiluted drink'.\"},\n            {\"src\": \"ARY\", \"where\": \"incoming/ARY/ARY_pages.txt and ARY_latin_index_pages.txt (grep 'سِک', 'SEC', 'SICCUS')\", \"stance\": \"silent\", \"note\": \"no hits; Aryanpur's IE-roots dictionary does not treat this word.\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"English\",\n          \"words\": \"sack\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English sack 'a strong, light-coloured wine from Spain and the Canaries' (Shakespeare's Falstaff's drink) is first recorded in the 1530s as wyne seck, i.e. a borrowing of French (vin) sec 'dry wine'; the later spelling sack with -a- is irregular ('not a normal development from the original seck', OED via Etymonline) and probably owes something to the unrelated homophone sack 'bag'. Klein: 'sack, n., strong wine. — Formerly spelled seck, fr. F. (vin) sec, \\\"dry wine\\\", fr. L. siccus, \\\"dry\\\". See siccative.' Watkins indexes SACK3 to seikw-. This is entirely uncontroversial and matches Nourai's arrow French → English exactly.\",\n          \"derivation_fa\": \"واژهٔ انگلیسیِ sack به معنی «شرابِ نیرومندِ روشن‌رنگِ اسپانیایی» نخستین بار در دههٔ ۱۵۳۰ به صورتِ wyne seck ثبت شده، یعنی وام‌گیریِ فرانسویِ (vin) sec «شرابِ خشک». نگارشِ بعدیِ sack با a قاعده‌مند نیست و احتمالاً زیرِ تأثیرِ هم‌آواییِ آن با sack «کیسه» پدید آمده است. کلاین نیز می‌نویسد «sack … formerly spelled seck, fr. F. (vin) sec, fr. L. siccus» و واتکینز SACK3 را ذیلِ ریشهٔ seikw- فهرست کرده است. پیکانِ نورایی (فرانسوی ← انگلیسی) کاملاً درست است.\",\n          \"sources\": [\"https://www.etymonline.com/word/sack\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD:1141\", \"status\": \"partial\", \"note\": \"p. 1141 of the 1975 New College Edition body is lending-only; the same dictionary's IE appendix (AHD_watkins1985.txt l.2207) indexes 'SACK? = seikw-', confirming the claim.\"},\n            {\"ref\": \"OEW:346\", \"status\": \"not_checked\", \"note\": \"Shipley is lending-only on archive.org; no local copy (refs_online.json).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt l.33445 s.v. sack ('strong wine')\", \"stance\": \"supports\", \"note\": \"'Formerly spelled seck, fr. F. (vin) sec, \\\"dry wine\\\", fr. L. siccus, \\\"dry\\\".'\"},\n            {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt l.2207 (index) and l.912 (seikw-)\", \"stance\": \"supports\", \"note\": \"'SACK? = seikw-'; the root article lists SACK3 among its English descendants.\"}\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"English\",\n          \"words\": \"desiccate\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"A learned Latinism: Latin dēsiccāre 'to dry thoroughly' (dē- intensive + siccāre 'to dry', denominative of siccus), past participle dēsiccātus, taken into English in the 1570s as desiccate, with the intransitive sense 'become dry' from the 1670s. Etymonline: 'desiccate … 1570s, from Latin desiccare \\\"to make very dry\\\", from de- \\\"thoroughly\\\" + siccare \\\"to dry\\\" … from PIE root *seikw- \\\"to flow out\\\"'. Watkins indexes DESICCATE and EXSICCATE to seikw-. Nourai's arrow (Latin siccus → English desiccate, bypassing the intermediate verb) is a compression but not an error.\",\n          \"derivation_fa\": \"واژهٔ انگلیسیِ desiccate وام‌واژه‌ای کتابی از لاتین است: dēsiccāre «به‌کلی خشکاندن» از پیشوندِ تأکیدیِ dē- و فعلِ siccāre «خشکاندن» که خود از صفتِ siccus ساخته شده؛ صفتِ مفعولیِ dēsiccātus در دههٔ ۱۵۷۰ به انگلیسی راه یافته و معنای لازمِ «خشک شدن» از دههٔ ۱۶۷۰ پیدا شده است. اتیمآنلاین همین زنجیره را با ارجاع به ریشهٔ *seikw- «بیرون ریختن» می‌آورد و واتکینز نیز DESICCATE و EXSICCATE را ذیلِ همین ریشه فهرست کرده است. پیکانِ نورایی (siccus ← desiccate) فشرده است ولی نادرست نیست.\",\n          \"sources\": [\"https://www.etymonline.com/word/desiccate\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt l.912 s.v. seikw-: '… SACK3, SECCO, SICCATIVE; DESICCATE, EXSICCATE'; index l.1420 'DESICCATE selkw- [= seikw-]'.\"},\n            {\"ref\": \"OEW\", \"status\": \"not_checked\", \"note\": \"Shipley lending-only; no local copy.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt l.912, index l.1420 and l.1487 (EXSICCATE seikw-)\", \"stance\": \"supports\", \"note\": \"see ref_check.\"},\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt l.35121 s.v. siccative\", \"stance\": \"supports\", \"note\": \"'Late L. siccativus … fr. L. siccatus, pp. of siccare, \\\"to dry\\\", fr. siccus, \\\"dry\\\" … Cp. desiccate, exsiccate, hortus siccus, sack, \\\"strong wine\\\", sec, secco.'\"}\n          ]\n        },\n        {\n          \"id\": 9,\n          \"lang\": \"Sanskrit\",\n          \"words\": \"sincati\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Sanskrit siñcáti (सिञ्चति) 'pours out, sprinkles, moistens', class-6 present of the root sic- (सिच्), attested from the Ṛgveda (e.g. RV 10.21.3). Formally it is the nasal-infix present *si-n-kʷ-é-ti of PIE *seykʷ-, exactly parallel to Avestan hinčaiti, beside the thematic sécate 'pours'; Indo-Iranian *ć from PIE *kʷ before a front vowel gives Skt. c and Av. c. Pokorny p. 893 opens the material with 'Old Indic secate, sincati (asicat) \\\"giesst from\\\", seka- m. \\\"downpour\\\"'; Cheung's IE-cognate line for *haič gives 'SANSKRIT: sec \\\"to pour (out)\\\" (RV+)'. Nourai's transliteration drops the palatal diacritic (siñcati) and his gloss 'flows from' renders Pokorny's German 'giesst aus' a little loosely — the verb is transitive 'pours out'.\",\n          \"derivation_fa\": \"سنسکریتِ siñcáti «می‌ریزد، می‌پاشد، تر می‌کند» صورتِ مضارعِ طبقهٔ ششمِ ریشهٔ sic- است و از ریگ‌ودا (۱۰٫۲۱٫۳) به بعد گواهی دارد. از نظر ساخت، این همان مضارعِ دارای میان‌وندِ خیشومیِ *si-n-kʷ-é-ti از ریشهٔ هندواروپاییِ *seykʷ- است و دقیقاً هم‌ساختِ اوستاییِ hinčaiti؛ در کنارِ آن صورتِ sécate نیز هست. پوکورنی در ص ۸۹۳ ماده را با «Old Indic secate, sincati (asicat) giesst aus» آغاز می‌کند و چونگ نیز ذیلِ *haič می‌آورد «SANSKRIT: sec \\\"to pour (out)\\\" (RV+)». نورایی نشانهٔ کامیِ ñ را ننوشته و معنا را «flows from» آورده، حال آنکه فعل گذراست («می‌ریزد»). در کل ادعا درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%E0%A4%B8%E0%A4%BF%E0%A4%9E%E0%A5%8D%E0%A4%9A%E0%A4%A4%E0%A4%BF\"],\n          \"ref_check\": [\n            {\"ref\": \"POK:893\", \"status\": \"supports\", \"note\": \"POK_full.txt l.72672: 'Material: Old Indic secate, sincati (asicat) \\\"giesst from, begiesst\\\", seka- m. \\\"downpour, Erguss, Besprengung\\\", praseka- m.' — Nourai's word on his cited page.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"POK_full.txt l.72672 (IEW 893)\", \"stance\": \"supports\", \"note\": \"see ref_check.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"CHEUNG.txt l.9098-9100, EDIV s.v. *haič\", \"stance\": \"supports\", \"note\": \"'*SANSKRIT: sec \\\"to pour (out)\\\" (RV+) = EWAia II: 744' with '«PIE *seik\\\"- to pour © LIV: 523 | Pok.: 893 f.'\"},\n            {\"src\": \"IEC\", \"where\": \"IEC.txt l.16638 (Mann s.v. soik-)\", \"stance\": \"supports\", \"note\": \"'Skt. cf. sekah, m. \\\"outpour; libation\\\"; sektram, n. \\\"ladle\\\"' — the same Sanskrit family under the o-grade.\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 2,\n      \"root\": \"Seip\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *seyp- / *seyb- 'to pour out, drip, trickle; to sift'\",\n      \"note\": \"Pokorny 894: 'Root / lemma: seip-, seib- | Meaning: to pour, rain, sift, *sieve, stream, trickle, dribble … References: WP. II 467 f., WH. II 478, 504 … Page(s): 894' — Nourai's root name, language label, gloss and page are all right. Watkins prints the lemma as seib- 'To pour out, sieve, drip, trickle. [Pok. seip- 894.]'. Pokorny also notes that seip- and seikʷ- (the previous entry on this page of Nourai's book) probably both rest on a simple *sei- 'drip, trickle', which is why the two charts sit side by side. Note for the whole entry: the word for 'soap' is a Germanic creation (*saipǭ, originally a reddish hair-dye/pomade of the Germanic warriors, Pliny NH 28.191 'Gallorum … inventum'), and every non-Germanic form in the chart — Latin, Greek, Aramaic, Arabic, Persian — is a borrowing from it, so the left-hand chain should hang from the Germanic box, not directly from the root.\",\n      \"note_fa\": \"ریشهٔ هندواروپایی آغازینِ *seyp-/*seyb- «ریختن، چکیدن، صاف کردن» در پوکورنی ص ۸۹۴ با همین معنا آمده است («seip-, seib-: to pour, rain, sift, stream, trickle») و واتکینز آن را به صورت seib- ثبت کرده؛ نام، زبان، معنا و شمارهٔ صفحهٔ نورایی همگی درست است. پوکورنی می‌افزاید که seip- و seikʷ- هر دو احتمالاً بر پایهٔ *sei- «چکیدن» استوارند و به همین سبب این دو نمودار در کتاب کنار هم آمده‌اند. نکتهٔ مهمِ کل این مدخل: واژهٔ «صابون» ساختهٔ ژرمنی است (*saipǭ، که در آغاز نوعی رنگِ مو و چربیِ سرخ‌فامِ جنگاورانِ ژرمن بود و پلینیوس آن را اختراعِ گل‌ها/ژرمن‌ها می‌خواند) و همهٔ صورت‌های غیرِژرمنیِ نمودار — لاتینی، یونانی، آرامی، عربی و فارسی — وام‌واژه‌اند؛ از این رو زنجیرهٔ سمتِ چپ باید از جعبهٔ «ژرمنی» آویخته شود نه مستقیماً از ریشه.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/%D8%B5%D8%A7%D8%A8%D9%88%D9%86\",\n        \"https://en.wiktionary.org/wiki/%CF%83%CE%AC%CF%80%CF%89%CE%BD\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:894\", \"status\": \"supports\", \"note\": \"POK_full.txt l.72732-72760: 'Root / lemma: seip-, seib- | Meaning: to pour, rain, sift, *sieve, stream, trickle, dribble … Page(s): 894'.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"POK\", \"where\": \"POK_full.txt l.72732-72760 (IEW 894)\", \"stance\": \"supports\", \"note\": \"see ref_check; the article lists OHG sib, OE sife 'sieve', OE sīpian 'drip', Germanic *saip(i)ō, 'Latin sāpō (Germanic loanword)', Toch. A sip-/sep- 'anoint'.\"},\n        {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt l.912 s.v. seib-\", \"stance\": \"supports\", \"note\": \"'seib-. To pour out, sieve, drip, trickle. 1. Basic form in Germanic *sipōn in Old English sipian … SEEP. 2. Suffixed o-grade form *soib-on- in Germanic *saipōn-, \\\"dripping thing\\\", resin … SOAP … Latin sāpō, soap … 3. Variant Germanic form *sib- … SIEVE … SIFT. [Pok. seip- 894.]'\"},\n        {\"src\": \"WLD\", \"where\": \"WLD_Bd2_pages.txt l.31055-31090 (WP II 467-468)\", \"stance\": \"supports\", \"note\": \"the seip- article: 'hieher auch der germ. Name der Seife: ahd. seifa, seiffa, seipfa \\\"Seife, auch Harz\\\", mnd. sepe, ags. sāpe … vgl. Vf. LEWb. u. sapo (germ. Lw.)'.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Latin\",\n          \"words\": \"sâpô\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Latin sāpō, gen. sapōnis 'soap' is real and its ultimate root is indeed *seip-/*seib-, but it is NOT an inherited Latin word: every authority Nourai could have used says it is a loan from Germanic. Pokorny, on the very page cited (894), writes 'Germanic *saip(i)ō: … Old High German sei(p)fa \\\"soap\\\", also \\\"resin\\\", Middle Low German sēpe, Old English sāpe … Latin sāpō (Germanic loanword)'; Watkins files it as 'Suffixed o-grade form *soib-on- in Germanic *saipōn- … b. Latin sāpō, soap'; Klein s.v. saponaceous: 'L. sapo, gen. saponis, \\\"soap\\\", which is a Teut. loan word'; Walde-Pokorny II 468 refers to Walde's own Latin dictionary 's.v. sapo (germ. Lw.)'. The word enters Latin in the 1st c. CE — Pliny, NH 28.191, describes sāpō as a Gaulish/Germanic invention, a pomade of tallow and ash used to redden the hair, which is exactly the semantic starting point ('dripping fat/resin'). So the node is downgraded to plausible: right root, right word, but the chart's arrow should run root → Germanic → Latin, and Nourai even draws a Germanic box in the same chart without connecting it to the Latin one.\",\n          \"derivation_fa\": \"لاتینیِ sāpō (حالتِ اضافی sapōnis) «صابون» واژه‌ای واقعی است و سرانجام به همین ریشه بازمی‌گردد، اما واژه‌ای ارثی در لاتین نیست، بلکه وام‌واژه‌ای از ژرمنی است. پوکورنی در همان صفحهٔ ۸۹۴ که نورایی ارجاع داده می‌نویسد: «germ. *saip(i)ō: آلمانیِ علیای کهن sei(p)fa \\\"صابون، و نیز صمغ\\\"، ساکسونیِ میانه sēpe، انگلیسیِ کهن sāpe … لاتینی sāpō (وام‌واژهٔ ژرمنی)». واتکینز نیز آن را ذیلِ «*soib-on- در ژرمنیِ *saipōn-» می‌آورد و کلاین می‌گوید «L. sapo … which is a Teut. loan word». این واژه در سدهٔ یکم میلادی وارد لاتین شده؛ پلینیوس (تاریخ طبیعی ۲۸٫۱۹۱) sāpō را ساختهٔ گل‌ها/ژرمن‌ها و آمیزه‌ای از پیه و خاکستر برای سرخ‌کردنِ مو می‌داند — همان معنای آغازینِ «چربیِ چکنده». بنابراین ادعای نورایی با احتیاط پذیرفتنی است: ریشه درست است اما پیکان باید ریشه ← ژرمنی ← لاتینی باشد، و جالب آنکه نورایی خودْ جعبهٔ «ژرمنی» را در همین نمودار دارد ولی آن را به لاتینی وصل نکرده است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%CF%83%CE%AC%CF%80%CF%89%CE%BD\"],\n          \"ref_check\": [\n            {\"ref\": \"POK:894\", \"status\": \"partial\", \"note\": \"POK_full.txt l.72748-72750: 'here also the Germanic name the Seife: Germanic *saip(i)ō: … Old High German sei(p)fa \\\"soap\\\"; also \\\"resin\\\", Middle Low German sepe \\\"soap\\\", Old English sape f. (out of it nord. sapa) \\\"soap\\\", Latin sāpō (Germanic loanword)'. Pokorny has the word on the cited page, but explicitly as a Germanic loan, not a Latin inheritance.\"},\n            {\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"AHD_watkins1985.txt l.912 s.v. seib-: '2. Suffixed o-grade form *soib-on- in Germanic *saipōn-, \\\"dripping thing\\\", resin, in: a. Old English sāpe, soap …: SOAP; b. Latin sāpō, soap' — again Latin under the Germanic node.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"POK_full.txt l.72748 (IEW 894)\", \"stance\": \"partial\", \"note\": \"see ref_check.\"},\n            {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt l.912; index l.2212 (SAPONACEOUS/SAPONATE/SAPONIFY seib-)\", \"stance\": \"partial\", \"note\": \"see ref_check.\"},\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt l.33718 s.v. saponaceous; l.35756 s.v. soap\", \"stance\": \"partial\", \"note\": \"'fr. L. sapo, gen. saponis, \\\"soap\\\", which is a Teut. loan word. See soap.' and s.v. soap: 'L. sapō, \\\"soap\\\", is a Teut. loan word.'\"},\n            {\"src\": \"WLD\", \"where\": \"WLD_Bd2_pages.txt l.31073-31076 (WP II 468)\", \"stance\": \"partial\", \"note\": \"'vgl. Vf. LEWb. u. sapo (germ. Lw.)', with the discussion whether the word originally meant 'urine as a detergent' or 'a resinate'.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Greek\",\n          \"words\": \"sapôn\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Koine Greek σάπων, gen. σάπωνος 'soap' is a first/second-century borrowing of Latin sāpō(nem), the -ων stem rendering Latin -ō/-ōnem directly; it appears in the medical and technical literature of the Roman empire — Aretaeus of Cappadocia, Serenus Sammonicus, and in Greek pharmacological texts contemporary with Pliny's Latin notice (NH 77 CE). Wiktionary s.v. σάπων: 'usually said to be from Latin sāpō', with a minority suggestion of direct borrowing from Galatian (a Celtic language of Anatolia) — which would not change the ultimate Germanic origin. Mohammad Moʿin's etymological footnote in Borhan-e Qāṭeʿ gives exactly Nourai's sequence: '(عر) صابون، از یونانی sapon، لاتینی sapo … فرانسوی savon، انگلیسی soap، آلمانی Seife'. Node confirmed; the only correction is upstream (Latin sāpō is itself Germanic, node #1).\",\n          \"derivation_fa\": \"یونانیِ کوینه σάπων «صابون» وام‌واژه‌ای از لاتینیِ sāpō(nem) است که در سدهٔ یکم و دومِ میلادی وارد یونانی شده و پایانهٔ -ων آن مستقیماً برگردانِ -ō/-ōnem لاتینی است؛ نخستین کاربردهایش در نوشته‌های پزشکیِ دورهٔ روم است (آرِتایوسِ کاپادوکیه‌ای، سِرِنوس سامّونیکوس) هم‌زمان با گزارشِ لاتینیِ پلینیوس (۷۷ م). ویکی‌واژه می‌نویسد «معمولاً گفته می‌شود از لاتینیِ sāpō است» و تنها احتمالِ جایگزین، وام‌گیریِ مستقیم از گالاتیایی (زبانی سلتی در آناتولی) است که در خاستگاهِ نهاییِ ژرمنی تغییری نمی‌دهد. حاشیهٔ ریشه‌شناختیِ دکتر معین در برهان قاطع دقیقاً همین زنجیره را می‌آورد: «(عر) صابون، از یونانی sapon، لاتینی sapo … فرانسوی savon، انگلیسی soap، آلمانی Seife». ادعای نورایی در این گره درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%CF%83%CE%AC%CF%80%CF%89%CE%BD\"],\n          \"ref_check\": [\n            {\"ref\": \"BQT:1330\", \"status\": \"supports\", \"note\": \"Rendered with tools/ref_page.py; the صابون footnote is on the first page of the ص section of Borhan vol. 3 (the tool maps it to BQT:1328, pdf p. 123 of BQT_v3_picofile.pdf — the scan carries no printed folio numbers, and refs_online.json warns the vol-3 offset is approximate, so this is Nourai's 1330 within the ±2 uncertainty). Footnote 4 reads: '(عر) صابون، از یونانی sapon، لاتینی sapo و … بهمین معنی … فرانسوی savon، انگلیسی soap، آلمانی Seife. رک: لک ص ۳۰۹ و لغب ص ۹۴.' The headword above it is 'صاپون … معروف است و آن چیزی باشد که بدان جامه و امثال آن شویند'. Image cached at data/verification/sources/refs/ocr/BQT/1328.png.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BQT\", \"where\": \"refs/ocr/BQT/1328.png + .txt (Borhan vol. 3, ص section, Moʿin's footnote)\", \"stance\": \"supports\", \"note\": \"see ref_check — Moʿin gives Greek sapon > Latin sapo as the source of Arabic صابون, i.e. Nourai's chain.\"},\n            {\"src\": \"LKT\", \"where\": \"LKT.txt (grep 'sabun|sapon|Seife')\", \"stance\": \"silent\", \"note\": \"Lokotsch's dictionary of European words of oriental origin has no صابون entry — consistent with the word travelling west-to-east, not east-to-west; the only 'Seife' hits are unrelated (Nos. 549, 1585).\"},\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt l.35756 s.v. soap\", \"stance\": \"partial\", \"note\": \"Klein traces L. sapō to Germanic and does not discuss the Greek, but the Latin > Greek direction follows from his statement that the Latin is the Teutonic loan.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Arabic\",\n          \"words\": \"sâboun\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Arabic صابون ṣābūn 'soap' is certainly the same travelling word, and the Arab lexicographers themselves knew it was foreign (al-Jawāliqī, al-Muʿarrab p. 98). But the direct Greek → Arabic arrow is very probably one step short: the loan reached Arabic through Aramaic/Syriac ṣappōnā (ܨܦܘܢܐ, Jewish Aramaic צפון), and the emphatic ṣ- of the Arabic form is the tell-tale — Fraenkel, Die aramäischen Fremdwörter im Arabischen (Nachträge to p. 98), says it outright: 'Natürlich geht er aber nicht direct auf σάπων / sapo (keltischen Ursprungs) zurück, sondern auf dessen aramäische Aequivalente. Bemerkenswerth ist das ṣ als Anlaut; aber auch dies findet sich schon im aramäischen ṣappōn … In der Verwandlung des griech.-lat. s in den emphatischen Laut sehe ich eine Einwirkung des folgenden griechischen p.' Wiktionary gives the same chain: Proto-Germanic *saipǭ > Latin sāpōnem > Greek σάπων > Syriac ṣappōnā > Arabic ṣābūn. The Arabic shape ṣābūn (fāʿūl pattern, with -b- for the Greek/Aramaic -p-, Arabic having no p) is a regular naturalisation; it is treated as a noun without a native triliteral root. Nourai's own citation TAD:43 in fact names Latin, not Greek, as the source.\",\n          \"derivation_fa\": \"عربیِ «صابون» بی‌گمان همین واژهٔ جهانگرد است و خودِ لغت‌نویسانِ عرب نیز می‌دانستند که دخیل است (الجوالیقی، المعرّب، ص ۹۸). اما پیکانِ مستقیمِ یونانی ← عربی به احتمالِ قوی یک حلقه کم دارد: وام‌گیری از راهِ آرامی/سریانیِ ṣappōnā (ܨܦܘܢܐ) صورت گرفته و گواهِ آن همان «ص» مفخّمِ آغازین است. فرِنکل در «وام‌واژه‌های آرامی در عربی» (تعلیقات بر ص ۹۸) صریح می‌گوید: «البته این واژه مستقیماً به σάπων یونانی/sapo لاتینی بازنمی‌گردد، بلکه به معادلِ آرامیِ آن؛ ص آغازین شایانِ توجه است و همین در آرامیِ ṣappōn نیز دیده می‌شود؛ تبدیلِ s یونانی‑لاتینی به آوای مفخّم را اثرِ p پس از آن می‌دانم.» ویکی‌واژه نیز همین زنجیره را می‌دهد: ژرمنیِ آغازین *saipǭ ← لاتینی ← یونانی ← سریانی ← عربی. قالبِ «فاعول» و ابدالِ p به b (که در عربی p ندارد) طبیعی است. افزون بر این، مأخذی که خودِ نورایی آورده (التعریب، طوبیا العنیسی، ص ۴۳) منشأ را «لاتینی» می‌نامد نه یونانی. پس ادعا با احتیاط پذیرفتنی است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D8%B5%D8%A7%D8%A8%D9%88%D9%86\"],\n          \"ref_check\": [\n            {\"ref\": \"TAD:43\", \"status\": \"partial\", \"note\": \"TAD_pages.txt \\\\f-leaf 47 (printed p. ≈ 41-43 by the offset recorded in refs_online.json, i.e. Nourai's 43), l.1719 of TAD.txt: 'صابون © لاتيني sapo … ذكره بلينيوس وكان خليطا من رماد وشحم' — al-ʿUnaysī derives صابون from LATIN sapo (and cites Pliny: 'a mixture of ash and fat'), not from Greek as Nourai's arrow has it.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"AFA\", \"where\": \"AFA.txt l.10139-10147 (Fraenkel, Nachträge, note to p. 98)\", \"stance\": \"contradicts\", \"note\": \"'Bei diesen Toilettegegenständen muss noch der Name der Seife صابون erwähnt werden. Schon die Araber wussten, dass er fremd ist (Muʿarrab 98). Natürlich geht er aber nicht direct auf σάπων / sapo (keltischen Ursprungs) zurück, sondern auf dessen aramäische Aequivalente.' — an Aramaic intermediary, contra the direct Greek→Arabic arrow.\"},\n            {\"src\": \"AFM\", \"where\": \"AFM_pages.txt l.2719-2730 (Addi Shir s.v. صابون)\", \"stance\": \"partial\", \"note\": \"a long discussion listing the Latin, French savon, Italian sapone, Syriac ܨܦܘܢ and English/German forms, weighing a Persian origin (with a reference to Fraenkel) and concluding 'الصابون صيغة آرامية' — the form ṣābūn is Aramaic. Addi Shir does not accept a Persian source.\"},\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt l.33718, 35756\", \"stance\": \"partial\", \"note\": \"Klein makes the whole family Germanic in origin and the Latin a Teutonic loan; he does not treat the Arabic.\"},\n            {\"src\": \"TAD\", \"where\": \"TAD_pages.txt leaf 47\", \"stance\": \"partial\", \"note\": \"see ref_check — Latin, not Greek.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Persian\",\n          \"words\": \"sâbŭn «صابون»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"New Persian صابون ṣābūn is a straightforward Arabic loan, taken over with the Arabic orthography (ص for a sound Persian pronounces as plain s, ū written with wāw) after the Islamic conquest; Persians pronounce it sābūn. Moʿin's Farhang-e Fārsi tags the lemma 'صابون [= صابون، معرّب] (اِ.)' — i.e. an Arabicised (foreign) word — and glosses it as the chemical substance used for washing body and clothes; Moʿin's own etymological footnote in Borhan-e Qāṭeʿ (see node #2) marks the headword '(عر)' = Arabic and traces it further to Greek and Latin. Wiktionary's Persian section: 'Ultimately from Arabic صَابُون (ṣābūn)'. So this is a Greek/Latin word that reached Persian through Arabic — not a Persian word at all, and not (pace some Arab lexicographers reported by Addi Shir) a Persian original that Arabic borrowed.\",\n          \"derivation_fa\": \"«صابون» در فارسیِ نو وام‌واژه‌ای مستقیم از عربی است که پس از اسلام با همان املای عربی (با «ص» که فارسی‌زبانان آن را «س» تلفظ می‌کنند) وارد شده است. معین در فرهنگ فارسی مدخل را چنین نشان می‌دهد: «صابون [= صابون، معرّب] (اِ.)» و آن را «جسمی که از مادهٔ چرب ساخته شود و در شستشوی بدن و لباس به‌کار برند» تعریف می‌کند؛ در حاشیهٔ برهان قاطع نیز آن را «(عر)» نشانه زده و تا یونانی و لاتینی پی گرفته است. ویکی‌واژه هم می‌نویسد که فارسی آن را از عربیِ ṣābūn گرفته است. پس این واژه یونانی‑لاتینی است که از راهِ عربی به فارسی رسیده، نه واژه‌ای ایرانی — و برخلافِ گمانِ برخی لغویانِ عرب که ادّی شیر نقل می‌کند، اصلِ فارسی ندارد. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D8%B5%D8%A7%D8%A8%D9%88%D9%86\"],\n          \"ref_check\": [\n            {\"ref\": \"MON:2118\", \"status\": \"supports\", \"note\": \"MON_part1.txt l.88405-88413: 'صابون: [= صابون، معرّب] (اِ.) (شیم.) جسمی است که از ماده‌ای چرب ساخته شود و آن را در شستشوی بدن و لباس بکار برند …' — Moʿin's tag معرّب marks it as an Arabicised loan, which is Nourai's Arabic → Persian arrow. (Page numbers cannot be mapped in the OCR text file, but صابون falls in Moʿin's vol. 2, where p. 2118 lies.)\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"MON_part1.txt l.88405-88413\", \"stance\": \"supports\", \"note\": \"see ref_check.\"},\n            {\"src\": \"BQT\", \"where\": \"refs/ocr/BQT/1328.png (Borhan vol. 3, headword صاپون/صابون + Moʿin's footnote)\", \"stance\": \"supports\", \"note\": \"headword 'صاپون … معروف است و آن چیزی باشد که بدان جامه و امثال آن شویند و صهل خام است'; footnote '(عر) صابون، از یونانی sapon، لاتینی sapo'. Note Borhan's own main spelling صاپون with پ, a doublet of the Arabic-spelt form.\"},\n            {\"src\": \"AFM\", \"where\": \"AFM_pages.txt l.2719-2730\", \"stance\": \"partial\", \"note\": \"Addi Shir reports (and does not endorse) the opinion 'فذهب قوم الى أنه فارسي' — some held it Persian — but concludes the form is Aramaic; no support for a Persian origin, which is what Nourai's arrow direction (Arabic → Persian) also implies.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Germanic\",\n          \"words\": \"\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"An empty pass-through box standing for Proto-Germanic: Watkins reconstructs the o-grade *soib-on- > Proto-Germanic *saipōn- (Wiktionary *saipǭ) 'dripping thing, resin', plus a variant *sib- 'sieve' and *sīpōn- 'to drip, seep'. These give OHG seifa/seiffa, MLG sēpe, OE sāpe 'soap' (and sāp 'resin'), OE sife 'sieve', OE sīpian 'to seep'. Nourai's box is correct as far as it goes; its real defect is that it is not connected to the Latin box above it, since Latin sāpō is a loan out of precisely this Germanic word (see node #1).\",\n          \"derivation_fa\": \"این جعبه گرهی گذرا و بی‌واژه است و نمایندهٔ «ژرمنیِ آغازین» است: واتکینز صورتِ درجهٔ o یعنی *soib-on- را بازسازی می‌کند که در ژرمنیِ آغازین *saipōn- (در ویکی‌واژه *saipǭ) «چیزِ چکنده، صمغ» شده است، در کنارِ گونهٔ *sib- «غربال» و *sīpōn- «چکیدن». بازتاب‌های آن: آلمانیِ علیای کهن seifa، ساکسونیِ سفلای میانه sēpe، انگلیسیِ کهن sāpe «صابون» (و sāp «صمغ»)، sife «غربال» و sīpian «تراویدن». جعبهٔ نورایی در حدِّ خود درست است؛ عیبِ اصلی‌اش آن است که به جعبهٔ لاتینیِ بالای خود وصل نشده، حال آنکه لاتینیِ sāpō دقیقاً وام‌گرفته از همین واژهٔ ژرمنی است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt l.912 s.v. seib-: '2. Suffixed o-grade form *soib-on- in Germanic *saipēn- [*saipōn-], \\\"dripping thing\\\", resin … 3. Variant Germanic form *sib- …'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt l.912\", \"stance\": \"supports\", \"note\": \"see ref_check.\"},\n            {\"src\": \"POK\", \"where\": \"POK_full.txt l.72748 (IEW 894)\", \"stance\": \"supports\", \"note\": \"'Germanic *saip(i)ō: Finnish saip(p)io, Old High German sei(p)fa \\\"soap\\\"; also \\\"resin\\\", Middle Low German sepe \\\"soap\\\", Old English sāpe f.'\"},\n            {\"src\": \"WLD\", \"where\": \"WLD_Bd2_pages.txt l.31073-31082 (WP II 468)\", \"stance\": \"supports\", \"note\": \"'ferner, ob neben germ. *saip(p)ōn- auch ein germ. *sēpōn- \\\"Talg\\\" anzusetzen sei, das mit lat. sebum \\\"Talg\\\" auf ein idg. *se[i]bo- \\\"tropfbares Fett\\\" beziehbar wäre'.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"English\",\n          \"words\": \"soap, sip, sieve\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Two of the three words are right, the third is not. (1) soap: OE sāpe > ME sope > soap, from Proto-Germanic *saipǭ — confirmed by Watkins (SOAP under seib-), Klein ('ME. sope, fr. OE. sāpe, which is rel. to MLG. sēpe, Du. zeep, OHG. seiffa … fr. I.-E. base *se(i)b-'), Pokorny and Walde-Pokorny. (2) sieve: OE sife > ME sive > sieve, from the Germanic variant *sib-, Watkins 'Old English sife, a filter, sieve: SIEVE. b. Old English siftan, to sieve, drain: SIFT' — confirmed. (3) sip: this does not belong here. Watkins' seib- article lists SEEP (OE sipian, sypian), SIEVE and SIFT, but never SIP; Etymonline derives sip (late 14c. sippen 'drink in small mouthfuls') from OE sypian / a Continental Germanic source and calls it 'possibly a modification of sup intended to express a slighter action', i.e. from Proto-Germanic *supanan and PIE *seuǝ- 'to take liquid' — a different root (the one that also gives Latin sūcus 'juice', sūgere 'to suck'). Nourai has almost certainly substituted **sip** for **seep**, the word Watkins actually files under this root. Verdict for the node is the worst of the three.\",\n          \"derivation_fa\": \"از سه واژهٔ این جعبه، دو تا درست است و یکی نادرست. (۱) soap: از انگلیسیِ کهن sāpe و آن از ژرمنیِ آغازین *saipǭ؛ واتکینز، کلاین («ME. sope, fr. OE. sāpe … fr. I.-E. base *se(i)b-»)، پوکورنی و والده‑پوکورنی همگی تأیید می‌کنند. (۲) sieve: از انگلیسیِ کهن sife و گونهٔ ژرمنیِ *sib-؛ واتکینز SIEVE و SIFT را ذیلِ همین ریشه آورده است. (۳) اما sip به این ریشه تعلق ندارد: واتکینز ذیلِ seib- واژهٔ SEEP (انگلیسیِ کهن sipian) را می‌آورد نه SIP، و اتیمآنلاین sip را (از سدهٔ چهاردهم، sippen «جرعه‌جرعه نوشیدن») از sypian انگلیسیِ کهن یا منبعی ژرمنیِ قاره‌ای می‌داند و آن را «احتمالاً دگرگونیِ sup برای بیانِ کنشی سبک‌تر» می‌خواند، یعنی از ژرمنیِ *supanan و ریشهٔ هندواروپاییِ *seuǝ- «مایع برگرفتن» — ریشه‌ای دیگر که لاتینیِ sūcus و sūgere نیز از آن است. به احتمال زیاد نورایی به‌جای seep (که واتکینز واقعاً ذیلِ این ریشه دارد) sip نوشته است. پژوهشِ امروزی این بخش را رد می‌کند، و چون بدترین حکمِ واژه‌ها ملاک است، حکمِ گره «مورد اختلاف» است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/sip\",\n            \"https://en.wiktionary.org/wiki/%D8%B5%D8%A7%D8%A8%D9%88%D9%86\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives this node no reference of its own; the parent Germanic box carries only 'AHD', which was checked at node #5 and which lists SOAP, SIEVE, SIFT and SEEP — but not SIP — under seib-.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt l.912 s.v. seib-; index l.2273 (SOAP seib-), l.2255 (SIEVE seib-), l.2256 (SIFT seib-), l.2235 (SEEP seib-)\", \"stance\": \"partial\", \"note\": \"SOAP, SIEVE, SIFT and SEEP are all indexed to seib-; SIP is absent from the seib- article and from the index under this root.\"},\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt l.35756 s.v. soap\", \"stance\": \"partial\", \"note\": \"'soap, n. — ME. sope, fr. OE. sāpe, which is rel. to MLG. sepe, Du. zeep, OHG. seiffa, seifa … fr. I.-E. base *se(i)b-, \\\"tallow, resin\\\" … L. sapō, \\\"soap\\\", is a Teut. loan word.' Klein's soap article says nothing about sip, which he treats with sup.\"},\n            {\"src\": \"POK\", \"where\": \"POK_full.txt l.72736-72744 (IEW 894)\", \"stance\": \"partial\", \"note\": \"'Old High German sib, Dutch zeef, Middle Low German seve, Old English sife n. \\\"sieve\\\" … Old English sīpian, Middle Low German sipen \\\"drip, trickle\\\" … Old English sāpe f. \\\"soap\\\"' — sieve, seep and soap, no sip.\"},\n            {\"src\": \"SKT\", \"where\": \"SKT.txt l.17671 (s.v. saponaceous/soapy)\", \"stance\": \"silent\", \"note\": \"Skeat's concise edition OCR is badly damaged here; the soap entry itself could not be read cleanly, and there is no usable statement about sip.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\n"
}
```


### [2026-09-14T01:47:25.952Z] TOOL RESULT

```
File created successfully at: /home/sfmqrb/git/rishe/data/verification/page-437.json (file state is current in your context — no need to Read it back)
```


## [2026-09-14T01:47:31.434Z] TOOL CALL #71: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-437.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 437",
 "description": "Validate and run verify_check"
}
```


### [2026-09-14T01:47:32.850Z] TOOL RESULT

```
JSON OK
nodes verified: 15/15
node verdicts: {'confirmed': 9, 'plausible': 4, 'unverified': 1, 'disputed': 1}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 9, 'not_checked': 5, 'partial': 5}
books consulted: {'supports': 26, 'partial': 17, 'silent': 6, 'contradicts': 1} | by book: {'KLN': 8, 'AHD': 7, 'POK': 6, 'CHEUNG': 4, 'BQT': 4, 'IEC': 3, 'MON': 3, 'WLD': 3, 'BRT': 2, 'AFM': 2, 'HUB': 1, 'HRN': 1, 'SOD': 1, 'ARY': 1, 'LKT': 1, 'AFA': 1, 'TAD': 1, 'SKT': 1}
```


## [2026-09-14T01:47:53.509Z] AGENT

Done — `/home/sfmqrb/git/rishe/data/verification/page-437.json` written; `verify_check.py 437` reports 15/15 nodes, **0 PROBLEM lines**.

**Page 437 (book 407) — roots Seiku/Seikw and Seip**
- Roots: 2 confirmed (POK 893-894 and Watkins both match Nourai's names, labels and glosses).
- Nodes: 9 confirmed, 4 plausible, 1 unverified, 1 disputed.

Flagged items:
- **disputed** — Seip, node #6 `soap, sip, sieve`: *soap* and *sieve* are correct, but **sip** does not belong to *seip-/seib-*. Watkins lists SEEP (OE sipian), SIEVE, SIFT under this root, never SIP; Etymonline puts *sip* with *sup* < PGmc *supanan, PIE *seuǝ-. Almost certainly Nourai wrote "sip" for "seep".
- No `transcription_suspect` nodes and **no extraction errors**: the JSON matches the printed page exactly (page image archived at `data/verification/sources/refs/ocr/BOOK/437.png`).

Main substantive corrections recorded as `plausible`:
- Seip #1 Latin `sâpô` — POK (on the cited p. 894), Watkins, Klein and WP II 468 all say Latin *sāpō* is a **Germanic loanword**; the chain should run root → Germanic → Latin, and Nourai's own Germanic box is left unconnected.
- Seip #3 Arabic `sâboun` — Fraenkel (AFA, note to p. 98) explicitly denies a direct Greek→Arabic route: it came via Aramaic/Syriac *ṣappōnā* (hence the emphatic ṣ-); Addi Shir concurs ("الصابون صيغة آرامية"). Nourai's own TAD:43 names **Latin**, not Greek.
- Seiku #2 Persian `pašanjîdan` — root correct, prefix wrong: Hübschmann (PSt 42/191 `*pat-sinč-ītan`) and Cheung (`(+*pati-) BMP passinj-`, NP pišanjīdan) give ***pati-***, not the *fra-* that Nourai's ☞Per 1 pointer implies.
- Seiku #4 Latin `siccus` — Pokorny/Watkins/Klein support, but this is really Pokorny's secondary *seikʷ- "dry", and de Vaan/Wiktionary prefer *sisk(ʷ)os.
- **unverified** — Seiku #6 Persian `sek «سک»` "non-diluted drink": colloquially real, but Dehkhoda, Moʿin, Amid, fa.wiktionary, Borhan and Aryanpur all lack the sense and the French etymology, and Nourai's sole source VOP (Moshiri) has no copy anywhere.

Reference notes for the owner: SOD:303 is exact (leaf 369 = printed 303, entry 7537). TAD:43 is right within the recorded offset. BQT:1330 — the صابون footnote sits on the first page of the ص section of vol. 3; `ref_page.py` maps it to BQT:1328 (pdf p.123), but the scan has no printed folio numbers and refs_online.json flags the vol-3 offset as approximate, so Nourai's 1330 is within tolerance. Minor book typography: the page prints `fra-šaĕkam` (breve) where Bartholomae/Cheung have `fra-šaēkam`.
