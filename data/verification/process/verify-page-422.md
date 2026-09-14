# Verification process log — verify-page-422


## [2026-09-14T01:21:33.196Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 422 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-422.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-422.json. Write /home/sfmqrb/git/rishe/data/verification/page-422.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 422` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T01:21:34.156Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T01:21:34.945Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T01:21:34.963Z] TOOL RESULT

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


## [2026-09-14T01:21:35.382Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-422.txt"
}
```


### [2026-09-14T01:21:35.408Z] TOOL RESULT

```
1	=== PDF page 422 (book page 392) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Ret : to roll, run  (refs POK:866)
4	#1 (parent #0) [Avestan] refs=POK:866; LEW:904 | rad 2 : to run ; ratha : chariot ; ratha-eštra : standing on the chariot, soldier ☞Stâ
5	  #2 (parent #1) [Persian] refs=BQT:97,1895; MON:191; ARB:203 | arrâdeh «ارّاده» : chariot ; arteštâr «ارتشتار ( ارتش )» : chariot rider, soldier ; laškar «لشکر ( عسکر )» : army
6	  #3 (parent #1) [Pahlavi] refs=BQT:934 | râs : path, way
7	    #4 (parent #3) [Persian] refs=HUB:66; BQT:984; PLA:133; FFD:56 | râh «راه ( رَه ، رهرو ، راهرو )» : path, way, manner
8	      #5 (parent #4) [Persian] refs=HUB:66; BQT:984; PLA:133 | rahbar «رهبر ( رهنما ، راهنما )» : guide ; râygân «رایگان» : "found on the road", free ; râhbân «راهبان» : road guard ; râheb «راهب ( راهبه )» : one who watches his manners, monk
9	      #6 (parent #4) [Arabic] refs=TAD:17 | torrahât : minor paths, insignificant things
10	        #7 (parent #6) [Persian] refs=MON:1074 | torrahât «تُرَّهات» : worthless things
11	#8 (parent #0) [Old Persian] refs=KNT:176 | ratha : chariot ; u-ratha : having good chariots ☞Su 1
12	  #9 (parent #8) [None] refs=None |  | NOTE: box is printed entirely blank in the source (outlined box, no header text or content)
13	#10 (parent #0) [Latin] refs=AHD | rota : wheel ; ret-undus : wheel
14	  #11 (parent #10) [French] refs=AHD | 
15	    #12 (parent #11) [Persian] refs=MON |  «رولت ، کنترل»
16	    #13 (parent #11) [English] refs=AHD | round, roll, roulette, control
17	  #14 (parent #10) [English] refs=AHD | rotate, rotary
18	
```


## [2026-09-14T01:21:38.418Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-422.json | python3 -m json.tool | head -200",
 "description": "Read page 422 source JSON"
}
```


## [2026-09-14T01:21:39.364Z] TOOL CALL #4: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo \"---\" && cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "List verification dir and source matrix"
}
```


### [2026-09-14T01:21:39.494Z] TOOL RESULT

```
{
    "pdf_page": 422,
    "book_page": 392,
    "entries": [
        {
            "root": {
                "name": "Ret",
                "lang": "Indo-European",
                "refs": "POK:866",
                "gloss": "to roll, run"
            },
            "nodes": [
                {
                    "id": 1,
                    "parent": 0,
                    "lang": "Avestan",
                    "refs": "POK:866; LEW:904",
                    "words": [
                        {
                            "translit": "rad 2",
                            "gloss": "to run",
                            "script": null
                        },
                        {
                            "translit": "ratha",
                            "gloss": "chariot",
                            "script": null
                        },
                        {
                            "translit": "ratha-e\u0161tra",
                            "gloss": "standing on the chariot, soldier",
                            "script": null,
                            "see": [
                                "St\u00e2"
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
                    "refs": "BQT:97,1895; MON:191; ARB:203",
                    "words": [
                        {
                            "translit": "arr\u00e2deh",
                            "gloss": "chariot",
                            "script": "\u0627\u0631\u0651\u0627\u062f\u0647"
                        },
                        {
                            "translit": "arte\u0161t\u00e2r",
                            "gloss": "chariot rider, soldier",
                            "script": "\u0627\u0631\u062a\u0634\u062a\u0627\u0631 ( \u0627\u0631\u062a\u0634 )"
                        },
                        {
                            "translit": "la\u0161kar",
                            "gloss": "army",
                            "script": "\u0644\u0634\u06a9\u0631 ( \u0639\u0633\u06a9\u0631 )"
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 3,
                    "parent": 1,
                    "lang": "Pahlavi",
                    "refs": "BQT:934",
                    "words": [
                        {
                            "translit": "r\u00e2s",
                            "gloss": "path, way",
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
                    "refs": "HUB:66; BQT:984; PLA:133; FFD:56",
                    "words": [
                        {
                            "translit": "r\u00e2h",
                            "gloss": "path, way, manner",
                            "script": "\u0631\u0627\u0647 ( \u0631\u064e\u0647 \u060c \u0631\u0647\u0631\u0648 \u060c \u0631\u0627\u0647\u0631\u0648 )"
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 5,
                    "parent": 4,
                    "lang": "Persian",
                    "refs": "HUB:66; BQT:984; PLA:133",
                    "words": [
                        {
                            "translit": "rahbar",
                            "gloss": "guide",
                            "script": "\u0631\u0647\u0628\u0631 ( \u0631\u0647\u0646\u0645\u0627 \u060c \u0631\u0627\u0647\u0646\u0645\u0627 )"
                        },
                        {
                            "translit": "r\u00e2yg\u00e2n",
                            "gloss": "\"found on the road\", free",
                            "script": "\u0631\u0627\u06cc\u06af\u0627\u0646"
                        },
                        {
                            "translit": "r\u00e2hb\u00e2n",
                            "gloss": "road guard",
                            "script": "\u0631\u0627\u0647\u0628\u0627\u0646"
                        },
                        {
                            "translit": "r\u00e2heb",
                            "gloss": "one who watches his manners, monk",
                            "script": "\u0631\u0627\u0647\u0628 ( \u0631\u0627\u0647\u0628\u0647 )"
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 6,
                    "parent": 4,
                    "lang": "Arabic",
                    "refs": "TAD:17",
                    "words": [
                        {
                            "translit": "torrah\u00e2t",
                            "gloss": "minor paths, insignificant things",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 7,
                    "parent": 6,
                    "lang": "Persian",
                    "refs": "MON:1074",
                    "words": [
                        {
                            "translit": "torrah\u00e2t",
                            "gloss": "worthless things",
                            "script": "\u062a\u064f\u0631\u064e\u0651\u0647\u0627\u062a"
                        }
                    ],
                    "note": null,
                    "quote": {
                        "text": "\u0646\u062e\u0648\u062a \u0648 \u062f\u0639\u0648\u06cc \u0648 \u06a9\u0628\u0631 \u0648 \u062a\u064f\u0631\u064e\u0651\u0647\u0627\u062a - \u062f\u0648\u0631 \u06a9\u0646 \u0627\u0632 \u062f\u0644 \u06a9\u0647 \u062a\u0627 \u06cc\u0627\u0628\u06cc \u0646\u062c\u0627\u062a",
                        "poet": "Molav\u00ee"
                    }
                },
                {
                    "id": 8,
                    "parent": 0,
                    "lang": "Old Persian",
                    "refs": "KNT:176",
                    "words": [
                        {
                            "translit": "ratha",
                            "gloss": "chariot",
                            "script": null
                        },
                        {
                            "translit": "u-ratha",
                            "gloss": "having good chariots",
                            "script": null,
                            "see": [
                                "Su 1"
                            ]
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 9,
                    "parent": 8,
                    "lang": null,
                    "refs": null,
                    "words": [],
                    "note": "box is printed entirely blank in the source (outlined box, no header text or content)",
                    "quote": null
                },
                {
                    "id": 10,
                    "parent": 0,
                    "lang": "Latin",
                    "refs": "AHD",
                    "words": [
                        {
                            "translit": "rota",
                            "gloss": "wheel",
                            "script": null
```


### [2026-09-14T01:21:39.545Z] TOOL RESULT

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


## [2026-09-14T01:22:05.094Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -m json.tool data/extracted/batch/page-422.json | sed -n '200,400p'",
 "description": "Rest of page 422 JSON"
}
```


## [2026-09-14T01:22:05.912Z] TOOL CALL #6: Bash

```json
{
 "command": "sed -n '1,120p' data/verification/page-385.json",
 "description": "Look at a recent verification file for style"
}
```


### [2026-09-14T01:22:06.099Z] TOOL RESULT

```
                            "script": null
                        },
                        {
                            "translit": "ret-undus",
                            "gloss": "wheel",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 11,
                    "parent": 10,
                    "lang": "French",
                    "refs": "AHD",
                    "words": [],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 12,
                    "parent": 11,
                    "lang": "Persian",
                    "refs": "MON",
                    "words": [
                        {
                            "translit": null,
                            "gloss": null,
                            "script": "\u0631\u0648\u0644\u062a \u060c \u06a9\u0646\u062a\u0631\u0644"
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 13,
                    "parent": 11,
                    "lang": "English",
                    "refs": "AHD",
                    "words": [
                        {
                            "translit": "round, roll, roulette, control",
                            "gloss": null,
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 14,
                    "parent": 10,
                    "lang": "English",
                    "refs": "AHD",
                    "words": [
                        {
                            "translit": "rotate, rotary",
                            "gloss": null,
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                }
            ]
        }
    ]
}
```


### [2026-09-14T01:22:06.158Z] TOOL RESULT

```
{
  "pdf_page": 385,
  "book_page": 355,
  "verified_by": "claude-opus-5",
  "verified_on": "2026-09-07",
  "entries": [
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
          "note": "'peg-. Breast. 1. Suffixed variant form *pek-tos- in Latin pectus, breast: PECTORAL; EXPECTORATE, PARAPET. 2. Possibly suffixed variant form *pek-so- in Sanskrit paksah, wing: PUNKA. [Pok. (peg-), pog- 792.]' — this is verbatim Nourai's chart (grep '^peg-' AHD_watkins1985.txt line 820)."
        },
        {
          "src": "WLD",
          "where": "Walde-Pokorny II 3-4 (WLD_Bd2_pages.txt leaf 8)",
          "stance": "partial",
          "note": "Entry headed 'pag-' (their spelling) with 'ai. pajasyá- n. Bauchgegend, Weichen, russ. pachu \"Leistengegend\", pacha \"Achselhohle\" ... ein io-St. *pagio- in cech. paze \"Arm\"' — again 'flank/armpit', no 'breast'."
        },
        {
          "src": "IEC",
          "where": "Mann, alphabetical",
          "stance": "silent",
          "note": "grep of IEC.txt for 'peg-', 'pokso-', 'pektos' returns no headword for this root."
        }
      ],
      "nodes": [
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
        },
        {
          "id": 2,
          "lang": "Hindustani",
          "words": "pankâ",
          "verdict": "transcription_suspect",
          "error_in": "book",
          "book_prints": "pankâ",
          "correct_form": "pankhā",
          "derivation": "The Hindustani word is पंखा / پنکھا paṅkhā 'fan', with an aspirated -kh-, not 'pankâ'. The printed page (pdf 385, image saved as data/verification/sources/refs/ocr/BOOK/385.png) does read 'pankâ', so this is Nourai's own misprint, not an extraction error: the JSON is faithful to the book. Klein, whom Nourai cites here, spells it 'pankha'. The history: Sanskrit pakṣá- 'wing' > pakṣaka- (with -ka- suffix) > Sauraseni Prakrit pakkha- > Hindi paṅkh 'feather, wing', whence paṅkhā 'fan' (the -kh- is the Middle Indo-Aryan reflex of -kṣ-, and the nasal is an anusvara developed before the cluster). Its basic sense is simply 'fan' (originally a palmyra-leaf hand fan); the 'curtain hung from the ceiling and pulled by a servant' that Nourai glosses is the Anglo-Indian specialisation of the word from the 17th c. on, not the Hindustani meaning.",
          "derivation_fa": "صورت درست واژهٔ هندوستانی paṅkhā «بادبزن» است (با کاف دمیده -kh-)، نه «pankâ». تصویر صفحهٔ چاپی (pdf ۳۸۵) نشان می‌دهد که خودِ کتاب «pankâ» چاپ کرده است؛ پس این خطای چاپی نورایی است نه خطای خوانش اسکن. کلاین که نورایی به او ارجاع می‌دهد، «pankha» نوشته است. راه تحول چنین است: pakṣá- سنسکریت «بال» ← pakṣaka- (با پسوند -ka-) ← pakkha- در پراکریت شورسنی ← paṅkh هندی «پر، بال» و از آن paṅkhā «بادبزن»؛ خوشهٔ -kṣ- در هندوآریایی میانه به -kh- بدل می‌شود و پیش از آن غنّه (انوسوارَه) پدید می‌آید. معنای پایهٔ واژه همان «بادبزن» است؛ معنای «پردهٔ آویخته از سقف که خدمتکار می‌کشد» تخصیص انگلیسی‌ـ‌هندی واژه از سدهٔ هفدهم به بعد است.",
          "sources": [
            "https://en.wiktionary.org/wiki/%E0%A4%AA%E0%A4%82%E0%A4%96%E0%A4%BE",
            "https://en.wiktionary.org/wiki/punkah"
          ],
          "ref_check": [
            {
              "ref": "KLN:1272",
              "status": "partial",
              "note": "Klein 1966 p.1272 (leaf 678): 'punka, punkah, n., a large curtain serving to fan a room. — Hind. pankha, \"a fan\", fr. pankh, \"feather, wing\", fr. OI. pakṣaḥ, pákṣas, \"wing, side, half\"...' — the derivation is Nourai's, but Klein spells the Hindi word pankha and glosses it 'a fan'."
            },
            {
              "ref": "AHD",
              "status": "supports",
              "note": "Watkins 1985 s.v. peg- routes Sanskrit pakṣaḥ to English PUNKA, i.e. the same Sanskrit -> Hindustani -> English chain."
            }
          ],
          "consulted": [
            {
              "src": "HJB",
              "where": "Hobson-Jobson p.742 s.v. PUNKAH",
              "stance": "partial",
              "note": "'PUNKAH, s. Hind. pankhā. a. In its original sense a portable fan, generally made from the leaf of the palmyra ... b. But the specific application in Anglo-Indian colloquial is to the large fixed and swinging fan, formed of cloth stretched on a rectangular frame, and suspended from the ceiling.' Confirms the aspirate and shows the 'curtain' sense is the Anglo-Indian one."
            },
            {
              "src": "LKT",
              "where": "Lokotsch no. 1622 (printed p.132)",
              "stance": "supports",
```


## [2026-09-14T01:22:15.232Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD ret- ===\"; grep -n -A12 '^ret-' AHD_watkins1985.txt | head -60\necho \"=== POK ret- ===\"; grep -n 'reth-\\|ret(h)-\\|^ret-' POK_full.txt | head -30",
 "description": "Grep AHD and Pokorny for ret-"
}
```


### [2026-09-14T01:22:15.302Z] TOOL RESULT

```
=== AHD ret- ===
=== POK ret- ===
70102:ret-^ roar, bellow, rant, roister': 
70379:Root / lemma: ret(h)- 
93398:Root/ lemma: iureth-.) uroth-ox urath-{*hauerth-)
```


## [2026-09-14T01:22:16.833Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KNT ratha ===\"; grep -n 'raθa\\|ratha' KNT.txt | head -40\necho \"=== BRT raθa ===\"; grep -n 'raθa' BRT.txt | head -40",
 "description": "Grep Kent and Bartholomae for ratha"
}
```


### [2026-09-14T01:22:16.956Z] TOOL RESULT

```
=== KNT ratha ===
2252:III. Secondary comparison, that is, comparison by suffixes attached to the stem of the adjective as seen in the positive degree, was made in Aryan by the use of -tara- and -tama-, cf. Gk. -répos -raros, Lt. ex-terus and ex-timus. The comparative is seen in OP fratara- and ady. apataram, the superlative in fratama-. Nt. comp. frafaram has an alternative suffix with aspirated stop, seen in the Skt. superlative prathamd-. A simpler form of the
5700:frafara- adj. ‘superior’: fra- + variant com- par. suffix -thara- seen in Av. fraéara- ($1491, 6190.11; Wb. ЖА 41.319; Bv. 33.2.150-1, 34.1.33-4, Hz. AMI 4.126-7, 8.3940, ApI 166-7), cf. superl. -thama- in Skt. prathamd- ‘first’. Cf. also uradara-. — fra&aram asn. XPf 26f, 37.
=== BRT raθa ===
```


## [2026-09-14T01:22:23.843Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources\npython3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nfor k in ['POK','KNT','BRT','HUB','BQT','MON','PLA','FFD','TAD','ARB','LEW','AHD','PHD','HRN','NYB','IEC','SYN','WLD','KLN','AFM']:\n    v=d.get(k)\n    print('##',k, json.dumps(v,ensure_ascii=False)[:700])\n\"",
 "description": "Show refs_online entries for relevant abbreviations"
}
```


## [2026-09-14T01:22:24.677Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '70370,70450p' POK_full.txt",
 "description": "Print Pokorny ret(h)- entry"
}
```


### [2026-09-14T01:22:25.361Z] TOOL RESULT

```
## POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index 
## KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archiv
## BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between 
## HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by parag
## BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.c
## MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol 
## PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 leaves (pdftotext -layout, \\f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276).", "loo
## FFD {"title": "Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ماده-های-فعلهای-فارسی-دری-محسن-اب/ -> https://dl.eliteraturebook.com/app/public/attachments/6925d29630b83.PDF (free PDF site; grey)", "lookup_hint": "Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/download): nothing; only a related paid e-book 'واژگان زبان فارسی دری' (fidibo). ketabnak.com/book/45024 is a different book (فهرست فعلهای فارسی).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_asmaneketab.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/ref
## TAD {"title": "Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-hurufihi (2nd ed. Cairo 1932, ed. Yusuf Tuma al-Bustani; later Library of Lebanon reprint) — Nourai lists it under Arabic authors ('Unaysi T.'); its Table IV line was lost in the OCR", "kind": "archive_djvu", "url": "https://archive.org/details/TOB1932ARAR (1932 ed.); also https://archive.org/details/ar113lang79 and https://archive.org/details/elshandawily14640", "lookup_hint": "Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; inside.php search works.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD_pag
## ARB {"title": "al-Jawaliqi, al-Mu'arrab min al-kalam al-a'jami, Tehran 1966 (reprint of Ahmad M. Shakir's Cairo 1361/1942 edition)", "kind": "archive_djvu", "url": "https://archive.org/details/mo3rb (probably the Shakir edition) ; https://archive.org/details/almo3rab_gwaliqy_f_abduraheem (F. 'Abd al-Rahim ed., Damascus 1990) ; also uc1.aa0003615705 / AAlexandrina-148752 (Sachau's Leipzig 1867 ed.) ; text on shamela.ws", "lookup_hint": "Alphabetical Arabic headwords; grep in ARB_mo3rb.txt / ARB_abdulraheem.txt (raw, no page breaks); edition of mo3rb not confirmed — check its title page image.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/ARB_mo3rb.txt", "/home/sfmqrb/git
## LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt", "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.o
## AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifie
## PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<ident
## HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the 
## NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Nourai's 'NYB' nu
## IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Reconstruct
## SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<i
## WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.39015066210397 (browser only from this host)", "identifier": "in.gov.ignca.20339 (Band 3); also in.ernet.dli.2015
## KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO pri
## AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM.txt"], "page_offset": "19
```


### [2026-09-14T01:22:25.467Z] TOOL RESULT

```
Lithuanian ap-rept/" catch, gripe, conceive ', Litliuanian rep/es {0\d Prussian raples) f. 
PI. 'pliers'. 

References: WP. II 369 f., WH. II 417, Trautmann 244. 
Page(s): 865 

Root / lemma: ret(h)- 

Meaning: to run, to roll 

Material: Old Indie ratha-xw. " cart ', rathff-^ charioteer ', rathya-'zum cart belonging', 

rathar-yati^\xaye\s in cart '; rathes fha- ^wamor' = Avestan ra^aesfa 6s.; Avestan ra&a-^ 

cart', /"a/z^yaTahrstrafte'; Latin /"o/a "wheel', Z^z/D/i/s 'zweiradrig' (: Lithuanian dviratis), 

rotundus 'scheibenrund'; 

Maybe alb. /lO/a "wheel'. 

Irish rothm. 'wheel'; cymr. rhodi. 'wheel'; gall. PN Roto-magus (Rouen); Celtic *-reto- 

'run, flow', neutr. Abstraktsuffix in cymr. i6'/7//7-/'eo' 'perplexity' = Middle Irish brecht-rad 

'Mannigfaltigkeit', Kollektivsuffix in Middle Irish aig-red^\ce'; lengthened grade Vd/o-in 

mcymr. rhawd^xuu, flow, Laufbahn, Schaar', ^aea/-/'aM/o''Winterszeit' = Middle \us\\gem- 

radds., mcymr. bed-rawd, cymr. bedd-rod, bret. bez-ret ^Graber' (cymr. bedd'grave'), in 

addition Middle Irish ra(i)the^ season, quarter of the year' {*rdtio-); 

Old Irish reth/m'\auie' with compounds, Kaus. /10///7//77 'treibe an'; 

Maybe alb. /re//? 'hoop, rim (of wheel); circle', rretb/m 's\ege'; 

Old Irish verbal noun riuthvn. 'run, flow' {*rtu-); 

Maybe alb. rrjethe, rrjedhei. 'run, flow' {*rtu-); 

to Old Irish do-riuth^acc\xxxQ> belongs cymr. tyred {*to-rete) 'come!'; Old Irish fo-riuth, cymr. 
guo-redar succurro', acymr. Perf. gua-raut= Irish fo-raith {*upo-rdt-e); 

Old Icelandic rgdullm. 'Strahlenkranz, sun' and Old Saxon radur. Old English rador, 
rodorm. 'sky, heaven'; Gothic VaA's 'light', (Kompar. n. rat^izd) Old English A^o^'quick, 
fast, nimble, agile; graceful; sharp, keen ', Old High German rado, rata adv. 'quick, fast'; 
Old Low German rath, afr. reth, Old High German rad^wheeV, rade/dt'\N\t\r\ Raderchen 
versehen'; Lithuanian ratasm. 'wheel, circle ' (Plur. rafa/^ carriage, cart '), Latvian rats 
'wheel' (Plur. rat/^ cart '), Lithuanian ratelism. 'Radchen' (compare Old High German 
rade/otand Latin rotu/at 'Radchen'), o'l/z/a/zs (mostly PI. dviraciai) 'zweiradriger cart '; 

maybe alb. Geg me rotullue^io circulate', lllyrian GN Redon, Rodon 



Lithuanian ritu, n'st/'roW {*rt-); but gall, petor-ritum Werradnger cart ' kann Latin 
development from *petor-roto- sein. 

References: WP. II 368, WH. II 443 f., Trautmann 238. 
Page(s): 866 

Root / lemma: reu-b-ax\6 reu-g- 

Meaning: to vomit, retch 

Material: 1. /■ea&-;Old Icelandic rjupai. "Schneehuhn", Norwegian rjupa, /ype (compare 

Latvian /'i/i6'e/7/s'Birkhuhn'?); ablaut. Old Icelandic AO/Oa 'aufstoften', /yp/a'sich erbrechen', 

Old High German roffezzen^auisio^evi {*rupatjan). Middle High German rofzen. Modern 

High German reshaped to rulzen, rulpsen. 

2. reug-:H^ers. a-roy^dias Rulpsen'; Armenian o/ra/77'erbreche myself, burp' (from 
*orucam, o-\s suggestion vowel); gr. spsuYOMai 'speie from, erbreche myself, spuyyavcjo ' 
burp', spuyn "Aufstoften'; Latin erugo, -e/ie'ausrijlpsen', ructo, -a/ie "rulpsen, ausspeien'; 
Old English /"oce/Za/? "rulpsen', eo''/'c»c"das Wiederkauen', Old High German it-ruchen. 
Middle High German /fe/i/c/re/? "ruminate', iterochei. "gullet from ruminants', v\\s\. Jortru.
```


## [2026-09-14T01:22:32.314Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i 'roulette\\|rotundus\\|ROTATE' AHD_watkins1985.txt | head -20\necho \"=== ret ===\"; grep -n '^ret' AHD_watkins1985.txt | head",
 "description": "Grep Watkins for rot- root"
}
```


### [2026-09-14T01:22:32.382Z] TOOL RESULT

```
895:ryfe, abundant: RIFE. 3. Suffixed form *reip-d- in Latin ripa, bank (< “that which is cut out by a river”): RIPARIAN, RIVAGE, RIVER; ARRIVE. IV. Extended form *reib- in Germanic *rip-. 1. Germanic *ripja- in Old English ripe, ripe, ready for reaping: RIPE. 2. Germanic *ripan in Old English ripan, to reap: REAP. 3. Middle Low German repelen, to remove seeds, akin to the source of Middle English ripelen, to remove seeds: RIPPLE? [Pok. 1. rei- 857.] rei-2. Striped in various colors, flecked. Suffixed o-grade form *roi-ko- in Germanic *raihaz in Old English rd, raha, deer: ROE*. [Pok. 2. rei- 859.] rei-3, To flow, run. 1. Suffixed zero-grade form *7i-nu- in: a. Germanic *ri-nw-an, whence *rinnan, to run, in Old English rinnan, to run, and Old Norse rinna, to run: RUN, RUNNEL; b. secondary Germanic derivative *runiz in Old English ryne, a running: EMBER DAY. 2. Suffixed zero-grade form *ri-l- in Germanic *ril- in Dutch ril and Low German rille, running stream: RILL. 3. Suffixed form *rei-wo- in Latin rivus, stream: RIVAL, RIVULET; DERIVE. [Pok. 3. er- 326.] reidh-. To ride. I. Basic form *reidh-. 1. Germanic *ridan in: a. Old English ridan, to ride: RIDE; b. Middle Dutch riden, to ride (> ridder, rider, knight): RITTER. 2. Celtic *vo-réd- in Latin verédus, post horse (*vo-, under; see upo): PALFREY. II. O-grade form *roidh-. 1. Germanic *raid- in: a. Old English rdd, a riding, road: RAID, ROAD; b. possibly Middle High German reidel, rod between upright stakes (< “wooden horse”): RADDLE!. 2. Prob- ably Germanic *raid-ja- in Old English réde, geréde, ready (< “prepared for a journey’): READY. 3. Germanic *raidjan in Vulgar Latin *arrédare, to arrange: ARRAY. [Pok. reidh- 861.] reig-'. To bind. 1. Germanic *rigg- (the -gg- is anoma- lous) in Norwegian rigga, to bind, akin to the Scandina- vian source of Middle English riggen, to rig: RIG. 2. Zero-grade form *rig- in Latin corrigia (probably borrowed from Gaulish), thong, shoelace (cor-, from com-, together; see kom): SCOURGE. [Pok. reig- 861.] reig-2. To reach, stretch out. 1. O-grade form “roig- in Germanic *raikjan in Old English récan, to stretch out, reach: REACH. 2. Possibly suffixed (stative) zero-grade form “rig-é- in Latin rigére, to be stiff (? < “be stretched out”): RIGID, RIGOR. [Pok. (reig-) 862.] rendh-. To tear up. 1. Germanic *randjan in Old English rendan, to tear: REND. 2. Germanic *rind- in Old English rinde), rind (< “thing torn off”): RIND. [Pok. rendh- 865.] rep-. To snatch. Suffixed zero-grade form *rap-yo- in Latin rapere, to seize: RAPACIOUS, RAPE!, RAPID, RAPT, RAVEN?, RAVIN, RAVISH; EREPSIN, SURREPTITIOUS. [Pok. rep- 865.] rép-'. To creep, slink. Latin répere, to creep: REPENT?, REPTILE; SUBREPTION. [Pok. 1. rép- 865.] rép-2, Stake, beam. Suffixed variant form *rap-tro- in Germanic *raf-tra- in: a. Old English refter, rafter: RAFTER; b. Old Norse raptr, beam: RAFT!. [Pok. 2. rép- 866.] ret-. To run, roll. 1. Prefixed form *to-vo-ret-, “a running up to” (to-, to; vo, under, up, up from under; see upo), in Old Irish toir, pursuit: Tory. 2. Suffixed o-grade form *rot-d- in Latin rota, wheel: RODEO, ROLL, ROTA, RO- TARY, ROTATE, ROTUND, (ROTUNDA), ROULETTE, ROUND!, ROWEL; BAROUCHE, CONTROL, PRUNE?, ROTIFORM, ROTO- GRAVURE. [Pok. ret(h)- 866.] rét-. Post. O-grade form *rdt- in Germanic *réd- in Old English réd, rod, cross: ROOD. [Pok. rét+ 866.] reu-'. To bellow. 1. Extended form *reud- in Germanic *rauton in Old Norse rauta, to roar (akin to the Scandi- navian source of ROTE?): ROUT’. 2. Suffixed extended form *reum-os- in Latin riimor, rumor, “common talk”: RUMOR. 3. Extended form *reug- in Latin rigire, to roar: RIOT, RUT’. 4. Variant *rau-ko- in Latin raucus, hoarse: RAUCOUS. [Pok. 1. reu- 867.]
2199:ROOF kropo- ROOK! ker-2 ROOM reua- ROOST kred- ROOT! wrad- ROOT? wrdd- ROPE rej-1 RORQUAL = reudh-1, (s)kWal-o- ROSE! wrod- ROSEMARY ers-2 ROSTRUM_ réd- ROTA ret- ROTARY ret- ROTATE ret- ROTE? reu-! ROTE3 krut- ROTIFORM ret- ROTOGRAVURE ret- ROTUND ret- ROTUNDA ret- ROUGE reudh-1 ROUGH ruk-2 ROULETTE ret- ROUND! ret- ROUND? riino- ROUT! reup- ROUTS = reu-1 ROUX reudh-1 ROVER reup- Row! rej-1
=== ret ===
```


## [2026-09-14T01:22:33.984Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== LEW leaf for p.904 (leaf=p+12 => 916) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==917' LEW_1910.txt | head -60",
 "description": "LEW page 904"
}
```


### [2026-09-14T01:22:35.075Z] TOOL RESULT

```
=== LEW leaf for p.904 (leaf=p+12 => 916) ===
```


## [2026-09-14T01:22:39.988Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho leaves: $(awk 'BEGIN{RS=\"\\f\"} END{print NR}' LEW_1910.txt)\ngrep -n 'rota' LEW_1910.txt | head -20",
 "description": "Check LEW file size and rota"
}
```


### [2026-09-14T01:22:41.013Z] TOOL RESULT

```
leaves: 305
520:belsa (alt) I 852 blando, blendo I 842 bust (alt) I 573 cara I 165 coguastré I 241 gravena II 448 parran I 257 rota I 294
1385:II 508 awra- I 681 afnahvant- II 216 afsman- II 216 anuhi (gatha) [419 anra- I 406 anhaosamna- IT 624 anhiu- I 406, 419 anhyeitt I 406 ana I 43, 677 anamana- I 677 anarota- I 687 ainika- I 688,
4264:maic, saic If 381. maomaAn IT 331 navpdoow I 471 mafiw (kypr.) IT 267 maim 1574, II 267 mavdy (att.) IT 267 srarotat IT 253. naxtow IT 231, 232 adda I 3878, I 3di mahkaoty IT 240 tahatw IT 241 nahdun IT 240 sahdoow II 243 nahaoty II 240 nahevo I 143, I 582 addn IT 238, 331 rahiunuynddv I 417 adhw I 246 mahivogcos I 417 mahivoetoc II 222 mahuos IT 239, 243 ITahiddvov IT 233 nahhaun IT 233 mahhaxioyv IT 233 sahhaxic IT 233,386 mahhaxoc IT 233 manag, mdahdné
5751:or I 659 ostiiakon IT 225 rehtia IT 424 Sahnater II 476 termonios II 671 tolar II 689 voltiio- IT $30 vrotah IT 765 zonasto I 861
5769:acaunum I 5, 7 Ayrotalus [7 ad- I 11, 843 Aedui [15 Aesus I 419 Agaunus 15 alauda I 26 alla, allos I 30 Allobroges I 30 Amba(c)tus I 37 ambes I 681 ambi- I 36 Ambiosas IT 219 anax (gall.-lat.)
8668:kjorr I 594 klafi I 606 klaki I 603 klam I 617 klambra I 609 klapeygr I 606 klefe 1 232 kleiss I 108 klembra I 609 kleppr I 609 klina I 612 kljufa I 610 klombr I 609 klopp I 608 klumba I 609 knar I 518, 614, IT 150 kniébed I 495 knita IT 167 knykr II 178 kokr I 242 kolfr I 608 kollr I 579 konge I 591 konr I 591 korf I 858 kortr I 317 kostr I 628 kot I 176 kokkr I 801 kongurvafa Il 733, 770 korf I 273 kostr, kos I 595 kraka, krakr I 6165 kramr I 617 kras I 616 kremia I 621 krof I 278 krota I 623 krumma I 621 krytja I 624 kul I 586 kila IT 825 kuldi I 586 kumar I 588 kumla I 589 kundr I 598 kura ,,Klage‘ 1583 kura_ ,,knurren‘‘ I 583
8832:rota II 440
9671:meregrot, meregrota IT 39
9998:word I 56 wos II 818 wop IT 738 wrad I 719 wrestan II 434 wrecan II 839 wregan II 757 wrencan, wrenc II 436, 759 wrigels II 433 wrigian II 438 wrincle IT 436, 449, 759 wringen II 436, 759 wrion, wréon IT 433 writan II 435, 524 wroht I 200 wrotan II 440 wucu IT 782 wuduwe If 786 wulf I 836 wull I 756 wunian IT 753 wurth I 56 wylm IT 833 wynn IL 753 wyrtbed I 522 wyrtwalu, wyrt- wala Il 730 wyskean, wyskan II 753 gece II 849 yd II 818 yferra II 616 ymb(e) ,,um‘ I 36 ymbe ,,Bienen- schwarm II 210 ynce II $16 yndze II $16 ynné IT 820 yrfe II 220 yrre I 416 ysla II 841 qgwan II 201
11145:scouwon I 187 8c63, scoz I 185 screion, screi I 291 screvon II 500 scrian I 291, I1 498 scriban IT 499 scrint IT 500 scritan I 293 scrodén II 498 scrot IT 498 scrotan II 498 scruton, scrutilon IT 498 skubil I 311 skugin(a) IT 196 sculd(a) II 492 skultirra II 492 scum II 196 scuoh IT 196 scuoppa IT 583 scur ,,schauer, Un- wetter®’ I 190 skir ,,Schauer, Ob- dach*‘ IT 196 skiira IT 196 scurz I 273, 317 scutien I 210, II 400 sctitilon IIT 400 scuwo6, sci IT 196 scuz3zila IT 503 slat I 739 slaf I 739, II 661 slafan I 739 slahan I 743 slah I 759 slango I 248 sléha I 816 sléht I 802 slethha I 802 sléo I 751, 816 sléwa I §16 slidic I 749, 813 slifan I 739, 795, $23 slichan I 802 slimen I 802 slingan I 233, IT 195 slink I 759 slio I 802, II 683 sliofan I 823
12560:késiu, -ti £ 248 kova, koviau I 301 kovas, kdva I 184 kraké I 275 krantas I 286 krdsé I 288 kratjas I 295 krauju I 8 kratika I 275 kraukin, kratikte I 275, 2938 krauklé, kratklé, krduklas I 296 krauklgs I 275 kraupus I 296 krausai, krautil296 kretpta I 292, 293, 318, IT 503 kreju, kriet I 205 kreivas I 221, 317, IT 195, 500 kréslas I 288 kriauklé, kriatiklé, kriauklas I 296 kriauklys £293 kriausau, -yti I 296 krijas, krija I 205 krykscin, kroksti TE BUS ADI krimtt (Zem.) I 198 krintu, kristi I 198 kriokiu, kridkti I 298 krinkti I 275 -_kriusa I 296 krivis I 317 krokiu, krokts T 275, 293 kropti I 289 krosa, krosas I 278 krosnis I 166 krotai, krotos I 286 kriva I 8 kruwintas I 294 krtwinu, kriwinas, kruvinis I 294 krusu, kruéstr, krusa I 296 kiidas, kidikis I301 kugis I 301 kiigis I 263, 306
12701:pratesa IT 376 pravértéti IT 214 prazulnas I 448 pré IT 351 prédai II 353 prikimbu IT 487 prisimuoléti IT 102 protas I 711 put, pusti IT 354, 392
13621:vosta, vrosts IT 765 vretét, IIT 214, 765 vrechs IT 762 vrocho, vrésti IT 762 vrotati, vrokdati
13698:grotand I 627
14059:rota II 224, 757
```


## [2026-09-14T01:22:41.464Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KNT leaf 191 (p176) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==192' KNT.txt | head -80",
 "description": "Kent p.176"
}
```


### [2026-09-14T01:22:42.622Z] TOOL RESULT

```
=== KNT leaf 191 (p176) ===
 formed like Gk. &exero to root *segh-, ёттєтө to root *pet- (JAOS 62.269; 855.IT, §103.I1).
amala adv. ‘thence’: demonst. stem ama-, found (though rarely) in Skt., + adv. -tos, as in Skt. tátas ‘thence’, Gk. ёктоѕ ‘outside’, Lt. caelitus ‘from the sky’: Buck, Lg. 3.4-5; Jn. quoted by Gray, JRAS 1927.101: ef. Kent, JAOS 51.231. Hardly, with Gray, JRAS 1927.99-100, and Hz. ApI 65-6, the same as Skt. abl. asmat remade to *asmatas, with -tos ending. DPh 6, 7; DH 5, 6.
отида, see maub-.
ay- vb. ‘go’: Av. ay- (pres. aiti), Skt. i- (pres. éti), Gk. «о, Lt. it: conj., §208. Cf. also youviyd-. айу ($69) DZe 10. aii imf. (§72, 6228.11) DB 1.98; 2.67; 3.35, 43.
à + ay- ‘come’: aya"là 3d pl. imf. mid. ($181, $208) DZe 11.
ali- + ay- ‘go beyond, go along’: aliyäiš imf. (872, 8122, 5298.11) DB 3.73.
upa- + ay- ‘go to, arrive at’: [ulpayam Ist sg. imf. (8122, §131, 8226.IT) DB 1.91f.
169
upari- + ay- ‘behave, conduct one's self’: upa- riyü[ya]m 1st sg. imf. ($122, §226.1T) DB 4.64f.
nij- + ay- ‘go forth’: nijäyam Ist sg. imf. ($120, $208, $226.IT) DB 2.64. |
pati- + ay- ‘come to, come into the possession of’: patiyãiša” За pl. imf. ($140.11, $208, §232.- П) DB 1.18, 18.
тата + ay- ‘go forth, proceed’: paraidiy 2d sg. тту. (§122, §181, $2371) DB 2.30, 50; 3.14. paratta 2d pl. іту. ($181, §208, $231, $237) DB 2.20, 83; 3.58, 85. parailé npm. past ptc. ($122, 8242, 59421) DB 2.32f, 38, 43, 52, 58; 3.65.
pari- + ay- ‘go around before, respect’, with inst.: pariyaitiy XPh 52 (written -ait?, §52.1; wrongly interpreted by Hz. AMI 8.66f, ApI 219). paridiy 2d sg. imv. (§122, $131, $208, 237.7) ХРЬ 49 (also wrongly interpreted by Hz. ibid.). apari- yaya” 3d pl. imf. (with double augment, $208) DB 1.23 (not ápariyàya, for *ahapa-, to Skt. saparydti ‘worships’, despite Bthl. Stud. 2.67, AiW 1765: not to be emended to upariydya, as done by WBn xi, Wb. KIA 12); see JAOS 35.331-6, Lg. 13.303.
ayaumani- adj. ‘untrained’: neg. a- (§67.J) + yüwmani-. ayüu(ma)ini$ nsm. DNb 59 (852.VT; with epenthesis of -2-, $127, as in Avestan).
dyadana- sb. ‘sanctuary’: deriv. ($1471) of prefix à + vb. yad- ‘worship’. dyadand apn. DB 1.63f.
ar- vb. ‘move, go or come toward’: Av. ar-,
Skt. r-, Lt. oritur ‘rises’; pres. inchoative (897), OP rasa-, NPers. räsäë, Skt. rechdti, pIE *rske- (and *re-ske-, $32). See also arta-, hamarana-. arasam \st sg. imf. (§212) DB 1.54; 2.28, 48, 63.
ava- + ar- ‘go down to, arrive at^: avd{rasam] Ist sg. imf. ($131) DB 5.23f; [ајратазат DSf 24.
parü + ar- ‘come to, arrive at’, with acc. of place and abiy + acc. of person: parérasam Ist sg. imf. ($131) DB 2.65. parārasa imf. DB 2.22, 32, 52; 3.3, 44. |
ni- + ar- ‘come down, descend’, with abiy and acc. of place: nirasãtiy subj. (5140.1; §289) DPe 24.
Arakadri- sb. ‘Arakadri’, a mountain in Persia (832): Elam. ha-rak-ga-tar-ri-18, АКК. a-ra-ka-ad- ri-*; a possible etymology, Foy, KZ 35.62. Ara- kadri$ nsm. DB 1.37.
Árabüya- sb, ‘Arabia’; @ (provinee of the
170
Persian Empire (532, §75.V, 5166.111); also ‘Arab’, ethnic to same: Elam. har-ba-ia, Akk. a-ra-bi, Gk. "Аравіа. (1) ‘Arabia’: Árabáya nsm. DB 1.15; DPe 11; DNa 27; DSe 26°; DSm 7°; XPh 25 (2) ‘Arab’: Arabiya пет. A?P 18.
araían- sb. ‘cubit’ (832, §82, S155.ID): Av. nom. dual araénd, to Iran. stem aratan- атап, ef. Skt. aratnt-; Lg. 15.176-7 (borrowed from Iran. into General Slavic as aršin ‘ell’, Wb. AfOF 7.41, against Berneker, Slav. etym. Wrtb. 31, who thinks it borrowed from Turkish); cf. also Bv. Orig. 105. arasanit ipm. (§187) DSf 26 bis (not nom. sg., with Ву. Gr. $308, $318: not асс. pl.).
arika- adj. ‘evil, faithless’: deriv. (6146.11) of *asra
```


## [2026-09-14T01:22:49.887Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor n in 194 195 196 197; do echo \"########## leaf $n\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' KNT.txt | head -c 3000; done",
 "description": "Kent leaves 194-197"
}
```


### [2026-09-14T01:22:51.083Z] TOOL RESULT

```
########## leaf 194
t’).
-
LEXICON
ч.
Атах$аса- sb. ‘Artaxerxes’ (Т, son of Xerxes; П, son of Darius II; III, son of Artaxerxes II): Elam. ir-tak-Sa-a8-Sa, Akk; ar-tak-Sat-su, Gk. ’Aprakeptns (§29.n2, 530). From arta- ‘justice’ + т$аса- ‘kingdom’, ‘Having a kingdom of justice’ (hardly, with Nyberg, Rel. 352, ‘whose zšaça- de- rives from aría-); imitation of Xšayāršā, acc. -üm, explains the long vowel of the ultima in the nom. and acc. ($78, §161.[b; decl, §172, $187). Artazšaçã nsm. А:Ра 9°, 17°; АЧ; D'Sb 3°; A’Sa 1; A’5b; A*8c 1°; А4 1, 2; А? На 1; A*Hb; Ае 7, 156; A*Pa 5 (as acc., 52476), 8, 12 (as gen., $313.IT), 13 (as gen.), 14f (as gen.), 15f (as gen.), 21, 231; AVsb-d. — Ardaxcasca ($49; or -Sda) AVsa. Arlax áagüm asm. АІРА 51°; А%8а 4; A?He 5; S£ 2-4. ArtaxSacahyé gsm. D'Sb 2°; Artaxíafrahyà (Tm. Lex. 54) A?Ha 2f, 3; Arlazíagühya ($53) A’Sa 2 bis; A?He 101, (аз nom., 5313.1) 11.
ariàvan- adj. ‘righteous, blessed’, denoting the blissful state of the true religionists after death: identical with Av. asavan- ‘characterized by Arta or Asha, righteous’, Skt. rldvan- ‘true to sacred Jaw’ (cf. Hz. Ар! 289-93); from *ria-, OP arta-, with lengthened final vowel, + ad]. suffix -van- ($30, $155.IV). атара nsm. (8124.5, $187) XPh 48, 55.
Artavardiya- sb. ‘Artavardiya’, one of Darius’s generals: Flam. ?r-du-mar-ti-ja, АКК. ar- ta-mar-2i-ja. From arta- + vard- ‘to work’ + adj. suffix ($80, §31, §144.1V, S160.Ia): ‘Doer of Jus- tice’ (not from vard- ‘to increase’, Skt. vardh-, be- cause of -z- in АКК. and in Aram. "rívrzy, аз Bv. BSLP 31.2.66-7 shows). Artavardiya пет. DB 3.30f, 33. Artavardiyam asm. DB 3.36, 43.
Ardaxcasca (or -Sda), probably miswritten for Arlax&acü, q.v.
ardata- sb. ‘silver’: Av. arazata-, Skt. rajatá-, cf. Gk. &pyvpos, Lt. argentum. (S30, §88, $145); Yezdi ait ‘silver’ has Iran. ar-, not r- (Ву. BSLP 30.1.60, Origines 12). See also ardastdna-. arda- tam nsn. DSf 40.
ardastāna- sb. ‘window-frame, window cor- nice’: arda- ‘light’ as in OP ardata- ‘silver’, Skt. rajatd- ‘white’, rjrá- ‘red’, Gk. àpyós ‘shining’ + stāna- ‘place’ (831, §160.Ib; Foy, KZ 35.48; hardly as with Bthl. AiW 193, or Hz. Ар! 74-6); ‘light- place’. ardasténa nsm. DPc.
Ardumanis- sb. ‘Ardumanish’, ally of Darius
171
against Gaumata: АКК. a-ar-di-ma-ni-i$. From ardu- ‘upright’, GAv. arazu-, Skt. rjú- + manis-, see manah- ‘mind’ (§34, $68.11, §124.4, §156.IV, $61.IIa, 8185.11): ‘Upright-minded’ (hardly Ardimanis- ‘dessen manah- glühend ist’, as taken by Nyberg, Rel. 352).  Ar[duma]|n[is] nsm. DB 4.86.
Arbairà- sb. ‘Arbela’, a city in Assyria: Elam. har-be-ra, АКК. ar-ba-’-il, Gk. "Apfiqia. (§31, §107, 6106, $166.Ш). Arbazrayá isf. DB 2.90.
Armina- sb. ‘Armenia’, a province of the Persian Empire (§31, §106): see also under Ar- miniya-. Árminansm.########## leaf 195
пат. AsH 1, 5; DB 1.4f; DBa 6; DSf 13; XPf 19, 20; A’Pa 20 (as gen.; §313.1[). Aršämahyā gsm. DB 1.3, 5; DBa 4, 6.
arstà- sb. ‘rectitude’ ($80; $93): haplologie for *aršta-tā- (8129), abstract to arSta- ‘upright’ (8145), pIE *rĝ-ta-, with zero-grade to root *rej- (8122; Mt. Gr. $123, $125), cf. Av. arštāt- ‘goddess of rectitude’, OP ardu- in Ardumani&-, rüsta-; or merely fem. *rĝ-iã- as abstract (Bv. Gr. $123, $125). атат asf. DB (4.64.
172
аг$Е- sb. ‘spear’ (830): Av. arsti-, Skt. rstt-, pIE *rs-ti- ($152.IIT, $179.IIT), to root in Skt. drsatt rşáli ‘rush, push’. See also ár&tika-, arsti- bara-. ат] nsf. DNa 44.
Grshka- sb. 'spearman': from ar&- ‘spear’ with vriddhi (as in wárttika-, $126), + suffix -ka- ($146.10). ага пет. DNb 44.
arslibara- sb. ‘spear-bearer’: aršti- ‘spear’ + bara- ‘bearer’ ($122, §143.V, §160.Ia). arStbara пзш. DNe 2 (written 59519, $51; the original draft seems to have had ате; on proofread- ing, the $° which was to have replaced the s* was wrongly substituted for the a, and this falsely cor- rected orthography was inscribed on the rock).
‘ava- demonst. adj. and pron. ‘that’ (5260.11, $264): Av. ava-, Skt. gen. du. avós, oCS орй; see also avd, араба, avadà, avapard, avahyarüdiy, pasiva. Decl., $200.
avam asm. DB 1.21, 22, 31, 40, 49, 57, 76, 80, 84, 88; 2.4, 4f, 12, 17, 20, 25, 30, 31, 35, 40f, 46, 50, 51, 55, 61, 84, 87, 94, 97; 3.4, 7, 12, 14, 14f, 17, 27, 38, 45f, 47f, 50, 56f, 58, 62, 67, 82, 85, 89; 4.38, 66 bis; 5.6°, 27; DNa 2; DSe 2; DSf 2°; DSt 2°; рле, 1; DE 3; XPa 2; XPb 3; XPe 2; XPd 2; XPf 2, 28; XPh 2, 37; XE 4; XV 3; А?Ра 2f^; A’H 3; A*Pa 2f. avamsam DB 2.20, 821; 3.31, 85; 5.8. auahya gsm. DB 1.29; 3.70; 4.48f. алапа absm. DSf 81. араш npm. DB 5.15, 31°; DSf 48, 50°, 51, 53, 54. avaiy apm. DB 2.77; 4.69. avaišām gpm. DB 4.51.
avém asf. DSE 27; alva]m-c* (= -ciy, 852.1) DB 5.26; ava as asf. (856.V) XPh 33. [ора npf. DNa 39.
ava nsn. DB 1.20, 447; DNb 10, 11, 20, 22; DSf 42. ava-maiy DSj 4; 051 46. ava-di$ DNa 21; DSe 20°; XPh 19. avaš-ciy (89. VT, $105) DNb 55. ava asn. DB 1.62; DNa 20, 37, 49; DSa 4; DSe 19°, 32°, 34, 44°; DSf 20°; XPa 16; XPb 25; XPf 39, 42; XPg 10; XPh 18, 42. ava-taiy DB 4.76, 79. avas-cty DNb 5f, 57; XPa 20; ХРе 14; ХРЇ 48. арапа absn. DSe 88. avand isn. XPh 49, 51f.
’ava- prefix ‘away, down’: GAv. avd, LAV. ava, Skt. dva; with verbs ar-, *kan-, gam-, jan-, à-jan-, !rad-, sta-, hard-. Cf. JAOS 62.274-5,
avd adv. ‘thus’, correlative to уаба: perhaps isn. of !а0а-, but more probably error for атаба ($52.УТ), by omission of one character, as taken by MB Cr. $59; see also avdkara-. DB 4.51.
OLD PERSIAN
avakanam, see ?kan-.
avdkara- adj. ‘of such sort’: avd ‘thus’ + kara- ‘doer’ (§160.Ia; wrongly Hz. ApI 101-3, who takes -kara- in avükara- and ciyükara- not from kar- ‘do’, but as kara- ‘time’, as in haka########## leaf 196
's avabäštā adj. apm. 'thus standing".
avadà (ie. avadá) adv. ‘there, then’: LAv. атаба; from 'ava- + suffix seen in OP «dà (319.1). Usually resumptive of an immediately preceding place-phrase, which is thus made locative (so al- ways in DB except 1.85, 88; 2.24; 3.74; 4.81; 5.24, 28). See also avadasa.
(1) ‘there’: DB 1.85, 88, 92; 2.9, 23, 24, 28, 34, 39, 44f, 54, 59, 66, 96; 3.5, 23, 34f, 44, 61, 66; 4.81; 5.24, 28; XPh 40. avada-Sim (8135) DB 1.59; avadd-Sim DB 3.74; avada-šiš DB 3.52.
(2) ‘then ’: DNa 42.
avadasa adv. ‘from there, from then’: avadd- + abl. -ša (5191.1; ВЫ, AiW 170, with lit.; against his view, Ву. Gr. §325), always after hacd. (1) ‘from there’: DB 1.37; 342, 80; DSf 47. (2) ‘from then’: DSe 47f.
LEXICON
avaparü phrasal adv. ‘along there’: ava asn. + postpos. pard (S191.IV). DB 2.72; 3.792.
avastü- sb. ‘leather’ (König, Klotho 4.45-6): etymology uncertain ($145). avastlälylä] 15. DB 4.89f (JAOS 62.267); hardly стаз уот) as read and restored by KT, which could be only an un- augmented imf. of ava- + stā-. Probably not а reference to the Avesta, as suggested by Wb. ZDMG 61.730.
dvahana- sb. ‘village’ (5166): deriv. (8147.1) of à + vah- ‘dwell’, Av. vah-, Skt. vas-, Gm. Wesen ‘being’. dvahanam DB 2.33; DSf 46.
avahar|da| DB 2.94, see hard-.
avahya- denom. vb. ($217) ‘ask for help’: Av. avahya-, Skt. avasya- in dsm. pres. ріс. avasyaté (RV 1.116.283), to Av. avah- ‘aid’, Skt. dvas- (Jn. JAOS 27.190, MB Gr. §209, Bv. Gr. $193). pali- + avahya- ‘ask for help’: patiydvahyaty ($140.11) Ist sg. imf. mid. DB 1.55.
avahyarddty phrasal adv. (§191.1V) ‘for this reason’: avahyd ($185) gen. of !ava-, + rüdiy ‘on account of’, q.v. For phrasing, cf. Gk. rovrov évexa, robvexa, Lt. huius ret causd; JAOS 35.322-9. DB 1.6f, 51; 4.47, 62; DBa 9f.
asa- sb. ‘horse’ (590, $143.IIT): Med. aspa-, Av. aspa-, Skt. déva-, Lt. equos, pIE *ekyos. See also Asagarta-, asabüra-, aspa-. asam asm. (col- lective, $255) DB 1.87.
Asagarta- sb. ‘Sagartia’, a northwestern prov- ince of the Persian Empire (§29.n2, $81): Elam. ad]. a&-Sa-kar-tt-a, Akk. adj. sa-ga-ar-ta-a-a, Gk. Yayapria. Probably asan- ‘stone’ (with Med. s < pIE Ё; $9.1, 587) + *garta- ‘cave’ (Skt. gdria-), ‘Land of Stone-Cave Dwellers’ ($161.10, §166.1; Bthl. AiW 207, zAiW 119-20); hardly asa- ‘horse’ (with OP s < plE ky, §90) + *garta- ‘wagon’ (Skt. gária-), ‘Land of Horse-drawn Wagons’. See also Asagartiya-. Asagartansm. DPe 15. Asagartam asm. DB 4.23. Asagartaty lsm. DB 2.80f; 4.22; DBg 8f.
Asagartiya- adj. ‘Sagartian’: adj. to preced-
ing (§144.111, $159). Asagarfiya nsm. DB 2.79;
4.20f.
asan- sb. ‘stone’: plE *aken- (§9.V, $87, §155.1), ef. asman-. See also Asagaria-. ай (8124.5, $187) nsm. DSf 40f; but see also under daru-.
173
asabára- sb. ‘horseman’: NPers. suvdr, cf. also Tedesco, ZII 2.40-1; asa- ‘horse’ ($126) + bára- 'earri########## leaf 197
3. asmanam (853) A?Pa 3.
ašnaiy adv. ‘near’, lsn. of ašna- ‘near’ (Hz. Ap] 98-9), Av. dsna- ‘near’, in loc. dsnaé-ca, asne ‘near’, abl. asna ‘from near’; from pAr. root end- ing in $ or 2 (pIE Ё or ў: Skt. aánóti ‘attains’ and djatt ‘drives’ hardly suit); not *à-zd-na-, pte. to à + *had- ‘herangehen’ (Bthl. AiW 1755; but *had-, which always has prefix d, is only a semantic vari- ation of thad- ‘sit’), cf. Skt. dsanna- as adj. ‘near’ (Bthl. AW 220). Possibly from plE *afijh- ‘choke, throttle’, cf. Lt. атаб, Gk. &yxw, sb. Lt. angor, Av. azah-, Skt. qhas-: *afijh- + pte. -no- (806, §147.1, $191.11I, $243); for semantics, cf. Gk. &yx« adv. ‘near’ (JAOS 62.276-7). Not ‘on the march’, to pAr. root *aé-, Skt. djatt, Lt. agit (Bthl. А 264); nor ‘m friendship’ on the basis of the Elam. kanna ети git (WB; KT); nor ‘at peace’, cf. Av. dxsitd ‘peace’, dx Sta- ‘peaceful’ (Ву. BSLP 31.2.67-9). Elam. kan- recurs as the translation of dausid ‘friend’, but this meaning eliminates only ‘on the march’, since ‘friendship’, ‘peace’, and ‘nearness’ are related ideas. asnaty DB 2.11f; [aSnajiy DB 5.23.
агай adv. “known ОСА: azdà "thus", Phi. ага,
174
Skt. addhá ‘surely’, from pAr. *adzdhà (885); cf. MB Gr. §118. DB 1.32; DNa 43, 45; DNb 50.
tah- vb. ‘be’: Av. ah- Skt. as-, Gk. tert, Lt.
esl, Gt. ist, pIE *es-. See also hafya-, А@їуй- bau$na-. Conj., $208.
amiy ist sg., Av. ahmi, Skt. dsmz, Gk. Lesb. tume, Att. eui, NEng. am (5118.11, $226.1): AmH 9; DB 1.12, 39, 53, 75, 79; 2.10, 15, 80; 3.25, 81; 49, 11, 14°, 17, 19, 22, 25, 27, 30; DBb 5, 7; DBe 8f; DBd 4f, 7; DBe 6, 9; DBE 4f; DBg 7f; DBh 5f, 9; Рві 6, 10; DB} 5; DNa 35; DNb 6f, 7, 8, 1f, 13, 15, 26, 27, 34, 40, 42, 43, 44, 51; Die Т; A? He 18.
азу, Ау. asti, NPers. dst, Skt. ásti (5116, 5228.1): DB 4.46, 51; DNb 54f, 56; DSe 37; XPh 30.
a'mahy, Av. mahi, Skt. smds-1, Gk. Dor. dues 8118.11, §230.1): DB 1.7f, 11; DBa 12, 18.
ha"tiy 3d pl, Av. honti, Skt. sánti, Gk. Dor. iy i, Ове. sent ($89, §122, §232.1): DB 4.61, 63°.
Gham ist sg. imf., Skt. ham, Gk. Hom. ўа (867.II, §122, 6226.1): DB 1.14; 2.6, 12; 377; 4.63 bis, 64. алат XPh 15f ($53, $131; hardly with Hz. AMI 8.65, ApI 63-4).
аһа imf. *éset (5228.11), but Av. às from *ést: DB 1.21, 22, 29, 30, 36, 45f, 48, 62, 86, 89; 2.13, 181, 19, 24 bis, 94, 95; 3.8, 30, 70; 4.8; 5.20; DNa 38; DSe 32°; DSf 16, 57°; DSj 3°, 4, 4^; DSI 5; DZc 19°; XPF 18, 19, 22, 30, 38; XPh 35, 42.
dha" 3d pl. imf., Skt. dsan (5239.1: §274.n1): DB 1.8 (8259), 10, 38, 42, 56, 90, 96; 2.27, 36, 42, 47, 56, 70, 98; 3.19, 40, 47, 63, 69, 89; 4.51; 5.15°, 31°; DBa 18, 16; DNa 39°.
üha"tá За pl. imf. mid. ($236.11, §274.n1) DB 1.19, 58; 2.77; 3.75, 90°, 02; 4.81; XPf 29. алача (636.1Уе) DB 3.49, 51.
ahaniy 19% sg. subj., Skt. ísánz (5226.1): XPh 47, 48 (-d- extended from rest of tense, acc. to Ogden ap. Kent,
```


## [2026-09-14T01:23:00.256Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n 'uradara\\|ura&a\\|urafa\\|Urafa\\|u-ra' KNT.txt | head -20\necho \"=== leaves 199-201 ===\"; for n in 199 200; do echo \"#### leaf $n\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' KNT.txt | head -c 2500; done",
 "description": "Kent search uratha"
}
```


### [2026-09-14T01:23:01.383Z] TOOL RESULT

```
1052:II. OP 6 from pIE ih: pIE *pnihi-, OP acc. рабт ‘path’, Skt. pa6t-. pIE *rotho-, OP u-raba- ‘having good chariots’,
1778:IIT. With no obvious simpler nominal or verbal form: ama- in Arsdma-, asa- aspa-, u-ba-, poss. ^upa-, kaufa-, kara-, daiva-, darga-, naiba-, Parsa-, pisa-, Máda-, raba- in u-rafa-, varka- in Varkána- and Varka-zana-, Saka-, späda- in Taxma-spáda-, spára- in Vdya-spara-; the restored hana- in hana- {й-; mayüra-, of uncertain etymology; the pos- sible vāra- in ^U-vára-zmi-.
1806:Expressing abstracts (actions): fem. fra-má-nà-, loc. adv. aS-naiy, adj. *u-rada-na-, yà-na-, vaš- na-, ham-ara-na-; possibly fem. Patt-graba-né-, becoming a place-name.
1816:I. The suffix -ra-, sometimes primary and some- times secondary, appears in agra- whence agriya-, A*u-ra-, tig-ra-, personal name @uz-ra-, 6ü-ra- in Güra-vühara-; adj. dü-ra-, whence adv. nü-ram; the uncertain ^u-raBa-ra-. Problematic, and perhaps not Iranian, ѓасата- dacara-. On vazra- in vazra- ka-, vàhara- in 8üra-vahara-, ратіата-, see $154.I.
4346:9 bam : tya : urafaram : waspam : umartiyam
4929:Auramazdāł- sb. ‘Wise Lord, Ahuramazda’, supreme deity of the Zoroastrian religion: Av. пет, ahurd mazda, РМ. óhrmazd, NPers. hormizd; Elam.. u-ra-más-da., Akky u-ra-ma-az-da. ü-ri-mt-
5075:Arminiya- (1) adj. ‘Armenian’, (2) sb. (Ar- menia’, a province of the Persian Empire: Elam. har-mi-nu-ja, АКК. u-ra-aS-tu, Gk. Ариела. Аа). to Armina- ($144.11).
5195:urala- adj. ‘having good chariots’; Skt. sura- tha- as man’s name: u- ‘good’ + raba- ‘wagon’, Av. raba-, Skt. rdtha-, Lt. rota ‘wheel’ ($143.11). See also urafara-. ‘urabd-cd apn. as sb. ‘good chari- ots’ DSs 5.
5196:urafara- adj. ‘having good charioteers’: deriv. of urada- ($148.1). [u|raüaram asn. DSp 3 (Bv. BSLP 33.2.0451 and Hz. AMI 4.126 restore |f\raBaram).
5294:Küru- sb. ‘Cyrus’, founder of the Persian Empire: Elam. ku-rag, АКК. ku-ra-a$, Gk. Коро; (§164.V). Küru$ пэт. CMa 1; CMb 1; CMe.
5700:frafara- adj. ‘superior’: fra- + variant com- par. suffix -thara- seen in Av. fraéara- ($1491, 6190.11; Wb. ЖА 41.319; Bv. 33.2.150-1, 34.1.33-4, Hz. AMI 4.126-7, 8.3940, ApI 166-7), cf. superl. -thama- in Skt. prathamd- ‘first’. Cf. also uradara-. — fra&aram asn. XPf 26f, 37.
=== leaves 199-201 ===
#### leaf 199
DB 1.34f, 41, 461; 2.74, 88f; 5.19f, 35; DNb 30, 37, 40f, 43, 45; XPf 19f; XPh BAL.
щй AsH 13; DB 1.34 bis, 34f, 41 ter, 46 bis, 47, 57, 67, 77, 85; 2.3, 4, 18, 74 ter, 77, 81f, 87, 88, 89, 92; 3.30, 47, 48, 50, 58, 74, 77 (written ud, §52. VI), 88, 90, 91; 4.7, 56, 61, 62, 75 bis, 79, 89, 91 bis; 5.11, 12, 19, 20°, 28°, 31, 35 bis; DPd 15; DPe 18, 14; DNa 53; DNb 3f, 26, 27, 28, 30 bis, 37 bis, 40f, 41, 43 bis, 45 ter; DSe 28°, 51f; DSf 13, 28 bis, 29, 33, 35, 36, 37, 40, 44 bis, 48, 50, 52, 55, 57; Обр 2°; DSs 7°; DSt 9; "рле 11; XPa 19 bis; XPb 24, 30; ХРе 13 bis; XPd 19; XPf 19f, 20, 39, 46, 47; XPg 5, 11; XPh 24, 35, 38, 41, 48, 53, 54, 55, 58; Хе 5°; XV 20, 27°; A'Pa 24°: A%Sa 4, 5, 5°; ASe 5; A’Sd 4; A’Ha 5°, 6, 6f; A?He 19; A*Pa 25 bis, 26.
utü-maiy АЗН 12; DB 4.46 (visible to Cameron; ef. note ad loe.); DPh 10; DNa 52f; DH 8; XPb 29; XV 26f°; А?Не 20. utà-taiy DB 4.56, 58, 73f, 75, TH, 79. utā-šaiy DB 2.74f, 89. ша-&т DB 2.13°; 5.18, 26. иій-4ат DB 3.57; 5.15. ulá-di$ DNb 46f.
ula-maiy (§135) DSe 51°; DSf 58; DSj 6°; DSt 9°; XPa 15, 18f; XPd 18f; XPf 41, 45f; XPg 14; XPh 58 (space for w left blank; Lg. 13.303); XSc 5^; A'Pa 23°; Аа 4. uta-Sem (8135) XPh 34, (In restorations there is almost always un- certainty between utà- and uld-.)
Utüna- sb. ‘Otanes’, ally of Darius against Gaumata: Elam, fu-ud-da-na, Akb &»mi-it-la-na-" ,
176
Gk. 'Ürávgs; perhaps u- ‘good’ + tāna- to root tan- ‘stretch, extend’ (§164.II), Av. Skt. tan-, Gk. telve, Lt. tendit, cf. Skt. tdna-m ‘offspring’: ‘Hav- ing good posterity’. [апа] nsm. DB 4.83.
utava- adj. ‘strong, in health’: u- ‘good’ + deriv. of tav- ‘be strong’ (§122). utava nsm. DB 4.71f (emendation of HK, ApKT 1.63, 2.29, for KT’s detse, with first and third characters very faint; $541).
ubanuvaniya- sb. ‘good bowman’: u- ‘good’ + Sanwaniya- ‘bowman’. wudanwaniya nsm. DNb 42.
ud prep. and prefix ‘up’, becoming Iran. us- uz- before dentals ($85): Av. us- uz-, Skt. ud, pIE *ud (and *üd in NEng. out, NHG aus): ud with verbal root раф, us- in ustaxand-, u(z)- in uzma- (S84).
ира (i.e. upd, cf. 5140.1) prep. and prefix ‘to- ward’: Av. ира, Skt. úpa, Gk. iad, Lt. s-ub ‘under’, pIE “иро.
(1) Prep. with acc., ‘under, with, m the time of (hardly ‘belonging to’, as taken by Hz. ApI 353): DB 2.18, 3.30; A’Sa 4; А?Ра 23; Sf.
(2) Prefix, ‘under’, in Upadarma-; ‘toward’, #### leaf 200
 by Hz, ApI 71-2).
ufraSa- ufrasta- adj. ‘well punished": u- ‘well’ + pte. fraSta- or frasta- (893) ‘questioned, investi- gated? to root fraó-: pIE *su-prekto- (§33, 75, $242.II. — ufrasiam asm. DB 1.22, 4.66f; ufra&lam DB 438. ufrasa-diy apm. DB 4.69 (JAOS 35.351-2, ef. Bv. Gr. $845; not loc. ufrastë + prep. айту, as taken by ВШ. IF 12.110, A1W 60-1, Mt. Gr. $818).
uba- adj. ‘both’: GAv. uba-, Skt. dual ubhá(u), pIE *ubhó(u), cf. Gk. &p-dw, Lt. ат-00 ($143.11). ubà ndm. ($189) DSf 14; XPf 21.
ubarta- adj. ‘well-borne, lifted, esteemed’: u- well’ + barta- ‘borne’, pte. to bar- ‘bear’, pIE *su-bhrio- (830, $122, §242.1). ubartam asm. DB 1.21f;4.66.  ubartàm asf. DB 4.88. On meaning, cf. Altheim, ZII 3.33-5: hardly as taken by König, RulD 69.
[U]mamaita, see Atamaita-.
umartiya- adj. 'eontainig good men’: u- ‘good’ + martiya- ‘man’. umartiyd nsf. AmH 6; DPd 8f. wmartiyam asn. Р 11f; DSm 4°; DSp 3°; DZc 4.
Uyamad- sb. ‘Uyama’, a fortress in Armenia: Elam. t-i-ja-ma, Aram. huyaw (Cowley, AP 251 line 4, 257). Uyamà nsf. DB 244 (all charac- ters visible to Cameron),
urala- adj. ‘having good chariots’; Skt. sura- tha- as man’s name: u- ‘good’ + raba- ‘wagon’, Av. raba-, Skt. rdtha-, Lt. rota ‘wheel’ ($143.11). See also urafara-. ‘urabd-cd apn. as sb. ‘good chari- ots’ DSs 5.
urafara- adj. ‘having good charioteers’: deriv. of urada- ($148.1). [u|raüaram asn. DSp 3 (Bv. BSLP 33.2.0451 and Hz. AMI 4.126 restore |f\raBaram).
uradana- adj. ‘of good regulation’: u- ‘good’
+ deriv. of rad- ‘direct’ (§122, $147.I): see Hz. Ар1 206-7 (but he is wrong in drawing in also Lt. lé law). uradandm así. ОХЬ 23.
-
ре
LEXICON
tuva- refi. pron. ‘self? and poss. adj. ‘own’ (8118.1V): Av. z"a-, Skt. sva-, Gk. € and ds, Lt. sé and suos, pIE *sye and *suos (5148.11); in wada-, wvăipašiya-, wdmar kyu-.
watpasiya- adj. ‘belonging to self’ (wrongly ‘wayward’, Sen 246), nt. as sb. ‘own possession’: Ау. x’aépaibya- ‘own’; OP uvai-, nom. of wa-, as in Skt. svay-dm ‘self? (MB Gr. §293), + pAr. *natia-, formed on pIE *poti-, Av. рой ‘master, husband’, Skt. pati-, Gk. тоса ‘husband’, Lt. potis ‘able’, Lith. pats ‘self’: pIE *suoi-potio- (858, §143.- II, $152.11, $161.1Ib). watpasiyahya gsn. DNb 15.
 wüipasiya-, same as preceding, with vriddhi in initial syllable (§126; MB Gr. §298); but wai- may be an error for uvai-, or w
```


## [2026-09-14T01:23:10.986Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n 'raestar\\|raestá\\|ra9a\\|raQa\\|raba-\\|ra&a' BRT.txt | head -20\necho \"--- search Wagen ---\"; grep -n \"'Wagen'\" BRT.txt | head -10",
 "description": "Bartholomae search for ratha"
}
```


### [2026-09-14T01:23:11.060Z] TOOL RESULT

```
9599:•)  Vgl.  Stein  IA.  15.  21.  Er  liegt  nach  Bd. /J,  16  pa  saiasIStt  'in  SaisiJn'.  —  •')  Aus  dem An'ischen  Königshaus,  als  dessen  Heimat  das Gebiet  des  A:-Sees  gilt,  Bd.  31.  7.  —  ••*)  Im See  K.  ruht,  von  gg^jgg /ra&awy  bewacht,  der Same  des  Zara%uitra,  aus  dem  dereinst  die Saoiyanl  entstehen  sollen,   vßl.  unter  xsudru-'i. ,
13561:•  j.  d3r9zLra9a-  Adj.  'der  einen  festen, staiken  Wagen  hat":  taxm^m  ttaotär?m  .  . '■:iwi  YtJ7.i2.
21355:yavö.fra&ah-
22047:•  g.  vaeda-,  j.  'vae3a-  i)  m.  'Finden,  Er- langen, Erwerben':  raäitahe  pdhs  aistnüa 'Itmca  "das  Suchen  und  Finden  des  ge- radesten Pfads"  Y.  68. 13;  —  apayeHrfsd.) ra&anaaÄd  'd>m  Y,_J2.  u;  —  yat  usnam aiiti  'oya  (LS.)  "wenn  er  sich  (in  der  Er- langung sva.)  am  Ziel  seiner  Wünsche befindet"  Y.  10. 13  '>.  2)  Adj.  'der  etwas (Gen.)  verschafft,  zu  erwirken  weiss':  atSm- clt  ahyä  masda  "hwqm  mSAhl  paeurvim 'ihm  "auch  ich  (ja)  habe  erkannt,  dass du  das,  o  M.,  als  erster  zu  erwirken vermagst"  Y.  2g.  i  o  ".
23212:*vaz5.ra9a-
--- search Wagen ---
25078:•  j.  'ra^-a-  m.  'Wagen'*':  gäui  frazarSta (sd.)  aiSqm  "i'äj'fl  (LS.)  YL70,38;  — paiti.- stayata  'ihya  aül  vat>uhi  "es  luelt  an  auf dem  Wagen  A.  . ."  YLr7. 17;  —  akmya 'äa  hvasäna  \yX.48;  —  nöit  ihra  ../ras hyat  .  .  halnyS  '%ö  nsit  uspnpts  draßs YlÄsö;  —  yat  janäni  kitäsptm  'i^e paiti  vagaihyai  (sd.)  YLi^.aS;  —  tarn caxnm  (sd.)  . .  asmatam  ''h3in  ktnnavane . . ti  mg  väitm  ^anjaySnte  spirdasca  mainyui' attrasca  Yt.J(j.  43f.
```


## [2026-09-14T01:23:12.224Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HUB leaf 76 (p66) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==77' HUB.txt | head -60",
 "description": "Hübschmann p.66"
}
```


### [2026-09-14T01:23:13.155Z] TOOL RESULT

```
=== HUB leaf 76 (p66) ===
i — 66 —
601. Zu rdd 'freigebig = phi. rat (vgl. paz. rad% liberality'
Shk. 264) geh5rt arm. LW. arat *reichlich, freigebig,
giitig.
607. Geht rah *Weg' = paz. rah = arm. rah (bei Faiistus
V. Byz.) auf ap. *r5^a- (Horn vergleicht skr. rathya-
Tahrstrasse' von ratha- = zd. ra^a-*Wagen') zuriick, so
kann das Wort im Pehlevi, wo ras geschrieben wird,
in alter Zeit docli nur *r5^, jiinger rah gelautet haben.
Ich glaube dann nicht an ras als neupersische Neben-
form. Bei aspras 'Stadium* liegt die Deutung als Pferde-
weg' allerdings nahe, aber warum heisst es nicht *asprah
anstatt np. aspras, aspraz^ aspres, asprlz (Vullers),
aspres (Schefer, Chrest. pers., vgl. ZDMG. 44, 532),
phi. aspras, aspres (Pahl. Diet. Ill, p. 541), arm. LW.
asparez, aspar^ (g^n. asparisi)? Np. rastan gehort
nicht hierher, da es kein Denominativum sein kann.
608. Np. ruhdyad raubt' aus *rupayati ist wohl von robad
*fegt' aus *raupati zu trennen.
609. Np. raja, raSa *Reihe' scheint mir ein phi. *racak oder
"^rajfaky dagegen np. rada 'Richtung, Linie, Reihe* ein
phi.* ratak vorauszusetzen. Mit rajfa = '^racak Hesse
sich skr. raSana- 'Ordnung, Anordnung vergleichen. Fiir
skr. rdji- *Richtung, Linie' wiirde ich np. "^raz-a er-
warten. Vullers fiihrt ein np. raja {raSa, raza) 'funis
vestibus imponendis inserviens' auf, das = skr. rdjju-
'Strick, Seir sein kSnnte. Vgl. phi. araSak = arajak
'frei von Fesseln' Bdh. 61. 59?
610. Np.rwa? Wange gehSrt nicht hierher.
611. Np. rod weise, tapfer' stimmt in der Bedeutung nicht
zu zd. ratU' 'geistliches Oberhaupt, Herr' = paz. ra3
'master' Shk. 264 = np. rad (rad) 'Oberhaupt eines
Kreises' (Tab. 447). Nach NSldeke ist aber rad bei
F i r d u s i = 'Herr oder 'Held'. Vgl. z. B. Fi r d. 1, 130, 28.
612. Np. razm 'Schlacht' ist = ap. "^razma = zd. rasma
'Schlachtreihe (von Wzl. raz = idg. reg^, vgl. skr.
raju *Reihe'). Der Ubergang von 'Schlachtreihe' zu
'Schlacht' ist, meine ich, begreiflich und iiberdies be-
legbar, vgl. z. B. arm. iakat *Stim, Front, Heerresfront,
```


## [2026-09-14T01:23:26.192Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR>=25050 && NR<=25130' BRT.txt",
 "description": "BRT context around ratha"
}
```


### [2026-09-14T01:23:27.221Z] TOOL RESULT

```
astalnalibyj  N,  707;  —  '/rii'  pt^sbli  ^as- tsisca  .  .  N.  57;  57^  s6\  $4  i-,  4SL, 55''?'i — y^  ha:a  da!vayasnaiiby9..apa.- bara  (sd.)  aya  'frii  N.54;  S4-  /)  Abi:
*kahy'icit  «J  dahmanqm  sai^^räca  (sd.) '/ryd  (statt  NS.J  N.40.'  •{)  Gen.:  yas- nahe  ali'ake  °/ris  aratufris  g-l'^anam  N. 22;  —  vispanqm  gi^anqm  'fris  H.  22; 38,  SQ  (statt  NP'.);  —  agtämtJ(sd.)  'fris yaval  framaratti  N._?<S'i  3g  (statt  NP.), 2/',  2j;  —  °fril  canmanqmca  pasu.- vastranqmca  N.  ^8;  —  ci'aiti  narqm  *ÄaxtJ zaota  (sd.)  °fris  ahumm  vainm  frasrao'- yehe  N.  20.
KompE.  —  "J^l-  Adj.,  zum  V.  fräy- ;  ai,   */r7.
Adj.  —  Vgl.  iralii/rl-  t  —  Pü.:  rcOIAi.  — I  ')  Hds. /rfl-V*-  —  ''  Hds.  ralißh  ratuTöö, I      beide   lasammen    slatt   rafu/rii.    —    1)  Hds.
aralu/r*.   —    4>  Hds.  ralai.    —    S)  Hds.  raiu-
•  y  ratu-fritay-  f  1)  'Zufriedenstellung der  Satav,  an  die  Katar  zum  Zweck ihrer  Zufriedenstellung  gerichletes  Gebet': iiisptm  alavarum  aya  °ta  (LS.  als  Instr.) '' hvävayaahiin  ..paiti.bar3hi  humatiisia  .. Y-5i-4;  —  ahm3k>m  havanklica  'tayalca alavastäica  .  .  yai  saoiyanlqm  asaonqm Vr.  5. 1 ;  —  vispalsqmea  ra'^wqm  vlspa- ttqmla  'iinqm  Yi.g.j; — jaymBsyS  asSis .  .  jaymUsyä  °töis  Vr.i?.6;  —  ra'^walca 'layaica  Vr.  4. 2  (?) ;  —  yS  g.fi  anqm  aii^qm °tim  ava.radoayeiti  N.  43;  —  imqmca urvarqm  *bargsmainfm  /aymüslmla  'tlm mar^rsmia  var>zlmca  damaya  .  .  gaha- nqmca  srad^rim  JaymUiSmca  . .  ra>WJ 'ITm  Y.  22.  3;  — /aymuH^mam  ..  ra'iwJ 'iTm  yazamaide  Y.  7/.  3 ;  —  imqm  ar»hu- yqm^a  *asayqmca  ra'hwqmca  Ülm\fa\  Y, 3.4;  —  besonders  von  den  in  den  ver- schiedenen Tageszeiten  an  die  RatavdAmya (sd.)  zu  richtenden  Gebeten":  ys  rapthwi- nahe  '/a  (I.A.  als  Instr.)  rapi'iwinim  ratüm framaräite K. 4.  5; — yalät pascaita  aorqui °Um  ava.raghayeiii  tanüm  *firydti  "wenn er  alsdann  ein  einziges  der  täglichen  Ge- bete versäumt,  so  . ."  N,  42;   DS.  als
Inf.  sbes.  2)  'die  wegen  Beleidigung der  Ratav  notwendige  Sühne' ■^*:  altalsam ratufril  'tim  *hwfrisaili  "ihnen  schret'bt deijenige,  der  den  Ratav  gegenüber  seine Pflicht  erfüllt  hat,  die  Sühne  für  die  Ratav vor"  N.5j;  52.  [N.6'7;  lies  ratufrii.]
KompE.  —  Vgl.  tralu/ri:   —  Pü, :  rai/rani- mismfi,    Sü.:  gurvatmjnä;    %.  noch  Nq.  3.  —
ob,Google
raS'aestar-
1506
9.  _   i)  VgL  ^ratufri-  a.    —   J)  PüErl.!
•  j.  ratu-frit?e  Inf  "die  Ratav  zufrieden zu  stellen':   yat  pairi  Öansma  hanjasante 3at  r'  ". .  so  dient  das  dazu,  die  /?. frieden  zu  stellen"  N.ö's;  —  coat  niümpm hastnm  (sd.)  atshat  V°"/  N.^/.
Zum  V.  fräy-.    ~  'VgL  ral«fritay:    — fa  ral /ranämih^fh).  —  »  Hds.  fry».
j.  ratHfryät  N.  31:  lies  ratu/rißc.
j,  oäTä  ralufiU  ratu/Hs  tt.So:  lies  «iS
•  j.  ratu-naya-  m.  'Laie'  (im  Gegensatz zu  'ratav):  ratus  'nasin  a^a  'nays  ratüm A.J.  13;  —    myazdavi  ratus  amyazdc n?m     'naim    ayasttim   (sd.J    daste    antara mazdayasnäis  K.3.T,  8-12.
Eig.  'unter  der  Leitung  (*naya-  m.,  zum  V nay;  w.  -riaya-  m.)  des  J{.  stellend'. —  Npü. AäviSt,  Sü.:  Ü^a^  'Schüler'.
•  j.  "ratu'mam-   Adj.   'der   einen  Xa/av besitzt',   stets   neben  ahumani-  (sd.,  auch fdSt.):  •mat  P.jj;    —    <matS  (GS.)  Vr.  j. 5;  —  'irantam  Vr.  2.  7 ;  — +'»10^  (NS.) Vr.  2.  7,
Vgl.  aratav-.  —  Pq.  :  ralBmandih ;  vgl.  lu  a/" manl-.  —  1)  NA.  ralümla;  s.  ahumant.  No.  4.
•  j.  ^atu'mant-  Adj.  'das  Wort  ratav- enthaltend"':  aHai  vaiö..yaf  aAumat{s±) yai  ratumat  Y.  ig.  8.
Pü. :  ralämand,  erl. :  daslawar  daran.  —  1)  Vom /üauoräiVcflgebet.
•  j.  *ratuä.mar3t-'>  Adj.  'der  auf  den Ratav  merkt,  seine  Weisungen  beachtet': 'ta.  (IS.)  dagns^aca  Y. /p.  17.
Zum  V.  2mar.;  «tatt  »ratuSm'  geschr.  —  >i. '.J™/'-  Adj.  —  Vgl.  m)r>%7vane..  —  pü.:  rat öimuri,  erl,:  ^  daslawar  däriti  Sü.:  A««». /I/^i/ai.  _  .)  NA.  trennt
•  p.  rad-  V.,  nur  mit  ava  'verlassen'. Praes.  2  rada-.
i)  'verlassen,  abweichen  von  -':  pähim lyam  rästam  ma  avaradc^  m3  *starav<^ (zS.)  "vom  gebahnten  Pfad  weich  nicht  ab, versündige  dich  nicht"  D.6".6.  2)  'ver- lassen, im  Stich  lassen':  vis'tasfc^..  *avam *kanr  avärada^  (3S.)  Bh.2.  j6".
ai.  rahali  'er  verlisst',  np.  rakad  'er  kommt los  von  -•'),  —  I)  Ergänzung  nach  Fov  KZ. 35.  4z;  VgL  Eü.  Aber  Rl.  JrAS.  ij.  iv  las ai--4-^.  —  1)  S.  noch  /Üs.  lu  'j-ai-..  —  Dass ai.  rahah  mit  rähas-  n.,  jAw.  rasak-  lusam- mengehSrt  {so  zuletzt  FoY  KZ.  ^7.  564),  wird flnrcli  das  np.  Wort  unwahrscheinlich.    Viel-
mehr ar.  *radh-\  ».  'rood-  No.  I.  Wegen  der Bed.  des  np.  Verbums  i.  ai.  raAila-  Adj.,  PHP. lu  rah^aH,  eig.  'losgekommen  von  -'.
•  j.  'ra^-a-  m.  'Wagen'*':  gäui  frazarSta (sd.)  aiSqm  "i'äj'fl  (LS.)  YL70,38;  — paiti.- stayata  'ihya  aül  vat>uhi  "es  luelt  an  auf dem  Wagen  A.  . ."  YLr7. 17;  —  akmya 'äa  hvasäna  \yX.48;  —  nöit  ihra  ../ras hyat  .  .  halnyS  '%ö  nsit  uspnpts  draßs YlÄsö;  —  yat  janäni  kitäsptm  'i^e paiti  vagaihyai  (sd.)  YLi^.aS;  —  tarn caxnm  (sd.)  . .  asmatam  ''h3in  ktnnavane . . ti  mg  väitm  ^anjaySnte  spirdasca  mainyui' attrasca  Yt.J(j.  43f.
*)  rAa-  und  ^äxra-  bilden  nach  Yt.  /p.  43f. lusammen  den  väia-.  Sonach  bedeutet  ru^fl- im  Gegensatz  zu  väia-,  womit  der  Wagen  als Ganzes  gemeint  ist,  insbesondere  den  Wagen- kasten. Unrichtig  Gor.  OK.  391;  vgl.  Vt.  10. 52,  68  U.Ö.,  sowie  die  Komp. KompA,  (j-flifl",  ra%a!',  ra%Bi'),  E.;  Abieil, (s.  anch  hurä'i<va-'\.  —  aL  rälha-  m.;  mp.  ras.
•  j.  'ra'Ö'a-  m.  Name  einer  Pflanze  (?):  ^J °'%Ssca  pasvamdlsca  bammaine  "Äam,- vanniaymü  N.gj.
Ganz  unsicher.  -—  PQ.:  fehlt
•  j.  raö'ae-star-,  rad-ae-ätä-,  ra95i-ätä-'' m.  'Krieger,  Kriegsheld':  ya'ha  «j  taxmS °tä  (NS.)  Yt  13.  67;  —  taxmim  tusim  'ia- nm  Yt  5,  58;  Vyt  26;  —  mihnm  .  .  yim yaztnte  'tärS  Yt.  10.  \i;  j.  53  '> ;  —  mihrfm . .  laxiram  °tam  Yt  70.  140;  112,  25,  102; —  iraosahe  . .  taxmake  .  .  'ta  (GS.)  Y. 57-33;  —  ätari  spmta  'i3ra<yS.)^  Ny.j. 6;  Y.  ä^2.8Gl.  A)insbe3.alsBezeichnung für  den  zweiten,  den  Kriegerstand  (vgl.  unter 'piära-):  shrava  '/i  (NS.)  västryö /ü^qs Asitis'  Y.  ig.  ij;  11. 6,  Yt.i3.89,  V.5.  38, '^•45^i  —  ähravarum  ..'iär>nt  ..vasirJm fsuyantftn  Vr.^.  2;  Yt2, 12;  —  a%auru- naSca  °tüua  västrySica  fiitymte  Yt/p.  8; 7J.88,  V.5.  57,  58;  —  västry^Z  fsuyatas ..  'tä  (GS.)  ..  a'iiaurunS  Y.  13.21.;  — asti  iir  haim  (sd.)  ydha  'tärahe^l  Y.13. 44;  4Si  Vyt  J,  16,  Az.5;  —  vUpe  saya °%äis'ti  (LS.)  "alle  Ausrilstungsgegenstände für  einen  Krieger"  V.  74-9;  9;  —  '^^<»- urunqscä  -tascä  (AP.)  västryas^a  f/uyants Y.  7j.  3;  —  a^aurunqs^a  'tarSsla  (AP.)3) väitryqsca  fiuyants  Vr.^j,  5;  —  hast»ma alahe  ama  'ta  Y.13.2.
Komp.  mit  LS.  im  I.  Glied,  V/ar-  aus  idg. *jtAer;  der  KompForm  von  *ilAiltr-;  zum V.  stä-.  —  ai.  rathcffha-  m.  'Wagenkämpfer'. Utt  IF.  g.  209,  —  Pü. ;  arateUär  (gelW.), 48
dby  Google
ISO?
rad-aestä-
rapaka-
1508
Sü.:  kfotriyai.  —   0  Nor  in  ra%iuti  V.  14.  9.
—  •)  Ungeschickte  Herubernahme  ansVt 1 1 ;  falsch  S  396,  400.  —  3)  Tfaem.
•  j.  raS^eitä-  m.:  s.  unter  rä^aiÜar-
•  j.  raO^kara-  Adj.  (fem.  •kairJ-)  '(einen Wagen,  Wagenkasten  bildend,  d.  L)  wie ein  Wagenkasten  gestaltet"':  ufairi pusam bandayata  artdvT  .  .  asta^aoiäqm  'iair- yam*^  YL5.  n8.
■)  Anders  (falsch)  Gdn.  KZ.  xj.  401  ('uimutig'}, DsT.  ZA.  2.  396  ('en  forme  de  rone').  — ')  Nach  der  ä-DekL,  in  Ausgleich  mit  dem Tothergeh.  Wort.
•  j.  ra^üiä^nin^in  AbsoL  '>  'beim  Dahin- eilen im  Wagen,  beim  Fahren':  ahmt  .  . yim  sästa  daiähSus  .  .  patititim  (sd.)  vä .  .  'mm  vä  YL  75. 50.
Komp. :  raÄo— t-'iwwfu«,  Absol.  lam  V.  ^aS-
—  Geringe  Stelle.  —  »  Bthu  IF.  li.  348.
•  j.  raJhöi&tä-  m.:  s.  imter  rdhaistar-.
j.  ri&iaayäi  N.  ^6:  lies  rae%w:
•  j.  •ra^'wya-  Adj.  (fem.  'ya-)  'was  der gegebenen  Zeit  entspricht,  angemessen  ist, was  sich  zur  gegebenen  Zeit  und  im  ge- gebenen Fall  gehört':  ya^a  'ya  (NSf) vanna  (Sp.  1372  u.)  V.jj.  46;  —  mthnm .  .  yS  .  .  fravazaite  .  .  'ya  (IS.)  *äxra (sd.)  Aaämnff  Yt/0. 67;  —  yas3  ^wa aextö.nämana  yasna  'ya  (IS.)  vom  yazaite Yt  J0.3o;3i3,  56;  —  'yi  uxlä  F.jf.;  — vavan9  buye  'ya  manaaha  'ya  valargAa 'ya  ^aohna  A.  7, 1 1 ;  —  sonst  neben däitya'{sd.):  viovä  däilyqm ..  *yqm  ävisiim ". .  die  in  rechter  Fonn , ,,  zu  rechter  Zeit ach  vollziehende  Weihe"  Vr,  77.19; —  '^*'- yanqm  'yanqm  kvarstanqm  fyao%nanqm varttäi  pairi  a%3ityanam  ard^wyanam vansäi  Yx.15.  i;  —  argdvlm  .  .  yä  .  . iäirümqm  daitim  'wjtn  patma  ava.baraiti ". .  die  den  Umständen  und  der  Zeit  ent- sprechende Milch  .  ."  Y,  6j.  2 ;  —  in  der Rechtssprache  :f/di>V<i  'ya(APn.)/rSrai^ya (sd.)  F.^e.
KompA. ;  E.  —  Ableit  ans  ^raiav-.  —  ü.  vgl. X-tviya-  Adj.  —  Pü.  (zu  V.,  F.,  Vr.  IK,  Y.>! frirö»  -  (lu  Y.  erl.):  j^^  -,  (zu  Vr.  7/): ralVtä;  Sü.  (lu  A.):  ladätarl.
•  j.  "raÄTwya-  Adj.  'die  Hatav  betreffend, zu  ihnen  gehörig  (usw.)':  avi  ratüf  avi  *ya garmU  Vr.  4.  i  (?).
Ableit.  aas  'tatat-.-^  Gini  nnsicber.  —  Pü.: etän  pa  an  tafih  u  ctSn  fia  an  raliA  rasihüA. VgL  dain  Sp.  Komm.  2. 17,  DsT.  2A.  /-457-
•  j-  "galwa  kurs  (sd.)  . .  rad-wyasiufm buxts  ma^e"  FrW.2.2.
•  j.*raSTwyö.varstay-'*  f.  'angemessenes Handeln, Tun':  mananhaica*humaiH  Mt- vasca  huxti  zastayasca  *kvarsti  °ti  natdys (sd.)  aAmi  . .  "bei  gutem  Denken  des Sinns,  gutem  Reden  der  Zunge,  gutem, angemessenem  Handeln  der  Hände  bin ich  . ."  P.  28.
Pä.: /raren  iumiH.  —  ')  Hds.  ara%tB'.
•  g.  raiSya-  n.  'Weg':  data  xratsui  hitv9 '%Jm  stöi  mahyä  rizfng  .  .  sOAlJ  (sd.) ". .  damit  meine  Zunge  einen  Weg  habe . ." "' Y.50.Ö.
Ableit  ans  ra%a:  —  Vgl.  ai.  ratkyä-  f. 'Strasse',  np.  räh  'Weg'.  —  Pü.:  ras,  erL: JrahaxBk.  —  1)  D.  i.  dass  sie  den  fechten W«g  finde.     Vgl.  iSt.  Gdn.  GlrPh.  3.  31.
•  j.,  g.  rap-  V.  'Unterstützung  gewähren, —  finden',  Praes.  3  rapa-,  —  In£ ra/ihräi.
i)  'Unterstützung  geK^hren,  eine  feste Stütze  bilden,  sein  fiir  — '  (Dat);  a)  von Göttern:  rapdisca  tu  HS  äangrmiä  lUtäia Aaiqm  hudästsmä  Y.  47. 4;  —  ahunm mazdqm  d(ä)vanh3m  .  .rapantim  tarhia- nhtm  vispa  *voAü  Y.  yo.  1.  b)  von  Men- schen, gegenüber  den  Göttem  sva.  'ge- treulich dienen,  die  Treue  halten':  at  tsi atrJm  .  .  usJmahl . .  stSi  rapantl  ührä,- avatffam  (sd.)  at . .  daibiiyaniw . .  dirvstä- aSianhitn  Y.j4-4r — *stöi  *rapantqm^^ Ny.j.  10;  —  ayaptä{sA.)..yaii  rapantB daidu  x^äiri  ". .,  welche  die  Getreuen  in Wohfbehagen  versetzen"  Y.  28. 2.  2)'Un- terstützung  finden  bei  — ,  eine  feste  Stütze haben  an  — ',  mit  Gen.:  tat  mei  dsidl ahurä  hyal  matda  rapfn  tavä  "das  schaff mir,  o  Ah.,  dass  sie  an  dir,  o  M.,  eine feste  Stütze  haben"  Y.57. 18.
mit  a  dnwS.  i  a:  vanuAl  Oda  gaidi msi  ä  moi  a'^rapa  "mit  der  guten  Ada komm  zu  mir,  sei  mir  eine  feste  Stütze" Y.4P.I.
Et.?  Ohne  Wert  IF.  a.  il.  —  PS.:  rämFni- lär,  'tSrih,  (an  Y.  4g) :  arämemlär  {mit  neg.  a, Npü, :  bl)i  Sü. :  äiiaaJak,  priOHodatBam,  äntm' daiatiä.  —  ■)  Eine  nngescbickt  verwendete Reminiszenr  ans  Y.  34.  4.  —  *)  Nach  dem Metrum  zu  streichen.
•  j.  rapaka-  Adj.  'eine  Stiitze  bildend für  -,  im  Dienst  stehend  von  — '  (Gen.): a^  (näml.  daxmS)  sJ  asti  daibaitqtn  'AS vupsm  a  oAmOi  yat  alfa  *gainti/ tipaioAa- aüti  (sd.)  V.7."s6.'
Znm  V.  rafr.  —  Pü.:  rämilu.
dby  Google
'S09
rapant-
raoha-
1510
•  g.,  j.  rapant-  Adj.,  PPA.:  s.  rap-.
•  j.  ra-piihwä-  f.  'Mittag':  haca  '%wayät *matlyai  utayarai  pain.sacaiti  "sie  währt vom  Mittag  bis  zum  halben  Nachmittag" ^■49',  —  äat  yimB /ralasat  raoch  ä  upa •%wqm  hu  paiti  ahwanam  "da  ging  Y. zum  Licht  vor  am  Mittag  dem  Pfad  der Sonne  entgegen"  V,  3.  10.
Ableit.  —  Vgl.  ar3m.ps%ii,ä-,  ra  ist  AbUut». form  lU  *ata-,  woraus  arim  als  Adv,  —  Pn, (M  N.);  rap,%'«,m,  (lu  V.):  r<,p,%^in,„r  rSn.
"  j.  rapid'wana'tara-  Adj.  'der  südlichere, südlich':    ya^a  vatö  'tarät  nannat  .  .   A,
Kompar.  aus  *rafAwfna-  Adj.,  Ableit.  aus rafAwä-;  s.  rafAioitara-.
•  j.  rapi^Tvi'tara-  Adj.  'der  südlichere,  süd- lich' :  ä  dim  vätS  upa.vävS  satayeiii  'taral haca  naimäX  'iaralibyS  haca  naimatibyö H.  2.  7.
Kompar.  aas  "tap&iwa.y-  Adj.,  Abtcit.  aus  ra- pt^wä-;  \.  rapi^vanatara:  —  Pü.;  rap^^wintar.
•  j.  'rapi^Twina-  Adj.  'mittägig':  ä  °mm zrvamm  Y.p.  1 1,  Yt  &.  a8.  A)  m.  Gott- heit der  zweiten  der  fiinf  (priesterlichen) Tagesabteüungen'^:  'mm  asavamm  asahe ratäm  V.  2.  4;  G.  2,  5;  —  yS  'nahe  ralu- frita  'mm  ratüm  framaraite  *n»m  ratüm fräyazäiie  A.4-5i  —  °n3i  .  .  ra%we  .  . frädatßave  zantumäica  Y.  j.  4;  G.  2.  i; —   'nahe  ra'iwS  A.4.3;  —  'na  aSäum
y.  T.  20.
•)  Genannt  rapi%w3-  (id.)  und  nach  N.  4g von  Mittag  bis  zum  halben  Nachmittag  wäh- rend; TgL  noch  Bd.  35.  9  {nimric  gas)  und  zu asiiya:
Ableit.  — Ableit.  aus  riT/i&wä-.  —  Pa.:trans3iir.;
SQ.  erl. :  madhyähnahsamdhyah,
```


## [2026-09-14T01:23:43.736Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"j\\.  .rad-  V\\|g\\.  .rad-\\|rad-  V\" BRT.txt | head\necho \"=== CHEUNG raθ / rad ===\"; grep -n '\\*raθ\\|\\*rad\\|raθa' CHEUNG.txt | head -30",
 "description": "BRT rad- entries and Cheung"
}
```


### [2026-09-14T01:23:43.825Z] TOOL RESULT

```
5455:•  g-  (t  j)  arad-  V.  'gedeihen  lassen'. Praes.  i   arid-  :  »rjd-.
10242:•  j.  garad-  V.  'gradi',  nur  mit  Praev. Praes.  i  g>r>d-.
20055:•  g.  marad-  V.  'verderben'.  Praes.  3 mand-,  9  mSrmda-''^.
25074:•  p.  rad-  V.,  nur  mit  ava  'verlassen'. Praes.  2  rada-.
=== CHEUNG raθ / rad ===
13115:*rad- (i.e. *(H)ra(n)d), pace Morgenstierne, EVS\: l.c. Most, if not all, intransitive
```


## [2026-09-14T01:24:11.580Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD rāh/rās ===\"; grep -n 'rāh \\|rāh,\\|rās \\|rāh$\\|rāh\\b' PHD.txt | head -20\necho \"=== PHD artēštār ===\"; grep -n 'artēštār\\|artēšt\\|lašk\\|lašgar' PHD.txt | head -20",
 "description": "MacKenzie rāh, artēštār, lašgar"
}
```


### [2026-09-14T01:24:12.664Z] TOOL RESULT

```
=== PHD rāh/rās ===
166:~ih: wonder. àb-dàn [^5d?n!] water-holder. abdast ['5dst!] hand-guard. abdom Pfdwm | М ?bdwm] last, final(ly). ~ih: finality, end. abd-sahist [pdshst'] wonderful. abē- [5»(y)- | M ?by-, N bé] without, Jess. ~-bar [-5/] fruitless. ---bé$ [-bys] unharmed. ~-bim [-bym] fearless. ~-bimih: fearlessness. e--boy [-bwd] senseless. ---bēyih : senselessness. —-büd(ih) [-bwt', -bwtyh] deficiency. «=čim [-cym] without reason, cause. abēdān рругп!] of use, wanted. abé-|-guman [-gwmn!] without doubt, certain. —-$umiünih : certainty. ~-mizag [-m(y)ck!] tasteless. ~e must [-mwst'] uncomplaining, content. ~-niyaz [-пуа?с] free from want. ~=-68 [ws] M *by?wš, N béhóf] senseless, unconscious. -~-6Sih : senselessness, unconsciousness. abér [yl] very, much. abē-rāh Payis] e erring. abesar [fysl | M ?bysr, N afsar] crown. abesīhēnīdan, abesihén- [Ashyn-ytn', v. abesihidan] destroy. išn(īh): destruction. abesihidan, abesih- Pžs(y)%-ytn! | M? bysyh-] perish, be destroyed. —išn(ih): destruction, ruin. abespardan Pžļsp?/tn!) = abespurdan. abespurdan, abespār- [’fspwltn', ?psp'l- | M ?byspwrd, ?byspr-, N sipurdan, sipàr-] commit, entrust, consign. ubestag [5(y)s? k!] Avesta, the Mazdean scriptures, abestām [ēst m] = abestān. abestàn [°25/°п!] refuge, support, trust. ābestan Dóystn! | P ?bystn, N abtstan] = ābustan, abé-süd [yý swt'] profitless. “Аһ: profitlessness. a-bëš Буў] harmless; unharmed, invulnerable. ~ih: harmlessness; invulnerability. abē-|-wināh [-cwz?^s | M?bywr? 1] innocent. ~-wizend [-wznd] harmless, invulnerable, safe. abézag Pfyck! | M ?bycg, (N *oëza)] pure, holy. ~th: purity, holiness, abēzār Pye’, ?Буе?1 | N bézdr] free.
172:a-dàd [471], a-dādestān [?- DYNA, -dtst^n'] illegal, unjust. ih: injustice, illegality. a-dahm P@?hm] uninitiated. -ādan [- m! | P dn, N ~] suffix forming secondary infinitives. a-dàn [??п! | M din ignorant. ~ih: ignorance. «адап [??!] wealthy, solvent; wealth. “Аһ: wealth. a-dard [Pdlt'] painless. áüdaróg [wk], ātaxš 1 ~ : the simplest kind of sacred fire. adehig (’dhyk'] indigenous, domestic. adén [?tyn! | М dun) entry. *adén- ['dyn- | = M] bring, lead. ādišt Ptyst'] fire-stand. : ae. D i ‚ (ed уд ádüg Ptwk! | M "?dwg] capable. adur twr! | Mdwr, N ādar] fire; the god ‘Fire’; cal. gth month; oth day. adurestar [twrystl] ashes. ~én [-yx!] ashen. adur- gah [twrg’s] fire altar. ЖЕСЕ, āfrāh PSPs | М ??р?Л] teaching, doctrine. alva 2 KM N facaz\ ‘ace Luch >a-frasāwand [' Bl? wnd] imperishable. afridan, àfrin- / āfur- Pžlytn', ?Blyn-, *pwl- | M 'p(w)ryd, "po -— P >f+yn-, N āfarīdan, afarin-] praise, bless; create. áfrin ['pryn! | M?pryn, N áfarin] praise, blessing. 9544. "tien ~agan [-k”n!] Afrinagan prayers. аїгӧёар [ēlwšk! | N ~ a] a sweetmeat made of flour, butter, and honey. ‚ *afsálàn Pfs'Px!' | (N ābsālān)] springtime. afsān (?psn! | (M ?р?ле), N afsāna] story, fable. afsardan, afsar- ['psi-tn'] cool down. afsārdan, afsar- Pfs?/-tn'] cool, freeze, extinguish. „išn: cooling. afsáy-, v. afsūdan. afsénistan, afsén- [*5syx-stn!, v. abesihén-idan] destroy. --i$n : destruction. afsin [swn | N afsün] spell, incantation. M psan afsös [psws | N ~] scorn, mockery. ~gar [-g/] mocker. afsūdan, afsāy- ['pswtn!, *ps*d-] enchant, protect by spell. afšāndan, afšān- [5Zz?n-tn! | N ~] spread, scatter, sow. afSardan ['5?Its! | N ~] = afšurdan. af$urdan, afšār- 'Pfwltn!,?pP?l- | N ~] press, compress, crush. āfurīdan, afur- ?fwl-ytn', v. Afridan] create. ~išn: creation. -ag [-À! | M -g, N -a] suffix forming (i) adjectives, from nouns and verbal stems, (ii) nouns, from adjectives and present stems.
536:pa(č)čēn [pcgn!] copy. *pa(č)čībāg [pcyp k', PWNe- | N *pajiw] *deceptive. ^h : deceit, hypocrisy. *pa(č)čībāy- [pcyp'd-, PWNc-] deceive. pad [PWN, for *pty | M pd, N pa] to, at, in, on. pad- [pt- | M *pd-) fall. padam [pd”m | (IN pandm)] mask for the mouth, worn by a celebrating priest. !Ipádan, pày- (UIN TLWN-tn! < А V ntr; Ptn, pd- | M pd, p’y-, N páyidan] protect, watch, defend. *pádan, pāy- [N TLWN-tn!, etc.] stand, wait. pādāšn [p?td?fn! | M p’d’syn, N pàdàs] reward, retribution. padēx [ptyhw'] flourishing, prosperous. ~ih: prosperity. padéxénidan, padéxén- [ptyhwyn-ytn'] make flourish, prosper. pādēz [p'tyc | M p'dyz, N pāyēz] autumn. pad-góhr [PW Ngwhl] т. jewelled; 2. of good stock, well-born. padifrah [p’tpl’s | M p'dypr?h, N *pādafrāh] punishment, retribution. padir-, ~išn, v. padiriftan. padirag [ptylk' | M pdyrg, N paóira] towards, against, counter-. (6) — madan: come to mect. ~ih: meeting, opposition.
538:pādīrān [p'igP n!] restrained, held back. pādīrān(ēn)īdan, pādirān(ēn)- [þptgľn(yn)-ytn'] restrain, impede. padīriftan, padir- [MK BLWN-tn!Ü < A mqbl, V qbl; ptgl-ptn! | M pdyr-yptn, N paóiruftan] receive, accept. ~išn: reception, acceptance. īpadisār [ptys' | N padīsār ?] beginning, basis. tpadisār [ptys’/] bridle, halter. padisāy [pts’d | M рдуу] on account of, for the sake of. padist [ptst! | P pdyst] promise, vow. & (abar) burdan: promise. padistadan, padist- [ptyst-”tn! | (P pdystwd)] promise, vow. padistā(£) [ptyst*k! | (M pdystw)] = padist. padiš (pts | M pdys] to him, it; postposition (= pad) to, etc. padištān [pryst?n' | P pdyst??n] leg. padišxwar [ptshwl] dish, bowl. pādixšā(y) [SL Y TA < A йур; p’ths?(d) | M раху] ruler; powerful, authoritative, authorized. ~ЛЬ : sovereignty, authority. pādixšīr [p’thsyl] agreement, treaty. pad-néróg [PW Nnylwk!] strong. pad-niģerišn [PWNnkylin'] cared for, guarded. pādofrāh [p’twpl’s) = pādifrāh. pad-panag [PWNpnk!] guarded, protected. Р pádrazm [p’tlcm] battle. pàd-rózag [p’tlwck' | M p'drweg] fasting. pād-uzwān [p’??wzw’n'] reticent. ~ih: reticence. pad-wizén [PW Nwcyn!] choice, select. pādyāb [pty | N ~] ritually clean; ceremonial ablution. ~ih : ceremonial ablution. pādyāwand [p?tyd’wnd | J p'dywnd] strong, powerful. cAh : strength, superiority. pádzahr [p’tzhl | N pa(d)zahr] bezoar, antidote. pad-zyān [PWNzyd"?n'] harmful. pafšār- [pps?/-] shame. pafšīr- [ppsyl-] be ashamed. ~i8n(ih): shame. pah [p’h] sheep. ~ast [-st'] sheep-fold, -pen. pahikaftan, pahikaf- [ptkp-tn! | M phykf-] fall on, touch, hit, attack. ~išn: attack, fight. pahikāftan, pahikāf- [ptk’p-in'] throw on, make fight. pahikar [ptk] | M phykr, N paykar] picture, image. pahikār [ptk?! | M phyk”r, N paykār] struggle, battle, dispute. īpahikār- [ptk?/-] fight, contend with, defeat. pahikardan, *pahikār- [ptk’/-tn'] request, claim, consult.
555:rabih [/pyh | M rbyh] noon, midday (heat). rad [/t! | N —] (spiritual) chief, master. АҺ: office of rad. rad [Pu | P rd, N ~] generous, liberal. ~ih: generosity, liberality. radag [itk! | M rdg, N rada] line, rank, row. radómand [/t?^wmnd] having a rad. rad-passag [/tps’k'] ceremonies of the gáhanbar festivals. radunay [/twny = Av. ratunaya-] one under the guidance of a rad. raftan, raw- [SGY TWN-tn! < А V sg’; lwb- | M rptn, rw-, N ~] go, move, proceed. ~išn, v. rawišn. raftār [/pt?] | N ~] goer. rag А! | M rg, N ~] vein. «ЛЬ: disposition, character. ray [/gy | P rg] quick, swift. ray [Pg | N —] meadow, plain. rah [/s, lh, [hy | M rh(y)] chariot, wagon. rah-, у. rastan. rah [Ps | M rh, N ~] road, way. rahag [/hk! | P rhg] = rag. rāh-dār [lsd] | N ~] brigand, highway robber. ~ih: brigandage. rahig [/syk!, Ikyk' | M rhyg, N rahi] child, page. ~ih: childhood. rāh-nimāy [Psnm?d | (M r’-hnmwd’r), № ~numa] guide. ram [Pm | М әт, N ~] peace; cal. 21st day. ram(ag) [/m(k') | P rm, N ram(a)] herd, flock. ráménidan, rāmēn- [Pmyn-ytn! | M ?myn-] give peace, pleasure. rāmišn [P min! | M rmyfn, N rāmi$] peace, ease, pleasure. ~ig [-vk! | N —z#] peaceful, at ease. ran [Рп! | N ~] thigh. P rān- [/^n-] fight. randidan, rand- [/nd-ytn! | N —] scratch, grate, abrade. rang [/ng | M rng, N —] colour, dye. ranj [Inc | P rnj, (M rnz), N ~] toil, trouble. ~ag [-k' | N —a] troubled. ranjénidan, ranjén- [/ncyn-ytn'] trouble.
1349:consecrated bread drēn; ~ drink parāhēm.
1670:doctrine āfrāh, čāštag, poryotkésih.
1795:erring aband, abērāh.
3287:punishment drēš, pādifrāh, puhl.
3423:retribution pādāšn, pādifrāh..
3943:teaching āfrāh, čāšišn, hammēzišn.
4742:padyabib, ALI 00 t€» о) pādāšn VA My o padirán- ` - My yey a pādīrānēn- -p ry yey a pādīrānēnīdan W3 y ry We pādīrānīdan WS wy veyo pādīrān wey yey os paymar Ne теу o pādēz 23 voy o lpādan Y rero) pādofrāh ау\һе» 0) padzahr NS ve» o» pāygūs ISYA padrozag 15 cP rere pāyram » rey’ о
4743:padrazm sò rey о) pādifrāh © teras arzan!, gāwars! 5o)
4969:rah, (23%) ray, тау rāyūmand rāh
=== PHD artēštār ===
214:a-pus [' BRE] without a son, childless. ár-, v. árdan. 5 āranj "Inc | N ~] elbow.. 9-43. "Ant *a-rāst Prst'] untruth. ārāstan, ārāy- [Pstn!,^Pd- | N ~] prepare, arrange, adorn. ~ién: arrangement, adornment. a-rawüg [”/wbk!] immobile. Ard р | M?yrd, N ~] a goddess; cal. 25th day. ard [KHM A < А gm; п | N ~] flour. агаа [py | (M rd?w)] righteous, truthful. ardan, ār- [THNN-tn' < А V thn; ?l-tn'] grind, mill. ardāyīh ['i?dyh | M?rd?yyh] righteousness, rectitude. ardig [/tyk! | M ?rdyg] battle. ardikkar рук], -kl | M?rdyqr] warlike, warrior. ~ith: doing battle. arduš [”ldwš = Av. aroduš-] a degree of sin. Ardwahišt Prtwhst' | M ?rdywhyst, (N urdībihist)] Right, the second Amahraspand, guardian of fire; cal. 2nd month; 3rd day. arešk [lysk' | M ()rysk, N rašk] envy, jealousy. ~én [-yn'] envious, jealous. ārešn Pim! | M ”7ysn-, N (a)rif] cubit. aryand [?/епа | N ~] horrible. arģawān [*/gwk'*n! | N aryawān] purple. armēšt ["/myst'] inactive, infirm. ~ih: infirmity. armēšt-ģāh [-g’s] secluded place for the infirm. агбуї&п [/wdšn'] growth. ~ig [-y&!] growing, vegetable. ars Dis | M?rs, N ~] tear (drop). artēštār УЯ? | N artēšdār!] warrior. „īh: warriorhood. arus [2/00] white. arwand [wnd] swift, valiant; river Orontes. ~ih: swiftness, valour. arwés [lwys | M ?rwys, N ~] rope. arz [KSP! < А Ар; с | N ~] worth, value. Arzah [Iz h == Av. arazahi-] the eastern continent of the earth. arzan [PE < А prg’; len! | N <) millet. arzàn Plen | M *rz'n, N ~] valuable, worthy. ~ig [-yk'] worthy. ~igih: value, worth, worthiness. arzidan, arz- [?/с-уїп! | N ~] be worth. ~išn: value, worth. arziz (сус | M ?rzyz, N ~] tin, lead. —ën [-yn'] tin, leaden. ārzōg Picwk! | M'wrzwg, N àrzó] desire, lust,
432:— h: supplication. lajan [/cn! | N ~] mud, slime. larzidan, larz- [ilc-ytn' | P Irz-, N ~] shiver, tremble. laškar [ISk] | N ~] army.
3723:soldier laškarig; v. warrior.
3724:soldiering laškarīgīh.
4267:warriorhood artēštārīh.
4906:Rašu laškar laškarīgīh laškarīg raštan rištag radēmand radīh
```


## [2026-09-14T01:24:13.180Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN rah ===\"; grep -n \"rah 'Weg'\\|rāh\\|603\\. \\|607\\.\" HRN.txt | head -20",
 "description": "Horn rāh"
}
```


### [2026-09-14T01:24:13.238Z] TOOL RESULT

```
=== HRN rah ===
5399:603. rast recht, wahr, rechts*, 7'äste^ rastl, rästln (Sahn. I,
5422:607. rah^ ras ^), reh *Weg ; espyes.
11651:«•«pr«« 607.
12862:/iii-afc 607.
12864:^iirrf/e 607.
13438:räÄ 607.
13439:' reA 607.
13441:rehlden 607.
13459:/yW 607.
13467:resfen 607.
16359:fortan 607.
16754:ras 607.
16761:rast an 607.
18087:rathyä- 607.
19550:'r* 607.
19861:lär 607.
19984:ra/t 607.
20701:r« 607.
20702:n. räh 607.
```


## [2026-09-14T01:24:25.289Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '5399,5460p' HRN.txt",
 "description": "Horn 603-608"
}
```


### [2026-09-14T01:24:25.341Z] TOOL RESULT

```
603. rast recht, wahr, rechts*, 7'äste^ rastl, rästln (Sahn. I,
123 Vers 1070).
ap. rasta- recht, richtig'; aw. rasta--, phlv. rast,
rastlh\ ai. raddhd-,
oss. d. t. rast^ rasf (212).
LW. kurd. af/. bei. (222) rast; wa./. rast, ssiv, rüst.
604. räm *Ruhe; fröhlich, heiter, ramis, ramist (Lex.).
ap. vergl. Äriya]ramna', *Apia]^oi/nvt]g; aw. raman-
^) Aw. rati- (yt. 10, 45) ist = ai. arati- (Bartholomae, Altiran.
Verbum 194, BB. 17, 111 Anm., G;oldnor, KZ. 25,520 Note 61).— 135 —
*Ruhe'; phlv. hu]ram, ram(i)sn, rämmltan; ai. rdmU'
*Lust'.
oss. üromjn 'zurückhalten, hemmen, beruhigen' (263).
605. ran 'Schenkel'.
aw. räna- 'Schenkel'; phlv. ran^ ränpün, arm. LW.
eran, meist pl. eranK (Hübschmann, No. 96).
kurd. bei. (221) LW. ran; af/. vrün.
606. ränden 'treiben, stossen*, ranis,
Contrahirt aus rawdmden^ Causativ von reßen
(No. 619), vergl. Kä»än: Z(efre), beräw, heräivött^
heräft s. v. ränden,
Phlv. rayinTtan, räyma, räyln(i)sn, räymitärih (Men.),
jüd.-pers. pJN^NI (Is. 63, 17) sind nicht klar.
607. rah^ ras ^), reh *Weg ; espyes.
skr. vergl. rathyd- Xandstrasse' (spät) 2); phlv. reis,
aspjräs; af/. lär^),
LW. kurd. rl; bei. ra, n. rah (219); af/. räh;
arm. rah.
Gehört hierher auch np. reste^i (phlv. rastan, Men.),
Praes. reh-em^ rehlden u. s. w. 'befreit werden, ent-
kommen', wörtl. 'sich auf den Weg machen'?**)
608. rubüden 'wegnehmen, rauben', Praes. rubay-em,
riibäyende ; ruften 'fegen , gäten', Praes. röb-em,
ai. V^löp' (älter röp-) 'zerbrechen, packen, plündern,
rauben''^); phlv. röp 'Raub' (AV.-GL), kah]rupäl 'Bern-
stein (Säy. näsay. II, 115); got. biyaubön 'berauben'.
bei. röpcifj 'fegen, kehren' (329).
ö hat noch Kää. Z. böröw (Impt.), börowön (Aor.),
rowon (Praes.).
np. rubäyem geht auf älteres *rupäyati zurück.
^) BQ. Rückert bei do Lagarde, Ges. Abh. 51, Note l.
^) Aw. hizvö raiHm (y. 50, 6) beisst iiacb Bartholomae,
KZ. 28, 34 *Lenker der Zunge*, siehe aber Geldncr, KZ 28, 259.
') Aus *ral (Trunipp, Graramar of the Tastö § 7); //är,
Darmesteter, Ch. pop., p. CLXXV, Note 2.
*) AM. 183 Zeile 1 hat aUerdings biriheS,
^) Aw. urüpay^intl (y. 43, lÜJ muss als unsicher bei Seite ge-r
lasäcn werden.— 136 -
609. reje^ reze *Reihe\
aw. razista- ^geradester ; ai. räjistha- (Nöldeke,
mündliche Mitteilung). Jüd.-pers. T]T\ dagegen dürfte
zu aw. rasman- 'Schlachtreihe', ai. ragmän-^ racmi'^
ragi- gehören.
Geldner hatte KZ. 24, 387 Note 2 aw. razura-
'Geleis' (yt. 5, 50) vergleichen wollen.
np. rede 'Richtung, Linie, Reihe' (Öähn. I, 367
Vers 823) scheint dagegen zu aw. ereta-, areta-y ai.
ftd' 'richtig, vollkommen' zu gehören (ursprünglich
'etwas Rechtes, Gerades).'
610. ru%8 {rexs) 'Glanz, Licht', ru/^Tden [rexsiden).
aw. vergl. rao/snc^ 'glänzend, leuchtend, strahlend' ;
ai. ruksd' 'glänzend'.
```


## [2026-09-14T01:24:38.105Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== ARB mo3rb عسكر ===\"; grep -n 'العسكر\\|عسكر' ARB_mo3rb.txt | head -10\necho; echo \"=== ARB abdulraheem عسكر ===\"; grep -n 'عسكر' ARB_abdulraheem.txt | head -10\necho; echo \"=== ARB عرادة ===\"; grep -n 'عرادة\\|العرادة' ARB_mo3rb.txt ARB_abdulraheem.txt | head",
 "description": "Jawaliqi: ʿaskar, ʿarrāda"
}
```


### [2026-09-14T01:24:38.239Z] TOOL RESULT

```
=== ARB mo3rb عسكر ===
10309:وهو تابعى ثقسة ٠‏ قال أبو أحمد العسكرى : د كان صاحب راي على" يوم صفين » ثم ولاه اصطخر » 5 
17003:نت 7 عسكر مم 5 سم بأد معروتف ل قال الأزهرى 5 وكاله 
17013:(0) فى نا« وهى > ٠‏ وهو خطأ ٠‏ 09 عبارة المهرة ( ؟ 1مة) : ه والعسكر 
17015:لان در يد رأيان ٠‏ والظاهى أن الكلمة عرربية ٠‏ قال ابن الأعر الى : « العسكر : الكثير من كل شىء: 
17018:(0) هذاغير جيد . فكلية ”عسكر'' الراخ أنها عر بية» و ””مكرم'' بشم اليم وسكون الكاقف 
18244:سوه كر وعسكر ١‏ 3 ّّ - رار 

=== ARB abdulraheem عسكر ===

=== ARB عرادة ===
```


## [2026-09-14T01:24:39.692Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== TAD ترهات ===\"; grep -n 'ترهات\\|الترهات\\|ترّهات' TAD_pages.txt | head -10\necho \"=== TAD عسكر ===\"; grep -n 'عسكر' TAD_pages.txt | head -5",
 "description": "TAD turrahat"
}
```


### [2026-09-14T01:24:39.931Z] TOOL RESULT

```
=== TAD ترهات ===
=== TAD عسكر ===
1837:                                     ‫فارمي ‪ 9‬لشّكر © معناهجحش‬    ‫عسكر ‏‬
2546:                                                             ‫عسكر وجيش‬
```


## [2026-09-14T01:24:45.540Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR<=1840 && /\\[pdf page/ {p=$0; n=NR} END{}' TAD_pages.txt\ngrep -n '\\[pdf page' TAD_pages.txt | awk -F: '$1<1840' | tail -3\necho \"---- context 1820-1850\"; sed -n '1825,1845p' TAD_pages.txt",
 "description": "TAD page for ʿaskar"
}
```


### [2026-09-14T01:24:46.617Z] TOOL RESULT

```
---- context 1820-1850
           ‫‪١‬‬                                       ‫‪٠‬‏‬                      ‫اين‬
                   ‫تأومان ع عيحنة مللوفة شد يق لتركةظومان باه ‪:‬دفاو‬
‫طقا‪-‬لى وؤدغ وبراد ببرهئيطة اسطوائية يليسها سافةا! ‪-‬‬
                                                  ‫طأبيَة أايقياوو‬
                             ‫العربات فوىسكانا ‪ .‬أو هومنسوب الى طابة العامة‬

                                    ‫‪5‬‬

                           ‫عراب ‪ -‬سربانى‪ 8‬عرابا » معناءكفل المعثمن‬

‫عربة ج عربات سحبوناني دمممه بقلب أوها عينا وميمها بأىءكاقلبتميم مكة|!‬
          ‫بكة قد أدخل أبن بطوطة هذه اللفظة فىاللغة العربيةومعناها عجلة ومركية‬
                                     ‫فارمي ‪ 9‬لشّكر © معناهجحش‬    ‫عسكر ‏‬


 ‫عيراني]‬      ‫عود أي اله طرب وهو يكون من ستة أو عشرين وثرا‬
                                                                       ‫و‬
                                                ‫‪1‬‬
                                                        ‫ب‬
                                                        ‫م‬
                                                         ‫واه‬
```


## [2026-09-14T01:24:47.497Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('TAD_pages.txt',encoding='utf-8',errors='replace').read()\npages=re.split(r'\\f',t)\nprint(len(pages))\nfor i,p in enumerate(pages[:30]):\n    m=re.search(r'\\[pdf page (\\d+)\\]',p)\n    print(i, m.group(1) if m else None, repr(p[:80]))\nEOF",
 "description": "TAD page structure"
}
```


### [2026-09-14T01:24:48.770Z] TOOL RESULT

```
87
0 None '                                     \u202bالف\u202c\n           \u202bياكابىاللبناك\u202c  \u202b\u202aَ8\u202c\u202c\n  '
1 None '                    \u202bذكرى الذ ممردص\u202c\n \u202bالى الكير بروحه ونكرة\u202c        \u202bالى من حك '
2 None '                                       \u202b\u202a0\u202c\u202c\n\n              \u202bبس الآالبارىء الماد'
3 None '                                         \u202b(ب)\u202c\n \u202bعلى أن رد الاخيل إلى أصل لفته ق'
4 None '                                                                       \u202b\u202a0\u202c\u202c\n   '
5 None ' \u202b\u202a--\u202cفينيعي وفيالعبرانية « ارحمان \u202a 6\u202cوهو حيوان في جوف صدفة\u202c       \u202bاراد\u202c\n \u202b|اك'
6 None '\u202bمعاه أخبار تارمحية وقد استعمابا العرب ععى\u202c           \u202bاساطير \u200f بوناني \u202a8\u202c\u202c\n    '
7 None ' \u202bإرفج \u202a -\u202cتعريب علتهة؛ الجرماني الذيمعناهحر" وهوالسشمعب غرني\u202c\n\u202bجرمانيا الذي دوخ'
8 None '                             \u202b|قنوم ارامية \u202a 9 72\u202cقَدُوما \u202a 4\u202cمعناه الشخص\u202c\n \u202bفي '
9 None '                                    \u202b\u202a5\u202c\u202c\n\n                                 \u202bدرن'
10 None '                                 \u202bم\u202c\u202bميه\u202c\n                                    \u202bم'
11 None '                                                              \u202bعت ات\u202c\n\n\n \u202bبأميا '
12 None '                                 \u202bعت اب\u202c\n\n\n                                \u202bرجيس'
13 None '                                        \u202bك\u202c\n                                    '
14 None '                                  \u202bدوو\u202c\n\n\n\u202bمن « وى » أي رابحة ذكة و\u202a9\u202cستان» وهي '
15 None '                                  \u202bلدابإاو ده\u202c\n\n\n \u202b\u202a 001\u202cأي فرس و\u202a 81012\u202cأيتطيدب'
16 None '\u202bمن \u202a0110\u202cم تفاح\u202c      \u202bحت ابطالى \u202a010002\u202cوم أي فاح ذهى \u202a05 .\u202c\u202c               \u202bا'
17 None '                                \u202b\u202a0 0\u202c\u202c\n\n\n                          \u202bسبلوان \u202a--\u202c'
18 None '\u202bينع فيمصر واللفظة مصرية \u202a .\u202cجاءففيبعضترجمات الاتميلكانلابسا البرفير\u202c\n\u202bوالارجوان'
19 None ' \u202bبير| ح ايطالى همءنط من المرمانية «عنة عرببها جعة تصنم من مخمير الشعير\u202c\n       '
20 None '                              \u202bا\u202a4\u202cع\u202a1\u202cد\u202a #\u202cست\u202c\n                          \u202b\u202a#\u202cأن'
21 None '                                                            \u202bغهرن\u202c\n             '
22 None '                                     \u202b« بيت ثور » في الارامية أي ببتالنار\u202c\n     '
23 None '                               \u202b\u202a59\u202c\u202c   \u202b\u202a9\u202c\u202c   \u202b\u202a58\u202c\u202c\n\n\n\n\n\u202bج جن \u200f فارمبي «جان» '
24 None '                             \u202bاوج سد\u202c\n\n\n\n                                  \u202bجام\u202a'
25 None '                  \u202bهفعناه عاموبراد به قائد اليش\u202c                \u202bحترال | أنطالى '
26 None '                                          \u202bد\u202c\u202bد\u202c\n\n\n                             '
27 None "             \u202bظ\u202c                \u202bخانة\u202a :\u202cفارسى'«خانة© مسناهبيت\u202c\n\u202bخام\u202a -\u202cفارسبي«خ"
28 None '                                    \u202bد\u202c   \u202bلاه\u202c\n\n\n\n \u202bمفئاه وعاءمننحاس مرادقه مرك'
29 None '                                \u202bلسلا سم\u202c\n\n\n                                 \u202bدر'
```


## [2026-09-14T01:25:06.274Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AFM ترهات ===\"; grep -n 'ترهات\\|التره\\|ترهة' AFM.txt AFM_pages.txt | head -10\necho \"=== AFM عرادة ===\"; grep -n 'عرادة' AFM.txt | head -5\necho \"=== PLA ترهات/turraha ===\"; grep -n -i 'turraha\\|tarraha\\|ترهات\\|turrahat' incoming/PLA/PLA_pages.txt | head -10\necho \"=== PLA rah p133 ===\"; grep -n -i 'rāh\\|raha' incoming/PLA/PLA_pages.txt | sed -n '1,20p'",
 "description": "Addi Shir & Asbaghi for turrahat"
}
```


### [2026-09-14T01:25:06.415Z] TOOL RESULT

```
=== AFM ترهات ===
AFM_pages.txt:202:( الترهان القاطع )
AFM_pages.txt:907:و( ره الرجل وقع في استرهات . ان )انا لماطل : كل ذلك 2 من راه اى
AFM.txt:322:( الترهان القاطع ) 
AFM.txt:1482:و( ره الرجل وقع في استرهات . ان )انا لماطل : كل ذلك 2 من راه اى 
=== AFM عرادة ===
=== PLA ترهات/turraha ===
4282:e_>       -       tarariyya:                    Pl.        Vans       turraha        s.    turraha          »-
4343:an     -       turraha:          "Seitenpfad"                pers.       ı     wahrscheinlich               aus    dem    pers.     ol
=== PLA rah p133 ===
1092:„LT-            &zär:        "der           heidnische                  Name       von     Abrahams          Vater"       (Historia          religionis
1886:13.           Frahang         Pahlavik               s.     v.
2051: 10. Frahang                             Pahlavik s. v., Bundahifn                                          s. v.
3074:8.   Frahang        pahlavik
3507: 6.    Nyberg          Bd.    II       s.     v.,      Frahang              pahlawik           s.    v.
3776:5. Frahang               pahlawik.s.                   v.
4282:e_>       -       tarariyya:                    Pl.        Vans       turraha        s.    turraha          »-
4343:an     -       turraha:          "Seitenpfad"                pers.       ı     wahrscheinlich               aus    dem    pers.     ol
4750:3. Frahang                 pahlavik                 s.    Ve
6199:9.     Frahang           pahlavik                 s.    v.
6644:11.    pahl.-paz.              s.     v.,     Junker            S.     102,       Frahang             Pahlavik       s.    v.
8624: 4. Frahang Pahlavik S. 26, Bundahiän s. v.
8845: 9.    Frahang          Pahlavik              S.       33.
10045:Saöma                                                                          178                                                Sikarahang_
10078:ger         - $ikarahanf:                          "eine      Pflanze"                 pers.     iii          Sikarahang          15,
13561:11.    Frahang           Pahlavik             s.       v.
```


## [2026-09-14T01:25:11.913Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '4330,4360p' incoming/PLA/PLA_pages.txt\necho \"=== page tag near ===\"; grep -n '\\[pdf page' incoming/PLA/PLA_pages.txt | awk -F: '$1<4360' | tail -2",
 "description": "Asbaghi turraha entry"
}
```


### [2026-09-14T01:25:12.985Z] TOOL RESULT

```
a2                  uranfa:       nom.     un.        v.     turunf       q.    v.


ER         -        urun$i:           "orangefarbig"               s,    turung.


AT Eyn - taranfil:                      "Melisse"              taranpäan             s.   taranfän.


@l&s} - tarinfän:                       "Melisse"            = tarangän              s.   taranfän.

an     -       turraha:          "Seitenpfad"                pers.       ı     wahrscheinlich               aus    dem    pers.     ol
       rah          "Weg"       mp.               räh 2 abgeleitet.


&      -        arawwuß:          "Propaganda"                s.     rawäß.


&r         - tarwig:             "Verbreitung"                s, rawaß.

ol3        -    tiryäg:          "Bezoarstein"                pers.       3, eventuell               aus   pers.         SL,
       tiryäk.


 @L5-               tiryägi:           "berauscht,            Säufer"           Nisba      v.    Sl        tiryäg.


 SAL}- tiryäk:                   "Opium"         = tiryäg,              mand.        tiriak      4

=== page tag near ===
```


## [2026-09-14T01:25:19.959Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('incoming/PLA/PLA_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\n# find leaf containing 'turraha:'\nimport re\nidx=t.find('turraha:          \"Seitenpfad\"')\nleaf=t[:idx].count('\\f')+1\nprint('leaf',leaf,'printed page',leaf-15)\npages=t.split('\\f')\nprint('=== leaf148 (p133) ===')\nprint(pages[147][:1500])\nEOF",
 "description": "PLA leaf for turraha and page 133"
}
```


### [2026-09-14T01:25:21.253Z] TOOL RESULT

```
leaf 88 printed page 73
=== leaf148 (p133) ===
rähib                                                                      133                                                              rubäb


el     -     rähib:       "christlicher                      Mönch"        pers,            1    wahrscheinlich                aus    dem   pers.
        o), räh <T mp.)                      räh am.                 rasa,           air.       *räda     ®,       pers.ol       bän    "der    den
        schützt          und       daher          kennt"        .     s.      ruhbän.


ziel          -     rähnämaf:            "Seekarte,             Reisebuch"                        pers.        “lio},         rähnäme       <mp.
            ol, räh       s.       rähib          + pers.           «,l näme           "Brief,           Buch” << mp.            „rı    nämak       3,

                                                                                                                                                         4.
eleL -            rähwäß:          "leichtgehendes                    Pferd"                    pers.    ‚Lel        rähwär          u.o,»s, rahwa


olol -        rähwan          = rähwäf             q.    v.    5,


Er) - zähüf = rähwag a. v.
ol      -    räwug:       "Seiher,                Filter;       was        den        Wein       klärt,        Weingefäß,Becher"               aus
        pers, 2),1, räwak                    6 mp.             »»        rawäg "fließend"                      7

>39), - räwa
```


## [2026-09-14T01:25:38.454Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('leaves',len(pages))\nfor i,p in enumerate(pages[:5]):\n    m=re.search(r'\\[pdf page (\\d+)\\]',p); print(i,m.group(1) if m else None, p[:100].replace('\\n',' '))\nEOF",
 "description": "BQT v2 structure"
}
```


### [2026-09-14T01:25:39.631Z] TOOL RESULT

```
leaves 684
0 None 
1 None                                          ‫‪7‬‬                            ‫رن‪۳‬‬     ‫نات‬       ‫ا
2 None                    ‫م‬ ‫و‬ ‫نآکو سخنیم بیاموزد مرا‬                        ‫د‬ ‫د‬ ‫ل‬ ‫ج‬ ‫م‬ ‫ة‬ ‫
3 None                                                      ‫‪ar‬‬                                      ‫ما
4 None    ‫و‬              ‫فك اا ‪ .‬بخش‌اول (منطق)‬                           ‫‪ ۰‬ای‬   ‫حصحح سیدمحمد‬
```


## [2026-09-14T01:25:43.131Z] TOOL CALL #32: Bash

```json
{
 "command": "sed -n '1,60p' tools/ref_page.py",
 "description": "Inspect ref_page tool"
}
```


### [2026-09-14T01:25:43.177Z] TOOL RESULT

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
        pdf_page = int(argv[argv.index("--pdf-page") + 1])
        scan = scan or (scans[0] if scans else None)
    elif scan:
        pdf_page = None
        pm = scan.get("page_map")
        if pm and os.path.exists(pm):
            pdf_page = json.load(open(pm)).get("map", {}).get(str(page))
        if pdf_page is None:
            pdf_page = page + int(scan.get("pdf_offset", 0))
            print(f"(no exact page map; using offset {scan.get('pdf_offset', 0)} -> pdf page {pdf_page}; check the printed number and re-run with --pdf-page if off)")
```


## [2026-09-14T01:25:45.830Z] TOOL CALL #33: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:984 --image 2>&1 | head -60",
 "description": "Fetch BQT page 984"
}
```


### [2026-09-14T01:25:46.935Z] TOOL RESULT

```
no scan of BQT covers printed page 984 (see 'scans' in refs_online.json)
```


## [2026-09-14T01:25:49.979Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources\npython3 -c \"\nimport json;d=json.load(open('refs_online.json'))['BQT']\nprint(json.dumps(d.get('scans'),ensure_ascii=False,indent=1))\nprint('page_offset:',d.get('page_offset'))\nprint('lookup:',d.get('lookup_hint'))\"",
 "description": "BQT scans config"
}
```


### [2026-09-14T01:25:51.131Z] TOOL RESULT

```
[
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
]
page_offset: vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').
lookup: grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)
```


## [2026-09-14T01:25:57.240Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (390,391,392,440,441,442):\n    print('======== leaf',i,'≈ printed',i+543)\n    print(pages[i][:1200])\nEOF",
 "description": "BQT v2 leaves near 934 and 984"
}
```


### [2026-09-14T01:25:58.269Z] TOOL RESULT

```
======== leaf 390 ≈ printed 933
  ‫س‪۳‬‬
   ‫ه‪۳‬‬‫باه‬                                                                                             ‫ران‬
‫راك ‪ -‬بر وزن خاك * فوج گووسفند‬                          ‫راف د بر وزن کاف» بزبازست جربی‬
‫جکنگویبرناد ‪ - ۱‬و بمعنیکاسة آبخوری حم‬                          ‫سیاسه خوالند ‪ .‬گوشد يوست جوزاست ‪.‬‬
‫آمده است‪ -‬ورشتةٌ سوزن رانیز گفته‌اند‪ -‬وبلفت‬            ‫راقو نه= بر وزن بابونه ‪ ۰‬پودله را‬
‫زند ویازند(‪ )۱‬راه باشد که بعربی صراط وطریق‬              ‫گونند ؛ وباین معنی بجای فا قاف وبجای نون‬
                                          ‫خواند ‪. ۴‬‬     ‫تای قرشت هم منظر آمده امت که راقونه‬
‫دگااده » با کاف بر وزن آوار» ‪ ۰‬زن‬                                                                    ‫باشد ‪.‬‬
                        ‫فاحشه ویدکاره را گوند ‪۰‬‬         ‫‪ 94۰‬بروزن دافه‪ .‬کیاهیاست مانشدسیر‬
                                                                                        ‫ر‬
‫وبزرن کام‪ ۰‬شض وحش امت‬      ‫رام =‬                        ‫برادرپیاز‪ ,‬وآنرابربان کرده بخورند بفایت لذین‬
‫که الفت گرفته وآموخته وفرمان بردارباشد؟ ‪-‬‬               ‫باشد؛ وباین معنی با زای نقطه دار آهممده‌است؛‬
‫وهام روزییست وبکم است ازماه های شمسی؟ ‪-‬‬         
======== leaf 391 ≈ printed 934
  ‫رامعك‬                                                                                                      ‫‪-۳‬‬
‫رامش د بکراك بروزن داش ‪۰‬‬                                             ‫وآرمیدن رانیز گویندا ‪ -‬وبمعنی روان ‪7‬‬
‫بممنیآرامیدن‌و آرامش وسآود کی وفراغت باشد‪.‬‬                      ‫باشد ‪ -‬ونام شخصی که واضع سازچنگه بوده ؟‪.‬‬
‫گونند هش نگین انوشیروان چنین بوده که‬                           ‫و خوش وشاد و خرم را نیز گفته اند ‪ - ۳‬و نام‬
 ‫ومر‬
   ‫ر‪+‬اه بسیار تاريك است هرا چه بینش ؟ ع‬                         ‫دره‌ایست درملك هنب‌وستان ‪ -‬ونام عاشق ویس‌هم‬
 ‫دوباره ایست مراچه خواهش ؟ ومر گے درقفاست‬                       ‫هت » وچون او بيار عیاش وشادکام و پیوسته‬
 ‫بومعتی ساز و نوا و عیش‬             ‫<<‬     ‫مرا چه رامش‬          ‫خوشحال و خوش طبع بود او را بدن جپت رام‬
‫چه رامش گرخواننده وساز نده را‬              ‫وطرب هم هت‬           ‫وصهٌ آشان‬
                                                                        ‫میگفتند ‪ ۳‬و برامن شہرت دارد ق‬
                                                     ‫کوش‬        ‫وه رورا وبهاای تن باه د‬
                                                                                      ‫موم و‬
‫راهشت ه بكر ‪:‬الت بروزن
======== leaf 392 ≈ printed 935
 ‫~‪“r‬‬                                                                                                                       ‫رامشگر‬
 ‫رامیتن ‏ د با ثالث بتحتالی مجهول‬                                                                          ‫ا‬
                                                                           ‫رمشگر ه باکاف‌فارسی‌برو‪ :‬نیداشور‪,‬‬
 ‫رسیده وفوقانی مفتوح بنون زده » نام قصبه‌ایست‬                              ‫مطرب و خنیا کر راکوبند که خواننده وسازنده‬
‫از ولایت بخارا‪.‬و خواجه على رامیتنی که از‬                                                                                     ‫باشد ‪.‬‬
‫کمل اولیاست وبحضرت عزبزان اشتهار دارد از‬                                 ‫بکرثالث ورابع وسکلون‬             ‫رامشی؟ ‌‬
                                                ‫آلجاست ‪.‬‬                   ‫که ساز نده وخواننده‬      ‫تحتالی؛ بمعنی راه‌شگراست‬


‫رامین = بائالث بتحتانی رسیده وینون‬                                                                                           ‫باشد ‪.‬‬
‫زده ‪ ۰‬نام عاشق وس است و قصه وبس وراهین‬                                     ‫رامك = بفاح‌الت و‪‌-‬کون‌کاف؛ مصغر‬
‫مشهور انت ‪ - ۷‬و نام چنگه نوازی هم بوده‬
                      
======== leaf 440 ≈ printed 983
  ‫هی ‪۷۹۳‬‬
                                                                                                     ‫روغنای‬
                                                 ‫کف‬        ‫واو‬
                                                             ‫معروف است ‪ ۱‬و آنرا از دوغ گوسفند ک‬
‫روغی هفز ‪ -‬کنابه ازعقل و تدییر‬                              ‫اومثال آن م مبیگیرند » و نوعی دینگر همهت‬
                                                 ‫باشد ‪.‬‬
‫روغنی ‪ - ۴‬بفتح اول وغین شطمدار‪,‬‬                                 ‫و غن سنگه عصاری باشد ‪.‬‬        ‫شده غن است ‪۰‬‬


‫نالی باشد که خمیرآ لراباروغن سرشته باشند؟ ‪-‬‬                ‫روغناس = بر وزن و «عتی رویثای‬
               ‫وعسار وروغن گر را نگیوزیند ‪.‬‬                ‫است ‪ ۰‬وآن‌گیاهی باشدکه چیزها بدان رنگه‬
‫»بیان شله‌دار ونون بر‬                                                                             ‫کنند ‪. ۴‬‬
                    ‫روغنینه * غ‬
 ‫هیرآنرا‬
       ‫کم‬‫وزن هرشبینه » نرانایکوبند ‪٣‬‏ خ‬                    ‫روغن بریگ ربختن ‪ -‬کنابه‬
‫پهن کرده در روغن بفیدز(‪)۱‬؛ بستی گوبند نان‬                  ‫ازکار و مهم فرمودن بمردم بی ماحصل ر مهمل‬
‫کرمی است که بر آن روغن رز ند ودیگری را‬                      
======== leaf 441 ≈ printed 984
                                                                                               ‫‪۷‬‬


                                 ‫جشم امتت‪ .‬ء‬      ‫همچو باطنش‬           ‫رآن‬
                                                                         ‫ایهکه‬
                                                                             ‫ظر چ‬
                                                                                ‫و نم اول ه‬
 ‫رومی خوی کی رګاوندکه‬                                                                              ‫لباشد ‪.‬‬

‫دورنگه ومتلون مزاج‌باشد وبهر کهرسد برنگه‬          ‫روم = نم اول وئالی مجهول بر وزن‬
                              ‫وخوی اوشود ‪.‬‬        ‫موم » موی زهار باشد ‪ - ۱‬و با ثانی معروف‬
‫رومی رن رعنا د کنابه ازآفتاب‬                      ‫ملکی است مشهور بحدود شام‪ - ۴‬ومخفف رویم‬
                             ‫عالم تاب است ‪.‬‬       ‫هم هت یمنی روی هن ‪ -‬وبفتح اول نام درختی‬
‫روهینا ‪ -‬بروزن بوسیناه بمعنی زدوده‬               ‫نت » و بعضی گویند‬         ‫آکی‬‫رل م‬
                                                                                 ‫م مق‬
                                                                                    
======== leaf 442 ≈ printed 985
 ‫‪AA‬‬                                                                                                  ‫رواس‪‎‬‬

 ‫فته اند که‬
          ‫ګم‬‫کوبند «رون‌آن» بمنی سبب آن وباعث آن ‪١‬‏ | عسیب خوانند؟ ؛ و بکر اول ه‬
                                    ‫بروزن شکنج‬       ‫و با ثالی مجهول‪ .‬نام قصه‌ایست درهندوستان که‬

                         ‫ر‬
‫توجو ‪ - ۴‬بفتح اول وضمجیمبر‬                                                        ‫مولد ابوالفرح ب(ود‪. )۱‬‬
‫وزن سمن بو » کرمی باشد چوب خوار و بعربی‬                            ‫‪۱‬‬                ‫‪.‬‬          ‫ر‬
                                                                                           ‫نواس؟‬
                                   ‫ارضه گویتدش ‪.‬‬                                        ‫بضم اول وئالی مجهول‬


‫سیاره باشد که زحل و مشتری ومریخ و آفتاب‬                   ‫رز‬                         ‫ورسین بی لقطةٌ زده ‪.‬‬
                 ‫وزهره وعطارد وماه است ‪.‬‬                   ‫دج ‪(€7‬‬                   ‫کیاهی‌است‌معروف که‬
 ‫رو نما ‪ -‬و روی‌لها ک‪.‬نابه از (‪)۳‬‬                                                       ‫بدان جامه و ابریشم‬
 ‫هد به وتحفه‌است که در وقت دیدن روی عروی‬                     ‫رولای‬
```


## [2026-09-14T01:26:28.242Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nimport re\nfor kw in ['رایگان','راهب','رهبر','راهبان','پازند راه','صراط']:\n    hits=[i for i,p in enumerate(pages) if kw in p]\n    print(kw, [(i,i+543) for i in hits][:10])\nEOF",
 "description": "Locate raygan/rahbar in BQT v2"
}
```


### [2026-09-14T01:26:29.625Z] TOOL RESULT

```
رایگان [(114, 657), (395, 938), (396, 939), (464, 1007)]
راهب [(211, 754), (394, 937), (442, 985), (445, 988)]
رهبر [(437, 980), (446, 989), (579, 1122)]
راهبان []
پازند راه []
صراط [(51, 594), (64, 607), (124, 667), (135, 678), (230, 773), (236, 779), (265, 808), (387, 930), (388, 931), (390, 933)]
```


## [2026-09-14T01:26:43.494Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (443,444,445,446):\n    print('======== leaf',i,'≈ printed',i+543)\n    print(pages[i][:1600])\nEOF",
 "description": "BQT v2 leaves 443-446 (rah/rahbar)"
}
```


### [2026-09-14T01:26:45.189Z] TOOL RESULT

```
======== leaf 443 ≈ printed 986
  ‫رورشنه‬                                                                                            ‫”‪~A‬‬

                                                                ‫جو بنده‪ .‬کشت وزراعت پزرور و بالیده را‬
 ‫روا ‪ ۳‬وعزهبنر‌بوبا(‪ .)4‬بمعني‌روینده‬
 ‫باشد بعنی هرچیز که آززمین بروبد (‪ - )0‬ودر‬
                      ‫‪۳‬‬   ‫دبدترا گویند ‪۸‬‬       ‫عر هی خواب‬        ‫وکر ثالث ونون بتحتالی رسیده ‪ ۰‬آهن وپولاد‬
‫بنك = یمعای رو بنداست کهآ نرا‬                  ‫دوی‬

                                                                 ‫روهینا = بائالی‌مجهول بروزن موستنا»‬
 ‫روی پوش ‪ -‬بمعنی روپوش است‬                                       ‫بمعنی روهنی است که‌آهن وفولاد جوهردار باشد‬


 ‫کونایه اکزی چویزی که ظاهر وباطنش یکی‬                            ‫روهینابی(‪ - )۷‬وشمشر جرا قیمتی را نیز‬
                                                     ‫نباشد ‪.‬‬    ‫کفتماند‪ .‬وروهینیا بدو بای حطی هم بنظرآمده‬
 ‫روی خاندان د یکرنات ‪,‬کنابه‬                                                                             ‫است‪. .‬‬
 ‫از بپترین و اشرف ودودمان و خالدان باشد ‪.‬‬
                                                                 ‫رو هینی نز = عم اول وسکون انی‬
 ‫روی دل نمودن‪ -‬کنابه ازمردمی‬                                      ‫مجهول وثالث و خامی هر دو بتحتالی ر‪-‬یدهه‬
                          ‫باشف ‪۰‬‬   ‫کردن‬   ‫و گرمی واحسان‬
                                                                 ‫بمعنی روهیناست (‪ )۳‬که آهن وفولاد جوهردار‬
 ‫دوی دیدن ‪-‬کنایه از طرفگیری‬                                                        ‫باشد ‪ -‬و آلچه از آن ساز ند ‪.‬‬

   
======== leaf 444 ≈ printed 987
 ‫‪۲‬‬
                                                                                                                        ‫ررین‬
‫پر افراسیاب هم هت که در جنگ دوازدمرخ‬                            ‫بروزن علی بند » بلغت زند وپازند (‪ )۱‬سپر را‬
‫بردست بیژن پر کیوکشته شد ‪ -‬و نام یس‬                             ‫کون دکه بعربی‌جنه خوانند(‪ )۲‬ودرجای دیگر‬
‫پبران‌وسهکه او (‪ )۷‬بدست بیژ نکشته گشت‪-‬‬                          ‫ان اعلم‪.‬‬    ‫سرراگفته اند که مر نی وا کوټ‬

‫ونام ولابتی همهت ‪ - ۴‬وهرچیز را فيز گوبند‬                        ‫رولی‪ - ۱‬با الی مجهول بر وزن‬
                        ‫که از روی ‪-‬اخته باشند ©‬                 ‫بدان رنگه‬     ‫سوزن ‪ ۰‬رونای باشد که چیزی‬
 ‫رو لین (‪ )۴‬قن = لقب اسفندبار است‬                                                                                   ‫‪۲‬‬    ‫‏‪E‬‬



‫واورااسفندبار روبین(‪)۳‬نن میگفته‌اندا سوکنابه‬                    ‫بانانیمجهول » بمعنی دوین‬        ‫یوناس‬
                                                                                                    ‫ر‬
‫از معزول هم هت چه روبین تنی معزولی را‬                                                         ‫است که رونای باشد‬
                 ‫عده را گیفزته‌اند ‪.‬‬
                                   ‫کوبند م‪.‬و‬
                                                                ‫روی نسل ]دم = ‪.‬کنابه ازاشراف‬
‫زرو لین (‪)۳‬جم‪ -‬بضمخای نقطه‌دار(‪»)۸‬‬
                                                                ‫خلابق و پیغمبران باشد ‪ -‬و قرار وآرام را لیز‬
  ‫ند ‪. ۷‬‬  ‫کوس ودمامه و نقارة بکزروکیرا‬
                                                     
======== leaf 445 ≈ printed 988
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
               ‫وبمعنی پيك وقاصد هم آمده است ‪.‬‬                  ‫وبمعنی‌هوش وشمورباش
======== leaf 446 ≈ printed 989
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
```


## [2026-09-14T01:26:59.414Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('leaves',len(pages))\nfor kw in ['ارّاده','اراده','ارابه','ارتشتار']:\n    hits=[i for i,p in enumerate(pages) if kw in p]\n    print(kw, hits[:12])\nEOF",
 "description": "BQT v1 search arradeh"
}
```


### [2026-09-14T01:27:00.517Z] TOOL RESULT

```
leaves 777
ارّاده []
اراده [92, 96, 177, 252, 257, 280, 281, 321, 360, 484, 501, 527]
ارابه [306, 525]
ارتشتار []
```


## [2026-09-14T01:27:00.648Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor f in MON_part1.txt MON_part2.txt; do echo \"### $f\"; grep -c '' $f; grep -n 'ترهات' $f | head -5; done",
 "description": "Mo'in search torrahat"
}
```


### [2026-09-14T01:27:01.773Z] TOOL RESULT

```
### MON_part1.txt
99339
40294:یاوه. سخن بیفایده؛ ج. ترهات. 
### MON_part2.txt
94500
```


## [2026-09-14T01:27:06.895Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(pages[306][:1800])\nEOF",
 "description": "BQT v1 leaf 306 (arabeh)"
}
```


### [2026-09-14T01:27:07.928Z] TOOL RESULT

```
-9--
درودگری باشد . ومضفقف اکر هم هست که‌آن
کلمةٌ حرط است - و جاره را نیز گویند که
وید که در مقابل زن است
ارابه - بر وزن فرابه ۰ گردون را
گویند ٩‏ . ۱
اراقو بفتح اول و قاف و واو بالف
کشیده » بلفت رومی
نام تضمی است بشکل
دور و برنگه سیاء و
بفایت‌سلب ؛ و درمیان
کندم و علان. پسیاز
میباشد ؛ و انرا به
شيرازی‌سيمك‌خواند . #ق
آرد تن که و اف
پسرشند و بر ورمهای
کرم و صلب ضماد
کنند نرم ساژد .
ار اهو فی » با میم بر وزن فلاطونی»
- بلغت پونانی لاله را کونند . و آن باغی و
صحرابی هردو می باشد ۰ و بعربی شقایق النعمان
خوانند ۰ و نوعی دیگر هم مت که آنرا
آتربون گوند .
)۱ چش : است .
(:( چك : - وافه اعلم .
اد ان » بتشدید انی بر وزن بران » نلم
ولایتی است از آنریاجان که کنجه و بردع
ازاعمال آن است . گوند سعدن طلا و نفره در
آنجا هست (۱)؛ و می تشدید عم گفته اند ۴ -
و حنارا نیز گونند که بدان دست و پای
ار او فك ه بر وزن دماوند . بععنی
حصرت و آرژو باشد - ودجلة بفدادرا یز گویند»
وبعریی شط خوانند - وبممنی فروشن وشوکت
نیز آمده است - و نام کوهی است در نواحی ‏
همدان مشهور بالوند .
ار ا۲(۵)* بفتح اول و انی بالف کشد.
و های ساکن . بلفت رومی مسطکی را گوبند
و ابا سربی علك رومی خواند .طبیت آن
کرم و خشك است .
از بو - با بای ابجد بر وزن مهرو ؛
میوهُ ات که آنرا امرود کویند ۴ .
ار بو جینا . بکسرجیم وسکون‌تحتالی
و بالف کشیده , بلفت زند و پازند (۳) بمعتی
خربزه باشد ؟ . و آن میوه‌است عمروف و در
نختدیگر جزیره نوشته بودند که خشکی‌میان
دربا باشد وال اعلم (ع) .
اد و داد - بر وزن پهلودار , درخت
شید راگوند چه اربوامرود است ودار درخت.
) چك : ژند و باژند ۰
بطوطه این لفت را درعربی وارد کرد .
وشبةالدهر ولفث و آران وآلان.
دنایتی ۹+
```


## [2026-09-14T01:27:08.691Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '40285,40300p' MON_part1.txt\necho \"=== headword search ===\"; grep -n '^تره\\|ترهة\\|تُرَّه' MON_part1.txt MON_part2.txt | head\necho \"=== page markers? ===\"; head -20 MON_part1.txt",
 "description": "Mo'in file structure"
}
```


### [2026-09-14T01:27:08.865Z] TOOL RESULT

```
کردن» راهب شدن. (مسصم.) ترسانیدن. 
(امص.) پرستش» عبادت. 

تر ه‌بار: ع2ط-(م)هتها (- تربار) (امر.) (گیا.) 
سبزی‌های خوردنی و برخی میوه‌ها از قبیل 
کدو و گوجه فرنگی و بادنجان و باقلا و 
غبر ۵. 

ثر هه. مه [ع. ترهه ] (.) (کم.) سهو ده» 
یاوه. سخن بیفایده؛ ج. ترهات. 

تر هیب: واه [ع.] (مسص ع.) ترسانیدن) 
ج. ترهیبات. 

تریاق: ۱۵17 [معر. سبعی (منسوب به 
خاوی فک و ان( 
=== headword search ===
MON_part2.txt:43026:تره جات ۱ رز ) (پز.) گونه‌ای مرض 
MON_part2.txt:54780:تره سرد و خشکك. ۳ مزاج‌های مادی - 
MON_part1.txt:40284:ترهت. امططهته) [ع.] (مص‌ل.) عادت 
MON_part1.txt:40993:ترهای نوک‌تیز و بلسبه طویلی است که 
MON_part1.txt:50641:تره گون: (کد.) شب تاریکك. چشمة نیغ: 
MON_part1.txt:54260:تره تیز کك از اعلام مردان است. 
=== page markers? ===
0 
2 


چم 
نسم ی 


تمه موی موم 
3 


ماما نا موس ملاس 
روم و3 


2 
7 
س
```


## [2026-09-14T01:27:26.302Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '16995,17025p' ARB_mo3rb.txt",
 "description": "Jawaliqi ʿaskar context"
}
```


### [2026-09-14T01:27:26.354Z] TOOL RESULT

```
١ ١ ع 9 - مت يع 7 2 5 كر اعرسم‎ 
قال أبن دريد و‎ ٠١ فارسى معرب‎ ٠ 8 قال اءن قنبية : 4 العسر‎ 
رو لك)‎ 
53 هو ليش » بالفارسية ه وهو مجتمع اميش‎ 
26) 


5 مه سار تم وس و 5 5 5 2 0 
نت 7 عسكر مم 5 سم بأد معروتف ل قال الأزهرى 5 وكاله 


صرب ٠:‏ 
)١( :‏ ف اللسان : «وعزير امم يتصرف فته و إن كان أعميا » مثل نوح ولوط » ٠‏ وقالالإهام 
أبو البقاء المكبرى المتوق سنة 1 فى كاب إعراب القسرآن ( ؟ ؛: 7 ) : < لا يتصرف للعجمة 
ا » وهذا ضعيف» لأن الأهم عر عند أ كثر الناس » ٠‏ وقرأ عاصم والكسانى و يعقوب 
ل بالتنوين فالآب ٠‏ ادن سو رة التوية على أن ا لأسم على 6 وقرأ أ باقى الأر بعة عشر يدون تنو ين > 
وأختلف فى توحبه يما إعلم من كتب القراءات والتفسير» (١‏ الواو لم تذكر قى بف : 

(0) فى نا« وهى > ٠‏ وهو خطأ ٠‏ 09 عبارة المهرة ( ؟ 1مة) : ه والعسكر 
قاربى معرب »> !ما هوش » وهو ]آتفاق فى اللقتين » ٠‏ ولعل صوابه «أو هو اتقاق» فيُكون 
لان در يد رأيان ٠‏ والظاهى أن الكلمة عرربية ٠‏ قال ابن الأعر الى : « العسكر : الكثير من كل شىء: 
يقال : عسك من رجال » وخيل » وكلاب » ٠‏ وانظر المادةٌ فى اللسان ٠‏ 

(0) هذاغير جيد . فكلية ”عسكر'' الراخ أنها عر بية» و ””مكرم'' بشم اليم وسكون الكاقف 
وفتح الراء س هوكم بن مءزاء » أحد بنى جعونة بن الحرث » صاحب اجاج بن يوسف » أزل هذا 
الموضع , يتواحى بو زستان »6 وكانت هناك قرءة قدعة »© فيناها » رم ب زل لي ينيك ؟ وي جملها مدينة » 


قمياها اسك م ل الاسم كله شي خالص 9
```


## [2026-09-14T01:27:28.841Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor kw in ['رّاده','عراده','عرّاده']:\n    print(kw,[i for i,p in enumerate(pages) if kw in p][:10])\nEOF\ngrep -n 'ارابه\\|اراده' MON_part1.txt | head -8",
 "description": "Search arradeh in BQT v1 and Mo'in"
}
```


### [2026-09-14T01:27:29.986Z] TOOL RESULT

```
رّاده []
عراده []
عرّاده []
1921:ارابه آب به خانه‌ها رساند. (.) یکی از سه 
7492:پشت سر آنهارابه خوبی می‌توان دید. مانند: 
7551:اراده کنند که از او کراهت دارند. اجل 
7590:آنان. (فد.) اراده موٌکد که بدئبال آن حرکت 
7635:جن است و معنی بریان از آن اراده می‌شود. 
8086:به ارادهٌ محکوم علیه قابل تغییر است. (نج.) 
8410:اراده. 
8499:اراده» اختیارا؛ مق. به اجبار» اجیار ا.
```


## [2026-09-14T01:27:48.256Z] TOOL CALL #44: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-14T01:27:48.263Z] TOOL RESULT

```


```


## [2026-09-14T01:27:52.244Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B1%D8%A7%D9%87",
 "prompt": "Give the full Persian etymology section for راه (rāh) 'road, way': Middle Persian form, Old Iranian/Proto-Iranian reconstruction, cognates (Avestan, Sanskrit), and any cited sources (Hasandust, MacKenzie, Cheung)."
}
```


## [2026-09-14T01:27:53.979Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%84%D8%B4%DA%A9%D8%B1",
 "prompt": "Give the etymology of Persian لشکر (laškar) 'army': Middle Persian form, proposed origin, and whether Arabic عسكر (ʿaskar) is said to be borrowed from it. Quote the etymology text."
}
```


### [2026-09-14T01:27:57.253Z] TOOL RESULT

```
# Persian Etymology of راه (rāh)

Based on the Wiktionary entry, here is the documented etymology:

**Middle Persian Form:**
The word derives from Middle Persian *lʾs* (/rāh/, "road, way").

**Proto-Iranian Reconstruction:**
From Proto-Iranian *\*Hrāθáh*, which evolved through Proto-Indo-Iranian *\*Hrātʰás* and ultimately from Proto-Indo-European *\*Hret-*.

**Cognates:**
The entry notes a comparison with Old Armenian *ռահ* (ṙah), which was "borrowed from Middle Iranian."

**Cited Sources:**
The references section lists:
- MacKenzie, D. N. (1971) - *A concise Pahlavi dictionary* (page 70)
- Edelʹman, D. I. (2020) - *Etymological Dictionary of Iranian Languages*, volume 6

**Note:** The entry does not include specific Avestan or Sanskrit cognates, nor references to Hasandust or Cheung within the visible etymology section.
```


### [2026-09-14T01:27:57.898Z] TOOL RESULT

```
# Etymology of Persian لشکر (laškar)

**Middle Persian Form:** lškl

**Proposed Origin:** The word derives from Proto-Indo-Iranian *Hrákšati + Proto-Iranian *karah. According to the source:

> "Inherited from Middle Persian lškl, from Proto-Indo-Iranian *Hrákšati + Proto-Iranian *karah"

The text notes a comparison to Sanskrit रक्षति (rakṣati), indicating Indo-European roots rather than Arabic origin.

**Regarding Arabic عسكر (ʿaskar):** The provided content makes no mention of Arabic عسكر or any relationship between the Persian and Arabic terms. The etymology focuses exclusively on the Indo-European lineage through Middle Persian and Proto-Indo-Iranian sources.
```


## [2026-09-14T01:28:06.120Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B1%D8%A7%D9%87%D8%A8",
 "prompt": "Give the Arabic etymology of راهب (rāhib) 'monk': the root, related words (رهب rahiba 'to fear', رهبان ruhbān), and any mention of a Persian origin. Quote the etymology."
}
```


## [2026-09-14T01:28:08.415Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B1%D8%A7%DB%8C%DA%AF%D8%A7%D9%86",
 "prompt": "Give the etymology of Persian رایگان (rāygān) 'free, gratis': Middle Persian form and its origin (is it from rāh 'road'? from rāy?). Quote the etymology and any cited sources."
}
```


### [2026-09-14T01:28:10.686Z] TOOL RESULT

```
# Arabic Etymology of راهب (rāhib) 'monk'

**Root:** ر ه ب (r h b)

**Etymology:** According to the Wiktionary entry, the word is "Perhaps derived from the active participle of _رَهِبَ_ (rahiba, 'to dread'), from the root ر ه ب (r h b), with the intermediate meanings 'dreader', 'God-fearer', 'God-worshiper', 'venerator'."

**Related words:**
- رَهَب (rahab) — "veneration, respect"
- رَهْبَة (rahba) — "terror; dread; awe"

**Note on Persian:** The entry does not indicate a Persian origin for this word. Instead, Persian borrowed the term from Arabic: "Borrowed from Arabic _رَاهِب_ (rāhib)."

The word originates in Semitic Arabic and subsequently spread to Persian and other languages through borrowing.
```


### [2026-09-14T01:28:13.334Z] TOOL RESULT

```
# Etymology of Persian رایگان (rāygān)

According to the Wiktionary entry, رایگان derives from two Persian components:

**Etymology:** "From _[راه](/wiki/%D8%B1%D8%A7%D9%87#Persian "راه")_ (râh, "way") + _[ـگان](/wiki/%D9%80%DA%AF%D8%A7%D9%86#Persian "ـگان")_ (gân)."

**Proto-Iranian Origin:** The entry shows an etymology tree tracing back to Proto-Iranian *Hrāθáh, which became Middle Persian lʾs, then Persian راه (râh, "way").

The word literally compounds "way/road" (راه) with the suffix ـگان (gân), semantically evolving to mean "obtainable without payment, free."

The entry does not cite specific scholarly sources for this etymology—it presents the derivation as established lexicographic information on Wiktionary.
```


## [2026-09-14T01:28:20.859Z] TOOL CALL #49: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B9%D8%B1%D8%A7%D8%AF%D8%A9",
 "prompt": "Is there an Arabic entry عرادة (ʿarrāda)? Give its meaning and etymology (siege engine? from Persian?). Also note any Persian entry."
}
```


### [2026-09-14T01:28:22.235Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-14T01:28:23.046Z] TOOL CALL #50: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A7%D8%B1%D8%A7%D8%A8%D9%87",
 "prompt": "Give the etymology of Persian ارابه (arābe) 'cart, chariot' — origin, Middle Persian, Arabic عربة, any relation to راه or Avestan raθa-."
}
```


### [2026-09-14T01:28:26.334Z] TOOL RESULT

```
# Etymology of Persian ارابه (arāba)

Based on the Wiktionary entry, the word is "Borrowed from Turkic, from the same source as Turkish _araba_."

The page does not provide information about Middle Persian origins, Arabic عربة (Arabic *carriage*), connections to راه (*path/road*), or Avestan *raθa-*. The etymology traced here focuses on the Turkic borrowing pathway rather than deeper Indo-European or Semitic roots you've inquired about.
```


## [2026-09-14T01:28:36.186Z] TOOL CALL #51: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%B9%D8%B1%D8%A7%D8%AF%D9%87/",
 "prompt": "Give the Dehkhoda and Mo'in entries for عراده / عرّاده: meaning and any etymological note (Persian origin? منجنیق? ارابه?)."
}
```


## [2026-09-14T01:28:37.752Z] TOOL CALL #52: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%A7%D8%B1%D8%A7%D8%AF%D9%87/",
 "prompt": "Is there an entry ارّاده (arrâde) meaning cart/chariot or catapult in Dehkhoda or Mo'in? Quote it with any etymological note."
}
```


### [2026-09-14T01:28:42.092Z] TOOL RESULT

```
# عراده/عرّاده: Dehkhoda and Mo'in Entries

## Dehkhoda Dictionary

**Primary definition**: A military apparatus resembling a catapult (منجنیق), smaller in scale, used in ancient warfare to hurl stones at enemies. Also called "حصارگشای" (fortress-breaker).

**Etymology note**: The entry cites "غیاث اللغات" as source. A secondary geographic meaning appears: "a settlement on a hill-like formation between Ras Ayn and Nisibin where caravans unloaded cargo" (from معجم البلدان).

## Mo'in Dictionary

The Mo'in entry provides two senses:

1. **Military weapon**: "از ابزارهای جنگ شبیه به منجنیق که در قدیم برای پرتاب سنگ ازآن استفاده می کردند" — a war implement similar to the catapult, historically used for stone-throwing.

2. **Unit of measure**: A counting unit for artillery pieces (واحد شمارش توپ).

**Note**: Neither entry explicitly addresses Persian etymological origins; both reference comparison with منجنیق and historical military application.
```


### [2026-09-14T01:28:42.978Z] TOOL RESULT

```
# On "اراده" (arrāde) as Cart/Chariot

Based on the dictionary content provided, there is a secondary meaning listed in **Farhang-e Mo'in**:

> "(اَ رّ دِ) (اِ.) گردونه، ارابه"

This indicates an alternate pronunciation and meaning: **"wheel, cart/carriage."**

The entry also appears in **Farhang-e Farsi**: "۱ - گردونه [ارابه](/fatofa/ارابه/). ۲ - قسمت زیرین هواپیما..." (wheel/cart and aircraft landing gear components).

However, the provided text contains **no etymological notes** explaining the origin of this mechanical sense. The dictionary simply lists it as an alternate form without historical or linguistic derivation information.
```


## [2026-09-14T01:28:59.264Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PLA arrada ===\"; grep -n -i 'arrāda\\|arräda\\|arrada' incoming/PLA/PLA_pages.txt | head\necho \"=== AFM عرادة ===\"; grep -n 'العرادة\\|عرادة' AFM_pages.txt | head\necho \"=== TAD عراده ===\"; grep -n 'عراد' TAD_pages.txt | head\necho \"=== LKT ===\"; grep -n -i 'arrada\\|laschkar\\|laskar' LKT.txt | head",
 "description": "Search ʿarrāda in Arabic loan sources"
}
```


### [2026-09-14T01:28:59.362Z] TOOL RESULT

```
=== PLA arrada ===
877:           Sarräda                "Geschützlafette,                              Wurfgeschoßrad"                        heißt.       °c     ap.       rada,     aw.
=== AFM عرادة ===
=== TAD عراده ===
=== LKT ===
758:'Gefäß  mit  2  Henkeln,  um  darin  Wasser abzukühlen'  [vom  Vh.  barrada  'kalt, kühl  machen'  s.  hier  Nr.  241];  hieraus mit  ar.  Art.  sp.  albarrada  'Wand  aus trockenen  Steinen',  pg.  albarrada  'Vase für  Rosen  oder  andere  Blumen'  [in dieser  Bedeutung  wohl  Kontamination mit  ar.  warräda  aus  ward  'Rose'], 'Mauer  aus  losen,  also  trockenen  Steinen' [Constancio  Dicc  43  c].    [DE  68/69.
2604:'Krug  mit  engem  Halse',  also  wohl  ge- eignet, das  Wasser  frisch  zu  halten [vielleicht  aus  dem  Pers.  JA  (8)  I,  545; Lammens  Faruk  961];  hieraus  mit  ar. Art.  sp.  pg.  alcarraza  'irdener  Krug, Wasserkühlgefäß'  [dass.  wie  albarrada, s.  hier  Nr.  249;  DE  86/87],  prov.  alca- razas,  frz.  alcarraza.  —  „Diese  werden von  Frauen  [sc.  Spaniens]  besonders  im Zustande  der  Schwangerschaft  gern  zer- brochen und  gegessen ;  der  Genuß  ihrer Scherben  soll  gleichzeitig  auch  die  Haut weiß  färben."  Dtsch.  Rundschau  für Geographie.  Wien-Leipzig.  XXVH,  126. [Eguilaz  133.  Devic  DEt  7.  Lammens Rem  7/8.    ML  4743.
2949:'Ohrring',  plr.  akrät;  hieraus  mit  ar. Art.  sp.  arracadas  'dass.,  Ohrgehänge', pg.  algarradas  'Ohrläppchen'  [?  nach DE  86].
3045:'Heer,  Feldlager'  [verwandt  mit  ar.  'as- kar,  byzantinisch-gr.  dEdpKr|TOv,  lat.  e.xe)-- citus,  von  denen  das  lat.  Wort  wohl das  ursprüngliche  Grundwort  ist;  doch sind  die  Entlehnungsverhällnisse  der übri^'en  Formen  noch  ungeklärt,  vgl. z.  B.  VÖLLERS  in  ZDMG  L,  64G,  der das  ar.  Wort  aus  dem  Pers.  entlehnen will;  neuerdings  wird  ar.  'askar  auf  gr. äöKctpioq  'Schlauch-,  Wasserträger'  zu- rückgeführt, vgl.  Streitberg-Festgabe. Leipzig  1924.  S.  233];  hieraus  engl, angloind.  /«scar 'Seemann'.der  zu  Fahrten auf  den  tropischen  Meeren  angeheuert wird,  da  Europäer  in  der  doppelten Gluthitze  der  Tropensonne  und  des Kesselraums  nicht  arbeiten  könnten. Man  unterscheidet  den  sea-lascar  'Ma- trose' vom  gun-lascar  'Hilfsmann  bei der  Artillerie'  und  dem  tent-lascar  'Zelt- aufschläger'. Ebenso  frz.  lascar;  dtsch. Laskare;  pg.  lascar,  lascar  im,  liscarim [Constancio  Dicc648c].  [Hobson-Jobson .507/509.  Devic  DEt  1.51.  Lammens Rem  145.    Eguilaz  436.
5798:Laskare  1307
7932:algarradas  1260
7966:albarrada  249
9796:arfor  501 adraja  485 aduana  526 aduar  502 adufa  538 adufe  537 agengibre  1930 oguajaque  2168 aguanafa  1535 ahorrar  886 ajarafe  1840 «;e&e  1735 ajedrea  1872 ajedrez(atama)  1871 ajimenez  1815 ajimiz  1816 ajonjoU  744 ajorca  1951 ajovar  1959 ajuar  1959 alabarda  823 alabega  761 alacena  871 alacran  4:1 alafia  24 alahilca  904 alamar  67 alambar  78 alambique  79 alambre  78 alameda  1364 alamud  72 alancel  1428 alaqueca  45 alarbe  89 alarde  94 aZaWf^o  59  d.  100 I  alarife  99 alatar  134 alazan(o)  870 albacea  2158 albaheca  761 «Zöate  226 albanilear  216 albanal  204 nlbanar  204 albani(r)  216 albanil(esco)  216 alhaqida  188 albaran  226 albarazo  224 ffife«r(/a  228 albardän  241 a/fcarrfi  dial.  242 albardin  242 albaricoque  247 albarrada  249 albarrän  251 albarrana  251 albarraz  762 albayaldar  6 albayalde  6
```


## [2026-09-14T01:29:01.359Z] TOOL CALL #54: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B9%D8%B3%D9%83%D8%B1",
 "prompt": "Give the Arabic etymology of عسكر (ʿaskar) 'army, camp': is it said to be from Middle Persian lašgar / Persian لشکر? Quote the etymology and cited sources."
}
```


### [2026-09-14T01:29:06.385Z] TOOL RESULT

```
# Arabic Etymology of عسكر (ʿaskar)

Based on the Wiktionary entry, the Arabic word عسكر is indeed said to derive from Middle Persian. Here's what the source states:

**Etymology Quote:**
"Probably from Middle Persian lškl (/⁠laškar⁠/) with the -l- interpreted as the Arabic article ال (al-)."

The entry notes this etymology is "less likely" compared to an alternative Latin origin (from *exercitus*), though the Middle Persian derivation is presented as the primary explanation.

**Supporting Evidence:**
The article references modern Persian لشکر (laškar) as a cognate, suggesting a shared origin. This Middle Persian term was borrowed into Arabic and subsequently spread to numerous other languages through Ottoman Turkish and other intermediaries, eventually reaching languages as diverse as Indonesian, Russian, Greek, and Serbo-Croatian.

The etymology demonstrates how military terminology traveled across linguistic and cultural boundaries through trade routes and imperial contact.
```


## [2026-09-14T01:29:13.448Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('incoming/PLA/PLA_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nprint('\\n'.join(lines[860:895]))\nidx=sum(len(l)+1 for l in lines[:877])\nprint('LEAF',t[:idx].count('\\f')+1,'printed',t[:idx].count('\\f')+1-15)\nEOF",
 "description": "Asbaghi ʿarrāda entry"
}
```


### [2026-09-14T01:29:14.523Z] TOOL RESULT

```
Pt               - Adarkün:                        "wilder            Mohn"              aus    dem       pers.        J_;T adargün           5 mp.            Sina»,
           91; Atürgonag                            6, mand.               adrin,              syr.       went.

gl          -         ädarahs               = ägargafn                 a.     v.


on.              -        ädaryün             = ädargün                q. v.


weyt -’adgän:                           Pl. v..5; dagan q. v.

6451 -’adnaba: Pl. v. _, danb q. v.

li          -         ’aräba:               "Wagen"              pers.        7, die                arabisierte              Form   heißt        As araba          u.
           Carabäna,                    davon             russ.        serb.              arab          "Wagen"        8,
       Der                Verfasser                 v.        Bahär        ul-CAam                  ist       der Ansicht,           daß araba         eigentl.
           Sarräda                "Geschützlafette,                              Wurfgeschoßrad"                        heißt.       °c     ap.       rada,     aw.
           rava             10        mand.              arada        11,


al          -         ’aräßa:               "Steuer;                 Archiv"              pers.          12     wahrscheinlich             ist    es    eine
       kontrahierte                                Form        v.,    abär       bzw. ’awärka                     s.    äbär     u. ’awärda       .

      \;              >      -                                       —,,         -                  3     -
lt -                      ”aräyik:            Pl.         v.     ol         ’arika             s.       arika     .


1.    Nyberg                 Bd.        II         s,.    v.
2.    Macuch                 s,       v.
3.    LD.             s.     v.
4.    Mackenzie                       Ss.     v.
5.    Addai                 Scher           s.      v.,        Steingaß                  s.    v.
6.    Bundahitn                       S.      57
7.    LD.             s.     v.,        Johnson                S.     V.
8.    Lokotsch                    Ss.       v.
LEAF 23 printed 8
```


## [2026-09-14T01:29:34.010Z] TOOL CALL #56: Bash

```json
{
 "command": "ls site/pages/422.jpg 2>/dev/null; pdftoppm -f 422 -l 422 -r 200 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg422 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg422.png",
 "description": "Render PDF page 422"
}
```


### [2026-09-14T01:29:36.035Z] TOOL RESULT

```
site/pages/422.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb 66285 Sep 13 21:29 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg422.png
```


## [2026-09-14T01:29:37.962Z] TOOL CALL #57: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg422.png"
}
```


### [2026-09-14T01:29:38.547Z] TOOL RESULT

```

```


## [2026-09-14T01:29:38.542Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-14T01:30:05.096Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '13080,13130p' CHEUNG.txt",
 "description": "Cheung rad entry"
}
```


### [2026-09-14T01:30:05.220Z] TOOL RESULT

```
«PIE *H,leng""- ‘to spur, impel, incite (to act, work, run, etc.)’ = LIV: 247 | Pok.: 
660 f. 

*IE COGNATES: Olrish lingim ‘I jump’, OHG gi-lingan ‘to take place, succeed, have 
success’, NHG gelingen 

*REFERENCES: Christensen, Contributions I: 163, 260; Christensen, Contributions II: 57, 115; Abrahamian 
1936: 119; Andreev — PeSéereva: 313a; Gershevitch, Mithra: 181 f.; EVS: 68a; Nyberg II: 71b Ё; Werba 
1997: 223 


*Hrau ‘to warm’ 

*CHORESMIAN: (+ *pati-) pery- ‘to become warm’, pcr’w- (caus.) ‘to make warm’ 
= Samadi: 143 

*NEIR: (+ *4-) Oss. I. arawyn/aryd, D. arawun/arud ‘to scorch in the fire’ 

*SANSKRIT: ravi- (m.) ‘sun(god)’ (Up.+) > EWAia II: 440 

«PIE *H>reu- ‘to shine’ => LIV: — | Pok.: 873 

*IE COGNATES: Hitt. /haruyanai-/ ‘to become bright, dawn’, Arm. arew ‘sun’ 
*REFERENCES: Abaev, Slovar’ I: 57 f. 


*(H)raud ‘to tear, break’ 

*NEIR: (+ *us-) Yzgh. sori0-/sorust ‘to break, tear [intr.]’, sarand- (caus.) ‘to break, 
tear [tr.]’ || (+ *pati- ?) Yzgh. pərci0-/pərcust ‘to be torn’, porcand-/porcust (caus.) 
‘to tear [tr.]’ (with meatathesis: -cr- > -rc- ?) || (+ *para-, *pari-) Sh. (Baj.) piri0-/ 
pirüst, Rosh. рагё0-, pared-/paröst, Bart. paré0-/partist, Orosh. pira0-/pirist, Sariq. 
pirad-/pirüst ‘to burst, tear [intr.]’, Sh. pirénd-/pirént, Rosh. parend-/parent, Bart. 
parend-/parend, parent, Sariq. parin-/parind (caus.) ‘to tear, burst [tr.]'. O Not from 
*rad- (i.e. *(H)ra(n)d), pace Morgenstierne, EVS\: l.c. Most, if not all, intransitive 
Pamir forms, especially with a front vowel, may derive from the pres. (or pass. ?) 
formation *(H)r(a)ud-ia- (^ *(H)r(a)u0-1á- ?). 


*Hraud 193 


© The evidence for an Ir. root *(H)raud, which would derive from IE *(H)reud-, is 
limited to modern Pamir forms. 

«PIE *(H)reud- ‘to tear, break up’. 9 The reconstruction of an initial laryngeal is 
based on the premise that IE roots cannot begin with an initial *r-. = LIV: — | Pok.: 
869 

*IE COGNATES: Lat. rudus ‘(broken) rocks, gravel’, Olrish road ‘ruins’, Welsh (pl.)
```


## [2026-09-14T01:30:10.408Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n '^\\*(*H*)*ra' CHEUNG.txt | head -30",
 "description": "Cheung roots starting ra"
}
```


### [2026-09-14T01:30:10.475Z] TOOL RESULT

```
12585:*Hrab/f ‘to go’ 
12615:*Hrab/f3 (*ra(m)b?) 185 
12627:*Hrab/f ‘to attack, fight’ 
12659:*Hrab/f (*ra(m)b?) ‘to touch, affect, grab ?" 
12687:*Hrad ‘to dig, pave’ 
12712:*HraH ‘to offer, give’ 
12741:*Hraié 187 
12753:*(H)raHd ‘to succeed, accomplish’ 
12778:*Hraié ‘to pour, flow’ 
12840:*HraiH ‘to defecate’ 
12873:*Hraiz 189 
12880:*Hrais ‘to be torn, tear, cut, split’ 
12913:*Hraiz ‘to shake’ 
12940:*Hrak ‘to shelter, take refuge ?’ 
12974:*Hram ‘to rest, be calm’ 
13001:*Hranj 191 
13043:*Hranj ‘to take action, spur, urge (often with negative consequences) ?’ 
13092:*Hrau ‘to warm’ 
13107:*(H)raud ‘to tear, break’ 
13115:*rad- (i.e. *(H)ra(n)d), pace Morgenstierne, EVS\: l.c. Most, if not all, intransitive 
13120:*Hraud 193 
13138:*Hraud ‘to grow (bigger)’ 
13195:*(H)raudH ‘to moan, (be)wail’ 
13224:*HrauH (*HrabH ?) ‘to crackle; growl’ 
13248:*Hraup 195 
13259:*Hrauj ‘to belch’ 
13280:*Hraup ‘to tear, break; to suffer from pain’ 
13330:*Hraxš ‘to protect, defend’ 
13356:*Hraz ‘to draw a line; to direct, richten’ 
13379:*Hraz 197
```


## [2026-09-14T01:30:14.318Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '12687,12712p' CHEUNG.txt; echo \"==========\"; sed -n '13330,13360p' CHEUNG.txt",
 "description": "Cheung *Hrad and *Hraxš"
}
```


### [2026-09-14T01:30:14.397Z] TOOL RESULT

```
*Hrad ‘to dig, pave’ 
*AVESTAN: Y Av. raó- ‘to pave (a way)’, ? YAv. “pai0m raó- ‘road-paver’ (Yt 9.23). 
9 The long vowel of this hapax form is perhaps from the nominal derivative, on 


which see Kellens 1984: 116, 118 fn. 7f. — Liste: 56 
Pres. them.: IND. 3sg. YAv. raóaiti (Yt 10.68) 


*NWIR: Bal. rast'/raó- ‘to tear up the ground, be beaten’ 

*NEIR: (+ *fra-) Sh. (Baj.) raró-/ruxt ‘to dig, excavate, hollow out’, ? Rosh. rarö-/ruXt 
*to demolish, destroy, scatter? 

*SANSKRIT: rad ‘to dig, gnaw; to pave’ (RV+) = EWAia П: 430 

© The laryngeal disappeared in IIr., on which see further Lubotsky 1981: 134 ff. 

«PIE *HreHsd- ‘to gnaw, furrow’ (A.L.) = LIV: 497 | Pok.: 854 


*IE COGNATES: Lat. rödere ‘to gnaw (at) 
«REFERENCES: EVS: 68b; Shahbakhsh: s.v. raó- 


*HraH ‘to offer, give’ 
==========
*Hraxš ‘to protect, defend’ 

*KHOTANESE: (+ *pati-) parssa- ‘antidote’ 

*SOGDIAN: (+ *4-) BSogd. ’’r’xs ‘to rely on, trust, take refuge with’ 

Pres.: IND. 3sg. BSogd. ’’r’xst, SUBJ. 35р. BSogd. ’’r’xs’t, 3р1. BSogd. ’’r’xs’nt, SUBJ. 3pl. BSogd. 
”r’xs’nt, Perf.: IND. 3sg. BSogd. ’’r’xs’t 6’rt; Inf: BSogd. ’’r’xs’y, pret. BSogd. ’’r’xs’t 

*NWIR: NP laskar ‘army’ (dissim. loss of -x-, from *Hraxsa-kara-) 

*NEIR: (+ *4-) Oss. І. areexsyn/araxst, D. arzexsun/araxst ‘to fit, match; to deal, cope 
with; to be able’ 

*MISC: Arm. (LW) erasxi-k‘ ‘warrant, security’ (Benveniste 1945: 71) 

*SANSKRIT: raks” ‘to protect, guard’ (RV+) > EWAia II: 422 

9 This root goes back to an apparently old ingress. stem, which has a cognate in Gr. 
*PIE ingress. *Holek-s^/;- ‘to defend, protect” = LIV: 278 | Pok.: 32 


*IE COGNATES: Gr. &A€Ew ‘I ward off, defend’ 
*REFERENCES: Abaev, Slovar’ I: 59; DKS: 233b f.; Werba 1997: 468 


*Hraz ‘to draw a line; to direct, richten’ 
*AVESTAN: Y Av. raz- ‘to draw a line; to direct, richten’ || (+ *ham-) ‘[med.] to rise, 


become erect; to comb’ = Liste: 56f.
```


## [2026-09-14T01:30:31.928Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n 'bahnen\\|Bahn  brechen\\|ebnen' BRT.txt | head -20\necho \"=== search Yt 10.68 raôaiti forms ===\"; grep -n 'radaiti\\|raöaiti\\|ra%aiti\\|raSaiti' BRT.txt | head",
 "description": "Bartholomae raδ- 'to pave'"
}
```


### [2026-09-14T01:30:32.028Z] TOOL RESULT

```
=== search Yt 10.68 raôaiti forms ===
```


## [2026-09-14T01:30:46.843Z] TOOL CALL #62: Bash

```json
{
 "command": "timeout 900 python3 tools/ref_page.py BQT:1895 --image 2>&1 | tail -40",
 "description": "BQT page 1895 (laškar)"
}
```


### [2026-09-14T01:30:54.578Z] TOOL RESULT

```
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1895.png
REF: BQT:1895  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 692  OCR-lang: fas

بیان پازدهم
در لام با شین قرش مشتمل بر شش لغت
زد ۱ * بش اول وسکون ثانی؛مخفف نك ۴ « بفتح اول وسکون ثانی‌وکاف,
لوش است که لجن باشد و آن کل و لای تید* | بممنی پاره باشد که لشغك لغك بعنی پاره پاره -
و سیاه است که در ته تالابها و بن حوضها بهم و بمعنی شبتم هم‌آمده است و آن رطوبتی باشد
۳ : در هواکه برروی زمین و سبزه نشیند و مانند
لشتن - بح اول پروزن گشتن ۰ بعمنی برف زمین را سفیدکند ‎٩‏ ؛ و بان «عنی بکسر
تماغا وتفرج باشد - ویکسر اول. بممتی‌لینیدن | : ۱
بعنی زبان برچیزی مالیدن ۴ . اول هم‌آمده است .9۳
‎٩‏ علوش : ۹
صاف باشد زلال دولت تو تبره شد آب دشمنانت ز لش .
پور بهای جامی « جهانگیری » .
۴ - لش بفتح اول * لاش لاشه بمعنی جیفه » مردار » جد بیروح - کشته و پوست
کندهکاو و کوسفند وامتال‌آن - سخت بیکاره » تنبل - بیعار » بی‌غیرت « لفت نامه > .
۴ دلیعتن * لیسیدن » از ربشهٌ پارسی باستان لا » 2119012281 ۳ فارسی‌لشتن
زمان حال 18123001 5 ۳ فارسی 182280 ۵ ( نظیر نوشتن : نوبم)» 188880 پدید آمده
« هوبعمان ۹۵۶ > » پهلوی 1190128 , 1)1(8128 ۰ ارمنی 12677 ۰ 11280 » وخی 115-87
رك : اسشق ۹۵۶ . در اراك ( سلطان] باد ) 16512128 « مکی‌نژاد » :
امتندآستانت بزرگان ومهتران چون بوز پیرلشته بلب کاسةٌ پنیر .
سوزنی سمرقندی « جهالگیری >
۳ لشکه (ه.م.) 8 - ظ . مصحف « بشککه > (ه.م.) ‏ پشکه .

۵ لشکر - بفتح اول وسوم معرب‌آن عکر « داثرةالمعارف اسیلام *قلمه » از اینکه لشکر
به 7 عسکر» تعریب شده بعضی <دس زده‌اند که «ش » اصلی نیست . کر عربی در حقیقت از
کلمه‌ای مانند 0128187 یا 22812۴8۴ ناشی شده. انجمن آرای ناصری لشکر را از « لشکه »
( قطمه . باره ) ناغی میداند . ولی با این وجه موجب پیدایش حرف آخر نامعلوم امت
( 1۰ 1۵1۵ ,70 0۰ , ۳۳۵۵۵۷۹۵۲1۵۴ ,و5141 ) قول هدایت براساسی مبتنی نیست«لفت
نامه». آقای پورداود احتمال میدهند که این کلمه از اوستابی 72186512172 وپهلوی2۳11510127
( رزمی » سپاهی ) (رك : ص ‎٩۷‏ ح ۵ ) ناشی شده . بدین وجه رتشتر * رشتر * لشتر , اما
تبدیل لشتر به لشکر بمید مینماید ؛ کردی اع 168121۳ ( قشون ) « ژابااص ۳۷۹ > ؛ مجموعةٌ
سیاهیان » خیل , قشون :

سپاه اسك و رای و داش فزون به از لشکرکشن بی رهنمون .
ابوشکور بلخی « لفت نامه > .
- در اصطلاح نظام کنونی يك لشکر مر کب ازچند ( معمولا چهار ) هنگه ( فوج ) است -
```


## [2026-09-14T01:31:10.785Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (305,307):\n    print('======== leaf',i)\n    print(pages[i])\nEOF",
 "description": "BQT v1 leaves 305,307"
}
```


### [2026-09-14T01:31:11.888Z] TOOL RESULT

```
======== leaf 305
و تشنگی را فرو نشاند - و بفتح اول ‏ و کسرثالث
در غربی اهر بدربافتن است یمتی دریاب .
آذرد م6 - بروزن ادهم, نمدزین وئکلتوی
اسپ را گوند .
ادر مکش ع بفتح کاف و سکون شبن
نقطه دار » : نمعت ادرام است که درفش تکلتو
دوزی باشد .
اذر مه .- ی وزن صردمه » نمدزین
و را گویشد .
اذر نگ » بر وزن بدرنگ » بمعنی
محثت و رنج و هلااکت باشد » و حربی دمار
خوانند .
اد یس «» بکسر اول بروزن برجیس»
تام عخ یغمبری است مشپور . گونند از جپت دری
کنتن مبار د ین نامعلم شد . واورا مثلث النعمة
خوانند و نعمای ثلثهٌاو یادشاهی و حکمت ونبوت
بود » و اوحیات جاوید بات و اکنون در بپشت
می پاثف .
ادر بیس خانه - کنابه از بپشت
اصت:
ار « بفتخ غین نقطه دار بروزن سر صر »
بمعتی با گیر است .
اذل ه بنتح اول و ضم ثانی و سکون
کاف » فرج زنان و حیوانات دیگر باشد که‌آن
موضم جماع ایبشان است ‏
آذهن » بنتح اول و میم و سکون ثانی
(۱) چك : ژند ویاژند .
ادبون
و نون » مك خالس را کویند و بعربی اذفی
خوانند .
اذو ای < با واو بالف کشید. بر وزن
یکتای . بلمت زند و پازند (۱) بنعنی آوازباشد
و سربی صدا گوینه ٩‏ .
آذوس ‏ بفتح اول و ضم‌تانی وسکون
واو و سن بی نقطه , کسی را کویند که پسبب
علتی چشم او تاریکی کند - و شبکور را یز
کشته اید .
آذوی ه بتم اول و کر اث
وسکون ثالی و تحتانی مجهول , داروبی است که
آبرا اکر تر کی گویشد ووج دیز خوانند -
ویعتی گونند داروبی است که آنرا بعربی صبی
خوانند .
ادهحا یاها وجیم بروزن بدلقا » بونة
پر خارست که چون بر جابی بجسبد (۲) جدا
کردن از آن بسیار دشوار باشد .
ادیان » بروزن حذیان. چاروای‌دوندسرا
گویتف. .
ادذم ه بر وزن تدم . بععنی چرم
و بوست باشد - و بعضی بلفار را ادیم کوید ۳
وان پوستی باشد خوشبوی وعوج دار ورنگین.
کویند که از تابش ستار سهیل آن دنک بهم
هیرسالك . . .
آدون » بر وز ن گردون» بمعنی ادیان
است که چاروای دونده باشد . #
اواز ۰ < بونکر ٩۲‏ ‌.
======== leaf 307
ی
"ار پیاسیوس - با تحتانی و سین بی
نقطه و تحتالی دبکر بروزن مرد چایلوی . نام
حکیمی بود (۱) از یونان . گویند در علم طب
مپارنی تمام واخته است ۷ .
ار بیان س بر وزن بهلوان » علخ آبی
باشد و بعربی جرادالبحر
گوند . قوت, باه دهد
وبلفت اهل شام کل‌بابه نه
را گویند . اربیان
از تا - با نای قرشت پروزن برصیصاء
بلفت زند و پازند (۲) بام خانه را کوبند ۴ .
اد فا ه با تای قرشت بروزن فردا , بلفت
زند و پازند (۲) بوم و زمين را کویند ۴ .
ار تحك « بنتح جم بر وزن اسپرك :
برق برادر رعد را کوشد » و بکسر جیم حم
شظن آمده است . ۶ه
ار نگ » بر وزن فرهتگه » نگارخانة
مانی نقاش باشد - و نام بتخانةٌ چين هم هست -
و کی لت که لا مایت ما من
تقش است ؛ و بضی این لفت دا بجای حرف
ئالك ثای مثلثه آورده اند و کفته اند کهدرافت
فارسی بغیر از اين لفت و لغت ثغ بثای سه نقطه
)۱( چك : بوده .
و غین قطه دار دیگر لفتی بثای سه نقطه نبامده
است ۰ وئغ‌بت را کویند وعربان صنم خوانند .
ار تشدار * - با :حتالی مجهول
وشین فرشت و دال ابجد بر وزن پرهیز کار ؛
لشکری و سیاهی را گونند - ونم رود خاله‌ایست
بسپار بزرکث در حدود قبجاق .
از ث_بانای مثلئه بر وزن ابجد . نام
بیخی است که تخم آنرا فلفل بری و حب‌الفقد
خوانند و بات آنرا پنجنگشت و ذوخمة اوراق
ادج - بفتح اول و سکون الی و جیم
بمشی قدرو قیمت ومرتبه و حد واندازه‌باشد ۷
چه ارجمند صاحب فدر وقیمت و مرتبه را گویشد
و مند بمعتی صاحب و خداوند آمده اه نت
وبمعتی کندن و جدا کردن هم هست - ونامعرغی
است که پرهای او بسیار نرم میباشد و در میان
بالش کنند و بترکی قو ۷ خواند - وک رکدن
را نیز گفته اند وآن جانوری است درهندوستان-
شبیه بکاومیش لیکن برسر بینی شاخی دارد -
و بمعنی قیمت و بها و آرزش هم هت .
از جاسپ+۸ ۰ بر وزن طهماب ۰ نام
برة فراسياب است که در تون پدتاه ی کرد
و درروینه دژ (۳) ٩‏ مسکن داشت وچندین یس
(۳) چش : رومینه دژ .
9
۴ - رك : ارژنك .
دراوسثا ۲2۲26510412 و در گزارش بهلوی
استاده ۰ مهبای جنگ
س ۵۱6-۵۰4 * .
بقه در صفحهٌ ٩۸‏
```


## [2026-09-14T01:31:31.960Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== FFD p56 ===\"; python3 - <<'EOF'\nt=open('incoming/FFD/FFD_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('leaves',len(pages))\nimport re\nm=[i for i,p in enumerate(pages) if 'راه' in p]\nprint('راه leaves',m[:20])\nfor i in m[:3]:\n    print('--- leaf',i, pages[i][:500])\nEOF",
 "description": "FFD search rāh"
}
```


### [2026-09-14T01:31:32.982Z] TOOL RESULT

```
=== FFD p56 ===
leaves 115
راه leaves [7, 9, 14, 16, 20, 28, 111]
--- leaf 7 [pdf page 8]
۱ راهنمای نشانه‌ها
الف -نشانه‌های الفبایی

نشانه شرح

3 فتحه عربی

کسرهٌ عربی

3 ضمه عربی

3 آ

7 ی در واژهٌ «گیره»

57 و در واژهٌ «سرود»

3 یای مجهول» کسرة کشیدهٌ فارسی امروز ایران
5 واو مجهول. ضمةٌ کشیدٌ فارسی امروز ایران
6 بت

از پِ

1 ت‌

--- leaf 9 [pdf page 10]
راهتمای نشاند ‏ ست و
بلند, به جای آن که بنویسند 2: کوتاه» 2: بلند» می‌نویسند: 3.
+ : مراجعه شود.
<: منشأٌ واژه را نشان می‌دهد.
(:): وقتی نشانه‌ای در میان ( ) گذاشته می‌شود. آن نشانه ممکن است باشد یا
نباشد. به‌جای آن که پنویسند 38 و 133 می‌نویسند: ([)133.
دلالت می‌کند بر این که:
۱-تلفظ فرضی است.
۲ -معنی فرضی است.
۳-وازژه فرضی است.
[ ]: آنچه در میان [ ] آمده برای روشن‌شدن مطلب افزوده شده است.

--- leaf 14 [pdf page 15]
وا ففلهای فارسی دری
افزوده صورتی از واژه بوده» که در آن 2 وجود داشته و صورت بالانده صورتی از واژه
بوده» که در آن 5 به جای 2 می‌آمده است. اگر در صورت افزودة واژه یا 18 وجود
۱ داشته» حذف آن دو سیب ضعیف شدن واژه می‌شده است:
صورت ضعیف صورت افزوده صورت بالانده
3 ۵7 57 : بردن
120 1 40 : بستن
822 3رد نحرکت کردن
در ایرانی باستان اسم و صفت و ضمیر صرف می‌شده‌اند. اسم و صفت و ضمیر
هشت حالت: فاعلی, مفعولی» مفعولی‌له. مفعولی‌عنه» مفعولی معهء مفعولی فیه. اضافی
و ندایی» سه جنس: مذکره مونث و خنثی»
```


## [2026-09-14T01:31:35.555Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN rotate/roulette/control ===\"; grep -n 'roulette\\|rotund\\|^rota,\\|rota, n' KLN_1966.txt | head -10\necho \"=== WLD Bd2 368 ret ===\"; grep -n 'rotundus\\|rota ' incoming/WLD/WLD_Bd2_pages.txt | head -10\necho \"=== IEC ===\"; grep -n 'rota- wheel\\|rotos\\|reth-\\|ret- ' IEC.txt | head -10\necho \"=== SYN wheel ===\"; grep -n 'Lat. rota' SYN.txt | head -5",
 "description": "Klein, Walde-Pokorny, Mann, Buck on rota"
}
```


### [2026-09-14T01:31:35.670Z] TOOL RESULT

```
=== KLN rotate/roulette/control ===
26458:oracle,  n.  —  ME.,  fr.  OF.  (=  F.)  fr.  L.  draculum (for  *ora-tlom),  ‘divine  announcement,  oracle’, formed  with  instrumental  suff.  *-tlom  fr.  oro, ordre,  ‘to  speak,  pray,  beseech’.  See  oration, oracular,  adj.  —  L.  drdculdrius,  ‘dealing  in  ora¬ cles,  prophetic’,  fr.  oraculum.  See  oracle  and  -ar. Derivatives:  oracular-ly,  adv.,  oracular-ity,  n. oral,  adj.  —  Formed  with  adj.  suff.  -al  fr.  L.  os, gen.  oris,  ‘mouth,  face;  opening,  entrance,  ori¬ fice’,  fr.  *ous-,  whence  the  collective  noun  ora (for  *os-a),  ‘border,  coast’;  cogn.  with  OI.  ah, as-an,  ‘mouth’,  asyam,  ‘mouth;  opening’,  Aves¬ tic  ah-,  ‘mouth’,  Hitt,  aish  (gen.  ishash),  Mir.  a, ‘mouth’,  ON.  oss,  ‘mouth  of  a  river’,  OE.  dr, ‘beginning,  origin,  front’,  ora,  ‘bank,  shore’, Alb.  ant  (for  *ausnd),  ‘side,  border’.  Cp.  coram, orifice,  orle,  orotund,  oscitancy,  ostiary,  ostiole, usher,  Auriga,  vera.
26604:Orontium,  n.,  a  genus  of  plants,  the  golden  club (bot.)  —  ModL.,  prob.  fr.  Orontes,  a  river  of Syria.  For  the  ending  see  1st  suff.  -ium. orotund,  adj.,  1)  full,  resonant  (said  of  the  voice); 2)  pompous,  bombastic  (said  of  the  style  of utterance).  —  L.  (Horace,  Ars  Poetica,  323)  ore rotundo,  ‘with  a  round  mouth',  abl.  of  os  ro- tundum,  fr.  os,  gen.  oris,  ‘mouth’,  and  neut.  of rotundus,  ‘round’.  See  oral  and  rotund. Derivative:  orotund-ity,  n. orphan,  n.  —  Late  L.  orphanus,  fr.  Gk.  opqnxvoc, ‘without  father  or  mother,  orphaned’,  which  is cogn.  with  L.  orbus,  ‘bereft’,  OI.  arbhah,  ‘weak, child’.  Arm.  orb,  ‘orphan’,  arbaneak,  ‘servant, assistant',  OIr.  orbe,  orpe,  ‘heir’,  OSlav.  rabu, ‘slave’,  rabota,  ‘servitude,  slavery’,  Goth,  arbja, OHG.  arpeo,  erbo,  MHG.,  G.  erbe  (m.), OFris.  erva,  ON.  arfi,  OE.  ierfa,  ‘heir",  Goth. arbi,  OHG.  arbi,  erbi,  MHG.,  G.  erbe  (n.), OFris.  erve,  OS.  erbi,  OE.  ierfe,  ‘inheritance’, Goth,  arbaips,  ‘hardship,  toil,  work’,  OHG. arabeit,  MHG.  arebeit,  arbeit,  of  s.m.,  G.  Arbeit, ‘work’,  OFris.  arbed,  OS.  arabed(i),  ON.  erfidi, OE.  earfod,  ‘hardship,  suffering,  trouble’.  Cp. robot.
32035:Derivative:  redolent-ly,  adv. redondilla,  n,,  a  kind  of  rhymed  stanza.  —  Sp., dimin.  of  redondo,  ‘round’,  fr.  L.  rotundus.  See rotund.
33055:roll,  intr.  and  tr.  v.  —  ME.  rollen,  rolen,  fr.  OF. roller,  roler,  router  (F.  rouler),  fr.  VL.  *rotulare, fr.  L.  rotula,  ‘a  little  wheel’,  dimin.  of  rota, ‘wheel’.  See  rota  and  cp.  roll,  n.  Cp.  also  role, control,  enroll,  roulade,  rouleau,  roulette,  enroll, roly-poly.
33157:roth,  W.  rhod,  of  s.m.,  Gaul,  petorritum,  ‘four- wheeled  carriage'  (for  the  first  element  of  this compound  see  four),  OIr.  rethim,  ‘I  run’.  Cp. roll,  v.  and  n.  Cp.  also  redondilla,  rodeo,  rondeau, rondel,  rondo,  rondure,  Rotala,  rotate,  rotula, rotund,  roue,  rouelle,  roulette,  rounce,  round,  adj., rowel,  runlet,  ‘a  small  cask’,  rut,  ‘carriage’,  ar- rondissement,  tondo,  the  first  element  in  Ra- thayatra,  rodomontade  and  rut,  ‘carriage’,  and the  second  element  in  barouche  and  control.  Cp. also  rye  grass.
33178:rotula,  n.,  the  kneepan  (anat.  and  astron.). —  L. rotula,  ‘a  little  wheel’,  dimin.  of  rota\  see  rota and  -ule.  Cp.  Proven?.,  Catal.,  Port,  rodella, ‘kneepan’,  Sp.  rodilla,  ‘knee’,  which  derive  fr. VL.  rotella,  fr.  L.  rotula. rotund,  adj.,  round,  rounded.  —  L.  rotundus, ‘round’,  fr.  rota,  ‘wheel’.  See  round,  adj.,  and  cp. words  there  referred  to.  Cp.  also  next  word  and orotund.
33179:Derivatives:  rotund-ly,  adv.,  rotund-ness,  n. rotunda,  n.,  a  circular  building.  —  Refashioned after  the  Latin  form  from  earlier  rotonda,  fr.  It. rotonda,  prop.  fern,  of  the  adj.  rotondo  used  as  a noun,  fr.  L.  rotundus,  ‘round’.  See  prec.  word. F.  rotonde  is  a  loan  word  fr.  It.  rotonda.  See  prec. word.
33180:rotundate,  adj.,  rounded.  —  L.  rotundatus,  pp.  of rotundare,  ‘to  make  round’,  fr.  rotundus.  See  ro¬ tund  and  adj.  suff.  -ate.
33181:rotundi-,  combining  form  meaning  ‘round’.  —  Fr.
33182:L.  rotundus,  ‘round’.  See  rotund, rotundity,  n.,  roundness.  —  L.  rotunditas,  ‘round¬ ness’,  fr.  rotundus.  See  rotund  and  -ity. rotundo-,  combining  form  meaning  ‘roundly’.  — Fr.  L.  rotundus,  ‘round’.  See  rotund, roture,  n.,  the  state  of  being  a  roturier.  —  MF. (=  F.),  fr.  L.  ruptura,  ‘a  breaking’,  in  VL.  also ‘broken  land’,  formed  fr.  ruptus,  pp.  of  rumpere, ‘to  break’.  See  rupture  and  cp.  roto.
=== WLD Bd2 368 ret ===
24313:av.        „Wagen"’, raithya „Fahrstra6e“; lat, rota „Rad“, birotus „zwei-
24314:radrig“ (= lit. dvirdtis\ rotundus „scheibenrund“; ir. roth m. „Rad‘^; cymr.
38005: Hes., auch an rotundus erinnert man).
38522:jan^ ahd. krazzon „kratzen“, abl. anord. krota „eingraben“, Fick 111^51,
42083:Stroud-, sh'ud-mO^, Ygl. auch unten as, strota ,,guttur“, Persson Beiti*. 444,
42096:•werk“, nhd. (Blumefi-) Strang; hieher             auch as. strota ,,tuba, guttur“, mnd.
42353:       av. star- (Praes. staraHi, storonaoHi, stdVdnaHl) „sternere'', ptc. storota und
46494:  Buss, nereto, nerota „Art Fiscbreuse" (Miklosicb EW. 213, Persson Bei-
=== IEC ===
688:arotrom, see arátrom; arotos, see artos
737:artos (1) ‘ploughed; ploughed field’. WP I, 78. See aro (1) Arm. art, o-st. ‘field’; art-, arta-, px. "out: Gk. cf. (deverb.) arotós ‘arable’; árotos “field, crop’; Lat. cf. (deverb.) aratus; OE eard (fr. *artós); yrp (fr. *ártis); OFris. erd; MHG art; Li. ártas; Latv. arts, pp.
988:brotos ‘red liquid" (?) Gk. brótos ‘gore’; Cz. broť "red sap, woad’; Srb. broé "madder" cf. Cz. brotit, Pol. broczyc *bespatter w. blood'. (The Slav evidence is ambig., cf. bhrakt- in view of OCS brosti ‘purple dye’ & Ir. bracht 'sap")
1640:bhreth- (?) “blow? (expressive *-th-?) Gk. cf. prétho O OE brá&óan ‘breathe’; MHG cf. bradem “breath?
2644:in Arm. krkin ‘double’, cf. LG twit ‘narrow dividing lane’; E dial. twitton, twit, id.; *-&en-, *-Genes- in Skt. dvi-jánman; Gk. digenés and Lat. bigener, bigeneris; *-gueni- in Skt. dvi- jànih 'bigamous' and ON tví-kveni; *-iug- in Skt. (o-gde) dvyogah; Gk. dí-zux, -zugos & Lat. bi-jugis, -jugus; cf. Latv. div-jugs, s. 'two- in-hand'; *-plos, -plos in Av. bifro; Gk. diploüs, -plóos, -plós; Lat. duplus; Go. tweifls; OHG zwival; OFris. twifil and Du. twijfel; *-ped-, pod-, pd- in Skt. dvi- padah; Av. bib- dəm; Arm. cf. erkot-ani; Gk. di-podēs; Lat. bi-pēs, gs -pedis; cf. OE twi-fete; ON tví- foettr; *-poltos, -pltos in Gk. dí-paltos, di- plásios; Go. -falbs; MHG zwi-valt and ON tví-faldr; *-qusakos (or *-kakhos) in Skt. dvi- khakah, (-$akhah) ‘forked, two-pronged, bi- furcated'; Gk. dípsakos; Per. dū-šāxe and Li. dviSakas; *-rotos, (-rothos) in Lat. birotum, -rota and Li. dvirátis (fr. *rotios)
6222:cf. khés-imon “self-easement'; pés-imon “act of falling'; pega-imós 'act of departure'; Alb. het-im (inquiry): Li. skait-ymas reading); Ir. maoidh-eamh, gs -imh ‘telling’; áir-eamh, gs -imh ‘counting’; OCS pisimo “letter, writing; jarímü (fyoke', cf. Pol. ko-jarzyé "mont: Li. pie3-imas, ar-imas, grub-imas, &j-imas *design- ing, plowing, roughening, going’ beside grüd- ymas ‘hardening’; sür-ymas ‘saltwater’, etc. -inā, a generalizing extn. See next Gk. khoir-inë (‘musseľ: khoiros); dotiné (Hes: dos); (melíné ‘millet? in relation to *mel- ‘grind’, q. v. may belong here); Alb. lug- inë ((valley': lug 'trough); rreth-inë ('sur- roundings': rreth 'circle"); Lat. farina (:far); rüpina (:rüpes); haed-ina ('goatsflesh': hae- dus); OS cf. stulina ‘stealing’; lugina ‘lying’; OCS ozina ('anguish': ozükü, cf. Lat. angina); globina (‘depth’: globokü); dolina ('valley': dolü *ditch"). A variant occurs in Li. avíena “mutton”, cf. LLat. ovina, id. As an indicator of a female with a male counterpart, cf. Gk. héroiné (*heroine": héros); Lat. reg-ina (:rex); MHG cf. vühsinne (vixen': vuhs). A truncat- ed formula occurs in Go. managei, obl. -ein- ‘multitude’ and OHG hohi, obl. -1n-. See next -Inos, om (-Inios, om), an adjectival formant > a noun-derivative. Skt. a$v-in (:Lat. equinus); Av. peronin *wing- ed'; hámin- ‘summer’; Per. Sirin (sweet: Sir *milk); éübin (^wooden': éüb); pūstīn (‘fur coat: pūst "pelt: Oss. zàr-in ( golden": zàr); Arm. verf-in (final: verð); het-in, id. (fr. *en-pedinos, cf. Li. j-pedin “close behind”; Í-pédinis *successor"); Gk. pheg-inós (*oaken": phégós, cf. Lat. fàgínus of beech’); earinós (‘of spring": éar, cf. Lat. vernus); Lat. marinus, fibr-inus beside nüc-Ínus, màter-nus, ver-nus, etc.; W derw- in, lledr-in, hef-in ('oaken, leath- ern, summer: derw, lledr, haf); Go. fill-eins (‘of skin": fill, cf. Lat. pell-inus); fadr-ein (“pa- ternity, cf. Lat. paternus); OHG bibir-in, fuhs-in; MHG buech-in; ON gull-inn, OE medr-en, etc. “of beaver, fox, beech, gold, mother’; OCS materinü, materiní ‘maternal’; sestrinü, sestrini ‘sisterly’; krův-ínů (“of blood': krúvi, cf. Li. krùvinas ‘bloody’:kraŭjas “blood”). The variant -inios, where it occurs,
8004:krotos, us ‘rattling, shaking; rattle, shake’. WP I, 484. See kret-, krotolos Mir & Ir. crothaim, v. ‘tremble, shake’; Gk. krótos ‘rattle, clash’; krotéo, v. id.; ON hreójar ‘testicles’; Li. kratüs ‘shaking, trembling’; kra- týti, inf. ‘shake, tremble’; kratà, f. ‘rattle’; Latv. kratu, īt, v. id.
13451:prātos ‘wise; wisdom, intention, thought. Cf. protos. WP II, 86
13508:protos, is, form of prātos, is, q. v. WP II, 86. (Celtic forms ambig. Cf. rot-) Tokh. A pratim, B pratin ‘decision’; Ir. (am- big.) rath, m. (fortune, success, reward’. See rotos); OBr. rat, s. ‘grace, favour; W rhad, pl. au, m. id.; adj. “free, cheap’; Cor. ras, pl. -ow, m. “favour”; Go. frapi, n., MHG vrat, sn. *mind'; cf. also Go. ftapjan, sv. 6 'think; understand’; Li. cf. (w. nasal infix) prantùs, adj. ‘intelligent’; prasme, f. ‘meaning’; Latv. cf. pratigs, adj. ‘rational’; prat&js, m. ‘expert’; praša, f. ('understanding', fr. *protio)
14425:råtis ‘good, generous; generosity, good- ness”. Cf. reio (1) and rotos Skt. ratíh, adj. “generous, gracious, bountiful’; f. ‘favour’; Av. raitis, f. ‘generosity’; Latv. cf. ratns, adj. ‘good, well-behaved'"
=== SYN wheel ===
17351:It. sdrucciolare, fr. *dis-roteolare, de- tiv. of Lat. rota ‘wheel’. REW 2686.
17490:4. Ir. rethim, NIr. rithim, W. Br. redek :*Ir. roth, W. rhod, OHG rad Lat. rota ‘wheel’, Skt. ratha- ‘chariot’, Walde-P. 2.368, Pedersen 2.600 f. :
18313:Skt. ratha-, Av. ra8a- ‘chariot’ : Lat. rota, Lith. ratas ‘wheel’ (10.76).
18315:10.76 WHEEL Grk. —_zpoxés (xbxdos) Goth. .... Lith. ratas, tekinis ‘ NG —zpoxés, pda ON —hwel, hjal, hvel Lett. rats, ritenis, skritulis Lat. rota Dan. jul ChSl. kolo It. —ruota Sw.  hjul SCr. kolo, totak, kotat Fr. roue OE hwéol Boh. kolo Sp. rueda ME _hwele, whele Pol. kolo Rum.  roaté NE wheel Russ. koleso Ir. droch, roth Du. wiel Skt. cakra- NIr. roth OHG rad Av. éazra- W. olwyn, rhod MHG rat Br. rod NHG rad
23118:Lith. ratas ‘wheel’, also ‘circle’ : Lat. rota, OHG rad, ete. ‘wheel’ (10.76; cf. Lat. rotundus ‘round’, 12.81). Walde-P. 2.368.
```


## [2026-09-14T01:31:49.967Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('incoming/FFD/FFD_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nimport re\nfor i,p in enumerate(pages):\n    m=re.search(r'\\[pdf page (\\d+)\\]',p)\n    if m and m.group(1) in ('56','57','58'):\n        print('=== leaf',i,'tag',m.group(1)); print(p[:900])\nEOF",
 "description": "FFD page 56"
}
```


### [2026-09-14T01:31:51.064Z] TOOL RESULT

```
=== leaf 55 tag 56
[pdf page 56]
ماده‌های ماضی و مضارع فارسی دری --___شش ۵۱
صورت اصلی 3 است.» 0 پیش از ۲ به ۶ بدل شده است.
خواب < فارسی میانه 330: اسم است» در فارسی دری «خواب» به عنوان مادهٌ
مضارع «خفتن» به کار رفته است. ماده مضارع در فارسی میانه کته است.
بازماندهٌ ۹۷۵۵۵* ایرانی باستان. ۵۸:* ساخته شده است از ۸82 با بدل‌شدن 0 به ؟
پیش از 8 و 82 8 برای ساختن مادةٌ آغازی از ريشه به کار می‌رفته است. برای 2 آرای.
در فارسی دری از «خفس» که به صورتهای «خسپ» و «خسب» هم به کار رفته. مادهٌ
ماضی جعلی ساخته شده است: خفسید., خسپید, خسبید.
خندیدن
خندید < فارسی میانه ۰۵414 مادهٌ ماضی جعلی است. از ماده مضارع ساخته
شده است. َ
خند < فارسی میانه 75384 < ایرانی باستان ۰*۵4 380 در فارسی میانه و ایراتی
باستان» «خندیدن» معنی می‌دهد.
خواستن
خواست < فارسی میانه 7۳391« ایرانی باستان 9-1۵:*. برای اه آراست. 7۷36
صورت اصلی ۷38 است. 4 پیش از ۲ به 5 بدل شده است. ۷30 به معتی «خواستن»
است.
خواه + فارسی میانه ۳:5 < ایرانی باستان -۷۷24:*. بر
=== leaf 56 tag 57
[pdf page 57]
فعلهای فارسی دری
خوردن
خورد + فارسی میانه ۷۵7۵4 + ایرانی باستان ۷۷۵۲-1۵*. برای 2 آراست.
: خور + فارسی میانه 5۷۵7 < ایرانی باستان ۴*3۵۲-۵. برای 8 -> آرای.
و 3۷/8۲ به معنی (خوردن» و «نوشیدن» هر دو به کار رفته‌اند.
خوشیدن
«خوشید» مادةٌ ماضی جعلی است. از مادهٌ مضارع ساخته شده است.
خوش « فارسی میانه 355 < ایرانی باستان 8۸۵05-8*. برای ۵ -> آرای. ريشةٌ 1205 به
معنی «خشک شدن» است.
واژةٌ «خشک» از ريشهٌ ۳203 گرفته شده است. صورت فارسی ميانةٌ آن 1031 است. از
ایرانی باستان 8۵5-2*. 1805 صورت ضعیف ريشه و 1۵ پسوند است.
دادن
داد < فارسی میانه 434 < ایرانی باستان 43-12*. برای "18 > آراست. ريشهٌ 45
به‌معنی «دادن» است. در ایرانی باستان دو ريشةٌ 48 وجود داشته است: ۱-به معنی
«دادن»» ۲- به معنی «نهادن». «نهادن» از 13 به معنی «نهادن)» آمده است. >
نهادن.
ده < فارسی میانه 42 < ایرانی باستان ۵4۵۵5". 4202 ماد مضاعف است از 43.
داشتن
داشت + فارسی میانه 4381. به جای 4381 باید 417۵ می آمد از 4۲-12* ایرانی
=== leaf 57 tag 58
[pdf page 58]
ماده‌های ماضی و مضارع فارسی دری ۳ تا ۵۳
دانستن
دانست < فارسی میانه 420191. 432181 در فارسی میانه مادهٌ ماضی جعلی است.
دان + فارسی میانه 438 + فارسی باستان 4202* < ایرانی باستان 2288*: دانستن.
دراییدن
درایید ج فارسی میانه 473[14. در فارسی میانه 47316 مادءٌ ماضی جعلی است که از
7[ ماده مضارع و 14 ساخته شده است.
درای + فارسی میانه 473 « ایرانی باستان 472۳-۵7۵*. 278 برای ساختن مادهٌ
مضارع از ربشه به کار می‌رفته است. 41739 صورت بالاندهُ ريشهٌ 7۷ است و آن به معنی
«گفتن». ۳۷ وازژه‌ای اهریمنی بوده» یعنی برای اهریمن و دیو به کار می‌رفته است.
همین‌طور 4۲371120 واژه‌ای اهریمنی بوده است. در فارسی دری» که در آن واژه‌ها به
اهریمنی و اهورایی تقسیم نشده» «دراییدن» به معنی «یاوه گویی» به کار رفته است.
درودن
درود < فارسی میانه 4۳04 < ایرانی باستان 4۲8-۵*. برای 1۵ > آراست. 475
صورت ضعیف ريشةٌ 478۷ است. 4729 به معنی «درو کردن» است.
درو < فارسی میانه 47۵۷* < ایرانی باستان 45۵۳-۵* برای 2 > آرای.
```


## [2026-09-14T01:31:51.915Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('TAD_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 'تره' in p or 'ترة' in p or 'ترهة' in p:\n        print('leaf',i, [l for l in p.split('\\n') if 'تره' in l or 'ترة' in l][:4])\nEOF",
 "description": "TAD search turraha"
}
```


### [2026-09-14T01:31:52.972Z] TOOL RESULT

```
leaf 81 ['\u202bقال ابن الاثير \u202a :\u202cان لاخلرمخنار لامها مخمر العقل أي تستره \u202a .\u202cقلت الخر\u202c']
```


## [2026-09-14T01:32:03.830Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('incoming/FFD/FFD_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    m=re.search(r'\\[pdf page (\\d+)\\]',p)\n    if m and m.group(1) in ('61','62'):\n        print('=== leaf',i,'tag',m.group(1)); print(p[:1200])\nEOF",
 "description": "FFD printed page 56"
}
```


### [2026-09-14T01:32:04.931Z] TOOL RESULT

```
=== leaf 60 tag 61
[pdf page 61]
ان 111 0 اه ی ی ار ان نار اه
ره ج فارسی میانه ۲۵10 ج فارسی باستان ۹۳۵-۵ برای 2 -> آرای. اس <ایرانی
باستان 182: گریختن.
رُستن
رُست < فارسی میانه 7۵81 < ایرانی باستان ۳09-1۵*. برای 1۵ > آراست. ۲۳4
صورت اصلی 709 است. 4 پیش از ۲ به 8 بدل شده است. 104 صورت ضعیف 7800 است
و ريشةٌ 1304 به معنی «رشد کردن» است.
روی < فارسی میانه 70 < ایرانی باستان 7۵4-۵*. برای 2 > آرای.
رسیدن
رسید < فارسی میانه 72914. مادةٌ ماضی جعلی است. از ماده مضارع ساخته شده
است.
رس < فارسی میانه 7۵8 + ایرانی باستان ۲۵-۹-۵*. برای ۵ -> آرای. 8نشانه‌ای بوده که
برای ساختن‌مادء آغازی‌از ريشه‌به کار می‌رفته‌است.ريشةٌ ۲3به‌معنی «حرکت‌کردن» است.
«پذیره» بازماندةٌ 0207788 فارسی میانه است و ربطی به «پذیرفتن» ندارد. ۳02477۸8
بازماندةٌ 0211-78-6۵* ایرانی باستان است. 081 پیشوند و 1۵ پسوند و 73 ريشه است.
رشتن
«ریس) ماده مضارع «رشتن» است. ظاهراً «رشتن»» «ریس» از ربشةٌ 5۵12" به معنی
«بافتن» آمده است» به شرح زیر:
رشت < ایرانی باستان 718-1۵*. برای 1۸ -> آراست. ۲2 صورت اصلی قلة است» 7
پیش از 1 به 5 بدل شده است. 717 صورت ضعیف ريشه است.
ریس < ایرانی باستان 112-2*.برای 2 > آرای.در اینجا 2ب بدل شده است. > لشتن.
۱ رقتن
رقت < فارسی میانه 71 « ایرانی باستان ۴۲۵۳4۵. برای 12 -> آراست. 720 صورت

=== leaf 61 tag 62
[pdf page 62]
ماده‌های ماضی و مضارع فارسی دری سا ی ۵۷
اصلی 78۶ است» ۳ پیش از 1به ] بدل شده است.
رو < فارسی میانه 127۷ + ایرانی باستان ۲۵0-2*. برای 2 > آرای. ريشهٌ 780 به معنی
«حرکت کردن» است» چون 37 , 3820422 به معنی «حرکت کردن به سوی متکلم» است.
«رفتن» بط «دورشدن از متکلم» اختصاص پافته است.
روفتن
روب + فارسی میانه 30
ریختن
ریخت < فارسی میانه 7870 + ایرانی باستان 7۵۳1۵*. برای 1۵ > آراست. 7211
صورت اصلی 78 است» تا پیش از + به #بدل شده است. ريشةٌ 7 به معنی
«ترک‌کردن» است.
ریز + فارسی میانه 782 < ایرانی باستان 6-۵ز۲۵*. برای 2 > آرای. 5 به جای 3 آمده
است.
«گریختن» هم از ريشةٌ له آمده است > گریختن.
ریدن
رید + فارسی میانه 710.
ری < فارسی میانه 717
زادن
زاد < فارسی میانه 734 < ایرانی باستان 22-18*. برای 1۵ > آراست. 23 صورت
ضعیف ريشةٌ 227 است به معنی «زادن».
زای < فارسی میانه 237 < ایرانی باستان 22-72*. 8 نشانه‌ای بوده که برای ساختن
مادهٌ مجهول از ريشه به کار می‌رفته است.
```


## [2026-09-14T01:32:24.816Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('incoming/FFD/FFD_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    m=re.search(r'\\[pdf page (\\d+)\\]',p)\n    if m and m.group(1)=='60':\n        print(p[-1200:])\nEOF",
 "description": "FFD pdf page 60 tail"
}
```


### [2026-09-14T01:32:25.732Z] TOOL RESULT

```
[pdf page 60]
ماده‌های ماضی و مضارع فارسی دری نا ۵۵
بین < فارسی میانه ۷۷68 + ایرانی باستان ۹/۵۱-3* 23 نشانه‌ای بوده که برای ساختن
مادهٌ مضارع از ريشه به کار می‌رفته است. ريشةٌ ۷۵ به معنی «دیدن» است.
«دیدن» و «بین» چون «آمدن) و «آی» دو ریشه‌ای است.
رامیدن
۰ آرامیدن
راندن
راندن مخفف «روانیدن» است و آن فعل واداری از «رفتن» است. در فارسی دری
فعل واداری از مادةٌ مضارع + «ان» و «(عن» ساخته می‌شود. «۵۶) در متون کهن آمده
مادهٌ ماضی فعل واداری هميشه جعلی است و به جای «انید» ممکن است («اند» به
کار رود.
ربودن
ربود + فارسی میانه 1010.
ربای + فارسی میانه 1003 +« ایرانی باستان ۵رقم۳*, 2رقم" از ۳803: اسم
به‌معنی «ربودن» و 8نشانه‌ای که برای ساختن مادةٌ جعلی از اسم به کار می‌رفته» ساخته
شده است.
مادهٌ ماضی باید «رّفت» < فارسی میانه ۳۵۶۲ < آیرانی باستان ۵۵ می آمد. به قیاس
با 573 و 5736 «ربود» آمده است.
3 از ریشةٌ 780 به معنی «ربودن» و پسوند 3 ساخته شده است.
رّستن
رّست + فارسی میانه 7291 < فارسی باستان ۴۶۵۶-1۵ برای 1۵ -> آراست. 724
صورت اصلی 78 است» ‎٩‏ پیش از 1به 9بدل شده است.
```


## [2026-09-14T01:32:38.978Z] TOOL CALL #70: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/control",
 "prompt": "Give the etymology of 'control': Old French contreroller / contre-rolle, Medieval Latin contrarotulus, from Latin rotulus/rota. Also say what etymonline gives for 'roulette' and 'round' if visible."
}
```


## [2026-09-14T01:32:41.056Z] TOOL CALL #71: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AA%D8%B1%D9%87%D8%A7%D8%AA",
 "prompt": "Is there an entry for Arabic/Persian ترهات (turrahāt)? Give meaning and etymology; also check تُرَّهة (turraha) — is it said to be from Persian?"
}
```


### [2026-09-14T01:32:42.673Z] TOOL RESULT

```
# Etymology of "Control"

According to the Online Etymology Dictionary, **control** originates from early 15c. Anglo-French *contreroller*, meaning "to check the accuracy of, verify; regulate." This derives from Medieval Latin *contrarotulus* ("a counter, register"), combining Latin *contra* ("against") with *rotulus*, a diminutive of *rota* ("wheel").

The word likely emerged from "a medieval method of checking accounts by a duplicate register."

## Note on "Roulette" and "Round"

The provided content does not include etymological information for either "roulette" or "round," though "roll" is mentioned as a related entry that shares the Latin *rotulus* root.
```


### [2026-09-14T01:32:45.548Z] TOOL RESULT

```
# Response

Based on the Wiktionary page provided:

**Entry exists:** Yes, there is an entry for **ترهات** (turrahāt).

**Meaning:** The page identifies it as "plural of تُرَّهَة (turraha)" but does not provide a definition of what the singular noun means.

**Etymology:** The page contains no etymology information for either ترهات or تُرَّهة.

**Persian origin claim:** The Wiktionary entry does not indicate whether تُرَّهة is said to derive from Persian. While the page notes the word appears in both Persian and Russian Wiktionaries, it provides no etymological discussion or source attribution.

To learn the actual meaning and potential Persian origins, you would need to consult the singular form's entry (تُرَّهة) or other etymological resources.
```


## [2026-09-14T01:32:49.674Z] TOOL CALL #72: WebSearch

```json
{
 "query": "\"الترهات\" \"الطرق الصغار\" فارسية معربة لسان العرب ترهة"
}
```


### [2026-09-14T01:32:55.570Z] TOOL RESULT

```
Web search results for query: ""الترهات" "الطرق الصغار" فارسية معربة لسان العرب ترهة"

Links: [{"title":"arabicwords_0 on X: \"الترَّهات لفظ فارسي معرّب معناه الطرق غير الممهدة التي تتفرع من الطريق الأعظم، واستعير اللفظ ليشير إلى الباطل (لأن من يسلك الترهات لا يسير على الجادة الواضحة) والبسابس معناها الأكاذيب أو الفضاء القفر، وعندما يُقال ترهات البسابس فذلك مبالغة في المعنى أي الأباطيل البين ب","url":"https://x.com/arabicwords_0/status/1763669855696240709"},{"title":"أسماء الطرق عند العرب (عن لسان العرب لابن منظور) الجادَّةِ ...","url":"https://www.facebook.com/associationdesamisdelalanguearabeadala/posts/%D8%A3%D8%B3%D9%85%D8%A7%D8%A1-%D8%A7%D9%84%D8%B7%D8%B1%D9%82-%D8%B9%D9%86%D8%AF-%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D8%B9%D9%86-%D9%84%D8%B3%D8%A7%D9%86-%D8%A7%D9%84%D8%B9%D8%B1%D8%A8-%D9%84%D8%A7%D8%A8%D9%86-%D9%85%D9%86%D8%B8%D9%88%D8%B1%D8%A7%D9%84%D8%AC%D8%A7%D8%AF%D9%91%D9%8E%D8%A9%D9%90-%D8%A7%D9%84%D8%AC%D8%A7%D8%AF%D9%91%D9%8E%D8%A9-%D9%85%D8%B9%D8%B8%D9%85-%D8%A7%D9%84%D8%B7%D8%B1%D9%8A%D9%82-%D9%88%D8%A7%D9%84%D8%AC/775626225796239/"},{"title":"معربات فارسية - ويكيبيديا","url":"https://ar.wikipedia.org/wiki/%D9%85%D8%B9%D8%B1%D8%A8%D8%A7%D8%AA_%D9%81%D8%A7%D8%B1%D8%B3%D9%8A%D8%A9"},{"title":"تره – معجم لسان العرب لابن منظور","url":"https://wiki.dorar-aliraq.net/lisan-alarab/%D8%AA%D8%B1%D9%87"},{"title":"إسلام ويب - لسان العرب - حرف الطاء - طرق- الجزء رقم9","url":"https://www.islamweb.net/ar/library/content/122/5051/%D8%B7%D8%B1%D9%82"},{"title":"معنى ترة بالعربي — التعريف والشرح والمرادفات في معاجم ...","url":"https://www.arabdict.com/en/%D8%B9%D8%B1%D8%A8%D9%8A-%D8%B9%D8%B1%D8%A8%D9%8A/%D8%AA%D8%B1%D8%A9"},{"title":"إسلام ويب - لسان العرب - حرف التاء - تره- الجزء رقم2","url":"https://www.islamweb.net/ar/library/content/122/833/%D8%AA%D8%B1%D9%87"},{"title":"مقالات سياسية وأفكار","url":"http://laithaliraqi.blogspot.com/"}]

بناءً على نتائج البحث، إليك المعلومات عن كلمة "الترهات":

الترهات هي الطرق الصغار غير الجادة التي تتشعب عنها، والواحدة ترّهة، وهي كلمة فارسية معربة. 

استُعيرت هذه الكلمة لاحقاً في معنى الباطل، حيث يُقال: "الترهات البسابس" و"الترهات الصحاصح"، وهي من أسماء الباطل. 

وقد جاء ذلك في معجم لسان العرب لابن منظور، حيث أورد الجوهري هذا التعريف المفصل للكلمة.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-14T01:33:04.669Z] TOOL CALL #73: WebFetch

```json
{
 "url": "https://www.islamweb.net/ar/library/content/122/833/%D8%AA%D8%B1%D9%87",
 "prompt": "Quote the Lisan al-Arab entry for تره / الترهات: give the exact Arabic sentence defining الترهات as الطرق الصغار and whether it says فارسية معربة."
}
```


## [2026-09-14T01:33:06.729Z] TOOL CALL #74: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%DA%A9%D9%86%D8%AA%D8%B1%D9%84/",
 "prompt": "Does Farhang-e Mo'in (فرهنگ معین) mark کنترل as French ([فر.])? Quote the entry. Also any entry for رولت (roulette) with a French tag."
}
```


### [2026-09-14T01:33:09.526Z] TOOL RESULT

```
# Lisan al-Arab Entry for تره

Based on the provided text, here is the exact Arabic definition:

**Definition of الترهات:**
"التُّرَّهَاتُ الطُّرُقُ الصِّغَارُ غَيْرُ الْجَادَّةِ تَتَشَعَّبُ عَنْهَا"

**Origin note:**
The text explicitly states: "فَارِسِيٌّ مُعَرَّبٌ" (Persian word that has been Arabicized)

The entry clarifies that الترهات originally referred to small branching paths diverging from the main road, and this meaning was later metaphorically extended to denote falsehoods or absurdities (الأباطيل).
```


### [2026-09-14T01:33:10.556Z] TOOL RESULT

```
# Response

Yes, Farhang-e Mo'in marks کنترل as French. The entry states:

"(کُ تُ رُ ) [ فر. ] (اِ. ) جستجو، تفتیش"

This notation "[فر.]" indicates the French origin of the word.

However, the document provided contains no entry for رولت (roulette), so I cannot confirm whether that term receives a French tag in this dictionary.
```


## [2026-09-14T01:33:20.348Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n 'https://en.wiktionary.org/wiki/%D8%B1%D8%A7%D9%87' \\\n 'https://en.wiktionary.org/wiki/%D9%84%D8%B4%DA%A9%D8%B1' \\\n 'https://en.wiktionary.org/wiki/%D8%B1%D8%A7%D9%87%D8%A8' \\\n 'https://en.wiktionary.org/wiki/%D8%B1%D8%A7%DB%8C%DA%AF%D8%A7%D9%86' \\\n 'https://en.wiktionary.org/wiki/%D8%B9%D8%B3%D9%83%D8%B1' \\\n 'https://en.wiktionary.org/wiki/%D8%A7%D8%B1%D8%A7%D8%A8%D9%87' \\\n 'https://www.etymonline.com/word/control' \\\n 'https://abadis.ir/fatofa/%D8%B9%D8%B1%D8%A7%D8%AF%D9%87/' \\\n 'https://abadis.ir/fatofa/%D8%A7%D8%B1%D8%A7%D8%AF%D9%87/' \\\n 'https://abadis.ir/fatofa/%DA%A9%D9%86%D8%AA%D8%B1%D9%84/' \\\n 'https://www.islamweb.net/ar/library/content/122/833/%D8%AA%D8%B1%D9%87' ; do\n python3 tools/fetch_source.py \"$u\" --note 'pdf page 422, root Ret: verification of rah/laskar/rahib/turrahat/arrada/control chain' 2>&1 | tail -1\ndone",
 "description": "Archive web sources"
}
```


### [2026-09-14T01:33:29.367Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/8f4d082c8868532c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/cb5d281da757664f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/482aa63efcf42212.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/91f940f97da485e1.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4d1bbea360fb1f70.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d9f99415246a8d20.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f498383543d28a78.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8e1553a71e7bc7b3.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a931fc14f723fcc6.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5ff66c01506d3273.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b137584168c183f7.txt
```


## [2026-09-14T01:33:33.219Z] TOOL CALL #76: Bash

```json
{
 "command": "mkdir -p data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg422.png data/verification/sources/refs/ocr/BOOK/422.png && ls -la data/verification/sources/refs/ocr/BOOK/422.png\nsed -n '1,60p' tools/verify_check.py",
 "description": "Copy page image, inspect verify_check"
}
```


### [2026-09-14T01:33:33.316Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 66285 Sep 13 21:33 data/verification/sources/refs/ocr/BOOK/422.png
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
```


## [2026-09-14T01:34:46.612Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (389,390):\n    print('==== leaf',i)\n    print(pages[i][:2500])\nEOF",
 "description": "BQT v2 leaves 389-390 for rās"
}
```


### [2026-09-14T01:34:47.716Z] TOOL RESULT

```
==== leaf 389
                                                                                        ‫‪۲4‬‬
‫خوانند ‪ ۰‬اکر درون وبرا پراز گشنیز کنند‬                 ‫استیثه ‪ = ۲‬بروزن ماستینه ‪ .‬بمعنی‬
 ‫و خشك سازند خوردن قدری از آن کزندکی‬                                     ‫راسترن باشد که حقیقی ‪۳‬‬

‫جالوران زهردار را نافع باشد ‪ .‬کوبند اک رکب‬            ‫اسحت ؟ ب=ضم ثالث و سکون خای‬
                                                                                ‫ر‬
‫باشد بیرون آورند و بریای‬     ‫دهه‬
                               ‫نک‬‫زقتی‬
                                    ‫آنرا بو‬           ‫قطه دار (‪ )۱‬و تای قرشت ‪ .‬سمسوخته باشد‬
‫راست زن بندلد وباو جماع کنند آستن گردد ‪.‬‬
                                                       ‫و آلراروی‌سوخته‌یز کویندومعر آن‌روسختج(‪)۲‬‬
‫و گویندطمامی که زهرداشته باشد همین که‌ببیند‬
‫موهای‌خود راست(‪ )۵‬کند وبفرمادآ بد‪ .‬اگرخون‬
                                                      ‫|‬
                                                                                 ‫است درسم (‪. )۳‬‬
‫او را مبفراصل وخنازیر طلاکنند نافع باشد ‪.‬‬
                                                      ‫= بروزن دامن‪ .‬نام درخت پیل‬    ‫راس"‬
‫راش ه بورزن ماش » نوده والبار غلة‬                      ‫کوش است و آن داروبی (‪ )4‬باشد نافع جمیع‬
          ‫باك شذه و ازکاه برآورده راکویند ‪.‬‬
                                                       ‫آبلہا ودرد ها خصوصاً درد هابی که از رطوبت‬
 ‫راطینی ‪ - ۴‬بکرلطای‌حطی(‪ )+‬ونون‬                       ‫و سردی بود و گزندگی چالوران را سود دارد‬
 ‫وسکون هردوتحتانی» بلفت بونانی مطلق صمغ‌را‬                ‫زمینجویل شامی لگزویند‬
                                                                              ‫آولرا قط شا‬
‫کویند خواه مصطکی وخواه کندر و خواه کتیرا‬              ‫وغرساهمان‌است ‪ .‬بیخ نرا اصل‌الراسن وتخمآ ترا‬
                                  ‫وماشدآن ‪۲‬‬            ‫حب‌الراسن خوانند؛ وبعضی کویند لبانی است که‬
 ‫نعقینط‌هبی(‪)۷‬بروزن‌قابیل‪.‬‬
                         ‫راعیل = با‬                   ‫بویآن ببوی سیر می‌ماند ؛ وبعضی دیگر گونند‬
                    ‫بام زلیخای مشهور است ‪.‬‬            ‫علفی است که آارا ترکان قجی گویند وبا ماست‬
                                                                                           ‫خور ند‪.‬‬
 ‫راع " ‪ -‬بروزن باغ ‪ .‬مرغزار وسحرا‬
 ‫باشد ‪٩‬‏ ‪ -‬و دامن کوهی را نگیوزبند که بجالب‬               ‫راسو = بورزن مازو ‪ ۰‬جالوری است‬
                                 ‫صحرا باشف ‪.‬‬              ‫که آنرا موش خرما گویند و بعربی ابن عرس‬

==== leaf 390
  ‫س‪۳‬‬
   ‫ه‪۳‬‬‫باه‬                                                                                             ‫ران‬
‫راك ‪ -‬بر وزن خاك * فوج گووسفند‬                          ‫راف د بر وزن کاف» بزبازست جربی‬
‫جکنگویبرناد ‪ - ۱‬و بمعنیکاسة آبخوری حم‬                          ‫سیاسه خوالند ‪ .‬گوشد يوست جوزاست ‪.‬‬
‫آمده است‪ -‬ورشتةٌ سوزن رانیز گفته‌اند‪ -‬وبلفت‬            ‫راقو نه= بر وزن بابونه ‪ ۰‬پودله را‬
‫زند ویازند(‪ )۱‬راه باشد که بعربی صراط وطریق‬              ‫گونند ؛ وباین معنی بجای فا قاف وبجای نون‬
                                          ‫خواند ‪. ۴‬‬     ‫تای قرشت هم منظر آمده امت که راقونه‬
‫دگااده » با کاف بر وزن آوار» ‪ ۰‬زن‬                                                                    ‫باشد ‪.‬‬
                        ‫فاحشه ویدکاره را گوند ‪۰‬‬         ‫‪ 94۰‬بروزن دافه‪ .‬کیاهیاست مانشدسیر‬
                                                                                        ‫ر‬
‫وبزرن کام‪ ۰‬شض وحش امت‬      ‫رام =‬                        ‫برادرپیاز‪ ,‬وآنرابربان کرده بخورند بفایت لذین‬
‫که الفت گرفته وآموخته وفرمان بردارباشد؟ ‪-‬‬               ‫باشد؛ وباین معنی با زای نقطه دار آهممده‌است؛‬
‫وهام روزییست وبکم است ازماه های شمسی؟ ‪-‬‬                 ‫آن حلتت‬        ‫مهغ‬
                                                                         ‫صت ک‬
                                                                            ‫وبسی کوبند انجدان اس‬
‫وهام فرشته ابت که موکل روزرام ومصالح‌امور‬               ‫باشد ؛ و بضی دیگرکوبند بیخ درخت انجدان‬
 ‫وافت‬
    ‫مردم است در آن روز ‪ - ۴‬وآرام ط‬                                                                   ‫ات ‪:‬‬

                                                                      ‫جك ‪ :‬رند و یارند‪.‬‬   ‫(‪)۱‬‬



                        ‫‪ - ۱‬پهلوی ‪( 62۲‬دژکوب قوج قلمه خرا بکن) «اونوالا ‪٩۳4۰‬‏ ‪.‬‬
  ‫‪ ۳‬هس راکه قرائتی امت از «راس» پپلوی (ب‌عنی راه) وصحیح رای است‪ .‬رك ‪:‬رای۔‬
   ‫‪ ۴‬فس ‪ :‬پارسی باستان ‪ .۷۳۸[ 800۳2۲‬اوستا ‪ ( 0۳22۲-‬سکون‪ .‬آراش‪.‬‬
  ‫استراحت)» پپلوی ‪[ ۲5۵۲‬لاط‪ ۰ ۲015(1/۵۳2۴ .‬هندی باستان ‪( 20۳۵۲ -‬میل » تمایل)‪ .‬استی‬
  ‫‪ - ۴‬باین معتی لیز‬                 ‫( بازداشتن » مادم‪.‬شدن » ساکت کردن) «اسشق ‪4۰٩‬‏ ‪.‬‬                  ‫‪0‬‬

  ‫و بدین ممانی در اوستا بارها آمده (بتا ‪۲٩‬بند‏ *‪ » ۱‬بتا ‪ ۵۳‬بند ‪٤‬‏ وجزآن) ویز با دراوستا‬
  ‫بایزد رام اطلاق کردیده (بنا ‪۱‬بند ‪» ۳‬نا ‪٤‬‏ بند ‪ ۳‬وجزآن) ‪ ۰‬درغالب مواضم اوستا اورایس‬
  ‫ازبزد مهر نام برده‌اند ‪ .‬بانزده‌ی بشت اوستا بنام « رام بشت > امیده میشود ‪ .‬نگهبانی روز‬
       ‫>
```


## [2026-09-14T01:35:01.052Z] AGENT

Now I'll write the verification file.


## [2026-09-14T01:41:51.057Z] TOOL CALL #78: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-422.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\n\nentry = {\n  \"entry\": 0,\n  \"root\": \"Ret\",\n  \"verdict\": \"confirmed\",\n  \"modern_form\": \"PIE *Hret- (older notation *ret(h)-) 'to run, to roll'\",\n  \"note\": \"Pokorny IEW 866 prints exactly 'ret(h)- : to run, to roll' and lists Old Indic ratha- 'cart', Avestan raθa- 'cart', raiθya- 'carriage road', Latin rota 'wheel', rotundus, Old Irish rethim 'I run', Lithuanian ratas 'wheel'. Watkins/AHD has the same headword 'ret-. To run, roll. [Pok. ret(h)- 866.]', which is where Nourai's English gloss comes from verbatim. The only update modern scholarship makes is the initial laryngeal: because PIE roots cannot begin with plain *r-, the root is now written *Hret- (LIV 507; Cheung's Iranian entries are all cited as *Hr-), and the aspirate of Indic ratha- is secondary rather than a root variant *reth-. Language label ('Indo-European'), form and gloss are all right. Nourai's page-422 chart hangs four branches on it: Avestan, Old Persian, Latin, and (through Pahlavi) the Persian rāh family.\",\n  \"note_fa\": \"ریشهٔ هندواروپایی آغازین *Hret- (در نگارش کهن‌تر *ret(h)-) به معنی «دویدن، غلتیدن» است؛ پوکورنی در فرهنگ ریشه‌شناسی هندواروپایی (ص ۸۶۶) همین سرواژه را با همین معنا آورده و بازتاب‌های آن را برشمرده است: ratha- در سنسکریت «گردونه»، raθa- اوستایی «گردونه»، raiθya- «راهِ گردونه‌رو»، rota لاتینی «چرخ»، rotundus «گِرد» و ratas لیتوانیایی. معنایی که نورایی آورده («to roll, run») واژه‌به‌واژه از پیوست ریشه‌های هندواروپایی واتکینز (AHD) گرفته شده است. تنها اصلاح پژوهش امروزی افزودن حنجره‌ای آغازین است — چون ریشهٔ هندواروپایی با *r- ساده آغاز نمی‌شود — و نیز اینکه «ه» در ratha- سنسکریت پسین و درون‌هندوآریایی است نه بازماندهٔ *th هندواروپایی. در مجموع ادعای نورایی دربارهٔ خودِ ریشه درست است.\",\n  \"sources\": [W + \"Reconstruction:Proto-Indo-European/H%E2%82%81ret-\"],\n  \"ref_check\": [\n    {\"ref\": \"POK:866\", \"status\": \"supports\",\n     \"note\": \"Pokorny IEW p.866 (local POK_full.txt, line 70379): 'Root / lemma: ret(h)- ; Meaning: to run, to roll ; Material: Old Indic ratha- m. \\\"cart\\\", rathī- \\\"charioteer\\\", rathya- \\\"zum cart belonging\\\" ... rathēṣṭhā- \\\"warrior\\\" = Avestan raθaēštā; Avestan raθa- \\\"cart\\\", raiθya- \\\"Fahrstraße\\\"; Latin rota \\\"wheel\\\", birotus, rotundus \\\"scheibenrund\\\" ... References: WP. II 368, WH. II 443 f. Page(s): 866.' The page number is exact and the gloss is verbatim Nourai's.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. ret- (AHD_watkins1985.txt line 895)\", \"stance\": \"supports\",\n     \"note\": \"'ret-. To run, roll. 1. Prefixed form *to-wo-ret-, \\\"a running up to\\\" ... in Old Irish toir, pursuit: TORY. 2. Suffixed o-grade form *rot-a- in Latin rota, wheel: RODEO, ROLL, ROTA, ROTARY, ROTATE, ROTUND, (ROTUNDA), ROULETTE, ROUND, ROWEL; BAROUCHE, CONTROL, PRUNE, ROTIFORM, ROTOGRAVURE. [Pok. ret(h)- 866.]' — this single entry is the source of Nourai's whole Latin/French/English half of the chart.\"},\n    {\"src\": \"WLD\", \"where\": \"Walde-Pokorny II 368 (WLD_Bd2_pages.txt line 24313)\", \"stance\": \"supports\",\n     \"note\": \"'av. raθa- \\\"Wagen\\\", raiθya \\\"Fahrstraße\\\"; lat. rota \\\"Rad\\\", birotus \\\"zweirädrig\\\" (= lit. dviratis), rotundus \\\"scheibenrund\\\"; ir. roth m. \\\"Rad\\\"; cymr. ...' — the older (1927) statement of the same root that Pokorny 866 reprints.\"},\n    {\"src\": \"SYN\", \"where\": \"Buck 10.76 'wheel' and 10.46 (SYN.txt lines 18313, 17490, 23118)\", \"stance\": \"supports\",\n     \"note\": \"'Skt. ratha-, Av. raθa- \\\"chariot\\\" : Lat. rota, Lith. ratas \\\"wheel\\\" (10.76)'; and under 'run': 'Ir. rethim, NIr. rithim, W. redek : Ir. roth, W. rhod, OHG rad, Lat. rota \\\"wheel\\\", Skt. ratha- \\\"chariot\\\", Walde-P. 2.368' — Buck confirms both halves of the gloss ('run' and 'wheel/roll').\"},\n    {\"src\": \"IEC\", \"where\": \"Mann, alphabetical (grep 'rotos', 'reth-', 'ret-')\", \"stance\": \"partial\",\n     \"note\": \"Mann has no separate headword *ret-; the family surfaces only inside compounds, e.g. s.v. dwi- '*-rotos, (-rothos) in Lat. birotum, -rota and Li. dviratis (fr. *rotios)'.\"}\n  ],\n  \"nodes\": []\n}\n\nN = entry[\"nodes\"]\n\nN.append({\n  \"id\": 1, \"lang\": \"Avestan\",\n  \"words\": \"rad 2; ratha; ratha-eštra\",\n  \"verdict\": \"disputed\",\n  \"derivation\": \"Two of the three words are solid. (a) Av. raθa- m. 'chariot, chariot-box' is real and well attested (Yt 10.68, Yt 17.17, Yt 19.43f); it continues PIE *Hrot-o- with the regular Indo-Iranian aspiration of the dental (Skt. rátha-), Bartholomae AiW col. 1505f. glosses it 'Wagen' and gives the Pahlavi rendering 'ras'. (b) raθaēštar- / raθaēštā- 'warrior, chariot-fighter' (AiW col. 1506) is a compound of the locative raθaē 'on the chariot' + the root noun -štā- 'standing' (root stā-, so Nourai's cross-reference to Sta is right); it is the Avestan name of the warrior estate beside āθravan- 'priest' and vāstryō.fšuyant- 'herdsman', and its Pahlavi gloss in AiW is literally 'artēštār' — the direct ancestor of node 2. (c) 'rad 2 : to run' is not an Avestan verb: Bartholomae's only rad- entry (AiW col. 1505, immediately before raθa-) is marked 'p.' = Old Persian, occurs only with ava- 'to leave, to deviate from (the path)', and is compared with Skt. rahati, NP rahad; Cheung 2007 lists an Avestan raδ- but glosses it 'to dig, pave (a way)' (raδaiti Yt 10.68) from PIE *HreHsd-, a different root. The PIE root *Hret- has no verbal continuant in Iranian at all, so the verbal 'rad 2 to run' in this box is a conflation and cannot be supported by POK:866, which lists no Avestan verb.\",\n  \"derivation_fa\": \"از سه واژهٔ این خانه دو تا درست است. raθa- اوستایی «گردونه» (بارتولومه، فرهنگ ایرانی باستان، ستون ۱۵۰۵) بازماندهٔ *Hrot-o- هندواروپایی است و هم‌ریشهٔ rátha- سنسکریت؛ raθaēštar-/raθaēštā- «جنگاور، ارابه‌سوار» نیز ترکیبی است از raθaē (حالت دری/مکانی: «بر گردونه») و ستاک -štā- از ریشهٔ stā- «ایستادن»، و نام طبقهٔ جنگاوران در اوستاست که بارتولومه برابر پهلوی آن را «artēštār» آورده است — یعنی همان که در خانهٔ بعدی به «ارتشتار» رسیده است. اما «rad 2: دویدن» در اوستا فعل شناخته‌شده‌ای نیست: تنها مدخل rad- در بارتولومه پارسی باستان است و فقط با پیشوند ava- به معنی «رها کردن، از راه به در شدن» (هم‌ریشه با rahati سنسکریت)، و چونگ فعل اوستایی raδ- را «راه ساختن، کندن» و از ریشهٔ دیگری (*HreHsd-) می‌داند. ریشهٔ *Hret- در ایرانی هیچ بازماندهٔ فعلی ندارد؛ پس این بخش ادعای نورایی پذیرفتنی نیست.\",\n  \"sources\": [W + \"%D8%B1%D8%A7%D9%87\"],\n  \"ref_check\": [\n    {\"ref\": \"POK:866\", \"status\": \"partial\",\n     \"note\": \"IEW 866 supports raθa- and raθaēštā ('Avestan raθa- \\\"cart\\\", raiθya- \\\"Fahrstraße\\\" ... Old Indic rathēṣṭhā- \\\"warrior\\\" = Avestan raθaēštā') but lists no Avestan (or any Iranian) verb of this root, so it cannot support 'rad 2 : to run'.\"},\n    {\"ref\": \"LEW:904\", \"status\": \"not_checked\",\n     \"note\": \"Nourai cites Walde-Hofmann's Lateinisches etym. Wb. 3rd ed. p.904; only the 2nd ed. (1910) is on disk (LEW_1910.txt), whose pagination differs — its rota material is at WH/LEW I 294 per its own index line 520 ('rota I 294'). Not checkable at the cited page; in any case a Latin dictionary is an odd support for an Avestan box.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"BRT\", \"where\": \"AiW cols. 1505-1506 (BRT.txt lines 25074-25101)\", \"stance\": \"partial\",\n     \"note\": \"'j. raθa- m. \\\"Wagen\\\" ... ai. ratha- m.; mp. ras.' and 'j. raθaē-star-, raθaē-štā-, raθō.štā- m. \\\"Krieger, Kriegsheld\\\" ... Komp. mit LS. im I. Glied, *štar- ... zum V. stā-. — ai. rathēṣṭhā- m. \\\"Wagenkämpfer\\\" ... Pü.: arteštār (gelw.)'. But the preceding entry reads '• p. rad- V., nur mit ava \\\"verlassen\\\". Praes. 2 rada- ... ai. rahati \\\"er verlässt\\\", np. rahad' — Old Persian, not Avestan, and not 'to run'.\"},\n    {\"src\": \"CHEUNG\", \"where\": \"Etym. Dict. of the Iranian Verb, s.v. *Hrad (~p.186) (CHEUNG.txt line 12687)\", \"stance\": \"contradicts\",\n     \"note\": \"'*Hrad \\\"to dig, pave\\\": Y Av. raδ- \\\"to pave (a way)\\\", ? YAv. paθīm raδ- \\\"road-paver\\\" (Yt 9.23) ... PIE *HreHsd- \\\"to gnaw, furrow\\\" (LIV 497, Pok. 854)'. The only Avestan rad/raδ verb belongs to Pokorny 854, not 866, and does not mean 'to run'.\"},\n    {\"src\": \"PHD\", \"where\": \"MacKenzie 1971 s.vv. artēštār, rah (PHD.txt lines 214, 555)\", \"stance\": \"supports\",\n     \"note\": \"'artēštār [ʾrtštʾl | N artēšdār] warrior. -īh: warriorhood' and 'rah [lhy | M rh(y)] chariot, wagon' — both Middle Persian continuations of this Avestan box.\"}\n  ]\n})\n\nN.append({\n  \"id\": 2, \"lang\": \"Persian\",\n  \"words\": \"arrâdeh; arteštâr; laškar\",\n  \"verdict\": \"disputed\",\n  \"derivation\": \"arteštâr is exactly right: Av. raθaēštar- gave Middle Persian artēštār 'warrior' (MacKenzie p.12; Bartholomae himself glosses the Avestan word with Pahlavi artēštār), the name of the second (warrior) estate of Sasanian society; the Iranian initial cluster raθ- was resolved by the well-known Middle Persian metathesis/prothesis r-t- > art- (as in Av. arəta-/aša- > MP ard-), and -št- was kept. Mo'in's footnote in Borhan-e Qate' p.97 s.v. ارتشدار states the same (Avestan raθaēštār, Pahlavi gloss 'ready for battle'). The modern ارتش 'army' in Nourai's parenthesis is a 1314/1935 Farhangestan coinage back-formed from artēštār, so it belongs here legitimately. arrâdeh «ارّاده» 'cart, gun-carriage' is real Persian (Mo'in: «ارّاده: گردونه، ارابه») and Asbaghi 1988 p.8 (s.v. ʾarāba) reports the Bahār-e ʿAjam view that arāba is really ʿarrāda 'gun-carriage, wheel of a projectile-thrower' and compares 'ap. raθa, aw. raθa' — i.e. Nourai's arrow — but the mainstream view takes ارّاده/عرّاده to be the Arabic siege engine ʿarrāda (root ʿ-r-d) and ارابه to be a Turkic loan (araba), so this word is no better than plausible. laškar is wrong: Cheung 2007 p.195 derives NP laškar from Proto-Iranian *Hraxša-kara- 'making protection' (root *Hraxš 'to protect', Skt. rakṣ-) with dissimilatory loss of -x-, and Wiktionary follows him; Mo'in, in his own footnote at Borhan p.1895 which Nourai cites here, reports Purdavud's raθaēštar > artēštar > *laštar > laškar proposal and rejects the last step as 'far-fetched'. The parenthesis (عسکر) is right in direction though: Arabic ʿaskar is generally taken as a borrowing of MP laškar (Jawaliqi, al-Muʿarrab, quoting Ibn Qutayba 'al-ʿaskar is Persian arabicised' and Ibn Durayd 'it is laškar in Persian'), not the other way round.\",\n  \"derivation_fa\": \"«ارتشتار» درست است: raθaēštar- اوستایی در فارسی میانه artēštār «جنگاور» شده (مکنزی ص ۱۲؛ بارتولومه نیز برابر پهلوی واژهٔ اوستایی را همین artēštār می‌آورد)، و خوشهٔ آغازی raθ- بر اثر قلب و افزایش واکهٔ آغازین به art- بدل شده است؛ حاشیهٔ معین بر برهان قاطع (ص ۹۷، ذیل «ارتشدار») همین را می‌گوید. «ارتش» امروزی هم واژه‌ای است که فرهنگستان در ۱۳۱۴ از همین artēštār ساخته است. «ارّاده» در فارسی هست (معین: گردونه، ارابه) و اصبغی (۱۹۸۸، ص ۸) به نقل از بهارِ عجم آن را با raθa- اوستایی و پارسی باستان می‌سنجد؛ ولی دیدگاه رایج، «ارّاده/عرّاده» را واژه‌ای عربی (از ریشهٔ ع‌ر‌د، منجنیق کوچک) و «ارابه» را وام‌واژهٔ ترکی می‌داند، پس این بند بیش از «با احتیاط پذیرفتنی» نیست. «لشکر» اما نادرست است: چونگ آن را از *Hraxša-kara- ایرانی آغازین («نگهبانی‌کننده»، از ریشهٔ *Hraxš «پاسداشتن»، هم‌ریشه با rakṣ- سنسکریت) با حذف ناهمگون‌ساز -x- می‌داند، و خودِ معین در همان حاشیهٔ ص ۱۸۹۵ برهان که نورایی به آن ارجاع داده، فرضیهٔ پورداود (ارتشتر > لشتر > لشکر) را «بعید» شمرده است. تنها «عسکر» درست است: تازیان آن را از «لشکر» فارسی میانه گرفته‌اند (جوالیقی، المعرّب).\",\n  \"sources\": [W + \"%D9%84%D8%B4%DA%A9%D8%B1\", W + \"%D8%B9%D8%B3%D9%83%D8%B1\", \"https://abadis.ir/fatofa/%D8%A7%D8%B1%D8%A7%D8%AF%D9%87/\"],\n  \"ref_check\": [\n    {\"ref\": \"BQT:97\", \"status\": \"supports\",\n     \"note\": \"Borhan-e Qateʿ vol.1 p.97 (BQT_v1_pages.txt leaf 307, the leaf that ends 'بقیه در صفحهٔ ۹۸'): headword «ارتشدار ... لشکری و سپاهی را گویند», with Mo'in's footnote 4: «در اوستا raθaēštār و در گزارش پهلوی ... آماده، مهیای جنگ». Exactly Nourai's Avestan -> Persian arrow for arteštâr.\"},\n    {\"ref\": \"BQT:1895\", \"status\": \"partial\",\n     \"note\": \"Borhan vol.3 p.1895 (rendered with tools/ref_page.py; image at data/verification/sources/refs/ocr/BQT/1895.png), Mo'in's footnote 5 s.v. لشکر: «معرّب آن عسکر ... آقای پورداود احتمال می‌دهند که این کلمه از اوستایی raθaēštar و پهلوی artēštār (رزمی، سپاهی) (رک: ص ۹۷ ح ۵) ناشی شده. بدین وجه ارتشتر > رشتر > لشتر، اما تبدیل لشتر به لشکر بعید می‌نماید». The page does carry Nourai's etymology — attributed to Purdavud — but Mo'in himself calls the crucial step far-fetched.\"},\n    {\"ref\": \"MON:191\", \"status\": \"not_checked\",\n     \"note\": \"Mo'in's Farhang-e Farsi is only available here as unpaginated OCR and via vajehyab/abadis, so vol.1 p.191 cannot be verified; the entry itself exists: «ارّاده (اَ رّ دِ) (اِ.) گردونه، ارابه» (abadis.ir, Farhang-e Mo'in section).\"},\n    {\"ref\": \"ARB:203\", \"status\": \"supports\",\n     \"note\": \"al-Jawaliqi, al-Muʿarrab (ARB_mo3rb.txt lines 17003-17018, the ʿaskar entry): «قال ابن قتيبة: العسكر فارسي معرب. قال ابن دريد: هو لشكر بالفارسية وهو مجتمع الجيش» — the classical statement that Arabic ʿaskar is Persian laškar arabicised; the editor (Shakir) adds a dissenting footnote «والظاهر أن الكلمة عربية».\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"CHEUNG\", \"where\": \"s.v. *Hraxš 'to protect, defend' (~p.195; CHEUNG.txt line 13330)\", \"stance\": \"contradicts\",\n     \"note\": \"'*NWIR: NP laskar \\\"army\\\" (dissim. loss of -x-, from *Hraxša-kara-)' — laškar belongs to the root of Skt. rakṣ- 'to protect', PIE *Holek-s-, Pok. 32, not to *ret- 866.\"},\n    {\"src\": \"PHD\", \"where\": \"MacKenzie 1971 s.vv. artēštār, laškar (PHD.txt lines 214, 432)\", \"stance\": \"partial\",\n     \"note\": \"'artēštār [ʾrtštʾl | N artēšdār] warrior' (supports arteštâr) and 'laškar [lškl | N ~] army' (the MP word exists, but MacKenzie gives no etymology).\"},\n    {\"src\": \"LKT\", \"where\": \"Lokotsch no. 1307 (LKT.txt line 3045)\", \"stance\": \"contradicts\",\n     \"note\": \"s.v. laškar: «'Heer, Feldlager' [verwandt mit ar. ʿaskar, byzantinisch-gr. ἐξάρκητον, lat. exercitus, von denen das lat. Wort wohl das ursprüngliche Grundwort ist; ... vgl. Völlers ZDMG L,646, der das ar. Wort aus dem Pers. entlehnen will] ; hieraus engl.-angloind. lascar» — several origins are canvassed, none of them raθa-.\"},\n    {\"src\": \"PLA\", \"where\": \"Asbaghi 1988 p.8 s.v. ʾarāba (PLA_pages.txt leaf 23)\", \"stance\": \"partial\",\n     \"note\": \"«ʾarāba: \\\"Wagen\\\" pers., die arabisierte Form heißt عربة ʿaraba u. ʿarabāna ... Der Verfasser v. Bahār ul-ʿAǧam ist der Ansicht, daß araba eigentl. ʿarrāda \\\"Geschützlafette, Wurfgeschoßrad\\\" heißt. vgl. ap. raθa, aw. raθa, mand. arada» — the one source that does connect the arrāda/arāba word with Av./OP raθa-.\"},\n    {\"src\": \"BQT\", \"where\": \"Borhan vol.1 p.96 (BQT_v1_pages.txt leaf 306)\", \"stance\": \"partial\",\n     \"note\": \"«ارابه - بر وزن فرابه، گردون را گویند» — the cart-word on the page just before Nourai's BQT:97; Borhan gives no etymology for it.\"}\n  ]\n})\n\nN.append({\n  \"id\": 3, \"lang\": \"Pahlavi\",\n  \"words\": \"râs\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"'rās' is the graphic (Book Pahlavi) reading of the word MacKenzie transcribes rāh 'road, way': the heterographic spelling is <lʾs> (Manichaean <rʾh>), which older Iranists and the Persian tradition read literally as rās. Hübschmann, Persische Studien 66 (the reference Nourai cites on the next node) puts it exactly so: 'Geht rah \\\"Weg\\\" ... auf ap. *rāθa- zurück, so kann das Wort im Pehlevi, wo rās geschrieben wird, in alter Zeit doch nur *rāθ, jünger rāh gelautet haben' — i.e. Pahlavi <rās> stands for *rāθ > rāh, because intervocalic/final Old Iranian θ became h in Middle Persian. The word is not derived from the noun raθa- 'chariot' itself but from a lengthened-grade abstract *Hrāθah- (Proto-Iranian *Hrāθáh, Skt. rathyā- 'carriage road' beside ratha-), so the arrow 'Avestan -> Pahlavi' is right at root level and only loose at stem level.\",\n  \"derivation_fa\": \"«راس» خوانشِ حرف‌به‌حرفِ نوشتار پهلوی <lʾs> است؛ همان واژه‌ای که مکنزی آن را rāh «راه» آوانویسی می‌کند (در پهلوی مانوی <rʾh>). هوبشمان در «مطالعات فارسی» (ص ۶۶) همین را می‌گوید: اگر «راه» از *rāθa- پارسی باستان آمده باشد، در پهلوی که «rās» نوشته می‌شود، تلفظ کهن آن جز *rāθ و سپس‌تر rāh نمی‌توانسته باشد — چون «ث» ایرانی باستان در فارسی میانه به «ه» بدل می‌شود. باید توجه داشت که «راه» از خودِ اسم raθa- «گردونه» ساخته نشده، بلکه از صورت کشیده‌بنِ *Hrāθah- (هم‌سنگ rathyā- سنسکریت «راهِ گردونه») برآمده است؛ پس پیکان «اوستایی ← پهلوی» در سطح ریشه درست و در سطح ستاک تقریبی است. حاشیهٔ معین بر برهان قاطع نیز «راس» پهلوی را به معنی «راه» می‌آورد.\",\n  \"sources\": [W + \"%D8%B1%D8%A7%D9%87\"],\n  \"ref_check\": [\n    {\"ref\": \"BQT:934\", \"status\": \"supports\",\n     \"note\": \"Borhan vol.2 p.933/934 (BQT_v2_pages.txt leaf 390, ±1 page): the entry «راک ... و بلغت زند و پازند راه باشد که بعربی صراط و طریق خوانند», with Mo'in's footnote 2: «راک قرائتی است از «راس» پهلوی (بمعنی راه)». Precisely the Pahlavi rās = rāh that Nourai's box asserts.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"PHD\", \"where\": \"MacKenzie 1971 p.70 s.v. rāh (PHD.txt line 555)\", \"stance\": \"supports\",\n     \"note\": \"'rāh [lʾs | M rʾh, N ~] road, way' — MacKenzie's transcription rāh with the Pahlavi graph <lʾs>, i.e. Nourai's 'rās'; the same line also has 'rāh-dār ... brigand, highway robber' and 'rāh-nimāy ... guide'.\"},\n    {\"src\": \"HUB\", \"where\": \"Persische Studien p.66 no. 607 (HUB.txt leaf 77)\", \"stance\": \"supports\",\n     \"note\": \"'... so kann das Wort im Pehlevi, wo rās geschrieben wird, in alter Zeit doch nur *rāθ, jünger rāh gelautet haben. Ich glaube dann nicht an rās als neupersische Nebenform.'\"},\n    {\"src\": \"NYB\", \"where\": \"Nyberg, Manual II (glossary), grep 'rās', 'rāh'\", \"stance\": \"silent\",\n     \"note\": \"the OCR of NYB_vol2_glossary.txt returns no usable line for this word (Nyberg's transliteration conventions and the OCR of his diacritics defeat the grep).\"}\n  ]\n})\n\nN.append({\n  \"id\": 4, \"lang\": \"Persian\",\n  \"words\": \"râh\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"NP راه rāh 'road, way, manner' continues MP rāh (<lʾs>) < Proto-Iranian *Hrāθáh- < PIE *Hret-; Wiktionary (citing MacKenzie 1971:70 and Edelman, EDIL VI) gives exactly this chain, and Horn no. 607 sets out the same ('rah, rās, reh \\\"Weg\\\"; skr. vergl. rathyā- \\\"Landstrasse\\\" ... von ratha-'). The variants in Nourai's parenthesis are all real: رَه rah is the metrically shortened form used in verse, and رهرو/راهرو rah-row/rāh-row 'wayfarer, corridor' is rāh + the present stem row- of raftan (MP raw-). The sense 'manner, way (of doing)' is the ordinary metaphorical extension, already Middle Persian. One caveat on the sources: Nourai's FFD:56 belongs to a different word — Abolqasemi's page 56 treats the verb رَستن/رَهیدن 'to escape' (present stem رَه rah- < MP rah- < Old Persian raθ- 'to leave, escape'), the root that Bartholomae lists as OP rad- with ava-; Hübschmann had already warned 'Np. rastan gehört nicht hierher'.\",\n  \"derivation_fa\": \"«راه» فارسی نو دنبالهٔ rāh فارسی میانه (نوشتار <lʾs>) است، و آن از *Hrāθah- ایرانی آغازین و در نهایت از ریشهٔ *Hret- هندواروپایی؛ ویکی‌واژه به استناد مکنزی (۱۹۷۱، ص ۷۰) و ادلمان همین زنجیره را می‌آورد و هرن (بند ۶۰۷) نیز آن را با rathyā- سنسکریت «راهِ گردونه» می‌سنجد. صورت‌های داخل کمانک همگی واقعی‌اند: «رَه» کوتاه‌شدهٔ شعری «راه» است و «رهرو/راهرو» از «راه» + ستاک حال «رو» (از رفتن، فارسی میانه raw-) ساخته شده است. معنی «شیوه، روش» گسترش استعاری کهنی است. تنها نکتهٔ اصلاحی در ارجاعات است: ص ۵۶ کتاب ابوالقاسمی (FFD) دربارهٔ فعل «رَستن/رهیدن» و ستاک «رَه» (از *raθ- پارسی باستان به معنی «گریختن») است، نه دربارهٔ «راه»؛ هوبشمان هم پیش‌تر هشدار داده بود که «رستن» به این خانواده تعلق ندارد.\",\n  \"sources\": [W + \"%D8%B1%D8%A7%D9%87\"],\n  \"ref_check\": [\n    {\"ref\": \"HUB:66\", \"status\": \"supports\",\n     \"note\": \"Hübschmann, Persische Studien p.66 no. 607 (HUB.txt leaf 77): 'Geht rah \\\"Weg\\\" = paz. rah = arm. rah (bei Faustus V. Byz.) auf ap. *rāθa- (Horn vergleicht skr. rathya- \\\"Fahrstrasse\\\" von ratha- = zd. raθa- \\\"Wagen\\\") zurück, so ...' — the exact derivation drawn in the chart.\"},\n    {\"ref\": \"BQT:984\", \"status\": \"supports\",\n     \"note\": \"Borhan vol.2, the رَه section (BQT_v2_pages.txt leaves 445-446, printed ≈988-989, i.e. Nourai's 984 ±4): «رَه: بفتح اول و سکون ثانی، مخفف راه است ... که به عربی طرق گویند - و به معنی مرتبه و بار هم هست چنانکه گویند «یک ره»» — Borhan on the short form رَه of Nourai's parenthesis.\"},\n    {\"ref\": \"PLA:133\", \"status\": \"partial\",\n     \"note\": \"Asbaghi 1988 p.133 (PLA_pages.txt leaf 148) s.v. rāhib: '... pers. راه rāh < mp. rāh, am. rās, air. *rāδa' — Asbaghi attests the Persian word and its Middle Persian/Old Iranian prehistory, but the entry is about the Arabic loan rāhib, not about rāh itself.\"},\n    {\"ref\": \"FFD:56\", \"status\": \"contradicts\",\n     \"note\": \"Abolqasemi, Feʿl-hā-ye Fārsi-ye Dari, printed p.56 (FFD_pages.txt [pdf page 61]) is the entry «رَستن»: «رَه < فارسی میانه rah < فارسی باستان *raθ- ... < ایرانی باستان: گریختن» — the verb 'to escape', a homonymous رَه from Old Persian raθ- 'to leave, deviate', not the noun راه 'road'.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 607 (HRN.txt line 5422)\", \"stance\": \"supports\",\n     \"note\": \"'607. rah, rās, reh \\\"Weg\\\"; espres. skr. vergl. rathyā- \\\"Landstrasse\\\" (spät); phlv. rās, asp-rās; afgh. lār. LW. kurd. rī; bal. rā, n. rah; afgh. rāh; arm. rah.' Horn adds the doubt 'Np. rastan gehört nicht hierher' about the escape-verb.\"},\n    {\"src\": \"PHD\", \"where\": \"MacKenzie 1971 p.70 (PHD.txt line 555)\", \"stance\": \"supports\",\n     \"note\": \"'rāh [lʾs | M rʾh, N ~] road, way'; the derivatives rāh-dār and rāh-nimāy stand in the same entry, showing the compounding pattern of node 5.\"},\n    {\"src\": \"BQT\", \"where\": \"Borhan vol.2 leaf 390 (p.933/934)\", \"stance\": \"supports\",\n     \"note\": \"«... و بلغت زند و پازند راه باشد که بعربی صراط و طریق خوانند» with Mo'in's note on Pahlavi rās — the Persian lexicographic tradition ties رَاه to Pahlavi rās.\"}\n  ]\n})\n\nN.append({\n  \"id\": 5, \"lang\": \"Persian\",\n  \"words\": \"rahbar; râygân; râhbân; râheb\",\n  \"verdict\": \"disputed\",\n  \"derivation\": \"rahbar 'guide' = rah 'way' + -bar, present stem of bordan 'to lead, carry' (MP rāh-bar; the synonyms in the parenthesis, rahnamā/rāhnamā, are rah + namā 'shower', beside MP rāh-nimāy in MacKenzie p.70) — confirmed. râygân 'free of charge' is rāh + the suffix -gān, literally 'of the road, (as if) picked up on the road'; Wiktionary derives it exactly so, from راه + ـگان, and the semantic route 'lying on the road' > 'ownerless' > 'gratis' is the standard explanation — confirmed. râhbân 'road guard' is a regular rāh + bān 'keeper' compound (like bāghbān, galleh-bān) and is attested — plausible. râheb 'monk' is the disputed one: Arabic راهب rāhib is the active participle of رَهِبَ rahiba 'to fear, be in awe (of God)', from the common Semitic root r-h-b (cf. Heb. rahab), and Persian راهب is a loan back from Arabic; Wiktionary and the standard Arabic lexica give no Persian origin. Nourai is not inventing it, however: Asbaghi 1988 p.133 — the very page he cites — does derive Arabic rāhib from Persian rāh-bān 'the one who guards, and therefore knows, the road', and the Borhan (vol.2, p.≈989) etymologises رهبان as ره + بان 'keeper of the good way'. That is a Persian folk-etymology of an Arabic word, reinforced by the accidental similarity of the Arabic plural ruhbān to Persian rāhbān; modern scholarship rejects it.\",\n  \"derivation_fa\": \"«رهبر» از «ره» + ستاک حال «بر» (بردن) است (فارسی میانه rāh-bar)؛ «رهنما/راهنما» نیز از «ره/راه» + «نما» ساخته شده و صورت پهلوی آن rāh-nimāy در فرهنگ مکنزی آمده است — درست. «رایگان» از «راه» + پسوند «ـگان» است («آنچه در راه یافته شود»)، و همین را ویکی‌واژه می‌آورد؛ تحول معنایی «افتاده در راه» ← «بی‌صاحب» ← «مفت» روشن است — درست. «راهبان» ترکیب قاعده‌مند «راه + بان» (مانند باغبان و گله‌بان) و واژه‌ای واقعی است — پذیرفتنی. اما «راهب» پذیرفتنی نیست: «راهب» عربی اسم فاعل «رَهِبَ» (ترسیدن، پروا داشتن) از ریشهٔ سامی ر‌ه‌ب است و «راهب» فارسی وام‌واژه‌ای است از عربی. با این حال باید انصاف داد که نورایی این را از خود نساخته: اصبغی در همان صفحهٔ ۱۳۳ که بدان ارجاع می‌دهد، «راهب» عربی را از «راه‌بان» فارسی می‌داند، و برهان قاطع نیز «رهبان» را «ره (نیک) + بان (نگهدارنده)» تفسیر کرده است — ریشه‌شناسی عامیانه‌ای که از شباهت اتفاقی جمع عربی «رهبان» با «راهبان» فارسی مایه گرفته و پژوهش امروزی آن را رد می‌کند.\",\n  \"sources\": [W + \"%D8%B1%D8%A7%DB%8C%DA%AF%D8%A7%D9%86\", W + \"%D8%B1%D8%A7%D9%87%D8%A8\"],\n  \"ref_check\": [\n    {\"ref\": \"HUB:66\", \"status\": \"partial\",\n     \"note\": \"Hübschmann no. 607 establishes rāh/rah itself (see node 4) but says nothing about rahbar, rāygān, rāhbān or rāhib.\"},\n    {\"ref\": \"BQT:984\", \"status\": \"supports\",\n     \"note\": \"Borhan vol.2 leaf 446 (printed ≈989, Nourai's 984 ±5): «رهبان: به ضم اول و بای ابجد ... زاهد و پرهیزکار باشد و وجه تسمیه‌اش محافظت‌کنندهٔ نیکی و سیرت نیک باشد چه ره به معنی نیک و بان به معنی محافظت‌کننده است چنانکه باغبان و گله‌بان»; «رهبر: بر وزن شهیر، به معنی دلیل و برهان باشد» stands in the same column, and رایگان is at leaves 395-396.\"},\n    {\"ref\": \"PLA:133\", \"status\": \"supports\",\n     \"note\": \"Asbaghi 1988 p.133 (PLA_pages.txt leaf 148): «rāhib: \\\"christlicher Mönch\\\" pers., wahrscheinlich aus dem pers. راه rāh < mp. rāh ... + pers. بان bān \\\"der den (Weg) schützt und daher kennt\\\". s. ruhbān.» — Nourai's rāhbān > rāhib derivation is Asbaghi's, verbatim.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"Klein s.v. rabbi/rehoboam etc.; grep 'rahib', 'ruhban'\", \"stance\": \"silent\",\n     \"note\": \"Klein has no entry for the Arabic monk-word; the English borrowings of this Semitic root are absent from his dictionary.\"},\n    {\"src\": \"FVQ\", \"where\": \"Jeffery, Foreign Vocabulary of the Qurʾān (grep 'ruhban', 'rahib')\", \"stance\": \"silent\",\n     \"note\": \"the OCR of FVQ.txt yields no entry for رهبان/راهب; Jeffery's list of Qurʾānic foreign words does not claim a Persian source for it (the word is treated by others as a Syriac-influenced native formation).\"},\n    {\"src\": \"PHD\", \"where\": \"MacKenzie 1971 p.70 (PHD.txt line 555)\", \"stance\": \"supports\",\n     \"note\": \"'rāh-dār [lʾsdʾl | N ~] brigand, highway robber' and 'rāh-nimāy [lʾsnmʾd | (M rʾhnmwdʾr), N ~numā] guide' — Middle Persian already forms exactly this kind of rāh + agent compound, which is what rahbar/rāhbān continue.\"},\n    {\"src\": \"MON\", \"where\": \"Farhang-e Moʿin s.v. راهب (via abadis.ir)\", \"stance\": \"contradicts\",\n     \"note\": \"Moʿin tags راهب as [ع.] (Arabic), i.e. a loan from Arabic into Persian, not a Persian formation.\"}\n  ]\n})\n\nN.append({\n  \"id\": 6, \"lang\": \"Arabic\",\n  \"words\": \"torrahât\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"Arabic التُّرَّهات, sg. تُرَّهة turraha, is defined by al-Jawhari and Ibn Manẓūr (Lisān al-ʿArab s.v. ت ر ه) as 'الطُّرُقُ الصِّغارُ غير الجادَّةِ تتشعّبُ عنها' — 'the small paths branching off the main road' — and the same entry adds 'فارسيٌّ معرَّبٌ', 'a Persian word arabicised'. Asbaghi 1988 p.88 states the source precisely: 'turraha \\\"Seitenpfad\\\", pers., wahrscheinlich aus dem pers. ره rah \\\"Weg\\\", mp. rāh abgeleitet'. So the arrow Persian rāh/rah -> Arabic turraha is exactly what both the classical Arab lexicographers and the modern specialist monograph on Persian loanwords in Arabic say; the abstract sense 'nonsense, worthless things' is the metaphorical extension inside Arabic ('to take the side-tracks' = to stray from the plain truth), already in the classical idioms turrahāt al-basābis / al-ṣaḥāṣiḥ 'sheer falsehoods'. The doubling of the r and the -a(t) ending are the Arabic morphological adaptation.\",\n  \"derivation_fa\": \"«تُرَّهات» عربی (مفرد: تُرَّهة) در لسان‌العرب (ذیل ت‌ر‌ه، به نقل از جوهری) چنین تعریف شده است: «التُّرَّهاتُ الطُّرُقُ الصِّغارُ غيرُ الجادّةِ تتشعّبُ عنها» و بی‌درنگ افزوده شده «فارسيٌّ معرَّبٌ». اصبغی (۱۹۸۸، ص ۸۸) سرچشمه را دقیق‌تر می‌کند: turraha «راهِ فرعی»، احتمالاً برگرفته از «رَه» فارسی و rāh فارسی میانه. پس پیکان «راه ← ترّهات» همان است که هم واژه‌شناسان کلاسیک عرب و هم پژوهش امروزی دربارهٔ وام‌واژه‌های فارسی در عربی می‌گویند. معنای «یاوه، بیهوده» گسترش استعاری درون‌عربی است (بیراهه رفتن = از جادهٔ حقیقت منحرف شدن)، چنانکه در تعبیر کهن «ترّهات البسابس» دیده می‌شود. تشدید «ر» و پایانهٔ «ـة» نیز سازگارسازی صرفی عربی است.\",\n  \"sources\": [\"https://www.islamweb.net/ar/library/content/122/833/%D8%AA%D8%B1%D9%87\"],\n  \"ref_check\": [\n    {\"ref\": \"TAD:17\", \"status\": \"not_found\",\n     \"note\": \"Tobia al-ʿUnaysi, Tafsīr al-alfāẓ al-dākhila: the local OCR (TAD_pages.txt, 87 leaves, very poor Arabic OCR) yields no hit for ترهات / ترّهة / تره anywhere in the file, so the cited p.17 could not be read. (The same file does show the parallel Persian-loan entry «عسكر — فارسي: لشكر، معناه جيش» used at node 2, so the book is of the right kind for this claim.)\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"PLA\", \"where\": \"Asbaghi 1988 p.88 s.v. turraha (PLA_pages.txt leaf 103, line 4343)\", \"stance\": \"supports\",\n     \"note\": \"«turraha: \\\"Seitenpfad\\\", pers., wahrscheinlich aus dem pers. ره rah \\\"Weg\\\", mp. rāh abgeleitet.»\"},\n    {\"src\": \"AFM\", \"where\": \"Addi Shir, al-Alfāẓ al-fārisiyya al-muʿarraba (AFM_pages.txt line 907)\", \"stance\": \"partial\",\n     \"note\": \"the (badly OCRed) line «... وقع في ترّهات ... الباطل: كل ذلك من راه أي [الطريق]» reads as Addi Shir's own derivation of the ترّهات idiom from Persian راه 'road' — the same claim, from the other standard Arabic-side collection.\"},\n    {\"src\": \"KLN\", \"where\": \"Klein (grep 'turraha')\", \"stance\": \"silent\",\n     \"note\": \"the word has no English reflex and no Klein entry.\"}\n  ]\n})\n\nN.append({\n  \"id\": 7, \"lang\": \"Persian\",\n  \"words\": \"torrahât\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"Persian تُرَّهات torrahāt 'nonsense, worthless things' is the Arabic broken plural taken back into Persian — a classic Persian > Arabic > Persian round trip: Persian rah/rāh 'road' gave Arabic turraha 'side-path' (node 6), which developed the sense 'triviality, falsehood' in Arabic and was re-borrowed into literary Persian in its plural form, already common in the 6th/12th-7th/13th centuries, whence Rumi's line quoted in the chart, «نخوت و دعوی و کبر و تُرَّهات / دور کن از دل که تا یابی نجات». Moʿin's dictionary registers it as an Arabic loan: «تُرَّهه [ع. ترهة] (اِ.) بیهوده، یاوه؛ سخن بی‌فایده؛ ج. ترهات». The Persian form keeps the Arabic gemination and the sound-plural -āt, which is itself the mark of the re-borrowing.\",\n  \"derivation_fa\": \"«تُرَّهات» در فارسی جمع مکسّر عربیِ «تُرَّهة» است که دوباره به فارسی بازگشته — نمونه‌ای روشن از رفت‌وبرگشت فارسی ← عربی ← فارسی: «رَه/راه» فارسی در عربی «تُرَّهة» (بیراهه) شد، در عربی معنای «یاوه و باطل» گرفت و سپس به‌صورت جمع وارد فارسی ادبی شد؛ در سده‌های ششم و هفتم هجری کاربرد آن رایج است، چنانکه در بیت مولوی که خودِ کتاب نقل کرده: «نخوت و دعوی و کبر و تُرَّهات / دور کن از دل که تا یابی نجات». فرهنگ معین آن را با نشانهٔ [ع.] یعنی عربی ثبت کرده است: «تُرَّهه [ع.] (اِ.) بیهوده، یاوه؛ ج. ترهات». نگه‌داشتن تشدید و پایانهٔ جمع «ـات» خود نشانهٔ وام‌گیری دوباره از عربی است.\",\n  \"sources\": [\"https://www.islamweb.net/ar/library/content/122/833/%D8%AA%D8%B1%D9%87\"],\n  \"ref_check\": [\n    {\"ref\": \"MON:1074\", \"status\": \"partial\",\n     \"note\": \"the entry is in Moʿin (MON_part1.txt line 40294): «تُرَّهه [ع. ترهة] (اِ.) (کم.) بیهوده، یاوه. سخن بی‌فایده؛ ج. ترهات» — it confirms the Persian word and glosses it as Nourai does, but Moʿin tags it simply [ع.] 'Arabic' and gives no Persian etymology; the page number 1074 cannot be checked because the local Moʿin OCR is unpaginated.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"BQT\", \"where\": \"Borhan-e Qateʿ (grep ترهات in BQT_v1/v2_pages.txt)\", \"stance\": \"silent\",\n     \"note\": \"no entry for ترهات in the OCR of vols 1-2; the Borhan is a dictionary of Persian (dari) words and generally omits plain Arabic plurals.\"},\n    {\"src\": \"PLA\", \"where\": \"Asbaghi 1988 p.88\", \"stance\": \"supports\",\n     \"note\": \"by deriving the Arabic turraha from Persian rah, Asbaghi makes the Persian torrahāt a re-borrowing, which is exactly the shape of Nourai's two boxes.\"},\n    {\"src\": \"MON\", \"where\": \"Farhang-e Moʿin, s.v. ترّهه\", \"stance\": \"partial\",\n     \"note\": \"«[ع.]» tag: Moʿin's synchronic label is 'Arabic', i.e. the word entered Persian from Arabic — compatible with the round trip but not asserting it.\"}\n  ]\n})\n\nN.append({\n  \"id\": 8, \"lang\": \"Old Persian\",\n  \"words\": \"ratha; u-ratha\",\n  \"verdict\": \"plausible\",\n  \"derivation\": \"Kent's lexicon p.176 has 'uraθa- adj. \\\"having good chariots\\\"; Skt. su-ratha- as man's name: u- \\\"good\\\" + raθa- \\\"wagon\\\", Av. raθa-, Skt. rátha-, Lt. rota \\\"wheel\\\" (§143.II)', attested in the Susa inscription DSs 5 as uraθā-cā 'and good chariots', with the derivative uraθara- 'having good charioteers' (DSp 3). So u-ratha and its gloss are exactly right, and Nourai's cross-reference to 'Su 1' (the prefix u- 'good', Av. hu-, Skt. su-) is right too. The one qualification: the simplex raθa- is not attested in Old Persian — Kent lists it only among the stems that occur exclusively inside compounds ('raθa- in u-raθa-', §153) and states in his phonology 'pIE *rotho-, OP u-raθa- \\\"having good chariots\\\"'. Putting a free-standing 'ratha : chariot' in an Old Persian box is therefore a reconstruction, not an attested word.\",\n  \"derivation_fa\": \"کنت در واژه‌نامهٔ پارسی باستان (ص ۱۷۶) آورده است: «uraθa- صفت، «دارندهٔ گردونه‌های خوب»: u- «خوب» + raθa- «گردونه»، مقایسه شود با raθa- اوستایی، rátha- سنسکریت و rota لاتینی»، که در کتیبهٔ شوش (DSs 5) به‌صورت uraθā-cā گواهی شده، و نیز uraθara- «دارندهٔ گردونه‌رانان خوب» (DSp 3). پس «u-ratha» و معنای آن درست است و ارجاع نورایی به پیشوند «هو/su» نیز بجاست. تنها نکته اینکه صورت سادهٔ raθa- در پارسی باستان گواهی نشده است؛ کنت آن را در شمار ستاک‌هایی می‌آورد که «تنها در ترکیب» دیده می‌شوند («raθa- در u-raθa-»). بنابراین آوردن «ratha: گردونه» به‌عنوان واژه‌ای مستقل در خانهٔ پارسی باستان، بازسازی است نه واژهٔ ثبت‌شده.\",\n  \"sources\": [\"https://archive.org/details/oldpers/page/n200\"],\n  \"ref_check\": [\n    {\"ref\": \"KNT:176\", \"status\": \"supports\",\n     \"note\": \"Kent, Old Persian, Lexicon p.176 (KNT.txt leaf 200, the leaf after the one marked '176'): 'uraθa- adj. \\\"having good chariots\\\"; Skt. su-ratha- as man's name: u- \\\"good\\\" + raθa- \\\"wagon\\\", Av. raθa-, Skt. rátha-, Lt. rota \\\"wheel\\\" (§143.II). See also uraθara-. uraθā-cā apn. as sb. \\\"good chariots\\\" DSs 5.' Kent's grammar adds (§: 'pIE *rotho-, OP u-raθa- \\\"having good chariots\\\"') and lists 'raθa- in u-raθa-' among stems occurring only in compounds.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"BRT\", \"where\": \"AiW col. 1505 s.v. raθa- (BRT.txt line 25078)\", \"stance\": \"supports\",\n     \"note\": \"'j. raθa- m. \\\"Wagen\\\" ... ai. ratha- m.; mp. ras' — the Avestan cognate of the Old Persian compound member.\"},\n    {\"src\": \"TLM\", \"where\": \"Tolman, Ancient Persian Lexicon (grep 'uratha', 'raθa')\", \"stance\": \"silent\",\n     \"note\": \"Tolman's 1908 lexicon predates the Susa inscriptions DSs/DSp in which uraθa- was found, so the word is absent.\"},\n    {\"src\": \"POK\", \"where\": \"IEW 866\", \"stance\": \"partial\",\n     \"note\": \"Pokorny cites Old Indic ratha- and Avestan raθa- but no Old Persian form; the Old Persian evidence comes from Kent alone.\"}\n  ]\n})\n\nN.append({\n  \"id\": 9, \"lang\": \"None\",\n  \"words\": \"\",\n  \"verdict\": \"unverified\",\n  \"derivation\": \"An empty box: the printed page (pdf 422, image kept at data/verification/sources/refs/ocr/BOOK/422.png) shows an outlined rectangle to the right of the Old Persian box, with an arrow running into it from 'Old Persian', but no language header, no reference and no word inside it. The extraction is faithful to the book. It is a layout accident of Nourai's chart software — the same page has a French box with a header but no words (node 11), and here even the header failed to print; judging by the position (the slot where the Persian reflexes of the Old Persian box would go, mirroring the Avestan->Persian row above) the box was probably meant to hold nothing more than the continuation arrow. There is no claim here to verify.\",\n  \"derivation_fa\": \"این خانه یکسره تهی است: در صفحهٔ چاپی (تصویرِ نگهداری‌شده در data/verification/sources/refs/ocr/BOOK/422.png) کادری با خط دور در سمت راست خانهٔ «پارسی باستان» دیده می‌شود که پیکانی از آن خانه به آن می‌رسد، اما نه سرواژهٔ زبان دارد، نه ارجاع و نه واژه. خوانش اسکن درست است و خطا از کتاب است — در همین صفحه خانهٔ «فرانسه» هم سرواژه دارد ولی واژه‌ای در آن نیست. با توجه به جای آن (همان جایگاهی که در ردیف بالا خانهٔ فارسیِ برآمده از اوستایی نشسته است) به‌احتمال چیزی جز ادامهٔ پیکان در آن نبوده است. ادعایی برای راستی‌آزمایی وجود ندارد.\",\n  \"sources\": [],\n  \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the box carries no reference of its own.\"}],\n  \"consulted\": [{\"src\": \"BOOK\", \"where\": \"printed page 392 = pdf 422 (data/verification/sources/refs/ocr/BOOK/422.png)\", \"stance\": \"silent\", \"note\": \"the box is printed blank; the JSON's note 'box is printed entirely blank in the source' is correct.\"}]\n})\n\nN.append({\n  \"id\": 10, \"lang\": \"Latin\",\n  \"words\": \"rota; ret-undus\",\n  \"verdict\": \"transcription_suspect\",\n  \"error_in\": \"book\",\n  \"book_prints\": \"ret-undus : wheel\",\n  \"correct_form\": \"rotundus 'round'\",\n  \"derivation\": \"rota 'wheel' is perfect: it is the o-grade *Hrot-eh2 of the root (Watkins: 'Suffixed o-grade form *rot-a- in Latin rota, wheel'), with exact cognates in Lithuanian ratas, Old High German rad, Old Irish roth. The second word, printed 'ret-undus : wheel', is wrong twice over and the error is the book's, not the extraction's: the page image (data/verification/sources/refs/ocr/BOOK/422.png) plainly shows 'ret-undus : wheel'. The Latin word is rotundus 'round, circular' — derived from rota with the rare adjectival suffix -undus (as in secundus from sequor) — and it means 'round', not 'wheel'; Pokorny 866 has 'rotundus \\\"scheibenrund\\\"', Buck 12.81 the same. Nourai evidently re-spelled the first syllable to make the root shape 'ret-' visible, but the result is not a Latin word.\",\n  \"derivation_fa\": \"«rota» درست است: صورت بن‌کشیدهٔ o دار ریشه، یعنی *Hrot-eh₂ («چرخ»)، که ratas لیتوانیایی، rad آلمانی باستان و roth ایرلندی کهن هم‌ریشهٔ آن‌اند. اما واژهٔ دوم که «ret-undus: wheel» چاپ شده از دو جهت نادرست است و خطا از خودِ کتاب است نه از خوانش اسکن: تصویر صفحهٔ چاپی (data/verification/sources/refs/ocr/BOOK/422.png) به‌روشنی «ret-undus : wheel» نشان می‌دهد. واژهٔ لاتین rotundus است («گِرد»، از rota با پسوند کم‌کاربرد -undus مانند secundus)، و معنای آن «گِرد» است نه «چرخ»؛ پوکورنی (ص ۸۶۶) نیز «rotundus \\\"scheibenrund\\\"» آورده است. نورایی ظاهراً هجای نخست را دست‌کاری کرده تا شکل ریشه («ret-») پیدا باشد، ولی حاصل، واژه‌ای لاتین نیست. پس: خطای چاپی/ویرایشی کتاب.\",\n  \"sources\": [\"https://www.etymonline.com/word/control\"],\n  \"ref_check\": [\n    {\"ref\": \"AHD\", \"status\": \"partial\",\n     \"note\": \"Watkins 1985 s.v. ret-: '2. Suffixed o-grade form *rot-a- in Latin rota, wheel: ... ROTUND, (ROTUNDA) ...' — Watkins spells the derivative ROTUND (< rotundus) and gives 'wheel' only as the gloss of rota.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"IEW 866\", \"stance\": \"contradicts\",\n     \"note\": \"'Latin rota \\\"wheel\\\", birotus \\\"zweirädrig\\\" (: Lithuanian dviratis), rotundus \\\"scheibenrund\\\"' — the form is rotundus and the gloss 'disc-round'.\"},\n    {\"src\": \"KLN\", \"where\": \"Klein 1966 s.vv. rota, rotund (KLN_1966.txt lines 33157, 33178)\", \"stance\": \"contradicts\",\n     \"note\": \"'rotund, adj., round, rounded. — L. rotundus, \\\"round\\\", fr. rota, \\\"wheel\\\".' Klein also lists under rota the whole English family: 'redondilla, rodeo, rondeau, rondel, rondo, rondure, Rotala, rotate, rotula, rotund, roue, rouelle, roulette, rounce, round ... and the second element in barouche and control'.\"},\n    {\"src\": \"SYN\", \"where\": \"Buck 10.76 and 12.81 (SYN.txt lines 18315, 23118)\", \"stance\": \"contradicts\",\n     \"note\": \"'Lat. rota' under WHEEL, and 'cf. Lat. rotundus \\\"round\\\" (12.81)' under ROUND — rotundus belongs to the 'round' entry, not the 'wheel' one.\"},\n    {\"src\": \"LEW\", \"where\": \"Walde 1910, index 'rota I 294' (LEW_1910.txt line 520)\", \"stance\": \"supports\",\n     \"note\": \"Walde's Latin etymological dictionary treats rota at I 294 (2nd ed. pagination), with the same IE connections; Nourai's LEW:904 refers to the 3rd ed., not available here.\"}\n  ]\n})\n\nN.append({\n  \"id\": 11, \"lang\": \"French\",\n  \"words\": \"\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"A pass-through box with no words printed (the header 'French' and the reference AHD are there, the content line is empty). It stands for the Old/Middle French stage through which Latin rota and its derivatives reached English: Latin rotundus > Old French roont/reont > French rond (English round); Latin rotula 'little wheel' > Vulgar Latin *rotulare > Old French roller/rouler (English roll) and the diminutive roulette 'little wheel' (18th c. gambling game); Medieval Latin contrarotulus 'counter-roll' > Old French contre-rolle, verb contreroller (English control). Klein sets out the same chain s.v. roll: 'ME. rollen, fr. OF. roller, roler, rouler (F. rouler), fr. VL. *rotulare, fr. L. rotula, \\\"a little wheel\\\", dimin. of rota'.\",\n  \"derivation_fa\": \"این خانه گذرگاهی است و در چاپ هیچ واژه‌ای در آن نیامده (تنها سرواژهٔ «French» و ارجاع AHD چاپ شده است). مقصود، مرحلهٔ فرانسهٔ کهن و میانه است که واژه‌های لاتینیِ این ریشه از راه آن به انگلیسی رسیده‌اند: rotundus لاتین ← roont/reont فرانسهٔ کهن ← rond («round» انگلیسی)؛ rotula «چرخک» ← *rotulare لاتین عامیانه ← roller/rouler فرانسهٔ کهن («roll») و مصغّر roulette «چرخ کوچک» (نام بازی قمار از سدهٔ هجدهم)؛ و contrarotulus لاتین میانه («دفتر مقابله») ← contre-rolle و فعل contreroller («control»). کلاین نیز همین زنجیره را ذیل roll آورده است. پس ادعای نورایی درست است.\",\n  \"sources\": [\"https://www.etymonline.com/word/control\"],\n  \"ref_check\": [\n    {\"ref\": \"AHD\", \"status\": \"supports\",\n     \"note\": \"Watkins 1985 s.v. ret- routes ROLL, ROULETTE, ROUND, CONTROL and BAROUCHE through Latin rota, i.e. through French, exactly as this box represents.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. roll (KLN_1966.txt line 33055)\", \"stance\": \"supports\",\n     \"note\": \"'roll, intr. and tr. v. — ME. rollen, rolen, fr. OF. roller, roler, rouler (F. rouler), fr. VL. *rotulare, fr. L. rotula, \\\"a little wheel\\\", dimin. of rota. See rota and cp. ... role, control, enroll, roulade, rouleau, roulette ...'\"},\n    {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict. s.v. roll, round, control\", \"stance\": \"supports\",\n     \"note\": \"Skeat routes all three through Old French from Latin rota/rotulus, the standard account.\"}\n  ]\n})\n\nN.append({\n  \"id\": 12, \"lang\": \"Persian\",\n  \"words\": \"رولت ، کنترل\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"Two modern French loans in Persian, correctly placed under the French box: کنترل kontrol from French contrôle (itself Old French contre-rolle < Medieval Latin contrarotulus, dim. rotulus of rota) and رولت rulet from French roulette 'little wheel; the gambling game' (< Old French roelete, dim. of roele < Late Latin rotella, dim. of rota). Both entered Persian in the Qajar-to-Pahlavi period (later 19th-early 20th c.) through French technical and administrative vocabulary, the usual channel for European loans in Persian; Farhang-e Moʿin marks کنترل explicitly '[فر.]' = French: «کنترل (کُ تُ رُ) [فر.] (اِ.) جستجو، تفتیش». The Persian forms keep the French pronunciation (final -ol, -et) rather than the English one, which confirms the route.\",\n  \"derivation_fa\": \"دو وام‌واژهٔ فرانسویِ امروزی که درست زیر خانهٔ فرانسه نشسته‌اند: «کنترل» از contrôle فرانسوی (خود از contre-rolle فرانسهٔ کهن و contrarotulus لاتین میانه، مصغّرِ rota) و «رولت» از roulette فرانسوی «چرخک؛ نام بازی قمار» (از rotella لاتین پسین، مصغّر rota). هر دو در دورهٔ قاجار تا پهلوی و از مجرای واژگان فنی و اداری فرانسوی وارد فارسی شده‌اند — همان مجرای همیشگی وام‌واژه‌های اروپایی در فارسی. فرهنگ معین «کنترل» را با نشانهٔ [فر.] یعنی فرانسوی ثبت کرده است: «کنترل (کُ تُ رُ) [فر.] (اِ.) جستجو، تفتیش». تلفظ فارسی (پایانهٔ ـل و ـت به شیوهٔ فرانسوی، نه انگلیسی) نیز همین مسیر را تأیید می‌کند.\",\n  \"sources\": [\"https://abadis.ir/fatofa/%DA%A9%D9%86%D8%AA%D8%B1%D9%84/\", \"https://www.etymonline.com/word/control\"],\n  \"ref_check\": [\n    {\"ref\": \"MON\", \"status\": \"supports\",\n     \"note\": \"Farhang-e Moʿin s.v. کنترل: «(کُ تُ رُ) [ فر. ] (اِ.) جستجو، تفتیش» — the [فر.] tag is Moʿin's own mark for a French loan (read at abadis.ir, archived).\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"MON\", \"where\": \"Farhang-e Moʿin via abadis.ir\", \"stance\": \"supports\", \"note\": \"as above; Moʿin registers the word as French.\"},\n    {\"src\": \"KLN\", \"where\": \"Klein s.v. control, roulette (KLN_1966 lines 33055, 33157)\", \"stance\": \"supports\",\n     \"note\": \"Klein derives control from OF. contrerolle and roulette from F. roulette, dim. of OF. roele, fr. L. rotella, dim. of rota — the French forms that Persian borrowed.\"}\n  ]\n})\n\nN.append({\n  \"id\": 13, \"lang\": \"English\",\n  \"words\": \"round, roll, roulette, control\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"All four are French-mediated reflexes of Latin rota, and Watkins lists all four under ret-. round: Middle English round(e), from Old French roont, reont (French rond) < Latin rotundus 'round' (13th c.). roll: Middle English rollen < Old French roller/rouler < Vulgar Latin *rotulare < Latin rotula 'little wheel'. roulette: borrowed from French roulette in the 18th c., first of a small wheel-shaped tool, then of the casino game (1745 in English). control: early 15th c. Anglo-French contreroller 'to check the accuracy of, verify', from Medieval Latin contrarotulus 'a counter-register', contra + rotulus (dim. of rota) — from the medieval accounting practice of keeping a duplicate roll. Nourai's placement of these four under 'French' rather than direct from Latin is correct.\",\n  \"derivation_fa\": \"هر چهار واژه از راه فرانسوی به انگلیسی رسیده‌اند و واتکینز نیز هر چهار را ذیل ریشهٔ ret- آورده است. round: از roont/reont فرانسهٔ کهن، از rotundus لاتین (سدهٔ سیزدهم میلادی). roll: از roller/rouler فرانسهٔ کهن، از *rotulare لاتین عامیانه، از rotula «چرخک». roulette: وام‌گیری مستقیم از roulette فرانسوی در سدهٔ هجدهم، نخست به معنی ابزار چرخ‌مانند و سپس نام بازی قمار (۱۷۴۵ در انگلیسی). control: از contreroller در انگلیسی‌ـ‌نورمن سدهٔ پانزدهم به معنی «بازبینی و راستی‌آزمایی»، از contrarotulus لاتین میانه («دفتر مقابله»: contra + rotulus، مصغّر rota) که به رسم حسابداری قرون وسطا بازمی‌گردد. جای‌دادن این چهار واژه زیر خانهٔ «فرانسه» — نه مستقیم از لاتین — درست است.\",\n  \"sources\": [\"https://www.etymonline.com/word/control\"],\n  \"ref_check\": [\n    {\"ref\": \"AHD\", \"status\": \"supports\",\n     \"note\": \"Watkins 1985 s.v. ret-: '... in Latin rota, wheel: RODEO, ROLL, ROTA, ROTARY, ROTATE, ROTUND, (ROTUNDA), ROULETTE, ROUND, ROWEL; BAROUCHE, CONTROL ...' — all four words of this box are in the list.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"Klein 1966 s.vv. roll, rota (lines 33055, 33157)\", \"stance\": \"supports\",\n     \"note\": \"'fr. VL. *rotulare, fr. L. rotula ... Cp. also role, control, enroll, roulade, rouleau, roulette' and, s.v. rota, 'Cp. also ... rotund, roue, rouelle, roulette, rounce, round, adj. ... and the second element in barouche and control'.\"},\n    {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls New Standard Dictionary s.vv. control, roulette\", \"stance\": \"supports\",\n     \"note\": \"the same OF contre-rolle / F. roulette routes; consulted as a second English dictionary alongside Klein.\"},\n    {\"src\": \"SKT\", \"where\": \"Skeat s.vv. round, roll, control\", \"stance\": \"supports\",\n     \"note\": \"Skeat likewise takes all three from Old French, ultimately from Latin rota/rotundus/rotulus.\"}\n  ]\n})\n\nN.append({\n  \"id\": 14, \"lang\": \"English\",\n  \"words\": \"rotate, rotary\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"These two, by contrast with node 13, are learned borrowings taken straight from Latin, which is why Nourai hangs them on the Latin box and not on the French one: rotate (1794 as a verb, earlier rotated 1610s) from Latin rotatus, past participle of rotāre 'to turn, revolve', denominative of rota; rotary (1731) from Medieval Latin rotarius 'pertaining to wheels', likewise from rota. Watkins lists ROTARY and ROTATE among the English descendants of *rot-a- < ret-, and Klein gives 'rotate ... fr. L. rotatus, pp. of rotare, fr. rota'. The arrow Latin -> English is therefore right, and so is the implicit contrast with the French-mediated set above.\",\n  \"derivation_fa\": \"این دو واژه برخلاف خانهٔ پیشین، وام‌واژه‌های عالمانه‌اند که یکراست از لاتین گرفته شده‌اند — و به همین سبب نورایی آن‌ها را نه زیر «فرانسه» بلکه زیر «لاتین» نشانده است: rotate از rotatus لاتین، صفت مفعولی rotāre «چرخیدن، چرخاندن» (فعل ساخته‌شده از rota)، که از سدهٔ هفدهم/هجدهم در انگلیسی به کار رفته؛ و rotary (۱۷۳۱) از rotarius لاتین میانه «وابسته به چرخ». واتکینز هر دو را در فهرست بازماندگان *rot-eh₂ ذیل ret- آورده و کلاین نیز می‌نویسد «rotate ... از rotatus، صفت مفعولی rotare، از rota». پس پیکان «لاتین ← انگلیسی» درست است و تمایز آن با مسیر فرانسوی نیز بجاست.\",\n  \"sources\": [\"https://www.etymonline.com/word/control\"],\n  \"ref_check\": [\n    {\"ref\": \"AHD\", \"status\": \"supports\",\n     \"note\": \"Watkins 1985 s.v. ret- lists ROTARY and ROTATE (and the index line 'ROTARY ret- ROTATE ret-' in the English-to-root index, AHD_watkins1985.txt line 2199).\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. rota/rotate (KLN_1966.txt line 33157)\", \"stance\": \"supports\",\n     \"note\": \"the rota entry explicitly cross-references 'rotate, rotula, rotund' as its Latin-derived English family.\"},\n    {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century Dictionary s.vv. rotate, rotary\", \"stance\": \"supports\",\n     \"note\": \"'L. rotatus, pp. of rotare, to turn round, fr. rota, a wheel' and 'LL. rotarius' — the same direct-from-Latin route.\"}\n  ]\n})\n\ndoc = {\n  \"pdf_page\": 422,\n  \"book_page\": 392,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-13\",\n  \"entries\": [entry]\n}\n\nwith io.open('/home/sfmqrb/git/rishe/data/verification/page-422.json','w',encoding='utf-8') as f:\n    json.dump(doc, f, ensure_ascii=False, indent=2)\n    f.write('\\n')\nprint('ok')\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-422.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-422.json > /dev/null && echo JSON_OK && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 422",
 "description": "Write and check page-422 verification"
}
```


### [2026-09-14T01:41:52.504Z] TOOL RESULT

```
ok
JSON_OK
nodes verified: 14/14
node verdicts: {'disputed': 3, 'confirmed': 8, 'plausible': 1, 'unverified': 1, 'transcription_suspect': 1}
root verdicts: {'confirmed': 1}
ref checks: {'partial': 6, 'not_checked': 3, 'supports': 12, 'contradicts': 1, 'not_found': 1}
books consulted: {'partial': 7, 'contradicts': 7, 'supports': 20, 'silent': 7} | by book: {'KLN': 7, 'PHD': 5, 'PLA': 3, 'BQT': 3, 'MON': 3, 'BRT': 2, 'CHEUNG': 2, 'POK': 2, 'SKT': 2, 'LKT': 1, 'HUB': 1, 'NYB': 1, 'HRN': 1, 'FVQ': 1, 'AFM': 1, 'TLM': 1, 'BOOK': 1, 'SYN': 1, 'LEW': 1, 'FSD': 1, 'WEB': 1}
```


## [2026-09-14T01:42:00.717Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SKT round/roll/control ===\"; grep -n -i 'Round (1)\\|ROUND, circular\\|control, \\|Roll, ' SKT.txt | head -8\necho \"=== WEB rotate ===\"; grep -n 'rotare, to turn\\|rotatus' WEB_vol1.txt | head -5\necho \"=== FSD control ===\"; grep -n 'contrerolle\\|contre-rolle\\|contrarotul' FSD_vol1.txt FSD_vol2.txt FSD_vol3.txt FSD_vol4.txt | head -5",
 "description": "Verify Skeat/Webster/Funk quotes"
}
```


### [2026-09-14T01:42:00.851Z] TOOL RESULT

```
=== SKT round/roll/control ===
6857:|»%Biit    led.  fg'^    Dn.  Jfyt*. G.0iam.     O.  U  fimmm,  » .)    Anierf  to  Flov. fffftwiatny.  ft  tretbootec  (SipM.«E.— >   Spas.  jfiKliudcr,  a  aoe  imjuytiaa  flf .^ue^MCer.*  Dm.  mySmUtr,  •  fiwtiiiBfcr. >!>•.  vriftmittm,  to    roll,   yliMiiu.— Da.
11222:matriculate,  to  enrol    in    a (L)    From   pp.  of  Low  L. to  enrol,  a  coined  word.«>L. roister  t  dimin.  of  matrix  (sttn meaning  (i)  a  breeding  oftitnal,  (j) matrix,  (5I  a  public  re^kler,  roll, parent-stock.    See  laalrix  (.belowV
14289:deploy,  to  open  out,  exii F.  tifpioyer^  to  unroll,   unfold ; ploitr,  to  unfold.  — L.  i/w-,  a| to  fold.
16218:control,  i.b.  (F.-U)  r<  ■ for  contre-roil,  old  form  of G.  F.  contre-role^  a  duplicate  iK\^-^--~i,  • to  verify  the  official  or  first-made  roll O.  F.  contra,  over  against ;  ro/e,  a  rol L.  eoptfm.  against;  ntulmSt  a  roll; roll  (below).
16219:roll,   vb.   (F.  -  L.)     M.  E.  rpOm. O- F.  roler,  F.   rou^r.  —  I.ow   l>  r\ to  revolve,  roll.  — L.  rotuia,  a  littb dimin.   of  rota,  a   wheel.     Der.  rtOf O.  F.  roU,  L.  rotuttu.
17211:Shroud.    (E.)      A.S.    KttU, clothing.  4*  tcel  skraH^,  ornament, of  a  ship;  Dan.  and  SwtO.  jkn^J, atlirc.     Orig.  a  'shred  '  of  stuff,  a or  torn  off;  cf.  G.  ukrvt,  a  cut.  a| schroiat,  to  cut,  saw ;  Goth.  diJ-tAr\ Icirtoshreds:  AS. /crA;(//(  ■-raO'l.E. scroll,  a  roll   of  paper.  \V.  * Dimin.  (with  sufTix  -/)  of  M.  E- scroll.  -  O.  F.  tscroue,  'a  scrowle,* O.  Du.    iihrccde,  a  shred,    fclrip«  slip pai'cr;  allied  to  ahroud  (al>OTr>.
18700:strlplinfiT*  (£•)    A  double  dlmin.  from ttrip;  hence  a   tad  as  thin  ai  a  strips  a growing  lad  not  yet  filled  out. Strive ;  ».«  Stride. Stroke,  (I )  and  (a)  ;  see  Strike. Stroll,   to  wander.    (Scand.)     Formerly ttrauU.  strvyU.     (A  contracted  form,  as  if lot ttrugU*.)  Ftcquetitatjveof Dan.^/fT-^, to  stroll.  Swed.   stryla,  to  stroke,  also  to ramble.  Allied  to  StrUce:  c£  M.  E.jtn'Js£m, to  go,  proceed,  waiidcr.
19647:trill  (3),  to  turn  round  and  round. (Scand.)  Perhaps  obsolete.  M.  E.  trilUn, Chaucer.  C.  T.  10630. -Swed.  /nV/o,  Dan. trilU,  to  roll,  turn  round  ;  the  tame  as Dn.  driUen ;  see  drill  ( i )  above.
=== WEB rotate ===
=== FSD control ===
FSD_vol1.txt:78645:II.  «.  To  form  designs;  plot.  (<  F.  conirouter ,   < con-  (   <   L.  cum),  with,  -f-  trouzer,  find,  <   L.  turbo,  move, find,  <   turba,  crowd.]  con-treve'f;  con-trove't.—  con- trlv'a-bl(ep,  a.—  con-trlre'mentt,  n.—  con-triv'er,  n. con-trlre'2t»  rt.  To  consume;  spend;  wear  away, con-trol',  1   ken-trol';  2   cdn-trol',  rt.  [con-trolled', con^trold'3;  con-trol'ling.]  1.  To  exercise  a   direct- ing, restraining,  or  governing  influence  over;  direct; counteract;  regulate;  as,  to  control  the  engine  of  a   motor- boat  by  a   lever.  2.  To  check  by  a   duplicate  register; verify  or  rectify,  as  an  account.  [   <   F.  contrdler,  regis- ter, <   contrdle;  see  control,  n.J  Synj  see  check;  gov- ern; influence;  subdue. —   con-trol'llng‘bit'%  n.  A band  of  rawhide  attached  to  rein -rings  and  used  as  a   bit. — controlllng.nozle,  n.  A   nozle  with  a   device  to  control  the size  of  its  stream.—  to  control  the  point,  to  beat  down  the point  In  fencing  so  as  to  gain  the  advantage.—  con-troHa- bl  (ep,  a.— con-troI'Ta-bll'I-ty,  con-trona-b!  (e-nessp,  n. Con-trol%  n.  1.  The  act  of  controlling;  guidance.  2. Regulating  power;  restraining  or  directing  influence; check;  regulation.  3.  Spiritualism.  The  intelligence (whatever  its  nature)  which  regulates  the  communi- cation of  messages  through  a   medium  or  psychic.  4. Auto.  In  racing,  __  any  one  of  certain  reservations  at which  the  contesting  machines  are  halted  for  overhaul- ing and  repairs.  5 .   A   mechanical  device  for  the  control of  an  airplane,  motor-car,  dirigible  balloon  or  the  like. C.  Meteorol.  An  element,  as  atmospheric  pressure, physical  features,  altitude,  exposure,  air-  or  ocean- currents,  vegetation,  etc.,  serving  as  a   determinant  of climate.  7.  A   double  account  or  counter-register.  [   <   F. controls.  <   LL.  contrarotulum,  counter-roll.  <   L.  contra  (see contra-)  4*  LL.  TCtulus.  roll.  ult.  <   L-  rota,  wheel. I   eon- trole't;  con-tronl't-— Enij  see  ascendency:  dominion; influence.  — con- trol' -clock",  n.  In  clocks  operated electrically,  one  that  regulates  and  Imparts  the  time  to  all other  clocks  In  the  system.—  c.*experiment,  n.  An  ex- periment made  on  two  objects  of  the  same  kind,  as  upon two  rabbits,  or  two  compounds  In  chemistry,  one  of  which serves  as  a   standard  of  comparison  for  or  as  a   corroborator of  the  other.  c.«test*.  —   c. •pillar,  n.  Auto.  The  post which  supports  the  steering-wheel,  etc.— tandem  or  con- catenation c.  (Elec.),  the  motor-control  obtained  by  a cascade  connection.  See  connection. con-trol 'ler,  1   kan-trol'er;  2   con-trQl'er,  n.  1.  An  of- ficer who  is  appointed  by  a   state,  city,  corporation,  or the  like,  to  examine  and  verify  Its  accounts  by  compar- ison with  a   counter-roll  or  register  of  accounts,  comp- trol  TferJ.  2.  One  who  or  that  which  controls,  regulates, or  directs.  _   3.  [Gt.  Brit.]  Navy.  One  of  the  admi- ralty commissioners  who  is  mainly  responsible  for  naval construction  and  equipment:  officially  called  the  Third Naval  Lord  and  Controller.  4.  Naut.  A   cast 'iron block  with  depressions  in  its  upper  surface,  usually
FSD_vol1.txt:78648:bolted  to  the  forward  deck,  to  check  the  running  out of  a   chain  cable.  5.  Elec.  A   magnet  used  in  automatic regulation  of  a   current.  It  is  usually  so  arranged  as  to throw  the  regulator  magnet  out  of  the  main  circuit when  the  current-strength  changes.  See  illus.  under electric.  6.  Auto.  The  lever  which  controls  the throttle-valve  on  a   gasoline  machine.  See  motor  car. 7.  Originally,  one  who  kept  the  counter-rolls  or  check* accounts.  [   <   F.  contrdleur ,   <   LL,  contrarotulator, counter-roll  keeper,  <   contrarotulum ;   see  control,  n.J  — con-troner*gen'er-al,  n.  An  official  appointed  to  a somewhat  widely  extended  administrative  control,  as  over '   finances.— C.  of  the  Currency  [U.  S.1,  a   government  offi- cial having  supervision  of  the  national  banks.—  master  c., In  a   multiple-unit  system  of  electric  railroading,  the  singte Instrument  which  regulates  the  controllers  of  the  several cars  on  the  system.—  con-troHer-shlp,  n.  The  office  of or  the  state  of  being  a   controller,  comp-troner-shipt. con-trol'ment,  1   ken-trdl'ment  or  -mont;  2   con-trol'- 1   ment,  n.  1.  The  act  of  controlling,  or  the  state  of  be- ing controlled.  2f.  Opposition;  resistance. con"tro-vers'alt,  a.  1.  Facing  or  turned  In  opposite  direc- tions. 2.  Controversial.
```


## [2026-09-14T01:42:09.176Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i 'rotate,' WEB_vol1.txt | head -3\necho \"---\"; grep -c '' WEB_vol1.txt; grep -n -i 'rota,' WEB_vol1.txt | head -3\necho \"=== FSD rotate ===\"; grep -n 'ro\"ta-ry\\|ro-tate\\|rotare' FSD_vol3.txt FSD_vol4.txt | head -5",
 "description": "Check Webster and FSD for rotate"
}
```


### [2026-09-14T01:42:09.325Z] TOOL RESULT

```
33908:cir-cum-29’ra-t6-ry, a. moving in a circular manner, _ cir-cum-gyre’, v.i. to roll or turn round; to circumgyrate. [Obs.]} cir’cum-in-ces/sion, n. [circum-, and L. in- cessus, a going, walking, from incedere, to ad- vance, to walk.] in theology, the existence of persons in one another. 4 cir-cum-in/sii-lar, a. surrounding or around an island; in anatomy, around the insula of _the cerebral cortex. cir-cum-ja’cence, n. the state of bordering on every side, or of being circumjacent. cir-cum.ja’cent, a. [L. circumjacens, ppr. of circumjacere;, circum, and jacere, to lie.| lying round; bordering on every side. cir-cum-jo/vi-Al, n. one of Jupiter’s satellites or moons, cir-cum.-jo/vi-Aal, a. around Jupiter. cir’cum.1li-ga’/tion, n. [L. circumligare; cir- cum, and ligare, to tie, bind.] the act of bind- ing round; also, the bond with which any- thing is surrounded. [Obs.] cir-cum-lit/t6-ral, a. [circum-, and L. litus, litoris, shore.] adjacent to the shore. cir’cum-16-cii’tion, n. [L. circumlocutio, cir- cumlocution; circum, and locutio, a speaking, from loqui, to speak.] the use of a number of words to express an idea; an indirect or lengthy way of expressing something; also, an instance of this. cir’cum-16-cii’tion-4l, a. pertaining to cir- cumlocution. cir-cum-loc/i-t6-ry, a. pertaining to or char- acterized by circumlocution. cir’cum-mé-rid/i-an, a. [circum-, and L, me- ridies, midday.] about, or in close proximity to, the meridian. cir-cum-mire’, v.t. [circum-, and L. murus, wall.] to surround with a wall. cir-cum-nay/i-ga-ble, a. that may be sailed around. cir-cum-nav/i-gate, v.l.; circumnavigated, pt., pp.; circumnavigating, ppr. to sail around; to pass around by water; as, to circumnavigate the globe. cir-cum-nav-i-ga’tion, n. the act of sailing around. cir-cum-nav/i-g4-t6r, n. one who circumnav- igates. cir-cum-ni/tate, v.i. to exhibit circumnuta- tion. cir’cum-nii-ta/tion, n. [circum-, and L. nu- lare, to nod.} the act or inclination of the stems, roots, or shoots of plants to bend in various directions because of differences in the rate of growth of the opposite sides. cir-cum-oc/i-lar, a. around or near the eye. cir-cum-6/ral, a. [circum-, and L. os, genit. oris, mouth.| being situated near, or encir- cling, the mouth. cir’cum-pli-ca’tion, 2. [L. circumplicare; cir- cum, and plicare, to fold.] a folding, winding, or wrapping round. cir-cum-po/lar, a. about the pole: said of stars which are so near either pole as to revolve around it without setting; as, circumpolar stars; circumpolar sea. See cir’cum-po'si’tion, n. the act of placing in a circle, or the state of being so placed. 3 cir-cum-r0’ta-ry, a. turning, rolling, or whirl- ing around. y ; cir-cum-ro’tate, v.t. and v.t.; circumrotated, pt., pp.; circumrotating, ppr. to revolve; to rotate, as on an axis. z cīr’cum-rō-tā’tion, n. the act of rolling or revolving around, as a wheel; circumvolution. cir-cum-r0/ta-t6-ry, e. same as circumrotary. cir-cum:scis/sile, a. [circum-, and L. scissilis, easily cut, from sctssus, pp. of scindere, to cut.] in bot- any, opening or splitting by a transverse fissure aroun the circumference, leaving an upper and lower half: said of certain seed pods or capsules. cir-cum-scrib/a-ble, a. capa- ble of being circumscribed. cir-cum-scribe’, v.t.; circum- scribed, pl.. pp.; circum- scribing, ppr. (ME. circum- scrive; L. circumscribere, to draw a line around.] 1. to draw a line around. RS: 2. to enclose within a certain limit; to limit, bound, or confine. 3. to write around. [Rare.] 4. in geometry, (a) to draw a figure around (another figure) so as to touch it at as many points as possible; as, circumscribe a
---
114685
16142:ba-réuche’, n. [Gr. barutsche; It. baroccto, from LL. birota, a two-wheeled vehicle, from L. bis, two, and rota, a wheel.] a four-wheeled car- riage having a collapsible top, with a driver's seat on the outside and two inside seats facing each other,
28602:1. the edible, orange-red root of the Daucus carota, a plant of the celery family.
66119:&.qui-ro/tal, a. [equi-, and L., rota, a wheel.) having wheels of the same size or diameter, as a machine. {Rare.]
=== FSD rotate ===
```


## [2026-09-14T01:42:30.588Z] TOOL CALL #81: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 - <<'EOF'\nimport json,io\np='data/verification/page-422.json'\nd=json.load(open(p,encoding='utf-8'))\nnodes={n['id']:n for n in d['entries'][0]['nodes']}\n\n# node 11 SKT\nfor c in nodes[11]['consulted']:\n    if c['src']=='SKT':\n        c['where']=\"Skeat, Concise Etym. Dict. s.vv. control, roll (SKT.txt lines 16218-16219)\"\n        c['note']=\"'control, sb. (F.-L.) ... for contre-roll, old form of O.F. contre-role, a duplicate register ... O.F. contra, over against; role, a roll ... L. contra, against; rotulus, a roll' and 'roll, vb. (F.-L.) M.E. rollen ... O.F. roler, F. rouler. - Low L. rotulare, to revolve, roll. - L. rotula, a little [wheel], dimin. of rota, a wheel.'\"\nfor c in nodes[13]['consulted']:\n    if c['src']=='SKT':\n        c['where']=\"Skeat s.vv. control, roll (SKT.txt lines 16218-16219)\"\n        c['note']=\"'control ... for contre-roll, old form of O.F. contre-role, a duplicate register ... L. contra, against; rotulus, a roll'; 'roll, vb. ... O.F. roler, F. rouler. - Low L. rotulare ... L. rotula, dimin. of rota, a wheel.' (Skeat's own spelling of the OF forms.)\"\n    if c['src']=='FSD':\n        c['where']=\"Funk & Wagnalls New Standard Dict. vol.1 s.v. control (FSD_vol1.txt line 78645)\"\n        c['note']=\"'control, n. ... 7. A double account or counter-register. [< F. controle, < LL. contrarotulum, counter-roll, < L. contra (see contra-) + LL. rotulus, roll, ult. < L. rota, wheel]' — and s.v. controller: '< F. controleur, < LL. contrarotulator, counter-roll keeper'.\"\nfor c in nodes[14]['consulted']:\n    if c['src']=='WEB':\n        c['where']=\"Webster's New Twentieth Century Dict., vol.1 (A-...) s.v. barouche (WEB_vol1.txt line 16142)\"\n        c['stance']=\"partial\"\n        c['note']=\"the volume on disk stops before R, so it has no 'rotate' entry; it does document the same Latin word elsewhere, e.g. 'barouche ... It. baroccio, from LL. birota, a two-wheeled vehicle, from L. bis, two, and rota, a wheel' — one of the words Watkins likewise lists under ret-.\"\njson.dump(d, io.open(p,'w',encoding='utf-8'), ensure_ascii=False, indent=2)\nio.open(p,'a',encoding='utf-8').write('\\n')\nprint('patched')\nEOF\npython3 -m json.tool data/verification/page-422.json >/dev/null && python3 tools/verify_check.py 422",
 "description": "Patch consulted quotes and re-check"
}
```


### [2026-09-14T01:42:31.876Z] TOOL RESULT

```
patched
nodes verified: 14/14
node verdicts: {'disputed': 3, 'confirmed': 8, 'plausible': 1, 'unverified': 1, 'transcription_suspect': 1}
root verdicts: {'confirmed': 1}
ref checks: {'partial': 6, 'not_checked': 3, 'supports': 12, 'contradicts': 1, 'not_found': 1}
books consulted: {'partial': 8, 'contradicts': 7, 'supports': 19, 'silent': 7} | by book: {'KLN': 7, 'PHD': 5, 'PLA': 3, 'BQT': 3, 'MON': 3, 'BRT': 2, 'CHEUNG': 2, 'POK': 2, 'SKT': 2, 'LKT': 1, 'HUB': 1, 'NYB': 1, 'HRN': 1, 'FVQ': 1, 'AFM': 1, 'TLM': 1, 'BOOK': 1, 'SYN': 1, 'LEW': 1, 'FSD': 1, 'WEB': 1}
```


## [2026-09-14T01:42:39.775Z] TOOL CALL #82: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"FVQ:\"; grep -c -i 'ruhban\\|rahib\\|رهبان\\|راهب' FVQ.txt FVQ_pages.txt\necho \"KLN:\"; grep -c -i 'rahib\\|ruhban' KLN_1966.txt\necho \"KLN turraha:\"; grep -c -i 'turraha' KLN_1966.txt\necho \"IEC ret:\"; grep -c -i \"^ret-\\|^rotos\" IEC.txt",
 "description": "Confirm the silent greps"
}
```


### [2026-09-14T01:42:39.892Z] TOOL RESULT

```
FVQ:
FVQ_pages.txt:0
FVQ.txt:0
KLN:
0
KLN turraha:
0
IEC ret:
3
```


## [2026-09-14T01:42:42.166Z] TOOL CALL #83: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"^ret-\\|^rotos\" IEC.txt | head",
 "description": "Check IEC ret- headword"
}
```


### [2026-09-14T01:42:42.237Z] TOOL RESULT

```
14535:ret- (1) ‘run, roll, go”. Cf. rit- Umb. cf. amb-retuto ‘let them walk around’; (Gallo-Lat. petor-ritum is from a variant, *quetuor-, rit-); MIr. rethim, v. ‘run’; OBr. cf. *retic (misspelt retteticc), adj. ‘running’; Br. rédek, pp: rédet, v. ‘run’; W rhedeg, rhedu, inf. id.; Cor. resek *rezek', 3s: res, v. id.
14536:ret- (2) “space, interstice, openwork, net, sieve; open, spacious'. See next Oss. cf. rätän, s. ‘wicker of birch-branches'; OHG (ambig.) rédan, v. ‘sift; Li. rētas, adj. ‘tare, scant’: retéju, eti, v. ‘get rarified'; Latv. rets, adj. “open, rare, scant'; reteju, v. as Li.
14614:rotos, à, is (rátos, à, is) (2) (reasoning, cal- culation’. Cf. reios (reis). Skt. phonology ano- malous. Cf. rətos (1) (with hybridism?). Vari- ant rêt- Skt. cf. ratüh, f. ‘true speech’; rtih, f. “memory” (here?); Lat. ratus, adj. (1) ‘suppositional, authentic’; ratið, f. ‘reason, respect, cause, purpose, means, conditions, account, busi- ness; Go. raþjo, pl. -ons, f. (reckoning, num- ber’: Lat. ratio); OHG redia, f. ‘speech’; OS rethia, f. ‘discourse, account’; ON cf. (*-à-) ræða, f. ‘speech’; v. ‘speak’; OCS rotü, m., rota, f. ‘oath’; po-rota, f. (jury', and com. SI.); Srb. cf. ropp se, v. ‘conspire’. The variant *ret- arises in Skt. ràtih, f. “favour, gift; OS rad, m. (advice, gain’, and com. Gmc.) (*re- tós). The Celtic evidence is ambiguous (cf. protos), viz. Ir. rath, m. “fortune, success, re- ward’; OBr. rat, s. ‘grace, favour; W rhad, pl. -au, m. id.; Cor. ras, plur. -ow, m. id.
```


## [2026-09-14T01:42:49.480Z] TOOL CALL #84: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 - <<'EOF'\nimport json,io\np='data/verification/page-422.json'\nd=json.load(open(p,encoding='utf-8'))\ne=d['entries'][0]\nfor c in e['consulted']:\n    if c['src']=='IEC':\n        c['where']=\"Mann, IE Comparative Dictionary s.v. ret- (1) (IEC.txt line 14535)\"\n        c['stance']=\"supports\"\n        c['note']=\"'ret- (1) \\\"run, roll, go\\\". Cf. rit-. Umb. amb-retuto \\\"let them walk around\\\"; (Gallo-Lat. petor-ritum is from a variant *quetuor-, rit-); MIr. rethim, v. \\\"run\\\"; Br. redek, W rhedeg \\\"run\\\"' — Mann's gloss is Nourai's gloss exactly, though his material is Italic and Celtic only.\"\njson.dump(d, io.open(p,'w',encoding='utf-8'), ensure_ascii=False, indent=2)\nio.open(p,'a',encoding='utf-8').write('\\n')\nEOF\npython3 -m json.tool data/verification/page-422.json >/dev/null && python3 tools/verify_check.py 422",
 "description": "Fix Mann entry and recheck"
}
```


### [2026-09-14T01:42:50.906Z] TOOL RESULT

```
nodes verified: 14/14
node verdicts: {'disputed': 3, 'confirmed': 8, 'plausible': 1, 'unverified': 1, 'transcription_suspect': 1}
root verdicts: {'confirmed': 1}
ref checks: {'partial': 6, 'not_checked': 3, 'supports': 12, 'contradicts': 1, 'not_found': 1}
books consulted: {'partial': 8, 'contradicts': 7, 'supports': 19, 'silent': 7} | by book: {'KLN': 7, 'PHD': 5, 'PLA': 3, 'BQT': 3, 'MON': 3, 'BRT': 2, 'CHEUNG': 2, 'POK': 2, 'SKT': 2, 'LKT': 1, 'HUB': 1, 'NYB': 1, 'HRN': 1, 'FVQ': 1, 'AFM': 1, 'TLM': 1, 'BOOK': 1, 'SYN': 1, 'LEW': 1, 'FSD': 1, 'WEB': 1}
```


## [2026-09-14T01:43:12.697Z] AGENT

Page 422 (book p. 392, root **Ret**, one entry, 14 nodes) is verified; `verify_check.py 422` shows 14/14 nodes and 0 PROBLEM lines.

**Verdicts** — root: confirmed. Nodes: 8 confirmed, 1 plausible, 3 disputed, 1 transcription_suspect, 1 unverified (the blank box).

**Disputed / flagged**
- **#1 Avestan "rad 2 : to run"** — no such Avestan verb. Bartholomae's only `rad-` (AiW 1505) is *Old Persian*, only with `ava-` "to leave, deviate"; Cheung's Av. `raδ-` is "to pave/dig" (PIE *HreHsd-, Pok. 854). `ratha` and `ratha-eštra` in the same box are confirmed.
- **#2 Persian `laškar`** — Cheung p.195: NP laškar < PIr *Hraxša-kara- ("protecting host", root of Skt. rakṣ-), not from raθaēštar-. Mo'in's own footnote at the cited BQT:1895 reports Purdavud's raθaēštar > *laštar > laškar and calls the last step "بعید". (`arteštâr` confirmed via BQT:97 + MacKenzie; `arrâdeh` only plausible — Asbaghi p.8 does compare ap./aw. raθa-, but mainstream takes ارّاده/عرّاده as Arabic.)
- **#5 Persian `râheb`** — Arabic رَاهِب is the participle of رَهِبَ "to fear" (root r-h-b); Persian borrowed it back. Nourai's rāh-bān source is Asbaghi p.133 (his own cited page) plus Borhan's folk etymology — a minority/folk view. rahbar, rāygān, rāhbān are fine.
- **#10 Latin "ret-undus : wheel"** — transcription_suspect, `error_in: "book"`: the printed page really does read `ret-undus : wheel`; correct is **rotundus "round"**. Page image saved to `data/verification/sources/refs/ocr/BOOK/422.png`.

**No extraction errors found** — the JSON is faithful to the page everywhere, including the empty French box (#11) and the entirely blank box #9 hanging off Old Persian.

**Notable reference findings**: BQT:97 = «ارتشدار» with Mo'in's Avestan raθaēštār footnote (leaf 307, ends "بقیه در صفحهٔ ۹۸"); BQT:1895 fetched and cached as `refs/ocr/BQT/1895.png`; BQT:934 = Mo'in's note «راک قرائتی است از "راس" پهلوی (بمعنی راه)»; HUB:66 (§607) supports rās > *rāθ > rāh verbatim; **FFD:56 is a mis-citation** — Abolqasemi's p.56 is the verb رَستن/رَه "to escape" (< OP raθ- "leave"), not راه, a homonym Hübschmann explicitly excludes; TAD:17 not_found (TAD's Arabic OCR has no ترهات anywhere), but node 6 is independently confirmed by Lisān al-ʿArab ("الطرق الصغار… فارسي معرب") and Asbaghi p.88. Eleven web pages archived via `fetch_source.py`.
