# Verification process log — verify-page-269


## [2026-09-06T20:54:05.118Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 269 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-269.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-269.json. Write /home/sfmqrb/git/rishe/data/verification/page-269.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 269` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T20:54:06.619Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T20:54:07.353Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T20:54:07.371Z] TOOL RESULT

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


## [2026-09-06T20:54:07.527Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-269.txt"
}
```


### [2026-09-06T20:54:07.550Z] TOOL RESULT

```
1	=== PDF page 269 (book page 239) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Klei : to lean  (refs POK:600)
4	#1 (parent #0) [Avestan] refs=POK:600 | sray-, srinav-, srinu- : to lean ; srita, sray- : leaned
5	  #2 (parent #1) [None] refs=None | 
6	#3 (parent #0) [Greek] refs=POK:600 | klîma : sloping surface or land
7	  #4 (parent #3) [Arabic] refs=TAD:57 | eqlîm : a zone on earth, country
8	    #5 (parent #4) [Persian] refs=MON:326 | eqlîm «اقلیم» : country
9	  #6 (parent #3) [Latin] refs=AHD | clîma : a zone of earth
10	    #7 (parent #6) [English] refs=AHD | climate
11	#8 (parent #0) [Greek] refs=AHD:1523 | klině : bed ; klîmax : ladder
12	  #9 (parent #8) [French] refs=AHD | clinic
13	    #10 (parent #9) [Persian] refs=MON:3051 | kelînîk «کلینیک» : clinic
14	  #11 (parent #8) [English] refs=AHD | climax
15	#12 (parent #0) [Latin] refs=AHD:1523 | clîmâre : to lean, bend ; cliěns : dependent, client
16	  #13 (parent #12) [English] refs=AHD | decline, incline, recline ; client
17	#14 (parent #0) [Germanic] refs=AHD:1523 | hliněn : to lean ; hlaider : ladder ; hlid : that which bends over and covers, a lid
18	  #15 (parent #14) [English] refs=AHD | lean ; ladder ; lid
19	--- entry 1 ---
20	ROOT [Indo-European] Klem : tired, loose, dull  (refs POK:602)
21	#1 (parent #0) [Sanskrit] refs=POK:602 | sramana, saman : dull, a dull person who is not interested in anything but worshipping, a monk.
22	  #2 (parent #1) [Pahlavi] refs=TZF:77 | šaman : idol worshipper
23	    #3 (parent #2) [Persian] refs=BQT:1296; ETM:37; TZF:77 | šaman «شَمَن» : idol worshiper
24	
```


## [2026-09-06T20:54:10.604Z] TOOL CALL #3: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/data/extracted/batch/page-269.json",
 "description": "Read source JSON for page 269"
}
```


### [2026-09-06T20:54:10.644Z] TOOL RESULT

