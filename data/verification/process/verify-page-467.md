# Verification process log — verify-page-467


## [2026-09-14T02:27:50.897Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 467 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-467.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-467.json. Write /home/sfmqrb/git/rishe/data/verification/page-467.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 467` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T02:27:52.024Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T02:27:52.808Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T02:27:52.824Z] TOOL RESULT

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


## [2026-09-14T02:27:53.311Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-467.txt"
}
```


### [2026-09-14T02:27:53.338Z] TOOL RESULT

```
1	=== PDF page 467 (book page 437) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Spelgh, Sphelghen : spleen  (refs POK:987)
4	#1 (parent #0) [Avestan] refs=POK:987; KLN:1492 | sperezan : spleen
5	  #2 (parent #1) [Persian] refs=HRN:155; MON:1827 | seporz «سپرز» : spleen
6	#3 (parent #0) [Sanskrit] refs=SNS:176 | splîhân : spleen
7	#4 (parent #0) [Greek] refs=AHD | splĕn : spleen
8	  #5 (parent #4) [English] refs=None | spleen
9	--- entry 1 ---
10	ROOT [Indo-European] Spen, Pen, Poin; Pend : twist; turn, spin  (refs IEC:971; POK:988)
11	#1 (parent #0) [Persian] refs=IEC:971; MON:970 | pîneh «پینه» : patch of cloth, calluses
12	#2 (parent #0) [Germanic] refs=AHD:1542 | spinnan : to spin ; spithra : spinner, spider ; spin-ilôn : spindle ; spannjan : to bind, span
13	  #3 (parent #2) [English] refs=AHD | spin ; spider ; spindle ; span
14	#4 (parent #0) [Latin] refs=AHD:1542 | pendĕre : to hang
15	  #5 (parent #4) [English] refs=AHD | pendant ; pension ; append ; compensate ; depend ; expend ; perpendicular ; suspend ; pendulum
16	#6 (parent #0) [Latin] refs=AHD:1542 | pondô : by weight
17	  #7 (parent #6) [English] refs=AHD | pound
18	--- entry 2 ---
19	ROOT [Indo-European] Sper, Qusĕros, Kĕros : sparrow  (refs POK:997; IEC:613,1056)
20	#1 (parent #0) [Pahlavi] refs=MON:1789 | sâr : sparrow
21	  #2 (parent #1) [Persian] refs=IEC:613,1056; MON:1789 | sâr «سار ۳» : sparrow | extra: سارک،ساری، سارچ، سارجه
22	#3 (parent #0) [Sanskrit] refs=IEC:1056 | čârah : sparrow
23	#4 (parent #0) [Germanic] refs=AHD:1542 | sparwan : sparrow
24	  #5 (parent #4) [English] refs=AHD | sparrow
25	#6 (parent #0) [Greek] refs=IEC:613,1056 | psâros, psĕr : starling
26	
```


## [2026-09-14T02:27:56.354Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-467.json",
 "description": "Read source JSON for page 467"
}
```


### [2026-09-14T02:27:56.417Z] TOOL RESULT

```
{
  "pdf_page": 467,
  "book_page": 437,
  "entries": [
    {
      "root": {
        "name": "Spelgh, Sphelghen",
        "lang": "Indo-European",
        "refs": "POK:987",
        "gloss": "spleen"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:987; KLN:1492",
          "words": [
            {"translit": "sperezan", "gloss": "spleen", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "HRN:155; MON:1827",
          "words": [
            {"translit": "seporz", "gloss": "spleen", "script": "سپرز"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "SNS:176",
          "words": [
            {"translit": "splîhân", "gloss": "spleen", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD",
          "words": [
            {"translit": "splĕn", "gloss": "spleen", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "spleen", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Spen, Pen, Poin; Pend",
        "lang": "Indo-European",
        "refs": "IEC:971; POK:988",
        "gloss": "twist; turn, spin"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "IEC:971; MON:970",
          "words": [
            {"translit": "pîneh", "gloss": "patch of cloth, calluses", "script": "پینه"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "بر زبان ذکر و خاتمش بیمین - سبحه در دست و پینه بار جبین",
            "poet": "Dehkhodâ"
          }
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD:1542",
          "words": [
            {"translit": "spinnan", "gloss": "to spin", "script": null},
            {"translit": "spithra", "gloss": "spinner, spider", "script": null},
            {"translit": "spin-ilôn", "gloss": "spindle", "script": null},
            {"translit": "spannjan", "gloss": "to bind, span", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "spin", "gloss": null, "script": null},
            {"translit": "spider", "gloss": null, "script": null},
            {"translit": "spindle", "gloss": null, "script": null},
            {"translit": "span", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD:1542",
          "words": [
            {"translit": "pendĕre", "gloss": "to hang", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "pendant", "gloss": null, "script": null},
            {"translit": "pension", "gloss": null, "script": null},
            {"translit": "append", "gloss": null, "script": null},
            {"translit": "compensate", "gloss": null, "script": null},
            {"translit": "depend", "gloss": null, "script": null},
            {"translit": "expend", "gloss": null, "script": null},
            {"translit": "perpendicular", "gloss": null, "script": null},
            {"translit": "suspend", "gloss": null, "script": null},
            {"translit": "pendulum", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD:1542",
          "words": [
            {"translit": "pondô", "gloss": "by weight", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "pound", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Sper, Qusĕros, Kĕros",
        "lang": "Indo-European",
        "refs": "POK:997; IEC:613,1056",
        "gloss": "sparrow"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Pahlavi",
          "refs": "MON:1789",
          "words": [
            {"translit": "sâr", "gloss": "sparrow", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "IEC:613,1056; MON:1789",
          "words": [
            {"translit": "sâr", "gloss": "sparrow", "script": "سار ۳"}
          ],
          "script_extra": "سارک،ساری، سارچ، سارجه",
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "IEC:1056",
          "words": [
            {"translit": "čârah", "gloss": "sparrow", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD:1542",
          "words": [
            {"translit": "sparwan", "gloss": "sparrow", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "sparrow", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Greek",
          "refs": "IEC:613,1056",
          "words": [
            {"translit": "psâros, psĕr", "gloss": "starling", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
```


## [2026-09-14T02:27:57.103Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-14T02:27:57.158Z] TOOL RESULT

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


## [2026-09-14T02:28:01.873Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','IEC','AHD','KLN','HRN','MON','SNS','BQT','PHD','NYB','BRT','HUB','WLD','SYN','SKT','ARY','LEW','LAT','FSD','WEB']:\n    v=d.get(k)\n    if v: print(k, json.dumps(v, ensure_ascii=False)[:600]); print('---')\n\""
}
```


### [2026-09-14T02:28:02.966Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_
---
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 
---
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,
---
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h
---
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 
---
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په
---
SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt
---
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118
---
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-
---
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf
---
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1
---
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol
---
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039
---
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves
---
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves
---
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 
---
LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt", "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f b
---
LAT {"title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951", "edition_found": "1951 (3rd ed.) - matches Nourai", "kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "identifier": "ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine (4th ed. 1959 lending-only: dictionnairetymo0000unse; another open copy: DictionnaireEtymologiqueDeLaLangueLatine)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt", "page_offset": "leaf = printed + 18 for mos
---
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt
---
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/W
---
```


## [2026-09-14T02:28:06.272Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','IEC','AHD','KLN','SNS','MON','HRN','BRT']:\n    v=d[k]\n    print(k,'OFFSET:',v.get('page_offset'))\n    print(k,'HINT:',v.get('lookup_hint'))\n    print(k,'LOCAL:',v.get('local_file'))\n    print('===')\n\""
}
```


### [2026-09-14T02:28:07.455Z] TOOL RESULT

```
POK OFFSET: POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
POK HINT: Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\data\ie\pokorny&root=config
POK LOCAL: /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt
===
IEC OFFSET: TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
IEC HINT: Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.
IEC LOCAL: /home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt
===
AHD OFFSET: 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.
AHD HINT: Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves = original 1969 ed.).
AHD LOCAL: /home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt
===
KLN OFFSET: KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
KLN HINT: Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
KLN LOCAL: /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt
===
SNS OFFSET: 242 leaves; page offset not determined (OCR too poor to read printed numbers) — locate by transliteration then read the page image
SNS HINT: grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.
SNS LOCAL: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt']
===
MON OFFSET: None
MON HINT: Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks).
MON LOCAL: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt']
===
HRN OFFSET: leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
HRN HINT: Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.
HRN LOCAL: /home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt
===
BRT OFFSET: Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
BRT HINT: Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special transliteration is noisy - grep on a distinctive Latin gloss or the German meaning in quotes. Column numbers appear as standalone numbers at leaf tops.
BRT LOCAL: /home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt
===
```


## [2026-09-14T02:28:11.692Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"lemma: sp\" POK_full.txt | head -60"
}
```


### [2026-09-14T02:28:11.747Z] TOOL RESULT

```
79425:Root / lemma: spako- 
79439:Root / lemma: speg- 
79459:Root / lemma: speR- 
79518:Root / lemma: spend- 
79594:Root / lemma: speno- steno- p(a)steno- 
79629:Root / lemma: spergh-, spregh-, nasalized sprengh- 
79685:Root / lemma: sper-2(g-) 
79718:Root / lemma: sper-3 
79749:Root / lemma: sp(h)ei. sp(h)iav\6 sp(h)e. sp(h)a-2 
79821:Root / lemma: sp(h)elgh(en, -a), splengh-, splegh- 
79962:Root / lemma: sp(h)e(n)d- 
79985:Root / lemma: sp(h)eng- 
79993:Root/ lemma: sp(h)eng-\ to shine derived from Root/ lemma: *(s)p(h)ereg-, (s)p(h)erag-, 
80030:Root / lemma: sp(h)erd(h)-, (s)p(h)red(h)-, nasalized sp(h)rend(h)- 
80040:Root / lemma: sp(h)erd(h)-, (s)p(h)red(h)-, nasalized sp(h)rend(h)-\ to rush; to spring; 
80093:Root / lemma: sp(h)er-1, sp(h)era- 
80107:Root/ lemma: sp(h)er-1, sp(h)era-\ to make a rash movement, to push away, to rush, 
80290:Root / lemma: sp(h)er-3 
80420:Root / lemma: sp(h)e(i)-3, 5/7A-and sphe-. spha- 
80523:Root / lemma: sp(h)e-, sp(h)a-(<S^-) 
80594:Root / lemma: sp(h)reig- 
80727:Root / lemma: sprei- spreu-
```


## [2026-09-14T02:28:12.826Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"splегh\\|spelgh\\|splenghā\\|spelg\" POK_full.txt | head -30; echo ====; grep -n -i \"Milz\" POK_full.txt | head -30"
}
```


### [2026-09-14T02:28:12.910Z] TOOL RESULT

```
Exit code 1
(eval):2: === not found
```


## [2026-09-14T02:28:14.518Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '79821,79965p' POK_full.txt"
}
```


### [2026-09-14T02:28:14.586Z] TOOL RESULT

```
Root / lemma: sp(h)elgh(en, -a), splengh-, splegh- 

Meaning: spleen 

Note: taboo deformed 

Material: Old \r\d'\c p/Ihan-, Avestan sparazan-m., Armenian p'aicain, gr. airAnv (*aTTAr|YX, 

compare onAayxva Nom. PI. ' intestines, entrails '), Latin lien. Old Irish selgi.. Middle 

Breton felc'h. Old Church Slavic slezena. 

Maybe from Avestan spardzan 6en\/e6 alb. {*spelatan) shpretna ' sp\een' . 
References: WP. II 680, WH. I 789, Trautmann 256, Vasmer 2, 605, Turner BSOAS 18, 
451; different Specht, Die old Sprachen 5, 120. 
Page(s): 987 

Root / lemma: (s)p(h)el-1 



Meaning: to split, cut off, tear off; board 

Material: Old Indie sphafaf/ {Dhatup.) 'reiftt, springt auf, S/0/75///5-"gesprungen, zerfetzt', 
sp/7a///r5-'Bergkristair ('sich blattrig abspaltend'), *sphafayaf/ ^spWts', covered das 
participle sphatita-, sphutat/ ^spWts sich, springt auf, platzt, reiftt' (sek. sphotati); besides 
diesen /- present (: Old High German spaltan) das /c»-participle S/0/7^/5-'aufgebluht, open ' 
(: Gothic spilda); Old Indie /05/5//"splits sich, cracks', patayati^ sp\\\.s, breaks, rips' (: patu- 
"sharp', gr. nAaruc; ' salty '? s. under *pltu-s)\ 

yO/75/5//" cracks, springt divided ', phalakam ^ {*c\oyev\ wood) board, lath, leaf, shield, 
Holzbank', phala-xx\. ' plowshare ' ('zugespitztes AststiJck'?); Old pers. Glosse anapa- 
papai oi Ysppocpopoi Hes. 'schildtragend', npers. ispar, s/psA'shield' (Old Indie /0/7a/'a/77, 
spharam^s\\\e\6\ uncovered, probably from dem Iran, and in aniaut afteryC>/7a/a/r5/77 
directed); 

gr. ocpaAaaasiv tsijvsiv, ksvtsTv Hes., ocpaAa^ 'Stechdorn', oanaAaGoc; m. ds. ("*whereof 
man sich reiftt, scarifies '), ocpaAa^, aacpaAa^, anaAa^, aanaAa^ ' mole ' ('die Erde 
aufreiftend'), anaAuaasTai anapaaasTai, TapaaasTai Hes., aanaAov gkutoc; Hes., 
onaAauGpov "SchiJreisen'; anoAia ra napariAAotJSva spiSia ano tu)v oksAwv tu)v 
npopQTCjov Hes. (: Latin spolium), Attic anoAac; 'abgezogenes fell, fur' and "Uberwurf from 
Leder, breastplate, mantle', Aeolic anaAic;, Attic HJaAic; 'scissors'; to acpaAaaasiv also 
GcpaAoc; TuftblockforGefangene; Wurfscheibe' and ocpaAAu) 'throw (originally with 
'Prijgeln'), toss, fling, bump, poke' and '(at first beim Ringen) ein leg place, in fight, 
struggle hinder', from which 'bring to collapse, injure, hurt, deceive, cheat, deceive', Med. 
'waver, fall, sich irren', aa(paAr|(; 'unerschijtterlich, ohne sich fortstoften to let' - ' peaceful, 
certainly', ocpaAspoc; ' slippery ', ocpaAjja 'falscher footstep '; acpsAac; 'wooden log, club, 
cudgel; ausgehohlter block, bench '; 

from Alb. perhaps yoa/e'side, party ' ( *polna, compare Old Church Slavic pol-b 'side, 
bank, border, shore, gender, sex, half); yOOyoe/e'FelsstiJck, plaice', plis {*pli-tio-) 'clod of 
earth', plish^ reed ' {*pli-sio-)\ 

Latin spc»//^/77 'abgezogene orabgelegte Tierhaut; dem Feinde abgenommene RiJstung, 
booty'; 

with /-Erweit.: Old High German spaltan. Middle Low German spalden 'split', Gothic 
spilda {* spelta) 'Schreibtafel', Old Icelandic spjald {*speltos) 'board'. Old English speld 
'splint; bit of wood'. Middle High German spelte' cleaved bit of wood, Handgerat the 
Weberei'; Old Icelandic spjall, speZ/'damage' {*spell=>a-, -/■), Old English splld, splld' 
annihilation. Ruin', whereof Old Icelandic spllla, spella'spoW, slay' {* spell=>jan, *spell=>dn). 



Old Saxon spildian, Old English spMan' destroy', Old High German spildan, spilden 
"waste, spread', Old Saxon spildT generous '; Germanic /in Middle Low German spelte^ 
cloven piece'. East Frisian spa/terds., Germanic *spe/td {out of it Latin spelta) in Old High 
German spe/za Vulgar Latin spe/ta {irom which:) " spelt '; engl. spe/fer'Z\nk' {* spaldiz-); 
Old English Syoa/o'^/'' Balsam' {*spalduz- " effluence from cloven plant '); />present Old 
EnglishSyC»///a/7, Middle High German SyO///e/7 'split' {*spelljan), wherefore without s- Swedish 
^a7/"Schinnen in Haar'; Old Icelandic spglr^t\\\v\ flache shaft, pole'. Middle English spale 
ds.. Middle High German spale^ rung, horizontal step on a ladder'; probably (as "thin, flat 
bit of wood') Old High German spuolom., isl. 5/0o/e"Weberschiffchen', Norwegian spole 
"coil, spool' (Germanic *spdlan-)\ Old High German S/O^o/5 (Germanic *spdldn-) 'coil, 
spool', "duct, tube, pipe, quill '; without ani. s-\ Old Icelandic ^ip/"board' {*pela); 

with /-Erweit., but without s- probably Irish alta(i)n, cymr. ellyn, acymr. elinn' shearing 
knife ', abret. altln<^\. ' ferula ', Middle Breton autenn, nbret. aotenn' shearing knife ' 
{*paltlnS); mcymr. allaw'shave' {*alta-mu-); J. Loth RC. 45, 173. 

Lithuanian spalls, PI. spallal, Latvian 5pa//"Flachsschaben'; Latvian S/05/s "handle, hold, 
grasp'; Old Prussian 5pe/a/7A'//5 "splinter'; 

Old Church Slavic ras-platltr spWt' {*poltltl, compare Modern High German spalten. Old 
Indie sphatati), platb'^dKoc,, scrap, shred', poleno'p'\ece of wood wood', /OC»//ic5 "board', 
palica. Old Russian paltka'stScV!, russ. ras-polotb "entzweischneiden', polotb, poltb 
"(abgeschnittene) Speckseite', poltlna'haW, Old Church Slavic po/b. Gen. -^"half, side, 
bank, border, shore, gender, sex'; Old Bulgarian plevg, pletl {russ. polotb) " weed ', plevelb 
"weed'; *o-pelnb\r\ Czech opien, c»/0///7"Gipfstock, Rungenstock', sloven, opien 
"Wagengipfenholz' etc.; 

with dem i/from plevg {* peluo) is zusammenzuhalten: Latvian spalva' feather, 
Gefieder, hair', 5/0/7i/5"husk, Samenwolle, Wollgras', SyO//i/^/7s'Bettkissen' etc.; 

Tocharian A spaltk-, B spalk-^s\cV\ anstrengen'; 

References: WP. II 677 ff., WH. II 571 f., 577 f., Trautmann 204, Vasmer 2, 398, Flasdieck 

Zink under Zinn, 1 57 ff. 

See also: with {s)p{h)el- "split' hang possibly together: pel-'sk\r\, fell, fur', S/oe/g- "split', 

sp/e/- "split', yo/e/- "naked, bald, bleak', piek- plelk- ' rend ', pleu{s-, -k-) "ausrupfen', plas- 

"abspalten'. 

Page(s): 985-987 



Root / lemma: (s)p(h)el-2 

Meaning: to shine, shimmer 

Material: Old Indie sphulirjga-m. 'spark' (Erweiter. eines *sphuli= Armenian p'ail, Indo 

Germanic *spheli-), vi-sphulirjga-^s., vi-spulirjgaka-^ sparking, producing sparks'; 

Armenian p'ail. Gen. p'ailic' radiance, shimmer ', yC>'5//e/77 "gleam, shimmer'; p'alp'aHm, 

p 'oip 'oiim 'gleams'. 

fltextension sp(h)el-g-, nasalized (s)p(h)leng-: 

Latvian spulguof <^\q2xx\, sparkle, glitter', spulgis'\he Funkelnde = the morning star', 
spulgans, spilgans' shimmering, gleaming'; nasalized Germanic *flinka-' shimmering, 
also from rascher Bewegung' in Low German (Modern High German) /7//7/r'rash, hasty, 
quick, fast', flinkern' <^\QdX(\, shimmer'. Middle High German kupfervlinke'Kw^iererz', 
changing through ablaut (perhaps secondary) Modern High German /7i//7/re/77 'flicker; 
einem etwas vormachen', and perhaps Latvian planga, plunga, p/e/T^a 'blister'. 

o^extension, nasalized (s)plend-, (s)pland-: 

Gr. anAr|56q m. (anAr|5u) f. Hes.) 'ash'; Latin splendeo, -e/"© 'gleam, shimmer'. Old 
Lithuanian splendziu, sp/endet/ "g\ear(\, shine'; perhaps also Old Irish /ess {* /anssu- kom 
*pland-tu-) 'light'; Middle Irish /a//7/7ec/7 'gleaming' {*plandjakd). (common Celtic -/7S-, -nt- > 
-nn-). 

References: WP. II 679 f., WH. II 576 f. 
Page(s): 987 

Root / lemma: sp(h)e(n)d- 
Meaning: to shiver, to shake 

Material: Old Indie spandate' shrugs, jerks, hits, knocks from', spanda- m. ' twitch,
```


## [2026-09-14T02:28:42.265Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK lemma pen/spen 988 ===\"; grep -n \"lemma: (s)pen\\|lemma: spen\\|lemma: pen-\" POK_full.txt | head -20\necho \"=== POK sper sparrow ===\"; sed -n '79685,79760p' POK_full.txt"
}
```


### [2026-09-14T02:28:42.335Z] TOOL RESULT

```
=== POK lemma pen/spen 988 ===
66195:Root / lemma: pen-1 
66217:Root / lemma: pen-2, pen-ko- 
79518:Root / lemma: spend- 
79535:Root / lemma: (s)pen-l(d-) 
79594:Root / lemma: speno- steno- p(a)steno- 
=== POK sper sparrow ===
Root / lemma: sper-2(g-) 

Meaning: a kind of bird (sparrow?) 

Material: Gothic sparwa. Old English spearwa. Old High German spare ^ sparrow' (*proto 

Germanic *sparwan-); Middle High German sper//nc Moderr\ High Qerrr\ar\Sperling, 



diminutive; Old Icelandic spgrrds. from *sparwa-z, compare also Modern High German 
Sperber, Old High German sparwari{i\v\a\ ending after Old High German aro^ eagle ' 
transfigured?); 

