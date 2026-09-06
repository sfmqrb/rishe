# Verification process log — verify-page-248


## [2026-09-06T15:59:10.102Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 248 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-248.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-248.json. Write /home/sfmqrb/git/rishe/data/verification/page-248.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 248` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T15:59:11.751Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T15:59:12.458Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T15:59:12.471Z] TOOL RESULT

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


## [2026-09-06T15:59:12.646Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-248.txt"
}
```


### [2026-09-06T15:59:12.665Z] TOOL RESULT

```
1	=== PDF page 248 (book page 218) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Kei 2, Kie 2, Ki 1 : to set in motion  (refs POK:539)
4	#1 (parent #0) [Old Persian] refs=POK:539; HRN:172 | šiyav : to set in motion, march ; šaw : to go
5	  #2 (parent #1) [Pahlavi] refs=HRN:172 | šutan : to become
6	    #3 (parent #2) [Persian] refs=BQT:1261; FFD:62 | šodan «شدن» : to become | extra: شو ، تاشو
7	#4 (parent #0) [Avestan] refs=POK:539 | šav 2, šyav : to go ; šyaothna : conduct, effect ; šyaoman : action, work ; fra-šŭte : put in motion, moved
8	  #5 (parent #4) [None] refs=None | 
9	#6 (parent #0) [Greek] refs=POK:539 | kinein : to move ; kiněma : motion
10	  #7 (parent #6) [French] refs=AHD:243 | cinema : motion
11	    #8 (parent #7) [Persian] refs=MON:1985 | sînemâ «سینما» : cinema
12	    #9 (parent #7) [English] refs=None | cinema
13	  #10 (parent #6) [English] refs=None | kinetic
14	#11 (parent #0) [Latin] refs=AHD | ciěre : to move ; citâre : to put in motion, summon
15	  #12 (parent #11) [English] refs=None | citation, excite, solicit
16	--- entry 1 ---
17	ROOT Kei 3 -> redirect to Ak
18	
```


## [2026-09-06T15:59:15.702Z] TOOL CALL #3: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/data/extracted/batch/page-248.json; echo \"=== MATRIX ===\"; cat /home/sfmqrb/git/rishe/data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read page JSON and source matrix"
}
```


### [2026-09-06T15:59:15.748Z] TOOL RESULT

```
{
  "pdf_page": 248,
  "book_page": 218,
  "entries": [
    {
      "root": {
        "name": "Kei 2, Kie 2, Ki 1",
        "lang": "Indo-European",
        "refs": "POK:539",
        "gloss": "to set in motion"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Old Persian",
          "refs": "POK:539; HRN:172",
          "words": [
            {"translit": "šiyav", "gloss": "to set in motion, march", "script": null},
            {"translit": "šaw", "gloss": "to go", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "HRN:172",
          "words": [
            {"translit": "šutan", "gloss": "to become", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "BQT:1261; FFD:62",
          "words": [
            {"translit": "šodan", "gloss": "to become", "script": "شدن"}
          ],
          "script_extra": "شو ، تاشو",
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:539",
          "words": [
            {"translit": "šav 2, šyav", "gloss": "to go", "script": null},
            {"translit": "šyaothna", "gloss": "conduct, effect", "script": null},
            {"translit": "šyaoman", "gloss": "action, work", "script": null},
            {"translit": "fra-šŭte", "gloss": "put in motion, moved", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": null,
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Greek",
          "refs": "POK:539",
          "words": [
            {"translit": "kinein", "gloss": "to move", "script": null},
            {"translit": "kiněma", "gloss": "motion", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "French",
          "refs": "AHD:243",
          "words": [
            {"translit": "cinema", "gloss": "motion", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "Persian",
          "refs": "MON:1985",
          "words": [
            {"translit": "sînemâ", "gloss": "cinema", "script": "سینما"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 7,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "cinema", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 6,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "kinetic", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "ciěre", "gloss": "to move", "script": null},
            {"translit": "citâre", "gloss": "to put in motion, summon", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 11,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "citation, excite, solicit", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Kei 3",
        "redirect": "Ak"
      },
      "nodes": []
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


## [2026-09-06T15:59:40.256Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; ls; echo \"=== refs_online keys ===\"; python3 -c \"\nimport json\nd=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'))\nfor k in ['POK','HRN','BQT','FFD','MON','AHD']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:800])\n\""
}
```


### [2026-09-06T15:59:41.846Z] TOOL RESULT

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
NYB.txt
NYB_vol1.txt
NYB_vol2_glossary.txt
ocr
pageimg
PEI.txt
PHD_mackenzie.pdf
PHD_mackenzie.txt
PHD_pages.txt
PHD.pdf
PHD.txt
PHN.txt
POK_01.txt
POK_02.txt
POK_03.txt
POK_full.txt
RCH.txt
SBK.txt
SDQ.txt
SIN.txt
SKT.txt
SNS_pages.txt
SNS.txt
SOD_pages.txt
SOD.txt
SPG_keilinschriften1881.txt
SYN.txt
TAD_pages.txt
TAD.txt
tessdata
TLM.txt
UNV.txt
WEB_vol1.txt
WLD_band3.txt
ZAP.txt
=== refs_online keys ===
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<lea
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries ar
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/82307409
FFD {"title": "Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ماده-های-فعلهای-فارسی-دری-محسن-اب/ -> https://dl.eliteraturebook.com/app/public/attachments/6925d29630b83.PDF (free PDF site; grey)", "lookup_hint": "Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/download): nothing; only a related paid e-book 'واژگان زبان فارسی دری' (fidibo). ketabnak.com/book/45024 is a different book (فهرست فعلهای فارسی).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_asmaneketab.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/F
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifier": "watkins-american-heritage-dictionary-of-indo-european-roots-1985", "local_file": "/home/sfmqrb/
```


## [2026-09-06T15:59:46.042Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for n in 546 547 548; do echo \"===== POK_01 leaf $n =====\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1' POK_01.txt | head -70; done"
}
```


### [2026-09-06T15:59:47.638Z] TOOL RESULT

```
===== POK_01 leaf 546 =====
===== POK_01 leaf 547 =====
===== POK_01 leaf 548 =====
```


## [2026-09-06T15:59:49.933Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; wc -l POK_01.txt POK_02.txt POK_03.txt POK_full.txt; for f in POK_01 POK_02 POK_03; do echo \"$f pages: $(awk 'BEGIN{RS=\"\\f\"} END{print NR}' $f.txt)\"; done"
}
```


### [2026-09-06T15:59:51.695Z] TOOL RESULT

```
   5151 POK_01.txt
   6715 POK_02.txt
   5974 POK_03.txt
  93771 POK_full.txt
 111611 total
POK_01 pages: 363
POK_02 pages: 433
POK_03 pages: 429
```


## [2026-09-06T15:59:54.503Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for n in 194 195 196; do echo \"===== POK_02 leaf $n =====\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1' POK_02.txt | head -80; done"
}
```


### [2026-09-06T15:59:56.042Z] TOOL RESULT

```
===== POK_02 leaf 194 =====
köka-,  lit.  kaukti,  saukti,  slav. kukati  usw.)  Y.avv.aViag,  Y,avy.iaXogj  y.avy.LdXr,g  Vogelnamen  (Hes.) ;
536  f
aber  mcymr.  cuan,  cjmv.  cwan,  abret.  couann,  nbret.  kaouan,  dial.  cavan kotian,  kouhen  ds.  (Ernault  RC  36,  206  3)  sind  wohl  onomatopoetiscLe Neubildungen ;
lat.  (gall.)  cavannus  ^Nachteule'  (Anthol.  lat.);
ahd.  hüiüo  ,Eule^,  hüwila,  hiuwula  ^Nachteule^,  ahd.  hiuwilön  ,jubeln< mhd.  Muweln,  hiulen  ,heulen,  schreien^,  mnd.  hülen,  mengl.  hülen,  engl. howl ;
lit.  (s.  oben)  kaukiü,  kaükti,  lett.  käukt  ,heulen,  von  Hunden  oder  Wölfen', lit.  sukükti  jds.j  aufheulen^,  kaukaU  ^eine  Art  WasservogeP,  lett.  kaüka ;,Sturmwind^ ;
lit.  kövas  m.  _,Dohle^,  köva  f.  ^Saatkrähe'  (*käuä  =  poln.  kawa)-^
russ.  kdvka  ,Froscli^,  dial.  ^Dohle^,  kdvath  ^stark  husten',  klr.  (usw.) kdvka  ,Dohle^,  kavcdty  ^kreischen' ;  ablaut.  (*Ä:ew-)  bulg.  <^dvka,  serb.  ^ävha, öech.  cavka  , Dohle';  aksl.  kuja-jg,  -ti  ,murren';  russ.  kükath  ,murren, mucksen',  serb.  kükati  ,wehklagen'  usw.
Mit  -h~f  -h(h)o-:  ai.  kükkubha-  m.  , wilder  Hahn,  Fasan',  gr.  xovxovgpag ,Vogelart'  (spät,  kaum  echt  gr.);  schallnachahmend  sind:  y.i%vßog  wohl ,Nachteule'  (daneben  'Ai%y.aßrjy  yiUv^og  (daraus  lat.  cicuma),  xtxufi/g  ds., KL%7,aßav  ,deren  Schrei'),  lat.  cucuhiö,  -Ire  vom  Schrei  der  Nachteule (Thomas  Stud.  39  nimmt  Hiat  füllendes  h  an);  auch  die  i(Ä)-,Suffixe' der  vorgenannten  könnten  so  aufgekommen  sein.
Mit  -g-:  ai.  küjati  ,knurrt,  brummt,  murmelt';  norw.  Tiauke  ,johlen, rufen'.
Mit  -p-:  got.  liiufan  , wehklagen*,  anord.  hjüfra  ds.,  ags.  heofan  ds., as.  hiovan,  ahd.  hiofan^  Mob  an  ds.
Mit  -r-:  ai.  cdköra-  m.  ,eine  Art  Rebhuhn';  lat.  caurire  ,schreien,  vom brünstigen  Panther';  aksl.  kurz  ,Hahn',  ksl.  kurica  ,Henne';
Mit  anlaut.  Palatal:
Ai.  süka-  m.  ,Papagei';  arm.  sag  ,Gans'  (*kaua)  =  aksl.  sova  ,Eule' (:  kelt.  cavannus)]  lit.  saukiüj  §aükti  ,schreien,  laut  rufen,  nennen'; russ.  sycb  ,Zwergeule,  Sperlingseule',  cech.  syc  ,Eule'  (^kük-ti-)-,  unsicher aksl.  Surm  ,Geräusch'  (^IcEu-mo-s?  Brugmann  II ^  1,  247).
Vgl.  Suolahti  Dt.  Vogelnamen  185  (hier  über  die  Neuschöpfung  ahd. kaha  ,Dohle'  usw. ;  vgl.  lit.  kövas  usw.  ds.).
WP.  I  331  f.,  WH.  I  184,  190,  298,  Trautmann  122.
kau{9)lä  :  külä  ,Geschwulst;  bes.  Leibschaden,  Leistenbruch'.
Gr.  ion.  xrjlr],  att.  xdlr]  ,Geschwulst,  bes.  Leibschaden',  ßovßcovo-Ki^Xfj ,Leistenbruch'  u.  dgl.;  xala^ec  dyxoürai.  ""Axaioi  Hes.,  xc^Aa^ta*  5'yxog  Hes. (vokalisch  sehr  schwierig;  ion.  ytrjlr]  aus  Haf-sX-a,  att.  ach.  'a&I-^,  -5  aus
Y.äJ^-eX-a  ?) ;
537
anord.  haull,  ags.  heala,  abd.  höla  L  ^Leistenbruch^  {*käu[9]läy  allen- falls *kdu[d]lä)]
tiefstufig  ksl.  kyla  ^ds/ ;  russ.  kild  ,ds. ;  Knorren  am  Baum^,  serb.  klla ds.
===== POK_02 leaf 195 =====
;  lit.  dial.  knie  f.  ^AuswuchS;  Knorren^
WP.  I  333,  Trautmann  144.
^au-1-,  ku-1-  ,hohl;  Hoblstengel;  Röhrenknochen^
Gr.  Y.avX6g  m.  ^Stengel;  Federkiel,  Schaft^;  lat.  caulis  (^cölis,  caulus) ^Stengel,  Stiel  an  Pflanzen^;  mir.  cuaille  ,PfahP  {*kaullnio-) ]  lit.  kdulas m.  ,Knochen^  (Stoßton  sekundär),  lett.  kaüls  ,Stengel,  Knochen^,  apr. caulan  n.  ,Knochen,  Bein^
Schwundstufig:  ai.  külyam  n.  , Knochen^,  kulyä  f.  _,Bach,  Graben,  KanaF; anord.  liolr  ,hohP,  ahd.  ags.   hol  ds.,  got.  ushulön  ,aushöhlen^
WP.  I  332,  WH.  I  188  f.,  Trautmann  122;    vgl.  unter  2.  keu-.
kaus-  ,das  Los  ziehen^?
Gr.  y^avvog  ,Los^  (*yLccva-vog) ;  ksl.  k^h  m.  ,Los',  Hsiti  s^  ,losen^,  prekzsiti ,im  Würfelspiel  gewinnend WP.  I  332,  Berneker  672.
ke-  s.  unter  ko-,
ked-  ,rauchen,  rußen*.
Ai.  kadrü-  , braun*,  vielleicht  auch  kadamba-  m.  ,Nauclea  cadamba, ein  Baum  mit  orangefarbenen  Blüten'  und  kädamha-  m.  ,eine  Gansart mit  dunkelgrauen  Flügeln*;
aksl.  kadilo  ,Räucherwerk^,  kaditi  ,räuchern*,  russ.  cad  , Dunst*,  serb. 6ad  jcaligo*,  caditi  , rußig  werden*  (usw.,  s.  Berneker  133,  467),  vielleicht apr.  accodis  (^at-codis)  , Rauchloch,  durch  das  der  Rauch  herauszieht* ;
als  , Räucherhölzer*  sind  anzureihen  (?):
gr.  TciÖQog  ,Wacholder;  später:  Pinus  cedrus',  -asögig  ,Wacholderbeere ; Frucht  der  Zeder*;  lit.  kadagys,  apr.  kadegis  , Wacholder*  (aus  estn.  kadakas entlehnt?).
WP.  I  384f.,  Trautmann  112,  Specht  Idg.  Dekl.  147.
keg-y  keng-  und  kek-,  kenk-  , Pflock  zum   Aufhängen,   Haken,    Henkel*; auch  ,spitz  sein*;  vgl.  das  ähnliche  kak-^   kank-]  und  kenk-^  konk-, Npers.  (iang  , Klaue,  Faust*  (*kengo-)',
mir.  ail-ctieiig  f.  ,Rechen,  Waffengestell*  ( :  lit.  kenge,  s.  unten) ;
germ.  *hakan-j  *h5ka-,  *hekan-  m.  ,Haken*  in:  aisl.  PN  Haki  m.  , Haken*,
haka   f.  ,Kinn',   ags.  haca   m.   ,Riegel*,   hcecce  f.  ,Krummstab*;   aisl.   häkr
m.  jFrechling*,  ahd.  häko,  häggo  ^Haken^,  ags.  höc  m.  ,Haken*,  mnd.  hok^
huk    m.    ,Winkel,    Ecke,  Vorgebirge*,    aisl.    hekja    f.  (*hökiön-)   , Krücke',
538  •
heUll  m.  ,Hinterbug*;  mit  intensiver  Gemination:  ags.  haccian  ,liackeu* mnd.,  mhd.  hacken  ds.,  und  die  ^-Verba:  a^s.  ofhceccan  ,amputareS  ahd. hecchen  ,beißen,  stechenS  mhd.  hecken  , hauen,  stechen*;  nasaliert  mnd. hank  ,Henkel*  (daraus  aisl.  hgnk  m.,  hanki  f.  ,Henkel'),  ndl.  honk,  ostfries. hunk  ,Pfahl,  Pfosten';
germ.  *hakilö  f.  ,Hechel'  (von  den  gekrümmten  Eisenzähnen)  in:  asächsj hekilon  ,hechelnS  engl,  hatchel,  mhd.  hechel  ^Hechel\  norw.  hekla  ,Hech
===== POK_02 leaf 196 =====
el, StoppeP ;
germ.   *häkuda-  m.  ,Hecht'  (nach  den  spitzen  Zähnen)  in  ags.  hacodA *hakida  in  ags.   hacid  m.,  ahd.  hacMt,  hechit,  mnd.   heket  ^Hecht^^
lit.  kenge  f.  , Haken,  Klinke';
slav.  *kog^th  m.  in  russ.  kögoth  ,Klaue,  gekrümmte  Eisenspitze^,  osorb. kocht  ,Dorn,  Stachel'  (:  germ.  *hakuda-)-
vielleicht  hierher,  als  ,au£  einen  Haken   hinaufhängen,  wie  mit  einei Haken   kratzen,   reizen':   bulg.  kdcbj  kdc(ii)vam   ,erhebe,   erhöhe,    hänge*^ za-kdchj   -kdcam   ,hänge,    fasse,   necke',    serb.    zäkaciti    ,anhaken',   sloven. kdclti  ,necken,  ärgern'  (Berneker  465  f.).
WP.  I  382  f.,  WH.  I  307,  Trautmann  112,  Wissmann  Nom.  postverb. 182  f.,   Petersson,  Heterokl.  9 1  f . ;   Stokes  BB.  25,  252.
•'« kei-    ,in    Bewegung    setzen,    in    Bewegung   sein'    (:    koi-  :  kf-);    eu-Basis] (z.  T.  mit  22-Infix)  ki-{n-)eu-;  schwere  Basis  kiQ-  (:  Jcie-?).
Gr.  xio)  ,gehe  weg,  fahre'  ist  späte  Neubildung  zum  Aor.  e/.LOv]  Imper.i Y.U,  Partiz.  xiwy;
hom.  Präteritum  fxsr-sytiad-s,  -d-ov  {i  metr.  Dehnung)  , folgte  nach,  durch- streifte', Y.iazo'  s-ALvelvo  Hes.  (schwere  Wz.);  dvo-ytlvÖLog,  -y.lvöag  ,Esel- treiber',  y,Lvda^  , beweglich,  ei'nivrjTog''  (vgl.  zur   Bildung  äXlvdo),  ytvXlvdüijy
von  ki-n-eu-  :  gr.  y.tvv^ai  , werde  bewegt,  erschüttert,  gehe',  yavvaaoy,ai, ,sch wanke  hin  und  her',  '/.ivio)  ,setze  in  Bewegung,  treibe'  (*xlv«J^-ü>) ;
alb.  q^oj  , wecke,  erwecke'  (*kien{ö)j  qoj  , schicken,  senden'  (*ds-köj\ cys,  cyt  , reize,  necke'  (*ter-k{u-t-{ö),  syei^  syen  (*kiu-n-iö)  ,bestürmen,  an- fallen' (Jokl  Mel.  Pedersen  149 f.');
lat.  cieöj  eiere  (sekundär  ciö,  clre)  ,in  Bewegung  setzen,  rege  machen, herbeirufen'  (eiere  =  idg.  ki(i)e-??)j  citus  ,schnell',  cito,  -äre  ,in  Bewe- gung setzen,  kommen  lassen,  vorladen',  solli-citus  ,ganz,  stark  bewegt, beunruhigt,  in  Angst  und  Gefahr',  cunctus  (*con-citos),  gesamt,  sämtlich*.
Erweiterungen  von  der  einfachen  Wurzelform  kei-  aus :
Mit  d  (cZ-Präsens?):  vielleicht  ir.  cid-  z.  B.  mcisse  ,invecta',  Pass.  Konj. as-cesar   gl.    ,exseri'   (usw.,  Pedersen  KG.  II  490  f.),   sehr   wahrscheinlich  "^ got.  haitanj  ahd.  heisan,  ags.  hätan,  as.  hetan,  anord.  heita  ^heißen  {j=  aa- treiben),  befehlen,  anrufen,  nennen^;   vgl.  osset.  sidin  , rufend
I
539
Mit  i(o)- Formans:  Auf  *kEi-lo-s  ,bewegt,  wippend'  kann  beruhen:  lit. Jctele,  kyU,  lett.  cielaioa^  apr.  kylo  , Bachstelze',  acech.  cily  ,lehhaft';  lat. cillö,  -ere  , bewegen'  ist  vielleicht  nur  Grammatikererfindung.
Mit
```


## [2026-09-06T16:00:01.670Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for n in 197 198; do echo \"===== POK_02 leaf $n =====\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1' POK_02.txt | head -60; done"
}
```


### [2026-09-06T16:00:03.474Z] TOOL RESULT

```
===== POK_02 leaf 197 =====
 s:  ai.  cistati  ,bewegt  die  Glieder,  ist  in  Bewegung',  cesta- n.j  cestä ^Bewegung,  Gebärde'.
Wurzelform  ki-eu-  ohne  Nasalinfix:
ai.  cydvate  ,regt  sich,  geht  fort',  av.  5(y)avaite  ,setzt  sich  in  Gang, Marsch',  apers.  asiyavam  ,marschierte',  ai.  cyautnd-  n.  ,Unternehmung, Bemühung',  av.  syaod-na-  n.  ,Tun,  Handeln,  Wirken',  syaoman-  n.  ,Tat, Werk';
arm.  cu  (=  ai.  cyuti-)  , Aufbruch',  cvem  ,ich  breche  auf,  reise  ab',  Aor. (zum  Präs.  ert'am)  cogay  ,ich  ging'  (^kioit-)-,
gr.  Gsvo)  ,setze  in  rasche,  heftige  Bewegung',  Med.  ,eile,  bin  erregt' (aevstai  =  cyavate]  der  Diphthong  kann  nach  den  außerpräs.  Formen und  nach  unthemat.  Gevxai  festgehalten  sein),  hom.  saavTO  ,eilte',  Partiz. Perf.  ioav^svog,  iTvl-aavTog  ,herandrängend,  daherstürmend'  (=  ai.  cyutä- ,getrieben',  vgl.  av.  fra-süta-  ,in  Gang  gekommen*),  Ttav-avöir]  ,in  Eile'; att.  aovfxai  , bewege  mich  rasch  oder  heftig'  (^aoföofiaij^  avsi  (Bacchyl.) ,treibt',  iaoorjixevov  TsdoQvßri^hov,  öq^Tjjj^vov  Hes.,  hom.  Xao-Gaöog  ,die Völker  zum  Kampfe  antreibend';  att.  T€Vjj,ü)i.iaL  ,betreibe'  (vgl.  av.  syao- man-)-,  Tsvrd^u)  ,beschäftige  mich  anhaltend  mit  etwas';  eine  Dehnstufen- bildung wie  ai.  cyautnd-^  aber  rnit  geschwundenem  u^  ist  das  wohl  hierher gehörige  gcjtqov  ,das  hölzerne  Rad',  kTtlaooiXQOv  ,Radreifen'.
WP.  I  361  ff.,  WH.  I  213  f.,    Schwyzer  Gr.  Gr.  I  679,  686,  745.
I.'  kei-  ,liegen ;  Lager,  Heimstätte,  traut,  lieb  (von  derselben  Siedlung') ; koi'to-  , Lager' ;  kei-mo-,   koi-mo-  , vertraut',    kei-uo-,  ki-uo-   ds.
Ai.  süe  (älter  sdye)^  3.  PI.  sei%  av.  saUe  (:  gr.  -KelxaL)  ,liegt',  3.  PL sözVe,  ai.  sayate,  -ti  ,liegt,  ruht',  §ayä,  sayyä  , Lager',  madhyama-si-  ,in der  Mitte  sich  lagernd,  liegend',  ni-sl-tlia-  m.  »Mitternacht',  usw. ;
gr.  Y,sZTai  jliegt',  3.  PL  -/.eazai  aus  *xejnt-j  umgebildet  nach  y.sl-,  hom. xelaTat]  jung  ist  hom.  -Asoviai  (:  ai.  sayante)]  '/.oZxog  m.,  xotr^  f.  , Lager', äy,OLTig  , Gemahlin'  (mit  ion.  Psilose  aus  *&'-xoiTi$);  vgl.  bret.  {d)argud ,leichter  Schlaf  (^-are-koito-)]  v.oi^da)  , bringe  zu  Bett,  schläfere  ein'  (vgl. got.  haims,  air.  cöim,  lett.  säimey  auch  lit.  seimyna,  ags.  hceman).  Zweites Kompositionsglied  -x^-o-  in  Ttsqioöog,  vsoaaög,  u.  dgl.  Sehr  wahrscheinlich lat.  cünaej  cün
===== POK_02 leaf 198 =====
äbula  PL  , Wiege  ,Nest'  (*koi-na)  und  anord.  hldj  hidi  n. ,Lager  des  Bären'  (*kei-to-)',
hitt.  Mediopassiv  ki-it-ta  (kitta)  und  ki-it-ta-ri  (kittari)  ,liegt' ;  vielleicht auch  lyk.  sijeni  ,liegt'  (Pedersen,  Ljkisch  u.  Hitt,  17).
Mit  dem  Begriffe  ,Heim,  traut,  lieb':
540  •
mit  i-Suffix  ai.  Hla-  n.  , Gewohnheit,  Charakter*,  air.  ce{i)le  , Genosse, Gatte*  (*kei-U{o-s\  mit  sekundärem  i  cymr.  cilydd  , Genosse*,  usw.;
mit  i22-Suffix:
gr.  7ioi(.iaa)  (s.  oben),  yLsmrjhov  ,aufbewahrtes  Gut*  (von  *%aliia  n.  ,Lager*)' dehnstufig  xcj.aiy  f.  ,Dorf*  (*^ö[i]mä);
air.  com,  cöem  ,lieb*,  acymr.  cum^  ncymr.  cu  usw.  ,lieb*  (koimo-);
got.  haims  f.  (z-St.)  ,Dorf,  Flecken ;  PI.  dygoi^  anord.  heimr  m.  ,Heimat Welt*,  ping-heimr  ,die  beim  Thing  anwesende  Versammlung*,  ags.  häm as.  kern,  ahd.  heim  , Heimat,  Haus,  Wohnung*  (ags.  hceman  ,beschlafen heiraten*,  ursprüngl.  ,y.oifiav^)]
lett.  säime  f.  , Hausgesinde,  Familie*,  ablaut.  lit.  seimyna  i.,  apr.  seimim m.  , Gesinde*;
aksl.  sembja  , Gesinde,  Sklaven*,  semim  ,zum  Gesinde  Gehöriger,  Sklave**
lit.  kiemas  ,Bauernhof*,  kdimas  ,Dorf*,  lett.  ciems  ,Dorf,  Versammlungs- haus*, apr.  caymis  ,Dorf*,  lit.  kaimynas  ,Nachbar^,  kalmene  ,Herde*  sind der  Entlehnung  aus  germ.  *hai'maz  verdächtig;
Trautmann  (112  f.)  nimmt  ablaut.  urbalt.  *kaima-  ra.  und  *köimä  f.  an (idg.  öi :  ai);
mit  ro-Suffix:  arm.  ser  ,Neigung,  Liebe*,  sirem  ,ich  liebe*  (*keiro-)]
mit  uo-Suffix:  ai.  siva-  (=  germ.  Mwa-)  ,traut,  freundlich,  lieb,  wert*, iivd-  (=  germ.  *hiiüa-)  ,vertraut,  lieb,  .heilsam* ;
lat.  clvis  ,Bürger*  =  osk.  ceus  ds.;  die  i-Flexion  nach  hostis  (M.  Leumann Gnomon  9,  237) ;
got.  heuva-frauja  , Hausherr*,  ags.  hlw-cund  ,heimisch*,  hiw-rößden  f. , Haushaltung^,  ahd.  hl-rat  ^Heirat^  ags.  hl-red  ds.,  agutn.  hl-skepr  , Familie*, anord.  hy-hyli  Neutr.  Fl.  ,Hauswesen*  (daneben  ablaut.  *hiwa-  =  ai.  Hvd- in  anord.  herad,  aschwed.  hce-rap  ,Bezirk*,  hce-skaper  ,Familie*  aus  ^Mwa-)] der  germ.  St.  *hiwa-  ist  Kompositionsform  zu  ^hiwan-  ,Hausgenossen  (schaft)* in  anord.  hjü{n\  hjön  ,Ehepaar,  Dienerschaft,  Ge
```


## [2026-09-06T16:00:41.856Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== AHD watkins kei ===\"; grep -n -i -E \"^ *kei-?[0-9]|kei-2|kinein|kinema|solli-?citus|ciere\" AHD_watkins1985.txt | head -40"
}
```


### [2026-09-06T16:00:41.950Z] TOOL RESULT

```
=== AHD watkins kei ===
599:kei-2, Referring to various adjectives of color. 1. Suffixed o-grade form *koi-ro- in German *hairaz, “gray-haired,” old, venerable, hence master, in: a. Old English har, gray, hoary: HOAR; b. Old High German hér, worthy, exalted: JUNKER; Cc. Middle Dutch here, master, lord: YOUNKER. 2. Suffixed zero-grade form *ki-wo- in Germanic *hiwam in Old English hiw, héo, color, appearance, form: HUE}. [Pok. 2. Rei- 540.]
600:kei-3. To set in motion. I. Possibly extended o-grade form *koid- with suffixed form *koi-d-ti- in Germanic *haissiz in: a. Old English h&s, a command, a bidding: HEST; b. Old English compound beh#s, a vow, promise, com- mand (be-, intensive prefix; see ambhi): BEHEST (but perhaps to be referred to a separate root *kaid-). Il. Zero-grade form *ki-. 1. Form *ki-eyo- in Latin ciére (past participle citus), with its frequentative citdre, to set in motion, summon: CITE; EXCITE, INCITE, OSCITANCY, RESUSCITATE, SOLICITOUS. 2. Suffixed form *ki-neu- in Greek kinein, to move (> kinésis, motion): KINEMATICS, -KINESIS, KINETIC; CINEMATOGRAPH, CINEMATORADIOG- RAPHY, HYPERKINESIA, KINESIOLOGY, KINESTHESIA, KININ, (TELEKINESIS). [Pok. kei- 538.]
1626:HOAR kei-2
1657:HOYDEN kalto- HUBRIS ud- HUCKSTER keu-2 HUE! kei-2 HUGUENOT neud-, oito- HULL kel-2
1707:JOY gau- JUBILATE yu-2 JUDGE deik-, yewes- JUDICIAL deik- JUGATE yeug- JUGGERNAUT gWa- JUGGLE yek- JUGGLER yek- JUGULAR yeug- JUGUM yeug- JUICE yeue- JULEP ap-2, wrod- JuLY deiw- JUNCTION yeug- JUNCTURE yeug- JUNIOR yeu- JUNKER kei-2, yeu- JUNTA yeug- JUPITER deiw- JURAL yewes- JURIDICAL deik-, yewes- JURISCONSULT yewes- JURISDICTION deik-, yewes- JURISPRUDENCE yewes- JURIST yewes- JURY! yewes- JUSSIVE yeudh- susTl yewes- JusTiFy dhé-1
1716:KIND! gene- KIND? gene- KINDERGARTEN gene-, gher-1 KINDRED af-, gene- KINE gWou- KINEMATICS kei-3 KINESIOLOGY kei-3 -KINEsIS_ kei-3 KINESTHESIA kei-3 KINETIC kei-3 KING gene-
```


## [2026-09-06T16:00:52.641Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== AHD kyeu ===\"; grep -n -i -E \"kyeu|kiy-?eu|seue-|SEUE\" AHD_watkins1985.txt | head -20; echo \"=== HRN leaf 193 (p.172) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==194' HRN.txt | head -60"
}
```


### [2026-09-06T16:00:54.635Z] TOOL RESULT

```
=== AHD kyeu ===
135:The Indo-Europeans knew snow in their homeland; the word sneig”h- is nearly ubiq- uitous. Curiously enough the word for “rain,” however, varies among the different branches; we have words of differing distri- bution like seue-?, ombh-ro- and reg-?.
154:A large number of kinship terms have been reconstructed. They are agreed in pointing to a society that was patriarchal, patrilocal (the bride leaving her household to join that of her husband’s family), and patrilineal (de- scent reckoned by the male line). “Father” and “head of the household” are one: peter-, with his spouse, the mater-. These terms are ultimately derived from the baby-talk sylla- bles pa(pa) and ma(ma), but they had a socio- logical significance in the Indo-European family over and above this, which is marked by the kinship-term suffix -ter-. Related terms are found for the grandfather (awo-) and the maternal uncle (*awon-), and corre- spondingly the term nepét- (feminine *nepti-) applied to both grandson (perhaps originally daughter’s son) and nephew (sis- ter’s son). English soON and DAUGHTER clearly reflect Indo-European *siénu- (from seue-') and dhughater-.
931:seue-', To give birth. Suffixed zero-grade form in deriva- tive noun *su(2)-nu-, son, in Germanic *sunuz in Old English sunu, son: SON. See also su-. [Pok. 2. seu- 913.]
932:seue-2, To take liquid. I. Suffixed zero-grade form
1034:sii-. Pig. Contracted from *sua-; probably a derivative of seue-'. 1. Suffixed form *sua-ino- in Germanic *swinam in Old English swin, swine: SWINE. 2. Celtic expressive form *sukko-, swine, snout of a swine, plowshare, in: a. British *hukk- in Old English hogg, hog: HoG; b. per- haps Old French soc, plowshare: SOCKET. 3. Germanic *sii- in Old English sugu, sow: sow?. 4. Latin sis, pig: soit’. 5. Greek hus, swine: HYENA; HYOSCINE. [Pok. su-s 1038.]
1691:Is es- ISALLOBAR gWere-2 ISCHEMIA segh- ISINGLASS bhié-2 ISLAND akwa- ISOBAR gWere-2 ISOCLINE klei- ISOGLOss glogh- ISOHEL sawel- ISOHYET seue-2 ISOMER (S)mer-2 ISOMETRIC mé-2 ISOPIESTIC sed-1 ISOPLETH pele-1 ISOSCELES skel-3 IsosTasy sta- ISSUE ei-1
2261:SING sengh- SINGE senk- SINGLE sem-1 SINGSPIEL sengWh- SINISTRORSE wer-3 SINK seng¥- SINN FEIN s(w)e- SINTER sendhro- SIP seue-2
2276:SoL sdwel- SOLACE sel-2 SOLANINE sAwel- SOLAR sawel- SOLARIUM sawel- SOLE! sel-1 SOLE? s(w)e- SOLEMN sol- SOLICITOUS_ kei-3, sol- SOLID sol- SOLILOQUY s(wW)es, tolkw- SOLIPSISM s(w)e- SOLITARY s(w)e- SOLITUDE s(w)e- SOLO s(w)e- SOLSTICE sawel- SOLUBLE leu-1 SOLUM sel-1 SOLUTE leu-1 SOLVE leu-! SOMA teue- SOMATO- teua- SOME sem-! -SOME! sem-1 -SOME2  teue- SOMERSAULT sel-4, uper SOMNI swep-! SOMNOLENT swep-! SON seue-! SONANT swen- SONATA swen- SONE swen- SONG sengWh- SONIC swen- SONNET swen- SONOROUS swen- sooT sed-1 SOOTH es- SOOTHE es-
2277:SOP seue-2 SOPOR swep-1 SOPORIFIC swep-1 SOPRANINO uper SOPRANO uper SORCERER ser-3 SORDID swordo- SORDINO swer-2 SORE sai- SORITES teue- SORORAL swesor- SORORITY swesor- SORREL! siiro- SORREL? saus- SORROW swergh- SORRY Sai- SORT ser-3 SORTILEGE leg-1, ser-3 SORUS teue- SOTERIOLOGY teue- SOUBRETTE uper SOUFFLE bhlé-2 SOUGH (s)wagh- SOUND! swen- SOUND2 swento- SOUND3 swem- SOUND4 swem- SOUP seue-2 sOUR siiro- SOURDINE swer-2 SOUSE sal-1 SOUTANE upo SOUTH sawel- SOUTHERN sawel- SOUVENIR gWa- SOVEREIGN uper SOVIET sem-! sow! sé-1
2324:SUCK seue-2 SUCTION seue-2 SUCTORIAL seue-2 SUDATORIUM sweid-2 SUDDEN ei-1 SUDORIFEROUS sweid-2 SUDORIFIC sweid-2 suDs_ seut-
2326:SUMMON men-! sUMP swombho- SUMPTUARY em- SUMPTUOUS em- SUN sawel- SUNDAY sawel- SUNDER sen-2 SUNDRY sen-2 SUP! seue-!
2327:suP2 seue-2 SUPER- uper SUPERABLE uper SUPERANNUATED at- SUPERB uper SUPERCILIOUS kel-2 SUPERCILIUM kel-2 SUPEREROGATE reg-' SUPERFETATE dh@(i)- SUPERFLUOUS bhieu- SUPERIOR uper SUPERJACENT yé- SUPERLATIVE tele- SUPERNAL uper SUPERNATANT sna- SUPERNUMERARY _nem- SUPERSCRIBE skribh- SUPERSEDE sed-1 SUPERSTITION sta- SUPERVENE gWa- SUPERVISE weid- SUPINE! upo SUPINE? upo SUPPLANT plat- SUPPLE plek-, upo SUPPLICATE plek- SUPPLY pele-1 SUPPORT per-2 SUPPOSE apo- SUPPRESS per-5 SUPPURATE pu-2 SUPRA- uper SUPRALAPSARIAN leb-1 SUPREME uper SUPREMO uper SUR- uper SURCULOSE swer-3 SURD swer-2
=== HRN leaf 193 (p.172) ===
— 172 -
phlv. östaftan ') (vd. 7 (27) GL, 18 (98), Meii.) eilen,
arm. LW. staij, davon Denomin. stapim 'eilen.
aw. *aiwis + l^tap-, täpaj/eiti *iri Wärme, Hitze
bringen', dann tropisch-).
Zu aiwis vergl. oben np. hes- (No. 221).
778. sHden gehen; sein, werden', Praes. sev-em.
ap. \/^siya€', aslt/avam, asiyuva 'gehen, marschiren';
aw. {/sav-, suvaite'^) gehen'; ai. [/^cyav-, Ci/dvate 'fort-
gehen ; arm. cit 'Aufbruch', ciiem 'aufbrechen' (H.
No. 242).
kurd. eleu 'gehen', dicm; sify, soal 'werden, gehen';
oss. d. t. cäün 'gehen, schreiten, spazieren, fahren'
(319) ; bei. suta, siit, n. suöa, iud^a (322) ; wa;^. cduam,
si/n. oi\zafcam, sar. va]zevsam.
779. siirrän, serrün 'unablässig lliessend', slrän Kegen' (y),
sun-iden^), vergl. sär {äbsär), särulen, ,
ai. l^ksar-, ksdrati 'fliessen, strömen' (Geiger,
Etym. d. Bai. unter No. 66; bei. ö[ur 'Giessbach'
kann aber nicht verglichen werden, s. Htibsch-
mann, ZDMG. 44, 556).
780. Herrn 'Schaam'.
aw. fsarema- 'Schaam'; phlv. sarm *Schaam', sarm-
[gas 'Genitalien' (vd. 16 (5) Gl.).
oss. t. äfsdrm, d. äfsänni 'Schande' (121) ; LW. aty.
bei. (253) sarm 'Schaam', kurd. serm,
781. sest, sest 'sechzig*.
aw. yscasti- 'sechzig ; päz. säst (FPGl.); ai. saüi-,
kurd. FD. LW. sest; afy. speta,
782. susten Vaschen', Praes. söy-em^),
phlv. sustan, söyBnd^ söy(i)sn; kurd. LW. sustin
'waschen' (vergl. g. sustinUu neben sustmün) ; bei.
*) Pfiz. qastäftun^ qastäwidan (Men.) ist Unsinn.
*) An ursprüngliches ^sila^ten (vergl. jjuft aus jf*x^) darf man
wegen Praes. siiäb-em natürlich nicht denken.
^) Bartholomae, Ar. Forsch. III, 33 liest staitc.
*) Zum Teil unbelegt.
^j Reimt auf higöyetl, Vis und Rämln S. 70 Vers 6.
```


## [2026-09-06T16:01:04.585Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== KNT šiyav ===\"; grep -n -i -E \"siyav|šiyav|siyuv|asiyav\" KNT.txt | head -30; echo \"=== BRT šyav ===\"; grep -n -E \"syav|šyav|s\\'av|syao.na|syaoman|fra-suta|frasuta\" BRT.txt | head -40"
}
```