```
{
  "pdf_page": 269,
  "book_page": 239,
  "entries": [
    {
      "root": {
        "name": "Klei",
        "lang": "Indo-European",
        "refs": "POK:600",
        "gloss": "to lean"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:600",
          "words": [
            {"translit": "sray-, srinav-, srinu-", "gloss": "to lean", "script": null},
            {"translit": "srita, sray-", "gloss": "leaned", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": null,
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Greek",
          "refs": "POK:600",
          "words": [
            {"translit": "klîma", "gloss": "sloping surface or land", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Arabic",
          "refs": "TAD:57",
          "words": [
            {"translit": "eqlîm", "gloss": "a zone on earth, country", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Persian",
          "refs": "MON:326",
          "words": [
            {"translit": "eqlîm", "gloss": "country", "script": "اقلیم"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "تنت زورمندست و لشگر گران - ولیکن در اقلیم دشمن مران",
            "poet": "Sa`dî"
          }
        },
        {
          "id": 6,
          "parent": 3,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "clîma", "gloss": "a zone of earth", "script": null}
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
            {"translit": "climate", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD:1523",
          "words": [
            {"translit": "klině", "gloss": "bed", "script": null},
            {"translit": "klîmax", "gloss": "ladder", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "French",
          "refs": "AHD",
          "words": [
            {"translit": "clinic", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 9,
          "lang": "Persian",
          "refs": "MON:3051",
          "words": [
            {"translit": "kelînîk", "gloss": "clinic", "script": "کلینیک"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 8,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "climax", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD:1523",
          "words": [
            {"translit": "clîmâre", "gloss": "to lean, bend", "script": null},
            {"translit": "cliěns", "gloss": "dependent, client", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 12,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "decline, incline, recline", "gloss": null, "script": null},
            {"translit": "client", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 14,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD:1523",
          "words": [
            {"translit": "hliněn", "gloss": "to lean", "script": null},
            {"translit": "hlaider", "gloss": "ladder", "script": null},
            {"translit": "hlid", "gloss": "that which bends over and covers, a lid", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 15,
          "parent": 14,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "lean", "gloss": null, "script": null},
            {"translit": "ladder", "gloss": null, "script": null},
            {"translit": "lid", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Klem",
        "lang": "Indo-European",
        "refs": "POK:602",
        "gloss": "tired, loose, dull"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "POK:602",
          "words": [
            {"translit": "sramana, saman", "gloss": "dull, a dull person who is not interested in anything but worshipping, a monk.", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "TZF:77",
          "words": [
            {"translit": "šaman", "gloss": "idol worshipper", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "BQT:1296; ETM:37; TZF:77",
          "words": [
            {"translit": "šaman", "gloss": "idol worshiper", "script": "شَمَن"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "اگر تاج ایران سپارد به من - پرستش کنم چون بتان را شمن",
            "poet": "Ferdowsî"
          }
        }
      ]
    }
  ]
}
```


## [2026-09-06T20:54:10.945Z] TOOL CALL #4: Bash

```json
{
 "command": "sed -n 1,200p data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-06T20:54:11.081Z] TOOL RESULT

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
```


## [2026-09-06T20:54:15.022Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','AHD','TAD','TZF','ETM','BQT','MON']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:900])\n    print('---')\n\"",
 "description": "Check refs_online entries"
}
```


## [2026-09-06T20:54:17.082Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"ḱlei-\" POK_full.txt | head -20; echo \"=== search klei\"; grep -n \"^klei-\" POK_full.txt | head; echo \"=== klem\"; grep -n \"klem-\" POK_full.txt | head -20",
 "description": "Grep Pokorny for klei/klem"
}
```


### [2026-09-06T20:54:17.522Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry
---
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifier": "watkins-american-heritage-dictionary-of-indo-european-roots-1985", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt", "page_offset": "1985 Watkins ed.: lea
---
TAD {"title": "Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-hurufihi (2nd ed. Cairo 1932, ed. Yusuf Tuma al-Bustani; later Library of Lebanon reprint) — Nourai lists it under Arabic authors ('Unaysi T.'); its Table IV line was lost in the OCR", "kind": "archive_djvu", "url": "https://archive.org/details/TOB1932ARAR (1932 ed.); also https://archive.org/details/ar113lang79 and https://archive.org/details/elshandawily14640", "lookup_hint": "Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; inside.php search works.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD.txt"], "page_offset": "86 leaves (small book, ~80 printed pages); offset ≈ leaf − 4..6, verify against the printed numeral on the pa
---
TZF {"title": "Mohsen Abolghasemi, Tarikh-e Mokhtasar-e Zaban-e Farsi, Bonyad-e Andisheh-ye Eslami 1373/1994", "kind": "website", "url": "https://ketabnak.com/book/81646 (142 pp. PDF; login) ; https://farhangoadabeirani.blogsky.com/1395/07/20/post-1048/ (download post)", "lookup_hint": "Not on archive.org (only his دستور تاریخی زبان فارسی: archive.org/details/20220417_20220417_2237, and تاریخ زبان فارسی on samta.samt.ac.ir / library.tebyan.net/f/Viewer/Pdf/168187 which overlap in content).", "local_file": null, "page_offset": null, "covers_etymology": false, "notes": "PDF exists but not downloadable without login."}
---
ETM {"title": "Mohsen Abolghasemi, Risheh-shenasi (Etimoloji), Qoqnus 1374/1995", "kind": "catalog", "url": "https://ketabnak.com/book/107170/ (no download) ; https://ketab.ir/book/2ebb5f53-ba49-4955-98f4-d419919d0ebc ; purchase: https://adinehbook.com/gp/product/9643110451", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: not found.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: no digital copy on any permitted platform; catalogue/purchase only."}
---
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.c
---
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different paginati
---
```


### [2026-09-06T20:54:17.588Z] TOOL RESULT

```
=== search klei
=== klem
45026:bellows, roars, neighs ' {*klem-d-l\. Old English hiimman, h/ymman 'r\r\g, sound, clink, 
47419:Root / lemma: klem-, klem-, kleUi- 
47423:Note: (barely better as klem- : klam- must be assumed)
```


## [2026-09-06T20:54:22.201Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Root / lemma: k̂lei\" POK_full.txt | head; echo \"===\"; grep -n \"Root / lemma: k\" POK_full.txt | sed -n '1,400p' | grep -i \"lei\\|lem\" ",
 "description": "Find klei root lemma in Pokorny"
}
```


### [2026-09-06T20:54:22.265Z] TOOL RESULT

```
===
9334:Root / lemma: ken-2, kens-, keni-, kenu-\ "to rub, scrape off; ashes' must have come from 
31704:Root / lemma: g(e)u-lo- : glowing coals derivded from Root / lemma: ker(9)-3\ to burn 
43025:Root / lemma: kad^- 
43045:Root / lemma: kaghlo- 
43058:Root / lemma: kagh- : kogh- 
43100:Root / lemma: kago- or kogo-, -a- 
43138:Root / lemma: kai-ko- 
43168:Root / lemma: kaiR- or koiR- 
43205:Root / lemma: kai-lo- {kai-lu-) 
43240:Root / lemma: kais- 
43264:Root / lemma: kaito- 
43292:Root / lemma: kaiuf-t, kaiup-t 
43304:Root / lemma: kai2 
43320:Root / lemma: kakka- 
43342:Root / lemma: ka/-1 
43382:Root / lemma: kal-2, kali-, kalu- 
43403:Root / lemma: kalni- 
43419:Root / lemma: kamb- 
43424:Root / lemma: kam-er- 
43445:Root / lemma: kam-p- 
43495:Root / lemma: kand- skand-and (Old Indie) (s)kend-\ "to glow; bright, *moon' derived 
43531:Root / lemma: kan-tho- 
43567:Root / lemma: kan- 
43608:Root / lemma: kapro- 
43647:Root / lemma: kap-ut, -(e)lo- 
43693:Root / lemma: kap- 
43826:Root / lemma: kar-1 
43856:Root / lemma: kar-2, kara- 
43892:Root / lemma: kar-3, redupl. kartiar- 
43964:Root / lemma: kars- 
44004:Root / lemma: kat-1 
44033:Root / lemma: kat-2 
44054:Root / lemma: kau-/-, ku-l- 
44071:Root / lemma: kaus- 
44083:Root / lemma: kau- 
44109:Root / lemma: kad- 
44125:Root / lemma: kai-d-4, kai-t- 
44133:Root / lemma: kai-3, kf- 
44162:Root / lemma: kai-t- 
44168:Root / lemma: kak- 
44184:Root / lemma: ka/-3{kd/-7) 
44196:Root / lemma: kam- 
44204:Root / lemma: kapha- or Ropho- 
44211:Root / lemma: kapho-ox Ropho-: hoof, *claw, nail' derived from Root/ lemma: Reub- 
44222:Root / lemma: kapo- 
44234:Root / lemma: kap-, kap- 
44252:Root / lemma: kar- 
44274:Root / lemma: kau(a)la : kula 
44293:Root / lemma: kau- kau- 
44330:Root / lemma: kau- keu-, ku- 
44414:Root / lemma: ka- 
44460:Root / lemma: ka, ke, kom 
44482:Root / lemma: ked- 
44506:Root / lemma: keg- keng- and kek-, kenk- 
44557:Root / lemma: keid- 
44575:Root / lemma: keis- 
44587:Root / lemma: keku- 
44602:Root / lemma: keR- 
44616:Root / lemma: kelg- 
44630:Root / lemma: kel-1, kela- 
44697:Root / lemma: kel-2 
44745:Root / lemma: kel-3, kela-, A/a- extended klad- 
44927:Root / lemma: kel-5 
44963:Root / lemma: kel-6, k(e)le-, k(e)la-or 1(1-1 
45077:Root / lemma: kel-7{kol-, kj^ 
45105:Root / lemma: kel-7 
45113:Root / lemma: kelp-, l^lp- 
45133:Root / lemma: kemero- komero-, keinero- 
45157:Root / lemma: kema-, koma-, kma- {* hank-mhnos) 
45178:Root / lemma: kem-1 
45224:Root / lemma: kem-2 
45250:Root / lemma: keng-, kenk- 
45254:Root / lemma: kenk-1 
45286:Root / lemma: kenk-2 
45309:Root / lemma: kenk-3 
45331:Root / lemma: ken-1 
45431:Root / lemma: ken-2, kena-, keni-, kenu-; 
45687:Root / lemma: ken-3 
45722:Root / lemma: ken-4 
45748:Root / lemma: kenth(o)- 
45766:Root / lemma: kerd-1 
45792:Root / lemma: kerd-2 
45855:Root / lemma: ker(a)-3 
45913:Root / lemma: kerap-, krep- 
45988:Root / lemma: ker-1, kor-, kr-\ "a kind of sound (hoarse shrieking, etc.), *crane' derived 
46244:Root / lemma: ker-2 
46250:Root / lemma: ker-4 
46303:Root / lemma: ker-5 
46308:Root / lemma: kerm- 
46412:Root / lemma: kemo- 
46432:Root / lemma: kers- 
46462:Root / lemma: kert- kerat-, krat- {*kuers-t} 
46536:Root / lemma: kes- {*ghes-) 
46624:Root / lemma: keuad- kud- 
46660:Root / lemma: keu-1, skeu-, lengthened grade keu- 
46749:Root / lemma: keu-2, keua- 
47064:Root / lemma: kei- 
47147:Root / lemma: kel-, kol-, kal- 
47173:Root / lemma: ket- kot- 
47208:Root / lemma: kt^eO)- kt^aO)- {*ghde(i)-) 
47239:Root / lemma: kha khal 
47305:Root / lemma: kik- 
47325:Root / lemma: kista 
47337:Root / lemma: k/au- 
47351:Root / lemma: klafH^ra 
47363:Root / lemma: kla- 
47396:Root / lemma: kleiR- 
47419:Root / lemma: klem-, klem-, kleUi- 
47485:Root / lemma: kleno- 
47509:Root / lemma: klep- 
47526:Root / lemma: kleg-, klog- klag-, klang- kleg-, klog- kleig- kleik- 
47593:Root / lemma: klep- 
47677:Root / lemma: knei-g^h-, knei-b- 
47707:Root / lemma: kneug- 
47723:Root / lemma: knid-, Rnid-, sknid- 
47756:Root / lemma: ko ko, kak(k)-, ku(r)kur- 
47801:Root / lemma: kob- 
47828:Root / lemma: koi-lo- 
47844:Root / lemma: kois- 
47863:Root / lemma: koi-, kuT- 
47873:Root / lemma: koRsa {*hogha) 
47897:Root / lemma: kol(eli- 
47903:Root / lemma: kol(eli- : 'glue' derived from a reduction of the extended *glei-b'^- Root / 
47920:Root / lemma: kola- : klo- 
47939:Root / lemma: ko/i- 
47947:Root / lemma: kom 
48030:Root / lemma: konemo-, knamo-ox kenamo- 
48059:Root / lemma: kopso- 
48081:Root / lemma: koro-s, kono-s 
48112:Root / lemma: kos(e)lo- 
48137:Root / lemma: kost- 
48151:Root / lemma: krat- 
48157:Root / lemma: krafuj- : krau- : kru- 
48165:Root / lemma: krafu]-. krau-. kru-\ to heap up, put together; heap; roof, cottage, shed, 
48214:Root / lemma: kreb-5 
48220:Root / lemma: kred- 
48228:Root / lemma: kred- : beams, roof, derived from a suffixed Root / lemma: kra[u]- : kreu- : 
48260:Root / lemma: kreg-1 (and kerg-1) 
48273:Root / lemma: kreg-2 
48281:Root / lemma: krei-1 
48306:Root / lemma: krei-2, kreig-, kreik- 
48312:Root / lemma: krek-1 {-k-7) 
48341:Root / lemma: krek-2, kfk- 
48372:Root / lemma: krek-3 
48382:Root / lemma: krem- 
48390:Root / lemma: krep-1, kfp- 
48398:Root / lemma: krep-1, kfp- : body derived from -p- suffix of Root / lemma: (s)ker-4, (s)kera- 
48421:Root / lemma: krep-1, kfp- : body derived from -p- suffix of Root / lemma: (s)ker-4, (s)kere- 
48451:Root / lemma: krep-2 
48457:Root / lemma: kret-1 
48490:Root / lemma: kret-2 
48589:Root / lemma: kreu-2 
48615:Root / lemma: kreu-3, krou-s- 
48649:Root / lemma: kreu-4 
48657:Root / lemma: kreup- 
48692:Root / lemma: kreu-t- {kreu-d^-7) 
48713:Root / lemma: krek-4 : krok- 
48747:Root / lemma: krep-1 
48762:Root / lemma: krep-2 
48770:Root / lemma: kr(o)k-sko-, -u- 
48794:Root / lemma: krom- 
48816:Root / lemma: krut- 
48832:Root / lemma: kseip-, kseib- 
48850:Root / lemma: ks-en-, ks-es- ks-eu- 
48878:Root / lemma: kseud- {*gheud-) 
48907:Root / lemma: kuku 
48935:Root / lemma: ku-, kus- {*k"'uk"'h-) 
48970:Root / lemma: kuak- 
48989:Root / lemma: kuat(h)- 
49019:Root / lemma: kueiek- or kelak-, kolak- 
49051:Root / lemma: kuelp-2 
49079:Root / lemma: kuerp-, also kuerb- : to turn, wind, derived from a suffixed Root / lemma: 
49111:Root / lemma: kuet- : kuat- : kut- 
49140:Root / lemma: kuoi-, kuT- 
49157:Root / lemma: kures- kuers- kujrs- 
49185:Root / lemma: kjauo- kjeuo- 
49208:Root / lemma: kemer- 
49230:Root / lemma: kenako- 
51656:Root / lemma: konk- 
52439:Root / lemma: k''ei-1(t){*k''ehu-tj Note: common Proto Germanic -u- > -u-, -y-, -/-. 
52551:Root / lemma: k''ei-2{*k''ehu-) Note: common Proto Germanic -u- > -u-, -y-, -/-. 
52638:Root / lemma: k^'e-l {*k''ehu-) 
52782:Root / lemma: k''el-3{*k''ehul-) 
52862:Root / lemma: k''enth-{*k''ehuth-) 
52893:Root / lemma: k''er-1 {*k''ehur-) 
52937:Root / lemma: k''er-2{*k''ehur-) 
52959:Root / lemma: k''eru- {*k''ehur-) 
53158:Root / lemma: k^t^ei- 
53463:Root / lemma: k''rei-{*k''ehur-) Note: common Proto Germanic -u- > -u-, -y-, -/-. 
93753:Root / lemma: keleu-
```


## [2026-09-06T20:54:23.245Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '47410,47480p' POK_full.txt",
 "description": "Read klem- entry in Pokorny"
}
```


### [2026-09-06T20:54:23.297Z] TOOL RESULT

```
Church Slavic A/es/a "pliers', klestiti^ press ', Old Bulgarian si^-klestati sq^ torture, 
torment', russ. dial, klestftb (= klestftb) "press, clamp ' etc. 

References: WP. I 492, Trautmann 137. 
Page(s): 602 



Root / lemma: klem-, klem-, kleUi- 

Meaning: weak, ailing, feeble 

Note: (barely better as klem- : klam- must be assumed) 

Material: Old Indie offers on the one hand klamyati, klamati^ becomes tired, grows tired ', 

on the other hand sramyatT becomes tired, struggles, castigates oneself, sranta-^ 

fatigued, exhausted ', srama-m. ' fatigue, tiredness, exhaustion, feebleness '; sramana-' 

castigating, mendicant ' is to East Asiatic languages as Schamane " shaman, magician ' 

after they arrived to Europe (Indo Germanic change chain of events?; also the ambiguity of 

the liquid complicates the judgment; from kerm- "exhaust, get tired ' in any case, at least 

through the divided vowel position); 



gr. KAapapav rrAaSapav, aa0£vr| Hes.; 

Old Irish clam " leper, outcast, one who is rejected by society', cymr. acorn, claf. Middle 
Breton claff, nbret. klanv, klan^ sick '. 



References: WP. I 498. 
Page(s): 602-603 



Root/ lemma: kleng-a'c\6 klenk- 

Meaning: to bend, wind 

Material: 1. Latin dingo, -ere^ go around, surround, encompass, environ, gird, wreathe, 

crown ' (Paul, ex Festo 49 L., Glossen); 

Old Icelandic hlykkr^ curvature ', hlekkr^ x\x\<^ {*hlanki-, =) Old English hience ^\\rr\b, 
member or ring in a chain '; Old High German {ljjlanca'\r\\p, haunch' ('incurvation ' or ' 
place where one bends oneself). Middle High German lanke^ haunch, side, hip, flank ', 
Middle High German gelenke' bend', Modern High German gelenkSubst, ^e/e/7/r 'pliable', 
Middle High German lenken'bend', Modern High German lenkenlead', Old English hlanc 
' slim, thin' (actually 'pliable'), gehlencan l\ax, wattle, braid', also Old English /7///7C 'slope, 
hill'; Tocharian B kle/jke' fortification '; 

2. with auslaut. Tenuis: 

Balto Slavic *klenkid^ hobbles, limps ' in: Lithuanian klenktr go quickly, fast ', Latvian 
klenceV hobble, limp ', Old Church Slavic kl^cQ, kl^catl, kir. kljacu, kljacaty, Serbo- 
Croatian kleknem, kledr kneel ', sloven, kl^catr limp ', etc. 



References: WP. I 498 f., WH. I 233 f., Trautmann 136. 

See also: compare the rhyme roots /enk-'ben6', sleng-, slenk-^ coil, turn', skreng(h)-,
```


## [2026-09-06T20:54:29.574Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Page(s): 600\" POK_full.txt | head; echo \"=== 47340-47420\"; sed -n '47337,47425p' POK_full.txt",
 "description": "Read Pokorny page 600 root"
}
```


### [2026-09-06T20:54:29.654Z] TOOL RESULT

```
51393:Page(s): 600-602 
=== 47340-47420
Root / lemma: k/au- 

Meaning: to weep 

Note: only gr. and alb. 

Material: Gr. KAaiu) (Ionian), kAqu) (Attic) "cry, weep' (*KAaF-iu) : KAauao|jai, CKAauaa, 

Kkavioq and Kkavoioq): alb. k/anj, kanj, qaj^cvj, weep' ( *klaunjd). 

References: WP. I 490; compare 6. kel-. 

Page(s): 599 

Root / lemma: klafH^ra 

Meaning: alder 

Material: Gr. KAnGpa " alder, Betula ainus L.', Modern High German dial. (Zillertal) lutier, 

ludere, ludern {SchmeWer |2 1542) "Alpine alder, Betula nana L.'. 

References: WP. I 490. 

Page(s): 599 

Root / lemma: kla- 
Meaning: to heap up, to put 



Material: Lithuanian kloju, kloti^ hinbreiten, breit hinlegen ', Latvian klaju, k/at6s., 
Lithuanian klotas^ das Pflaster im Hofe ', uzklodas^ bedspread ', paklode^sheei, type of 
bed covering' {-d- from d- or d^-present as:) 



Old Bulgarian kladg, k/ast/"\oad, lay, place' (etc., in addition also russ. k/adu'cWp, cut '); 

/-present (partly perhaps also original /b-nouns) in Gothic afhlat^an "overburden ', Old 
Icelandic hiada. Old English Old Saxon hiadan. Old High German ^/ao'a/? (participle 
gihiatan) "stratify, layer, load'; Old Icelandic /7/ad"Pflaster im Hofe, pile, stack, heap'. Old 
English hlaedu. " Erdaufwurf, heap', hlseder dipper ', and full grade (compare Lithuanian 
klotas) nisi. /7/ddNom. PI. "stove, hearth' as well as Old English hlodi. "booty; bulk, mass, 
troop, multitude, crowd'. Old Franconian h/otha^ booty', Middle High German /uot, md. /ut 
"load, big, giant bulk, mass, gang'. 

-to-or -sto-, -5/iHioun to *hlal=>an\s Old Icelandic hiassu. "load, cargo', agst. hiaestu.. 
Old High German last, PI. lestii. "load'. 

Special position from Old English hlodi. " robbery, booty', hlodere^ robber' (: Old High 
German landeri^ a mercenary soldier'. Old Icelandic hlennT robber, thief, hlanna^rob', 
Germanic *hlant^-); (under the influence of common Celtic -ns-, -nt- > -nn-), then also 
Middle High German luot, md. lOt, which have not derived from *hlant^-, whose meaning 
"gang', is only for the Old English. 

References: WP. I 489, Trautmann 135 f. 
Page(s): 599 

Root / lemma: kleiR- 

Meaning: to press, squeeze 

Material: Old Indie A//s/7a//" afflicts, bothers ', klisyate' is tormented, suffers ', klesa-rw. 

"pain, affliction, complaint ', sam-k//s-^ squeeze'; 

Lithuanian kliset "crab's claws' (therefrom probably also /r//s5s "crooked-legged'), 
kleisiuoti^ run with crooked feet '; 

Slavic *k//sa and */r/es5 "pliers, scissors' (from Balto Slavic *k/e/s/a- and *k/a/s/a-) p\aced 
in poln. k//szawy and kir. *klfsavyj^ bowlegged'; besides r.-Church Slavic A/esca "pliers', 
sloven, klesce, kIr. kliscfi. PI. ds. (from Balto Slavic *klaistia-)\ 

Church Slavic A/es/a "pliers', klestiti^ press ', Old Bulgarian si^-klestati sq^ torture, 
torment', russ. dial, klestftb (= klestftb) "press, clamp ' etc. 

References: WP. I 492, Trautmann 137. 
Page(s): 602 



Root / lemma: klem-, klem-, kleUi- 

Meaning: weak, ailing, feeble 

Note: (barely better as klem- : klam- must be assumed) 

Material: Old Indie offers on the one hand klamyati, klamati^ becomes tired, grows tired ',
```


## [2026-09-06T20:54:33.694Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '51300,51400p' POK_full.txt",
 "description": "Read Pokorny pages 600-602 entry"
}
```


### [2026-09-06T20:54:33.750Z] TOOL RESULT

```
Note: only Armenian and gr. 

Material: Armenian siun = gr. kIwv " pillar '. 

References: W P. I 451. 

Page(s): 598 



Root / lemma: ^/ex- 
Meaning: to tip, incline, lean 

Material: Old Indie srayat/" leans, puts against ', srayate' leans, resides ', srita- = Avestan 
srita-{\ sray-) "leaned"; 

Avestan sray-, srinav-, sr/nu- '\ean' (compare gr. kAivioj); 

Armenian /earn, Gen. /e/7/7 "mountain' {*Rleitrno-'7'7); 

doubtful Armenian ///7//77 "become, originate, befall, be' (compare Old Indie srayate^be'); 

gr. K^vu), Lesbian kAIvvu) (*kATviu)) " make one thing slope against another, turn aside, 
make another recline, make subservient, inflect ' (Fut. kATvoo, Perf. KSKAipai), kAito^ 
"suitable', kAIoic; "tendency', KAiaia f. "cottage, tent', SikAISec; "double door', KAivri "bed', 
kAivthp, KAia|j6(; "couch, bed, place for resting ', kATtu(; (lies kA£itu(;, Herodian.) f. "slope, 
hill' (hellen. kATto(;, kKuoc, "hill'), KAipa n. " inclination, s/O/Oe of ground ', KATpia^f. "ladder'; 

Latin cITno, -are^ben6, bow, incline ' (previously to compounds neologism and thematic 
reshuffling a *l<If-na-mi), acclTnis^ leaning on, inclined to ', triclTnium' a couch for three 
persons reclining at meals, eating-couch, dinner-sofa, table-couch ', cliens, -tis^ a 
personal dependant, client ', clemens^mMe, gentle' {*RleJomenosl)\ cITtellae' a pack- 
saddle, sumpter-saddle ', diminutive of a *Rleitra= Umbrian l<letram^ a litter, bier, sedan, 
portable couch, palanquin, sofa, lounge ' (and Gothic fileit^rat "tent'); c//V^s"hiir (= Gothic 
filaiwu. "grave'), c//V/i/s "slant, skew = unlucky, of omen, sign'; 

Middle Irish cie, cymr. cledd, bret. I<leiz, corn, ciedh^ left, unlucky ' = "slant, skew' 
{*Rleios), Middle Irish fo-chia, cymr. go-gledd^v\orVc\'\ Middle Irish c/e/7 "leaning, tendency', 
wish' (: cymr. o'/c/7/k/7 "watchful, wakeful' from * dT-eRs-Riin-, Loth RC 42, 87 f.); 

Old Irish cidin, c/oe/7 "slant, skew, krummriJckig '; gallorom. *cleta^ hurdle ', Middle Irish 
cITatfi ^ cra{es\ cymr. c/wyd' hurdle, barrier', acorn. c/uifg\. " clita ', bret. RIoued-enn 
"grove, hedge ' {RIeito-, -ta)\ in addition acymr. clutam^ lump, mass together ', clut, ncymr. 
c/i/o'"heap' {*Rloi-ta)\ Middle Irish cletfieu. "roof beam, roof, zero grade cymr. cledr-en 
"rafter, lath, fence' {*Rli-tra= Middle Irish c/etiiar^ pad'), Middle Breton clezr-en, nbret. 



klerenn' main piece of tlie wicl<er rack ' (ablaut, witin Umbrian kletram, Latin clitellae, 
Gothic h/e/Pra and Old High German leitara); 

Old High German {hj//nen'\ean (intr.)', asachs. hlinon. Old English hiinian, hieonian 
( *hlinen) ds.; Old High German hiina ' the back of a couch ', Old English hiinbedd, hiinung 
" lair', Old High German hlina^ a lattice, enclosure, grating, grate, balustrade, bars, 
railings, bar in a court of justice '; Kaus. Old High German (h)leinen. Old English hlaenan 
"lean (tr.)'; Gothic hIaineQeu. PI. "the hill', nisi, hleinn^ rock ledge ', Norwegian dial, leini. 
" mound, hillside, slope' (: Latvian slains); Gothic h/a/w^ grave', Proto Norse hiaiwads.. Old 
High German Old Saxon /7/eo "burial mound, grave'. Old English h/aw^bur\a\ mound, 
gravestone ' (= Latin clfvus); Gothic hlijam. "tent, cottage'; Old High German (h)ITta, 
Modern High German Leite^ mountainside ', Old Icelandic hiidt "slope, mountainside ' 
(compare gr. kA£itu(;, Lithuanian slaTtas); Old Icelandic hiidi. "side'. Old English hITdu. " 
heap, mound, hill' (: KAiTO(;, Lithuanian slite); Gothic h/e/Pra^ cottage, tent' (see above to 
Latin cITtellae etc.); Old High German {h)/e/tara ladder'. Old English hlsec^djer ds.; Old 
English -hlTdan^ cover', hlidr\. "cover, door'. Old High German ///"cover' (Modern High 
German Augenlid), Old Icelandic hlid^door, GattertiJr', Gothic h/e/duma 'Wnker'; 

Lithuanian s//eju, s/ze/'/ (older zem. sleju= Old Indie srayati=) Latvian sleju, s/iet' lean ', 
in addition Lithuanian s/y//" lean, incline, verge ', su-slij§s^ be bending ', causative nu- 
slajinti^ turn over, overturn, capsize; keel over '; nouns: Latvian slejsru., slejai. "line'; Old 
Prussian s/ayann. " sledge skid ', Nom. PI. slayo^ sled ', Lithuanian slajos\. PI. ds.; at- 
slainis rr\. " wing, outhouse, outbuilding ', Latvian slains^ wo man einsinkt ', Lithuanian 
slaTtas rw. "slope', slynai. ' loam, clay ', at-slaTmasrw. "forecourt'; Latvian slitat "fence', 
Lithuanian zem. pa-slitas ^s\ar\t, skew' (= Old Indie srita-, gr. kAit6(;); Lithuanian slite, slitis 
f. " Garbenhocke ' (: gr. kAIok;), Old Lithuanian 5///e "ladder'; Lithuanian sleivas^ 
bowlegged' (compare Latin c//V^5 "slope'), ablaut. s//V/sm. "bowlegged person'; to the 
rhyme word Lithuanian kleTvas, klyvas^ bowlegged' see below (s)kel- ^ber\d'; different 
Specht Indo Germanic Dekl. 130, 31 7^; 

Slavic *slojb " layer ' {*kloJo-s) in sloven, s/oy" layer, lair ', russ. Czech s/ojds.; compare 
formal above Old Prussian s/ayann. " sledge skid '. 

About the extremely dubious affiliation from Old Bulgarian etc. k/etb " room, cell ' 
(Lithuanian k/et/s " granary, garner, barn ' is Slavic loanword) under assumption from West 
Indo Germanic Guttural s. Berneker 517 f. 

References: WP. I 490 ff., WH. I 231 f., 233, 234 f., 236, Wissmann Nom. postverb. 144 f., 
Trautmann 308 f.. Loth RC 42, 87 f., Vendryes RC 46, 261 ff. 



See also: extension from Rel-2^ incline '; s. also under (s)kel-bev\6\ 
Page(s): 600-602 

Root / lemma: Rlep- {sRlep-1) 

Meaning: to cover, conceal, steal 

Material: Gr. kAshtu) (*KA£ni(ji)) "steal' (KSKAocpa, SKAannv and SKAscpGnv), kKzuoc, n.,
```


## [2026-09-06T20:54:59.680Z] TOOL CALL #11: Bash

```json
{
 "command": "pdftoppm -f 269 -l 269 -r 300 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg269 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/",
 "description": "Render page 269 image"
}
```


## [2026-09-06T20:55:01.171Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD klei\"; grep -n -i \"klei-\" AHD_watkins1985.txt | head -20; echo \"=== AHD ladder/lid\"; grep -n \"hlaidri\\|hlinen\\|hlid-\" AHD_watkins1985.txt | head -20",
 "description": "Grep AHD Watkins for klei"
}
```


### [2026-09-06T20:55:02.758Z] TOOL RESULT

```
total 1816
drwx------ 2 sfmqrb sfmqrb   4096 Sep  6 16:55 .
drwx------ 4 sfmqrb sfmqrb   4096 Sep  6 16:32 ..
-rw-rw-r-- 1 sfmqrb sfmqrb    220 Sep  6 16:54 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 456331 Sep  6 16:54 bqt1594_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  64531 Sep  6 16:53 build261.py
-rw-rw-r-- 1 sfmqrb sfmqrb  95615 Sep  6 16:39 coord_pg262.png
-rw-rw-r-- 1 sfmqrb sfmqrb   4560 Sep  6 16:39 crop_ak2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   4014 Sep  6 16:39 crop_ak.png
-rw-rw-r-- 1 sfmqrb sfmqrb  25373 Sep  6 16:42 crop_alk.png
-rw-rw-r-- 1 sfmqrb sfmqrb   6411 Sep  6 16:39 crop_gr.png
-rw-rw-r-- 1 sfmqrb sfmqrb  23559 Sep  6 16:42 crop_kohul.png
-rw-rw-r-- 1 sfmqrb sfmqrb  59386 Sep  6 16:39 crop_lat2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   4761 Sep  6 16:39 crop_lat.png
-rw-rw-r-- 1 sfmqrb sfmqrb   3974 Sep  6 16:37 crop_me2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   3300 Sep  6 16:37 crop_me.png
-rw-rw-r-- 1 sfmqrb sfmqrb  10236 Sep  6 16:39 crop_op2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   4935 Sep  6 16:37 crop_op.png
-rw-rw-r-- 1 sfmqrb sfmqrb   5599 Sep  6 16:37 crop_pers.png
-rw-rw-r-- 1 sfmqrb sfmqrb    228 Sep  6 16:34 jscheck.js
-rw-rw-r-- 1 sfmqrb sfmqrb   1433 Sep  6 16:45 merge262.py
-rw-rw-r-- 1 sfmqrb sfmqrb  11601 Sep  6 16:42 p262-g01.json
-rw-rw-r-- 1 sfmqrb sfmqrb  10625 Sep  6 16:43 p262-g02.json
-rw-rw-r-- 1 sfmqrb sfmqrb  19393 Sep  6 16:46 p262-g03.json
-rw-rw-r-- 1 sfmqrb sfmqrb  19959 Sep  6 16:44 p262-g04.json
-rw-rw-r-- 1 sfmqrb sfmqrb  12063 Sep  6 16:43 p262-g05.json
-rw-rw-r-- 1 sfmqrb sfmqrb  12051 Sep  6 16:44 p262-g06.json
-rw-rw-r-- 1 sfmqrb sfmqrb  12737 Sep  6 16:44 p262-g07.json
-rw-rw-r-- 1 sfmqrb sfmqrb  17259 Sep  6 16:46 p262-g08.json
-rw-rw-r-- 1 sfmqrb sfmqrb  17820 Sep  6 16:53 p262-g09.json
-rw-rw-r-- 1 sfmqrb sfmqrb  17855 Sep  6 16:45 p262-g10.json
-rw-rw-r-- 1 sfmqrb sfmqrb  14983 Sep  6 16:44 p262-g11.json
-rw-rw-r-- 1 sfmqrb sfmqrb  25352 Sep  6 16:46 p262-g12.json
-rw-rw-r-- 1 sfmqrb sfmqrb  17745 Sep  6 16:44 p262-g13.json
-rw-rw-r-- 1 sfmqrb sfmqrb 105748 Sep  6 16:39 p263hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  66777 Sep  6 16:42 pg261.png
-rw-rw-r-- 1 sfmqrb sfmqrb  84660 Sep  6 16:39 pg262.png
-rw-rw-r-- 1 sfmqrb sfmqrb  71156 Sep  6 16:38 pg263.png
-rw-rw-r-- 1 sfmqrb sfmqrb  92930 Sep  6 16:37 pg264hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  57862 Sep  6 16:35 pg264.png
-rw-rw-r-- 1 sfmqrb sfmqrb  82276 Sep  6 16:46 pg265.png
-rw-rw-r-- 1 sfmqrb sfmqrb  79922 Sep  6 16:42 pg266.png
-rw-rw-r-- 1 sfmqrb sfmqrb  69592 Sep  6 16:52 pg268.png
-rw-rw-r-- 1 sfmqrb sfmqrb  71754 Sep  6 16:55 pg269.png
```


### [2026-09-06T20:55:02.825Z] TOOL RESULT

```
=== AHD klei
633:klei-. To lean. I. Full-grade form *klei-. 1. Suffixed form *klei-n- in Latin -clindre, to lean, bend: DECLINE, IN- CLINE, RECLINE. 2. Suffixed form *klei-tro- in Latin *clitra, litter, with diminutive clitellae, packsaddle: CLITELLUM. 3. Suffixed form *kiei-wo- in Latin clivus, a slope: ACCLIVITY, DECLIVITY, PROCLIVITY. II. Zero-grade
812:os-. Ash tree. Germanic “aski- in Old English zsc, ash: ASH?2. [Pok. 6s- 782.] 6s-. Mouth. 1. Latin ds (stem 6r-), mouth, face, orifice, and derivative dstium (< suffixed form *6s-to-), door: ORAL, OS!, OSCULATE, OSCULUM, OSTIARY, OSTIUM, USHER; INOSCULATE, ORIFICE, ORINASAL, OROTUND, OSCITANCY, PERORAL. 2. Possibly Latin auriga, chari- oteer (< *6r-ig-, “he who manages the (horse’s) bit”; -ig-, driving, from *ag-; see ag-): AURIGA. [Pok. 1. 6us- 784.] ost-. Bone. 1. Latin os (stem oss-), bone: 082, OSSEOUS, OSSICLE, OSSUARY; OSSIFRAGE, OSSIFY. 2. Greek osteon, bone: OSTEO-; ENDOSTEUM, EXOSTOSIS, PERIOSTEM, SYN- OSTOSIS, TELEOST. 3. Suffixed form *ost-r- in: a. Greek ostrakon, shell, potsherd: OSTRACIZE, OSTRACOD; b. Greek ostreon, oyster: OYSTER; C. variant form in Greek astragalos, vertebra, ball of the ankle joint, knuck- lebone, Ionic molding: ASTRAGAL, ASTRAGALUS. [Pok. ost(h)- 783.] ous-. Also aus-. Ear. 1. Suffixed form *ous-en- in Ger- manic *auzan- in Old English éare, ear: EAR}. 2. Suffixed form *aus-i- in Latin auris, ear: AURAL!, AURICLE; AURIFORM, ORMER. 3. Latin auscultdre, to listen to (*aus- + *kli-to-, inclined; see klei-): AUSCULTATION, scouT!. 4. Suffixed basic form *ous-os- in: a. Greek ous (stem 6t-), ear: OTIC, OTO-; MYOSOTIS, PAROTID GLAND; b. Greek Jagés, hare (< */ag-ous-, “with drooping ears”; *lag-, to droop; see slég-). [Pok. dus- 785.] owi-. Sheep. 1. Germanic *awi- in Old English ewe, eowu, ewe: EWE. 2. Latin ovis, sheep: OVINE; OVIBOS. [Pok. oui-s 784.] pa-. To protect, feed. Contracted from *pas-. 1. Suffixed form *pé-trom in Germanic *fodram in: a. Old English fédor, fodder: FODDER; b. Old French feurre, fodder: FORAGE; C. Old French forreure, trimming made from animal skin, fur (< “sheath, case, lining”): FuR. 2. Suf- fixed form *pd-dhlom (doublet of *pd-trom) in Latin padbulum, food, fodder: PABULUM. 3. Extended form *pat- in: a. Germanic *féd-, food, in Old English foda, food: Froop; b. Germanic denominative *fédjan, to give food to, in Old English fédan, to feed: FEED; Cc. suffixed form *pdt-tro- in Germanic *fdstra- in Old English fostor, food, nourishment: FOSTER. 4. Extended form *pds- in: a. suffixed form *pds-sko- in Latin pdscere, to feed: PASTURE; ANTIPASTO, PESTER, REPAST; b. Latin pdstor, shepherd: PASTOR; C. suffixed form *pds-t-ni- in Latin pGnis, bread (diminutive pastillus, medicine tablet): PANADA, PANATELA, PANNIER, PANOCHA, PANTRY, PAS- TILLE, (PENUCHE); APPANAGE, COMPANION, (COMPANY). 5. Suffixed form *pd-ti- in Iranian *pdti- in Persian pdd, protecting against: BEZOAR. 6. Suffixed form *pd-won-, protector, in Old Persian khshathra-pdvd, protector of the province: SATRAP. [Pok. pd- 787, 1. pd(i)- 839.] pag-. Also pak-. To fasten. 1. Lengthened-grade form *“pak- in Germanic *fogjan, to join, fit, in Old English fégan, to fit closely: FAY}. 2. Nasalized form *pa-n-g- in: a. Germanic *fangiz, seizure, in (i) Old English fang, feng, plunder, booty: FANG (ii) Dutch vangen, to catch: VANG; b. Latin pangere, to fasten: COMPACT!, IMPINGE. 3. Root form *pak- in: a. Latin pdx, peace (< “a binding together by treaty or agreement”): PACE?, PAY!, PEACE; APPEASE, PACIFIC, PACIFY; b. Latin pacisci, to agree: PACT. 4. Suf- fixed form *pak-sio- in: a. Latin pdlus, stake (fixed in the ground): PALE!, PALISADE, PEEL’, POLE?; IMPALE, TRA- VAIL, (TRAVEL); b. probably Latin pdla, spade: PALETTE, PEEL*. 5. Lengthened-grade form *pdg- in: a. Latin pdagus, “boundary staked out on the ground,” district, village, country: PAGAN, PEASANT; b. Latin pdgina, “trellis to which a row of vines is fixed,” hence (by metaphor) column of writing, page: PAGE?, PAGEANT; c. Latin prépdgés (pré-, before, in front; see per'), layer of vine, offspring (< “a fixing before”): PROPAGATE; d. Greek pégnunai, to fasten, coagulate: PECTIN, PEGMA- TITE. [Pok. pak- 787.] pan-. Fabric. 1. Germanic *fandn- in: a. Old English
1210:ACLINIC LINE klei- ACME ak-
1371:CLAY gel-1 CLAYMORE kel-1, mé-3 CLEAN gel-2 CLEANSE gel-2 CLEAR kele-2 CLEAT gel-1 CLEAVE! gleubh- CLEAVE? gel-! CLEAVERS gel-1 CLEF kleu-3 CLEISTOGAMOUS_ kleu-3 CLEISTOTHECIUM dhé-1, kleu-3 CLEMATIS kel-1 CLENCH gel-1 CLEPSYDRA klep-, wed-! CLERK kel-1 CLEVER gleubh- CLEVIS gleubh- CLEW! gel-1 CLIENT klei- CLIMATE klel- CLIMAX Klei- CLIMB gel-1 CLINAL klei- CLINANDRIUM klei- CLINCH gel-1 CLINE klel-
1373:CLINIC klei- CLINO- klei-
1375:CLIP? gel-1 CLITELLUM klei- CLoAcA kleu-2 cLop gel-1 CLOISONNE kleu-3 CLOISTER kleu-3 CLONE kel-1 CLONUS kel-3 CLOSE kleu-3 CLOSURE kleu-3 CLOT gel-1
1416:DECEIVE kap- DECEMBER dekm DECEMVIR dekm, wi-ro- DECENARY dekm DECENNIUM at-, dekm DECENT dek-! DECI- dekm DECIDE kae-id- DECIDUOUS _ kad- DECIMAL dekm DECIMATE dekm DECK! (s)teg- DECK? (s)teg- DECKLE (s)teg- DECLAIM kele-2 DECLARE kele-2 DECLINE klei- DECLIVITY kKlei- DECOCT pekw- DECOLLATE! kWwel-1 DECOLLETE kwel-1 DECOR dek-! DECORATE dek-1 DECOROUS dek-1 DECORTICATE sker-1 DECOY keue-2, to- DECREASE ker-3 DECREE krei- DECREPIT ker-2 DECREPITATE ker-2 DECUMBENT keu-2 DECUPLE dekm, pel-3 DECURRENT kers-2 DECUSSATE dekm DEDANS en DEDICATE deik- DEDUCE deuk- DEDUCT deuk- DEED dhé-1
1424:DEVANAGARI deiw- DEVASTATE eu-2 DEVEST wes-4 DEvi deiw- DEVIATE wegh- DEVIL gWele-! DEVIOUS wegh- DEVISE weidh- DEVOID eu-2 DEVOIR ghabh- DEVOLVE wel-3 DEVOTE weg¥h- DEVOUR gWera-4 DEVOUT weg*h- DEW dheu-2 DEXTER deks- DEXTERITY deks- DEXTRO- deks- DEXTRORSE_ wer-3 DHARMA dher-2 DI-!_ dwo- DIABASE gWa- DIABETES gWa- DIABOLIC gWela-1 DIACRITICAL krel- DIADEM dé- DIAGNOSIS gnd- DIAGONAL genu-! DIAGRAM gerbh- DIAL deiw- DIALECT leg-1 DIALOGUE leg-1 DIALYsIs_leu-1 DIAMETER mé-2 DIAMOND deme-2 Diana deiw- DIANTHUS andh- DIAPASON pant- DIAPAUSE paus- DIAPEDESIS ped-1 DIAPHANOUS bha-1 DIAPHORESIS bher-1 DIAPHRAGM bhrekw- DIAPHYsIS bheue- DIARRHEA sreu- DIARTHROSIS ar- DIARY deiw- Diaspora sper-4 DIASTASIS sta- DIASTOLE stel- DIASTROPHISM_streb(h)- DIATESSARON kWetwer- DIATHESIS dhé-1 DIATOM tem- DIATRIBE tere-1 DIAZO = gWei- DICAST deik- DICENTRA kent- DICHASIUM dwo- DICHO- dwo- DICHOTOMY tem- DICKER dekm DICLINOUS  klei- DICROTISM kret-2 DICTATE deik- DICTION deik- DICTUM deik- DIDACTIC dens-! DIDAPPER dub- DIDYMIUM dwo- DIDYMOUS dwo- DIE! dheu-3 DIE? dé-
1456:ENAMEL mel-1 ENAMOR amma ENANTIOMER §ant- ENANTIOMORPH ant- ENARTHROSIS at- ENATE gene- ENCAUSTIC kéu- ENCEINTE? kenk-1 ENCEPHALO- ghebh-el- ENCHANT kan- ENCHASE kap- ENCHIRIDION ghesor- ENCLAVE kleu-3 ENCLITIC klei- ENCOUNTER kom ENCROACH ger-2 ENCYCLICAL kwel-1 ENCYCLOPEDIA pau- END ant- ENDEAVOR ghabh- ENDEMIC da- ENDERGONIC werg- ENDOCARDIUM kerd-1 ENDOCRINE krei- ENDOERGIC werg- ENDORSE dorsum ENDOSTEUM ost- ENDOTHECIUM dhé-1 ENDOTHELIUM dhé@(i)- ENDOW do- ENDUE deuk-, eu-1 ENDURE deru ENEMA yé-
1676:INCIDENT kad- INCINERATE keni- INCIPIENT kap- INCISE kae-id- INCITE kei-3 INCLINE klei- INCLUDE kleu-3 INCONDITE dhé-1 INCREASE ker-3 INCUBATE keu-2 INCULT kWwel-1 INCUMBENT keu-2 INCUNABULUM kei-1 INCUR kers-2 INCUS kau-2 INDEMNIFY dap- INDEMNITY dap- INDENT! dent- INDENTURE dent- INDEX deik- INDICATE deik- INDICT deik- INDIGEN gene- INDIGENOUS gene- INDIGENT eg- INDIGN dek-1 INDIGNANT dek-1 INDIGNATION dek-1 INDITE deik- INDOLENT del-3 INDOMITABLE deme-2 INDUCE deuk- INDURATE deru INDUSTRY en, ster-2 INEBRIATE 6g¥h- INEFFABLE bha-2 INELUCTABLE leug-1 INEPT ap-1
1691:Is es- ISALLOBAR gWere-2 ISCHEMIA segh- ISINGLASS bhié-2 ISLAND akwa- ISOBAR gWere-2 ISOCLINE klei- ISOGLOss glogh- ISOHEL sawel- ISOHYET seue-2 ISOMER (S)mer-2 ISOMETRIC mé-2 ISOPIESTIC sed-1 ISOPLETH pele-1 ISOSCELES skel-3 IsosTasy sta- ISSUE ei-1
1726:LAAGER legh- LABEL leb-! LABELLUM leb-2 LABIAL leb-2 LABILE leb-1 LABIUM leb-2 LABOR leb-1 LABRET leb-2 LABRUM leb-2 Lac! reg-3 LACCOLITH laku- LACERATE |@k- LACHRYMAL dakru- LACINIATE l@k- LACK leg-2 LACROSSE ger-2 LACTATE melg- LACTEAL melg- LACTESCENT melg- LACTO- melg- LADDER Klei- LADE kla-
1739:LEAGUER! legh- LEAK leg-2 LEAN! klei- LEAP klou- LEARN leis-1 LEASING leu-! LEAST leis-2 LEATHER letro- LEAVE! leip- LEAVE? §leubh- LEAVEN legWh- LECHER leigh- LECTERN leg-1 LECTION leg-1 LECTURE leg-' LEDGE legh- LEDGER legh- LEE kele-1 LEECH! feg-1 LEECH? leig-1 LEEK leug-! LEER kleu-! LEES legh- LEGACY leg-1 LEGAL leg-1 LEGATE leg-1 LEGATO leig-1 LEGEND leg-1 LEGERDEMAIN leg¥h- LEGIBLE leg-1 LEGION leg-1 LEGISLATOR leg-1, tele- LEGIST leg-1 LEGITIMATE leg-1 LEITMOTIF leit-2 LEMAN leubh- LEMMA! (s)lag¥- LEMMA? lep-t LEMURES_ lem-2 LEND leikw- LENGTH del-1 LENIENT [6-2 LENIS [6-2 LENITIVE |@-2 LENITY 16-2 LENT del-1 LENTO lento-, lep-1. LEPIDO- lep-1 LEPIDOTE lep-1 LEPRECHAUN kWrep-, legwh- -LEPSY (s)lag¥- LEPTO- lep-1 LEPTON! lep-1
1742:LICH GATE [k- Lick leigh- LICORICE dik-u-, wrad- LID. klei-
1882:MOLTO mel-4 MOLY md6(u)lo- MOLYBDENUM plumbum MOMENT meue- MOMENTOUS meue- MOMENTUM meue- MONAD men-4 MONANTHOUS = andh- MONASTERY men-4 MONAXON aks- MonpDay mé-2 MONEY men-! MONGER meng- MONGREL mag- MONILIFORM mon- MONISH men-1 MONITION men-1 MONITOR men-1 MONK men-4 MONO- men-4 MONOCLE oOkw- MONOCLINIC klei- MONOCLINOUS klei- MONOCOQUE kokkos MONODY wed-2 MONOECIOUS weik-! MONOMER (s)mer-2 MOoNOPHYSITE bheue- MONOPODIUM ped-1 MONOPOLY pel-5 MONOTREME tere-1 MONS men-2 MONSTER men-1 MONTAGNARD men-2 MONTANE men-2 MONTE men-2 MONTH mé-2 MONTICULE men-2 MONUMENT men-! MOOCH meug-! MOOD! mé-1 MOOD? med- MOON mé-2
2065:Pass pete- PASSIBLE pé@{(i)- PASSIM pete- PASSION pé@{i)- PASSIVE pé@(i)- PASTILLE pa- PASTOR pa- PASTURE pa- PATEN pete- PATENT pete- PATER peter- PATERNAL peter- PATERNOSTER nes-2 PATH pent- PATHETIC kWent(h)- PATHO- kWent(h)- PATHOGNOMIC gné- PATHOGNOMONIC kWent(h)- PATHOS kWent(h)- -PATHY kWent(h)- PATIENT pé@(i)- PATINA! pete- PATINA? pete- PATRI- peter- PATRIARCH peter- PATRICIAN peter- PATRICLINOUS _ klei- PATRIMONY peter- PATRIOT peter- PATRON peter- _ PATRONYMIC nO-men- PATULOUS  pete- PAUCITY pau- PAUPER pau- PAUSE paus- PAVE peu-
2079:PER- pert PERCEIVE kap- PERCENT dekm PERCH? perk-1 PERCOLATE kagh- PERCURRENT kers-2 PERCUSS kwét- PERDITION d6- PERDURABLE deue- PEREGRINE agro- PEREMPTORY em- PERENNIAL at- PERFECT dhé-1 PERFIDY bheidh- PERFORATE bher-2 PERFUME dheu-1 PERFUNCTORY bheug-2 PERFUSE gheu- PERGOLA perg- PERI- per! PERICARDIUM kerd-1 PERICLINE Klei- PERIGEE gé PERIHELION sawel- PERIL per-4 PERIMYSIUM mis- PERINEPHRIUM negWh-ro- PERIOD sed-2 PERIONYCHIUM nogh- PERIOSTEM ost- PERIPATETIC pent- PERIPETEIA pet- PERIPHERY bher-1 PERIPHRASIS gWhren- PERIPHYTON bheue- PERIPTERAL pet- PERISARC  twerk- PERISH ei-1 PERISSODACTYL per! PERISTALSIS | stel- PERISTYLE sta- PERITHECIUM dhé-1 PERITONEUM ten- PERITRICH _ thrix PERIWINKLE! weng- PERJURE yewes- PERMANENT men-3 PERMEATE mei-1 PERMIT (s)meit(a)- PERMUTE mei-1 PERNICIOUS nek-1 PERONEAL per-2 PERORAL 6s- PERORATE 6r- PERPEND (S)pen- PERPENDICULAR (S)pen- PERPETRATE peter- PERPETUAL pet- PERPLEX plek-
2136:PRO-2 per? PROBABLE per! PROBE pert PROBITY per! PROBLEM gWele-1 PROBOSCIS g¥6- PROCEED ked- PROCLAIM kele-2 PROcLITIC § klei- PROCLIVITY klei- PROCREATE ker-3 PROCTITIS prdkto- PROCTOLOGY prdkto- PROCTOR cura PROCTOSCOPE prdkto- PROCUMBENT keu-2 PROCURATOR cura PROCURE cura PROCYON kwon- PRODIGAL ag- PRODIGY ég- PRODROME der-1 PRODUCE deuk- PROFANE dhés- PROFESS bha-2 PROFESSOR reg-! PROFFER bher-1 PROFICIENT dhé-1 PROFILE gWhi- PROFIT dhé-1 PROFLIGATE bhiig- PROFOUND bhudh- PROFUSE gheu- PROGENITOR gene- PROGENY gene- PROGLOTTID glégh- PROGNOSIS gnd- PROGRAM gerbh- PROGRESS ghredh- PROHIBIT ghabh- PROJECT yée- PROLAN al-3 PROLAPSE leb-1 PROLATE tele- PROLEGOMENON leg-! PROLEPSIS (s)lag¥- PROLETARIAN al-3 PROLIFEROUS _al-3 PROLIFIC al-3 PROLIX wleik- PROLOCUTOR tolkw- PROLOGUE leg-1 PROLONG del-1 PROLUSION leid- PROMENADE men-2 PROMINENT men-2 PROMISCUOUS meik- PROMISE (s)meit(e)- PROMOTE meue- PROMPT em- PRONE per! PRONEPHROS _ negwh-ro- PRONOUN no-men- PRONOUNCE neu-! PROOF per! PROPAGATE pag- PROPEL pel-6 PROPEND (8)pen- PROPER pert PROPERTY per? PROPHET bha-2 PROPHYLACTIC phulax PROPINQUITY per? PROPIONIC ACID peie- PROPITIOUS pet- PROPOLIS pele-3 PROPORTION pere-2 PROPOSE apo- PROPRIOCEPTION per! PROPRIOCEPTOR per? PROPTOSIS pet- PROPYLAEUM pulé PROPYLON pulé PROROGUE reg-1 PROS- pert PROSCRIBE skribh- PROSE wer-3 PROSECUTE sekw-1 PROSELYTE leudh-1 PROSOMA teue- PROSOPOPEIA kWwel-2, per! PROSPECT spek- PROSPER spé-1 PROSTATE sta- PROSTHESIS dhé-1 PROSTITUTE sta- PROSTOMIUM ste-men-
2174:REBUT bhau- RECALESCENCE kele-! RECANT kan- RECAPITULATE kaput RECEDE ked- RECEIVE kap- RECENSION kens- RECENT ken-3 RECIDIVISM kad- RECIPROCAL pert RECISION kae-id- RECK reg-1 RECKLESS reg-! RECKON reg-1 RECLAIM kele-2 RECLINE klei- RECLUSE kleu-3 RECOGNIZE gnd- RECOIL (s)keu- RECOMMEND man-2 RECONDITE dhé-1 RECORD kerd-1 RECOURSE kers-2 RECOVER kap- RECREANT kerd-1 RECREMENT krei- RECRIMINATE  krei- RECRUDESCE kreud-! RECRUIT ker-3 RECTANGLE reg-1 RECTIFY dhé-1, reg-1 RECTILINEAR reg-1 RECTITUDE reg-!
2333:SYNARTHROSIS ar- SYNCLINAL klei- SYNCOPE skep- SYNDESMOSIS dé- SYNDETIC dé- SYNDIC deik- SYNECDOCHE dek-', eghs SYNERGID werg- SYNERGISM werg- SYNESIS yé- SYNIZESIS sed-1 SYNKARYON kar-! SYNOD sed-2 SYNONYMOUS nd-men- SYNOPSIS OkW- SYNOSTOSIS ost- SYNTAX tag- SYRINGOMYELIA mis- SYSSARCOSIS twerk- SYSTALTIC stel- SYSTEM sta-
=== AHD ladder/lid
635:form *kli-. 1. Germanic *hlid-, “that which bends over,” cover, in Old English Alid, cover: Lip. 2. Suffixed form *kli-n- in Germanic *hlinén, in Old English Alinian and hleonian, to lean: LEAN! 3. Suffixed form “*kli-ent- in Latin cliéns, dependent, follower: CLIENT. 4. Suffixed form *kli-to- in Latin *aus-klit-d- in auscultare, “to hold one’s ear inclined,” to listen to (see ous-). 5. Suffixed form *kli-n-yo- in Greek klinein, to lean: CLINAL, CLINE, -CLINIC, CLINO-; (ACLINIC LINE), CLINANDRIUM, ENCLIT- IC, (ISOCLINE), MATRICLINOUS, (MONOCLINIC), PAT- RICLINOUS, PERICLINE, PROCLITIC, SYNCLINAL. 6. Greek lengthened form *&ii- in: a. suffixed form *kli-n-d in Greek kliné, bed: CLINIC; DICLINOUS, MONOCLINOUS, TRICLINIUM; b. suffixed form *kii-m- in Greek klimax, ladder: CLIMAX; C. suffixed form *kli-mn in Greek klima, sloping surface of the earth: cLimaTE. III. Suffixed o-grade form *kloi-tr- in Germanic *hiaidr- in Old Eng- lish hléd(der, ladder: LADDER. [Pok. Rlei- 600.]
```


## [2026-09-06T20:55:11.150Z] TOOL CALL #13: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg269.png"
}
```


### [2026-09-06T20:55:11.650Z] TOOL RESULT

```

```


## [2026-09-06T20:55:11.647Z] INPUT

[Image: original 2550x3300, displayed at 1546x2000. Multiply coordinates by 1.65 to map to original image.]


## [2026-09-06T20:55:22.457Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg269.png')\nprint(im.size)\n# Latin box approx y 1330-1470 orig? displayed 820-890 => *1.65 => 1353-1470; x 600-980 => 990-1617\nc=im.crop((580,1350,1000,1480)).resize((1680,520))\nc.save('crop_latin269.png')\nc2=im.crop((580,1490,1250,1680)).resize((2010,570))\nc2.save('crop_germ269.png')\n\"",
 "description": "Crop Latin and Germanic boxes"
}
```


### [2026-09-06T20:55:24.722Z] TOOL RESULT

```
(2550, 3300)
```


## [2026-09-06T20:55:26.994Z] TOOL CALL #15: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/crop_latin269.png"
}
```


### [2026-09-06T20:55:27.015Z] TOOL RESULT

```

```


## [2026-09-06T20:55:38.572Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== TAD iqlim\"; grep -n \"اقليم\\|إقليم\\|أقليم\" TAD_pages.txt | head -20; echo \"=== TAD leaf tags near\"; grep -n \"pdf page\" TAD_pages.txt | head -5",
 "description": "Grep TAD for iqlim"
}
```


### [2026-09-06T20:55:38.632Z] TOOL RESULT

```
=== TAD iqlim
=== TAD leaf tags near
```


## [2026-09-06T20:55:39.514Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT sray\"; grep -n \"srayaiti\\|sray\\b\\|srinav\\|srinu\" BRT.txt | head -30",
 "description": "Grep Bartholomae for sray"
}
```


### [2026-09-06T20:55:39.566Z] TOOL RESULT

```
=== BRT sray
3508:•  j.  apa-j-zära-  m.  'Abfluss,  {Wasser)ab- zwejgung'  a)  des  VouruAasa:  srayä  vouru.- kasaya  .  .  yeäke  . .  Aazannm  -ranam  . . kasal  aSsqm  °ranqm  c(&war>.sat»m  ayan.- baranqm..*arihas(a  me  *afi:aAka  Spö 'rö *vt)asaiti  vispJis  aoi  karsvqn  Y.  65.  4  £; —  aija  käu  'rö  bvat  zrayanAs  vouru.- kaiahe  vairil  yH  Aaosravä  nqma  Yt  ig. 56;  —  zrayauhs  vouru.kasahe  ,  .  vTspJ rairi/  a^araiti  vlsp}sca..nimraoi!  vlspSsca srlr!  'äire (AP.)'> \i.8.i,f>;~ katiht kaüht •,lire(XS.)  Ytj.ioi.  b)  der  Ratfka:\ tipa  guoim  'r>m  ra»hayh  Yt/5. 27,  j
3629:•  j.  apa-srayamna-  Adj..,  PPM.:  s.  sray-. m  j.  apa-za<)ah-  Adj.  (auch  fem.)  'den Steiss  ab-,  weghaltend  (nach  oben?)''*, von  der  Fliege:  ^maxsiJiihrpa  prrfaitya frasnaol  °Sawi4ff(GSf.))  * akaramm.driwya (sd.)  V.7.2.
7958:—  II  dahyäv^  'mä  tyä  hami^^iyä  abav^ .. Bh.^4.  b)  substantivisch:  II  ^«na*  lyJ" .  .  akunavam  valnä  ef'ur^mazdakt^  .  . akunavam  Bh.  4.  6,  12;  2;  —  -matn  (ASn) tya^  aiuna  AjB.4i?);  i — yaha'matyalU frävaoHm  Yt/7.  22;  —  zugleich  zurück- weisend: zac'ira  .  .  "ma  .  .  y>i  .  .  pasca vazitili  Yt.5. 94f.  4)  auf  einen  Satz rcÄX  yäha  oder  yat,  substantivisch:  "mat varths  "mal  srayö  yaia  tarn  .  .  valartlu V.5.  21;  —  'mat  .  .  stil7i!t?m  ^yao^mm maiya  v»r»zinli  . .  yai  kainyS  usväuayäiiü YL  i-j.  59;  —  in  Kongruenz  mit  dem Praedikat:    'mint  'iwqm  tuirlm  ySn»m  .  .
8578:Pü. ;  undeutlich.  —  ■)  S.  zu  vsaia-. j.  usrärayä  Vyt.  4t\  s.  sray-.
9251:srayä  voumkaiaya  Y,  65. 4;  —  ys  haaiay-j  S/-'^v^'^'jU^'ond''zD"'"w',/irLter ...va  uruassayat  '«o»  Yt,5.  131;  —  ^-i  HriÄ^-^  No^T).  -  mp,  fl'ü.  Tu  V.'s  49" rasmanS  hqm.ststse  (sd.)  ^5  ^'na  ">  J'  karkäi,  vgl.  np.  (Npa,)  kargas. iHndayänti  Yt,  jj.  39;  —  yaoz)nH  »aA'«j.*kahrkäs5.parana-"  Adj. 'mit  Federn •«ff  (NP.)'>  rasmans  Ytio.36.  2)  zeitlich  ^  des  (Vogels)  Kakrklsa  versehen':  isunqm (nur  Komp.).  ^-paranum'^  Yt/o.isg.
12871:p.  daray' :  lies  dray',  i.  unter  sray,
14499:•  p,  9''ay-  V.:  s.  unter  sray-.
15856:•  j.,  g.  pasav-  -.ßav-  m.  'Vieh,  domestizirtes vierfüssigcs  Tier,  Haustier',  Sing,  auch  kolL : azsm  .  .  tJ  nipayanl .  .  ya^a  'sßm  pasa.- vastr?m  (sd.)  Vtj.  89;  —  ki  mH  'sSui ^ mS  nä  >rat3  vists  .  .  axdä  (sd.)  .  .  Y. 50.1;  — /su  F.5(?)";  —  im  Gegensatz 2U  nar-  oder  vira-:  'svamca  naramca  Y. 4-  S  i  —  y^  "^J  'P^  •  ■  °fli»t  vä  narim vä  raiiyät  W. 13.^1;  32;  —  västryehys •sSui  vTräatiä  (sd.)  Y.  JJ.  1 5 ;  —  va/  virpt^ ahmäksng  frada^ai  (sd.)  J  Y.  4:5.  9;  — pairT  'sUs  pain  vlrSng  dadtmahl  Y.  JÄ 6.  a)  in  Dual  Verbindung  mit  vJra-  (sd., audi  fdSt):  -j*  vlra  *Yt.  y.  iz  usw.;  — 'Tirä  Wrayi  Vr.7.3usw,;  —  'subya  vTraäbya V.6.^2.  A)  insbes.  vom  Kleinvieh,  den Schafen  und  Ziegen,  im  Gegensatz  zu staora-  (sdj:  -svamca  staoranameä  masyl- nqmca  sünqmla  vayqmca  V.  2.8;  10,  Äiz, 13;  —  °vasca  (als  NP.)  staoräea . .  masyäca bmngra  Yt.5.89;  Äs,  V.2.8,  9,  11,5.5, 6,  15;  —  °sv5  (AP.)  staeräca  V.  p.  39=;  — •subya  staoralibya  vayafibya  patantaäbya (sd,)  YL  /o.  119;  —  's}ul*g?ribui  ysistahe (sd.)  A.J.  3;  — -pania-dasa  °svs  sraoni.masa F. 25b(?); —  *hvBiSa^a{&A.)  'sus./iva^'> N.  5>V;  —  mit  anumaya-  (sd.):  ustrahe  . . aspahe  .  .  gSuI .  .  mtfnumat  ap?r3näyBk»in yaoida^S  °sSul  ^g^nbus  anumayeke  V.  9. 38 ; 2.  24;  —  bis  hapta  "vö  (AP.)  anumaya  . . fiissrinuyäi  V,  i4- 16.  a)  spez.  als  Opfer- tier: zadhrä  hE ushärayfti .,'sum  hl pacaym
16639:ava^a  hl  ^^ato  (sd.)  puhnm  atskat  aOiS 'ytm  haca  avantanqm  nisrinuyät  äat  yezi Avant  näirika  bavaiti(%A^  alu§ 'y>m  paiti nidanäiti  yezt  du-j'irqm  (sd.)  fanü  tialm>m •y>m  frajasät  Vd,2  (der  Sinn  ist:  Frau und  Söhne  des  Erblassers  sollen  aus  der Erbschaft  den  gleichen  Teil,  die  Töchter die  Hälfte  davon  bekommen);  —  ytmasät ys  matyfng  cixinusS  akmakSng  gaus  -gä (APn.)  «"JwMWii  (sd.)  V.  J2.  8;  ~  'ya Y.16^''.  a)  bes.  'günstiges  Los,  Glück': yazäi  *apqmca  'y»mca  YL  /j.  i.  o)  bes.  1 vom  Glück  in  der  Ehe,  'Eheglück'  (nur Komp.)'*.         [Yt/6".  15:  lies  voku.b'.\
16848:tutssvö  aitavat  apat  kaca  mibsray?n  "man    19.  3)  'heimtragen,  einheimsen':  vlips
19091:•  j.  nanhaidya-  m.  Name  emes  /?aÄa*':  ein' (nur  Komp.),  a)  Praev.  (mit 'ar-,  a*-, ifidrfm  ..  saurum  ..  '^im  daeum  V.JO.9;  gam-,  ää;pais;  vas-,  sray-  usw.).  Ohne —   dafvanam    dagvd  indrS  .  .  *sauru  .  .[Wert:  «J3  VyLjl^''.
27305:•  j.  sray-,  p.  ^'ay-  V,  'lehnen'.  Fraes. I  sray- :  srl-,  z  sraya-,  7  sr3ray-^\  %''äray''> IQ  srinav;  siriaav-'*:srinu;  sirinv-'^;  Perf. I  s-tsray-{i)i\  —  PPfP.  srHa-,
27333:•  j.  srayana-  Adj.,  PP\L:  s.  sray
27423:•  j.  srita-  Adj.,  PPfP.:  s.  sray-. KompE.
27424:•  j.  sritay-  f  'Lehnen  (usw.)'. KompE.  —  Zom  V.  sray-,  —  gr.  «X/n«.
28319:KompE. ;  Ableit.  —  ä.  j'räyai'  n.  'Fläche', mp.  (Pü.)  iray,  np.  daryä  (woiu  Hbm.  PSt 62).  —  ')  So  auch  y.  42. 4  au  lesen,  wo  NA. sarayö  neben  zrayaohö  bietet.  —  ')  NA.  da- ray'.  —  J)  Nach  der  o-Dekl  ;  aber  die  Form ist  nicht  sicher.  —  *)  FrMOllbr  WZKM.  //. 3S6  hat  ZDMG.  46-  298  jedenfalls  nicht  nach- geschlagen. —  i)  Wegen  der  LS.  traya,  srayä (so  Pt4  lu  Y.  55.  4,  F  I  ru  Yt.  J.  4.  *■  3"  J NA.  hat  auch  trayäi),  beides  verderbte  For- men, s.  Bthl.  ZDMG.  43.  668,  4S-  [49-  Anders FoY  IFAni.  3.  18.
```


## [2026-09-06T20:55:46.910Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '27300,27340p' BRT.txt; echo \"=== 27420\"; sed -n '27420,27430p' BRT.txt",
 "description": "Read BRT sray entry"
}
```


### [2026-09-06T20:55:46.966Z] TOOL RESULT

```
Abieit.  aus  jraasa-.  —  VgL  sraoJyä:
•  j.  sraosyä-  £  'Zuchtmittel,  Strafe': sä%rascit  .  .  yH  nistayeiti  k^rptje  °yqm ". .,  der  die  Strafe  zu  vollstrecken  befiehlt" Yt.  10. 109;  — yS  nöil  jvö  'yqm  usvirityetti "wenn  er  nicht,  so  lang  er  leb^  seine Strafe  abmacht"  V.  /j.  3.
Abieit,  aus  iraoso:  -~  Vgl.  sraosya-.  —   Pü.:
•  j.  sraxtay-,  öraxtay-  f.  'Ecke,  Seite': yat  äkrasca  atvqm  %raxiim  yaozddäiat . . N.  y4'i  ~—  y^i  ■  •  ahrasca  tisrS  'hraxtii yaosda^aiti.y3;—*haoyqm  upa  %raxHm''> N.  7p;  —  daHmm  (sd.,  No.  i)  upa  sraxtim
ai.  srakläy-  f.,  mp.  (Pü.)  sraxISl,  lat  an-fraelus (deSaussube  Mim.  17).  —  ')  T  sr:  —  ')  Hds. •///Tl.  —  3)  Vgl.  inm  ir.  a-(%t-)  %S/.2,  2S3.
•  j.  sray-,  p.  ^'ay-  V,  'lehnen'.  Fraes. I  sray- :  srl-,  z  sraya-,  7  sr3ray-^\  %''äray''> IQ  srinav;  siriaav-'*:srinu;  sirinv-'^;  Perf. I  s-tsray-{i)i\  —  PPfP.  srHa-,
i)  Med.  'sich  lehnen  an  — '  (Lok.):  baoa iia  histahe  anyehe  ävan  (sd.)  srayaiio V.  _J.  29.  j)    'anvertrauen':    sriia    F.
12.  ka%a  JftriTya (3SPfA.).3'  aya^a  tl.. Vyt.5/(?).
mit  apa  'sich  anlehnen  an  — ,  hin- wenden zu  -'  (Abl.)*>:  *taolars  {sA.)  äättyS gätu!  .  ,  ma%p/näi  arä^raol  apa.sritö N.  -jS.  a)  absol.  'sich  anstemmen': frava^ayU  .  .  afrakavasUma  (sd.)  apa.- srayamnanqm  Yt.  y.  26.
mit  upa  Med.  'sich  lehnen,  schmiegen an  — '  (Gen.):    naidyB  mqm  upaJtilta  .  .
upa  ml  srayarauAa  väSahe  Yt  17.21;  — Ufa  kl  srayata  vaiake  Ytij.ai.
mit  ut  'ausliefern,  ausantworten':  %risäj tl  kamahe  ayan  tanüm  usrärayS^  Vyt 41.    Wertlos.  '
mit  paili  und  «r  'zustellen,  überant- worten'; yeä/ur  daiti  paiti  vankö  nisrJia (jSPrM.)  anaiwiJrjtxH  i^A.)  Y.  65. 11;  — ai^anttmälibyö  (sd.)  . .  kanfl  paiti  nisri- nuyat  V.J.  20.
mit«r  i)  'hinbringen  zu —'(Akk.):  t)m  va ahüm  drvanis  syae'hnais  cfäii  *x^ä  *daaia nisirinuyät"^    V.  5.  6a.  2)    'zustellen,
zuweisen.  Überantworten':  yniam  vatmhi (Sp.  1397  m.)  nisrinaela  V3n%ra-jnimca  .. abyö  daiähubyS  .  .  Yt  Jj.34;  —  tSm  in alibyS  xfayamna  nisirinavähi^  Yt5. 87;
—  bawar}  vazyanqm  alsmanqm  .  .  ä%re akurahe . .  aiiJm  nisiriiiuyät  V.  14. 2 ;  Vd.  2  ;
—  nisrität  paiti  draortät  (sd.)  nava nisriläi  V.5.26;  —  niiriiaj  N. //(?);
—  iitum  tl  nanm  nisrinaomi  impm  ml narsm  nisrärayä^  upa  iürqm  fra^.- kfrftim  "diesen  Mann  überantworte  ich dir,  diesen  Mann  sollst  du  mir  (wieder) ausantworten  bei . ."  V.  18.  51.  3)  'aus- teilen, (Schläge)  versetzen':  balvan  ymqnä nisirinaoiti  Vt  10. 27.  4)  0  '(wieder)  in Stand  setzen,  einrichten':  ayadand  tyä gaumäta^  hy<^  magus  inyakcf  adam  niya- ^'ärayam  "die  Kultusstätten,  die  G.  . . zerstört  hatte,  setzte  ich  wieder  in  Stand" Bh./.  i4'>.
irayati,  airel,  iistaya ;  hilälf ;
(a^  afaspirlati.  S.  noch  No.  3.  —  ' II.  S,  itS.  —  »)  Meist  sirin',  %  300.  a;  i.  die einzelnen  Belege.  —  1)  Gant  unsicher;  Fii. : tyän.  —  4)  VgL  gr.  xpiiiäiai  asi  .  .,  lat.  pm- dh-t  «...  —  5)  Them.  —  «)  Ersetzt  noTiat der  Mutterstelle  Y.  31.  zo.  —  7)  So  verbinde ich  troll  ZDMG.  54.  341,  373.  —  «)  D.  i.  ai
j.  iraya,  srayd  Yt.  //.  II,  H.  3.g:  s.  unter
•  j,'srayan-  n.  'Schönheit?:  Ä  asti  masyS vanhs  srays  (sd.)  aOtm  dit)m  . .  upairi anyaii  sraväil  masana/a  vai^Aana/a  °ya- ««(IS.)/«  V.5.23;  —  Ä/Ä  Sic?«  /aiana ava  »lasaiiaca  vanhanaca  °yanaca .  .ya'ha yat  ml  st^ayehi  "Jeder  hat  dich  gern  ge- habt wegen  jener  (deiner)  Schöne  imd  . ., so  wie  du  mir  erscheinst"  H.  2. 1 1 ;  —  ka aiva    als.itüitis    yä    dasa    anyastam    .  .
52»
dby  Google
srav-  n  3  A
1640
masanaca  vaohatuxca  •yana.'a  aryjaili  H. /.6;  Yt/p.  s«,  A.J.  12,  P.4i'>.
KompE.;  AbldL    —    Zd  träy-  f.   —  VgL  ai.
i><m(a«-m.'AnueichnuDE'(aiu  ar.  'indj^man-,
I  &;;  I  /■i;?.  »  No,  I,  —  Pö.:  nrwai,  n?-j.'ai-
tum.  —  'I  Hd».  irajr:
•  j.  *8rayan-  Adj.  'schön':  kaiij/S  -avhuäu yeähi  vJ  (Sp.  1418  il)  masäruiscä  vaaAä- nascS  'jrafiaf(GS.)iä  tankprimahT  "ein wahlhafter  Wohltäter  (ist  er),  cuius  magoi- que  bonique  pulcrique  glorüm  praedi- camus"  Y.5Ä4-
Ableit.  ans  'irt^an-  n.  (igL  antcr  'niuiiii-).  — Pü.:  rüjiialäk.
•  j.  srayana-  Adj.,  PP\L:  s.  sray
•  j.  srayah-  Adj.  'der  schönere':  cä  aUi masyS  vanhs  'yS  aSstn  dätim  yim  vjdsyüm .  .  iipairi  anyäis  sraväÜ  "um  wie  viel ; grösser,  besser,  schöner  ist  dies  Gesetz  . .  1 als  die  andern  Lehren"  V.5.  22;  —  imat\ vaahs  imat  'yS  yj^a  tum  .  .  valaahe  V.  | 5.  a  I ;  —  yalca  ahmst  asti  mazyö  .  . '. vatfhS  . .  'yd  . .  parS.ar?jaslar3m    tat  .  .
Y.ff5-i4.  '      I
Kompar.  in  irwa-.  —  ai-  »gl.  h/yas-  Adj. (wotn  IF.7.  73  No.).—  Pn.:  nrwaklar,  »iwai- tum  (fa  dllan).
•  j-i  g-  srav-  V.  'audire'.  Praes.  1  srav-: srv,  10  surunav;  srunav- :  turunv-*'^ ,  16 (Des.)  suiruia-,  3  7  (Pass.)  sruya-,  30  (Kaus.) srävaya-,  PrP.  smvj;  Pert  i  susru-; j-Aor.  I  smi:  —  PPfP.  irSta-,  PFP. suruftvata-;  Inf.  srüidyai,  srävayeiihi,  srä- vayei'iyäi;  Absol.  -srut^m.
I)  'hören,  mit  dem  Gehör  wahrnehmen'; 1)  ohneObj.:  «3,t/w/ffi>J..j«(Sp.  1607  m.) aoJB  surunaoiii  gaaiaiwe  ya^a  mihrascU. . Yt,  10. 107 ;  —  aj  fravaxlyS  nü  *güiBjiäm (sd.)  na  traotä'>  (iP.)  Y.45. 1;  —  tp^ntä mainyü  sraotü  maidh  ahurS  "durch  den heiligen  Geist  höre  MAh"  Y.45, 6;  — PPA,   mrunvant-    sbes.  2)    mit   Obj.
{etwas,  auf  etwas)  im  i)  Akk.:  sraotä\ ^gSui-ais  {si.y>  vahistä  avaenata  iäcä  (sd.)  1 manattha  Y.^jo.  a;  —  tatcä  vohu  mazdä- sraotü  manarfhü  (Sp.  1131  ra.)  sraotü  asä güsahva  (sd.)  tu  aAura  "und  das  höre VM.,  Q  Matdäh,  .  ."  Y.4g.  7;  —  sraotn sasni  ßfnghyS  (sd.)  Y.  45.  9;  —  also tmrr^B ..ä^rS  vaHm  surunaoiti  FrW. /0.41 ; —  surunuya  nö  yasrum . .  xsnuya  nd  yasnsm Y.  68. 9.  a)  Des.  "mit  dem  Gehör  achten, horchen  auf  — ':  värrfnahe  ..yD..  vayqm väHm  susru.iimiiS*^Yt.i4.ai.      b)pass.
'audiri':  yj/lfyä  (sd.)  s^haiil ysis  srsvi^ itamä  qyatffiä  ". .  Mcut  auditor  .  ,"  Y. 52.7;  —  sva.  'Gehör  findei':  yä  sneyf ( I S.)  **  **  pari  (sd.)  *magaimS  V.  ^J.  7 ;  aL V.  i-j.  7*';  —  sva.  'bekannt,  berühmt, berüchtigt  werden':  iyaomqm  aipl  daibi- tänä  (Sp.  7610.)  yäii  *asnildiim  ( Augm.) "
=== 27420
•  g.  sravabyeiti  Inf.  "bekannt,  berüchtigt
zu  werden' :  pourü  amä  Snäxitä  yäis  sr" yni  iäi!  ahä  hSIU.maräm  (sd.)  .  .  vSistä "die  vielen  Untaten,  durch  die  er  es  er- reicht hat  berüchtigt  zu  werden,   ob  es
durch  sie  so  (werden  wird)":  .  .  du  weisst es  . ."  Y.J2. 6. I      Zu  einem  Praes.  *jrä:>a^>^-,  denom.  Praes.  31 aus  'irävanka-  d.  'Berühmtheit',  Abteil,  (mil Vj-ddhih)  au(  sravak:  —  Pü. !  ie  irül  estil,  Sü. : yak  uklo  'sH.  —  1)  Nämlich  wie  er  es  vorhat ; t.  die  vorhergehende  Strophe, g.  srniini  Y.  a8.  7  -■  t.  sravay-.
•  j.  srita-  Adj.,  PPfP.:  s.  sray-. KompE.
•  j.  sritay-  f  'Lehnen  (usw.)'. KompE.  —  Zom  V.  sray-,  —  gr.  «X/n«.
•  j.  srifa-  m.  'Nüstern':  yal .  .  aspa- nqmca  'fa  xsfufsqn  "und  wenn  die  Nüstern der  Pferde  in  Aufregung  geraten"  Yt /0.113.
Weist  auf  ar.  *sripha;  womit  ich  ai.  siprä-  f. 'Nase'  (im  Nir.)  nicht  lu  vereinigen  weist.
•  ].,  g.  srira-  Adj.  (fem.  T3-)  i)  "schön anzu  sehen,  schön' ;  a)  vom  schönen Äussern  der  Menschen  und  Götter:  virahe kihrpa  ,.  'rahe  YX.14.2T,  17;  —  kainlnö kihrpa  'rayä  Yt.  5.  64,  H.  2.  9;  —  'rB ahi  tara^uilra  huktntB  ahi  . .  kvascvB darrj^.bäiäus  Yi.i-].%z;  —  kikrpasla  ,. 'ra  amisanqm  sppntanqm  Yl  y .  8 1 ;  F.  72 ;
—  'r?m  .  .  bavilki  yaha  .  .  Az.  3;  — dämqn .. pouruca  'raca  Yt7ß.  loj  —  Sat mqm  .  .  'rqm  Aaitrm  srtrSJarqm  . .  H. 2.14;  —  'räsca  Q)  vohu  tnanS  rätaca vanuAi  V.  ig.  1 9  (?) ;  —  usqm  'rqm  G.  5,  J ;
—  °ra  dityha  ahurahe  masdi  V.ig.  13';  30, *F.^e";  —  yima  'ra  (VS.)  V.  2. 3,  9,  »2; 3 ;  — yimäi  'rät  V,  2.  2 ;  —  AaomS  fräimis .  .  °rS  Y.57. 19;  —  oHÜ  vanuhi  'ra  Yt. y.  107;  — a«  •«  (VSf.)  Yt.  77. 6,  60,  61;
—  satavalsB ..'rS  Yt.1j.44;  Äg;  —  aiä -ra  (VSd.)  Y.  j5.  3 ;  —  vsiahe  kihrpa . .  -raht Yt.  74.  2;    —    dalnayai   'rayüi  Yt.  70,  64;
```


## [2026-09-06T20:55:48.590Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && wc -l TAD.txt TAD_pages.txt; echo \"=== head\"; head -40 TAD.txt; echo \"=== grep qlim\"; grep -n \"قليم\" TAD.txt TAD_pages.txt | head",
 "description": "Inspect TAD files"
}
```