gr. anapaaiov opvsov i\x(^z^ZQ, arpouGco Hes. (*anapF/7-//c»/77); the formant ^also (??) in 
gr. ijjap, Ionian ep. i^jrip (hom. Akk. PI. ii;r|pa(;), Gen. ijjap6(; 'Star' (originally *ijjapF-(;, 
Gen. *itjapF6(;?), newer i^jcipoq, i|japO(;, 4JC(po(; m. ds., iijap6(; "stargrau'; in addition 
probably Old Saxon spra, Dutch spreeuw. North Frisian SyO/7a/7, Middle Low German spren. 
Low German (Modern High German) sprehe^ Star'; 

corn, frau, bret. frao^crow' {*sprawa)\ daft Latin parra'e\n bird, dessen Geschrei 
UngliJckbedeutete', Umbrian parfam, parfa 'parram' {*parsa) an s- loose kinsman, relative 
sei, is quite dubious; 

Tocharian A sparan'e\n bird'; 

forms auf p: gr. PN iTTopyiAoq "sparrow', (a)TT£pyouAo(; 6pvi9apiov aypiov Hes.; Old 
High German sperk, sperch, SyO//r/7 'sparrow'. Old Prussian spergla-wana^is] 'Sperber' 
(actually 'Sperlingsgeier'), ablaut, spurglisvn. 'sparrow'. 

References: WP. II 666 f., WH. II 257, Trautmann 275. 
Page(s): 991 

Root / lemma: sper-3 

Meaning: to turn, wind 

Material: Gr. ansTpa f. ' convolution, Spirale, all Geflochtene (e.g. of net, rope, hawser)', 

GTTeipau) 'coil, wickle', onEipapa ' convolution, diaper '; o-napioo, m. 'ein shrub, bush, from 

dessen Ruten man Bander or Stricke flocht', anaprov, anaprri 'gedrehtes or geflochtenes 

rope, band'; anupi(; (Ionian a(pupi(;) 'geflochtener basket' (from dem Akk. anupiSa derives 

through etrusk. mediation Latin spo/Ya 'geflochtener basket'); 

Old Lithuanian spartas^bav\6, strap'; probably here Armenian p'arem, p'arim 
'umschliefte, umarme'. 

^-extension spereg- nasalized spreng- ' coil, umwickein, dadurch eng tie up ': 

Gr. anapyu) 'wickle ein', anapyavov ' diaper '; 

Lithuanian springstu, sprihgti' strangle, throttle, choke (Intr., beim Schlucken)', 
sprengetiAs., sprangus 'wurgend', Latvian sp/'a/7^^/'einschnuren'. 



References: WP. II 667 f., Trautmann 279. 
Page(s): 991-992 



Root / lemma: sp(h)ei. sp(h)iav\6 sp(h)e. sp(h)a-2 
Meaning: to pull, drag 

Material: Gr. anaw, and) ( *spa-sd) 'pull, zerre, verrenke, falle with Zuckungen, Krampfen 
an, pull ein, suck ein'; a(paK£Ao(; m. 'Zuckung, cramp'; anaapoq m. "Ziehen, Zuckung, 
cramp', anaa|ja n. ds. "rag, scrap, shred'; arra-S- e.g. in napaauaq, -OT\a,boc,i. 
"Pflanzenabsenker', arraSi^ "abgerissenerZweig', anaScbv m. " twitch, cramp, ana5u)v "the 
castrator', Ionian anaSi^w "pull ab, reifte ab (5£ppa)', argiv. ana5iov "araSiov' ("in die 
Lange gezogen'); das sonstige araSiov " racecourse ', probably through support in aTa5iO(; 
"stehend'; arraTOc; n. "skin' ("*Abgezogenes'); 

partly auf a present *spa-n63iX\6 spa-nuo based on probably die Germanic family Old
```


## [2026-09-14T02:28:44.391Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== IEC 971 area ===\"; grep -n \"^spen-\\|^spend-\\|^spenu\\|^pend-\\|^poin\" IEC.txt | head -20\necho \"=== IEC kseros/keros ===\"; grep -n \"^k.eros\\|^keros\\|^ku.seros\\|sparrow\" IEC.txt | head -40"
}
```


### [2026-09-14T02:28:44.477Z] TOOL RESULT

```
=== IEC 971 area ===
13313:poin- (1) (phoin-) Skt. cf. phenah, m. ‘foam’; OCS (and com. Sl.) pěna, f. id.; Li. píenas m. ‘milk’; Latv. piens, m. id.
13314:poin- (2) “twist, turn’. Cf. pin-. WP II, 661 Skt. penami, v. “wander; embrace; Per. cf. pine ‘patch of cloth’; Arm. henum, hinem, v. ‘weave, twist, plait; MHG (?) vein, adj. com, pact; Li. painüs, adj. ‘tangled; complex; wrong"; painioti, inf. ‘twist, weave’ beside pai-
=== IEC kseros/keros ===
3317:Cast or ‘foggy; fog; Gaul. donnos ‘dun’; Mir & Ir. donn, id.; W dwn, id.; OE dunn, OS dun, id.; LG dun, fig. ‘drunk’; ON dunna ‘mallard’; Norw. dynn ‘mire’. Cf. the Eng. birdnames dunlin (a greyish marsh-bird) and dunnock 'hedge-sparrow?
4009:ging- (gingl-, gingr-) (1), whoop, cackle, whistle Arm. čnčay ‘whinchať beside čnčyuk (dim. type: 'sparrow; Skt. cf. -jinga- (a cpd. *-tongue-); Gk. cf. gigglismós (2) “laugh”, beside giggrás, Hes. gíggron ‘flute’; Lat. gingrio, ire ‘cackle’, beside (LW?) gingrina ‘flute’; OE cinc-ung ‘guffaw’; Du. cf. kink- hoest *whooping-cough'; E cf. to chink
5717:ĝid- ‘small creature. Cf. WP I, 527. See eidh-, dig- Arm. Cit, gs cti, i-st. ‘small sparrow, tit; Alb. dhí ‘goat’ (ambig. see 8idh-); MHG kiz, kitze ‘buck, kid?; G Kitz ‘fawn in first year’; Kitze *she-cat, kid, fawn’; EME chit (freckle; young person’. Cpds: chit-lark, chit-pease); E dial. chit “eye of potato’; cf. E kit (kitten, fr. Norse?); Du. cf. kittig ‘sprightiy’
6301:itius ‘newborn child, novice’; OCS plovic, pisící ‘swimmer; writer’. (As a dim. suffix, cf. Slovene volčič “young wolf; Cz. panic “lord- ling; Li. vilkytis, gs -čio, as Slovene) itm, adverbial particle. Cf. it (ito) Lat. item “also, likewise’; Li. itin ‘especially’ itós, pt. of root i- ‘go’, see ei-mi, etc. Skt. itáh; Gk. itós; Lat. itus ‘gone’. (Gk. also = *passable") itro, io (variant of enter, q.v.) (?). Cf. etor, nter- Gk. ítria, npl. “abdomen; OBr. cf. hr *be- tween, among’; ON iór & iðrar, pl. ‘entrails’ Iuos ‘osprey, kite, buzzard, sparrow-hawk'.
6315:(onomat. NB: the cry of the osprey resembles iw) Alb. iv ‘buzzard or sparrowhawk’; OE giw ‘vulture’; Li. yvas “brown owl?
7671:korguos (variant of krguos, q.v.) fa raucous bird". Cf. WP I, 413 Per. kalay ‘crow’; Lat. (ambig.) corvus, id.; Blg. cf. krag-uj 'sparrow-hawk'; Cz. krah-ujec, id.
7770:kräeg, ið ‘caw, croak’. See next Gk. krázo, pf. kekraga, id.; Lat. pro-crago, ere, pf. -cràxi 'shout'; OE cf. hrace, hracu ‘throat, gorge’: MHG rache, wm. d: Sw. cf. rackla, v. ‘cough up, hawk’; Slovene cf. kro- guljiti ‘ring’; Cz. cf. krahuj, krahujec 'sparrow- hawk
7781:“a corvine bird"; cf. rackeln, v. ‘caw’; Pol. cf. krogulec *sparrow-hawKk ; Li. krágas ‘coot, dab- chick'. Long-grade in MHG ruoch, Du. roek, OE hroc ‘rook’; OCS kraguj 'sparrow-hawk
8165:kseros (2) (quseros ?) “sharp, harsh'. (Same as (1)? The alternative initial is suggested by Gk. psorós (rough?) Skt. khárah, kharuh 'rough, harsh'; Oss. cf. áxsálí ‘Juniper’; Tokh. A tsår, B Scire trough, hard’; R cf. Sero-xovatyj ‘rough, rugged’; Ukr. Sory, pl. ‘barbs’. Long-gde in R o-šaràšiť ‘dumbfound’
9294:words: ‘whistle, bird-cry; bird with shrill cry’, etc. W variant quil- W cf. pila, pl. pilaon ‘finch’ beside pilan, pl. -od, f. 'sparrow-hawk'; Li. Svilys, m., Latv. svilis (1) ((redcap' or sim. bird). Extended forms include OE hwilpe, f. (‘curlew or *plover?); Du. wulp, Fris. wylp (‘curlew’, also ‘whelp’; cf. also Li. Svilpis, io, m. ‘whistle sound”, Évilpti, v. ‘whistle’. Cf. Kulp-. Long- gde in Slovene, with variant initial cviliti ‘whimper’ '
9297:Kuingor- Arm. (with assimilated consonants) čnčay ‘whinchat’ beside čnčyuk, dim. type (‘hedge sparrow? or sim.); Alb. cínxull, cínxérr, m. f. tit; Nor. cf. kvinke, v. ‘chirp, wail’; kvinke, kvinkelere “pipe, flute’; kvinkre, v. “twitter” (Norw. kv- for hv- in *landsmál). Radical in Alb. cíngem, v. ‘whine’. See next
12324:oros, ios Coros) ‘eagle, hawk. Cf. orneu-, ornis. WP I, 135 Oss. wári ‘hawk’; Arm. ori, gs: orvo, ab. s. oreav ‘sparrow-hawk’; Hitt. haras, gs: haranas *eagle'; Gk. óros (4) ‘kind of eagle beside cpds. ór-neon, ór-peton (unidentified bird- names); Lat. cf. vult-ur, gs: -uris, m. vulture’,
16925:sprieZu, spriest, v. “stretch — linen’; Sw. cf. sprint, m. “bolt, bar. (Isophone: MHG sprinze, wm. ‘splinter’; wf. ‘sparrow-hawk’; sprénzen, sv. 3. ‘be motley’)
19529:ug- (2), suffix-element in bird-names Gk. cf. órt-ux, gs: -ugos ‘quail’; Lat. cf. ves- per-ügo, gs: -üginis, f. (2) *bat'. Tertullian); Ir. cf. truide-og, druide-og beside (simplex) truid & druid, f. ‘starling’; W drud-wy, m. id.; OE cf. heaf-oc & haf-oc ‘hawk’; rudd-uc ro, bin"; E dunn-ock ('sparrow', but for OE tosoc,
19770:uarbh- (uarbhl-) “twitter, warble’. E warble, v.; warble-fly *bot-fly'; Skt. cf. var- vana (a fly), beside barbana, f. id.; OCS vra- bij, m. ‘sparrow’; R vorobéj, Blg. vràbej, vrà- bec, vrabaléc, m. id.; Cz. vrabec, id.; Pol. wróbel, m. id.; (zero-gde in) Hes. rháphos, m. (kind of bird); Li. virbe, f. ‘moorhen’. (The background of Alb. borboléc *bot-fly' is ob- scure)
```


## [2026-09-14T02:28:53.117Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK entries with Page(s) 997 ===\"; grep -n \"Page(s): 99[0-9]\" POK_full.txt | head -30"
}
```


### [2026-09-14T02:28:53.173Z] TOOL RESULT

```
=== POK entries with Page(s) 997 ===
43012:Page(s): 996-998 
79627:Page(s): 990 
79654:Page(s): 998 
79683:Page(s): 990-991 
79716:Page(s): 991 
79745:Page(s): 991-992 
80091:Page(s): 995-996 
80176:Page(s): 992-993 
80288:Page(s): 993-995 
80306:Page(s): 995 
80324:Page(s): 992 
80358:Page(s): 998-999 
80592:Page(s): 999-1000 
80631:Page(s): 999 
80651:Page(s): 999
```


## [2026-09-14T02:28:53.834Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== IEC starling ===\"; grep -n \"starling\" IEC.txt | head -30"
}
```


### [2026-09-14T02:28:53.892Z] TOOL RESULT

```
=== IEC starling ===
2456:dreutis (drutis) ʻa song-bird’ Arm. (ambig.) artiwt, artujt & artut, gs artuti (i-st. lark?); W drudwy ‘starling’; Ir. druid, id.
2507:drut- (drutis, drudis) (2), cf. dreutis, etc. and WP I, 761 Arm. artujt, gs artuti ‘lark is ambig.; Ir. druid ‘starling’; SW Ger. cf. Trose (thrush? or *greenfinch")
3892:gargəlos, à ‘babbling, raucous; babble, bubbling, gurgle, croak’. Onomat. Cf. WP I, . 538 & 683 Skt. gárgarah, gargarā; Per. yaryara ‘gurgle’; Gk. gárgalos (2), id.; Alb. gárgull ‘starling’; LLat. gargala ‘windpipe’; Li. gargalas, m. ‘hoarse speaker’; cf. garge “a water-fow?
8706:Keros (3) ‘dapple, marked with grey or black’. WP I, 360 & 420 Skt. Saráb ‘motley’; Per. sar ‘starling’; Gk. cf. kerülos “blue kingfisher’; Ir. ciar, MIr. cíar “dark, brown, black’; OCS sérü (and com. SI. *grey^); Li. cf. šeřkšnas ('greyish', from a type *Kersnos); Scots cf. haar (/sea-mist, from Norse?). Cf. OHG harinc, sm. ‘herring’
13726:püg- (pügom, ios) “lump, mass, crowd" Skt. pügam, n. ‘crowd’; R pyZ, m. “wad, wodge'. (Isophone: Fris. füke, Du. fuik ‘dragnet, bownet"); Fris. cf. fükje, v. ‘swarm as starlings’
14332:quséros (qusáros? Initial and vocalism pro- blematic) ‘motley’. Variant initial consonant- ism in Indo-Iranian. Cf. WP II, 666 Skt. cf. Caráh, Sàrab, id.; Per. sar, sarak, s. "star. ling’; Gk. psàrós, adj. ‘motley’; pser, gs: -ós, beside psar, m. ‘starling’; Alb. cf. shore ( rash, eruption’, but see quseros above); OCS Sarü, šara, mf. ‘colour’; Sar&jo se, v. “be variegated'; Srb. Sar, adj. ‘motley’; Blg. Sar, m. ‘dye’ be- side šaren, adj. ‘motley’. (The initial conso- nantism of Lat. varius, adj. ‘motley, change- able’ and vārī, mpl. ‘rash, pockmarks? is of uncertain background)
16900:` starling’ or sim. WP II, 666
16903:& Sprei, f. ‘starling’; Du. spreeuw, m. id. spraió (spráuio, sph-) ‘rush, gush’. WP II,
17300:stornos ‘starling’. WP II, 649 Lat. sturnus, gs: 3, m. id.; OE stearn, m. (a sea-bird). (WH untenable)
19132:trut- (5) “a song-bird'. (Arm. ambig., cf. drut-, etc.) Arm. cf. artujt, gs: artuti, Let ‘lark’; It. cf. trutilare, inf. ‘sing like a songbird’; Ir. cf. truideog, f. ‘starling’; truid, f. id.; Br. treidi, pl. treided, m. ‘starling’; W cf. trodwen, f. id.; Cor. tros, pl. tryjy, id.
19529:ug- (2), suffix-element in bird-names Gk. cf. órt-ux, gs: -ugos ‘quail’; Lat. cf. ves- per-ügo, gs: -üginis, f. (2) *bat'. Tertullian); Ir. cf. truide-og, druide-og beside (simplex) truid & druid, f. ‘starling’; W drud-wy, m. id.; OE cf. heaf-oc & haf-oc ‘hawk’; rudd-uc ro, bin"; E dunn-ock ('sparrow', but for OE tosoc,
```


## [2026-09-14T02:29:08.495Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '42960,43015p' POK_full.txt\necho \"=== IEC leaf numbers ===\"\npython3 - <<'EOF'\np='/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt'\nt=open(p,encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nfor target in (8706,14332,13314,8165):\n    pre='\\n'.join(lines[:target])\n    leaf=pre.count('\\f')\n    print(target,'leaf',leaf,'-> printed pp ~', (leaf-15)*2, (leaf-15)*2+1)\nEOF"
}
```


### [2026-09-14T02:29:09.961Z] TOOL RESULT

```
Lithuanian spuogas^ stain, dot, speck '; - without an!, s, and concomitant as variant 
besides *pertt-, *preR-^ dappled ' (see 820 f.): Old Icelandic freknottr^ freckly, freckled ', 
Norwegian and nisi, frekna^ freckle ', engl. freak^ make striped '; 

Old English spraecu. 'scion, shoot, twig, branch', sprancam. ds. (5p/7/7ce/' basket- 
snare'); in the meaning ' crackle, rustle, break, crack' based on Norwegian sprek' dry 
deadwood'. Old Icelandic sprek' rotten, decayed, decomposed; brittle wood'. Old High 
German sprahhu/a 'spWnter, chaff'. Middle Low German sprok, sprokke/'6ea6\NOod'; holl. 
sprokkig^ brittle ', sprokke/n^ break, crack', Norwegian dial, sproka, sprokka^ crack, 
spring, cleft, fissure'. Old English forspiercan^dry, dehydrate, desiccate'; mnl. sporkel 
February' (probably of bud sprout, compare engl. spring^ spring '), Low German sprickel 
"deadwood, dry twig, branch'; 

compare also Old English spracen^ alder ', Norwegian sprake^ juniper ', Old High 
German sporah, spurchaAs., also ('twitching, shooting up, elastic') Old High German 
houue-spranca locusia (grasshopper)'. Old Saxon sprinco ds., Middle Low German 
spranke, sprinke, sprenkel 6s.; Middle High German sprinke^ bird trap ', Low German 
Modern High German Sprenker S'pecV\e ' ds.; Low German sprenker clamp wood '; 

Old High German springa^ shackle, fetter, or chain for the feet, a springe, gin, snare ', 
older Modern High German SprengeF bird trap ', engl. springe, springle^ bird's loop ' are 
influenced by springen, 

Latvian spFrgC become fresh, strengthen ', spirg(t)s^^resh, alert, awake, smart, fit, 
healthy'; spirgsti {pirgsti) 'glowing coals under the ash'; sp/zy^/zs 'splinter' 
('*Weggesprj^tzb|s '); spridzinaV spray around, spring ', spridzfgs^ rash, hasty, alert, 
awake, smart'; spurguls^ srr\a\\, munteres child', spQrgans^ brittle, alert, awake, smart'; 
Lithuanian sprogis, Latvian spradzis^ Erdfloh '; 

D. without aniaut s- compare still: Old Indie parjanya-^ rain cloud (squirting, spraying); 
the rain God and thunderstorm God ' (see above S. 819, 823); Old Irish a/y'drip', mcymr. 
eiry, cymr. e/Za'snow', acorn, irch, ncorn. er, bret. erc'h6s. {*pargo-, *pargio-); common p- 
> zero Celtic Armenian. 



probably also Old Church Slavic prbga^ neuer Kornansatz des Weizens ', russ. perga' 
pollen ' ; Old Church Slavic /s-prbgngt/ ^spr'\r\g out', poln. p/erzgn^c^ break, crack (skin)'; 
nasalized Old Bulgarian vbs-prggngt/" sprout ', prggb ' locust, grasshopper '; as 'shooting 
up ' Old Church Slavic prgg/o ' a little snare, noose, a little stretcher ', russ. pruga, pruzina 
"jumping feather', u-prugij^ shooting up flexibly, bulging ', also the family proto Slavic 



*pr§gQ^ tighten, hitch, harness an animal; tense, pull taught, stretch tight ', prggh' yoke ', 
poln. popr^g^beW.' etc. 

Maybe alb. pranga " cuffs ' : Slavic prggh ' yoke '. 

References: WP. II 672 ff., WH. II 566 f., Trautmann 276 f., 278 f., Vasmer 2, 337, 450. 
Page(s): 996-998 

Root / lemma: *uep-1 : uop- : up- 
Meaning: water 
=== IEC leaf numbers ===
8706 leaf 347 -> printed pp ~ 664 665
14332 leaf 585 -> printed pp ~ 1140 1141
13314 leaf 539 -> printed pp ~ 1048 1049
8165 leaf 325 -> printed pp ~ 620 621
```


## [2026-09-14T02:29:21.993Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\np='IEC.txt'\nt=open(p,encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i in (346,347,348,584,585,586,538,539,540):\n    L=leaves[i]\n    print('--- leaf',i,'first 200:',repr(L[:200]))\n    print('    last 150:',repr(L[-150:]))\nEOF"
}
```


### [2026-09-14T02:29:23.229Z] TOOL RESULT

```
--- leaf 346 first 200: 'atera-, Gk. krétér, krátér (mixing bowl". LW in Lat. cràter, crà- tera); OHG hruorjan, OS hrorjan, OE hreran ‘stir, shake’; OE, OS hror “active, lively’, cf. E dial. a roosing fire (paroxytonic protot'
    last 150: ", scale’; Gk. kérkos “penis”; kerkis ‘peg, shuttle; Little tail\nKerm-os, -o(n) 'greyish-white; grey-white creature, stoat, ermine’. Cf. Kormo, and WP "
--- leaf 347 first 200: "I, 463 Alb. i thjermé ‘grey’; Li. Sermuó, gs -efis ('stoat. See Kormó(n); MHG cf. hermel-, cpds. 'ermine-' beside (o-gde) harm, harme, id.; Latv. cf. sermuls ‘weasel’\nKermn- (1) “timber, log? Ober, cf"
    last 150: "oruó ‘torment’ Skt. Sarvami “hurt, kil; MHG harewen 'exa- cerbate'; OHG *haro, MHG hare, gs harewes ‘harsh’; ME harwe, herwe ‘plunder’; E to har- row "
--- leaf 348 first 200: "(in sense of ‘torment’. Isophonic w. Sw. harva 'to harrow a field'. NB. the initial seems to be reflected in Alb. tharb, adj. ‘sour; m. “acid”; v. “make sour”, and in Umbrian queried cerf- “harsh, bit"
    last 150: 'ad, top, tip\'; Oss. sår ‘head, beginning"; Arm. sar, u-st. as Per.; Myc. cf. karuwe- (ffigureheads, corbels\' or sim. cf. Gk. karuátides); Gk. kár, n. '
--- leaf 584 first 200: 't. ‘desire’; MIr. saint, f. id.: W chwant, m. id.; Br. chwant, Cor. chwans, id.; OBr. cf. ar-uanta, adj. ‘very desirous’; Pol. chęć, f., Cz. chuť, f. id. Verbal derivative: Per. xandam, v. ‘laugh’; Ar'
    last 150: 'babble’; W chwil, adj. ‘whirling, reeling’; Br. chwil, m. (?) (“beetle”; but a phonol. background *suel- or *suil- is possible); OCS šaliti, inf. ‘rav'
--- leaf 585 first 200: 'e, rage’;\nquséió — quseudo, ið\n20\n25\n30\n35\n40\n45\n1056\nR 3al&t “get silly, grow confused”; cf. Salyj *playful and 3alíja, f. ‘wanton woman’; OCz. Sieliti, Cz. Sílit, Slovak aalt & Sale, v. ‘rave’; Slov'
    last 150: 'blast’; W chwyddo, inf. ‘swell’; chwydd, m. ‘swelling’. Variants implied in Skt. ksvid-, vb. root “hiss, whizz’ and in Ukr. švydkyj, adj. “swift? qusi'
--- leaf 586 first 200: 'ið (qusinið) “crush, destroy” Skt. ksinómi, ksinami, v. “destroy” beside ksih, f. ‘destruction’; Av. xSi-, id.; Gk. psío, v. ‘crush’. Extns. of this root are seen in Gk.\nquseudros (qusudros) — quso£os'
    last 150: 'bright, red? Av. xSaeto “bright; Per. Said (2), id. beside sed-, cpds. (“bay” of a horse); (LW in) Arm. ašxęt, adj. (“bay” of horse); Arm. xajt, i-st.'
--- leaf 538 first 200: 'nd com. Gmc.)\npnt- (pnts-) ‘go, track; passage, way’. Cf. pent-, pont-. WP II, 26 Skt. cf. patháh, gen.sg. of pánthah, m. ‘way’; Av. paða-, id.; Ober, paði- f. id.; Oss. cf. fätäg (Cleader" Here: Abae'
    last 150: ') Go. fotus, OHG fuos, OE fot, pl. fet, ON fótr, pl. fætr, m. d: OCS podü, m. “floor, storey”; Srb. ‘floor’; R ‘hearth, open-hearth"; Big. ‘stone floo'
--- leaf 539 first 200: "r, slab’ beside Cz. půda, f. “ground”; Li. pádas, m. ‘sole of foot’; pádis, gs: padio, m. ‘base’ (Li. pádas also “bottom, floor of hearth, threshing-floor' under infl. of Russian); Latv. pads, m. ‘cla"
    last 150: " ‘grass, fodder, grazing, meadow’. WP II, 74 Gk. poíe, poía, póe, f. ‘meadow grass’; Li. pieva, f. ‘meadow of mowing-grass'\npoios (poiios), -es- ‘drin"
--- leaf 540 first 200: 'king; drink’. Cf pt-, etc. Skt. páyas, n. “fluid, sap, juice, milk’ beside peyah, adj. & s. ‘drinkable; drink’; payam, pt. (while drinking: (radical of) OCS na-paj-ati, v. ‘give to drink’); Av. payo, '
    last 150: "HG in) LLat. velcho, MHG velche, G Fel- chen (*whitefish' or sim.); Li. pal$as, palša, mf. ‘bream’\npolKos, à (2) ‘fallow’. See above, and WP I, 516 Ga"
```


## [2026-09-14T02:29:29.451Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i in (346,347,348,538,539,540,584,585):\n    L=leaves[i]\n    nums=re.findall(r'\\n(\\d{3,4})\\n', L)\n    print(i, nums[:10])\nEOF"
}
```


### [2026-09-14T02:29:30.540Z] TOOL RESULT

```
346 ['611', '612']
347 ['613', '614']
348 ['615', '616']
538 ['969', '970']
539 ['971', '972']
540 ['973']
584 ['1055']
585 ['1056', '1057']
```


## [2026-09-14T02:29:41.733Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '79535,79600p' POK_full.txt"
}
```


### [2026-09-14T02:29:41.791Z] TOOL RESULT

```
Root / lemma: (s)pen-l(d-) 

Meaning: to pull; to spin 

Note: (s)pen- : spe(i)-^7\e\\eu' = pen-leed'\ pa-^ graze the cattle, feed' = b^a- : b'^en- 

'speak'; compare das different vokalisierte pan-^ texture ', above S. 788. 

Material: 1 . forms without -5-: 

Armenian hanum, Aor. hanayav\d henum, Aor. henrio weave, stitch up, sew together'; 
s. above Meillet Esquisse2 55, 105, 111 f.; 

gr. TT£vo[jai 'strenge myself an, miihe myself ab, have Mangel', ttovo^ 'muhsame work, 
hardship, distress ', novsoj 'mijhe myself ab, etc.', novr|p6(; 'in schlechtem Zustande, 
defective, faulty, lewd, lasterhaft', nsvnc; 'arm, poor', nsvia 'lack, poverty', nsivnv 'starve', 
from which probably retrograd nsivr) 'hunger' and Trarot; svSupa Tf|(; "Hpat; Hes. as *pn- 
tos, diese or eine similar /-formation lies also dem Old Irishe/- ' apparel ' the basic; 

Lithuanian pinli, p/nt/l\ax, wattle, braid', pant/sm. f.. Old Prussian pantoi. 'manacle', 
Latvian pinu, /O/7'flax, wattle, braid', yC>//7e/r/s 'manacle'; 



Old Church Slavic pbng, yO^Z/'spannen', ablaut. opona\. "curtain', ponjava'limhang, 
dress', /op/c»"manacle'(serb. puto), wherefore among others russ. prepjatb "hinder', 
raspjatb "crucify ', pjatb, pnutb "with dem Fuftestoften' and Old Church Slavic p§ta 
"calcaneus ' (serb. petasati^W\Vc\ den Fijften ausschlagen'), russ. pjata, serb. peta, 
Lithuanian pent/sm. "ds.; back the axe, the scythe'. Old Prussian yoe/7//s "calcaneus '; 

perhaps alb. pende, pende^pa\r Ochsen; yoke (piece of wood as field measure)' from a 
*penta'* yoke, pair of harnessed oxen '; also yOe'/7/r"Kopper; 

2. forms with aniaut. s-: 

Latin spontelrom eigenem actuation, from freiem Willen'; 

Gothic Old High German Old English spinnan. Old Icelandic spinna "spinnen' {*spenud, 
compare spannanS. 982 from *spa-nud). Old High German spinna^ spider' (under the 
influence of common Celtic -ns-, -nt- > -nn-); with plain rr. Old Icelandic spun/m. 
"Gespinsf, Old English spinel. Old High German sp/na/a {and spinnila) " spindle'. 

3. extension (s)pen-d-: 

Lithuanian spendziu, sp^sf/^e'\nen Fallstrick lay, place (spannen)'. Old Lithuanian 
spandau, -y// "spannen', Lithuanian spanskus^ narrow, driJckend', sp^stas' dragnet', 
Latvian sp/est'press, constrain, oblige', iterative spaidft, sp^ds/s' Fallstrick, dragnet ', 
Latvian spendele^ feather an a Schlosse', 5/oa/7o''a"Strickwerk am Pflug', as also pam. 
s/?^/7c//'"plough', gr. aniv5£Tpa aporpov Hes. (i.e. aniv5r|pa); 

Old Church Slavic /0^/7o'6 "span', pgd/t/^urge, press, push, drive, push' (originally 
perhaps "ein Vieh an gespanntem Strick vorwartsziehen'); presumably also as "gespannt 
hangen', Latin pendeo, -ere^ hang, herabhangen', pendo, -ere'\Nagen, assess, pay' (to 
weighing hang), Umbrian a/77yC>e/7/^"impendit6'; whether also Old English fintam. "tail, 
Folge'? 

References: WP. II 660 ff., WH. II 579 f., Trautmann 214, 219, Vasmer 2, 272, 379 f. 
Page(s): 988 

Root / lemma: speno- steno- p(a)steno- 

Meaning: teat; breast 

Material: 1 . aniaut sp. Old Irish sine m. "teat': bo tri-phne = bo tnsine "cow with drei 

Zitzen', Middle Irish sineSeain ^uvu\a';
```


## [2026-09-14T02:29:52.402Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD spen ===\"; grep -n \"^(s)pen-\\|^spen-\\|^(s)pen\" AHD_watkins1985.txt | head\necho; echo \"=== AHD splegh/spelgh ===\"; grep -n -i \"splegh\\|spelgh\\|spleen\" AHD_watkins1985.txt | head\necho; echo \"=== AHD sper sparrow ===\"; grep -n -i \"^sper-\\|sparrow\" AHD_watkins1985.txt | head"
}
```


### [2026-09-14T02:29:52.486Z] TOOL RESULT

```
=== AHD spen ===

=== AHD splegh/spelgh ===
153:Internal organs were also named in Indo- European times, including the womb (g“elbh-), gall (ghel-?), brain (mregh-mno-, confined to Low German and Greek), spleen (spelgh-), and liver (yekr). The male sexual organs, pes- and ergh-, are common patri- mony, as is ors-, “backside.”
736:Latin micturire, to want to urinate (desiderative of meiere, to urinate): MICTURATE. [Pok. meigh- 713.] meik-. To mix. 1. Variant form *meig- in Greek mig- nunai, to mix: AMPHIMIXIS, APOMIXIS, PANMICTIC, PAN- MIXIS. 2. Suffixed zero-grade form *mik-sk- in Latin miscére (past participle mixtus), to mix: MEDDLE, (MED- LEY), (MELANGE), MESTIZO, MISCELLANEOUS, MISCIBLE, MIX, MIXTURE; ADMIX, COMMIX, IMMIX, MISCEGENATION, (PELL-MELL), PROMISCUOUS. 3. Possibly a Germanic form *maisk- in Old English mdsc, macs, mdx, mashed malt: MASH. [Pok. meik- 714.] mei-no-. Opinion, intention. 1. Germanic *main- in Old English *mdn, opinion, complaint (> Middle English mone, complaint): MOAN; (BEMOAN). 2. Germanic *main- Jan in Old English ménan, to signify, tell, complain of, moan: MEAN}, [Pok. mei-no- 714.] mel-1, Soft; with derivatives referring to soft or softened materials of various kinds. I. Extended form *meld-. 1. Germanic *meltan in Old English meltan, to melt: MELT. 2. Possibly Germanic *miltja- in Old English milte, spleen, and Middle Dutch milte, milt: mit. 3. Possibly Germanic *malta- in Old English mealt, malt: MALT. 4. Suffixed variant form *mled-sno- in Greek blennos, slime, also a name for the blenny: BLENNY. 5. Suffixed zero-grade form *mid-wi- in Latin mollis, soft: MOIL, MOLLIFY, MOLLUSK, MOUILLE; EMOLLIENT; 6. Possibly nasalized variant form *mlad- in Latin blandus, smooth, caressing, flattering, soft-spoken: BLAND, BLANDISH. II. Variant form *smeld-. Germanic *smelt- in: a. Middle Dutch and Middle Low German smelten, to smelt: SMELT!; b. Old High German smalz, animal fat: SCHMALTZ; C. Italian smalto, melted glass: SMALT; d. Old French esmail, enamel: ENAMEL; e. perhaps Old English smelt, smylt, a marine fish, smelt: SMELT?. III. Extended form *meldh-. 1. Germanic *mildja- in Old English milde, mild MILD. 2. Possibly Greek maltha, a mixture of wax and pitch: MALTHA. IV. Suffixed form *mel-sko- in Ger- manic *mil-sk- in Old English melfi)sc, mylsc, mild, mellow (> Middle English melsche, friable): MULCH. V. Extended form *mfk- in Greek malakos, soft: CHON- DROMALACIA, MALACOLOGY, OSTEOMALACIA. VI. Possi- bly Celtic *molto-, sheep, in Old French moton, sheep: MUTTON. VII. Suffixed zero-grade form *()ml-u- in Greek amblus, blunt, dull, dim: AMBLYGONITE, AMBLY- opiA. [Pok. 1. mel- 716.] mel-2, Of a darkish color. 1. Greek melas, black: MEL- ANO-; MELANCHOLY, PSILOMELANE. 2. Greek mullos, a marine fish: MULLET; (SURMULLET). 3. Latin mulleus, reddish purple (used only to designate a ceremonial shoe worn by Roman magistrates): MULE. 4. Perhaps Ger- manic *mal- in Middle Dutch malen, to paint: MAUL- STICK. [Pok. 6. mel- 720.] mel-3. A limb. Greek melos, limb, hence a musical member or phrase, hence music, song, melody: MELISMA; ACRO- MELIC, MELODRAMA, MELODY. [Pok. 5. mel- 720.] mel-4. Strong, great. 1. Suffixed (comparative) form *mel-yos- in Latin melior, better: (AMELIORATE), MELIO- RATE, MELIORISM. 2. Suffixed zero-grade form *m/J-to- in Latin multus (neuter multum), much, many: MOLTO, MULTI-, MULTITUDE. [Pok. 4. mel- 720.] mel-5. Bad. Latin malus, bad, and male, ill (> malignus, harmful): MAL-, MALICE, MALIGN; DISMAL, MALADY, MALEDICT, MALEFACTOR, MALEVOLENT, MALVERSATION. [Pok. mélo- 724.] mel-€, Wool. Possibly suffixed zero-grade form *ml-no- in Greek mallos, wool. [Pok. 2. mel- 719.] mel-?. To miss, deceive. Germanic *mai- in Middle Dutch mal, foolish, silly: MALLEMUCK. [Pok. 2. mel- 719.] meldh-. To pray, speak words to a deity. Germanic *meld- in Old High German meldén, to proclaim, reveal: MELD}. [Pok. 1. meldh- 722.] mele-. Also mel-. To crush, grind; with derivatives referring to various ground or crumbling substances (such as flour) and to instruments for grinding or crush-
981:ably from the splitting of its husk at threshing), akin to the Germanic source of Late Latin spelta, spelt: SPELT!. 2. Extended form ‘*spelt- in Germanic *spilthjan in Old English spillan, to spill, destroy: sPILLt. 3. Suffixed o-grade form *spol-yo- perhaps in Latin spolium, hide torn from an animal, armor stripped from an enemy, booty: SPOIL; DESPOIL. [Pok. 1. (s)p(h)el- 985.] spel-2. To shine, glow. Extended form *splend- in Latin splendére, to shine: SPLENDID; RESPLENDENT. [Pok. 2. (s)p(h)el- 987.] spel-3. To say aloud, recite. Suffixed form *spel-no-. 1. Germanic *spellam in: a. Old English spell, discourse, story: SPELL?; b. Old English spel, news: GOSPEL. 2. Ger- manic denominative *spellén in Old French espeller, espelir, to read out: SPELL!. [Pok. (s)pel- 985.] spelgh-. Spleen, milt. 1. Deformation *(pjlihén in Latin lién, milt, spleen: LIENAL. 2. Uncertain preform in: a. Greek splén, spleen: SPLEEN; b. Greek splankhna, inward parts: SPLANCHNIC. [Pok. sp(h)elgh(en) 987.] (s)pen-. To draw, stretch, spin. I. Basic form *spen-. 1. Suffixed form *spen-wo- in Germanic *spinnan, to spin, in: a. Old English spinnan, to spin, with derivative *spin-thron-, “the spinner,” contracted to spithra, spi- der: SPIN, SPIDER; b. Germanic derivative *spin-ilén in Old English spinel, spindle: SPINDLE. 2. Extended form *pend- in Latin pendére, to hang (intransitive), and pendere, to cause to hang, weigh, with its frequentative pensdre, to weigh: PAINTER2, (PANSY), PENCHANT, PEN- DANT, PENDENTIVE, PENDULOUS, PENSILE, PENSION}, PENSIVE, PESO, POISE!; ANTEPENDIUM, APPEND, (APPEN- DIX), COMPENDIUM, COMPENSATE, DEPEND, DISPENSE, EXPEND, IMPEND, PENTHOUSE, PERPEND, PERPENDICU- LAR, PREPENSE, PROPEND, SUSPEND, VILIPEND. 3. Per- haps suffixed form *pen-ya- in Greek penia, lack, poverty (< “a strain, exhaustion”): -PENIA. II. O-grade forms *spon-, *pon-. 1. Germanic “spannan in: a. Middle Dutch spannen, to bind: SPAN; b. Old High German spannan (> German spannen), to stretch: SPANNER. 2. Germanic *spanno- in Old English span(n), distance: SPAN], 3. Perhaps Germanic *spangé in Middle Dutch spange, clasp: SPANGLE. 4. Suffixed and extended form *pond-o- in Latin pondé, by weight: PoUND!. 5. Suffixed and extended form *pond-es- in Latin pondus (stem ponder-), weight, and its denominative ponderdre, to weigh: PONDER, PONDEROUS; EQUIPONDERATE, PREPON- DERATE. 6. Perhaps suffixed form *spon-t- in Latin sponte, of one’s own accord, spontaneously: SPONTANE- ous. 7. Greek penesthai, to toil, with o-grade derivatives ponos, toil, and ponein, to toil: GEOPoNic. [Pok. (s)pen-(d)- 988.] spend-. To make an offering, perform a rite, hence to engage oneself by a ritual act. O-grade form *spond-. 1. Suffixed form *spond-eyo- in Latin spondére, to make a solemn promise, pledge, betroth: SPONSOR, SPOUSE; DESPOND, ESPOUSE, RESPOND. 2. Suffixed form *spond-a in Greek spondé, libation, offering: SPONDEE. [Pok. spend- 989.]} sper-'. Spear, pole. 1. Germanic *speru- in: a. Old Eng- lish spere, spear: SPEAR; b. Middle Low German spér, spit: SPARERIBS. 2. Germanic *sparjén- in Old Norse sperra, rafter, beam: SPAR}. [Pok. 1. (s)per- 990.] sper-2. To turn, twist. 1. Suffixed form *sper-ya- in Greek speira, a winding, coil, spire: SPIRE?. 2. Suffixed zero-grade form *spr-to- in Greek sparton, rope, cable: ESPARTO. [Pok. 3. sper- 991.] . sper-3. Bird’s name, sparrow. Suffixed o-grade form *spor-wo- in Germanic *sparwan- in Old English spearwa, spearwe, sparrow: SPARROW. [Pok. sper-(g)- 997.] sper-4. To strew. I. Zero-grade form *spr-. 1. Germanic *spr- in Old English spréawlian, to sprawl: SPRAWL. 2. Extended form *spreut- in Germanic *sprit- in: a. Old English spriitan, to sprout: SPROUT; b. Old English spryttan, to sprout, come forth: sPpuRT; c. Old English
1747:LIEN leig-1 LIENAL_ spelgh- LIEUTENANT ten- LIFE leip-
2279:SPECIOUS spek- SPECTACLE spek- SPECTRUM spek- SPECULATE spek- SPECULUM spek- SPEECH spreg- SPEED spé-1 SPELL! spel-3 SPELL? spel-3 SPELT! spel-! SPERM! sper-4 SPEW spyeu- SPHENE spé-2 SPHENO- spé-2 SPICA spei- SPICA_ spei- SPICULUM spei- SPIDER (s)pen- SPIKE! spei- SPIKE? spei- SPILE spei- SPILL! spel-1 SPILL? spei- SPIN (s)pen- SPINDLE (s)pen- SPINE spei- SPINEL spei- SPINIFEX dhé-1 SPINNEY spei- SPIRACLE spirare SPIRE! spei- SPIRE? sper-2 SPIRIT spirare SPIT! spyeu- SPIT? spei- SPITTLE spyeu- SPITZ spel- SPLANCHNIC spelgh- SPLEEN spelgh- SPLENDID spel-2 SPLICE splei- SPLINT splei- SPLINTER splei- SPLIT splei- SPOIL spel-1 SPOKE! spei- SPONDEE spend- SPONSOR spend- SPONTANEOUS (s)pen- SPONTOON peuk- SPOON spé-2 SPOOR spere- SPORADIC sper-4 SPORE sper-4 SPORO- sper-4 SPORRAN bursa SPORT per-2 SPOUSE spend- SPOUT spyeu- SPRAG (s)preg- SPRAWL sper-4 SPREAD sper-4 SPREE ghend- SPRING spergh-

=== AHD sper sparrow ===
147:LING (storo-), and, at least in some dialects, the SPARROW (sper-’), FINCH (sping-), and woodpecker ((s)peik-). The generic term for “bird” was awi- (Latin avis), and from this was derived the well-represented word for egg, *dOwyo-.
980:sper-4
981:ably from the splitting of its husk at threshing), akin to the Germanic source of Late Latin spelta, spelt: SPELT!. 2. Extended form ‘*spelt- in Germanic *spilthjan in Old English spillan, to spill, destroy: sPILLt. 3. Suffixed o-grade form *spol-yo- perhaps in Latin spolium, hide torn from an animal, armor stripped from an enemy, booty: SPOIL; DESPOIL. [Pok. 1. (s)p(h)el- 985.] spel-2. To shine, glow. Extended form *splend- in Latin splendére, to shine: SPLENDID; RESPLENDENT. [Pok. 2. (s)p(h)el- 987.] spel-3. To say aloud, recite. Suffixed form *spel-no-. 1. Germanic *spellam in: a. Old English spell, discourse, story: SPELL?; b. Old English spel, news: GOSPEL. 2. Ger- manic denominative *spellén in Old French espeller, espelir, to read out: SPELL!. [Pok. (s)pel- 985.] spelgh-. Spleen, milt. 1. Deformation *(pjlihén in Latin lién, milt, spleen: LIENAL. 2. Uncertain preform in: a. Greek splén, spleen: SPLEEN; b. Greek splankhna, inward parts: SPLANCHNIC. [Pok. sp(h)elgh(en) 987.] (s)pen-. To draw, stretch, spin. I. Basic form *spen-. 1. Suffixed form *spen-wo- in Germanic *spinnan, to spin, in: a. Old English spinnan, to spin, with derivative *spin-thron-, “the spinner,” contracted to spithra, spi- der: SPIN, SPIDER; b. Germanic derivative *spin-ilén in Old English spinel, spindle: SPINDLE. 2. Extended form *pend- in Latin pendére, to hang (intransitive), and pendere, to cause to hang, weigh, with its frequentative pensdre, to weigh: PAINTER2, (PANSY), PENCHANT, PEN- DANT, PENDENTIVE, PENDULOUS, PENSILE, PENSION}, PENSIVE, PESO, POISE!; ANTEPENDIUM, APPEND, (APPEN- DIX), COMPENDIUM, COMPENSATE, DEPEND, DISPENSE, EXPEND, IMPEND, PENTHOUSE, PERPEND, PERPENDICU- LAR, PREPENSE, PROPEND, SUSPEND, VILIPEND. 3. Per- haps suffixed form *pen-ya- in Greek penia, lack, poverty (< “a strain, exhaustion”): -PENIA. II. O-grade forms *spon-, *pon-. 1. Germanic “spannan in: a. Middle Dutch spannen, to bind: SPAN; b. Old High German spannan (> German spannen), to stretch: SPANNER. 2. Germanic *spanno- in Old English span(n), distance: SPAN], 3. Perhaps Germanic *spangé in Middle Dutch spange, clasp: SPANGLE. 4. Suffixed and extended form *pond-o- in Latin pondé, by weight: PoUND!. 5. Suffixed and extended form *pond-es- in Latin pondus (stem ponder-), weight, and its denominative ponderdre, to weigh: PONDER, PONDEROUS; EQUIPONDERATE, PREPON- DERATE. 6. Perhaps suffixed form *spon-t- in Latin sponte, of one’s own accord, spontaneously: SPONTANE- ous. 7. Greek penesthai, to toil, with o-grade derivatives ponos, toil, and ponein, to toil: GEOPoNic. [Pok. (s)pen-(d)- 988.] spend-. To make an offering, perform a rite, hence to engage oneself by a ritual act. O-grade form *spond-. 1. Suffixed form *spond-eyo- in Latin spondére, to make a solemn promise, pledge, betroth: SPONSOR, SPOUSE; DESPOND, ESPOUSE, RESPOND. 2. Suffixed form *spond-a in Greek spondé, libation, offering: SPONDEE. [Pok. spend- 989.]} sper-'. Spear, pole. 1. Germanic *speru- in: a. Old Eng- lish spere, spear: SPEAR; b. Middle Low German spér, spit: SPARERIBS. 2. Germanic *sparjén- in Old Norse sperra, rafter, beam: SPAR}. [Pok. 1. (s)per- 990.] sper-2. To turn, twist. 1. Suffixed form *sper-ya- in Greek speira, a winding, coil, spire: SPIRE?. 2. Suffixed zero-grade form *spr-to- in Greek sparton, rope, cable: ESPARTO. [Pok. 3. sper- 991.] . sper-3. Bird’s name, sparrow. Suffixed o-grade form *spor-wo- in Germanic *sparwan- in Old English spearwa, spearwe, sparrow: SPARROW. [Pok. sper-(g)- 997.] sper-4. To strew. I. Zero-grade form *spr-. 1. Germanic *spr- in Old English spréawlian, to sprawl: SPRAWL. 2. Extended form *spreut- in Germanic *sprit- in: a. Old English spriitan, to sprout: SPROUT; b. Old English spryttan, to sprout, come forth: sPpuRT; c. Old English
987:sping-. Also ping-. Bird’s name, sparrow, finch. Ger- manic *finki- in Old English finc, finch: FINCH. [Pok. (s)jpingo- 999.]
1096:5. Greek trias, the number three: TRIAD. 6. Greek trikha, in three parts: TRICHOTOMY. 7. Greek compound triérés, galley with three banks of oars, trireme (-érés, oar; see era-'): TRIERARCH. 8. Suffixed form “*tri-to- in Greek tritos, third: TRITIUM; TRITANOPIA. 9. Compound form *tri-pl-, “threefold” (*-pl- < combining form *-plo-; see pel-3), in Greek ¢triploos, triple: TRIPLE. 10. Compound form *tri-plek-, “threefold” (*-plek-, -fold; see plek-), in Latin triplex, triple: TRIPLEX. 11. Compound form *tri-st-i, “third person standing by” (see sta-), in Latin testis, a witness: TESTAMENT, (TESTIMONY); ATTEST, CONTEST, DETEST, OBTEST, PROTEST, TESTIFY. 12. Per- sian si, three: straR. III. Extended zero-grade form “iris, “thrice.” 1. Latin ter, thrice: TERN?; TERPOLYMER. 2. Greek tris, thrice: TRISOCTAHEDRON. 3. Suffixed form *tris-no- in Latin trini, three each: TRINE, (TRINITY). IV. Suffixed o-grade form *troy-o- in Russian troje, three: TROIKA. [Pok. trei- 1090.] trem-. To tremble. Possibly related to trep-' and tres- through a hypothetical base *ter-. Latin tremere, to shake, tremble: TREMENDOUS, TREMOR, TREMULOUS. [Pok. trem- 1092.] trep-'. To tremble. Possibly related to trem- and tres- through a hypothetical base *ter-. Latin trepidus, agi- tated, alarmed: TREPID; INTREPID. [Pok. 1. trep- 1094.] trep-2. To turn. 1. Greek trepein, to turn: -TROPOUS; APOTROPAIC, TREPONEME. 2. O-grade form *trop- in: a. suffixed form *trop-o- in Greek tropos, a turn, way, manner: TROPE, TROPO-, TROVER; CONTRIVE, (RE- TRIEVE); b. suffixed form *trop-d- in Greek tropé, a turning, change: TROPHY, TROPIC; ENTROPY. [Pok. 2. trep- 1094.] tres-. To tremble. Possibly related to trem- and trep-1 through a hypothetical base *ter-. Metathesized form *ters- in o-grade suffixed (causative) form *tors-eyo- in Latin terrére, to frighten (< “to cause to tremble”), with vowel e from terror (< *ters-os-), terror: TERRIBLE, TERROR; DETER, TERRIFIC. [Pok. tres- 1095.] treud-. To squeeze. 1. Suffixed o-grade form *troud-o- in Germanic *thrautam in Old English thréat, oppression, use of force: THREAT. 2. Variant form *trid- in Germanic “thristjan in Old Norse thrysta, to squeeze, compress: THRUST. 3. Latin tridere, to thrust, push: ABSTRUSE, EXTRUDE, INTRUDE, OBTRUDE, PROTRUDE. [Pok. tr-eu-d 1095.] trozdo-. Thrush. 1. Germanic *thrust- in Old English throstle, thrush: THROSTLE. 2. Germanic *thruskj6n- in Old English thrysce, thrush: THRUSH}. 3. Zero-grade reduced form *trzdo- in Latin turdus, thrush: STURDY. 4. Perhaps altered in Greek strouthos, sparrow, ostrich: STRUTHIOUS; (OSTRICH). [Pok. trozdos 1096.] tu-. Second person singular pronoun; you, thou. 1. Lengthened-grade form “ti (accusative “te, *tege) in Germanic *thii (accusative *theke) in Old English thi (accusative thec, thé), thou: (THEE), THOU!. 2. Suffixed extended form *éwjei-no- in Germanic *thinaz in Old English thin, thine: THINE, THY. [Pok. tu- 1097.] twei-. To agitate, shake, toss. 1. Extended form *tweid- in Germanic *thwit- in: a. Old English thwitan, to strike, whittle down: WHITTLE; b. Middle Dutch duit, a small coin (? < “piece cut or tossed off”): DorT. 2. Extended form *tweis- in Greek seiein, to shake: SEISM, SISTRUM. [Pok. 2. tuei- 1099.] twengh-. To press in on. Germanic *thwang- in: a. Old English thwong, thwang, thong, band (< “constraint”): THONG; b. by-form *twangjan in Old English twengan, to pinch: TWINGE. [Pok. twengh- 1099.] twer-', To turn, whirl. Zero-grade *tur-. I. Variant form *stur-. 1. Suffixed form *stur-mo- in Germanic *sturmaz, storm (< “whirlwind”), in Old English storm, storm: STORM. 2. Germanic *sturjan in Old English styrian, to move, agitate: STIR!. II. Suffixed form *tur-bd in Greek turbé, tumult, disorder (> Latin turba, disorder, turbé, spinning top, and turbdre, to confuse, disorder): (TROU-
2278:sow2 si- SPADE! spé-2 SPADE2 spé-2 SPAN! (s)pen- SPAN2 (s)pen- SPANGLE (s)pen- SPANNER (s)pen- SPAN-NEW newo-, spé-2 SPAR! sper-! SPARERIBS rebh-2, sper-1 SPARGE (s)preg- SPARLING spei- SPARROW sper-? SPARSE (S)preg- SPATHE spé-2 SPATHIC spé-2 SPATULA spé-2 SPAY spé-2 SPEAK spreg- SPEAR sper-! SPECIES spek- SPECIMEN spek-
```


## [2026-09-14T02:30:01.271Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('POK_02.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nprint('nleaves',len(leaves))\nfor p in (990,991,996,997,998):\n    i=p-344\n    print('=== printed',p,'leaf',i,'===')\n    print(leaves[i][:900])\nEOF"
}
```


### [2026-09-14T02:30:02.402Z] TOOL RESULT

```
Exit code 1
nleaves 434
=== printed 990 leaf 646 ===
Traceback (most recent call last):
  File "<stdin>", line 7, in <module>
IndexError: list index out of range
```


## [2026-09-14T02:30:05.364Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor f in POK_01.txt POK_02.txt POK_03.txt; do echo \"$f: $(python3 -c \"\nt=open('$f',encoding='utf-8',errors='replace').read(); print(t.count(chr(12))+1)\")\"; done\necho \"---- search Sperling in POK_03 ----\"\ngrep -n \"Sperling\" POK_03.txt | head -20"
}
```


### [2026-09-14T02:30:06.538Z] TOOL RESULT

```
POK_01.txt: 364
POK_02.txt: 434
POK_03.txt: 430
---- search Sperling in POK_03 ----
3134:8*  sper-(g-)  in  Vogelnamen,  besonders  , Sperling^;  sparuo-'.prauo-  ds.
3135:Got.  sparwa,  ags.  spearwa,  ahd.  sparo  ^Sperling'  (*urgerm.  *sparwan-)'^ ■  mhd.  sperlinc  nhd.  Sperling^  Deminutiv;  aisl.  spgrr  ds.  aus  *sparwa-z, r  vgl.  auch  nhd.  Sperber,  ahd.  sparwari  (Endglied  nach  ahd.  aro  ,Aar,  Adler' umgestaltet  ?) ;
3139:Formen  auf  g:  gr.  PN  ^TCoqyiXog  , Sperling*,  ((y)7t€QyovXog'  ögvid-ägiov ^yqiov  Hes.;  ahd.  sperk,  sperch,  spirch  , Sperling',  apr.  spergla-wanag[is] ,Sperber*  (eig.  ,Sperlingsgeier'),  ablaut.  spurglis  m.  , Sperling*.
3157:spritzen',  weiter:  sper-  , Sperling',  sper-  , Sparren*,  sp(h)er-  ,MistkÜge!»
3265:[s)pingo-  , Sperling,  Fink',  vom  piependen  Laute.
3266:Gr.  GTtlyyog  (Hes.),  an:il^a  {^Grtiyyia)  ,Fink*  (ähnlich  arcvyyag,  OTiivd^ihv, üftb'og  ,Fink*),  oml^iag  m.  ,Sperber'  (Bed.  ,Sperlingstößer'  wie  in  nhd. Sperber :  ahd.  sparo  »Sperling^),  aiti^o)  ,piepe^ ;  schwed.  spinh,  spikke  ^kleiner Vogel,  Sperling  u.  ä.',  engl,  (aus  dem  Nord.)  spink  ,Fink';  ai.  phiidgaka-  m. ,ein  best.  Vogel,  der  gabelschwänzige  Würger*  (Bed.  wie  in  ör/rt^/ag,  s.  o.) ;
3267:daneben  ohne  anlaut.  s-  ahd.  fincho,  ags.  finc,  engl,  finch  ,Fink',  davon unabhängige  Schallbezeichnung  in  frz.  pinson,  ital.  pincione,  span.  pinzon, wie  wohl  auch  in  schwed.  pink  ,Sperling*,  engl,  dial,  pink,  pinch  ,Fink^
4667:Ai.  tittibha-  m.  ,Parra  jacana';  lett.  titühis,  titübite  ,Wasserla  f --^-^ tilvikas,  titilvtkas,  tiülvis  , Brachhuhn,  Schnepfe' ;  gr.  TiTvSiCtü  o/l       * ßitw  ,gackern  (vom  Rebhuhn,  der  Schwalbe');  lat.  titiöj  -äre    zw^i^^^ vom  Sperling';  lett.  titet  ,singen'.  TT?***»
```


## [2026-09-14T02:30:10.723Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('POK_03.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nfor target in (3134,3265):\n    leaf='\\n'.join(lines[:target]).count('\\f')\n    print('line',target,'leaf',leaf)\nleaves=t.split('\\f')\nfor i in range(224,232):\n    head=leaves[i][:120].replace('\\n',' | ')\n    print(i, head)\nEOF"
}
```


### [2026-09-14T02:30:11.890Z] TOOL RESULT

```
line 3134 leaf 232
line 3265 leaf 240
224 Macht'  (wohl  auch lett.  spXte  , Trotz',  spitigs  , trotzig'); | aksl.  spSjg^  speti  , Erfolg  haben';  sp^ch^  m.  
225 ;  ausspaichen  ,mit  Schrittii oder  ausgespannten  Fingern  ausmessen',  norw.  speika  ,mit  steifen  fe». spannten) 
226 i  „h"]  (auch  germ.  -II- ^ohl  aus  -In-)  lett.  pett  ,schmähen,  lästern,  verleumden^,  paVas  (Plur.)  ,Ta- del,
227 lat.  spolium  »abgezogene  oder  abgelegte  Tierhaut;  dem  Feinde  aW nommene  Rüstung,  Beute'; | mit  ^Erweit. ;  ahd.
228 ei-   ,kahl',  piek-  pleik-,   ,reißen'J | 987 | pleu(s-,  -k-)  ,ausrupfen',  plas-  ,abspalten'. | WP.  n  677  ff.,  WH.  
229 . | 1.  Formen  ohne  -s- :  *)  ^| Arm.  hanurrij  Aor.  hanay  und  henum,  Aor.  heni  ,weben,  zusammennähe»* | s.  darü
230 )pei2-),  (s)pon-,  {s)pondho-  ,Holzeimer^,  auch  gelegentlich  von  an- deren Holzgeräten;  verwandt  mit  s'phe-,  s
231 ch  lit.  speügti  ,klingen',  lett.  spiegt  ,wie  eii^ Maus  pfeifen'  angereiht  werden; | vielleicht  idg.  spheng-,
```


## [2026-09-14T02:30:16.068Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('POK_03.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i in range(228,240):\n    nums=re.findall(r'(?<![\\d.])(9[5-9]\\d|10\\d\\d)(?![\\d])', leaves[i])\n    print(i, nums[:8], '||', leaves[i][:80].replace('\\n',' '))\nEOF"
}
```


