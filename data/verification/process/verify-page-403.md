# Verification process log — verify-page-403


## [2026-09-14T00:53:01.245Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 403 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-403.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-403.json. Write /home/sfmqrb/git/rishe/data/verification/page-403.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 403` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T00:53:02.342Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T00:53:03.175Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T00:53:03.192Z] TOOL RESULT

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


## [2026-09-14T00:53:03.675Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-403.txt"
}
```


### [2026-09-14T00:53:03.689Z] TOOL RESULT

```
1	=== PDF page 403 (book page 373) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Pilo, Pislos : hair  (refs POK:830; IEC:940,1650)
4	#1 (parent #0) [Persian] refs=IEC:940,1650 | pîleh «پیله» : cocoon
5	#2 (parent #0) [Latin] refs=AHD:1535; IEC:1650 | pilus : hair ; pileus : felt cap
6	  #3 (parent #2) [English] refs=AHD | pile, pluck, plush, caterpillar, pillage
7	#4 (parent #0) [Greek] refs=IEC:1650; AHD:1535 | pilos : felt
8	  #5 (parent #4) [English] refs=AHD | pilocarpine
9	--- entry 1 ---
10	ROOT [Indo-European] Pin : wood, tree stump  (refs POK:830)
11	#1 (parent #0) [Greek] refs=POK:830; SYN:345 | pinakx : board, platter
12	  #2 (parent #1) [Persian] refs=BQT:1502 | pangân «پَنگان» : cup
13	    #3 (parent #2) [Arabic] refs=None | 
14	      #4 (parent #3) [Persian] refs=MON | fenjân «فنجان» : cup
15	--- entry 2 ---
16	ROOT [Sanskrit] Pippalî : pepper  (refs AHD:1535; KLN:1154; SYN:382)
17	#1 (parent #0) [Persian] refs=BQT:1499; FVF:503 | pelpel «پلپل» : pepper
18	  #2 (parent #1) [Arabic] refs=FVF:503 | felfel : pepper
19	    #3 (parent #2) [Persian] refs=BQT:1499 | felfel «فلفل» : pepper
20	#4 (parent #0) [Greek] refs=AHD:972 | peperi
21	  #5 (parent #4) [Latin] refs=None | 
22	    #6 (parent #5) [English] refs=KLN:1154 | pepper
23	
```


## [2026-09-14T00:53:06.573Z] TOOL CALL #3: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/data/extracted/batch/page-403.json",
 "description": "Read source JSON page 403"
}
```


### [2026-09-14T00:53:06.620Z] TOOL RESULT

```
{
  "pdf_page": 403,
  "book_page": 373,
  "entries": [
    {
      "root": {
        "name": "Pilo, Pislos",
        "lang": "Indo-European",
        "refs": "POK:830; IEC:940,1650",
        "gloss": "hair"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "IEC:940,1650",
          "words": [
            {"translit": "pîleh", "gloss": "cocoon", "script": "پیله"}
          ],
          "note": null,
          "quote": {
            "text": "کرم پیله همی بخود بتند - که همی بند گرددش چپ و راست",
            "poet": "Mas`ŭd Sa`d Salmân"
          }
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD:1535; IEC:1650",
          "words": [
            {"translit": "pilus", "gloss": "hair", "script": null},
            {"translit": "pileus", "gloss": "felt cap", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "pile, pluck, plush, caterpillar, pillage", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Greek",
          "refs": "IEC:1650; AHD:1535",
          "words": [
            {"translit": "pilos", "gloss": "felt", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "pilocarpine", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Pin",
        "lang": "Indo-European",
        "refs": "POK:830",
        "gloss": "wood, tree stump"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Greek",
          "refs": "POK:830; SYN:345",
          "words": [
            {"translit": "pinakx", "gloss": "board, platter", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:1502",
          "words": [
            {"translit": "pangân", "gloss": "cup", "script": "پَنگان"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Arabic",
          "refs": null,
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Persian",
          "refs": "MON",
          "words": [
            {"translit": "fenjân", "gloss": "cup", "script": "فنجان"}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Pippalî",
        "lang": "Sanskrit",
        "refs": "AHD:1535; KLN:1154; SYN:382",
        "gloss": "pepper"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "BQT:1499; FVF:503",
          "words": [
            {"translit": "pelpel", "gloss": "pepper", "script": "پلپل"}
          ],
          "note": null,
          "quote": {
            "text": "تو گویی پلپل سوده بکف داشت - پراکند از دو کف در دیده پلپل",
            "poet": "Manŭchehrî"
          }
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Arabic",
          "refs": "FVF:503",
          "words": [
            {"translit": "felfel", "gloss": "pepper", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "BQT:1499",
          "words": [
            {"translit": "felfel", "gloss": "pepper", "script": "فلفل"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD:972",
          "words": [
            {"translit": "peperi", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Latin",
          "refs": null,
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "English",
          "refs": "KLN:1154",
          "words": [
            {"translit": "pepper", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
```


## [2026-09-14T00:53:07.247Z] TOOL CALL #4: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-14T00:53:07.295Z] TOOL RESULT

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


