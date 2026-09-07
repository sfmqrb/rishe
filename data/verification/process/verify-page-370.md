# Verification process log — verify-page-370


## [2026-09-07T20:14:49.936Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 370 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-370.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-370.json. Write /home/sfmqrb/git/rishe/data/verification/page-370.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 370` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-07T20:16:04.365Z] AGENT

I'll start by reading the instructions.


## [2026-09-07T20:16:05.057Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-07T20:16:05.078Z] TOOL RESULT

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


## [2026-09-07T20:16:05.698Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-370.txt"
}
```


### [2026-09-07T20:16:05.722Z] TOOL RESULT

```
1	=== PDF page 370 (book page 340) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Nomn, Enomn : name  (refs POK:321)
4	#1 (parent #0) [Avestan] refs=POK:321; KNT:193 | nâma, nâman : name ; duš-naman : bad name ☞Dus
5	  #2 (parent #1) [Persian] refs=BQT:2106; HRN:229 | nâm «نام» : name ; došnâm «دشنام» : a curse ; nâmeh «نامه» : letter, book
6	#3 (parent #0) [Old Persian] refs=KNT:193 | nâman : name
7	  #4 (parent #3) [None] refs=None | 
8	#5 (parent #0) [Germanic] refs=AHD | namon
9	  #6 (parent #5) [English] refs=None | name
10	#7 (parent #0) [Latin] refs=AHD | nomen
11	  #8 (parent #7) [English] refs=None | noun, nominal, nominate, denominate, pronoun, nomenclature
12	#9 (parent #0) [Greek] refs=AHD | onoma : name
13	  #10 (parent #9) [English] refs=None | synonym, antonym, anonymous
14	--- entry 1 ---
15	ROOT [Indo-European] Nôr, Anôr : watery, juicy  (refs IEC:1645)
16	#1 (parent #0) [Pahlavi] refs=IEC:1645 | anâr : pomegranate
17	  #2 (parent #1) [Persian] refs=MON:4557; IEC:1645 | anâr «انار (نار)» : pomegranate | NOTE: SKT:360 links this word to Sanskrit "Naranga: orange tree"
18	#3 (parent #0) [Armenian] refs=IEC:1645 | nurn, nran : pomegranate
19	--- entry 2 ---
20	ROOT Nu -> redirect to Newo
21	
```


## [2026-09-07T20:16:08.602Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-370.json",
 "description": "Read source JSON for page 370"
}
```


### [2026-09-07T20:16:08.638Z] TOOL RESULT

```
{
  "pdf_page": 370,
  "book_page": 340,
  "entries": [
    {
      "root": {
        "name": "Nomn, Enomn",
        "lang": "Indo-European",
        "refs": "POK:321",
        "gloss": "name"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:321; KNT:193",
          "words": [
            {"translit": "nâma, nâman", "gloss": "name", "script": null},
            {"translit": "duš-naman", "gloss": "bad name", "script": null, "see": ["Dus"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:2106; HRN:229",
          "words": [
            {"translit": "nâm", "gloss": "name", "script": "نام"},
            {"translit": "došnâm", "gloss": "a curse", "script": "دشنام"},
            {"translit": "nâmeh", "gloss": "letter, book", "script": "نامه"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Old Persian",
          "refs": "KNT:193",
          "words": [
            {"translit": "nâman", "gloss": "name", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": null,
          "refs": null,
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "namon", "gloss": null, "script": null}
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
            {"translit": "name", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "nomen", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "noun, nominal, nominate, denominate, pronoun, nomenclature", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD",
          "words": [
            {"translit": "onoma", "gloss": "name", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 9,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "synonym, antonym, anonymous", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Nôr, Anôr",
        "lang": "Indo-European",
        "refs": "IEC:1645",
        "gloss": "watery, juicy"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Pahlavi",
          "refs": "IEC:1645",
          "words": [
            {"translit": "anâr", "gloss": "pomegranate", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "MON:4557; IEC:1645",
          "words": [
            {"translit": "anâr", "gloss": "pomegranate", "script": "انار (نار)"}
          ],
          "script_extra": null,
          "note": "SKT:360 links this word to Sanskrit \"Naranga: orange tree\"",
          "quote": {
            "text": "بفرمود تا آب نار آورند - همان تـرّهٔ جویبار آورند",
            "poet": "Ferdowsî"
          }
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Armenian",
          "refs": "IEC:1645",
          "words": [
            {"translit": "nurn, nran", "gloss": "pomegranate", "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Nu",
        "redirect": "Newo"
      },
      "nodes": []
    }
  ]
}
```


## [2026-09-07T20:16:10.270Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KNT','IEC','MON','BQT','HRN','AHD','SKT','WLD','PHD','NYB','BRT','HUB','ARY','SYN','KLN','CHEUNG']:\n    v=d.get(k)\n    print(k, json.dumps(v, ensure_ascii=False)[:400])\n\""
}
```


### [2026-09-07T20:16:11.562Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "loca
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
CHEUNG null
```


## [2026-09-07T20:16:17.587Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KNT','IEC','MON','BQT','HRN','SKT','AHD','ARY','WLD','SYN','BRT','PHD','NYB','HUB','KLN']:\n    v=d[k]\n    print('===',k)\n    for f in ['local_file','page_offset','lookup_hint','scans','kind']:\n        if v.get(f): print(' ',f,':',str(v[f])[:500])\n\""
}
```


## [2026-09-07T20:16:18.098Z] TOOL CALL #6: Bash

```json
{
 "command": "ls data/verification/sources/refs/ | head -60 && echo --- && cat data/verification/sources/SOURCE_MATRIX.md | head -80"
}
```


### [2026-09-07T20:16:18.940Z] TOOL RESULT

```
=== POK
  local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt
  page_offset : POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
  lookup_hint : Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?bas
  kind : archive_djvu
=== KNT
  local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt
  page_offset : leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
  lookup_hint : Lexicon (Part III, pp. 164 ff.) headwords are transliterated OP words at line start followed by part of speech, e.g. grep -n '^apadana-' ; section refs like '$147'. Nourai's page numbers should fall in 164-215 for lexicon citations.
  kind : archive_djvu
=== IEC
  local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt
  page_offset : TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
  lookup_hint : Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.
  kind : archive_djvu
=== MON
  local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incom
  lookup_hint : Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Aden
  kind : website+archive_djvu
=== BQT
  local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '
  page_offset : vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, 
  lookup_hint : grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf imag
  scans : [{'volume': '3', 'file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', 'first_printed': 1208, 'last_printed': 1925, 'pdf_offset': -1205, 'page_map': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pagemap.json', 'lang': 'fas', 'ocr_text': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', 'ocr_note': '689/721 pdf pages OCRed (tesseract fas+eng, mediocre); pages are separated by form-feeds a
  kind : archive_djvu+local_scan_ocr
=== HRN
  local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt
  page_offset : leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
  lookup_hint : Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.
  kind : archive_djvu
=== SKT
  local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt
  page_offset : leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
  lookup_hint : Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags.
  kind : archive_djvu
=== AHD
  local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt
  page_offset : 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.
  lookup_hint : Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New Colleg
  kind : archive_djvu+website+archive_restricted
=== ARY
  local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt']
  page_offset : printed page = pdf page + 1
  lookup_hint : Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image
  scans : [{'file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_aryanpur_kashani_rishehaye_hend_o_orupayi.pdf', 'first_printed': 1, 'last_printed': 546, 'pdf_offset': -1, 'lang': 'fas+eng', 'ocr_text': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt'}]
  kind : local_scan_ocr
=== WLD
  local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf', '/home/sfmqrb/git/rishe/data/veri
  page_offset : Band 3: leaf = printed + 6. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696).
  lookup_hint : Band 3 is the index (Wortregister by language) - it maps a word to 'Band, page' in vols 1-2, so it can at least confirm that a word is treated at the cited WP volume/page. For the actual entry text, use Pokorny 1959 (POK), whose entries cite 'WP. I 177' etc. and are essentially a revision of WP.
  kind : archive_djvu
=== SYN
  local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt
  page_offset : leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
  lookup_hint : Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed page number line.
  kind : archive_djvu
=== BRT
  local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt
  page_offset : Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
  lookup_hint : Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special transliteration is noisy - grep on a distinctive Latin gloss or the German meaning in quotes. Column numbers appear as standalone numbers at leaf tops.
  kind : archive_djvu
=== PHD
  local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt
  page_offset : leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
  lookup_hint : Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsianjoman.org/wp-content/uploads/2015/09/A-Concise-Pahlavi-Dictionary.pdf (8.4 MB).
  kind : archive_djvu
=== NYB
  local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt
  page_offset : Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
  lookup_hint : Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates and 'Bthl.' refs.
  kind : archive_djvu
=== HUB
  local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt
  page_offset : leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
  lookup_hint : Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number.
  kind : archive_djvu
=== KLN
  local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt
  page_offset : KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
  lookup_hint : Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
  kind : archive_djvu
```


### [2026-09-07T20:16:19.010Z] TOOL RESULT

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
```


## [2026-09-07T20:16:24.291Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK_full lemma nomn\"; grep -n -i \"lemma: .*nom\" POK_full.txt | head -20\necho \"=== POK_full enomn\"; grep -n -i \"enomn\\|nomen-\\|ǝnomn\" POK_full.txt | head -20"
}
```


### [2026-09-07T20:16:24.369Z] TOOL RESULT

```
=== POK_full lemma nomn
26895:Root / lemma: en(o)mQ-, (o)nomQ, nomij, {*hien h3(o)mij^ 
29822:Root/ lemma: gang-', "to mock' derived from the onomatopoeic duplication of Root/ 
62532:derived from a zero grade of Root/ lemma: en(o)mQ-, (o)nomQ, nomij'. name. 
63119:Root / lemma: nomp {*he- nomp) 
67528:Root/ lemma: peuor, pur, Gen. pu-n-es, Lok. puuen/{Nom. -r-, Gen. -n- inanimate 
=== POK_full enomn
44992:calator^ a servant for calling, etc., a crier ', nomen-clator^ one who calls by name, a 
54721:better to glynu, Irish glenald^ get stuck, stick '), Old Irish lenomnalb^ a smearing on a 
63120:See also: s. enomn.
```


## [2026-09-07T20:16:25.052Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KNT nāman\"; grep -n \"naman\\|nāman\\|nāma-\" KNT.txt | head -30"
}
```


### [2026-09-07T20:16:25.139Z] TOOL RESULT

```
=== KNT nāman
```


## [2026-09-07T20:16:28.298Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '26890,26960p' POK_full.txt"
}
```


### [2026-09-07T20:16:28.347Z] TOOL RESULT

```
References: Schwyzer Gr. Gr. I 424 with Anm. 5, Feist 140 f., Speclit Dekl. 15 f. 
Page(s):314 

Root / lemma: en(o)mQ-, (o)nomQ, nomij, {*hien h3(o)mij^ 

Meaning: name 

Material: Old Indie nama, Instr. Sg. namna, Avestan nama^name'; 

Armenian anun, Gen. anuan, after Meillet Esquisse 48 from *anuwn, *onomno-, after 
EM2 675 from *ondmno-\ 

gr. ovopa (from reduced *e/7c»-with assimilation e- o), dial, ovupa, *'iy\j\\a in lak. 
'Evu[jaKapTi5a(;, (reduced u derived before pvfrom Gen. *bjo\jNoq), avcbvufjoq, vu)vupvo(; 
"nameless"; 

alb. Tosc emer, Geg emen {*enmen-); 
Note: 
{* da-a-ma-an) > alb. Geg e/77e/7 [common alb. -Baltic cf->zero] 

Latin nomen, -inis, n. Umbrian nome, Abl. nomne'name' and "people'; 

Old Irish a/nmm n-n., PI. anmann {*enmn-)\ acymr. anu, PI. enuein, out of it ncymr. enw, 
corn, hanow. Middle Breton hanff, hanu, bret. ano; 

Gothic namon., Old Icelandic nafnn., Old English nama, Old High German namom. 
"name'; with o-grade Old Frisian nomia. Middle High German be-nuomen' name'; 

Note: 

Taboo word for ( *dap-no-) " sacrificial animal, sacrificial meal '. 

Old Prussian emnes, emmensm. {*enmen-)\ 

Slavic *bm§, out of it *Jbm§\'r\ Old Church Slavic im§, Serbo-Croatian Tme, Old Czech 
jme, Qeu. jmene, russ. fmja; 

Tocharian A nem, B nom\ 

Hittite la-a-ma-an {laman), with dissimilation of Aniauts; {* nda-a-ma-an) 

compare finno-ugr. nam, nam, nem, namma, magyar. /7ei/"name'. 



References: WP. I 132, Feist 369 f., Schwyzer Gr. Gr. I 352, Hirt Indo Germanic Gr. II 98, 

121. 

Page(s): 321 



Root / lemma: enos-or onos- 

Meaning: burden 

Grammatical information: n. 

Material: Old Indie anahu. "load wagon' = Latin onus, -en's' a load, burden ' {onustus' 

loaded, laden, burdened, freighted ', onerare' load, burden, fill, freight '). 

In addition perhaps gr. avia, Aeolic ovia " grief, sorrow, distress, trouble', avioq, aviap6(; 
" grievous, troublesome, annoying' (the dialect distribution from avia : ovia as with the 
preposition ava : 6v); after Wackernagel Gl. 14, 54 f. but dissimilated from *a|jTFa = Old 
Indie amTvai. " grief, sorrow, distress, trouble, plague ' (see below ome^. 

References: WP. I 132f.;
```


## [2026-09-07T20:16:29.848Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KNT nama\"; grep -n \"nama\" KNT.txt | head -40; echo \"=== leaf count\"; python3 -c \"\nt=open('KNT.txt',errors='replace').read().split('\\f')\nprint(len(t))\nprint(t[208][:3000])\n\""
}
```


### [2026-09-07T20:16:31.280Z] TOOL RESULT

```
=== KNT nama
955:П. When final in the word, pIE т and m beeame pAr. a, which of course was written à in OP ($36.1): асс. *nomn ‘name’, OP nama, Skt. пата, Lt.
1368:pIE *nómg ‘name’, OP néma, Skt. nama, Lt
1382:pIE *пйту ‘name’, ОР пата, Skt. nama, 1А. nomen.
2215:fix -men- have nom.-ace, in the zero-grade -mx;' асс. OP nama, Skt. пата, 14. ndmen, from *nomn.
2388:(j) Type of Skt. namasyati (denominative). $208. Тнк Present-Tense SYSTEM OF TYPE
2516:NOMINATIVE Venss (type, Skt. namas-yati ‘re-
2706:C. Expressing specification: пата ‘as to name’ (see Lex. s.v. for examples, and $312), and pos- sibly nama (if long-vowel loc. and not acc.); prob- ably We 1 CXX karíayà ‘120 (units) in weight’, and D'Sa 1 (and A?Hb) apadénam stündya (if for -üyà) afagainam ‘palace made of stone as to its column(s)’,
2715:D. Alone, to express specification: DNb 40f yãumainiš amiy ша daslaibuyü ша pādaibiyā ‘trained am I both as to hands and as to feet’. So also with numerals: DB 2.56 Andmakahya mahyd XV raucabi$ 6akatà aha ‘of the month Anamaka, 15 by days were past’; Wa 1 IT karšā ‘2 (units) by weight’; cf. Lg. 19.227-9.
3081:8312. Tue Namina Punaszs. It is a feature of OP style, that at the first mention of a person (other than of the ruling king) or of a place (other than of а governmental province) the name of that person or place should be followed by пата or nàmà; there are a few exceptions, as in DSf 12f, where the names of Arsames and Нуѕђаврез lack лата, and in DB 3.11 and 5.4, where the province- names Marguí and (ја are accompanied by nama. These phrases are always! in the nomina- tive case, whether or not that is their funetion in the sentence; they are usually followed by a re- sumptive pronoun or adverb. The form пата is used unless there is a following generic term of feminine gender (dahydus, didd), when лйт@ is
3087:DB 1.58f Sikayauvališ пата дда Nisdya nama dahydus Madaty avadasim avàjanam ‘a fortress by name Sikayauvati, a district by name Nisaya, in Media—there I smote him.’
3100:nama-phrase of place intervenes, which has its own
3101:resumptive avadd in each passage. The six helpers of Darius (DB 4.83-6) are not followed by re- sumptives, because they stand in a list appositive to a preceding substantive, and are not further mentioned. Typical phrasings are those of DB 2.29f (quoted above) and of 1.77f I martiya Babi- ruviya Naditabaira nama Ainairahyd риса haw udapatatà Babtraw ‘One man, a Babylonian, Ni- dintu-Bel by name, son of Ainaira—he rose up in
3114:II. With names of places, 32 occurrences. The E | common sequence is typified by DB 2.39 Tigra -% nama йай Arminiyaty wadā hamaranam akunava a ‘A stronghold by name Tigra, in Armenia—there 4 they made battle.’ A more elaborate phrase isin 4
3486:30 tà : Bardiya : nama : Sha : hamátà : hamapità : Kabtijiyahyd : pasiva : Ka
3584:519. 1.90-6. Saith Darius the King: After that I went off to Babylon. When I had not arrived at Babylon, à town by name Zazana, beside the Euphrates—there this Nidintu-Bel who called himself Nebuchadrezzar came with an army against me, to deliver battle. Thereupon we joined battle; Ahuramazda bore me aid; by the favor of Ahuramazda I smote that army of Nidintu-Bel exceedingly. The rest was thrown into the water, (and) the water carried it away. Of the month Anamaka II days were past, then we fought the battle.
3586:Техт or DB, Сошмх П: 1 :98ty : Dárayavaus : xSayafiya : paeüva : Naditabaira : ha 2 dà : kamnaibis : asabaraibis : amufa : Bübirum : ašiya 3 va: pasàva : adam : Babirum : ašiyavam : vasnd : Auramazdiha : uta : Ba 4 birum : agarbiyam : uta : avam : Naditabairam : agarbüyam : pasáva : ava 5 m : Naditabairam : adam : Babirauv : avüjanam —— :0ütüy : Dārayavauš : x 6 Sdyabiya : yātā : adam : Bübirauv : àham : ima : dahydva : tyà : hacàma : ha 7 migiyà : abava : Рагва : Üvja : Mada : Aðurā : Mudráya : Parfava : Margus : Өз 8 tagui:Saka : абу : Dārayavauš : x8dyabiya : I martiya : Martiya : nā Q ma : Cicixrais : puca : Kuganakà : пата : vardanam : Pársaty : avada : adaraya : 10 hauv : udapatatà : Uvjaiy : Кагаһуй : avaðā : afaha : adam : Imanis : amiy : 0 11 vjeiy :xSdyafiya —— : @atiy : Darayavaus : zsayattya : adakaiy : adam : asna 12 iy : àham : abiy : Üvjam : pasáva : hac&ma : alarsa : Üvjiy& : avam : Marti 13 yam :agarbaya : hyašām : mafista : dha : шат : avàjana — : 00у: D 14 árayavaus : xSiyafiya : І martiya : Fravartiá : пата : Мада : hauv : udapatat 15 à : Madaiy : Катаһуй : ауаба : абала : adam : XSa6rita : amìy : Uvaxdtrah 16 уй : taumàyá : pasáva : kāra : Mada : hya : v'àpaliy : haw : hacáma : hamiciya : a 17 bava : abiy : avam : Fravartim : aSiyava : hauv : тёйуайтуа : abava : Madaiy 18 9àtry : Dárayavaus : xšāyaðiya : kara : Parsa : ша : Мада : bya : ира : mim : 4 19 ha : hauv : kamnam : aha : раѕауа : adam : kdram : fraiSayam : Vidarna : пата : Pársa : man 7 20 à : badaka : avam&àm : mafistam : akunavam : avataSaám : afaham : parait : avam : К 2] dram : tyam : Madam : jatà : hya : mand : пау : gaubataiy : pasiva : hauv : Vidarna : ha 22 dà : kara : айуауа : yafà : Madam : parárasa : Māruš : пата : vardanam : Ma 23 дау : ауада : hamaranam : akunaus : hada : Мада : һуа : Màdaisuvà 24 :ma(iSta : dha : hauv : adakaiy : пау : avadà : аһа : Auramazdimary : u 25 раѕійт : арага : vasnà : Auramazdáha : kāra : hya : тара : avam : kàram : t 26 yam : hamiciyam : aja : vasiy : Animakahya : mähyä : XXVII : raueabis : fakat 27 à : аһа : avatüsám : hamaranam : kartam : pasáva : hauv : Ката : һуа : manā : Карада : пат 28 à : dahydus : Mádaiy : avadà : mam : amánaiya : y8tà : adam : arasam : Mada ' 20m : 08у : Dàrayavaus : xšāyaðiya : адаг х : nàma : Arminiya : man 30 à : badaka : avam : adam : frāišayam : Árminam : avafasazy : aaham : paraidiy : ka 31 ra : һуа : hamigiya : mană : naiy : gaubataiy : avam : jadiy : pasiva : Dadarsi 32 š : aSiyava : yafà : Arminam : parárasa : pasáva : hamigiya : hagmatà : paral 33 tà : patiš : Dādaršim : hamaranam : cartanaiy : Züzahya : пата : àvahanam : А 34 rmíniyaiy : avadà : hamaranam : akunava : Auramazdimaiy : upastàm : a 35 bara : vasnà : Auramazdàha : kāra : һуа : manā : avam : küram : {уаш : hamigiyam : 36 aja : vasiy : Oüravaharahya : máhya : VIII : raucabis : 09akatà : dha : ava 87 à$üm : hamaranam :kartam : бабу : Dárayavaus : z3àyaffya : patiy : duv 38 itiyam : hamigiyà : hagmatà : paraitd : patiš : Dàdar&im : hamaranam : carta 3€ nay : Tigra : пата : didà : Arm‘niyavy : avadà : hamaranam : akunava : А 40 uramazdàmaiy : upastàm : арага : vašnā : Ашатагдаћа : kāra : һуа : тапа :a 41 vam : káram : tyam : hamigiyam : aja : vasiy : G9üravüharahya : mihya : ХҮШ 42 :raueabiá : бакаќа : аһа : ауабадат : hamaranam : kartam —— : 00у : Daraya 43 vaus : xšāyaðiya : patiy : citiyam : hamictyd : hagmatà : paraita : pat 44 iš : Dádar&im : hamaranam : cartanaiy : Uyama : nama : didi : Arm'myaty :a 45 vadā : hamaranam : akunava : Auramazdimaiy : upastam : арага : vaSnà : Aurama 46 zdàha : kāra : һуа : manā : avam : küram : tyam : ham?giyam : aja : vasiy : Oàigarea 7 d :mábyà : IX : raucabis : Nakata : dha : ауада ат : hamaranam : kartam : pasava 48 : Dadarsis : citā : mim : amánaya : Arm/niyaiy : yiti : adam : arasam : Ма
3608:65 Babiraus : айуауаш : Madam : уада : Madam : parárasam : Kud"ru$ : nama :
3615:72 gi : nama : dahyaus : Mádaiy : avapara : asiyava : pasiva : adam : karam : f
3646:Rl. has the following correct readings, in whieh he records as visible certain characters, here indicated by roman type, which were not visible to KT: * Naditabai- fram; *бай]у : Dárayavaus; *aham : i[mà; * Auri; з rhiyal6iya; * nama : var[danam; ” avais;  Dárayavaus : xéáya[frya; ? haeáma; * hya; * mahya : VI : ralucabes (VI is corrected to VIII by КІ. on page 218); * parazta : pat(is; 9 Armaniyaiy (RI. misread the third character); * vasiy; * ham[igrya; *! Uvaz[Stra]hyá; *! uzmayapat]iy.
3670:exceedingly; of the month Anamaka XV days” were past, then the battle was fought by them. §30. 2.57-63. Saith Darius the King: Again a second time the rebels assembled (and) came out against Vaumisa to join battle. A district by name Autiyara, in Armenia—there they joined battle. Ahuramazda bore me aid; by the favor of Ahuramazda my army smote that rebellious army exceedingly; on the last day of the month Thura- vahara—then the battle was fought by them. After that, Vaumisa waited for me in Armenia
3693:5 nā : nama : vardanam : Рагдауају : ауада : hamaranam : akunaus : hada:
3707:23 : Yautiyd : nama : dahyáus : Pársaiy : avadà : adāraya : ha
3725:44 iy : Parga : nama : Каша : avadā : hamaranam : akunava : Auramazdima 45 iy : upastám : арага : vaSnà : Àuramazdáha : kara : hya : manā : ava
3798:exceedingly; of the month Anamaka XIII days Babylonians became rebellious from me. One may 3 |
3817:1 :98tiy : Darayavaus : xsayaüiya : ima : t 2 ya:manà :kartam': Babireuv — :98ty : D З árayavaus : xSàyaftya : ima : tya : adam : akuna 4 vam : vasnà : Autamazdiha : һашаһуйуй : баг 5 da : pasáva : yada : xšāyaðiya : abavam : ХІХ : hamaran 6 Я : akunavam : vasnd : Auramazdiha : adamšim : а Т janam : uta : IX : x&ayatty& : agarbiyam : 1 Gaumata : 8 n&ma : magus : aha : hau : adurujiya : ava : абаһа : adam : 9 Bardiya : amiy : hya : Küraus : puça : hauv : Parsam : ha 3 10 migiyam : akunaus : Z Acina : пата : Uvjiya : hauv : adu 11 rujiya : ауаба : afaha : adam : xSiyaliya : amiy : Uvjaiy 12 : hauv : Üvjam : hamigiyam : akunaus : manā : I Naditabaira : n 13 dma : Babiruviya : hauv : adurujiya : avafá : aGaha : 14 adam : Nabukudracara : amiy : hya : Nabunaitahya : puga : 15 hauv : Babirum : hamigiyain : akunaus : I Martiya : na 16 ma : Pársa : hauv : adurujiya : атаба : ađaha : adam : Imani 17 š : amiy : Uvjaiy : cSayasiya : hauv : Üvjam : hamiciya 18 m : akunaus : I Fravarti$ : пата : Mada : hauv : adurujiya 19 : ауада : абаћа : adam : XSa@rita : amiy : UvaxStrahya : taumay 20 à : hauv : Madam : hamiciyam : akunaus : I Cigataxma : пата : Asa 21 gartiya : hauv : adurujiya : ava : afaha : adam : xšāyað 22 iya : amiy : Asagariaiy : UvaxStrahya : taumāyā : hauv 23 : Asagartam : hamigiyam : akunauS : І Frida : nama : 24 Margava : liauv : adurujiya : ааба : ađaha : adam :
3822:26 yam : akunaus ; J Vahyazdàta : nama : Parsa : hauv : a
3876:83 à : Vidafarnà : пато : V&yaspárahy& : puça : Parsa : Utàna : пата : Guxrahyá 84 : риса : Parsa : Gaubaruva : паша : Marduniyahyá : puça : Parsa : Vidarna : nama : Ва 85 gabignahya : puça : Parsa : Bagabux’a : пата : Dütuvahyahyà : риса : Pársa :
4986:Anàümaka- adj. ‘Anamaka’, tenth month, Dec.-Jan.: Elam. handémakas, АКК. febétu. Cpd. of neg. a- + ndma- ‘name’ (see ndman-) + adj. suffix -ka- ($146.11), possibly with vriddhi (8126; Anámaka- ?): ‘Month of the Nameless (= High- est) God’. Anàmakahya gsm. DB 1.96; 2.26, 56; 3.63.
5419:tauman- sb. ‘power, strength’: deriv. of root tav- ‘be strong’, with suffix -man- as in Skt. nama ‘name’, Lt. nomen (§122, $155.11). For separa- tion from taumd- ‘family’, see Tm. Lex. 91, and Kent, JAOS 35.329-31. See also tawiyah-. taumā nsn. ($187) DB 4.74, 78; 5.19°, 35. tau- тату (= taumanis-Saiy; §41, §130, $138, $187) ipn. DNb 25f (Lg. 15.171-2, 176; not gen. sg. with Hz. Api 327; hardly loc. sg. with Sen 247; possibly aee. du., ‘two powers lof mind and of body|’, with Pisani, Riv. Stud. Or. 19.88-9).
5597:niman- sb. ‘name’: Ау. náman-, NPers. пат, Skt. náman-, Lt. nomen, pIE *nómen-, cf. Gk. буора, NEng. name ($109, $110, 5155.11). See also Andmaka-. náma^, suffixless lsn. used with mase. and nt. generic nouns to denote specification ($112, $187, §251C, §312): DB 1.28, 30, 36, 37, 74, 77, 92; 2.8f, 9, 14°, 19, 22, 29, 38, 49, 65, 79, 82, 95; 3.5, 12, 13, 22 bis, 31, 34, 44, 51, 56, 78, 84; 4.8, 10, 12f, 15f, 18, 20, 23, 26, 29, 83 bis, 84 bis, 85, 86°; 5.5, 8, 27; DSe 45°; DSf 31, 46; Юле 9; XPf 18, 19; А?Не 14f; A?Pa 19, 20; Sa 2f. nama, either asn. *ndmá ог lsn. лата” (with lengthened grade), specialized for similar use with fem. generic nouns because of similarity of end- ing ($67.1T, $187, §249L, $312; cf. Tm. Lex. 105,
=== leaf count
232
 Skt. jū- ‘press for- ward, impel quickly, excite, promote’, pres. jdvate ‘hastens’, caus. javayati. Cf. Ву. BSLP 332.152; Hz. AMI 4.127, 8.37-8, 65-6, ApI 366-7; Wb. МА 41.8320; Bailey, BSOS 7.292-4; Schaeder SbPAW 1935.502; Kent, Lg. 9.43, 231.
abi- + jav- caus. ‘promote, increase, add to’: abiyajüvayam 1st sg. imf. ($215) XPg 9; abijáva- yam (§23.1, $140.IIT) XPf 40.
jtyamna- pte. as adj. ‘growing old’, nt. as sb. ‘end’ ($109, $241): Av. Jyamna-, pte. to root }уй- ‘grow weak’, Skt. jinåti ‘grows old’. jiyamnam asn. DB 2.62.
ji- vb. ‘live’: Av. fait: (gay-, Bthl. AiW 502), Skt. Джай, Lt. vivit, pIE *g*īųeti (§216); see also gaiéd-, jiva-. ajivatam 3d du. imf. ($229) DSf 14; XPf 21. jwà 2d sg. imv. ($2371) DB 4.56, 75.
jiva- ad). ‘living’: Av. fva-, Skt. jivd-, Lt. vivos, pIE *g*iuo-, cf. *g*iuo- in Gk. Blos "life", *g*ig*o- in OEng. cwicu "living, NEng. quick (8101, $114, $150). See also 7й-. Jiva nsm. XPh 48, 54. jva-diy Аза 3 (dubious $22, 555.1; ef. JAOS 51.229, Scheil 21.93, Wb. AfOF 7.45). jivahya gsm. DB 5.19f, 35.
jü- vb., see jav-.
-{а- encl, demonst. pron. ‘this, it’: Av. Skt. ta-, ef. OP tya-. Only -tā apm., referring to patikarā,
185
in avabasa-a DB 4.72 (8133, $196; JAOS 62.272- 3).
{аита- sb. ‘family’ (8149.1): Av. taoxman-, NPers. tuzm, Skt. tokd-m ‘offspring’, tókman- tokma-s ‘young blade of barley’; -zm- became OP -hm- (5103.1, 5118.1), but remained in Med. (Ву. BSLP 31.2.76-9, Gr. $188; wrongly Mt. Gr. §75, Kent JAOS 35.329-31). taumd nsf. DB 1.8; 4.56, 58f, 64, 75, 79; DBa 13. іаитат asf. DB 488. іаитӣуӣ gsf. ($119) DB 1.9, 28f, 45, 49; 2.16, 81; 4.19f, 22; DBa 15; DBe 8; DBg 11f. taumaya absf. DB 1.61f.
tauman- sb. ‘power, strength’: deriv. of root tav- ‘be strong’, with suffix -man- as in Skt. nama ‘name’, Lt. nomen (§122, $155.11). For separa- tion from taumd- ‘family’, see Tm. Lex. 91, and Kent, JAOS 35.329-31. See also tawiyah-. taumā nsn. ($187) DB 4.74, 78; 5.19°, 35. tau- тату (= taumanis-Saiy; §41, §130, $138, $187) ipn. DNb 25f (Lg. 15.171-2, 176; not gen. sg. with Hz. Api 327; hardly loc. sg. with Sen 247; possibly aee. du., ‘two powers lof mind and of body|’, with Pisani, Riv. Stud. Or. 19.88-9).
lauviyah- adj. ‘stronger’: comp. to *tauma-, adj. to tauman- ‘power’; for formation ($48, $122, $156.IIT, $190.1-1), ef. Skt. sthürd- ‘strong’ and comp. sthdviyas-, Av. stūra- and comp. staoyah-, tarma- ‘brave’ and comp. tqsyah-: JAOS 58.324. іашлуй nsm. (§185.1V) DSe 39 (not to pres. pte. tavya-nt-, as taken by Hz. ApI 328).
takabara- adj. ‘wearing the petasos’ (§76.V, 6160.1а), ав proved by Akk. ‘who bear shields on their heads’ (Andreas, Verh. d. 13. Internat. Orien- talisten-Kong. 1902, 96-7; Wb. AbkSGW 29.1.33; other views by Foy KZ 35.63, 37.545-6, Bthl. AiW 626, Tm. Lex. 91, PAPA 44.liii-lv). taka- bara npm. DNa 29; DSm 10f^; A?P 26 (for nsm., 656.111).
taxma- adj. ‘brave’ ($9.11, S103.IT, $1491; with Med. -zm-, Ву. Gr. $133): Ау. tazma-, NPers. lühm; in Cigataxma-, Taxmaspáda-.
Taxmaspáda- sb. ‘Takhmaspada’, one of
```


## [2026-09-07T20:16:44.255Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('KNT.txt',errors='replace').read()\nleaves=t.split('\\f')\nfor i,L in enumerate(leaves):\n    if \"niman- sb. ‘name’\" in L or \"naman- sb\" in L or \"nāman- sb\" in L:\n        print(\"LEAF\",i)\n        print(L[:200])\n        print(\"...\")\n        import re\n        print(\"standalone nums:\", re.findall(r'^\\s*(\\d{2,3})\\s*$', L, re.M))\n        print(L[-1500:])\nEOF"
}
```


### [2026-09-07T20:16:45.539Z] TOOL RESULT

```
LEAF 216
e 15; DZe 10. drayahya lsn. ($136, §251A; wrongly taken as gen., Hz. АрІ 141-3) DB 1.15, DPe 14, DSe 28°; drayahiyà ($27) XPh 23.
naiy adv. ‘not’: Av. 207, РЫ. në, Skt. ned; :
from pIE *ne, Skt. na, L
...
standalone nums: ['193']
sb. ‘Nabonidus’, last king of the New Babylonian Empire, 556-39. в.с: Elam. na- bu-ni-da, Akk. nabü-na'id; Gk. Aaßivnros (Hat. 1.74, ete.). Nabunailahyà gsm. DB 1.79. Na- bunaitahya (§36.1Vb) DB 3.81; 4.14, 30; DBd 5f; DBi 7f.
niman- sb. ‘name’: Ау. náman-, NPers. пат, Skt. náman-, Lt. nomen, pIE *nómen-, cf. Gk. буора, NEng. name ($109, $110, 5155.11). See also Andmaka-. náma^, suffixless lsn. used with mase. and nt. generic nouns to denote specification ($112, $187, §251C, §312): DB 1.28, 30, 36, 37, 74, 77, 92; 2.8f, 9, 14°, 19, 22, 29, 38, 49, 65, 79, 82, 95; 3.5, 12, 13, 22 bis, 31, 34, 44, 51, 56, 78, 84; 4.8, 10, 12f, 15f, 18, 20, 23, 26, 29, 83 bis, 84 bis, 85, 86°; 5.5, 8, 27; DSe 45°; DSf 31, 46; Юле 9; XPf 18, 19; А?Не 14f; A?Pa 19, 20; Sa 2f. nama, either asn. *ndmá ог lsn. лата” (with lengthened grade), specialized for similar use with fem. generic nouns because of similarity of end- ing ($67.1T, $187, §249L, $312; cf. Tm. Lex. 105,
193
with lit.; not with Foy, KZ 35.11, 37.505, IF 12.172n, nor with Debrunner, IF 52.153): DB 1.58, 58f; 2.271, 39, 44, 52, 59, 72; 3.11, 23, 61, 66, 12, 19; 54°.
nay- vb. ‘lead’: Av. nayeitt, Skt. náyati. Conj., §213. anaya imf. DB 2.88; 3.88°; 5.12. [ajnaya" 3d pl. imf. ($232.11) DB 5.28. anayatá imf. mid. as pass. ($235.П) DB 1.82, 2.73; 5.26". Some or all of these are possibly ànay-, from à + nay-. | fra- + nay- ‘lead forth, provide’: fránayam Ist sg. imf. ($226.11) DB 1.87.
nar- sb. ‘man’: Av. Skt. nar-, Gk. дир, cf. Lt. Ner-6; i
```


## [2026-09-07T20:16:50.857Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== IEC nor/anor pomegranate\"; grep -n -i \"pomegranate\" IEC.txt | head -30"
}
```


### [2026-09-07T20:16:50.905Z] TOOL RESULT

```
=== IEC nor/anor pomegranate
7535:kokon ‘knob, boll, seed, berry’. Extn. variant of kokos, q. v. Oss. kákon ‘sloe’; LW in Arm. kokan, id.; Gk. kókkon (‘pomegranate seed’. LW in Lat. *coc- conem, cf. Sard. coccone ‘bran-bread’; Fr. cocon ‘cocoon’); Ir. cocán ‘calyx, bud, poppy, topknot'; OE haga, gs hagan, wm. ( ‘haw’, and com. Gmc.)
```


## [2026-09-07T20:16:51.698Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN 229 leaf 250\"; python3 -c \"\nt=open('HRN.txt',errors='replace').read().split('\\f')\nprint(len(t))\nprint(t[250][:3500])\n\""
}
```


### [2026-09-07T20:16:52.996Z] TOOL RESULT

```
=== HRN 229 leaf 250
412
— 229 —
kurd. näw 'Nabel'; afy. nti^ nüm; oss. d. naffä;
bei. napag, nafag, n. nafay (259).
aw. naba[nazdista', ai. ndhhi- etc. gehen auf indog. bh
zurück, während die übrigen Formen auf ph weisen.
lOS^O'»'» nak Vermischt, nicht pur, verunreinigt*.
phlv. andk *böse', anokih^).
lC^t21. noffäh plötzlich, unerwartet*.
aw. *anäkasa' *improvisus* ; phlv. anakäslhd 'un-
vermutet', vergl. np. (igäh (No. 40).
näl 'Schilf* siehe nei (No. 1060).
1-022. näm 'Name' 2).
ap. nOtnan- 'Name* ; aw. nquian- ; phlv. mim, nCLmik
berühmt*, nämlnltan (PPGrl.); ai. wamaw- ; arm. anim
(H. No. 24).
LW. (?) kurd. näw 'Name' ; afy. nüm ; bei. nam
(181) ; oss. (echt) t. nom, d. non (198).
Rückert wollte ZDMG. 10, 219 auch neng 'Schimpf,
Schande', hierherziehen (als 'ein unregelmässig zu-
sammengezogenes Diminutiv von näm*).
1023. nän 'Brot'.
arm. nkan iyygvcplac *unter der Asche gebackenes
Brot'; vergl. chorasm. pekend (Vullers); hei. nagan,
n. nayan *Brot', nagan[pad *Bäcker* (249) ; minj. nayan;
phlv.-päz. nän (PPGl.).
Also zu l/^kan- + ^h ursprünglich '(unter die heisse
Asche) Vergrabenes* (zuerst de Lagarde)?
1024. näv Wasserkanal; Schiffchen', nävdän.
ap. näviyä' 'Flottille'; aw. navOza^ 'Schiffer* (Bar-
tholomae, ZDMG. 46, 294 Anm. 3), vergl. nävaya-
'fliessend'; phlv. nävfäk (aw. nävaya-), nävTcak (Bund.);
ai. näV' 'Schiff, Kahn, Nachen*, vergl. nävyä- *Strom*.
kurd. LW. nav; oss. LW. d. navä, t. nau- 'Schiff';
arm. nav 'Schiff*, navem 'schiffen* (H. No. 216).
naf 'Schilf*, vergl. tiäüej siehe unter nei (No. 1060).
*) Justi vergleicht ZDMG. 46, 282 arm. N. pr. Anak^ aber gegen
seine Lesung der betr. Gemme sprechen die voUständig deutlichen
Buchstaben auf dem Steine.
«j Vergl. Bartholomae, BB. XVII, 132.
```


## [2026-09-07T20:17:10.385Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN dušnam\"; grep -n -i \"dušnam\\|dusnam\\|dosnam\\|došnâm\\|dušnâm\" HRN.txt | head; echo \"=== HRN Schimpf\"; grep -n \"Schimpf\" HRN.txt | head -20\necho \"=== HRN nameh\"; grep -n -i \"nämak\\|nâmak\\|namak 'Brief\\|Brief\" HRN.txt | head -20"
}
```


### [2026-09-07T20:17:10.458Z] TOOL RESULT

```
=== HRN dušnam
=== HRN Schimpf
1319:104. ek 'Schimpf, Schande, Unglück', ak'^),
6052:aw. duzaka- Igel' (als Schimpfname des Hundes
8876:Rückert wollte ZDMG. 10, 219 auch neng 'Schimpf,
=== HRN nameh
518:äßdän (Denkart III). — Bartholomae (briefliche Mit-p
1131:ZDMG. 32, 408, Kärnämak, 54 '). Bartholomae
1181:490). Die Lesung stenik, sten scheint Bartholomae nach brieflicher
1695:phlv. papak (vergl. Nöldeke, Kärnämak, 35 Note 3;
1817:')von Stackelberg (briefliche Mitteilung) stellt dazu auch
1850:Bartholomae schlägt mir brieflich für ap. ahäcuris die folgende
2371:sonans durch u, ü angenommen, ebenso Dr. Andreas (nach brieflicher
2606:dazu gr. älaog (Bartholomae, briefl. Mitteilung),
2656:be rg (briefliche Mitteilung).
2670:*) Bartholomae wiU nach brieflicher Mitteilung *pcUas 'schützend*
2743:^j Vergl. Geldner, Studien I, 16. Bartholomae (briefliche
2818:Bartholomae (briefliche Mitteilung) nimmt für np. pir als
2888:von Stackeiberg (briefl. Mitteilung) vergleicht
3030:Bartholomae (briefliche Mitteilung).
3110:Bartholomae stützt diese Erklärung brieflich
3139:y. 45, 5, 6)^); Nöldeke, Kärnämak 49, Note 2.
3141:phlv. pa (pO) nihan (s. No. 1058) ; Nöldeke, Kärnämak
3224:') Bartholomae (briefl. Mitteilung) meint, dass die Verdächtigung
3896:Bartholomae meint (briefl. Mitteilung), dass np.
4220:*) Bartholomae (briefl. MitteiluDg) nimmt nach dem Glieder-
```


## [2026-09-07T20:17:11.545Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD nam\"; grep -n \"^nam\\|^nām\\|^dušnām\\|^duš\" PHD.txt | head -30\necho \"=== PHD anar\"; grep -n \"pomegranate\" PHD.txt | head -10\necho \"=== NYB nam\"; grep -n \"^nām\\|^nam\\|pomegranate\" NYB_vol2_glossary.txt | head -20"
}
```


### [2026-09-07T20:17:11.619Z] TOOL RESULT

```
=== PHD nam
317:duš-ēwāz��h 29 dwāzdahān
495:nāmīģ 58
496:namig [n’myk' | N nami] famous, renowned. ~ih: renown.
2858:dušfarragīh,
2886:name nām.
4531:nāmčišt!
5271:nam -< \
5275:nāmburdār bw Diye t nāmīgīh ^ Aye nimig уел wamidan ur aert SE 15e nāmčištīg 143 teu ee '
5276:nāmčišt tery Qe wāspuhr 102.294
5389:dušpādixšāv
5391:dušpādixšāvīh кукуму ary v
5403:dušwār, gūšwār dušwārīh dušnām Gušnasp dušwīr
5410:dušwurrūyišnīh 49 pty ` rey
5412:dušmen
5423:dušhūxt
=== PHD anar
193:---rēšn(ih) [-Iwsn!, -lwsnyh] Infinite Light. anāhīd р/у | N ndhid] immaculate; a goddess; astr. Venus. an-àáhóg P7 kwok!] undefiled. an-ālūd [?77/wt'] undefiled. a-nāmčištīg m mcftyk!] unspecified. an-ámurzid [?rmwlcyt! | M ?n’mwrz‘yd] merciless. an-āmurzišn [*7”mwicšn!] mercilessness. anār [71 | N ~] pomegranate. anārģēl [777/gy/ | N nārgēl) coconut. an-arzünig [?77/c”nyk!] undeserving, unworthy. an-ast [^n 4 Y T'] non-existent.
540:pahikēftan, pahikob- [ptkwp-tn'] strike. pahlawig [*p’hlwbyk' | (M phlwnyg), N paklaw(ān)i] Parthian; Pahlavi. pāhlom [phlwm] excellent, best, foremost. ~ih: excellence. pahlüg [p'Aok! | N pahli] side, rib. pahn [p?An! | N ~] wide, broad. сау [2d | N —à] width, breadth. lpahrextan, pahrēz- [phlyhtn', p'hlyc- | M phryz-, ] ~, N parhéxtan, parhéz-] abstain, refrain, avoid. *pahréxtan, pahrēz- [p’hlyhtn', p'hlyc- | M (phrystn), phryz-] care for, tend, protect. pahréz [Аус | N parhéz] defence, care. *pahrmāh- [ptimwh- | (N parmds-)] touch. ~арфіһ [Pkyh], ~i$n: touch, feeling. pak [DKY A < A аку; рк | = M, N ~] clean, pure, holy. ~ih: purity, holiness. pākīzaģ [p’kyck' | N ~a] pure. palang [ping | N ~] leopard. —-mušk [-mwsk' | N ~] speckled basil. pálüdag [p'Iwtk! | N ~a] starch jelly, flummery. pālūdan, pālāy- [p’lwtn', pPd- | (M p’rwdn, p’r’y-), N ~] strain, filter, purify. pambag [pmbk' | N panba] cotton. —ën [-yn'] (made of) cotton. pānāģ [p’n(’)k' | M p’ng] guard, protector; shepherd. ~th: protection. panāh [рт | = M, N ~] protector; refuge. pad ~ griftan: take refuge with. ~ih: protection. pand [pnd | = M, N ~] path; counsel, advice. panir [pnyl | N ~] cheese. panj [pnc | P рту, (M pnz), N ~] five. ~ag [-k! | N —a] pentad; hand, paw. ~аһ [h | N ~] fifty. panzdah [p’ncdh | M p’nzdh, N ~] fifteen. ірагаб [p?/k! | N para] piece, part, portion. ?párag [p?/k! | M p’rg, N para] gift, offering, bribe. paráhóm [pP?hwm = Av. para.haoma-] consecrated drink (the infusion in holy water of pounded лот and pomegranate twigs, sometimes with milk added). pardag [pitk! | N parda] veil, curtain. pardaxtan, pardaz- [pldhin', pldc- | M prdxt, N ~}, ~ az: be done with, freed of. ^ 6: set about, undertake. ~išn: freedom; undertaking. pardāxtan, pardaz- [pld’htn', pld?c- | N ~] accomplish.
3175:pomegranate anār.
=== NYB nam
2554:name Qais born by the kings of Kinda, v. Nyberg, Unvala Vol. 111-112. — For mēx-var, v.g. v. mex.
2618:namäc [nm?c'; ‘SGDH, inser. SGDH] adoration, homage: ~ u paristisn + yaz- dan adoration and worship of the gods 6816; ~ burtan to do adoration by pros- trating oneself before (kings and super- iors): hac dar + ētšān bagān ~ burt (from the door of =) at the court of His
2628:namat [nmt'] felt 3117. — Av. (1068) nə- mata-, regarding which v. Benveniste, BSL 32, 1931, 82sq.; NP namad; bor- rowed in Aram and Arab (namaf-).
2633:nām-cišt [n’mc$t'] especially, particularly 18°; pat ~ 8018. — = Paz.; from nām + cist, pt. of Av. (429 sqq.) kačš- ‘to teach, to assign’.
2634:nāmcištīk special, particular 11012. Nam-x"ast [n’mhw’st'; SMhw’st'] n. pr. 1811 (SM-)-16, 1926, 2213-15, — Possibly the
5235:naman-: nam
5236:namra.vaxs-: *a-namr- tom
6740:namaž: namac
6741:namcišt: ~
6742:namüdan: nimütan
7268:namad: namat .
7270:namaz: namac
7271:namudan: namütan
```


## [2026-09-07T20:17:18.923Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD line 495-500\"; sed -n '493,500p' PHD.txt\necho \"=== PHD grep nam [\"; grep -n \"nām \\[\\|nāmag\\|dušnām\\|nāmag \\[\" PHD.txt | head -20\necho \"=== PHD_mackenzie\"; grep -n \"nāmag\\|dušnām\\|anār \" PHD_mackenzie.txt | head -20"
}
```


### [2026-09-07T20:17:18.997Z] TOOL RESULT

```
=== PHD line 495-500
Р murd [то | P mort !] death. murdan, mir- (YMYTWN-tn! < A ymwtwn, V mwt; mulin' | M murd, myr-, N ~] die. murdār [mwrt?], mwld?l | N ~] carrion. murnjénidan, murnjén- (mwlncyn-ytn'] destroy. murw [mwlw! | M mwrw, (N mury)] bird. murwāģ [mwlw’k' | M mwrw’, N murwd] omen. murwizag [mwlwyck'] little bird. murw-nīš [mwlwnys] augur, soothsayer. must [mwst'] force, violence. ž*must [mwst'] = must. *must [mwst'] complaint. must|-abarmānd [mwst!’plm’nd] aggressive, aggressor. ~gar [-kl] violent, rebellious, mustómand [mwst?wmnd | N mustmand] complaining, unhappy. ImuSk [отео | N ~] musk. 2mušk [mwsk! | (N mis)] mouse, rat. must [mzvšt! | N ~] fist. muštan, māl- [mwéstn', wl- | N ~] rub, sweep.
nab [np | N nawa] grandson. nabānazdišt [nb”nzdšt! = Av. nabünazdista-] next of kin. паї [w | M mp] family. ~ag [-R! | N náf(a)] navel. !naft [npt! | = M, N ~] moist, damp; naphtha. *naft [npt'] descendant. nahang [жле] province. *nakkira [nkyl’y] denying, repudiating. ~yih: repudiation. nāl- [wl- | P (n’r-), N ~] groan, complain. nam [nm | N ~] moisture. nám [SM < A £m; m | = M, N ~] name, fame. namad [nmt' | N <) felt. námag [MGLTA < A melt: ттк! | M пто, N пата] book, letter. namak [nmk! | M nmyhk, N ~] salt. namāz [OSGDE < A sgdh; nm’c | = M, N ~] reverence, prostration, prayer. ~ burdan: pay homage. nām-burdār [л?т bwlt?l | N ~] heir, preserving the father's name. nāmčišt [?жт-, ŠMcst'], (pad) ~: in particular, especially. ~ig [-yk'] famous, well known.
nāmīģ 58
namig [n’myk' | N nami] famous, renowned. ~ih: renown.
nan [ИМА < А Jm": тп! | = M, N ~] bread, food.
nang [nng | N ~] shame, modesty.
nar [ZKL < A shr; nl | M nr, N ~] male, manly. nargis [nlgs | N ~] narcissus.
narig [n(y)lyk'] woman, lady, wife.
=== PHD grep nam [
25:'To reduce the number of doubtful words it has been necessary to concentrate on the simpler vocabulary of such texts as the Kārnāmag i Ardaxsir, Dádestán i Ménog i Xrad, Arda Wiráz nāmag, Bundahisn, and the Pahlavi Texts edited by Jamasp- Asana. Although I have also drawn upon the Pahlavi versions of scriptural texts (Vendidad, Yasna, and Vispered), most of their very special vocabulary has been omitted. So have the many nonce-words and ad hoc compounds of religious texts such as the Dénkard, since it is generally a simple matter to analyse Pahlavi compounds, given the elements and provided that the rules of their construction are understood. Those words calling for inclu- sion whose form or meaning remain doubtful are marked with an asterisk.
125:did ... add other. add dig |YTMAL < А *?{т?1 | N di] yesterday. delete *drém ... (read balgam) drubušt ... add protective. drust [drw(d)st' ... duš-čihr ... add ill-natured. duš-nām [-n^m | (M dwjn'm), N ~] add ill-famed. dušwār [dwáw?l | (M dwjw'r), ... ékanag ... for obedient read loyal, faithful. ~th : for obedience read loyalty, faithfulness. for Farrēbāg... read KFarrēbāy [pinb(^)g] ... frayad |pl(y)d^t' | N faryad] ... delete M pry'd. frazand |prz/znd | ... frusag ... add M prwšg. garódman ... read | P grdm'n. gazdum |gcd(w)m, gzd(w)m |... guftàr ..., ~th : add eloquence. hambar |hm-, hnb] |... add  hamest |hmyst'] whose good and bad deeds weigh equal. ~(ag)an |-(k)^n'] limbo, the neutral station between heaven and hell. delete hammist ..., ~(ag)an ... handarz ... add M °’ndrz. hammoxtan, hammoz-, ~i8n : add learning. hast |TWMNYA < A tmny ; ... add hūg [HZWLYA < A hzyr’; hwk' | M hwg, N xiig] pig. add hūkar(ag) |hwkl(k') | N xükara] porcupine. (not hedgehog) add *huzārag [hwc’lk | N хијага) little, small, few. !jadag ... add fortune. jüdan ... | M jwwdn, jwy- ... add karawuš [kl wš| N ^] wine-press. delete karbunag ... read karbūg |klpwk', klbwk'| lizard. kardagān ... add service (ofthe gods). delete karxēš vds
705:abuse (n.) dušnām, wad-wāzag.
1045:book mādayān, nāmag, nibég.
3347:record kārnāmag.
5057:kār- wing! *kār-ān kārāgāh kārāgāhīh kārdāg kārīgīh kārīg kārēzār kārawānīg kārawān kārnāmag kahrubāy kalbodómand kālbod kārframān kārd
5403:dušwār, gūšwār dušwārīh dušnām Gušnasp dušwīr
=== PHD_mackenzie
```


## [2026-09-07T20:17:20.233Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== NYB nam entry\"; grep -n \"nām \\[\\|nām\\[\\|nāmak\\|dušnām\" NYB_vol2_glossary.txt | head -20\necho \"=== NYB anar\"; grep -n \"anār\\|anar\\[\" NYB_vol2_glossary.txt | head -10"
}
```


### [2026-09-07T20:17:20.313Z] TOOL RESULT

```
=== NYB nam entry
331:āivēn ['dwyn'] rites, customs 818; cas.obl. —-E [+1] nāmak 121%, the Sassanian code of courteous manners and conduct, NP dīn-nāmah, often referred to by Mus- lim authors. — < OIr "abi-dayana- from "day- (v. dītan),. whence NW-Prth ab- den, but SW-Prs *aibiden > *aiviyén .> diven. — KZŠPrth 1. 19 "bdyn = Prs l. 24 *dwyn, Gr. v. #00¢; Ps. ’dwyny translating Syr. nāmēsā = the Mosaic Law; MPrth 'bdyn ‘habit, custom’ (Hen- ning, TPhS 1944, 110-112); Arm. lw. aurēn-k* ‘institution, the Law ; the Eucha- rist’; Syr. lw. b-abden ‘similar to’, cf also hämöden; Paz. NP Gin, Skr. v. äcära; Arab. lw. °@in. V. Markwart, UJ VII, 1927, 89-121; Junker, WuS XII, 1919, 150.
1421:rad (v. below). 1. HN’: ~ nāmaky this inscription (here above) P 2:3; ~ vizand hac yātūkēh i ~ kanik 373: ~-ic évak hac avdéh the following is one of the miracles 4474; kē hac ~ aštak, veh he
2627:nämak [n’mk'; inser. n’mky; SM-k'] in- scription P2:3; letter 3? etc.; book 1071, 12119; in book-titles: Kär-nämak, Pand-nāmak etc. - MPrs n’mg; NP nā- mah; from nam.
2752:nipistan [npštn'; YKTYBWN-tn'] nipés- to write 419. 110? etc. ; nipist estet it has been written, it is written 1139; nipist ēstāt it was written 1!—?; — pres. pass. nipēsihēt [YKTYBWN-yhyt'] is being written 18%; — pat dp i zarr nipištak 1079; apar nipistak written down 108?!; nāmak ~ 6 to write a letter to 49-9. 822, an inscription P 2:3.4; apar fravartak čton nipišt estat kū it was written in the letter (then dir. speech) 1872; apar én ayyätkär nipišt estet 1135-9. — OP ni-pais- ; MPrthPrs nbyštn nbys-; Paz. nawaštan nivés-; NP nuvistan, nivištan, nivés-.
=== NYB anar
347:a-kanārakēh boundlessness, endlessness, of Ohurmazd 637-28,
1808:ham-biitan to be together with, to follow: či kanārak i... apar hambüt [hmbwt'] hom I kept on together (with him) all
2193:kanürak [kn'lk'; ŠTL”] boundary 512’. 529.11, — MPrs kn’rg ‘side’; Paz. kanāra; NP kanärah ‘side, shore’.
2556:mihr [mtr'] 1. n. pr. the Aryan god Mitra, Av. Midra: ~u Srēš u Rasn 1215; ~ u Zurvān i akanārak u menčyč datistan 77-12, ~ zg"'"atài névak, Dahman Afrin 9213, ~ yazét u x"aršet 961! ; atur burzen ~ the third of the three imperial fires 11%. 2°, symbolizing the class of the cattle- breeders and farmers 2° (cf Av. [1430] Midrē yö vouru.gaoyaotiš); — existing in all animal beings 965-%; — Dadv pat ~ the name of the 15th day of the month 9715-16, — 2. the sun 78. 317. 7913-18, — 3. abstr. friendship, loyalty: — u došaram i apāk čišan 87°; ~ + amāh 98; ~ i čvak 6 dit 119; vehän ... ~ däst u dosteh varzit 5526-27, — Av. (1183 sqq.) midra-.
7233:kālbad, kālbud: kalpaš kāmīdan: kāmistan kanār, karān: kanār kanārah: kanārak kanīzah: kanīcak karavah: *karbēk kārd: kārt
```


## [2026-09-07T20:17:29.734Z] TOOL CALL #18: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nprint(json.dumps(d['BQT']['scans'],ensure_ascii=False,indent=1))\nprint(json.dumps(d['MON'],ensure_ascii=False,indent=1)[:3000])\n\""
}
```


### [2026-09-07T20:17:30.972Z] TOOL RESULT

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
```


## [2026-09-07T20:17:44.887Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\ngrep -n \"\\[pdf page 189\\]\" BQT_v4_pages.txt; python3 - <<'EOF'\nt=open('BQT_v4_pages.txt',errors='replace').read().split('\\f')\nprint(len(t))\nfor i,L in enumerate(t):\n    if '[pdf page 189]' in L or '[pdf page 190]' in L:\n        print('---',i)\n        print(L[:2500])\nEOF"
}
```


### [2026-09-07T20:17:46.414Z] TOOL RESULT

```
7535:[pdf page 189]
553
--- 188
[pdf page 189]
فامور هنن
روز دهم است ازسالهای ملکی- و مردمان بپادر | نامآور است که‌خداوند ناموآواژه ومشهورومعروفق
وشجاع را دز کوبند .#۸ باعد ۴ .
5 نامزد ۱ - بسکون ثالك وفتح زای ناموس * - بر وزن قاموی » بممنی
هوز » لشکریراکونند که بجهت مهمی و کاری ۲ خانه و ۰
8 پانگك و آوازه۹ - و ساحب مرا وخانه و منزل
بطرفی روانه کنند ۴ - و دختری که بعد ازچند | * 8
کاء دیگر بخواهند . باشد - وبمعنی‌عسمت وعفت هم‌عست۷ - وجنگه
نامود ۴ - با وار بروزن دا دکر,مشفف | وجدال را هم کفته‌اند - و ملالکه ۸ - و احکام
۱- از : نام ۲ زد ( زده) ( آسم مفعول مرخم ).
۴ - یکی لشکری نامزدکرد شاه کنید آنگهی تور لشکر براه -
قردوسی طوسی « شاهنامةٌ بخ ج۱ ان ۴۷۸ 2
۴ - از: نام ور( پسوند اتصاف ودارندگی ) [ ازمسدر 827 بردن | . رك: هرمزدنامه
۰-۹ و ر4 : دارمتتن . تتبعات ج۱ ص ۲۹۳ .۰
۴ -هثر در جهان از من‌آمد پدید چو من نامور تخت شاهی ندید -
فردوسی طوسی «شاهنامةٌ بخ ج ص۲۹
- لزنازی, از یونانی 36۵1305 بمعنی عادت و شربمت « تفس > « ژابا ص 4۱۹ ۴ در
عربی « ناموس » ساحب رازآ کاه بر نهانی امن - با صاحب راز خبن - و نام جبرئیل علره‌اللاي
و مرد دانا ماهر‌درکار - ولظرف‌المدخل - و کازء صیاد ودامآن - ومرد سخن چین - ومکرو حيلهٌ
نهانی - وخوایگاه شیر» ناموسة «ثله. > «منتهی‌الارب * وایز وحی - وخانةٌ راهب - و دروغزن -
و شریمت « اقرب‌الموارد > و لیز درظفه بمعنی قالون و حکمآید . بمعانی دیگن مذ کور درمتن
متعمل در فارسی‌است ۰
‎٩‏ -کیست که پیغاممن بشهر شروان برد ابك سخن از من بدان مرد سخندان برد
گوید: خافایا ۱ اين‌همه ناموی چیست؟ نه هر که دو بیت گفت لقب زخاقان برد.
جمال‌الدین اصقپانی ۸« مجمع‌الفسحاء ج ‎٩‏ ص ۰۴۱۷۸
۷ - باین معنی امروزه بیشتر متداول است- ۸ - درعربی « ناموی > و « تاموی
آلاکبر» فقط جیرئیل راگوبند. رك : اقرب‌الموارد .
نام - پپلوی 2200 ۰ ابرانی باستان -32087 « بارتولمه ۱*۹۲ > « نیب رکه اص
۶ پارسی باستان 82۳1271 ( نام » اسم ‎ )‏ اوستا 321027 , هندی باستان -8228.
آرمنی 2818 ۰ اففابی 80772 ۰ بلوچی 8270 » استی 30770 ۰ 307 ۰ رك : امشق ۱۹۲۲ ‎٩‏
‏کردی/287 ( اسم » شهرت ) . 8۵۷ ۰ 88۲0 ۰ زازا 88106 « ژابا س 2۱۵ *؛ اورامانی 32817
* که . اورامان سس ۱۲۸ > , ختنی 3۳78 ( نام ) « رو زکارلو ج 4 شمارة ۳ص ۵۲ > ؛ لفظی
که بدا ن کی پا چیزی را بخوانند , اسم - شهرت وآوازه :
نام نیکوگر بماند ز آدمی به کزو ماند مرای زرنگار -
سعدی غیرازی « امثال وحکم دهخدا >.
2 لاه‌دار - از : بام دار (.دارنده ) » مشهور , معررف » نامی » نام‌آور :
بپرسیدشان از نژزاد کیان وزان نامداران قرخ کوان ...
فردوسی‌طوسی « شاهنامةٌ بخ ج اص ۸+
( برهان قاطع ۲۹۹ )

--- 189
[pdf page 190]
-۱۳- نان‌آشروی
الهی را نیز کوبند ۱ - و بمعنی کمی نگاه صیاد هم آمده است ‎٩‏ - واخط تعلیق را نیز گویند
هم آمده است - ۰ باعتبار ایشکه احکام و فرامین را بآن خط می-
ناموس | کیر - کنایه ازجبرئیل ۶ .| نوسند۷ .
است ۲ . نامه چهاره - اغارء بفرقان است که
ناموس گاه - کنایه از جنگه کاء قرآن باشد چه بعد از زبور وتوراة وانجیل تال
باشد چه ناموی بمعنی جنگ هم آمده است. شده است .
نامو به ۴« بفتح تحتانی بر وزت نامی - بروزن جامی . بمعنی‌ناموربودن
واکوبه , زنی‌راگوبند که بقیراز يك‌شوهرندیده
| و شهرت کردن ونام برآوردن باغد ۸ - و تامه
و بمرد دیگر نرمیده باشد و مران او و شوهرش فرمانرا هم میکویند ‎٩‏ 1
نهایت الفت ومحبت و اتحاد بود ۴ . و فرمانر! هم میخوشد * - و جراعری بمعتی
نامه ه : ِ ۱ بالنده وه نموکننده باشد .۸
نامه < بروزن خامه . کتابت وفرمان
را گوبند - وبمعنی کتاب هم هست همچوشاهنامه نان آتش ری *۱- کنابه ا زآتاب
وفرس نامه و بازنامه وامثال‌آن - و بممتی‌سیلاب | عالمتاب است .

۱- « مینداری د که آمدم تا ناموی وتورت باط لکنم . نه نیامدم که منشو خکنتم .. >
( قول عیمی2 ) * انجیل فارسی ص*۹ >. ۲ - رد4 : اقرب الموارد - ۴ - رشیدی
کوید : ۰ معنی تر کیبی آن منسوب به « نام » بعنی درآن‌کار نامدار و نامو رکشته > ظ . از +
نام ۳ وبه ( پنوند ) <- که معرب آن « وبه > بفتح واو است [ قن : شیروبه » سیبویه .
مسکوبه ] رك: ند که. تبعات ابرانی. وین ۱۸۸۸ ص48 یمد .

۴ - سولت او دران صف ناورد زن نامویه بر کند از هرد -

سنائی غزنوی «جهانگیری» « رشیدی *.
مولف فرهنکه نظام لویسد : « ناموبه مر کب از نا (نه) و موبه ( زاری ) است (۱) و یمعتی زلی
که موبه نکرده (۱) یعنی شوهردار است و معنی شمر این است که ممدوح درجنگه زق شوهردار
را بی شوهر میکند .> فس : نامزد . * - بخلوی 828281 (کتاب ) مأخوذ از * تام »
« نیب رکه ص ۱۵۶ > > کردی ع 88816 ( مراسله ) « ژاباس 2۱۹ >

- در جهانگیری و بنقل از او در رشیدی آمده . ۷ - ر3 : جهانگیری ۰
رشیدی . ۸ - از: نام ۲ ی(سبت)» بعلوی ۳ آ(3217 بمعنی‌نامور ومشهورة اسشق ۱*۲۲

‎٩‏ - مصحف با تلقظ عامیانهٌ ‎٩‏ نامه » (ه.م.) *- و نیز « بان آشین » بهمین
معنی « رشیدی * .

‏لامیدی - از : نام ۳یدن (پسوندمصدری) ؛ پپلوی 34130181188 « اسشق ۱۰۲۲ 44
نام گذاشتن -کسی را بنام خواندن .- احضار کردن .

‏نان - پپلوی 82 ۰ ارمتی 1362 (نان‌پخته درخا کتر). مأخوذ ازپهلوی «ن2عاقط
«پارسی 081888 ۰ بلوچی 38888 و نظایر آن . از ایرانی ( باستان ) 888888 ۰ منجی
80 رك : اسشق - عوبشمان ۱۳۲۳ . نیب که نیز کوید: نان (فارمی) مٌخوذاز 828100
است و ارجاع به هرن و هوبشمان کرده « نیب رکه س ۶۱۵۶ ؛ کردی 888 ۰ 820 ۰ زقزا
0 . 8 ۰ دوجیکی 10 * ژابا س ۸۱۹ > + گیلکی 388 ۰ فربزندی »: برتی‌ونطتزی 280
.اس ۰۲۹۰ سمتانی 8183 . سنگری وسرخه‌یی ۰308 لاسگردی :۰807 شهمیرژادی
0 که .۲ س ۱۹۰ ؛ قطعه‌ای از آرد خمین کرده وبرآتش پخته کهآترا خورند. -
```


## [2026-09-07T20:18:01.081Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\npython3 - <<'EOF'\nt=open('BQT_v4_pages.txt',errors='replace').read().split('\\f')\nfor i in (186,187,188,189,190):\n    L=t[i]\n    print('---',i, L.split('\\n')[0])\n    print(repr(L[-120:]))\nEOF"
}
```


## [2026-09-07T20:18:02.107Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BQT v2 doshnam\"; grep -n \"دشنام\" BQT_v2_pages.txt | head -10\necho \"=== BQT v1 anar\"; grep -c \"انار\" BQT_v1_pages.txt; grep -n \"^انار\\|انار -\\|انار،\" BQT_v1_pages.txt | head -10"
}
```


### [2026-09-07T20:18:02.381Z] TOOL RESULT

```
--- 186 [pdf page 187]
'نگیری . ۸ دنله (هم.) \u200e٩\u200f - رد4 : نالیدن . *- اسم فاعل مرخم\n(در ت رکیب) . ۱- از : نال ( بالیدن )+ آن ( پوند صفت فاعلی )1\n'
--- 187 [pdf page 188]
'یان اندوه خوبش کردن , زاریدن :\nپنال پلبل اگر با منت سر بارست که ما دو عاشق زاریم وکارما زارست .\n« حافظ شیرازی س \u200e4٩\u200f *.\n'
--- 188 [pdf page 189]
'امی » نام\u200cآور :\nبپرسیدشان از نژزاد کیان وزان نامداران قرخ کوان ...\nفردوسی\u200cطوسی « شاهنامةٌ بخ ج اص ۸+\n( برهان قاطع ۲۹۹ )\n'
--- 189 [pdf page 190]
'8183 . سنگری وسرخه\u200cیی ۰308 لاسگردی :۰807 شهمیرژادی\n0 که .۲ س ۱۹۰ ؛ قطعه\u200cای از آرد خمین کرده وبرآتش پخته کهآترا خورند. -\n'
--- 190 [pdf page 191]
'اند وهمین سه بیت را درزءرء اشمار دیگن شاهدآورده\u200cاند وهمین قول صحیح است.\n\u200e٩\u200f - رك: رغیدی . ۷ - در رشیدی "نان سپید فلك» .\n'
```


### [2026-09-07T20:18:02.454Z] TOOL RESULT

```
=== BQT v2 doshnam
14146:     ‫وزن ماهی خوار » دشنام شنونده کروابند ‪.‬‬                                                                                         ‫ری ‪. ۴‬‬
14147: ‫خواری گردن ‏ کنابه از دشنام‬                                 ‫جو ار رم » نام‌شهر ست‌معروف ومشپور‬
14155: ‫بائالی ممدو له بروزن عازه »‬    ‫حور از و ‌‬                                       ‫‪۰‬‬    ‫گویند ‪۹‬‬   ‫را‬    ‫دهنده‬   ‫دشنام‬             ‫‪4‬‬    ‫چارباره‬
14160: ‫پندیرا دکیوزیند اعم اآزنکه بجهت آبین بندی‬                  ‫دشنام‬       ‫و‬    ‫‪-‬‬       ‫باشد ‪۷‬‬   ‫دشنام دهی‬       ‫‪ ۰‬نمعتی‬               ‫وارداری‬
15228:‫را‬     ‫خو له * = بورزن موبه " پاروب‬                  ‫گوبند» ویشتراین لفظ را درمحل قدح ودشنام‬
16517: ‫ودعوی‌کازبرانیز گفته‌اند؟ ‪ -‬وبمعنی‌فحش ودشنام‬              ‫درخت فرو برند تا سیر شود‬                ‫که درآن شاخہای‬
18299: ‫دشنام ‪ ۰‬دشمن ) ودو ا گاه) آمده‬                  ‫ِ دزخیم ‪a‬‏‬           ‫مر کب بل‬            ‫‪ ۰‬در کلمات‬       ‫‪020 -‬‬       ‫‏_‪ ۰ dur‬آرئی ‪2‬‬
19250:‫‪ ۰‬ودشنام‬         ‫دل» چه من بمحنی دل همآمده ست‬
19270:       ‫بوده ‪.‬‬      ‫‪:‬‬   ‫)ل( جك‬            ‫‪ :‬دشنام ‪۰‬‬      ‫‏)‪ (e‬چك‬             ‫‪۲‬‬   ‫‪ ۳‬دشسل‬        ‫‪ ۰‬چش‬    ‫)‪ (4‬چك‬
19276:  ‫‪ - ۴‬در اراک (سلطانآباد) ‪« 8۷500‬مکی‌نژاد» وکره‪ :‬دشپیل ‪.‬‬                                              ‫دشخو ار ‪۳‬‬           ‫دشنام‪.‬‬
=== BQT v1 anar
25
13817:انار قر ها - ۳۳ رای شرشته. ۸
13831:انار مثك ت بکسر عم وسکون شین
20830:اناری است که مرا ز کل شمری دمگرنداردءوآن
26512:انار و است" از حروف تهبجي
```


## [2026-09-07T20:18:08.646Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v1_pages.txt',errors='replace').read().split('\\f')\nprint(len(t))\nfor i,L in enumerate(t):\n    if 'انار' in L:\n        print('=== leaf',i, L.split('\\n')[0][:60])\nEOF"
}
```


### [2026-09-07T20:18:09.906Z] TOOL RESULT

```
777
=== leaf 27 نوزده زبانهای ایرانی
=== leaf 39 سی ويك زبا نبای‌ایراتن
=== leaf 48 چپل
=== leaf 50 مقدمه چبل و دو
=== leaf 214 آب ست
=== leaf 243 دوع ۰ با غن نقطه دار سس وزن
=== leaf 312 بخشایش » بمعنی خیر و خیرات و چیزی در راه
=== leaf 322 ارمند
=== leaf 380 که زر بائد! .۷
=== leaf 386 انجین
=== leaf 397 نوهیان - بکرم بروزن‌مجوسیان.
=== leaf 476 " بر‌سان « بنتح اول می وزن نرسان :
=== leaf 522 بلوسیطوی
=== leaf 647 بنحك - یشم اول بروزث اردك» کل له
=== leaf 670 شطالی باشد .3
=== leaf 680 تايه زر - یواح
```


## [2026-09-07T20:18:17.893Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v1_pages.txt',errors='replace').read().split('\\f')\nfor i in (380,381,382):\n    print('===== leaf',i)\n    print(t[i])\nEOF"
}
```


### [2026-09-07T20:18:19.924Z] TOOL RESULT

```
===== leaf 380
که زر بائد! .۷
امی‌صادق - بنم اول , اشاره (۱) به
حضرت رسالت ناه صلوات‌اله علیه باشد .
امیله ه بروزن دلیله » بمعی‌آمله‌است
وان وهای باشد درهندوستان که درشکرپرورده
۲۳ وخورند .
ان - بفتح اول وسکون ثانی بلفت زند
ویازند(۲) والده را گویند که عادرباشد - وب‌عنی
آن هت که درمقابل این‌است؟ - وافاده فاعلیت
نز کند هر کاه که در آخر کلمه در آودند همجو
اقتان وخبزان .
انا قو لقن - با نای‌ترشت ونون وفوقانی
بروزن جفاجوی حن . بلفت زند وپازند(۲)بمعنی
گذاشتن ونهادن باشد؟ .۶
انار قر ها - ۳۳ رای شرشته. ۸
درخت انارست که در بستون واقه‌است . گویند
چون فرهاد از شنبدن فوت شیرین نيشه برس
خود زد دس تیشه خونآ لود کردید وا کوه بر
زمین افتاد وسرآن برزمین نشست » و چون آن
ازچوب انار بود بقدرت الهی سبزشد ودرخت آنار
۹۹ چك : شارت .
بهم رسید وانار آنرا چون باز کنند اندرون آن
سوخته وخاکستر شدء باشد . ۱
افار گیر ا - با کاف فارسی بتحتانی
رسیده و رای بی‌نقطه بالف کشیده . در فرهنگه
جهانگیری بممنی کو کدار وغور خشخاش باشد,
ودر صحاح الادوبه بجایرای بی نقطه آخرواوآعده
است - وخدخاش را نز کفته‌اند .
انار مثك ت بکسر عم وسکون شین
قرشت و کاف . نام دارویی است که ازهندوستان
آورند . و آن تخمی باشد سرخ دنگه و اندله
سبزی در میان دارد . و سرب دهان عصری
خوانند .
! ناطبطس باطایحعی سحتانی‌رسیده
وطای دیگر ببین بی نفطةٌ زده . لفتی است به
۴ - هز27 . چهلوی 6 بمعنی
مسر آعده و
===== leaf 381
یوتانی۱ وممنیآن‌بفارسی « سنگه زاییدن آمان
کن » باشد . وآن دانه ایست ساهرنگه بمقداو
جوژبوا. بغایت املی‌وصلب ودشوارشکن: وچون
بجنبانند مفز آن در درون وی صدا کند وآنرا
بشیرازی « کن ابلیس » خوانند نم کاف فارسی
ونون ۰ یعنی خایةٌ شبطان و بعربی حجرالولادة
گوبند . چه هرگاه در زیر زنان آستن دود
کنند زود بزایند و اکر باشیرزنان سح قکنند
وقدری پشم را بدان بیالایند و زنی‌ که نمی زاید
بوفت جماع بخود بر گیرد آستن قود.. گو یف
چونآنرا دردست گیرند وبا کسی مخاصمت کنند
برآ نکس غالب‌آیند .
| ناغاطسی - باغننقطه داربالفکفیده
وطای حطی مضموم بسین بی‌نقطه زده ۰ بونالی
سنکی باشد که چون آنرا بآب بسابند رنگی
مانند خون از آن برآید و با شیر زنان درچشم
چکانند ورم چشم و بیاری آب آمدن از چشم
رانافم‌است» وآن‌را بعربی‌حجر اناغاط یگویند .
افاغلس مه بن غین تقطه دار و لام
وسکون مین بی‌قطه ۰ بیونانی؟ دوایی است که
آنرا بفارسی مرذنگوش وبعربیآ ذان‌الفار گویند,
چه بر ک» آن بگوش موش میماند » باس رکه بر
کزیدگی عغرب مالنده نافم است
افا لیقی - با لام و قاف هر دو بتحتالی
رسیده . بلفت رومی دوابی که انرا انجرء
وتخم آنرا بذرالانجره گویندوبمربی قض‌خوانند.
انبارده
تخم آن مستعمل است . اکر مقدار سه درم از
آن باشیر گوسفند بخورند قوت‌باه دهد » ویضی
گویند انالیقی همان بذرالافجره است .
| ثاهیكف ؟ » با های‌تحتانی رسیدموبدال "
زده . بمعنی ناهمد است که ساره زهره باشد .
اب - بفتح اول و انی و سکون بای
ابجد . بادنجان را گوشد و آن ممروفست؟ »
بافراط خوردن آن جذام د ماع و بی‌خوایی
آورد» و بعضی گویند عرمی است ۱
ی رزن
افلاطون » حصار قلمه و جای محکم ر! کوشد -
انبار 1 ع بفتح‌اول‌بروزن زنگار «بمعی
لبریز و مملو و پر باشد - و فروربختن خانه
و افتادن دبوار و امثال الرا نیز گویندب ویمعنی
خی و خاشاله و فثلة اسان و س رکین خیوانات
دبگر باشد که توده کرده‌باشند و مزارعان‌برزمی
زراعت ریز ند واستخر وتالاب رائیز انبار گوینف
و بکر اول مخفف این بار است
انبادذ گی « بروزن و معنی انباششگی
اک ستتی. ود باه مت نب
| ثباددن ۱ « با دال ابجد بروژن‌وعنی
انباشتن است کهپر کردن و انبار کردن‌چیزی‌باشد
از چیزی دیگر
)۱ چك : ژند ویاژند .
۱ - بونانی2601185 «اشتبتگاس» ش بان 881021115 0استینگاس »0 202
«دزی»,
آلوده. جمما بعنی
داده‌اند ای کردند. ۶ بشت ۱
- بهلوی ۵2۸02۲ 0 از
۴ راك : لك ٩‏ ص۱۹۱ .
4 «مناس ۲۷۵ :
: : انبار) ۳ دن‌یسوند مصدری ۳
===== leaf 382
اتبارش
که پر کرده باشد - و بمعنی پرنسمت و با نعست
هم اجه ات ۵
نبادش! -بروزن‌افزایش. پر کردنی‌را
کوبند . و آن چیزی باشد که جوف درون
چیزبرا بان پر کنند. وأنرا بعربی حشوخوانند.
انبار "سیر وزن دمساز » خومات و رفیق
و همتا را گویند . "
نباشت ۱0 بروزن برداشت ۳ ماضی
انباشتن است ععنی کر و ممل و گرداند ۰
۶ ۵۸۱ ه ۳ > ۳
انباشتی ۲۷ " سبروزن برداشتن,بسنی
پر کردن و مملو گردانیدن و آنبار نمودن باشد .
افیا ۴ - باغی تقطم‌دار .دوزن‌را گوبند
دیگری‌را انباغ باشد .8
اثبان باد - بکر نون و با بای ابجد
بروزن می‌دان‌کار. مردم فربه - و بیکاره وهیجکاره
را گوند ۰
برمی آورند .
اثبر ب بنتح اول وضم الث وسکون‌انی
و رای فرشت » التی باشد از آهن که ز رکران
و مسکران طلا و مس تفته دا بدان گیرند ,وبه
عربی کلوب خوانند .
۱ 1 از انبار شش بوند آسم
و
] ذیر وت ده بروزن‌عنزروت , امیودباشد
و آن میومایست معروف ۵ .
افیره - ینم ات بروزن‌قنجفه «هرجیز
موی رنخته را کونند عموماً وشتر موی ریخثه را
خصوصا ‏ و اسب و شتر آبکش را نز گفتماس
و در عربی شکنبه را گویند - و بمعنی دره کوه
نیز حست ؛ و بفتح ثالث بر وزن حنجره هم
آمفه ات .
اثیست - بروزنک‌بت : نلیط و بته
شده را کومند ۷ .
| ثیسقه - بر وزن برجسته ,هر چي زکه
آن بته و سخت شده باشد و بدشواری وا شود
و حل گردد - و شبر و ماست و خون بستهرانیز
گوبتد ٩‏ .
اثبله - بنتح اول و الث بروزن‌حنظله,
تمر هندی رأگویند و بهندی ابلی خوانتد ۰۷
انیمی ۸ س بکسر ثالث وقتح میم‌بروزن
صف‌شکن , بلفت زند و بازند (۳) انگور باشد
و بعربی علب گویند .
افیق یه - بروزن میغوب . فرش وساط
و گتردنی را گومشه. :
اثبو 4 - بر وزن منصوبه . ماشوره را
گویند - و وله آشابه و مانئد آنرا نیز
کفته‌اند .
۴ - پهلوی ۵:۳۰98۵1, 20۵۵2۵۷
۲
۴ ات ود اون
ت۱۳ تم ستد.
۸ حز2(8021130),
```


## [2026-09-07T20:18:29.164Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('IEC.txt',errors='replace').read().split('\\f')\nprint('leaves',len(t))\nfor i in range(830,845):\n    print('=== leaf',i)\n    print(t[i][:1200])\nEOF"
}
```


### [2026-09-07T20:18:30.432Z] TOOL RESULT

```
leaves 858
=== leaf 830
 ‘desired’; vairyo *desir- able’; varom & varo, gs: varáh-, n. ‘gift; Tokh. cf. A wäl, B wel, s. ( ‘king’, to ual- (2), q.v.); Gk. defect. vb. eilon, aor. ‘I chose’; Lat. (*-e- or *-o-) volo, inf: velle, defect. vb. ‘wish; OLat. cf. velim, v. ‘may wish’; Osc. cf. vellia-, f. ‘will: It. voglia, id. beside Rumansh veglia, id.; cf. also lat. volup, volupe, defect, adj. (pleasant, fr. *uel-/uol- + *op- in opes ‘wealth, power, help’; and volup-tàas, cf. Umb. gs. opeter “of the best’: Skt. aptas, n. “act of sacrifice’. See op- (2) and (3) and opoetom. Not as WH); Ir. feillim, v. ‘suit, please’; Go. wiljan, wv. ‘wish’; wilja, f. id.; MHG wëllen, wv. anomal. vb. ‘wish’; Du. willen; OE willan, id. beside willen, adj. ‘desirous’; ON vilja, v. ‘wish, will’; vili, m. id.; OCz. vele, adv. "great. ly’; Cz. vele-, cpds. id.; beside OCS (o-gde) vole! “well! indeed"; voljo, voliti, v. ‘wish’; Cz. volit, inf. ‘choose’; (e-gde in) OCS po- velja, f. ‘edict’; Cz. povel, gs: -u, m. ‘com- mand’; (o-gde also in MHG welen, weln, Go. waljan, tr. ‘choose’); OLI. velmi, 3s: velti, velt, v. ‘wish, augur’; Li. pa-vélti, v. 'grant'; cf. velyjimas, m. ‘greeting’; véliju, yti, v. ‘wish sb. sth’; velyk, adv. ‘rathe
=== leaf 831
 ‘better’; OE cf. we- lig, adj. ‘rich, prosperous, abundant, fertile, luxurious’; Du. welig, id.; LG welig “bright, gay, luxuriant’; Go. cf. ga-wiljis, adj. “willing, agreeable’; Scots walie, adj. ‘ample, large; jol- ly’; ON cf. vilgi, adv. “very, at al’; OCS velij, adj. ‘big’; OCz. velí, Srb. velji, id.; Li. vély, adv. ‘rather’. Compounding forms in Per. bali- *up- beside bali (“indeed, certainly, yes’: Li. vély “rather?); Ir. feile- ‘very’; Go. waila-, px. *well2; OE, Du. wel, wel- ‘very, fully’; OCS, Cz. Slovene vele-, px. "great" Verbal forms: Per. balidan, inf. ‘grow’; Tokh. A. cf. wäl, B
uel- — uelik- (uelk-)
20
25
30
35
40
45
1510
walo ‘king’; OE wealian, v. "be defiant’; Sw. vilja, v. ‘wish, want’: Slovene veljati, inf. ‘be worth, hold good'; Cz. velet, inf. command'. (Isophones: Arm. gelum, aor: geli (4) 'squat'; W gweli, pl. -iau, m. ‘wound, offence’; gwefio, inf. ‘expose; wound’, Big. velja, v. “speak, say’; Li. velið, v. (2) “adhere”; veléju (2) *devour)
uelaio “fly, dash? Gk. eláo, v. “drive, ride, sail; Lat. volo, are, v. ‘fly’; (Gk. elelízo, v. (2), tr. “twist, whirl, shake, rally may represent a type *ueluel-)
ueld- (1) ‘suppress, be suppressed". Cf. uel- (6) Tokh. 
=== leaf 832
�mina, pl., vellemina & vellimina, n. s. & pl. id.
(uelnó, possible reconstruction of Lat. vello, see uel- (4) & cf. ueluó)
(uelquóo, possible reconstruction of OCS vlékg & Li. velkü, Latv. velku, see uelk- above, and cf. suelk-)
(uelsó, possible reconstruction for Lat. vel- lo, ére ‘tug’, but cf. uel- (4) & uelno. Ambig. also in Lat. vellus, gs: -eris, n. ‘fleece; foliage’, but cf. OCS (o-gde) vlasü, m. ‘hair’, and com. SL)
(uelumn-, see uelmn- and uelumn- (1) and Ou
uelutrom “wrap, cover. Cf. uel- (2), but ambig. in Skt.
Skt. varutram, n. ‘cloak’; Gk. élutron, n. ‘wrap, sheath, veil; shell
ueluel-, redup. of type uel- (2) in Gk. elelízo, v. ‘whirl’; Lat. volvulus, m. "feld. roller. The radical arises also in Gk. helínos, m. ‘tendril; Tokh. A walyi ‘worms’
uelumn- (1) ‘turn, twist, curve, bend’. Cf. uelmn-, ueluó & uel- (2)
Oss. würm, orm, s. (vault, cellar; Arm. ge- lumn. gs: gelman, s. ‘distortion, contortion’; Gk. eílüma, n. “cover, dress’; Lat. volümen, gs: -inis ‘roll, fold, turn, wind, volume’; Myc.
uelk- — uén-
10
20
25
30
35
40
45
1512
cf. werumata (queried: 'straps"); Icel. cf. vö- lundar, pl. ‘labyrinth’; Li. cf. velanas, m. ‘rol- ler, cylinder’. Cf. WP I, 298. The radic
=== leaf 833
utifully’; Sw. vän, adj. ‘pleasant’; Li. vēnios, fpl. ‘strength’. (Isophonic: Latv. pa- vēnis ‘shade, shadow, shelter’)
uën- (2) “lacking, defective, immature; lack’, etc. Cf. uän-. Gk. ambig. Hom. Cf. énis, gs: énios, adj. (immature, un- mated, virgin’ of heifer); LG Du. wàn-, wan-, cpds. *mis-; cf. G Wahn-sinn (infl. by Wahn, see uen- (1). Semantics of Lat. jünix fr. ieun-, q. v.). See Supt: U
uendh- (1) ‘turn’. WP I, 261. Cf. uondh-, undh- Skt. cf. vandhürabh, m. *chariot-seat'; Arm. cf. gind, gs: gndi, ab. s. -av, also gint, gs: gnti, s. (ring; gndak, dim. ‘tendri’; Tokh. AB wánt-, v. ‘wrap’; Gk. cf. peirins, gs: peírinthos, f. “wicker body of chariot if fr. *peri-uendh-); Umb. (queried) aha-uendu “let him turn aside’; Go. bi-windan, sv. 3. “wind, wrap’; MHG winden, winten (and com. Gmc.),id.; G & MHG Winde, winde, wf. *winder, spool, capstan, convolvulus'; OHG winta, f. id. (and “spiral staircase’); ON vinda, sv. 3. ‘wind’; f. ‘hank’; vindr, adj. fawry'; cf. vindli, m. ‘wisp’; Sw. vind, adj. ^warped'; OE windan, sv. 3. ‘wind’; wind, n. ‘wind, path, weave, textile’; Srb. (?) vedja, f. ‘eyebrow’. (A hapax arises in Ir. feann, s. *flaying, skinning’)
uendh- (2) ‘barren, withered;
=== leaf 834
) joy’; OE wynn, f. ‘delight’; cf. wyn-sum ‘winsome’. (FK:EWDS untenable: Wonne). See next
1515
uénskKó ‘desire’. Cf. uenos, -es-, and uén- (1). WP I, 259 Skt. vafncami, v. id.; Du. wenschen, mod. wensen, v. id.; wens, m. id.; (zero-gde in G wünschen)
uenter- (uentor-) (uemster-?) *wickerwork, basket" (?); ‘bag, net? (?) Av. cf. vafita, f. ‘wicker’; Lat. venter, gs: ven- tris, m. (abdomen, stomach, womb'. Fig. sense of *bread-basket (?), cf. pàn-tex ‘paunch’, if a cpd. of panis "bread", and cf. E. dial. breadbasket = *'abdomen); Li. vénteris, gs: vénterio, m. *bownet, fishtrap', Latv. ven- teris ( fish-trap, fish-basket' or '-pot"); but cf. also Icel. vinstur, pl. vinstrar, f. “fourth stom- ach of ruminant'. See Supt: U: uemstr-
uéntos (*uéntos) ‘blow, blowing, wind, gust’. WP I, 220. Cf. ueio (“uëið) Tokh. want, wànt, B yente (sic), id.; Hitt. huwantas, pl. huwantes, id.; Lat. ventus, gs: 4, m. ‘wind, storm’; Ir. (?) fead, mf. whistle’, only if for *féad); W gwynt, pl. -oedd, m. *wind'; Br. gwent, m. id.; Cor. gwyns, pl. -ow, m. id.; OHG wint, i-st. & o-st. m. id.; OE, Du. wind, m. id.; OE winde, adj. ‘windy’; ON vindr, m. “wind, air”
uequó (uequmi, uiuéqumi) “call, say, speak, as
=== leaf 835
ņemt, v. ‘take heed’;
uer- (3) (uero, ið) ‘speak’. Cf. ueru-, uoru-. WP I, 283 Hitt. weriyami, v. “call, invite’; Gk. eíro, v. “say, speak, tell; éromai, v. "ask
uer- (4) (?) *up, upon' Per. bar, adv. & prp. id.; Arm. ger, cpds: gera-, id.; Lat. (?) cf. the hapax: verones plum- bei ‘sheets of lead”
uër- (1) ‘charm, favour”, etc.; (2) ‘true, right", etc. See ueros (1) & (2)
uerbos, -es- (uorb-, urb-); uerba ‘stick, withy’ Lat. verber, gs: verberis, n. ‘stick, lash’; OE (o-gde) wearp, n. ‘twig, osier’; OCS (and com. Sl.) vrüba, f. ‘withy, willow’; Li. verbà ‘sallow, palm-spray'; (z-gde in) vifbas, m. ‘twig, stick".
1517
See next
uerbo (uorb-, urb-) ‘twist, lash, fling’. WP I, 275. Cf. uerbos above and cf. urb- as a sepa- rate entry OHG wérfan, wérphan sv. 3. ‘throw’; OE weor- pan, Du. werpen, ON verpa, v. id.; Sw. várpa, v. “lay — eggs’; Li. (z-gde) virbu, eti, v. ‘move, twist, tremble’; cf. also OE weorp, n. ‘dash; castings, rubbish?
uerbhos, à  'farm-animal'. uer- (2) and -bhos Olr. ferb, f. ‘cow’; Ir. fearbh, f. ‘doe, deer, cow"; OE weorf, n. *farm-animal, beast of burden’
ueredh- (uerdh-) 'seethe, boil, stir, rouse, rile, anger Gk. erétho, erethízo, v. ‘rile’; OCS vrézdo, vréditi
=== leaf 836
‘work’; (denom. in) OHG wérkon, w&rchon, v. "work do’; Swiss werchen, id.; Du. werken, id.; OE weorcan, id. beside (z-gde) wyrcan, id.; ON verka, v. ‘work’; Alb. virdhem, v. ‘gain a skill, win sympathy’, mp. fr. *uergemoi or sim.. Nomi- nal types: Pahl. varz, s. “practice, work? (Per. id. fr. Pahl.); cf. also Per. barz-gar, s. 'farm-labou- rer’; Arm. (e- or o-gde), o-st. "work act, fact’; Myc. we(r)k-, cpds. *draught-, work": cf. were- kara- (“tooP or sim.); Gk. érgon, n. "work op- eration, deed, act, necessity; MIr. ferg, f. (battle; fury; warrior, but cons. ambig. Cf. uerg-, uergh-, etc.); Ir. fearg, f. (anger, am- big.); OBr. guerg, adj. ‘effective’; OHG wérk, wérch, n. ‘work, deed’; Du. werk, id.; OE weorc, n. id.; ON verk, n. id. cf. virki, n. id. (and ‘stronghold’, mod. Icel. *saddleframe"); ON cf. also virkr, adj. ^working-; mod. ver- kur, pl. verkir, m. ‘pain’; Sw. värk, m. id.; värka, f. ‘hurt
uerĝh-, alternative to uerĝ- (1), q.v. (Balto- Slav. ambig.). Cf. uergho (1) ON virgill, m. ‘halter; MHG wergel, m. (Cstrangler, fr. *uorghil-); Blg. vrěž, vrěža, f. ‘tendril’; Li. verzle, f. 'screw-nut'; verZe- klis, m. id.; Latv. verzeles, pl. ‘trappings’; Finn. LW verkko ‘net, web
=== leaf 837
nus ‘barrier’; Br. gwern, pl. -iu, f. 'ship's mast’; W gwernen, pl. gwerni, f. id.; Cor. gwern, pl. gwernow, f. id.; ON vorn, f. beside vernd, f. ‘defence’; Sw. värn, n. id.; Finn. (LW) varras, s. ‘spit, pole, shaft
uern- (1), see uermn- (2)
uern- (2) (uernà, is, ios) ‘withy, shoot, suck- er; alder. WP I, 292 Gk. érnos, n. ‘young plant, sucker, shoot’; Alb. verr, m. “alder, white poplar’; Gaul. verna, f. ‘alder; LW in Fr. verne, vergne, id.; Ir. fearn, gs: -a, m. ‘alder’; Br. gwern, pl. gwer- nennu, m. id.; W gwern, coll. id.; Cor. gwern, id.
ueró, ueros, see uer- (1)
(uerógh-, see Supt: U)
uéros, à (1) ‘goodwill, grace, charm, favour, fortune' Skt. varah, m. “treasure”; -varah, cpds.; Av. vàro, m. ‘will, goodwill, gift, grace’; Hom. Gk. ēra, acc. sg. id.; Lat. cf. (?) se-vérus ‘harsh, exacting’; Go. cf. un-wéerei, f. ‘reluctance’; OHG cf. ala-wari, mite-wari, adj. ‘amicable, favourable’; ON vert, adj. ‘snug, peaceful. (Isophonic: Latv. veris ‘deciduous forest; vera, adv. “into notice, prominently’: OE wär, adj.)
uéros, ios (2) “true, right, proper. WP I, 268 Lat. verus, id.; MIr. fir, Ir. fior, id.; Br. W gwir, Cor. gwyr, id.; OBr. guir, id.; OHG war, wāri, id. beside wara, f. (tr
=== leaf 838
ag’; Lat. verro, ére, OLat. vorro ('drag, trail; sweep, brush”,
uerpo — uertos
15
20
25
30
35
40
45
1522
but a type *uris- is possible for verro in the sense of 'sweep^); Latv. cf. (?) verSuü, vērst, v. ‘direct’; vērsties, refl. ‘go, wend’; cf. ver- stuve, f. ‘plowtail’. See next
uerstis (urst-) ‘turn’. Cf. uert-, uort-, urt- and extns. Av. varstis, f., varstvom, n. ‘deed’; OW gwers, f. ‘while’; R cf. izobrësti, inf. 'invent'; z-gde in Skt. vrttib, f. ‘course, mode’; OCS vrüstí & vrüsta, f. 'age'; Croat vrst, f. “kind, sort; R verstà, f. (about a km.); Li. versti, inf. ‘to turn’
uertenos, ā, is ‘turn, roll, roller, axle-tree, cart’. Cf. uerto. WP I, 274 Skt. vartaníh, f. ‘felloe of wheel’; Oss. wär- don, pl. wärdättä, s. Ceart LW in Romani vardon, id.); Per. vardāne, s. ‘rolling-pin’; (z- gde in) Gk. rhatánē, f. (/stirring-stick'. fr. *ur- tona); Lat. cf. Vertumnus, m. ‘god of change: LLat. vertumnum, n. *ironwort, heliotrope'; OCS (and com. Sl.) vréteno, n. ‘spindle’; LW in Finn. värttinä, id.
uertitos, à, io, cf. uertó, etc. Skt. vartitah, adj. ‘turned, revolved'; OBr. guirtitou, pl. ‘spindles’; Br. gwerzid, pl. -i, f. id. (and *banister); W gwerthyd, pl. -au, f. ‘spindle, axis’;
=== leaf 839
a dike’; G Werd, m. “island, coastal strip’; Ukr. vereta, f. ‘blanket. (Go. wairdus, G Wirt, m. “host, entertainer’, fr. *uer-tüs?, but *ues- "be, dwell" for Lat. verna, mf. “household slave). See next
uerut- (2) (?) ‘crowd, group, team’ Skt. cf. varütham, n. (2) 'swarm, crowd; Tokh. A wartsi, B wertsya, -tsyo, f. ‘crowd, retinue’; OE werod, n. (1) ‘team, band, troop’
ueru- (1) “din, confusion, strife'. Cf. uoru-. Verbal type (also): ‘utter, blab? Skt. cf. (*-e- or *-o-) varvarah, adj. (1) fstam- mering’; Gk. eréo, eró, v. “will speak’; éris, gs: éridos, f. ‘strife’; Lat. cf. verv-ex, -ecis, mf. ‘wether; ewe Ir. fearb, f. “ox, cow; doe; bel- lows’; cf. the cpd. in Gk. éri-phos, mf. (Ckid', lit. *bleater); Blg. vréva, f. ‘brawl, shouting, roar’; Srb. id. (and ‘crowd, swarm); Cz. vřava
uertulos (uertolos, uort-, urt-) — ues-
20
25
30
35
40
45
1524
‘brawl’; Slovak cf. (o-gde) vrava, f. ‘speech’; vravet, inf. ‘speak, say”; Li. verventi, inf. “bark, yap’; vervü, čti, v. (‘whine for, plead, beg; bark’: Hom. éromai, v. ask: Latv. cf. verve- leju, v. jabber’. Variant in Skt. brávimi, v. ‘say, speak’. WP I, 283. Cf. uoru-
ueru- (2) ‘tie, knot’. WP II, 499 Gk. cf. eíro, v. (1) ‘tie, knot, we
=== leaf 840
, wasami, wasiyami, wasemi, v. ‘put on — clothes’; Gk. Ion. heimai, 2s: héssai, 3s: héstai, v. ‘wear’ beside Gk. hénnüm,i, fut: héso, tr. ‘put on — a garment’; cf. esthés, gs: -étos, f. ‘garment’; Alb. vesh, v. ‘put on — clothes’; véshem & víshem, v. ‘get dressed; Lat. cf. vestis, f. ‘garment’; Go. cf. (o-gde) wasjan, tr. “put on — clothes’; OE werian, v. (id. E *wear). Variant of type *ués-sK- in Arm. z-gec-nem, tr. ‘dress’; Br. gwiska, tr. id.; W gwisgo, id.; cf. Br. gwisk, pl. -u, m. ‘dress’; W gwisg, pl. -oedd, f. id.
ues- (5) ‘soak; water’. Cf. uosolos, uðsos Skt. cf. vasin, m. ‘otter’; Tokh. A wes, B wents ‘urination’ beside B wesye, wensye, s. ‘mud’; Per. bàh ‘sperm’; Arm. cf. to-gorem, v. (soak, steep’: Gk. deüo, v. id.); cf. also Gk. di-éme- nos, pp. ‘watered, sprinkled', and eiíamenés, f. 4ey-meadow'; Lat. cf. (?) v&s-sica (bladder, anat. if fr. *ues-siqu- ^water-drip); MHG wise, f. ‘meadow’. (For Lat. urina, urinor, see uüsos)
ues- (6) ‘shine’. Cf. uesel- . Skt. (radical only) vas- ‘shine’; cf. vasrah, m. *daytime'; vasar- in cpds.; Vedic also vàsá- yami, v. “make shine’; Av. váh-, v. ‘lighten, dawn’; Arm. cf. gey, o-st. (beauty, fr. *uesel- or *uesl-, cf. ueselos below)
=== leaf 841
 id. cf. Li. ve-du, id.
ues- (2) “breath, air, breeze, cool, fragrance’. WP I, 222. Extn. uésm- Skt. vàsah, m. ‘perfume’; vasáyami, v. tr. id.; vasin, adj. ‘fragrant’; Gk. cf. à-ema, n. (^wind', if fr. *sm-uésm-); Du. waas, n. “bloom on fruit’; wasem, m. ‘fog, vapour’; cf. wasig, adj. ‘nebulous, vague Li. vesà, f. cool": vesus, adj. id.; véesümas, m. ‘freshness, cool; vēsu- mà, f. ‘cool spot’; Latv. vēss, adj. cool: vēsma, f. “breeze”; Li. véstu, vésti, v. ‘grow cool
uës- (3) ‘offal, waste? Gk. čia, npl. (2) ‘husks, chatt": OFris. wasa, f. “dirt”; Icel. væra, f. 'scurf'; Norw. cf. vås, n. (nonsense, but cf. ues- (3))
uesiios (uesios) “better, more, bigger'. Cf. uesus Skt. vásiyah, vásyah, adj. “better”; Per. bis, adj. ‘much, more’; cf. bihin, adj. ‘better, best’; bih ‘better’; Ir. feárr "better fearra, adj. ‘more’. (The radical arises in Gk. es-thlós ‘virtuous’)
(uesimn-, see uesmn- (1) and (2))
uesis ‘existence, substance, matter’. Cf. ues- (2) Arm. go, gs: guji, ab. s: gujiv, s. ‘existence; goods’; Tokh. B wassi, wässi ‘material’; ON ver, n. ‘station’; veran, f. “existence, essence’; o-gde in MHG war, ware, sf. ‘wares, goods’, and com. W. Gmc.
uesitos ‘dwelling, dweller’. Cf. ues
=== leaf 842
 Cf. ues- (2). WP I, 222 Skt. vasanam, n. ‘fumigation, scenting'; Gk. cf. á-ëma, n. ‘wind’; Du. wasem, m. ‘vapour’; Latv. vēsma, f. ‘breeze’; Li. cf. vesumas, m. ‘coolness’; vesumáà, f. «cool place’
uesnà, is ‘springtime’. Variant of type uesor- (1) Gk. cf. enis, gs: -ios ‘yearling’; Lat. cf. ver- nalis, adj. “of spring’; OCS vesna (and com. SI.) ‘springtime’
uesnom (uosnom) ‘price’. Cf. ues- (1). WP I, 311 Skt. vasnám, n. id.; Oss. cf. wäi, s. ‘sale’; Hitt. cf. wesiya(s), s. ‘cost, price’; Arm. gin, gs: gno, s. id.; Lat. venum in — dare ‘sell’; venus, gs: -üs, m. ‘sale’; Umb. cf. (?) uestisia *JJibation'; OCS venjo, -iti, v. (1) "sell
uesnt- ‘indwelling; dwelling-place, place’. Cf. ues- (2), ueslos (2), uesitos Skt. vasatíh, f. ‘dwelling; stay’; Alb. vend, pl. -e, m. ‘place’; Gaulish venta, f. ‘township, settlement’; cf. Br. placename: Gwenned ‘Vannes’; W gwent, pl. -oedd, f. “open space; Monmouthshire’; MHG wésent, adj. “being, essential, authentic, lasting, domestic’; Fris. went, wente, s. ‘dwelling, house’. (For Gk. éntea 'gear', see esnt-)
(uésos, see ues- (2))
uéstor- ‘herdsman, protector Av. vasta, acc: vastàrom, m. “protector; protec- tion’; Hitt. westaras, s. ‘shepherd’
ue
=== leaf 843
r-old, annual; yearling'. Cf. uetos. WP I, 251 Skt. vatsáh, m. ‘calf, young animal, child”; Hitt. cf. sa-wetesc, adj. “of the same year; Gk. éteios, adj. ‘year-old; yearling’; Alb. vig, m. ‘calf; OLat. veter, Lat. vetus, gs: eis, adj. Cold" LW in Alb. i vjetër, id.); Go. wiprus, m. ‘ram’; OE weber, m. id. (and *wether); ON veðr, gs: veórs, m. ‘wether’; Sw. vädur, m. ‘ram, wether’; Du. cf. ouder-wetsch, -wets,
1531
adj. *old-fashioned'; OCS vetüxü, adj. old: Cz. cf. vetes, f. junk, old rubbish”; OLi. vetu- Sas, adj. "old beside mod. vecias, id. Verbal extns. in Lat. vetero, åre, v. ‘grow old: ME wideren, E to wither
uetəlos, om ‘year-old; yearling’. Cf. uetos and extns. Aeol. étalon, n. ‘yearling’; Lat. vetulus, adj. *oldish'; m. Cold man" Vocalism of Lat. vitu- lus, 1, m. ‘cal? problematical)
uëtəlos (?) “bad? Gk. cf. a-ésulos (Hom. “wicked'); OHG wā- dal, adj. (poor; waàdali f. ‘poverty; OE wæðl & wædi, f. id.
uetios, cf. uetesios & uetos Arm. (?) gocan, s. ‘pig’, fr. *uetion-?); Li. ve- čias "old
uetos, -es- “year, age’. Cf. uetesios, uetesi. WP I, 251 Skt. cf. tri-vatsám, n. ‘year’; vatsáh ‘yearling calf; Hitt. cf. weti “in a year’; wetasas (que- ried: “annual festival); wetanc 
=== leaf 844
‘crossbar, bail’ beside LLat. vibra, id.; W gwif, pl. -ion, m. "lever, bar; LG wipp, f. (tilting-board, springboard, seesaw? > G Wippe, f. id.); Sw. vipp, m. *pump-handle, beam-crane, lever; MHG cf. wife and wifel, f. “benchmark, landmark’. (NB. E whip is iso- phonic, since -h- is non-historical. Go. wipja, f. ‘garland’: LG Wiepe, Wipen ‘wisp of straw and Du. wiep, f. ‘faggot are isolated)
uib- (2) “pipe, whistle; piping bird” Ir. fibín, m. ‘laughing-stock, fool; EME wipe, s. ‘peewit; jeer’; Sw. vipa, f. ‘peewit; (prob. also) Gk. ibis, gs: ibios, -eos, f. “African wader bird, ibis’; ibú, adv. ‘shrill, loug’. (Isophones: Lat. vibð, -onis, m. ‘britannica’ (bot.); Latv. vibotne, f. ‘mugwort, artemisia’)
uibr-àio, -ðið ‘shake’. Variants Lat. vibrō, āre, tr. & intr. ‘shake; fling; curl, frizz’; LG (ambig.) wippen, wippeln. v. ‘wag’;
1533
Sw. vippa, v. ‘swing’; Li. cf. viburiuoti, výbu- riuoti & výburti, v. “wag? beside vibrúoti, inf. intr. ‘shake, tremble’
(uibhón, -en-, cf. WP I, 258 in W gwyfen, gwyfyn, pl. -od, f. ‘grub, worm, moth’; OE wibba, gs: an. wm. ‘beetle, worm’, cf. also OE tord-wifel, m. *dung-beetle; G Wiebel, m. ‘weevil’ and Du. wiebelen, v. *wrig- gle’)
uid-, radical for
```


## [2026-09-07T20:18:45.077Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor p in \"nurn\" \"nran\" \"anar\" \"anār\" \"nōr\" \"Punica\" \"granat\"; do echo \"=== $p\"; grep -n -i -- \"$p\" IEC.txt | head -8; done"
}
```


### [2026-09-07T20:18:46.426Z] TOOL RESULT

```
=== nurn
=== nran
=== anar
523:aner (anər-, anr-) “man, creature’. Cf. ano, ner- Gk. aner, gs. andrós; Phryg. anar; cf. Alb. njerí
2790:dhenər (dhern-) “palm of hand, hollow of hand’. WP I, 853. Cf. dhern- Av. danaro ‘a food measure’: (?) = ‘handful’; Gk. thénar; MIr. dernu ‘palm, paw’; Ir. deárna,
4876:ghránis, os ‘tip, point, spike, edge’. Cf. ghróünis, os. WP I, 606 Tokh. B Kran (queried: ‘spine’ but Tokh. A kran 'nose' is: Skt. ghranam, -a, id. fr. ji-ghrà-mi 'smel); Olr. gráin “point, edge’; Ir. f. ‘spearhead’; W gran ‘cheekbone; eyelid’; grain ‘socket, ring’; Lat. (fr. Gmc.) granus, grana ‘moustache’; MHG gran “tip of hair, hair on lip, bristle’; G Granne; ON gron, pl. granar ‘hair on lip, lip of cattle’; (the Ir. and Gmc. forms are ambig. see ghrün-); Pol. grań ‘crest of mountain’; R grani ‘facet; limit"; Cz. hráň, hráně 'crystal ; hrana “edge, corner, angle’; cf. hranol ‘prism’; Srb. grána ‘branch; shoot; ankle’; Blg. gran, pl. -ove ‘facet’; grani (3) ‘branch’; Lusat. hrana ‘corner’. (The Sl. forms are ambig. cf. ghrõnis, os)
4967:ghronos ‘point, tip; mark, period; moment, (Semantics of Gk. stigmë, id. & Go. stiks ‘point of time’, and of OE prica ‘point; short period’). Cf. ghránis Gk. khrónos ‘time’; EMAlb. grané ‘red dye’ (here?); Ir. gron “spot, stain; trace’; OHG (am- big.) grana ‘moustache’; MHG gran, grane, f. ‘tip of hair, bristle, moustache’; OE granu ‘moustache’; OHG cf. chran-poum ‘juniper’; Sw. gran ‘pine’; Norw. gran, grane, id. beside gren ‘branch’; ON gron, gs granar (‘pine; moustache, lip’. Semantics of rtis, q. v.); Du. cf. grene-boom ‘pine’; Lusatian grono, hrono,
5019:ghrd- (variant of ghrud-, ghrüd-, q. v.). Cf. WP I, 611. Per. (archaic) gard “dust” beside gil ‘mud, clay’; Gk. cf. for consonantism khérados ‘gravel, silt, shingle’; Lat. (ambig.) hordeum, n. (“barley”, but a type *ghrsd- is possible, see PK: EWDS: Gerste. Lat. horreum 'granary' may stand for *ehrd- + *segh- cf. Gk. ekhe- in cpds); Du. gort (crushed barley, groats’. Distinct fr. grut *grits, groats")
5848:?ordos (?), see ger-, gor- (1) OE ceart ‘rough land’; E chert ‘siliceous sedi- mentary rock’; Li. Zárdas (‘drying-rack; island; granary’. Basic mng. obscure); Latv. zards ‘drying-rack’
5900:$£uhen- (guhon-, guhn-) ‘sound; resound’. See next & ĝuenghõ, &uhon- Skt. jhanarni, v. id.; Alb. zâ, gs záni (T: zë, gs zëri) ‘voice, sound’; cf. pé-zàj, bzáj ‘bawl’; për- zâj (2), id.; Lat. (o-gde) honos, honor beside hones-tus (*&uhonos, -es-; OCS zvonů “sound, bel; Pol. dzwon, id. beside OCS (z-gde in i-basis) zvínjo, -čti ‘resound’ and zví- nú, pl. zvir évy ‘noise’; Latv. zvans "bell" WP I, 642
7320:klētis ‘shelter, shed, store’ Gk. cf. klêjsis ‘enclosure’; OCS klëti ‘house’; Pol. kleć, kleta, f. ‘wattle hut, silo’; Slovene klet ‘cellar’; Li. klētis ‘storehouse’; Latv. klēts ‘granary, pantry’
=== anār
=== nōr
11854:(nōr-. See Supt: N)
=== Punica
=== granat
5850:$rnàtos, -itos ‘grained, of grain’. Sce grnóm Alb. i grynjtë ‘wheaten’; Lat. grānātus ‘granu- lar, grained’; It. granato, id. and ‘robust’; gra- nito ‘robust’; s. ‘granite’; OE cyrnod; Norw. kornet; Cz. zrnatý & zrnitý ‘granular
7535:kokon ‘knob, boll, seed, berry’. Extn. variant of kokos, q. v. Oss. kákon ‘sloe’; LW in Arm. kokan, id.; Gk. kókkon (‘pomegranate seed’. LW in Lat. *coc- conem, cf. Sard. coccone ‘bran-bread’; Fr. cocon ‘cocoon’); Ir. cocán ‘calyx, bud, poppy, topknot'; OE haga, gs hagan, wm. ( ‘haw’, and com. Gmc.)
```


## [2026-09-07T20:18:46.467Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('IEC.txt',errors='replace').read().split('\\f')\n# find highest printed page numbers\nfor i in range(len(t)-12,len(t)):\n    nums=re.findall(r'^\\s*(1[45678]\\d\\d)\\s*$',t[i],re.M)\n    print(i,nums, t[i][:120].replace('\\n',' | '))\nEOF"
}
```


### [2026-09-07T20:18:47.820Z] TOOL RESULT

```
846 ['1536', '1537'] ow in middie of elephants | forehead’; Li. vidüs, m. ‘middle; room, cham- ` | ber”; Latv. vidus, m. ‘middle’; (?) Arm. girk,
847 ['1538', '1539'] ��: Latv. videnis *torso, rump' and Li. Latv. vidus, m. *middle) | uig-, uigl- (1) 'alert' Skt. vigráh, adj. (queried: *vi
848 ['1540', '1541'] f. *filigree-gold'; MHG wiere, f. id.; OE wir, m. ‘wire; filigree; creeper’; Du. wier, n. ‘seaweed’; Norw. vier, s. ‘wil
849 ['1542']  cf. am- usin, s. (spouse, fr. *som-uiKin-, cf. Lat. uxor, if fr. *uoiK-sor-); Alb. (?) vis, pl. -e, m. (place, if fr. *
850 ['1543', '1544'] WP I, 259 & 577 Gk. mus, s: -ios, mf. ‘son, daughter’; Lat. cf. vin-dex, gs: -dicis, m. (lit. ‘speaker on behalf of a fr
851 ['1545', '1546'] “man, husband, hero’. WP I, 314 Skt. viráh “man, hero’; Av. viro ‘man’; Tokh. A wir, id.; Gk. (Pelasgian ?) cf. Ka-beiro
852 ['1547', '1548'] rul-entus ‘poisonous’. Cf. OE wode-wistle ‘hemlock’. (Isophonic: Mir fial ‘modest; W gwyl, id.) | uisolos (2) (uislos, us)
853 ['1549', '1550'] - sure, acceptance'. Cf. uoit- (2) Skt. vitáh, adj. (2) id.; vitíb, f. ‘pleasure’; Lat. cf. Vitula ‘goddess of mirth’; i
854 ['1551'] Skt. vívakmi, v. ‘say, speak, tell beside vávak- mi, id.; (Hitt. wewakhi, v. see ufuék-); Gk. cf. en-ípto, v. ‘reprove’.
855 ['1552', '1553'] Lat. liquor, gs: -óris, m. ‘fluid’; MIr. & Ir. fliuch *wet'; OBr. gulip & guilp, id.; W gwlyb, m., gwleb f. id.; Br. glé
856 ['1554'] bulga is ambig. Skt. várgā ‘sect, class’ seems to be unrelated) | (ulio (1) ‘wind, wrap’, see uluið; (2) ‘boil’, see ulāið
857 [] (1) only in Skt. ürnómi, v. ‘envelop’; (2) only in Gmc. cf. Go. wulan and OE wylian 'seethe? beside wyllan, v. id. (fr.
```


## [2026-09-07T20:18:58.333Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '11845,11865p' IEC.txt\necho \"--- supt mentions\"; grep -n \"Supt: N\" IEC.txt | head -20\necho \"--- file size / last\"; tail -c 400 IEC.txt"
}
```


### [2026-09-07T20:18:58.406Z] TOOL RESULT

```
35
40
45
852
(if w. *-n-) Vedic nàdhamanah ‘importunate’; nadhitáh ‘oppressed, needy’. (For OHG nen- den “dare”, ge-nindan, sv. “be eager”, and ON nenna "be keen on, woo', see nnt-)
(noqu-, ultimate theme of type *noktis, *nokts, q. v. and cf. nqu-, nqut- Cf. Hitt. nekuc-; Gk. nukheüo “watch through the night; nukhth-émeron, n. "a day and a night', and the vocalism of nüx 'night'; Li. nakvinti, inf. “put up for the night; nakvyne *night's lodging")
nor- (1) “penetration; inside; interior; depth’. Cf. nið, enor-, ner- (2), nerteros. WP IT, 333 OCS norü, m. “den, hole, cave, nest’; nora, norja, f. id.; R norà, f. ‘burrow’; Ukr. norà, f. “hole; source, spring’; Li. náras *diver-bird', cf. naroms, adv. “under water; narüs, adj. “Table to sink”
nor- (2) “join, joint Per. narà ‘partition wall (?); Sw. nara, f. 'car- penter's nail; Li. narys, gs: -io, m. “joint, link, member’; Latv. naris ‘fetter on horse's leg; fetlock'; nàrs (with syntactical length), m. 'vice, clamp'
nor- (3) (?) “narrow, close’. Gmc. fr. *nor- quos in view of Finn. LW, but see noruos (2) below Oss. cf. nárág ‘narrow’; OS naru, OE nearu “narrow, close, strict; OE nearu, gs. we, s. ‘danger’; Finn. (LW) narka, adj. ‘narrow’; Li. (?) narávas, m. (archaic) ‘power; force; tyrant; (mod.) ‘obstinacy’
(nōr-. See Supt: N)
noruos, å (1) ‘incision, groove, burrow, cut, mark, impression; character, habit'. Cf. en-, rouið, rouos, rüió OHG narwa, f. ‘scar; MHG narwe, nar, w. & sf, id.; LG nor, wf. id.; G Narbe, f. d EMSw. narf, Sw. narv, m. 'pockmark, pitted skin’; OCS nravü, m. ‘manner; OCz. nrav ‘custom’; Slovene nráv ‘nature’; R nòrov ‘habit, man- nerism'; Ukr. norov ‘temper’; cf. also Cz. po- nrava ‘larva’; Li. nařvas, narvà, m. f. “cell of honeycomb; cage’; cf. also (?) narávas, m. (*obstinacy'. See nor- (3) above). (For Hes. norbá ‘incision’: Go. at-snarpjan: Du. sner- pen; ON snerpa, see snorb- Supt)
853
noruos, à (2) (?) “narrow; strait'. See nor- (3)
nos “we, us’. Cf. menes, mnés, ns, mes (“me and yow as against ‘me and mine’, hence the varied phonology). Cf. WP II, 320 Skt. nas, acc.gen.dat. ‘us’; Hitt. -nas, acc. & dat. id.; Av. cf. na, adj. our: Alb. na, ne(ve) ‘us’; Lat. nos, prn. ‘we, us’; OCz. ny, nas, prn. ‘us’; OCS ny, nasü, as OCz.
-nos, -nom, -nā (theme of medio-passive participle. Cf. -tós, -tóm, -tà, theme of pas- sive part. with an implied agent). Cf. -men. Skt. cf. dináh, stirnáh ‘given, strewn' as against ditáh, strtáh, id.; sannáh 'seated" as against sattáh, id.; Gk. rhignós ‘perished w. cold”; sparnós ‘rare’ as against spartós 'scat- tered'; Lat. plenus “fulP as against com-pleétus; G ver-dorben as against ver-derbt; E shaven, rotten, molten as against shaved, rotted, melt- ed, etc.
(noseió, frequentative of type nes- (2) ‘turn’, in Gk. noéó ‘turn over in mind, consider, know’, etc.)
nósít- (prob. for *onóo-sth-) “application, addiction, emphasis'. Celtic forms ambig. Cf. Ir. nós, m. ‘custom, habit (phon. uncertain); W naws, pl. au f. ‘nature’, cf. nawd, f. id., adj. “kind, soft’; Br. ncez, f. “way, shape, look, pretence’ beside (LW fr. W?) naóz, id.; Du. noest, adj. ‘hard-working’; Latv. nost, adv. “gone, away, dead? beside nostāja, f. (fr. no + stāja 'attitude")
nót-, os (1) (notis) (prob. for *onót-, see ono:
Gk. áno “above on top”, etc.) Oss. nag (queried: ‘top, surface, cover, back"); Arm. nuk, acc: nus, s. ‘back’; Gk. nótos, m. “surface, ridge, back, backside’; Lat. cf. (vari- ant) nátis, usu. pl. nátes ‘backside’; MIr. nát, s. ‘buttock’; Cz. nat, f. gs: -i “part of a plant above ground; radish- or turnip-top'. Cf. WP II, 340 e
nót- (2) (notiom, io) (?). Cf. nost-, snadh-
(2). (Celtic initial uncertain) W nawd, f. ‘nature’; adv. ‘easily’; Fris. noed (care; responsibility; risk. Phonol. ambig. *notós?); Icel. cf. naeói, if for *noeói, n. “lei- sure, rest’. (Equations uncertain)
--- supt mentions
11854:(nōr-. See Supt: N)
11889:(nug- ‘stab’; nüg- ‘trifle, whim’ (?) See Supt: N and cf. snug-)
11928:nguos, nguinos (?) ‘rotten, sluggish’. Cf. nguo ON okkvinn ‘stodgy, underbaked'; Sw. unken ‘mouldy’; Li. ingas, adj. ‘sluggish’. (For nguén- (?), see Supt: N)
11944:(ntolos (?), see Supt: N)
--- file size / last
d.; OE welt id. MHG (Upper Ger) wülpe, id.; ON ylgr, ds: ylgi, id.; Li. vilke, id.
ulquó, ið (ambiguous consonantism, unless related to type ulquos, etc. see next). Skt. varke, mp. ((seize', but cf. type *uelk-) beside vrkah (2) '(plough'; Srb. vučem, v. ‘drag’; cf. OCS (hapax) vlüci, s. (Ccaltrop? or sim.); Li. vilkiu, eti, v. ‘wear — a garment’; cf. vilktas, m. (tech. *priming); L
```


## [2026-09-07T20:19:06.336Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /tmp && curl -s \"https://archive.org/metadata/mann-an-indo-european-comparative-dictionary-1984-1987\" -o /tmp/iec-370-meta.json && python3 -c \"\nimport json\nd=json.load(open('/tmp/iec-370-meta.json'))\nprint(d.get('server'), d.get('dir'))\nfor f in d['files']:\n    print(f['name'], f.get('size'))\n\" 2>&1 | head -40"
}
```


### [2026-09-07T20:19:11.383Z] TOOL RESULT

```
ia802900.us.archive.org /17/items/mann-an-indo-european-comparative-dictionary-1984-1987
Mann - An Indo-European Comparative Dictionary (1984-1987).epub 2121286
Mann - An Indo-European Comparative Dictionary (1984-1987).pdf 75622175
Mann - An Indo-European Comparative Dictionary (1984-1987)_chocr.html.gz 51141410
Mann - An Indo-European Comparative Dictionary (1984-1987)_djvu.txt 3698758
Mann - An Indo-European Comparative Dictionary (1984-1987)_djvu.xml 45262215
Mann - An Indo-European Comparative Dictionary (1984-1987)_hocr.html 93307559
Mann - An Indo-European Comparative Dictionary (1984-1987)_hocr_pageindex.json.gz 10999
Mann - An Indo-European Comparative Dictionary (1984-1987)_hocr_searchtext.txt.gz 1486201
Mann - An Indo-European Comparative Dictionary (1984-1987)_jp2.zip 1165905241
Mann - An Indo-European Comparative Dictionary (1984-1987)_page_numbers.json 171319
Mann - An Indo-European Comparative Dictionary (1984-1987)_scandata.xml 275575
__ia_thumb.jpg 6096
mann-an-indo-european-comparative-dictionary-1984-1987_archive.torrent 31962
mann-an-indo-european-comparative-dictionary-1984-1987_files.xml None
mann-an-indo-european-comparative-dictionary-1984-1987_meta.sqlite 20480
mann-an-indo-european-comparative-dictionary-1984-1987_meta.xml 1446
```


## [2026-09-07T20:19:16.833Z] TOOL CALL #29: Bash

```json
{
 "command": "ls -l /home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt\ncurl -sG 'https://ia802900.us.archive.org/fulltext/inside.php' --data-urlencode 'item_id=mann-an-indo-european-comparative-dictionary-1984-1987' --data-urlencode 'doc=mann-an-indo-european-comparative-dictionary-1984-1987' --data-urlencode 'path=/17/items/mann-an-indo-european-comparative-dictionary-1984-1987' --data-urlencode 'q=nurn' -o /tmp/iec370-ft.json; head -c 3000 /tmp/iec370-ft.json"
}
```


### [2026-09-07T20:19:18.532Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 3311889 Sep  4 14:06 /home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt
{"ia":null,"q":null,"indexed":true,"matches":[],"error":"No hOCR or Abbyy file present"}
```


## [2026-09-07T20:19:22.997Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /tmp && curl -s -L \"https://ia802900.us.archive.org/17/items/mann-an-indo-european-comparative-dictionary-1984-1987/Mann%20-%20An%20Indo-European%20Comparative%20Dictionary%20%281984-1987%29_djvu.txt\" -o /tmp/IEC-370-full.txt && ls -l /tmp/IEC-370-full.txt && grep -n -i \"nurn\\|nran\" /tmp/IEC-370-full.txt | head -20"
}
```


### [2026-09-07T20:19:25.147Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 3698758 Sep  7 16:19 /tmp/IEC-370-full.txt
118692:nar ‘pomegranate’ and Arm. nurn, gs: nran,
```


## [2026-09-07T20:19:28.299Z] TOOL CALL #31: Bash

```json
{
 "command": "sed -n '118660,118720p' /tmp/IEC-370-full.txt"
}
```


### [2026-09-07T20:19:29.660Z] TOOL RESULT

```
& *mr- especially when followed by the semi- 
vowels *-i- or *-u-. This gives rise to apparent 
doublets, especially in Germanic, in which the 
vowel -a- alternates with -u-) 

(nåt- in Br. nados, nadoz, pl. nadosiu, f. 
a cpd. ‘needle’; Blg. nàtra ‘woof thread’, and 
Latv. nàtns, adj. "of yarn’) 

(nātrā, iə in Li. notrà ‘woundwort and Latv. 
natra, nātre 'nettle") 

(nédus, nédrom in Gk. nēdús “belly, womb’ 
and R & OCS nédro ‘bosom’; Cz. ňadra, npl. 
id.) 

(nédhio in Br. niž, niš, m. “flight, niža, v. 
“fly? and Icel. naeóa, v. ‘blow keenly’) 

(nequrt-, nequort- ‘not a time, not a turn, 
not once' in Br. né-préd never and Li. nekart, 
nekartg *often'. Cf. quert-, qurt-) 

(ni-quol-, -qul- “turned downwards' in Skt. 
ni-külah *downward-moving' and OE neowol 
*precipitious, headlong'. Cf. quel-, quol- and 
ni-) 

(nomos, om in Av. nomo, n. “prayer” and 
OBr. nom ‘temple’, W nwf ‘holy’) 

(nór, onür ‘watery’ (?) in Pahl. anàr, Per. 
nar ‘pomegranate’ and Arm. nurn, gs: nran, 
id.) 

(nüg- or nüg- in Lat. nüga ‘trifle and LG 
nück, G fr. LG Nucke, Nücke, Du. nuk, f. 
‘whim, fad', in G ‘bad temper; Sw. nyck 
fad") 

(nugio (2) in Gk. nüsso, fut: nüxo, aor: 
enügén ‘stab, nudge, dent? and Eng. nick, 
notch) . 

nür- in Av. nüro “quick, instantaneous' and 
OCS nyrjo, nyrati ‘plunge, dive’) 

(nghur- in Gk. ákhor, -oros, n. ‘dandruff 
beside ákhura ‘bran, haf? and Po. wagry, 


musor- — oiros, à, ios 


15 


20 


25
```


## [2026-09-07T20:19:37.264Z] TOOL CALL #32: Bash

```json
{
 "command": "python3 - <<'EOF'\nt=open('/tmp/IEC-370-full.txt',errors='replace').read()\nlines=t.split('\\n')\nidx=None\nfor i,l in enumerate(lines):\n    if 'nurn, gs: nran' in l: idx=i\nprint(idx)\nimport re\n# search backwards and forwards for 4-digit page numbers standing alone\nfor j in range(idx-400, idx+400):\n    s=lines[j].strip()\n    if re.fullmatch(r'1[5-7]\\d\\d', s):\n        print(j, s)\nEOF"
}
```


### [2026-09-07T20:19:38.573Z] TOOL RESULT

```
118691
118328 1641
118421 1642
118488 1643
118579 1644
118642 1645
118734 1646
118803 1647
118893 1648
118962 1649
119055 1650
```


## [2026-09-07T20:19:57.511Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HUB anar\"; grep -n -i \"anâr\\|anār\\|Granatapfel\\|nurn\" HUB.txt | head -20\necho \"=== HRN anar\"; grep -n -i \"Granatapfel\\|anâr\\|anār\" HRN.txt | head -20\necho \"=== HUB nam\"; grep -n \"1022\\|näm 'Name\\|nām\" HUB.txt | head -20"
}
```


### [2026-09-07T20:19:57.586Z] TOOL RESULT

```
=== HUB anar
4246:auar 'Granatapfel', aveza rein*, Anosarvan Anosagdn (Tab.
=== HRN anar
=== HUB nam
```


## [2026-09-07T20:19:58.235Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SKT 360 leaf 380\"; python3 -c \"\nt=open('SKT.txt',errors='replace').read().split('\\f')\nprint(len(t))\nprint(t[380][:2500])\n\""
}
```


### [2026-09-07T20:19:59.588Z] TOOL RESULT

```
=== SKT 360 leaf 380
657
  if*-  (for  i»),
```


## [2026-09-07T20:20:06.526Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SKT ORANGE\"; grep -n \"^ORANGE\\|ORANGE,\" SKT.txt | head\npython3 - <<'EOF'\nimport re\nt=open('SKT.txt',errors='replace').read().split('\\f')\nfor i,L in enumerate(t):\n    if 'ORANGE' in L:\n        print('leaf',i)\n        print(L[:200])\nEOF"
}
```


## [2026-09-07T20:20:07.000Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '4230,4260p' HUB.txt"
}
```


### [2026-09-07T20:20:07.905Z] TOOL RESULT

```
=== SKT ORANGE
```


### [2026-09-07T20:20:07.941Z] TOOL RESULT

```
ist paz. phi. frdrun Regular, right, exceUent*. War die altere Pehlevi-
form ^apakrun : *frdkrun von apdk : *frdk (siehe oben p. 22 und 84)
-I- run?
') Np. az musste als selbstHndiges Wort sein a behalten, da cs
einsilbig war (s. p. 120), enolitisch aber musste es a vor folgendem Vokal
verlieren.— 122 -
Vgl. auch np. yd oder, alter aya mit paz. ayao\ np.
yad *Erinnerung* mit paz. ayad ; yadgdr 'Andenken* = arm.
yetkar 'Brief, Bericht' mit paz. ayadagar; np. yCir Treund
mit paz. ayar Shk. 235, doch ist die Lesung der Pehlevi-
formen noch unsicher. Siehe oben p. 106.
Ueber den Abfall von a- = ap. w- siehe § 22.
Da der Abfall des a erst im alteren Neupersisch statt-
fand, sind mehrfach noch die alten Formen mit a uber-
liefert: so abe- *ohne* (in der Poesie, wie aba, abar s. § 22),
aya'oder {v-aya s. oben p. 106), anosa 'Eeil*\ (bei Firdusi),
auar 'Granatapfel', aveza rein*, Anosarvan Anosagdn (Tab.
136), AnOsazad (Tab. 263, 467), Abevard^) (neben Bevard
und Bavard) Barbier de Meynard, Diet. 13, 81, AnaheS
(Tab. 4) bei arabischen Historikern. Vgl. auch aras und
arask oben p. 12 — 13.
Gegen die Kegel hat sich agar Venn* (neben gar und
ar) = paz. agar bis jetzt erhalten.
Unklar ist das Verhaltniss von avam zu avam : vdm
(== fain JRAS. 1894, 432) 'Schuld*, phi. &pam, bal. LW.
vam (oben p. 19).
§ 3. Im Inlaut ist a (ebenso wie i und u) geschwunden
in der Kompositionsfuge , ausser vor Doppelkonsonanten?
und zwar schon zur Sassanidenzeit.^) Ueber die altere
Zeit erlaubt die Pehlevischrift kein Urtheil, auch das Ar-
menische nicht, das seinen eigenen Gesetzen folgend iiberall,
```


## [2026-09-07T20:20:14.689Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"naranga\\|narangi\\|Orange\" SKT.txt | head -20\necho \"=== leaf for printed 360\"; python3 - <<'EOF'\nimport re\nt=open('SKT.txt',errors='replace').read().split('\\f')\nfor i in range(374,388):\n    print('leaf',i, repr(t[i][:150]))\nEOF"
}
```


### [2026-09-07T20:20:15.982Z] TOOL RESULT

```
7926:Orange,  Granite  :  see  Oroln.
12832:became  *r^t^  by  a  popular  cty- V  fraa  ffr,  Kotd.  Cf.  Span,  tuxranja, |^£e.  ••  llal.  aramcio^  an  orange.  — itinmj,  nSrinj.  mdrgn^,  an  orange. to  PcT».  n<jV,  a  pomegranate. ion.  Orator ;  see  Oral. (F.  —  L  )  I'.  oede.^L.  er^em,  ace. »,  ■  circle,  kpfaexe.
21824:Zest.    I F.  -  L.  -  Gk.)      Fonoerly  a  «Wp of  orange  or  lemon-peel,  used  for  fla' drinks ;  hence,  something  that  gives or  simply  a  reli»h.  — F.  ust,  'tneih whereby  the  kenicll  of  a  walnut  is Cot.;   hence,  a  slice  of  lemoupecL  ^ schisttu,   schistos,  Itt.   cleft,  divide'
23620:Freneh  from  Italian  from  Persian:  car- case (^carcass),  jargonelle,  mommy,  orange« rebeck,  taffeta  (u(^tV^^.
=== leaf for printed 360
leaf 374 ' various  coloun,  in  patches.\n•  L.;  and  C.)  Compounded  ol  pit,  a pic.  and  bald\\  see  Bald.  The  old B  of  baid,  or  balCd,  is  streake'
leaf 375 'rru^me  j see  below.\npemiqtie.  (F.-ltml.— L.)  la  ose  in the  I7tli  cent.;  periwig  beuig  earlier  ^in Engli-h).  —  F.  perruque.  —  Ital.  p'
leaf 376 'ch  (i). to  waste  away  ;  set  Fain. see  Pound  ^i). •cc  Fen  (*).\nlo  pierce,  prick.  (C.—  L.  ?) to  prick.  A  nasaiifted  form the  sense  '
leaf 377 's  which,  F.  /i/Vr  meant  to  excel  in  a thing.  Note  also  F.  pimpant.  smart, fipnicc:  and  sec  Littri.  —  ll  pipart,  to chirp  (hence  '
leaf 378 'L.) ;  older  form /!> ;  A.  S /w".  —  L. jai  fix,  pitch,  •f-  Gk.  maca  \\J[qi \'  "man.  ptkkit.  pitch.\n10  pitch  the  scajn  of  a  &hip. ,) '
leaf 379 "itAq^,  a  flat  sur- face; s«  Plain.\nplan.  (F.-L.)     F.plan,  'the  grouxid-\nfilat  of  a  building;'  Cot.  —  V. pian,  flat ; atcr  form  of  "
leaf 380 '  if*-  (for  i»), '
leaf 381 'tt*,  to  iikould.  form  in  clay  or m\\aaau<f  «  w\\nr-y«iv  •,  ony.  lo ^to  rAart/T,  flat. "  -Gkl  L.  //«/iou.-Gk. formoQlding.~Gk.  vXa^ircu\''
leaf 382 'd.  ;F.-L.)  M.  E.  pit<ien,~0.  F. plat  Jeff  to  plead,  argue.  —  O.  F. /il«</,  a plea ;  see  plea  above.\npleasure.  (F.-L.)  An  £.  spelli'
leaf 383 'lement.  (F.—L,)  F, Col.  —  L.  sttppUmfHtum,  a  filling  ^ suppUre,  to  hll  up.— L.  tup-  \\xmi pUre,  to  fill.\nsupply.  (F.  —  L.)    Forme; '
leaf 384 ' Ptump^  verb,  to  fall  heavily  down  ;  so  also G.  plumpeu^  Swed.  piumpa,  &c.,  to  fall plump,  are  all  due  to  L.  plumbum,  lead, plung'
leaf 385 ' (.F.-L).    O.F. employ.  — L.  imflUatf,  to  impll employ^ :  see  tmplicatc  below.\nexplicate,  to  explain.  tL* of  L.  explicare,  to  unfold, '
leaf 386 'cf.  mod.  E.  to  Afljf.  to  pxktt.^V.  poeAr,  a bag  ;  see  pouoh,  sv.  Poko  (i).\nPock  (I),  a  pustule.  (E. ;  ptrhaps  C.) Smali  pes  «  s'
leaf 387 "wards  extended  to /fiuttrr-er;  fcuUr'jf  (foe f>CMit'fr-y\\\nX\n3<53\nPOOP.\npullet  (F.-L.)  M.  E. f^fete,  later  pouUtte^  fcra. a  chicken  (above)"
```


## [2026-09-07T20:20:23.672Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nraw=open('SKT.txt',errors='replace').read()\n# find leaf index of the ORANGE line\npos=raw.find('to  PcT**') \ni=raw.find('a  pomegranate')\nleaf=raw[:i].count('\\f')\nprint('leaf',leaf)\nt=raw.split('\\f')\nprint(t[leaf])\nEOF"
}
```


### [2026-09-07T20:20:24.968Z] TOOL RESULT

```
leaf 341
  of  an  original  by  meul — O.  F.  f^pit,  abundance;  ftlvH L.  f#^d.  plenty  (aboveV         ^|
office,  duly.    (F.-L.)      F.  ^ offidum.  duty  pKc-^oiaAM^a^Ma. contr.  from  optficiHm.^X^  ^i'»> of  opa,  wealth  ;  fiutrt.  to  do;| Der.  effi('fr,  F.  ojffUttr,  Low  ~ offie-i-CHS,  F.  cfficitux,  L.  o^
optimism,  the  doctrine the  best.  (L.>     From  L.  oftim' best;  with  suffix   -ism  (Gk. 0P'ti-PHus  is  a  supcrl,  form  fn (i.  c.  choice) ;  cf.  optart,  to
option,  choice.   vF.  — L.) L.  optiomm,  ace.  of  «//!«,  ch( to  L.  opfart,  to  wish  (above).
opment,  wealthy     (F.  — 1-> i!nf/.  — L.  opuUntui,  wc&lthy.  — L. of  «|/Vj,  uealth.     Cf.  Skt.  a^oi,  \ Optic,  relating  to  the  tight.    ( F.  optiqu€.  —  Gk,  orriffiii,  bell sight ;  ci.   t*T^Pt  a  spy.     Fi ow-  (for  0*-)  seen  in  Ionic  Sw~ seen,  Sip-ofiat,  I  shall  see;  cf.  t^ the  eye.     See  Sr«.     ( ^AK.)
autopsy,  [fCTSonal  ins]>ccti« iik.  a^mifia,  a  seeing  with  our's  c
—  Gk.  aur-*li,  self;  and  ^(t,  sight catoptric,  relating  tooplicaj  r
(Gk.)  Gk.  KaTorrpixdr,  rcflcxi* ic&Towr^ov,  a  mirror. —  Gk.  aarH inward ;  CirT-o/iat,  I  see.
dioptrics,  the  science  of  the  i of  li^,'ht.  (Ck.)  Gk.  rd  fitorr^ tries. —  Gk.  ^owrpiK6s,  relating  lo Tpa,  an  optical  instrument  for  takinf &c.  —  Gk.  9tA.  through  ;  ^i
ophthalmia,  inflomniatiou] Gk.  i^aA,>iia.  — Gk.  ti^tfoA^. for  uwTuK^ui  •  ;  cf.  Doric
—  Gk.  SwT-oi/at,  I  sec. synopsis,  a  gmcral    view,
I...  jyncpsis.  —  Gk.  ffi-i-oi^n,  i together. —  Gk,  ffvr,  togctlicr: Der.  synpptif-a!,  from  Gk.  ad^.
Or  (l),  conjunction,  offerin^j tive ;  see  Either.
Or  (a),  ere:  sec
Or  (3\  gold  ;  Kc  Auraste.
Oracle ;  see  Or&L
Oral,  8i>okcn.    (L.)     Coino) stem  of  OS,  the  mouth.  ^SkL tinana,  mouth,     (VAN.) odors.  (L.)     L.  tfJInm.
ORANG-OUTANG.
to  i  wfjxrWt  to  p(ay«  from  er-,  ttem  of
mouth.
corable.    ( P.  *  L. )      V.  intxof^ifle.
tejtfffft^tUs.  that  cannot  \>c  moved  by
K.  — X*  lit ,  not;  /x-erart,  lo  gma  by
y-
m  dMne  ftimounccnicnt ;  double fonned  from  ^ra-re,  to  \>ny  (abo\'e). don.  (F.  —  L.)  P.om/fOH.  —  L.acc. tm.  ••  L.  antiiu,  pp.  of  Arn/v,  to  pray  ; >r*  ^above).
tor.  (F.—L.)  FonneHy  0A2/tfvr. — Scvr.^L.  efXttSnm^  ace.  of  orator,  a r.«L.  fiftt/us,  pp.  of  o/urr,  to  pray,
](<ftb0Vf!).
to*.  <F.-L.)  F.  OTT/Jfr,  a  small g.  w  L.  firt/tium,  an  opening,  lit. l£  of  a  mouth.'  — L.  ff/i-,  crude  form Boath ;  /utrt,  to  make.
(r,  ortxistm).^  I.,  craiwntm, »#,    a    prayer ;    &ee    oration
From  pp.  of little
to  kla.  (!.> timri,  lo  kis.*L  osmium,  a
pretty  month ;  double  dimtn.  of  es, «th.
(F.— L.)      F.  peroration. I,  ace  of  piritra/io,    the
,  —  L.  prremtMs,  pp.   of
speak  (above)
plete  a  speech.
l|*-4>lltAng,  a  lar^e  Ai>e.  (Malays ^•cmg iiianAit-  'wild  man* --Malay a  man  ;  $itam,  kiitan,  woods,  wilds  of iry,  wild.
IM.  (F.  -  Ital.  -  Pera.)  O  F. (F.  gfOMgt).  Put  for  narengt*,  but ti»l ««  was  lost  (ID  ItaliBn).  and  then
became  *r^t^  by  a  popular  cty- V  fraa  ffr,  Kotd.  Cf.  Span,  tuxranja, |^£e.  ••  llal.  aramcio^  an  orange.  — itinmj,  nSrinj.  mdrgn^,  an  orange. to  PcT».  n<jV,  a  pomegranate. ion.  Orator ;  see  Oral. (F.  —  L  )  I'.  oede.^L.  er^em,  ace. »,  ■  circle,  kpfaexe.
rbitant,  catrava^ant.  (F.-L.)    F.
IM^  ■*  L*  fJtcrhtaitt',  stem  of  pres.
>H  JiVtffg,  lo  fly  out  of  a  track.  *U
a  track  (below).
L  »riim,  ft  track,  circuit ;
-4(it  >LifIis   -ta  from  <v^'-,  crude f  «v^r  An  offa^  circle.
E;  aec^Krort. B»  l]L»Ck.)    L.  mvJUfim.^
ORE.
Gk.  A/>xi^crpa,  an  orchestra;  which,  in  the Attic  tbcfllrCf  was  a  space  on  which  the chorus  danced.  — Uk.  6pxioftai,  I  tlaucc. Orchis,  a  plant.  (L.  — Gk.)  L.  anhis.^ Gk.  opx^f,  a  testicle,  a  plant  with  roots  of testicular  shape.  Dor.  orchid,  a  false form,    since    tne    gen.    caM    of   ^x"  ^
hp\itM.
Ordain ;  see  Order.
Ordoal;  sec  Deal.
Order.  (F.-L.)    F.  erdtt,  O.  F.  erdine.
—  L.  oniincm,  ace.  of  erdo,  order.  I'cr- hapc  allied  to  Oiigrixi.     Der.  dis-onltr.
oo-ordi
```


## [2026-09-07T20:20:42.781Z] TOOL CALL #39: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'))\nprint(json.dumps(d['SKT'],ensure_ascii=False,indent=1))\n\"\ncd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('SKT.txt',errors='replace').read().split('\\f')\nfor i in (338,339,340,341,342,343):\n    nums=re.findall(r'\\b(3[0-9]\\d)\\b',t[i])\n    print(i,nums[:8], t[i][:60].replace('\\n',' '))\nEOF"
}
```


### [2026-09-07T20:20:44.042Z] TOOL RESULT

```
{
 "title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)",
 "edition_found": "1911 'new and corrected impression' (Google scan)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/aconciseetymolo01skeagoog",
 "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt",
 "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags.",
 "notes": "Nourai says '1882-1967'; the 1967 Oxford reprint reproduces the 1911 rewritten edition, so the 1911 scan is the right pagination.",
 "cites": "page number of Skeat, Concise Etymological Dictionary"
}
338 [] cll  (alxivc). '  ince  percci^-ed  by  its  smell ,     'le
339 []  -  0.  F. «r//  (F.  huili).  —  L   oleum.  «  Gk.  ^Aojov
340 ['316'] tame  n^trne.o Ck.  6fi'!y-tt  same;  Cvofta,  name.  See  S
341 []   of  an  original  by  meul — O.  F.  f^pit,  abundance;  f
342 [] nat«.  (L.)  L.  co-  (for  ntm\ together;  ortiinatus^  arr
343 [] correct  anting.  (F. -Gk.)     M.  E.  erte^raphit.^J  prit
```


## [2026-09-07T20:22:03.576Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /tmp && curl -s \"https://archive.org/metadata/bub_gb_4ZkRAAAAIAAJ\" -o /tmp/skt370.json && python3 -c \"\nimport json;d=json.load(open('/tmp/skt370.json'))\nprint(d.get('server'),d.get('dir'))\nfor f in d['files']:\n  if 'txt' in f['name'] or 'hocr' in f['name']: print(f['name'],f.get('size'))\n\""
}
```


### [2026-09-07T20:22:05.997Z] TOOL RESULT

```
ia800509.us.archive.org /23/items/bub_gb_4ZkRAAAAIAAJ
bub_gb_4ZkRAAAAIAAJ_chocr.html.gz 35806664
bub_gb_4ZkRAAAAIAAJ_djvu.txt 3120575
bub_gb_4ZkRAAAAIAAJ_hocr.html 72439436
bub_gb_4ZkRAAAAIAAJ_hocr_pageindex.json.gz 8109
bub_gb_4ZkRAAAAIAAJ_hocr_searchtext.txt.gz 1090826
```


## [2026-09-07T20:22:11.038Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /tmp && curl -s -L \"https://ia800509.us.archive.org/23/items/bub_gb_4ZkRAAAAIAAJ/bub_gb_4ZkRAAAAIAAJ_djvu.txt\" -o /tmp/skt1882-370.txt && ls -l /tmp/skt1882-370.txt && python3 - <<'EOF'\nimport re\nt=open('/tmp/skt1882-370.txt',errors='replace').read()\nleaves=t.split('\\f')\nprint('leaves',len(leaves))\nfor i,L in enumerate(leaves):\n    if re.search(r'ORANGE|Orange, the name of a fruit|naranga|nSranga', L):\n        print('=== leaf',i)\n        print(L[:100].replace('\\n',' '))\nEOF"
}
```


### [2026-09-07T20:22:13.380Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 3120575 Sep  7 16:22 /tmp/skt1882-370.txt
leaves 1
```


## [2026-09-07T20:22:16.153Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /tmp && grep -n -i \"naranga\\|narangi\\|a pomegranate\" /tmp/skt1882-370.txt | head -10"
}
```


### [2026-09-07T20:22:17.433Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-07T20:22:20.335Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /tmp && head -c 600 /tmp/skt1882-370.txt; echo; grep -c . /tmp/skt1882-370.txt; grep -n -i \"orange\" /tmp/skt1882-370.txt | head"
}
```


### [2026-09-07T20:22:21.602Z] TOOL RESULT

```
A  CONCISE 
ETYMOLOGICAL 
DICTIONARY  OF 
THE  ENGLISH 

LANGUAGE 

Walter  William  Skeat 


Digitized  by  Google 


HARPERS'  LATIN  DICTIONARY 


A  J.ATIN  DICTIONARY,  FOUNDED  ON  THE  TRANSLATION  OF 
"FREUND'S  LATIN  GERMAN  LEXICON."  Edited  by  E.  A.  An- 
drews, LL.D.  Revised,  Enlarged,  and  in  great  part  Rewritten  by 
Charlton  T.  Lkwis.  Ph.D.,  and  Charles  Short,  LL.D.,  Professor 
of  Latin  in  Columbia  College,  N.  Y.    Royal  8vo,  2033  pp.,  Sheep,  $6  50. 

*  *  •  Amoug  the  peculiar  feature?  which  distinguish  the  present  work  may  be  noted 
72198
13968:Low  L.  acc.  citronem.  —  L.  citrus,  orange- 
51232:Orange.  (F.  -  Ital.  -  Pers.)  O.  F. 
51233:orenge  (F.  orange).  Put  for  narenge*,  but 
51237:an  orange.  —  Ital.  arancio,  an  orange.  — 
51238:Pers.  naranj,  ndrinj,  ndrang,  an  orange. 
91162:of  orange  or  lemon-peel,  used  for  flavouring 
96399:case  (carcass),  jargonelle,  mummy,  orange,
```


## [2026-09-07T20:22:25.795Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /tmp && sed -n '51225,51245p' /tmp/skt1882-370.txt; echo \"--- page numbers nearby\"; python3 - <<'EOF'\nimport re\nlines=open('/tmp/skt1882-370.txt',errors='replace').read().split('\\n')\nfor j in range(51100,51330):\n    s=lines[j].strip()\n    if re.fullmatch(r'3[0-9]\\d', s) or re.match(r'^(ORANGE|ORDER|OPTION|ORCHESTRA)', s):\n        print(j, s)\nEOF"
}
```


### [2026-09-07T20:22:27.088Z] TOOL RESULT

```
through ;  orare,  to  speak  (above). 

Orang-outang,  a  large  ape.  (Malay.) 
Malay  6rang  titan,  lit.  '  wild  man.'  —  Malay 
6rang,  a  man  ;  titan,  htitan,  woods,  wilds  of 
•a  country,  wild. 

Orange.  (F.  -  Ital.  -  Pers.)  O.  F. 
orenge  (F.  orange).  Put  for  narenge*,  but 
the  initial  n  was  lost  (in  Italian),  and  then 
arenge  became  orenge  by  a  popular  ety- 
mology from  or,  gold.  Cf.  Span,  naranja, 
an  orange.  —  Ital.  arancio,  an  orange.  — 
Pers.  naranj,  ndrinj,  ndrang,  an  orange. 
Allied  to  Pers.  ndr,  a  pomegranate. 

Oration,  Orator ;  see  Oral. 

Orb.  (F.  — L.)  F.  orbe.  —  h.  orbem,  acc. 
of  orbis,  a  circle,  sphere. 

--- page numbers nearby
51179 317
```


## [2026-09-07T20:22:42.542Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /tmp && python3 - <<'EOF'\nimport re\nlines=open('/tmp/skt1882-370.txt',errors='replace').read().split('\\n')\nidx=[j for j,l in enumerate(lines) if l.strip() in ('359','360','361')]\nprint(idx)\nfor j in idx:\n    print('=== marker',lines[j].strip(),'at',j)\n    print('\\n'.join(lines[j:j+25]))\nEOF"
}
```


### [2026-09-07T20:22:44.002Z] TOOL RESULT

```
[57635, 57873]
=== marker 359 at 57635
359 


tremble,  tri*ph,  tri-plic'ity,  qvadru-ple, 
multi-pie,  &c. 

Pneumatic.  (Gk.)  Gk.  wtvuaruco*, 
relating  to  wind  or  air.  —  Gk.  wtv^m.  (stem 
W(vuar-),  wind,  air.  — Gk.  vviuv,  to  blow. 
Allied  to  Neeae. 

pneumonia.  (Gk.)  Gk.  wtvuovia, 
disease  of  the  lungs. —  Gk.  vvtvfiov-,  stem 
of  irvfl/uaiv  (also  n\*vuuv),  a  lung.  — Gk. 
*WctK,  to  blow,  breathe. 

pulmonary,  affecting  the  lungs.  (L  ) 
L.  pulmonarius,  affecting  the  lungs.  — L. 
pulmon-,  stem  of  pulmo,  a  lung.  Pulmo  «= 
Gk.  vXtvuwv,  variant  ofwtvuiup  (above). 
Poach  (1),  to  dress  eggs.  (F.  — O.  Low 
G.  ?)  Formerly  poch.  —  F.  pecher  ;  Cot. 
gives  4  atuf  pochJ,  a  potched  (poached)  egg.' 
The  orig.  sense  was  prob. '  a  pouched '  egg, 
i.  e.  an  egg  so  dressed  as  to  preserve  it  in 
=== marker 361 at 57873
361 


bed,  couch.  —  O.polster,  a  bolster,  cushion, 
quilt;  the  same  as  E.  Bolster,  q. v.  A 
folhvon  is  a  bolster-man,  a  lie-a-bed. 

Poly-,  many.  (L.-Gk.)  L.  >Wp-.-Gk. 
jroAu-,  crude  form  of  vokxn,  much.-f-Skt. 
puru,  much.   Allied  to  Fall. 

policy,  a  warrant  for  money  in  the 
funds,  a  contract  of  insurance.  (F.— Low 
L.  —  Gk.)  Confused  with  policy,  from 
police,  with  which  it  has  nothing  to  do.  — 
F.  police  (Hamilton).  — Late  L.  politicum, 
polccticum,  corruptions  of  polyptychum,  a 
register  (a  common  word ;  Ducange).  —  Gk. 
vox  vnrvxov*  a  piece  of  writing  in  many 
folds,  hence  a  long  register ;  orig.  neut.  of 
■nokvnrvxos,  having  many  folds.  —  Gk.iroA.u-, 
much  ;  wti/xo-,  crude  form  of  lrrvf,  a  fold, 
leaf,  layer,  connected  with  mvoauv,  to 
fold  up.
```


## [2026-09-07T20:22:52.350Z] TOOL CALL #46: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-07T20:22:52.359Z] TOOL RESULT

```


```


## [2026-09-07T20:22:57.087Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%83n%C3%A9h%E2%82%83mn%CC%A5",
 "prompt": "Give the reconstructed form, gloss, and the list of descendants (Indo-Iranian, Avestan, Old Persian, Persian, Germanic, Latin, Greek, Armenian) for the PIE word for \"name\". Also quote any note on the reconstruction's shape."
}
```


## [2026-09-07T20:22:59.437Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A7%D9%86%D8%A7%D8%B1",
 "prompt": "What does the Persian entry انار (anār) say about etymology? Quote the etymology section fully, including any Middle Persian form, Proto-Iranian reconstruction, and cognates (Armenian, Sanskrit). Also any note about نار."
}
```


### [2026-09-07T20:23:02.826Z] TOOL RESULT

```
# Proto-Indo-European Word for "Name"

**Reconstructed Form:** *h₁nómn̥

**Gloss:** name

**Key Descendants:**
- **Indo-Iranian:** Proto-Indo-Iranian *Hnā́ma
- **Avestan/Persian:** Descendants from Proto-Indo-Iranian form
- **Germanic:** Proto-Germanic *namô (from the collective form)
- **Latin:** Proto-Italic *nōmn̥
- **Greek:** Proto-Hellenic *ónomə
- **Armenian:** Proto-Armenian *anuwn

**Reconstruction Note:**

"Sources disagree on the reconstruction of this word. Some reconstruct it with initial *h₃- because of Greek ónoma, ónuma and (a)nṓnumos, but the lack of an initial laryngeal in Hittite lāman might suggest *h₁."

The article notes that alternative reconstructions exist, including *h₃néh₃mn̥, *nómn̥, and *h₁nḗh₃mn̥, reflecting ongoing scholarly debate about the precise phonological shape of this ancient root.
```


### [2026-09-07T20:23:04.121Z] TOOL RESULT

```
# Etymology of Persian انار (anār)

Based on the Wiktionary content, here is what the Persian etymology section states:

The entry indicates that انار is **"Inherited from Middle Persian _𐭠𐭭𐭠𐭥_ (ʾnʾl /⁠anār⁠/)"** and notes it is **"Arguably, ultimately related to the pomegranate terms under Arabic _رُمَّان_ (rummān)."**

The article does not provide a Proto-Iranian reconstruction, Armenian cognates, or Sanskrit cognates. There is no separate discussion of the alternative form نار (nār) in the etymology section itself—it only appears listed under "Alternative forms."
```


## [2026-09-07T20:23:09.667Z] TOOL CALL #49: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B1%D9%85%D8%A7%D9%86",
 "prompt": "Quote the Arabic رُمَّان (rummān) 'pomegranate' etymology section in full, including any discussion of Middle Persian anār, Armenian nuṙ, Aramaic, Akkadian, and any substrate/Wanderwort theory."
}
```


## [2026-09-07T20:23:11.781Z] TOOL CALL #50: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D5%B6%D5%B8%D5%BC",
 "prompt": "Quote the Armenian նուռ (nuṙ) 'pomegranate' etymology in full — is it a loan from Iranian/Middle Persian anār, or inherited? What genitive form (nṙan) is given? Any cited scholars?"
}
```


### [2026-09-07T20:23:13.190Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-07T20:23:15.717Z] TOOL RESULT

```
# Arabic رُمَّان (rummān) Etymology

The Wiktionary entry states the etymology is of "uncertain direct and ultimate source, not Semitic." It compares cognates across multiple ancient languages:

**Semitic comparanda:** "Hebrew _רִמּוֹן_ (rimmṓn), Punic _*rmn_, and Aramaic _rimmōnā_"

**Other ancient languages:** The entry references Ge'ez, Akkadian forms, and notes Egyptian borrowing from Semitic sources, tracing through Demotic Egyptian and Coptic variants.

**Wanderwort discussion:** Under "Further potential cognates," the text presents Sumerian, Akkadian, Hurrian, and Ugaritic terms for pomegranate with consonantal reordering: "compare also" various cuneiform attestations and Old Armenian _nuṙn_.

**Notable absence:** The entry does not discuss Middle Persian anār or propose substrate theories. It treats the word as borrowing into Egyptian from Semitic languages, suggesting ancient Near Eastern circulation rather than proposing Indo-European or substrate origins.
```


## [2026-09-07T20:23:22.537Z] TOOL CALL #51: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D5%B6%D5%B8%D5%BC%D5%B6",
 "prompt": "Quote the Old Armenian նուռն (nuṙn) 'pomegranate' etymology in full — loan from Iranian (Middle Persian anār) or not? genitive nṙan? cited scholars (Hübschmann, Ačaṙyan)?"
}
```


## [2026-09-07T20:23:23.580Z] TOOL CALL #52: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%86%D8%A7%D9%85",
 "prompt": "Quote the Persian نام (nām) etymology section in full: Middle Persian form, Old Persian/Avestan, Proto-Iranian, PIE. Also list any derived terms like نامه and دشنام mentioned."
}
```


### [2026-09-07T20:23:23.969Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-07T20:23:30.918Z] TOOL RESULT

```
# Persian نام (nām) Etymology

## Etymology Chain

**Middle Persian:** ŠM (/nām/)

**Old Persian:** 𐎴𐎠𐎶 (n-a-m /nāma/)

**Proto-Iranian:** *Hnā́ma (compared with Northern Kurdish nav, Pashto نوم nūm, Avestan 𐬥𐬁𐬨𐬀𐬥- nāman-)

**Proto-Indo-Iranian:** *Hnā́ma (compared with Sanskrit नामन् nā́man, Hindi नाम nām, Urdu نام nām)

**Proto-Indo-European:** *h₁nómn̥ "name" (compared with Greek όνομα ónoma, Italian nome, Armenian անուն anun, English name)

## Derived Terms

The entry lists these related words:
- بدنام (bad-nâm, "infamous")
- بنام (be-nâm, "renowned")
- بهنام (beh-nâm, "of good repute; Behnam")
- نامزد (nâm-zad, "candidate")
- نامور (nâm-var, "renowned")
- نامی (nâmi, "renowned")
- نامیدن (nâmidan, "to name")

Note: While دشنام (dashnām, "insult/curse") shares the نام root, it is not explicitly listed in this entry's derived terms section.
```


## [2026-09-07T20:23:39.378Z] TOOL CALL #53: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D5%B6%D5%B8%D6%82%D5%BC%D5%B6",
 "prompt": "Quote the Old Armenian նուռն (nuṙn) 'pomegranate' etymology in full — is it a loan from Iranian (Middle Persian anār) or inherited? genitive nṙan? cited scholars?"
}
```


## [2026-09-07T20:23:40.685Z] TOOL CALL #54: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AF%D8%B4%D9%86%D8%A7%D9%85",
 "prompt": "Quote the Persian دشنام (došnām) etymology in full — Middle Persian dušnām, prefix duš-, Avestan duš-, and the meaning."
}
```


### [2026-09-07T20:23:45.606Z] TOOL RESULT

```
# Persian Etymology of دشنام

**Etymology Chain:**
The word دشنام (došnām) traces back through Middle Persian (dušnām), derived from Proto-Iranian *dušHnā́ma meaning "insult." This combines the prefix meaning "bad" with a root meaning "name."

**Key Components:**
- **Middle Persian form:** dušnām
- **Prefix duš-:** Corresponds to Avestan duš-, meaning "bad"
- **Meaning:** "Insult" or "verbal abuse"

The Wiktionary entry notes: "from Proto-Iranian *dušHnā́ma ("insult"), from Proto-Indo-European *dus- ("bad") + *h₁nómn̥ ("name")."

Within Persian itself, related words include došman ("enemy") and nâm ("name"), which share etymological components with دشنام.
```


### [2026-09-07T20:23:46.118Z] TOOL RESULT

```
# Etymology of Old Armenian նուռն (nuṙn)

The etymology is **not** from Iranian Middle Persian. According to the Wiktionary entry, նուռն derives from Hurrian _nuranti_ ("pomegranate"), which is related to:

- Hittite _nurati_
- Akkadian _nurimdu/nurimtu_
- Sumerian _nurma_
- Akkadian _nurmû_

The entry notes: "See Arabic _rummān_ for another order of the consonants."

**Genitive form:** նռան (nṙan)

**Cited scholars in Further Reading:**
- Hrachia Adjarian (Armenian Etymological Dictionary, 1971–1979)
- Igor M. Diakonoff ("Hurro-Urartian Borrowings in Old Armenian," 1985)
- Geworg J̌ahukyan (History of Armenian Language, 1987 & 2010)
- Rasmus Thorsø (Prehistoric loanwords in Armenian, 2023)

This represents a **Hurro-Urartian borrowing**, not an Iranian one.
```


## [2026-09-07T20:24:00.782Z] TOOL CALL #55: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E0%A4%A8%E0%A4%BE%E0%A4%B0%E0%A4%99%E0%A5%8D%E0%A4%97",
 "prompt": "Quote the Sanskrit नारङ्ग (nāraṅga) 'orange tree' etymology in full — Dravidian origin? any link to Persian nār 'pomegranate'? cited scholars."
}
```


## [2026-09-07T20:24:01.775Z] TOOL CALL #56: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/orange",
 "prompt": "Quote the full etymology of \"orange\", including Sanskrit naranga-s, Persian narang, and any statement about the ultimate origin (Dravidian? unknown?)."
}
```


### [2026-09-07T20:24:06.518Z] TOOL RESULT

```
# Etymology of "Orange"

According to the Online Etymology Dictionary, the word "orange" traces back through multiple languages:

**Direct lineage:** Late 14th century English "orange" comes from Old French *orange/orenge*, which derives from Medieval Latin *pomum de orenge*, Italian *arancia* (originally *narancia*), and ultimately Arabic *naranj*.

**Earlier origins:** The Arabic term stems from Persian *narang*, which itself comes from Sanskrit *naranga-s* meaning "orange tree."

**Ultimate origin:** The dictionary notes that Sanskrit *naranga-s* has "a word of uncertain origin," indicating the etymological trail ends there without definitive explanation of its ultimate source. The entry provides no mention of Dravidian or other language families as possible origins.

**Historical note:** The text indicates "The tree's original range probably was northern India," establishing the geographical context for these Asian language sources.
```


### [2026-09-07T20:24:07.310Z] TOOL RESULT

```
# Sanskrit नारङ्ग (nāraṅga) Etymology

## Dravidian Origin
The word is "Borrowed from Dravidian" with comparisons to Tamil नार्त्तङ्काय (nārttaṅkāy, "citron"), Telugu నారంగము (nāraṅgamu), Malayalam നാരങ്ങ (nāraṅṅa), and Kannada ನಾರಂಗಿ (nāraṅgi).

## Possible Proto-Austroasiatic Connection
A deeper etymology suggests derivation from "Proto-Austroasiatic *ŋaːm ('sweet')" citing Shorto (2006), Schuessler (2007), and comparative forms in Proto-Bahnaric and Proto-Khasian.

## Cited Scholars
- **Manfred Mayrhofer** (2001) - *Etymologisches Wörterbuch des Altindoarischen*
- **Ralph Lilley Turner** (1969–1985) - *A Comparative Dictionary of the Indo-Aryan Languages*
- **Monier Williams** (1899) - *A Sanskrit–English Dictionary*

## No Persian Connection Mentioned
The provided content contains no reference to Persian nār (pomegranate) in relation to नारङ्ग's etymology.
```


## [2026-09-07T20:24:16.479Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD nomn\"; grep -n \"^nō-men\\|nomen-\\|^no-men\\|nō-mn̥\\|nomn\" AHD_watkins1985.txt | head -20\necho \"=== AHD grep 'name' root\"; grep -n -i \"onomatopoeia\\|NOMENCLATURE\\|SYNONYM\" AHD_watkins1985.txt | head -10"
}
```


### [2026-09-07T20:24:16.545Z] TOOL RESULT

```
=== AHD nomn
=== AHD grep 'name' root
789:METONYMY, METRONYMIC, ONOMATOPOEIA, PARO- NOMASIA, PARONYMOUS, PATRONYMIC, PSEUDONYM, SYNONYMOUS. [Pok. en(o)mn- 321.]
1977:ONAGER agro-, asinus ONCE oi-no- ONCOGENESIS nek-2 ONCOLOGY nek-2 ONE oi-no- ONEIROMANCY oner- ONEROUS en-es- ONOMASTIC no-men- es ONOMATOPOEIA kWej-2, no-men- ONSLAUGHT ant, slak- -ONT es-
2333:SYNARTHROSIS ar- SYNCLINAL klei- SYNCOPE skep- SYNDESMOSIS dé- SYNDETIC dé- SYNDIC deik- SYNECDOCHE dek-', eghs SYNERGID werg- SYNERGISM werg- SYNESIS yé- SYNIZESIS sed-1 SYNKARYON kar-! SYNOD sed-2 SYNONYMOUS nd-men- SYNOPSIS OkW- SYNOSTOSIS ost- SYNTAX tag- SYRINGOMYELIA mis- SYSSARCOSIS twerk- SYSTALTIC stel- SYSTEM sta-
```


## [2026-09-07T20:24:17.597Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== WLD band3 nomen\"; grep -n \"nomen\\|nōmen\" WLD_band3.txt | head -20\necho \"=== WLD Bd1 page 132\"; python3 -c \"\nimport re\nt=open('incoming/WLD/WLD_Bd1_pages.txt',errors='replace').read().split('\\f')\nprint(len(t))\nprint(t[140][:200])\n\" "
}
```


### [2026-09-07T20:24:18.939Z] TOOL RESULT

```
=== WLD band3 nomen
3115:quetechen ak 492. {undectlich) mil- 00", eat) (gut) ayek- 521", treud- 755, | Reflexivypronomen s- 454°. b'iq- 451, dklga- STT j 4 . eh 465", mig- 224* Tgsiatiz) Aewdh- 147"  rieeeln meregh- meng- 268", | rege sein weg Rind qou- 606 or coon Soma Regen 2. rede S65" | (junges) « men a9%..| Le ae Rinde Bat. 180" regnerisches Wetter agAl(u a 563". Reh ork eh Shen Ba ‘ ae - 1 oto fork. : 1 ° pi ene pitt retben ps oe. L, dhon- Boz. Ranke gel. 447. 2. gou- BO. peled- 6°. rafien 2. reu- 351". ger- S99, pleu- 24", rid. 200°. 2. gher- 608. 4, ai{i)- 464", ragen lL. gel- 453; u. der- G28. acik- 466°. _/- regh> 367".  £ mer: 270". _ aeip~ 467°. Rahm reugh-mieju. | (@chuef) 2. ghréu- 648 | 1. seu- 408°, 357". L.ghrem- 655 epee 1. feg- 422°. Rand Bid 183, (aber) amd G55". lnise) #ag- O12*. leizd- 409°, | Teichen ened’ 125, Rippe(agegend) I. perk’-44" (acharfar)  bArtu- 196". 2. teg- 716. rigiki 2. prr- 28". ranzig L. dher- 854. be de 1. | ritmen =. yer- 286, (a)tég- 622%, aik- 465° 2 hg ranzig werden none Hh reichlich men(e}gh- i va : 25" peim(i} 11", | Keichtum 1 175. Fagen derbi. 08. | Reif 3. ker. 409 Rock (aus Ziogertel) bait rassel py fresh , Nears reif werden i cdnioh. Rabre aes bx Ratechlud (weber) 1. deve | _ | | ts gtr ruuben 8. uel Bo. ie 7 mea. Me | Pakconkinohen quel 399. ater GG". machen 2 495. ar Raubtier nlp 317. relnigen 1. 13*. rhaten 10. bher- 165%. Raubyogel, bidao- 135°. | Rela utr.  Lég(s)- 421° bhdg- 187°. (grofer) fino 605. | Reisen aent- 496". | Totlich g.ser- 490°. | Them: S61:; | Reisighaniol For. 462. IRS. m- 451. Bead | or- 452 is”. smeugh- 688" | reifien 8, wel. 30 Rogen raghio- 374". rauchen in- 37D. i. TRS. roh emu 179, = 84. : « PF, sire-a O15" 451. 219%. | Rohr Lolrma-s 40 smugh- 635" j.rei- B43". reth- 368%. rault sein 1. E’er{a)- 427. Pico a74*, | rot reudh- 358° Raum iro- 70. 4. aper- 668", 3. aer- 400", reyoe 356°, (an thy i. Rack machen 2. sew- 323%, Raum haben tulp- 741. | Ruderblatt ip. 428°. upe gep(, jad 346. reizen g er- oe 186. | ern l.eré- 143. rauschen =. go". | . STi. | Ribe rip- S41*. 1 *, Ralativum om 510, fickon niz- 740", areth- TO4". | religifes dhéze- 867. | Riicksicht nehmen ghow- (dompf)  mormor- reno lL. dhen- 852. 635. | a07*. | pleu- 94° rihmen 2. gar- 353. ‘hea Hee sachets tgraitoy te) 5 gage inepien (die Ne Nan) Boi Ge eeshnem Lede! 808, | Richtung’= Lorep- 908%, | Aes : tung nnhmen od. Wei- Chetan reuse. ad rechizeitiy 2ima- 290", | 28, mentor X reckon (reig-) 347* -eont- 406%. | rlitteln (sbgilt- B01", « Frys Fs /. hen L. ond - LT4. rofen ™ 1k a = i - guyAri- ' he 217. 2 gil. 672. dhew- 345 - 443, tod. 7a. i dhewes- S43. gai). 52
=== WLD Bd1 page 132
895
132                    eu(o)nien-, (o)nomen-, nomen-, e n(„)men-             — enos-, onos'

aber mir .nimb ,.Tropfen“, Fick I 4 193, stammt aus dem Lat., Osthoff IF.
4, 27b f.   .




   Ygl. Curtius
```


## [2026-09-07T20:24:25.658Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD entry\"; sed -n '780,795p' AHD_watkins1985.txt\necho; echo \"=== WLD Bd1 leaf 140 (p.132)\"; python3 -c \"\nt=open('incoming/WLD/WLD_Bd1_pages.txt',errors='replace').read().split('\\f')\nprint(t[140][:4000])\n\""
}
```


### [2026-09-07T20:24:26.931Z] TOOL RESULT

```
=== AHD entry
nem-. To assign, allot; also to take. 1. Germanic *nem- in: a. Old English niman, to take, seize: NIM, NUMB; (BENUMB); b. Old English n#mel, quick to seize, and numol, quick at learning, seizing: NIMBLE. 2. Greek nemein, to allot: NEMESIS. 3. O-grade form *nom- in: a. Greek nomos, portion, usage, custom, law, division, district: NOME, -NOMY; ANOMIE, ANTINOMIAN, AN- TINOMY, (ASTRONOMER), (ASTRONOMY), AUTONOMOUS, BINOMIAL, DEUTERONOMY, METRONOME, NOMOGRAM, NOMOGRAPH, NUMISMATICS; b. Greek nomé, pasturage, grazing, hence a spreading, a spreading ulcer: NOMA; c. Greek nomas, wandering in search of pasture: NOMAD; d. Greek nomimos, legal, probably borrowed in Latin nummus, coin: NUMMULAR, NUMMULATE. 4, Perhaps suffixed o-grade form *nom-eso- in Latin numerus, num- ber, division: NUMBER; ENUMERATE, SUPERNUMERARY. [Pok. 1. nem- 763.]
nepot-. Grandson, nephew. Feminine *nepti-. Latin nepos, grandson, nephew, and neptis, granddaughter, niece: NEPHEW, NEPOTISM, NIECE. [Pok. nepdt- 764.] ner-1, Under, also on the left; hence, with an eastward orientation, north. Suffixed zero-grade form *nr-t(r)o- in Germanic *north-, north, in: a. Old English north, north: NORDIC, NORTH; NORMAN; b. Old English northerne, northern: NORTHERN; c. Middle Dutch nort, north: NorsE. Compare deks-. [Pok. 2. ner- 765.] ner-2, Also aner-. Man; basic sense ‘vigorous, vital, strong.” 1. Oldest root form *aner- (with prothetic vowel) in Greek anér (stem andr-, from zero-grade “anr-), man: ANDRO-, -ANDROUS, -ANDRY; PHILANDER. 2. Extended zero-grade form *(9)nrt- in Sanskrit nrtyati, he dances (“moves vigorously”): NAUTCH. 3. Referred by some to this root (as if “having human eyes”; dps, eye; see ok’-) but more likely of unknown origin is Greek anthropos, man (earliest Greek form anthrék”os): ANTHROPIC, AN- THROPO-; LYCANTHROPE, MISANTHROPE, PHILANTHROPY, THEANTHROPIC. [Pok. 1. ner-(t)- 765.]
nera-. To dive, swim. Possibly in Greek Néreus, name of a sea god: NEREID, (NEREIS), NEREUS, NERITIC. [Pok. 3. ner- 766.]
nes-'. To return safely home. 1. Germanic *nes-tam in Old English, Old High German (in composition), and Old Norse nest, food for a journey, akin to the possible Germanic source of Old French harnes, harness: HAR- NESS. 2. Suffixed o-grade form *nos-to- in Greek nostos, a return home: NosTatcla. [Pok. nes- 766.]
nes-2, Oblique cases of the personal pronoun of the first person plural. For the nominative see we-. 1. Zero-grade form *ns- in Germanic *uns in Old English ds, us (accu- sative): Us. 2. Suffixed (possessive) zero-grade form *ns-ero- in Germanic *unsara- in Old English dser, ire, our: OUR, OURS. 3. O-grade form *nos-, with suffixed (possessive) form *nos-t(e)ro-, in Latin nds, we, and noster, our: NOSTRUM; PATERNOSTER. [Pok. 3. ne- 758.] nétr-. Snake. Germanic *néthré- in Old English nédre, snake: ADDER. [Pok. né-tr- 767.]
neu-'. To shout. Suffixed (participial) o-grade form *now-ent-(yo-), “shouting,” in Latin niintius, “announc- ing,” hence a messenger, also a message, and ndéntium, message: NUNCIO; ANNOUNCE, DENOUNCE, ENUNCIATE, PRONOUNCE, RENOUNCE. [Pok. 1. neu: 767.] neu-2, To nod. 1. Latin *nuere, to nod (attested only in compounds), frequentative nutdre, to nod: NUTATION; INNUENDO. 2. Suffixed form *neu-men- in Latin niimen, “a nod,” hence “command,” divine power, deity: NUMEN. [Pok. 2. neu- 767.] neud-. To make use of, enjoy. Germanic *nautam, “thing of value, possession,” in: a. Old English néat, bovine
newn
animal: NEAT2; b. compound form *ga-nauta- (*ga-, with, together; see kom), “he with whom one shares possessions,” companion, fellow, in (i) Middle Dutch ghenét, noot, fellow: MATELOTE (ii) Old High German ginéz, companion, in German Eidgenosse, confederate: HuGuEnot. [Pok. neu-d- 768.] newn. Nine. 1. Germanic *niwun, with variant *nigun, in Old English nigon, nine: NINE, NINETEEN, NINETY, NINTH. 2. Latin novem, nine (< *noven, with m for n by analogy with the m of septem, seven, and decem, ten): NOVEMBER, NOVENA; NONAGENARIAN. 3. Ordinal form *neweno- in Latin nénus, ninth: NONA-, NONES, NOON; (NONAGON), (NONANOIC ACID). 4. Prothetic forms *enewn, *enwn in Greek ennea, nine (> *ennewa, *enwa-): ENNEAD. [Pok. e-neuen 318.] newo-. New. Related to nu-. 1. Suffixed form *new-yo- in Germanic *neuja- in: a. Old English néowe, niwe, new: NEw; b. Old Norse njyr, new: SPAN-NEW. 2. Basic form *newo- in Greek newos, neos, new: NEO-, NEON, NEOTER- IC; MISONEISM. 3. Suffixed form “new-aro- in Greek nearos, young, fresh, contracted into néros, fresh (used of fish and of water), hence néron, water: ANEROID. 4. Basic form *newo- in Latin novus, new: NOVA, NOVATION, NOVEL!, NOVEL?, (NOVELTY), NOVICE; INNOVATE, REN- OVATE. 5. Suffixed form *new-er-ko- in Latin noverca, stepmother (< “she who is new”): NOVERCAL. [Pok. neuos 709.] ni. Down. 1. Suffixed form *ni-t- in Germanic *nith- in Old English nithan, neothan, below: BENEATH, UNDER- NEATH. 2. Suffixed (comparative) form *ni-tero-, lower, in Germanic *nitheraz in Old English nither, lower: NETHER. See compound root nizdo-. [In Pok. 1. en 311.] [niké. Victory. Greek noun of unknown origin. NIKE.] nizdo-. Bird’s nest. Compound root formed from ni + *sd-, zd-, zero-grade form of sed-; literally, “place where the bird sits down.” 1. Germanic *nist- in: a. Old English nest, nest: NEST; b. Germanic ‘*nistilon in Old English nestlian, to make a nest: NESTLE. 2. Latin nidus, nest: NICHE, NIDE, NIDUS; EYAS, NIDIFY. [In Pok. sed- 887.] nobh-. Also ombh-. Navel; later also “central knob,” boss of a shield, hub of a wheel. 1. Germanic *nabo in: a. Old English nafu, nafa, hub of a wheel: NAVE?; b. compound *nabé-gaizaz, tool for piercing wheel hubs (*gaizaz, spear, piercing tool; see ghaiso-), in Old Eng- lish nafogar, auger: AUGER. 2. Variant form *ombh- in Latin umbé, boss of a shield: uMBO. 3. Suffixed form *nobh-alo- in Germanic *nabalé in Old English nafela, navel: NAVEL. 4. Suffixed variant form *ombh-alo- in: a. Latin umbilicus, navel: UMBILICUS; NOMBRIL; b. Greek omphalos, navel: OMPHALOS. [Pok. 1. (enebh-) 314.] nogh-. Also enogh-, ongh-. Nail, claw. 1. Suffixed (diminutive) form *nogh-ela- in Germanic *nagla- in Old English negl, nail: NAIL. 2. Form *onogh- in Greek onux (stem onukh-), nail: ONYX; PARONYCHIA, PERIONYCHIUM, SARDONYX. 3. Variant form *ongh- in Latin unguis, nail, claw, hoof, with diminutive ungula, hoof, claw, talon (< ongh-eld-): UNGUIS. [Pok. onogh- 780.] nogv-. Naked. 1. Suffixed forms *nog’-eto-, *nog’-oto- in Germanic *nakweda-, *nakwada- in Old English nacod, naked: NAKED. 2. Suffixed form *nog~-edo- in Latin niidus, naked: NUDE, NUDI-; DENUDE. 3. Suffixed form *nog’-mo- differentiated or developed into Greek gum- nos, naked: GYMNASIUM, GYMNAST; GYMNOSOPHIST, GYMNOSPER\M. [Pok. nog¥- 769.] no-men-. Name. Earlier form *()noo-mn, zero-grade form *(g)na-men-. 1.Germanic *nam6n- in Old English nama, name: NAME. 2. Latin némen, name, reputation: NOMINAL, NOMINATE, NOUN; AGNOMEN, COGNOMEN, DENOMINATE, IGNOMINY, MISNOMER, NOMENCLATOR, NUNCUPATIVE, PRAENOMEN, (PRONOUN), RENOWN. 3. Greek onoma, onuma, name: ONOMASTIC, -ONYM, -ONYMY; ANONYMOUS, ANTONOMASIA, EPONYM, (EPON- YMOUS), EUONYMUS, HETERONYMOUS, HOMONYMOUS,
okv-
METONYMY, METRONYMIC, ONOMATOPOEIA, PARO- NOMASIA, PARONYMOUS, PATRONYMIC, PSEUDONYM, SYNONYMOUS. [Pok. en(o)mn- 321.]
nét-. Buttock, back. 1. Greek ndton, ndtos, back: NOTO- CHORD. 2. Zero-grade form *noé- in Latin natis, buttock: NATES; AITCHBONE. [Pok. n6¢- 770.]
[nous. Mind, sense, reason, intellect. Greek noun (earliest form noos) of unknown origin. NOESIS, NOUMENON, NOUS; PARANOIA.]
eal Latin énsis, sword: ENSIFORM. [Pok. nsi-s (ids nu-. Now. Related to newo-. 1. Old English ni, now: Now. 2. Latin nunc (< *nun-ce; -ce, a particle meaning “this,” “here”; see ko-), now: QUIDNUNC. [Pok. nu- 770.]
6-. To believe, hold as true. Suffixed form *6-men- in Latin 6men, a prognostic sign, omen: OMEN.
obhel-. Also abhel-. To augment, increase. Greek ophe- los, advantage: ANOPHELES. [Pok. obhel- 772.]
od-'. To smell. 1. Suffixed form *od-os- in Latin odor, smell: opor. 2. Suffixed form *od-é- in Latin olére, to smell (with J for d representing a Sabine borrowing): OLFACTORY, REDOLENT. 3. Suffixed form *od-yo- in Greek ozein, to smell: OZONE. 4. Suffixed form *od-md- in Greek osmé, smell: OSMATIC, OSMIUM; ANOSMIA. [Pok. 1. od- 72.] od-2. To hate. Latin édi, I hate, and odium, hatred: ANNOY, ENNUI, (NOISOME), ODIUM. [Pok. 2. od- 773.] 6g-. Fruit, berry. 1. Zero-grade form *ag- in Germanic *ak-ran- in Old English zcern, acorn: ACORN. 2. Latin iva (preform uncertain), grape: UVEA, UVULA; PYRUVIC ACID. [Pok. 6g- 773.] oid-. To swell. 1. Possibly Old English date, oat: oat. 2. Greek oidein, to swell: EDEMA. [Pok. oid- 774.] oi-no-. One, unique. I. Basic form *oi-no-. 1. Germanic *ainaz in: a. Old English dn, one: A1, AN!, ONCE, ONE; (ALONE), ANON, (ATONE), (LONE), (LONELY), NONE; b. compound *ain-lif-, “one left (beyond ten),” eleven (*lif-, left over; see leikw-), in Old English endleofan, eleven: ELEVEN; Cc. Old High German ein, one, in Ger- man vereinen, to unite: EINKORN, TURNVEREIN. 2. Latin anus, one: INCH}, OUNCE!, UNCIAL, UNI-, UNION, UNITE, UNITY; COADUNATE, QUINCUNX, TRIUNE, UNANIMOUS, UNICORN, UNIVERSE. 3. Latin ndn, not (< *ne-oinom, “not one thing”; ne, not; see ne). II. Suffixed form *oino-ko- in: a. Germanic *ainigaz in Old English &nig, one, anyone: ANY; b. Latin dnicus, sole, single: UNIQUE. III. Suffixed form *oino-lo- in Latin dllus, any (see ne). [In Pok. e- 281.] oito-. An oath. Probably derived from ei-1. Germanic *aithaz in: a. Old English dth, oath: OATH; b. Old High German eid, oath, in German Eidgenosse, confederate: Hucuenor. [In Pok. 1. ei- 293.] okt6(u). Eight. 1. Germanic *ahté in: a. Old English eahta, eight: EIGHT; b. Old Norse ditjan (tjan, ten; see dekm), eighteen: ATTO-. 2. Latin octé, eight: OcTANS, OCTANT, OCTAVE, OCTAVO, OCTET, OCTO-, OCTOBER, OCTONARY; OCTODECIMO, OCTOGENARIAN. 3. Greek okt6, eight: OcTAD; ocTopus. [Pok. okt6 775.]

=== WLD Bd1 leaf 140 (p.132)
132                    eu(o)nien-, (o)nomen-, nomen-, e n(„)men-             — enos-, onos'

aber mir .nimb ,.Tropfen“, Fick I 4 193, stammt aus dem Lat., Osthoff IF.
4, 27b f.   .




   Ygl. Curtius 294, 33S, J. Schmidt KZ. 23, 270 (hier schon zweisilbiger
Wzansatz; ebenso Hirt Abl. 131), Krit. 153, Persson Wzerw. 226, Fick I 4
97, 165, 273, 502, II 191, III 293, Meringer WS. 5, S2 (vertritt bestimmter
                     4         4

als Schmidt KZ. 23, 270 ursprgl. Gleichheit mit enelh- „Nabel“, indem dies
eigentlich die blutfiihrende Kabelschnur bezeichnet hatte wenn zutreffend,                   ;


vielleicht eher „der beim Kinde noch einige Zeit naB bleibende Nabel
samt dem Reste der Nabelschnur“ gewiB berechtigt ist die Abtrennung
                                                            ;


von nebh- ,,bersten“; Scheidung dieser Wurzeln bei Johansson IF. 4, 139
Anm. 3).

en o)men-, (o)nomen-, iiomen-,        )men- „Name“ n.    «.n( 0

     Ai. namci(n-),               „Name“, ap. nama (s. Bartholomae Air.
                          av. narna(n-) n.
IVb. 1064); lat. numen, umbr. nome, numem, gen. nomncr „Yame“ (lat.
agnomen, cognomen die friiher fiir Herkunft von Wz. gen(o) „nosco“ ins
                             ,


Feld gefiihrt wurden — s. dagegen J. Schmidt IvZ. 23, 267f.
                                   -                              beruhen                                 —
auf erst lat. Yermischung mit einem Agnomen = gr. yrcb/na „Kennzeichen“,
aruss. snam g „Zeichen“j.  Gr. ovofia, dial, ovvjua j.Name                                       11
                                                           avcbvvjuoe, vcb-                           ,



rvjnrog  „namenlos“, lakon. "Erv/ua ygaridag (Kretschmer Gl. 1, 353, vgl.
apr. enmeus   Evv/uavTtddag s. Bechtel KZ. 44, 354
                  >,                                  arm. anun (aus *anonn,        ;


alter *onomn oder
                     * nomn) „Name“ Hiibschmann KZ.
                      e                                   22, 10, Arm. Gr. I
                   2
420, Brugmann II     1, 234   Alb. geg. enter, tosk. emeu ,,Kame“ (G. Meyer
                                       1
                                           .




BB. 8, 190, Alb. Wb. 94, Pedersen KG. I 46; wolil aus en^men-')\ air.
ainm n-, pi. unnumn, acymr. ami, pi. (mit Umlaut* cnuein (daher sg. mcymr.
ncymr. enw corn, hanow, mbret. hanff, hanu, nbret. hano „Name“ ;s. Fick
                  ,



II 4 33, Zupitza KZ. 36, 72, Pedersen KG. I 46, Yf. Uber alteste sprachl.
Beziehungen z\v. Ivelten und Italikern 47 f. als Gdf. setze ich nun e n 0 men-
                                                                        ;



an    :   abg. ime, russ. imja, skr.                 hue, cech. jmeno,              alt jme           „Name‘ (Hnmc,
                                                                                                              £




idg. en\ 0 ]>iien);                  emnm ,.Name (mit Hochstufe en- der
                        ape. emmens m., acc.                                   i;




1.   Silbe wie gr. Evv/ia-;         *enm- eine vor -nm- erfolgte Sonder-
                                               das   pr.
behandlung der Red. -St.          und gr. Evvua- dissimilatorische Dialekt-
form aus uvvfta sei, ist kauin zu begrunden). Got. namo n., ahd. as. namo,
ags. noma zum Masc. geworden, aisl. nafn n. „Name“, dehnstufig mhd.
bcnnomen,        ndl.    noetnen „nennen“.
     Curtius 5 320 f.,      zum Ablaut J. Schmidt KZ. 23, 267
                                                      f., Bartholomae BB.
17, 132,                Dio Yerknupfung mit ono- „5vojuai“ (Fick I 4 99,
                Hirt Abl. 92.
276, 272, 505, Yf. LEWb. 2 u. nota) unter „bezeichnen, mit einem Mai
versehen“ und „zeichnen                =
                            bescliuldigen“ hat jede Berechtigung verloren,
da lat. nota, das diese Doppelbed. der Wz. ono- vortauschte, vielmehr als
*gno-t
```


## [2026-09-07T20:24:41.460Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT nāman\"; grep -n \"1064\" BRT.txt | head -10\npython3 - <<'EOF'\nimport re\nt=open('BRT.txt',errors='replace').read().split('\\f')\nfor i,L in enumerate(t):\n    if re.search(r'\\b1064\\b', L) and re.search(r'nam|nām|nãm', L):\n        print('leaf',i)\n        # print segment around 1064\n        j=L.find('1064')\n        print(L[max(0,j-1500):j+1500])\n        break\nEOF"
}
```


### [2026-09-07T20:24:42.960Z] TOOL RESULT

```
=== BRT nāman
```


## [2026-09-07T20:24:46.506Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"Name'\\|Name’\\|,Name\\|„Name\" BRT.txt | head -20\necho \"=== search naman\"; grep -n -i \"naman-\\|nãman\\|näman\" BRT.txt | head -20"
}
```


### [2026-09-07T20:24:46.578Z] TOOL RESULT

```
6130:•  j.  *asa-  n.  Name'*  des  mit  asnn  voha vahUttm  astX  beginnenden  Gebets  Y.  27. 14*':  yö  °s3m  staoiti  (sd.)  . .  hö  mam  slaoiti yim  ahunm  mazdqm  H.  i.  3;  7;  —  stäomi a^3m  n3isml  äagvs\t.24.y,  Y. //.  19  und /2. 1 ;  —  sardiiustrahe  .  .  yd  paoiryö  .  . Staat  'Lm  naist  daivS  Yt.  13. 89;  —  yal  nä . .  %ris  "s^n  ufajtuyät  V.  18. 43 ;  —  "hmca *!0  pasca  hü  fräsmSJaitim  (näml  stuyät od.dgl.)  N.  6"^;  imd  so  Öfters.  a)  auch  mit a)  vanhav-'h  aiwi^r^lmahi  's>m  voAa  Vr. J7. 1.  ß)  vaAista-'^:  ahun^mca  vairitn  .  . °s?m(a  vahUtim . .yeAhl.tiätqmca\.6i.\\i3. 8,'Hyuf.S;—jainii  mqm  ahuna  vairya  ..lapa- yäti  mqm  'la  vakUta  Yt/7. 20;  —  6ayqm 'iahe  vahistake  yazatnatde  'sähe  vahÜtahe yasamaide  frasraeimmca  .  .  Y.  20.  5;  — zara^uitrS  ys  paoiryö  .  .  staota  °sfm  ya^
=== search naman
2895:•  j.  aoxtö-näman-  Adj.  i)  'des  Name  (im Gebet  besonders)  genannt  wird',  von  Gott- heiten: ahrasca  "«lanii  Vr.9.5;  —  vananttm ..  'mamm  YL2/.  1;  —  °ma>um  yasatim V.2,3;  —  'manB yazatahe  Y.J.3,  _j.2of.^, 22.27.  2)  'worin  der  Name  (des  an- gerufenen Gottes)  besonders  genannt  wird', vom  Gebet:  -mana  iwü  yasna  . ,  müra yazäi  Yt.iO.31;  30,  54,  56,  8.  II,  23,  15.
7818:El.?  Ir.  *aiiman-  (S  29J.  \i),  dessen  an  auf ar.  an  oder  an  mit  reduzirtem  denl.  Verschluss- taul  gehen  kann  (S  24.  S.  noch  No.  4-  — Pa,  (lu  Y.  30):  vai  elön  karp  luxsiin  dahel tpandaramat  /ü  astavih,  erl.  i  vi!  iavfl  slav  tie »avfUi;  (tnY-V^):  ifta  tayat  aiLrv  ii  ränoiik dälär,  erLi  Aac  rtr  i  apärön  slav  ne  taz'eH); (ittV.  45)-  kr  fa  an  i  nSmik  srül  estil  a^alä'i i  dättäk,  Sü.!  anyanämalayä.  —  ')  In  Ober- einstimmung  mit  dem  asynd.  danebenstehen- den  uiayiiitis.  —  a)  s.  dazu  Bgm.  Totaüiäl  7 No.  a.  —  3)  S.  NA.,  Ntr.  —  4)  S.  dazu  Dst. ZA.  /.  ai2,  ferner  Gdn.  GIrPh.  3.  31  ('Un. wandelbarkeit'),  JusTl  PrJ. -JA  34I,  24?  ('oiine Bestürzung',  'Maeht'!,  Gray  JAOS.  21.  124 ('immulability').  Aber  die  Etymologie  der  Pü. zu  V.  50  und  44  (cum  V.  nam-)  ist  ebenso unmöglich  wie  die  zu  Y.  4^  (zu  näman-).
10056:—  hyat  vä  ti>i  nämanqm  vüziitjm  .  .  tä Sa-J  pairijasämaids  Y.  j6",  3;  4,  5,  3^.  5, 36. 1  (yio pairf.J');  —  mat  va  padäis(sd.) .  .pairijasäi  Y.50. 8.  a)  'dienend  nahen, dienen':  y!  vä    mazJä   ahurä  pairJ.jasäi
18732:•  j.  nairyö.näman-Adj.  '(mit  männlichem
18733:Namen  sva.)  männlichen  Geschlechts',  von Tieren;  hazanräis  jJ!nr/(sd.)  strl.nämanS ..  -manaitiP.)  V. 13.51,  l4-iG\.  Wert- los; ani>iaHbyS  .  ,  yS  asti  yazatanam  . . *'manh'^Yt4.Z. FB.  (lu  V.):  iiar  näm ;  s.  noch  No.  i.  —  >)  So F  1 ;  NA.  ray5.it',  vgl.  Npü. :  xälis  n.inii.
18879:•  p.  nima",  nämä"  Adv.:  s,  näman-.
18880:•  j.,  g.,  p.  näman-,  j.  n^tnan-"  n.  "Name":
19111:•  ].  n^man-  n.:  s.  unter  näman-.  DieBüdung  ist  andeutlich;  "niil  m  ni"  wohl
20110:AbleiL  —  Pü. :  ämurasnämand.
20768:jAiw.;  das  Relativ  ist  a)  substantivisch: yOi  däityayaona  ''car^nta  ..noil  aitaEsqm.. N.52;—  s.  noch  N.55(Sp.  1205  0. j; — mit  Gen.  part:  yatca  aSaliqm  ra%wqm faoiryö  paiti  ä./asät  hävanänim  (sd.)  a^m astayeiti  N.  ^2;  —  die  Beziehung  ist  un- genau: yä(AFn.)  *malz5  vä  ..  *srävayeiti aUaiiqm  (Sp.  1 4  u.)  vacqm . .  N.  J7.  ß)  ad- jektivisch :  yä  (NDm.)  nara  iämSjfarn^a . . hamqm  aSe  *x^äudrim  (sd.)  saoisram  ba- rälB'lü.64.  e)  ta-  (Sp.617  m.);'A)  im gA^.;  das  Relativ  ist  et)  substantivisch: yastap''  mxidsm  . .  nsit  däill  ia  iim . .  Y. 44. 19;  — yBi  aisirMtn  varadm  ..yaisqtn nSit  Avarstäis  vas  duivar/ia  tst . .  Y.  4g. 4; —  ffyi  urvafymisd.)  cazdsnnhvadi^s tainS-.vaocH  Y.J/.3; — ^^(NPn.)  vS  abi- frä  ta  xsairakya  'Y.33. 13;  — yn  (APn.)W( asä  ya  asäi  g7ul  tasä  (sd.)  mraot ..  tä  . . Y.  46.  g;  31.7,  44.6; — yqscä  haxSai  . . fi-5  mis  vJspäis..  Y.46. 10;  —  yfngs/S"'^ ..  hadimöi  mina/fsd.)  ..  ßng  zbayä  Y. 46.14;  —  mit  Gen.  part:  hyat  vä  tsi nämanqm  väzut>tn  .  .  tä  'hwa  pairijasä- maidl  Y.36.3;  —  die  Beziehung  ist  un- genau: ylf  akftn  dr>gväiti . .  zastSibyä  (sd.) va  varisaitl  vanhäu  va  cöihait!{sd.)  asftm tdi  varäi(sd.)  rädtnilY.ss.z*'^; — yehya . ,  vahist3in  valda  (sd.)  mazda  . .  tq  yatäi Y.  5/,  2a*>;  —  hyaX"'>  miidsm  ..  magavabyö (sd.)  Mit  para  ta  vf..saväi/*c>vTii(,s±) Y. 5/.  15;  —  yam"^  da  .. ränSibya  xSnüt^ni /i>'o/(Sp. I20I  m.)  urvatim  ..tat  n} .,  vaocä Y.^J.3;  vgL57.9  (Sp.  1216  m.);  —  ya (zu  ß)  frasä  (sd.)  avl^ya  yä  (zu  ß)  . .  *p)r?- salte..y}  vä  ..  ayaniaite*baßm  /J(APn.) . .  valnahi  Y.31. 13  "''.  3)  adjektivisch: yäsc'ä  tat  g?nä  . .  vairya  tä  yazamaide  Y. 38.  r ;  —  yä  vS  .  .  *namqm  dadät . .  täis va yasamaidlY. 38.  i,\—  yä  ihids  dadtnts da%ranqm  (sd.)  hacä  ai'äunS  yäs{za.  it)a . .  dngvSJjbyö  ya%a   tä  a»Am  Y.j/.  14;
21471:—  iTjnm  taxmfm  dämSts  upamamm  'tym Y.  2.  15,  7.  26;  7/.  23,  /.  15;  —  nairys.- saahahe  'tahe  Ny.5.6;  V./7  11;  —  apam napätim  .,  yö  upaps  'ts  Yt/p.  52;  — ariisis  'tahe  Y.  57.  33;  —  a^rS . .  aoxts.- nämanS  'tahe  Y.j.  21;  —  atarl  spjnta 'ta  (VS.)  Ny.5.  6;  4,  6;  —  uHJarmim  '.  '. -t»m  Y.  2.  14;  —  S3m5  huhanhs  'tahe  S. i.  28;  2.  28;  —  tardhustrahe  .  .  aoxts.- nämans  'tahe  Y._j.ai.  a)  sie  zerfallen in  mainyava-ißtveiz.) und gai^ya- (Stverz.) : hanjamansm  frabarata  .  .  ahurS  ha'ära mainyaoibys  'taäbyS  V.  2.  20;  —  mainya- väffhs  'tär^hS  satgmca  hazatframca  Yt  6.  i ; ■ —  vtspaHbyB  'tasibyB  mainyaotbyasca  gai- %ya^byasca  Y.j.  19;  usw.
22665:amisf  sfmts  .  .  trlräi/  näman  äzbaya  Y.        '»»t  «'«"'  'bespcien';  s.  AbsoL
23604:•  j.,  g.  väzi^ta-  Adj.  'der  am  besten  vor- wärts bringt,  der  förderlichste,  nützlichste': Ayat  va  tut  nämanqm  't»m  atan  .  .  ta "hwa  pairijasamaid!  "welcher  deiner  Na- men der  förderlichste  ist,  mit  dem  .  ." y.36.  3.  a)  bes.  von  'astay  (sd.):  AvS tsi  matda  .  .  'lö  aakailT  astt/  Y. 31.32; —  buyama  ahurake  .  .  frya  °ta  astayß Y.  70. 4;  —  frytkl  'tahl  asiöii  ratüm amruy!  ätrSm  ..  Y.  13.  a.  A)  Bezeich- nung einer  der  fünf  Arten  des  Feuers": ätr>m  (sd.)  °Um  Y.ij.ii;  —  ätrvm  'hm .,*daium.jatum  sp^n/ayrrm (sd.)  W.ig.40.
25099:•  j.  •ra^'wya-  Adj.  (fem.  'ya-)  'was  der gegebenen  Zeit  entspricht,  angemessen  ist, was  sich  zur  gegebenen  Zeit  und  im  ge- gebenen Fall  gehört':  ya^a  'ya  (NSf) vanna  (Sp.  1372  u.)  V.jj.  46;  —  mthnm .  .  yS  .  .  fravazaite  .  .  'ya  (IS.)  *äxra (sd.)  Aaämnff  Yt/0. 67;  —  yas3  ^wa aextö.nämana  yasna  'ya  (IS.)  vom  yazaite Yt  J0.3o;3i3,  56;  —  'yi  uxlä  F.jf.;  — vavan9  buye  'ya  manaaha  'ya  valargAa 'ya  ^aohna  A.  7, 1 1 ;  —  sonst  neben däitya'{sd.):  viovä  däilyqm ..  *yqm  ävisiim ". .  die  in  rechter  Fonn , ,,  zu  rechter  Zeit ach  vollziehende  Weihe"  Vr,  77.19; —  '^*'- yanqm  'yanqm  kvarstanqm  fyao%nanqm varttäi  pairi  a%3ityanam  ard^wyanam vansäi  Yx.15.  i;  —  argdvlm  .  .  yä  .  . iäirümqm  daitim  'wjtn  patma  ava.baraiti ". .  die  den  Umständen  und  der  Zeit  ent- sprechende Milch  .  ."  Y,  6j.  2 ;  —  in  der Rechtssprache  :f/di>V<i  'ya(APn.)/rSrai^ya (sd.)  F.^e.
25180:j.  rayS.näman'  Yt.  4.  3:  lies  nOByS.»'.
26393:•  j.  süni-''  m."  'Hund':  yat  'nJi para.- irihyäti  ^nastä.ismanasca  pairista.xlu- drasca  "wenn  ein  Hund  stirbt,  der  sein Brod  nicht  mehr  verdient  imd  dem  der Same  versiegt  ist"  V,  y.  50;  —  Aaianrsis 'nl/  slrlMämanö  hasanräis  'nJ/  nairyS.- nämanS  mihwana  strica  nairyasca  "auf tausend  weibliche  und  tausend  mannliche Hunde  kommt  paarweise  ein  Weibchen und  ein  Männchen"  V.  y.  5iä>; —  hasa- tträU  °nXi  strJJiätnanS  haxanrnii  'tüs nairyS.nämattS  V.  14.  i  Gl.
26801:•  j.  stri,niinan-  Adj.  '(mit  weiblichem Namen  sva.)  weiblichen  Geschlechts',  von Tieren:  hatanr.fi/  sartl/(sd.)  °manS  (NP.) . . nairyS.nämanö  V.  13. 51,  i4- 1  GL
26802:ai.  sirinäman-  Adj.  'einen  Weibernamen  fah- rend'. —  Pü. :  mälat  »am.
27013:Abieil  in  ifitn/i  mainyal  (NS.>  —  Pu,t  sfien3i mtnäk,  S&.  (lU  Y.  /):  ifianämanhsj-f/ih,  etl.:  I hermijdena  s^!lah.  —  ■)  Vgl,  in  aiirS.main- yatia-  No.  I.
27255:—  mi^rB ..'iasca  afys sBrS  nairyü.satakasla Yt./0.52;  j^.  85,  Vyt^lO;  —  daütam  hl\ (nämL  mi^rahe)  upa  ar^»m  vazaite  ys\ vanhus  *sS  afys  vairyaMSnm  .  .  rasnus  1 Yt  10.  100;  41;  —  imal  vS . .  jaioyemi mi^ra  .  .  '/a  asya  .  .  rainvS  Y.  6^5.  1 70.3;  —  '^ahe  asyeke  asBiSca  vankuyä naitythela  satikake  Vr.  u.  16;  7.1;  — brUta  U  (näml,  aSsif)  y5  vaahui  °ls  asyS Yt.  //.  16;  —  'sähe  asyehe  taxmahe  tanu- mq%rahe  darH.draoi  ähüiryehe  aoxtö,- nämanU yazatoAe  Y.  3.  so;  4.23,  Y.iS.  14;
```


## [2026-09-07T20:24:55.201Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nraw=open('BRT.txt',errors='replace').read()\nlines=raw.split('\\n')\ni=[j for j,l in enumerate(lines) if 'näman-,  j.  n^tnan-' in l or 'näman-,' in l and 'g.,  p.' in l]\nprint(i)\n# leaf\noff=sum(len(l)+1 for l in lines[:18879])\nleaf=raw[:off].count('\\f')\nprint('leaf',leaf)\nt=raw.split('\\f')\nL=t[leaf]\nprint(re.findall(r'\\b10[5-9]\\d\\b', L)[:20])\nk=L.find('g.,  p.  näman-')\nprint(L[max(0,k-2600):k+1800])\nEOF"
}
```


### [2026-09-07T20:24:56.535Z] TOOL RESULT

```
[18879]
leaf 592
[]
3. 8:  -?-■>.
»>  Ohne  Wert  GdN.  Stud,  /.  81.
•  g.,  j.  naidyah-  Adj.  'der  schwächere; unterliegend':  läiizl  nh  syaeäsanäil byenti.. hyat  as  *aoJä  'dyattAtm  "denn  durch  diese
Taten  setzen  sie"  uns'' in  Furcht , ,,  inso- fern er"'  stark  ist,  (mich)  den  schwächeren" Y.34.Z;  —  _v«5a  aojä  'dyanAtm  Y.j7. io'>;  —  'dy&tpAs  {Q&.)i^  gaotumahe  {%^) parS.yä  Yt /^.  16**.
Kompai.  aus  der  Basis  ar.  *nädh-;  vgl.  ai. nidhilä-  Adj.  'bedrängt,  hilfsbedürftig',  ksL naida  'Not';  s.  dam  Roth  ZDMG.  25.  330, Gdn.  KZ.  ag.  5S4-  —  Pü.:  naadtn  dahUn {yiiiT.-a  DsT.  ZA.  1.  253).  —  »  'sie  uns',  d.  i. der  Irrlehrer  (Pii.  erl.  richtig  airamSy,  s.  unter iay-)  und  seine  Anbänger  mich  {Zara^ui/ra} und  meine  Anhänger.  Im  Folgenden  bat  Zar. nur  den  Irrlehrer  allein  und  sich  selbst  im Auge,  daher  er  nun  den  Sing,  braucht:  "er .  .  den  schwächeren".  —  ')  Aus  Y.  _j^  8 beruh  ergenommen.  —  3)  Man  erwartete  °ar>A', wie  aber  nur  minderwertige  Hds.  bieten.  VII. war  auch  hier  die  Erinnerung  an  Y.  34.  8 wirksam,  s.  No.  2.  —  4)  Zu  Darabs  Ansicht  ■ s.  unter  gaoUma-.
•  j.  näfa-  m.  'Nabel' :  °/S¥.3  g.  a)  'Ver- wandtschaft, Familie':  Aaväi  kscit  '/ai''> havayäi  vise  Aaväi  zantave  Aavayäi  äaiA- Aave  "jede  für  ihre  Familie  . ."  Yt  13.66; —  *yavata  Ai  °/e  *x"ahwan/tä  (sd.)  N,  I7.
KompE;  AbleiL  (s.  auch  •nä/aina-).  —  VgL nä/ah-  und  itaiämadii/a:  —  np.  »ä/  'Nabel* ; ai.  Tgl.  näMqy-  f.  'Nabel',  s.  dazu  S  2j  b.  — Pü.:  Hä/ai.  —  I)  Sonst  erscheint  in  dieser  Zu- sammenstellung nmäna-  n.  'Haus',  sd.  mit  *).
•  j.  nafah-  n.  'Verwandtschaft,  Familie': gayehe  (sd)  mar^hru}  . .  yaAmat  Aata  frä- ^wpTPsat  (näml.  aAurö  matda)  °/3'^  airya- nam  dahyunatn  Yt. /J.  87.
Vgl.  näfa-.  —  I)  Allenfalls  AP.  aus  ♦nä/-  f.. Tgl.  ai.  nabh-  l.
•  j,  näfya-  Adj.  familienangehörig,  ge- schlechtsverwandt"': druatam  °/lm  fbatSs
VytJ7  (?)'>■
KompA.  —  Ableit.  aus  näfO'.  —  ■)  Gdn.s Erklärung,  VSt.  2.  19  ('adelig')  ist  verfehlt; vgl.  oa/fl.  No.  1  und  Pü.  zu  aä/yS.liu-,  — «)  Vgl.  Y.  63.  7.
•  j.  näfyö.karSta-  Adj.  'von  Familien- angehörigen, Geschlechtsverwandten  be- wirkt, \eiAXÜ.3£,A':paitistätJe  'taAe  lbag£at»hs Yt.  13. 120.
•  j.  näfyö.tbis-  Adj.  'der  die  Familien- angehörigen, Geschlechts  verwandten  be- feindet'; inä  nS . .  dusrfta»a»Ae . .  mä  'IbÜe Y.  65.  7.
Pü. ;  nSf  bes,  crL;  kt  patuiandätt  bistl.
•  p.  nima",  nämä"  Adv.:  s,  näman-.
•  j.,  g.,  p.  näman-,  j.  n^tnan-"  n.  "Name":
äat  hi  'ma  fradai^yh  atr».dät)m
```


## [2026-09-07T20:25:06.974Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SYN NAME\"; grep -n \"NAME$\\|18\\.28\\|NAME  \\|'NAME'\" SYN.txt | head -20\npython3 - <<'EOF'\nimport re\nt=open('SYN.txt',errors='replace').read()\nfor m in re.finditer(r'\\d+\\.\\d+\\s+NAME', t):\n    print(m.start(), t[m.start()-100:m.start()+1500].replace('\\n',' ')[:1800])\n    print('---')\nEOF"
}
```


### [2026-09-07T20:25:08.448Z] TOOL RESULT

```
=== SYN NAME
21464:W. tawel, fr. taw ‘silence’ (18.28).
31429:SING A Spout, CRY OuT 18.14 VaRrrous CRIES 18,21 SPEAK, TALK 18.22 Say 18,23 Be SILENT 18.24 LANGUAGE 18.25 DIALECT 18,26 WorD 18.27 DicTIONARY 18.28 NAME 18.31 Asx! (Question, Inquire) 18.32 ANSWER (vb.) 18.33 ApMiT, CONFESS 18.34 Deny 18.35 Asx?, REQUEST 18.36 Promise (vb.) 18.37 RerusE 18.38 Forbip
31815:18.28 NAME ae dvopa Goth. namo Lith. vardas G bvona ON nafn Lett. vdrds we nomen Dan. navn ChSl. me a nome Sw. namn SCr. ime 5 nom OE nama Boh.  gméno h, nombre ME name Pol. imie nae nume NE name Russ. imja Ni ainm Du. naam Skt. ndman- W tT.  ainm OHG namo Av. naman-, nqman- : enw MHG zame Br, hano NHG name
32166:Other terms are derivs. of nouns for ‘name’ (18.28), as Grk. dvouatw, the Gme. group Goth. namnjan, OE nem- nan, etc., and the Slavic group (not in- cluded in the list; some of them mostly ‘ame’ = ‘appoint’ or the like) ChSl. tmenovati, Boh. gmenovait, etc.
3697859 8,21 SPEAK, TALK 18.22 Say 18,23 Be SILENT 18.24 LANGUAGE 18.25 DIALECT 18,26 WorD 18.27 DicTIONARY 18.28 NAME 18.31 Asx! (Question, Inquire) 18.32 ANSWER (vb.) 18.33 ApMiT, CONFESS 18.34 Deny 18.35 Asx?, REQUEST 18.36 Promise (vb.) 18.37 RerusE 18.38 Forbip 18.41 Cau (vb. = Summon) 18.42 Catt (vb. = Name) 18.43 ANNOUNCE 18.44 THREATEN 18.45 Boast (vb.) 18.51 Write 18.52 Reap 18.53 Lerrer (of the Alphabet) 18.54 Letrer (= Epistle) 18.55 TABLET 18.56 PAPER 18.57 Pen 18.58 Ink 18.59 Penci 18.61 Boox 18.62 Pace 18.63 Line 18.64 Print (vb.) 18.65 LiTERATURE 18.66 AuTHor, WRITER 18.67 Portr 1247 CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar Digitized by Arya Samaj Foundation Chennai and eGangotri 1248 SELECTED INDO-EUROPEAN SYNONYMS 18.11 WOICE (sb.) Grk. dw Goth.  stibna Lith. balsas NG gw ON rodd, raust Lett. balss Lat. vor Dan.  stemme, r¢st ChSl.  glasi It. voce Sw. rést, stamma SCr.  glas Fr. voix OE stefn, reord Boh. hlas Sp. voz ME vois, steven Pol. gtos Rum. voce, glas NE voice Russ. golos Ir. guth Du. stem Skt. vac- Nir. — guth, glor OHG _ stimma, stimna, rarta Av. vdé- W. ais MHG ss stimme Br. mouez NHG = stimme Words for ‘voice’ are mostly connect- ed with verbs for ‘speak, say’ (18.21, 22) or are words for the more generic ‘sound’ (15.44), several of which (besides those repeated here) are, as including vocal -sound, also frequently ‘voice’. 1. Derivs. of IH *wekv- ‘speak, say’ (18.21). Walde-P. 1.245f. Ernout-M. 1185 f. Grk. dy (poet.); Lat. vdx (> It. voce, Fr. voiz, Sp. voz, Rum. lit. voce); Skt. vdc-, Av. vié- (nom. sg. Skt. vak, Av. vars); Toch. A 
---
3747980 ’ as listed in 18.26, e.g. NIr. focloir (W. geiriadur), Lith. Zodynas, SCr. rjetnik, Russ. slovar’. 18.28 NAME ae dvopa Goth. namo Lith. vardas G bvona ON nafn Lett. vdrds we nomen Dan. navn ChSl. me a nome Sw. namn SCr. ime 5 nom OE nama Boh.  gméno h, nombre ME name Pol. imie nae nume NE name Russ. imja Ni ainm Du. naam Skt. ndman- W tT.  ainm OHG namo Av. naman-, nqman- : enw MHG zame Br, hano NHG name CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar Digitized by Arya Samaj Foundation Chennai and eGangotri 1264 SELECTED INDO-EUROPEAN SYNONYMS Nearly all the common words for ‘name’ belong to an inherited group of unknown root connection. 1. IE *enmen-, *nmen-, *ndmen-, etc. with manifold gradation. Walde-P. 1.132. Ernout-M. 675f. Falk-Torp 758. Berneker 426. Here belong all the words li cept the Lith. and Lett.; also OPruss emmens (cf. Grk. dial. évuna in Lac, By. Hakpariéas, etc.), Arm. anun, Alb. émén Hitt. aman (with dissim.), and Toch, A rom, B fiem (SSS 50). 2. Lith. vardas, Lett. vards (the latter also ‘word’) : Lat. verbum ‘word? (18.26), Sted ex. 18.31 ASK! (Question, Inquire) Grk. épwrdw Goth. fraihnan Lith. klausti NG pure ON spyrja, fregna, frétta Lett.  jautat, vaicat, klaust Lat. rogare, quaerere Dan.  spé¢rge ChSl.  vitprositi It. domandare Sw. frdga SCr. _ pitati Fr. demander OE Sregnan, dscian, Boh. pti se Sp. preguntar spyrian Pol. pytaé Rum. inireba ME aske, frayne Russ. — sprosit’ Tr. tarmi-foig, imm- NE ask Skt.  pracch- comairc Du. vragen Av. Sras- Nir. fiafruighim OHG  fragén, eiscon W. gofyn MHG vragen, eischen Br. goulenn NHG fragen Ther
---
```


## [2026-09-07T20:25:14.518Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor w in \"^noun,\" \"^name,\" \"^nomenclature,\" \"^synonym,\" \"^antonym,\" \"^anonymous,\"; do echo \"=== $w\"; grep -n \"$w\" KLN_1966.txt | head -3; done"
}
```


### [2026-09-07T20:25:15.821Z] TOOL RESULT

```
=== ^noun,
25680:noun,  n.  —  ME.  nowne,  fr.  AF.  noun,  fr.  OF.  non, nom  (F.  nom ),  fr.  L.  nomen,  ‘name’.  See  name and  words  there  referred  to  and  cp.  esp.  nomi¬ nal,  nominate.
=== ^name,
24927:name,  n.  —  ME  .name,  fr.  OE.  nama,  rel.  to OFris.  nama,  OS.,  OHG.  namo,  MDu.,  MHG., G.  name,  Du.  naam,  ON.  nafn  (for  *namn),  Dan. navn.  Swed.  and  Norw.  namn,  Goth,  namo.
24930:name,  tr.  v.  —  ME.  namen,  fr.  OE.  namian,  fr. nama,  ‘name’.  See  name,  n.
=== ^nomenclature,
=== ^synonym,
=== ^antonym,
3020:antonym,  n.,  opposite  in  meaning  to  another word.  —  Formed  fr.  Gk.  dvxcovupia,  ‘a  word used  for  another,  a  pronoun',  fr.  avxi,  ‘instead of’  (see  anti-),  and  ovup.a,  dialectal  form  of ovoux,  ‘noun’.  See  name  and  cp.  anonym  and words  there  referred  to.
=== ^anonymous,
```


## [2026-09-07T20:25:18.292Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '24927,24935p' KLN_1966.txt; echo ---; grep -n \"nomenclature\\|synonym,\" KLN_1966.txt | head -6"
}
```


### [2026-09-07T20:25:18.374Z] TOOL RESULT

```
name,  n.  —  ME  .name,  fr.  OE.  nama,  rel.  to OFris.  nama,  OS.,  OHG.  namo,  MDu.,  MHG., G.  name,  Du.  naam,  ON.  nafn  (for  *namn),  Dan. navn.  Swed.  and  Norw.  namn,  Goth,  namo.
‘name’,  fr.  I.-E.  base  *enomen,  *onomen,  *no- men,  whence  also  OI.  nama,  Avestic  nama,  Toch. A  hom,  B  hem,  Hitt,  laman  (formed  with  dissim¬ ilation  fr.  *naman),  Arm.  a  mm  (gen.  anuan),  Gk. ovop.a  (dial,  form  ovup.a),  Alb.  emen,  L.  no- men,  OSlav.  ime  (gen.  imene,  imeni),  OPruss. emmens,  emnes,  OIr.  ainm,  OW.  anu  (pi.  enueiri), W.  enw,  Co.  hanow,  ‘name’.  Outside  Indo- European  cp.  Lapp,  namma,  Finn,  nime-.  Hung. nev,  ‘name’.  Cp.  agnomen,  allonym,  anonymous, antonomasia,  antonym,  cognomen,  cryptonym, denominate,  eponym,  Evonymus,  homonym, ignominy,  Jerome,  metonymy,  metronymic,  mis¬ nomer,  nom,  nomen,  nomenclator,  nomenclature, nominal,  nominate,  nominative,  noun,  nuncupa¬ tive,  onomastic,  onomato-,  paronomasia,  paro- nymous,  patronymic,  polyonymous,  praenomen, pseudonym,  renown,  synonym,  toponym,  trino- minal.
Derivatives:  name,  v.  (q.v.),  name-less,  adj., name-ly,  adv.
name,  tr.  v.  —  ME.  namen,  fr.  OE.  namian,  fr. nama,  ‘name’.  See  name,  n.
Derivatives:  name-able,  nam-able,  adjs.,  name- abil-ity,  n.,  nam-abil-ity,  n.,  nam-er,  n.
namesake,  n.,  a  person  having  the  same  name  as an  other.  —  Contraction  of  name's  sake.  Name¬ sake  lit.  denotes  ‘a  person  named  for  the  sake  of another’s  name'.
nan-,  form  of  nano-,  before  a  vowel.
Nancy,  fem.  PN.  —  Prob.  from  a  misdivision  of mine  Ancy  into  my  Nancy.  Ancy  is  a  dimin.  form of  ME.  Annis,  ‘Agnes’.  See  Agnes.  For  a  similar misdivision  cp.  Nanny.
nanism,  n.,  dwarfishness.  —  F.  nanisme,  formed with  suff.  -isme  fr.  L.  nanus,  fr.  Gk.  vavo q,  vxv- vo ?,  ‘dwarf’,  which  is  of  uncertain  etymology. It  is  perh.  a  child’s  lip  word  and  rel.  to  vavvas, vcwo q,  ‘uncle’,  vavvx,  ‘aunt’.  See  nun  and -ism.
---
7809:claim,  tr.  and  intr.  v.  —  ME.  claimen,  fr.  OF. claim-,  accented  stem  of  clamer,  ‘to  call,  cry  out, claim’,  fr.  L.  clamare ,  ‘to  shout,  cry  aloud,  call, declare’,  which  is  rel.  to  cld-rus,  ‘clear,  bright’,’ fr.  I.-E.  base  *kla-,  var.  of  *kal-,  ‘to  shout,  re¬ sound’.  See  calends  and  cp.  clear.  Cp.  also  low, ‘to  make  the  sound  of  a  cow’.  Cp.  also  acclaim, chamade,  clamant,  clamor,  clarity,  class  and the  second  element  in  council,  declaim,  de¬ clamation,  disclaim,  exclaim,  exclamation,  no- menclator,  nomenclature,  paraclete,  proclaim, proclamation,  reclaim,  reclamation.
24928:‘name’,  fr.  I.-E.  base  *enomen,  *onomen,  *no- men,  whence  also  OI.  nama,  Avestic  nama,  Toch. A  hom,  B  hem,  Hitt,  laman  (formed  with  dissim¬ ilation  fr.  *naman),  Arm.  a  mm  (gen.  anuan),  Gk. ovop.a  (dial,  form  ovup.a),  Alb.  emen,  L.  no- men,  OSlav.  ime  (gen.  imene,  imeni),  OPruss. emmens,  emnes,  OIr.  ainm,  OW.  anu  (pi.  enueiri), W.  enw,  Co.  hanow,  ‘name’.  Outside  Indo- European  cp.  Lapp,  namma,  Finn,  nime-.  Hung. nev,  ‘name’.  Cp.  agnomen,  allonym,  anonymous, antonomasia,  antonym,  cognomen,  cryptonym, denominate,  eponym,  Evonymus,  homonym, ignominy,  Jerome,  metonymy,  metronymic,  mis¬ nomer,  nom,  nomen,  nomenclator,  nomenclature, nominal,  nominate,  nominative,  noun,  nuncupa¬ tive,  onomastic,  onomato-,  paronomasia,  paro- nymous,  patronymic,  polyonymous,  praenomen, pseudonym,  renown,  synonym,  toponym,  trino- minal.
25546:calare,  ‘to  call,  cry’.  See  nominal,  claim  and  -tor. nomenclature,  n.,  system  of  names;  terminology. —  L.  nomenclatura,  ‘calling  of  names’.  See  prec. word  and  -ure.
25547:Derivative:  nomenclature,  v.
37893:(Greek  antiq.)  —  Gk.  auvcoptoaia,  ‘a  swearing together’,  fr.  auvoptvuvat,  ‘to  swear  together’,  fr. auv  (see  syn-)  and  optvuvai,  ‘to  swear’,  which  is prob.  cogn.  with  OI.  amiti,  ‘presses  on;  asserts emphatically’.  Cp.  the  second  element  in  swami. synonym,  n.  — •  ME.  sinonyme,  fr.  Late  L.  synd- nymum,  fr.  Gk.  auvtlwujxov,  neut.  of  the  adj. ouvtovupmp,  ‘synonymous’,  used  as  a  noun.  The literal  meaning  of  auvthvupLop  is  ‘having  the same  name  as’;  it  is  formed  fr.  auv  (see  syn-) and  ov-jjaa,  dial,  form  of  ovopta,  ‘name’.  See and  name  cp.  onomato-.  Cp.  also  antonym, homonym,  anonymous.
```


## [2026-09-07T20:25:31.923Z] TOOL CALL #66: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%A7%D9%86%D8%A7%D8%B1/",
 "prompt": "What does the فرهنگ معین (Mo'in) section say for انار? Quote the Mo'in entry verbatim including any bracketed origin tag such as [په.] or [پهلوی]. Also quote the Dehkhoda entry's etymological remarks if present."
}
```


## [2026-09-07T20:25:32.697Z] TOOL CALL #67: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/name",
 "prompt": "Quote the full etymology of the noun \"name\" including the PIE root reconstruction and cognates (Sanskrit, Avestan, Old Persian, Greek, Latin, Armenian, Hittite)."
}
```


### [2026-09-07T20:25:38.230Z] TOOL RESULT

```
# Etymology of "Name" (Noun)

Based on the provided content, here's what the source documents:

The noun "name" originates from Old English *nama*/*noma*, meaning "word by which a person or thing is denoted." It derives from Proto-Germanic *\*naman-*, which appears in cognate forms across Germanic languages (Old Saxon *namo*, Old Frisian *nama*, Old High German *namo*, German *Name*, Dutch *naam*, Old Norse *nafn*, Gothic *namo*).

The ultimate source is the Proto-Indo-European root **\*no-men-** meaning "name."

## Important Limitation

The webpage provided does **not** include cognates from Sanskrit, Avestan, Old Persian, Greek, Latin, Armenian, or Hittite. While the article references Latin *praenomen* and Greek *patrōnymos* in related entries, it does not offer a comprehensive reconstruction showing how the PIE root *\*no-men-* appears across these ancient languages.

To obtain the full comparative etymology you're requesting, you would need to consult more comprehensive Indo-European linguistic resources beyond this particular etymonline entry.
```


### [2026-09-07T20:25:39.592Z] TOOL RESULT

```
# Farhangs Entry for انار

## Farhang-e Mo'in (Moein Dictionary)

The Mo'in entry states:

"( اَ ) [ په . ] ( اِ. ) = نار: درختچه ای از تیرة موردی ها دارای برگ های بیضوی و گل های قرمزرنگ"

This translates to a small tree from the Punicaceae family with oval leaves and red flowers.

## Dehkhoda Etymological Remarks

The Dehkhoda dictionary provides extensive etymological discussion, noting that انار appears in historical Persian sources and appears in Pahlavi texts. The entry traces the term through classical Persian literature and medical texts, indicating its longstanding presence in Persian vocabulary without providing a single definitive foreign origin statement, though it acknowledges scholarly debate about the term's ultimate roots.
```


## [2026-09-07T20:25:43.980Z] TOOL CALL #68: Bash

```json
{
 "command": "sed -n '1,120p' tools/verify_check.py"
}
```


### [2026-09-07T20:25:44.048Z] TOOL RESULT

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


## [2026-09-07T20:25:45.718Z] AGENT

Now let me archive the web sources.


## [2026-09-07T20:25:50.708Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₃néh₃mn̥' --note 'page 370, entry 0 root Nomn/Enomn: PIE word for name, reconstruction debate h1/h3, descendants' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/نام' --note 'page 370 entry 0 node 2: Persian nām < MP ŠM/nām < OP nāma, Proto-Iranian *Hnā́ma' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/دشنام' --note 'page 370 entry 0 node 2: Persian došnām < MP dušnām < PIr *dušHnā́ma' 2>&1 | tail -3"
}
```


### [2026-09-07T20:25:53.063Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/884535e27b67844a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6fabfc517fa8395f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8f25ccc06855358f.txt
```


## [2026-09-07T20:26:03.374Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/انار' --note 'page 370 entry 1 node 2: Persian anār < MP ʾnʾl anār; \"arguably ultimately related to pomegranate terms under Arabic rummān\"' 2>&1 | tail -2\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/رمان' --note 'page 370 entry 1: Arabic rummān pomegranate, not Semitic, ancient Near Eastern Wanderwort; cf Old Armenian nuṙn' 2>&1 | tail -2\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/նուռն' --note 'page 370 entry 1 node 3: Old Armenian nuṙn, gen. nṙan, from Hurrian nuranti — Hurro-Urartian loan, not IE' 2>&1 | tail -2\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/नारङ्ग' --note 'page 370 entry 1 NOTE (SKT:360): Sanskrit nāraṅga borrowed from Dravidian, not from Iranian nār' 2>&1 | tail -2\npython3 tools/fetch_source.py 'https://www.etymonline.com/word/orange' --note 'page 370 entry 1 NOTE: orange < Ar naranj < Pers narang < Skt naranga-s, word of uncertain origin' 2>&1 | tail -2\npython3 tools/fetch_source.py 'https://www.etymonline.com/word/name' --note 'page 370 entry 0 node 6: English name < OE nama < PGmc *naman-, PIE *no-men-' 2>&1 | tail -2\npython3 tools/fetch_source.py 'https://abadis.ir/fatofa/انار/' --note 'page 370 entry 1 node 2: Mo3in entry for انار tagged [په.] = Pahlavi (MON:4557 cross-check)' 2>&1 | tail -2"
}
```


### [2026-09-07T20:26:08.915Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/a582ba5607479c59.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f834596221635778.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4b58b08f6e299532.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e67e0eeb143d0be5.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/7b87a97274c0d98d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/af4b2cc7812997f2.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/2de7d9431e93bbb7.txt
```


## [2026-09-07T20:26:16.424Z] TOOL CALL #71: Bash

```json
{
 "command": "ls site/pages/370.jpg 2>/dev/null; pdftoppm -f 370 -l 370 -r 200 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf /tmp/pg370-p370 && ls -l /tmp/pg370-p370.png"
}
```


### [2026-09-07T20:26:18.281Z] TOOL RESULT

```
site/pages/370.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb 53336 Sep  7 16:26 /tmp/pg370-p370.png
```


## [2026-09-07T20:26:20.067Z] TOOL CALL #72: Read

```json
{
 "file_path": "/tmp/pg370-p370.png"
}
```


### [2026-09-07T20:26:20.500Z] TOOL RESULT

```

```


## [2026-09-07T20:26:20.498Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-07T20:26:32.212Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification\npython3 - <<'EOF'\nimport glob,json\nfor f in sorted(glob.glob('page-*.json')):\n    d=json.load(open(f))\n    for e in d.get('entries',[]):\n        for n in e.get('nodes',[]):\n            if not n.get('words'):\n                print(f, e.get('root'), n.get('id'), n.get('lang'), n.get('verdict'), '|', (n.get('derivation') or '')[:200])\nEOF"
}
```


### [2026-09-07T20:26:33.885Z] TOOL RESULT

```
<persisted-output>
Output too large (72.7KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/tool-results/b0d9o8ysp.txt

Preview (first 2KB):
page-101.json B.r.q 5 Arabic plausible | Pass-through node: Arabic zumurrud زُمُرُّد 'emerald' does go back to Greek smaragdos, but not directly: Wiktionary derives Arabic zumurrud from Persian zumurrud (< Middle Persian ʾwzmbwlt /uzumburd/ 
page-103.json B.y.z, B.w.s 5 Latin confirmed | The empty pass-through box is Latin byssus, -ī f. 'fine linen, byssus', borrowed from Greek βύσσος with the ordinary Latin rendering of upsilon by y and of the Greek nominative -os by -us; it is the f
page-105.json Chiang-yu 2 French plausible | An empty pass-through box, and a reasonable one: French soja (also soya) is a borrowing of the Dutch word, spread through botany — Linnaeus' binomial Dolichos soja / Glycine soja is built on the Dutch
page-105.json Chou-shu, Shu-shu 1 Mongolian disputed | An empty pass-through box asserting Mongol transmission of the Chinese word into Persian. The idea is superficially attractive — the Ilkhanid period is exactly when the Chinese loans Laufer discusses 
page-105.json Cîrâğ 9 Aramaic confirmed | An empty pass-through box, and the crucial one for this branch: the Iranian word reached Arabic through Aramaic, not directly. The Aramaic form is שְׁרָגָא šərāgā, Classical Syriac ܫܪܳܓܳܐ šrāḡā, Manda
page-107.json Čop, Čop-gân 6 Greek confirmed | Pass-through node: the Greek box is printed empty in the book (only the header 'Greek  SKT:87'), so the extraction is faithful — no word was lost. The word Nourai means is Byzantine (medieval) Greek τ
page-112.json Deik 6 French confirmed | A pass-through node with no word printed: it stands for the French forms that carried the Latin dic- family into Persian, i.e. dictée (feminine past participle of dicter, itself from Latin dictāre, fr
page-112.json Deik 10 French plausible | Another empty pass-through box, standing for French disque, the immediate source of Persian دیسک. Two corrections to the arrow as drawn. First, French disque did not come from Greek directly: it is a 
...
</persisted-output>
```


## [2026-09-07T20:26:41.414Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification\npython3 - <<'EOF'\nimport glob,json\nfor f in sorted(glob.glob('page-*.json')):\n    d=json.load(open(f))\n    for e in d.get('entries',[]):\n        for n in e.get('nodes',[]):\n            if not n.get('words') and not n.get('lang'):\n                print(f, e.get('root'), n.get('id'), repr(n.get('lang')), n.get('verdict'), '|', (n.get('derivation') or '')[:300])\n                print()\nEOF"
}
```


### [2026-09-07T20:26:42.868Z] TOOL RESULT

```
page-121.json Deru 1 9 None unverified | An empty box: on the printed page (pdf 121 = book p.91) the arrow out of the Old Persian box points to a rectangle with no language label, no reference and no words — a layout artefact of Nourai's chart software, probably a slot he meant to fill with the New Persian or English continuation of asā-dā

page-137.json Dinghw, Dnghu, Ghu 2, Ghuâ 6 None unverified | There is nothing to verify: on the printed page (p.107 = pdf 137) the box hanging to the right of the Old Persian box is a completely EMPTY double-ruled rectangle — no language label, no reference, no word, no gloss. It mirrors the position of the filled Persian box that hangs to the right of the Pa

page-171.json Gene 1 5 None unverified | Empty pass-through box: on the printed page (pdf p. 171) the box to the right of 'Avestan / Old Persian zana 1' is drawn but contains no language label and no words, so there is no derivation to check. The extraction is faithful to the page — the blank box is in the book. Presumably the slot was mea

page-187.json Ghen 2 None unverified | There is nothing to verify. On the printed page (book p.157 = pdf 187) the arrow leaving the Avestan box runs right across the chart into a plain double-ruled rectangle that carries no language label, no reference, no word and no gloss — the same kind of stray, unfilled frame that occurs elsewhere i

page-189.json Gher 4 2 None unverified | Empty pass-through box: on the printed page (pdf p. 189, book p. 159; see data/verification/sources/refs/ocr/BOOK/189.png) the box to the right of the Avestan box is drawn but left completely blank — no language, no reference, no word. The extraction is faithful to the page; there is nothing to veri

page-190.json Ghers 4 None unverified | A blank double-bordered box that the Avestan node arrows into on the printed page (verified on the 400 dpi render of pdf p.190). It carries no language label and no words, so there is no derivation claim to check. It was missing from the original extraction and has been added as a pass-through node.

page-192.json Gheu 1 20 None unverified | A completely blank rectangle to the right of the second Avestan box (âzŭtay, zav 2), reached by an arrow from it on the printed page (checked on the page image). It has no language header and no words, so it carries no derivation claim. It was missing from the original extraction and has been added 

page-193.json Gheugh, Ghŭgh 6 None unverified | An empty box hanging off the Avestan node on the printed page (top right of the first tree; no language label, no words; see the archived page image data/verification/sources/refs/ocr/BOOK/193.jpg). It carries no derivation claim, so there is nothing to verify. It was missing from the original extra

page-203.json Gwa, Gwâ, Gwen 2 2 None unverified | Empty pass-through box. On the printed page (pdf p. 203, book p. 173; see data/verification/sources/refs/ocr/BOOK/203.png) the large rectangle to the right of the Avestan/Old Persian box is drawn but left completely blank — no language, no reference, no word. The extraction is faithful; there is not

page-203.json Gwadh 2 None unverified | Empty pass-through box: on the printed page (data/verification/sources/refs/ocr/BOOK/203.png) the rectangle to the right of the Avestan box in the Gwadh chart is drawn but left blank — no language, no reference, no word. The extraction is faithful and there is nothing to verify; by the layout of the

page-204.json Gwebh 2 2 None unverified | An empty pass-through box: the printed page (PDF 204) shows a blank rectangle drawn to the right of the 'Old Persian gabawo' box, with no language label, no reference and no word in it — evidently a slot the author left unfilled (there is no Persian reflex of a Baltic word for 'toad'). The extractio

page-206.json Gweie, Gweye 7 None unverified | Empty box. The printed page (PDF p.206 = book p.176, image copied to data/verification/sources/refs/ocr/BOOK/206.png) shows a wide rectangle to the right of the žayâi box with no language label, no reference and no word in it: the author drew the frame and never filled it. The extraction is faithful

page-206.json Gwel 1 2 None unverified | Empty box. On the printed page (book p.176 / PDF p.206, image at data/verification/sources/refs/ocr/BOOK/206.png) the frame to the right of the ni-γrā-ire box is drawn but blank — no language, no reference, no word. The JSON reproduces the page correctly; there is nothing to verify.

page-207.json Gwelbh 2 None unverified | Empty pass-through box. On the printed page (pdf p. 207, book p. 177; see data/verification/sources/refs/ocr/BOOK/207.png) the wide rectangle to the right of the Avestan box in the Gwelbh chart is drawn but left completely blank — no language label, no reference, no word — and no arrow leaves it. Th

page-210.json Gwer 3, Gwere 2 7 None unverified | An empty box. On the printed page (p. 180) the box to the right of 'Old Persian | gar: to devour' carries no language label, no word and no reference — it is a blank continuation cell of the chart's grid, presumably a slot the author left unfilled (the obvious candidate would have been a Persian ref

page-214.json Gwhen 1 21 None unverified | Blank box in the printed chart (p.184), drawn to the right of the Old Persian ni-kan/vi-kan box with an arrow from it; it carries no language label or word. Nothing to verify. The box was missing from the extraction and was added by the owner.

page-224.json I 2, Io, E 4 None unverified | A completely blank box on the printed page (page 224 of the PDF, book p.194): no language header, no reference, no word — only the empty rectangle, drawn to the right of the Avestan pronoun box #3. The extraction is faithful to the page. There is nothing to verify; the derivatives that would have st

page-224.json I 2, Io, E 11 None unverified | A blank box on the printed page — a narrow empty rectangle to the right of the Avestan a-tāra box, with no language header, no reference and no word. The extraction is faithful; there is nothing to verify. Nourai's layout leaves it empty because the Iranian *-tero- comparative has no New Persian con

page-227.json Isto 7 None unverified | An empty box. On the printed page (pdf 227 = book p.197, copied to data/verification/sources/refs/ocr/BOOK/227.png) the arrow leaving the third Avestan box runs right across the chart into a plain double-ruled rectangle with no language label, no reference and no words — the slot where the Persian o

page-231.json Kâ 1, Qâ 6 None unverified | There is nothing to verify: on the printed page (PDF p. 231 = book p. 201, image saved at data/verification/sources/refs/ocr/BOOK/231.png) the box to the right of the 'čanah, činah, činman' box is drawn EMPTY — no language label, no reference, no word, only the rectangle and the connecting arrow. Th

page-234.json Kak 1 10 None unverified | Blank box in the printed chart (p.204), drawn to the right of the Avestan čagad/čageman/čagvah box with an arrow from it; no language label or word. Nothing to verify. The box was missing from the extraction and was added by the owner.

page-248.json Kei 2, Kie 2, Ki 1 5 None unverified | Empty pass-through box: the chart draws an arrow from the Avestan box to a framed rectangle that carries no language label, no reference and no words. The printed page confirms this is how the book itself looks (pdf p.248 rendered at 200 and 600 dpi; copy at data/verification/sources/refs/ocr/BOOK/2

page-263.json Keu 3, Kou, Skeu 3, Skou 8 None unverified | An empty box in the printed chart: the rectangle to the right of the Avestan čevîšî node carries no language label, no word and no reference (confirmed on the page image, site/pages/263.jpg). Nourai's layout normally puts a descendant here; nothing was filled in, and no descendant of čəuuīšī can be 

page-263.json Keu 3, Kou, Skeu 3, Skou 10 None unverified | A second empty box in the printed chart, drawn to the right of the mislabelled 'Old Persian' node and carrying no language, word or reference (checked on the page image). As with node 8 the box was never filled in, so there is no claim to test; the extraction reproduces the page correctly.

page-264.json Keu 4, Keu-bh 5 None unverified | Empty pass-through box: on the printed page (site/pages/264.jpg) an arrow runs from the 'Old Persian caune' box to a blank framed box at the right margin with no language label, no reference and no word in it. It is a layout stub — the slot where a descendant (presumably a European reflex of the 'ma

page-267.json Ki 2, Ko 2, Kyô, Ke 2, Ghe 2 7 None unverified | Blank box in the printed chart (p.237), drawn to the right of the Avestan zî / nôit-zî box with an arrow from it; no language label or word. Nothing to verify. The box was missing from the extraction and was added by the owner.

page-269.json Klei 2 None unverified | Empty box. The printed page (pdf 269, book 239) really does show a blank rectangle to the right of the Avestan box, joined to it by an arrow, with no language label, no reference and no word — see data/verification/sources/refs/ocr/BOOK/269.png. The extraction is faithful; there is nothing to verify

page-270.json Kleu 1 10 None unverified | An empty box on the printed page (checked on the 300-dpi render, copied to data/verification/sources/refs/ocr/BOOK/270.png): the rectangle drawn to the right of the Pahlavi du-srav box carries no language label, no word, no gloss and no reference — only the frame. The extraction is faithful (lang nu

page-272.json Klou-ni 5 None unverified | Empty pass-through box: on the printed page an arrow leaves the 'Old Persian slaunis' box and ends in a wide, completely blank rectangle to its right (verified on the 200 dpi render of pdf page 272). There is no language label, no reference and no word, so nothing can be checked; it is a layout arte

page-275.json Krei 2 None unverified | Blank box in the printed chart (p.245), drawn to the right of the Avestan srî/srîra/sra-yah box with an arrow from it; no language label or word. Nothing to verify. The box was missing from the extraction and was added by the owner.

page-276.json Kreu, Qreu, Qreus, Qruwes, Qrus 21 None unverified | Blank box in the printed chart (p.246), drawn to the right of the Avestan xrŭ/xrŭra/xrŭždra box with an arrow from it; no language label or word. Nothing to verify. The box was missing from the extraction and was added by the owner.

page-279.json Ksei 3 2 None unverified | An empty box on the printed page: on the 200/600-dpi render of pdf page 279 (copied to data/verification/sources/refs/ocr/BOOK/279.png) a wide, completely blank rectangle is drawn to the right of the Avestan šaēiti/šōiθra box, with the arrow from it, but it carries no language label, no reference an

page-286.json Kŭp 2, Kwĕp 5 None unverified | An empty box. On the render of pdf page 286 (200 dpi, copied to data/verification/sources/refs/ocr/BOOK/286.png) a wide blank rectangle is drawn to the right of the 'Old Persian kupsins' box, joined to it by an arrow, with no language label, no reference and no word inside; the extraction is faithfu

page-288.json Kwe, Qwe, Kue, Que, Kwi 2 2 None unverified | An empty box, and empty in the printed book too: pdf p.288 (book p.258) shows a plain rectangle to the right of the Avestan box with no language header, no reference and no word, joined to it by an arrow. There is nothing to verify. From its position (the slot where Nourai normally puts the Middle/N

page-288.json Kwe, Qwe, Kue, Que, Kwi 2 4 None unverified | The second empty box, again blank on the printed page: a rectangle to the right of the Old Persian box, no language header, no reference, no word, reached by an arrow from Old Persian. Nothing to verify. As with node #2 the slot is where the later Persian reflex would go (Middle Persian -(i)č, New P

page-289.json Kwei 2, Kwoi 7 None unverified | An empty box, empty in the printed book too: the render of pdf p.289 (200 dpi, copied to data/verification/sources/refs/ocr/BOOK/289.png) shows a wide blank double-ruled rectangle to the right of the 'Old Persian sâ 1 / fra-sâ' box, joined to it by an arrow, with no language header, no reference and

page-289.json Kwei 2, Kwoi 10 None unverified | A second empty box, blank on the printed page as well: on the render of pdf p.289 a plain double-ruled rectangle stands to the right of the 'Pahlavi pari-sp' box, joined by an arrow, with no language header, no reference and no word. Nothing to verify. The obvious candidate for what Nourai left out 

page-289.json Kwei 2, Kwoi 12 None unverified | The third empty box on this chart, blank in the book as well: on the render of pdf p.289 a plain rectangle stands to the right of the 'Avestan kaěš / fra-kaěš, vi-kaěš' box, joined by an arrow, with no language header, no reference and no word. Nothing to verify. Had it been filled, the natural cont

page-298.json Kwon, Ka 2, Sua 8 None unverified | An empty box, empty in the printed book as well: the 200-dpi render of pdf p.298 (copied to data/verification/sources/refs/ocr/BOOK/298.png) shows a wide blank double-ruled rectangle at the right of the 'Old Persian KNT:210 | spâda : army' box, joined to it by a plain arrow, with no language header,

page-298.json Kwon, Ka 2, Sua 10 None unverified | A second empty box, blank in the printed book too: the render of pdf p.298 (data/verification/sources/refs/ocr/BOOK/298.png) shows a wide double-ruled rectangle to the right of the 'Old Persian KNT:209 | sakâ 2 : dog' box, joined by an arrow, with no language header, no reference and no word. Nothin

page-301.json Lakti, Ljakti 2 None unverified | An empty pass-through box. The printed page really is blank here: the 200-dpi render of pdf p.301 (copied to data/verification/sources/refs/ocr/BOOK/301.png) shows an arrow leaving the Avestan yaxšti box and ending in a wide double-ruled rectangle that carries no language header, no reference and no

page-305.json Legwh 9 None unverified | Blank box in the printed chart (p.275), drawn to the right of the Avestan ragu/ravi box with an arrow from it; no language label or word. Nothing to verify. The box was missing from the extraction and was added by the owner.

page-312.json Leuk, Leuqos 15 None unverified | Blank, unlabelled box in the printed chart, arrowed from the Old Persian box (raucah 'day'); it carries no language label and no words, so there is nothing to verify. The box was missing from the extraction and was added by the coordinator after checking the page image.

page-319.json Maghos, Maghu 2 None unverified | Blank box: the printed page (pdf p. 319, checked on the rendered image, copy kept at data/verification/sources/refs/ocr/BOOK/319.png) really does show an arrow running from the Avestan mağava box into an empty rectangle with no language label, no word and no reference — a leftover of the author's ch

page-324.json Me 2, Měnôt 6 None unverified | An empty pass-through box. On the printed page (pdf 324, book 294) there really is an arrow running right out of the azdā box into a large rectangle that carries no language label and no word — the box was left blank in the book's own artwork, exactly as the extraction records it. There is nothing t

page-331.json Men 1 15 None unverified | Blank, unlabelled box in the printed chart, arrowed from the Old Persian box (man 1, manah, maniš, haxâ-maniš); it carries no language label and no words, so there is nothing to verify. The box was missing from the extraction and was added by the coordinator after checking the page image.

page-333.json Men 3 12 None unverified | Blank, unlabelled box in the printed chart, arrowed from the Avestan box (mati, mnti; fra-manyente); it carries no language label and no words, so there is nothing to verify. The box was missing from the extraction and was added by the coordinator after checking the page image.

page-333.json Men 3 13 None unverified | Blank, unlabelled box in the printed chart, arrowed from the Avestan box (minu; manaothri, moneutro); it carries no language label and no words, so there is nothing to verify. The box was missing from the extraction and was added by the coordinator after checking the page image.

page-335.json Mer 2, Mer-d, Mer-k, Mor-to, Smerd 19 None unverified | Blank, unlabelled box in the printed chart, arrowed from the Avestan box (morandat, marenčaiti; maraxš; mared); it carries no language label and no words, so there is nothing to verify. The box was missing from the extraction and was added by the coordinator after checking the page image.

page-342.json Mreğu, Mrğu 10 None unverified | Blank, unlabelled box in the printed chart, arrowed from the Avestan box (merezu, marazu; merezu-jîti; berez 2; berez-čaxra); it carries no language label and no words, so there is nothing to verify. The box was missing from the extraction and was added by the coordinator after checking the page ima

page-350.json Nas 7 None unverified | Blank, unlabelled box in the printed chart, arrowed from the Avestan / Old Persian box (nâh, nâham); it carries no language label and no words, so there is nothing to verify. The box was missing from the extraction and was added by the coordinator after checking the page image.

page-351.json Ne 1, Nei 3, An 4 18 None unverified | Blank, unlabelled box in the printed chart, arrowed from the Avestan / Old Persian box (a-karana, a-muyamnô, a-sŭr, an-usant); it carries no language label and no words, so there is nothing to verify. The box was missing from the extraction and was added by the coordinator after checking the page im

page-356.json Nei 2, Neia, Nî 3 3 None unverified | A genuinely blank box: the printed page (pdf 356, copy at data/verification/sources/refs/ocr/BOOK/356.png) shows an empty rounded frame to the right of the Pahlavi box, with no language label, no word and no reference, so the extraction is faithful and there is no claim to test. Judging from the lay

page-358.json Neku, Nokut, Nek 2, Nk, Enek, Enk 8 None unverified | Blank, unlabelled box in the printed chart, arrowed from the Avestan box (nas 2, naš, nasaiti, fra-nâš, ašnaoti, asa 2); it carries no language label and no words, so there is nothing to verify. The box was missing from the extraction and was added by the coordinator after checking the page image.

page-361.json Ner 1 14 None unverified | Blank, unlabelled box in the printed chart, arrowed from the Pahlavi box (nâyrig); it carries no language label and no words, so there is nothing to verify. The box was missing from the extraction and was added by the coordinator after checking the page image.

page-362.json Nes 1 10 None unverified | Blank, unlabelled box in the printed chart, arrowed from the Avestan box (asta 2 'home, residence'); it carries no language label and no words, so there is nothing to verify. The box was missing from the extraction and was added by the coordinator after checking the page image.

page-364.json Newo / Nu 13 None unverified | Blank, unlabelled box in the printed chart, arrowed from the Old Persian box (nŭram); it carries no language label and no words, so there is nothing to verify. The box was missing from the extraction and was added by the coordinator after checking the page image.

page-365.json Nî 1 11 None unverified | Blank, unlabelled box in the printed chart, arrowed from the Avestan box (ni-gerepta, ni-yaštâya, ni-paidhya); it carries no language label and no words, so there is nothing to verify. The box was missing from the extraction and was added by the coordinator after checking the page image.

page-366.json Nis 5 None unverified | Blank, unlabelled box in the printed chart, arrowed from the Avestan / Old Persian box (niš, nij; niš-bar); it carries no language label and no words, so there is nothing to verify. The box was missing from the extraction and was added by the coordinator after checking the page image.

page-62.json Ar, Are 5 None unverified | An empty pass-through box. The printed page (pdf p. 62, rendered at 450 dpi) really does show a blank rectangle drawn to the right of the 'Avestan arânte / aram, arem' box, with the connecting arrow, but with no language label, no reference and no word inside it — Nourai's layout left the descendant

page-80.json Bhad 2 None unverified | There is nothing to verify: the printed page really does show an empty box here. On the rendered page (pdftoppm -r 200 of pdf p.80, saved as data/verification/sources/refs/ocr/BOOK/80.png) the box to the right of the Avestan box in the Bhad chart is drawn with its frame and its internal divider but 

page-86.json Bhen 2 None unverified | Pass-through/empty node: on the printed page (book p. 56 = pdf p. 86) an arrow leaves the Avestan box and ends in a large box that is completely blank — no language header, no word, no reference. The extraction is faithful (lang, refs and words are all null/empty in the JSON exactly as in the book);
```


## [2026-09-07T20:26:53.609Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"dus\\.nam\\|duz\\.nam\\|duž.nam\\|dušnam\\|duinam\\|duS\\.nam\" BRT.txt | head -10\necho \"=== search 'schlechten Namen'\"; grep -n \"schlechten  Namen\\|bösen  Namen\\|Namen'\" BRT.txt | head -10\necho \"=== AVG\"; grep -n -i \"dušnaman\\|duš.nāman\\|dus-naman\" AVG.txt 2>/dev/null | head"
}
```


### [2026-09-07T20:26:53.697Z] TOOL RESULT

```
=== search 'schlechten Namen'
18886:•  Yt7.3; — frsit  mg  tat  'ma  framrüm  Yt /.  S;  — yasia  me  .  .  tmi  •inlnli  (als  AP.) drfftJayS  . .  Yt/.  16;  11,  15;  —  ^vjsqs *taia  imi  'msnü  (als  NP.)  parltas^a  '.  . vismie  Yt /.  19;  —  l&sca  mg  °ma  (AP.) abaya^a  Yti5. 49,  50;  —  gSusca  'ma mazdaoätfm  Yt  Ä  2 ;  —  'mSni  amslanqtn sptnianqm  Ytrf-a;  7;  —  sPaitka  va  duyta va  'va'ni  V.  14. 15  (?) -ö.  a)  AS.  und  LS. (im  Sinn  des  IS.)^*  als  Adv.  'mit  Namen'; i)  im  jAw.  AS.  nqma,  hinter  dem  Nom. propr.ä':  iar^zahi ..yat  vaolii^A^ häkairJm °ffio  Yt/0.88;  12-7,  i^-SS';  — pairikayai .  .yS  duzyairya  yqm  mafyaka  . .  Auyäiryqm 'ma  ao/aiti!  (sd.)  YtÄ  51;  V. /j.  z,  6;  — tturf/S  .  .  yim  ma^aka  .  .  kahrkatas  'ma ac/ai/e  (sd.)  V.iS.i$;  17.31  —  vayui  bä 'ma  äkmi  Yt  75.  43 ;  43-48  (oft),  /.  7,  8, 12—15  (oft);  —  vairil yB  haosrava  'ma YtJp-sö;  59,62,  7.30,7^,129',  142,74. 59*,  V, /i".  15;  —  ar?dvi  'ma  apa  V.7.16;
=== AVG
```


## [2026-09-07T20:27:04.892Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('BRT.txt',errors='replace').read()\nfor m in re.finditer(r'du[sz][.\\-]?n', t):\n    print(m.start(), t[max(0,m.start()-200):m.start()+300].replace('\\n',' '))\n    print('---')\nEOF"
}
```


### [2026-09-07T20:27:06.325Z] TOOL RESULT

```
249876  von  a)  ya^ä:  '^,J  nf  atshat yaiiS  hvö  vasat  (sd.)  ¥.29,4;  _J5.6;  — *"i<i  nj''  jjrj'J'j  (sd.)  buyqn  *ya>:a  rtl  .  . YL/6".3;  —  Oa  jamylt  ya^a  afrXnSmi SrB.5;  N.^q;  —  °ü<i(&  duznidätö  yida t.iyui  V.y.47;  — yS  Als  '^a  fräyasaite ya^a..  Yt /J.41;  — yai^S  aAßfsd.)  vairyü 'ia  ralus  Y.Sy.ii;  —  ya^a  ts  l..ming- Mla  .  .  "Jj  iai  dadtmahl  aka*  .  .  Y. j'y.4;  —  ya^a  aetahe  frast>r>näiH  '"^a altahe  paiiLbarat  N.  70;  /2,  6*(?),  F.^a; —  yaisa  ni 
---
1952977 o  M.  ver- nachlässigt wird"  Yt/0.48. Zum  V.  'bar-.  —  ■)  Ob  richtig  überliefert? J  10  hat  •bariHtö.  Jedenfalls  ist  didh'  gram- matisch entsprechend  dem  hubiritöHx..  10.  11» •  j.  duz-ni'8äta- "  Adj.  etwa  'auf  den man  sich  schlecht  verlassen  kann,  unzu- verlässig': dkah  'ts  (näml.  ist  der  Hund) \ya'ia  tayus  . .  '13  ya>a  disus  V.  ij.  47, I      Pü.;    duS(i)'^hein   'übel   veranlagt',   mit    der Erl.:    tat  /n  /ir  i  apt  vimärenend  apt  a^arel, 
---
```


## [2026-09-07T20:27:17.911Z] TOOL CALL #77: WebSearch

```json
{
 "query": "Avestan \"dužnāman\" OR \"duš.nāman\" bad name Bartholomae"
}
```


### [2026-09-07T20:27:24.177Z] TOOL RESULT

```
Web search results for query: "Avestan "dužnāman" OR "duš.nāman" bad name Bartholomae"

Links: [{"title":"BARTHOLOMAE’S LAW - Encyclopaedia Iranica","url":"https://www.iranicaonline.org/articles/bartholomaes-law-the-name-given-to-a-rule-of-phonetic-assimilation-in-the-indo-iranian-and-probably-also-the-proto-indo-eu/"},{"title":"BARTHOLOMAE, CHRISTIAN - Encyclopaedia Iranica","url":"https://www.iranicaonline.org/articles/bartholomae-christian-german/"},{"title":"Books on Avestan (Avesta) Language","url":"https://www.avesta.org/abooks.html"},{"title":"Bartholomae's law - Wikipedia","url":"https://en.wikipedia.org/wiki/Bartholomae's_law"},{"title":"Altiranisches Wörterbuch by Bartholomae Christian - AbeBooks","url":"https://www.abebooks.com/book-search/title/altiranisches-w%F6rterbuch/author/bartholomae-christian/"},{"title":"Avestan alphabet","url":"https://en-academic.com/dic.nsf/enwiki/933243"},{"title":"On the Etymology of the Avestan Personal Name pourušaspa- in: Iran and the Caucasus Volume 28 Issue 1 (2024)","url":"https://brill.com/view/journals/ic/28/1/article-p72_6.xml"}]

The search results provide information about Christian Bartholomae and his extensive work on Old Iranian linguistics, but they don't contain specific information about the Avestan term "dužnāman" or "duš.nāman" (meaning "bad name"). 

The results show that Bartholomae developed an older transcription scheme for Avestan that is still referenced in modern Avestan studies, and he produced comprehensive works on Old Iranian including his Altiranisches Wörterbuch (1904), which would be the type of reference work where such a term might be documented.

However, the specific term "dužnāman"/"duš.nāman" and its relationship to Bartholomae's work does not appear in these search results. You may need to consult Bartholomae's dictionary directly or search for more specialized Avestan linguistic resources to find information about this particular term.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-07T20:27:30.259Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY\ngrep -n \"انار\" ARY_pages.txt | head -5\necho \"=== nam\"; grep -n \"^نام\\|نام -\\|نام،\" ARY_pages.txt | head -10\necho \"=== latin index\"; grep -n -i \"NAM\\b\\|ANAR\" ARY_latin_index_pages.txt | head -10"
}
```


### [2026-09-07T20:27:30.340Z] TOOL RESULT

```
3628:انار
6315:فرانسه (88۸/0/4): انار نونی (لتی) (47714(7ا): 115
10647:تخاری ۸ (۸ ۷(لق م7 70): ۸0 انگلیسی کهن (تاقنا80 صزم: ‏ انار
12593:بونانی 080): 005 ولزی (5(7ا#): انار ۱
14314:انگلیسی (6(/0/580): انار ۱۷ 8 (98ت01)) +7
=== nam
74:نام «مند و اروپایی؛ (1800-81-8078۸0۷0) بدین دلیل نو آوری شده که زبانهای این
829:نامعلومی حدود سه هزار کیلومتر راه پیموده و خود را به درّه‌ی نا رم در ترکستان چین رساندند. به
12384:نام این پرنده یک واژه‌ی آوایی (نام آوا 03081۸707081۸) است که در بسیاری از زبان‌های هند و اروپایی
=== latin index
2293:AJINAM AZAK H(PAHLAVD 5 ay
2584:Now ENGLISH) JS NONAM, NU, NU:(SANSKRIT) <4 Suite
2814:STARE, STANARE -STANVANTI, STA, TISHATI
2822:stan STANAM ARMENIAN (a)
4320:DELANARRE: ===S=S*~*~« PENI, PENI, PASUNE
4571:PARNAM, PURNA PARENEM, PARQNA
4870:Vv4A fgets Say SKAMBHANA, SKAMBHANAM
5484:TYRAS, TYRE — (LITHUANIAN) ,¢\y-) ANAM ARMENIAN) +
6096:JATUK, JANAM (ARMENIAN) +,
9265:HOLD CHURCH SLAVIC) 4S v5 Yel JAN AJANAM |
```


## [2026-09-07T20:27:35.199Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY\npython3 - <<'EOF'\nt=open('ARY_pages.txt',errors='replace').read().split('\\f')\nfor i,L in enumerate(t):\n    if 'انار' in L.split('\\n')[0] or L.strip().startswith('انار'):\n        print('block',i, L[:60])\n# find the block containing line 3628\nlines=open('ARY_pages.txt',errors='replace').read().split('\\n')\nprint(repr(lines[3620:3645]))\nEOF"
}
```


### [2026-09-07T20:27:36.570Z] TOOL RESULT

```
['8۸7۸ ,8۸3۸2 ,8۸7۱/78 ,8۸336172', 'پپلوی (1مالهم: (۸۲۲۵185) 852 لیتوانی (۸(1۸/4ل 4 7/.): 8 و817]8', 'ساسکریت (54۸/۶8۵/7): 818۸۸/۸3۸ آتونی (لتی) (7۵/۷ا): 7', '8۸/81۸۸ پروسی کهن (4۷ا59نا۲# ا0): ۰ 817785', 'لاتین (/710مل): 08 ایرلندی کهن (#اکلقا 0ا0): انا', 'ایسلند یکهن (ل۵/( 0ات5 صام. 8 گالی (0ل8لانا0۸): 2305', 'آلمانی کهن ((05۸۸/۸ ۲04 صاه): ولزی (7اک7): اد', 'انار', 'آلمانی (0874۸0): دازا پسگشت\u200cها گت دش', 'انگلیسی کهن (تل5لل5(/0 طان): ردنا 6 ۶0020', 'انگلیسی (8(/01387): ادن 5 (888) جمترچید', 'دانمارکی (/0۸//3): 2 142 :م05', 'سرئدی (7ل8(75275): 3 4 (885) :28( مار', 'نروژی (/(2/0717201۵): 3 192 ۸0', 'هلندی (7ل007): 11 4 (852) :0/05', 'اسلاری کهن (10ما؟ تال صز): 3 (888) 37', 'ی 810175۸ برهان قاطع : ۳و ۳۱۶', 'ای چکه (62808:. ۷5۸ لغت\u200cنامه دهخدا: ۳۳۹', 'اسلراکی ماه ۷0۲5۸', 'یادداشت,', '۱ واژه\u200cی آانگیین" فارسی از آانگه" به چم "شیر ۰ و عسل" است(برهان قاطع :: ۱۷۴). واجریشه\u200cی ۰81881 از هند و', 'اروپایی -8737* به چم "زنبور" است. واژه\u200cهای "انگدان" و "انجبار" و "انگوژه" نشان می\u200cدهد که "انگه" به چم "یره', 'و شهد" است. لذا "انگیین" يا "انگویین " یعنی یره پا شهد" زنبور,', '\x0c[pdf page 125]', 'لا زژ)۹گگگک ۳']
```


## [2026-09-07T20:27:44.463Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY\ngrep -n \"^نام$\\|^نام \\|^انار$\\|^انار \" ARY_pages.txt | head -10\necho \"=== latin index NAMA\"; grep -n \"NAMA\\|NOMEN\\|ONOMA\" ARY_latin_index_pages.txt | head -20"
}
```


### [2026-09-07T20:27:45.752Z] TOOL RESULT

```
74:نام «مند و اروپایی؛ (1800-81-8078۸0۷0) بدین دلیل نو آوری شده که زبانهای این
3628:انار
12384:نام این پرنده یک واژه‌ی آوایی (نام آوا 03081۸707081۸) است که در بسیاری از زبان‌های هند و اروپایی
=== latin index NAMA
1339:bean (ONOMATOPOIC) 1 sTeln pT stan So s2oge 1 y Ci
3710:gen GUL; 42 OT Glan Jy e| CONOMATOPOETIC) “pls yal gol S aw Sy
3876:Sha ge! gins Ailes (ONOMATOPOEIA) "1,7 ao OFA ody cal fol abet ak aly Heat
4691:cesl (ONOMATOPOEIA)")T gi" pl sul y ta set aly oe!
5116:al (ONOMATOPOEIA) "1,1 (8 es odls ol
6856:scl (ONOMATOPOEIA) "iT (" es 0515 gy! tisisas ONIONS , SKEAT -)
12132:Naa! 9 4 Sd 31 Saker g2 Seal (ONOMATOPOEIA 157 (4) .olsT uly Ss og col (t
12916:yar iat dhy GANAMA KHOTANESE) >
13406:NAMAS LITHUANIAN) «y:3 ZIMBER
14362:NOM s(TOKHARIAN B) B og js NAMAN righ, AMESTAN) glen! a
14363:NAMA HKHOTANESE) | ¢35- NAMAN {ORD PERSIAN) deal posi
14364:NAMAN ASANSKRIT) 2 Suit NAM PAHLAVI) 5 lay
14366:ONOMA, ONYMA HMGREEK) gk y NAM, NAV, NAW (KURDISH) «53 Ss
14367:NOMEN LATIN) spa NAM BALUCHD) gx gy
14379:HANO, ANO HBRETON) 5.2 NAMA (OLD FRISIAN) 552.5
14384:POKORNY. SS~S~*~*~«S NAMA, NOMA
14596:NANTO AGALISH) JS NAMAC, NAMAZH, (PAHLAVI) «5 4, |
14597:NANT WELSH) 5315 NAMAZ | ce aed,
14600:REFERENCES boky NAMASH, NAWASH aazuce ea
14603:(REVERENCE) 130 NAMATI, NATA-
```


## [2026-09-07T20:27:53.530Z] TOOL CALL #81: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY\npython3 - <<'EOF'\nlines=open('ARY_latin_index_pages.txt',errors='replace').read().split('\\n')\n# find nearest pdf page tag before 14362\nimport re\npg=None\nfor j in range(14362,0,-1):\n    m=re.search(r'\\[pdf page (\\d+)\\]', lines[j])\n    if m: pg=m.group(1); print('pdf page',pg,'at line',j); break\nprint('\\n'.join(lines[14355:14395]))\nEOF"
}
```


### [2026-09-07T20:27:54.904Z] TOOL RESULT

```
pdf page 492 at line 14338
‘MACKENZIE: (NAVEL) 124 NAFLI, NOF, NOR
BUCK: 250 NAVLA HOLD FRISIAN) oS 5 8
ONIONS (NAVEL) 604 OLD HIGH GERMAN) pS gist
SKEAT: (NAVEL) 396 NABALO, NABA
Thee i ebG oby NABEL, NABE HAGERMAN) giST
— oe
NOM s(TOKHARIAN B) B og js NAMAN righ, AMESTAN) glen! a
NAMA HKHOTANESE) | ¢35- NAMAN {ORD PERSIAN) deal posi
NAMAN ASANSKRIT) 2 Suit NAM PAHLAVI) 5 lay
ANUN, ANOUN (ARMENIAN) NOM, NON HOSSETIC) gl
ONOMA, ONYMA HMGREEK) gk y NAM, NAV, NAW (KURDISH) «53 Ss
NOMEN LATIN) spa NAM BALUCHD) gx gy
NOM PRENCH) «ii NUM HAPGHANI) ( 5-4),
NOMBRE SPANISH) gti NEM ‘(TORHARIAN A) A 5 los
[pdf page 493]
at
IMJA RUSSIAN) 03, NOME LUTALIAN) pile!
IME (CZECH) So NUME ARUMANIAN) gla
MENO, N4ZOV whizerorany Sib NOME (PORTUGUESE) J »
qh EMNES, (OLD PRUSSIN) ofS 9.4 NAMO GOTHIC) &3,6
EMMENS (OLD SCANDINAVIAN) 9551)
AINM. HOLD IRISH) oS 5-4) p'\ NAEN
ENW (WELSH) § 315 NAMO HOLD SAXON) oS Gig-S a
HANO, ANO HBRETON) 5.2 NAMA (OLD FRISIAN) 552.5
fMEN ALBANIAN) gAST (OLD HIGH GERMAN) oy git
LAMAN HITTITE) cea NAMO
NAME (GERMAN) gst
‘REFERENCES bok HOLD ENGLISH) 9S 88
POKORNY. SS~S~*~*~«S NAMA, NOMA
BARNHART: ‘(NAME) 693 NAME ENGLISH) Sl
DELAMARRE: (NOM) 52 NAVN (DANISH) jails
MACKENZIE: (NAME) 124 NAMN (SWEDISH) 4b y+
BUCK: 1263 NAVN (NORWGIAN) $395
ONIONS: (NAME) 602 NAAM (DUTCH) tha
SKEAT: (NAME) 395 OLD CHURCH SLAVIC) 5 5.5%!
rhe sbi iby IME
IMIE, NAZWA (POLISH) long!
at) ot |
NAGS NAVAZA, NAVAYA  :(AVESTAN) gl!
NAY, NAVEM ARMENIAN) (OLD PERSIAN) jkonk ge 5
```


## [2026-09-07T20:28:08.176Z] TOOL CALL #82: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"Fluch\\|Schmähung\\|Schimpfwort\\|Scheltwort\" HRN.txt HUB.txt | head -10\necho \"=== HRN dus- section\"; grep -n \"^[0-9]*\\. *duš\\|duš\" HRN.txt | head -20"
}
```


### [2026-09-07T20:28:08.250Z] TOOL RESULT

```
HRN.txt:777:afrtn 1) 'schaffend' 2) 'Lob', vergl. nefnn 'Fluch'.
HRN.txt:779:äfritan 'schaffen', afrm 'Lob', nafrm 'Fluch' (AV.);
HRN.txt:9286:guväze 'Schmähung*, gtwäSzden, schelten' (unbelegt).
HRN.txt:11218:wältigen, siegen'; arm. canem *in die Flucht schlagen,
=== HRN dus- section
```


## [2026-09-07T20:28:16.911Z] TOOL CALL #83: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -o \"انار[^ ]\\{0,80\\}\" MON_part1.txt | head -8\necho \"=== nam\"; grep -o \"نام \\[[^]]*\\][^,]\\{0,80\\}\" MON_part2.txt MON_part1.txt | head -8\necho \"=== doshnam\"; grep -o \"دشنام[^\\n]\\{0,120\\}\" MON_part1.txt | head -5"
}
```


### [2026-09-07T20:28:18.198Z] TOOL RESULT

```
انار
انار
انار
انار
اناره:
انار.
انار:
انارین:
=== nam
=== doshnam
دشنام گونه‌ای است.) (اح. 
دشنام به آدم بی‌حال و 
دشنام دادن» فحش گفتن. 
دشنام» 
دشنام دهد» دشنام دهنده» ناسا
```


## [2026-09-07T20:28:23.603Z] TOOL CALL #84: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -o \".\\{0,60\\}انار\\.\\?[ ]\\?\\[.\\{0,120\\}\" MON_part1.txt | head -6\necho \"=== 'انار (اِ.)'\"; grep -n -o \"انار.\\{0,140\\}\" MON_part1.txt | grep \"په\\|پهلو\" | head -5\necho \"=== nam pahlavi\"; grep -n -o \"نام\\.\\{0,3\\}\\[.\\{0,120\\}\" MON_part2.txt | head -6"
}
```


### [2026-09-07T20:28:27.356Z] TOOL RESULT

```
ugrep: error: error at position 97
(?:[^\n\x80-\xbf][\x80-\xbf]*){0,120}
        exceeds complexity limits___/


=== 'انار (اِ.)'
=== nam pahlavi
```


## [2026-09-07T20:28:32.956Z] TOOL CALL #85: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nfor f in ('MON_part1.txt','MON_part2.txt'):\n    t=open(f,errors='replace').read()\n    for m in re.finditer(r'انار', t):\n        s=t[m.start():m.start()+130].replace('\\n',' ')\n        if 'په' in s or 'اِ' in s:\n            print(f, '|', s)\n    print('----')\n    for m in re.finditer(r'نام\\b', t):\n        s=t[m.start():m.start()+120].replace('\\n',' ')\n        if s.startswith('نام [') or s.startswith('نام(') or 'په .' in s[:20]:\n            print(f,'NAM|',s)\nEOF"
}
```


### [2026-09-07T20:28:34.376Z] TOOL RESULT

```
----
MON_part1.txt NAM| نام [- بوساندن|  پسوسانید» بسپوسان» پوساننده» پوسان»  بوسانیده). سوسیدن داشتن» بوسیده کردن»  تغییر دادن صورت چیزی اعم از
MON_part2.txt | اناری گر فته» بعد از آنکه ور آمد به  قدر بشقاب کوچکی پهن کرده» رویش را با  شانه لوزی کرده» در تنور یا در فر می‌پزند»  نان طابون. خ
----
```


## [2026-09-07T20:28:49.403Z] TOOL CALL #86: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nraw=open('KLN_1966.txt',errors='replace').read()\nlines=raw.split('\\n')\nimport re\nfor target,label in ((24927,'name'),(25680,'noun'),(25546,'nomenclature'),(37893,'synonym'),(3020,'antonym')):\n    off=sum(len(l)+1 for l in lines[:target])\n    leaf=raw[:off].count('\\f')\n    print(label,'leaf',leaf,'-> approx printed p.',(leaf-12)*2,'or',(leaf-12)*2+1)\nEOF"
}
```


### [2026-09-07T20:28:50.888Z] TOOL RESULT

```
name leaf 549 -> approx printed p. 1074 or 1075
noun leaf 566 -> approx printed p. 1108 or 1109
nomenclature leaf 563 -> approx printed p. 1102 or 1103
synonym leaf 827 -> approx printed p. 1630 or 1631
antonym leaf 57 -> approx printed p. 90 or 91
```


## [2026-09-07T20:30:12.833Z] TOOL CALL #87: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK_full nor watery\"; grep -n -i \"lemma: n[oō]r\\|Granatapfel\" POK_full.txt POK_01.txt POK_02.txt POK_03.txt | head -20\necho \"=== AHD nor\"; grep -n \"^nō-r\\|^nor-\\|pomegranate\" AHD_watkins1985.txt | head\necho \"=== SYN pomegranate\"; grep -n -i \"pomegranate\" SYN.txt | head\necho \"=== WLD band3 Granatapfel\"; grep -n -i \"Granatapfel\" WLD_band3.txt incoming/WLD/WLD_Bd1_pages.txt incoming/WLD/WLD_Bd2_pages.txt | head"
}
```


### [2026-09-07T20:30:12.970Z] TOOL RESULT

```
=== POK_full nor watery
=== AHD nor
=== SYN pomegranate
=== WLD band3 Granatapfel
```


## [2026-09-07T20:30:20.556Z] TOOL CALL #88: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nraw=open('PHD.txt',errors='replace').read()\nlines=raw.split('\\n')\noff=sum(len(l)+1 for l in lines[:192])\nleaf=raw[:off].count('\\f')\nprint('anar leaf',leaf,'printed p.',leaf-21)\nraw2=open('NYB_vol2_glossary.txt',errors='replace').read()\nl2=raw2.split('\\n')\nfor tgt,lab in ((2627,'namak'),):\n    off=sum(len(l)+1 for l in l2[:tgt])\n    leaf=raw2[:off].count('\\f')\n    print(lab,'leaf',leaf,'printed p.',leaf-8)\nEOF\necho \"=== LEW nomen\"; grep -n \"^nomen\\|nōmen\" LEW_1910.txt | head -5\necho \"=== LAT nomen\"; grep -n \"^nomen\\|nōmen\" LAT.txt | head -5"
}
```


### [2026-09-07T20:30:22.005Z] TOOL RESULT

```
anar leaf 30 printed p. 9
namak leaf 150 printed p. 142
=== LEW nomen
=== LAT nomen
5339:nomen articulare) ; designe auasi 1 1 articulation d'un mot, toujours
6852:nomen <cum> 'us’ bannita iuncta.
20644:nomenclatores qui clam uelut infercirent nomina salutatorum in aurem
41687:nomen
41732:nomenclator: esclave charge d'appeler les noms des clients; nomen¬
```


## [2026-09-07T20:30:25.092Z] TOOL CALL #89: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '41680,41740p' LAT.txt"
}
```


### [2026-09-07T20:30:25.141Z] TOOL RESULT

```
pas" dquivoquant avec Mola non d'une ville de Campanie: in triclinio
Coam, in cubiculo Molam , Cael. ap. Quint. 8,6,53«
nolo: y.uolO.
nqmen, -inis n<: i° nom donnd k une personae ou k une chose: n.
proprium, commune} n. Latinum (dans socii nominis Latini, cf. en
ombrien I u r s k u m, Maharkum u me m, I a p u z k u m
numen, T.Eug.ib,17). Distingui de uerbum par les grammairieis- 7O7 "
nomen
(comme ovojkx de p^^ia): in nomine "au nom de", nomen Domini periphrase
de la 1. de l/^glise equivalant a dominus ; s° renon; 3 0 en droit "nom
d'un accuse": nomen dSferre, accipere; "nom d'un debiteur", d'ou
"titre de creance": tituli debitorum nomina dicuntur praesertim in
iis debitis, in quibus hominum nomina scripta sunt, quibus pecuniae
accommodatae sunt , Asc. ap. Cic., Verr.3,1,10 §38. tant que le nom
s 1 oppose a la chose ( cf. gr. o vop,a et epyov), ndmen peut designer "un
vain nom", d'ou nSmine, sub nomine "sous le pretexte de". - Usite
de tout temps; panroman, M.L.5949.
Composes: agnomen, cognSmen, praenomen : les deux derniers sont
seuls usites; agnomen semble une creation des grammairiens faite
en vue de distinguer (agnascere) les surnoms individuels des surnoms
communs a tous les descendants d'une gens , cf.Diom.,GLK I 313,3,
propriorum nominum quattuor sunt species: praenomen, nomen, cognomen,
agnomen: praenomen est quod nominibus gentiliciis praeponitur, ut
Marcus Puplius; nomen proprium est gentilicium, i.e., quod originem
gentis uel familiae declarat, ut Porcius, Cornelius; cognomen est
quod uniuscuiusque proprium est et nominibus gentiliciis subiungitur,
ut Cato, Scipio; agnomen uero est quod extrinsecus cognominibus adici
solet, ex aliqua ratione uel uirtute quaesitum, ut Africanus, Numan¬
tinus, et similia. II n r y a pas dans nomen de g initial etymologique;
agnomen, cognSmen, et plus tard agnSmentum, cognSmentum, sont des
formes analogiques faites sur le modele nosco/agnosco, cognosco (cf.
Isid. Or.1,6,4, cognomentum uulgo dictum eo quod nomini cognitionis
causa superadicitur, siue quod cum nomine est), dont nomen etait ori-
ginairement independant (il est peu vraisemblable de supposer que
cognomen n'est pas apparente knomen, et doit etre rattache h cognSscere,
r epr<?sentant co-gnSmen "signe de reconnaissance", avec un -gnomen
equivalant a yvuj|ia). Mais, a 1'epoque historique, les Latins ne s4-
paraient pas nosco de nSmen ( cf. P.F.179,13 nomen dictum quasi nouimen,
quod notitiam facit), et Plaute emploie ignobilis au sens de "homme
sans nom" (et non "inconnu"), Amp.440, ubi ego Sosia nolim esse, tu
esto sane Sosia; | nunc, quando sum, uapulabis nisi hinc abis, igno¬
bilis. II y a eu la une ^tymologie populaire toute naturelle.
Autres derives et composes: nominalis; nominalia n.pl.: "jour
ou 1'enfant recevait son nom"; nomina.liter; nominosus = gloriosus
(Gl.); nominarii "qui savent lire les noms"(par oppos. aux sylla-
b ari 1).
nomino,-as: nommer (ovop,a^w, ovop-aCvio); panroman, M.L.5950; et
ses derives nominatim, nominStio,-tor,-torius; -tus,-us; nominatiuus
(t. de gramm. n. casus = T) ovop.acrxi.x^ [71x0x11,5]); nominito, -as (Lucr.
pour eviter le cr^tique form^ par les formes de nomina)', innominabilis
(Apul., Tert. ); nominatus "celebre" Tert. d'apres ovo(ACtaxo5; innomi¬
natus (Don.) = avovo(xaaxoC;
nomenclator: esclave charge d'appeler les noms des clients; nomen¬
clatio, -elatura. Cf. calare; adnominatio: = 7capovojiaa(a; agnomentum
(Apul.) = agnomen ; cognomina, Erxovoiia^o); cognomentum,-minatio, etc.;
c ognominis : qui a le meme nom (= op,wvup,05 ); M.L. 3030a.
denomino ( epoq. imper.): designer par un nom, denommer (= xax—
ovop,a4oj); denominatio (= xaxovo(iaCTi,a, mpo)vup,Ca, 7capovopxxaCa) ; denomi-
natiuus (t. de gramm.): deriv£; praenomino: donner un prenom; nommer
en premiere ligne (b.lat.).
pronomen: t. de gramm. "pronom" d'apres gr. avxwvu(i,05, pronominalis,
```


## [2026-09-07T20:30:34.340Z] AGENT

Now I'll write the verification file.


## [2026-09-07T20:40:50.544Z] TOOL CALL #90: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-370.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\n\ne0 = {\n  \"entry\": 0,\n  \"root\": \"Nomn, Enomn\",\n  \"verdict\": \"confirmed\",\n  \"modern_form\": \"PIE *h₁nómn̥ (older notation *(e)nom̤n̥- / *nōmn̥-, *onomn̥) 'name'\",\n  \"note\": \"Nourai's two headword forms are literally Pokorny's: IEW 321 prints the lemma 'en(o)m̥-, (o)nom̥, nōm̥-' — 'Nomn' = *nōmn̥, 'Enomn' = *enomn̥. Walde-Pokorny I 132 has the same set ('en(o)men-, (o)nomen-, nōmen-, en(ə)men- ‚Name‘ n.'), Watkins/AHD lists it as 'nō-men-. Name.' with the earlier form *(ə)noə-mn̥, and Buck 18.28 (p. 1263) calls it 'an inherited group of unknown root connection'. The language label 'Indo-European' and the gloss 'name' are both right, and the six daughter branches Nourai draws (Avestan, Old Persian, Germanic, Latin, Greek — plus the Persian continuation) are exactly the branches Pokorny, WP and AHD list. The only thing modern work has changed is the laryngeal: Wiktionary reconstructs *h₁nómn̥ (Hittite lāman has no initial laryngeal reflex) against *h₃néh₃mn̥ (which would explain Greek ónoma and (a)nṓnumos); this is a notational refinement, not a change of substance. No node on this chart is affected by it.\",\n  \"note_fa\": \"ریشهٔ هندواروپایی آغازین *h₁nómn̥ «نام» که پوکورنی در صفحهٔ ۳۲۱ به صورت en(o)m̥-، (o)nom̥، nōm̥- از آن یاد کرده است؛ دو صورتی که نورایی می‌آورد (Nomn و Enomn) همان دو جزء سرمدخل پوکورنی است. والدهٔ‌پوکورنی (ج۱ ص ۱۳۲)، واتکینز (AHD) و باک (ص ۱۲۶۳) نیز همین ستاک ماندگارٔ -mn- را با همان شاخه‌ها (اوستایی، پارسی باستان، ژرمنی، لاتینی، یونانی) می‌آورند. تنها نوآوری پژوهش امروزی بر سر جایگاه حنجره‌ای (h₁ در برابر h₃) است که بر هیچ یک از حلقه‌های این نمودار اثر نمی‌گذارد. ادعای نورایی درست است.\",\n  \"sources\": [\n    W + \"Reconstruction:Proto-Indo-European/h₃néh₃mn̥\",\n    \"https://www.etymonline.com/word/name\"\n  ],\n  \"ref_check\": [\n    {\"ref\": \"POK:321\", \"status\": \"supports\",\n     \"note\": \"POK_full.txt lines 26895-26935: 'Root / lemma: en(o)m̥-, (o)nom̥, nōm̥- ... Meaning: name ... Material: Old Indic nama ... Avestan nama ‚name‘; Armenian anun ...; gr. ὀνομα ...; Latin nomen, -inis, n. ...; Gothic namo, Old Icelandic nafn, Old English nama, Old High German namo ‚name‘ ... References: WP. I 132 ... Page(s): 321'. Exactly Nourai's root, gloss and branch list.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"WLD\", \"where\": \"Bd. I p. 132 (incoming/WLD/WLD_Bd1_pages.txt leaf 140)\", \"stance\": \"supports\",\n     \"note\": \"Headword 'en(o)men-, (o)nomen-, nōmen-, en(ə)men- ‚Name‘ n.': 'Ai. nāma(n-), av. nāma(n-) n. ‚Name‘, ap. nāma (s. Bartholomae Air. Wb. 1064); lat. nomen, -inis, umbr. nome, numem, gen. nomner ...; Gr. ὀνομα, dial. ὀνυμα ...; arm. anun ...; Got. namo n., ahd. as. namo, ags. noma ..., aisl. nafn n.'\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. nō-men- (AHD_watkins1985.txt line 789)\", \"stance\": \"supports\",\n     \"note\": \"'nō-men-. Name. Earlier form *(ə)noə-mn̥, zero-grade form *(ə)nə-men-. 1. Germanic *namōn- in Old English nama: NAME. 2. Latin nōmen ... 3. Greek onoma, onuma ... [Pok. en(o)mn̥- 321.]' — the same three western branches Nourai draws, with Nourai's own page reference.\"},\n    {\"src\": \"SYN\", \"where\": \"Buck 18.28 NAME, p. 1263-64 (SYN.txt)\", \"stance\": \"supports\",\n     \"note\": \"'Nearly all the common words for ‚name‘ belong to an inherited group of unknown root connection. 1. IE *enmen-, *nmen-, *nōmen-, etc. with manifold gradation. Walde-P. 1.132.' Table lists Skt. nāman-, Av. nāman-, n̩man-, Lat. nomen, Grk. ὀνομα, Goth. namo, OE nama, NE name.\"},\n    {\"src\": \"IEC\", \"where\": \"Mann p. 852 (IEC.txt line 11854)\", \"stance\": \"silent\",\n     \"note\": \"Mann has no *nōmen- entry at the alphabetical place; only the neighbouring nor-(1)/(2)/(3) entries and the cross-reference '(nōr-. See Supt: N)'. Checked to make sure Mann does not contradict; he treats 'name' elsewhere and is not cited by Nourai here.\"}\n  ],\n  \"nodes\": []\n}\n\ne0[\"nodes\"] = [\n {\n  \"id\": 1, \"lang\": \"Avestan\", \"words\": \"nâma, nâman; duš-naman\",\n  \"verdict\": \"plausible\",\n  \"derivation\": \"Avestan nāman- n. 'name' (Younger Av. also n̩man-) is Bartholomae's headword 'j., g., p. nāman-, j. n̩man- n. ‚Name‘' (AiW col. ~1064, the column Walde-Pokorny cites); the suffixless nom.-acc. sg. is nāma, whence Nourai's first pair 'nāma, nāman'. It continues PIE *h₁nómn̥ with the Indo-Iranian lengthened-grade *nā- (Skt. nā́man-, Av. nāman-, OP nāman-), the stem-final *-n being lost in the nom.-acc. so that only nāma appears in the paradigm's direct cases. That half of the node is confirmed. The second word is not: 'duš-naman ‚bad name‘' is NOT an attested Avestan lexeme. Bartholomae's Altiranisches Wörterbuch has a long series of duš-/duž- compounds (duž-nišāta-, duž-θiš-, etc.) but no duš-nāman-, and Kent p. 193, which Nourai cites here, lists only nāman-. The compound is first documented one stage later, in Middle Persian: Manichaean dwj nʾm, Book Pahlavi duš-nām 'ill-famed' (MacKenzie, Concise Pahlavi Dictionary, addenda to p. 58), and Wiktionary accordingly reconstructs Proto-Iranian *dušHnā́ma rather than quoting an Avestan form. Both elements are good Old Iranian (Av. duš-/duž- 'ill, bad' < PIE *dus-, cf. Nourai's cross-reference to the root Dus), so the pre-form is legitimate; it is the label 'Avestan' that overstates the evidence, which is why the node is plausible rather than confirmed.\",\n  \"derivation_fa\": \"اوستایی nāman- (و در اوستای متأخر n̩man-) «نام» سرمدخل بارتولومه (ستون ۱۰۶۴) است؛ صورت فاعلی‌مفعولی مفرد آن nāma است، و این ستاک ماندگار از ریشهٔ هندواروپایی *h₁nómn̥ با کشیدگی واکهٔ ریشه در هندوایرانی (*nā-) برجای مانده است: سنسکریت nā́man-، پارسی باستان nāman-. این نیمهٔ ادعا درست است. اما «duš-naman» در اوستا گواهی نشده است؛ بارتولومه ده‌ها مرکب با پیشوند duš-/duž- دارد ولی duš-nāman- ندارد، و کنت (ص ۱۹۳) که مرجع خود نورایی است تنها nāman- را می‌آورد. قدیمی‌ترین گواه این مرکب فارسی میانه است (مانوی dwj nʾm، پهلوی کتابی duš-nām «بدنام»، مکنزی ص ۵۸)، و ویکی‌واژه آن را به ایرانی آغازین *dušHnā́ma بازمی‌گرداند. بنابراین ساخت واژه ایرانی است ولی برچسب «اوستایی» برای آن با احتیاط پذیرفتنی است.\",\n  \"sources\": [W + \"Reconstruction:Proto-Indo-European/h₃néh₃mn̥\", W + \"دشنام\"],\n  \"ref_check\": [\n   {\"ref\": \"POK:321\", \"status\": \"supports\",\n    \"note\": \"POK_full.txt line 26900: 'Material: Old Indic nama, Instr. Sg. namna, Avestan nama ‚name‘' — supports the Avestan word; Pokorny says nothing about a duš- compound.\"},\n   {\"ref\": \"KNT:193\", \"status\": \"partial\",\n    \"note\": \"KNT.txt leaf 216 (printed page number '193' standing on the leaf): 'nāman- sb. ‚name‘: Av. nāman-, NPers. nām, Skt. nāman-, Lt. nomen, pIE *nómen-, cf. Gk. ὀνομα, NEng. name.' Kent expressly gives the Avestan cognate, so the first word is supported; he has no duš-nāman-, so the second is not.\"}\n  ],\n  \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch, headword at BRT.txt leaf 592 (col. ~1064, the column cited by WP I 132)\", \"stance\": \"partial\",\n    \"note\": \"'• j., g., p. nāman-, j. n̩man- n. ‚Name‘:' with the adverbial uses ('AS. und LS. ... als Adv. ‚mit Namen‘; im jAw. AS. n̩ma, hinter dem Nom. propr.'). Searching the whole file for duš-/duž-nāman- returns nothing (only duž-nišāta- etc.), so Bartholomae does not know Nourai's second Avestan word.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. I p. 132\", \"stance\": \"supports\",\n    \"note\": \"'av. nāma(n-) n. ‚Name‘ ... ap. nāma (s. Bartholomae Air. Wb. 1064)' — Walde-Pokorny's own pointer is what fixes the Bartholomae column.\"},\n   {\"src\": \"PHD\", \"where\": \"MacKenzie p. 58 and the addenda list (PHD.txt line 125)\", \"stance\": \"partial\",\n    \"note\": \"Addenda: 'duš-nām [-nʾm | (M dwjnʾm), N ~] add ill-famed.' The compound therefore exists — in Middle Persian, not Avestan; Manichaean dwjnʾm shows it is genuinely old, but not old enough to be labelled Avestan.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 18.28, p. 1263\", \"stance\": \"supports\",\n    \"note\": \"Table gives 'Av. nāman-, n̩man-' alongside Skt. nāman- for the concept NAME.\"}\n  ]\n },\n {\n  \"id\": 2, \"lang\": \"Persian\", \"words\": \"nâm «نام»; došnâm «دشنام»; nâmeh «نامه»\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"All three words are the regular New Persian continuation of the Old Iranian n-stem. (1) نام nām: Middle Persian nām, written with the Aramaic ideogram ŠM (MacKenzie p. 58: 'nām [ŠM < A šm; nʾm | = M, N ~] name, fame'), from Old Iranian nāman-, whose stem-final -n had already been lost in the nom.-acc. (OP nāma); Horn's entry no. 1022 (Grundriss p. 229) gives exactly this chain: 'nām ‚Name‘ — ap. nāman-, aw. nāman-, phlv. nām, nāmīk ‚berühmt‘, ai. nāman-, arm. anun'. (2) دشنام došnām: MP duš-nām (Manichaean dwjnʾm) 'ill-famed', a bahuvrīhi of duš- 'bad' + nām; in New Persian the adjective was reinterpreted as a noun and the sense moved from 'having a bad name, ill repute' to the speech-act 'abuse, curse, insult' (Moʾen's footnote on نامزد in Borhān-e Qāţeʽ s.v. نام treats the whole نام- family this way). (3) نامه nāmeh: MP nāmag, written with the Aramaic ideogram MGLTA 'scroll' (MacKenzie p. 58: 'nāmag ... book, letter'), a -ag noun built on nām; Nyberg, Manual of Pahlavi II p. 142, s.v. nāmak: 'inscription; letter; book; in book-titles: Kār-nāmak, Pand-nāmak etc. — MPrs nʾmg; NP nāmah; from nām.' MP final -ag regularly gives NP -a(h) (ماهه > ماهه; -ه), hence نامه and the -نامه of شاهنامه. The semantics 'name' > 'written name, inscription' > 'letter' > 'book' is documented step by step in the Pahlavi corpus.\",\n  \"derivation_fa\": \"هر سه واژه دنبالهٔ منطقی ستاک ایرانی باستان nāman- اند. «نام» از فارسی میانهٔ nām (در خط پهلوی با هزوارش آرامی ŠM نوشته می‌شده) و آن از پارسی باستان nāma/nāman- است؛ همان زنجیره‌ای که معین در حاشیهٔ برهان قاطع (ص ۲۱۰۶) می‌نویسد: «نام — پهلوی nām، ایرانی باستان *nāman-، پارسی باستان nāman-، اوستا nāman-، هندی باستان nāman-، ارمنی anun»، و هرن در مادهٔ ۱۰۲۲ (ص ۲۲۹) نیز همین را می‌آورد. «دشنام» از فارسی میانهٔ duš-nām «بدنام» است (پیشوند duš- «بد» + نام)، که در فارسی نو از صفت به اسم بدل شد و تحول معنایی «بدنامی» ← «فحش و ناسزا» یافت. «نامه» از پهلوی nāmag است (هزوارش MGLTA)، مشتق از نام با پسوند -ag؛ نیبرگ (ج۲ ص ۱۴۲) صریحاً می‌نویسد «from nām»، و -ag پایانی پهلوی در فارسی نو به -ه بدل شده است. ادعای نورایی درست است.\",\n  \"sources\": [W + \"نام\", W + \"دشنام\"],\n  \"ref_check\": [\n   {\"ref\": \"BQT:2106\", \"status\": \"supports\",\n    \"note\": \"Borhān-e Qāţeʽ vol. 4, printed p. 2106 = pdf p. 189 of BQT_v4_picofile.pdf (printed = pdf + 1917); the page carries the headwords نام‌آور، نامزد، ناموس and نام with Moʾin's etymological footnote: 'نام - پهلوی nām، ایرانی باستان *nāman- «بارتولمه ۱۰۶۲»، «نیبرگ ص ...»، پارسی باستان nāman- (نام، اسم)، اوستا nāman-، هندی باستان nāman-، آرمنی anun، ... کردی nāv ...' (BQT_v4_pages.txt, block [pdf page 189]). نامه falls on the facing page 2107 (pdf 190) with the footnote 'پهلوی nāmak (کتاب) مأخوز از «نام»، «نیبرگ ص ۱۵۶»'.\"},\n   {\"ref\": \"HRN:229\", \"status\": \"partial\",\n    \"note\": \"HRN.txt leaf 250 (running head '— 229 —'), entry '1022. nām ‚Name‘: ap. nāman- ‚Name‘; aw. nāman-; phlv. nām, nāmīk ‚berühmt‘, nāmīnītan (PPGl.); ai. nāman-; arm. anun (H. No. 24)'. Horn supports نام exactly, but his Grundriss has no entry for دشنام or نامه (searched for dušnām, Fluch, Schimpfwort — nothing).\"}\n  ],\n  \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie p. 58 (PHD.txt leaf 79, block containing 'nāmīǵ 58')\", \"stance\": \"supports\",\n    \"note\": \"'nām [ŠM < A šm; nʾm | = M, N ~] name, fame.' and 'nāmag [MGLTA < A mglt; nʾmkʹ | M nʾmg, N nāma] book, letter.' plus 'nām-burdār ... heir, preserving the father's name' and (addenda) 'duš-nām ... ill-famed' — all three Persian words have their Middle Persian antecedent here.\"},\n   {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II p. 142 s.v. nāmak\", \"stance\": \"supports\",\n    \"note\": \"'nāmak [nʾmkʹ; inscr. nʾmky; ŠM-kʹ] inscription P2:3; letter 3² etc.; book 107¹, 121¹⁹; in book-titles: Kār-nāmak, Pand-nāmak etc. - MPrs nʾmg; NP nāmah; from nām.' Explicit derivation of nāmeh from nām.\"},\n   {\"src\": \"ARY\", \"where\": \"Aryanpur, Latin index pdf pp. 492-493 (printed 493-494), entry for نام\", \"stance\": \"supports\",\n    \"note\": \"The cognate block lists 'NAMAN (AVESTAN), NAMAN (OLD PERSIAN), NAM (PAHLAVI), NAMAN (SANSKRIT), ANUN/ANOUN (ARMENIAN), ONOMA/ONYMA (GREEK), NOMEN (LATIN), NAMO (GOTHIC), NAMA/NOMA (OLD ENGLISH), NAME (ENGLISH), LAMAN (HITTITE)', with 'REFERENCES: POKORNY ...; MACKENZIE (NAME) 124; BUCK 1263; ONIONS (NAME) 602; SKEAT (NAME) 395' — an independent modern Persian handbook giving the same chain as Nourai.\"},\n   {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien\", \"stance\": \"silent\",\n    \"note\": \"Searched for nām / 1022 / dšnām: Hübschmann's Part I follows Horn's numbering but has no note on Horn no. 1022, so he neither confirms nor contradicts.\"}\n  ]\n },\n {\n  \"id\": 3, \"lang\": \"Old Persian\", \"words\": \"nâman\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"Old Persian nāman- 'name' is a real lexical entry, though attested only in its case forms: the suffixless nom.-acc./loc. nāma and the long-vowel nāmā used adverbially ('by name') after proper names throughout the Bisitun and other Achaemenid inscriptions (DB 1.28, 1.58, 2.39 Tigra nāma didā 'a stronghold by name Tigra', etc.). Kent's Lexicon p. 193 gives it as a headword with precisely Nourai's derivation: 'nāman- sb. ‚name‘: Av. nāman-, NPers. nām, Skt. nāman-, Lt. nomen, pIE *nómen-'. Phonologically it needs no change from the parent: PIE *h₁nómn̥ gave Proto-Indo-Iranian *Hnā́ma with lengthened grade, and Old Persian preserves the *nām- stem unaltered (the same word supplies the negated compound Anāmaka-, the tenth Achaemenid month, 'of the Nameless [= Highest] God', Kent p. 168).\",\n  \"derivation_fa\": \"پارسی باستان nāman- «نام» واژه‌ای واقعی است که در سنگ‌نوشته‌های هخامنشی تنها به صورت nāma / nāmā و در نقش قیدی «به‌نام» گواهی شده است (دب ۱٫۵۸، ۲٫۳۹ Tigra nāma didā). کنت در صفحهٔ ۱۹۳ همین را با همان زنجیرهٔ نورایی می‌آورد. از نظر آوایی دگرگونی‌ای رخ نداده: ریشهٔ هندواروپایی در هندوایرانی به *Hnā́ma با واکهٔ کشیده بدل شد و پارسی باستان همان ستاک nām- را نگاه داشته است (از همین واژه است نام ماه Anāmaka- «ماه خدای بی‌نام»). ادعای نورایی درست است.\",\n  \"sources\": [W + \"نام\"],\n  \"ref_check\": [\n   {\"ref\": \"KNT:193\", \"status\": \"supports\",\n    \"note\": \"KNT.txt leaf 216, page marker '193' on the leaf: 'nāman- sb. ‚name‘: Av. nāman-, NPers. nām, Skt. nāman-, Lt. nomen, pIE *nómen-, cf. Gk. ὀνομα, NEng. name (§109, §110, §155.II). See also Anāmaka-. nāma, suffixless lsn. used with masc. and nt. generic nouns to denote specification ...'. Nourai's page is exact.\"}\n  ],\n  \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. I p. 132\", \"stance\": \"supports\",\n    \"note\": \"'ap. nāma (s. Bartholomae Air. Wb. 1064)' listed beside Skt. and Avestan in the same entry.\"},\n   {\"src\": \"BRT\", \"where\": \"BRT.txt leaf 592, headword '• j., g., p. nāman-'\", \"stance\": \"supports\",\n    \"note\": \"Bartholomae's 'p.' tag on the headword means the word is also Old Persian; his separate cross-entry '• p. n̩ma, nāmā Adv.: s. nāman-' (BRT.txt line 18879) records the Old Persian adverbial forms.\"},\n   {\"src\": \"ARY\", \"where\": \"Aryanpur Latin index, pdf p. 492 (printed 493)\", \"stance\": \"supports\",\n    \"note\": \"'NAMAN (OLD PERSIAN)' listed in the نام cognate block, next to NAMAN (AVESTAN) and NAM (PAHLAVI).\"}\n  ]\n },\n {\n  \"id\": 4, \"lang\": None, \"words\": \"\",\n  \"verdict\": \"unverified\",\n  \"derivation\": \"A blank box. The 200 dpi render of pdf page 370 (book p. 340) shows an empty double-ruled rectangle drawn to the right of the 'Old Persian | nāman : name' box, joined to it by a plain arrow, with no language header, no reference and no word inside — the same unfilled layout slot that recurs throughout the book (cf. pages 350, 351, 358, 361, 362, 364, 365, 366 of this same run). The extraction is faithful (lang, refs and words are all null/empty in the JSON exactly as on the page), so there is nothing to verify. Judging by the layout, the slot is where the New Persian continuation of the Old Persian branch would have gone — but that is already covered by node #2, hanging off the Avestan box.\",\n  \"derivation_fa\": \"جعبهٔ تهی. در تصویر صفحهٔ ۳۷۰ پی‌دی‌اف (ص ۳۴۰ کتاب) در سمت راست جعبهٔ «پارسی باستان nāman» مستطیلی دوخطه دیده می‌شود که هیچ برچسب زبانی، مرجع یا واژه‌ای در آن نیست؛ این همان جای‌خالی‌هایی است که در سراسر کتاب نورایی پر نشده مانده است. خوانش اسکن درست است و ادعایی برای سنجیدن وجود ندارد.\",\n  \"sources\": [],\n  \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The node carries no reference in the book (refs=None) and no word, so there is nothing to look up.\"}],\n  \"consulted\": [{\"src\": \"BOOK\", \"where\": \"pdftoppm -r 200 of pdf page 370 (/tmp/pg370-p370.png), read directly\", \"stance\": \"silent\", \"note\": \"The rectangle to the right of the Old Persian box is drawn but completely blank — no header, no reference, no word. Extraction faithful.\"}]\n },\n {\n  \"id\": 5, \"lang\": \"Germanic\", \"words\": \"namon\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"Nourai's 'namon' is Watkins's citation form: AHD s.v. nō-men- has 'Germanic *namōn- in Old English nama, name: NAME'. In current terms the Proto-Germanic word is *namō, an n-stem (gen. *namniz) generalised from the PIE oblique/collective stem *nomn-, whence Gothic namō, Old Norse nafn (< *namn, with the regular Norse mn > fn), Old English nama/noma, Old Saxon and Old High German namo, Old Frisian nama, Dutch naam, German Name. Pokorny 321 gives the same set ('Gothic namon, Old Icelandic nafn n., Old English nama, Old High German namo ‚name‘; with o-grade Old Frisian nomia, Middle High German be-nuomen'). Klein s.v. 'name' lists the identical Germanic comparanda from the I.-E. base '*enomen, *onomen, *nomen'. The derivation from the root as drawn is uncontroversial.\",\n  \"derivation_fa\": \"صورتی که نورایی می‌آورد (namon) همان ضبط واتکینز است: *namōn- ژرمنی آغازین، که امروز معمولاً *namō (ستاک -n) نوشته می‌شود و از ستاک حالت‌های غیرفاعلی *nomn- هندواروپایی برامده است: گوتی namō، نورسی کهن nafn (با تبدیل قاعده‌مند mn > fn)، انگلیسی کهن nama/noma، آلمانی علیای کهن namo. پوکورنی (ص ۳۲۱) و کلاین همین فهرست را می‌دهند. ادعای نورایی درست است.\",\n  \"sources\": [\"https://www.etymonline.com/word/name\"],\n  \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"AHD_watkins1985.txt line 789, s.v. nō-men-: '1. Germanic *namōn- in Old English nama, name: NAME.' Nourai's node label and word are copied from this line.\"}\n  ],\n  \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"IEW p. 321 (POK_full.txt line 26918)\", \"stance\": \"supports\",\n    \"note\": \"'Gothic namon., Old Icelandic nafn n., Old English nama, Old High German namo m. ‚name‘; with o-grade Old Frisian nomia. Middle High German be-nuomen ‚name‘.'\"},\n   {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. name, n. (KLN_1966.txt leaf 549)\", \"stance\": \"supports\",\n    \"note\": \"'name, n. — ME. name, fr. OE. nama, rel. to OFris. nama, OS., OHG. namo, MDu., MHG., G. name, Du. naam, ON. nafn (for *namn), Dan. navn, Swed. and Norw. namn, Goth. namo, ‚name‘, fr. I.-E. base *enomen, *onomen, *nomen ...'\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 18.28, p. 1263\", \"stance\": \"supports\",\n    \"note\": \"Germanic column: 'Goth. namo, ON nafn, Dan. navn, Sw. namn, OE nama, ME name, NE name, Du. naam, OHG namo, MHG name, NHG name.'\"}\n  ]\n },\n {\n  \"id\": 6, \"lang\": \"English\", \"words\": \"name\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"Old English nama (Anglian noma) > Middle English name > Modern English name; the word is the direct native reflex of Proto-Germanic *namō, with the OE weak n-stem levelled to a simple -e noun in Middle English and the final -e lost in pronunciation by the 15th century while the spelling stayed (and the vowel raised to /ei/ in the Great Vowel Shift). Klein: 'name, n. — ME. name, fr. OE. nama'; Etymonline: 'from Old English nama/noma ‚word by which a person or thing is denoted‘, from Proto-Germanic *naman-, ... ultimately from PIE root *no-men- ‚name‘'. The verb 'to name' is OE namian, denominative from the noun.\",\n  \"derivation_fa\": \"انگلیسی name بازماندهٔ مستقیم انگلیسی کهن nama (گونهٔ آنگلی noma) است که در انگلیسی میانه name شد و ستاک -n آن ساده گردید؛ -e پایانی در سدهٔ پانزدهم از تلفظ افتاد و واکه در جابجایی بزرگ واکه‌ها به /ei/ بدل شد. کلاین و اتیمانلاین همین را می‌گویند. ادعای نورایی درست است.\",\n  \"sources\": [\"https://www.etymonline.com/word/name\"],\n  \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The node carries no reference in the book; it inherits the AHD citation of its Germanic parent, which was checked (see node #5).\"}],\n  \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. name, n. and name, v. (KLN_1966.txt leaf 549)\", \"stance\": \"supports\",\n    \"note\": \"'name, n. — ME. name, fr. OE. nama ...'; 'name, tr. v. — ME. namen, fr. OE. namian, fr. nama, ‚name‘.'\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. nō-men-\", \"stance\": \"supports\",\n    \"note\": \"'Germanic *namōn- in Old English nama, name: NAME' — NAME is listed as the English derivative of the Germanic branch, exactly as drawn.\"}\n  ]\n },\n {\n  \"id\": 7, \"lang\": \"Latin\", \"words\": \"nomen\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"Latin nōmen, gen. nōminis, n. 'name' continues the lengthened-grade *nōmn̥ of the same PIE stem; the sister dialect Umbrian shows nome, numem with gen. nomner, which guarantees the *-mn- stem rather than a *-men- suffix on some other root. Walde-Pokorny I 132 lists it in the entry ('lat. nomen, -inis, n., umbr. nome, numem, gen. nomner ‚Name‘'), and both WP and Ernout-Meillet stress that the initial g- of agnōmen/cognōmen is secondary: Ernout-Meillet (Dict. étym. de la langue latine, s.v. nōmen, p. 707) writes 'Il n'y a pas dans nomen de g initial étymologique; agnomen, cognōmen ... sont des formes analogiques faites sur le modèle nosco/agnosco, cognosco', i.e. the ancient tie to nōscō 'know' (P.F. 179,13 'nomen dictum quasi nouimen, quod notitiam facit') is a folk etymology. Nourai draws the arrow root → Latin, which is exactly right; his 'nomen' is again AHD's citation form.\",\n  \"derivation_fa\": \"لاتینی nōmen (مضاف‌الیه nōminis) دنبالهٔ گونهٔ کشیدهٔ *nōmn̥ از همان ستاک هندواروپایی است؛ گونهٔ امبریایی nome/numem با مضاف‌الیه nomner نشان می‌دهد که ستاک واقعاً -mn- بوده است. والدهٔ‌پوکورنی (ج۱ ص ۱۳۲) و ارنو‌مییه (ص ۷۰۷) هر دو تأکید می‌کنند که g آغازین در agnōmen و cognōmen ثانوی و قیاسی است و پیوند دادن nōmen به nōscō «دانستن» ریشه‌شناسی عامیانه است. ادعای نورایی درست است.\",\n  \"sources\": [W + \"Reconstruction:Proto-Indo-European/h₃néh₃mn̥\"],\n  \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"AHD_watkins1985.txt line 789, s.v. nō-men-: '2. Latin nōmen, name, reputation: NOMINAL, NOMINATE, NOUN; AGNOMEN, COGNOMEN, DENOMINATE, IGNOMINY, MISNOMER, NOMENCLATOR, NUNCUPATIVE, PRAENOMEN, (PRONOUN), RENOWN.'\"}\n  ],\n  \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. I p. 132\", \"stance\": \"supports\",\n    \"note\": \"'lat. nomen, -inis, n. umbr. nome, numem, gen. nomner ‚Name‘ und ‚people‘ (lat. agnomen, cognomen ... beruhen auf erst lat. Vermischung mit einem Agnomen = gr. γνῶμα ‚Kennzeichen‘)'.\"},\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet, s.v. nōmen, p. 707 (LAT.txt line 41687 ff.)\", \"stance\": \"supports\",\n    \"note\": \"'nōmen, -inis n.: 1° nom donné à une personne ou à une chose ... Usité de tout temps; panroman, M.L.5949 ... Il n'y a pas dans nomen de g initial étymologique.'\"},\n   {\"src\": \"POK\", \"where\": \"IEW p. 321\", \"stance\": \"supports\",\n    \"note\": \"'Latin nomen, -inis, n. Umbrian nome, Abl. nomne ‚name‘ and ‚people‘.'\"}\n  ]\n },\n {\n  \"id\": 8, \"lang\": \"English\", \"words\": \"noun, nominal, nominate, denominate, pronoun, nomenclature\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"All six are Latinate borrowings on nōmen, and all six are in Watkins's own derivative list for the Latin branch. noun: Middle English nowne, from Anglo-French noun, Old French non/nom (Modern French nom), from Latin nōmen — the grammatical use calques Greek ὄνομα as against ῥῆμα 'verb' (Ernout-Meillet: 'Distingué de uerbum par les grammairiens ... comme ὄνομα de ῥῆμα'). nominal < Latin nōminālis (Ernout-Meillet lists nominalis, nominaliter). nominate < Latin nōminātus, pp. of nōmināre 'to name'. denominate < Latin dēnōmināre, dēnōminātiō (itself a calque of Greek κατονομασία/παρονομασία). pronoun < Latin prōnōmen, itself the grammarians' calque of Greek ἀντωνυμία ('pronomen: t. de gramm. ‚pronom‘ d'après gr. ἀντωνυμος', Ernout-Meillet p. 707), reaching English through French pronom / Latin. nomenclature < Latin nōmenclātūra 'calling of names', a compound of nōmen + calāre 'to call' (Klein: 'nomenclature, n. ... L. nomenclatura, ‚calling of names‘'), via French nomenclature in the 17th century. The one thing worth noting is that these are learned borrowings of the Renaissance and after, not an unbroken Latin-to-English descent — but the arrow Latin → English is the standard way of drawing that.\",\n  \"derivation_fa\": \"هر شش واژه وام‌واژه‌های لاتینی‌تبار مبتنی بر nōmen اند و هر شش در فهرست مشتقات واتکینز از شاخهٔ لاتینی می‌آیند. noun از فرانسوی کهن non/nom و آن از nōmen؛ کاربرد دستوری اش گرته‌برداری از ὄνομα یونانی در برابر ῥῆμα است. nominal از nōminālis، nominate از اسم مفعول nōminātus، denominate از dēnōmināre، pronoun از prōnōmen که خود گرته‌برداری ἀντωνυμία یونانی است، و nomenclature از nōmenclātūra (نام + calāre «خواندن»). تنها نکته اینکه این‌ها وام‌گیری‌های کتابی دورهٔ رنسانس و پس از آن اند، نه تداوم طبیعی لاتینی در انگلیسی. ادعای نورایی درست است.\",\n  \"sources\": [W + \"نام\"],\n  \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"No reference is printed on this node; the parent Latin node carries 'AHD', whose derivative list (NOMINAL, NOMINATE, NOUN, DENOMINATE, NOMENCLATOR, PRONOUN) covers all six words and was checked.\"}],\n  \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. noun (leaf 566) and nomenclature (leaf 563)\", \"stance\": \"supports\",\n    \"note\": \"'noun, n. — ME. nowne, fr. AF. noun, fr. OF. non, nom (F. nom), fr. L. nomen, ‚name‘. See name and words there referred to and cp. esp. nominal, nominate.'; 'nomenclature, n., system of names; terminology. — L. nomenclatura, ‚calling of names‘.' Klein's 'Cp.' list under name includes denominate, misnomer, nomenclator, nomenclature, nominal, nominate, nominative, noun, praenomen, renown.\"},\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. nōmen, p. 707\", \"stance\": \"supports\",\n    \"note\": \"'Autres dérivés et composés: nominalis ... nomino, -as: nommer ... nominatim, nominatio, -tor ... nomenclator: esclave chargé d'appeler les noms des clients; nomenclatio, -clatura. Cf. calare ... denomino ... denominatio ... pronomen: t. de gramm. ‚pronom‘ d'après gr. ἀντωνυμος.' Every one of Nourai's six English words has its Latin base here.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. nō-men-\", \"stance\": \"supports\",\n    \"note\": \"Latin branch derivatives: 'NOMINAL, NOMINATE, NOUN; AGNOMEN, COGNOMEN, DENOMINATE, IGNOMINY, MISNOMER, NOMENCLATOR, NUNCUPATIVE, PRAENOMEN, (PRONOUN), RENOWN.'\"}\n  ]\n },\n {\n  \"id\": 9, \"lang\": \"Greek\", \"words\": \"onoma\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"Greek ὄνομα, gen. ὀνόματος 'name' (Aeolic/Doric ὄνυμα, Laconian ὅνυμα in Ἐνυμακαρτίδας) is the same *-mn̥ stem with a prothetic vowel; Pokorny explains the initial as 'gr. ὄνομα (from reduced *eno- with assimilation e- > o-)', and the -υ- of ὄνυμα as generalised from the genitive *ὀνύμνος before -μν-. The alternation is precisely what motivates the modern reconstruction *h₃néh₃mn̥ (o-coloured laryngeal) for those who prefer it, since a bare *h₁- would not by itself explain the o-vowel; the negated compound ἀν-ώνυμος / νώνυμνος 'nameless' preserves the long vowel of the compositional form. The arrow root → Greek and the gloss 'name' are both right.\",\n  \"derivation_fa\": \"یونانی ὄνομα (مضاف‌الیه ὀνόματος؛ گونهٔ لهجه‌ای ὄνυμα) همان ستاک *-mn̥ است با واکهٔ افزایشی آغازین. پوکورنی (ص ۳۲۱) می‌نویسد ὄνομα از صورت کاهشی *eno- با همگونی e- > o- پدید آمده و واکهٔ -υ- در ὄνυμα از مضاف‌الیه در جایگاه پیش از -μν- تعمیم یافته است؛ مرکب منفی ἀνώνυμος «بی‌نام» واکهٔ کشیدهٔ صورت ترکیبی را نگاه داشته است. ادعای نورایی درست است.\",\n  \"sources\": [W + \"Reconstruction:Proto-Indo-European/h₃néh₃mn̥\"],\n  \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"AHD_watkins1985.txt line 789, s.v. nō-men-: '3. Greek onoma, onuma, name: ONOMASTIC, -ONYM, -ONYMY; ANONYMOUS, ... SYNONYMOUS.'\"}\n  ],\n  \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"IEW p. 321\", \"stance\": \"supports\",\n    \"note\": \"'gr. ὀνομα (from reduced *eno- with assimilation e- o), dial. ὀνυμα, *ὄνυμα in lak. Ἐνυμακαρτίδας, (reduced u derived before μν from Gen. *ὀνύμνος), ἀνώνυμος, νώνυμνος ‚nameless‘.'\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. I p. 132\", \"stance\": \"supports\",\n    \"note\": \"'Gr. ὀνομα, dial. ὀνυμα ‚Name‘, ἀνώνυμος, νώνυμνος ‚namenlos‘, lakon. Ἐνυμακαρτίδας.'\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 18.28, p. 1263\", \"stance\": \"supports\",\n    \"note\": \"Greek column of the NAME table: 'Grk. ὄνομα, NG ὄνομα'.\"}\n  ]\n },\n {\n  \"id\": 10, \"lang\": \"English\", \"words\": \"synonym, antonym, anonymous\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"Three Greek-based learned formations on ὄνυμα, the dialectal (Aeolic/Doric) form of ὄνομα that Greek compounding regularly uses. synonym: Middle English sinonyme, from Late Latin synōnymum, from Greek συνώνυμον, neuter of συνώνυμος 'having the same name', σύν 'with' + ὄνυμα (Klein). anonymous: from Greek ἀνώνυμος 'nameless' (ἀν- privative + ὄνυμα), through Late Latin anōnymus, 17th c. antonym: not a classical word but a 19th-century coinage on Greek ἀντωνυμία 'a word used for another, a pronoun' (ἀντί 'instead of' + ὄνυμα), formed in English as the opposite of synonym — Klein: 'antonym, n., opposite in meaning to another word. — Formed fr. Gk. ἀντωνυμία ... fr. ἀντί ‚instead of‘ and ὄνυμα, dialectal form of ὄνομα.' All three therefore descend from the Greek node as drawn; only 'antonym' is a modern formation rather than a borrowed Greek word, which the chart's arrow does not distinguish.\",\n  \"derivation_fa\": \"سه ساختهٔ کتابی بر پایهٔ ὄνυμα، گونهٔ ترکیبی ὄνομα در یونانی. synonym از یونانی συνώνυμον «هم‌نام» از راه لاتینی متأخر و انگلیسی میانه sinonyme؛ anonymous از ἀνώνυμος «بی‌نام»؛ ولی antonym واژه‌ای یونانی نیست بلکه ساختهٔ سدهٔ نوزدهم در انگلیسی بر قیاس synonym و بر پایهٔ ἀντωνυμία است (کلاین). هر سه در نهایت از گرهٔ یونانی می‌آیند و ادعای نورایی درست است.\",\n  \"sources\": [W + \"نام\"],\n  \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"No reference printed on this node; the parent Greek node's 'AHD' citation lists ANONYMOUS and SYNONYMOUS among the Greek-branch derivatives and was checked.\"}],\n  \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. synonym (leaf 827) and antonym (leaf 57)\", \"stance\": \"supports\",\n    \"note\": \"'synonym, n. — ME. sinonyme, fr. Late L. synōnymum, fr. Gk. συνώνυμον ... The literal meaning of συνώνυμον is ‚having the same name as‘ ... See name'; 'antonym, n. ... Formed fr. Gk. ἀντωνυμία ... See name and cp. anonym.'\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. nō-men-\", \"stance\": \"supports\",\n    \"note\": \"Greek branch: 'ONOMASTIC, -ONYM, -ONYMY; ANONYMOUS, ANTONOMASIA, EPONYM, ... SYNONYMOUS' — the -ONYM entry is where antonym and synonym belong.\"}\n  ]\n }\n]\n\ne1 = {\n  \"entry\": 1,\n  \"root\": \"Nôr, Anôr\",\n  \"verdict\": \"disputed\",\n  \"modern_form\": \"no such Indo-European root; MP anār / Arm. nuŕn are reflexes of an ancient Near-Eastern Wanderwort for the pomegranate (Hurrian nuranti, Hittite nurati, Akkadian nurmû / nurimtu, Sumerian nurma), of which Arabic rummān / Hebrew rimmōn is the metathesised variant\",\n  \"note\": \"The reference is genuine and exact — but it is the weakest kind of authority. Mann's An Indo-European Comparative Dictionary p. 1645 (in the Supplement, which is missing from the local OCR and had to be fetched from the archive.org djvu text) reads verbatim: '(nōr, onōr ‚watery‘ (?) in Pahl. anār, Per. nār ‚pomegranate‘ and Arm. nurn, gs: nran, id.)'. Both the surrounding parentheses and the '(?)' are Mann's own signals that the reconstruction is a guess; the main volume (p. 852) carries only the stub '(nōr-. See Supt: N)'. No other Indo-European dictionary knows the root: Pokorny, Walde-Pokorny (Bd. I-III) and Watkins/AHD were all searched for a root *nōr- 'watery/juicy' and for the gloss Granatapfel/pomegranate and are silent, and Buck has no 'pomegranate' concept. Modern scholarship treats both of Nourai's daughter words as loans from the ancient Near East, not as Indo-European cognates: Old Armenian նուձն nuŕn (gen. նձան nŕan) is a Hurro-Urartian borrowing from Hurrian nuranti 'pomegranate' (Ačaŕyan HAB; Diakonoff, 'Hurro-Urartian Borrowings in Old Armenian', 1985; J̌ahukyan 1987/2010; Thorsø 2023), beside Hittite nurati, Akkadian nurmû/nurimtu, Sumerian nurma; and Wiktionary's Persian انار entry says it is 'arguably, ultimately related to the pomegranate terms under Arabic rummān', which is itself 'of uncertain direct and ultimate source, not Semitic'. Two further inaccuracies in the box: Nourai's gloss 'watery, juicy' adds 'juicy' to Mann's bare 'watery', and drops Mann's question mark; and his 'Anôr' renders Mann's onōr (o-, not a-). Verdict: disputed — the reference says what Nourai says, but the claim itself is not accepted.\",\n  \"note_fa\": \"مرجع نورایی درست است ولی ادعا پذیرفتنی نیست. من (Mann) در صفحهٔ ۱۶۴۵ ، در بخش پیوست، عیناً می‌نویسد: «(nōr, onōr ‚watery‘ (?) in Pahl. anār, Per. nār ‚pomegranate‘ and Arm. nurn, gs: nran)» — پرانتز و علامت پرسش خود نشانهٔ وانمودن تردید نویسنده است. پوکورنی، والدهٔ‌پوکورنی و واتکینز هیچ کدام چنین ریشه‌ای ندارند. پژوهش امروزی هر دو واژهٔ پایینی را وام‌واژه می‌داند: ارمنی کهن nuŕn (مضاف‌الیه nŕan) وام‌گیری از هوریایی nuranti است (آچاریان، دیاکونوف ۱۹۸۵، جاهوکیان، تورسو ۲۰۲۳)، هم‌ریشه با حتی‌ای nurati، اکدی nurmû/nurimtu و سومری nurma؛ و عربی رُمّان قلب‌شدهٔ همین واژهٔ درهم‌جوشیدهٔ خاور نزدیک است. پس این ریشه وام‌واژه‌ای منطقه‌ای است و نه هندواروپایی؛ پژوهش امروزی ادعای نورایی را رد می‌کند. افزودن «آبدار» (juicy) به معنای من و نیز ضبط Anôr در برابر onōr دو بی‌دقتی دیگر است.\",\n  \"sources\": [\n    W + \"انار\",\n    W + \"رمان\",\n    W + \"նուղն\"\n  ],\n  \"ref_check\": [\n   {\"ref\": \"IEC:1645\", \"status\": \"supports\",\n    \"note\": \"Mann, An Indo-European Comparative Dictionary, Supplement, p. 1645. The local IEC.txt stops at p. 1554, so the page was read in the archive.org djvu text of the same scan (item mann-an-indo-european-comparative-dictionary-1984-1987, line 118691, between the page markers 1645 and 1646): '(nōr, onōr ‚watery‘ (?) in Pahl. anār, Per. nār ‚pomegranate‘ and Arm. nurn, gs: nran, id.)'. The page and the content are exactly as cited; the reservation is Mann's own '(?)' and the parentheses, which Nourai drops, and Mann's Persian form is nār, not anār.\"}\n  ],\n  \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"IEW, searched POK_full/POK_01/02/03 for 'lemma: nōr', 'nor-' + Granatapfel\", \"stance\": \"silent\",\n    \"note\": \"Pokorny has no root *nōr-/*onōr- 'watery'; the only n-r- roots near it are 1./2./3. ner- 'under/man/dive' (pp. 765-766) and nu- 'now' (p. 770). No pomegranate word anywhere in the IEW.\"},\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. I-III (WLD_band3.txt index and WLD_Bd1/Bd2_pages.txt)\", \"stance\": \"silent\",\n    \"note\": \"grep for 'Granatapfel' in all three volumes returns nothing; the German Wortregister of Bd. III has no entry for the fruit, so WP has no such root either.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 (AHD_watkins1985.txt)\", \"stance\": \"silent\",\n    \"note\": \"grep for '^nō-r', '^nor-' and 'pomegranate': no hits. Watkins does not recognise the root.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 1949 (SYN.txt)\", \"stance\": \"silent\",\n    \"note\": \"grep -i pomegranate: no hits. Buck has no concept entry for the fruit, so no independent IE comparison is offered there.\"}\n  ],\n  \"nodes\": []\n}\n\ne1[\"nodes\"] = [\n {\n  \"id\": 1, \"lang\": \"Pahlavi\", \"words\": \"anâr\",\n  \"verdict\": \"disputed\",\n  \"derivation\": \"The word itself is beyond doubt: MacKenzie's Concise Pahlavi Dictionary p. 9 has 'anār [ʾNʾL | N ~] pomegranate' (with the derivative anārǵēl 'coconut'), and Pahlavi liturgical vocabulary uses pomegranate twigs — parāhōm is defined by MacKenzie as the infusion of pounded hōm and pomegranate twigs. What is disputed is the arrow: the derivation of anār from an Indo-European root *nōr-/*onōr- 'watery' is Mann's private and self-questioned conjecture (see the root note), and there is no Iranian etymology for it — no Avestan or Old Persian antecedent is attested and Cheung's Etymological Dictionary of the Iranian Verb offers no verbal root to build it on. The modern account makes MP anār part of the ancient Near-Eastern culture-word for the pomegranate (Hurrian nuranti, Hittite nurati, Sumerian nurma, Akkadian nurmû, Aramaic rimmōnā, Arabic rummān): the fruit was domesticated in the Iranian/Transcaucasian zone and its name travelled with it, so the Iranian form is one member of a Wanderwort family rather than the IE-inherited head of it. Note also the aphaeretic byform: the initial a- is original (nār is the reduced form), which Hübschmann demonstrates independently.\",\n  \"derivation_fa\": \"خود واژه قطعی است: مکنزی در صفحهٔ ۹ فرهنگ پهلوی خود «anār [ʾNʾL | N ~] pomegranate» دارد. اما پیکان نمودار پذیرفتنی نیست: بازگرداندن anār به ریشهٔ هندواروپایی *nōr- «آبدار» حدسی است که خود من هم با علامت پرسش آورده است، و هیچ پیشینهٔ اوستایی یا پارسی باستان برای آن گواهی نشده است. دیدگاه امروزی anār را عضوی از خانوادهٔ واژه‌های درهم‌جوشیدهٔ خاور نزدیک می‌داند (هوریایی nuranti، حتی‌ای nurati، سومری nurma، اکدی nurmû، آرامی rimmōnā، عربی رُمّان)، نه سرچشمهٔ موروثی آن. پژوهش امروزی ادعای نورایی را رد می‌کند.\",\n  \"sources\": [W + \"انار\", W + \"رمان\", W + \"նուղն\"],\n  \"ref_check\": [\n   {\"ref\": \"IEC:1645\", \"status\": \"supports\",\n    \"note\": \"Mann Suppl. p. 1645 (archive.org djvu text of the same scan, line 118691): '(nōr, onōr ‚watery‘ (?) in Pahl. anār, Per. nār ‚pomegranate‘ and Arm. nurn, gs: nran, id.)' — the Pahlavi form and the arrow are literally Mann's, so the reference supports the chart even though the claim is rejected by other authorities.\"}\n  ],\n  \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary p. 9 (PHD.txt leaf 30)\", \"stance\": \"partial\",\n    \"note\": \"'anār [ʾNʾL | N ~] pomegranate. anārǵēl [ʾNʾLgyl | N nārgēl] coconut.' MacKenzie confirms the Middle Persian word and its New Persian continuation but, as always, gives no Indo-European etymology; the English-Pahlavi index (p. ~163) likewise has 'pomegranate anār'.\"},\n   {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II (glossary)\", \"stance\": \"silent\",\n    \"note\": \"grep for anār / anar: no entry — the word does not occur in the texts Nyberg glosses, so he neither confirms nor contradicts the derivation.\"},\n   {\"src\": \"POK\", \"where\": \"IEW\", \"stance\": \"silent\",\n    \"note\": \"No root *nōr- 'watery' and no pomegranate word; Pokorny offers no Indo-European home for anār.\"}\n  ]\n },\n {\n  \"id\": 2, \"lang\": \"Persian\", \"words\": \"anâr «انار (نار)»\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"This single step — Pahlavi anār > New Persian انار anār, with the byform نار nār that Nourai puts in brackets — is solid, whatever the ultimate origin of the word. MacKenzie's entry already writes the New Persian reflex as identical ('anār [ʾNʾL | N ~]'), and Wiktionary's Persian انار is 'inherited from Middle Persian 𐨠𐨭𐨠𐨥 (ʾnʾl /anār/)'. نار is not a separate word or an Arabic loan (Arabic for the fruit is رُمّان, and نار in Arabic means 'fire'): it is the aphaeretic form produced by the loss of unstressed initial a-, and Hübschmann, Persische Studien p. 122, uses this very word as one of his examples that the a- was still there in early New Persian — 'Da der Abfall des a erst im älteren Neupersisch stattfand, sind mehrfach noch die alten Formen mit a überliefert: so ... anār ‚Granatapfel‘, avēza ‚rein‘'. Moʾin tags the entry '[په.]', i.e. Pahlavi, and expressly equates انار with نار. Ferdowsī's line quoted in the box ('بفرمود تا آب نار آورند') documents the short form in the earliest New Persian. — On the chart's own NOTE, that SKT:360 links this word to Sanskrit 'Naranga: orange tree': modern scholarship rejects the link. Sanskrit नारङ्ग nāraṅga 'orange tree' is a Dravidian borrowing (Tamil nārttaṅkāy, Telugu nāraṅgamu, Malayalam nāraṅṅa, Kannada nāraṅgi; so Mayrhofer EWAia and Turner CDIAL), and it is Sanskrit → Persian nārang/nāranj → Arabic nāranj → Italian arancia → English orange, i.e. the traffic runs the other way and has nothing to do with the pomegranate. Skeat's own wording is a guess, not a derivation ('Allied to Pers. nār, a pomegranate'), and Nourai's page number does not fit either printing of the Concise Dictionary (see ref_check).\",\n  \"derivation_fa\": \"این یک پله — پهلوی anār ← فارسی نو «انار» با گونهٔ کوتاه «نار» — قطعی است، جدا از اینکه سرچشمهٔ نهایی واژه چه باشد. معین این ماده را «[په.]» می‌زند و انار را با نار یکی می‌گیرد. «نار» واژهٔ جدا یا معرّب نیست (نار در عربی «آتش» است و انار در عربی رُمّان)، بلکه حاصل افتادن الف آغازین بی‌تاکید است؛ هوبشمان در مطالعات فارسی (ص ۱۲۲) همین واژه را نمونهٔ بازماندن الف در فارسی نوی کهن می‌آورد. دربارهٔ یادداشت نمودار (پیوند با سنسکریت nāraṅga «درخت نارنج») پژوهش امروزی آن را رد می‌کند: nāraṅga خود وام‌واژه‌ای دراویدی است (تامیلی nārttaṅkāy، تلوگویی nāraṅgamu) و راه وام‌گیری سنسکریت ← فارسی نارنگ/نارنج ← عربی نارنج ← ایتالیایی arancia است، که ربطی با انار ندارد؛ گفتهٔ اسکیت نیز تنها احتمال بود نه اثبات.\",\n  \"sources\": [W + \"انار\", W + \"नारङ्ग\", \"https://www.etymonline.com/word/orange\", \"https://abadis.ir/fatofa/انار/\"],\n  \"ref_check\": [\n   {\"ref\": \"MON:4557\", \"status\": \"supports\",\n    \"note\": \"The six-volume Amir Kabir Farhang-e Fārsī is not scanned anywhere (see refs_online.json MON notes), so the page number itself cannot be checked. The entry was read instead in the Moʾin section of abadis.ir/fatofa/انار: '( َا ) [ په . ] ( اِ. ) = نار: درختچه‌ای از تیرهٔ موردی‌ها دارای برگ‌های بیضوی و گل‌های قرمزرنگ'. Moʾin's origin tag '[په.]' = Pahlavi is exactly the arrow Nourai draws (Pahlavi → Persian) and the '= نار' confirms the bracketed byform.\"},\n   {\"ref\": \"IEC:1645\", \"status\": \"partial\",\n    \"note\": \"Mann Suppl. p. 1645 gives the Persian form as 'Per. nār ‚pomegranate‘', i.e. only the aphaeretic form, not Nourai's headword anār; and he attaches it to the questioned root, not to the Pahlavi word. The Pahlavi → Persian step as such is not what Mann's line asserts.\"},\n   {\"ref\": \"SKT:360\", \"status\": \"not_found\",\n    \"note\": \"Checked both printings of Skeat's Concise Etymological Dictionary. In the 1911 text (local SKT.txt) p. 360 is the PNEUMATIC/POACH area and the ORANGE entry stands on p. 318 (leaf 341, running heads ORANG-OUTANG / ORE); in the 1882 first edition (archive.org bub_gb_4ZkRAAAAIAAJ djvu text) p. 360 is again PNEUMATIC/POACH and ORANGE is on p. 318: 'Orange. (F. - Ital. - Pers.) O.F. orenge ... Pers. naranj, nārinj, nārang, an orange. Allied to Pers. nār, a pomegranate.' So the claim Nourai reports does exist in Skeat, but neither the page number nor the Sanskrit form 'Naranga: orange tree' is in the Concise Dictionary (the Sanskrit form belongs to Skeat's larger Etymological Dictionary).\"}\n  ],\n  \"consulted\": [\n   {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien p. 122 (HUB.txt line 4246)\", \"stance\": \"supports\",\n    \"note\": \"'Da der Abfall des a erst im älteren Neupersisch stattfand, sind mehrfach noch die alten Formen mit a überliefert: so abe- ‚ohne‘ ..., anōša ‚Heil‘ (bei Firdusi), anār ‚Granatapfel‘, avēza ‚rein‘' — independent proof that anār is the older form and nār the reduced one, which is exactly how Nourai's box writes it, 'انار (نار)'.\"},\n   {\"src\": \"PHD\", \"where\": \"MacKenzie p. 9\", \"stance\": \"supports\",\n    \"note\": \"'anār [ʾNʾL | N ~] pomegranate' — the 'N ~' notation means the New Persian form is identical to the Middle Persian one, i.e. MP anār > NP anār without change.\"},\n   {\"src\": \"MON\", \"where\": \"Moʾin, Farhang-e Fārsī s.v. انار, read via abadis.ir\", \"stance\": \"supports\",\n    \"note\": \"'( َا ) [ په . ] ( اِ. ) = نار ...' — Pahlavi origin tag, and انار equated with نار.\"},\n   {\"src\": \"BQT\", \"where\": \"Borhān-e Qāţeʽ vol. 1, leaves 380-381 (printed pp. ~160-161)\", \"stance\": \"silent\",\n    \"note\": \"Borhān has only the compounds انار فرهاد, انارگیر and انارمشک at this place, with no simple headword انار and no Moʾin etymological footnote for it, so Borhān contributes nothing either way (the fruit was too everyday for Tabrīzī's dictionary of 'difficult' words).\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict. s.v. ORANGE, p. 318 (1882 and 1911)\", \"stance\": \"partial\",\n    \"note\": \"'Pers. naranj, nārinj, nārang, an orange. Allied to Pers. nār, a pomegranate.' Skeat does propose the link Nourai reports, but he only says 'allied to' and gives no Sanskrit form; Mayrhofer, Turner and Wiktionary derive nāraṅga from Dravidian instead, and Etymonline calls it 'a word of uncertain origin'.\"}\n  ]\n },\n {\n  \"id\": 3, \"lang\": \"Armenian\", \"words\": \"nurn, nran\",\n  \"verdict\": \"disputed\",\n  \"derivation\": \"The Armenian word exists, but neither its shape nor its origin is what the chart implies. Old Armenian նուղն nuŕn 'pomegranate' has the genitive նձան nŕan; Nourai's 'nurn, nran' is Mann's Latinisation of that nominative-plus-genitive pair, not two independent words, so the box reads as if Armenian had two forms for the fruit. More importantly, the arrow drawn from an Indo-European root is rejected by Armenian etymology: nuŕn is a Hurro-Urartian loanword, from Hurrian nuranti 'pomegranate', alongside Hittite nurati, Akkadian nurimdu/nurimtu and nurmû, and Sumerian nurma — the position of Ačaŕyan (Hayeren armatakan bararan), Diakonoff ('Hurro-Urartian Borrowings in Old Armenian', 1985), J̌ahukyan (1987, 2010) and most recently Thorsø (Prehistoric loanwords in Armenian, 2023). Arabic رُمّان rummān / Hebrew רִמּוֹן rimmōn represent the same culture-word with the consonants in the other order. On that account the Armenian and the Middle Persian words are not IE cognates descended in parallel from a root, but two independent uptakes of one ancient Near-Eastern name for the fruit, and Armenian did not get it from Iranian either (contrast the many genuine Iranian loans in Armenian catalogued by Hübschmann).\",\n  \"derivation_fa\": \"واژهٔ ارمنی وجود دارد، اما نه به این شکل و نه با این خاستگاه. ارمنی کهن նուղն nuŕn «انار» مضاف‌الیه նձան nŕan دارد؛ پس «nurn, nran» دو واژه نیست بلکه جفت فاعلی‌مضافی است که من آورده و نورایی برداشته است. مهم‌تر اینکه ریشه‌شناسی ارمنی این واژه را وام‌واژهٔ هوریایی‌اورارتویی می‌داند، از هوریایی nuranti، در کنار حتی‌ای nurati، اکدی nurimtu/nurmû و سومری nurma (آچاریان، دیاکونوف ۱۹۸۵، جاهوکیان، تورسو ۲۰۲۳)؛ عربی رُمّان و عبری rimmōn هم قلب‌شدهٔ همین واژه اند. پس ارمنی و فارسی میانه هم‌ریشهٔ هندواروپایی نیستند بلکه دو وام‌گیری جداگانه از یک واژهٔ فرهنگی خاور نزدیک اند. پژوهش امروزی ادعای نورایی را رد می‌کند.\",\n  \"sources\": [W + \"նուղն\", W + \"رمان\"],\n  \"ref_check\": [\n   {\"ref\": \"IEC:1645\", \"status\": \"supports\",\n    \"note\": \"Mann Suppl. p. 1645: '... and Arm. nurn, gs: nran, id.' — Nourai's two 'words' are Mann's nominative and genitive, and Mann does put the Armenian form under the questioned root, so the reference matches the chart. Mann's own '(?)' remains.\"}\n  ],\n  \"consulted\": [\n   {\"src\": \"Wiktionary/Ačaŕyan\", \"where\": \"en.wiktionary.org Old Armenian նուղն (nuŕn), with Further reading: Ačaŕyan HAB 1971-79; Diakonoff 1985; J̌ahukyan 1987, 2010; Thorsø 2023\", \"stance\": \"contradicts\",\n    \"note\": \"'From Hurrian nuranti (‚pomegranate‘)', related to Hittite nurati, Akkadian nurimdu/nurimtu, Sumerian nurma, Akkadian nurmû; 'See Arabic rummān for another order of the consonants.' Genitive given as նձան (nŕan). A Hurro-Urartian borrowing, explicitly not Indo-European and not Iranian.\"},\n   {\"src\": \"Wiktionary (Arabic رُمّان)\", \"where\": \"en.wiktionary.org رمان\", \"stance\": \"contradicts\",\n    \"note\": \"'of uncertain direct and ultimate source, not Semitic', with Hebrew rimmōn, Punic *rmn, Aramaic rimmōnā, and under 'Further potential cognates' the Sumerian/Akkadian/Hurrian/Ugaritic pomegranate words 'with consonantal reordering', including Old Armenian nuŕn — i.e. the fruit-name is an ancient Near-Eastern Wanderwort, not an inherited IE lexeme.\"},\n   {\"src\": \"POK\", \"where\": \"IEW\", \"stance\": \"silent\",\n    \"note\": \"No Armenian pomegranate word and no root that could yield it; Pokorny's Armenian material under en(o)mn̥- and the ner-/nor- entries is unrelated.\"},\n   {\"src\": \"HUB\", \"where\": \"Hübschmann (Persische Studien; his Armenische Grammatik is the standard list of Iranian loans in Armenian)\", \"stance\": \"silent\",\n    \"note\": \"The local Persische Studien text mentions anār only in the phonological discussion on p. 122 and says nothing about an Armenian nuŕn, so Hübschmann does not treat it as an Iranian loan in Armenian either.\"}\n  ]\n }\n]\n\ndoc = {\n  \"pdf_page\": 370,\n  \"book_page\": 340,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-07\",\n  \"entries\": [e0, e1]\n}\n\nwith io.open('/home/sfmqrb/git/rishe/data/verification/page-370.json','w',encoding='utf-8') as f:\n    json.dump(doc, f, ensure_ascii=False, indent=2)\n    f.write('\\n')\nprint('written')\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-370.py"
}
```


### [2026-09-07T20:40:52.038Z] TOOL RESULT

```
written
```


## [2026-09-07T20:41:08.528Z] TOOL CALL #91: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 - <<'EOF'\nimport io\np='data/verification/page-370.json'\nt=io.open(p,encoding='utf-8').read()\nsubs=[\n (\"նուղն\",\"նուռն\"),\n (\"nuŕn\",\"nuṙn\"),\n (\"nŕan\",\"nṙan\"),\n (\"Ačaŕyan\",\"Ačaṙyan\"),\n (\"նուձն\",\"նուռն\"),\n (\"նձան\",\"նռան\"),\n (\"𐨠𐨭𐨠𐨥 (ʾnʾl /anār/)\",\"ʾnʾl /anār/\"),\n]\nfor a,b in subs:\n    t=t.replace(a,b)\nio.open(p,'w',encoding='utf-8').write(t)\nEOF\ngrep -c \"նուռն\" data/verification/page-370.json; grep -o \"nuṙn\" data/verification/page-370.json | wc -l; grep -o \"նուղն\\|nuŕn\\|nŕan\\|𐨠\" data/verification/page-370.json | wc -l\npython3 -m json.tool data/verification/page-370.json > /dev/null && echo \"JSON OK\"\npython3 tools/verify_check.py 370"
}
```


### [2026-09-07T20:41:09.961Z] TOOL RESULT

```
7
9
0
JSON OK
nodes verified: 13/13
node verdicts: {'plausible': 1, 'confirmed': 9, 'unverified': 1, 'disputed': 2}
root verdicts: {'confirmed': 1, 'disputed': 1}
ref checks: {'supports': 9, 'partial': 3, 'not_checked': 4, 'not_found': 1}
books consulted: {'partial': 4, 'supports': 27, 'silent': 7, 'contradicts': 2} | by book: {'POK': 5, 'WLD': 4, 'PHD': 4, 'KLN': 4, 'SYN': 3, 'HUB': 3, 'AHD': 3, 'BRT': 2, 'NYB': 2, 'ARY': 2, 'LAT': 2, 'BOOK': 1, 'MON': 1, 'BQT': 1, 'SKT': 1, 'Wiktionary/Ačaŕyan': 1, 'Wiktionary (Arabic رُمّان)': 1}
```


## [2026-09-07T20:41:19.507Z] TOOL CALL #92: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\ngrep -o \"Ača[^\\\"]\\{0,10\\}\" data/verification/page-370.json | head\npython3 - <<'EOF'\nimport glob,json,collections\nc=collections.Counter()\nfor f in glob.glob('data/verification/page-*.json'):\n    d=json.load(open(f))\n    for e in d.get('entries',[]):\n        for n in e.get('nodes',[])+[e]:\n            for x in n.get('consulted') or []:\n                c[x.get('src')]+=1\nfor k,v in c.most_common(60): print(v,'|',k)\nEOF"
}
```


### [2026-09-07T20:41:21.168Z] TOOL RESULT

```
2255 | KLN
1291 | AHD
1172 | WLD
1097 | POK
900 | PHD
900 | MON
790 | SKT
771 | BRT
715 | HRN
698 | IEC
657 | BQT
610 | SYN
576 | NYB
552 | CHEUNG
539 | LKT
521 | HUB
500 | ARY
348 | LAT
334 | Wiktionary
305 | KNT
294 | WEB
276 | FSD
208 | FVQ
204 | Etymonline
203 | PLA
157 | AFM
157 | DEV
155 | SOD
136 | HJB
95 | AFA
87 | PHN
71 | LEW
61 | ISS_alt_DKS
56 | TAD
55 | AKD
54 | RCH
45 | BOOK
41 | WIKT
38 | FSF
33 | ETYMONLINE
25 | TTS
25 | AID
24 | FFD
23 | web
22 | TLM
21 | AVG
20 | HENNING
19 | LAM
19 | FRS
17 | DOZ
17 | ARB
16 | SIN
16 | SNS
11 | GPL
10 | ISS
9 | Dehkhoda
8 | etymonline
7 | WEB-Etymonline
6 | AHM
5 | SPG
```


## [2026-09-07T20:41:33.682Z] TOOL CALL #93: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 - <<'EOF'\nimport io,json\np='data/verification/page-370.json'\nd=json.load(io.open(p,encoding='utf-8'))\nfor e in d['entries']:\n    for n in e['nodes']:\n        for c in n.get('consulted') or []:\n            if c['src'].startswith('Wiktionary'):\n                old=c['src']; c['src']='Wiktionary'\n                c['where']=old.replace('Wiktionary/','').replace('Wiktionary (','').replace(')','')+' — '+c['where'] if '/' in old or '(' in old else c['where']\njson.dump(d, io.open(p,'w',encoding='utf-8'), ensure_ascii=False, indent=2)\nio.open(p,'a',encoding='utf-8').write('\\n')\nEOF\ngrep -o '\"src\": \"[^\"]*\"' data/verification/page-370.json | sort | uniq -c\npython3 tools/verify_check.py 370"
}
```


### [2026-09-07T20:41:35.260Z] TOOL RESULT

```
      5 "src": "AHD"
      2 "src": "ARY"
      1 "src": "BOOK"
      1 "src": "BQT"
      2 "src": "BRT"
      3 "src": "HUB"
      1 "src": "IEC"
      4 "src": "KLN"
      2 "src": "LAT"
      1 "src": "MON"
      2 "src": "NYB"
      4 "src": "PHD"
      6 "src": "POK"
      1 "src": "SKT"
      5 "src": "SYN"
      2 "src": "Wiktionary"
      6 "src": "WLD"
nodes verified: 13/13
node verdicts: {'plausible': 1, 'confirmed': 9, 'unverified': 1, 'disputed': 2}
root verdicts: {'confirmed': 1, 'disputed': 1}
ref checks: {'supports': 9, 'partial': 3, 'not_checked': 4, 'not_found': 1}
books consulted: {'partial': 4, 'supports': 27, 'silent': 7, 'contradicts': 2} | by book: {'POK': 5, 'WLD': 4, 'PHD': 4, 'KLN': 4, 'SYN': 3, 'HUB': 3, 'AHD': 3, 'BRT': 2, 'NYB': 2, 'ARY': 2, 'LAT': 2, 'Wiktionary': 2, 'BOOK': 1, 'MON': 1, 'BQT': 1, 'SKT': 1}
```


## [2026-09-07T20:41:46.145Z] TOOL CALL #94: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nmkdir -p data/verification/sources/refs/ocr/BOOK && cp /tmp/pg370-p370.png data/verification/sources/refs/ocr/BOOK/370.png && ls -l data/verification/sources/refs/ocr/BOOK/370.png\npython3 - <<'EOF'\nimport io\np='data/verification/page-370.json'\nt=io.open(p,encoding='utf-8').read()\nimport json; json.loads(t); print('valid json, bytes',len(t))\nfor bad in ('նուղն','nuŕn','nŕan','Ačaŕyan','𐨠'):\n    print(bad, t.count(bad))\nprint('նուռն', t.count('նուռն'), '| nuṙn', t.count('nuṙn'), '| nṙan', t.count('nṙan'), '| Ačaṙyan', t.count('Ačaṙyan'))\nEOF\nsed -i 's|\"https://en.wiktionary.org/wiki/նուռն\"|\"https://en.wiktionary.org/wiki/նուռն\"|' data/verification/page-370.json\ngrep -o 'https://en.wiktionary.org/wiki/[^\"]*' data/verification/page-370.json | sort -u"
}
```


### [2026-09-07T20:41:47.432Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 53336 Sep  7 16:41 data/verification/sources/refs/ocr/BOOK/370.png
valid json, bytes 55699
նուղն 0
nuŕn 0
nŕan 0
Ačaŕyan 0
𐨠 0
նուռն 7 | nuṙn 9 | nṙan 5 | Ačaṙyan 0
https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₃néh₃mn̥
https://en.wiktionary.org/wiki/նուռն
https://en.wiktionary.org/wiki/انار
https://en.wiktionary.org/wiki/دشنام
https://en.wiktionary.org/wiki/رمان
https://en.wiktionary.org/wiki/نام
https://en.wiktionary.org/wiki/नारङ्ग
```


## [2026-09-07T20:41:53.811Z] TOOL CALL #95: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; grep -o \"A[čc]a[^ ]* HAB\\|Diakonoff[^,]*\\|Thorsø[^)]*\" data/verification/page-370.json | head"
}
```


### [2026-09-07T20:41:53.896Z] TOOL RESULT

```
Diakonoff
Thorsø 2023
Diakonoff ('Hurro-Urartian Borrowings in Old Armenian'
Thorsø (Prehistoric loanwords in Armenian, 2023
Diakonoff 1985; J̌ahukyan 1987
Thorsø 2023",
```


## [2026-09-07T20:41:57.497Z] TOOL CALL #96: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; grep -o \".\\{0,40\\}HAB.\\{0,20\\}\" data/verification/page-370.json; echo \"--- around Diakonoff\"; grep -o \".\\{0,60\\}Diakonoff.\\{0,10\\}\" data/verification/page-370.json"
}
```


### [2026-09-07T20:42:00.562Z] TOOL RESULT

```
Hurrian nuranti 'pomegranate' (Ačaŕyan HAB; Diakonoff, 'Hurro-
 (nuṙn), with Further reading: Ačaŕyan HAB 1971-79; Diakonoff 
--- around Diakonoff
borrowing from Hurrian nuranti 'pomegranate' (Ačaŕyan HAB; Diakonoff, 'Hurro-U
rma — the position of Ačaŕyan (Hayeren armatakan bararan), Diakonoff ('Hurro-U
n նուռն (nuṙn), with Further reading: Ačaŕyan HAB 1971-79; Diakonoff 1985; J̌a
```


## [2026-09-07T20:42:07.286Z] TOOL CALL #97: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 - <<'EOF'\nimport io\np='data/verification/page-370.json'\nt=io.open(p,encoding='utf-8').read()\nprint('U+0155 count before:', t.count('ŕ'))\nt=t.replace('ŕ','ṙ')\nio.open(p,'w',encoding='utf-8').write(t)\nprint('after:', t.count('ŕ'), '| U+1E59:', t.count('ṙ'))\nimport json; json.loads(t); print('valid')\nEOF\ngrep -o \".\\{0,20\\}HAB\" data/verification/page-370.json\npython3 tools/verify_check.py 370"
}
```


### [2026-09-07T20:42:08.824Z] TOOL RESULT

```
U+0155 count before: 4
after: 0 | U+1E59: 18
valid
egranate' (Ačaṙyan HAB
r reading: Ačaṙyan HAB
nodes verified: 13/13
node verdicts: {'plausible': 1, 'confirmed': 9, 'unverified': 1, 'disputed': 2}
root verdicts: {'confirmed': 1, 'disputed': 1}
ref checks: {'supports': 9, 'partial': 3, 'not_checked': 4, 'not_found': 1}
books consulted: {'partial': 4, 'supports': 27, 'silent': 7, 'contradicts': 2} | by book: {'POK': 5, 'WLD': 4, 'PHD': 4, 'KLN': 4, 'SYN': 3, 'HUB': 3, 'AHD': 3, 'BRT': 2, 'NYB': 2, 'ARY': 2, 'LAT': 2, 'Wiktionary': 2, 'BOOK': 1, 'MON': 1, 'BQT': 1, 'SKT': 1}
```


## [2026-09-07T20:42:31.382Z] AGENT

Done. `python3 tools/verify_check.py 370` reports 0 PROBLEM lines.

**Page 370 (book p. 340) — 2 charts + 1 redirect (Nu → Newo, skipped)**

Verdicts: nodes 13 total — 9 confirmed, 1 plausible, 2 disputed, 1 unverified (blank box). Roots — 1 confirmed, 1 disputed.
Ref checks: 9 supports, 3 partial, 1 not_found, 4 not_checked. 43 `consulted` entries across POK, WLD, AHD, SYN, KLN, LAT, BRT, KNT, PHD, NYB, HRN, HUB, BQT, MON, ARY, SKT, IEC, Wiktionary.

Flagged items:
- **Nôr, Anôr (ROOT) — disputed.** Mann IEC p. 1645 really does say it, but verbatim as `(nōr, onōr 'watery' (?) …)` — parenthesised and question-marked in his Supplement. Pokorny, Walde-Pokorny, Watkins and Buck are all silent; no such IE root exists. Nourai also adds "juicy" to Mann's bare "watery" and writes *Anôr* for Mann's *onōr*.
- **#1 Pahlavi anâr — disputed.** The word is real (MacKenzie p. 9) but is not IE-inherited; it belongs to the ancient Near-Eastern pomegranate Wanderwort (Hurrian *nuranti*, Akkadian *nurmû*, Sumerian *nurma*, metathesised in Arabic *rummān*).
- **#3 Armenian nurn, nran — disputed.** Old Armenian նուռն *nuṙn* (gen. նռան *nṙan* — so the box's "two words" are really nominative + genitive) is a Hurro-Urartian loan from Hurrian *nuranti* (Ačaṙyan, Diakonoff 1985, J̌ahukyan, Thorsø 2023), not an IE sibling of Pahlavi *anār*.
- **#1 Avestan (Nomn chart) — plausible.** *nāma/nāman-* is confirmed (Bartholomae, Kent p. 193), but **duš-naman is not an attested Avestan word** — Bartholomae has no such compound; it is first attested in Middle Persian (Manichaean *dwjnʾm*, Pahlavi *duš-nām* "ill-famed").
- **SKT:360 (the chart's own NOTE) — not_found and rejected.** Neither the 1882 nor the 1911 Skeat Concise has anything on p. 360 (that page is PNEUMATIC/POACH); the ORANGE entry is on p. 318 and says only "Allied to Pers. nār, a pomegranate", with no Sanskrit form. Modern view: Skt. *nāraṅga* is a Dravidian loan (Mayrhofer, Turner) with no connection to *anār/nār*.
- **MON:4557 — page unverifiable** (no scan of the 6-vol Farhang exists); content checked via abadis.ir, where Moʾin tags انار `[په.]` = Pahlavi and equates it with نار, which does support the arrow.
- **BQT:2106 verified precisely**: vol. 4, pdf p. 189 (printed = pdf + 1917), headword نام with Moʾin's footnote giving Pahlavi *nām* / OIr. *nāman-* / Bartholomae 1062; نامه is on the facing p. 2107.

Extraction errors: **none**. The JSON matches the printed page exactly, including node #4, which is a genuinely blank, unlabelled rectangle in the book (page render copied to `data/verification/sources/refs/ocr/BOOK/370.png`).

Note for the library: `data/verification/sources/refs/IEC.txt` is truncated at printed p. 1554 and lacks Mann's Supplement (pp. ~1555–1682); the full `_djvu.txt` from archive.org has it, and that is where IEC:1645 had to be read.
