# Verification process log — verify-page-476


## [2026-09-14T02:28:15.380Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 476 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-476.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-476.json. Write /home/sfmqrb/git/rishe/data/verification/page-476.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 476` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T02:28:16.452Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T02:28:17.335Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T02:28:17.350Z] TOOL RESULT

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


## [2026-09-14T02:28:17.845Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-476.txt"
}
```


### [2026-09-14T02:28:17.859Z] TOOL RESULT

```
1	=== PDF page 476 (book page 446) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Stebh : support, stem  (refs POK:1012)
4	#1 (parent #0) [Avestan] refs=POK:1012; BQT:1098; SOD:363 | stawra : firm ; stambana : support ; stembya : hard
5	  #2 (parent #1) [Pahlavi] refs=BQT:1098; FVQ:59; MON:261,262 | stapr, stawr : strong ; hôstubâr, astô-bâr : firm ☞Bher ; astô-bân : firm ☞Pa
6	    #3 (parent #2) [Persian] refs=BQT:127, 1098; FVQ:59; MON:240 | setabr «ستبر ( استبر )» : strong, thick ; estabrak «استبرک ( استبرق )» : strong cloth ; ostovâr «استوار ( سُتوار )» : firm, an army rank ; ostovân «استوان ۲ ( سُتوان ۲ )» : firm, an army rank
7	  #4 (parent #1) [Sogdian] refs=SOD:63 | stmb : stern
8	#5 (parent #0) [Old Persian] refs=BQT:1100; KNT:210 | stambaka : strong ; stamb : stand firm, revolt
9	  #6 (parent #5) [Persian] refs=BQT; FSF:223 | setonbeh «ستنبه» : strong, violent, ugly
10	#7 (parent #0) [Sogdian] refs=SOD:66 | `st`np : strong, violent
11	#8 (parent #0) [Germanic] refs=AHD | 
12	  #9 (parent #8) [English] refs=None | stamp, stump, staple, step, staff
13	#10 (parent #0) [Greek] refs=None | 
14	  #11 (parent #10) [English] refs=AHD | Steven , Stephen
15	
```


## [2026-09-14T02:28:20.787Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-476.json",
 "description": "Read source JSON for page 476"
}
```


### [2026-09-14T02:28:20.954Z] TOOL RESULT

```
{
  "pdf_page": 476,
  "book_page": 446,
  "entries": [
    {
      "root": {
        "name": "Stebh",
        "lang": "Indo-European",
        "refs": "POK:1012",
        "gloss": "support, stem"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:1012; BQT:1098; SOD:363",
          "words": [
            {"translit": "stawra", "gloss": "firm", "script": null},
            {"translit": "stambana", "gloss": "support", "script": null},
            {"translit": "stembya", "gloss": "hard", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "BQT:1098; FVQ:59; MON:261,262",
          "words": [
            {"translit": "stapr, stawr", "gloss": "strong", "script": null},
            {"translit": "hôstubâr, astô-bâr", "gloss": "firm", "script": null, "see": ["Bher"]},
            {"translit": "astô-bân", "gloss": "firm", "script": null, "see": ["Pa"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "BQT:127, 1098; FVQ:59; MON:240",
          "words": [
            {"translit": "setabr", "gloss": "strong, thick", "script": "ستبر ( استبر )"},
            {"translit": "estabrak", "gloss": "strong cloth", "script": "استبرک ( استبرق )"},
            {"translit": "ostovâr", "gloss": "firm, an army rank", "script": "استوار ( سُتوار )"},
            {"translit": "ostovân", "gloss": "firm, an army rank", "script": "استوان ۲ ( سُتوان ۲ )"}
          ],
          "note": null,
          "quote": {
            "text": "چو چندی برآمد بر این سالیان - مران سرو استبر گشتش میان",
            "poet": "Ferdowsî"
          }
        },
        {
          "id": 4,
          "parent": 1,
          "lang": "Sogdian",
          "refs": "SOD:63",
          "words": [
            {"translit": "stmb", "gloss": "stern", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Old Persian",
          "refs": "BQT:1100; KNT:210",
          "words": [
            {"translit": "stambaka", "gloss": "strong", "script": null},
            {"translit": "stamb", "gloss": "stand firm, revolt", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Persian",
          "refs": "BQT; FSF:223",
          "words": [
            {"translit": "setonbeh", "gloss": "strong, violent, ugly", "script": "ستنبه"}
          ],
          "note": null,
          "quote": {
            "text": "گرفتش دایه و گفتش چه بودت ؟ - ستنبه دیو بدخو چه نمودت ؟",
            "poet": "Vîs-o-Râmîn"
          }
        },
        {
          "id": 7,
          "parent": 0,
          "lang": "Sogdian",
          "refs": "SOD:66",
          "words": [
            {"translit": "`st`np", "gloss": "strong, violent", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "stamp, stump, staple, step, staff", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 0,
          "lang": "Greek",
          "refs": null,
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 10,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "Steven , Stephen", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
```


## [2026-09-14T02:28:21.585Z] TOOL CALL #4: Bash

```json
{
 "command": "sed -n 1,200p data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-14T02:28:21.702Z] TOOL RESULT

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
```


## [2026-09-14T02:28:25.539Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"stebh\" POK_full.txt | head -40; echo \"=== POK page area\"; grep -n \"stē̆bh\\|steb-\" POK_full.txt | head -30",
 "description": "Grep Pokorny for stebh"
}
```


### [2026-09-14T02:28:25.616Z] TOOL RESULT

```
=== POK page area
74966:*stent)^- (see steb-' jamb, upright section of a doorframe or window frame; stanchion, 
81265:stabna-, s. *steb- " jamb '); Tocharian A stam, B stam "tree'; but Old High German
```


## [2026-09-14T02:28:26.560Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"stebh\\|stembh\\|stabh\" AHD_watkins1985.txt | head -40",
 "description": "Grep AHD Watkins"
}
```


### [2026-09-14T02:28:26.635Z] TOOL RESULT

```
250:stebh-. 2. Germanic nasalized form *stamp- in: a. Middle English stampen, to pound, stamp: STAMP...
1002:[stam-. To push, stutter, stammer. Germanic root. 1. Old English stamerian, to stammer:. STAMMER. 2. Middle Dutch stom, mute: stum. 3. Old Norse stemma, to stop: STEM?, 4, Old Norse *stumla, stumra, to stumble, akin to the probable Scandinavian source of Middle English stumblen, to stumble: sTUMBLE. [In Pok. stem- 1021.]] [staup-. (Cooking) vessel. Germanic root. 1. Old Norse staup, vessel: stouP. 2. Middle Low German stove, heated chamber: sTOVE!. [In Pok. 1. stew- 1032.]] stebh-. Post, stem; to support, place firmly on, fasten. I. Basic form *stebh-. 1. Germanic *stab- in Old English
1005:stef, stick, rod: STAFF!. 2. Greek stephein, to tie around, encircle, crown, wreathe: STEMMA, STEPHANOTIS. II. Un- aspirated form *steb-. 1. Germanic *stap- in: a. Old English stapol, post, pillar: sSTAPLE?; b. Old English stzpe, step (< “a treading firmly on, foothold”): sTEP; c. Middle Dutch stapel, pillar, foundation: STAPLE}; d. Middle Dutch stoep, stoop: stoor?; e. Low German stope, a step: STOPE. 2. Germanic nasalized form *stamp- in: a. Middle English stampen, to pound, stamp: STAMP; b. Middle Low German stump, stump: sTuMP; c. Old High German stam, base, stem, in German Stammlager, base camp: STALAG; d. Provencal estampier, to stamp: STAMPEDE. III. Variant *stabh- in Greek staphulé, grape- vine, bunch of grapes: STAPHYLO-. [Pok. steb(h) 1011.]
2281:SPRINGE spergh- SPRINKLE (8)preg- SPRIT sper-4 SPROUT sper-4 SPRY (s)preg- SPUME (S)poi-mo- SPUR spere- SPURGE peue- SPURN spere- SPURRY (s)preg- SPURT sper-4 SPUTNIK ksun, pent- SPUTTER spyeu- SPUTUM spyeu- SPY spek- SQUAD kWetwer- SQUALENE (8)kWal-o- SQUARE kWetwer- SQUASH2 kwét- SQUAT ag- SQUIRE skei- SQUIRREL ors-, skeoi- STABLE! sta- STABLE? sta- STACK steg- STACTE stag- STADDLE sta- STADHOLDER sta- STAFF! stebh- STAG stegh- STAGE sta- STAGGER steg- STAGNANT stag- STAIN teng-
2283:STAIR steigh- STAKE! steg- STALAG legh-, stebh- STALK! | stel- STALK?  ster-4 STALL  stel- STALLION stel- STALWART wer-3 STAMEN sta- STAMMEL sta- STAMMER stam- STAMP stebh- STAMPEDE stebh- STANCE sta- STANCH sta- STANCHION sta- STAND sta- STANDARD kar-1, sta- STANZA sta- STAPHYLO- stebh- STAPHYLORRHAPHY wer-3 STAPLE! stebh- STAPLE? stebh- STAR ster-3 STARBOARD bherdh-, sta- STARCH  ster-1 STARE ster-1 STARETS sta- STARK ster-1 STARLING!  storo- STARLING? sta- START sster-1 STARTLE  ster-1 STARVE ster-1 STASIS sta-
2293:STEM? stam- STEMMA stebh- STENCIL skeei- STENO- sten- STENOSIS sten- STEP stebh-
2294:STEP- (s)teu- STEPHANOTIS stebh- STERCORACEOUS  sker-4 STERE ster-1 STEREO- ster-1 STEREOBATE gWa- STERIGMA ster-! STERILE ster-5 STERN! | ster-1 STERN? sta- STERNOCOSTAL kost- STERNUM Ster-2 STERNUTATION _pster- STEROPE ster-3 STERTOR pster- STET sta- STEVEDORE steip- STEWARD wer-4 STICH steigh- STICHOMETRY steigh- STICHOMYTHIA  steigh-
2311:STOOP! (s)teu- STOOP? stebh-
2313:STOPE stebh-
2323:sTuD2 sta- STUDENT (s)teu- sTUDY (s)teu- STULTIFY _ stel- sTUM stam- STUMBLE stam- STUMP stebh- STUN (s)tena- STUPA steu(@)- STUPE steu(9)- STUPEFY (s)teu- STUPENDOUS (s)teu- STUPID (s)teu- STURDY trozdo- STUTTER (s)teu- stTy2  steigh- STYLITE sta- STYLOBATE gWa-, sta- STYPTIC steu(@)- Styx (s)teu- SUASION swad- SUAVE swad- SUB- upo SUBALTERN al-1 SUBAUDITION au-5 SUBDUCTION deuk- SUBDUE deuk- SUBITO ei-! SUBJACENT yé- SUBJECT yé- SUBJOIN yeug- SUBJUGATE yeug- SUBLUNARY leuk- SUBMERGE mezg-! SUBMIT (s)meit(9)- SUBORDINATE ar- SUBORN ar- SUBPOENA kwei-1 SUBREPTION rép-1 SUBROGATE reg-1 SUBSCRIBE skribh- SUBSEQUENT sekw-1 SUBSIDE sed-1 SUBSIDY sed-1 sUBSIST sta- SUBSTANCE sta- SUBSTITUTE sta- SUBSTRATUM ster-2 SUBSTRUCTION | ster-2 SUBSUME em- SUBTEND ten- SUBTERFUGE bheug-', upo SUBTERRANEAN ters- SUBTLE teks- SUBTRACT tragh- SUBULATE syU- SUBVENTION gWa- SUBVERT wer-3 SUCCEED ked- succincT kenk-1 succor kers-2 succuBUS keu-2 SUCCULENT seud-2 SUCCUMB keu-2 SUCCUSSION kwét- SUCH swo-
```


## [2026-09-14T02:28:33.844Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"steb(h)\\|stē̆b\\|stebh-\\|steb-\" POK_full.txt POK_01.txt POK_02.txt POK_03.txt 2>/dev/null | head -30; echo \"---- search stambana\"; grep -rn \"stambana\\|stamba\\|stembya\\|stawra\" POK_full.txt BRT.txt | head -30",
 "description": "Search Pokorny/Bartholomae"
}
```


### [2026-09-14T02:28:34.007Z] TOOL RESULT

```
POK_03.txt:3388:gv.  atdfxvog  ,KrugS  ara^tv-eg  PI.  , Ständer,  Seitenbalken';  cymr.  cy^  ^ ,erster'  {*kentu-stamino-)',  mir.  samaigim  ,stelle',  cymr.  sefyll^  corn.  %t^ ^stehen',  bret.  sevell  (*stamilio-)  ,errichten,  bauen'  (daneben  mit  kelt.  |  f^ tamun  »Baumstamm*;  ahd.  stam,  Stammes  ,Stamm''  usw.  scheint  Verqn|^ kung  eines  verwandten  *stamna-  mit  einem  staina-,  s.  *steb-  ,Pfo8teii')j toch.  A  stäm,  B  stäm  ,Baum*;  aber  ahd.  ungistuomi  ,ungestüm'  zu  «i^^ , hemmen',  s.  dort.  ,^,^,
POK_full.txt:74966:*stent)^- (see steb-' jamb, upright section of a doorframe or window frame; stanchion, 
POK_full.txt:81265:stabna-, s. *steb- " jamb '); Tocharian A stam, B stam "tree'; but Old High German 
POK_full.txt:81374:Root / lemma: steb(hj- and steb(h)-. stdo"^-, nasalized stemb(h)-, step- {a\so step-?), 
---- search stambana
POK_full.txt:20451:norw Dialectal stamma, stamba'sWv\\C Indo Germanic have been newly created or only 
POK_full.txt:56449:), Modern High German Scfilamm {*stamba-). Late Middle High German stemmen least, 
POK_full.txt:81380:Old Indie stabaka-m. n. " tussock ', stamba-m. "bush, tussock ' (= Lithuanian stambas 
POK_full.txt:81422:"pad', Avestan stawra- "tight, firm', np. sitabr, /stabr^ strong, vast, grand'; ved. stabhuyan, 
BRT.txt:7815:•  }.  a^iSyä-  f.  'Pfosten':  mi^nm  .  .  yj .  . stawra  yä  kirtnaotti  Yt. /O.  a8.
BRT.txt:26553:•  j.  stawra-  Adj.  (fem.  -ra-)  'stark,  fest": mihrvin  .  .  yS  .  .  'ri  aikya  k?rmaoiti Yt.  10.  28.
```


## [2026-09-14T02:28:37.218Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '81370,81480p' POK_full.txt",
 "description": "Print Pokorny steb(h)- entry"
}
```


### [2026-09-14T02:28:37.563Z] TOOL RESULT

```
Page(s): 1004-1010 



Root / lemma: steb(hj- and steb(h)-. stdo"^-, nasalized stemb(h)-, step- {a\so step-?), 
nasalized stemp-, nominal stdo'^o-s, stemb(h)ro-s, stomb(h)o-s 
Meaning: post, pillar, stump; to support, etc.. 
Note: relationship to *5/^- "stand' is possible. 
Material: root form with -b. 

Old Indie stabaka-m. n. " tussock ', stamba-m. "bush, tussock ' (= Lithuanian stambas 
"Kohlstrunk'); 

gr. OTEppu) " stamp, mishandle, abuse, revile ', OTEppa^siv Aoi5op£Tv, Hes. oio^oc, m. 
"Schelten, boastfulness ', OTOpsu), aropa^u) " abuse, revile '; 

Old Saxon preterit s/op "trat fest auf. Old English staeppan {steppan), stop'fest treten, 
march, step, stride, strut'. Old High German s/e/Ofe/7 and s/5/0/&/7"fest auftreten, fest 
auftretend schreiten', in addition Kaus. Old English s/^y05/7"einweihen'. Old High German 
(Hildebrandslied) stoptun tosamane l\essen zusammenstapfen'; Middle Low German 
stappe, Old High German stapf, stapfo {staffo) "Stapfe, footprint ' (Germanic *stapp-)\ Old 
Icelandic stgpullm. " jamb, pillar, tower'. Old Frisian s/5/0^/"Richtblock; Krone eines 
Zahnes', Old English stapolxw. "stem, jamb, column ', Middle Low Germans/S/Oe/m. " 
column, Unterlage, stacked heap, Stapelplatz' (out of it Modern High German Staper pile, 
stack '), Old High German stapfal, staffar foundation, footstep, grade'. Modern High 
German Staffer rung, horizontal step on a ladder, Treppenabsatz'; Old Saxon sfopom. " 
step, tread; kick, strike or blow delivered by the foot; footprint, track, footprint ', Old English 
stdpe/6s., Old High German stuoffa, stuofa. Modern High German grade. Middle High 
German s/^e/fe "tight, firm, strong'; Old English staepe, stepe, PI. stapas^ footstep, grade'. 
Old Frisian stepe 6s., Old Icelandic stapim. "hoher and steiler rocks'; Old Frisian stepa 
"beisteuern' (denominative from:) Old Frisian ield-stdpe^Eeisieuer, Wergeld', Old High 
German stuopfa6s. (Old Church Slavic stapiD "Steigbugel' from dem Germanic); 

nasalized Old Low German stamp. Old High German stampfxw. "tool zum Stolen', (Old 
Church Slavic s/O/Oa "mortar' from dem Germanic), therefrom Old Icelandic stappa^bwcw^, 
poke, stomp, crunch ', Old English stempan"\n mortar grind ' (engl. stamp a\so " stamp '), 
Middle High German stempfenan6 Old High German stampfon. Middle High German 
stampfen' stomp, hit, stamp ' and further Middle Low German stempel. Old High German 
5/e/77yO///"Stampfel, pestle'; Middle Low German stump m. " stump; adj. "dull, stupid'. Old 
High German stumpfm. " stub, stump '; Adj. 'stumpf mutilated, abbreviated '; 



problematisch Middle Irish sibara walking, marching' {*stebulo-). 

root form with -b'^-: 

Old Indie stabhnati, stabhnoti, stambhate, -//"prop, support, hamper', Med. " stiff 
become, solidify, congeal ', stabhita-^ qesiiJXz'C , stabdha-^ stiff, rigid; haughty', Kaus. 
stambhayati, -/e 'fastens, makes stiff, lahmt, halt an, oppressed', stambha-m. " jamb, 
column; hindrance, Lahmung; Aufgeblasenheit', (compare np. s/tamba' violent, brutal, 
streitsiJchtig'), stambhanam^ fortification, Festhalten, hindrance ' = Avestan stembana- 
"pad', Avestan stawra- "tight, firm', np. sitabr, /stabr^ strong, vast, grand'; ved. stabhuyan, 
stabhuyamana-^ sich nichtfrom the Stelle ruhrend, unbeweglich ', ap. sta^bava' resist! 
rebel!' (indoiran. *sta'^'^au-)\ 

gr. aoTEpcpnt; "unerschijtterlich' (actually 'wer nicht gepreflt become kann'), GTspicpuAa n. 
PI. 'ausgepreftte Oliven orTrauben', aracpuAri " grape, grapevine; uvula in mouth', 
GTacpuAr) "plummet'; 

Middle Irish sabt ' shaft, pillar, stick' {*st9b[h]a)\ semmor^ clover' {*stemb[h]ro-)\ 

Old Icelandic stefja {*stabjan) "hinder', stefna^ dam ' (*make stiff, stiffen, make rigid, 
halt, stop, cause to stop, block '), Old High German staben^ rigid, stiff sein'. East Frisian 
star stiff, lame'; Gothic *s/a/fe(Nom. PI. stabeis) aroixsTa "Buchstaben' (lesson through 
Runenstabchen), Old Icelandic s/5/^"staff, pad, alphabetic letter'. Old English s/^/'staff, 
alphabetic letter'. Old High German Middle High German stap{-b-) " stick, pad, rod '; 
Swedish Danish staver^ fence post ' (compare Old Church Slavic stoborb, Lithuanian 
stabaras); Old Frisian s/e/'staff; 

Maybe alb. stap^ stick, pad, rod ' a Germanic loanword. 

Old Icelandic stefu. {*stabja-), stefnai. {*stabanjdn-) " certain, feste time etc.', Old 
English stefn, sfemmm. "time, Mai, Periode'; Old Icelandic stafnn. 'Steven, Hausgiebel', 
Old Saxon stamnm. 'Steven', Old English stefn, stemnm. 'stem, root, Steven', Old High 
German sfam {-mm-) ' tree truck, Geschlechtsstamm ', Modern High German stem 
(Verquikkung eines *stad-na- \N\t\r\ a *stam-na-: Old Irish tamun ^tree truck'); 

nasalized Old High German stumba/' cut-off piece, stump ', stumb/7dn' mutilate ', Old 
Frisian stemb//nge' mutilation '. 

Lithuanian stembtr stalk ansetzen', stembras, stembrys^ stalk' (= Middle Irish 
semmor), stimbras^ tail stub, tail stump ', zem. stambris^ stalk', Lithuanian stambus 



'coarse, coarsely granulated ', 5/a/77i6'55'Kohlstrunk', Latvian stuobrs^ stem, reed'; 
Lithuanian stebulei. 'hub of a wheel', Latvian stebe^ mast ', russ. stebatb, kir. stebnuty' 
lash, flog; steppen, sew '; stabyti, stabdyti^ halt, stop, cause to stop, block ', stabas' jamb, 
Schlagfluft', Old Lithuanian sfabas' idol ' (gottlich verehrter Pflock), Latvian stabs' pillar, 
column ', Old Prussian stab/sm. ' stone ', stabn/t '( stony) oven', Lithuanian stabaras'6ry 
bough'. Old Church Slavic stoborb ' column '; with the meaning ' be amazed, marvel ': 
Lithuanian stebetis; 

root form in -/?-: 

Old Indie in Kaus. sthapayami' place, found, ground '; 

Old Church Slavic stopa' footprint ', stepent 'grade'. Old Lithuanian s/S/OyZ/s 'stand 
bleiben', Lithuanian s/epas 'Schlagfluft', stapinti' penem erig6re '; 

Old Church Slavic stgpiti, stgpat/'trea6'. 

References: WP. II 623 ff., Trautmann 280, 284, Kniper Nasalpras. 195 ff., Vasmer 3, 16, 

19,35. 

Page(s): 1011-1013 

Root / lemma: stegh-, nasal, stengh- 
Meaning: to stick; pole, stalk, etc..
```