### [2026-09-06T20:55:48.647Z] TOOL RESULT

```
  3312 TAD.txt
  3117 TAD_pages.txt
  6429 total
=== head
الف 
8 َ نبي بى اكابى اللبناك 


لحتل 


- اا لدم 
: 7 تت 1 1 ظ 
ا مون 
هني بنشره وتصحيحه وتعليق <واشيه 
ا 


الو مان 


ده ل دام 


« طبعة ثانية 6 


حل ' 


ذكرى الذ ممردص 
الى من حك العل ويغاد على الاادب الى الكير بروحه ونكرة 
وقلبه ؛ الى من حب اطق وشرف الحق ولا نخاف في سبيل المقلومةلاتم 
والى الصديق الصادق فى كرم الا نسانية 
عبم المل ين بابتا اباظ 
اهدي هذا الكتاب 
المخلص 
امم يوس توبا السسّافى 


مصر فى 737 أبريل #اسرة !ا صاحب مكتية العرب 


عر خح- 
=== grep qlim
```


## [2026-09-06T20:55:55.218Z] TOOL CALL #20: Bash

```json
{
 "command": "timeout 300 python3 tools/ref_page.py TAD:57 --image 2>&1 | tail -40",
 "description": "Fetch TAD page 57"
}
```


### [2026-09-06T20:55:56.954Z] TOOL RESULT

```
no scan of TAD covers printed page 57 (see 'scans' in refs_online.json)
```


## [2026-09-06T20:56:03.537Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('TAD_pages.txt',encoding='utf-8').read()\npages=t.split('\\f')\nprint('n pages',len(pages))\nprint(repr(pages[0][:200]))\n\" ; echo \"=== grep leaf tag\"; grep -n \"\\[pdf\" TAD_pages.txt | head -3; grep -c \"\" TAD_pages.txt",
 "description": "Inspect TAD_pages structure"
}
```


### [2026-09-06T20:56:05.701Z] TOOL RESULT

```
n pages 87
'                                     \u202bالف\u202c\n           \u202bياكابىاللبناك\u202c  \u202b\u202aَ8\u202c\u202c\n                       \u202bنببى\u202c\n\n\n\n\n       \u202bلحتل\u202c\n    \u202b\u202a -\u202cاا لدم\u202c  \u202b\u202a1\u202c\u202c             \u202bتت\u202c             \u202b\u202a7\u202c\u202c   \u202b\u202a:\u202c\u202c\n     \u202bا'
=== grep leaf tag
3118
```


## [2026-09-06T20:56:08.629Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nimport re\nt=open('TAD_pages.txt',encoding='utf-8').read()\npages=t.split('\\f')\nfor i in range(58,68):\n    p=pages[i]\n    print('---- leaf',i,'----')\n    print(p[:1500])\n\" ",
 "description": "Print TAD leaves 58-67"
}
```


### [2026-09-06T20:56:10.217Z] TOOL RESULT

```
---- leaf 58 ----
                                      ‫سد‬    ‫اهم‬



                                           ‫‪2‬ك » وهو الحجل‬
                                                        ‫قب ‪ .-‬فارسي ك‬
     ‫معنأه حماس و ‪ 110 862‬ألاتزلاه‬   ‫قرس ل أخوة النحاسى ‏ لانيني امن‬

                                                                 ‫رسسي‬
                                                                    ‫بحا‬
                                                                      ‫أقين‬
                        ‫بعر يب ‪50]0/5‬ألء وهو اسممصر ف اليونانية‬
                                                              ‫قبط ت‬

 ‫ايطالي مطةالمةن معناه فى الاصل رئيس مرادقه ناك السفينة‬            ‫قبطان ف‬

                                            ‫وفائد الجيش وعميد القوم وعمدة وكش‬
     ‫قدوم ‪ -‬عبراني « كردُوم » تأدغت الراء بالدال فصار « قدوم » وهو‬
                                                   ‫مجر النجار وم‪:‬ته‬
      ‫وهو وع سن الهوخ كرة شه حب‬               ‫بوناني ‪8‬‬       ‫قراسيأ وقراصا‬

‫‪١‬‏‬                                         ‫االعلنباسود الا ان فىلبه عجمة واحدة‬
                       ‫قراغول ‪ -‬ترك « فراغول » معناهرييئةوطليعة وخفير‬
                                    ‫قرداحي ‪ -‬أرامي « قرداحا » وهو الحداد‬
                                                         ‫فرش س راجع غرش‬
                 ‫قرصان | ‪.‬يطالمي ‪ ©1350‬معئاه غازون وبراد به لصوص البحر‬

             ‫قرطاس ‏ وناني همارك معناه ما جرسم به مرادفه ورقة وصحيفة‬

              ‫معناه قرن
---- leaf 59 ----
                                        ‫ده‬     ‫ااه‬



‫اراق « كرميل »عد الإل الال وهو تدناظري 'تحوت دينكم أي |‬
‫دودة ول أي حراء وهزاكوقة عراء كرن ف ‪:‬ضوف اقاء مو نف ابيقة ‪1‬‬
‫اوتستعها وهو نوسود ف نينا ‪١١‬‏‬
                            ‫ويقع على ورق شجرة بلوط القرمز وعلى أنه ) ب‬
  ‫والهند والككيك وسائرالبلدان الحارةفيجمعفىحينهويصبغ به ولونه أحر قانر‬
                                   ‫فنقل قرمر منالعر ببة الى لغات اوريا بلفظ و‪6‬ممه؟‪1‬‬

                                            ‫قرقة © ‪ --‬تركي( غورق عريهارنقاء‬
    ‫قرميبدد ‪ -‬بوناني ‪5112:2, 8‬نع‪ 21‬معناه تراب محروق أي طهيشنوي” وهو‬
                                                               ‫الخزف والفخار والاجر‬
   ‫وزاك الذئ بال حل عالقا ستول سن انوناق وموم عرو اينرنيتاة‬
    ‫عندمم زمانووقت ومدة وستون و دكأبظا على الهالزمان مرادفه دهر أي مأئة سنة‬
   ‫قترفل ‪ -‬فى اليونانية مله رخفا وهو شجر قروئه أفضل الافاويه‬
   ‫وبطلق أيضاعلىنبات بستاني زغوه علتن الاقامتفاء وان مداوكه وقد‬
                                                               ‫ينجبتز فاىئر الانطيل‬
                                             ‫قن وخر" ‪ -‬لفظ فارسي براد بهالخرير‬

   ‫قس وقِسّهس ‪ -‬أرامي « قشيشا » معناه شيخ وقديم وقد يلقب به الكامن‬
                                                                          ‫عيدنا ازاما‬
                       ‫قشطة”” ‪ -‬عامي وهو مصكف قثدة أي الزبدة الرقيقة‬
                                        ‫ا‬    ‫قشلة ‪ -‬ترك » قشلاق ‪ 6‬معناه مسُتى‬

    ‫قصبار ‏ من اليوناني هفهطادءا أي طهر ونظا
---- leaf 60 ----
                                  ‫سالاع سد‬


 ‫اللانني شمعئاه حصن وقلعة‬        ‫‏‪ ٠‬عرني محض وهو الصرح أما مق‬

              ‫ومنه البلاط أي قصر الملك‬        ‫‪"3 00‬قِالأديية ا‬
                                                             ‫والقهعر‬

                     ‫قصدر ‪ -‬ونالى وم‪2‬ه‪1‬أ‪:55‬؟‪ 1‬وهو ممدن لين يطلى به‬
                                                                ‫ل‬
                       ‫ونه ‪ -‬فايليونانية ‪ 50421101‬معناه زنبيل من خلاف‬

 ‫غلاف اللكحلة ‏ فارسي مركب ون كف أي كلل ؤذا نوعو‬               ‫تدان ‪-‬‬

                                             ‫صيغة ظرف المكان تلصق بالاسياء‬
‫قفص ‪ -‬عرنيمحض وقفسالفارسي التركي مأخوذ منقفصالعربي و دومه)!‬
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


                                   ‫قله في اليونائية ‪5022
---- leaf 61 ----
                                                       ‫لوش ‪ -‬اطلب كالوش‬
                          ‫كظورنت‬
                               ‫قس وقومس ‪ -‬أمير ورجل شريف ‪ -‬ان‬
 ‫قاش ‪ -‬في الفارسية ك«ش » معناه نسيج من قطن شن ثمنقل قاش الى‬
                                                            ‫الفارسية بلفظة فاش‬
      ‫ترك « قامش ‪ 6‬معناه قضيب وقصب و ( فجي » معناه سوط‬                     ‫‪2‬‬

 ‫وفي اللغة‬             ‫في الايطالية *‪01‬مهه وفي اللاتينية الركيكة‬       ‫فض‬
‫كا فعي منقولة من اللاتمنية الى العربية والى السسربانية ايضا‬        ‫اللعزنطية ‪805‬‬

                                                                   ‫‪6 05 2‬‬
                                                                           ‫َ ‪2‬‬
                             ‫قمهم‪ --‬فارسي «‪ ) 5‬وعرببه يعدروم‬
                    ‫معناه ‪1‬ون وموقد‬       ‫وق الخجام ب بوناني ‪5‬‬             ‫ثين‬

‫وفي اللاتينية دتاتاء معناه أعلىكل شيء مرادفه‬       ‫شه وهامة ‪ -‬بوناني ‪51‬‬
                                                                      ‫وك‬         ‫‪010‬‬

                                                            ‫قله وقلة وشعدفة‬
                                                                           ‫‪9‬‬

‫شريمتفازنى و كد ب و©أصل هذا النبات من بلاد الهند وفارس فتقل‬
             ‫الى اليونانية ونطهدسهة ومنها إلى الابطالية ‪#‬مقصد وسائر لغات اوربا‬
       ‫قكرذةف من المدفم مرادفهاقذيفة‬
                                   ‫قنبلةبتري « قومباره » وتهي‬
                      
---- leaf 62 ----
                                      ‫د‬    ‫سابةاجم‬




   ‫عمعناه شمعة يستضاء مهامرادفه مصصباح وسراج‬            ‫قنديل ‪ -‬لانيى ‪84‬‬
                                                                              ‫‪1‬‬     ‫‪01‬‬

‫قعل ‪ 5‬ب لاتيبى امه معثاه مشتكاد وراد به فى زماننا تمثل الدولة‬

              ‫«الالنةرعاتون معناه مئوي من «اتاأهعء مائة‬            ‫قنطار لاتينى‬

 ‫متسوب الى ‪80:00212‬و]آ‬             ‫قنطارون وقنطورون ‪ -‬لاتق ‪82‬‬

‫قنطورس اليوناني وهو هولة اي هسك نصفه اسان ونصقه فرص ومعنى قنطورس‬

                             ‫افلييونانية تاخز الفرس وهو ابيحشيشة مر الطم‬
                  ‫قال ‪ 3-3‬لاسى ماله معذأه خجرى الماء مر أدقه وناة وبرعة‬

‫‪0‬قت ‪ -‬وون‪.‬انى وهو ‪1‬خادم الكنيس ‪1‬ة وعرببه ا ‪1‬لنصيح الجللازي وهو‬
                                                             ‫‪0‬لف‬
                                                                                    ‫اه‬
    ‫طًُ‬

                                                               ‫قد‬
                                                                           ‫خادم البيعة‬


‫معناه مدر اأبيت وبراد به أمين الدخل‬                   ‫وونابى ‪5‬‬              ‫قبرمان‬
 ‫ن الفارسيفبو متحوت مقر العرنى ومانالفارسىي ععى صاحت‬
                                                   ‫وار ‪ 3‬امأقبرماج‬


           ‫وهو هب للشاه أ‪,‬ضنا‬          ‫وهو مستعمل عندثم تهى غالب وظافر ‪0‬‬


‫قوأنج بست مرض تصيب القولون ممامعآ‪ 1‬اليونابى الذي معثاه شعية من الأمعاء‬


                                   
---- leaf 63 ----
                                    ‫ساي سم‬


    ‫وناتي ‪80‬م ومنه الانكيزي مو وهو الحندب البحري‬                     ‫قريدس‬

‫اليوناني ومعناه قرن صغير ويطلق على قرن‬             ‫دوعا‬     ‫ل‬          ‫قراط‬

‫الخرنوب وعلى حبة الخرنوب أيضا وكان الاقدمون يزئون الذهب بالقيراط أي‬
                                        ‫حبة الخرتوب وكل ‪5‬ح‪4‬بة نساوي أأوقية‬
      ‫معنأه مشمّم وبراد به مرحم ضمّد به‬               ‫بوناني ‪06‬‬      ‫قيروطي‬
                             ‫قينةسأي بنتنيةف الأضل العتراق ماعة ارائنة‬
                                     ‫دك »‬
                ‫كابلا ‪ -‬ايطالي ‪2‬ااعومهه معناء معبّد أيكنيسة صغيرة‬
‫كاتدرائية ‪ -‬منسوب الى ‪20060‬ادك اليونائي الذي مدا واس و‪ 1‬سي‬

‫وبراد بهكنيشةكرسي المطران لان كرسي المطران أي عرشه نصب بهاعادة‬
                        ‫كاويك د نانى وعانادط]ه»! معناء جامع شامل عام‬
                                ‫كاغد ‪ --‬فارسي ‪ 2‬كاغد » معناة ورقزمقة‬

‫نفاينية ‪ 2500121‬وهوصمغ شجرة تنبت في المند والصين‬
                                               ‫كاافلويروس‬
                    ‫”‬        ‫واليابانأبيض لماعشفاف قابل الاحتراق طب ةو‬
  ‫‪6‬‬                ‫‪0‬‬‫هعناه خادم الاله‬
                                   ‫ر م‬                          ‫كامنل‬

                                            ‫مهئأه العاضى ا‬           ‫‪0‬‬

           ‫‪8‬‬             ‫‪8‬‬              ‫‪0‬‬                               ‫‪5‬‬
‫وهو سيال‬       ‫الشيء ‪0‬‬    ‫مط‬   ‫سن‬   ‫كاوتشو ‪ -_-‬امه امريكية براد با المطاط‬



             
---- leaf 64 ----
                               ‫‪ 2-0‬ل‬


                ‫فونانى ‪5169‬مم‪ !2‬عربيهالأصّيف م ى الزغر‬          ‫‪53-5‬‬

‫“سول الفيؤنانكه عار ولاموله طناسنة قارف ادراونة تن‬
                              ‫وهو قعيحشى من ملح الزئيق فيشعل البارودة‬
    ‫“كتهدا وكاغية حر ‪:‬وكتخا واه يهسقندالواليوكاتمسر"ه‬

‫«وتينا » وف اليونانية‬
                    ‫‪ - 8‬عبرانى ‪ » 65‬وى الارامية كم‬
‫للك ‪ 0‬وهو القميص من كتان وغيره الظاهر الها مشتقة من الكتان‬
                            ‫مادمها وهو نبات معروف تنسج من لهاءه الثياب‬
              ‫نالسران ‪ 3‬كر وق التونانة ددم‬             ‫‪71‬و‬
                                  ‫كرباج ب تر « ‪.‬قرباج » وهو السوط‬
‫فى ع اللكيمياوعنهكرنزنات‬     ‫يوطناسلي ‪0‬تدوطمرهء ام‬
                                                 ‫اكر‬
                              ‫‪0‬‬          ‫وهو كن من الخامض الفحهي‬

                  ‫كرنون ‪ -‬ايطالى ‪680‬ةه معناه ورق صفيق ومقو"ى‬
                           ‫اال فارسي كار حانه» معئاه معيل‬

 ‫‪ -‬بوتالى ‪ 5022:6:1‬وهو شجر سمي بالكرز كمرناسون وهي مديلة‬
‫فاىسيا الصغرى على ساحل اليحر الاسود وثقله ارلوىمية القائدأ كولو‬
                                               ‫سنة “لاق م راجم قراسيا‬
 ‫‪ 1‬راز ‪ -‬فارسي ‪ » 600‬وهو الغركافة نقلت الى الابطالية ‪:612‬ة>»‬

‫دحل بطنها‬     ‫ج‬
              ‫جنةامن‬
                   ‫زيقني‬
                       ‫فاسترجعنها العامة بلفظ كرافيه وعربيها غرافه وه‬
                               ‫وضاق عنقها كان يشرب مهاعرب اسبانيا‬
‫أكرّز‪ -‬أرامي «كرّز » ( المستممل الآن ك|رز
---- leaf 65 ----
              ‫معنا ودس ويارك ومازاً ‪1‬‬                ‫‪ 1‬ع ‪ -‬لانيي ‪1‬‬

                      ‫«رشف » وهو القطن‬
                                     ‫اتيف وكرفس‪ -‬فارسي ك‬
                              ‫فلارامية «كرفسا »( بات)‬
                                                    ‫كرفس ا‬
                               ‫نات )‬          ‫الآراية ناه‬            ‫"كر حاف‬
      ‫ايطالى فوعامج رونو معناة اونشوك نومامرادقه الجر الصحي‬                ‫ال‬

‫كرنيتة ‪7‬س ايطالى هااءد‪.‬ده معناه قرن صغير وهو بوق تحيف ينفخ فيْه‬
                                                                            ‫كازمارة‬

‫واروسميهة وكروبين وشارويين ‪ -‬فاىلعيرانية « كووب ‪3‬‬                        ‫‪1‬‬

‫كع » وثم بمثلون الملاتكة الغير المنظورين الا ان صورتهم الحسوسة انما هي‬
‫‪ 85:91‬حزقيال ‪١٠:١١‬‏ الك‬              ‫ور دو أربعة أجدحة تكوين م ‪:‬خ‪4‬روج‬
 ‫أصل هذا اللفظ أشوري ومعناه حارس لان سكان شنعار فىبكابالنوا يصورون‬
                 ‫حفراً فى جدران الدور ثورا ذا أجنحة ايحرس الانواب والمداخل‬
                         ‫سب ايطالى ‪822‬ه‪ ©223‬معناه عربة وعجلة‬                 ‫>‬

 ‫كرون سديوناق وها زعو نات ووو عر عداو ا قل انيما‬
‫الكرويا نبات معروف يشبه أغصانه وورقه بالرجلة‪.‬الا ان لون أغصانه وورقه الى‬
                                 ‫الكودة أميل وقوته قريبة الاحوال من الانيسون‬
‫وفى اليونانية ودمععامصة‪ :‬معناه جلد‬         ‫وفى الفارسية ‪00‬‬
                                                         ‫كركدن ح‬

    ‫‪0‬‬          ‫‏(‪ )١‬وأليقماتمى ويبهه ناسو وهو آلة مانل
---- leaf 66 ----
‫فاتدير سموا به وحيد القرن على سبيل المشاعبة أدذمهها ‪:50‬عتاوهاء فراسوه‬
‫وعر وه كروكدحنأييد القرن الهنديويوز أنيكون الاسمفينيقي« قرنإحد»‬
                                                        ‫أي وحيد القرن‬
               ‫كستك وكشتبج فارمبي ‪ 9‬ع ‪ 6‬معناه خبط غليظ‬

‫الوا ‪:‬فاه ونيفاة‬            ‫“كتوفت لعن بوالقين الفولة حمر‬
‫تقممان النوروقدتكسف الشمس لهاولة القمربينهاويين الارض مرادفه احتجي‬
‫"ابح لاتق دءمفادن وهو شجر وف اليونانية «م«ماوةا سمي‬
                                   ‫باسممدينة فى بلاد اليونان مهدا الامبر‬

        ‫"تان حب فارسي « انكشتانه » معناه اصبعي مرادفه فمالخباط‬

  ‫رديبطهة‬
        ‫خمرا‬
           ‫معناهجامكل شيء وال‬        ‫‪ 1-‬ب أرامي‪ 8‬كر‪0‬‬
‫ل المذكور « كناش » فى قالون ان سينا‬        ‫امتكدي يجمم فها رزقه ومن‬
                           ‫وهودقتريكتب فيهالانسان ماينغي أن محنظه‬
                                   ‫تعريب «كاك ‪ 6‬القارسبى‬        ‫“كيك‬

 ‫معناه غطاء عقب الرجل ‪ .‬وجورب‬       ‫كاسات وقاشين ‪ -‬لانيني ‪3‬ع‬

       ‫‪0‬‬            ‫رلارجدلفه لفافة الرجل‬
                                        ‫ججوارب فارسيمعناهقبمر ا‬
‫وتالى ‪5‬ه معناه إرث ونصيب واللمراد به كبئةاليعةلان‬           ‫كليرس‬
                                                                ‫لله نصيمهم‬
 ‫كاله د ايطال مده 'مضاة ورقة مدل يتوه ‪:‬مزادفة تنك للامز‬
                                                            ‫والصك والوثيقة‬
                           ‫ونطروي معتاه بدل التقود وصرفبا‬         ‫‪00‬‬

---- leaf 67 ----
  ‫‪ 1‬وبراد به منطقة من شعر ‪1‬‬            ‫فارسي « كر ‪ 4‬ا‬              ‫‪0‬‬      ‫‪3‬‬

                                                                       ‫اعلحىقوين‬
‫اه فى الغارسية والتركية مرادفه دار التمكس وما يؤخد‬           ‫كلك سوم‬
                                   ‫على البضائع والسلم ‪ 0‬له مكساج مكوس‬
   ‫كنحة ‪ 9‬فسارسي «كانجه » وهيآلةطرب ذات أوتار تشبه الربابة‬
              ‫كنار مدفازني‪ «:‬كنار »وهو اقيق أ بهل شير المدد‬
 ‫“نار أتوار تسرهو عماتور مقن "لزان يللد الوص ال غار‬
                                                       ‫كناريا فى غرى افريقية‬
        ‫‪ 0-5‬فارسي « كنار » براد به حاشية الثوب والطرف والساحل‬
‫فى الارامية ك«نارا © وفى العبرانية « و » وعي لشبه‬                       ‫‪00‬‬
                                   ‫اليونانة أي قيثار ذات هسة ‪1‬‬              ‫‪2‬‬

‫كناثة كناش باق ‪:‬تارق التو سياه وقتق ردي كنتنة الارابي‬
                         ‫أي جسعوالمرادبه دقتر يدرج فيه ما براد استذكاره‬
‫فى مقدمة ابن خلدون ‪ -‬اسباتي قدم تررمء معناه ىق الاصل ركار‬              ‫نان‬

‫مقداستعماوه لقياس سمت الارتفاع فكان لمكحك مهتدون به فى سفر البحر‬
     ‫ا‬
                                                       ‫كفل ووش أي غطاء‬

                      ‫‪ (0‬لبانق به مأ‪,‬وضم فيه الدراعم‪ 5‬ونوا ل أن‬
         ‫(؟) قااللنشيفاء الكمتجه رياب معروف معربكانجه عر بهحادلئون ا قيل‬
                ‫‪+‬إلى جام تسيصيا‬          ‫اليس حلجق وناك‬
                 ‫ما‬
                 ‫‪5‬ن‬   ‫وراح عناا‬          ‫اليس من صدا يبآ‬
```


