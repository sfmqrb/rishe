# Verification process log — verify-page-271


## [2026-09-06T20:55:22.530Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 271 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-271.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-271.json. Write /home/sfmqrb/git/rishe/data/verification/page-271.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 271` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T20:55:23.799Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T20:55:24.514Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T20:55:24.527Z] TOOL RESULT

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


## [2026-09-06T20:55:25.132Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-271.txt"
}
```


### [2026-09-06T20:55:25.159Z] TOOL RESULT

```
1	=== PDF page 271 (book page 241) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Klěu 2, Klâu : hook, peg used to lock doors  (refs POK:604)
4	#1 (parent #0) [Greek] refs=AHD | kleiein : to close ; kleidos, kleiss : key
5	  #2 (parent #1) [Persian] refs=BQT:1687; FVQ:268; ARK:236 | kelîd «کلید» : key
6	#3 (parent #0) [Aramaic] refs=None | 
7	  #4 (parent #3) [Arabic] refs=FVQ:267 | eqlîd : key ; meqlâd, maqâlîd | NOTE: FVF:35 claims "eqlîd" is from Persian "kelîd:key".
8	    #5 (parent #4) [Persian] refs=MON:4283 | meqlâd «مقلاد» : key | extra: مقالید
9	#6 (parent #0) [Germanic] refs=AHD | hluta : portion obtained
10	  #7 (parent #6) [English] refs=None | lot, lottery, lotto
11	#8 (parent #0) [Latin] refs=AHD | claudere : to lock up, close
12	  #9 (parent #8) [English] refs=None | close, closet, clause ; include, exclude, conclude
13	--- entry 1 ---
14	ROOT [Indo-European] Klis : adhere  (refs IEC:1637)
15	#1 (parent #0) [Old Iranian] refs=FFD:60 | srîš, sraîš : a plant and its resin that was used for making glue.
16	  #2 (parent #1) [Avestan] refs=BQT:1136; FFD:60 | srîš : to join, attach, glue
17	    #3 (parent #2) [Pahlavi] refs=FFD:60 | sriš : glue
18	      #4 (parent #3) [Persian] refs=BQT:1136; FFD:60; MON:1867,1880; IEC:1637 | serîš «سیریش» : glue | extra: سیرش ، سریشم
19	  #5 (parent #1) [Avestan] refs=HRN:162; HUB:75 | sraěš : mixture, nature
20	    #6 (parent #5) [Persian] refs=BQT:1124; HRN:162 | serešt «سرشت» : nature ; sereštan «سرشتن» : to mix
21	#7 (parent #0) [Sanskrit] refs=BQT:1134; IEC:1637 | slisyâmî : adhere ; črî : bind, mix
22	
```


## [2026-09-06T20:55:28.967Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-271.json && echo \"=== MATRIX ===\" && cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source JSON and source matrix"
}
```


### [2026-09-06T20:55:29.012Z] TOOL RESULT

```
{
  "pdf_page": 271,
  "book_page": 241,
  "entries": [
    {
      "root": {
        "name": "Klěu 2, Klâu",
        "lang": "Indo-European",
        "refs": "POK:604",
        "gloss": "hook, peg used to lock doors"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD",
          "words": [
            {"translit": "kleiein", "gloss": "to close", "script": null},
            {"translit": "kleidos, kleiss", "gloss": "key", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:1687; FVQ:268; ARK:236",
          "words": [
            {"translit": "kelîd", "gloss": "key", "script": "کلید"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Aramaic",
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Arabic",
          "refs": "FVQ:267",
          "words": [
            {"translit": "eqlîd", "gloss": "key", "script": null},
            {"translit": "meqlâd, maqâlîd", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": "FVF:35 claims \"eqlîd\" is from Persian \"kelîd:key\".",
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Persian",
          "refs": "MON:4283",
          "words": [
            {"translit": "meqlâd", "gloss": "key", "script": "مقلاد"}
          ],
          "script_extra": "مقالید",
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "hluta", "gloss": "portion obtained", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "lot, lottery, lotto", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "claudere", "gloss": "to lock up, close", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "close, closet, clause", "gloss": null, "script": null},
            {"translit": "include, exclude, conclude", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Klis",
        "lang": "Indo-European",
        "refs": "IEC:1637",
        "gloss": "adhere"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Old Iranian",
          "refs": "FFD:60",
          "words": [
            {"translit": "srîš, sraîš", "gloss": "a plant and its resin that was used for making glue.", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Avestan",
          "refs": "BQT:1136; FFD:60",
          "words": [
            {"translit": "srîš", "gloss": "to join, attach, glue", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Pahlavi",
          "refs": "FFD:60",
          "words": [
            {"translit": "sriš", "gloss": "glue", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Persian",
          "refs": "BQT:1136; FFD:60; MON:1867,1880; IEC:1637",
          "words": [
            {"translit": "serîš", "gloss": "glue", "script": "سیریش"}
          ],
          "script_extra": "سیرش ، سریشم",
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 1,
          "lang": "Avestan",
          "refs": "HRN:162; HUB:75",
          "words": [
            {"translit": "sraěš", "gloss": "mixture, nature", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Persian",
          "refs": "BQT:1124; HRN:162",
          "words": [
            {"translit": "serešt", "gloss": "nature", "script": "سرشت"},
            {"translit": "sereštan", "gloss": "to mix", "script": "سرشتن"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "عیب رندان مکن ای زاهد پاکیزه سرشت - که گناه دگران بر تو نخواهند نوشت",
            "poet": "Hâfez"
          }
        },
        {
          "id": 7,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "BQT:1134; IEC:1637",
          "words": [
            {"translit": "slisyâmî", "gloss": "adhere", "script": null},
            {"translit": "črî", "gloss": "bind, mix", "script": null}
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


## [2026-09-06T20:55:34.806Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','AHD','FVQ','IEC','HRN','HUB','MON','BQT','FFD','ARK','ARY','FVF','KLN','BRT','PHD','NYB','WLD','SKT','AFM','PLA','LKT','CHEUNG','SYN','LEW','LAT','AFA','TAD','ARB']:\n    v=d.get(k)\n    print('==',k,json.dumps(v,ensure_ascii=False)[:600] if v else 'MISSING')\n\""
}
```


### [2026-09-06T20:55:36.525Z] TOOL RESULT

```
== POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_
== AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,
== FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sou
== IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 
== HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 
== HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol
== MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په
== BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118
== FFD {"title": "Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ماده-های-فعلهای-فارسی-دری-محسن-اب/ -> https://dl.eliteraturebook.com/app/public/attachments/6925d29630b83.PDF (free PDF site; grey)", "lookup_hint": "Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/download): nothing; only a related paid e-book 'واژگان زبان فارسی دری' (fidibo). ketabnak.com/book/45024 is a different book (فهرست فعلهای فارسی).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/s
== ARK {"title": "M.H. Rokn-zadeh Adamiyyat, Arkan-e Sokhan, Sharq 1347/1968", "kind": "catalog", "url": null, "lookup_hint": "Not found.", "local_file": null, "page_offset": null, "covers_etymology": false, "notes": "none online. || RE-SEARCH 2026-09: nothing digitised on any permitted platform (archive.org, Google Books, Persian libraries/ebook stores). Check opac.nlai.ir manually / buy second-hand."}
== ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 
== FVF {"title": "S.M.A. Emam Shushtari, Farhang-e Vazheha-ye Farsi dar Zaban-e Arabi, Anjoman-e Asar-e Melli 58, Tehran 1347/1968", "kind": "website", "url": "https://noorlib.ir/book/info/105056 (page viewer: https://noorlib.ir/book/view/105056?pageNumber=<N>&viewType=pdf) ; https://ketabnak.com/book/48613 (818 pp. PDF, login) ; http://parsianjoman.org/?p=1265 (download post)", "lookup_hint": "Alphabetical by Persian headword; noorlib page number N is the scan page — browser needed to read. Not on archive.org.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "PDF exists 
== KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h
== BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1
== PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-
== NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf
== WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039
== SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves
== AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/
== PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 lea
== LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 
== CHEUNG MISSING
== SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves
== LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt", "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f b
== LAT {"title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951", "edition_found": "1951 (3rd ed.) - matches Nourai", "kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "identifier": "ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine (4th ed. 1959 lending-only: dictionnairetymo0000unse; another open copy: DictionnaireEtymologiqueDeLaLangueLatine)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt", "page_offset": "leaf = printed + 18 for mos
== AFA {"title": "S. Fraenkel, Die aramäischen Fremdwörter im Arabischen, Leiden 1886 (repr. Hildesheim 1962, same pagination)", "edition_found": "1886", "kind": "archive_djvu", "url": "https://archive.org/details/diearamischenfr00fraegoog", "identifier": "diearamischenfr00fraegoog (also bub_gb_SzdbAAAAQAAJ)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AFA.txt", "page_offset": "leaf = printed + 30 (e.g. leaf 38 = p.8). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
== TAD {"title": "Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-hurufihi (2nd ed. Cairo 1932, ed. Yusuf Tuma al-Bustani; later Library of Lebanon reprint) — Nourai lists it under Arabic authors ('Unaysi T.'); its Table IV line was lost in the OCR", "kind": "archive_djvu", "url": "https://archive.org/details/TOB1932ARAR (1932 ed.); also https://archive.org/details/ar113lang79 and https://archive.org/details/elshandawily14640", "lookup_hint": "Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; insi
== ARB {"title": "al-Jawaliqi, al-Mu'arrab min al-kalam al-a'jami, Tehran 1966 (reprint of Ahmad M. Shakir's Cairo 1361/1942 edition)", "kind": "archive_djvu", "url": "https://archive.org/details/mo3rb (probably the Shakir edition) ; https://archive.org/details/almo3rab_gwaliqy_f_abduraheem (F. 'Abd al-Rahim ed., Damascus 1990) ; also uc1.aa0003615705 / AAlexandrina-148752 (Sachau's Leipzig 1867 ed.) ; text on shamela.ws", "lookup_hint": "Alphabetical Arabic headwords; grep in ARB_mo3rb.txt / ARB_abdulraheem.txt (raw, no page breaks); edition of mo3rb not confirmed — check its title page image.", "lo
```


## [2026-09-06T20:55:53.490Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK klāu ===\"; grep -n \"klāu\" POK_full.txt | head -40\necho \"=== AHD klau ===\"; grep -n -i \"^klau\\|klāu\\|kleu-\" AHD_watkins1985.txt | head -40"
}
```


### [2026-09-06T20:55:53.550Z] TOOL RESULT

```
=== POK klāu ===
=== AHD klau ===
189:Most interesting are the cases where from two or more traditions (usually including Homer and the Rig-Veda) it is possible to reconstruct a poetic phrase or formula con- sisting of two members. Such are the expres- sions ‘“‘imperishable fame,” *klewos ndhg’hitom (kleu-', dhg“hei-); “holy (men- tal) force,” *isorom menos (eis-', men-'); and the “weaver (or crafter) of words,” the Indo- European poet himself, *wek”om teks-on (wek”, teks-). The immortality of the gods (*n-mrto-, from mer-?) is emphasized anew by the vivid verb phrase nek-' tera-?, “to overcome death,” appearing in the Greek word nektar, the drink of the gods. And at least one three-member formula (in the sense of the word in traditional oral poetry) can be reconstructed for the poetic language of prayer, on the combined evidence of four languages, Latin, Umbrian, Avestan, and Sanskrit: “Protect, keep safe, man and cat- tle!” (pa- wi-ro- peku).
638:kleu-1, To hear. I. Extended form *kleus- in Germanic *hleuza- in Old English hléor, cheek (< “side of the face” < “ear”): LEER. II. Zero-grade form *klu-. 1. Germanic *hlustjan in Old English Alystan, to listen: LIsT*. 2. Ger- manic *hlusin6én in Old English Alysnan, to listen: LIs- TEN. 3. Suffixed lengthened form *kli-to- in Germanic *hlidaz, “heard,” loud, in: a. Old English Alid, loud: Loup; b. Old High German Aldti, sound: ABLAUT, UM- LauT. III. Suffixed form *klew-yo- in Greek kleiein, to praise, tell: Cio. [Pok. 1. Rleu- 605.]
639:kleu-2. To wash, clean. 1. Latin clodca, sewer, canal: CLOACA. 2. Zero-grade form *klu- in Greek kluzein, to wash out: CLYSTER; CATACLYSM. [Pok. 2. kleu- 607.] kleu-3. Possibly hook, peg. I. Extended zero-grade form *klud- possibly in Germanic *Aluta-, lot, portion (seman- tic development obscure). 1. Old English Alot, lot: Lor. 2. Dutch lot, lot: LOTTERY. 3. Old French lot (> French lot), lot, portion: LOTTO; ALLOT. II. Suffixed variant form *klau-do- in Latin claudere, to close (< “to lock with a hook, bolt”): CLAUSE, CLOISONNE, CLOISTER, CLOSE, (CLOSURE), (CLOZE); CONCLUDE, ECLOSION, EXCLUDE, INCLUDE, OCCLUDE, PRECLUDE, RECLUSE, SECLUDE. III. Variant form *k/dw-. 1. Suffixed form *kldw-i- in Latin cldvis, key: CEMBALO, CLAVICLE, CLAVIER, CLEF, KEVEL; CLAVICHORD, CONCLAVE, ENCLAVE. 2. Suffixed form *kldw-o- in: a. Latin cldévus, nail: CLOVE!, CLOY; b. Latin clava, club: CLAVATE; CLAVICORN, CLAVIFORM. 3. Suffixed form *k/dw-yo- in: a. Greek kleiein, to close: CLATHRATE; b. Greek verbal adjective kleistos, closed: CLEISTOGAMOUS, CLEISTOTHECIUM. [Pok. k/éu- 604.] klewo-. Bald. Variant *kal(a)wo- in Latin calvus, bald: CALVARIUM. [Pok. k,/ouo- 554.]
1208:ABAFT apo- ABANDON bha-2 ABASE bassus ABASH bat- ABASIA gWa- ABATE battuere ABBREVIATE mregh-u- ABDICATE deik- ABDUCENS deuk- ABDUCT deuk- ABELE albho- ABERRATION ers-1 ABET bheid- ABEYANCE bat- ABHOR ghers- ABIDE bheidh- ABJECT yé- ABJURE yewes- ABLATION  tele- ABLAUT apo-, kleu-1 ABLE ghabh- ABLUTION leu(@)- ABNEGATE ne ABNORMAL gné- ABODE bheidh- ABOLISH al-3 ABORT er-! ABOUND wed-1 ABOUT ud- ABOVE upo ABRADE réd- ABRIDGE mregh-u- ABROGATE reg-1 ABROSIA gWere-4 ABRUPT reup- ABSCESS ked- ABSCISE kae-id- ABSCOND dhé-1 ABSENT eS- ABSOLUTE leu-1 ABSOLVE feu-1 ABSORB srebh- ABSTAIN ten- ABSTRACT tragh- ABSTRUSE treud- ABSURD swer-2 ABULIA gWele-1 ABUT bhau- ABYSS gWadh- ACANTHO- ak- ACANTHOPTERYGIAN pet- ACANTHUS ak- ACAPNIA kwép- ACCEDE ked- ACCELERATE kel-3 ACCENT kan- ACCEPT kap- ACCESS ked- ACCIDENT kad- ACCIPITER Oku- ACCLAIM kele-2 ACCLIVITY klel- ACCOLADE kwel-1 ACCOMMODATE med- ACCOMPLISH pele-1 ACCORD kerd-1 accosT kost- ACCOUNT peu- ACCRUE_ ker-3 ACCUMBENT keu-2 ACCUMULATE keue-2 ACCURATE cira ACERATE ak- ACERB ak- ACETABULUM ak- ACETIC ak- ACETUM = ak- ACHALASIA ghé-
1229:ALLEGE ag-, leg-1 ALLEGORY al-!, ger-1 ALLELOMORPH al-1 ALLERGY werg- ALLEVIATE legh- ALLEY! al-2 ALLIGATOR al-1 ALLITERATE deph- ALLITERATION deph- ALLO- al-1 ALLOCUTION tolkw- ALLOMERISM (s)mer-2 ALLOPATRIC  peter- ALLOT kleu-3 ALLOY leig-1 ALLUDE |leid- ALLUVION leu(e)-
1336:CASE2 kap- CASHIER kes-2 CASTE kes-? CASTIGATE kes-2 CASTLE kes-2 CASTRATE kes-2 CATA- kat-1 CATABOLISM gWele-1 CATACHRESIS gher-5 CATACLYSM kleu-2 CATALECTIC slég- CATALEPSY (s)lag¥- CATALOGUE leg-1 CATALYSIS leu-1 CATAMENIA mé-2 CATAPLEXY plak-2 CATAPULT pél- CATARRH sreu- CATASTASIS sta- CATASTROPHE streb(h)- CATCH kap- CATCHPOLE pau- CATECHIZE (s)wagh- CATEGORY ger-1 CATER-CORNERED kWetwer- CATERPILLAR pilo- CATHEDRA sed-1 CATHEPSIN kat-1 CATHETER yé- CATHODE sed-2 CATHOLIC sol- CATION ei-1 CATOPTRIC okw- CATTLE kaput CAUDILLO kaput CAUDLE kele-1 CAULESCENT kaul- CAULICLE kaul- CAULIFLOWER _bhel-3, kaul- CAULINE kaul- CAUSTIC kéu- CAUTERY kéu- CAUTION keue-1 CAVE keue-2 CAVEAT keue-1 CAVERN keue-2 CAVETTO keue-2 CAVIL  kel-8
1340:CELLA kel-2 CELLAR kel-2 CELLARER kel-2 CEMBALO keu-2, kleu-3 CEMENT kae-id- CEMETERY kei-1 CENACLE sker-1 -CENE_ ken-3 CENOBITE gWei-, kom CENOGENESIS ken-3 CENOTAPH dhembh-, ken-4 Cenozoic ken-3 CENSOR kens- CENSUS kens- CENT dekm CENTAL dekm CENTAVO dekm CENTENARIAN dekm CENTENARY dekm CENTENNIAL dekm CENTER kent- CENTESIMAL dekm CENTESIS kent- CENTI- dekm CENTIGRADE ghredh- CENTIME dekm CENTNER dekm CENTO kentho- CENTRIFUGAL bheug-'
1370:CLAN plat- CLANDESTINE kel-2 CLANG kleg- CLASMATOCYTE kel-1 cLass kele-2 CLAST kel-1 CLasTIC kel-1 CLATHRATE kleu-3 CLATTER gal-2 CLAUSE kleu-3 CLAVATE kleu-3 CLAVICHORD kleu-3 CLAVICLE kleu-3 CLAVICORN ker-1, kleu-3 CLAVIER kleu-3 CLAVIFORM kleu-3 CLAW gel-1
1371:CLAY gel-1 CLAYMORE kel-1, mé-3 CLEAN gel-2 CLEANSE gel-2 CLEAR kele-2 CLEAT gel-1 CLEAVE! gleubh- CLEAVE? gel-! CLEAVERS gel-1 CLEF kleu-3 CLEISTOGAMOUS_ kleu-3 CLEISTOTHECIUM dhé-1, kleu-3 CLEMATIS kel-1 CLENCH gel-1 CLEPSYDRA klep-, wed-! CLERK kel-1 CLEVER gleubh- CLEVIS gleubh- CLEW! gel-1 CLIENT klei- CLIMATE klel- CLIMAX Klei- CLIMB gel-1 CLINAL klei- CLINANDRIUM klei- CLINCH gel-1 CLINE klel-
1374:Cio kleu-1
1375:CLIP? gel-1 CLITELLUM klei- CLoAcA kleu-2 cLop gel-1 CLOISONNE kleu-3 CLOISTER kleu-3 CLONE kel-1 CLONUS kel-3 CLOSE kleu-3 CLOSURE kleu-3 CLOT gel-1
1376:CLOTH peie- cLoup  gel-1 cLouT gel-1 CLOVE! kleu-3 CLOVE? gleubh- cLoy kleu-3 CLOZE kleu-3 CLUB) gel-1
1378:CLUMP gel-1 CLUTCH! gel-1 CLUTTER gel-1 CLYSTER kleu-2 co- kom COADUNATE oi-no- COAGULUM_ ag- COAL g(e)u-lo- COALESCE al-3 COARCTATE ar- coasT kost- COBALT ku- cocciD kokkos coccus kokkos COCHINEAL kokkos COCHLEA konk(h)o- cock? ku- COCKAIGNE kak-2 COCKCHAFER gep(h)-
1389:cons deuk- CONATION ken-1 CONCAVE keue-2 CONCEAL kel-2 CONCEDE ked- CONCEIVE kap- CONCERN krei- CONCESSION ked- CONCH konk(h)o- CONCHA konk(h)o- CONCHO- konk(h)o- CONCIERGE servus CONCILIATE kela-2 CONCISE kae-id- CONCLAVE kleu-3 CONCLUDE kleu-3 CONCOCT pekw- CONCOMITANT ei-1 CONCORD kerd-1 CONCOURSE kers-2 CONCRESCENCE ker-3 CONCRETE ker-3 CONCUBINE keu-2 CONCUPISCENCE kwép- CONCUR kers-2 CONCUSS kwét- CONDEMN dap- CONDENSE dens-2 CONDESCEND skand- CONDIGN dek-1 CONDIMENT dhé-1 CONDITION deik- CONDOLE del-3 CONDONE do- CONDOTTIERE deuk- CONDUCE deuk- CONDUCT deuk- CONDUPLICATE dwo- CONE k6-
1441:EsLis gWela-1 EBULLIENCE beu-! ECBOLIC gWele-1 ECCENTRIC kent- ECCHYMOSIS gheu- ECCLESIA kela-2 ECCRINE krei- ECEsIsS weik-1 ECHARD segh- ECHELON skand- ECHIDNA ang¥hi- ECHINO- ang¥hi- ECHINUS angVhi- ECHO (s)wagh- ECHOLALIA 1a- ECLAIR kelo-2 ECLAIRISSEMENT kelo-2 ECLAMPSIA [ap- ECLECTIC leg-! ECLIPSE leikw- ECLOSION kleu-3 ECOLOGY weik-1 ECONOMY weik-1 ECRU kreue-1 ECSTASY sta- ECTO- eghs ECTOSARC twerk- ECU skei- ECUMENICAL welk-1 ECZEMA yes- EDACIOUS ed- EDAPHIC sed-! EDDY eti EDELWEISS _athal-, kweit- EDEMA oid- EDENTATE dent- EDGE ak-
1456:ENAMEL mel-1 ENAMOR amma ENANTIOMER §ant- ENANTIOMORPH ant- ENARTHROSIS at- ENATE gene- ENCAUSTIC kéu- ENCEINTE? kenk-1 ENCEPHALO- ghebh-el- ENCHANT kan- ENCHASE kap- ENCHIRIDION ghesor- ENCLAVE kleu-3 ENCLITIC klei- ENCOUNTER kom ENCROACH ger-2 ENCYCLICAL kwel-1 ENCYCLOPEDIA pau- END ant- ENDEAVOR ghabh- ENDEMIC da- ENDERGONIC werg- ENDOCARDIUM kerd-1 ENDOCRINE krei- ENDOERGIC werg- ENDORSE dorsum ENDOSTEUM ost- ENDOTHECIUM dhé-1 ENDOTHELIUM dhé@(i)- ENDOW do- ENDUE deuk-, eu-1 ENDURE deru ENEMA yé-
1485:EXAMINE ag- EXAMPLE em- EXANTHEMA andh- EXARCH arkhein EXCALIBUR kal-3 EXCAVATE keue-2 EXCEED ked- EXCEL kel-6 EXCEPT kap- EXCERPT kerp- EXCISE? kae-id- EXCITE kei-3 EXCLAIM kela-2 EXCLUDE kleu-3 EXCORIATE sker-1 EXCREMENT krei- EXCRESCENCE ker-3 EXCURSION kers-2 EXECRATE Sak- EXECUTE sekw-1 EXEDRA sed-1 EXEGESIS sag- EXEMPLARY em- EXEMPLIFY em- EXEMPLUM em- EXEMPT em- EXERCISE arek- EXERGONIC werg- EXERGUE werg- EXERT ser-3 EXFOLIATE bhel-3 EXHAUST aus-2 EXHIBIT ghabh- EXHILARATE sel-2 EXHORT gher-5 EXHUME dhghem- EXIGENT ag-
1676:INCIDENT kad- INCINERATE keni- INCIPIENT kap- INCISE kae-id- INCITE kei-3 INCLINE klei- INCLUDE kleu-3 INCONDITE dhé-1 INCREASE ker-3 INCUBATE keu-2 INCULT kWwel-1 INCUMBENT keu-2 INCUNABULUM kei-1 INCUR kers-2 INCUS kau-2 INDEMNIFY dap- INDEMNITY dap- INDENT! dent- INDENTURE dent- INDEX deik- INDICATE deik- INDICT deik- INDIGEN gene- INDIGENOUS gene- INDIGENT eg- INDIGN dek-1 INDIGNANT dek-1 INDIGNATION dek-1 INDITE deik- INDOLENT del-3 INDOMITABLE deme-2 INDUCE deuk- INDURATE deru INDUSTRY en, ster-2 INEBRIATE 6g¥h- INEFFABLE bha-2 INELUCTABLE leug-1 INEPT ap-1
1711:KEEL’ gel-3 KEELHAUL kele-2 KEELSON ku- KEESHOND kwon- KEN gno- KENNEL! kwon- KENNING gno- KENO penkwe KENOSIS ken-4 KERATIN ker-! KERATO- ker-1 KERCHIEF kaput KERF gerbh- KERMES k*rmi- KERN! kat-2 KERNEL gre-no- KEVEL kleu-3 KEY? kagh-
1739:LEAGUER! legh- LEAK leg-2 LEAN! klei- LEAP klou- LEARN leis-1 LEASING leu-! LEAST leis-2 LEATHER letro- LEAVE! leip- LEAVE? §leubh- LEAVEN legWh- LECHER leigh- LECTERN leg-1 LECTION leg-1 LECTURE leg-' LEDGE legh- LEDGER legh- LEE kele-1 LEECH! feg-1 LEECH? leig-1 LEEK leug-! LEER kleu-! LEES legh- LEGACY leg-1 LEGAL leg-1 LEGATE leg-1 LEGATO leig-1 LEGEND leg-1 LEGERDEMAIN leg¥h- LEGIBLE leg-1 LEGION leg-1 LEGISLATOR leg-1, tele- LEGIST leg-1 LEGITIMATE leg-1 LEITMOTIF leit-2 LEMAN leubh- LEMMA! (s)lag¥- LEMMA? lep-t LEMURES_ lem-2 LEND leikw- LENGTH del-1 LENIENT [6-2 LENIS [6-2 LENITIVE |@-2 LENITY 16-2 LENT del-1 LENTO lento-, lep-1. LEPIDO- lep-1 LEPIDOTE lep-1 LEPRECHAUN kWrep-, legwh- -LEPSY (s)lag¥- LEPTO- lep-1 LEPTON! lep-1
1753:List! leizd- List? leizd- LIis™ kleu-1 LisT5 las-
1754:LISTEN kleu-1 LITER fithra
1767:LoT kleu-3 LOTION leu(@)- LOTTERY kleu-3 LoTTo kleu-3 Loup kleu-1 LOUGH laku- LOUP-GAROU_ wi-ro-, wIkwo- LOUSE lis- LouT! leud- LouT? leud- LOVE leubh- Low! legh-
1952:OBEY au-5 OBFUSCATE dheu-1 OBITUARY el-1 OBJECT! yé- OBJURGATE ag-, yewes- OBLAST epi, wal- OBLATE! tele- OBLIGE leig-1 OBLITERATE deph- OBLIVION lel- OBLONG del-1 OBLOQUY tolkw- OBNOXIOUS nek-1 OBOE busk- OBSCURE (s)keu- OBSEQUIOUS sekw-1 OBSERVE ser-! oBsEss sed-1 OBSTACLE sta- OBSTETRIC sta- OBSTINATE sta- OBSTREPEROUS §strep- OBSTRUCT ster-2 OBTAIN ten- OBTECT (s)teg- OBTEST trei- OBTRUDE treud- OBTUND (s)teu- OBVERT wer-3 oBvious wegh- OBVOLUTE wel-3 OCARINA awi- OCCASION kad- occipuT kaput OCCLUDE kleu-3 occuLT kel-2 occupy kap- occur kers-2 OCELLUS okWw- OCHLOCRACY wegh- OCHLOPHOBIA wegh- OCTAD okto(u) OctTans okt6(u) OCTANT oktd(u) OCTAVE okt6d(u) OcTAvO okt6(u) OCTENNIAL at-
2129:PRECINCT kenk-! PRECIOUS per-6 PRECIPITATE kaput PRECISE kae-id- PRECLUDE kleu-3 PRECOCIOUS pekw- PRECURSOR kers-2 PREDATORY ghend- PREDECESSOR ked- PREDICATE delk- pRepicT deik- PREDOMINATE deme-1 PREEMPTION em- PREFACE bha-2 PREFECT dhé-1 PREFER bher-1 PREFIGURE dheigh- PREFIX dhig¥- PREGNABLE ghend- PREGNANT! gene- PREGNANT? per-5 PREHENSILE ghend- PREHENSION ghend- PREJUDICE deik-, yewes- PRELAPSARIAN leb-1 PRELATE telo- PRELECT leg-1 PRELIBATION [éi- PRELUDE leld- PREMATURE ma-1 PREMIER per! PREMISE (s)meit(@)- PREMIUM em- PREMONITION men-1 PREMORSE mer-2 PREMUNITION mel-3 PREPARE pere-! PREPENSE (s)pen- PREPONDERATE (S)pen- PREPOSITION apo- PREPOSTEROUS apo- PREPOTENT _poti- PREPUCE pu-! PREROGATIVE reg-1 PRESAGE sag- PRESBYOPIA per! PRESBYTER pert PRESCIENT skel- PRESCIND  skel- PRESCRIBE skribh- PRESENT! es- PRESENT? es- PRESENTIMENT sent- PRESERVE ser-! PRESIDE sed-! PRESS! per-5 PRESSURE per-5 PRESTIGE streig- PRESUME em- PRETEND ten- PRETERIT el-1!, per? PRETERMIT (s)melt(@)- PRETEXT teks- PRETZEL mregh-u- PREVAIL wal- PREVENIENT gWa- PREVENT gWa- PREVIOUS wegh- PREVISE weld- PREY ghend- PRICE per-6
2174:REBUT bhau- RECALESCENCE kele-! RECANT kan- RECAPITULATE kaput RECEDE ked- RECEIVE kap- RECENSION kens- RECENT ken-3 RECIDIVISM kad- RECIPROCAL pert RECISION kae-id- RECK reg-1 RECKLESS reg-! RECKON reg-1 RECLAIM kele-2 RECLINE klei- RECLUSE kleu-3 RECOGNIZE gnd- RECOIL (s)keu- RECOMMEND man-2 RECONDITE dhé-1 RECORD kerd-1 RECOURSE kers-2 RECOVER kap- RECREANT kerd-1 RECREMENT krei- RECRIMINATE  krei- RECRUDESCE kreud-! RECRUIT ker-3 RECTANGLE reg-1 RECTIFY dhé-1, reg-1 RECTILINEAR reg-1 RECTITUDE reg-!
2230:sEccO seikw- SECEDE ked-, s(w)e- SECERN krel-, s(w)e- SECLUDE kleu-%, s(w)e- SECOND2 sekw.-1 SECONDO sekw-1 SECRET krel-, s(w)e- -SECT sek-, sekw-1 SECTILE sek- SECTION sek- SECTOR sek- SECUND sekw-1 SECUNDINES sekw-1 SECURE cilirra, s(w)e- SEDATE! sed-1 SEDENTARY sed-1 SEDERUNT sed-1 SEDGE sek- SEDILIA sed-1 SEDIMENT sed-1 SEDITION ei-1, s(w)e- SEDUCE deuk-, s(w)e- SEE] sekw.2
2433:UMBRA andho- UMBRELLA andho- UMLAUT ambhi, kleu-1 uN-l ne
```


## [2026-09-06T20:55:54.815Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== IEC klis ===\"; grep -n -i \"klis\\|kleis-\\|ḱleiḱ\" IEC.txt | head -40\necho \"=== CHEUNG sraiš ===\"; grep -n -i \"srai\\|sriš\\|srēš\" CHEUNG.txt | head -40"
}
```


### [2026-09-06T20:55:54.877Z] TOOL RESULT

```
=== IEC klis ===
336:akolos, akilos, aklos “point, spike, sting’. Cf. aKil-, aKul- OHG (ambig.) agal- in agal-stra (G. Elster); Li. aklys; Latv. aklis, beside akles, ak]i
659:aquilios ‘spike, thorn, prong’. Cf. akulos. WP I, 29 Lat. aculeus (ambig. cf. aKulos); W ebill; Cor. ebyl; Br. ébil, ibil “peg, nail, aw; OE awel ‘fork, hook’; Latv. aklis ‘gadfly’
1752:Big. brúsde “plough-point'; Li. cf. bruzdùklis ‘peg.
3325:dhurkos, à ‘stab; spike, prong’. Cf. WP I, 802. Cf. bhrkos, dhuró Arm. durk 'dagger:; Gk. cf. türkhe “(“fork?, if. fr. *thurk&); (Lat. furca ‘fork’, and forco "plough-point' are ambig. See bhrk-); Ir. duirc, pl. -eanna (fdirk, whence EME dork, Scots durk, id.); Cz. drk 'stab'; drkati, v. id.; Li. cf. dür-klas (‘bayonet’, prob. fr. *dhur-dhlom, but ambig.); Latv. durklis, id. (and 'prong?)
4076:glidsko (?). Cf. glid- Lat. glisco, Ere; G klitsch-ig “sticky, doughy’; Du. klis ‘bur’; Norw. kliss ‘sticky mess”; klisse ‘stick’. (OHG klétta “bur” represents a variant *elidh-)
4099:glisdh- ‘cluster, clump, mass’. Cf. glisteros Gk. á-glis, gs -glithos ‘clove of garlic”, fr. - *sm-°); Hes. cf. (Maced. or Thrac.) a-glidia *earlic-cloves'; Latv. glizda ‘clay, marl’; cf. EMDou. (*-i-) klis, klisse-kruid, klitte “bur”; klissen ‘adhere’; Du. klis (also = ‘tangle, knot")
4101:glist-, glisteros ‘adhesive’. WP I, 620 Mod. Gk. glisterós 'slippery, smooth'; cf. also Gk. glískhros 'gluey; MHG klister ‘glue’; OCS glista ‘tapeworm’; Srb. glista ‘worm’. Isophonic forms are S. Alb. glisht, Alb. gisht ‘finger’ and LGer. kliste ‘thwart on raft?
6732:kankol- (1) ‘rod, bar, rib, string of instru- ment’. Cf. konkəl-. (Much of the evidence is ambig.). Cf. WP I, 400 Skt. cf. kankalah ‘skeleton’; kankellih “ashoka- tree’; Gk. *kagklís (?) usu. kigklis ‘grille’ be- side kágkelon ‘bar’; Lat. LW cancelli, LW also in Br. kael, kili ‘railing, hurdle, trellis’; ON hail, m. (‘peg, pin’, or to kankəl- (2)?); Li. kankuolys (‘bell-clapper’, isophonic w. Skt. kankalab) beside kañkalas, id. (& ‘knocker’); Latv. kokle, pl. “zither, cymbalon, harp’; Li. kafikles “primitive zither'
7351:kliKo, io (?) ‘squeeze, twist. WP I, 492 Skt. klisSyami “torture, force’; Li. cf. klisas ‘crippled’; klystu, -ti ‘get crippled'
7483:knk- (2) (konk-) ‘haunch, hock, hip’. Cf. WP I, 401 & II, 599 Gk. cf. podo-káke ‘fetter, hobble’; OE cf. hóh (*hock, heel", fr. *konk-); Srb. kük (:haunch', fr. *konk-); Li. kinka ‘shin’; Latv. cf. Cinklis, dial. "Achilles tendon’
7808:krop ‘torture’; R kropát, v. ‘botch, mangle? kraps- ‘grab, snatch; rapacious; grab, sei- zure’ Br. krafa ‘seize, snatch; scratch, engrave’; kraf ‘seizure’; kraf, m. ‘stylus’: kraf, krav ‘stitch’; W craff ‘quick, keen; secure’; m. pl. -au ‘clasp, cramp’; craffu, v. ‘secure, grip’; Cor. crafa, v. ‘grip’; crāf, adj. ‘tenacious’; s. pl. crafow "basting-stitch"; cf. crefny, adj. ‘grasping, gree- dy’; OE hrespan ‘strip, despoil’; hresp ‘spolia- tion’ krās- (?) ‘glory, praise’ ON hrósa, v. ‘praise’; hrósan, f. ‘praise; boast- ing’; hræsni, f. id.; mod. Icel. hrós, n. ‘praise’; OCS krasa ‘beauty’ (and com. Sl.); Latv. cf. krāšns 'splendid'. See Supt. K : krās- (krast-, see karst-). Variant in W cras ‘toasted, parched, arid’; Br. kraz, id. krateið ‘overpower’. See kratos Gk. kratéo ‘rule’; OCS krostọ, krotiti (tame' and com. Sl.) kratos, is, us “strong; strength, power, force’. WP I, 354 Skt. krátuh “power, will, ability’; Av xratus ‘wisdom’; Ober xraQu-, id.; Gk. kratüs *power- ful”; krátos, n. ‘power’; W crad, craid, m. (“vig- our, force’, fr. *kratos, *kratis); OHG hrad ‘swift; OE hrad “swift, active; ON hraór, id.; OCS cf. krotükü ('tame', lit. overpower- ed"). Isophonic: Li. kratüs (rough, uneven’ krátos, à, is 'enclosure, envelope” W crawd “coating, surface’; OE hréóa 'goat- skin cover, mantle’; cf. hroó-girela ‘crown’; Li. krótai, krótos, mfpl. "lattice, grille’; Latv. krats ‘cage, prison’. (W and OE ambig.) kratsos, ios (?) Lat. crassus ‘fat, gross’; ON hress “hale, hear- ty’; hressa, Lat v. ‘cheer’ (kraug-, variant of krauk-, q. v.). (WP I, 417, 477 & II, 573) Hes. kraugós ‘woodpecker’; Gk. kraugé ‘croak, caw’ krauk- ‘caw, croak; crow, raven’. (Variant: krauk-) EMAIb. krak, mod. krrak ‘a bird of crow type’; OE hrēa (Crumble in the bowels’? Cf. hream ‘uproar’, fr. *kraukmo-?); Pol. Ukr. kruk ‘raven’; Latv. kraukjs ‘rook’ beside krauklis
7918:krik- (krik-) ‘screech, creak, scream’. Cf. WP I, 416. Onomat. Gk. cf. aor. é-krikon “I shouted’; Alb. cf. krisje “bang, crack? beside krísun, pp. (if < *krikio-); (OFr. criquer ‘creak: chirrup' is non-historical onomatopoeia, as also Nor. Fr. criquet “cricket insect); W crig, m. ‘crack’ beside crygu (‘be hoarse’: *-1-/-i-); cf. criciad, cricell, f. “cricket insect’; OCS krico, -ati shout? and com. Sl.; krikü, kričí, m. id.; Cz. křičet “shout? beside kfecet ‘screech’ (*-1-/-i-); Li. krykiü, krýkti “cry, screech?’ beside kriksiu, eti, id. (*-1-/-1-); cf. krykie, f. ‘wild duck’; Latv. cf. krikis "out: cracker bird’ beside krīklis and krikis ‘teal (*-1-/-i-)
8019:krükilis (krüklis), ios ‘throat, gorge’ W crigell, m. ‘ravine’; Latv. krūklis ‘larynx’; Li. cf. krūkiu, ti, v. beside kriūkiu, ti ‘grunt’
8294:kükilos, is (küklis) ‘tip, point, peak, knob, protruberance'. Cf. kukos and kükos, on Alb. kikél, f. ‘tip, point; ELG Hügel (“hilP > HG, id.); Cz. kyCel, m. kyčle, kyCla, f. *hip- bone”; Latv. cf. kükums ‘hump’
10510:mek- (mék-) ‘bleat, stammer, utter Gk. (*-e-) mekáomai, v. ‘bleat; W meg, f. (D ‘utterance’; Srb. Croat mečim, -ati ‘bellow’: Cz. mecet, inf. *bleat'; Li. cf. mekis, meklis, m. 'stammerer'; Blg. mèča, v. ‘mew’
10805:mimeio, mimiio ‘bleat, wail’. Cf. meio (1). WP II, 243 Skt. mimàmi, mimiye, id.; Hitt. cf. memahi ‘speak’; Gk. mimízo ‘neigh, bleat’; (mimeo- mai ‘mimic’ unrelated, cf. smiio); Br. cf. émé- zun, 1sg. ‘I say; OCS mimatt (or mümati?), inf. ‘stammer’; (onomat. basis also of Li. me- meklis *stammerer)
11262:mrk- (2) ‘twinkle, blink, shine’. Cz. mrk, m. ‘blinker; blink’; mrkat, mrknout, v. “blink”; R cf. mercàť, inf. ‘glimmer, glint’; Latv. cf. mirklis, Li. mirka, f. “blink”
13817:putlos (phutlo-) “fizzy, frothy, puffy, windy, airy, vacuous’. Cf. putos, pūst- Arm. (ambig.) pul, gs: plo, o-st. (crumbling, tottering’, cf. pül- (3)); Gk. cf. phusalís, f. “bladder”; phüsalos, m. toad"; Li. putlüs, adj. ‘puffy, flabby, weak’; Latv. cf. puteklis, s. ‘dust’?
17284:stok- (sthok-) “strike, jab, stab’. (Skt. & Balt. ambig. Cf. sthak-) Skt. stakami, v. “dash against; Arm. tak, Get, ‘mallet’; Br. steki, pp: stokit, v. ‘jolt, poke’; stok, pl. -u, m. id.; Li. stakē, f. ‘barb’; Latv. cf. staks, m. ‘beaten flax’; staklis, s. ‘prong’. (Iso- phones: W sog, f. ‘wallowing’; soga, inf. “wal- low’; Arm. V ok ‘warp’). (For differentiation of Arm. -0- and Arm. -a-, see SEM: Arm. & IE, §§ 33, 33a)
17564:stháuoros (variant of sthauros (sthouros) above, and of stheuros, stheuoros Skt. sthávaráh, adj. ‘firm, strong’; Av. cf. stavro, id. & OPer. ustuvar, id.; Skt. (variant) sthavirah "old: Gk. (ambig.) cf. stérízo, v. ‘fix beside au-stérós (‘harshb’. Ambig. cf. sthar-); Latv. cf. stavoklis, s. *post
19427:tuerolos, is ‘turner, twister’. Cf. tuer- (3) Lat. ambig. ferula, f. ‘stick; giant fennel’; OE pwiril, m. 'churning-stick, dolly’; LG dwirl, m. *pegtop'; G dial. Dorl, id. beside G Quirl, m. 'twirling-stick'; Li. tvéralas, m. “band, bandage’; Latv. cf. tvereklis, s. "band. mill
20054:uerĝh-, alternative to uerĝ- (1), q.v. (Balto- Slav. ambig.). Cf. uergho (1) ON virgill, m. ‘halter; MHG wergel, m. (Cstrangler, fr. *uorghil-); Blg. vrěž, vrěža, f. ‘tendril’; Li. verzle, f. 'screw-nut'; verZe- klis, m. id.; Latv. verzeles, pl. ‘trappings’; Finn. LW verkko ‘net, web’. (Isophones:
=== CHEUNG sraiš ===
9648:wix" ad ‘to open, unlock’ (diff. EVS, l.c., s.v. *srai), Wa. wsers(br)y-/w»bis(2)n- ‘to let 
23191:*srai ‘to lean’ 
23198:(V 3.20, ViD 2); Pres. {2} them.: INJ. med. 35р. YAv. ира... sraiiata (Yt 17.21), IMPV. 25р. ҮАУ. upa... 
23199:sraiian'ha (Yt 17.21); Fut.: IND. 3sg. YAv. sraesiieiti (V 8.34); Aor. athem.: INJ. med. 3sg. YAv. nisrita 
23200:(Y 65.11); Perf.: IND. 35р. ? YAv. sisraiia (Vyt 51); Partic.: pres. {2} med. YAv. apa.sraiiamna- (Yt 
23201:13.26), fut. ҮАУ. sra@Siiant- (У 8.34), aor. med. Y Av. sraiiana- (V 3.29, Vyt 36), perf. pass. YAv. srita- 
23205:*srais 355 
23214:*KHOTANESE: Q LKh. ssaidä, assigned by Bailey (DKS: 412a f.) to *srai, has a 
23215:different etymology, on which see *srai8. 
23228:phonetically impeccably to Old Ir. *ui-, *aua-srai(a)-". 
23244:*sraiS ‘to put together, attach’ 
55306:*kas?, *rag, *srais, жас? 
55862:(s.v.), *par? (s.v.), *srai 
56022:*ha(n)j, *rag, *srais (s.v.) 
56737:*srais (s.v.) 
57049:*srai 
57506:*srais
```


## [2026-09-06T20:56:02.641Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== CHEUNG srais entry ===\"; sed -n '23244,23330p' CHEUNG.txt\necho \"=== POK 604 area ===\"; grep -n \"klēu-\\|klāu-\\|klāu̯i\\|Haken, krummes Holz\" POK_full.txt | head -20"
}
```


### [2026-09-06T20:56:02.702Z] TOOL RESULT

```
=== CHEUNG srais entry ===
*sraiS ‘to put together, attach’ 


*AVESTAN: (+ *ham-) YAv. ham.sris- ‘to put together’ — Liste: 66 

Aor. them. (s- ?): SUBJ. 3sg. YAv. ham.srisäiti (N 99) 

*MIDDLE PERSIAN: BMP slš- /sris-/ ‘to mix, knead’ 

*PARTHIAN: srysysn ‘mixture’ {hapax} = DMMPP: 309b 

*KHOTANESE: LKh. sis- (sais-) ‘to take hold of? || (+ *ni-) OKh. näsäs- ‘to attach, 
adhere’ — SGS: 130 

*CHORESMIAN: (+ *pati-) ? pš- ‘to put together, lean towards’ = Samadi: 163 

*NWIR: NP siristan/sirés- ‘to mix, mingle; knead’, Gz. siris-/sirist ‘to knead the 
dough’, NP sirism ‘glue’ 

*NEIR: Oss. І. sasm, D. sans ‘glue’, ? I. sis, D. ses ‘wall’ || (+ *ni-) Pash. nxat-/nxal- 
‘to cling, stick’ 

*SANSKRIT: Sres ‘to cling, stick, be attached, hold’ (RV) = EWAia II: 670 

© This Пг. root has no certain IE cognates. 

*REFERENCES: EVP: 53; DKS: 410a, 187a; Abaev, Slovar’ III: 37 f., 113 Е; WIM II/1: 82; Werba 1997: 
246; Cheung 2002: 222; NEVP: 60 


356 *srasé 


*srasó ‘to drip’ 

*AVESTAN: YAv. srasc- ‘to drip’ — Liste: 66 

Pres. them.: IND. med. 3pl. YAv. srascintaé ° (Yt 5.120); Partic.: pres. YAv. srascint- (Yt 16.9, V 3.29, V 
6.36); Caus.: OPT. 3pl. YAv. visrascaiion (V 7.29 ff.) 

*CHORESMIAN: (?) cš- ‘to drip’ (<< *Sasca- < *ѕгаѕса-) = Samadi: 52 

*NEIR: Wa. Sac-/Sact- ‘to seep, drip, leak (away)’, (caus.) $әс(ы)у-/$әсоуа- ‘to aim; 
to filter’, Pash. cacadal ‘to leak, drop, fall in drops’ (with affric. assimil.) || (+ *ni-) 
Yi. noxé-/noxcai, M. nič- ‘to drip, drop from the eaves’ 

*MISC: Arm. (LW ?) srskel ‘to sprinkle’ 

9 An IE origin for this root is difficult to ascertain: it may be expressive or onoma- 
topoetic. Similar forms are well attested in Balto-Slavic: Lith. Slakéti ‘to drip’, 3lékti 


‘to sprinkle’, Latv. slacit ‘to make wet’, Russ. s/jakot’ ‘sleet’, Lith. släkas ‘drop’ 
*REFERENCES: EVP: 16 f.; IFL П: 349, 234b; Steblin-Kamenskij 1999: 349; Lubotsky 2001: 40 


*sra0H ‘to loosen’ 

*NEIR: Sh. (Baj.) Xá0- ‘to be lazy, slacken’ 

*SANSKRIT: srath' ‘to become loose, to give way’ (RV+) = EWAia II: 662 

Ó The existence of the Ir. cognate root of Skt. srath' is uncertain, in the absence of 
other Ir. continuations. It is impossible to draw any conclusions from a form attested 
in a single Pamiri language. 

*REFERENCES: EVS: 104a; Werba 1997: 412 f. 


*srau ‘to hear, listen’ 

*AVESTAN: srao- ‘to hear, listen’ || (+ *abi-) ‘to hear, understand’ || (+ *upa-) ‘to hear 
upon, understand’ || (+ *fra-) ‘to be heard, known [pass., impers.]’ || (+ *ui-) ‘to 
learn, hear from’ = Liste: 66f. 

Pres. nu-: IND. 3sg. YAv. surunaoiti (Yt 10.107, FrW 10.41), 3sg. them. YAv. (auui) surunuuaiti (N 24, 
N 60), 3р1. YAv. ()upa.surunuuainti (N 21), ОРТ. Zeg. YAv. surunuiia (Y 68.9); Aor. {1} athem.: IND. 
med. 3р1. OAv. asruuätom (Y 30.3), med. 2р1. OAv. asrūdūm (Y 32.3), SUBJ. 3sg. YAv. srauuat (F 12), 
OPT. 1р1. OAv. srouummä (28.7), IMPV. 35р. OAV. sraotü (Y 45.6, Y 49.7, Y 49.9), 2р1. OAv. sraota (Y 
30.2, Y 33.11, Y 45.1); Aor. {2} s-: SUBJ. med. 15р. OAv. soraosane (Y 50.4); Perf.: IND. med. 15р. 
Y Av. susruiie (Yt 17.17), 1р1. sūsrūma (Yt 13.148); Partic.: pres. surunuuat- (Y 35.4, Yt 8.3, cf. Panaino, 
Tist. П: 91), caus. YAv. sräuuaiiant-, med. Y Ау. sräuuaiiamna-, desid. Y Av. susrusomna- (Yt 14.21), aor. 
{1} YAv. aiBisr(a)uuana- (V 3.40), aor. {2} them. YAv. sraosomna- (V 13.17 Ё), perf. pass. YAv. srüta- 
(N 37, Y 22.25, Y 25.6, etc.), OAv. frasrüta- (Y Y 50.8), YAv. frasrüta- (Y 27.7, Y 65.3, Yt 8.2); Inf.: 
pres. caus. OAv. sräuuaiienhe (Y 29.8), YAv. sräuuaiieiöiiäi (Vyt 46), aor. OAv. srüidiiai (Y 34.12, Y 
45.5); Pass.: pres. IND. med. 1sg. OAv. sruiie (Y 33.7), INJ. 3sg. YAv. visruiiata (Yt 13.91), aor. INJ. 
3sg. OAv. srauui (Y 32.7 f., Y 49.7, Y 49.9); Caus.: pres. IND. 35р. YAv. srauuaiieiti (V 18.9, N 26, 
=== POK 604 area ===
```


## [2026-09-06T20:56:04.525Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD sreš/srišt ===\"; grep -n -i \"sre[sš]\\|sri[sš]\\|srišt\" PHD.txt PHD_mackenzie.txt | head -30\necho \"=== NYB ===\"; grep -n -i \"sri[sš]t\\|srē[sš]\\|sriš\" NYB_vol2_glossary.txt | head -30"
}
```


### [2026-09-06T20:56:04.590Z] TOOL RESULT

```
=== PHD sreš/srišt ===
PHD.txt:568:spas dāštan, ~ hangárdan: thank, give thanks. spās-dār [sp?sd?] | N sip~] grateful, thankful. ~ih: gratitude. spās|-ešnās [sp’ssn’s] grateful. —ómand [-’wmnd] grateful. spas [sp = Av. 0Bàsa-] space, atmosphere. spaxr [sp?hl | M ‘spxr, N *siparx] merrymaking, revelry. spazg [spzg | (M ‘spgj), N sipazg-] slanderous. «il: slander. spëd [spyt! | M ‘spyd, N sapéd] white. ~ag [-k! | N -a] white (of egg, etc.). —bàg [-p’k!' | N -bā] curd soup. --dàr [-?1 | N -dár] white poplar, aspen. spenag [sp(y)m?k! = Av. spanta-, cf. $annág] holy. ~ ménóg : the Good Spirit. Spig [spyk' | M ‘spyg, (N sapriy)] т. brilliance; 2. sprout, shoot. spihr [spy(y)hl | (M ‘spyr), N sipihr] sphere, sky, firmament, fate. ~ig [-yk'] heavenly. spinjanagih [spne’nkyh] hospitality. spiš [spyš | (N šipt$)) louse. Spitāmān [spyt?m?^n] of the Spitama family. spiz- [spyc- | M “рухіп, *spyz-] 1. shine; 2. sprout. —išn: 1. brilliance; 2. sprouting. spöxtan, spēz- [spwhtn', spwc- | M *spwxt, N sip~] thrust; overstep, disobey; delay, reject. ~išn: delay, rejection; disobedience. SpOz [spwe | N sipóz] disobedience; delay. ~gar LEIT N ~] disobedient; dilatory. sprahm(ag) [splhm(k') | M *sprhm(g), N siparham] flower, fragrant herb. spul [spwl] spleen. spurdan, spar- [spwiltn', spl- | N sip~] tread, trample. spurrig [spwlyk!' | (M ‘spwr), N sipari] entire, complete, perfect. ~ith: completeness, perfection. spurz [*spiz | P “spwrz, N sipurz] spleen. srat (sit! | cf. Ar. sirát] street. sraw [s/wb'] word, spell. srawénidan, srawén- [slwbyn-ytn'] report, broadcast. sraxtag [s/htk! = Av. sraxti-] side, part. sray [sd | N saray] house, hall. Igrāy-, -išn, v. srüdan. srāyīdan, ?sráy- [sPd-ytn! = Av. @rdya-] protect. ~išn: protection. srešk [sl(y)£h | (P srsk), N sirifk] drop, tear. srištan, *srēš- [s/szn! | P sryi-, N sir-~] mix, knead. sri$wadag [s/ystotk! = Av. Oriswa-] a third. sréd [s/zvt! | M srwd, N suród] song.
PHD.txt:1699:drop passing, paššinjag, srešk.
PHD.txt:2532:knead srištan.
PHD.txt:2830:mix abyóxtan, améxtan, guméxtan, srištan.
PHD.txt:3944:tear (n.) ars, sreški%v?
PHD.txt:4782:gáy- gādanī wattart wattarīh! srawēn- srawēnīdan srūwēn ` sarw, sraw, srü srūwar sarw bar-! burdan! srub srubén Srūš srūšīg srūd srūdan sarmāg srub srešk srištan sardīh sard, srat
PHD.txt:4790:srāy l?syáy- srāyišnīh srāyišn sarāsar srayidan sraxtag wad! sargén srišwadag
PHD.txt:4791:srešk
PHD_mackenzie.txt:4642:sristan, ·srM· [slftn' I P sryf-, N sir-] mix, knead.
PHD_mackenzie.txt:4643:sriswadag [slyftvtk l = Av. 6rifwa-] a third.
PHD_mackenzie.txt:6926:iron ahan; (a.) ahanen.                    knead sristan.
PHD_mackenzie.txt:7111:  sristan.                                     mussuck mask; small ...... maskizag.
PHD_mackenzie.txt:7752:tangible girisnig, griftaromand.          third sidig; -seyom; (n.) sriswadag.
PHD_mackenzie.txt:7764:tear (n.) ars, sreSkt,L~~                    siderati011.
PHD_mackenzie.txt:9012:sristan
PHD_mackenzie.txt:9019:sard, srat                  \~        sriswadag            ,~tD~
=== NYB ===
505:lapar [’pl; MDM, v. 2apar] adj. situated above, lying above: évak ~, apäk dit, v.s.v. žapāk (2); — heavenly, often in compounds: apar-apükeh etc., v. below; comp. ~-tar [’pltl] higher 5426, 581°, highest 1097; sup. ~-tom highest 415. 102°; v. also apartaréh; — adv. empha- sizing an adj.: highly, extremely: apar- aržānīk, v. aržānīk. — Av. (393) upara-, adv. upara (instr.), uparam; MPrth ’br adj. and adv. (MHC), comp. ’brdr, sup. ’brdwm; Ps. ?pldl; Paz. awartar, awardar (SGV); NP bar ‘height, top, summit’, bartar ‘higher’. ?apar [MDM, erroneous reading of OAram QDM] 1. adv. above: (3 päs) i-m guft ~ of which I spoke above 65°; či nümak" cé hac ~ nipišt" éstat the inscription that had been written here above P2:3, cf hacapar; — prev. over, on, upon, up, or simply expressing the initiation of the action, with varying vbs., cf esp. (@)ma- tan, burtan, grätan, raftan, rasitan ; follow- ed by enclitics: apar-p-im ravišn I must needs ascend 4076, v.s.v. -p(i); — refer- ring back to an encl. pron.: api-š Vidrafš . ~ mšast and V. got on it (the horse) 25W5; cē-t avdom margéh ~ raset for at the end Death will come upon thee 726-7; (martömän) tāi-šān āmēcišn ~ nē barend as long as one does not impart instruction to them 801. — 2. prep. a) local: over, on, on to, down on: Krisäsp ~ én damik raset K. is roaming all over this earth 3318; ~ giyāk on the spot 3", 102; ~ ki Zartuxst bé dahém where we shall deposit Z. 3957; ~ pad ēstāt rose to his feet 1821; asp ... — rahy vartét harness the horse! 5418-14; srišk ~ srišk drop after drop 214
1993:the opposite of Vahuman 654-5; Srēš his chief adversary 665. 7711, 2516, 2814 v.s. v. distak; — his epithets: mūtak and tanäpuhrak 619%; zürdrus 7211-12, 103977; v. these ws. — Av. (35 sq.) aēšma- (Asmodatos, Book of Tobit 3:8 Av. ačšmo.dačva-); MPrth ‘smg’n ‘devils of wrath’; MPrs xysm; Paz. NP rašm, zism.
1997:hihréh [hslyh] impurity, filth 9319-21, 9424, — Av. (1812) hixra- ‘fluid secretion of the body’. The passage 9319-?! also in BdA p. 918-%, where hdl = Air (but Cod. DH hyhl = hizr). As to the spelling -sl- for -hr- cf s. v. srišvatak.
2556:mihr [mtr'] 1. n. pr. the Aryan god Mitra, Av. Midra: ~u Srēš u Rasn 1215; ~ u Zurvān i akanārak u menčyč datistan 77-12, ~ zg"'"atài névak, Dahman Afrin 9213, ~ yazét u x"aršet 961! ; atur burzen ~ the third of the three imperial fires 11%. 2°, symbolizing the class of the cattle- breeders and farmers 2° (cf Av. [1430] Midrē yö vouru.gaoyaotiš); — existing in all animal beings 965-%; — Dadv pat ~ the name of the 15th day of the month 9715-16, — 2. the sun 78. 317. 7913-18, — 3. abstr. friendship, loyalty: — u došaram i apāk čišan 87°; ~ + amāh 98; ~ i čvak 6 dit 119; vehän ... ~ däst u dosteh varzit 5526-27, — Av. (1183 sqq.) midra-.
2783:4321, 4874, 4912.25, 548.10, 10917; srišk srišk drop by drop incessantly 412°,
3510:srišk [slyšk'; slšk'] drop 211. 412°, 8920, — Av. (1645) sraska- 'tear'; MPrth srsk (List 87); NP sirisk.
3511:srišvātak [slySw^tk', slsw’tk', slšwtk'] a third 41°. 1022-19, — Borrowed from Av. (812) Ortšva- ‘a third’ enlarged with a Phl. element (tak 'leap, run', g.v., — length covered by one leap = distance ?). V. also catrusvätak.
3518:Srēš-ahlāt
5354:sraska-: srišk
5392:tap-, tapa-, tapaya-: taftan (vi-)tar-: vitartan tarasca: turist tarsna-: tisnak taro: !tar, turist taš-: tašitan tašta-: tašt taOra-: tārīk taOrya-: tàrik tauruna-: tarr tav-: tuvan (pati-)!tav-: pattài, pattàn tavah-: stob tiyri-: tigr | Tird.nakaOwa-: Tir Tištrya-: Tistr tiži-: tēž tkaēša-: kēš tõi, to: -t türa-: Tur Tusa-: Tiis tušni-: tušn (fra)-Oang-: frahaxtan Oračtaona-: Fréton Orah-: sahm Orah-, terosa-: tarsitan Orisant-: !sih Orišva-: srišvātak Orita-: Srit Orita-: Oritak Oritya-: sitikar Owa-: to Owaxš-: tuxšitan
7404:sirišk: srišk
```


## [2026-09-06T20:56:25.089Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK search klau/klaui ===\"; grep -n \"klāu̯i\\|kl.u-, kl.u̯i\\|Riegel, Schlüssel\\|kläu\" POK_full.txt | head -20\necho \"--- try clavis ---\"; grep -n \"clāvis .Schlüssel\\|clāvus\\|claudō\" POK_full.txt | head -20"
}
```


### [2026-09-06T20:56:25.168Z] TOOL RESULT

```
=== POK search klau/klaui ===
--- try clavis ---
```


## [2026-09-06T20:56:27.045Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT sraes/sris ===\"; grep -n \"sraēš\\|sriš\\|hąm.sriš\\|sraeš\" BRT.txt | head -30\necho \"=== HRN sirišt ===\"; grep -n -i \"sirišt\\|siriš\\|sirišm\\|serišt\" HRN.txt | head -20\necho \"=== HUB ===\"; grep -n -i \"sirišt\\|siriš\\|sriš\" HUB.txt | head -20"
}
```


### [2026-09-06T20:56:27.123Z] TOOL RESULT

```
=== BRT sraes/sris ===
=== HRN sirišt ===
=== HUB ===
```


## [2026-09-06T20:56:31.039Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK head ===\"; ls -la POK_full.txt POK_01.txt; head -c 400 POK_full.txt\necho; echo \"=== grep clavis ===\"; grep -n \"clavis\" POK_full.txt | head -10\necho \"=== grep Schlüssel ===\"; grep -c \"Schl\" POK_full.txt\necho \"=== grep kleu ===\"; grep -n \"kleu\" POK_full.txt | head -20"
}
```


### [2026-09-06T20:56:31.118Z] TOOL RESULT

```
=== POK head ===
-rw-rw-r-- 1 sfmqrb sfmqrb  981836 Sep  4 14:06 POK_01.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 3971883 Sep  4 14:06 POK_full.txt
List of language abbreviations in tlie lED 



Abbreviation Language name 


Aeq. 




Aequian 


Akk. 




Akkadian 


Alan. 




Alanian (=Old Ossetic) 


Alb. 




Albanian 


Anat. 




Anatolian 


Ang. 




Anglian 


AngN 




Anglo-Norman 


Aram.- 


■Iran 


Aramaeo-lranian 


Ash. 




Ashkun 


Ass. 




Assyrian 


Auk. 




Aukshtaitian 


Bactr. 




Bactrian 


Bel. 




Beloruss
=== grep clavis ===
47630:Latin clavis^ key ', Demin. claviculae^ a tendril ', c/avus'naW ', claudo, -ere "shut, lock ' 
=== grep Schlüssel ===
80
=== grep kleu ===
5404:enkel. Old Frisian onkel, onkleu. Modern High German Enkel, 
44780:The inanimate suffix -ur- . bret. kleur^ Gabelbaum am Wagen ') : 'lAAupioi , oi, lllyrians, 
44978:Aor. (£)k£kA£to, Doric k£vto = (£)k£Ato; [about k£A£uu) see below kleu-]; K£Aapu^u) 
47521:See also: s. still under kleu- " rinse '. 
47616:Root/ lemma: kleu- {a\so kleu-1) and klau- 
49036:assumption secondary lengthened grade *kleup/b-ov\e has added Gothic hiaupan'ruvi, 
51494:( *kleuos) "fame'; Pedersen Tochar. 225. 
51520:= "*will hear' from *kleua-s-id has future s). 
51555:Germanic *kleuo-)\ 
51565:applied, would be for kleu- : kel- the relation sreu-' flow ' : ser- either model or parallel.
```


## [2026-09-06T20:56:34.030Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '47600,47680p' POK_full.txt"
}
```


### [2026-09-06T20:56:34.078Z] TOOL RESULT

```
geleb{h)-, gleb{h)- (: glab{h)-) and glet{h)- {:g/b{h)-) of Root/ lemma: ge/-1: "to curl; round, 

*fathom, arm' [see above]. 

Material: Middle High German /after' fathom, arm', Latvian /r/e/7/s "lap, lapful', Lithuanian 

klebys' fathom, armful, armload ' (/? perhaps aiter g/ebys' armful, armload '). 

Initial sound variation besides Lithuanian glebys. Modern High German Klafter' fathom'? 
(see above S. 359 under ^e/-" clench '). - Old High German halftra' halter', Lithuanian 
kilpa' loop, noose, snare, steep hill ' (Persson) see below s/re/- "split'. 

References: WP. I 498, Buga Kalba irs. I 71, MiJhlenbach-Endzelin II 224. 
Page(s): 604 

Root/ lemma: kleu- {a\so kleu-1) and klau- 

Meaning: hook; hooked branch or piece of wood, etc.. 

Material: Gr. Ionian KAn'i'q -T5oc;, Old Attic KApc;, Attic kKzxq,, Doric KAai'c;, -i'Soc; " key ' (also 

"bar, bolt; hook-shaped noose; oarlock ')., Doric secondary KAg^, epidaur. Gen. kAqiko^ 



ds., KAn'i'u) (Ionian), KApu) (Old Attic), kAeIu) (Attic) " 'draw forward' the bolts closing the 
door, by means of the thong, bar, bolt, key ', KApiGpov (Ionian), KAfiGpov (Old Attic), 
KAsTGpov (Attic) " bar for closing a door, boom of a harbour, fences, railings '; 

Latin clavis^ key ', Demin. claviculae^ a tendril ', c/avus'naW ', claudo, -ere "shut, lock ' 
{*klaui-dd, with present formation d)\ in addition probably c/audus'\ame' (to cludus, clodus 
s. WH. I 231), claudeo, -ere^ limp '. 

Old Irish do, PI. c/o/'nail'; unclear mcymr. cloxw. "bar, bolt, fastener', PI. cloeu^ nails ', 
Middle Breton clou^ ferrement ' (Ernault RC. 37, 104 f.); 

from Germanic probably here (with moveable s-) Old High German sliozan. Middle Low 
German sluten. Old Frisian s/J/a'shut', Old High German sluzzil, asachs. slutiT key ', Old 
High German slozu. " lock ' (sAfrom skl-)\ compare Middle English slote= Low German 
s/afen^bar, bolt'. Middle Low German s/e/from *sleuta-^ flexible shaft, pole', if from " little 
peg, branch piece '. 

without 5- perhaps Old Norse /7^0/a strong. V. " draw lots for, receive'. Old English 
hieotan. Old Saxon hliotan^ draw lots for, release, liberate ', Old High German hiiozan' 
draw lots for, forecast, soothsay, conjure, perform magic', Gothic h/autslot, fate, heritage'. 
Old Icelandic h/autr'\ot, fate'. Old High German h/ozn., Old Saxon h/dt'\ot, fate, the 
assigned right or property'. Old Icelandic h/utr'\ot, fate, allotment, thing'. Old High German 
(h)luz^ lot, closed allotment, portion of the land, allotment, plot of land'. Old Frisian Old 
English hlotu. 'lot, fate', Dutch /o/ds.; 

Latvian M7/"become, succeed, attain ', kfutas'fate, destiny', Lithuanian nekliutas 
"mishap, mischief and Lithuanian kliudyti^ make hang '; 

Lithuanian kliuvu, kliuti^ hook, hang, remain hung', kliutis, kliute^ hindrance ', kliaute^ 
hindrance, disability ', pasikliau-ju, -tT trust on ' ("*cling on to something '), Latvian kl'Ostu, 
kiuf{ remain hung), (whereto) obtain, become', klaustfties^ remain hung ', klum-s, -a, -e' 
hindrance '; causative with -d-. Lithuanian kliudau, -yti' make hang ', kliaudau, -///'hinder', 
kliauda^ the physical disability ' (see above to Latin claudus), Latvian kfudft \ter. to k/ut 
(see above); 

with Ar-forms Old Church Slavic k/Jucb "hook, key ', kljuc-g, -iti^ combine, merge '; russ. 
kljuka^ crutch, crosier, crozier, bishop's staff, OfenkriJcke ', serb. kljuka^hook, key, agrafe, 
clasp ', Old Church Slavic kljuc-im, -///'bend, crook', also Church Slavic /r^i//ra 'artifice, 



deceit' , and as " hook, hang = fit together, suit, occur ' Old Bulgarian kluciti s§ " fit, 
assemble '; probably also serb. klJuna^V\v\6 of hook, cramp', kljun^ something crooked'. 

Maybe alb. geles^ key ', pe/"open, unlock ', p/Z/e^'sincere ', pe/eY'light (color) ', pa/e/"lame 
(with crooked legs) ', galoj^ limp ', galaman^ limped person ' Slavic loanword (common 
Avestan Slavic k> 6: alb. k> ts ><^: Greek Tocharian labialized k"-> /-). 

References: WP. I 492 ff., WH. I 231 , Trautmann 137 f. 
Page(s): 604-605 

Root / lemma: knei-g^h-, knei-b- 

Meaning: to incline, bend
```


## [2026-09-06T20:56:54.434Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== FVQ maqalid/iqlid ===\"; grep -n -i \"maqālīd\\|maqalid\\|iqlīd\\|iqlid\\|aqlīd\\|Iklid\" FVQ_pages.txt | head -20"
}
```


### [2026-09-06T20:56:54.487Z] TOOL RESULT

```
=== FVQ maqalid/iqlid ===
```


## [2026-09-06T20:56:56.849Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON kelid ===\"; grep -n \"مقلاد\\|مقالید\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt 2>/dev/null | head -20\necho \"=== MON sirish ===\"; grep -n \"سریش\\|سیریش\\|سریشم\" MON_part1.txt MON_part2.txt 2>/dev/null | head -20"
}
```


### [2026-09-06T20:56:56.928Z] TOOL RESULT

```
=== MON kelid ===
incoming/MON/MON_2vol_Adena_v1_djvu.txt:15581:اقلید: ۱14 [معر.] (ا.) کلید» مقلاد. 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:78978:سلاخ: مقلاده [ع ] (ص.) کسی که گوسفند 
MON_part1.txt:15581:اقلید: ۱14 [معر.] (ا.) کلید» مقلاد. 
MON_part1.txt:78978:سلاخ: مقلاده [ع ] (ص.) کسی که گوسفند 
=== MON sirish ===
MON_part2.txt:10841:قطع کن می‌برند و اجسام حاصل را به سریشم 
MON_part2.txt:14475:امکان می‌یافت و بعد کله را با سریشم به زبانه 
MON_part2.txt:17078:بسنام‌های چلغوز» حب القسریش» حب 
MON_part2.txt:20751:بسریشم‌نما؛ کتان زبلند الجدیدة. کتان 
MON_part2.txt:43633:جدار مثانهٌ شنای وی سریشم ماهی تهیه 
MON_part2.txt:61396:سریشم‌هایی را که بر اثر فشار از کناره‌های 
MON_part2.txt:86420:پبارچه و بافته‌ای اسریشمی» وشی» 
MON_part1.txt:40335:تسریشه: (۱2:18)0 [- تراشه] (.) خرده 
MON_part1.txt:40337:تسریشین: ۱181 (.) (جاد.) یکی از 
MON_part1.txt:73184:بکا رود و آن را از سریشم ماهی» گلیسرین 
MON_part1.txt:77728:سریش: 14:»: (.) (گبا.) گیاهی است از
```


## [2026-09-06T20:57:01.865Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== FVQ leaf 284/285 (p.267/268) ===\"; awk 'BEGIN{RS=\"\\f\"} NR>=284 && NR<=286' FVQ_pages.txt | head -120"
}
```


### [2026-09-06T20:57:03.519Z] TOOL RESULT

```
=== FVQ leaf 284/285 (p.267/268) ===
266 FOREIGN VOCABULARY OP THE QUR ? AN
mashydb ; Phlv. -"tW^ (Shikand, Glossary, 258), and the Manichaean
Soghdian msyh' (Henning, Manichaisches Beichibuch, 142).
The word was well known in both N. and S. Arabia in pre-Islamic
times. 1
JLf (Mishkdt).
xxiv, 35.
A niche in a wall.
The word was early recognized as foreign (Siddiqi, 13). as-Suyutl,
Itq, 324, gives it as Abyssinian on the authority of Mujahid, 2 and
al-Jawaliql, Mu'arrab, 135, 3 andal-Kindi, Risala, 85, both know that it
is an Abyssinian borrowing. Some, of course, sought to interpret it
as an Arabic word from vXli (LA, xix, 171, quoting Ibn Jinni), but
their difficulties with the word make it obvious that it is a loan-word.
The philologers were correct in their ascription of its origin, for it
is the Eth. o^M\^ (0/* f |i'Th), which is an early word formed from
Ah ID (cf. fcOO, <i*Kt)), and quite commonly used. 4
>
J^A (Misr).
ii, 58 ; x, 87 ; xii, 21, 100 ; xliii, 50.
Egypt.
It occurs only in connection with the stories of Moses and Joseph.
The fact that it is treated as a diptote in the Qur'an would seem
to indicate that it was a foreign name, and this was recognized by some
Df the exegetes, as we learn from Baid. on ii, 58, who derives it from
, which obviously is intended to represent the Heb.
The Eth. ?ftC = Minaean )&3 5 is the only form without the
final ending, and so S. Arabia was doubtless the source of the Qur'anic
form (but see Zimmern, AkJcad. Fremdw, 91).
1 Horovitz, KU, 129, 130 ; Ryckmans, Nome propres, i, 19 ; Rossini, Olossarium,
179.
* See also Mutaw, 41 ; Muzhir, i, 130, for other authorities.
3 Who quotes from Ibn Qutaiba, vide Adab al-Katib, p. 527,'andal-AnbarI, Kitab
al*A4dad, p. 272.
* Noldeke, Neue BeMrage, 51 ; Voliers, ZDMO, Ii, 293.
6 Vide Ryckmans, Nome propres, i, 348 ; Rossini, Ghasarium, 180.
FOREIGN VOCABULARY OP THE QUR*AN 267
(Musawwir).
\ix, 24.
One who fashions.
It is one of the names of God, and its form is undoubtedly Arabic.
Lidzbarski, SB AW, Berlin, 1916, p. 1218, however, claims that in this
technical sense it is a formation from the borrowed Aram. 1JS, 1
which frequently occurs in the Rabbinic writings as a name of God,
and is also found in the Palm, inscriptions in the combination ""
(Lidzbarski, Ephemeris, ii, 269).
(Ma'm).
xxiii, 52 ; xxxv'u, 44 ; Ivi, 18 ; Ixvii, 30.
A fountain, or clear flowing water.
It occurs only in early and middle Meccan passages.
The philologers were uncertain whether it was a form J^** from
.*J*A to flow, or connected with J^V, or from Jl, so called because
of its clearness cf. Zam. on xxiii, 52, and LA, xvii, 179, 298.
The word VJ7, for a spring of water, is of course common Semitic,
but Fraenkel, Fremdw, 281, noted that the Qur'anic ^ is the Heb.
"pUtt, Syr. IfiA^ = Tn/y 7 ?, commonly used for spritig or a bubbling
fountain. From one of these sources, probably from the Syriac, it
came into Arabic.
(Miqldd).
xxxix, 63 ; xlii, 10.
Key.
Only in the plural form JL)LS^4 in the phrase " His are the keys
of heaven and earth", where the use of 7*^** in the similar phrase in
\~?
vi, 59, proves that it means keys, though in these two passages many
of the Commentators want it to mean $ 13>- storehouses?
1 Vide also Hirechfeld, Beitrage, 87.
2 Raghib, Mufradat, 422, and Bakl. on vi, 59.
268 FOREIGN VOCABULARY OF THE
It was early recognized as a foreign word, and said by the philologers
to be of Persian origin. 1 The Pers. JL^ to which they refer it is itself
a borrowing from the Gk. tfAe/9, K\ida (Vullers, Lex, ii, 876),
which was also borrowed into Aram. JOvpX > Syr.
Iri^QO or Irt^o). In spite of Dvorak's vigorous defence of the theory
that it passed directly from Persian into Arabic, 2 we are fairly safe in
.
concluding that the Ar. JLlJ 1 is from the Syr. ) r *.,lo'), 3 and the form
Zy^i* formed therefrom on the analogy of jr ILL*, etc. 4
-V
4Li (Milla).
ii, 114, 124, 129 ; iii, 89 ; iv, 124 ; vi, 162 ; vii, 86, 87 ; xii, 37, 38 ;
xiv, 16 ; xvi, 124 ; xviii, 19 ; xxii, 77 ; xxxviii, 6.
Religion, sect.
It is most commonly found in the phrase ^Al j\ 4U, but is used
for the faith of Jews and Christians (e.g. ii, 114), and for the old heathen
beliefs (e.g. xii, 37 ; xiv, 16). 5 The Muslim authorities take it as an
Arabic word but have some difficulty in explaining it. 6
It has long been recognized as one of those religious terms for
which Muhammad was indebted to the older religions. Sprenger held
that it was an Aramaic word which the Jews brought with them to the
Hijaz, and Hirschfeld, Beitrdge,^, agrees, 7 as does Toiivy, Foundation,
48. The Aram. fcOQ, like the late Heb. !T7Q, means word, but could
be used figuratively for the religious beliefs of a person. The Syr. U^,
(AjkLo, however, is a more likely source, for besides meaning word,
1 al-Jawaliqi, Mu'arrab, 139; as-Suyiitl, Uq, 324; Mutaw, 46; al-KhafajI, 18].
2 Fremdw, 79 ff. ; Muhit* sub voc., wants to derive it directly from Greek.
3 Fraenkel, Fremdw, 15, 16 ; Mmgana, Syruic Influence, 88.
4 Fraenkel, Fremdw, 16, thinks that a form with may have been known in the
Aramaic from which the Arabic word was borrowed.
5 Raghib, Mufradat, 488, says that 4JU can only be used for a religion that was
proclaimed by a Prophet. Cf. LA, xiv, 154.
6 See Sprenger, Leben, ii, 276, n.
7 In his New Researches, 16, Hirschfeld suggests that in Muhammad's mind
X!*O may have been somewhat confused with HT'D circumcision, so that
representing the doctrine of Abraham, and H^D representing the outward
sign of the Abrahamic covenant, being confused together, produced <L as the ^j
of Abraham. This seems, however, a little far-fetched.
```


## [2026-09-06T20:57:18.335Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['BQT','MON','FFD','IEC','HRN','HUB']:\n    v=d[k]; print('==',k); print(' offset:',v.get('page_offset')); print(' hint:',v.get('lookup_hint')); print(' local:',v.get('local_file'))\n\""
}
```


### [2026-09-06T20:57:20.654Z] TOOL RESULT

```
== BQT
 offset: vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').
 hint: grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)
 local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt']
== MON
 offset: None
 hint: Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks).
 local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt']
== FFD
 offset: 115 leaves (PDF pages); printed page = PDF page − 5 (PDF 40 = p.35). 2nd printing 1385 of the same Qoqnus setting (ISBN 964-311-015-X).
 hint: Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/download): nothing; only a related paid e-book 'واژگان زبان فارسی دری' (fidibo). ketabnak.com/book/45024 is a different book (فهرست فعلهای فارسی).
 local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_asmaneketab.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_pages_faseng.txt']
== IEC
 offset: TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
 hint: Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.
 local: /home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt
== HRN
 offset: leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
 hint: Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.
 local: /home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt
== HUB
 offset: leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
 hint: Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number.
 local: /home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt
```


## [2026-09-06T20:57:25.609Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN leaf 183 (p.162) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==184' HRN.txt\necho \"=== HUB leaf 85 (p.75) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==86' HUB.txt"
}
```


### [2026-09-06T20:57:27.213Z] TOOL RESULT

```
=== HRN leaf 183 (p.162) ===
— 162 -
732. siristen 'niisclien, vermengen; schaffen, bilden, sirls
{*sires)j siriäem 'Leim* *).
aw. l^sraes- , sraesyeiti 'sich an etwas hängen ;
phlv. sristan^ sresct (PPGh); ai. skr. [/^rres-^ (^les-^
rlisyatl Verbinden, zusammenfügen'.
sar. xlr/'am ^vermischen, mengen etc.'
733. sirUk "Tropfen .
aw. sraska- 'Hagel' (Justi); für srasc- nimmt
Geldner, KZ. 27, 252 die Grundbedeutung giessen*
an, aw. sraska- bedeutet vielleicht 'Reif, Nebel'.
Unsicher.
734. serTfy sm% serfm *Horn'.
aw. srvä' *Klaue, Hörn'; phlv. srüh (d.i. srtn^), snw.
bei. srunbe^ surum 'Huf (348) -).
7»>r>. suvTiden singen, Praes. seräy-em^ seräf/tden 'singen;
sprechen (Sahn. I, 70 Vers 156), seräyis^ siirüd Lied'.
aw. l'^sruv-, (^aus. srävayeüi; phlv. srüfan 'recitiren',
srayltan^ sräy(i)su^ srüt 'Gesang; ai. l/'grav-^ Caus.
^rävdyati.
wa/. sirav-am^ sar. nasrav-am 'recitiren*.
736. seröä 'Engel' (Vis und RämTn, S. 37, V. 4 v. u.).
aw. Sraosa-; phlv. Srös, vergl. asrös ungehorsam*
(aw. asraosa-),
737. snrTniy surtn 'Hinterbacken, Hinterer.
aw. sraoni- *Hüfte*; phlv. sarük, vd. 8 (178) (181),
sarin 'Hinterer (Bund.) , sar'mak (PPGl.) ; ai. grmü'
'Hinterbacke, Keule, Hüfte'; lit. szlaimis, lat. cliinis,
gr. XA0I7C,' (?), ahd. hlatm ^).
bei. saren 'Lenden, Hüften* (338, wohl in sarzn zu
ändern, vergl. Hübschmann, ZDMG. 44, 555 unter
No. 2) ; wa/. simj, siyn. saun, sar. xdiin,
738. seztden sich ziemen, passen, sezä, sezäyiden.
phlv. sacifan^ sacPt (päz. sazed, saSSd), sacäk.
*) Afy. LW. s(fle/ -, i<(dex'
^) Geiger wirft np. sum^ suub *Huf* fälschlich mit serüu *Horn*
zusammen; vergl. No. 745.
*) Arm. srunl^ ^Schienbeine, Waden', das auch seiner Bedeutung
nach nicht paast, gehört nicht liierher (Fl übschmann, No. 260).
=== HUB leaf 85 (p.75) ===
— 75 -
usrup und usruf an. Alle stimmen nicht zu zd. sruva-
'Blei' (nur als accus. 'srutn belegt).
731. Np. sarma ^est forme par analogie siir garma'* Dar-
mesteter, Etud. iran. I, p. 267 Anm. Die Analogie-
bildung fand schon im Phi. statt [sarmok nach gar-
mak).
732. Vgl. afgh. LW. sariSi, siriSt 'nature, temperament',
sar^ 'glue, birdlime, stickness, adhesiveness' = sal^,
salSx^ $aU§t, Der Bedeutung nach schliessen sich naher
zusammen 1) skr. grU 'verbinden, zusammenfiigen',
vgl. skr. gri *mengen, mischen', np. si/ristan 'mischen,
sirist 'Mischung, Natur, Anlage' (vgl. am^zis *Mischung*
==*Temperament'); 2) skr. glis anhangen, haften, kleben',
zd. ms 'haften', np. sir^ *Leim*.
733. Darmesteter iibersetzt sraska- durch TThrane'.
Zu srasd {tySsrasdat/en *sie sollen besprengen) gehSrt
arm. srsk-em *besprenge\
734. Dazu zd. srvaena- *h5rnen' = phi. sruvBn (geschrieben
srUbSn) 'horny' Gl. and Ind. 162.
735. In den Nachtrftgen wird richtig bemerkt, dass surod
'Gesang, Lied' (mit d) zu sprechen ist, vgl. die LW.
bal. sarDd musik' (Dames p. 87), afgh. sardd a song,
modulation , melody* sowie zd. sraota- vsp. 21 , 3
Taudition' (Darmesteter). Damit ist nicht gesagt,
dass auch der Infinitiv surddan gelautet habe, da neben
sarCLyam ein mirudan stehen kann wie neben sitdyam
ein stUudan steht, wie denn auch in der That in dem
bei Vullers s. v. surudan angefiihrten Verse suru-
dan mit sutudan reimt. Auch N did eke liest nach
anderen Beimen surudan.
737. Das Verhaltnis von np. surin = bal. sar^ aus "^sren
zu np. surUn JRAS. 1894, 469 aus *8rdn ist mir unklar.
740. Zu streichen, da die Etymologic fehlt. Vgl. Horn
p. XI, Anm.
741. Beachte, dass anl. s vor Vokalen im Neupersischen
nicht = idg. s sondern = idg. k^, k% sk^, 8k% ist.
Im Uebrigen sind ja die Bildungen „onomatopoetisch".
```


## [2026-09-06T20:57:44.935Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BQT v2 leaf 593 (~p.1136) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==594' BQT_v2_pages.txt | head -60\necho \"=== BQT v2 leaf 581 (~p.1124) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==582' BQT_v2_pages.txt | head -60"
}
```


### [2026-09-06T20:57:46.414Z] TOOL RESULT

```
=== BQT v2 leaf 593 (~p.1136) ===
  ‫سروچ‬                                                                                                     ‫¬‬
‫ګوبند که راست رود وآن را ياين اعبار آزاد‬              ‫میباشد ‪ :‬مکی‌سروآزاد و دیگری سروسهی‌وسیم‬
 ‫کفته‌ادد که از ید کی و داراستی ویبوستن‌بشاخ‬                                  ‫سرو ناز وهر يك درجای خود‬
‫یوبند هردرختیکه‬
              ‫وک‬‫دیگر فارغ است » ی‬                                            ‫خواهد آمد » وعربان سرو را‬
 ‫میوه ندهدآنرا آزاد خوانند چوون سرو موه‬
‫آزاد باشد» وجممی کفته‌اند عر‬       ‫ندهد ياين سیب‬
                                                                                ‫شجرة الحبه خوانند چه گوننه‬
                                                                             ‫هرجا که سروهست البته مارهم‬
‫درختی رکامالی و زوالی هت چنانکه کاهی‬
                                                                              ‫هست‪ .‬اکر بر کهآ نرابکوبند‬
 ‫که‬
  ‫ر‌ب‬
    ‫وی پژمرده و بی‬
                 ‫پر برکه و تازه اکستاه‬
                                                                             ‫و با سر که بیامیزند موی را‬
‫هيچيك از اینها نیت و همه وقت‬               ‫ورورا‬
                                               ‫س‬
‫سبز و تازه است و اژین علتها فارغ و این صقت‬                  ‫سرو‬                 ‫صاه کند‪ -‬ونام مکی‌ازیادشاهان‬


      ‫آزاد کان است پس بدین جهتآزاد باشد‪.‬‬              ‫یمن است که دختر بیکی از فرزندان فرسون‬
 ‫سر اول‪ - 4‬اول بروزن بزاله‪.‬طفی‬                                                                                  ‫داده بود ‪.‬‬

‫ین که‬
    ‫مو‬‫هشد‬
        ‫بودکه برسرآن خارهای نیز با‬                     ‫سر وا ‪ = ۱‬بروژن پروا» یمعتی حدیت‬
     ‫بحامه فرو رفت جدا کردن‌آن دشوار است‪.‬‬            ‫وعر حم‬
                                                          ‫و سخن باشد ‪ -‬و بمعنی آفانهٌ دروغ ش‬
‫سر وب ‪ - ۸‬بفتح‌اول وضم تالی‌وسکون‬                                                                          ‫گفته اند ‪. ۳‬‬
 ‫ثالث مجهول و بای ابجد ‪ .‬بلفت زسوی‌ازند(‪)۱‬‬            ‫»ام‌منظوم‬
                                                              ‫سرو اك ‪ - ۲‬بروزن فرهاد کل‬
            ‫بمعتی سخن باشد وبعربی کلامگویند‪.‬‬          ‫افون‬     ‫ویمعتی افانه و‬                   ‫شمر را کویند ‪- ۴‬‬        ‫و‬

‫ختح اول وفوقانی وثالت‬     ‫سر و تلك* "‬                                                            ‫وسرود همگفته‌اند ‪۰‬‬

‫مجهول بروزن عروسكك ‪..‬بمعنی شورش وآشوب‬                 ‫سرو اده * = بفتح اول بروزن‌شهزاده‪:‬‬
 ‫وغوغا باشد ؛ و باين معثی بفتح اولوئانیوفوقالی‬
             ‫حم کنته‌اند که بروژّن فرزدق باشد‪.‬‬       ‫قافیة شمر راکوبند ‪ ۱‬همچو بهار ونگار و هزار‬
                                                      ‫وزمین و کمن وامین»وحرف دال درین لفت‌ولفت‬
‫بفتح اول وضم تانی‌وسکون‬            ‫سر وج‬                             ‫ماقبل بثایر قاعده کلی نقطه‌دار است‪.‬‬
‫ثالث مجپول و جیم فارسی ‪ ۰‬دامدشتی است در‬
                                   ‫نواحی کرمان ‪.‬‬      ‫‪ ۲۰‬بکر واو ؛ سرویرا‬                          ‫د‬
                                                                                                   ‫زوا|‬
                                                                                                      ‫سر‬
                                                                         ‫(‪ )۱‬چك ‪ :‬ژند ویاژند ‪۰‬‬
                                       ‫‪:‬‬   ‫رك ‪ ۱‬سرواد ‪ 4‬سرواده‪ .‬ورك ‪ :‬ح ‪۸‬همین‌صفحه‬                     ‫‪_ ۱‬‬

            ‫چند فروشی بمن نو اين سرو سروا‪.‬‬              ‫‪ - ۴‬چند دهی وعد دروغ همی چند ؟‬
  ‫اورمزدی‪« .‬لفت فری ‪۷٩‬‏ ‪.‬‬
                                                        ‫‪.‬‬   ‫» سرود‬       ‫سروا‬   ‫‪ :‬سرواده»‬         ‫رك‬        ‫‪۴‬‬


         ‫بازار وفست سرواد‪.‬‬   ‫که رفت رة‬

   ‫لیی ‪ .‬ل٭فت فرس ‪۸°۱۹‬۔‬
                                                                     ‫‪.‬‬   ‫سروا‬       ‫»‬   ‫رواد‬     ‫رك‪:‬‬   ‫_‬    ‫‪۵‬‬


             ‫ممانی از او وسرواده‬    ‫سای خوش‬             ‫‪- ۱‬بشمر» خواجه! منم داد شاعری داده‬
=== BQT v2 leaf 581 (~p.1124) ===
                                                                                          ‫نف‬

          ‫از استخوان سازند ویدان بدترا خارند‪.‬‬      ‫= ینم اول و خای قطه‌دار‬      ‫سرخاب‬
 ‫سخراریدن ‪ -‬کنابه از نوميد شدن‬                     ‫بر وزن مرغاب » نام رودخانه ابست کوچك در‬
‫‪ -‬و نگاهداشتن ‪ -‬و تسلی کردن ‪ -‬وراغب شدن‬             ‫له آب آن بسرخی مايل است ببب‬
                                                                              ‫تواحی‌کاب ک‬
 ‫‪ -‬ولطف نمودن ‪ -‬و تعلل ودرنگه‌واهمالررزیین‬          ‫سرخی خاك رودخانه ‪ -‬و نکاموهی است‌برجنوب‬
‫‪ -‬وعاجز شدن در جواب خصم ‪ -‬و حیله و مکر‬             ‫است بشهر » و گویند چند‬      ‫ل‬ ‫صو‬ ‫تربز‬
                                                                                       ‫مر تب‬
                                                                                           ‫شه‬
 ‫نمودن ‪ -‬وخجل شدن وشرمنده‬        ‫وتملق‬   ‫کرو‬        ‫جای دیگرسرخاب هت ‪ - ۴‬ولوعی ازمرغابی‬
                 ‫گردیدن ‪ -‬وبپانهآوردن باشد‪.‬‬        ‫باشذ سرخ رنگه ‪ . ۴‬کوبند ماد آنرا مانند‬
 ‫سرخ بال ‏ بابای ابجد بروزن‌ختك‬                    ‫زنان حیض ميآد ‪ ,‬و بسنی کویند پرنده ایست‬
 ‫سال » تیپو راگویند»وآن‌بر ندمایت‌مانند كبك‬         ‫که تمام شب از جفت خود جدا باشد وبکدیگر‬
               ‫لیکن از كبك کوچکتر می‌باشد‪.‬‬          ‫را له بیتند لیکن آواز دهند ویسمت آواز بقصد‬
                                                    ‫ماوم شب‬    ‫توند‬
                                                                  ‫اما ملافی نش‬   ‫نمد‬‫بت ه‬‫آاقا‬‫مل‬
 ‫سرخ پای د ببای فارسی » سابمزء‬
 ‫ایست بفایت نازك وطعم آن ترش باشد و بحربی‬          ‫جدا شود جفتی‬       ‫ت‬
                                                                      ‫فاز‬
                                                                        ‫جون‬
                                                                          ‫بیقرار باشند و چ‬
                                                   ‫دمگر نکند و اگر یکی از آنپا جفت خود را‬
                             ‫حماس خوانندش ‪.‬‬
 ‫وخنگسبرتخ‪ ۷‬بکبرختا‪-‬ی‌نبقطنه‌امدوالر و بایایسد()‬    ‫درآتش بیند او یز خود را درآ تس اندازدراورا‬
                                                   ‫ای باشد‬    ‫ه‬
                                                              ‫اخیز و‬
                                                                   ‫غوسر‬
                                                                      ‫خرچال هم مدگوبند ‪-‬‬
‫دوت‌بز رها ند‬
 ‫درموضم بامیان ازمضافات‌ابل در سرحدبدخشان‬            ‫نا‪-‬م‬
                                                        ‫که زنان با سفید آب برروی خود ماولند‬
                                                    ‫پهلوانی بوده از پپاوانان فبروز پسر بزدجرد ‪-‬‬
 ‫از سنگه تراشیده ک‪.‬وبند بلندی هر بك ازآن‬
                                                   ‫ونام یکی از ملوك هم هت و او از سل بهرام‬
 ‫آنها مجوف است‬        ‫ن‬
                      ‫مشدار‬
                          ‫با‬        ‫گز‬
                                     ‫وو‬‫دجاه‬
                                          ‫پن‬
 ‫چنانکه ازکنهای بای ابشان راه است و نردبان‬
                                                    ‫کور بوده ‪ -‬سوهراب پسر رستم را لیز سرخاب‬
                                                    ‫وامه‬‫میگفته‌اند و‪-‬شراب لعلی‌را لیز کوبند کن‬
 ‫پابھاکرده‌اند که بجمیم نجاویفآنها میتوان کشت‬                ‫از خون همهت که بعرییدم خوانند‪.‬‬
‫حتی سرهای انگشتان دست و بای ابشان و آ ها‬
 ‫را بعربی دموق ویفوث‌خوانند ویضی لات ومنات‬          ‫سرخاره ‪ = ۴‬بروزن انگاره » سوزن‬
 ‫خوانند‪ .‬گووبند سرخ بت عاشق خنگبت است‬               ‫زرینی باشد که زنان بجهت زینت بر سر زنند‬
 ‫آولرا سرخ بد ‪ ۷‬هم‌خوانند کهبجای حرفآخر‬             ‫دتا ازسرابشان‬        ‫نحك‬
                                                                           ‫نبرل‬‫کآن‬‫دابا‬
                                                                                     ‫نر‬‫بنمه‬
                                                                                          ‫ومق‬
                                 ‫یاشف‪.‬‬   ‫دال اعد‬   ‫یند که‬    ‫لیفتد ‪ - 9‬و پنجه مانندی رکا نویز‬

                                                                     ‫(‪ )۱‬چك ‪ :‬وبا‪.‬‬
                                                               ‫‪ = ۱‬سپراب («‪.‬م‪. ).‬‬
                   ‫‪.‬یهان ص ‪. ۵۹۳‬‬
                               ‫‪ - ۴‬نیز موضعی در ساو جبلاغ «جفرافیای سیاسی ک‬
            ‫چون‌نذروان سرخ وچون سرخاب ‪.‬‬                 ‫‪- ۳‬پیش او کی شوند بازسپید‬
   ‫مروزی‪ «.‬لغت فری ‪۳۳٩‬‏ ‪.‬‬     ‫عسسدی‬
```


## [2026-09-06T20:57:46.769Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== IEC leaf 833/834 ===\"; awk 'BEGIN{RS=\"\\f\"} NR>=834 && NR<=835' IEC.txt | head -80\necho \"=== IEC klis grep ===\"; grep -n \"^kliK\\|^klis\\|^kleis\\|^slis\\|^ḱlis\\|Kli[sš]\" IEC.txt | head"
}
```


### [2026-09-06T20:57:48.466Z] TOOL RESULT

```
=== IEC leaf 833/834 ===
utifully’; Sw. vän, adj. ‘pleasant’; Li. vēnios, fpl. ‘strength’. (Isophonic: Latv. pa- vēnis ‘shade, shadow, shelter’)
uën- (2) “lacking, defective, immature; lack’, etc. Cf. uän-. Gk. ambig. Hom. Cf. énis, gs: énios, adj. (immature, un- mated, virgin’ of heifer); LG Du. wàn-, wan-, cpds. *mis-; cf. G Wahn-sinn (infl. by Wahn, see uen- (1). Semantics of Lat. jünix fr. ieun-, q. v.). See Supt: U
uendh- (1) ‘turn’. WP I, 261. Cf. uondh-, undh- Skt. cf. vandhürabh, m. *chariot-seat'; Arm. cf. gind, gs: gndi, ab. s. -av, also gint, gs: gnti, s. (ring; gndak, dim. ‘tendri’; Tokh. AB wánt-, v. ‘wrap’; Gk. cf. peirins, gs: peírinthos, f. “wicker body of chariot if fr. *peri-uendh-); Umb. (queried) aha-uendu “let him turn aside’; Go. bi-windan, sv. 3. “wind, wrap’; MHG winden, winten (and com. Gmc.),id.; G & MHG Winde, winde, wf. *winder, spool, capstan, convolvulus'; OHG winta, f. id. (and “spiral staircase’); ON vinda, sv. 3. ‘wind’; f. ‘hank’; vindr, adj. fawry'; cf. vindli, m. ‘wisp’; Sw. vind, adj. ^warped'; OE windan, sv. 3. ‘wind’; wind, n. ‘wind, path, weave, textile’; Srb. (?) vedja, f. ‘eyebrow’. (A hapax arises in Ir. feann, s. *flaying, skinning’)
uendh- (2) ‘barren, withered; wasting, de- cay’. WP I, 261 Skt. vandhyah ‘barren’; Arm. goně, Let. ‘mangy, scurvy’ beside (dial) eung id.; Ir. cf. fann, adj. (weak, faint’. Ambig. cf. uán-, but possibly < *undh- as also Br. gwann, f. *carrion"); Du. G EME, Sw. cf. wind-ei, -egg, -ägg ‘addled egg’; G cf. also windisch, adj. ‘lean, limp’; Pol. wigd, s. m. ‘wasting, decay’; Cz. vada, f. (defect. LW in Pol. wada, id.) beside Cz. z-vadly, adj. *withered"; Slovene
uén- — uenos, -es-
10
15
20
25
30
35
40
45
1514
védel, id. (Vocalism of ON vándr "bad is ob- scure. Comparative form of type *uendh-tero- (?) in MHG winster, ON vinstri, adj. “left- hand")
ueng- ‘turn, bend’. WP I, 260. Cf. uenĝ- and uengh- Skt. vangami, v. limp, hobble, go’; Tokh. B wünk-, v. (queried: ‘propose’ or sim.); OHG winchan, MHG winken, sv. 3. 'sidle, wag, sway’; OE cf. wince, f. ‘winch, pulley’; E to winch (‘wind w. a winch’: mod. only); Sw. vink, m. “bracket'; Li. véngiu, véngti, v. ‘dodge’. Extn. of type *uengəl-, uengil- in MHG winkel, sm. ‘corner’; OE wincel, id.
uengolos, iom (uengil-) “child” OE wincel E wencel, m. (2), id.; Cz. viZle, n. id.
uengh- “go, move’. Cf. ueng- and ueng- Skt. vanghe, mp. ‘go’; Sw. cf. vingla, v. ‘stroll; wangle, cheat’; Norw. vingle, v. ‘flutter; wan- der; vacillate’; Icel. cf. vingl, m. ‘madness’; vingull, m. (1) ‘fool’; Oss. cf. wängäl, ongäl, s. ‘plague, epidemic’; (o-gde in) E to wangle
uenĝ-, variant of type ueng-, q. v. (Gmc. am- big.) MHG (ambig.) winken, sv. 3. ‘wag, sway, bow’; E to winch; OCS vẹzọ, vesti, v. ‘fix’; u-? ‘to garland’; OCz. vëZu, vésti or viesti, v. ‘tie. Nominal types: OE wince, f. ‘winch, pulley’; MHG winc, gs: winkes, sm. ‘sway, wavering’; winkel, sm. ‘corner’; OCS vẹza, f. ‘strangula- tion’; R vjazi, f. ‘tie, binding’; Cz. s-vaz, m. ‘union’ beside vaz, m. ‘neck’; Sw. vink, m. *bracket'. Extn. in Skt. vañjulah, m. (a plant, perh. *creeper); OCS vezlo, n. ‘bind, tie’. (O- gde in) OCS vozü, voza, mf. “bond, tie, fetter’, vọzlo, m. id.
uenos, -es- ‘desire’. Cf. uén- (1) and WP I, 259 Skt. vanas, n. ‘loveliness’ beside vanā & vanih, f. id.; vanús, adj. ‘keen; loving’; Lat. Venus, gs: -eris, f. ‘Venus’; beside vinulus & vinnulus, adj. ‘dainty; wanton’; W gwên, pl. gwenau, f. “smile”, cf. Gweno, f. “evening star, Venus’; (z-gde in) OHG wunja, MHG wunne, wünne, f. (2
) joy’; OE wynn, f. ‘delight’; cf. wyn-sum ‘winsome’. (FK:EWDS untenable: Wonne). See next
1515
uénskKó ‘desire’. Cf. uenos, -es-, and uén- (1). WP I, 259 Skt. vafncami, v. id.; Du. wenschen, mod. wensen, v. id.; wens, m. id.; (zero-gde in G wünschen)
uenter- (uentor-) (uemster-?) *wickerwork, basket" (?); ‘bag, net? (?) Av. cf. vafita, f. ‘wicker’; Lat. venter, gs: ven- tris, m. (abdomen, stomach, womb'. Fig. sense of *bread-basket (?), cf. pàn-tex ‘paunch’, if a cpd. of panis "bread", and cf. E. dial. breadbasket = *'abdomen); Li. vénteris, gs: vénterio, m. *bownet, fishtrap', Latv. ven- teris ( fish-trap, fish-basket' or '-pot"); but cf. also Icel. vinstur, pl. vinstrar, f. “fourth stom- ach of ruminant'. See Supt: U: uemstr-
uéntos (*uéntos) ‘blow, blowing, wind, gust’. WP I, 220. Cf. ueio (“uëið) Tokh. want, wànt, B yente (sic), id.; Hitt. huwantas, pl. huwantes, id.; Lat. ventus, gs: 4, m. ‘wind, storm’; Ir. (?) fead, mf. whistle’, only if for *féad); W gwynt, pl. -oedd, m. *wind'; Br. gwent, m. id.; Cor. gwyns, pl. -ow, m. id.; OHG wint, i-st. & o-st. m. id.; OE, Du. wind, m. id.; OE winde, adj. ‘windy’; ON vindr, m. “wind, air”
uequó (uequmi, uiuéqumi) “call, say, speak, ask’. Cf. uoóqu-. WP I, 245 Skt. vátmi, vakmi, vívakmi, 2, 3s: vaksi, vakti, *say, speak, tell, name, call, announce, des- cribe, reproach’; pp: uktáh, inf: váktum; Av. vað-, v. ‘talk’; Per. güvam, inf: guftan, v. ‘say’; Tokh. B wek-, v. ‘say, speak’; Arm. (?) goéem, v. Cer, if to Skt. vivaksami ‘wish to say"); Gk. eípo, v. ‘say’; Olr. cf. in-fét, 3s. ‘tells’; pf: in-féccid (sic) “he told’; OCz. vece Che said”: inf: vecéti); OPr. wack-, v. ‘cal? (de- nom.?). Nominal types: Skt. vacas, n. “speech, word"; Av. vačō, obl. vacáh-, n. id.; Gk. épos, gs: -eos, n. id.; Hitt. cf. wekuwar, n. ‘request’; Arm. (?) gov, s. ‘praise’; OR. cf. véCe, n. ‘coun- cil, commons'. Extn. of type *uequtis beside *uoqutis, *uqutis in Skt. vaktih, f. “speech; Av. cf. uxtis, z-gde, f. 'expression'; Arm. cf. (?) goCiwn, s. 'shout' (but Iran. LW in Arm. uxt, Lët vow); Cz. (?) od-vet, mf. ‘retaliation’; o-veta, id. (Gmc. LW?)
uequtió cf. uequó
uénsKó — uerbos, -es- (uorb-, urb-); uerbà
10
15
20
25
30
35
40
45
1516
Alb. cf. p-ves & pyes, aor: p-veta, pyeta, v. (ask', fr. apo-°); Ir. cf. fachtaim, v. id.
uer- (1) (uero, io, uro, ið) open, close’. WP I, 280 Skt. várami, v. pp: vrtab, id.; Av. var-, v. ‘cover; Lat. cf. ambig. ap-erio, erte, v. ‘open’; cop- erio, -erire, v. ‘close, cover, hide’; Li. veriü, vérti, v. tr. (9) open or shut — a door or window’; Latv. veru, vērt, tr. ‘open’; (z-gde in) OCS (and com. SL) vro, vréti, v. ‘close’; cf. Cz. ote-vfit, inf. "open": za-vřít, inf. ‘close’. Nominal types: Osc. vereias, adj. f. ʻofa door’; R verejà, f. 'doorpost; Cz. vefeje, f. id.; cf. roz-vera, f. *wantonness'. (Isophones, of un- certain kinship to uer- (1): Skt. long-gde varah “time, turn’; Per. bar, id. beside di-vàr "wall": Romani -var *-times'; Lat. hapax verones, pl. ‘sheets of lead; ON -var, in pris-var ‘three times’; Skt. varah; m. ‘enclosure, space, room’: Av. varo ‘garden’ beside vairis, m. ‘lake’; Medic in Gk. ouéra, f. ‘gardem or sim. Cf. Osc. veru, neut. pl. ‘door’; MIr. farr, pl. fairre, n. -es-st. bedpost; OE wer, m. "wer: ON ver, n. 'fish-weir'; Gk. cf. próra ‘prow’, if for *pro-ueràa)
uer- (2) “look, watch, observe, care for. Verbal type: uereio, cf. uor- (2). WP I, 284 Tokh. wär-, B war-, v. “sense, feel Lat. vereor, inf. vereri, v. ‘regard, revere’; Br. cf. gwéré, pl. -u, f. ‘watchtower, coastguard post; Srb. verem se, inf: verati se, v. ‘keep a look-out, be furtive’; Latv. cf. veros, inf: vērtis, v. ‘watch, look’; cf. vērā 
=== IEC klis grep ===
7296:kleistos (variant of kleitos, see next) Gk. kleistós, adj. "but": W clwys, pl. au, m. *enclosure'
7351:kliKo, io (?) ‘squeeze, twist. WP I, 492 Skt. klisSyami “torture, force’; Li. cf. klisas ‘crippled’; klystu, -ti ‘get crippled'
```


## [2026-09-06T20:58:04.395Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor L in 890 893 896; do echo \"### leaf $L ###\"; awk -v n=$((L+1)) 'BEGIN{RS=\"\\f\"} NR==n' IEC.txt | grep -o \"16[0-9][0-9]\" | head -5; done\necho \"=== search Klis- headword ===\"; grep -n \"klis-\\|kliso\\|klisio\\|ḱlis\" IEC.txt | head"
}
```


### [2026-09-06T20:58:06.314Z] TOOL RESULT

```
### leaf 890 ###
### leaf 893 ###
### leaf 896 ###
=== search Klis- headword ===
```


## [2026-09-06T20:58:09.347Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} {n=NR-1; if (match($0,/1[56][0-9][0-9]/)) { print n\": \"substr($0,RSTART,4) } }' IEC.txt | tail -40\necho \"--- total leaves ---\"; awk 'BEGIN{RS=\"\\f\"} END{print NR}' IEC.txt"
}
```


### [2026-09-06T20:58:10.964Z] TOOL RESULT

```
5: 1572
8: 1651
482: 1547
498: 1655
802: 1648
825: 1500
826: 1502
827: 1504
828: 1505
829: 1507
830: 1509
831: 1510
832: 1512
833: 1514
834: 1515
835: 1517
836: 1519
837: 1521
838: 1522
839: 1524
840: 1526
841: 1528
842: 1530
843: 1531
844: 1533
845: 1535
846: 1536
847: 1538
848: 1540
849: 1542
850: 1543
851: 1545
852: 1547
853: 1549
854: 1551
855: 1552
856: 1554
--- total leaves ---
858
```


## [2026-09-06T20:58:15.472Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR>=857' IEC.txt | tail -30"
}
```


### [2026-09-06T20:58:17.135Z] TOOL RESULT

```
bulga is ambig. Skt. várgā ‘sect, class’ seems to be unrelated)
(ulio (1) ‘wind, wrap’, see uluið; (2) ‘boil’, see ulāið)
ulksuos, à (ul'suos, à) (?) ‘sorcerer, prophet Gk. cf. (?) álsos, n. ‘sacred grove’; ON cf. volva ‘prophetess’; OCS vlüxvü, m. ‘prophet’; vlüxvij, adj. *magical'; Blg. vláxva, m. *high- wayman'; LW in Finn. velho ('sorcerer', vocal- ism of Finn. verho “top”, cf. urks- (4))
ulm- ‘surge, billow; wide mouth, gulf’. WP I, 298. Gk. ambig. & uncertain Skt. ürmíb, mf. ‘wave, billow’; Gk. cf. lámos, m. ‘gulf; lámia, f. ‘monster, wide-mouthed fish’; cf. lamurós ‘deep, awful; riotous’; Arm. cf. aymuk, gs: aymki, ab. s. aymkav, s. *up- roar’; OE wylm, m. ‘surge, billow, boiling’; G (7) Wolm, m. ‘archway, porch, curved ba- nister’; ON olmr, adj. ‘wild, boisterous’. (Iso- phone: Li. vilminti, inf. ‘cheat’)
uln- (1) (ulna, ulon-) ‘wool’. WP I, 206. (Var- iant initial in Oss.) Skt. urna, f. id.; Av. cf. una, f. “lock, curl’; Oss. cf. qun, Dig. gun, s. ‘wool, hair’; Hitt. cf. hulana-, Luvian hulani- (queried: *wool"); Lat. lana, f. id.; Ir. olann, gs: olna & olla, f. id.; W gwlan, OBr. gulan, Breton gloan, m. id.; OHG wolla, f. id.; Go. wulla, f. id.; OE wull, wll f. id.; ON ull, ds: ullu, f. id.; OCS vlüna, Cz. vina, Pol. wełna, Big. vlána, id.; Li. vilna, Latv. vilna, id.
ulgh- — ulquos, is
20
25
30
35
40
45
1554
uln- (2) (ulnis, à) ‘surge, wave’. WP I, 302- 3. (Gk. ambig.) Oss. wlän ‘wave’; Arm. cf. alik, gen. aleaç, abl. aleawk, id.; Gk. cf. alés, halés, adj. ‘surg- ing’; but Gk. hális, adv. (“in a mass’ equally fr. a type *uluit-, see uluió and extns.); Alb. valë, pl. id., f. ‘wave’; OE wll m. ‘fountain’; OCS vlüna, Cz. vina, f. (2) ‘wave’; Li. vilnis, i&s, f. id.; Latv. vilnis, id.
(ulnio (1) see uluið; (2) see ulaið) 
(1) only in Skt. ürnómi, v. ‘envelop’; (2) only in Gmc. cf. Go. wulan and OE wylian 'seethe? beside wyllan, v. id. (fr. *ulnio)
ulquátis, os *tearer, devourer, killer’. Cf. ul- quos (1) Skt. vrkátih, m. ‘robber, murderer’; Slovene volkác ‘Alsatian dog’; Li. vilkátas, m. *wer- wolf; Late vilkatis, vilkacs, id.
ulquio ‘she-wolf’. Cf. ulquos (1) Skt. vrkih, id.; OE welt id. MHG (Upper Ger) wülpe, id.; ON ylgr, ds: ylgi, id.; Li. vilke, id.
ulquó, ið (ambiguous consonantism, unless related to type ulquos, etc. see next). Skt. varke, mp. ((seize', but cf. type *uelk-) beside vrkah (2) '(plough'; Srb. vučem, v. ‘drag’; cf. OCS (hapax) vlüci, s. (Ccaltrop? or sim.); Li. vilkiu, eti, v. ‘wear — a garment’; cf. vilktas, m. (tech. *priming); L
```


## [2026-09-06T20:58:39.438Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BQT v2 grep سرشت ===\"; awk 'BEGIN{RS=\"\\f\"} /سرشت/ {print \"leaf \"NR-1}' BQT_v2_pages.txt | head -20\necho \"=== BQT v2 grep سریش ===\"; awk 'BEGIN{RS=\"\\f\"} /سریش|سریشم/ {print \"leaf \"NR-1}' BQT_v2_pages.txt | head -20\necho \"=== BQT v2 grep sirišm latin footnote ===\"; awk 'BEGIN{RS=\"\\f\"} /sirišm|siriš|srēš|srišt/ {print \"leaf \"NR-1}' BQT_v2_pages.txt | head -20"
}
```


### [2026-09-06T20:58:41.364Z] TOOL RESULT

```
=== BQT v2 grep سرشت ===
leaf 62
leaf 157
leaf 190
leaf 236
leaf 313
leaf 366
leaf 411
leaf 440
leaf 577
leaf 586
leaf 598
=== BQT v2 grep سریش ===
leaf 586
=== BQT v2 grep sirišm latin footnote ===
```


## [2026-09-06T20:58:44.243Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### leaf 586 ###\"; awk 'BEGIN{RS=\"\\f\"} NR==587' BQT_v2_pages.txt\necho \"### leaf 577 ###\"; awk 'BEGIN{RS=\"\\f\"} NR==578' BQT_v2_pages.txt | head -50"
}
```


### [2026-09-06T20:58:45.928Z] TOOL RESULT

```
### leaf 586 ###
   ‫)‪۷۱‬ات‬

‫که بجمد و جهنده باشد ‪ -‬و نام درختی است‌در‬           ‫بمعنی ربختن باشد ‪-‬ویمعنی‬         ‫ر‬
                                                                                     ‫شتاچه‬
                                                                                         ‫لبریز اس‬
   ‫آردثور‬
        ‫بلخکه کلهای سفید مابل بسرخی دا‬
‫و کی گونند کل ان‬          ‫آزاد درخت ءیگوند‬
                                                    ‫سر شب = بروزن هرشب ؛ بمعنی‌شاهین‬
                       ‫درخت سر شك نام دارد ©‬
                                                                    ‫باشد وآن جالوربست شکاری ‪.‬‬
 ‫سر شك ‪ ۲‬تش ه کنابه از فطرحامی‬                      ‫بکر اول و انی بر وزن‬            ‫سر شت ‪۲‬‬
          ‫می‌چکد‪.‬‬    ‫است که از هیزم تر اش‬           ‫بهشت ‪ ,‬خلقت و طیئت و هاب طبع و طبیمت ‪۴‬‬
 ‫ترشی‬   ‫کنابه از‬    ‫انگیین =‬     ‫‪2‬‬                   ‫غطشوته‬
                                                          ‫وخوی آدمی راگویند ‪ -‬وبمعنی مآخلو‬
                                                                ‫و ماضیآغشته کردن هم حست‪* .‬‬
 ‫رسکه‬
    ‫چواشنیی است که مرکب ازآب وعسل و‬
               ‫باشد ‪ -‬و دوشاب را نبزگفته‌اند‪.‬‬      ‫ثالث بروزن فرقف ‪ .‬نام‬           ‫ح‬
                                                                                   ‫ففت=‬
                                                                                      ‫رش‬‫سب‬
‫سرشك شور ‪ -‬بکسکان‪ .‬کناب‬                            ‫غله‌ایت شبیه بخردل که روغن تلخ از آن کبرند‬
                                                                     ‫میباشد‪.‬‬        ‫سدروخ‬
                                                                                        ‫وکل او زر‬
                       ‫اازشك غمزدکان باشد‪.‬‬
                                                    ‫زرشث‬      ‫عننوی‬
                                                                  ‫موز‬
                                                                    ‫سر شك = بر‬
 ‫سشرکوان ‪ - ۱‬بکر اول ثوالی‬
‫وابع و واو بکالشفیده و بنونِ‬
                           ‫وکون ثالث ر‬
                                     ‫س‬
                                                      ‫یرس‬
                                                        ‫ارمیرالب‬
                                                               ‫بهبع‬
                                                                  ‫باشد‪ , .‬وآن لباتی‌است «عروف ک‬
                                                     ‫گوبند ‪ .‬و فانق آشپا کنند ؛ و بعضی ررخت‬
‫ه‌ای را کویند که درشب زفاف پیش‬
                             ‫زپدرهد»‬
                                                    ‫و بوتهٌ زرشك را سرشك میگوبند ‪ - ۴‬و مطلق‬
         ‫عروی بیاویززند ونآرا بعربی کله گویند‪.‬‬
                                                    ‫قطره را گویند عموماً و قطر۾ء باران و اشك‌چشم‬
 ‫سر شکون ‪ -‬بفتح واو و سکون نون»‬                     ‫را خصوصا ؟ ‪ -‬و بمعتی شراره و خرو آمشی‌بود‬
    ‫‪ ۱‬فی ‪ :‬اففالی ‪( 1151715) , 1‬طبیمت‪ ,‬مزاج)‪ ( 0156۳25 ,‬سریش‪,‬چسب‪.‬‬
   ‫چبن دگی) = ‪.60۳56125 , 7 . 58125‬ءعنی که تزددك است به ‪ ( 051۲۲ ۱ :‬بستن»‬
   ‫متحد کردن » متصل کردن) قی ‪ :‬ساف کریت ‪îrç‬‏ (آمیختن › مخلوط کودن) ‪.‬فارسی ‪ :‬سرشتن‪.‬‬
   ‫( ‪ ,‬فارسی ‪ :‬سرش‬      ‫)‪.‬اوستا ‪hsirs‬‏ (چبدن‬      ‫«( مالکرت ‪hsilç‬‏ ( آویزان بودن ۽ چبیدن‬
  ‫‪ 9۱‬گرچه سرشت رو ز گار برآن جماه آمد که‬             ‫‪۳‬‬         ‫ورك ‪ :‬سرشتن *‬        ‫«‪+‬هوشمان ‪۲۳۷‬‬
        ‫‪ = ۴‬زرشك («م‪. ).‬‬            ‫هیج فرزلد پند پدر خویش را د«رقنباندبد‪.‬و»سنامه ص ‪. ۱‬‬
   ‫ورك‪ :‬هویشمان ‪۳۳۷۰‬‬      ‫‪- ۴‬اوستا _ ‪(86158]5‬نگ رکه) ‪ ۶‬بارتولمه ‪« ۵۸۹۱‬اسشق ‪۳۳۷‬‬
                                                ‫سرشك فارسی شابد از پارتی ‪( 5۲5‬قطره) باشد ‪:‬‬
            ‫‪Henning, A list of Middle ۳6۲5۱۵9... BSOS, 126,1,‬‬                           ‫‪۰‬‬
   ‫درپهلوی )‪ ( 181۲5‬قطره ) « تیبرکه ‪ « . » ۹۰۲‬زرشك و سرشك » انبرباریس بود »‬
   ‫‪«- ۵‬سرشك‪ .‬قطرء آب چشم بود » وبکی کلی بود که پاره‌ای بسرخی‬                        ‫«لفت فری‪.*۹۰۳‬‬
   ‫زد ‪«,‬دیگر درخت کل رائیز کوبند وآزاد درخت‌بیزش کوبند ‪ .‬دبگر قطرة باران وقطر‪ :‬هرچیز‬
                                                                  ‫بود ‪ .‬عنصری (بلخی) کوبد ‪:‬‬
            ‫وآن سرشکش برنگه تازسرشك»‪.‬‬                       ‫نگائته برشك‬            ‫ردخیزده‬
   ‫« لفت فری ‪٩۲‬‏ © ‪.‬‬                                                           ‫‪۱‬‬
                             ‫‪ -‬رك‪:‬سرشکوان ‪.‬‬  ‫‪ -‬رك س‪:‬رشکون ‪.‬‬
  ‫کن اول و دوم ِ ِِِ ب>هلوی ‪[ 881215۳5‬رك‪ :‬سرشت ]ه‬ ‫کک ‪-‬‬
        ‫سر دکلنی ‪ma-xrix‬‏ ( آمیختن‪ .‬مخلوط کردن) «اسدق‪ -‬هویشمان ‪ ۲۷۷‬؛مخلوط کردنا‬
                                                         ‫ساختن ‪ -‬خمیر کردن ‪ -‬معجون ساختن ‪.‬‬

### leaf 577 ###
                                                                                                                        ‫‪۱۱۱‬‬     ‫‪6--‬‬
                                                                                                                        ‫‪۰‬‬
                             ‫ونهشت را نیزگوبند‪.‬‬              ‫‪-‬‬   ‫ات‬
                                                                                ‫حضممزه‬
                                                                                     ‫سر او‪ ۱‬صبفتح اول توانی و‬
‫اجان علفی ‪:‬یبش‬
  ‫یاه‬      ‫م‬         ‫خیاره‬        ‫‪۸‬‬
                                          ‫ا‬
                                          ‫‪۳‬‬       ‫ای‬
                                                       ‫رای‬                     ‫و سکون واو بر وزن سمنو » نام رودخانه‌است‬
  ‫به‬
   ‫او‬‫ند‬
      ‫کزن‬
        ‫که بکرنار فالیز و کشت وزراعت سا‬                                         ‫بکنار آن رودخانه وافست‪.‬‬
                                                                                                      ‫که شهر اوده ‪ ۴‬ر‬
                ‫از روز گارودلیا هم هت ‪.‬‬                                        ‫سر آوردن د کنانه از آخر شدن‬
                                                                                                              ‫وشهات رسدن باشد‪.‬‬
‫و کنانه‌از‬     ‫‪ ,‬شراسخائه وخرایات را گوند ‪۳‬‬                      ‫نقطه‬
                                                                              ‫سر او ند = بروزن زراوند ‪ ,‬ریگ زرد‬
                                                                                                                ‫را گونند مطلعاً و‪5‬‬
‫بکسر رابع بر وزن‬                        ‫*‪-‬‬        ‫سراش‬                         ‫سر آهنګ = بفتح اول وها وسکون‬
‫تراوش ‪ ۰‬بمعنی زبان قال است که سخن گفتن‬                                         ‫واف » تنشورازی و خوانند کی و دو بیت‬
                                                                                                                 ‫نون گ‬
        ‫و فغمه بردازی آدمیان وسرود مرغان باشد‪.‬‬                                 ‫خوانی رگاویند ‪ -‬و پیشرو لشکررا نکیفزته‌اند‬
‫ینم شین شله دار ‪.‬‬                 ‫‪-‬‬    ‫شرور‬       ‫سر ای‬
                                                                               ‫که بعربی مقدمة‌الجیش خوانند و بترکی‌هراول‬
‫و فمارخائه‬          ‫کنابه ازميکده و شرابخاله باشد ‪-‬‬                            ‫کو‪.‬ند ‪ - ۴‬ویمعتی‌عس وشبگرد هم آمده‌است‬
 ‫و کنانه از دنا ودوزخ هم‌هست‪.‬‬                     ‫را نیز گویند ‪۳‬‬               ‫فت ‪ ۴‬ت و تار انف را ف‬              ‫فا‬            ‫و سره‬
                                                                                                          ‫کویند که برسازها کشند ‪.‬‬
 ‫باعتبارشتی جیت که بالا ویابین وپیش وپس‌ورچپ‬                                   ‫بن جاه‬             ‫رای ام رجا‬
                                                   ‫باشد‪.‬‬     ‫و راست‬
                                                                             ‫باشد کهبعربی بیت خوانند‪ -‬و بمعنی‌خوانندکی‬
‫سر ای شمر ده = خانه ای را گوبند‬                                               ‫همست ‪٩‬‏ ‪ -‬و بمعنی سخن کوی‬
                                                                                                      ‫ورابیدن ه‬
                                                                                                              ‫س‬
‫را در آ تجا شمرده‌تليم‬                 ‫خود‬    ‫که رعاما ماز واجبی‬
                                                                               ‫و حرفزن که شاعر و قصه خوان باشد هم آمده‬
                                                                               ‫کیب گفته‬
                                                                                      ‫است ‪.۱‬لیکن دربن دو جا بدون ت‬
                                      ‫اهاده و بش ازو لبوده ‪.‬‬                   ‫نمیشود «مجو مدحت سرای وسخن سراییواهر‬
 ‫محمود*‪٩۶‬‏‬      ‫د ه مقامات‬              ‫سر‌ای مجمو‬                             ‫بباین دو سه معتی باشد عنی چیزی بخوان‬
‫است که خدابتعالیبحضرت رسالت یناه صلوات اف‬                                      ‫حرف بزن ‪-‬‬  ‫و خوانندگی کن و مدح بگو و‬
  ‫باشد ‪۰‬‬       ‫و کنانه از «پشت‬            ‫علبه وعده کرده أاست›‬                 ‫وئام شهریست بزر گك و حسن خیز درجانب‌شمال‬
                                                                                                                       ‫دارالملك تاتار ‪.‬‬
                                      ‫است که عالم جاوید باشد‪.‬‬                   ‫ساريان ‪ ۰ ۲‬بروزن کدابان خوانندکی‬
 ‫سر ای هفت ر خشان ‪ -‬کناه ار‬                                                    ‫وگوبند گی و شمه سرایی کنانرا کوبند ‪ -‬ونام‬
                                                       ‫آسمان اض‬                                           ‫جابی حم همست درخراسان ‪.‬‬
                ‫‪۳‬‬             ‫‪۰‬‬          ‫‪۹۱‬‬     ‫! دید ‪۰‬‬                         ‫دهشت‬
                                                                                       ‫سرای چاوید د کنابه از‬
 ‫نغمه پردازی و سخن‌سرابی وحرف زدن آدمیان‬                                                     ‫نة المآواست ‪.‬‬
```


## [2026-09-06T20:59:11.635Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor L in 596 597 598; do echo \"##### leaf $L #####\"; awk -v n=$((L+1)) 'BEGIN{RS=\"\\f\"} NR==n' BQT_v2_pages.txt | head -60; done"
}
```


### [2026-09-06T20:59:13.214Z] TOOL RESULT

```
##### leaf 596 #####
  ‫‪۱۳‬‬                                                                                        ‫سروشه‬

                                                         ‫و مصالع آن رو" بدو مقرر است خودهم بتدبیر‬
 ‫وح‌اول بمعنی‌سرین است که شت‌گاه‌مردمان‬            ‫=‬     ‫ومصالح آن‌روز می‌پردازد‪ .‬بنابرآن بجهت‌شرف‬
                         ‫وکفل چاربابان باشد ‪۰ ۴‬‬        ‫آن روز راعد کنند وجشن سازند » ولیزهر کدام‬
 ‫وتا‬      ‫ر‬     ‫کاله‬       ‫ك‬        ‫سر ونار‬             ‫از سروشها بمحافظت جوهری وعنصری مقرراست‬
  ‫راگوبند چه ناز بمعتی لورسته عم آمده | ت‬                ‫چنانکه خرداد بآرب مو کل است و اردیبهشت‬
‫سوروبرا یزکوبند که شاخپای آن بهر طرف‬                    ‫بآرتش و مرداد براشجار وبافی سروشرابمحافظت‬
                                                       ‫آیچه در بل نام آن سروش مقرر ات ‪ -‬ونام‬
                                        ‫ماوزسیقی ‪.‬‬      ‫ن بدست‌اوست‬   ‫اند‬‫گست ب‬
                                                                             ‫ملکی دز هست که ربا‬
                                                       ‫و تدییر امور و مصالحی که در روز سروش وافع‬
   ‫کوون‬
      ‫سروق = بفتح اول وضم اسنی‬
‫که شاخ‬        ‫است‬   ‫سرون‬       ‫ثالث و تحتالی ‪« ۰‬معنی‬
                                                         ‫رموز حفدهم باشد‬
                                                                       ‫است ‪ -‬و نا‬     ‫لق‬
                                                                                       ‫عدو‬
                                                                                         ‫تب‬‫عود‬
                                                                                             ‫می‬
                                                       ‫از هرماه شمسی ‪ .‬نك است دراعن روزدعا کردن‬
‫ویضم اول سرین و کقل‬        ‫‪-‬‬    ‫کوسفند و کاوباشد ©‬
                                                                   ‫ونبشآکده رفتن و بافی امور بداست‪.‬‬
                                    ‫هرد وچاروا ‪٩‬‏ ‪.‬‬

‫سر و یس د بااول و تحتالی مجپول بر‬                        ‫وه ‪ = ۱‬بن اولوفتح شین‌رشت‪.‬‬
                                                                                  ‫سر ش‬
‫وزن نوکیسه » قوس قزح رکاویند ‪ - ۷‬ومهر‬                    ‫بممنی سروش است جکبهرئیل باشد خصوصاً ‪-‬‬
                    ‫های سنگین را هممیگوند ‪.‬‬                                   ‫وملائکةٌ دیگر عموماً ‪.‬‬
‫سر ‪ = ۵‬بفتح اول وثالی » زر رایج تمام‬                     ‫سر ول ‪ -‬بفتح اولبروزن ملول‪ ,‬بمعنی‬
 ‫تسف‬    ‫عبار باشد»وآن نقیض قلب است که اسره‬               ‫حقد باشد»‌وآن بدکوبی و غیبت مردم در خاطر‬
‫‪ -‬وآب عمیقی که از سر مردم بگذرد ‪ -‬و هر‬                   ‫نگاهداشتن است وطالب فرصت‌بدی کردن بودن‪.‬‬

 ‫چیزی لیکو و راست و بی عیب ‪ - ۸‬و خلاصه‬                   ‫سر ون = بفتح‌اول بروزن زبون » بمعنی‬

                     ‫‪:‬‬   ‫‪ :‬سرو‬    ‫رك‬    ‫‪۴‬‬        ‫ترديك لفط اوستابی «سروش» («‪.‬م‪۲ ).‬‬      ‫‪۱‬‬

               ‫سرولی است بر رسته‌چون کر گدن‪.‬‬                 ‫ز پیشانی هربك از مرد وزن‬
   ‫نظامی کنجوی‪ .‬ک«نجینه ‪۸۸۰‬‬
   ‫‪ = ۴‬سرین ( «م‪ » ) .‬اوستا ‪ ( 1002۳3 -‬تپیگاه ) » پهلی ‪)ras‬‏ ‪01۲25 ۰‬‬
   ‫(سرین)‪,‬هندی باستان ‪( 1۵۵۳9 -‬سرین‪ ,‬ران » تپیگاه) ل»توانی ‪ , 5101212۹‬لانینی ‪610016‬‬
   ‫بوتانی ‪ » )( »51061‬بلوچی ‪ ( 0۵۲25‬کمر ؛ تپیگاه ) «اسشق ‪ .۷۳۷0‬هوبشمان‌کوید ‪ :‬سیت‬
       ‫شن‬
        ‫دایومن‬
             ‫فظرسی «سرین» ‏ بلوچی ‪ 06725‬از ‪ # 6۳5‬و فارسی «سرون »از ‪ ۵ 00۲5‬بر‬
                                                                           ‫یت «حوبشمان ‪: ۷۳۲۷‬‬
               ‫گرچه برتابد آن میان وسرون‪.‬‬                      ‫کفش با سلاح بشکفتم‬
   ‫شهد بلخی‪«.‬لفت فرس ‪۹۷۳٩‬‏ ‪.‬‬
                                   ‫‏‪ « Cupressus sempervirens = ¢‬یتباث ‏‪. “AY‬‬
   ‫‪ - ۷‬مصحفهسد که»‬                ‫‪ -‬رك‪ :‬سرون ‪٩‬‏ سرین ‪.‬‬            ‫‪ _ ۵‬رك ‪ :‬سرو ‪ ۰‬سرون ‪.‬‬
                                                                              ‫س دکیس («‪.‬م‪۱ ).‬‬    ‫>‬

               ‫پیرزن کرک باشد‪ .‬او بره بود‪.‬‬                  ‫‪ - ۸‬مادرم کفت کو زلی سره بود‬
       ‫تظامی کنجوی‪ «.‬کنجینه‪»۸۸‬‬
   ‫(برهانقاطع ‪)۷۴۱‬‬

##### leaf 597 #####
  ‫صری‬                                                                                 ‫ه‬
                                                                                      ‫ا‪۱‬‬‫‪۳۱‬‬
                                                                                         ‫‪-‬‬


 ‫سر هنګ رک بروزن‌فرهنگه ؛سردار‬                     ‫پوسندیده و برگزبده واعلی وفیس باشد چذان‬
‫پویشرو لشکر و سیاء باشد» چه هنگه بمعنی‬            ‫وعبیدب‌دار را یابه گویشد‬ ‫که هرچیز زیون و‬
‫سپاه لیز آمده است ‪ -‬و بمعنی پهلوان و مبارز‬        ‫‪ -‬و شقة حریر سفید علم را یز میگوبند ‪٩‬‏ ‪-‬‬
                                   ‫همکفته‌اند ‪.‬‬
                                                  ‫و بمعنی اصل هم آمده است چنانکه فرع‌راپابه‬
                                                                                      ‫خوانند ‪.‬‬
 ‫سرق = بفتح اول بروزن پری» سرداری‬
                                                  ‫هرال ‪ -‬باهای بالف کشیده بروزن‬
                                                                              ‫س‬
‫سوپهسالاری باشد ‪ - ۴‬و بمعنی سرای هم هست‬           ‫ابدال " مردم سر کشته وسر کردان را گوبند ‪-‬‬
‫که خانه باشد ‪ - ۴‬و چیزیرا یز کویند ازآهن‬
                                                  ‫را‬       ‫ك‬
                                                           ‫لو‬‫فت ‪-‬‬
                                                                ‫و بمعنی کردون هآممده اس‬
‫بندند ‪ -‬و نام‬      ‫سرب‬
                     ‫رس‬‫با‬        ‫گزه‬
                                   ‫نر رو‬
                                       ‫جد‬‫که‬       ‫یز گفته اند‪ -‬وهر چیز را میگوبن دکه همیشه‬
 ‫‪¥.‬‬   ‫©‬    ‫مشهورسری‌ستملی‬   ‫بکی‌از اولاوافه إت‬
                                                                               ‫درگردش باشد‪.‬‬

          ‫بقول اصمعی «سرق» لوعی ازحریر " معرب «سره» پارسی است‪« .‬این‌درید»‪. ‎‬‬      ‫‪٩‬‬
  ‫‪ _ ۴‬رك‪ :‬سرآهنگه ‪« :‬خداوند برآن‌نده خشم کرد وغضبناكشد واورا در دست‌سرهنگان‪‎‬‬
  ‫از ‪ :‬سر (راس) ‪ +‬ی‪‎‬‬        ‫‪۴‬‬           ‫یداد تااورا شکنجه دهند ‪« » .‬انجیل فارسی ص ‪. ۴ 4۸۱‬‬
 ‫© _ رك ‪ :‬تذ کر الاولیاه عطار‪‎‬‬          ‫رك ‪ :‬سرای ‪.‬‬    ‫‪۴‬‬        ‫(مصدری) ؛ رباست » سروری ‪.‬‬
                                                             ‫پاچ ندیل ج ‪‎ ۱‬ص ‪۷۲۸۸ ¬ ۲۷4‬‬
 ‫‪ #‬سریالی ‪ -‬بضم اول » منوب بسورستان ( عراق وبلاد شام ) « ممجم البلدان » ‪ .‬نام‪‎‬‬
   ‫فومی سامی نژاد که با قوم آرامی خویشاوند بودند ولهجةٌ آنان را لیز سربانی ‪6110317795‬نامند‪‎.‬‬
  ‫ابن لپجه‌از لیجه‌های مهم آرامی شرقی است و در ابران از خود آرامی معروف تراست و چون‪‎‬‬
 ‫آنار ابن لهجه نسبة متأخر است » آثار پیشن آرامی را رفته رفته از بادها زدوده » جاندین آن‪‎‬‬
   ‫کردیده است ‪ .‬خبطیرکاهی لوشتن سربالی بکار میرفتهبااند تفییراتی هآمرانامخیط‌است‪‎‬‬
 ‫(ك ‪ :‬آرامی برابرص ‪ .)۶۳‬مرکز این لهجه درشمال عراق (بن‌النهرین) ذپر ادا‪۲06552 ‎‬‬     ‫ر‬
 ‫اورفا نامند ‪ ۰‬در قرن‪‎‬‬  ‫ن‬ ‫و‬          ‫ه‬ ‫د‬        ‫ی‬ ‫م‬    ‫ب‬ ‫ت‬
                            ‫و درک اسلا الرها خوان شده وکان‬     ‫‪1‬‬ ‫‪3‬‬    ‫ی‬ ‫ل‬
                                                                   ‫است که در سربا ‪۲0‬‬
‫دوم میلادی این شهر یکی از مراکز مهم عیوبان کردبد و در چندین قرن پیش از آن » از‪‎‬‬
 ‫زمان اسکندر جوانینان وی سلوکس و انتبوخس‪ ,‬شمال بن‌النپرین از مراکززبان سربالی‌بوده‪‎‬‬
 ‫و بواسطةٌ مپاجرت گروهی از مردم‌ان مقدویه وبودان درآن سرزمینها » سربابی رنگه و روی‪‎‬‬
 ‫خاصی کرفت و بر دبگر لپجه های آرامی برتری بافت و بیاری از لغات بونالی بازبان سربالی‪‎‬‬
 ‫در آمیخت‌وتفییری در انشاء واسلوب آن یدید آمد ‪ ,‬آنچنانکه در تحریر مسائل دینی وفلسفی‪‎‬‬
 ‫و علمی زبالیرسا و روتمند کردید ‪ .‬خط سربالی هم اخزط یونالی متأثر کشته برای کتابت‪‎‬‬
 ‫‪N5115‬‬   ‫بپتر و روشنتر شد ‪ .‬دیگر از مراکز مهم سریالی‪ ,‬شهر روحانی عیسوبان شرقی‪ .‬صبین‪‎‬‬
 ‫ات ‪ .‬آثاری که بزبان وخط سربالی برش از لفوق دین عیسی بجای مانده نبة الدك است " اما‪‎‬‬
  ‫آثار پس ازآن عبد که غالباً ترجمه و تفر توراة و ااجبل ومائل‌دینی وسرود های مذاهبی‌است‪‎‬‬
‫بسیار است ‪ .‬وهمچنین در ادبیات وتاریخ وعلوم بکاادرهای کرالبهابی بدین زبان بافی مانده » از‪‎‬‬
 ‫جمله اسکنترنامة مجمول و متسوب بکالیستنس » نرجمة سربانی قالون مدلی زمان ساسالیان که‪‎‬‬
 ‫مترجم آن یشوع بخت ایرالی سطوری است ‪ .‬مانی مشهور کشتشاب خود رابزبان سربالی‌لوشت‪‎‬‬
‫چون در آن زمان زبان سربالی درمغرب ابران زبان علمی ‌ ادبی بود ‪ .‬حنوز هم در بسیاری از‪‎‬‬
 ‫یه درصفحةٌ‪۱۱۳۹ ‎‬‬

##### leaf 598 #####
    ‫‪-۱ ۱۳۹‬‬
‫هآممده است ‪ ۵‬و‪-‬نام ولابتی وجایی‌بیز هت‬                         ‫»ن درمچه ‪ .‬نام جانوری‬   ‫بررچوز‬  ‫س‬
      ‫ویمربی‌آور‬    ‫‪-‬‬   ‫‪۹‬‬   ‫که فارکیضرو آنجا است‬
                                                              ‫است پرنده وکوچك جثه و دراز دم که یشتر بر‬
                                  ‫و تخت راگوبند ‪.‬‬
                                                               ‫کتارهای آب شیند ودم جنباند وآنرا مرغ‌فاطمه‪.‬‬
‫سریرافراز = بزای شله دار (‪)۱‬‬                                                  ‫خوانند ورحربی صموه کوبند ‪. ۱‬‬
‫و‬      ‫و غاری که کی‬            ‫در آخر » نام شهربت‬

‫ن آن رفت و غاب شد در نواحی آن شهر‬                               ‫یه ‪ ۴‬مشسبلاخمادیار بورزن‬
                                                     ‫بدرو‬
                                             ‫‪Y۷‬‏ ‪.‬‬       ‫ات‬   ‫خلیفه » مرخ سقارا گویند» وآن پردماست که‬
‫سر یرفلك ‪ -‬کنابه از بنات‌النش‬                                  ‫درفك اسفل او بعثی درزیر منقار زبرین‌آوپوستی‬
                                                                                   ‫بمالند مشگیجه آوبخته است‬
‫صورت‬        ‫ستاره باشد شمالی‬          ‫است» ‪ 3‬آن هفت‬
                                             ‫چو کان ‪۰‬‬          ‫سر یف ‪ ۴‬هوسزبنر‌کشید ‪ .‬جامة غوك‬
‫= بر وزن حربری » نام پادشاه‬                                     ‫دبرهای‬
                                                                     ‫کاوند » وآن چیزی باشد سبز که آ‬
                                                                                                  ‫ر‬
                                         ‫ری‬
                                          ‫سر‬
‫سربر افراز است ‪ - ۸‬و منوب بسربر را یز‬                          ‫اینتاده بهم رسد ‪ -‬و رسمانی که اطفال از جابی‬
                               ‫کول‬                                    ‫آویز ندوبرآن شته در هوا آیند وروند‪.‬‬

‫بش د بکسر اول و ثانی و سکون‬                                     ‫سر بر = بروزن‌حردر»بمعنی سروسه ‪۴‬‬
                            ‫سر‬
‫(‪ » )۷‬رستنیی باشد ® كەدر‬              ‫ثالك و شین قرش تت‬        ‫است که قوس قزح باشد و باين معنی بکسراول‬
                                                     ‫(چك ‪ -:‬قرشت ‪.‬‬
                                                                 ‫‪) .‬‬               ‫(‪ )۱‬چك ‪ :‬بازا‪.‬‬              ‫‪۱‬‬
                                          ‫ی و کرت‬                         ‫و ا‬              ‫ر‬
              ‫بانگه سریجه خاسته السرسرای او ‪>».‬‬                       ‫کشته پلوك باره بان سرایچه‬
     ‫‪. ۴‬‬   ‫‪ ۶‬لضت فرس ‪۳۰۵‬‬                                         ‫سر بحعه؟ («‪.‬م‪).‬‬    ‫‪ _۴‬ظ » مصحف‬
                               ‫‪ :‬سرویمه‪:‬‬    ‫رك‬       ‫‪۴‬‬           ‫‪ ,‬مصحف سر ند* (ھ م‪).‬‬        ‫‪۴‬ظ‬
    ‫آوردء» رك‪ :‬سروب ه»سر کیس‪.‬‬             ‫‏‪ e».‬درسامی دمعنی فوس قرح‬      ‫® ‪ -‬رشیدی گوبد‪«:‬سر یر‬
    ‫‪ - ۷‬در اصل «سریرسرافراز » مأخوذ ازین‬                          ‫‪۰‬‬   ‫آ_ رك ‪ :‬حدودالمالم (فهرست)‬

                                                                                         ‫بیت نظامی گنجوی ‪:‬‬
                   ‫وجام او ‪.‬‬    ‫ختضرو‬
                                    ‫دکرویتخ‬                            ‫سربر سر افراز شد نام او‬             ‫‪۱‬‬
     ‫« گاجینه ‪ » ۸۸‬ورك ‪ :‬سریر ‪.‬‬                                            ‫‪ - ۸‬دژبان فلعاً سریر ‪:‬‬
             ‫برآن‌تختگه کرد خواهد گذار ‪.‬‬                               ‫سربری خبر یافت کان تاجدار‬
     ‫ظامی کنجوی‪ .‬ک«نجینه ‪.*۸۸‬‬
                                  ‫‪.‬‬    ‫رك‪ :‬سرشت‬      ‫^ = ‪« 1600۵۵5۸‬کل گلاب ‪. ۲۸۱‬‬
                                                                                         ‫بقیه از صفحةٌ ‪۰۳۷۱۷‬‬


     ‫سرزمین های عربی زبان » لهجة سربانی وجود دارد ‪ ۰‬لهج آشوربہا و کلدایهای سوربه و عراق‬
     ‫وتر کیه وابران سربانی است ‪ .‬لهجةٌ سربانی آشوربها بالیجةٌ سربانی کلدانیها اندكتفاولی‌دارد‪.‬‬
     ‫امن لپجه درسرزمینهابی که بر شمردیم بازبانهای محلی چون عربی وفارسی و ترکی آمیخته‌شده‬
     ‫و صورت « سربانی لو» در آمده است ‪.‬رك ‪ :‬فاب اص ‪ .۱۹۱-۷۷۱‬خوارزمى كوبد «‪:‬السربالية‬
     ‫الذين ‪.‬يقال لاهلمنبط » وبهاکان بجری كلام حاشية الملوك ااال واالحوائج و شکوی الظلامات‬
                                                                         ‫مفائیم ‪. > ۵۷‬‬    ‫لاا املق الالسنة ‪.٩‬‏‬
```


## [2026-09-06T20:59:31.701Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==600' BQT_v2_pages.txt | head -70"
}
```


### [2026-09-06T20:59:33.209Z] TOOL RESULT

```
                                                                                          ‫پا احد‬

‫شنجرف سوخته است » بعنی شنجرف عملی‬                    ‫بخورند وبعد‬       ‫مات‬
                                                                         ‫منداوب‬
                                                                              ‫سبزی وتاز کی بیز‬
 ‫که آنرا اسزیماب سازند نآهنکه اکزان‬                 ‫کفش‪-‬‬     ‫سازند و‬   ‫کنند وآرد‬    ‫از رسد کی خشك‬


                                      ‫برآ ورند ‪.‬‬     ‫چبانند ‪٩‬‏ ‪-‬‬       ‫ان‬
                                                                        ‫بزدها‬
                                                                            ‫چی‬        ‫فان‬
                                                                                        ‫حناو‬
                                                                                           ‫کصرا‬

   ‫لی‬
    ‫االی‬
       ‫تر ث‬
          ‫حلوک‬
             ‫تاو‬
               ‫ونم‬
                 ‫سرلن ‪- ۴‬ب‬                                                                    ‫‪.‬‬    ‫جلد‬
 ‫ولون ساکن » شتگاه آدمی‪ -‬و کفل وساغری‬
                                                    ‫سر لع ه بفتح اول و کر انی وسکون‬                  ‫‪۰‬‬
                      ‫حیوانات دنکر ‪ ۴‬ك‬
                                                     ‫تحتانی ر غین اقطه‌دار ‪ ۰‬خوشه انگور بردأله‌باشد»‬

  ‫سر یانفکندن کدنایه اززاچانرو‬                           ‫بند خوش انگوری باهشدنکوهز‬
                                                                                 ‫وضی‬
                                                                                   ‫کبع‬
                                                                                     ‫و‬
                           ‫شتن باشد ‪.‬‬     ‫مرب‬
                                            ‫و‬                            ‫‪.‬‬   ‫درست لشده بادث‬       ‫دالهاش‬

‫سر بنگاه = بمنی مطلق شتگاه باشد‬                     ‫سر یقون ‪ « ۲‬بفتح اول و ضم قاف‬
  ‫عموماً ‪ -‬وبمعنی تخت بادشاحان پود خصوصاً ‪.‬‬          ‫وسکون واو و لون » لغتی است سربالی وبمعنی‬


                                              ‫بيان دهم‬

 ‫سز گی پ=قتح اول و سکون‌انی وکاف‬                    ‫سز ا * ‪ .-‬بفتح اول بروزن جزا ء پاداش‬
 ‫سختی ورلج‬         ‫نی‬
                    ‫مهع»‬ ‫فارسی بتحتانی رس‬
                       ‫بید‬                          ‫را‬     ‫فق‬
                                                            ‫وارا و‬
                                                                 ‫مزاو‬
                                                                    ‫لا‪-‬یق وس‬
                                                                           ‫وشد‬
                                                                             ‫نیکی و بدی با‬
                                   ‫وآزار باشد ‪.‬‬                                        ‫لىز گونند ‪۴#.‬‬

‫سز بتونتن ‪ - ۷‬بافوقانی و دونوتای‬                         ‫دیاول‬
                                                             ‫اول و سکون ان‬          ‫=ح‬
                                                                                     ‫برفت‬
                                                                                        ‫س‬
‫فت زند‬  ‫قرشت ( ‪ ) ۱‬بر وزن پربرو فبکنل‪.‬‬              ‫ابجد ؛ بمعنی جاوزد باشد که سفید خار و خار‬
 ‫وپازند (‪)۲‬بمعنی رفتن است که درمقابل آمدن‬           ‫سفید است ‪ -‬و بفتح اول و انی بمعنی می‌سزد‬
                                      ‫باشد (‪,)۳‬‬                    ‫باشد ‪٩‬‏ یمنی لابق وسزاوار همست ‪۰‬‬




       ‫(‪ )۳‬چش ‪:‬آمده است‪.‬‬                ‫)‪ (+‬چك ‪ :‬ژند وباژند‪.‬‬             ‫‪ :‬و تا ‪.‬‬   ‫(‪ )۱‬چك‬



    ‫‪ ۳‬سرون (ه‪.‬م‪.).‬‬     ‫‪۳‬‬           ‫رك ‪ :‬سلیقون ‏ زرفون‪.‬‬        ‫‪۴‬‬             ‫ره‬     ‫ارك‬


           ‫سرین دهان ز در منضد کند همی‪.‬‬            ‫سوسن سرین زبیرم کحلی کندهمی‬            ‫‪۴‬‬
```


## [2026-09-06T21:00:12.054Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== leaves containing hsilç / hsirs (śliṣ / sriš OCR) ===\"; awk 'BEGIN{RS=\"\\f\"} /hsilç|hsirs|îrç/ {print \"leaf \"NR-1}' BQT_v2_pages.txt\necho \"=== page numeral scan leaves 584-600 ===\"; for L in 584 586 588 590 592 594 596; do echo -n \"leaf $L: \"; awk -v n=$((L+1)) 'BEGIN{RS=\"\\f\"} NR==n' BQT_v2_pages.txt | head -3 | tr -d '\\n' | head -c 120; echo; done"
}
```


### [2026-09-06T21:00:13.818Z] TOOL RESULT

```
=== leaves containing hsilç / hsirs (śliṣ / sriš OCR) ===
leaf 586
=== page numeral scan leaves 584-600 ===
leaf 584:  ‫‪“NYY‬‬                                                                                                     
leaf 586:    ‫)‪۷۱‬ات‬‫که بجمد و جهنده باشد ‪ -‬و نام درختی است‌در‬           
leaf 588:  ‫‪۷۱۷ ۷۹‬‬‫و سرزش کردن و طعنه زدن را یز گوبند ‪-‬‬                     �
leaf 590:     ‫اس‬     ‫م‪۷‬‬                                                                                     
leaf 592:    ‫‪ ۳۱‬ات‬ ‫و لبلابرا نیزکوبند‪,‬وآن‬    ‫حطی حم آمده است ‪-‬
leaf 594:    ‫‪۰‬؟(‪-۳۱۱‬‬                               ‫‪o‬‏‬    ‫‪«.‬‬                     
leaf 596:   ‫‪۱۳‬‬                                                                                        ‫سروشه�
```


## [2026-09-06T21:00:18.628Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== FFD pdf page 65 (printed p.60) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==65' incoming/FFD/FFD_pages.txt\necho \"=== grep sriš in FFD ===\"; grep -n \"سریش\\|سرشتن\\|sriš\\|sraiš\" incoming/FFD/FFD_pages.txt | head -20"
}
```


### [2026-09-06T21:00:20.291Z] TOOL RESULT

```
=== FFD pdf page 65 (printed p.60) ===
[pdf page 65]
انا انا فعلهای فارسی دری
«ستاند» ج «ستانید» مادهٌ ماضی جعلی از «ستان» است.
۱ ستودن
ستود + فارسی میانه 5100 < ایرانی باستان ۹18-12*. برای 2 آراست. صورت
ضعیف 514۷ است و ريشهٌ 912۷ به معنی «ستودن» است.
ستای < فارسی میانه 513 < ایرانی باستان 8ر813۷-۵*. 278 نشانه‌ای بوده که
برای ساختن مادهٌ مضارع از ريشه به کار می‌رفته است. ‎٩13‏ صورت بالاندةٌ ریشهٌ 312۷
است.
دا
سخت + فارسی میانه 3231 < ایرانی باستان ۶۵-1*. برای ۵ > آراست. 8 صورت
اصلی است و آن صورت ضعیف ريشهٌ 8 به معنی «کشیدن» است. برای
ضعیف‌کردن ريشه 8 حذف شده است.
سنج + فارسی میانه [828 < پهلوی اشکانی [8۵2 < ایرانی باستان ۵-[۶28*. برای 8 ->
آرای. [به جای ج آمده است.
سرشتن
سرشت < فارسی میانه 85151 + ایرانی باستان ۶713-1۵*. برای ۵ > آراست. کزرّه
صورت ضعیف ريشةٌ 8788 است و آن به معنی «چسباندن» است.
سریش < فارسی میانه 8783 < ایرانی باستان ۶۲۵15-2*. برای 2 > آرای.
«(سریش)» به معنی «رستنی‌ای که ... بعد از رسیدگی خشک کنند و آرد سازند و
کفشگران و صحافان چیزها بدان چسبانند.» (برهان قاطع)» از ریشهٌ 788 است.
سرودن
سرود + فارسی میانه ۶734 < ایرانی باستان ۹۳8-1۵" برای 1۵ > آراست. ‎٩۳3‏
‏صورت ضعیف ريشةٌ 818۷ است. به معنی «خواندن».

=== grep sriš in FFD ===
1636:سرشتن
1639:سریش < فارسی میانه 8783 < ایرانی باستان ۶۲۵15-2*. برای 2 > آرای.
1640:«(سریش)» به معنی «رستنی‌ای که ... بعد از رسیدگی خشک کنند و آرد سازند و
```


## [2026-09-06T21:00:31.777Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== v3 leaves with کلید ===\"; awk 'BEGIN{RS=\"\\f\"} /کلید/ {print \"leaf \"NR-1}' incoming/BQT/BQT_v3_pages.txt | head -30\necho \"=== faseng ===\"; ls incoming/BQT/ | head -20"
}
```


### [2026-09-06T21:00:33.493Z] TOOL RESULT

```
=== v3 leaves with کلید ===
leaf 289
leaf 290
leaf 399
leaf 424
leaf 432
leaf 433
leaf 472
leaf 473
leaf 479
leaf 480
leaf 523
leaf 532
leaf 573
leaf 613
leaf 635
=== faseng ===
BQT_v3_pagemap.json
BQT_v3_pages.txt
BQT_v3_picofile.pdf
BQT_v4_pages.txt
BQT_v4_pages.txt.pages
BQT_v4_picofile.pdf
BQT_v5_pages.txt
BQT_v5_pages.txt.pages
BQT_v5_picofile.pdf
```


## [2026-09-06T21:00:36.034Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor L in 479 480; do echo \"##### leaf $L #####\"; awk -v n=$((L+1)) 'BEGIN{RS=\"\\f\"} NR==n' incoming/BQT/BQT_v3_pages.txt | head -60; done"
}
```


### [2026-09-06T21:00:37.730Z] TOOL RESULT

```
##### leaf 479 #####
[pdf page 480]
—\ur—

تانی ‎Sash‏ خمیر آن از دبوار تنور افتاده ودر
‎Ole‏ آش پخته شده باشد ‎٩‏ - و دان بز رکه
روغنیرا 55 کوبند ۴ - و بکر اول و تحتالی
مجهول, اسبی راکوبند که هردو پای او کچ
باشد ۴ .

HS ‏بنتح اول وجیم فارسی‎ - GT
‏چرین را گویند ۴ که بدان کلیدابرا بگشایند‎
‏رضم اول نان کوچك روغتی‌باشد 6 و کنابه‎ -
‏از قرص ماء وآفتاب هم‌هست ۲ ؛ وباین دومعنی‎
‏با کاف فارسي همآمده است - و جامه‌ای را لیز‎
-۲ ‏وین کهآ نرامانند سوزن ی آجیده کرده‌باشند‎

کلیدانه
‎ae,‏ را هم کگفتهاند .

‎dr‏ سیم ه کنابه از ماه شب
چهاردهم است. #

‏کلیدان ‎A‏ - بفتح اولبروزن‌حریفان»
کنده‌ای را گوید که برپای دزدان و کناهکاران
بهند - و بکر اول آلت بست و کفاد در باغ
و در کوچه و امثال ‎UT‏ گونند و بعربی غلق
خوانند ‎٩‏ - وقفل را نیز کنته‌اند ‎٩‏ .

‏کلیفا4 ‎oh‏ بروزن دلیرانه : بمعنی
آخرکلیدان است که قفل وغلق درخانه باشد.

‎mm ۱‏ کلییه ‏ کلوج :
کریم ی که بر سفر# عم دارد

‏کلیچ از مه ‎SVT Gy‏ کلیچه .
ابوالملاء گنجوی « رشیدی *.

‏۴ - قن ‎az lS:‏ ( در تداول ‎jae‏ حاشر).

‏۴ - پیش رخش نو سبزخنکه فك

‎. ‏بان کلیج‎ oy A, KS

‏عجدی مروزی « رشیدی ©

‏۴ رك : رشیدی .کردی ‎killj‏ (کلید) روسی ۷106 ‎(os)‏ « ژابا ص۳4۱*.
‎GIT 9‏ < کلیج , ررك : کلیچه در مهذب‌الاسماه معنی فارسی ۶ فرص را کلیچه

‏توشته و در يك ساب کهنه این شعرهست :
قفول باز بگردبدن و افول غروب

‏و در ده کهنة صاب‌الصبیان این شمر هست :
دابوغه خربز آمد و بطیخ خربزه

‏چنالکه قر سکلیچه . سمیدنان‌سپید.

‏چون ‎BLS‏ وقرص کلییچه. لبا فله.

‏پس در قدیم کلیچه ‎pines‏ مطلق کرد نان بوده « فرهنگ نظام > .

##### leaf 480 #####
[pdf page 481]
کلید ایمان
‎ALT‏ ایمان ‎ats‏ از کل شهادت

باشد .

کلیژ » بفتح اول بروزن ‎oe‏ بمعنی
زبور باشد ‎٩‏ .گویند اگر زنبوری برموش‌مرده
شته باشد و کیرا ‎Be GTS SS‏ شود.

کلیز دان » با دال ابجد بر وزن عزیز
خان . ‎UE‏ زنبوررا کویند چه ‎AT‏ بمعنی زنبور
‎ath‏ .
کلیزه « بقتح اول‌بروزن عریضه,سبوی
آب راکوت ۴ .#

‎Ko Fle‏ اول و ثانی بتحتانی
مجپول رسیده و سین بی‌نقطه بالف رمیده:مخفف
‎LI‏ است که جای پرستش و معبد ترسایبان
‎me‏ :

‎pie = CAAT‏ اول بروزن شربك .تشم
کل راگویند وعربان‌یزرالوردخوانند سوپرنده‌ای
را یز گوبند که بنحوست مشهوراست وآنراجفد
‎Gs‏ وبوم ‎PaaS ws‏ - و بمعنی‌کاژ و ‎EP‏
‏واحول هم ‎he‏ آمده است ۵ - و بکسر اول 1
هم ‎onl‏ معتی که احول باشد - وهم‌بسمتی‌انگفت

‎٩‏ - آن ‎Sage‏ درحلاوش ست بدل
‎OT lala»‏ تخم کلیز عمل است

‏روا

‏کوچك بوذکه بعربی ختص کوشد ۷ .
کلیکان ‎che‏ اول بروزن کنیزان ,
کیاهی باشد بغایت گنده و بدیوی که آنرا کمای
و کل گنده ‎js‏ کویند - وبکسراول. سبزیی‌باشد
معروف کهخورند وآنرا ‎Slate‏ ترخان ی گویند؛
‎samy‏ گویند کیاهی باشد کهآ نرا طرخون‌خوانشد
وییخآ نرا عافرفرحا نامند . ۱
کلیکرون * بکسراول وفتح رابع‌ورای
بی نقطه بواو کشیده وبنون زده » بلفت بونالی
رستنیی باشد که ‎OT‏ را کهزك خوانند وآن‌خردل
بوستالی است.آب آنراگرفته درپای درخت انار
ترش بریزند شیرین شود وبسنی گویند ‎Dyes‏
‏است که بزبان عربی جیرجیر خوانند.
‎EIT‏ ۲ » بروزن حتیتی,کاج واحول
راگویند هرچند می‌بایت که بمعنی احولی‌باشد
چه کليك بممنی احول است لیکن همه‌جا یمعنی
لوچ و احولآمده است واین‌هم درست است.
کلیم ۵ست = بمعنی ‎Soler‏ دست‌ونادر
دست و پا کیزه دست باشد بعنی در کارها بدیضا
‎A ls‏
کلیواج 8 با نات مجهول, بروزن
بارب نرسك بپیچ نوعیش خلل
کدانهاز آن‌شود کدوهای‌عسل.
در صفت خریزه « جهانگیری *.

‏۴ - رك : ‎sat,‏ کردی 66102 (کوزه ؛ سبو) « ژابا ص ۳۸۱ . قس :کراز(هیم).
```


## [2026-09-06T21:00:45.964Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==479' incoming/BQT/BQT_v3_pages.txt | head -70"
}
```


### [2026-09-06T21:00:47.470Z] TOOL RESULT

```
[pdf page 479]
کل هكوشة ملك هو
کله گوشة ملاك - ‎gin‏ میم .کنابه لیا - بکسر اول وسکون ‎gt‏ وتعتانی
از پادشاه زاده باشد . بالف کشیده , به‌عنی شخار است که قلیا باشد
‎oS"‏ هشکین- ‎ga‏ اول و تج ‎ta» GU‏ صابون یزان بکار ‎Vary‏ - و بلغت زلد

. ۷ ‏وپازند گوسفند را کوبند‎ se
. ‏مشدد . کنابه از زلف وکا کل است‎

‎j ۱‏ ۱ ۰ . گلیاس = بکس اول پروزن فرطای »
‎is ne‏ نیلوفری ۳ | ‎yin‏ درخانه ‎Aust‏ وادبخانه را یز گوبن که

‎ ۸دنناوخ ‏بربام خان‌سازند و آنرا بعربی کربای‎ eee

‏ضم ۱ ثالی ‎Le‏ ۰ ۲

‏۲ کلی ‎Ge GUS ete ote‏ اول بروزن مهمالی .
پمعنی دهی و روتتابی باشد چ* ‎tne, | EST‏ اشق است وآن صمغ کیاهی که آنرابدران
و روضتا (۱) هم‌آمده است ۴ - و عرباله را نیز ۲ ۲ تا

‎. ‏کویند و بمربی صمغ الطرئوث خوانند‎ oo

‏گویند و آن‌دایره‌ای باشد حلفه‌دار که‌یشترعربان ‎ei‏
‏نوازند ۴ - ونوعی‌ازماهی هم‌هست وآن‌پر کوشت یاوه * = بنتح اور وآخر که ‎aly‏
‏و کوچك ‎athe‏ و خوردتش قوت شهوت ومد | ‎Seah‏ وید رین ی کسی که ‎GS‏ اوشنود
‎WT,‏ عربان سمك رضراضی خوانند - ودا عاتی | «بعربی اسم‌خوانند *۱.
و مرضي‌هم‌هست که آلرا خوره گوبند ۴ -وقرس کلیچ = بنتح اول وثانی بتحتالی کشیده
‎vb‏ روغنی بزر که را هم گفته‌اند * و بفتح اول | وبجیم زده , صاحب عجب وتکیر وتجبرروخودستا
یمعنی کچلی باشد وآن ‎le‏ است‌ممروف که در | باشد ‎-٩۱‏ وبمعنی ‎ae‏ و ریم هم آمدماست۱۱:
سر اطفال بهم میرسده . و پاینمعتی با جیم فارسی نی زکفته‌الد - وض‌اول

‏(۱) چش : روستاگی .

‏۱ - بکراول . ۴ رك :کل .

‏۴ - من ازآن ساده دلی ببهده برهرسخنی پای میکوبم چون ‎IAS‏ برنای کلی.
فرخی سیستانی . رك : رشیدی » فرهنگ نظام ‎(AS)‏ . دیوان فرخی نچاپ عبدالرسولی ص444
و دخ خطی ‎Fs‏ در نسخة سروری مرض معروف که آنراجذام خوانند «رشیدی»

‏کله ‎ne)‏ معنی) : « و چون عیی دریکی ازشهرها بود ۰ آمدیکی مرد از کلی جدام پر
بود ؛ عیسی را دید ... وگنت : ای خداوند ! اکر بخواهی بتوانی مرا پاك کردانی . عسی‌دست
خود بر‌آورد 9 بد و گفت خوامتم , پاك شو ! همان ساعت کلی ازو رفت و با شد ... »۶ انجیل
فارسی‌س*۵* - ‎ge Lege‏ الجیل‌بجای این کلمه ‎Legos dry?‏ فرانشوی 160۲6 آورده‌اند.

‏۵ از :کل (کچل) ی ( اسم مسدر ‎٩ A‏ -رك ‎Ub:‏

‎AW Gy « (arg) ۷۵۱۱092 . ۷2۱8 jy ۷

‏۸ مبدل (عی) « کربای » بالکس خلا جای بر بام که کاریز ‎OT‏ بر زمین باشد . *
۶ منتهی‌الارب *. ‎٩‏ کالیوه ‎Ceo)‏ .

‏*۶- ای طوطی ‎ge‏ نفس » وی بلبل شیرین نوا

‏ین زهره را کلیاوه کن » زین شمه‌های جانتزا .
مولوی بلخی‌رومی « رشیدی » > فررهنگ‌نظام >.

‎«gi =‏ مخفف‌آ نکلج س کلچ .۰
```


## [2026-09-06T21:00:58.209Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==480' incoming/BQT/BQT_v3_pages.txt | sed -n '1,200p' | grep -n \"کلید\\|klid\\|kliy\\|κλ\\|یونان\" "
}
```


### [2026-09-06T21:00:59.994Z] TOOL RESULT

```
11:‏چرین را گویند ۴ که بدان کلیدابرا بگشایند‎
17:کلیدانه
23:‏کلیدان ‎A‏ - بفتح اولبروزن‌حریفان»
30:آخرکلیدان است که قفل وغلق درخانه باشد.
46:‏۴ رك : رشیدی .کردی ‎killj‏ (کلید) روسی ۷106 ‎(os)‏ « ژابا ص۳4۱*.
63:. ‏کلیدانه‎ A
64:‏تو کلیدانی است هموار‎ oles
69:‏4 کلیددان « ‎LIME Sa‏ چاپ اروپا ج ‎TYTN‏ ۱۵»:
71:‏زبان تو کلید ‎OT‏ نگهدار .
75:‏۶ = کلیدان .
84:‏کلید
88:‎Hohe ‏نامه‎ share « ». ‏بود‎ alls ‏کلید‎
```


## [2026-09-06T21:01:02.155Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==480' incoming/BQT/BQT_v3_pages.txt | sed -n '58,110p'"
}
```


### [2026-09-06T21:01:03.865Z] TOOL RESULT

```
‏پس در قدیم کلیچه ‎pines‏ مطلق کرد نان بوده « فرهنگ نظام > .

‎eV ‏رك :کلیچه » ورك : ح‎ ٩
‏من ترا پیرهندم و زیباست‎ - ۷
. ‏کلیدانه‎ A
‏تو کلیدانی است هموار‎ oles

‏کهن من . کلیچه ‎Bathe‏ من,
سوزنی سمرقندی « رشیدی *.

‏4 کلیددان « ‎LIME Sa‏ چاپ اروپا ج ‎TYTN‏ ۱۵»:

‏زبان تو کلید ‎OT‏ نگهدار .

‏پهلوان محمود فتالی بنقل ایجمنآرا در « اسکندان».

‏۶ = کلیدان .

‎Acie) (kleidos ‏و‎ ( klefss gu yj! ( ‏مرکزی‎ ings ( ‏پکسر اول‎ - aye o

‏کردی ع ‎kilid‏ (ففل) . م14 « ژابا س ۳4۱ ۰ ‎Tope‏ « اقلید » و
«اکلیل > و «مقلاد» « تفی » ؛ ابزاری که بدان قفل راکشابند وبندند :

‎Qe

‏کلید

‎2 ‏اتفاق کردند که این حادثه را ج زکفایت سندیاد‎ ol, ‏حکما‎ ke Us?

‎Hohe ‏نامه‎ share « ». ‏بود‎ alls ‏کلید‎
```


## [2026-09-06T21:01:16.426Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD klid ===\"; grep -n \"klīd\\|klyt\\|kilid\\|klid\" PHD.txt PHD_mackenzie.txt | head -10\necho \"=== HRN kilid ===\"; grep -n -i \"kilid\\|kilTd\\|klid\" HRN.txt | head -10\necho \"=== HUB kilid ===\"; grep -n -i \"kilid\\|klid\" HUB.txt | head -10\necho \"=== KLN clause/claudere ===\"; grep -n \"clavis\\b\" KLN_1966.txt | head -5\necho \"=== SKT close ===\"; grep -n \"^close\\|clause\" SKT.txt | head -10"
}
```


### [2026-09-06T21:01:16.525Z] TOOL RESULT

```
=== PHD klid ===
PHD_mackenzie.txt:3296:kilel [klyl I N kilid)] key.
=== HRN kilid ===
7430:ist wie ein Schlüssel (lies kilid statt kältd) für den
=== HUB kilid ===
=== KLN clause/claudere ===
4032:Derivatives:  autochthon-al,  autochthon-ic,  au¬ tochthonous,  adjs.,  autochthon-ism,  n. autoclave,  n.,  a  container  used  for  sterilizing  and cooking,  —  F.,  lit.  ‘self-locking’,  a  hybrid  coined fr.  Gk.  auxii;, ‘self’, and  L.  clavis,  ‘key’.  See  auto- and  clavicle.
7385:chiastolite,  n.,  a  variety  of  andalusite  (mineral.) —  Compounded  of  Gk.  yla.a'coc,  (see  prec. word)  and  Xt&o;,  ‘stone’.  See  -life,  litho-. chiaus,  n.,  a  Turkish  messenger.  —  Turk,  chd- wush,  chaush.  See  chouse, chiave,  n.,  clef  (music).  —  It.,  ‘key’,  fr.  L.  clavem, acc.  of  clavis,  ‘key’,  whence  also  F.  clef,  ‘key’. See  clavicle  and  cp.  clef,  conclave, chibouk,  chibouque,  n.,  a  Turkish  tobacco pipe.  —  F.  chibouque,  fr.  Turk,  chubuq,  chibuq, ‘pipe’,  prop,  meaning  ‘stick,  staff,  tube’,  and rel.  to  chub,  ‘stick,  staff’, chibrit,  n.,  elemental  mercury  supposed  to  pro¬ duce  metals  (alchemy).  —  Arab,  chibrtt,  ‘sulfur’, rel.  to  Heb.  gophrith,  Jewish-Aram.  guphrithd, kubhrithd,  Christ.-Palest.  Aram,  guphri,  Syr. kebhrithd,  Akkad,  kupritu,  ‘brimstone,  sulfur’, chic,  n.,  style,  elegance.  —  F.,  prob.  fr.  G.  Schick, ‘fitness,  tact,  skill’,  fr.  MHG.  schicken,  ‘to  ar¬ range,  set  in  order’,  whence  G.  schicken,  ‘to send',  Geschick,  ‘fitness,  aptness,  fate,  destiny’, Schicksal,  Schickung,  ‘fate,  destiny’. Derivatives:  chic,  adj.  and  tr.  v.
7861:ML.  clavicymbalum.  See  clavicembalo. Derivative:  clavecin-ist,  n. clavelization,  n.,  inoculation  with  sheep  pox virus  (med.)  —  F.  clavelisation ,  fr.  clavelee, ‘sheep  pox’,  fr.  Late  L.  cldvellus,  ‘sheep  pox’, dimin.  of  L.  clavus,  ‘nail’,  which  is  rel.  to  clavis, ‘key’;  see  clavicle  and  -ization.  The  disease  is so  called  because  the  pustules  caused  by  it  re¬ semble  nailheads.
7862:clavicembalo,  n.,  a  harpsichord.  —  It.,  lit.  ‘cymbal with  a  keyboard’,  compounded  of  L.  clavis, ‘key’,  and  cymbalum,  ‘cymbal’.  See  clavicle  and cymbal.
7863:Claviceps,  n.,  a  genus  of  sac  fungi  (bot.)  —  ModL., compounded  of  L.  clava,  ‘club’,  and  -ceps, ‘-headed",  fr.  L.  caput,  ‘head’.  See  clava  and capital,  adj.  For  the  change  of  Latin  a  (in  caput) to  e  (in  -ceps)  see  biceps. clavichord,  n.,  an  early  keyboard  instrument.  — ML.  davichordium,  compounded  of  L.  clavis, ‘key’,  and  chorda,  ‘string’.  See  clavicle  and  chord, clavicle,  n.,  the  collarbone.  —  F.  clavicule,  fr.  Late L.  cldvicula,  ‘a  little  key,  bar,  bolt,  tendril’,  dimin. of  L.  clavis,  ‘key’,  which  is  rel.  to  clavus,  ‘nail’, claudere,  ‘to  shut’.  In  its  anatomical  sense  Late L.  cldvicula  was  first  used  by  the  translators of  Avicenna  about  the  year  980.  See  close,  adj., and  cp.  chiave,  clavelization,  clavier,  clavis,  clef, autoclave,  conclave,  enclave,  kevel,  laticlave, subclavian.  Cp.  also  lot.
=== SKT close ===
3525:close  (n,  to  shut  iQ.  (K-L.)  M.  £. doutt.-^O.y.  das,  pp.  of  OF-  dort^  to shut  io.  — L.  dauruj.  pp.  of  daudirt  (as above).     Der.  tiu-dast,  ert'doie.  in-dase.
3526:close  (3).  shut  up.  (F.-L.)  M.  £. dot.  f/aw.  —  O,  F.  dot  (as  abore).
3733:Colon  (i).  a  mark   (:)   in  writing  ud printing.    (Gk.)      Gk.  jruXof,   a    daoKj hence  a  stop  marking  on*  a  clause- Colon  (2),  part  o?  the  intestines.  (GLj Glc  KoiKov,  the  same.
3813:Com,m^a.  (L.  —  Gk.)  L.  rvmma.  —  Gk, «4)>i/ia,  that  which  is  struck,  a  stamp,  a clause  of  a  sentence,  a  comma  (that  marks the  clause). —  Gk.  «^«T«i*',  to  bew.  stnke. CVSKAP.)
22989:cithern  — guitar, clause  —dose,  xS,
```


## [2026-09-06T21:01:25.261Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD key ===\"; grep -n \"] key\\|key\\.\" PHD.txt | head -10\necho \"=== KLN lot ===\"; grep -n \"^lot,  n\\.\\|lot,  n\\.\" KLN_1966.txt | head -5\necho \"=== KLN close adj ===\"; grep -n \"close,  adj\" KLN_1966.txt | head -5"
}
```


### [2026-09-06T21:01:25.356Z] TOOL RESULT

```
=== PHD key ===
69:In seeking an unknown word, or one known only in another transcription, it may be necessary first to find it in the Pahlavi key. The English-Pahlavi index is intended to serve as an aid to memory, and for tracing synonyms, etc., but is emphatically not an English-Pahlavi dictionary.
419:kābēn [%”fyx! | N kabin] marriage-portion, dowry (assigned to the bride). kabig [Rpy&! | N kab/pi] monkey.
428:kem [kym] less, fewer; v. kam. кёп [kyn' | = M, N kīn(a)] hate, malice, revenge. ~ig [-yR'] malicious, vengeful. kennār [Rl] lyre, harp. ~-sray [-sPd] harpist. kénwar [kynwl | (M kynw’r), N kinawar] vengeful, vindictive. ««īh: vindictiveness. kër [kyl | N ~] penis. kēsar [kysl] Caesar. këš [kyš | = M, N ~] dogma, faith (especially non-Mazdean). ~-dar [-d’/] sectary, non-Mazdean. keSidan, keš- [k(y)$-ytn! | (M kr$-), N kafidan] pull, draw. Kēwān [kyw’n! | Ar. kaywān] astr. Saturn. kēwūd [kypwt! | M R'ywd] box, ark. kilēl [R]yl | N ktlīd)] key. kirb [klp | M kyrb] body, form. kirbag [krpk' | M kyrbg, N Аја] virtue, good deed. ~ig [-y%!] virtuous, pious. kirbakkar [krpkkl | M kyrbkr] beneficent. ~ih: beneficence. kirih- [OBYDWNyh-, v. kardan, kiyh- | M kyryh-] be done, made. kirm [kim | M krm, N —] worm, serpent. kirrénidan, kirrén- [klyn-ytn'] rend; create (daevic). kirróg [k(y)lwk! | M grwg] artisan, craftsman; skilled. ~th: arts, crafts, craftsmanship, skill. kiš [k(y)š | M АЎ, N ~] furrow, line. kišnīz [kšnyc] = gi$niz. kištan, kar- [ZL Y TWN-tn! < А У ar; kyštn!, Pl- | M kyšt, kis- N ~] till, furrow; sow. kištār [ZLY TW NTt'l] tillage. kišw, ~4n [kysw', x! | P Аун] tillage. ~(an)zar [-c?/ | (N kištzār)] field. ki$war [Rystol | M kyswr, N ~] region, clime, continent. kišwzār, v. kišwānzār. kūb-, v. koftan. kódak [kxwtk! | M gwdk, N ~] young, small; baby. kof [kwp | = M, N koh] hill, mountain; hump. ~ag [-4! | N Абла] saddle. ~ig [-yk! | N kēkī] wild, mountain-. koftan, kūb- [kwp-tn' | N ~] beat, pound, crush. kör [kwl | M kar, N ~] blind. ~-dil [-dyl | M -dyl, N ~] blind-hearted, incorrigible. kūstan [kwstn' | = M, N ~] beat, pound. kūš-, v. kóx&-. kēšk [how fA! | N ~] pavilion, palace, kiosk.
=== KLN lot ===
2758:fr.  Xa-pela,  ‘hired  labor,  worship’.  See  -latry. angelot,  n.,  1)  a  gold  coin ;  2)  a  sort  of  cheese  made
4333:Derivatives:  balloon,  tr.  and  intr.  v.,  and  the hybrid  noun  balloon-ist,  n. ballot,  n.  —  F.  ballotte,  fr.  It.  ballotta,  ‘little  ball’, dimin.  of  balla,  ‘ball’  (see  E.  ball,  ‘a  round body’);  so  called  in  allusion  to  the  small  balls formerly  dropped  into  the  voting  um. Derivatives:  ballot,  intr.  and  tr.  v.,  ballot-age (q-v.)
5203:Derivatives:  blossom,  intr.  v.,  blossom-ed,  adj., blossom-ry,  n.,  blossom-y,  adj. blot,  n.,  a  spot.  —  ME.  blot,  blotte,  fr.  MF.  blotte, ‘a  clod  or  clot  of  earth’,  fr.  OF.  bloste  or  blostre, which  are  of  uncertain  origin, blot,  tr.  and  intr.  v.,  to  make  spots,  to  blur.  — MF.  blotter,  fr.  blotte.  See  prec.  word. Derivatives:  blott-er,  n.,  blott-ing,  adj.,  blott¬ ing-!  y,  adv.
5204:blot,  n. ,  1 )  in  backgammon,  an  exposed  man ;  2)  an exposed  point.  —  Prob.  rel.  to  Dan.  blot,  Swed. blott,  LG.  blutt,  MDu.,  Du.  Woo/,  MHG.  Woj, G.  blof,  ‘bare,  naked’,  OHG.  W03,  ‘proud’,  ON. blautr,  ‘soft,  tender’,  and  possibly  cogn.  with  Gk. tyXu&av,  ‘to  overflow’,  9Xu8ap6<;,  ‘soft,  flabby’, L.fluere,  ‘to  flow’.  See  fluent  and  cp.  words  there referred  to.
6035:cachalot,  n.,  the  sperm  whale.  —  F.,  fr.  Sp.  ca¬ chalot?,  fr.  Port,  cacholotte,  lit.  ‘thick-headed’, fr.  cachola,  ‘head,  pate’,  which  is  perh.  a  dimin. of  cacha,  ‘handle  of  a  razor’,  fr.  VL.  capula, pi.  of  capulum,  corresponding  to  L.  capulus, ‘handle,  hilt  of  a  sword’,  fr.  capere,  ‘to  catch, seize’.  See  captive.
=== KLN close adj ===
7856:claudicate,  intr.  v.,  to  limp.  —  L.  claudicat-(um), pp.  stem  of  claudicare,  ‘to  limp,  halt,  be  lame’, fr.  claudus,  ‘lame,"  which  is  of  uncertain  origin. It  was  influenced  in  form  by  a  popular  con¬ nection  of  this  word  with  claudere,  ‘to  shut,  en¬ close'  (see  close,  adj.).
7857:Claudius,  Claude,  masc.  PN.  —  L.  Claudius, name  of  two  Roman  gentes,  rel.  to  claudus, "lame".  See  prec.  word  and  cp.  Claudia, clausal,  adj.,  pertaining  to  a  clause.  —  Formed fr.  next  word  with  adj.  suff.  -al. clause,  n.  —  ME.,  fr.  OF.  (=  F.)  clause,  fr.  ML. clausa,  used  in  the  sense  of  L.  clausula,  ‘the close  of  a  rhetorical  period",  fr.  L.  clausus,  pp. of  claudere,  ‘to  shut,  enclose’.  See  close,  adj., and  cp.  words  there  referred  to.
7859:claustral,  adj.,  pertaining  to  a  cloister.  —  ML. claustrdlis,  fr.  L.  claustrum,  ‘bolt,  bar’,  in  its ML.  sense  "cloister".  L.  claustrum  stands  for *claud-trom  and  literally  means  ‘that  by  which anything  is  shut  up",  and  is  formed  fr.  claudere, ‘to  shut",  with  instrumental  suff.  *-trom.  See close,  adj.,  and  cp.  cloister.  For  the  suff.  see rostrum.  Cp.  also  next  word  and  the  first  ele¬ ment  in  claustrophobia.
7863:Claviceps,  n.,  a  genus  of  sac  fungi  (bot.)  —  ModL., compounded  of  L.  clava,  ‘club’,  and  -ceps, ‘-headed",  fr.  L.  caput,  ‘head’.  See  clava  and capital,  adj.  For  the  change  of  Latin  a  (in  caput) to  e  (in  -ceps)  see  biceps. clavichord,  n.,  an  early  keyboard  instrument.  — ML.  davichordium,  compounded  of  L.  clavis, ‘key’,  and  chorda,  ‘string’.  See  clavicle  and  chord, clavicle,  n.,  the  collarbone.  —  F.  clavicule,  fr.  Late L.  cldvicula,  ‘a  little  key,  bar,  bolt,  tendril’,  dimin. of  L.  clavis,  ‘key’,  which  is  rel.  to  clavus,  ‘nail’, claudere,  ‘to  shut’.  In  its  anatomical  sense  Late L.  cldvicula  was  first  used  by  the  translators of  Avicenna  about  the  year  980.  See  close,  adj., and  cp.  chiave,  clavelization,  clavier,  clavis,  clef, autoclave,  conclave,  enclave,  kevel,  laticlave, subclavian.  Cp.  also  lot.
7882:with  L.  clavis,  ‘key’,  clavtts,  ‘nail’,  claudere,  ‘to shut’.  See  close,  adj.,  and  cp.  cleisto-,  cleithral and  the  first  element  in  cleoid.  Cp.  also  clathrate.
```


## [2026-09-06T21:01:31.845Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"cogn\\.  with  Gk\\.  xXe\" KLN_1966.txt | head -3\necho \"---\"; sed -n '7880,7884p' KLN_1966.txt\necho \"=== close adj full ===\"; grep -n \"close,  adj\\.,  shut\" KLN_1966.txt | head; grep -n \"^close\" KLN_1966.txt | head\necho \"=== search 'lot,  n.,  1)' ===\"; grep -n \"lot,  n\\.,  a  portion\\|lot,  n\\.,  1\" KLN_1966.txt | head"
}
```


### [2026-09-06T21:01:31.953Z] TOOL RESULT

```
---
cleido-,  before  a  vowel  cleid-,  combining  form meaning  ‘key’  or  ‘clavicle’. — Gk.  xXei8o-,xXei.S-, fr.  xXet?  (for  *xXv)u;,  fr.  *xXafu;,  cp.  Ion.  xXrjfi;, Dor.  xXit?,  Old  Att.  xX/jq),  ‘bar,  bolt,  key’, whence  xXcleiv  (for  ‘xXiFieiv),  ‘to  shut,  close, bar’,  xXeWpov,  ‘bar  for  closing  a  door’;  cogn.
298
with  L.  clavis,  ‘key’,  clavtts,  ‘nail’,  claudere,  ‘to shut’.  See  close,  adj.,  and  cp.  cleisto-,  cleithral and  the  first  element  in  cleoid.  Cp.  also  clathrate.
cleisto-,  before  a  vowel  deist-,  combining  form meaning  ‘closed’,  as  in  cleistogamy.  — -  Gk. xXeiciTo?,  ‘shut’,  verbal  adj.  of  xXsteiv.  See cleido-.
cleistogamy,  n.,  self  fertilization  of  certain  closed flowers  ( bot .)  —  Compounded  of  cleisto-  and Gk.  -yapda,  fr.  y afio?,  ‘marriage’.  See  -gamy. Derivatives:  cleistogam-ic,  adj.,  cleistogam-ic: al-ly,  adv.
=== close adj full ===
7963:close,  adj.  —  ME.  clos,  fr.  OF.  (=  F.)  clos,  fr. L.  clausus,  pp.  of  claudere,  ‘to  shut,  close’, which  is  rel.  to  clavis,  ‘key’,  clavus,  ‘nail’,  cldva, ‘a  knotty  stick,  staff,  club’,  and  cogn.  with  Gk. xXetp,  gen.  y.XsiSop,  ‘bar,  bolt,  key'  [whence xXctsiv  (for  ‘xXeFieiv),  ‘to  shut,  close,  bar’, xXel&pov,  ‘bar  for  closing  a  door’],  OIr.  c/d,  ‘nail’, OSlav.  kljuci,  ‘key’,  Russ,  kljuc,  of  s.m.,  OSlav. kljuciti,  ‘to  shut  up',  Serb,  kljuka,  ‘hook’,  Lith. kliuti ,  ‘to  catch,  be  caught  on’,  kliauties,  Lett. Mauties,  ‘to  rely  upon’,  OFris.  s/itta,  MLG., MDu.  sluten,  Du.  sluiten,  OHG.  sliu^an,  MHG. slie^en,  G.  schliefien ,  ‘to  shut,  close,  lock’,  OS. slutil,  OFris.  sletd,  MDu.  slbtel,  Du.  sleutel, OHG.  i/«3Jt/,  MHG.  slit33el,  G.  Schlussel, ‘key’.  All  these  words  derive  fr.  I.-E.  base  *qlau-, *(s)qleu-,  ‘hook,  forked  branch,  key;  to  close, shut’.  Cp.  autoclave,  chiave,  clathrate,  claustral, clava,  clavate,  clavelization,  clavicle,  clavier, claviform,  clavis,  cleido-,  cleisto-,  cleithral,  cle- oid,  cloison,  cloister,  closet,  closure,  clove,  ‘spice’, clove,  ‘a  former  weight’,  cloy,  conclave,  con¬ clude,  conclusion,  disclose,  eclosion,  enclave,  en¬ close,  exclude,  exclusion,  foreclose,  glaive,  in¬ clude,  inclusion,  occlude,  occlusion,  parclose, preclude,  preclusion,  recluse,  seclude,  seclusion, sloat,  slot,  ‘bolt’,  subclavian.  Cp.  also  lot. Derivatives;  clos-ed,  adj.,  close-lv,  adv.,  close¬ ness,  n.
7964:close,  n.,  enclosure,  space.  —  OF.  (=  F.)  clos,  en¬ closure’,  pp.  used  as  a  noun.  See  next  word. close.tr.  and  intr.  v.  —  ME.  closen,  fr.  OF.  (=  F.) clos,  pp.  of  clore,  ‘to  shut’,  fr.  L.  claudere.  See close,  adj.
7965:close,  n.,  completion.  —  Fr.  prec.  word, closet,  n.  —  OF.,  dimin.  of  clos,  ‘enclosure’.  See close,  ‘enclosure’,  and  -et.
13406:close,  compact’,  verbal  adj.  ofvtxacrstv,  ‘to  press close’,  which  is  of  uncertain  origin.
=== search 'lot,  n.,  1)' ===
2758:fr.  Xa-pela,  ‘hired  labor,  worship’.  See  -latry. angelot,  n.,  1)  a  gold  coin ;  2)  a  sort  of  cheese  made
```


## [2026-09-06T21:01:36.822Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"OE\\.  hlot\\|hlot,\\|hleotan\" KLN_1966.txt | head -5\necho \"=== lottery ===\"; grep -n \"lottery\" KLN_1966.txt | head -5"
}
```


### [2026-09-06T21:01:36.889Z] TOOL RESULT

```
22176:lot,  n.  —  ME.  lotte,  fr.  OE.  blot,  rel.  to  ON.  hlutr, ‘lot,  share’,  OHG,  hlu3,  lu3,  ‘share  of  land’,  OS. hlot,  ON.  hlaut,  Swed.  loti,  Dan.  lod ,  OHG. hid 3,  I03,  MHG.  I03,  G.  Los,  Goth,  hlauts,  of s.m.,  OE.  hleotan,  OS.  hliotan,  ON.  hljota, OHG.  hlio33an,  lio3an,  MHG.  Iie3en,  ‘to  cast lots,  to  foretell’,  fr.  Teut.  base  *hlut-,  which  pos¬ sibly  meant  orig.  ‘to  hook  to’,  and  corresponds to  I.-E.  base  *(s)qleu-,  *qldu-,  ‘a  hook,  forked branch,  key;  to  close,  shut;  to  catch,  be  caught on’.  See  close,  adj.,  and  cp.  words  there  referred to.  F.  lot,  ‘lot,  portion,  share’,  It.  lotto,  ‘lot, portion,  share’,  lotteria,  ‘lottery’,  are  Teut.  loan words.  Cp.  lottery,  lotto,  allot.
=== lottery ===
17156:handgrip,  n.  —  ME.,  fr.  OE.  handgripe,  ‘a  grasp of  the  hand’.  See  hand  and  grip, handicap,  n,  —  For  hand  in  cap,  orig.  a  kind  of lottery  game,  in  which  the  forfeit  money  was held  in  the  hand  in  a  cap.
20603:Prob.  fr.  F.  quine,  ‘five  winning  numbers  in  a lottery’,  fr.  L.  quini,  ‘five  each’,  which  is  rel.  to quinque,  ‘five’  (see  quinque);  so  called  because in  this  game  numbered  balls  are  arranged  in rows  of  five;  the  player  who  first  has  a  row  of five  covered  wins.
22176:lot,  n.  —  ME.  lotte,  fr.  OE.  blot,  rel.  to  ON.  hlutr, ‘lot,  share’,  OHG,  hlu3,  lu3,  ‘share  of  land’,  OS. hlot,  ON.  hlaut,  Swed.  loti,  Dan.  lod ,  OHG. hid 3,  I03,  MHG.  I03,  G.  Los,  Goth,  hlauts,  of s.m.,  OE.  hleotan,  OS.  hliotan,  ON.  hljota, OHG.  hlio33an,  lio3an,  MHG.  Iie3en,  ‘to  cast lots,  to  foretell’,  fr.  Teut.  base  *hlut-,  which  pos¬ sibly  meant  orig.  ‘to  hook  to’,  and  corresponds to  I.-E.  base  *(s)qleu-,  *qldu-,  ‘a  hook,  forked branch,  key;  to  close,  shut;  to  catch,  be  caught on’.  See  close,  adj.,  and  cp.  words  there  referred to.  F.  lot,  ‘lot,  portion,  share’,  It.  lotto,  ‘lot, portion,  share’,  lotteria,  ‘lottery’,  are  Teut.  loan words.  Cp.  lottery,  lotto,  allot.
22183:Lotophagi,  n.  pi.,  a  people  mentioned  in  Homer’s Odyssey,  IX;  they  were  supposed  to  live  in  a state  of  indolence  caused  by  their  subsisting  on the  fruits  of  the  lotus.  —  L.,  fr.  Gk.  Awrocpivoi, lit.  ‘lotus  eaters’,  fr.  Xcoroq,  ‘lotus’,  and  the  stem of  9ayciv,  ‘to  eat’.  See  lotus  and  -phagous. lottery,  n.  —  It.  lotteria,  ‘public  lottery’,  fr.  lotto, ‘lot,  portion,  share'  (but  F.  loterie  derives  fr.  Du. loterije,  fr.  Du.  lot,  ‘lot’).  See  lot  and  cp.  lotto. Lottie,  Lotta,  fem.  PN.  —  Dimin.  of  Charlotte, lotto,  n.,  a  game  of  change.  —  It.,  lit.  ‘a  lot’.  See lot  and  cp.  lottery.
31557:Derivatives:  radul-ar,  radul-ate,  adjs. raff,  n.,  rabble.  —  ME.  raf,  fr.  OF.  raffe,  fr. raffer,  ‘to  sweep  together’.  See  raffle,  ‘lottery’, and  cp.  riffraff.
```


## [2026-09-06T21:01:45.880Z] TOOL CALL #38: Bash

```json
{
 "command": "sed -n '1,60p' tools/fetch_source.py"
}
```


### [2026-09-06T21:01:45.913Z] TOOL RESULT

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
    fetch_url = urllib.parse.urlunsplit((parts.scheme, parts.netloc.encode("idna").decode(),
                                         urllib.parse.quote(parts.path, safe="/%:@!$&'()*+,;="),
                                         urllib.parse.quote(parts.query, safe="=&%:/?+"), parts.fragment))
    os.makedirs(WEB, exist_ok=True)
    path = os.path.join(WEB, h + ".txt")
    if os.path.exists(path) and time.time() - os.path.getmtime(path) < 86400:
        print(path); return 0
    status, title, text = 0, "", ""
    try:
        req = urllib.request.Request(fetch_url, headers={"User-Agent": UA, "Accept-Language": "en"})
        with urllib.request.urlopen(req, timeout=60) as r:
            status = r.status
            raw = r.read(4_000_000)
            ctype = r.headers.get("Content-Type", "")
            enc = "utf-8"
            m = re.search(r"charset=([\w-]+)", ctype)
            if m: enc = m.group(1)
            body = raw.decode(enc, errors="replace")
            if "html" in ctype or body.lstrip().lower().startswith("<!doctype html") or "<html" in body[:2000].lower():
                mt = re.search(r"(?is)<title>(.*?)</title>", body)
```


## [2026-09-06T21:01:53.434Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor U in \"https://en.wiktionary.org/wiki/%DA%A9%D9%84%DB%8C%D8%AF\" \"https://en.wiktionary.org/wiki/%D8%A5%D9%82%D9%84%D9%8A%D8%AF\" \"https://en.wiktionary.org/wiki/%CE%BA%CE%BB%CE%B5%CE%AF%CF%82\" \"https://www.etymonline.com/word/lot\" \"https://www.etymonline.com/word/close\" \"https://en.wiktionary.org/wiki/%D8%B3%D8%B1%D8%B4%D8%AA%D9%86\" \"https://en.wiktionary.org/wiki/%D8%B3%D8%B1%DB%8C%D8%B4\" \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%E1%B8%B1leh%E2%82%82u-\"; do\n echo \"### $U\"; python3 tools/fetch_source.py \"$U\" --note \"page 271, roots Kleu/Klis: kelid/eqlid/serist chains\" 2>&1 | tail -2\ndone"
}
```


### [2026-09-06T21:01:59.190Z] TOOL RESULT

```
### https://en.wiktionary.org/wiki/%DA%A9%D9%84%DB%8C%D8%AF
/home/sfmqrb/git/rishe/data/verification/sources/web/32bcb7353841251d.txt
### https://en.wiktionary.org/wiki/%D8%A5%D9%82%D9%84%D9%8A%D8%AF
/home/sfmqrb/git/rishe/data/verification/sources/web/256b11cef04e3a26.txt
### https://en.wiktionary.org/wiki/%CE%BA%CE%BB%CE%B5%CE%AF%CF%82
/home/sfmqrb/git/rishe/data/verification/sources/web/214827e973fc93f0.txt
### https://www.etymonline.com/word/lot
/home/sfmqrb/git/rishe/data/verification/sources/web/f95f3899d9b643ab.txt
### https://www.etymonline.com/word/close
/home/sfmqrb/git/rishe/data/verification/sources/web/12c99759fad28e21.txt
### https://en.wiktionary.org/wiki/%D8%B3%D8%B1%D8%B4%D8%AA%D9%86
/home/sfmqrb/git/rishe/data/verification/sources/web/d60ecf08a9e575c6.txt
### https://en.wiktionary.org/wiki/%D8%B3%D8%B1%DB%8C%D8%B4
/home/sfmqrb/git/rishe/data/verification/sources/web/32ea9853f3d18115.txt
### https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%E1%B8%B1leh%E2%82%82u-
/home/sfmqrb/git/rishe/data/verification/sources/web/030a36383b81a399.txt
```


## [2026-09-06T21:02:02.173Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nfor f in 32bcb7353841251d 256b11cef04e3a26 32ea9853f3d18115 d60ecf08a9e575c6; do echo \"##### $f\"; grep -n -A25 \"Etymology\" $f.txt | head -60; echo; done"
}
```


### [2026-09-06T21:02:04.035Z] TOOL RESULT

```
##### 32bcb7353841251d
65: Etymology 
66-
67- 1.3 
68- Noun 
69-
70- 1.3.1 
71- Descendants 
72-
73- 1.4 
74- Further reading 
75-
76- 2 
77- Persian 
78-
79- Toggle Persian subsection 
80-
81- 2.1 
82- Alternative forms 
83-
84- 2.2 
85: Etymology 
86-
87- 2.3 
88- Pronunciation 
89-
90- 2.4 
91- Noun 
92-
93- 2.4.1 
94- Derived terms 
95-
96- 2.4.2 
97- Descendants 
98-
99- 2.5 
100- References 
101-
102- Toggle the table of contents 
103-
104- کلید 
105-
106- 16 languages 
107-
108- فارسی 
109- Français 
110- Magyar 
--
185: Etymology
186- [ edit ] 
187-
188- Borrowed from Classical Persian کِلِید ( kilīd ) .
189-
190- Noun
191- [ edit ] 
192-
193- کلید • ( klyd / kilīd /) 
194-
195- key 
196- Synonyms: قفل ( qfl /⁠qüfl⁠/ ) , مفتاح ( mftʾḥ /⁠miftāh⁠/ ) 
197- 1484 , Ali-Shir Nava'i , فرهاد و شیرین [ Farhad and Shirin ], page 250b : اچیب اول کنج قفلین بو کلیدیم 

##### 256b11cef04e3a26
62: Etymology 
63-
64- 1.2 
65- Noun 
66-
67- 1.2.1 
68- Declension 
69-
70- 1.2.2 
71- Derived terms 
72-
73- 1.3 
74- References 
75-
76- Toggle the table of contents 
77-
78- إقليد 
79-
80- 2 languages 
81-
82- Magyar 
83- Malagasy 
84-
85- Entry 
86-
87- Discussion 
--
140: Etymology
141- [ edit ] 
142-
143- From Aramaic אַקְלִידָא / ܐܩܠܝܕܐ ( ʾaqlīdā , “ key ” ) from Ancient Greek κλεῖδα ( kleîda ) , accusative singular of κλείς ( kleís , “ key ” ) , from Proto-Indo-European *kleh₂us ( “ nail, pin, hook – instruments of old use for locking doors ” ) , from the root *(s)kleh₂w- .
144-
145- Noun
146- [ edit ] 
147-
148- إِقْلِيد • ( ʔiqlīd )  m ( plural أَقَالِيد ( ʔaqālīd ) ) ( Ḥaḍramawt ) 
149-
150- key 
151- 7th century CE , Ṣaḥīḥ al-Buḵāriyy , 64:86 : فَدَخَلْتُ فَكَمَنْتُ، فَلَمَّا دَخَلَ النَّاسُ أَغْلَقَ الْبَابَ، ثُمَّ عَلَّقَ الأَغَالِيقَ عَلَى وَتَدٍ قَالَ فَقُمْتُ إِلَى الأَقَالِيدِ ، فَأَخَذْتُهَا فَفَتَحْتُ الْبَابَ. fadaḵaltu fakamantu, falammā daḵala n-nāsu ʔaḡlaqa l-bāba, ṯumma ʕallaqa l-ʔaḡālīqa ʕalā watadin qāla faqumtu ʔilā al-ʔaqālīdi , faʔaḵaḏtuhā fafataḥtu l-bāba. So I went in (the castle) and hid myself. When the people got inside, the gate-keeper closed the gate and hung the keys on a fixed wooden peg. I got up and took the keys and opened the gate. 
152-
153- Declension
154- [ edit ] 
155-
156- Declension of noun إِقْلِيد ( ʔiqlīd )
157-
158- singular
159-
160- basic singular triptote 
161-
162- indefinite
163-
164- definite
165-

##### 32ea9853f3d18115

##### d60ecf08a9e575c6
```


## [2026-09-06T21:02:11.040Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"=== kelid persian section ===\"; sed -n '200,300p' 32bcb7353841251d.txt\necho \"=== sirish size ===\"; wc -c 32ea9853f3d18115.txt d60ecf08a9e575c6.txt; head -30 32ea9853f3d18115.txt"
}
```


### [2026-09-06T21:02:11.095Z] TOOL RESULT

```
=== kelid persian section ===
näsībim äylä ne kim bar ümīdim / (please add an English translation of this quotation) 

 Descendants
 [ edit ] 

 Uyghur: كىلىت ( kilit ) 

 Uzbek: kalit 

 Further reading
 [ edit ] 

 Bahawudun, Muhemmettursun; Gheyurani, Ghenizat; Qadir, Isma'il; Ehet, Ablimit ( 2002 ), چاغاتاي تىلىنىڭ ئىزاھلىق لۇغىتى [ Explanatory Dictionary of the Chagatai Language ]‎ [1] (in Uyghur), Shinjang Xelq Neshriyati, →ISBN 

 Ünlü, Suat ( 2013 ), Çağatay Türkçesi Sözlüğü [ Dictionary of Chagatai Turkic ] (in Turkish), Konya: Eğitim Yayınevi, →ISBN , page 633 

 Persian
 [ edit ] 

 Persian Wikipedia has an article on: کلید 

 Wikipedia fa 

 Alternative forms
 [ edit ] 

 کیلیت ( kilit ) ( dialectal , Tehrani ) 

 کلیل ( kelil ) ( dialectal , Dezfuli ) 

 کلی ( kilī ) ( dialectal , Kabuli ) 

 Etymology
 [ edit ] 

 Inherited from Middle Persian *kilēd , from Ancient Greek κλείς, κλειδός ( kleís, kleidós ) .

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /ka.ˈliːd/ , /ki.ˈliːd/ 

 ( Dari, formal ) IPA ( key ) : [kʰä.liːd̪] , [kʰɪ.liːd̪] 

 ( Dari, formal ) IPA ( key ) : [kʰä.liːd̪] , [kʰɪ.liːd̪] 
 ( Kabuli ) IPA ( key ) : [kʰɪ.liː] 

 ( Hazaragi ) IPA ( key ) : [kʰi.li] 

 ( Iran, formal ) IPA ( key ) : [kʰʲæ.liːd̪̥] , [kʰʲe.liːd̪̥] 

 ( Iran, formal ) IPA ( key ) : [kʰʲæ.liːd̪̥] , [kʰʲe.liːd̪̥] 
 ( Tehrani ) IPA ( key ) : [kʰʲiː.liːt̪ʰ] 

 ( Tajik, formal ) IPA ( key ) : [kʰä.lid̪] 

 Rhymes: -iːd 

 Readings

 Classical reading ? 

 kalīd, kilīd

 Dari reading ? 

 kalīd, kilīd

 Iranian reading ? 

 kalid, kelid

 Tajik reading ? 

 kalid

 Audio ( Iran ) : ( file ) 

 Noun
 [ edit ] 

 Dari

 کلید 

 Iranian Persian

 Tajik

 калид 

 کلید • ( kalīd, kilīd / kalid, kelid ) ( plural کلیدها ( kalīd-hā, kilīd-hā / kalid-hâ, kelid-hâ ) , Tajik spelling калид ) 

 key 

 ( music ) clef 
 کِلیدِ سُل ― kelid -e sol ― treble clef 
 کِلیدِ فا ― kelid -e fâ ― bass clef 

 Derived terms
 [ edit ] 
=== sirish size ===
4764 32ea9853f3d18115.txt
2989 d60ecf08a9e575c6.txt
7753 total
URL: https://en.wiktionary.org/wiki/%D8%B3%D8%B1%DB%8C%D8%B4
FETCHED: 2026-09-06T21:01:58Z
STATUS: 200
TITLE: سریش - Wiktionary, the free dictionary

سریش - Wiktionary, the free dictionary 

 Jump to content 

 Main menu 

 Main menu

 move to sidebar 
 hide 

 Navigation

 Main page 
 Community portal 
 Requested entries 
 Recent changes 
 Random entry 
 Help 
 Glossary 
 Contact us 
 Special pages 

 Search
```


## [2026-09-06T21:02:21.736Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor U in \"https://en.wiktionary.org/wiki/%D8%B3%D8%B1%DB%8C%D8%B4%D9%85\" \"https://en.wiktionary.org/wiki/%D8%B3%D8%B1%D8%B4%D8%AA\" \"https://en.wiktionary.org/wiki/%E0%A4%B6%E0%A5%8D%E0%A4%B2%E0%A4%BF%E0%A4%B7%E0%A5%8D\" \"https://en.wiktionary.org/wiki/%D9%85%D9%82%D9%84%D8%A7%D8%AF\"; do\n echo \"### $U\"; python3 tools/fetch_source.py \"$U\" --note \"page 271 entry 1: serisht/sirishm/Skt slis; miqlad\" 2>&1 | tail -1\ndone\necho \"=== PIE kleh2u ===\"; grep -n -A20 \"^ Etymology\" data/verification/sources/web/030a36383b81a399.txt | head -40"
}
```


### [2026-09-06T21:02:26.685Z] TOOL RESULT

```
### https://en.wiktionary.org/wiki/%D8%B3%D8%B1%DB%8C%D8%B4%D9%85
/home/sfmqrb/git/rishe/data/verification/sources/web/814bc2fdc27e2b40.txt
### https://en.wiktionary.org/wiki/%D8%B3%D8%B1%D8%B4%D8%AA
/home/sfmqrb/git/rishe/data/verification/sources/web/1c3a6a8119cbef72.txt
### https://en.wiktionary.org/wiki/%E0%A4%B6%E0%A5%8D%E0%A4%B2%E0%A4%BF%E0%A4%B7%E0%A5%8D
/home/sfmqrb/git/rishe/data/verification/sources/web/cfab7c32e8d4c4fd.txt
### https://en.wiktionary.org/wiki/%D9%85%D9%82%D9%84%D8%A7%D8%AF
/home/sfmqrb/git/rishe/data/verification/sources/web/80ddaf85030de03b.txt
=== PIE kleh2u ===
```


## [2026-09-06T21:02:30.215Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nfor f in 814bc2fdc27e2b40 1c3a6a8119cbef72 cfab7c32e8d4c4fd 80ddaf85030de03b 030a36383b81a399; do echo \"##### $f  ($(wc -c <$f.txt) bytes)\"; sed -n '1,6p' $f.txt; grep -n -i \"borrowed\\|inherited\\|From Proto\\|from Middle Persian\\|from Sanskrit\\|Proto-Indo-Iranian\" $f.txt | head -10; echo; done"
}
```


### [2026-09-06T21:02:32.463Z] TOOL RESULT

```
##### 814bc2fdc27e2b40  (156 bytes)
URL: https://en.wiktionary.org/wiki/%D8%B3%D8%B1%DB%8C%D8%B4%D9%85
FETCHED: 2026-09-06T21:02:24Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found
##### 1c3a6a8119cbef72  (4979 bytes)
URL: https://en.wiktionary.org/wiki/%D8%B3%D8%B1%D8%B4%D8%AA
FETCHED: 2026-09-06T21:02:25Z
STATUS: 200
TITLE: سرشت - Wiktionary, the free dictionary

سرشت - Wiktionary, the free dictionary 
237: Borrowed from Classical Persian سرشت ( sirišt ) .
272: Urdu terms borrowed from Classical Persian 

##### cfab7c32e8d4c4fd  (6073 bytes)
URL: https://en.wiktionary.org/wiki/%E0%A4%B6%E0%A5%8D%E0%A4%B2%E0%A4%BF%E0%A4%B7%E0%A5%8D
FETCHED: 2026-09-06T21:02:26Z
STATUS: 200
TITLE: श्लिष् - Wiktionary, the free dictionary

श्लिष् - Wiktionary, the free dictionary 
194: From Proto-Indo-Iranian *ćRayš ( “ to adhere, attach ” ) ; cognate with Persian سِریشُم ( serišom , “ glue ” ) . Further origin is uncertain; perhaps related to Proto-Indo-European *ḱley- ( “ to lean, incline ” ) .
243: Categories : Sanskrit terms inherited from Proto-Indo-Iranian 
244: Sanskrit terms derived from Proto-Indo-Iranian 
245: Sanskrit terms inherited from Proto-Indo-European 
246: Sanskrit terms derived from Proto-Indo-European 

##### 80ddaf85030de03b  (5677 bytes)
URL: https://en.wiktionary.org/wiki/%D9%85%D9%82%D9%84%D8%A7%D8%AF
FETCHED: 2026-09-06T21:02:26Z
STATUS: 200
TITLE: مقلاد - Wiktionary, the free dictionary

مقلاد - Wiktionary, the free dictionary 

##### 030a36383b81a399  (184 bytes)
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%E1%B8%B1leh%E2%82%82u-
FETCHED: 2026-09-06T21:01:59Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found
```


## [2026-09-06T21:02:46.238Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\ngrep -n -B2 -A8 \"Proto-Indo-European\" 214827e973fc93f0.txt | head -40\necho \"=== maqlad ar ===\"; grep -n -B3 -A8 \"Etymology\" 80ddaf85030de03b.txt | sed -n '1,60p' | grep -v \"^[0-9]*- *$\" | head -40"
}
```


### [2026-09-06T21:02:47.834Z] TOOL RESULT

```
181- [ edit ] 
182-
183: From Proto-Hellenic *klāwī́ds , from Proto-Indo-European *kleh₂u- ( “ nail; pin; hook ” , instruments, of old use for locking doors ) . Cognate with Latin clāvus ( “ nail; pin ” ) , Old Church Slavonic ключь ( ključĭ , “ key ” ) . [ 1 ] 
184-
185- Pronunciation
186- [ edit ] 
187-
188- IPA ( key ) : /klěːs/ → /ˈklis/ → /ˈklis/ 
189-
190- ( 5 th BCE Attic ) IPA ( key ) : /klěːs/ 
191-
--
482- Categories : Ancient Greek terms inherited from Proto-Hellenic 
483- Ancient Greek terms derived from Proto-Hellenic 
484: Ancient Greek terms derived from Proto-Indo-European 
485- Ancient Greek 1-syllable words 
486- Ancient Greek terms with IPA pronunciation 
487- Ancient Greek lemmas 
488- Ancient Greek nouns 
489- Ancient Greek oxytone terms 
490- Ancient Greek feminine nouns 
491- Ancient Greek third-declension nouns 
492- Ancient Greek feminine nouns in the third declension 
=== maqlad ar ===
59- Toggle Arabic subsection 
61- 1.1 
62: Etymology 
64- 1.2 
65- Noun 
67- 1.2.1 
68- Declension 
70- Toggle the table of contents 
--
133- Arabic
134- [ edit ] 
136: Etymology
137- [ edit ] 
139- Tool noun derivative of إِقْلِيد ( ʔiqlīd , “ key ” ) .
141- Noun
142- [ edit ] 
144- مِقْلَاد • ( miqlād )  m ( plural مَقَالِيد ( maqālīd ) )
```


## [2026-09-06T21:03:08.018Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AFM اقلید ===\"; grep -n \"اقليد\\|إقليد\\|مقلاد\\|كليد\" AFM_pages.txt | head -10\necho \"=== ARB ===\"; grep -n \"اقليد\\|إقليد\\|مقلاد\" ARB_mo3rb.txt ARB_abdulraheem.txt | head -10\necho \"=== TAD ===\"; grep -n \"اقليد\\|إقليد\\|مقلاد\" TAD_pages.txt | head -10\necho \"=== AFA Fraenkel ===\"; grep -n -i \"iqlid\\|aqlid\\|Schlüssel\" AFA.txt | head -10"
}
```


### [2026-09-06T21:03:08.103Z] TOOL RESULT

```
=== AFM اقلید ===
=== ARB ===
ARB_mo3rb.txt:22211:؟ د” المقُليدُ “ : المفتاح ٠‏ فارسى معرب ٠‏ لغة فى ” الإقليد » وابامسع 
ARB_mo3rb.txt:22238:([ له مقاليد السموات والأرض # « وهى عربية خااصة » وكذلك ”” الإقليد “ ٠‏ وادسى ابن دريدآن 
ARB_mo3rb.txt:22241:الأفاليد ”5 إقليد “" » ٠‏ ومادة ” ليد “ عرربية » والاشتقاق مئها وام بين ٠‏ 
=== TAD ===
2213:            ‫رولها؟‪ 1‬معناه متاح‬      ‫إقليد واكليل ومعلاد و ناني‪5‬‬
=== AFA Fraenkel ===
1122:dass auch die Namen der Schlösser und Schlüssel vielfach
1157:u. s. w. wohl alle aus 4XjJL5l »Schlüssel*' erst denominativ
1229:Ein bestimmter Verschluss, ohne Schlüssel zu offnen,
10203:erklärt; »Ein iT/rpsT;;, in dessen Hand Schlüssel und Sie-
```


## [2026-09-06T21:03:16.995Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AFA 1145-1175 ===\"; sed -n '1145,1175p' AFA.txt\necho \"=== TAD context ===\"; sed -n '2205,2220p' TAD_pages.txt"
}
```


### [2026-09-06T21:03:17.045Z] TOOL RESULT

```
=== AFA 1145-1175 ===
M herausgebildet hat und dass diese dann in das Arabi-
sche übergegangen ist. Bei einem fremden Werkzeugnamen
ist eine solche Analogiebildung sehr begreiflich und vnx
begegnen ihr auch sonst noch. So sind z. B. zwei gleich gut
überlieferte Namen des Hammers i^HätlS und NHäTnO.
[Daneben besteht eine echt arabische Wurzel jJU »drehen**
(dann » umgeben** cX I aj sich umgürten), davon 'ic!^ und o^
= svr. Ir— s Die technische Bedeutuuij, die dies Wort für
den rr*^ hatte, beweist schon seine Echtheit, und die Be-
deutuugsilhnlichkeit darf nicht verleiten, etwa die ganze,
dem Hebräischen fehlende Wurzel für entlehnt zu halten]. ')
Dagegen sind die Bedeutungen von jJLi »anvertrauen**
u. s. w. wohl alle aus 4XjJL5l »Schlüssel*' erst denominativ
abgeleitet.
Den n'*?pX werden Sanhedrin 110«, 14 a. f. ^^3lp (so
lies nach ^Aruch; unsere Agg. haben ^S/p) gegenüber-
gestellt. Auch dies Wort ist, zunächst gewiss aus dem
Aramäischen, (auch syr. jl^cj- ZDMG. XXVII. 623,
O 9
4 a. f.) ins Arabische als Jlä» (vgl. Hai zu Kelim 11,4 als
Erklärung von S"ll2D1*7p = jcAäDö-tpov »arab. ^Slp") über-
gegangen; davon werden denominativ J^, J^ajI u. s. w.
gebildet Die Wurzel kommt auch in einer echt arabischen
Bedeutung vor, JLa» »trocken sein,** vgl. 73p (jüd. aram.)
»zusammenlegen** (von der Pflanze, die sich faltet und
zusammenlegt , wenn sie trocken wird); daher ist wohl auch
1) 6«iix Ton dieser Wanel zn trennen and nor mit ithiop. Zalada
XU combinieren scheint «AÜ .Wasser sammeln" und (Alä^ (rom Meere) »ver-
lenken;" «AÜ •Regen'" »ein Wasseri^etass'* athiop. makiaä.17
JlaS »umwenden" (verto) abzuleiten, so auch }' ,n X '): wie
weit dagej^en ]\ ^ ^ Job 11, 6. wirklich mit Recht von
=== TAD context ===
  ‫ميةدوع اللاتينية معناها عليةوخْرّانة مخنشب أما االقلفصيوفنانية‬
                                                               ‫هونان‬
                                                                   ‫الي‬
                                          ‫فبلفظ «ماءموه‪ 2‬وافلىلانينى وعحدء‬

                                      ‫ترى « قفتان » وهوالقاء‬    ‫قفطان ‪-‬‬


            ‫رولها؟‪ 1‬معناه متاح‬      ‫إقليد واكليل ومعلاد و ناني‪5‬‬

                                        ‫‪ - 3‬في اللاثينية ‪ 518‬معناه حياس‬

                                                  ‫اتلس انحظتركليس‬
 ‫قلقاس ‪ .-‬ووناني ‪ 5019850‬معناه مستدير ويطلق عندثم على اللفتعلى انه‬
                                                                    ‫مستدبر‬
```


## [2026-09-06T21:03:29.547Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT sris variants ===\"; grep -n -i \"sris\\|srié\\|sri§\\|sriš\" BRT.txt | head -20\necho \"=== ARY کلید ===\"; grep -n \"کلید\" incoming/ARY/ARY_pages.txt | head -10\necho \"=== ARY سریش/سرشت ===\"; grep -n \"سریش\\|سرشت\" incoming/ARY/ARY_pages.txt | head -10"
}
```


### [2026-09-06T21:03:29.625Z] TOOL RESULT

```
=== BRT sris variants ===
4790:der  Richtung:  atcit  dim  aiwyäili'^^  ya dahma . .  ofritis  P.J2.  a)  'begehen,  (einen Weg)  gehen':  mä  dim  psrisS ..yim  xrvan- tim..pantqm  aiwitim^*'''  "frag  den  nicht, .  .  der  den  grausigen  .  .  Weg  gegangen ist"  H.2.17.        S.  noch  No.  26.
10335:•  j,  gä^iwya-  Adj.  ',fiiäisch,  in  den Cjäjs  enthalten':  Aakra  ana  °ya  vaca "mit  diesem  ^5>ischen  Wort"  Y.  70. 19, Ö5. 14,  Ny.  4.  8'*;  —  *imqm  'yqm  (APm.) vac9  srävayis  "diese  ^aSrischen  Worte  her- sagend" H.2.  20.
11645:got.  qens.  —  Vgl.  janay-,  —  Pü. :  srisülak  ösän cnikih  }eh  {i.  janay-  a)  dranjenit.  —  >)  So  Dach pa.     Ganz  unRichcc.
12462:—  pas/a  para.iris/Tm  {täxa\.yaeida^ryeAe) 'va  .  .  iae^^m  ava%a  fratsrisinti  ya%a maesi  .  .  vthrkai  haüa  V.  /(j.  ^^ ;  —  va&n yji  -va  .  .  ova.mwamaAi  kisüotHa  pivasca (sd.)  V./Ä  55;  —  'va  ml .  .  aohm  (sd. hqmpmsmte  V. /p.  3;  —  ya'A  zT  hvan ndit  uzuxsydti  d',a  'va  vTspä  *m?nnHnta Yt  6, 3;  8.  44;  —  aat  Ae  pattyänm  (sd.) avaJ>ar>nti  'va  'vanqm  yasnäica  vahmaica V.  16. 11;  —  vlspanam  *zT  *ava.sras^ntam ..  'va  *ra^ai/e  (sd.)    V.68;  y.ig.2&(?);
13393:•  j.  'dänav-  Adj.,  bezeichnet  einen  den  Ira- niern  feindlichen  i'Srischen  Volksstamm: tala  yöi  taxma  xstüvayS  'nubyS  az)n  p?sana yüz»tn  (näml.  /ravasayj)  tdm  taurvayata v>r?^r?m  'nunqtn  türanqm..t6al^3  'nunam türanqm  .  .  xrBma  asSbis  frasinta  (sd.) "nunqm  baivari.pailinqm  Yt-/J.  37f.;  — yat  baväma  aiwi.vanya  °nav3  (als  AP.) tära  vyäxana  Yt.  J.  73.
14668:•  j.  SrisaSTwant-  Adj.  'dreissigfach':  'wä (nämL  asti  mürS)  antan  vamSna  Yt 10. 116.
14708:•  j.  ^SriS-hastra-'*  n.  'Versammlung  von dreien':  yä  bii.hastrim  sravayeiä  . .  *rsm
16991:K  zu  sehr  in  die  Länge  ziehend"  Yt.  10. 138; —  binstm  baräi  saota  väam  hii'tpmnd pasca  'ma  YLJ7.  61;  —  yö  'ma  *aivah- mat  naimat  hamsrisäiti  hqm  va  dansa- yeili  N.  pp;  —  yat  patri  °ma  hanjasante N.  6"2;  —  tim  yazäi . .  haomayff  {sdi.)  gava 'mana  Ny.  /.  16;  —  aao'ira^  .  .  'ma'  äytse yesti  sao^ra  haoaJar^sma  .  .  'ma  hala.- saehra  äyese  yesti  akmya  sadhre  imai  '""^ .  .  ana  'mana  imqm  zaoirqm  .  .  ha%a.- zao^rfm  imai  '«"^  Syae  ydti  Y.  2.  i;  —
18672:3  airySma  (sd.)  .  .  jantü  mnbyasiä HäiribyascS  zara%uslrakl  Y.54.  i;  FrW. i.\;  —  narasca  *tiairTsla  Vyt.30;  — rtaram  näirinamca  V,  2.  27,  30;  8.  12,13, Vd.3,  Y.(?Än*;  —  in  Verbindung  mit alavan-  (s.  auch  Sp.  1050  o.):  aiaunqm .  .  urunS  .  .  kiidö.taianqmltt  narqmcä näirinqmlä  Y.J9.2;  J7-3,  -i'.?,  8,  10, Yz.iS.  2,Yt./j,  143-145^  A)näirika-. nar 3m  vä  *nSirikqm  vä  FrB.;  Az.  I,  Vyt. /,  Vd.  7j,  Nik-i-j^;  —  hala  nä  (statt Abi.)  paiti.irisi5  haca  näirika  paitiSriste V,  iO.  s ;  —  in  Verbindung  mit  aSavan- (s.  auch  Sp.  1050  o.):  nanm  asavamm .  .  näiriiqm  asaonim  V.p,33,  42,  ig.  12, 26,  71.1,  3,  7,  10  (statt  Abi.);  Vr.^.  4, G.4.9.  a)  jahikä-:  narS  (tiS.)''>  pai- ristä.xsu%rS  . .  Jahika  paraJax^ta  Yt  J7. 54.  f)  vantav-:  yaisa  nä  fryS  fryäi vantaoe{sA.)  ..  pu%r»m  ..  avi  avii.baraili ^- 3-  *S-  g)  pu'^ra-.  nanm  vä  .. puhnm  vä  FrB.;  Az.  /,  Vyt  7,  Nik. I.  h),  i)  aptnnäyBka-,  kainikä-:  na- ramHa  .  .  apmnäyükanamca  kainika- nqm!a  Y.  68.12;  26.  8 f.'  2)  sonst: nar/^  k?hrpa  panca.dasanlüs  YtÄi3, i4~^T,  Vdiy;  —  niUmactt  ..  stärqm {sA)  ya%a  nars  matmyehe  v(r/han>m    F.
26247:J575  üb- mit  ä  —  ssriSta-  'ST^
28946:bei  Verben  der  Bewegung":  tfar»  pas^a paraSristtm  .  .  us  h'  6a^S  (sd.)  ayaj  V. 7.  3 ;  —  US  A°  nasavS  attavai  apat  ha'a (s.  Sp.  1747  u)  rdibaraym  (Sp.  939  0.) V.  6'.  31;  —  US  hala  (s,  Sp.  1747  u.)  aHbyS nmana^bys  baraym  .  .  atnmca  .  .  us  h' iristim    baraym    V.  5. 40.  II)    Praen.;
=== ARY کلید ===
=== ARY سریش/سرشت ===
1673:دو واجسریشه‌ی هسند و اروپایی 02008* ,۶026130 را به صورت دو قلم مجزا
2004:ا-ایسن واجریشه‌ق فسندواروپشایی بمتا وأجسسریشه‌های د رطع (418: ۳060137۷) ز ]۹۳
```


## [2026-09-06T21:03:39.588Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"1589\\|hamsris\\|hqm.sris\\|sris-\" BRT.txt | head -20\necho \"---- context 26240-26255 ----\"; sed -n '26240,26256p' BRT.txt"
}
```


### [2026-09-06T21:03:39.651Z] TOOL RESULT

```
16991:K  zu  sehr  in  die  Länge  ziehend"  Yt.  10. 138; —  binstm  baräi  saota  väam  hii'tpmnd pasca  'ma  YLJ7.  61;  —  yö  'ma  *aivah- mat  naimat  hamsrisäiti  hqm  va  dansa- yeili  N.  pp;  —  yat  patri  °ma  hanjasante N.  6"2;  —  tim  yazäi . .  haomayff  {sdi.)  gava 'mana  Ny.  /.  16;  —  aao'ira^  .  .  'ma'  äytse yesti  sao^ra  haoaJar^sma  .  .  'ma  hala.- saehra  äyese  yesti  akmya  sadhre  imai  '""^ .  .  ana  'mana  imqm  zaoirqm  .  .  ha%a.- zao^rfm  imai  '«"^  Syae  ydti  Y.  2.  i;  —
26498:1589  staotar-
---- context 26240-26255 ----
•  j.,  g.  säsni-  f.  'Lehre;  Gebof:  vakilta 'nanqm  yqm  hudä  sästl  asä  akurS  ". .  ist die  beste  der  Lehren  die,  die  der  wohl- meinende Ah.  durch  Asa  lehrt"  Y.-^.a; —  tim  äzOtöi/isd.)  ahurS  mq%r3m  talal . . spunta  'naya  (IS.)  Y,  29.  7 ;  —  sraffta  'nä fiSnghyS  (sd.)  Y.  4g.  9;  —  yS  nS  alvB  'nä güsatä  zara^u^trB  spitämö  "der  einzige, der  unsre  Lehren  vernommen  hat,  ZarSp." V.2g.S;  —  mä  as  at  vS  drtgvaß  (Sp. 776  o.)  mq%rqscä  gBsta  •näscä  "keiner von  euch  höre  auf  des  ./ungläubigen Worte  und  Gebote"  Y.jj.  18";  —  gayehe man^nS  . .  yS  paoiryS  akurSi  . .  manasla *guita  'näsca  Yt.rj.87*';  —  *maihyDi.mäa- hahe  . .  yS  paoiryS  zarahustrSi  mq'hrtmca *gusla  'näsca  Yt.  JJ.  95'';  —  gusta  'na F.,?f.;  —  sat>m  'nanqm  Vyt /J.
KompA.  —  Zum  V.  läk-.  —  aL  vgL  Säsana' n.  —  Pü.:  ämöriin,  ämSxliht. —  1)  Die  lelztea Worte  der  Stelle  hat  der  Verfasser  von  Yt. '3-  87,  95  bennwt  —  ">  S.  No.  I.
•  j.  säsnö.güä-"  Adj.  'der  die  (heiligen) Lehren  hört,  vernimmt';  paoiryanqm  tkaf- lanqm  paoiryanqm  'güsqm ''  "der  ersten Verkünder  und  Hörer  der  heiligen  Lehren" Y.aö'.  4,  Yt.jj.149J'.
*gis-  Adj.,  zum  V.  gaoi-.  —  Pü. :  nigöHht  i ämöähtin,  erl. :  fratum  /lävill  i  aatalull,  — 1)  Vgl.  No.  3.  —  »)  Vgl.  Y.  19.  8,  Yt.  rj 87.  9S-  —  J'  Wo  Fl   'gülqm  bietet
•  j.,  g.  sah- V.  'hcissen'.  Praes.  1  sah-, 3  sJia-,  2z  sähT:  —  PPfP.  sJäa-'\ s:ista-.
'heissen,  lehren',  mit  dopp.  Akk.:  data xratsul . .  razSng  voAb  säAli  mananAa "(es)  lehre  (mich)  der  Schöpfer  der  Geistes- kraft durch  VM.  (seine)  Satzungen"  Y. $0. 6;  —  y^  nä  )mBs  savatshs  pdhs  slisit "der  uns  die  rechten  Wege  des  Vorteils lehren  könnte"  Y.4J.3;  —  süa  nä  aia
dby  Google
J575  üb- mit  ä  —  ssriSta-  'ST^
faiS..:^aiai^(iA.)  \.34.ii;  —  vafdäJ  \.^i.\^-,32.ft;  —  diidi  mäi . . awLmOii läsnanqm  fsd.^  jqm  . .  ilttl  aii  a^rS  hainsti  ipfniää  maiitrü  wuttdJ  briHrntj' Y.4A. 3.  yüiti  manaoAä  r-t-Aä  •mihi  "scfafnk  mir..
mit  a  Verheisseii,  in  Aassicht  stellen':  Uasterblicbkdt  und  Wohlfahrt  durch  den at  tH  atrim  . .  *ajjil)m'> ..  stzi  rapafäi  beüigsten  Gast,  o  J/i,  Kiaft  mid  Bestand ctirä-ovaahjm  (iA.)  ¥,^4.4.  durch  YM.    bei    dem    Richtereprach"    V,
mit /rJ  i/rS)  'lehren,  ofiienbaren',  mit  5J-7-  4»  'Reden,  Spreeben  lüber  Je- dopp.  Akk.:  ahyä  xraiü  JrS  mi  s3stü  mandes)':  ^J  nar^m  aSaraiam  ain^.z^ifs- vahistä  "durch  seine  Weisheit  lehre  a  mich  «Jt  .  .  kavfanhs  Isd.)  'ahäi  da-iäiti ,  V. das  Beste"  Y.  45, 6; — '/rtuasta-.       a)mit   /J- a*'-  5f    Tled^    Woti":    *ambm9wf
Akl(.  dcrPers-undlDC:  ti>m  mazdä  oAurä  •^)Bi  •r»Ä>m  T.^t;  3t,  12.  S.  noch /rff  mä  liiä  "iwahmät  vaocaAhl  *mainjr^  bei  n&ifjtjatpha-.
haca  Ja-J  i)at»hä  "du,  o  MAk^  lehre  mich      KompE.  —  Zun  V.  nk-.  —  aL  icV«-  m.  —
aas    deinem    Geist   durch    deinen    Mond      K^: -"■"'^-;*- ("L^- ■**  »6  =  ™^=™*,  ,«
1  -     j      71  >r      i>  ■-  4°-  3  """1  ■"  *■  ■  "^*";  *-  noch  No-  at
verkuDden"  H.'JS.ii.  :     _  .,  s  »■ />b«^a».*a..  —  .,  Vi.-,  ki i i li
mit  ^in  'zurechtweisen':  •Hamaästa-,    '     niiur  ämSchui,  oL:  o^  bKHät;  s.  No.  3.—
```


## [2026-09-06T21:03:53.609Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"kleben\\|anhaften\\|zusammenfügen\" BRT.txt | head -20\necho \"=== running heads 158x-159x ===\"; grep -n \"^15[78][0-9] \\|  15[78][0-9]  \" BRT.txt | head -20"
}
```


### [2026-09-06T21:03:53.674Z] TOOL RESULT

```
15851:'an  nnander  befestigen,  zusammenfügen': s.  sartmyapax^pad:
20952:aurvanta  *yux/a*i  vai'a  %imjasiaU  Yt j  to.  1 36.  2)  'zusammenfügen;  verbünden'; ia)  absolut:  upa  tair^m  Aarayä  yuxtayi
25577:werde  ich  . .  wieder  zusammenfügen  die
=== running heads 158x-159x ===
26402:1585  »süra-
26498:1589  staotar-
28980:Sp.  928  o.)  ist  weggelassen:  danys.Hli (sd.)  ile  vTse  afrJnämi  yahmat  h°  imti zaoira  y.SS.i^;  \t.  S.  4'.  '  b)  bei NomiDa";  o)  bei  verbalen  Substantiven: raiis  i&i.;  'decessum')  rm  A^  ariha  ztmat vaähs  k^nnaoili  Vt.  17.  20;  —  spmtat  h" mainyaot  aisam  ahr^m  ('origo')  FrW. 70,40;  —  yä  h"  daSnayUt  .  ,  apastüilis ('abdicatio'j  ^.4J-  ß)  bei  Raumwörtera: dsräl  Cprocul')  A'  ahmiil  nmänät  .  .  ays i^yejä . .*yeyenH yeAhe ..  Y.57,  14;  14';  — nSii . .  *dräjyS  ('longius')  *'iyeillm  framraomi (sd.)  . .  ä/rllim  yUnat  -4'  .  .  P.  7j;  — nazdyS  ('propius')  ahmi  . .  yaia  änha  k' *gaosaHöya  P.  2  V;  28;  —  airime  gätüm hs nUhthaüta  . .  *psr3ntanm  (sd.;  'seorsum') h'  anyanbyS  mazdayasna^byS  V.g.  33;  29; —  aiai  dräjö  ('quantam  longitudinem')  h* i!^ral\.  3. 16;  16^;  — yS  hn%rS.masar»h3m iS/wamm  ('viam  miUe  passuum')  h'  vizibys paräiti  V.  JJ.  18;  —  äiat  ('quantum*)  h' mtiya^bya  Y.i).  10;  8f.';  —  avavat  ('tan- tum')  h'  paourt-aiibya  yäha  %rigilim  V. 1M39;  II,  76;  — yd  *yujyastxm  (sd.)  h' gat^abyS  parätti  'v.  7^.  17;  N.  8,  <??(?), V,_j.  17*,  J(5'.4*,  17. 4«,  b)  im  gÄw. a)  bei  Verben  (bei  solchen  der  Bewegung nicht  bezeugt):  frg  ma  sl/iJ  (Sp.  1575  o.) "iiwahmut  *vaoca^hl  *mainy}us  h'  'üwä Siaiihn  "..  pronuntiare  ex  tuo  , tuum  os"  Y.  28. 11;  —  ysi  gSus  h'  iyävtl (sd.)  "qui  a  bove  (habitant  sva.)  stant' Y.  J7.  a";  —  ka^ü  . .  zarjm  (sd.)  laränl h'  xsmap''  ",  .  impetrem  a  vobis  (sva. per  vos)"  Y.  44-17;  —  a^byS  mazdh  .  . xsäi^rät  A'  paifi.mraot  ". .  per  Regnum (deum)  respondit"  Y.ya.  2;  —  sonst mit  'asa-  A  (als  Gottheit)  im  Sinn  von 'peri^nim,  As'o  juvante  (u.  dgl.)':  aiät  h'
29472:naisim  vamavätaiy  duruxlam  (Sp.  767  m.)  mainySui  dSmqn  yat  ir/(APn.)  , .  anaä-ä- *maniyitaiy  Bh.  4. 8;  —  äh^ind' ..  *a>ia-  maide  Vt.  12. 4.  «)  Der  Begriff  auf  den ya/ä  abiy  mim  adamsim  avajaimm  Bh.  j  sich  h'  zurUckbezieht,  ist  zuvor  nicht  ge- /.  17;  ^-gaumäiam  .  .  kärJ' Hm . . atarsd'inxaoX,  aber  aus  der  Sachlage  eikenntlicb: EL  /.  13;  —  aniyaf'  apiyä  *äkyata  api- ,  mt^rfm  . .  yd  dai^hSus  rqxsyqihyi  para litn^''  paräbari^  Bh.  i.  19;  —  rtäV-  rausta  baraili  .  .  avar»%i  hls  (APm., taxmam  agariayi^ .  ■  duvarayätnaiy  basti/'  1  näml.  regionis  incolas)  fl/iwKCtCSp.  140710.) adilriy  haruvt^sim  kär^  avaifia*  pasä-  Ytio.i-j;  —  »oÄT/*^»'Sa  . .  jfl/{Sp.  1581  u.) va''iiin  arbairäyä  uzmayapatiy  akutMvam  yaia    Alm  (ASn,   'es')*'   ädar?    mafyäka
```


## [2026-09-06T21:04:05.700Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== NYB sristan ===\"; grep -n \"sristan\\|srištan\\|srēš\\|sris-\" NYB_vol2_glossary.txt | head -10\necho \"=== SYN key ===\"; grep -n -i \"key.*clavis\\|clavis.*key\\|kleis\" SYN.txt | head -10\necho \"=== LAT claudo ===\"; grep -n \"claudo\" LAT.txt | head -5\necho \"=== SYN glue ===\"; grep -n -i \"glue\" SYN.txt | head -8"
}
```


### [2026-09-06T21:04:05.795Z] TOOL RESULT

```
=== NYB sristan ===
=== SYN key ===
11682:2. Lat. conclave, cpd. of clavis ‘key’ (7.24), hence a place that can be locked up. Otherwise only words for special rooms, as cubiculum mostly ‘bedroom’, fr. cubdre ‘recline’; triclinium ‘dining- room’, orig. the couch on three sides of the table, fr. Grk. rpixdinoy,
11774:W. clo : Lat. clavis ‘key’, etc. (7.24).
15080:2. Lat. clavus (whence, partly through VLat. *claus, It. chiodo, Fr. clou, Sp. clavo) : Ir. clé ‘nail’, Lat. clavis, Grk. kdels, ChSI. kljuct ‘key’, orig. ‘peg for
21654:1. Derivs. of IE *klau-, *klawi-, de- noting the (wooden) ‘peg’ or primitive ‘key’, as Grk. xdjs, Kdels, Lat. clavis, ChSl. kljucét ‘key’, Lat. clavus, Ir. clé ‘nail’, ete. (cf. ‘key’ 7.24). Walde-P.
34022:development of ‘hinder’ from ‘get caught’ on something and so ‘be in the way’ : Lat. claudere ‘shut’, claudére ‘limp’ and ultimately the group of words for ‘hook, peg; key’, Grk. xvels, Lat. clavis, ete. Walde-P. 1.492 ff. Muhl.-Endz. 2.241.
=== LAT claudo ===
9191:claudo, etc., se retrouve dans gr. xav8apo£* avGpai;, etc. Mais aillenrs
12308:clau-; clauis, clauus (clauos), claudo. 1° clauis,-is f. : cl^, lo-
12338:3° claudo,-is,-si,-sum,-ere (et cludo doublet tir£ des composes en
12378:d'ou serait sorti clduis. D'antre part, il y a claudo qui semble indi-
12382:y.sl.kljuci "cl< 5 " rappelle claudo, clduus, et gr.xAotFtc est malais^
=== SYN glue ===
9960:cking to’, clipa ‘plas- sglei-t-, extension of Lat. glis ‘glue’, OF etc. As a name ly referred orig. to
15606:ee; irt’ fr. also ‘fat, dirt’, etc.) ee . yala ‘glue’, OE cleg low, 4).
15622:OE cl@g, ME clai, NE clay, Du. klei : ChSl. glina, ete. (below, 6), Grk. yNia, yhiva, Lat. gliten ‘glue’, Ir. glenim, O#G klenan, klebén ‘stick, adhere’, etc. Walde-P. 1.619. Walde-H. 1.611 f.
17639:W. dilyn, canlyn, epds. of di- intensive or can (gan) ‘with’ and glynu ‘adhere, stick’ (: Ir. glenim id., Grk. yAta, Lat. gliten ‘glue’, etc.). Pedersen 2.539. Walde-P. 2.389, 1.619.
```


## [2026-09-06T21:04:14.804Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== WLD Bd1 klāu ===\"; grep -n \"klāu\\|klău\\|kläu\\|Haken, hakenförmig\" incoming/WLD/WLD_Bd1_pages.txt | head -10\necho \"=== find page 492 ===\"; awk 'BEGIN{RS=\"\\f\"} /492/ {print NR-1\": \"substr($0,1,80)}' incoming/WLD/WLD_Bd1_pages.txt | head -5"
}
```


### [2026-09-06T21:04:16.366Z] TOOL RESULT

```
=== WLD Bd1 klāu ===
=== find page 492 ===
34: 26                                               aues-


archangelica)" beide Pf
49:                      -                                ,
```


## [2026-09-06T21:04:20.528Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"Schlüssel\" incoming/WLD/WLD_Bd1_pages.txt | head -10\necho \"---\"; grep -n \"clāuis\\|clauis\\|clāvis\" incoming/WLD/WLD_Bd1_pages.txt | head -10\necho \"--- leaf offset probe ---\"; for L in 500 505 510; do echo -n \"leaf $L: \"; awk -v n=$((L+1)) 'BEGIN{RS=\"\\f\"} NR==n' incoming/WLD/WLD_Bd1_pages.txt | head -2 | tr '\\n' ' ' | head -c 90; echo; done"
}
```


### [2026-09-06T21:04:22.324Z] TOOL RESULT

```
---
--- leaf offset probe ---
leaf 500:                    g  
leaf 505:                                                            klep-                          
leaf 510:
```


## [2026-09-06T21:04:26.330Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor L in 504 505 506 507; do echo \"##### leaf $L\"; awk -v n=$((L+1)) 'BEGIN{RS=\"\\f\"} NR==n' incoming/WLD/WLD_Bd1_pages.txt | head -25; done 2>/dev/null | head -110"
}
```


### [2026-09-06T21:04:27.985Z] TOOL RESULT

```
##### leaf 504
496                    qleg-, qlog-, qlag-, qlang-; qleg-; ql5q-, qlsq-; qleig-; qleiq-



     lit.   sluoju, slaviaii, sluoti „fegen, wischen", Uuota „Besen“, lett. sluota ds.,
                                                      1
slaiicit          ,,fegen,wischen  slaukset „platschen, pladdern“, slaukt „melken“.
                                                          '',




     "Vgl.        Curtius 151, Fick I 4 48, 427 (unter Fernhaltung der bait. Sippe),
                               5

II 4 102, III 4 113, Vf.                        LEWb. 2 u. cluo, Trautmann Bsl. Wb. 307. — Ai. fra-,
cruvati „zerflieBen“ (Froehde BB. 8, 162)                                                        ist    eher ortbographische Yariante
von sru- „fliefien‘'.                        — Fernzuhalten                           ist   cech. kliditi „reinigen“, russ. kljudb
,,Ordnung“, cech. klouditi „sauber     machen“ (s. Berneker 527 m. Lit., der
sie  nun an russ.-ksl. kl'uditi ankniipft, woriiber u. qleu- „Haken“) und alb.
Jiul ,,Mehlbrei‘‘ (G. Meyer Alb. St. Ill 4; sei qlud-lo-; weder die Bed. noch
der Gutt.              fiigt       sich).

      Petersson LUA. 1916, 60 f. halt '*kleu- fur Erweiterung eines *kel- „feucht,
naB“, das auch folgenden Wzln. zugrunde liege                                                                 :       kb:})-   „feucht“    (s. d.),       klcq
##### leaf 505
                                                           klep-                                                     497

„lachen“,    Kaus. aisl. klpgia „zum Lachen bringen'-. got. ufhlohjan „auf-
lachen machen'-.
    Ags. Jiltgan „to give a reputation for (wisdom); attribute to“ hlisa, hligsa
„Bericht, Ruf, Ruhm“, mndl. lien be-hen , liken „sagen, melden“, ndl. belijden                                         ,


afries. hUa „melden, bekennen“(Fick III 4 112, Franck- van Wiik EWb. 2 47 f.),
lit. klinku M'tkti ,,plotzlich pfeifend aufkreischen“, klykiii, klf/kti „kreischen“,

Mykauti „quietschen“, abg. kliknqti „aufschreien“, klicati „schreien, rufen“,
Mill* „Geschrei“ (usw., Berneker 519, Trautmann Bsl. Wb. 136).
    Ahnliche Schallworte sind lat. glocio, -Ire „glucken“, mhd. klukken, ags.
cloecian ds. (nicht nach Zupitza Gutt. 163 zu lit. ehugauti „schluchzen“,
auch Falk-Torp u. klukke ), ksl. khcati ,,klopfen“, lit. klnksiti ,,glucken“
(u. dgl., Berneker 525 u. khcajq 1.2.), aisl. klaka „schwatzen“, engl. clack
„Rasseln, Klappern; Muhlglockchen", mhd. Klechcl, Kleckel „Glocken-
schwengelY Reimworte bietet die Schallwz. qer-. Vgl. Curtius 3 3, Fick I 3 70,
                 103, III 4 1 10, J. Schmidt Yoc. 497, Zupitza Gutt. 118 KZ. 36
               s
I 4 395 f., II

241, Vf. LEWb.
                             2
##### leaf 506
       ,    ;




498                                                    qlep-    — qleng-, qlenq-

qlep- „mit den           Armen und im SchoB zusammenhalten“?
     Mhd. lafter „Klafter“,                       lett.      kl'epis   „SchoB, SchoBvoll",                       lit.   klebys          „Arm-
weite, Klafter, Armvoll“ \b vielleicht naeh glebys „Armvoll“).                                                          Persson Beitr.
592 f. a 1, der wegen ai. kalapa-li „Bimd, Biindel“ eine zweisilbige Wz.
qolep-  „umfangen“ ansetzt, wenn letzteres nicht etwa doch nach PW. und
Siitterlin IF. 19, 567 f. aus kald „Teil“ und CLpa- zusammengesetzt ist, als
„was die Teile aufnimmt, zusammenhalt '; anders, aber verfehlt Charpentier  1




IF. 29, 394). Buga Kalba ir s. I 71, Miihlenbach-Endzelin II 224.
   Anlautvariante neben lit. glebys dt. Klafter ? (s. u. gel- ,,ballen“).
                                                                ,
                                                                          Ahd.                                                        —
halftra „Halfter“, lit. k'l lpa „Schlinge, Steigbiigel“ (Persson) s. u. sqel
,,spalten‘\

##### leaf 507
                                        kloibho-, kllbho-   — klou-nis                                         499

(eigentl. „biegsam".                Ob auch ags. Mine „ Abhang, Rain, Hiigel" (Tick III 4
11 Of.)?  Mit ausl. Tenuis abg. klec-q -afi „knien“, ksl. klekno -nqti „sich
                                                      ,                                           ,


knien", poMqcn-jq,  -ti „sich kriimmen; hinken", russ. kljafo „Knebel, Quer-

holz" („*Krummholz“) usw. (a. Berneker 514f., 524).
   Ygl. Johansson PBrB. 14, 298f. m. Lit. (s. auch zu glng- „Milch“). Aber
ai. cfwkhala „Kette, Fessel" (Fick I
                                       4
                                         395, Zupitza Gutt. 69 IvZ.- 36, 58)
s    u.   her- „drehen,        flechten".       Alte Beziehung zu            (
                                                                                 s)qel -   „biegen" iEhris-
mann PBrB. 20, 53) ist unsicher, dazu vgl. immerhin ( s)qreng'h)- neben (s)qer-
„drehen". Theoretisch moglich ist es daher, auch die Wz. sleng- „biegen“
(ahd. slingan usw.                 aus *sqlenq- erleichtert sein zu lassen.

kloibho-, kllbho- etwa „in Pfannen gebackenes Brot“.
     Got. hlaifs „Brot“, aisl. hleifr , ags. hlaf, ahd. hleib                ,
                                                                                  leib „Laib Brot, Brot“;
mhd. lebe-kuoche        ,
                             -zelte „Lebkuchen“: gr. yJJfiavog           -   att. y.otjiavog)         „Geschirr,
```


## [2026-09-06T21:04:33.483Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==501' incoming/WLD/WLD_Bd1_pages.txt | head -40"
}
```


### [2026-09-06T21:04:35.003Z] TOOL RESULT

```
                   g




492                                                      qleik-   — qleu-, qlau-

qleik- „(schmerzhaft) driicken, quetschen, klemmen, zwicken".
  Ai. kligndti „qualt, belastigt",   kliryatc ,,wird gequalt, leidet", Mega- m.
,,Schmerz, Leiden,     Beschwerde“, sq-klig- ,, quetschen": lit. Jcl'tse „Krebs-
schere" (davon wohl auch ITiias „schiefbeinig“,- mit schiefen, nach innen
gebogenen FiiBen", kleisiuoti „mit krummen FiiBen laufen“); ksl. klesta
„Zange", klesiiti „premere“ (usw., z. B. russ. klesnjd „Zange, Krebsschere"),
                                        1
abg. sb-klistati se ,,crueiari russ. dial. klestitb (= klestitb) „driicken, pressen,
                                            ',


klemmen" usw., eecli. s-klesnouti „zusammendrucken, -legen, (die Lippen,
Zahne) zusammenpressen, zusammenbeiBen“, russ. klescb (fur Mein) „Zecke,
Milbe, Holzbock" („sich festkneifend" usw.          S. Bezzenberger BB. 12, 78.
                                                                         i




Fick I 4 31, Berneker 5 6 f (gegen dessen Grundformen nicht zutreffend
                                    1
                                                 .




Bruckner KZ. 46, 211, Trautmann Bsl. Wb. 137.


qleu- (auch qleu- ?) und qlau-, vielleicht eigentlich „Haken, krummes Holz
    oder Astgabel, Pflockchen", verbal einerseits „anhaken (sich anklam-
    mern), bangenbleiben machen, (durch Anbinden an einen Pflock?) in
    der Bewegung beschranken, hemmen, auch von solch hinkendem
```


## [2026-09-06T21:04:40.669Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n '1,120p' tools/verify_check.py"
}
```


### [2026-09-06T21:04:40.707Z] TOOL RESULT

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


## [2026-09-06T21:04:55.063Z] TOOL CALL #56: Bash

```json
{
 "command": "pdftoppm -f 271 -l 271 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg271 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


### [2026-09-06T21:04:57.107Z] TOOL RESULT

```
total 18184
drwx------ 2 sfmqrb sfmqrb    4096 Sep  6 17:04 .
drwx------ 4 sfmqrb sfmqrb    4096 Sep  6 16:32 ..
-rw-rw-r-- 1 sfmqrb sfmqrb     264 Sep  6 16:57 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  456331 Sep  6 16:54 bqt1594_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2824 Sep  6 16:59 bqt83_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb   91526 Sep  6 16:59 bqt_v3_83.png
-rw-rw-r-- 1 sfmqrb sfmqrb   64531 Sep  6 16:53 build261.py
-rw-rw-r-- 1 sfmqrb sfmqrb   95615 Sep  6 16:39 coord_pg262.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4560 Sep  6 16:39 crop_ak2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4014 Sep  6 16:39 crop_ak.png
-rw-rw-r-- 1 sfmqrb sfmqrb   25373 Sep  6 16:42 crop_alk.png
-rw-rw-r-- 1 sfmqrb sfmqrb   24852 Sep  6 17:04 crop_fr269.png
-rw-rw-r-- 1 sfmqrb sfmqrb   43238 Sep  6 16:55 crop_germ269.png
-rw-rw-r-- 1 sfmqrb sfmqrb   51654 Sep  6 17:04 crop_gk269.png
-rw-rw-r-- 1 sfmqrb sfmqrb   64142 Sep  6 17:02 crop_gr267.png
-rw-rw-r-- 1 sfmqrb sfmqrb    6411 Sep  6 16:39 crop_gr.png
-rw-rw-r-- 1 sfmqrb sfmqrb   23559 Sep  6 16:42 crop_kohul.png
-rw-rw-r-- 1 sfmqrb sfmqrb   59386 Sep  6 16:39 crop_lat2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   51357 Sep  6 16:55 crop_latin269.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4761 Sep  6 16:39 crop_lat.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3974 Sep  6 16:37 crop_me2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3300 Sep  6 16:37 crop_me.png
-rw-rw-r-- 1 sfmqrb sfmqrb   10236 Sep  6 16:39 crop_op2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4935 Sep  6 16:37 crop_op.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5599 Sep  6 16:37 crop_pers.png
-rw-rw-r-- 1 sfmqrb sfmqrb   30419 Sep  6 17:02 crop_skt267.png
-rw-rw-r-- 1 sfmqrb sfmqrb   10043 Sep  6 16:58 crop_slav.png
-rw-rw-r-- 1 sfmqrb sfmqrb   24463 Sep  6 16:58 crop_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb 5301166 Sep  6 17:01 ediv.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb 1773345 Sep  6 17:01 ediv.txt
-rw-rw-r-- 1 sfmqrb sfmqrb     228 Sep  6 16:34 jscheck.js
-rw-rw-r-- 1 sfmqrb sfmqrb    1433 Sep  6 16:45 merge262.py
-rw-rw-r-- 1 sfmqrb sfmqrb   63035 Sep  6 16:56 mk265.py
-rw-rw-r-- 1 sfmqrb sfmqrb 8373934 Sep  6 17:00 mk.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb  378445 Sep  6 17:00 mk.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   11601 Sep  6 16:42 p262-g01.json
-rw-rw-r-- 1 sfmqrb sfmqrb   10625 Sep  6 16:43 p262-g02.json
-rw-rw-r-- 1 sfmqrb sfmqrb   19393 Sep  6 16:46 p262-g03.json
-rw-rw-r-- 1 sfmqrb sfmqrb   19959 Sep  6 16:44 p262-g04.json
-rw-rw-r-- 1 sfmqrb sfmqrb   12063 Sep  6 16:43 p262-g05.json
-rw-rw-r-- 1 sfmqrb sfmqrb   12051 Sep  6 16:44 p262-g06.json
-rw-rw-r-- 1 sfmqrb sfmqrb   12737 Sep  6 16:44 p262-g07.json
-rw-rw-r-- 1 sfmqrb sfmqrb   17259 Sep  6 16:46 p262-g08.json
-rw-rw-r-- 1 sfmqrb sfmqrb   17820 Sep  6 16:53 p262-g09.json
-rw-rw-r-- 1 sfmqrb sfmqrb   17855 Sep  6 16:45 p262-g10.json
-rw-rw-r-- 1 sfmqrb sfmqrb   14983 Sep  6 16:44 p262-g11.json
-rw-rw-r-- 1 sfmqrb sfmqrb   25352 Sep  6 16:46 p262-g12.json
-rw-rw-r-- 1 sfmqrb sfmqrb   17745 Sep  6 16:44 p262-g13.json
-rw-rw-r-- 1 sfmqrb sfmqrb  105748 Sep  6 16:39 p263hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   66777 Sep  6 16:42 pg261.png
-rw-rw-r-- 1 sfmqrb sfmqrb   84660 Sep  6 16:39 pg262.png
-rw-rw-r-- 1 sfmqrb sfmqrb   71156 Sep  6 16:38 pg263.png
-rw-rw-r-- 1 sfmqrb sfmqrb   92930 Sep  6 16:37 pg264hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   57862 Sep  6 16:35 pg264.png
-rw-rw-r-- 1 sfmqrb sfmqrb   13324 Sep  6 16:57 pg265_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb   86370 Sep  6 16:57 pg265.png
-rw-rw-r-- 1 sfmqrb sfmqrb   79922 Sep  6 16:42 pg266.png
-rw-rw-r-- 1 sfmqrb sfmqrb   70622 Sep  6 16:56 pg267.png
-rw-rw-r-- 1 sfmqrb sfmqrb   69592 Sep  6 16:52 pg268.png
-rw-rw-r-- 1 sfmqrb sfmqrb   71754 Sep  6 16:55 pg269.png
-rw-rw-r-- 1 sfmqrb sfmqrb  122626 Sep  6 16:58 pg270hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   87489 Sep  6 16:55 pg270.png
-rw-rw-r-- 1 sfmqrb sfmqrb   66696 Sep  6 17:04 pg271.png
-rw-rw-r-- 1 sfmqrb sfmqrb   68566 Sep  6 16:58 pg272.png
```


## [2026-09-06T21:05:00.169Z] TOOL CALL #57: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg271.png"
}
```


### [2026-09-06T21:05:00.501Z] TOOL RESULT

```

```


## [2026-09-06T21:05:00.498Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-06T21:05:17.784Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && pdftoppm -f 271 -l 271 -r 450 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf pg271hi && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg271hi.png'); w,h=im.size; print(w,h)\nim.crop((int(w*0.50),int(h*0.415),int(w*0.80),int(h*0.45))).save('crop_sirish.png')\nim.crop((int(w*0.20),int(h*0.13),int(w*0.40),int(h*0.17))).save('crop_gk271.png')\n\""
}
```


### [2026-09-06T21:05:20.941Z] TOOL RESULT

```
3825 4950
```


## [2026-09-06T21:05:23.312Z] TOOL CALL #59: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/crop_sirish.png"
}
```


### [2026-09-06T21:05:23.323Z] TOOL RESULT

```

```


## [2026-09-06T21:05:26.735Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg271hi.png'); w,h=im.size\nim.crop((int(w*0.50),int(h*0.455),int(w*0.80),int(h*0.50))).save('c1.png')\nim.crop((int(w*0.20),int(h*0.145),int(w*0.42),int(h*0.19))).save('c2.png')\n\""
}
```


### [2026-09-06T21:05:28.662Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T21:05:31.043Z] TOOL CALL #61: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/c1.png"
}
```


### [2026-09-06T21:05:31.058Z] TOOL RESULT

```

```


## [2026-09-06T21:05:38.234Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg271hi.png'); w,h=im.size\nc=im.crop((int(w*0.62),int(h*0.478),int(w*0.79),int(h*0.495)))\nc=c.resize((c.width*3,c.height*3), Image.LANCZOS)\nc.save('c3.png'); print(c.size)\n\""
}
```


### [2026-09-06T21:05:40.232Z] TOOL RESULT

```
(1950, 252)
```


## [2026-09-06T21:05:42.515Z] TOOL CALL #63: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/c3.png"
}
```


### [2026-09-06T21:05:42.533Z] TOOL RESULT

```

```


## [2026-09-06T21:05:50.972Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg271hi.png'); w,h=im.size\nc=im.crop((int(w*0.635),int(h*0.478),int(w*0.695),int(h*0.496)))\nc=c.resize((c.width*6,c.height*6), Image.LANCZOS)\nc.save('c4.png'); print(c.size)\n\""
}
```


### [2026-09-06T21:05:52.851Z] TOOL RESULT

```
(1380, 534)
```


## [2026-09-06T21:05:55.116Z] TOOL CALL #65: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/c4.png"
}
```


### [2026-09-06T21:05:55.133Z] TOOL RESULT

```

```


## [2026-09-06T21:06:09.917Z] TOOL CALL #66: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/c2.png"
}
```


### [2026-09-06T21:06:09.931Z] TOOL RESULT

```

```


## [2026-09-06T21:06:20.722Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '77725,77740p' MON_part1.txt\necho \"=== MON سرشت ===\"; grep -n \"^سرشت\\|سرشت:\\|سرشتن:\" MON_part1.txt | head -5"
}
```


### [2026-09-06T21:06:20.799Z] TOOL RESULT

```
مخفی کنند؛ راز» سر. باطن» نیت» ج. سراثر 
(سرایر): 

سریش: 14:»: (.) (گبا.) گیاهی است از 
تبر ۵ سوسنی‌ها که دارای گل‌های زینتی است 
و چون دارای ساقةٌ زیرزمینی ضخیم لعابدار 
است؛ از كویيدةً ريشة آن به عنوان چسب 
استفاده می‌کنند. این گیاه بطور خودرو در 
اکثر نقاط دنیا و همچنین ایران می‌روید؛ 
اشراس؛ اشراش. (گیا.) درختی است زینتی 
از تیرُ سماقیان که جزو گونه‌های زیتون تلخ 
(سنجد تلخ) می‌باشد. این درخت از خارج 
وارد اسران شده و در جنوب ایران 
(بندرعباس و چاه بهار) کشت می‌شود. اصل 
آن از هندوستان و هندوچین است؟؛ چریش. 
(کد.) بد کار» بدعمل. ( کد.) حقیر» فرومایه. 
=== MON سرشت ===
3576:سرشتن. آشفتن خواب کسی راء بهم زدن 
28440:پا ک‌سرشت: .۲ (ص‌مر.) با کك 
55366:سرشتی. ند خواهی» دشمنی» کینه‌ورزی. 
57359:سرشت؛ نهاد» طسعت. خوی» عادت. 
77040:سرشت: (ا.) فطرت» طینت نهاد. خوی»
```


## [2026-09-06T21:06:52.788Z] TOOL CALL #68: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg271.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/271.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/ | tail -3"
}
```


### [2026-09-06T21:06:52.867Z] TOOL RESULT

```
-rw-rw-r--  1 sfmqrb sfmqrb  78178 Sep  5 10:14 95.png
-rw-rw-r--  1 sfmqrb sfmqrb  72929 Sep  5 10:19 96.png
-rw-rw-r--  1 sfmqrb sfmqrb  65608 Sep  5 10:43 99.png
```


## [2026-09-06T21:14:53.185Z] TOOL CALL #69: Write

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/page-271.json",
 "content": "{\n  \"pdf_page\": 271,\n  \"book_page\": 241,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-06\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Klěu 2, Klâu\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *kleh₂u- / *(s)kleh₂w- (Pokorny kleu- : klēu- : klāu-) 'hook, hooked piece of wood, peg; hence bolt, key; to lock, shut'\",\n      \"note\": \"Pokorny IEW 604-605 heads the lemma 'kleu- (also klēu-) and klāu-, Meaning: hook; hooked branch or piece of wood', and gathers under it Gk. κλείς/κληΐς 'bar, bolt, key' and κλείειν, Lat. clāvis, clāvus, claudere, OCS ključь, Lith. kliūti, and the Germanic 'lot' words (Goth. hlauts, OE hlot). Watkins/AHD prints the same root as 'kleu-3. Possibly hook, peg. [Pok. klēu- 604]'. So the root, its language label and its gloss ('hook, peg used to lock doors') are all correct; the only slip is the numbering — Nourai's 'Klěu 2' is Pokorny's page-604 lemma, which AHD numbers kleu-3 (Pokorny's kleu-1 = 'hear' p.605, kleu-2 = 'wash' p.607). Note also that AHD hedges the meaning with 'possibly', and Walde-Pokorny with 'vielleicht eigentlich'.\",\n      \"note_fa\": \"ریشهٔ هندواروپایی آغازین *kleh₂u- (در پوکورنی kleu- / klēu- / klāu-، ص ۶۰۴–۶۰۵) به معنی «قلاب، چوب کج، میخ چوبی» و سپس «کلون و کلید». پوکورنی زیر همین ریشه یونانی κλείς «کلید»، لاتینی clāvis و claudere، اسلاوی کهن ključь و واژه‌های ژرمنی hlaut/hlot «قرعه، بهره» را می‌آورد و واتکینز در پیوست فرهنگ American Heritage همان را با یادداشت «شاید: قلاب، میخ» تکرار می‌کند. پس ادعای نورایی دربارهٔ خودِ ریشه، زبان آن و معنای آن درست است؛ تنها شمارهٔ ریشه اندکی متفاوت است (نورایی «Klěu 2»، واتکینز kleu-3).\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/%CE%BA%CE%BB%CE%B5%CE%AF%CF%82\",\n        \"https://en.wiktionary.org/wiki/%D8%A5%D9%82%D9%84%D9%8A%D8%AF\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:604\", \"status\": \"supports\", \"note\": \"POK_full.txt line 47616 ff.: 'Root/lemma: kleu- (also klēu-) and klāu-. Meaning: hook; hooked branch or piece of wood, etc. … Gr. Ionian κληΐς -ῖδος, Attic κλείς \\\"key\\\" (also \\\"bar, bolt; hook-shaped noose\\\"), κλείειν \\\"draw forward the bolts closing the door\\\" … Latin clavis \\\"key\\\", clavus \\\"nail\\\", claudo, -ere \\\"shut, lock\\\" … Old Norse hljóta, OE hlēotan \\\"draw lots for\\\", Gothic hlauts \\\"lot\\\" … References: WP. I 492 ff. Page(s): 604-605.' Exactly Nourai's root box and its four branches.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"WLD\", \"where\": \"Bd. I p. 492 (incoming/WLD/WLD_Bd1_pages.txt leaf 500; leaf 504 carries running head '496')\", \"stance\": \"supports\", \"note\": \"'qleu- (auch qlēu- ?) und qlāu-, vielleicht eigentlich \\\"Haken, krummes Holz oder Astgabel, Pflöckchen\\\", verbal einerseits \\\"anhaken (sich anklammern), hängenbleiben machen, (durch Anbinden an einen Pflock?) in der Bewegung beschränken, hemmen\\\"' — the page Pokorny himself cites (WP. I 492 ff.).\"},\n        {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt line 639, s.v. kleu-3\", \"stance\": \"supports\", \"note\": \"'kleu-3. Possibly hook, peg. I. Extended zero-grade form *klud- possibly in Germanic *hluta-, lot, portion (semantic development obscure) … II. Suffixed variant form *klau-do- in Latin claudere … III. Variant form *klāw-. 1. … Latin clāvis, key … 3. a. Greek kleiein, to close … [Pok. klēu- 604.]' — the same root, the same four branches, but numbered kleu-3.\"},\n        {\"src\": \"SYN\", \"where\": \"Buck, SYN.txt lines 21654 and 34022\", \"stance\": \"supports\", \"note\": \"'Derivs. of IE *klāu-, *klāwi-, denoting the (wooden) \\\"peg\\\" or primitive \\\"key\\\", as Grk. κλᾴς, κλείς, Lat. clavis, ChSl. ključь \\\"key\\\", Lat. clavus, Ir. cló \\\"nail\\\", etc.'; and 'Lat. claudere \\\"shut\\\" … and ultimately the group of words for \\\"hook, peg; key\\\" … Walde-P. 1.492 ff.'\"},\n        {\"src\": \"KLN\", \"where\": \"KLN_1966.txt line 7963, s.v. close, adj.\", \"stance\": \"supports\", \"note\": \"'All these words derive fr. I.-E. base *qlau-, *(s)qleu-, \\\"hook, forked branch, key; to close, shut\\\". … Cp. also lot.' Klein's base and gloss are Nourai's root box word for word.\"},\n        {\"src\": \"IEC\", \"where\": \"Mann, IEC.txt — no kleu-/klāu- lemma reachable in this scan (the file's alphabet runs to u- at p.1554)\", \"stance\": \"silent\", \"note\": \"Not cited by Nourai for this root; recorded only because the scan is incomplete beyond p.1554.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Greek\",\n          \"words\": \"kleiein : to close; kleidos, kleiss : key\",\n          \"verdict\": \"transcription_suspect\",\n          \"error_in\": \"book\",\n          \"book_prints\": \"kleidos, kleiss\",\n          \"correct_form\": \"kleidos, kleis (κλείς, gen. κλειδός)\",\n          \"derivation\": \"Greek κλείς (Attic kleís, Ionic κληΐς klēís, Doric κλᾱΐς klāís), gen. κλειδός kleidós, 'bar, bolt, key', from Proto-Hellenic *klāwī́ds < PIE *kleh₂u- 'nail, pin, hook (instruments of old use for locking doors)'; the intervocalic *w was lost in Attic-Ionic (*klāwid- > κλᾱϝίς > κληΐς > κλείς), which is why the stem shows up only in the oblique cases (κλειδ-). The denominative verb κλείειν (for *κλεϝίειν) 'to shut, close, bar' and κλεῖθρον 'door-bar' are built on it, and the verbal adjective κλειστός 'shut' gives modern cleistogamous. The book's second Greek form is printed 'kleiss', which is no Greek word: it is Nourai's misprint (or a misreading of a hand-set 'kleis') for the nominative κλείς. Since he gives the genitive first ('kleidos'), the pair is plainly meant as κλείς / κλειδός. The extraction is faithful to the page (see data/verification/sources/refs/ocr/BOOK/271.png, Greek box: 'kleidos, kleiss : key'). The derivation itself is entirely correct.\",\n          \"derivation_fa\": \"یونانی باستان κλείς (کلِیس، حالت اضافی κλειδός کلِیدوس) «کلون، قفل، کلید» از یونانی آغازین *klāwī́ds و آن از ریشهٔ هندواروپایی *kleh₂u- «میخ، قلاب (ابزار بستن در)»؛ واکهٔ w میان دو واکه در گویش آتیک–ایونی افتاده و از این‌رو ستاک اصلی تنها در حالت‌های غیرفاعلی (κλειδ-) دیده می‌شود. فعل κλείειν «بستن» و κλεῖθρον «کلون در» بر همین پایه ساخته شده‌اند. کتاب صورت «kleiss» را چاپ کرده که چنین واژه‌ای در یونانی نیست؛ این خطای چاپی خودِ نورایی برای κλείς (kleis) است، نه خطای خوانش اسکن — تصویر صفحه همان «kleidos, kleiss» را نشان می‌دهد. جز این غلط چاپی، اشتقاق درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%CE%BA%CE%BB%CE%B5%CE%AF%CF%82\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt line 639, kleu-3 III.3: 'Suffixed form *klāw-yo- in: a. Greek kleiein, to close: CLATHRATE; b. Greek verbal adjective kleistos, closed'. Watkins gives kleiein exactly as Nourai does (he does not print the noun κλείς here, but it stands in his Latin section as the cognate of clāvis).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"POK_full.txt line 47616 ff. (p.604)\", \"stance\": \"supports\", \"note\": \"'Gr. Ionian κληΐς -ῖδος, Old Attic κλῄς, Attic κλείς, Doric κλαΐς, -ίδος \\\"key\\\" (also \\\"bar, bolt; hook-shaped noose; oarlock\\\") … κλῄειν (Ionian), κλείω (Attic) \\\"draw forward the bolts closing the door\\\"'. No form 'kleiss' anywhere.\"},\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt lines 7963 (close, adj.) and 7882 (cleido-)\", \"stance\": \"supports\", \"note\": \"'Gk. κλείς, gen. κλειδός, \\\"bar, bolt, key\\\" [whence κλείειν (for *κλεϝίειν), \\\"to shut, close, bar\\\", κλεῖθρον, \\\"bar for closing a door\\\"]' — the nominative is κλείς, never *kleiss.\"},\n            {\"src\": \"IEC\", \"where\": \"IEC.txt line 7296\", \"stance\": \"supports\", \"note\": \"Mann has 'kleistos (variant of kleitos) Gk. kleistós, adj. \\\"shut\\\"' under the same family.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"kelîd «کلید» : key\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"NP کلید kelīd/kilīd 'key' is a Greek loanword, taken over in the Hellenistic/Parthian centuries from the oblique stem κλειδ- of κλείς (acc. κλεῖδα): Gk. kleid- > MP *kilēd (unattested in the Book-Pahlavi corpus but presupposed by MacKenzie's PHD entry 'klīd [klyt' | N kilīd] key') > NP kilīd/kelīd, with the regular Middle-to-New Persian raising ē > ī and the anaptyctic i in the initial cluster kl- (compare Dezfuli kelil, Kabuli kilī, Tehrani kilit). The word spread onward from Persian: Chagatai کلید, Uyghur كىلىت, Uzbek kalit, Kurdish kilīd, and (through Arabic) back into Persian as مقلاد (node 5). Mo'in's own footnote in Borhan-e Qate' p.1687 states the same route.\",\n          \"derivation_fa\": \"«کلید» وام‌واژه‌ای یونانی است: از ستاک غیرفاعلیِ κλειδ- (حالت مفعولی κλεῖδα) واژهٔ یونانی κλείς، که در دورهٔ هلنی/اشکانی به ایرانی راه یافته و به فارسی میانهٔ *kilēd رسیده (مکنزی: klīd [klyt'] «کلید»، فارسی نو kilīd) و سپس با تبدیل ای کشیدهٔ فارسی میانه به ی در فارسی نو «کلید» شده است؛ همزهٔ میانجی i در خوشهٔ آغازین kl- افزوده شده (قس گویش دزفولی کلیل، کابلی کِلی، تهرانی کیلیت). حاشیهٔ معین بر برهان قاطع (ص ۱۶۸۷) نیز همین را می‌گوید: «کلید … یونانی kleis و kleidos». از فارسی به کردی، ترکی جغتایی، اویغوری و ازبکی رفته است. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%DA%A9%D9%84%DB%8C%D8%AF\"],\n          \"ref_check\": [\n            {\"ref\": \"BQT:1687\", \"status\": \"supports\", \"note\": \"Borhan-e Qate' ed. Mo'in, vol. 3, printed p.1687 = incoming/BQT/BQT_v3_pages.txt leaf 479 ([pdf page 480]). Mo'in's footnote to کلید reads: «کلید — بکسر اول … یونانی kleis و kleidos … کردی kilid (قفل) … معرَّب: «اقلید» و «اکلیل» و «مقلاد» … ابزاری که بدان قفل را گشایند و بندند». Exactly Nourai's arrow Greek → Persian, plus the Arabic offshoots of nodes 4-5.\"},\n            {\"ref\": \"FVQ:268\", \"status\": \"supports\", \"note\": \"Jeffery, FVQ_pages.txt leaf 285 (printed p.268), s.v. مقلاد: 'The Pers. کلید to which they refer it is itself a borrowing from the Gk. κλείς, κλειδα (Vullers, Lex, ii, 876), which was also borrowed into Aram. אקלידא, Syr. ʾaqlīdā.'\"},\n            {\"ref\": \"ARK:236\", \"status\": \"not_checked\", \"note\": \"Rokn-zadeh Adamiyyat, Arkan-e Sokhan (1347/1968): refs_online.json records it as not digitised on any accessible platform (kind 'catalog', url null).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie, PHD_mackenzie.txt line 3296\", \"stance\": \"supports\", \"note\": \"'klīd [klyt' | N kilīd] key' (OCR renders the headword as 'kilel [klyl | N kilid]'; the same entry stands in PHD.txt line 428 as 'kilēl [klyl | N kilīd] key'). MacKenzie gives the Pahlavi ancestor of NP kilīd.\"},\n            {\"src\": \"MON\", \"where\": \"Mo'in, MON_part1.txt line 15581 s.v. اقلید\", \"stance\": \"partial\", \"note\": \"«اقلید: [معر.] (اِ.) کلید، مقلاد» — Mo'in treats the Arabic اقلید as Arabicized Persian کلید, i.e. Persian is the immediate source of the Arabic, though he derives کلید itself from Greek in his Borhan footnote.\"},\n            {\"src\": \"HRN\", \"where\": \"HRN.txt, grep 'kilid' → only line 7430, an incidental occurrence\", \"stance\": \"silent\", \"note\": \"Horn's Grundriss has no numbered entry for kilīd (a transparent Greek loan, outside his inherited-vocabulary remit).\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Aramaic\",\n          \"words\": \"\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The empty pass-through box stands for Jewish/Christian Aramaic אַקְלִידָא ʾaqlīdā, Syriac ܐܩܠܝܕܐ ʾaqlīdā 'key', the form through which the Greek word reached Arabic. It is not an inherited Indo-European descendant of the root — Aramaic is Semitic — but a Hellenistic-period loan from Greek κλεῖδα (accusative of κλείς), with the prosthetic ʾa- that Aramaic regularly puts before an initial kl- cluster and the Aramaic determined-state ending -ā. Drawing it as a branch straight off the Indo-European root box (rather than off the Greek box, as the arrow from Greek to Aramaic in fact does on the page) is a diagram convention of Nourai's, not a claim of Semitic descent from PIE; read that way the node is right. The chart's own arrow does run Greek → Aramaic, which is the accepted route (Fraenkel, Jeffery, Wiktionary).\",\n          \"derivation_fa\": \"این جعبهٔ خالی نمایندهٔ واژهٔ آرامی/سریانی «ܐܩܠܝܕܐ / אקלידא» (ʾaqlīdā) «کلید» است که حلقهٔ واسط میان یونانی و عربی است. آرامی زبانی سامی است و این واژه در آن ارثی نیست، بلکه وام‌واژه‌ای است از یونانی κλεῖδα (حالت مفعولیِ κλείς) در دورهٔ هلنی، با همزهٔ آغازینِ افزوده (ʾa-) که آرامی پیش از خوشهٔ kl- می‌آورد و پایانهٔ حالت معرفهٔ -ā. اتصال این جعبه به خود ریشهٔ هندواروپایی صرفاً شیوهٔ نمودارکشی نورایی است؛ پیکان واقعیِ صفحه از یونانی به آرامی می‌رود و همین مسیر را فرنکل، جفری و ویکی‌واژه می‌پذیرند. پس با این تفسیر، گره پذیرفتنی است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D8%A5%D9%82%D9%84%D9%8A%D8%AF\"],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The node carries no reference of its own in the book; the Aramaic link is documented at the Arabic node's FVQ:267-268.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"FVQ\", \"where\": \"Jeffery, FVQ_pages.txt leaf 285 (p.268)\", \"stance\": \"supports\", \"note\": \"'… the Gk. κλείς, κλειδα … which was also borrowed into Aram. אקלידא, Syr. ʾaqlīdā. … we are fairly safe in concluding that the Ar. إقليد is from the Syr. ʾaqlīdā.'\"},\n            {\"src\": \"AFA\", \"where\": \"Fraenkel, AFA.txt lines 1145-1160 (Die aramäischen Fremdwörter im Arabischen, pp. 15-16)\", \"stance\": \"supports\", \"note\": \"Fraenkel treats إقليد as an Aramaic loan and adds 'Dagegen sind die Bedeutungen von قلّد \\\"anvertrauen\\\" u. s. w. wohl alle aus الإقليد \\\"Schlüssel\\\" erst denominativ abgeleitet' — the Arabic verbal root is secondary to the borrowed noun.\"},\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt line 7963 (close, adj.)\", \"stance\": \"silent\", \"note\": \"Klein lists the Indo-European reflexes of *qlāu- but says nothing about the Aramaic transmission.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Arabic\",\n          \"words\": \"eqlîd : key; meqlâd, maqâlîd\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Arabic إِقْلِيد ʾiqlīd 'key' (Ḥaḍramī; already in Ṣaḥīḥ al-Buḵārī 64:86, pl. أَقَالِيد ʾaqālīd) continues Aramaic/Syriac ʾaqlīdā, itself from Gk. κλεῖδα; مِقْلَاد miqlād with plural مَقَالِيد maqālīd is then an Arabic tool-noun (ism al-āla, pattern mifʿāl) re-formed on ʾiqlīd by analogy with مفتاح miftāḥ 'key' — the plural maqālīd is the Qur'anic form (39:63, 42:10, 'His are the maqālīd of the heavens and the earth'). On the chart's NOTE (FVF:35 claims eqlīd is from Persian kelīd): the two claims are not really rivals, since Persian kelīd is itself Greek; the question is only the immediate donor. The medieval philologists (al-Jawālīqī, al-Khafājī, al-Suyūṭī) and, following them, Emām Shūshtarī, Mo'in and Addi Shir call it muʿarrab of Persian کلید; Dvořák defended the direct Persian route; but Fraenkel and Jeffery — and today Wiktionary with the Syriac citation — prefer the Aramaic mediation, chiefly because of the prosthetic ʾa- and the -d (not -t/-dh) which point to the Aramaic determined form ʾaqlīdā rather than to Persian kilīd. Modern scholarship therefore sides with Nourai's chart (Greek → Aramaic → Arabic) against the note.\",\n          \"derivation_fa\": \"«إقليد» عربی (کاربرد حَضرَمی؛ در صحیح بخاری ۶۴:۸۶ با جمعِ أقاليد) دنبالهٔ آرامی/سریانیِ ʾaqlīdā است و آن خود از یونانی κλεῖδα. «مِقْلاد» با جمعِ «مَقالید» صورتی است که عرب بر وزن اسم آلت (مِفعال) از إقليد ساخته، به قیاس «مفتاح»؛ جمع «مقالید» صورت قرآنی است («له مقالید السموات والأرض»، زمر ۶۳ و شوری ۱۰). دربارهٔ یادداشت صفحه (ادعای فرهنگ واژه‌های فارسی در زبان عربی که إقليد از «کلید» فارسی است): این دو ادعا در اصل ناسازگار نیستند، چون «کلید» فارسی خود یونانی است؛ اختلاف تنها بر سر واسطهٔ بی‌واسطه است. جوالیقی، خفاجی، سیوطی، ادی شیر و معین آن را «معرّبِ کلید» می‌خوانند، اما فرنکل و جفری — و امروز ویکی‌واژه — واسطهٔ آرامی را ترجیح می‌دهند، به دلیل همزهٔ آغازین (ʾa-) و دالِ پایانی که به صورت معرفهٔ آرامی ʾaqlīdā می‌خورد نه به kilīd فارسی. پس پژوهش امروزی جانب نمودار نورایی را می‌گیرد، نه جانب آن یادداشت.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%A5%D9%82%D9%84%D9%8A%D8%AF\",\n            \"https://en.wiktionary.org/wiki/%D9%85%D9%82%D9%84%D8%A7%D8%AF\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"FVQ:267\", \"status\": \"supports\", \"note\": \"Jeffery, FVQ_pages.txt leaf 285, entry '(Miqlād). xxxix, 63; xlii, 10. Key. Only in the plural form مقاليد …' beginning on printed p.267 and continuing on p.268: 'It was early recognized as a foreign word, and said by the philologers to be of Persian origin. The Pers. کلید to which they refer it is itself a borrowing from the Gk. κλείς, κλειδα … In spite of Dvořák's vigorous defence of the theory that it passed directly from Persian into Arabic, we are fairly safe in concluding that the Ar. إقليد is from the Syr. ʾaqlīdā, and the form مقلاد formed therefrom on the analogy of مفتاح, etc.' This is Nourai's node verbatim, including the NOTE's counter-claim and its rebuttal.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"ARB\", \"where\": \"al-Jawālīqī, al-Muʿarrab, ARB_mo3rb.txt lines 22211 and 22238-22241\", \"stance\": \"partial\", \"note\": \"«المِقليد: المفتاح، فارسي معرّب، لغة في الإقليد» and, on maqālīd, «وهي عربية خالصة، وكذلك الإقليد، وادّعى ابن دريد … ومادة (ق ل د) عربية والاشتقاق منها غير بيّن» — al-Jawālīqī records the Persian-loan view (Nourai's NOTE), while noting others held it pure Arabic; he knows nothing of the Aramaic link.\"},\n            {\"src\": \"TAD\", \"where\": \"al-ʿUnaysī, TAD_pages.txt line 2213\", \"stance\": \"supports\", \"note\": \"«إقليد وإكليل ومقلاد … يوناني … معناه مفتاح» — al-ʿUnaysī classes the whole group as Greek in origin, meaning 'key'.\"},\n            {\"src\": \"AFA\", \"where\": \"Fraenkel, AFA.txt lines 1145-1160 (pp. 15-16)\", \"stance\": \"supports\", \"note\": \"Fraenkel's pages 15-16 — Jeffery's own authority — treat إقليد as the Aramaic loan and the Arabic verb قلّد as denominative from it.\"},\n            {\"src\": \"AFM\", \"where\": \"Addi Shir, AFM_pages.txt (grep 'اقليد', 'إقليد', 'مقلاد', 'كليد')\", \"stance\": \"silent\", \"note\": \"No hit in the OCR of Kitāb al-Alfāẓ al-Fārisiyya al-muʿarraba.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Persian\",\n          \"words\": \"meqlâd «مقلاد» : key\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Literary/Arabizing Persian مقلاد meqlād 'key' (with the Arabic broken plural مقالید maqālīd, freely used in Persian prose and in Qur'anic quotation) is a re-borrowing: the Greek word entered Persian once directly as کلید, then travelled Greek → Aramaic → Arabic (miqlād), and Arabic handed the derived form back to Persian after the conquest — a classic Persian → (via Greek/Aramaic) Arabic → Persian round trip in which مقلاد and کلید are doublets in the same language. Mo'in's own dictionary registers the pair: «اقلید: [معرّب] (اِ.) کلید، مقلاد», and his Borhan footnote lists «معرَّب: اقلید و اکلیل و مقلاد» under کلید.\",\n          \"derivation_fa\": \"«مقلاد» در فارسی ادبی و در متون قرآنی‌مآب (با جمع عربی «مقالید») وام‌واژه‌ای است از عربی؛ یعنی همان واژهٔ یونانی که یک‌بار مستقیم به شکل «کلید» به فارسی آمده بود، بار دوم از راه آرامی و عربی و در قالب صرفی عربیِ مِفعال (میقلاد/مِقلاد) به فارسی بازگشته است. بنابراین «مقلاد» و «کلید» در فارسی دوگانه (doublet) اند. معین در فرهنگ فارسی می‌نویسد «اقلید: [معر.] (اِ.) کلید، مقلاد» و در حاشیهٔ برهان قاطع ذیل «کلید» می‌آورد: «معرَّب: اقلید و اکلیل و مقلاد». ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D9%85%D9%82%D9%84%D8%A7%D8%AF\"],\n          \"ref_check\": [\n            {\"ref\": \"MON:4283\", \"status\": \"not_checked\", \"note\": \"Only the 2-volume Adena abridgement of Mo'in is on disk (MON_part1/2.txt, no page mapping to the 6-volume Amir Kabir set Nourai cites), and refs_online.json notes that vajehyab/abadis give the entry text but no page numbers. In the abridgement the relevant statement is at MON_part1.txt line 15581: «اقلید: [معر.] (اِ.) کلید، مقلاد» — it supports the content of the node, but the page 4283 itself could not be checked.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' ed. Mo'in, vol. 3 p.1687 (BQT_v3_pages.txt leaf 479), footnote to کلید\", \"stance\": \"supports\", \"note\": \"«… معرَّب «اقلید» و «اکلیل» و «مقلاد» …» — Mo'in explicitly lists مقلاد as the Arabicized offshoot of کلید, i.e. the form Persian took back from Arabic.\"},\n            {\"src\": \"MON\", \"where\": \"MON_part1.txt line 15581\", \"stance\": \"supports\", \"note\": \"«اقلید: [معر.] (اِ.) کلید، مقلاد».\"},\n            {\"src\": \"RCH\", \"where\": \"Richardson, RCH.txt\", \"stance\": \"silent\", \"note\": \"No usable OCR hit for مقلاد in the scan.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Germanic\",\n          \"words\": \"hluta : portion obtained\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Proto-Germanic *hlutą / *hlutaz 'lot, share' (Goth. hlauts, ON hlutr, hlaut, OE hlot, OS hlot, OHG (h)luz, MHG lôz, G. Los), with the strong verb *hleutaną 'to cast lots, obtain by lot' (OE hlēotan, ON hljóta, OHG hliozan 'to cast lots, foretell, practise magic'). The connexion to *kleu-/*klāu- 'hook' rests on the zero-grade extension *klud- and on a semantic guess — the lot as the little peg or hooked stick drawn from a container, hence 'the piece one hooks out' > 'portion obtained' > 'fate'. Both of Nourai's own authorities hedge it: AHD writes 'Extended zero-grade form *klud- POSSIBLY in Germanic *hluta-, lot, portion (semantic development obscure)', and Klein 'fr. Teut. base *hlut-, which POSSIBLY meant orig. \\\"to hook to\\\"'. Pokorny prints the Germanic set 'ohne s- perhaps' under the same lemma. The form 'hluta' is AHD's reconstruction copied exactly; the gloss 'portion obtained' is likewise AHD's. Verdict plausible rather than confirmed because the Germanic-to-*kleu- link is explicitly marked as uncertain by every source that states it.\",\n          \"derivation_fa\": \"ژرمنی آغازین *hlutą/*hlutaz «قرعه، بهره» (گوتی hlauts، نورس کهن hlutr و hlaut، انگلیسی کهن hlot، آلمانی عالی کهن (h)luz، آلمانی Los) در کنار فعل قوی *hleutaną «قرعه انداختن، به قید قرعه به دست آوردن». پیوند این خانواده با ریشهٔ *kleu-/*klāu- «قلاب، میخ» بر صورت صفرْدرجهٔ *klud- و بر حدسی معنایی استوار است: قرعه همان چوب یا میخِ کوچکی بوده که از ظرف بیرون می‌کشیده‌اند، پس «آنچه با قلاب بیرون کشیده می‌شود» ← «بهرهٔ به‌دست‌آمده» ← «سرنوشت». هر دو مرجعِ خودِ نورایی این پیوند را با احتیاط می‌آورند: واتکینز می‌نویسد «شاید در ژرمنی *hluta-، تحول معنایی مبهم است» و کلاین «شاید در اصل به معنی چنگ‌زدن/آویختن». پس ادعا با احتیاط پذیرفتنی است، نه قطعی.\",\n          \"sources\": [\"https://www.etymonline.com/word/lot\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"AHD_watkins1985.txt line 639: 'kleu-3 … I. Extended zero-grade form *klud- possibly in Germanic *hluta-, lot, portion (semantic development obscure). 1. Old English hlot, lot: LOT. 2. Dutch lot, lot: LOTTERY. 3. Old French lot (> French lot), lot, portion: LOTTO; ALLOT.' The form and gloss are Watkins's, but he flags the connexion with 'possibly' and the semantics as 'obscure' — Nourai's box carries no such caveat.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"POK_full.txt p.604-605 block\", \"stance\": \"partial\", \"note\": \"'without s- perhaps Old Norse hljóta strong v. \\\"draw lots for, receive\\\", Old English hlēotan … Gothic hlauts \\\"lot, fate, heritage\\\" … Old High German (h)luz \\\"lot, closed allotment, portion of the land\\\"' — Pokorny too introduces the set with 'perhaps'.\"},\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt line 22176, s.v. lot\", \"stance\": \"partial\", \"note\": \"'ME. lotte, fr. OE. hlot, rel. to ON. hlutr, \\\"lot, share\\\" … Goth. hlauts … fr. Teut. base *hlut-, which possibly meant orig. \\\"to hook to\\\", and corresponds to I.-E. base *(s)qleu-, *qlāu-, \\\"a hook, forked branch, key; to close, shut; to catch, be caught on\\\".'\"},\n            {\"src\": \"WLD\", \"where\": \"WLD Bd. I p.492 ff. (leaf 500 ff.)\", \"stance\": \"supports\", \"note\": \"The Germanic 'Los' family is placed under qleu-/qlāu- in the same article whose head reads 'vielleicht eigentlich \\\"Haken, krummes Holz…\\\"'.\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"English\",\n          \"words\": \"lot, lottery, lotto\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English lot is inherited: OE hlot 'lot, portion, share, what falls to one' > ME lot(te) > lot, with the sense 'a large number' only from the 19th century. Lottery and lotto are re-imports of the same Germanic word through Romance: Frankish/Germanic *hlot was taken into Old French as lot and into Italian as lotto 'lot, share', whence It. lotteria 'public lottery' > E. lottery (16th c., first of the Genoese and Venetian state draws) and It. lotto > E. lotto (18th c. game). Klein states the loan direction explicitly. So the words are English, they mean what the chart implies, and they do descend from the Germanic box above them.\",\n          \"derivation_fa\": \"واژهٔ انگلیسی lot میراثی است: انگلیسی کهن hlot «قرعه، بهره» ← انگلیسی میانه lot(te) ← lot امروزی (معنی «مقدار زیاد» تنها از سدهٔ نوزدهم). اما lottery و lotto همان واژهٔ ژرمنی‌اند که از راه زبان‌های رومی بازگشته‌اند: صورت ژرمنی/فرانکی *hlot به فرانسهٔ کهن lot و به ایتالیایی lotto «قرعه، سهم» رفته و از ایتالیایی lotteria «قرعه‌کشی همگانی» به انگلیسی lottery (سدهٔ شانزدهم، هم‌زمان با قرعه‌کشی‌های دولتی جنوا و ونیز) و lotto (بازی سدهٔ هجدهم) رسیده است. کلاین همین جهت وام‌گیری را تصریح می‌کند. ادعای نورایی درست است.\",\n          \"sources\": [\"https://www.etymonline.com/word/lot\"],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The node carries no reference in the book; checked against Klein and AHD instead (below).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt lines 22176 (lot) and 22183 (lottery, lotto)\", \"stance\": \"supports\", \"note\": \"'F. lot, \\\"lot, portion, share\\\", It. lotto, \\\"lot, portion, share\\\", lotteria, \\\"lottery\\\", are Teut. loan words. Cp. lottery, lotto, allot.' and 'lottery, n. — It. lotteria, \\\"public lottery\\\", fr. lotto … (but F. loterie derives fr. Du. loterije, fr. Du. lot, \\\"lot\\\"). … lotto, n., a game of chance. — It., lit. \\\"a lot\\\".'\"},\n            {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt line 639 and index line 1767\", \"stance\": \"supports\", \"note\": \"'1. Old English hlot, lot: LOT. 2. Dutch lot, lot: LOTTERY. 3. Old French lot … LOTTO; ALLOT'; index: 'LOT kleu-3 … LOTTERY kleu-3 LOTTO kleu-3'.\"},\n            {\"src\": \"SKT\", \"where\": \"SKT.txt\", \"stance\": \"silent\", \"note\": \"Skeat's concise edition gives lot from AS. hlot but the relevant lines are unreadable in this OCR (grep '^lot' returns nothing usable).\"}\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"Latin\",\n          \"words\": \"claudere : to lock up, close\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Latin claudō, -ere, clausī, clausum 'to shut, close, lock up' is a d-present built on the *klāu-i- noun that also gives clāvis 'key' (i.e. *klāwi-dō 'to work with the bolt/key'), beside clāvus 'nail, peg' and clāva 'knotty stick, club'; Pokorny prints it as '*klāui-dō, with present formation -d-'. The -au- of the root shows up unchanged in the simplex claudō but is regularly weakened to -ū- in composition (*con-claudō > conclūdō, in-clūdō, ex-clūdō), which is why the English prefixed verbs in node 9 have -clude and the simplex gives close. The gloss 'to lock up, close' is exact.\",\n          \"derivation_fa\": \"لاتینی claudō, -ere «بستن، قفل کردن» فعلی است ساخته‌شده با «د»ِ حاضرساز بر پایهٔ همان نامِ *klāu-i- که clāvis «کلید» را هم داده است (یعنی *klāwi-dō «با کلون/کلید کار کردن»)، در کنار clāvus «میخ» و clāva «چماق». پوکورنی همین را می‌نویسد: «claudo, -ere \\\"shut, lock\\\" (*klāui-dō، با ساخت حاضرِ -d-)». دوگانهٔ au در فعل ساده دست‌نخورده می‌ماند اما در ترکیب به ū بدل می‌شود (con-claudō ← conclūdō، inclūdō، exclūdō)؛ به همین سبب است که در انگلیسی صورت ساده close و صورت‌های پیشوندی conclude/include/exclude اند. معنای داده‌شده دقیق است.\",\n          \"sources\": [\"https://www.etymonline.com/word/close\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt line 639: 'II. Suffixed variant form *klau-do- in Latin claudere, to close (< \\\"to lock with a hook, bolt\\\"): CLAUSE, CLOISONNE, CLOISTER, CLOSE, (CLOSURE), (CLOZE); CONCLUDE, ECLOSION, EXCLUDE, INCLUDE, OCCLUDE, PRECLUDE, RECLUSE, SECLUDE.'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"POK_full.txt p.604 block\", \"stance\": \"supports\", \"note\": \"'Latin clavis \\\"key\\\", Demin. claviculae \\\"a tendril\\\", clavus \\\"nail\\\", claudo, -ere \\\"shut, lock\\\" (*klāui-dō, with present formation -d-); in addition probably claudus \\\"lame\\\" …'\"},\n            {\"src\": \"LAT\", \"where\": \"Ernout-Meillet, LAT.txt lines 12308-12382\", \"stance\": \"supports\", \"note\": \"The article 'clau-; clauis, clauus (clauos), claudo' treats clāuis, clāuus and claudō as one family and compares Gk. κλαϝίς and OCS ključь ('y.sl. kljuci \\\"clé\\\" rappelle claudo, clauus, et gr. κλαϝίς').\"},\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt line 7963, s.v. close, adj.\", \"stance\": \"supports\", \"note\": \"'L. clausus, pp. of claudere, \\\"to shut, close\\\", which is rel. to clavis, \\\"key\\\", clavus, \\\"nail\\\", clava, \\\"a knotty stick, staff, club\\\".'\"}\n          ]\n        },\n        {\n          \"id\": 9,\n          \"lang\": \"English\",\n          \"words\": \"close, closet, clause; include, exclude, conclude\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"All six are Latin words that reached English through French. Close: L. clausus (pp. of claudere) > OF clos > ME clos, and the verb ME closen from OF clos, pp. of clore. Closet: OF closet, diminutive of clos 'enclosure'. Clause: ML clausa (for L. clausula 'the close of a rhetorical period', from clausus), through OF clause, 13th c. Include, exclude, conclude: L. inclūdere, exclūdere, conclūdere — the prefixed compounds of claudere with the regular au > ū weakening — adopted in Middle English (14th-15th c.) partly through French, keeping the -clude of the Latin infinitive. Klein and Watkins list exactly this set under the root.\",\n          \"derivation_fa\": \"هر شش واژه لاتینی‌اند و از راه فرانسه به انگلیسی رسیده‌اند: close از clausus (اسم مفعول claudere) ← فرانسهٔ کهن clos ← انگلیسی میانه clos؛ closet از closet فرانسهٔ کهن، مصغّرِ clos «محوطهٔ بسته»؛ clause از لاتینی میانهٔ clausa (به جای clausula «پایان یک دورهٔ بلاغی») از راه فرانسهٔ کهن در سدهٔ سیزدهم؛ و include/exclude/conclude از inclūdere، exclūdere و conclūdere، یعنی همان claudere با پیشوند و با ابدال قاعده‌مندِ au به ū در ترکیب، که در سده‌های چهاردهم و پانزدهم وارد انگلیسی میانه شده‌اند. کلاین و واتکینز دقیقاً همین فهرست را ذیل این ریشه می‌آورند. ادعای نورایی درست است.\",\n          \"sources\": [\"https://www.etymonline.com/word/close\"],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"No reference on the node in the book; checked against Klein and AHD.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt lines 7857 (clause), 7963-7965 (close, closet)\", \"stance\": \"supports\", \"note\": \"'clause, n. — ME., fr. OF. (= F.) clause, fr. ML. clausa, used in the sense of L. clausula … fr. L. clausus, pp. of claudere'; 'close, adj. — ME. clos, fr. OF. (= F.) clos, fr. L. clausus'; 'closet, n. — OF., dimin. of clos, \\\"enclosure\\\"'. Klein's cross-reference list under close, adj. includes conclude, exclude, include.\"},\n            {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt line 639 and index lines 1370, 1389, 1676, 1485\", \"stance\": \"supports\", \"note\": \"Index entries 'CLAUSE kleu-3', 'CLOSE kleu-3', 'CONCLUDE kleu-3', 'INCLUDE kleu-3', 'EXCLUDE kleu-3'.\"},\n            {\"src\": \"SKT\", \"where\": \"SKT.txt lines 3525-3526\", \"stance\": \"supports\", \"note\": \"'close (2), to shut in. (F.-L.) M.E. clos … O.F. clos, pp. of clore, to shut in. — L. clausus, pp. of claudere … Der. dis-close, en-close, in-close.'\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 1,\n      \"root\": \"Klis\",\n      \"verdict\": \"plausible\",\n      \"modern_form\": \"Proto-Indo-Iranian *ćraiš- 'to adhere, attach' (Skt. śreṣ-/śliṣ-, Proto-Iranian *sraiš-); a Proto-Indo-European antecedent is not securely reconstructable\",\n      \"note\": \"The family is real and the gloss 'adhere' is right, but the level at which it can be reconstructed is Indo-Iranian, not Indo-European. Cheung (Etymological Dictionary of the Iranian Verb, s.v. *sraiš 'to put together, attach') closes the article with the flat statement 'This Ir. root has no certain IE cognates', and Wiktionary, following Mayrhofer EWAia II 670, derives Skt. श्लिष् from Proto-Indo-Iranian *ćRayš 'to adhere, attach' and adds 'Further origin is uncertain; perhaps related to Proto-Indo-European *ḱley- (\\\"to lean, incline\\\")'. Nourai's headword 'Klis' is Mann's reconstruction style (he cites IEC:1637), and Mann does reconstruct freely at IE level; but the page cited cannot be checked (see ref_check) and no other IE dictionary sets up a root *klis- 'adhere' — Pokorny has no such lemma. Hence 'plausible': the Indo-Iranian core of the chart is solid, the Indo-European label on the root box is not. A second, structural caveat runs through the whole entry: Nourai stacks Old Iranian → Avestan → Pahlavi → Persian, but the Persian words continue Old Iranian directly; Avestan is a sister, not an ancestor, and the Avestan verb is attested only in the compound ham.sriš-.\",\n      \"note_fa\": \"خانوادهٔ واژگانی واقعی است و معنای «چسبیدن» درست، اما سطحی که می‌توان این ریشه را بازسازی کرد هندوایرانی است نه هندواروپایی. چونگ در فرهنگ ریشه‌شناختی فعل ایرانی ذیل *sraiš «به هم پیوستن، چسباندن» صریح می‌نویسد: «این ریشهٔ ایرانی هم‌ریشهٔ هندواروپایی مطمئنی ندارد»، و ویکی‌واژه به پیروی از مایرهوفر (EWAia II: 670) سنسکریت श्लिष् را از هندوایرانی آغازین *ćraiš «چسبیدن» می‌گیرد و می‌افزاید که «خاستگاه دورتر آن نامعلوم است؛ شاید با ریشهٔ هندواروپایی *ḱley- \\\"تکیه دادن\\\" پیوند داشته باشد». سرواژهٔ «Klis» شیوهٔ بازسازی مان (Mann) است که نورایی به او ارجاع می‌دهد، ولی صفحهٔ ارجاع‌شده در نسخهٔ در دسترس نیست و هیچ فرهنگ هندواروپایی دیگری ریشه‌ای به صورت *klis- «چسبیدن» ندارد؛ پوکورنی چنین مدخلی ندارد. پس: هستهٔ هندوایرانی نمودار استوار است، اما برچسب «هندواروپایی» بر جعبهٔ ریشه پذیرفتنی نیست. ایراد ساختاری دوم آنکه نورایی زنجیرهٔ ایرانی باستان ← اوستایی ← پهلوی ← فارسی را پشت‌سرهم چیده، حال آنکه واژه‌های فارسی مستقیماً دنبالهٔ ایرانی باستان‌اند و اوستایی خواهرِ آنهاست نه نیایشان؛ افزون بر این فعل اوستایی تنها در ترکیبِ ham.sriš- گواهی شده است.\",\n      \"sources\": [\"https://en.wiktionary.org/wiki/%E0%A4%B6%E0%A5%8D%E0%A4%B2%E0%A4%BF%E0%A4%B7%E0%A5%8D\"],\n      \"ref_check\": [\n        {\"ref\": \"IEC:1637\", \"status\": \"not_checked\", \"note\": \"Mann's Indo-European Comparative Dictionary runs to p.1682, but the archive.org scan on disk (IEC.txt, 858 leaves) breaks off in the letter u- at printed p.1554 (last leaf: 'ulquō … uln- (2)'), so p.1637 — which on Mann's plan falls in the back Supplement, where 'Supt: K' is repeatedly cross-referenced from the main text — is simply absent. Searching the whole file for a headword 'klis-', 'kleis-' or 'ḱlis-' returns nothing; the nearest lemmas are 'kliḱō, io (?) \\\"squeeze, twist\\\"' (Skt. kliśyāmi) and 'kleistos', neither of which means 'adhere'.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"CHEUNG\", \"where\": \"CHEUNG.txt lines 23244-23270, s.v. *sraiš\", \"stance\": \"contradicts\", \"note\": \"'*sraiš \\\"to put together, attach\\\" … *SANSKRIT: śreṣ \\\"to cling, stick, be attached, hold\\\" (RV) = EWAia II: 670. ⊙ This Ir. root has no certain IE cognates.' Cheung reconstructs the root at Iranian/Indo-Iranian level only and denies a secure IE pedigree.\"},\n        {\"src\": \"POK\", \"where\": \"POK_full.txt (searched 'klis', 'kleis', 'śliṣ', 'ślēṣ')\", \"stance\": \"silent\", \"note\": \"Pokorny has no lemma *klis-/*kleis- 'adhere'; the only near forms are kleu- 'hook' (p.604) and gleit-/glei- 'kleben' (an unrelated g-initial family).\"},\n        {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. I (incoming/WLD/WLD_Bd1_pages.txt, region qleik- … qleu- at pp.492 ff.)\", \"stance\": \"silent\", \"note\": \"The q-l-i- section has 'qleik- \\\"(schmerzhaft) drücken, quetschen, klemmen\\\"' (Skt. kliśnāti) but no root meaning 'adhere'.\"},\n        {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien p.75 no. 732 (HUB.txt leaf 85)\", \"stance\": \"partial\", \"note\": \"Hübschmann sorts the material into two semantic groups without setting up an IE root: '1) skr. śrī \\\"verbinden, zusammenfügen\\\", vgl. skr. śri \\\"mengen, mischen\\\", np. siristan \\\"mischen\\\", sirišt \\\"Mischung, Natur, Anlage\\\" …; 2) skr. śliṣ \\\"anhangen, haften, kleben\\\", zd. riš \\\"haften\\\", np. siriš \\\"Leim\\\".'\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Old Iranian\",\n          \"words\": \"srîš, sraîš : a plant and its resin that was used for making glue.\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Abolghasemi (FFD p.60), Nourai's source, sets up an Old Iranian VERBAL root *sraiš- 'to stick, to glue' with two nominal derivatives: the weak/zero grade *srišta- (> MP srišt > NP سرشت) and the full grade *sraiša- (> MP srēš > NP سریش). So the reconstructed forms *sraiš / *sriš are right, and Proto-Iranian *sraiš- is confirmed independently by Cheung. What is not right is the gloss: 'a plant and its resin that was used for making glue' is not an Old Iranian meaning but the New Persian meaning of سریش, which Abolghasemi quotes verbatim from Borhan-e Qate' («رستنی‌ای که … بعد از رسیدگی خشک کنند و آرد سازند و کفشگران و صحافان چیزها بدان چسبانند») to illustrate the descendant, not the ancestor. The plant is the asphodel (Asphodelus, Persian سریش/اشراس), whose dried, pounded root — not a resin — yields the paste; Mo'in's own dictionary describes it so. Nourai has folded the Persian gloss back into the Old Iranian box.\",\n          \"derivation_fa\": \"ابوالقاسمی در «فعل‌های فارسی دری» ص ۶۰ — همان مأخذ نورایی — ریشهٔ ایرانی باستانِ *sraiš را به معنی «چسباندن» می‌نهد و دو مشتق نامی از آن می‌گیرد: صورت ضعیف *srišta- (← فارسی میانه srišt ← «سرشت») و صورت کامل *sraiša- (← فارسی میانه srēš ← «سریش»). پس صورت‌های بازسازی‌شده درست‌اند و چونگ نیز ایرانی آغازینِ *sraiš را تأیید می‌کند. آنچه درست نیست معنای جعبه است: «گیاهی و صمغ آن که با آن چسب می‌ساختند» معنای ایرانی باستان نیست، بلکه معنای فارسی نوِ «سریش» است که ابوالقاسمی آن را عیناً از برهان قاطع نقل کرده تا فرزندِ واژه را نشان دهد نه نیای آن را. این گیاه «اشراس/سریش» (Asphodelus) است و چسب از آردِ ریشهٔ خشک‌شدهٔ آن به دست می‌آید نه از صمغ. نورایی معنای فارسی را به جعبهٔ ایرانی باستان بازگردانده است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"FFD:60\", \"status\": \"partial\", \"note\": \"FFD_pages.txt pdf page 65 (= printed p.60), entry «سرشتن»: «سرشت < فارسی میانه srišt < ایرانی باستان *srišta-. … srišt صورت ضعیف ریشهٔ sraiš است و آن به معنی «چسباندن» است. سریش < فارسی میانه srēš < ایرانی باستان *sraiša-. … «(سریش)» به معنی «رستنی‌ای که … بعد از رسیدگی خشک کنند و آرد سازند و کفشگران و صحافان چیزها بدان چسبانند.» (برهان قاطع)، از ریشهٔ sraiš است.» Supports the two Old Iranian forms and the root meaning 'to stick', but the plant gloss is Borhan's New Persian definition, not Abolghasemi's Old Iranian one.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"CHEUNG\", \"where\": \"CHEUNG.txt line 23244 ff.\", \"stance\": \"supports\", \"note\": \"'*sraiš \\\"to put together, attach\\\"' as the Proto-Iranian root, with BMP sriš- and 'NP siristan/sirēs- \\\"to mix, mingle; knead\\\", NP sirism \\\"glue\\\"'.\"},\n            {\"src\": \"MON\", \"where\": \"Mo'in, MON_part1.txt line 77728, s.v. سریش\", \"stance\": \"supports\", \"note\": \"«سریش: (اِ.) (گیا.) گیاهی است از تیرهٔ سوسنی‌ها که دارای گل‌های زینتی است و چون دارای ساقهٔ زیرزمینی ضخیم لعابدار است، از کوبیدهٔ ریشهٔ آن به عنوان چسب استفاده می‌کنند … اشراس، اشراش.» — the glue comes from the pounded mucilaginous root, not from a resin.\"},\n            {\"src\": \"BRT\", \"where\": \"Bartholomae, BRT.txt\", \"stance\": \"silent\", \"note\": \"No Old Iranian *sraiš- headword recoverable from this scan's OCR (searched 'sriš', 'sraēš', 'sris-'); only the Nirangistan citation quoted at node 2.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Avestan\",\n          \"words\": \"srîš : to join, attach, glue\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"There is an Avestan verb of this shape, but only in a compound and only once: Younger Avestan ham.sriš- 'to put together', attested in the aorist subjunctive 3sg. ham.srišāiti at Nirangistan 99 (Cheung, s.v. *sraiš; Bartholomae's AiW quotes the same passage, '… hamsrisāiti hąm vā daŋhayeiti N. 99'). A bare Avestan srīš- 'to join, attach, glue' is not a lemma in Bartholomae or in Cheung's Liste, and the gloss 'glue' belongs to the Middle and New Persian nouns, not to the Avestan verb. Horn (no. 732) does write 'aw. √sraēš-, sraēšyeiti \\\"sich an etwas hängen\\\"' and Mo'in's Borhan footnote cites «اوستا sriš (چسبیدن)», so Nourai is repeating a form that his Persian and 19th-century sources do use; it is a normalised citation form rather than an attested Avestan word. Structurally, too, this box is a sister of the Middle Persian development, not its ancestor: MP srēš/srišt continue Old Iranian directly and cannot come 'through' Avestan.\",\n          \"derivation_fa\": \"فعلی با این صورت در اوستایی هست، اما تنها در ترکیب و تنها یک‌بار: اوستایی متأخر ham.sriš- «به هم پیوستن»، در صیغهٔ التزامی سوم‌شخص مفرد ham.srišāiti در نیرنگستان ۹۹ (چونگ ذیل *sraiš؛ بارتولمه هم همین عبارت را در فرهنگ ایرانی باستان می‌آورد). صورت سادهٔ «srīš» به معنی «پیوستن، چسباندن، چسب» مدخلی در بارتولمه یا فهرست چونگ نیست و معنای «چسب» از آنِ نام‌های فارسی میانه و نو است نه فعل اوستایی. با این حال هرن (بند ۷۳۲) می‌نویسد «اوستایی √sraēš-، sraēšyeiti \\\"به چیزی آویختن\\\"» و حاشیهٔ معین بر برهان نیز «اوستا sriš (چسبیدن)» دارد؛ پس نورایی صورتی هنجارشده را از منابع فارسی و سدهٔ نوزدهمی خود نقل کرده است. از نظر ساختاری هم این جعبه خواهرِ تحول فارسی میانه است نه نیای آن: srēš/srišt مستقیماً دنبالهٔ ایرانی باستان‌اند. پس با احتیاط پذیرفتنی است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"BQT:1136\", \"status\": \"partial\", \"note\": \"Borhan-e Qate' ed. Mo'in, vol. 2 (BQT_v2_pages.txt): the Latin-script footnote that carries the Avestan citation stands on leaf 586 (printed p.1124, the سرشت page), where Mo'in writes «سانسکریت śliṣ (آویزان بودن، چسبیدن)، اوستا sriš (چسبیدن)، فارسی: سریش». The page Nourai cites, 1136, is the سریش headword itself (leaf 598: «سریش: بکسر اول و ثانی … رستنیی باشد که …»), which describes the plant but carries no Avestan form. So the Avestan srīš is in Borhan, three columns earlier than the cited page.\"},\n            {\"ref\": \"FFD:60\", \"status\": \"partial\", \"note\": \"FFD p.60 (pdf 65) reconstructs the root as Old Iranian *sraiš and never invokes Avestan; Abolghasemi's chain is *sraiš > MP srišt/srēš > NP, with no Avestan step.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"Bartholomae, AiW; BRT.txt line 16991\", \"stance\": \"partial\", \"note\": \"The scan preserves the citation '… yō °ma *aiwahmat naēmat hamsrisāiti hąm vā daŋhayeiti N. 99 …' — Bartholomae records the compound ham.sriš- (Nirangistan 99); the simplex is not separately lemmatised in what the OCR yields.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"CHEUNG.txt lines 23244-23250\", \"stance\": \"partial\", \"note\": \"'*AVESTAN: (+ *ham-) YAv. ham.sriš- \\\"to put together\\\" — Liste: 66. Aor. them. (s- ?): SUBJ. 3sg. YAv. ham.srišāiti (N 99)' — the only Avestan attestation, and only with the preverb ham-.\"},\n            {\"src\": \"HRN\", \"where\": \"Horn, Grundriss p.162 no.732 (HRN.txt leaf 183)\", \"stance\": \"supports\", \"note\": \"'732. siristen \\\"mischen, vermengen; schaffen, bilden\\\", siriš (*sirēš), sirišem \\\"Leim\\\". aw. √sraēš-, sraēšyeiti \\\"sich an etwas hängen\\\"; phlv. sristan, srešt (PPGl); ai. skr. √śreṣ- (śleṣ-), śliṣyati \\\"verbinden, zusammenfügen\\\".' Horn does cite an Avestan √sraēš-.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"sriš : glue\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Middle Persian has the verb srištan, present stem srēš- (Book Pahlavi <slštn'>, <slyš->) 'to mix, knead', and the noun srēš 'glue' (Abolghasemi's *sraiša- > MP srēš > NP سریش). MacKenzie's Concise Pahlavi Dictionary prints 'srištan, *srēš- [slštn' | P sryš-, N sir-] mix, knead', and Cheung 'BMP slš- /sriš-/ \\\"to mix, knead\\\"'. So the shape Nourai gives, 'sriš', is the present stem of the verb (or Cheung's reading of it) while the gloss he attaches, 'glue', belongs to the noun srēš; the two are separated by the ē/i of full versus zero grade. The Pahlavi step itself is entirely real — the node is right in substance, imprecise in form. Note again that this box continues Old Iranian directly, not the Avestan box drawn above it.\",\n          \"derivation_fa\": \"فارسی میانه فعلِ srištan با ستاک مضارع srēš- (پهلوی کتابی <slštn'>, <slyš->) به معنی «آمیختن، خمیر کردن» دارد و نامِ srēš «چسب» (ابوالقاسمی: ایرانی باستان *sraiša- ← فارسی میانه srēš ← «سریش»). مکنزی در فرهنگ کوچک پهلوی می‌آورد: «srištan, *srēš- [slštn' | P sryš-, N sir-] آمیختن، خمیر کردن» و چونگ: «BMP slš- /sriš-/ آمیختن، خمیر کردن». پس صورتی که نورایی می‌دهد (sriš) ستاک مضارع فعل است، حال آنکه معنایی که به آن بسته («چسب») از آنِ نامِ srēš است؛ این دو در درجهٔ آوایی (ē در برابر i) از هم جدا می‌شوند. خودِ حلقهٔ پهلوی کاملاً درست است؛ ایراد تنها در دقتِ صورت و معناست. باز هم یادآور می‌شویم که این جعبه مستقیماً دنبالهٔ ایرانی باستان است نه اوستایی.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"FFD:60\", \"status\": \"partial\", \"note\": \"FFD_pages.txt pdf 65 (p.60): «سرشت < فارسی میانه srišt …» and «سریش < فارسی میانه srēš …». Abolghasemi's Middle Persian forms are srišt (past stem) and srēš (the noun/present stem); he does not print a Pahlavi 'sriš : glue', so Nourai's box mixes the two.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie, PHD.txt line 568 (s.v. srištan) and PHD_mackenzie.txt line 4642\", \"stance\": \"partial\", \"note\": \"'srištan, *srēš- [slštn' | P sryš-, N sir-] mix, knead'; the English-Pahlavi index (line 2532) gives 'knead srištan' and (line 2830) 'mix … srištan'. MacKenzie has the verb but no noun 'glue'.\"},\n            {\"src\": \"NYB\", \"where\": \"Nyberg, NYB_vol2_glossary.txt (searched 'srištan', 'srēš', 'sriš')\", \"stance\": \"silent\", \"note\": \"Nyberg's glossary has srišk 'drop' (line 3510, 'Av. sraska- \\\"tear\\\"; NP sirišk') and srišvātak 'a third', but no srištan/srēš — the verb does not occur in the texts he glosses.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"CHEUNG.txt line 23250\", \"stance\": \"supports\", \"note\": \"'*MIDDLE PERSIAN: BMP slš- /sriš-/ \\\"to mix, knead\\\"' — Cheung's transliteration is exactly Nourai's 'sriš', with the sense 'mix, knead' rather than 'glue'.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Persian\",\n          \"words\": \"serîš «سیریش» : glue\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"NP سریش serīš/sirīš (Nourai spells it سیریش, with the doublets سیرش and سریشم serīšom) 'glue; the asphodel plant from whose pounded root the glue is made' continues Middle Persian srēš, from Old Iranian *sraiša-, an -a- stem of the root *sraiš- 'to stick'; the Middle Persian ē regularly becomes ī in New Persian, and the initial cluster sr- is broken by the prothetic/anaptyctic vowel (sr- > sir-/ser-) exactly as in سرشک < srišk. The variant سریشم has the -m of MP -ōm/-am (Cheung: 'NP sirism \\\"glue\\\"'), and the plant is Asphodelus, also called اشراس/اشراش in Persian. Wiktionary's Sanskrit article names Persian سِریشُم as the cognate of śliṣ-. The node is right in form, meaning and route.\",\n          \"derivation_fa\": \"«سریش/سیریش» فارسی نو، با گونه‌های «سیرش» و «سریشم»، هم به معنی چسب است و هم نام گیاهی (اشراس، Asphodelus) که از آردِ ریشهٔ خشکش چسب می‌سازند. این واژه دنبالهٔ فارسی میانهٔ srēš است و آن از ایرانی باستان *sraiša-، ستاکی نامی از ریشهٔ *sraiš «چسباندن». ای کشیدهٔ فارسی میانه در فارسی نو به ی بدل شده و خوشهٔ آغازین sr- با واکهٔ میانجی شکسته شده (sr- ← sir-/ser-)، درست مانند «سرشک» از srišk. گونهٔ «سریشم» پسوندِ -m فارسی میانه را دارد (چونگ: NP sirism «چسب»). ویکی‌واژه نیز در مدخل سنسکریتِ श्लिष् «سِریشُم» فارسی را هم‌ریشهٔ آن می‌شمارد. ادعای نورایی در صورت، معنا و مسیر درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%E0%A4%B6%E0%A5%8D%E0%A4%B2%E0%A4%BF%E0%A4%B7%E0%A5%8D\"],\n          \"ref_check\": [\n            {\"ref\": \"BQT:1136\", \"status\": \"supports\", \"note\": \"Borhan-e Qate', vol. 2, printed p.1136 = BQT_v2_pages.txt leaf 598 (the leaf-to-page offset is +538, fixed by the two Nourai citations: leaf 586 = p.1124 سرشت, leaf 598 = p.1136 سریش). The entry: «سریش: بکسر اول و ثانی و سکون ثالث و شین قرشت … رستنیی باشد که … بعد از رسیدگی خشک کنند و آرد سازند و کفشگران و صحافان بدان چیزها چسبانند».\"},\n            {\"ref\": \"FFD:60\", \"status\": \"supports\", \"note\": \"FFD pdf 65 (p.60): «سریش < فارسی میانه srēš < ایرانی باستان *sraiša-. … از ریشهٔ sraiš است.»\"},\n            {\"ref\": \"MON:1867,1880\", \"status\": \"not_checked\", \"note\": \"The 6-volume Mo'in Nourai paginates is not on disk (only the 2-volume Adena abridgement, without page mapping). The content is confirmed there at MON_part1.txt line 77728: «سریش: … گیاهی است از تیرهٔ سوسنی‌ها … از کوبیدهٔ ریشهٔ آن به عنوان چسب استفاده می‌کنند؛ اشراس، اشراش».\"},\n            {\"ref\": \"IEC:1637\", \"status\": \"not_checked\", \"note\": \"Beyond the last leaf of the available Mann scan (see the entry-level ref_check).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HRN\", \"where\": \"Horn p.162 no.732 (HRN.txt leaf 183)\", \"stance\": \"supports\", \"note\": \"'siriš (*sirēš), sirišem \\\"Leim\\\"' listed with siristen; 'phlv. sristan, srešt'.\"},\n            {\"src\": \"HUB\", \"where\": \"Hübschmann p.75 no.732 (HUB.txt leaf 85)\", \"stance\": \"supports\", \"note\": \"'2) skr. śliṣ \\\"anhangen, haften, kleben\\\", zd. riš \\\"haften\\\", np. siriš \\\"Leim\\\"' — and he cites the Afghan loan 'sriš \\\"glue, birdlime, stickiness\\\"'.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"CHEUNG.txt line 23260 ff.\", \"stance\": \"supports\", \"note\": \"'*NWIR: NP siristan/sirēs- \\\"to mix, mingle; knead\\\", Gz. siris-/sirist \\\"to knead the dough\\\", NP sirism \\\"glue\\\".'\"},\n            {\"src\": \"MON\", \"where\": \"MON_part1.txt line 77728\", \"stance\": \"supports\", \"note\": \"«سریش … از کوبیدهٔ ریشهٔ آن به عنوان چسب استفاده می‌کنند».\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Avestan\",\n          \"words\": \"sraěš : mixture, nature\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The Avestan form as such is Horn's citation form: Grundriss p.162 no.732 gives 'aw. √sraēš-, sraēšyeiti \\\"sich an etwas hängen\\\"' as the antecedent of NP siristan/sirišt, and Hübschmann p.75 comments on precisely that entry. So the reference is accurately used. Two things are nevertheless not Avestan: the gloss and the split. 'Mixture, nature' is the meaning of the New Persian noun سرشت, not of any Avestan word — Avestan attests only ham.sriš- 'to put together' (N 99). And the reason Nourai draws two separate Avestan boxes is Hübschmann's semantic sorting of the SANSKRIT evidence (§732: '1) skr. śrī \\\"verbinden, zusammenfügen\\\" … np. sirišt \\\"Mischung, Natur, Anlage\\\"; 2) skr. śliṣ \\\"anhangen, haften, kleben\\\" … np. siriš \\\"Leim\\\"'), not two attested Avestan lemmas. Modern work (Cheung, Abolghasemi) treats سرشت and سریش as two derivatives — zero-grade *srišta- and full-grade *sraiša- — of one and the same root, which is the better analysis.\",\n          \"derivation_fa\": \"صورت اوستاییِ این جعبه از هرن گرفته شده است: در «مبانی ریشه‌شناسی فارسی نو» ص ۱۶۲ بند ۷۳۲ می‌خوانیم «اوستایی √sraēš-, sraēšyeiti \\\"به چیزی آویختن\\\"» به عنوان نیای فارسیِ siristan/sirišt، و هوبشمان در ص ۷۵ بر همین بند حاشیه زده است؛ پس ارجاع درست به کار رفته. اما دو چیز اوستایی نیست: معنا و دوشاخه‌کردن. «آمیزه، سرشت» معنای نامِ فارسی نوِ «سرشت» است نه هیچ واژهٔ اوستایی؛ در اوستا تنها ham.sriš- «به هم پیوستن» (نیرنگستان ۹۹) گواهی شده است. و سببِ اینکه نورایی دو جعبهٔ اوستاییِ جداگانه کشیده، تقسیم‌بندی معناییِ هوبشمان از شواهد سنسکریت است (بند ۷۳۲: «۱) śrī \\\"پیوستن، آمیختن\\\" … فارسی sirišt \\\"آمیزه، سرشت، نهاد\\\"؛ ۲) śliṣ \\\"چسبیدن\\\" … فارسی siriš \\\"چسب\\\"»)، نه وجود دو مدخل اوستایی. پژوهش امروزی (چونگ، ابوالقاسمی) «سرشت» و «سریش» را دو مشتقِ یک ریشه می‌داند: *srišta- با درجهٔ صفر و *sraiša- با درجهٔ کامل — و همین تحلیل درست‌تر است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"HRN:162\", \"status\": \"supports\", \"note\": \"HRN.txt leaf 183 (printed p.162), no. 732: 'siristen \\\"mischen, vermengen; schaffen, bilden\\\", siriš (*sirēš), sirišem \\\"Leim\\\". aw. √sraēš-, sraēšyeiti \\\"sich an etwas hängen\\\"; phlv. sristan, srešt (PPGl); ai. skr. √śreṣ- (śleṣ-), śliṣyati \\\"verbinden, zusammenfügen\\\".' Horn does print aw. sraēš-, though he glosses it 'to hang on to something', not 'mixture, nature'.\"},\n            {\"ref\": \"HUB:75\", \"status\": \"supports\", \"note\": \"HUB.txt leaf 85 (printed p.75), no. 732: 'Vgl. afgh. LW. sariš, sirišt \\\"nature, temperament\\\", sriš \\\"glue, birdlime, stickiness, adhesiveness\\\" … Der Bedeutung nach schliessen sich näher zusammen 1) skr. śrī \\\"verbinden, zusammenfügen\\\", vgl. skr. śri \\\"mengen, mischen\\\", np. siristan \\\"mischen\\\", sirišt \\\"Mischung, Natur, Anlage\\\" (vgl. amēziš \\\"Mischung\\\" = \\\"Temperament\\\"); 2) skr. śliṣ \\\"anhangen, haften, kleben\\\", zd. riš \\\"haften\\\", np. siriš \\\"Leim\\\".' This is the source of Nourai's two-branch layout and of the gloss 'mixture, nature'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"CHEUNG\", \"where\": \"CHEUNG.txt lines 23244-23250\", \"stance\": \"contradicts\", \"note\": \"Cheung lemmatises one root *sraiš 'to put together, attach' with a single Avestan attestation, ham.sriš- (N 99); there is no Avestan *sraēš- 'mixture, nature' and no reason to split the family in two.\"},\n            {\"src\": \"BRT\", \"where\": \"Bartholomae, BRT.txt (searched 'sraēš', 'sriš')\", \"stance\": \"silent\", \"note\": \"No lemma sraēš- recoverable from this OCR; only the ham.srišāiti citation at line 16991.\"},\n            {\"src\": \"FFD\", \"where\": \"Abolghasemi p.60 (FFD_pages.txt pdf 65)\", \"stance\": \"contradicts\", \"note\": \"Abolghasemi derives both سرشت and سریش from the one Old Iranian root sraiš (weak grade *srišta-, full grade *sraiša-) and posits no Avestan intermediary at all.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Persian\",\n          \"words\": \"serešt «سرشت» : nature; sereštan «سرشتن» : to mix\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"NP سرشتن sereštan (present stem سرش- sereš-) 'to knead, mix, mould, create' and its past-participle-turned-noun سرشت serešt 'what has been kneaded/moulded > constitution, nature, temperament' continue Middle Persian srištan / srēš- 'to mix, knead' (MacKenzie), from Old Iranian *srišta-, the zero grade of *sraiš-; the initial cluster sr- again takes a prothetic vowel (sr- > ser-). The semantic path 'knead, mould (clay)' > 'that which was moulded' > 'inborn nature' is the same one Persian takes with طینت/سرشت and Latin fingere > figura; Hübschmann puts it neatly, sirišt 'Mischung, Natur, Anlage' beside āmēziš 'Mischung' = 'Temperament'. The Hafez couplet printed in the box («عیب رندان مکن ای زاهد پاکیزه سرشت / که گناه دگران بر تو نخواهند نوشت») uses the noun in exactly this sense. Both words, both glosses and the derivation are correct.\",\n          \"derivation_fa\": \"«سرشتن» (ستاک مضارع «سرش-») به معنی «خمیر کردن، آمیختن، شکل دادن، آفریدن» و اسم‌شدهٔ صفت مفعولی آن «سرشت» به معنی «آنچه سرشته شده ← نهاد، طبیعت، خوی» دنبالهٔ فارسی میانهٔ srištan / srēš- «آمیختن، خمیر کردن» (مکنزی) است، و آن از ایرانی باستان *srišta-، صورت ضعیفِ ریشهٔ *sraiš. خوشهٔ آغازین sr- باز با واکهٔ میانجی شکسته شده است (sr- ← ser-). تحول معنایی «خمیر کردن (گِل)» ← «آنچه سرشته شده» ← «نهاد ذاتی» همان راهی است که «طینت» عربی و figura لاتینی (از fingere) رفته‌اند؛ هوبشمان همین را می‌گوید و سرشت را در کنار «آمیزش = مزاج» می‌نشاند. بیت حافظ که در همان جعبه چاپ شده («عیب رندان مکن ای زاهد پاکیزه‌سرشت / که گناه دگران بر تو نخواهند نوشت») واژه را دقیقاً در همین معنا به کار برده است. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D8%B3%D8%B1%D8%B4%D8%AA\"],\n          \"ref_check\": [\n            {\"ref\": \"BQT:1124\", \"status\": \"supports\", \"note\": \"Borhan-e Qate' ed. Mo'in, vol. 2, printed p.1124 = BQT_v2_pages.txt leaf 586. Headword: «سرشت: بکسر اول و ثانی بر وزن بهشت، خلقت و طینت و نهاد و طبع و طبیعت و خوی آدمی را گویند — و بمعنی مخلوط و آغشته کردن هم هست». Mo'in's Latin-script footnote on the same leaf: «سانسکریت śliṣ (آویزان بودن، چسبیدن)، اوستا sriš (چسبیدن)، فارسی: سریش … سانسکریت śri (آمیختن، مخلوط کردن)، فارسی: سرشتن … پهلوی [srištan] [رک: سرشت] … هوبشمان ۲۷۷/۳۳۷».\"},\n            {\"ref\": \"HRN:162\", \"status\": \"supports\", \"note\": \"HRN.txt leaf 183, no. 732: 'siristen \\\"mischen, vermengen; schaffen, bilden\\\" … phlv. sristan, srešt' — Horn's entry is precisely NP sereštan with its Pahlavi antecedent.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie, PHD.txt line 568\", \"stance\": \"supports\", \"note\": \"'srištan, *srēš- [slštn' | P sryš-, N sir-] mix, knead' — the '| N sir-' cross-reference is to the New Persian verb.\"},\n            {\"src\": \"HUB\", \"where\": \"Hübschmann p.75 no.732\", \"stance\": \"supports\", \"note\": \"'np. siristan \\\"mischen\\\", sirišt \\\"Mischung, Natur, Anlage\\\" (vgl. amēziš \\\"Mischung\\\" = \\\"Temperament\\\")' — the semantic bridge from 'mixture' to 'nature' spelled out.\"},\n            {\"src\": \"MON\", \"where\": \"MON_part1.txt line 77040\", \"stance\": \"supports\", \"note\": \"«سرشت: (اِ.) فطرت، طینت، نهاد، خوی» (and line 3576 «سرشتن …»).\"},\n            {\"src\": \"CHEUNG\", \"where\": \"CHEUNG.txt line 23260\", \"stance\": \"supports\", \"note\": \"'NP siristan/sirēs- \\\"to mix, mingle; knead\\\"' under *sraiš.\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"Sanskrit\",\n          \"words\": \"slisyâmî : adhere; črî : bind, mix\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Both forms are real Sanskrit. श्लिष्यामि śliṣyāmi is the 1sg. present of श्लिष् śliṣ (class 4, śliṣyati) 'to adhere, cling, stick to, embrace' (RV+), the Indic match of Iranian *sraiš- and, with the variant श्रेष्/श्रिष् śreṣ/śriṣ, the form Cheung cites from EWAia II 670. Nourai's second form 'črî' is his transcription — taken over from Mo'in's Persian-script footnote, where it is written śri — of श्री/श्रि śrī 'to mix, to cook (a mixture), to blend', the root of śrītá- 'mixed'; the č merely stands for the palatal sibilant ś, which he elsewhere writes š. The two are exactly the pair Hübschmann sets side by side at Persische Studien p.75 (śrī 'verbinden, zusammenfügen' / śri 'mengen, mischen' vs śliṣ 'anhangen, haften, kleben') and the pair Mo'in reproduces in his Borhan footnote. Wiktionary derives śliṣ from Proto-Indo-Iranian *ćRayš 'to adhere, attach' and names Persian سریشم as its cognate — the very link the chart draws.\",\n          \"derivation_fa\": \"هر دو صورت سنسکریتِ واقعی‌اند. श्लिष्यामि (śliṣyāmi) اول‌شخص مفرد مضارعِ ریشهٔ श्लिष् (śliṣ، گروه چهارم، śliṣyati) «چسبیدن، آویختن، در آغوش گرفتن» است که از ریگ‌ودا به بعد گواهی دارد و همتای هندیِ *sraiš ایرانی است؛ چونگ آن را با گونهٔ श्रेष् (śreṣ) از مایرهوفر (EWAia II: 670) نقل می‌کند. صورت دومِ نورایی، «črî»، آوانگاری اوست — برگرفته از حاشیهٔ معین بر برهان که آن را śri می‌نویسد — از श्री/श्रि (śrī) «آمیختن، مخلوط کردن»، ریشهٔ śrītá- «آمیخته»؛ حرف č در نویسه‌گردانی او همان سایشیِ کامیِ ś است. این دو دقیقاً همان جفتی‌اند که هوبشمان در «مطالعات فارسی» ص ۷۵ رودرروی هم می‌گذارد و معین در حاشیهٔ برهان بازمی‌آورد. ویکی‌واژه śliṣ را از هندوایرانی آغازینِ *ćRayš «چسبیدن» می‌گیرد و «سریشم» فارسی را هم‌ریشهٔ آن می‌شمارد — همان پیوندی که نمودار می‌کشد. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%E0%A4%B6%E0%A5%8D%E0%A4%B2%E0%A4%BF%E0%A4%B7%E0%A5%8D\"],\n          \"ref_check\": [\n            {\"ref\": \"BQT:1134\", \"status\": \"partial\", \"note\": \"The Sanskrit forms Nourai reproduces are in Mo'in's footnote, but on printed p.1124 (BQT_v2_pages.txt leaf 586, the سرشت page), not on p.1134: «… سانسکریت śliṣ (آویزان بودن، چسبیدن)، اوستا sriš (چسبیدن)، فارسی: سریش … سانسکریت śri (آمیختن، مخلوط کردن)، فارسی: سرشتن …». Leaf 596 (= p.1134 on the +538 offset fixed by Nourai's own two other citations) carries the entries سروش/سرون/سره and no Sanskrit at all. Most likely a digit slip in the book for 1124.\"},\n            {\"ref\": \"IEC:1637\", \"status\": \"not_checked\", \"note\": \"Beyond the last leaf of the Mann scan on disk (see the entry-level ref_check).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HUB\", \"where\": \"Hübschmann p.75 no.732 (HUB.txt leaf 85)\", \"stance\": \"supports\", \"note\": \"'1) skr. śrī \\\"verbinden, zusammenfügen\\\", vgl. skr. śri \\\"mengen, mischen\\\" … 2) skr. śliṣ \\\"anhangen, haften, kleben\\\"' — both Sanskrit roots, with both of Nourai's glosses.\"},\n            {\"src\": \"HRN\", \"where\": \"Horn p.162 no.732\", \"stance\": \"supports\", \"note\": \"'ai. skr. √śreṣ- (śleṣ-), śliṣyati \\\"verbinden, zusammenfügen\\\"' — the present śliṣyati, of which Nourai's slisyâmî is the 1sg.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"CHEUNG.txt line 23262\", \"stance\": \"supports\", \"note\": \"'*SANSKRIT: śreṣ \\\"to cling, stick, be attached, hold\\\" (RV) = EWAia II: 670.'\"},\n            {\"src\": \"IEC\", \"where\": \"Mann, IEC.txt line 7351\", \"stance\": \"silent\", \"note\": \"The only kli- lemma reachable in the scan is 'kliḱō, io (?) \\\"squeeze, twist\\\" … Skt. kliśyāmi \\\"torture, force\\\"' — a different Sanskrit verb (kliś-), not śliṣ-.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\n"
}
```


### [2026-09-06T21:14:53.232Z] TOOL RESULT

```
File created successfully at: /home/sfmqrb/git/rishe/data/verification/page-271.json (file state is current in your context — no need to Read it back)
```


## [2026-09-06T21:14:57.469Z] TOOL CALL #70: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-271.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 271"
}
```


### [2026-09-06T21:15:01.225Z] TOOL RESULT

```
JSON OK
nodes verified: 16/16
node verdicts: {'transcription_suspect': 1, 'confirmed': 9, 'plausible': 6}
root verdicts: {'confirmed': 1, 'plausible': 1}
ref checks: {'supports': 11, 'not_checked': 8, 'partial': 6}
books consulted: {'supports': 34, 'partial': 7, 'silent': 9, 'contradicts': 2} | by book: {'CHEUNG': 7, 'KLN': 6, 'MON': 5, 'HRN': 4, 'POK': 3, 'PHD': 3, 'BRT': 3, 'HUB': 3, 'IEC': 2, 'AFA': 2, 'AHD': 2, 'SKT': 2, 'FVQ': 1, 'ARB': 1, 'TAD': 1, 'AFM': 1, 'BQT': 1, 'RCH': 1, 'WLD': 1, 'LAT': 1, 'NYB': 1, 'FFD': 1}
```


## [2026-09-06T21:15:08.925Z] TOOL CALL #71: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/page-271.json'))\nurls=set()\ndef walk(o):\n    if isinstance(o,dict):\n        for k,v in o.items():\n            if k=='sources': urls.update(v)\n            else: walk(v)\n    elif isinstance(o,list):\n        for x in o: walk(x)\nwalk(d)\nidx={json.loads(l)['url'] for l in open('data/verification/sources/web/index.jsonl')}\nfor u in sorted(urls): print(('OK ' if u in idx else 'MISSING '), u)\n\""
}
```


### [2026-09-06T21:15:11.065Z] TOOL RESULT

```
OK  https://en.wiktionary.org/wiki/%CE%BA%CE%BB%CE%B5%CE%AF%CF%82
OK  https://en.wiktionary.org/wiki/%D8%A5%D9%82%D9%84%D9%8A%D8%AF
OK  https://en.wiktionary.org/wiki/%D8%B3%D8%B1%D8%B4%D8%AA
OK  https://en.wiktionary.org/wiki/%D9%85%D9%82%D9%84%D8%A7%D8%AF
OK  https://en.wiktionary.org/wiki/%DA%A9%D9%84%DB%8C%D8%AF
OK  https://en.wiktionary.org/wiki/%E0%A4%B6%E0%A5%8D%E0%A4%B2%E0%A4%BF%E0%A4%B7%E0%A5%8D
OK  https://www.etymonline.com/word/close
OK  https://www.etymonline.com/word/lot
```


## [2026-09-06T21:15:31.336Z] AGENT

Done. `python3 tools/verify_check.py 271` → 16/16 nodes, **0 PROBLEM lines**.

**Page 271 (book p. 241) — 2 entries, 16 nodes**
- Node verdicts: 9 confirmed, 6 plausible, 1 transcription_suspect. Root verdicts: 1 confirmed (Klěu 2/Klâu), 1 plausible (Klis).
- Ref checks: 11 supports, 6 partial, 8 not_checked. 22 books consulted (Pokorny, Walde‑Pokorny p.492, Watkins/AHD, Buck, Klein, Skeat, Ernout‑Meillet, Jeffery, Fraenkel, al‑Jawālīqī, al‑ʿUnaysī, Bartholomae, MacKenzie, Nyberg, Cheung, Horn, Hübschmann, Abolghasemi, Borhan‑e Qateʿ vols 2–3, Moʿin, Mann).

**transcription_suspect (1)**
- Klěu 2 #1 Greek `kleiss` — no such Greek word; the printed page really shows "kleidos, kleiss" (page PNG saved to `data/verification/sources/refs/ocr/BOOK/271.png`), so `error_in: "book"` — Nourai's misprint for κλείς *kleis*. Extraction is faithful; **no data fix needed**.

**disputed:** none. Notable "plausible" calls:
- Root **Klis "adhere"** — Cheung s.v. *sraiš: "This Ir. root has no certain IE cognates"; Wiktionary/EWAia reconstruct only PIIr. *ćraiš‑. No IE dictionary has a root *klis‑; Pokorny has none.
- Entry 1's chain Old Iranian → Avestan → Pahlavi → Persian is a sister, not an ancestor line; Avestan attests only *ham.sriš‑* (Nirangistan 99). The two Avestan boxes come from Hübschmann's split of the *Sanskrit* evidence (śrī vs śliṣ), not from two Avestan lemmas.
- Aramaic box (#3) is a Greek loan, not an IE descendant; Germanic *hluta* is flagged "possibly / semantics obscure" by both AHD and Klein.
- The chart's NOTE (FVF: eqlīd from Persian kelīd) is settled in the chart's favour: Jeffery p.267‑8 rejects Dvořák's direct‑Persian route for the Syriac ʾaqlīdā one, as does Wiktionary/Fraenkel.

**Reference issues for the owner (in the JSON, not data errors)**
- `BQT:1134` (Sanskrit node) — the Sanskrit śliṣ/śri footnote is on printed p.**1124**, not 1134; likely a digit slip. `BQT:1136` (سریش) and `BQT:1124` (سرشت) both land exactly (v2 leaf→page offset +538); `BQT:1687` (کلید, with Moʿin's Greek footnote) lands exactly in v3.
- `IEC:1637` unverifiable: the archive.org Mann scan on disk stops at p.1554. `ARK:236` (Arkan‑e Sokhan) and `MON:4283 / MON:1867,1880` not checkable (books not digitised / only the 2‑vol abridgement on disk).