## [2026-09-14T02:28:47.084Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '26540,26575p' BRT.txt; echo \"=== stembana\"; grep -n \"stmbana\\|stembana\\|st.mbana\" BRT.txt | head; echo \"=== stemby\"; grep -n \"stmby\\|stemby\\|st.mby\" BRT.txt | head",
 "description": "Bartholomae stawra / stembana"
}
```


### [2026-09-14T02:28:47.179Z] TOOL RESULT

```
•stay-
159»
Ytio.iig; —  myatdavä  ratui  amyasda- vamtit  ratunaim  vänmtum  (sd.)  ^rtm  fra- ptnnaoiti  h.3. 10;  —  mtjmfm  (bz.  mah»- mam,  ayrTm)  'r?m  anjd  "um  den  Preis eines  Stücks  Gross vieh  vod  geringster (mittlerer,  bester)  Qualität)"  V.7.413,  43^ •)  Im  Gegensatz  lum  Kleinvieh  {pasmi-,  anu- maya-)  auch  zum  Ziehen.  Reiten  und  Lasten- tragen  lu  verwenden.  —  ••)  Sonach  derReihen- folEe  ihres  Werts,   s.  V.  /.  4a.
KompE.  —  mp.  stSt  'Zagtier,  Ross',  op.  ju/w- 'Ross;  (überhaupl)  Tier",  OMS.  sturiä  'Vieh'; got  sHur  'Stier'.  —  Pü,:  stör,  Npü.  {m  A): gSvän  u  götpandän,  Sü.  (lu  A);  ecäuipaäam.
•  \.  staorö.paya-  Adj,  'wo  eine  Viehhut ist":  yS  älrjm  pantat  hala  'y3t  daitim gäiUm  avi  ava.baraiti  V,  8. 94 '\
*paya-  n.,  lum  V.  pä(y}:  —  PÜ.;  sler  pän.  — >)  Es  handelt  sich  also  um  ein  von  Hirten angemachtes  Feuer.
•  j.  staorö.maza-  Adj.  'durch  Verpfändung eines  Stücks  Grossvieh  (Rind)  geschlossen', von  mi^ra-  m.  'Vertrag'*':  tairyS  (nämi. mihrS)  'zS  "die  vierte  (Art  des  Vertrags wird)  durch  Verpfändung  eines  Rinds  ge- schlossen" V.  4,2;  —  allö  mtiirS  .  .  yg *zB  V.  4. 8;  —  'zS  atäj  framamaiti  -aJ «Sa^  antatf  urvaitya  (sd.)  fraddkaiti  V. 4-^;  —  yS  tnikrim  aiwi.drviaiti  yim 'ztm  V.  4.14;  —  hs  upaMtniS  {sü.)  .. hau  -zff  V.4.  48.
**)  Eig.  wobei  Verpfändung  eines  Stücks  Gcois- vieh  stattfindet.  Es  nimmt  dieser  Vertrag  unter den  6  verschiedenen  Vertragsarten  die  dritte Stelle  (von  oben)  ein,  iwiichen  dem  m&rS  fiaiu.- maiä  and  virS.mazö  stehend.    S.  noch  zu  Fn.
Fa.:  itärmaiSi.  erl,:  12  sffr'itiiöUStir' (nixal.
itt  das  Pfandobjekt  wert), p.  ttaiav^  D.  6.  6:  lies  startevJ',  t.  *tiat'
•  j.  ataxta-  Adj.  'stark,  fest* :  'tu  F.  12. Fö.:  +j/art'').  —  O  So  lese  ich  für  hds,  ddt dpt,  indem  ich  p  für  dp  selie.  Ich  ver- gleiche ooss.  Ilatod,  das  -  wenn  gleich  ai. slab-lhä-  Adj.,  PPfF.;  s.  GIrPh.  /  Anh.  30, S  33;  doch  s.  auch  34,  S  J9-  '  -  sich  lu  mp. stafi  verhält  wie  ai.  äabdhi-  lu  jAw.  dapta-,
•  j,  staxra-  Adj.  'stark,  fest',  inbes.  vom Winterfrost  'streng':  TS  mrUrS  ty&  V, 2.  22;  F.  /2;  —  zaya  ava%a  °rS  yat  .  . "der  Winter  ist  darum  (so)  streng,  weil . ," FrW. 8.t;  —  'rahe  FrW.  8.  a.
Vgl.  tthd.  siakat,  spr.  stakU  'Stahl';  litt,  in BSächsGW.  iSgy.  ao.  —  S.  auch  staxlö  und  np. ätam,  mp.  ri'arm.— PÖ.(iuF.):  sturk,  (luV.): kac  an  slaxmakih.
•  j.  stawra-  Adj.  (fem.  -ra-)  'stark,  fest": mihrvin  .  .  yS  .  .  'ri  aikya  k?rmaoiti Yt.  10.  28.
Zum  V.  slamb-.  —  np.  silabr.
•  j.  "stanvS ''  v3  puili  paihi  davaisfie  vä" V.  7.  43  PÜZ-"-
0  So  Wo.    SP,  und  die  NA  des  FahlVend.:
•  j.  staman-  m.  'Maul',  nur  von  dem des  Hunds:  'manim  .^^(näml.  des  Hunds) . .  nySzaym  (Sp.  362  o.)  V.  ij.  30;  —  yat . . alte  ganma  (sd.)  :^an%a  •maram  vü Aizvam  v3  apa.daiat  (näml.  dem  Hund)
v./i.4-
Vgl,  gr.  Q-niia;  kymr.  la/«;  gani  unsicheres bei  Hirt  PBrB.  22. 223.  —  Pü. :  asiämak  (bei jAUASPji  GI0SS.  549  'gums").
•  j.,  g.  *stay-  £,  m.'>  'Wesen';  1)  'Sein, Dasein':  ßm  (näml.  katium)  mli  data dangahyä  ^yaol. .  vairyä  stSisyS  %waAmt x/a^rSi  vnci  "ihn  soÜt  ihr  mir  gewähren, ,  .  den  Wunsch  nach  der  langen  Dauer des  köstlichen  Daseins,  von  dem  gesagt ist,  dass  es  in  deinem  Reiche  sei"  Y. 4?-  13''-  a)  von  einem  einzelnen Seienden  'Geschöpf:  ^/vzos  .  .  pdhs  . . /laihymg  (sd.)  *ä  *stisi>  yfng  *a.saän ahurs  Y.  43-3;  —  Aspla  gSuscä  *asaiiAäcä asaonasca  asävairyisiä  stsis  "er  ist  der Vater  des  Rinds  und  des  A!a  und  jedes zum  Asa  gehörigen  männlichen  und  weib- lichen Geschöpfes"  Y.  5Ä  4.  a)  mit  GS. asaonö  (Sp,  251  u.):  u^la  paoiryam  asaonS stXm  yasamaide  ".  .  das  erste  Geschöpf des  Heiligen*'  . ."  '^1.18.1;  —  kai^yä- var?S3m  (ASm.!)'J  .  .  aiäonS  stim  G. ?.  7-  3)  von  der  Gesammtbeit  der Seienden  'Schöpfung,  Welt":  zara%ustr-7m .  .  gal%yayä  stsis  ahUmca  ratumca  "den Z.  .  .,  den  A.  und  R.  der  materiellen Schöpfung"  Vr.  2.  4;  4;  —  zara%ustraAe . . ys  paoirys  stöii'  astvai^yä ..  Yt.  13.  Bg  ii ;
—  asmamm  ..  *gaä^Im  *gaH&yayä  stSis Vr.  7. 4.  a)  mit  GS.  aiaone{^^.  251  u.): yaca  upairi  (sd.)  iS  akarana  anayra  a^acnS Sil/  aSi  Yt.  Ä",  48;  —  ^antim  trvamm mainyava  stx/*asaonS data  .w(Sp.a76ni.) V.  2.  igPüZ.  et)  mit  vlspa--.  vTspqm asaenS  stim  .  .  mainynfm/ä  gaihyqmcä Y.  3S.i;Vt.  16. 1 ;-- vlspqm  asaons'stXm haitlmca  bavairUlmca  büsydntlmca  Y.  ip.g;
—  vJspayä  asaonS  stöis  haihysüa  bavqi- %yaica  büiyqikylUca   Y. 52.1,  68.22;  —
dby  Google
^^593
*siay-
stav-  mit  US
1594
frad^si  vUpayh  aiaonS  stöi!  hamisße vispayä  drvats  siBii  Y.52. 4;  4.2,  ÄS, 55.3,  70.6,  Vr.n.  I,  Yt./.2i,5.89,  //.17, V.  jo.  5,  F.  26,  b)    mit    GS.    drvati^
(Sp.  777  o.)  und  vls^a-.  ravasca  .  .  äfrX- nämi  -vlspayh  aiaenS  stSis  qsasca . .  vlsfaya drvaW  siDis'Y.  8.  8;  52.  4,  61.  5.  4)  sva. 'Besitz,  Hab  und  Gut'(?):  asavatam  mahr- ka^äi  aom  Hhr>mca  *stimca  "um  den Gläubigen  zu  verderben,  ihn  und  sein Geschlecht  und  sein  Hab  und  Gut"  Yt. ig.  la.  LS.  stsi,  Sil  als  Inf,  sbes,
KompA.,  E. ;  AbleiL  —  ai.  stäy-  m.  (?,  LUDWIG Rigvcdi  5.  220);  lat.  caele-slisli  'qui  est  ir caelo'.  —  Pü. :  gc/ai  (?,  geschr.  ddt  d),  Sü, : paiiküh,  sj-i/ih;  E.  noch  No.  2,  4  und  Komp., Ableit.  —  i)  Nur  Y.  43-  3,  G.  3-  7  und  Y, Jif.  4;  sn  der  letzten  Stelle  handelt  ce  Eicb um  den  Gegensatz  von  männlich  und  weib- lich; vgl.  ^ääman-  No.  2.  —  •)  Pü. : /3  kämak isläl,  Sfi. :  sveechayästu.  —  Sl  NA.  äsßl;  %.  aber Pt4  und  PQ.  —  4)  PüErl.:  gaySmart,  — S>  Anders  KZ.  3g.  370,  XF.  13.  185.
•  j.  'stay-  f.  'Stehen,  Treten  (usw.)'.
KompE.  —  Zum  V.  sli:  —  ai.  'slhay-  f.  — Aus  «r.  *'slAai-,  der  KompForm  zu  'slhilal- (ai.  slhilay-);  IF.  ;-.  70.  —  Vgl.  'j/o-,
•  j-,  g,  Stav-  V.  'preisen'.  Praes.  i  slav-i stv-'K  —  PPfP.  'siSfa-;  PFP.  'staota-,  Inf. staomaine.
1)  'preisen,  loben,  besingen':  staomi maly^mca  värinüa  .  .  slaemi  garayS  .  . staomi  zqm  .  .  slaomi  z)mS  .  .  laramm Y.  10. 3  £  a)  bes.  Gottheiten:   haoms
uxsyeiti  stavanS'^  a%a  (sd.)'  nS  yS  dim staoiti  .  .  Y.  /o.  6 ;  —  yäha  mä  (näml. haotmni)  aparaät  saofyantB  slavqn^'*  Y, g.2;  —  fravasayö  ..  avat  avS  zixSnS- nhimna  (sd.)  ks  «J  stavSp''  kü  yasäite  ks ufyät  Yt. /j.49f.;5.  8;  —  asäunqm  ..fra- vasayS  staomi  sbayemi  ufyemi  Y.  77. 18; —  yS  ahm  staoiti  (s.  i.)  hS  mqm  staoiti yim  akurtm  H. /.  3;  3*;  —  *yavatä  %wa tnazdä  *slaoml*^  u/ya(sd.)cä  'V.43-8;  — at  fravaxsyS  vjspanam  mazishm  (sd.) s'tavas  aiä  yS  kudä  (sd.)ysi  &'«/r(NSni.)5> Y.45.6;  —  aj  vi  yazäi  slavas^  mazäa akuri  hadä  (sd.)  a/ä  Y,  jo.  4;  —  täis  va yasnäis  paitl  stavas^''  ayeni  mazda  asä "mit  diesen  Gebeten  euch  preisend  will ich  wieder  vor  euch  treten,  o  M.  und Äsa"  Y.jo.  9;  —  ycCkä  vi  yaz^mnas/a urväidyä  (sd.)  stavas^''  ayenX  paitl  Y. 34.6.  2)  Tenn.  techn.  fdr  das  Beten des  Asageht\s'''>:  yö  ahm  staoiti  hS..  "wer
=== stembana
=== stemby
```


## [2026-09-14T02:28:48.657Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"WP. II 623\\|623 ff\" WLD_band3.txt | head; ls /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/",
 "description": "Check WLD files"
}
```


### [2026-09-14T02:28:48.730Z] TOOL RESULT

```
WLD_Bd1_1930_dli_70244_djvu.txt
WLD_Bd1_1930_dli_70244_text.pdf
WLD_Bd1_pages.txt
WLD_Bd2_1927_dli_106624_djvu.txt
WLD_Bd2_1927_dli_106624_text.pdf
WLD_Bd2_pages.txt
```


## [2026-09-14T02:28:56.935Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"stamb-\\|stambana\\|stmbana\\|st?mbana\" BRT.txt | head -20; echo \"=== V. stamb\"; grep -n \"V\\.  stamb\\|V\\. stamb\" BRT.txt | head",
 "description": "Grep BRT for stamb verb"
}
```


### [2026-09-14T02:28:57.001Z] TOOL RESULT

```
=== V. stamb
```


## [2026-09-14T02:28:59.570Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"slamb\\|stamb\\|slembana\\|stembana\\|Pfosten'\\:\" BRT.txt | head -30",
 "description": "Grep BRT stamb variants"
}
```


### [2026-09-14T02:28:59.649Z] TOOL RESULT

```
7815:•  }.  a^iSyä-  f.  'Pfosten':  mi^nm  .  .  yj .  . stawra  yä  kirtnaotti  Yt. /O.  a8.
19305:j.  Hmöi  N.  8-,  lid  nmänäl •  j,nrnäna-,g.,j.''dflniana-'',j.'V;'«ff»a- n.  'Behausung,  Haus',  von  jedem  zum Aufenthalt  für  Menschen  (Götter)  und Haustiere  dienenden  Bauwerk,  sowie  auch von  dem  zu  einem  Anwesen  gehörigen Gebäudekomplex;  I)  von  Wohnungen  fUr Menschen  (und  Götter):  yanyS buyä  'nshu ma^yäkanqm  Y.  6i.\;  —  ahmi  *ne  ya^ m!^ayasnBi^{Stve.Tz.)  V.5.45;  —  vasö.. mazdayasna  ahe  'nahe  myasd>m  äaihyäril V,  &22J  —  ätacäni  sünm  'mm  drvatS Yt-5'  3S;  —  <Mi  'tarn  yim  ^alpaihjm Yt5.63;  62;  —  ha%ra  'ni  avastaya  ka~ t>mca  /raslamb>m{s,ü.)Si  ..  V.  2. 26;  — yat  bä  paiti  nä  a/ava  'mm  uedasta  ä%ra- vai  gaomavat  nsirivat  ..  V.J.  2;  15.  ai; —  mürnm  . .  ylF  stunä  v^ärayeiti  iirtsi- mitahe  'nahe  Yt /O.  28;  30;  —  tBm..°na inasilä  ..  dahähi  YtJO.30; —  sraohm .. yS  driyaolca  . .  amava£  'mm  hüm.täsH  Y. $'j.  10;  —  as>m  yS  ahurB  masda  . .  yas> tat  'npm  ahnmm  srirtm  raoximm  frs- d^rirsrym  V.  22.1^;  \.Sy.2i;  —  iaiiihe ka^he  apayisire  'mm  htitaite  hi^ättm  Yt. 5.  loi;  —  aliqm  "nä  hvihätä  .  .  hUhfUe Vti7.  8;  V./j.  4g;  —  hubaotUl  ba^aite °mm  yeAhe  'ne  asis  varmhi  . .  psta  mda- ^aite  Yt.ij.6;  ij.107;  —  iha  ml  tum (nämL./4/fl)  hamJaranuha  *antary.ar^?m •nahe  srJrahe  Ytzj.öo;  jj.  147, 156';  — alU  . .  ramyai  i%a  upa  tmai  °mm  yat ahüiri  Y./O.i;  6'o.2,  Yt  14.41; — vainti ahmi  'ne  sraesS  Y.  tfo.  5;  Yt7j.  52,  FrD. /3;  —  vUfa  'na  sraoiö.psta  yazamaide  Y. 57-34)  —  damt  ha^a  ahmüt 'nät  ..rhyeja ■  •  ^'yeyenti  yejihe  *'?ya*'  sraoh  . .  astf paiti^ants  Y.57. 14;  /o.  7;  —  mä  yave imat  'mm  i^'annS  frazakXi  Y.60.  7;  Vyt 5;  —  xihsii  äfrlnstttu  {jis-viA.  fravas<rfS) ahmya  'ne  vattuhim  asim  . .  xsnüiä  para- yantu  haca  ahmst  'nät . .  msüm  gtnzänä pärayantu  haca  ahmst  'nät  ahmSkfm^a mazdayasnanqm  Yt  13. 157;  Y.  2j.  3;  — aai  ahmSi  'näi  dähäiti  gluica  vqhwa  vlra- nqm/a  Yt.!0.  a8;  —  äat  ..  ahe  'nahe/ra- pi^iws  gäu^  .  -  Y.  j.  3 ;  —  t^it  ahmi  'ne *sänaite  ä^rava . .  äat  ahmi  'ne  Sayhnte  da- hahaca..Y.ii,6;  — /raddhsi  ahe'naheY. 52.4;  4.5,  Vr./J.  13*;  —  'n?m  hS  manyaita paraJa%B  V.  ;*.  28;  ■ —  (8«  miknäi  daiva *aipi.jaiti  'ne  aiAhai  gundayai  (sd.)  V,  3.
26554:Zum  V.  slamb-.  —  np.  silabr.
```


## [2026-09-14T02:29:09.137Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"mbana\\|mbya\" BRT.txt | head -20",
 "description": "Grep BRT for mbana/mbya"
}
```


### [2026-09-14T02:29:09.192Z] TOOL RESULT

```
4713:•  j.  anvarJitavas't?ma-<>  Adj.  (fem,  °m3-) etwa  'der  am  will  fahrigsten,  geeignetsten wirkt*:  fravasayö  'tfmä  frascimbananqm ". .  die  geeignetsten  unter  den  StÜUbalken" yt.y.26.
10561:xumbya-
10564:•  j.  xumbya-'*  m.  ER  eines  Gläubigen: fra'jaxSt:is  "ythe  asaonS  Yt./J.i38.
11733:manS,  vehu  manS  taj  vanaiti  Yt. /p.  96;  jA'w.;  hazannm  azinqm  .  .  ava.janyät .  . —  parä  .  .  *daiahSui  anhat  b?r3t5  (sd.)  ■  "hrisattm  frascimbananqm  frasHmbaySit ..; vSstrvm:  ttm  {ah  ASn.)  aß paurvavazai-'tat  aiAhe  aiti  paititil  tat'  ..V.  18.1  ^Z.; lyai  (sd.)  V.  2. 24;  —  hixrsm  .  .  ast^m  .  .'P.4j;  — asavamm  . .  ajyei^yai  mraomt..; aaÄai^Tm  .  .;  ta  (APa)  hdhra  frafrS-^  tat  zl  vatiks  Y.7/-13;  —  dazdi  m!  ydka vayaAi  y.S.16;  —  hixr?m  .  .  aslim  ....  mjanani  ..  dahat  ahmäi  ..  ya;%a  ta aishaihim  .  .;  ta  (APn.)  Aa'hra  /ra/rä-'(]S.)upauha(at\t.i5.^t; — iviqm  iainitiS vaySmi;  ti  (statt  NPn.)  kiitmti  yzary.-  \ . .  failySnte  . ,;  tarn  tä  (AP.)  aiibys  .  . yiarmtts..  V.5,i8£;  —  a%ra  ml  urvarä'.msirinavahi  Yt5.87;  —  yB  dim  *fra- raöhnü  vTspä  ,.;  ta  (statt  APf.)  ha%ra  hinan  {sA.)..,  anairyanqtn  tai  dahytmqm vJvärayemi^ . 5.  \^i.;  —  vTspanqm  narqm\vfrihrai  uzjasaiti  N.ffff;  —  agtmanqmat ..  vispanqm  gSus  sar^anqm  . .;  //(ADf.)'*'.  .  vazyail {sA.)  . .  ratSui  nmStum  fi-anäia- larpnava  müwaireisd.)  ..  V,2.27f.;  — 'yatayezi  tajyayata  naväj  tatyayata(sd.) mit  Numeniswechsel:  jahi  . .;  tisca  t^A-j.s;  s\  s',  4';  —  ym  i^  (tiDxi.)  yaf- mraomi  jq%wS.lara  ..  V.i&öa— 65;  — '  tatary  {sd.) 'S.  4  g;  —  ASn.  in  kollektivem "mi^rS.ao/anAs  ..  yatcit  vlmaiiim  (sd.)  Smo:  umarä  baiiazyä ..,- tat  vlsp^m /rTttä- ai^ha  s3mS,   t»mSt  tnihrS  hangrp/simnS  mahi,  tat'  vuppm'  . .  V,  20.  4£  a)  in
17922:•  j,  fra-sdimbana-  n.  'Stütze,  Balken, Stutz-,  BrUckenbalken':  ^risahm  'nanqm /rasambaysit  tarasca  äps  nävayä  "dreissig BrUckenbalken  soll  er  über  äiessendcm Wasser  befestigen"  V.  j8. 74; — fravasayS
22104:i)  Akt.  'sehen,  ansehen,  beschauen': vamai  F.i?;  —  I  Aarunt^stm  kärJ"  avainJ' Bh.2.13,  14;  —  hyJ' aparam  imäm  äipi. vainäAy  "der  du  später  diese  Inschrift ansehen  wirst"  Bh.^.  ig— 17^;  II  —  vTspjm vafnaiti  druzitUsm  .  .  tni^rS  Yt  10.  107; 105;  —  rriä  gqm  valnuit  astbya  Y. ^.29;  29;  —  hö  vTsp^m  akUm  ..  iiayä vamat   dßi>mbya    Yt.  ip.  94;    —    canma
26461:mit  ^a  'festmachen,  befestigen':  %ri- sttüm  frasambananqm  {si.) /rasiimbayBit*^ tarasla  äps  Ttavayä  V. /i?.  74.
29717:7/.a(/(sd.Vo  V.7.53.  DS.  7«ai  als  Inf.  L     =      hazaBrö.frasÜmbana-    Adj.    'auf
```


## [2026-09-14T02:29:21.109Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '26440,26470p' BRT.txt",
 "description": "BRT verb stamb- entry"
}
```


### [2026-09-14T02:29:21.170Z] TOOL RESULT

```
•  j.  skapta-  Adj.  'erstaunlich,  wunderbar':
mp.  (Pö.)  SliafI  (in  SO.:  adMutai),  np,  ügr// 'Erstaunen',  iiguflan  'sich  wandern'.
•  j.  skand- V. 'brechen'.   Praes.9  +  24'>
scandaya-,  ^shndaya-,  scindaya:
'zerbrechen,  zerstören,  zu  nichte  machen' : yS  rasmanö  iHndayäti  Yt  14.  62;  — Jra- vasayS  .  .  yä  .  .  aurva%anqm  ,  .  iSsBs scandayeinti  YtJj.  31;  —  ime  nS  *^uyra *bäzava  kanta  .  .  sHndayeinti  "die  da machen  unsere  starken  Arme  . .  mit  dem Messer  zu  nicht"  Yt.  /o.  42;—  tum  aisqm.. Ibaisi  scindayehi  Yt. 70.76;  —  alsqm  ihai^S scindaydmtmYt.i.tT,  —  sSndaya  {i%lh..) asavajanS  Yt.  iO.  76;  —  scindayat  F.  12,
mit  ai>i  'entzweibrcchen'(?):  yS ratmanS sHndayäti  . .  avi  rasmans  *sc?ndayeiti'^ Yt  14.  62.
mit  upa  'zerstören':  /rafa  upa.scanda- yeiii  mürS  .  .  uta  nmamm  Yt.  70.  18;  — upa  anyh  (näml  timanä)  sandayäti  Yt j  10.  28.
I  mit_^a 'zerbrechen,  zerstören,  zunichte I  machen':  fra  rasmanS  scandayäti  Yt  70.
dby  Google
IS87
skamb-
"staota-
15S8
36;  —  ahmäi  frasHndayati  nmammia  . .
Yt  10.  87;  —  tarn  ta  fraslindayehi  yil  .  .
äaiiihJvB   Yt  10.  78;  —  fravasayS  yra-
slandayeintis  . .  (bagiä  Yt  13. 33.
np.  htaila»,  likanad.  —  Pii. :  tkastan,  siaitär iSlan.  —  1)  Dieser  Antati  wegen  des  np. Fraei.  Sitanad.  Natürlich  kann  man  auch  ein Praes.  30  (Iter.)  anseilen.     S,  siami-  mit  No.  1.
—  >)  F  I,  E  1;  NA.  hat  sanä"  mit  *iner  Hds.
•  j.  skamb-  'stemmen',  nur  mit  Praev. Praes.  9+24  sambaya-^^.  —  Inf.  'scapta- yalca;  Absol.  'skamhm.
mit  upa  'festmachen':  s.  Absol.
mit  ^a  'festmachen,  befestigen':  %ri- sttüm  frasambananqm  {si.) /rasiimbayBit*^ tarasla  äps  Ttavayä  V. /i?.  74.
mit  paiti  'sich  entgegen  stemmen':  s. Inf.
ai.  skambhilhah,  siabhnäti,  liaihäydü;  np.  vgl. faliam  (Hbjc  AGr. /.  225).  —  PQ.  (ioV.7*): /rSi  aai^aniian ;  s.  noch  zum  Absol.  —  ')  iBild.
i.  BtHL.  Stud.  2.  104,  IIa.     Vgl.  auch  siattJ-
mit    No.    I.    —     '}    iSchr.    des    Nasals    s.
S  '6S.  53.
•  j.  skarana-  Adj.  (fem.  'na-)  'rund': aiibAa  z^ms  yal  pa%anayä  (sd.)  *nayS dBraiparayä  Yt.  10.  95;  5.  38,  J7, 19,
Eig.  'gekrümmt,  gedreht',  ITfP.;  %.  skärayat.- ™3o-.  Vgl.  PDw.  ;iiw-r^ 'gekrümmt',  gr.  n^arysa; Bthl.  IF.  10.  199.  —  Pü.  i  girl.
•  j.  skairya-  n.  eine  Art'*  Vorrichtung zur  Feuerung:  yö  ätnm  °yat  kaca  dsitlm gatBm  avi  avabaraiti  V.  8.  95.
Pü.!  fehlt.  ~  ■)  Welche?  Vgl.  Sf.  Komm. /.  z66,  DST.  ZA,  2.  141.
```


## [2026-09-14T02:29:43.595Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"tamb-\\|tsmb-\\|t?mb-\" BRT.txt | head -20",
 "description": "Grep BRT tamb-"
}
```


### [2026-09-14T02:29:43.650Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T02:29:50.317Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KNT stamb\"; grep -n -i \"stamba\\|stambava\\|stab-\" KNT_full.txt | head -20",
 "description": "Kent stambaka"
}
```


### [2026-09-14T02:29:50.376Z] TOOL RESULT

```
=== KNT stamb
```


## [2026-09-14T02:29:51.592Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== FVQ istabraq\"; grep -n -i \"istabraq\\|istabrak\\|stabrak\\|brocade\" FVQ_pages.txt | head -20",
 "description": "Jeffery istabraq"
}
```


### [2026-09-14T02:29:51.647Z] TOOL RESULT

```
=== FVQ istabraq
782:Qur'an of such words as ($j\L\ and ^JUu. for line silk brocade,
2432:(3j!*i' (Istabraq)
2434:Silk brocade.
```


## [2026-09-14T02:29:53.680Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '2400,2500p' FVQ_pages.txt",
 "description": "Jeffery istabraq entry"
}
```


### [2026-09-14T02:29:53.730Z] TOOL RESULT

```
scripsit (Rossini, Glossarinm, 194), so it is not impossible that there was
S. Arabian influence on the form of the word. See further under
(AM)
ii, 130, 134 ; iii, 78 ; iv, 161 ; vii, 160.
The Tribes. Flu. of ia*-

It occurs only in Madman passages and always refers to the
Children of Israel. In vii, 160, it is used normally of the Twelve Tribes,
but in all the other passages the J^L^1 are spoken of as recipients of
revelation, and one suspects that here Muhammad is confusing the
Jewish use of " the Twelve " for the Minor Prophets with that for the
Twelve Tribes. 3
The philologers derive it from a.+~ a thistle, their explanation
thereof being interesting if not convincing (LA, ix, 1 82). Some, however,
felt the difficulty, and AbiYl-Laith was constrained to admit that it was
a Hebrew loan-word (as-Suyuti, Itqan, 318 ; Mutaw, 58). The ultimate
source, of course, is the Heb. C92&7, and Geiger 141, followed by many
1 Of. QsQ2k2) !r&* cheirographum dnbium, as contrasted with
fju^A Ir4*l cfairoywphwn validum.
2 So Minganft, Syriac Influence, 89.
8 Vide Sprengcr, Lelwn, ii, 276, who thinks Muhammad took it to he a proper name,
which, however, is unlikely in view of vii, 160 (Hirschfeld, Beitrdge, 41).58 FOREIGN VOCABULARY OF THE QUR'AN
later scholars 1 has argued for the direct borrowing from Hebrew.
Fraenkel, however, noted the possibility of its having been borrowed
through the Syr. \&n = <f)v\r) 2 and Mingana, Syriac Influence, 86,
definitely claims it as a Syriac loan-word. It is impossible to decide,
but in any case it was borrowed in the sing, and given an Arabic plural.
There does not seem to be any well-attested pre-Islamic example
of the use of the word, for the case in Samau'al cannot be genuine, as
Noldeke shows (ZA, xxvii, 178), and that in Umayya, Iv, 7, "seems to
depend on Sura, Ixxxix, 23. This confirms the idea that it was a late
introduction probably by Muhammad himself.
(3j!*i' (Istabraq)
xviii, 30 ; xliv, 53 ; Iv, 54 ; Ixxvi, 21.
Silk brocade.
Used only in early passages in description of the raiment of the
faithful in Paradise. It is one of the few words that have been very
generally recognized by the Muslim authorities as a Persian loan-word, cf.
ad-Dahhak in as-Suyiitl, Itq, 319; al-Asma'I in as-Suyuti,Mwz^r,i,137;
as-Sijistanl, 49; al-Jawharl, Sihdh sub voc.; al-Kindi, Risala, 85; Ibn
al-Athlr, Nihaya, i, 38. Some, indeed, took it as an Arabic word,
attempting to derive it from (3 J. (cf. Baid. on Ixxvi, 21), but their
argument depends on a variant reading given by Ibn Muhaisin which
cannot be defended (Dvorak, Fremdw, 39, 40).
The philologers, however, were in some confusion as to the original
Persian form. LA, xi, 285, quotes az-Zajjaj as stating it was from Pers.
ayilJ, and TA, vi, 292, quotes Ibn Duraid to the effect that it is
from Syr. Dj JL-I, neither of which forms exist. The Qdmus, s.v.
:, however, rightly gives it as from a^L-l, 3 which al-Jawhari,
1 Fraenkel, Vocab, 21 ; Vautz, Offenbarung, 124 n. ; Hirschfeld, Beitrayc, 41 ;
Horovitz, KL\ 90. *
2 Horovitz also notes this possibility. The Palestinian form 1^3QJI quoted by
Sohwally, Idioticon, 92, which agrees closely with the Talmudic XMW, is not
so close to the Arabic.
3 So TA, loc. cit., and al-Khafaji, in his supcrcommentary to Bai4awi, cf. also
Addai Sher, 10.FOREIGN VOCABULARY OF THE QUR AN OVJ
Sikdh, says is from jb+*, meaning JiJ^. 1 Pers. s /^-*-l sometimes
written j*b*>\, as al-Jawhari gives it, 2 is a form of j*^** meaning
big, thick, gross, apparently from a root, j'jl**' firm, stable (cf. Skt.
Wf%T 3 ; Av. ji3&^Si^A) staura 4 ; Oss. st'ur 5 ; and Arm.
minima).? The Phlv. \)tf)) stafjr = thick (Nyberg, Glossar,
206), is used of clothing in eschatological writings, e.g. Arda Viraf,
xiv, 14, )i<o,tfp0 )K>0*) ^Itftf 1 V^ (0 1 "and glorious and thick
splendid clothing ". Phlv. ]$$$, with the suffix ), gives the Mod.
Pers. d)j*L*\, which #, 994, defines as ^/JaJ *Axj c^> and
Vullers, Zej, i, 94, as vestis serica crassior.
From Mid.Pers. the word was borrowed into Armenian as
jwiniififiiff 7, and into Syr. as lQ&a>1 or
-
Duraid, according to TA, vi, 292, quoted L?^AX-^I as a borrowing from
Syr., but PSm, 294, gives the Syr. forms only as dictionary words from
BA and BB, and there can be little doubt that the word passed directly
into Arabic from the Middle Persian. 9 The Ar. 3 represents the Phlv.
suffix ^, 10 which in Syr. normally became yi , as we see in such examples
1 BQ, 492, defines it as kJLs. dL til) . ,of Vullcrs, 7,ca:, i, 97.
^ w > > .
3 Lagardc, 6M, 13. ^f%^ means thick, compact, solid, cf. Monicr Williams,
Ninificrit Dictionary, 1265.
4 Rartholomap, AI W, 1592; Horn, Grundrixx, p. 158; Hubsohmann, Persische
Mudicn, 74.
5 For this Ossetian form see Hubschmann, ZDMG 9 xxxix, 93.
Hubsebmann, Arm. (iramtn, i, 493. Cf. also Gk. oravpos.
7 Hubschmann, Arm. tiramm, i, 153. The form seems proof that the borrowing
was from Pers. and not from Ar., though the passage in Moses Kalankatuaci, which
Hubsuhmann quotes, refers to fujunuLftw/^u [^ ai^jiuiiu/^u t a gift from the Caliph
Mu'awiya I. Cf. Stackelberg in ZDAIG, xlviii, 490.
8 Fraenkel, Vocab, 25, quotes this as L. JI^AcD |, which is copied by Dvorak, Fremdw,
42, and Horovitz, Parodies, 16, but neither this form nor the (l^AflOl quoted by Addai
Sher, 10, is to be found in the Syriae Lexicons.
9 Mingana, Syriac Influetice, 88, however, claims that the borrowing was from Syr.
into Arabic.
10 The philologers had recognized, however, that Pers. <il did sometimes become ^
in Ar. Cf. SIbawaih in Siddiqi, 21.60 FOREIGN VOCABULARY OF THE QUR*AN
as Phlv. ^-utf)3O* avistak (= Pers. lx*%j| or lu*^!), 1 which in
Syr. is ^Afioaj^ an d in Ar. v3^l (Ibn al-Athlr, Nihaya, i, 38).
(Ishdq).
ii, 127-134 ; iii, 78 ; iv, 161 ; vi, 84 ; xi, 74 ; xii, 6, 38 ; xiv, 41 ;
xix, 50 ; xxi, 72 ; xxix, 26 ; xxxvii, 112, 113 ; xxxviii, 45.
Isaac.
The Biblical Patriarch, who is never mentioned save in connection
with one or more of the other Patriarchs, and never in an early passage.
```


## [2026-09-14T02:30:03.167Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"stab\\|stamb\\|rebel\" KNT_full.txt | head -40",
 "description": "Kent grep stab/stamb"
}
```


### [2026-09-14T02:30:03.225Z] TOOL RESULT

```
2789:§30. OLD Persian у seems to be established in 
2878:$31. OLD Persian ar seems to be established 
2909:$32. Отр Persian ara seems to be established * 
2931:to be established in the following: 
4954:established’ (on -$-, §117), Skt. dsddayam. 
5041:the name assumed by the Median rebel Phra- 
5192:unassimilated -tp-, established by the Elam. and 
5216:apatatā ‘he rose up (in rebellion)’, suffers com- 
6188:Sku"za a Seythian rebel, Elam. 23-ku-in-qa. 
6728:niyasddayam ‘I established’. 
9342:ferentiation would seem to be established. Yet in 
10765:- apatata ‘he rose up, rebelled’. 
11138:tarsam; 2d sg. stabava* apa-gaudaya* ava-rada*; 3d 
11499:mà: ist sg. tarsam (226.1), 2d sg. stabavat apa- 
11886:maty hamigiya abava ‘he became rebellious toward 3 
12356:jadiy ‘the rebel army which does not call itself 
12359:hya mand naty gaubdtaiy атат jatà ‘the rebel army 
12416:and Hyrcania became rebellious from me, they 
12651:people’ (DB 4.34f), where zmazy refers to the rebel 
12907:mands proceed (= agent), from whom rebellion 
13006:rebels assembled (and) eame out'; DNa 43-5 
13251:stabava DNa 60; in the third person, &adaya DNa 
13450:tala ‘when he rose up in rebellion’. The same 
13900:hamigiyam ‘that rebellious army’ (DB 2.35, etc.). 
14086:іаїу ‘the rebel army which does not call itself 
14555:rebellious, whatever I see (to be) not (rebellious)’; 
15394:stand m line the captive rebels, 9 in number, with 
16821:establishing the original text of a number of passages 
16993:people became rebellious from Cambyses, (and) 
17031:that I put in its place; I reestablished it on its 
17037:reestablished the people on its foundation, both 
17052:strove until I reestablished our royal house on its 
17065:rebellious, (and) went over to that Аспа; he 
17071:Nidintu-Bel; Babylonia became rebellious; he 
17283:Nores то DB II: * asabirazbi$, form established by 
17342:rebellious from me: Persia, Elam, Media, Assyria, 
17372:rebellious from me, (and) went over to that 
17388:rebellious army exceedingly. Of the month Ana- 
17401:forth, that rebellious army which does not call 
17404:menia, thereafter the rebels assembled (and) came
```


## [2026-09-14T02:30:11.917Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nfor k in ['POK','KNT','BQT','MON','SOD','FVQ','FSF','AHD','WLD','PHD','NYB','HRN','HUB','ARY','IEC','SYN','KLN','SKT','BRT']:\n    v=d.get(k)\n    print(k, json.dumps(v, ensure_ascii=False)[:600])\n    print()\n\"",
 "description": "Inspect refs_online entries"
}
```


### [2026-09-14T02:30:13.036Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id=

FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sou

FSF {"title": "Abdolhossein Noushin, Vazhe-namak: Farhang-e Vazheha-ye Doshvar-e Shahnameh (Farhang-e Shahnameh), Donya 1363/1984", "kind": "archive_djvu", "url": "https://archive.org/details/20220809_20220809_1444", "lookup_hint": "grep the headword in FSF_pages.txt (alphabetical glossary); use inside.php search for leaf numbers. Also https://archive.org/details/nooshinshahnameh is a different Noushin book (گزارشی چند درباره شاهنامه).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF.txt"], "page_offs

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-

NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1
```


## [2026-09-14T02:30:19.751Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"stabava\\|stab-\\|tab-\" KNT_full.txt | sed -n '1,60p'; echo \"=== total lines\"; wc -l KNT_full.txt",
 "description": "Kent stabava occurrences"
}
```


### [2026-09-14T02:30:19.814Z] TOOL RESULT

```
11138:tarsam; 2d sg. stabava* apa-gaudaya* ava-rada*; 3d 
11499:mà: ist sg. tarsam (226.1), 2d sg. stabavat apa- 
13251:stabava DNa 60; in the third person, &adaya DNa 
19324:60 : avarada : mà : stabava 
19347:with Wb. © stabava (as Rl. JRAS 10.310 had it), see Lex. 
29239:MB Gr. $202). stabava 2d sg. inj. (8216, §224, 
=== total lines
29987 KNT_full.txt
```


## [2026-09-14T02:30:22.259Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '29220,29260p' KNT_full.txt",
 "description": "Kent lexicon stabava entry"
}
```


### [2026-09-14T02:30:22.330Z] TOOL RESULT

```
Ist sg. imf. (§214) DB 1.63, 66, 69. 

ni- + sld-, generalized ništā- (8117, $140. VT), 
‘enjoin, command’ (ef. Altheim, ZII 3.37; Hz. 
ApI 315-8): niyasidyam 1st sg. imf. (5140.1, 
§214) DB 3.91; DZe 8, 11; XV 23f. niyaštāya 
imf. D8n 1; XPh 50; XV 21; nistàya (528.1, $140.- 
IIT) XPh 52. 


stana- sb. ‘place’: Ау. -siána- in сраз., NPers. 
-stán, Skt. sthana-; deriv. of root sta- ($116, $122, 
§132.2-3, §147.1). See also ardastana-. siünam 
asn. XV 20f. 


sta™b- vb. ‘revolt’: NPers. suámb- ‘revolt’, 
perhaps also Skt. sta(m)bh- ‘fasten, hold up, op- 
pose’ (Wb. AbkSGW 29.1.34; Mt. Аз. 1911.637; 
MB Gr. $202). stabava 2d sg. inj. (8216, §224, 
6227.1, $287) DNa 60. 


stiind- sb. ‘column’: Av. stna- masc., stünà- 
fem., NPers. sutūn, Skt. sthiind- (6147.1). stund 
npf. DSf 45 (wrongly nsf. collective, Hz. AMI 
3.68-9). [stünä}] apf. DSg 3°. stünaya uncertain 
form, perhaps 18. (for -àya, $52.IIT, $176, §255; 
hardly adj. asm., with Hinz, ZDMG 95.250; 
wrongly Kent, JAOS 51.227-8) D'Sa 1, A?Hb. 


späda- sb. ‘army’: GAv. spdda-, NPers. sipah, 
Anglo-Indian spahi; in Taxmaspada-, cf. spá- 
maida- (76.V, $83.IT, $116, 5143.11). Possibly 
from pIE *kyd- ‘swell, be great’ (Gray, Lg. 25. 
377-8; cf. §90). ‘ 


spü&maida- sb. ‘camp, war’, meaning shown 
by АКК. version: cf. späda- ‘army’ (883.II), Av.
```


## [2026-09-14T02:30:30.124Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR<=29239{n+=gsub(/\\f/,\"\")} END{print \"formfeeds before line 29239:\", n}' KNT_full.txt",
 "description": "Find leaf for Kent stambava"
}
```


### [2026-09-14T02:30:31.317Z] TOOL RESULT

```
formfeeds before line 29239: 0
```


## [2026-09-14T02:30:37.406Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '29100,29250p' KNT_full.txt | grep -n \"^[0-9]\\{3\\}\\|LEXICON\\|OLD PERSIAN\" ",
 "description": "Find page marker near Kent stamb"
}
```


### [2026-09-14T02:30:37.461Z] TOOL RESULT

```
69:1935.489-96. 
98:210 
141:6227.1, $287) DNa 60.
```


## [2026-09-14T02:30:41.916Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nv=d['BQT']\nprint(json.dumps(v, ensure_ascii=False, indent=1))\n\"",
 "description": "BQT offsets"
}
```


### [2026-09-14T02:30:42.977Z] TOOL RESULT

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
```


## [2026-09-14T02:30:51.104Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==559' BQT_v2_pages.txt | head -80",
 "description": "BQT vol2 leaf 558 (p.1098)"
}
```


### [2026-09-14T02:30:52.159Z] TOOL RESULT

```
 ‫‪۱۰۵۹‬‬                                                                                                                     ‫ستار‬
‫تک ناف و آن چیزست راست ‪ ۳‬تنک و بهن‬
                                                                     ‫فر»‬
                                                                     ‫ف‬       ‫ستاد = بنتح اول برو‬
                                                                       ‫مزنخقطا‬
‫بمرض دوانگشت بافکموترل‪,‬اادزباجوب واستضوان‬                       ‫ستاره باشد که‌بعربی کو کب خوانندا ‪-‬وخیمه‌ای‬
‫و امثال آن سازندویعربی مسطر خوالند ؛ویمعنی‬
                                                                ‫را یزکوبند کهبجهت منم مگس وپشه زند‬
‫کوکب ومسطر بفتح اول گهفمته‌اند ‪ -‬و بازی‬
 ‫سیم فرد را یز گوبند که ستا باشد و‪۷‬ب‪-‬معنی‬
                                                                ‫وبتکار دارریلن هزمماآنمده‌دااسنت گووابینن‌داصح؛‌اوسبتس‪-‬نیو سااوزل‬
‫رات وعلم‌هم آمده است ‪ -‬وآستان درخانه راهم‬                                                      ‫طتبور را حم میگوبند ‪۴‬‬
                           ‫‪:‬‬       ‫کو‬
                                                                ‫ستاره ‪ -‬بفتح اول بروزن شرارهءنوعی‬
                                                                ‫راازچناییزربکاوشندنکده کدهر‪۲‬اازشاپمایراچنةه‌خوابنينادر ‪-‬ناوخیمه‌ای‬
‫ستارة رهیی ه‌کنانه از سنگه طلق‬
‫باشد » و آن سنگی احت مانند آیینه براق‬
                                                                ‫زك دوزند‬
  ‫از روی حم مرھىشىرد ‪.‬‬             ‫وشفاف که برده برده‬                                                     ‫بجهت منع مک‬
                                                                ‫و بشه ‪ ۳‬آ را درین زمان‬
‫ستاره شمر ‪ ۰ ۸‬بن شین نقطه‌دار »‬
                                                            ‫بشه‌دان خوانند ‪ ۴‬؛ و ؛معنی اول بکسر اول‌هم‬
                    ‫منجم وستاره شنای رگاوبند ‪.‬‬                  ‫آمده است که بروزن آشاره باشد ؛ وبکسر اول‬
‫ستاره شمردن ‪ -‬کنابه از بدا‬                                      ‫طنبوره وسازیرا گویند که ‪-‬ه‌تار داشته‌باشد وباین‬
                         ‫کردن وشب زنده‌داری باشد‪.‬‬           ‫ممتی منقصل بابد نوشت ‪ - ۴‬و کوک را یز‬
‫شمر‬   ‫بمعنی‌ستاره‬    ‫=‬   ‫ستاره شناس ‪٩‬‏‬                          ‫کوبند ® ‪ -‬و افزار جدول کثانرا ‪ ۱‬حم ستاره‬
                                                                                       ‫‪ :‬ستاره ‪.‬‬      ‫رکه‬         ‫‪۱‬‬


  ‫‪ - ۴‬بقول داد که ستاره عربی است بممنی پوشش مشتق ازستو(پوشیدن)‬                                    ‫سیم است)رك ‪:‬ساره ‪.‬‬

  ‫‪ :‬دارای‬    ‫(ست)‬        ‫تار ط ه‬      ‫از ‪ :‬سف‬   ‫‪-‬‬   ‫‪۴‬‬   ‫سار ‪.‬‬     ‫ورك ‪:‬تاه‬       ‫اسشق ‪۷‬‬                    ‫دهوبشمان؟ ‪۱۷6‬‬

  ‫باستان‬    ‫«هندی‬    ‫«‪:‬نسرکه ‪»۷۰۲‬‬       ‫_اوستا‪( ۲25-‬کوکب)؛یپلوی ‪2۲20۹‬‬                                  ‫‪ :‬صتار ‪.‬‬   ‫رك‬    ‫سیم‬


  ‫و ]‪ahg‬‏ ‪( rats‬چشم)‪ .‬استی ‪, stali‬‬
                                ‫تفا ‪ ,‬ارمنی ‪u‬‏ کردی ‪٤۲1‬‏ ‪ ,‬افغانی ‪1۵۲01‬‬
   ‫وخی ‪. ۲05‬شفنی ‪۷۲۵20۲٩‬‏ ‪, ۷71۸0٩ ,‬سریکلی ‪. ×11‬منج ‪. 74082‬سنکلیجی ‪127051۷‬‬
                    ‫«اسشق ‪ ۰ ۱۱۷۲‬دزفولی ‪ 31252‬و ‪ 8۲2065‬دامام» ‪ .‬گیلکی ‪. 2۲8125‬‬
  ‫دوشت و ستاره با اء منقوط باين ممتی که در‬                       ‫ف‬
                                                                 ‫لطاء‬
                                                                    ‫مد با‬
                                                                        ‫‪«- ۱‬باين ممتی کوبا باب‬
                                                                                                            ‫ست گلتان ‪:‬‬
               ‫‪.‬‬    ‫شواند که کج رود دول‬                                  ‫لاجرم چون ستاره راست بود‬
                                                                    ‫واين بت دیگر سمدی در قصاند ‪:‬‬

             ‫دانی که بی ستاره‌ترفته‌است‌جدولی‪.‬‬                   ‫ترواست باش تا گ«ران راستی کنند‬
  ‫در اغلب سخ خطی و چاپی بائاء منقوط دوشته » بايد بدون شبهة غلط ناج باشد و در‬

  ‫چاپ فروغی درموضم دوم باطاء ملف وشته ‪ ,‬سوطاره مشدداً که درست مزبور لابد ضرورة‬
‫ديدمکهدر‬
       ‫کتبلفتیفنم« قیاساًسیر معفولو درست بنظرمیآید و بعد‬
                                                       ‫مخخف خد »ه در‬
 ‫‪:‬انی که‬
       ‫نخة وحیدالملکی کهاقدمنخکلیات سمدی است ایز سطاره دربن بت دومی ععنی د‬
 ‫‪ . 1‬در‬                   ‫بسیطاره ترفته است جدولی ‪ +‬صربحا واضحاً باطاء مولفه مسطور‬
                   ‫فرخنگه رشدی دز آمده ‪ « :‬ستاره بمعنی مسطر جدول سطاره است‌بطا وعربی است‬
                                     ‫‪ - ۸‬لز ‪ :‬ستاره شمر (شمرلده) ‪.‬‬                          ‫‪ - ۷‬رکه‪ :‬ستا‪.‬‬
                                                        ‫‏‪ - ٩‬از ‪ :‬ستاره ‪ +‬شنای (شناسنده) ‪.‬‬
```


## [2026-09-14T02:31:05.460Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 560 561 562; do echo \"###### NR=$n\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' BQT_v2_pages.txt | head -60; done",
 "description": "BQT vol2 leaves 559-561"
}
```


### [2026-09-14T02:31:06.527Z] TOOL RESULT

```
###### NR=560
                                                                                           ‫‪ ۷4۰‬ات‬
‫‪ -‬وبضی مطلق شاخ درخت را گفتداند خواه‬
‫تازه باشد و خواه غیر نازه ؛ وبشین تقطمدار حم‬        ‫=به از آفتاب‬
                                                               ‫ستارة قلندر اکننا‬
 ‫آمده است و درست است چه درفارسی سی‌وشن‬                                               ‫عالمتاب است ‪.‬‬
                            ‫بتهبمدبل مییابند‪.‬‬        ‫=کسر اول بروزن چراغ؛بمعنی‬
                                                                             ‫ستاع ب‬
 ‫ساخت‬        ‫لرجام‬
                 ‫نو‌ل ب‬
                      ‫وسزر ا‬
                           ‫ستام ‪ -‬بک‬                ‫کرة اسب شیر خواره باشد ‪ -‬و کرة اسبیرا لیز‬
                                                    ‫کوبند که هنوز اورا زین بریشت نهاده‌باشند ‪۱‬‬
  ‫وتی‬
    ‫‪۵‬م‪-‬ع‬
       ‫وبراق زين اسب راکوبند مطلقاً ب‬
                                                    ‫‪-‬مطلق اسبرا بکیوزبند اعمازآنکه کره‌باشد‬‫و‬
‫عخملی بزر وشره هم‌آمده است‬        ‫راوفار‬
                                       ‫سام‬
                                         ‫لج‬
               ‫گزوبند ‪٩‬‏ ‪.‬‬
                         ‫‪ -‬وآ‪-‬تان درخانه رال‬
                                                     ‫ودم‬‫اسب ازاینده آ‬       ‫نوی‬  ‫عه ‪-‬‬‫مکر‬
                                                                                       ‫بغیر‬
                                                                                          ‫با‬
                                                     ‫که بفارسی سترون و بعربی‬         ‫بازاینده حم هت‬
 ‫ستان ‪ -‬بکر اول بروزن شان‪,‬بریشت‬                      ‫عقیمه گوبند ‪ -‬و شتران شبردهنده وشتران‌سیار‬
‫ای ابوهی وبیلری‬
              ‫خواییده راکوبند ‪- ۷‬جو‬                  ‫شیر را یز ستاغ میگویند؟ و‪-‬بمعئی سرون‌هم‬
 ‫چیز ها بائد ‪ ۸‬همچو کلتان ويتان‬                      ‫وشوفتفہ دوعترا‬
                                                                  ‫آمده است که شاخ کگاو‬
 ‫رهندوستان وامثال آن وباین معتی‌بدون ترکیپ‬                                              ‫وکفل باشد‪.‬‬
‫یز‬         ‫طیاقت‬
               ‫‌ی ب‬
                  ‫یمعن‬
                     ‫یوب‬
                       ‫و‪-‬‬‫ر‌شود‬
                             ‫بدمی‬
                                ‫صته‬
                                  ‫گف‬                ‫بکر اول وثانی‌بالف کشیدہ‬         ‫ستاك ‪۴‬‬
     ‫ی‬
     ‫جتاکه‬
         ‫آستان هم ه‬           ‫فف‬
                               ‫خ‪-‬‬‫ماست‬‫وده‬
                                       ‫آم‬           ‫و بکاف زده ‪ ,‬حر شاح دورستة تازه و داز را‬
‫کفش کندن است درخانها‪ -‬ویفتح اول ستاننده‬              ‫کون که از بیخ درخت بجهد عموماً ‪ ۴‬سوشاخ‬
‫راگونن که چیزی گیرنده باشد ‪ -‬و امر باین‬              ‫بازك و تاز درخت تاك راکه درخت انگور باشد‬
               ‫معنی حمحت یمنی بستان وبگیر‪.‬‬           ‫کوبند خصوصاً وآنرا بسبب ترش‌م زگی‌میخورند‬
                                         ‫«ستاغ ‪ ,‬اسب زین ناکرده ‪ .‬خفاف کفت ‪:‬‬             ‫‪- ۱‬‬

                ‫مهنی‪».‬‬
                     ‫ارزه ج‬
                          ‫لوچون ستاغ ک‬                     ‫من با تورام باشم حمواره‬
     ‫د لفت فری ‪ > ۷۳۲‬۔‬
                           ‫‪ = ۴‬متاخ = استاخ (هم‪. ).‬‬
                                            ‫‪ - ۴‬سوسن‌لطیف وشیربن‌چون خوشه‌های‌سیمین‬
     ‫‪۰‬‬   ‫کایی‌مروزی‪ .‬لفت فری‪»۷۲ 4‬‬    ‫برج ثور وجوزا‪.‬‬     ‫چون‬   ‫شاخ و ساك سرین‬


               ‫اسب با زین خسروی وستام ‪.‬‬                    ‫© در زمان سوی توفرستادی‬
     ‫‪:‬‬    ‫فرخی سیستالی‪«.‬لفت‌فری ‪4۴‬‬
###### NR=561
‫هه اس‬                                                                                                ‫ستاله‬


‫گفتن‬   ‫لمیدحکوبی‬  ‫دعا وثنا وشکر لسمت و‬                ‫ستائه ‪ = ۱‬بر وزن فاله "بمعنی آستاله‬
                   ‫وستودن وآفرین باشد ‪.‬‬                                ‫دن باشد‪.‬‬   ‫کینکفش‬
                                                                                       ‫است که جا‬
‫ستایشگاه ‪ -‬شربطه و مخلص شمر را‬                        ‫دماوند ؛‬     ‫ستاو ند = بفتح اول بورزن‬
‫کوبند بمنی بیتی که فصبده باقطعه بامثنوی‬               ‫رواق و بالا خانه باشد که بیش آن مانند ابوان‬
                              ‫بدان تمام شود ‪٩‬‏ ‪*.‬‬        ‫نزد‬
                                                           ‫ما ی‬
                                                              ‫هر‬‫و‬‫کر ک‬
                                                                    ‫کوده بود و‪-‬صفهٌ بلندی بز‬

‫ستیر ‪ ۲‬ه بکر اول » بروزن و معنی‬                      ‫ص‪-‬فوه‌ای رکانهتمه‌اند که سقف آنرا بيك‬
‫سطبر است که کنده و لك ويك و غلبظ باشد ؛‬               ‫سبتروانفراشته باشند ‪ ۴‬؛ و باضومل‌یز آمده‬
                                                                                                     ‫است ‪.‬‬
                ‫وسطبر با طای حطی معرب آنست ‪.‬‬
 ‫ستبر نای ‪- ۸‬بانون بکاشلیفدهبتحتانی‬                   ‫ستأوه ‪ -‬بفتح اول جروزن کجاوه‪.‬بمعنی‬
                                                      ‫مکر و فریب و حیله و خدعه باشد ‪# ۴‬ویکسر‬
‫زده ‪,‬کند کی و سطبری و غلیظی و لك و یکی‬                                                   ‫اول همگفته‌اند ‪۰‬‬
‫ربکزی چیزی را کویند وآ ارابعربی خضمه‬ ‫و‬
                               ‫خوانند ‪.‬‬                ‫بکر اول بروزن سياه ‪ ۰‬مخفف‬‫ستأه ب‬
                                                      ‫ستاره باشد که‌بعریی کو کب کوبند ‪ - ۴‬وبمعنی‬
 ‫ستخر *‪ -‬بکر اول‌وفتح ثانی‌وسکون‬
 ‫تفای اقطفوار بوروای ب فة محف اس‬                      ‫تقره وسم قلب‌وناسره هم مده است‪-‬ونام پرده‌ای‬
                                                                                   ‫ازموسیتقی ‪.‬‬       ‫حم هت‬
 ‫است که تالاب و یگنر باشد _ و نام قلعه‌ایست‬
‫مشهور در فاری که جمشید ساخته است وچون‌حر‬               ‫ستایش * = بکر اول بروزن‌فزایش‪,‬‬
                                                                  ‫وك‪ :‬آستانه ‪ 4‬آستان ‪۰‬‬           ‫‪۱‬‬

        ‫بایوان چه بری رلج ویکاخ وبتاوند ؟!‬              ‫‪_ ۴‬جهان جای بقا نیست باسانی بگذار‬
   ‫طان‌مرءری‪« .‬لغت فرس ‪۹٩‬؟‪.‬‏‬
                                      ‫انگیزد از برای توهردم ستاوه‌ای ‪ .‬بنقل رشیدی ‪.‬‬              ‫‪2‬‬
  ‫‪« - ۴‬مولف چهانگیری لفظ مکذور را مخفف ستاره هم خبطکرده واین شعر ابوالفرج‬
                                                                             ‫آوزده ‪:‬‬    ‫رولی را هم شاهد‬

           ‫‪۰‬‬    ‫بگفتار اوسیپر وستاه‬   ‫ص‬   ‫نپاده‬           ‫کشاده چشم بدبدار او زمین‌وزمان‬
  ‫لیکن در سخة چاپ طهران دبوان ابرالفرج بجای ستاه «سپاه» نوشته و درتصحیح بجای‬
  ‫نطام»‪.‬‬       ‫لفظطی نست‪».‬افرهنگه‬     ‫وسیاه» را صحیح دانته ‪ ۰‬دس ستاه مخفف‌ستاره‬         ‫سيهر وستاه اصییف‬

                 ‫® _ اسم مصدر از ستاییدن و ستودن » پهلوی ‪nhs)i(yãts‬‏ «اسشق ‪۹۱۲۷٩‬‏ ‪.‬‬
                ‫ستایشگاه شعر وخطبه ‪ ,‬تا حشر‪.‬‬                     ‫‏‪ ٩‬بنام و کنیتت آراسته باد‬
       ‫‪.‬‬
       ‫‪8‬ی؟‪۵۱‬‬
           ‫عنصری بلخی‪«.‬لخت فر‬
  ‫استبر ‪ ,‬اوستا ‪-arhbatse ( 8۳۷۷205-‬‏ ‪( ) ۵۲۵۳۵۵۳۱٩ .‬محکم ) » پهلوی‬                              ‫‪۲‬‬
  ‫تکیه دادن ) ‪ ۰‬قس ‪:‬‬           ‫و ‪ . ۴۷7215‬هندی بانتان ره — ‪hbats‬‏ ( تمیدن کردن‬                        ‫‪۲7‬‬
                       ‫استی ‪( 0205‬قوی) «اسشق ‪ ۳۱۷۰‬ورك‪ :‬حوبشمان ‪ ۳۱۷‬ویب رکه ص ‪. ۹۰۲‬‬
                ‫‪ _ ۸‬از ‪ :‬ستبر («‪.‬م‪ - ).‬بای (= با‪,‬یوند اسم مصنر همجو حرازنا ‪,‬ژرفنا) ‪.‬‬
                                                                         ‫‪.‬‬   ‫‪ :‬استخر‪‎‬‬   ‫رك‬   ‫_‬   ‫‪٩‬‬

   ‫‪ ۶#‬ستایبدی ‪ -‬از ‪ :‬ستا (ه‪.‬م‪ -۳).‬بدن ( پسوند مصدری )‪,‬پپلوی ‪ « 042011205‬اسشق‬

###### NR=562
                                                                                                                          ‫نز شا او‬

            ‫بقزرک‬
        ‫وهیجث‬
  ‫‌ههویکل‬                                ‫یمت‬  ‫فے»‬
                                           ‫امرد‬   ‫بز‬
                                                ‫برگ‬                            ‫آن تالاب بزرکی هت بنابر آن بدان‌نام‌خوانند‪,‬‬
 ‫وتند وخشمناك‬         ‫و ستیزه‌کار‬       ‫را گوشد ‪-‬‬            ‫و درشت‬
                                                                                                              ‫و صطخر معرب آلست‪.‬‬
‫بی‌آزرم را‬    ‫را لیز گفته اند‪ -‬و مردم لجوج و‬
‫هم میگوبند ‪ ۸‬؛ و بفتح اول و کسر اول حم‬                                        ‫ثالث و سین بی‌نقطة مفتوح ‪ ۰‬بمعنی غربال باشد‬
                                                ‫آمده ات ‪.‬‬
                                                                                       ‫که بدان چیزها پزند وبعربی حلهال‌خوانند‪.‬‬
‫ستر کا ‏ بفتح اول وثالی وسکون ثالث‬

 ‫وکاف بالف کشیده ‏ صمغی است سرخ بیاهی‬                                                         ‫استخوان است و بتازی عظم گوبند ‪.‬‬
 ‫مایل ؛ وبعضی گونند صمح درخت روم است‪.‬وآن‬
                                                                              ‫بفتح اول بر وزن لبریز »‬          ‫=‬   ‫‪۴‬‬    ‫ستخىز‬
‫درختی است که مقل مکی میوژ آانمت ؛‬
                                                                                  ‫مخفف رستخیز است که محشروقیامت باشد‪*.‬‬
 ‫و بعضی دیگر کوبند که صمغ حرخت زبتون‬                                          ‫‪ = ۳‬بفتح اول بروزن سفر مخفف‬                      ‫سر‬
‫امت و ترله را نافع‬            ‫کرم و خفك‬             ‫است و آن‬

                                                         ‫میباشد ‏‬                                ‫استر است کهبعربی بغل گوبند ‪.‬‬
‫بم اول وئائیو کر کاف‬                ‫‪-‬‬        ‫ستر کش‬
                                                                                  ‫ستر ان ؟ ‪ ۰‬بکر اول بروزن‌فشردن‪,‬‬
 ‫(‪ .)۱‬بمعنی برآشفتن‪-‬‬                ‫طنهش‌یندار‬
                                             ‫ن سقکو‬
                                                  ‫و‬                           ‫؛بضم اول‬
                                                                                     ‫بمعنی باكکردن وتراشیدن باشد ® و‬
                                                                                                                   ‫وثالی عمگفته‌اند ‪.‬‬
    ‫جولال باشد که در مقابل شکفتن ج‬
 ‫ومال‬
                                                               ‫ا‬              ‫‪4‬‬    ‫فاك‪.‬ا‪۱‬‬    ‫بقعح اول بروزن‬    ‫=‬
                                                                                                                   ‫‪۹‬‬

                                                                                                                        ‫ستر سا‬
                                                                                                                                 ‫ِ‬




 ‫بقتح اول بروزن‌بدرنگه‪,‬‬          ‫سترنگ"! ص‬                                    ‫بمعنی حس باشد و جمع آن حواس است و‬
‫مردم کیا باشد » وآن رستنی و نباتی است شبیه‬                                    ‫ستر سالیبمعنی حی‌منی آنچه بنظر وحس‬
 ‫بآدمی و درزمین چین روبد ‪ .‬گوبند تگون سار‬                                                                                            ‫در اید ‪.‬‬

   ‫می‬
    ‫دسر‬
      ‫آوی‬
        ‫بود چنان کهربشه اش بمنزلة م‬                                            ‫= یسم اول و انی بر وزن‬              ‫‪۷‬‬     ‫س‬



                                                                                              ‫تقطه دار ‪.‬‬   ‫‪- :‬‬     ‫چك‬    ‫(‪)۱‬‬


                                                    ‫‪٣‬‏‬        ‫ر مخز‬     ‫رك‪:‬‬        ‫‪۴‬‬             ‫‪ - ۱‬رك‪ :‬استخوان ‪.‬‬
             ‫چذانکه لشکر طالوت کرد برجالوت‪.‬‬                                         ‫بجان منبر ستخیز کرد لشکرعشق‬
   ‫از ‪:‬متر ‪+‬‬          ‫‪-‬‬   ‫‪۴‬‬              ‫‪.‬‬   ‫استر‬   ‫وك‪:‬‬        ‫‪--‬‬   ‫‪۴‬‬
                                                                                       ‫طیان مرغزی‪.‬هلفت فرس ‪۹۸۱٩‬‏ ‪.‬‬
```


## [2026-09-14T02:31:35.950Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"ستنبه\\|سترنبه\\|ستنبک\" BQT_v2_pages.txt | head -20",
 "description": "Grep BQT v2 for setonbeh"
}
```


### [2026-09-14T02:31:36.043Z] TOOL RESULT

```
33653: ‫ستنبه ‏ = بکر اول بروزن شکنبه »‬                        ‫کتیبی ابن لفت استرمالند است چه ستربمعنی‬
33673:                                 ‫‪ = ¥‬ستمبه‪.‬رك ‪ :‬استنبه » پارسی با‪۹‬ست‪0‬ان‪-8‬‬
33732:          ‫دلیر و ستنبه هو کینه کاه‪.‬‬                         ‫‪ -‬ازابرانیان بد تهم کینه‌خواه‬
```


## [2026-09-14T02:31:39.372Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"; n=0} {n++; if (index($0,\"ستنبه\")>0) print \"LEAF_NR=\"n}' BQT_v2_pages.txt; echo \"---\"; awk 'BEGIN{RS=\"\\f\"} NR==563' BQT_v2_pages.txt | sed -n '1,70p'",
 "description": "Locate setonbeh leaf"
}
```


### [2026-09-14T02:31:40.455Z] TOOL RESULT

```
LEAF_NR=563
LEAF_NR=564
---
  ‫‪۵‬ات‬       ‫‪4‬‬
                                                                                              ‫سثروك‬
 ‫استرءوون بمعنی شبه و مانند" باشد‪ ,‬وچون‌استر‬           ‫باشد اروماده دست در گردن هم کرده و بابها در‬
‫لمی‌زابد او را باین‌اعتبار بدین نام خواننماند ‪-۴‬‬          ‫اتی‬
                                                            ‫ییراس‬
                                                                ‫رپا‬
                                                                  ‫بررا‬
                                                                     ‫یکدیگر محکم ساخته ون‬
 ‫زولی رکاویزبند که بیش ايزك‌فرزند‬                      ‫چپ ماده افتاده است و ماده را بمکس آن»وهر‬
‫تزایینه‌باشد ‪ ۰‬وبا اول وثالی‌مضموم همآ مفهاست‪.‬‬
                                                        ‫آرا بکند باندك روزی بمترد » و حاصل‬
                                                                                         ‫کس ا‬
‫بفتح اول و الی بروزن کقل »‬         ‫‪-‬‬   ‫ستل‬              ‫کردن آن باین نوع است که اطراف نآراخالی‬
 ‫بمعنی كتك زدن وآزاردادن باشد ‪ -‬وبکراول‪,‬‬                ‫کنند چنانکه بادك قولی کنده شود؛س‌رسمالی‬
          ‫ند ® ‪.‬‬
               ‫کتخورنرا‬
                      ‫لاب و اس‬
                             ‫وبتکایر‬
                                   ‫آ‬                   ‫آوریه وبك سر ران را برآن و سر دیگر‬
 ‫ستم = بکر اول بروزن شکم‪ .‬ممروف‬                       ‫شکاری در‬          ‫جذنادلووری‬
                                                                                 ‫راکبمر سکی بن‬
                                                                                             ‫و‬
‫است که تمدی و آزار باشد ‪٩‬‏ ‪ -‬و بمعتی دبفه‬              ‫شکار‬     ‫مجالب‬    ‫يا سکه‬    ‫سگه سر دهند‬    ‫یش‬

        ‫هنتف خوالند‪.‬‬   ‫‪ ۳‬دانته لیز کفته‌اند و دمر ی‬     ‫بدود وآن از بیخکنده شود آونرا بعربی‪,‬بروج‪-‬‬
‫ستم آ پاد ک‪-‬نابه ازجابی است که‬                          ‫الستم خواند ‪ -‬وبازبی هم هت مشهوروممرول‬

                                                       ‫ز چوپ سا اند پاين ابر سترنه نل‬
 ‫آا للم و تعدی بسیار وافع شود ک‪-‬نوابه‬
                                    ‫در ن‬                ‫و چون درآن بازی صورت پادشاه ووز هردورا‬
                                 ‫از دیا هم هت ‪.‬‬

 ‫‪۰‬نابه‬
     ‫ستم بر ور = بفتح بای فارسی ک‬
                                                       ‫نهاده اند و معرب آن شطرنج است و اکنون به‬
                                                                               ‫قعرمب اشتهار دارد ‪٩‬‏ ‪.‬‬
  ‫نده و ظلم روا دارنده باشد ‪.‬‬
                            ‫کطنلم‬
                                ‫از ظالم و‬
                                                        ‫ستر و لك= بفتح اول‌بروزن متروك‪,‬مردم‬
 ‫ستی آ و ده ‪ -‬من اول والی‌وسکون‬                         ‫می‌مایه وییکار ‪ -‬وبدخو و خشمناك ‪ -‬ودزد پیشه‬
 ‫لون وهمزه ممدوده و فتح واو و تون ودال ابجد‬                                       ‫‪ -‬وهرژه گوی رکاویند‪.‬‬
 ‫هردو حاکن » صفه و ابوان خاله را گونندکه‬
 ‫بيك ستون بر پباایشد ؛ و بکسر اول یز‬                    ‫سترون ‪ /‬ه بفتح اول و واو بر وزن‬
                                        ‫کفته اند ‪.‬‬      ‫قلمزن » زن لا زاینده وفقیمه راکونند ‪ ۴‬ومعنی‬
 ‫ستنبه ‏ = بکر اول بروزن شکنبه »‬                        ‫کتیبی ابن لفت استرمالند است چه ستربمعنی‬
  ‫‪ ۴‬هندی باستان ‪ ( 11805-‬یی حاصل ‪ ,‬ا حاصلخیز )‬          ‫‪ - ۱‬رك ‪ :‬شترنگه ‪.‬‬

   ‫ارمتی ‪۲6‬ا‪ , 8‬بوفالی ‪ , 8۳1603‬لاتینی ‪ . 5111۲605‬کتی ‪۵‬تنقاد « اسشق ‪.» ۹۱۷‬بهودی ‪-‬‬
                                             ‫فارمی ‪« 0011۷-۲8153‬هوبشمان ‪ .۹۱۷۲‬رك ‪ :‬استرون ‪.‬‬
          ‫از آن فرزند زادن شسدترون ‪.‬‬                    ‫فرئوت‬       ‫کدشوت‬
                                                                        ‫ک‪۴‬ن‪-‬ون‌شوش بمر‬
   ‫‪ ۶‬منوچهری دامغالی ‪. ۷۵‬‬
   ‫وندبشومان اآرا قابل توجه‌داند « استق‪-‬‬
                                       ‫هدا‬
                                         ‫‪-‬رن این وجه اشتغاق را عامیانه می‬
                                                                        ‫‪ ۴‬ه‬
   ‫رك‪ :‬اتم ‪ .‬بهلوی ‪mhats‬‏‬
                        ‫‪- ۱‬‬                        ‫رك‪ :‬اسقل ‪٥‬‏ امتخی ‪:‬‬      ‫‪6‬‬         ‫هزیشمان‪.> ۹۱۷‬‬
   ‫که >‪»۰۲‬‬  ‫از ایرانی باستان ‪ 2 801×4۸5‬قس اوستا ‪( 27205 :‬فوی) «بارتولمه ‪١۹٥٠٩‬‏ لریب‬
   ‫و هم در پپلوی ‪k2‬‏ ‪ ats‬ر ‪hkamhats‬‏ ر ‪kamxats‬‏ ‪( ,hîkamxats‬جبری ‪ ,‬جور)‪.‬‬
                                   ‫نیز اوستا ‪ » © 801205 -‬فی ‪580٩ [4۲- :‬‏ « اسشق ‪: › ۷۱۷‬‬
          ‫دوستدارش روزسختی دشمن روزا ون ات ‪.‬‬                  ‫پادشاهی کو روا دارد ستم برزبردست‬
   ‫دلتان ‪. ۰ ۷۲‬‬
              ‫ک‬
                                 ‫‪ = ¥‬ستمبه‪.‬رك ‪ :‬استنبه » پارسی با‪۹‬ست‪0‬ان‪-8‬‬
       ‫‪ © 26200۳‬فس ‪ :‬هندی باستان ‪-‬‬
   ‫‪:‬‬    ‫‪ :‬لیبرکه ‪۲۷‬‬     ‫> ورك‬    ‫« اسشق ‪۸۷‬‬     ‫اة (تکر م رمدعها‪ ۰ ).‬ارمنی ع ‪kabmats‬‏‬            ‫هاا‬

                                                                                      ‫‪: stambakîh‬‬
```


## [2026-09-14T02:31:52.554Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"; n=0} {n++; if (index($0,\"استبرق\")>0 || index($0,\"استوار\")>0) print \"LEAF_NR=\"n}' BQT_v1_pages.txt | head -20",
 "description": "Locate estabraq/ostovar in BQT v1"
}
```


### [2026-09-14T02:31:53.979Z] TOOL RESULT

```
LEAF_NR=15
LEAF_NR=27
LEAF_NR=36
LEAF_NR=342
LEAF_NR=367
LEAF_NR=423
LEAF_NR=451
LEAF_NR=498
LEAF_NR=525
LEAF_NR=576
LEAF_NR=587
LEAF_NR=697
LEAF_NR=706
LEAF_NR=731
```


## [2026-09-14T02:31:58.363Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==342' BQT_v1_pages.txt | head -70",
 "description": "BQT v1 leaf 341"
}
```


### [2026-09-14T02:31:59.451Z] TOOL RESULT

```
وت ۱ تیم
استوی بش اول والث بر وزت بر
کوی » مهر پشت را کویند .
استه * ه ختح اول بروزن خسته , دالةٌ.
خرما و شفتالو و زردآ لو ء امثال آبرا کوبند -
واستضوانآ دمی‌وحبوانات. دبگررایز گفتهان -
وضم اول کفل وسرین را کوبند -و بکر اول
وضم تاكث وظهورهای هوز مضفف امتوه است که
ملول وتشکهآمده ومانده شده‌باشد - وبکنراول
وثالث وظهوها بمعنی ستیزه ولجاجت. باشد .
استهیتن- بکر اول وثاكث : بمعنی
لجاجت کزدن ونتیزه نمودن باشد .
استیا - بابای حطی‌بروزن اقترا . نم
کوهیست از کوحپای مىاین هرات وغزنه .
ان پروز نکفگیر: مقداری باشد
ممین وآن ششی درم و نیم اسث .
استیژه - بکس اول » بعنی متیزه
و لجاجت و جنکه و خمومت - و خشم و کین
استیم » بنتع اول بروزن تسلیم. آستین
جلمه را گویند - وبیعتی دهان ظروف و ارانی
هست - و بکسر اول جراحتی را کویند که
ک رکه (۱ ) شده باشد بعنی سرما خورده باشد
ویع‌بی کابوی‌خوانند - ویسمتی دیوهمآمدماست
که درمقابل برست: - ومودم دلیر وصاحب قوت
وقوی‌بازو را نیز کفتهانم.:
استو ار ۱ بم اول بروزن خشکوار
بمعنی محکم و عضبوط باشد - و آمین و متمد
وامادی‌را نیز کوبند - وبمعنی باورهم حست‌چه
استوار داشتن بمعنی باورداشتن است .
استوان ۲ - بن اولو تالث بروزن
پلبلان » بسعنی استوار است که محکم و مضبوط
واهمین ومعتمد باشد.
استو‌ذان؟ - بن اول و ثاك و دا
بالف کشیده و بتون زده » دخمه ومقبرة کبران‌ر!
گوند .
استود ذ بنم اول واكث و سکون‌تالی
و رایع و رای قرشت شت ۰ هر چهار یاه را گوینه
عموماً و اسپ واستر را خصوصاً .
استون - بر وزج کلکون . بسنی
ستون باشد؟
استوه - بکرلول ونم ثالث وسکون
نانی و راب و ها » بمنی مانده شده و افرده,
ویتنگه آمد - وماند گی وبتنگهآوردن- وملول
بلشد ؛ وجضم اول هم درست است.
۹ پهاری 105111025 معتفد وثابت‌فدم «بونکر*4», 8504087 «بوستی. بندهش۹4*.
ی ون . ۴ - بهلوی 2540080 ,
حرزه اول آن نمعتی استخوان است و دان دسو ند مکان است . چون زرششان استخوان مرده را
پی‌از 1: ن.که ک رکس‌ها ولاشه خوران گوشت جد وی را خوردند - او را ح رکودالی می‌اندازند ,
آن کودال را اسنودان کویند و مجاراً یگورستان اطلاق میشود . در تهران رسم مذ کور در میان
زرشتیان منسوخ شده است
۴ - بپلوی50002, اوستا 50002 بارتولمه ۱5۰۸* فارسی‌نيزستون «یبر که 0۹۰۵.
۵ _ رک : هه واستخوان . وکا فنلسته::
۴ - ساسکریت 56216 وهندی366۲ ( چپل بك يك 1120104 هندی ) فارسی استیر
وسیر (چهل بك من) : « هراستیر چپار درم بود چن‌انکه سیمد استیر هزار ودوست ددم بود ۰
(سد درش) « بوروزنامه ۱۰۲ » رکه : لفت‌نامه » وستیر
```


## [2026-09-14T02:32:13.958Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"; n=0} {n++; if (index($0,\"استبرق\")>0) print \"LEAF_NR=\"n}' BQT_v1_pages.txt; echo \"=== استبرک\"; awk 'BEGIN{RS=\"\\f\"; n=0} {n++; if (index($0,\"استبرک\")>0) print \"LEAF_NR=\"n}' BQT_v1_pages.txt",
 "description": "Locate estabraq in BQT v1"
}
```


### [2026-09-14T02:32:15.119Z] TOOL RESULT

```
=== استبرک
```


## [2026-09-14T02:32:20.290Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 336 337 338; do echo \"##### NR=$n\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' BQT_v1_pages.txt | head -50; done",
 "description": "BQT v1 leaves 335-337"
}
```


### [2026-09-14T02:32:21.309Z] TOOL RESULT

```
##### NR=336
اسیندار هف ۱ - بش میم وسکون
ذال نقطه دار. بروزن ومعنی اسفندارمن است که
مام دواژدهم باشد از سال شمسی - و نام روز
پنبم بود از حرماه شمسی ؛ و فارسیان این روز
را درین ماء مبارك شمرند و عید کنند و جشن
سازند بتابر قاعد کلیه که پیش ایشان متداول
است که چون نام ماء بانام روزموافق باشدا لروز
را عد کنند . نيك‌است درین روز جامه پوشیدن
و درخت شاندن - و نام فرشته‌ایست که م و کل
اسبوهن
است که پس رگشتاسب باشد ۴ و آنرا دوبین تن
و
اسینوی ه بکر اول و فتح ناك وضم
داماد افراساب است گویند ببار جییله نوده»
چون تژاو کرشت بیژن او را مصرن شد » و
باضافةٌ کاف بعد از حرف ال که اسیکنوی باشد
هم بنطر آمده است . 4
اسب و فردین نهادن - ی
است بر درختان و بشها و تدبیر امور و مسالحی
که در ماه و روز اسفندار وافع مشود بدو علق
دارد - وزمین‌را نیز گوبند که بعربی‌ارض خوانند.
اسیندان ب‌ مکتر اون بروژن بی‌دندأن»
تخمی امت بیار ربزه و آنرا خردل گوبند ۴ .
اسینف‌یاد - بر وزن و عمنی اسقندیار
اسب و فرزینبطرح دادن وبازی را بردن‌و کنابه
از غالب شدن و زبادنی کردن باشد .
اسب فقی» با تای قرشت بر وزن پهلو
شکن . بلغت زند و پازند ( ۱ ) بمعنی دیدن
ومشاهده کردن باشدد. و بمعنی دوانیدن هم‌بنظر
آمده است ۴ وافهاعلم و
(۱) چك *« ژند ویاژند .
۱ - اوستا ۸۳۳۵ 5۳6008 بهلوی ۳۷۵6 52902۲ , بارسی مپندار مذ »
سفندارهت ۰ اسفندارمث و کاه سَخفف صیند ار واسفنه ۰ باب از دوحزه : میند که صقت است
بمعی با و عقدی ۰ ارمتی با ارمسی 141 همم کب از دو حجزع : 70 قد است سمعنی
درصت » چنانکه باید وشاید و بسح » دوم 1 از در 90 سعنی اندشیدن قافن کتید
ارم ٍِ متی » میم بادغام حذف شده» پی ارمتی بمعنی فروتنی و بردباری و ساز گاری » و سپنته
آرمتی بمعنی بردباری و فروتتی مقدس است . مپندارمذ که نگپبانی دوازدهمین سال و پنجمین
روز ماه بدو سپرده شده » پنجمین امشاسینداست واو نمانده بردباری و شکییابی و سازش اهورا
مزداست و ماتند دیگر امشاسپندان واسطةٌ آفربد گار و آفرید گانست و در جهان خاکی نگهبانی
زمین با اوست . سروای لام بنجمین روز ماه را در فپرست روز های ابرانی « اسفندارمد * و در
فهرست مفدی « سبندارمف. » و در فهرست خوارزمی « اسبندار مجی > آورده ۰ زرتشتیان ایران
۶ سیندارمزد » لوسند . «روز شماری ۲۷۲-۲۱»
۴ افرا ۸۵6۲ دایتی +۰۱5 . ۴ - دریهلوی )5۳2۳0022 اوستا -506700
0 م رکب ار سینته بمشی مقس وجزه دوم ازسدر 42 بمعنی آفربدن ودادن » جمعا .«عنی
مقدی آفریده »با فربدة (خرد) مالك , مزدسنا۳۳۱ ‌. ۳ هز 25160120 وصور ۶
آن, بهلوی 0122 سمعتیدبدن «بونکره٩»؛‏ در اینجا صورت کلمه‌تصحرف شدءسجای تاه اول باء
نوشنه وخوانده اند وممنی اول « دیدن و مشاهده کردن » درست است ومعنی دوم از افزودن واو
به «دیدن؟ (دودن) و عدیهٌ آن ( دوایدن ) برخاسته !
۵ اسیوختی - رك : سپوختن -
##### NR=337
ابجد و ظهور های هوز ؛ مخفف اسباه است که
لشکر و سپاه باشد - و سگه را ليز کوشد که
بتازی کلب خوانند» وبا پای‌فارسی هم گفته‌اندا .
اسبهان » سر وزن و مصنی اصفهان
است, وآن شهری باشد داراللطنه در ملك‌عراق
و با بای فارسی هم آهده است » و آن شهر رادد
قدیم دارالیهود ی گنتندی ء گوشد دجال ازآنسا
خروج کند .و ابتدای قحط عالم از آخجا شود »
وه رکه چهل روز درآن شهرباشد بخیل ومسك
شود - و جمم سیاه یز هست - و چنم‌سگم
کفته اند که بازی کلب خوانند , چه در دتاب
معجم‌البلدان در صحیح نام اصفهان کفته اند نه
«لاصبهان ۴ اس‌مشتق من الجندية و ذلكان‌لنظ
اسبهان اذا رد الی اسمه بالفارسية کان ا-باهان
و هی جمم اسباه و اسباه اسم للجند والخنل ۴
وبشفت‌فیقال‌اسبه ۴ وجمعه‌بالفارسية اسبهان6 .»
۱ رك : اسباه و سیاه
0
است مخصوص ملول طبرستان ۷ - و بنعنی سپه
سالاز هم آهده است که‌سردار و خداوند (ثکر
باشد چه بد بمعنی خداوند و صاحب و اسپه
سیاه ولشکر بود » و نم بای‌ابجد هم گفته اند
و محرب آن اخفییه لست .
آسهید خو ده » بنتح خای قطمدار
و رای بی نقطه و واو معدولهٌ ماکن ۰ اشرافیان
فاری نفی تاطفه را کون دکه ا وت متعنیة
انانی انت ۷ .۵
اسبیچاب » با تتای مجهول و جبم
فارسی‌بر وزن استیعاب , نام شهری است
ماوراء النپر که آنرا بترکی شبران بنر وزن
۱ ۱
آسییل # . تسه کیت که فش
سیاه باشد - و بمعنی بی نقش و بی‌لون هم‌آهده
است . 4۶
آسیید‌دو ۵ « دم رودخانه است اژ
آذربایجان که بدیلمان و گیلان گنرد .
ت ازولات
۴ - ممجم‌البلدان ( این ) : فعلی هذا جمعوا
۰۵ ۱3۲ 9 ۹۸+
رك: سکه شناسی‌طبرستان. اونوالا ۰۳۹-۷۸
‌ اسپیتمان _ راء : سییتمان .
هی کت او :۶ : اسیه (مشفف اسیاه
۲ رت وخره 4 ی رت
##### NR=338
۱ ۷۲۳
ظروف می را سفید کند و اورا قلعی کر وسفید
کر ی زگویند .
اسپیل « بنتح‌اولبروزن‌تصیل » شخصی
را گویند که پیوسته اسب دزدد و سوای اسب
دزدی کار دیگر نکند .
اسپیوش ‏ بائین فرشت ۰ بر وزن
و ممثی اسیغول است که بزر فطونا باشد .
است » بفتح اول و سکون تانی و ای
فرشت ۰ مضفف استر باشد که از دواب مشهوره
است. کوند ازجملة صرفات فرعون است ۱ -
و استخوان آدمی و ساير حیوانات ۴ - و تشم
ودانهٌ میوه‌ها را نیز گویند؟ - و تضیر کتاب زئد
و پاژند (۱) هم‌هست که‌آنرا استا نیز خوانند »
وباین حمثی جنم اول هم آعده است ء واصح ابن
است ۴ - و باول موم سرین و کفل حردم
وانداختن هم آمده است - و بکتی اول بمعنی
ستایش باشد - و امر باستادن هم هست سنی
باست - و حلفةٌ دبر را نیز گویند که سوراخ
کون باشد » و بعضی باين معنی و بمعنی سرین
وکقل عرمی مبدانند ۵ .
استا - بتح اول وسکون ثانی و اك
بالف کشده شیر کتاب زند (۷) است و آن
(۱) چك
۱ - رگ : استر
۴ رك : اوستا
۱ رگ : اوستا..
: ژند ویاژند .
۲ - ره :
تصنیف زردشت است ۱ - ونام‌قلمه ایست‌ازولامت
رستمدار که بسسات تمام اشتهار دارد - و نم
اول مخفف استاد است که آموزاننده باشد ۷ -
و تضیرزند را جضم اول نیز گفته‌اند 4 - وبکس
اول ستااش کناده را کوبند و نم قربه است
از قرای سمرفند ی ی
خوانند .
استاخ - جنم اول » بروزن و حعنی
کستاخ است که بیادب و لجوج باشد - وبکس
اول شاخی که نازه از درخت روییده باشد .
استأث * - جنماولوسکون‌دال, آعوز کار
و آموزانده باشد - و داند صنمتی از امور
کلیه و جزلیه را دز استاد کودند . ۶
استاد باك » بکر اول.نم‌شهریانت
در طبرستان مشهور باسترآباد *۷.
استاده ه بکر اول ممروف است که
متاره و ک و کب باشد- و شامیانه و سایبان راهم
گفته اند - و مسطر فولادی و چوب جدول
کشانرا نیز گوبند - و بمعنی طنبور سه تار هم
هست - و نام بلوکی است از مضافات لاعیجان
0- و نام قلعهای باشد از ملك دکن ۹
```


## [2026-09-14T02:32:46.939Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== PHD stabr\"; grep -n -i \"stabr\\|stawr\\|astōbān\\|astwbʾn\\|ast(y)wbʾn\" PHD.txt PHD_mackenzie.txt | head -20; echo \"== NYB\"; grep -n -i \"stabr\\|stabrih\" NYB_vol2_glossary.txt | head -20",
 "description": "MacKenzie / Nyberg stabr"
}
```


### [2026-09-14T02:32:47.010Z] TOOL RESULT

```
== PHD stabr
PHD.txt:570:Srēš [slw$ | M sros, N surūš] the god Obedience; cal. 17th day. ~ig [-yk'] obedient. srū [slwb' | N suri(n)] horn, nail, prong. srub [s/(w)p | N usrub] lead. ~ën [-yn'] leaden. srüdan, sray- [s/wtn', sPd- | M sry-, № sur~] sing, recite, play (an in- strument). ~i$n(ih): singing, recitation. srüwar [siwbw!] horned. srūwēn [slwbyn'] horny. stabr [stpl | M stbr, N sitabr] big, coarse, strong. 7-ih : coarseness; strength, force. stabrag [stpik! | Ar. istabrag] shot silk. stadan, stán- [YNSBWN-tn' < A ynsbwn, V nsb | M ‘std, *stn-, N sit~] take. staft [stpt! | M ‘stpt] hard, firm; harsh, tyrannous; very. stahm [sthm | N sitam] power, oppression. ~ag [-k'] strong, oppressive. ~(ag)ih: oppression. stambag [sthmbk! (-h- < stahm) | M ‘stmbg, N sitamba] oppressive; obstinate. “АҺ: oppression; obstinacy. stān-, v. stadan. star [sil] = stāraģ. stárag [st?/k! | M ‘st?rg, N sitara] star. stard [st!/t!] stunned, stupefied, confounded. ~ih: stupidity, stupefaction. : star-Ošmār, -6šmur [stProfm?l, 2wfmwl] astrologer. starwan [stlwn' | N sit~] barren, childless. stáyIdan (s? dytn! | M гуд, N sit~] = stüdan. Stéy [styk! | N. sitéy] erect. sténdag [styndk!] standing, erect. stér [styl | N sitēr] stater. Stézag [styck! | M ‘styz-, N sitéza] quarrel, strife. sti [sty(y) = Av. sti-] being, existence. Std [stwh! | (P *stwb, N sutdh)] distressed, defeated. ~wih : distress. stör [stwl | P ‘stwr, N sutór] horse, mount; large cattle. «bān [-p’n' | N -bàn] (head) groom. --ģāh [-g’s] stable. *stēš [stw$] the fourth morning after death. stówénidan, stówén- [stwhyn-yin'] defeat, overcome, Stówih, v. sto. stüdan, stāy- [stwtn', st?d- | M ‘stwd, ‘st?y-~~, N sit—] praise. ~išn: praise. ~išnīg : praiseworthy.
PHD.txt:994:big wuzurg, stabr.
PHD.txt:1261:coarse stabr, sturg.
PHD.txt:1262:coarseness stabrih.
PHD.txt:2000:force must, stabrih; vital ~ axw.
PHD.txt:3654:Silk abrēšom; shot — stabrag; v. damask.
PHD.txt:3849:strong amawand, nérogómand, ēstī- gan, ózómand, pad-nérég, pādyā- wand, saxt, stabr, stahmag, sūr, tagig, zorig, zóromand.
PHD.txt:3870:пёгӧр, 62, saxtih, stabrīh,
PHD.txt:4757:stardsmur starwan stardih stard stabr stabrih stabrag
PHD_mackenzie.txt:4656:stabr [stpl' M <stbr, Nsitabr] big, coarse, strong.
PHD_mackenzie.txt:4658:stabrag [stplh' , Ar. istabraq] shot silk.
PHD_mackenzie.txt:6027: bear (v.) burdan; ,..., offspring zadan,    big wuzurg, stabr.
PHD_mackenzie.txt:6213:coarse stabr, sturg.                     complexion gon(ag).
PHD_mackenzie.txt:6214:coarseness stabrih.                      compose hambastan, hamenidan.
PHD_mackenzie.txt:6628:force must, stabrih; vital- axw.             friend ayar, dost, erman.
PHD_mackenzie.txt:7578:silk abresom; shot -- stabrag; v.             sleep (v.) xuftan, nibastan.
PHD_mackenzie.txt:7695:   piidyiiwandih, saxtih, stabrih,         summer hiimin, tiibestiin j(a.) hiiminig.
PHD_mackenzie.txt:7707:   wand, saxt, stabr, stahmag, sur,        supplication liibag, liibakkarih.
PHD_mackenzie.txt:8847:panag                         \~""tJ         stabrih                 ~O)tUJ
PHD_mackenzie.txt:8848:panzdah                   "'U <; t'" t)      stabrag                  ;~V~
== NYB
```


## [2026-09-14T02:32:48.412Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== HRN\"; grep -n -i \"sitabr\\|stabr\\|ustuvar\\|ustuwar\" HRN.txt | head -20; echo \"== HUB\"; grep -n -i \"sitabr\\|stabr\\|staura\" HUB.txt | head -20",
 "description": "Horn / Hübschmann"
}
```


### [2026-09-14T02:32:48.528Z] TOOL RESULT

```
== HRN
6253:vergl. usttiwär^); arab. LW. istabraq'^^) grober Atlas-
23114:i istabraq 718.
== HUB
6057:(= siped) weiss, zd. spaeta-; istabr = sitabr H. 713;
6116:Konsonant 4- Vokal + Konsonant (z. B. siped. sitabr) in
6398:awra- ; sitabr stark'= zd. stawra-. Ueber asdb *Verwirrung'
```


## [2026-09-14T02:32:58.602Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '6240,6265p' HRN.txt; echo \"=== leaf\"; awk 'NR<=6253{n+=gsub(/\\f/,\"\")} END{print \"leaf:\",n}' HRN.txt",
 "description": "Horn context sitabr"
}
```


### [2026-09-14T02:32:59.669Z] TOOL RESULT

```
46, 285) den Vorzug zu behalten.
*) Hübschmann, Indog. Vocalsystem, S. 31.
') Im Hähname sehr häufig -sitän, z. B. guhitän (I, 161 Vers 594),
KäbuUitän (z. B. I, 157 Vers 506), Zabulsitän (I, 146 Vers 821). Die
Wörterbücher führen längst nicht alle vorkommenden Composita auf;
ich erwähne nur merdumsitänl (Vis und Rämlii, S. 7S Vers 4 v. u.),
sowie jüd.-per.^. JNHDn (^«- ^ 8) "• «^- (Indot,^ Forsch. 11, 140).— 158 —
kuid. istirk; af/. sförai, 8tar[ya fAuge'); oss. stali
(229) ; wa/. stär, si/n. starf^ stirj ^), sar. /turj^ minj.
asiäri, sangl. ustürak.
712. {2)sitäre Tliegennetz, Schirm' (Öähn. I, 102 Vers 746).
Zu [/^star- ausbreiten' (Rückert, ZDMG. 8, 314).
713. sitebr, setehr (AM. 112 Zeile 4), istebr *stark, gewaltig',
vergl. usttiwär^); arab. LW. istabraq'^^) grober Atlas-
stoff'.
aw. stawra- i^stahlira-, "^str^bhra-) *fest*; phlv. stapr
(vd. 18 (65) GL), d. i. stawr; ai. [^stabh- 'feststellen,
stützen etc., stambha- 'Pfosten, Säule (Hübsch-
niann, ZDMG. 39, 93 Note 1).
oss. vergl. sfawd stark*.
714. sifff/r, ista/r 'Wasserbassin* (eigentlich etwas 'fest
sc. Ummauertes*).
Kh«. esseil j ostor ^ üsor^ sa/r (vergl. isfel etc. bei
Vullers).
aw. sta/ra- 'stark, fest'; vergl. den Stadtnamen
Sfa/r^ Ista/r,
=== leaf
leaf: 179
```


## [2026-09-14T02:32:59.739Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '6390,6405p' HUB.txt; echo \"=== leaf\"; awk 'NR<=6398{n+=gsub(/\\f/,\"\")} END{print \"leaf:\",n}' HUB.txt",
 "description": "Hübschmann context"
}
```


### [2026-09-14T02:33:01.011Z] TOOL RESULT

```
geschlagenem a: abrU 'Augenbraue* = skr. bhrU".
In den armenischen LW. erscheint stets anl. b = ap.
np. b, vgl. band *Kerker = np. band u. s. w.
b) Ap. b nach n ^= np. 6: xunb *Krug, zd. xumba-
u. s. w., siehe Kap. 28 (m = nb).
§ 75. Ap. b nach Vokalen, d. h. ap. w ist in einigen
Fallen im Np. zu 6, sonst aber zu v geworden:
a) = np. b in : abr * Wolke' = paz. awar Shk. 233, zd,
awra- ; sitabr stark'= zd. stawra-. Ueber asdb *Verwirrung'
u. s. w. (H. 32) vgl. oben p. 7 (phi. dsdp) und iiber (mar i)
s^ba *Viper (H. 800) oben p. 82 und unten p. 185 (phi. sBpak).
Da ab *Glanz' == skr. abha- H. 3 unsicher ist, so ergiebt
sich, dass ap. w nur vor r sicher zu np. b wird. Doch
vgl. np. girlb ein Getreidemass, arab. jarib, syr. NDn:i
(Tab. 242) = arm. griv = ap. ^grfwa-.
b) = np. V in : n^v Vacker , phi. nevak schon (— np.
=== leaf
leaf: 191
```


## [2026-09-14T02:33:11.781Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== stmb\"; grep -n \"stmb\\|st'np\\|stnp\\|stnb\" SOD_pages.txt | head -30",
 "description": "Gharib Sogdian stmb"
}
```


### [2026-09-14T02:33:11.842Z] TOOL RESULT

```
== stmb
8590:                ospancne ? Ospnyn'k) -^spnyn'y                          1679 'st'np B                  (<r~^)^
8591:                                                                               =>stmb
8592:                (6>/)iron                                                    (o)stamb ©<*stamba; Parth. st}mb; MP 'stmbg
8598:           1667 'spy s- B, S                    j^^o^o^                 1680 'st'npr'k     B                             ^^K^
8604:          1668 >spytc ? S                         (j^y)j/^<^                  (o)stanpore, stambare ? ^st'npyr'k
11990:      BBB; GMS 1068; VJ 11; TSP 3.204 n pl98;                    2898 pw6stnp) S                              j^UjlJl^.*
29686:     staftar, stapdar ©pi. -r* =»stmb                                 C2, 54R28, 68V27
29694:       ~ty =*}stptyy, stmb                                      9006 stw-pnc^ C                                  .l?wj^
29706:8995 stmb M                     (C^Jc^.^^
37053:      GMS 99; TSP 6.108, 2.15; VJ 431; BSTBL, Dhu.                      zof-astambe ? =»zwstmby
37171:11499 zwstmbkyu M                                                           BSTBL, Dhy. 151, 210, 332, 381
37178:11504 zwstmby        M                                                      Schwartz. STSC 134.33 n pl44
37179:      zu-stambe          ©pi. -t ^zwP'st'npy                         11511 zwydm* C                                           jojl^j
```


## [2026-09-14T02:33:17.161Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for L in 8590 29706 29686; do awk -v L=$L 'NR<=L{n+=gsub(/\\f/,\"\")} END{print \"line\",L,\"leaf:\",n}' SOD_pages.txt; done; echo \"=== pdf page tags near\"; sed -n '8570,8600p' SOD_pages.txt; echo \"....\"; sed -n '29690,29730p' SOD_pages.txt",
 "description": "Locate SOD leaves/pages"
}
```


### [2026-09-14T02:33:18.232Z] TOOL RESULT

```
line 8590 leaf: 131
line 29706 leaf: 430
line 29686 leaf: 430
=== pdf page tags near
                                                                              GMS 539 n 2; STi 38.6
                  (a)spaxst ©pt. st. ^'sp'ys-, 'spyst-
                  0o)serve, (to)rcspcct                                 1675 -'st                                    J^\j\ ^Ju^ x^^
                  GMS 520, 884                                               (a)st, (9)st
                                                                             elative suffix
           1661 >spymh B                     (? aJt^JL^i^ji rU)              GMS 1309
                (o)spem ? Ospynmwh, 'spymwh)
                (name of a/z)illness, tumour                            1676 'st'k S                               <£^jy ^^^ iS\x^
                TSP 7.61; -mwK TSP 2.36; Hen. Texts. 715                     astak ©pi. -t

           1662 'spymwh =» 'spymh                                             sapling, stem
                                                                              S W, KG 503 pl80
           1663 >spyn M                                      j^Lij&kf
                ospin Ospynd/t) ©pi. -d-t          =^spyn}wy, spn}k     1677 'st'nd ** >st>nt
                sinful, sinner                                          1678 >st*nk B                                ^jW(^>r^
                 GMS     112; Hen. BSOAS      11, 66; BBB f8; S W, C2        astong ?, (o)stang ?

                   p95.13                                                     (name of tfn)illness
                                                                              TSP 2.35
           1664 'spyn'nk B                                        ^7
                ospancne ? Ospnyn'k) -^spnyn'y                          1679 'st'np B                  (<r~^)^
                                                                               =>stmb
                (6>/)iron                                                    (o)stamb ©<*stamba; Parth. st}mb; MP 'stmbg
                TSP 2.850
                                                                              coarse, rough
           1665 'spynd/t         M => }spyn
           1666 'spynmwh           B =» 'spymh                                BSTBL, Dhy. 169; Benv. Notesiii 227

           1667 'spy s- B, S                    j^^o^o^                 1680 'st'npr'k     B                             ^^K^
                ospcs =^spxs-, 'spyst-, 'sp'ys-, sps-                         (o)stambare
                (to)scrvc, (^)respect                                         violent, cruel
....
                                                                     one hundred and eighty
8993 stpty(y) M                          ^^<jii**                            ^st-2p312.100, 101 (clxxx)
                                                                     Hen. Cosm.
     stapde ©<*stafta-t Parth. MP istaft ©ob. pi.
       ~ty =*}stptyy, stmb                                      9006 stw-pnc^ C                                  .l?wj^
     cruel
                                                                     satu-pancas ^pnc*s
      BBB b85; GMS 157                                               one hundred and fifty
                                                                     C2, 13R27
8994 stq- C                                  $&**
                                                                9007 stwr C, S                                        jy^
     (a)ste ©<*astaka ©nom. -y; pi. stqty ^}stk-
       st}yn}k                                                        stor ©ob. -y; pi. -f; ob. pi. ~ty ^'st'wrh
     bone                                                             sheep, cattle
      STi 55.19; GMS 87, 981; BSTii 84628: C2, 69R 26                 BSTii 849.4, 918.3: C2, 12R4, 11V18; STi 22, 22;
                                                                        CII 1990 E18
8995 stmb M                     (C^Jc^.^^
     stamb ©<Av. stdnbya-, MP istambagih ^Wnp,                  9008 stwrpSyy M                                IJL^ijj*.
       stpty(y)                                                      stor-paSe ^'st'wrpS^c
      stern                                                          animal, cattle
                                                                     BBB 508; Gersh. Advice. 86 n27
      Sogdica. 16.13b pl8; GMS 157
                                                                9009 stwry'ty S               j^f      ^x+Jj^^c+if
8996 -stn                               ju — cU-<J^.
                                                                     storyate ?
     stan ©<*stanaka =»pwSst}n, cynst}n, 5ywstn,                     flesh or skeleton of sheep
       -st>n
      suffix of place                                                 CII 1990 E18
      GMS 1118
                                                                9010 sty' C => >sty]
8997 stpWk     B                              (Ljl*)IJj*        9011 sty2 C                                 4~^j,<4*j%
      satpa5e (stp5}k) =»st-2                                        sate
      millipede, centipede(wz7/i hundred- feet)                      raised (stty) ©pp. =»sn~, st-1
      TSP 6.9; GMS 1316                                              BSTi 113; Hen. JRAS 1945, 135; BSTii 903.10:
8998 stp8>k => stp>8>k                                                 C2, 57R10; styy, 3sg. intrans. pret. GMS 864
8999 stryc M, C                                   j j ,03u           being
                                                                9012 sty*wy  C                                ij^-jcj^a
      (a)stric, strec ©<*strikd\ Av. strl ©pi. -yst                  styawe    =»sty}-y
        =^stryc
      female, woman                                                  Sund. AoFi 1974 p234.6
                                                                                                                                    364
```


## [2026-09-14T02:33:32.871Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==132' SOD_pages.txt | tail -20; echo \"#### leaf131 tail\"; awk 'BEGIN{RS=\"\\f\"} NR==131' SOD_pages.txt | tail -8; echo \"#### leaf132 head\"; awk 'BEGIN{RS=\"\\f\"} NR==132' SOD_pages.txt | head -6",
 "description": "Find SOD printed page numbers near 'st'np"
}
```


### [2026-09-14T02:33:33.971Z] TOOL RESULT

```
                Hen. JRAS 1944, 143.19                                  1683 Wny S                                           c&*<±
          1671 >srt(y) C                                                         xnt, }nt2=>>stny
                                                                             (o)stane
                (a)sart(y) ©a-sarta-, Skt. asirta
                united, together with                       cr=*"r           MDii p38.18
                Sund. AoF 1981, 213; S W, Ham. CII, 1990, 73,
                  G15.4                                                      place
                                                                        1684 'st'nyk B                           j/l^^b^Ji^L
                                                                             astanik
                                                                             messenger
          1672 >st' ** 'st1
          1673 >st' B                                                        VJ 1384; GMS 997A; BSTii 880. 12; Benv. ETii
                                                            >*rs<^
     ■A




;1

#### leaf131 tail
1645 >spt- B                                      fU,-<>lT        1656 >sptyh     M *± 'spt'k
     (o)spat ©in compd.
     complete                                                     1657 'sptyy M =» 'spt'k
     GMS 982, 1192                                                1658 >spwrn(w) B, S                            J? <*
                                                                       (a)spurn ©<*us-prna-, Khot. uspurra-, Pahl.
1646 >Sptw B                        (J^i^jU^                              uspur =»'spwrn, spwrn-, V 'spwrnw
     (o)spat ©<*spata-, Av. safa; Khwar.'jW; Oss.                      full, complete, enough

#### leaf132 head
            'spwrny'kh                                                                                                              66


                  TSP 776; MDii B4R19V1; GMS 99, 151
                                                                              ast  (^styh, >styy) ^'sty3
                                                                              existence
```


## [2026-09-14T02:33:44.967Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==430' SOD_pages.txt | head -12; echo \"... tail\"; awk 'BEGIN{RS=\"\\f\"} NR==430' SOD_pages.txt | tail -6; echo \"=== which NR holds 8995\"; awk 'BEGIN{RS=\"\\f\"} /8995 stmb/{print NR}' SOD_pages.txt",
 "description": "SOD page 363 check"
}
```


### [2026-09-14T02:33:46.053Z] TOOL RESULT

```
                                                                                                                   362
srt

        29-47                                                    BSTii 843.56; S W, C2 p84, 40R10, 68V25, 111V6
8963 srt - B                                    *j+        8974 sry'ws       B                  ^Ja^u* i<j&\ «ojy- ~&*>
          w                                                     saryos
     sart ©<Avsar9ta\ Yaghn. sort ©nom. ob. -y,
                                                                 disturbed
      cold                                                       SCE 318; GMS 551
     GMS 526; TSP 2.420 3, 259, 265; VJ 533, 961;
                        ,                                  8975 srypt}m B                              ^<£j
       SCE 291; Frag. Len. 65.9, *srttw, SCE 386                sarepdam ? (sr'yptta, sryPtm) ©ob. -y
... tail
                                                                (a)stanik
                                                                messenger ^'st'nyk
8973 sry'qyc C                              j^j^J ' j*
     saryakic ©*sry*q+ ic ©pi. -qyst
     head, leader                                               BSTii 880.12: C2, 77V12 n pl56

=== which NR holds 8995
431
```


## [2026-09-14T02:34:01.343Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== FSF setonbeh\"; grep -n \"ستنبه\" FSF_pages.txt | head; echo; echo \"== MON\"; grep -n \"ستنبه\\|ستبر\" MON_part1.txt MON_part2.txt 2>/dev/null | head -10",
 "description": "FSF and MON greps"
}
```


### [2026-09-14T02:34:01.599Z] TOOL RESULT

```
== FSF setonbeh
14835:                        ‫ستنبه (بروزن شکنجه)‬                  ‫زناشوئی زال و رودابه می‌نویسد‪:‬‬
14839:‫گوی پیر و جادو» ستنبه» سترگ‬                          ‫که بنده نباید کهباشد سترگ‬
14842: ‫ستنبه دیو بدخو چه نمودت؟‬

== MON
MON_part2.txt:1276:مفروق. درهم آميخته. (گیا.) استبرق. 
MON_part2.txt:2269:اغلب‌ستبر گردن. 
MON_part2.txt:2457:شدن» ستبر گردیدن. (امص.) ستبری» 
MON_part2.txt:5190:فر وهشته گردیدن. ستبر شدن. غلیظط گفتن. 
MON_part2.txt:5270:ستبر گر دیدن. بر شدن. کت 
MON_part2.txt:5365:ستبر و قوی که در بس در خانه (سرای) 
MON_part2.txt:6634:ستبر گردن و دلیر. 
MON_part2.txt:6740:در فرن پخته باشند» نان گرده ستبر با نانی که 
MON_part2.txt:16820:نتواند؛ بخت» بختک» برخفج) استنبه؛ 
MON_part2.txt:19013:ستبر و کلفت نیز اطلاق می‌نموده‌اند و
```


## [2026-09-14T02:34:03.215Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== KLN staff/Stephen\"; grep -n -i \"Gk. stephein\\|stephanos\\|Stephen\" KLN_1966.txt | head -10; echo \"== SKT staff\"; grep -n -i \"^staff\\|staff (1)\\|STAFF,\" SKT.txt | head",
 "description": "Klein/Skeat greps"
}
```


### [2026-09-14T02:34:03.340Z] TOOL RESULT

```
== KLN staff/Stephen
2511:A  hybrid  coined  fr.  Greek  d-  (see  priv.  pref.  a-) and  moral,  a  word  of  Latin  origin;  first  used  by Robert  Louis  Balfour  Stephenson  (1850-94). Derivatives:  amoral-ism,  n.,  amoral-ity,  n. amorist,  n.,  a  practicer  of  gallantry,  lover.  — Formed  fr.  L.  amor,  ‘love’  (see  amorous),  with suff.  -ist.
10371:Dasypus,  n.,  a  genus  of  armadillos  (zool.)  — ModL.,  fr.  Gk.  Sacju7rou?,  ‘a  hare’,  lit.  ‘the hairy-footed  animal’,  fr.  dasy-  and  rot)?,  gen. no8o?,  ‘foot’.  See  dasy-  and  -pod. Dasystephana,  n.,  a  genus  of  plants  of  the  gentian family  (bot.)  —  ModL.,  compounded  of  dasy- and  Gk.  axccpavoi;,  ‘crown’.  See  Stephanos, dasyure,  n.,  any  of  small  marsupial  mammals  of Australia.  —  Compounded  of  dasy-  and  Gk. oup£,  ‘tail’.  See  uro-,  ‘tail-’, data,  n.  —  PI.  of  datum  (q.v.) date,  n.,  a  given  point  of  time.  —  ME.,  fr.  OF. (=  F.)  date,  fr.  ML.  data  (scil.  littera)  (whence also  It.,  Proven?.,  Sp.  data),  lit.  ‘(letter)  given’, prop.  fem.  pp.  of  L.  dare,  ‘to  give’.  This  term derived  fr.  L.  datum  (neut.  pp.  of  dare),  the  first word  used  in  letters  to  indicate  the  place  and time  of  writing  as  e.g.  datum  Romae  pridie Kalendas  Maids,  ‘given  (i.e.  written)  at  Rome on  the  last  day  of  April’.  L.  dare  is  rel.  to  dos, ‘marriage  portion,  dowry’,  do-num,  ‘gift’,  dond, donare,  ‘to  give  as  a  present’,  fr.  I.-E.  base  *dd-, *d1-,  ‘to  give’,  whence  also  OI.  da-da-ti,  ‘gives’, Avestic  dadaiti,  of  s.m.,  OI.  da-tar-,  da-tar-, ‘giver’,  da-tram,  ‘gift’,  Gk.  8i-Bco-pi,  ‘I  give’, Sd)-T(0p,  Sco-xrjp,  So-xrjp,  ‘giver’,  8£>-pov,  Sto- t(vt),  8<o;,  ‘gift’,  S6-m;,  ‘a  giving;  gift’,  Bo-xo; (verbal  adj.  of  Si-Sto-ptt),  ‘given’,  OSlav.  dati,  ‘to give’,  da-ru,  ‘gift’,  da-ni,  ‘tax’,  da  mi,  ‘I  shall  give’, Lith.  duomi,  ‘I  give’,  OPruss.  dost,  ‘gives’,  Arm. ta-m,  ‘I  give’,  tu-r,  ‘gift’,  Alb.  Sa-sc,  ‘I  gave’. Cp.  add,  addendum,  anecdote,  antedate,  anti¬ dote,  apodosis,  condone,  dado,  dation,  dative, die,  ‘cube’,  donation  and  words  there  referred to,  dose,  dosimeter,  dosology,  dot,  ‘marriage portion’,  dower,  dowry,  edit,  irredenta,  post¬ date,  reddendum,  reddition,  render,  rendition, sacerdotal,  subdititious,  surrender,  tradition, traitor,  treason.  Cp.  also  mandate,  command, commend,  countermand,  demand.  Cp.  also  the second  element  in  vend.
17062:Halesia,  n.,  a  genus  of  plants  of  the  storax  family (bot.)  —  ModL.,  named  after  the  English physiologist  Stephen  Hales  (1677-1761).  For the  ending  see  suff.  -ia.
27797:peckhamite,  n.,  an  iron  magnesium  silicate  ( mine¬ ral'., )  —  Named  after  the  American  chemist Stephen  F.  Peckham  (1839-1916).  For  the  end¬ ing  see  subst.  suff.  -ite.
36729:step-,  combining  form  denoting  relation  through remarriage.  —  ME.  step-,  fr.  OE.  steop-,  rel.  to OFris.  stiap-,  ON.  stjup-  (cp.  ON.  stjiipr, ‘stepson’),  Swed.  styv-,  MLG.  stef-,  Du.  stief-, OHG.  stiof-,  MHG.,  G.  stief-,  ‘step-’,  ON. stjiipr,  ‘stepson’,  OE.  astiepan,  bestiepan,  ‘to  de¬ prive’,  OHG.  arstiufen,  bistiufen,  ‘to  deprive  of parents  or  of  children’.  For  sense  development cp.  L .privignus,  ‘stepson’,  which  is  rel.  to  privus, ‘deprived’  (see  deprive). stephan-,  form  of  stephano-  before  a  vowel. Stephana,  fern.  PN.  —  ModL.,  fern,  of  L.  Ste¬ phanas.  See  Stephen.
36731:stephanion,  n.,  the  point  where  the  sutura  coro- nalis  crosses  the  temporal  ridge  ( craniol .)  — ModL.,  fr.  Gk.  crxcq) xvtov,  dimin.  of  ax£( potvoc;, ‘crown’,  ‘that  which  encircles,  crown,  wreath’, which  is  rel.  to  oxEtpavv),  ‘that  which  encircles; diadem’,  used  also  as  a  medical  term  to  denote the  sutura  coronalis.  For  this  use  of  crxeipavifj see  Aretaeus  Medicus,  ed,  K.  Hude,  Corpus Medicorum  Graecorum,  II,  Xpovicov  voocov HEparceimxov,  I,  2.  See  prec.  word, stephanite,  n.,  a  black  mineral.  —  G.  Stephanit, named  after  Archduke  Stephan,  mining  director of  Austria  (died  in  1867).  The  ending  -it  goes back  to  Gk.  -  txr;? ;  see  subst.  suff.  -ite. stephano-,  before  a  vowel  stephan-,  combining form  denoting  crown.  —  Gk.  0x890010-,  fr. atitpaMoq,  ‘that  which  encircles ;  crown ;  wreath’, fr.  crxEcpEtv,  ‘to  encircle;  to  crown;  to  wreathe’, See  stemma  and  cp.  Stephana,  stephane,  ste¬ phanion,  Stephanos,  Stephanotis,  Stephen  and  the second  element  in  Dasystephana.
36732:Stephanos,  n.,  a  kind  of  headdress  (Gk.  antiq.)  — Gk.  atiipotvoq,  ‘crown’.  See  stephano-. Stephanotis,  n.,  a  genus  of  plants  of  the  milkweed family  ( bot .)  —  ModL.,  fr.  Gk.  ateipxvtotiq (fern.),  ‘fit  for  a  crown’,  fr.  ax£9avouv,  ‘to crown’,  fr.  oxcoavoc,  ‘crown’.  See  stephano-. Stephen,  masc.  PN.  —  L.  Stephanus,  fr.  Gk.  Sxe- 9avo;,  lit.  ‘crown’.  See  stephano-  and  cp.  Ste¬ phana.
== SKT staff
2012:Boat.  (E.)  M.  E.  boot.  A.  S.  bat.  + Icel.  b<Ur\  Swcd.  bAt\  Dn.  bcof\  Kuss. bof  ;  W.  boii;  Gael.  b4ta,  a  boat.  fl.  The orig.  boat  was  prob.  a  bat,  i.e.  slick,  branch, Stem  of  a  tree:  cf.  Gael,  and  Irish  ^M. staff,  stick,  pole,  branch,  bat.     Sec  Bat.
5197:Distaff".  (E.I  A  di>tftff  is  a  staf bedizfntd  with  flux,  fttdy  to  be  spun  off. '  I  dysyn  .1  dystafft,  I  put  the  fiaxe  upon  it to  spvnne;  Palsgrave.  M.  E.  distaf. dysestaf.  A.S.  distaf.  The  A.S.  distaf stands  for  disi-sfttf.  where  sfaf=  E.  staff, and  dist  *  ■>  Low  G.  diesse,  the  bunch  of flax  OD  a  distafT.     See  Diiea.
18281:fee  of  a  cask,  part  of  a  piece (£.)  Merely  another  form  of to  M,  E.  dat  sin^.  ttaue  (s/avt) ttatici  yttavts)^  Cf.  Iccl.  ita/r^  a itavc;  Dan.  sf\w,  staff,  stavt^  stave. (I),  t;\ink  of  a  tree.  \Vs.)  M.  E. VS.  sU/n,  itt/n,  sttmH,  (i)  stem se,  {i)  &teii>  or  prow  of  a  vc&scl ; sit  iMfnti,  ittfna.  Fornicd,  with ,floni  A,S,  ttaf,  a  ^taff,  prop;  a being  the  iitai^  or  support  of of  a  nuel  being  the  upright It  of  it  -f  Du.  skim,    trunk,
18470:to  tfecr  with;  f>t*n/,  board,  border,  edge  or tide ;  sec  Board,  The  O,  H.  G.  siium means  a  prop,  staff,  paddle,  rodder,  allied to  Icel.  staurTf  a  post,  stake,  Gk.  irravptSr, an  upright  pole  or  stadte.  {^SV\},  allied to  Vi*^A.)+  DU'  stNurhccrd,  Icel.  itj6m' ^rSi,  Dan.  Swcd.  styr^rj;  all  oimilatly compounded.
18537:Stick  (i),  a  staff,  twig;  svc  Stick  (i).
18540:Stiff.  ^E  )  M.  E,  stif.  A.  S.  ////  stiff. +  Du.  slijf,  Dan.  sfitf,  Swcd.  sty/.  Allied to  Lith.  stipruj,  strong,  Uip-ti.  to  be  stiff, L.  stipes,  a  stem  ;  also  to  E.  Staff,
18735:StufT,  materials.  (F.-L.)  O.  F.  atofe. *  stufTe ; '  Cot.  —  L.  stupa,  stuppm,  the  coarse part  of  flax,  hards,  tow;  the  pronunciation of  this  L.  word  being  Gennanised  before  it passed  into  French  (Dies).  Cf.  G.  staff, slufT,  materials.  %  The  sense  of  the  L. word  is  better  preserved  in  the  verb  to stuff,  i,  e.  to  cram,  to  stop  up,  <.'».  ttcp/en, to  fill,  stuff,  quilt,  from  Low  L.  stuppatt, to  stop  up ;  wDcnce  also  £.  Stop,  q.  v.
19884:i^taff,  later  tipstaff,  an  officer  with  a
```


## [2026-09-14T02:34:14.646Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '14825,14850p' FSF_pages.txt; echo \"=== leaf\"; awk 'NR<=14835{n+=gsub(/\\f/,\"\")} END{print \"leaf:\",n}' FSF_pages.txt; grep -n \"page_offset\" /dev/null; python3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'));print(d['FSF'].get('page_offset'))\"",
 "description": "FSF setonbeh entry + page"
}
```


### [2026-09-14T02:34:15.771Z] TOOL RESULT

```
 ‫وگرگاه یابی نگردی سترگ‬                                     ‫نخستین به پیش تو آید دو گرگ‬
‫(‪)۴-۸۶۷۱‬‬                                             ‫نر و ماده هریک چو پیلی سترگ‬
                                    ‫ستمگاره‬         ‫(‪۶-۰۷۱-۷۶‬ع)‬
‫از ستم ‪+‬گاره [=گارء پسوند مفید معنی‬                                         ‫(اسدی ‪)۳۰۱-۱۴‬‬

                      ‫ر‬            ‫ا‬                    ‫بگشتتند باهم دگورد سترگ‬
        ‫کنون ای گرامی» کتایون کجاست‬                 ‫گن‌شسته چو ارغنده گرگ‬
                                                                        ‫بچهنحو‬
‫مسراتگمرگاره خواند رواست‬                                       ‫‪۲-‬گستاخ» رسکش نافرمان‪:‬‬
‫(‪۶-۸۴-۰۴‬ع‪)6‬‬                                         ‫سام در نامۀ خود به منوچهر دربارة‬
                        ‫ستنبه (بروزن شکنجه)‬                  ‫زناشوئی زال و رودابه می‌نویسد‪:‬‬
                        ‫زشت‌رو بدقیافه‪:‬‬                    ‫یکی آرزو دارد اندر نهان‬
                     ‫(دقیقی ‪:)۶-۳۷-۶۲۱‬‬               ‫بیاید [زال] بخواهد ز شاه جهان‬
           ‫یکی نام او بیدرفش بزرگ‬                           ‫نکردیم بی رای شاه بزرگ‬
‫گوی پیر و جادو» ستنبه» سترگ‬                          ‫که بنده نباید کهباشد سترگ‬
                        ‫(ویس ‪:)۲۱۴-۸۳‬‬                ‫(‪)۱-۵۰۲-۲۶۰۱‬‬
       ‫گرفتش دایه و گفتش چه بودت؟‬                                  ‫‪-۳‬تندخو خشمناک‪ ,‬لجوج‪:‬‬
 ‫ستنبه دیو بدخو چه نمودت؟‬
                                           ‫‪۳۹۹‬‬                                      ‫ستودان‬



                                                                                   ‫ستودان‬
                   ‫جنگ پیکار نبرد‪:‬‬               ‫از اوستایی ‪ 2652‬فبارسی استه‪ .‬هسته‪.‬‬

        ‫ز پیلان جنگی ندارد گریز‬                  ‫استخوان (یادداشت‌های گات‌ها ‪ )۶‬د‪+‬ان‪:‬‬
=== leaf
leaf: 298
484 leaves; edition/printing of this scan not identified — determine offset from printed page numbers on the page text/image when checking
```


## [2026-09-14T02:34:35.983Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"استبرق\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt 2>/dev/null | head -10; echo \"=== استوار footnote\"; grep -n \"استوار\" MON_part1.txt | head -10",
 "description": "Mo'in greps"
}
```


### [2026-09-14T02:34:36.072Z] TOOL RESULT

```
incoming/MON/MON_2vol_Adena_v1_djvu.txt:11396:استبرق: رجرطاهای هر ِ- استبرکث| ۰( 
MON_part1.txt:11396:استبرق: رجرطاهای هر ِ- استبرکث| ۰( 
MON_part2.txt:1276:مفروق. درهم آميخته. (گیا.) استبرق. 
MON_part2.txt:51440:رسد. (گیا.) استبرق. (فز.) معبر جریان برق. 
=== استوار footnote
2162:استوار و معین ناب دوم. ۳ ۳ ۲ ..عسم.) 
2426:استوار کنند تا پرندگان بر روی آن نشینند. 
4781:آمن: 20( [ع.] (ص‌تفض..) استوار تر» 
5416:استوار کردن چنانکه تن رابر ستور و مانند 
5592:محکم کردن؛ استوار کردن. براق کردن (بر 
6162:اپرام: 2022 [ع. ۰[ (مص م ۰) استوار کردن» 
6901:کردنء استوار کردن کار. (امص.) استواری» 
7058:استوار داشته, معتمدان. . " 
7748:احتصان: صرومهاده [ع.] (مسص‌ل.) استوار 
7749:بودن» محکم بودن. (امسص.) استواری»
```


## [2026-09-14T02:34:40.889Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '11390,11402p' MON_part1.txt; echo \"=== استوار entry\"; grep -n \"^استوار\\|استوار:\" MON_part1.txt | head -5",
 "description": "Mo'in estabraq context"
}
```


### [2026-09-14T02:34:41.029Z] TOOL RESULT

```
را؛ عوض چیزی. 

استبراء: 8 [ع. ف. استبرا] (مص‌م.) 
طلب یی برائت دسه خواستن» 
با کی خواستن 

استبرق: رجرطاهای هر ِ- استبرکث| ۰( 
دیبای ستبر» استب رکث. (کیا.) نام دو و نه 
درختچه از تيرةٌ کتوس‌ها که در هند و مالزی 
و در جنوب ایران در نقاط گر مسیر و 
سواحل دریای عمان و خلیج فارس 
می‌رویند و از گیاهان کاچو ؟ ثی ابران هستند. 
استخر. 
=== استوار entry
2162:استوار و معین ناب دوم. ۳ ۳ ۲ ..عسم.) 
2426:استوار کنند تا پرندگان بر روی آن نشینند. 
5416:استوار کردن چنانکه تن رابر ستور و مانند 
7058:استوار داشته, معتمدان. . " 
8094:استواری.
```


## [2026-09-14T02:34:47.216Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"ستبر\\|ستنبه\\|استوار\" incoming/ARY/ARY_pages.txt | head -15; echo \"=== latin index\"; grep -n -i \"STEBH\\|STEB(H)\\|SETABR\\|OSTOVAR\" incoming/ARY/ARY_latin_index_pages.txt | head -10",
 "description": "Aryanpur greps"
}
```


### [2026-09-14T02:34:47.285Z] TOOL RESULT

```
378:دیدمان‌ها بر پایه‌ی قراین و احتمالات استوارند و بس.
940:ایزدسازی عوامل طبیعی (ماه و خورشید و توفان و غیره) استوار بود. مثلاً واژه‌ی «شاه» در شش زبان
953:رسید که اساس فرهنگك و جامعه‌ی هند و اروپایی بر سه انديشه استوار است: ۱-روحانی و یزدانی ۲-
1001:و عموها)» وایل (مرکب از چند خانواده‌ی گسترده و یک سرور) استوار بود. پدر در رس خانواده و
10227:۶ | ستبر» استبر
10290:۸ | ستنبه» ستمبه (به چم *مرد درشت و قوی و دلیر")
10296:فارسی ((۳28814): استنبه, ستمبه (به چم آمرد درشت و قوی و دلیر) 5
10303:بازگشت به: ستبر
=== latin index
```


## [2026-09-14T02:34:48.949Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== IEC Mann\"; grep -n \"stembh\\|stebh\\|stembos\\|stebos\" IEC.txt | head -15; echo \"== SYN Buck\"; grep -n -i \"stebh\\|stambha\" SYN.txt | head -10",
 "description": "Mann and Buck"
}
```


### [2026-09-14T02:34:49.040Z] TOOL RESULT

```
== IEC Mann
17187:stembh- (stembhəlos, stembhros) ‘hard; hardness, firmness, stay, support’. WP II, 624 Skt. stambh- radical: ‘support’; Av. stomb-, id.; Arm. cf. tmbi, s. ‘limetree’; Gk. cf. a- stemphés, adj. *'unshakable'; stémphula, npl. ‘oilcake’; Li. stembas, stembras, m. *haulm'; stembstu, stembti, v. ‘harden off; Latv. cf. stiebrs, m. *haulm, rush’
17591:sthembh- “fix, harden' Per. (ambig.) sitam, s. ‘oppression’. Cf. sthem-, stemb-); Gk. cf. the cpd. a-stembhés, adj. *un- shakable, stubborn; MHG stimmen, v. (2) “fix, determine”; cf. G be-stimmen, id.; OLi. stembiü, stembti, v. ‘resist’; Li. stembstu, "ti, intr. ‘harden, wither’. (A possible *sthen- guho- wd. link Gk. w. Latvian stengs “firm,
== SYN Buck
34165:Av. stamba- (Barth. 1606, IF 11.139), cf. NPers. sitamba ‘violent, quarrelsome’ : Skt. stambha- ‘inflation, arrogance’, lit. ‘post, pillar, support’. Cf. Horn 718.
```


## [2026-09-14T02:34:56.185Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '10215,10310p' incoming/ARY/ARY_pages.txt",
 "description": "Aryanpur setabr/setonbeh entries"
}
```


### [2026-09-14T02:34:56.255Z] TOOL RESULT

```
ْ سانسکریت (84//807): -87071 574109 برهان قاطع + ۹۸
زو
بادداشت: ۹ ۰
۱ بازگشت به؛ ستودن,
هه ۱
ا
: 3
افغانی (پشتو) (//۸۳0/۸): ۸ فرانسه کهن ([۳۲2۸0 010): دنه ۷
تخاری ۸ (۸ (۸ل70221۸): 07 ایتالیایی (۸۸لل77): دش دب
سانسکریت (8۵(9۳7): 57۸181۸8 ابسلندی کهن (/524(0/0۸7/14 0ا0):
ِ پونانی (07628): 595 ,57038 ,57۸ 87118
[pdf page 345]
۶ | ستبر» استبر
ساکسونی کهن ((54200 070): 50 ۸8 ,8717
فریزی کهن ((۲۸/54 ا0): 8706 لنرنی (لني) (7714(7): 5
آلمانی کهن (/688/4 04[ (01): ایرلندی کهن (5/7لااالما0): 8۸3
1 و
41 870 خی ما
آلمانی ۰:84 57066 ,5706 پسگشت‌ها و دورو ۵9 ۵
انگلیمی کهن 8۱0870 ط۵1): نا
0 ,5700 0 ۰87000 وی ات ان
انگلیسی (0ل6/08): ادن 3 (501038) :مانم 05
دانمارکی (0۸184): 0 1 (8700) :0108 ۱
سرئدی (8178015): 57۸ 5 (8706) +57
: نروژی (07077801407): ه6الا57۸ برهان قاطع + ۱۳۴2۷
هلندی (077627): وین لفت‌نامه دهخدا : ۲۱۰۵۸
لیتوانی (1۸071۸0ط7/): فرهنگ معین : ۳۱
بادداشت:
۱ به احتمال زیاد واژه‌های فارس "ساق" و "ساقه" هم از همین واجریشه‌اند .
۳ چم این واژه در زبان سانسکریت: فشار آوردن؛ فشردن» (ضربه) زدن,
چم این واژه در زبان ایتالیایی؛ شمشیر,
چم این واژه در زبان یونانی: چوبدستی» خصاء
۳ هشدار: خویشی واژه‌های ایرانی اين فهرست با واجریشه‌ی هند و اروپایی و دیگر واژه‌های این فهرست مورد
تأئید همه‌ی خبرگان نبست به ویژه برای اینکه شکل اوستایی و پهلوی آن هم در دست نمي‌باشد.
اوستایی (/4۷570): سانسکریت (84/5277): +57۸8
۸ ,87۸۲0۸ بونانی 0780): 05
پارسی باستان (/۲۴۶۹1۸ 010): گنیک (0077770)+ ند
امد ان اپسلندی کهن (/701۸3/14(مک5 صته):
پهلوی (تشاتل۸): ۸ 87۸78
۰ 57۸78 ب#ا87۸ آلمانی کهن (08724۸07 ۲/04 صا0):
اوستی (0858712): ررر نان لزان
کردی (078215): دادن آلمانی (/08704۸): زان
هه
[pdf page 346]
۹
سترون» استرون / ۳۴۷
ِ :
انگلیسی کهن (بلولا52(0 ۵ا0: 57۸7 پسگشت‌ها ۸/5
ٍ انگلیسی (لوآلا6۸/0): ان 2 ت۶0
د دانمارکی (0۸715/7): 7 ,57۸8 6 (87۸7۲) +8۸0/7
سوئدی (8(۷5075/1): ین :۸213
نروژی (/0۷07008014: 5۸ 4 (873036) ,104 610
هلندی ((0176): 57۸0 61 (87۸77) :0/10
روسی (894(7تا): ان دون 57
لیتوانی ((۸(/۵ت7(4/)): ,7 ,595 (87۸77)
5 ,87۸1815 9 (ت57581
لنونی (لتی) (/4774ل): نراد ادن 8 13160 تنم
| برهان قاطع + 1.۹۸
یادداشت:
ِ چم اين واژه در زبان‌های ژرمنی: چوبدستی.
پهردی - فارسی تایه ایک انگلیسی کهن (#اکناه/80 ۰:0۵ 571886
سانسکریت (5۸/5۳77): 57۸85 انگلیسی (تل5ل6۸/0)(از فرانشه) 8788312
ارمنی (4/۵45149۷): زد ان بلفاری ((متماناق): 8رد ان
بونانی (6523): 57818۸ ,57۸88717۸ آلبانی ‏ (/(۸۸۷1۸قله): درون
لاتین (710۷با): 578315
ا فرائسه (/۳88/6): - ند اد دنم پسگشت‌ها 5
ٍ اسپانیایی (5۶۸(/1524): نا 1
[ اه ایبایای (ملم: 8 ون 6 ات78 2/7
پرتغانی (۳:077618892 3818811 5 ای نامام
گرتیک (007[716): ید ان 8 (۲3ت975) :0/705
ایسلندی کهن (/0104/1۸2/(ی50 صا0): 2 (878۴-۲۵) یا
871871۸ برهان قاطع : ۰
آلمانی کهن (057214(0 0[7اتز صزه): لفت‌نامه دهخدا : ۶ رو ۲۸۴۸
زد دی فرهنگ معین + ۳۳
[pdf page 347]
۸ | ستنبه» ستمبه (به چم *مرد درشت و قوی و دلیر")
یادداشت:
۱ فقدان واژه‌های همریشه در زبان‌های اوستایی و پهلوی و دیگر زبان‌های ایرانی وابستگی "سترون" يا واجریشه‌ی
هند و اروپایی 8781۰ را نامسجّل می‌کند و بهمین دلیل در جلو واجریشه‌ی مندارلاییای (شاید) آورده‌ام.
به احتمال زباد واژه‌های "استر" (به چم "قاط" که جانوری" مقطوع اللسل است) و سترون" (به چم" پا کر د(وارييي.
تراشیدن نیز از همین واجریشه‌اند. ً
فارسی ((۳28814): استنبه, ستمبه (به چم آمرد درشت و قوی و دلیر) 5
اوستایی (/4837۸2): 338۸1۸ آرمنی (4ل842(14): 87۸/8۸
پارسی باستان (۳881۸(۷ صا0): :
87۸3/8۸3۸ پسگشت‌ها ایشا دی
سانسکریت (54(5877): سا
57۸305۸ ,فت57۸/8[1 برهان قاطع + ۱۱۰-۱
یادداشت: 1
بازگشت به: ستبر
اوستایی (/488740): پونانی (0۴۵80): ۰ 5781171 ,878177۸
,57۸077 ,51۸03 87۸ ۱
پهلری (/۶۸۶۲): 57218۸3 ,857۳080۸3 پسگشت‌ها لاه هراد نان دی
اوستی (0355716): 87۸177 ,8770 ,5700 ۳۲ ۱
افغانی (پشتر) (/4۳0۸۸): نت82۸ 27 :قاط
سانسکریت (8۸۸8/7): 8 (58ت۳۴۸) تم ها
71 57۷۸7 دلا57۸ +87 برهان قاطع + 1۱۰۱
```


## [2026-09-14T02:34:56.890Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '34150,34175p' SYN.txt",
 "description": "Buck context"
}
```


### [2026-09-14T02:34:56.965Z] TOOL RESULT

```
(razdiratt ‘tear to pieces’). Berneker 214 f.
SCr. kavga, fr. Turk. (cf. NG xaByas, above, 1).
Boh. hadka hddati ‘guess’, refi.
‘quarrel’, ChSl. gadati ‘guess, think’, etc., with semantic development through ‘dispute’. Berneker 288 f.
Boh. svdr = Ch&l. svarii ‘battle, fight’ (late also svara ‘quarrel’), with vb. svariti ‘scold’ : ON svgr (sb.), svara (vb.) ‘an- swer, OE and-swaru, etc. ‘answer’, Goth. swaran, etc. ‘swear’. Walde-P. 2.527. Meillet, tudes 239.
Pol. sprzeczka, cpd. of przeczka ‘con- tradiction’ : przek(o) ‘crosswise’. Briick- ner 445.
Pol. kiétnia : ktécié ‘stir, shake, dis- turb’, refl. ‘quarrel’, ChSI. klatiti ‘move, shake, shove’, etc. Berneker 550. Briickner 237.
Russ. ssora, etym. dub. (: Boh. svdr, etc. above?). Walde-P. 2.527.
7. Skt. kalaha-, etym. dub.; perh. with kali- ‘discord, strife’ : Arm. éelk‘em ‘split’, ChSl. koljq, klati ‘prick, split’, etc. Walde-P. 2.591.
Skt. vivdda-, fr. vi-vad- ‘contradict, dispute, quarrel’, cpd. of vad- ‘speak’ (cf. ChSI. stivada, above, 6).
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Skt. dvandva-, lit. ‘pair, couple’ (: dud, etc. ‘two’), hence ‘pair of opposites’, ‘strife, etc.’.
Ay. mrvi-, etym. dub. Barth. 1197.
Digitized by Arya Samaj Foundation Chennai and eGangotri
SOCIAL RELATIONS 1363
Av. stamba- (Barth. 1606, IF 11.139), cf. NPers. sitamba ‘violent, quarrelsome’ : Skt. stambha- ‘inflation, arrogance’, lit. ‘post, pillar, support’. Cf. Horn 718.
19.63 PLOT, CONSPIRACY
Grk. ouvwpocia Goth. ‘ Lith. samokslas, suokalbis NG cuvwpocta ON samblastr, samsvar- Lett. sazvérestiba Lat. coniuralio, conspira- ning ChSls. - 266
uid Dan. sammensvergelse SCr.  urota It. congiura, cospiracione Sw. sammansvarjning Boh.  spiknutt Fr. complot, conspiration OE gecwidr@den, gecwis Pol. spisek, spikniente Sp. conjuracién, conspi- ME _ coniuracion, con- Russ. zagovor
racién spiracioun Skt.  kapataprabandha- Rum. complot, conspira- NE plot, conspiracy
{iune Du. samenzwering Ir. comlugae, cocur OHG = eidswartt NIr.  cealg, coimhchealg, MHG _beswerunge
cogar NHG .verschwérung
W. cydfwriad Br. trienn, kavailh
Words for ‘conspiracy’ are most com- monly connected with those for ‘swear’ or ‘oath’, especially ‘swear together’, whence ‘form a pact or confederacy by oath’ and in a bad sense ‘conspire against’. There is much semantic bor- rowing, especially in the case of the Gmc. group. Others are from ‘breathe to- gether’ (here also both formal and se- mantic borrowing), ‘talk together’, ‘de- ceit’?, with some isolated and partly doubtful sources.
1. From words for ‘swear’ (21.24) or ‘oath’ (21.25). Grk. cuvwpyoota (: cvvdp- vor); Lat. coniaratio (: coniirare), with the Romance words It. congiura, Fr. conjuration (> ME conjuracion), Sp. conjuracién; Ir. comlugae (lit. ‘joint oath’, gl. coniwratione Ml. 44b5); ON samsvarning, Dan. sammensvergelse, Sw. sammansvdrjning, Du. samenzwering, OHG eidswartt (lit. ‘oath-swearing’, gl. coniuratio), MHG beswerunge, NHG ver- Schwérung; Lett. sazvérestiba (: sazvéréties ‘conspire’, cpd. refl. of 2vérét, fr. MLG sweren); SCr. urota (: ChSl. rota ‘oath’).
CC-O0. In Public Domain. Gurukul Kangri Collection, Haridwar
```


## [2026-09-14T02:35:07.107Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"1606\" BRT.txt | head -10",
 "description": "Find BRT col 1606"
}
```


### [2026-09-14T02:35:07.206Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T02:35:09.207Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '26575,26640p' BRT.txt",
 "description": "BRT after stawra"
}
```


### [2026-09-14T02:35:09.276Z] TOOL RESULT

```
uxsyeiti  stavanS'^  a%a  (sd.)'  nS  yS  dim staoiti  .  .  Y.  /o.  6 ;  —  yäha  mä  (näml. haotmni)  aparaät  saofyantB  slavqn^'*  Y, g.2;  —  fravasayö  ..  avat  avS  zixSnS- nhimna  (sd.)  ks  «J  stavSp''  kü  yasäite  ks ufyät  Yt. /j.49f.;5.  8;  —  asäunqm  ..fra- vasayS  staomi  sbayemi  ufyemi  Y.  77. 18; —  yS  ahm  staoiti  (s.  i.)  hS  mqm  staoiti yim  akurtm  H. /.  3;  3*;  —  *yavatä  %wa tnazdä  *slaoml*^  u/ya(sd.)cä  'V.43-8;  — at  fravaxsyS  vjspanam  mazishm  (sd.) s'tavas  aiä  yS  kudä  (sd.)ysi  &'«/r(NSni.)5> Y.45.6;  —  aj  vi  yazäi  slavas^  mazäa akuri  hadä  (sd.)  a/ä  Y,  jo.  4;  —  täis  va yasnäis  paitl  stavas^''  ayeni  mazda  asä "mit  diesen  Gebeten  euch  preisend  will ich  wieder  vor  euch  treten,  o  M.  und Äsa"  Y.jo.  9;  —  ycCkä  vi  yaz^mnas/a urväidyä  (sd.)  stavas^''  ayenX  paitl  Y. 34.6.  2)  Tenn.  techn.  fdr  das  Beten des  Asageht\s'''>:  yö  ahm  staoiti  hS..  "wer
das  Asa  betet,  der  .  ."  H,  /,  3;  —  staomi ahm  . .  näismt  dalvS  Y.  11. 1 9  und  12.  i ; Vr.  24.3;  —  us>hiitata  mc^yäka  staota (aP.)  aism  yat  vahiltfm  nista  *dafva  V. lÄiö";  —  zara%tdtrahe . .  yö  paoiryö  . . Staat  ahm  näist  daltiS  /raor?nata  masda- yasnS  .  .  Yt  13.  89;  —  %ara%uHrö  yS paoiryB  . .  staota  (3S.)  ahm  yaj  vakisl^m Vl  17.  18.  a)  mit  Dat  coram.(?);  yam
ö.l  nä/rar)uhar)ta  haurvatbya  am»r3talbya asim  staoiti  H.  1.  7.  3)   'etwas  (Akk.)
geloben';  nimaaha  asäi  uzdätä  (näml. zao'kra'i) paitT  avat  stuyi{\%.y^  tüSil  ahmät *ä  *syänlm(sd.)..x/tä  "..gelobe  ich  das: .." Y./2.3,
mit  aoi  dnwS.,  mit  Inf.  staomaine:  aoi mqm  staomaine  stäibi  ya%a  mä  aparaai saoiyanis  stavqn  (s.  SimpL)  Y.p,  2,
mit  apa  'sich  abgeloben,  etwas  ab- schwören'; a)  mit  Akk.:  apa.stavanuka^ .  .  dainqm  mätdayasnim  Y.ig.6;  —  nsi^ ki  {als  Akk.)  apastavUne  .  .  damqm  . . V.  ig.l-  b)    mit    haca  und   AbL:  yS
hala  dainaySt  mäzdayasnsit  *apastv3ii^ N.4I-
mit  3  i)  dnwS.  i:  vankraynis  kinttm *ästaoiti*'>  Adhra  ana  gäiwya  vaca  Y. if».  igj  —  S  tl  (statt  Akk.)  aitihe  Jraca stuyi^''  Y.1.21.  2)  Med.  'sich  ange- loben an  — ,  sich  einschwören  auf—'  (Akk.): yat  tipar»hacat  .  .  vlstäspgm  .  .  yat  imqm dafnqm  ästaota  (38.)  Yt.  ig.  84;  —  aitäHt (nänJ.  Syaöisnd)  asbyB  *spänAaUi  ästa- vanaiibyS  dalnqm  . .  V.J.  40;  —  astuyl'-^ dainqm  mSsdayasnlm  Y.  12. 9;  —  yezi anhal  ästüts  vä  aiwijravanS  (sd.)  v3 damqm  mäidayasnXm  V.3. 40;  —  <lstuys'> humat>m  manö  ästuyi  hUxt»m  vacö  ästuyl hvarltim  syao%anim  Y.  72, 8'>.  a)  'sich dem  Glauben  angeloben',  absol.:  masda- yasnS  .  .  fravaräng  (sd.)  ästatas^S  fra- varstascä  Y.  12.  8;  —  *spayeiti  .  .  dama matdayasnis  nars  ästavanahe  bandim V.J.  41.
mit  upa  1)  dnwS.  i:  vXspe  haoma tipa.staomi  Y.  JO.  17;  2';  —  ydhra  bäha upa.staoiti  haomake  .  .  ü^nm  dasvan baisas»m  Y, /o.  7;  VytJ9;  —  s.  noch PFP.  2)  dnwS.  2:  yai  nä  ..  Sri/  ahm upa.stuyüt  V,  iH.  43;  —  satgm  asö.stüitinqm upastvBis^  Y.  ig.  32.
mit  US  'sich  feierlich  lossagen  von  -, abschwören',    mit   Abi.:    us  güi/  stuyi''>
dby  Google
'595
stav-  Schluss
'Star-  Noten
1596
tayaaüä   hazafihaüa  us   mazäayasnanqm  \ vTsqm  tyanayal{%Ä.)cä  vivapaila  Y.  12.  i.     ' xaitfrä  1)  dowS.i ;  a  ff  (statt  Akk.)  atriAe , /ra^a  stuyl'1  Y.  r.  21.  2)  'etwas  (Akk,)  j
zu  Jemands  (Dat.)  Preis  anheben': /rJ  */?| *staemaide"'^  .  .  *var3hüi  yasnasca  *vaA-' masca  N.  48.  3)  'sich  angeloben  an  -,  \ sich  feierlich  verpflichten  auf—'  (Akk.  oder Dat.):  yam  bä  nä  .  .  alim  slaoiti  fra- stavanB  humataca  hüxtaSa  hvarstaia  H. ;.  7;  —  frasluyi'-^  huinatöibyasca  hüxtöi- byasca  .  .  Y.li.  17'".
u.  iläumi,  stuvanli,  stola  (iP.\  iluM,  t/ävönai, slaläli;  rap.  ästai/äti"\  sutüdan. —  PB.;  stäyi- tän,  (fia)  iläyila,  (lu  V.  J.  40 f.):  äs/avän;  s. noch  No.  7.  —  ■)  D.  i.  Huf,  %  i6S.  12,  19.  — »)  S  »qp-  3.-3)  Them.  —  «  NA.  i/äBmi; s.  Var.  —  S)  Ar.  'sidpal-  geg.  ai.  siitväni--, S  i-*2  d.  p.  —  6)  Vgl-  PüErl.  lU  ahräkih  sLlyil H.  /.  7 !  an  i  ahm  vohü  ei  gmetl ;  ferner  Y. ir,  19,  wo  hinler  siasmi  ai>m  das  Eingebet  | folgt  Gdn.  hat  das  bei  Eeinei  Übersetzung  I von  V,  iS.  16  {SPreoEsAW.  ig.  424)  nicht beiücksicbtigt;  doch  s.  zu  \.i8.^i.  —  7}  S. No.  6.  Pü.  eil.:  iasän  ahräiih  släyil  a}än\ *äevän  luiäiit  iatrni/.  —  8)  Pt  4 1  NA.  'ir.  — 9)  Mit  Ssluyc  wird  später  das  Kunjstück  Y. 13.  8  bis  13.  8  beieichnet;  %.  No.  11.  —  | "*)  So  T  und  FrW.  7.  3.  Ausg.  'maidi,  auch  1 in  der  Wiederholung.  Aber  das  Suffii  maidi kommt  »on«  im  jAw.  nicht  vor.  —  "1  Mit' frastuye  bezeichnet  man  später  das  y'iu«iTatück  1 Y,  //.  17  bis  13.  7j  s.  No.  9.  —  ")  S.  daiu  | Hbm.  AGr.  7.  161.
•  g.  stavat-  Adj.,  PPA.:  s.  stav-  mit No.  5-
•  j.  stavana-  Adj.,  PPM.:  s.  stav-  mit No.  2.
KompE.
•  j,  stavak-  n.  'Dicke,  Stärke'. KompE.  —  Vgl.  slüta:  —  Pü.:  tahik.
•  j.  'Star-  V.  'stemere'.  Pracs.  i  star-^ 10  sttrtnu-,  1 1  slmnä- :  st>rm-  \,  1 1  +  ^5 sürvnaaa],  27  (Pass.)  'strya-.  —  PPfP. star^a-'^,  st^nta-;  PFP.  'statrya-;  Inf. *'st)rmti.         [S.  noch  "/rastaraityB^
i)  'auseinander  breiten,  spreiten,  durch Spreiten  zurecht  machen':  yahmya  stari- tasca  gätus  anyäsca  bjnxhä  avanlä  Yl 17.  7;  —  ya'ka  nä  fryö  fryäi  vantaee startta  gätus  sayamanS  (ad.)  püinm  .  . avi  ava.baraiti  V.^.  35.  a)  als  Term, techn.  für  das  Spreiten  des  Barisman (s.  Sp.  948'*),  d.  i.  dessen  Zurechtmachen, Bereiten  durch  vorschrifismässiges  An-  und Aufeinanderlegen  der  einzelnen  Stengel {urvarS-,  Sp.  402  m.,    403  u.):    ti   (näml.
fravaSayS)  ..staritalsu  bansmdhu  saoyi Yt.  /^-  2  7 ;  —  gaota  . .  p^nnimia  bansma (sd.)  staränS  darrj»m^a  yasn»m  yazJnS Yt.  70. 138; — /rac'arätH  (sd.)  aiva  tnazda- yasna  barismatt  * sl>r>n»nti*^  N.  103;  — bansma  stinnaSa (OpL)^  V.  12. 2'*;  —  ima slar)tai^  (nämL  bansma)  tma  myasda (näml.  avaioayamahi)  Vi.  11.  3;  —  Aap/a /lanti  fiävaiia  bar?sma  "stsrmaHli  N. /02(?)s'.  a)  mit  Dat  comm.:  bansma
/a  shr»nay?n^^  airyä  äaiiihävö  pasäm  hl pacayin  Yl  8.  58.  2)  'niederwerfen,  zu
Boden  strecken':  s.  -stfr^ta-.  a)  Pass. 'erliegen',  mit  Dat.  des  wem?:  druxs  hl stintö"''  apa.dvarai  baUi  dali-S  'V.ig.2;
—  yimS . .  d!ul.manaAyai{sA.)ca  hS  sUntS nidarat  upairt  zqm  Yt.  iff.  34.
mit  ava  und  J  'zu  Boden  strecken'": 3aJ  ha  druxs  avästryeite  kamiit  vä  vaca- tfhqm  V.^,  13;  —  spmiayä  ärmatsU  dsi- ^r3bya  avästryala  mairyS  YL  /,  29.
mit  US  'atisstrccken':  >^»(  bä  na  :^a/h3oa ustryamnS*^  avanuhabdfmnS  (sd.)  a^?m staoiti  H.  7. 11.
mit  nl  'htnbreiien':  s.  rtistantö.:
mit  yrJ  dnwS.  I  a:  sraoüm  ..yS paairyB bansma  frastmnata  j*  Y.  5  7, 6 ;  —  yS bansmqn  *ft'ast»rmte'*''  (3S.)  haomqsca var^Ss{si.)ca  N.97;  *6o',  *soi';  —  ya'ha aitahe  (näml.  öansmanB)  fras^rmäiii aia  .  .  N.  70;  —yH  anu  ailqm  (Sp.  34  u.) bansma  ^frastirmie^''  ya^a  .  .  jäm3spS *frast3rmaita  (Praet)"'>  N.  8g;  —  %risum bansma  /rast»r>nuyä  Vt.  /2, 3 ;  —  imal bansma  hähajaohnm  haha.aiwyaahan»m asaya  frastar>t3m  Y.  2.  i;  4.\,  62.^, 7/.  23,  Vr.(/.2.  V.J.  15,  Ä14,  15.  Vytsj;
—  bansmana  asaya  fi-astarilahe  Vr. 10.  2;  —  frastirstat  paiti  barssrrun  V, 9.56,  A.4.5,  YL/o.  137,  7j.a,  Y.57.2;  — bansmanqmca  aÜaya  */rastfr»tanqm"^ Vr.  12. 3;  —  yö  urvarqm  (sd.)  [.  ,]  *Jra- stfnnte^^  ü.gS;  gS;  —  haxattnm  fra- stirftanqm  (näml.  urvaranqm)  bansmaine frastairyät  "tausend  spreitbare  (PSanzen- stengel)    soll    er    zum    B.    spreiten"    V.
ai.  stj-nAü,  sljTiiti,  släratc,  'slfiak;  np,  gMsiar- dan.  —  Pü.;  viilarlax,  vistarcnilan;  s.  noch No.  1-7,  12.  —  ')  In  der  Wunelülbe  dem ai.  slirnäh  entsprechend.  —  ')  Hds.  itirmti, Vä.:  vislarincnd.  —  i>  Them.  —  *)  PO.:  bandft 'er  bindet';  die  Pü.  zu  V.  /:;  ist  gana  jung.  — ,      i)    Pü.:   x'istanitiiA;     ta   N.  loa:    ka^t   hinä
dby  Google
»597
'star-
ku  fa    Aävan
raShä     iarim     viitarilnTA.    —
7)   Pa.   (fürs   Pass.};    aiSr
iilan.  —  8)  Pö. !  HJ  n  p  dm  iirüA.  —  9)  St««
*/raslitinle  (ar,  *pra-sfinlai)  erscheint  in  den
N,-Hds.  •slpriHli  N.  /O  I.St,    sonst  •slariiUi;
s.  No.  lo.  —    ■")  HAi. /tasiarm:  —    '•)  So
K  7  tt,  b.  —  ")  Fü.:  lOoo  pa  fräe  vislarünlh
barsm  /räf  e  vislarel.     Ich  nehme  das  PPfP.
im  Sinn  des  PFP.   Anders  Gdn.  SPreussAW.
ig.  130.
•  j.,  p.  *star-  V,  'süDdigen'.    Praes,  4  b
(Kaus.)  Ji3ra-'\   10  si^nnav-,  20  *starav-
(p.)'*,    27    starya-,    'strya-,    30    (Kaus.)
stäraya-.   —  AbsoL  **slarayantlm,  'shr»-\
t>m.  I
'silndigeo,   sich   versündigen':    ll/fläim'
tyäm  rSstam  ma  avarada"  (sd.)  ma  "slara-
va''  (zS.)''  Ti.6.6.  a)  mit  star>m  als.
Akk.  des  Inhalts:  *it3rmmiti  ana  *avavai
star»n  (sd.)  .  •  ya^a  .  .  P.  2$.
mit  ä  'sündigen,  sich  versündigen,  in den  Zustand  der  Sündigkeit  geraten;  sündig sein,  sich  im  Zustand  der  Süodigkeit  be- finden', Akt  und  Med.;  i)  absolut:  vlsatti (sd.)  ainyS  "usyS  null  ainyS  ^vlsimnö *äsiryäte  ava  ^vJsalte  (sd.)  *na^a.cil ästryeite  (in  pass.  Sinn  'non  pcccatur') P,57;  —  ya%a  .  .  äai^y^t  a^a  äsfryati "als  ob  er  ,  ,  so  versündigt  er  sich"  V. y.  zo;  —  aetavalla  aesasctt  *ästryäli^^ "und  in  solchem  Mass  macht  auch  er sich  sündig"  N. /2(?);  —  yalöil  (sd)  .  . asrävays  hyat  a^a  .  .  ästryaÜ  ",  .  bleibt er  im  Zustand  der  Sündigkeit"  N.  44',  — *ntsriti  (sd.)  aitahe  ästryeiti  mit  *'anisrili N.  II.  a)  Kaus.  'sündig  machen,  in den  Zustand  der  Sündigkeit  versetzen':; tiöit  asavarum  ainisHs  (sd.)  ästärayeiti\ P.12;  —  nsit  *asavan»m  *a/n)j?('/ (sd.)  1 ättäraiti  N,  log;  —  nStt  sp.bint5 ..  nasus nar?m  ndil  *äslärayaii  V.  5.  3 ;  "•'Nik.  2 ;  — AiaJ  aUai^qm  lyaoi^nanqm  (als  Subj.) astaraiti  "in  welchem  Mass  macht  solches Tun  sündig?"  V.  13.  20;  4.  5;  —  aha  tai "ä/rimnS  astärayäti  N.  12  (P);  —  mä äa/a  . .  *asläraila  Vyt_37(?).  2)  mit a)  Abi.  oder  Gen.  dessen,  an  dem,  b)  Instr, oder  Akk.  (des  Inhalts)  dessen,  womit man  sich  versündigt:  mit  ästryeiti  anyS^ ahmst  yS  kl  ''gaväsiryavans  N.  18;  —  nsil astqm  .  .  pairi.spaiti  (sd.)  apqm  ästrySnte V.  o,  2  9 ;  —  nasujpaSm  (sd.)  . .  astryante . . apasla  zimasca  urvarayasca  V.  6'.  3 ;  — fiBtl  gähanq/n  asruiti  ästryäti  N._50;  — yai  . .  anaiwiSfi  (sd.)  ästryäti  N.  i4\  ^4,
3star-  1 598
'3\  *^5<  ^5>  '8,  22;  —  rUli^  . .  anaiwiitlm ästryanti  N.  4;  —  yai  sS  *nisritim  frära (Sp.  185m.)  *ä  hl  *anisritlm  {staryäti) yeti . .  nSit  . .  frära  mii  *amsrrtlm  astryäte  . . *ahra  *a^ way aisAf m (sd.)  ..*ä  Ai*anisritlm staryäti  N.  10;  —  nsit  anaiwySsti  astrmti''^ N.p5;  —  ä  anaiwyasti strmti^  ^•95>  9^i —  :^araya  (sd.)  .  .  bäzujataya  .  .  yät^m ästryäti  N.  ^2^';  —  yattm  aslryäe  "er begeht  die  Z-Sünde"  F.^f.  a)  Kaus. *il  sl  ditn  aitalsqm  *bao6s.jaitii  astaraiti'''' "es  belastet  ihn  ihnen  gegenüber  die SUnde  ß."  N.  67.  3)  mit  Dat  incomm. : yaica  ,.  Aaine  ..  gar}7V}m  iri<yäii  ptfr>byö [Sp.  906  f,)  ästryäti  V.  15.  i  a.
mit  para  und  ä  Kaus.  'J^^i^nd  (Akk.) einer  Sünde  (Instr.)  schuldig  machen': nabanaadiltitn  hl  para  ^pascaita  *raisaca *atwadäityaea  ''astaraiti''''  "seinen  nächsten Verwandten  macht  er  alsdann  der  Sünden R.  und  A.  schuldig"  N.5.
mp.  vg!.  äilSr  'Sünde';    s.  noch  Pü.  —   Pü.:
dieErl.!  THnäsiä'r  6i/an*),  bi.*fl/-/oif.  — 'o  Vgl. zu  lap-  No.  l.  —  »)  Them.  NA  hat  das  gani unglaubwürdige  siaiava^  (ZDMG.  43.  530).  — J)  Hds.  äitärayeili.  —  4)  Statt  •rinti  >=  'rysnti geschr. ;  i.hindav- 1\0.  i.  —  i)  Die  Konstruktion wechselt  zwischen  LS.  (statt  15.)  und  AS.  — ^)  Das  Praev.  ä  ist  doppelt  geseilt.  —  7)  Hds. äslräinli,  PQ.:  ästatinend.  S.  jSL  BtHL.  IF. /a.  118.  l&ipara  richtig?  Pü.  lässt  es  aus.  — 8)  Auch  als  Übersetiung  (N.  jo).
•  j.,  g.  ^star-  m.  'Stern':  tainm  (sd.) httraihya  . .  yat . .  aiwits  urvisntti  staras- (NP.)'V'ä  mäsca  kvartla  Yt.  J2.  25;  V. '  2.  40;  —  slrfus{A2.)ca  mänhfmca  hvarna raocä  yazamaide  G.^.  6;  Y.  2.  11,  yi.<), Vtio.  145,  *V.  7.  52  (äs  Nom.)'>;  —  kuka . . yaosda'iäni . . ku%a  *strSus'* . . mänh>m . . hvart  V.  11.  \;  1  (als  Nom.),  10  (statt Abi.);  ~  kasnä  :^'Sng  *s/rfm(,GP.)äca  däl adväfam  (sd.)  Y.  44-  3 ;  —  ankam  (näml. fravasinqm)  raya  . .  hvan  . .  mh  . .  stärS ava  pdka  yänti  Yt.  i_j.  16;  FrBy.;  — fra- va^ayB  .  .  yä  strqm  mStthS  kür5  anayra- nqm  rao^anhqm  pa%S  dalsay»n~^\..i3.$T; V.l.  16;  —  Ääu  ma..  ave  stärö  V.9.41; Yt.  Ä  i;  —  tistrJm  ..yim  ratBm  ..vlspaisqm stärqm  Yt.  S.  44;  —  nittmalit  avaüqm stärqm  ya'ka  nars  malmyehe  va-^'hangm "selbst  die  kleinsten  jener  Sterne  (sind  so gross)  wie  der  Kopf  eines  mittelgrossen Manns"  'S. 4^;  —  ha(a  avaibyü  st>r^yS Ytj.  85;  —  slärqmia  sptntB.mainya'vanqm
dby  Google
```


## [2026-09-14T02:35:27.331Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"silamba\\|sitamba\\|stamba\\|slamba\" BRT.txt | head -10; echo \"== cols 1605-1607\"; grep -n \"^>1605\\|1605\\b\" BRT.txt | head",
 "description": "BRT stamba search"
}
```


### [2026-09-14T02:35:27.427Z] TOOL RESULT

```
11802:PQ.:  fehlt;  Npü.:  an  samisiän  silambaiar  dar an  iahr  i  Hä,  —  ')  VgL  anairyäca  Jaiiilius.- aiwistära  V.  1.   17.
== cols 1605-1607
```


## [2026-09-14T02:35:46.985Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== PHD astōbān/astwar\"; grep -n -i \"ēstōw\\|estow\\|astōb\\|ʾstwb\\|stwb\\|ustuwar\\|ustwar\" PHD.txt PHD_mackenzie.txt | head -20; echo \"== NYB astob\"; grep -n -i \"astōb\\|astub\\|stwb\\|stubar\\|stuban\" NYB_vol2_glossary.txt | head -20",
 "description": "MacKenzie/Nyberg astōbār"
}
```


### [2026-09-14T02:35:47.083Z] TOOL RESULT

```
== PHD astōbān/astwar
PHD.txt:195:~ih: destruction. ānāstag [Mrstā!] = ānāst. an-āstawān [”1-”stwb*n', -’stwp’n'] disbelieving.
PHD.txt:219:āsn [?sn'], ~ xrad: innate wisdom. ásnidag [snytk'] = āsnūdaģ. asnüd(ag) [^snwt(k)'] cleansed, purified; pure, noble. a-sohisn [Pswhšn') unfeeling. Я asp [SW.SY A < A swsy’; sb | N ~] horse; (chess) knight. Ha 5Р7 aspánür [sp nwl] tomb. a-spās [’sp’s] ungrateful. aspast ["spst! | N ~] clover, lucerne. NM aspinj [^spnc | P “рулу, N sipanj] hospitality; inn. ШУ "Sy Me asprés [?splys | N ~] race-course. asré Pslwk! = Av. Gbrawa] priest. ~th : priestly office. Asré-kerpa [slzv(k)!klpk = Av. ādrē kahrp-] the form of fire. asrón Pslwn! = Av. āfrawan-) priest. last [AY T! < A?yty | M °st, N <] is, exists. ~ih : existence. *ast(ag) [*st(k)! | M ’st(g), N hasta] bone; (fruit) stone. astānaģ [s??nk!] need, misfortune. ~Smand [-wmnd] needy. āstār [s] | M ?sbr] sin. āstārēnīdan, āstārēn- (^s? ]yn-ytn!] cause to sin. āstawān [*stwb'n', ?stwp^n! | M ”stw?n] confessing, professing. ~th: confession, belief. astódàn [?stw(k)d’n' | M ?stwd^?n] sepulchre, ossuary. astómand [?st?zomnd] corporeal, material. ~th: corporeality. astux4n [sth(w)’n' | N ustux"án] bone. astwand ['stwnd | — M] — astómand. Astwihād [?stwyd’t'] the demon of death. āsūdan, āsāy- [*swtn!, ^? d- | N ~} rest, repose. —išn: rest, peace.
PHD.txt:223:āwēnišnīg : blameworthy. a-wēnišnīģ Pzwynšnyk'] invisible. awérag [”wylk!] = awērān. awērān Pwyln', ?5yPn! | N wērān] desolate, ruined. awestad ['zos??t! | M *zxoyst?d, N ēstād] master (craftsman). awestām [*wst?m | M ?wyst?m] province, district. awestarag [”wstlk! | N ustura] razor. awestardan, awestar- [*xvst/-tn! | P °wystr-, N suturdan] wipe; shave. mišn : wiping. awestwār Pwstwb’l | M ?wystw?r, N ustuwār] firm, reliable. “Аһ: reliability, firmness. awēšān [OLE?n, у. бу | М юу п, N ēšān] they, those. a-wināh Pwrs] innocent. a-winast [”wnst'] unharmed, immaculate. awiš [wbš | M ?wys] to him, it; postposition (= ©) to. awištāb Puwst*5 | M ’wyst?b, N šitāb] oppression. P awištādan, awišt- ['zoft2tn! | P ?wyst!dn] stand. awištāftan, awištāb- ['wi?j-tm | M ?wyšt?b-, N sitāftan, šitāb-] oppress; hasten (tr.). tāwištan, tāwāš- [HTYMWN-tn! < A Мут, V htm; ?wbstn' | M *wyšt] seal. a-wiyabanig Pwyd?f?nyk! | N biyābānī] astr. fixed (star). a-wizirignig Pweylinyk'] unavoidable, inevitable. āwurdan, awar- [YHYTYWN-in' < A hyty, У № | M wrd, "wr-, N ~] bring. āxēzīdan [>лусуѓп!] = āxistan. āxistan, āxēz- Phstn', ?hyc- | М *xyst, ?xyz-] rise, stand up. Axrámidan, āxrām- >А?т-уѓп! | M ?xr’m-, N xiram-idan] stride, strut. axtar [Atl | M *xtr, N ~] star, constellation, sign of the zodiac. axtar(ā)mār [Phil(?)m’/] astrologer. ~th: astrology. laxw Dell being, existence, world. ?axw Phw! | M *xvx] mind, will; vital force. *axw Phu'] lord. a-xwamn [’hwmn'] sleepless. axwān Phw’n'] = захм. a-xwārīh ['Aw'iyh] unhappiness. āxwarr [hwi | N àxur] manger, stable. --Sālār [-srd?I] head groom. a-xwaš [D BS YM] unpleasant; unhappy. ~ih: unhappiness. a-xwēškār [kwyšk'I] undutiful. ay Dy | N —J that is to say. āy-, у. amadan. ayāb [уор | М ik, N уд] or. ayāb- v. ayāftan.
PHD.txt:252:bāmdād [6’md’t' | М bmd?d, N ~] dawn, morning. bāmīģ [P myk!] brilliant, glorious. -bān [-??s! | M Aa, N ~] suffix, -keeper, -guard. band [bnd | = Р, N ~] bond, link. band-, v. bastan. bandag [bndk! | P bndg, N ~a] servant. bang [bng | N ~] henbane. bānūg [Pnwk! | N Бапи) lady. bar [b] | N ~] fruit, produce, profit. bar-, —išn, v. burdan. ībār [Pl | N ~] time, occasion. *bār [P1 | N ~] bank, shore. заг [D] | M P?r, N ~] fruit. ‘bar [b] | M br, N ~] load, burden; duty. bāraģ [5/А! | N ~a] mount, horse. barbut [blbwt! | N ~] lyre. bārestān [b/st?n'] patient, resigned. ~ih: patience, resignation. barig/k [b’lyk' | N bārīk (cf. tārīg)) thin, fine, subtle. bar-jamag [bly mk! | N ~a] saddle-bag. barómand [b wmnd | N ~] fruitful, prolific. barsom [blswm | M brswm] the bunch of twigs used in the Yasna cere- mony. baršnūm [b/s2wm] the major purification ritual. bastan, band- [ASLWN-tn! < A Vier bstn', bnd- | M bstn, (bn-), P bnd-, N ~] tie, bind. bāstān [b’st?n' | M PysPn, N ~] always, often. bas [YHWWNS | M P, N ~] be! (imperative of büdan, q.v.) baSkué [bskwe] gryphon. bašn [bén' | = P] top, peak; stature; mane (v. buš). baw-, —i$n, v. büdan. baxš-, —išn, v. baxtan. baxt [b()At! | N ~] fortune, fate. baxtan, baxš- [HLKWN-tn! < А У hig; bC)htn', bhf- | M bxt, bx$-, N baxsidan] apportion, distribute. ~išn: bestowal, distribution. bay [ORHY A < A */h; bk', bg | M by] god, lord. im ~: his Majesty. бу ~: his late Majesty. bayaspān [by’sp’n'] messenger, envoy.
PHD.txt:310:das [d’s | N ~] sickle. dàs?r [d’sl = Av. dātra-) gift, reward. dast [Y DE < A yd-h; dst! | = M, N ~] hand. dastag [dstk! | N —a] bunch, bundle, group. dast(a)gird [Y DE., dst-krt! | M dstygyrd, N dastgird] estate. dast- gir [dst OH DWN, (v. griftan) | N ~] 1. helper; 2. captive. dast-graw [dstglwb!] captivity. dast-kàrih [ҮЛЕ ГУА | N ~7] handiwork. dast-šūy [dstšwd] = ģūmēz. dastwar [dstwbl | М dstwr, N dastür] authority, priest, minister. ~th: custom; authority. dastyar [dstyd?l | (P dstd’r), N ~] helper. ~th: help, assistance. dašn [dšn! | = M] right hand. dāšn [d”$n' | M d’s(y)n] gift. dašnaģ [dsnk' | N ~a] 1. right hand; 2. dagger. dašt [dst! | = M, N —] plain, open ground. daštān [dft?n! | N ~] menstruation; menstruous. „estān [-st?n'] secluded place for menstruous women. -—--màh [-m?h] menstrual cycle. -ūmand [-’wmnd] menstruous. dāštan, dar- [YHSNN-tn! < А V ben: d^ftn', Pl- | M d'An, ar-, N ~] have, hold, keep, preserve. pad . . . dāštan: hold by, to; take for. pad éd dāštan [cf. N pindāštan] consider. --išn: preservation, maintenance. dāštār [4° #1 keeper, preserver. daw-, v. dawidan, dawistan. idawāl [dwb’l | N ~] leather, skin. ždawāl [dwbl | N ~] deceit, trickery. idawīdan, daw- [LH TWN-tn! < A Vrht; dwytn', dwb- | M dw-, N ~] run. *dawidan, daw- [dw-ytn'] speak (daevic). 1, 2 dawistan [LH TWN-stn!, dwstn'] = 1 * dawidan. daxmag [dhmk' | P dxmg, N ~a] tomb, dakhma (a building where corpses are exposed for destruction). „estān [-si?n!] cemetery. dax$ag [dhšk! | M dxsg] mark, sign, characteristic; memory. pad ~ dàštan : remember. az — hištan: forget. ~6mand [-’wmnd] marked. Day [ddw' | M dyy, N ~] Creator; cal. roth month; 8th, 15th, 23rd days. dayag [d^yk! | M d?yg-, N ~aj (wet-)nurse. „ānīh [nyh] | (N dāyagī)] nursing, nurture. dazidan, daz- [dc-ytn'] burn, scorch. --išn : burning.
PHD.txt:570:Srēš [slw$ | M sros, N surūš] the god Obedience; cal. 17th day. ~ig [-yk'] obedient. srū [slwb' | N suri(n)] horn, nail, prong. srub [s/(w)p | N usrub] lead. ~ën [-yn'] leaden. srüdan, sray- [s/wtn', sPd- | M sry-, № sur~] sing, recite, play (an in- strument). ~i$n(ih): singing, recitation. srüwar [siwbw!] horned. srūwēn [slwbyn'] horny. stabr [stpl | M stbr, N sitabr] big, coarse, strong. 7-ih : coarseness; strength, force. stabrag [stpik! | Ar. istabrag] shot silk. stadan, stán- [YNSBWN-tn' < A ynsbwn, V nsb | M ‘std, *stn-, N sit~] take. staft [stpt! | M ‘stpt] hard, firm; harsh, tyrannous; very. stahm [sthm | N sitam] power, oppression. ~ag [-k'] strong, oppressive. ~(ag)ih: oppression. stambag [sthmbk! (-h- < stahm) | M ‘stmbg, N sitamba] oppressive; obstinate. “АҺ: oppression; obstinacy. stān-, v. stadan. star [sil] = stāraģ. stárag [st?/k! | M ‘st?rg, N sitara] star. stard [st!/t!] stunned, stupefied, confounded. ~ih: stupidity, stupefaction. : star-Ošmār, -6šmur [stProfm?l, 2wfmwl] astrologer. starwan [stlwn' | N sit~] barren, childless. stáyIdan (s? dytn! | M гуд, N sit~] = stüdan. Stéy [styk! | N. sitéy] erect. sténdag [styndk!] standing, erect. stér [styl | N sitēr] stater. Stézag [styck! | M ‘styz-, N sitéza] quarrel, strife. sti [sty(y) = Av. sti-] being, existence. Std [stwh! | (P *stwb, N sutdh)] distressed, defeated. ~wih : distress. stör [stwl | P ‘stwr, N sutór] horse, mount; large cattle. «bān [-p’n' | N -bàn] (head) groom. --ģāh [-g’s] stable. *stēš [stw$] the fourth morning after death. stówénidan, stówén- [stwhyn-yin'] defeat, overcome, Stówih, v. sto. stüdan, stāy- [stwtn', st?d- | M ‘stwd, ‘st?y-~~, N sit—] praise. ~išn: praise. ~išnīg : praiseworthy.
PHD.txt:987:bestowal baxšišn.
PHD_mackenzie.txt:1067:an-astawln ['n-'stwb'n ' , -'stwp'n l ] disbelieving.
PHD_mackenzie.txt:1245:Istawln ['stwb'n l , )stwp'n l I M ))stw'n] confessing, professing.
PHD_mackenzie.txt:1319:awestwar ['wsw.Nll M )wystw)r, N ustuwar] firm, reliable.
PHD_mackenzie.txt:1525: .......isn: bestowal, distribution.
PHD_mackenzie.txt:1916:dastwar [dstwbll M dstwr, N dastilr] authority, priest, minister.
PHD_mackenzie.txt:1970:den-astawan [dyn)stwb)n ], den-burdar [dynbwlel] believing, faithful.
PHD_mackenzie.txt:4685:sto [stwbl , (P <stwb, N suto/z)] distressed, defeated.
PHD_mackenzie.txt:4691:stowenidan, stowen- [stwbyn-ytn'] defeat, overcome.
PHD_mackenzie.txt:6074:bestowal baxsisn.                           body kalbod, kirh, tan.
== NYB astob
714:astavanéh [’stwb’nyh] confession, creed 101%, — MPrs ?stwnyy (A-H II).
1210:dastavar [dstwbl], cas. obl. dastavareh [dstwblyh] 9815 : 1. valid religious doctrine, custom, law 10871; canon of religious doctrines etc. 109°; decision (of a relig- gious authority): pat ~ % oi 101%; <pat> ~ + Hušetar 96; pat hàn à Husetarmäh ~-éh 9814-15, — 2. an expert in religious matters, a theologian, a Dastur, also of the Zoroastrian clergy in general: a theo- logian 1018; x“atai u dahyupat u sardār u ~ + den 1081-2; pl. cas. obl.: ~-dn u dätavarän u hérpatàn u magupatān u den- burtärän 107'3-14, — MPrs dstwr ‘a priest’ (S); Paz. dastūr, Skr. v. ācārya, guru; NP dastür in profane senses (v. Steingass). — dast- from Av. (746) dqh- ‘to teach’, cf (745) dqstvà ‘religious doctrine’; hence MPrth dst ‘able, skilful? (A-H III). Cf Bailey, ZP 160, n. 5; TPhS 1945, 8.
2831:östavär [’wstwb’l] a confidant, pl. cas. obl. ~-dn 1314. — Adj. ‘faithful’ Mx 3911-33, 617, Paz. ztastvär (for xostuvdr), Skr. v. karma-kušala- ‘experimented’, SGV sudak- satara ‘very well qualified’; NP ustuvār; MPrs ’wystw’r pl. ‘the elders of the family’, not to be separated from ava-stā, ava- and avi- having already begun to coalesce in Av.
3544:stob [stwb'] powerless: ~ kartan to de- feat 3319. 858-12, 11574; ~ bütan to be defeated 912. — NW form: MPrth ‘stwb- ‘to enfeeble, to annihilate’ (A-H II, 302 n. 4), evidently a denom. of the adj. ‘stwb = estob (i. e., estöß), taken over by BP as stwb' (the original NW form ’stwb' is still found in FrP, Cod. P fol. 6%) and developed to *stēw > *stöi alternating as usual with stoh, which prevailed: Paz. stoh, stuh, NP sutüh. (The reading stwb' = "stav which I gave in HP was wrong, as shown by the MPrth form ; the spelling -wb- for -v- is unknown in MPrth). The authentic SW form is ‘stw = estav (also in Prth: MPrth ‘st’w- caus. ‘to annihilate’, W.-L. 112, II R 3b) attested in ‘stwy- gwn- ‘to overcome’, ‘stwy-bwdn ‘to be defeated’ (List 81, cf s. v. àkas?), also attested by FrP, Cod. P fol. 284, in the form stw' (erroneously read in Paz. stün, but glossed by sutüh, Anguetil Duperron ‘foible, pauvre’). I derive it from *us- tavah- ‘out of force, powerless’, from Av. (639) tavah-; MPrth estob may go back to *ustava(h)-bū- ‘being powerless’, cf SW ‘stwy-bwdn just mentioned.
```


## [2026-09-14T02:36:05.457Z] TOOL CALL #55: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-14T02:36:05.464Z] TOOL RESULT

```


```


## [2026-09-14T02:36:08.621Z] TOOL CALL #56: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/stebʰ-",
 "prompt": "What is the root, its meaning, and its descendants (Indo-Iranian, Germanic, Greek)? Quote the gloss and note Pokorny page."
}
```


## [2026-09-14T02:36:10.924Z] TOOL CALL #57: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B3%D8%AA%D8%A8%D8%B1",
 "prompt": "Persian ستبر (setabr): give the full etymology, Middle Persian form, Avestan/Proto-Iranian ancestor, and any cited sources (Hasandust, MacKenzie)."
}
```


### [2026-09-14T02:36:13.537Z] TOOL RESULT

```
# Proto-Indo-European Root *stebʰ-

**The Root and Meanings:**
The reconstructed root is *stebʰ-, meaning "to stand still" and "to harden."

**Key Descendants:**

*Indo-Iranian:* Sanskrit stámbhate (स्तम्भते), meaning "to support, strengthen," and stabhnā́ti (स्तभ्नाति)

*Germanic:* Proto-Germanic *stabaz (see further descendants listed)

*Greek:* Ancient Greek staphulḗ (σταφυλή), noted as "most likely Pre-Greek"

**Reference:**
The entry cites Helmut Rix's *Lexikon der indogermanischen Verben* [Lexicon of Indo-European Verbs], 2nd edition (2001), pages 588-589, as the authoritative source for this root.
```


### [2026-09-14T02:36:16.384Z] TOOL RESULT

```
# Etymology of Persian ستبر (setabr)

Based on the Wiktionary entry provided:

**Middle Persian form:** _stpl_ (stabr), meaning "strong, firm"

**Etymology:** The word derives from Middle Persian and is related to cognates across Indo-European languages, including:
- Sanskrit _स्तम्भ_ (stambha, "pillar")
- Old Norse _stafr_ ("staff")
- Old Church Slavonic _стоборъ_ (stoborŭ, "column")
- Ancient Greek _στιβαρός_ (stibarós, "firm")

**Proto-Iranian ancestor:** The document does not explicitly provide a Proto-Iranian reconstruction or reference Avestan forms.

**Cited sources:** The entry does not cite specific scholarly sources such as Hasandust or MacKenzie. It only notes the etymological relationships without attributing them to particular reference works.

The adjective conveys meanings of "strong, firm" (archaic) and "thick" in modern Persian usage.
```


## [2026-09-14T02:36:19.868Z] TOOL CALL #58: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A7%D8%B3%D8%AA%D9%88%D8%A7%D8%B1",
 "prompt": "Persian استوار (ostovār/ustuvār): give the full etymology — Middle Persian form, the prefix and root analysis, and any cited sources."
}
```


## [2026-09-14T02:36:21.365Z] TOOL CALL #59: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A7%D8%B3%D8%AA%D8%A8%D8%B1%D9%82",
 "prompt": "Arabic استبرق (istabraq): give the etymology — Persian source word, Middle Persian, and any cited sources."
}
```


### [2026-09-14T02:36:22.602Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-14T02:36:25.354Z] TOOL RESULT

```
# Etymology of Persian استوار (ustuwār/ostovâr)

The word is **inherited from Middle Persian** _awestwār_ (ʾwstwbʾl in Book Pahlavi). According to the Wiktionary entry, this Middle Persian term is documented in "A concise Pahlavi dictionary" by D. N. MacKenzie (Oxford University Press, 1971), which lists the entry on page 14.

The term does not appear to undergo prefix-root decomposition in the available documentation. The etymology section simply traces the word back through Middle Persian to its historical form without breaking down internal morphological components. The Wiktionary source identifies it as an inherited term but does not provide detailed analysis of roots or affixes.
```


## [2026-09-14T02:36:29.632Z] TOOL CALL #60: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A5%D8%B3%D8%AA%D8%A8%D8%B1%D9%82",
 "prompt": "Arabic إستبرق / استبرق (istabraq): give the etymology — Persian/Middle Persian source, meaning, Qur'anic attestation."
}
```


## [2026-09-14T02:36:30.756Z] TOOL CALL #61: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/staff",
 "prompt": "Etymology of staff (n.): Proto-Germanic form and PIE root cited. Also mention what PIE root etymonline gives."
}
```


### [2026-09-14T02:36:34.839Z] TOOL RESULT

```
# Etymology of Staff (n.)

According to the Online Etymology Dictionary, the noun "staff" traces back through several linguistic layers:

**Proto-Germanic Origin:**
The word comes from Proto-Germanic "*stab-", which is the source of cognates across Germanic languages including Old Saxon, Old Norse, and German forms.

**Proto-Indo-European Root:**
The dictionary identifies the PIE root as "*stebh-", defined as "post, stem, to support, place firmly on, fasten." This root appears in various ancient languages including Old Lithuanian, Sanskrit, Greek, and Old Church Slavonic, all carrying meanings related to support, pillars, or structural elements.

The entry notes that many extended senses derive from the concept of "that which upholds or supports, that which sustains"—exemplified in the phrase "staff of life" referring to bread, which derives from the Biblical expression about cutting off food supplies.
```


### [2026-09-14T02:36:35.223Z] TOOL RESULT

```
# Etymology of إستبرق (Istabraq)

**Source Language:** The word comes from Middle Persian *stplk* (/stabrag/, meaning "shot silk"), which derives from *stpl* (/stabr/, "strong").

**Related Form:** Classical Persian *ستبر* (sitabr) shares the same root, meaning "strong, thick."

**Qur'anic Attestation:** The term appears in Qur'an 44:53 (609–632 CE): "dressed in fine silk and rich brocade, facing one another." This passage describes garments worn in paradise, emphasizing the word's association with luxurious silk fabric.

**Meaning in Arabic:** إِسْتَبْرَق refers to "silk brocade"—a rich, ornamental silk textile, reflecting its Persian origin denoting quality woven material.
```


## [2026-09-14T02:36:40.621Z] TOOL CALL #62: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/Stephen",
 "prompt": "Etymology of the name Stephen/Steven: Greek Stephanos, stephein, and what PIE root is cited."
}
```


## [2026-09-14T02:36:41.232Z] TOOL CALL #63: WebSearch

```json
{
 "query": "Persian ستنبه ستمبه etymology Middle Persian stambag Hasandust"
}
```


### [2026-09-14T02:36:44.316Z] TOOL RESULT

```
# Etymology of Stephen/Steven

The name Stephen derives from Latin *Stephanus*, which comes from Greek *Stephanos*. 

The Greek root *stephein* means "to encircle, crown, wreathe, tie around." According to the source, this traces back to the Proto-Indo-European root **\*stebh-**, which signifies "post, stem; place firmly on, fasten."

The literal meaning of *stephanos* is "that which surrounds," and it was used to describe a crown, wreath, or garland—particularly one awarded as a victory prize in public contests. The name thus carries connotations of triumph and honor.
```


### [2026-09-14T02:36:47.384Z] TOOL RESULT

```
Web search results for query: "Persian ستنبه ستمبه etymology Middle Persian stambag Hasandust"

Links: [{"title":"ستبر - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D8%B3%D8%AA%D8%A8%D8%B1"},{"title":"Setareh","url":"https://en.wikipedia.org/wiki/Setareh"},{"title":"Middle Persian literature","url":"https://en.wikipedia.org/wiki/Middle_Persian_literature"},{"title":"Middle Persian","url":"https://en.wikipedia.org/wiki/Middle_Persian"},{"title":"Persian Online – Grammar & Resources » Middle Persian","url":"https://sites.la.utexas.edu/persian_online_resources/history-of-the-language/middle-persian/"},{"title":"-stan - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/-stan"},{"title":"Category:Persian terms derived from Middle Persian - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Category:Persian_terms_derived_from_Middle_Persian"},{"title":"مجله زبان و ادبیات عربی (Aug 2021)","url":"https://doaj.org/article/29d88127086c4ef39b4a6a29f385977a"}]

Based on the search results, I was unable to find specific information about the Persian words ستنبه or ستمبه, their etymology from Middle Persian "stambag," or any connection to "Hasandust" in the results returned.

The search results returned information about other Persian etymologies (such as ستبر from Middle Persian "stabr," and the suffix -stan from Proto-Iranian *stáHnam), and academic articles related to Persian linguistic studies, but none of these specifically address the terms you're searching for.

To get more targeted results about these specific Persian words and their etymological connections, you might want to try:
- Searching for Persian lexicographical resources or dictionaries
- Looking for specialized articles on Persian historical linguistics
- Consulting academic papers on Middle Persian vocabulary

If you have access to specific academic sources or can provide additional context about where these terms appear, that might help narrow down the search.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-14T02:36:54.010Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== WLD Bd2 steb\"; grep -n \"steb(h)\\|stebh\\|stembh\\|stamba\" incoming/WLD/WLD_Bd2_pages.txt | head -20",
 "description": "Walde-Pokorny Bd II steb-"
}
```


### [2026-09-14T02:36:54.069Z] TOOL RESULT

```
== WLD Bd2 steb
41366:stebh- und stebh- stobh-, nasaliert stembh-;
43043:Fick ni^, 484 = Falk-Torp u. stemme I zu stebh- „Pfosten usw.“; verfehlt
```


## [2026-09-14T02:36:55.196Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== KLN staff\"; grep -n \"base \\*stebh\\|\\*stebh-\\|stebh-\" KLN_1966.txt | head -10",
 "description": "Klein stebh base"
}
```


### [2026-09-14T02:36:55.260Z] TOOL RESULT

```
== KLN staff
```


## [2026-09-14T02:36:58.169Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '41355,41420p' incoming/WLD/WLD_Bd2_pages.txt; echo \"=== leaf\"; awk 'NR<=41366{n+=gsub(/\\f/,\"\")} END{print \"leaf:\",n}' incoming/WLD/WLD_Bd2_pages.txt",
 "description": "WLD steb(h)- entry"
}
```