## [2026-09-14T00:53:16.015Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nfor k in ['POK','IEC','AHD','SYN','KLN','BQT','MON','FVF','FVQ','PLA','AFM','SKT','LKT','HJB','ARY','HRN','HUB','WLD','LAT','LEW','TAD','ARB','WEB','FSD','RCH']:\n    v=d.get(k)\n    print('==',k, json.dumps(v,ensure_ascii=False)[:600] if v else 'MISSING')\n\"",
 "description": "Inspect refs_online metadata"
}
```


## [2026-09-14T00:53:16.727Z] TOOL CALL #6: Bash

```json
{
 "command": "sed -n 1,80p /home/sfmqrb/git/rishe/tools/verify_check.py",
 "description": "Read verify_check tool"
}
```


### [2026-09-14T00:53:17.095Z] TOOL RESULT

```
== POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_
== IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 
== AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,
== SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves
== KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h
== BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118
== MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په
== FVF {"title": "S.M.A. Emam Shushtari, Farhang-e Vazheha-ye Farsi dar Zaban-e Arabi, Anjoman-e Asar-e Melli 58, Tehran 1347/1968", "kind": "website", "url": "https://noorlib.ir/book/info/105056 (page viewer: https://noorlib.ir/book/view/105056?pageNumber=<N>&viewType=pdf) ; https://ketabnak.com/book/48613 (818 pp. PDF, login) ; http://parsianjoman.org/?p=1265 (download post)", "lookup_hint": "Alphabetical by Persian headword; noorlib page number N is the scan page — browser needed to read. Not on archive.org.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "PDF exists 
== FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sou
== PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 lea
== AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/
== SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves
== LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 
== HJB {"title": "H. Yule & A. C. Burnell, Hobson-Jobson, 2nd ed. by W. Crooke, London 1903 (Delhi reprint 1968)", "edition_found": "1903 Crooke edition (pagination identical to the 1968 reprint)", "kind": "archive_djvu", "url": "https://archive.org/details/hobsonjobsonagl02croogoog", "identifier": "hobsonjobsonagl02croogoog (others: bub_gb_6Z5iAAAAMAAJ, hobsonjobsonglos00yulerich, india.history.resource.89053)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HJB.txt", "page_offset": "leaf = printed + 35..51 (plates inserted; e.g. leaf 83 = p.32, leaf 319 = p.270, leaf 535 = p.4
== ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 
== HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 
== HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol
== WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039
== LAT {"title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951", "edition_found": "1951 (3rd ed.) - matches Nourai", "kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "identifier": "ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine (4th ed. 1959 lending-only: dictionnairetymo0000unse; another open copy: DictionnaireEtymologiqueDeLaLangueLatine)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt", "page_offset": "leaf = printed + 18 for mos
== LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt", "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f b
== TAD {"title": "Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-hurufihi (2nd ed. Cairo 1932, ed. Yusuf Tuma al-Bustani; later Library of Lebanon reprint) — Nourai lists it under Arabic authors ('Unaysi T.'); its Table IV line was lost in the OCR", "kind": "archive_djvu", "url": "https://archive.org/details/TOB1932ARAR (1932 ed.); also https://archive.org/details/ar113lang79 and https://archive.org/details/elshandawily14640", "lookup_hint": "Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; insi
== ARB {"title": "al-Jawaliqi, al-Mu'arrab min al-kalam al-a'jami, Tehran 1966 (reprint of Ahmad M. Shakir's Cairo 1361/1942 edition)", "kind": "archive_djvu", "url": "https://archive.org/details/mo3rb (probably the Shakir edition) ; https://archive.org/details/almo3rab_gwaliqy_f_abduraheem (F. 'Abd al-Rahim ed., Damascus 1990) ; also uc1.aa0003615705 / AAlexandrina-148752 (Sachau's Leipzig 1867 ed.) ; text on shamela.ws", "lookup_hint": "Alphabetical Arabic headwords; grep in ARB_mo3rb.txt / ARB_abdulraheem.txt (raw, no page breaks); edition of mo3rb not confirmed — check its title page image.", "lo
== WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/W
== FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt
== RCH {"title": "J. Richardson, A Dictionary, Persian, Arabic and English, new ed. by F. Johnson, London 1829 (Lahore reprint 1984)", "edition_found": "1829 Johnson edition (DLI scan, 1814 leaves)", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.24303", "identifier": "in.ernet.dli.2015.24303 (other editions: 1806-10 a-dictionary-persian-arabic-and-english-vol.-i, india.history.resource.17812; 1852 Johnson dictionarypersia00johnuoft)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/RCH.txt", "page_offset": "leaf ~= printed + 93..94 (e.g. leaf 336 =
```


### [2026-09-14T00:53:17.152Z] TOOL RESULT

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
```


## [2026-09-14T00:53:26.539Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -A25 -i \"^ *pilo-\" AHD_watkins1985.txt | head -60; echo \"=== pin\"; grep -n -B2 -A20 -i \"pin-.*Wood\\|pin- *$\" AHD_watkins1985.txt | head -60",
 "description": "grep AHD Watkins for pilo- and pin-"
}
```


### [2026-09-14T00:53:27.580Z] TOOL RESULT

```
853:pilo-. Hair. A possible root. 1. Latin pilus, hair: PELAGE, PILAR, PILE’, PILOSE, PILUS, PLUCK, PLUSH, POILU; CAT- ERPILLAR, DEPILATE. 2. Suffixed reduced form “pil-so- possibly in: a. Latin pilleus, pileus, felt cap: PILEUS, PILLAGE; b. Greek pilos, felt: PILOCARPINE. [Pok. pi-lo- 830.]
854-pipp-. To peep. Imitative root. 1. Latin pipdre, to chirp (> Old High German pfiffa, pipe): FIFE, PIPE. 2. Latin pipire, to chirp: PIGEON. 3. Gaelic piob, a pipe, in Scot- tish Gaelic piobaireachd, pipe music: PIBROCH. [Pok. pip(p)- 830.]
855-[pippali. Pepper. Sanskrit noun of unknown origin. Possibly related to pippala, the bo tree. 1. Sanskrit pippali: PEPPER, (PIMPERNEL). 2. Sanskrit pippalam: PEEPUL.]
856-[pius. Dutiful, devoted, pious. Latin word having cog- nates in other Italic languages. PIACULAR, (PIETA), PI- ETY, PIOUS, PITTANCE, PITY; EXPIATE, IMPIOUS.]
857-plab-. To flap. Imitative root. Middle English flappen, to flap: FLAP [Pok. plab- 831.]
858-plak-'. Also plak-. To be flat. Extension of pele-2. 1. Germanic *fléh6 in Old Norse fl6, layer, coating: FLOE. 2. Variant form *pldg- in: a. Germanic *flék- in Old English fléc, flatfish: FLUKE!; b. Germanic *flakaz in Norwegian flak, flat piece, flake, probably akin to the Scandinavian source of Middle English flake, flake: FLAKE}; c. Germanic *flak- in Old Norse flaki, fleki, hurdle: FLAKE?. 3. Extended form *plakd in Germanic *flag6 in Old Norse flaga, layer of stone: FLAG, FLAW}. 4. Possibly suffixed (stative) form *plak-é-, to be calm (as of the flat sea), in Latin placére, to please, be agreeable: PLACEBO, PLACID, PLEA, (PLEAD), PLEASANT, PLEASE; COMPLACENT. 5. Lengthened suffixed form *plak-G- in Latin placdre, to calm (causative of placére): PLACABLE, PLACATE. 6. Nasalized form *pla-n-k- in Latin plancus, flat, flat-footed, whence planca, board: PLANCHET, PLANK, PLANK-SHEER. 7. Variant form *plag- in: a. perhaps Latin plaga, net (? < “something ex- tended”): PLAGIARY; b. Greek plagos, side: PLAGAL, PLAGIO-, PLAYA. 8. Root form *plak- in Greek plax, flat, flat land, surface: PLACENTA, PLACOID. 9. Variant form *pelag- in Greek pelagos, sea: PELAGIC; ARCHIPELAGO. [Pok. 1. pla-k- 831.]
859-plak-2. To strike. 1. Nasalized variant forms *pla-n-k-, *pla-n-g- in: a. Germanic *flang- in Old Norse flengja, to flog, whip, akin to the Scandinavian source of Middle English flingen, to fling: FLING; b. Latin plangere, to strike (one’s own breast), lament: PLAINT, PLANGENT; COMPLAIN. C. suffixed form *plang-yo- in Greek plazein, to drive away, turn aside: PLANKTON. 2. Variant form *plag- in Latin plaga, a blow, stroke: PLAGUE. 3. Suf- fixed form *pldk-yo- in Greek pléssein, to beat, strike: PLECTRUM, -PLEGIA, PLEXOR; APOPLEXY, CATAPLEXY, PARAPLEGIA. [Pok. 2. pldk- 832.]
860-plat-. To spread. Extension of pele-?. 1. Variant form *plad- in Germanic *flataz, flat, in: a. Old Norse flatr, flat: rLAT!; b. Old French flater, to flatter: FLATTER!. 2. Suffixed variant form *plad-yo- in Germanic *flatjam in Old English flei(t), floor, dwelling: FLAT?. 3. Basic form *plat- in Germanic *flathd(n), flat cake, in Late Latin
861-plegan
862-flad6, flat cake, pancake: FLAN. 4. Germanic nasalized suffixed form *flu-n-th-r-j6- in Old Swedish flundra, flatfish, flounder, probably akin to the Scandinavian source of Middle English flounder, flounder: FLOUNDER?. 5. Nasalized form *pla-n-t- in Latin planta, sole of the foot, and denominative plantdre, to drive in with the sole of the foot, plant, whence planta, a plant: CLAN, PLAN, PLANT, PLANTAIN!, PLANTAR; PLANTIGRADE, SUPPLANT. 6. Suffixed form “plat-u- in Greek platus (feminine plateia), flat, broad: PIAZZA, PLACE, PLAICE, PLANE‘, (PLANE TREE), PLATE, (PLATEAU), (PLATITUDE), (PLATY?), PLATY-, (PLAZA). [Pok. plat- 833.] [plegan. To pledge for, stake, risk, exercise oneself. West Germanic verb. 1. Old English plegian, to exercise one- self, play: PLAY. 2. Late Latin plevium (> Old French plevir, to pledge), pledge, guarantee: PLEDGE; REPLEVIN. 3. Germanic derivative noun *plehti- in Old English pliht, danger, peril: PLIGHT?.] plek-. To plait. Extension of pel-*. 1. Suffixed o-grade form *plok-so- in Germanic *flahsam, flax, in Old Eng- lish fleax, flax: FLAX. 2. Full-grade form *plek- in Latin -plex, -fold (in compounds such as duplex, twofold; and supplex, “with legs folded under one,” kneeling, entreat- ing; see dwo-, upo): MULTIPLEX, QUINTUPLE, SUPPLE. 3. Latin plicdre, to fold (also in compounds used as denominatives of words in -plex, genitive -plicis): PLAIT, PLIANT, PLICA, PLICATE, PLIGHT!, PLISSE, PLY!; APPLY, COMPLICATE, COMPLICE, DEPLOY, DISPLAY, EMPLOY, EXPLICATE, IMPLICATE, REPLICATE, SUPPLICATE. 4. Suf- fixed forms “plek-to- and *plek-t-to- in Latin plectere (past participle plexus), to weave, plait, entwine: PLEACH, PLEXUS; AMPLEXICAUL, COMPLECT, (COMPLEX), PERPLEX. 5. Greek plekein, to plait, twine, and plektos, twisted: PLECOPTERAN, PLECTOGNATH. [Pok. plek- 834.] plék-. Also pleik-. To tear. 1. Zero-grade form *pbk- becoming *plak- in Germanic *flahan in Old English fléan, to strip the skin from: FLAY. 2. Suffixed o-grade form “ploik-sk- perhaps in Germanic “flaiskjan, piece of flesh torn off, in Old English flésc, flesh: FLESH. 3. Zero-grade form *plik- in Germanic *flikkja in: a. Old English flicce, side of a hog: FLITCH; b. Germanic ablaut form *flekkja in Old Norse flekkr, piece of skin or flesh, spot, stain: FLECK. [Pok. plék- 835.] pleu-. To flow. I. Basic form “pleu-. 1. Latin pluere, to rain: (PLOVER), (PLUVIAL), PLUVIOUS. 2. Greek pleusis, sailing: PLEUSTON. 3. Suffixed zero-grade form *plu-elos dissimilated into Greek puelos, trough, basin: PYELITIS. 4. Suffixed form *pl/(e)u-mon-, ‘‘floater,” lung(s), in: a. Latin pulmé (< *plumonés), lung(s): PULMONARY; b. Greek pleumén, pneumon, lung: PNEUMONIA, PNEU- MONIC. 5. Suffixed o-grade form *plou-to- in Greek plou- tos, wealth, riches (< ‘‘overflowing’’): PLUTO; PLUTOCRACY. 6. Lengthened o-grade form *pl6(u)- in: a. Germanic *fléwan, to flow, in (i) Old English flowan, to flow: FLOW (ii) perhaps Middle Dutch vluwe, fishnet: FLUE?; b. suffixed form *pld-tu- in Germanic *fléduz, flowing water, deluge, in Old English fléd, flood: FLOOD. II. Extended form *pleuk-. 1. Germanic *fleugan, to fly, in Old English fléogan, to fly: FLY!. 2. Germanic *fleu- gon-, flying insect, fly, in Old English fléoge, a fly: FLY?. 3. Probably Germanic *fleuhan, to run away, in Old English fléon, to flee: FLEE. 4. Germanic causative *flauhjan in Old English flygan, flégan, to put to flight: FLEY. 5. Germanic suffixed form *fleug-ika in Old French fleche, arrow: FLECHE, FLETCHER. 6. Zero-grade form *pluk- in: a. Germanic *flugja-, feather, in Old English -flycge, with feathers (only in unfligge, featherless): FLEDGE; b. suffixed form *flug-ti- in Old English flyht, act of flying, and *flyht, act of fleeing, escape: FLIGHT, FLIGHT?; Cc. possibly (but unlikely) suffixed form *flug- laz, dissimilated into *fuglaz, bird, in Old English fugol, bird: FowL; d. Germanic suffixed form *flug-ila in Mid- dle High German viiigel (> Germanic Fliigel), wing: FLUGELHORN, FUGLEMAN. III. Extended form *pleud-.
863-poti-
864-1. Germanic *fleutan in Old English fléotan, to float, swim: FLEET!, FLEET2, 2. Zero-grade form *plud- in Germanic *flut-, *flot- in: a. Germanic derivative *floton, to float, in (i) Old English flotian, to float: FLoaT (ii) Old French floter, to float: FLOTSAM; b. Old Norse floti, raft, fleet: FLOTILLA; c. Old English floterian, flotorian, to float back and forth (-erian, iterative and frequentative suffix): FLUTTER; d. Germanic *flutjan, to float, in Old Norse flytja, to further, convey: FLIT. 3. Probably Ger- manic suffixed form *flaut-sta-, contracted into *flausta- in Icelandic flaustr, hurry, and flaustra, to bustle, akin to the probable Scandinavian source of FLUSTER. [Pok. pleu- 835, pl(e)u-mon- 837.] pleus-. To pluck; a feather, fleece. 1. Germanic *fleusaz, fleece, in Old English fléos, fleece: FLEECE. 2. Suffixed zero-grade form *plus-ma in Latin pliima, a feather: PLUMATE, PLUME, PLUMOSE, PLUMULE; DEPLUME. [Pok. pleus- 838.] plou-. Flea. 1. Extended form *plouk- in Germanic *flau- haz in Old English fléa(h), flea: FLEA. 2. Extended zero-grade form *plus- metathesized into *pusl- in: a. Latin pilex (< *puslex), flea: PUCE; PULICIDE; b. Greek psulla, flea: PSYLLA. [Pok. blou- 102.] [plumbum. Lead. Latin noun, probably borrowed from the same unidentified source as Greek molubdos, lead. 1. Latin plumbum: PLUMB, PLUMBAGO, PLUMBER, PLUMBISM, PLUMMET, PLUNGE; APLOMB, PLUMBIFEROUS. 2. Greek molubdos: MOLYBDENUM.] pneu-. To breathe. Imitative root. 1. Germanic *fneu- in Old English fnéosan, to sneeze: SNEEZE. 2. Greek pnein, to breathe (> pnoia, breathing): APNEA, DIPNOAN, DYSP- NEA, EUPNEA, HYPERPNEA, HYPOPNEA, POLYPNEA, TACHYPNEA. 3. Suffixed form *pneu-mn in Greek pneuma, breath, wind, spirit: PNEUMA, PNEUMATIC, PNEUMATO-, PNEUMO-. [Pok. pneu- 838.]
865-pdo(i)-. To drink. Contracted from *poo(i)-. I. Basic form *p6(i)-. 1. Suffixed reduced form *pd-to- in Latin pdtus, drunk (> pdtdre, to drink): POISON, POTABLE, POTATION, POTATORY, POTION. 2. Reduplicated form *pi-poa-o-, whence *pi-bo-, assimilated to *bi-bo- in Latin bibere, to drink: BEVERAGE, BIB, BIBULOUS; IMBIBE. 3. Suffixed zero-grade form *po-ti-, *po-ti- in Greek posis, drink, drinking: sympostum. II. Zero-grade form *pi- (< *pia-). 1. Suffixed form *pi-ro- in Old Church Slavonic piri, feast (> Russian pir, feast): prroG. 2. Suffixed (nasal present) form *pi-no- in Greek pinein, to drink: prnocy- tosis. [Pok. 2. pd(i)- 839.]
866-pol-. Finger. Possibly the same root as pol-. Latin pollex, thumb: POLLEx. [Pok. polo- 840.]
867-p6l-. To touch, feel, shake. 1. Germanic *féljan, to feel, in Old English félan, to examine by touch, feel: FEEL. 2. Reduplicated zero-grade form *pal-p- in: a. Latin palpus, a touching: PALP; b. Latin palpdri, palpdre, to stroke gently, touch: PALPABLE, PALPATE!, PALPITATE; c. Latin palpebra, eyelid (< ‘that which shakes or moves quickly”): PALPEBRAL. 3. Perhaps suffixed zero-grade form *pal-yo- in Greek pallein, to sway, brandish: CATA- PULT. 4, Perhaps suffixed form “psal-yo- in Greek psal- lein, to pluck, play the harp (but more likely of imitative origin): PSALM, PSALTERY. [Pok. 1. G. pel- 801.] [po6mum. Apple. Latin noun of unknown origin. POMACE, POMADE, POME.]
868-[populus. People. Latin noun of Etruscan origin. PEO- PLE, POPULACE, POPULAR, POPULATE, PUBLIC, PUEBLO; DEPOPULATE.]
869-porko-. Young pig. 1. Germanic *farhaz in: a. Old Eng- lish fearh, little pig: rakROW’; b. diminutive form in Middle Dutch varken, small pig: AARDVARK. 2. Latin porcus (> Old French porc), pig: PORCELAIN, PORCINE, PORK; PORCUPINE, PORPOISE, (PURSLANE). [Pok. porko-s 841.]
870-poti-. Powerful; lord. 1. Latin potis, powerful, able (> potestas, power): PODESTA, POSSESS, POWER. 2. Latin compound posse, to be able (contracted from potis, able
871-prak-
872-+ esse, to be; see es-): POSSIBLE, POTENT; (IMPOTENT), PREPOTENT. 3. Form *pot- in: a. compound *ghos-pot-, “suest-master,” host (see ghos-ti-); b. compound *dems-pot-, “house-master,” ruler (see deme-'). 4. Old Persian pati-, master: PADISHAH. [Pok. poti-s 842.] [prak-. To make, do. Greek root. Greek prassein (Attic prattein), to effect, do: PRACTICAL, (PRACTICE), PRAG- MATIC, PRAXIS. [In Pok. 1. per 811.]] prek-. To ask, entreat. 1. Basic form *prek- in Latin *prex, prayer (attested only in the plural precés), with denominative precdri, to entreat, pray: PRAY, PRAYER?, PRECARIOUS; DEPRECATE, IMPRECATE. 2. Suffixed zero-grade form *prk-sk- becoming *pork-sk-, contracted into *posk- in suffixed form *posk-to-, contracted into *posto-, which appears in Latin postuldre, to ask, re- quest: POSTULATE; EXPOSTULATE. [Pok. 4. perk- 821.] prep-. To appear. Suffixed zero-grade form *prp-yo- in Germanic *furbjan, to cause to have a (good) appearance, polish, in Old French fo(u)rbir, to polish, burnish: FuR- BISH. [Pok. prep- 845.] preu-. To hop. 1. Zero-grade form *pru- in Germanic *fru- in Old English frogga (with obscure expressive suffix -gga), frog: FROG. 2. Extended o-grade form *prowo- in Germanic *frawaz in: a. Middle Dutch uro, “leaping with joy,” happy: FROLIC; b. Old High German fré, happy, in frewida, joy (> German Freude): scHa- DENFREUDE. [Pok. preu- 845.] preus-. To freeze, burn. 1. Germanic *freusan, to freeze, in Old English fréosan, to freeze: FREEZE. 2. Suffixed zero-grade form *prus-to- in Germanic *frustaz, frost, in Old English forst, frost, frost: FROST. 3. Suffixed form *preus-i- in Latin *preusis, *preuris, act of burning, whence denominative pririre, to burn, itch, yearn for: PRURIENT, PRURIGO, PRURITUS. 4. Suffixed zero-grade form *prus-ina in Latin pruina, hoarfrost: PRUINOSE. [Pok. preus- 846.] pri-. To love. Contracted from *pria-. 1. Suffixed form *priy-o- in Germanic “frijaz, beloved, belonging to the loved ones, not in bondage, free, in: a. Old English fréo, free; FREE; b. Dutch vrij, free: FILIBUSTER. 2. Suffixed (participial) form “priy-ont-, loving, in Germanic ‘“fri- Jjand-, lover, friend, in Old English friond, fréond, friend: FRIEND. 3. Suffixed shortened form *pri-tu- in Germanic *frithuz, peace, in: a. Old High German fridu, peace: SIEGFRIED; b. Old French esfreer, to disturb: AFFRAY; c. Germanic *frij-, peace, safety, in compound *berg-frij-, “high place of safety” (see bhergh-?). 4. Suffixed femi- nine form *priy-G, beloved, in Germanic *frijj6, beloved, wife, in: a. Old Norse Frigg, goddess of the heavens, wife of Odin: Fricc; b. Germanic compound “*frije-dagaz, “day of Frigg” (translation of Latin Veneris diés, “Ve- nus’s day”), in Old English frigedeg, Friday: FRIDAY. [Pok. prdi- 844.] prokto-. Anus. Greek prokios, anus: PROCTITIS, PROCTOL- OGY, PROCTOSCOPE. [Pok. prdkto- 846.] pster-. Also ster-. To sneeze. Imitative root. 1. Suffixed form *ster-nu- in Latin sternuere, to sneeze: STERNUTATION. 2. Suffixed form *ster-t- in Latin ster- tere, to snore: STERTOR. [Pok. pster- 846.] pu-'. Also phu-. To blow, swell. Imitative root. 1. Ex- tended form *pus- in Latin pustula, a bubble, blister: PUSTULE. 2. Perhaps extended form “pit-, penis, in Latin praepiitium, foreskin (prae-, before, in front; see per’): PREPUCE. 3. Variant form *phi- in Greek phusa (> phusan, to blow), bellows, bladder: EMPHYSEMA, PHYSO- STIGMINE, PHYSOSTOMOUS. [Pok. 1. pu- 847.] pu-2, To rot, decay. 1. Suffixed form *pi-lo- in Germanic *filaz, rotten, filthy, in: a. Old English fi, unclean, rotten: FOUL; b. Old Norse fill, foul, akin to the Scandi- Navian source of FULMAR; ¢. Germanic abstract noun *filithd in Old English fylth, foulness: FILTH; d. Ger- manic denominative *filjan, to soil, dirty, in Old English fylan, to sully: FILE’; DEFILE!. 2. Extended form *pug- in Germanic *fuk- in Icelandic fiki, rotten sea grass, and
873-réd-
874-Norwegian fogg, rank grass, probably akin to the Scandi- navian source of Middle English fog, fogge, aftermath grass: FoG?. 3. Extended variant form *pous- in Ger- manic *fausa- in Low German fussig, spongy: FUZZY. 4. Suffixed form *pu-tri- in Latin puter (stem putri-), rotten: PUTRESCENT, PUTRID; OLLA PODRIDA, (POT- POURRI), PUTREFY. 5. Suffixed form *puw-os- in: a. Lat- in pus, pus: PURULENT, PUS; SUPPURATE; b. Greek puon, puos, pus: PYO-. 6. Greek compound empuein, to suppu- rate (en-, in; see en): EMPYEMA. [Pok. 2. pii- 848.]
875-[piibés. Pubic hair. Latin noun of obscure origin. Related to Latin piaber, pabés, adult, grown-up. 1. Latin piibés, pubic hair: PUBES, PUBIC, PUBIS. 2. Latin piber, piibés, adult: PUBERTY, PUBERULENT, PUBESCENT.]
876-puk-1. To make fast. Suffixed form *puk-ino- in Greek pukinos, later puknos, strong, fast, thick: PYKNIC; PYC- NIDIUM, PYCNOMTER. [Pok. 2. puk- 849.]
877-puk-2, Bushy-haired. Suffixed form *puk-so- in: a. Ger- manic *fuhsaz, fox, in Old English fox, fox: Fox; b. Ger- manic feminine *fuhsdn- in Old English fyxe (> Middle English fixen), she-fox: VIXEN. This root is in part a taboo deformation of wikwo- and wip-é-. [Pok. pik- 849.]
878-[pulé. Gate. Greek noun of obscure origin. PYLON, PYLO- RUS; AEOLIPILE, MICROPYLE, PROPYLAEUM, PROPYLON.]
=== pin
```


## [2026-09-14T00:53:27.719Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==(830+8)' POK_01.txt | head -120",
 "description": "Pokorny page 830"
}
```


### [2026-09-14T00:53:28.765Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T00:53:44.463Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls | head -50; echo ---; for f in POK_01.txt POK_02.txt POK_03.txt POK_full.txt; do echo \"== $f\"; python3 - \"$f\" <<'EOF'\nimport sys\nt=open(sys.argv[1],encoding='utf-8',errors='replace').read()\nprint('formfeeds',t.count('\\f'),'len',len(t))\nEOF\ndone",
 "description": "List refs dir and POK page counts"
}
```


### [2026-09-14T00:53:45.595Z] TOOL RESULT

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
---
== POK_01.txt
formfeeds 363 len 966268
== POK_02.txt
formfeeds 433 len 1119436
== POK_03.txt
formfeeds 429 len 1150862
== POK_full.txt
formfeeds 0 len 3967710
```


## [2026-09-14T00:53:46.251Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"pi-lo-\\|pilo-\\|pīlo\" POK_full.txt | head -20; echo \"=== pin\"; grep -n \"^pin-\\|pin- *:\\|Holzstück\" POK_full.txt | head -20",
 "description": "grep Pokorny full for pilo and pin"
}
```


### [2026-09-14T00:53:46.316Z] TOOL RESULT

```
67949:Root / lemma: pi-lo- 
67955:Root / lemma: pi-lo- : hair, felt, : Root / lemma: pu-lo- : "hair, felt ' derived from Root / 
69225:Root / lemma: pi-lo- : hair' : Root / lemma: pu-lo- : hair' derived from Root / lemma: pleuk- 
=== pin
```


## [2026-09-14T00:53:49.435Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '67930,68010p' POK_full.txt",
 "description": "Pokorny db dump around pilo"
}
```


### [2026-09-14T00:53:49.528Z] TOOL RESULT

```
References: WP. II 70; compare Feist 155 f. 

Page(s): 830 



Root / lemma: pik(h)o- 

Meaning: lump, knot 

Material: Avestan yO/A'5- "knot' in nava-pixem "neunknotigen'; Latvian piks, pika^E.x6- and 

Lehmklumpen', sniega-pika "Schneeballen'. 

References: WP. II 70. 

Page(s): 830 

Root / lemma: pi-lo- 

Meaning: hair, felt 

Note: 

Root / lemma: pi-lo- : hair, felt, : Root / lemma: pu-lo- : "hair, felt ' derived from Root / 

lemma: pel-2a, pela- : pla- : to cause to move, drive, felt. 

Material: Latin pilus m. "hair', whereof as collective "Haarknauel' also pilai. " ball, bale, 

Strohpuppe'; auf an 5-stem based on 'yO/T-s-os "verfilzf, in gr. mkoc, m. " felt ', ttTAsoj "filze', 

Latin pilleus, -ei//77 "Filzkappe, FilzmiJtze' ( *pilseio-)\ Old Church Slavic pl-bstb " felt '. 

References: WP. II 71, WH. II 302 f., 304 f. 

Page(s): 830 



Root / lemma: pi-n- 

Meaning: a piece of wood 

Material: Old Indie /0/>75/r5-/77 'staff, stick, club, mace, joint'; gr. iTiva^, -qkoc; 'Sparre, balk, 

beam, board, Schreibtafel, Gemalde'; Old High German witu-f?na\.. Middle Low German 

K/>7e"Holzhaufen'; Old Church Slavic ptnt m., serb. panjeic. "tree truck, -strunk'. 

References: WP. II 71; Vasmer2, 335; 

See also: probably to spei- "sharp, pointed bit of wood'. 

Page(s): 830 

Root / lemma: pTp(p)- 

Meaning: to squeak 

Note: also unredupl. pA-with variant derivatives, onomatopoeic word 

Material: Old Indie pippaka "ein certain bird', pippTka- "ein bird'? gr. nTno(; f. or ninTTO(; m. 

"young bird', nlncb, nirrpa f. "a kind of Baumhacker', nin(n)i^u) "piepe'; Latin pTpilo, -are, 

pTpio, -Tre, pTpo, -^/'e"piepen', pip(p)itare^oi Naturlaut the Mause', pTpulum^ ^qs Wimmern', 

Oscan yC>//75//c» "clamor plorantis'. Modern High German (Low German) piepen {\n\Vc\ 

verhinderter consonant shift); Lithuanian yOyyO//"whistle' (loanword?); Czech pipteti 

"piepsen', sloven, pfpa^ chicken; duct, tube, pipe', serb. pipa, eine disease, malady of the 

chicken ' (Modern High German Pips) etc.; 

Czech yC>//ra//"piepen', ; Bulgarian pile, Serbo-Croatian /7//e"Kuchlein' ; similarly alb. bibe 
"young water bird ', Armenian i6'/Z?e/77"pigolare', gr. nicpiy^, ni(paAAi(; "a bird'. 

References: WP. II 70, WH. II 309; Vasmer2, 363 f.
```


## [2026-09-14T00:53:50.881Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Page(s): 830\" POK_full.txt | head; echo ===; grep -n \"pinak\\|πίναξ\\|pínax\" POK_full.txt | head",
 "description": "Pokorny page 830 entries"
}
```


### [2026-09-14T00:53:50.931Z] TOOL RESULT

```
Exit code 1
67933:Page(s): 830 
67947:Page(s): 830 
67967:Page(s): 830 
67985:Page(s): 830 
68011:Page(s): 830 
(eval):1: == not found
```


## [2026-09-14T00:54:03.534Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nprint('leaves',len(leaves))\nfor i in (485,486,487,488):\n    print('---- leaf',i)\n    print(leaves[i][:900])\nEOF",
 "description": "IEC leaves near p.940"
}
```


### [2026-09-14T00:54:04.632Z] TOOL RESULT

```
leaves 858
---- leaf 485
; OE ear (queried: “harrow'). (Iso- phone: Umb. ocar, ocri ‘treasury’). Cf. akris
oks- ‘sharp, rough, bitter, harsh’. See next Skt. aksám “blue vitriol’; Arm. ox, gs. A. ab. S. -av, & ok pl. ‘spite’; Gk. oxús ‘sharp, tart; Óxos, gs. -eos, n. ‘vinegar; Lat. oscus (rough, coarse’. Phonol. of musca, viscum, misceo, ascia, etc.); OBr. och, s. “point of sword’; Latv. (ambig.) a8s (*quick, alert. Cf. aks-, aK-, etc.)
oks- (variant of above) (?). Cf. oKus Arm. cf. an-uj8, gs: -u8i, i-st (sweet, lit. ‘not sharp); W (ambig.) cf. awch, m. (edge, sharp- ness, keenness, ardour’. But cf. aks-); OCS cf. opaší, f. (tail, if for *ap(o)-oksis 'rear- point"). (Isophones: MHG uohse, üehse, s. & wf. ‘armpit; Arm. uš, o-st. ‘thought, care
Okso, ið “drive, drive away, scare’. Cf. óKus Gk. cf. di-Óóko ('pursue', fr. *duis-^); Slovak jaSit , inf. ‘scare’; -sa, v. ‘shy, as horse; MHG cf. uohte, wf. ((2) ‘pasture
---- leaf 486
pellbound’; Gk. cf. óllumi, fut:
oKtomos (oKdom-) olni
10
20
25
30
35
40
45
872
oléo & oléso ‘destroy’ beside oloós 'destruc- tive, deadly’; cf. also (?) ól-unthos *winter- fig that does not mature’; Lat. cf. ab-oleo, -olere “destroy” beside vi-olens, -olentis (^vio- lent, fr. *uis-^) and vi-olàre, pf. -olavi ‘violate’; R cf. (?) ólux, m. ‘boor’; Li. àlinti, inf. “sup- press, starve’; aléti, inf. “live in misery’; cf. alata, mf. ‘wretch’. See Supt.
(olouos, see oluos)
olénà, olinà, olənā ‘forearm, elbow, ell" WP I, 156 Per. cf. arang ‘elbow’; Oss. cf. árm-àárin, Dig. cáng-arinà "elt: Gk. oléne, f. ‘elbow’; Alb. llânë, T llërë, f. ‘forearm; eil; Lat. ulna, Fa- liscan olina "elt": Olr. uilen & uilind, f.; Ir. uille, gs: uilleann, f. ‘elbow, forearm, bend’; OBr. elin, Br. élin, ilin, pl. -u, m. ‘elbow’; W elin, pl. au, f. ‘elbow, bend’; Cor. elyn, pl. elynnow, m. id. (and “angle'); Go. alei
---- leaf 487
��disease’; amatib, f. ‘poverty’; adj. ‘poor; amiva, f. ‘suffering’; amin, adj. ‘sick’; cf. also áme, mp. ‘oppress’; Gk. (Hom.) omoiíos (fdire, horrible, epithet of old age, war, death: Skt. amivam, A 'suffering)); Av. cf. amayavo (worthless. Queried here by
olnos — -omeno-
10
20
25
30
35
40
45
874
Justi); ON ama, v. “torment'; mod. ami, m., amstur, n.. ‘annoyance’
om- (3) ‘strength, power, ability, skill. (Cf. em- m- ‘take, hold”, etc.) Skt. ámah ‘strength’; Av. amo, m. id. (and
.'strong)). Type omotà, -is in Skt. amátih f.
(3) “form, shape, beauty’; Li. àmata, f. ‘craft, skill, trade’; Latv. amats, id. (and ‘mode, usage’). (Isophonic: àmas voice)
om- (4) (omotos, ios, omost-) ‘dead, dull, oppressive’. Cf. om- (2) Arm. amaji, adj. ((deserted, desert’, fr. *omo- tio-); s. desert; Alb. i åmtë, i àmshté, adj. *sultry; insipid; peevish; slothful; stupid"; Icel. cf. amstur, n. ‘annoyance’. S
---- leaf 488
mal to be sacri- ficed'
omsos (omes-) “shoulder”. WP I, 178 Skt. ámsah, m. id.; Av. (queried) áxmo, id.; Tokh. antse, pl: esán, id.; Arm. us, o-st., id.; Gk. ómos, m. id.; Lat. cf. umerus, humerus, gs. -i, m. id.; Umb. onse “on the shoulder’; Go. *ams, acc. pl. amsans ‘shoulder’. (Of un-
omes- — ondhos
20
25
30
35
40
45
 
876
certain origin is Arm. ant, Let 'armpit). A reduced vowel aíso arises in Gk. améso, dual. *shoulder-blades?
(omul-, see omol-)
-ön (-ünos, -ónà, -ónom), derivative suffix relating to a radical simplex. Examples are numerous. The simplex is given in brackets. Av. Caranom, acc. sg. m. (ffield, plot: Carai(mi) "go: Per. angustane, s. ( finger-ring': angust); Tadjik somon, saman (Cquietude': Av. samo); Arm. durn, pl: drunk (fgate': durk, pl. door: Gk. thurón (‘halľ: thüra); Lat. falcon ('hawk': falx); Osc. eituns ('soldiers': ei-, i- go); MIr. cammán ('crook': camm); W
```


## [2026-09-14T00:54:17.040Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"pile\\b\\|pīle\\|pile ‘cocoon\\|cocoon\" IEC.txt | head -30; echo \"=== pilos\"; grep -n \"pilos\\|pîlos\\|pilleus\\|pileus\" IEC.txt | head -20",
 "description": "grep IEC for pile/cocoon/pilos"
}
```


### [2026-09-14T00:54:17.102Z] TOOL RESULT

```
1006:budhos (?). Cf. busd- (buzd-) Gk. buthós; OE pudd ‘ditch’. Cf. E pod ‘pod, cocoon, eelnet'
1114:bhalið ‘hit, hurt. (Cf. bal-, suppt.) WP II, 189. ON bella, pt. ball, id.; Tokh. (ambig.) päl, B pile ‘wound’; OCS boljo, bolëti (ambig.) “hurt?
1251:bhermn-, bhern- ‘load’. WP II, 154 Skt. bhárman, bhariman “support, nourish- ment; Av. bareman; Oss. bärn ‘onus’; Arm. bern; Gk. phérma; Br. bern ‘pile’; Cor. bern, id.; MHG bérn ‘tribute’; Du. cf. berm ‘berme in bulwark’; OCS bréme
1440:bhld- “lump, mass”. OFris. bult ‘pile’; Du. bult “lump”; LG bult, bülte “peat; mound; tuft’; bülten ‘stacks of rushes’; bolten ‘bundle of linen’; Sw. bult, bylte, w. m. ‘bundle’; Ukr. boüd ‘rock, stone’. (MHG bolz ‘porridge’, if related, is infl. by Lat. puls)
1495:bholos, å, is ‘round lump, hump; mass, crowd’ Arm. bujik, gen. bulic “company, host? beside blur, gs blro ‘hil’; Oss. bal “band, crowd"; Du. boel “mass, pile, crowd’; ON bóla “boss, blain; bubble’; Pol. bal ‘bole’; Li. cf. buolas ‘hornless’; and cf. Latv. bolit acis ‘roll the eyes'
1783:bhrghos ‘hill, mound’. ((1)?) (bhrg&h-?) Oss. (ambig.) barz, bardz “pile, crowd'; Olr. brí (“hillock?. Loss of -g- as in rí ‘king’); Gaul. briga ‘mountain’; Br. bré, id.; W & Cor. brev, bré “hil”; ON borg (1) ‘knoll’; Cz. (in placenames) -brh ‘hill’, cf. also brh ‘stack’
1956:bhür-, is, à, om (1) ‘pile, mass, crowd’ Skt. bhürih *mass'; Av. büiri, n. id.; Gk. cf. la-phüron ‘plunder’; ge-phüra ‘mound, bridge’; Li. būrys, io ‘crowd, flock; W (*-u-) cf. bwr ‘embankment
2754:dheigh- ‘shape, earth up; form, wall (There is some confusion with dheig- above). WP I, 833. Cf. dhoigh- Skt. (ambig. prob. o-gde) dehah, am “shape, body’; Av. (pairi-) daezo ‘surrounding fence” beside diz- “earth up, cover’; LW in Arm. dez ‘mound’, dizem ‘pile up’; Gk. teikhos “outer wall, dam’; Ose. feíhüss, acc.pl. ‘walls’; Go. digan (z-gde) ‘shape, mould’; OPr. zeidis (metath. *wall') For Cz. dize ‘kneading- trough” and OHG teic, E dough, etc. see dhoiĉh-. The connexion, if any, with OE digan ‘overcome, survive, benefit’ is obscure
2882:dhom- (2) (dham-, dhóm-) (theme of a rad- ical “set, fixed’. See dhê- (2), etc.) Gk. thamüs fcompact', thamá, adv.; thámnos ‘thicket’; thaminós, adj. “close, frequent’; cf. also Hes. thaimós “family, household’; Lat. fam-ul, -ulus, -ilia; W daf, pl.-oedd “issue, output; MHG tam, gs. tammes; Du. dam ‘dam’; Go. faür-dammjan (‘dam up’. -mm- unexplained, cf. Li. domüs, j-domus “atten- tive; interesting; dome “attention? *-a- and Gk. thomós ‘pile’ *-o-)
2915:dhis- (2) (?) Per. diha ‘village’; Myc. & Gk. this, thin, gs thinós “earth, bottom, pile, silt’
2965:dhoiĝhos, om, is, iə ‘shape, mould; shaper’. Cf. dheiĝh-. WP I, 833 Skt. dehah, -am “body, mass, person’; dehth ‘rampart; Av. -daeza, in pairi- ‘rampart’; LW in Arm. dez, gs dizi “pile, rick and par- tez ‘paradise’; Tokh. A tseke ‘plastic figure’; tsek-, B tsaik- ‘to shape’; Gk. toikhos “house- wall’; Myc. to(i)ko-, id.; Gothic daigs, OHG teic, OE dag ‘dough, mass: ON deg id., deigr ‘plastic’; Pol. dzieza, Slovak dieZa, Cz. diže ('kneading-trough'. Isophonic with OE dæge *bread-maker'; ON deigja "mad": Finn. LW taika *magic'; taikina *dough'; Li. (perh. by metath.?) žiedas (fring, thimble, blossom’. Semantics obscure). (W dull *form, shape? seems to represent a type *dhoighlio-)
3893:gargoros, ios “mass, pile, heap'. Cf. WP I, 590 Arm. karkar, Let ‘heap, pile’; Gk. gárgara, n. pl. id. cf. Hes. gargarés ‘tumult’: Li. cf. gargolas “lump, knot
4126:glombos, ios (1) “mass, lump, clump'. Cf. WP I, 616 & glembó Sw. klamp “lump, stump’; Fris. klampe “pile; swollen ankle’, beside Norw. klepp “lump, dough-ball’; ON kleppr “lump; plummet’; Cz. hloub, Slovak hlúb ‘cabbage-stump’; Pol. glab, id. (Isophonic: SGer. Klampfe, LG klampe 'clamp")
4241:gong- ‘hump, lump’. Cf. gong- and WP I, 535 Gk. (ambig.) gógge (an alleged form: = 'tap- root); Hes. góggon ‘fool’; R. (dim.) güzka ‘tump’; Blg. gáza ‘buttocks’; ON cf. kakka, v. ‘pile up’
4256:grabho “scratch, scrape'. Cf. grbh- Gk. (ambig.) grápho, id. and ‘write’; W cf. gra “nap, pile’; Sw. krabba “scratch, scrabble’. With s-extn. cf. Gk. grápso, fut.; ON OSw. krafsa ‘scrape, scratch, as fowls’. Cf. also Sw. kräfta ‘crab’. (Sw. karva, v. ‘notch’ is fr. *gorbh-
4341:grom- (1) ‘pile, mass, chattels’ Skt. gramah ‘pile’; G (uncertain vocalism) cf. Kram (“chattels?, but MHG kram “tent, shop, goods’ of uncertain origin); OCS cf. gromada ‘pile’, grominica ‘shop’
4354:grondhos, à (gronth-) ‘mass, tuft, bunch? Skt. cf. granthah, ih ‘knot’; Gk. grónthos ‘balled fist, punch’; Cor. gron ‘mass, bunch’; Br. cf. (?) grunn ‘mass, pile’; W (?) grwn, pl. grynau (fridge, baulk’, but cf. grondos, above); Latv. (ambiguous) grods ‘tightly twisted, knotted’
4404:grumbəlos ‘hump, grumbh- and gruməlos Alb. grúmbull ‘pile, heap’; Latv. grumbulis ‘Jump, knob, knoiP. (Isophonic: G fr. LG Krumpel, Krümpel ‘ruck, crease’: E crumple)
4440:gubos, à ‘pile; peak; top, head’. Cf. WP I, 562-7 MHG koph, kopf ‘poll, head, skull’; OE copp ‘summit’; EME cop ‘hillock, spindleful of yarn’; Du. kop ‘head, hilltop’; Sw. koppa (1) ‘crewcut head’ beside (*-ü- in) kūpa ‘hump’; Li. Latv. gubà, guba, f. ‘pile, stook’. (The Gmc. forms are ambig. ? *ĝub-)
4446:güd- (2) “lump, balP. Per güy, id. (fr. *güdio-); Arm. kujt, gs kuti, i-st. “pile, mass’; kut (2) ‘wealth’: MLG küte ‘bundle of flax’; Du. kuit ‘calf of leg’; G Kauz (2) ‘bun of hair, wisp of hair; Scots kyte ‘belly’; E dial. cf. bumble-kite ‘blackberry’; Icel. kútur ‘keg’; kút-magi ‘maw of fish’ Cf. Du. vis(ch)-kuit ‘roe’
4452:gūĝos, à, ios, iə (1) “lump, hump, knuckle- bone, knob’. Cf. WP I, 559 & gugos Arm. kuz ‘hump; bunch’; adj. ‘hunchbacked’ beside dim. type kcik, gs kckan “ball of thread’ (ambig. cf. kuĝ-); (OHG coccho, etc. ambig. cf. gugos); OCZ gyža ‘unripe grape’; Cz. hyZe, hyzdé ‘thigh’; Li. gūžis (2) ‘knuckle-bone’; gūžē “head of cabbage’ beside gùžulas ‘bun- dle, sheaf; Latv. gūza (2) ‘heap, pile’; gūža “hip, loin, meat-joint'. Variant in EME cockle- bone: Li. gùžulas
4478:gum- (gumos, à) “lump, mass’. See next Alb. gumé "rock: cf. gümull “pile, mass’; Latv. gums “lump”?
4480:gumbulos, gambəlos (gumbh-, gum-) ‘swel- ling’. WP I, 573. See gumb- and next. Oss. gumbul ‘ball of cheese’; Alb. gúmull ‘mass, pile’; OE cumbl, cumul ‘swelling’: ON
4534:ghabheolos, io, io- (ghabhul-) “hold, holder”. Cf. ghabh- (1) Gaul. gabalo- (LW in Lat. gabalus *gibbet"); Fr. cf. javelle (‘handful of corn; pile, heap’, fr. *gabella); MIr. cf. frith-gabál ‘bridle’; Ir.
5041:ghub- “peak, pile'. Variant of ghubh- (1), q. v. Oss. (ambig.) cf. gubank, Dig. gobat *mound, hillock’; MHG gupf, e wm., guphe, f. “peak, top, tip'; G Gupf, id.; cf. MHG goffe, guffe, f. ‘buttocks’; Li. (ambig.) gubà ‘shock of shea- ves?
5046:ghübhos, à (1) ‘hump, lump’. (Same as next? Cf. dholos for semantics) Oss. cf. gubank, gobat ‘mound’; Gk. küphos, n. (2) ‘hump, tumour’; OE guba ‘buttock, flank’; Norw. cf. gubbe old man’; Li. gubà, Latv. guba ‘pile, stook’; Cz. cf. o-heb, o-hyb ‘hump; bend’
5069:ghundhos (ghundholos), à “lump, ball, tu- mour, pile; balled, lumped’. WP I, 588. Va- riant: ghund-. Skt. cf. hundih, m.f. Jump, heap’; Av. gundo ‘round loaf; ear of corn’; gunda ‘round loaf; Per. gunde, adj. ‘thick, coarse’; Arm. gunt, gs gnto beside gund, gs gndi, abl. gndav ‘bali, mass”; Gk. cf. kolo-künthe (“pumpkin”, lit. “big ball); OHG cf. gunde-réba, f. (“ground-ivy” because used against goitre). Extns. in Per.
6117:9heu-, 8heumn-, £huuo, etc. Skt. havab ‘sacrifice’; Arm. cf. (e-gde) dzev, o-st. ‘shape’; Myc. -kowa (in a cpd. epithet of *oil); Gk. khóos, khoüs “liquid measure, dyke, mound’; khoé *outpour'; cf. also khóo, khónü- mi 'pile up'
6232:distinguishes relationship from content, as in Cz. krevní ‘relating to blood": Li. kraujinis, id., cf. the Ligurian river-name Beverin (in the Engadine), and the Sequanian aidrini “bright in the Coligny weather-diary, cf. Gk. aithrinós “of early morning’. The passage from adj. to noun is illustrated in Arm. grean, gs greno Cliterature': gir ^writing"); cf. also Per. pūst- in (ffurcoat? :püst (fur); Gk. eruthrinos Ca red fish": eruthrós); Alb. dulli, gs dullini (ju- niper, lit. ‘fragrant bush’, cf. dhülos (1) above); Lat. scrinium (^writing-case' in rela- tion to scribo); sterquilinium (tdungheap'": stercus); Ir. goirm-ín (*woad, indigo’: gorm “blue”); Li. gandrynas (‘swarm of storks’: gañ- dras); akmenynas, akmenjne (‘pile of stones? :akmuoó). For the fem. suffix cf. Alb. kopshtin- je (market garden’ : kopsht *garden"). An ad- jectival extn. of an adj. occurs in Skt. navinah (new': navah), and cf. Arm. mi£in (‘mid- most': me£). A dim. extn. arises in Ir. goib-ín (small mouth": gob) and in Go. gait-ein Cd": gaits); W dern-yn (‘small piece’: darn); Li. merg-inà ("little girl: mergà)
6420:ieumos, is, io (ium-) den, cave’. Cf. ioma, ieunis Ir. uaimh, f. ‘cave, cellar; kiln’; Latv. cf. jums ‘roof, shelter, vault, clamp’; Go. (?) jumjo “pile?
=== pilos
8400:kupəlos (kupilos) ‘bulge, swelling, mass, pile; bulging, luxuriant. WP I, 373 Hes. cf. kúpalon (queried: ‘allocation, lot); Gk. cf. küpellon ‘bulging cup’; OHG hubil, MHG hübel, hubel, m. ‘hil’; Du. cf. heuvel, m. (id. but phonology ambig.); Li. kuplùs, adj. ‘spreading, luxuriant’; Latv. kupls ‘dense, bushy’. See next
12822:popilos, is 'fleeting creature’. WP II, 107. Cf. pipl- (pipol-) Skt. pipiláh, m., -ih, f. rant: Hes. cf. pipalís, f. (-lizard', for (?) *papil-); Lat. cf. papilio, gs: -Onis, m. “butterfly, moth’; W cf. ilir, eilir & eilier, pl. -ion, m. id.; OPr. cf. pipalins, acc.
12888:pilos, à, iə “ball, globe’. See Supt:P Gk. pilos, m. *oakapple'; cf. mes-pilon, n. (*medlar,, lit. “honeyball , cf. medhu); Lat. pila, f. “ball”; Li. pylà & pile, f. id.
12937:pislos, om, à “hair, fibre' Per. pile ‘cocoon’; Gk. pilos, m. ‘hair, wool, felt; MHG cf. viseln, pl. ‘fibres’; G Fisel, m. ‘tatter’; fiseln, v. ‘fray’; Du. vesel, f. ‘fibre’; Latv. cf. pislis, pl. pīšļi (/speck, mote’; pl. *dust"). (Short -i= in Lat. pilus, m. ‘hair un- accountable)
16833:spiglos, ios (sph-) “point, spike, prickle’. Cf. spilos. Radical spig- Du. spikkel, m. ‘spot, stain’; Li. spyglys, gs: -io, m. ‘thorn’; Latv. spiguls, m. ‘firefly’: spigolis, id. (lit. *spark"). Radical in ON spik, pl. -r, f. ‘splinter, splint’; Sw. spik ‘nail’; E spike
16835:spilos, à, io “point, spike. prickle, pin". WP II, 654. Variant spil-. Cf. spiglos Gk. spílos, m. ‘spot, stain; reef crag’; cf. also spílás, gs: -ádos "rock: EMAIb. fill, m. “end, tip, point’; Br. spilen, s. ‘pin’; spíl, s. ‘icicle’; MHG ep, sm. ‘tip, spear’; MLG splile ‘spit’; G Speil, m. ‘chip’; Du. spijl, f. ‘spike, railing,
```


## [2026-09-14T00:54:28.340Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\n# find leaf index for given line numbers\ndef leafof(lineno):\n    pre='\\n'.join(lines[:lineno])\n    return pre.count('\\f')\nfor ln in (12888,12937,12822):\n    print(ln, 'leaf', leafof(ln))\nEOF",
 "description": "Find IEC leaf for pislos entry"
}
```


### [2026-09-14T00:54:29.534Z] TOOL RESULT

```
12888 leaf 520
12937 leaf 522
12822 leaf 517
```


## [2026-09-14T00:54:38.547Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\nL=t.split('\\f')\nfor i in (520,521,522):\n    print('==== leaf',i)\n    print(L[i][:1800])\nprint('==== last leaf 857'); print(L[857][:600])\nprint('==== leaf 840'); print(L[840][:600])\nEOF",
 "description": "Print IEC leaves 520-522 and tail"
}
```


### [2026-09-14T00:54:39.667Z] TOOL RESULT

```
==== leaf 520
nger’; pykstü, pýkti, v. ‘be angry; LW in Ir. pioc, pioch, m. ‘droplet; jot; pore & in Alb. pikë ‘point, dot, source of Fr. pique, fr. a Lat. type *picca. A type pīkāið arises in Alb. pikoj, v. ‘drip’; OCz. pikati, inf. ‘urinate’ and in OCS pikanina, pikotyna, f. “urine?
pikolos, à, is (pikl-) ‘tip, point. Cf. pik-, pikos, a and WP II, 17
pig- — piks-
20
25
30
35
40
45
936
Alb. pikél, f. ‘dot, point, snag’; Ligurian (in Rhaeto-Rum.) pical, m. ‘beak’; pikla, f. *finger- tip’; Li. cf. pikule, f. "hedge-mustard'
pikis, ios, io “pitch, raging fire’. Extn. piknis, os. WP II, 75 Gk. píssa, pitta, f. ‘pitch; hell; Lat. pix, gs: picis, f. “pitch” beside picula ‘scrap of pitch’; OHG.OS cf. fehon, v. ‘consume, destroy’; OCS cf. píklü, nol m. *pitch" beside piklinú, adj. infernal; Blg. cf. pákál, m. ‘pitch, hell; Srb. cf. paklina “tar, pitch’, pakao, m. "bell": Li. pikis, gs: io, m. ‘pitch’; Latv. pikis “pitch, hell. (DW in Alb. pis, m. ‘pitch’). For the extn. *piknos, cf. Lat. pinus, gs: -üs & <i, f. ‘pine’; Arm. cf. eye-vin, gs. -vno, o-st. id. (for eye- see elntà); OS cf. fini-star, n. ost & fini-stri, f. i-st. (*darkness'. Cf. ster-); MHG vin-ster, OS fini-stri, adj. “dark?
pikos "a bird’. WP II, 681 Skt. pikah, m. ‘cuckoo’; Alb. cf. (dim. type) pikth, m., piké, f. (^woodpecker. Sense in- fluenced by Lat. picus, pica, see poiKos, à). (Isophone: Latv. piks, m., pika, f. “lump, clot ; Alb. cf. pikset, 3s. *coagulates'")
pikos, à “point, prick, stab, sting'. Cf. piko- los EMAIb Alb. pikë, f. “point, dot: të pik&-t, n. ‘stab’; Lat. pica, f. ‘oestrus in pregnant women’; MIr. íoc, m. ‘suffering’; íocaim, v. ‘suffer; Slovene pik ‘sting — of insects; R pik, m. ( ‘peak’, geog.); Ukr. pyka, f. ‘snout. (Isophonic are It. picca ‘pike, spear’; picco, adj. and m. ‘stung; pungency; mountain 
==== leaf 521
fig" beside pippalih, f. ‘capsicum, chilli’; pippalah ‘sacred figtree; nipple; pippalam, n. ‘berry, (The variants occur in the river-name Pimpala & Pippalàa); Sp. cf. pimpóllo ‘shoot; beau’; Port. pimpáo, id. beside pimpolho ‘bud’ (LW in E pimple); G Fimmel, Femmel, m. “male hop, male hemp’; Li. cf. pirnpis, pimpelis, m. “penis. (Isophones: OE fifel ‘giant’; ON fimbul-, cpds. *mighty-)
pin- (pinák-) ‘wood, stick, board, log. WP II, 71 Skt. cf. pinakam ‘stick, cudgel; Gk. pinax, gs: -akos, m. “board, tablet, platter’; OCS (and com. S1.) pini, m. ‘trunk, log
pin- (2), see pino and cpds.
ping- (1) ‘mark, daub, stain’ Skt. pinkte, 3s. ‘dyes, paints’; Lat. (ambig.)
piktos — pipël-
10
15
20
25
30
35
40
45
938
pingo, ére, pf. pinxi, v. tr. ‘daub, paint, stain’; R cf. pjatnó (“blot, stain', if fr. *pingtino-); (non-nasal in) Cz. piha ('freckle', fr. *piga)
ping- (2) ‘chirp, squeak’ Skt. pinkte, 3s (2), id.; Hes. pígga-, f. ‘chick’; cf. Gk. sál-pigx, gs: -piggos, f. (trumpet'. See Kul-); MHG vinke, wm., OE finc, m. ‘finch’
pingolos ‘lizard’. WP II, 9 Skt. pingaláh, m. id.; adj. ‘tawny’; Hes. píg- galos, m. id.
pingol- Skt. piñjalah, adj. ‘chaotic; G finkeln, v. ‘botch, hash’; Sw. finkel, m. ‘hooch, illegal liquor
(pink-, variant of type ping- (?), but cf. pik-, peik-, poik-) Tokh. B pink-, v. (write, paint'. Lat. pingo is ambig. as also Norw. Dong, adj. "elegant
pinó (pein-, poin-, pin-) ‘twist, constrict. WP II, 661 Skt. cf. pinda, adv. “in a knot; OCS píng, peti, v. (^wind, twist, and com. S1.); Li. pinü, pinti; Latv. pinu, pit, id.; (o-gde in) Arm. hinem, henum, id.; Alb. cf. m-pij, v. Che: numb’, fr. *en-pinjo); sh-pij, v. (limber up’, fr. *eKs-pinijo). Long-grade in OCS pinajo, v. ‘stretch’; Li. one f. ‘wattle, weave, webbing, braid, plait; Latv. pine, id.
pino ‘drink, abso
==== leaf 522
, f. ‘chick’; pipizo, v. ‘cheep’; cf. oino-pipés, adj. ‘gasping for wine’; Lat. pipo, åre, v. ‘cheep’ beside ppo. ire, v. ^whim- per; Li. pypiü, pýpti, v. ‘cheep’. Doubtfully to W iâr, Br. jar, Cor. yar, f. Chen, qua *piporà)
pis- “mess; messy Per. pih ‘tallow’; LG fies, adj. ‘nasty’; Ukr. cf. po-psuty, v. ‘spoil beside zi-psuty, v. (“de- moralized', but associated with the Sl. type písü, m. (dog); Cz. piz-dit, inf. “mess up, spoil; Latv. pisa ‘morass’. (OHG fésa, MHG vése, wf. *chaff to pisiom, q.v.)
pisdó (piséd-, pisod-) “bear down on, trample'. Cf. pi- (epi), sed-. WP I 122 & II, 486. See next Skt. pidayami, v. ‘squeeze, press’; Gk. piézo, piazo, v. id. beside psiázo, v. (dance, fr. *Ks- pi-sodio); Ir. (?) iadhaim, v. ‘enclose, brace’; W (?) eddu, v. ‘press on, go: OCz. pezd, gs: pzda, m., pizda, f. 'arse
pisdom, à “posterior, seat, vulva’. Cf. pisdo.
pípét- — pislom, à
10
20
29
30
35
40
45
940
WP II, 69 Skt. pitham, n. ‘seat, base beside pida, (basket. Semantic relationship, if any, ob- scure; cf. however pida (2) 'garland" and Ir. iodh, gs: idhe f. ‘chain, ring, collar, if fr. *pisd- ‘twist, constrain’, cf. Ir. iodha, f. *pang"); Alb. pith & pidh, m. ‘vulva’; OCz. pezd, gs: pzda, m. beside pizda, f. (arse; vulva’; Big. pizda, f. ‘vulva’; Li. pyzdà, Latv. pizda, d: OPr. peisda (-ei- for ZA. f. id.
pisimnos, à ‘ground, pounded, small. Cf. pisio, pistos, etc. Skt. Av. pi&-, v. root ‘grind’; Gk. cf. ptisáne, f. (“pearl barley, barley-gruel, fr. *d-pision-); LLat. pisinnus, adj. ‘tiny’; G Fesen, Vesen, m. ‘spelt; grain-husk'; R pšenò, n. ‘millet; Slo- vene ‘groats’; OPr. cf. som-pisinis (‘coarse bread": Skt. sam-piš-); Skt. cf. pista-pesanah, m. ‘flour, meal
pisið (pins-) ‘crush, pound’. WP II, 1. Cf. pisimnos, pistos Skt. pinsami, pp: pistah, v. id.; Av. piš-, id.; Gk
==== last leaf 857
(1) only in Skt. ürnómi, v. ‘envelop’; (2) only in Gmc. cf. Go. wulan and OE wylian 'seethe? beside wyllan, v. id. (fr. *ulnio)
ulquátis, os *tearer, devourer, killer’. Cf. ul- quos (1) Skt. vrkátih, m. ‘robber, murderer’; Slovene volkác ‘Alsatian dog’; Li. vilkátas, m. *wer- wolf; Late vilkatis, vilkacs, id.
ulquio ‘she-wolf’. Cf. ulquos (1) Skt. vrkih, id.; OE welt id. MHG (Upper Ger) wülpe, id.; ON ylgr, ds: ylgi, id.; Li. vilke, id.
ulquó, ið (ambiguous consonantism, unless related to type ulquos, etc. see next). Skt. varke, mp. ((seize', but cf. type *uelk-) beside vrkah (2) '(plough'; Sr
==== leaf 840
, wasami, wasiyami, wasemi, v. ‘put on — clothes’; Gk. Ion. heimai, 2s: héssai, 3s: héstai, v. ‘wear’ beside Gk. hénnüm,i, fut: héso, tr. ‘put on — a garment’; cf. esthés, gs: -étos, f. ‘garment’; Alb. vesh, v. ‘put on — clothes’; véshem & víshem, v. ‘get dressed; Lat. cf. vestis, f. ‘garment’; Go. cf. (o-gde) wasjan, tr. “put on — clothes’; OE werian, v. (id. E *wear). Variant of type *ués-sK- in Arm. z-gec-nem, tr. ‘dress’; Br. gwiska, tr. id.; W gwisgo, id.; cf. Br. gwisk, pl. -u, m. ‘dress’; W gwisg, pl. -oedd, f. id.
ues- (5) ‘soak; water’. Cf. uosolos, uðsos Skt. cf. vasin, m. ‘otter’; T
```


## [2026-09-14T00:54:48.534Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"pisl\\|pîle\\|pile ‘\\|pile '\" IEC.txt | head -20; echo \"=== supplement start\"; grep -n \"SUPPLEMENT\\|Supplement\" IEC.txt | head -10",
 "description": "grep IEC pisl and supplement"
}
```


### [2026-09-14T00:54:48.597Z] TOOL RESULT

```
1114:bhalið ‘hit, hurt. (Cf. bal-, suppt.) WP II, 189. ON bella, pt. ball, id.; Tokh. (ambig.) päl, B pile ‘wound’; OCS boljo, bolëti (ambig.) “hurt?
12596:peil- "a tool, file, scraper, knife'(?) OHG fila, f., MHG vile, sf., OE feol, f. (fle and com. Gmc.); OCS pila, f. ‘saw’; Cz. pila, id. beside pilnik, m. ‘file’; Srb. pila ‘saw, file’; Li. peilis, gs. 20. m. ‘knife’; Latv. peilis, id.; cf. Li. pielà ‘saw’. (Lat. pila ‘pestle’ is prob. fr. *pisla or *pisdhla, see pis-, pistos, etc.)
12910:pins-, form of type pis-, see pisio “crush, grind, pound’. WP II, 9 Skt. cf. pina$mi (sic!), 3s: pinasti, id.; cf. pisi- lam (sic: *platter); pistib, f. ‘flour, powder; Lat. pinso, ére, v. *pound, knead; peck; scoff, berate’; Lat. cf. also pilum ‘pestle’; pila *mor- tar; sup-pilo, åre, v. (pilfer. Romance type *piliàre ‘take, remove, pillage’); Latv. cf. pīšļi, mpl. ‘dust, ash’; pislitis, dim. ‘speck?
12923:pípét- — pislom, à
12937:pislos, om, à “hair, fibre' Per. pile ‘cocoon’; Gk. pilos, m. ‘hair, wool, felt; MHG cf. viseln, pl. ‘fibres’; G Fisel, m. ‘tatter’; fiseln, v. ‘fray’; Du. vesel, f. ‘fibre’; Latv. cf. pislis, pl. pīšļi (/speck, mote’; pl. *dust"). (Short -i= in Lat. pilus, m. ‘hair un- accountable)
12938:pislom, à ‘pestle, crusher’. Cf. pisio, pistos, pisimnos Lat. pilum, n. ‘pestle’; cf. pila, f. ‘mortar’;
16844:rod'; E spile ‘peg, spigot, pile of timber, stack’; Norw. spile, s. ‘lath, stay’; Cz. spile, f. ‘spit, skewer’; Pol. $pila, f. id.; Big. spila, f. ‘rock, cliff; Li. spylys, gs: -io, m. ‘spit, prick- le’; spylà, f. ‘reed, split twig’; Latv. spile, f. ‘clamp, claw, grapple, mandible, cleft stick’. Short-grade in Gk. spilás ‘rock’; Ir. spealán, m. (chip, shaving’, fr. *sphilon); OE spilu, s. ‘tip, point, pencil’; Du. Fris. spil, f. ‘spindle’; E spill ‘taper of wood’
=== supplement start
23:11. 1987. 1573-1684 (uolobhis-uupsios + Supplement + Corrigenda)
127:VAN Wu. N.: Etymologisch Wb. der nederlandse Taal, 1912. With Supplement by C. B. van Haeringen, 1936. Reprint Staatsdrukkerij- en Uitgeverijbedrijf, den Haag 1949
```


## [2026-09-14T00:54:55.091Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\nL=t.split('\\f')\nimport re\n# find supplement: look for leaves containing 16xx page numbers\nfor i in range(len(L)-60,len(L)):\n    m=re.findall(r'\\b16[0-9]{2}\\b',L[i])\n    head=re.findall(r'\\n([a-zA-ZÀ-ɏ\\-]+ — [a-zA-ZÀ-ɏ\\-]+)\\n',L[i])\n    if m or head:\n        print(i, m[:4], head[:3])\nEOF",
 "description": "Locate IEC supplement leaves"
}
```


### [2026-09-14T00:54:56.083Z] TOOL RESULT

```
799 [] ['tük- — tūl-']
802 ['1648'] []
806 [] ['tue- — tuérios']
808 [] ['tuis- — tuonk-']
809 [] ['tuor- — turtos']
817 [] ['uaio — ual-']
818 [] ['uàl- — uàn-']
829 [] ['uek- — uel-']
832 [] ['uelk- — uén-']
838 [] ['uerpo — uertos']
840 [] ['ues- — uesoar-']
849 [] ['uiK- — uin-']
851 [] ['uis — uisg-']
855 [] ['ulon- — ulg-']
```


## [2026-09-14T00:55:12.665Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\nL=t.split('\\f')\nfor i in (801,802,803):\n    print('==== leaf',i); print(L[i][:1200])\nEOF",
 "description": "IEC leaves 801-803"
}
```


### [2026-09-14T00:55:13.862Z] TOOL RESULT

```
==== leaf 801
; Vedic: ‘big, strong’; Oss. tímbil, Dig. tumbul, adj. ‘found’; Alb. cf. tumull-ac, adj. ‘chubby’; m. “bladder, balloon’; Lat. tumulus, gs: -i, m. ‘hillock’ beside tumultum, n. ‘tumult’; Ir. cf. tomhal- tach, adj. ‘gluttonous’; tomhlaim, v. ‘guzzle’; OE pumle, pl. ‘entrails’ beside (*-ü-) bymel, m. 'thumb-stall, thimble’; ON pumall, m. ‘thumb’; Cz. tmel, m. ‘putty’; Slovak cf. tmo- lit sa, inf. ‘tumble, frolic’; Li. tümulas, m. ‘Jump, mass, pother'. See next
tumo, eio ‘swell’. Cf. tumos, tumolos. WP I, 708 Skt. cf. túmrah ‘swollen’; Per. cf. tuman *my- riad’; Tokh. A tmān, B tumane & tmane, wd: Lat. tumeo, ere, v. ‘swell, increase; W tyfu, inf. ‘grow’; twf, m. ‘growth’; Cor. tevy, inf. ‘grow’; Li. tumü, eti, v. ‘congeal’; tumus, adj. ‘clotted’; tumà, f. ‘mass; cloudiness’; Latv. tumu & tumëju, et, v. ‘thicken, clot’
tumos, à, ön), io ‘swell, lump, mass, myriad, crowd’. Cf. tuməlos, tumo. WP I, 708 Skt. cf. túmrah ‘swollen’; Per. tuman, s. ‘my- riad’; Tokh. A tman, B tmāne & tumane, id.; Ir. tom, m. ‘bush, knoll, lump’; W twf, m. ‘growth’; Cor. towan, pl. tewennow, m. ‘dune, hillock’; (*-ü- in) OE püma, wm. ‘thumb’; MHG dūme & (late) doume, wm. id.; Ukr. cf. tíma (for *tüma? *abunda
==== leaf 802
ny, adj. ‘sly’; tutela, po-tutela, mf. 'sly- boots'; Latv. (fr. a form of Li. type) tuntulet, inf. “wrap up, mummify'; tuntulis, s. “lump, knot; botcher'. (Not in Li.!)
tuntoló (tuntuló, tuntlo) (2) ‘rumble, babble’. (Gk. Aib. type: tuntulaio) Gk. tuntlázo, v. ‘babble’; Alb. tunduliloj, v. ‘shake, rattle, dash’. Nominal types: Per. am- big. tundar ‘thunder’. Cf. Gk. túntlos, m. ‘twaddle’
tuntind (1) “bang, echo, resound'. Cf. tunto- lo (2) Lat. (assimilated vowels) tintino, tintinno, are & tintinnio, ire, v. ‘ring, resound’; OE cf. bundian, v. ‘flog; OCS totinajo, ati, v. ‘resound’; Pol. tetnic, v. (“beat — drum; intr. *rumble, roar’); Blg. tántja, v. “boom, hum, drone’; táten, s. ‘din’; Li. cf. pa-tuntas, m. “blow, stroke’
tuntinó (-6i0) (2) “rock, sway, reel, wander”. (Arm. type *-àio) Arm. tntnam, v. ‘dandle, rock’; Li. tuntineju, eti, v. ‘mooch round’; Rum. (substrate?) cf. tont, adj. “silly”
tup- see tupo (1) and (2)
tüpolos (tüpulos) ‘bulge; dolt'. Per. ambig. cf. tübhor- Skt. tüparáb, adj. ‘hornless; m. ‘hornless goat’; Oss. tuppur, adj. ‘bulging’; s. ‘bulge, hump’; Per. tübre, s. Chag LW in Tk. torba, id.); Latv. tüplis, s. *arse'; Slovene cf. tepec, m. (“blockhead”, fr. *t
==== leaf 803
ty, violent; torrential’, vocal- ism zero-gde to a type *tuers-); Ir. (variant) turraic, f. (thrust; rush’, fr. *turs-); ON byrja, v. ‘sweep, rush’; OCz. and Cz. tyrati, v. “per- secute'; Blg. tirja, v. (chase away’. Nominal type in Skt. turáh ‘dashing’
tur- (2) “check, hold, have’. Cf. tuer- (2) Hitt. türi(mi), turiyami, v. harness"; It. turare, v. “block, stop’; Lat. cf. re-türo, are, v. “un- block, unstop'; ob-türo, are, v. “block, stop’; cf. tarunda, f. ‘cramming food for fowls’; Li. turiü, éti, v. “have, hold'; Latv. turu, ét, id. Skt. turáh (3) ‘strong’; Av. türo, m. ‘enemy’; Tuiryo, adj. ‘Turanian’; (Iran. LW in) Gk. tú- rannos ‘tyrant’; Li. tūris, gs: -io, m. 'capa- city’; Latv. tura, f. “hold, stand, attitude’; pl. ‘scaffolding’
tur- (3) (?), see turs- (4)
tūr- “aged, old, crumbly, brittle, decrepit, matured” Av. (alleged) tūris, tūiris, s. ‘whey’; Myc. A Gk. türós, m. ‘cheese’; Mir. túr, adj. ‘fallow’; Cz. cf. tyfet, inf. ‘crumble, age’. (Isophones: Olr. túr ‘search’; Li. türai, mpl. 'sidewhis- kers’; uncertainly Sw. ture, wm. ‘boon com- panion, wag’)
turbā (trubā, trb-) ‘throng, mass, communi- ty’; turbio, -àio ‘throng, riot. WP I, 750 Hitt. (ambig.) taruppai(mi), v. ‘th
```


## [2026-09-14T00:55:27.261Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\nL=t.split('\\f')\nfor i in range(845,858):\n    nums=re.findall(r'\\b1[0-9]{3}\\b',L[i])\n    print(i,nums[:6], L[i][:60].replace('\\n',' '))\nEOF",
 "description": "page numbers at IEC end"
}
```


### [2026-09-14T00:55:28.385Z] TOOL RESULT

```
845 ['1535']  v. “become visible’. Cf. type *uidoi! in Gk. idoú! ‘behold’
846 ['1536', '1537'] ow in middie of elephants forehead’; Li. vidüs, m. ‘middle; 
847 ['1538', '1539'] ��: Latv. videnis *torso, rump' and Li. Latv. vidus, m. *mid
848 ['1540', '1541'] f. *filigree-gold'; MHG wiere, f. id.; OE wir, m. ‘wire; fil
849 ['1542']  cf. am- usin, s. (spouse, fr. *som-uiKin-, cf. Lat. uxor, i
850 ['1543', '1544'] WP I, 259 & 577 Gk. mus, s: -ios, mf. ‘son, daughter’; Lat. 
851 ['1545', '1546'] “man, husband, hero’. WP I, 314 Skt. viráh “man, hero’; Av. 
852 ['1547', '1548'] rul-entus ‘poisonous’. Cf. OE wode-wistle ‘hemlock’. (Isopho
853 ['1549', '1550'] - sure, acceptance'. Cf. uoit- (2) Skt. vitáh, adj. (2) id.;
854 ['1551'] Skt. vívakmi, v. ‘say, speak, tell beside vávak- mi, id.; (H
855 ['1552', '1553'] Lat. liquor, gs: -óris, m. ‘fluid’; MIr. & Ir. fliuch *wet';
856 ['1554'] bulga is ambig. Skt. várgā ‘sect, class’ seems to be unrelat
857 [] (1) only in Skt. ürnómi, v. ‘envelop’; (2) only in Gmc. cf.
```


## [2026-09-14T00:55:58.495Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN 1966 pepper\"; grep -n \"pepper, n\\.\\|^pepper\" KLN_1966.txt | head -5; echo \"=== KLN1971 pepper\"; grep -n \"pepper,\" KLN_1971.txt | head -5",
 "description": "grep Klein for pepper"
}
```


### [2026-09-14T00:55:58.569Z] TOOL RESULT

```
=== KLN 1966 pepper
28054:pepper,  n.  —  ME.  peper ,  piper ,  fr.  OE.  pipor,  tr. L.  piper,  ‘pepper’,  fr.  Gk.  nenspi,  ult.,  through Persian  mediation,  fr.  OI.  pippalf,  ‘berry,  pep¬ percorn’,  which  is  of  imitative  origin.  OFris. piper,  Du. peper,  OHG.  pfeffar  (whence  MHG., G.  pfeffer).  It.  pepe,  OProven?.,Catal.,Sp.  pehre, F.  poivre,  OSlav.  piprit,  Lith.  pipiras,  OIr.  pio- bhar,  W.  pybyr,  pubyr,  ‘pepper’,  are  all  borrowed fr.  L.  piper.  See  papula  and  cp.  paprika,  pebrine, pimpernel,  Piperaceae,  piperine,  poivrade.  Cp. also  pilpul,  pipal.
28056:peppermint,  n.  - —  Compounded  ot  pepper  and mint,  ‘aromatic  plant’.
28896:pepper.
29362:pepper  ane  -ade.
=== KLN1971 pepper
40797:castor, n. (of pepper, etc.) — Fr. earlier caster. 
177758:rogr.) — It., fr. pepere, ‘pepper,’, fr. L. piper em, 
177780:pepper, n. — ME. peper , piper, fr. OE. pipor, fr. 
183074:piper, ‘pepper’. See pepper,
```


## [2026-09-14T00:56:00.113Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SYN leaf 369 (p345)\"; python3 - <<'EOF'\nt=open('SYN.txt',encoding='utf-8',errors='replace').read()\nL=t.split('\\f')\nprint(len(L))\nfor i in (368,369,370):\n    print('--- leaf',i); print(L[i][:1200])\nEOF",
 "description": "Buck SYN page 345"
}
```


### [2026-09-14T00:56:01.240Z] TOOL RESULT

```
=== SYN leaf 369 (p345)
1545
--- leaf 368
nt,
tt. nekumane Da! : a nekus ‘evening’ Hitt. Gram. 122 f.). : 9, NG -youuv6s, . ues by associa- ‘ +4} x dpyw ‘Undress . an cat gol, fr. Slavic (below, 7). 4, Ir. lomm, NIv. lom (also frequently epd. lomnocht with nocht, above, 1), W. Tom ‘bare’ : Olr. lommar ‘callow, bare’, Mir. lommraim ‘strip, peel’, prob. fr. the root *leu-bh- in Russ. lub ‘bast’, Lith. lwobas ‘tree bark’, etc., beside
Digitized by Arya Samaj Foundation Chennai and eGangotri
BODY; BODILY FUNCTIONS AND CONDITIONS 325
*leu-p in Skt. lup- ‘break, injure, plun- der’, Lith. lupti ‘peel’. Walde-P. 2.418.
5. ON berr, Dan., Sw. bar, OF ber, ME, NE bare, OHG, MHG bar (NHG bar in old sense in cpds. barfuss, barhaupt and readopted in the modern lit. lan- guage) : Lith. basas, Lett. bass, ChSl. bosti ‘barefoot’, with guttural suffix Arm. bok id. Walde-P. 2.189.
Du. bloot, MHG bléz, NHG bloss (OHG bloz ‘proud’, fr. ‘empty, vain’?) : OE bléat ‘miserable’, ON blautr ‘soft’, also OE bléap, ON blaudr ‘timid’, prob. from extensions of *bhlau- seen in Grk. grdatpes ‘petty, trivial’, Walde-P. 2.208. Falk-Torp 85 f.
6. Lett. pliks and kails, both also ‘bald’ (4.93).
7. ChSl. gol, SCr. go, Boh. holy, Pol. goli, Russ. golyj : OE cal
--- leaf 369
eed on’ as homely words use The’ gabsti- (perh. : Lat. tergére ‘rub off’, terere ‘rub’,
ing’ oF yulgarly of men. : sul tutes are partly words meaning original-
ly ‘chew, nibble, swallow’, etc., which were used of animals ‘feeding ‘ and also gs colloquial or slang expressions with reference to men (cf. NE where’ll we feed?), until they finally became the standard words for ‘eat’. Others are derivatives of nouns meaning ‘food, meal’ (these of various sources discussed under ‘food’, etc.), that is, ‘take food, a meal’; or again from the notion of ‘par- take of’, with specialization to ‘partake of food’, as frequently in NE. 1. IE *ed-. Walde-P. 1.118. nout-M, 294f. Walde-H. 1.392 f. Grk. éw (poet.), Att. éciw; Lat. ésse, late edere, Ose. edum; Ir. subj. estar, Oe * Pass. eisse, etc. (supplying parts of Grae ef. Pedersen 2.559; Thurneysen, ae 471), W. ysu ‘devour’; Goth. titan, : as Gme.; Lith. ésti, Lett. ast, Br a aa jasti, ete., general Slavic; wie (re eulem; Hitt. ef-. But Dan. ith, as for ‘eat? in Dan. Bible) and ae are now used only of animals Barly of men). Falk- NSB gy. alk-Torp 1411.
Cf, feat enw Goth. fra~itan (for xarecOls zon ‘de, se ), OE fretan, OHG free- » Whence NHG fre
--- leaf 370
l. pitéti ‘feed’, etc. (5.12). Pedersen 2.559.
W. bwyita, fr. bwyd ‘food’ (5.12).
Br. dibri, MBr. dibriff, OBr. sb. diprim ‘food’, Corn. dibry., prob. fr. a cpd. *di-prim-: NIr. creimim ‘gnaw, chew’ (Ir. vbl. n. creim, K. Meyer, Contrib. 511). Henry 95. Loth, Vocab. vieux-breton 105. (Otherwise, but to be rejected, Pedersen 1.111).
5. Goth. matjan (more common than titan), fr. mats ‘food’ (5.12).
Dan. spise, fr. sb. spise, loanword fr. MLG spise ‘food’ (5.12). As the polite term this has displaced the old ede (above, 1), as NHG speisen has en- croached on essen, but without displac- ing it (Kretschmer, Wortgeogr. 469).
6. Lith. valgyti (displacing és¢; 1), fr. valgis ‘food, meal’ (5.12),
7. Russ. kugat’, polite term ‘partake of’ food or drink : ChSl. = kuszij ‘taste? etc. (15.31). :
8. Skt. ag- ‘eat, devour’, et: ; Walde-P. 1.112, pe!
Skt. bhuj- ‘enjoy’, esp. ‘enjoy food eat’, prob. : Lat. fungi ‘be engaged in, perform’. Walde-H. 1.566 (with Tefs.)
Skt. ghas-, Av. gah- ‘eat, devour’ (Av. only of evil beings), etym.? Walde- P. 1.640. Barth. 517.
Skt. khad- ‘chew’, colloq. for ‘eat’ and in MIndic mostly displacing ad-. Wack- ernagel-Debrunner, KZ 67.158.
Av. x"ar- ‘consume, eat or dr
```


## [2026-09-14T00:56:13.755Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"wivag\\|pinax\\|mivaé\\|zivaé\\|pinak\" SYN.txt | head -20; echo \"=== find p345\"; python3 - <<'EOF'\nt=open('SYN.txt',encoding='utf-8',errors='replace').read()\nL=t.split('\\f')\nimport re\nfor i,leaf in enumerate(L):\n    if re.search(r'\\b34[45]\\b', leaf) and ('DISH' in leaf.upper() or 'FOOD' in leaf.upper() or 'VESSEL' in leaf.upper()):\n        print(i, leaf[:200].replace('\\n',' '))\nEOF",
 "description": "grep Buck for pinax and page 345"
}
```


### [2026-09-14T00:56:15.120Z] TOOL RESULT

```
8735:1, Grk. mivat ‘board, plank, tablet’ and ‘platter’ : Skt. pinaka- ‘staff’, ChSI. pint, Russ. pen’, ete. ‘tree-trunk’ or ‘stump’, Walde-P, 2.71.
=== find p345
386 la, eran ME panne Pol.  panew, patelnia i aloe peers NE pan Russ. skovoroda ee iftt Du. pan Skt.  kataha- bhrasta- Ri figaie, tingire, crala{ Ti igen OHG pfanna Av. wae Nk. oighean MHG pfanne W. — pad
388 Gme., Goth. biups ‘table’, etc., orig. ‘servine- tray’ (7.44) Berneker 64. Stender Petersen 404. ; SCr. zdjela, fr. *sdjeti, ChSl. sii-délt ‘put together, make’. CC-0. In Public Domain. Gurukul Kangri
808 aAas, and so reg. 0 NT and pap.). 2. Lat. prehendere, préndere (> Rum. prinde ‘seize, effect, begin’, etc.; It. prendere, Fr. prendre ‘take’) fr. praé CC-0. In Public Domain. Gurukul Kangri Collection
1194 Hnown in IE times. It Debably rea ndia, pad a Slavic group der, Reale ects the ‘lick’ kiss. Schra- Snifr. oe x S.v, Kuss. Hopkins, The B19 an Ancient India, JAOS Orient, Ber, Pal Der Kuss im alten 8s.
```


## [2026-09-14T00:56:19.990Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SYN.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\npre='\\n'.join(lines[:8735]); leaf=pre.count('\\f')\nprint('leaf',leaf)\nL=t.split('\\f')\nprint(L[leaf][:1500])\nEOF",
 "description": "Buck leaf containing pinax"
}
```


### [2026-09-14T00:56:21.602Z] TOOL RESULT

```
leaf 388
Gme., Goth. biups ‘table’, etc., orig. ‘servine- tray’ (7.44) Berneker 64. Stender Petersen 404. ;
SCr. zdjela, fr. *sdjeti, ChSl. sii-délt ‘put together, make’.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
fooD AND DRI
NK; COOKING AND UTENSILS
Digitized by Arya Samaj Foundation Chennai and eGangotri
345
even when ‘cup’, fr. Skt. pa- ‘protect,
-tna- used for various ; te. ay Id
p, bhajar take of? (cf. bhaks- guard’, hence orig. ‘container’. Walde- hes, £2. Blade een coat, etc.)- P, 2.71, 72. os ‘fe 1, Grk. EF icin howl) plate’ Skt. cardva- ‘shallow dish’, also ‘cover’ at palra- used a teup’ it may be = | : carman- ‘shelter’, etc., fr. IE *kel- snany reoeptacle- IE *pa(i)-, Skt. pa ‘cover’ in Ir. celim, OE helan, Lat. oc- Jat. paculum, a der use, and so perh. | culere ‘hide’, ete. Walde-P. 1.432. : t in igrink’, bu
5.32 PLATE Goth. més : Lith.  leék&té, torélius, tori-
Grk. alvak ON diskr, skutill elka NG dro 11a) Dan.  tallerken Lett. telek’is, Sk'ivis at. (lanz, soule Sw. tallrik ChSl. misa, bljudo It. — pialto lat OE disc SCr.  tanjir ca ie ME ie plate poh. ae p . NE plate ol. erz a fuer Mae Du. bord Russ. tarelka See OHG disc Nir. a MHG._ iallar, teller ‘e nried NHG teller
The ancestor of the modern individual plate is the serving ‘platter’, originally a piece of flat board. The words listed here from earlier periods mean ‘platter’ and in part other forms of dishes. Sev- eral of them have been discussed under ‘dish’,
1, Grk. mivat ‘board, plank, tablet’ and
```


## [2026-09-14T00:56:27.354Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nleaf='\\n'.join(lines[:28054]).count('\\f')\nL=t.split('\\f')\nprint('leaf',leaf,'total',len(L))\nseg=L[leaf]\nprint(re.findall(r'\\b1[0-9]{3}\\b',seg)[:10])\nprint(seg[:300])\nEOF",
 "description": "Klein leaf/page for pepper"
}
```


### [2026-09-14T00:56:28.671Z] TOOL RESULT

```
leaf 616 total 903
['1571', '1630', '1154', '1155', '1810', '1835', '1849']
dj.,  having  five  metrical  feet  (pros.)
—  See  prec.  word.
pentane,  n.,  any  of  three  hydrocarbons  (C5Hlt)  of the  methane  series  ( chem .)  —  Formed  fr.  pent- with  suff.  -ane;  so  called  because  its  molecule contains  five  carbon  atoms.
pentarchy,  n.,  a  government  by  f
```


## [2026-09-14T00:56:34.730Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && ls -la; wc -c BQT_v3_pages.txt 2>/dev/null; head -c 400 BQT_v3_pages.txt 2>/dev/null",
 "description": "check BQT v3 OCR"
}
```


### [2026-09-14T00:56:34.779Z] TOOL RESULT

```
total 28692
drwxrwxr-x  4 sfmqrb sfmqrb     4096 Sep  4 14:06 .
drwxrwxr-x 23 sfmqrb sfmqrb     4096 Sep  4 14:06 ..
-rw-rw-r--  1 sfmqrb sfmqrb     8390 Sep  4 14:06 BQT_v3_pagemap.json
-rw-rw-r--  1 sfmqrb sfmqrb  2499427 Sep  4 14:06 BQT_v3_pages.txt
-rw-rw-r--  1 sfmqrb sfmqrb 11053965 Sep  4 14:06 BQT_v3_picofile.pdf
-rw-rw-r--  1 sfmqrb sfmqrb  2055176 Sep  4 14:06 BQT_v4_pages.txt
drwxrwxr-x  2 sfmqrb sfmqrb    20480 Sep  4 12:59 BQT_v4_pages.txt.pages
-rw-rw-r--  1 sfmqrb sfmqrb  8501918 Sep  4 14:06 BQT_v4_picofile.pdf
-rw-rw-r--  1 sfmqrb sfmqrb   723928 Sep  4 14:06 BQT_v5_pages.txt
drwxrwxr-x  2 sfmqrb sfmqrb    12288 Sep  4 13:14 BQT_v5_pages.txt.pages
-rw-rw-r--  1 sfmqrb sfmqrb  4472561 Sep  4 14:06 BQT_v5_picofile.pdf
2499427 BQT_v3_pages.txt
[pdf page 1]
[NOT OCRED - use tools/ref_page.py]
[pdf page 2]
7
Ub
sits k ge
AS ۱۰۶۲ ‏نتف‌بال‎
‏ومع‎ ‘oo ‏داي و‎ el Oe

far
en rotons ‘ ‘ ths ۰ ‏دیهان‎
‎۳ 2 7
۰ SF Ps
On Awe
۰
‏-ل‎ 9 ‘il
۱۳۴۳ ‏چاپ دوم فروردین‎
‏با تجدید نظر کامل‎
‏بسرمایه کتاپفروشی ابن سینا- تهران‎

|
```


## [2026-09-14T00:56:35.448Z] TOOL CALL #27: Bash

```json
{
 "command": "sed -n 1,60p tools/ref_page.py",
 "description": "read ref_page.py header"
}
```


### [2026-09-14T00:56:35.505Z] TOOL RESULT

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


## [2026-09-14T00:56:38.166Z] TOOL CALL #28: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:1502 --image 2>&1 | head -60",
 "description": "Fetch BQT p.1502"
}
```


### [2026-09-14T00:56:45.115Z] TOOL RESULT

```
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1502.png
REF: BQT:1502  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 295  OCR-lang: fas

شا ار را
«به خایه را گوبند و بریی مفتوق خواشد ۱ - | اس ت که مرد ذکر بزرگه باشد ‏
و بمعتی زشت و قبیح نیز آمده است - و جنم فنجگشت ۱ - بر وزن و معتّی
اول نلم شهری است ازولایت زنگیار - ودبه‌خایه | پنجنگشت است , و آن رستنیی باشد که بعربی
را لیز کفته‌اند ۴ (۱)* و بختح اول وثانی‌ماربرا | نوخمة (؟) اسابع و نوخمة(؟) اوراق‌خوانند.
کویند که زار یکی ترسالد . قنجنوش ۴ - با نون‌بروزن‌زر دکوش,
فنجا « بفتح اول‌بروزن تنها بحالنی‌است رم‌آهن مصنوعی باشد وبعر بی‌خبت|الحدید کوبند
که آدمیرا در وقت درآمدن تب واقع شودوآن و ساختن آن چنان اس ت که بگیرند ریم‌آهن را
خمیلزه ‏ وکش‌وا کش وکمان کشی بدن‌باشدوبهریی | و سحق نمایند و در شراب انگوری بخیانند تا
قشمرنره وتمطی خوانند ۴ - وبرف را نی زگوبند چهپارده روز » بعد از آن خعك کرده باز بایند
و آن چبزیت که در ایام زمستان از آسمان | وبا روغن باداخ بربان کنند . باه را زبادهکند .
بمانند پنیه‌ای که حلاجی میکردٍ باند ۳ فنجیدن ۸ بروزن راجدن » بمعتی
- وبکس اول بممنی دمه‌باشد. ون پادی‌است خمیازه و خود راکشیدن باشد پیش ازآنکه تب
در وقت باربدن برف بهم میرسد.** بهم رسد و آنرا بعریی قشعریره و تمط ی کویند
فنجر ۴ ه‌ بروزن‌سنجر,شخصیر| گویند ودر حالت خمار شراب‌وخمار خواب نیز این‌حالت
که‌آلت مردی او بز رکه وکنده باشد . بهم میرسد .
فنجره ۰ - بروزن جندره, بمعنی‌فنجر فند - بفتح اول وسکون ثانی ودال‌ایجد»
(۱) چك. چش : گویند - () چك » چش : نوخمه .
‎٩‏ سفنك « لغت فری ۷۱: عجبآبدمرا زت و که همی
چون کشی آن کلان دواخایهٌ فنج .
منجيك ترمذی « لغت فرس ۹۹ *.
۴ - همکرر است . در لغت فرس ( ید و۷۱ ) هم دوبار بدوعبارت آ مده ۰
۳ - رك : فنجیدن . ای - فنجه (م.) ۰ ۵ <خفنجی (ه.م.).
‎٩‏ فجنکشت > فنجکشت « عقار ۳۰۸ معرب « پنجنگشت > ۳ « پنج انگشت »
(هم.) ورك : دزی ح؟اص ۲۸۳ :۲ ؛ عقار ۳۰۸ ف - ۷ - « فنجنوش . بنون بمداز جیم»
اسم اسطلاحی ممجون خبت‌الحدید است » و عوام پادزهر کاوی را باین اسم مینامند . » « تحفةٌ
حکیم موْمن >. ۸ از : فنج ( رك : فنجا )+ایدن ( پوند مصدری ).
5 فنجان - (بکراول) < پنگان (۸.م.) از بونانی0181 ۰ کردی 17020:1080
و ۵8[8۵ « ژابا ۲۹۵ » کیلکی 118188 ؛ پیاله ( چای‌خوری » قهوه‌خوری) » پنگان -
بقیه حاشيهٌ صفحهٌ ۱۶۹۱
رشیدی کوید : « قلیو وقلیوه بقاف است نه بفا > ورك : فلاد ؛ فلاده - ۴ - ر4: فلیو .
ه_ (ص) «فناه » عنب‌الئملل است» « تحفهٌ حکم مومن > ور : عقار ۲۹۷ .مایرهوق
«فناء > را عربی ولغة بمعنی لستی دانته «عقار۲۹۷ ف >.
‎-۹٩‏ باز تو بی رنج باش وجان توخرم با نی و با رود و يا نبیذ فتا روز .
رود کی سمرقندی « لخت‌فرس ۰۱۸۷
```


## [2026-09-14T00:56:54.279Z] TOOL CALL #29: Bash

```json
{
 "command": "timeout 600 python3 /home/sfmqrb/git/rishe/tools/ref_page.py BQT:1499 --image 2>&1 | head -70",
 "description": "Fetch BQT p.1499"
}
```


### [2026-09-14T00:57:01.792Z] TOOL RESULT

```
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1499.png
REF: BQT:1499  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 292  OCR-lang: fas

۱۸۹۵۸ فلیند
گوبند که آنرا ‎)٩(‏ از غل وغش پاك و پاکیزه قللف - بنتح اول‌وسکون تانی‌وذال ضطه‌دارء
ساخته باشند عموماً و پنبه‌ای که آن را از پنبه ,| درعربی بمعنی بربدن و قطم کردن باغسویکس
دانه جدا کرده باشند خصوصاً ‎٩‏ . اول پارهای جگر و جگر اشتر راکویند ۹.

فلخید - بر وزن فهمید » پنبه دانه را قلرز ۷ - بغتح اول وثانی وسکون رای
کوبند ۱ - و ماضی فلخیدن هم‌هست بمنی‌پنبه | بی‌نقطه و زای نقطه‌دار . پمعنی زله باشد وآن
دانه را از پنبه جداکرد ؟ - وکسیرانیزکوبند | خوردنی وطمامی باشد(؟) که ازمهماتیهاوعروسیها
که پنبه‌دانه را از پنبه بیرون آورد - وینبه‌زنرا | درکربای پاره ودستمال (۳) بندند .
هم میگویند بعنی‌شخص ی که پنبه را حلاجی کند فلرز نگ ۸ - بفتح اول و ثانی وزای
- و بمعنی پنبه زدن و حلاجی کردن هم کفته‌اند. | نقطه‌دار وسکون نون وکاف فارسی » بمعنی فلرز
که مصدر باشد ویمعنی ماضی‌هم آمده است بعنی است که خوردنی و طعامی باشد که از مهمانیها
پنبه زد وحلاج ی کرد . برداشته بجای دیگر برند .
قلخیدن * - بروزن فهمیدن » بممنی فلشاگ - بکر اول ونانی وسکون‌شین
پنیه‌دانه از پنبه برآوردن باشد - و بممنی پنبه | نقطه‌داروکاف؛ کوزه‌ای که بجهت‌طفلان‌نقاشی کنند.
زدن و حلاجی کردن هم آمده است . فلفند با غين نقطه‌دار بروزن فرزند»
فلخیده ۴ « بروزن فهمیده » هرچیز | پرچین و خاریستی‌را کوبن دکه بر دور دیوار باغ
راگوبن که آنرا از غل وغش پاك ساخته باشند و زراعت کنند ‎٩‏ ؛ و جم اول و سیم هم درست
عموما و پنبه‌ای که آنرا از پنبه‌دانه جدا کرده است - و جا و محل خطرناکیرا هم کنته‌اند از
باشند بمنی پنبه دانه را از آن برآورده باشند | دربا که کشتیرا درآن خطر عظیم است و آنرا
خسوسا 9 . بمربی فم الاسد خوانند .#۰
69 خم۳:- آنرا )0( خم۳ : است . (۳) خم۳: دستمالی ؛ خم۱ : دسمالی.
۱ رد4 : فلخود » فلخیده . ۳ رد4 : فلخیدن . ۴ ع فلخودن. ر4:
حاشيه4 صفحهٌ قبل ورك: حاشیهٌ4 همین صفحه . ۴ - اسم مفعول ازه فلخیدن » :
موی زبر بغلس کته دراز وزقفا موی پاك فلخیده . طیان مرغزی «لغت فرس ۰6۱۹۹
8 - ر4 : فلخود , فلخوده . ‎٩‏ - بهر دومعنی عربی است . رل : منتهی‌الارب .
۷ «فظرزنگه (هم.) . ۸ «فرز :
آن کرنج و شکرش برداشت؟ پاك واندر آن دستار آن زن بست‌خاك
آن زن از دکان فرودآمد چوباد" پی فلرزتگش بدست اندر نهاد.
رودکی سمرقندی «لغت فرس ص ۲-۱۷۱ ورك: رشیدی؟ .
‎٩‏ - جنیش شیب تازبانه چو دید بگذرد ازسر دو صد فلفند .
شمسی فغری « رشیدی ؟ .
۵ فلقفل - ( بکسر اول وسوم ) معرب پلپل (۸ .م۰ ) » از که

سانسکربت 010021 «وبلیامن۱:۹۲۸> ورك: عقار*۳۱ف؛ کر دی ال ۹ ۴

« زاب ۹۵ +کیلکی ال - ( صصونه 8100۲ ) نوی از یره 8 9 ۱

بیدیها 881100688 که در هند و جزایر جنوب شرقی‌آسیا میروید .94 ۸

میوءٌ آن سته‌است قرمز رنگك که چون خعك شود.سیاه گردد و بسیار ۹ هم

تند است «کلکلاب ۰.۰۲۷۲ فلفل
```


## [2026-09-14T00:57:11.264Z] TOOL CALL #30: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1502.png"
}
```


### [2026-09-14T00:57:11.852Z] TOOL RESULT

```

```


## [2026-09-14T00:57:11.849Z] INPUT

[Image: original 1650x2546, displayed at 1296x2000. Multiply coordinates by 1.27 to map to original image.]


## [2026-09-14T00:57:29.228Z] TOOL CALL #31: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1499.png"
}
```


### [2026-09-14T00:57:29.847Z] TOOL RESULT

```

```


## [2026-09-14T00:57:29.844Z] INPUT

[Image: original 1650x2546, displayed at 1296x2000. Multiply coordinates by 1.27 to map to original image.]


## [2026-09-14T00:57:56.074Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT && cat > 1502.vision.txt <<'EOF'\n[Borhan-e Qate', ed. Mo'in, printed p. 1502 — read from the page image (pdf p. 295 of BQT_v3_picofile.pdf)]\n\nFootnote 9 (bottom of the page, continuing the entry فنجان whose headword stands on p. 1501):\n\n۹ ـ فنجان ـ (بکسر اول) = پنگان (هم.) از یونانی pínkx ، کردی fynjân, fynjan\nو fanjân ، ژابا ۲۹۵ ، گیلکی finjân ؛ پیاله ( چای‌خوری ، قهوه‌خوری) ، پنگان .\n\n[i.e. Mo'in: \"fenjān (with kasra on the first letter) = pangān (q.v.), from Greek pínkx\n[= πίναξ pínax; the Latin-script form as printed is pínkx], Kurdish fynjân/fynjan and\nfanjân (Jaba p. 295), Gilaki finjân; = piyāle (tea-cup, coffee-cup), pangān.\"]\n\nMain column of the same page (right-hand column) carries the entries فنجا ، فنجر ، فنجره ،\nand the left column فنجنگشت ، فنجنوش ، فنجیدن ، فند — the Greek etymology is only in the\nfootnote quoted above.\nEOF\ncat > 1499.vision.txt <<'EOF'\n[Borhan-e Qate', ed. Mo'in, printed p. 1499 — read from the page image (pdf p. 292 of BQT_v3_picofile.pdf)]\n\nFootnote 10 (bottom right of the page, with a woodcut of the pepper plant labelled فلفل):\n\n۱۰ ـ فلفل ـ ( بکسر اول و سوم ) معرب پلپل ( ه . م . ) ، از سانسکریت pippalî\n« ویلیامز ۱:۹۲۸ » ورک : عقار ۳۱۰ف ، کردی fylfil ، ژابا ۲۹۴ ، گیلکی filfîl =\n( Piper nigrum ) نوعی از تیرهٔ بیدیها Salicinées که در هند و جزایر جنوب شرقی آسیا\nمی‌رود . میوهٔ آن ستهایست قرمز رنگ که چون خشک شود سیاه گردد و بسیار تند است « گل‌گلاب ۲۷۲ » .\n\n[i.e. Mo'in: \"felfel (kasra on 1st and 3rd) is the mo'arrab (Arabicized form) of pelpel\n(q.v.), from Sanskrit pippalī (Monier-Williams I:928); cf. 'Aqqār 310; Kurdish fylfil\n(Jaba 294), Gilaki filfīl = Piper nigrum …\"]\nEOF\nls -la *.vision.txt",
 "description": "Save BQT vision transcriptions"
}
```


### [2026-09-14T00:57:57.139Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 1076 Sep  4 15:27 103.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 1325 Sep  7 16:52 1074.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 2600 Sep  6 17:59 1092.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 1579 Sep  6 17:54 1187.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  818 Sep  6 11:40 1219.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 1254 Sep  4 14:18 1225.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 1013 Sep  6 17:24 1237.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 1652 Sep  6 18:18 1266.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 1292 Sep  6 18:18 1267.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  741 Sep  6 11:43 1280.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 1085 Sep  5 22:32 1294.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 2048 Sep  6 17:03 1296.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  573 Sep  5 22:32 1299.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  238 Sep  5 22:32 1300.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  284 Sep  5 22:32 1302.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 1262 Sep  6 17:39 1320.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 2008 Sep  4 14:34 1385.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 1790 Sep  4 19:14 1445.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  958 Sep 13 20:57 1499.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  965 Sep 13 20:57 1502.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  797 Sep  6 11:43 1564.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 1691 Sep  6 11:41 1572.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 2183 Sep  6 11:32 1578.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 2566 Sep  6 17:53 1583.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 1100 Sep  6 16:54 1594.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 3246 Sep  6 16:38 1604.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 1332 Sep  6 11:56 1637.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  580 Sep  6 12:02 1648.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 1084 Sep  6 12:12 1688.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 2123 Sep  6 11:45 1689.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 1192 Sep  6 12:12 1709.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 1484 Sep  5 16:15 172.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 2166 Sep  6 16:48 1738.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 3319 Sep  6 11:37 1774.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 1117 Sep  5 22:20 1786.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 3889 Sep  6 11:01 1803.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 1288 Sep  5 01:39 180.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 1196 Sep  5 01:39 181.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  979 Sep  6 11:00 1854.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 1449 Sep  6 18:46 1874.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 2421 Sep  6 18:46 1876.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 2338 Sep  7 15:38 1922.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 2023 Sep  7 14:23 1931.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 2069 Sep  7 12:21 1949.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 1308 Sep  7 11:54 2001.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 1505 Sep  7 12:04 2002.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 1912 Sep  7 13:46 2014.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  668 Sep  6 11:00 2023.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 2090 Sep  7 13:40 2049.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 1942 Sep  7 11:56 2060.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 1238 Sep  7 12:21 2083.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 1832 Sep  7 14:22 2095.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 1487 Sep  7 14:20 2170.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 1264 Sep  7 15:34 2173.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  762 Sep  7 15:39 2195.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 1063 Sep  5 02:20 220.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 1091 Sep  7 15:39 2210.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 1558 Sep  6 11:26 2242.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  805 Sep  4 19:14 2246.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  842 Sep  7 12:21 2316.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  561 Sep  6 11:25 2417.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 2009 Sep  6 11:17 2420.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 1757 Sep  5 16:28 2427.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 2615 Sep  4 15:28 31.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 1339 Sep  5 16:12 333.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 1508 Sep  4 15:27 58.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 1931 Sep  4 15:02 70.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 1476 Sep  7 16:31 71.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 1606 Sep  4 14:54 72.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 1152 Sep  5 01:39 733.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  981 Sep  6 18:36 829.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 1658 Sep  5 16:20 902.vision.txt
```


## [2026-09-14T00:58:04.292Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BQT v1 پیله\"; grep -n \"پیله\" BQT_v1_pages.txt | head -20",
 "description": "grep BQT v1 for pileh"
}
```


### [2026-09-14T00:58:04.339Z] TOOL RESULT

```
=== BQT v1 پیله
8487:و پیله که دربالش و هالی ولحاف و اثال آن پر
```


## [2026-09-14T00:58:06.134Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN pile\"; grep -n -i \"pīla\\|pīle\\|pila 'cocoon\\|Cocon\" HRN.txt | head -20; echo \"=== HUB\"; grep -n -i \"pīla\\|pīle\\|Cocon\" HUB.txt | head -20",
 "description": "grep Horn/Hübschmann for pileh"
}
```