## [2026-09-06T20:56:24.683Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nimport re,sys\nt=open('TAD_pages.txt',encoding='utf-8').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    for ln in p.split('\\n'):\n        c=re.sub(r'[‎‏‪-‮\\s]+','',ln)\n        if 'قليم' in c or 'قلم' in c and 'اقل' in c:\n            print(i,'|',ln.strip())\n\"",
 "description": "Search TAD for iqlim"
}
```


### [2026-09-06T20:56:26.520Z] TOOL RESULT

```
81 | ‫فز‬‫لآفظرةاضة « وا »© وهوامقتقدياقل م‬
```


## [2026-09-06T20:56:38.593Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('TAD_pages.txt',encoding='utf-8').read()\npages=t.split('\\f')\nfor i in (10,11,12,13,14):\n    print('---- leaf',i,'----')\n    print(pages[i][:1200])\n\"",
 "description": "Print TAD early leaves"
}
```


### [2026-09-06T20:56:40.327Z] TOOL RESULT

```
---- leaf 10 ----
                                 ‫م‬‫ميه‬
                                    ‫م ل‬




‫وممامدم أي قاس وهو‬
                 ‫مكب م‪6‬ن‪ 5008‬أي قل د‬
                                   ‫باروسيرت يوناني ر‬
                                           ‫تستعمل لنرقة قن الوا وطذعاه‬
‫بارون ‪ -‬ايطاني مهن أصله من لغة جرمانيا ااقديمة ةط ومعناه رجل‬
‫حر كان يتولى قدي أراضي الامراء اعا هو الآن لقب شرف دون الكونت‬
                                                       ‫وهوآخر الالقاب‬
           ‫باز وبازي ‪ -‬فارسي عر بيهالصقر والعقاب واللاعة والحياقية‬
                                                 ‫اسايق ب ينا‬
     ‫وني مه لتههطا معناهملكيوهو لقب لعرق في الذراع‬
  ‫جرل ومن شاه أي ماك وسلطان‬
                          ‫باشا‪ -‬فارسي مركب من باأي لدم و‬
  ‫| باشق ‏ فارسي « باشه » وهو طائر أصشر من العقاب مرادفه يؤيو وج‪1‬م‬
‫بال ايطالي دادم معناه رفش وعربيه قملب ‪:‬قلب به الارضللزراعةأما‬
                        ‫رويب ‪ 8:585‬الابطالي وهومجرفة منحلية '‬
                                                            ‫عفه‬
                                                              ‫تمر‬
                                                                ‫ال‬
‫بال وبالة ‏ لاتيني ‪806‬هلده مناه 
---- leaf 11 ----
                                                              ‫عت ات‬


 ‫بأميا ‪ -‬نبات له قرون تطبخ أصله من أهريكا الحو ببة واسمه هناك هطتترمع‬
 ‫و ‪40362‬دمع وعرنوه ياميا لويتئوه ‪1‬اناء وأطل! أي غاذق إزجة وهو من قصيلة‬
                                                                                                                          ‫الخعامي‬

                                                        ‫‪-‬مي « بير ب»راد به هعنردي‬    ‫ار‬‫يفبر‬
                                                 ‫بيغاء ‏ أصل هذا الطائر من الهند واسمه هندي‬
                                 ‫موف المفسول‬
                                           ‫من‬‫لم‬
                                              ‫ايج‬
                                                ‫بت ‪ -‬فارسي ‪ 0‬بت © وهو نس‬
               ‫مول ‪ 0‬ايطالي وتامماءم معناه زيت الحجر والنفط يستخرج منه‬

                ‫وبراد بهترميل من حشسب‬                          ‫دن اليونانية نا‬                  ‫ايطالي ‪06‬‬             ‫بثية ب‬


                                                                   ‫نخت ‪ -‬فارسي « مخت ‪ 4‬معناه حظ‬
                                       ‫‪5‬‬           ‫‪5‬‬                              ‫‪5‬‬          
---- leaf 12 ----
                                 ‫عت اب‬


                                ‫رجيس ‪ -‬اسمالسيار لمشئري بالفارسية‬
 ‫ايطالي ‪ 35618200‬معناه سثر الباب أصله فارسي « برده (أي ‪5‬‬       ‫رداه‬

                                                           ‫وسجف وغطاء‬
‫ريد ‪ -‬فارسي دن ردن أي دل وهومذكورفيسفراستيروكان مستعملا‬

 ‫قبل ‪5‬ال‪626‬؟ اللاتيني الذي أنشاهاو عوطس لنقل الرسائل وفى الايطالية ‪8150‬م‬
                                                        ‫وقد عرلوه بوسطة‬
                    ‫برد س حامية‪ --‬تركي « برداخ » أي صل وجلا‬
                                   ‫ردي ‪ -‬مصرية وهو نبات كالقصب‬
                    ‫معناه زائر كنانمي”‬       ‫ودبوط ‪ -‬يوناني ‪7‬‬
             ‫رذعة ‏ ارامية ‪ 9‬بروّعتا » أي حلسالدابةمرادفه وكاف‬
            ‫دون ‪ 53‬لانيني مه ‪,‬روك قاط أي كل ابوهحصان وآية ائان‬

            ‫“رشان ‪ -‬ارامية «فريستا» أي قرصة تصنم املندقيق الابيض‬
                 ‫برسام ‏ فارسى مركب من راي صدر وسام أي المهاب‬
                                                  ‫رشت ‪ -‬انظر برشت‬
‫رطاش ‪ -‬عامية مأخوذة من ‪ 82:61:00‬الايطالية ومعناها ستر البابوعر بها‬
                                                            ‫أسكدَّة الاب‬
                                 
---- leaf 13 ----
                                        ‫ك‬
                                        ‫ح ‪:‬و‬
                                           ‫تبن‬


      ‫ركي‪ -‬عامية ‏ فارسي « بملكرىوبالكدهف»ها لويعحلثمل أن‬
                          ‫رميل ‪ -‬ايطالمي ‪ 11:35‬وهو وعاء مستدير من خشب‬


                   ‫َ‬

                ‫وهو التعة‬          ‫برنيطة ب ايطالى ممتااع معط اوم ‪0‬‬



‫معناه ورقة ملصقة بالسجل وبراد به‬        ‫لظ بير نعطي‪6100‬م‬               ‫بروتوقل‬


                                  ‫السجل الأول والمحضروبيان الجلسات السياسية‬
                         ‫ببزار ‪ 3301‬فارسي « بازدار » أي حامل البازي أ الباز‬

‫معناه الحاصل قدام‬         ‫ايطالي ‪2121502‬م من اليوناني ‪56‬‬              ‫بروسطاتة‬

                       ‫وعربيه خائقةالمثانوةهي غدة محيطبعنقامثانةكزيق القميص‬
                            ‫فارمي ‪ 0‬بازيار ‪ 0‬أي الأكار أوالفلاح‬         ‫سار س‬


                                              ‫ديا » أي الثدي‬            ‫‪0‬‬
         ‫معناه جواز المربى مرادفه جواز‬          ‫ايطالي وم‬                ‫‪00‬‬

                         ‫وببكفي وتحاب"‬
                                     ‫بن "‪1‬س لنظفازبيبرادفهكتىو‬



  ‫و"ر‬
    ‫ب مر‬
       ‫وناها‬
 
---- leaf 14 ----
                                  ‫دوو‬


‫من « وى » أي رابحة ذكة و‪9‬ستان» وهي أداة‬           ‫يتان ‪ -‬فارسي ‪5‬‬

                                                    ‫تدل على ظرف المكان‬
    ‫على ‪ 1‬ايطالي والودام ج للأءذام وهو تصغير ‪05‬وم أي وزنوقاللانشة‬

‫بلبنيوس وفي اليونانية هؤام وهو نات بستني سنويله سنف أي‬         ‫كام ‪6‬‬

    ‫قرون في جوفها كحابلمص حاوالطيموقد ينبت في جبل لبنان وتسميه العامة‬
‫ش‬                                                 ‫هناك « الحالية » من طممه‬
           ‫شتختة ‏ عابى ‪ -‬الصندوق الصفير ‪ .‬فارسي م ركب م‬
‫بنيش أي أمام‬
                                                ‫ومختهأي لوح‬
                               ‫تركي « بشلك ‪ 6‬معناه حماسى‬         ‫شلك‬
‫معناه ضارية وبراد به عدة مدافم تطلق م وفي‬       ‫بطارية ل يللي ‪3‬‬
                                        ‫لكوت ‪ +‬كك اليف‬
‫رظأقة حاارائية و قات أ ‪.‬وطالة وكتانتة وووقة وأم[ مناه ‪ 121‬اليا‬
                                        ‫كانت شق من اللوح ليكتب عليها‬
    ‫بطرشيل س بو ثان ‪1‬ي‪00‬ل هزه وعوببر‪ 8-5‬من أع أيفودودوزاغطعه»؟‬
‫ةجعلبا الكاهن فيعنقهعندمباشرنه‬
                             ‫رطرز ي‬
                                  ‫نزيم‬
                                     ‫وقةل
```


## [2026-09-06T20:56:53.346Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('TAD_pages.txt',encoding='utf-8').read()\npages=t.split('\\f')\nprint(pages[60])\nprint('=====61=====')\nprint(pages[61])\n\"",
 "description": "Print TAD leaf 60 and 61 fully"
}
```


### [2026-09-06T20:56:54.885Z] TOOL RESULT

```
                                  ‫سالاع سد‬


 ‫اللانني شمعئاه حصن وقلعة‬        ‫‏‪ ٠‬عرني محض وهو الصرح أما مق‬

              ‫ومنه البلاط أي قصر الملك‬        ‫‪"3 00‬قِالأديية ا‬
                                                             ‫والقهعر‬

                     ‫قصدر ‪ -‬ونالى وم‪2‬ه‪1‬أ‪:55‬؟‪ 1‬وهو ممدن لين يطلى به‬
                                                                ‫ل‬
                       ‫ونه ‪ -‬فايليونانية ‪ 50421101‬معناه زنبيل من خلاف‬

 ‫غلاف اللكحلة ‏ فارسي مركب ون كف أي كلل ؤذا نوعو‬               ‫تدان ‪-‬‬

                                             ‫صيغة ظرف المكان تلصق بالاسياء‬
‫قفص ‪ -‬عرنيمحض وقفسالفارسي التركي مأخوذ منقفصالعربي و دومه)!‬
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


                                   ‫قله في اليونائية ‪5022‬داة؟آ ممناه قصة‬

‫الارضية مرادفه دقع‬      ‫براد به منطقة م ن مناطق الك‬    ‫‪0‬‬         ‫اع‬

                                                               ‫وبتعة وفعي‬
   ‫‪3‬‬                                              ‫‪00‬‬
 ‫همععناه فى الاصل غطاء راس‬          ‫فلنسوة وقلسوة وقاوسهة ‪ -‬وناني ‪2‬‬

  ‫‪02‬‬        ‫بكري به زكروسهم مشتمًا من ‪1‬‬‫رأَةوهوالنصيفيغطيٍ‬
                                                        ‫الى‬

                                                           ‫ل !اس أي عا‬

=====61=====
                                                       ‫لوش ‪ -‬اطلب كالوش‬
                          ‫كظورنت‬
                               ‫قس وقومس ‪ -‬أمير ورجل شريف ‪ -‬ان‬
 ‫قاش ‪ -‬في الفارسية ك«ش » معناه نسيج من قطن شن ثمنقل قاش الى‬
                                                            ‫الفارسية بلفظة فاش‬
      ‫ترك « قامش ‪ 6‬معناه قضيب وقصب و ( فجي » معناه سوط‬                     ‫‪2‬‬

 ‫وفي اللغة‬             ‫في الايطالية *‪01‬مهه وفي اللاتينية الركيكة‬       ‫فض‬
‫كا فعي منقولة من اللاتمنية الى العربية والى السسربانية ايضا‬        ‫اللعزنطية ‪805‬‬

                                                                   ‫‪6 05 2‬‬
                                                                           ‫َ ‪2‬‬
                             ‫قمهم‪ --‬فارسي «‪ ) 5‬وعرببه يعدروم‬
                    ‫معناه ‪1‬ون وموقد‬       ‫وق الخجام ب بوناني ‪5‬‬             ‫ثين‬

‫وفي اللاتينية دتاتاء معناه أعلىكل شيء مرادفه‬       ‫شه وهامة ‪ -‬بوناني ‪51‬‬
                                                                      ‫وك‬         ‫‪010‬‬

                                                            ‫قله وقلة وشعدفة‬
                                                                           ‫‪9‬‬

‫شريمتفازنى و كد ب و©أصل هذا النبات من بلاد الهند وفارس فتقل‬
             ‫الى اليونانية ونطهدسهة ومنها إلى الابطالية ‪#‬مقصد وسائر لغات اوربا‬
       ‫قكرذةف من المدفم مرادفهاقذيفة‬
                                   ‫قنبلةبتري « قومباره » وتهي‬
                                 ‫«ند» قرفن الب‬
                                             ‫ند ‪ -‬فارسي ك‬
 ‫فارسي «كندسك ‪ 6‬معنأه خصية الكاب وغو‬               ‫ا‬     ‫وفلدز دن‬          ‫‪5‬‬

                                          ‫كلب الماء وخصيته يقال لها جندييدستر‬
‫قندسة وكتدجة ‪ -‬فارسي «وكنده » وهوخشبة يستعملها البثساؤنفي‬
                                                                   ‫بنيان القناطر‬
```


## [2026-09-06T20:57:11.740Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in MON_part1.txt MON_part2.txt; do echo \"== $f\"; grep -n \"اقلیم\" $f | head -5; echo \"-- kelinik\"; grep -n \"کلینیک\" $f | head -5; done",
 "description": "Grep Mo'in for eqlim and kelinik"
}
```


## [2026-09-06T20:57:12.714Z] TOOL CALL #27: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:1296 --image 2>&1 | tail -40",
 "description": "Fetch Borhan-e Qate page 1296"
}
```


### [2026-09-06T20:57:13.667Z] TOOL RESULT

```
== MON_part1.txt
15585:باشد. قدما زمین ت_ به هفت اقلیم تءه 
15587:اقلیمیا": 2 [- قلیمیا» معر .] (ا.) خلطی 
23718:مسیع؛ ؛ (کد.) زمین به اعتبار هفت اقلیم. ۰ نوع 
49019:اقلیمیاء کلیما. 
-- kelinik
32629:بلی کلینیک: ۲ اه (امر.) (بز.) 
80374:متبلور را گویند که در سیستم منوکلینیک 
== MON_part2.txt
13360:اقلیم. . کرانه؛ ج. اقطار. (هس. نج.) الف - هر 
23485:از هفت بحش زمین؟ اقلیم. 
23689:هفت بخش کر؟ٌ زمین؛ اقلیم. مملکت. بهم 
90407:پادشاهان هفت کشور (يا هفت اقلیم). همه 
90411:گردش: هفت کشورء هفت اقلیم. 
-- kelinik
29969:اکثر در سیستم مون وکلینیکك متبلور می‌شود و 
70416:سبز مون وکلینیک است.
```


### [2026-09-06T20:57:21.406Z] TOOL RESULT

```
که بردین شمای‌آتش پر ست بودند وعدل‌ترسابان | و لوحه‌کنان ‎٩‏ - ورمیده شده و آشفته‌وپریشان
داشتند و امشانرا عربان شماسه خوانند. گشته باشد - و بمعنی لفرت کننده - و ترسنده

شماغنده ۴ - با غن نقطهدار بر وزن | - و بیهوش شده - وف برلشی افتاده ازنشنگی

پراکنده » هرچیزی بد بوی راکوبند عموما | - وبانك وکريةٌ دمادم -وكريةٌ درکلو هم‌هست.

و زن بد بوی ومتمفن را خصوصا. شمائیف ۲ « بروزن ومعنی رمانیدباشد
۱۹- 58203۳28 از عبری « شماشا » ( شماس/خادم » عابد ) مشتق از 5102706510
(خدمت کرد * آفتاب‌را پرستید » لماز گزارد) درکناب‌التاج آمده: الشمای کشداد «ن‌رژی الذصاری
الذی بحلق وسط رأسه لازه) للبيعة . « آلاثار آلارامية فی لفة الموصل العامية س ‎0٩‏ > شمای ها

( دیکان‌ها 1۳6200853 ) درسازمان کلبا| » گروهی از روحالیان بودند که شغل آنان توجه بفقرا
بود وبعد ها کشیشان را کفتند ( تارخ‌کلیسای قدیم در امپراطوری روم وایران .و.م. میلن . ترجمةٌ

علی‌نختین ۱۹۳۱ س ۱۳۷۰۱۰۹ - ۱۳۹ ۲۸۳۰۱۷۸ وغیره) :

بناقوی و پزنار و بقندیل بیوحنا و شمای و بحیرا .اخاقانی‌شروانی ۰2۲۵

۴ - جمع شماسی (منسوب بشمای [۸.م.]) لغة پرستند کان آفتاب.

۴ - شمفند (.م.)- شمفنده (و.م.) :

خطش چوپشت و روش شما فنده و سیاه " کاعذ باه و ژنده چو کون دریدکان .
یور بهای جامی.«جهانگیری» .

۴ - (عر) ۶ شمال دست چپ است ضد دست راست ... وشمال بفتح و کسر اول بادست
که میوزد از روبروی حجریا آن بادستکه پیش میآید نرا از دست راست تو وتو پیش آبندة باو
ودرست وسحیح آنت که جای وزیدن ارمپان برآمدن آفتاب وبنات اللمش با از جای برآمدن

فش است تاحای فرو رفتن سرطایر» «شرح فاموی» . ‎٩‏ - آسم فاعل وحال‌ازهشمیدن» .

: ‏شمان . بانگه کربهٌ دمادم در کلو باشد » عنصری (بلخی) گفت‎ - ٩

ز آن ملك را نظام وازین عهد رابقا ز آن دوستان بفخرو آزین د«شمنان شمان.»

« لفت فری ۰.۳۸۸ ۷ -ماضی از «شمایدن» .

شماره سم اول ۳ شمار (ه.م.)
```


## [2026-09-06T20:57:31.375Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && grep -n \"شمن\" BQT_v3_pages.txt | head -30",
 "description": "Grep BQT v3 for shaman"
}
```


### [2026-09-06T20:57:31.430Z] TOOL RESULT

```
31:د انشمند محتر ,آقای‌د کترحمد معین‌استاد د انشگاه تهران
83:‏آقای سهرآب بتلی‌والا از ‎QUIT ZI‏ داشمند پارسی حند مقیم بمبئی بادداشتی شامل‌لفات
94:‏در خالمه , ‎ob‏ دیگر ازخوانند کان ادیپ ودانشمند درخواست دارد که اطلاعات خودارا
665:دشمنات هستمند و مبتلا وممتحن دوستاات شادمان وشادکام وشادخوایب
2241:بی‌خبر وغافل که درشب برس دشمن برند.
2310:‎cot oly‏ بردن ‎ath‏ برسر دشمن ‎SiGe‏
2788:تخت بر دن‌باشدبر سرد شمن چنا که غاف لو بیخبر باشد.
3010:این ‎col cate cal‏ اما نه مانندلفات کیی (بوزینه) وشکر وشمن وچندن (سندل) که از زمان
3064:‏- و بهندی دشمن را کویند - و بقتح اوژوثانی
4928:‎ath‏ همچو دشمن شکر یعنی دشمن شکن ۸ -
4930:‎oF‏ و دشمن بشکن ‎A‏ - وبا ثالی مشددسیخول
5174:شنوبدن ۰ ‎ines‏ شکار کردن و شکستن دشمن
5833:را بجالب دشمن اندازند*٩‏ - ومیوه‌ای باشد گرد
6252:شمنان = ‎ch‏ اول و ثالی بر وزن
6256:سرطان » جمع شمن امت که بت پرستان‌باشد-
6266:شمنده ۲ = بنتح اول بروزن(۱)زشده ,
6311:۴ - بماشقی چومن‌ایزد لیافرمد شمن
6435:عربی ۷ - ‎yee‏ دشمنی کردن‌باشدودشن‌داشتن
6510:۴ - رك : شمیدن , شمند . فی : ساسکریت 8818 ( مشوش شدن . آشفتن )
6586:ز آن ملك را نظام وازین عهد رایقا 5 ‎OT‏ دوستان بفخرو ازین دشمنان شمان.»
7709:پشت فروچفته(خفته . دهضدا) چوپشت شمن.
10227:رسولان شاه نیز در کرد ‎OT‏ بود که هربك عصابی دردست داشت . دراینکنبد بفرمان دشمن ‎Nad‏
12284:‏دشمن آندازند ۴ - و بمعنی کرم شب اب‌هم‌آعده
13880:باشد - وقهرآلود و خشمناك را نیز گویند ‎٩‏ ؛
14056:خشمناله شدن وقه رآ لود گردیدن باشد .
14187:خشمناه وقپرآلود وفمگن باشد .
14221:‏دشمن خوش را بری فرمان
14328:‏* غرهیدن - بقتح اول وپنجم؛ بمعتی خشمنال و کینهور شدن. ظ . مصحفب «غزمیدن»
16157:‏دولشت‌باد حریف (حریق.دهشدا)» دشمنت‌فيشه ونال.»
17015:قلمه و حصار گذارندتا چون دشمن ‎sls‏ حصار(4)
```


## [2026-09-06T20:57:36.248Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && sed -n '6230,6320p' BQT_v3_pages.txt; echo \"=== nearest page tags\"; awk 'NR>=6100 && NR<=6330 && /pdf page/ {print NR\": \"$0}' BQT_v3_pages.txt",
 "description": "Read BQT v3 around shaman entry"
}
```


### [2026-09-06T20:57:38.709Z] TOOL RESULT

```
تای فرشت )0( ‎e‏

‏شملیز ۰۷ بر وزن پرهیز » بمعنی

‏آمده است .

‏(۳) چك : بوزن .

‏۴ شفند (هم.) ‏ شماغنده

‎= Cpe) pale alee ‏ار‎

‎Cee) ‏شنبلیله‎ (pal ‏دنبلید‎ ٩

‏* همعدان - از : شمع ‎Obs)‏ ( پونده‌کان وظرف ] ؛ معرب آن ‎jl‏ شمعدان
جمم شمعدانات رشماءدیندزی چ ۱ص ۰۷۸۸ «تفی»۰ ‎AT‏ که درآن شمم راجا ‎radiates‏

[pdf page 83]
شملید است که حلبه وشبلیله باشد .
شم. ۱
کوند ۴ .

شمنان = ‎ch‏ اول و ثالی بر وزن

* بر وزن چمن » بت پرست زا

سرطان » جمع شمن امت که بت پرستان‌باشد-
وکی را یز کوبند که بسبب دوبدن یا تلنگی
با برداشتن باری‌شس ‎EF‏ پی‌دربی میزده داشد ۴
وفراش وباط بز رکه رالیزگویند.

شهفك = بر وزن کمند » بمعنی بهوش
ویهوشی باشد ۴ - و پممنی برحه و ‎UL‏ کنند
و بترسند و برمند هم گفته اند ۵ - و به‌عنی
بهبودی هم بنظر آمده است.

شمنده ۲ = بنتح اول بروزن(۱)زشده ,
‎the pe‏ و دلاور و پپلوان را کوند ۷ -
و بیهوش شده - و بیم زده - و پوننده را ‎ph‏
‎ee‏

شمول - باو اومجهول بر وزن قبول «
پیمنی جممیت وسامان وسکون وآرام باشد.

(۱) چك : بوزن .

سک

شمه = اول وفتح الی * درشیر
و قیماق راکویند ۵ - و چربی شیر و پثیر را
یز کفته اند , و با تشدید ثالی هم ‎otk‏ معنی
آمده است - و بفتح اول وثالی مخفف» شیریرا
کویند که اثر آن در سر ‎Obs‏ پیش از ‎ASST‏
‏بدوشند ظاهر باشد وبی دوشیدن قطره قطره حم
برآید - ویفتح اول ونالی ‎ode‏ درعربی بممنی
کم و ‎Sal‏ باشد - ومطلق بوی را ی زکفته اند
خواه بوی کل و خواء بوی چیزی دیگر ‎wath‏
‏شمی ‎٩‏ » بنتح اول بر وزن کمی »
بمعنی رمی باشد که از رمیدن است و بمعنی
درحه وافغان کنی- ومتنفر(۲)شوی - و بترسی-
‎oo Saal,‏ هم کفته اند ۰

شمید ۱۰

2 بر وزن رسید ۰ بمعنی
بیهوش باشد - و بمعنی بیپوش گردید - وآشفته
شد - و هراسید - و متنفر و ‎pat‏ زده گشت -
و رمید هم گفته اند . و این لفظ را بدبر وجه
استممال کندد : اول با لفط شمیده که شمید
و شمیده باشد ۱۱ ‎om‏ که مذ کورشد ودریم

(۷) چش : ومتفرق -

۱ - دز اوراق مالوی (بپارتی) ‎shmn‏ (ازساس‌کربت 5۲210202 راهب بودابی) :
‎Henning, A list of Middle Persian...,BSOS,IX,1,p. 88.‏
«*سرمته » در ساسکریت کی است که ‎yale‏ کسان خود را ترك کوید و در خلوت

بررباضت‌وعبادت گذراند و بعبارت ‎gir So‏ زاهد وتاركدنیا. درزبان ۳۵ که بکی‌از لهجه‌های
سالسکریت است و قدیمترین و معتبرتریین کثب دینی بودائیان جنوبی ‎oth‏ زبان درشته شده
این ‎ak‏ 521080 آمده است «یشتها ‏ ص ‎٩۳۷-۳۹‏ خود بودارا معاصران وی«سرمته کوقمه ©
‎LET)‏ مرتاض ) می ‎ata‏ «یشتها ۷ س ۳۰ ‎٩‏ .
۴ - بماشقی چومن‌ایزد لیافرمد شمن
« معزی لشابوری ‎TENT‏ +
۴ -رك :شم ‎Saez)‏ -

بدلبری چونو کیتی لپرورید صنم.

۴ - بان معنی مصحف «شمان» (۶ م.) ورك : ۱2۱۲۹۷ -
6 رك : شمیدن . ‎٩‏ اسم فاعل ازه‌شمیدن»
۲ - باين معنی ازدساتیر ‎eos piles Kin br‏ .

=== nearest page tags
6143: [pdf page 82]
6247: [pdf page 83]
6329: [pdf page 84]
```


## [2026-09-06T20:57:53.854Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && grep -n \"شماغنده\\|شمائیف\" BQT_v3_pages.txt | head; echo \"=== tags 6050-6250\"; awk 'NR>=5900 && NR<=6260 && /pdf page/ {print NR\": \"$0}' BQT_v3_pages.txt; echo \"=== ocr cache\"; ls /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/ 2>/dev/null | head -20",
 "description": "Locate BQT printed page for shaman"
}
```


### [2026-09-06T20:57:55.502Z] TOOL RESULT

```
6180:‎ode‏ بعنی شماغنده است که چیزهای بد بو
6238:‏۴ شفند (هم.) ‏ شماغنده
6542:شماغنده ۴ » با غن نقطددار بر وزن
=== tags 6050-6250
5965: [pdf page 80]
6052: [pdf page 81]
6143: [pdf page 82]
6247: [pdf page 83]
=== ocr cache
0001.png
0001.txt
0049.png
0049.txt
103.vision.txt
1219.png
1219.txt
1219.vision.txt
1223.png
1223.txt
1225.png
1225.txt
1225.vision.txt
1226.png
1226.txt
1261.png
1261.txt
1272.png
1272.txt
1275.png
```


## [2026-09-06T20:58:03.677Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && awk 'NR>=6247 && NR<=6900 && /pdf page/ {print NR\": \"$0}' BQT_v3_pages.txt; echo \"=== which pdf page is BQT:1296\"; python3 -c \"\nimport json,sys\nd=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'))\nprint(json.dumps(d['BQT'].get('scans'),ensure_ascii=False)[:2000])\nprint(d['BQT'].get('page_offset'))\n\"",
 "description": "Find BQT page mapping"
}
```


### [2026-09-06T20:58:05.158Z] TOOL RESULT

```
6247: [pdf page 83]
6329: [pdf page 84]
6414: [pdf page 85]
6471: [pdf page 86]
6527: [pdf page 87]
6593: [pdf page 88]
6683: [pdf page 89]
6759: [pdf page 90]
6848: [pdf page 91]
=== which pdf page is BQT:1296
[{"volume": "3", "file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf", "first_printed": 1208, "last_printed": 1925, "pdf_offset": -1205, "page_map": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pagemap.json", "lang": "fas", "ocr_text": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt", "ocr_note": "689/721 pdf pages OCRed (tesseract fas+eng, mediocre); pages are separated by form-feeds and tagged [pdf page N]; remaining pages via tools/ref_page.py"}, {"volume": "4", "file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf", "first_printed": 1920, "last_printed": 2475, "pdf_offset": -1917, "lang": "fas", "offset_note": "printed = pdf+1917, checked at pdf 150 and 500", "ocr_text": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt"}, {"volume": "5", "file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf", "first_printed": 1, "last_printed": 290, "pdf_offset": 5, "lang": "fas", "note": "vol 5 = ta'liqat (addenda) with its own pagination 1-290; cite as BQT5:<page>. Plain BQT:<n> with n<1208 refers to vols 1-2 (OCR text files BQT_v1_pages.txt / BQT_v2_pages.txt), not to this scan.", "ocr_text": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt", "requires_volume": true}]
vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').
```


## [2026-09-06T20:58:26.728Z] TOOL CALL #32: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:1296 --pdf-page 83 --image 2>&1 | tail -15",
 "description": "Render BQT vol3 pdf page 83"
}
```


### [2026-09-06T20:58:28.302Z] TOOL RESULT

```
۴ - (عر) ۶ شمال دست چپ است ضد دست راست ... وشمال بفتح و کسر اول بادست
که میوزد از روبروی حجریا آن بادستکه پیش میآید نرا از دست راست تو وتو پیش آبندة باو
ودرست وسحیح آنت که جای وزیدن ارمپان برآمدن آفتاب وبنات اللمش با از جای برآمدن

فش است تاحای فرو رفتن سرطایر» «شرح فاموی» . ‎٩‏ - آسم فاعل وحال‌ازهشمیدن» .

: ‏شمان . بانگه کربهٌ دمادم در کلو باشد » عنصری (بلخی) گفت‎ - ٩

ز آن ملك را نظام وازین عهد رابقا ز آن دوستان بفخرو آزین د«شمنان شمان.»

« لفت فری ۰.۳۸۸ ۷ -ماضی از «شمایدن» .

شماره سم اول ۳ شمار (ه.م.)
```


## [2026-09-06T20:58:35.469Z] TOOL CALL #33: Bash

```json
{
 "command": "for p in 1297 1298; do echo \"##### $p\"; timeout 600 python3 tools/ref_page.py BQT:$p 2>&1 | head -25; done",
 "description": "Fetch BQT pages 1297 and 1298"
}
```


### [2026-09-06T20:58:47.098Z] TOOL RESULT

```
##### 1297
REF: BQT:1297  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 88  OCR-lang: fas

-۱۲۹۳- :مش
که ماضی رمانیدن است - و بهمنی آشفته کرد- ! وكوچك راگویند - و آبگیر و «رجاکه آب
و آشفته شد - و ترسانید - و ترسید- وپربشان | امتاده باغد ۴ - و جایی از زمین وکوه‌که آب
ساخت - وپربشان شد - وبیهوش کرد- وبیهوش | باران در آن جمع شود - وپای درخت را یز
کردید هم گفته‌اند - و بمعنی نف برنفی‌افتادن | کوبند که آب درآن استاده باشد ؛ و بی‌آب
از تشنگی بعنی پی درپی و دم بدم شس‌کشیدن | کم واندك را شم رکویند که درهرجای از روی
هم آمد. است و شمافیدن مسدرآن باشد. | زمین و جوفها و شکافهای س وپاهای درخت

وامثال آن بایستد - وجوی كوچك وخردوجدول

سا < بنج او بروفت خسن | آب را نیز کنتهاد ونورد آپ را هم میگویند

جمع شمال است ثه بمعنی خوبی داث وسرشت ۱ ان - و نمع قماد نظر آمده‌است
بیگر - و خمانهای پا کیزه و اغلاتر نو سره اش ه» هم بنظر امه

شد ., ده هده اعت
و این امم است - و رارق 0 باشد -وشاخ شمرش < بم اول وثانی وکسر را
لو رسته و شاخ خرد درخت - و جوی کوچك و سکون شین قرشت , بمعنی فرض و تقدرباشد
وجدول آب و گروه مردم اند که را نی زگفته‌اند. رجا سل کنند که عر بان بالفرض‌والتقدین

شد
شمپودی ۴ - با بای فارسی بر وزن شمسا ۷ - باسین بی قطه بروزن‌سدا,
راجوری » بمعنی قری (۱) باشد که نقیض‌طبعی بلقت زند و پازید (۴) بمعثی نور باشد. که آن
##### 1298
REF: BQT:1298  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 89  OCR-lang: fas

شمفاد -۱۹-
شمخاد ه بکراول‌بروزن بهزادءممروف وبعربی آذان‌الفار کوبند .
است. وآن درختی باشد که چوب آن در غات شمشک * - بکر اوز و فتح نانی
سختی و ملائی بود و از آن چیزها سازند ۱ - | واسکون ثالك‌وکاف , بلفت زند وپازند(۱) کاجد
و مرزنگوش را نی ز گوبند » وآن نوعی ازریحان | راکوبند و آن دانه‌ای باشد معروف که(؟)ازآن
باشد در غایت سبزی و خوشبویی ؛ و بفاح اول | روغن کیرند.
م آمده است - و کنایه از فامت خوبان هم شمذور * بنم اول بروزن پرزورء بلفت
هت , کیلانی رستنیی باشد که برکه آن ببر کهسمتر
شمخار - بکراول‌برون یار شاخهای ماند و در آشپای ترش «داخل کنند و روغن‌آن
تازه را گوبند که از درخت شمعاد برآید وب رکه درد گوش را تافعم است.
آن درمایت سبزی و لطافت وطاراوت و نزاکت شمشیر ۹ « بفتح اول بروزن نخجیر .
باشد و ازغایت با ز کی میل بجانب زمین کندلهذا معروفت و وجه تمه آن شم شیر است که‌دم
شعر!آ ترا پزلف خوبان تشبیه کرده‌اند ۲ ,وبعضی
کوبند درختی است مانند شمشاد وآاهم پیوسته
سبز وخرم میباشد وازچوب آلهم چیزهامیتراشند ی موی
وی دیگر کوبند شمشاد و شمشار هر دو یکی | ۳
است اختلاف در دال ورا شده است ۳ ۰
شمشدر ۴ « با رال و رای بی شله شمشیر
بروزن ستمگر , بلفت زند وپازند (۱)سیر براور | شیر وناخن شیر باشد چه شم بممنی دم و ؛اخن
از راکویند . هردوآمده است ۷ - وروشنایی صبح‌وآفتاب‌رانیز
شمشُر ! - با رای بی‌قطه پروزن غمزداء گوبند . ۹ 9
رستنیی باشد دوابی و آنرا مرزاگوش خوانند شمشی ر گوشتین « بممنی تبغ کوشتین
() چك: ژند ویاژند . (۷) چش: و .
```


## [2026-09-06T20:59:03.895Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && for w in شمپودی شمشاد شمخار شملیز; do echo \"== $w\"; grep -n \"$w\" BQT_v3_pages.txt | head -3; done",
 "description": "Align BQT text file tags with printed pages"
}
```


### [2026-09-06T20:59:05.664Z] TOOL RESULT

```
== شمپودی
== شمشاد
6692:تازه راکویند که از درخت شمشاد برآبد وب رکه
6696:گویند درختی است مالند شمشاد وآلهم پیوسته
6698:ویضی دیگر کویند شمشاد و شم‌شار هر دو ,یکی
== شمخار
== شملیز
6232:‏شملیز ۰۷ بر وزن پرهیز » بمعنی
```


## [2026-09-06T20:59:20.987Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && pdftoppm -f 83 -l 83 -r 200 -png -singlefile /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf bqt_v3_83 && python3 -c \"\nfrom PIL import Image\nim=Image.open('bqt_v3_83.png'); print(im.size)\nim.crop((0,0,im.size[0],220)).save('bqt83_head.png')\n\"",
 "description": "Render BQT v3 pdf page 83 header"
}
```


### [2026-09-06T20:59:23.726Z] TOOL RESULT

```
(1100, 1698)
```


## [2026-09-06T20:59:26.115Z] TOOL CALL #36: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bqt83_head.png"
}
```


### [2026-09-06T20:59:26.129Z] TOOL RESULT

```