### [2026-09-14T02:36:59.308Z] TOOL RESULT

```
stlngti „gerinnen, steif, dick werden“, lett, stingstu, stingt „starr, steif, kom-
pakt werden“, stingrs „stramm, starr, zshaltend, gespannt, steif“.
   Vgl. Fick I^ 569, III ^ 480 f., Falk-Torp u. stegg, stang, Ahnlich ^steg-
„Stange“, s. d.


steb- und steb- stob-, nasaliert stemb-;
                          :



stebh- und stebh- stobh-, nasaliert stembh-;
                                  :



step- (auch step-?), nasaliert stemp-.
  Bedeutungsumfang: ,.Pfosten, Pfeiler, Slander, Stamm, Baumstumpf (auch
Busch, Biischel, wohl zunachst von den         um einen Baumstumpf wuchern-
den    W
       urzeltrieben Strunk, Stengel), Stab, z. T. auch (aufragender) Stein^';
                              ;



verbal: „stutzen, versteifen, feststellen, anhalten'^ fauch „hemmen“, was z. T.
auch aus ,,entgegenstemmen“ oder „entgegentreten“ oder „Prugel unter
die PiiBe        werfen“       sein kann)
                                  entwickelt„mit dem FuBe aufstampfen,
                                                                ;


treten      (Tritt,  FuBspur), starapfen (z. T. auch mit einem Pfosten,
                      Stufe,
StoBel); beschimpfen (teils aus mit den Fiifien treten, teils aus steif und
herausfordernd dastehn; aus letzterem wohl hauptsachlich die Bed. prahlen,
groBsprechen), staunen (aus erstarrt dastehen)“. Ahnlich ist der Bedeu-
tungsumfang von Wz. ^steihQiy (mit der Eeichelt KZ. 39, ^8 ganzlich un-
berechtigt Vereinigung unter stdj:bh- ste[i]l)h~ sucht; Zupitza KZ. 36, 67).
                                                       :



Einstige Beziehung zu         „stehn‘' ist der Bed, nach denkbar (Lewy KZ.
40, 420 lehne ich freilich ab).
   Wzf. mit -6 (die aus dem Kelt, und Balt.-Slav. angefiihrten Worte ge-
statten keine sichere Entscheidung zwischen   und -hh und sind nur aus
andern       —
           nicht ganz verbindlichen                    — Erwagungen    teils hier, teils bei der
Wzf. auf -bh eingereiht):
     ai.   sfdbaJca-h,    -m          „Buscher‘, stambd-h „Busch, Buschel“ = lit. stdmbas
„Kohl8trunk“, mir.           tomm „Busch^^ (auch „kleiner Hiigeh*; ob darum eher
zu     gr. TV ji^og      „Erdhuger‘, ai. tumja-h „Anhohe“? Pedersen KG. I 109.
Kir. stjablo „Schussel aus Binsengeflechf', bulgar. sizblo,                  sHmbel „Halm‘‘‘?
Uhlenbeck Ai.Wb. 342 f.);
                         miBhandle, schmahe^ (kaum mit /S aus
     gr. oxeju^co ,,stampfe,                                           zu o-ot.
stigqan            Sabler KZ. 31, 282f. zur Wahl gestellt auch z. B. von
             „stoBen“,
Prellwitz^ 432, Hirt IF. 32, 224; s. Zupitza GG. 2S), oxejLifidCeiv^ Xoidogeiv,
                              ;                    f



624                                        steb-   — stemp-
yJ.evdCeiv Hes.,        aoT8f.i^ay.Tog    „unbeschiinpft‘^, oro^og „Schelten, Prahlerei“,
=== leaf
leaf: 627
```