### [2026-09-14T02:30:17.168Z] TOOL RESULT

```
228 ['987', '988'] || ei-   ,kahl',  piek-  pleik-,   ,reißen'J 987 pleu(s-,  -k-)  ,ausrupfen',  plas
229 ['982', '989'] || . 1.  Formen  ohne  -s- :  *)  ^| Arm.  hanurrij  Aor.  hanay  und  henum,  Aor.
230 ['990'] || )pei2-),  (s)pon-,  {s)pondho-  ,Holzeimer^,  auch  gelegentlich  von  an- deren
231 ['991'] || ch  lit.  speügti  ,klingen',  lett.  spiegt  ,wie  eii^ Maus  pfeifen'  angerei
232 ['992'] || rammeln^,  ahd.  mhd.  sperren  , durch  einen  Sperrbalken verschließen,  sperr
233 ['993'] || iterung  spereg-,  nas.  spreng-  ,winden,  umwickeln,  dadurch  ««f zusammensch
234 ['994'] ||  dem  Fuße  ausschlagen^,  ags.  spurnan,  spornan  ^ds._,  auch  , zurückstoßen
235 ['995'] ||  mnd.  spröte  , (Spritzer  =)  Fleck^  Sommersprosse^ B.  z- Basis  sprei-d-,  
236 ['996'] ||   Sprenkel  beim  Vogelfang',  luxemb.  spriegel Sperrholz  zum  Auseinanderspan
237 ['998', '997'] ||   AjI, springen  der  Blumen;  das  Sich-spreizen^,  mengl.  sprenten  , springe
238 ['998'] || �,  -ere  ,streuen,  hinstreuen,  sprengen,  spritzen' ; mnd.  sparJcen  , Funke
239 [] ||   ,Regenwolke  (spritzend, sprengend);  der  Regen-  und  Gewittergott'  (s.  ob
```


## [2026-09-14T02:30:23.024Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('POK_03.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nprint(leaves[231][:400])\nprint('~~~~~~~ LEAF232 ~~~~~~~')\nprint(leaves[232][:2500])\nEOF"
}
```


### [2026-09-14T02:30:24.100Z] TOOL RESULT

```
ch  lit.  speügti  ,klingen',  lett.  spiegt  ,wie  eii^ Maus  pfeifen'  angereiht  werden;
vielleicht  idg.  spheng-,  also  zu  gr.  q)€'yyog  n.  ,Licht,  Schein',  y^j^ ,leuchte,  erhelle';  i?
da  *spend-  »glänzen'  eine  Zerlegung  in  *sp(h)en-g-,  -d-  zur  Erwägt^j» stellt,  kann  speng-  nicht  zuversichtlich  als  Nasalform  eines :
{s)peg-  gelten,  das  erschlossen  wird  aus  nhd.  
~~~~~~~ LEAF232 ~~~~~~~
rammeln^,  ahd.  mhd.  sperren  , durch  einen  Sperrbalken verschließen,  sperren-,  ausspreizen*;
^veitergebildet  ahd.  spirdren  ,nlti'  (j-Verb  wie  muntren,  s.  Schatz^,  Ger- r    manica  für  Siewers  367);
ohne  anl.  s-:  lat.  paries  ,Wand^  (ursprüngl.  ,die  Seitenstützen  eines 2eltes  u.  dgl.*);  slav.  *phrg,  *perti  ,stützen',  mit  pod^-  ,fulcire^,  mit  za- .claudere*,  z.  B.  aksl.  pod^phrg,  präti  , stützen*,  zaprHi  , schließen',  russ. ^.pereth  ^stemmen,  an  oder  gegen  etwas  stützen;  refl.  sich  woran  lehnen, sich  wogegen  sperren,  sträuben^  zapereth  ,versperren,  verschließen',  poln. przec  , spreizen,  sperren^,  aksl.  pod^por^,  -pora  ,fulcrum,  baculum',  russ. upor  , Stütze,  Strebepfeiler*  usw.
WP.  II  665  f.,  WH.  II  254,  568,  Trautmann  275  f.,  Vasmer  2,  341.
8*  sper-(g-)  in  Vogelnamen,  besonders  , Sperling^;  sparuo-'.prauo-  ds.
Got.  sparwa,  ags.  spearwa,  ahd.  sparo  ^Sperling'  (*urgerm.  *sparwan-)'^ ■  mhd.  sperlinc  nhd.  Sperling^  Deminutiv;  aisl.  spgrr  ds.  aus  *sparwa-z, r  vgl.  auch  nhd.  Sperber,  ahd.  sparwari  (Endglied  nach  ahd.  aro  ,Aar,  Adler' umgestaltet  ?) ;
gr.  aTtaqaaiov  Ugvsov  if.ig)SQeg  ütqov&w  Hes.  i^aTtctQft^-tiom)'^  das  forman- tische  u  auch  (??)  in  gr.  xp&q,  ion.  ep.  iprjq  (hom.  Akk.  PL  xpfjqag),  Gen. xpäQÖg  ,Star'  (ursprüngl.  "^'(p&qf-q,  Gen.  *ipaQf6g'i!),  jünger  ip&qog,  y^^Qog, xpagog  m.  ds.,  xpäQÖg  ,stargrau';  dazu  wohl  as.  sprä,  ndl.  spreemo,  nordfries. sprian,  mnd.  spren,  nd.  (nhd.)  sprehe  ,Star^;
com.  frau,  bret.  fräo  ,Krähe'  (*sprawä)]  daß  lat.  parra  ,ein  Vogel, dessen  Geschrei  Unglück  bedeutete',  umbr.  parfam,parfa  ,parram^  (*parsa) ein  s-loser  Verwandter  sei,  ist  ganz  fragwürdig;
toch.  A  späraü  ,ein.  Vogel';
Formen  auf  g:  gr.  PN  ^TCoqyiXog  , Sperling*,  ((y)7t€QyovXog'  ögvid-ägiov ^yqiov  Hes.;  ahd.  sperk,  sperch,  spirch  , Sperling',  apr.  spergla-wanag[is] ,Sperber*  (eig.  ,Sperlingsgeier'),  ablaut.  spurglis  m.  , Sperling*.
WP.  II  666  f.,  WH.  II  257,  Trautmann  275.
3.  sper-  , drehen,  winden'.
Gr.  ansTga  f.,  ,Windung,  Spirale,  alles  Geflochtene  (z.  B.  vom  Netz,  Tau)*, (Jusigdo)  ,winde,  wickle^  aneiQG^a  ,Windung,  Windet;   anägTog  m.   ,ein
992  #
Strauch,  aus  dessen  Ruten  man  Bänder  oder  Stricke  flocht*,  otvccqtovj  ai ,gedrehtes  oder  geflochtenes  Seil';  a^vglg  (ion.  Gg)VQig)  ^geflochtener (aus
```


## [2026-09-14T02:30:48.646Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT sp∂r∂zan ===\"; grep -n -i \"sp.r.zan\\|Milz\" BRT.txt | head -20\necho; echo \"=== PHD spleen ===\"; grep -n -i \"spleen\\|spul\\|spurz\" PHD.txt PHD_mackenzie.txt | head -20\necho; echo \"=== HRN spurz/sipurz ===\"; grep -n -i \"spurz\\|Milz\\|supurz\\|sipurz\" HRN.txt | head -20\necho; echo \"=== HUB ===\"; grep -n -i \"spurz\\|Milz\" HUB.txt | head -20"
}
```


### [2026-09-14T02:30:48.765Z] TOOL RESULT

```
=== BRT sp∂r∂zan ===
20910:YtÄ  48.  f)  GPra.:  mtirS  vtspS  matda'\  hacaite  asis  .  .  uyrasca  dämdis  upamanO yasnanqm  yam  asaenqm  fr}},wä{sd.)cit  .  .\uyrasca  asaonqm  frava^ayS  yasla  pouru- Yt./o.i3ci,  IIB) bedeutungslos  erscheint  HflOT  hairaks\%A:)  Yt.  /o.  66.  b)  NSf.: uns  das  Relativ  vielfach  dann,  wenn  es,  j>'n^  dim  upanhacat  yä  uyra  naire  kam.' ohne  dass  ein  Verbum  folgt,  dem  Nomen,  1  z-'n/vift'/ Yt. /p.  39;  —  aiHi  ätm  atwyäiti mit  dem  es  kongruirt,  und  dessen  Attri-|_V'l  dahma  *va»uhi  afritis  P,J2;  —  kai buten  vorausgeht  a)  im  gAw.;  I)  \\a\hE  vä  i7j><«  (Sp.  237  m.)  *v?nzyap  ya  näi- Nominativ  oder  dem  ihm  gleichen  Akku- ,  rika  N.  6;  —  saoayeiti  yü  hava  daena  H. sativ.  Die  Fälle,  die  hierher  gezogen  wer-  2.9;  it']  —  ks  yä  kaine  'V.i4.-i^^'>'>;  — den  können,  sind  unter  IIB  verzeichnet:  [hierher  oder  zuIB  (Rel,  in  Kongruenz  mit Y-JO-S  0'^  dr3gva\  4ü.z  (ysi  uxsanS  Atm  Praed.):  *kä  larJ.maitisl  ya  kaca asnqm),32.i.%{yä  karapuäsm  k3Vltasi^,\dainay3t  milzdayasiiStl  apastüitii  U.  4t; 45- 1  (ya  n^qs  sadra),  46.Z  (yy  vä  iiiDi' —  ya  papiiiua  vasö  acisße  (sd.)  N, yä  galhä  datdl  *aSnaAhFj  usw.  Z)  in  ■  62.       c)N.-APm.r  *'taty5i  taxma  xitavayB
27019:•  j,  sp^razan-  m.  "Milz':  'm  F.jg.

=== PHD spleen ===
PHD.txt:568:spas dāštan, ~ hangárdan: thank, give thanks. spās-dār [sp?sd?] | N sip~] grateful, thankful. ~ih: gratitude. spās|-ešnās [sp’ssn’s] grateful. —ómand [-’wmnd] grateful. spas [sp = Av. 0Bàsa-] space, atmosphere. spaxr [sp?hl | M ‘spxr, N *siparx] merrymaking, revelry. spazg [spzg | (M ‘spgj), N sipazg-] slanderous. «il: slander. spëd [spyt! | M ‘spyd, N sapéd] white. ~ag [-k! | N -a] white (of egg, etc.). —bàg [-p’k!' | N -bā] curd soup. --dàr [-?1 | N -dár] white poplar, aspen. spenag [sp(y)m?k! = Av. spanta-, cf. $annág] holy. ~ ménóg : the Good Spirit. Spig [spyk' | M ‘spyg, (N sapriy)] т. brilliance; 2. sprout, shoot. spihr [spy(y)hl | (M ‘spyr), N sipihr] sphere, sky, firmament, fate. ~ig [-yk'] heavenly. spinjanagih [spne’nkyh] hospitality. spiš [spyš | (N šipt$)) louse. Spitāmān [spyt?m?^n] of the Spitama family. spiz- [spyc- | M “рухіп, *spyz-] 1. shine; 2. sprout. —išn: 1. brilliance; 2. sprouting. spöxtan, spēz- [spwhtn', spwc- | M *spwxt, N sip~] thrust; overstep, disobey; delay, reject. ~išn: delay, rejection; disobedience. SpOz [spwe | N sipóz] disobedience; delay. ~gar LEIT N ~] disobedient; dilatory. sprahm(ag) [splhm(k') | M *sprhm(g), N siparham] flower, fragrant herb. spul [spwl] spleen. spurdan, spar- [spwiltn', spl- | N sip~] tread, trample. spurrig [spwlyk!' | (M ‘spwr), N sipari] entire, complete, perfect. ~ith: completeness, perfection. spurz [*spiz | P “spwrz, N sipurz] spleen. srat (sit! | cf. Ar. sirát] street. sraw [s/wb'] word, spell. srawénidan, srawén- [slwbyn-ytn'] report, broadcast. sraxtag [s/htk! = Av. sraxti-] side, part. sray [sd | N saray] house, hall. Igrāy-, -išn, v. srüdan. srāyīdan, ?sráy- [sPd-ytn! = Av. @rdya-] protect. ~išn: protection. srešk [sl(y)£h | (P srsk), N sirifk] drop, tear. srištan, *srēš- [s/szn! | P sryi-, N sir-~] mix, knead. sri$wadag [s/ystotk! = Av. Oriswa-] a third. sréd [s/zvt! | M srwd, N suród] song.
PHD.txt:3780:spleen spul, spurz.
PHD.txt:4773:spéd spēdag spēdbāg spenāg spóxtan spandan Spandarmad sabuk spul spurrigih spurrig spurdan spūz spēz- spinjānagīh spozgar spūzišn sabz spazg spazgīh spar spar- sprahm sprahmag
PHD.txt:4774:spurz
PHD_mackenzie.txt:4627:spul [spwl] spleen.
PHD_mackenzie.txt:4631:spurz [·splz I P ·<spwrz, N sipurz] spleen.
PHD_mackenzie.txt:7628:  sorcerer Jadug.                       spleen spul, spurz.
PHD_mackenzie.txt:8926:spul                       '\\Q)..U
PHD_mackenzie.txt:8955:spurz                    ~o.).U          sped.diir            \..o~G.U'

=== HRN spurz/sipurz ===
6156:702. supurz Milz', uspurz.
6172:aw. spereza- 'Milz' (ZPGl.) ; pblv. spärz; ai. pWidn-
6173:*Milz\

=== HUB ===
2565:siipul *Milz* (Miller p. 80).
5031:spurtand d. i. paz. spurd and Gl. and Ind. 156); supurz *Milz'
6087:ustun - sutun 'Saule' ; ustor = sutor *Ross'; uspurz = supurz
6088:'Milz'; usruh *Blei* = surh (aiis "^suruh), g. suroh^ afgh. bal.
6101:fem. 'Pflugschar; supurz 'Milz* = zd. spereza; supus, supus- 173 —
6292:sipardan *auf etwas treten' H. 701; supurz *Milz H. 702;
7812:supurz 'Milz' = zd. spereza, skr. pllhan-; supar 'Pflug =
7899:Ap. r^ = iran. r;2 = np. rz: supirz Milz* {g^h) =
```


## [2026-09-14T02:30:56.057Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\ndef leafof(path,target):\n    t=open(path,encoding='utf-8',errors='replace').read()\n    lines=t.split('\\n')\n    return '\\n'.join(lines[:target]).count('\\f'), t.split('\\f')\nl,leaves=leafof('HRN.txt',6156)\nprint('HRN line 6156 leaf',l,'-> printed', l-21)\nprint(leaves[l][:600])\nprint('=======BRT=======')\nl2,lv2=leafof('BRT.txt',27019)\nprint('BRT line 27019 leaf',l2)\nprint(lv2[l2][:300])\nnums=re.findall(r'(?<!\\d)(1[0-9]{3})(?!\\d)', lv2[l2])\nprint('nums',nums[:20])\nEOF"
}
```


### [2026-09-14T02:30:57.278Z] TOOL RESULT

```
HRN line 6156 leaf 176 -> printed 155
— 155 —
Also zu aw. [/^spas'y spast/eiti *spälien'? Sehr un-
sicher, Hübschmann, Armen. Stud., S. 50, No. 257^).
699. »ipah *Heer , sipeh^ ispeh\hed (arab. isbah[hu(/), jüd.-
pers. HNDID (Is. 13, 4).
ap. Ta/ma]späda- ; aw. spaöa- *Heer ; phlv. späh,
spühpat, arm. LW. späh, aspalmhet-),
oss. d. t. afsady t. ä/sud grosse Menge, xVbteilung
von Personen, Heer, Regiment* (40).
700. sljßer, isper *Schild'.
ap. anaoa^ßdgai' oi ye()()0(p6(}0i Hesyeh ; aw. spüra-
'Schild* in sparö.\dästa' ; phlv. spar (Men.); skr. phara-,
phalaka- (Mbh.) 'SchikV, daneben LW. sphara-^spharaka-
(Nöldeke, Monatsber. BAW. 
=======BRT=======
BRT line 27019 leaf 884
neuestens  wieder  '.  dam  verstehen  konnten, ipjHia-  von  lit.  saifiUas,  ksl.  svftä  losiu- reissen,  ist  mir  nicht  begreiflich.  Wenn  dem awest.  spinia-  eine  andre  Bedeutung  als  'heilig' inkommen  sollte,  so  mijssie  es  eine  Bedeu- lungsverschiebung  oder  eine  Umdeutung  er- 
nums ['1624', '1362']
```


## [2026-09-14T02:31:05.002Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('BRT.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i in range(880,890):\n    nums=re.findall(r'(?<!\\d)(1[5-7]\\d\\d)(?!\\d)', leaves[i])\n    print(i, nums[:10])\nprint('---- leaf 884 around spereza ----')\nL=leaves[884]\nj=L.find('sp^razan')\nprint(L[max(0,j-1500):j+800])\nEOF"
}
```


### [2026-09-14T02:31:06.123Z] TOOL RESULT

```
880 []
881 ['1561', '1618']
882 ['1620']
883 []
884 ['1624']
885 ['1626']
886 ['1637']
887 []
888 ['1631']
889 []
---- leaf 884 around spereza ----
inyav-  Adj.  'dem  heiligen
Geist  entstammt,  zur  Schöpfung  des  heiligen Geists  gehörig':  kat  ial  dqma  anrS.main' yava  ailatfAqm  dämanqm  . .  Aazavra/a •yus'l  (näml.  dqma;  IP.  als  APn.)''/iiift'.- jasaiti  V.  13. 5.
Ableit.  zu  spmIS  maiityu} [HS.).  —  Pü,;  ^nak minök.  —  «)  NA.  'yüm,  s.  aber^die  Var.  und V.  13.  1.  —  >)  Vgl.  10  aoröjnainyav  No.  1.
•  j.  spsntö.mainyava-  Adj.  'dem  heiligen Geist  entstammt,  zur  Schöpfung  des  heiligen Geists  gehörig':  vlspanam  'yavanqm  spa- aiiranqm   \.  13.16;   —  a^jfanfymaii&yB
dby  Google
i6»3
"spvnti
spitay-
1624
'yavanam  damanqm  V.  j,  so;  —  kqi  tal äqtna  'yava  (statt  NSn.)'>  altanhqtn  ääma- nqm  V.  13.  \;  —  a/tal  tl  vayS  yasamatde yat  tl  asti  'yaom  Y.  25.  5 ;  —  t>m  vafmÜt . .  'yaom  Yt  jj.  42;  —  upa  ave  siarS  ySi 'yava  ¥1-/2.32;  —  stärqmca  'yavanam dsmanam  Y.i.ii.
Abieil  in  ifitn/i  mainyal  (NS.>  —  Pu,t  sfien3i mtnäk,  S&.  (lU  Y.  /):  ifianämanhsj-f/ih,  etl.:  I hermijdena  s^!lah.  —  ■)  Vgl,  in  aiirS.main- yatia-  No.  I.
•  }.yai  tÜrS  tarS.d»nänO . .  "aatara  spanti" ratufrU  N.  lOJ.
Pä.:  Aaiar  j  . .  pa  ham  haiatün  kam  därend; vgl.  dam-  No.  9.
g.  sfhrval  Y.  J/.  a  I ;  s.  ispä:
•  g.  sp»rad-  £  "Eifer':  tJm  tX  vS  *'da'^ *mvar3ni(Sp.  1362  m.)  Y.5J.4.
Zum  «i.  V.  ifidrMa/t.  —  d.  j//rf-i-  f.  'certa- men'.  —  Pü.;  ösfiurri,  Sü.:  fiarifiirriali.  — ")  So  Pt4,  Ja;  NA.  tpiridäni  vat*,
•  j,  sp^razan-  m.  "Milz':  'm  F.jg.
np,  supurz  •),  —  Pü. :  j;^«»-:  (in  Aw.-Bachst.).  — >}  Das  Verhällni*  zu  fti.  ptihän-  m.,  g
```


## [2026-09-14T02:31:17.904Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nls data/verification/sources/ ; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'));print(json.dumps(d['SNS'],ensure_ascii=False,indent=1))\""
}
```


### [2026-09-14T02:31:19.067Z] TOOL RESULT

```
MISSING_REFERENCES.md
refs
refs_online.json
SOURCE_MATRIX.md
web
{
 "title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/VajnameShayest",
 "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt"
 ],
 "page_offset": "242 leaves; page offset not determined (OCR too poor to read printed numbers) — locate by transliteration then read the page image",
 "covers_etymology": true,
 "notes": "OCR quality is POOR: Persian text mostly garbage, Latin transliterations partially readable. Verification will usually need the page image."
}
```


## [2026-09-14T02:31:24.759Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\ngrep -ho '\"refs\": \"[^\"]*SNS[^\"]*\"' data/extracted/batch/*.json | sort | uniq -c | sort -rn | head -20\necho \"--- langs with SNS ---\"\npython3 - <<'EOF'\nimport json,glob,collections\nc=collections.Counter()\nfor f in glob.glob('data/extracted/batch/*.json'):\n    d=json.load(open(f))\n    for e in d.get('entries',[]):\n        for n in e.get('nodes',[]):\n            r=n.get('refs') or ''\n            if 'SNS' in r: c[n.get('lang')]+=1\n        r=e.get('root',{}).get('refs') or ''\n        if 'SNS' in r: c['ROOT:'+e['root'].get('lang','')]+=1\nprint(c.most_common(20))\nEOF"
}
```


### [2026-09-14T02:31:26.051Z] TOOL RESULT

```
      3 "refs": "SNS:6"
      3 "refs": "SNS:36"
      3 "refs": "SNS:147"
      2 "refs": "SNS:74"
      2 "refs": "SNS:35"
      2 "refs": "SNS:192"
      2 "refs": "SNS:168; BQT:1063"
      2 "refs": "SNS:148"
      2 "refs": "SNS:117"
      2 "refs": "POK:849; SNS:137"
      2 "refs": "POK:842; SNS:267; IEC:1351"
      2 "refs": "POK:842; SNS:267"
      2 "refs": "BQT; HUB:39; SNS:133"
      1 "refs": "SYN:290; WLD:331; SNS:150"
      1 "refs": "SYN:1051; SNS:90"
      1 "refs": "SNS:98"
      1 "refs": "SNS:96,106,107; MON:476"
      1 "refs": "SNS:6; BQT:61; MON:91"
      1 "refs": "SNS:67"
      1 "refs": "SNS:59; HRN:110"
--- langs with SNS ---
[('Pahlavi', 74), ('Persian', 61), ('Avestan', 22), ('Sanskrit', 6), ('ROOT:Avestan', 3), ('Avestan / Old Persian', 2), ('Old Persian', 2), ('Armenian', 1), ('ROOT:Pahlavi', 1), ('Arabic', 1)]
```


## [2026-09-14T02:31:34.724Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SNS plihan/spurz ===\"; grep -n -i \"plihan\\|pl.h.n\\|spurz\\|sp.r.z\" SNS.txt SNS_pages.txt | head -20\necho; echo \"=== KLN spleen ===\"; grep -n \"^spleen\" KLN_1966.txt KLN_1971.txt | head\necho; echo \"=== IEC spleen ===\"; grep -n \"spleen\" IEC.txt | head -10\necho; echo \"=== SYN spleen ===\"; grep -n -i \"spleen\" SYN.txt | head -6"
}
```


### [2026-09-14T02:31:34.845Z] TOOL RESULT

```
=== SNS plihan/spurz ===
SNS_pages.txt:7334:                                                                                                           iUlja A*. 1>M U o-l^l^iSLi^ljl^j JUi"-j -:spurz:
SNS_pages.txt:7339:                                                                                                                      Uii/&.1623)'pllhan-:                        i^ ^» sparazan-
SNS_pages.txt:15112:                         sparazan- 176/5                   hacfaoxta- 2/17          hu-raata- 73/10
SNS_pages.txt:15866:                                                         spurz 176/3                       stSr 178/17-181/19
SNS.txt:10789:£ iUl ja A*. 1>M U o-l^l^iSLi^ljl^j JUi"-j Jtf -:spurz: £^10).a* 
SNS.txt:10791:Uii/&.1623)'pllhan-: i ^ t5 ^» sparazan- : t- 
SNS.txt:29055:sparazan- 176/5 
SNS.txt:31439:spurz 176/3 