### [2026-09-06T16:01:04.659Z] TOOL RESULT

```
<persisted-output>
Output too large (32.6KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/tool-results/b4qzmj7qn.txt

Preview (first 2KB):
=== KNT šiyav ===
1402:‘death’, cf. -30- in OP martiya ‘man’. adurujiya ‘he lied’, cf. drauga ‘the Lie’. asiyava ‘he went forth’, Skt. (mid.) deyavala.
2583:II. The secondary ending was pIE -nt, which - lost the final ¢ in pAr. unless sentence phonetics ` permitted its retention; for in pAr. only a single consonant could stand at the end of a word. In OP, also, the final n was not written (§112). Be- fore this ending the thematic vowel was -o-: pIE *ebheront, Gk. égepov, Skt. dbharan, OP abara”; OP abava", anaya”, ayauda", asiyava", alarsa”, agar- báya"; passive арата", ayadiya". Non-thematic stems would normally have pIE -nt after conso- nants, becoming pAr. -at; but this was commonly replaced by -an(t) after the -am of the Ist sg.: pIE *és-nt, but Skt. азат, ОР аһа”; OP apariy- diya”, avájana",
2668:G. To express the goal; names of places are often used thus without a preposition (regularly with fra-ais-, ar-, ava-ar-, pard-ar-, Siyav-), but names of persons always have the preposition: DB 8.82 abiy avam Аттат asiyava Babirum; exception DB 5.21f a&yavam abiy Saküm, cf. DB 2.72, 3.73f (Styav-), 2.721 (fra-ats-), DB 5.23f (ava-ar-), DPe 24 (ni-ar-). With ay- ‘go’ places as well ав persons take prepositions, ef. DB 1.91f, 3.73, DZe 11 for places, DB 1.93, 2.32f for persons.
2711:A. With hada, to denote accompaniment either friendly or hostile: DB 2.21f pasdva haw Vidarna hada kärä ašiyava ‘after that this Hydarnes with the army marched forth’; DB 2.23 avadé hamar- anam akunaus hadi Müdaibi$ ‘there he made battle with the Medes’.
3487:31 büjiya : avam : Bardiyam : avàja * уаба : Kabüjiya : Bardiyam : avaja : kürahy 32 à : пазу : azdà : abava : (уа : Bardiya : avajata : раѕауа : Kabijiya : Mudráyam 33 : akiyava : уада : Kabūjiya : Mudrayam : aSiyava : pasáva : kara : апка : abava 34 : pasava : drauga : dahyauvi : vasiy : abava : uta : Parsaiy : ша : Mádaiy : ut 35 d:aniy&uvà : dahyuSuvà ; 0àtiy : Dàrayavaus :х3йуайуа : pa
...
</persisted-output>
```


## [2026-09-06T16:01:07.731Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -E \"^ *[Ss]iyav-|[Ss]iyav-.*(go|march)\" KNT.txt | head -20"
}
```


### [2026-09-06T16:01:07.782Z] TOOL RESULT

```
2668:G. To express the goal; names of places are often used thus without a preposition (regularly with fra-ais-, ar-, ava-ar-, pard-ar-, Siyav-), but names of persons always have the preposition: DB 8.82 abiy avam Аттат asiyava Babirum; exception DB 5.21f a&yavam abiy Saküm, cf. DB 2.72, 3.73f (Styav-), 2.721 (fra-ats-), DB 5.23f (ava-ar-), DPe 24 (ni-ar-). With ay- ‘go’ places as well ав persons take prepositions, ef. DB 1.91f, 3.73, DZe 11 for places, DB 1.93, 2.32f for persons.
```


## [2026-09-06T16:01:12.205Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i -E \"iyav|march.*forth|set forth\" KNT.txt | grep -i -E \"lexicon|march|proceed|go\\b\" | head -20; echo \"---- lexicon area ----\"; grep -n \"sarva\\|Siyati\\|siyati\" KNT.txt | tail -20"
}
```


### [2026-09-06T16:01:12.288Z] TOOL RESULT

```
2668:G. To express the goal; names of places are often used thus without a preposition (regularly with fra-ais-, ar-, ava-ar-, pard-ar-, Siyav-), but names of persons always have the preposition: DB 8.82 abiy avam Аттат asiyava Babirum; exception DB 5.21f a&yavam abiy Saküm, cf. DB 2.72, 3.73f (Styav-), 2.721 (fra-ats-), DB 5.23f (ava-ar-), DPe 24 (ni-ar-). With ay- ‘go’ places as well ав persons take prepositions, ef. DB 1.91f, 3.73, DZe 11 for places, DB 1.93, 2.32f for persons.
2711:A. With hada, to denote accompaniment either friendly or hostile: DB 2.21f pasdva haw Vidarna hada kärä ašiyava ‘after that this Hydarnes with the army marched forth’; DB 2.23 avadé hamar- anam akunaus hadi Müdaibi$ ‘there he made battle with the Medes’.
3793:had made one man their chief. Thus he said to them: “Go forth; smite Vivana and that army which calls itself King Darius's!" Thereupon this army marched off, which Vahyazdata had sent forth against Vivana to join battle. A fortress by name Kapishakani—there they joined battle. Ahuramazda bore me aid; by the favor of Ahura- mazda my army smote that rebellious army
4886:After the death of Nidintu-Bel at Babylon, Darius set forth for Media against Phraortes (§31). His march took him near Elam, where a Persian named Martiya had set himself up as King under the name of Imanish. At the approach of Darius the Elamites were terrified, and seized Martiya and killed him (§22-§23) Darius now sent a force of Persians and Medes under Arta- vardiya, a Persian officer, against Vahyazdata, who had made himself King in Persia; he himself, with the rest of the Persian force, went on into Media (§41) and at Kunduru was attacked by Phraortes himself and his army, on I 25, 521/0 (§31). Phraortes’ army was routed; he himself es- caped with a few horsemen, but was overtaken and captured at Raga, and mutilated and put to death with torture at Ecbatana ($32). From Raga Darius sent a force of Persians to reinforce Hystaspes in Parthia (§36).
---- lexicon area ----
2127:II. Fem. - stems (some possibly -7- stems): Nom. Sg.: аг )$, уан, 1185, probably фр]. Acc. Sg.: Siyatim, bajim, dipim ; рабіт (to a hetero-
3064:hya adadà Siyatim martryahyd has the verb before 3 | the direct object). ;
4103:Tux Inscriptions or NaAQS-1-RugTAM. DNa = Darius, Nags-1-RustaMm A. 1 baga : vazraka : Auramazda : һуа : im 2 ām :bümtm :adà : hya : avam : asm 9 апат :adà : һуа : martiyam :adà : h 4 ya : Siyatim :adā : martiyahyà 5 :hya : D&rayavaum :xšāyaðiyam : ak 6 unau$ : aivam : parüvnàm : xSdyaé 7 iyam :aivam : parüvnàm : framátà 8 ram : adam : DarayavauS : xsayatiya : va 9 zraka : xSàyafiya : xSdyafiyanim 10 : xSdyaiya : dahyünàm : vispazaná 11 nam : х$йуайуа :abyáyà : шт ` 12 уа :уалаКауй : diiraiapiyf: Vistas 13 pahyà : puça : Haximanisiya : Parsa : P 14 àrsahyà : риса : Ariya : Ariya : ei 15 с̧а :0atiy : Darayavaus : xsaya 16 fiya : vašnā : Auramazdaha : ima : 17 dahyáva : {уй : adam : agarbáyam : 18 apataram : haeà : Ратѕа : adamsàm : 19 patiyaxSayaiy : manā : bàjim : abara 20 ha : tyasàm : hacdma :afahya :ava : a 21 kunava : dàtam : tya : mani : avadis : 22 adaraiya : Mada : Uvja : Parfava : Harai 23 va : Bàxtri$ : Suguda : Üvürazm 24 i$ : Zraka : Harauvatis : Gatagus : Ga 25 dara : Hidug : Saki : haumavargà : Sa 26 kā : tigraxaudà : Bābiruš : A 27 Gura : Arabàya : Mudràya : Armina
4505:4 п: ада : hya : Siyatim : ada : mar
4538:3 :martiyam :adà : һуа : Siyatim :adá :
```


## [2026-09-06T16:01:17.289Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -E \"yav-\" KNT.txt | head -30"
}
```


### [2026-09-06T16:01:17.337Z] TOOL RESULT

```
2668:G. To express the goal; names of places are often used thus without a preposition (regularly with fra-ais-, ar-, ava-ar-, pard-ar-, Siyav-), but names of persons always have the preposition: DB 8.82 abiy avam Аттат asiyava Babirum; exception DB 5.21f a&yavam abiy Saküm, cf. DB 2.72, 3.73f (Styav-), 2.721 (fra-ats-), DB 5.23f (ava-ar-), DPe 24 (ni-ar-). With ay- ‘go’ places as well ав persons take prepositions, ef. DB 1.91f, 3.73, DZe 11 for places, DB 1.93, 2.32f for persons.
```


## [2026-09-06T16:01:21.587Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i \"cyav\\|cyavate\\|Cyavana\" KNT.txt | head; echo \"=== lexicon S section ===\"; grep -n \"Siyav\\|siyav\\|Sivav\\|$iyav\" KNT.txt | sed -n '1,40p'"
}
```


### [2026-09-06T16:01:23.814Z] TOOL RESULT

```
=== lexicon S section ===
1402:‘death’, cf. -30- in OP martiya ‘man’. adurujiya ‘he lied’, cf. drauga ‘the Lie’. asiyava ‘he went forth’, Skt. (mid.) deyavala.
2583:II. The secondary ending was pIE -nt, which - lost the final ¢ in pAr. unless sentence phonetics ` permitted its retention; for in pAr. only a single consonant could stand at the end of a word. In OP, also, the final n was not written (§112). Be- fore this ending the thematic vowel was -o-: pIE *ebheront, Gk. égepov, Skt. dbharan, OP abara”; OP abava", anaya”, ayauda", asiyava", alarsa”, agar- báya"; passive арата", ayadiya". Non-thematic stems would normally have pIE -nt after conso- nants, becoming pAr. -at; but this was commonly replaced by -an(t) after the -am of the Ist sg.: pIE *és-nt, but Skt. азат, ОР аһа”; OP apariy- diya”, avájana",
2668:G. To express the goal; names of places are often used thus without a preposition (regularly with fra-ais-, ar-, ava-ar-, pard-ar-, Siyav-), but names of persons always have the preposition: DB 8.82 abiy avam Аттат asiyava Babirum; exception DB 5.21f a&yavam abiy Saküm, cf. DB 2.72, 3.73f (Styav-), 2.721 (fra-ats-), DB 5.23f (ava-ar-), DPe 24 (ni-ar-). With ay- ‘go’ places as well ав persons take prepositions, ef. DB 1.91f, 3.73, DZe 11 for places, DB 1.93, 2.32f for persons.
3487:31 büjiya : avam : Bardiyam : avàja * уаба : Kabüjiya : Bardiyam : avaja : kürahy 32 à : пазу : azdà : abava : (уа : Bardiya : avajata : раѕауа : Kabijiya : Mudráyam 33 : akiyava : уада : Kabūjiya : Mudrayam : aSiyava : pasáva : kara : апка : abava 34 : pasava : drauga : dahyauvi : vasiy : abava : uta : Parsaiy : ша : Mádaiy : ut 35 d:aniy&uvà : dahyuSuvà ; 0àtiy : Dàrayavaus :х3йуайуа : pa
3490:40 àt& : pasiva : kira : haruva : hamigiya : abava : haeà : Kabüjiyà : abiy : avam : 4] aSiyava : uta : Parsa : ша : Mada : uta : aniyà : dahyáva : xfagam : hauv
3527:72 iya : ima : tya : adam : akunavam : pasiiva : уай : xSayabiya : abavam ‚ 73 : Dürayavaus : xSdyabiya : уа : adam : Gaumatam : tyam : magum : avüjanam : ра 74 sīva : I martiya : Agina : пата : Upadarmahya : puça : hauv : udapatalá : Uujai 75 y : kàrahyà ; ava : afaha : adam : Üvjaiy : xiiiyasiya : amiy : pasdva : Uv 76 пуй: hamigiya : ауа :abiy : avam : Aginam : aSiyava : hauv : xšđyaðiya . TI :abava : Üvjaiy : uti : I martiya : Babiruviya : Naditabaira : патол : Ainatrahy
3529:78 à : puça : hauv : udapatatà : Babirauv : káram : ауада : adurujiya : adam : Nab 79 uk"dracara : amiy : hya : Nabunaitahy& : риса : pasava : kära : һуа : Babiruviya 80 : hamva : ably : avam : Naditabairam : aSiyava : Babirus : hamigiya : abava : x
3535:84 birum : asiyavam : abiy : avam : Naditabairam : hya : Nabuk'dracara : agaubatà 85 : kara : пуа : Naditabairahya : Tigrám : adàraya : avada : aistatà : uta : i abiš : nāviyā : dha : pasiva : adam : küram : maškāuvā : avakanum : aniyam : usa : 87 bürim : akunavam : aniyahyà : asam : frinayam : Auramazdàmaiy : upastim 88 : abara : vaSnà : Auramazdaha : Tigrām : viyatarayama : avadà : avam : kàram : 80 tyam : Naditabairahyà : adam : ajanam : vasiy : ыз MR E rau
3586:Техт or DB, Сошмх П: 1 :98ty : Dárayavaus : xSayafiya : paeüva : Naditabaira : ha 2 dà : kamnaibis : asabaraibis : amufa : Bübirum : ašiya 3 va: pasàva : adam : Babirum : ašiyavam : vasnd : Auramazdiha : uta : Ba 4 birum : agarbiyam : uta : avam : Naditabairam : agarbüyam : pasáva : ava 5 m : Naditabairam : adam : Babirauv : avüjanam —— :0ütüy : Dārayavauš : x 6 Sdyabiya : yātā : adam : Bübirauv : àham : ima : dahydva : tyà : hacàma : ha 7 migiyà : abava : Рагва : Üvja : Mada : Aðurā : Mudráya : Parfava : Margus : Өз 8 tagui:Saka : абу : Dārayavauš : x8dyabiya : I martiya : Martiya : nā Q ma : Cicixrais : puca : Kuganakà : пата : vardanam : Pársaty : avada : adaraya : 10 hauv : udapatatà : Uvjaiy : Кагаһуй : avaðā : afaha : adam : Imanis : amiy : 0 11 vjeiy :xSdyafiya —— : @atiy : Darayavaus : zsayattya : adakaiy : adam : asna 12 iy : àham : abiy : Üvjam : pasáva : hac&ma : alarsa : Üvjiy& : avam : Marti 13 yam :agarbaya : hyašām : mafista : dha : шат : avàjana — : 00у: D 14 árayavaus : xSiyafiya : І martiya : Fravartiá : пата : Мада : hauv : udapatat 15 à : Madaiy : Катаһуй : ауаба : абала : adam : XSa6rita : amìy : Uvaxdtrah 16 уй : taumàyá : pasáva : kāra : Mada : hya : v'àpaliy : haw : hacáma : hamiciya : a 17 bava : abiy : avam : Fravartim : aSiyava : hauv : тёйуайтуа : abava : Madaiy 18 9àtry : Dárayavaus : xšāyaðiya : kara : Parsa : ша : Мада : bya : ира : mim : 4 19 ha : hauv : kamnam : aha : раѕауа : adam : kdram : fraiSayam : Vidarna : пата : Pársa : man 7 20 à : badaka : avam&àm : mafistam : akunavam : avataSaám : afaham : parait : avam : К 2] dram : tyam : Madam : jatà : hya : mand : пау : gaubataiy : pasiva : hauv : Vidarna : ha 22 dà : kara : айуауа : yafà : Madam : parárasa : Māruš : пата : vardanam : Ma 23 дау : ауада : hamaranam : akunaus : hada : Мада : һуа : Màdaisuvà 24 :ma(iSta : dha : hauv : adakaiy : пау : avadà : аһа : Auramazdimary : u 25 раѕійт : арага : vasnà : Auramazdáha : kāra : hya : тара : avam : kàram : t 26 yam : hamiciyam : aja : vasiy : Animakahya : mähyä : XXVII : raueabis : fakat 27 à : аһа : avatüsám : hamaranam : kartam : pasáva : hauv : Ката : һуа : manā : Карада : пат 28 à : dahydus : Mádaiy : avadà : mam : amánaiya : y8tà : adam : arasam : Mada ' 20m : 08у : Dàrayavaus : xšāyaðiya : адаг х : nàma : Arminiya : man 30 à : badaka : avam : adam : frāišayam : Árminam : avafasazy : aaham : paraidiy : ka 31 ra : һуа : hamigiya : mană : naiy : gaubataiy : avam : jadiy : pasiva : Dadarsi 32 š : aSiyava : yafà : Arminam : parárasa : pasáva : hamigiya : hagmatà : paral 33 tà : patiš : Dādaršim : hamaranam : cartanaiy : Züzahya : пата : àvahanam : А 34 rmíniyaiy : avadà : hamaranam : akunava : Auramazdimaiy : upastàm : a 35 bara : vasnà : Auramazdàha : kāra : һуа : manā : avam : küram : {уаш : hamigiyam : 36 aja : vasiy : Oüravaharahya : máhya : VIII : raucabis : 09akatà : dha : ava 87 à$üm : hamaranam :kartam : бабу : Dárayavaus : z3àyaffya : patiy : duv 38 itiyam : hamigiyà : hagmatà : paraitd : patiš : Dàdar&im : hamaranam : carta 3€ nay : Tigra : пата : didà : Arm‘niyavy : avadà : hamaranam : akunava : А 40 uramazdàmaiy : upastàm : арага : vašnā : Ашатагдаћа : kāra : һуа : тапа :a 41 vam : káram : tyam : hamigiyam : aja : vasiy : G9üravüharahya : mihya : ХҮШ 42 :raueabiá : бакаќа : аһа : ауабадат : hamaranam : kartam —— : 00у : Daraya 43 vaus : xšāyaðiya : patiy : citiyam : hamictyd : hagmatà : paraita : pat 44 iš : Dádar&im : hamaranam : cartanaiy : Uyama : nama : didi : Arm'myaty :a 45 vadā : hamaranam : akunava : Auramazdimaiy : upastam : арага : vaSnà : Aurama 46 zdàha : kāra : һуа : manā : avam : küram : tyam : ham?giyam : aja : vasiy : Oàigarea 7 d :mábyà : IX : raucabis : Nakata : dha : ауада ат : hamaranam : kartam : pasava 48 : Dadarsis : citā : mim : amánaya : Arm/niyaiy : yiti : adam : arasam : Ма
3615:72 gi : nama : dahyaus : Mádaiy : avapara : asiyava : pasiva : adam : karam : f
3628:85 āva : Taxmaspáda : hada : kira : aSiyava : hamaranam : akunau’ : had )
3716:33 dam : разӣуа : Artavardiya : hada : Ката : asiyava : Pārsam ` 34 : yaa : Pársam : parárasa : Ваха : папа : vardanam : Parsaly : а
3723:42 mufa : aSiyava : Paxsyàuvadàm : hacd : avadaga : kāram : àyasa
3758:81 racara : amiy : hya : Nabunaitahya : puça : pasàva : kara : Bübiruviya : hacáma : Һа 82 migiya : abava : abiy : avam : Arxam : aSiyava : Babirum : hauv : agarbayat
3770:80 fkjdrahya KT. #1 Nabunaitahya KT; cf. §36.IVb. 8 yigsfars[n*a KT, cf. 86 and 88; videfer*a RI. 3 Pa[rsa] KT, cf. 4.83; Mada RI. ** RL’s tyam at the beginning of the line ів not there, acc. to KT. ** Babiruvi[yajm KT. 35 [ga]ubütaty KT; gaubdiaty Rl. 9 Rl's abiy between aSiyava and Babirum is not on the Rock, acc. to KT. 88 yiga[f«ro |n a, KT; v'd^[f^r*]a Ri. *5BabiruvilyM : aja KT; Babirum : agarbaya Rl., WB. * [agarbáya] WBn, HK; [basta : anaya) or [anaya : abiy : тат) Tm. VS. 9.r... nahya WB, WBn; Margazünahyá HK; IMalr[gajalnahya
3945:pB V TEXTS WITH NOTES AND TRANSLATION 133 8 nima : Pársa : тапа : badaka : avamSém : табат : aku 9 navam : pasáva : haw : Gaubaruva : hada : kara : aSiyava :
```