## [2026-09-14T02:37:46.358Z] TOOL CALL #67: Bash

```json
{
 "command": "pdftoppm -f 476 -l 476 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg476 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg476.png",
 "description": "Render PDF page 476"
}
```


### [2026-09-14T02:37:48.074Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 61025 Sep 13 22:37 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg476.png
```


## [2026-09-14T02:37:50.010Z] TOOL CALL #68: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg476.png"
}
```


### [2026-09-14T02:37:50.493Z] TOOL RESULT

```

```


## [2026-09-14T02:37:50.490Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-14T02:38:05.832Z] TOOL CALL #69: Bash

```json
{
 "command": "mkdir -p data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg476.png data/verification/sources/refs/ocr/BOOK/476.png && python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/stebʰ-' --note 'page 476, root Stebh: PIE *stebʰ- gloss and descendants' ; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/ستبر' --note 'page 476, node 3 setabr: NP ستبر < MP stabr' ; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/استوار' --note 'page 476, node 3 ostovar: NP استوار < MP awestwar (MacKenzie p.14)' ; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/إستبرق' --note 'page 476, node 3 estabrak: Ar. istabraq < MP stabrag' ; python3 tools/fetch_source.py 'https://www.etymonline.com/word/staff' --note 'page 476, node 9: English staff < PIE *stebh-' ; python3 tools/fetch_source.py 'https://www.etymonline.com/word/Stephen' --note 'page 476, node 11: Stephen < Gk stephanos/stephein < PIE *stebh-'",
 "description": "Archive web sources"
}
```