### [2026-09-14T00:58:06.205Z] TOOL RESULT

```
=== HRN pile
=== HUB
```


## [2026-09-14T00:58:14.499Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for w in \"پیله\" \"پيله\" \"پنگان\" \"فنجان\" \"پلپل\" \"فلفل\"; do echo \"=== $w\"; grep -c \"$w\" MON_part1.txt MON_part2.txt incoming/ARY/ARY_pages.txt 2>/dev/null; done",
 "description": "count Persian words in MON and ARY"
}
```


### [2026-09-14T00:58:15.624Z] TOOL RESULT

```
=== پیله
incoming/ARY/ARY_pages.txt:0
MON_part1.txt:18
MON_part2.txt:2
=== پيله
incoming/ARY/ARY_pages.txt:0
MON_part1.txt:0
MON_part2.txt:0
=== پنگان
incoming/ARY/ARY_pages.txt:0
MON_part1.txt:5
MON_part2.txt:0
=== فنجان
incoming/ARY/ARY_pages.txt:1
MON_part1.txt:1
MON_part2.txt:3
=== پلپل
incoming/ARY/ARY_pages.txt:0
MON_part1.txt:0
MON_part2.txt:1
=== فلفل
incoming/ARY/ARY_pages.txt:0
MON_part1.txt:11
MON_part2.txt:53
```


## [2026-09-14T00:58:18.734Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== MON پیله\"; grep -n -m8 \"پیله\" MON_part1.txt | cut -c1-400; echo; echo \"=== MON پنگان\"; grep -n -m6 \"پنگان\" MON_part1.txt | cut -c1-400",
 "description": "MON entries pileh, pangan"
}
```


