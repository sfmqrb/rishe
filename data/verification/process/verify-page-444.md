# Verification process log — verify-page-444


## [2026-09-14T01:55:54.085Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 444 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-444.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-444.json. Write /home/sfmqrb/git/rishe/data/verification/page-444.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 444` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T01:55:55.671Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T01:55:56.443Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T01:55:56.458Z] TOOL RESULT

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


## [2026-09-14T01:55:56.609Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-444.txt"
}
```


### [2026-09-14T01:55:56.633Z] TOOL RESULT

```
1	=== PDF page 444 (book page 414) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Sen 2, Seni : apart, separated, without  (refs POK:907)
4	#1 (parent #0) [Avestan] refs=POK:907 | hanare : without
5	#2 (parent #0) [Sanskrit] refs=POK:907 | sanu-tar : apart from
6	#3 (parent #0) [Latin] refs=POK:907 | sine : without ; sincěrus : not affected, pure
7	  #4 (parent #3) [English] refs=KLN:1447 | sans : without ; sans serif ; sincere
8	--- entry 1 ---
9	ROOT Seni -> redirect to Sen 2
10	--- entry 2 ---
11	ROOT Seno -> redirect to Sen 1
12	--- entry 3 ---
13	ROOT [Indo-European] Septm : seven  (refs POK:909)
14	#1 (parent #0) [Avestan / Old Persian] refs=POK:909; KLN:1426; GPL:41 | hapta : seven ; hapta-dasa : seventeen ☞Dekm ; haptâiti : seventy
15	  #2 (parent #1) [Persian] refs=BQT:2341 | haft «هفت ( هفته ، هفده ، هفتاد )» : seven
16	#3 (parent #0) [Germanic] refs=AHD | sibum : seven
17	  #4 (parent #3) [English] refs=None | seven, seventeen, seventy
18	#5 (parent #0) [Latin] refs=AHD | septem : seven
19	  #6 (parent #5) [English] refs=None | September
20	--- entry 4 ---
21	ROOT [Indo-European] Ser 1 : to flow  (refs POK:909)  PART 1
22	#1 (parent #0) [Avestan / Old Persian] refs=POK:909 | hareva, haraiva : name of a river in Afghanistan
23	  #2 (parent #1) [Persian] refs=None | harât «هرات» : "the flowing"
24	#3 (parent #0) [Latin] refs=AHD | serum : liquid from animal tissue
25	  #4 (parent #3) [French] refs=None | 
26	    #5 (parent #4) [Persian] refs=MON | serom «سیروم» : liquid from animal tissue
27	  #6 (parent #3) [English] refs=AHD | serum
28	
```


## [2026-09-14T01:56:00.010Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-444.json",
 "description": "Read source JSON page 444"
}
```


### [2026-09-14T01:56:00.056Z] TOOL RESULT

```
{
  "pdf_page": 444,
  "book_page": 414,
  "entries": [
    {
      "root": {
        "name": "Sen 2, Seni",
        "lang": "Indo-European",
        "refs": "POK:907",
        "gloss": "apart, separated, without"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:907",
          "words": [
            {"translit": "hanare", "gloss": "without", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "POK:907",
          "words": [
            {"translit": "sanu-tar", "gloss": "apart from", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Latin",
          "refs": "POK:907",
          "words": [
            {"translit": "sine", "gloss": "without", "script": null},
            {"translit": "sincěrus", "gloss": "not affected, pure", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "English",
          "refs": "KLN:1447",
          "words": [
            {"translit": "sans", "gloss": "without", "script": null},
            {"translit": "sans serif", "gloss": null, "script": null},
            {"translit": "sincere", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Seni",
        "redirect": "Sen 2"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Seno",
        "redirect": "Sen 1"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Septm",
        "lang": "Indo-European",
        "refs": "POK:909",
        "gloss": "seven"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "POK:909; KLN:1426; GPL:41",
          "words": [
            {"translit": "hapta", "gloss": "seven", "script": null},
            {"translit": "hapta-dasa", "gloss": "seventeen", "script": null, "see": ["Dekm"]},
            {"translit": "haptâiti", "gloss": "seventy", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:2341",
          "words": [
            {"translit": "haft", "gloss": "seven", "script": "هفت ( هفته ، هفده ، هفتاد )"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "sibum", "gloss": "seven", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "seven, seventeen, seventy", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "septem", "gloss": "seven", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "September", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Ser 1",
        "lang": "Indo-European",
        "refs": "POK:909",
        "gloss": "to flow"
      },
      "part": 1,
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "POK:909",
          "words": [
            {"translit": "hareva, haraiva", "gloss": "name of a river in Afghanistan", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": null,
          "words": [
            {"translit": "harât", "gloss": "\"the flowing\"", "script": "هرات"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "serum", "gloss": "liquid from animal tissue", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "French",
          "refs": null,
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Persian",
          "refs": "MON",
          "words": [
            {"translit": "serom", "gloss": "liquid from animal tissue", "script": "سیروم"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 3,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "serum", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
```


## [2026-09-14T01:56:00.705Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-14T01:56:00.755Z] TOOL RESULT

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


## [2026-09-14T01:56:05.163Z] TOOL CALL #5: Bash

```json
{
 "command": "sed -n '1,60p' tools/verify_check.py && echo ---- && python3 -c \"\nimport json;d=json.load(open('data/verification/page-385.json'));print(json.dumps(d['entries'][0],ensure_ascii=False,indent=1)[:3000])\"",
 "description": "Inspect checker and an example output"
}
```


### [2026-09-14T01:56:06.454Z] TOOL RESULT

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
----
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
   "w
```


## [2026-09-14T01:56:07.072Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json;d=json.load(open('refs_online.json'))\nfor k in ['POK','KLN','AHD','BQT','MON','GPL','BRT','KNT','PHD','HRN','HUB']:\n    print(k, json.dumps(d.get(k),ensure_ascii=False)[:600]);print()\n\"",
 "description": "Check refs_online entries"
}
```


### [2026-09-14T01:56:08.305Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

GPL {"title": "J. T. Platts & G. S. A. Ranking, A Grammar of the Persian Language, Part I: Accidence, Oxford 1911", "edition_found": "1911", "kind": "archive_djvu", "url": "https://archive.org/details/grammarofpersian0000plat", "identifier": "grammarofpersian0000plat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/GPL.txt", "page_offset": "leaf = printed + 12 (e.g. leaf 17 = p.5). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Grammar organised by n

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1

KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol
```


## [2026-09-14T01:56:12.594Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json;d=json.load(open('refs_online.json'))\nprint(d['POK']['page_offset']); print(d['POK'].get('lookup_hint'))\nprint('KLN:',d['KLN']['page_offset'], d['KLN'].get('lookup_hint'))\nprint('AHD:',d['AHD'].get('page_offset'), d['AHD'].get('lookup_hint'))\nprint('BQT:',d['BQT'].get('page_offset'), d['BQT'].get('lookup_hint'), d['BQT'].get('scans'))\n\"",
 "description": "Get page offsets"
}
```


### [2026-09-14T01:56:13.679Z] TOOL RESULT

```
POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\data\ie\pokorny&root=config
KLN: KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
AHD: 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page. Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves = original 1969 ed.).
BQT: vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...'). grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor) [{'volume': '3', 'file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', 'first_printed': 1208, 'last_printed': 1925, 'pdf_offset': -1205, 'page_map': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pagemap.json', 'lang': 'fas', 'ocr_text': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', 'ocr_note': '689/721 pdf pages OCRed (tesseract fas+eng, mediocre); pages are separated by form-feeds and tagged [pdf page N]; remaining pages via tools/ref_page.py'}, {'volume': '4', 'file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', 'first_printed': 1920, 'last_printed': 2475, 'pdf_offset': -1917, 'lang': 'fas', 'offset_note': 'printed = pdf+1917, checked at pdf 150 and 500', 'ocr_text': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt'}, {'volume': '5', 'file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', 'first_printed': 1, 'last_printed': 290, 'pdf_offset': 5, 'lang': 'fas', 'note': "vol 5 = ta'liqat (addenda) with its own pagination 1-290; cite as BQT5:<page>. Plain BQT:<n> with n<1208 refers to vols 1-2 (OCR text files BQT_v1_pages.txt / BQT_v2_pages.txt), not to this scan.", 'ocr_text': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', 'requires_volume': True}]
```


## [2026-09-14T01:56:20.097Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"lemma: seni\\|lemma: septm\\|lemma: ser-\\|lemma: sen\" POK_full.txt | head -30",
 "description": "Grep POK_full for lemmas"
}
```


### [2026-09-14T01:56:20.150Z] TOOL RESULT

```
43497:from Root/ lemma: sen(o)-{*heno)\ 'old, *old moon' 
72799:Similar Root / lemma: sek-1 : to flow out, dry out (of water) : Root / lemma: seng"- : to fall, 
73527:Root /lemma: send'^ro-, -a 
73548:Root / lemma: seng^h- 
73565:Root / lemma: seng"- 
73571:From Root / lemma: sek-1 : to flow out, dry out (of water) derived Root / lemma: seng"- : to 
73586:Root /lemma: seni-, senu- {Sgni-), sp-ter- 
73618:Root / lemma: senk- 
73643:Root / lemma: sen(o)- {*heno) 
73684:Root / lemma: sent- 
73732:Root / lemma: sen-, sene- sen(e)u-, sena- 
73956:Root / lemma: ser-1 ( *ker- < *kel-) 
73996:Root / lemma: ser-2 
74030:Root / lemma: ser-3, sor- 
74054:Root / lemma: ser-4 
74093:Root / lemma: ser-5, extended serp-
```


## [2026-09-14T01:56:21.578Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 141 142 143 144 145 146 147; do echo \"=== leaf $n ===\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1{print}' POK_03.txt | head -20; done",
 "description": "Print POK_03 leaves around p.907"
}
```


### [2026-09-14T01:56:22.539Z] TOOL RESULT

```
=== leaf 141 ===
;  arm.  ham-  ,mit'  wohl  aus  dem Iran.) ;
lit.  sam-,  sq-  (z.  B.  sam-dyti  , dingen',  sdn-dora  , Eintracht',  sq-zine  , Ge- wissen, conscientia'),  apr.  san-,  sen-  (^san-insle  , Gürtel'),  sen  (*sem)  Präp. ,mit'  (idg.  *sem);  aksl.  so-  ,mit'  (sg-sMh  , Nachbar',  vgl.  ai.  sam-sdd-  »Ver- sammlung'), sq-log^  ,consors  tori',  vgl.  ä-Xoxog  usw. ;
mit  aksl.  sg-  ablautend  ist  *s^n-,  s^  (*Som)  z.  B.  in  s^n-iti  ,convenire^, s^-vezati  , zusammenbinden'  sowie  s^  Präp.  ,mit';  falls  lit.  sü  ,mit'  dazu- gehört, könnte  es  samt  aksl.  s^  und  gr.  ^vv,  avv  ,mit'  auf  idg.  *ksu  bzw. Vcsun  zurückgeführt  werden;  vgl.  Schwjzer  Gr.  Gr.  2,  487 ^
904
f
Von  som-  stammt  somo-s:  ai.  samci-  ,ehen,  gleich,  derselbe',  samdm  Adr und  Präp.  ,zusammenS  samdyä  ,m  gleicher  Weise,  mitten  hindurch^  *samal yati  ,ebnet,  bringt  in  Ordnung',  av.  ap.  hama-  .gleich,  derselbe',  arm.  o,„^ ^irgendwer'  (Meillet  Esquisse^  90) ;  über  ai.  simä-  ,selhst*  s.  WackernageU Debrunner  3,  578;
gr.  öuög  .gemeinsam;  ähnlich,  gleich,  eben,  glatt',  öf^ov  Adv.  und  Prip^p .zusammen',  öi-iö-^ev  ,aus  demselben  Ort^  öfiö-as  ,an  denselben  Ort',  6ifio,g'Ü ,gleichwohl'   (ö^ioiog,   natt.   o^oiog  .ähnlich^;   hierher   SjXTjQog  (oben  S.  ^^ ö^aoTSO)  ,begleite'  (zu  *OLiaQTog  aus  *som-r-to-s)j  nach   Szemer^nyi  Gl.  88  : 265  zu  *er-,  oben  S.  327  f. ;  air.  -som  .ipseS  air.  sund   ,hierS   cymr.   hunui' .dieser'  (aus  idg.  *so7ndhe,  welches  zu  sondo-  umgebildet  wurde);  got.  i^;^ sama  .derselbe*,  aisl.  samr^  inn  sami  .derselbe^  samt  Adv.  ,ununterbrochenV ahd.  der  samo  .derselbe',  vgl.  auch  Zs.  wie  got.  sama-kuns,  anord.  samkynU ,von  gleichem   Geschlecht^   gr.   Ofiöynog  ds.,   ai.   sama-jätiya  , gleichartig*,^ anord.   samfedra,  öf.i07i(XTüjQ,   ap.    hamapitar-   .von    demselben  Vater',  aiijj* sammedri,  ofiOfirjTQLog  .von  derselben  Mutter*;
ein  i-Fem.  *somi,  *sml  , Beisammensein,  Vereinigung,  z.  T.  auch  kämp*« fendes   Aneinandergeraten'   in  ai.   sami-kd-  n.   , Kampf,  Schlacht^;  aber  gr. 6'«i-Aog  , Haufe.  Versammlung,  Schlachtgedränge',  bf-älla  ,Umgang,  Verkehr*^ ö^lXso)   .verkehre'   bleiben  wegen   äol.  l)fxiXXog  fern,  ebenso  lat.  miles,  vj Szemerenyi   Arch.    Ling.    6.   41 ;    gr.    Sc^dXa    .Streit,    Kampf,  Wettstreit (*Sem-il-ia)y  ä{.iLXXaadai  .wettkämpfen';
dazu  mit  dem  Begriffe  des  friedlichen  Beisammenseins,  auch  des  Zrf sammenstimmens  aisl.  sama  , passen,  sich  schicken' ;  got.  samjan  .gefallen^ zu  gefallen  suchen',  aisl.  semja  (=  ai.  samayati)  , zusammenstellen,  vereini gen, 
=== leaf 142 ===
 einig  werden  um,  ordnen,  zustandebringen';  dazu  wohl  germ.  *sampu in  ahd.  semfti  (Adv.  samfto)  ,hequem,  gemächlich,  freundlich',  nhd.  «an/<, as.  safto  Adv.  .leicht',  mnd.  sachte  Adj.  Adv.  , sanft,  mild',  ags.  s^fU (Adv.  softe)  , ruhig,  mild',  vgl.  dazu  bes.  ai.  säntva-  n.  .gute  beschwichti- gende Worte',  säman-  m.   n.  .ds..  Milde,  freundliches  Entgegenkommen*;
germ.  *sampia-  ist  viell.  aus  einem  ^w-St.  *sampu-  umgebildet,  der  mit ai.  säntva-  auf  idg.  *söm-tu-  zurückgehen  kann ;
dagegen  ist  ags.  smede,  smöd^  as.  smödl  ,glatt.  eben,  sanft,  milde'  wegen westfäl.  smgid  aus  *sman]ji  entstanden;  got.  samap  , zusammen',  as.  samad, ags.  samodj  ahd.  samit  (samant  mit  n  nach  saman-),  nhd.  samt;  eine c?- Ableitung  in  ai.  samad-  f.  , Streit,  Kampf,  gr.  d^adog  , Gewühl,  Menschen- menge* ;
dehnstufig  ai.  säman-,  samand- , ruhig',  säma-gir- , freundliche  Worte  redend', säntva-  (s.  o.),  av.  häma-   ,gleich,   derselbe',   np.   hämün  , Ebene',  air.  »aw» - ,Ruhe'   (aus   ,*trauliches    Beisammensein'),   säim   ,ruhig,   mild',   aisl.   söma (*sömen)  ,passen,   geziemen*,   sömi  m.   ,Ehre,  Auszeichnung',   semr  .gezie-
905
lueiid,  passend^  as.  sömi  ds.;  ags.  söm  f.  , Einigkeit,  Versammlung',  ge-söm einmütig,  freundlich^,  mhd.  suome  , angenehm,  lieblich^;  abgel.  aisl.  sema gich  finden  in,  Rücksicht  nehmen  auf,  ehren^,  ags.  seman  , versöhnen' 5 eflo-l.  seem  , ziemen,  scheinen'  ist  nord.  Lw.;
aksl.  saim  ,ipse,  solus,  unus';
mit  i2-Formans:  ai.  säman-,  sämana-  s.  oben;  mit  ö-Stufe  wohl  ai.  sa- mana-  n.  , Zusammenkunft,  Festversammlung',  samanä  Adv.  ,zusammen, crleichzeitig,  ebenmäßig';  got.  samana  ,beisammen',  aisl.  saman  ,zusammen^, ahd.  samaUj  zi  samane,  nhd.  zusammen]  davon  abgeleitet  aisl.  samna,  ahd. savianön,  mhd.  samenen  , sammeln',  dissim.  samelen,  nhd.  sammeln-^  mit Red. -St.  ir.  samain  ,das  Fest  des  1.  Nov.'  (eigentlich  , Zusammenkunft'), hech-samain  ,Bienenschwarm' ;
eine  Dehnstufe  *sem  vielleicht  in  gall.  ao-aiv  , dieses^  und  im  n.  des  air. Artikels  {s)a'\  vortonig  aus  *sin,  dieses  aus  *sem  über  ^^sln]  die  übrigen Formen  sind  durch  Übertragung  der  Endflexion  auf  eine  Adv.-Form  *sinde (aus  ^sem-dhe;  es  läßt  sich  nach  ai.  sa-dha  idg.  *<iÄe,  oder  nach  ir.  suide  aus idg.  *so-de  (^o-Flexion)  =  gr.  8-6e  auch  idg.  *cZe  ansetzen)  entstanden; Demonstr.  ir.  sin,  cymr.  hynn  gehen  auf  den  Stamm  *sindo-  zurück  und stellen  die  enklitische  Form  dar.
WP.  II  488 ff.,  WH.  II  511  f.,  513,  533 ff.,  Trautmann  249 f.;  J.  Gonda Reflections  on  the 
=== leaf 143 ===
 Numerais.
5.  sem-  , Sommer'  (Gen.  Sein-ös)]  mit  Erweiterung  zum  ä-St.  Semä]  r-St. *Scn2er-. Ai.  sdmä  f.  , Halbjahr,  Jahreszeit,  Jahr*  (=  arm.  am),  äi-sd-mah  ,heuer' (wohl  aus  einem  Lok.  *äi-samäi  umgebildet,  s.  oben  S.  286) ;  av.  ham- ,Sommer';  arm.  am  ,Jahr^  (=  ai.  sdma)^  amafn  , Sommer'  (^Stm^rom)]  air. sam  i^semo-)  und  samrad  {^s^mo-röto-,  oben  S.  866),  cymr.  corn.  haf,  bret. haüv  , Sommer*;  cymr.  hafod  , Sommerhaus^,  bret.  havreg  , Brachfeld',  mir. samad  m.  , Ampfer';  gall.  samon\ios]  , Sommermonat*,  samolus  , Sauerklee', Samara  , Ulmensamen';  fern  bleibt  der  ibero-rom.  Fischname  samauca (Hubschmid  Rom.  Phil.  8,  12  f.);  ahd.  sumar^  ags.  sumor  m.,  aisl.  sumar n.  ,Sommer^;  als  , einjährige  Tiere'  aisl.  simull  ,(einjähriger)  Ochs',  simi, simir  ds.,  norw.  simla  , Renntierkuh'  (idg.  sem-).  schwed.  somel  ,Renntier- kalb'.
WP.  II  492  f.
semi-  ,halb'  als  1.  Kompositionsglied.
Ai.  sämi-  ,halb'  (d-sämi-  Adj.  ,nicht  halb,  vollständig');  gr.  ijjta-  ,halb' (fjfiiGvg    jhalb'   aus   ursprüngl.   f](J.iTvg  m.  ,*Hälfte',  vgl.   kret.   ii^itv-tyLtov,
906
epid.  'fjuirsLtt',  fiidva  ,HälfteO;  lat.  semi-  {semus  späte  Adjektivierung);  ,g^ indekl.'  ,halb,  Hälfte^  wohl  nach  6is;  ahd.   sämi-,   as.   säm--^  vgl.  lat.  ^gnit vivus,  gr.   'fj^d-ßiog,  ahd.  sämi-quecJc,  as.  säm-quick  ,halbtot^ WP.  II  493,  WH.  II  512  f.
sen-,   sene-,   sen{e)u-,   send-   ,hereiteii;   ausarbeiten,  vollenden,  erzielen'^
Ai.  dsanam  ,ich  gewann',  sanima  ,wir  mögen  gewinnen';  saiiöti  ;gewiiin|t' sanukd-  ,beutegierig',  sanitär-  ,Gewinner,  Sieger',  Partiz.  sätd-  ;gewoiinen<* säti-  f.  ,Gewinnung,  Erwerb';  gr.  *ävvfa,  themat.  dvvo),  att.  äpvco  und  hont      ^ ävü)    {*ävJ^(x})   ,vollende';    gr.    ävvrto    ds. ;    davsg-    od    T€Xsad^7]a6f.ievov    He^ iv    ävdTOig'    iv    änoqlaLg    Hes.    {äv-arog    ,unvollendet') ;    hom.    ivveci-BQYQ^ Jgya   dvvajv^',    svagcc    ,die   Rüstung   des   erschlagenen    Gegners'   (*,Kanip. fesbeute');   davon   ivalgco,    Aor.    'ijvaQOv   ,im   Kampfe   toten',   svagllu)  ,dem getöteten  Feinde  die  Rüstung  ausziehen;  im  Kampfe  töten';  lak.  ivagaa^^ Qog  „rä  evaga  cpsgcov"]   evrsa  (Sg.   evrog)  ,Rüstung';   woneben   *ivuig  ,Zu».,. rüstung,  Vollendung'  vorausgesetzt  von  irzva),  iviivco  , mache  fertig,  rüstf^^ zu,  bereite';  neben  tö   evrog  steht  ovv-ivrrig'   avvegyög  Hes.   und  aid^hrn^-^ ,*mit  eigener  Hand  vollbringend:  Mörder;  Herr*;
air.  con-sul  ,sucht  zu  erwerben,  macht  streitig',  cymr.  cynyddu  ,erobemS zu  gewinnen  suchen'  usw. ;
hitt.  §anh-  ,suchen,  erstreben,  fordern';  auch  , fegen'  (,*durchsuchen*).
WP.  II  493,  Pedersen  Hitt.  185.
sendhro-,  -ä  , geronnene,  sich  verdichtende  Flüssigkeit':  nur  germ.  und  slav» Aisl.  sindr  n.  , Metallschlacke'  und  , Hammerschlag'  (dazu  sindra  ,Funken sprühen')^  ags.  sinder  ds.,  ahd.  sinter  ds.,  nhd.  Sinter,  Kalksinter  (dazu sintern  , durchsickern,  gerinnen');  vermutlich  ve
=== leaf 144 ===
rwandt  ist  norw.  dial.i sinkla  ,sich  mit  einer  Eiskruste  beziehen'  als  *si7id-kla-  serb.-ksl.  8ediy\ krhvhnyje,  russ.-ksl.  sjadry  krovnyja  ,geronnene  Blutmassen',  skr.  sl^dra^ , Kalksinter',  cech.  sddra  ,Gips'  (aus  '*sendhrä). WP.  II  497,  Trautmann  256.
seng^-  ,  fallen,  sinken'.
Arm.  ankanim  , falle,  weiche,  nehme  ab';  gr.  sdcp^vj  ,sank'  {dOTiig)]
germ.  *sinkwan  in:  got.  sigqan^  aisl.  sekkva^  ags.  sincan,  as.  ahd.  sinkan^'^
sinken,  Intens,  dän.-norw.  sakka,   ndl.   zakken^   nhd.   sacken  , sinken';   Adj/j:-!^
*sinhti-  in  ags.  sihte  , sumpfig',  mhd.  slht{e),  nhd.   seicht,  alem.  sieht  ,sebr;^''"'^
feucht'  (von  Wiesen).
WP.  II  495  f.
seng^h-   »singen,   mit   singender   Stimme    vortragen';   song^bo-s   , Gesang'»
907
präkr.  samghai  , sagen,  belehren*;  gT.  öf-irfr}  , Stimme,  Prophezeiung* /*sojig^(ihä),  Tcavoucpalog  , Beiname  des  Zeus';  mcymr.   de(h)ongl  , erklären';
o-ot.  siggwan  ^singen,  vorlesen,  rezitieren',  aisl.  syngua,  ags.  ahd.  as. gingan,  singen-^  got.  saggws  , Gesangs  Musik,  Vorlesung',  aisl.  sgngr  , (kirch- licher) Gesang^,  ags.  sang,  song,  ahd.  as.  sang,  Sang  , Gesang,  Lied'.
WP.  n  496,  Bloch  BSL  31,  62,  Vendryes  RC  48,  476;  nach  W.  Wüst (brieil.)  gehört  präkr.  samghai  zu  kens-,  oben  S.  566.
seni-f  senu-,  (seni-),  sn-ter-  ,für  sich,  abgesondert^
Ai.  sanu-tdr  ,abseits  von,  weit  weg^  sdnutara-(?),  sdnutya-  ,verstohlen, unvermerkt'  (*,beiseite'),  av.  hanard  , abseits,  ohne^;  gr.  Ureo  (ion.)  , abseits, ohne'  {^snter)]
as.  sundir  ,ohne'  (=  Uisq),  ahd-.  suntar  »abgesondert'  und  ,aber,  dagegen', nhd.  sondern  (diese  Bed.  aus  jaußer,  ohne'),  ags.  sundor  ,für  sich,  beson- ders', anord.  sicndr  , entzwei',  got.  sundrö  ,für  sich,  abseits,  besonders^, Adj.  mhd.  sundei',  besunder,  nhd.  besonder]
lat.  sine  ,ohne'  (wohl  neutr.  "^seni,  nächststehend  dem  ir.  sain  aus  *5e7w*-);
air.  sain  Adj.  »verschieden,  besonders^  (*V^i-s),  cymr.  o-han-y  a-han-  ,von', gwa-han  , getrennt,  verschieden',  acymr.  han  ,alium' ;  cymr.  hanes  , Er- zählung' =  mir.  Sanas  , Geheimnis,  Lispeln'  (*sani-sta) :  corn.  hanys  ,heim- lich';  toch.  A  sne^  B  snai  {*sanai)  ,ohne*;
Die  Bedeutung  ,abgesondert,  für  sich'  läßt  Verbindung  mit  dem  Reflexiv- stamm *se-,  *s(e)iie-  zu,  vgl.  mit  Anlaut  su-:  aksl.  svSnS  ,außer,  ohne'  und lat.  sed,  se  Präp.  ,sine,  ohne*,  Präf.  ,ohne,  beiseite'.
WP.  II  494f.,  WH.  II  542f.,  H.  Lewis  EC.  1,  322.
=== leaf 145 ===
kenheit,  Dürre',  sine  {-g-)  ,das  Sengen',  sungen,  sunken , anbrennen',  sungeln,  sunkeln  ,knistern',  norw.  dial.  sengra,  sengla  ,brenzlich riechen',  schwed.  dial.  sjängla  ,sengen',  isl.  säng{u)r,  n.  sangt  ,versengt, angebrannt' ;
aksl.  pre-socitl,  isqciti  ,trocknen',  sgcilo  ,Ofen',   russ.   izsjaklyj  , trocken'.
WP.  II  495.
serz(o)-  ,alt';  seno-mäter  , Großmutter'.
Ai.  sdna-^  av.  hana-  ,alt',  ai.  sanakd-  , ehemal  ig,  alt'  (:  lat.  senex,  fränk. Sinigus^  gall.  Seneca),  sanah  ,vor  alters',  sdnä^  sanät,  sandtä  ,von  alters her,  von  jeher,  stets',  sanätdna-  ,ewig,  unvergänglich,  beständig';  arm. hanajpaz  , immer',  hin  ,alt';  gr.  svog  ,alt,  vom  Aderigen  Jahre',  di-evog  ,zwei-
908  •
jährig^  evT;.yMl  via  ,der  Tag  vor  dem  Neumond  und  der  erste  des  beginnen, den  Monats';  lat.  sßnex,  Gen.  senls,  Kompar.  senior  ,alt,  bejahrt';  seneö,  -gre, ,alt,  schwach  sein',  smlscö,  -ere  ,altern,  hinschwinden',  Senium  \Alters. schwäche,  zehrende  GemütsstimmungS  senätus,  -üs  (osk.  Gen.  senattU) , Senat',  senectüs  , Alter',  seneciö  ds. ;  air.  sen  ,^\i',  acjmr.  corn.  bret.  ^en ,senex',  Komp.  air.  siniu,  cymr.  %n;  ir.  sen-mäth{a)ir  (==  lit.  sen-mrfeg) , Großmutter';  gall.  Seno-gnätus  u.  dgl,  Äerieca;  got.  sineigs  „^Qsaßvrr^gU^ sinista  ,ältester',  afränk.  sini-skalkus  ,der  älteste  Hausdiener',  aisl.  sina ,vorjähriges  Gras';  lit.  senas  ,alt',  senis  ,Greis',  seniaX  ,vor  alters,  längst', seneju  , werde  alt'  (=  lat.  seneö).
WP.  II  494,  WH.  II  513  f.,  Trautmann  256.
sent-  ,eine  Richtung  nehmen,  gehen'  {sento-  , Gehen,  Reisen;  Weg')  und im  geistigen  Sinne  ,empfinden,  wahrnehmen'.
A.  im  geistigen  Sinne:  lat.  sentiö,  -Ire,  -si,  -sum  ,fühlen,  empfinden,  wahr« nehmen',  sensus,  -üs  , Gefühl,  Sinn,  Gesinnung,  Meinung',  sententia  (*sen- tientia)  , Meinung  usw.';  ahd.  sin,  -nnes  ,Sinn'  (*sent-no-),  sinnan  ,trachten, begehren',  nhd.  sinnen]  lit.  sinteti  , denken';  aksl.  sesth  ,klug'.
B.  im  eigentlichen  Sinne :  av.  haut-  (Präs.  hl-sasat,  Fut.  ni-sqsya)  ,gelan- gen,  gelangen  lassen';  arm.  dntac  ,Weg,  Gang',  dntanam  ,gehe,  reise,  eile';
air.  set  ,Weg',  cymr.  hynt  ds.,  mbret.  nbret.  hent  ds.  (=  germ.  *sin'pa-)y abret.  Gl.  do-guo-hintiliat  ,inceduus',  acorn.  cam-hinsic  Gl.  ,iniustus*  {cam- , krumm'),  eun-hinsic  Gl.  ,justus'  (eun-  , gerecht');  davon  air.  setig  ,Frau' (, Weggenossin',  l-Fem.  eines  Adj,  *setach)',  cymr.  carrynt  (zu  cai^r  ,Wagea') ,Weg,  Reise',  epynt  (zu  eb-,  *ekuo-)  ,Pferde-Weg',  dyffrynt  ,Tal'  (zu  dtofr ,Wasser');  aus  *sentio-:  mcymr.  hennydd  , Gefährte',  bret.  hantez  , Nachbar', ; corn.   hynsa  ds. ;
got.  sinps  m.  ,Mal',  aisl.  sinn  n.  ,Mal',  sinni  n.  ,Gang,  Reise'  (und  als Nachkomme  eines  *gasinpja-  
=== leaf 146 ===
auch  , Gefolge,  Unterstützung'),  ags.  sld  m.  j jFahrt,  Reise,  Weg,  Mal',  as.  sld  ,Weg,  Richtung*,  ahd.  sind  ,Gang,  Weg, Reise,  Fahrt';  got.  ga-sin^a  ,Reisegefährte',  aisl.  sinni  ds.,  ags.  ges'ip,  as. gisid,  ahd.  gisind  , Gefährte',  wozu  n.  ags.  gesid  , Begleitung',  as.  gesithi, mnd.  {ge)sinde  , Gesinde',  ahd.  gisindi  , Reisegefolge,  kriegerisches  Gefolge', nhd.  Gesinde,  aisl.  sinni  n.  , Gefolge';  ahd.  sinnan  (s.  oben)  auch  ,gehen, reisen,  wandern,  kommen';  Kaus.  got.  sandjan,  aisl.  senda,  ags.  sendan, ahd.  senten  , senden'  (aisl.  senda  auch  , opfern') ;  *senpön  Denom.  von  ^senpa- (s.  oben)  in  aisl.  sinna  ,reisen,  sich  worum  kümmern,  beachten',  as.  sidön , gehen,  ziehen,  wandern',  ags.  sldian  ds.,  ahd.  sindön  ds.;
lit.   siunUii   {*suntiii  ass.   zu  *siuntiü),   sii{,sti,   lett.    sütu,    sittit   ,senden, schicken'  (halt,  un  Red.- St.  o«  neben  der  Vollstufe  von  got.  sandjan).
WP.  II  496  f.,  Trautmann  292.
909
grt-  ,sich  mit  etwas  abgeben,  in  Ehren  halten*;  sep-el-  , Sorge,  Ehrfurcht'.
^i.  sdpati  ^liebkost,  umwirbt,  pflegt,  betreibt',  av.  hap-  (2.  3.  Sg.  hafll, hapt'^)  )(i^  döJ'  Hand)  halten,  stützen*;  gr.  -stio)  (mit  äf.iq)L-,  öl-,  e(p-, neS-'i  ft€Qi-),  Aor.  krc-e-aTtov,  -arceXv  ,besorge,  bereite,  bearbeite*;  otzXov  n. \Verkzeug,  Gerät,  Waffe ^,  ÖTtlaoj  ,schirre  an',  dnlofxai  , bereite  mir  zu*  usw.*
dazu  idg.  *sepeliö  in  ai.  saparydti  ,veneratur',  lat.  sepeliö  ,-ire^  sepultum begraben^  d.  i.   ,venerari  sepulcro'.
WP.  II  487,  WH.  II  517,  Benveniste  Origines  1,  47
sept^  »sieben*.
Ai.  saptd,  av.  hapta,  arm.  evtn,  gr.  l/rira,  lat.  Septem,  air.  secht  n-,  cjmr. usw.  saith,  got.  ahd.  sihun,  ags.  seofon,  anord.  siau  (-n  bewahrt  nach  einem neben  *sibun  stehenden  sibuni;  ^-Verlust  im  Ordinale  sep[t]7ii-tos  dissimi- latorisch  erfolgt;  ob  septun  der  Lex.  sal.  noch  gesprochenes  seftun  oder Latinisierung  eines  echten  *sifun  ist,  steht  dahin),  lit.  septym,  aksl.  sedmh (nach  dem  Ordinale),  alb.  shtate  (*s[e]p^m-^i-;  Zahlabstraktbildung  wie  ai. saptati-j  av.  haptäiti-  70,  aisl.  siaund  , Anzahl  A^on  7^);  toch.  A  spät, B  suk(t);  hitt.  sipta.
Ordinale:  sept(e)mos  in  ai.  saptamd-,  npers.  Tiaftumj  gr.  eßdoiiog,  dial. eßÖE^oq  (die  Erweichung  stammt  aus  einer  Form  eßd^xog^  vgl.  aksl.  sedmh), lat.  septimus,  gall.  sextametos,  air.  sechtm-ady  cjmr.  seithfed  {* Septem- etos), alit.  sekmas,  apr.  sep{t)mas,  aksl.  sedm^'^  *septm-tO'S  in  ai.  saptdtJiahj  av. haptad^a-,  as.  sivotho,  ags.  seofoäa  (auch  akzentuell  =  saptätah]  daneben ahd.  sibunto,  as.  sivondo,  anord.  siunde,  siaunde),  lit.  septintas.
WP
=== leaf 147 ===
.  II  487.
1,  ser-  »strömen,  sich  rasch  und  heftig  bewegen';  sero-m  ,Flüssigkeit* ; ser-mo'  ,Fluß',  sorä  ds.
Ai.  sisartij  sdrati  ,fließt,  eilt,  jagt  wornach,  verfolgt';  fut.  sarisydti,  De- siderativ  sislr^ati  von  einer  schweren  Basis  ^serd-,  vgl.  hom.  Q(x)0(.LaL  , be- wege mich  schnell,  kräftig,  stürme  an,  eile'  aus  *s?'ö-to;  ein  Wurzel- nomen *sp,  dazu  ai.  "^sir,  "^sirdh,  ist  die  Grundlage  des  a-St.  ai.  sirä  und slrä  , Rinnsal,  Strom';  ai.  sarü  f.  ,Bach,  Fluß",  sararia-  ,laufend',  sa-sr-d- jStrömend*,  sd-sr-i-  , laufend,  eilend';  sardyu-,  sarayü-  m.  ,Name  eines Flusses',  ap.  Haraiva-,  av.  (Akk.)  Haröyüm,  np.  Hare  ,Fluß  und  Gegend von  Herät';
ai.  sdrma-  m.  ,das  Fließen',  gr.  ÖQ(.irj  , Anlauf,  Angriff,  Drang  nach  etwas', wovon  ögf-idü)  ,treibe  an,  rege  an',  intr.  , stürme  daher,  worauf  los';  dazu 8Qf.iEvov  ,Salbei  als'  die  anreizende,  s.  Strömberg,  Gr.  Pflanzennamen  93; algeco  »ergreife'  statt  ^aigct)  (*SeHö)  durch  Einfluß  von  dygico  ds. ;
910  •
ai.  sard-  , flüssig',  sard  ,Fluß,  BachS  gv.  ögög^  lat.  serum  ,der  wässeri«^' Teil  der  geronnenen  Milch,  Molke';  vielleicht  alb.  gjize  {*ser-dia)  ;gelabtft Milch,  Käse^;
thrak.  ON  Germi-sera  ^Warmwasser*,  FIN  leg^iog;  frz.  la  SerrriQj^^ (*Sermanna\  oberital.  Sermenza  {*Sermentia),  ven.  ON  Slrmiö  {*Sermifi\ paanon.  ON  Sirmium,  poln.  (ven.)  ON  Srem  (*Sermo-)',  illyr.  FIN  Sarnm (Kampanien);  gall.  (ven.-illyr.)  FIN  Sara  (*Serä),  Sarävus  ,die  Saar*;  ßar^ bildet  viele  FIN  in  der  Lombardei,  Schweiz  und  Frankreich,  auch  Appell^, tiva  (Mantua  sariöl  ,Bach^  usw.);  cymr.  FIN  Sör  (*Sora}',  sor-  auch  in den  FIN  apr.  Sar-ape,  lit.-poln.  Szar-upa,  lett.  Sarija;
mir.  shnd  (*se'nti)  , durchwandert,  sucht  heim,  plündert,  verlangt^,  Verbal- nomen  siriud-,  cymr.  herw  (*ser-uo-)  ^Landstreicherei',  mir.  serb  , Diebstahl*»
lit.  apsirti  , umzingeln',  lett.  sirt  , umherschwärmen,  Raubzüge  machen* sira  (vgl.  ai.  sira)  ,Umherstreifer,  Bettler'.
WP.  II  497  f.,  WH.  II  525,  Schwyzer  Gr.  Gr.  1,  727^;  dazu  sreu-  ,fließen*} nach  E.  Fraenkel  Gl.  32,  33  hierher  gr.  qed-sa  ,Nasenlöcher,  Nase',  ^d^oj , Wogenschwall',  sowie  ^/^,  qivög  ,Nase^  als  ,die  Triefende'.
3.  ser-  , sorgend  Obacht  geben,  schützen,  bewahren'.
Av.  haraiti  ,hat  acht,  schützt';  haurvaiti  ds.,  haurva-  ,beschützend, hütend'  in  pasus-haurvö  spä  ,die  Schafe  beschützender  H
```