### [2026-09-14T02:38:08.970Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/f234f4b72f72e47f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c8e02a9d3fdb6851.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/bec6852001ca946f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/dbfc2efc070c3613.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c56dd2ab8044fa94.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f63d6048fd0b4991.txt
```


## [2026-09-14T02:38:11.529Z] TOOL CALL #70: Bash

```json
{
 "command": "sed -n '1,120p' /home/sfmqrb/git/rishe/tools/verify_check.py",
 "description": "Read verify_check.py"
}
```


### [2026-09-14T02:38:11.577Z] TOOL RESULT

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


## [2026-09-14T02:39:58.428Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"staff,  n\\.\\|staff, n\\., a stick\" KLN_1966.txt | head -3; echo \"---\"; grep -o \"staff, n\\.[^|]\\{0,400\\}\" KLN_1966.txt | head -2; echo \"=== stamp\"; grep -o \"stamp, tr\\. and intr\\. v\\.[^|]\\{0,350\\}\" KLN_1966.txt | head -2; echo \"=== staple\"; grep -o \"staple, n\\., a U-shaped[^|]\\{0,300\\}\" KLN_1966.txt | head -2",
 "description": "Klein entries for staff/stamp/staple"
}
```


### [2026-09-14T02:39:59.682Z] TOOL RESULT