### [2026-09-14T00:58:18.816Z] TOOL RESULT

```
=== MON پیله
6246:تارهای پیله برای دوختن و بافتن سازند؛ 
6250:شکون نیک دارند. کرم ابریشم: کرم پیله 
6258:تارهای پیله بهم کند و خیط و رشته سازد. 
21554:بدپیله: (0-)0]12-. (ص‌مر.) ند کینه» سخت 
35603:پیله: ()ه [- بیله - پله - فیله - فیلجه - 
35612:ابریشم گفته می‌شود. زیرا از الباف این پیله 
35614:می‌گردد. الیاف پیله را نوزاد حشرات که 
35631:پیله: )هام () (هم) کین عداوت» 

=== MON پنگان
32919:پنگان: حقوصعهم [ - - بنکام - فنجان» معر.] (.) 
32931:ظرف طعام و یا آب باشد پنگان گویند» 
32935:پنگان: (کد.) آسمان؛ نیلی پنگان. 
91590:آسمان. طاس و پنگان: طاس و ساعت. 
92467:0 قیف. نوعی از پنگان رویین.
```


## [2026-09-14T00:58:22.008Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"--- MON pileh ctx\"; sed -n '35598,35635p' MON_part1.txt; echo; echo \"--- MON pangan ctx\"; sed -n '32915,32940p' MON_part1.txt",
 "description": "MON context for pileh and pangan"
}
```


### [2026-09-14T00:58:22.084Z] TOOL RESULT

```
--- MON pileh ctx
پیلور: 0112۲ [- پبله‌ور | (ص‌مر. امر.) 
کسی که دوا فر وشد» داروفروش» صیدلانی. 
آنکه سوزن و نخ و مهره و مانند آن به 
خانه‌ها برد و فروشد» خرده‌فروش. 

پیله: ()ه [- بیله - پله - فیله - فیلجه - 
فیلق] (.) (جاذ.) محفظه‌ای که نوزاد برخضی 
حشرات دور خود نت و در داخل آن 
دورةٌ دگردیسی خود را میگذرانند و پس از 


را را ۳۳ 
آن خارج می‌گر دند. (جاد.) ببله بالااخص در 
تداول به محفظهٌ ایجاد شده به وسیلةً کرم 
ابریشم گفته می‌شود. زیرا از الباف این پیله 
در صنعت برای تهية تارهای ابریشم استفاده 
می‌گردد. الیاف پیله را نوزاد حشرات که 
صورت کرمی دارند به وسیلة غدد مترشحه 
بزاقی خود ترشح می‌کنند و به وسیله 
تفه ۶ یلا مسطمشن درمی آورند؛ 
ترشحات این غدد ابتدا شکل لعاب مانند و 
5 هس روت 

شته‌های سیار باریکك (شبه تار عنکبوت) 
0۳ فیلق» جوزالقز» پیلة کرم ابریشم؛ 
پیلة ابریشم. (جاذ.) کرمی که ازو ابریشم 
حاصل شود کرم ابریشم. کیسه‌ای که در آن 
اشیای مختلف را برای فروش ریزند و به 
دوش کشتند و گردانند؛ خربطه» تويره. 
بوی‌دان؛ عطردان. پشم و پیل کسی ریختن: 
(عم.) ناتوان شدن اوه از بين رفتن قدرت و 
همبنة او. بل ۱ بریشم: (جاد.) یله. کرم پیل: 
کرمی که از او ابریشم حاصل گر دد. 
پیله: )هام () (هم) کین عداوت» 
تاره تراک آزار و تعرض توآم با 
لجاجت. ببله بیدا کردن با کسی: کینه و 
عداوت یافتن نسبت بدو. پیله کسی به کسی 
گرفتن: آزار و تعرض وی بدو رسیدن. 

--- MON pangan ctx

پنکه: (0-)022۵ [هند] (۱.) بادیزن برقی. 
پنگ: : ود (.) ( گیا.) خوشةٌ خرما که پس از 
جدا کردن خرما به مصرف سوختن می‌رسد. 
پنگان: حقوصعهم [ - - بنکام - فنجان» معر.] (.) 


طاسی باشد از مس و امثال آن که در بن آن 
سوراخ تنگی کنند به قدر زمانی معین یعنی 
چون آن طاس را بر روی آب ایستاده نهند 
به قدر آن زمان معین پر شود و به ته آب 
شتا هقی آستاران رت ارشان دار شله 
ظرف آبی که در قدیم با آن پاس‌ها و 
ساعت‌های شبانروز را معین می‌کر ده‌انده 
ساعت آبی» صندوق ساعت» طاس ساعت؛ 
بنکام. هر کاسه و طاس رویین و مسین را که 
ظرف طعام و یا آب باشد پنگان گویند» 
کاس. تبوکک» سرطاس. جام؛ زلفه» اجانه؛ 
انجانه. طشت» تشت. ده برخ شبانروز. (چه 
شانر وز را به ده هنگام کر ده‌اند.) بیروزه 
پنگان: (کد.) آسمان؛ نیلی پنگان. 
پنهان: 060.۰ ,۳2130 (ص. ق.) نهفته» 
پوشیده» نهان. مسخفی» مکتوم» مستوره 
مدفون» مختفی» متواری» در سر محر مانه» 
ار و تا ]سیر 
کمینگاه» از کمین» از مکمن (-ز بنهان).
```


## [2026-09-14T00:58:33.482Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== MON2 فنجان\"; grep -n -m5 \"فنجان\" MON_part2.txt | cut -c1-300; echo \"=== MON2 پلپل\"; grep -n -m3 \"پلپل\" MON_part2.txt | cut -c1-300; echo \"=== MON1 فنجان\"; grep -n -m3 \"فنجان\" MON_part1.txt | cut -c1-300",
 "description": "MON fenjan, pelpel"
}
```


### [2026-09-14T00:58:33.599Z] TOOL RESULT

```
=== MON2 فنجان
9593:افیال؛ فیول. فیل و فنجان: (عم.) دو چیز غیر 
16889:کاپ: ۲ (.) فنجان. فنجانی که از طلا یا 
23792:فنجان سازند تا به زمین تواند نشست. سعب 
=== MON2 پلپل
8577:پلپلمونیه. ضح.- برخی از کتب فلفلمویه را 
=== MON1 فنجان
32919:پنگان: حقوصعهم [ - - بنکام - فنجان» معر.] (.)
```


## [2026-09-14T00:58:35.200Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AFM فنجان\"; grep -n \"فنجان\\|بنكام\\|پنگان\" AFM_pages.txt | head -10; echo \"=== AFM فلفل\"; grep -n \"فلفل\" AFM_pages.txt | head -10",
 "description": "Addi Shir for finjan and filfil"
}
```


### [2026-09-14T00:58:35.275Z] TOOL RESULT

```
=== AFM فنجان
721:(البنكام » ܓ < ܒ في البيهان القاطع > `
=== AFM فلفل
1754:( دار فلفل ) عند 06 الفلفل معناه 33 الفلفل
3085:( الفلفل ) لحا هندي شُديد اللرافة 9 به الطعام تعريب يليل ويواتة
3090:3 اتكلدالي | ܐ ١01105‏ 1 095 )فضا شخر الفلفل .
3091:والظاهر ان 5 فلفل وهو 3 نوع يحمل 0 9 3610
5797:فلفل ١١‏
```


## [2026-09-14T00:58:41.809Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"--- 3080\"; sed -n '3080,3095p' AFM_pages.txt; echo \"--- page tag near 3085\"; awk 'NR<=3085 && /\\[pdf page/ {p=$0} END{}' AFM_pages.txt; grep -n \"\\[pdf page\" AFM_pages.txt | awk -F: '$1<3085' | tail -2; echo \"--- 715-725\"; sed -n '715,725p' AFM_pages.txt; grep -n \"\\[pdf page\" AFM_pages.txt | awk -F: '$1<721' | tail -2",
 "description": "Addi Shir context and page"
}
```


### [2026-09-14T00:58:42.972Z] TOOL RESULT

```
--- 3080
ܨܢ 3 ܠܟ اعلديد فلغة في القُولاذ
( النولاذ) دك الحديد معرب عن 'يولاد ومنة ايضاً مشتق ( |[ ) وهو نخاس
17 نفك لبدو الور 0 او هو خمث المديد او 0 7 ) الغليظ
ܐܬܢܐ ٠والفارسي‏ 20 يطلق ܩ[ على السيف ܢܐ وهو 5 علدهم | سم
عفرمت١٠‏ ووثة السّر 3 ܦܠܕܐ والعبرالي ܟܪ والكردي بولا
( الفلفل ) لحا هندي شُديد اللرافة 9 به الطعام تعريب يليل ويواتة
29 ܕܠ 11 وهو 6 ع مع بالاتكلر 3.4 ع6 بار 1
و0606 ® ܕ 0156م ܢܐܩ ܐܚܝܬ و ܐ ]61 [110 بالروسة وبر او بوبر »3
وفافل بالكردّة و ܦܠܦܠ او ܦܠܦܠܬ او كلح إن 13330
ܐܬ مثتى مه ܦܠܦܠ ومعناه بذر بث ܐܠܐ( ܐܪܝ 0 ܫ
3 اتكلدالي | ܐ ١01105‏ 1 095 )فضا شخر الفلفل .
والظاهر ان 5 فلفل وهو 3 نوع يحمل 0 9 3610
لا حرافة فيه
* }| يبقى من اللبن في اسفل ܘ كله وهو اللأ
جد (١(‏ فل ) سجر 10 ذو زهر ܚ 1 الرائحة 5 0
9 0"( 052 :9 1 0090 5:01 38
--- page tag near 3085
--- 715-725
* (بنظيان) امراة شنظيان بنظيان اي سيّئة الخلق صحابة ٠‏ دهي معر بة عن
0 زيان اي أصل ܣ والضرز: وشُظنان اتناع مع التقديم
ܐ 9 تعريب 9 نبات من جوم الأرض © 3 ومنة بنفشه
ܥ < 3 0
( البليقة » 5 وقالوا فيه بق تعر يب ينيك
(البنك» فارسى ححض وهو اصل الثىء ومنة الكردي بن
(البنكام » ܓ < ܒ في البيهان القاطع > `
باككاف الفارسيّة على وزن سندان يطلق سموماً على القدح والكاس وخصوصاً على
0 من النحاس متعارف بين فلاحي الهند يتقاسمون به !ܬܐ ٠‏ وذلك انْ اصعاب
تكروم والزروع والبساتين يتمعون في راس المقسم ٠‏ فيلقون الطاس في الماء 9
ماء من ܗ الى ان يمتلى ]ܦ ܐ 2 في مدة
```


## [2026-09-14T00:58:52.984Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -c \"\\[pdf page\" AFM_pages.txt; echo \"=== PLA finjan\"; grep -n -i \"fingān\\|finǧān\\|finjan\\|pingān\\|pangān\\|panǧān\" incoming/PLA/PLA_pages.txt | head -10; echo \"=== PLA filfil\"; grep -n -i \"filfil\\|pilpil\" incoming/PLA/PLA_pages.txt | head -10",
 "description": "check AFM pagetags and grep Asbaghi"
}
```


### [2026-09-14T00:58:53.065Z] TOOL RESULT

```
0
=== PLA finjan
=== PLA filfil
```


## [2026-09-14T00:58:56.536Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && head -c 600 incoming/PLA/PLA_pages.txt; echo; echo \"=== try arabic\"; grep -n \"فنجان\\|فلفل\" incoming/PLA/PLA_pages.txt | head -10; echo \"=== djvu\"; grep -n -i \"filfil\\|fing\\|فلفل\\|فنجان\" incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt | head -15",
 "description": "inspect PLA text"
}
```


### [2026-09-14T00:58:56.598Z] TOOL RESULT

```
             Asya Asbaghi


Persische Lehnwörter im Arabischen




    OTTO HARRASSOWITZ   - WIESBADEN
          Asya Asbaghi
Persische Lehnwörter im Arabischen
               Asya Asbaghi


Persische Lehnwörter ım Arabischen




                    1988


    OTTO   HARRASSOWITZ    - WIESBADEN
CIP-Titelaufnahme der Deutschen Bibliothek

Asbaghi, Asya:
Persische Lehnwörter im Arabischen / Asya Asbaghi. -
Wiesbaden : Harrassowitz, 1988
  ISBN 3-447-02757-6




Alle Rechte vorbehalten. © Otto Harrassowitz, Wiesbaden 1988. Photomechanische und photographi-
sche Wiedergabe nur mit ausdrü
=== try arabic
=== djvu
5000:usa» - bangangast: "castus, Fünffingerkraut, Fünfblatt" aus dem pers. 
5003:a ah pan&-angost TI mp. so pang "fünf" + pre angost "Finger" 6, 
5006:wtoios - banfandadt: "Fünffingerkraut" = bankandast s. bankanfast . 
16847:olLassS_- kiStban: "Fingerhut" pers. 2, wahrscheinlich aus pers. Ol... 
16848:anguStban pers. af angost "Finger" MP. gupy angust + bäan q. v.
```


## [2026-09-14T00:59:02.102Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"fulful\\|filfil\\|fingän\\|fing&n\\|fingan\\|bankam\\|bankäm\\|pang&n\\|pingan\" incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt | head -20; echo \"=== f- section\"; grep -n \"^f[a-zäöü]*:\" incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt | head -30",
 "description": "Asbaghi f-entries"
}
```


### [2026-09-14T00:59:02.249Z] TOOL RESULT

```
=== f- section
```


## [2026-09-14T00:59:04.855Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \" - f[a-z]\" incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt | head -40",
 "description": "Asbaghi headwords starting with f"
}
```


### [2026-09-14T00:59:04.901Z] TOOL RESULT

```
7089:Wr - falbä : "eine Art Anzug" pers. 13, wahrscheinlich aus dem pers. 
7670:ls - fawäriä: "Magenstärkung" aus dem pers. AS gawärek 4 Syrah 
7789:a1,» - faurägiyya: "eine Geldeinheit", eigentlich Nisba v. Gaurgan 
7876:ir - fauzmäzag = guzmäzaß Ss. $uzmäzaß. 
7932:or - fausaq: "Palast; Zodiakus" aus dem pers. u kuSk > mp .pois köfk, 
15011:aL.b - farsiyya: "die persische Sprache" s. färs u. färsi. 
15017:>» - falüud: "süße Speise aus Mehl, Wasser u. Honig" pers. o29L 
15021:>>%b - falud = falüd q. v. 
15022:C>>b - falüdag = falüd a. v. 
15032:>»b - fanid: "reiner Kandis" pers. „| pänid 11 syr. =o . 
15059:Vs - fiträk: "Sattel" pers. 1, 
15063:Ss - fatkar: "Idol, Dämon! pers. _G peykar SP Io patkar ap. 
15069:amp)» - faräßin: Pl. v. .„o> farfin q. v. 
15071:>)’ - farädis: Pl. v. or,» firdus q. v. 
15074:Or» - faräzadaqg: Pl. v. c3%5 farzadag q. v. 
15075:ar)» - faräzin: Pl. v. cr farzin g. v. 
15079:zb - faräsih: Pl. v. > farsah a. v. 
15080:>): - farafir: Pl. v. „5, farfur q. v. 
15081:ls - farämin: Pl. v. ol.» farmän q. v. 
15082:Grels - farämin: Pl > £ 
15089:>12 - faränid: Pl. v. »> farand q. v. 
15092:Ge» - farbiyün = farfiyun q. v. 
15120:lb; - firßärid = firfär q. ve °. 
15123:Ssb> - firdäri: "mit dem Zirkel gemacht"- 
15126:I - farfin: "Zaun" ” pers. un. 3 mp. yo) pargän "Wand, Mauer" 
15132:am» - farha: "junge Henne" pers.c&, parpahn ?. 
15135:ar - firdus:; "Paradies" a. pairidaeza "kreisförmig, rund" °— mp. 
15159:ob - farzän: "die Königin im Schach" pers. s. farzäna 
15189:&!,,> - farzäna: "weise, gelehrt" mp. se&do frazänak "weise" 
15192:Gr - farzadag: "Teigklumpen, Brotkrumen" pers. eo», purazdeh 5 ?. 
15194:9,2 - farzan = farzan q. v. 
15195:@# - farzin = farfin q. v. 
15198:0X? - furus: Pl. v.cswl färsi q. v. 
15201:Sims - farastük: "Schwalbe" s. farästük *. 
15204:> - farsah: "Parasange,; ein persisches Maß, ungefähr 6232 mt pers. 
15208:Bw - farsak: "Pfirsich", dtsch. Pfirsich s. mazad ıl, 
15215:338 - farfur = fagfür a. v. 14, 
15218:5»? - farfürl: "Porzellan" Nisba v.G,»> farfür q. v. 
15247:> - farfir = farfur g. v. 
15251:ki; - farkär = fardar a. v. 2,
```


## [2026-09-14T00:59:10.223Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '15251,15450p' incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt | grep -n -i \"ful\\|fil\\|fin\" | head -30",
 "description": "Asbaghi f entries continued"
}
```


### [2026-09-14T00:59:10.275Z] TOOL RESULT

```
163:oe,» - filäwira: Pl. v._» filür q. v. 4 
167:_.. - filür: "Apotheker" pers. ?. s. filäwira. 
168:©2L5 - finafin: Pl. v.glo,» finfan q. v.
```


## [2026-09-14T00:59:12.886Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '15415,15470p' incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt",
 "description": "Asbaghi finjan entry"
}
```


### [2026-09-14T00:59:12.936Z] TOOL RESULT

```
Arab _ falangamisk = faranfamiäk q. v. 5 
_.. - filür: "Apotheker" pers. ?. s. filäwira. 
©2L5 - finafin: Pl. v.glo,» finfan q. v. 


„bs - fanär: "Leuchtturm, Laterne" pers, 6, 


las - in$än: "Porzellanschale; Kaffeetasse" pers. o%& pangän 7 


<< mp. So Paygal "Tasse" 8, syr. we 9, 


Fun s. 
Oi» - fundug: "Haselnuß" mp. na Pundak 10 aram. 653 11, 


1. Nyberg Bd. IIs. v. 

2. ebda. 

3. Muhit s. v., Addai Scher s. v. 

4. al-Mu°arrab s. v., Muhit s. v. 

5. Kamal s. v. 

6. Muhit s. v. 

7. al-MuCarrab s. v., Muhit s. v., al-Mungid s. v. 
8. Mackenzie s. v. 

9, Thesaurus syriacus Bd. 2 S. 3174, 

10. BQ. s. v., Bundahißön s. v., Mackenzie s. v. 
11. Löw s. v. 


fanraß 212 futa_ 


&>- fanrag: "ein Tanz, bei dem die Tanzenden sich an den Händen halten" 
2 


pers. aaı, pange "Hand, Pfote" "m. so» panfak ”. 

PER 3 Pe 4 

uw - fank: "Wiesel; Biber" pers. ”, wahrscheinlich aus pers. —ıL palang 
"Leopard, Biber" mit tot. prog. ass. v. l in n vgl. mit dtsch. flink 
Auch dtsch, Biber ist m. E. verwandt mit pers. babar mp. 3, babar 
"Tiger" u. >, babrag "Biber", engl. beaver 4
```


## [2026-09-14T00:59:24.989Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD\"; grep -n -i \"paygāl\\|pygʾl\\|pangān\\|pingān\\|pilpil\\|pylpyl\" PHD.txt PHD_mackenzie.txt | head -20; echo \"=== NYB\"; grep -n -i \"paygāl\\|pangān\\|pilpil\" NYB_vol2_glossary.txt | head -10",
 "description": "MacKenzie/Nyberg for paygal, pangan, pilpil"
}
```


### [2026-09-14T00:59:25.056Z] TOOL RESULT

```
=== PHD
PHD.txt:1462:cup-maker paygālgar.
PHD.txt:4759:pah, pay pahnāy pahn pāyag paygāl
PHD.txt:4760:1 3pahréxtan pahrez l-pahréz- pahlawig pahlüg pahlom pahlomih paygālgar pahast lpüy-
=== NYB
```


## [2026-09-14T00:59:26.914Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== ARB mo3rb فنجان\"; grep -n \"فنجان\\|بنكام\\|فلفل\" ARB_mo3rb.txt | head -10; echo \"=== ARB abdulraheem\"; grep -n \"فنجان\\|فلفل\" ARB_abdulraheem.txt | head -10",
 "description": "Jawaliqi for finjan and filfil"
}
```


### [2026-09-14T00:59:26.971Z] TOOL RESULT

```
=== ARB mo3rb فنجان
18160:(:) قال اذى شير : « الفنجان يرب «فتكن*» 20٠.‏ () الزيادةءن النسخ المخطوطة ٠‏ 
=== ARB abdulraheem
```


## [2026-09-14T00:59:32.271Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -B3 -A3 \"paygālgar\" PHD.txt | head -30; echo \"=== ARB ctx\"; sed -n '18150,18170p' ARB_mo3rb.txt",
 "description": "PHD paygal entry and ARB context"
}
```


### [2026-09-14T00:59:32.330Z] TOOL RESULT

```
1459-cultivated ābādān; — land warzbüm.
1460-cultivation abadanih,
1461-cup paygal.
1462:cup-maker paygālgar.
1463-curator stür.
1464-curds mast.
1465-cure bēšiz(ēn)-.
--
4757-stardsmur starwan stardih stard stabr stabrih stabrag
4758-staft
4759-pah, pay pahnāy pahn pāyag paygāl
4760:1 3pahréxtan pahrez l-pahréz- pahlawig pahlüg pahlom pahlomih paygālgar pahast lpüy-
4761-pas
4762-petig, sti stendag sidig, stéy sidigar stér stézag stowih stūwēn- stowēnīdan stē Sadwēs dīdan -istan stūn stūnag stor, stür sturg stūrīh stórgáh storban stard *stūš stūdan star
4763-staróámár
=== ARB ctx
9 5 يا شر داسو اش 
ويقال له أيضًا ” فلج “ . قال النايغة المعدى : 


االسسسسمسيده 





(:) قال اذى شير : « الفنجان يرب «فتكن*» 20٠.‏ () الزيادةءن النسخ المخطوطة ٠‏ 
وهذه المادةلم أجدها فى معا جم ألاغة إلا فى الميار» قال: « الفتجان > ,اجيم > إناء معروف 6 معرب 
ينكان" ؛ و يكس فاره © الوأحد بهاء ٠‏ بحجمه فتاجين 6 #لبال و .ابول 6 وسر وال وسراويل» ٠‏ 

(م) بكسرالفاء وتضم ٠‏ وفيه أربع لفات أخر» ذكت فى اللسان وسعجم لاف ود “2 » 
مشديد السين وحذف اليلاء الأولى » و *” قُستاط ©“ ب بدال الطاءالأولى ماء؟ مع شم الفاء وكدرها فييما ٠‏ 
وفى ياقوت قتح الفاء فى الثانية بدل الكسر» وهو خط من الناسخ أو المصحم ٠‏ ووقع فى الأساث أيضأ خطاً 
مايعى فى قوله «ركسر التاء لغة فين »> وصوايه « ركمر الفاء» وق القاموس لفتان أخريان « الفستات» 
ادبن مع شم الفاء وكدرها ٠‏ وقال ياقوت : « و يجع فساطبط ال التراء فق تادر رحن امم 
تساتيط ول أسمعها فساسيط » (١ ٠‏ اطاط ©“ فى اغة العرب : شرب من الأبنية فى السفر 
دون السادق» ويه سمت المدنة ٠‏ وقيل : مجتمم أهل الكورة حوالى مسجد جماعمم ٠‏ هكذا قسره
```


## [2026-09-14T00:59:43.319Z] TOOL CALL #50: Bash

```json
{
 "command": "sed -n 1,40p /home/sfmqrb/git/rishe/tools/fetch_source.py",
 "description": "read fetch_source.py"
}
```


### [2026-09-14T00:59:43.378Z] TOOL RESULT

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
```


## [2026-09-14T00:59:49.547Z] TOOL CALL #51: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/%D9%81%D9%86%D8%AC%D8%A7%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%D9%BE%D9%86%DA%AF%D8%A7%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%CF%80%CE%AF%CE%BD%CE%B1%CE%BE\" \\\n \"https://en.wiktionary.org/wiki/%D9%BE%DB%8C%D9%84%D9%87\" ; do\n timeout 120 python3 tools/fetch_source.py \"$u\" --note \"page 403 verification\" 2>&1 | tail -2; done",
 "description": "Archive Wiktionary pages for finjan, pangan, pinax, pileh"
}
```


### [2026-09-14T00:59:53.912Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/9ef42ff46eeb7f50.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/af17d8c5a1f42a91.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3cc14fab85bd323e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/047074afaa8d35e7.txt
```