## [2026-09-06T16:01:31.781Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== BRT syaoθna ===\"; grep -n -E \"syao|s'yao|ayao.na|Handeln, Wirken|Tat, Werk\" BRT.txt | head -30"
}
```


### [2026-09-06T16:01:31.838Z] TOOL RESULT

```
=== BRT syaoθna ===
2477:y^  . .  möi  gas'^iä  dazdl  *amaiiklmit  akyä  \  myazdS  . .  äisy.ll  kl  anhe  ava{  mlid^m  A. maä%rilfrö^StY.46.Z\'—yatäröpaurvö^3.(il.;  — yastal  mihdgm  haiuftt? nöit däitX äire  . .  paitiJiaraiti  ahmäi  atars  ä/rJnat  .  .  kä  tsm  ahyä  *maeHis(sA.)  ar»hatY.44. V.1S.26;  YLIJ.51; — y ahmäi  xlnstö  ba-\  i^.  b)  .\Sn.,  f.  mit  Äaca  sva. 'dadurch': vaili  mi^rä  ahmäi  Jasaiti  avaiäke  YLIO.  yezi  mit  spä  ..  maeyevä  . .  pai'jyäite  ahmat 84;  87,  Y.GS.w*;  — yöi  nsil  ahm  main-  haca  irisyät  "sonst  konnte  der  Hund  in  . . yantä  aiibyö  dair?  (sd)  voka  as  manö  Y.  \  geraten,  dadurch  könnte  er  Schaden  neh- 34-&]  9.  2&  10,  45-ii  — yaisqm  ..  mazdä  \iata"  V,/_j.37;  —  ahmat  haca  /«>nj  (sd) ..  vatghö  vai'ja  alsqm  ..  Yt.i6.%; — ^J  sayiJ/A' Nik.  7;  *2; — yesi  tat  paiti  irisjati syao^anä  yä  vacatihä  yä  yasnJ  .  .  ae^qm  '  aiähal  hala  iyae>n!i7ar3za  (sd.)  .  ,  V./_?. töi..}hmä  pourutimäil  äasl?(sd.}Y.j4-^,''  38-  2)  vorausweisend;  i)  adjektivisch ■ —  yöi  *aite  . .  *gä'kä  nSit  *srävayänti  . .  I  auf  direkte  Rede  oder  Zitat:  vahiütsm  . . assqm  fyaohamm\ia'\  .  .  N, 25;  —  ySt  ..'igänii  ..  vir^zyat  öyä  (ISf.)  «>/f  (sd.):  hvö avatahabdgnti  (sd..)  /ramar?nl>m  (sd.)  ag-  *pt3  asahyä  mazdlY.4y.2;~aya  antar?.- £qm  nöit  aita^qm  ratufris  ..  N.52;  ^j\  uxti  (sd.) :  nöit  nS  mana  (usw.,  Y..^5.z) —  yahmät  kakmäicit  nalmaruim  vätS  ä'^rö  Y.ig.i$.  —  a)  mit  ergänzendem  Relativ: baoiolm  vibaraiti  (sd.)  ahmll  kahmäiHt  aya  aibigara  (LS.  als  Instr.)  aya  aibijary- nalmanqm..\.8.&o.  a)  Die  Beziehung  ta{d.^.)  yä  amfsanqm  sp^ntanqm..:  gave ist  ungenau:  ^yJ  räakaytn  (sd.)  sravaahä  rto5j/(usw.,Y._j5.4)  Vr.J2.i.  a)  substan- vahistät  iyadkanäl  mantärü  aeibyö  mazäi  tivisch  und  adjektivisch  auf  eine  erläuternde akä  (sd)  mraot  "qua  alienant  doc-  oder  ergänzende  nominale  Beifügung:  «7.5- trina  . .,  üs  .  ."  (statt  qui  ..  iis  ,  .)  Y.32.  yacä  i^agtuL  yäsat  ahyi  Virßzin3m..ahyä .. 1 2'*^  Anhang  zu  II  I  1,  2.     a)  An   ahurahya  uruasimai^A.)  mazda  Y.j2.i ;  2S.
2531:y.  I ;  —  cayö  'te  raola  at»A)n  . .  yö  ava^a  '  vayrjanake  .  .  yat  °&o  kanjasante  paouru Sraoiayeite'^.2.^<j\  —  "taFsva  daxtnaih'a .gaonaAec'a  IsA.)  . .  ti.6^\  yi(7);  —  taotarf yöi  faiti  äya  z^mä  iavainti  "V.y.^^;  — ^.gstava  ..  ■""'oa'*  ..  N-tVi;  —  yetiAe  'oa "U  malsma  .  .  yaHbyö  .  .  framayattte  V. .  mazdayasnanqm  näirika  . .  *ham.raf^wa- (S'.ii;  —  'taisam  syao^nafiam  yöi  v»r>-  yeiti  "wes  von  den  M.  Frau  dort  . ."  N, sjbA'  masy.lka  V.  J5.2;  —  "tiitbyff  zao-  11;  —  ava'ia  ''QrtV.4.50;  —  taica  "'jaca >rabyö  ..  yämham  ..  N.  71;  —  ku^a  -tat  pü^nm    baraili    Y.iy^^if).  a)    mit
2559:;j.  I ;  —  cayö  'tt  raocii  atjhin  . .  yö  avaha  '  v(rf'ianahe  .  .  yat  '6a  han)asSnte  paouru Sraoeayeite\.2.y);  —  'tae^va  äaxmagh'a,gaonaAe^a  (sd.)  ..  N.f*j;  "/(?);  —  saetari frV  paiii  3ya  ztma  bavainii  V.7.54;  ■ — \gätava  .  .  *'oa'>  ,  ,  N.  A;  —  yetiie  '6a "le  malsma  .  .  yaiibyö  .  .  /rasnayiinte  V. ;  mazdayasnanam  näirika  . .  *hqm.raEä:wa- J'.ii;  —  'taiiam  syao^naiiqm  yöi  V3r>-  yeiti  "wes  von  den  M.  Frau  dort  . ."  N, ziiiti  masyjka  V. /j.  2;  —  "täibyö  zao-  11;  —  avaoa  °oa  'V.4-50;  —  taica  °üaca 'irJbyß  ..yäakqm..  N.  7/;  —  iu>a 'tat  pu>nm    baraiti    V.  15. 49(?).  a)    mit
2587:(faiVw  ,.  "_)'«/  (NSf.)  paiti  rarsta  syao'ina
2967:y}m3  arsdrv  m>at*paouruyÖ  ya'i^a'i^wäy.^YCi.mi'atxe:  'rasiä  ..yai:a  anya  vp&ria zivTitUn  uz^maiT {iVFA.)'*  syao^iatiot  sp?n-\ii/_in_^y^  ^2_
3004:xsa>r,lis  yßpn{sd.)  ..  'i-ais  syaoianäii maslm  Y.  46. 11;  —  hyal . .  °i3  mana/fM . .  "hJ  iyad^an^m  vacaahil  . .  fraanas  . .
3160:•  j,  a-£i9'öiri§ta-  Adj.  'nicht  durch  Busse zu  wenden,  unsiihnbar':  *paoirya  *vtträa (LS.)  asSqm  syaoian)in\c(i\  'tjm  "schon wenn  sie  sie  zum  ersten  Mal  begehen, ist  ihre  Tat  nicht  mehr  zu  sühnen"  N.  23.
3525:den  ist's  yü  andusat  *'tat'>  ajayaunia (sd.)  N.  54;  —  caiti  ta  syadhna  varlta .  .  fraSa  'ta  ■'  anusvarsta  aiAhat  hala I  syaohnavar»za  (sd.)  ,  .  "wie  vielfach  sind die  getanen  Taten  . .  —  begangen  (sind sie),  nicht  beglichen,  nicht  wieder  gut gemacht—:  es  werden  . ."  Y.i$.\.
3665:—  y!^  anyake  nairika  . .  yS  anyahe  *°ha (IS.)^  ..  a'^aurutum  *pararikacaiii  (sd.) N.  7;  77;  —  yat  he  aoxte  aisa  yeiihe  'ks hacatsuha  ms  *ana  "ka  (VS.)  N.5;  7,  *y, *io,  10 ;  —  'ktm  iiahmB.kßrpl)m  *syaokn3m.- v>r}Nm  (sd.)  V.7J.23;  ¥.2^.27.
4425:•  j.  an-ä'p«rafta-  Adj.  'was  (auch  durch Leibesstrafen)  nicht  ausgeglichen,  gesühnt werden  kann':  aya  °i<i  (APd.)  syaoina nard.vaipaya  V.  /.  1 1 ;  12,  16;  —  *spayäli
4426:.  .  daina  mSzdayasnis  .  .  '%pm  syadhram V.J.  41;  —  'S«  fiaca  syao'ina  V.j,39, Vd.2.
4540:•  j.  an-uz'var^-  Adj.  'nicht  wieder  gut gemacht':  astunim  .  ,  syaoh?nanqm  v»r>- zimmm  'tai paiH paurvät  "..ohne  dass  die frühere  (Tat)  wieder  gut  gemacht  ist"  V. 4.2a;  —  syaokna  varsta  . . /ralla  apatita 'ta  (APn.)  V.75.2.
4812:(mit  Akk,):  yezica  hi  anya  aya  /yao^na /ravarsia paiti fa'^^ i'''  As cii:a  "und  wenn er  andere  Übeltaten  begangen  hat,  so  ist die  Strafe  dafür  beglichen"  V.y.  21;  — *paiiit^m'^^  ^'^  he  manu  ar?kat  *paiti- t>m  vaio  syaoimm  uzvarlt>m  (sd.) . .  "so soll  ihm  beglichen  sein,  was  er  (übles)  ge- dacht, gesagt,  getan  hat,.."  V.  7.  51.  S. noch  paitita-  bes.
5034:•  p.  ava'dä  {'da')  '\  j.  ava'8a  Adv.  i)  'dort, da':  \ patigrabanä  näma"  vardanam  . .  "da kamaranam  akunaus  Bh,  j.  ij  7,  9,  10, 2.6— 11^  16; — imaiy  martiyä  tyaiy  *ada- kly(sA.)  'da  aha''ta  Bh.4. 18;  j.  18',  2.  3, 6,J.4, 11,5.4;  —  didä  ..  'dasim  aväjanam Bh,  /.  13;  5. 1,  J.8'';  II  —  kva  .  .  °äa  bä  , . asne  hamsrihät  "wo  .  .  ?  .  .  dort  . ."  H.  2. 20,  *Vyt.54;  Yt6'.47>  Jp- 93>  N./5,  2^'; —  ''ha  agtaha  altahe  syao%nahe  ,  .  V.  4. 50.  a)  II  halä  avadas<^'''>  'von  da  aus': kami  udapatalä  bäbirauv  dubälJ"  namä" dahyäu/  halä  av  hauv  udapatata  Bh._j. 13;  J,  11;  —  hauv  . .  aÜyavaf"  paisiya- ^uvSdiim  haiä  av'  käram  *äyasatä  hyä''- param  *aif..  Bh.j.7  I ,  a)  'dorthin,  da- hin': U  raxa  rtSma!'  vardanam . .  'da  hauv .  .  *ä//Bh._y.6;  1. 19,  2.13;  — fravaSayS
5317:•  j.  a-ra9Twya-  'unzeitig;  unangemessen, ungebührlich':  'wya  daxsta  "wimla  gar)- m3um  V. /.  18;  17;  —  ra%wyanqm  .  . syaohnanqm  . .  aoäityanqm  •wyanqm  dui- varstanam  iyao^nanam  Vr.  15.1;  —  °wya Vyt.47'-(?),  4^C?)-  '
5471:—  ya  'du/at  *apaiHtal  äjayaurva  (sd.) N.  5^;  —  *°duia''>  havayaahim  ^axt?m N.rjC?);  —  puxh^mHi  (sd.)  °du!qm  tanüm piryeiti\.4.iT, — ya%a  ü'hrusum  *yärf gä%ä  asrävayd  hyai  *'du/''''^  hi  syao- %an»m  "wenn  er  ein  Vierteljahr  lang  die G.  nicht  aufeagt,  so  (gilt)  sein  Tun  einer -4.-SQnde  (gleich)"  N.  42.  a)  mit  sna'^a- verbunden:  yö  nar>m  'dusa  snd^a  jainti "wer  einem  einen  .li.-Hieb  versetzt"  V.  4. s6;  29.
5689:•  j.  arS-syaoUna-  "Adj.  'der  die  richtigen
5960:Zum  V.  sTir.-.  —  Die  Urtypen  sind  ASm.  9U5  ,  varUa   syao^na  ^kt^'wA   asaäa  "was  hat
6071:'sa  (ab  Subj.)^  naptyoisä  . .  türaAya  uxjSn  a  a:  aevö  panlä  yS  'sähe  Y,  72.  1 1 ;  — (sd.)  Y.  4Ö.  1 3 ;  —  y7  xidknm  .  .  'iä .  ratus  . .  'sähe  *dasayat  paniqta  Vyt  42 ; /radähai  (sd.)  aspp/fsata  Y.ji.  161  — 1 — 'sähe  faiti  pantqm  ti/ahi  päi/i  mq^rynt %wahmät  äkras^a  manaahascä  yayä  syao- !  V.  ^  43  (s.  ob.) ;  —  sva.  'Stätte,  wo  das %anaU  °hm  %raosiä  (sd)  \.46.J;  — ,  j^sa  heittüxh  ist' :  haoa  nJ  ß-aounauayät/i vanh^us  :^aasus  i^aaatä  (sd.)  vaahius  'sähe  paiti  panlqm  drujg  vaiim^la  asmi- •/fli/J..  Y.J5.  5.  a)  GS.  mit /«ä- 'der  nqm  (sd.)  "waim  wird  uns  (die  Rinder) Pfad  des  ASa,  der  Wahrheit,  des  beUigen  !  zurUckführcn  zum  Pfad  des  Asa  . ."  Yt Rechts'   (s.  I  3  b  a):    dr^gvafö  .  .    *"Ji/j  70. 86.  ß)  GS.  mit  bir^  (sd.):  hnja
6091:—  kadä  vatds  yezT  <ahyä  xlayaüa  (sd.) masda  °sa  (Vok.)  ".  .  o  M.  und  Asa" Y.4<?,g;  i^.  18, 50. 9;  —  atvs  staoiä  aojäi (sd.)  mazda..  'sa  Y.50,11;  2,  6,8,  2Ä  i, 34.T,  —  hvö  zi  "Sil  .  .  ahamMs  (sd.) urväkS  masds  Y.44.2;  18;  —  ara' (sd.) sf  xsmä  mazda  °s3  ahurä^^''  hyal  .  . yoorjaaäa  (sd.)  Y.  50.  5;  —  in  GHapt: masda  aAura  .  .  fava/ä  haxamS  (sd.) -sahyala  \.4a.ii.;  41.6; —  *aAura.mazda °ia  (Vok.)  srira  Y.j'5.3;  —  masdai  ahurai 'säila  vahistai  Y.  JJ.  j ;  4/.  i .  «)  in dualiscjiei  Verbindung  mit  ahura-:  yöi  vS syaoianäissärMil{%d.)aAurff*asa*Aisvä^''''> axhai/ ..  Y.51.3  (s.c).  b)  neben  VoAu- ManaA:  yäcS  vehü  uxoa  fral%  (sd.)  ma- nauAä  yOcs  °sa  (Instr.)  aahlus  Y.  44-  8; '31  —  yf  «""'^  "^  (Instr.)  tmüi  hvö *mainyJus  a  vaMstat  kaya{iA.)..  Y.S3.6; 4g,$;  —  %wavas  . ,  masda  hadtmsi  (sd.) -ia  vohulä  yyas  manavkä  Y.  44-  9 ;  2Ä  5 ;
6189:Gen.  subj.  und  obj.:  alsm  *d>nidyäi{iA.) .  .  rayS  'st/  ". .  jrXoiiTOU  fioi'pai"  Y.  4J.  i ; —  abifra  (sd.) . .  ya  vaahsus  'sis  mananha Y._3i5.i3;  —  aiahya  yasa  {%A:)  'slm  y am iiyam  Y.  54.1;  —  °M/a  ^ae^ananqm viäu/(sd.)  ahurakya  mazdS  ".  .  des  AhM. Belohnungen  fiir  die  Taten  . ."  Y.2<V,4; — ■  nöit  kl  "M  *^ao^nanqm  vimysit  N. 16  ij);  —  zard>!ustrahe  .  .  asatinS  'itmia fravaiimca  yazamatde  Vr.  16. 2 ;  2,  Yt  13. 95;  —  tti  ahmt  nmane  Jamyarps  yh  asao- nqm  xshätas/a  'sayasca  . .  paitisatitayasla Y.  60. 2.  a)  mit  vanAav-  Adj.  und  aka^ Adj.  näher  bestimmt:  vatfkttyascä  °Ssi/ .. yS  ns  ara^ä  (sd.)  irmavaia^a  asanhäxs ^■5^-3't  —  syao^ana  mizdavqn  (sd.)  .. akfm  akai  vamthlm  'stm  vanhaavi  Y. 43. 5 ;  —  tSm  vatmklm  yasä  (sd.)  °sim  Y. 5;. ai;  —  maifyn  siaya  ahm  vaaAuya 'st  gaui  (sd)  Y.5/.  10«;  —  xmBth  afn- n>ntu  ahmya  nmsne  vawtklm  °/lm  i^a- parqm  Yt.  /J. i  S 7 ;  —  vaauAlsca  aöa  vaau- klsca  'sayS  Y.53.3;  —  yhca  tsi  gmh *aiura.mazda  ..  iSä  . .  vanukim  iihl/  'lim . .  ihm  .  .  *panndlm  yazamaidi  Y.^S. if  b)  Du.  'die  beiden,  beiderlei  Lose', d.  i.  (das)  gute  und  (das)  böse:  tmnanha (sd.) y5  dä%alibyd  priLratüm  xsayqs  'äfä*"^ üista  ". .,  der  über  beiderlei  Lose  gebietend den  Klugen  den  wahren  Ratav  versprochen hat"  Y.57.5.  A)  als  Gottheit,  die  die Lose,  insbesondere  die  guten  verteilt,  im jAw.  als  Göttin  des  durch  Frömmigkeit  ver- dienten Wohlstands*';  I)  im  gAw,:  Siraosö 'sfi  mqza.raya  (sd.)  Aacimnif  ya  vT  altl *ran3ibya  savlfi(sd.)  vldayäi  \ .  4j.  1 2 ; -^ sraosS  .  .  yU  *'li^  haiaiti  *mqxaraya  V. 27.6,  Vr. /2.1;  —  ya  vldayaf  'sts' (HS.) räshqm  (sd.)  Y.j^.  la;  —  ys  fta  'sSis aojaifha  var>dayaita  yqm  ,  .  gai^qm  .  . Y.  so.  3.  a)  Du,  in  Verbindung  mit armaiay-  Du.  ^A.  und  Arm.':  yads  ahm zivlm  (sd.)  .  ,  mazdasca  .  .  'sicil  armaitl Y.31.^.  II)  im  jAw.:  yö  'lim  yazäite ..k5  mihnm  yazaiieY\..i-j.2;  —  -/j  (VS.) srlre  'si  banumaili  .  .  °li  dä'ire  vehäm i^arifiilYt.sy.^;  6of.*;  —  hm  hacSl  'Hl pourvsj^ä'iira'Yt  /j?.54;  — /rä  mqm  aiwt.- urvalsayatfuha  marsdik?m  'al  (als  VS.) hnzaiti  Yl  77. 1 5 ;  —  'lim  . .  darr/S.- variiman3m..bartntltn  vispä  baSlazsY.S'i. 2;  —  sraohmla  'lim  nairXmca  sauh>m IVyt.40;   —  fravalays   .  .    'Isil  balsaza
6222:•  j.  aiava-gan-"  Adj.  'der  einen  Gläu- bigen tötet':  yS  'vaja  (NS.)  yS  yätumk Y.  65.8;  —  yai!a  sat»m  kayaoanam  avavat (sd.)  •va.Jacit'^  Yt/0.2; —  scindaya  °va- jans  (AP.)  Yt  /o.  7  6 ;  —  'vaynqmca  asava.- liaisqmöi  Y.  61. 4.
6254:—  syao%ami  razistä  (sd.)  ängvataicä kyai<ä  *'iaotii  yehyäiä  ASmunylsaitl  (sd.) mi^aAyä  yucä  ksi  är»svä  Y.  _jj.  i ;  —  yS vü  xsayqs  adqs  drTtä  ayanhm  urvatsis (sd.)  Vit  huiSntul .  .  ra/nä  jvqs  yS  'savä dr3gvant)m  Y.  46.  5.  a)  Ko-i  it  von Zara^ustra  (s.  2  c  a  und  drTgvaiit- 1  2  a  a) : y!  äyal  •iavanam  divamnsm  (sd.)  hsi  . . *dusji^arä^Sm  (sd.)  . .  ISm  *vi  ahSm  dr>g- vants..dams  «a<tf«/(sd.)  Y.^7.20.  b)  im jAw.:  kat  *sava . .  vanai drvantami  'idva vanat  drußm  °sava  vanat  drvantpm  Yt. I.2S;  —  x^ayamnam  '/avanim  däyata *axsyamn^m  drvant^m  Y.  Ä  5  ;  —  vasB.- x/a'iirB  kyüi  'sava  avasS.xia'^rS  hyäf  drvä Y.S.6;  —  yqm  'lara  ..  asayqm  (sd.) va^  tarn  drva  ^ihva  Vr.  22.2;  —  mt^nm ms  janyh  mä  yim  drvatat  pimanke  mU yim  n^adafnat  'iaoiiat  uvayä  af  asti  (sd.) mskrB  drvataica  'saonai^a  Yt/o.  2;  — pdhqm  %rvB.däianqm  jasaiti  yasla  drvaile yas^a  '/aofieV.  lff.$o;  — yai  azäite^sd.) tsm  ahum  pai'iyaite  yim  "soonam  yesi  nHii azUiie  tun  aAam  pai^yäite  yim  drvatqm V.  /Ä76;  —  drvatqm  ..  urvänS ..'läunqm V.  ig.  30;  —  ga>il  nmätiam  ^mr^yS  asti '/SvaoyB  (DP.)  naSai  drvatqm  Yt,7.4;  — hiiia  para  'saonqm  pa^a  urva/ai/i  iu^a drvatqm  Yt4.4;  —  narqm  vä  'saonqm kanjamanäis  drvatqm  vä  . .  kandvaranäü YLi/,4; — yai  •i'ava  para.iriiyeiä  . . yal drvä  ava.*miryeie  H.2.1  — 19;  7,  8,  10, 15*,  16',  18  {'iaonyäi);  s.  unter  drvatif- 1 1.  2)  sonst,  a)  im  gAwr.  (ausser GHapt):  zara'^usträ  kastl  'lavä  urva^S mazsi  magäi  (sd.)  Y,  46. 14;  —  tSm  (näml. pounicistqm)  . ,  varänl  (sd.)  .  .  yä  försi vTdäl  paüyaFcä  västryaHbyo  (sd.) . .  *°iapnj 'iavabyS  Y.  5J.4;  —  hvs . .  yas^a  vadarS (sd.)  vBizdal  'iauni  Y.^a.io.        a)  spez.
6533:iSt.  Yt.  /o.  77. "  g.  aiyah-,  j.  aäah-  '>  Adj.  'der  schlech- tere, üblere,  bösere'*':  yS  vahys  vatthsul iazäl  yascä  .  .  at  ahmäi  akäi  "syB  yJ .  . Y.5/.6;  —  jamyHt  vS  vat?Aaot  vauhd  mS ^  jamyifi  akät  'so  Y.55.31;  31.  A)  in leligiös- moralischem  Sinn:  y}  däi  mans rakyd  maeää  'syasLü  hv5  dalnqtn  syao- 'ianäcä  vaca»käcä  "wer  sein  Denken  (jetzt) besser  macht  und  (jetzt)  schlechter,  o  M., und  (ebenso)  sein  Ich  durch  sein  Tun und  Reden"  V.4*.  4-^*-
6568:yezi  a>ä  sia  Aai'iJm  (sd.)  \.34.fi;  — ■".  .  Wesenheiten  (animalta)  .  ."  V,^.  40 h)nH*^  anyhHt  aiasca  söi>r<hca  "es  gibt  PiiZ.;  — yä  kstqm  syaoianartqm  vahista auch  noch  andre.."  V.J. 20;  —  at'a  h>nii' hyäl  "welche  unter  den  Werken,  die  es paritöJanunqm  (sd.)  syao^nanqtn  asi^arj- ;  gibt,  die  besten  sind"  Y.  jj.  3;  Vr.  72.  4; tayS  ¥.7,52  PüZ.;  —  kapta  hanti , —  daatayli  yat  hattinqm  vahistayäi *hävanayl  miat'S 'S.  102  Q);  — yfAud>i\"dN  besten  aller  Religionen"  YL/j.  91, ySi  /antl  "der  es  wohlmcint  mit  denjga;  —  aisam  aukunam  hatam  VyL Seienden"  Y.  45.  6;  44^  i6S>,  5/.  io;_— |J0(?);  —  ot'j  .  .  vasiniAe  hat's  (GS.)"» yehyä  .  .   vahUl}m    vaidä    (sd.)    mazdh  .  .  i  aoäitlm  (sd.)    vao'ait  V.  4-  46.  I )  mit
6740:•  g.  a-hämusta-  Adj.  'des  man  nicht froh  werden  kann,  widerwärtig';  drjgT'ä.. duiazSba  hqs  x'äil  syaoianäil  "ts  ".  .  er, der  übelberiichtigt  ist,  widerwärtig  ob seines  Tuns"  Y.  46. 4.
6759:(wen?)  valnm  dämBhu  ahümca  ratümca •  j..  g.  "a-hü-,  a-Bhü-m.;  g.  a-Duhi-f.l^^^%,^„„;„  YtiO.gsS);  —  syao>manam 'Herr;  Herrin';  i)  eines  Hauses, 'Hausherr,  i^a  ahüm  hlrayäti  (sd.)  Y.79.13. pater  famiUas;  Hausherrin':  ydi  *dr^g--  .)  ich  nehme  an,  dass  die  Rechtspflege  im vantS  mazibis  cik5it>r>i  aauhlsca  (APf.)  alten  Iran  ähnlich  geordnet  war  wie  bei  den oü^iMi-'S  (APm.)  apayäa{%A.)  vaed^m  Y.  Griechen,  Italern,  Kelten  usw.;  5.  Schrader 52.1..  a)   eines   Gemeinwesens  'Ober-   Re"Il"-685.   Der  .4*»  (aus  dem  Kriegerstand;
6875:2g.  6,  33.6,  II,  51.  15,  53.  i):  y}  sivim 'rS  mazda  Jiä..  Y.j:^.ii;2Ä'.5;  —  spmtim at  %'wil  mazdä  m}nghl{sA.)  "rä  Y.  43.  5; 2g.  T,  5'.  16;  —  sp>ntS.t?mo  ..  mazdä  °rö Y.45.S;  —  mazda  sai^ärJi^A^  mairisiö.. kvS  vleirsisd.)  'r3'>  V.25.4;  —  hätä-maräm (sd.)  'rä  . .  mazdä  Y.  32.  6 ;  —  yaslqm tu  °rä  irixl»m  mazdä  vagdiitö  ahl  Y._y2. 7;  —  ai  S  (sd.)  vaocat  -rö  mazda  vtdva vq/äf  (sd.)  Y.  25.  6;  —  aiiiyS  mazda  'rS .  .  paiti.mraot  Y.^2.  2;  —  tvSm  mazdä °rä  frS  mä  sTsä  .  .  *vaocaiihi  Y.  28.  11; 4S-  ^  >  —  anhsttl  (sd.)  akya  paourvJm *yqm  mSi  vJdva  (sd.)  mazda  vaocat  'rö '^'■45-V>  —  tat  %w<i  pinsä  (sd.)  »nl mSi  vaocä  'rä  .  ,  azJm  täÜ  "iwä  fraxsnt (sd.)  avämX  masdä  .  .  vupanam  dätJnm \.44~T,  1-4,8-11,  14-18,'^/.  14,  J4- 15;  —  °rä  yaübys  mazdä  "hwöi  vasyäl damä  Y.44.11;  —  sdr  «7  mazdä  'rä vanhsus  /radaxitä  (sd.)  majianhB  Y.jj. 1 7 ;  34-  13;  —  yehya  . .  vakisUm  . .  valdä mazdä  'rff  Y.  51.2a;  31.3;  —  yJ  viHnaot dä%imcä  (sd.)  aää'^?mca  dangrä  mantu aM  mazdä  'rö  Y.  46. 17;  2S.  10;  —  ustä aAmäi  yahmäi  ultä  (sd.)  kakmäicii  *vasS xiayqs  mazda  däyät'rö\. 43.1  •,32.16;  — yS  afimJnT(sd.)  matda  srävT  °rö  Y.  45. 10"*;  —  tä^ä  x/a^rä  mazdä  dqmis  °rS Y.  45.  7 ;  —  voAb  xia%r»m  manaahä mazdä  dadät  'rS  Y.5J.  ai;  31.  zi,  34.  i, 47.  I ;  —  at  mazdä  taibyS  xi'a%r?m  voAli mananhä  *vSivTdaitl  aübyo  sastl{sA.)  °ril.. Y._jo.  8;  46'.  12;  —  at  hsi  mazda  ahüm (sd.)  dadät  'rB  V.^tf'ij;  —  y}  vahyo vat^Asuf  dazdi  ,  .  'rö  xsa'hrä  mazdä  at ahmäi  akäjl  asyS  Y.5/.  6;  —  Aat»Aus(sd.) ; .  .  mazdä  dadät  'rö  . .  yai'öi  vTspäi  ä  Y. 53- Ai  I.  5'-'7>  54- i;  —  aslscä  syao>a-^ nanqm  ..  mazdä  'rahyä  Y.2Ä4;  —  'rahyä urväzsmä  matda  Y._J2.  i; —  'rä  .,  hyal\ *avistä  *hudäbys  mTidfm{&A.)  mazdä  yehyä  ' tu  da'^nm  ^.34- 13;  14, 5 J.  15;  —  mazda  \ x/dira  *vanzT (sd.)  «ä  dyäj  'rö pasüs,,^ frada^äi  ä  Y.45.  9;  —  at  ahyäi  (n'äml.  1 gavöi)  asä  mazdä  urvara  vaxlai  'rö  Y. 4S.  6;  —  C7«  äzötöis  'rö  mq^r>m  lasai . . ' mazda  Y.2(J.  7;  —  ?«;s/  paüö  ya?ia' mazda  'rff  *saittl  ^.33.5;  46.16;  — y^ngstü  mazdä  kad»möi  minas  'rä  Y.  46. , 14; — gätamcä  'räi..t3raohm(^A^  mazdäi ^ Y. 2&5;  —  töi  rwr<7/(sd.)  rädmil  -rahyä- zaosl  mazdä  ^.33.2;   —    yai'ä  xsnaol)H\
6944:•  j.,  g.  ahmät  Adv.  I)  'inde';  i)  räumlich; nHt  käu  as  vaote  (sd.)  .  .  nBit  a'  vaiata ". ,  oon  inde  procedit"  P.  4^.  2)  zeit- lich, a)  'von  nun  an,  nunmehr':  ys . .  kayä (sd.)  a°  . .  7'ästryä  Y._jy.6;  — yä  a°  staota yasnya  irävayeni  "indem  ich  nunmehr  die StY.  aufsage"  Ny.4-S-  b)  mit  folgen-' dem  ya^a  und  fiiL  Konj.  'doncc,  bis  dass': aU'it  a'  yaha  ap?mgm  maniva  an  Aat mz'Ji/is  (sd.)  Y. 10.16.  U)  beim  Kompar., wörtL  'als  das',  was  i)  vorausgeht  oder 1)  folgt;  meist  unübersetzbar,  i)  zurück- weisend auf  zuvor  Genanntes  oder  Ge- sagtes: imaj  vS  jatöyemi  .  .  yalca  a°  asH miirya  ".  .  quodque  hoc  est  maius"  Y. 'jj.  14;  14'i  —  saisisca  .  .  oAqxitäiscä *ß-äyjblscal(sA.)ca  a-  Vr.  Ä  i.  a)  in Verbindung  mit  eil :  ayaaAaUtäis  kan- täis  paiti  azdibis  avaJitriäiyilt  {%^)  masyd vü  'mii-'i/V. 4. 50;  51,52.  2)  voraus- weisend auf  einen  Nebensatz  mit  &)yd:ia: yifnö  zqm  visävayat  afvit  irii'va  a'  mas- yefäm  ydia  fara  ahmai  Y.  2. 1 1 ;  —  nüit il  a-  *drajyS  *yätltn  framraemi  (sd.)  .  . äfrOIm  .  .  ya>a  .  .  V.33;  Yt.  I3. 64^;  — xraesyöJaraia  (sd.)  ri5  a'  ya>a  vikrkS raiÄfsd.)  Ißi/eV.  IJ.8;  —  näirivai/e.  .  «• pÖurum  '>  frantraomi  . .  ya%a  mayavö  (sd.) /ratäxsffit'V.4.^T,  47J.  h)  yäha  yat: itsit  vaakö  a'  fyao>amm  v»r^yeiti  ya'^a yai..karMt^.4S;^.iS.\o.  c)  yattsit: nSit  vanhs  a'  syao%tum   vtnsyeiti  yaüöil
7151:ah'  m'  puhrsm  (statt  Gen.)  V.5.  2,  15.  | 45;  —  'trun'a  ioa  ah'  m'  pu^inm  yazo- maide  Vr.  lO.  i ;  Yt.  I().  46,  S.  2.  7,  9S,  Y. 2.4,  12,  /Ö.4,  /7,ii',  ifj.2,  25.7',  V.fV. 14,15,75.48.  2)imYHapt.:  ö:5_)'<7  SjcjI 'Uro  vpr?iinil  paouruyS  pairTjasSmatdi mazdä  ahurä  '^wä  ~iivä  mainya  spSniitä , yi  ä  axlis  (sd.)  .  ,  "mittelst  der  Tätigkeit  j dieses  Feuers  hier  nahen  wir  uns  dir  zuerst,  I o  MAh.,  mittelst  deines  heiligsten  Geistes  I dir,  der  .  ,"__  Y.j6".i;  —  «/rf/-/ (NS.)  Ti>i: (sd.)  mazdii  ahurahya  ahi  mainyus  v!ii- ahyä  spsnisis  ahl  Y.  36. 3 ;  —  urz-iizist? (s.  I  d)  hvö  ria  . .  paili.jamya  'tan  mazdä ahurahya  (s.  I  Anhang  o)  Y.  3O.  2 ;  — hyat  i'ä  töi  namanqm  väzist^m  fs.  I  d)  'tar» mazda  ahurahya  (s.  I  Anhang  a)  Y.  3!}. 3-  3)  im  gAw.,  persönlich  und  gött- lich gedacht,  meist  als  dem  MasdähAh. angehörig  —  '^wa-  'tuus'  —  bezeichnet (vgl.  Anhang  zu  I ) :  him  nä  mazda  mavaiti päyütn  (sd.)  dadät  .  .  anyim  ^wahmat '^irasüi  mananhasai yaya  syao'iamüi  ahm
```


## [2026-09-06T16:01:39.634Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -E \"Tat, Werk|Tun, Handeln|in Gang gekommen|in Gang, Marsch|sich in Bewegung setzen\" BRT.txt | head -20"
}
```


### [2026-09-06T16:01:39.692Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T16:01:43.135Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -E \"fra-su|frasu|fra.süta|fraiuta|fra'suta\" BRT.txt | head -20; echo \"--- syav headword ---\"; grep -n -E \"^. *[gj]\\. *s.?yav|1 *syav|syav-\" BRT.txt | head -20"
}
```


### [2026-09-06T16:01:43.262Z] TOOL RESULT

```
3320:•  j.  aSlca-,  atlUL-  m. 'Oberkleid,  Mantel': fraziihm  a'ikiin  vatikämm  Vt.j.iaö;  — at.kSsca  frasusS-.yesi  *'aoamn{sd.)  *aiw- yanhayanti  .  .  yezi  *upar3m  .  .  N.  ff 2.
5203:•  j.  avi,  aoi  I)  Praen.  1)  mitAkk.;  a)  'auf —  zu,  hin  zu  —  (auf  — ),  advcrsus',  a)  bes. bei  Wörtern  der  Bewegung:  tiltrim  . .  yö .  .  vazsite  'i-i  zrayS  .  .  ya>a  tifrii  yim anhat  irsxsö  .  .  airyd.x^ii>a(  ka>a  garöit x^anvanhtn  'vt  gairjm  YLÄ6;  H.  2.  i6^ Yt.5.85  ('oi),  132J  ('ei),  Ä33',  70.151, ;p.8z  2.  St.,  V,7.i8  PüZ.,  5,19',  <.V.i03, Y.  6^.  3  (°oiy,  —  nä  tai  frasusaiti  haca /qfnavö  raonqm  'vi  bansiiavS  gairinqm V.5.2;  i';  —  ^J  .  .  vTjasnt  vlspais  ''vi karh-qn  Yt/0.89;  64,  72.4*,  7^.94,  Y, O5.I  (Vi),  0,5.5  ('<»■>;  —para.aki  upa.- vazat3uha  °vi  nmärum  ..  V.  22, 7;  13, Y.57.23,  24,  Yt70.3o;  —  urvänB pärayänli '  °i7  ahurahi  .  ,  "vi  atmsanqm  .  ,  °vi'^ \gätvS  .  .  'i'i  gars   nmätam  Y.  1^.32;  —
8623:•  j.  uz-uätSna- ■>  Adj.  'leblos':  yat  .. nliriia  .  .  apuhrTm  (sd.)  nijassi  'na  V, 5.45; — ym  näirika  . .  apuirim  *Vw»w'' nijasäUi  Vd.  ig;  —  *«i  (ÄPn.)  .  .  uäana- ?'(kW  vTspä  frasumaitJs  (sd.)  P.  5Ä
8783:rlspii  frasumatlii  (sd.)  P.^iA;  —  Äi>  turo  ^j,  jgg.  __  vgl.  .iin^u-U.!»,,-.
9093:•  j.  ustana'vant- Adj.  (fem.  -Taiii')  'leben- dig, lebend':  uzuitani  .  .  "vaitls  (APf.) vupa  frasumaitls  (sd.)  P.ji?;  —  hs  aet-ö 'valqm  ih-a.vaima  (sd.)  apayeiti  "er  allein unter  allen  lebenden  (Geschöpfen) . ."  Yt.
11897:auf  diese  Weise',  zurückweisend;  a)  avavat kavaim  ^armd  ya%a  yat  .  .  us./ravayBit (sd.)  . .  f  asti  kavalm  ifarmS  %rä^nm  . . Yt.  ig.  6Bi  b)  als  Korrelat  von  iya^ 'wie':  s?rao^  ita  astü  .  .  hyaf  paour- vXm  f  ust3mfm(sd.)cyt  Y.  56.  i,  Vr.  g. 7.  c)  bei  elliptischer  Ausdrucksweise im  Sinn  von  'das  (Gesagte)  gilt  ,  .':  Aaea hä  vaxiat  [.  .]  mailyai  xsape  palrisacäiti t°  Aatna  t°  *ami.gäme  ".  .  das  gilt  im Winter,  das  im  Sommer"  N.ji;  48',  103Q); —  tat^giiniakva  %rigamlm  f  lkaesaAe{sA.) f  *vtkayehe  f  arüaAe  f  arikavanS  F. 2jb.  7)  wie  unser  schwach  toniges  (zeit- liches und  räumliches)  'da'  zur  Belebung einer  Schilderung  (usw.):  na  t°  para.- irihyeiti  avi  jqfnavS  raonqm  a  f  mirTy^m .tisvazaitcupa  tarn  kiArptm  fratauAaraiü \..3t°  msnyim  utvazaite  ,  .  avi  bar^i- navs  gairinam  . .  nä  f  frasusaUi  .  .  upa
12842:■L  dardinti,  t^yjäyai,  äärayati;  dflai, ;  Dp.  darrJ- dani  gr.  ipenif.  —  Pü. ;  darrUan.  —  ')  Nur  im Inf. •  j.  *dar-  V.  'achten',    Ptaes,  27  dir^ya-. —  PPfP.   •dir^ta-. 'achten':  s.  adsrstö.'. mit  3  'achten  auf  — ,  wachen  über  — ' (Akt.):    darssa  na  pairyaoxtaca  umllanä *äd»nyäte ''  nyde  uslanavaitt!  vJsph  frasu- maitls  (sd.)  P.  S^-
15551:I):  fei,  (lu  II):  api  hac,  (lu  III):  apc;  s.  noch No.  2  ff.,  6,  8  ff.  —  0  Hds.  pari.  —  »)  D.  i. TOT  oder  nach  der  Rezitation  der  Gs%ä%\  Pü.: pas  -  tu  fralum    kär   ape   kuntt  pas   apasläk gffujet-aiävp/i—ku  afaitik  (Rest  weggelassen). —  3)  Pü.:  ausgelassen.  —  4)  Unsicher.     Pü.: apar.     -    S>  Vgl.  Bipi  II  I   i  (Sp.  83  ">■)■  - 6)    PD.  :    apar  pa  barsm.    —     ?)   S.  dam  Dbr, VglS.  /.   71 1.  —  »'  PS-:  i'  onrfflr  an  apar.  — 9)  Pü. !  *ia/.  —  10)  Pü. :  undeutlich.  —  "»  Pii, : apF,  —  ")  Wörtlich :  "non  profuse  sine  semine', eine  Vermischung  der  beiden  sinngemäss  rich- tigen  Ausdrücke   */rai>har>iäl  pairi  xl'    und tt/raa/iamäl  paiti  xs',    vgl.  anädntxlay-  No. I.     Pü.:    fehlt.    —     '.0  Pü.:    hat.  —   M)  Wo NA.  unrichtig  abteilt ;    s.  Vt,  3,  la  —  >5)  Wo die  Hds.  das  2.  Mal/aiV/  bieten;  s.  Yt.  j.  14. •  j.   *pairi.aoxtay- ",    pairyaoxtay-    f. i)    'Aussprache,    Vortrag':  yezi  araitrim (sd.)  *'ta'^  pairi Jta  Ü.32.         2)  'Zuruf, Befehl':    dansa    nä    'tala    (LS.  als  IS.) uzustanä    *adir»yäte  .  .  frasumaitls  (sd.)
18053:•  j.  frasu'mant-  Adj.  (fem.'maifl-)  'sich vorwärts  bewegend,  beweglich' :  dansa  na pairyaoxlaca  taus/a/iä  *äd)rfydte  nyäe a^tanavaitls  vlspä  'maitls  (APf.  statt  n.) "durch  Blick  und  Zuruf  Überwacht  man (alle)  leblose,  leitet  man  alle  lebende  be- wegliche Habe"  P.5*'>.
21228:jAw.:  i)  mit  Ind.:  ^°  aiAlA  amS  mkanie spanasia  irista  . .  ka  hl  asti  aha  V.3.  36; iX  36,  37,  12.  i;  —  y  .  .  caratd  dva  mS apajw>tayaaa  V.y.49;  —  hs para  mintS daSvS  .  ■  y  maiys  maitm  xhtdra  avi franhirftaiti  y  vä  mafys  .  .  xsudranqm *pairi,gmrvayäti  V.  Ä32;  —  hs  ba  .  . arhtqm  MtyS  y  na  paurva  frabda  (Sp. 984  o) /rabdsJrajB  framalxaiti  V.  j8.  40; 34,  46,  54;  —  y  aoxte  aiia  . .  a%a  *ha *x/ayete..  haxäsit (sd.)  ü.g;  7;  — y  hakat *amrute  . .  aliü  *ratu/rii y5 . .  N.24;  — ta^a  y  paiti.barvnti  yä  .  .  äjayaurra N,54;  —  yl>  sSne  piÜr^m  jainti  . . yas»*'^ tat . .  täyus  . .  para.baraiti  dasa  (sd.)  oSj/ päili  afsl  aiayai(sd.)  Y.  13. 10;  —  aät y  bavaiti  avijpastS  sasta  .  .  ta  hascit upajbayäte  Yl  13.  69;  46;  —  yO  nars snaHmt  usihiltaiti  a^at  hl  ag^r^ptam  (sd.) y  frasusaiti  altai  hl  avaoirist»m  {sd.)  y . . Y.4.1T,  —  al^  zr  narS  paityeinti  (sd.) *aslS.vitotus  pgsanaiti  yasla'>''  isui..p»ia- naiti yasca^..Y .4.^^^^; — h^m  ita  (s.Ntr.) tltao^ra  bavairiti  (Sp.  939  O.)  yasj*^  tava frabannte  drvantö  . .  ".  .  dann  .  .  wenn (sie)  dir  darbringen  . ."  Yt.5. 94,  2)  mit Konj.  (oder  Inj.);  y  .  .  masdayasna  .  . nassum  frajasqn  ku%a  . .  v^myqn  "ange- nommen den  Fall:  die  M.  stossen  aul einen  Leichnam  .  .,  wie  .  .?"  V.  6. 36: 5.45,  Äi,  4,  J&i;  —  y  •■  spä  avaca va  bavat , ,  kuha  . .  vjrxyqn  . .  masdqyasna V.  13.  39;  35;  — y  . .  masdayasna  bal^atai (sd.)  fravasänte  katärö  paurvB  ämayänie (sd.)  V.  7. 36;  —  y  iavani  (sd.)  aiwi.- sasls  . .  eis  aiAhe  asti  balfazd  Yt  J4.34; —  y  afvS  zaata  (sd.)  frayatäiti .,  zaoiars gatava  N,  tf/;  70;  —  y  ahmt  nmlne  . . nairika  daxstavaiti  arthal  y  vä  ..  *aipi.- irytS.gatus  isd.)  altala  .  .  V.5.  59;  — y pouruiaist^a  hanjasänte . .  t^m  i^ra  ha*- Jasante  V,  7,44;  YL//.6;  —  yas/a^>  .  . väcim  paiti  taBtii' {sd.)  ar?hat  nsil.. täyus .  .  para.baraiti  Y.J3.40;  —  y  ma^äia frayazantt  .  .  rüsit  t^ra  airyä  daiähävS /ras  hyätYt.i4.^&;  — y paoirim . . itryntäl .  .y ' . ,  ktrmtät'  ava  hö  miryaite  anämStS ZT  ais6  Y.y.^T,  —  nthenyesi:  yeti/a  alte asti  . .  gar>mBkva  (sd.)  vjiänte  y  vä  aiU gar^ma  (sd.)  i^ars^a  stamaruM  .  .  apa.- daiai  .  .  aiühai   haca  .  .  bavainti  p»sB.-
22133:barsein,  sva.)  so  dass  es  gesehen  werden kann,  sichbarlich,  vor  aller  Augen' :  V  ahmat haca  i^arfttS  mgrrjahe  Afhrpa  frasusat "sichtbarlich  in  Gestalt  eines  Vogels  . ." Yt  j_9.34;  —  v°  ahmat  para  dafva  pataym "sichtbarlich  trieben  sich  vor  ihm  dieZ^cffu herum"  Ytiß- 8o'>;  80'.
27591:taxtmm  frasuitim  4*  itsUm  (Sp.  420) Yt./p.4a.
28527:avi  frasusSni  zqm  avi  ni.urvis-
--- syav headword ---
12978:KompA.  —  Zum  V.  dar!- ;  vgl.  p.  didorlay:  — Pü.;  ikaj'l.  —  1)  Vgl.  darsyav-,  womit  sich  die obigen  formen  bei  der  Annahme  vereinigen lassen,  dass  'hs,  •stm  nach  S  xS.  14  für  •syi'l, 'him  stehen.
28503:Yt  II.  4;  —  vavam  luye  ra^wya  manavAa . .  vacatiha  . .  '%na    A.  7. 1 1 ;    —    sakai mananhe  . .  vacauhe  . .  *^nahe  (statt  Dat) Y.  68. 4,  Any.  2  (wo  •'kna).        Undeutlich : tusit  kl  asi  *''knanam  v^nzySii  N.  16. KompA.,  E.    —    Zum  V.   syav-.    —    ai.  vgl. ryaulnä-  n.  'Unlernehmung'.    —    Pü.:  iuniin, (lü  Y.  28.  5,  43-  5):  i-unisn  iar,  (zu  V.  /.  11, 16,   s-  21.  39.  41):   '"'"'^-    —    ''    Die  regel- rechte  Fchteibung  ist   '%tt'  für  jAw-,    °%an'  , ffirs  gAw.  —   ä)  S.  Pü.  —  i'>  S.  Sp.   1713  m. ' No.  3.
28515:•  p.  äiyav-,  g,  Syav-,  j.,  g.  äav-'>  V. 'sich  in  Bewegung  setzen'.  Praes.  i  syav-, sav- :  A»-'*,  2  siyava-,  14  iüsa-'*,  30  (Kaus.) /ävaya-;  j-Aor.  i   /ae/-;  Per  f.  i   suiu-*\
```


## [2026-09-06T16:01:49.922Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '28490,28540p' BRT.txt"
}
```


### [2026-09-06T16:01:49.972Z] TOOL RESULT

```
ha  . .  aia  •%anfm  va^attha  . .   '%anä  .  .  spmtäi  *mainyavi  dad^mahT  Y.
^^^(sd.)  Y.J2.5;  —  ^awfT'a- I5Ä  6;  *P.  2^  (•&«•);—  vgrikraynahe  paiü
anai»has£avar)k7u^..'^anahyä  manahi .  .vacahi ..  '^ne  Yt  14.  3&;  —  mit
aXyaca  Y.  jj.  14;  45.8; —  a/j  näherer  Bestimmung  durch  ein  Adj.:  Jstuyf
.  .  manahica    vacakica    "hanSixkumatim     manö    hüxtsm    vacB    Avarst^m
iM(sd.)iä  Y.J0.3;47. 1.       An-x'^kantm  Y.72.8;  Vr.  2.  5,  Aog.  27,  Gs.  7^j,
•%an3i  üslnti  katvS  xsd^rfm\Y\..i6.(>,  V.i&.ij';  —  vanAsu!  manaa/a
)  'Hanäi  ..ya%a  *vä  *haxml'.  .  vacanhs  ..  •'hnahe  taokräbyS  Any. s;
b)  im  j  AiAT.  (auch  wie  facinus .  —   alasara  manaa/ia  . .  va^anAa  . .  '^m
dby  Google
i7'3
SyaoS-ananam
äyav-  mit  avi  und  ß-a        1714
Yt  II.  4;  —  vavam  luye  ra^wya  manavAa . .  vacatiha  . .  '%na    A.  7. 1 1 ;    —    sakai mananhe  . .  vacauhe  . .  *^nahe  (statt  Dat) Y.  68. 4,  Any.  2  (wo  •'kna).        Undeutlich : tusit  kl  asi  *''knanam  v^nzySii  N.  16. KompA.,  E.    —    Zum  V.   syav-.    —    ai.  vgl. ryaulnä-  n.  'Unlernehmung'.    —    Pü.:  iuniin, (lü  Y.  28.  5,  43-  5):  i-unisn  iar,  (zu  V.  /.  11, 16,   s-  21.  39.  41):   '"'"'^-    —    ''    Die  regel- rechte  Fchteibung  ist   '%tt'  für  jAw-,    °%an'  , ffirs  gAw.  —   ä)  S.  Pü.  —  i'>  S.  Sp.   1713  m. ' No.  3.
•  j.  SyaoS'ananam:  zitirt  die  zweite,  mit diesem  Wort  beginnende  Hälfte  von  Y. 27.13;  zB.  li.46.         Vgl.  ijao^nSJat-.
•  g.  Syao^anäi  Inf.:  s,  unter  ^yao%ana- (Sp.  1711U-}.
Zum  V.  syoT/:
•  j.  äyaoSnä-varaza-  m.  'der  die  Tat begeht,  Täter' :  yai  tat  paiti  irisytiti  aii»kal hata  'za  a^a  bavainti  p>sS.tanvS  "wenn  .., so   werden    dadurch  die  Täter  zu  PP  V.
•  j.  *syao9Tiam.v«r«z-'J  Adj.  'eine  Tat tuend  sva.  ein  Geschäft,  einen  Dienst  ver- richtend' '"^-ya^a . .  apinnayakim . .  'vinzim virssyäi  syao'hn>m^'>  paitt  taröpviw?i/i i/ai^yat..  ^'a.h  ob  er  ein  in  seinem  Dienst tätiges  ,  .  Kind  —  es  verrichtet  einen Dienst^'  —  mit  schlechter  Nahrung  ver- sähe .  .'■  V.  13. 33-
Komp.  mit  AS.  im  1.  Glied.  ~  Fa.:  iiinün varz,  er!.!  /  k-mmd  ai  ö  bun.  —  O  So  K  1, L4,  Pt2;  NA.  "S«üPflr'.  —  »)  Vgl.  N./Oj.— 3>  Die  Worte  viT?tyäl  sy'  sind  Glosse  zu  ly'.
•  j.  äyaolhiö.tät-  f.  \lyao%TiaXwxD.,  d.  i.) 'die  mit  dem  Wort  iyao^ananam  be- ginnende Stelle,  die  Stelle  'syao%ananqm' des  ^/;««(j;'a»»yagebets':  *'täitya^^  (LS.) *hävanaHbya  paitt.jatiAsit  "bei  der  Stelle fy'  soll  er  sich  zum  Mörser  begeben" N.  1?/;  —  /rä  ml  spanyä  manivä  vavaca (sd.)  iiTspqm  asaonö  stlm  .  .  'tättya  syao- 'i^nanqm  aahiuS  mazääi  ". .  mit  der  Stelle sy,  (nämlich):   ^iy.  a.  m.'"  Y.ig.g.
VgL  us/a/äl-  2.  —  Pü. :  /a  syai>%anaHqni  ra- -jiisniA,  pa  tanisn  rauiiiniA.  —  ■)  Hds.  '%an3.'.
•  g.  Syaoman-  n.  Tat,  Werk':  drüjasca fairimatsisiä  -mam  (NP.)  aipj  daibitänä (Sp.  761  0.)  Y.y2.  3.
Zum  V.  lyo"-  —  Vgl.  !yao%na-.  —  Pü.:  ri- jecnel  man,  Sü. :  fracärayali  mayi.  Man  trennte ofTenbar  lyao  mqm[
•  g.  lyant-  Adj.,  PPA.:  s,  siay-.
•  p.  äiyav-,  g,  Syav-,  j.,  g.  äav-'>  V. 'sich  in  Bewegung  setzen'.  Praes.  i  syav-, sav- :  A»-'*,  2  siyava-,  14  iüsa-'*,  30  (Kaus.) /ävaya-;  j-Aor.  i   /ae/-;  Per  f.  i   suiu-*\
—  PPfP.  •su/a-.  Int  'sBi/i,  's'BtBit,  syao-
1)  'sich  in  Gang,  Marsch  setzen,  pro- Acisci',  miliüLiisch;  i)  ohne  Zielangabe: pasävn^  dadarlis  asiyav^  ya%ä  arminam parärast^  .  .  Bh.  2.  7;  lo,  6,  14,  _J.  3,  11; — pasäzJ'  vistäspa^  *äyasatä  avam  iäram aHyav<^  "da  zog  V.  jenes  Heer  an  sich, er  setzte  sich  in  Marsch"  Bh.j.  1;  — Pasav^  viväna*  hadä  Itärä  nipadiy  (sd.) tyaiy    aHyavJ*  Bh.^.  11.  a)    mit  Inf.:
kauv  kära^  asiyavJ'  .  .  hamaranam  ear- tanaiy    Bh.  ^.  9.  2)    mit    Zielangabe
durch  a)  AkL  'nach  .  .':  pasav^  ka'bü- jiyaf'  mudrSyam  asiyav<^  ya%ä  . .  mu- dräyam   asiyavc^  .  .  Bh.  I.  10;  _y.  6',  5.1;
—  adam  babirum  asiyavam  Bh. /.  19,  18, 2. 1 ;  1 3 ;  —  vahyazdäti^  hadä  kamnaibis *asb3raibis  amu^t/'  aHyavJ'  *pisiyä^uv3- däm  Bh.5. 7.  a)  Adv,  statt  Akk.:  fra- variis  . .  amuh<^  rag!  nämä"  dahyäul  .  . avadä  asiyavJ'  Bh.  2.  13.  b)  abiy und  Akk,,  uzw.  a)  'nach  .  .':  ^vfda*' famä  ..  asiyavc^  abiy  bsbirum  Bh.j.  14; 2. 1,  J.  4.  ß)  'gegen  — ',  in  feindlichem Sinn:  adam  bäbirum  (s.  a)  asiyavam  abiy avam  nadi"iabairam  Bh.  i.  !&.  2 )  "über- gehen zu  -,  Jemands  Partei  ergreifen',  mit abiy  und  Akk.:  iura*  .  .  iami'är''iyi^  (sd.) abara"  haca  ka'bajiyä''  abiy  avam  asiyavt^ Bh.7.11;  16,  2.5,  _j.  s,  13;  —  "uvajiyä hamih'^iya  abava"  abiy  avam  äh''inam aSiyava'  Bh.  /.  16. 1  3)  'an  etwas  (Akk.) herangehen,  (eine  Angelegenheit)  betreiben' : arfhä  (sd.)  ta  yä  voha  fyaväi  manaaßiä ^■33-  8.  4)  'verfahren  gegen  -'  (Akk.): ya  /«»<«■/? (3PPM.)W  adrSngisd.)  jriivänhB y.2g.  3.  5)  'handeln,  tun':  s.  Inf.  syao- ^anäi.  6)  'weggehen,  weichen  von  — ', mit  kaäi  und  Abi.:  i^armO  apammata.. /usal    ifarmB   yimal    haca    .  .    mtrrjake
■  kphrpa  Vt.  75. 35,  Undeutlich;  laosaiti F.5(?)i  —  -svas"^  F.25b(?).
mit  apa  Kaus.  'wegbewegen,  entfernen':
frä    va.    apa    va    lavayeiti    (näml.    ap^m,
I  nach  Pü.)  N.  /q)"'.
mit  aiwi:  s.  Inf.
j     mit  avi  xmA/rä  'fortgehen  zu  — '  (Akk.):
avi  frasusSni  zqm  avi  ni.urvis-
dby  Google
I7I5
iyav-  mit  ui
Siyätay-
1716
yüni  Vt  ly.  $t,  ^  mä  avi  asmarum  fr suta  Yt  ty.  60.
mit   US    Kaus.    'emporheben': xia^rBJi?r>tahe(%A^  gaoSeJbfr^a  u. (näml.   alima   baeioi,    nach  Pii.)    ".  .  soll , er  sie  zur  Höhe  des  Ohrs  emporheben" N.46".  I
mit  /ra  1)  Srorwärtsgehen,  sich  auf-! machen':  armaiU  fraca  Äa  (aS.)9>  vica^ mmanka  (sd.)  V.  2.  i  o ;  —  usihiStat  tara-  \ %ultrS  fralBsat  .  .  V.  jp. 4;  —  jfS  nars\ snaham  usihisiaiti  .  .  yat  fralusaiti  aitat  I hi  avaoiriihm  (sd.)  V. 4. 1 7 ;  18.  \\  PüZ.,  j Y.57.0PÜZ.  (wo  *säsaite);  —  äai  fra-\ Süsmfi  . .  fravasayd  . .  3p>m  a^>mna  (sd.) Yt.  13.  65.  a)  mit  Zielangabe  durch a)  Dax.:  frä  raruyS  aHavaoyS  .  ,  ht^uyqm
V.  2.  11.         c)  sva.  'auseinanderkneten': ydka  nü  maryäka  'xriisii  vmf(sd.)  Visa- sArittm  vayänie  V.  2. 31 ".
JäVayBit  "i-  'yävatt,  eyänayaü;  lyoffhik;  ateyuvimäkk ; "  cnll  eyutäk ;  DD.  iirvad  'er  geht' ,  iuda.  —  Pü. :  raf/att, "  (Kaus.):  rawinTlün;  5.  noch  Xo.  5-S.  [o,  13  ff.
—  ■)  $  ja  z.  —  »  D.  L  iuv-,  I  36S.  1  z.  — 1)  Ich  «ehreibe  n»cb  der  NA.;  doch  s.  die Var,  —  4)  S  'Oa  L  3  "E-  —  S>  S  '^7-  »• Pü.:  s.  m  öai'fl-,  —  *)  Hds.  i»}/.  Pö.  bat nur  eine  nndeuüicbe  Erläutemne.  Da*  Wott ist  wahncheinlicb  m\X /raiutaiä  V.  4.  17  m- sammen zubringen.  —  7)  Pö.:  raflatt  statt  n>- ainUnH.  —  »)  Pb.;  tadäriin.  —  «  Theni.  — w)  Pü.!/räf  «lUan.  —  11)  So  E  I.  ^K./ra- iav:  —  ■»>  Pü.:  pa  fräe  iavihüh,  erl.:  ia  ä/ o/?  ö  *orwn  («/]  *arÄf , .  . —  "J>  Po.:  ir,.fräc ramit  lik  nun .  .fräi  raweiät  hoc  nin/rä?.  — '*)  Pa.  X  pa  .  •  /räc  rawiliüh.
g.   syä-,  j.  Sä-'*  V.  'sich  freuen'.
(iSOPfA.)  Yt  Ä  II  (=;o.  55,  74,  wolPraes.  I  o-ä-.  —  PPfP.  jr>j/tf-,  f'ä/'.i-;  Inf iüs').  ß)   am   und  Akk.;    na  tat  fra-  sätti,  VjW,  'litte.
```


## [2026-09-06T16:02:03.198Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /tmp; ls /home/sfmqrb/git/rishe/site/pages/248.jpg 2>/dev/null; pdftoppm -f 248 -l 248 -r 200 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg248 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


### [2026-09-06T16:02:05.383Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/site/pages/248.jpg
total 8728
drwx------ 4 sfmqrb sfmqrb    4096 Sep  6 12:02 .
drwx------ 4 sfmqrb sfmqrb    4096 Sep  6 10:51 ..
-rw-rw-r-- 1 sfmqrb sfmqrb    1012 Sep  6 12:00 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  180887 Sep  6 11:56 bqt1637_fn.png
-rw-rw-r-- 1 sfmqrb sfmqrb   50592 Sep  6 11:56 bqt1637_kaz.png
-rw-rw-r-- 1 sfmqrb sfmqrb   92182 Sep  6 10:55 bqt1854.png
-rw-rw-r-- 1 sfmqrb sfmqrb   66580 Sep  6 10:57 bqt2023.png
-rw-rw-r-- 1 sfmqrb sfmqrb   69965 Sep  6 11:25 bqt2242crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb   28189 Sep  6 11:25 bqt2417crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb  431133 Sep  6 11:16 bqt2420_fn.png
-rw-rw-r-- 1 sfmqrb sfmqrb    9548 Sep  6 11:25 bqt2meta.json
-rw-rw-r-- 1 sfmqrb sfmqrb   81018 Sep  6 11:16 build213.py
-rw-rw-r-- 1 sfmqrb sfmqrb   67391 Sep  6 11:49 build225.py
-rw-rw-r-- 1 sfmqrb sfmqrb   71757 Sep  6 11:47 build232.py
-rw-rw-r-- 1 sfmqrb sfmqrb   49952 Sep  6 11:57 build234b.py
-rw-rw-r-- 1 sfmqrb sfmqrb   32265 Sep  6 11:51 build234.py
-rw-rw-r-- 1 sfmqrb sfmqrb   24770 Sep  6 12:01 build243.py
-rw-rw-r-- 1 sfmqrb sfmqrb    6504 Sep  6 11:13 c1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3402 Sep  6 11:22 c224_n10.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4812 Sep  6 11:28 c224_n12.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4744 Sep  6 11:22 c224_n1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3203 Sep  6 11:28 c224_n7.png
-rw-rw-r-- 1 sfmqrb sfmqrb   12820 Sep  6 11:27 c229_bibua.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5308 Sep  6 11:27 c229_greek.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5313 Sep  6 11:27 c229_persian.png
-rw-rw-r-- 1 sfmqrb sfmqrb    9059 Sep  6 11:50 c237_n18.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2389 Sep  6 11:50 c237_n3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4987 Sep  6 11:52 c239_kandid2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4734 Sep  6 11:52 c239_kandid.png
-rw-rw-r-- 1 sfmqrb sfmqrb   12852 Sep  6 11:52 c239_persian.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4087 Sep  6 11:52 c239_sandarus.png
-rw-rw-r-- 1 sfmqrb sfmqrb   15240 Sep  6 11:54 c246_caiique.png
-rw-rw-r-- 1 sfmqrb sfmqrb   84366 Sep  6 11:54 c246_n2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   51690 Sep  6 11:54 c246_n6.png
-rw-rw-r-- 1 sfmqrb sfmqrb    7793 Sep  6 11:13 c2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4371 Sep  6 11:13 c_gacele.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3485 Sep  6 11:16 c_harmathan.png
-rw-rw-r-- 1 sfmqrb sfmqrb   12347 Sep  6 11:20 c_hdr.png
-rw-rw-r-- 1 sfmqrb sfmqrb    9147 Sep  6 11:16 c_herman2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3841 Sep  6 11:16 c_herman.png
-rw-rw-r-- 1 sfmqrb sfmqrb   12691 Sep  6 11:20 c_ieuo.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2071 Sep  6 11:26 c_ijlak2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   14654 Sep  6 11:20 c_ijlak.png
-rw-rw-r-- 1 sfmqrb sfmqrb   12239 Sep  6 11:20 c_latis.png
-rw-rw-r-- 1 sfmqrb sfmqrb    6280 Sep  6 11:13 c_mag.png
-rw-rw-r-- 1 sfmqrb sfmqrb  169482 Sep  6 11:58 crop_1648b.png
-rw-rw-r-- 1 sfmqrb sfmqrb   45260 Sep  6 11:57 crop_1648.png
-rw-rw-r-- 1 sfmqrb sfmqrb  305924 Sep  6 11:57 crop_1731.png
-rw-rw-r-- 1 sfmqrb sfmqrb    6971 Sep  6 11:03 crop1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    8619 Sep  6 11:03 crop2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5240 Sep  6 11:03 crop3.png
-rw-rw-r-- 1 sfmqrb sfmqrb   12820 Sep  6 11:05 crop_germ.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3408 Sep  6 11:05 crop_guthjo.png
-rw-rw-r-- 1 sfmqrb sfmqrb  111118 Sep  6 11:19 crop_habl.png
-rw-rw-r-- 1 sfmqrb sfmqrb    9001 Sep  6 11:05 crop_node12.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5564 Sep  6 11:05 crop_node1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5286 Sep  6 11:05 crop_varathra.png
-rw-rw-r-- 1 sfmqrb sfmqrb   11652 Sep  6 11:13 c_xzn.png
-rw-rw-r-- 1 sfmqrb sfmqrb   83691 Sep  6 11:19 gen215.py
-rw-rw-r-- 1 sfmqrb sfmqrb    2303 Sep  6 11:25 j.json
-rw-rw-r-- 1 sfmqrb sfmqrb     228 Sep  6 11:06 jscheck.js
-rw-rw-r-- 1 sfmqrb sfmqrb   37376 Sep  6 11:09 mk201.py
-rw-rw-r-- 1 sfmqrb sfmqrb   77132 Sep  6 11:11 mk207.py
-rw-rw-r-- 1 sfmqrb sfmqrb   61121 Sep  6 11:11 mk208.py
-rw-rw-r-- 1 sfmqrb sfmqrb   80041 Sep  6 11:14 mk214.py
-rw-rw-r-- 1 sfmqrb sfmqrb   67513 Sep  6 11:27 mk217.py
-rw-rw-r-- 1 sfmqrb sfmqrb   74459 Sep  6 11:33 mk218b.py
-rw-rw-r-- 1 sfmqrb sfmqrb   17605 Sep  6 11:25 mk218.py
-rw-rw-r-- 1 sfmqrb sfmqrb   50138 Sep  6 11:24 mk222.py
-rw-rw-r-- 1 sfmqrb sfmqrb   78297 Sep  6 11:32 mk223.py
-rw-rw-r-- 1 sfmqrb sfmqrb   47928 Sep  6 11:38 mk224.py
-rw-rw-r-- 1 sfmqrb sfmqrb   53093 Sep  6 11:40 mk226.py
-rw-rw-r-- 1 sfmqrb sfmqrb   51303 Sep  6 11:39 mk228.py
-rw-rw-r-- 1 sfmqrb sfmqrb   29152 Sep  6 11:37 mk229.py
-rw-rw-r-- 1 sfmqrb sfmqrb   47535 Sep  6 11:47 mk230.py
-rw-rw-r-- 1 sfmqrb sfmqrb   64267 Sep  6 11:59 mk235.py
-rw-rw-r-- 1 sfmqrb sfmqrb   73422 Sep  6 12:02 mk237.py
drwxrwxr-x 2 sfmqrb sfmqrb    4096 Sep  6 11:44 p216
drwxrwxr-x 2 sfmqrb sfmqrb    4096 Sep  6 11:52 p233
-rw-rw-r-- 1 sfmqrb sfmqrb   33321 Sep  6 11:51 part1.json
-rw-rw-r-- 1 sfmqrb sfmqrb   54688 Sep  6 10:58 pg201.png
-rw-rw-r-- 1 sfmqrb sfmqrb   70083 Sep  6 10:52 pg204.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77858 Sep  6 10:52 pg206.png
-rw-rw-r-- 1 sfmqrb sfmqrb   67371 Sep  6 10:53 pg207.png
-rw-rw-r-- 1 sfmqrb sfmqrb   59146 Sep  6 10:53 pg208.png
-rw-rw-r-- 1 sfmqrb sfmqrb   53054 Sep  6 11:00 pg209.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74515 Sep  6 11:02 pg211.png
-rw-rw-r-- 1 sfmqrb sfmqrb  141781 Sep  6 11:03 pg212hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   75961 Sep  6 11:02 pg212.png
-rw-rw-r-- 1 sfmqrb sfmqrb   83761 Sep  6 11:03 pg213.png
-rw-rw-r-- 1 sfmqrb sfmqrb   83752 Sep  6 11:01 pg214.png
-rw-rw-r-- 1 sfmqrb sfmqrb  194102 Sep  6 11:05 pg215hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  117034 Sep  6 10:54 pg215.png
-rw-rw-r-- 1 sfmqrb sfmqrb   76564 Sep  6 11:13 pg216.png
-rw-rw-r-- 1 sfmqrb sfmqrb   82798 Sep  6 11:16 pg217.png
-rw-rw-r-- 1 sfmqrb sfmqrb  147278 Sep  6 11:13 pg218hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   82099 Sep  6 11:13 pg218.png
-rw-rw-r-- 1 sfmqrb sfmqrb   71937 Sep  6 11:19 pg219.png
-rw-rw-r-- 1 sfmqrb sfmqrb   63280 Sep  6 11:18 pg220.png
-rw-rw-r-- 1 sfmqrb sfmqrb   71497 Sep  6 11:18 pg221.png
-rw-rw-r-- 1 sfmqrb sfmqrb  118895 Sep  6 11:16 pg222hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   84108 Sep  6 11:16 pg222.png
-rw-rw-r-- 1 sfmqrb sfmqrb   79615 Sep  6 11:18 pg223.png
-rw-rw-r-- 1 sfmqrb sfmqrb   90848 Sep  6 11:22 pg224hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   55412 Sep  6 11:15 pg224.png
-rw-rw-r-- 1 sfmqrb sfmqrb   80963 Sep  6 11:32 pg225.png
-rw-rw-r-- 1 sfmqrb sfmqrb  161218 Sep  6 11:26 pg226hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74322 Sep  6 11:19 pg226.png
-rw-rw-r-- 1 sfmqrb sfmqrb   54381 Sep  6 11:31 pg227.png
-rw-rw-r-- 1 sfmqrb sfmqrb   52519 Sep  6 11:25 pg228.png
-rw-rw-r-- 1 sfmqrb sfmqrb   78760 Sep  6 11:27 pg229hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   42112 Sep  6 11:26 pg229.png
-rw-rw-r-- 1 sfmqrb sfmqrb   65310 Sep  6 11:32 pg230.png
-rw-rw-r-- 1 sfmqrb sfmqrb   69894 Sep  6 11:34 pg231.png
-rw-rw-r-- 1 sfmqrb sfmqrb   67111 Sep  6 11:35 pg233.png
-rw-rw-r-- 1 sfmqrb sfmqrb   82071 Sep  6 11:44 pg234.png
-rw-rw-r-- 1 sfmqrb sfmqrb   47149 Sep  6 11:44 pg236.png
-rw-rw-r-- 1 sfmqrb sfmqrb  125593 Sep  6 11:50 pg237hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   67972 Sep  6 11:50 pg237.png
-rw-rw-r-- 1 sfmqrb sfmqrb  168221 Sep  6 11:52 pg239hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   78380 Sep  6 11:51 pg239.png
-rw-rw-r-- 1 sfmqrb sfmqrb   81131 Sep  6 11:51 pg240.png
-rw-rw-r-- 1 sfmqrb sfmqrb   97613 Sep  6 11:49 pg242.png
-rw-rw-r-- 1 sfmqrb sfmqrb   80947 Sep  6 11:59 pg244.png
-rw-rw-r-- 1 sfmqrb sfmqrb   80632 Sep  6 11:55 pg245.png
-rw-rw-r-- 1 sfmqrb sfmqrb   79253 Sep  6 11:54 pg246.png
-rw-rw-r-- 1 sfmqrb sfmqrb   49887 Sep  6 12:02 pg248.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1209522 Sep  6 11:39 sin_goog.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  147680 Sep  6 11:20 sns167.jpg
```


## [2026-09-06T16:02:08.384Z] TOOL CALL #21: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg248.png"
}
```


### [2026-09-06T16:02:08.799Z] TOOL RESULT

```

```


## [2026-09-06T16:02:08.794Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-06T16:02:20.435Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; S=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad; pdftoppm -f 248 -l 248 -r 600 -png -singlefile EtymologicalDictionary-persian-english.pdf $S/pg248hi && python3 -c \"\nfrom PIL import Image\nim=Image.open('$S/pg248hi.png'); print(im.size)\nw,h=im.size\n# persian box approx x 0.55-0.78, y 0.175-0.21 of page based on 200dpi coords (x 850-1190 of 1700 wide -> .50-.70; y 390-455 of 2200 -> .177-.207)\nim.crop((int(0.48*w),int(0.170*h),int(0.75*w),int(0.212*h))).save('$S/c248_persian.png')\n\"; ls -la $S/c248_persian.png"
}
```


### [2026-09-06T16:02:25.090Z] TOOL RESULT

```
(5100, 6600)
-rw-rw-r-- 1 sfmqrb sfmqrb 3046 Sep  6 12:02 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/c248_persian.png
```


## [2026-09-06T16:02:27.712Z] TOOL CALL #23: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/c248_persian.png"
}
```


### [2026-09-06T16:02:27.724Z] TOOL RESULT

```

```


## [2026-09-06T16:02:30.693Z] TOOL CALL #24: Bash

```json
{
 "command": "S=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad; python3 -c \"\nfrom PIL import Image\nim=Image.open('$S/pg248hi.png'); w,h=im.size\nim.crop((int(0.52*w),int(0.185*h),int(0.80*w),int(0.215*h))).save('$S/c248_persian2.png')\n\""
}
```


### [2026-09-06T16:02:32.861Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T16:02:34.997Z] TOOL CALL #25: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/c248_persian2.png"
}
```


### [2026-09-06T16:02:35.013Z] TOOL RESULT

```

```


## [2026-09-06T16:02:38.515Z] TOOL CALL #26: Bash

```json
{
 "command": "S=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad; python3 -c \"\nfrom PIL import Image\nim=Image.open('$S/pg248hi.png'); w,h=im.size\nim.crop((int(0.54*w),int(0.192*h),int(0.79*w),int(0.211*h))).resize((1500,int(1500*(0.211-0.192)*h/((0.79-0.54)*w)))).save('$S/c248_p3.png')\n\""
}
```


### [2026-09-06T16:02:41.033Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T16:02:43.250Z] TOOL CALL #27: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/c248_p3.png"
}
```


### [2026-09-06T16:02:43.263Z] TOOL RESULT

```

```


## [2026-09-06T16:02:48.497Z] TOOL CALL #28: Bash

```json
{
 "command": "S=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad; python3 -c \"\nfrom PIL import Image\nim=Image.open('$S/pg248hi.png'); w,h=im.size\nc=im.crop((int(0.54*w),int(0.200*h),int(0.79*w),int(0.222*h)))\nc=c.resize((1600,int(1600*c.size[1]/c.size[0])))\nc.save('$S/c248_p4.png')\n\""
}
```


### [2026-09-06T16:02:50.867Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T16:02:53.475Z] TOOL CALL #29: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/c248_p4.png"
}
```


### [2026-09-06T16:02:53.495Z] TOOL RESULT

```

```


## [2026-09-06T16:03:06.428Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== PHD šudan ===\"; grep -n -i -E \"^ *(sw-|sudan|šudan|saw-)|sudan \\[|YHMTWNtn\" PHD.txt PHD_mackenzie.txt | head -20; echo \"=== NYB glossary sutan ===\"; grep -n -E \"\\bsutan\\b|šutan|SDKWN|YHMTWNtn\" NYB_vol2_glossary.txt | head -20"
}
```


### [2026-09-06T16:03:06.534Z] TOOL RESULT

```
=== PHD šudan ===
PHD_mackenzie.txt:4707:sudan, say- [swtnl, s)d- I N -] rub.
PHD_mackenzie.txt:4855:sudan, saw- [OZLWN-tn l < A .v )zl; lwb- I M lwdn, lw-, N -] go.
PHD_mackenzie.txt:10145:saw-I                    -,~,       wanand                          ~\\,
PHD_mackenzie.txt:10147:sudanI                 \\to,~,      nozdah
=== NYB glossary sutan ===
188:SBW?: S'BU, st. abs. of st. emph. S'BUTA matter, affair, business SDKWN-: SDO to split
392:ämatan [Y"TWN-tn']dy-to go, to come, to arrive, to come on, to issue, to appear, passim; together with other vbs.: àyet u tapet 2219.13.16 (3d p. sg.); à? u den stāt 9926-27, apt-š Amat 2 zan nisastak dit hav- ing arrived there he saw ... 617; druyist šutan u āmatan to go and come in due
445:motion: šutan, dväristan, opastan, ete., and with ēstātan and nisastan (also ~ 6). — 2. prep. in, local, temporal and figura- tive: ~ Pārs; ~ im xünak P1:6; ~ miyàn i in the middle of 865; ~ han hangam at the time 613; ~ ham zamān at the same time 127°; ~ zamān in due time 221, etc.; ~ sap in the night 529, 614; ~ hàsr for a single moment 663; ~ hàn in the meantime 5615-17; — xtatäyeh + Xösrör 1184; ~ Vistasp šāh kisvarikan when V. was the emperor of the world 365; — freftür ~ : concerning 3419-20, 10923; spasdārēh ~ , an-ispās ~ : to, against; with other substantives, v. these separately ; — together with another prep.: ~ 6 into, on to, up to: ~ 6 nun 404; with apakandan, burtan, guméxtan (also without 6), hištan, kartan (v.s.v. kar); apar ~ 402, — Av. (131 sq.) antara, antarš, OP antar (better read antara^); MPrthPrs ’ndr; Paz. NP andar; v. also niyandar.
476:apäc [L'WEIL ; ’p’c] 1. adv. back, back- ward (opp. frāc 25?-*), again: hac 7-salak ~ for seven years 16?5; hac én and (q.v.) sal ~ 1674; — prev. with vbs. of motion, e. g. dmatan, šutan, vastan, ete., and many others, e.g. guftan, gumeatan, etc. — 2. prep. with (= apäk) 42%. — 1. < *apācā instr. adv. from Olr adj. *apdnk-, weak st. apük- and apác, derived from Av. (72) apa, OP apa, cf Skr apdfic- ‘situated be- hind’; MPrth °b’c; Paz. awāž; NP baz. — 2. < *upācā, instr. adv. from Olr adj. *wpünk- derived from Av. (388 sq.) upa, OP upä ‘under, with’; J-Prs ?b?z ‘with’ (common); v. further apäk.
972:the v. n. and the pt.: bé tacét, bé tacitan, bé tacióneh (e.g. 564); be šutan to go away, to disappear, bē šutak gone, van- ished 5?; etc. — b) denoting the per- fective aspect of the act, viz. that it comes to an end, or has its limit: with the pret. it gives it the sense of an act completed in the past, as in French the passé défini or in Lat. the perfectum historicum; with the pres. it denotes the completion of the aet in the future (Milr. has no special future tense); it is very often put before an imp., giving the order a peremptory force; also used in other expressions implying an act of will, cf apdyistan and framūtan; in this sense it does not stand together with an inf., or with a pt., nor with a negation, nor with other preverbs (which themselves give a_ perfective sense): be bavét he will be, but nē bavēt he will not be. The functions a) and b) are often difficult to keep apart. — 3. prep. a) except, but: hec zvandak apdc bà nē mānēt be hàn i ēvak Arjāsp no one but A. alone 2926-27; 2415-16; 964; cärak be man an kas xYāstan nē tuvān it is not possible to request a means from any other than me 34?; followed by a sub- ordinate clause: nisem nē vindät bē ka
1348:drinišn [SDKWN-8n'] 1027, v. n. of
1349:dritan [SDKWN-tn'] drin- [SSDKWN-] to tear to pieces, to slit 502. 1027-8 (v.s. v. daštan). — Av. (689) !dar-, pres. darand- (Skr middle droite). Reading according to FrP 18; BP also darritan darr- = NP dar(r)idan dar(r)-.
1436:. ~ šutan nē šāyet except on a mission ‘of the gods it is not possible to pass 7810-11; ba 801% is not taken up by ~ until 1. 24; bē ka rāst göbeh ēnyā, ham- dātistān ne bavém except if thou tellest the truth we shall not come to terms 1521-22; 6520 v. pditiašdi; hakar ... vicà- ret — ... if he explains ... [it is just right], otherwise ... 1181-15, as in Arab in halla wa'illa; hac Armail ~ except (by) Armail 1151-11, — Av. (138) anyādā, Gath. for anyd@G, Skr anydtha; Paikuli, Prs ’yny’ (Herzfeld p. 132); FrP
2220:kārēcār [k'lyc'l] battle, combat 1198, with: ~ % 8?9, 4 apäk 108%; pat ~ bē dzatan to kill in battle 9722; ~ xtinrécisnéh (q.v.) 1312-13, kéasisn u kārēcār 901; ~ kartan to fight 25-29, passim. 511. 95!1; vas ~ u ozanišn apāk ... kart 138-4; ~ dästan to keep contending, wrestling 329-19; be 0 m~ ìi... šutan to engage in battle with 9617-18 ete. — MPrs kryer, krer (S); Paz. kārīžār, NP kürzür; käre- cas. obl. of kar < OP kära- ‘army’, + cär from Av. (449) 5kar- ‘to move’, cf NP caridan ‘to graze’ and vicar-.
3565:sit [swt'] use, advantage, benefit 6219. 6313.24 ote, — MPrs swd; Paz. sud, NP süd, from Av. (1561) sav- ‘to benefit’, savā- savah- '(eternal) welfare’, cf Sošans. sütak [swtk'] torn to rags 112'*. — Pt. of sutan = NP sidan säy- ‘to rub, to wear, to tear’.
3662:$ón [šwn'] kind, sort, way, manner: pat han i vattar ~ bandet 7471-22, — < *šavana-, from šutan: Bailey, BSOS VI, 1932, 947 n. 1.
3675:šutan [ZLWN-tn'] šav- [ZLWN-), forms v. I, 177, to go, opp. (G)matan to come: hac ki mat hom u apāc 6 ku šavom? whence have I come and whither shall I go? 6245; pat druyist šutan u āmatan that they may go and come safely 8723; ka han damistan Sut when this winter has gone 972; hac man šavdi thou shalt go (fly) off from me 2715; — regularly be ~ to go away, passim; bē o ... ~ to go (away) to; bé ~ to disappear, vanish 9416, to escape 2415-16 ; bē-šutak baxt whose luck is gone, who is off his luck 5?; — andar ~ : tigr tai parr pat aškamb andar šut the arrow penetrated right up to the feather into its belly 3%; to enter 181%, also andar-rón 1813, andarón 1912-13; 7525. 10278; — apāc ~ to go back, to
3846:ul [L^L?] adv. up, used as prev. l. in a purely local sense together with āmatan, estätan, handäztan, hangézénitan, hixtan, kašitan, nikeritan, östätan, patitan, raftan, šutan, vaxšitan, vàzenitan, v. these vbs.; — 2. in a more abstract sense denoting, the start of an action: ul šust he set about washing 417; ul. nipast hénd they lay down 4369-11; ul zātan to be born 44?3.? the literal translation of Av. (1658) us zāy-. — < Olr *róva- (Skr ürdhva- < *fdhua-). Av. (350) aradwa- ‘turned upwards’; MPrs 'wl (S); Paz. (awal, probably a misreading of "wi (but cf J-Prs. wr!).
```


## [2026-09-06T16:03:21.591Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== CHEUNG cyaw ===\"; grep -n -E \"\\*[cć]iau|\\*[cć]yaw|CIAU|ćiau\" CHEUNG.txt | head -20"
}
```


### [2026-09-06T16:03:21.643Z] TOOL RESULT

```
=== CHEUNG cyaw ===
```


## [2026-09-06T16:03:24.516Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i -E \"sudan|šudan|siyav|syav|cyav\" CHEUNG.txt | head -30"
}
```


### [2026-09-06T16:03:24.566Z] TOOL RESULT

```
2514:*NWIR: NP baxsudan/baxSsay- ‘to grant, bestow’, Gur. (Kand.) bas ‘give !’, Ham. 
3780:Pres. them.: impf. IND. 15р. as(i)yavam <a-8-i-y-v-m> (DB 1.84, DB 1.91, DB 2.3, etc.), 3sg. asiyava 
3781:<а-$-1-у-у> (DB 1.80,DB 2.17, DB 2.22, etc.), «a-s-i-y-v» (XPf 33 Ё), 3pl. asiyava" «a-&-i-y-v» (DB 
3818:*NWIR: Widely attested: NP sudan/sav- ‘to become; [obs.] go’, Bal. Sut-/ (supplet. 
3839:*SANSKRIT: cyav ‘(to start) to move, to set out’ (RV+) = EWAia I: 552 f. 
19516:*NWIR: (+ *us-) NP sipari ‘complete’ (+ Sudan: ‘to end, pass, be finished’) || (+ 
21559:*NWIR: (+ *a-) NP asudan/asay-, Kurd. (Sor.) hasanawa/hasé- ‘to rest’ (with sec. h 
22307:*NWIR: NP sudan/say- ‘to rub, wear, tear’, Kurd. (Kurm.) sö-, su-/sutin, (Sor.) su-, 
24130:*NWIR: (+ *upa-) ? NP bisudan/bisav- ‘to handle, feel, touch, rub etc.’ (rather from 
40778:asudan/asay-, 328 
41523:sudan/say-, 340 
41571:Sudan/Sav-, 41 
51594:cyav, 41
```


## [2026-09-06T16:03:26.796Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '3760,3850p' CHEUNG.txt"
}
```


### [2026-09-06T16:03:26.844Z] TOOL RESULT

```
* ап ‘to move, go’ 

*AVESTAN: S(ii)auu- (Sauu-, $0-) ‘to move, go’ || (+ *abi-) ‘to come to’ || (+ *fra-) ‘to 
set, go forth’ || (+ *ui-) caus. ‘to set apart’? = Liste: 70 

Pres. {1} (a)them.: IND. (med.?) 3sg./pl. OAv. Sauuaité (Y 29.3), SUBJ. med. 159. OAv. Siiauuai (Y 
33.8), IMPV. 2sg. YAv. *frašauua (V 2.10, V 2.18); Pres. {2} s-: IND. 3sg. YAv. fraSusaiti (V 5.2, VdPZ 
18.14), 3pl. YAv. frasüsonti (Yt 13.65), med. 3р1. YAv. frasüsonte (Yt 13.42), INJ. 3sg. ()Süsat, SUBJ. 
lsg. YAv. frasusani (Yt 17.57 Е), IMPV. 2sg. YAv. frasusa (Yt 17.60); Perf.: OPT. lsg. YAv. fra 
Susuiiam (Yt 8.11), 3sg. YAv. *frašušuiiat (Yt 11.5); Partic.: pres. YAv. Sauuant-, caus. ҮАУ. 
fra.$äuuaiiant- (N 103), med. YAv. frasauuaiiamna- (Vr 12.2), perf. pass. YAv. "frasüta- (Vr 12.2); Inf.: 
YAv. “aiBisuiti (N 4); Caus.: IND. Zeg. YAv. frasauuaiieiti (Yt 10.36, N 103), 3р1. YAv. visauuaiieinti (V 
2.31 Е), INJ. 3sg. YAv. visauuaiiat (V 2.11), SUBJ. 3sg. YAv. "frasauuaiiat (V 16.7), OPT. 2sg. ҮАУ. 
*frasauuaiiois (Yt 1.24), 3sg. YAv. vi Sauuaiidit (V 8.75 f). 0 OAv. Sauuaité is rather infinitive ?: "The 
form Savaité cannot be 3pl. pres. because of the subj. form in the following yahmai Jima. Ind. and subj. 
cannot stand in parallel in relative clauses of such future value, only modal forms or inf.", Insler, Gathas: 
149 

*OLD PERSIAN: S(1)yav- ‘to set, go forth’ = Kent: 211a 

Pres. them.: impf. IND. 15р. as(i)yavam <a-8-i-y-v-m> (DB 1.84, DB 1.91, DB 2.3, etc.), 3sg. asiyava 
<а-$-1-у-у> (DB 1.80,DB 2.17, DB 2.22, etc.), «a-s-i-y-v» (XPf 33 Ё), 3pl. asiyava" «a-&-i-y-v» (DB 
1.76) 

*MIDDLE PERSIAN: MMP sw-, BMP swb- (‘ZLWN-) /Saw-/ ‘to go>? = DMMPP: 
319b f. 

Pres.: IND. 3sg. MMP Swyd, 2р1. MMP Swyd, 3р1. MMP Swynd, SUBJ. 3sg. MMP Sw’d, 3pl. MMP 
Su па, IMPV. Zeg. MMP sw, 2pl. MMP swyd; Partic.: perf. pass. MMP swd; Inf.: MMP swdn 


*PARTHIAN: Sw- ‘to go’ || (+ *fra-) frs’w- (old caus.) ‘to send (off/forth)’ = Ghilain: 
67, 77, 49 | DMMPP: 319b f., 156b f. 


*Ciau 41 


Pres.: IND. 25р. šwy, šwyh, Swyy, 35р. šwyd, 3pl. šwynd, SUBJ. 2sg. šw'h, 1р1. šw'm, ОРТ. 3sg. hyb 
*šwyd, IMPV. 2sg. Sw, 2р1. šwyd; Partic.: perf. pass. šwd; Inf.: šwdn || (+ *fra-) Pres.: IND. 3pl. fršwynd, 
SUBJ. 1sg. frs’w’n, 25р. frs’w’h, frs’w’, 3sg. frs’w’h, IMPV. 25р. frs’w; Partic.: perf. pass. frswd 
*KHOTANESE: tsu- (tsi-), Tumsh. ccha- ‘to go’ || (+ *ati-) OKh. *ttätsu- (ttátsa-) ‘to 
cross’ || (+ *aua-) OKh. vatsei- (vatsu-) ‘to go down’, Tumsh. vatsy- || (+ *pati-) 
patäts- ‘to give up, abandon’ || (+ *fra-) ? hats- ‘to come out’ || (+ *nis-) OKh. 
naltsu- (naltsei-) ‘to go out? > SGS: 42, 38, 118, 67, 49 

*SOGDIAN: SSogd. Su - BSogd. Sw-, CSogd. sw-, MSogd. šw- ‘to go, walk, move’ 
Widely attested: Pres.: IND. 15р. BSogd. sw’’m, 25р. dur. CSogd. Swysq, dur. BSogd. sw’m "om, 25р. 
BSogd. sw’y, dur. BSogd. sw’’y ’skwn, BSogd. sw’y 'skwn, etc. 


*CHORESMIAN: (+ *abi-) m/fsw- ‘to become reddish (of cheeks), blush’ || (+ *ui-a-) 
y’sw- ‘to go away to; to pass; to defect to; to flow’. Ф According to MacKenzie 
1990: 104, the initial y- of Chor. y’sw- is spontaneous, which is, in my opinion, 
rather a gratuitous explanation. > Samadi: 71, 255 f. 

*BACTRIAN: роо- ‘to go’, ? paor- (caus.) ‘to use, spend’ = S-W, Bact.: 234b 

*NWIR: Widely attested: NP sudan/sav- ‘to become; [obs.] go’, Bal. Sut-/ (supplet. 
raw-) ‘to go’, Kurd. (Kurm.) cun, ёпут (ё1-), (Sor.) ¿ün (či-) ‘to go, leave’, Zaz. 
Siyayis/Sin-, Abyan. šó/š-, Anar. Si/S-, Ard. $0/5-, Awrom. šiáy (only pret.), Fariz. 
-St-/-$-, Yar. -Sö-/Si-, Gz. $-/So(1), Gil. (Rsht.) Soan/s- ‘to go’, Mah. š-/š(Dt-, Khuns. 
č-, (supplet. &i-/um) ‘to (be)come’, (LW ?) š-/št ‘to go, walk’, Ham. Siydn/s-, Isfah. 
S(ev)-/Sezán, Jow. Jo -fu-/a-f-, Khr. be-$i-/da-$-, Meim. be-foj-/a-f-, Nn. $i/S-, 
Natan. -$1-/-8-, Qohr. $6/s-, Semn. -Si(€-), -Sä-/-S-, Sang. -Süj-/Sun-, Shamerz. -Si(n)-/ 
Süm-, Siv. 5-/S1, Soi St-/S-, Sorkh. -šo/ (1sg.) sin, Lasg. -50/ (1sg.) Sin ‘to go’, Ham. 
bär-Siayän/bär-e-5- ‘to flee, run’, (sec. caus.) Abyan. Stia/Stin-, Abz. Süta/Sün- ‘to 
lead’, Fariz. -uni- / -(S)uni-, Yar. -Sün-/-3-uni- ‘to bring (someone)’, Lasg. 6-vi-n/ 
(supplet. -ord- < *à- + *bar'), Yar. -$i- ‘to bring, carry (someone) || (+ *upa- ?) Tal. 
pese ‘to go in, on, up’ 

*NEIR: Oss. I. cewyn/cyd, D. czewun/cud, Yghn. sau-/Säuta, (supplet. éta) ‘to go’, 
Sh. saw-/stid, Rosh. saw-/sawd, Bart. saw-/sud, Sariq. so-/sit, süt ‘to go, become’, 
Yi. (supplet. pres. oy-) sui, M. (supplet. pres. äy-) Soy, Yzgh. (supplet. pres. bad-) 
Sod-, Pash. šwəl ‘to happen, occur’, Wa. caw- (supplet. tayd-) ‘to leave, depart || (+ 
*pati-) Oss. D. fecawun/fecud ‘to pass, drive by’ 

*MISC: Par. čh-/čhī ‘to go, become’, Par. chó ‘going, walking’, Огт. caw-/cawök, 
caw-/c’ék ‘to go’ = c(aw)-/c(aw)ók, Огт. caw-/caw’ék (caus.) ‘to cause to go’ 
*SANSKRIT: cyav ‘(to start) to move, to set out’ (RV+) = EWAia I: 552 f. 

© An Ir. proto-form *siau- (vel sim.) is often found in (older) handbooks, but the 
Ossetic and Khotanese evidence clearly points to an reconstruction *cjau, with 
initial affricate. 


42 *dab 


*PIE *kjeu- ‘to move, go’. Ф Rather with initial labiovelar *k"jeu- on account of 
notably Arm. c'ogan with palatal č‘ (cf. lowc'e- < *löukie- ‘to set fire’), according
```


## [2026-09-06T16:03:38.299Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD; ls; grep -n \"\\[pdf page\" FFD_pages.txt | head -5; echo \"=== search شدن ===\"; grep -n \"شدن\" FFD_pages.txt | head -20"
}
```


### [2026-09-06T16:03:38.357Z] TOOL RESULT

```
FFD_asmaneketab.pdf
FFD_pages.txt
FFD_pages.txt.pages
1:[pdf page 1]
24:[pdf page 2]
59:[pdf page 3]
70:[pdf page 4]
75:[pdf page 5]
=== search شدن ===
115:نحوی و آوایی و متروک‌شدن برخی از واژه‌ها سبب شده است که ماده‌های ماضی و
213:[ ]: آنچه در میان [ ] آمده برای روشن‌شدن مطلب افزوده شده است.
303:۱ داشته» حذف آن دو سیب ضعیف شدن واژه می‌شده است:
331:غالبا با تغییراتی در هجای آغازی» از جمله کوتاه‌شدن 3میانی:
383:و 4 بردن 4 برده‌شدن
404:گرم‌شدن شروع به گرم‌شدن کردن (
414:در ایرانی باستان 18188 < (2 - 8 - 127) «شروع به گرم‌شدن کردنْ» و 1402 «گرم‌شدن)
415:معنی می‌دهد. در فارسی میانه 15ها <ج 12182 و 130 + 1302 هردو به معنی «گرم‌شدن»
831:«اسردشدن) هستند.
1072:7 در ایرانی باستان و میانه و دری به معنی «شدن» هم به کار رفته است:
1106:بدل‌شدن [و 2 ایرانی باستان به 2» ۷87128 جانشین له و ۷۵18 شده است.
1279:است» 130 به معنم «گرم‌شدن» است و 130 به معن «گرم کردن». «تفتن) از 130 آمده
1295:130 به معنی «گرم‌شدن» آمده است. -> تافن و تفسیدن.
1301:مادهٌ آغازی از ريشه به کار می‌رفته است. ريشةٌ 187 به معنی «گرم‌شدن» است. 0 پیش از 5
1403:بازماندهٌ ۹۷۵۵۵* ایرانی باستان. ۵۸:* ساخته شده است از ۸82 با بدل‌شدن 0 به ؟
1431:معنی «خشک شدن» است.
1545:«رفتن» بط «دورشدن از متکلم» اختصاص پافته است.
1705:شدن
1789:ضعیف ريشهٌ قَة: «روانه‌شدن ‏ وکردن» و برای پسوند 2 > آراست.
1943:ساختن مادهٌمضارع از ريشه‌به کار می‌رفته است. ریشةٌ 8۲3 به معنی «خم‌شدن) است.
```


## [2026-09-06T16:03:42.973Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD; awk 'NR>=1690 && NR<=1730' FFD_pages.txt; echo \"--- page tag before 1705 ---\"; awk 'NR<=1705 && /\\[pdf page/ {p=$0; n=NR} END{}' FFD_pages.txt; grep -n \"\\[pdf page\" FFD_pages.txt | awk -F: '$1<=1705' | tail -3"
}
```


### [2026-09-06T16:03:44.567Z] TOOL RESULT

```
ساپ, ساو, که در فارسی دری به کار رفته‌اند» بازمانده‌های 83# پهلوی اشکانی
هستند. 378[2* ایرانی باستان در فارسی میانه به صورت 37 و در پهلوی اشکانی به
صورت 7 درآمده است.
شایسترد
شایست < فارسی میانه 19ر52. 1 مادهٌ ماضی جعلی و از مادهٌ مضارع ساخته
شده است.
شای < فارسی میانه 33 < ایرانی باستان 8-ر۹83*. برای 2 -> آرای. 529« صورت
بالاندة ريشهٌ وهکدو آن به معنی «توآنابودن» است.
شتافتن
شتافت < فارسی میانه 53130» صورت کهنتر 2۳15130 + ایرانی باستان ۵01-3110 *
برای 18 -> آراست. 201 پیشوند فعلی است. ۰8130 صورت بالاندةٌ ريشهٌ ۰۶127 صورت
اصلی 131 است. 0 پیش از 1به ؟بدل شده است. ريشهٌ به معنی «فشار آوردن» است.
در فارسی میانه 55131127 به معنی «فشارآوردن» و «اشتافتن» است.
شتاب + فارسی میانه 053180» صورت کهنتر 2۳8130 + ایرانی باستان 201-8130-8*.
برای ۵ سه آرای.
شدن
شد < فارسی میانه 504 + ایرانی باستان 50-1۵*. برای 1۵ > آراست. 80 صورت
ضعیف ريشةٌ 5۵7و آن به معنی «رفتن» است.
[pdf page 68]
ماده‌های ماضی و مضارع فارسی دری سا ۳و۶
شو < فارسی میانه 32 + ایرانی باستان 32-۵*. برای 2 > آرای.
شست.
شست < فارسی میانه 5081 ج ایرانی باستان 3508-1۵*. برای 1۵ -> آراست. 7504
صورت اصلی 3۷8 است. 4 پیش از 1 به 5 بدل شده است. 7504 صورت ضعیف ريشةٌ
40 و آَن به معنی «تحریک کردن» است.
شوی < فارسی میانه 50 < ایرانی باستان 35200-8*. برای 2 آرای. «شور) به جای
اشوی» جدید است > جستن.
شکافت < فارسی میانه 531 < ایرانی باستان ۴2-31-1۵ برای 12 -> آراست. 2
پیشوند فعلی است. 831 صورت بالاندهٌ ریشهٌ قاا است و ۴۵۲ به معنی «شکافتن» است.
شکاف < فارسی میانه 5۶ + ایرانی باستان 2-3۶-۵*. برای 2 -> آرای.
شکست < فارسی میانه 5۵91 < ایرانی باستان ۹16۵۶-12*. برای 18 -> آراست. ‎٩1۵0‏
‏صورت اصلی ۶۵8 است. 4 پیش از ۲ به 8 بدل شده است. ۹24 صورت ضعیف ريشةٌ
4 است.برای‌ضعیف کردن ريشه #حذف شده‌است. 5۵74 به‌معنی «شکستن»است.
شکن < فارسی میانه 5۵7 < ایرانی باستان ۶1۸2-۵*. برای 2 -> آرای.
شکفت < فارسی میانه 5/1
شکف جشکوف ج فارسی میانه 501
شکیفت < ایرانی باستان ۴۶1۵1۲1۵. برای 18 - آراست. ‎٩1۸10‏ صورت اصلی ‎٩۳۵۲‏
[pdf page 69]
جوا را فعلهای فارسی دری
است. این ريشه به معنی «صبر کردنْ» است.

--- page tag before 1705 ---
1621:[pdf page 65]
1645:[pdf page 66]
1683:[pdf page 67]
```


## [2026-09-06T16:03:55.807Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; timeout 600 python3 tools/ref_page.py BQT:1261 --image 2>&1 | tail -40"
}
```


### [2026-09-06T16:04:03.471Z] TOOL RESULT

```
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1261.png
REF: BQT:1261  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 52  OCR-lang: fas

بیان هشتم
در شین نقطه‌دار با دال بی نقطه مشتمل برشش لغت
- بنم اول و سکون نانی «بعنی‌رفت قوی قزح را گوبند و آنرا کمان رستم دز
وگذشت ۱ - و بفتح اول وتشدید ثانی»باصطلاح خوانند #۰
شمه وران و مطربان آن است که نفمه را بلند شده بند < بم اول و فتح تانی و بای
کنند و پست کنند تا وقتی که موافق مدعاراست | ابجد و سکون نون و دال بی نقطه ءواقنه نومی
شود - و در عربی بمعنی استوار بستن واسخت | راگویند «
غدن -وسفت گرفتن - وقوی کردانیدن - وبلند | شد‌پار ۶ - با پای حطی, پروزن‌وستی
شدن روز - و حمله بردن باشد. شدکار است که شغم کردن و شکافتن زمین باعد
شدکار ؟ - بنم ارل واکاف بالف | بجهت زرامت کردن ؛وباذال نقطه‌دارهم آمفماست
کشیده بر وزن کلزار » بمعنی شیار است بعنی | بمعنی زمینی که آنرا کار رانده باشند تا تخم
زمین را بجهت زراعت کردن بشکافند و مستعد | بیفشالد .
سازند۴ #وباذال نقطه‌دارهم گفته‌اندیمعنی‌زمینیکه شد بار بدن ‎٩‏ بم اول مصدرشدپار
آبرا شیار کرده باشند و تخم افعانده باشند. باشد که بممنی جفت کاوراندن و زمین را
شد کیس ی - بفتح‌اول بروزن تلییس, شکافتن ومستعد ساختن‌است بجپت زراعت کردن-
۱ ۱ ب ر4: شدن . ۳ شدبار < شیار (ه.م.) .
۴ - نا زنده‌ام مرایست جز مدح تو دگر کار
کمعت ودرودم این است. خرمن همین و شدکار .
رردکی سمرقندی . «لغت فری ۰۱۲۵
۴ -سدکین (هم). ۵ < شدکار د شیار (ه.م.) .
۹ - از: شد‌بار (وم.)+ سن (پوند مصدری) .
* شدن - بنم اول وفتح دال > شودن ( ۸.م.). پهلوی ۰513180 ابرانی باستان -
‎٩ 5102۷ - ۰5892۷ -‏ بارتولمه ۱۷۱۶۸ * « نیب رک ۲۱۸ ۰ پارسی باستان ريشه - 5172۷
(رفتن » راه رفتن)» اوستا ربشهٌ -5122۷ (رفتن)» هندی باستان ريشهٌ -92۷ (رفتن ,ادامهرادن)»
ارمنی 2۱8 (حر کت). 04617۱ (عزیمت کردن). کردی 216 ( رفتن) , 41610 , اقفانی 580۷8
( کردیدن . رفتن) : استی 31. (رفتن . قدم نهادن) ۰ بلوچی 512012 . 513101 و 510106112
ر501182. وخی 24210270. شغنی 202۲2210[ ۰۷۱ سریکلی 206۷52100 ]۷2 «امشق ۴۷۷۸
ختنی«تسوته» (روز کارئو ج» شمارء۳ : کشورختن بقلم بیلی ور4: مقدمهٌ کناب حاضرص خشافرده)»
طبری 58۷82222 ( میروم ) » مازندرانی کنونی 52026 و 5010106 ۶ واژه نامه ۰4۹۱
کیلکی 5000۳ (رفتن) . حر کت کردن -گهتن :گردیدن : َ
آبنه بی شش شد باید بها زآنکه شد حاکی ز جمله ششها .
مثنوی مولوی ی ۵۰۳ س۲۹* منقضی کفتن - اجرا کدتن .
```


## [2026-09-06T16:04:16.002Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"سینما\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt 2>/dev/null | head -20"
}
```


### [2026-09-06T16:04:16.071Z] TOOL RESULT

```
MON_part2.txt:9640:تصاویر سینمایی بکار می‌رود. عرض آن 
MON_part2.txt:9668:نمایش سینمایی. 
MON_part2.txt:9671:فیلم‌بر دارنده] (ص‌فا.) کسی که فیلم سینمایی 
MON_part2.txt:26837:(بلیط های تأتر» سینما؛ راه آهن و غیره). 
MON_part2.txt:68800:مجلات و سینما بکار می‌رود. بهم پیوستن 
MON_part2.txt:68821:انفرادی یک تن بدون مخاطب در سینما و 
MON_part2.txt:87971:می‌گر دد. پرده آن مانند پردهٌ سینما اسکوپ 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:9640:تصاویر سینمایی بکار می‌رود. عرض آن 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:9668:نمایش سینمایی. 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:9671:فیلم‌بر دارنده] (ص‌فا.) کسی که فیلم سینمایی 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:26837:(بلیط های تأتر» سینما؛ راه آهن و غیره). 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:68800:مجلات و سینما بکار می‌رود. بهم پیوستن 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:68821:انفرادی یک تن بدون مخاطب در سینما و 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:87971:می‌گر دد. پرده آن مانند پردهٌ سینما اسکوپ 
MON_part1.txt:2642:سینماء نقاشی و مانند آن ماهر باشد» هنرمند. 
MON_part1.txt:2643:کسی که در صحنة تأتر» سینما و تلویزیون 
MON_part1.txt:20929:فوقانی تماشاخانه با سینما که قسمتی از سالن 
MON_part1.txt:27309:سینمار بی‌نماز. 27-]9 (ص‌مر.) 
MON_part1.txt:62256:فن تزیین صحنة نمایش یا سینما؛ عمل تزیین. 
MON_part1.txt:74856:نمایش سینما یا تاتر در یکك روز: ستانس
```


## [2026-09-06T16:04:23.560Z] TOOL CALL #38: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-06T16:04:23.566Z] TOOL RESULT

```


```


## [2026-09-06T16:04:27.170Z] TOOL CALL #39: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B4%D8%AF%D9%86",
 "prompt": "Persian شدن (šodan): give the full etymology section — Middle Persian form, Proto-Iranian, Proto-Indo-European reconstruction, cognates, and the meanings listed."
}
```


## [2026-09-06T16:04:28.297Z] TOOL CALL #40: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/cinema",
 "prompt": "Give the full etymonline entry for cinema, including cinematograph, French cinéma, Greek kinema/kinein, and dates."
}
```


### [2026-09-06T16:04:34.181Z] TOOL RESULT

```
# Etymology of Persian شدن (šodan)

**Middle Persian Form:**
The word derives from Middle Persian "šudan" (/⁠šudan⁠/), which came from Old Persian "š(i)yav-" meaning "to set, go forth."

**Proto-Language Reconstruction:**
It traces back to Proto-Indo-Iranian "*čyáwatay" and ultimately to Proto-Indo-European "*kyew-" meaning "to move, go."

**Cognates:**
Related words appear across Indo-European languages, including Northern Kurdish "çûn" (to go), Ossetian "цӕуын" (cæwyn), Pashto "شول" (šwəl), Sanskrit "च्यवते" (cyávate, move to and fro), Old Armenian "չու" (čʻu), and Ancient Greek "σεύω" (seúō, put in quick motion).

**Additional Notes:**
Several Old Armenian terms—"արշաւեմ" (aršawem), "ապաշաւ" (apašaw)—were borrowed from Iranian sources, demonstrating the word's influence on neighboring languages.
```


### [2026-09-06T16:04:35.637Z] TOOL RESULT

```
# Etymology of Cinema

**Cinema (noun)** entered English in 1899, meaning "movie hall." It derives from the French *cinéma*, which was shortened from *cinématographe*—a device created by the Lumiere brothers in the 1890s.

The French compound combines a Latinized form of Greek *kinēmat-* (from *kinēma* meaning "movement") with the suffix *-graphy*. The Greek root *kinein* means "to move," tracing back to the PIE root *\*keie-* ("to set in motion").

**Earlier terminology:** The fuller English form *cinematograph* appeared in 1896, predating the abbreviated "cinema," but the shorter version ultimately prevailed. Competing terms included Edison's *vitascope* (1895) and *animatograph* (1898).

**Semantic expansion:** By 1914, "cinema" broadened to encompass "movies collectively, especially as an art form."

**Related phrases:** *Cinéma vérité* (a documentary film style) was established by 1963 from French origins.

The word efficiently compressed technological innovation into linguistic currency, replacing more cumbersome predecessors within decades.
```


## [2026-09-06T16:04:39.651Z] TOOL CALL #41: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/kinetic",
 "prompt": "Full entry for kinetic: Greek kinetikos, kinein, date of entry into English, PIE root."
}
```


## [2026-09-06T16:04:39.872Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/cite",
 "prompt": "Full entry for cite / citation / excite / solicit: Latin citare, ciere, frequentative, and the PIE root given."
}
```


### [2026-09-06T16:04:43.604Z] TOOL RESULT

```
# Etymology of Kinetic

The word **kinetic** entered English in 1841, derived from Greek *kinetikos* meaning "moving, putting in motion." 

The Greek root traces back to *kinein*, which means "to move," ultimately stemming from the Proto-Indo-European root *keie-, meaning "to set in motion."

Initially, kinetic described anything "relating to muscular motion." By 1855, its meaning expanded to encompass things that "cause motion." The term relates to related words like *kinetical* and *kinetically*.
```


### [2026-09-06T16:04:47.509Z] TOOL RESULT

```
# Etymology of "Cite"

The word **cite** originates in the mid-15th century as a verb meaning "to summon, call upon officially." It derives from Old French *citer* and Latin *citare*, meaning "to summon, urge, call; put in sudden motion."

## Key Origin Points

**Latin Root:** The term comes from Latin *citare*, described as a "frequentative of *ciere* 'to move, set in motion, stir, rouse, call, invite.'" This traces back to the Proto-Indo-European root *keie-, meaning "to set in motion, to move to and fro."

**Semantic Evolution:** The original sense of summoning shifted over time. The meaning "call forth a passage of writing, quote the words of another" first appeared in the 1530s, establishing cite's modern academic usage.

## Related Terms

The same Latin root spawned related words like:
- **Citation** (c. 1300) - originally "summons"; later "passage cited"
- **Incite** (mid-15c.) - combining Latin *in-* with *citare*
- **Recite** (early 15c.) - combining Latin *re-* (back, again) with *citare*
```


## [2026-09-06T16:04:56.148Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%B3%DB%8C%D9%86%D9%85%D8%A7/",
 "prompt": "Show the فرهنگ معین (Mo'in) entry for سینما, including any bracketed origin tag such as [فر.] and the definition text."
}
```


## [2026-09-06T16:04:57.086Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B3%DB%8C%D9%86%D9%85%D8%A7",
 "prompt": "Persian سینما: etymology (borrowed from which language?), pronunciation, meaning."
}
```


### [2026-09-06T16:05:02.098Z] TOOL RESULT

```
# Persian سینما Analysis

**Etymology:** The word is "From [French](https://en.wikipedia.org/wiki/French_language "w:French language") _[cinéma](/wiki/cin%C3%A9ma#French "cinéma")_."

**Pronunciation:** The term has three regional variants:
- Dari (formal): [siː.nä.mɑ́ː]
- Iranian (formal): [siː.ne.mɒ́ː] or [siː.næ.mɒ́ː]
- Tajik (formal): [si.nä.mɔ́] or [sinemɔ́]

**Meaning:** The word denotes "cinema" in Persian.
```


### [2026-09-06T16:05:02.758Z] TOOL RESULT

```
# فرهنگ معین Entry for سینما

According to the Mo'in dictionary section, the entry reads:

**(نِ ) \[ فر. \] (اِ. ) ۱ - ملخص سینماتو - گراف و آن نمایش مناظر و اشیاء و اشخاص به روی پردة نمایش به وسیلة دستگاه مخصوص است . ۲ - محل نمایش فیلم**

The origin tag is **[فر.]** (indicating French origin), and the entry provides two primary definitions:

1. A condensed form of "cinematograph" involving the display of scenes, objects, and people on a screen using specialized equipment
2. The venue or location where films are shown
```


## [2026-09-06T16:05:12.602Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%E1%B8%B1yew-",
 "prompt": "Proto-Indo-European *ḱyew-: meaning, descendants (Indo-Iranian, Greek, Armenian), and whether it is related to or distinct from *keyh₁-."
}
```


## [2026-09-06T16:05:14.045Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CE%BA%CE%B9%CE%BD%CE%AD%CF%89",
 "prompt": "Ancient Greek κινέω: etymology, PIE root reconstruction, derivatives such as κίνημα, κινητικός."
}
```


### [2026-09-06T16:05:14.412Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-06T16:05:20.865Z] TOOL RESULT

```
# κινέω (kinéō) - Ancient Greek Verb

## Etymology
The verb κινέω derives from Proto-Indo-European *keyh₂-, meaning "to start to move." Related forms include κίω (to go) and Latin cieō (to move).

## Core Meanings
This verb encompasses multiple senses:
- Physical motion: "to set in motion," "to move," "to remove"
- Linguistic use: "to inflect" (grammatical term)
- Social action: "to meddle," "to change," "to innovate"
- Emotional effect: "to arouse," "to anger," "to exasperate," "to taunt"

## Grammatical Features
Κινέω conjugates as a regular Ancient Greek -εω verb with both active and middle/passive voices. The conjugation tables show uncontracted and contracted forms across multiple tenses including present, imperfect, future, aorist, perfect, and pluperfect.

## Descendants & Compounds
Modern Greek κινώ (kinó) continues this verb. Numerous compounds exist using κινέω as a base, including διακινέω, ἐγκινέω, and προσκινέω, demonstrating its productivity in Ancient Greek word formation.
```


## [2026-09-06T16:05:26.412Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/kyew-",
 "prompt": "PIE *kyew-: meaning, root form, descendants (Indo-Iranian, Greek σεύω, Armenian), any note on relation to *keyh₂-/*keih₁-."
}
```


### [2026-09-06T16:05:28.359Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-06T16:05:31.979Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CF%83%CE%B5%CF%8D%CF%89",
 "prompt": "Ancient Greek σεύω: etymology, PIE reconstruction, cognates in Sanskrit and Avestan."
}
```


## [2026-09-06T16:05:32.970Z] TOOL CALL #49: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/cieo",
 "prompt": "Latin cieō: etymology, PIE root, related citō/citāre, and any cognates named (Greek κίω, κινέω)."
}
```


### [2026-09-06T16:05:37.685Z] TOOL RESULT

```
# σεύω (Ancient Greek Verb)

**Meanings:** The verb means to chase, drive, or impel (active voice), or to rush, hasten, or hurry (middle voice).

**Etymology:** The word's origin is disputed among scholars. According to Beekes, it derives from Proto-Indo-European *kyew-, making it cognate with Sanskrit च्यु (cyu). However, Beekes acknowledges that the expected phonetic outcome doesn't perfectly match the actual Greek form, suggesting possible analogical reshaping.

Alternative theories propose connections to related Greek verbs κινέω and κίω, or derivation from an original athematic present form *kyéw-to with later restoration of the -ευ- element.

**Key scholarly sources include Beekes' Etymological Dictionary of Greek, the Lexikon der indogermanischen Verben (LIV), and works by Frisk and Chantraine examining Greek etymologies.
```


### [2026-09-06T16:05:39.387Z] TOOL RESULT

```
# Latin Verb *cieo*

**Etymology & PIE Root:**
The term derives from Proto-Italic *kieō* ("to stir"), tracing back to Proto-Indo-European *keyh₂- ("to move"). This connects to cognates including Ancient Greek κίω (kíō, "to go") and κῑνέω (kīnéō, "to move, set in motion"), plus Albanian qoj ("to wake up").

**Core Meanings:**
The verb encompasses several related senses: "to set in motion," "to move/stir/shake," "to summon or call," and notably "to rouse, stimulate, excite; disturb; produce; cause; begin; provoke."

**Related Terms:**
Derivatives include citō (swiftly), citāre (to cite/summon repeatedly), and citus (quick/rapid). Compound forms like excitō, incitō, and concitō extend the root's semantic range. The entry notes that "citō" carries the sense of rapid motion derived from this etymological line.
```


## [2026-09-06T16:05:47.700Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== KLN cinema ===\"; grep -n -i -E \"^cinema|cinematograph|kinema\" KLN_1966.txt KLN_1971.txt | head -10; echo \"=== KLN kinetic ===\"; grep -n -i -E \"^kinetic|kinetikos|kinesis\" KLN_1966.txt KLN_1971.txt | head -10; echo \"=== KLN cite ===\"; grep -n -i -E \"^cite,|^citation|ciere\" KLN_1966.txt KLN_1971.txt | head -10"
}
```


### [2026-09-06T16:05:47.827Z] TOOL RESULT

```
=== KLN cinema ===
KLN_1971.txt:29919:biograph, n., a cinematograph. — Lit. ‘living des- 
KLN_1971.txt:47211:cinema, n., a motion picture. — Short for cine- 
KLN_1971.txt:47214:cinematograph, kinematograph. — Coined by the 
KLN_1971.txt:47217:‘to write’ See kinematic and -graph. 
KLN_1971.txt:47218:Derivatives: cinematograph, tr. and intr. v. and 
KLN_1971.txt:47219:adj. , cinematograph-ic, cinematograph-ic-al, adjs., 
KLN_1971.txt:47220:cinematograph-ic-al-ly, adv., cine mat ograph-y,n. 
KLN_1971.txt:47224:(see kinematic), on analogy of panorama; see 
KLN_1971.txt:131393:kinema, n. — See cinema. 
KLN_1971.txt:131395:kinematic, also kinematical, adj., pertaining to 
=== KLN kinetic ===
KLN_1971.txt:6179:adj. of xtveiv, ‘to move’. See kinesis, 
KLN_1971.txt:70164:diadochokinesia, diadochokinesis, n., the normal 
KLN_1971.txt:70171:See prec. word and kinesis, 
KLN_1971.txt:118166:hyperkinesia, hyperkinesis, n., abnormally exces- 
KLN_1971.txt:118169:xlvelv, ‘to move’. See kinesis, 
KLN_1971.txt:131404:kinetic and cp. words there referred to. 
KLN_1971.txt:131406:kinesis, n., physical movement. — Gk. xbnrjms, 
KLN_1971.txt:131408:and cp. akinesia, diadochokinesis, hyperkinesia, 
KLN_1971.txt:131409:telekinesis. 
KLN_1971.txt:131417:kinetic, adj., 1) pertaining to motion; 2) having 
=== KLN cite ===
KLN_1971.txt:47804:citation, n., 1) summons; 2) quotation. — ME., 
KLN_1971.txt:47811:cite, tr. v., 1) to summon; 2) to quote. — F. citer, 
KLN_1971.txt:47813:provoke, call urgently’, freq. of ciere (pp. cit us), 
KLN_1971.txt:85880:isus, pp. of eciere, ‘to eat*. See eat For the de- 
KLN_1971.txt:87578:excite, provoke, call urgently’, freq. of ciere 
KLN_1971.txt:121743:ciere (pp. cites), ‘to set in motion’. See cite and 
KLN_1971.txt:131422:and cogn. with L. ciere, ‘to put in motion’, 
KLN_1971.txt:169465:‘to move’, freq. of ciere. See oral and cite. For 
KLN_1971.txt:226005:‘whole, entire’, and citus, pp..of ciere , ‘to put in 
KLN_1966.txt:7784:citation,  n.,  1)  summons;  2)  quotation.  —  ME., fr.  L.  citationem,  acc.  of  citdtio,  fr.  citatus,  pp. of  citare.  See  cite  and  -ation. citatory,  adj.  —  L.  citatorius,  fr.  citatus,  pp.  of citare.  See  next  word  and  the  adj.  suffixes  -ate and  -ory.
```


## [2026-09-06T16:05:51.156Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '47211,47226p;131417,131426p;47804,47820p' KLN_1971.txt; echo \"=== solicit ===\"; grep -n -A4 \"^solicit,\" KLN_1971.txt | head -12"
}
```


### [2026-09-06T16:05:51.254Z] TOOL RESULT

```
cinema, n., a motion picture. — Short for cine- 
matograph. 

cinematograph, kinematograph. — Coined by the 
brothers Lumtere in 1896 fr. Gk. xbnr^a, gen. 
xtv7)p.aT0(;, ‘motion’, and -ypa<po<;, fr. ypa<peiv, 
‘to write’ See kinematic and -graph. 
Derivatives: cinematograph, tr. and intr. v. and 
adj. , cinematograph-ic, cinematograph-ic-al, adjs., 
cinematograph-ic-al-ly, adv., cine mat ograph-y,n. 
cinerama, n., a modern motion-picture system 
employing a wide screen to simulate panoramic 
vision. — Formed fr. Gk. xtveiv, ‘to move’ 
(see kinematic), on analogy of panorama; see 
-rama. The word cinerama is incorrectly formed. 
The correct form would be cinorama. 
citation, n., 1) summons; 2) quotation. — ME., 
fr. L. citationem, acc. of citdtio, fr. citatus , pp. 
of citare. See cite and -ation. 
citatory, adj. — L. citdtorius, fr. citatus, pp. of 
citare. See next word and the adj. suffixes -ate 
and -ory. 

cite, tr. v., 1) to summon; 2) to quote. — F. citer, 
fr. L. citare , ‘to put into quick motion, excite, 
provoke, call urgently’, freq. of ciere (pp. cit us), 
‘to set in motion’, fr. base *qi-, whence also Gk. 
xUiv, ‘to go’. This base is rel. to base *qi-, 
whence Gk. xivetv, ‘to move’, and to base 
*qieu-, whence OI. cydvate, ‘moves, goes away’, 
Gk. oeuetv, ‘to hunt, chase, drive away’. Cp. 
excite, incite, kinetic, oscitancy, recite, solicit, 
suscitate. Cp, also hight and words there refer- 
kinetic, adj., 1) pertaining to motion; 2) having 
moving force. — Gk. xtv/)Tix6<;, ‘putting in 
motion’, fr. ‘moved’, verbal adj. of 

xTveiv, ‘to move’, which is rel. to xietv, ‘to go’, 
and cogn. with L. ciere, ‘to put in motion’, 
citare , ‘to put into quick motion’. See cite and 
cp. cinema, cinerama, kinematics, kino-, Acineta. 
Derivatives: kinetic-al, adj., kinetic-al-ly, adv. 
kinetics, n., that branch of science which deals 
=== solicit ===
226000:solicit, tr. v., to entreat; intr. y., to make solicita- 
226001-tion. — ME. solid ten, fr. MF. (= F.) solliciter , 
226002-fr. L. sollicitdre , ‘to stir, agitate, move, excite, 
226003-urge’, fr. sollicitus, ‘violently moved’, lit. ‘wholly 
226004-moved’, solli-citus being a compound of sollus , 
--
266315:solicit, court, woo’, Du. werven, ‘to enlist’, 
266316-Goth, hairban , ‘to wander’. All these words 
266317-derive fr. I.-E. base *k w erp-, ‘to turn, re- 
266318-volve’, whence also Gk. xap7t6<;, ‘wrist’, and 
266319-prob. also Toch. A karp -, ‘to turn to, to go’, OI.
```


## [2026-09-06T16:06:03.895Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== LAT cieo ===\"; grep -n -i -E \"^cieo|cieo,|cieō\" LAT.txt | head -5; echo \"=== LEW cieo ===\"; grep -n -i -E \"cieo|ciere\" LEW_1910.txt | head -8; echo \"=== SKT cite ===\"; grep -n -i -E \"^cite|^citation|ciere\" SKT.txt | head -8; echo \"=== HUB sudan ===\"; grep -n -i -E \"sudan|siyav|syav|cyav\" HUB.txt | head -12"
}
```


### [2026-09-06T16:06:03.992Z] TOOL RESULT

```
=== LAT cieo ===
11567:cieo. Ce qui se combine le mieux ayec le causatif ceueo, c 1 est le
11711:cieo
11736:cieo, -5s, citum, clere; cio, cis, clui, citum (dans accitum),
11738:evitees quand une voyelle suit l'e dn thfeme: on ne rencontre pas cieo,
11749:Composes: accieo,-es (accio, -is) : faire venir, appeler, cf .arcesso-,
=== LEW cieo ===
=== SKT cite ===
=== HUB sudan ===
143:neben ap. sit/dti-, np. savam neben ap. asiyavam. Laut-
2742:*syavaka') ein phi. *siyav (= zd. syava-) vorkam, was
4198:lich'; hctz *ziiruck, ofFen' = paz. aicaz, skr. apad-; haxsudan
4748:afzayam, Diesen Mustern ist auch dsUdan (oben p. 7) ruhen,
4760:p. 36) ; baxsudan : baxsdyam 'gnadig sein, verzeihen . Von
4875:sUdan gnadig sein, verzeihen', paz. atvaxiaisni 'forgiving*--^
5332:zyana- ; siydh *schwarz' = zd. sycLva-, dazu Siyavas = zd.
5333:syavarsan-; mayazd (besser miyazd) *6elage' (parsisch) =
5337:sad *frohlich' = phi. sat, ap. siyati- 'Behagen, Freude'; sudan,
5338:pr. savam gehen, werden*, ap. ipf. asiyavam. In beiden
5947:syava-) ;
6235:zuriick, offen', skr. apdc-; baxsudan 'gnadig sein', phi. apux-
```


## [2026-09-06T16:06:06.739Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '5330,5342p;138,148p' HUB.txt; echo \"=== LAT cieo entry ===\"; sed -n '11736,11760p' LAT.txt"
}
```


### [2026-09-06T16:06:06.803Z] TOOL RESULT

```
VOK
m HtBSCHMANN.
STRASSBURG.
VERLAG VON KARL J. TRttBNIlR.
1895.- 8 —
neben ap. sit/dti-, np. savam neben ap. asiyavam. Laut-
lich wiirde OSiyana ein ap. ^asidana- oder ^Osadana^
(vgl. np. piyada = skr. padati-) voraussetzen, das viel-
leicht zur Wurzel sad *sitzen' gestellt werden konnte.^)
Vgl. np. nisastan *sitzen' und nis^m *Nest'. v. Stackel-
berg denkt an osset. axston (aus dxs-don oder dxst-don)
821; saya *Schatten H. 695; xaya *Er H. 468;' miyan 'Mitte
= zd. maidyqna- (doch s. § 41); ziyan *Schaden = zd.
zyana- ; siydh *schwarz' = zd. sycLva-, dazu Siyavas = zd.
syavarsan-; mayazd (besser miyazd) *6elage' (parsisch) =
zd. myazda^; niyCt *Grossvater' = ap. zd. nyaka-; razm-yOz
'kampfsuchend', arm. yoiz.
§ 41. Ap. y schwand nach s schon im Pehlevi: np.
sad *frohlich' = phi. sat, ap. siyati- 'Behagen, Freude'; sudan,
pr. savam gehen, werden*, ap. ipf. asiyavam. In beiden
Fallen ist np. s = ap. siy = arisch dy. Vgl. § 132. Aus
anlaut. dy- und jfy ist / geworden : np. ja^t Xeben, Seele* ^)
= skr. dhyana- *Nachsinnen'? (s. oben p. 49) ; javTdan *kauen',
ksl. zwati, Wzl. arisch jyu (§ 120).
=== LAT cieo entry ===
cieo, -5s, citum, clere; cio, cis, clui, citum (dans accitum),
cire (pour la double forme, cf. tuor et tueor-, les formes de cieo sont
evitees quand une voyelle suit l'e dn thfeme: on ne rencontre pas cieo,
cieam): mettre en mouvement; par suite: i° faire venir k soi, appeler,
invoquer; ciere, nominare P.F.58,11; t.de droit, T.L.10,8,10, qui
patrem ciere possent "citer en justice"; 3 ° exciter, provoquer, erctum
ciere "provoquer k un partage de biens", cf. ercisco, expression qui
n'etant plus comprise adonne lieuala fausse interpr^tation de Servius,
B.8,643, "ercto non cito" i.e. patrimonio uel hereditate non diuisa-,
nam citus diuisus significat ; "pousser" ( gemitus, uoces, fletus). Se
dit generalement de tout ce qui entre en mouvement et en action, par
rapport k ce qui est immobile et au repos. Ni citus,-us, ni citio, ni
citor n'existent (mais imbricitor).
Composes: accieo,-es (accio, -is) : faire venir, appeler, cf .arcesso-,
accitus,-us: appel; accita, M.L.76.
concieo: i° faire venir ensemble, rassembler; 3° agir violemment (ou
tout d'un coup), exciter, soulever, provoquer; concitus: pouss£ ensemble
ou avec force, concitor: excitateur. (Ne semble plus atteste aprbs
Tac.; double et supplee par concito).
excieo (-cio) : faire sortir, appeler hors de, exciter; cf. P.F.70,7,
exciet, excutiet (anteclassique, et quelquefois a 1'^poque imperiale
sans doute par affection d'archaisme); excitus: agite.
percieo (-cio) rare et arch.: mettre en mouvement, ^branler, agiter
fortement; percitus: pousse avec force.
prScieo: cf. P.F.351,33 procitant: prouocitant. Citare enim ut uoci-
```


## [2026-09-06T16:06:12.951Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '11760,11800p' LAT.txt"
}
```


### [2026-09-06T16:06:13.010Z] TOOL RESULT

```
prScieo: cf. P.F.351,33 procitant: prouocitant. Citare enim ut uoci-
tare, unde procet (l.procit) et prociet.
Cio, cieo et leurs composes, rares k 1 '^poque r 4 publicaine, et
presque uniquement po^tiques (Cic. evite le mot dans ses discours,cieo
3x4
et n'en a que de rares ex. dans ses traites), sont trait6s comme des
archaismes et disparaissent asaez vite de la latinit 4 imperiale. Dbs
le second sibcle, iis ne sont plus que rarement attest6s, et dans des
emplois techniques. De bonne heure, iis ont tendu 1 etre remplaces
par le frequentatif-intensif:
cito,-as et ses composes (voir le tableau comparatif des emplois
de cieo/cito, Thes. III ii99,65sqq.). A 1 'epoque r6publicaine, usite
dans la langue juridique et politique au sens de "convoquer (le S 4 nat),
citer (en justice)"; d'oii "invoquer le temoignage de", et de 11 "citer,
mentionner". C'est surtout 1 1 'epoque imperiale que le verbe a le sens
etymologique de "mettre en mouvement, exciter, provoquer", et dans
la langue rustique "produire, pousser" (Colum.Pali.). Citatus est trait6
tantot comme participe, e.g. Enn., A.461, rex deinde citatus conuellit
sese-, Sen., Med.853, uultus citatus ira riget ; tantot comme adj ., avec
comparatif et superlatif, avec le sens de "rapide, vif": T.L.37,50,1,
citatiore quan inde uenerat agnine. De la: citdtio (b. lat. jurid. et
milit.): proclamat ion; commandement.
concito: mouvoir, ou exciter violemment ou rapidement (aspect de-
termine); excito: faire sortir, appeler hors de; exciter, provoquer.
Dans la 1 . de 1 'architecture "elever" (faire sortir de terre): - turris,
tunulun. S'emploie au sens physique comme au sens moral. M.L.3970 et
et 3515 *deexcito-, incito: lancer en avant, M.L.4356 >4355 a ; percito
exciter violemment (rare et arch.); recito: refaire l'appel des noms
cit6s devant le tribunal, e.g. Cic. Verr.S>xo, da, quaeso, scribae,
recitet ex codice ; puis "lire k baute voix, reciter" M.L.7133; suscito
de *subs-cito: faire lever, Elever, soulever. M.L.8483. Se dit du mala-
de, e.g. Hor.S. I 1,83, medicum roget | ut te suscitet ; et par suite
des morts dans la langue de l'iglise: suscitare nortuos, suscitatus(St-
Aug.); d'ou resuscito "redresser, faire revivre" (deja dans Ovide au
sens moral, comme recreo). Tous ces verbes ont des d 4 riv 6 s en -tor et
en -tio. Le rapport 4 tymologique avec cieS n 1 est plus sensible dans
la plupart.
De cieo le participe est citus "mis en mouvement" , avec son contraire
incitus "immobile, bloque" conservb dans l'expression technique du
jeu de dames ad incitas (scil.caZces cf. Pl., Poe.908, quin prius dispe-
ribit faxo quan una m calcen ciuerit) redigere "r 4 duire k 1 1 immobilite"
```


## [2026-09-06T16:06:15.709Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '11800,11830p' LAT.txt"
}
```


### [2026-09-06T16:06:15.772Z] TOOL RESULT

```
ribit faxo quan una m calcen ciuerit) redigere "r 4 duire k 1 1 immobilite"
(sens propre et figure, cf. Isid.Or.18,67). Citus figure comme participe
dans tous les compos 4 s de cieo (k cot 4 de -citus ,&ans incitus, avec
in- marquant le mouvement), il est second terme de compose dans solli¬
citus "entibrement agite", "profondement troubl6" (v.soZZus), employe
surtout au sens moral, d'ou sollicitudo; sollicito, -as "tourmenter,
donner du souci", et ses d 4 riv 4 s; cf. M.L.8076 (meme image que dans
uexdre). Mais il est, comme altus, le plus souvent considere comme
adjectif au sens de "vif, rapide", et muni d'un comparatif et d'un
superlatif. Cf. 1 1 adverbe cito "vite" et, g 4 n 4 ralement accompagne d'une
negation, "facilement" (comme gr. ttoc^cx), de 14 . citius comparatif 4 qui-
valent a potius. - M.L.1954 (cito, citto, citius). Citus est classique,
mais surtout usit 4 en poesie. L'adverbe est au contraire frequent dans
la prose.
La racine indo-europeenne fournissait sans doute un aoriste ath 4 -
matique dont le grec a une trace indirecte dans 1'aoriste thematique
exi/OV. Les presents, faits secondairement, varient d'une langue k
1 'autre, ainsi grec XLveco; c'est ce qui fait que le latin a cio et
cieo cote a cote. One forme k elargissement - u- joue un grand role:
hom. eocnjTO "il s' est mis en mouvement" et creuu), ou, avec infixe nasal,
xovujjai, (xi/Vew serait-il xlvefto?); arm . cu "depart" et cogay "je suis315
cimex
all£"j skr. cyavate "il ae «et en mouvement", vieux perae asiyavam "je
me ania «ia en marche", etc.
clgnus, -I m.: cigne, meanre valant huit scrupules. Rare et trfea
tardif. Emprunt?
cllibantua, -I et cilliba, -ae f.: table ronde on quadrangulaire,
cf. Varr.L.L.5, i8i et 118. Du gr. xiXXl,( 3 (XC,-avxoc. Mot populaire, qui
aemble appartenir a la langae dea aoldata.
cilicium, -I n.: 4 toffe grossibre en poil de chbvrej cilice. Ainai
nommee parce qu’elle eat originaire de Cilicie. M.L.X9X8.
```


## [2026-09-06T16:06:29.331Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== ARY latin index KEI/KEIE ===\"; grep -n -i -E \"^ *KEI|KEI-|KEIE|KYEU|CIEO|KINEIN\" incoming/ARY/ARY_latin_index_pages.txt | head -20; echo \"=== IEC kei ===\"; grep -n -E \"^kei-|^kēi-|kiē-|kineō|kīneō\" IEC.txt | head -10; echo \"=== SYN go/become kei ===\"; grep -n -E \"cyavate|asiyavam|šiyav|kineo\" SYN.txt | head -10"
}
```


### [2026-09-06T16:06:29.461Z] TOOL RESULT

```
=== ARY latin index KEI/KEIE ===
12062:KEIKTI ALITHUANIAN) gi
=== IEC kei ===
=== SYN go/become kei ===
```


## [2026-09-06T16:06:32.648Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== ARY شدن ===\"; grep -n \"شدن\" incoming/ARY/ARY_pages.txt | head -15; echo; echo \"=== IEC kinew/kiu ===\"; grep -n -i -E \"kiu-|kieu-|kineo|cyavate\" IEC.txt | head -12"
}
```


### [2026-09-06T16:06:32.733Z] TOOL RESULT

```
=== ARY شدن ===
89:برتری نژادی آنها کم شد. هر چه اين کوچگران از آلمان دورتر شدند؛ میزان آمیختگی خون آنها با
133:آلمان به خارج مهاجرت کردند ولی هر چه از آلمان دورتر شدند آمیزش آنان با اقوام محلی موجب
134:پست شدن نژادی و تیرگی نسبی رگ مو و چشم آنها شد. موضوع پرتری‌های نژادی (که امروزه
182:شدند. مردمان این نواحی (مثلا ساکنان آذربایجان و ترکیه) همه به زبانهای هند و اروپایی تکلم
270:اثر قطع تماس باگهواره» این واژگان و ویدگی‌های زبانی عتبق به اصطلاح منجمد شدند. ممکن است
355:«ارمنی‌ها» و «یوتانی‌ها»)پرانداخته شدند.
373:تبدیل به کشو رگشایان کوچگر شدند!
382:به زبانهای متفارت کرد به طوری که آنان دیگر حرف‌های همدیگر را درک نمی‌کردند و مجبور شدند
391:محسوب می‌شدند) به وجود آمدند. به همین دلیل این زبانها «پست» هستند و مرتباً دگرگون
399:شماری از دانشمندان اروپایی متوجه شباهت‌هایی میان برخی از زبان‌ها شدند. آنچه که ک‌کم واضح
404:بلغارستانی و غیره است. بدین روش | کثر زبانهای اروپایی دسته‌بندی شدند. ضمناً بررسی نوشتارهای
413:اروپایی ردیابی و دفته‌بندی شدند.
528:(1۸۸۸ ,87180 ,7۸7۳387[3) هر یک در اقلیمی سا کن شدند و نسل و زبان جدا گانه‌ای را به وجود
646:وسیعی از بین‌النهرین تا شمال شبه قاره‌ی هند ماندگار شدند. سپس کوچگران ایرانی آمدند و فلات
655:(5۸۸/۸71۸07) نه تنها در کرانه‌های رود دانوب کوج نشین شدند پلکه در قرن دوم میلادی برای

=== IEC kinew/kiu ===
7235:kiuis, os, io "small animal, chick'. (In part onomat. Cf. Kiu-) , Oss. ciw, Dig. cew “a small bird’; cf. ciw-ciw kånin ‘to chirp’; (Gk. kis, gs kiós ‘worm, wee- vi, a potential isophone, but not onomat. as Oss. W & Li.); W cyw, pl. ion, m. ‘young animal, chick’; Li. kivē, f. ‘peewit (beside kivynas ‘kind of worm’; pl. “infusoria'); ki- výna ‘tadpole’
8810:Kiu-, (Kiué-, Kiuiko-) fsquealer'. Onomat. Skt. cf. $ivaluh “jackaP; Gk. sús ‘pig’; Alb. thi, gs thiu, id.; Slovene sevka ‘lark’; Li. šivi! (call to a bird); Latv. sivēns 'piglet'; W cyw, pl. -ion, m. ‘chick’
15509:skáuios “bent, twisted, left-hand’, etc. See skaiuos. The present variant arises in Alb. i huej, i huaj, adj. ‘strange, foreign’; t&-huej, v. ('alienate', fr. *at-skaujo); EMDu. schou- wen, v. ('avoid'. NB. Du. schuwen, id. is fr. a type *skeukio: skük- in view of OHG skiu- hen, G scheuen, etc. LWs in OFr. eschiver, It. schivare, E eschew, etc.); schouw, adj. *depraved, wayward'
```


## [2026-09-06T16:06:37.982Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -E \"^K(ei|ēi|ei̯|iē)\" IEC.txt | head -20; echo \"---\"; grep -n \"to set in motion\" IEC.txt | head -10"
}
```


### [2026-09-06T16:06:38.059Z] TOOL RESULT

```
7187:Keis, kiglis 'siskin; finch; tit" or sim. Arm. cf. čzam, Gem (‘squeaľ’, fr. *kigio); OE hice ‘tit’; hicol ‘woodpecker’; OCS, R zi, Ciz *siskin'; Blg. Cigla *missel-thrush'; Slovene cf. Cigva *sandmartin'
8619:Kei- (Keii, Kī-) (1) ‘He; fal’. WP I, 358 Skt. sáye “lie? beside Stee ‘fall out, perish’; Av. sāi-, sae- ‘lie’; Oss. säjun, säin “Tie ill’; Hitt. cf. kitta, kittari, 3s ‘lies’; Myc. (queried) ke- ‘lie’; Gk. keïmai,id.; Lat cpd.(?) ja-ceo, -cere (lit. ‘go and be": Ir. cf. foi-chim (“co- habit with’, fr. upo-^); W (ambig.) cwydd ‘fall’; Br. kuéz, pl. kuésiu, m. “fall'; kuéza, denom. id.; Cor. codha “fall; happen?
8620:Kei (Kei, Kein-) (2) “here, there; hither,
8622:Keis (cpd. of Ke ‘behold’ and is *this"); Kis ‘this, he’. WP I, 453 Gk. cf. keinos, ekeinos ‘he’; Lat. cis, cis- ‘this’; Olr., Ir. cé, indecl. (this, in bith cé “this world"); OS he, hi, Du. hij, LG he, OE he ‘he’; OCS sí; Li. Sis, id.
8623:Keiuos, à (1) “beloved; spouse’. Cf. Kru- Arm. Ser, gs siro, ab. sirov ‘love’; Skt. sevah, a, adj. ‘beloved’; OHG hiwa ‘wife’; Du. cf. huwen, v. ‘marry’; Latv. sieva ‘woman’
8624:Keiuos (2) (?) ‘fibre, pondweed, tangle’ Skt. cf. $evalam *pondweed' beside $aivahb, id.; Ir. ciabh, pl. céabhanna, f. “lock, hair’; ciabhar, m. coll. “hair?
8628:Keita (Keit-) ‘rest, lair, abode, room’. Cf.
8629:Kei-, Ki-, etc. Skt. Sáyita ‘rest, abode’; Go. hépyo ‘room’. Long-grade radical also in Skt. śāyah, adj. “sleeping, resting’; short-gde in śayah, id. and m. ‘sleep, rest, sofa". Cf. WP I, 358 & 376
8636:Keiota (Keit-) — Kensos, à, us
---
```


## [2026-09-06T16:06:46.419Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i -E \"kineo|kinéo|kīneo|ki-neu|kinumai\" IEC.txt | head; echo \"=== Kiu- entries ===\"; grep -n -E \"^Kiu\" IEC.txt | head; echo \"=== WLD Bd1 kei set in motion (p.361) ===\"; grep -n -E \"in Bewegung setzen\" incoming/WLD/WLD_Bd1_pages.txt | head -10"
}
```


### [2026-09-06T16:06:46.511Z] TOOL RESULT

```
7209:kin- ‘start, move, do, perform’. WP I, 362 & 510 and cf. Supt: K Skt. &inomi ‘put, arrange, pile, build’; Hitt. kina(mi) (queried: 'stir, move, begin"); Gk. kinéo, id.; Lat. -cinor, -cinari (do act in cpds. ratio-^, latro-^, patro-?^, leno-?. Cf. -ci- nium, s. form); OCS po-Cíng, inf. -Ceti ‘begin’; R po-éat, inf. “begin; tap a cask’; OCz. ve-, za-Cnu, -Cieti ‘begin’ beside OCS (and com. Sl.) Cinü ‘act’; cf. also Gk. apó-kinos “escape; a comic dance’; Latv. cina ‘struggle, fight
=== Kiu- entries ===
8810:Kiu-, (Kiué-, Kiuiko-) fsquealer'. Onomat. Skt. cf. $ivaluh “jackaP; Gk. sús ‘pig’; Alb. thi, gs thiu, id.; Slovene sevka ‘lark’; Li. šivi! (call to a bird); Latv. sivēns 'piglet'; W cyw, pl. -ion, m. ‘chick’
8813:Kiuos (2) 'sharp, astute, clever'. (Same as (1)?)
8815:Kiuos, ðn, is (Keiu-?) (3) ‘person’. Initial ambig. in Lat. and Gmc. Cf. WP I, 359 OLat. ceiuis, Lat. civis, gs -is, m. f. “citizen, freeman, -woman'; Osc. ceus, id.; Go. heiwa- (cpds. *house-, family-); OE hiwan, mpl, hiwen, npl. *household'; G cf. Hei-rat *mar- riage’; Du. huw- (cpds. "mariage" OS cf. hiwian, v. ‘mate’; Du. huwen, v. ‘marry’; Sw. hjon, n. ‘person’; hjon-lag ‘marriage’. (W ciwed ‘rabble’ appears to be a LW, cf. Lat. civitas ?). Here prob. also Latv. siéva ‘woman’
8816:Kiuos (Kieuos) (4) dark grey’. WP I, 361 Skt. $yaváh, id.; Av. syavo ‘black’; Per. siyah,
=== WLD Bd1 kei set in motion (p.361) ===
3281:    „schwingen, in Bewegung setzen, ffihren".
7015:Persson Wzerw. 26; s. vielmehr er- „in Bewegung setzen“) rnd- „schuldig“,
13066:      Alte Beziehung von ere- „rudern“ mit cr- „in Bewegung setzen" ist denk-
13440:84F; s. er- ..in Bewegung setzen, woraus erd- wohl erweitert ist.
27251:diesem Ausgang.   s. u. qei- ,.in Bewegung setzen”: s. nocli Boisacq lOSG
27316:(liber ogodauvos ds     s. u. er- ..in Bewegung setzen".liber gadivog, g ada-                                                              ;
33817:qei- (?? s. u.) „in Bewegung setzen, in Bewegung sein“ (: qdi-:ql-); eu-
33844:     Lat. do, cire          und cieo, ciere „in Bewegung setzen, rege machen, wecken“
39932:    Q^raoren ,.in Bewegung setzen. riicken, riiliren -- . as. hr ora .,Bewegung, Auf-
44645:(um etwas herum) tatig sein; trans. in Bewegung setzen, betreiben”, nhd.
```


## [2026-09-06T16:06:50.035Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '33817,33900p' incoming/WLD/WLD_Bd1_pages.txt; echo \"=== page tag ===\"; awk 'NR<=33817 && /\\[pdf page/{p=$0;n=NR} END{print n\": \"p}' incoming/WLD/WLD_Bd1_pages.txt"
}
```


### [2026-09-06T16:06:51.787Z] TOOL RESULT

```
qei- (?? s. u.) „in Bewegung setzen, in Bewegung sein“ (: qdi-:ql-); eu-
    Basis (z. T. mit w-Infix, Ebel KZ. 1, 300, Pedersen IF. 2, 311 Anm. 1)
        qi-(n-)eu- ; set-Basis qia-            (   :
                                                       qic-'l).

      Gr. x'm „gehn, weggehn, (von Schiffen :) fahren“ (nur Praes.) und yJo/icv,
y.loifu,   yucbv (zur Aktionsart s. Delbriick Ygl. Synt. II 100);

      hom. Impf. jUETey.la&e, -Pov „folgte nach, verfolgte                       ;
                                                                                     durchstreifte“, y.iaio     '




ixivslro Hes. (Set-Formen); ovo-y.lvdiog , - yJvdag „Eseltreiber“, y.ivbag, „be-
weglich, svyJvr]Tog“ (vgl. zur Bildung dktvboo, y.vUvbm, Persson Beitr. 156;
nicht nach Bechtel BB. 23, 250 als ke nd- zu ags. hunta „Jager“, hentan
„verfolgen“), wozu wohl auch xlvbvvog „Gefahr“ (vgl. nach Yendryes und
Boisacq 1115 lat. solli-citus auch „geangstigt, in Gefahr“);
     von gl-n-eu -,   xivvfiat „werde bewegt, erschiittert, bewege mich,
                              gr.
gehe“,               „werde bewegt, schwanke zweifelnd bin und her“,
            xlvvooouai
xivew „setze in Bewegung, treibe“ (dies wenigstens sehr wahrscheinlich
fiir *xlvef-io, Saussure Mem. 187   Anm., Solmsen KZ. 32, 541; Brug-
mann II 2 3, 260, 324 liiBt auch *xi-v-eioj als eine Bildung wie ai. dhu-
n-ayati offen).
     Lat. do, cire          und cieo, ciere „in Bewegung setzen, rege machen, wecken“
(ciere   = idg. qi(i)e-V!), citus „(*in Bewegung gesetzt=) schnell“, cito, -are
„in    Bewegung setzen, kommen                                  lassen,        vorladen", solli-citus „ganz,             stark
bewegt, beunrukigt, in Angst und Gefahr“, cunctus (wobl aus *con-citos ,
s. Yf. LEWb.
             2
               s. v.) „gesamt, samtlich“, ac-citus.


     Yon den versuchten kelt. Anreihungen    (Curtius 4 149, Fick II 4 75) ist
air. rochim „erreiche“ vielmehr anfangbetontes ro-saigim (Thurneysen Hdb.
47Sf., Pedersen KG. II 609) und wird corn, he, mbret. que, quae nbret.                                               ,


Jcae „geh!    von Pedersen KG. II 453 als imperativisch verwendete Par-
                 -
                     ‘



tikel „her!“ oder „fort!“ gedeutet.                                    —
                                          Gegen Yerbindung von xtveoo mit
ai. Qindti (unbelegt) oder mit ai. cinoti s. Pedersen IF. 2, 311a 1.                                                     —
     Ganz       fraglich       reiht Charpentier IF. 28, 184 ai. kit-,                                   ketati   „gehn“ und
,,jagen, verfolgen", kheta-              m. n. „Jagd :t u. dgl. an.

     Erw. von der einfachen "Wzf. qei- aus:
  Mit s: ai. cestati „bewegt die Glieder, ist in Bewegung“, cesta- n., celta
,Bewegung, Gebarde“ (vgl. formal ai. restate lat. vieo; Uhlenbeck Ai. Wb.              :




93, Yf. LEWb.
                 2
                   u. cieo Persson Beitr. 328, Trautmann KZ. 46, 240); nicht
                                             ,


iiberzeugend erwiigt Liden Le monde orient. 5, 196 zw.        Zugehor auch
von lit. k'tikis „Hase“ zu dieser s-Ervv.
     Mit d (d-Praesens?)                 :        vielleicht     ir.     cid-    z.   B.   in   cisse „invecta“,     d-an-di-
chdet „deducunt“                (usw.,             Pedersen KG. II 490 f.), sehr wahrscheinlich                               got.
haitan, ahd. hetman, ags. hatan, as. hctan, anord. heita „heiBen (= antreiben,
befehlen, anrufen, nennen“;     Brugmann IF. 6, 94 m. Lit., Hoffmann Jepa?
40 f., Fick III 4 61, Falk-Torp u. hede m. Lit., vgl. zur Bed. gr. xettco
„bewege“ xeloyai „treibe an, fordere auf, rufe beim Namen“; nicht iiber-
                 :



zeugend vergleicht Zupitza Gutt. 105 haitan als „benennen     unterscheiden“                              =
mit lit. skiesti „scheiden“, aksl. cediti „seihen“).
  Mit ?(o) -Formans Auf einem kl-lo-s ke x i-Io-s „bewegt, wippend" kann
                                    :
                                                                          ,

=== page tag ===
:
```


## [2026-09-06T16:06:58.269Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"\\[pdf page\" incoming/WLD/WLD_Bd1_pages.txt | awk -F: '$1<=33817' | tail -2; sed -n '33900,33960p' incoming/WLD/WLD_Bd1_pages.txt"
}
```


### [2026-09-06T16:07:00.161Z] TOOL RESULT

```
beruhen (Schrader BB. 15, 127 f., Trautmann KZ. 46, 239 f.), gr. xtUovQog'
oeiaonvyig Hes. („Bachstelze“, der Ausgang     ist ovga „Schwanz“, aber viel-
leicht erst  nach oetoovga ds. angetreten), lit. Idele, kyle lett. cielawa, apr.
                                                                                                     ,

ktjlo „Bachstelze‘' (Froehde BB. 3, 306; aber ai. khelati „schwankt“, ebenda,

bleibt      besser          fern;       desgleichen wohl                      lat.    motacilla,   s.    Yf.   LEWb. 2 s. v.‘;
lat.    cdlo,        -ere   „bewegen“                   ist   vielleicht nur           Grammatikererfindung,             s.   Yf.
LEWb. 2 s. v.; wenn echt, ware es kaum als *ci-l-no aufzufassen, eher als
*cllo    mit Konsonantenschiirfung nach                                   cello').

     Zum Wzvokalismus:                           fiir   e-Yok.     (qei-) ist          das urgerm. nord. Praet. *hcH
(:   got. haihait)           keine           sichere          Stiitze.
                                                  ist lit. koja, lett. kdja   Andrerseits
„Fu6“, das Bezzenberger KZ. 47, 82 fur idg. *qdi- anfuhrt, in seiner Zu-
gehorigkeit sehr zu bezweifeln.
     Wzform qi-eu- ohne Nasalinfix     :   ai. cyavate   „regt sich, geht fort“, ao. s[y)a-
vaite „setzt sich in     Gang, Marsch       ,
                                                apers. usiyavani    ;
                                                                        ,marschierte“ (usw.,
s. Bartholomae Airan. Wb. 1714 f.), ai. cydutnd- n. „Unternehmung, Be-
muhung", av. syad&na- n. „Ton, Handelu, Wirken", syadman- n. „Tat,
Werk“ (Wackernagel KZ. 25, 276 m. Lit.); arm. cu (= ai. cyuti-) „Auf-
bruch", qvem ,,ich breche auf, reise ab“, Aor. (zum Praea. erfam) cogay
„ich ging“ ( *qioyi-; Hiibschmann Arm. Gr. I 485 ff.); gr. oevco „setze in
rasche, heftige Bewegung", med. „eilen, erregt sein“ (ore ooevano usw.;
aevezat = cyavate-, das nur arcbaische Verbum— att. ware *oeco         fordert    —
trotz Brugmann-Thumb GrGr. 4 323 keine Gdf. *oev-oa> mit Determinativ
-s-, s. Wackernagel aaO.; der Diphthong kann nach den auBerpraes. Formen

und nach unthemat. aevzai        —
                               wenn dies alt ist              —
                                                     festgehalten sein), hom.
eoovzo „eilte“, ppp. iaavpevog, em-aavzog „herandrangend, daherstiirmend"
s. auch Bois. u. enaaavzEQog = ai. cyuta- „getrieben“, vgl. av. fra-suta-  „in
Gang gekommen", jzav-ovdig (s. Bois.); att. aovjuai „bewege mich rasch
oder heftig" ( *oopoopat), ovei (Bacchyl.) „treibt“, iaoorjpivov ze&OQvPgpevov,
                                                                            -



OQfig/zevov lies., hom. ?.ao-oo6og „die Yolker zum Kampfe antreibend";
att. zsvpibpai „betreibe“ (vgl. av. syadman-)        zevzaCoj „bescliaftigo mich
                                                          ;


anhaltend mit etwas" (Bezzenberger Fick BB. 6, 236, Wackernagel KZ.
                               s
28, 121, Brugmann Grdr. I         274, G. Meyer Alb. St. Ill 52, Lagercrantz
Z. gr. Ltgesch. 5Sff.) ; eine Dehnstufenbildung wie ai. cyautnd -, aber mit
geschwundenem u ist das wohl hierhergehorige acbzgov „das holzerne Rad",
emaacozQov „Radreifen“ (Prellwitz 1 2 s. v., Bechtel Lexil. 133).
                                            ‘




kei-g-, kei-p- „nach Luft schnappen, vor Nachlaufen keuchen"?
  Fick III 4 89 Falk-Torp u. hibe, hige hikke, forhippen fuhren auf eine
```


## [2026-09-06T16:07:17.048Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== SKT cite/excite ===\"; grep -n -i -E \"ciere|citare|excite\" SKT.txt | head -10; echo \"=== SKT kinetic ===\"; grep -n -i -E \"kinetic|kinema|cinema\" SKT.txt | head -5; echo \"=== FSD cinema ===\"; grep -n -i -E \"^cin.ema|cinematograph\" FSD_vol1.txt | head -5"
}
```


### [2026-09-06T16:07:17.135Z] TOOL RESULT

```
=== SKT cite/excite ===
5887:Entloe.  f F.)  M.  E.  mfiren.  -  O.  F.  ^«- tiegr,  nuUhtr^  lo  excite.     Origin  onknown.
11652:Gommiserstion.  (F  -L) era/ion.  —  L  ace.  commiieraJtoaem,  p* an  oration    intended  to  cxaie    ptty commiserari,    to    excite    pity.  —  L {-cum),   with;    miseran,   to  pitj.  « miser.
16240:(iicand.)     M.  E.  ruggeti\  a1$o C.  T.  ^^^s>.     The  Utter  is  from '.  rough,  hairy.  -•  Swcd.  ruggt Ijjlcd  hnir  (above). Roulotte :  see  Botary. >UQd,  to  wliu]>cr :  sec  Budo. L  Boimdel :  see  Botary. 1(1).  to  excite,  to  wake  up.  (Scond.) if  the  chase ;   when  a  hart  nuhed Its   covert,   it  was  &aid    to  roNse. \sen,  to  rush  out.  •»  Swed.  rusa,  to Mt  frtm.  to   nisb  forward;    Dan. |aih.     Cf  A.  S.  hrt6xan^  to  rush, Ed  quickly.     (Base  MRUS.) K  (Scand,)     Formed  from  rtmse ring  a-.     This  prefix  was  clearly d  by  that  of  arMt ;  see  A-  (4). [1),    to    move    swiftly    forward. '  \E.  rmehtn.^O.  Swed.  nukik, lo  shake.     Extesuion  of  O. tn  rush  ;   sec  above.     Cf.  Dan. ike.  (nill,  twitch. (Scand.)      Fre<|nent.  of  Swed. tir,  make  a  noi«c.  a  variant  of nka,  to  shake,  rush  ;  sec  above. tstheHf   nucAen,    to   niatlc.  to
17758:—  L.  soUicitus,  lit.  wholly  agitated.  *  L. «//j-,  for  toih;  crude  form  of  sollus,  whole  ; ff'/wi.  aroused,  pp.  of  eiere,  to  shake,  excite. See  Solemn  and  Oite.  Der.  nt/ici/ot4s, for  L.  soilidtus;  sa/icitude,  F,  toliciiiuU, from  L.  soHiitndo,  anxiety.
20472:Uproar,  tumult.  (Du.)  The  spelling shews  confusion  with  E.  nwr.  —  Du.  oproer, '  uprore,  tumult ; '  Mexham.  —  Dn.  ep,  up ; roeren,  to  excite,  stir,  move ;  $0  that  oprotr >=  a  stirring  up.  commotion,  -f*  Swetl.  upp- rer,  Dan.  uprar,  G-  aufruhr.  p.  The verb  is  Da.  rvcrtn,  Swed.  rSra,  Dan.  rihr, G.  riihrtn,  A.  S.  Mr/raa,  to  stir  ;  see R«remoiiae.  The  A.  S.  Ar/ran  is  from An<r,  a(l|.,  active,  busy,
=== SKT kinetic ===
=== FSD cinema ===
11571:mou  fowls  and  pheasants.  [<  Gr.  alcktorts,  fern,  of  alcklOr,  Orne  department,  France.—  Alen^on  lace,  see  lace1.  al"e-tno-ra'ma,  1   alVtbo-rU'ma;  2   al'e-tho-ra'raa,  n.  An cock.]  —   aI"cc-tor'l-dlnc,  a.  a-Iength't»  adv.  <t  prep.  At  full  length;  lengthwise  to  or  of.  Improved  cinematograph  in  which  the  screen  is  continu-
66945:sisters.  2.  A   household  drudge;  kitchen-maid.  3.  [Eng.]  A dance  kept  up  till  midnight.  [F.  cendrUlon,  little  clnder-girL] Cl-ne'ans,  1   si-nl'anz;  2   cl-nS'ans*  n.  pi.  Bib.  (Douai). cln^e-fac'tlont,  n.  Reduction  to  ashes, cln'c-ma,  1   eln'o-ma;  2   gln’e-ma,  n.  [Eng.]  A   motion- picture;  picture-play.  [Abbr.  or  cinematograph.] cln"e-mat'lc,  etc.  Same  as  kinematic,  etc. cln"e-mat  'o-graph,  1   slnVmat'o-grnf;  2   cln'e-miit'o-grM,
66958:cln'e-neg"a-tlref \   1   sln'i-neg'a-tlv;  2   cln'e-n&g'a-tlv, n.  A cln'e-neg*a-tlv3,  J   film  of  cinematographic  negatives.  [<
```


## [2026-09-06T16:07:48.680Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; for u in \\\n 'https://en.wiktionary.org/wiki/%D8%B4%D8%AF%D9%86' \\\n 'https://www.etymonline.com/word/cinema' \\\n 'https://www.etymonline.com/word/kinetic' \\\n 'https://www.etymonline.com/word/cite' \\\n 'https://abadis.ir/fatofa/%D8%B3%DB%8C%D9%86%D9%85%D8%A7/' \\\n 'https://en.wiktionary.org/wiki/%D8%B3%DB%8C%D9%86%D9%85%D8%A7' \\\n 'https://en.wiktionary.org/wiki/%CE%BA%CE%B9%CE%BD%CE%AD%CF%89' \\\n 'https://en.wiktionary.org/wiki/%CF%83%CE%B5%CF%8D%CF%89' \\\n 'https://en.wiktionary.org/wiki/cieo' ; do\n python3 tools/fetch_source.py \"$u\" --note 'pdf page 248, root Kei 2 (PIE *keih2-/*kyew-), verification of sodan/cinema/kinetic/cite chain' 2>&1 | tail -2\ndone"
}
```


### [2026-09-06T16:07:55.721Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/851d8fcd26a60f97.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8b28004c742e69c3.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/bc48103fdad16ae7.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/08d74d823c9e15e5.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8ae1ec2743cede47.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c39311e3d4b6e4c7.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/33e798ae47488532.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c76bb6249b08f04a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8887e83775dc93a8.txt
```


## [2026-09-06T16:08:00.152Z] TOOL CALL #64: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg248.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/248.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/248.png; echo \"=== verify_check help ===\"; sed -n '1,60p' /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-06T16:08:00.250Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 49887 Sep  6 12:08 /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/248.png
=== verify_check help ===
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


## [2026-09-06T16:08:03.128Z] TOOL CALL #65: Bash

```json
{
 "command": "sed -n '60,130p' /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-06T16:08:03.173Z] TOOL RESULT

```
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


## [2026-09-06T16:09:27.449Z] AGENT

Now I'll write the verification file.


## [2026-09-06T16:14:39.318Z] TOOL CALL #66: Bash

```json
{
 "command": "cat > /home/sfmqrb/git/rishe/data/verification/page-248.json << 'JSONEOF'\n{\n  \"pdf_page\": 248,\n  \"book_page\": 218,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-06\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Kei 2, Kie 2, Ki 1\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *keyh₂- (Pokorny's kēi- : kəi- : kī̆-) 'to set in motion, be in motion'\",\n      \"note\": \"The root is real and correctly labelled: Pokorny IEW 538-539 'kēi-, kəi-, kī̆- : in Bewegung setzen, in Bewegung sein (: koi- : kī-); eu-Basis (z. T. mit n-Infix) ki-(n-)eu-; schwere Basis kiə-'. Nourai's three variant names Kei/Kie/Ki simply reproduce Pokorny's ablaut series (kēi- : kiē- : kī-), and the gloss 'to set in motion' is Pokorny's and Watkins' own ('kei-3. To set in motion. [Pok. kei- 538]'). Wiktionary/LIV² now write the root as *keyh₂-. ONE CROSS-CUTTING CAVEAT applies to the whole chart: Pokorny (539), Walde-Pokorny (I 361ff.), Klein (s.v. cite) and Ernout-Meillet (s.v. cieo) all treat the u-extension ki-eu- (Skt. cyávate, Av. šyav-, OP šiyav-, Gk. σεύω) as belonging to this same root, which is exactly what Nourai draws. Modern reconstruction (LIV² 340 vs 346, Beekes s.v. σεύω, Cheung EDIV 41) splits them: the Indo-Iranian branch goes back to *ḱyew- with a palatal (satem c-/š-), whereas Greek κίω/κινέω and Latin cieō require a plain velar *keyh₂-. Under that split the Old Persian and Avestan boxes of this chart do not in fact hang from the same root as the Greek and Latin boxes.\",\n      \"note_fa\": \"ریشهٔ هندواروپایی آغازین که نورایی آن را «Kei 2, Kie 2, Ki 1» به معنی «به حرکت درآوردن» آورده، همان ریشهٔ kēi- در فرهنگ پوکورنی (ص ۵۳۸–۵۳۹) است: «in Bewegung setzen, in Bewegung sein»؛ سه صورتی که نورایی نام برده در حقیقت همان زنجیرهٔ ابدال آوایی (kēi- : kiē- : kī-) نزد پوکورنی است. در بازسازی امروزی این ریشه را *keyh₂- می‌نویسند. یک نکتهٔ مهم دربارهٔ کل این نمودار: پوکورنی، والده-پوکورنی، کلاین و ارنو-مییه شاخهٔ گسترش‌یافته با -eu (سنسکریت cyávate، اوستایی šyav-، پارسی باستان šiyav-، یونانی σεύω) را زیر همین ریشه می‌آورند و نورایی نیز چنین کرده است؛ اما پژوهش امروزی (LIV²، بیکس، چونگ) این دو را جدا می‌کند: شاخهٔ هندوایرانی از *ḱyew- با کام‌گانه (ḱ) است و یونانی κινέω و لاتینی cieō از *keyh₂- با ک ساده. بنابراین اصلِ ریشه درست است، ولی پیوند دو نیمهٔ نمودار (ایرانی در برابر یونانی/لاتینی) بر پایهٔ ریشه‌شناسی کهنِ پوکورنی است.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/%CE%BA%CE%B9%CE%BD%CE%AD%CF%89\",\n        \"https://en.wiktionary.org/wiki/%CF%83%CE%B5%CF%8D%CF%89\",\n        \"https://en.wiktionary.org/wiki/cieo\",\n        \"https://en.wiktionary.org/wiki/%D8%B4%D8%AF%D9%86\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:539\", \"status\": \"supports\", \"note\": \"POK_02.txt leaf 196 (= IEW p.538) prints the headword 'kei- ,in Bewegung setzen, in Bewegung sein' (: koi- : kī-); eu-Basis (z. T. mit n-Infix) ki-(n-)eu-; schwere Basis kiə- (: kiē-?)'; the section 'Wurzelform ki-eu- ohne Nasalinfix' with the Iranian forms falls on leaf 197 = p.539, so Nourai's page number is right for the Iranian material and one page late for the root heading itself.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"WLD\", \"where\": \"Bd. I p. 361 ff., s.v. qei- (WLD_Bd1_pages.txt line 33817)\", \"stance\": \"supports\", \"note\": \"'qei- (?? s. u.) „in Bewegung setzen, in Bewegung sein“ (: qəi- : qī-); eu-Basis ... qi-(n-)eu-; set-Basis qiə-' — the direct model for Pokorny's entry, same lumping of the Greek/Latin and Indo-Iranian material.\"},\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. kei-3\", \"stance\": \"supports\", \"note\": \"'kei-3. To set in motion. ... II. Zero-grade form *ki-. 1. Form *ki-eyo- in Latin ciēre (past participle citus), with its frequentative citāre ... 2. Suffixed form *ki-neu- in Greek kinein, to move (> kinēsis, motion) ... [Pok. kei- 538.]' — identical root and gloss; Watkins lists no Indo-Iranian under it (his appendix only tracks English words, so this is not evidence against).\"},\n        {\"src\": \"IEC\", \"where\": \"searched IEC.txt for Kei-/Kiu-/kineo\", \"stance\": \"silent\", \"note\": \"Mann has 'Kei- (1) He, fall', 'Kei (2) here, there' and 'Kiuos (4) dark grey', but no root Kei- 'to set in motion'; his nearest entry is 'kin- start, move, do, perform. WP I, 362 & 510 ... Gk. kinéo'.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Old Persian\",\n          \"words\": \"šiyav; šaw\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"OP šiyav- 'to set out, march' is genuine and well attested: impf. 1sg. ašiyavam <a-š-i-y-v-m> (DB 1.84, 1.91, 2.3), 3sg. ašiyava (DB 1.80, 2.17), 3pl. ašiyavan (DB 1.76); Bartholomae's headword (AiW col. 1715) is exactly 'p. šiyav-, g. syav-, j., g. šav- V. „sich in Bewegung setzen“', and Kent 211a glosses it 'go, march'. It continues Proto-Iranian *ćyaw- < PIE *ḱyew- (Skt. cyávate), the -y- reflecting Indo-Iranian *ćy-. TWO reservations. (a) The second word 'šaw : to go' is not an Old Persian form — no OP *šaw is attested anywhere in the Achaemenid corpus; šaw- is the Middle Persian present stem (BMP ʿZLWN-, MMP šw-, /šaw-/) continued by NP شو, and Nourai has pulled it up one stage. Horn's cited page has it as the New Persian present ('šūden ... Praes. šev-em'), and Nourai himself puts Avestan šav- in node #4. (b) The arrow from this root holds only under Pokorny's lumping; Cheung EDIV 41 sets the whole Iranian family under *ćiau < PIE *ḱyew-, a root distinct from the *keyh₂- that yields Greek κινέω and Latin cieō.\",\n          \"derivation_fa\": \"پارسی باستان šiyav- «به راه افتادن، لشکر کشیدن» واژه‌ای اصیل و پرکاربرد در سنگ‌نبشتهٔ بیستون است (ašiyavam «به راه افتادم»، ašiyava «رفت»)؛ بارتولومه در ستون ۱۷۱۵ سرواژه را چنین آورده: «پارسی باستان šiyav-، گاهانی syav-، اوستایی متأخر šav- : به حرکت درآمدن»، و کنت نیز آن را «رفتن، لشکر کشیدن» معنی کرده است. این ستاک از ایرانی باستان *ćyaw- و آن از هندواروپایی *ḱyew- است (هم‌ریشه با سنسکریت cyávate). دو نکته: نخست آنکه واژهٔ دوم یعنی šaw «رفتن» صورت پارسی باستان نیست؛ هیچ گواهی از *šaw در پارسی باستان در دست نیست و šaw- ستاک مضارع فارسی میانه (پهلوی ʿZLWN-) و «شو»ِ فارسی نو است، چنان‌که هرن نیز آن را ستاک مضارع فارسی نو («šev-em») آورده. دوم آنکه پیوند این جعبه با ریشهٔ یونانی/لاتینی نمودار، بر پایهٔ ریشه‌شناسی کهن است و چونگ آن را زیر ریشهٔ جداگانهٔ *ćiau می‌آورد. پس ادعای نورایی با احتیاط پذیرفتنی است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D8%B4%D8%AF%D9%86\"],\n          \"ref_check\": [\n            {\"ref\": \"POK:539\", \"status\": \"supports\", \"note\": \"POK_02 leaf 197 (= IEW p.539): 'Wurzelform ki-eu- ohne Nasalinfix: ai. cyávate „regt sich, geht fort“, av. š(y)avaite „setzt sich in Gang, Marsch“, apers. ašiyavam „marschierte“' — Nourai's arrow root → OP šiyav- is verbatim Pokorny's.\"},\n            {\"ref\": \"HRN:172\", \"status\": \"supports\", \"note\": \"HRN.txt leaf 194 (printed p.172), entry 778: 'šūden „gehen; sein, werden“, Praes. šev-em. ap. √šiyav-, ašiyavam, ašiyuva „gehen, marschiren“; aw. √šav-, šuvaite „gehen“; ai. √cyav-, cyávate „fortgehen“' — supports OP šiyav-, but shows šev-/šaw- as the NEW Persian present, not an OP word.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"col. 1715, s.v. šiyav-\", \"stance\": \"supports\", \"note\": \"'p. šiyav-, g. syav-, j., g. šav- V. „sich in Bewegung setzen“. Praes. 1 syav-, šav-, 2 šiyava- ... 1) „sich in Gang, Marsch setzen, proficisci“, militärisch' with the Bisotun citations (Bh. 2.7, 3.1, 4.11); no Old Persian šaw.\"},\n            {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, §; lexicon s.v. šiyav- (KNT.txt line 1402, 2668)\", \"stance\": \"supports\", \"note\": \"'ašiyava „he went forth“, Skt. (mid.) cyavate'; and in the syntax section 'names of places are often used thus without a preposition (regularly with fra-ais-, ar-, ava-ar-, pard-ar-, šiyav-)'. Only šiyav- is listed as the Old Persian stem.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"EDIV p. 41, s.v. *ćiau\", \"stance\": \"partial\", \"note\": \"'*OLD PERSIAN: š(i)yav- „to set, go forth“ = Kent: 211a' — confirms the OP word, but files the whole family under *ćiau with '*PIE *kjeu- „to move, go“', i.e. a different root from the one Nourai's box hangs on.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"šutan\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The Middle Persian verb is real and the form is right: Book Pahlavi <šwtn'> is read šutan (Nyberg) or šudan (MacKenzie), present šaw- written with the Aramaic ideogram ʿZLWN-. It continues OIr. *šu-ta- (weak grade of *šyaw- plus the -ta- participle suffix) beside present *šaw-a-; Hübschmann §41 states the sound law precisely: 'Ap. y schwand nach š schon im Pehlevi: np. šudan, pr. šavam „gehen, werden“, ap. ipf. ašiyavam. In beiden Fällen ist np. š = ap. šiy = arisch čy.' The one problem is the GLOSS: in Middle Persian šutan/šudan means 'to go' (opposite of āmatan 'to come'), not 'to become' — MacKenzie and Nyberg both give only 'go'. The copular/inchoative sense 'to become' (and the passive auxiliary) is a New Persian development; Cheung records it as 'NP šudan/šaw- „to become; [obs.] go“'. So the node is right in form and descent, one stage early in meaning.\",\n          \"derivation_fa\": \"فعل فارسی میانه که در پهلوی کتابی <šwtn'> نوشته می‌شود و آن را šutan (نیبرگ) یا šudan (مکنزی) می‌خوانند، با ستاک مضارع šaw- که با هُزوارش ʿZLWN- نوشته می‌شود. این صورت از ایرانی باستان *šu-ta- (صورت ضعیف ریشهٔ *šyaw- + پسوند اسم مفعولی -ta) و ستاک مضارع از *šaw-a- است. هوبشمان در بند ۴۱ قانون آوایی را روشن بیان کرده: «ی پس از ش، در پهلوی از میان رفته است؛ فارسی نو šudan و ستاک مضارع šavam در برابر پارسی باستان ašiyavam؛ در هر دو مورد š فارسی نو برابر šiy پارسی باستان و čy آریایی است.» تنها ایراد در معنی است: در فارسی میانه šutan یعنی «رفتن» (در برابر āmatan «آمدن») و معنیِ «شدن، گردیدن» تحول معنایی دورهٔ فارسی نو است. پس صورت و تبار درست است و معنی یک مرحله زودهنگام آمده.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D8%B4%D8%AF%D9%86\"],\n          \"ref_check\": [\n            {\"ref\": \"HRN:172\", \"status\": \"partial\", \"note\": \"Horn no. 778 (printed p.172) is headed by the NEW Persian infinitive 'šūden „gehen; sein, werden“' and cites Old Persian, Avestan and Sanskrit for it; he gives no Pahlavi form in this paragraph (unlike his neighbouring entries 777, 782 where 'phlv.' forms are quoted). The page therefore backs the OP → NP chain but does not itself document the Pahlavi box.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary, s.v. (PHD_mackenzie.txt line 4855)\", \"stance\": \"partial\", \"note\": \"'šudan, šaw- [ʿZLWN-tn' < A ʾzl; MMP lwb- | M lwdn, lw-] go.' — form confirmed, meaning given only as 'go', not 'become'.\"},\n            {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II, glossary s.v. šutan (NYB_vol2_glossary.txt line 3675)\", \"stance\": \"partial\", \"note\": \"'šutan [ʿZLWN-tn'] šav- [ʿZLWN-], to go, opp. (ā)matan to come: hac kē mat hom u apāc ō kū šavom? „whence have I come and whither shall I go?“' — Nourai's transliteration šutan is Nyberg's; the gloss 'to become' is not Middle Persian.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"EDIV p. 41, s.v. *ćiau, section *MIDDLE PERSIAN / *PARTHIAN\", \"stance\": \"supports\", \"note\": \"'MMP šw-, BMP šwb- (ʿZLWN-) /šaw-/ „to go“ ... Inf.: MMP šwdn'; Parthian 'šw- „to go“'.\"},\n            {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien §41 (HUB.txt line 5337)\", \"stance\": \"supports\", \"note\": \"'np. šudan, pr. šavam „gehen, werden“, ap. ipf. ašiyavam. In beiden Fällen ist np. š = ap. šiy = arisch čy.'\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"šodan «شدن»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"NP شدن šodan < MP šudan/šutan < Old Iranian *šu-ta- (past stem, weak grade of the root šyaw- + -ta-), with the present stem شو šow < MP šaw- < OIr. *šaw-a-. Abolghasemi (FFD) states it in exactly these terms: 'شد < فارسی میانه šud < ایرانی باستان *šu-ta ... šu صورت ضعیف ريشهٔ šyaw و آن به معنی «رفتن» است' and 'شو < فارسی میانه šaw < ایرانی باستان *šaw-a'. Semantically the verb kept 'to go' into classical Persian (Ferdowsi, Rumi) and then specialised as the copula/inchoative 'to become' and as the passive auxiliary (کشته شد), the sense the modern language knows; Cheung glosses NP šodan 'to become; [obs.] go'. The parenthesised forms Nourai adds are (i) شو šow, the present stem/imperative, and (ii) تاشو tāšow 'folding, collapsible' (تا 'fold' + شو), a modern compound built on that stem.\",\n          \"derivation_fa\": \"«شدن» بازماندهٔ فارسی میانهٔ šudan/šutan است و آن از ایرانی باستان *šu-ta- (صورت ضعیف ریشهٔ šyaw- به‌علاوهٔ پسوند -ta) ساخته شده؛ ستاک مضارع «شو» از فارسی میانهٔ šaw- و ایرانی باستان *šaw-a-. ابوالقاسمی در «فعل‌های فارسی دری» ص ۶۲ همین را می‌گوید: «شد < فارسی میانه šud < ایرانی باستان *šu-ta ... šu صورت ضعیف ریشهٔ šyaw و آن به معنی رفتن است» و «شو < فارسی میانه šaw < ایرانی باستان *šaw-a». معنی اصلی «رفتن» بوده که تا فارسی کلاسیک (فردوسی، مولوی) زنده مانده و سپس به «گردیدن، صیرورت» و کاربرد کمکیِ مجهول («کشته شد») تحول یافته است. دو صورت داخل پرانتز در کتاب، «شو» (ستاک مضارع/امر) و «تاشو» (تا + شو، «تاشونده») است. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D8%B4%D8%AF%D9%86\"],\n          \"ref_check\": [\n            {\"ref\": \"BQT:1261\", \"status\": \"supports\", \"note\": \"Borhan-e Qate' p.1261 (BQT_v3_picofile.pdf pdf-page 52; rendered to data/verification/sources/refs/ocr/BQT/1261.png). Mo'in's footnote under the headword شدن reads: «شدن ... پهلوی šutan، ایرانی باستان *šyav-، *šav-؛ بارتولمه ۱۷۱۶، نیبرک ۲۱۸؛ پارسی باستان ریشهٔ šiyav- (رفتن، راه رفتن)، اوستا ریشهٔ šyav- (رفتن)، هندی باستان ریشهٔ cyav- (رفتن، ادامه دادن)، ارمنی č̣u (حرکت)، کردی čū (رفتن)، افغانی šawəl، آستی cæwyn، بلوچی šutin/šawagh، طبری šawwāme (می‌روم)، مازندرانی šone، گیلکی šoon (رفتن)» — i.e. exactly Nourai's Old-Persian → Pahlavi → Persian chain, and Mo'in himself cites Bartholomae col. 1716 and Nyberg 218.\"},\n            {\"ref\": \"FFD:62\", \"status\": \"supports\", \"note\": \"Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, headword شدن (FFD_pages.txt lines 1705-1712, pdf pages 67-68 = printed 61-62): «شد < فارسی میانه šud < ایرانی باستان *šu-ta ... šu صورت ضعیف ریشهٔ šyaw و آن به معنی «رفتن» است» and on the next page «شو < فارسی میانه šaw < ایرانی باستان *šaw-a».\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HRN\", \"where\": \"no. 778, p.172\", \"stance\": \"supports\", \"note\": \"'šūden „gehen; sein, werden“, Praes. šev-em. ap. √šiyav- ... aw. √šav-, šuvaite „gehen“; ai. √cyav-, cyávate' — plus the dialect reflexes kurd. čūn, oss. cæwyn, bal. šuta/šut.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"EDIV p. 41, s.v. *ćiau, section *NWIR\", \"stance\": \"supports\", \"note\": \"'NWIR: Widely attested: NP šudan/šaw- „to become; [obs.] go“, Bal. šut-, Kurd. (Kurm.) čûn, čûyîn (ç-), Zaz. šiyayiš/šin-, Gil. (Rsht.) šoan/š- „to go“' — documents both the form and the 'go' → 'become' shift.\"},\n            {\"src\": \"HUB\", \"where\": \"Persische Studien §41\", \"stance\": \"supports\", \"note\": \"'np. šudan, pr. šavam „gehen, werden“, ap. ipf. ašiyavam' — the y-loss after š.\"},\n            {\"src\": \"MON\", \"where\": \"Mo'in's etymological footnote as printed in Borhan-e Qate' p.1261\", \"stance\": \"supports\", \"note\": \"same footnote as under BQT:1261 above; Mo'in's own reconstruction «ایرانی باستان *šyav-, *šav-» matches the chart.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Avestan\",\n          \"words\": \"šav 2, šyav; šyaothna; šyaoman; fra-šŭte\",\n          \"verdict\": \"transcription_suspect\",\n          \"error_in\": \"book\",\n          \"book_prints\": \"fra-šŭte\",\n          \"correct_form\": \"fra-šūta-\",\n          \"derivation\": \"Three of the four words are exactly right. (1) Av. šav-/šyav- 'to move, set out': Bartholomae AiW col. 1715 heads the verb 'p. šiyav-, g. syav-, j., g. šav- V. „sich in Bewegung setzen“', so Nourai's 'šav 2, šyav' reproduces the two Avestan stem shapes (Gathic syav-, Younger Avestan šav-). (2) šyaoθna- n. 'deed, action' (AiW col. 1711-1714, 'Zum V. syav-; ai. vgl. cyautná- „Unternehmung“'; Pahlavi gloss kunišn) — Nourai's 'conduct, effect' is a loose but acceptable rendering. (3) šyaoman- n. 'Tat, Werk' (AiW col. 1713, Y 32.3) = Nourai's 'action, work', verbatim. (4) 'fra-šŭte' is NOT an attested Avestan form: what the texts have is the perfect passive participle fra-šūta- 'set going, in motion' (Vr 12.2; Pokorny 539 'vgl. av. fra-šuta- „in Gang gekommen“'), beside the s-present frašusaiti (V 5.2) and the imperative frašusa (Yt 17.60); Bartholomae's sub-entry is 'mit avi und fra „fortgehen zu —“ ... mā avi asmanəm frašuta Yt 19.60'. The page image (pdf p.248, copied to sources/refs/ocr/BOOK/248.png) shows that the book itself prints 'fra-šŭte', so this is Nourai's own misprint/mis-citation of fra-šūta-, not an extraction error. Verdict for the derivation as a whole: the four words all belong to the verb šyav- and are in Pokorny at 539 word for word, but as with node #1 the arrow from *keyh₂- holds only under the older lumping; Cheung/LIV² put them under *ḱyew-.\",\n          \"derivation_fa\": \"سه واژه از چهار واژهٔ این جعبه کاملاً درست است: اوستایی šav-/šyav- «به حرکت درآمدن» (بارتولومه ستون ۱۷۱۵؛ صورت گاهانی syav- و اوستایی متأخر šav-)؛ šyaoθna- «کردار، کنش» (ستون ۱۷۱۱–۱۷۱۴، در پهلوی kunišn، هم‌ریشه با سنسکریت cyautná-)؛ šyaoman- «کار، کردار» (ستون ۱۷۱۳، یسنه ۳۲٫۳). اما صورت چهارم، «fra-šŭte»، در متون اوستایی گواهی نشده است؛ آنچه هست fra-šūta- (اسم مفعول کامل، ویسپرد ۱۲٫۲: «به راه افتاده») و نیز frašusaiti و امرِ frašusa است. تصویر صفحهٔ چاپی نشان می‌دهد که خودِ کتاب «fra-šŭte» چاپ کرده است؛ پس این خطای چاپی کتاب است نه خطای خوانش اسکن. افزون بر این، مانند جعبهٔ پارسی باستان، انتساب این واژه‌ها به همین ریشه بر پایهٔ ریشه‌شناسی پوکورنی است و چونگ آن‌ها را زیر *ḱyew- می‌آورد.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%CF%83%CE%B5%CF%8D%CF%89\"],\n          \"ref_check\": [\n            {\"ref\": \"POK:539\", \"status\": \"supports\", \"note\": \"POK_02 leaf 197 (= IEW p.539): 'av. š(y)avaite „setzt sich in Gang, Marsch“ ... av. šyaoθ-na- n. „Tun, Handeln, Wirken“, šyaoman- n. „Tat, Werk“ ... vgl. av. fra-šuta- „in Gang gekommen“'. All four of Nourai's Avestan items stand on this page, but the printed form is fra-šuta-, not fra-šŭte.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"AiW cols. 1711-1716\", \"stance\": \"supports\", \"note\": \"col. 1715 'p. šiyav-, g. syav-, j., g. šav- V. „sich in Bewegung setzen“ ... PPfP. *šuta-'; col. 1713 'g. šyaoman- n. „Tat, Werk“ ... Zum V. šyav-. Vgl. šyaoθna-'; the šyaoθna- article ends 'Zum V. syav-. — ai. vgl. cyautná- n. „Unternehmung“. — Pü.: kunišn'; under 'mit avi und fra': 'mā avi asmanəm frašuta Yt 19.60'.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. I p. 362, s.v. qei-, section 'Wzform qi-eu-'\", \"stance\": \"supports\", \"note\": \"'av. š(y)avaite „setzt sich in Gang, Marsch“, apers. ašiyavam „marschierte“ (usw., s. Bartholomae Airan. Wb. 1714 f.), ... av. šyaoθna- n. „Tun, Handeln, Wirken“, šyaoman- n. „Tat, Werk“ ... vgl. av. fra-šuta- „in Gang gekommen“' — again fra-šuta-.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"EDIV p. 41, s.v. *ćiau, section *AVESTAN\", \"stance\": \"partial\", \"note\": \"'*AVESTAN: š(ii)auu- (šauu-, šu-) „to move, go“ || (+ *fra-) „to set, go forth“ ... Partic.: perf. pass. YAv. *frasūta- (Vr 12.2) ... IMPV. 2sg. YAv. frasusa (Yt 17.60)' — confirms the words and the form fra-šūta-, but assigns the family to *ćiau < PIE *kyeu-, not to Nourai's root.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": null,\n          \"words\": \"\",\n          \"verdict\": \"unverified\",\n          \"derivation\": \"Empty pass-through box: the chart draws an arrow from the Avestan box to a framed rectangle that carries no language label, no reference and no words. The printed page confirms this is how the book itself looks (pdf p.248 rendered at 200 and 600 dpi; copy at data/verification/sources/refs/ocr/BOOK/248.png shows a blank double-ruled box to the right of the Avestan box), so the extraction is faithful and there is simply nothing to verify — presumably a layout slot Nourai left unfilled (elsewhere on this page the same position holds the borrowing/descendant of the box to its left).\",\n          \"derivation_fa\": \"این جعبه در خود کتاب خالی است: از جعبهٔ اوستایی پیکانی به یک چارگوش بی‌نام و بی‌واژه کشیده شده که نه نام زبان دارد و نه ارجاع. تصویر صفحهٔ چاپی (صفحهٔ ۲۴۸ پی‌دی‌اف، برابر صفحهٔ ۲۱۸ کتاب) نشان می‌دهد که خطای خوانش اسکن در کار نیست و خودِ کتاب جعبه را تهی گذاشته است؛ ظاهراً جای واژه‌ای بوده که نویسنده پر نکرده است. بنابراین چیزی برای راستی‌آزمایی وجود ندارد.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the node carries no references in the book.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BOOK\", \"where\": \"printed page 218 = pdf page 248, image at data/verification/sources/refs/ocr/BOOK/248.png\", \"stance\": \"silent\", \"note\": \"the box is printed blank in the original; nothing was lost in extraction.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Greek\",\n          \"words\": \"kinein; kiněma\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Gk. κῑνέω, inf. κῑνεῖν 'to set in motion, move' (Homer onwards, Il. 1.47 etc.) is built on the nasal-infixed stem *ki-n-u- of the root: Pokorny 538 'von ki-n-eu-: gr. κίνυμαι „werde bewegt, erschüttert, gehe“, κινύσσομαι „schwanke hin und her“, κῑνέω „setze in Bewegung, treibe“ (*κῑνεϝ-ω)'. The verbal noun κίνημα, gen. κινήματος 'movement, motion' (Aristotle, Plato) is regularly formed with the -μα/-ματ- suffix. Wiktionary derives κινέω from *keyh₂- and links it with κίω 'to go' and Latin cieō, i.e. exactly the group Nourai draws. Nourai's 'kiněma' with a breve is his own transcription habit; the Greek vowels are long ῑ and η (kī́nēma).\",\n          \"derivation_fa\": \"یونانی κῑνέω / مصدر κῑνεῖν «به حرکت درآوردن» از ستاک با میان‌وند خیشومی *ki-n-u- ساخته شده است؛ پوکورنی در ص ۵۳۸ می‌نویسد: «از ki-n-eu-: یونانی κίνυμαι „به حرکت درمی‌آیم“، κῑνέω „به حرکت درمی‌آورم“ (از *κῑνεϝ-ω)». اسم مصدر κίνημα (اضافی κινήματος) «حرکت» با پسوند -μα/-ματ- از همین فعل ساخته شده و نزد ارسطو و افلاطون به کار رفته است. ویکی‌واژه نیز κινέω را از *keyh₂- و هم‌خانوادهٔ κίω «رفتن» و لاتینی cieō می‌داند؛ یعنی همان گروهی که نورایی رسم کرده است. نشانهٔ کوتاهی روی «ě» در «kiněma» شیوهٔ آوانگاری خودِ نورایی است؛ در یونانی هر دو واکه بلندند. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%CE%BA%CE%B9%CE%BD%CE%AD%CF%89\"],\n          \"ref_check\": [\n            {\"ref\": \"POK:539\", \"status\": \"partial\", \"note\": \"the Greek material is on IEW p.538, not 539: POK_02 leaf 196 has 'von ki-n-eu-: gr. κίνυμαι ... κῑνέω „setze in Bewegung, treibe“ (*κῑνεϝ-ω)' before the page number 539 appears in the running text. Correct in substance, one page off in the citation (the entry spans 538-539).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"WLD\", \"where\": \"Bd. I p. 361, s.v. qei-\", \"stance\": \"supports\", \"note\": \"'von qi-n-eu-: gr. κίνυμαι „werde bewegt, erschüttert, bewege mich, gehe“ ... κινέω „setze in Bewegung, treibe“ (dies wenigstens sehr wahrscheinlich für *κῑνεϝ-ιω)'.\"},\n            {\"src\": \"KLN\", \"where\": \"s.v. kinetic / cinematograph (KLN_1971.txt lines 131417, 47214)\", \"stance\": \"supports\", \"note\": \"'Gk. κινητικός „putting in motion“, fr. κινητός „moved“, verbal adj. of κῑνεῖν „to move“'; 'cinematograph ... fr. Gk. κίνημα, gen. κινήματος, „motion“'.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. kei-3\", \"stance\": \"supports\", \"note\": \"'2. Suffixed form *ki-neu- in Greek kinein, to move (> kinēsis, motion): KINEMATICS, -KINESIS, KINETIC; CINEMATOGRAPH ...'\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"French\",\n          \"words\": \"cinema\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"French cinéma is genuinely descended from Greek κίνημα, but not as a French word meaning 'motion' and not by inheritance: it is a clipping of cinématographe, a learned neo-Greek coinage (κίνημα, gen. κινήματος 'movement' + -γράφος 'writing') registered by Léon Bouly in 1892 and taken over by Auguste and Louis Lumière for their 1895 apparatus; the short form cinéma is in French use by the late 1890s and English borrows it in 1899 (Etymonline). Klein: 'cinema, n., a motion picture. — Short for cinematograph. cinematograph ... — Coined by the brothers Lumière in 1896 fr. Gk. κίνημα, gen. κινήματος, „motion“, and -γραφος, fr. γράφειν, „to write“.' So the arrow Greek → French is right, but (a) the intermediate cinématographe is missing from the chart and (b) the gloss 'motion' belongs to the Greek etymon, not to French cinéma, which has only ever meant 'the cinema, the pictures, a picture house'.\",\n          \"derivation_fa\": \"فرانسوی cinéma به‌راستی از یونانی κίνημα می‌آید، ولی نه از راه وراثت و نه به معنی «حرکت»: این واژه کوتاه‌شدهٔ cinématographe است، یک ساختِ نوساختهٔ عالمانه از κίνημα (اضافی κινήματος) «حرکت» + -γράφος «نگارنده»، که لئون بولی در ۱۸۹۲ ثبت کرد و برادران لومیر در ۱۸۹۵ برای دستگاه خود به کار بردند؛ صورت کوتاه cinéma از اواخر دههٔ ۱۸۹۰ در فرانسه رایج شد. پس پیکانِ یونانی ← فرانسوی درست است، اما حلقهٔ میانی (cinématographe) در نمودار نیامده و معنی «حرکت» از آنِ واژهٔ یونانی است نه واژهٔ فرانسوی که همواره به معنی «سینما، نمایش فیلم» بوده است. ادعای نورایی با احتیاط پذیرفتنی است.\",\n          \"sources\": [\"https://www.etymonline.com/word/cinema\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD:243\", \"status\": \"not_checked\", \"note\": \"AHD:243 is a page of the body of the American Heritage Dictionary, New College Edition 1975 (where the entry 'cinema' falls alphabetically); only the Watkins IE-roots appendix of that edition is available locally (AHD_watkins1985.txt), and the New College Edition scans on archive.org are lending-only. What IS checkable is Watkins s.v. kei-3, which lists CINEMATOGRAPH among the English derivatives of Greek kinein — consistent with the arrow.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"s.v. cinema, cinematograph (KLN_1971.txt lines 47211-47217)\", \"stance\": \"supports\", \"note\": \"'cinema, n., a motion picture. — Short for cinematograph. cinematograph, kinematograph. — Coined by the brothers Lumière in 1896 fr. Gk. κίνημα, gen. κινήματος, „motion“, and -γραφος, fr. γράφειν, „to write“.'\"},\n            {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls, s.v. cinema (FSD_vol1.txt line 66945)\", \"stance\": \"supports\", \"note\": \"'cin'e-ma, n. [Eng.] A motion-picture; picture-play. [Abbr. of cinematograph.]'\"}\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"Persian\",\n          \"words\": \"sînemâ «سینما»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Persian سینما sinemā is a straightforward twentieth-century loan from French cinéma, taken over with the rest of the vocabulary of the new medium (Mirza Ebrahim Khan Sahhafbashi opened the first public cinema in Tehran in 1904, and the French-schooled Iranian elite supplied the terminology). Phonetically French [sinema] is rendered with Persian ā for the final stressed -a, as regularly in French loans (تئاتر, کمدی, دیپلم); the initial س reflects French s-, and the spelling سینما with ی marks the long ī. Mo'in's dictionary tags it '[فر.]' (= French) and defines it 'ملخص سینماتوگراف' — 'abbreviation of cinématographe' — which is precisely Nourai's arrow French → Persian, with Mo'in independently noting the same clipping. Wiktionary: 'From French cinéma.'\",\n          \"derivation_fa\": \"«سینما» وام‌واژه‌ای است از فرانسوی cinéma که در آغاز سدهٔ بیستم همراه با خودِ این رسانه وارد فارسی شد (نخستین سینمای عمومی تهران را میرزا ابراهیم‌خان صحاف‌باشی در ۱۲۸۳ خورشیدی گشود) و اصطلاحات آن را فرانسه‌دانان ایرانی آوردند. از نظر آوایی، واکهٔ پایانی فرانسوی به «ا»ی کشیدهٔ فارسی بدل شده است، همان‌گونه که در دیگر وام‌واژه‌های فرانسوی (تئاتر، کمدی، دیپلم). معین در فرهنگ خود آن را با نشانِ «[فر.]» آورده و چنین تعریف کرده: «ملخص سینماتو‌گراف و آن نمایش مناظر و اشیاء و اشخاص به روی پردهٔ نمایش به وسیلهٔ دستگاه مخصوص است»؛ یعنی همان مسیری که نورایی رسم کرده و همان کوتاه‌شدگی از cinématographe. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%B3%DB%8C%D9%86%D9%85%D8%A7\",\n            \"https://abadis.ir/fatofa/%D8%B3%DB%8C%D9%86%D9%85%D8%A7/\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"MON:1985\", \"status\": \"supports\", \"note\": \"Mo'in's entry for سینما reads «(نِ) [ فر. ] (اِ.) ۱ - ملخص سینماتو‌گراف و آن نمایش مناظر و اشیاء و اشخاص به روی پردهٔ نمایش به وسیلهٔ دستگاه مخصوص است. ۲ - محل نمایش فیلم» — the [فر.] tag is exactly Nourai's French → Persian arrow. Verified through the full Mo'in text served by abadis.ir (archived); the printed page number 1985 itself could not be checked, since the online Mo'in carries no pagination and the archive.org copy is only a two-volume abridgement.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"Farhang-e Farsi s.v. سینما, via abadis.ir (فرهنگ معین section)\", \"stance\": \"supports\", \"note\": \"«[ فر. ] ... ملخص سینماتو‌گراف».\"},\n            {\"src\": \"WIKT\", \"where\": \"en.wiktionary.org/wiki/سینما\", \"stance\": \"supports\", \"note\": \"'Etymology: From French cinéma.' Pronunciations given: Iranian [siː.ne.mɒ́ː], Dari [siː.nä.mɑ́ː], Tajik [si.nä.mɔ́].\"}\n          ]\n        },\n        {\n          \"id\": 9,\n          \"lang\": \"English\",\n          \"words\": \"cinema\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English cinema 'a movie hall' is first recorded in 1899 as a borrowing of French cinéma; the fuller cinematograph had come in three years earlier (1896), and by 1914 cinema had widened to 'motion pictures collectively, as an art form'. It beat out the rival trade names vitascope (Edison, 1895) and animatograph (1898). Klein files it simply as 'Short for cinematograph', and Funk & Wagnalls marks the short form '[Eng.]', i.e. the British usage. The word is thus a sibling, not a parent, of Persian سینما — both are independent borrowings of the same French clipping, which is how Nourai draws it.\",\n          \"derivation_fa\": \"انگلیسی cinema نخستین بار در ۱۸۹۹ به معنی «سالن نمایش فیلم» ثبت شده و وام‌واژه‌ای است از فرانسوی cinéma؛ صورت بلندتر cinematograph سه سال پیش‌تر (۱۸۹۶) وارد انگلیسی شده بود و تا ۱۹۱۴ معنی «هنر سینما» نیز به آن افزوده شد. این واژه بر رقیبان خود، vitascope (ساختهٔ ادیسون، ۱۸۹۵) و animatograph (۱۸۹۸)، چیره شد. کلاین آن را کوتاه‌شدهٔ cinematograph می‌داند و فرهنگ فانک و واگنالز آن را با نشانِ «[Eng.]» یعنی کاربرد بریتانیایی آورده است. پس انگلیسی cinema و «سینما»ی فارسی هر دو مستقلاً از همان صورت کوتاه فرانسوی وام گرفته شده‌اند، دقیقاً همان‌گونه که نورایی رسم کرده است. ادعای نورایی درست است.\",\n          \"sources\": [\"https://www.etymonline.com/word/cinema\"],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the node carries no reference in the book; checked against Klein, Funk & Wagnalls and Etymonline instead.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"s.v. cinema (KLN_1971.txt line 47211)\", \"stance\": \"supports\", \"note\": \"'cinema, n., a motion picture. — Short for cinematograph.'\"},\n            {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls, s.v. cin'e-ma (FSD_vol1.txt line 66945)\", \"stance\": \"supports\", \"note\": \"'cin'e-ma ... n. [Eng.] A motion-picture; picture-play. [Abbr. of cinematograph.]'\"}\n          ]\n        },\n        {\n          \"id\": 10,\n          \"lang\": \"English\",\n          \"words\": \"kinetic\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English kinetic (1841, first of muscular motion, then from 1855 'causing motion', and in physics 'kinetic energy' from Thomson & Tait) is taken from Greek κινητικός 'putting in motion', the adjective of the verbal adjective κινητός 'moved', itself from κινεῖν. It reached English through the scientific Latin/French of the period rather than by any inherited route, so the arrow Greek → English is a learned borrowing. Klein: 'kinetic, adj. ... — Gk. κινητικός, „putting in motion“, fr. κινητός, „moved“, verbal adj. of κῑνεῖν, „to move“, which is rel. to κίειν, „to go“, and cogn. with L. ciere ... See cite and cp. cinema, cinerama, kinematics.'\",\n          \"derivation_fa\": \"انگلیسی kinetic (نخستین کاربرد ۱۸۴۱ دربارهٔ حرکت ماهیچه‌ای و از ۱۸۵۵ به معنی «حرکت‌زا»، و در فیزیک در ترکیب kinetic energy) از یونانی κινητικός «به‌حرکت‌درآورنده» گرفته شده که خود صفتِ κινητός «به حرکت درآمده» از فعل κινεῖν است. این واژه از راه لاتینِ علمی و فرانسویِ سدهٔ نوزدهم به انگلیسی رسیده، یعنی وام‌گیری عالمانه است نه وراثت. کلاین می‌نویسد: «kinetic از یونانی κινητικός، از κινητός، صفت فعلیِ κῑνεῖν „حرکت دادن“، که با κίειν „رفتن“ خویشاوند و با لاتینی ciere هم‌ریشه است». ادعای نورایی درست است.\",\n          \"sources\": [\"https://www.etymonline.com/word/kinetic\"],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"no reference given in the book for this node; checked against Klein, Watkins and Etymonline.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"s.v. kinetic (KLN_1971.txt line 131417)\", \"stance\": \"supports\", \"note\": \"'Gk. κινητικός, „putting in motion“, fr. κινητός, „moved“, verbal adj. of κῑνεῖν, „to move“, which is rel. to κίειν, „to go“, and cogn. with L. ciere, „to put in motion“, citare.'\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. kei-3\", \"stance\": \"supports\", \"note\": \"KINETIC is listed there among the English words from 'Greek kinein, to move'; the index line 'KINETIC kei-3' confirms it.\"}\n          ]\n        },\n        {\n          \"id\": 11,\n          \"lang\": \"Latin\",\n          \"words\": \"ciěre; citâre\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Latin cieō, ciēre (with a by-form ciō, cīre), perfect cīvī, ppp. citus, 'to set in motion, stir, summon, call'; from it the frequentative-intensive citō, citāre 'to put into quick motion, summon, cite'. Ernout-Meillet s.v. cieo describe the sense as 'mettre en mouvement; par suite: faire venir à soi, appeler ... exciter, provoquer' and note that the old simple verb faded early and was 'de bonne heure ... remplacé par le fréquentatif-intensif cito, -as'. Formally ciēre reflects *ki-eh₁- / *ki-eyo- beside the zero grade of the root; Pokorny 538 'lat. cieō, ciēre (sekundär ciō, cīre) „in Bewegung setzen, rege machen, herbeirufen“ (ciēre = idg. ki(i)ē-??), citus „schnell“, citō, -āre „in Bewegung setzen, kommen lassen, vorladen“, solli-citus, cunctus (*con-citos)'. Nourai's 'ciěre / citâre' with breve and circumflex are his own length marks; the Latin quantities are ciēre, citāre.\",\n          \"derivation_fa\": \"لاتینی cieō / مصدر ciēre (با صورت فرعی ciō, cīre)، ماضی cīvī و اسم مفعول citus، به معنی «به حرکت درآوردن، برانگیختن، فراخواندن»؛ و از آن فعل تکراری-تشدیدیِ citō, citāre «به شتاب به حرکت درآوردن، احضار کردن». ارنو و مییه در ذیل cieo معنی را «به حرکت درآوردن؛ و از آنجا: فراخواندن، برانگیختن» آورده‌اند و یادآور شده‌اند که فعل سادهٔ کهن زود از میان رفت و جای خود را به صورت تکراری cito داد. از نظر ساخت، ciēre بازتاب *ki-eh₁-/*ki-eyo- از صورت ضعیف ریشه است؛ پوکورنی در ص ۵۳۸ همین صورت‌ها را با solli-citus و cunctus (از *con-citos) می‌آورد. نشانه‌های کوتاهی و کشیدگی در «ciěre» و «citâre» شیوهٔ آوانگاری خودِ نورایی است؛ کمیّت درست ciēre و citāre است. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/cieo\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. kei-3: 'II. Zero-grade form *ki-. 1. Form *ki-eyo- in Latin ciēre (past participle citus), with its frequentative citāre, to set in motion, summon: CITE; EXCITE, INCITE, OSCITANCY, RESUSCITATE, SOLICITOUS.' Nourai's citation carries no page number, and this is the appendix entry it refers to.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"LAT\", \"where\": \"Ernout-Meillet, s.v. cieo (LAT.txt lines 11736-11825)\", \"stance\": \"supports\", \"note\": \"'cieo, -es, citum, ciere; cio, cis, ciui, citum, cire ... mettre en mouvement; par suite: 1° faire venir à soi, appeler, invoquer ... 3° exciter, provoquer'; and at the end 'Une forme à élargissement -u- joue un grand rôle: hom. ἔσσυτο ... et σεύω ... arm. cu „départ“ ... skr. cyavate „il se met en mouvement“, vieux perse asiyavam „je me suis mis en marche“' — i.e. Ernout-Meillet make the same connection between the Latin and the Iranian material that Nourai's chart assumes.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. I p. 361, s.v. qei-\", \"stance\": \"supports\", \"note\": \"'Lat. cio, cire und cieo, ciere „in Bewegung setzen, rege machen, wecken“ (ciere = idg. qi(i)ē-?), citus „(*in Bewegung gesetzt =) schnell“, cito, -are „in Bewegung setzen, kommen lassen, vorladen“, solli-citus.'\"},\n            {\"src\": \"KLN\", \"where\": \"s.v. cite (KLN_1971.txt line 47811)\", \"stance\": \"supports\", \"note\": \"'L. citare, „to put into quick motion, excite, provoke, call urgently“, freq. of ciere (pp. citus), „to set in motion“, fr. base *qi-, whence also Gk. κίειν, „to go“.'\"}\n          ]\n        },\n        {\n          \"id\": 12,\n          \"lang\": \"English\",\n          \"words\": \"citation, excite, solicit\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"All three are Latin-via-French borrowings on citāre / citus. CITATION: c.1300 in the sense 'summons', ME citacioun < Old French citation < Latin citātiōnem, acc. of citātiō, from citātus, ppp. of citāre; the sense 'passage quoted' follows the verb cite (1530s). EXCITE: mid-14c., ME exciten < Old French exciter < Latin excitāre 'call out, stir up, rouse', ex- 'out' + citāre. SOLICIT: ME soliciten < Middle/Modern French solliciter < Latin sollicitāre 'to stir, agitate, move, urge', denominative of sollicitus 'violently moved', literally 'wholly moved', a compound of sollus 'whole, entire' (cf. solemn) and citus, ppp. of ciēre — so the root sits in the second element. Klein and Skeat agree in every step (Skeat s.v. solicit: 'L. sollicitus, lit. wholly agitated ... citus, aroused, pp. of ciere, to shake, excite. See Solemn and Cite.').\",\n          \"derivation_fa\": \"هر سه واژه وام‌واژه‌های لاتینی‌اند که از راه فرانسوی به انگلیسی رسیده‌اند و همه بر پایهٔ citāre / citus ساخته شده‌اند. citation از حدود ۱۳۰۰ میلادی به معنی «احضاریه»، از فرانسوی کهن citation و آن از لاتینی citātiōnem (از citātus، اسم مفعولِ citāre)؛ معنی «نقل‌قول» پس از فعل cite در دههٔ ۱۵۳۰ پیدا شد. excite از میانهٔ سدهٔ چهاردهم، از فرانسوی کهن exciter و لاتینی excitāre («ex-» + citāre) «برانگیختن». solicit از فرانسوی solliciter و لاتینی sollicitāre، برگرفته از صفتِ sollicitus «به‌تمامی برانگیخته» که ترکیبی است از sollus «همه، تمام» (هم‌ریشه با solemn) و citus، اسم مفعول ciēre؛ یعنی ریشهٔ موردبحث در جزء دوم این ترکیب نشسته است. کلاین و اسکیت در همهٔ حلقه‌ها هم‌داستان‌اند. ادعای نورایی درست است.\",\n          \"sources\": [\"https://www.etymonline.com/word/cite\"],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"no reference given in the book for this node; checked against Klein, Skeat, Watkins and Etymonline.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"s.v. citation, cite, solicit (KLN_1971.txt lines 47804, 47811, 226000)\", \"stance\": \"supports\", \"note\": \"'citation ... fr. L. citationem, acc. of citatio, fr. citatus, pp. of citare'; 'cite ... F. citer, fr. L. citare ... freq. of ciere'; 'solicit ... fr. L. sollicitare „to stir, agitate, move, excite, urge“, fr. sollicitus, „violently moved“, lit. „wholly moved“, solli-citus being a compound of sollus, „whole, entire“, and citus, pp. of ciere.'\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat, s.v. solicit (SKT.txt line 17758)\", \"stance\": \"supports\", \"note\": \"'L. sollicitus, lit. wholly agitated. — L. solli-, for sollus, whole; citus, aroused, pp. of ciere, to shake, excite. See Solemn and Cite.'\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. kei-3 and index\", \"stance\": \"supports\", \"note\": \"'CITE; EXCITE, INCITE, OSCITANCY, RESUSCITATE, SOLICITOUS' listed under Latin ciēre/citāre; index line 'SOLICITOUS kei-3, sol-' confirms the double root of the compound.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\nJSONEOF\npython3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-248.json > /dev/null && echo \"JSON OK\""
}
```


### [2026-09-06T16:14:41.786Z] TOOL RESULT

```
JSON OK
```


## [2026-09-06T16:14:45.149Z] TOOL CALL #67: Bash

```json
{
 "command": "python3 tools/verify_check.py 248"
}
```


### [2026-09-06T16:14:47.003Z] TOOL RESULT

```
nodes verified: 12/12
node verdicts: {'plausible': 3, 'confirmed': 7, 'transcription_suspect': 1, 'unverified': 1}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 7, 'partial': 2, 'not_checked': 5}
books consulted: {'supports': 27, 'partial': 4, 'silent': 1} | by book: {'KLN': 6, 'CHEUNG': 4, 'WLD': 3, 'AHD': 3, 'BRT': 2, 'HUB': 2, 'MON': 2, 'FSD': 2, 'KNT': 1, 'PHD': 1, 'NYB': 1, 'HRN': 1, 'BOOK': 1, 'WIKT': 1, 'LAT': 1, 'SKT': 1}
```


## [2026-09-06T16:15:08.433Z] AGENT

Page 248 (book p. 218) verified — written to `/home/sfmqrb/git/rishe/data/verification/page-248.json`, `verify_check.py 248` reports 12/12 nodes, 0 PROBLEM lines.

**Counts** — root: 1 confirmed. Nodes: 7 confirmed, 3 plausible, 1 transcription_suspect, 1 unverified. Ref checks: 7 supports, 2 partial, 5 not_checked (4 of those are nodes with no refs in the book).

**Flagged items**
- `transcription_suspect` #4 Avestan **fra-šŭte**: not an attested Avestan form. Bartholomae (AiW 1715), Pokorny 539, Walde-Pokorny I 362 and Cheung (EDIV 41) all have the ppp. **fra-šūta-** (Vr 12.2) beside frašusaiti / impv. frašusa. The 600-dpi page render shows the book itself prints "fra-šŭte" → `error_in: book`, extraction faithful. The other three Avestan words (šav/šyav, šyaoθna, šyaoman) are confirmed verbatim from Pokorny 539.
- `plausible` #1 Old Persian **šaw**: no Old Persian *šaw is attested; šaw- is the MP/NP present stem (BMP ʿZLWN-, NP شو), and Horn's own cited p. 172 gives it as the New Persian present "šev-em". Nourai has pulled it up one stage; OP šiyav- itself is fine (Kent 211a, BRT 1715).
- `plausible` #2 Pahlavi **šutan "to become"**: form right (Nyberg's own transliteration), but MacKenzie and Nyberg gloss MP šudan/šutan only 'to go'; 'to become' is a New Persian development (Cheung: "NP šudan 'to become; [obs.] go'"). HRN:172 marked `partial` — Horn's entry 778 is headed by the NP infinitive and cites no Pahlavi form.
- `plausible` #7 French **cinema "motion"**: correct as descent from Gk κίνημα, but via the missing link cinématographe (Bouly 1892 / Lumière 1895); French cinéma never meant "motion".
- `unverified` #5: an **empty box printed in the book** itself (confirmed on the page image, copied to `sources/refs/ocr/BOOK/248.png`). Nothing lost in extraction.

**Cross-cutting caveat** recorded on the root: Pokorny 538-539, Walde-Pokorny I 361ff., Klein and Ernout-Meillet all lump the ki-eu- extension (Av./OP šyav-, Skt cyávate, Gk σεύω) with Gk κινέω / Lat. cieō, exactly as Nourai draws it; LIV², Beekes and Cheung split *ḱyew- from *keyh₁/₂-, so the Iranian half of this chart would not hang from this root today.

**No extraction errors found** — the JSON matches the printed page throughout (including the Persian script_extra «شو ، تاشو» and the blank node). Nourai's BQT:1261 and FFD:62 both check out word-for-word (Mo'in's footnote in Borhan p. 1261; Abolghasemi p. 62 «شد < فارسی میانه šud < ایرانی باستان *šu-ta»); MON:1985 verified in substance ([فر.] "ملخص سینماتوگراف") but the page number is unverifiable online; AHD:243 is a New College Edition body page, not available locally.