```
11831:dissymmetric,  dissymmetrical,  adj.,  t)  asymme¬ trical;  2)  symmetrical  in  opposite  directions.  — Formed  fr.  dis-  and  symmetric,  resp.  symmetrical, dissymmetry,  n.,  1)  absence  of  symmetry,  asymme¬ try;  2)  symmetry  in  opposite  directions.  — Formed  fr.  dis-  and  symmetry, distaff,  n.  —  ME.  distaf,  dysestaf,  fr.  OE.  distxf, a  compound  lit.  meaning  ‘a  bedizened  staff.’ The  first  element  of  this  compound  is  rel.  to MLG.  disc,  LG.  diesse,  ‘a  bunch  of  flax  on  a distaff’,  and  to  E.  dizen,  bedizen.  The  second element  is  identical  with  OE.  sttef,  ‘staff’.  See staff.
36528:stadholderate,  stadtholderate,  n.,  office  of  a  stad¬ holder.  —  A  hybrid  coined  fr.  prec.  word  and -ate,  a  subst.  suff.  of  Latin  origin, stadium,  n.,  1)  a  Greek  measure  of  length;  2)  a racecourse.  —  L.,  fr.  Gk.  oxocSiov,  ‘racecourse, stadium’,  which  is  a  blend  of  on diSiov,  ‘race¬ course’,  and  oxaSiov,  neut.  of  axaSioi;,  ‘fix, firm’.  ZtoxSiov  is  a  derivative  of  onas/,  ‘to  draw, tear’  (see  spasm).  ZxaSioc  derives  fr.  I.-E.  base *sta-,  ‘to  stand’;  see  state, staff,  n.  —  ME.  staf,  fr.  OE.  stsef,  ‘stick,  staff",  rel. to  OS.  staf,  ON.  stafr,  Dan.  star,  Swed.  staf, OFris.  stef,  MLG.,  MDu.,  Du.  staf,  OHG.  stab, MHG.  slap,  G.  Slab,  Goth.  *staf-s  (in  dat.  pi. stabim),  ‘element’,  and  cogn.  with  OLith.  stabas, ‘idol’,  Lith.  stebas,  ‘staff,  pillar’,  Lett,  stabs, OSlav.  stoborii,  ‘pillar’,  OPruss.  stabis,  ‘stone’, OI.  stabhrtati,  stabhndti,  ‘supports’.  All  these words  derive  fr.  I.-E.  base  *steb(h)-,  ‘to  cause  to stand,  place,  support;  to  step’.  See  step  and  cp. words  there  referred  to.  Cp.  also  stave  and  the second  element  in  distaff,  Gustavus,  palstave. Derivatives :  staff,  tr.  v.,  staff-ed,  adj. stallage,  n.,  accessories.  —  G.,  fr.  stuffier en,  ‘to dress  up,  trim,  garnish’,  fr.  MLG.  stofferen,  staf- feren,ft.  MDu.  stofferen,  fr.  OF.  estofer  (F.  itof- fer),  fr.  OHG.  stopfon  (MHG.,  G.  stopferi),  ‘to stuff,  fill’.  OF.  estofe  (F.  etoffe),  ‘stuff,  material’, is  prob.  a  back  formation  fr.  estofer  (F.  etoffer). See  stuff  and  -age.
39327:Norw.  tipla,  ‘to  drink  in  small  quantities,  to drip’ ;  of  uncertain  origin, tipstaff,  n.,  a  staff  tipped  with  metal.  —  For  tipped staff.
---
=== stamp
=== staple
```