```


## [2026-09-06T20:59:42.557Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '15575,15595p' MON_part1.txt; echo \"=== kelinik ctx\"; sed -n '32620,32640p' MON_part1.txt",
 "description": "Read Mo'in eqlim and kelinik contexts"
}
```


### [2026-09-06T20:59:42.622Z] TOOL RESULT

```
فارسی «دست کم) مستعمل است. 
اتلیت: و21 [ع.] (مسص جه.) 
اقل‌بودن» کم بودن. قسمت کمتر» بخش 
کمتر) مق. اکثربت. (اصط.) گروهی از افراد 
یک کشور با یک شهر که از لحاظ دین و 
مذهب يا نوا از اکثریت ممتز باشند. 
اقلید: ۱14 [معر.] (ا.) کلید» مقلاد. 
اتلیم: «آه [سعر.] (.) ناحیه‌ای از کرة 
زمین» قطعه‌ای از کر ارض که از حیث آب 
و هوا و اوضاع طبیعی از قطعات دیگر ممتاز 
باشد. قدما زمین ت_ به هفت اقلیم تءه 
کرده‌اند. کشور» مملکت. ولایت» ج. قلیم. 
اقلیمیا": 2 [- قلیمیا» معر .] (ا.) خلطی 
که پس از گداختن طلا و نقره و دیگر فلزات 
در خلاص ماند و آن شامل انواع است: 
فضی (نقره‌ای)» ذهبی (طلایی)» نحاسی 
(مسی)» معدنی ( کانی). 

اتماع: قصو [ع.] (مص ع.) خوار کردن» 
حقیر گردانیدن کسی را. شکستن» سغلوب 
کردن. راندن» دفع کردن. 
=== kelinik ctx

پلیس: 215 (۱.) (بنا.) ناهمواری. 

ئُلیس: »۲01 (.) شهربانی» نظمیه. پاسبان» 
آژان» عسس » مسحتسب. اداره تاش 
سرکلانتری (فره.) پلیس مسخفی: کا رآ گاه 
(فر ه.) 

پلیسه: 6 (ص.) چیندار؛ بانور: دامن 
بلی کلینیک: ۲ اه (امر.) (بز.) 
مطبی که دارای درمانگاه‌های مختلف است و 
درصورت لزوم‌امراض مختلف را در آنجا 
مورد مداوا قرار می‌دهند. 

پماد: 0 (.) (بز.) محصولات داروبی 
نرم که با مواد روغنی و نرم بی‌تفاوت و 
خنثی نظیر آکسونژ وازلین؛ لانولین» بیه و 
روغن زیتون مخلوط کنند و جهت استعمال 
خارجی مورد استفاده قرار می‌گیرد؛ مانند 
پماد اکسید دوزنگ یا پماد اکسیدژون 
دومرکور.
```


## [2026-09-06T20:59:44.476Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN climate\"; grep -n \"climate\" KLN_1966.txt | head -6; echo \"=== KLN climax\"; grep -n \"^climax\\|climax,\" KLN_1966.txt | head -6; echo \"=== KLN clinic\"; grep -n \"clinic\" KLN_1966.txt | head -6; echo \"=== KLN client\"; grep -n \"client,\" KLN_1966.txt | head -4",
 "description": "Grep Klein for climate/climax/clinic/client"
}
```


### [2026-09-06T20:59:44.578Z] TOOL RESULT

```
=== KLN climate
1345:fr.  ad-  and  clamare,  ‘to  cry  out’.  See  claim  and cp.  declaim,  exclaim,  proclaim,  reclaim, acclamation,  n.  —  L.  acclamatio,  gen.  -onis,  fr. acclamat-(um),  pp.  stem  of  acclamare,  ‘to  cry out  at’.  See  acclaim  and  -ation. acclimate,  tr.  and  intr.  v.  —  F.  acclimater,  fr.  d (fr.  L.  ad),  ‘to’,  and  climat,  ‘climate’.  See  a  and climate.
1346:Derivatives:  acclimate-ment,  n.,  acclimat-ion,  n. acclimatize,  tr.  and  intr.  v.,  to  acclimate.  —  See acclimate  and  -ize.
7922:climactic,  adj.,  pertaining  to  a  climax.  —  Irreg¬ ularly  formed  fr.  Gk.  xXijxa^,  gen.  xX!|j.xxop, ‘ladder’.  See  climax  and  -ic. climate,  n.  —  F.  climat,  fr.  L.  clima,  gen.  -atis, ‘region,  climate’,  fr.  Gk.  xXiua,  gen.  xX((J.<xt oq, ‘inclination,  slope,  region’,  from  the  stem  of xXfvsiv,  ‘to  cause  to  slope,  bend’.  See  clinical and  cp.  clime,  which  is  a  doublet  of  climate.  Cp. also  climax,  acclimate,  acclimatize.
7923:Derivatives:  climate,  intr.  v.,  climat-ic,  climat- ic-al,  adjs.,  climat-ic-al-ly,  adv. climatography,  n.,  description  of  climates.  — Compounded  of  Gk.  xXijxa,  gen.  x.Xip.xTop, ‘climate’,  and  -ypoctpia,  fr.  ypdhpEiv,  ‘to  write’. See  climate  and  -graphy.
7924:Derivative:  climatograph-ical,  adj. climatology,  n.,  the  scientific  study  of  climates.  — Compounded  of  Gk.  xX((ca,  gen.  xXi|jlocto<;, ‘climate’,  and  -Xoyix,  fr.  -Xoyop,  ‘one  who  speaks (in  a  certain  manner);  one  who  deals  (with  a certain  topic)'.  See  climate  and  -logy. Derivative:  climatolog-ist,  n. climax,  n.  L.,  fr.  Gk.  xXipuxi;,  ‘ladder’,  lit. ‘something  sloping,  something  leading  up  by  de¬ grees’,  from  the  stem  of  xXNs tv,  ‘to  cause  to slope,  bend’.  See  clinical  and  cp.  ladder. Derivative:  climax,  intr.  and  tr.  v. climb,  intr.  and  tr.  v.  —  ME.  climben,  fr.  OE. climban,  rel.  to  OHG.  klimban,  MHG.  klimben, klimmen,  G.  klimmen,  MLG.  klimmen,  klim- meren,  and  in  gradational  relationship  to  ME. clambren,  clameren,  ‘to  climb’.  The  original meaning  of  these  words  was  ‘to  stick  on  to’. They  are  rel.  to  clam,  ‘to  smear’,  clammy,  cleave, ‘to  stick’,  and  further  to  clay  (qq.v.) Derivatives :  climb,  n.,  climb-able,  adj.  (a  hybrid), climb-er,  n.
7925:clime, n.,  i)  a  region;  2)  climate.  —  L.  clima.  See climate.
=== KLN climax
2970:anticlerical,  adj.  —  Formed  fr.  anti-  and  clerical Derivative:  anticlerical-ism,  n. anticlimax,  n.,  the  opposite  of  climax  (rhet.)  — Coined  by  Alexander  Pope  (1688-1744)  fr.  anti- and  climax.
4547:bathos,  n.,  anticlimax,  a  descent  from  the  sublime to  the  ridiculous.  —  Gr.  paffo?.  ‘depth’,  rel.  to paffu?,  ‘deep’,  and  prob.  also  to  pcv&o?,  ‘depth’ — which  seems  to  have  been  formed  on  analogy of  nsvffo?,  ‘grief’ — and]  to  pijacia  (for  *pa&-
7922:climactic,  adj.,  pertaining  to  a  climax.  —  Irreg¬ ularly  formed  fr.  Gk.  xXijxa^,  gen.  xX!|j.xxop, ‘ladder’.  See  climax  and  -ic. climate,  n.  —  F.  climat,  fr.  L.  clima,  gen.  -atis, ‘region,  climate’,  fr.  Gk.  xXiua,  gen.  xX((J.<xt oq, ‘inclination,  slope,  region’,  from  the  stem  of xXfvsiv,  ‘to  cause  to  slope,  bend’.  See  clinical and  cp.  clime,  which  is  a  doublet  of  climate.  Cp. also  climax,  acclimate,  acclimatize.
7924:Derivative:  climatograph-ical,  adj. climatology,  n.,  the  scientific  study  of  climates.  — Compounded  of  Gk.  xX((ca,  gen.  xXi|jlocto<;, ‘climate’,  and  -Xoyix,  fr.  -Xoyop,  ‘one  who  speaks (in  a  certain  manner);  one  who  deals  (with  a certain  topic)'.  See  climate  and  -logy. Derivative:  climatolog-ist,  n. climax,  n.  L.,  fr.  Gk.  xXipuxi;,  ‘ladder’,  lit. ‘something  sloping,  something  leading  up  by  de¬ grees’,  from  the  stem  of  xXNs tv,  ‘to  cause  to slope,  bend’.  See  clinical  and  cp.  ladder. Derivative:  climax,  intr.  and  tr.  v. climb,  intr.  and  tr.  v.  —  ME.  climben,  fr.  OE. climban,  rel.  to  OHG.  klimban,  MHG.  klimben, klimmen,  G.  klimmen,  MLG.  klimmen,  klim- meren,  and  in  gradational  relationship  to  ME. clambren,  clameren,  ‘to  climb’.  The  original meaning  of  these  words  was  ‘to  stick  on  to’. They  are  rel.  to  clam,  ‘to  smear’,  clammy,  cleave, ‘to  stick’,  and  further  to  clay  (qq.v.) Derivatives :  climb,  n.,  climb-able,  adj.  (a  hybrid), climb-er,  n.
7932:clinical,  adj.  - —  Formed  with  adj.  suff.  -al  fr.  L. clinicus,  fr.  Gk.  xXmx6s,  ‘a  physician  who  at¬ tends  patients  in  their  beds’,  from  the  adjectiva xXIvixo?,  ‘pertaining  to  a  bed’,  fr.  xXfvtr),  ‘bed’, which  is  rel.  to  xXtueiv,  ‘to  cause  to  slope,  slant, incline’,  xXlptoc,  ‘inclination,  slope,  region’,  xXt- |xa£,  ‘ladder’,  xXtpaxTrip,  ‘rung  of  a  ladder’, xXTt6<;,  xXecru?,  ‘slope,  hillside’,  fr.  I.-E.  base *klei-,  ‘to  incline,  lean’,  whence  also  L.  -clinare (with  the  exception  of  the  pp.  clinatus,  occur¬ ring  only  in  compounds),  ‘to  bend,  turn’,  clivus, ‘slope,  hill’,  clitellae  (dimin.  of  *clitra,  for *kleitrd),  ‘a  packsaddle’,  Umbr.  kletram  (acc.), ‘litter,  bier’,  OI.  srayati,  ‘leans’,  sritah,  ‘leaning’, Lith.  slyti,  ‘to  slope’,  slieti,  ‘to  lean’,  slaitas, ‘declivity,’  sleivas,  ‘bandy-legged’,  Ofr.  cloin, ‘crooked,  wrong’,  Mir.  clithar,  ‘hedge’,  W. dedren,  ‘enclosure’,  Mir.  cle,  W.  cledd,  Co. cledh,  Bret,  kleiz,  ‘left’,  lit.  ‘slanting,  oblique’, Mir.  fo-chla ,  W.  go-gledd,  ‘north’,  lit.  ‘left’  (for sense  development  cp.  Heb.  semdl,  Arab. sham'dl,  shimdl,  ‘left;  north’),  Arm.  learn  (gen. leriri),  ‘mountain’,  Goth,  hlaiw,  ‘grave,  tomb’, OE.  hlxw,  hlaw,  ‘mound,  hill;  cave’,  OE.  hlinian, ‘to  lean’.  See  lean,  ‘to  incline’,  and  cp.  words there  referred  to.  Cp  also  acclivity,  aclinic,  anti¬ clinal,  clement,  client,  climacterium,  climate, climax,  clinamen,  clino-,  clitellum,  clition,  clivus, declension,  decline,  declivity,  diclinous,  enclitic, heteroclite,  incline,  isoclinic,  microcline,  mono- clinal,  pericline,  recline,  synclinal,  triclinium. I.-E.  base  *klei-  is  an  enlargement  of  base  *kel-, for  the  derivatives  of  which  see  heel,  ‘to  lean’ Derivative:  clinical-ly,  adv clink,  intr.  and  tr  v.  —  Prob.  fr.  MDu.  clinken (Du.  klinken),  ‘to  sound,  tinkle’,  which  is  rel.  to MLG.  klingen[  whence  ON.  klingia,  Dan .klinge, Swed.  klinga],  OHG.klingan,MHG.,G.klingen, ‘to  sound,  tinkle’;  of  imitative  origin.  Clink  is related  to  clank;  for  the  thinning  of  a  to  i  cp. click  and  clack.  Cp.  dough.
20992:lad,  n.  —  ME.  ladde,  ‘a  youth,  manservant’;  of unknown  origin, ladanum,  n.  —  L.  See  labdanum. ladder,  n.  —  ME.  laddre,  fr.  OE.  hlxder,  hlzedder, rel.  to  OFris.  hledere,  MDu.  ledere,  leder  (Du. leer),  Du.  ladder,  OHG.  leitara,  MHG.  leitere, leiter,  G.  Letter,  ‘ladder’,  fr.  I.-E.  base  *kli-,  ‘to slope,  incline’,  whence  also  Goth,  hleipra,  ‘tent’. See  lean,  v.,  and  cp.  climax,  clinical.
=== KLN clinic
1460:aclinic,  adj.,  not  dipping  (said  of  a  magnetic needle).  —  Formed  with  suff.  -ic  fr.  Gk.  axXivrjt;, ‘bending  to  neither  side’,  fr.  a-  (see  priv.  pref. -a)  and  xXtveiv,  ‘to  incline’.  See  clinic, acme,  n.,  the  highest  point.  —  Gk.  axiri),  ‘point, edge;  the  highest  point  of  anything,  the  flower, prime  of  man’s  age’,  rel.  to  ax?),  ‘point’,  and
2882:anorthoclase,  n.,  a  triclinic  potash-soda  feld¬ spar.  _  Coined  by  the  German  mineralogist Harry  Rosenbusch  (1836-1914)  in  >885  fr-  priv. pref.  -an  and  orthoclase  (q.v.) anosmia,  n.,  lack  of  the  sense  of  smell  (med.)  — Medical  L.,  fr.  priv.  pref.  an-  and  Gk.  bmirr ‘smell,  odor’.  See  osmium  and  -ia. another,  adj.  and  pron.  —  Formed  fr.  the  indef. article  an  and  other.
2971:anticlinal,  adj.,  leaning  in  opposite  directions.  — Formed  fr.  anti-  and  Gk.  y.Xtvav,  ‘to  cause  to slope’.  See  clinical.
7890:clement,  adj.  —  L.  clemens,  gen.  -entis,  ‘mild, calm,  soft,  gentle,  merciful,  forbearing,  indul¬ gent’,  for  *kteyomenos,  lit.  ‘inclined’,  a  parti¬ cipial  form  of  base  *klei-,  ‘to  lean,  incline’, whence  also  OI.  srayate,  ‘leans’,  srayamanah, ‘leaning’,  Gk.  xXfveiv,  'to  cause  to  slope,  slant’, L.  -clinare  (found  only  in  compounds),  ‘to  bend, turn'.  See  clinical  and  cp.  words  there  referred to.  For  the  participial  suff.  -menos  see  alumnus. For  the  sense  development  of  L.  clemens  (fr. base  *klei-,  ‘to  lean,  incline’),  cp.  the  E.  adj.  in¬ clined,  in  the  sense  ’disposed  favorably’.
7916:Derivatives:  click,  n.,  click-er,  n.,  click-y,  adj. client,  n.  —  F.,  fr.  L.  clientem,  acc.  of  cliens, ‘retainer,  follower,  dependent’,  lit.  ‘one  who leans  on  another’,  fr.  I.-E.  base  *klei-,  ‘to  lean, incline’,  whence  also  L.  -clinare,  ‘to  bend,  turn’. See  clinical  and  cp.  words  there  referred  to.  The usual  derivation  of  L.  cliens  from  the  stem  of cluere,  ‘to  be  named’,  is  erroneous. Derivatives:  client-age,  n.,  client-al,  adj.,  cheat¬ ed,  adj.,  client-ry,  n.
7922:climactic,  adj.,  pertaining  to  a  climax.  —  Irreg¬ ularly  formed  fr.  Gk.  xXijxa^,  gen.  xX!|j.xxop, ‘ladder’.  See  climax  and  -ic. climate,  n.  —  F.  climat,  fr.  L.  clima,  gen.  -atis, ‘region,  climate’,  fr.  Gk.  xXiua,  gen.  xX((J.<xt oq, ‘inclination,  slope,  region’,  from  the  stem  of xXfvsiv,  ‘to  cause  to  slope,  bend’.  See  clinical and  cp.  clime,  which  is  a  doublet  of  climate.  Cp. also  climax,  acclimate,  acclimatize.
=== KLN client
7916:Derivatives:  click,  n.,  click-er,  n.,  click-y,  adj. client,  n.  —  F.,  fr.  L.  clientem,  acc.  of  cliens, ‘retainer,  follower,  dependent’,  lit.  ‘one  who leans  on  another’,  fr.  I.-E.  base  *klei-,  ‘to  lean, incline’,  whence  also  L.  -clinare,  ‘to  bend,  turn’. See  clinical  and  cp.  words  there  referred  to.  The usual  derivation  of  L.  cliens  from  the  stem  of cluere,  ‘to  be  named’,  is  erroneous. Derivatives:  client-age,  n.,  client-al,  adj.,  cheat¬ ed,  adj.,  client-ry,  n.
7932:clinical,  adj.  - —  Formed  with  adj.  suff.  -al  fr.  L. clinicus,  fr.  Gk.  xXmx6s,  ‘a  physician  who  at¬ tends  patients  in  their  beds’,  from  the  adjectiva xXIvixo?,  ‘pertaining  to  a  bed’,  fr.  xXfvtr),  ‘bed’, which  is  rel.  to  xXtueiv,  ‘to  cause  to  slope,  slant, incline’,  xXlptoc,  ‘inclination,  slope,  region’,  xXt- |xa£,  ‘ladder’,  xXtpaxTrip,  ‘rung  of  a  ladder’, xXTt6<;,  xXecru?,  ‘slope,  hillside’,  fr.  I.-E.  base *klei-,  ‘to  incline,  lean’,  whence  also  L.  -clinare (with  the  exception  of  the  pp.  clinatus,  occur¬ ring  only  in  compounds),  ‘to  bend,  turn’,  clivus, ‘slope,  hill’,  clitellae  (dimin.  of  *clitra,  for *kleitrd),  ‘a  packsaddle’,  Umbr.  kletram  (acc.), ‘litter,  bier’,  OI.  srayati,  ‘leans’,  sritah,  ‘leaning’, Lith.  slyti,  ‘to  slope’,  slieti,  ‘to  lean’,  slaitas, ‘declivity,’  sleivas,  ‘bandy-legged’,  Ofr.  cloin, ‘crooked,  wrong’,  Mir.  clithar,  ‘hedge’,  W. dedren,  ‘enclosure’,  Mir.  cle,  W.  cledd,  Co. cledh,  Bret,  kleiz,  ‘left’,  lit.  ‘slanting,  oblique’, Mir.  fo-chla ,  W.  go-gledd,  ‘north’,  lit.  ‘left’  (for sense  development  cp.  Heb.  semdl,  Arab. sham'dl,  shimdl,  ‘left;  north’),  Arm.  learn  (gen. leriri),  ‘mountain’,  Goth,  hlaiw,  ‘grave,  tomb’, OE.  hlxw,  hlaw,  ‘mound,  hill;  cave’,  OE.  hlinian, ‘to  lean’.  See  lean,  ‘to  incline’,  and  cp.  words there  referred  to.  Cp  also  acclivity,  aclinic,  anti¬ clinal,  clement,  client,  climacterium,  climate, climax,  clinamen,  clino-,  clitellum,  clition,  clivus, declension,  decline,  declivity,  diclinous,  enclitic, heteroclite,  incline,  isoclinic,  microcline,  mono- clinal,  pericline,  recline,  synclinal,  triclinium. I.-E.  base  *klei-  is  an  enlargement  of  base  *kel-, for  the  derivatives  of  which  see  heel,  ‘to  lean’ Derivative:  clinical-ly,  adv clink,  intr.  and  tr  v.  —  Prob.  fr.  MDu.  clinken (Du.  klinken),  ‘to  sound,  tinkle’,  which  is  rel.  to MLG.  klingen[  whence  ON.  klingia,  Dan .klinge, Swed.  klinga],  OHG.klingan,MHG.,G.klingen, ‘to  sound,  tinkle’;  of  imitative  origin.  Clink  is related  to  clank;  for  the  thinning  of  a  to  i  cp. click  and  clack.  Cp.  dough.
```


## [2026-09-06T21:00:13.344Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== MON kelinik variants\"; grep -n \"کلینیك\\|كلینیک\\|کلینیک\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt 2>/dev/null | head -10; echo \"=== PHD shaman\"; grep -n -i \"šaman\\|shaman\\|smn\\b\" PHD.txt PHD_mackenzie.txt | head -10; echo \"=== NYB\"; grep -n -i \"šaman\\|šmn\" NYB_vol2_glossary.txt | head -10",
 "description": "Grep MON, PHD, NYB"
}
```


### [2026-09-06T21:00:13.447Z] TOOL RESULT

```
=== MON kelinik variants
incoming/MON/MON_2vol_Adena_v2_djvu.txt:29969:اکثر در سیستم مون وکلینیکك متبلور می‌شود و 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:70416:سبز مون وکلینیک است. 
MON_part1.txt:32629:بلی کلینیک: ۲ اه (امر.) (بز.) 
MON_part1.txt:80374:متبلور را گویند که در سیستم منوکلینیک 
MON_part2.txt:29969:اکثر در سیستم مون وکلینیکك متبلور می‌شود و 
MON_part2.txt:70416:سبز مون وکلینیک است. 
=== PHD shaman
PHD.txt:671:yāsaman [y smn! | N ~] Jasmine. yask [ysk! | = M] illness, sickness. yasn [ysn' | = M] adoration, worship. yašt [yst! | = M] prayer, worship. yaštan, yaz- [YDBHWN-tn! < A ydbhwn, V dbh; уйт, yc- | M yz-] worship, celebrate, recite. ~Л&п : worship. yāt [yt! = Av. yáta-] a degree of sin. P yāwēd(ān) [5?*wyt(?*n)! | P y'wyd(?n)] always, eternally. yaz-, ~išn, v. ya&tan. yazd [yzdt! | M yzd, N ~] god, divinity. yāzdah [y'cdh | M y'zdh, N ~] eleven. yazdān [yzd’n'] (pl.) gods, spirits. yējdahr [ywid?sl | М ywjdhr] holy, pure. ~th: holiness, purity. yojdahrgar [ywsd’slkl] purifier. ~ih: purification, sanctification. убх [ywc | N ~] cheetah, hunting leopard.
PHD_mackenzie.txt:5690:yasaman (y)smn IN......,] jasmine.
=== NYB
1396:duš-kunišn [dwškwnšn'] of evil deed 752. duš-man [dwšmn'] hostile 825; enemy 414 (twice). 141-2, 6211, 63?5; coll. 249. 262°. 278.20.24, 297.19; pl. cas. obl. ~-an 6%. 3712, - Av. (753 sq.) duš-manah-; MPrth dwémn (S); MPrs ef dwšmny*dyh ‘hostil- ity’ (A-H I); Paz. NP dušman. Cf dušmen.
1996:hešm-maniha (hšmnyh"] in a rage 50?. — -man- < Av. (1126 sgg.) manah-, cf duš- man.
```


## [2026-09-06T21:00:15.400Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== CHEUNG sray\"; grep -n -i \"sray\\|\\*sray\" CHEUNG.txt | head -10; echo \"=== SOD shmn\"; grep -n -i \"šmn\\|šaman\\|šman\" SOD.txt | head -10; echo \"=== HRN shaman\"; grep -n -i \"šaman\\|schaman\\|samana\" HRN.txt HUB.txt | head -10",
 "description": "Grep Cheung, Gharib, Horn, Hübschmann"
}
```


### [2026-09-06T21:00:15.477Z] TOOL RESULT

```
=== CHEUNG sray
23230:*SANSKRIT: sray ‘to lean against’ (RV+) = EWAia II: 665 
23341:*MIDDLE PERSIAN: MMP sr’y-, BMP sl’d- /sray-/ ‘to sing’ || (+ *fra-) MMP frsy- ‘to 
23346:Caus.: pres. IND. 3pl. MMP sr’ynd’, sr'yynd, BMP sl’dynd /srayend/; Partic.: perf. pass. BMP slwt 
25748:*NEIR: Ishk. tsranj-/tsrayd- ‘to compress’, M. tro(n)jv-/tardyd- ‘to stretch’, Yi. 
35528:sI'd- /sray-/, 357 
48521:dsray-/dsrsd, 79 
51966:Sray, 355 
=== SOD shmn
=== HRN shaman
HUB.txt:2433:arm. Samanak 'Zeit, Alter, Gelegenheit*.
HUB.txt:2850:hemna-) yt. 13, 49 = skr. jijMsamana- (Idg. Forsch. L
```


## [2026-09-06T21:00:21.557Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '23200,23270p' CHEUNG.txt",
 "description": "Read Cheung sray entry"
}
```


### [2026-09-06T21:00:21.605Z] TOOL RESULT

```
(Y 65.11); Perf.: IND. 35р. ? YAv. sisraiia (Vyt 51); Partic.: pres. {2} med. YAv. apa.sraiiamna- (Yt 
13.26), fut. ҮАУ. sra@Siiant- (У 8.34), aor. med. Y Av. sraiiana- (V 3.29, Vyt 36), perf. pass. YAv. srita- 
(Е 531), YAv. apa.srita- (N 78), Y Av. nisrita- (N 10); Caus.: SUBJ. 2sg. YAv. nisraraiia (V 18.51) 


*srais 355 


*OLD PERSIAN: (+ ni-) niyagär- ‘to restore’ — Kent: 188b 

Caus.: impf. IND. 1sg. niyacarayam <n-i-¢-a-r-y-m> (DB 1.64) 

*MIDDLE PERSIAN: (+ *ni-) BMP ns’y /nisay/ ‘conveying, dispatch’ 

*KHOTANESE: Q LKh. ssaidä, assigned by Bailey (DKS: 412a f.) to *srai, has a 
different etymology, on which see *srai8. 

*CHORESMIAN: (+ *apa-) bs’ry- ‘to reject, decline’ = Samadi: 25 

*NWIR: Gz. särt, Siv. sid ‘staircase, ladder’ (< "OP" *¢(a)ita- < Ir. *sr(a)ita-) 

*NEIR: Pash. sal (m.) ‘stair (built of stone or earth)’, Yzgh. Хаа ‘ladder [pieced 
together]’ || (+ *us- ?) Pash. sayal/Sayam ‘to reject, repudiate’, ? Sh. soxis- ‘to slip’ 
(formally difficult), ? Sh. Хоу, Rosh. xüy, Bart. Xüy ‘moraine of large boulders’ || (+ 
*ui-) ? Pash. waxedal ‘to slip (from the hand)’, Sh. (Baj.) wixi(y)-/wixid, Rosh. 
wiXay-/wixid, Bart. wixi-/wixid, Yzgh. x"ay-/x'ad ‘to open, unlock’, Wa. 
WBIS(b1)y-/Wbis(o)n- ‘to untie, loose, release’. Ф As for Wa. wbis(bi)y-/wbris(o)n- cf. 
Steblin-Kamenskij 1999: 403: "We note that Wa. ъы$(ы)у- can go back 
phonetically impeccably to Old Ir. *ui-, *aua-srai(a)-". 

*SANSKRIT: sray ‘to lean against’ (RV+) = EWAia II: 665 

© This root has an impeccable IE etymology. 

«PIE *Klei- ‘to lean’ = LIV: 332 f. | Pok.: 601 f. 

*IE COGNATES: Gr. KAtivo ‘I lean’, Lat. clinare ‘to bow, to bend’, Lith. sliéti, OHG 


hlinén ‘to lean’, Engl. to lean, etc. 
*REFERENCES: EVP: 78, 79; EVS: 101a, 77a, 95, 104b; DKS: 412a f.; WIM II/2: 732; WIM III: 342; 
Werba 1997: 245 f.; Steblin-Kamenskij 1999: 334, 403 


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
```


## [2026-09-06T21:00:29.535Z] TOOL CALL #42: Bash

```json
{
 "command": "sed -n '1,40p' tools/fetch_source.py",
 "description": "Inspect fetch_source tool"
}
```


### [2026-09-06T21:00:29.574Z] TOOL RESULT

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


## [2026-09-06T21:00:34.121Z] TOOL CALL #43: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%E1%B8%B1ley-\" \\\n \"https://www.etymonline.com/word/climate\" \\\n \"https://www.etymonline.com/word/climax\" \\\n \"https://www.etymonline.com/word/clinic\" \\\n \"https://www.etymonline.com/word/client\" \\\n \"https://www.etymonline.com/word/ladder\" \\\n \"https://www.etymonline.com/word/lid\" \\\n ; do python3 tools/fetch_source.py \"$u\" --note \"page 269, roots Klei/Klem\" 2>&1 | tail -2; done",
 "description": "Archive Wiktionary and Etymonline pages"
}
```


### [2026-09-06T21:00:38.546Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/af836658d4cb6f30.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b0c505847131e40b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/720696b649ae6232.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5f38b60d6dda1101.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b81d8d8e66ca8dc7.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/900300b1ae3dbca0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c7d237f2cd8ace33.txt
```


## [2026-09-06T21:00:41.943Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in af836658d4cb6f30 b0c505847131e40b 720696b649ae6232 5f38b60d6dda1101 b81d8d8e66ca8dc7 900300b1ae3dbca0 c7d237f2cd8ace33; do echo \"##### $f\"; head -c 2200 $f.txt | tr -s '\\n' '\\n'; echo; done 2>&1 | head -150",
 "description": "Read archived pages"
}
```


### [2026-09-06T21:00:43.771Z] TOOL RESULT

```
##### af836658d4cb6f30
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%E1%B8%B1ley-
FETCHED: 2026-09-06T21:00:36Z
STATUS: 200
TITLE: Reconstruction:Proto-Indo-European/ḱley- - Wiktionary, the free dictionary
Reconstruction:Proto-Indo-European/ḱley- - Wiktionary, the free dictionary 
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
 Proto-Indo-European 
 Toggle Proto-Indo-European subsection 
 1.1 
 Etymology 1 
 1.1.1 
 Root 
 1.1.1.1 
 Derived terms 
 1.2 
 Etymology 2 
 1.2.1 
 Root 
 1.2.1.1 
 Derived terms 
 1.2.1.2 
 Descendants 
 1.3 
 References 
 Toggle the table of contents 
 Reconstruction:Proto-Indo-European/ ḱley- 
 1 language 
 Français 
 Reconstruction 
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
 Get shortened URL 
 Print/export
 Download as PDF 
 Printable version 
 In other projects
 Appearance
 move to sidebar 
 hide 
 From Wiktionary, the free dictionary
 This Proto-Indo-European entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.
 Proto-Indo-European
 [ edit ] 
 Etymology 1
 [ edit ] 
 Reanalysed root of *ḱléyti , from *ḱel- ( “ to cover ” ) +‎ *-éyti ( *éy-present suffix ) .
 Root
 [ edit ] 
 *ḱley- 
 to shelter , cover 
 Derived terms
 [ edit ] 
 Terms derived from the Proto-Indo-European root *ḱley- (cover) (18 c, 0 e) 
 *ḱléy-tis ~ *ḱli-téys 
 Proto-Balto-Slavic: 
 Lithuanian: šliti̇̀s ( “ shove-shed ” ) 
 *ḱléy-treh₂ 
 *ḱloyw-ó-s 
 Proto-Germanic: *hlaiwaz ( “ shelter ” ) 
 Proto-West Germanic: 
##### b0c505847131e40b
URL: https://www.etymonline.com/word/climate
FETCHED: 2026-09-06T21:00:36Z
STATUS: 200
TITLE: Climate - Etymology, Origin & Meaning
Climate - Etymology, Origin & Meaning 
 Search 
 Log in 
 Columns 
 Forum 
 Apps 
 Premium 
 Log in 
 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
 Origin and history of climate 
 climate (n.) 
 late 14c., "horizontal zone of the earth's surface measured by lines parallel to the equator," from Old French climat "region, part of the earth," from Latin clima (genitive climatis ) "region; slope of the earth," from Greek klima "region, zone," literally "an inclination, slope," thus "slope of the earth from equator to pole," from a suffixed form of PIE root *klei- "to lean."
 Ancient geographers divided the earth into zones based on the angle of sun on the slope of the earth's surface and the length of daylight. Some reckoned 24 or 30 climates between Meroe on the upper Nile in Sudan and the mythical Riphaean Mountains which were supposed to bound the Arctic; a change of climate took place, going north, at a place where the day was a half hour longer or shorter, according to season, than the starting point. Others counted 7 (each dominated by a particular planet) or 12 (dominated by zodiac signs).
 Change of temperature gradually came to be considered more important, and by late 14c. the word was being used in the sense "a distinct region of the earth's surface considered with respect to weather." The sense shift to "combined results of weather associated with a region, characteristic condition of a country or region with reference to the variation of heat, cold, rainfall, wind, etc.," is attested by c. 1600. Figuratively, of mental or moral atmosphere, from 1660s.
 also from late 14c. 
 Entries linking to climate 
 acclimate (v.) 
 1792, "habituate (something) to a new climate," from French acclimater , verb formed from à "to" (see ad- ) + climat (see climate ). Intransitive sense "adapt to a new climate" is from 1861. Related: Acclimated ; acclimating . The extended form acclimatize is now more common in the older sense of this word (generally in re
##### 720696b649ae6232
URL: https://www.etymonline.com/word/climax
FETCHED: 2026-09-06T21:00:37Z
STATUS: 200
TITLE: Climax - Etymology, Origin & Meaning
Climax - Etymology, Origin & Meaning 
 Search 
 Log in 
 Columns 
 Forum 
 Apps 
 Premium 
 Log in 
 A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 
 Quick and reliable accounts of the origin and history of English words. Scholarly, yet simple.
 About
 Who Did This 
 Sources 
 Introduction
```


## [2026-09-06T21:00:49.495Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"== klei- etym2\"; grep -n -A40 \"Etymology 2\" af836658d4cb6f30.txt | head -70",
 "description": "Read Wiktionary klei- etymology 2"
}
```


### [2026-09-06T21:00:49.543Z] TOOL RESULT

```
== klei- etym2
71: Etymology 2 
72-
73- 1.2.1 
74- Root 
75-
76- 1.2.1.1 
77- Derived terms 
78-
79- 1.2.1.2 
80- Descendants 
81-
82- 1.3 
83- References 
84-
85- Toggle the table of contents 
86-
87- Reconstruction:Proto-Indo-European/ ḱley- 
88-
89- 1 language 
90-
91- Français 
92-
93- Reconstruction 
94-
95- Discussion 
96-
97- English 
98-
99- Read 
100-
101- Edit 
102-
103- View history 
104-
105- Tools 
106-
107- Tools
108-
109- move to sidebar 
110- hide 
111-
--
180: Etymology 2
181- [ edit ] 
182-
183- Reanalysed root of *ḱléyti , from *ḱel- ( “ to incline ” ) +‎ *-éyti ( *éy-present suffix ) . [ 1 ] [ 2 ] 
184-
185- Root
186- [ edit ] 
187-
188- *ḱley- ( perfective ) [ 1 ] [ 3 ] [ 4 ] 
189-
190- to lean , slope , incline 
191-
192- Derived terms
193- [ edit ] 
194-
195- Terms derived from the Proto-Indo-European root *ḱley- (incline) (46 c, 0 e) 
196-
197- *ḱléy-t ~ *ḱli-ént ( root aorist ) 
198- Proto-Indo-Iranian: 
199- Proto-Indo-Aryan: 
200- Sanskrit: अश्रेत् ( áśret ) 
201-
202- Proto-Indo-Iranian: 
203- ⇒ Avestan: 𐬥𐬌𐬯𐬭𐬍𐬙𐬀 ( nisrīta , “ to bring to, assign ” , 3sg.inj.mid. ) 
204-
205- Proto-Italic: *klient- ( “ who supports, who depends ” , act.ptc. ) [ 5 ] 
206- Latin: cliēns 
207-
```


## [2026-09-06T21:00:52.696Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 720696b649ae6232 5f38b60d6dda1101 b81d8d8e66ca8dc7 900300b1ae3dbca0 c7d237f2cd8ace33; do echo \"##### $f\"; grep -n -m1 -A6 \"^ climax (n.)\\|^ clinic (n.)\\|^ client (n.)\\|^ ladder (n.)\\|^ lid (n.)\" $f.txt; done",
 "description": "Extract Etymonline entries"
}
```


### [2026-09-06T21:00:54.362Z] TOOL RESULT

```
##### 720696b649ae6232
56: climax (n.) 
57-
58- 1580s, in the rhetorical sense ("a chain of reasoning in graduating steps from weaker to stronger"), from Late Latin climax (genitive climacis ), from Greek klimax "propositions rising in effectiveness," literally "ladder," from suffixed form of PIE root *klei- "to lean."
59-
60- Originally in rhetoric an arrangement of successive clauses so that the last important word of one is repeated as the first important word of the next, as in Romans v.3-5: "... but we glory in tribulations also: knowing that tribulation worketh patience; and patience, experience; and experience, hope: And hope maketh not ashamed ...." Compare anadiplosis . From the rhetorical meaning, the word evolved through "series of steps by which a goal is achieved," to "escalating steps," to (1789) "high point of intensity or development," a usage credited by the OED to "popular ignorance."
61-
62- The meaning "sexual orgasm" is recorded by 1880 (also in terms such as climax of orgasm ), and is said to have been promoted from c. 1900 by birth-control pioneer Marie Stopes (1880-1958) and others as a more accessible word than orgasm (n.).
##### 5f38b60d6dda1101
23: clinic (n.) 
24-
25- 1620s, "bedridden person, one confined to his bed by sickness," from French clinique (17c.), from Latin clinicus "physician that visits patients in their beds," from Greek klinike (techne) "(practice) at the sickbed," from klinikos "of the bed," from kline "bed, couch, that on which one lies," from suffixed form of PIE root *klei- "to lean."
26-
27- Also "one who defers baptism until the death-bed" (1660s). Sense of "private hospital" is from 1884, from German Klinik in this sense, itself from French clinique , via the notion of "bedside medical education, examination of a patient by an instructor in the presence of students." The modern sense thus reverses the classical one, in which the "clinic" came to the patient. General sense of "conference for group instruction in something" is from 1919.
28- also from 1620s 
29-
##### b81d8d8e66ca8dc7
23: client (n.) 
24-
25- late 14c., "one who lives under the patronage of another," from Anglo-French clyent (c. 1300), from Latin clientem (nominative cliens ) "follower, retainer" (related to clinare "to incline, bend"), from PIE *klient- , a suffixed (active participle) form of root *klei- "to lean." The notion apparently is "one who leans on another for protection." In ancient Rome, a plebeian under the guardianship and protection of a patrician (who was called patronus in this relationship; see patron ).
26-
27- The meaning "a lawyer's customer" is attested from c. 1400, and by c. 1600 the word was extended to any customer who puts a particular interest in the care and management of another. Related: Cliency .
28-
29- The relation of client and patron between a plebeian and a patrician, although at first strictly voluntary, was hereditary, the former bearing the family name of the latter, and performing various services for him and his family both in peace and war, in return for advice and support in respect to private rights and interests. Foreigners in Rome, and even allied or subject states and cities, were often clients of Roman patricians selected by them as patrons. The number of a patrician's clients, as of a baron's vassals in the middle ages, was a gage his greatness. [Century Dictionary]
##### 900300b1ae3dbca0
23: ladder (n.) 
24-
25- "frame of wood, rope, etc., consisting of two side-pieces and cross-rungs or rounds, by which a person may ascend," Middle English laddere , from Old English hlæder "ladder, steps," from Proto-Germanic *hlaidri (source also of Old Frisian hledere , Middle Dutch ledere , Old High German leitara , German Leiter ), which is reconstructed to be from a suffixed form of PIE root *klei- "to lean" (source also of Greek klimax "ladder").
26-
27- Figuratively, of any means of ascending or rising, from late Old English. In late Old English, rungs were læddrestæfæ and the side pieces were ledder steles . The superstitious avoidance of walking under a ladder is attested by 1787, but it also is sound advice. Related: Ladderway .
28-
29- Entries linking to ladder 
##### c7d237f2cd8ace33
23: lid (n.) 
24-
25- "movable or removable cover for a pot, etc.," mid-13c., from Old English hlid "covering, opening, gate," from Proto-Germanic *hlidan "a cover," literally "that which bends over" (source also of Old Norse hlið "gate, gap," Swedish lid "gate," Old French hlid , Middle Dutch lit , Dutch lid , Old High German hlit "lid, cover"), from PIE *klito- , from root *klei- "to lean."
26-
27- Meaning "eyelid" is from early 13c. Slang sense of "hat, cap" is attested from 1896. As a measure of marijuana, one ounce, 1967, presumably the amount of dried weed that would fit in some commercial jar lid. Slang phrase put a lid on "clamp down on, silence, end" is from 1906; many figurative senses are from the image of a pot boiling over.
28- also from mid-13c. 
29-
```


## [2026-09-06T21:01:03.441Z] TOOL CALL #47: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/%D8%A5%D9%82%D9%84%D9%8A%D9%85\" \\\n \"https://en.wiktionary.org/wiki/%D8%A7%D9%82%D9%84%DB%8C%D9%85\" \\\n \"https://en.wiktionary.org/wiki/%D8%B4%D9%85%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%E0%A4%B6%E0%A5%8D%E0%A4%B0%E0%A4%AE%E0%A4%A3\" \\\n \"https://en.wiktionary.org/wiki/shaman\" \\\n \"https://en.wiktionary.org/wiki/%CE%BA%CE%BB%E1%BF%96%CE%BC%CE%B1\" \\\n ; do python3 tools/fetch_source.py \"$u\" --note \"page 269, Klei/Klem: eqlim, shaman\" 2>&1 | tail -1; done",
 "description": "Archive Persian/Arabic Wiktionary pages"
}
```


### [2026-09-06T21:01:08.701Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/f90962a3f3dc821a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8f256598112aa129.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6b6501fb5b2b9d42.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/24d8310abe88dc12.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/7bdc93b01b0aeb67.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1bfb30057002e0e2.txt
```


## [2026-09-06T21:01:11.902Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in f90962a3f3dc821a 8f256598112aa129 6b6501fb5b2b9d42 7bdc93b01b0aeb67; do echo \"##### $f\"; awk '/^ Etymology/,0' $f.txt | head -30; echo; done",
 "description": "Read Wiktionary etymologies"
}
```


### [2026-09-06T21:01:13.393Z] TOOL RESULT

```
##### f90962a3f3dc821a
 Etymology 

 1.2 
 Pronunciation 

 1.3 
 Noun 

 1.3.1 
 Declension 

 1.3.2 
 Derived terms 

 1.3.3 
 Descendants 

 1.4 
 See also 

 Toggle the table of contents 

 إقليم 

 6 languages 

 العربية 
 Català 
 Magyar 
 Kurdî 

##### 8f256598112aa129
 Etymology 

 1.2 
 Pronunciation 

 1.3 
 Noun 

 1.3.1 
 Derived terms 

 1.3.2 
 Descendants 

 2 
 Urdu 

 Toggle Urdu subsection 

 2.1 
 Etymology 

 2.2 
 Pronunciation 

 2.3 
 Noun 

 2.3.1 
 Derived terms 

##### 6b6501fb5b2b9d42
 Etymology 

 1.2 
 Pronunciation 

 1.3 
 Noun 

 1.3.1 
 References 

 Toggle the table of contents 

 شمن 

 3 languages 

 فارسی 
 Malagasy 
 Русский 

 Entry 

 Discussion 

 English 

 Read 

 Edit 

##### 7bdc93b01b0aeb67
 Etymology 

 1.2 
 Pronunciation 

 1.3 
 Noun 

 1.3.1 
 Usage notes 

 1.3.2 
 Derived terms 

 1.3.3 
 Descendants 

 1.3.4 
 Translations 

 1.4 
 References 

 1.5 
 Anagrams 

 2 
 Danish 

 Toggle Danish subsection
```


## [2026-09-06T21:01:17.025Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in f90962a3f3dc821a 8f256598112aa129 6b6501fb5b2b9d42 7bdc93b01b0aeb67 24d8310abe88dc12; do echo \"##### $f\"; grep -n -m2 -A8 \"Borrowed from\\|Learned borrowing\\|From Sanskrit\\|From Proto\\|Ultimately from\" $f.txt | head -30; echo; done",
 "description": "Extract etymology text"
}
```


### [2026-09-06T21:01:18.489Z] TOOL RESULT

```
##### f90962a3f3dc821a
174: Borrowed from Ancient Greek κλίμα ( klíma ) .
175-
176- Pronunciation
177- [ edit ] 
178-
179- IPA ( key ) : /ʔiq.liːm/ 
180-
181- Noun
182- [ edit ] 

##### 8f256598112aa129
173: Borrowed from Arabic إِقْلِيم ( ʔiqlīm ) , from Ancient Greek κλίμα ( klíma ) .
174-
175- Pronunciation
176- [ edit ] 
177-
178- ( Classical Persian ) IPA ( key ) : /ʔiq.ˈliːm/ 
179-
180- ( Dari, formal ) IPA ( key ) : [ʔɪq.líːm] 
181-
--
234: Borrowed from Classical Persian اِقْلِیم ( iqlīm ) , from Arabic إِقْلِيم ( ʔiqlīm ) , from Ancient Greek κλίμα ( klíma ) .
235-
236- Pronunciation
237- [ edit ] 
238-
239- ( Standard Urdu ) IPA ( key ) : /ɪq.liːm/ 
240-
241- Noun
242- [ edit ] 

##### 6b6501fb5b2b9d42

##### 7bdc93b01b0aeb67
211: Borrowed from German Schamane , [ 1 ] from Russian шама́н ( šamán ) , [ 1 ] from Evenki шама̄н ( şamān ) , сама̄н ( samān ) , [ 2 ] from Proto-Tungusic *samān . The Evenki word is possibly derived from the root ша- ( şa- , “ to know ” ) ; [ 3 ] or else a loanword from Tocharian B ṣamāne ( “ monk ” ) [ 4 ] or Chinese 沙門  / 沙门 ( shāmén , “ Buddhist monk ” ) , from Pali samaṇa from Sanskrit श्रमण ( śramaṇa , “ ascetic, monk, devotee ” ) , from श्रम ( śrama , “ weariness, exhaustion; labor, toil; etc. ” ) , which would make this a doublet of sramana . [ 4 ] 
212-
213- Pronunciation
214- [ edit ] 
215-
216- ( Received Pronunciation ) IPA ( key ) : /ˈʃɑːmən/ , [ 5 ] /ˈʃæmən/ [ 5 ] 
217-
218- Audio ( Southern England ) : ( file ) 
219-

##### 24d8310abe88dc12
193: Borrowed from Sanskrit श्रमण ( śramaṇa ) .
194-
195- Pronunciation
196- [ edit ] 
197-
198- ( Standard Hindi ) IPA ( key ) : /ʃɾə.məɳ/ , [ʃɾɐ.mɐ̃ɳ] 
199-
200- Noun
201- [ edit ]
```


## [2026-09-06T21:01:25.236Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"== شمن\"; sed -n '150,260p' 6b6501fb5b2b9d42.txt; echo \"== sramana sanskrit\"; grep -n -B3 -A12 \"Sanskrit\\b\" 24d8310abe88dc12.txt | sed -n '1,80p'",
 "description": "Read Persian shaman and Sanskrit sramana entries"
}
```


### [2026-09-06T21:01:25.319Z] TOOL RESULT

```
== شمن
 ( Dari, formal ) IPA ( key ) : [ʃä.mán] 

 ( Dari, formal ) IPA ( key ) : [ʃä.mán] 
 ( Kabuli ) IPA ( key ) : [ʃä.mán] 

 ( Hazaragi ) IPA ( key ) : [ʃä.mán] 

 ( Iran, formal ) IPA ( key ) : [ʃæ.mǽn] 

 ( Tajik, formal ) IPA ( key ) : [ʃä.mán] 

 Rhymes: -an 

 Readings

 Classical reading ? 

 šaman

 Dari reading ? 

 šaman

 Iranian reading ? 

 šaman

 Tajik reading ? 

 šaman

 Noun
 [ edit ] 

 Dari

 شمن 

 Iranian Persian

 Tajik

 шаман 

 شمن • ( šaman ) 

 ( archaic ) an idolater 
 10th Century CE , Ferdowsi , Shahnameh 
 از ایران یکی کهترم چون شمن 
پیام آوریده به شاه یمن az irân yeki kehtaram čon šaman 
payâm âvaride be šâhe yaman I am a servant from Iran, humble as an idolater 
bringing a message to the king of Yemen . 

 shaman 

 References
 [ edit ] 

 Dehkhoda, Ali-Akbar ( 1931– ), “ شمن ”, in Dehkhoda Dictionary Institute , editors, Dehkhoda Dictionary (in Persian), Tehran: University of Tehran Press . 

 Retrieved from " https://en.wiktionary.org/w/index.php?title=شمن&oldid=77586001 "

 Categories : Persian terms inherited from Middle Persian 
 Persian terms derived from Middle Persian 
 Persian terms with IPA pronunciation 
 Rhymes:Persian/an 
 Rhymes:Persian/an/2 syllables 
 Persian lemmas 
 Persian nouns 
 Persian terms with archaic senses 
 Persian terms with quotations 

 Hidden categories: Parthian terms in nonstandard scripts 
 Requests for native script for Sogdian terms 
 Pages with entries 
 Pages with 1 entry 

 This page was last edited on 10 January 2024, at 00:31.

 Definitions and other text are available under the Creative Commons Attribution-ShareAlike License ; additional terms may apply. By using this site, you agree to the Terms of Use and Privacy Policy. 

 Privacy policy 

 About Wiktionary 

 Disclaimers 

 Legal & safety contacts 

 Code of Conduct 

 Developers 

 Statistics 

 Cookie statement 

 Mobile view 

 Search 

 Search 

 Toggle the table of contents 

 شمن 

 3 languages 

 Add topic== sramana sanskrit
74- References 
75-
76- 2 
77: Sanskrit 
78-
79: Toggle Sanskrit subsection 
80-
81- 2.1 
82- Alternative scripts 
83-
84- 2.2 
85- Etymology 
86-
87- 2.3 
88- Pronunciation 
89-
90- 2.4 
91- Adjective 
--
190- Etymology
191- [ edit ] 
192-
193: Borrowed from Sanskrit श्रमण ( śramaṇa ) .
194-
195- Pronunciation
196- [ edit ] 
197-
198- ( Standard Hindi ) IPA ( key ) : /ʃɾə.məɳ/ , [ʃɾɐ.mɐ̃ɳ] 
199-
200- Noun
201- [ edit ] 
202-
203- श्रमण • ( śramaṇ )  m 
204-
205- ( Buddhism , Jainism ) ascetic , monk 
--
242-
243- McGregor, Ronald Stuart ( 1993 ), “ श्रमण ”, in The Oxford Hindi-English Dictionary , London: Oxford University Press 
244-
245: Sanskrit
246- [ edit ] 
247-
248- Alternative scripts
249- [ edit ] 
250-
251- Alternative scripts
252- শ্ৰমণ ( Assamese script ) 
253- ᬰ᭄ᬭᬫᬡ ( Balinese script ) 
254- শ্রমণ ( Bengali script ) 
255- 𑰫𑰿𑰨𑰦𑰜 ( Bhaiksuki script ) 
256- 𑀰𑁆𑀭𑀫𑀡 ( Brahmi script ) 
257- ၐြမဏ ( Burmese script ) 
--
293-
294- ( Vedic ) IPA ( key ) : /ɕɾɐ.mɐ.ɳɐ́/ 
295-
296: ( Classical Sanskrit ) IPA ( key ) : /ɕɾɐ.mɐ.ɳɐ/ 
297-
298- Adjective
299- [ edit ] 
300-
301- श्र॒म॒ण • ( śramaṇá ) stem 
302-
303- making effort or exertion , toiling , labouring , (esp.) following a toilsome or menial business ( W. )
304-
305- base , vile , bad (ib.)
306-
307- naked ( L. )
308-
--
854- Further reading
855- [ edit ] 
856-
857: Monier Williams ( 1899 ), “ श्रमण ”, in A Sanskrit–English Dictionary,   [ … ] , new edition, Oxford: At the Clarendon Press , →OCLC , page 1096 , column 2. 
858-
859- Retrieved from " https://en.wiktionary.org/w/index.php?title=श्रमण&oldid=92292828 "
860-
861: Categories : Hindi terms borrowed from Sanskrit 
862: Hindi terms derived from Sanskrit 
863- Hindi terms with IPA pronunciation
```


## [2026-09-06T21:01:31.694Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '100,150p' 6b6501fb5b2b9d42.txt",
 "description": "Read shaman Persian etymology block"
}
```


### [2026-09-06T21:01:31.732Z] TOOL RESULT

```
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

 See also: سمن 

 Persian
 [ edit ] 

 Etymology
 [ edit ] 

 From Middle Persian šmn ( šaman , “ Buddhist monk ” ) , akin to Manichaean Parthian šmn ( šaman , “ Buddhist monk ” ) , Sogdian [script needed] ( šmn /⁠šaman⁠/ , “ monk ” ) .

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /ʃa.ˈman/ 

 ( Dari, formal ) IPA ( key ) : [ʃä.mán]
```


## [2026-09-06T21:01:51.675Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== LKT klima\"; grep -n -i \"klima\\|iqlim\\|aqlim\" LKT.txt | head -10; echo \"=== FVQ iqlim\"; grep -n -i \"iqlim\\|klima\" FVQ.txt | head -5; echo \"=== SKT ladder/lean/lid\"; grep -n \"^ladder\\|ladder, sb\\|lean (1)\\|lid, sb\\|climate\\|climax\" SKT.txt | head -10",
 "description": "Grep Lokotsch, Jeffery, Skeat"
}
```


### [2026-09-06T21:01:51.747Z] TOOL RESULT

```
=== LKT klima
1710:Hieraus  ist  der  Name  der  Jutepflanze Gorchorus  capsularis  L.  oder  C.  olitorius L.  entstanden,  da  ihre  Wurzel  stark  ge- wellt oder  kraus  ist.  Die  Pflanze,  die in  Indien,  besonders  in  Bengalen,  hei- misch ist,  ähnelt  dem  Hanfe  sehr,  ist aber  kleiner  und  gedeiht  in  feuchtheißem Klima.  Nach  Europa  gelangle  die  Jute {früher  dtsch.  Dschute  gesprochen], engl,  jute,  zu  Anfang  des  18.  Jahr- hunderts durch  Vermittlung  eines  engl. Kaufmanns  in  Kalkutta.  Der  Hauptein- fuhrhafen für  ganz  Europa  ist  Liverpool geworden;  die  erste  Spinnerei  für  Jute wurde  i.  J.  183!2  in  Dundee  errichtet. [Hobson-Jobson  474.
=== FVQ iqlim
=== SKT ladder/lean/lid
3566:cUmaz.  the  highest  degree.  (Gk.) itKifutf,  a  ladder,  staircase,  highest  jntch expression    (in    rhetoric).  — Gk.  KAm»v» slope.     Der.  anti-climax. clime.  (U-Gk)    L  fUmta^w^
22994:climate — clime.
23497:French  from  Leno  f-atin  from  Greek : acolyle.allegor}',  almanac,  anchoret  (anchor- ite), apostasy,  apostate,  botllc(i),  butler, jibuttery,  bushel,  calender,  calm,  carbine, card  (O,  CRile,  cnt»logue,  cauterise,  celan- dine, chronicle,  clergy,  climacter,  climate,
```


## [2026-09-06T21:01:54.408Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== WLD I 490\"; grep -n \"k̂lei\\|klei-\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -10; echo \"=== IEC klei\"; grep -n \"klei-\\|kleiō\\|klinō\" IEC.txt | head -10; echo \"=== SYN lean\"; grep -n -i \"klinein\\|klino\\|kline \" SYN.txt | head -8",
 "description": "Grep Walde-Pokorny, Mann, Buck"
}
```


### [2026-09-06T21:01:54.484Z] TOOL RESULT

```
=== WLD I 490
26394:„Schonheit, Zierde, Schmuck", aksl. krasbm ,.schon, angenehm. weiB geklei- 
27087:Worte fiir „Schutz“ nicht besser nach Noreen Ltl. 32 an klei- „lehnen" 
27102:Basis der viel reicher entwickelten Wzf. klei- , ; lehnen‘‘ und sehr wahr- 
27153:der i-Basis klei- „lehnen“ vermuten, und hat man z. B. auch kel- „beugen", 
30825:qlau- — klei- 
30841:klei- „neigen. lehnen"; vielfach von angelehnten Stangen (daher Zelte 
30850:Arm. Stud. 101. Gdf. *klei-iio- mit r- und w-Formantien weitergeb.? Schef- 
30890:klei- 
31182:bleibt dims, s. klei- „lehren“), und gloria (s. eine zw. Yermutung unter *yal- 
=== IEC klei
8928:cline’. Cf. Kleio and Klit-. WP I, 490 Av. -sirinaomi, cpds. "gor: Gk. klinō, tr. intr. ‘lean, bend, tilf”; Lat. cfino, are, id.; MIr. den ‘inclination’; OHG hlinen ‘lean, lie down’; MHG linen, lénen, wd ` OS hlinon, tr. ‘lean, til; OE hlinian ‘lean, lie down’; Li. Slynü, Slýti ‘incline, lean". For Du. lenig, cf. Gk. klinikós .
=== SYN lean
```


## [2026-09-06T21:02:05.787Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '30838,30860p' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt; echo \"=== SKT lean/ladder/lid\"; grep -n -i \"ladder, a  frame\\|ladder\\.\" SKT.txt | head -5; grep -n \"lean (1)\\|lean, to  incline\\|lid, a  cover\" SKT.txt | head -5",
 "description": "Read WLD klei- and Skeat entries"
}
```


### [2026-09-06T21:02:05.860Z] TOOL RESULT

```
ludern (Schmellerl 2 1542) „Alpenerle, Betula nana L.“. Schrader BB. 15, 
2S9, RL. 199. 

klei- „neigen. lehnen"; vielfach von angelehnten Stangen (daher Zelte 
mit Stangengerippe : Sattelstangen , Leitern, leiter- oder gitterartigen 
Holzkonstruktionen (s. zum Sachlichen Meringer IF. 1(1. 1 I7ff.), andrer- 
seits von Berglehnen, Hiigeln u. dgl. 

Ai. crayaft „lehnt, legt an“, erayate „lehnt sich an, befindet sich“, oritd- 
= av. srita- ( : sray-) „gelehnt". 

Arm. lathi, gen. lerin „Berg“ (Hubschmann Arm. Gr. I 451 m. Lit., Liden 
Arm. Stud. 101. Gdf. *klei-iio- mit r- und w-Formantien weitergeb.? Schef- 
telowitz BB. 2S. 292 setzt kleitra an, was lautlich nicht moglich scheint). 

Unsicher arm. It min ,,werde. entstebe. geschehe. bin - ' (Bed. ware dieselbe 
wie ai. erayate ..befindet sich ££ , M-Praes. wie im Gr., Lat. und Germ.: 
Bugge Beitr. S, Hiibscbmann Arm. Gr. I 451 ; dagegen von Pedersen KZ. 30, 
341: 39. 343 mit alb. /■?/>, fee .,war“ verbunden, idg. Anlaut tjl-). 

Gr. y.Xrvo >, lesb. y.Xfvvco (*xXlv-ico) „neige, lebne an“ (Fut. x/jvm, Pf. 
y.sy.Xnad, y.Xao g ..gelegem", x.Xioi ? „Neigung“, y.Xtola „Hutte, Zelt“ (s. dazu 
auch Fraenkel KZ. 45, 108), dry. 7.<V5sg PI. ..zweifliigelige Turk y.Xivi] „Bett‘ £ , 
=== SKT lean/ladder/lid
1860:Bladder.  (E.)    See  Blow  (1).
1945:bladder.  (E)     ME.  b. bKrJr,  1  Mi<((-r.  lit.  M  blowin"
9844:Ladder.  (E.>  M.EJaddn.  A.S.A/ader, a  ladder.  4*  l^u.  /adder,  ladder,  rails  ul a  cart;  O.  H.  G.  k/ttin,  G.  UiUr,  a ladder.
16560:Suxlfrage,  a  plant.  (F.  — L.)  F.  saxi- ffa^e-  —  L.saxi/nj^,  spleen-wort ;  so  natnetJ bccau&c  it  was  suppo:^^^  to  break  stones  io the  bladder.  *L.  saxt',  for  saxttm,  a  stunc; /ra^ ,  base  cA  frnti^re,  to  break.
16594:I  jro/a,  a  ladder.     L.  ui-(a ^ Jtmd^U* sttd-t  bate  of  MOMdin,  to  climb
```


## [2026-09-06T21:02:08.825Z] TOOL CALL #55: Bash

```json
{
 "command": "python3 tools/fetch_source.py \"https://abadis.ir/fatofa/%DA%A9%D9%84%DB%8C%D9%86%DB%8C%DA%A9/\" --note \"page 269, MON:3051 kelinik, Mo'in entry\" 2>&1 | tail -1; python3 tools/fetch_source.py \"https://abadis.ir/fatofa/%D8%A7%D9%82%D9%84%DB%8C%D9%85/\" --note \"page 269, MON:326 eqlim, Mo'in entry\" 2>&1 | tail -1",
 "description": "Archive Mo'in online entries"
}
```


### [2026-09-06T21:02:13.866Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/c92105c87df88342.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/77391006c74b7222.txt
```


## [2026-09-06T21:02:17.378Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"== kelinik abadis\"; grep -n -m3 -A6 \"معین\" c92105c87df88342.txt | head -30; echo \"== eqlim abadis\"; grep -n -m3 -A6 \"معین\" 77391006c74b7222.txt | head -30",
 "description": "Read abadis Mo'in entries"
}
```


### [2026-09-06T21:02:17.441Z] TOOL RESULT

```
== kelinik abadis
20: کلینیک. [ کْلی / ک ِ ] ( فرانسوی ، اِ ) مطب. محکمه. ( فرهنگ فارسی معین ). || درمانگاه. ( فرهنگ فارسی معین ). || ( ص ) بالینی : امراض کلینیک ( بیماریهای بالینی ). 
21-
22- فرهنگ فارسی
23-
24- مطب، بیمارستان، درمانگاه
25-۱ - ( اسم ) مطب محکمه . ۲ - ( صفت ) بالینی : امراض کلینیک 
26-
27: فرهنگ معین
28-
29- (کِ ) [ فر. ] ۱ - (اِ. ) ساختمان یا بخشی در بیمارستان یا مراکز بهداشتی - درمانی که به درمان بیماران یا مراقبت پزشکی از بیماران سرپایی اختصاص داشته باشد، درمانگاه . (فره ). ۲ - (ص . ) بالینی . 
30-
31- فرهنگ عمید
32-
33- ۱. درمانگاه
--
45:• فرهنگ فارسی، محمد معین، انتشارات امیر کبیر، تهران، ۱۳۷۵
46-• غلط ننویسیم، ابوالحسن نجفی، مرکز نشر دانشگاهی، تهران، ۱۳۸۶
47-• فرهنگ کوچک زبان پهلوی، دیوید نیل مکنزی، ترجمه مهشید فخرایی، پژوهشگاه علوم انسانی و مطالعات فرهنگی، تهران، ۱۳۷۹
48-
49- بروم " کورزدایی " کنم. 
50-پزشک دردم را کور کند. بیماری زدایی.
51-
== eqlim abadis
48: فرهنگ معین
49-
50- ( اِ ) [ معر - یو. ] (اِ. ) ۱ - کشور، مملکت . ۲ - ولایت . ج . اقالیم . 
51-
52- فرهنگ عمید
53-
54- ۱. [مجاز] مملکت، کشور.
--
68:آب و هوا یا اقلیم برآمد شرایط جوی یک محل طی بازه زمانی معین ( معمولاً چند دهه ) است. به عبارت دیگر رویدادهای پر بسامد جوی طی سالیان متمادی را اقلیم گویند؛ در جمع بندی و طبق تعریف ارائه شده به وسیلهٔ کاویانی و علیجانی ( ۱۳۷۹ ) ، آب و هوا ( اقلیم ) را می توان «شرایط جوی غالب ( دراز مدت ) در یک محل» تعریف کرد. [ ۴] اقلیم شناسی دانشی است که اقلیم ( آب وهوا ) را مطالعه می کند و از زیرشاخه های جغرافیای طبیعی است. 
69-اقلیم در مناطق مختلف دنیا با عرض جغرافیایی و ارتفاع از سطح دریا مشخص می شود. ایران فلاتی است مرتفع که در عرض جغرافیایی ( ۴۰–۲۵ ) درجه در نیمکرهٔ شمالی و در منطقهٔ گرم واقع است. تقسیمات اقلیمی، که بر اساس مطالعات و پیشنهادهای دانشمندان محیط شناس ایرانی تدوین شده عموماً در حیطهٔ معماری شامل تقسیم بندی های چهارگانه به شرح زیر است:
70-• اقلیم گرم و خشک ( فلات مرکزی ایران ) 
71-• اقلیم سرد کوهستانی ( مناطق کوهستانی غرب کشور ) 
72-• اقلیم معتدل و مرطوب ( کرانهٔ جنوبی دریای خزر ) 
73-• اقلیم گرم و مرطوب ( کرانهٔ شمالی خلیج فارس و دریای عمان ) 
74- wiki: اقلیم 
--
148:• فرهنگ فارسی، محمد معین، انتشارات امیر کبیر، تهران، ۱۳۷۵
149-• غلط ننویسیم، ابوالحسن نجفی، مرکز نشر دانشگاهی، تهران، ۱۳۸۶
150-• فرهنگ کوچک زبان پهلوی، دیوید نیل مکنزی، ترجمه مهشید فخرایی، پژوهشگاه علوم انسانی و مطالعات فرهنگی، تهران، ۱۳۷۹
151-
152- " اقلیم ". اکلیم ، کلیم، گفته، نامیده، نام نهاده شده به نام خویشی، کسی و یا کسانی که در آن زندگی می دارند.
153-
154- به جای واژه بیگانه {اقلیم}، از واژه های {آب و هوا، بوم و بَر، مرز و بوم، بوم} بِکار ببریم.
```


## [2026-09-06T21:02:41.166Z] TOOL CALL #57: Bash

```json
{
 "command": "python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/%E0%A4%B6%E0%A5%8D%E0%A4%B0%E0%A4%AE\" --note \"page 269, Klem: Sanskrit śrama etymology\" 2>&1 | tail -1",
 "description": "Archive Wiktionary śrama"
}
```


## [2026-09-06T21:02:43.170Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== ARY klei\"; grep -n -i \"KLEI\\|KLINO\" incoming/ARY/ARY_latin_index_pages.txt | head -10",
 "description": "Grep Aryanpur index for klei"
}
```


### [2026-09-06T21:02:43.551Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/c108752542a3ab1f.txt
```