## [2026-09-14T01:56:50.159Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD septm ===\"; grep -n \"^sept\" AHD_watkins1985.txt | head; echo \"=== AHD ser ===\"; grep -n \"^ser-\" AHD_watkins1985.txt | head; echo \"=== AHD seni ===\"; grep -n \"^seni\\|^sen-\\|^sem-1\" AHD_watkins1985.txt | head",
 "description": "Grep AHD Watkins roots"
}
```


### [2026-09-14T01:56:50.298Z] TOOL RESULT

```
=== AHD septm ===
923:septm. Seven. 1. Germanic *sebum in Old English seofon, seven: SEVEN. 2. Latin septem, seven: SEPTEMBER, SEP- TENNIAL, SEPTET, SEPTI-, SEPTUAGINT, SEPTUPLE; SEP- TENTRION. 3. Greek hepta, seven: HEBDOMAD, HEPTA-, HEPTAD. [Pok. septm 909.]
=== AHD ser ===
924:ser-1, To protect. 1. Extended form *serw- in Latin serudre, to keep, preserve: CONSERVE, OBSERVE, PRE- SERVE, RESERVE, (RESERVOIR). 2. Suffixed length- ened-grade form *sér-6s- perhaps in Greek hérés, “protector,” hero: HERO. [Pok. 2. ser- 910.]
925:ser-?, To flow. 1. Suffixed form *ser-o- in Latin serum, whey: SERAC, SERUM. 2. Basic form *ser- in Sanskrit sarati, sasarti, it flows, it runs: SAMSARA. 3. Extended roots *sr-edh-, *sr-et-, to whirl, bubble, in Germanic *stred- in Old High German stredan, to whirl, swirl, whence ablaut formation in Middle High German séru- del, whirlpool: STRUDEL. [Pok. 1. ser- 909; sr-edh- 1001.]
926:ser-3, To line up. 1. Latin serere, to arrange, attach, join (in speech), discuss: SERIES, SERTULARIAN; ASSERT, DESERT’, DISSERTATE, EXERT, INSERT. 2. Suffixed form *ser-mon- in Latin sermé (stem sermé6n-), speech, dis- course: SERMON. 3. Suffixed form *ser-d- perhaps in Latin sera, a lock, bolt, bar (? < “that which aligns”): SEAR?, (SERRIED). 4. Suffixed zero-grade form *sr-t- in Latin sors (stem sort-), lot, fortune (probably from the lining up of lots before drawing): SORCERER, SORT; ASSORT, CONSORT, SORTILEGE. [Pok. 4. ser- 911.]
=== AHD seni ===
1654:sem-1
```


## [2026-09-14T01:56:52.267Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN sans ===\"; grep -n \"^sans,\" KLN_1966.txt | head; echo \"=== KLN sincere ===\"; grep -n \"^sincere\" KLN_1966.txt | head; echo \"=== KLN seven ===\"; grep -n \"^seven,\" KLN_1966.txt|head; echo \"=== KLN serum ===\"; grep -n \"^serum,\" KLN_1966.txt|head; echo \"=== KLN September ===\"; grep -n \"^September\" KLN_1966.txt|head",
 "description": "Grep Klein headwords"
}
```


### [2026-09-14T01:56:52.463Z] TOOL RESULT

```
=== KLN sans ===
=== KLN sincere ===
13893:sincere,  ‘to  vanquish’.  See  vincible  and  cp.  evict. Derivatives:  evinc-ible ,  adj.,  envinc-ibl-y,  adv., envinc-ive,  adj.
=== KLN seven ===
=== KLN serum ===
=== KLN September ===
34619:September,  n.,  the  ninth  month  of  the  year.  —  L. September  (mensis),  lit.  ‘the  seventh  month  (of  the Roman  year)’,  fr.  septem,  ‘seven';  see  septem-. The  Roman  year  began  with  March  (cp.  Octo¬ ber,  November,  December).
```


## [2026-09-14T01:57:07.393Z] TOOL CALL #12: Bash

```json
{
 "command": "pdftoppm -f 444 -l 444 -r 300 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg444 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg444.png",
 "description": "Render PDF page 444"
}
```


## [2026-09-14T01:57:09.241Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 734 735 736; do echo \"=== KLN leaf $n ===\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1{print}' KLN_1966.txt | grep -n \"sans\\|sincer\\|1447\\|1446\" | head -20; done",
 "description": "Find sans/sincere in KLN leaves"
}
```


### [2026-09-14T01:57:10.340Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 70076 Sep 13 21:57 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg444.png
```


### [2026-09-14T01:57:11.712Z] TOOL RESULT

```
=== KLN leaf 734 ===
17:Sanoussi,  n.  —  See  Senussi. sans,  prep.,  without  (archaic).  —  F.,  fr.  OF.  sens, a  blend  of  L.  sine,  ‘without’  (see  sine,  ‘without’), and  L.  absentia,  ‘in  the  absence  of’  (abl.  of  ab¬ sentia,  ‘absence’ ;  see  absence).  Cp.  senza. Sanscrit,  n.  and  adj.  —  See  Sanskrit, sans-culotte,  n.,  a  republican  of  the  poorer  class¬ es  in  the  French  Revolution.  —  F.,  lit.  ‘without breeches’.  For  the  first  element  see  sans.  F.  ca¬ lotte  is  a  diminutive  form  derived  fr.  cul,  ‘bot¬ tom,  backside’,  fr.  L.  cuius ;  see  culotte.  The name  sans-culotte  prop,  denotes  those  who — in contradistinction  to  the  upper  classes  that  wore culottes — chose  pantalons ,  (long  trousers)  for their  distinctive  costume.
18:Derivatives:  sans-culott-ic,  sans-culott-ish,  adjs. sans-culottism,  n.,  the  principles  of  sans-culottes.
19:—  F.  sans-cullottisme,  fr.  sans-culotte.  See  prec. word  and  -ism.
=== KLN leaf 735 ===
=== KLN leaf 736 ===
```


## [2026-09-14T01:57:16.477Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"sincere,  adj\\|sincere, adj\\|sincer\" KLN_1966.txt | head -10; echo \"=== sine ===\"; grep -n \"sine,  prep\\|sine, prep\\|^sine,\" KLN_1966.txt | head -10",
 "description": "Find sincere and sine in Klein"
}
```


### [2026-09-14T01:57:16.552Z] TOOL RESULT

```
37:On  this  occasion  I  would  like  to  extend  my  affectionate  feelings  to  two  of  my  closest  and dearest  friends  in  Toronto,  whom  I  love  both  as  if  they  were  brothers  to  me  in  the  literal  sense  of this  term :  Mr.  Arthur  Minden,  Q.C.,  whose  friendship  and  love  I  treasure  as  one  of  the  greatest gifts  bestowed  upon  me  by  Providence  and  whose  zeal  and  encouragement  have  been  an  im¬ portant  factor  in  my  writing  and  completing  this  dictionary,  and  Mr.  Leo  Bermann,  whose sincere  brotherly  affection  and  friendly  devotion  have  always  been  and  continue  to  be  a  grati¬ fying  source  of  spiritual  joy  to  me,  and  who  had  a  decisive  role  in  the  history  of  the  publication of  my  dictionary.
42:May  this  dictionary,  which  plastically  shows  the  affinity  and  interrelationship  of  the  nations of  the  world  in  the  way  in  which  their  languages  developed,  contribute  to  bringing  them  nearer to  one  another  in  the  sincere  pursuit  of  peace  on  earth  —  which  was  one  of  my  cardinal  aims in  writing  this  dictionary.
5871:Derivative :  bunker,  tr.  v. bunkum,  buncombe,  often  shortened  to  bunk,  n., speechmaking  for  effect;  insincere  talk; hum¬ bug.  —  From  Buncombe ,  name  of  a  county  in North  Carolina,  one  of  whose  representatives was  said  to  have  spoken  frequently  in  Congress, merely  to  impress  his  constituents, bunny,  n.,  pet  name  for  a  rabbit.  —  Formed  fr.
6338:candescent,  adj.,  glowing.  —  L.  candescens,  gen. -entis,  pres.  part,  of  candescere,  ‘to  begin  to glow’,  inchoative  of  candere,  ‘to  shine,  glow’, whence  also  candidus,  ‘glowing,  white’.  See  next word  and  -escent,  and  cp.  incandesce. Derivative r  candescent-ly,  adv. candid,  adj.,  impartial;  frank,  sincere.  —  F.  can- dide,  ‘open,  frank,  ingenuous,  sincere,  candid’, fr.  L.  candidus,  ‘glowing,  white;  pure,  honest.
6341:Derivative:  candidat-ure,  n. candle,  n.  —  ME.  candel,  fr.  OE.  candel,  fr.  L. candela,  ‘candle  made  of  wax  or  tallow’,  fr. candere,  ‘to  shine,  glow,  burn’.  See  candid  and cp.  candelabrum,  chandelier,  chandler. Candlemas,  n.  —  ME.  candelmasse,  fr.  OE.  can- dehmesse,  compounded  of  candel,  ‘candle’,  and mxsse,  ‘Mass’.  See  candle  and  Mass, candlestick,  n.  —  ME.  candlestikke ,  fr.  OE. candelsticca,  compounded  of  candel,  ‘candle’, and  sticca,  ‘stick’.  See  candle  and  stick,  n. candor,  candour,  n.,  impartiality,  frankness.  — L.  candor,  ‘whiteness;  sincerity,  candor’,  from the  stem  of  candere,  ‘to  be  white'.  See  candid and  -or.
6551:Caridea,  n.,  a  group  of  crustaceans  (zool.)  — ModL.,  formed  with  suff.  -idea  fr.  Gk.  y.ipiq, gen.  xapiSop,  ‘shrimp,  prawn’,  which  is  prob. rel.  to  xipxflop,  ‘horned  beetle’.  See  scarab  and cp.  Carabidae.  Cp.  also  Epicarides,  Syncarida. caries,  n.,  decay  ( med .)  —  L.  caries,  ‘decay,  rot¬ tenness-,  fr.  I.-E.  base  *ker-,  ‘to  hurt,  hit’, whence  also  Gk.  xf,p,  ‘death,  destruction’, jtxypx rop,  ‘unhurt’,  xepxtljs'.v  (for  *x£pxfl^eiv), 'to  lay  waste’,  xspxuvop  [for  *xspx-.r(s)vd;], ‘thunderbolt,  lightning’,  lit.  ‘smasher,  crusher'. OI.  srnSti,  ‘breaks,  crushes’,  iiryate,  siryate, ‘falls  asunder’,  OIr.  ar-a-chrinim,  ‘I  fall  to pieces’,  irchre,  ‘fall,  ruin',  crin,  ‘withered,  faded'. Cp.  cerauno-  and  the  second  element  in  sincere, carillon,  n.,  musical  bells.  —  F.,  ‘peal  of  bells’, fr.  OF.  quarregnon,  carignon,  fr.  VL.  quadrini- onem ,  acc.  of  *quadrinid,  refashioned  on  anal¬ ogy  of  words  beginning  with  quadri-  (see  qua- dri-),  fr.  L.  quaternid,  ‘a  group  of  four  things’ (here  used  in  the  sense  of  ‘a  group  of  four bells’).  See  quaternion.
7013:cerauno-,  kerauno-,  a  combining  form  meaning ‘thunderbolt".  —  Gk.  xepauvo-,  fr.  xspauvoi;, ‘thunderbolt,  lightning’,  which  stands  for  *xepa- F(e)vo p,  lit.  ‘smasher,  crusher’,  rcl.  to  xepat^ew (for  *xEpafi£eiv),  ‘to  lay  waste’,  and  cogn. with  L.  caries,  ‘decay,  rottenness’.  See  caries and  cp.  the  second  element  in  sincere, ceraunograph,  keraunograph,  n.,  an  instrument for  recording  thunderstorms  and  lightnings.  — Compounded  of  cerauno-  and  Gk.  -ypaepot;,  fr. ypatpEiv,  ‘to  write’.  See  -graph.
13893:sincere,  ‘to  vanquish’.  See  vincible  and  cp.  evict. Derivatives:  evinc-ible ,  adj.,  envinc-ibl-y,  adv., envinc-ive,  adj.
14508:federal,  adj.  —  F.  federal,  from  L.  foedus,  gen. foederis,  ‘league,  treaty,  covenant’,  which  stands in  gradational  relationship  to  fidere,  ‘to  trust’, fidelis,  ‘true,  faithful,  sincere’.  See  fidelity  and cp.  federate,  confederate.  For  the  ending  see adj.  suff.  -al.
19436:inlet,  n.,  anything  put  in;  an  arm  of  the  sea,  etc. —  Formed  fr.  in,  adv.,  and  let,  ‘to  leave’, inly,  adv.,  within,  inwardly.  —  ME.  inliche,  inly, fr.  OE.  inlice,  ‘internally;  sincerely’.  See  in  and adv.  suff.  -ly.
=== sine ===
35284:Derivative:  sincipit-al,  adj. sindon,  n.,  a  fine  fabric  of  linen.  —  L.,  fr.  Gk. (p.vScov,  ‘linen’,  lit.  ‘Indian  stuff’.  See  sendal. sine,  n.  ( trigon .)  —  L.  sinus,  ‘the  fold  of  a  garment ; bosom;  curve,  gulf’,  in  Late  L.,  ‘sine’;  cogn. with  Alb.  gi-ri  (for  *gin-ri),  ‘bosom,  womb’.  As a  mathematical  term,  L.  sinus  was  first  used  by Gherardo  of  Cremona  in  his  translation  from the  Arabic  (about  the  year  1150)  to  render  Arab. jayb,  ‘chord  of  an  arc;  sine’  (fr.  Ol.jiva-,  ‘bow¬ string’),  which  he  confused  with  Arab,  jayb, ‘fold  of  garment’.  Cp.  cosine, sine,  prep.,  without  (in  Latin  phrases).  —  L.  sine, ‘without’,  is  an  enlarged  form  of  L.  sed,  se, ‘without’  and  is  cogn.  with  OI.  sanitup,  ‘with¬ out,  outside’,  sanutar,  ‘far  away’,  Gk.  Strep  (for *sn-ter),  ‘without’,  Goth,  sundrd,  ‘alone,  separ¬ ate’,  OHG.  suntar,  MHG.  sunder,  ‘aside,  apart’, OE.  sundor,  ‘apart,  asunder’,  MHG.  sundern,  G. sondern,  ‘but’.  See  sunder,  and  cp.  se-  and  the first  element  in  sincere  and  in  sinecure.  Cp.  also sans.
35286:Derivatives:  sinecur-ism,  n.,  sinecur-ist,  n. sine  die,  without  a  date  fixed.  —  L.  sine  die,  lit. ‘without  a  day’,  fr.  sine,  ‘without’,  and  die,  abl. of  dies,  ‘day’.  See  sine,  prep.,  and  dies  non. sine  prole,  without  issue  (law).  —  L.,  ‘without  off¬ spring’,  fr.  sine,  ‘without’,  and  prole,  abl.  of proles,  ‘offspring,  descendant'.  See  sine,  prep., and  proletarian.
37463:sunder,  tr.  and  intr.  v.,  to  separate,  divide.  — ME.  sundren,  fr.  OE.  sundrian  (only  in  the  com¬ pounds  asundrian,  gesundrian,  onsundrian,  td- sundrian),  fr.  sundor,  ‘asunder’,  which  is  rel.  to OS.  sundar,  ON.  sundr,  Swed.  sonder,  OFris. sunder,  OHG.  suntar,  ‘aside,  apart’,  MHG.  sun¬ der,  G.  sonder,  Du.  zonder,  ‘without’,  Goth. sundro,  ‘apart’.  Cp.  ON.  sundra,  Swed.  siindra, MLG.  sunderen,  Du.  -zonderen,  OHG.  suntaron, MHG.  sundern,  siindern,  G.  sondern  (now  used only  in  the  compounds  absondern,  aussondern), ‘to  separate’,  which  derive  from  the  adverbs  ON. sundor,  resp.  its  equivalents  given  in  the  prec. sentence.  These  words  are  cogn.  with  OI.  sanu- tdr,  ‘far  away’,  Avestic  hanar e,  ‘without’,  Toch. A  snu,  B.  snai,  sne,  ‘without’,  Gk.  a- rep  (for *sn-ter ),  ‘without’,  L.  sine,  ‘without’,  OIr.  sain (for  *sani),  ‘different’,  OW.  han,  ‘another’, hannr,  W.  banner,  ‘the  half’  (lit.  ‘the  other  part’). All  these  words  ultim.  derive  from  I.-E.  base *seni-,  ‘away  from,  without’.  Cp.  sine,  prep., sinecure,  sincere.  Base  *seni-  is  an  enlargement of  the  reflexive  base  *se-.  See  se-. sunderance,  n.  —  A  hybrid  coined  fr.  sunder  and -ance,  a  suff.  of  Latin  origin, sundry,  adj.,  various.  —  ME.,  fr.  OE.  syndrig,  ‘sep¬ arate,  several’,  fr.  sundor,  ‘apart’.  Cp.  OHG. sunrarig,  ‘sundry’,  and  see  sunder  and  -y  (rep¬ resenting  OE.  -ig).
```


## [2026-09-14T01:57:18.832Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==735{print NR}' KLN_1966.txt >/dev/null; for n in 733 734; do echo \"=== leaf $n first/last ===\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1{print}' KLN_1966.txt | head -3; echo \"....\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1{print}' KLN_1966.txt | tail -3; done",
 "description": "Show KLN leaf boundaries"
}
```


### [2026-09-14T01:57:19.831Z] TOOL RESULT

```
=== leaf 733 first/last ===
s’,  fr.  Samnium,  which  prob.  stands for  *Sabniom  and  is  rel.  to  Sabinus,  ‘Sabine’. See  Sabine  and  subst.  suff.  -ite.
Samoan,  adj.,  pertaining  to  Samoa;  n.,  an  inhabi¬ tant  of  Samoa.  —  Formed  with  suff.  -an  fr. Samoa,  name  of  a  group  of  islands  in  Polynesia. Derivative :  Samoan,  n.,  an  inhabitant  of  Samoa. Samolus,  n.,  a  genus  of  plants,  the  brookweed (bot.)  —  L.  samolus,  ‘brookweed’,  prop,  ‘a  sum¬ mer  plant’,  fr.  Gaul.  *samos,  ‘summer’,  whence also  L.  samauca,  name  of  a  fish.  Cp.  samara, samovar,  n.,  a  Russian  tea  urn.  —  Fr.  Tatar  sana- bar,  ‘tea  urn’,  altered  by  folk  etymology  into Russ,  samovar,  ‘self-boiler’,  fr.  samo,  ‘self’,  and varit',  ‘to  boil’.
Samoyed,  Samoyede,  n.  and  adj.,  name  of  a  Si¬ berian  people.  —  Russ.  Samoyed,  lit.  ‘self¬ eaters’,  used  in  the  sense  of  cannibals,  a  name given  them  by  the  Russians  (the  native  name  of the  people  is  Nenets).  For  the  first  element  in Samoyed  see  same.  The  second  element  is  cogn. with  Gk.  28siv,  L.  edere,  Goth,  itan,  OE.  elan, ‘to  eat’ ;  see  eat.
....
sang-de-boeuf,  n.,  deep  red  color  found  in  old Chinese  porcelain.  —  F.  sang-de-bauf,  lit.  ‘bul-
i  not
lock’s  blood’.  F.  sang,  ‘blood’,  
=== leaf 734 first/last ===
derives  fr.  VL. sanguem.  See  prec.  word.  F.  de,  ‘of,  from’, comes  fr.  L.  de,  ‘from,  away  from’;  see  de-.  F. beeuf,  ‘ox,  bullock’,  comes  fr.  L.  bovem,  acc.  of bos;  see  bovine.
sang-froid,  n.,  presence  of  mind,  composure.  — F.,  fr.  MF.,  lit.  ‘cold  blood’.  For  the  first  ele¬ ment  see  sanguine  and  cp.  prec.  word.  F.  froid, ‘cold’,  derives  fr.  L.  frigidus;  see  frigid.  The word  sang-froid  was  introduced  into  English  by Lord  Chesterfield  (1694-1773). sangrado,  n.,  an  ignorant  physician.  —  After Doctor  Sangrado,  a  character  in  Le  Sage’s  Gil Bias.  The  name  is  connected  with  Sp.  sangrador, ‘bloodletter’,  fr.  sangrar,  ‘to  let  blood’,  fr.  san¬ gre,  ‘blood’.  See  sangaree. sangrail,  sangreal,  n.,  the  holy  grail.  —  Refash¬ ioned  fr.  OF.  saint  graal,  ‘the  holy  grail’,  after L.  sdnctus,  ‘holy’.  See  saint  and  grail, sangui-,  combining  form  meaning  blood.  —  L. sangui-,  fr.  sanguis,  ‘blood’.  See  sanguine, sanguification,  n.,  the  conversion  of  food  into blood.  —  Compounded  of  sangui-  and  fication. Sanguinaria,  n.,  a  genus  of  plants,  the  bloodroot {hot.)  —  ModL.,  fr.  L.  sanguinaria  herba,  ‘a  herb that  stanches  blood’,  fr.  sanguis,  gen.  sanguinis, ‘blood’  (see  sanguine) ;  so  called  from  the  color of  the  juice.
sanguinary,  adj.,  bloody.  — •  L.  sanguinarius,  ‘per¬ taining  to  blood’,  fr.  sanguis,  gen.  sanguinis, ‘blood’.  See  sanguine  and  adj.  suff.  -ary. Derivatives:  sanguinari-ly,  adv.,  sanguinari-ness, n.
....
sapodilla,  n.,  an  evergreen  tree,  Achras  zapota.
Sp.  sapotilla,  zapotilla,  dimin.  of  sapota,  zapota. See  Sapota.
saponaceous,  adj.,  soapy.  —  Formed  with  suff. -aceous  fr.  L.  sapo,  gen.  saponis,
```


## [2026-09-14T01:57:28.111Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nimport re\n# map line -> leaf\nleaves=t.split('\\f')\ndef leafof(sub):\n    for i,l in enumerate(leaves):\n        if sub in l: return i\nfor s in ['sans,  prep.,  without','sine,  prep.,  without','sinciput']:\n    print(repr(s), 'leaf', leafof(s))\ni=t.find('sinciput')\nprint(t[i-3000:i+200])\nEOF",
 "description": "Locate sincere entry in Klein"
}
```


### [2026-09-14T01:57:29.440Z] TOOL RESULT

```
'sans,  prep.,  without' leaf 734
'sine,  prep.,  without' leaf 768
'sinciput' leaf 134
k.  — Shortened  fr.  capriole  (q.v.)
Derivatives:  caper,  n.,  caper-er,  n.,  caper-ing, suff.  adj.,  caper-ing-ly ,  adv. caper,  n.,  a  privateer;  its  captain  (hist.)  —  Du. kaper,  fr.  kapen,  ‘to  seize’,  which  prob.  derives fr,.  Fris.  kdpia,  ‘to  buy’,  used  euphemistically  in the  sense  ‘to  take  away’,  fr.  kap,  ‘purchase’,  a euphemistic  term  for  ‘piracy’.  Fris.  kap  is  rel. to  MDu.  coop,  Du.  koop,  OHG.  koitf,  ON.  kaup, etc.,  ‘purchase’.  See  cheap,  n. caph,  kaph,  n.,  name  of  the  nth  letter  of  the Hebrevv  alphabet.  —  See  kaph. capercailzie,  also  capercaillie,  n.,  the  largest grouse,  Tetrao  urogallus.  —  Gael,  capulcoille, lit.  ‘horse  of  the  woods’,  fr.  capul,  ‘horse’  and coille,  ‘wood’.  Gael,  capul  is  borrowed  fr.  L. caballus,  ‘horse’.  See  cavalry, caphar,  n.,  a  toll  levied  by  the  Turks  upon  travelers for  protecting  them  (obsol.)  —  Fr.  Arab,  kha- fdrah,  ‘protection’,  fr.  khafara,  ‘he  protected’, capias,  n.,  a  writ  of  arrest  (law).  —  L.,  ‘thou mayest  take’,  2nd  person  sing.  pres,  subjunctive of  capere,  ‘to  catch,  seize,  hold'.  See  captive, capillaire,  n.,  the  maidenhair  fern.  —  F.  capil- laire ,  fr.  L.  herba  capillaris,  ‘the  maidenhair’,  fr. capillaris,  ‘pertaining  to  the  hair’,  fr.  capillus. See  capillary.
capillarity,  n.,  the  property  of  exerting  capillary attraction.  —  F.  capillarite,  fr.  L.  capillaris.  See next  word  and  -ity.
capillary,  adj.,  hairlike;  n„  a  very  thin  blood vessel.  —  L.  capillaris,  ‘pertaining  to  the  hair’, fr.  capillus,  ‘hair’,  which  is  prob.  rel.  to  caput, gen.  capitis,  ‘head’.  See  capital,  adj. capistrate,  adj.,  hooded.  —  L.  captstratus,  pp. of  capistrare,  ‘to  halter',  fr.  capistrum,  ‘halter’, fr.  capere,  ‘to  catch,  seize,  hold’.  See  captive  and adj.  suff.  -ate  and  cp.  capstan, capital,  adj.  —  F.,  fr.  L.  capitalis,  ‘pertaining  to the  head,  capital,  chief,  first’,  formed  with  suff. -dlis,  fr.  caput,  gen.  capitis,  ‘head’,  fr.  I.-E. *qap-ut,  whence  also  OI.  kaput-,  ‘head’,  in  ka- pucchalatn,  ‘hair  of  the  hind  part  of  the  head’, Goth,  haubip ,  OE.  heafod ,  ‘head’.  Cp.  I.-E. *qap-elo-  in  OI.  kapilam,  ‘skull,  potsherd,  dish,
it
i *  ■
H
-
& . *  \
lid’,  kapalt-,  ‘mendicant’s  bowl’.  See  head  and  cp. capital,  ‘principal’,  capital,  ‘head  of  a  column’, and  chief.  Cp.  also  achieve,  ancipital,  biceps, cabildo,  cabotage,  cadet,  camail,  camouflage,  Ca- pito,  cap-a-pie,  cape,  ‘promontory’,  capitan,  ca¬ pitation,  capitellum,  Capito,  Capitol,  capitulate, caporal,  capot,  caprice,  captain,  cater,  ‘to  provide food’ ;  cattle,  caudillo,  cavesson,  chabot,  chapiter, chapter,  chef,  chevet,  chieftain,  corporal  (mil.),  da capo,  decapitate,  kerchief,  mischief,  muscovado, occiput,  precipice,  precipitant,  precipitate,  quadri¬ ceps,  sinciput,  triceps.  Cp.  also  capillary. Derivatives:  capital,  n.  (q.v.),  capital-ly,  adv. capital,  n.,  stock  of  money,  principal.  —  Late  L. capitate,  ‘property’,  prop.  neut.  of  th
```


## [2026-09-14T01:57:41.070Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==769' KLN_1966.txt | grep -o \"sincere[^$]\\{0,900\\}\" | head -2; echo \"=== page numerals leaves 733-735 ===\"; for n in 733 734 735; do echo \"-- $n --\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1{print}' KLN_1966.txt | grep -oE \"\\b14[0-9][0-9]\\b\" | head -5; done",
 "description": "Get Klein sincere entry and page numerals"
}
```


### [2026-09-14T01:57:42.358Z] TOOL RESULT

```
sincere,  adj.  —  MF.  (=  F.)  sincere,  fr.  L.  sincerus.
sincere’,  which  is of  uncertain  origin.  It  possibly  stands  for  sine *cera  in  the  sense  of  sine  carie,  ‘without  decay’. For  the  first  element  see  sine,  ‘without’.  The  sec¬ ond  element  is  cogn.  with  Gk.  Kfjp,  ‘the  goddess of  death;  doom,  destruction’,  XYjpalvctv,  ‘to harm,  destroy’,  ax7)paTo?,  ‘unhurt’,  L.  caries, ‘decay,  rottenness’.  See  caries  and  cp.  cerauno-. Derivatives:  sincere-ly,  adv.,  sincere-ness,  n., sincerity  (q.v.)
=== page numerals leaves 733-735 ===
-- 733 --
-- 734 --
-- 735 --
```


## [2026-09-14T01:58:10.240Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"serif\" KLN_1966.txt | head -5; echo \"=== leaf of sanserif ===\"; python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i,l in enumerate(leaves):\n    if 'serif' in l: print('leaf',i, l[l.find('serif')-300:l.find('serif')+200].replace('\\n',' ')[:500]); break\nEOF",
 "description": "Find serif in Klein"
}
```


### [2026-09-14T01:58:11.346Z] TOOL RESULT

```
7039:Cerion,  n.,  a  genus  of  snails  (zool.)  —  Gk.  x^ptov, ‘honeycomb’,  fr.  >0] po?,  ‘beeswax’.  See  cere,  n. ceriph,  serif,  n.,  a  horizontal  line  at  the  top  or bottom  of  a  capital  letter.  —  Prob.  fr.  Du. schreef,  ‘stroke,  dash’,  which  is  rel.  to  schrijven, ‘to  write’,  fr.  L.  scribere.  See  scribe  and  cp. sanserif.
27600:Passeres,  n.  pi.,  an  order  of  birds  equivalent  to the  Passeriformes  (ornithol.)  —  ModL.  passeres , prop.  pi.  of  L.  passer,  ‘sparrow’.
27602:Passeriformes,  n.  pi.,  an  order  of  birds  (ornithol.)
27603:—  ModL.  Passeriformes,  lit.  ‘having  the  form  of sparrows’,  fr.  L.  passer,  ‘sparrow’,  and  -formis, ‘of  the  form  of’,  fr.  forma,  ‘form,  shape’.  See Passer  and  form,  n.
27604:passerine,  adj.,  pertaining  to  the  Passeriformes  or Passeres;  n.,  a  passerine  bird.  —  L.  passerinus, ‘pertaining  to  the  sparrow’,  fr.  passer.  See  passer and  -ine  (representing  L.  -inus). passibility,  n.  —  Late  L.  passibilitas,  ‘capability of  suffering,  passibility’,  fr.  passibilis.  See  next word  and  -ity.
=== leaf of sanserif ===
leaf 148 L.,  fr.  L.  cerintha,  cerinthe, ‘the  waxflower’,  fr.  Gk.  xyjoivIJo:,  ‘beebread’, which  was  prob.  formed  fr.  xvjpoc,  ‘wax’,  with suff.  -ivho;.  See  cere,  n. Cerion,  n.,  a  genus  of  snails  (zool.)  —  Gk.  x^ptov, ‘honeycomb’,  fr.  >0] po?,  ‘beeswax’.  See  cere,  n. ceriph,  serif,  n.,  a  horizontal  line  at  the  top  or bottom  of  a  capital  letter.  —  Prob.  fr.  Du. schreef,  ‘stroke,  dash’,  which  is  rel.  to  schrijven, ‘to  write’,  fr.  L.  scribere.  See
```


## [2026-09-14T01:58:11.366Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT hapta ===\"; grep -n \"hapta-\" BRT.txt | head -20",
 "description": "Grep Bartholomae for hapta"
}
```


### [2026-09-14T01:58:11.423Z] TOOL RESULT

```
=== BRT hapta ===
29265:•  j.  hapta-Dhätay-  Adj,  (auch  mask.) 'sieben  Hatay  umfassend,  siebenteilig',  von ^yasna-  (sd.  a;  Stverz.):  yastiasca  'nAaitis Y.57. 22;  —  yasntm  'nhäitSm  Y.41.Z usw. ;  —  yasnahe  •fsAütsi^  Vr.  ly.  1  usw.
```