=== KLN spleen ===
KLN_1971.txt:21045:spleen*. 
KLN_1971.txt:137443:spleen’ (see spleen), and -itis, a suff. of Greek 
KLN_1971.txt:229305:spleen, n. — Fr. OF. esplen or directly fr. L. splen , 
KLN_1971.txt:229373:spleen and adj. suff. -ic. 
KLN_1971.txt:229391:spleen. 
KLN_1971.txt:229425:spleen, G. spleiflen , ‘to split’, and prob. also to 
KLN_1966.txt:36331:spleen,  n.  —  Fr.  OF.  esplen  or  directly  fr.  L.  splen, fr.  Gk.  aTtXfjV.  which  stands  for  *ct7tXt]yx  and  is rel.  to  <77rXxvy  va,  ‘the  inward  parts’  (see  splanch¬ nic),  and  cogn.  with  OI.  plihdn-,  Avestic  spsrlzan (for  *splgh-en),  Arm.  p‘aicain,  L.  lien,  OSlav. slilzena  (perh.  for  *selgh-ena),  Lith.  bluznis, bluzne,  OPruss.  blusne  (the  Baltic  forms  are prob.  dissimilated  fr.  *blunlnis,  fr.  I.-E.  *blngh-), OIr.  selg,  MBret .felc'h  (for  *spelgha-),  ‘spleen’. Cp.  Asplenium,  lienal,  lienculus.

=== IEC spleen ===
962:blu- “an intestine" (?) E pluck ‘intestines of game’; Li. cf. blužnis, iés ‘spleen’; OPr. bluzne, id.
16781:‘spleen’. (Cons. and vowels anomalous. Prob. a cpd.) Skt. cf. plihan, m.; Av. sporozn; Per. supurz; Arm. pajcayn, gs: pajceyan; Gk. splén, gs: splénós, m. id. beside a-splenion *spleenwort'; splágkhnon, n. “bowel'; Lat. lien & lienis, gs. id. m. ‘spleen’; MIr. selg, Ir. sealg & seilg, f. id. beside seabhag, m. (sic), id.; Br. felch, m. id.; OCS slezena, f.; OCz. slezeň, m., R sele- zën-ka, f. id.
17418:strügh- ‘gall, poison? Gk. strükhnon, m. (a solanum-plant); ON strügr, m. “bile, spleen’; Srb. cf. srž, f. (2) ‘pus’; (isophonic: Li. strügas, striügas, adj. "short?

=== SYN spleen ===
27501:Many parts of the body or bodily ac- tions are associated with emotions. Notably the heart, the words for which are universally used to denote the seat of emotion or ‘temperament, disposi- tion’, and in part (alone or in derivs. or cpds.) for special emotions such as ‘courage’, ‘fondness, love’, ‘sympathy, pity’, and (in Balto-Slavic) ‘anger’. Bristling of the hair may indicate ‘hor- ror’ (Lat. horror; cf. NE adj. hatr-razs- ing) or pleasurable excitement, ‘joy’ (Skt. harsa-, 16.22). To lower or wrinkle the eyebrows, ‘frown, scowl’, usually shows displeasure, but also arrogance (cf. numerous Grk. phrases with é¢pts, LS s.v.; NE. supercilious). Not only tears but also downcast eyes indicate ‘srief, sadness’ (NG xarn¢is ‘sad’, 16.36). Laughter may show pleasure or ridicule. Puffing out’ the chest suggests ‘pride’ (cf. NG kapapdvw etc., 16.48), as does also strutting or a stiff bearing. Words for ‘breath’ are the most common source of those for ‘soul, spirit’, and heavy breath- ing may indicate ‘hate’ (OE anda, 16.41) or ‘anger’ (Lett. dusmas, 16.42). The bile or gall is associated with bitter anger (Grk. xédos, 16.42; NE gall in U.S. slang ‘excessive assurance, impu- dence’; cf. also Grk. pedayxonia ‘black gall, melancholy’; the spleen with a variety of quite disparate emotions (NED s.v. spleen). A Greek word for the principal internal organs (orAayxva) was felt as the seat of various emotions (ef. LS s.v.), and later, through its use in the LXX and NT to translate a cer- tain Hebrew word and rendered in our
```


## [2026-09-14T02:31:47.630Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\ndef pageinfo(path,target,pat=r'(?<!\\d)(\\d{3,4})(?!\\d)'):\n    t=open(path,encoding='utf-8',errors='replace').read()\n    lines=t.split('\\n'); leaf='\\n'.join(lines[:target]).count('\\f')\n    leaves=t.split('\\f')\n    return leaf, re.findall(pat, leaves[leaf])[:12]\nprint('KLN_1966 spleen', pageinfo('KLN_1966.txt',36331))\nprint('IEC spleen root', pageinfo('IEC.txt',16781))\nEOF"
}
```


### [2026-09-14T02:31:48.996Z] TOOL RESULT

```
KLN_1966 spleen (792, ['1804', '1754', '1827', '0865', '1743', '1822', '1800', '777', '7770', '777'])
IEC spleen root (691, ['602', '667', '660', '680', '660', '680', '1253', '659', '1254'])
```


## [2026-09-14T02:31:50.639Z] TOOL CALL #31: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && pdftoppm -f 467 -l 467 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg467 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/"
}
```


### [2026-09-14T02:31:52.861Z] TOOL RESULT

```
total 26000
drwx------ 3 sfmqrb sfmqrb   12288 Sep 13 22:31 .
drwx------ 4 sfmqrb sfmqrb    4096 Sep 13 20:49 ..
-rw-rw-r-- 1 sfmqrb sfmqrb   92443 Sep 13 21:13 391-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb  129993 Sep 13 21:11 394hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   21316 Sep 13 21:11 394-zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb   44712 Sep 13 21:14 400-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  116049 Sep 13 21:14 400-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   99858 Sep 13 21:16 404-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   91913 Sep 13 21:18 411-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   34177 Sep 13 21:23 412-zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb   79667 Sep 13 21:24 414-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  110116 Sep 13 21:31 417hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   88133 Sep 13 21:31 417-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   12361 Sep 13 21:31 417-zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb   45082 Sep 13 21:33 421-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   96996 Sep 13 21:38 428hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   18073 Sep 13 21:38 428-zoom2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   21962 Sep 13 21:38 428-zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb  112884 Sep 13 21:41 429hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   16099 Sep 13 21:41 429-zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb   96248 Sep 13 21:43 431-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   94911 Sep 13 21:46 432-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  115297 Sep 13 21:42 436-full.png
-rw-rw-r-- 1 sfmqrb sfmqrb  125916 Sep 13 22:14 440-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb  119070 Sep 13 22:18 442hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   32445 Sep 13 22:18 442-zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb   99953 Sep 13 22:12 444hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   18325 Sep 13 22:12 444-zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77093 Sep 13 22:10 445-mid.png
-rw-rw-r-- 1 sfmqrb sfmqrb  115375 Sep 13 22:12 446-full.png
-rw-rw-r-- 1 sfmqrb sfmqrb  113997 Sep 13 22:18 450hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   21276 Sep 13 22:18 450-zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb   85759 Sep 13 22:19 454-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb  114246 Sep 13 22:16 457hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   17873 Sep 13 22:16 457-zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1227534 Sep 13 21:24 afm74-420.png
-rw-rw-r-- 1 sfmqrb sfmqrb  908713 Sep 13 21:23 afm76-421.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2451 Sep 13 22:28 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    4868 Sep 13 21:29 ahd430.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   46904 Sep 13 21:10 beekes410.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    1158 Sep 13 21:33 bqt1328-ftr-437.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1151 Sep 13 21:33 bqt1328-hdr-437.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1872 Sep 13 21:33 bqt1328-top-437.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3114 Sep 13 21:33 bqt1330-top-437.png
-rw-rw-r-- 1 sfmqrb sfmqrb     146 Sep 13 22:00 bqt1-440.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  309946 Sep 13 21:35 bqt2123-fn-435.png
-rw-rw-r-- 1 sfmqrb sfmqrb   95654 Sep 13 20:53 bqt390_436_foot.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   34040 Sep 13 20:54 bqt390_436_top.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  124665 Sep 13 20:53 bqt390_662_foot.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   93636 Sep 13 20:53 bqt390_662_top.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  537986 Sep 13 20:53 bqt390_n436.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  527696 Sep 13 20:53 bqt390_n662.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  267233 Sep 13 22:02 bqt439-l254.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  171966 Sep 13 22:31 bqt469-n486-bottom.png
-rw-rw-r-- 1 sfmqrb sfmqrb  620205 Sep 13 22:31 bqt469-n486.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   13019 Sep 13 22:31 bqt469-n486-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   21513 Sep 13 21:39 build2-434.py
-rw-rw-r-- 1 sfmqrb sfmqrb   19296 Sep 13 21:42 build3-434.py
-rw-rw-r-- 1 sfmqrb sfmqrb   66340 Sep 13 21:06 build-389.py
-rw-rw-r-- 1 sfmqrb sfmqrb   60725 Sep 13 21:08 build-390.py
-rw-rw-r-- 1 sfmqrb sfmqrb   66850 Sep 13 21:11 build-391.py
-rw-rw-r-- 1 sfmqrb sfmqrb   67328 Sep 13 21:13 build393.py
-rw-rw-r-- 1 sfmqrb sfmqrb   65361 Sep 13 21:10 build-394.py
-rw-rw-r-- 1 sfmqrb sfmqrb   53331 Sep 13 21:06 build-395.py
-rw-rw-r-- 1 sfmqrb sfmqrb   49820 Sep 13 21:12 build-396.py
-rw-rw-r-- 1 sfmqrb sfmqrb   61718 Sep 13 21:06 build-398.py
-rw-rw-r-- 1 sfmqrb sfmqrb   55842 Sep 13 21:13 build-400.py
-rw-rw-r-- 1 sfmqrb sfmqrb   56563 Sep 13 21:13 build-401.py
-rw-rw-r-- 1 sfmqrb sfmqrb   45908 Sep 13 21:12 build-405.py
-rw-rw-r-- 1 sfmqrb sfmqrb   52807 Sep 13 21:06 build-406.py
-rw-rw-r-- 1 sfmqrb sfmqrb   63772 Sep 13 21:13 build-407.py
-rw-rw-r-- 1 sfmqrb sfmqrb   44609 Sep 13 21:22 build-412.py
-rw-rw-r-- 1 sfmqrb sfmqrb   55188 Sep 13 21:23 build-414.py
-rw-rw-r-- 1 sfmqrb sfmqrb   53220 Sep 13 21:24 build-415.py
-rw-rw-r-- 1 sfmqrb sfmqrb   76184 Sep 13 21:30 build-417.py
-rw-rw-r-- 1 sfmqrb sfmqrb   56437 Sep 13 21:35 build-418.py
-rw-rw-r-- 1 sfmqrb sfmqrb   55739 Sep 13 21:45 build-419.py
-rw-rw-r-- 1 sfmqrb sfmqrb   59029 Sep 13 21:41 build-422.py
-rw-rw-r-- 1 sfmqrb sfmqrb   56950 Sep 13 21:42 build-425.py
-rw-rw-r-- 1 sfmqrb sfmqrb   63145 Sep 13 21:40 build-426.py
-rw-rw-r-- 1 sfmqrb sfmqrb   53942 Sep 13 21:37 build-428.py
-rw-rw-r-- 1 sfmqrb sfmqrb   66449 Sep 13 21:40 build-429.py
-rw-rw-r-- 1 sfmqrb sfmqrb   52975 Sep 13 21:39 build-430.py
-rw-rw-r-- 1 sfmqrb sfmqrb   56759 Sep 13 21:42 build-431.py
-rw-rw-r-- 1 sfmqrb sfmqrb   21413 Sep 13 21:37 build-434.py
-rw-rw-r-- 1 sfmqrb sfmqrb   50426 Sep 13 21:45 build-435.py
-rw-rw-r-- 1 sfmqrb sfmqrb   61435 Sep 13 21:55 build-438.py
-rw-rw-r-- 1 sfmqrb sfmqrb   71845 Sep 13 22:16 build-439.py
-rw-rw-r-- 1 sfmqrb sfmqrb   65194 Sep 13 22:13 build-440.py
-rw-rw-r-- 1 sfmqrb sfmqrb   61144 Sep 13 22:11 build-444.py
-rw-rw-r-- 1 sfmqrb sfmqrb   55607 Sep 13 22:10 build-445.py
-rw-rw-r-- 1 sfmqrb sfmqrb   65723 Sep 13 22:11 build-446.py
-rw-rw-r-- 1 sfmqrb sfmqrb   52352 Sep 13 22:17 build-447.py
-rw-rw-r-- 1 sfmqrb sfmqrb   42400 Sep 13 22:13 build-448.py
-rw-rw-r-- 1 sfmqrb sfmqrb   57147 Sep 13 22:17 build-450.py
-rw-rw-r-- 1 sfmqrb sfmqrb   60619 Sep 13 22:15 build-452.py
-rw-rw-r-- 1 sfmqrb sfmqrb   86059 Sep 13 22:16 build-453.py
-rw-rw-r-- 1 sfmqrb sfmqrb   76125 Sep 13 22:18 build-454.py
-rw-rw-r-- 1 sfmqrb sfmqrb   80202 Sep 13 22:19 build-455.py
-rw-rw-r-- 1 sfmqrb sfmqrb   35780 Sep 13 22:11 build-458.py
-rw-rw-r-- 1 sfmqrb sfmqrb    2291 Sep 13 20:56 c404-empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77003 Sep 13 21:01 c404-greek.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4255 Sep 13 20:56 c404-patil.png
-rw-rw-r-- 1 sfmqrb sfmqrb   34837 Sep 13 20:57 c404-pest.png
-rw-rw-r-- 1 sfmqrb sfmqrb   46825 Sep 13 20:57 c404-symp2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   34820 Sep 13 20:56 c404-symp.png
-rw-rw-r-- 1 sfmqrb sfmqrb   35928 Sep 13 21:11 c412_cedar.png
-rw-rw-r-- 1 sfmqrb sfmqrb   42397 Sep 13 21:11 c412_makrome.png
-rw-rw-r-- 1 sfmqrb sfmqrb   81867 Sep 13 21:12 c412_makrome_zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb   54838 Sep 13 21:11 c412_meqrameh.png
-rw-rw-r-- 1 sfmqrb sfmqrb   62842 Sep 13 21:12 c412_meq_zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4665 Sep 13 21:12 c412_sedr_zoom2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   35561 Sep 13 21:12 c412_sedr_zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb   35749 Sep 13 22:05 c442-fa8b.png
-rw-rw-r-- 1 sfmqrb sfmqrb   26067 Sep 13 22:05 c442-fa8c.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5703 Sep 13 22:04 c442-fa8.png
-rw-rw-r-- 1 sfmqrb sfmqrb   17003 Sep 13 22:05 c442-samavar2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   14614 Sep 13 22:05 c442-samavar3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2377 Sep 13 22:04 c442-samavar.png
-rw-rw-r-- 1 sfmqrb sfmqrb   38593 Sep 13 22:06 c442-symp-zoom2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   67256 Sep 13 22:05 c442-symp-zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3627 Sep 13 20:54 crop14-394.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4873 Sep 13 20:54 crop18-394.png
-rw-rw-r-- 1 sfmqrb sfmqrb   11820 Sep 13 21:11 crop411_a.png
-rw-rw-r-- 1 sfmqrb sfmqrb    8609 Sep 13 21:11 crop411_b.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4088 Sep 13 21:11 crop411_c.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5339 Sep 13 21:28 crop419_a.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5380 Sep 13 21:28 crop419_b.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1676 Sep 13 21:28 crop419_c.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4192 Sep 13 21:28 crop419_d.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3506 Sep 13 21:29 crop419_grk.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4444 Sep 13 21:29 crop419_skt.png
-rw-rw-r-- 1 sfmqrb sfmqrb   25580 Sep 13 21:26 crop428a.png
-rw-rw-r-- 1 sfmqrb sfmqrb    6915 Sep 13 21:26 crop428b.png
-rw-rw-r-- 1 sfmqrb sfmqrb   54756 Sep 13 21:26 crop428c.png
-rw-rw-r-- 1 sfmqrb sfmqrb   48027 Sep 13 21:26 crop428d.png
-rw-rw-r-- 1 sfmqrb sfmqrb   12740 Sep 13 21:36 crop-437.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5500 Sep 13 22:30 crop460-latin.png
-rw-rw-r-- 1 sfmqrb sfmqrb   18309 Sep 13 22:31 crop460-mithere.png
-rw-rw-r-- 1 sfmqrb sfmqrb    6433 Sep 13 22:31 crop460-shamunhdr.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3606 Sep 13 22:30 crop460-shamun.png
-rw-rw-r-- 1 sfmqrb sfmqrb   44719 Sep 13 21:39 e0-434.json
-rw-rw-r-- 1 sfmqrb sfmqrb   20203 Sep 13 20:57 edit_about.py
-rw-rw-r-- 1 sfmqrb sfmqrb    6853 Sep 13 21:12 edit_research.py
drwxrwxr-x 2 sfmqrb sfmqrb    4096 Sep 13 21:14 ffprof
-rw-rw-r-- 1 sfmqrb sfmqrb   49815 Sep 13 21:44 gen-420.py
-rw-rw-r-- 1 sfmqrb sfmqrb 1434288 Sep 13 21:31 irn-425.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb  200105 Sep 13 21:31 irn-425.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  929137 Sep 13 22:03 kent2-448.txt
-rw-rw-r-- 1 sfmqrb sfmqrb     146 Sep 13 22:03 kent-448.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  944060 Sep 13 21:57 knt-440.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  944060 Sep 13 21:58 knt443.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   45281 Sep 13 21:58 meta-443-knt.json
-rw-rw-r-- 1 sfmqrb sfmqrb  120893 Sep 13 20:58 pg390b.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   39607 Sep 13 20:58 pg390b.png
-rw-rw-r-- 1 sfmqrb sfmqrb   55136 Sep 13 20:50 pg390.png
-rw-rw-r-- 1 sfmqrb sfmqrb  113843 Sep 13 20:57 pg391big.png
-rw-rw-r-- 1 sfmqrb sfmqrb   18836 Sep 13 20:57 pg391crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb   81140 Sep 13 20:57 pg391.png
-rw-rw-r-- 1 sfmqrb sfmqrb   34659 Sep 13 20:58 pg391root.png
-rw-rw-r-- 1 sfmqrb sfmqrb   21174 Sep 13 20:58 pg391sog.png
-rw-rw-r-- 1 sfmqrb sfmqrb   75438 Sep 13 20:56 pg392.png
-rw-rw-r-- 1 sfmqrb sfmqrb  101976 Sep 13 20:57 pg393.png
-rw-rw-r-- 1 sfmqrb sfmqrb  145431 Sep 13 20:54 pg394hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   96039 Sep 13 20:53 pg394.png
-rw-rw-r-- 1 sfmqrb sfmqrb   72433 Sep 13 20:54 pg397.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77067 Sep 13 20:55 pg398.png
-rw-rw-r-- 1 sfmqrb sfmqrb   85891 Sep 13 21:00 pg399-crop1.png
-rw-rw-r-- 1 sfmqrb sfmqrb   45417 Sep 13 21:00 pg399-greek.png
-rw-rw-r-- 1 sfmqrb sfmqrb   64776 Sep 13 20:54 pg399.png
-rw-rw-r-- 1 sfmqrb sfmqrb   43498 Sep 13 21:00 pg399-sog.png
-rw-rw-r-- 1 sfmqrb sfmqrb  167174 Sep 13 20:58 pg400big.png
-rw-rw-r-- 1 sfmqrb sfmqrb   24547 Sep 13 20:58 pg400_fa_heli.png
-rw-rw-r-- 1 sfmqrb sfmqrb   23086 Sep 13 20:58 pg400_fr2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   14689 Sep 13 20:58 pg400_french.png
-rw-rw-r-- 1 sfmqrb sfmqrb   32600 Sep 13 20:58 pg400_kasak2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   35662 Sep 13 20:58 pg400_kasak3.png
-rw-rw-r-- 1 sfmqrb sfmqrb   22852 Sep 13 20:58 pg400_kasak.png
-rw-rw-r-- 1 sfmqrb sfmqrb   79028 Sep 13 20:57 pg400.png
-rw-rw-r-- 1 sfmqrb sfmqrb   70671 Sep 13 21:01 pg402.png
-rw-rw-r-- 1 sfmqrb sfmqrb  136264 Sep 13 20:56 pg404hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   71542 Sep 13 20:56 pg404.png
-rw-rw-r-- 1 sfmqrb sfmqrb   63962 Sep 13 20:58 pg405.png
-rw-rw-r-- 1 sfmqrb sfmqrb   63610 Sep 13 20:57 pg406.png
-rw-rw-r-- 1 sfmqrb sfmqrb   79866 Sep 13 20:59 pg407.png
-rw-rw-r-- 1 sfmqrb sfmqrb   21327 Sep 13 20:55 pg408-ampus.png
-rw-rw-r-- 1 sfmqrb sfmqrb   33681 Sep 13 20:55 pg408-germ.png
-rw-rw-r-- 1 sfmqrb sfmqrb   78365 Sep 13 20:54 pg408.png
-rw-rw-r-- 1 sfmqrb sfmqrb   37449 Sep 13 21:14 pg409.png
-rw-rw-r-- 1 sfmqrb sfmqrb  100242 Sep 13 21:09 pg410hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   18557 Sep 13 21:09 pg410-k2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   17676 Sep 13 21:09 pg410-kadm2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    6217 Sep 13 21:09 pg410-kadm.png
-rw-rw-r-- 1 sfmqrb sfmqrb    7410 Sep 13 21:09 pg410-persian.png
-rw-rw-r-- 1 sfmqrb sfmqrb   65183 Sep 13 21:08 pg410.png
-rw-rw-r-- 1 sfmqrb sfmqrb   23704 Sep 13 21:09 pg410-q2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1736 Sep 13 21:09 pg410-qedam.png
-rw-rw-r-- 1 sfmqrb sfmqrb   64940 Sep 13 21:11 pg411_300.png
-rw-rw-r-- 1 sfmqrb sfmqrb   56566 Sep 13 21:10 pg411.png
-rw-rw-r-- 1 sfmqrb sfmqrb  161139 Sep 13 21:11 pg412_hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74221 Sep 13 21:11 pg412.png
-rw-rw-r-- 1 sfmqrb sfmqrb  481466 Sep 13 21:14 pg412_uhi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   35423 Sep 13 21:09 pg413.png
-rw-rw-r-- 1 sfmqrb sfmqrb   36532 Sep 13 21:12 pg414-greek.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74486 Sep 13 21:12 pg414.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3823 Sep 13 21:16 pg415-emptybox.png
-rw-rw-r-- 1 sfmqrb sfmqrb   78342 Sep 13 21:16 pg415hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   73449 Sep 13 21:11 pg415.png
-rw-rw-r-- 1 sfmqrb sfmqrb   39289 Sep 13 21:17 pg416-v.png
-rw-rw-r-- 1 sfmqrb sfmqrb   55756 Sep 13 21:17 pg417.png
-rw-rw-r-- 1 sfmqrb sfmqrb  178105 Sep 13 21:15 pg418hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   87213 Sep 13 21:15 pg418.png
-rw-rw-r-- 1 sfmqrb sfmqrb   28628 Sep 13 21:15 pg418-raj2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   13818 Sep 13 21:15 pg418-raj3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    6734 Sep 13 21:15 pg418-rajidan.png
-rw-rw-r-- 1 sfmqrb sfmqrb  114625 Sep 13 21:28 pg419_hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   79366 Sep 13 21:26 pg419.png
-rw-rw-r-- 1 sfmqrb sfmqrb   72677 Sep 13 21:27 pg420b.png
-rw-rw-r-- 1 sfmqrb sfmqrb   66620 Sep 13 21:27 pg420.png
-rw-rw-r-- 1 sfmqrb sfmqrb   31408 Sep 13 21:27 pg421.png
-rw-rw-r-- 1 sfmqrb sfmqrb   66285 Sep 13 21:29 pg422.png
-rw-rw-r-- 1 sfmqrb sfmqrb   66328 Sep 13 21:27 pg423.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74989 Sep 13 21:24 pg424.png
-rw-rw-r-- 1 sfmqrb sfmqrb   67629 Sep 13 21:26 pg426.png
-rw-rw-r-- 1 sfmqrb sfmqrb  154381 Sep 13 21:26 pg428hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   61436 Sep 13 21:23 pg428.png
-rw-rw-r-- 1 sfmqrb sfmqrb    7200 Sep 13 21:23 pg429-crop1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    7703 Sep 13 21:23 pg429-crop2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4400 Sep 13 21:23 pg429-crop3.png
-rw-rw-r-- 1 sfmqrb sfmqrb  168822 Sep 13 21:23 pg429hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   78202 Sep 13 21:23 pg429.png
-rw-rw-r-- 1 sfmqrb sfmqrb   81124 Sep 13 21:24 pg431.png
-rw-rw-r-- 1 sfmqrb sfmqrb   92551 Sep 13 21:33 pg432.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74286 Sep 13 21:24 pg433.png
-rw-rw-r-- 1 sfmqrb sfmqrb   46452 Sep 13 21:28 pg435-n1.png
-rw-rw-r-- 1 sfmqrb sfmqrb   42245 Sep 13 21:28 pg435-n4.png
-rw-rw-r-- 1 sfmqrb sfmqrb   89932 Sep 13 21:28 pg435.png
-rw-rw-r-- 1 sfmqrb sfmqrb   66400 Sep 13 21:31 pg436.png
-rw-rw-r-- 1 sfmqrb sfmqrb   60815 Sep 13 21:36 pg437-437.png
-rw-rw-r-- 1 sfmqrb sfmqrb  153828 Sep 13 21:36 pg437hi-437.png
-rw-rw-r-- 1 sfmqrb sfmqrb  100480 Sep 13 21:42 pg438.png
-rw-rw-r-- 1 sfmqrb sfmqrb   82782 Sep 13 22:03 pg439.png
-rw-rw-r-- 1 sfmqrb sfmqrb   75018 Sep 13 22:03 pg440.png
-rw-rw-r-- 1 sfmqrb sfmqrb  174306 Sep 13 22:04 pg442hi-442.png
-rw-rw-r-- 1 sfmqrb sfmqrb   84851 Sep 13 22:03 pg442-p442.png
-rw-rw-r-- 1 sfmqrb sfmqrb  496661 Sep 13 22:06 pg442uhi-442.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77924 Sep 13 21:59 pg443.png
-rw-rw-r-- 1 sfmqrb sfmqrb   70076 Sep 13 21:57 pg444.png
-rw-rw-r-- 1 sfmqrb sfmqrb   24437 Sep 13 22:00 pg444-serom.png
-rw-rw-r-- 1 sfmqrb sfmqrb   19924 Sep 13 22:00 pg444-sibum.png
-rw-rw-r-- 1 sfmqrb sfmqrb   11542 Sep 13 22:00 pg445-crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74593 Sep 13 22:00 pg445.png
-rw-rw-r-- 1 sfmqrb sfmqrb   47049 Sep 13 22:03 pg446.png
-rw-rw-r-- 1 sfmqrb sfmqrb   43874 Sep 13 22:04 pg447-crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb   69608 Sep 13 22:04 pg447.png
-rw-rw-r-- 1 sfmqrb sfmqrb   75433 Sep 13 22:04 pg449.png
-rw-rw-r-- 1 sfmqrb sfmqrb  145450 Sep 13 22:01 pg450hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   11427 Sep 13 22:01 pg450-pechkam.png
-rw-rw-r-- 1 sfmqrb sfmqrb   79151 Sep 13 22:00 pg450.png
-rw-rw-r-- 1 sfmqrb sfmqrb   11602 Sep 13 22:01 pg450-shangarf.png
-rw-rw-r-- 1 sfmqrb sfmqrb   82815 Sep 13 22:05 pg451.png
-rw-rw-r-- 1 sfmqrb sfmqrb   63836 Sep 13 21:59 pg452.png
-rw-rw-r-- 1 sfmqrb sfmqrb   78966 Sep 13 21:58 pg453.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74797 Sep 13 22:01 pg454.png
-rw-rw-r-- 1 sfmqrb sfmqrb  102312 Sep 13 22:00 pg456-germ.png
-rw-rw-r-- 1 sfmqrb sfmqrb   70887 Sep 13 22:00 pg456hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   33661 Sep 13 21:58 pg456.png
-rw-rw-r-- 1 sfmqrb sfmqrb   34197 Sep 13 22:05 pg457_crop3b.png
-rw-rw-r-- 1 sfmqrb sfmqrb   21717 Sep 13 22:05 pg457_crop3c.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4990 Sep 13 22:04 pg457_crop3.png
-rw-rw-r-- 1 sfmqrb sfmqrb  144439 Sep 13 22:04 pg457hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   79186 Sep 13 22:04 pg457.png
-rw-rw-r-- 1 sfmqrb sfmqrb   43086 Sep 13 21:58 pg458.png
-rw-rw-r-- 1 sfmqrb sfmqrb   68729 Sep 13 22:30 pg459.png
-rw-rw-r-- 1 sfmqrb sfmqrb   84070 Sep 13 22:30 pg460hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   80591 Sep 13 22:30 pg460.png
-rw-rw-r-- 1 sfmqrb sfmqrb   14451 Sep 13 22:29 pg462-fa.png
-rw-rw-r-- 1 sfmqrb sfmqrb  146281 Sep 13 22:29 pg462hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   60489 Sep 13 22:29 pg462.png
-rw-rw-r-- 1 sfmqrb sfmqrb   29574 Sep 13 22:30 pg462-sog2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   20304 Sep 13 22:29 pg462-sog.png
-rw-rw-r-- 1 sfmqrb sfmqrb   62814 Sep 13 22:30 pg463-v.png
-rw-rw-r-- 1 sfmqrb sfmqrb   50604 Sep 13 22:30 pg465.png
-rw-rw-r-- 1 sfmqrb sfmqrb   18202 Sep 13 22:31 pg466-crop1.png
-rw-rw-r-- 1 sfmqrb sfmqrb   18603 Sep 13 22:31 pg466-crop2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   15010 Sep 13 22:31 pg466-crop3.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77713 Sep 13 22:31 pg466hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   53053 Sep 13 22:30 pg466.png
-rw-rw-r-- 1 sfmqrb sfmqrb   73548 Sep 13 22:31 pg467.png
-rw-rw-r-- 1 sfmqrb sfmqrb   10610 Sep 13 22:31 pg472-crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb   96623 Sep 13 22:31 pg472hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   60397 Sep 13 22:31 pg472.png
-rw-rw-r-- 1 sfmqrb sfmqrb   84381 Sep 13 22:29 pg477.png
-rw-rw-r-- 1 sfmqrb sfmqrb       0 Sep 13 22:27 queue.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  387279 Sep 13 21:13 sem410.html
-rw-rw-r-- 1 sfmqrb sfmqrb   59726 Sep 13 21:14 u_mak.png
-rw-rw-r-- 1 sfmqrb sfmqrb   49161 Sep 13 21:14 u_meq.png
-rw-rw-r-- 1 sfmqrb sfmqrb   34177 Sep 13 21:14 u_sedr.png
-rw-rw-r-- 1 sfmqrb sfmqrb   47858 Sep 13 21:06 write397.py
-rw-rw-r-- 1 sfmqrb sfmqrb   59484 Sep 13 21:11 write-402.py
-rw-rw-r-- 1 sfmqrb sfmqrb   43710 Sep 13 21:22 write409.py
-rw-rw-r-- 1 sfmqrb sfmqrb   28665 Sep 13 21:19 write410.py
-rw-rw-r-- 1 sfmqrb sfmqrb   47575 Sep 13 21:42 write436.py
```


## [2026-09-14T02:32:04.156Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nprint(len(leaves))\nfor i in range(788,796):\n    L=leaves[i]\n    # page numbers often near start/end\n    print(i,'HEAD:',repr(L[:110]))\nEOF"
}
```


### [2026-09-14T02:32:05.342Z] TOOL RESULT

```
903
788 HEAD: '. name  of  the  campanula.  See  speculum  and  -ia.\nspeculate,  intr.  v.,  to  think,  conjecture.  —  L.  '
789 HEAD: 'ModL.,  compounded of  spermato-  and  Gk.  ^o)ov,  ‘animal’.  See  zoo-, spermine,  also  spermin,  n.,  a  c'
790 HEAD: 'ument  for  meas¬ uring  blood  pressure  in  the  arteries.  —  Com¬ pounded  of  sphygmo-  and  manometer, s'
791 HEAD: ' (naut.)  — Formed  fr.  spinx,  misreading  of  Sphinx,  the name  of  a  yacht  that  carried  the  sail, sp'
792 HEAD: '  despite.\nDerivatives:  spite,  tr.  v.,  spite-ful,  adj.,  spite-ful- ly,  adv.,  spite-ful-ness,  n. spitt'
793 HEAD: 'lunderer.  —  L.  spoliator, ‘pillager,  plunderer,  spoiler’,  fr.  spoliatus,  pp.  of spoliare.  See  spoil'
794 HEAD: 'a  with  the  dimin.  suff.  -ala. See  spore  and  -ule.\nspot,  n.  —  ME.  spotte,  spot,  rel.  to  MDu.  s'
795 HEAD: 'ask’,  and  to  OE.  spurnan,  ‘to  kick  with  the  foot’ ; see  spurn  and  cp.  speer,  spoor.  It.  sp(e)r'
```


## [2026-09-14T02:32:14.381Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i in (757,759,761):\n    print(i,'HEAD:',repr(leaves[i][:150]))\nEOF\necho \"--- search for spleen in 1971 with page context ---\"\nsed -n '229300,229320p' KLN_1971.txt"
}
```


### [2026-09-14T02:32:15.569Z] TOOL RESULT

```
757 HEAD: '  shape’.  See  prec.  word  and  suff.  -oid. Derivative:  sesamoid-al,  adj.\nSesban,  n.  —  The  same  as  Sesbania.\nSesbania,  n.,  a  genus  of  '
759 HEAD: 'darkness’,  Olr.  scath,  OW.  scod, Bret,  squeut,  ‘darkness’.  Cp.  shadow  and  shed, n.  (which  is  a  doublet  of  shade).\nDerivatives:  shade,'
761 HEAD: 'cepter’,  and  to  Heb. shebhet,  Tod,  staff,  club,  scepter’,  Aram,  shibhtd. Tod,  staff’,  Ethiop.  zabata,  ‘he  beat’, shebeen,  n.,  an  unli'
--- search for spleen in 1971 with page context ---
splay, tr. v., to spread out; n., spread ; adj., spread 
out. — ME. splay en, aphetic for displayen. See 
display. For a similar aphesis cp. sport , stain, 
stress. 