## [2026-09-14T00:59:56.909Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 9ef42ff46eeb7f50 af17d8c5a1f42a91 047074afaa8d35e7; do echo \"########## $f\"; grep -n -i -A12 \"Etymology\" $f.txt | head -60; done",
 "description": "read wiktionary finjan/pangan/pileh"
}
```


### [2026-09-14T00:59:58.094Z] TOOL RESULT

```
########## 9ef42ff46eeb7f50
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Noun 
69-
70- 1.3.1 
71- Declension 
72-
73- 1.3.2 
74- Descendants 
--
82: Etymology 
83-
84- 2.2 
85- Pronunciation 
86-
87- 2.3 
88- Noun 
89-
90- 2.3.1 
91- See also 
92-
93- 3 
94- Ottoman Turkish 
--
102: Etymology 
103-
104- 3.3 
105- Noun 
106-
107- 3.3.1 
108- Declension 
109-
110- 3.3.2 
111- Derived terms 
112-
113- 3.3.3 
114- Descendants 
--
128: Etymology 
129-
130- 4.3 
131- Pronunciation 
132-
133- 4.4 
134- Noun 
135-
136- 4.5 
137- Further reading 
138-
139- 5 
140- South Levantine Arabic 
--
145: Etymology 
146-
147- 5.2 
148- Pronunciation 
########## af17d8c5a1f42a91
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Noun 
69-
70- 1.3.1 
71- Declension 
72-
73- 1.3.2 
74- Descendants 
--
154: Etymology
155- [ edit ] 
156-
157: Etymology tree
158-
159- Ancient Greek πίναξ ( pínax ) bor. 
160- Aramaic פִּינְכָא ( pīnəkā ) 
161- Classical Syriac ܦܝܢܟܐ ( pīnəḵā ) bor. ? 
162- Persian پنگان 
163-
164- Presumed to be borrowed, alongside Ossetian фынг ( fyng ) , фингӕ ( fingæ , “ table ” ) , [ 1 ] from Ancient Greek πίναξ ( pínax ) , πίνακος ( pínakos , “ wooden plank, dish, writing table ” ) , [ 2 ] possibly via Classical Syriac ܦܝܢܟܐ ( pinkā ) . [ 3 ] Perhaps cognate with Sanskrit पिनाक ( pínāka , “ staff, stick ” ) . [ 4 ] Whereas according to Vinson this is all from a compound of Middle Chinese , Mandarin 瓫 ( pén , “ flat dish ” ) ) and 盎 ( àng , “ wide-bellied bowl ” ) (perhaps instead 銀  / 银 ( yín , “ silver ” ) , 案 ( àn , “ desk, table ” ) ?), however not attested, so alternatively he suggests 平安 ( píng'ān , “ tranquil, safe ” ) printed onto Chinese household appliances like vases. [ 5 ] 
165-
166- Pronunciation
167- [ edit ] 
168-
169- ( Classical Persian ) IPA ( key ) : /pin.ˈɡaːn/ 
--
261: Pages with etymology trees 
262: Persian entries with etymology trees 
263- Sanskrit terms with non-redundant manual transliterations 
264- Mandarin terms with redundant transliterations 
265- Chinese terms with redundant transliterations 
266- Pages with entries 
267- Pages with 1 entry 
268- Requests for inflections in Persian noun entries 
269- Requests for inflections in Persian entries 
270-
271- This page was last edited on 24 August 2026, at 15:25.
272-
273- Definitions and other text are available under the Creative Commons Attribution-ShareAlike License ; additional terms may apply. By using this site, you agree to the Terms of Use and Privacy Policy. 
274-
########## 047074afaa8d35e7
```


## [2026-09-14T01:00:07.233Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"##### finjan arabic\"; grep -n -i \"pingān\\|pangān\\|pínax\\|Borrowed from\\|Persian\" 9ef42ff46eeb7f50.txt | head -25; echo; echo \"##### pileh\"; sed -n '140,230p' 047074afaa8d35e7.txt",
 "description": "read finjan/pileh etymologies"
}
```


### [2026-09-14T01:00:07.292Z] TOOL RESULT

```
##### finjan arabic
120: Persian 
122: Toggle Persian subsection 
245: Ancient Greek πίναξ ( pínax ) bor. 
248: Classical Persian پِنْگَان ( pingān ) bor. 
251: Borrowed from Classical Persian پِنْگَان ( pingān ) , possibly borrowed from Classical Syriac ܦܝܢܟܐ ( pīnəḵā ) , from Aramaic פִּינְכָא ( pīnəkā ) , borrowed from Ancient Greek πίναξ ( pínax ) .
447: → Persian: فنجان ( fenjân ) 
459: Ancient Greek πίναξ ( pínax ) bor. 
462: Classical Persian پِنْگَان ( pingān ) bor. 
466: Inherited from Arabic فِنْجَان ( finjān ) , borrowed from Classical Persian پِنْگَان ( pingān ) , possibly borrowed from Classical Syriac ܦܝܢܟܐ ( pīnəḵā ) , from Aramaic פִּינְכָא ( pīnəkā ) , borrowed from Ancient Greek πίναξ ( pínax ) .
505: Ancient Greek πίναξ ( pínax ) bor. 
508: Classical Persian پِنْگَان ( pingān ) bor. 
512: Borrowed from Arabic فِنْجَان ( finjān ) , borrowed from Classical Persian پِنْگَان ( pingān ) , possibly borrowed from Classical Syriac ܦܝܢܟܐ ( pīnəḵā ) , from Aramaic פִּינְכָא ( pīnəkā ) , borrowed from Ancient Greek πίναξ ( pínax ) . Doublet of پنكان ( pingân , “ cup ” ) .
889: Persian
894: Persian Wikipedia has an article on: فنجان 
908: Ancient Greek πίναξ ( pínax ) bor. 
911: Classical Persian پِنْگَان ( pingān ) bor. 
913: Persian فنجان 
915: Borrowed from Arabic فِنْجَان ( finjān ) , borrowed from Classical Persian پِنْگَان ( pingān ) , possibly borrowed from Classical Syriac ܦܝܢܟܐ ( pīnəḵā ) , from Aramaic פִּינְכָא ( pīnəkā ) , borrowed from Ancient Greek πίναξ ( pínax ) .
920: ( Classical Persian ) IPA ( key ) : /fin.ˈd͡ʒaːn/ 
968: Hayyim, Sulayman ( 1934 ), “ فنجان ”, in New Persian–English dictionary , Teheran: Librairie-imprimerie Béroukhim 
970: Dehkhoda, Ali-Akbar ( 1931– ), “ فنجان ”, in Dehkhoda Dictionary Institute , editors, Dehkhoda Dictionary (in Persian), Tehran: University of Tehran Press . 
978: From Arabic فِنْجان ( finjān ) , from Classical Persian پنگان ( pingān ) .
1003: Arabic terms borrowed from Classical Persian 
1005: Arabic terms derived from Classical Persian 
1020: Hijazi Arabic terms derived from Classical Persian 

##### pileh
```


## [2026-09-14T01:00:12.860Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && wc -l 047074afaa8d35e7.txt; sed -n '1,120p' 047074afaa8d35e7.txt | grep -n -i \"pile\\|etym\\|cocoon\" | head -30",
 "description": "inspect pileh wiktionary text"
}
```


### [2026-09-14T01:00:12.915Z] TOOL RESULT

```
5 047074afaa8d35e7.txt
```


## [2026-09-14T01:00:15.267Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && cat 047074afaa8d35e7.txt; echo \"=== index\"; tail -6 index.jsonl",
 "description": "check pileh fetch result"
}
```


### [2026-09-14T01:00:15.321Z] TOOL RESULT

```
URL: https://en.wiktionary.org/wiki/%D9%BE%DB%8C%D9%84%D9%87
FETCHED: 2026-09-14T00:59:53Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found=== index
{"url": "https://en.wiktionary.org/wiki/%D9%BE%D9%84", "file": "data/verification/sources/web/b462a4a24d1c76af.txt", "fetched": "2026-09-14T01:00:07Z", "status": 200, "bytes": 6322, "title": "پل - Wiktionary, the free dictionary", "note": "page 395, root Per 2 (pol/forat/-bar/par/porta) verification"}
{"url": "https://www.etymonline.com/word/Euphrates", "file": "data/verification/sources/web/6eaac385e459a207.txt", "fetched": "2026-09-14T01:00:07Z", "status": 200, "bytes": 6411, "title": "Euphrates - Etymology, Origin & Meaning of the Name", "note": "page 395, root Per 2 (pol/forat/-bar/par/porta) verification"}
{"url": "https://en.wiktionary.org/wiki/%D9%81%D8%B1%D8%A7%D8%AA", "file": "data/verification/sources/web/4bc475b6e31ac862.txt", "fetched": "2026-09-14T01:00:08Z", "status": 200, "bytes": 6958, "title": "فرات - Wiktionary, the free dictionary", "note": "page 395, root Per 2 (pol/forat/-bar/par/porta) verification"}
{"url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/p%C3%A9rtus", "file": "data/verification/sources/web/73354da5ae61a9b7.txt", "fetched": "2026-09-14T01:00:08Z", "status": 200, "bytes": 4086, "title": "Reconstruction:Proto-Indo-European/pértus - Wiktionary, the free dictionary", "note": "page 395, root Per 2 (pol/forat/-bar/par/porta) verification"}
{"url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/parn%C3%A1m", "file": "data/verification/sources/web/d0e64a347c59d293.txt", "fetched": "2026-09-14T01:00:09Z", "status": 200, "bytes": 4573, "title": "Reconstruction:Proto-Indo-Iranian/parnám - Wiktionary, the free dictionary", "note": "page 395, root Per 2 (pol/forat/-bar/par/porta) verification"}
{"url": "https://en.wiktionary.org/wiki/%D8%B1%D9%88%D8%AF%D8%A8%D8%A7%D8%B1", "file": "data/verification/sources/web/4a1909790b53bd7c.txt", "fetched": "2026-09-14T01:00:09Z", "status": 200, "bytes": 2650, "title": "رودبار - Wiktionary, the free dictionary", "note": "page 395, root Per 2 (pol/forat/-bar/par/porta) verification"}
```


## [2026-09-14T01:00:27.052Z] TOOL CALL #56: Bash

```json
{
 "command": "for u in \\\n \"https://www.etymonline.com/word/pepper\" \\\n \"https://www.etymonline.com/word/caterpillar\" \\\n \"https://www.etymonline.com/word/pillage\" \\\n \"https://www.etymonline.com/word/plush\" \\\n \"https://www.etymonline.com/word/pluck\" \\\n \"https://en.wiktionary.org/wiki/pilus\" \\\n \"https://en.wiktionary.org/wiki/%CF%80%E1%BF%96%CE%BB%CE%BF%CF%82\" \\\n \"https://en.wiktionary.org/wiki/%CF%80%CE%AD%CF%80%CE%B5%CF%81%CE%B9\" \\\n \"https://en.wiktionary.org/wiki/%D9%81%D9%84%D9%81%D9%84\" \\\n \"https://en.wiktionary.org/wiki/%E0%A4%AA%E0%A4%BF%E0%A4%AA%E0%A5%8D%E0%A4%AA%E0%A4%B2%E0%A5%80\" ; do\n timeout 120 python3 tools/fetch_source.py \"$u\" --note \"page 403 verification\" 2>&1 | tail -1; done",
 "description": "Archive etymonline and wiktionary pages"
}
```


### [2026-09-14T01:00:34.081Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/1fe6a93483fe940e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/bf316f9fd91a9625.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/048d4603615e9ec2.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/71072d3b098275dc.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/dc3bc768e0f218ae.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6e4946e8617689b6.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/646f3a76aea3175b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b0de6db9b7a9f299.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/10e25d69af150d3e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9bad58f7b8fc5941.txt
```


## [2026-09-14T01:00:37.699Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 1fe6a93483fe940e bf316f9fd91a9625 048d4603615e9ec2 71072d3b098275dc dc3bc768e0f218ae; do echo \"########## $f\"; head -3 $f.txt; grep -n -i \"pilus\\|pippali\\|piper\\|peperi\\|Latin\\|Old French\" $f.txt | head -12; done",
 "description": "read etymonline entries"
}
```


### [2026-09-14T01:00:39.008Z] TOOL RESULT

```
########## 1fe6a93483fe940e
URL: https://www.etymonline.com/word/pepper
FETCHED: 2026-09-14T01:00:28Z
STATUS: 200
25: "dried berries of the pepper plant," Middle English peper , from Old English pipor , from an early West Germanic borrowing of Latin piper "pepper," from Greek piperi , probably (via Persian) from Middle Indic pippari , from Sanskrit pippali "long pepper." The Latin word is the source of German Pfeffer , Italian pepe , French poivre , Old Church Slavonic pipru , Lithuanian pipiras , Old Irish piobhar , Welsh pybyr , etc.
31: "to sprinkle as with pepper," 1610s, from pepper (n.). Old English had gepipera . Meaning "to pelt with shot, etc.; hit with what pains or annoys" is from 1640s. Related: Peppered ; peppering .
42: condiment made from types of dried, ground sweet red peppers, 1839, from Hungarian paprika , a diminutive from Serbo-Croatian papar "pepper," from Latin piper or Modern Greek piperi (see pepper (n.)). A condiment made from a New World plant, introduced into Eastern Europe by the Turks; known in Hungary by 1569.
62: plant or herb of the primrose family, c. 1400, from Old French pimprenelle, earlier piprenelle (12c.) and directly from Medieval Latin pipinella name of a medicinal plant. This is perhaps from *piperinus "pepper-like" (so called because its fruits resemble peppercorns), a derivat
66: "to strike repeatedly" (with something), c. 1500, a word of unknown origin; according to one old theory it is perhaps from early 13c. pelten "to strike," a variant of pilten "to thrust, strike," from an unrecorded Old English *pyltan, from Medieval Latin *pultiare, from Latin pul
70: , green or red pepper," also pimienta "black pepper," from Late Latin pigmenta, plural of pigmentum "vegetable juice," from...[I]n med.L. spiced drink, hence spice, pepper (generally), Sp. pimiento, Fr. piment are applied to Cayenne or Guinea pepper..., capsicum; in Eng. the name has passed to allspice or Jamaica pepper....The piece of red sweet pepper stuffed in a pitted olive so called from 1918, earlier pimiento (1901), from Spanish....
90: "many-stemmed woody plant," from Old English bysc (found in place names), from West Germanic *busk "bush, thicket" (source also of Old Saxon and Old High German busc, Dutch bosch, bos, German Busch). Influenced by or combined with Old French (busche "firewood") and Medieval Latin
94: c. 1200, "vegetable substance aromatic or pungent to the taste added to food or drink to enhance the flavor," also "a spice used as a medication or an alchemical ingredient," from Anglo-French spece, Old French espice (Modern French épice), from Late Latin species (plural) "spice
########## bf316f9fd91a9625
URL: https://www.etymonline.com/word/caterpillar
FETCHED: 2026-09-14T01:00:29Z
STATUS: 200
25: "larva of a butterfly or moth," mid-15c., catyrpel , probably altered (by association with Middle English piller "plunderer;" see pillage (n.)) from Old North French caterpilose "caterpillar" (Old French chatepelose ), literally "shaggy cat" (probably in reference to the "wooly-bear" variety), from Late Latin catta pilosa , from catta "cat" (see cat (n.)) + pilosus "hairy, shaggy, covered with hair," from pilus "hair" (see pile (n.3)).
34: Old English catt (c. 700) "domestic cat," from West Germanic (c. 400-450), from Proto-Germanic *kattuz (source also of Old Frisian katte , Old Norse köttr , Dutch kat , Old High German kazza , German Katze ), from Late Latin cattus .
36: The near-universal European word now, it appeared in Europe as Latin catta (Martial, c. 75 C.E.), Byzantine Greek katta (c. 350) and was in general use on the continent by c. 700, replacing Latin feles . It is probably ultimately Afro-Asiatic (compare Nubian kadis , Berber kadiska , both meaning "cat"). Arabic qitt "tomcat" may be from the same source. Cats were domestic in Egypt from c. 2000 B.C.E. but not a familiar household animal to classical Greeks and Romans.
38: The Late Latin word also is the source of Old Irish and Gaelic cat , Welsh kath , Breton kaz , Italian gatto , Spanish gato , French chat (12c.). Independent, but ultimately from the same source are words in the Slavic group: Old Church Slavonic kotuka , kotel'a , Bulgarian kotka , Russian koška , Polish kot , along with Lithuanian katė and (non-Indo-European) Finnish katti , which is via Lithuanian.
46: mid-14c., "downy plumage;" late 15c, "fine, soft hair," from Anglo-French pyle or Middle Dutch pijl , both from Latin pilus "a hair" (source of Italian pelo , Old French pel ), a word of uncertain origin. Phonological evidence rules out transmission of the English word via Old French cognate peil , poil . Meaning "soft, raised surface of a regular and closely set kind upon cloth" is from 1560s.
58: late 14c., "act of plundering" (especially in war), from Old French pilage (14c.) "plunder," from pillier "to plunder, loot, ill-treat," possibly from Vulgar Latin *piliare "to plunder," probably from a figurative use of Latin pilare "to strip of hair," perhaps also meaning "to s
82: 1630s, "a ghost, specter, disembodied spirit" (earlier as larve, c. 1600), from Latin larva (plural larvae), earlier larua "ghost, evil spirit, demon," also "mask," a word from Roman mythology, of unknown origin; de Vaan finds a possible derivation from Lar "tutelary god" (see La
86: late 14c., "a thing done," from Latin actus "a doing; a driving, impulse, a setting in motion; a part in a play," and actum "a thing done" (originally a legal term), both from agere "to set in motion, drive, drive forward," hence "to do, perform," figuratively "incite to action; 
90: early 15c., "correspondence, proportion," from Old French analogie or directly from Latin analogia, from Greek analogia "proportion," from ana "upon, according to" (see ana-) + logos "ratio," also "word, speech, reckoning" (from PIE root *leg- (1) "to collect, gather," with deriv
########## 048d4603615e9ec2
URL: https://www.etymonline.com/word/pillage
FETCHED: 2026-09-14T01:00:29Z
STATUS: 200
25: late 14c., "act of plundering" (especially in war), from Old French pilage (14c.) "plunder," from pillier "to plunder, loot, ill-treat," possibly from Vulgar Latin *piliare "to plunder," probably from a figurative use of Latin pilare "to strip of hair," perhaps also meaning "to skin" (compare figurative extension of verbs pluck , fleece ), from pilus "a hair" (see pile (n.3)).
36: "to plunder, despoil, strip of money or goods by open violence," 1590s, from pillage (n.). Related: Pillaged ; pillaging; pillager . The earlier form of the verb in English was simply pill (late Old English pilian ), which probably is from Medieval Latin pillare .
43: mid-14c., "downy plumage;" late 15c, "fine, soft hair," from Anglo-French pyle or Middle Dutch pijl , both from Latin pilus "a hair" (source of Italian pelo , Old French pel ), a word of uncertain origin. Phonological evidence rules out transmission of the English word via Old French cognate peil , poil . Meaning "soft, raised surface of a regular and closely set kind upon cloth" is from 1560s.
47: "larva of a butterfly or moth," mid-15c., catyrpel , probably altered (by association with Middle English piller "plunderer;" see pillage (n.)) from Old North French caterpilose "caterpillar" (Old French chatepelose ), literally "shaggy cat" (probably in reference to the "wooly-bear" variety), from Late Latin catta pilosa , from catta "cat" (see cat (n.)) + pilosus "hairy, shaggy, covered with hair," from pilus "hair" (see pile (n.3)).
69: "that which is obtained or offered as the reward of exertion or contest; reward or symbol of victory," spelling alteration of Middle English prise (c. 1300 in this sense), from Old French pris "price, value, worth; reward" (see price (n.)). Figuratively, "anything worth striving 
73: early 14c., riflen (implied in rifling), "to plunder or pillage" (a place, house, receptacle, bag, etc.), from Old French...wrinkle," Old High German riffilon "to tear by rubbing," Old Norse rifa "grapple, seize; pull up, tear, break," hrifsa "rob, pillage...
77: violently of clothes, strip a slain enemy," from Anglo-French espoiller, Old French espoillier, espillier "strip, plunder, pillage..." and directly from Latin spoliare "strip, uncover, lay bare; strip of clothing, rob, plunder, pillage," a verb from spolia...It is attested from late 14c. in English as "strip with violence, rob, pillage, plunder (a place), dispossess; impoverish...
81: from Old French ravinos, ravinous, of people, "rapacious, violent," of water, "swift-flowing," from raviner "to seize, pillage...
89: "robbery, plunder, loot, theft," c. 1400, spoliacioun, Anglo-French esploiacion, from Latin spoliationem (nominative spoliatio) "a robbing, plundering, pillaging," noun of action from past-participle stem of spoliare "to plunder, rob" (see spoil (v.)). Related: Spoliator; spoliat
93: early 15c., hostilite, "hostile action," from Old French hostilité "enmity" (15c.), or directly from Late Latin hostilitatem (nominative hostilitas) "enmity," from Latin hostilis "inimical," from hostis, in earlier use "a stranger, foreigner," in classical use "an enemy," from PI
97: "act of plundering, pillaging," late 15c. (Caxton), from Old French depredacion (15c., Modern French déprédation), from Late Latin depraedationem (nominative depraedatio) "a plundering," from past-participle stem of Latin depraedari "to pillage," from de- "thoroughly" (see de-) +
########## 71072d3b098275dc
URL: https://www.etymonline.com/word/plush
FETCHED: 2026-09-14T01:00:29Z
STATUS: 200
25: "soft fabric, cloth having a softer and longer nap than that of velvet," 1590s, from French pluche "shag, plush," contraction of peluche "hairy fabric," from Old French peluchier "to pull, to tug, to pluck" (the final process in weaving plush), from Vulgar Latin *piluccare "remove hair" (see pluck (v.)). Related: Plushy ; plushness .
37: Middle English plukken , "pull (something) off or out from a surface" (especially hair or feathers, but also teeth), from late Old English ploccian , pluccian "pull off, cull," from West Germanic *plokken (source also of Middle Low German plucken , Middle Dutch plocken , Dutch plukken , Flemish plokken , German pflücken ). This is perhaps from an unrecorded Gallo-Roman or Vulgar Latin *piluccare (source of Old French peluchier , late 12c.; Italian piluccare ), a frequentative, ultimately from Latin pilare "pull out hair," from pilus "hair" (see pile (n.3)). But despite the similarities, OED finds difficulties with this and cites gaps in historical evidence. From late 14c. as "to pull sharply with a sudden jerk or force (of the strings of a bow, harp, etc.). Related: Plucked ; plucking .
53: mid-15c., "lax, flaccid, soft, tender" (obsolete or dialectal), from Old French lasche "soft, loose, slack, negligent, cowardly," from laschier "loosen," from Late Latin laxicare "become shaky," related to Latin laxare "loosen," from laxus "loose" (from PIE root *sleg- "be slack,
57: mid-14c., "real, ordinary; earthly, drawn from the material world" (contrasted with spiritual, mental, supernatural), a term in scholastic philosophy and theology, from Old French material, materiel (14c.) and directly from Late Latin materialis (adj.) "of or belonging to matter,
61: late 15c. (Caxton), "a building," a sense now obsolete, from Old French fabrique (14c.), verbal noun from fabriquer (13c.), from Latin fabricare "to make, construct, fashion, build," from fabrica "workshop," also "an art, trade; a skillful production, structure, fabric," from fab
65: c. 1400, "an end, settlement, retribution," from Old French finance "end, ending; pardon, remission; payment, expense; settlement of a debt" (13c.), noun of action from finer "to end, settle a dispute or debt," from fin (see fine (n.)). Compare Medieval Latin finis "a payment in 
69: mid-13c., "unblemished, refined, pure, free of impurities," also "of high quality, choice," from Old French fin "perfected, of highest quality" (12c.), a back-formation from finire or else from Latin finis "that which divides, a boundary, limit, border, end" (see finish (v.)); he
77: late 14c., solucioun, "explanation, answer; interpretation of a dream; the dissolving of a substance in a liquid, transformation of matter to a liquid state," from Old French solucion "division, dissolving; explanation; payment" and directly from Latin solutionem (nominative solu
81: "artificer in timber, one who does the heavier sort of wood-working," c. 1300 (attested from early 12c. as a surname), from Anglo-French carpenter, Old North French carpentier (Old French and Modern French charpentier), from Late Latin (artifex) carpentarius "wagon (maker); carri
########## dc3bc768e0f218ae
URL: https://www.etymonline.com/word/pluck
FETCHED: 2026-09-14T01:00:30Z
STATUS: 200
25: Middle English plukken , "pull (something) off or out from a surface" (especially hair or feathers, but also teeth), from late Old English ploccian , pluccian "pull off, cull," from West Germanic *plokken (source also of Middle Low German plucken , Middle Dutch plocken , Dutch plukken , Flemish plokken , German pflücken ). This is perhaps from an unrecorded Gallo-Roman or Vulgar Latin *piluccare (source of Old French peluchier , late 12c.; Italian piluccare ), a frequentative, ultimately from Latin pilare "pull out hair," from pilus "hair" (see pile (n.3)). But despite the similarities, OED finds difficulties with this and cites gaps in historical evidence. From late 14c. as "to pull sharply with a sudden jerk or force (of the strings of a bow, harp, etc.). Related: Plucked ; plucking .
40: mid-14c., "downy plumage;" late 15c, "fine, soft hair," from Anglo-French pyle or Middle Dutch pijl , both from Latin pilus "a hair" (source of Italian pelo , Old French pel ), a word of uncertain origin. Phonological evidence rules out transmission of the English word via Old French cognate peil , poil . Meaning "soft, raised surface of a regular and closely set kind upon cloth" is from 1560s.
48: "soft fabric, cloth having a softer and longer nap than that of velvet," 1590s, from French pluche "shag, plush," contraction of peluche "hairy fabric," from Old French peluchier "to pull, to tug, to pluck" (the final process in weaving plush), from Vulgar Latin *piluccare "remove hair" (see pluck (v.)). Related: Plushy ; plushness .
60: c. 1200, rolle, "rolled-up piece of parchment or paper, scroll" (especially one inscribed with an official record), from Old French rolle "document, parchment scroll, decree" (12c.), Medieval Latin rotulus "a roll of paper" (source also of Spanish rollo, Italian rullo), from Lati
68: (implied in past participle excerpte "taken from a book"), from Latin excerptus, past participle of excerpere "pluck out,...pick out, extract," figuratively "choose, select, gather," also "to leave out, omit," from ex "out" (see ex-) + carpere "pluck..., gather," from PIE root *kerp- "to gather, pluck, harvest."...
72: slender" (17c.), from Italian svelto "slim, slender," originally "pulled out, lengthened," past participle of svellere "to pluck...or root out," from Vulgar Latin *exvellere, from Latin ex- "out" (see ex-) + vellere "to pluck, stretch," from PIE *wel-no...
76: according to OED is from Vulgar Latin *scarsus, from a presumed *escarpsus, earlier *excarpsus, past participle of *excarpere "pluck...out," from classical Latin excerpere "pluck out" (see excerpt)....
92: a word applied at first to almost any of the larger fungi but later to the agaricoid fungi and especially the edible varieties, mid-15c., muscheron, musseroun (attested 1327 as a surname, John Mussheron), from Anglo-French musherun, Old French meisseron (11c., Modern French mouss
```


## [2026-09-14T01:01:00.093Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 6e4946e8617689b6 646f3a76aea3175b b0de6db9b7a9f299 10e25d69af150d3e 9bad58f7b8fc5941; do echo \"########## $f\"; head -4 $f.txt; grep -n -i \"from \\|uncertain\\|Proto-Indo\\|borrow\" $f.txt | head -14; done",
 "description": "read wiktionary pilus/pilos/peperi/filfil/pippali"
}
```


### [2026-09-14T01:01:01.212Z] TOOL RESULT

```
########## 6e4946e8617689b6
URL: https://en.wiktionary.org/wiki/pilus
FETCHED: 2026-09-14T01:00:31Z
STATUS: 200
TITLE: pilus - Wiktionary, the free dictionary
222: From Wiktionary, the free dictionary
244: Learned borrowing from Latin pilus ( “ hair ” ) . Doublet of pile .
323: Uncertain. Older sources reconstruct Proto-Indo-European *pilo- ( “ hair ” ) , with Latin pilleus ( “ felt cap ” ) , Ancient Greek πῖλος ( pîlos , “ wool or hair wrought into felt ” ) , Proto-Slavic *pь̑lstъ ( “ felt ” ) as cognates, [ 1 ] [ 2 ] but this is no longer accepted. [ 3 ] [ 4 ] [ 5 ] 
465: Borrowings:
488: Proto-Indo-European *peys- der. 
489: Proto-Indo-European *pistlom 
494: From pīlum ( “ javelin ” ) .
572: R. E. Latham , D. R. Howlett, & R. K. Ashdowne, editors ( 1975–2013 ), “ pilus ”, in Dictionary of Medieval Latin from British Sources ‎ [2] , London: Oxford University Press for the British Academy , →ISBN , →OCLC 
586: Retrieved from " https://en.wiktionary.org/w/index.php?title=pilus&oldid=91351548 "
589: English learned borrowings from Latin 
590: English terms borrowed from Latin 
591: English terms derived from Latin 
592: English terms derived from Proto-Indo-European 
612: Latin terms derived from Proto-Indo-European 
########## 646f3a76aea3175b
URL: https://en.wiktionary.org/wiki/%CF%80%E1%BF%96%CE%BB%CE%BF%CF%82
FETCHED: 2026-09-14T01:00:31Z
STATUS: 200
TITLE: πῖλος - Wiktionary, the free dictionary
146: From Wiktionary, the free dictionary
156: From the same Proto-Indo-European source as Proto-Slavic *pьlstь ( “ felt ” ) , Old English felt ( English felt ) and probably Latin pilleus . A connection with Latin pilus ( “ a hair ” ) and pila ( “ a ball ” ) has been abandoned.
304: Retrieved from " https://en.wiktionary.org/w/index.php?title=πῖλος&oldid=88883075 "
306: Categories : Ancient Greek terms derived from Proto-Indo-European 
########## b0de6db9b7a9f299
URL: https://en.wiktionary.org/wiki/%CF%80%CE%AD%CF%80%CE%B5%CF%81%CE%B9
FETCHED: 2026-09-14T01:00:32Z
STATUS: 200
TITLE: πέπερι - Wiktionary, the free dictionary
148: From Wiktionary, the free dictionary
156: From an Indo-Aryan source; compare Sanskrit पिप्पलि ( pippali , “ long pepper ” ) . [ 1 ] 
299: Retrieved from " https://en.wiktionary.org/w/index.php?title=πέπερι&oldid=92281861 "
301: Categories : Ancient Greek terms borrowed from Indo-Aryan languages 
302: Ancient Greek terms derived from Indo-Aryan languages 
########## 10e25d69af150d3e
URL: https://en.wiktionary.org/wiki/%D9%81%D9%84%D9%81%D9%84
FETCHED: 2026-09-14T01:00:33Z
STATUS: 200
TITLE: فلفل - Wiktionary, the free dictionary
193: From Wiktionary, the free dictionary
215: Borrowed from Classical Persian پِلْپِل ( pilpil ) , from Sanskrit पिप्पलि ( pippali , “ long pepper ” ) .
822: Borrowed from Arabic فِلْفِل ( filfil ) , from Classical Persian پلپل ( pilpil ) , from Sanskrit पिप्पलि ( pippali , “ long pepper ” ) , ultimately from Dravidian . Compare Tamil திப்பலி ( tippali ) , Swahili pilipili , Aramaic פלפלא ( pelplā ) , Hebrew פלפל ( pilpél ) , Old Armenian պղպեղ ( płpeł ) , պղպիղ ( płpił ) , Armenian պղպեղ ( pġpeġ ) and Georgian პილპილი ( ṗilṗili ) , Iranian borrowings.
892: Inherited from Arabic فِلْفِل ( filfil ) , from Classical Persian پلپل ( pilpil ) , from Sanskrit पिप्पलि ( pippali , “ long pepper ” ) .
915: Retrieved from " https://en.wiktionary.org/w/index.php?title=فلفل&oldid=92515841 "
917: Categories : Arabic terms derived from Classical Persian 
918: Arabic terms derived from Indo-Aryan languages 
919: Arabic terms derived from Sanskrit 
920: Arabic terms derived from Dravidian languages 
921: Arabic terms borrowed from Classical Persian 
938: Persian terms borrowed from Arabic 
939: Persian terms derived from Arabic 
940: Persian terms derived from Classical Persian 
941: Persian terms derived from Dravidian languages 
########## 9bad58f7b8fc5941
URL: https://en.wiktionary.org/wiki/%E0%A4%AA%E0%A4%BF%E0%A4%AA%E0%A5%8D%E0%A4%AA%E0%A4%B2%E0%A5%80
FETCHED: 2026-09-14T01:00:34Z
STATUS: -1
TITLE:
```


## [2026-09-14T01:01:22.656Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN pil\"; grep -n -i \"pîl\\|pīl\\|pil[ae] \" HRN.txt | head -20; echo \"=== HUB pil\"; grep -n -i \"pîl\\|pīl\" HUB.txt | head -20",
 "description": "Horn/Hubschmann pil words"
}
```


### [2026-09-14T01:01:22.720Z] TOOL RESULT

```
=== HRN pil
=== HUB pil
```


## [2026-09-14T01:01:24.264Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== ARY latin index PILE\"; grep -n -i \"pile\\|pilus\\|pinax\\|pippal\" incoming/ARY/ARY_latin_index_pages.txt | head -20",
 "description": "ARY latin index"
}
```


### [2026-09-14T01:01:24.318Z] TOOL RESULT

```
=== ARY latin index PILE
1062:Deaths NPcoknt yoy yp 50 pile oT ae ys S grb sT 5534 LOLT oy gal
1195:say gel pile LS 30 ph Scant Gh J Es shy came 9 tals sb Oe
3785:BANDA (LITHUANIAN) J! 3 BAND SPANISH) pile!
4882:PILE ALBANIAN) gis PAKSHMAN, PAKSHMALA
8747:‘REFERENCES betKey LIBRE (SPANISH) pile!
10069:POKORNY, ~S*~*~*~«ML: ESTERIL (SPANISH) pile! |
12429:HGSGATO pile) CHAT gests y CATUS oS yKATZE gliT 5 CAT poJ63i laejly lt
12734:SIRDS ALATVIAN) (33) i CUER, CORAZON (SPANISH) pile! f
13425:2 AF ia piles BOdUs 2205 oul oe
14372:IMJA RUSSIAN) 03, NOME LUTALIAN) pile!
```


## [2026-09-14T01:01:32.265Z] TOOL CALL #61: Bash

```json
{
 "command": "for u in \"https://abadis.ir/fatofa/%D9%BE%DB%8C%D9%84%D9%87/\" \"https://en.wiktionary.org/wiki/%D9%BE%D9%8E%DB%8C%D9%84%D9%87\" \"https://en.wiktionary.org/wiki/pile\"; do timeout 120 python3 tools/fetch_source.py \"$u\" --note \"page 403, pileh/pile\" 2>&1 | tail -1; done",
 "description": "fetch abadis pileh and wiktionary pile"
}
```


### [2026-09-14T01:01:36.062Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/86635d74340f5ae7.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/fc665c9ae8b53333.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/577eeb6f0273cf99.txt
```


## [2026-09-14T01:01:38.876Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && head -5 86635d74340f5ae7.txt; grep -n \"پیله\" 86635d74340f5ae7.txt | head -20",
 "description": "read abadis pileh"
}
```


### [2026-09-14T01:01:38.924Z] TOOL RESULT

```
URL: https://abadis.ir/fatofa/%D9%BE%DB%8C%D9%84%D9%87/
FETCHED: 2026-09-14T01:01:34Z
STATUS: 200
TITLE: پیله - معنی در دیکشنری آبادیس

4:TITLE: پیله - معنی در دیکشنری آبادیس
6:پیله - معنی در دیکشنری آبادیس 
10: پیله
13: مترادف پیله : ابریشم، کرم ابریشم، آماس، ورم، اصرار، تأکید، توبره، خریطه، طبله، عطردان، تعرض، عداوت، کینه، حقه، کلک، نادرستی، نیرنگ، دارو، دوا، تنش، تنیدن
20: پیله. [ ل َ / ل ِ ] ( اِ ) محفظه ابریشمین کرم ابریشم. ماده ای که کرم ابریشم از لعاب دهن دور خود می تند و در ساخت ابریشم بکار می آید. ( فرهنگ نظام ). بادامه. آن بادامچه بود که ابریشم ازاو گیرند. ( لغت نامه اسدی ). اصل ابریشم و غوزه ابریشم که کرم تنیده باشد. ( برهان ). غوزه ابریشم و کج. صلجه. شرنق. شرنقه. اصل ابریشم. ( صحاح الفرس ). فیلق. ( دهار ). فیله. پله. بیله. کناغ. نوغان. ابریشمی که کرم آنرا برگرد خود مثل بادام بتند. بیضه ابریشم که کرم تننده در آن جای گیرد. ( غیاث ) : 
22:در بریشم چو کرم پیله زمین. عنصری.
23:تاپیل چو یک فریشم پیله 
28:بیخرد، چون کرم پیله ، جان خود سازد هدر. ناصرخسرو.
29:کرم پیله همی بخود بتند
32:کرم پیله هم بدست خویشتن دوزد کفن. سنائی.
34:که کرم پیله نماید ورا عصای کلیم. سوزنی.
35:خصمش ز کم بقائی ماند بکرم پیله 
37:آنچه حق آموخت کرم پیله را
40:او نه از کرم پیله نامی شد. سعدی.
42:نه چون کرم پیله بخود برتنند. سعدی.
44:چو کرم مرده شمر کو درون پیله در است. کاتبی.
45:دمقاص ؛ ریسمان پیله. دمقص ؛ ابریشم یا ریسمان پیله که نوعی از ابریشم ردی است یا دیبا یا کتان. ( منتهی الارب ). || کرمی باشد که ازاو ابریشم حاصل شود. ( غیاث ). کرم ابریشم. ( برهان ). دودالقز به کرم تننده ابریشم. ( غیاث ) : و هوشنگ... انگبین از زنبور و ابریشم از پیله بیرون آورد. ( نوروزنامه ).
47:زرّ قراضه در وی چون تخم پیله مضمر. خاقانی.
49:چون تخم پیله زنده شوم باز بر درت. خاقانی.
54: ( اسم )پیکانی سر پهن پیکان تیر پیله : چنان چون سوزن از وشی و آب روشن از توزی بطوسی پیل بگذاری به آماج اندرون پیله . ( فرخی )
```


## [2026-09-14T01:01:51.290Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for w in \"pilocarpine\" \"pileus\" \"pilose\" \"caterpillar\" ; do echo \"=== $w\"; grep -n -m2 \"^$w,\" KLN_1966.txt | cut -c1-700; done",
 "description": "Klein entries for pilocarpine, pileus, caterpillar"
}
```