### [2026-09-06T21:02:43.601Z] TOOL RESULT

```
=== ARY klei
```


## [2026-09-06T21:02:46.896Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n -m3 -A6 \"Sanskrit\" c108752542a3ab1f.txt | sed -n '1,10p'; echo \"---\"; awk '/^ Sanskrit$/,0' c108752542a3ab1f.txt | grep -n -m2 -A10 \"Etymology\"",
 "description": "Read Wiktionary śrama etymology"
}
```


### [2026-09-06T21:02:48.740Z] TOOL RESULT

```
74: Sanskrit 
75-
76: Toggle Sanskrit subsection 
77-
78- 2.1 
79- Alternative scripts 
80-
81- 2.2 
82- Etymology 
--
---
42: Etymology
43- [ edit ] 
44-
45- From the root  श्रम् ( śram , “ to be or become weary or tired, be tired of doing anything ” ) .
46-
47- Pronunciation
48- [ edit ] 
49-
50- ( Vedic ) IPA ( key ) : /ɕɾɐ́.mɐ/ 
51-
52- ( Classical Sanskrit ) IPA ( key ) : /ɕɾɐ.mɐ/
```


## [2026-09-06T21:02:52.416Z] TOOL CALL #60: Bash

```json
{
 "command": "sed -n '1,80p' tools/verify_check.py",
 "description": "Inspect verify_check tool"
}
```


### [2026-09-06T21:02:52.455Z] TOOL RESULT

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


## [2026-09-06T21:02:54.529Z] TOOL CALL #61: Bash

```json
{
 "command": "sed -n '80,140p' tools/verify_check.py",
 "description": "Rest of verify_check"
}
```


### [2026-09-06T21:02:54.574Z] TOOL RESULT

```
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


## [2026-09-06T21:03:19.443Z] TOOL CALL #62: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg269.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/269.png && cat > /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1296.vision.txt <<'EOF'\n[read from the page image of BQT_v3_picofile.pdf, pdftoppm page 83 — running head reads \"-۱۲۹۶-\" with the catch-headword «شمن» on the right, so printed page 1296 = pdf page 83 of the vol.3 scan (ref_page.py's default mapping 1296 -> pdf 87 lands on the شماس/شمان page instead; the vol.3 scan is mis-ordered around the 1291–1294 gap).]\n\nشمن * بر وزن چمن، بت پرست را گویند ۴.\nشمنان = به فتح اول و ثانی بر وزن سرطان، جمع شمن است که بت پرستان باشد؛ و کسی را نیز گویند که به سبب دویدن یا تلنگی یا برداشتن باری نفس پی‌درپی می‌زده باشد؛ و فراش و باغبان بزرگ را نیز گویند.\nشمنک = بر وزن کمند، به معنی بیهوش و بیهوشی باشد …\nشمنده = به فتح اول بر وزن رزنده، مرد دلیر و دلاور و پهلوان را گویند …\n\nحاشیهٔ معین (پانویس ۱، ذیل «شمن»):\n«در اوراق مانوی (پهلوی/پارتی) shmn (از سانسکریت śramaṇa، راهب بودایی):\nHenning, A list of Middle Persian…, BSOS, IX, 1, p. 88.\n«شرمنه» در سانسکریت کسی است که خانه و کسان خود را ترک گوید و در خلوت به ریاضت و عبادت گذراند، و به عبارت دیگر زاهد و تارک دنیا. در زبان پالی که یکی از لهجه‌های سانسکریت است و قدیمترین و معتبرترین کتب دینی بودائیان جنوبی به آن زبان نوشته شده، این واژه samaṇa آمده است («یشت‌ها»، ص ۳۹–۳۷). خود بودا را معاصران وی «سرمنه گوتمه» (= مرتاض) می‌خواندند («یشت‌ها» ۲، ص ۳۰).»\n\nشاهد شعری ذیل «شمن»: «به عاشقی چو من ایزد نیافرید صنم / به دلبری چو تو کیتی نپرورید صنم» (معزی نیشابوری).\nEOF\necho saved",
 "description": "Save BQT vision notes and page PNG"
}
```


### [2026-09-06T21:03:21.108Z] TOOL RESULT

```
saved
```


## [2026-09-06T21:04:29.945Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== BQT v1 eqlim\"; grep -n \"اقلیم\" BQT_v1_pages.txt | head -5; echo \"== LEW clima\"; grep -n -i \"clima\\b\\|clino\\|clivus\" LEW_1910.txt | head -8; echo \"== MON shaman\"; grep -n \"شمن:\" MON_part2.txt MON_part1.txt | head -5",
 "description": "Grep BQT v1, Walde LEW, Mo'in"
}
```


### [2026-09-06T21:04:30.022Z] TOOL RESULT

```
== BQT v1 eqlim
1439:مقدسی در احسن‌التقاسیم درشرح‌اقلیم خر اسان وماوراعالنپر آردا :
3239:اییون » ارغتون » اقلیمیا وغیره . ۱
13309:اقلیما بفتح اول بروزن‌مه‌سیماه نلدختر
13311:اقلیمیا ۲ بکرارلوميم وتحتانی بالف
13314:میباشد: فنی وذهبی ونحاسی ومعدنی» واقلیمیای
== LEW clima
== MON shaman
MON_part1.txt:27980:پارشمن: 0 (ا.) بوست حبوانی» 
MON_part1.txt:46334:نشمن: «صمد [ع. و .) هشت 
MON_part1.txt:61844:دشمن: 0 (۱.) آنکه ند خو اه دیگری 
MON_part1.txt:86768:شمن: 1 .( راهب بودایی یا بر همایی.
```


## [2026-09-06T21:04:31.362Z] TOOL CALL #64: Bash

```json
{
 "command": "python3 tools/fetch_source.py \"https://abadis.ir/fatofa/%D8%B4%D9%85%D9%86/\" --note \"page 269, Klem: Persian شمن in Dehkhoda/Mo'in\" 2>&1 | tail -1",
 "description": "Archive abadis shaman entry"
}
```