spleen, n. — Fr. OF. esplen or directly fr. L. splen , 
fr. Gk. ottXyjv, which stands for *07 tXt}yx and is 
rel. to o?7tXaYX va > ‘the inward parts’ (see splanch- 
nic), and cogn. with OI. plihdn -, Avestic sp^r s zan 
(for *splgh-en). Arm. p'aicain, L. lien, OSlav. 
slezena (perh. for *selgh-ena), Lith. bluSnis , 
bluzne , OPtuss. blusne (the Baltic forms are 
prob. dissimilated fr. * blunt nis, fr. l.-E. *blngh-), 
OIr. selg, MBret. (for *spelgha -), ‘spleen’. 
Cp. Asplenium, lienal, lienculus. 

Derivatives: spleen , tr. and intr. v., spleenful , 
adj. 

splen-, form of spleno- before a vowel, 
splenalgia, n., pain in the spleen. — Medical L.,
```


## [2026-09-14T02:32:27.395Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 -c \"\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(repr(t[748][:120])); print(repr(t[438][:120]))\"\necho \"=== MON سپرز ===\"; grep -n \"سپرز\" MON_part1.txt MON_part2.txt | head -5\necho \"=== MON پینه ===\"; grep -n \"پینه\" MON_part1.txt MON_part2.txt | head -5\necho \"=== MON سار ===\"; grep -n \"سار\\b\" MON_part2.txt | head -3"
}
```


### [2026-09-14T02:32:28.596Z] TOOL RESULT

```
'ence  also Swed.  sate,  Dan.  sxde;  rel.  to  OHG.  saze,  MDu.\nseaward\nsecure\ngesaete,  ‘seat’,  OHG.  gisdyi,  MHG. '
' —  ModL.,  fr.  Gk.  eEpeauovr),  ‘a wreath  of  olive  wound  round  with  wool’,  fr. slpo q,  ‘wool’,  which  is  re'
=== MON سپرز ===
MON_part2.txt:90460:جگر» شش دل» زهره» سپرزه گرده). (اخ.) 
MON_part2.txt:90486:باطن (دل» شش؛ جکرء زهره؛ گرده» سپرزء 
MON_part1.txt:10973:اسبل: [00 (- اسپرز] (.) (عم.) سپرز» 
MON_part1.txt:10974:اسپرز» طحال. ورم بزرگی که در پهلو پدید 
MON_part1.txt:30683:مربوط به سپرز از آن استفاده می‌کردند. در 
=== MON پینه ===
MON_part1.txt:27324:پینه: (۱]۸26-6 (.) جایی در سر حمام که 
MON_part1.txt:33606:پهرو: ۲۳5 (.) وصله» پینه» دربی. 
MON_part1.txt:35833:پینه: (-)0102 (.) رقعه‌ای که سر جامه با 
MON_part1.txt:35958:پینه؛ وصله رقعه» در پی. نظم» شعر. صلحء 
MON_part1.txt:67042:ردم: ۵ [ع.] (مصم.) رخنه بستن» پینه 
=== MON سار ===
97:سامداددی» ج. عادیات» عسوادی. ساران 
539:غایت: از کثرت. به غایت: به کمال. ساره 
634:(فق.) خسارت صریح و بسیار در خرید
```


## [2026-09-14T02:32:40.770Z] TOOL CALL #35: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg467.png"
}
```


### [2026-09-14T02:32:41.359Z] TOOL RESULT

```

```


## [2026-09-14T02:32:41.354Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-14T02:32:53.910Z] TOOL CALL #36: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-14T02:32:53.916Z] TOOL RESULT

```


```


## [2026-09-14T02:32:57.517Z] TOOL CALL #37: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B3%D9%BE%D8%B1%D8%B2",
 "prompt": "Give the full Persian entry for سپرز: etymology (Middle Persian, Avestan, Proto-Iranian, PIE forms cited), meaning, and any references (Hasandust, MacKenzie, Bartholomae)."
}
```


## [2026-09-14T02:32:59.209Z] TOOL CALL #38: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%BE%DB%8C%D9%86%D9%87",
 "prompt": "Give the full Persian entry for پینه: meanings and etymology (any Middle Persian / Proto-Iranian / PIE origin given), and references."
}
```


### [2026-09-14T02:33:00.535Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-14T02:33:01.368Z] TOOL RESULT

```
# Response

Based on the provided Wiktionary content, I cannot fulfill this request. The page shown is an **Ottoman Turkish entry**, not a Persian entry. 

The only Persian reference included states: "Borrowed from Persian _سپرز_ (seporz), a variant of _اسپرز_ (esporz, 'spleen, milt')."

The document does not provide:
- Full Persian etymology with Middle Persian, Avestan, Proto-Iranian, or PIE forms
- Scholarly references to Hasandust, MacKenzie, or Bartholomae
- Detailed Persian linguistic history

To obtain the comprehensive etymological information you're seeking, you would need to access the actual Persian Wiktionary entry (فارسی) or specialized Persian etymological sources.
```


## [2026-09-14T02:33:05.767Z] TOOL CALL #39: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A7%D8%B3%D9%BE%D8%B1%D8%B2",
 "prompt": "Give the Persian entry for اسپرز: meaning and full etymology (Middle Persian, Avestan, Proto-Iranian, PIE), plus references cited."
}
```


## [2026-09-14T02:33:07.370Z] TOOL CALL #40: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B3%D8%A7%D8%B1",
 "prompt": "Give the Persian entries for سار, especially the bird sense (starling/myna): meaning and etymology (Middle Persian, Proto-Iranian, Sanskrit or Greek cognates), plus references."
}
```


### [2026-09-14T02:33:09.971Z] TOOL RESULT

```
# Persian Entry: اسپرز (esporz)

**Meaning:** Spleen or milt (anatomy term)

**Etymology:**
The word is "Inherited from Proto-Iranian *spr̥jā́." The document provides only this level of etymological detail, with no information about Middle Persian, Avestan, or Proto-Indo-European origins.

**Alternative Form:** سپرز (seporz)

**Synonym:** طحال (tahâl)

**Descendant:** The word descended into Khalaj as "ispurz"

**Note:** The Wiktionary entry contains no references section and does not cite academic sources for its etymological claims.
```


### [2026-09-14T02:33:12.538Z] TOOL RESULT

```
# Persian Entry for سار (sâr)

## Meaning
The Persian term **سار** (sâr) denotes a "starling" - specifically the common starling (*Sturnus vulgaris*).

## Etymology
The Wiktionary entry provides limited etymological depth for the Persian form. However, it notes that the Ottoman Turkish borrowing came directly from Persian, suggesting the word's Persian roots predate Ottoman adoption.

Unfortunately, the provided source does not trace the word back to Middle Persian, Proto-Iranian, or Sanskrit/Greek cognates. The entry offers pronunciation data across Persian dialects but lacks deeper historical linguistic analysis.

## References
The document lists no dedicated Persian etymological references. For comprehensive diachronic investigation of this ornithological term's path through Indo-European and Iranian language families, additional specialized etymological resources would be necessary—those extending beyond this Wiktionary entry's scope.

The term's presence across multiple language families (Arabic, Persian, Ottoman Turkish, Kohistani Shina) suggests ancient borrowing patterns, though specific etymological pathways remain undocumented in this source.
```


## [2026-09-14T02:33:19.024Z] TOOL CALL #41: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CF%88%CE%AC%CF%81",
 "prompt": "Give the Ancient Greek entry ψάρ: meaning, declension, and etymology — what origin does it give (Pre-Greek? PIE *sper-? cognates with Persian sār, Sanskrit)? Quote Beekes if cited."
}
```


## [2026-09-14T02:33:20.449Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/spider",
 "prompt": "Give the full etymology of \"spider\", including Old English spithra/spinnan and PIE root; also state which PIE root Etymonline assigns."
}
```


### [2026-09-14T02:33:24.274Z] TOOL RESULT

```
# Ancient Greek ψάρ (psār)

**Meaning:** Starling (*Sturnus vulgaris*)

**Etymology:** The word derives from Proto-Hellenic *spḗr, ultimately from Proto-Indo-European *spḗr meaning "sparrow, bird." It shares cognacy with English "sparrow."

**Declension:** Third declension masculine noun. Example forms include:
- Nominative singular: ψᾱ́ρ (psā́r)
- Genitive singular: ψᾱρός (psārós)
- Nominative plural: ψᾶρες (psâres)

**Note on Sources:** The entry cites standard lexicographical references (Liddell & Scott, Autenrieth, Bailly, and Cunliffe) but does not include commentary from Beekes or discussions of Persian or Sanskrit cognates in the provided content.
```


### [2026-09-14T02:33:26.166Z] TOOL RESULT

```
# Etymology of "Spider"

**Full Etymology Chain:**

The word "spider" originates from late 14th century Middle English *spydyr*, tracing back to Old English *spiðra*. According to Etymonline, it derives from Proto-Germanic *\*spin-thron-*, which is "etymologically 'spinner.'"

**PIE Root Assignment:**

Etymonline assigns the PIE root *\*(s)pen-*, defined as "to draw, stretch, spin." The entry states: "from PIE root *(s)pen- 'to draw, stretch, spin' + formative or agential *\*-thro."

**Cognate Evidence:**

The connection becomes clearer through related Germanic words like Middle Low German, Middle Dutch, and German *spinne*, plus Dutch *spin*—all meaning "spider." This transparent relationship to the spinning root demonstrates the semantic link between the creature and its web-making ability.

**Historical Note:**

The entry notes that "spider" was not the dominant Old or Middle English term; earlier words included *loppe*, *atorcoppe* (literally "poison-head"), and *gangewifre* ("a weaver as he goes").
```


## [2026-09-14T02:33:33.942Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/spleen",
 "prompt": "Give the full etymology of \"spleen\" (Old French/Latin/Greek chain, PIE root) and of \"sparrow\" if mentioned; quote the PIE root assigned to spleen."
}
```


## [2026-09-14T02:33:35.079Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/pound",
 "prompt": "Give the etymology of \"pound\" (unit of weight): Old English pund, Latin pondo, libra pondo, and the PIE root assigned."
}
```


### [2026-09-14T02:33:38.827Z] TOOL RESULT

```
# Etymology of "Spleen"

**Full Etymology Chain:**

The word spleen traces through Old French *esplen*, Latin *splen*, and Greek *splēn* ("the milt, spleen"), ultimately deriving from the Proto-Indo-European root.

**PIE Root:**

The assigned PIE root is "*spelghn-" meaning "spleen, milt," which also generated cognates in Sanskrit (*plihan-*), Avestan (*sperezan*), Armenian (*p'aicaln*), and various other Indo-European languages.

**Figurative Development:**

In medieval medicine, the spleen was regarded as "the seat of morose feelings and bad temper." This produced the figurative sense of "violent ill-temper" by the 1580s, spawning related adjectives like *spleenful*, *spleenatic*, and *spleeny* in the late 16th-17th centuries.

---

**Note on "Sparrow":**

The provided document contains no etymology for "sparrow," so that information cannot be supplied from this source.
```


### [2026-09-14T02:33:39.465Z] TOOL RESULT

```
# Etymology of "Pound" (Unit of Weight)

**Old English Origin:**
"Old English _pund_ 'pound' (in weight or money)...from Proto-Germanic _\*punda-_"

**Latin Source:**
The word derives from Latin _pondo_, meaning "by weight." This appears in the phrase "libra pondo" (a pound by weight), where _pondo_ functions as an ablative form of _pondus_, meaning "weight."

**PIE Root:**
The ultimate source traces to the Proto-Indo-European root **(s)pen-**, defined as "to draw, stretch, spin." The connection reflects an underlying concept: the weight of an object measured by how much it stretches a cord or balance.

This etymological chain demonstrates how the unit of weight measurement evolved from a practical, physical concept through Latin and Germanic languages into English.
```


## [2026-09-14T02:34:09.779Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== ARY latin index pine/sar/spurz ===\"; grep -n -i \"PINE\\|SAR \\|SEPORZ\\|SEPURZ\\|SIPURZ\" incoming/ARY/ARY_latin_index_pages.txt | head -20\necho; echo \"=== ARY persian ===\"; grep -n \"پینه\\|سپرز\" incoming/ARY/ARY_pages.txt | head -10\necho; echo \"=== BQT v1/v2 پینه ===\"; grep -n \"پینه\" BQT_v1_pages.txt BQT_v2_pages.txt | head -10\necho; echo \"=== BQT سار ===\"; grep -c \"سار\" BQT_v2_pages.txt"
}
```


### [2026-09-14T02:34:09.900Z] TOOL RESULT

```
=== ARY latin index pine/sar/spurz ===
296:tar 991361 goby y tyaley sib aguas glreSly tied ge Se slylo Sar cat pr
836:Scalp Sar gly Higla contd Jl anally agen a LL 5 og! 4 Sal Glatt § .
973:29 Bop ceri atl oF Gop ead Sar pp NT yp SE y 5 om chin gyal
1344:feu! Slit| PENSARE .plJls| PENSAR elilel y PENSER (541) » PENSARE
4119:BARNHART: (NOSE) 710 NASAR (OLD NORSE) oS 35
4819:OLD CHURCH SLAVIC) 4S 59%! PUS, PUSAR PAHLAVI) 5 ay
6968:tS Sib KAISAR oly) CAESAR 2 ojly Say) Jem! eel GS" aly pho oN
6969:31K gd (CAESAR Ki KAISER LIT KISAR SG TSAR yoy) CZAR ging) CESAR
7198:SYSTIR - SAR ‘(TOKHARIAN A) A 6 65
7200:(OLD HIGH GERMAN) yf al svASAR SANSKRIT) <2 Sail
7958:DIERA (SLOVAK) Splat TSAR :(TOKHARIAN A) A (5 \65
7959:DIRTI :(LITHUANIAN) .\ 3 TSAR :(TOKHARIAN B) B «5 ,\o5
9173:Sar gles 2,4 iy) SUKI 22 5s cal
9751:STARE (SWEDISH) 54 y= SAR PAHLAVI) 5 gay
10245:SAR HBALUCHI) gx sh SARAH- HAVESTAN) gles}
10246:SAR HAPGHAND (4) git SAR PAHLAVI) 65 ay
10247:SIRAS, CHIRAS (SANSKRIT) Soi SAR HOSSETIC) ue 3\
10248:SAR ARMENIAN) | SAR, SER, SEROK (KURDISH) 52,5
10287:POKORNY: 551 SARN, SAR ARMENIAN)
11442:WS Gr OS Sar 9 Ad OW 059 cal ee

=== ARY persian ===

=== BQT v1/v2 پینه ===
BQT_v1_pages.txt:3524:یج - خوزه‌تانی: پینه (۳) کودم خواره.
BQT_v1_pages.txt:4870:بیعنی آ پینه یست
BQT_v1_pages.txt:16051:را نیز کوبند - و رقعه و پینه را نیز گوین که
BQT_v1_pages.txt:18086:نهند بوقت شکافتن - و پینه را نیز گویند که‌بر
BQT_v1_pages.txt:24811:و پاره ولخت باشد -- و پینه ووصله رائیز گویند
BQT_v2_pages.txt:11119:  ‫و سله کردن کفش های کهنه وخراز بمعنی کفاش و پینه دوزاست‪.‬ه دزی ح ‪۱‬ص ‪( ۰ ۱۹۳‬امروز‬
BQT_v2_pages.txt:17174:‫باشد خوفای ها » پارچه و پینه کروایند که بر‬                                                 ‫وتعطیل کردن باشد ‪.‬‬
BQT_v2_pages.txt:31963:‫وون بشکافند‬‫بیز خوانشش‪ .‬گرم وخشك است چ‬                 ‫‪ .‬سام = بروزن لام دعالمپینهواحللام‬

=== BQT سار ===
185
```


## [2026-09-14T02:34:21.118Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BQT سار bird ===\"; grep -n \"سار\" BQT_v2_pages.txt | grep -n \"مرغ\\|پرنده\\|زرزور\" | head -10\necho; echo \"=== BQT_v3 سار ===\"; grep -n \"سار\" incoming/BQT/BQT_v3_pages.txt | grep \"مرغ\\|زرزور\" | head -10\necho; echo \"=== MON2vol سار ===\"; grep -n \"زرزور\" incoming/MON/MON_2vol_Adena_v2_djvu.txt MON_part2.txt | head -10"
}
```


### [2026-09-14T02:34:21.256Z] TOOL RESULT

```
=== BQT سار bird ===
107:31645:‫از مازدران تزديك آمل*‪ - ۱‬و نام پرنده است‬                  ‫ومعنی سارنج است که مرك سیاه‌ضعیف‌باشد‪.‬‬
169:38956:                                                                  ‫‪.‬لام پرنده‌ایست کوچك و آلرا بفارسی سار گوبند‬
170:39088:‫سارو باشد » وآن پرنده‌ایست‪ .‬سیامرنگو قطهای‬                            ‫شده‌باشد ‪ ۴‬؛ و بعضی‬    ‫دشه‬  ‫ی دم‬

=== BQT_v3 سار ===

=== MON2vol سار ===
```


## [2026-09-14T02:34:26.359Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '39080,39098p' BQT_v2_pages.txt\necho \"--- page tag ---\"\nawk 'NR<=39088 && /\\[pdf page/ {p=$0} END{}' BQT_v2_pages.txt >/dev/null\nhead -39088 BQT_v2_pages.txt | grep -o \"\\[pdf page [0-9]*\\]\" | tail -2"
}
```


### [2026-09-14T02:34:27.460Z] TOOL RESULT

```
                                                                                      ‫سوری ‪ -‬و بزم ایامعید با‬
                                           ‫ومد بنه‌اسءت ‪٩‬‏ ‪#.‬‬             ‫خاکستری بیاهی مابل‌هم هست و‪-‬اسب‌واسشس‬
                                                                      ‫انند سمند‬        ‫‌همخط‬
                                                                                           ‫یک‬‫هیند‬
                                                                                                ‫اکو‬
                                                                                                  ‫یرا‬‫سغی‬
                                                                                                       ‫ور الا‬‫خ‬
 ‫سودان ‪ ۲‬بر وزن توران» بممنی‬
‫سارو باشد » وآن پرنده‌ایست‪ .‬سیامرنگو قطهای‬                            ‫شده‌باشد ‪ ۴‬؛ و بعضی‬    ‫دشه‬  ‫ی دم‬
                                                                                                     ‫شل تا‬
                                                                                                         ‫کا ک‬
                                                                                                            ‫از‬
                               ‫صفند دارد وخوشآواز باشد‪*-‬‬              ‫اسب بآن رنه را خوب نمی‌دانندلهذا میگویند‬
                                                                      ‫ولام مرغی هم هست_‪-‬ورنگه‬                 ‫«مور ازګله دور“‬
 ‫کزف‬
   ‫»وعی ا‬
        ‫سو ‪3‬ج » بر وزن تورح ب‬                                         ‫سرخ رکافنتیهز‌الد چهگل سرخ راگل سوری‬
‫درجابیکه تردمك بدربا کوه‬                   ‫خرن باشد ‪ ۸‬وآن‬
                                                                      ‫و لاله را لالة سوریوشراب لعلی‌راشراب‌سوری ‪۴‬‬
--- page tag ---
```


## [2026-09-14T02:34:37.272Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"سپرز\\|اسپرز\" BQT_v1_pages.txt BQT_v2_pages.txt incoming/BQT/BQT_v3_pages.txt 2>/dev/null | head -10\necho \"=== v2 سار headword ===\"\ngrep -n \"‫سار\\b\\|سار ‪\" BQT_v2_pages.txt | head -10\necho \"=== HUB spurz page ===\"\npython3 -c \"\nt=open('HUB.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nfor tgt in (7812,6101,7899):\n    print(tgt,'leaf',('\\n'.join(lines[:tgt])).count('\\f'), '-> p', ('\\n'.join(lines[:tgt])).count('\\f')-10)\n\""
}
```


### [2026-09-14T02:34:38.484Z] TOOL RESULT

```
=== v2 سار headword ===
1633:                                                       ‫سار سصیاسین بینقطه بروزن‌سخت‬              ‫جش‬
3904:‫سارو باشد وآن آهك رسیده با چیز ها آیخته‬                                          ‫چاووش و شیب قافله راگوبند © ‪.‬‬
10973:                                                                                       ‫سار برزکه وعالی ‪١‬‏ ‪.‬‬
12749: ‫سار‬       ‫خطر‬   ‫و‬   ‫خوف‬   ‫آن‬   ‫خطی است که در‬      ‫و‬
13807:                                                                       ‫سار » خششار » خشتنسار ‪.‬‬
16753:   ‫چون زند برکردن گردان عمود گاوسار ‪.‬‬                                ‫چون زند بر مهرة ثیران دبوس شصت‌من‬
18236:                           ‫نیزکرنند ؛ وزبا‬                 ‫سارات‌را کویند که زحل ومشتری‌ومریخ و آفتاب‬
18939:  ‫سار | منال ودستگز ار(دستگذار)‪.‬‬         ‫نت‬           ‫ردست‬                 ‫زرای تست خرد را دلیل وباریگر‬         ‫‪۴‬‬
20010:‫سارزان ‪٩‬‏ ‪ -‬وکوهی لیز‬
21150:                                     ‫سار وياله‬
=== HUB spurz page ===
7812 leaf 229 -> p 219
6101 leaf 183 -> p 173
7899 leaf 232 -> p 222
```


## [2026-09-14T02:34:48.882Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD sar ===\"; grep -n \"^sār\\|sār \\[\\|starling\" PHD_mackenzie.txt | head -10\necho; echo \"=== NYB sar starling ===\"; grep -n \"starling\\|sār\" NYB_vol2_glossary.txt | head -10\necho; echo \"=== CHEUNG pin/pain ===\"; grep -n \"pain\\|\\*payn\" CHEUNG.txt | head -5\necho; echo \"=== SKT spleen/sparrow/span ===\"; grep -n \"^Spleen\\|^Sparrow\\|^Span\\|^Spider\\|^Spin\\b\" SKT.txt | head -10"
}
```