### [2026-09-14T01:01:52.448Z] TOOL RESULT

```
=== pilocarpine
=== pileus
=== pilose
28838:pilose,  adj.,  covered  with  hair  (bot.)  —  L.  pilosus, ‘hairy’,  fr.  pilus,  ‘hair’.  See  pile,  ‘hair’,  and  adj. suff.  -ose,  and  cp.  pilous, pilosity,  n.,  the  state  of  being  pilose.  —  ML. pilositds,  fr.  L.  pilosus.  See  prec.  word  and  -ity. pilot,  n.  —  MF.  (=  F.)  pilote,  fr.  It.  pilola,  fr. Olt.  pedota,  fr.  Byzantine  Gk.  *trr]8coT7)i;, ‘steersman’,  fr.  Gk.  mr)S6v,  ‘the  blade  of  an  oar’, which  is  rel.  to  mfjSAXiov,  ‘rudder’,  7nr)Sav,  ‘to bound’,  tnf)Sr)[ta,  ‘a  leaping,  bounding’,  fr.  I.-E. base  *ped-,  enlarged  form  of  base  *ped-,  ‘foot’, whence  Gk.  tteSt],  ‘fetter’, 
=== caterpillar
6796:caterpillar,  n.  —  ONF.  catepelose,  corresponding to  OF.  chatepelose,  fr.  Late  L.  catta  pilosa, ‘hairy  cat’.  For  the  etymology  of  Late  L.  catta see  cat.  L.  pilosa  is  fern,  of  pilosus,  ‘hairy’,  fr. pilus,  ‘hair’;  see  pile,  ‘hair’.  The  ending  of  the English  word  was  influenced  by  piller,  ‘one  who pills’  (see  pill,  ‘to  rob’).
```


## [2026-09-14T01:01:57.090Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -m3 \"pilocarpine\\|Pilocarpus\\|pilleus\\|pileus\" KLN_1966.txt | cut -c1-800; echo \"=== pile hair\"; grep -n -m4 \"pile,  n\\.\" KLN_1966.txt | cut -c1-800",
 "description": "Klein pilocarpine, pileus, pile"
}
```


### [2026-09-14T01:01:57.175Z] TOOL RESULT

```
20107:jaborandi,  n.,  the  dried  leaflets  of  S.  American shrubs  of  the  genus  Pilocarpus.  —  Port.,  fr.  Tupi yaborandi.
28820:Derivative:  pile,  tr.  v.,  to  form  a  pile, pile,  n.,  soft,  fine  hair.  —  ME.,  fr.  L.  pilus,  ‘hair’, rel.  to  pila,  ‘ball,  playing  ball’,  prob.  also  to pilleus,  ‘a  felt  cap’,  and  cogn.  with  Gk.  7ttXo<;, ‘felt’.  Cp.  depilate,  peel,  ‘to  strip  off’,  pelage, pellet,  pelon,  pelota,  pelt,  ‘to  strike’,  Pilea,  pileus, pill,  ‘a  little  ball  of  medicine’,  pill,  ‘to  rob;  to peel’,  pilule,  platoon,  plot,  ‘to  press  into  cakes’, plot,  ‘conspiracy’,  pluck,  plush,  poilu,  and  the second  element  in  caryopilite,  caterpillar,  horri- pilate.
28822:Pilea,  n.,  a  genus  of  plants,  the  richweed  (bot.)  — ModL.,  fr.  L.  pileus,  more  exactly  pilleus,  ‘felt cap’.  See  pileus.
=== pile hair
28815:pilch,  n.,  1 )  orig.  an  outer  garment  made  of  skin; 2)  a  light  saddle;  3)  an  infant’s  triangular wrapper,  worn  over  the  diaper.  —  OE.  pylece, fr.  ML .  pellicea,  'furred  garment’,  prop.  fem.  of L.  peliiceus.  made  of  skins’,  fr.  pellis,  ‘skin’.  See fell,  ‘hide',  and  cp.  pelisse, pilchard,  n.,  name  of  a  fish  of  the  herring  family. —  Fr.  earlier  pilcher,  a  word  of  uncertain  origin, pile,  n.,  a  heavy  timber  or  beam  driven  into  the ground  to  serve  as  a  support.  —  ME.,  ‘dart, stake',  fr.  OE.  pit,  ‘pointed  stake,  prickle’,  fr.  L. pilum,  ‘javelin;  pestle’  1  whence  also  ON.  pita, OHG.,  MHG.  pfil  (G.  Pfeil),  ‘arrow’],  which  is rel.  to  L.  pita,  ‘mortar’.  See 
28817:pile,  n.,  the  reverse  of  a  coin.  —  Prob.  fr.  pile,  ‘a heap’.
28818:pile,  n.,  a  large  heap.  —  ME.,  fr.  OF.  (=  F.)  pile, fr.  L.  pita,  ‘pillar’.  See  pillar  and  cp.  words  there
28820:Derivative:  pile,  tr.  v.,  to  form  a  pile, pile,  n.,  soft,  fine  hair.  —  ME.,  fr.  L.  pilus,  ‘hair’, rel.  to  pila,  ‘ball,  playing  ball’,  prob.  also  to pilleus,  ‘a  felt  cap’,  and  cogn.  with  Gk.  7ttXo<;, ‘felt’.  Cp.  depilate,  peel,  ‘to  strip  off’,  pelage, pellet,  pelon,  pelota,  pelt,  ‘to  strike’,  Pilea,  pileus, pill,  ‘a  little  ball  of  medicine’,  pill,  ‘to  rob;  to peel’,  pilule,  platoon,  plot,  ‘to  press  into  cakes’, plot,  ‘conspiracy’,  pluck,  plush,  poilu,  and  the second  element  in  caryopilite,  caterpillar,  horri- pilate.
```


## [2026-09-14T01:02:06.198Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -m3 -i \"pilocarpine\" FSD_vol1.txt FSD_vol2.txt FSD_vol3.txt FSD_vol4.txt WEB_vol1.txt 2>/dev/null | cut -c1-500",
 "description": "grep FSD/WEB for pilocarpine"
}
```


### [2026-09-14T01:02:06.295Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T01:02:09.758Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -m3 -i \"pilocarp\" FSD_vol3.txt FSD_vol4.txt WEB_vol1.txt KLN_1971.txt 2>/dev/null | cut -c1-400; echo \"=== jaborandi WEB\"; grep -n -m2 -i \"Pilocarpus\" WEB_vol1.txt KLN_1971.txt | cut -c1-400",
 "description": "grep for pilocarp"
}
```


### [2026-09-14T01:02:09.850Z] TOOL RESULT

```
KLN_1971.txt:127901:shrubs of the genus Pilocarpus . — Port., fr, Tupi 
KLN_1971.txt:182605:pilocarpine, pilocarpin, n., an alkaloid C n H, 6 N 2 0 2 
KLN_1971.txt:182607:Pilocarpus, n., a genus of shrubs of the rue fam- 
=== jaborandi WEB
KLN_1971.txt:127901:shrubs of the genus Pilocarpus . — Port., fr, Tupi 
KLN_1971.txt:182607:Pilocarpus, n., a genus of shrubs of the rue fam-
```


## [2026-09-14T01:02:12.190Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '182600,182615p' KLN_1971.txt",
 "description": "Klein 1971 pilocarpine entry"
}
```


### [2026-09-14T01:02:12.262Z] TOOL RESULT

```
pillow, n. — ME. pilwe , fr. OE. pyle, pylu , fr. L. 
pulvinus, ‘cushion, pillow’, whence also OS. puli, 
MDu. pdlu (Du. peluw), OHG. pfuliwi, pfulwo 
(MHG. pfiilwe , G. Pfuhl), of s.m. See pulvinus. 
Derivatives: pillow , tr. and intr. v., pillow- y, adj. 
pilocarpine, pilocarpin, n., an alkaloid C n H, 6 N 2 0 2 
(chem .) — See next word and chem. suff. -ine, -in. 
Pilocarpus, n., a genus of shrubs of the rue fam- 



ily (bot.) — ModL., compounded of Gk. 7tIXo<;, 
‘felt’, and xaprrdc, ‘fruit’. See pile, ‘hair’, and 

carpel.
```


## [2026-09-14T01:02:18.221Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== LAT pilus\"; grep -n -m3 \"^pilus\\|pilus:\" LAT.txt | cut -c1-200; grep -n -m2 \"pilleus\\|pilleum\" LAT.txt | cut -c1-300; echo \"=== LAT piper\"; grep -n -m3 \"piper\" LAT.txt | cut -c1-400",
 "description": "Ernout-Meillet pilus, pilleus, piper"
}
```


### [2026-09-14T01:02:18.314Z] TOOL RESULT

```
=== LAT pilus
47516:pilus. Suetone ecrit, Calig.44, plerisque centurionum... primos pilos
47541:pilus, -I m.: poil, cheveu. Les deux sens sont bien attestes,
25338:galerum n. (et galerus, Vg.Ae.7,688; galera C.Gracch.?): - pilleum
47498:ad pilleum uocare, T.L.34,33; 3 0 coiffe du nouveau-nd. Ancien (Pl.),
=== LAT piper
15196:piper , A fldchir le noa qni devient cummis (gum-; acc.cuna in dans
32373:de lasserpiciun, laserpiciun (faite aur le modble de cicer, piper,
37265:fructum ferens comestibilem, maiorem pipere, gustu suauem, unde et
```


## [2026-09-14T01:02:21.424Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '47541,47570p' LAT.txt; echo \"=== pilleus\"; sed -n '47490,47510p' LAT.txt; echo \"=== piper entry\"; grep -n \"piper, -eris\\|piper,-eris\\|piper -eris\" LAT.txt | head -3",
 "description": "Ernout-Meillet pilus/pilleus entries"
}
```


### [2026-09-14T01:02:21.531Z] TOOL RESULT

```
pilus, -I m.: poil, cheveu. Les deux sens sont bien attestes,
cf. Ov., A. A. 3, 194, d,uris aspera crura pilis, et Sen., Tranq. An. 8,3,
non minus molestum esse caluis quam comatis pilos uelli ; mais celui
de "poil" est plus frequent. Differe de capillus en ce que celui-ci
est plutot un collectif, pilus designant au contraire le poil ou le
cheveu pris isolement. Pilus 3’emploie, g<?neralement avec une nega-
tion, comme notre "pas un cheveu; il s'en faut d'un cheveu, etc.",
pour designer une chose de peu d'importance: non facere pili} ne
pilo quidem, etc. - Ancien, usuel. Panroman, M.L.6508. Celt.: iri.
6tZ; bret. arm. palucha "pesseler" de *piluccare ?
Derives et composes: pilS, - 5 s: se couvrir de poils (Afran., Novius),
et "epiler" (Mart.); cf. P.F.325,4: pilat, pilos habere incipit;
alias pro detrahit pilos, a quo depilati (cf. populor et depopulor,
etc.); le second sens seul est demeure dans les 1 . romanes, M.L.C502;
pilUsus, M.L.6505; pilutus ; depilo,-as, M.L.2571; dWpilis) expilor
(?) Lucii, ap.Non.95,15. Cf. encore pilamen, M.L.C499; alipilus, v.ala.
Aucun rapprochement valable. Il n'y a pas de terme indo-europ£en
commun pour cette notion.
pina (pinna), - ae f.: pinne marine (coquillage). Du gr.7tCva, 7Uvva.
Passe en germ.: v.angl. pinewincle.pinguis
pincerna, -ae m.: celui qui mdlange les Tina, i chan son. Mbt vul-
gaire et tardif, sana donte empruntd k gr. TifyxepvtiC (de n ovio et. xer
pavvujii; sar la forne grecque, v. Heraeus, KjL Schr., i»o et s.), servant
k tradnire 1 ’hdbreu maseck, cf. 0 G 1 V 333,36.-
pingd, -is, pinxi, pictun, pingere: broder (avec des fils de dif¬
ferentes conleurs), tatoue*: pingere acu,, Ov., M.6,33; textile stra¬
gulum, magnificis operibus pictum Cic., Tuse.5,31,61; picti Geloni
Vg v G.3,2.15; et "peindre" (sens propre et figurd "colorer, enbellir") :
tabula picta, Cic., Brut. 75, etc., sens conserve dans les 1 . romanes.
Le picti... lacerti de Vg., G. 4,13 r appelle le "ldzard" d'Hd-
=== pilleus
aonies publiques; v. entre autres Vg., Ae.0,665-6. Mot gaulois, coaae
carpentum ?
pllleus (pili eum n.; les foraes avec -II- sont aieux attestdes
que la graphie pileus, cf. Stolz, Bist.gram. I 934), -I a.: 1®bonnet
d'hoame, de caractbre rituel, fait originaireaent' d'une pean de brebis
no n rasde, que portaient les pontifes, les flamines, les'Saliens,
et que l*on donnait anx esciaves en signe d*affraachisseaent; syabole
de la libertd, ddsigne par adtonyaie la libertd elle-meae: seruos
ad pilleum uocare, T.L.34,33; 3 0 coiffe du nouveau-nd. Ancien (Pl.),
usuel. M.L.6504.
Ddrivds: pilleatus,-a,-um’, pilleolus (-lum),-i} pilleolata (Suo);
pillea,-as (b.lat.).
Cf. pila et pilus ? On pense, d*autre part, A gr. 7ttXoC "feutre".
pll 5 , - 5 s: v. pila.
pilum "pilqn": v. pinsa.
pilum, -I n.: javelot. Arae de jet, ancienne en Italie aais d’ori¬
gine contestde; cf. Couissin, Les armes romaines, p.aosqq. A fourni
l*all. Pfeil (v.h.a.£/ii, /ii); en celt.: gall. pi l—wrn "trait".Pilumnus
- 898
Derives: pllSnus: soldat arm^ du javelot, qui combattait au troisieme
rang, triadre; d'ou anteplldnus : soldat des deux premiers rangs;
=== piper entry
47714:piper, -eris n.: poivre; poivrier. Ne seable pas attestd avant
```


## [2026-09-14T01:02:26.573Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '47714,47730p' LAT.txt",
 "description": "Ernout-Meillet piper"
}
```


### [2026-09-14T01:02:26.682Z] TOOL RESULT

```
piper, -eris n.: poivre; poivrier. Ne seable pas attestd avant
Varron. Panroaan. M.L.6531. Gera.: v.b.all .pepar et finn .pippuri’,
celt.: iri .pipur, scibar} britt. pebr.
Ddrivds: piperatus : poivrd; subat.piperatum: poivrade; piperatCriumx
poivrier; piperlnus, attestd dans Isid.iy,10,8 piperinus (scii.
lapis) subalbidus cum punctis nigris, durus atque fortissimus, et
dans la glose corroapue piperina : ciienines, OGL XII 537,31: pdpdrin;
M.L.Csaia; piperacius (lapis Groa.); piperitis ; pipereus (Orib.),
piperoterarium "aoulin k poivre" (Gloss.).pipilo
- 003
Piper est un eaprunt coaaercial, cf. gr. 7ie7iepi qui lui-afeae pro-
rient de l*Orient: le skr. a pippali f."grain de poirre", dont 1 1 l
app arti en drait 4 1 'Inde orientale, tandis que le mot grec et latin
riendrait de l*.Inde de 1 'Ouest ou r est noraal.
plplld, - as, -are; plpld, -Is, -Ire; pIpC, -Ss, -are; plp(p)io,
-Ss, -are: onoaatopdes signi fiant "pdpier, piauler (ce dernier de
piulare, M.L.6551), piailler, glousser"; C&M.L.6533 pipilare (arec t);
```


## [2026-09-14T01:02:32.280Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /tmp && timeout 300 pdftoppm -f 403 -l 403 -r 200 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf /tmp/pg403-p403 && ls -la /tmp/pg403-p403.png",
 "description": "Render PDF page 403"
}
```


### [2026-09-14T01:02:33.998Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 61315 Sep 13 21:02 /tmp/pg403-p403.png
```


## [2026-09-14T01:02:35.830Z] TOOL CALL #72: Read

```json
{
 "file_path": "/tmp/pg403-p403.png"
}
```


### [2026-09-14T01:02:36.347Z] TOOL RESULT

```

```


## [2026-09-14T01:02:36.343Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-14T01:02:49.634Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"pippal\\|pepper\" SYN.txt | head -20",
 "description": "Buck pepper"
}
```


### [2026-09-14T01:02:49.693Z] TOOL RESULT

```
9625:Skt. dsaka- ‘salt’ or ‘pepper’, with usa- ‘salt-pit’, wsana- ‘black Pepper’, usara- ‘salty’, fr. us- ‘burn’ (1.84), Reichelt, op. cit.
9627:5.82 PEPPER
9629:NG awirepe ON’  piparr Lat. piper Dan. pebber It. pepe Sw. peppar Fr. powvre OE pipor Sp. pimienia ME _peper Rum. piper NE pepper Ir. scibar, pipur Du. peper Nir. piobar OHG  pfeffar W. pupur MHG pfeffer Br. pebr NHG pfeffer
9630:1. Nearly all the Eur. words for ‘pep- per’ are fr. Lat. piper, itself a loanword fr. Grk. rémept, this being, like the ar- ticle itself, of Indian orig. Cf. Skt. pippala-, pippali-, ‘berry, pepper’. Schrader, Reallex. 2.164. Boisacq 769. Ernout-M. 771.
9634:Russ. perec Skt.  pippala-, etc. Ay. wietare :
9637:3. Skt. pippala-, etc., above, 1. Also marica-, etym.?
```


## [2026-09-14T01:02:53.440Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SYN.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n'); leaf='\\n'.join(lines[:9627]).count('\\f')\nL=t.split('\\f')\nimport re\nprint('leaf',leaf, re.findall(r'\\b3[0-9]{2}\\b',L[leaf])[:8])\nprint(L[leaf][:400])\nEOF",
 "description": "Buck page for 5.82 PEPPER"
}
```


### [2026-09-14T01:02:54.686Z] TOOL RESULT

```
leaf 428 ['328', '382']
 Br.  Augenn NHG _beere
Although there is a word for ‘berry’ in most of the Eur. languages, it is only in the Gmc. group that the word fuishes a long series of cpds. denoting the special kinds of berry. Thus NE ber- Ty, whence strawberry, raspberry, black- berry, blueberry, cranberra , gooseberry, éle,, formerly also wineberry (OE wein- berige, like Goth. weinabasi), now re- placed by grape, Simil
```


## [2026-09-14T01:03:07.561Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== LKT pfeffer\"; grep -n -i \"pippali\\|filfil\\|fulful\" LKT.txt | head -10; echo \"=== LKT fincan\"; grep -n -i \"findschan\\|fingan\\|fincan\\|pingan\\|pínax\\|pinax\" LKT.txt | head -10",
 "description": "Lokotsch pepper and fincan"
}
```


### [2026-09-14T01:03:07.646Z] TOOL RESULT

```
=== LKT pfeffer
=== LKT fincan
506:ar.  isfänäg,  isfinäg  'Spinat'  [Vielleicht kommen  diese  Formen  selbst  aus  dem Lateinischen,  etwa  spitia  'Dorn'  oder besser  *spinax  SBKAW  Wien  PhhKl CXXXII,  362];  hieraus  zunächst  die  ro- manischen Formen  afrz.  espinoche,  espi- nard;  frz.  epinard,  prov.  espinar,  kat. espinac,  sp.  espinaca,  pg.  espinafre,  it. spinace,  rum.  spanac.  Mit  steter  An- lehnung an  lat.  spina  auch  im  Germa- nischen dtsch.  Spinat,  ndl.  spinazie, engl,  spinage.  Russ.  spinal,  bulg.  spa- nak,  serb.  spanac,  äech.  Spinat,  poln. szpinak.  [Devic  DEt  110/111.  Eguilaz 391.    ML  706.
```


## [2026-09-14T01:03:11.876Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"Pfeffer\" LKT.txt | head -8; echo \"=== HJB pepper\"; grep -n -i \"PEPPER\\b\" HJB.txt | head -8",
 "description": "Lokotsch Pfeffer, Hobson-Jobson pepper"
}
```


### [2026-09-14T01:03:11.953Z] TOOL RESULT

```
986:[Nach  Bürän,  der  Gemahlin  des  Kalifen al-Ma'mün  813 — 833  n.  Chr.]  'eine  Art Speise';  hieraus  sp.  alboronia,  moronia 'Speise  aus  Eieräpfeln,  Kürbis,  Tomaten und  Pfeffer'  [Dicc  Gast  107  a].   [DE  73.
2284:953.  Tk.  jenibahar: 'Spanischer  Pfeffer,  Capsicum  annuum' [aus  ik.jeni  'neu'  vom  Stamme  en,  en, jeü  'klein,  jung,  neu'  Vämbery  TktEtWb S.  32,  Nr.  35 II  und  ar.  lahär  'Gewürz']; hieraus  rum.  enibahar  'Paradieskörner, Piment  zum  Würzen  der  Wurst'.
2325:'Auf  eiserne  Spieße  gesteckte,  stark  ge- pfefferte und  über  einem  Kohlenfeuer gebratene,  kleine  Stücke  Hammelfleisch' [z.  B.  ßi  ugsch,  Reise  nach  Persien  I,  143], tk.  kebab;  hieraus  rum.  chebab  'Brat- fleisch' ;  bulg.  kebap,  serb.  öebab,  klruss. kebab  'am  Bratspieß  gebratenes  Fleisch', russ.  kebab,  kabaw,  kebaf  'gebratenes Fleisch'.  [Gorjajew  1 38.  Bern  SlEtWb  498.
=== HJB pepper
143:The  words  with  which  we  have  to  do,  taking  the  most  extensive  view  of the  field,  are  in  fact  organic  remains  deposited  under  the  various  currents of  external  influence  that  have  washed  the  shores  of  India  during  twenty centuries  and  more.  Rejecting  that  derivation  of  elephant*  which  would connect  it  with  the  Ophir  trade  of  Solomon,  we  find  no  existing  Western term  traceable  to  that  episode  of  communication  ;  but  the  Greek  and  Roman commerce  of  the  later  centuries  has  left  its  fossils  on  both  sides,  testifying to  the  intercourse  that  once  subsisted.  Agallochum,  carba^us,  camphor, sandal,  musk,  nard,  pepper  (Wire/w,  from  Skt.  pippali,  *long  pepper'),  ginger (^tyyi^pis,  see  under  Ginger),  lac,  costus,  opal,  malabathrum  or  folium  indicum, beryl,  sugar  {adjcxap,  from  Skt.  sarkara,  Prak.  saJdcara),  rice  (Upvia,  but  see  s.v.), were  products  or  names,  introduced  from  India  to  the  Greek  and  Roman world,  to  which  may  be  added  a  few  terms  of  a  different  character,  such  as Bpax/taret,  ^apfidyes  {sramanas,  or  Buddhist  ascetics),  ^;Xa  ffayaXLpa  koI  <r<urafi[va (logs  of  teak  and  shisham),  the  ffdyycLpa  (rafts)  of  the  Periplus  (see  Jangar in  Gloss.)  ;  whilst  dindra,  dramma,  perhaps  kastira  (*  tin,'  Kaafflrepos),  kasturl (*musk,'  Koardpiov,  properly  a  different,  though  analogous  animal  product), and  a  very  few  more,  have  remained  in  Indian  literature  as  testimony  to  the same  intercourse.t
1792:corraption  of  a^uaeate  or  ahwbcaU  (see below),  which  appean  to  have  been  the natiTe  name  in  Cential  America)  still sarviying  there.  The  Quichna  name  is paUa^  which  is  used  as  well  as  agucuxUe' Dj  Gieza  de  Leon,  and  also  by  Joseph de  Aoosta.  Grainger  {Suaarcam,  hk. I.)  calls  it  "rich  tabbaea^  which  he says  is  '^the  Indian  name  of  the  avoeatOj ofooeadOy  avigato^  or  as  the  English corraptly  call  it,  aUigaior  fear.  The Spaniaros  in  S.  America  call  it  AquacaJte^ and  under  that  name  it  is  described  by Ulloa."  In  French  it  is  called  avocat. The  praise  which  Qiainger,  as  quoted below,  "liberally  bestows"  on  this fruit,  is,  if  we  might  judge  from  the specimens  occasionally  met  with  in India,  absurd.  With  liberal  pepper and  salt  there  may  be  a  remote  sugges- tion of  marrow :  but  that  is  all. Indeed  it  is  hardly  a  fruit  in  the ordinary  sense.  Its  common  sea  name of  'midshipman's  butter'  [or  'sub- altern's butter  *]  is  suggestive  of  its merits,  or  demerits.
2185:E  1624.—"  And  therewith  they  mix  a  little es  of  sea-shells  and  some  small  pieces  of an  Indian  nut  sufficiently  common,  which they  here  call  Foufel,  and  in  other  places Axeca;  a  very  dry  fruit,  seeming  within like  perfect  wood ;  and  being  of  an  astringent nature  they  hold  it  good  to  strengthen  the Teeth."— A  delia  Voile,  Hak.  Soo.  i.  86. Mr  Grey  says:  "As  to  the  Port,  name, Foujd  or  Fojtl,  the  origin  is  uncertain.  In Sir  J.  Maundeville's  lYavels  it  is  said  that black  pepper  "is  called  Fulful,'*  whioh  is probably  tne  same  word  as  "  i^ou/e/."  But the  Ar.  Faufal  or  F^fdl  is  'betel-nut.*]
2496:1562,—"  800 bahares of  pepper."— Cajte>i- Aedttf  ii.  301.  Correa  writes  bares,  as  does also  Couto.
2498:c.  1569. — "  After  this  I  saw  one  that  would have  g^ven  a  baire  of  Pepper,  which  is  two Quintals  and  a  half e,  for  a  little  Measure  of water,  and  he  could  not  have  it."— (7. Fredericke,  in  ffait,  ii.  858.
2555:1727. — "JSaninjay  is  famous  for  making fU"*^**^l>g.  A  Sauce  made  of  dried  Shrimpe, Cod-pepper,  Salt,  and  a  Sea-weed  or  Graas, all  well  mixed  and  beaten  up  to  the  Con- fdsteocy  of  thick  Mustard." — A,  ffamiKorif ii.  194.  The  same  author,  in  speaking  of Pegu,  calls  the  like  sauce  Proci  (44),  which was  probably  the  Talain  name.  It  appears also  in  Sonnerat  under  the  form  Prox (ii.  305).
2562:c.  1562.— "All  these  thinj^s  were  brought by  the  Moors,  who  traded  in  pepper  which they  brouffht  from  the  hills  where  it  grew, by  land  m  Bisnega,  and  Bala«ate,  and dambay.  "—Oorreo,  ed.  Ld.  Stanley,  Hak. Soc.  p.  344.
2836:1813.— "The  East  India  Company  for seventy  years  had  a  large  hanlhiaijil,  or warehouse,  at  Mirzee,  for  the  reception  of the  pepper  and  sandalwood  purchased  in the  dominions  of  the  Mysore  Rajah." — Forbea,  Or.  Mem,  iv.  109.
```


## [2026-09-14T01:03:22.607Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AFA\"; grep -n -i \"pilpel\\|filfil\\|Pfeffer\" AFA.txt | head -10; echo \"=== FVQ\"; grep -n -i \"filfil\\|pippal\" FVQ.txt | head -5; echo \"=== TAD\"; grep -n \"فنجان\\|فلفل\" TAD_pages.txt | head -8",
 "description": "Fraenkel, Jeffery, Unaysi"
}
```


### [2026-09-14T01:03:22.714Z] TOOL RESULT

```
=== AFA
5708:spricht von gepfeffertem Weine f (i*Äj) ; Becher , die ge-
5853:läuder (vgl. Low Aram. Pfianz. 319) Pfeffer an Wein163
=== FVQ
=== TAD
2040: ‫فلفل‪ -‬لنظ هنديحيث منشأ هذا البات الذيحبه شديد الحراقة اوسفيفاة‬
2057:              ‫فنجان ‪ -‬فارسي « فنجان وبتكان » وهو قدح صغير من خزف‬
```


## [2026-09-14T01:04:18.218Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && grep -n -i \"pilleus\\|pīlo\\|pilo-\\|pьlstь\\|plъstь\" WLD_Bd2_pages.txt | head -10; echo \"=== search page 71\"; grep -n \"\\[pdf page\" WLD_Bd2_pages.txt | head -3",
 "description": "Walde-Pokorny Bd2 p71"
}
```


### [2026-09-14T01:04:18.320Z] TOOL RESULT

```
3865:Wollmasse‘'; aber abg. phsih ds. zu 7u?.og, pilleus, s. J. Schmidt KZ. 32,
4745:pilo- „TIaar% es-St. *piles-
4751:TtiXog „Filz‘‘ {7iiXi(D             .jfilze, presse Z8.“), lat. pilleus, -etmi „Filzkappe, Filz-
5564:— Lat. pilus           8.   u.   *pilo- „Haar“.
=== search page 71
```


## [2026-09-14T01:04:21.242Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && sed -n '4740,4775p' WLD_Bd2_pages.txt",
 "description": "WLD pilo- entry text"
}
```


### [2026-09-14T01:04:21.303Z] TOOL RESULT

```
Brett, Schreibtafel, Gremalde“; abg. ptnh m. „Bauinstamin, -strunk". Fick
1* 83, 48^; Perssons Beitr. 410 a 3 weitere Ankniipfung an spei „spitz,
spitzes Holzstiick^ ist unwabrscheinlich.


pilo- „TIaar% es-St. *piles-
    Lat. p^liis „Haar“,               wovon wohl als Kollektiv „*Haarknauer' auch pila
„Ball, Ballen'^        (s. Yf.       LEWb.^ s. v.); ob dazu, im ^1. und der Bed. durch
Tiregov     beeinfluBt,          auch      gr. nxlXov „Peder, Plaumfeder“? (s. u. pet- „auf
etwas lossturzen^)              ;
                                     auf einem -es-St. beruht *pil-s-6s „verfilzt“, in gr.
TtiXog „Filz‘‘ {7iiXi(D             .jfilze, presse Z8.“), lat. pilleus, -etmi „Filzkappe, Filz-

mutze“       (so,    nicht pileus,auch nach dem Romanischen, s. Meyer-Liibke
KZ. 33, 308 f.),        abg. phsh „Filz“. J. Schmidt KZ. 32, 387 f., s. auch Yf.
LEWb.2 s. V.; dt. Filz s. u. pel- „sto6en'^

po(i):pT und (von po aus) po „trinken“. Langdiphthongische Wz. nach
    Schulze KZ. 27, 420 f. Praes. *pi-po-mi (oder wohl *pi-l)omi), pi-po’
    me, themat. *pi-h6, wobei h nach Thumeysen lA. 22, 65, Hdb. 138 wohl
    der im Inlaut erhaltene urspriingliche Wz. kons. ist, der im Anlaut
    durch friihidg. Anlautwandel zu p verhartet wurde; vgl. auch Brug-
       mann IP 3, 37.
   Themat, Praes. ai. pibati „trinkt“, lat. bibo, -ere, air. ib- ds. (z. B. 3. sg. ni ib
„er trinkt nicht“, ibid 2. pi. Imp, „trinketl“), acymr. iben „bibimus“, corn.
evaf „bibo“, bret. emjf. Unthemat. ai. pi-p-ate 3. pL, pi-p-Clna-, pi-pana-
Ptc., apiplta (: nuit-oxco, falisk. pipafo „ich werde trinken“ (wohl mit -d-,
wie lat. dd-bo, trotz GL 5, 317; vgl. auch pf. med. gr. 7tmoTai)\ si.pd-ti
,,trinkt“,pay-dyati „gibt zu trinken, trankt“, pdyaie „trankt“ (: abg. pojq,
air.        ai,     „getrunken, getrunken habend"' (abl. gr. jrdrog „Trank“,
lat. pdtus „getrunken habend“, vgl. auch potus „Trank“, lit. puta „Zechge-

lage“, pUi-h „Trunk‘‘ (= abg. piti Inf. „trinken“; abl. gr. nooig „Trunk, das
Trinken‘‘,  und ajujicong „Ebbe“, lat. poti-o das Trinken“); ai. patave inf.
„zu trinken^ (= apr. poutivei ) patar-, pdtdr- „der TrinkeF‘ = lat. potor ds.
                                              ;
```


## [2026-09-14T01:04:29.492Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && sed -n '4728,4744p' WLD_Bd2_pages.txt",
 "description": "WLD pin- entry"
}
```


### [2026-09-14T01:04:29.551Z] TOOL RESULT

```
Vf. LEWb.^ u. pipilo (s. auch plpinna), Iljinski KZ. 43, 179.
   Cech. pikati „piepen“, russ. pikath ds., piJcb „das Piepen wilder Jfest-
linge“ u. dgl.
   Aksl. piskati usw. „pfeifen'‘ (ob dazu ai, picchora „Pfeife, Flote^- ? Zu-
baty KZ. 31, 13 zw.).
   Bulg. pile, skr. pile „Kuchlein“ u. dgl.     Iljinskij aaO, (wo auch lat.
pica, picus usw. yerglichen werden, s. u. *sp1qo- „Specht'').
                                                   pin    — pD(i)                                   71


pin „Hokstuck“.
   Ai. pinaka-m „Stab, Stock, Keule“; gv. mvai, -axo? „Sparre, Balken,
Brett, Schreibtafel, Gremalde“; abg. ptnh m. „Bauinstamin, -strunk". Fick
1* 83, 48^; Perssons Beitr. 410 a 3 weitere Ankniipfung an spei „spitz,
spitzes Holzstiick^ ist unwabrscheinlich.
```


## [2026-09-14T01:04:41.451Z] TOOL CALL #81: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/pg403-p403.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/403.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/403.png; cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n -i -m6 \"plank\\|Etymology\\b\" 3cc14fab85bd323e.txt | head; sed -n '150,175p' 3cc14fab85bd323e.txt",
 "description": "copy page png and check pinax wiktionary"
}
```