### [2026-09-06T21:04:34.626Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/befac29b5e5bb3a9.txt
```


## [2026-09-06T21:04:40.903Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '86760,86780p' MON_part1.txt; echo \"=== abadis shaman\"; grep -n -m3 -B2 -A8 \"فرهنگ معین\" /home/sfmqrb/git/rishe/data/verification/sources/web/befac29b5e5bb3a9.txt | head -30",
 "description": "Read Mo'in shaman entries"
}
```


### [2026-09-06T21:04:40.967Z] TOOL RESULT

```
باغ‌ها کشت می‌شو د. . برای ازدبادش یه لا 
ار قلمه استفاده می‌کنند» گیل 
نوقی. العثر. 

شمعک؛ 8-20-26 [ع. ف.] (ا.مصف.) شمع 
محافظت با دیوار مشک وکی که پیم خرایی 
آن رو د. 

شمن: 1 .( راهب بودایی یا بر همایی. 
ش_منده: (6-)3200-2002 (افا.) تر سنده» 
رمنده. هو ش شونده. آشفته شونده. بانگ 
و غریو برآورنده (از تشنگی و گرسنگی). 
شمنده: (0-)520-2002 (افا.) بو بنده. 
شسموس: 05 آمعر. چموش] (ص .) 
سر کش (اسب و استر و مانند آن)» چموش» 


۹5۸ فرهنگ فارسی معین شمول 


توسن. 
=== abadis shaman
61-نام دهی به استر آباد و ابو علی حسین بن جعفر شمنی از آنجاست . 
62-
63: فرهنگ معین
64-
65- (شَ مَ ) [ په . ] (اِ. ) ۱ - راهب بودایی یا برهمایی . ۲ - بت پرست . 
66-
67- فرهنگ عمید
68-
69- ۱. مرتاض در میان بوداییان، راهب بودایی.
70-۲. [قدیمی] بت پرست: بت پرستی گرفته ایم همه / این جهان چون بت است و ما شمنیم (رودکی: ۵۲۶ )، به عاشقی چو من ایزد نیافرید شمن / به دلبری چو تو گیتی نپرورید صنم (امیرمعزی: ۴۱۱ ). 
71-
--
178- دیکشنری آبادیس
179-
180: آبادیس از سال 1385 فعالیت خود را در زمینه فن آوری اطلاعات آغاز کرد. نخستین پروژه آبادیس، سایت دیکشنری آبادیس بود. دیکشنری آنلاین آبادیس از ابتدا تاکنون تغییرات بسیاری کرده و ویژگی های مختلفی به آن اضافه شده است. آبادیس افزونه ای کاربردی برای مرورگرهای فایرفاکس و کروم و اپلیکیشن موبایل طراحی کرده است که میتوانید از لینک های بالا دانلود کنید. دیکشنری آبادیس شامل بخش هایی نظیر دیکشنری به زبان های مختلف از جمله انگلیسی، فارسی، عربی و همچنین بیست دیکشنری تخصصی با تلفظ انگلیسی و آمریکایی، ترجمه مخفف و کلمات اختصاری، مترجم آنلاین متن، لغتنامه دهخدا، فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راهنمای انتخاب اسم و ... می باشد. 
181-
182- لینک ها 
183-
184- حقوق این سامانه وابسته به دیکشنری آبادیس می باشد. 
185-
186- استفاده از نوشتارهای این دیکشنری، با ذکر منبع، آزاد است. 
187-
188- © 2006-2026 abadis.ir
```


## [2026-09-06T21:04:48.423Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg269.png')\nim.crop((980,1030,1300,1140)).resize((1280,440)).save('crop_fr269.png')\nim.crop((580,1030,960,1170)).resize((1520,560)).save('crop_gk269.png')\n\"",
 "description": "Crop French and Greek boxes"
}
```


### [2026-09-06T21:04:50.252Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T21:04:52.732Z] TOOL CALL #67: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/crop_fr269.png"
}
```


### [2026-09-06T21:04:52.753Z] TOOL RESULT

```

```