### [2026-09-14T02:34:49.005Z] TOOL RESULT

```
=== PHD sar ===

=== NYB sar starling ===
473:ap [MY”; ’p' 607. 787. 862.6, 878-11] water 1416-26 and passim; pl. cas. obl. āpān Dp?n'] 1095. — Av. (325 sqq.) āp-, OP āpt-; MPrthPrs ’b; Paz. āw, àv; NP ab. - V. dp-cthrak, āp-sārān, āpīk.
481:apāc-sārēh [—-s'lyh] rebellion 13%. — Paz.
482:awāž-sār ‘headstrong, rebellious, abstr. awāž-sārī SGV XI, 247-249, < apāc (1) + sār < Av. (1572) sära- = sarah- in compounds. Cf nigne-sär.
763:ütur ['twr'; inser. ’twry] fire, referring to the old Iranian fire cult: ~ yazét god Ātur 25?; ~ farröbäg, gušnasp u burzen mihr the names of the three sacred fires connected with the three classes of the old Iranian society 118, explained 27-9; ~ farröbäg, i -bag 974. 9511; ~ gusnasp 955; ~burzén mihr 95%; ~-dn šāh the head of the sacred fires 1222-23, 131; — sal 58, āturv i Artaxšahr säl 40, āturv Šahpuhr i āturān šāh sal 24 SPrs:1-3 = sar 58, ātarē Artaxéahr sar 40, ātarē Šāhēpuhr ātarūn xšāh sār 24 SPrth:1-3: ‘... of the year 58 (viz.) the year 40 (of =) after the (enthronement) fire of Artax- Sahr, the year 24 (of =) after the (en- thronement) fire of Sahpuhr, the head of the fires’, which means the year 266 A.D., v. Christensen apud Ghirshman, Rev. des arts asiatiques X, 1936, 127—128 (the year 40 reckoned from the coronation of A. in the year 226, the year 24 reckoned from the coronation of S. in the year 242, and the year 58 reckoned from what must have been the epochal year of Sassanid time-reckoning, viz. 208 A. D.). — [~ the name of the 9th day of the month, also of the 9th month of the year; dade (q.v.) pat — the name of the 8th day of the month: FrP 28.] — Av. v.s. v. ätaxs; Prth ätarö (g. v.); MPrthPrs ’dwr; Paz. ädur; NP āčar, ādar. As to the three sacred fires v. Christensen, Sass. 164— 167; cf also de Menasee, Feux (1964); Mary Boyce, BSOAS XXXI, 1968, 52- 68, 270-289.
1760:4. partitive: hac fradandan + han mart kasé anyone of the children of that man 25; hac šmāh xiönän ke hast ke ...? 25” ete.; fratom hac ax" i astomand 53%; xuastom hac z"arisnàn the most delicious of dishes 7413; ete. — 5. in comparison ‘than’: hac apārīk kanicakän āžarmīktar 422; Zarristan ke... zan-ē hac či hucihr- tar nest 259-19; hac tē veh 411; kū-š suk mas būt hac apdrik gāv 492°; more emphatically yuvattar (g. v.) hac hàn + huhömikän homtar 40°’. — 6. causative: hac hàn dušxvār sahist by this he was very much shocked 4?-?; hac hàn 1 devan sārēnišn 3774-25 : causal conj. : hac hàn cigon because 4511; hac han i with a nominal clause 48!. — 7. forming adverbs: hac pas, hac pes, hac be, hac apar (hacapar), hacadar; prepositions: pas hac, peš hac (= patiš hac 368), yuvat hac, bé hac; frame prepositions: hac. . . rād owing to 1525-26; hac .. . bérén 20%; hac . . . yuvatāk 76°. — Av. (1746 sqq.) hacé; OP haca; MPrth ^c, "Z; MPrs 'c, "z; Paz. ez (eži-ca); NP az.
2544:mēš-sār [myás?l] *'of the sheep category” = of sheep-leather: kamar % ~ 6’. — Av. (1109) mačša-, NP meš + sar < Av. (1566 sg.) !saraöa- ‘species’.
3038:patīsār [ptys']] unbroken succession: throughout, from the first to the last
3040:SGV XV, 50); NP padisdr ‘taking up and finishing any business which has already been begun’ (possibly a learned w.).— < *pattš-sār < *patisa-sära- ("head onward'') ‘continuous forward move- ment’.
3397:sardārēh chieftainship, leadership 70%. 71%. säreh [s'lyh] v. apäc-säreh. sārēnišn [s'lynšn'] instigation 372, from
3398:särenitan [s’lynytn'] to egg on, to incite, 6 to: 48°. 552%, 615. — Cf Paz. mardum yak awar dit särinom ‘I will stir up men against each other', SGV XIV, 27 (allus- sion to Isa. 19:2; misunderstood by de Menasce); BdA p. 59 hakar artik nē sārēnē ‘if thou dost not provoke war’. V. Verbum 205 and BSOAS XI, 1943, 61.

=== CHEUNG pin/pain ===
541:*-eH,, one certain example: *darH ‘to have pain’ (Lat. doleo ‘I suffer, am in pain’) 
1400:Oss. І. пуу, D. nive ‘image, drawing, painting, form’ || (+ *ui-) Oss. I. ivajyn/ivad, 
4568:fierce’. © MSogd. öx5- “о give pain, hurt’, which is often cited (e.g. Gharib 1995: 
4990:*darH ‘to have pain’ 
4992:*MIDDLE PERSIAN: MMP drd, BMP dr /dard/ ‘pain, illness’ || (+ *a-) MMP ’y’rd-, 

=== SKT spleen/sparrow/span ===
3339:Span,  xaque,  ja»iue.  Port,  xiv/ue,  C.  $chach,
7890:Span.  form.     Named  from  its  iikenesi  1
17926:Spangle.  ;E  )  M.  E,  ipanetl,  dimin.  of iMft^.  a  metal  fastening  (hence,  small uiinutg  ornament).    A.  S.  tpangt,  a  metal
17929:Spaniel.    (P.  -  Spaa.  —  L.) spaniel,   spane-yeoU.  —  O.  F.    tsfiag spaniel.   Spanisli    dog.  —  Spaa.  ^ Spanish.  —  Span     Eipaiia^ /Ihpania,  Spain.
17930:Spank,  to  slap,  move  quickl^ also   have  spatiker,  a  laige  %i animal ;    sNmking^    larj^e,    lu&tj word.  +  Low  G.  xpaJtktrrt, run  and  spring  about   quidcly. base  SPAK,   sjgnt6cnnt   of  ql Der.  spani-tr,  an  after  sail  in  aj
17931:Span-new ;  see  Spooo.
18072:Spider;  see  Spin.
18086:Spin,   to  draw  out  threads.  (E.)     A.S.
18142:Spleen.  (L.  -  GV.)  M.  E.  spUn.  « I,,  tp/m.  —  Ck.  ^rXiJi*,  the  splcen.-^Skt Plihan;  I-.  h'tn.     Der.  splcn-etic.
23408:Spanish  from  CilHt:  bravado,  gmfan dine  (gaberdine).  galUard,  garrote  (jpl rottc).
```


## [2026-09-14T02:34:58.413Z] TOOL CALL #50: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%B3%D8%A7%D8%B1/",
 "prompt": "Quote the فرهنگ معین (Mo'in) entry/entries for سار — especially any bracketed origin tag such as [په.] (Pahlavi) and the bird meaning (زرزور/starling). Also quote the دهخدا entry if it gives an etymology."
}
```


## [2026-09-14T02:35:00.883Z] TOOL CALL #51: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D9%BE%DB%8C%D9%86%D9%87/",
 "prompt": "Quote the فرهنگ معین (Mo'in) entry for پینه — the bracketed origin tag if any (e.g. [په.]) and the meanings (وصله، رقعه، سختی پوست). Also any دهخدا etymology note."
}
```


### [2026-09-14T02:35:05.783Z] TOOL RESULT

```
# Etymology of سار (sār)

## Meaning: Starling (Bird)

From **فرهنگ معین**:
- **(پ.‍)** پرنده ای است شبیه گنجشک اما بزرگتر از آن که بیشتر به شکار ملخ می پردازد
- **(This indicates Pahlavi origin)** — "a bird resembling a sparrow but larger, mostly hunting locusts"

The دهخدا lexicon describes it as "پرنده ای است سیاه و خوش آواز که خالهای سفید ریزه دارد" (a black melodious bird with fine white spots), identifying it as the **زرزور** (starling).

## Secondary Meanings

Beyond the avian reference, سار functions as a **suffix** meaning:
- **Head/leader** (in compounds like تیمسار)
- **Abundance/profusion** (as in چشمهسار — cascading spring)
- **Resemblance** (as in comparison constructions)

The word carries an ancient Indo-European or Persian root, appearing in classical Persian literature with various semantic extensions.
```


### [2026-09-14T02:35:06.351Z] TOOL RESULT

```
# پینه (Pine) - Farhang-e Mo'in Entry

**Origin tag:** (نِ) (اِ)

**Meanings:**
1. "تکه پارچه ای که بر قسمت پاره شدة جامه دوزند" — a fabric patch sewn onto torn clothing
2. "پوست کلفت و ضخیم شدة کف دست در اثر کار زیاد" — thickened skin on the palm from excessive work

**Dehkhoda etymology note:**
The word originally derives from "پی نه" (literally "placed after"), referring to something positioned sequentially—hence a patch applied to repair torn fabric or footwear.

**Additional context:**
The term also describes calluses and hardened skin that develop on hands, feet, or knees from repetitive labor or, in religious contexts, from frequent prostration during prayer.
```


## [2026-09-14T02:35:18.191Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \"https://en.wiktionary.org/wiki/اسپرز\" \"https://en.wiktionary.org/wiki/سپرز\" \"https://en.wiktionary.org/wiki/سار\" \"https://en.wiktionary.org/wiki/ψάρ\" \"https://www.etymonline.com/word/spider\" \"https://www.etymonline.com/word/spleen\" \"https://www.etymonline.com/word/pound\" \"https://abadis.ir/fatofa/سار/\" \"https://abadis.ir/fatofa/پینه/\"; do\npython3 tools/fetch_source.py \"$u\" --note \"page 467 verification (Spelgh/Spen/Sper): spleen, pineh, sar, psar etymologies\" 2>&1 | tail -2\ndone"
}
```


### [2026-09-14T02:35:25.374Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/770d4f1ef94a12dc.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6dba1ce70b4e5248.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d32e122d841cba9e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4d5d15f57ce2911d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/814a5f9f6528b708.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1fed2efb54d28954.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3d2861ad3ff90a2e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a8f53ca5a4237cf3.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/49a81a71a85e2522.txt
```


## [2026-09-14T02:35:30.147Z] TOOL CALL #53: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/spelǵʰ-",
 "prompt": "Does this reconstruction page exist? Give the PIE root for 'spleen', its gloss, and the descendants listed (Sanskrit plīhán, Avestan, Greek splēn, Latin lien, etc.)."
}
```


## [2026-09-14T02:35:31.377Z] TOOL CALL #54: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/sparrow",
 "prompt": "Give the etymology of \"sparrow\": Old English spearwa, Proto-Germanic *sparwan-, and the PIE root assigned (with any Greek/other cognates mentioned)."
}
```


### [2026-09-14T02:35:31.526Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-14T02:35:35.713Z] TOOL RESULT

```
# Etymology of "Sparrow"

**Old English Origin:**
"Middle English _sparwe_, from Old English _spearwa_" traces back through Germanic languages.

**Proto-Germanic:**
The word derives from Proto-Germanic *sparwan, which also appears in Old Norse _spörr_, Old High German _sparo_, and German _Sperling_.

**PIE Root:**
Scholars reconstruct this as coming from PIE *spor-wo-, ultimately from the root *sper- (3), which "form[s] names of small birds in Germanic, Baltic, and Greek."

**Cognates:**
Related forms include Old Prussian _spurglis_ ("sparrow"), Greek _sparasion_ (a small sparrow-like bird diminutive), _spergoulos_ (small field bird), and _psar_ (starling). The root appears across multiple Indo-European language families for naming small bird species.
```


## [2026-09-14T02:35:54.780Z] TOOL CALL #55: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E0%A4%B6%E0%A4%BE%E0%A4%B0",
 "prompt": "Give the Sanskrit entry शार (śāra): meanings and etymology. Also mention if शारि/शारिका (śāri/śārikā 'myna bird') is linked."
}
```


## [2026-09-14T02:35:57.314Z] TOOL CALL #56: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E0%A4%AA%E0%A5%8D%E0%A4%B2%E0%A5%80%E0%A4%B9%E0%A4%A8%E0%A5%8D",
 "prompt": "Give the Sanskrit entry प्लीहन् (plīhán): meaning and etymology, including the PIE root and cognates (Avestan, Greek, Latin) and any note about taboo deformation / metathesis from *splegh-."
}
```


### [2026-09-14T02:35:59.809Z] TOOL RESULT

```
Based on the provided Wiktionary page, I cannot give you the Sanskrit entry for शार (śāra) because the page only covers the **Konkani** language entry.

The page shows that शार in Konkani:
- Is "Borrowed from Classical Persian _شهر_ (šahr)"
- Means "city" with synonyms including नगर (nagar) and पाटण (pāṭaṇ)

While the page header indicates there are Sanskrit entries available (showing "संस्कृतम्" as one of 4 languages), the actual content provided does not include the Sanskrit definition or etymology. To access that information, you would need to visit the Sanskrit Wiktionary version directly.

Regarding शारि/शारिका (myna bird): **No such link appears** on this particular page excerpt.
```


### [2026-09-14T02:36:03.168Z] TOOL RESULT

```
# Sanskrit Entry: प्लीहन् (plīhán)

**Meaning:** The spleen

**Etymology:** Derived from Proto-Indo-Iranian *spliHȷ́ʰā́, which traces back to Proto-Indo-European *(s)pli(H)ǵʰḗn.

**PIE Root & Cognates:** The entry notes cognate relationships across multiple language families:
- Ancient Greek: σπλήν (splḗn), which gives English "spleen"
- Latin: lien
- Avestan: 𐬯𐬞𐬆𐬭𐬆𐬰𐬀𐬥 (spərəzan)
- Old Armenian: փայծաղն (pʻaycałn)
- Russian: селезёнка (selezjónka)
- Lithuanian: blužnis
- Persian: اسپرز (esporz)

**Note on Metathesis:** The document does not explicitly discuss taboo deformation or metathesis from *splegh-. However, the consistent retention of the "spl-" cluster across cognates suggests the etymology remained relatively stable across Indo-European languages without undergoing the phonetic rearrangement your question implies.
```


## [2026-09-14T02:36:26.340Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nL=leaves[691]\nprint('nums', re.findall(r'\\n(\\d{3,4})\\n', L)[:6])\ni=L.find(\"'spleen'. (Cons\")\nprint(repr(L[max(0,i-300):i+60]))\nEOF\necho \"=== WLD Bd2 spelgh ===\"; grep -n \"Milz\" incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt | head -5"
}
```


### [2026-09-14T02:36:27.474Z] TOOL RESULT

```
nums ['1253', '1254']
'ti, inf. save’: G sparen); OE sparian, v. ‘spare, save, ref'
=== WLD Bd2 spelgh ===
18804:aisl. milti ^Milz“ (Kluge EWb. s. v., Pick I* 517, s. aucbYf. IF. 25, IGOflf.; 
44231:sp(h)elgh(en, -a), splengh-, spligh- „Milz“. 
44235:apr. hltisne „Milz“. Uber die schwierigen Lautverhaltnisse s. die Lit. bei 
44240:Zu ahd. milzi „Milz“ (Petersson IP. 23, 158 f.) fiihrt freilich kein Weg.
```


## [2026-09-14T02:36:32.948Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '16778,16782p' IEC.txt\necho \"=== WLD page ===\"; sed -n '44225,44245p' incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt\necho \"=== WLD pages.txt tag ===\"; grep -n \"sp(h)elgh\" incoming/WLD/WLD_Bd2_pages.txt | head -3"
}
```


### [2026-09-14T02:36:33.034Z] TOOL RESULT

```
review, purview'. Cf. speK- (1) Skt. spastah, pp. & adj. ‘clear’; Av. spasta, obl: -tar, m. ‘watchman’; (LW from Iran. in) Arm. Spas, u, u, S. (service, cf. Per. sipás 'thanks- giving"), beside past, i-st. (? also an Iran. LW) “proof, reason, plea’; Tokh. cf. spaktàn, s. "ser. vice’; Gk. cf. (metath.) sképsis, f. 'considera- tion’; Lat. spectus, gs: -üs, s. ‘sight’: W ffes, m. ‘insight’, fr. *speKtis, cf. nos < *noktis or *nokts; ffesu, inf. ‘see through’; MDu. cf. spiede, spie, m. ‘spy’
(spel-, see sphel-)
spelé$hnos, à (speloghnos, à, splighén-)
‘spleen’. (Cons. and vowels anomalous. Prob. a cpd.) Skt. cf. plihan, m.; Av. sporozn; Per. supurz; Arm. pajcayn, gs: pajceyan; Gk. splén, gs: splénós, m. id. beside a-splenion *spleenwort'; splágkhnon, n. “bowel'; Lat. lien & lienis, gs. id. m. ‘spleen’; MIr. selg, Ir. sealg & seilg, f. id. beside seabhag, m. (sic), id.; Br. felch, m. id.; OCS slezena, f.; OCz. slezeň, m., R sele- zën-ka, f. id.
spelg- (sphelg-) (1) ‘faint’
=== WLD page ===
veret, k7]Q£i Hes., lit. paspiTgqs „dunn im Stroh (vom Korn), ira Wachstum 
zuruckgeblieben“ (Hoffmann BB. 18, 154, Persson BB. 19, 258 [gegen Pick 
I^ 149f., Johansson IP. 2, 44], Boisacq s. v.) ; sie werden besser zu einer 
eigenen Sippe der Bed. „verkummern, kummerlich*^ zusammengeschlossen, da 
eine altereBed. in„kleinere Splitter abspalten“ in keiner Weise zu stutzen ist. 

sp(h)elgh(en, -a), splengh-, spligh- „Milz“. 

Ai. pllhdn-^ av. spdroran-,^ arm. paicahi^ gr. onh]v i^onhqyy^,^ vgl. on7Ayyya 
„Eingeweide“), lat. lien,^ air. selg^ mbret. feldh,^ abg. slezena^ lit. hliimls^ 
apr. hltisne „Milz“. Uber die schwierigen Lautverhaltnisse s. die Lit. bei 
Boisacq 899, am ausfiihrlichsten Yf. IF. 25, 160 ff.; an der Moglichkeit 
lautlicher Yermittlung verzweifeln z. B. Persson Beitr. 906 a 1, 908, Yen- 
dryes Msl. 18, 310. 

Zu ahd. milzi „Milz“ (Petersson IP. 23, 158 f.) fiihrt freilich kein Weg. 
spes- „wehen, hauchen'\ 

Gr. on'^kvyS, -yyog (daraus lat. speluncd), oniqXaiov „H6hle‘* (vgl. zur Bed. 
dvTQov : dvspog)^ hom. oniog^ g. oneiovg (d. i. oneTog,, *OTis£og^ Brugmann 
IP. 9, 160) ds. (scheint *ajr?/[a]o?, Ehrlich KZ. 40, 386 f.); lat. vermutlich 
=== WLD pages.txt tag ===
45144:sp(h)elgh(en, -a), splengh-, spligh- „Milz“.
```


## [2026-09-14T02:36:44.022Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\np='incoming/WLD/WLD_Bd2_pages.txt'\nt=open(p,encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nfor pat in ['sp(h)elgh(en','(s)pen-','sper- „Sperling','Sperling']:\n    for i,l in enumerate(lines):\n        if pat in l:\n            # find nearest preceding [pdf page N]\n            tag=None\n            for j in range(i,max(0,i-400),-1):\n                m=re.search(r'\\[pdf page (\\d+)\\]', lines[j])\n                if m: tag=m.group(1); break\n            print(pat,'| line',i+1,'| pdf page',tag,'|',l.strip()[:90])\n            break\nEOF"
}
```


### [2026-09-14T02:36:45.207Z] TOOL RESULT

```
sp(h)elgh(en | line 45144 | pdf page None | sp(h)elgh(en, -a), splengh-, spligh- „Milz“.
sper- „Sperling | line 44358 | pdf page None | S. weiter die    folgenden Gruppen: sper- „Sperling^‘; sper- „Sparren“,
Sperling | line 571 | pdf page None | letzen^^ anreihen(?).    IJber dt. Fink s. u. "^spingo- „Sperling, Fink“.
```


## [2026-09-14T02:36:50.358Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"sper-(g-)\\|sper- „Sperling\\|sparuo-\" incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt | head -5\necho \"---\"\ngrep -n -A6 \"^(s)pen-\\|^spen- „ziehen\\|ziehen, spannen, spinnen\" incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt | head -30"
}
```


### [2026-09-14T02:36:50.443Z] TOOL RESULT

```
43446:S. weiter die folgenden Gruppen: sper- „Sperling^‘; sper- „Sparren“, 
---
```


## [2026-09-14T02:36:53.285Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"Sperling\" incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt | head -10\necho \"=== spinnen ===\"\ngrep -n \"spannen, spinnen\\|„spinnen\" incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt | head -10"
}
```


### [2026-09-14T02:36:53.354Z] TOOL RESULT

```
612:letzen^^ anreihen(?). IJber dt. Fink s. u. "^spingo- „Sperling, Fink“. 
11054:der Dohle/', fringilla ..Fink. Sperling**: 
42666:sphih „kleiner Yogel“ usw. s. aber u. spingo- „Sperling“), obgleich z. T. 
43302:2. sper- in Yogelnamen, besonders „ Sperling 
43304:Got. sparwa, ags. speanva^ ahd. sparo „Sperling^ (*urg. sparwan-\ mhd. 
43305:sperlinc^ nhd. Sperling Deminutiv) ; aisl. spqrr (gen. spqrs) ds. aus ^spariva-s, 
43335:(Galen), mhd. sperk{e)^ sperch{e) „Sperling^, apr. spergla’Wanag\is] „Sperber‘‘ 
43336:(eig. „Sperlingsgeier“). 
43348:Zugehorigkeit zu sp{h)er- „zucken, mit dem Fufie ausschlagen“ (Sperling 
43446:S. weiter die folgenden Gruppen: sper- „Sperling^‘; sper- „Sparren“, 
=== spinnen ===
331:Vgl. die ahnliche, aber anders vokalisierte Wz. {s)pen- „spinnen“. 
22405:ristan „spmnen“, bal. resag, resay „spinnen, flechten“ Uhlenbeck Ai. Wb. 
24352:rng- „spinnen, Gespinst“. 
42927:1. (s)p6n- .jzieben, spannen“ und „spinnen“, indem die zu flecbtenden, spin- 
42931:*ten- „dehnen, spannen'* fiir „spinnen, flechten^'. {s)pen- : spe(i)- „ziehen“ 
42998:got ahd. ags. spinnan^ dd&l. spinna „spinnen" (von Brugmann IF. 1, 173 
45161:*spne-, zu got. spinnan „spinnen“, lit. ^nti^ abg. p§ti „flechten“) und ein 
45177:lat. weo, were „spinnen“, nemen „Gespinst, Gewebe“, netus ds.;
```


## [2026-09-14T02:37:27.388Z] TOOL CALL #62: Bash

```json
{
 "command": "sed -n '1,120p' tools/verify_check.py"
}
```


### [2026-09-14T02:37:27.435Z] TOOL RESULT

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


## [2026-09-14T02:37:32.240Z] TOOL CALL #63: Bash

```json
{
 "command": "mkdir -p data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg467.png data/verification/sources/refs/ocr/BOOK/467.png && ls -la data/verification/sources/refs/ocr/BOOK/467.png"
}
```


### [2026-09-14T02:37:32.309Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 73548 Sep 13 22:37 data/verification/sources/refs/ocr/BOOK/467.png
```