### [2026-09-14T01:04:42.475Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 61315 Sep 13 21:04 /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/403.png
62: Etymology 
154: Etymology
179: board ; plank 

 Ancient Greek
 [ edit ] 

 Etymology
 [ edit ] 

 Since Fick (1890), considered a native word of Proto-Indo-European origin, cognate with Sanskrit पिना॑क ( pínāka , “ staff; stick ” ) and Proto-Slavic *pь̏ňь (whence Old Church Slavonic пьнь ( pĭnĭ ) , Russian пень ( penʹ , “ trunk; stub ” ) ). On the other hand, Beekes inevitably prefers a Pre-Greek origin, though allows that the Slavic terms may be cognate. [ 1 ] 

 Pronunciation
 [ edit ] 

 IPA ( key ) : /pí.naks/ → /ˈpi.naks/ → /ˈpi.naks/ 

 ( 5 th BCE Attic ) IPA ( key ) : /pí.naks/ 

 ( 1 st CE Egyptian ) IPA ( key ) : /ˈpi.naks/ 

 ( 4 th CE Koine ) IPA ( key ) : /ˈpi.naks/ 

 ( 10 th CE Byzantine ) IPA ( key ) : /ˈpi.naks/ 

 ( 15 th CE Constantinopolitan ) IPA ( key ) : /ˈpi.naks/ 

 Noun
 [ edit ]