## [2026-09-14T02:46:39.165Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -o \"staple, n\\.[^|]\\{0,300\\}\" KLN_1966.txt | head -2; echo \"=== step\"; grep -o \"step, intr\\. and tr\\. v\\.[^|]\\{0,300\\}\" KLN_1966.txt | head -2",
 "description": "Klein staple/step"
}
```


### [2026-09-14T02:46:40.205Z] TOOL RESULT

```
=== step
```


## [2026-09-14T02:52:20.604Z] TOOL CALL #73: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/write476.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW_PIE = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/steb%CA%B0-\"\nW_SETABR = \"https://en.wiktionary.org/wiki/%D8%B3%D8%AA%D8%A8%D8%B1\"\nW_OSTOVAR = \"https://en.wiktionary.org/wiki/%D8%A7%D8%B3%D8%AA%D9%88%D8%A7%D8%B1\"\nW_ISTABRAQ = \"https://en.wiktionary.org/wiki/%D8%A5%D8%B3%D8%AA%D8%A8%D8%B1%D9%82\"\nE_STAFF = \"https://www.etymonline.com/word/staff\"\nE_STEPHEN = \"https://www.etymonline.com/word/Stephen\"\n\ndata = {\n  \"pdf_page\": 476,\n  \"book_page\": 446,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-13\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Stebh\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *stebʰ- (unaspirated variant *steb-, nasalised *stembʰ-/*stemb-) 'post, pillar, stump; to prop, make firm'\",\n      \"note\": \"Pokorny's lemma runs 'steb(h)- und stēb(h)-, stəb(h)-, nasalized stemb(h)-, step- (also stēp-?), nasalized stemp-', glossed 'post, pillar, stump; to support, etc.', IEW pp. 1011-1013 — so Nourai's POK:1012 falls squarely inside the entry and his gloss 'support, stem' is a fair condensation of it. Watkins/AHD has the same root as 'stebh-. Post, stem; to support, place firmly on, fasten. [Pok. steb(h)- 1011]'; Walde-Pokorny II 623f. gives the same triple root-shape. Wiktionary reconstructs *stebʰ- 'to stand still, to harden' after LIV² 588-9. Language label and gloss are both right. Pokorny notes that a connection with *stā- 'stand' is conceivable but unproven — relevant below, because two of the Persian words on this chart (ostovâr, ostovân) in fact belong to *steh₂- and *stew-, not here.\",\n      \"note_fa\": \"ریشهٔ هندواروپایی آغازین *stebʰ- «ستون، تیرک، کندهٔ درخت؛ تکیه دادن، استوار کردن»، با گونهٔ بی‌دمشِ *steb- و گونهٔ خیشومی‌شدهٔ *stembʰ-. پوکورنی این مدخل را در صفحه‌های ۱۰۱۱ تا ۱۰۱۳ آورده است، پس ارجاع نورایی (POK:1012) درست در میان همان مدخل می‌افتد و برگردان او «support, stem» فشرده‌ای درست از معنای پوکورنی است؛ والده-پوکورنی (جلد ۲، ص ۶۲۳–۶۲۴) و واتکینز در پیوست فرهنگ American Heritage نیز همین ریشه و همین معنا را می‌دهند. پس ادعای نورایی دربارهٔ خودِ ریشه درست است. تنها نکتهٔ هشداردهنده این است که پوکورنی خود پیوند احتمالی این ریشه را با *steh₂- «ایستادن» یادآور می‌شود، و همین‌جاست که دو واژهٔ «استوار» و «استوان» در این نمودار به اشتباه زیر این ریشه نشانده شده‌اند.\",\n      \"sources\": [W_PIE, E_STAFF],\n      \"ref_check\": [\n        {\"ref\": \"POK:1012\", \"status\": \"supports\", \"note\": \"POK_full.txt (grep 'steb(hj-'), entry ending 'Page(s): 1011-1013': 'Root / lemma: steb(h)- and stēb(h)-, stəb(h)-, nasalized stemb(h)-, step- ... Meaning: post, pillar, stump; to support, etc.. Note: relationship to *stā- \\\"stand\\\" is possible.' Nourai's page 1012 is inside this entry; the gloss matches.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"POK\", \"where\": \"IEW 1011-1013 (POK_full.txt, line ~81374)\", \"stance\": \"supports\", \"note\": \"'Meaning: post, pillar, stump; to support, etc.'; the Iranian material of the whole chart (Av. stembana-, Av. stawra-, np. sitabr, np. sitamba, ap. stabava) is gathered in this one entry.\"},\n        {\"src\": \"WLD\", \"where\": \"Bd. II 623-624 (WLD_Bd2_pages.txt, line 41366)\", \"stance\": \"supports\", \"note\": \"'steb- und stēb- stob-, nasaliert stemb-; stebh- und stēbh- stobh-, nasaliert stembh-; step- ... Bedeutungsumfang: \\\"Pfosten, Pfeiler, Ständer, Stamm, Baumstumpf ... Stab\\\"; verbal: \\\"stützen, versteifen, feststellen, anhalten\\\"'.\"},\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. stebh- (AHD_watkins1985.txt, line 1002)\", \"stance\": \"supports\", \"note\": \"'stebh-. Post, stem; to support, place firmly on, fasten. I. Basic form *stebh- ... II. Unaspirated form *steb- ... III. Variant *stabh- in Greek staphulē. [Pok. steb(h) 1011.]'\"},\n        {\"src\": \"IEC\", \"where\": \"Mann col. ~1300, s.v. stembh- (IEC.txt line 17187)\", \"stance\": \"supports\", \"note\": \"'stembh- (stembhəlos, stembhros) \\\"hard; hardness, firmness, stay, support\\\". WP II, 624. Skt. stambh- radical: \\\"support\\\"; Av. stəmb-, id. ...'\"},\n        {\"src\": \"SYN\", \"where\": \"Buck p. 1363 (SYN.txt line 34165)\", \"stance\": \"supports\", \"note\": \"under 'quarrel': 'Av. stamba- (Barth. 1606, IF 11.139), cf. NPers. sitamba \\\"violent, quarrelsome\\\" : Skt. stambha- \\\"inflation, arrogance\\\", lit. \\\"post, pillar, support\\\". Cf. Horn 718.'\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"stawra; stambana; stembya\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"All three are Avestan formations on this root. (a) stawra- adj. 'stark, fest' (Bartholomae AiW col. 1593, quoting Yt 10.28) continues *stabʰ-ra-/*stəbʰ-ra-, Indo-Iranian *-bʰr- yielding Avestan -wr-; Bartholomae's own entry closes 'Zum V. stamb-. — np. sitabr', i.e. exactly the line of this chart. (b) stəmbana- n. 'prop, support' is the nasal stem *stembʰ- plus -ana-; Bartholomae has it in the compound fra-stəmbana- 'Stütze, Balken, Stutz-, Brückenbalken' (Vd 18.74, s.v. the verb skamb- 'stemmen', the Avestan sk-/st- doublet of Skt. skambh-/stabh-), and Pokorny equates it outright: 'stambhanam \\\"fortification, Festhalten\\\" = Avestan stembana- \\\"Stütze\\\"'. (c) stəmbya- is the -ya- adjective 'hard, violent'; Gharib cites it as 'Av. stənbya-' when explaining Sogdian stamb (Sogdian Dictionary no. 8995, p. 363) — which is precisely the SOD:363 Nourai gives here. Nourai's stawra/stambana/stembya are therefore ordinary transliterations of stawra-, stəmbana-, stəmbya-, and the glosses 'firm / support / hard' are the standard ones.\",\n          \"derivation_fa\": \"هر سه واژهٔ این جعبه اوستایی‌اند و از همین ریشه ساخته شده‌اند. stawra- «استوار، سخت» از *stabʰ-ra- می‌آید؛ خوشهٔ *-bʰr- هندوایرانی در اوستایی به -wr- بدل شده است، و بارتولمه (ستون ۱۵۹۳) خود در پایان همین مدخل می‌نویسد: «مربوط به فعل stamb-؛ فارسی نو sitabr». stəmbana- «تکیه‌گاه، ستون» از ستاک خیشومی *stembʰ- با پسوند -ana- ساخته شده و در ترکیب fra-stəmbana- «تیر پل، شاه‌تیر» (وندیداد ۱۸٫۷۴) گواهی دارد؛ پوکورنی آن را برابر سنسکریت stambhanam می‌گذارد. stəmbya- نیز صفتی است با پسوند -ya- که قریب (فرهنگ سغدی، مدخل ۸۹۹۵، ص ۳۶۳) هنگام شرح واژهٔ سغدی stamb به آن ارجاع می‌دهد — همان ارجاعی که نورایی در این جعبه آورده است. پس ادعای نورایی در این گره درست است.\",\n          \"sources\": [W_PIE],\n          \"ref_check\": [\n            {\"ref\": \"POK:1012\", \"status\": \"supports\", \"note\": \"IEW 1011-1013: 'stambhanam \\\"fortification, Festhalten, hindrance\\\" = Avestan stembana- \\\"pad\\\" (Stütze), Avestan stawra- \\\"tight, firm\\\", np. sitabr, /stabr/ \\\"strong, vast, grand\\\"'.\"},\n            {\"ref\": \"BQT:1098\", \"status\": \"supports\", \"note\": \"Borhan vol. 2, leaf NR=561 of BQT_v2_pages.txt (= printed p. 1098; the leaf two earlier carries the running head ۱۰۹۶), footnote 2 to ستبر: «استبر، اوستا stawra- (محکم)، پهلوی stabr و stawr، هندی باستان stabh- (تمید کردن، تکیه دادن)، قس: استی stur (قوی)». The Avestan etymon Nourai draws is Mo'in's.\"},\n            {\"ref\": \"SOD:363\", \"status\": \"supports\", \"note\": \"SOD_pages.txt leaf NR=431 (printed 363), entry '8995 stmb M — stamb ©<Av. stənbya-, MP istambagih ⇒'st'np, stpty(y) — stern'. Gharib's 'Av. stənbya-' is Nourai's 'stembya'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"AiW col. 1593 s.v. stawra-, col. 1588 s.v. skamb- / fra-stəmbana- (BRT.txt lines 26553, 26461, 17922)\", \"stance\": \"supports\", \"note\": \"'j. stawra- Adj. (fem. -ra-) \\\"stark, fest\\\": mihrəm .. yə .. °rī aiβya kərənaoiti Yt. 10.28. Zum V. stamb-. — np. sitabr.' and 'j. fra-stəmbana- n. \\\"Stütze, Balken, Stutz-, Brückenbalken\\\"'.\"},\n            {\"src\": \"POK\", \"where\": \"IEW 1012 (POK_full.txt line 81422)\", \"stance\": \"supports\", \"note\": \"'= Avestan stembana- \\\"pad\\\", Avestan stawra- \\\"tight, firm\\\", np. sitabr'.\"},\n            {\"src\": \"SOD\", \"where\": \"Gharib no. 8995, p. 363\", \"stance\": \"supports\", \"note\": \"cites 'Av. stənbya-' as the comparandum of Sogd. stamb — the only book on the shelf that knows Nourai's 'stembya'.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. II 624-625\", \"stance\": \"supports\", \"note\": \"the -bh- root-shape section gathers 'ai. stabhnāti, stambhate ... av. stəmbana-, stawra-' under the same lemma (WLD_Bd2_pages.txt, leaf 627).\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"stapr, stawr; hôstubâr, astô-bâr; astô-bân\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"The first pair is right, the other two are not. (a) stapr/stawr: Book-Pahlavi <stpl>, read stabr by MacKenzie (CPD p. 77: 'stabr [stpl | M stbr, N sitabr] big, coarse, strong; ~īh: coarseness; strength, force'). Horn prints precisely Nourai's doublet — 'phlv. stapr (Vd. 18 (65) Gl.), d.i. stawr' (Grundriss no. 713, p. 158) — where stapr is the graphic transliteration of <stpl> and stawr the phonetic reading; the form continues Av. stawra- with Old Iranian -wr- passing into MP -br-. Confirmed. (b) hôstubâr / astô-bâr: this is MP <'wstwb'l>, read awestwār by MacKenzie (CPD p. 14: 'awestwār | M ʾwystwʾr, N ustuwār — firm, reliable') and ōstavār by Nyberg (Manual II, s.v.), who says explicitly that it is 'not to be separated from ava-stā-, ava- and avi- having already begun to coalesce in Avestan' — i.e. ava- + the root *steh₂- 'stand' + the suffix -wār, not *stebʰ- + a second element from *bʰer-. Nourai's odd-looking hôstubâr is in fact the Pāzand form Nyberg records, xᵛastvār (for xōstuvār), so it is not a misprint, but his analysis 'astō- (firm) + -bār (☞Bher)' is rejected by the standard Middle-Persian dictionaries. (c) astō-bân: MP āstawān <'stwb'n', 'stwp'n'> 'confessing, professing' (MacKenzie CPD p. 13; Nyberg, astavānēh 'confession, creed'; negated an-āstawān 'disbelieving'), from Avestan stav- 'to praise, profess' (PIE *stew-). Its sense 'steadfast, firm in belief' is what Mo'in's footnote renders «معتقد و ثابت‌قدم», which is why Nourai read it as 'firm'; but the -wān is the participle of stav-, not the agent suffix -bān 'keeper' from √pā-.\",\n          \"derivation_fa\": \"از سه فقرهٔ این جعبه تنها فقرهٔ نخست درست است. stapr/stawr همان <stpl> پهلوی است که مکنزی آن را stabr می‌خواند («بزرگ، درشت، نیرومند»، فرهنگ کوچک پهلوی ص ۷۷) و هرن در «گروندریس» (شمارهٔ ۷۱۳) دقیقاً همین جفت را می‌آورد: «پهلوی stapr، یعنی stawr»؛ stapr نویسه‌گردانی خط پهلوی و stawr خوانش آوایی آن است، و واژه از اوستایی stawra- می‌آید با تبدیل -wr- ایرانی باستان به -br- فارسی میانه. اما hôstubâr/astō-bār همان <ʾwstwbʾl> است که مکنزی awestwār و نیبرگ ōstavār می‌خوانند و نیبرگ به‌صراحت می‌گوید که این واژه را نباید از ava-stā- «ایستادن» جدا کرد؛ یعنی از ریشهٔ *steh₂- است نه از *stebʰ-، و جزء دوم آن پسوند -wār است نه بازماندهٔ ریشهٔ bher-. (شکل غریب hôstubâr خطای چاپی نیست؛ همان صورت پازند xᵛastvār/xōstuvār است که نیبرگ ثبت کرده.) astō-bān نیز در اصل āstawān «معترف، مقرّ به دین» است (مکنزی ص ۱۳، نیبرگ astavānēh «اقرار، اعتقاد»)، از ریشهٔ اوستایی stav- «ستودن، اقرار کردن» (هندواروپایی *stew-)؛ معنای «ثابت‌قدم» که معین در حاشیهٔ برهان آورده از همین‌جاست. پس پژوهش امروزی دو فقرهٔ دوم و سوم را از این ریشه بیرون می‌برد.\",\n          \"sources\": [W_OSTOVAR],\n          \"ref_check\": [\n            {\"ref\": \"BQT:1098\", \"status\": \"supports\", \"note\": \"Borhan vol. 2 p. 1098, Mo'in's footnote to ستبر: «پهلوی stabr و stawr» — supports the stapr/stawr pair only.\"},\n            {\"ref\": \"FVQ:59\", \"status\": \"supports\", \"note\": \"Jeffery, Foreign Vocabulary of the Qur'an p. 59 (FVQ_pages.txt line ~2470): 'The Phlv. stabr = thick (Nyberg, Glossar, 206), is used of clothing in eschatological writings, e.g. Arda Viraf, xiv, 14 ... \\\"and glorious and thick splendid clothing\\\"'. Again only the stabr/stawr line.\"},\n            {\"ref\": \"MON:261,262\", \"status\": \"partial\", \"note\": \"the local Mo'in is the 2-volume Adena reprint, whose pagination differs from the 6-volume Amir Kabir set Nourai cites, so pp. 261-262 could not be turned to; the corresponding headwords استوار/استوان are present but Mo'in gives no Pahlavi Latin form in this reprint. Mo'in's etymological note for استوار/استوان is however preserved in his Borhan footnote at BQT:127 (below), which reads «پهلوی ... معتقد و ثابت‌قدم «یونکر»».\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD p. 77 s.v. stabr; p. 14 s.v. awestwār; p. 13 s.v. āstawān\", \"stance\": \"partial\", \"note\": \"'stabr [stpl | M stbr, N sitabr] big, coarse, strong' supports the first pair; but 'awestwār [ʾwstwbʾl | M ʾwystwʾr, N ustuwār] firm, reliable' and 'āstawān [ʾstwbʾn', ʾstwpʾn' | M ʾstwʾn] confessing, professing' show the other two belong elsewhere.\"},\n            {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II s.v. ōstavār and astavānēh (NYB_vol2_glossary.txt lines 2831, 714)\", \"stance\": \"contradicts\", \"note\": \"'ōstavār [ʾwstwbʾl] a confidant ... Paz. xᵛastvār (for xōstuvār) ... NP ustuvār; MPrs ʾwystwʾr ... not to be separated from ava-stā, ava- and avi- having already begun to coalesce in Av.' — explicitly a *steh₂- word, not *stebʰ-.\"},\n            {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 713, p. 158\", \"stance\": \"supports\", \"note\": \"'aw. stawra- (*stabhra-, *str̥bhra-) \\\"fest\\\"; phlv. stapr (vd. 18 (65) Gl.), d. i. stawr' — Nourai's 'stapr, stawr' is taken straight from here. Horn only says 'vergl. ustuwār', i.e. compares it, without deriving it from this root.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"setabr «ستبر ( استبر )»; estabrak «استبرک ( استبرق )»; ostovâr «استوار ( سُتوار )»; ostovân «استوان ۲ ( سُتوان ۲ )»\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Two of the four are solid, two are not. (a) setabr ستبر (variant استبر with prothetic vowel before initial st-) < MP stabr 'big, coarse, strong' < Av. stawra-; Hübschmann makes it a textbook case of the sound law, 'sitabr \\\"stark\\\" = zd. stawra-' with ap./OIr. w > NP b before r (Persische Studien §75), and Horn no. 713 lists sitebr/setebr/istebr 'stark, gewaltig'. The semantic drift 'firm, solid' → 'thick, stout' is the ordinary one; Ferdowsī's line quoted in the box ('مران سرو استبر گشتش میان') already uses the 'thick' sense. Confirmed. (b) estabrak استبرک < MP stabrag <stplk'> 'shot silk, thick brocade' = stabr + the adjectival suffix -ag; MacKenzie glosses the Pahlavi word and, unusually, gives its offspring in the entry itself: 'stabrag [stplk' | Ar. istabraq] shot silk'. The word was taken into Arabic before the Qur'ān as إستبرق istabraq 'silk brocade' (Q 18:31, 44:53, 55:54, 76:21), the Arabic -q rendering the Middle Persian suffix -k/-g (Jeffery, FVQ 58-60, citing al-Jawharī, the Qāmūs and Addai Shir; 'there can be little doubt that the word passed directly into Arabic from the Middle Persian'), and it came back into Persian in that Arabic dress — hence Nourai's parenthesis (استبرق). Mo'in's own dictionary says the same: «استبرق: [معرب استبرک] دیبای ستبر». Confirmed, with the round trip Persian → Arabic → Persian. (c) ostovâr استوار: disputed. The Persian word continues MP awestwār/ōstavār <ʾwstwbʾl>, which MacKenzie and Nyberg derive from ava-stā- 'to stand (firm)', i.e. PIE *steh₂-; Wiktionary follows MacKenzie (CPD p. 14). It is not a compound of stabr with a 'bearing' element. The gloss 'firm, an army rank' is nevertheless accurate for modern usage — استوار is the Iranian army's warrant-officer rank, a 20th-century use of the old adjective. (d) ostovân استوان: disputed likewise. It is MP āstawān 'professing, confessing (the faith)', hence 'steadfast, trustworthy' — Mo'in's footnote in Borhan p. 127 glosses the Pahlavi «معتقد و ثابت‌قدم» citing Junker — from Av. stav- 'to praise, profess' (PIE *stew-). Both ostovâr and ostovân are genuine Persian words with the glosses given; only their parentage is wrong.\",\n          \"derivation_fa\": \"از چهار واژهٔ این جعبه دو تا استوارند و دو تا نه. «ستبر» (گونهٔ «استبر» با واکهٔ آغازین افزوده پیش از st-) از فارسی میانهٔ stabr و آن از اوستایی stawra- می‌آید؛ هوبشمان در «مطالعات فارسی» (بند ۷۵) آن را نمونهٔ درسی این قاعده می‌داند که w ایرانی باستان پیش از r در فارسی نو به b بدل می‌شود. تحول معنایی «سخت، محکم» به «کلفت، ضخیم» طبیعی است و در بیت فردوسیِ همین جعبه معنای «ضخیم» به کار رفته است. «استبرک» از فارسی میانهٔ stabrag «دیبای ستبر» است (stabr + پسوند -ag)؛ مکنزی خودش در همان مدخل می‌نویسد «stabrag [stplk'] — عربی istabraq». این واژه پیش از اسلام به عربی رفته و در قرآن (کهف ۳۱، دخان ۵۳، الرحمن ۵۴، انسان ۲۱) به صورت «إستبرق» آمده است — قاف عربی جانشین پسوند -k/-g پهلوی شده — و سپس به‌صورت معرّب «استبرق» به فارسی بازگشته است؛ پس نمونهٔ روشنی از وام‌گیری دوسویه (فارسی ← عربی ← فارسی) است. معین نیز می‌نویسد: «استبرق: [معرب استبرک] دیبای ستبر». اما «استوار» و «استوان» را پژوهش امروزی از این ریشه بیرون می‌برد: «استوار» دنبالهٔ فارسی میانهٔ awestwār/ōstavār است از ava-stā- «ایستادن» (ریشهٔ *steh₂-)، و «استوان» همان āstawān «معترف، مقرّ به دین» است از ریشهٔ stav- «ستودن» (*stew-). هر دو واژه واقعی‌اند و معنای «استوار/معتمد» را دارند (و «استوار» امروز درجهٔ نظامی است)، ولی نسبتشان با ریشهٔ Stebh درست نیست.\",\n          \"sources\": [W_SETABR, W_ISTABRAQ, W_OSTOVAR],\n          \"ref_check\": [\n            {\"ref\": \"BQT:127\", \"status\": \"supports\", \"note\": \"Borhan vol. 1, leaf NR=342 of BQT_v1_pages.txt = printed p. 127 (the leaf four earlier carries the running head ۱۲۳): headwords استوار «بمعنی محکم و مضبوط ... امین و معتمد», استوان ۲ «بمعنی استوار است که محکم و مضبوط و امین و معتمد باشد», with Mo'in's footnote «پهلوی … معتقد و ثابت‌قدم «یونکر»». The page is the right one for ostovâr/ostovân; note that it gives no *stebʰ- etymology, only the Pahlavi form.\"},\n            {\"ref\": \"BQT:1098\", \"status\": \"supports\", \"note\": \"Borhan vol. 2 p. 1098 s.v. ستبر: «بکسر اول، بروزن و معنی سطبر است که کلفت و لُنک و غلیظ باشد؛ و سطبر با طای حطی معرب آنست», footnote «اوستا stawra- (محکم)، پهلوی stabr و stawr، هندی باستان stabh-».\"},\n            {\"ref\": \"FVQ:59\", \"status\": \"supports\", \"note\": \"Jeffery pp. 58-60 on إستبرق: 'one of the few words that have been very generally recognized by the Muslim authorities as a Persian loan-word ... Pers. استبرک sometimes written استبرق ... is a form of ستبر meaning big, thick, gross, apparently from a root stabr firm, stable (cf. Skt. sthavira; Av. staura; Oss. st'ur) ... The Ar. ق represents the Phlv. suffix -k.' Exactly Nourai's arrow.\"},\n            {\"ref\": \"MON:240\", \"status\": \"partial\", \"note\": \"the local Mo'in is the 2-volume Adena reprint (different pagination), so p. 240 of the 6-volume edition could not be turned to; the entry itself is there and says what Nourai needs: «استبرق: [معرب استبرک] دیبای ستبر، استبرک» (MON_part1.txt line 11396).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 713, p. 158\", \"stance\": \"partial\", \"note\": \"'sitebr, setebr, istebr \\\"stark, gewaltig\\\", vergl. ustuwār; arab. LW. istabraq \\\"grober Atlasstoff\\\"' — supports setabr and estabrak > Ar. istabraq, but only 'compares' ustuwār instead of deriving it.\"},\n            {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien §75, p. 181 (HUB.txt line 6398); index p. 74\", \"stance\": \"supports\", \"note\": \"'ap. b nach Vokalen ... = np. b in: abr \\\"Wolke\\\" ... ; sitabr \\\"stark\\\" = zd. stawra-'; and 'istabr = sitabr H. 713'.\"},\n            {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD p. 77\", \"stance\": \"supports\", \"note\": \"'stabr [stpl | M stbr, N sitabr] big, coarse, strong' and 'stabrag [stplk' | Ar. istabraq] shot silk' — the Middle-Persian link for both setabr and estabrak, with the Arabic loan named in the entry.\"},\n            {\"src\": \"MON\", \"where\": \"Mo'in, Farhang-e Farsi s.v. استبرق (MON_part1.txt line 11396)\", \"stance\": \"supports\", \"note\": \"«استبرق: [معرب استبرک] دیبای ستبر، استبرک».\"},\n            {\"src\": \"NYB\", \"where\": \"Nyberg, Manual II s.v. ōstavār\", \"stance\": \"contradicts\", \"note\": \"'NP ustuvār ... not to be separated from ava-stā' — takes استوار out of this root.\"},\n            {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e rishe-ha-ye hend-o-orupayi, entry ستبر/استبر (ARY_pages.txt, pdf page 345)\", \"stance\": \"supports\", \"note\": \"heads the entry «ستبر، استبر» and lists the Avestan/Sanskrit/Germanic cognates of this root with a citation to برهان قاطع ۱۰۹۸ — the same page Nourai cites.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Sogdian\",\n          \"words\": \"stmb\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The word and the gloss are right: Gharib, Sogdian–Persian–English Dictionary no. 8995 (p. 363), 'stmb M — stamb, © < Av. stənbya-, MP istambagīh, ⇒ ʾstʾnp, stpty(y) — stern' (attested in the Manichaean-script Sogdica 16.13b). What is not right is the filiation drawn on the chart: Sogdian is not descended from Avestan. Sogdian stamb continues the common Old Iranian nasal stem *stamba- (whence also Parthian stʾmb and MP stambag), and Gharib's '< Av.' is his usual way of citing the Avestan comparandum, not a line of descent. Nourai's citation 'SOD:63' is a misprint: the printed page of the dictionary itself reads 'Sogdian [book] SOD:63' (so the extraction is faithful), but Gharib's stmb stands on p. 363 — the very number Nourai gives one box above, for the Avestan node; a digit has been dropped in the book.\",\n          \"derivation_fa\": \"واژه و معنا درست است: قریب در «فرهنگ سغدی» (مدخل ۸۹۹۵، ص ۳۶۳) می‌آورد: «stmb (مانوی) — stamb، از اوستایی stənbya-، فارسی میانه istambagīh — سختگیر، درشت». اما پیکان نمودار دقیق نیست؛ سغدی فرزند اوستایی نیست. stamb سغدی دنبالهٔ ستاک خیشومی ایرانی باستان *stamba- است (همان که پارتی stʾmb و فارسی میانه stambag نیز از آن‌اند) و علامت «<Av.» در فرهنگ قریب به معنای «هم‌ریشه با اوستایی» است نه «برگرفته از اوستایی». ارجاع SOD:63 نیز خطای چاپی کتاب است — تصویر صفحهٔ چاپی همین «SOD:63» را نشان می‌دهد، پس خطای خوانش اسکن نیست — و شمارهٔ درست ۳۶۳ است، یعنی همان صفحه‌ای که نورایی یک جعبه بالاتر آورده است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"SOD:63\", \"status\": \"not_found\", \"note\": \"SOD_pages.txt leaf NR=129/130 (printed p. 63) is in the ʾsp- range and has no stmb. The entry is no. 8995 on p. 363 (leaf NR=431; the preceding leaf carries the running number 362). The printed book page 446 shows 'SOD:63', so this is Nourai's own misprint for SOD:363.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"SOD\", \"where\": \"Gharib no. 8995, p. 363\", \"stance\": \"supports\", \"note\": \"'stamb ©<Av. stənbya-, MP istambagih ⇒ʾstʾnp, stpty(y) — stern'; the gloss 'stern' is word-for-word Nourai's.\"},\n            {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD p. 77 s.v. stambag\", \"stance\": \"supports\", \"note\": \"'stambag [sthmbk' (-h- < stahm) | M ʾstmbg, N sitamba] oppressive; obstinate' — the Middle Persian member of the same *stamba- family Gharib cross-refers to.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Old Persian\",\n          \"words\": \"stambaka; stamb\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"stamb is genuine Old Persian. Kent's lexicon, p. 210: 'staᵐb- vb. \\\"revolt\\\": NPers. sutamb- \\\"revolt\\\", perhaps also Skt. sta(m)bh- \\\"fasten, hold up, oppose\\\" ... stabava 2d sg. inj. DNa 60' — the sole attestation is the injunctive stabava in Darius' Naqš-e Rostam inscription (DNa 60, mā stabava 'do not resist/rebel'), which Pokorny also cites ('ap. staᵇbava \\\"resist! rebel!\\\"'). So the label, the form and the gloss 'stand firm, revolt' are correct. stambaka 'strong', however, is not attested in Old Persian: no such entry exists in Kent. The -ka- derivative is Middle Persian stambag <sthmbk'> 'oppressive, obstinate' (MacKenzie p. 77), which is also the source of Armenian stambak; Mo'in's footnote at Borhan p. 1100 writes «پارسی باستان stamba-» and compares Skt. stambha- and Arm. stambak, and Buck (p. 1363) cites 'Av. stamba-' after Bartholomae. Nourai's 'stambaka' is therefore a Middle-Persian/Armenian form projected back into Old Persian; the underlying *stamba- is real, the Old Persian label for the -ka- form is not.\",\n          \"derivation_fa\": \"stamb واقعاً پارسی باستان است: کنت در واژه‌نامهٔ «پارسی باستان» (ص ۲۱۰) می‌آورد «staᵐb- فعل «شوریدن»: فارسی نو sutamb- «شوریدن»، شاید هم‌ریشه با سنسکریت sta(m)bh-؛ صیغهٔ stabava، دوم‌شخص مفرد، کتیبهٔ DNa سطر ۶۰» — یعنی همان جملهٔ داریوش در نقش رستم «mā stabava» (سرکشی مکن). پوکورنی نیز همین صورت را نقل می‌کند. اما stambaka در پارسی باستان گواهی ندارد و در واژه‌نامهٔ کنت نیست؛ صورت با پسوند -ka در فارسی میانه است: stambag «ستمگر، لجوج» (مکنزی ص ۷۷)، که ارمنی stambak نیز از آن وام گرفته شده. معین در حاشیهٔ برهان (ص ۱۱۰۰) «پارسی باستان stamba-» می‌نویسد و باک (ص ۱۳۶۳) به نقل از بارتولمه «اوستایی stamba-». پس ادعای نورایی با احتیاط پذیرفتنی است: ستاک *stamba- واقعی است، ولی برچسب «پارسی باستان» برای stambaka درست نیست.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"KNT:210\", \"status\": \"supports\", \"note\": \"KNT_full.txt, the page bearing the printed numeral 210: 'staᵐb- vb. \\\"revolt\\\": NPers. sutamb- \\\"revolt\\\", perhaps also Skt. sta(m)bh- \\\"fasten, hold up, oppose\\\" (Wb. AbhSGW 29.1.34; Mt. As. 1911.637; MB Gr. §202). stabava 2d sg. inj. (§216, §224, §227.1, §287) DNa 60.' Exactly Nourai's 'stamb: stand firm, revolt' — but there is no stambaka in the lexicon.\"},\n            {\"ref\": \"BQT:1100\", \"status\": \"supports\", \"note\": \"Borhan vol. 2, leaf NR=563 (= printed p. 1100), headword ستنبه with Mo'in's footnote: «ستنبه = ستمبه. رک: استنبه، پارسی باستان stamba- ... قس: هندی باستان ... ارمنی stambak «اسشق ۸۷» ورک: نیبرگ ۲۷ ... stambakīh». This is where Nourai's 'Old Persian stambaka' comes from.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, Lexicon p. 210\", \"stance\": \"partial\", \"note\": \"has staᵐb- 'revolt' (stabava, DNa 60) but no stambaka; also gives 'NPers. sutamb- \\\"revolt\\\"', which is the ستنبه of the next box.\"},\n            {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD p. 77 s.v. stambag\", \"stance\": \"contradicts\", \"note\": \"the -ka- form is Middle Persian: 'stambag [sthmbk' (-h- < stahm) | M ʾstmbg, N sitamba] oppressive; obstinate. ~īh: oppression; obstinacy.'\"},\n            {\"src\": \"SYN\", \"where\": \"Buck p. 1363\", \"stance\": \"partial\", \"note\": \"'Av. stamba- (Barth. 1606, IF 11.139), cf. NPers. sitamba \\\"violent, quarrelsome\\\" : Skt. stambha- \\\"inflation, arrogance\\\"' — Buck labels the base form Avestan, not Old Persian.\"},\n            {\"src\": \"POK\", \"where\": \"IEW 1012\", \"stance\": \"supports\", \"note\": \"'ap. staᵇbava \\\"resist! rebel!\\\" (indoiran. *staᵐbʰau-)' beside 'compare np. sitamba \\\"violent, brutal, streitsüchtig\\\"'.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Persian\",\n          \"words\": \"setonbeh «ستنبه»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"NP ستنبه setonbeh (also written ستمبه setambeh, استنبه) continues Middle Persian stambag <sthmbk'> 'oppressive, obstinate' — MacKenzie sets out the whole line in one entry, 'stambag [sthmbk' (-h- < stahm) | M ʾstmbg, N sitamba]', noting that the -h- of the Book-Pahlavi spelling is a graphic contamination from stahm 'violence' (whence NP ستم). MP -ag regularly gives NP -a/-e, so stambag > سِتَمبه, and the nasal is written indifferently m or n before b, whence the usual spelling ستنبه. The chart's arrow from Old Persian is right in substance — NP descends from MP, which continues the Old Persian stem staᵐb- that Kent glosses 'revolt' and to which he himself attaches 'NPers. sutamb- \\\"revolt\\\"' — it merely skips the Middle-Persian stage. All three of Nourai's glosses are attested: Pokorny 'np. sitamba \\\"violent, brutal, quarrelsome\\\"' and Buck 'NPers. sitamba \\\"violent, quarrelsome\\\"' give 'strong, violent'; Noushin's Shahnameh glossary heads the entry «ستنبه (بروزن شکنجه): زشت‌رو، بدقیافه» ('ugly, ill-favoured') and quotes the Daqiqi line about Bīdarafš and precisely Nourai's Vīs-o-Rāmīn couplet «گرفتش دایه و گفتش چه بودت؟ / ستنبه دیو بدخو چه نمودت؟».\",\n          \"derivation_fa\": \"«ستنبه» (و گونه‌های «ستمبه» و «استنبه») دنبالهٔ فارسی میانهٔ stambag «ستمگر، لجوج» است؛ مکنزی همهٔ زنجیره را در یک مدخل می‌آورد: «stambag [sthmbk'] — مانوی ʾstmbg، فارسی نو sitamba» و یادآور می‌شود که «ه» در املای پهلوی کتابی از آمیختگی با stahm «ستم» پدید آمده است. پسوند -ag فارسی میانه در فارسی نو به -ه بدل می‌شود و خیشومی پیش از b گاه «م» و گاه «ن» نوشته می‌شود، از این‌رو املای رایج «ستنبه». پیکان نمودار از «پارسی باستان» در اصل درست است — فارسی نو از راه فارسی میانه به ستاکِ staᵐb- پارسی باستان می‌رسد و کنت خودش در همان مدخل «فارسی نو sutamb-» را می‌آورد — تنها حلقهٔ فارسی میانه را نانوشته گذاشته است. هر سه معنای نورایی گواهی دارند: پوکورنی و باک «تندخو، ستیزه‌جو» و نوشین در «واژه‌نامک» «زشت‌رو، بدقیافه» می‌دهد و همان بیت ویس و رامین را که نورایی نقل کرده شاهد می‌آورد. ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"BQT\", \"status\": \"supports\", \"note\": \"Borhan vol. 2 p. 1100 s.v. ستنبه «بکسر اول بروزن شکنبه ... درشت و ستیزه‌کار ... و تند و خشمناک ... و مردم لجوج و بی‌آزرم را هم می‌گویند», with Mo'in's footnote «ستنبه = ستمبه. رک: استنبه، پارسی باستان stamba- ... ارمنی stambak». Nourai gives no page for this one and the page is right where his Old-Persian box points (BQT:1100).\"},\n            {\"ref\": \"FSF:223\", \"status\": \"partial\", \"note\": \"the entry is in Noushin's glossary — «ستنبه (بروزن شکنجه): زشت‌رو، بدقیافه» with the Daqiqi and Vīs-o-Rāmīn citations, FSF_pages.txt line 14835 — but in the local scan it falls near printed p. 399, not 223; the scan's edition/printing is not the Donya 1363 one Nourai cites, so the page number could not be confirmed. The content matches Nourai's gloss 'ugly' and his quoted couplet exactly.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD p. 77 s.v. stambag\", \"stance\": \"supports\", \"note\": \"'stambag [sthmbk' (-h- < stahm) | M ʾstmbg, N sitamba] oppressive; obstinate' — the direct Middle-Persian ancestor.\"},\n            {\"src\": \"FSF\", \"where\": \"Noushin, Vazhe-namak s.v. ستنبه (local scan p. ~399)\", \"stance\": \"supports\", \"note\": \"«ستنبه (بروزن شکنجه): زشت‌رو، بدقیافه» + «ستنبه دیو بدخو چه نمودت؟» (ویس).\"},\n            {\"src\": \"SYN\", \"where\": \"Buck p. 1363\", \"stance\": \"supports\", \"note\": \"'cf. NPers. sitamba \\\"violent, quarrelsome\\\" : Skt. stambha- ... lit. \\\"post, pillar, support\\\"'.\"},\n            {\"src\": \"POK\", \"where\": \"IEW 1012\", \"stance\": \"supports\", \"note\": \"'(compare np. sitamba \\\"violent, brutal, streitsüchtig\\\")' placed directly beside Skt. stambha-.\"},\n            {\"src\": \"ARY\", \"where\": \"Aryanpur, entry «ستنبه، ستمبه (به چم مرد درشت و قوی و دلیر)» (ARY_pages.txt, pdf page 347)\", \"stance\": \"supports\", \"note\": \"gives Old Persian/Avestan stamba-, Sanskrit stambha-, Armenian stambak and cross-refers «بازگشت به: ستبر» — the same family tree as this chart.\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"Sogdian\",\n          \"words\": \"`st`np\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Gharib no. 1679, p. 66: 'ʾstʾnp B — (ə)stamb, © <*stamba-; Parth. stʾmb; MP ʾstmbg — coarse, rough' (Buddhist Sogdian, BSTBL Dhy. 169; Benveniste, Notes iii 227), with the derivative no. 1680 'ʾstʾnpr'k — (ə)stambare — violent, cruel'. Sogdian script writes -np- for phonetic [mb], and the word carries the prothetic ʾ- Sogdian regularly puts before initial st-; the reconstruction Gharib gives, *stamba-, is the Old Iranian nasal stem of this root, so the arrow straight from the Indo-European box is correct (the Sogdian form is not mediated by Avestan or by Persian). Nourai's gloss 'strong, violent' fuses Gharib's 'coarse, rough' (1679) with 'violent, cruel' (1680), which is fair. The citation SOD:66 is exact — the page carrying the running numeral 66 is the one with entry 1679.\",\n          \"derivation_fa\": \"قریب در «فرهنگ سغدی» (مدخل ۱۶۷۹، ص ۶۶) می‌آورد: «ʾstʾnp (سغدی بودایی) — (ə)stamb، از *stamba-، پارتی stʾmb، فارسی میانه ʾstmbg — درشت، زبر»، و بلافاصله مدخل ۱۶۸۰ «ʾstʾnprʾk — (ə)stambare — خشن، بی‌رحم». در خط سغدی -np- نمایندهٔ آوای [mb] است و همزهٔ آغازین نیز واکهٔ افزودهٔ سغدی پیش از خوشهٔ st- است. صورتی که قریب بازسازی می‌کند، *stamba-، همان ستاک خیشومی ایرانی باستان از همین ریشه است؛ پس پیکانی که مستقیم از جعبهٔ هندواروپایی به این جعبه کشیده شده درست است. معنای «نیرومند، خشن» نزد نورایی ترکیبی از دو مدخل ۱۶۷۹ و ۱۶۸۰ است و ارجاع SOD:66 کاملاً دقیق است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"SOD:66\", \"status\": \"supports\", \"note\": \"SOD_pages.txt leaf NR=132, which carries the running numeral 66: '1679 ʾstʾnp B — (ə)stamb ©<*stamba-; Parth. stʾmb; MP ʾstmbg — coarse, rough — BSTBL, Dhy. 169; Benv. Notes iii 227' and '1680 ʾstʾnprʾk B — (ə)stambare — violent, cruel'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"SOD\", \"where\": \"Gharib nos. 1679-1680, p. 66\", \"stance\": \"supports\", \"note\": \"'<*stamba-; Parth. stʾmb; MP ʾstmbg' — the Old Iranian base, exactly the root of this chart.\"},\n            {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD p. 77 s.v. stambag\", \"stance\": \"supports\", \"note\": \"the MP ʾstmbg that Gharib cross-refers to: 'stambag ... oppressive; obstinate'.\"}\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"Germanic\",\n          \"words\": \"\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Empty pass-through box standing for Proto-Germanic. Watkins/AHD organises the Germanic material of this root in exactly the two shapes the box implies: from the basic aspirated form, Germanic *stab- (Old English stæf 'stick, staff'); from the unaspirated variant *steb-, Germanic *stap- (OE stapol 'post, pillar'; OE stæpe 'step') and the nasalised *stamp- (ME stampen; MLG stump). Verner's law and Grimm's law give *bʰ > Gmc *b, and the *b of *steb- gives Gmc *p, which is why 'staff' and 'step' look so different while belonging together. The AHD citation Nourai gives is the standard authority for the box.\",\n          \"derivation_fa\": \"این جعبه تهی است و تنها حلقهٔ ژرمنی آغازین را نشان می‌دهد. واتکینز در پیوست فرهنگ American Heritage همین دو شاخه را برای ژرمنی می‌آورد: از صورت دمیدهٔ *stebʰ- ژرمنی *stab- (انگلیسی کهن stæf «چوبدست») و از گونهٔ بی‌دمشِ *steb- ژرمنی *stap- (انگلیسی کهن stapol «ستون»، stæpe «گام») و گونهٔ خیشومی *stamp-. بر پایهٔ قانون گریم، *bʰ هندواروپایی در ژرمنی b و *b در ژرمنی p می‌شود؛ از همین‌روست که staff و step با اینکه هم‌ریشه‌اند چنین ناهمگون می‌نمایند. ادعای نورایی درست است.\",\n          \"sources\": [E_STAFF],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. stebh-: 'I. Basic form *stebh-. 1. Germanic *stab- in Old English stef, stick, rod: STAFF... II. Unaspirated form *steb-. 1. Germanic *stap- ... 2. Germanic nasalized form *stamp- ...'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. stebh- (AHD_watkins1985.txt line 1002)\", \"stance\": \"supports\", \"note\": \"explicitly reconstructs Germanic *stab-, *stap-, *stamp- under this root.\"},\n            {\"src\": \"POK\", \"where\": \"IEW 1011-1012\", \"stance\": \"supports\", \"note\": \"the Germanic section of the entry ('Old Saxon preterit stōp ... Old High German stapf ... Old Icelandic stafr ... Old English stæf \\\"staff\\\"') is the largest block of the lemma.\"},\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. staff (KLN_1966.txt line 36528)\", \"stance\": \"supports\", \"note\": \"'ME. staf, fr. OE. stæf ... rel. to OS. staf, ON. stafr ... OHG. stab ... All these words derive fr. I.-E. base *steb(h)-, \\\"to cause to stand, place, support; to step\\\".'\"}\n          ]\n        },\n        {\n          \"id\": 9,\n          \"lang\": \"English\",\n          \"words\": \"stamp, stump, staple, step, staff\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"All five are listed under stebh- in Watkins/AHD, and the AHD index confirms each of them word by word (STAFF¹ stebh-, STAMP stebh-, STAPLE¹/STAPLE² stebh-, STEP stebh-, STUMP stebh-). In detail: staff < ME staf < OE stæf 'stick, rod' < PGmc *stabaz (Klein: 'All these words derive fr. I.-E. base *steb(h)-'); step < OE stæpe (n.) / steppan (v.) 'to tread firmly' < PGmc *stap-, the unaspirated variant, the noun literally 'a treading firmly on, foothold'; staple¹ 'U-shaped fastener' < OE stapol 'post, pillar', and staple² 'chief commodity, market town' through Middle Dutch stapel 'pillar, foundation, emporium', same word; stamp < ME stampen < the nasalised Germanic *stamp- 'to pound' (cf. OHG stampfōn); stump < Middle Low German stump. The Germanic doublet *stab-/*stap- explains why the group is phonetically so varied. Etymonline gives staff the same root, 'PIE root *stebh- \\\"post, stem, to support, place firmly on, fasten\\\"'.\",\n          \"derivation_fa\": \"هر پنج واژه در پیوست فرهنگ American Heritage زیر همین ریشه آمده‌اند و فهرست الفبایی آن کتاب نیز یکایک آن‌ها را به stebh- بازمی‌گرداند. staff از انگلیسی میانهٔ staf و انگلیسی کهن stæf «چوب، عصا» و ژرمنی آغازین *stabaz است؛ step از انگلیسی کهن stæpe/steppan «محکم پا نهادن» و ژرمنی *stap- (از گونهٔ بی‌دمشِ ریشه)؛ staple از انگلیسی کهن stapol «ستون، پایه» (و در معنای «کالای اصلی/بازار» از راه هلندی میانهٔ stapel)؛ stamp از ژرمنیِ خیشومی‌شدهٔ *stamp- «کوبیدن»؛ و stump از آلمانی سفلای میانهٔ stump. همین دوگانگی *stab-/*stap- در ژرمنی است که ظاهر این واژه‌ها را تا این اندازه ناهمگون کرده است. کلاین و Etymonline نیز همین ریشه را می‌دهند. ادعای نورایی درست است.\",\n          \"sources\": [E_STAFF],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the box carries no reference of its own; it hangs off the Germanic box, whose citation is AHD, and that entry does cover all five words (Watkins 1985 s.v. stebh- and the index: 'STAFF¹ stebh-', 'STAMP stebh-', 'STAMPEDE stebh-', 'STAPLE¹ stebh-', 'STAPLE² stebh-', 'STEP stebh-', 'STUMP stebh-').\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985, index pp. 2281-2323 (AHD_watkins1985.txt lines 2281, 2283, 2293, 2311, 2323)\", \"stance\": \"supports\", \"note\": \"'STAFF! stebh-' ... 'STAMP stebh-' ... 'STAPLE! stebh-' 'STAPLE? stebh-' ... 'STEP stebh-' ... 'STUMP stebh-' — every one of Nourai's five.\"},\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. staff\", \"stance\": \"supports\", \"note\": \"'All these words derive fr. I.-E. base *steb(h)-, \\\"to cause to stand, place, support; to step\\\". See step and cp. words there referred to.'\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat s.v. Stave / Stem / Stiff (SKT.txt lines 18281, 18540)\", \"stance\": \"partial\", \"note\": \"'Cf. Icel. stafr, a stave; Dan. stav, staff' and, s.v. Stiff, 'Allied to Lith. stipras, strong ... also to E. Staff' — the same Germanic family, though Skeat's concise edition does not give the IE root-shape.\"}\n          ]\n        },\n        {\n          \"id\": 10,\n          \"lang\": \"Greek\",\n          \"words\": \"\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Empty pass-through box for the Greek branch. Watkins/AHD puts two Greek items under this root: from the basic form, 'Greek stephein, to tie around, encircle, crown, wreathe: STEMMA, STEPHANOTIS', and, as 'Variant *stabh-', staphulḗ 'grapevine, bunch of grapes'. Pokorny has the same Greek material under steb(h)- (a-sterphḗs 'unerschütterlich', stémphula, staphulḗ, and the -b- forms stémbō 'stamp, abuse'). The semantic bridge for stéphō is 'to fasten/tie firmly around' → 'to wreathe, crown'. It should be said that Beekes and Wiktionary treat staphulḗ as most likely Pre-Greek, and stéphō is not beyond doubt either; but AHD, Klein and Etymonline — the authorities Nourai's chart depends on — all keep stephein under *stebh-.\",\n          \"derivation_fa\": \"این جعبه نیز تهی است و تنها شاخهٔ یونانی را نشان می‌دهد. واتکینز دو دستهٔ یونانی را زیر این ریشه می‌آورد: از صورت پایه، stephein «گرداگرد چیزی بستن، تاج نهادن» (و از آن stemma و stephanotis)، و از گونهٔ *stabh-، staphulē «خوشهٔ انگور». پوکورنی نیز همین مواد یونانی را در همان مدخل دارد (a-sterphēs «تزلزل‌ناپذیر»، stémphula، stémbō). پل معنایی برای stéphō چنین است: «سفت گرداگرد چیزی بستن» ← «تاج و حلقهٔ گل بر سر نهادن». باید افزود که بیکس (Beekes) و ویکی‌واژه staphulē را به احتمال زیاد واژه‌ای پیشایونانی می‌دانند و دربارهٔ stéphō نیز تردید هست؛ اما AHD و کلاین و Etymonline، یعنی همان منابعی که نورایی بر آن‌ها تکیه دارد، stephein را زیر همین ریشه نگه می‌دارند.\",\n          \"sources\": [E_STEPHEN, W_PIE],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the Greek box carries no citation in the book; the English box below it cites AHD, and Watkins s.v. stebh- does supply the Greek link: '2. Greek stephein, to tie around, encircle, crown, wreathe: STEMMA, STEPHANOTIS.'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. stebh-\", \"stance\": \"supports\", \"note\": \"'2. Greek stephein, to tie around, encircle, crown, wreathe: STEMMA, STEPHANOTIS. ... III. Variant *stabh- in Greek staphulé, grapevine, bunch of grapes: STAPHYLO-.'\"},\n            {\"src\": \"POK\", \"where\": \"IEW 1012\", \"stance\": \"supports\", \"note\": \"'gr. a-sterphḗs \\\"unerschütterlich\\\" ... stémphula n. Pl. \\\"ausgepreßte Oliven oder Trauben\\\", staphulḗ \\\"grape, grapevine\\\"' — the Greek block of the lemma.\"},\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. stephano- (KLN_1966.txt line 36731)\", \"stance\": \"supports\", \"note\": \"'stephano- ... Gk. stephanos, \\\"that which encircles; crown; wreath\\\", fr. stephein, \\\"to encircle; to crown; to wreathe\\\". See stemma...' — Klein files stephein with stemma, i.e. with this root.\"}\n          ]\n        },\n        {\n          \"id\": 11,\n          \"lang\": \"English\",\n          \"words\": \"Steven , Stephen\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Greek stéphanos 'that which encircles; crown, wreath' — especially the victor's wreath at the public games — is the abstract noun to stéphein 'to encircle, wreathe, crown'. It became the personal name of the first Christian martyr (Acts 6-7), was latinised as Stephanus, and passed through Old French Estienne/Estievne into Middle English as Steven; the learned re-latinised spelling Stephen prevailed in writing while the vernacular pronunciation survives in the spelling Steven and in the surname Stevens/Stephenson. Klein s.v. Stephen: 'L. Stephanus, fr. Gk. Στέφανος, lit. \\\"crown\\\". See stephano-'; Etymonline traces the same chain and gives the PIE root as *stebh- 'post, stem; place firmly on, fasten'. Nourai's AHD citation is the modern standard for the root assignment (AHD files STEPHANOTIS and STEMMA under stebh-).\",\n          \"derivation_fa\": \"واژهٔ یونانی stéphanos «آنچه گرداگرد چیزی می‌پیچد؛ تاج، حلقهٔ گل» — به‌ویژه تاج گل پیروزی در بازی‌های همگانی — اسم مصدرِ فعل stéphein «گرداگرد بستن، تاج نهادن» است. این واژه نام نخستین شهید مسیحی (اعمال رسولان، باب‌های ۶ و ۷) شد، در لاتین Stephanus گشت، از راه فرانسهٔ کهن Estienne به انگلیسی میانه رسید و آنجا Steven شد؛ املای عالمانه و بازلاتینی‌شدهٔ Stephen در نوشتار چیره شد، حال آنکه تلفظ عامیانه در املای Steven و در نام خانوادگی Stevens/Stephenson بازمانده است. کلاین (ذیل Stephen) و Etymonline همین زنجیره را می‌دهند و ریشهٔ هندواروپایی را *stebʰ- می‌شمارند. ادعای نورایی درست است.\",\n          \"sources\": [E_STEPHEN],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. stebh-, I.2: 'Greek stephein, to tie around, encircle, crown, wreathe: STEMMA, STEPHANOTIS' — the name Stephen is not itself an AHD headword, but the Greek etymon and the root assignment Nourai needs are there; Klein supplies the name: 'Stephen, masc. PN. — L. Stephanus, fr. Gk. Στέφανος, lit. \\\"crown\\\". See stephano-.'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. Stephen and stephano- (KLN_1966.txt line 36732)\", \"stance\": \"supports\", \"note\": \"'Stephen, masc. PN. — L. Stephanus, fr. Gk. Στέφανος, lit. \\\"crown\\\". See stephano- and cp. Stephana.'\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. stebh-\", \"stance\": \"supports\", \"note\": \"assigns Greek stephein (whence stephanos) to this root.\"},\n            {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century Dictionary, s.v. Stephen\", \"stance\": \"silent\", \"note\": \"grep of WEB_vol1.txt for 'Stephen' returns only proper-name-derived entries (stephanite, stephanotis), no etymology of the personal name; recorded as silent.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\n\nwith io.open(\"/home/sfmqrb/git/rishe/data/verification/page-476.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(data, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"written\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/write476.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-476.json > /dev/null && echo \"JSON OK\" && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 476",
 "description": "Write and validate page-476.json"
}
```