## [2026-09-14T02:44:58.868Z] TOOL CALL #64: Write

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/page-467.json",
 "content": "{\n  \"pdf_page\": 467,\n  \"book_page\": 437,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-13\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Spelgh, Sphelghen\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *sp(h)elǵʰ(en)-, *splenǵʰ-, *spleǵʰ- 'spleen, milt' (Pokorny 987; Watkins spelgh-; Wiktionary *(s)pli(H)ǵʰḗn)\",\n      \"note\": \"Nourai's root name, language label and gloss are all right. Pokorny 987 heads the entry 'sp(h)elgh(en, -a), splengh-, splegh- \\\"Milz\\\"' and marks it 'tabuistisch umgestaltet' — the anomalous consonantism (Skt pl-, Lat. l-, Gk spl-, Arm. p'-) is why the reconstruction is given in several shapes, and why Nourai's double citation form 'Spelgh, Sphelghen' is legitimate. Watkins/AHD writes the root 'spelgh-. Spleen, milt' and derives Gk splēn and Lat. lien from it; Mann (IEC) sets it up as 'spelég̑hnos (speloghnos, splig̑hén-) \\\"spleen\\\"' and calls the consonants and vowels 'anomalous'. The one systematic caution for the whole page: Nourai's breve (splĕn, psĕr, Kĕros) is a plain vowel mark in his transcription system, not a quantity mark — Greek σπλήν has a LONG ē.\",\n      \"note_fa\": \"ریشهٔ هندواروپایی آغازین *sp(h)elǵʰ(en)- «سپرز، طحال» در پوکورنی، ص ۹۸۷، با همین سه‌گونهٔ spelgh-/splengh-/splegh- آمده است و نام ریشه، برچسب زبانی و معنایی که نورایی داده درست است. پوکورنی خود تصریح می‌کند که این واژه «تابویی و دگرگون‌شده» است، یعنی همخوان‌های آغازین در زبان‌های گوناگون بی‌قاعده‌اند (سنسکریت pl-، لاتین l-، یونانی spl-، ارمنی p'-)؛ به همین سبب چند صورت بازساخته برای آن نهاده‌اند. واتکینز (AHD) و مان (IEC) نیز همین را می‌گویند. تنها نکتهٔ هشدارآمیز آنکه علامت کوتاهی (ĕ) در دستگاه آوانگاری نورایی نشانهٔ کمیت مصوّت نیست: σπλήν یونانی «ای» بلند دارد.\",\n      \"sources\": [\n        \"https://www.etymonline.com/word/spleen\",\n        \"https://en.wiktionary.org/wiki/%E0%A4%AA%E0%A5%8D%E0%A4%B2%E0%A5%80%E0%A4%B9%E0%A4%A8%E0%A5%8D\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:987\", \"status\": \"supports\", \"note\": \"POK_03.txt leaf 228 (printed p. 987) and POK_full.txt 'Root / lemma: sp(h)elgh(en, -a), splengh-, splegh- / Meaning: spleen / Note: taboo deformed / Material: Old Indic plīhán-, Avestan spərəzan- m., Armenian p'aicaḷn, gr. σπλήν … Latin lien, Old Irish selg, Middle Breton felc'h, Old Church Slavic slezena. … Page(s): 987'. Exactly Nourai's root.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"WLD\", \"where\": \"Bd. II (= WP. II 680), s.v. sp(h)elgh(en, -a)\", \"stance\": \"supports\", \"note\": \"WLD_Bd2_1927_dli_106624_djvu.txt line 44231: 'sp(h)elgh(en, -a), splengh-, spligh- „Milz“. Ai. plīhán-, av. spərəzan-, arm. p'aicaḷn, gr. σπλήν (*σπληγγ, vgl. σπλάγχνα „Eingeweide“), lat. lien, air. selg, mbret. felc'h, abg. slezena, lit. blužnis, apr. blusne „Milz“. Über die schwierigen Lautverhältnisse s. …' — the direct predecessor of Pokorny 987.\"},\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. spelgh-\", \"stance\": \"supports\", \"note\": \"AHD_watkins1985.txt: 'spelgh-. Spleen, milt. 1. Deformation *(p)lihén in Latin lién, milt, spleen: LIENAL. 2. Uncertain preform in: a. Greek splén, spleen: SPLEEN; b. Greek splankhna, inward parts: SPLANCHNIC. [Pok. sp(h)elgh(en) 987.]'\"},\n        {\"src\": \"IEC\", \"where\": \"p. 1253/1254 (leaf 691), s.v. spelég̑hnos\", \"stance\": \"supports\", \"note\": \"IEC.txt: 'spelég̑hnos, ā (speloghnos, ā, splig̑hén-) “spleen”. (Cons. and vowels anomalous. Prob. a cpd.) Skt. cf. plihan, m.; Av. spərəzn; Per. supurz; Arm. pajcayn …; Gk. splén, gs: splénós, m. id. …; Lat. lien …' — same family, same members, Mann only rejects a neat reconstruction.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"sperezan\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Avestan spərəzan- m. 'spleen' is attested in the Frahang ī ōīm (F. 9), the Avestan–Pahlavi glossary, glossed there by Pahlavi spurz. It continues PIE *spelǵʰ-en- / *spleǵʰ-en- with the regular Iranian outcomes: PIE *-lǵʰ- > Ir. *-rz- after the Iranian change of a syllabic/short l to r (Iranian has no l), and the *-en- suffix of the body-part heteroclite gives the -an- of the nominative stem. The word is the ancestor of the Middle and New Persian word in node #2. Nourai's 'sperezan' is a plain-ASCII rendering of spərəzan- (schwas written e); Bartholomae's own headword is spərəzan-.\",\n          \"derivation_fa\": \"واژهٔ اوستایی spərəzan- «سپرز» در فرهنگ اویم (Frahang ī ōīm، بند ۹) آمده و در همان‌جا با واژهٔ پهلوی spurz برابر نهاده شده است. این واژه دنبالهٔ صورت هندواروپایی *spelǵʰ-en- است: خوشهٔ *-lǵʰ- در ایرانی باستان به -rz- بدل شده (زیرا «ل» هندواروپایی در ایرانی به «ر» می‌گراید) و پسوند -en- ستاک اندام‌نام‌ها همان -an- پایانی را داده است. صورت «sperezan» نزد نورایی همان spərəzan- بارتولومه است که «شوا»ها را با e نوشته‌اند. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%E0%A4%AA%E0%A5%8D%E0%A4%B2%E0%A5%80%E0%A4%B9%E0%A4%A8%E0%A5%8D\"],\n          \"ref_check\": [\n            {\"ref\": \"POK:987\", \"status\": \"supports\", \"note\": \"Pokorny 987 lists 'Avestan spərəzan- m.' among the first witnesses of the root (POK_03.txt leaf 232 area / POK_full.txt Material line).\"},\n            {\"ref\": \"KLN:1492\", \"status\": \"supports\", \"note\": \"Klein s.v. spleen (KLN_1966.txt line 36331; KLN_1971.txt line 229305): 'Gk. σπλήν, which stands for *σπληγχ and is rel. to σπλάγχνα, “the inward parts” …, and cogn. with OI. plihán-, Avestic spərəzan (for *splgh-en), Arm. p'aicaḷn, L. lien …'. The content is exactly Nourai's arrow. Caveat: our scan of the 1966 two-volume edition has no printed folios, and the leaf-to-page estimate for this leaf (792) lands nearer p. 1550 than p. 1492, so the page figure itself could not be confirmed.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"col. 1624\", \"stance\": \"supports\", \"note\": \"BRT.txt leaf 884, column 1624: 'j. spərəzan- m. „Milz“: -m F. 9. — np. supurz. — Pü.: spurz (in Aw.-Buchst.). — Das Verhältnis zu ai. plīhán- m. …' — Bartholomae himself draws the line Avestan → NP supurz that Nourai draws.\"},\n            {\"src\": \"SNS\", \"where\": \"p. 176 line 5\", \"stance\": \"supports\", \"note\": \"SNS_pages.txt index 'sparazan- 176/5' and the entry on p. 176 pairing '-:spurz:' with 'sparazan-' and 'plīhán-' plus a cross-reference '(1623)' to Bartholomae's column.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. II (= WP. II 680)\", \"stance\": \"supports\", \"note\": \"'Ai. plīhán-, av. spərəzan-, arm. p'aicaḷn, gr. σπλήν …'\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"seporz «سپرز»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Av. spərəzan- → Middle Persian spurz (MacKenzie: 'spurz [splz | P spwrz, N sipurz] spleen', beside the by-form spul) → New Persian سپرز sipurz / supurz / seporz, with the common prothetic-alef variant اسپرز ispurz/esporz (as in اسپر ~ سپر, استخوان ~ ستخوان). The sound history is regular and was set out by Hübschmann: Old Iranian *-rz- is kept as -rz- in New Persian (his example list 'Ap. rz = iran. rz = np. rz: supirz “Milz”'), while the Avestan nominal suffix -an- is lost in Middle Persian, so *spərəz- alone survives. Horn (no. 702) cites the word with exactly this chain. Wiktionary's Persian entry اسپرز derives it from Proto-Iranian *spr̥jā́, the same etymon.\",\n          \"derivation_fa\": \"«سپرز» از فارسی میانهٔ spurz (مکنزی: spurz «طحال»، با گونهٔ spul) و آن از ایرانی باستان / اوستایی spərəzan- است. خوشهٔ -rz- ایرانی باستان در فارسی نو دست‌نخورده مانده (هوبشمان، ص ۲۲۲: «rz پارسی باستان = rz ایرانی = rz فارسی نو: supirz»)، و پسوند -an- اوستایی در فارسی میانه افتاده است. گونهٔ «اسپرز» با الف آغازین همان دگرگونی آشنای «سپر ~ اسپر» و «ستخوان ~ استخوان» است. هرن در بند ۷۰۲ (ص ۱۵۵) همین زنجیره را می‌آورد و ویکی‌واژه نیز آن را از ایرانی آغازین *spr̥jā́ می‌گیرد. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%A7%D8%B3%D9%BE%D8%B1%D8%B2\",\n            \"https://en.wiktionary.org/wiki/%D8%B3%D9%BE%D8%B1%D8%B2\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"HRN:155\", \"status\": \"supports\", \"note\": \"HRN.txt leaf 176, which is headed '— 155 —': '702. supurz “Milz”, uspurz. … aw. spərəza- “Milz” (ZPGl.); phlv. spurz; ai. plīhán- “Milz”.' Horn's page 155 is exactly where Nourai says it is.\"},\n            {\"ref\": \"MON:1827\", \"status\": \"not_checked\", \"note\": \"The print pagination of Mo'in's 6-vol. Farhang-e Farsi cannot be mapped in the available 2-vol. Adena OCR (MON_part1/2 have no page breaks); the word is present there (MON_part1.txt line 10973 'اسبل: [… - اسپرز] … سپرز، اسپرز، طحال').\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"p. 76 s.v. spurz / spul\", \"stance\": \"supports\", \"note\": \"PHD_mackenzie.txt lines 4627 and 4631: 'spul [spwl] spleen.' and 'spurz [·splz | P ·spwrz, N sipurz] spleen.' — MacKenzie gives the Middle Persian link and the New Persian reflex.\"},\n            {\"src\": \"HUB\", \"where\": \"pp. 173, 219, 222\", \"stance\": \"supports\", \"note\": \"HUB.txt: 'supurz “Milz” = zd. spərəza' (p. 173), 'supurz “Milz” = zd. spərəza, skr. plīhán-' (p. 219), 'Ap. rz = iran. rz = np. rz: supirz “Milz” (ph.)' (p. 222).\"},\n            {\"src\": \"BQT\", \"where\": \"—\", \"stance\": \"silent\", \"note\": \"grep of BQT_v1_pages.txt / BQT_v2_pages.txt / BQT_v3_pages.txt for 'سپرز' and 'اسپرز' returns no headword; the س volume of Borhan available here does not carry the entry in readable OCR.\"},\n            {\"src\": \"SNS\", \"where\": \"p. 176 line 3\", \"stance\": \"supports\", \"note\": \"SNS_pages.txt index 'spurz 176/3'; the Shayast-ne-Shayast glossary lemmatises Pahlavi spurz with Av. sparazan- and Skt plīhán-.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Sanskrit\",\n          \"words\": \"splîhân\",\n          \"verdict\": \"transcription_suspect\",\n          \"error_in\": \"book\",\n          \"book_prints\": \"splîhân\",\n          \"correct_form\": \"plīhán- (प्लीहन्)\",\n          \"derivation\": \"The Sanskrit word for 'spleen' is plīhán- (प्लीहन्), first in the Atharvaveda/Brāhmaṇa language; there is no Sanskrit form *splīhān with initial s-. Nourai's 'splîhân' is a reconstruction written as if it were attested: Klein, whose entry he follows for the Avestan node, writes 'OI. plihán- … (for *splgh-en)', and Watkins likewise speaks of a 'Deformation *(p)lihén'. The printed page (checked at 300 dpi, copy at data/verification/sources/refs/ocr/BOOK/467.png) really does read 'splîhân', so the extraction is faithful and the s- is the book's own. The derivation itself is right: PIE *spleǵʰ-en- > Proto-Indo-Iranian *spliHȷ́ʰā́- > Skt plīhán- with taboo loss of the initial s- (and the ǵʰ > h of Indo-Aryan); the same taboo deformation explains Lat. lien and Arm. p'aicaḷn.\",\n          \"derivation_fa\": \"واژهٔ سنسکریت «سپرز» plīhán- (प्लीहन्) است و صورتی با «س» آغازین (*splīhān) در سنسکریت گواهی نشده است. آنچه نورایی نوشته در حقیقت صورت بازساختهٔ *spliǵʰ-en- است که کلاین و واتکینز آن را در کنار plīhán- می‌آورند، نه خودِ واژهٔ سنسکریت؛ این خطای چاپی/سهو خودِ کتاب است، نه خطای خوانش اسکن (تصویر صفحه بررسی شد). ریشه‌شناسی، امّا، درست است: از هندواروپایی *spleǵʰ-en- به هندوایرانی آغازین *spliHȷ́ʰā́- و سپس plīhán- سنسکریت، با افتادن «س» آغازین بر اثر همان دگرگونی تابویی که در lien لاتینی و p'aicaḷn ارمنی هم دیده می‌شود.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%E0%A4%AA%E0%A5%8D%E0%A4%B2%E0%A5%80%E0%A4%B9%E0%A4%A8%E0%A5%8D\"],\n          \"ref_check\": [\n            {\"ref\": \"SNS:176\", \"status\": \"partial\", \"note\": \"SNS p. 176 (index lines 'spurz 176/3', 'sparazan- 176/5'; text at SNS.txt line 10791) does carry the Sanskrit cognate, but spells it 'pllhan-' (= plīhán-), i.e. without the s-: the page Nourai cites contradicts the form he prints while supporting the link.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"p. 987\", \"stance\": \"partial\", \"note\": \"'Old Indic plīhán-' — the root is right, the form has no s-.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. II (= WP. II 680)\", \"stance\": \"partial\", \"note\": \"'Ai. plīhán-' — likewise without s-.\"},\n            {\"src\": \"SKT\", \"where\": \"s.v. Spleen\", \"stance\": \"partial\", \"note\": \"SKT.txt line 18142: 'Spleen. (L. — Gk.) M.E. splen. — L. splen. — Gk. σπλήν, the spleen. — Skt. plīhan; L. lien.' — Skeat too has plīhan.\"},\n            {\"src\": \"IEC\", \"where\": \"p. 1253/1254 s.v. spelég̑hnos\", \"stance\": \"partial\", \"note\": \"'Skt. cf. plihan, m.' — Mann's reconstructed headword splig̑hén- is what Nourai's spelling really reflects.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Greek\",\n          \"words\": \"splĕn\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Ancient Greek σπλήν (splḗn), gen. σπληνός, 'spleen', in Hippocrates and Aristotle; it stands for an older *σπληγχ-, as its by-form σπλάγχνα 'inward parts, viscera' shows, and so preserves the s- and the velar of *spleǵʰ- that Sanskrit and Latin lost. The Ionic-Attic ē is long (η), so Nourai's breve is only his transcription mark, not a quantity. Watkins files it under spelgh- as an 'uncertain preform'.\",\n          \"derivation_fa\": \"یونانی باستان σπλήν (splḗn، اضافی σπληνός) «سپرز» نزد بقراط و ارسطو به کار رفته است و صورت کهن‌تر آن *σπληγχ- بوده، چنان‌که هم‌خانوادهٔ آن σπλάγχνα «احشا، اندرونه» نشان می‌دهد؛ بدین‌سان یونانی هم «س» آغازین و هم همخوان کامی *ǵʰ را نگاه داشته، برخلاف سنسکریت و لاتین. «ای» این واژه بلند است (η)، پس علامت کوتاهی در splĕn نزد نورایی تنها نشانهٔ آوانگاری اوست. ادعای نورایی درست است.\",\n          \"sources\": [\"https://www.etymonline.com/word/spleen\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt s.v. spelgh-: '2. Uncertain preform in: a. Greek splén, spleen: SPLEEN; b. Greek splankhna, inward parts: SPLANCHNIC.'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"s.v. spleen\", \"stance\": \"supports\", \"note\": \"'Gk. σπλήν, which stands for *σπληγχ and is rel. to σπλάγχνα, “the inward parts”'.\"},\n            {\"src\": \"POK\", \"where\": \"p. 987\", \"stance\": \"supports\", \"note\": \"'gr. σπλήν (*σπληγχ, compare σπλάγχνα Nom. Pl. “intestines, entrails”)'.\"},\n            {\"src\": \"SKT\", \"where\": \"s.v. Spleen\", \"stance\": \"supports\", \"note\": \"'— Gk. σπλήν, the spleen.'\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"English\",\n          \"words\": \"spleen\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Greek σπλήν was taken into Latin as splēn, thence Old French esplen, and Middle English splen (late 14th c., in the medical writers); modern spelling spleen. The figurative 'ill temper, melancholy' sense (1580s) comes from humoural medicine, in which the spleen was the seat of black bile. Nourai's arrow Greek → English collapses the Latin and Old French stages, but those are the standard, uncontroversial links.\",\n          \"derivation_fa\": \"واژهٔ یونانی σπλήν به لاتین splēn و از آن به فرانسهٔ کهن esplen و سپس انگلیسی میانه splen (اواخر سدهٔ چهاردهم میلادی، در متون پزشکی) رفت و صورت امروزی spleen شد. معنای مجازی «کج‌خلقی، مالیخولیا» (دههٔ ۱۵۸۰) از طب اخلاط سرچشمه می‌گیرد که سپرز را جایگاه سودا می‌دانست. پیکان نورایی از یونانی یک‌راست به انگلیسی می‌رود و حلقه‌های لاتین و فرانسهٔ کهن را نادیده می‌گیرد، ولی آن حلقه‌ها کاملاً شناخته و بی‌مناقشه‌اند.\",\n          \"sources\": [\"https://www.etymonline.com/word/spleen\"],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference on this node; the parent Greek node carries 'AHD', whose SPLEEN entry covers the English word.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"s.v. spleen\", \"stance\": \"supports\", \"note\": \"'spleen, n. — Fr. OF. esplen or directly fr. L. splen, fr. Gk. σπλήν …'\"},\n            {\"src\": \"SKT\", \"where\": \"s.v. Spleen\", \"stance\": \"supports\", \"note\": \"'Spleen. (L. — Gk.) M.E. splen. — L. splen. — Gk. σπλήν …'\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 1,\n      \"root\": \"Spen, Pen, Poin; Pend\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *(s)pen- / *(s)pen-d- 'to draw, stretch, spin' (Pokorny 988; Watkins (s)pen-)\",\n      \"note\": \"The root is real and Nourai's two references hit it exactly. Pokorny 988 heads '(s)pen-1(d-) … to pull; to spin' and explicitly notes the s-mobile ('1. Formen ohne -s-' / '2. Formen mit anlaut. s-'), which is what licenses Nourai's double citation form 'Spen, Pen'; the d-extension '(s)pen-d-' is his 'Pend'. His fourth shape 'Poin' is not Pokorny's but Mann's: IEC 971 has a separate headword 'poin- (2) “twist, turn”' cross-referred to WP II 661, i.e. to this same root. Nourai's gloss 'twist; turn, spin' is Mann's wording; the primary sense in Pokorny and Watkins is rather 'draw, stretch, spin' (spinning being 'drawing out' the fibre), which is why the Latin 'hang, weigh' branch belongs here at all.\",\n      \"note_fa\": \"ریشه درست است و هر دو ارجاع نورایی دقیقاً بر آن می‌نشیند. پوکورنی در ص ۹۸۸ سرواژهٔ «(s)pen-1(d-) کشیدن، تنیدن» را می‌آورد و خود صورت‌های بی‌«س» و با «س» را از هم جدا می‌کند («۱. صورت‌های بدون -s-» / «۲. صورت‌های با s- آغازین»)؛ همین است که صورت دوگانهٔ Spen/Pen نزد نورایی را توجیه می‌کند، و «Pend» همان گسترشِ d-دارِ پوکورنی است. صورت چهارم یعنی «Poin» از پوکورنی نیست، بلکه از مان است: در IEC ص ۹۷۱ سرواژهٔ جداگانهٔ «poin- (۲) پیچیدن، گردیدن» هست که خود مان آن را به WP II, 661 یعنی به همین ریشه ارجاع می‌دهد. معنایی که نورایی داده («پیچیدن؛ گردیدن، رشتن») واژگان مان است؛ معنای بنیادی نزد پوکورنی و واتکینز «کشیدن، تنیدن» است و همین است که شاخهٔ لاتینی «آویختن، وزن کردن» را در این ریشه می‌گنجاند.\",\n      \"sources\": [\"https://www.etymonline.com/word/spider\", \"https://www.etymonline.com/word/pound\"],\n      \"ref_check\": [\n        {\"ref\": \"POK:988\", \"status\": \"supports\", \"note\": \"POK_full.txt: 'Root / lemma: (s)pen-1(d-) / Meaning: to pull; to spin … 2. forms with anlaut. s-: Latin sponte …; Gothic Old High German Old English spinnan … Old High German spinna “spider” …; Old English spinel, Old High German spinala “spindle”. 3. extension (s)pen-d-: … Latin pendeo, -ere “hang”, pendo, -ere “weigh, assess, pay” … Page(s): 988'.\"},\n        {\"ref\": \"IEC:971\", \"status\": \"supports\", \"note\": \"IEC.txt leaf 539, whose printed folios are 971/972: 'poin- (2) “twist, turn”. Cf. pin-. WP II, 661 — Skt. penami, v. “wander; embrace”; Per. cf. pine “patch of cloth”; Arm. henum, hinem, v. “weave, twist, plait”; MHG (?) vein, adj. compact; Li. painus, adj. “tangled; complex” …'. Both the root shape 'Poin' and the Persian word of node #1 come from this page.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. (s)pen-\", \"stance\": \"supports\", \"note\": \"'(s)pen-. To draw, stretch, spin. I. Basic form *spen-. 1. Suffixed form *spen-wo- in Germanic *spinnan … 2. Extended form *pend- in Latin pendēre, to hang … II. O-grade forms *spon-, *pon-. 1. Germanic *spannan … 4. Suffixed and extended form *pond-o- in Latin pondō, by weight: POUND. … [Pok. (s)pen-(d)- 988.]' — the whole of Nourai's chart in one entry.\"},\n        {\"src\": \"WLD\", \"where\": \"Bd. II 660 ff. (= WP. II 660)\", \"stance\": \"supports\", \"note\": \"WLD_Bd2_1927_dli_106624_djvu.txt line 42927: '1. (s)pén- „ziehen, spannen“ und „spinnen“, indem die zu flechtenden, spinnenden … ' with the note '(s)pen- : spe(i)- „ziehen“'.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Persian\",\n          \"words\": \"pîneh «پینه»\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"NP پینه pīna is well attested in both of Nourai's senses: 'a patch sewn on torn cloth or a shoe' (whence پینه‌دوز 'cobbler') and 'callus, thickened skin of the palm or the forehead from work or prostration' — the sense in the Dehkhodā verse printed in the box ('سبحه در دست و پینه بار جبین'). The etymology, however, rests on one source only: Mann (IEC 971) lists 'Per. cf. pine “patch of cloth”' under *poin- (2) 'twist, turn', the s-less o-grade of *(s)pen- 'spin, plait' — semantically 'something plaited/woven on', formally NP -īna < Ir. *-ainā-/*-ain-ka-. No Iranian handbook confirms it: Horn, Hübschmann, MacKenzie and Nyberg have no entry, Wiktionary has no Persian page for پینه, and Mo'in gives the word without any origin tag (no [په.]), while Dehkhodā offers only the folk etymology پی‌نه 'set after/behind'. Accepted as compatible but unconfirmed.\",\n          \"derivation_fa\": \"«پینه» در هر دو معنایی که نورایی آورده گواهی شده است: «وصله‌ای که بر جامه یا کفش پاره می‌دوزند» (از همین‌جا «پینه‌دوز») و «پوست کلفت‌شدهٔ کف دست یا پیشانی بر اثر کار یا سجدهٔ بسیار» — همان معنایی که بیت دهخدای چاپ‌شده در جعبه («سبحه در دست و پینه بار جبین») بدان اشاره دارد. امّا ریشه‌شناسی تنها بر یک منبع استوار است: مان در IEC ص ۹۷۱ ذیل *poin- (۲) «پیچیدن، تابیدن» می‌نویسد «فارسی: pine، وصلهٔ پارچه»، یعنی از گونهٔ بی‌«س»ِ ریشهٔ *(s)pen- «رشتن، بافتن»، با پسوند فارسی -ینه از ایرانی *-ainā-. هیچ‌یک از دستینه‌های ایرانی (هرن، هوبشمان، مکنزی، نیبرگ) این واژه را ندارند، ویکی‌واژه مدخل فارسی ندارد، و معین آن را بی هیچ برچسب ریشه‌ای (مثلاً [په.]) می‌آورد؛ دهخدا نیز تنها ریشه‌شناسی عامیانهٔ «پی + نه» را پیش می‌کشد. پس ادعای نورایی با احتیاط پذیرفتنی است، نه تأییدشده.\",\n          \"sources\": [\"https://abadis.ir/fatofa/%D9%BE%DB%8C%D9%86%D9%87/\"],\n          \"ref_check\": [\n            {\"ref\": \"IEC:971\", \"status\": \"supports\", \"note\": \"IEC leaf 539 (printed 971/972): 'poin- (2) “twist, turn”. … Per. cf. pine “patch of cloth”'. Nourai's node is a direct transcript of this line, gloss included.\"},\n            {\"ref\": \"MON:970\", \"status\": \"partial\", \"note\": \"Mo'in has the word with exactly Nourai's two senses — abadis.ir quotes the Mo'in entry 'پینه (نِ) (اِ) ۱- تکه پارچه‌ای که بر قسمت پارهٔ جامه دوزند ۲- پوست کلفت و ضخیم‌شدهٔ کف دست در اثر کار زیاد' — but gives NO origin tag, so it supports the meanings and not the Indo-European derivation. The 6-vol. pagination cannot be checked in the 2-vol. OCR on disk (MON_part1.txt lines 35833, 35958 carry the word).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HRN\", \"where\": \"—\", \"stance\": \"silent\", \"note\": \"grep of HRN.txt for 'pina', 'pine', 'Flicken', 'Lappen' gives no entry for this word; Horn does not treat پینه.\"},\n            {\"src\": \"PHD\", \"where\": \"—\", \"stance\": \"silent\", \"note\": \"no Middle Persian *pēn/*pīn 'patch' in MacKenzie (PHD_mackenzie.txt); the word has no Pahlavi attestation.\"},\n            {\"src\": \"BQT\", \"where\": \"vol. 1 (پ), several passing mentions\", \"stance\": \"partial\", \"note\": \"Borhan uses پینه only as a defining synonym of رقعه/وصله (BQT_v1_pages.txt lines 16051 'و رقعه و پینه را نیز گویند', 24811 'و پینه و وصله را نیز گویند'); no headword with an etymological footnote by Mo'in.\"},\n            {\"src\": \"MON\", \"where\": \"s.v. پینه (via abadis.ir)\", \"stance\": \"partial\", \"note\": \"meanings confirmed, no origin bracket; Dehkhodā's note derives it from 'پی نه' — a folk etymology, not a historical one.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Germanic\",\n          \"words\": \"spinnan; spithra; spin-ilôn; spannjan\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Three of the four are exactly Watkins's forms: Gmc *spinnan 'to spin' (< suffixed *spen-wo-; Goth./OHG/OE spinnan, ON spinna), Gmc *spin-ilōn 'spindle' (OE spinel, OHG spinala), and the o-grade *spannan 'to stretch, bind' (MDu. spannen, OHG spannan) beside the noun *spannō 'span'. Two small slips: (a) 'spithra' is not a Germanic but an Old English form — Watkins and Etymonline give Gmc *spin-thron- 'the spinner', contracted in Old English to spiþra > spider, the West-Germanic cognates being MDu./MLG/OHG spinne; (b) Nourai's 'spannjan' is a weak jan-causative (of the type OHG spennen); the ancestor of English span is the strong verb *spannan and the noun *spannō, not the causative. Pokorny moreover puts *spannan not here but under *spə-nu- on p. 982, cross-referring; Watkins keeps it under (s)pen-, and Nourai follows Watkins.\",\n          \"derivation_fa\": \"سه صورت از چهار صورت این جعبه دقیقاً همان‌هایی است که واتکینز می‌آورد: ژرمنی *spinnan «رشتن» (از *spen-wo-؛ گوتی و آلمانی علیای باستان و انگلیسی باستان spinnan)، *spin-ilōn «دوک» (انگلیسی باستان spinel)، و صورت o-دارِ *spannan «کشیدن، بستن». دو لغزش کوچک هست: نخست آنکه spithra ژرمنی نیست بلکه انگلیسیِ باستان است — واتکینز ژرمنی *spin-thron- «رشنده» را می‌آورد که در انگلیسی باستان به spiþra کوتاه شده و spider امروزی از آن است؛ دوم آنکه «spannjan» فعلِ سببیِ ضعیف است (مانند spennen آلمانی علیای باستان)، حال آنکه نیای واژهٔ انگلیسی span فعل قویِ *spannan و نامِ *spannō است. افزون بر این، پوکورنی *spannan را نه در این ریشه بلکه ذیل *spə-nu- در ص ۹۸۲ جای می‌دهد؛ واتکینز آن را همین‌جا نگاه می‌دارد و نورایی از واتکینز پیروی کرده است.\",\n          \"sources\": [\"https://www.etymonline.com/word/spider\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD:1542\", \"status\": \"partial\", \"note\": \"Watkins 1985 s.v. (s)pen-: '1. Suffixed form *spen-wo- in Germanic *spinnan … in: a. Old English spinnan, to spin, with derivative *spin-thron-, “the spinner,” contracted to spithra, spider: SPIN, SPIDER; b. Germanic derivative *spin-ilōn in Old English spinel, spindle: SPINDLE. … II. O-grade forms *spon-, *pon-. 1. Germanic *spannan in: a. Middle Dutch spannen, to bind: SPAN …'. Supports the node except that AHD's forms are *spannan (not *spannjan) and it labels spithra Old English. The page number 1542 belongs to the 1976 AHD appendix (pp. 1505-1550), which is not open online; the alphabetical position of spen-/sper- makes it plausible.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"p. 988 (and 982)\", \"stance\": \"partial\", \"note\": \"'Gothic Old High German Old English spinnan, Old Icelandic spinna “spinnen” (*spenu-, compare spannan S. 982 from *spə-nu-). Old High German spinna “spider” …; Old English spinel, Old High German spinala (and spinnila) “spindle”.' — Pokorny has spinnan, spinna, spinel here but files spannan under a neighbouring root.\"},\n            {\"src\": \"SKT\", \"where\": \"s.v. Spin, Spider\", \"stance\": \"supports\", \"note\": \"SKT.txt lines 18072, 18086: 'Spider; see Spin.' / 'Spin, to draw out threads. (E.) A.S. spinnan …'\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. II 660 ff.\", \"stance\": \"supports\", \"note\": \"line 42998: 'got. ahd. ags. spinnan, aisl. spinna „spinnen“'.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"English\",\n          \"words\": \"spin; spider; spindle; span\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"OE spinnan (strong verb III) > ME spinnen > spin; OE spiþra (< *spin-þron- 'the spinner') > ME spiþre/spydyr (late 14th c., displacing older loppe, atorcoppe) > spider; OE spinel (f., *spin-ilōn) > spindle, with the excrescent -d- of the type thunor > thunder; OE spann(n) 'distance between thumb and little finger' (Gmc *spannō) > span, reinforced by the verb span 'to stretch, bind' which English partly owes to Middle Dutch spannen. All four are standard.\",\n          \"derivation_fa\": \"spin از انگلیسی باستان spinnan (فعل قوی ردهٔ سوم)؛ spider از انگلیسی باستان spiþra (از *spin-þron- «رشنده») که در اواخر سدهٔ چهاردهم جای واژه‌های کهن‌ترِ loppe و atorcoppe را گرفت؛ spindle از انگلیسی باستان spinel با «د» میانجی (همانند thunor > thunder)؛ و span از انگلیسی باستان spann «فاصلهٔ میان انگشت شست و کوچک» (ژرمنی *spannō) که فعلِ همریشهٔ آن تا اندازه‌ای از هلندی میانه (spannen) نیز تقویت شده است. هر چهار واژه از موارد استاندارد و بی‌مناقشه‌اند؛ ادعای نورایی درست است.\",\n          \"sources\": [\"https://www.etymonline.com/word/spider\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 index (AHD_watkins1985.txt line 2278-2279): 'SPAN1 (s)pen- · SPAN2 (s)pen- · SPIN (s)pen- · SPINDLE (s)pen- · SPIDER (s)pen-'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"SKT\", \"where\": \"s.v. Spin / Spider / Spangle\", \"stance\": \"supports\", \"note\": \"'Spider; see Spin.'; 'Spin, to draw out threads. (E.) A.S. spinnan.'\"},\n            {\"src\": \"KLN\", \"where\": \"s.v. spider, spindle, span\", \"stance\": \"supports\", \"note\": \"Klein's S-volume (KLN_1966.txt leaves 791-792) carries the same derivations under spin/spider/spindle/span.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Latin\",\n          \"words\": \"pendĕre\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Latin has a pair from the d-extension *(s)pen-d-: pendēre (2nd conj., stative) 'to hang, be suspended' and pendere (3rd conj., pependī, pēnsum) 'to cause to hang, weigh out, pay', with the frequentative pēnsāre 'to weigh'. Nourai's spelling 'pendĕre' with the gloss 'to hang' mixes the two (the 'hang' verb is pendēre with long ē), but that is his generic breve again, and both verbs are the same root and both feed the English list below. Pokorny 988 puts them here with the semantic bridge 'gespannt hängen' — hanging from a taut cord — and pairs them with OCS pędь 'span' and pęditi 'drive'.\",\n          \"derivation_fa\": \"لاتین از گسترشِ d-دارِ *(s)pen-d- دو فعل جفت دارد: pendēre (باب دوم، حالتی) «آویزان بودن» و pendere (باب سوم) «آویختن، وزن کردن، پرداختن» با فعل مکررِ pēnsāre «سنجیدن». نورایی «pendĕre» را با معنای «آویختن» آورده که دو فعل را در هم می‌آمیزد (فعلِ «آویزان بودن» pendēre با «ای» بلند است)، ولی این همان علامت کوتاهیِ تشریفاتیِ اوست و هر دو فعل از یک ریشه‌اند و هر دو مشتق‌های انگلیسیِ جعبهٔ بعد را می‌زایند. پوکورنی در ص ۹۸۸ همین دو را اینجا می‌نهد و پل معنایی را «آویخته بر ریسمانِ کشیده» می‌داند و آن‌ها را با pędь اسلاوی کلیسایی کهن «وجب» می‌سنجد.\",\n          \"sources\": [\"https://www.etymonline.com/word/pound\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD:1542\", \"status\": \"supports\", \"note\": \"Watkins s.v. (s)pen-: '2. Extended form *pend- in Latin pendēre, to hang (intransitive), and pendere, to cause to hang, weigh, with its frequentative pensāre, to weigh: … PENDANT … SUSPEND, VILIPEND.'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"p. 988\", \"stance\": \"supports\", \"note\": \"'presumably also as “gespannt hängen”, Latin pendeo, -ere “hang, herabhängen”, pendo, -ere “wägen, assess, pay” (to weighing hang), Umbrian ampentu “impendito”.'\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. II 660 ff. (= WP. II 661 f.)\", \"stance\": \"supports\", \"note\": \"the Latin pair stands in the same paragraph of Walde-Pokorny that Pokorny 988 abridges.\"},\n            {\"src\": \"KLN\", \"where\": \"s.v. pendant, pending\", \"stance\": \"supports\", \"note\": \"Klein derives the whole pend- family from L. pendēre 'to hang', rel. to pendere 'to weigh'.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"English\",\n          \"words\": \"pendant; pension; append; compensate; depend; expend; perpendicular; suspend; pendulum\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"All nine are Latin-derived, mostly through Old French: pendant < OFr. pendant, pres. part. of pendre < L. pendēre; pension < L. pēnsiō (from pendere 'pay out'); append < L. appendere; compensate < L. compēnsāre (com- + pēnsāre); depend < OFr. dependre < L. dēpendēre 'hang from'; expend < L. expendere 'weigh out, pay'; perpendicular < L. perpendiculāris, from perpendiculum 'plumb-line' (that which hangs straight down); suspend < L. suspendere; pendulum < ModL. pendulum, neuter of L. pendulus 'hanging' (coined for Huygens's clock, 1660). The semantic hinge throughout is Roman weighing with a suspended balance, which is why 'hang', 'weigh' and 'pay' are one family.\",\n          \"derivation_fa\": \"هر نُه واژه از لاتین‌اند، بیشترشان از راه فرانسهٔ کهن: pendant از اسم فاعلِ pendre؛ pension از pēnsiō لاتینی (از pendere «پرداختن»)؛ append از appendere؛ compensate از compēnsāre؛ depend از dēpendēre «از چیزی آویختن»؛ expend از expendere «وزن کردن و پرداختن»؛ perpendicular از perpendiculum «شاقول، ریسمانِ راست‌آویخته»؛ suspend از suspendere؛ و pendulum از لاتینِ نو، خنثای pendulus «آویزان» که در ۱۶۶۰ برای ساعتِ هویگنس ساخته شد. لولای معنایی همهٔ این‌ها ترازوی آویختهٔ رومی است؛ به همین سبب است که «آویختن»، «سنجیدن» و «پرداختن» یک خانواده‌اند. ادعای نورایی درست است.\",\n          \"sources\": [\"https://www.etymonline.com/word/pound\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins s.v. (s)pen- lists PENDANT, PENDULOUS, PENSION, PENSIVE …; APPEND, COMPENDIUM, COMPENSATE, DEPEND, DISPENSE, EXPEND, IMPEND, PERPENDICULAR, SUSPEND — Nourai's list is a subset with 'pendulum' added (Watkins has PENDULOUS).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"s.vv. pendant, pension, pendulum\", \"stance\": \"supports\", \"note\": \"Klein gives each of these from L. pendēre/pendere via Old French or Modern Latin.\"},\n            {\"src\": \"SKT\", \"where\": \"s.v. Pendant, Pension\", \"stance\": \"supports\", \"note\": \"Skeat: 'Pendant. (F. — L.) F. pendant, hanging; from pendre, to hang; L. pendēre.'\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Latin\",\n          \"words\": \"pondô\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Latin pondō is the frozen ablative of an old noun *pondus 'weight' (later pondus, ponder-), literally 'by weight', used in the formula libra pondō 'a pound by weight' and thence as an indeclinable noun 'a pound'. It is the o-grade *pond-o- of the same d-extension as pendere, with the regular Latin outcome of *o. Its denominative ponderāre 'to weigh' gives English ponder, ponderous.\",\n          \"derivation_fa\": \"pondō لاتینی صورتِ به‌جامانده از حالتِ ازی (ablative) نامِ کهنِ *pondus «وزن» است، به‌معنای تحت‌اللفظیِ «به وزن»، که در ترکیبِ libra pondō «یک لیبرا به وزن» به کار می‌رفت و سپس خود به نامی تغییرناپذیر به معنای «رطل» بدل شد. این همان درجهٔ o-دارِ *pond-o- از همان گسترشِ d-داری است که pendere را ساخته است. فعلِ برساختهٔ ponderāre «سنجیدن» نیز واژه‌های انگلیسیِ ponder و ponderous را داده است. ادعای نورایی درست است.\",\n          \"sources\": [\"https://www.etymonline.com/word/pound\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD:1542\", \"status\": \"supports\", \"note\": \"Watkins s.v. (s)pen-, II.4: 'Suffixed and extended form *pond-o- in Latin pondō, by weight: POUND1.' — Nourai's node word for word, gloss included.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"p. 988\", \"stance\": \"partial\", \"note\": \"Pokorny cites 'Latin pendo, -ere “wägen”' here but does not spell out pondō; the o-grade noun is Walde-Pokorny's / Watkins's addition.\"},\n            {\"src\": \"KLN\", \"where\": \"s.v. pound (weight)\", \"stance\": \"supports\", \"note\": \"Klein derives OE pund from L. pondō, ablative of *pondus.\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"English\",\n          \"words\": \"pound\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Latin pondō (in libra pondō) was borrowed early — before the Anglo-Saxon migration, along with the Roman weights-and-measures vocabulary — into Proto-Germanic as *pundą, whence Old English pund, Old High German pfunt, Gothic pund, and so Middle English pound. Nourai's arrow Latin → English is right in substance but skips the Germanic stage: pound is not a learned Latinism but a very old Germanic loan from Latin, which is why it shows the Germanic vowel and no -o. (This is also how Watkins draws it, without the intermediate.) The currency sense comes from the medieval pound of silver.\",\n          \"derivation_fa\": \"واژهٔ لاتینِ pondō (در ترکیبِ libra pondō) بسیار زود — پیش از کوچِ آنگلوساکسون‌ها و همراه با دستگاه اوزان و مقادیر رومی — به ژرمنیِ آغازین وام داده شد و *pundą را ساخت؛ از آن انگلیسی باستان pund، آلمانی علیای باستان pfunt و گوتی pund، و سپس انگلیسی میانه pound پدید آمد. پیکانِ نورایی از لاتین یک‌راست به انگلیسی از نظر محتوا درست است ولی حلقهٔ ژرمنی را نادیده می‌گیرد: pound وام‌واژه‌ای دیرین و مردمی است نه لاتینی‌گراییِ کتابی، و به همین سبب مصوّت ژرمنی دارد و پایانهٔ -o را از دست داده است. (واتکینز نیز آن را به همین شکلِ بی‌واسطه رسم می‌کند.) معنای پولی آن از رطل نقرهٔ سده‌های میانه است.\",\n          \"sources\": [\"https://www.etymonline.com/word/pound\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins index: 'POUND1 (s)pen-'; entry II.4 'Latin pondō, by weight: POUND1'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"s.v. pound\", \"stance\": \"supports\", \"note\": \"Klein: OE pund, from Proto-Germanic *pundam, an early loan from L. pondō.\"},\n            {\"src\": \"SKT\", \"where\": \"s.v. Pound\", \"stance\": \"supports\", \"note\": \"Skeat marks Pound '(L.)' with A.S. pund from L. pondō, libra pondō.\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 2,\n      \"root\": \"Sper, Qusĕros, Kĕros\",\n      \"verdict\": \"plausible\",\n      \"modern_form\": \"PIE *sper-(g-) 'name of a small bird, esp. sparrow' (Pokorny 991, NOT 997; Watkins sper-3) — Nourai has merged it with Mann's separate *quséros / *ḱeros 'motley, dappled' (IEC 1056, 613)\",\n      \"note\": \"Two separate matters. (a) The page number: Pokorny's sparrow root is on p. 991, not 997 — POK_03.txt leaf 232 carries '2. sper-(g-) in Vogelnamen, besonders „Sperling“; sparuo-:prauo- ds.' and the folio 992 falls after it, while the entry before it (1. (s)per- 'Sparren') is p. 990 and the one after (3. sper- 'drehen') runs 991-992. Nourai's '997' is copied from Watkins's bracket '[Pok. sper-(g)- 997]', which is itself wrong. (b) The substance: 'Qusĕros' and 'Kĕros' are Mann's headwords, and Mann glosses them 'motley, dapple', NOT 'sparrow' — he keeps them apart from *sper-. Nourai has fused a Germanic/Greek bird-name root with an Indo-Iranian colour word, which is his own synthesis; it is defensible only because Greek ψάρ 'starling' / ψᾱρός 'dapple-grey' sits in both families (Pokorny puts it under sper- with an explicit '(??)', Mann under quséros). The gloss 'sparrow' for the whole box is therefore too narrow: 'starling / small speckled bird' would be right.\",\n      \"note_fa\": \"دو نکته. نخست شمارهٔ صفحه: ریشهٔ «گنجشک» نزد پوکورنی در ص ۹۹۱ است نه ۹۹۷ — در POK_03 برگ ۲۳۲ سرواژهٔ «۲. sper-(g-) در نام پرندگان، به‌ویژه گنجشک» آمده و شمارهٔ ۹۹۲ پس از آن می‌افتد؛ نورایی «۹۹۷» را از قلّابِ واتکینز «[Pok. sper-(g)- 997]» برداشته که خود نادرست است. دوم محتوا: «Qusĕros» و «Kĕros» سرواژه‌های مان‌اند و مان معنای آن‌ها را «رنگارنگ، خال‌خال» می‌داند نه «گنجشک»، و آن‌ها را از *sper- جدا نگاه می‌دارد. نورایی ریشهٔ نامِ پرندهٔ ژرمنی–یونانی را با واژهٔ رنگِ هندوایرانی یکی گرفته است؛ این ترکیب تنها از آن رو دفاع‌پذیر است که ψάρ یونانی «سار» و ψᾱρός «خاکستری‌خال» در هر دو خانواده جای می‌گیرند (پوکورنی آن را با علامت پرسش دوگانه ذیل sper- می‌آورد و مان ذیل quséros). پس معنای «گنجشک» برای کل جعبه تنگ است؛ «سار / پرندهٔ کوچکِ خال‌دار» درست‌تر می‌بود. داوری: با احتیاط پذیرفتنی.\",\n      \"sources\": [\"https://www.etymonline.com/word/sparrow\", \"https://en.wiktionary.org/wiki/%CF%88%CE%AC%CF%81\"],\n      \"ref_check\": [\n        {\"ref\": \"POK:997\", \"status\": \"partial\", \"note\": \"The root exists but the page is wrong. POK_03.txt leaf 232: '2. sper-(g-) in Vogelnamen, besonders „Sperling“ … Got. sparwa, ags. spearwa, ahd. sparo „Sperling“ (*urgerm. *sparwan-) … gr. ψάρ, ion. ep. ψήρ … „Star“ … WP. II 666 f., WH. II 257, Trautmann 275.' The leaf's folio number is 992 and it stands after the entry, so the root begins on p. 991; POK_full.txt likewise prints 'Page(s): 991'. Pokorny p. 997 falls inside (s)p(h)ereg- 'to sprinkle' (996-998), which is unrelated.\"},\n        {\"ref\": \"IEC:613\", \"status\": \"supports\", \"note\": \"IEC.txt leaf 347, printed folios 613/614: 'Ḱeros (3) “dapple, marked with grey or black”. WP I, 360 & 420 — Skt. śaráḥ “motley”; Per. sār “starling”; Gk. cf. kērulos “blue kingfisher”; Ir. ciar, MIr. cíar “dark, brown, black”; OCS sěrŭ …'. The page is right; the gloss is 'dapple', not 'sparrow'.\"},\n        {\"ref\": \"IEC:1056\", \"status\": \"supports\", \"note\": \"IEC.txt leaf 585, which carries the marginal folio '1056': 'quséros (qusáros? Initial and vocalism problematic) “motley”. Variant initial consonantism in Indo-Iranian. Cf. WP II, 666 — Skt. cf. cāráḥ, śāráḥ, id.; Per. sār, sārak, s. “starling”; Gk. psārós, adj. “motley”; psēr, gs: -ós, beside psār, m. “starling”; … OCS šarŭ, šara “colour” …'. Page and forms exactly as Nourai cites them; the gloss again is 'motley'.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. sper-3\", \"stance\": \"partial\", \"note\": \"'sper-3. Bird's name, sparrow. Suffixed o-grade form *spor-wo- in Germanic *sparwan- in Old English spearwa, spearwe, sparrow: SPARROW. [Pok. sper-(g)- 997.]' — supports the Germanic/English branch and is the source of Nourai's wrong page; it knows nothing of Persian sār.\"},\n        {\"src\": \"WLD\", \"where\": \"Bd. II 666 f. (= WP. II 666)\", \"stance\": \"supports\", \"note\": \"WLD_Bd2 line 43302: '2. sper- in Vogelnamen, besonders „Sperling“ — Got. sparwa, ags. spearwa, ahd. sparo „Sperling“ (*urg. sparwan-, mhd. sperlinc, nhd. Sperling Deminutiv); aisl. spǫrr …'\"},\n        {\"src\": \"POK\", \"where\": \"p. 991\", \"stance\": \"partial\", \"note\": \"Pokorny attaches Greek ψάρ to this root only with a double question mark: 'das formantische u auch (??) in gr. ψάρ, ion. ep. ψήρ … „Star“' — i.e. the Greek link that Nourai's box depends on is itself flagged as doubtful.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"sâr\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"A Middle Persian *sār 'starling' is not attested in the published Pahlavi corpus: it is absent from MacKenzie's Concise Pahlavi Dictionary and from Nyberg's glossary (both greppable here, and both have sār only in the unrelated senses 'head, category' < Av. sarah-/saraδa-). The node rests entirely on Mo'in, who tags the New Persian bird-word سار '(پ.)' = of Pahlavi origin. That tag is a reasonable inference — the word is old and has no Arabic or Turkic look — but it is an inference, not an attestation. The gloss should be 'starling' (زرزور), not 'sparrow'; Mo'in's own wording, 'پرنده‌ای است شبیه گنجشک اما بزرگتر از آن', 'a bird like a sparrow but bigger', is evidently what made Nourai write 'sparrow'.\",\n          \"derivation_fa\": \"صورتِ فارسی میانهٔ *sār «سار» در پیکرهٔ منتشرشدهٔ پهلوی گواهی نشده است: نه در فرهنگ کوچکِ پهلویِ مکنزی هست و نه در واژه‌نامهٔ نیبرگ (در هر دو، sār تنها به معنای بی‌ربطِ «سر، گونه» از اوستاییِ sarah-/saraδa- آمده است). این جعبه یکسره بر معین استوار است که واژهٔ فارسیِ «سار» (پرنده) را با برچسبِ «(پ.)» یعنی پهلوی‌تبار نشان می‌دهد. این برچسب استنباطی معقول است — واژه کهن است و نشانی از عربی یا ترکی ندارد — ولی استنباط است نه گواهی. معنای درست «سار/زرزور» است نه «گنجشک»؛ عبارتِ خودِ معین، «پرنده‌ای است شبیه گنجشک اما بزرگ‌تر از آن»، پیداست که سبب شده نورایی «sparrow» بنویسد. داوری: با احتیاط پذیرفتنی.\",\n          \"sources\": [\"https://abadis.ir/fatofa/%D8%B3%D8%A7%D8%B1/\"],\n          \"ref_check\": [\n            {\"ref\": \"MON:1789\", \"status\": \"supports\", \"note\": \"Mo'in s.v. سار (quoted at abadis.ir): '(پ.) پرنده‌ای است شبیه گنجشک اما بزرگتر از آن که بیشتر به شکار ملخ می‌پردازد' — the bracket (پ.) is Mo'in's tag for Pahlavi origin, which is precisely Nourai's Pahlavi box. The 6-vol. page 1789 itself cannot be checked (no paginated copy of Mo'in on disk or online).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"s.v. sār (absent)\", \"stance\": \"silent\", \"note\": \"grep of PHD.txt / PHD_mackenzie.txt for 'starling' and for a headword sār returns nothing; MacKenzie has only apāc-sār, mēš-sār etc. with sar 'head, kind'.\"},\n            {\"src\": \"NYB\", \"where\": \"Glossary, s.vv. apāc-sārēh, mēš-sār\", \"stance\": \"silent\", \"note\": \"NYB_vol2_glossary.txt has sār only in 'mēš-sār … NP mēš + sar < Av. (1566) saraδa- “species”' and 'apāc-sār' — no bird.\"},\n            {\"src\": \"IEC\", \"where\": \"pp. 613, 1056\", \"stance\": \"partial\", \"note\": \"Mann labels the word simply 'Per. sār, sārak “starling”' without a Middle Persian stage.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"sâr «سار ۳»\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"NP سار sār is the common starling, Sturnus vulgaris (Dehkhodā: 'پرنده‌ای است سیاه و خوش‌آواز که خال‌های سفید ریزه دارد' — a black, sweet-voiced bird with fine white specks), with the diminutives and variants Nourai prints in the box: سارک sārak, ساری sārī, سارچ sārč, سارجه sārja. Borhān-e Qāṭeʿ gives the same description under سارو ('پرنده‌ای است سیاه‌رنگ و نقطه‌های سفید دارد و خوش‌آواز باشد'). The word is inherited, not borrowed; its Indo-European affiliation is Mann's *quséros/*ḱeros 'dappled' (Skt śāra- 'motley', OCS šarŭ 'colour'), i.e. the bird named from its speckling, with Old Iranian *sā́ra- > NP sār. Wiktionary's Persian entry gives no etymology, so Mann remains the only authority, and the derivation is compatible with but not confirmed by modern Iranian lexicography. The chart's gloss 'sparrow' is wrong for the bird itself; 'starling' is what every source says.\",\n          \"derivation_fa\": \"«سار» در فارسی نو همان پرندهٔ Sturnus vulgaris است (دهخدا: «پرنده‌ای است سیاه و خوش‌آواز که خال‌های سفید ریزه دارد») با گونه‌ها و مصغرهایی که نورایی در جعبه آورده است: سارک، ساری، سارچ، سارجه. برهان قاطع نیز ذیل «سارو» همین وصف را می‌آورد: «پرنده‌ای است سیاه‌رنگ و نقطه‌های سفید دارد و خوش‌آواز باشد». واژه ارثی است نه وام‌واژه؛ پیوند هندواروپاییِ آن از آنِ مان است: *quséros/*ḱeros «خال‌خال، رنگارنگ» (سنسکریت śāra- «رنگارنگ»، اسلاوی کلیسایی کهن šarŭ «رنگ»)، یعنی پرنده را از خال‌هایش نام داده‌اند، با ایرانی باستان *sā́ra- > فارسی نو «سار». ویکی‌واژه ریشه‌شناسی نمی‌دهد و فرهنگ‌نویسیِ ایرانیِ امروز نیز خاموش است، پس تنها گواه مان است. معنای «گنجشک» در نمودار نادرست است؛ همهٔ منابع «سار/زرزور» می‌گویند.\",\n          \"sources\": [\"https://abadis.ir/fatofa/%D8%B3%D8%A7%D8%B1/\", \"https://en.wiktionary.org/wiki/%D8%B3%D8%A7%D8%B1\"],\n          \"ref_check\": [\n            {\"ref\": \"IEC:613,1056\", \"status\": \"supports\", \"note\": \"IEC leaf 347 (folios 613/614) 'Per. sār “starling”' under Ḱeros (3), and leaf 585 (folio 1056) 'Per. sār, sārak, s. “starling”' under quséros — both pages carry the Persian word exactly as Nourai cites them, including the diminutive sārak.\"},\n            {\"ref\": \"MON:1789\", \"status\": \"supports\", \"note\": \"Mo'in s.v. سار: '(پ.) پرنده‌ای است شبیه گنجشک اما بزرگتر از آن' (abadis.ir). Page not verifiable.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BQT\", \"where\": \"vol. 2, s.v. سارو / سودان\", \"stance\": \"supports\", \"note\": \"BQT_v2_pages.txt line 39088: 'سودان … بمعنی سارو باشد، و آن پرنده‌ایست سیاه‌رنگ و نقطه‌های سفید دارد و خوش‌آواز باشد' — Borhān's description of the bird; no etymological footnote by Mo'in at this place.\"},\n            {\"src\": \"HRN\", \"where\": \"—\", \"stance\": \"silent\", \"note\": \"Horn's Grundriss has no entry for the bird sār (grep of HRN.txt for 'Star', 'sār' yields only sar 'Kopf').\"},\n            {\"src\": \"MON\", \"where\": \"s.v. سار (via abadis.ir)\", \"stance\": \"supports\", \"note\": \"Pahlavi tag + starling sense confirmed; Dehkhodā there: 'زرزور'.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Sanskrit\",\n          \"words\": \"čârah\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Nourai's source is Mann, who writes under quséros 'Skt. cf. cāráḥ, śāráḥ, id.' — but 'id.' there refers to the headword's gloss 'motley', not to 'starling/sparrow'. Nourai has carried the bird gloss down into the Sanskrit box, and that is not what any Sanskrit dictionary says. The genuine Sanskrit words are (i) śāra- 'variegated, mottled, dappled' (the colour adjective, the true cognate of Persian sār on Mann's scheme) and (ii) śāri- / śārikā- 'the myna, Turdus salica' — a bird, but with ś-, not c-. Sanskrit cāra- means 'going, motion; a spy', an entirely different word from √car 'to move'. So the node as drawn — Sanskrit 'čârah' = 'sparrow' — is not supported: the form with c- is Mann's own doubtful variant ('Variant initial consonantism in Indo-Iranian', and for the root itself 'Initial and vocalism problematic'), and the gloss is wrong.\",\n          \"derivation_fa\": \"خاستگاه این جعبه مان است که ذیل quséros نوشته «سنسکریت: cāráḥ، śāráḥ، همان» — امّا «همان» در آنجا به معنای سرواژه یعنی «رنگارنگ، خال‌خال» بازمی‌گردد نه به «سار/گنجشک». نورایی معنای پرنده را به جعبهٔ سنسکریت هم کشانده است و هیچ فرهنگ سنسکریتی چنین نمی‌گوید. واژه‌های راستین سنسکریت این‌هایند: śāra- «رنگارنگ، خال‌خال» (همان صفتِ رنگ که بنا بر طرح مان هم‌ریشهٔ «سار» فارسی است) و śāri-/śārikā- «مینا، سارِ هندی» — پرنده، ولی با «ش» نه «چ». امّا cāra- در سنسکریت به معنای «رفتن، حرکت؛ جاسوس» است و از ریشهٔ car- «رفتن» می‌آید و ربطی به این خانواده ندارد. پس این جعبه چنان‌که رسم شده پذیرفتنی نیست: هم صورتِ «چ»دار گونهٔ مشکوکِ خودِ مان است (که خود می‌نویسد «همخوانِ آغازین در هندوایرانی دگرگون است» و دربارهٔ خودِ ریشه «آغاز و مصوّت‌ها مسئله‌دارند») و هم معنا نادرست است. پژوهش امروزی این پیوند را به این شکل نمی‌پذیرد.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D8%B3%D8%A7%D8%B1\"],\n          \"ref_check\": [\n            {\"ref\": \"IEC:1056\", \"status\": \"partial\", \"note\": \"IEC.txt leaf 585 (folio 1056): 'quséros (qusáros? Initial and vocalism problematic) “motley”. Variant initial consonantism in Indo-Iranian. Cf. WP II, 666 — Skt. cf. cāráḥ, śāráḥ, id.' The page has the form Nourai prints, but Mann's gloss for it is 'motley', not 'sparrow', and he hedges both the form and the root.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"IEC\", \"where\": \"p. 613 s.v. Ḱeros (3)\", \"stance\": \"contradicts\", \"note\": \"Mann's other page gives the Sanskrit cognate as 'Skt. śaráḥ “motley”' — with ś-, and glossed 'motley', confirming that the bird sense belongs only to Persian and Greek.\"},\n            {\"src\": \"POK\", \"where\": \"p. 991\", \"stance\": \"silent\", \"note\": \"Pokorny's sper-(g-) has no Indo-Aryan member at all: the material is Germanic, Greek, Baltic, Tocharian, Celtic.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. II 666\", \"stance\": \"silent\", \"note\": \"WP II 666 likewise lists no Sanskrit form under the sparrow root.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Germanic\",\n          \"words\": \"sparwan\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Proto-Germanic *sparwan- 'sparrow' (an n-stem) is directly attested in Gothic sparwa, Old English spearwa, Old High German sparo, Old Icelandic spǫrr (< *sparwaz); the German diminutives MHG sperlinc, NHG Sperling belong here too, as does Sperber 'sparrow-hawk' (OHG sparwāri). It continues the suffixed o-grade *spor-wo- of PIE *sper-, with the Germanic sound shift leaving *sp- untouched and *o > a.\",\n          \"derivation_fa\": \"صورت ژرمنیِ آغازینِ *sparwan- «گنجشک» (ستاک n-دار) در گوتی sparwa، انگلیسی باستان spearwa، آلمانی علیای باستان sparo و ایسلندی باستان spǫrr (از *sparwaz) یک‌راست گواهی شده است؛ مصغّرهای آلمانی sperlinc/Sperling و نیز Sperber «قوش گنجشک‌گیر» (از sparwāri) به همین خانواده‌اند. این صورت دنبالهٔ درجهٔ o-دارِ پسوندداریِ *spor-wo- از ریشهٔ هندواروپاییِ *sper- است؛ در جابه‌جایی آواییِ ژرمنی خوشهٔ *sp- دست‌نخورده می‌ماند و *o به a بدل می‌شود. ادعای نورایی درست است.\",\n          \"sources\": [\"https://www.etymonline.com/word/sparrow\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD:1542\", \"status\": \"supports\", \"note\": \"Watkins s.v. sper-3: 'Suffixed o-grade form *spor-wo- in Germanic *sparwan- in Old English spearwa, spearwe, sparrow: SPARROW.' — Nourai's node verbatim.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"p. 991\", \"stance\": \"supports\", \"note\": \"'Got. sparwa, ags. spearwa, ahd. sparo „Sperling“ (*urgerm. *sparwan-); mhd. sperlinc, nhd. Sperling Deminutiv; aisl. spǫrr ds. aus *sparwa-z.'\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. II 666\", \"stance\": \"supports\", \"note\": \"identical material at WLD_Bd2 line 43304.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"English\",\n          \"words\": \"sparrow\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Old English spearwa (masc. n-stem) > Middle English sparwe > sparrow, with the regular Middle English lowering/vocalisation of the -we ending to -ow (cf. OE bealu > ME balwe > bale, OE mearg > marrow). No competing etymology exists.\",\n          \"derivation_fa\": \"از انگلیسی باستان spearwa (ستاک n-دار مذکر) به انگلیسی میانه sparwe و سپس sparrow، با همان تحول قاعده‌مندِ پایانهٔ -we به -ow در انگلیسی میانه (همانند mearg > marrow). ریشه‌شناسیِ رقیبی برای این واژه وجود ندارد و ادعای نورایی درست است.\",\n          \"sources\": [\"https://www.etymonline.com/word/sparrow\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins index: 'SPARROW sper-3'; entry: 'Old English spearwa, spearwe, sparrow: SPARROW.'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"s.v. sparrow\", \"stance\": \"supports\", \"note\": \"Klein's S-volume gives ME sparwe < OE spearwa, rel. to Goth. sparwa, OHG sparo.\"},\n            {\"src\": \"POK\", \"where\": \"p. 991\", \"stance\": \"supports\", \"note\": \"'ags. spearwa' heads the West Germanic list.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Greek\",\n          \"words\": \"psâros, psĕr\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Ancient Greek ψάρ (psā́r), gen. ψᾱρός, Ionic-epic ψήρ (Homeric acc. pl. ψῆρας, Iliad 16.583 and 17.755, of the starlings that scatter before a hawk), later ψᾶρος/ψάρος, is the starling Sturnus vulgaris; the homophonous adjective ψᾱρός means 'dapple-grey, speckled'. Pokorny puts it under sper-(g-) but only as 'das formantische u auch (??) in gr. ψάρ', i.e. explicitly as a doubtful case: an original *ψαρϝ-ς, gen. *ψαρϝός would be needed, and the initial ψ- for σπ- is irregular. Wiktionary and Etymonline accept the link (Proto-Hellenic *spḗr < PIE *spḗr 'sparrow, bird', cognate with English sparrow; Etymonline lists 'psar (starling)' among the cognates of sparrow), while Mann puts the same word under his *quséros 'motley' — beside ψᾱρός 'dapple' — which is where Nourai's second and third root-names come from. The word and the gloss are right; only the affiliation is contested, and Nourai's chart silently takes both sides at once.\",\n          \"derivation_fa\": \"یونانی باستان ψάρ (اضافی ψᾱρός) و گونهٔ ایونی–حماسی ψήρ (در ایلیاد، ۱۶٫۵۸۳ و ۱۷٫۷۵۵، دربارهٔ سارانی که از برابر باز می‌گریزند) و صورت متأخرتر ψᾶρος، همان پرندهٔ «سار» است؛ و صفتِ هم‌آوای ψᾱρός به معنای «خاکستریِ خال‌خال» است. پوکورنی آن را ذیل sper-(g-) می‌آورد ولی با علامت پرسشِ دوگانه: باید صورتِ کهنِ *ψαρϝ-ς، اضافی *ψαρϝός را فرض کرد و ψ- به‌جای σπ- بی‌قاعده است. ویکی‌واژه و اتیمونلاین این پیوند را می‌پذیرند (هلنیِ آغازین *spḗr از هندواروپایی *spḗr «گنجشک، پرنده»، هم‌ریشه با sparrow انگلیسی)، حال آنکه مان همین واژه را ذیل *quséros «رنگارنگ» و در کنار ψᾱρός «خال‌خال» می‌نهد — و نام‌های دوم و سومِ ریشه در جعبهٔ نورایی از همین‌جا آمده است. واژه و معنا درست است و تنها وابستگیِ ریشه‌ای محلِ گفت‌وگوست؛ نمودار نورایی بی‌آنکه بگوید هر دو طرف را یک‌جا پذیرفته است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%CF%88%CE%AC%CF%81\", \"https://www.etymonline.com/word/sparrow\"],\n          \"ref_check\": [\n            {\"ref\": \"IEC:613,1056\", \"status\": \"supports\", \"note\": \"IEC leaf 585 (folio 1056): 'Gk. psārós, adj. “motley”; psēr, gs: -ós, beside psār, m. “starling”' — both of Nourai's Greek forms and his gloss 'starling' come from this page; leaf 347 (folio 613) has only the Greek kērulos.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"p. 991\", \"stance\": \"partial\", \"note\": \"'das formantische u auch (??) in gr. ψάρ, ion. ep. ψήρ (hom. Akk. Pl. ψῆρας), Gen. ψᾱρός „Star“ (ursprüngl. *ψαρϝ-ς, Gen. *ψαρϝός?), jünger ψᾶρος, ψάρος m. ds., ψᾱρός „stargrau“' — the connection is made, but flagged doubtful.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. II 666\", \"stance\": \"partial\", \"note\": \"same wording as Pokorny's source at WLD_Bd2 line 43302 ff.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins s.v. sper-3\", \"stance\": \"silent\", \"note\": \"Watkins keeps only the Germanic branch; Greek ψάρ is not listed under sper-3.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\n"
}
```


### [2026-09-14T02:44:58.909Z] TOOL RESULT

```
File created successfully at: /home/sfmqrb/git/rishe/data/verification/page-467.json (file state is current in your context — no need to Read it back)
```


## [2026-09-14T02:45:01.228Z] TOOL CALL #65: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-467.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 467"
}
```