```


## [2026-09-14T01:05:07.382Z] AGENT

Now I'll write the verification file.


## [2026-09-14T01:11:59.460Z] TOOL CALL #82: Bash

```json
{
 "command": "cat > /home/sfmqrb/git/rishe/data/verification/page-403.json <<'JSONEOF'\n{\n  \"pdf_page\": 403,\n  \"book_page\": 373,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-13\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Pilo, Pislos\",\n      \"verdict\": \"plausible\",\n      \"modern_form\": \"PIE *pilo- 'hair' (Lat. pilus) beside an -es-stem derivative *pil-s-o- 'felted' (Gk. πῖλος, Lat. pilleus, OCS plъstь); modern handbooks no longer join the two\",\n      \"note\": \"Both names Nourai prints are genuine reconstructions and are cited correctly. Pokorny IEW 830 has 'pi-lo- Meaning: hair, felt', with Lat. pilus, Gk. πῖλος, Lat. pilleus (< *pilseio-) and OCS plъstь; Walde-Pokorny II 71 spells out the second stem as *pil-s-os 'verfilzt', which is Nourai's 'Pislos', and Mann IEC 940 heads an entry 'pislos, om, ā \\\"hair, fibre\\\"'. Watkins (AHD app.) prints 'pilo-. Hair. A possible root' — the hedge is his. What is no longer accepted is the unity of the group: Ernout-Meillet s.v. pilus already wrote 'Aucun rapprochement valable. Il n'y a pas de terme indo-européen commun pour cette notion', and de Vaan/Beekes (followed by Wiktionary) separate Lat. pilus 'hair' (etymology unknown) from Gk. πῖλος / Lat. pilleus / OCS plъstь 'felt', which belong to the 'beat, full (cloth)' root *pel- (Pok. 801 pel-2a) — a link Pokorny himself flagged in his note and WP II 71 ('dt. Filz s. u. pel- \\\"stoßen\\\"'). So the box is right as a report of POK/AHD/IEC but its single gloss 'hair' over-unifies two etyma.\",\n      \"note_fa\": \"ریشهٔ «Pilo / Pislos» در کتاب دقیقاً برگرفته از پوکورنی (ص ۸۳۰) و والده‑پوکورنی (ج۲ ص ۷۱) است: *pilo- «مو» و ستاکِ گسترشیافتهٔ *pil-s-o- «نمدشده» که در یونانی pîlos «نمد»، لاتینی pilleus «کلاه نمدی» و اسلاوی کهن plъstь «نمد» بازتاب یافته است؛ مان (IEC ص ۹۴۰) نیز مدخل pislos «مو، لیف» را دارد. اما ریشه‌شناسی امروزی این خانواده را یکپارچه نمی‌داند: ارنو‑مه‌یه دربارهٔ pilus لاتینی می‌نویسد «هیچ قیاس معتبری در کار نیست»، و بیکس و دخان (و ویکی‌واژه) واژه‌های «نمد» را به ریشهٔ *pel- «کوبیدن، نمد مالیدن» می‌برند نه به ریشه‌ای به معنی «مو». بنابراین نقل نورایی از منابعش درست است ولی معنیِ یگانهٔ «مو» برای هر دو ستاک با پژوهش امروزی همخوان نیست؛ ادعا با احتیاط پذیرفتنی است.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/pilus\",\n        \"https://en.wiktionary.org/wiki/%CF%80%E1%BF%96%CE%BB%CE%BF%CF%82\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:830\", \"status\": \"supports\", \"note\": \"Pokorny IEW p. 830 (POK_full.txt, 'Page(s): 830'): 'Root / lemma: pi-lo- ; Meaning: hair, felt … Latin pilus m. \\\"hair\\\" … gr. πῖλος m. \\\"felt\\\", Latin pilleus \\\"Filzkappe\\\" (*pilseio-); Old Church Slavic plъstь \\\"felt\\\". References: WP. II 71, WH. II 302 f.' — exactly the root, label and gloss of Nourai's box.\"},\n        {\"ref\": \"IEC:940\", \"status\": \"supports\", \"note\": \"Mann, IEC p. 940 (IEC.txt leaf 522, running header 'pípét- — pislom, ā', page number 940 printed on the leaf): 'pislos, om, à \\\"hair, fibre\\\" Per. pile \\\"cocoon\\\"; Gk. pilos, m. \\\"hair, wool, felt\\\" … (Short -i- in Lat. pilus, m. \\\"hair\\\" unaccountable)'. This single entry is the source of Nourai's root name 'Pislos', of his Persian node and of his Greek node.\"},\n        {\"ref\": \"IEC:1650\", \"status\": \"not_found\", \"note\": \"Our OCR of Mann breaks off at printed p. 1554 (u-words; leaf 845). p. 1650 falls in the Supplement/Corrigenda of the last fascicle (1573-1684), which is not in the scan; grep of the whole file for 'pisl', 'pile ‘cocoon' returns only the p. 940 entry. Could not verify the second page reference.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"POK\", \"where\": \"IEW p. 830, s.v. pi-lo-\", \"stance\": \"supports\", \"note\": \"'Meaning: hair, felt … auf einem -es-Stamm beruhend *pil-s-os \\\"verfilzt\\\", in gr. πῖλος'; Pokorny's own Note already derives pi-lo- from 'pel-2a, pelə- : plā- to cause to move, drive, felt'.\"},\n        {\"src\": \"WLD\", \"where\": \"Bd. II 71 (WLD_Bd2_pages.txt l. 4745-4752, running header 'pin — pō(i) 71')\", \"stance\": \"supports\", \"note\": \"'pilo- „Haar“, es-St. *piles- … auf einem -es-St. beruht *pil-s-6s „verfilzt“, in gr. πῖλος „Filz“ …, lat. pilleus … abg. plъstь „Filz“ … dt. Filz s. u. pel- „stoßen“' — the form *pil-s-os is literally Nourai's 'Pislos'.\"},\n        {\"src\": \"AHD\", \"where\": \"Watkins appendix s.v. pilo- (AHD_watkins1985.txt l. 853)\", \"stance\": \"partial\", \"note\": \"'pilo-. Hair. A possible root. 1. Latin pilus, hair … 2. Suffixed reduced form *pil-so- possibly in: a. Latin pilleus, pileus, felt cap …; b. Greek pilos, felt … [Pok. pi-lo- 830.]' — same content, but Watkins twice hedges ('A possible root', 'possibly').\"},\n        {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. pilus (LAT.txt l. 47541-47557)\", \"stance\": \"contradicts\", \"note\": \"'pilus, -i m.: poil, cheveu … Aucun rapprochement valable. Il n'y a pas de terme indo-européen commun pour cette notion.' Under pilleus (l. 47498): 'Cf. pila et pilus ? On pense, d'autre part, à gr. πῖλος \\\"feutre\\\"' — i.e. hesitant.\"},\n        {\"src\": \"IEC\", \"where\": \"p. 940 s.v. pislos\", \"stance\": \"supports\", \"note\": \"see ref_check; Mann is the only book that puts Persian pīle in this family.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Persian\",\n          \"words\": \"pîleh «پیله» : cocoon\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"NP پیله pīla/pīle 'silk cocoon' is a real and old word (Asadi's Loghat-e Fors, Dehkhoda quotes 'Onsori, Naser Khosrow, Sana'i, Sa'di, and Mas'ud Sa'd Salman's line that Nourai prints). The IE affiliation, however, rests on one source only: Mann IEC 940 lists 'Per. pile \\\"cocoon\\\"' first under *pislos 'hair, fibre', beside Gk. pilos 'hair, wool, felt', MHG viseln 'fibres', Du. vezel 'fibre' — the semantics being 'filament, fibre' > 'the filament-case the silkworm spins'. No Old or Middle Iranian antecedent is attested (no *pi(s)la- in Bartholomae, MacKenzie or Nyberg), and no reflex of *-sl- > NP -l- can be demonstrated for it; Horn and Hübschmann do not treat the word at all, and Dehkhoda and Mo'in give the meaning and the by-forms (بیله، پله، فیله، فیلق) without any etymology. Since فیلق is itself Arabic fīlaq 'cocoon' (from Greek), a loan history for the whole group cannot be excluded. Accepted as possible, not proven.\",\n          \"derivation_fa\": \"«پیله» به معنی پیلهٔ کرم ابریشم واژه‌ای کهن در فارسی دری است (اسدی در لغت فرس، و بیت مسعود سعد سلمان که نورایی آورده). پیوند آن با هندواروپایی تنها از یک منبع می‌آید: مان (IEC ص ۹۴۰) آن را ذیل ستاک *pislos «مو، لیف» در کنار pîlos یونانی و vezel هلندی «لیف» می‌نهد، با تحول معنایی «رشته/لیف» ← «تنیدهٔ کرم ابریشم». اما هیچ صورت ایرانی باستان یا فارسی میانه‌ای برای آن گواهی نشده (در بارتولومه، مکنزی و نیبرگ نیست)، هرن و هوبشمان هم به آن نپرداخته‌اند، و دهخدا و معین تنها معنی و گونه‌های «بیله، پله، فیله، فیلق» را می‌آورند بی هیچ ریشه‌شناسی؛ وانگهی «فیلق» خود عربیِ برگرفته از یونانی است. پس ادعای نورایی با احتیاط پذیرفتنی است و اثبات‌شده نیست.\",\n          \"sources\": [\"https://abadis.ir/fatofa/%D9%BE%DB%8C%D9%84%D9%87/\"],\n          \"ref_check\": [\n            {\"ref\": \"IEC:940\", \"status\": \"supports\", \"note\": \"IEC.txt l. 12937 (leaf 522 = printed p. 940): 'pislos, om, à \\\"hair, fibre\\\" Per. pile \\\"cocoon\\\"; Gk. pilos, m. \\\"hair, wool, felt\\\" …' — the arrow is exactly Mann's.\"},\n            {\"ref\": \"IEC:1650\", \"status\": \"not_found\", \"note\": \"printed p. 1650 lies in Mann's Supplement, beyond the end of the local OCR (last printed page 1554); no second entry for pile could be located.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"Farhang-e Farsi s.v. پیله (MON_part1.txt l. 35603)\", \"stance\": \"partial\", \"note\": \"'پیله [= بیله = پله = فیله = فیلجه = فیلق] (اِ) محفظه‌ای که نوزاد برخی حشرات دور خود می‌تند …' — the word and the sense are confirmed, but Mo'in gives no origin tag at all.\"},\n            {\"src\": \"BQT\", \"where\": \"Dehkhoda/Borhan, via abadis.ir s.v. پیله\", \"stance\": \"partial\", \"note\": \"'پیله. [ ل َ / ل ِ ] (اِ) محفظه ابریشمین کرم ابریشم … اصل ابریشم و غوزه ابریشم که کرم تنیده باشد. (برهان)' and the very line Nourai quotes, 'کرم پیله همی بخود بتند'; no etymology offered.\"},\n            {\"src\": \"HRN\", \"where\": \"Grundriss der neupersischen Etymologie — grep 'pīl', 'pîl', 'Cocon' in HRN.txt\", \"stance\": \"silent\", \"note\": \"no entry; Horn does not treat پیله.\"},\n            {\"src\": \"HUB\", \"where\": \"Persische Studien — same greps in HUB.txt\", \"stance\": \"silent\", \"note\": \"no entry.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Latin\",\n          \"words\": \"pilus : hair ; pileus : felt cap\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Both words are real Latin: pilus, -ī m. 'a (single) hair', opposed to the collective capillus (Ernout-Meillet), and pilleus/pileus, -ī m. 'the conical felt cap' worn by the flamines and given to a freed slave (hence servos ad pilleum vocare, Livy 34.33). Nourai's arrow puts both under one 'hair' root, which is the traditional handbook analysis (WP II 71: pilus < *pilo-, pilleus < *pil-s-eio-, i.e. 'made of felt'); the -ll- of the better-attested pilleus is what forces the *-ls- reconstruction. Modern Latin etymology detaches pilus (Ernout-Meillet: 'Aucun rapprochement valable'; de Vaan: no IE etymology) and keeps pilleus with Greek πῖλος in the 'felt' group, so the joint derivation drawn here is the older view, not the current one.\",\n          \"derivation_fa\": \"هر دو واژه لاتینیِ اصیل‌اند: pilus «تارِ مو» (در برابر capillus که جمعی است) و pilleus/pileus «کلاه نمدیِ مخروطی» که کاهنان رومی بر سر می‌گذاشتند و به بردهٔ آزادشده می‌دادند. نورایی هر دو را زیر یک ریشه به معنی «مو» می‌آورد که همان تحلیل سنتی والده‑پوکورنی است (pilus < *pilo-، pilleus < *pil-s-eio- یعنی «نمدین»)؛ دوگانگی لام در pilleus همان دلیلِ بازسازیِ *-ls- است. اما در پژوهش امروزی pilus را جدا و بی‌ریشهٔ شناخته می‌دانند (ارنو‑مه‌یه: «هیچ قیاس معتبری نیست») و pilleus را با pîlos یونانی در گروه «نمد» می‌نهند. پس این پیکان دیدگاه کهن‌تر را بازمی‌تاباند.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/pilus\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD:1535\", \"status\": \"supports\", \"note\": \"Watkins's appendix entry pilo- (local 1985 ed., l. 853) has '1. Latin pilus, hair … 2. … a. Latin pilleus, pileus, felt cap'; the 1975 New College appendix runs pp. 1505-1550, so a p-root at 1535 is the same entry (our local copy is the 1985 standalone reprint and repaginates).\"},\n            {\"ref\": \"IEC:1650\", \"status\": \"not_found\", \"note\": \"beyond the local OCR (see entry-level note); Mann's remark on Latin pilus is on p. 940: '(Short -i- in Lat. pilus, m. \\\"hair\\\" unaccountable)' — a caveat Nourai does not report.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"LAT\", \"where\": \"Ernout-Meillet, s.v. pilus and pilleus\", \"stance\": \"contradicts\", \"note\": \"pilus: 'Aucun rapprochement valable…'; pilleus: 'les formes avec -ll- sont mieux attestées que la graphie pileus … Cf. pila et pilus ? On pense, d'autre part, à gr. πῖλος \\\"feutre\\\".'\"},\n            {\"src\": \"KLN\", \"where\": \"Klein 1966 p. 1155 s.v. pile 'soft, fine hair' (KLN_1966.txt l. 28820)\", \"stance\": \"supports\", \"note\": \"'fr. L. pilus, \\\"hair\\\", rel. to pila … prob. also to pilleus, \\\"a felt cap\\\", and cogn. with Gk. πῖλος, \\\"felt\\\"' — Klein still joins them, as Nourai does.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. II 71\", \"stance\": \"supports\", \"note\": \"'lat. pilleus, -eum „Filzkappe, Filzmütze“ (*pilseio-)'.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"English\",\n          \"words\": \"pile, pluck, plush, caterpillar, pillage\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Four of the five are securely Latin pilus-words. PILE (n.3) 'soft fine hair, nap': ME pile from Anglo-French pyle / MDu. pijl < L. pilus (Etymonline notes the phonology rules out transmission through OFr. peil/poil). CATERPILLAR: mid-15c. catyrpel, from Old North French catepelose (OFr. chatepelose) 'shaggy cat' < Late Latin catta pilosa, pilosus < pilus — the English ending being reshaped after ME piller 'plunderer' (so Klein p. 1155 and Etymonline agree). PLUSH: 1590s from Fr. pluche < peluche < OFr. peluchier < VL *piluccare 'to pull the hair off' (the last stage of weaving plush). PILLAGE: late 14c. from OFr. pilage < pillier, from VL *piliare, 'probably a figurative use of Latin pilare \\\"to strip of hair\\\"' — note that Watkins instead files PILLAGE under pilleus 'felt cap', so the two standard sources route it differently within the same family. PLUCK is the weak member: the derivation of OE pluccian / West Gmc *plokken from VL *piluccare is 'perhaps' only, and the OED (cited by Etymonline) 'finds difficulties with this and cites gaps in historical evidence'. Hence plausible rather than confirmed for the node as a whole.\",\n          \"derivation_fa\": \"چهار واژه از پنج واژه به‌روشنی از pilus لاتینی‌اند: pile «پرز، کرک» از انگلیسی میانه، از انگلوفرانسوی pyle یا هلندی میانه pijl؛ caterpillar «کرم پروانه» از فرانسویِ شمالی کهن catepelose < لاتینی متأخر catta pilosa «گربهٔ پشمالو» (pilosus از pilus) که پایانه‌اش در انگلیسی به قیاسِ piller «غارتگر» دگرگون شده است؛ plush «مخمل پرزدار» از فرانسوی pluche < peluche < peluchier < لاتینی عامیانه *piluccare «مو کندن»؛ و pillage «غارت» از فرانسوی کهن pilage از pillier، به‌گمانِ اتیمولوژیست‌ها از کاربرد مجازیِ pilare «موکندن، پوست‌کندن» — هرچند واتکینز آن را ذیل pilleus «کلاه نمدی» می‌آورد. حلقهٔ سست، pluck است: پیوند pluccian انگلیسی کهن با *piluccare تنها «شاید» است و فرهنگ آکسفورد آن را دشوار و بی‌گواهِ تاریخی می‌داند. از این رو حکم این گره «با احتیاط پذیرفتنی» است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/caterpillar\",\n            \"https://www.etymonline.com/word/pillage\",\n            \"https://www.etymonline.com/word/plush\",\n            \"https://www.etymonline.com/word/pluck\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins s.v. pilo- (AHD_watkins1985.txt l. 853): '1. Latin pilus, hair: PELAGE, PILAR, PILE, PILOSE, PILUS, PLUCK, PLUSH, POILU; CATERPILLAR, DEPILATE. 2. … a. Latin pilleus, pileus, felt cap: PILEUS, PILLAGE' — all five of Nourai's English words are there, though PILLAGE hangs from pilleus rather than pilus.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein 1966 p. 1155 s.v. pile ('soft, fine hair') and p. 258 s.v. caterpillar (KLN_1966.txt l. 28820, 6796)\", \"stance\": \"supports\", \"note\": \"under pile: 'Cp. depilate, peel … pill, \\\"to rob; to peel\\\" … pluck, plush, poilu, and the second element in caryopilite, caterpillar, horripilate'; s.v. caterpillar: 'ONF. catepelose … fr. Late L. catta pilosa, \\\"hairy cat\\\" … L. pilosa is fem. of pilosus, \\\"hairy\\\", fr. pilus'.\"},\n            {\"src\": \"FSD/WEB\", \"where\": \"Funk & Wagnalls and Webster vol. 1 — grep 'pilocarp', 'pilose' in FSD_vol1-4.txt, WEB_vol1.txt\", \"stance\": \"silent\", \"note\": \"the relevant alphabet stretch is not in the volumes we hold (vol. 1 of Webster only, and the F&W OCR has no hit), so no independent confirmation from them.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Greek\",\n          \"words\": \"pilos : felt\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Gk. πῖλος (pîlos) m. 'wool or hair wrought into felt; felt cap' is real and correctly glossed, and every handbook Nourai cites puts it here: Pokorny 830 derives it from the -es-stem *pil-s-os (πιλέω 'to felt, press together'), WP II 71 the same, Watkins '*pil-so- … b. Greek pilos, felt', Mann IEC 940 lists it under pislos beside Persian pile. Formally, therefore, Nourai's 'Pislos' is exactly the right preform for πῖλος. What is not current is the label 'hair': Beekes and Wiktionary keep πῖλος with Proto-Slavic *pьlstь 'felt' and OE felt (i.e. the root *pel- 'to beat, full cloth') and state flatly that 'a connection with Latin pilus \\\"a hair\\\" and pila \\\"a ball\\\" has been abandoned'. The arrow is thus right in form, wrong in the semantic head it hangs from.\",\n          \"derivation_fa\": \"πῖλος یونانی «نمد، کلاه نمدی» واژه‌ای واقعی و درست معنی‌شده است و همهٔ منابعِ خودِ نورایی آن را همین‌جا می‌نهند: پوکورنی (ص ۸۳۰) و والده‑پوکورنی (ج۲ ص۷۱) آن را از ستاکِ *pil-s-os می‌گیرند (قیاس کنید با فعل πιλέω «نمد مالیدن»)، واتکینز نیز «*pil-so- … یونانی pilos، نمد». پس صورتِ «Pislos» دقیقاً پیش‌صورتِ درستِ این واژه است. آنچه امروز پذیرفته نیست برچسبِ معناییِ «مو» است: بیکس و ویکی‌واژه πῖλος را با *pьlstь اسلاوی و felt انگلیسی کهن هم‌ریشه و از ریشهٔ *pel- «کوبیدن، نمد مالیدن» می‌دانند و پیوند آن را با pilus لاتینی «رهاشده» می‌خوانند. یعنی پیکان از نظر آوایی درست و از نظر معنایی نادرست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%CF%80%E1%BF%96%CE%BB%CE%BF%CF%82\"],\n          \"ref_check\": [\n            {\"ref\": \"IEC:1650\", \"status\": \"not_found\", \"note\": \"not in the local OCR (ends at p. 1554); the relevant Mann entry is on p. 940: 'pislos … Gk. pilos, m. \\\"hair, wool, felt\\\"'.\"},\n            {\"ref\": \"AHD:1535\", \"status\": \"supports\", \"note\": \"Watkins s.v. pilo-: '2. Suffixed reduced form *pil-so- possibly in … b. Greek pilos, felt: PILOCARPINE.'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"IEW 830\", \"stance\": \"supports\", \"note\": \"'auf an -s-stem based on *pil-s-os \\\"verfilzt\\\", in gr. πῖλος m. \\\"felt\\\", πιλέω \\\"filze, presse zs.\\\"'.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. II 71\", \"stance\": \"supports\", \"note\": \"'*pil-s-6s „verfilzt“, in gr. πῖλος „Filz“ … abg. plъstь „Filz“ … dt. Filz s. u. pel- „stoßen“'.\"},\n            {\"src\": \"KLN\", \"where\": \"Klein 1966 p. 1155 s.v. pile\", \"stance\": \"supports\", \"note\": \"'cogn. with Gk. πῖλος, \\\"felt\\\"'.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"English\",\n          \"words\": \"pilocarpine\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Pilocarpine is the alkaloid isolated in 1875 from jaborandi, the leaves of the South-American shrub genus Pilocarpus (Rutaceae); the genus name is Modern Latin, coined from Gk. πῖλος 'felt' + καρπός 'fruit' (from the fruit's felted/cap-like appearance), and the drug name is that genus plus the chemical suffix -ine. Klein states it in so many words, and the route Greek πῖλος > ModL. scientific coinage > English is not a sound-change chain but an 18th/19th-c. learned formation, which is exactly how the chart draws it (Greek → English).\",\n          \"derivation_fa\": \"«پیلوکارپین» نامِ شبه‌قلیایی است که در ۱۸۷۵ از گیاه ژابوراندی، از سردهٔ Pilocarpus (تیرهٔ سدابیان) در امریکای جنوبی جدا شد. نام سرده لاتینیِ نو و ساخته‌شده از pîlos یونانی «نمد» و karpós «میوه» است (به سببِ ظاهرِ نمدیِ میوه)، و نام دارو همان نام سرده به‌علاوهٔ پسوندِ شیمیاییِ ‎-ine. پس این پیکان نه تحول آوایی بلکه واژه‌سازیِ دانشورانهٔ سدهٔ نوزدهم است و همان‌گونه که نمودار نشان می‌دهد از یونانی به انگلیسی می‌رسد. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%CF%80%E1%BF%96%CE%BB%CE%BF%CF%82\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins s.v. pilo-, branch 2b: 'Greek pilos, felt: PILOCARPINE.'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein 1971 one-vol. ed., s.v. pilocarpine / Pilocarpus (KLN_1971.txt l. 182605-182609)\", \"stance\": \"supports\", \"note\": \"'pilocarpine, pilocarpin, n., an alkaloid … — See next word and chem. suff. -ine' ; 'Pilocarpus, n., a genus of shrubs of the rue family (bot.) — ModL., compounded of Gk. πῖλος, \\\"felt\\\", and καρπός, \\\"fruit\\\". See pile, \\\"hair\\\", and carpel.'\"},\n            {\"src\": \"KLN\", \"where\": \"Klein 1966, s.v. jaborandi (KLN_1966.txt l. 20107)\", \"stance\": \"supports\", \"note\": \"'jaborandi, n., the dried leaflets of S. American shrubs of the genus Pilocarpus. — Port., fr. Tupi yaborandi' — confirms the plant behind the drug name.\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 1,\n      \"root\": \"Pin\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *pin- 'a piece of wood, stick, board' (Pok. 830)\",\n      \"note\": \"Pokorny IEW 830 has 'Root / lemma: pi-n- ; Meaning: a piece of wood', with Old Indic pínāka-m 'staff, stick, club', Gk. πίναξ, -ακος 'rafter, beam, board, writing tablet, painting', OHG witu-pin, MLG vīne 'woodpile', OCS pьnь m. and Serbian panj 'tree trunk, stump' — Nourai's gloss 'wood, tree stump' simply merges Pokorny's meaning with the Slavic sense. Walde-Pokorny II 71 has the identical entry under the running head 'pin — pō(i) 71', and Buck §5.32 (p. 345) gives the same comparison. The one modern reservation concerns the Greek member: Beekes prefers a Pre-Greek origin for πίναξ while allowing that the Slavic words may be cognate.\",\n      \"note_fa\": \"ریشهٔ *pin- «تکه‌چوب» در پوکورنی ص ۸۳۰ آمده است: سنسکریت pínāka- «چوب‌دست، گرز»، یونانی πίναξ «تخته، لوح نوشتن، تابلو»، آلمانی علیای کهن witu-pin، اسلاوی کهن pьnь و صربی panj «تنه و کندهٔ درخت». معنیِ «چوب، کندهٔ درخت» که نورایی می‌دهد آمیزه‌ای است از معنیِ پوکورنی و معنیِ شاخهٔ اسلاوی؛ والده‑پوکورنی (ج۲ ص۷۱) و باک (ص ۳۴۵) نیز همین قیاس را دارند. تنها تردید امروزی دربارهٔ عضو یونانی است: بیکس πίναξ را واژه‌ای پیش‑یونانی می‌شمارد هرچند هم‌ریشگی صورت‌های اسلاوی را ناممکن نمی‌داند. روی‌هم‌رفته ادعای نورایی درست است.\",\n      \"sources\": [\"https://en.wiktionary.org/wiki/%CF%80%CE%AF%CE%BD%CE%B1%CE%BE\"],\n      \"ref_check\": [\n        {\"ref\": \"POK:830\", \"status\": \"supports\", \"note\": \"POK_full.txt, 'Root / lemma: pi-n- ; Meaning: a piece of wood ; Material: Old Indic pinaka-m \\\"staff, stick, club\\\"; gr. πίναξ, -ακος \\\"Sparre, Balken, Brett, Schreibtafel, Gemälde\\\"; … abg. pьnь m., serb. panj \\\"tree trunk, -strunk\\\". References: WP. II 71 … Page(s): 830'.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"WLD\", \"where\": \"Bd. II 71 (WLD_Bd2_pages.txt l. 4737-4743)\", \"stance\": \"supports\", \"note\": \"'pin „Holzstück“. Ai. pinaka-m „Stab, Stock, Keule“; gr. πίναξ, -ακος „Sparre, Balken, Brett, Schreibtafel, Gemälde“; abg. pьnь m. „Baumstamm, -strunk“.'\"},\n        {\"src\": \"SYN\", \"where\": \"Buck, p. 345, §5.32 PLATE (SYN.txt l. 8735, leaf 388)\", \"stance\": \"supports\", \"note\": \"'1. Grk. πίναξ \\\"board, plank, tablet\\\" and \\\"platter\\\" : Skt. pinaka- \\\"staff\\\", ChSl. pьnь, Russ. pen', etc. \\\"tree-trunk\\\" or \\\"stump\\\", Walde-P. 2.71.'\"},\n        {\"src\": \"IEC\", \"where\": \"Mann, p. 938 s.v. pin- (IEC.txt leaf 521)\", \"stance\": \"supports\", \"note\": \"'pin- (pinák-) \\\"wood, stick, board, log\\\". WP II, 71 Skt. cf. pinakam \\\"stick, cudgel\\\"; Gk. pinax, gs: -akos, m. \\\"board, tablet, platter\\\"; OCS (and com. Sl.) pьnь, m. \\\"trunk, log\\\".'\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Greek\",\n          \"words\": \"pinakx : board, platter\",\n          \"verdict\": \"transcription_suspect\",\n          \"error_in\": \"book\",\n          \"book_prints\": \"pinakx\",\n          \"correct_form\": \"pínax (πίναξ, gen. πίνακος)\",\n          \"derivation\": \"The word meant is Gk. πίναξ, gen. πίνακος 'plank, board, writing-tablet, picture; dish, platter' — Buck's §5.32 'PLATE' heads the Greek column with exactly this word. The form 'pinakx' printed in the book is impossible: it looks like a conflation of the nominative πίναξ (pínax) with the oblique stem πίνακ- (pinak-). I rendered pdf page 403 at 200 dpi and read it: the page itself prints 'pinakx : board, platter', so the JSON extraction is faithful and the error is Nourai's; he most likely copied it from Mo'in's footnote in Borhan-e Qate' p. 1502, where the Greek source of پنگان is printed in Latin letters as 'pínkx' (read from the page image). Apart from the spelling the derivation is the traditional one (Pokorny 830, WP II 71, Buck 345, Fick 1890); Beekes dissents, preferring a Pre-Greek origin for πίναξ while allowing the Slavic words as possible cognates.\",\n          \"derivation_fa\": \"واژهٔ مقصود πίναξ (حالت اضافی πίνακος) است به معنی «تخته، لوح نوشتن، تابلو» و نیز «بشقاب، سینی» — باک در بخش ۵٫۳۲ «بشقاب» (ص ۳۴۵) ستون یونانی را با همین واژه آغاز می‌کند. صورتِ چاپیِ «pinakx» ناممکن است و آشکارا آمیزه‌ای است از صورت فاعلیِ pínax و ستاکِ مایلِ pinak-. صفحهٔ ۴۰۳ نسخهٔ پی‌دی‌اف را با دقت ۲۰۰ نقطه بازنمایی و خواندم: خودِ کتاب «pinakx» چاپ کرده است، پس خطای خوانشِ اسکن در کار نیست و خطای چاپی از نورایی است؛ به‌گمان بسیار آن را از حاشیهٔ معین در برهان قاطع (ص ۱۵۰۲) گرفته که در آنجا نیز صورت یونانی به لاتین «pínkx» چاپ شده است. جز این غلط املایی، خودِ اشتقاق همان دیدگاه سنتی (پوکورنی، والده‑پوکورنی، باک) است؛ بیکس آن را پیش‑یونانی می‌داند.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%CF%80%CE%AF%CE%BD%CE%B1%CE%BE\"],\n          \"ref_check\": [\n            {\"ref\": \"POK:830\", \"status\": \"supports\", \"note\": \"'gr. πίναξ, -ακος \\\"Sparre, Balken, Brett, Schreibtafel, Gemälde\\\"' under Root pi-n-.\"},\n            {\"ref\": \"SYN:345\", \"status\": \"supports\", \"note\": \"Buck p. 345 (leaf 388, running head 'FOOD AND DRINK; COOKING AND UTENSILS 345', section '5.32 PLATE'): '1. Grk. πίναξ \\\"board, plank, tablet\\\" and \\\"platter\\\" : Skt. pinaka- \\\"staff\\\", ChSl. pьnь, Russ. pen' … \\\"tree-trunk\\\" or \\\"stump\\\", Walde-P. 2.71.' — both the gloss 'board, platter' and the root connection are Buck's.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"WLD\", \"where\": \"Bd. II 71 s.v. pin\", \"stance\": \"supports\", \"note\": \"same comparison; spells the Greek πίναξ, -ακος.\"},\n            {\"src\": \"IEC\", \"where\": \"Mann p. 938 s.v. pin- (pinák-)\", \"stance\": \"supports\", \"note\": \"'Gk. pinax, gs: -akos, m. \\\"board, tablet, platter\\\"' — note Mann's correct 'pinax', which shows the printed 'pinakx' is not a transliteration convention of the sources.\"},\n            {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org s.v. πίναξ\", \"stance\": \"partial\", \"note\": \"'Since Fick (1890), considered a native word of Proto-Indo-European origin, cognate with Sanskrit पिना॑क (pínāka) and Proto-Slavic *pь̏ňь … On the other hand, Beekes inevitably prefers a Pre-Greek origin, though allows that the Slavic terms may be cognate.'\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"pangân «پَنگان» : cup\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"NP پنگان pangān/pingān is a copper bowl — in the older texts specifically the pierced bowl of the water-clock (طاسی از مس که در بن آن سوراخ تنگی کنند … ساعت آبی), then any metal cup or basin. It is a borrowing of Gk. πίναξ, πίνακος 'dish, platter', the -ak- of the oblique stem giving Persian -gān with the regular voicing of intervocalic k in the Middle Iranian period; the loan is of the Parthian/Sasanian period, when Greek table-ware vocabulary entered Iranian, and the same Greek word was taken over into Aramaic/Syriac as pīnəkā (ܦܝܢܟܐ) and into Ossetic as fyng, fingæ 'table', so a Syriac relay is possible. Mo'in says so expressly in his footnote to Borhan-e Qate' p. 1502 (the page Nourai cites), and Wiktionary's Persian entry has the same tree. The one dissenting voice is Asbaghi (PLA p. 212), who takes Arabic finǧān from Persian pangān but then traces pangān to MP paygāl 'cup' (MacKenzie) — phonetically impossible as a source of pangān, and paygāl is in fact the ancestor of NP پیاله.\",\n          \"derivation_fa\": \"«پنگان» در متون کهن طاسی مسین است که ته آن سوراخی تنگ دارد و با آن ساعت‌های شبانه‌روز را می‌سنجیدند (ساعت آبی)، و سپس هر کاسه و جام مسین. این واژه وام‌گرفته از یونانی πίναξ / πίνακος «بشقاب، سینی» است: ستاک مایلِ pinak- در ایرانی میانه با نرم‌شدنِ ک میان دو واکه به ‎-gān بدل شده و صورت پنگان/پنگان به دست آمده؛ وام‌گیری به روزگار اشکانی‑ساسانی بازمی‌گردد که واژگان ظروف یونانی به ایرانی راه یافت، و همین واژهٔ یونانی در آرامی/سریانی pīnəkā و در آسی fyng «میز» نیز بازتاب دارد، پس میانجیگری سریانی هم ممکن است. معین در حاشیهٔ برهان قاطع (ص ۱۵۰۲) — همان صفحه‌ای که نورایی ارجاع می‌دهد — همین را می‌گوید. تنها آصف‌باغی (PLA ص ۲۱۲) پنگان را به فارسی میانهٔ paygāl «جام» می‌برد که از نظر آوایی نشدنی است و paygāl در حقیقت نیای «پیاله» است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%BE%D9%86%DA%AF%D8%A7%D9%86\",\n            \"https://en.wiktionary.org/wiki/%D9%81%D9%86%D8%AC%D8%A7%D9%86\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"BQT:1502\", \"status\": \"supports\", \"note\": \"Borhan-e Qate' ed. Mo'in, p. 1502, footnote 9 (fetched with tools/ref_page.py BQT:1502 = pdf p. 295 of BQT_v3; OCR poor, so read from the PNG and transcribed to refs/ocr/BQT/1502.vision.txt): «فنجان ـ (بکسر اول) = پنگان (هم.) از یونانی pínkx ، کردی fynjân, fynjan و fanjân ، ژابا ۲۹۵ ، گیلکی finjân ؛ پیاله (چای‌خوری، قهوه‌خوری)، پنگان». Mo'in thus gives fenjān = pangān and a Greek source — exactly Nourai's chain; note he prints the Greek as 'pínkx', which is almost certainly where Nourai's 'pinakx' comes from.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"Mo'in, Farhang-e Farsi s.v. پنگان (MON_part1.txt l. 32919)\", \"stance\": \"supports\", \"note\": \"'پنگان [= بنکام = فنجان، معر.] (اِ) طاسی باشد از مس و امثال آن که در بن آن سوراخ تنگی کنند … ساعت آبی، صندوق ساعت، طاس ساعت، بنکام. هر کاسه و طاس رویین و مسین را که ظرف طعام یا آب باشد پنگان گویند' — pangān and fenjān explicitly equated, fenjān marked معرّب.\"},\n            {\"src\": \"PLA\", \"where\": \"Asbaghi, Persische Lehnwörter im Arabischen, p. 212 s.v. finǧān\", \"stance\": \"partial\", \"note\": \"'finǧān: \\\"Porzellanschale; Kaffeetasse\\\" pers. پنگان pangān … << mp. pygʾl paygāl \\\"Tasse\\\"' (footnotes: al-Muʿarrab, Muḥīṭ, al-Munǧid; MacKenzie). Supports pangān > Arabic, but offers a different — and phonetically untenable — ultimate origin instead of Greek.\"},\n            {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary, English index 'cup paygāl' (PHD.txt l. 1461-1462)\", \"stance\": \"partial\", \"note\": \"MacKenzie has MP paygāl 'cup', paygālgar 'cup-maker', but no *pangān; paygāl is the ancestor of NP پیاله, not of پنگان, which confirms that Asbaghi's alternative does not work.\"},\n            {\"src\": \"AFM\", \"where\": \"Addi Shir, al-Alfaz al-farisiyya al-mu'arraba s.v. البنكام (AFM_pages.txt l. 721-724)\", \"stance\": \"supports\", \"note\": \"'(البنكام) … في البرهان القاطع … بالكاف الفارسية على وزن سندان يطلق عموماً على القدح والكأس وخصوصاً على … طاس من النحاس … فيلقون الطاس في الماء …' — the Persian water-clock bowl, borrowed into Arabic.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Arabic\",\n          \"words\": \"\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"The empty box is Arabic فِنْجَان finjān (also فنجال finjāl) 'small cup, coffee cup', the Arabicized form of Persian pingān: Persian p- has no Arabic counterpart and is regularly replaced by f- (cf. پیل > فیل, پارسی > فارسی), and the -g- is rendered by ǧīm, giving fin-ǧān; the pattern fiʿlān is a familiar shape for vessel names. The Arab lexicographers themselves note the word is foreign: al-Jawāliqī's editor quotes al-Miʿyār, 'al-finjān, with jīm, a well-known vessel, muʿarrab of pingān … its plural is fanājīn', and Addi Shir and al-Unaysi say the same.\",\n          \"derivation_fa\": \"جعبهٔ خالی نمایندهٔ «فِنْجان» عربی است، معرّبِ «پنگان» فارسی: پِ فارسی در عربی معادل ندارد و به ف بدل می‌شود (چنان‌که پیل > فیل و پارسی > فارسی) و گ به جیم می‌گراید، پس پنگان > فنجان بر وزن فِعلان که برای نام ظرف‌ها آشناست. خودِ فرهنگ‌نویسان عرب آن را دخیل می‌دانند: در حاشیهٔ المعرّبِ جوالیقی از «المعیار» نقل شده است «الفنجان، بالجیم، إناء معروف، معرّب پنکان … یجمع فناجین»، و ادّی شیر و طوبیا العنیسی نیز همین را می‌گویند. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D9%81%D9%86%D8%AC%D8%A7%D9%86\"],\n          \"ref_check\": [\n            {\"ref\": \"(none cited)\", \"status\": \"not_checked\", \"note\": \"the chart gives no reference for this pass-through Arabic box; the surrounding references (BQT:1502, MON) were checked on the neighbouring nodes.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"ARB\", \"where\": \"al-Jawaliqi, al-Mu'arrab, editor's footnote (ARB_mo3rb.txt l. 18160-18162)\", \"stance\": \"supports\", \"note\": \"«قال أدي شير: الفنجان معرّب پنگان … وهذه المادة لم أجدها في معاجم اللغة إلا في المعيار، قال: الفنجان، بالجيم، إناء معروف، معرّب پنکان؛ ويكسر فاؤه، الواحد بهاء، يجمعه فناجين».\"},\n            {\"src\": \"TAD\", \"where\": \"al-Unaysi, Tafsir al-alfaz al-dakhila, s.v. فنجان (TAD_pages.txt l. 2057)\", \"stance\": \"supports\", \"note\": \"«فنجان ـ فارسي «فنجان وپنگان» وهو قدح صغير من خزف» — 'Persian: finjān and pingān; a small earthenware cup'.\"},\n            {\"src\": \"PLA\", \"where\": \"Asbaghi p. 212 s.v. finǧān\", \"stance\": \"supports\", \"note\": \"'finǧān … pers. پنگان pangān' with al-Muʿarrab, al-Muḥīṭ and al-Munǧid as witnesses.\"},\n            {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org s.v. فنجان (Arabic)\", \"stance\": \"supports\", \"note\": \"'Borrowed from Classical Persian پِنْگَان (pingān), possibly borrowed from Classical Syriac ܦܝܢܟܐ (pīnəḵā), from Aramaic פִּינְכָא (pīnəkā), borrowed from Ancient Greek πίναξ (pínax).'\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Persian\",\n          \"words\": \"fenjân «فنجان» : cup\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"NP فنجان fenjān 'cup, coffee/tea cup' is the Arabic word taken back into Persian — a classic round trip (Persian pingān > Arabic finǧān > Persian fenjān), so that Persian now has a doublet: the native پنگان (obsolete, 'water-clock bowl') beside the re-imported فنجان, which is the ordinary modern word and is written with the Arabic spelling. The re-borrowing is late (the modern sense 'coffee cup' spreads with coffee-drinking from the 16th c. onwards, whence also Ottoman/Turkish fincan, Kurdish finjān, Gilaki finjān). Mo'in marks the relation explicitly by glossing پنگان with '= فنجان، معرّب'.\",\n          \"derivation_fa\": \"«فنجان» فارسیِ امروز همان واژهٔ عربی است که دوباره به فارسی بازگشته است؛ سفرِ رفت‌وبرگشتِ کلاسیک: پنگانِ فارسی ← فِنجانِ عربی ← فنجانِ فارسی. از این رو در فارسی دوگانه (doublet) داریم: «پنگان» کهن و متروک به معنی طاسِ ساعت آبی، و «فنجان» وام‌گرفتهٔ دوباره با املای عربی که واژهٔ رایج امروزی است. این وام‌گیریِ دوم دیرهنگام است و با رواج قهوه‌نوشی از سدهٔ دهم هجری گسترش یافته است (نیز ترکی fincan، کردی finjān، گیلکی finjān). معین با آوردن «پنگان [= فنجان، معر.]» همین پیوند را نشان می‌دهد. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D9%81%D9%86%D8%AC%D8%A7%D9%86\"],\n          \"ref_check\": [\n            {\"ref\": \"MON\", \"status\": \"supports\", \"note\": \"Mo'in, Farhang-e Farsi s.v. پنگان (MON_part1.txt l. 32919): 'پنگان [= بنکام = فنجان، معر.]' — Mo'in equates the two and tags فنجان as the Arabicized form; his footnote in Borhan-e Qate' 1502 spells the chain out (فنجان < پنگان < یونانی).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' p. 1502 fn. 9 (refs/ocr/BQT/1502.vision.txt)\", \"stance\": \"supports\", \"note\": \"«فنجان ـ (بکسر اول) = پنگان (هم.) از یونانی pínkx … گیلکی finjân؛ پیاله (چای‌خوری، قهوه‌خوری)، پنگان».\"},\n            {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org s.v. فنجان (Persian)\", \"stance\": \"supports\", \"note\": \"'Borrowed from Arabic فِنْجَان (finjān), borrowed from Classical Persian پِنْگَان (pingān) … Doublet of پنكان (pingân, \\\"cup\\\").'\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 2,\n      \"root\": \"Pippalî\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"Sanskrit पिप्पली pippalī 'long pepper (Piper longum)'\",\n      \"note\": \"The headword is correctly labelled Sanskrit (not an IE root) and correctly glossed, though strictly pippalī is 'long pepper'; beside it stand pippala- 'berry; the bo tree' and pippalam 'berry'. Watkins brackets the entry precisely because it is not IE: '[pippali. Pepper. Sanskrit noun of unknown origin. Possibly related to pippala, the bo tree. 1. Sanskrit pippali: PEPPER, (PIMPERNEL). 2. Sanskrit pippalam: PEEPUL.]' Modern opinion (Wiktionary, Mayrhofer) suspects a Dravidian source, cf. Tamil tippali; Ernout-Meillet already observed that the -l- form belongs to eastern India while the Greek and Latin r-form must come from western India 'où r est normal'. Everything downstream on this chart is a Wanderwort chain and is well documented.\",\n      \"note_fa\": \"سرواژه درست برچسب خورده است (سنسکریت، نه ریشهٔ هندواروپایی) و معنی نیز درست است، هرچند pippalī دقیقاً «فلفل دراز» (Piper longum) است؛ در کنار آن pippala- «دانه؛ درخت بودهی» جای دارد. واتکینز همین را در قلاب می‌آورد: «pippali. فلفل. اسمی سنسکریت با خاستگاه نامعلوم، شاید مربوط به pippala». پژوهش امروزی (مایرهوفر و ویکی‌واژه) خاستگاه دراویدی را محتمل می‌داند (قیاس کنید با تامیلی tippali). ارنو‑مه‌یه نیز یادآور شده که صورتِ دارای «ل» به هند شرقی و صورتِ دارای «ر» در یونانی و لاتینی به هند غربی تعلق دارد. زنجیرهٔ پس از آن، واژه‌ای جهانگرد (Wanderwort) و به‌خوبی مستند است. ادعای نورایی درست است.\",\n      \"sources\": [\n        \"https://www.etymonline.com/word/pepper\",\n        \"https://en.wiktionary.org/wiki/%CF%80%CE%AD%CF%80%CE%B5%CF%81%CE%B9\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"AHD:1535\", \"status\": \"supports\", \"note\": \"Watkins's appendix (AHD_watkins1985.txt l. 855, immediately after pilo- and pipp-): '[pippali. Pepper. Sanskrit noun of unknown origin. Possibly related to pippala, the bo tree. 1. Sanskrit pippali: PEPPER, (PIMPERNEL). 2. Sanskrit pippalam: PEEPUL.]' — same headword, same gloss; the 1975 New College appendix runs pp. 1505-1550, so the p-entries fall about p. 1535.\"},\n        {\"ref\": \"KLN:1154\", \"status\": \"supports\", \"note\": \"Klein 1966, p. 1154/1155 (KLN_1966.txt l. 28054, on the leaf carrying the page numbers 1154-1155), s.v. pepper: 'ME. peper, piper, fr. OE. pipor, tr. L. piper, \\\"pepper\\\", fr. Gk. πέπερι, ult., through Persian mediation, fr. OI. pippalī, \\\"berry, peppercorn\\\"'.\"},\n        {\"ref\": \"SYN:382\", \"status\": \"supports\", \"note\": \"Buck, p. 382, §5.82 PEPPER (SYN.txt l. 9627-9630, leaf 428 which carries '382'): 'Nearly all the Eur. words for \\\"pepper\\\" are fr. Lat. piper, itself a loanword fr. Grk. πέπερι, this being, like the article itself, of Indian orig. Cf. Skt. pippala-, pippali-, \\\"berry, pepper\\\". Schrader, Reallex. 2.164. Boisacq 769. Ernout-M. 771.'\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"HJB\", \"where\": \"Hobson-Jobson, Introductory Remarks (HJB.txt l. 143)\", \"stance\": \"supports\", \"note\": \"among the products 'introduced from India to the Greek and Roman world': 'pepper (πέπερι, from Skt. pippali, \\\"long pepper\\\")'.\"},\n        {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. piper (LAT.txt l. 47714-47728)\", \"stance\": \"supports\", \"note\": \"'Piper est un emprunt commercial, cf. gr. πέπερι qui lui-même provient de l'Orient: le skr. a pippalī f. \\\"grain de poivre\\\", dont l'l appartiendrait à l'Inde orientale, tandis que le mot grec et latin viendrait de l'Inde de l'Ouest où r est normal.'\"},\n        {\"src\": \"IEC\", \"where\": \"Mann, leaf 521 s.v. pippal- (IEC.txt)\", \"stance\": \"partial\", \"note\": \"Mann lists 'pippalih, f. \\\"capsicum, chilli\\\"; pippalah \\\"sacred figtree; nipple\\\"' under an expressive pipp- group — i.e. he keeps the Indian word apart from any inherited IE root, as Watkins does.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Persian\",\n          \"words\": \"pelpel «پلپل» : pepper\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Persian پلپل pilpil/pelpel is the Indian word taken into Iranian by the spice trade: Skt. pippalī, with its geminate -pp- and final -ī, was adapted as pilpil with dissimilatory l for the second p (the same l appears in Aramaic pilpelā, Hebrew pilpēl, Old Armenian pġpeł, Georgian ṗilṗili — all, as Wiktionary notes, Iranian-mediated borrowings). The word is attested in classical Persian verse — Manūchehrī's line that Nourai prints ('تو گویی پلپل سوده بکف داشت') — and is the form that Mo'in and the Arab lexicographers name as the source of Arabic filfil.\",\n          \"derivation_fa\": \"«پلپل» فارسی همان واژهٔ هندی است که با بازرگانیِ ادویه به ایران رسیده است: pippalī سنسکریت با پـ مشدّد و یای پایانی، در ایرانی به pilpil سازگار شده و «پ» دوم به «ل» بدل گشته است (همین «ل» در آرامی pilpelā، عبری pilpēl، ارمنی کهن pġpeł و گرجی ṗilṗili دیده می‌شود که همه وام‌های ایرانی‌میانجی‌اند). این صورت در شعر فارسی گواه دارد — همان بیت منوچهری که نورایی آورده است — و معین و فرهنگ‌نویسان عرب نیز همین را خاستگاه «فلفل» عربی می‌دانند. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D9%81%D9%84%D9%81%D9%84\"],\n          \"ref_check\": [\n            {\"ref\": \"BQT:1499\", \"status\": \"supports\", \"note\": \"Borhan-e Qate' ed. Mo'in p. 1499, footnote 10 (fetched with tools/ref_page.py BQT:1499 = pdf p. 292 of BQT_v3; read from the PNG, transcript saved as refs/ocr/BQT/1499.vision.txt): «فلفل ـ (بکسر اول و سوم) معرب پلپل (ه.م.)، از سانسکریت pippalî «ویلیامز ۱:۹۲۸» … کردی fylfil … گیلکی filfîl = (Piper nigrum)». Mo'in's پلپل < Skt pippalī is precisely Nourai's arrow.\"},\n            {\"ref\": \"FVF:503\", \"status\": \"not_checked\", \"note\": \"Emam Shushtari, Farhang-e Vazheha-ye Farsi dar Zaban-e Arabi — refs_online.json records no local copy and no OCR (noorlib page viewer needs a browser session), so p. 503 could not be read.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' p. 1499 fn. 10\", \"stance\": \"supports\", \"note\": \"see ref_check: «معرب پلپل … از سانسکریت pippalî».\"},\n            {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org s.v. فلفل (Arabic section)\", \"stance\": \"supports\", \"note\": \"'Borrowed from Classical Persian پِلْپِل (pilpil), from Sanskrit पिप्पलि (pippali, \\\"long pepper\\\"), ultimately from Dravidian … Compare … Aramaic פלפלא (pelplā), Hebrew פלפל (pilpél), Old Armenian պղպեղ … Iranian borrowings.'\"},\n            {\"src\": \"KLN\", \"where\": \"Klein 1966 p. 1154 s.v. pepper\", \"stance\": \"supports\", \"note\": \"'fr. Gk. πέπερι, ult., through Persian mediation, fr. OI. pippalī' — Klein too routes the word through Persian.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Arabic\",\n          \"words\": \"felfel : pepper\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Arabic فِلْفِل filfil (also fulful, fulfil) 'pepper' is the Arabicization of Persian pilpil: Persian p- is replaced by f- exactly as in pingān > finjān and pīl > fīl, and the resulting fil-fil fits the native reduplicated fiʿlil pattern perfectly, which is why the word was fully naturalized and even generated a verb فلفل 'to season with pepper'. The lexicographers know it is foreign: Addi Shir enters it among the Persian words arabicized, and al-Unaysi calls it 'an Indian word, since the plant originates there'.\",\n          \"derivation_fa\": \"«فِلفِل» عربی معرّبِ «پلپل» فارسی است: پِ فارسی مانند پنگان > فنجان و پیل > فیل به ف بدل شده و صورتِ حاصل، fil-fil، درست بر وزن مکرّرِ فِعلِل عربی نشسته است؛ به همین سبب واژه چنان بومی شد که فعل «فلفل» (ادویه زدن) نیز از آن ساختند. فرهنگ‌نویسان عرب دخیل بودنش را می‌دانند: ادّی شیر آن را در شمار الفاظ فارسیِ معرّب می‌آورد و طوبیا العنیسی می‌نویسد «لفظ هندي حيث منشأ هذا النبات». ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D9%81%D9%84%D9%81%D9%84\"],\n          \"ref_check\": [\n            {\"ref\": \"FVF:503\", \"status\": \"not_checked\", \"note\": \"Shushtari's Farhang-e Vazheha-ye Farsi dar Zaban-e Arabi is not available locally or as OCR (see refs_online.json: local_file null, noorlib viewer only).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"AFM\", \"where\": \"Addi Shir, al-Alfaz al-farisiyya al-mu'arraba, s.v. الفلفل (AFM_pages.txt l. 3085)\", \"stance\": \"supports\", \"note\": \"«(الفلفل) لحاء هندي شديد الحرافة … تعريب پلپل …» followed by the Kurdish and Syriac forms — 'ta'rīb of pilpil', i.e. exactly the arrow drawn here.\"},\n            {\"src\": \"TAD\", \"where\": \"al-Unaysi, Tafsir al-alfaz al-dakhila, s.v. فلفل (TAD_pages.txt l. 2040)\", \"stance\": \"supports\", \"note\": \"«فلفل ـ لفظ هندي حيث منشأ هذا النبات الذي حبّه شديد الحرافة» — registered as a foreign (Indian) word.\"},\n            {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' p. 1499 fn. 10\", \"stance\": \"supports\", \"note\": \"«فلفل … معرب پلپل … از سانسکریت pippalî».\"},\n            {\"src\": \"FVQ\", \"where\": \"Jeffery, Foreign Vocabulary of the Qur'an — grep 'filfil', 'pippal' in FVQ.txt\", \"stance\": \"silent\", \"note\": \"no entry: filfil is not a Qur'anic word, so Jeffery does not treat it.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"felfel «فلفل» : pepper\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Modern Persian فلفل felfel is the Arabic form re-imported into Persian, displacing the native پلپل: the Arabic spelling with fā' is the one written today, and the word covers both black pepper and (later) capsicum, with compounds like فلفل سبز, فلفل قرمز. Persian therefore has a doublet پلپل / فلفل of the kind the chart draws, and Mo'in signals it by defining فلفل as 'muʿarrab of pelpel' — i.e. a Persian word that returned home in Arabic dress. Wiktionary's Persian entry gives the same route (Arabic filfil < Classical Persian pilpil < Skt pippali).\",\n          \"derivation_fa\": \"«فلفل» فارسی امروز همان صورت عربی است که به فارسی بازگشته و جای «پلپل» بومی را گرفته است؛ املای عربی با «ف» امروزه رایج است و واژه هم فلفل سیاه و هم (بعدها) فلفل فرنگی را دربر می‌گیرد (فلفل سبز، فلفل قرمز). پس در فارسی دوگانهٔ «پلپل / فلفل» داریم، درست همان‌گونه که نمودار نشان می‌دهد، و معین با تعریف «فلفل: معرّب پلپل» به همین بازگشت اشاره می‌کند. ویکی‌واژه نیز همین مسیر را می‌دهد (عربی filfil < فارسی pilpil < سنسکریت pippali). ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D9%81%D9%84%D9%81%D9%84\"],\n          \"ref_check\": [\n            {\"ref\": \"BQT:1499\", \"status\": \"supports\", \"note\": \"the footnote is filed under the Persian headword فلفل on p. 1499 and reads «فلفل ـ (بکسر اول و سوم) معرب پلپل (ه.م.)، از سانسکریت pippalî» — Mo'in is describing the Persian word فلفل as the Arabicized shape of پلپل, which is Nourai's node exactly.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"Mo'in, Farhang-e Farsi, فلفل / فلفل‌مویه (MON_part2.txt l. 8577 and the فلفل entries in MON_part1.txt)\", \"stance\": \"supports\", \"note\": \"the lexicon carries فلفل as the ordinary Persian word (with the by-form پلپل‌مویه beside فلفل‌مویه), confirming that the Arabic-shaped form is the current Persian one.\"},\n            {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org s.v. فلفل (Persian)\", \"stance\": \"supports\", \"note\": \"'From Arabic فِلْفِل (filfil), from Classical Persian پلپل (pilpil).'\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Greek\",\n          \"words\": \"peperi\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Gk. πέπερι (péperi) n. 'pepper', first in Hippocrates and the medical writers, is a borrowing of the same Indian word along the Achaemenid/Hellenistic trade route: an Indo-Aryan form of the pippalī type gave πίπερι/πέπερι with r for the Indian l — Ernout-Meillet's point that the r-form 'viendrait de l'Inde de l'Ouest où r est normal', i.e. from a north-western Prakrit (compare Middle Indic pippari). Nourai draws the arrow straight from Sanskrit; Klein and Etymonline insert Iranian mediation ('ult., through Persian mediation, fr. OI. pippalī'; 'from Greek piperi, probably (via Persian) from Middle Indic pippari'), which fits the trade geography and does not conflict with the chart, since Persian pilpil is the sister node.\",\n          \"derivation_fa\": \"πέπερι یونانی «فلفل» که نخست در بقراط و پزشک‌نامه‌ها دیده می‌شود، وامِ همان واژهٔ هندی است که از راه بازرگانی هخامنشی و هلنی به یونان رسیده: صورتی هندوآریایی از گونهٔ pippalī به πίπερι/πέπερι بدل شده با «ر» به‌جای «ل» هندی — چنان‌که ارنو‑مه‌یه گفته، صورتِ «ر»دار از هند شمال‌غربی می‌آید که در آنجا «ر» عادی است (قیاس کنید با هندی میانهٔ pippari). نورایی پیکان را مستقیم از سنسکریت می‌کشد؛ کلاین و اتیمآنلاین میانجیگری فارسی را می‌افزایند («از راه واسطهٔ فارسی») که با جغرافیای بازرگانی سازگار است و با نمودار ناسازگار نیست، چون «پلپل» فارسی در همان نمودار گرهِ خواهر است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%CF%80%CE%AD%CF%80%CE%B5%CF%81%CE%B9\",\n            \"https://www.etymonline.com/word/pepper\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD:972\", \"status\": \"not_checked\", \"note\": \"this is a page of the body of the American Heritage Dictionary (New College Edition), not of Watkins's appendix; only the appendix (AHD_watkins1985.txt) is held locally, so p. 972 could not be read. Its appendix cross-reference, '[pippali … 1. Sanskrit pippali: PEPPER]', says the same thing.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"SYN\", \"where\": \"Buck p. 382 §5.82\", \"stance\": \"supports\", \"note\": \"'Nearly all the Eur. words for \\\"pepper\\\" are fr. Lat. piper, itself a loanword fr. Grk. πέπερι, this being, like the article itself, of Indian orig. Cf. Skt. pippala-, pippali-.'\"},\n            {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. piper\", \"stance\": \"supports\", \"note\": \"'gr. πέπερι qui lui-même provient de l'Orient: le skr. a pippalī … tandis que le mot grec et latin viendrait de l'Inde de l'Ouest où r est normal.'\"},\n            {\"src\": \"HJB\", \"where\": \"Hobson-Jobson, Introductory Remarks\", \"stance\": \"supports\", \"note\": \"'pepper (πέπερι, from Skt. pippali, \\\"long pepper\\\")'.\"},\n            {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org s.v. πέπερι\", \"stance\": \"supports\", \"note\": \"'From an Indo-Aryan source; compare Sanskrit पिप्पलि (pippali, \\\"long pepper\\\").'\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Latin\",\n          \"words\": \"\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"The empty box is Latin piper, -eris n. 'pepper; the pepper plant', a commercial borrowing of Gk. πέπερι that Ernout-Meillet say is not attested before Varro (1st c. BCE) — the period when the Roman pepper trade with Malabar took off. Latin piper is the ancestor of the whole European set (It. pepe, Fr. poivre, Sp. pebre, OCS pьprъ, Lith. pipiras, OIr. piobhar, W. pybyr) and of the Germanic forms including OE pipor.\",\n          \"derivation_fa\": \"جعبهٔ خالی نمایندهٔ لاتینی piper, -eris «فلفل» است؛ وامی بازرگانی از πέπερι یونانی که به گفتهٔ ارنو‑مه‌یه پیش از وارّو (سدهٔ یکم پیش از میلاد) گواهی ندارد — درست همان روزگاری که بازرگانی فلفلِ روم با مالابار رونق گرفت. همین piper نیای همهٔ صورت‌های اروپایی است: pepe ایتالیایی، poivre فرانسوی، pьprъ اسلاوی کهن، pipiras لیتوانیایی، piobhar ایرلندی و نیز pipor انگلیسی کهن. ادعای نورایی درست است.\",\n          \"sources\": [\"https://www.etymonline.com/word/pepper\"],\n          \"ref_check\": [\n            {\"ref\": \"(none cited)\", \"status\": \"not_checked\", \"note\": \"the chart gives no reference for this pass-through Latin box; KLN:1154 on the following node covers the Latin > English step.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. piper (LAT.txt l. 47714)\", \"stance\": \"supports\", \"note\": \"'piper, -eris n.: poivre; poivrier. Ne semble pas attesté avant Varron. Panroman … Piper est un emprunt commercial, cf. gr. πέπερι.'\"},\n            {\"src\": \"SYN\", \"where\": \"Buck p. 382 §5.82\", \"stance\": \"supports\", \"note\": \"'Nearly all the Eur. words for \\\"pepper\\\" are fr. Lat. piper' — with the table NG πιπέρι, Lat. piper, It. pepe, Fr. poivre, OE pipor, OHG pfeffar.\"},\n            {\"src\": \"KLN\", \"where\": \"Klein 1966 p. 1154 s.v. pepper\", \"stance\": \"supports\", \"note\": \"'It. pepe, OProvenç., Catal., Sp. pebre, F. poivre, OSlav. pipru, Lith. pipiras, OIr. piobhar, W. pybyr … are all borrowed fr. L. piper.'\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"English\",\n          \"words\": \"pepper\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English pepper continues Old English pipor, an early West Germanic borrowing of Latin piper made while the Germanic tribes were still in contact with Roman trade (the same loan gives OHG pfeffar with the High German consonant shift, Du. peper, ON piparr). OE pipor > ME peper, piper > NE pepper, with the regular lowering of the first vowel and doubling of the medial consonant in Middle English spelling. Klein's entry on the page Nourai cites states the whole chain.\",\n          \"derivation_fa\": \"«pepper» انگلیسی دنبالهٔ pipor انگلیسی کهن است؛ وامی کهن از piper لاتینی که در دورانِ داد و ستدِ ژرمن‌ها با روم گرفته شده است (همین وام در آلمانی علیای کهن pfeffar را با جابه‌جایی همخوانیِ آلمانی علیا، و در هلندی peper و نورسی کهن piparr پدید آورده). pipor انگلیسی کهن به peper/piper انگلیسی میانه و سپس pepper امروزی رسیده است. کلاین در همان صفحه‌ای که نورایی ارجاع می‌دهد (ص ۱۱۵۴) تمام این زنجیره را می‌آورد. ادعای نورایی درست است.\",\n          \"sources\": [\"https://www.etymonline.com/word/pepper\"],\n          \"ref_check\": [\n            {\"ref\": \"KLN:1154\", \"status\": \"supports\", \"note\": \"Klein 1966, p. 1154 (KLN_1966.txt l. 28054): 'pepper, n. — ME. peper, piper, fr. OE. pipor, tr. L. piper, \\\"pepper\\\", fr. Gk. πέπερι, ult., through Persian mediation, fr. OI. pippalī, \\\"berry, peppercorn\\\" … OFris. piper, Du. peper, OHG. pfeffar …'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"Etymonline\", \"where\": \"etymonline.com s.v. pepper (n.)\", \"stance\": \"supports\", \"note\": \"'Middle English peper, from Old English pipor, from an early West Germanic borrowing of Latin piper \\\"pepper\\\", from Greek piperi, probably (via Persian) from Middle Indic pippari, from Sanskrit pippali \\\"long pepper\\\".'\"},\n            {\"src\": \"SYN\", \"where\": \"Buck p. 382 §5.82 table\", \"stance\": \"supports\", \"note\": \"'OE pipor / ME peper / NE pepper' in the Germanic column, all under Lat. piper.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\nJSONEOF\npython3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-403.json > /dev/null && echo \"JSON OK\"",
 "description": "Write verification JSON for page 403"
}
```


### [2026-09-14T01:12:00.920Z] TOOL RESULT

```
JSON OK
```


## [2026-09-14T01:12:03.650Z] TOOL CALL #83: Bash

```json
{
 "command": "python3 tools/verify_check.py 403",
 "description": "Run verify_check for page 403"
}
```


### [2026-09-14T01:12:04.883Z] TOOL RESULT

```
nodes verified: 15/15
node verdicts: {'plausible': 4, 'confirmed': 10, 'transcription_suspect': 1}
root verdicts: {'plausible': 1, 'confirmed': 2}
ref checks: {'supports': 12, 'not_found': 3, 'not_checked': 5}
books consulted: {'partial': 5, 'silent': 4, 'contradicts': 1, 'supports': 35} | by book: {'KLN': 7, 'Wiktionary': 6, 'BQT': 4, 'MON': 3, 'LAT': 3, 'WLD': 3, 'SYN': 3, 'PLA': 2, 'AFM': 2, 'TAD': 2, 'HRN': 1, 'HUB': 1, 'FSD/WEB': 1, 'POK': 1, 'IEC': 1, 'PHD': 1, 'ARB': 1, 'FVQ': 1, 'HJB': 1, 'Etymonline': 1}
```


## [2026-09-14T01:12:24.500Z] AGENT

Page 403 (book p. 373) verified — 3 entries, 15 nodes, 0 PROBLEM lines from `verify_check.py`.

**Counts**: roots — 2 confirmed, 1 plausible. Nodes — 10 confirmed, 4 plausible, 1 transcription_suspect. Ref checks: 12 supports, 3 not_found, 5 not_checked. 35 supporting consultations across 20 books.

**transcription_suspect**
- Pin / node #1 Greek `pinakx` "board, platter" — impossible form for πίναξ (gen. πίνακος). `error_in: book`: pdf p. 403 rendered at 200 dpi prints `pinakx`, so the extraction is faithful. Almost certainly copied from Mo'in's footnote in Borhan-e Qate' p. 1502, which prints the Greek in Latin letters as `pínkx` (read from the page image). The derivation itself is fine (Pokorny 830, WP II 71, Buck 345).

**No `disputed` items, but two weak spots flagged as `plausible`**
- Root *Pilo, Pislos* "hair": the citations are exact (POK 830, WP II 71 *pil-s-os, Mann IEC 940 `pislos`), but the group is no longer held together — Ernout-Meillet ("Aucun rapprochement valable"), de Vaan/Beekes/Wiktionary split Lat. *pilus* (no IE etymology) from Gk. πῖλος / Lat. *pilleus* / OCS *plъstь* "felt" (root *pel- "beat, full cloth"). Nodes #2 (Latin) and #4 (Greek) inherit this.
- Persian پیله *pîleh* "cocoon": only Mann connects it; Horn and Hübschmann are silent, Dehkhoda and Mo'in give no etymology, no Old/Middle Iranian antecedent.
- English node (pile, pluck, plush, caterpillar, pillage): four are secure Latin *pilus*-words, but *pluck* < VL *piluccare is only "perhaps" (OED finds difficulties), and Watkins routes *pillage* via *pilleus* while Etymonline routes it via *pilare*.

**Extraction errors for the owner**: none — the JSON (words, glosses, scripts, refs, both verse quotations) matches the printed page exactly.

**Notable positives**: Mo'in's own footnotes, fetched as page images and transcribed to `refs/ocr/BQT/1502.vision.txt` and `1499.vision.txt`, confirm both Persian chains verbatim (فنجان < پنگان < Greek; فلفل معرّب پلپل < Skt. pippalī). Asbaghi (PLA 212) dissents on پنگان, deriving it from MP *paygāl* — phonetically untenable, and MacKenzie's *paygāl* is in fact the ancestor of پیاله. IEC:1650 could not be checked three times over: our Mann OCR stops at printed p. 1554, and p. 1650 lies in the unscanned Supplement. Page image copied to `data/verification/sources/refs/ocr/BOOK/403.png`.