## [2026-09-06T21:11:46.973Z] TOOL CALL #68: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build269.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\nKLEY = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%E1%B8%B1ley-\"\n\ne0nodes = []\n\ne0nodes.append({\n \"id\": 1, \"lang\": \"Avestan\", \"words\": \"sray-, srinav-, srinu-; srita, sray-\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Young Avestan verb sray- 'to lean' is the regular Iranian continuant of PIE *ḱley-: the PIE palatal *ḱ gives Proto-Iranian *s (satem development, Av. s- against Gk. k-), and PIE *l merges with *r already in Indo-Iranian, so *ḱley- > PIr. *srai- > Av. sray-. Bartholomae lists exactly the stems Nourai prints: present class 1 sray-/srī-, class 2 sraya-, class 10 (nu-present) srinav-/srinu-, perfect sisray-, and the past participle srita- 'leaned' (whence the abstract sritay- f. 'a leaning', which Bartholomae himself equates with Gk. klisis). Sanskrit śrayati 'leans', śritá- 'leaned' are the exact cognates. Nourai's second word field 'srita, sray-' is not two words but the participle srita- with a cross-reference back to the verb sray-, as printed in Bartholomae; only srita- carries the gloss 'leaned'.\",\n \"derivation_fa\": \"فعل اوستایی sray- «تکیه دادن، خم شدن» بازماندهٔ منظم ریشهٔ هندواروپایی آغازین *ḱley- است: کام‌کامی (palatal) ‏*ḱ در ایرانی باستان به s بدل می‌شود (تحول اقمار/ساتم) و *l هندواروپایی از دورهٔ هندوایرانی با r یکی شده است؛ پس *ḱley- > ایرانی باستان *srai- > اوستایی sray-. بارتولومه در «فرهنگ ایرانی باستان» دقیقاً همین ستاک‌ها را می‌آورد: sray-/srī-، sraya-، ستاک با پسوند -nav-/-nu- یعنی srinav-/srinu-، و صفت مفعولی srita- «تکیه‌داده». هم‌ریشهٔ سنسکریت آن śrayati و śritá- است. آنچه نورایی در ردیف دوم آورده («srita, sray-») دو واژه نیست؛ همان صفت مفعولی srita- است با ارجاع به فعل sray-. ادعای نورایی درست است.\",\n \"sources\": [KLEY],\n \"ref_check\": [{\"ref\": \"POK:600\", \"status\": \"supports\", \"note\": \"Pokorny IEW s.v. 'ḱlei- Meaning: to tip, incline, lean', Page(s) 600-602 (POK_full.txt line 51306ff.): 'Old Indic srayati \\\"leans, puts against\\\", srayate ..., srita- = Avestan srita- (: sray-) \\\"leaned\\\"; Avestan sray-, srinav-, srinu- \\\"lean\\\" (compare gr. κλίνω)' — verbatim Nourai's node.\"}],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"AiW col. 1636 s.v. sray-\", \"stance\": \"supports\", \"note\": \"BRT.txt line 27305: 'j. sray-, p. ϑray- V. \\\"lehnen\\\". Praes. 1 sray-: srī-, 2 sraya-, ... 10 srinav-; srinu- ...; Perf. sisray-; — PPfP. srita-'; and line 27424 'j. sritay- f. \\\"Lehnen (usw.)\\\". Zum V. sray-. — gr. κλίσις'.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"s.v. *srai, p. 355\", \"stance\": \"supports\", \"note\": \"CHEUNG.txt line ~23190-23240: Avestan sray-/srī- forms listed; '© This root has an impeccable IE etymology. «PIE *ḱlei- \\\"to lean\\\" = LIV: 332 f. | Pok.: 601 f.' with IE cognates 'Gr. κλίνω, Lat. clinare, Lith. sliéti, OHG hlinēn'.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. I 490\", \"stance\": \"supports\", \"note\": \"WLD_Bd1 line 30841ff.: 'klei- \\\"neigen, lehnen\\\" ... Ai. çrayati \\\"lehnt, legt an\\\", çrayate ..., çritá- = av. srita- (: sray-) \\\"gelehnt\\\"'.\"},\n   {\"src\": \"PHD\", \"where\": \"searched PHD.txt / PHD_mackenzie.txt\", \"stance\": \"silent\", \"note\": \"No Book-Pahlavi reflex of this verb under sr- in MacKenzie; the Middle Persian continuation is the unrelated-looking nisāy- (Cheung).\"}\n ]\n})\n\ne0nodes.append({\n \"id\": 2, \"lang\": None, \"words\": \"\",\n \"verdict\": \"unverified\",\n \"derivation\": \"Empty box. The printed page (pdf 269, book 239) really does show a blank rectangle to the right of the Avestan box, joined to it by an arrow, with no language label, no reference and no word — see data/verification/sources/refs/ocr/BOOK/269.png. The extraction is faithful; there is nothing to verify. Judging by the layout of the parallel charts (Avestan → Persian), Nourai left the slot for a New Persian reflex of Av. sray- and never filled it; no Persian reflex of this verb in fact survives (the NP words for 'lean' come from other roots).\",\n \"derivation_fa\": \"این خانه در صفحهٔ چاپی خالی است: مستطیلی بی‌برچسب زبان، بی‌ارجاع و بی‌واژه در سمت راست خانهٔ اوستایی که تنها با یک پیکان به آن پیوسته است (تصویر صفحه: data/verification/sources/refs/ocr/BOOK/269.png). خطای خوانش اسکن نیست؛ خودِ کتاب چنین چاپ کرده است. با توجه به الگوی نمودارهای دیگر (اوستایی ← فارسی)، گویا نورایی جای بازماندهٔ فارسی نو فعل sray- را باز گذاشته و پرنکرده است؛ در فارسی نو نیز بازماندهٔ روشنی از این فعل بر جای نمانده است.\",\n \"sources\": [],\n \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the box carries no reference in the book.\"}],\n \"consulted\": [\n   {\"src\": \"BOOK\", \"where\": \"printed page 239 (pdf 269), rendered at 300 dpi\", \"stance\": \"silent\", \"note\": \"the box is empty on the page itself; JSON matches the print.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"s.v. *srai, p. 355\", \"stance\": \"silent\", \"note\": \"lists MP nisāy- and dialect forms but no New Persian continuant of the simplex, consistent with an empty slot.\"}\n ]\n})\n\ne0nodes.append({\n \"id\": 3, \"lang\": \"Greek\", \"words\": \"klîma\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Greek klíma, gen. klímatos, n. 'inclination, slope of the ground, region', is a -mn̥/-mat- action noun built to klínō 'I make slope, lean' (< *ḱli-n-yō), i.e. PIE *ḱli-mn̥. Hellenistic geographers (Eratosthenes, Hipparchus, Ptolemy) used it technically of the belts of the earth's surface defined by the sun's angle and the length of the longest day, hence the 'seven klimata'; that technical geographical sense, not the plain 'slope', is what Nourai's gloss 'sloping surface or land' and the whole Arabic/Latin branch below depend on.\",\n \"derivation_fa\": \"یونانی klíma (اضافی klímatos) «شیب، سراشیبی زمین، ناحیه» اسم مصدرِ ساخته‌شده با پسوند ‎-mn̥/-mat-‎ از فعل klínō «کج کردن، خم کردن» است، یعنی *ḱli-mn̥ از همان ریشه. جغرافی‌دانان دورهٔ هلنیستی (اراتوستن، هیپارخوس، بطلمیوس) آن را اصطلاحاً برای کمربندهای زمین به‌کار بردند که بر پایهٔ زاویهٔ تابش خورشید و درازای بلندترین روز تعریف می‌شد — همان «هفت اقلیم». معنای اصطلاحیِ جغرافیایی است که شاخه‌های عربی و لاتینی زیرِ آن بر آن استوارند. ادعای نورایی درست است.\",\n \"sources\": [\"https://www.etymonline.com/word/climate\", KLEY],\n \"ref_check\": [{\"ref\": \"POK:600\", \"status\": \"supports\", \"note\": \"Pokorny 600-602 s.v. ḱlei-: 'κλίμα n. \\\"inclination, slope of ground\\\"' listed among the Greek derivatives beside κλίνω, κλίνη, κλῖμαξ.\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"KLN_1966 s.v. climate / clinical\", \"stance\": \"supports\", \"note\": \"'Gk. κλίμα, gen. κλίματος, \\\"inclination, slope, region\\\", from the stem of κλίνειν, \\\"to cause to slope, bend\\\"'.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins, klei- II.6c\", \"stance\": \"supports\", \"note\": \"AHD_watkins1985 line 635: 'suffixed form *kli-mn̥ in Greek klima, sloping surface of the earth: CLIMATE'.\"}\n ]\n})\n\ne0nodes.append({\n \"id\": 4, \"lang\": \"Arabic\", \"words\": \"eqlîm\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Arabic إِقْلِيم ʔiqlīm 'clime, zone of the earth, province', pl. أقاليم ʔaqālīm, is a straight loan of Greek klíma (acc. klíma, oblique stem klímat-), taken over during the 8th-9th c. translation movement together with Ptolemy's geography — most likely through Syriac ʔeqlīmā, which supplies the prosthetic ʔi- and the ā/ī vowel; the word was then re-analysed on the native Arabic pattern ʔifʕīl and given a broken plural. The Islamic geographers' 'seven aqālīm' (Ibn Khurradādhbih, Muqaddasī, Iṣṭakhrī) are simply the seven Greek klimata, which is why the sense drifted from 'zone of latitude' to 'province, country'. Not an inherited word: Arabic is Semitic, so this is a Greek → Arabic borrowing, exactly as Nourai's arrow shows.\",\n \"derivation_fa\": \"عربی «إقلیم» (جمع: أقالیم) وام‌واژه‌ای است مستقیم از یونانی klíma (ستاک غیرفاعلی klímat-)، که در جنبش ترجمهٔ سدهٔ دوم و سوم هجری همراه با جغرافیای بطلمیوس به عربی راه یافت — به احتمال زیاد از راه سریانی ʔeqlīmā، که همزهٔ آغازین و کشش واکه‌ها را توضیح می‌دهد؛ سپس بر وزن «إفعیل» تحلیل شد و جمع مکسر گرفت. «هفت اقلیم» جغرافی‌نویسان مسلمان (ابن خردادبه، مقدسی، اصطخری) همان هفت klimata یونانی است و از همین‌جاست که معنا از «کمربند عرضِ جغرافیایی» به «ولایت، کشور» گراییده است. چون عربی زبانی سامی است، این پیوند وام‌گیری است نه وراثت — و پیکان نورایی درست همین را نشان می‌دهد.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/%D8%A5%D9%82%D9%84%D9%8A%D9%85\"],\n \"ref_check\": [{\"ref\": \"TAD:57\", \"status\": \"supports\", \"note\": \"Tobia al-ʿUnaysī, Tafsīr al-alfāẓ al-dakhīla, is arranged by consonantal skeleton, so إقليم stands in the qāf section next to إقليد/إكليل. The Arabic OCR of TAD_pages.txt is very rough, but leaf 60 (printed ≈ 55-57) preserves the entry's definition: '... يراد به منطقة من مناطق الك[رة] الأرضية' ('a zone of the zones of the terrestrial globe'), immediately after the Greek-source marker, and the neighbouring entry reads 'إقليد وإكليل ومقلاد - يوناني [κλείς] معناه مفتاح'. Nourai's page 57 is within the ±2-leaf uncertainty of this OCR's page offset.\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"KLN_1966 s.v. climate\", \"stance\": \"partial\", \"note\": \"gives Gk. κλίμα > L. clima > F. climat but says nothing about the Arabic branch (Klein is an English dictionary) — silent rather than contrary.\"},\n   {\"src\": \"FVQ\", \"where\": \"grep 'iqlim|klima' in FVQ.txt\", \"stance\": \"silent\", \"note\": \"Jeffery has no entry: إقليم is not a Qur'anic word, so its absence is expected and carries no weight against the derivation.\"},\n   {\"src\": \"LKT\", \"where\": \"grep 'klima|iqlim' in LKT.txt\", \"stance\": \"silent\", \"note\": \"Lokotsch covers Oriental words that entered Europe; إقليم went the other way, so he has no entry.\"}\n ]\n})\n\ne0nodes.append({\n \"id\": 5, \"lang\": \"Persian\", \"words\": \"eqlîm «اقلیم»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"New Persian اقلیم eqlīm 'clime, region, country' is the Arabic ʔiqlīm taken over wholesale in the Islamic period, with the Persian pronunciation eqlīm (short e for Arabic i, as regularly in Persian) and the Arabic broken plural اقالیم kept alongside. In classical Persian it means both the geographer's 'clime' (haft eqlīm 'the seven climes' = the whole inhabited world) and simply 'country, realm' — the sense in Nourai's Saʿdī couplet 'tanat zūrmand-ast o laškar gerān / va-lēkan dar eqlīm-e došman marān' ('your body is strong and your army heavy, but do not ride into the enemy's country'). This is therefore a Greek → Arabic → Persian route, not a Persian word Arabised.\",\n \"derivation_fa\": \"«اقلیم» در فارسی نو وام‌واژه‌ای است از عربی إقلیم که در دورهٔ اسلامی یکسره به فارسی درآمده است، با تلفظ eqlīm (کسرهٔ کوتاه فارسی به‌جای i عربی) و همان جمع مکسر «اقالیم». در فارسی کلاسیک هم معنای اصطلاحی جغرافیایی دارد («هفت اقلیم» = همهٔ جهان آباد) و هم معنای ساده‌ترِ «کشور، ولایت» — همان معنا در بیت سعدی که نورایی آورده است: «تنت زورمند است و لشکر گران / ولیکن در اقلیم دشمن مران». پس مسیر یونانی ← عربی ← فارسی است، نه واژه‌ای فارسی که معرّب شده باشد. ادعای نورایی درست است.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/%D8%A7%D9%82%D9%84%DB%8C%D9%85\", \"https://abadis.ir/fatofa/%D8%A7%D9%82%D9%84%DB%8C%D9%85/\"],\n \"ref_check\": [{\"ref\": \"MON:326\", \"status\": \"supports\", \"note\": \"Mo'in, Farhang-e Fārsi s.v. اقلیم tags the word '[معر - یو.]' = معرّب – یونانی, 'Arabicised, from Greek', glossing '۱- کشور، مملکت ۲- ولایت، ج. اقالیم' (text of the entry via abadis.ir 'فرهنگ معین' section; MON_part1.txt line 15583ff. has the same entry, '[معر.] (ا.) ناحیه‌ای از کرهٔ زمین ... قدما زمین را به هفت اقلیم تقسیم کرده‌اند').\"}],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"MON_part1.txt line 15583 s.v. اقلیم + abadis 'فرهنگ معین'\", \"stance\": \"supports\", \"note\": \"'[معر - یو.]' — Mo'in himself marks the Greek source and the Arabic mediation.\"},\n   {\"src\": \"BQT\", \"where\": \"grep 'اقلیم' in BQT_v1_pages.txt\", \"stance\": \"silent\", \"note\": \"Borhān-e Qāṭeʿ has اقلیما and اقلیمیا but no entry for اقلیم itself — Tabrizi excluded plain Arabic loanwords; no counter-evidence.\"},\n   {\"src\": \"AFM\", \"where\": \"Addi Shir, al-Alfāẓ al-fārisiyya al-muʿarraba\", \"stance\": \"silent\", \"note\": \"not listed: Addi Shir collects Persian words Arabised, and إقليم is Greek, not Persian — its absence agrees with the Greek origin.\"}\n ]\n})\n\ne0nodes.append({\n \"id\": 6, \"lang\": \"Latin\", \"words\": \"clîma\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Latin clima, gen. climatis, 'region, zone of the earth', is a learned borrowing of Greek klíma with the Greek -mat- stem preserved, taken into Latin with the rest of Greek scientific geography (Pliny, Vitruvius, later Isidore). It is a borrowing, not an inherited cognate; the inherited Latin reflexes of the same root are -clīnāre, clīvus, clītellae, cliēns (node #12). Nourai's arrow Greek → Latin is therefore right, and the gloss 'a zone of earth' is the correct technical sense.\",\n \"derivation_fa\": \"لاتینی clima (اضافی climatis) «ناحیه، کمربند زمین» وام‌واژه‌ای است عالمانه از یونانی klíma با حفظ ستاک ‎-mat-‎، که همراه با جغرافیای علمی یونان به لاتینی راه یافت (پلینیوس، ویترویوس و سپس ایزیدور). این پیوند وام‌گیری است نه وراثت؛ بازماندگان ارثی همین ریشه در لاتینی ‎-clīnāre‎، clīvus، clītellae و cliēns‌اند (خانهٔ ۱۲). پس پیکان یونانی ← لاتینی نورایی درست است.\",\n \"sources\": [\"https://www.etymonline.com/word/climate\"],\n \"ref_check\": [{\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins' klei- entry routes CLIMATE through 'Greek klima, sloping surface of the earth'; the Latin intermediary clima is standard and is spelled out in Klein and Etymonline (see consulted).\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"KLN_1966 s.v. climate\", \"stance\": \"supports\", \"note\": \"'L. clima, gen. -atis, \\\"region, climate\\\", fr. Gk. κλίμα'.\"},\n   {\"src\": \"SKT\", \"where\": \"SKT.txt line 3566 s.v. clime\", \"stance\": \"supports\", \"note\": \"'clime. (L.-Gk.) L. clima ...' — Skeat likewise makes Latin clima the Greek word borrowed.\"}\n ]\n})\n\ne0nodes.append({\n \"id\": 7, \"lang\": \"English\", \"words\": \"climate\",\n \"verdict\": \"plausible\",\n \"derivation\": \"English climate is attested from the late 14th century ('horizontal zone of the earth's surface'), but its immediate donor is Old French climat, not Latin directly: OF climat < Latin clima, climatis < Greek klíma. Nourai's arrow Latin → English is right about the ultimate source but silently drops the French stage that Klein, Skeat and Etymonline all insist on; hence plausible rather than confirmed. The modern sense 'characteristic weather of a region' develops c. 1600 out of the geographers' latitude-belt, and the figurative 'moral/mental atmosphere' from the 1660s.\",\n \"derivation_fa\": \"واژهٔ انگلیسی climate از اواخر سدهٔ چهاردهم میلادی گواهی شده است، اما وام‌دهندهٔ بی‌واسطهٔ آن فرانسهٔ کهن climat است نه مستقیماً لاتینی: climat < لاتینی clima/climatis < یونانی klíma. پیکان نورایی (لاتینی ← انگلیسی) خاستگاه نهایی را درست نشان می‌دهد ولی حلقهٔ فرانسوی را — که کلاین، اسکیت و اتیمانلاین هر سه بر آن پای می‌فشارند — انداخته است؛ ازاین‌رو «با احتیاط پذیرفتنی است». معنای امروزی («آب‌وهوای ویژهٔ یک ناحیه») حدود ۱۶۰۰ از همان کمربند عرض جغرافیایی جغرافی‌دانان پدید آمد.\",\n \"sources\": [\"https://www.etymonline.com/word/climate\"],\n \"ref_check\": [{\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins klei-: '... in Greek klima, sloping surface of the earth: CLIMATE'; AHD's headword list (AHD_watkins1985 line 1371) has 'CLIMATE klei-'.\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"KLN_1966 s.v. climate\", \"stance\": \"partial\", \"note\": \"'climate, n. — F. climat, fr. L. clima ...' — French, not Latin, is the immediate source.\"},\n   {\"src\": \"SKT\", \"where\": \"SKT.txt line 23497\", \"stance\": \"partial\", \"note\": \"Skeat lists 'climate' among the words that came 'French from Low Latin from Greek'.\"}\n ]\n})\n\ne0nodes.append({\n \"id\": 8, \"lang\": \"Greek\", \"words\": \"klině; klîmax\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Two Greek nouns from the same root: klī́nē f. 'couch, bed' (< *ḱli-n-eh₂, built on the nasal present klī́nō 'I lean'), and klîmax f. 'ladder, staircase' (< *ḱli-m-ak-, literally 'the leaning thing', a ladder being propped against a wall). Nourai's 'klině' uses the book's ě for long ē, i.e. klī́nē — not a misprint but his house transliteration (compare cliěns in node #12). Both nouns feed the modern learned vocabulary: klī́nē → klīnikós 'of the bedside' → clinic (#9), klîmax → climax (#11).\",\n \"derivation_fa\": \"دو اسم یونانی از یک ریشه: klī́nē «بستر، تخت» (از *ḱli-n-eh₂، ساخته بر ستاک حال با میان‌وند نونیِ klī́nō «کج می‌کنم») و klîmax «نردبان، پلکان» (از *ḱli-m-ak-، تحت‌اللفظ «چیزِ تکیه‌داده»، چون نردبان را به دیوار تکیه می‌دهند). آنچه نورایی «klině» نوشته همان klī́nē است؛ در این کتاب ě نشانهٔ ē کشیده است (مانند cliěns در خانهٔ ۱۲) و خطای چاپی نیست. هر دو واژه به واژگان علمی نو راه یافته‌اند: klī́nē ← klīnikós ← clinic؛ klîmax ← climax. ادعای نورایی درست است.\",\n \"sources\": [\"https://www.etymonline.com/word/climax\", \"https://www.etymonline.com/word/clinic\"],\n \"ref_check\": [{\"ref\": \"AHD:1523\", \"status\": \"supports\", \"note\": \"The 1975 New College appendix page number cannot be checked against our copy (the 1985 standalone Watkins edition has its own pagination), but the content is exact: AHD_watkins1985 line 635, klei- II.6: 'Greek lengthened form *klī- in: a. suffixed form *klī-n-ā in Greek klinē, bed: CLINIC ...; b. suffixed form *klī-m- in Greek klimax, ladder: CLIMAX'.\"}],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"IEW 600-602 s.v. ḱlei-\", \"stance\": \"supports\", \"note\": \"'κλίνη \\\"bed\\\", κλιντήρ, κλισμός \\\"couch, bed, place for resting\\\" ... κλῖμαξ f. \\\"ladder\\\"'.\"},\n   {\"src\": \"KLN\", \"where\": \"KLN_1966 s.v. clinical, climax\", \"stance\": \"supports\", \"note\": \"'κλίνη, \\\"bed\\\", which is rel. to κλίνειν ... κλῖμαξ, \\\"ladder\\\", κλιμακτήρ, \\\"rung of a ladder\\\" ... fr. I.-E. base *klei-'.\"}\n ]\n})\n\ne0nodes.append({\n \"id\": 9, \"lang\": \"French\", \"words\": \"clinic\",\n \"verdict\": \"transcription_suspect\",\n \"error_in\": \"book\",\n \"book_prints\": \"clinic\",\n \"correct_form\": \"clinique\",\n \"derivation\": \"The chain itself is right — Gk. klī́nē 'bed' → klīnikós 'of/at the bedside' → Late Latin clīnicus 'physician who visits patients in their beds' → French clinique (17th c.) — but the form in the French box is wrong: French is clinique, not 'clinic'. The printed page really does read 'clinic' under the header 'French' (see the crop of pdf page 269 saved as data/verification/sources/refs/ocr/BOOK/269.png), so the extraction is faithful and the error is Nourai's own: he has put the English spelling in the French box. English clinic (1620s, first 'a bedridden person') is itself borrowed from French clinique, so the box conflates the two.\",\n \"derivation_fa\": \"زنجیره درست است — یونانی klī́nē «بستر» ← klīnikós «بالینی» ← لاتینی متأخر clīnicus «پزشکی که بر بالین بیمار می‌رود» ← فرانسوی clinique (سدهٔ هفدهم) — اما صورتِ درون خانه نادرست است: در فرانسه clinique است نه clinic. تصویر صفحهٔ چاپی (data/verification/sources/refs/ocr/BOOK/269.png) نشان می‌دهد که خودِ کتاب زیر عنوان «French» واژهٔ «clinic» را چاپ کرده است؛ پس خطای خوانش اسکن نیست، خطای چاپی/سهو خودِ نورایی است که املای انگلیسی را در خانهٔ فرانسوی گذاشته. انگلیسی clinic (۱۶۲۰م، نخست به معنی «بیمار بستری») خود وام‌گرفته از همان clinique فرانسوی است.\",\n \"sources\": [\"https://www.etymonline.com/word/clinic\"],\n \"ref_check\": [{\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins klei- II.6a routes CLINIC through 'Greek klinē, bed'; AHD does not print the French form, so it neither confirms nor corrects the spelling 'clinic'.\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"KLN_1966 s.v. clinical\", \"stance\": \"partial\", \"note\": \"'L. clinicus, fr. Gk. κλινικός, \\\"a physician who attends patients in their beds\\\" ... fr. κλίνη, \\\"bed\\\"' — Latin clīnicus is the immediate source of the French adjective; Klein spells the French word clinique elsewhere, never 'clinic'.\"},\n   {\"src\": \"BOOK\", \"where\": \"printed page 239 (pdf 269), 300 dpi crop\", \"stance\": \"supports\", \"note\": \"the box header reads 'French  AHD' and the word line reads 'clinic'; JSON matches the print exactly, so the fault is the book's.\"}\n ]\n})\n\ne0nodes.append({\n \"id\": 10, \"lang\": \"Persian\", \"words\": \"kelînîk «کلینیک»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Persian کلینیک kelīnīk 'clinic, out-patient department' is a 20th-century loan straight from French clinique, borrowed with the whole French medical vocabulary during the Qajar/early Pahlavi modernisation of Iranian medicine (compare پلی‌کلینیک poli-klīnīk, کلینیکال). The French final -que [k] is rendered by Persian ک, and the French nasal-free [kli-] is broken up by an anaptyctic e (ke-lī-nīk) because Persian does not tolerate initial clusters. Mo'in tags the word '[فر.]', i.e. French, and Dehkhoda 'فرانسوی' — exactly Nourai's arrow.\",\n \"derivation_fa\": \"«کلینیک» وام‌واژه‌ای است از فرانسوی clinique که در سدهٔ چهاردهم خورشیدی همراه با کل واژگان پزشکی فرانسوی در دورهٔ نوسازی پزشکی ایران وارد فارسی شد (مقایسه کنید با «پلی‌کلینیک»). ‎-que‎ پایانی فرانسوی به «ک» بدل شده و چون فارسی خوشهٔ همخوانی آغازین را برنمی‌تابد، میان k و l کسرهٔ میانجی افزوده شده است: ke-lī-nīk. معین این واژه را «[فر.]» و دهخدا «فرانسوی» برچسب می‌زند — همان چیزی که پیکان نورایی نشان می‌دهد. ادعای نورایی درست است.\",\n \"sources\": [\"https://abadis.ir/fatofa/%DA%A9%D9%84%DB%8C%D9%86%DB%8C%DA%A9/\"],\n \"ref_check\": [{\"ref\": \"MON:3051\", \"status\": \"supports\", \"note\": \"Mo'in, Farhang-e Fārsi s.v. کلینیک: '(کِ) [ فر. ] ۱- (اِ.) ساختمان یا بخشی در بیمارستان ... درمانگاه. ۲- (ص.) بالینی' — the tag [فر.] = French is Mo'in's own origin label (entry text via abadis.ir 'فرهنگ معین'; the print page number 3051 could not be checked because the OCR of MON_part1/2 loses the page numbering).\"}],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"abadis.ir 'فرهنگ معین' s.v. کلینیک\", \"stance\": \"supports\", \"note\": \"'[ فر. ]' — French origin stated by Mo'in.\"},\n   {\"src\": \"ARY\", \"where\": \"Dehkhoda, Loghatnāme s.v. کلینیک (via abadis)\", \"stance\": \"supports\", \"note\": \"'کلینیک. [ کْلی / کِ ] ( فرانسوی، اِ ) مطب. محکمه. (فرهنگ فارسی معین). || درمانگاه.' — a second Persian lexicographer marking the word فرانسوی.\"}\n ]\n})\n\ne0nodes.append({\n \"id\": 11, \"lang\": \"English\", \"words\": \"climax\",\n \"verdict\": \"plausible\",\n \"derivation\": \"English climax appears in 1580s as a term of rhetoric ('a series of propositions rising in force'), taken from Late Latin climax, gen. climacis, itself the Greek klîmax 'ladder' used metaphorically by the Greek rhetoricians. Nourai's direct Greek → English arrow is right about the source word but skips the Latin transmission that Klein ('climax, n. L., fr. Gk. κλῖμαξ') and Etymonline ('from Late Latin climax ... from Greek klimax') both record; hence plausible. The sense 'high point, culmination' is a late-18th-century misunderstanding of the rhetorical term, and 'sexual orgasm' is recorded from 1880.\",\n \"derivation_fa\": \"واژهٔ انگلیسی climax در دههٔ ۱۵۸۰م نخست اصطلاحی بلاغی بود («زنجیره‌ای از گزاره‌ها که پله‌پله نیرومندتر می‌شوند») و از لاتینی متأخر climax (اضافی climacis) گرفته شده که خود همان klîmax یونانی «نردبان» است در کاربرد استعاری بلاغیان یونان. پیکان مستقیم نورایی (یونانی ← انگلیسی) واژهٔ خاستگاه را درست می‌گوید اما حلقهٔ لاتینی را — که کلاین و اتیمانلاین هر دو ثبت کرده‌اند — می‌اندازد؛ پس «با احتیاط پذیرفتنی است». معنای «اوج» برداشتی نادرست از همان اصطلاح بلاغی در اواخر سدهٔ هجدهم است.\",\n \"sources\": [\"https://www.etymonline.com/word/climax\"],\n \"ref_check\": [{\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985 line 1371 index: 'CLIMAX klei-'; klei- II.6b: 'suffixed form *klī-m- in Greek klimax, ladder: CLIMAX'.\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"KLN_1966 s.v. climax\", \"stance\": \"partial\", \"note\": \"'climax, n. L., fr. Gk. κλῖμαξ, \\\"ladder\\\", lit. \\\"something sloping, something leading up by degrees\\\"' — Latin is the immediate donor.\"},\n   {\"src\": \"SKT\", \"where\": \"SKT.txt line 3566\", \"stance\": \"partial\", \"note\": \"'climax. the highest degree. (Gk.) κλῖμαξ, a ladder, staircase, highest expression (in rhetoric). — Gk. κλίνειν, slope.'\"}\n ]\n})\n\ne0nodes.append({\n \"id\": 12, \"lang\": \"Latin\", \"words\": \"clîmâre; cliěns\",\n \"verdict\": \"transcription_suspect\",\n \"error_in\": \"book\",\n \"book_prints\": \"clîmâre\",\n \"correct_form\": \"clīnāre\",\n \"derivation\": \"The Latin verb meaning 'to lean, bend' is clīnāre (attested only in compounds: dēclīnāre, inclīnāre, reclīnāre), from *ḱli-n-. There is no Latin *clīmāre; the printed page unambiguously shows 'clîmâre' (300-dpi crop of pdf 269, saved as data/verification/sources/refs/ocr/BOOK/269.png), so the extraction is faithful and this is Nourai's own misprint — an m for n, probably contaminated by clīma two boxes above. The second word is fine: cliēns, gen. clientis, 'dependant, client' < *ḱli-ent- 'one who leans on another' (Klein: 'the usual derivation of L. cliens from the stem of cluere, \\\"to be named\\\", is erroneous'); the book's 'cliěns' is just its house spelling of long ē, as in klině in node #8.\",\n \"derivation_fa\": \"فعل لاتینی به معنی «خم شدن، تکیه دادن» clīnāre است (تنها در ترکیب‌ها گواهی شده: dēclīnāre، inclīnāre، reclīnāre) از *ḱli-n-. در لاتینی *clīmāre وجود ندارد. تصویر ۳۰۰ نقطه‌ای صفحه (data/verification/sources/refs/ocr/BOOK/269.png) به‌روشنی «clîmâre» را نشان می‌دهد؛ پس خطای خوانش اسکن نیست، خطای چاپیِ خودِ کتاب است — m به‌جای n، احتمالاً زیر تأثیر clîma که دو خانه بالاتر آمده. واژهٔ دوم درست است: cliēns (اضافی clientis) «وابسته، دست‌نشانده» از *ḱli-ent- «آن‌که بر دیگری تکیه می‌کند»؛ صورت «cliěns» کتاب هم فقط شیوهٔ نگارش ē کشیده در همین کتاب است (مانند klině در خانهٔ ۸).\",\n \"sources\": [\"https://www.etymonline.com/word/client\", KLEY],\n \"ref_check\": [{\"ref\": \"AHD:1523\", \"status\": \"contradicts\", \"note\": \"The very reference Nourai cites prints the correct form: AHD_watkins1985 line 633, klei- I.1: 'Suffixed form *klei-n- in Latin -clīnāre, to lean, bend: DECLINE, INCLINE, RECLINE', and II.3: 'Suffixed form *kli-ent- in Latin cliēns, dependent, follower: CLIENT'. So AHD supports the arrow and the word cliēns but shows that 'clîmâre' is wrong for clīnāre.\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"KLN_1966 s.v. clinical, client\", \"stance\": \"contradicts\", \"note\": \"'L. -clinare (with the exception of the pp. clinatus, occurring only in compounds), \\\"to bend, turn\\\"' and 'client, n. — F., fr. L. clientem, acc. of cliens ... fr. I.-E. base *klei-' — clīnāre, never clīmāre.\"},\n   {\"src\": \"POK\", \"where\": \"IEW 600-602 s.v. ḱlei-\", \"stance\": \"contradicts\", \"note\": \"'Latin clīno, -are \\\"bend, bow, incline\\\" ... acclīnis ... cliens, -tis \\\"a personal dependant, client\\\"' — again clīno/clīnāre.\"},\n   {\"src\": \"BOOK\", \"where\": \"printed page 239 (pdf 269), 300 dpi crop\", \"stance\": \"supports\", \"note\": \"the page really prints 'clîmâre : to lean, bend' — the JSON reproduces the book correctly; the fault is the book's.\"}\n ]\n})\n\ne0nodes.append({\n \"id\": 13, \"lang\": \"English\", \"words\": \"decline, incline, recline; client\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"All four are Latin words taken into English through French: dēclīnāre > OF decliner > ME declinen (c. 1300); inclīnāre > OF encliner/incliner > ME enclinen; reclīnāre entered later as a Latinism (1520s in the sense 'lay down', 1660s 'lean back'); and cliēns/clientem > Anglo-French clyent (c. 1300) > English client 'one who lives under the patronage of another' (late 14c.), the modern 'a lawyer's customer' from c. 1400. The prefixes are Latin dē- 'down', in- 'into, towards', re- 'back' on the same *ḱli-n- stem, so the whole box is a single derivational family.\",\n \"derivation_fa\": \"هر چهار واژه لاتینی‌اند که از راه فرانسوی به انگلیسی رسیده‌اند: dēclīnāre ← فرانسهٔ کهن decliner ← انگلیسی میانه declinen (حدود ۱۳۰۰م)؛ inclīnāre ← encliner/incliner ← enclinen؛ reclīnāre دیرتر همچون واژه‌ای عالمانه وارد شد (۱۵۲۰م به معنی «خواباندن»، ۱۶۶۰م «به عقب تکیه دادن»)؛ و cliēns/clientem ← انگلیسی-فرانسوی clyent (حدود ۱۳۰۰م) ← client «کسی که در پناه دیگری می‌زید» (اواخر سدهٔ چهاردهم)، و از حدود ۱۴۰۰م «موکّل». پیشوندهای لاتینی dē- «فرود»، in- «به‌سوی» و re- «بازپس» بر همان ستاک *ḱli-n- نشسته‌اند. ادعای نورایی درست است.\",\n \"sources\": [\"https://www.etymonline.com/word/client\"],\n \"ref_check\": [{\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985 klei- I.1 lists exactly 'DECLINE, INCLINE, RECLINE' under Latin -clīnāre and II.3 'CLIENT' under cliēns; the index lines 1416/1676/2174 confirm 'DECLINE klei-', 'INCLINE klei-', 'RECLINE klei-'.\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"KLN_1966 s.v. client\", \"stance\": \"supports\", \"note\": \"'client, n. — F., fr. L. clientem, acc. of cliens, \\\"retainer, follower, dependent\\\", lit. \\\"one who leans on another\\\"'.\"},\n   {\"src\": \"POK\", \"where\": \"IEW 600-602\", \"stance\": \"supports\", \"note\": \"Latin clīno/-clīnāre and cliens are both listed as reflexes of ḱlei-.\"}\n ]\n})\n\ne0nodes.append({\n \"id\": 14, \"lang\": \"Germanic\", \"words\": \"hliněn; hlaider; hlid\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Three Proto-Germanic formations on the zero grade *hli- (< PIE *ḱli-): (a) *hlinēn 'to lean' (weak verb, OHG (h)linēn, OS hlinon, OE hlinian/hleonian) — Nourai's 'hliněn' with ě = ē is exact; (c) *hlid- 'cover, that which bends over' (OE hlid, ON hlið, OHG hlit) — exact. (b) is the weak point: the standard reconstruction of the ladder word is *hlaidri- / *hlaidrī (OE hlǣd(d)er, OFris. hledere, OHG leitara, Ger. Leiter), and no Germanic *hlaider is reconstructed with that shape; Nourai's 'hlaider' is a simplified quasi-Old-English spelling rather than a real Proto-Germanic form. The derivations themselves are all standard; only the middle form is loosely written, so plausible rather than confirmed.\",\n \"derivation_fa\": \"سه ساخت ژرمنی آغازین بر پایهٔ درجهٔ صفر *hli- (از *ḱli- هندواروپایی): (الف) *hlinēn «تکیه دادن» (فعل ضعیف؛ آلمانی علیای کهن (h)linēn، ساکسون کهن hlinon، انگلیسی کهن hlinian/hleonian) — همان «hliněn» نورایی، که در آن ě نشانهٔ ē است؛ (ج) *hlid- «سرپوش، آنچه روی چیزی خم می‌شود» (انگلیسی کهن hlid، نورس کهن hlið، آلمانی علیای کهن hlit) — درست. اما (ب) سست است: بازسازی پذیرفته برای واژهٔ «نردبان» *hlaidri-/*hlaidrī است (انگلیسی کهن hlǣd(d)er، فریزی کهن hledere، آلمانی علیای کهن leitara، آلمانی Leiter) و صورتی به شکل *hlaider در ژرمنی آغازین بازسازی نشده است؛ «hlaider» نورایی املایی ساده‌شده و شبه‌انگلیسی‌کهن است نه صورت ژرمنی آغازین. خودِ اشتقاق‌ها همه معیارند و تنها صورت میانی سرسری نوشته شده؛ ازاین‌رو «با احتیاط پذیرفتنی است».\",\n \"sources\": [\"https://www.etymonline.com/word/ladder\", \"https://www.etymonline.com/word/lid\"],\n \"ref_check\": [{\"ref\": \"AHD:1523\", \"status\": \"partial\", \"note\": \"AHD_watkins1985 line 635 gives 'Germanic *hlid-, \\\"that which bends over,\\\" cover, in Old English hlid, cover: LID' and '*kli-n- in Germanic *hlinēn, in Old English hlinian and hleonian, to lean: LEAN', but for the ladder III reads 'Suffixed o-grade form *kloi-tr- in Germanic *hlaidr- in Old English hlǣd(d)er, ladder: LADDER' — *hlaidr-, not 'hlaider'.\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"KLN_1966 s.v. ladder\", \"stance\": \"partial\", \"note\": \"'ladder, n. — ME. laddre, fr. OE. hlǣder, hlædder, rel. to OFris. hledere, MDu. ledere ..., OHG. leitara ... fr. I.-E. base *kli-' — the Germanic base is *hlaidr-, no form 'hlaider'.\"},\n   {\"src\": \"POK\", \"where\": \"IEW 600-602\", \"stance\": \"supports\", \"note\": \"'Old High German (h)linēn \\\"lean\\\" ... Old High German (h)leitara \\\"ladder\\\", Old English hlǣd(d)er ds.; Old English -hlīdan \\\"cover\\\", hlid n. \\\"cover, door\\\", Old High German lid \\\"cover\\\"'.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann, IEC.txt line 8928\", \"stance\": \"supports\", \"note\": \"'WP I, 490 ... OHG hlinen \\\"lean, lie down\\\"; MHG linen, lenen; OS hlinon; OE hlinian \\\"lean, lie down\\\"'.\"}\n ]\n})\n\ne0nodes.append({\n \"id\": 15, \"lang\": \"English\", \"words\": \"lean; ladder; lid\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"The three English words are the direct inherited continuations of the Germanic forms in the box above: OE hlinian/hleonian > ME lenen > lean (the initial hl- cluster lost its h in early Middle English, as in hlāf > loaf); OE hlǣd(d)er > ME laddre > ladder (the same hl- > l-, with -dd- from the geminate); OE hlid 'covering, opening, gate' > ME lid > lid, with 'eyelid' from the early 13th century. All three are attested in Old English, so no borrowing is involved anywhere in this branch.\",\n \"derivation_fa\": \"این سه واژهٔ انگلیسی بازماندگان ارثیِ مستقیم صورت‌های ژرمنی خانهٔ بالایند: انگلیسی کهن hlinian/hleonian ← انگلیسی میانه lenen ← lean (خوشهٔ آغازین hl- در آغاز دورهٔ انگلیسی میانه h خود را از دست داد، مانند hlāf ← loaf)؛ انگلیسی کهن hlǣd(d)er ← laddre ← ladder؛ انگلیسی کهن hlid «پوشش، در» ← lid، که از اوایل سدهٔ سیزدهم معنی «پلک» نیز یافته است. هر سه در انگلیسی کهن گواهی شده‌اند، پس در این شاخه هیچ وام‌گیری در کار نیست. ادعای نورایی درست است.\",\n \"sources\": [\"https://www.etymonline.com/word/ladder\", \"https://www.etymonline.com/word/lid\"],\n \"ref_check\": [{\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985 index lines 1726, 1739, 1742: 'LADDER klei-', 'LEAN! klei-', 'LID. klei-'; the klei- entry itself routes each through the Old English forms.\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"KLN_1966 s.v. ladder\", \"stance\": \"supports\", \"note\": \"'ladder, n. — ME. laddre, fr. OE. hlǣder ... See lean, v., and cp. climax, clinical.'\"},\n   {\"src\": \"SKT\", \"where\": \"SKT.txt line 9844 s.v. Ladder\", \"stance\": \"supports\", \"note\": \"'Ladder. (E.) ME. laddre. A.S. hlæder, a ladder. + Du. ladder ...; O.H.G. hleitra, G. Leiter, a ladder.'\"}\n ]\n})\n\nentry0 = {\n \"entry\": 0,\n \"root\": \"Klei\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *ḱley- 'to lean, incline, slope' (Pokorny ḱlei-, IEW 600-602; LIV 332f.)\",\n \"note\": \"Root, language label and gloss are all correct. Pokorny's headword is ḱlei- with a palatal (Nourai's 'Klei' loses the diacritic, as he does throughout), the meaning is 'to tip, incline, lean', and the page is 600 (the article runs 600-602), so POK:600 is exact. Every branch on the chart is one Pokorny prints under that lemma: Av. sray-/srita-, Gk. klínō/klíma/klínē/klîmax, Lat. clīnāre/cliēns/clīvus, Gmc. hlinēn/hleitara/hlid. Two flags on this entry: node #12 prints a non-existent Latin 'clîmâre' for clīnāre, and node #9 puts the English spelling 'clinic' in a French box (French is clinique) — both are the book's own errors, not extraction errors. Node #2 is a genuinely empty box on the printed page. The three English boxes (#7 climate, #11 climax, #13) silently skip the French/Latin intermediaries that Klein, Skeat and Etymonline record.\",\n \"note_fa\": \"ریشه، برچسب زبان و معنای آن هر سه درست است. سرواژهٔ پوکورنی ḱlei- با کام‌کامی است (نورایی مانند همه‌جا نشانهٔ کام‌کامی را نمی‌آورد) و معنای آن «کج شدن، خم شدن، تکیه دادن»، در صفحهٔ ۶۰۰ (مقاله از ۶۰۰ تا ۶۰۲)، پس ارجاع POK:600 دقیق است. هر شاخهٔ این نمودار در همان مدخل پوکورنی هست: اوستایی sray-/srita-، یونانی klínō/klíma/klī́nē/klîmax، لاتینی clīnāre/cliēns/clīvus، ژرمنی hlinēn/hleitara/hlid. دو نکتهٔ هشدار: خانهٔ ۱۲ صورت ناموجود لاتینی «clîmâre» را به‌جای clīnāre چاپ کرده و خانهٔ ۹ املای انگلیسی «clinic» را در خانهٔ فرانسوی نشانده است (در فرانسه clinique است) — هر دو خطای خودِ کتاب است نه خطای استخراج. خانهٔ ۲ در صفحهٔ چاپی به‌راستی خالی است. سه خانهٔ انگلیسی (۷ climate، ۱۱ climax، ۱۳) حلقه‌های میانی فرانسوی/لاتینی را که کلاین، اسکیت و اتیمانلاین ثبت کرده‌اند نادیده گرفته‌اند.\",\n \"sources\": [KLEY, \"https://www.etymonline.com/word/climate\"],\n \"ref_check\": [{\"ref\": \"POK:600\", \"status\": \"supports\", \"note\": \"POK_full.txt line 51306ff.: 'Root / lemma: ḱlei- | Meaning: to tip, incline, lean | Material: Old Indic srayati \\\"leans\\\" ... Avestan sray-, srinav-, srinu- \\\"lean\\\" ... gr. κλίνω ... κλῖμα n. \\\"inclination, slope of ground\\\", κλῖμαξ f. \\\"ladder\\\" ... Latin clīno, -are \\\"bend, bow, incline\\\" ... cliens, -tis ... Old High German (h)linēn \\\"lean\\\" ... (h)leitara \\\"ladder\\\" ... hlid n. \\\"cover, door\\\". References: WP. I 490 ff. ... Page(s): 600-602'.\"}],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. I 490\", \"stance\": \"supports\", \"note\": \"'klei- \\\"neigen, lehnen\\\"; vielfach von angelehnten Stangen (daher Zelte mit Stangengerippe: Sattelstangen, Leitern ...), andrerseits von Berglehnen, Hügeln u. dgl.'\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985, klei-\", \"stance\": \"supports\", \"note\": \"'klei-. To lean. ... [Pok. ḱlei- 600.]' — Watkins' bracketed cross-reference is Nourai's own POK:600.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann, IEC.txt line 8928\", \"stance\": \"supports\", \"note\": \"'Cf. Kleio and Klit-. WP I, 490. Av. -sirinaomi, cpds.; Gk. klinō, tr. intr. \\\"lean, bend, tilt\\\"; Lat. clino, -are, id.; ... OE hlinian \\\"lean, lie down\\\"; Li. šlynù, šlýti \\\"incline, lean\\\".'\"},\n   {\"src\": \"CHEUNG\", \"where\": \"s.v. *srai, p. 355\", \"stance\": \"supports\", \"note\": \"'«PIE *ḱlei- \\\"to lean\\\" = LIV: 332 f. | Pok.: 601 f.' — the current Iranian-verb handbook keeps the same root.\"}\n ],\n \"nodes\": e0nodes\n}\n\ne1nodes = []\n\ne1nodes.append({\n \"id\": 1, \"lang\": \"Sanskrit\", \"words\": \"sramana, saman\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Sanskrit श्रमण śramaṇá- is real and is exactly the word that gives the whole branch, but Nourai's gloss inverts its sense. It is built on the root śram- 'to toil, exert oneself, wear oneself out (esp. with religious austerities)' (śrāmyati, śrama- m. 'toil, weariness'), so śramaṇá- means 'one who exerts himself, ascetic, mendicant', and only secondarily 'Buddhist/Jain monk' — not 'a dull person'. Pokorny does put śramyati under klem- 'weak, ailing, feeble' (the semantic bridge being 'wear oneself out' → 'be weary'), and he explicitly connects śramaṇa- with the word Schamane; but he flags the difficulty himself ('the ambiguity of the liquid complicates the judgment', śram- beside klam-), and Mayrhofer's EWAia gives śram- no secure PIE etymology. The second form 'saman' is not Sanskrit at all: it is the Middle Indic (Pali/Prakrit) samaṇa, which is what Mo'in's footnote in Borhān-e Qāṭeʿ actually cites, and which is the shape that reached Iranian and Chinese. Hence plausible: right word, wrong gloss, and one form mislabelled.\",\n \"derivation_fa\": \"سنسکریت श्रमण śramaṇá- واژه‌ای واقعی است و سرچشمهٔ همهٔ این شاخه، اما معنایی که نورایی داده وارونه است. این واژه از ریشهٔ śram- «کوشیدن، رنج بردن، خود را در ریاضت فرسودن» ساخته شده (śrāmyati، śrama- «رنج، خستگی»)، پس śramaṇá- یعنی «آن‌که خود را به رنج می‌افکند، مرتاض، زاهد» و تنها به‌طور ثانوی «راهب بودایی/جینی» — نه «آدم کودن». پوکورنی śramyati را زیر klem- «ناتوان، بیمارگون، سست» آورده (پل معنایی: «خود را فرسودن» ← «خسته بودن») و آشکارا śramaṇa- را به Schamane پیوند می‌زند؛ ولی خود او دشواری کار را گوشزد می‌کند («دوگانگی روان‌واک [r/l] داوری را دشوار می‌کند»، śram- در برابر klam-) و مایرهوفر در EWAia برای śram- ریشه‌شناسی هندواروپایی مطمئنی نمی‌آورد. صورت دوم «saman» اصلاً سنسکریت نیست: همان samaṇa هندی میانه (پالی/پراکریت) است — همان که معین در حاشیهٔ برهان قاطع نقل می‌کند و همان صورتی که به ایرانی و چینی رسیده است. پس: واژه درست، معنا نادرست، و یکی از دو صورت برچسبِ زبانی نادرست دارد؛ «با احتیاط پذیرفتنی است».\",\n \"sources\": [\"https://en.wiktionary.org/wiki/%E0%A4%B6%E0%A5%8D%E0%A4%B0%E0%A4%AE%E0%A4%A3\", \"https://en.wiktionary.org/wiki/%E0%A4%B6%E0%A5%8D%E0%A4%B0%E0%A4%AE\"],\n \"ref_check\": [{\"ref\": \"POK:602\", \"status\": \"supports\", \"note\": \"POK_full.txt line 47419ff.: 'Root / lemma: klem-, klēm- | Meaning: weak, ailing, feeble | Material: Old Indic ... śramyati \\\"becomes tired, struggles, castigates oneself\\\", śrānta- \\\"fatigued, exhausted\\\", śrama- m. \\\"fatigue, tiredness\\\"; śramaṇa- \\\"castigating, mendicant\\\" is to East Asiatic languages as Schamane \\\"shaman, magician\\\" ... Page(s): 602-603'. Pokorny thus carries both the word and the shaman connection Nourai builds on — though he adds '(Indo Germanic change chain of events?); also the ambiguity of the liquid complicates the judgment'.\"}],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny I 498 (as cited by IEW)\", \"stance\": \"supports\", \"note\": \"Pokorny's own 'References: WP. I 498' for klem-, i.e. Walde-Pokorny is where the Sanskrit material is set out.\"},\n   {\"src\": \"BQT\", \"where\": \"Borhān-e Qāṭeʿ vol. 3, printed p. 1296, Mo'in's footnote 1 s.v. شمن\", \"stance\": \"partial\", \"note\": \"'«شرمنه» در سانسکریت کسی است که خانه و کسان خود را ترک گوید و در خلوت به ریاضت و عبادت گذراند ... زاهد و تارک دنیا. در زبان پالی ... این واژه samaṇa آمده است' — Mo'in glosses śramaṇa as 'ascetic, world-renouncer', not 'dull', and assigns samaṇa to Pali, not Sanskrit.\"},\n   {\"src\": \"IEC\", \"where\": \"grep 'klem-|sramana' in IEC.txt\", \"stance\": \"silent\", \"note\": \"Mann has no entry joining śram- to klem-; no support, no contradiction.\"}\n ]\n})\n\ne1nodes.append({\n \"id\": 2, \"lang\": \"Pahlavi\", \"words\": \"šaman\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Middle Persian/Parthian šmn /šaman/ 'Buddhist monk' is attested in the Manichaean documents from Turfan (Henning, 'A List of Middle Persian and Parthian Words', BSOS IX/1, p. 88), beside Sogdian šmn 'monk'. It is a Buddhist technical term borrowed into Iranian from Middle Indic — Gāndhārī ṣamana / Prakrit-Pali samaṇa < Skt. śramaṇa — in the Kushan and post-Kushan Buddhist milieu of Bactria and Sogdiana, whence Chinese 沙門 shāmén and Tocharian B ṣamāne. So the arrow is a borrowing, not an inheritance (an inherited Iranian reflex of PIE *ḱlem- would not look like this), and the gloss shifts from 'Buddhist monk' in Middle Persian to 'idol-worshipper' in the Islamic-period sources, once Buddhist and Hindu images were the paradigm of 'idols' for Muslim Persians. MacKenzie's Book-Pahlavi dictionary has no entry because the word is confined to the Manichaean corpus.\",\n \"derivation_fa\": \"صورت فارسی میانه/پارتی šmn ‏/šaman/ «راهب بودایی» در اسناد مانوی تورفان گواهی شده است (هنینگ، فهرست واژه‌های فارسی میانه و پارتی، BSOS، جلد ۹ بخش ۱، ص ۸۸)، در کنار سغدی šmn «راهب». این اصطلاحی بودایی است که از هندی میانه — گاندهاری ṣamana / پالی و پراکریت samaṇa، از سنسکریت śramaṇa — در محیط بودایی بلخ و سغد دورهٔ کوشانی و پس از آن به ایرانی راه یافته و از همان‌جا به چینی 沙門 shāmén و تخاری ṣamāne رسیده است. پس این پیکان وام‌گیری است نه وراثت (بازماندهٔ ارثیِ *ḱlem- در ایرانی چنین صورتی نمی‌یافت)، و معنا از «راهب بودایی» در فارسی میانه به «بت‌پرست» در متون دورهٔ اسلامی گراییده است، چون برای مسلمانان ایرانی پیکره‌های بودایی و هندو نمونهٔ آشکار «بت» بودند. فرهنگ پهلوی مکنزی این واژه را ندارد، زیرا تنها در پیکرهٔ مانوی به کار رفته است. ادعای نورایی درست است.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/%D8%B4%D9%85%D9%86\", \"https://en.wiktionary.org/wiki/shaman\"],\n \"ref_check\": [{\"ref\": \"TZF:77\", \"status\": \"not_checked\", \"note\": \"Abolghasemi, Tārikh-e Mokhtaṣar-e Zabān-e Fārsi (Bonyād-e Andisheh-ye Eslāmi 1373) — refs_online.json records no downloadable copy (ketabnak requires login; not on archive.org), so p. 77 could not be read.\"}],\n \"consulted\": [\n   {\"src\": \"BQT\", \"where\": \"Borhān-e Qāṭeʿ vol. 3, printed p. 1296, Mo'in's footnote 1 s.v. شمن\", \"stance\": \"supports\", \"note\": \"'در اوراق مانوی (پهلوی/پارتی) shmn (از سانسکریت śramaṇa، راهب بودایی): Henning, A list of Middle Persian…, BSOS, IX, 1, p. 88.' — exactly Nourai's Sanskrit → Pahlavi arrow, with the primary reference. Page confirmed from the scan's running head '-۱۲۹۶-' with catchword «شمن» (pdftoppm page 83 of BQT_v3_picofile.pdf); saved as data/verification/sources/refs/ocr/BQT/1296.vision.txt.\"},\n   {\"src\": \"PHD\", \"where\": \"grep 'šaman|šmn' in PHD.txt / PHD_mackenzie.txt\", \"stance\": \"silent\", \"note\": \"MacKenzie has no šaman; the only smn is yāsaman 'jasmine'. Expected: CPD covers Book Pahlavi, not the Manichaean lexicon.\"},\n   {\"src\": \"NYB\", \"where\": \"grep 'šaman|šmn' in NYB_vol2_glossary.txt\", \"stance\": \"silent\", \"note\": \"Nyberg's glossary (Book-Pahlavi texts) has only dušman, hešm-manīhā — no šaman.\"}\n ]\n})\n\ne1nodes.append({\n \"id\": 3, \"lang\": \"Persian\", \"words\": \"šaman «شَمَن»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"New Persian شَمَن šaman 'idol-worshipper; Buddhist or Brahmin monk' is the direct inheritance of Middle Persian šaman, with no phonetic change at all (MP šaman > NP šaman); Mo'in tags the word '[په.]' = Pahlavi. Borhān-e Qāṭeʿ defines it 'بر وزن چمن، بت‌پرست را گویند' and gives the plural شمنان 'بت‌پرستان'. It is a stock word of classical poetry for the pagan/Buddhist worshipper, standing beside بت 'idol' and often paired with صنم — Rudaki 'این جهان چون بت است و ما شمنیم', Amir Moʿezzi 'به عاشقی چو من ایزد نیافرید شمن', and the Ferdowsi couplet Nourai quotes, 'agar tāj-e Irān sepārad be man / parastesh konam čon botān rā šaman' ('if he hands me the crown of Iran, I shall worship [him] as the šaman worships idols'). English shaman is a separate, much later arrival (German Schamane < Russian šamán < Evenki samān), whose link to śramaṇa is debated — Persian شمن is not its source.\",\n \"derivation_fa\": \"«شَمَن» در فارسی نو «بت‌پرست؛ راهب بودایی یا برهمایی» بازماندهٔ مستقیم فارسی میانهٔ šaman است، بی هیچ دگرگونی آوایی؛ معین آن را «[په.]» یعنی پهلوی برچسب می‌زند. برهان قاطع می‌آورد: «شمن، بر وزن چمن، بت‌پرست را گویند» و جمع آن «شمنان … که بت‌پرستان باشد». این واژه در شعر کلاسیک در کنار «بت» و «صنم» می‌نشیند: رودکی «این جهان چون بت است و ما شمنیم»، امیرمعزی «به عاشقی چو من ایزد نیافرید شمن»، و همان بیت فردوسی که نورایی آورده: «اگر تاج ایران سپارد به من / پرستش کنم چون بتان را شمن». واژهٔ انگلیسی shaman راهی جداگانه و بسیار دیرتر پیموده (آلمانی Schamane از روسی šamán از اونکی samān) و پیوندش با śramaṇa محل بحث است؛ «شمن» فارسی سرچشمهٔ آن نیست. ادعای نورایی درست است.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/%D8%B4%D9%85%D9%86\", \"https://abadis.ir/fatofa/%D8%B4%D9%85%D9%86/\"],\n \"ref_check\": [\n   {\"ref\": \"BQT:1296\", \"status\": \"supports\", \"note\": \"Borhān-e Qāṭeʿ, printed p. 1296 (confirmed from the running head '-۱۲۹۶-' and the catchword «شمن» on pdftoppm page 83 of BQT_v3_picofile.pdf; ref_page.py's default mapping lands one leaf off because of the mis-ordered scan around the 1291-1294 gap): 'شمن * بر وزن چمن، بت پرست را گویند' and 'شمنان ... جمع شمن است که بت‌پرستان باشد', with Mo'in's footnote deriving it from Manichaean MP/Parthian shmn < Skt. śramaṇa.\"},\n   {\"ref\": \"ETM:37\", \"status\": \"not_checked\", \"note\": \"Abolghasemi, Rishe-shenāsi (Etimoloji), Qoqnus 1374 — refs_online.json: no digital copy on any permitted platform (catalogue/purchase entries only).\"},\n   {\"ref\": \"TZF:77\", \"status\": \"not_checked\", \"note\": \"Abolghasemi, Tārikh-e Mokhtaṣar-e Zabān-e Fārsi — no downloadable copy.\"}\n ],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"MON_part1.txt line 86768 and abadis.ir 'فرهنگ معین' s.v. شمن\", \"stance\": \"supports\", \"note\": \"'شمن (شَ مَ) [ په. ] (اِ.) ۱- راهب بودایی یا برهمایی. ۲- بت‌پرست.' — Mo'in's own origin tag [په.] = Pahlavi is precisely Nourai's arrow.\"},\n   {\"src\": \"BQT\", \"where\": \"vol. 3 p. 1296\", \"stance\": \"supports\", \"note\": \"'بت پرست را گویند' — the gloss Nourai prints.\"},\n   {\"src\": \"ARY\", \"where\": \"Dehkhoda / Amid via abadis\", \"stance\": \"supports\", \"note\": \"Amid: '۱. مرتاض در میان بوداییان، راهب بودایی. ۲. [قدیمی] بت‌پرست', with the Rudaki and Amir Moʿezzi shawāhed.\"}\n ]\n})\n\nentry1 = {\n \"entry\": 1,\n \"root\": \"Klem\",\n \"verdict\": \"plausible\",\n \"modern_form\": \"PIE *klem- / *klēm- 'weak, ailing, feeble' (Pokorny, IEW 602-603)\",\n \"note\": \"The root exists and the page is right (Pokorny klem-, klēm-, klēmi-, IEW 602-603, so POK:602 is exact), but Nourai's gloss 'tired, loose, dull' is a paraphrase: Pokorny's meaning is 'weak, ailing, feeble' (schwach, kränklich, matt), and 'loose' has no basis. More importantly the root is one of Pokorny's shakier entries — he prints the caveat '(barely better as klem-: klām- must be assumed)' and, on the very Sanskrit material this chart rests on, 'the ambiguity of the liquid complicates the judgment' (śram- beside klam-). Its firm members are Skt. klāmyati 'grows tired', Gk. κλαμαρόν · ἀσθενῆ (Hesychius) and OIr. clam 'leper'; the Indo-Iranian śram- family is attached with reservation, and Mayrhofer's EWAia leaves śram- without a secure PIE root. The Iranian half of the chart (Pahlavi and Persian šaman) is, by contrast, very well documented — but as a Buddhist loanword from Middle Indic, not as an inherited descent from PIE, and Mo'in's footnote in Borhān-e Qāṭeʿ says so explicitly, citing Henning.\",\n \"note_fa\": \"ریشه وجود دارد و شمارهٔ صفحه درست است (پوکورنی klem-, klēm-, klēmi-، صفحهٔ ۶۰۲–۶۰۳؛ پس POK:602 دقیق است)، اما معنایی که نورایی داده («خسته، سست، کودن») بازگویی آزاد است: معنای پوکورنی «ناتوان، بیمارگون، سست» است و «loose/سست‌بودن» پایه‌ای ندارد. مهم‌تر آنکه این یکی از مدخل‌های لرزان پوکورنی است؛ خود او هشدار می‌دهد که «به‌سختی می‌توان klem- : klām- را بهتر فرض کرد» و دربارهٔ همین مادهٔ سنسکریتی که نمودار بر آن استوار است می‌نویسد «دوگانگی روان‌واک داوری را دشوار می‌کند» (śram- در برابر klam-). اعضای استوار این ریشه klāmyati سنسکریت، κλαμαρόν یونانی (هزیخیوس) و clam ایرلندی کهن «جذامی» است؛ خانوادهٔ هندوایرانی śram- با احتیاط بدان پیوسته شده و مایرهوفر در EWAia برای śram- ریشهٔ هندواروپاییِ مطمئنی نمی‌آورد. در مقابل، نیمهٔ ایرانی نمودار (شمن پهلوی و فارسی) بسیار خوب مستند است — اما همچون وام‌واژه‌ای بودایی از هندی میانه، نه بازماندهٔ ارثی هندواروپایی؛ و حاشیهٔ معین در برهان قاطع، به نقل از هنینگ، آشکارا همین را می‌گوید.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/%E0%A4%B6%E0%A5%8D%E0%A4%B0%E0%A4%AE\", \"https://en.wiktionary.org/wiki/shaman\"],\n \"ref_check\": [{\"ref\": \"POK:602\", \"status\": \"supports\", \"note\": \"POK_full.txt line 47419ff.: 'Root / lemma: klem-, klēm-, klēmi- | Meaning: weak, ailing, feeble | Note: (barely better as klem- : klām- must be assumed) | Material: Old Indic offers on the one hand klāmyati, klamati \\\"becomes tired, grows tired\\\", on the other hand śramyati ..., śramaṇa- \\\"castigating, mendicant\\\" is to East Asiatic languages as Schamane \\\"shaman, magician\\\" ... gr. κλαμαρόν· ἀσθενῆ Hes.; Old Irish clam \\\"leper\\\" ... References: WP. I 498. Page(s): 602-603'.\"}],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny I 498 (Pokorny's own reference for klem-)\", \"stance\": \"supports\", \"note\": \"IEW's 'References: WP. I 498' — the root is Walde-Pokorny's, taken over unchanged into IEW.\"},\n   {\"src\": \"AHD\", \"where\": \"grep 'klem-' in AHD_watkins1985.txt\", \"stance\": \"silent\", \"note\": \"Watkins does not admit a root klem- at all (no English reflex), so the AHD appendix is silent on this entry — a sign of how marginal the root is.\"},\n   {\"src\": \"BQT\", \"where\": \"Borhān-e Qāṭeʿ vol. 3 p. 1296, Mo'in's footnote\", \"stance\": \"partial\", \"note\": \"Mo'in traces شمن to Sanskrit śramaṇa via Manichaean Middle Persian but says nothing about a Proto-Indo-European root; the Iranian chain is a loan chain, not a genetic one.\"}\n ],\n \"nodes\": e1nodes\n}\n\nout = {\n \"pdf_page\": 269,\n \"book_page\": 239,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-06\",\n \"entries\": [entry0, entry1]\n}\n\nwith io.open(\"/home/sfmqrb/git/rishe/data/verification/page-269.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(out, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"written\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build269.py",
 "description": "Write page-269 verification JSON"
}
```


### [2026-09-06T21:11:49.271Z] TOOL RESULT

```
written
```


## [2026-09-06T21:11:53.673Z] TOOL CALL #69: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-269.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 269",
 "description": "Validate JSON and run verify_check"
}
```


### [2026-09-06T21:11:55.751Z] TOOL RESULT

```
JSON OK
nodes verified: 18/18
node verdicts: {'confirmed': 11, 'unverified': 1, 'plausible': 4, 'transcription_suspect': 2}
root verdicts: {'confirmed': 1, 'plausible': 1}
ref checks: {'supports': 14, 'not_checked': 4, 'contradicts': 1, 'partial': 1}
books consulted: {'supports': 25, 'silent': 10, 'partial': 8, 'contradicts': 2} | by book: {'KLN': 11, 'BQT': 4, 'SKT': 4, 'POK': 4, 'BOOK': 3, 'MON': 3, 'CHEUNG': 2, 'WLD': 2, 'PHD': 2, 'ARY': 2, 'IEC': 2, 'BRT': 1, 'AHD': 1, 'FVQ': 1, 'LKT': 1, 'AFM': 1, 'NYB': 1}
```


## [2026-09-06T21:12:12.822Z] AGENT

Done — `data/verification/page-269.json` written, `verify_check.py 269` shows **18/18 nodes, 0 PROBLEM lines**.

**Page 269 (book p. 239), 2 entries, 18 nodes**
- Node verdicts: 11 confirmed · 4 plausible · 2 transcription_suspect · 1 unverified
- Root verdicts: Klei confirmed · Klem plausible
- Ref checks: 14 supports · 1 partial · 1 contradicts · 4 not_checked (TZF, ETM — no digital copy anywhere)

**transcription_suspect (both `error_in: "book"` — extraction is faithful)**
- Klei #12 Latin: book prints **`clîmâre`**; the correct form is Latin **clīnāre** (AHD, the very reference Nourai cites, prints `-clīnāre`; so do Klein and Pokorny). Nourai's own misprint, m for n, likely contaminated by `clîma` two boxes above.
- Klei #9 French: book prints **`clinic`** in a box headed "French"; French is **clinique**. Verified on a 300-dpi crop of the printed page.

**Other findings**
- Klei #2 is a genuinely **empty box** on the printed page (arrow off the Avestan box into a blank rectangle) — verdict `unverified`, not an extraction bug.
- Klei #7 climate, #11 climax, #13 client: plausible only because the chart skips the French/Latin intermediaries all standard sources record (OF *climat*, LL *climax*, AF *clyent*).
- Klei #14 Germanic `hlaider` is not a real reconstruction; standard is PGmc `*hlaidr-`/`*hlaidrī` (AHD, Klein) — marked plausible.
- Klem #1 Sanskrit: gloss inverted — `śramaṇá-` is "one who exerts himself, ascetic", not "a dull person"; and `saman` is Pali/Prakrit *samaṇa*, not Sanskrit. Root Klem is one of Pokorny's shakier entries (his own caveat about the r/l ambiguity); Watkins/AHD does not admit it at all.
- Best positive find: **BQT:1296 checked exactly right** — the running head of the vol.-3 scan (pdftoppm page 83) reads `-۱۲۹۶-` with catchword «شمن», and Mo'in's footnote there gives Manichaean MP/Parthian `shmn` < Skt `śramaṇa` citing Henning, BSOS IX/1 p. 88. Mo'in also tags شمن `[په.]` and اقلیم `[معر - یو.]` and کلینیک `[فر.]`, confirming three arrows outright.

**No extraction errors to fix** — the JSON matches the printed page everywhere I checked.

Artefacts saved: page image `data/verification/sources/refs/ocr/BOOK/269.png`, `data/verification/sources/refs/ocr/BQT/1296.vision.txt`, and 15 archived web sources via `fetch_source.py`.