### [2026-09-14T02:45:02.646Z] TOOL RESULT

```
JSON OK
nodes verified: 18/18
node verdicts: {'confirmed': 11, 'transcription_suspect': 1, 'plausible': 5, 'disputed': 1}
root verdicts: {'confirmed': 2, 'plausible': 1}
ref checks: {'supports': 16, 'not_checked': 2, 'partial': 4}
books consulted: {'supports': 29, 'silent': 9, 'partial': 11, 'contradicts': 1} | by book: {'POK': 9, 'KLN': 8, 'WLD': 7, 'SKT': 7, 'PHD': 3, 'BQT': 3, 'IEC': 3, 'SNS': 2, 'HRN': 2, 'MON': 2, 'BRT': 1, 'HUB': 1, 'NYB': 1, 'AHD': 1}
```


## [2026-09-14T02:45:21.909Z] AGENT

Page 467 (book p. 437) verified — `data/verification/page-467.json`, `verify_check.py 467` shows **0 PROBLEM lines**, 18/18 nodes.

**Counts** — roots: 2 confirmed, 1 plausible. Nodes: 11 confirmed, 5 plausible, 1 disputed, 1 transcription_suspect. Ref checks: 16 supports, 4 partial, 2 not_checked. 14 different books consulted.

**Flagged items**

- `transcription_suspect` — **Spelgh #3 Sanskrit "splîhân"**: no Sanskrit form with initial s- exists; the word is plīhán- (प्लीहन्). `error_in: "book"` — the printed page really reads *splîhân* (page PNG saved to `data/verification/sources/refs/ocr/BOOK/467.png`); Nourai has written Klein's/Watkins's reconstruction *\*splgh-en* as if attested. Even his own citation, SNS p. 176, prints `pllhan-`.
- `disputed` — **Sper #3 Sanskrit "čârah : sparrow"**: Mann (IEC 1056) glosses `cāráḥ, śāráḥ` "motley", not "sparrow"; Nourai carried the bird gloss down into the Sanskrit box. The real Sanskrit words are śāra- "dappled" and śāri-/śārikā- "myna"; cāra- means "going, spy".
- `plausible` root — **Sper, Qusĕros, Kĕros**: Nourai has fused Pokorny's Germanic/Greek bird root *sper-(g-) with Mann's separate *quséros/*ḱeros "motley". Also **POK:997 is the wrong page** — Pokorny's sparrow root is on p. 991 (p. 997 falls inside (s)p(h)ereg- "sprinkle"); Nourai copied the error from Watkins's bracket "[Pok. sper-(g)- 997]".
- `plausible` nodes: Persian پینه (only Mann IEC 971 has the etymology; Mo'in gives no origin tag, Dehkhodā only the folk etymology پی‌نه); Pahlavi/Persian سار (no Pahlavi attestation in MacKenzie or Nyberg — Mo'in's "(پ.)" tag only; and the gloss should be **starling**, not sparrow, in three boxes); Germanic node (spithra is Old English, not Germanic; *spannjan* should be *spannan*); Greek ψάρ (Pokorny attaches it with an explicit "(??)").

**Extraction errors: none.** The JSON matches the printed page everywhere I checked, including `splîhân`, `spannjan`, `pendĕre`, `pondô`, `سار ۳` + the four variants, and the Dehkhodā quote. Only cosmetic difference: the page prints سپُرز with a damma, the JSON has سپرز.

Confirmed refs worth noting: POK:987, POK:988, IEC:613/971/1056 (all three IEC folios verified exactly from the scan's marginal page numbers) and HRN:155 (Horn no. 702) all land precisely where Nourai says. KLN:1492 has the right content but our unpaginated 1966 scan couldn't confirm the folio.