## [2026-09-14T01:58:18.643Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== BRT 'sieben' ==\"; grep -n \"'sieben'\" BRT.txt | head -20; echo \"== BRT Siebzig ==\"; grep -n \"Siebzig\\|siebzig\" BRT.txt | head -10; echo \"== BRT hanar ==\"; grep -n \"hanar\" BRT.txt | head -10",
 "description": "Grep Bartholomae for seven/seventy/hanare"
}
```


### [2026-09-14T01:58:18.744Z] TOOL RESULT

```
== BRT 'sieben' ==
29251:•  j.  (,  g.)  hapta  indckl.  Zw.  'sieben':  h° (als  Nom.)  hffiti  hqminö  maT?hs  V.  /.  3 PUZ.;  16.  9,  10,  N.  i02;  —  h°  attush  spinla YL  2.  la;  y.  83»,  Yd.  J^;  —  aee  strSus  . . yOi  °ta  haptoiringa  S.2. 13;  —  h'  (als Akk.)  sartTjü  V./5.4S;  ig-^t;  — yS  h° A?ndu(sA.)  V.r.  18;  —  h'  karhqn  Yt <V.4o,  /0.8s,  ^9- 82;  5-30.  Ä33,  /0.64,  89, r^.94,  rp.Sa,  Y.Ör.s,  65.5,  F. 5;  —  biS h'  nmana  "zweimal  sieben  Häuser"  V. 1$.  45;  14.  i6-i;  —  bis  h'  a^rJ  dax/fym''' V.  14.  6;  —  A'  sata  upäzananqm  V.  4. 13; 13,  Yt^.  30;  —  h'  (alslnstr.)  saläis  Aaha.- eihanqm  V.  4.  7.
30076:•  j.  bindav-,  h«ndav-",  p.  hi°dav-  m. Name  eines  Lands,  Indien:  II  imä  dahyava^ tyä  adam  agarbäyam  . ,  'du/  D.  5.  3 ;  5.  2 ; —  Aaca  us'as/ara  'dva  avi  daolastanm 'dum  V.J.  r8  PiiZ.;  —  yH^i  ulastaire •dvS  *ägiurvayeiii  yatSt  daoiataire  niytu "auch  wenn  er  im  Östlichen  Indien  ist, er  packt  (ihn);  auch  wenn  er  im  west- lichen ist,  er  schlägt  (ihn)  nieder"  Y. 57.  2g.  a)  mit  Aapla  'sieben'  dn.: paniadasfm  asunhamca  . .  frä'^wirtsfm  . , yS  Aapta  'du  (AP.)'»  V.  /.  i8.
== BRT Siebzig ==
== BRT hanar ==
3356:•  g.  a-drujyant-  Adj.  'trügeriscli,  arglistig, böslich  handelnd  (gegen  — )':  hanara  .  . vastryehyä  asnanhö  pas^ul  virlalcJ  "yants "ohne  Gewalttat  an  des  Bauern  Tieren und  Leuten,  der  (ihm)  doch  kein  Arg tut"  y.  j;.  15.
6253:7;  benutzt  G.j.6,  Vr./Äa,  V.28-,  —  taca .  .  'säum  Mi  (sd.)  yä  xl  ctia  vahisiä hanar»  '^wahtnst  zaosät  dr)gvä  haxiaitl (sd.)  Y.47.S;  —  tat^  %wahmt  *J  dam (sd.)  nipanhe  manS  voha  urunasüä  'säunqm ..  at..  dr?g7-atif  aiäi/ :ifarfhai/ (sd.) paiil urvqnö  paityeintl  Y.4t}.io{.;  zT,  benutzt 42.4;  — yä  ihids  dadiiti? ditiranam  (sd.) Aa^ä  'iäuniS y&scä  ..  dr.'gvS.dfbyd\.3i.i4;
11697:•  g.  Jyätav- :y>T/»-''  m.  'Leben':  talclt ma  mSnndm  (sd.)  JyStüm  Y.  J2.  11;  — ySi  gSus  mBrmdm  urvSxs.uxl{{&A^  jyötüm Y.J2. 12;  —  dus.sasti!  .  .  mSrindai  (sd.) .  .  jyatSus  .  .  xratOm  Y.  J2,  9 ;  —  yastim xia%raf  .  .  msi^at  (sd.)  jyätSui  vä  Y. 46- a;  —  ys  is  fymiä  hlmi^yai  (sd.) vas7.itSiscä  Y.  5^.  9 ;  —  avais  aibl  ying dairüT  nSitjyätJm  xiayamnfng  vasS  "durch die  (gerade),  die  sie  nicht  nach  Gefallen über  ihr  Leben  schalten  lassen"  Y.^2. I S-  2)  'Lebensunterhalt' :  y!  nsitjyötäm hanarf  (sd.)  vinastJ . .  "der  seinen  Lebcns- miterhalt  nicht  findet  ohne  .  ."  Y._j/.  15.
16667:i)  'Anteil  haben  an  — ,  inne  haben; Anteil  nehmen  an  — ,  bekommen',  mit Akk.  oder  Gen.:  nöil  .  .  avsstryö  .  . Aum»rjtsis{sd.)  baxs'täY. 31. 10;  —  tiuiasSt nSii  baxiaiti  vahiitahe  auhSus  "und,  wenn er  gestorben  ist,  wird  er  des  besten  Lebens nicht  teilhaftig"  V.5.61;  —  asäuni  cdis (sd.)   yä    il    cicä    vahistä     hanarp    (sd.)
19041:US  (Sp.  426  M.)  asraesyanam  tanunam  asahe  yS  n°  jyölämi^ä.)  hanar}  vtnasti . .  olnatshB .  .''vlZaiti'^  'S.  15;  N. ^2,  Nik.i;  —  «"  «S  . ,,  Y.^/.  15;  —  yöi  n*  aspm  mainyanta  (sd.) aSvan'  dva  n°*  ..asahe  tf  asayS  fräl3fiii'>  ■\.34-^\  —  yallam  n'  kvarstäis  vai  (sd.) (Sp.  360  u.)  V.44;  V.J5. 48»;  —  n°  na  duivarstä  ¥.49.4;  —  tacit  . .  ya  n°  va
29423:ai.  samärana-  n.  —  Vgl.  hanara-,  hamir>%a:  — ')  Stve«,  unter  'iar-,  Sp.  445  o.  und  unter lartanaiy.  —  ')  So  F  I ;  NA.  'nöia.  Elg.  **on der  Schlacht  hei'.
```


## [2026-09-14T01:58:29.460Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"hapt[aä]iti\\|haptai0i\\|hapta.dasa\\|haptadasa\\|haptaOa\\|haptaqa\" BRT.txt | head -10; echo \"== hanar headword ==\"; grep -nE \"hanar[a-zə»}9ȤÖ]+ *(Adv|Präp|Praep)\" BRT.txt | head -10; echo \"== Haraiva ==\"; grep -n \"Haröyüm\\|Haroyu\\|Haraiva\\|haröiva\\|Harôiva\\|haröyü\" BRT.txt KNT.txt | head -20",
 "description": "Grep BRT/KNT for haptaiti, hanare, Haraiva"
}
```


### [2026-09-14T01:58:29.566Z] TOOL RESULT

```
11042:—  im  jAw,  nur  beim  Zahlwort:  pancä/'a haptäitim  h.  3.  q,  12  (s,  dagegen  7 ;  Sp, 569  o.).  2)  die  Glieder  sind  verbal;  mit Tmesis:  m!ncä  T  [inaz\dazdäm  fsd.)  vafdd- dam  . .  Y.59.  5.  3)  bei  beiden;  b)  im Awf.;  i)  die  Glieder  sind  nominal;  a)  sie folgen  sich  unmittelbar:  uhi  kaurvascü amsritathscä  '^■34-  n;  32.  15;  —  van,ll haurvasca  ain»ntih'a  uva  SiPum^a  tar'- n^mca  Yt  /p- 96; —  *a:'a(ND.)  .  .  vyqsca vyänasca  Yty.  35;  —  twaSm  i^arfiimca vattnmca  Y.  55.  z ;  —  yais  ap3r»saH?m mazdiscä  zara^ultrascä  Y.  /2.  5 ;  —  at hv5  . .  Tsäcä    ataitilcä  Y.4^-5i  V.5. 53;
24456:•  g.,  j.  vispa.hUat-  Adj.  'alles  aus- spürend, wahlnehmend':  nSil  diwiaidyäi (sd.)  'äMias  (NS.)  ahurs  \.45-a;  — verwendet:  haptadasa  'a.hi^as{nixtA.ahmi) Yl  /.  8.
29253:•  j.  haptadasa-  Adj.  'der  siebzehnte':  °sa (statt  NSm.)  vJspa.hisas  (n^ml.  nama  ahmt) Yt  I.  8.
== hanar headword ==
== Haraiva ==
KNT.txt:1768:Haraiva-, Haldita-.
KNT.txt:1981:Akaufaciya ‘Men of Akaufaka’; Unarazmiy and -miš ‘Chorasmia’; Gadára ‘Gandaritis’; 8ata- gu’ Sattagydia’; Рала ‘the Daae’; Maka or ethnic Maciya; Saka or fem. бака Scythia’ or Хака ‘the Scythians’; Sug(u)da ‘Sogdiana’; Haraiva ‘Aria’; Hidus Sind’.
KNT.txt:3474:15 Qura : Arabaya : Mudraya : tyaiy : drayahya : Sparda : Yauna : Mada : Armina : Kat 16 patuka : Parfava : Zraka : Haraiva : Uvárazmiy : Bāxtriš : Suguda : Gadara : Sa
KNT.txt:4074:16 ka : Haraiva : Bāxtriš : Sug'da : Uv
KNT.txt:4214:DSe = Darius, Susa Е. 1 baga : vazraka : Auramazdà : hya : ima 2 т: bimim : adadé ; һуа : avam : as 3 татат : adadà : hya : martiyam : ad 4 ada : hya : &iyàülim : adad& : mart 5 iyahyü : hya : Darayavaum : XŠm : ak 6 unauš : айбат : parūvnām : XSm : a 7 шат : parüvnüm : framálàram : a 8 dam : Darayavaus : XS : vazraka : XS : XSy 9 anim : XS : dahyünám : vispazanü 10 nam : XS : ahyaya : bümiyà : vaz 11 rakàyà : düraiy : apiy : Vistas 12 pahyà : puça : HazamaniSya : Рат 13 sa : Pārsahyā : рисо : Ariya : Ari 14 ya : ciga : 08tiy : Dàrayavaus : XS : 15 уа&па : Auramazdaha : imá : dahy 16 āva : {уй : adam : agarbayam : apaia 17 ram : hacd : Parsa : adamsdm : pat 18 iyaxíayaty : manā : bajim : abara : 19 tyasam : hacéma : afahya : ava : aku 20 nava : datam : tya : mand : avadis : a 21 dáraya : Майа: Uja : Parðava : Haraiva : 22 Baatris : Suguda : Uvarazmis 23 : Zrdka : Наташайх : Bataguš : Maci 24 уй : Gadàra : Hidus : Зака : haumava 25 rgà : Saká : tigrazaudà : Babir 26 u$ : Авита : Arabéya : Мийгаа : 27 Armina : Katpatuka : Sparda : Yaun 28 à : аву : drayahya : ula : уа 29 y : paradraya : Skudra : Putayà : 30 Kuxiyd : Karka ; 6àtiy : Рата 31 yavau& : XS : vasiy : tya : duskarta 32 m : Gha : ava : naibam : akunavam : da 33 hyáva : ayauda : aniya : aniyam : 34 aja : ava : adam : akunavam : vašnā 39 : Auramazdaha : уаба : aniya : a 36 шуат : пау : jatiy : cind : gà 37 fava : kaSciy : astiy : дат : 38 tya : maná : haeá : avana : tarsat 39 y : улда : hya : tauviyd : tyam :s 40 kauéim : naiy : jatiy : naiy : vi 41 mardatiy : байу : Dérayavaus :
KNT.txt:4330:7 Üja : BabiruS : Авита : Arabya : Mudrüya : Sparda : 8 Yauna : Майа: Armina : Katpatuka : Parbava : Zraka : 9 Haraiva : Uvürazmi$ : Báxtri& : Suguda : Gadára : 10 8atagut : Harawvati$ : Hidus : Skudra : Yound : taka
KNT.txt:4576:21 : Haraiva : Baxtn$ : Sugda : Uvarazmi
BRT.txt:24647:yim  . ,  'rve  (DS.)  '>  V.  J5. 3 ;  13.11;  —  sünam ,  .  yim  .  .  'rvqmca  (GP.)  V.y.8;  —     us *iaHl  späna  fatmti  pasulAaurvamca  (sd) 'rvqmca  V.  jj.  43, Komp.:  vls-\-k;  eig.  Ma«  Hau»  beschüliend' S  304  II-  4S  No.  —  Bd.;  sak  i  mänpin.  RlT. sak  i  xäna.  —  Pü.:  Iransskr.  —  >)  NA.  anch ohoeTiennung;  zB.  V.  ^5.49  3.St.  —  OUnthem. S  4ti.  3  «■ •  j.  viä.harazana-  Adj.  'wo  die  Häuser verlassen  werden'{?)'>:  haröyüm  yim  'tarn V.i.S.
BRT.txt:29583:•  p,  haraiva-,  j.  haröiva-'>  m.  Name eines  Lands,  Aria:  II  ima  dahyäv^  tyä riiana  paiiyäisa'  .  .  "»u*  Bh.  /.  6;  D.  5.  2, Ö.  3;  —  x/tUm  asatfhqmca  . .  frai'W»r»s>m . .  'rSySm  yim  vis.hantam>n  (sd.)  V.  t.  8.
```


## [2026-09-14T01:58:48.693Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== KNT Haraiva lexicon ==\"; grep -n \"Haraiva-\" KNT.txt | head; echo \"== PHD haft ==\"; grep -n \"haft\\b\" PHD.txt | head -10; echo \"== PHD haft mackenzie ==\"; grep -n \"haft\" PHD_mackenzie.txt | head -10",
 "description": "Kent Haraiva and MacKenzie haft"
}
```


### [2026-09-14T01:58:48.774Z] TOOL RESULT

```
== KNT Haraiva lexicon ==
1768:Haraiva-, Haldita-.
== PHD haft ==
304:~ag LEI | N ~a] wand, arrow shaft.
388:h- [HWE- < A d hwh; h- | M h-] be (defective verb). !had [HWEt! ! = Av. Gat] now, then; that is (= à). *hàd [/?t!] a section of the Yasna. hàdamaàns?r [/Ptkmnsl = Av. hača.mādra-| those scriptures dealing with ritual matters. ~ig [-yk'] concerned with the above. - hādēxt [W#twht! = Av. hadaoxta-] certain scriptural texts; a particular sacrifice. haft [лб | M Apt, N ~] seven. ~ad [7o | M hpt'd, N ~] seventy. ~ag [-À! | N hafta] week. —šn [-”x!] the seven planets. haftàr [h5tl | (N kaftār !)] hyena. haftdah [%tdh | N ~, hifdah] seventeen. Haftóring [kftw(k)lng = Av. haptóiringa-] astr. the Great Bear. hagriz [hkic | M hgryc, N hargiz] ever; (with a negative) never. halag [Alz'] foolish, imprudent. ~th: folly, madness. halām [Pm | N ~] potted meat. halilag [hlylk' | N ~a] myrobalan. ham [hm | = M, N ~] also; same; v. 6. —ih: association, union, harmony. hamābēr [hm’fyl | M 72m°byr] storehouse. hamāģ [hm’k' | M Pwg, N hama] all. ~-dén [-dyn'] a complete religious ceremony. hamagih [hmkyh | N —i] totality, universality. hamahl [4(*)4[] = hamāl. hamāl [ml | N ~] equal, peer; comrade, hambadig [hmbtyk'] opponent, adversary. hambah-, v. *hambastan. hambāh-, ~išn, v. hambástan. hambān [hmb’n' | N anbán(a)] skin bag. hamband [hmbnd] connected. ~ih: connection. hamband-, —išn, v. 'hambastan.
851:arrow tigr; ~ shaft Cóbag.
2349:‘huzwarish’ uzwārišn. hyena haftār.
3142:planet abaxtar; the haftün.
3603:seven haft.
4808:sen murw sezd sézdén haftād*
== PHD haft mackenzie ==
164:der Preussischen Akademie der Wissenschaften (Berlin), 1933. i. 91-152,
1804: -ag [_kl I N -a] wand, arrow shaft.
2656:haft [hpt' I M hpt, N ] seven.
2658: .......ag [_kl I N hafta] week.
2660:haftar [hpt)i/ (N kafttir I)] hyena.
2661:haftdah [hptdh / N ......., hifdah] seventeen.
5969: anti- jud- i allti-demollic jud-dew.     arr(11) tigr; ,...., shaft U,hag.
6826:hyena haftir.                            impotent husk-kun.
7302:   haftan.                                    idan; -- out wextan.
7524: sectary kesdiir; Y. heretic.              seven haft.
```


## [2026-09-14T01:58:50.062Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== HRN haft ==\"; grep -n \"haft\" HRN.txt | head -20; echo; echo \"== HUB haft ==\"; grep -n \"haft\" HUB.txt | head -10",
 "description": "Horn and Hübschmann haft"
}
```


### [2026-09-14T01:58:50.165Z] TOOL RESULT

```
== HRN haft ==
36:und wissenschaftliches Vermögen dar, das häufig nur schwierig zu entdecken ist.
40:Google ist stolz, mit Bibliotheken in partnerschaftlicher Zusammenarbeit öffentlich zugängliches Material zu digitalisieren und einer breiten Masse
633:17. ärey 'Hass, Feindschaft*, rey,
714:Zweifelhaft, denn np. s passt nicht zu skr. g, aw. s;
1062:Jaba-Justi, sind wegen des t zweifelhaft); bei. als
1138:anhaftenden mythologischen Bedeutung (vergl. de
1339:ist wohl unzweifelhaft; päz. agar,
1468:angris 'Rechenschaft' (Hüb seh mann, Osset. Etym.
1592:'standhaft, zuverlässig*; phlv. östam bezw. tistäm
1634:ist mir zweifelhaft.- 33 -
1680:dem Begriff des 'Verbundenseins mit, des Anhaften«*
1844:\;i68. haften 'weben', baf, n^ND 'Garbe' (Jer. 9, 21).
1989:zweifelhaft.
2145:Ortschaft' 2).
2188:*) Phlv. vrejan ist nur fehlerhafte Schreibung; np. biristen ist
2358:arm. LW. bun 'Stamm (eines Baumes), Schaft*.
2535:haft ist; vergl. aber gr. xar«/, napai, vnai bei Homer
2553:bedeutet, ist sehr zweifelhaft; Sahn. I, 109 Vers 876
2915:Das Wort ist zweifelhaft und auch durch den von
2965:115, NB. ohne Stern) contrahirt sei, ist durchaus unstatthaft. Pärsä

== HUB haft ==
49:wissenschaftlich behandelt worden ist, hat jetzt Horn in
64:mit Mangeln und Fehlern behaftet ist, die bei langerer und
257:'anhangen, anhaften, hangen bleiben' = ap. hanj in
530:'bhdjin theilhaftig*), zd. baz 'zutheilen* gehoren. Das
569:riechend*, arm. LW. anoi§ wohlriechend, schmackhaft,
606:skr. ava-sthcL (ptc. avasthita- standhaft, zuverlassig') als
633:Geldner: *Genossenschaft' , nach Darmesteter;
729:'Seite, Pfeifenrohr* (Socin, a. a. 0.). Rathselhaft
847:Studien II, p. 19) Bauernstand, Bauernschaft*, dagegen
874:zweifelhaft".
```


## [2026-09-14T01:58:58.685Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== HRN sieben ==\"; grep -n \"'sieben'\\|,sieben'\\|sieben\" HRN.txt | head -10; echo \"== HUB sieben ==\"; grep -n \"sieben\" HUB.txt|head -6; echo \"== KNT Haraiva ctx ==\"; grep -n -A3 -B3 \"^Haraiva\\|Haraiva- \" KNT.txt | head -40",
 "description": "Horn/Hübschmann sieben, Kent Haraiva"
}
```


### [2026-09-14T01:58:58.793Z] TOOL RESULT

```
== HRN sieben ==
2555:249. hellten sieben', Praes. bez-em^ beziden^) ; perv&zen 'Sieb*.
2557:oder Worfeln aussondern'; päz. veytan sieben'.
2558:kurd. bltin 'sieben', bezink 'Sieb'; bei. gecag sieben',
9496:\A098. lieft 'sieben, hefte Woche'.
9497:aw. haptn 'sieben*; phlv. haß; ai. saptd; arm.
9516:sieben Throne* erklärt.
== HUB sieben ==
1103:249. Zu beoctan *sieben' (nach Noldeke *streuen) stellt
1107:sieben, Geiger, Etym. und Lautl. d. Afghan. Nr. 360.
3641:anlautendes h von haft 'sieben.
4387:*der siebente', paz. haftum Min. Gl. 96, Shk. 247 etc.; phi.
5466:zd. vahista-; bayo *Braut', skr. vadhu; bBxtan 'sieben = paz.
6551:np. /: haft *sieben' = zd. hapta, iran. *hafta, u. s. w. ;
== KNT Haraiva ctx ==
1765-Nisdya-, Parga-, Pirüva-, Früda-, Maka-, Mu-
1766-drüya-, Yauna-, Labanüna-, Sug(u)da-, Sku"za-,
1767-Skudra-, Sparda-, Zazüna-, Züzahya-, Zra*ka-,
1768:Haraiva-, Haldita-.
1769--ü- stems: A��urd-, Arbairü-, Arsada-, Izali-, Uyamá-, Kuganaké-, Téravd-, Tigrà-, Çüšā-, Yautiyd-, Yadà-, Raxá-, Ragà-.
1770--I- stems: Arakadri-, Küpisakàni-, Cicirri-, Cišpi-, Pütisuvüri-, Vispauzüti-.
1771--й- stems: Abirddu-, Ku"duru-, Babiru-, Màru-. $142. Roor Nouns AND ADJECTIVES, some of
```


## [2026-09-14T01:59:04.634Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '9494,9520p' HRN.txt; echo \"=== KNT Aria lexicon ===\"; grep -n \"Aria\\b\" KNT.txt | tail -15",
 "description": "Horn 1098 and Kent lexicon Aria"
}
```


### [2026-09-14T01:59:04.739Z] TOOL RESULT

```
LW. kuvd. liilän lassen, verlassen'; bei. Uar/^ llag,
n. üay 'lassen, verlassen, zulassen, erlauben' (165).
\A098. lieft 'sieben, hefte Woche'.
aw. haptn 'sieben*; phlv. haß; ai. saptd; arm.
evtn (H. No. 102).
kurd. LW. haft; dfy. öwa, aua; oss. d. aft, d. t.
au'd (43); wa/. hüby hub, nb, sar. üwd, §i/n. wuwd,
^ sangl. hof't, niinj. ed\ yayn. au.
X()99. Jiuft 'Schluck, Zug.
Nöldeke (mündliche Mitteilung) möchte nhd.
saufen, Suff, ahd. süfan 'schlürfen, trinken ver-
gleichen. Die Wurzel ist nach Kluge, Etymolog.
Wörterbuch s. v. noch nicht aussergermanisch nach-
gewiesen.
l/llOO. heftäd ^siebzig.
aw. haptäiti' 'siebzig; phlv. haftät; ai. saptati-,
kurd. hafte, heftt; af/. awiyä,
niOl. heftöreuff 'Grosser Bär (Sternbild)'^).
aw. haptöiringa- 'Grosser Bär; phlv. haftökrany
d. i. haftörani/ ; vergl. skr. lulga^ 'Kennzeichen' etc.
(Fick, Wörterbuch'^ I, 305).
Volksetymologisch von den Lexicographen als 'die
sieben Throne* erklärt.
i, 1102. Uenfi auch, zugleich*, als Praetix hem-^), hen- 'zu-
sammen, mit', vergl. behem 'zusammen'; em-, en-,
ap. harn- ; aw. hqm- etc. ; phlv. ham , ham^ ; ai.
sam-; arm. ham- (H. No. 154).
=== KNT Aria lexicon ===
1884:! In Cica-tazma- the prior element is not the bare Stem, but the stem with an added nasal, attested in the transliterations into Elam., Akk., and Greek. This nasal ean hardly be the acc. ease-ending (as tentatively sug- gested by Bthl. AiW 587); it seems unexplainable except as a transfer from some other ера, in which & nasal in this position was justified (Schulze, KZ 33.216.n3; Richter, IF 9.208-4; Foy KZ 37.504-5). Cf. Gk. 'Aprga- Bápys (Hdt. 1.114-6, 9.122; Aesch. Pers. 29, 302, 971) = OP *Artam-bara ‘Aria-upholder’, where the prior ele- ment seems to be in the accusative (ef, Stonecipher, Graeco-Persian Names 27).
1981:Akaufaciya ‘Men of Akaufaka’; Unarazmiy and -miš ‘Chorasmia’; Gadára ‘Gandaritis’; 8ata- gu’ Sattagydia’; Рала ‘the Daae’; Maka or ethnic Maciya; Saka or fem. бака Scythia’ or Хака ‘the Scythians’; Sug(u)da ‘Sogdiana’; Haraiva ‘Aria’; Hidus Sind’.
3564:$6. 1.12-7. Saith Darius the King: These are the countries which eame unto me; by the favor of Ahuramazda I was king of them: Persia, Flam, Babylonia, Assyria, Arabia, Egypt, (those) who are beside the sea, Sardis, Ionia, Media, Armenia, Cappadocia, Parthia, Drangiana, Aria, Choras- mia, Bactria, Sogdiana, Gandara, Scythia, Satta- gydia, Arachosia, Maka: in all, ХХИ provinces.
4089:§2. 5-18. Saith Darius the King: By the favor * 1 of Ahuramazda these are the countries which Ie got into my possession along with this Persian folk, which felt fear of me (and) bore me tribute: Elam, Media, Babylonia, Arabia, Assyria, Egypt, Armenia, Cappadocia, Sardis, Ionians who are of the mainland and (those) who are by the sea, and countries which are across the sea; Sagartia, Parthia, Drangiana, Aria, Bactria, Sogdiana, Chorasmia, Sattagydia, Arachosia, Sind, Gandara, Scythians, Maka. |
4111:§3. 15-30. Saith Darius the King: By the favor of Ahuramazda these are the countries which I seized outside of Persia; I ruled over them; they bore tribute to me; what was said to them by me, that they did; my law—that held them firm; Media, Elam, Parthia, Aria, Bactria, Sogdiana, Chorasmia, Drangiana, Arachosia, Sattagydia, Gandara, Sind, Amyrgian Scythians, Scythians with pointed caps, Babylonia, Assyria, Arabia, Egypt, Armenia, Cappadocia, Sardis, lonia, Scythians who are across the sea, Skudra, petasos-
4336:menia, Cappadocia, Parthia, Drangiana, Aria, Chorasmia, Bactria, Sogdiana, Gandara, Satta- gydia, Arachosia, Sind, Skudra, petasos-wearing Ionians, ...
4614:68. 18-28. Saith Xerxes the King: By the favor of Ahuramazda these are the countries of which I was king ... (= DNa 18-22) ; Media, Elam, Ara- chosia, Armenia, Drangiana, Parthia, Aria, Bac- tria, Sogdiana, Chorasmia, Babylonia, Assyria, Sattagydia, Sardis, Egypt, Fonians, those who dwell by the sea and those who dwell across the sea, men of Maka, Arabia, Gandara, Sind, Cappa- docia, Dahae, Amyrgian Scythians, Pointed-Cap Scythians, Skudra, men of Akaufaka, Libyans, Carians, Ethiopians.
```


## [2026-09-14T01:59:16.021Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('incoming/BQT/BQT_v4_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor p in pages:\n    m=re.search(r'\\[pdf page (\\d+)\\]',p)\n    if m and int(m.group(1)) in (423,424,425):\n        print('=====',m.group(1));print(p[:1800])\nEOF",
 "description": "Print BQT v4 pdf pages 423-425"
}
```


### [2026-09-14T01:59:17.186Z] TOOL RESULT

```
===== 423
[pdf page 423]
هه رنه
ثانی وکسر قوقافی وواو به‌تحتانی مجهول کشیده هینی ۲ < بفتح اول بروزن پلنگه,
وبشین نقطه‌دار زده , نام روز پنجم است‌ازخمسةٌ [ مردم بی‌سر وپا ومغلی راکویند.
مسترقةٌ قدی که رو زآخر سال فازسیان باشد. هش -بنم اول و ثانی وسکون واو :
هشته ۱ < بکس اول بر وزن ی بمعنی هوش و ذعن و عقل و زبرکی باشد 8 -
بمدنی گذاشته‌وقر و گذاشنه و رهاکرده وآویشته | وقلمه و حصار را نی زکقته‌اند .
۳ هفت هیکل رضوان ۲ - کناب هو ار ؟ - پا واو» بر وزن ومنی
: ۹ | هغیار است که نقیض بیهوش باشد .
از هعت بهشت است .
هشفیفل « بنتح اول واسکون نانی هشومند ۷ - بنم اول وفتح میم
و ای بتحتانی رسیده و فای دیگر مضموم ولام | بروژن کلوبند » بممنی هوشمند است که‌خداوند
ساکن.زردك سحراثی را کویند که شقاقل‌باشد۴ . | عقل واهوش و زیرکی باشد ؛ و بفتح اول هم
قوت باه دهد وشیر زنانرا هم زیادهکند . گقته‌اند .۴
۹ - اسم مفعول از «هشتن» (۸م.) ۴ - رضوان,نام‌فوشتهٌ موکل‌بهشت. وبهشت.
۴ - « هقفیقل , شقاقل است .> « تحفهٌ حکیم مومن . ۰
۴ - « هرد بی‌سر وین است » « صحاح‌الفری دخةٌ طاعتی » سروری کوید : « هشنگه
بروزن فرنگه » هردی بی‌سر وین باشد در لخةٌ وفائی » جهانگیری از سروری نقل کرده »
اما بجای بی سروبن » پی سر و پا نوشته ( در رشیدی هم هردابی سروپا آمده م.م. ) مأخذ همه
صداح‌الفری است که چون دیدند درخت بی سروین معنی درمتی نمیدهد درخت را تبدیل بمرد
کردند . مقصود سحاح تن درخت بربده است و ممکن است «.ان را مجازاً در هرد تثبل رت
استعمال کرد مثل کندء ناتراش » لیکن هیچکدام شاهد استممال لیاورد.(اند) . « فرهنکه‌نظام >.
8 - ر4: هون هش. ظاهراً امه «شومند (۸.م.) را مرکب‌از: هشو ۳ مند پنداشته‌اند
و هشورا بمعنی‌هوش گرفته‌اند ! - از : هش (* هوش) + وار (پسوند اتساف‌ودارندکی)
< هفیار ۳ هوشیار . ۷ از :هش (< هوش) +ومند 078284 ( مند » پوند
اتصاف و دارندگی ):
ز تخمی که کشتی درایین رودبار ترا داد ای ناهشومند » بار ‏
فردوسی طوسی « رشیدی >.
هثیار - بشم اول , از : هش ( ۳ هوش )۳ بار ( پوند دارندگی ) ۳ هوشیار -
هشیوار (هم.) رك : ه«وشیار .
2 هثیاری - ب
===== 424
[pdf page 424]
در هفت آختان
هشیدن ۱ » بکس اول وفتح دال بر ۱ هشیو ار ؟ - بنتح اول ۴ رواوبروزن
وزن اشیمن ۰ بمعنی گذاشتن وفرو گذاشتن ورها | خربدار » بممنی خردمند و عاقل وهشیار باشد؛
کردن - وآوبختن باشد ۴ . ۱ و جنم اول هم درست است. ۹
بیان باز دهم
در های هوز بافا مشتمل بر یکصد و شانزده لغت و کنایت
هف ۰ - بفتح ارلوسکون ثانی,کا رکاه اول, الدك خمکیرا کوبند که بند از ری بهم
جولاهیر| کوبند؛ و بستی‌شانهٌ جولاهیر| گفته‌اند. | رسد .
هفت ۱ . بفتح اول‌وسکون‌انی‌وفوقانی», هفت 7 با ه کنایه از هفت آسمان
مددی است معروف ۷ - و شم اول » هردمی است .
باشد ازآب و شراب و شربت و دوغ و امثال‌آن هفت‌اختان ‎٩‏ پم همزه, کنایه
که فروکشند و بش کی‌قرت کوبند ۸ - وبکس | از هفت کوکب اس ت که زحل و مشتری و مریخ
۹ هفتن (ه.م ) * هلیدن (ه.م.) ۴ ر4: ح۲ صفحة۲۳۳۸.
۴ هار (ه.م.) ۳ هوشیار (ه.م.) :
خرد یافت لختی و شد کاروان هشیوار و با هنگه و بسیاردان.
فردوسی طوسی « رشیدی ؟.
ورك : هشیواری . ۴ - بم اول » صحیح است . 2-8 هف , کارکاه جولاهی
باش دکه بفتری نیز گوبند .> ۸« سروری > ۰ ‎٩‏ - اوستا 383212 (هفت) . پپئوی 88۲ ,
هندی باستان 58018 ۰ ارمنی*6۷1 ؛ افغانی ۵۱۷4 , 2۷۷8 ؛ استی 211 ۰ 2۲۷ ؛ وخی‌تافاطه
طاناط , ط ؛ سربکلی 1۷۷6 ۰ غفنی ۳۷۷۹/۵ ؛ سنگلیجی 120۴1 ؛ منجی 6010 . بغنوییا2 .
« اسفق ۱*۹۸ ؛کردی ۵6۴1 (هفت) . 811 ۰ ۵81 ۰ 32۷ ؛ زازا 28۷۲ ؛ دوجیکی]65ظ
« ژابا ی ۸4۹ ۰ نیز استی 8۷6 43 . است ۱*۷ *. ۷ - مدد میان خش وهشت ءپنج
بعلاو دو + ۸ - نوند که ( چرصدا](3/1:۸۸۵ 00116856 ) 8۷1۳ ( قرت, جرعه ) را با
آلمانی عالی جدید 381168 ۰ 5105۲ » آلمانی عالی قدیم 80588 ( جرعه جرعة آشامیدن »
نوشیدن ) مقاسه میکند . ريشهٌ کلمه طبق ۷۷۵۲۸۵۲0۱6 312800108۰ , 8۴10806 بغیر
ژرمانی مرتبط نمی‌نماید «اسشق ۰۶۱۳۹۹ ‎٩‏ - جمع« اخت > (خواهر) عربی بسیاق فارسی.
۰ هشیواری - چم اول » از : هشیوار (ه.م.) ی (حاصل مصدر اسم معتی ) هه
هوشیاری ۳ هشیاری ؛ زب رکی ؛ خردمندی ۰ کاهی :
بروی وان کردن تعجیل به‌به کرد تعجیل بطب اندر باشد ز سبکساری
آهتگیی باید آنجا ومدارایی صد کونه‌عم
===== 425
[pdf page 425]
هلتادکفتی - ۳۸ -
وآفتاب و زهره و عطارد وقمر . باشد. ‎٩۴‏ هفت اژدها - کنایه انهفت ک و کب
+هفتاد کشتی - بنم کاف , کنایه از | است .
هفتاد علت است. کوبند امراضی که حیوادات را هفتآ سیا - کنابه از هفت فلك‌است
عرص میشود عفتاد ات ۱ که فلك زحل وفلك مشتری وفلك مریخ وفلك
هفتاد و دوشاخ - کنابه ازهفتاد | چرن ‏ ورن یبن ما با :
۳ آفتاب و فلك زهره و فلك عظارد و فلك قص
ودوقوم - وهفتاد و دو ترتیل قران - وهفتّاد ودو
ملت است. باشد. . :
هفناد ود و کشتی ؟ - پسمنیآخر هفت اصل «» کنابه از هفت طبقهٌ
هقتاد. ودوشاخ باشد که هفتاد رنوملت است(۱)# | ازمین است - و هفت اقلیم را نیزمهفت اصل
()چش:- هفتاد و دوکشتی ... هفتاد ودوملت است .
- هفتادکشتی (بکرکاف) ( قی: هفتاد و دوکشتی ) مراد هفتاد ود ملت عالم‌است:
خردمند کشتی چو در بانلهاد برانگیخته موج آزو تند باد
چو هفتاد کشتی درو ساخته همه .بادیانپا برافراخته
هیانه یکی‌خوب کشتیعروی برآراسته همچو چشم خروس
پیمبر پدو اندرون با علی همه اهل بیت ‏ لبی و وصی.
فردوسی طوسی « نظامی عروضی . چهارمقاله . طبع دوم نکارنده س ۷۹ *. رك : هفتاد ودوملت.

۲ - بکرکاف » رك : هفتادکشتی (ح۱) » هفتاد ودوملت .

هفت اختر - بفتح اول وچهارم وششم ؛ سبعةٌ سباره که درنظرقدما : قمن است وعطارد
و زهره » شمس و هریخ و امشتری و زحل :

وین هفت گوهران کدازان را سقراط باز بت بهفت اختر .
* ناصرخسرو بلخی . دیوان: ی ۱۸۹ *.
ر4 +حهفت کوهران .

۵ فاد - بفنح اول, اوستا 82011 (هفتاد ) » پهلوی 1281121 , هندی باسان
58018 . افغانی 812۸ « اسشق ۱۱*۰ ؛کردی 368 ( هفنتاد ‎ )‏ 6اطة . 82106 ۰
68 . ۳۸۶6 ؛ زازا 88۷۸۵ ؛ درجیکی ۳2۷42 « ژابا س ۶4۹ > ؛کبلکی 131184؛
صدد برایر هفت بار ده » پنجاه بعلاو پیت .

هااد و دوملت - بننح اول وکر میم وافتح لام مشدد : از : هفتاد و دو+علت
(ع) [بممتی دین و مذهب] ؛ هفتاد و دو دی ن که می‌پنداشتنددر کرة زمین وجود دارد : «مأمون
کفت:پیغامبر علیه‌السلام گفته است که «ستفرق امتی‌ائنی وسبعین فرقة, الناجی‌منها واحد > یعنی
آمتان من بعد از من «نتاد و دوگروه شوند . و رستگار از ایشان يك کر
```


## [2026-09-14T01:59:40.873Z] TOOL CALL #27: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg444.png"
}
```


### [2026-09-14T01:59:41.738Z] TOOL RESULT

```

```


## [2026-09-14T01:59:41.730Z] INPUT

[Image: original 2550x3300, displayed at 1546x2000. Multiply coordinates by 1.65 to map to original image.]


## [2026-09-14T01:59:59.798Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg444.png')\nprint(im.size)\n# serum persian box approx y 1300-1380 of 2000-display => scale 1.65\nim.crop((1500,2130,2000,2280)).resize((1500,450)).save('pg444-serom.png')\nim.crop((580,1520,1000,1650)).resize((1260,390)).save('pg444-sibum.png')\n\"; ls",
 "description": "Crop serom and sibum regions"
}
```


### [2026-09-14T02:00:01.192Z] TOOL RESULT

```
(2550, 3300)
391-top.png
394hi.png
394-zoom.png
400-bot.png
400-top.png
404-top.png
411-top.png
412-zoom.png
414-bot.png
417hi.png
417-top.png
417-zoom.png
421-top.png
428hi.png
428-zoom2.png
428-zoom.png
429hi.png
429-zoom.png
431-top.png
432-bot.png
436-full.png
afm74-420.png
afm76-421.png
agents.txt
ahd430.txt
beekes410.txt
bqt1328-ftr-437.png
bqt1328-hdr-437.png
bqt1328-top-437.png
bqt1330-top-437.png
bqt2123-fn-435.png
bqt390_436_foot.jpg
bqt390_436_top.jpg
bqt390_662_foot.jpg
bqt390_662_top.jpg
bqt390_n436.jpg
bqt390_n662.jpg
build2-434.py
build3-434.py
build-389.py
build-390.py
build-391.py
build393.py
build-394.py
build-395.py
build-396.py
build-398.py
build-400.py
build-401.py
build-405.py
build-406.py
build-407.py
build-412.py
build-414.py
build-415.py
build-417.py
build-418.py
build-419.py
build-422.py
build-425.py
build-426.py
build-428.py
build-429.py
build-430.py
build-431.py
build-434.py
build-435.py
build-438.py
c404-empty.png
c404-greek.png
c404-patil.png
c404-pest.png
c404-symp2.png
c404-symp.png
c412_cedar.png
c412_makrome.png
c412_makrome_zoom.png
c412_meqrameh.png
c412_meq_zoom.png
c412_sedr_zoom2.png
c412_sedr_zoom.png
crop14-394.png
crop18-394.png
crop411_a.png
crop411_b.png
crop411_c.png
crop419_a.png
crop419_b.png
crop419_c.png
crop419_d.png
crop419_grk.png
crop419_skt.png
crop428a.png
crop428b.png
crop428c.png
crop428d.png
crop-437.png
e0-434.json
edit_about.py
edit_research.py
ffprof
gen-420.py
irn-425.pdf
irn-425.txt
knt-440.txt
knt443.txt
meta-443-knt.json
pg390b.jpg
pg390b.png
pg390.png
pg391big.png
pg391crop.png
pg391.png
pg391root.png
pg391sog.png
pg392.png
pg393.png
pg394hi.png
pg394.png
pg397.png
pg398.png
pg399-crop1.png
pg399-greek.png
pg399.png
pg399-sog.png
pg400big.png
pg400_fa_heli.png
pg400_fr2.png
pg400_french.png
pg400_kasak2.png
pg400_kasak3.png
pg400_kasak.png
pg400.png
pg402.png
pg404hi.png
pg404.png
pg405.png
pg406.png
pg407.png
pg408-ampus.png
pg408-germ.png
pg408.png
pg409.png
pg410hi.png
pg410-k2.png
pg410-kadm2.png
pg410-kadm.png
pg410-persian.png
pg410.png
pg410-q2.png
pg410-qedam.png
pg411_300.png
pg411.png
pg412_hi.png
pg412.png
pg412_uhi.png
pg413.png
pg414-greek.png
pg414.png
pg415-emptybox.png
pg415hi.png
pg415.png
pg416-v.png
pg417.png
pg418hi.png
pg418.png
pg418-raj2.png
pg418-raj3.png
pg418-rajidan.png
pg419_hi.png
pg419.png
pg420b.png
pg420.png
pg421.png
pg422.png
pg423.png
pg424.png
pg426.png
pg428hi.png
pg428.png
pg429-crop1.png
pg429-crop2.png
pg429-crop3.png
pg429hi.png
pg429.png
pg431.png
pg432.png
pg433.png
pg435-n1.png
pg435-n4.png
pg435.png
pg436.png
pg437-437.png
pg437hi-437.png
pg438.png
pg443.png
pg444.png
pg444-serom.png
pg444-sibum.png
pg452.png
pg453.png
pg456.png
pg458.png
queue.txt
sem410.html
u_mak.png
u_meq.png
u_sedr.png
write397.py
write-402.py
write409.py
write410.py
write436.py
```


## [2026-09-14T02:00:04.250Z] TOOL CALL #29: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg444-serom.png"
}
```


### [2026-09-14T02:00:04.275Z] TOOL RESULT

```

```


## [2026-09-14T02:00:09.161Z] TOOL CALL #30: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg444-sibum.png"
}
```


### [2026-09-14T02:00:09.209Z] TOOL RESULT

```

```


## [2026-09-14T02:00:16.339Z] TOOL CALL #31: Bash

```json
{
 "command": "sed -n '1,40p' tools/fetch_source.py",
 "description": "Inspect fetch_source.py"
}
```


### [2026-09-14T02:00:16.385Z] TOOL RESULT

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


## [2026-09-14T02:00:18.494Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== MON سرم ==\"; grep -n \"سرم\" MON_part1.txt MON_part2.txt | head -10; echo \"== MON هرات ==\"; grep -n \"هرات\" MON_part1.txt MON_part2.txt | head -5; echo \"== BQT v4 هرات ==\"; grep -n \"هرات\" incoming/BQT/BQT_v4_pages.txt | head -5",
 "description": "Grep Mo'in and Borhan"
}
```


### [2026-09-14T02:00:18.603Z] TOOL RESULT

```
== MON سرم ==
MON_part2.txt:33:این کتاب به سرمایه‌گذاری آقای حمید اله‌بیگی و غلامرضا صابر به چاپ رسیده و 
MON_part2.txt:34:متعلق به سرمایه‌گذار می‌باشد و کلیه حق و حقوق کتاب مذکور محفوظ برای 
MON_part2.txt:494:باشد. زنی که به سبب سرمایةٌ خویش از 
MON_part2.txt:1320:غسرم: (.) هسر چه ادايش لازم 
MON_part2.txt:6599:فر مول: :0۲ (.) نمونه» سرمشق. رمر. 
MON_part2.txt:7560:اختلافی بین مقدار گرما و سرمای آن نقطه 
MON_part2.txt:7583:نتیجه سرما بیشتر می‌شود. بهار و پاییز واسطة 
MON_part2.txt:7585:سرما باشد» فصل را پاییز و اگر بعکس باشد 
MON_part2.txt:7795:سرمایه کار انجام نمی‌شود. 
MON_part2.txt:9004:دهان بیرون کنند. ورکك. سروری و سرمة 
== MON هرات ==
MON_part1.txt:34762:دارند؛ بول» شاشء زهرات؛» قاروره» ادرار. 
MON_part1.txt:41371:تظاهرات. 
MON_part1.txt:48826:گوهران» گوهرها؛ ج. جو اهرات. 
MON_part1.txt:49113:یک از احجار کریمه؛ ج. جواهرء جواهرات 
MON_part1.txt:71303:یدوردو پتاسیم موجب تظاهرات عوارض 
== BQT v4 هرات ==
2837:۲ - مرغاب ( بفتح اول) قربه‌ایست ازهرات وازقرای مالین - ونام نهری بمروشاهجان-
2838:و لهری بسره «ممجم‌البلدان» رك:می‌غاب- « مغ سپید » موضمی‌است درهرات. رك : چهار مقالةٌ
2884:۹ -رك : فقس . ۲ - موضعی است بحدود غور وهرات . حکیم سنائی گفته :
4694:در لفت تمیم مانند « متا » است از تافص در لغت غیرایشان » و کوبند من شرعاً وعرفا در هرات
8010:جوانی که بهرات میبود و پنهان از پدر شراب میخورد » پوشیده ازریحان خادم فرودسرای خلوتها
```


## [2026-09-14T02:00:28.188Z] TOOL CALL #33: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/sept%E1%B9%83\" \\\n \"https://en.wiktionary.org/wiki/sincerus\" \\\n \"https://www.etymonline.com/word/sincere\" \\\n \"https://www.etymonline.com/word/sans\" \\\n \"https://www.etymonline.com/word/serum\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 444, roots Sen 2 / Septm / Ser 1 verification\" ; done",
 "description": "Archive web sources batch 1"
}
```


### [2026-09-14T02:00:32.525Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/0903568449a371c0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/7ef155a301e09d31.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b7809040cea698f0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/12e8ab79c1f8c5bc.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/2c52576f62a76824.txt
```


## [2026-09-14T02:00:35.744Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 0903568449a371c0 7ef155a301e09d31 b7809040cea698f0 12e8ab79c1f8c5bc 2c52576f62a76824; do echo \"########## $f\"; head -c 2500 $f.txt | tr -s ' '; echo; done",
 "description": "Inspect archived pages"
}
```


### [2026-09-14T02:00:36.840Z] TOOL RESULT

```
########## 0903568449a371c0
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/sept%E1%B9%83
FETCHED: 2026-09-14T02:00:29Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found
########## 7ef155a301e09d31
URL: https://en.wiktionary.org/wiki/sincerus
FETCHED: 2026-09-14T02:00:31Z
STATUS: 200
TITLE: sincerus - Wiktionary, the free dictionary

sincerus - Wiktionary, the free dictionary 

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

 Search 

 Appearance 

 Donations 

 Create account 

 Log in 

 Personal tools 

 Donations 

 Create account 

 Log in 

 Contents

 move to sidebar 
 hide 

 Beginning

 1 
 Latin 

 Toggle Latin subsection 

 1.1 
 Alternative forms 

 1.2 
 Etymology 

 1.3 
 Pronunciation 

 1.4 
 Adjective 

 1.4.1 
 Declension 

 1.4.2 
 Derived terms 

 1.4.3 
 Descendants 

 1.5 
 References 

 Toggle the table of contents 

 sincerus 

 7 languages 

 Català 
 Español 
 Français 
 Magyar 
 Malagasy 
 ဘာသာမန် 
 Русский 

 Entry 

 Discussion 

 English 

 Read 

 Edit 

 View history 

 Tools 

 Tools

 move to sidebar 
 hide 

 Actions

 Read 

 Edit 

 View history 

 General

 What links here 
 Related changes 
 Upload file 
 Permanent link 
 Page information 
 Cite this page 
 Get shortened URL 

 Print/export

 Create a book 
 Download as PDF 
 Printable version 

 In other projects

 Appearance

 move to sidebar 
 hide 

 From Wiktionary, the free dictionary

 Latin
 [ edit ] 

 Alternative forms
 [ edit ] 

 syncerus ( Medieval Latin ) 

 Etymology
 [ edit ] 

 From Proto-Italic *senkairos , from Proto-Indo-European *sem- (compare Latin simplex , and Sanskrit सम ( sama , “ whole, together ” ) ) and *ḱer- ( “ grow ” ) (compare Sanskrit किर् ( kir , “ pour out ” ) ). According to De Vaan, the second part of the compound derives from the unattested adjective *caerus found in the first part of caerimōnia , which is also related to caelum ( “ sky ” ) . [ 1 ] However, this is problematic: the expected outcome of Proto-Italic *senkairos would be *sincīrus , since Proto-Italic /ai/ gives /iː/, not /eː/ under vowel reduction (as in occīdere ), and it is implausible that this word was imported from rural dialects of Latin which monophthongize /ai/ to /ɛː/, as in fēnum , without leaving any trace of the urban Latin development.

 Pronunciation
 [ edit ] 

 ( Classical Latin ) IPA ( key ) : [sɪŋˈkeː.rʊs] 

 ( modern Italianate Ecclesiastical ) IPA ( key ) : [sin̠ʲˈt͡ʃɛː.rus] 

 Adjective
 [ edit
########## b7809040cea698f0
URL: https://www.etymonline.com/word/sincere
FETCHED: 2026-09-14T02:00:31Z
STATUS: 200
TITLE: Sincere - Etymology, Origin & Meaning

Sincere - Etymology, Origin & Meaning 

 Search 
 Log in 

 Columns 
 Forum 
 Apps 
 Premium 

 Log in 

 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 Origin and history of sincere 

 sincere (adj.) 

 1530s, "pure, unmixed, unadulterated;" also "free from pretense or falsehood," from French sincere (16c.), from Latin sincerus , of things, "whole, clean, pure, uninjured, unmixed," figuratively "sound, genuine, pure, true, candid, truthful" (unadulterated by deceit), a word of uncertain origin.

 There has been a temptation to see the first element as Latin sine "without." But there is no etymological justification for the common story that the word means "without wax" ( *sine cera ), which is dismissed out of hand by OED, Century Dictionary ("untenable"), and others, and the stories invented to justify that folk etymology are even less plausible. Watkins has it as originally "of one growth" (i.e. "not hybrid, unmixed"), from PIE *sm-ke-ro- , from *sem- "one" (see same ) + root of crescere "to grow" (from PIE root *ker- (2) "to grow"). De Vaan finds plausible a source in a lost adjective *caerus "whole, intact," from a PIE root meaning "whole."
 also from 1530s 

 Entries linking to sincere 

 same (adj.) 

 "identical, equal; unchanging; one in substance or general character," from Proto-Germanic *samaz "same" (source also of Old Saxon, Old High German, Gothic sama , Old High German samant , German samt "together, with," Gothic samana "together," Dutch zamelen "to collect," German zusammen "together"), from PIE *samos "same," from suffixed form of root *sem- (1) "one; as one, together with."

 Old English seems to have lost the adjective except in the adverbial phrase swa same "the same as" (literally "so same"). But the word that emerged in Middle English as "the ordinary adjectival pronominal designation of identity" [OED] is considered to be more likely (or mostly) from the Old Norse cognate same , samr "same." In its revival it replaced synonymous ilk .

 As a pronoun, "the person or thing just mentioned," from c. 1300. In Middle English also a verb and an adjective, "together, mutually" (as in comen same "gather together, unite," kissen same "embrace one another").

 Colloquial phrase same here "the same thing applies to me" as an exclamation of 
########## 12e8ab79c1f8c5bc
URL: https://www.etymonline.com/word/sans
FETCHED: 2026-09-14T02:00:32Z
STATUS: 200
TITLE: Sans - Etymology, Origin & Meaning

Sans - Etymology, Origin & Meaning 

 Search 
 Log in 

 Columns 
 Forum 
 Apps 
 Premium 

 Log in 

 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 Origin and history of sans 

 sans (prep.) 

 c. 1300, sauns , saun , "without" (mid-12c. in surnames), from Old French san , sans , sen , senz (some of the forms with adverbial genitive -s ) "without, except, apart, not counting." This is cognate with Provençal senes , Old Catalan senes , Old Spanish sen (Spanish sin ), Old Italian sen , all from Vulgar Latin *sene , from Latin sine "without," an enlarged form of sed , se "without" (from PIE root *sen(e)- "apart, separated;" see sunder ).

 "A French word which has existed long in English without becoming naturalized; now archaic or affected, except as used in heraldry ..." [Century Dictionary, 1891]; OED writes that the words limited modern use is "chiefly with reminiscence of Shakespere," which it spells that way. In reference to fonts, by 1927, short for sans-serif . Sans souci , French, as an adverbial phrase "free from care, without care or concern," was the name of Frederick the Great's royal palace at Potsdam. 
 also from c. 1300 

 Entries linking to sans 

 sans-serif 

 also sanserif , "printing type without finishing cross-lines on the main strokes," 1830, from French sans "without" (see sans ) + English serif (1841), earlier ceref (1827). This is perhaps from Dutch and Flemish schreef "a line, a stroke," a noun related to schrijven "to write," a Germanic borrowing from Latin scribere "to write" (from PIE root *skribh- "to cut"). OED finds the Dutch and Flemish word "fairly suits the sense and form; but historical evidence is wanting, and the quasi-French form of sans-ceriph is not accounted for." Short form sans is by 1927.

 sunder (v.) 

 Middle English sonderen , "separate (two or more things) from each other," from Old English sundrian , syndrian "to divide, disunite in any manner." This is from the adjective and adverb sundor "separately, apart," which is from Proto-Germanic *sunder (source also of Old Norse sundr , Old Frisian sunder , Old High German suntar "aside, apart;" German sondern "to separate").

 This is from PIE root *sen(e)- "apart, separated" (source also of Sanskrit sanutar "away, aside," Avestan hanare "without," Greek ater "
########## 2c52576f62a76824
URL: https://www.etymonline.com/word/serum
FETCHED: 2026-09-14T02:00:32Z
STATUS: 200
TITLE: Serum - Etymology, Origin & Meaning

Serum - Etymology, Origin & Meaning 

 Search 
 Log in 

 Columns 
 Forum 
 Apps 
 Premium 

 Log in 

 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 Origin and history of serum 

 serum (n.) 

 1670s, "watery animal fluid," especially the clear pale-yellow liquid which separates in coagulation of blood in wounds, etc., from Latin serum "watery fluid, whey." This is held to be from PIE *sero- "flowing, liquid," from verbal root *ser- "to run, flow" (source also of Greek oros "whey, watery parts of curdled milk;" Sanskrit sarah "flowing, liquid," sarit "brook, river"). The word was applied by 1893 to blood serum used in medical treatments.
 also from 1670s 

 Entries linking to serum 

 Saar 

 river in western Germany, perhaps ultimately from PIE verbal stem *ser- "to run, flow" (see serum ). Related: Saarland , Saarlander .

 samsara (n.) 

 "endless cycle of death and rebirth, transmigration of souls," 1886, from Sanskrit samsara "a wandering through," from sam- , prefix denoting completeness (from PIE root *sem- (1) "one; as one, together with"), + sr- "to run, glide" (from PIE verbal stem *ser- "to flow;" see serum ).

 serology 
 serotonin 
 serous 
 strudel 
 See All Related Words (6) 

 Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 More to explore

 edema 

 also oedema, "excessive accumulation of serum in tissue spaces or a body cavity," c. 1400, idema, "a swelling filled with...

 soiree 

 "late, at a late hour," from serum "late hour," neuter of serus "late," from PIE *se-ro-, suffixed form of root *se- (2)...

 humor 

 mid-14c., "fluid or juice of an animal or plant," from Old North French humour "liquid, dampness; (medical) humor" (Old French humor, umor; Modern French humeur), from Latin umor "body fluid" (also humor, by false association with humus "earth"); related to umere "be wet, moist,"

 blood 

 Old English blod "blood, fluid which circulates in the arteries and veins," from Proto-Germanic *blodam "blood" (source also of Old Frisian blod, Old Saxon blôd, Old Norse bloð, Middle Dutch bloet, Dutch bloed, Old High German bluot, German Blut, Gothic bloþ), according to some s

 skill 

 early 12c., "knowledge, divine wisdom;" late 12c., "power of discernment, sound judgment;
```


## [2026-09-14T02:00:52.355Z] TOOL CALL #35: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/septm%CC%A5\" \\\n \"https://en.wiktionary.org/wiki/%D9%87%D9%81%D8%AA\" \\\n \"https://en.wiktionary.org/wiki/%D9%87%D8%B1%D8%A7%D8%AA\" \\\n \"https://en.wiktionary.org/wiki/%D8%B3%D8%B1%D9%85\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 444: Septm/Ser 1 Persian nodes (haft, Herat, serom)\"; done",
 "description": "Archive Persian/PIE wiktionary pages"
}
```


### [2026-09-14T02:00:55.937Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/7b8dfa6e67abb2a7.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/437b057b58f75f60.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d949634b8e77cacd.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d1ca278c6bff35d7.txt
```


## [2026-09-14T02:00:59.391Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 7b8dfa6e67abb2a7 437b057b58f75f60 d949634b8e77cacd d1ca278c6bff35d7; do echo \"########## $f\"; sed -n '1,6p' $f.txt; python3 - \"$f.txt\" <<'EOF'\nimport sys,re\nt=open(sys.argv[1],encoding='utf-8').read()\ni=t.find('From Wiktionary')\nprint(re.sub(r'[ \\t]+',' ',t[i:i+2200]))\nEOF\ndone",
 "description": "Inspect wiktionary pages"
}
```


### [2026-09-14T02:01:00.846Z] TOOL RESULT

```
########## 7b8dfa6e67abb2a7
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/septm%CC%A5
FETCHED: 2026-09-14T02:00:54Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Foundd
########## 437b057b58f75f60
URL: https://en.wiktionary.org/wiki/%D9%87%D9%81%D8%AA
FETCHED: 2026-09-14T02:00:54Z
STATUS: 200
TITLE: هفت - Wiktionary, the free dictionary

هفت - Wiktionary, the free dictionary 
From Wiktionary, the free dictionary

 See also: ہفت 

 Gilaki
 [ edit ] 

 Numeral
 [ edit ] 

 هفت ( haft ) 

 seven 

 Mazanderani
 [ edit ] 

 Numeral
 [ edit ] 

 هفت ( haft ) 

 seven 

 Persian
 [ edit ] 

 Etymology
 [ edit ] 

 From Middle Persian hp̄t' ( haft , “ seven ” ) , from Proto-Iranian *haptá , from Proto-Indo-Iranian *saptá , ultimately from Proto-Indo-European *septḿ̥ .

 Indo European cognates include Avestan 𐬵𐬀𐬞𐬙𐬀 ( hapta ) , Northern Kurdish heft , Ossetian авд ( avd ) , Pashto اووه ( uwə ) ), Sanskrit सप्त ( saptá ) , Urdu سات ( sāt ) , Hindi सात ( sāt ) , English seven , Latin septem , Ancient Greek ἑπτά ( heptá ) , etc.

 Pronunciation
 [ edit ] 

 Dari

 هفت 

 Iranian Persian

 Tajik

 ҳафт 

 ( Classical Persian ) IPA ( key ) : /ˈhaft/ 

 ( Dari, formal ) IPA ( key ) : [háft̪] 

 ( Dari, formal ) IPA ( key ) : [háft̪] 
 ( Kabuli ) IPA ( key ) : [ʔáft̪] 

 ( Hazaragi ) IPA ( key ) : [ʔáft̪] 

 ( Iran, formal ) IPA ( key ) : [hǽft̪ʰ] 

 ( Tajik, formal ) IPA ( key ) : [háft̪] 

 Rhymes: -aft 

 Readings

 Classical reading ? 

 haft

 Dari reading ? 

 haft

 Iranian reading ? 

 haft

 Tajik reading ? 

 haft

 Numeral
 [ edit ] 

 Persian numbers ( edit ) 

 70 

  ←  6 

 ۷ 
 7 

 8  →  

     Cardinal : هفت ( haft ) 
     Ordinal : هفتم ( haftom ) 

 هفت • ( haft ) ( Persian numeral ۷ ) 

 seven 

 Related terms
 [ edit ] 

 هفتاد ( haftâd ) 
 هفته ( hafte ) 
 هفت‌اورنگ ( haft-owrang ) 
 هفت‌سین ( haft-sin ) 

 Descendants
 [ edit ] 

 Judeo-Tat: ħoft 

 Retrieved from " https://en.wiktionary.org/w/index.php?title=هفت&oldid=92089928 "

 Categories : Gilaki lemmas 
 Gilaki numerals 
 Mazanderani lemmas 
 Mazanderani numerals 
 Persian terms inherited from Middle Persian 
 Persian terms derived from Middle Persian 
 Persian terms inherited from Proto-Indo-European 
 Persian terms derived from Proto-Indo-Iranian 
 Persian terms derived from Proto-Indo-European 
 Persian terms inherited from Proto-Iranian 
 Persian terms derived from Proto-Semitic 
 Persian terms derived from Proto-Afroasiatic 
 Persian terms inherited from Proto-Indo-Iranian 
 Persian terms derived from Proto-Iranian 
 Persian terms derived from the Proto-Indo-Europea
########## d949634b8e77cacd
URL: https://en.wiktionary.org/wiki/%D9%87%D8%B1%D8%A7%D8%AA
FETCHED: 2026-09-14T02:00:55Z
STATUS: 200
TITLE: هرات - Wiktionary, the free dictionary

هرات - Wiktionary, the free dictionary 
From Wiktionary, the free dictionary

 Ottoman Turkish
 [ edit ] 

 Etymology
 [ edit ] 

 Borrowed from Classical Persian هَرَات ( harāt ) , from Arabic هَرَاة ( harāh ) , from Middle Persian [Term?] ( /⁠harēw⁠/ ) .

 Proper noun
 [ edit ] 

 هَرات • ( Herât ) 

 Herat (a city in Afghanistan )

 Related terms
 [ edit ] 

 هَرَوی ( Herevî ) 

 Descendants
 [ edit ] 

 Turkish: Herat 

 Further reading
 [ edit ] 

 Redhouse, James W. ( 1890 ), “ 2162 ”, in A Turkish and English Lexicon ‎ [1] , Constantinople: A. H. Boyajian 

 Pashto
 [ edit ] 

 Pashto Wikipedia has an article on: هرات 

 Wikipedia ps 

 Etymology
 [ edit ] 

 Borrowed from Classical Persian هرات ( harāt ) , Borrowed from Arabic هَرَاة ( harāh ) , from Classical Persian هَریوْ ( harēw ) , from Middle Persian [Book Pahlavi needed] ( hlyb' /⁠harēw⁠/ ) , from Old Persian 𐏃𐎼𐎡𐎺 ( h-r-i-v /⁠haraiva⁠/ ) .

 Pronunciation
 [ edit ] 

 IPA ( key ) : [ha.rɑːt̪] 

 Proper noun
 [ edit ] 

 هرات • ( harāt ) 

 Herat (a city in Afghanistan )

 Persian
 [ edit ] 

 Persian Wikipedia has an article on: هرات 

 Wikipedia fa 

 Etymology
 [ edit ] 

 Borrowed from Arabic هَرَاة ( harāh , “ Herat ” ) , from Classical Persian هَریوْ ( harēw ) , from Middle Persian [Book Pahlavi needed] ( hlyb' /⁠harēw⁠/ ) , from Old Persian 𐏃𐎼𐎡𐎺 ( h-r-i-v /⁠haraiva⁠/ ) , from Proto-Indo-European *ser- ( “ to flow, run ” ) ; see also Avestan 𐬵𐬀𐬭𐬊𐬌𐬎𐬎𐬀 ( haroiuua ) .

 Compare Persian حمات ( hamât , “ Hamat ” ) , from Arabic حَمَاة ( ḥamāh ) .

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /ha.ˈraːt/ 

 ( Dari, formal ) IPA ( key ) : [hä.ɾɑ́ːt̪] 

 ( Dari, formal ) IPA ( key ) : [hä.ɾɑ́ːt̪] 
 ( Kabuli ) IPA ( key ) : [ʔä.ɾɑ́ːt̪] 

 ( Hazaragi ) IPA ( key ) : [ʔä.ɾɔ́ːt̪] 

 ( Iran, formal ) IPA ( key ) : [hæ.ɹɒ́ːt̪ʰ] 

 ( Tajik, formal ) IPA ( key ) : [hi.ɾɔ́t̪] 

 Rhymes: -aːt 

 Readings

 Classical reading ? 

 harāt

 Dari reading ? 

 harāt

 Iranian reading ? 

 harât

 Tajik reading ? 

 hirot

 Proper noun
 [ edit ] 

 Dari

 هرات 

 Iranian Persian

 Tajik

 Ҳирот 

 هرات • ( harât ) 

 Herat (a city in Afghanistan )

 Herat (a province of Afghanistan )
 ولایت هرات ― wilāyat-i harāt ― the province of Herat ,
########## d1ca278c6bff35d7
URL: https://en.wiktionary.org/wiki/%D8%B3%D8%B1%D9%85
FETCHED: 2026-09-14T02:00:55Z
STATUS: 200
TITLE: سرم - Wiktionary, the free dictionary

سرم - Wiktionary, the free dictionary 
From Wiktionary, the free dictionary

 See also: شرم 

 Arabic
 [ edit ] 

 Pronunciation
 [ edit ] 

 IPA ( key ) : /surm/ 

 Noun
 [ edit ] 

 سُرْم • ( surm )  m ( plural أَسْرَام ( ʔasrām ) ) 

 anus ; rectum ; lower end of the large intestine 

 Declension
 [ edit ] 

 Declension of noun سُرْم ( surm )

 singular

 basic singular triptote 

 indefinite

 definite

 construct

 informal

 سُرْم 
 surm 

 السُّرْم 
 as-surm 

 سُرْم 
 surm 

 nominative

 سُرْمٌ 
 surmun 

 السُّرْمُ 
 as-surmu 

 سُرْمُ 
 surmu 

 accusative

 سُرْمًا 
 surman 

 السُّرْمَ 
 as-surma 

 سُرْمَ 
 surma 

 genitive

 سُرْمٍ 
 surmin 

 السُّرْمِ 
 as-surmi 

 سُرْمِ 
 surmi 

 dual

 indefinite

 definite

 construct

 informal

 سُرْمَيْن 
 surmayn 

 السُّرْمَيْن 
 as-surmayn 

 سُرْمَيْ 
 surmay 

 nominative

 سُرْمَانِ 
 surmāni 

 السُّرْمَانِ 
 as-surmāni 

 سُرْمَا 
 surmā 

 accusative

 سُرْمَيْنِ 
 surmayni 

 السُّرْمَيْنِ 
 as-surmayni 

 سُرْمَيْ 
 surmay 

 genitive

 سُرْمَيْنِ 
 surmayni 

 السُّرْمَيْنِ 
 as-surmayni 

 سُرْمَيْ 
 surmay 

 plural

 basic broken plural triptote 

 indefinite

 definite

 construct

 informal

 أَسْرَام 
 ʔasrām 

 الْأَسْرَام 
 al-ʔasrām 

 أَسْرَام 
 ʔasrām 

 nominative

 أَسْرَامٌ 
 ʔasrāmun 

 الْأَسْرَامُ 
 al-ʔasrāmu 

 أَسْرَامُ 
 ʔasrāmu 

 accusative

 أَسْرَامًا 
 ʔasrāman 

 الْأَسْرَامَ 
 al-ʔasrāma 

 أَسْرَامَ 
 ʔasrāma 

 genitive

 أَسْرَامٍ 
 ʔasrāmin 

 الْأَسْرَامِ 
 al-ʔasrāmi 

 أَسْرَامِ 
 ʔasrāmi 

 References
 [ edit ] 

 Баранов, Х. К. ( 2011 ), “ سرم ”, in Большой арабско-русский словарь (Bolʹšoj arabsko-russkij slovarʹ) , 11th edition, Москва : Живой язык , →ISBN 

 Lane, Edward William ( 1863-1893 ), “ سرم ”, in Arabic-English Lexicon , London: Williams & Norgate. 

 Steingass, Francis Joseph ( 1884 ), “ سرم ”, in The Student's Arabic–English Dictionary ‎ [1] , London: W.H. Allen 

 The template Template:R:ar:Wehr-3 does not use the parameter(s): 1=سرم Please see Module:checkparams for help with this warning. Wehr, Hans ( 1960 ), “ سرم ”, in J. Milton Cowan, editor, A Dictionary of Modern Written Arabic , 3rd edition, Ithaca, NY: Otto Harrassowitz 

 Wehr, Hans ( 1979 ), “ سرم ”, in J. Milton Cowan
```


## [2026-09-14T02:01:16.443Z] TOOL CALL #37: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/sept%E1%B8%BF%CC%A5\" \\\n \"https://abadis.ir/fatofa/%D8%B3%D8%B1%D9%85/\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ser-\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 444: PIE septm, Persian serom, PIE ser- to flow\"; done",
 "description": "Fetch PIE septm, abadis serom, PIE ser-"
}
```


## [2026-09-14T02:01:19.740Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== AHD apart ==\"; grep -n \"Apart, separated\\|^sen-\\|^seni\" AHD_watkins1985.txt | head; echo \"== SYN seven ==\"; grep -n \"13.16\\|Seven\\b\" SYN.txt | head -8; echo \"== IEC septm ==\"; grep -n \"septm\\|septem\" IEC.txt | head -8; echo \"== IEC seni/sine ==\"; grep -n \"^sine\\|senī\\|seni-\" IEC.txt | head -8",
 "description": "AHD seni root, Buck seven, Mann"
}
```


### [2026-09-14T02:01:20.107Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/0133faf3fda8c0e6.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6caa01546759cb79.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9167be6b04c84557.txt
```


### [2026-09-14T02:01:20.232Z] TOOL RESULT

```
== AHD apart ==
916:tive verb *salbén in Middle Dutch salven, to anoint, salve, in obsolete Dutch guacksalver, a quack: QUACK- SALVER. [Pok. selp- 901.] sem-'. One; also adverbially “as one,” together with. I, Full-grade form *sem-. 1. Greek *hem- in: a. Greek heis (< nominative singular masculine *hen-s < *hem-s), one: HENDECASYLLABIC, HENDIADYS, HENOTHEISM; b. Greek he- in hekaton, one hundred (? dissimilated from *hem-katon; see dekm). 2. Suffixed form *sem-el- in Latin simul, at the same time: SIMULTANEOUS; ASSEM- BLE, ENSEMBLE. 3. Suffixed form *sem-golo- in Latin singulus, alone, single: SINGLE. 4. Compound *sem-per- (*per, during, for; see per’) in Latin semper, always, ever (< “once for all”): SEMPRE; SEMPITERNAL. II. O-grade form *som-. 1. Sanskrit sam, together: SAMSARA, SAN- DHI, SANSKRIT. 2. Suffixed form *som-o- in: a. Germanic *samaz, same, in Old Norse samr, same: SAME; b. Greek homos, same: HOMEO-, HOMO-; ANOMALOUS; Cc. Greek homilos, crowd: HOMILY. 3. Suffixed form *som-alo- in Greek homalos, like, even, level: HOMOLOGRAPHIC, HO- MOLOSINE PROJECTION. III. Lengthened o-grade form *s6m-. 1. Suffixed form *sém-i- in Germanic *sdmiz in Old Norse scemr, fitting, agreeable (< “making one,” “reconciling”): SEEM, SEEMLY. 2. Suffixed lengthened o-grade form *sém-o- in Russian sam, samo-, self: SAMIZ- DAT, SAMOVAR. IV. Zero-grade form *sm-. 1. Greek ha-, a-, together, in compound a-kolouthos, accompanying (a- + keleuthos, way, path): ANACOLUTHON. 2. Greek com- pound haplous, simple (-plous, -ploos, -fold; see pel-3): HAPLOID. 3. Suffixed form “smm-o- in Germanic *sumaz in: a. Old English sum, one, a certain one: SOME; b. Old English -sum, like: -soME!. 4. Suffixed form *syym-alo- in Latin similis, of the same kind, like: SIMILAR; ASSIMI- LATE, RESEMBLE. 5. Compound *sm-kéro-, of one grow- ing (see ker-3). 6. Suffixed form *sm-tero- in Greek heteros (earlier hateros), one of two, other: HETERO-. 7. Compound *srn-plek-, “one-fold,” simple (*plek-, -fold; see plek-), in Latin simplex, simple: SEMPLICE, SIMPLEX, SIMPLICITY. 8. Compound sym-plo-, “one-fold,” simple (*-plo-, -fold; see pel-3), in Latin simplus, simple: SIMPLE. 9. Extended form *syma in Greek hama, together with, at the same time: HAMADRYAD. 10. Basic form sm- in Old Russian si-, together, in compound siivéti (> Rus- sian sovet), assembly (véti, council; see weite-): SOVIET. [Pok. 2. sem- 902.] sem-2, Also sema-. Summer. Suffixed zero-grade form *sma-aro- in Germanic *sumaraz in Old English sumor, summer: SUMMERI. [Pok. 3. sem- 905.] sémi-. Half. 1. Germanic *sémi- in Old English sdm-, half: SAND-BLIND. 2. Latin sémi-, half: sEmI-. 3. Latin sémis, half: SESQUI-, SESTERCE. 4. Greek hémi-, half: HEMI-. [Pok. sémi- 905.] sen-', Old. 1. Latin senex, old, an elder: SEIGNIOR, SEN- ATE, SENECTITUDE, SENESCENT, SENILE, SENIOR, SENO- PIA, (SIGNORY), (SIR), SIRE, (SURLY). 2. Suffixed form *sen-o- in Germanic *senaz in compound “*sini-skalkaz, old servant (Germanic *skalkaz, servant, slave; see skalkaz), in Medieval Latin siniscalcus, seneschal: SEN- ESCHAL. [Pok. sen(o)- 907.] sen-2. Also seni-. Apart, separated. 1. Suffixed zero-grade form *sn-ter- in: a. Germanic *sundré in Old English sundor, sunder, apart: ASUNDER; b. Germanic denominative *sundrén in Old English syndrian, sun- drian, to put apart: SUNDER; Cc. Germanic derivative adjective *sundriga- in Old English syndrig, apart, separated: SUNDRY. 2. Zero-grade form *snni- in Latin sine, without (< “outside,” “out of’): SANS; SINECURE. [Pok. seni- 907.] sendhro-. Crystalline deposit. Germanic *sendra-, slag, in: a. Old English sinder, iron slag, dross: CINDER; b. Old High: German sintar (> German Sinter), slag: SINTER. [Pok. sendhro- 906.] sengw-. To sink. Germanic *sinkwan in: a. Old English sincan, to sink: SINK; b. Scandinavian intensive form
== SYN seven ==
13908:wm foul, skoulm 13 e, cord, etc., 1S & pa a ie words are mostly means a Pics denoting ‘tie, fasten’ cognate ee Pefnstening: The applica- Sa jump or protuberance in the body or on a tree is clearly secondary in at, nodus. For the Gme. group as @ whole the view that the latter sense 1s the earlier (cf, Paul, Deutsches Wtb. s.v. Knoten, “bedeutet urspriinglich ‘riind- liche Anschwellung an einem Gegen- stand’”) is favored by the nearest cog- nates like OHG knopf ‘knob, knot’, OF cnoll ‘hilltop’, etc. But in the history of OE cnotta—NIE knot, this sense is chronologically later (NED s.v. knot, sb!, 13-16) and for the prevailing earlier use, cf. the derivative OE cnytta ‘tie with a knot’ (NE knit). i Gre Guua (anything for tying, cov- a te opr),
23356:13.16 More
23561:924 SELECTED INDO-EUROPEAN SYNONYMS 13.16 MORE Grk. —-rAclwy, zAbwy Goth. managiza (maizo, Lith. daugiaus NG meptoadrepos mais adv.) Lett. vairak Lat. _pliis ON metri; fleiri (pl.) ChSl.  bolzjt, MUNOzZE;t, vedte It. pitt Dan. mer; flere (pl.) SCr. vide Fr. plus de Sw. mer; flere (pl.) Boh. _ vic(e) Sp. mas OE ma Pol. —- wiecej Rum. maz mult ME mo; more (sg.) Russ. _bol’Se Ir. mo; lia (pl.) NE more Skt. bhilyas-, bahutara- NIr. —tuilleadh; lia (pl.) Du. meer Av. Srayah- W. mwy OHG = mér, méro; manigiron Br. mut, mutoc’h (pl.)
23595:13.162. Words for the superlative ‘most’ generally go with those for ‘more’, as Grk. mdéicros beside mAciwv, Lat. plirimus beside plis, Goth. managists beside managiza, ON flestr beside fleiri, OE mé@st beside m4, etc.
24895:Above, Seven, vertoeven : Dan. igve, etc.,
25160:OHG iomér (iamér, iemér), MHG, NHG immer, fr. eo, io (= OF a, above) and mér ‘more’ (13.16), hence at first only with reference to fut. time, but ac- tually not so restricted. Weigand-H. 1.918. Kluge-G. 262.
25178:A times’ parallel to those for ‘three times’ | (13.44). Grk. woAddxis, with same suffix ¥ | as in zprdxs ‘three times’, NG zoAXés gopés, Fr. bien de fois, Sp. muchas veces, W. llawer gwaith, Br. alies (i.e. a lies) and lies gwech (lies ‘several’ : Ir. lia ‘more’, etc. 13.16), NE many times, etc. Most of these and other similar phrases are omitted from the list. Cf. also Ir. menic (below, 4).
== IEC septm ==
15220:septm (sequdm-) ‘seven’. Cf. seque, du ‘with two extra'?. Cf. sequdm Skt. saptá; Av. hapta; Per. haft; Arm. eawt'n; Tokh. A spät B sukt; Hitt. cf. septamas 'se- venth'; Gk. heptá; Lat. septem; Olr. secht; Li. septyni, Latv. septini. Cf. Alb. shtatë; W saith; Br. seiz and Cor. seyth. The ordinal of type *septomos arises in Skt. saptamah; Hitt. septamas; Lat. septimus; OPr. septmas. Variants in Gk. hébdomos & Li. sekmas; OCS sedmyj
15221:sequdm, sequdomos 'seven; seventh'. Vari- ant of type septm, q. v. Olr. cf. secht, Ir. seacht; Go. sibun, OS sibun, OE seofon; MHG siben, seben and suben; Du. zeven; Lux. zivon; OFris. sigun, siugun; Fris. saun; OCS (and Com. Sl.) sedmt Cf. further Oss. avd; Tokh. spat, beside sáptànt
17197:stepti-, variant of type septm (and *se- qudm-?) in W saith ‘seven’; Br. seiz, d: Alb. shtatë, id.; Olr. cf. secht, id. (fr. *sequt- ?)
== IEC seni/sine ==
```


## [2026-09-14T02:01:34.371Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('incoming/WLD/WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('npages',len(pages))\nfor i,p in enumerate(pages):\n    if re.search(r'seni-|sn̥ter|sept\\w{0,2}\\s*,?\\s*.?sieben|ser-\\s*,?\\s*.strömen', p):\n        m=re.search(r'\\[pdf page (\\d+)\\]',p)\n        print('---',i,m.group(1) if m else '?', p[:120].replace('\\n',' '))\nEOF",
 "description": "Locate Walde-Pokorny pages"
}
```


### [2026-09-14T02:01:35.436Z] TOOL RESULT

```
npages 725
--- 175 ?                                                     :                    :                 .         ;                  
--- 491 ?                                                                                                       ;                 
--- 492 ? 488                                             sem*   leicht (Petersson KZ. 47, 279)  arm. amal ^ausleeren, entladen“ {
--- 493 ?                                                       :                                         ;                       
--- 497 ?                                                              senii*         seii-                                       
--- 498 ? 494                              sen(o)      seni-,    senu-    (se^ii*),     s^-ter-    den);   e.    daizog Geratschaf
```


## [2026-09-14T02:01:38.595Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('incoming/WLD/WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (491,498,499):\n    print('=========== leaf',i)\n    print(pages[i][:2600])\nEOF",
 "description": "Print Walde-Pokorny leaves 491, 498-499"
}
```


### [2026-09-14T02:01:39.738Z] TOOL RESULT

```
=========== leaf 491
                                                                                                      ;




                                                             sep           sem>                                               487

sep- „mit innerer Anteilnahme etwas betreiben, besorgen'*.
     Ai. sdpati           „liebkosen,             umwerben,            riihren,    pflegen,     betreiben,             sich   um
etwas zu tun machen^S                          av. hap- (2. 3. sg. hafsl^ haptt) „(in der Hand) halten,
stiitzen^^; gr. -ejico                  (mit   di.i(pi~,           ecp-,          7ieQt-\   Aor. en-e-aTiov,             -otzeTv
„womit beschaftigt sein, besorgen, bereiten, bearbeiten'^ (Fick   138,561,
unter richtiger Trennung von          ^seq^-)\ onXov „Kustzeug, Werkzeug,
Gerat, Riistung, WafFen^S bnliix) „schirre an'S ojikojuai „bereite mir zu (die
Mahlzeit)^, onXi^oy „macbe zurecht. bereite zu, schirre an, riiste'^ (s. bes.
L. Meyer KZ. 23, 73 f.,                        Sommer Gr. Ltst. 99).                Yielleicht anord.              sefi,      ags.
sefa, as, seio „Sinn, Gemiit'^                                              Uhlenbeck PBrB.
                                                           got, sifan ,,frohlocken'‘          (s.

27, 130 f.); mit txpco,                   arm. e/m „koche'‘ ist aber keine glaubhafte Verbin-
dung herstellbar.
     Dazu idg. ^scpelib in ai. sdparyati „veneratur‘‘, ap. hapariya- „Ehrfurcht
bezeugen‘‘,             lat.       sepelio, -ire, sepiiltum            „begraben'‘ d. i. „venerare sepulcro^^
(Benfey, Sonne,                    s.                  KZ. 41, 335, und zur
                                        Bechtel Lex. 135,              ferner Schulze
altertiimlichen ^Bildung iiberhaupt auch Pedersen KZ. 39, 354 f.,; die ar.
Verba also nicht nach Hoffmann BB. 18, 287 und Prellwitz KZ. 47, 296
mit idg. r, und zu gr. vielleicht kypr. ejtEQQtoai' (ptXonov^oai, ineQioaev'
EfpeoTidoaro Hes., die wohl die Praep. ijzl als erstes Glied habenj.


septni „sieben^^
     Ai. saptd,          arm. evtn (Hiibschmann Arm. St. I 30, Arm. Gr.
                          av. hapta.
I 445),          lat.   eptcm,   cymr. usw. sadh (zum brit. bewahrten 5-
                                        air. seclit n-,

s. Pedersen KG. I 72), got. ahd. sihun, ags, scofon, anord. siau (zum laut-

lichen s. Brugmann II ^ 18; -n bewahrt nach einem neben "^sibun stehenden
sihimi\  ^-Yerlust im Ordinale scp\t\m-tos dissimilatorisch erfolgt; ob sep-
tun der Lex. sal. noch gesprochenes seftun oder Latinisierung eines echt
=========== leaf 498
494                              sen(o)      seni-,    senu-    (se^ii*),     s^-ter-



den);   e.    daizog Geratschaften^^,            woneben "^ivzvg                 ^,Zurustung,          Vollendung**
nach Schulze Qu. ep. 337 vorausgesetzt von ivzvco^ ivzvvco „mache fertig,
riiste zu, bereite^; neben to evzog steht ovv~hz')]g* ovvegyog Hes. und aM-
ivzrjg       eigener Hand vollbringend Morder Herr^^ (in der Bed. „M6rder‘‘
                                                       :
                                                                          ;            ;


aber vielleicht aus '^avzo^&€vz'i]g :'&8ivo}; s. Kretschmer Gi. 3, 289 f.: 4. 340;
Schwyzer aaO.).
   Lit. bei      Bechtel Lexil. 122f., 126f.


sen(o)-      :,alt“.

   Ai. sdna-^ av. liana- j^alt'*,          ai.   sanalcd- .,ehemalig,                  alt'^ (; lat.   senex^ frank.
sinigtis^ gall. Seneca)^  sanah ..vor alters'\ sana^ sandd^ sandta „Yon alters
her, von jeher, stets'*, sdnemi ,,im ganzcn Umfang, vollstandig“ (? s. Brug-
mann Total. 37 f.), sanatdna- „ewig, unvergiinglich, bestandig^^; arm. liana-
Xiaz ,.immer‘’ (s. auch Brugmann Total. 7f. Anm. 2 m. Lit.; dagegen got.
sdnteins „immerwahrend, taglich“ und lat. semper zu                     ,,eins’'), arm.

hin „alt** (Hiibschmann Arm. St. I 39; mit 2 t-Umlaut von e zu a nach M. E.
Schmidt KZ. 47, 189 f. lian^ g, Jianivoy ,,Gro6mutter^’) gr. svog „alt, vom                 ;


vorigen Jahre“, di^evog „zweijahrig^' (nicht nach Ehrlich Z. idg. Sprgesch. 75
zu "^sem- in ai. sdma ,,Jahr'', ahd. sumar „Sommer''), tvi] xal vea „der Tag
vor dem Keumond und der erste des beginnenden Monats^'; lat. senex^ senis
Komp. senior „alk bejahrk' (s. zur Flexion Brugmann AflL. 15, Iff.: senis
kons. flektiert nach jiivenis; ^weshalb die A:-Ableitung auf den X. sg. be-
schrankt ist, ist unklar). S€ 7 ieo^ -ere „alt, schwach sein'‘, sencsco, -ere ,,altern,
hinschwinden^^ sen item „ Alter, Betagtheit, korperliche Abnahme, zehrende
Gemiitsstimmung^*' (s. auch Vf. LEWb.“ u. so^iiutn)^ scnCitus, -fis (osk. gen.
senateis) .,Senat'', scnechis ,, Alter*, scneeio ..Erigeron^*                          ;
                                                                                            air. sen ,,alt'*,   acymr.
corn.           bret. lien „senex^%        Komp. air. shim, cymr. liyn (s. zuletzt Osthoff
MU. YI 280, Pedersen KG. I 377). gall. Seno-(piaUis u. dgl., Seneerr, got.
sineigs „7Tgeo^vrrjg'\ shilsta ,,altester‘S afrank. smi-sltalkus ,.der alteste Haus-
diener\ mhd. sen-ivnrz ,,senecio”, anord. sina ,,verwelktes Gras vom vorigen
Jahre'^ (F
=========== leaf 499
                                                                                                               :
                                                                                                               ;
                                                                                                               '




                                                 senq-   — sengyj-                                          495

besonders'', anord.   sundr „entzwei'', got. stmdro ,,fur sich, abseits, beson-
ders‘‘,    Adj. mhd. sunder^ hestmder^ nhd. besonder (Bugge BB. 3, 120)^);
   lat.   sme „ohne“ (wohl neutr.                         nachststehend dem ir. sain aus ''^Seni-
Ygl. MeilletEt. 153f., Vf.                  LEWb.^ 714f.);
   air. sain Adj.           „verschieden, besonders“                      cymr. giva-han ,,getrennt.
verschieden*' (gtvaJianu „trennen‘^), acymr. Jian „alium^^, cymr. hanred j.Ab-
trennung^^ (Fick II ^ 289    liber ir. cosnam „Streit“ und andere von Zupitza
                                        ;


KZ. 35, 265 angereihte Worte s. aber Pedersen KG. s. vv. cymr. Jia7wei\                  ;



corn. bret. banter „Halfte“ setzt Zupitza richtig                     =
                                                       gr. lasoog^ nur daB dabei
von idg. ^sm-tero- auszugehn ist, s, Anm. 2).
   Die Bed. „abgesondert, fiir sich“ laBt Verbindung mit dem Kefiexiv-
stamm "^'se-, ^s{e)iie- zu, vgl. mit Anl. sn- aksl. svene ^auBer, ohne'' und
ohne K-Formans anord. siii-virda „mi6achten“ (Koreen Lti. 219, Perssoii
IF. 2, 223, Solmsen Enters. 206, Yf. LEWb.^ 694 unter sed^ 714 unter sine)
und lat. sed, se Praep. „8ine, ohne“, Praef. „ohne, beseite".

senq- „brennen, dorren”.
  Ags. sejigan^ mnd. mhd. sengen ,.sengen‘* (^sangjan „brennen macheii”)
nd. sangeren ,,in der Haut prickeln^' (eig. „brennen”), alter ndl. sengeJ
„Funke% mhd. senge ,,Trockenheit, Durre'\ sine {^g-) ,.das Sengen“, snngen^
simJcen „anbrennen,                  versengt werden''. sungeln^ simlceln ,jknistern'% norw.
mdartl. sengra^ sengla ,,brenzlich riechen^‘, schwed. nidartl sjcmgla „sengen‘%
isl.    sangfir,      n.    sa^tgt ^versengt,         angebrannf';    ob auch          aisl.      s7a „Funke''
{senJiio7i)'^        Dazu wohl          abg. pYe-sgeiti^     isaeitl „trocknen''         (s.      auch   u. seq~
„abrinnen‘’),         sgcilo ..Ofen'',        russ.   izsjaldgj ,.trockeii*^     (deren Trennung von
slav. seh-^ sak- „flie6en‘*                 schon Miklosich EWb. 291 erwiigt                 i.



   Ygl. Zupitza Gutt. 205 (aber ap
```


## [2026-09-14T02:01:46.130Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('incoming/WLD/WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (501,502,503):\n    print('=========== leaf',i); print(pages[i][:1800])\nEOF",
 "description": "Walde-Pokorny ser- page"
}
```


### [2026-09-14T02:01:47.524Z] TOOL RESULT

```
=========== leaf 501
                                                             seudhro-, -a       —   ter-                                         497


sind ,,Gefahrte‘’, wozu n. ags. gesipp „Begleitung, Gefolge^', as. geslthi, nind.
{ge)sinde „Gesinde”., ahd. gisindi „Reisegefo]ge, kriegerisches Gefolge*\ nhd.
Gesinde, aisl. sinni „Gefolge“; ahd. sinnan (s. o.) auch ,,gehn, reisen,
wandern, kommen“; Kaus. got. sandjan, aisl. senda, ags. sendan, ahd. senien
„senden“       senda auch mit der ebenfalls aus „gehii lassen“ entw. Bed.
                   (aisl.

„toteii“)     ;   Denom. yon ^senpa- (s,o.) in aisl. simia, -ada und -7ita
                   ^’senpon
„reisen, sich worum kiimmern, beachten^’, as. sUhon, sldmi ,,gehn, ziehn,
Avandern^, ags. slpian                          ds.,    ahd.      smdon ds.
     Lit. shincin              ("^snntiii        ass,        zu                     siusti,     lett.   sahi,       siiVd .,senden.

schicken'* (bait,                im Red. -St.                     neben der Yollstufe von got. sandjau'. Lit.
bei Trautmann Bsl. Wb. 292j.
   Ygl. im allgemeinen Fick        562 (falsch iiber sa^idja^i 136 j, II^ 300. III^
430,   Falk-Torp  u. sind (Lit. iiber unhaltbare Kombinationen), Yf.            b.-                                        LEY
u. sentio, — Dt. smne^i nicht als sen[e\m- zu gr. vovq als '’^snouos, got. smitrs
,,weise‘‘         (s.   u.               ,.einen        kurzen Ruck geben'*}.

sendhro-, -a ,,geronnene, sich verdichtende Flussigkeit“.
  Serb.-ksl. sedry hrhvhnyje, russ.-ksl. sjadry krovnyja „geronnene Blut-
massen“, skr. seclra „Kalksinter“, eech. sddra .,Gips^' (aus ^se^idhra) aisl.                                                ;


sindr n. .,Metallschlacke"' und .jHammerschlag'^ (dazu smdra „Funken
spriihen^),             ags
=========== leaf 502
                                                                                                             ;




498                                                    ser-



ronnenen Milch, die Molke, Easewasser"; vielleicht                         alb. (Jokl SBAk. Wien
168, 128)                „gelabte Milch; Tropfen, Ease''                Suffix             Gdf. ser-rfy'a)
      gall.   FluBname Sarnus (vgl. ai. sardna- „laufend^0;
     lett.    sirt „uuiherschwarinen,        Raubziige machen^, sira (formell                 =   ai.   sir a)
imd sira „das bettelnde Herumstreifen^', sin „Marodeure‘‘; mit ahnlicher
Bed. vielleicht hieher (nach Brugmann IF. 19, 383) kymr. hcrw „Land-
streicherei, Bauberei^, mir. serh (mit h=^w) „Ilaub, Frevek^^)
   Vermutiich ist (nach Brugmann IF. 32, Iff.) auch gr, aiQsoy als Deno-
minativ eines ’^aiQa ( ai. sira — (pvl^a (pvy?]) „das An-, Eindringen wor-
                                  :                           :



auf, 0 QjLnj‘^ mit der Bed.-Entw. zu ,,in seine Gewalt bekommen, kriegen“
anzureihen.
   Curtius Gdr. ^ 349, FickI ^ 140, 562, II ^ 291, Prellwitz ^ 336 f., Yf. LEWb.^
704 f.       —   S.   auch sreu-      „flie6en‘\


3.    ser- „sorgend Obacht geben, schiitzen, bewahren“.
      Av.     Jiaraiti    „hat acht,
                              schiitzt''; haurvaiti ds., haurva- „beschutzend,
hiitend'"        in          spa „das Eleinvieh, die Schafe beschiitzender
                      pasus-Jiaurvo
Hund, Schaferhund^* (wie lat. servus, servo von einer «i-Erw., vgl. Persson
Beitr. 563, Brugmann II ^ 3, 270 f.; sie wird wegen fjgcog, St.          nicht
aus einem -^o-St. "^ser-tio- herzuleiten sein); hardtar- „wer woriiber wacht,
darauf achthat^, haro&ra- „Pflege, Wartung, Unterhalt“; hara- „acht-
habend, hutend“, red. h
=========== leaf 503
                                                               ser*                                                    499

Gr. ovQog ,,Wachter‘''  ist von njua-OQog, ogdco                                                   nicht zu      trenneii
(Bechtel Lexil. 262); die Yereinigung dieses                                                .,gewahren,      achtgeben‘‘
mit unserem         unter         durch Sommer Gr. Ltst. It2f. ist nur auf
den gr, Asper aufgebaut, der aber kein ausreichender Beweis fiir gr.
und jene Ur form ist, s. Persson Beitr. 549.      Uber gr. £Qvo&at „retten,      —
bewahren^ s. "^uer- ^verschlieSen'*.
  x\ls Gutturalerw.    hieher (Froehde BB. 21, 206, Persson Beitr. 563) lit.
s&g-mi, -ti, -iti „behute, bewache^*', sdrgas „WachteF', PI. sargal^ sargus
,,wachsam‘', apr. hiitsargs ..Haushalter”, abserg^snan Acc. ,,Schutz'\
   Aber aksL stregq, stresti .,huten wegen russ. storozh .,Wachter'‘ nicht
                                                               *



aus neben '^serg- stehendem '’^’sreg-, sondern aus "'^sferg-, ^storg- (s. Siitter-
lin IR 4, 101, Mikkola IF. 6, 349 ff., Pedersen KZ. 38, 319, Yf. LE^Yb.2
u. servo und s Wz. sterg- „lieben‘^      Yerkehrt will Bruckner KZ. 42, 48
auch lit. set'gmi aus diesem "^sterg- erklaren, durch Yermischung mit sergd ^
,.bin krank’‘).
  Zu sergmi trotz Pick     562, KZ. 43, 132, Bechtel Lexil. 141, 255 nicht
auch gr. ig^ardco, dgyajo^, dqyauoz, s. ^uergh- ( ^uer- „drehen'‘).                     :




3. ser-. sor-         ,,rot,   rotlich*\
   Ai. wahrscheinlich in sdra-m,                         -It       „Mark        eines       Baumes   (vgl.    lat.   rdhtir
,,Kernholz‘';,    Festigkeit, Kraft*\                   sarawga-li „bunt,                   scheckig^'    (versch.     von
rdra-h    ds.,   s.
```


## [2026-09-14T02:01:48.260Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== LEW sincerus ==\"; grep -n \"sincerus\" LEW_1910.txt | head -5; echo \"== LEW serum ==\"; grep -n \"^serum\\|serum \" LEW_1910.txt | head -5; echo \"== LAT sincerus ==\"; grep -n \"sincerus\" LAT.txt | head -5; echo \"== LAT serum ==\"; grep -n \"serum\" LAT.txt | head -5",
 "description": "Walde LEW and Ernout-Meillet on sincerus/serum"
}
```


### [2026-09-14T02:01:48.367Z] TOOL RESULT

```
== LEW sincerus ==
== LEW serum ==
226:Ammat I 39 amnud I 36, II 210 ampert I 686, II 284, 285 amprufid I 686, II 364, 366 ampt I 36 ampu<bulum I 46, 546 Apunuco I 45 amviannud I 36, IGEYAS an- I 686 avaSaxet I 43, 440 Anafriss I 681,687 Anagtiai I 47, 693 anamum I 49 ancensto I 199, 686 anet I 55 angetuzet I 25, 43, 693 ant I 53 antkadum I 538, 128 anter I 43, 687, 708 Anterstatat II 356, 597 Arafiis I 65 aragetud I 66, 686 aserum I 12, II 5238 atrud I 32 autt, avt, aut I 87 (een Tg 45 843 Battets I 93 Bansae I 1745 biass II S01 bittam II 809, 810 bivus II 809 Blaisiis I 108
== LAT sincerus ==
57097:sincerus, singuli, etc.).
58473:sincerus
58480:sem- est devant le groupe -pl~. - "V.sem-per, et cf .sincerus.
58516:sincerus, -a, -um ( sinceris tardif): pur, exempt de m^lange;
58530:deux tres tardifs); insincerus = avayvoc (Vg.). Les representants
== LAT serum ==
5428:pose *aserum, avec apophonie reguliere. H.L.693.
26197:gingrlS, -Is, -Ire: gingrire anserum'uocis proprium est. Inde
27491:hara, -ae f.: Atable pour aniaaux, h. anserum', spAcialeaent "por-
28260:138: uolturus in spinis miserum mandebat homonem, dont on rapprochera
57668:la main devant le juge ( asserere manu ou manum, cf. osq. manim aserum)
```


## [2026-09-14T02:01:56.486Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('incoming/WLD/WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\np=t[501]; i=p.find('1. ser-')\nprint(p[-1700:] if i<0 else p[i:i+1700])\"; echo \"=== LAT sincerus ===\"; sed -n '58510,58545p' LAT.txt",
 "description": "WLD ser- start and Ernout-Meillet sincerus"
}
```


### [2026-09-14T02:01:57.669Z] TOOL RESULT

```
t annehm-
bare Y^eiterungen bei Petersson                                     LUA. 1915, 44f.

1.    ser- „str6men, sich rasch und heftig wohin bewegen".
     Ai. sisarti, sdrati              ,,flie6t, eilt, jagt wornach. verfolgt^; fut. sarisyati, De-

siderativ sislrsati                 von einer schweren Basis "^sere-, vgL hom. gcbogai „be-
wege mich                schnell,          kraftig,          stiirme          an,   eile^^   aus    '^sro-id\       ein Y^znomen
           dazu,        ai.    '"^str,     *sirdJi,      ist      die    Grundlage des «-St.                  ai.   shd und sl7'd
„Strom, Rinnsal**;                   ai.    sarit       f.   „Bach, FluB'^, sarirdm, salildm „Y^assermasse.
Flut“, sarird- ,,wogend, flutend, unstet'*, sa^srHt- „stromend'', sd-sr-i-’ ,,lau-
fend, eilend^’; sardyu-li, sa^^ayu-h                                   ..Name eines Fiusses‘‘, ap. Haraica-,                     av.
(Acc.) Haroyum, np. Hare „Flu6 und Gegend von Herat^':
  ai. sdnna-h ,,das Fliefien'', gr. oqjlu] „Anlauf, Angriif, Drang nach etw^as''^),

wovon Sojudoj ..treibe an, rege an, intr. stiirme daher, v^orauf los*‘ aiber
oQjuog ..Ankerplatz*                       s.   Boisacq           s.   y.j;
     ai.    sard- „fliissig% gr. ogog,                            lat.   sey'iim^;      ,,der    wilsserige         Teil   der ge-

   9 Bedeutungseinfiuh seitens oqvvlii (mit welchem Sommer Gr. Lautst. 133 ogfiij ge-
radezu verbindet) ist vielleicht, aber nicht notwendig anzuiiehmen: auch aioeo) setzt
eine Bed. „andringen, worauf eindringen^ voraus.
     Wegen ogog unwahvscheinlich steilte Bruginanu BSGW. 1897, 20 serum zu ai.
l^aram -Wasser“, IxkiraU .zerflieht, fiieht^.

=== LAT sincerus ===
sin: v.st.
sinapi ( sinape Apicius),-is n.(et sinapis, -is f.,Plaut.): mou-
tarde. Empr. au gr. crCva,7U., comme sinapizo, sinapismus. Les formes
romanes remontent A sinapi et sindpi, les unes conservant le fon
grec, les autres 1 'accent latin, M.L.7933; et germ.:got. sinap,etc.
d'ou finn. sinappi.
sincerus, -a, -um ( sinceris tardif): pur, exempt de m^lange;
par suite, au moral "pur, sincere". - Ancien (Pl., Enn.), classique,
usuel.
Le sens de "pur, sans m^lange" est bien attest^ pour 1 'adjectif
et pour ses derivas: sincerum lac, sincera axungia; sincerum equestre
proelium, T.L.30,11; dans porci sacres sinceri (Pl. Men. 39 °), 1 'adj.sincinium
1108
semble vouloir dire "sana tache", de meme dans corium sincerissimum,
Pl.Rud. 7 S 7 . De la 1 '^tymologie aicienne, e.g. Don. ad Eu. 177: -m,
purum sine fuco et simplex est, ut mei sine cera ; Ps.Acr. ad Hor.
Epod.3,15 hoc est fauos premit, ut ceram separet et mei sincerum
reparet. Mais la forne attendue en ce cas serait *secSrus (comme
sSdulus) et il n'y a 11 qu’une etymologie populaire; cf. sine.
Derives: sinceritas (< 5 poq. imper. ), sincerb, -ds, sincerdsco, -is (tous
deux tres tardifs); insincerus = avayvoc (Vg.). Les representants
romans sont de la langue savante, M.I.7934.
Forme comme pro—cSTus. Le sin- est le meme premier element de
compos 4 que dans sim-plex. L'adjectif signifierait '^'une yenue".
sincinium, -I n. ( sincinia f.): translation du gr. p,ov£j)SCot, at-
testee a date tardive; cf.Ernout, Philologica, p.77, n.i.
( sinc^iput, -is n. : moitie de tete ( cf. occiput), glose correctement
BM*LHecpocXoc i ov, T|p.L>cpcxvov, medium, dimidium caput • En particulier
"cervelle" (Plaute).
Derive: sincipitdmentum, Pl.Men.311. Mot de la 1 . familiere (Pl.,
Pers., Juv. et Sid.), probablement terme de cuisine. De *sem(iJcaput .
Pour le traitement de 1 ’e, cf. le traitement de 5 dans nuncupa.
sine, preposition suivie de 1 'ablatif: sans. Remplace a 1 'epoque
bistorique un plus ancien se, sed . S'emploie seul, ou avec une n^gation
formant litote non, haud sine', souvent joint aussi a ullus, omnis.
Ne figure dans aucun compose; mais a servi a traduire, joint a un
```


## [2026-09-14T02:02:04.870Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== GPL leaf 53 ===\"; awk 'BEGIN{RS=\"\\f\"} NR==54' GPL.txt | head -40",
 "description": "Platts grammar p.41"
}
```


### [2026-09-14T02:02:05.924Z] TOOL RESULT

```
=== GPL leaf 53 ===
the adjective precede the substantive the ی‎ or * of indefiniteness must be affixed to the noun; ۰.8. بندی دادی‎ ASS ‘good counsel hast thou given’; tS eB سکی‎ استخوانی می خورد‎ ‘a hungry dog was eating a dry bone’. Similarly, if the substantive is in the plural, it alone takes the زی‎ e.g. مردمانی خوب‎ ‘(some) good men’; بندگانی صادق‎ ‘ true (or loyal) servants’.
§ 39. Adjective used as a Subst. An adjective, whether Persian or Arabic, may be used substantively, and in that case it will be treated in every respect as a substantive; e.g. bls a learned man’; دانایان عصر‎ ‘the learned men of the age’; Jol» ‘an ignorant man’; yw ele ‘ignorant men’ ; بدهای آشعارش‎ ‘the bad things in (lit, of) his poems’,
In the rare cases which occur of a noun in the plural number in construction with what appears to be an adjective also in the plural it is generally considered that the ‘ adjective’ is used substantively in apposition. Such instances are—
Faithful servants بندگان مخلصان‎ Worldlywise sages asin پیران‎ Valiant heroes مردانن دلاوران‎
DEGREES OF COMPARISON §40 a. The comparative degree of adjectives (Persian or Arabic) is formed by adding the suffix ثر‎ tar to the positive, and the superlative by adding ین‎ in to the comparative ; e.g. ده‎ ‘good’, بهتر‎ ‘better’, بهترین‎ ‘best’; wo ‘bad’, بدتر‎ (generally contracted to بثر‎ battar, and often to بتر‎ batar) ‘worse’, بدترین‎ (contrac
```


## [2026-09-14T02:02:06.600Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i,l in enumerate(leaves):\n    if 'seven,  adj' in l or 'seven, adj' in l:\n        print('leaf',i)\n        j=l.find('seven,  adj')\n        print(l[j:j+1400]); break\nEOF",
 "description": "Klein seven entry"
}
```


### [2026-09-14T02:02:07.873Z] TOOL RESULT

```
leaf 757
seven,  adj.  —  ME.  seven,  sevene,  fr.  OE.  seofon, rel.  to  OS.  sebun,  ON.  sjau,  Swed.  sju,  Dan.  syv, OFris.  si(u)gun  [on  analogy  of  the  g  in  ni(u)gun], MDu.  seven,  Du.  zeven,  OHG.  sibun,  MHG. siben,  G.  sieben,  Goth,  sibun,  and  cogn.  with  OI. saptd,  Avestic  hapta,  Toch.  A  spat,  B.  sukt,  guk (with  k  for  p,  on  analogy  of  the  k  of  the  follow¬ ing  numeral  okt ,  ‘eight’),  Hitt,  shipta.  Arm. evt'n,  Gk.  Ititoi,  L.  septem,  Alb.  state  (prob. assimilated  to  gaste,  ‘six’),  OSlav.  sedmi  (for *sebdmi ),  Lith.  septyni,  OIr.  sechtn,  W.  saith, ‘seven’.  Cp,  hebdomad,  hepta-,  septem-,  Septem¬ ber.
Derivatives:  seven,  n.,  seven-fold,  adj.  and  adv., seven-fold-ed,  adj.
seventeen,  n.  —  ME.  seventene,  fr.  OE.  seofon- tyne.  See  seven  and  -teen, seventeenth,  adj.  —  ME.  sevententhe;  see  prec. word  and  numeral  suff.  -th.  The  OE.  form  is seofon-teoda.
Derivatives:  seventeenth,  n.,  seventeenth-ly,  adv. seventh,  adj.  —  ME.  seventhe;  see  seven  and numeral  suff.  -th.  The  OE.  form  is  seofoda;  cp. ON.  sjaundi,  OS.  sivondo,  Dan.  syvende,  Swed. sjunde,  OHG.  sibunto,  MHG.  sibende,  G  sie- bente,  siebte.  Cp.  also  septimal,  septime. Derivatives:  seventh,  n.,  seventh-ly,  adv. seventieth,  adj.  and  n.  —  ME.  seventithe.  See seventy  and  numeral  suff.  -th.
```


## [2026-09-14T02:02:21.617Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i in range(720,762):\n    nums=re.findall(r'\\b1[34][0-9]{2}\\b', leaves[i])\n    head=leaves[i].strip()[:60].replace('\\n',' ')\n    print(i, nums[:6], '|', head)\nEOF",
 "description": "Calibrate Klein leaf to printed page"
}
```


### [2026-09-14T02:02:22.909Z] TOOL RESULT

```
720 ['1354', '1355'] | t-ful-ness,  n.,  robust-ic, adj.,  robust-ic-ity,  n.,  rob
721 ['1356'] | ext  word, romaika,  n.,  Greek  national  dance.  —  ModGk.
722 ['1484', '1359'] | aceae. | •t A A 4 rosacean,  adj.,  rosaceous.  —  See  next
723 ['1360'] | rumpere,  ‘to  break’.  See  route  and  cp.  rut, ‘routine’
724 [] | en;  prob.  a  blend  of  rover,  ‘sea robber’,  and  ON.  r
725 ['1474'] | to  read,  ‘red’.  See  red  and  cp. rudd,  the  fish,  rud
726 ['1365'] | he cud’,  fr.  ruminatus,  pp.  of  ruminari.  See  prec. wo
727 [] | suff.  -ine. Cp.  rucervine. rusk,  n.,  light,  soft  bread
728 [] | i,  F.  samedi,  ‘Saturday’  and — prob. through  the  mediu
729 ['1373'] | onsecration.  —  ME.,  verbal  noun  of sacren,  ‘to  consec
730 [] | :  Sahar-an,  Sahar-ian,  Sahar-ic,  adjs. sahib,  n.,  a  t
731 ['1490', '1376', '1377'] | See  salt  and  -ine  (representing L.  -inus)  and  cp.  L.
732 ['1378'] | fr.  OF.  saluta- cion  (F.  salutation),  fr.  L.  salutati
733 ['1380'] | s’,  fr.  Samnium,  which  prob.  stands for  *Sabniom  and 
734 ['1382'] | derives  fr.  VL. sanguem.  See  prec.  word.  F.  de,  ‘of,
735 [] | ‘soap’,  which  is a  Teut.  loan  word.  See  soap. Derivat
736 [] | um,  fr.  sar- pere,  ‘to  cut  off,  lop,  trim’,  fr.  I.-
737 ['1388'] | —  ME.  Saterdai,  fr.  OE.  Satsern(es)- dteg,  Sseterd&g, 
738 ['1390'] | .  secgan,  ‘to  say’.  See  say  and  cp.  saga, which  is 
739 ['1391', '1392'] | e  head).  See  Kluge- Mitzka, EWDS.,  p.  633  s.v.  Schale
740 [] | ades,  shoulders’,  which  is of  uncertain  origin.  It  po
741 ['1394', '1393'] | the  Tower  under  Henry  VIII. scazon,  n.,  1)  a  choliam
742 [] | 91) fr.  schizo-  and  Gk.  p.uxY]Tei;,  pi.  of  ‘fun¬ gus’
743 [] | ic  Greek  calendar  (corresponding  to  the  sec¬ ond  half
744 ['1401', '1402'] | n.  —  It.  scopo,  ‘mark,  target,  thing  aimed at,  aim",
745 ['1405'] | .  escourgee,  ecourgee,  ‘whip, scourge’),  fr.  VL.  *ex-c
746 [] | referred  to. scriptorium,  n.,  a  writing  room  esp.  tha
747 ['1406'] | ON.  skarpr, OE.  scearp ,  ‘sharp’  (see  sharp).  Cp.  Dan
748 ['1408', '1409'] | ence  also Swed.  sate,  Dan.  sxde;  rel.  to  OHG.  saze, 
749 ['1410'] | second'.  See  second,  adj. securable,  adj.  —  Formed  fr
750 ['1413'] | hol,  n.,  name  of  the  Heb. -Aram,  vowel  sign  ’.' —  A
751 ['1414', '1415'] | asXrjvT],  ‘moon’,  rel.  to  osX aq,  ‘light,  brightness, 
752 ['1416'] | Biblical  Heb.  samakh,  of s.m.),  used  elliptically  for 
753 [] | ion  of  seven  see  prec.  word. seiior,  n.,  a  Spanish  
754 [] | e next  word  and  cp.  sepia. sepsis,  n.,  putrefaction.  
755 ['1422'] | no,  ‘coin’, dimin.  formed  fr.  zecca,  ‘a  mint’,  fr.  A
756 ['1424', '1425'] | net,  sermonette  (qq.  v.),  sermonettino (q.v.),  sermon-i
757 ['1426', '1427'] | shape’.  See  prec.  word  and  suff.  -oid. Derivative:  se
758 ['1428'] | verus.  See  severe and  -ity. Seville  orange,  also  Sevil
759 [] | darkness’,  Olr.  scath,  OW.  scod, Bret,  squeut,  ‘darkne
760 [] | n.  F.  chantier,  ‘workshop’, fr.  F.  chantier,  ‘timberya
761 [] | cepter’,  and  to  Heb. shebhet,  Tod,  staff,  club,  scept
```


## [2026-09-14T02:02:36.553Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i in range(764,772):\n    nums=re.findall(r'\\b1[34][0-9]{2}\\b', leaves[i])\n    print(i, nums[:6], '|', leaves[i].strip()[:70].replace('\\n',' '))\nprint('---- leaf 767 sample ----')\nprint(leaves[767][:600])\nEOF",
 "description": "Klein leaves 764-771 page numbers"
}
```


### [2026-09-14T02:02:37.764Z] TOOL RESULT

```
764 ['1439', '1440', '1441', '1488'] | shout-er,  n.,  shout-ing,  n. shove,  tr.  and  intr.  v.  —  ME.  sh
765 ['1442'] | er,  tr.  v.,  shutt-er- less,  adj.,  shutt-ing,  n. shuttle,  n.  — 
766 ['1443', '1445'] | .  -crximov,  fr.  oxo7reiv,  ‘to  look  at,  ex¬ amine’.  See  -scope
767 ['1444', '1446'] | g  to,  or  con¬ taining,  silica.  —  See  silica  and  -ous. silicic
768 ['1448'] | Pure  is  dealt  with  as  an  impostor  and  is  believed only  after
769 ['1449', '1450', '1451'] | ,  pertaining  to Ceylon;  n.,  a  native  of  Ceylon.  —  Formed  wit
770 [] | cleft,  dis¬ sected;  rose’  (said  of  the  sun).  Cp.  Saracen, sarc
771 ['1452', '1453'] | nding  to  Goth,  sik,  OHG.  sih,  MHG.,  G. sich,  ‘himself,  hersel
---- leaf 767 sample ----
g  to,  or  con¬ taining,  silica.  —  See  silica  and  -ous. silicic,  adj.,  derived  from,  or  pertaining  to,  silica. —  See  silica  and  adj.  suff.  -ic. siliciferous,  adj.,  containing  silica.  —  See  silica and  -ferous.
silicify,  tr.  v.,  to  convert  into  silica;  intr.  v.,  to  be converted  into  silica.  —  See  silica  and  -fy. silico-,  before  a  vowel  silic-,  combining  form  in¬ dicating  the  presence  of  silicon.  —  See  silicon, silicle,  n.,  a  small  and  short  silique.  —  L.  silicula, ‘a  little  husk  or  pod’,  dimin.  of  siliqua.  See s ilia  lie
```


## [2026-09-14T02:02:50.889Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && python3 - 6caa01546759cb79.txt <<'EOF'\nimport sys,re\nt=open(sys.argv[1],encoding='utf-8').read()\nprint(t[:200])\ni=t.find('سرم')\nprint(re.sub(r'[ \\t]+',' ',t[max(0,i-200):i+2500]))\nEOF",
 "description": "Check abadis serom page"
}
```


### [2026-09-14T02:02:52.164Z] TOOL RESULT

```
URL: https://abadis.ir/fatofa/%D8%B3%D8%B1%D9%85/
FETCHED: 2026-09-14T02:01:19Z
STATUS: 200
TITLE: سرم - معنی در دیکشنری آبادیس

سرم - معنی در دیکشنری آبادیس 

 دیکشنری مترجم بپرس 

 سرم
 /serom/

 مت
URL: https://abadis.ir/fatofa/%D8%B3%D8%B1%D9%85/
FETCHED: 2026-09-14T02:01:19Z
STATUS: 200
TITLE: سرم - معنی در دیکشنری آبادیس

سرم - معنی در دیکشنری آبادیس 

 دیکشنری مترجم بپرس 

 سرم
 /serom/

 مترادف سرم : خونابه
 معنی انگلیسی : serum 

 دنبال کنید 

 لغت نامه دهخدا

 سرم. [ س َ ] ( اِ ) کنگر و آن رستنیی بود که برگش خاردار است و آن را پزند و با ماست خورند و بعربی حرشف خوانند. ( برهان ) ( از آنندراج ).به لغت شیرازی اسم فشاع است. ( تحفه حکیم مؤمن ).
 سرم. [ س َ رَ ] ( ع اِ )درد کون. ( آنندراج ) ( منتهی الارب ) ( اقرب الموارد ).
 سرم.[ س َ ] ( ع صوت ) کلمه ای است که بدان سگ را زجر کنند،فیقال : سَرْماً سَرْماً. ( آنندراج ) ( منتهی الارب ).
 سرم. [ س ُ ] ( ع اِ ) دهان روده که مخرج ثفل است. ( غیاث ) ( آنندراج ). اندرون دبر مردم. ج ، اسرام. ( مهذب الاسماء ). نام دیگر معاء مستقیم است. ( از ابوعلی سینا در قانون ص 215 ).
 سرم. [ س ِ رَ ] ( ترکی ، اِ ) لفظ ترکی است بمعنی دوال خراشیده. ( غیاث اللغات ). دوالی که روی آن را خراشیده باشند تا نرم شود و به همین مناسبت کسی را که از بسیاری کار دستها پینه بسته باشد سرم دست گویند. ( آنندراج ) : 
از بهر پای باز تو صیاد لامکان 
از پشت شیر لجه خضرا کشد سرم. ؟ ( از رشیدی ).
رجوع به سیرم شود. 

 فرهنگ فارسی

 یکی از سه پسر فریدون . در اوستا ( فروردین یشت بندهای ۱۴۴ - ۱۴۳ ) از ممالک ایران و توران و سلم و سائینی و داهی اسم برده شده است .سه مملکت اول یاد آور داستان معروف فریدون است که جهان را در میان سه پسر خود سلم و تور و ایرج تقسیم کرده . مملکت سلم یا سرم در اوستا آمده و در تعیین محل آن اشکال است . مورخان این مملکت را روم و روس و آلان ومغرب و خاور زمین و بلاد فرنگستان و اروپا ذکر کرده اند و خاورشناسان نیر بحدس و احتمال پرداخته برخی بقوم سامی نژاد سلیم که در آسیای صغیر در مملکت لیکیه ساکن بوده اند متوجه شده اند ولی غالب آنان گمان برده اند که قوم سلم همان طوایف معروف ساورمات یا سورمات باشند و مارکوارت نیز بر این عقیده بود. سرمتها قومی بودند آریایی نژاد . سرزمین آنان از شمال شرقی دریاچه آرال تا رود ولگا امتداد داشت . آنان چادر نشین بودند و از تمدن و زندگانی شهری بهره ای نداشتند. بنا بقول مورخان قدیم یونان و روم مادها خود را از بستگان و خویشان سرمتها میخواندند ( یشتها پور داود ۶ - ۵۵ : ۲ برهان چا . م . معین : سلم ).
( اسم ) ۱ - خون آبکی خونابه . ۲ - دارویی مایع مانند که برای جلوگیری از مرض به وسیله آبدزدک به بدن تزریق کنند .
دهان روده که مخرج ثقل است . اندرون دیر مردم . جمع اسرام . 

 فرهنگ معین

 (س رَ ) (اِ. ) تسمه ، دوال .
 (س رُ ) [ فر. ] (اِ. ) ۱ - خون آبکی . ۲ - دارویی مایع حاوی مواد قندی یا ویتامین ها یا سایر داروهای حیاتی که جهت جلوگیری از بیماری یا برای ادامه حیات از محفظه ای شیشه ای یا پلاستیکی به وسیلة لولة پلاستیکی توسط سرنگ مخصوص از طریق سرخ رگ به بدن بیمار تزریق 

 فرهنگ عمید

 = کَنگر
محلول آب مقطر حاوی موادی مانن
```


## [2026-09-14T02:02:53.016Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== ARY latin index HAFT/SEPT/SER ==\"; grep -n -i \"haft\\|septm\\|^SER\\b\" incoming/ARY/ARY_latin_index_pages.txt | head -15; echo \"== SYN seven sapta ==\"; grep -n \"sapta\\|septem\" SYN.txt | head -8",
 "description": "Aryanpur and Buck"
}
```


### [2026-09-14T02:02:53.123Z] TOOL RESULT

```
== ARY latin index HAFT/SEPT/SER ==
449:Vv haft | sept sieben zeven su
1297:Ser ctls Biel, a SUF sods 30 eloT BEG GAB) lal pel aber
15513:syv DANISH) Sail HAFT s(PAHLAV]) «5 shay
15516:‘EVEN DUTCH) .gasa HEFT, HAFT, AHFT, HEVFT
15540:SEVENTY HENGLISH) gulS3i HARTAD, HAFTAT (PAHLAVI) «5 ly
15560:HEBDOMOS (GREEK) gly HAFTUM AAPAHLAVI) 5 shy
== SYN seven sapta ==
```


## [2026-09-14T02:03:04.574Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== NYB haft ==\"; grep -n \"haft\" NYB_vol2_glossary.txt | head -6; echo \"== PHD Herew ==\"; grep -n -i \"har[ēee]w\\|hlyw\" PHD.txt PHD_mackenzie.txt NYB_vol2_glossary.txt | head -8; echo \"== SYN numerals seven ==\"; grep -n \"13\\.1[0-9] \" SYN.txt | head",
 "description": "Nyberg haft, MacKenzie Harew"
}
```


### [2026-09-14T02:03:04.673Z] TOOL RESULT

```
== NYB haft ==
441:andar [BYN] in: 1. adv. a) referring to a preceding encl. pron. (ef apäk, apar, avis, haciš, patiš): zäyak-e ke-š murvēcak ~ an egg in which there is a chicken 92%; api-§ ... must" (g. v.) u drog ~ nest F:7; without a preceding encl. pron.: Sugud i haft janakan ~ in which there are seven j. (q.v.) 11318-14; haft x"ataidan ~ būt 11314-95; — b) prev., esp. with vbs. of
608:*ap-töm: read [hptwm] haftom. *āpurišn ['pwlin']: read appurišn.
1639:igart [glt'] dust 2020-24, — NP gard. 2gart v. haft-gart.
1770:haft [hpt'; SB’; figures] seven; pl. cas. obl. —-àn the seven planets 5’; the seven heroes bringing about the fraskart 10615.
1771:haít-dahom [hptdhwm] the seventeenth. haft-gart [7-glt'] v. -kart.
1772:haft-kišvar [hptkyšwl] the world as a geographical totality, consisting of seven
== PHD Herew ==
== SYN numerals seven ==
8025:Sp. cansado, pple. of cansar ‘tire’ (now trans.; refl. ‘get tired’), this (not : Fr. casser ‘break’ ifr. Lat. quassare ‘shake’, as Diez 91, REW 6939, but) = It. cansare ‘avoid’, fr. Lat. campsdre ‘turn aside from’, fr. Grk. xaépyar aor. Of kaurrw ‘bend’ (9.14). So Korting, Menéndez Pidal, C. C. Rice, Language 13.18 f., 19.154, Leo Spitzer, Language 14.205 f., Wartburg 2.156. Lat. campsdare occurs in Ennius in the nautical sense of doub- ling a headland (frequent in Grk.), then only in late Latin in more general sense of ‘turn aside from’ e.g. ut de via cam- semus Pereprinatio 10.8 and in many Blosses, The semantic development in Spanish was prob. (otherwise Rice) oan > ‘cease’ > ‘get hired INe ra as ie > es atl oie re 4 € association is there, ‘get tired? ae cho Russ. ustavat! 0 Slensich » ustate get tired, cease’ =
23351:13.11 Quantity
23352:13.12 Numper
23353:13.13 WHOLE
23354:13.14 Every; Au (pl.)
23355:13.15 Mucu; Many
23356:13.16 More
23357:13.17 Lirruz (Quantity); Few (Number)
23358:13.18 ENnoucH
23359:13.19 Moxtirupr, Crowp
```


## [2026-09-14T02:03:12.635Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^ser[oōaā]\\{0,2\\}-\\? \\|^serom\\|^ser- \\|^seni\\|^sini\\|^sn̥ter\" IEC.txt | head -12; echo \"---\"; grep -n \"sine .without\\|sine 'without'\\|serum\" IEC.txt | head -8",
 "description": "Mann IEC ser- and seni-"
}
```


### [2026-09-14T02:03:13.610Z] TOOL RESULT

```
15236:ser- (1, 2) radical form of type sero (1) “Join, link’; (2) of sero (2) ‘watch’
15244:ser- — seruð (seruuó, soru-)
---
4822:ghór- ‘outflow, liquid filth, slurry, gore, pus’. Cf. ghur- Gk. cf. i-khór ('gore, pus, serum’, fr. *uis- ghor-, see uis-); Br. gor ‘abscess’; W gôr ‘pus’; G Guhr ‘slurry; manure’
5087:ghuros ‘outflow, filth, matter’. Cf. &huuo (1) (For Gk. i-khór *gore, matter, serum', see uis and ghuuo); Lat. (?) dial. foria (‘thin excre- ment’, for *horia?); Ir. gur, gor ‘pus, abscess’; Br. gor, pl. -iu, f. abscess; W gori 'suppura- tion’; OE gor, gyr (dirt, mud’; E gore; G Gur ‘dung; filthy water from coalmining'; ON gyrja (bloodstain': Lat. foria?); Sw. gorr ‘pus’; OCS cf. voz-grja (ómucus', fr. uos-, q.v. + ghurio); Cz. voz-her, m. ‘mucus, snot
5552:guhros, å, iə (2) ‘filth’. Cf. ghuros (as a pos- sible variant) & guhurs- Lat. (ambig.) fória, npl. ‘diarrhoea’; Ir. gor (2) ‘pus’; W gôr, id.; Br. gôr (“abscess?, a LW in Norman Fr. gore ‘venereal disease’. For OE gor ‘dung’, E gore, cf. ghuros, a variant of guhros (?). Gk. ikhór ‘serum’ etc. seems to represent a type *uis-Shuuor-, see uis-, ĝhuu-. Gk. phúrð ‘mix, defile’ indicates a form *gu- hur-)
8163:kserom (?) “fluid? Skt. ksaram (water; Lat. (ambig.) serum ‘whey’ (equates equally with Skt. sáras, n. “fluid, water”. See seros, om)
9359:Kuoiios, -ón, -en ‘whey, serum’. WP I, 468-9
15242:seros, om (?) “fluid”. Cf. ksero-, selos, uoruos. Evidence ambig. (For Skt. saráh, adj. “fluid”; sarà, f. “stream; Per. gau-har 'essence', see sel-); (for Gk. ouros, orrós ‘whey’, see uoruo-); (for Lat. serum, n. ‘whey’, see also ksero-, in view of Skt. ksaram, n. ‘water’); Pol. (*-ē-) siara, f. ‘colostrum’; Blg. séra, f. ‘rinse for wool. Cf. WP II, 497. Cf. also: Hitt. sesariya(mi), v. (filter, a redup. of type *sísér-)
19555:-um, inf., active participle, and future parti- ciple ending. See next Osc. cf. deíkum ‘to say’; ezum ‘to be’; Umb. deicum ‘to say’; (?) Alb. cf. i lidhëm, adj. Chound Ambig.); OBr. acom ‘to deny’; Latv. cf. deverbal nouns of type sed-ums ‘haven’, etc. (Eastern Armenian presents of type serum em ‘I am loving’, apparently embody a pp. of type -(o)menos as Gk.)
```


## [2026-09-14T02:04:37.903Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== HRN Herat ==\"; grep -n \"Herat\\|Harē\\|Hare '\" HRN.txt | head -6; echo \"== SKT sincere/sans ==\"; grep -n \"^SINCERE\\|sincere\\|^SANS\\|sans,\" SKT.txt | head -6; echo \"== KLN serum ==\"; grep -n \"serum,  n\\|serum, n\" KLN_1966.txt | head -3; echo \"== GPL numerals ==\"; grep -n -i \"haft\\|cardinal numbers\\|NUMERALS\" GPL.txt | head -10",
 "description": "Horn Herat, Skeat, Klein serum, Platts numerals"
}
```


### [2026-09-14T02:04:38.013Z] TOOL RESULT

```
== HRN Herat ==
== SKT sincere/sans ==
3189:incessant,  ceaseleu.  (L.)  L.  itues- lanf;  stem  of  ittcfssaMt,  unceasing.— L.  wi-, not ;  cessans,  ceasing,  pros.  pt.  of  ressart, to  cease ;  see  oeaae  (above).
17300:Sincere.  (F.-L)  O.F.  shteert.^t. simtms,  pure,  sincere.  Dor.  sineerify, from  F.  sincerity,  from  Ij.  ace.  sineeritaiem.
== KLN serum ==
3007:Derivatives:  antiseptic-al-ly,  adv.,  antiseptic- ism,  n.,  antiseptic-ist,  n.,  antiseptic-ize,  tr.  v. antiserum,  n.  —  A  hybrid  coined  fr.  Gk.  dvxi, ‘against’,  and  L.  serum,  ‘whey’.  See  anti-  and serum.  The  correct  form  would  be  antiorus,  fr. Gk.  dvxi,  ‘against’,  and  opo?,  ‘whey’, antisocial,  adj.  —  A  hybrid  coined  fr.  Gk.  dvxi, ‘against’,  and  L.  socialis,  fr.  socius,  ‘companion’. Sec  anti-  and  social.
34728:Derivatives:  serri-ed-ly,  ad v.,  serri-ed-ness,  n, Sertularia,  n.,  a  genus  of  branching  hydroids (zool.)  —  ModL.,  fr.  L.  sertula  (pi.),  dimin.  of serta,  ‘wreathes  of  flowers,  garlands’,  which  is prop.  pi.  neut.  pp.  of  serere,  ‘to  join  together'. See  series  and  cp.  words  there  referred  to. Sertullarian,  adj.,  pertaining  to  the  genus  Ser- tullaria.  —  See  prec.  word  and  -an. serum,  n.  —  L.,  ‘watery  fluid;  whey’,  cogn.  with Gk.  6p6g  (for  *aop6?),  ‘whey’,  OI.  sarah, ‘flowing’,  sarit,  ‘brook,  river’,  Gk.  op|ir),  ‘as¬ sault,  attack,  onset,  impulse’,  opptav,  ‘to  urge, stimulate’,  Lett,  sirt,  ‘to  make  a  raid’,  fr.  I.-E. base  *ser~,  *sor-,  "to  run,  flow’.  Cp.  hormone, orrho-,  serac  and  the  second  element  in  Apsaras, samsara.  I.-E.  base  *ser-,  *sor-,  ‘to  flow,  run’, is  rel.  to  base  *srew-,  of  s.m;  see  rheo-. servable,  adj.  —  Formed  fr.  serve  with  suff.  -able, serval,  n.,  an  African  wild  cat  (Felix  serval).  — F.,  introduced  by  Buffon  fr.  Port,  lobo  cerval, ‘lynx’,  which  is  formed — with  change  of  suff. — fr.  L.  lupus  cervarius  (whence  also  F.  loup  cer- vier),  ‘lynx’,  lit.  ‘wolf  that  hunts  the  stag’,  fr. lupus,  ‘wolf’,  and  cervarius,  ‘pertaining  to  a stag’,  fr.  cervus,  ‘stag’.  See  cervine.
== GPL numerals ==
54:NoumERALS, 41. Words used Idiomatically in Numbering, 43. Dis- tributive Numerals, 44. Multiplicative Numerals, 45. Approxi- mate Numbers, 45. Fractional Numbers, 46. Adverbial Numbers, 46. Pronoun, 46. Independent Personal Pronouns, 47. Affixed Personal Pronouns, 50. Reflexive Pronouns, 52. Demonstrative Pronouns, 54. Relative Pronouns, 58. Inter- rogative Pronouns, 62. Indefinite Pronouns and Nouns, 65.
64:DrnominativE Nouns. Noun of Unity, 169. Noun denoting Vessel or Receptacle, 170. The Relative Adjective, 170. The Abstract Noun of Quality, 171. The Diminutive, 172. Formation of Feminines from Masculines, 172. Number, 173. The Dual, 173. Regular Plurals, 173. Broken Plurals, 174. The Plural of the Plural, 180. The Declension of Nouns, 180. The Numerals, 181.
66:Construction of the Numerals, 182. Fractional Numbers, 183. Pronominal Suffixes, 183. The Demonstrative Pronoun, 183.
242:§ 14. The twenty-eight letters of the Arabic alphabet are sometimes used as numerals. Their numerical order, however, differs from that given in the alphabet, being, in fact, the order of the Hebrew or Phoenician alphabet. ‘The letters in this order are grouped into the following eight meaningless words, to serve as a memoria technica, and are briefly called ‘the ۵ * ۶:
520:Numerals—The Cardinal Numbers Al
523:IV. THE NUMERALS (اسمای اعداه)‎ A. Tae دجم‎ NumBers (اسمای اعداد ذاتیه)‎ § 46. The following are the cardinal numbers :—
539:60. 1. شصت‎ for orig. شست‎ (Phi. shasht; O.P. khshvashti). 70. هفتاد مب‎ (Phi. haftat; O.P. haptaiti).
550:Note 2. In the language of the present day, the particle تا‎ (v. § 53) is affixed to the numerals to denote the individuals; 6.۵ دو تا‎ ‘two’, تا‎ sw ‘three’, تا‎ so ‘a hundred’, هزار تا‎ ‘a thousand’.
551:§ 48. The cardinals are not inflected. The exceptions to this rule are the numerals هزار‎ and رصد‎ which, as collective nouns, take the plural suffix; e.g. صدها‎ ‘hundreds’ ; Es هزارا‎ and هزارها‎ ‘thousands’.
552:Nor, with the exception of wh ‘ , do the numerals have the ya-t-tankir affixed to them.
```


## [2026-09-14T02:04:47.490Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '520,548p' GPL.txt",
 "description": "Platts p.41 numerals"
}
```


### [2026-09-14T02:04:47.552Z] TOOL RESULT

```
Numerals—The Cardinal Numbers Al
excess’; while that at the end of the substantive is called زائد‎ Call ‘the redundant alzf’. It is the latter alzf that also occurs in the
word گفتا‎ (= wa) ‘he said’, This use of alifis not found in Phl. or O.P., it has its origin in modern Persian, and is probably derived from the Arabic: cf. the final ali in the Ar. وا زیدا‎ ‘Oh Zaid’ ! وا امیر الوم تن‎ 8 for the Conumander of the Belvo? ! This alif is called 433231 eet, or in Persian .الف ندیه‎
IV. THE NUMERALS (اسمای اعداه)‎ A. Tae دجم‎ NumBers (اسمای اعداد ذاتیه)‎ § 46. The following are the cardinal numbers :—
Units (احاد)‎ 1.1 eb (Phi. gvak; O.P. aiva). 5.0 5%) (O.P. paiicha).
2. ۲ 49 (OP. dea). 6. 4 شش‎ (O.P. khshvash). 3. ۳ sw (O.P. thre). 7. ۷ هفت‎ (O.P. hapta).
4. ۴ چهار‎ or le (O.P. ۲ 8. ۸ هشت‎ (O.P. ashta), 9. 4 35 (O.P. nava).
۱ Tens (عشرات)‎
0 دهد‎ (poet. also) sls (O.P. dasa).
11. ۱۱ یازده‎ (dialec.) 3335, (O.P. aivadasa).
12. ۳ دوانزده . وو دوازده‎ (O.P. dvadasa). 13. ۱۳ وو سیزده:‎ .  هدزنیس‎ (O.P. thridasa).
14. ۱۴ چهارده‎ or چارده‎ ) ۰ chathrudasa).
15. 10 بانزده‎ )0.۳۰ paiichadasa).
16. ۱۰ شانزده‎ )۰ khshvashdasa).
17, ۱۷  هدتفه‎ or هفده‎ (O.P. haptadasa).
18. ۱۸ هزده رهشتده‎ or رتجدة‎ (O.P. ashtadasa).
19. 44 $9353; ,وا زده‎ dialec. نوانزده‎ )۰ navadasa). 20. ۲۰ بیست‎ (Phl. vist; O.P. 0190860
30. r- سی‎ (Phi. sth O.P. thrisat).
40. ۰ 2 Je (Phl. chahal ; O.P. chatvaresata). 50. 0+ Ash (Phi. panchah ; O.P. patichasat).
60. 1. شصت‎ for orig. شست‎ (Phi. shasht; O.P. khshvashti). 70. هفتاد مب‎ (Phi. haftat; O.P. haptaiti).
80. a. هشتاد‎ (Phi. hashtat; O.P. ashtaittt).
90. ۰ - نود‎ (Phi. navat ; O.P. ۵۵۵۸۸(۰
42 A ccidence
Hunpreps (متات)‎ 100. 1.. صد‎ (orig. Jw; Phi. sat; 0:۳, sata), plural les. 200. ۲۰۰ دویست‎ (O.P. duye saite) and to 59. 300 ۳ شیک‎ 500. 6. wah,
THOUSANDS (آلوف)‎ ۱
1000. ۱۰۰۰ هزار‎ (Phi. hazar; O.P. hazanra), plural هزاران‎ or .هزارها‎ 10,000. _\j@ ده‎ or UJ, obs. بیور‎ (Phi. 0200۴ و‎ O.P. baévar).
100,000. 7
500,000. هزار‎ sail ne 1,000,000 = کرور‎ yo.
§ 47. The [0 which indicate numbers compounded of the units and the tens, hundreds, &c., are formed by placing the highest number first, the others following in order, and each being connected with the preceding number by the conjunction و‎ ‘and’; as eh بیست و‎ ‘twenty and one, twenty-one’; sy و نود و‎ do هزار و هشت‎ eh ���one thousand and eight hundred and ninety and three’.
```


## [2026-09-14T02:04:57.165Z] TOOL CALL #54: Bash

```json
{
 "command": "python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/sebun\" --note \"page 444, Septm: Germanic 'sibum' node — correct PGmc form\"; mkdir -p data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg444.png data/verification/sources/refs/ocr/BOOK/444.png && ls -la data/verification/sources/refs/ocr/BOOK/444.png",
 "description": "Fetch PGmc sebun, copy page PNG"
}
```


### [2026-09-14T02:05:00.504Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/aebf4f7b6e6756d4.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 70076 Sep 13 22:05 data/verification/sources/refs/ocr/BOOK/444.png
```


## [2026-09-14T02:05:03.708Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && python3 - aebf4f7b6e6756d4.txt <<'EOF'\nimport sys,re\nt=open(sys.argv[1],encoding='utf-8').read()\ni=t.find('From Wiktionary')\nprint(re.sub(r'[ \\t]+',' ',t[i:i+1200]))\nEOF",
 "description": "Check PGmc sebun page"
}
```


### [2026-09-14T02:05:05.031Z] TOOL RESULT

```
From Wiktionary, the free dictionary

 This Proto-Germanic entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.

 Proto-Germanic
 [ edit ] 

 Etymology
 [ edit ] 

 From earlier *sebunt , from Pre-Germanic *sepḿ̥t , a dissimilatory alteration of *septḿ̥t ( “ seven ” ) , from Proto-Indo-European *septḿ̥ ( “ seven ” ) , with -t added through influence of *newun ( “ nine ” ) and *tehun ( “ ten ” ) . [ 1 ] An alternative theory posits that the -t is due to the influence of Proto-Indo-European *septm̥th₂ós ( “ seventh ” ) (compare Lithuanian septiñtas , Sanskrit सप्तथ ( saptatha ) ). [ 2 ] [ 3 ] 

 Pronunciation
 [ edit ] 

 IPA ( key ) : /ˈse.βun/ 

 Numeral
 [ edit ] 

 Proto-Germanic numbers ( edit ) 

 70 [a] , [b] 

  ←  6 

 7

 8  →  

     Cardinal : *sebun 
     Ordinal : *sebundô 
     Multiplier : *sebunfalþaz 

 *sebun [ 4 ] 

 seven 

 Derived terms
 [ edit ] 

 *sebundiz 

 *sebunstirniją 

 Descendants
 [ edit ] 

 Proto-West Germanic: *sebun Old English: seofon , sufon , syfon — Late West Saxon , siofun , seofun — Mercian , seofo , siofu , sifu — N
```


## [2026-09-14T02:11:55.496Z] TOOL CALL #56: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-444.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW = \"https://en.wiktionary.org/wiki/\"\n\ne0 = {\n \"entry\": 0,\n \"root\": \"Sen 2, Seni\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *sen-, *seni-, *senu-, *sn̥-ter- 'apart, separated, for oneself, without' (Pokorny 907; Watkins sen-2)\",\n \"note\": \"Pokorny IEW p.907 heads the entry 'seni-, senu-, (senī-), sn̥-ter- „für sich, abgesondert“' and lists exactly the three descendants Nourai draws (Av. hanarə, Skt. sanu-tár, Lat. sine). Nourai's headword shape 'Sen 2, Seni' is copied from Watkins/AHD ('sen-2. Also seni-. Apart, separated. [Pok. seni- 907.]'), not from Pokorny, who has no 'sen 2'. Root, language label and gloss are all correct. The only problem on this chart is the Latin box: Pokorny, Walde-Pokorny and Watkins all keep sincērus AWAY from sine (Watkins files SINCERE under sem-1 'one').\",\n \"note_fa\": \"ریشهٔ هندواروپایی آغازین *sen-/*seni-/*sn̥-ter- به معنای «جدا، کنار، بی‌ـ» در فرهنگ پوکورنی (ص ۹۰۷) با سرواژهٔ «seni-, senu-, (senī-), sn̥-ter- „für sich, abgesondert“» آمده و همان سه بازماندهٔ نمودار نورایی (hanarə اوستایی، sanu-tár سنسکریت و sine لاتین) را برمی‌شمارد. شکل سرواژهٔ «Sen 2, Seni» را نورایی از پیوست ریشه‌های هندواروپایی واتکینز (AHD) گرفته است نه از پوکورنی. ریشه، برچسب زبانی و معنا هر سه درست‌اند؛ تنها اشکال نمودار در جعبهٔ لاتین است: پوکورنی، والده‑پوکورنی و واتکینز هیچ‌یک sincērus را به sine نمی‌بندند و واتکینز آن را ذیل ریشهٔ *sem- «یک» می‌آورد. ادعای نورایی دربارهٔ خودِ ریشه درست است.\",\n \"sources\": [\n   \"https://www.etymonline.com/word/sans\",\n   \"https://www.etymonline.com/word/sincere\"\n ],\n \"ref_check\": [\n   {\"ref\": \"POK:907\", \"status\": \"supports\",\n    \"note\": \"POK_03.txt leaf 144 (= printed p.907): 'seni-, senu-, (senī-), sn̥-ter- „für sich, abgesondert“. Ai. sanu-tár „abseits von, weit weg“ … av. hanarə „abseits, ohne“; gr. ἄτερ (ion.) „abseits, ohne“ (*sn̥ter); … lat. sine „ohne“ (wohl neutr. *seni …). WP. II 494 f., WH. II 542 f.' Page number exact; gloss and the three branches match the chart.\"}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. II 494-495 (WLD_Bd2_pages.txt leaf 498-499)\", \"stance\": \"supports\",\n    \"note\": \"Headword 'seni-, senu- (senī-), sn̥-ter-' with 'lat. sine „ohne“ (wohl neutr. *senī, nächststehend dem ir. sain aus *seni-)' and the Germanic sundr-/sundor group. Nothing about sincērus.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. sen-2 (AHD_watkins1985.txt line 916)\", \"stance\": \"partial\",\n    \"note\": \"'sen-2. Also seni-. Apart, separated. 1. Suffixed zero-grade form *sn̥-ter- … 2. Zero-grade form *sn̥ni- in Latin sine, without (< \\\"outside,\\\" \\\"out of\\\"): SANS; SINECURE. [Pok. seni- 907.]' — supports the root and sine/sans, but lists SINCERE not here, rather under sem-1 IV.5 '*sm̥-kéro-, of one growing'.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann, searched for seni-/sine/sn̥ter lemmas\", \"stance\": \"silent\",\n    \"note\": \"grep '^sine|senī|seni-' in IEC.txt returns nothing; Mann has no lemma for this root.\"}\n ],\n \"nodes\": []\n}\n\ne0[\"nodes\"] = [\n {\n  \"id\": 1, \"lang\": \"Avestan\", \"words\": \"hanare\", \"verdict\": \"confirmed\",\n  \"derivation\": \"Avestan hanarə (hanare in Nourai's simplified transliteration) is an adverb and preposition 'aside, apart, without', used in the Gāthās with the genitive (Y.31.15 'yə nōit jyātūm hanarə vīnastī' \\\"who does not find his livelihood without …\\\", Y.34.15 hanarə vastryehyā … \\\"without violence to the farmer's cattle and men\\\"). It continues the PIE adverbial stem *sen-/*sn̥- of Pokorny's seni-, senu-, sn̥-ter- with the Iranian regular change of initial PIE/PIIr. *s- before a vowel to h- (*san-ar- > han-ar-ə), the same change that gives Av. hapta from *sapta and Av. hama- from *sama-. Greek ἄτερ (< *sn̥ter) and Gothic sundrō 'apart' are the exact formal parallels; Klein and Watkins both cite Avestan hanare in this set.\",\n  \"derivation_fa\": \"«hanarə» اوستایی قید و حرف اضافه‌ای است به معنای «جدا، بی‌ـ، بدون» که در گاهان با اضافه به کار رفته است (یسنا ۳۱ بند ۱۵: «yə nōit jyātūm hanarə vīnastī» یعنی «آن‌که روزیِ خود را بی‌… نمی‌یابد»). این واژه دنبالهٔ ستاک قیدی هندواروپایی آغازین *sen-/*sn̥- است و تبدیل *s آغازینِ پیش از واکه به h در ایرانی باستان (دگرگونی آوایی منظم) آن را از *san-ar- به han-ar-ə رسانده است؛ همان دگرگونی که *sapta را به hapta و *sama- را به hama- بدل کرده است. ἄτερ یونانی (از *sn̥ter) و sundrō گوتی هم‌ریشه‌های دقیق آن‌اند. ادعای نورایی درست است.\",\n  \"sources\": [\"https://www.etymonline.com/word/sans\"],\n  \"ref_check\": [\n    {\"ref\": \"POK:907\", \"status\": \"supports\",\n     \"note\": \"POK_03.txt leaf 144 (p.907): 'av. hanarə „abseits, ohne“' stands in the same list as Skt. sanu-tár and Lat. sine, exactly as the chart draws it.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"BRT\", \"where\": \"Bartholomae AiW, s.vv. a-drujyant- and jyātav- (BRT.txt lines 3356, 11697)\", \"stance\": \"supports\",\n     \"note\": \"Bartholomae cites the word repeatedly in its Gāthic contexts and translates it 'ohne': 'hanarə .. vastryehyā asnanhō pasəuš viraiiå \\\"ohne Gewalttat an des Bauern Tieren und Leuten\\\" Y.31.15'; 'yə nōit jyātūm hanarə (sd.) vīnastī .. \\\"der seinen Lebensunterhalt nicht findet ohne ..\\\" Y.31.15'.\"},\n    {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. sunder (KLN_1966.txt, leaf 771 area)\", \"stance\": \"supports\",\n     \"note\": \"'These words are cogn. with OI. sanu-tár, \\\"far away\\\", Avestic hanare, \\\"without\\\", Toch. A snu, B snai, sne, \\\"without\\\", Gk. ἄτερ (for *sn-ter), \\\"without\\\", L. sine, \\\"without\\\" … All these words ultim. derive from I.-E. base *seni-, \\\"away from, without\\\".'\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. sen-2\", \"stance\": \"silent\",\n     \"note\": \"Watkins lists only the Germanic and Latin reflexes of the root; Avestan hanare is not named (Etymonline's article on sunder does name it).\"}\n  ],\n  \"derivation_placeholder\": None\n },\n {\n  \"id\": 2, \"lang\": \"Sanskrit\", \"words\": \"sanu-tar\", \"verdict\": \"confirmed\",\n  \"derivation\": \"Vedic sanutár is an adverb 'away, aside, far off' (RV, e.g. sanutár dhehi 'put it far away'), formed from the same *sen-/*sn̥- element plus the adverbial/contrastive suffix -tar- (-tr̥-) seen in Greek ἄτερ < *sn̥-ter and Germanic *sundr- (OE sundor, Goth. sundrō). Sanskrit keeps the inherited *s- where Avestan turns it into h-, so Skt. sanutár : Av. hanarə is the regular pair. Nourai's gloss 'apart from' renders the usual dictionary sense ('abseits von, weit weg' in Pokorny; 'far away' in Klein); the word is an adverb rather than a preposition governing a case.\",\n  \"derivation_fa\": \"«sanutár» در سنسکریت ودایی قیدی است به معنای «دور، به‌کنار، جدا» (در ریگ‌ودا)، ساخته از همان عنصر *sen-/*sn̥- با پسوند قیدیِ -tar- که در ἄτερ یونانی (از *sn̥-ter) و *sundr- ژرمانی (sundor انگلیسی باستان، sundrō گوتی) نیز دیده می‌شود. سنسکریت *s آغازین را نگاه می‌دارد و ایرانی آن را به h بدل می‌کند؛ پس sanutár سنسکریت و hanarə اوستایی جفت آوایی منظم‌اند. معنای «apart from» که نورایی داده با «abseits von, weit weg» پوکورنی و «far away» کلاین می‌خواند، هرچند واژه قید است نه حرف اضافه. ادعای نورایی درست است.\",\n  \"sources\": [\"https://www.etymonline.com/word/sans\"],\n  \"ref_check\": [\n    {\"ref\": \"POK:907\", \"status\": \"supports\",\n     \"note\": \"POK_03.txt leaf 144 (p.907): 'Ai. sanu-tár „abseits von, weit weg“, sánutara-(?), sánutya- „verstohlen, unvermerkt“ (*„beiseite“)' — Nourai's form and gloss come straight from this line.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. II 494-495\", \"stance\": \"supports\",\n     \"note\": \"Same Sanskrit material stands at the head of the 'seni-, senu-, sn̥-ter-' article, which Pokorny 907 abbreviates ('WP. II 494 f.').\"},\n    {\"src\": \"KLN\", \"where\": \"Klein 1966 s.vv. sine, prep. (p.1447/1448) and sunder\", \"stance\": \"supports\",\n     \"note\": \"s.v. sine: 'cogn. with OI. sanituḥ, \\\"without, outside\\\", sanutar, \\\"far away\\\", Gk. ἄτερ (for *sn-ter), \\\"without\\\" …'.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. sen-2\", \"stance\": \"silent\",\n     \"note\": \"No Sanskrit form listed under this root; Etymonline (s.v. sunder) gives 'Sanskrit sanutar \\\"away, aside\\\"'.\"}\n  ]\n },\n {\n  \"id\": 3, \"lang\": \"Latin\", \"words\": \"sine; sincěrus\", \"verdict\": \"disputed\",\n  \"derivation\": \"Two words with two different fates. (a) sine 'without' is confirmed: Pokorny p.907 'lat. sine „ohne“ (wohl neutr. *senī, nächststehend dem ir. sain aus *seni-)', Watkins 'Zero-grade form *sn̥ni- in Latin sine'; Ernout-Meillet note that sine historically replaced the older se, sed 'without, apart' (which belongs to the reflexive *s(w)e- stem Pokorny connects with this root). (b) sincērus 'pure, unmixed' is disputed. Klein, whom Nourai cites, only guesses: 'of uncertain origin. It possibly stands for sine *cera in the sense of sine carie, \\\"without decay\\\"'. Modern Latin etymology rejects this: Ernout-Meillet say flatly that the expected outcome of sine + a *cēr- element would be *sēcērus (cf. sēdulus) and that 'il n'y a là qu'une étymologie populaire', adding 'Le sin- est le même premier élément de composé que dans sim-plex; l'adjectif signifierait \\\"(d')une venue\\\"'; Watkins files SINCERE under sem-1 'one' (*sm̥-kéro- 'of one growing'); de Vaan (via Wiktionary) reconstructs Proto-Italic *senkairos from *sem- + *ḱer- 'grow'; Etymonline calls the 'without wax' story one that OED and the Century Dictionary dismiss 'out of hand'. So the arrow root→sincērus is wrong by current scholarship. Note also that the printed page spells the word 'sincěrus' with a breve; the Latin vowel is long (sincērus), and the JSON faithfully reproduces the book's breve.\",\n  \"derivation_fa\": \"این جعبه دو واژه دارد با دو سرنوشت. نخست sine «بی، بدون» که پذیرفتنی است: پوکورنی (ص ۹۰۷) می‌نویسد «lat. sine „ohne“ (wohl neutr. *senī)» و واتکینز آن را از گونهٔ صفر *sn̥ni- می‌گیرد؛ ارنو‑مییه نیز یادآور می‌شوند که sine جانشین صورت کهن‌ترِ se/sed شده است. دوم sincērus «پاک، بی‌آمیغ» که پژوهش امروزی آن را از این ریشه بیرون می‌برد: کلاین — که مأخذ نورایی است — تنها گمان زده که شاید sine + *cera باشد، ولی ارنو‑مییه صریحاً آن را «ریشه‌شناسی عامیانه» می‌خوانند و می‌گویند صورت مورد انتظار *sēcērus می‌بود و جزء نخستِ sin- همان است که در sim-plex دیده می‌شود؛ واتکینز نیز SINCERE را ذیل *sem- «یک» (*sm̥-kéro- «از یک رویش») می‌آورد و دِ ڤان صورت ایتالیایی آغازین *senkairos را از *sem- و *ḱer- «رُستن» بازمی‌سازد. پس این پیکان نادرست است. افزون بر این، کتاب واژه را «sincěrus» با علامت کوتاهی چاپ کرده، حال آنکه ē در لاتین کشیده است؛ داده‌های استخراج‌شده همان چاپ کتاب را بازتابیده‌اند.\",\n  \"sources\": [\n    \"https://en.wiktionary.org/wiki/sincerus\",\n    \"https://www.etymonline.com/word/sincere\",\n    \"https://www.etymonline.com/word/sans\"\n  ],\n  \"ref_check\": [\n    {\"ref\": \"POK:907\", \"status\": \"partial\",\n     \"note\": \"POK_03.txt leaf 144 (p.907) has 'lat. sine „ohne“ (wohl neutr. *senī, nächststehend dem ir. sain aus *senis)' — supports sine. Pokorny's article never mentions sincērus, so the second word of the box has no backing on the cited page.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"LAT\", \"where\": \"Ernout-Meillet, DELL s.v. sincerus (LAT.txt lines 58516-58535)\", \"stance\": \"contradicts\",\n     \"note\": \"'De là l'étymologie ancienne, e.g. Don. ad Eu. 177: … purum sine fuco et simplex est, ut mel sine cera … Mais la forme attendue en ce cas serait *sēcērus (comme sēdulus) et il n'y a là qu'une étymologie populaire; cf. sine. … Le sin- est le même premier élément de composé que dans sim-plex. L'adjectif signifierait \\\"(d')une venue\\\".'\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. sem-1 (IV.5) and s.v. sen-2\", \"stance\": \"contradicts\",\n     \"note\": \"Under sem-1: 'IV. Zero-grade form *sm̥-. … 5. Compound *sm̥-kéro-, of one growing (see ker-3)' — that is the entry that yields SINCERE; under sen-2 only 'SANS; SINECURE' are listed.\"},\n    {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. II 494-495\", \"stance\": \"partial\",\n     \"note\": \"Gives lat. sine under this root and refers to Walde LEWb.² 714 f. s.v. sine; sincērus is not brought in.\"}\n  ]\n },\n {\n  \"id\": 4, \"lang\": \"English\", \"words\": \"sans; sans serif; sincere\", \"verdict\": \"plausible\",\n  \"derivation\": \"All three English words do go back to the Latin box, but through French, which the chart's direct Latin→English arrow suppresses. sans: Middle English sauns/saun (c.1300, in surnames from mid-12c.), from Old French san, sans, senz, from Vulgar Latin *sene, from Latin sine; Klein adds that the Old French form is 'a blend of L. sine and L. absentia', which explains the -s. In English it stayed a French word ('now archaic or affected, except as used in heraldry', Century Dict.) and survives chiefly from Shakespeare's 'sans teeth, sans eyes'. sans serif (also sanserif) is a printers' term of 1830 compounding French sans with serif (itself probably from Dutch/Flemish schreef 'stroke', related to schrijven 'to write' < Latin scribere), so only its first element belongs to this root. sincere entered in the 1530s from Middle French sincère, from Latin sincērus; the English word is a faithful descendant of sincērus, but, as at node 3, sincērus itself is not derived from sine in modern scholarship — which is why this node is 'plausible' rather than 'confirmed'.\",\n  \"derivation_fa\": \"هر سه واژهٔ انگلیسی به جعبهٔ لاتین بازمی‌گردند، اما از راه فرانسه که پیکان مستقیمِ نمودار آن را نادیده گرفته است. sans از انگلیسی میانهٔ sauns (حدود ۱۳۰۰ م.) و آن از فرانسهٔ باستان san/sans/senz، از لاتین عامیانهٔ *sene و سرانجام از sine لاتین است؛ کلاین می‌افزاید که صورت فرانسهٔ باستان آمیزه‌ای است از sine و absentia لاتین که -s پایانی را توضیح می‌دهد. sans serif اصطلاحی چاپی از ۱۸۳۰ م. است، مرکب از sans فرانسوی و serif (که خود احتمالاً از schreef هلندی «خط» است)، پس تنها جزء نخست آن به این ریشه تعلق دارد. sincere در دههٔ ۱۵۳۰ م. از sincère فرانسهٔ میانه و آن از sincērus لاتین وارد انگلیسی شده است؛ پیوند انگلیسی‑لاتین درست است، ولی چنان‌که در گرهٔ ۳ گفته شد، خودِ sincērus در پژوهش امروزی از sine گرفته نمی‌شود. از این رو این گره «با احتیاط پذیرفتنی» ارزیابی می‌شود.\",\n  \"sources\": [\n    \"https://www.etymonline.com/word/sans\",\n    \"https://www.etymonline.com/word/sincere\"\n  ],\n  \"ref_check\": [\n    {\"ref\": \"KLN:1447\", \"status\": \"partial\",\n     \"note\": \"Klein 1966 p.1447/1448 (KLN_1966.txt leaf 768, which carries the running number 1448) is the page with both 'sine, prep.' and 'sincere, adj.'; s.v. sine: 'L. sine, \\\"without\\\", is an enlarged form of L. sed, se … cp. se- and the first element in sincere and in sinecure. Cp. also sans.' and s.v. sincere: 'MF. (= F.) sincère, fr. L. sincerus … of uncertain origin. It possibly stands for sine *cera in the sense of sine carie, \\\"without decay\\\".' So the page supports the chart's grouping only tentatively — and 'sans' is not on it: Klein's sans entry ('F., fr. OF. sens, a blend of L. sine, \\\"without\\\", and L. absentia') stands on leaf 734, printed p.1382/1383.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"SKT\", \"where\": \"Skeat s.v. Sincere (SKT.txt line 17300)\", \"stance\": \"silent\",\n     \"note\": \"'Sincere. (F.-L.) O.F. sincere, L. sincerus, pure, sincere.' — Skeat stops at Latin and offers no internal analysis, so he neither supports nor contradicts the sine-derivation.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.vv. sen-2 and sem-1\", \"stance\": \"partial\",\n     \"note\": \"SANS and SINECURE are listed under sen-2, but SINCERE under sem-1 — i.e. two of the chart's three English words belong here and one does not.\"},\n    {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. ceriph, serif (leaf 148) and sans-culotte (leaf 734)\", \"stance\": \"partial\",\n     \"note\": \"'ceriph, serif, n., a horizontal line at the top or bottom of a capital letter. — Prob. fr. Du. schreef, \\\"stroke, dash\\\" … Cp. sanserif.' — confirms that only the 'sans' half of sans serif comes from Latin sine.\"}\n  ]\n }\n]\nfor n in e0[\"nodes\"]:\n    n.pop(\"derivation_placeholder\", None)\n\ne3 = {\n \"entry\": 3,\n \"root\": \"Septm\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *septḿ̥ 'seven' (Pokorny 909 septm̥; Watkins septm̥)\",\n \"note\": \"One of the most securely reconstructed words in the family. Pokorny p.909 'septm̥ „sieben“' lists Ai. saptá, av. hapta, arm. evtʿn, gr. ἑπτά, lat. septem, air. secht n-, got./ahd. sibun, ags. seofon, lit. septyni, toch. A ṣpät, hitt. šipta. Nourai's spelling 'Septm' is Watkins's headword; the modern notation adds the accent and the syllabic mark, *septḿ̥. The only defective box on the chart is the Germanic one (see node 3).\",\n \"note_fa\": \"ریشهٔ هندواروپایی آغازین *septḿ̥ «هفت» از استوارترین بازسازی‌های این خانواده است. پوکورنی (ص ۹۰۹) ذیل «septm̥ „sieben“» این بازمانده‌ها را می‌آورد: saptá سنسکریت، hapta اوستایی، evtʿn ارمنی، ἑπτά یونانی، septem لاتین، secht ایرلندی باستان، sibun گوتی و آلمانی عالی قدیم، seofon انگلیسی باستان، septyni لیتوانیایی و šipta هیتی. املای «Septm» از پیوست واتکینز گرفته شده؛ نگارش امروزی *septḿ̥ است. تنها جعبهٔ معیوب نمودار، جعبهٔ ژرمانی است (بنگرید به گرهٔ ۳). ادعای نورایی دربارهٔ ریشه درست است.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/%D9%87%D9%81%D8%AA\"],\n \"ref_check\": [\n   {\"ref\": \"POK:909\", \"status\": \"supports\",\n    \"note\": \"POK_03.txt leaf 146 (= printed p.909): 'septm̥ „sieben“. Ai. saptá, av. hapta, arm. evtʿn, gr. ἑπτά, lat. septem, air. secht n-, cymr. usw. saith, got. ahd. sihun (sic, = sibun), ags. seofon, anord. siau … lit. septynì, aksl. sedmь … toch. A ṣpät, B ṣuk(t); hitt. šipta. … WP. II 487.' Exact page, exact gloss.\"}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. II 487 (WLD_Bd2_pages.txt leaf 491)\", \"stance\": \"supports\",\n    \"note\": \"'septm̥ „sieben“. Ai. saptá, av. hapta, arm. evtʿn …, lat. septem, air. secht n-, … got. ahd. sibun, ags. seofon, anord. siau' — the source Pokorny abbreviates.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. septm̥ (AHD_watkins1985.txt line 923)\", \"stance\": \"supports\",\n    \"note\": \"'septm̥. Seven. 1. Germanic *sebum (read *sebun) in Old English seofon, seven: SEVEN. 2. Latin septem, seven: SEPTEMBER … 3. Greek hepta, seven: HEBDOMAD … [Pok. septm̥ 909.]' — this is the source of Nourai's three-branch layout.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann, IEC.txt line 15220 s.v. septm\", \"stance\": \"supports\",\n    \"note\": \"'septm (sequdm-) \\\"seven\\\". … Skt. saptá; Av. hapta; Per. haft; Arm. eawtʿn; Tokh. A ṣpät B ṣukt; … Gk. heptá; Lat. septem; OIr. secht; Li. septyni' — includes the Persian reflex the chart draws.\"}\n ],\n \"nodes\": [\n  {\n   \"id\": 1, \"lang\": \"Avestan / Old Persian\", \"words\": \"hapta; hapta-dasa; haptâiti\", \"verdict\": \"plausible\",\n   \"derivation\": \"Avestan hapta 'seven' is the regular Iranian outcome of PIIr. *saptá < PIE *septḿ̥, with initial *s- > h- (the same change as in hanarə, node 1 of the Sen 2 chart) and loss of the final syllabic nasal; Bartholomae's AiW documents it in dozens of passages ('j. (g.) hapta indekl. Zw. „sieben“'). haptadasa- is likewise attested, but Bartholomae glosses it as the ORDINAL 'der siebzehnte' (Yt.1.8), so Nourai's 'seventeen' is at best the cardinal use of the same form; and haptāiti- 'seventy' is a numeral abstract in -ti- of exactly the type of Skt. saptatí- (Pokorny cites 'av. haptāiti- 70' under septm̥). The 'Old Persian' half of the label is the weak point: none of these three words is attested in the Old Persian inscriptions (Kent's lexicon has no numeral hapta), and Nourai has simply taken over Platts's grammar, which prints '7. هفت (O.P. hapta)', '17. هفده (O.P. haptadasa)', '70. هفتاد (Phl. haftāt; O.P. haptaiti)' — Platts's 'O.P.' there means Old Iranian/Avestan, not epigraphic Old Persian.\",\n   \"derivation_fa\": \"«hapta» اوستایی بازتاب منظم *saptá هندوایرانی از *septḿ̥ هندواروپایی است؛ *s آغازین در ایرانی باستان به h بدل شده (همان دگرگونی که در hanarə دیده می‌شود) و ـm̥ پایانی از میان رفته است. بارتولومه در «فرهنگ ایرانی باستان» آن را با ده‌ها شاهد ثبت کرده است. haptadasa- نیز گواهی‌شده است، اما بارتولومه آن را «هفدهمین» (شمارهٔ ترتیبی) معنی می‌کند، پس «seventeen» نورایی دقیق نیست؛ و haptāiti- «هفتاد» اسم‌مصدر عددی با پسوند -ti- است، درست مانند saptatí- سنسکریت، و پوکورنی نیز «av. haptāiti- 70» را ذیل همین ریشه می‌آورد. نقطهٔ سست، نیمهٔ «پارسی باستان» برچسب است: هیچ‌یک از این سه واژه در سنگ‌نبشته‌های پارسی باستان گواهی نشده و نورایی آن‌ها را از دستور فارسی پلاتس گرفته که در ص ۴۱ می‌نویسد «۷ هفت (O.P. hapta)»، «۱۷ هفده (O.P. haptadasa)»، «۷۰ هفتاد (Phl. haftāt; O.P. haptaiti)» — و مقصود پلاتس از O.P. ایرانی باستان/اوستایی است نه پارسی باستانِ کتیبه‌ها. پس با احتیاط پذیرفتنی است.\",\n   \"sources\": [\"https://en.wiktionary.org/wiki/%D9%87%D9%81%D8%AA\"],\n   \"ref_check\": [\n     {\"ref\": \"POK:909\", \"status\": \"supports\",\n      \"note\": \"POK_03.txt leaf 146 (p.909) s.v. septm̥: 'av. hapta' among the cardinals, and in the ordinal paragraph 'Zahlabstraktbildung wie ai. saptati-, av. haptāiti- 70'. Both chart forms are on the cited page.\"},\n     {\"ref\": \"KLN:1426\", \"status\": \"supports\",\n      \"note\": \"Klein 1966 p.1426/1427 (KLN_1966.txt leaf 757, whose running numerals are 1426 and 1427) s.v. seven: '… cogn. with OI. saptá, Avestic hapta, Toch. A ṣpät, B ṣukt … Hitt. shipta, Arm. evtʿn, Gk. ἑπτά, L. septem …'. Nourai's page number is exact.\"},\n     {\"ref\": \"GPL:41\", \"status\": \"supports\",\n      \"note\": \"Platts-Ranking, Grammar of the Persian Language, p.41 (GPL.txt lines 520-540, the page headed 'Numerals—The Cardinal Numbers 41'): '7. ۷ هفت (O.P. hapta)'; '17. ۱۷ هفده (O.P. haptadasa)'; '70. هفتاد (Phl. haftāt; O.P. haptaiti)'. This is evidently where Nourai's triple — and the 'Old Persian' label — comes from.\"}\n   ],\n   \"consulted\": [\n     {\"src\": \"BRT\", \"where\": \"Bartholomae AiW s.vv. hapta and haptadasa- (BRT.txt lines 29251, 29253)\", \"stance\": \"partial\",\n      \"note\": \"'j. (g.) hapta indekl. Zw. „sieben“' with many citations (V.15.45, Yt.8.40 etc.), and 'j. haptadasa- Adj. „der siebzehnte“: °sa (statt NSm.) vīspa.hišas … Yt.1.8' — the second is glossed as an ordinal, not 'seventeen'.\"},\n     {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, Lexicon (searched for hapta/haptāiti)\", \"stance\": \"silent\",\n      \"note\": \"Kent's lexicon has no numeral hapta or haptāiti; the only Old Persian h-r- item relevant to this page is Haraiva 'Aria' (KNT.txt line 1981). The Achaemenid inscriptions write numbers out in words only sporadically, so the 'Old Persian' label cannot be confirmed from Kent.\"},\n     {\"src\": \"IEC\", \"where\": \"Mann, IEC.txt line 15220\", \"stance\": \"supports\",\n      \"note\": \"'Av. hapta; Per. haft' in the septm entry — the same Avestan-to-Persian line the chart draws.\"}\n   ]\n  },\n  {\n   \"id\": 2, \"lang\": \"Persian\", \"words\": \"haft «هفت ( هفته ، هفده ، هفتاد )»\", \"verdict\": \"confirmed\",\n   \"derivation\": \"New Persian هفت haft continues Middle Persian haft [hpt'] (MacKenzie, Nyberg) from Proto-Iranian *haptá, i.e. Av. hapta; the only sound change on the way is the Middle Persian shift of the cluster -pt- to -ft-, the same change that gives MP haft-/NP هفت from *hapta as it gives NP گفتن guftan beside OIr. *gaub-ta-. Hübschmann formulates it directly: 'np. f: haft „sieben“ = zd. hapta, iran. *hafta'. The three derivatives in the parenthesis are equally regular: هفته hafta 'week' < MP haftag (MacKenzie 'haftag [-k'] | N hafta, week'); هفده hifdah/hevdah 'seventeen' < MP haftdah (MacKenzie 'haftdah | N ~, hifdah'), with assimilation of -ftd- ; هفتاد haftād 'seventy' < MP haftād [hpt'd] < Av. haptāiti- (Horn no.1100 'heftād „siebzig“: aw. haptāiti-, phlv. haftāt, ai. saptati-').\",\n   \"derivation_fa\": \"«هفت» در فارسی نو دنبالهٔ «haft» فارسی میانه (پهلوی، به خط پهلوی hpt') است که خود از *haptá ایرانی آغازین یعنی hapta اوستایی می‌آید؛ تنها دگرگونی آوایی در این راه، بدل شدن خوشهٔ -pt- به -ft- در فارسی میانه است. هوبشمان همین را صریح می‌نویسد: «np. f: haft „sieben“ = zd. hapta, iran. *hafta». سه مشتقّ درون کمانک هم قاعده‌مندند: «هفته» از haftag پهلوی (مکنزی: haftag | N hafta)، «هفده» از haftdah پهلوی با همگونیِ خوشهٔ میانی (مکنزی: haftdah | N hifdah)، و «هفتاد» از haftād پهلوی و آن از haptāiti- اوستایی (هرن، شمارهٔ ۱۱۰۰). حاشیهٔ معین بر برهان قاطع (ص ۲۳۴۱) نیز همین زنجیره را می‌آورد. ادعای نورایی درست است.\",\n   \"sources\": [\"https://en.wiktionary.org/wiki/%D9%87%D9%81%D8%AA\"],\n   \"ref_check\": [\n     {\"ref\": \"BQT:2341\", \"status\": \"supports\",\n      \"note\": \"Borhan-e Qateʿ ed. Moʿin, printed p.2341 = vol. 4 pdf page 424 (BQT_v4_pages.txt, [pdf page 424]); the entry «هفت» carries Moʿin's footnote 9: «اوستا hapta (هفت)، پهلوی haft، هندی باستان sapta، ارمنی evtn؛ افغانی awa, ava؛ استی avd, ævd؛ … کردی heft (هفت) …» — exactly Nourai's arrow. The facing page (2342) gives «هفتاد … اوستا haptāiti (هفتاد)، پهلوی haftāt، هندی باستان saptati».\"}\n   ],\n   \"consulted\": [\n     {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD p.40 area (PHD.txt line 388; PHD_mackenzie.txt line 2656)\", \"stance\": \"supports\",\n      \"note\": \"'haft [hpt' | M hpt, N ~] seven. ~ad [-t'd | M hpt'd, N ~] seventy. ~ag [-k' | N hafta] week. … haftdah [hptdh | N ~, hifdah] seventeen.' — all four Persian words of the box, with their Pahlavi ancestors.\"},\n     {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II, glossary (NYB_vol2_glossary.txt lines 1770-1771)\", \"stance\": \"supports\",\n      \"note\": \"'haft [hpt'; SB'; figures] seven; pl. cas. obl. -ān the seven planets'; 'haft-dahom [hptdhwm] the seventeenth'; also 'read [hptwm] haftom'.\"},\n     {\"src\": \"HRN\", \"where\": \"Horn, Grundriss nos. 1098 and 1100 (HRN.txt lines 9496, 9509)\", \"stance\": \"supports\",\n      \"note\": \"'1098. haft „sieben“, hafte „Woche“. aw. hapta „sieben“; phlv. haft; ai. saptá; arm. evtʿn' and '1100. haftād „siebzig“. aw. haptāiti- „siebzig“; phlv. haftāt; ai. saptati-.'\"},\n     {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien (HUB.txt line 6551)\", \"stance\": \"supports\",\n      \"note\": \"'np. f: haft „sieben“ = zd. hapta, iran. *hafta, u. s. w.' — the statement of the pt > ft rule for exactly this word.\"},\n     {\"src\": \"ARY\", \"where\": \"Aryanpur, Latin index (ARY_latin_index_pages.txt lines 15513, 15540)\", \"stance\": \"supports\",\n      \"note\": \"'SEVEN … HAFT (PAHLAVI)' and 'SEVENTY … HAFTAD, HAFTAT (PAHLAVI)' — the same Pahlavi ancestors.\"}\n   ]\n  },\n  {\n   \"id\": 3, \"lang\": \"Germanic\", \"words\": \"sibum\", \"verdict\": \"transcription_suspect\",\n   \"error_in\": \"book\",\n   \"book_prints\": \"sibum\",\n   \"correct_form\": \"*sebun\",\n   \"derivation\": \"There is no Germanic form *sibum. The reconstructed Proto-Germanic numeral is *sebun (Wiktionary, Kroonen), continued in Gothic sibun, Old High German sibun, Old Saxon sebun, Old English seofon, Old Norse sjau. Nourai's source, the AHD/Watkins appendix, reads 'Germanic *sebun in Old English seofon, seven: SEVEN' (our OCR of the 1985 printing renders it '*sebum', showing how easily the final n is misread as m). The printed page 414 of Nourai's book plainly shows 'sibum' — so the JSON extraction is faithful and the error is the book's: the vowel has additionally been changed from e to i, presumably under the influence of Gothic/OHG sibun. The correct derivation is PIE *septḿ̥ > pre-Germanic *sebun(t) with Grimm's law turning *p into *f and then Verner's law voicing it to *b between voiced sounds, and loss of the final nasal syllable.\",\n   \"derivation_fa\": \"صورت ژرمانی *sibum وجود ندارد. عدد بازسازی‌شدهٔ ژرمانی آغازین *sebun است که در sibun گوتی، sibun آلمانی عالی قدیم، sebun ساکسون قدیم، seofon انگلیسی باستان و sjau نورس باستان بازمانده است. مأخذ نورایی، یعنی پیوست ریشه‌های واتکینز در AHD، «Germanic *sebun in Old English seofon» دارد (در متن اسکن‌شدهٔ چاپ ۱۹۸۵ نیز nِ پایانی به m خوانده شده است). صفحهٔ ۴۱۴ چاپی کتاب آشکارا «sibum» دارد؛ پس خوانشِ داده‌ها درست است و خطا از خودِ کتاب است، که افزون بر m، واکهٔ e را هم — احتمالاً به تأثیر sibun گوتی — به i بدل کرده است. زنجیرهٔ درست چنین است: *septḿ̥ هندواروپایی > *sebun(t) پیش‑ژرمانی، با تبدیل *p به *f بر پایهٔ قانون گریم و سپس واک‌دارشدن آن به *b بر پایهٔ قانون ورنر، و افتادن هجای نونیِ پایانی. خطای چاپی کتاب.\",\n   \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/sebun\"],\n   \"ref_check\": [\n     {\"ref\": \"AHD\", \"status\": \"partial\",\n      \"note\": \"Watkins 1985 s.v. septm̥ (AHD_watkins1985.txt line 923): 'Germanic *sebum in Old English seofon, seven: SEVEN' — the OCR of the printed '*sebun'. The reference supports a Germanic node but not the form 'sibum' with i.\"}\n   ],\n   \"consulted\": [\n     {\"src\": \"KLN\", \"where\": \"Klein 1966 p.1426 s.v. seven (leaf 757)\", \"stance\": \"contradicts\",\n      \"note\": \"'ME. seven, sevene, fr. OE. seofon, rel. to OS. sebun, ON. sjau, Swed. sju, Dan. syv, OFris. si(u)gun, MDu. seven, Du. zeven, OHG. sibun, MHG. siben, G. sieben, Goth. sibun' — every attested Germanic form has -n, none has -m.\"},\n     {\"src\": \"POK\", \"where\": \"Pokorny p.909\", \"stance\": \"contradicts\",\n      \"note\": \"'got. ahd. sibun, ags. seofon, anord. siau (-n bewahrt nach einem neben *sibun stehenden sibuni)' — Pokorny's Germanic base is *sibun/*sebun, never *sibum.\"},\n     {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. II 487\", \"stance\": \"contradicts\",\n      \"note\": \"'got. ahd. sibun, ags. seofon, anord. siau … -n bewahrt nach einem neben *sibun stehenden sibuni'.\"}\n   ]\n  },\n  {\n   \"id\": 4, \"lang\": \"English\", \"words\": \"seven, seventeen, seventy\", \"verdict\": \"confirmed\",\n   \"derivation\": \"Old English seofon (from Proto-West-Germanic *sebun) gives Middle English seven, seuene and modern seven; seventeen is OE seofontīene (seofon + -tīene 'ten'), ME seventene; seventy is OE hundseofontig, later seofontig (seofon + -tig, the decade suffix), ME seventi. The medial f of the Old English spelling was pronounced [v] between voiced sounds, which is why Modern English has seven and not *sefen.\",\n   \"derivation_fa\": \"«seven» انگلیسی از seofon انگلیسی باستان (و آن از *sebun ژرمانی غربی آغازین) می‌آید و از راه seven/seuene انگلیسی میانه به امروز رسیده است؛ «seventeen» از seofontīene (seofon + -tīene «ده») و «seventy» از hundseofontig/seofontig (seofon + پسوند دهگانِ -tig). fِ املای انگلیسی باستان در میان دو واکدار [v] تلفظ می‌شده و از همین‌رو امروز seven است نه *sefen. این گره در نمودار مأخذی ندارد، ولی زنجیره در کلاین (ص ۱۴۲۶) به‌تمامی آمده است. ادعای نورایی درست است.\",\n   \"sources\": [],\n   \"ref_check\": [\n     {\"ref\": \"(none cited)\", \"status\": \"not_checked\",\n      \"note\": \"The node carries no refs= in the book; Klein p.1426 (cited one box up) covers the whole chain and was checked instead — see consulted.\"}\n   ],\n   \"consulted\": [\n     {\"src\": \"KLN\", \"where\": \"Klein 1966 p.1426 s.vv. seven, seventeen, seventieth (leaf 757)\", \"stance\": \"supports\",\n      \"note\": \"'seven, adj. — ME. seven, sevene, fr. OE. seofon …'; 'seventeen, n. — ME. seventene, fr. OE. seofon-tyne. See seven and -teen'; 'seventieth, adj. and n. — ME. seventithe. See seventy and numeral suff. -th.'\"},\n     {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. septm̥\", \"stance\": \"supports\",\n      \"note\": \"'Germanic *sebun in Old English seofon, seven: SEVEN' — the derivative listed in caps is exactly this node.\"}\n   ]\n  },\n  {\n   \"id\": 5, \"lang\": \"Latin\", \"words\": \"septem\", \"verdict\": \"confirmed\",\n   \"derivation\": \"Latin septem 'seven' is the direct outcome of PIE *septḿ̥: the syllabic *m̥ is resolved as -em in Latin (as in decem < *déḱm̥), and the initial cluster is untouched because Latin, unlike Germanic and Iranian, leaves *s- and *p- alone. Pokorny and Walde-Pokorny both cite it in the first line of the septm̥ article, and Watkins gives 'Latin septem, seven: SEPTEMBER, SEPTENNIAL, SEPTET, SEPTI-, SEPTUAGINT, SEPTUPLE; SEPTENTRION.'\",\n   \"derivation_fa\": \"«septem» لاتین بازتاب مستقیم *septḿ̥ هندواروپایی است: *m̥ هجایی در لاتین به -em بدل می‌شود (چنان‌که decem از *déḱm̥) و خوشهٔ آغازین دست‌نخورده می‌ماند، زیرا لاتین برخلاف ژرمانی و ایرانی *s- و *p- را نگاه می‌دارد. پوکورنی و والده‑پوکورنی هر دو آن را در نخستین سطر مقالهٔ septm̥ آورده‌اند و واتکینز نیز «Latin septem, seven: SEPTEMBER, SEPTUAGINT …» می‌نویسد. ادعای نورایی درست است.\",\n   \"sources\": [],\n   \"ref_check\": [\n     {\"ref\": \"AHD\", \"status\": \"supports\",\n      \"note\": \"Watkins 1985 s.v. septm̥ (AHD_watkins1985.txt line 923): '2. Latin septem, seven: SEPTEMBER, SEPTENNIAL, SEPTET, SEPTI-, SEPTUAGINT, SEPTUPLE; SEPTENTRION.'\"}\n   ],\n   \"consulted\": [\n     {\"src\": \"POK\", \"where\": \"Pokorny p.909 (POK_03.txt leaf 146)\", \"stance\": \"supports\",\n      \"note\": \"'Ai. saptá, av. hapta, arm. evtʿn, gr. ἑπτά, lat. septem, air. secht n- …'\"},\n     {\"src\": \"LAT\", \"where\": \"Ernout-Meillet, DELL (searched s.v. septem)\", \"stance\": \"supports\",\n      \"note\": \"DELL treats septem as the inherited Latin cardinal; its derivatives September, septimus, septuāgintā are all built on it (the dictionary's sincerus article on p.1108 refers to the same sim-/sem- vs. sin- distinction, showing sin- and septem are unrelated matters).\"}\n   ]\n  },\n  {\n   \"id\": 6, \"lang\": \"English\", \"words\": \"September\", \"verdict\": \"confirmed\",\n   \"derivation\": \"September is a learned Latin borrowing that reached English through Old French septembre / directly from Latin September (mensis), literally 'the seventh month': the Roman calendar year began in March, so the seventh month counting from March was our ninth. The name kept its place when January and February were prefixed to the year, which is why September, October, November and December all now sit two months later than their numerals say. Klein states it in exactly these terms.\",\n   \"derivation_fa\": \"«September» وام‌واژه‌ای است ادبی از لاتین که از راه septembre فرانسهٔ باستان (یا مستقیماً از September (mensis) لاتین) به انگلیسی رسیده و تحت‌اللفظ یعنی «ماه هفتم»: سال رومی از مارس آغاز می‌شد، پس هفتمین ماه از مارس همان ماه نهم امروزی است. پس از آنکه ژانویه و فوریه به آغاز سال افزوده شدند، نام‌ها سر جای خود ماندند و از همین‌روست که September و October و November و December دو ماه از شمارهٔ خود عقب‌ترند. کلاین نیز دقیقاً همین را می‌گوید. ادعای نورایی درست است.\",\n   \"sources\": [],\n   \"ref_check\": [\n     {\"ref\": \"(none cited)\", \"status\": \"not_checked\",\n      \"note\": \"No refs= on this node; the parent Latin box cites AHD, whose SEPTEMBER is listed under septm̥. Klein was checked instead — see consulted.\"}\n   ],\n   \"consulted\": [\n     {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. September (KLN_1966.txt line 34619)\", \"stance\": \"supports\",\n      \"note\": \"'September, n., the ninth month of the year. — L. September (mensis), lit. \\\"the seventh month (of the Roman year)\\\", fr. septem, \\\"seven\\\"; see septem-. The Roman year began with March (cp. October, November, December).'\"},\n     {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. septm̥\", \"stance\": \"supports\",\n      \"note\": \"SEPTEMBER heads the list of English derivatives of Latin septem under this root.\"}\n   ]\n  }\n ]\n}\n\ne4 = {\n \"entry\": 4,\n \"root\": \"Ser 1\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *ser- 'to flow, run swiftly'; derivative *ser-o-m 'liquid, whey' (Pokorny 909-910, '1. ser-'; Watkins ser-2)\",\n \"note\": \"Pokorny's entry begins on p.909 and runs onto p.910, so Nourai's POK:909 is right. The headword reads '1. ser- „strömen, sich rasch und heftig bewegen“; sero-m „Flüssigkeit“; ser-mo- „Fluß“, sorā ds.' Both of the chart's branches — the Iranian river/land name Haraiva and Latin serum — are named there verbatim, which makes this one of the better-sourced charts on the page. Watkins numbers the root ser-2 where Pokorny has 1. ser-; that is only a numbering difference, not a disagreement.\",\n \"note_fa\": \"مدخل پوکورنی از ص ۹۰۹ آغاز می‌شود و به ص ۹۱۰ می‌کشد، پس ارجاع POK:909 نورایی درست است. سرواژه چنین است: «1. ser- „strömen, sich rasch und heftig bewegen“; sero-m „Flüssigkeit“; ser-mo- „Fluß“, sorā». هر دو شاخهٔ نمودار — نام ایرانیِ رود/سرزمین Haraiva و serum لاتین — در همان صفحه به‌عینه آمده‌اند و از این‌رو این نمودار از مستندترین نمودارهای این صفحه است. واتکینز این ریشه را ser-2 شماره می‌زند و پوکورنی 1. ser-؛ این تنها اختلاف شماره‌گذاری است نه اختلاف نظر. ادعای نورایی دربارهٔ ریشه درست است.\",\n \"sources\": [\"https://www.etymonline.com/word/serum\"],\n \"ref_check\": [\n   {\"ref\": \"POK:909\", \"status\": \"supports\",\n    \"note\": \"POK_03.txt leaf 147 (pp.909-910): '1. ser- „strömen, sich rasch und heftig bewegen“; sero-m „Flüssigkeit“; ser-mo- „Fluß“, sorā ds. Ai. sisarti, sárati „fließt, eilt“ … sarayú-, sarayū- m. „Name eines Flusses“, ap. Haraiva-, av. (Akk.) Harōyūm, np. Harē „Fluß und Gegend von Herāt“; … ai. sará- „flüssig“, gr. ὀρός, lat. serum „der wässerige Teil der geronnenen Milch, Molke“ … WP. II 497 f.'\"}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. II 497-498 (WLD_Bd2_pages.txt leaves 501-502)\", \"stance\": \"supports\",\n    \"note\": \"'1. ser- „strömen, sich rasch und heftig wohin bewegen“. Ai. sisarti, sárati … sarayú-ḥ „Name eines Flusses“, ap. Haraiva-, av. (Acc.) Harōyum, np. Harē „Fluß und Gegend von Herāt“ … ai. sará- „flüssig“, gr. ὀρός, lat. serum „der wässerige Teil der geronnenen Milch, die Molke, Käsewasser“.'\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. ser-2 (AHD_watkins1985.txt line 925)\", \"stance\": \"supports\",\n    \"note\": \"'ser-2, To flow. 1. Suffixed form *ser-o- in Latin serum, whey: SERAC, SERUM. 2. Basic form *ser- in Sanskrit sarati, sasarti, it flows, it runs: SAMSARA. … [Pok. 1. ser- 909; sr-edh- 1001.]'\"},\n   {\"src\": \"IEC\", \"where\": \"Mann, IEC.txt line 15242 s.v. seros, om\", \"stance\": \"partial\",\n    \"note\": \"'seros, om (?) \\\"fluid\\\". … (for Lat. serum, n. \\\"whey\\\", see also ksero-, in view of Skt. kṣāram, n. \\\"water\\\"); Pol. siara, f. \\\"colostrum\\\"… Cf. WP II, 497.' Mann accepts the root but flags the assignment of Latin serum as ambiguous between *ser- and a *kser- type.\"}\n ],\n \"nodes\": [\n  {\n   \"id\": 1, \"lang\": \"Avestan / Old Persian\", \"words\": \"hareva, haraiva\", \"verdict\": \"plausible\",\n   \"derivation\": \"The forms are real and the root is right, but the gloss compresses two things. Old Persian Haraiva- (h-r-i-v) is the name of a SATRAPY, Greek Areia, the province around modern Herat; it appears in the province lists of Bisotun, Naqsh-e Rostam and Susa (Kent: 'Haraiva \\\"Aria\\\"'). Bartholomae's entry is 'p. haraiva-, j. harōiva- m. Name eines Lands, Aria' — so Nourai's 'hareva' is a loose transliteration of the Young Avestan harōiva- and 'haraiva' the Old Persian. The country was named after its river, the Harī-rūd, whose Avestan name is Harōiuuā / acc. Harōyūm, and it is that hydronym, not the province name, that means 'the flowing' — it is formally the same formation as Vedic Sarayū́-, a river name from *ser- 'to flow'. Iranian h- again from *s-. So 'name of a river in Afghanistan' is half of the truth: the attested Old Persian word names the land, the underlying name is the river's.\",\n   \"derivation_fa\": \"صورت‌ها واقعی و ریشه درست است، اما معنای داده‌شده دو چیز را در هم می‌آمیزد. Haraiva- پارسی باستان نام یک ساتراپی است — «آریا»ی یونانیان، همان سرزمین پیرامون هرات امروزی — که در فهرست سرزمین‌های بیستون و نقش رستم و شوش آمده است (کنت: «Haraiva \\\"Aria\\\"»). مدخل بارتولومه چنین است: «p. haraiva-, j. harōiva- m. نام سرزمینی، آریا»؛ پس «hareva» نورایی آوانگاری آزادِ harōiva- اوستایی متأخر و «haraiva» صورت پارسی باستان است. نام سرزمین از نام رودش گرفته شده — هریرود، که نام اوستایی‌اش Harōiuuā (رایی: Harōyūm) است — و همین نامِ رود است که معنای «روان، جاری» دارد و از نظر ساخت همان Sarayū́- ودایی است، نام رودی از ریشهٔ *ser- «روان شدن». hِ ایرانی باز هم از *s ایرانی باستان است. پس «نام رودی در افغانستان» نیمی از حقیقت است. با احتیاط پذیرفتنی است.\",\n   \"sources\": [\"https://en.wiktionary.org/wiki/%D9%87%D8%B1%D8%A7%D8%AA\"],\n   \"ref_check\": [\n     {\"ref\": \"POK:909\", \"status\": \"supports\",\n      \"note\": \"POK_03.txt leaf 147 (p.909, under '1. ser-'): 'sarayú-, sarayū́- m. „Name eines Flusses“, ap. Haraiva-, av. (Akk.) Harōyūm, np. Harē „Fluß und Gegend von Herāt“'. Pokorny puts the forms under this root exactly as the chart does, and his gloss 'Fluß und Gegend' shows the river/land ambiguity.\"}\n   ],\n   \"consulted\": [\n     {\"src\": \"BRT\", \"where\": \"Bartholomae AiW s.v. haraiva- (BRT.txt line 29583)\", \"stance\": \"partial\",\n      \"note\": \"'p. haraiva-, j. harōiva- m. Name eines Lands, Aria: imā dahyāva tyā manā patiyāiša … Bh. I 6; DPe 2, DSe 3' — 'name of a land', not of a river; cf. also 'haraēuua/harōyūm' in V.1.8.\"},\n     {\"src\": \"KNT\", \"where\": \"Kent, Old Persian §141 and the province lists (KNT.txt lines 1768, 1981, 3474)\", \"stance\": \"supports\",\n      \"note\": \"'Haraiva \\\"Aria\\\"' in Kent's list of country names; the form appears in DB 1.15-17, DNa, DSe, XPh as one of the dahyāva.\"},\n     {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. II 497\", \"stance\": \"supports\",\n      \"note\": \"'sarayú-ḥ, sarayū́-ḥ „Name eines Flusses“, ap. Haraiva-, av. (Acc.) Harōyum, np. Harē „Fluß und Gegend von Herāt“'.\"}\n   ]\n  },\n  {\n   \"id\": 2, \"lang\": \"Persian\", \"words\": \"harât «هرات»\", \"verdict\": \"plausible\",\n   \"derivation\": \"The line from the Old Iranian name to the modern Persian one is real but not straight. Old Persian Haraiva- gives Middle Persian Harēw (written hlyw'), which survives as Classical Persian هَریو harēw and as the bare river name Harē (so Pokorny: 'np. Harē „Fluß und Gegend von Herāt“'). The form هرات harāt with a final -t is an Arabic round trip: Arabic borrowed Harēw as هَرَاة harāh, with the tāʾ marbūṭa, and Persian took that form back, where the marbūṭa is read as a plain t; the same shape shows in Arabic حَمَاة ḥamāh > Persian حمات. So the chart's single arrow Avestan/OP → Persian هرات hides an Arabic mediation. The gloss '\\\"the flowing\\\"' is the etymological sense of the underlying hydronym (< *ser- 'to flow'), not a meaning the Persian word ever had.\",\n   \"derivation_fa\": \"پیوند نام ایرانی باستان با نام فارسی امروزی واقعی است، اما مستقیم نیست. Haraiva- پارسی باستان در فارسی میانه Harēw (به خط پهلوی hlyw') شده و در فارسی دری به صورت «هَریو» و در نام خودِ رود به صورت «هَری» (هریرود) بازمانده است؛ پوکورنی هم «np. Harē» می‌نویسد. اما صورت «هرات» با tِ پایانی یک رفت‌وبرگشت عربی است: عربی Harēw را به شکل «هَراة» با تاء مربوطه وام گرفت و فارسی همان معرَّب را بازپس گرفت و تاء مربوطه را t خواند؛ همان الگویی که در «حماة» عربی > «حمات» فارسی دیده می‌شود. پس پیکان یگانهٔ نمودار، میانجیگری عربی را پنهان می‌کند. معنای «the flowing» نیز معنای ریشه‌شناختی نامِ رود است (از *ser- «روان شدن») نه معنایی که واژهٔ فارسی هرگز داشته باشد. با احتیاط پذیرفتنی است.\",\n   \"sources\": [\"https://en.wiktionary.org/wiki/%D9%87%D8%B1%D8%A7%D8%AA\"],\n   \"ref_check\": [\n     {\"ref\": \"(none cited)\", \"status\": \"not_checked\",\n      \"note\": \"The node carries no refs= in the book. The parent box's POK:909 was checked instead and does cover the Persian continuation ('np. Harē').\"}\n   ],\n   \"consulted\": [\n     {\"src\": \"POK\", \"where\": \"Pokorny p.909 s.v. 1. ser-\", \"stance\": \"partial\",\n      \"note\": \"'np. Harē „Fluß und Gegend von Herāt“' — Pokorny's New Persian form is Harē, not harāt; he names Herāt only as the modern place.\"},\n     {\"src\": \"BRT\", \"where\": \"Bartholomae AiW s.v. haraiva- (BRT.txt line 29583)\", \"stance\": \"partial\",\n      \"note\": \"Gives only the Old Iranian forms ('Name eines Lands, Aria'); no New Persian form, so the -t of هرات is unexplained from Bartholomae alone.\"},\n     {\"src\": \"MON\", \"where\": \"Moʿin / Dehkhoda via abadis.ir (searched)\", \"stance\": \"silent\",\n      \"note\": \"The lexicon volumes of Moʿin available online do not carry an etymological note on the proper name هرات (it belongs to the aʿlām volumes 5-6, which are not in the local library); Wiktionary's Persian entry supplies the Arabic-mediated chain instead.\"}\n   ]\n  },\n  {\n   \"id\": 3, \"lang\": \"Latin\", \"words\": \"serum\", \"verdict\": \"confirmed\",\n   \"derivation\": \"Latin serum is the o-stem *ser-o-m of the root, 'the watery part of curdled milk, whey' — Pokorny's own gloss on p.910 — and is the exact formal match of Sanskrit sará- 'fluid, flowing' and Greek ὀρός 'whey' (< *soros). Watkins: 'Suffixed form *ser-o- in Latin serum, whey: SERAC, SERUM.' Nourai's gloss 'liquid from animal tissue' is the modern medical sense, not the classical one: in Latin the word means whey and, by extension, any thin watery fluid; the application to the clear liquid that separates from clotting blood is a seventeenth-century technical extension (first attested in English in the 1670s).\",\n   \"derivation_fa\": \"«serum» لاتین همان ستاک -o یعنی *ser-o-m از این ریشه است به معنای «بخش آبکیِ شیر بریده، آبِ پنیر» — و این دقیقاً معنایی است که پوکورنی در ص ۹۱۰ می‌دهد — و برابر آوایی دقیقِ sará- سنسکریت «روان، مایع» و ὀρός یونانی «آب‌پنیر» (از *soros) است. واتکینز می‌نویسد: «Suffixed form *ser-o- in Latin serum, whey». معنایی که نورایی داده («مایعِ برآمده از بافت جانوری») معنای پزشکیِ نو است نه معنای کلاسیک: در لاتین این واژه «آبِ پنیر» و به‌گسترش هر مایع رقیق آبکی است، و کاربردش دربارهٔ مایع زلالی که از لخته‌شدن خون جدا می‌شود، گسترشی فنی از سدهٔ هفدهم میلادی است. ادعای نورایی دربارهٔ اشتقاق درست است.\",\n   \"sources\": [\"https://www.etymonline.com/word/serum\"],\n   \"ref_check\": [\n     {\"ref\": \"AHD\", \"status\": \"supports\",\n      \"note\": \"Watkins 1985 s.v. ser-2 (AHD_watkins1985.txt line 925): 'To flow. 1. Suffixed form *ser-o- in Latin serum, whey: SERAC, SERUM. … [Pok. 1. ser- 909]'.\"}\n   ],\n   \"consulted\": [\n     {\"src\": \"POK\", \"where\": \"Pokorny p.910 (POK_03.txt leaf 147)\", \"stance\": \"supports\",\n      \"note\": \"'ai. sará- „flüssig“, gr. ὀρός, lat. serum „der wässerige Teil der geronnenen Milch, Molke“'.\"},\n     {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. serum (KLN_1966.txt line 34728)\", \"stance\": \"supports\",\n      \"note\": \"'serum, n. — L., \\\"watery fluid; whey\\\", cogn. with Gk. ὀρός (for *sorós), \\\"whey\\\", OI. saraḥ, \\\"flowing\\\", sarit, \\\"brook, river\\\" … fr. I.-E. base *ser-, *sor-, \\\"to run, flow\\\".'\"},\n     {\"src\": \"IEC\", \"where\": \"Mann, IEC.txt line 15242\", \"stance\": \"partial\",\n      \"note\": \"'seros, om (?) \\\"fluid\\\" … (for Lat. serum, n. \\\"whey\\\", see also ksero-)' — Mann keeps open a rival *kser- source for the Latin word.\"}\n   ]\n  },\n  {\n   \"id\": 4, \"lang\": \"French\", \"words\": \"\", \"verdict\": \"confirmed\",\n   \"derivation\": \"An empty pass-through box standing for French sérum, a learned (not inherited) borrowing of Latin serum taken straight into medical French; had it been inherited through Vulgar Latin the outcome would have been something like *sier. It is this French medical word — not Latin directly — that the Persian medical term of the next box was taken from, which is why Nourai inserts the box; Moʿin's own tag on سرم is [فر.] 'French'.\",\n   \"derivation_fa\": \"جعبه‌ای خالی و واسطه است که نمایندهٔ sérum فرانسوی است؛ وام‌واژه‌ای ادبی (نه موروثی) از serum لاتین که یکسره وارد زبان پزشکی فرانسه شد — اگر موروثی می‌بود صورتی چون *sier می‌داد. همین واژهٔ پزشکیِ فرانسوی — و نه مستقیماً لاتین — خاستگاه اصطلاح فارسیِ جعبهٔ بعدی است و نورایی به همین سبب این جعبه را افزوده است؛ خودِ معین نیز بر «سرم» نشانِ [فر.] گذاشته است. ادعای نورایی درست است.\",\n   \"sources\": [\"https://abadis.ir/fatofa/%D8%B3%D8%B1%D9%85/\"],\n   \"ref_check\": [\n     {\"ref\": \"(none cited)\", \"status\": \"not_checked\",\n      \"note\": \"Empty box with no refs= in the book; checked against the Moʿin tag quoted in the next node and against Etymonline's Latin>modern-medical account.\"}\n   ],\n   \"consulted\": [\n     {\"src\": \"MON\", \"where\": \"Moʿin, Farhang-e Farsi s.v. سرم, via abadis.ir (archived)\", \"stance\": \"supports\",\n      \"note\": \"«(س رُ) [ فر. ] (اِ.) ۱ - خون آبکی. ۲ - دارویی مایع حاوی مواد قندی یا ویتامین‌ها …» — the bracketed [فر.] is Moʿin's tag for a French loan, i.e. the French intermediary the empty box stands for.\"},\n     {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. serum\", \"stance\": \"silent\",\n      \"note\": \"Klein takes English serum straight from Latin and says nothing about the French medical term.\"}\n   ]\n  },\n  {\n   \"id\": 5, \"lang\": \"Persian\", \"words\": \"serom «سیروم»\", \"verdict\": \"transcription_suspect\",\n   \"error_in\": \"extraction\",\n   \"book_prints\": \"سِرُم\",\n   \"correct_form\": \"سرم\",\n   \"derivation\": \"The etymology is right but the Persian script in the JSON is not what the book prints. Page 414 of the printed book shows «سِرُم» — sīn with kasra, rāʾ with ḍamma, mīm — i.e. سرم, read serom, matching the Latin-script 'serom' in the same box. The extraction has turned the two vowel marks into full letters, producing the non-existent «سیروم». This is an extraction error, not the author's; the printed page is correct and the owner should fix the data. On the substance: Persian سرم serom 'serum, blood plasma; an intravenous drip' is a twentieth-century medical loan from French sérum (Moʿin tags it [فر.]), itself from Latin serum; Dehkhoda's older entries under سرم are unrelated homographs (سَرم 'a thistle-like edible plant', Arabic سُرْم 'rectum', Turkish سِرَم 'scraped leather').\",\n   \"derivation_fa\": \"ریشه‌شناسی درست است، ولی صورت فارسیِ ثبت‌شده در داده‌ها با آنچه کتاب چاپ کرده نمی‌خواند. صفحهٔ ۴۱۴ چاپی «سِرُم» دارد — سینِ مکسور، رای مضموم، میم — یعنی «سرم» که همان serom لاتین‌نگاشتِ همان جعبه است. در استخراج، دو علامتِ کسره و ضمه به حرف بدل شده و صورت ناموجودِ «سیروم» پدید آمده است. این خطای خوانش اسکن است نه خطای کتاب، و مالک داده‌ها باید آن را اصلاح کند. اما دربارهٔ خودِ واژه: «سرم» در فارسی وام‌واژه‌ای پزشکی از sérum فرانسوی در سدهٔ بیستم است (معین آن را [فر.] نشان زده) و آن نیز از serum لاتین؛ مدخل‌های کهن‌تر دهخدا ذیل «سرم» واژه‌های هم‌نگارهٔ بی‌ربط‌اند («سَرم» کنگر، «سُرْم» عربی به معنی مقعد، و «سِرَم» ترکی به معنی دوالِ خراشیده).\",\n   \"sources\": [\"https://abadis.ir/fatofa/%D8%B3%D8%B1%D9%85/\"],\n   \"ref_check\": [\n     {\"ref\": \"MON\", \"status\": \"supports\",\n      \"note\": \"Moʿin, Farhang-e Farsi s.v. سرم (quoted at abadis.ir/fatofa/سرم/, archived): «(س رُ) [ فر. ] (اِ.) ۱ - خون آبکی. ۲ - دارویی مایع حاوی مواد قندی یا ویتامین‌ها یا سایر داروهای حیاتی که … از طریق سرخ‌رگ به بدن بیمار تزریق [می‌کنند]». The [فر.] tag is precisely Nourai's French→Persian arrow, and the headword is سرم.\"}\n   ],\n   \"consulted\": [\n     {\"src\": \"BQT\", \"where\": \"Dehkhoda's سرم entries quoted alongside Moʿin at abadis.ir (which cite برهان and آنندراج)\", \"stance\": \"partial\",\n      \"note\": \"«سرم. [س َ] (اِ) کنگر و آن رستنیی بود که برگش خاردار است … (برهان) (از آنندراج)» — Borhan-e Qateʿ knows only the plant name سَرم; the medical serom is post-classical and therefore absent from it, as expected for a modern European loan.\"},\n     {\"src\": \"ARY\", \"where\": \"Aryanpur, Persian index (searched for سرم)\", \"stance\": \"silent\",\n      \"note\": \"Aryanpur's dictionary of Indo-European roots of Persian does not treat this modern French loan.\"}\n   ]\n  },\n  {\n   \"id\": 6, \"lang\": \"English\", \"words\": \"serum\", \"verdict\": \"confirmed\",\n   \"derivation\": \"English serum was taken directly from Latin in the 1670s in the sense 'watery animal fluid', especially the clear pale-yellow liquid that separates when blood clots; the further sense 'blood serum used in medical treatment (antitoxin)' dates from 1893, after Behring's work on diphtheria antiserum. It is a learned borrowing with no intermediate vernacular stage, so the chart's Latin→English arrow is exactly right; Watkins lists SERUM (with SERAC) as the English derivative of *ser-o-.\",\n   \"derivation_fa\": \"واژهٔ انگلیسی serum در دههٔ ۱۶۷۰ م. مستقیماً از لاتین گرفته شده، به معنای «مایع آبکیِ جانوری»، به‌ویژه مایع زلالِ زردرنگی که هنگام لخته‌شدن خون جدا می‌شود؛ معنای «سرمِ درمانی/پادزهر» از ۱۸۹۳ م. و پس از کار برینگ بر پادسرم دیفتری رواج یافته است. این واژه وام‌واژه‌ای ادبی است و هیچ مرحلهٔ میانیِ عامیانه ندارد، پس پیکان لاتین ← انگلیسیِ نمودار درست است؛ واتکینز نیز SERUM (در کنار SERAC) را بازماندهٔ انگلیسیِ *ser-o- می‌شمارد. ادعای نورایی درست است.\",\n   \"sources\": [\"https://www.etymonline.com/word/serum\"],\n   \"ref_check\": [\n     {\"ref\": \"AHD\", \"status\": \"supports\",\n      \"note\": \"Watkins 1985 s.v. ser-2: '1. Suffixed form *ser-o- in Latin serum, whey: SERAC, SERUM.'\"}\n   ],\n   \"consulted\": [\n     {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. serum (KLN_1966.txt line 34728)\", \"stance\": \"supports\",\n      \"note\": \"'serum, n. — L., \\\"watery fluid; whey\\\" … fr. I.-E. base *ser-, *sor-, \\\"to run, flow\\\". Cp. hormone, orrho-, serac and the second element in Apsaras, samsara.'\"},\n     {\"src\": \"WEB\", \"where\": \"Etymonline s.v. serum (archived; Webster's grep gave no clean entry)\", \"stance\": \"supports\",\n      \"note\": \"'1670s, \\\"watery animal fluid,\\\" especially the clear pale-yellow liquid which separates in coagulation of blood … The word was applied by 1893 to blood serum used in medical treatments.'\"}\n   ]\n  }\n ]\n}\n\nout = {\n \"pdf_page\": 444,\n \"book_page\": 414,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-13\",\n \"entries\": [e0, e3, e4]\n}\np = \"/home/sfmqrb/git/rishe/data/verification/page-444.json\"\njson.dump(out, open(p, \"w\", encoding=\"utf-8\"), ensure_ascii=False, indent=1)\nprint(\"wrote\", p)\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-444.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-444.json > /dev/null && echo JSON_OK && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 444",
 "description": "Write and validate page-444.json"
}
```


### [2026-09-14T02:11:57.018Z] TOOL RESULT

```
wrote /home/sfmqrb/git/rishe/data/verification/page-444.json
JSON_OK
nodes verified: 16/16
node verdicts: {'confirmed': 9, 'disputed': 1, 'plausible': 4, 'transcription_suspect': 2}
root verdicts: {'confirmed': 3}
ref checks: {'supports': 11, 'partial': 3, 'not_checked': 4}
books consulted: {'supports': 23, 'silent': 7, 'contradicts': 5, 'partial': 9} | by book: {'KLN': 9, 'AHD': 6, 'BRT': 4, 'WLD': 4, 'POK': 4, 'LAT': 2, 'KNT': 2, 'IEC': 2, 'ARY': 2, 'MON': 2, 'SKT': 1, 'PHD': 1, 'NYB': 1, 'HRN': 1, 'HUB': 1, 'BQT': 1, 'WEB': 1}
```


## [2026-09-14T02:12:07.582Z] TOOL CALL #57: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport json,io\np='data/verification/page-444.json'\nd=json.load(open(p,encoding='utf-8'))\ns=json.dumps(d,ensure_ascii=False,indent=1)\ns=s.replace(\"Klein 1966 s.v. sunder (KLN_1966.txt, leaf 771 area)\",\"Klein 1966 s.v. sunder (KLN_1966.txt line 37463)\")\ns=s.replace(\"Horn, Grundriss nos. 1098 and 1100 (HRN.txt lines 9496, 9509)\",\"Horn, Grundriss nos. 1098 and 1100 (HRN.txt lines 9496 and 9508-9510)\")\ns=s.replace(\"Klein 1966 s.vv. sine, prep. (p.1447/1448) and sunder\",\"Klein 1966 s.vv. sine, prep. (p.1447/1448, leaf 768) and sunder (line 37463)\")\nopen(p,'w',encoding='utf-8').write(s)\nEOF\npython3 -m json.tool data/verification/page-444.json >/dev/null && python3 tools/verify_check.py 444",
 "description": "Fix citation locators and re-check"
}
```


### [2026-09-14T02:12:08.931Z] TOOL RESULT

```
nodes verified: 16/16
node verdicts: {'confirmed': 9, 'disputed': 1, 'plausible': 4, 'transcription_suspect': 2}
root verdicts: {'confirmed': 3}
ref checks: {'supports': 11, 'partial': 3, 'not_checked': 4}
books consulted: {'supports': 23, 'silent': 7, 'contradicts': 5, 'partial': 9} | by book: {'KLN': 9, 'AHD': 6, 'BRT': 4, 'WLD': 4, 'POK': 4, 'LAT': 2, 'KNT': 2, 'IEC': 2, 'ARY': 2, 'MON': 2, 'SKT': 1, 'PHD': 1, 'NYB': 1, 'HRN': 1, 'HUB': 1, 'BQT': 1, 'WEB': 1}
```


## [2026-09-14T02:12:25.736Z] AGENT

Page 444 (book p.414) verified — `data/verification/page-444.json`, `verify_check.py 444` shows 0 PROBLEM lines.

**Counts** — roots: 3 confirmed. Nodes 16/16: 9 confirmed, 4 plausible, 1 disputed, 2 transcription_suspect. Ref checks: 11 supports, 3 partial, 4 not_checked (nodes with no refs in the book). 17 books consulted.

**Disputed**
- **Sen 2 / Latin `sincěrus`** — Klein (KLN:1447, the cited page) only guesses "possibly *sine cera*"; Ernout-Meillet call that a folk etymology ("la forme attendue serait *sēcērus … le sin- est le même premier élément que dans sim-plex"), Watkins files SINCERE under `sem-1` (*sm̥-kéro- "of one growing"), de Vaan/Wiktionary reconstruct PItal. *senkairos < *sem- + *ḱer-. `sine` itself is solidly confirmed; the node takes the worse verdict.

**transcription_suspect**
- **Septm / Germanic `sibum`** — `error_in: book`. The printed page really shows "sibum"; no such Germanic form exists (PGmc *sebun; Goth./OHG sibun, OE seofon). AHD, Nourai's source, prints *sebun. Extraction is faithful.
- **Ser 1 / Persian `serom «سیروم»`** — `error_in: extraction`. **Owner must fix the data**: page 414 prints «سِرُم» (= سرم, kasra + damma), and the extractor turned the two vowel marks into the letters ی and و, yielding the non-existent «سیروم». Etymology itself is fine (Mo'in tags سرم as [فر.] < French *sérum*).

**Plausible (notable nuances)**
- Septm node 1: the Av./OP triple (hapta, hapta-dasa, haptāiti) is lifted verbatim from Platts GPL p.41, whose "O.P." labels really mean Old Iranian/Avestan — none of the three is attested in Old Persian; Bartholomae glosses haptadasa- as the *ordinal* "seventeenth".
- Ser 1 nodes 1–2: OP Haraiva- names the *land* Aria (Kent, Bartholomae), not a river; and NP هرات came back via Arabic هَرَاة, the -t being the tāʾ marbūṭa (MP Harēw, Pokorny's "np. Harē").
- Sen 2 node 4: English *sans* reached English through Old French, and AHD puts SINCERE elsewhere.

Page image archived at `data/verification/sources/refs/ocr/BOOK/444.png`; 12 web pages archived via `fetch_source.py`.