### [2026-09-14T02:52:22.209Z] TOOL RESULT

```
written
JSON OK
nodes verified: 11/11
node verdicts: {'confirmed': 7, 'disputed': 2, 'plausible': 2}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 14, 'partial': 3, 'not_found': 1, 'not_checked': 2}
books consulted: {'supports': 29, 'partial': 5, 'contradicts': 3, 'silent': 1} | by book: {'PHD': 6, 'POK': 5, 'AHD': 4, 'KLN': 4, 'SOD': 3, 'NYB': 2, 'HRN': 2, 'ARY': 2, 'SYN': 2, 'BRT': 1, 'WLD': 1, 'HUB': 1, 'MON': 1, 'KNT': 1, 'FSF': 1, 'SKT': 1, 'WEB': 1}
```


## [2026-09-14T02:52:39.400Z] AGENT

**Page 476 (book p. 446) — one chart, root Stebh, 11 nodes. 0 PROBLEM lines.**

Verdicts: root confirmed · nodes 7 confirmed, 2 plausible, 2 disputed.
Ref checks: 14 supports, 3 partial, 1 not_found, 2 not_checked. 17 books consulted (POK, WLD, AHD, IEC, SYN, BRT, KNT, PHD, NYB, HRN, HUB, SOD, BQT v1+v2, MON, FSF, ARY, KLN, SKT, FVQ, WEB).

Disputed:
- **#2 Pahlavi `hôstubâr, astô-bâr` / `astô-bân`** — MacKenzie (CPD 14) and Nyberg read `ʾwstwbʾl` as *awestwār/ōstavār* and Nyberg says it is "not to be separated from ava-stā-", i.e. PIE \*steh₂-, not \*stebʰ-; `astô-bân` is MP *āstawān* 'confessing, professing' from Av. *stav-* (\*stew-). Nourai's ☞Bher / ☞Pa second elements are rejected. (`stapr, stawr` is fine — it is verbatim Horn no. 713.)
- **#3 Persian `ostovâr` / `ostovân`** — same reason; `setabr` and `estabrak` are fully confirmed (MP *stabrag* → Ar. *istabraq*, Qur'ān 18:31 etc., per Jeffery FVQ 58-60 and MacKenzie's own entry).

Plausible:
- **#4 Sogdian `stmb`** — word and gloss right (Gharib no. 8995), but Sogdian does not descend from Avestan; it continues Old Ir. \*stamba-.
- **#5 Old Persian `stambaka`** — not attested in Old Persian (absent from Kent); the -ka- form is MP *stambag*, whence Arm. *stambak*. `stamb` itself is confirmed by Kent p. 210 (*stabava*, DNa 60).

Book misprints (printed page checked, extraction is faithful — image saved to `data/verification/sources/refs/ocr/BOOK/476.png`):
- **`SOD:63` on node #4** should be **SOD:363** — Gharib's *stmb* is on p. 363, the same page Nourai cites correctly one box above. The page prints "SOD:63".
- `FSF:223` (node #6) could not be confirmed: the local scan puts ستنبه near p. 399; different printing. Content (Noushin's gloss «زشت‌رو، بدقیافه» + the exact Vīs-o-Rāmīn couplet) matches.
- `MON:240` / `MON:261,262` not turnable — the local Mo'in is the 2-volume Adena reprint with different pagination; the entries themselves were found and support the claims.

No extraction errors found: the JSON matches the printed page in every word, script form, gloss and citation.
