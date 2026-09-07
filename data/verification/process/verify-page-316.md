# Verification process log — verify-page-316


## [2026-09-07T01:37:06.639Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 316 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-316.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-316.json. Write /home/sfmqrb/git/rishe/data/verification/page-316.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 316` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-07T01:37:11.335Z] AGENT

I'll start by reading the agent instructions.


## [2026-09-07T01:37:11.798Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-07T01:37:11.812Z] TOOL RESULT

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


## [2026-09-07T01:37:12.659Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-316.txt"
}
```


### [2026-09-07T01:37:12.676Z] TOOL RESULT

```
1	=== PDF page 316 (book page 286) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Mâ, Mâ-ter : Mâ: breast. Mâ-ter: feeder (of the family), mother ☞ Ter 3. This has probably started as a nursery word and became a usual term in the Indo-European languages.  (refs POK:694; PRT:386,863; SYN:103)
4	#1 (parent #0) [Avestan] refs=POK:694; SKT:336 | mâtar : mother
5	  #2 (parent #1) [Pahlavi] refs=BQT:1933; SNS:237 | mâtar : mother ; matak : female ; mâdiyânag, mâyag : essence
6	    #3 (parent #2) [Persian] refs=BQT:1933,1946,1964; HRN:213; MON:3716; SNS:237 | mâdar «مادر» : mother ; mâdeh «ماده» : female ; mâyeh «مایه» : origin, originality, essence, value | extra: مام ، ماما
7	مادگان ، مادیان ، ماکیان
8	#4 (parent #0) [Germanic] refs=AHD; KLN | môthar
9	  #5 (parent #4) [English] refs=None | mother
10	#6 (parent #0) [Latin] refs=AHD; KLN:948 | mamma : breast ; mâter : mother ; mâtrix : pregnant animal, womb ; mâteriěs, materia : tree's source of growth, trunk, also hard wood, material
11	  #7 (parent #6) [French] refs=None | 
12	    #8 (parent #7) [Persian] refs=MON:3679,3716 |  | extra: مامان ، ممه
13	  #9 (parent #6) [English] refs=AHD | mammal, maternal, maternity, matrimony, matrix, matter, material
14	#10 (parent #0) [Greek] refs=AHD | mětěr : mother, main, central
15	  #11 (parent #10) [English] refs=None | metro, metropolitan
16	
```


## [2026-09-07T01:37:16.231Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-316.json",
 "description": "Read source JSON for page 316"
}
```


### [2026-09-07T01:37:16.273Z] TOOL RESULT

```
{
  "pdf_page": 316,
  "book_page": 286,
  "entries": [
    {
      "root": {
        "name": "Mâ, Mâ-ter",
        "lang": "Indo-European",
        "refs": "POK:694; PRT:386,863; SYN:103",
        "gloss": "Mâ: breast. Mâ-ter: feeder (of the family), mother ☞ Ter 3. This has probably started as a nursery word and became a usual term in the Indo-European languages."
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:694; SKT:336",
          "words": [
            {"translit": "mâtar", "gloss": "mother", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "BQT:1933; SNS:237",
          "words": [
            {"translit": "mâtar", "gloss": "mother", "script": null},
            {"translit": "matak", "gloss": "female", "script": null},
            {"translit": "mâdiyânag, mâyag", "gloss": "essence", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "BQT:1933,1946,1964; HRN:213; MON:3716; SNS:237",
          "words": [
            {"translit": "mâdar", "gloss": "mother", "script": "مادر"},
            {"translit": "mâdeh", "gloss": "female", "script": "ماده"},
            {"translit": "mâyeh", "gloss": "origin, originality, essence, value", "script": "مایه"}
          ],
          "script_extra": "مام ، ماما\nمادگان ، مادیان ، ماکیان",
          "note": null,
          "quote": {
            "text": "تا ز دُرج گهر گشاید قند - گویدش مادگانه لفظی چند",
            "poet": "Haft Paykar"
          }
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD; KLN",
          "words": [
            {"translit": "môthar", "gloss": null, "script": null}
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
            {"translit": "mother", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD; KLN:948",
          "words": [
            {"translit": "mamma", "gloss": "breast", "script": null},
            {"translit": "mâter", "gloss": "mother", "script": null},
            {"translit": "mâtrix", "gloss": "pregnant animal, womb", "script": null},
            {"translit": "mâteriěs, materia", "gloss": "tree's source of growth, trunk, also hard wood, material", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "French",
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "Persian",
          "refs": "MON:3679,3716",
          "words": [],
          "script_extra": "مامان ، ممه",
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 6,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "mammal, maternal, maternity, matrimony, matrix, matter, material", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD",
          "words": [
            {"translit": "mětěr", "gloss": "mother, main, central", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 10,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "metro, metropolitan", "gloss": null, "script": null}
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


## [2026-09-07T01:37:16.972Z] TOOL CALL #4: Bash

```json
{
 "command": "sed -n '1,200p' data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-07T01:37:17.047Z] TOOL RESULT

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


## [2026-09-07T01:37:24.790Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','PRT','SYN','SKT','BQT','SNS','HRN','MON','AHD','KLN','WLD','IEC','BRT','PHD','NYB','ARY','LEW','LAT','HUB','FSD','WEB']:\n    v=d.get(k)\n    print('=====',k)\n    print(json.dumps(v,ensure_ascii=False,indent=1)[:1400])\n\""
}
```


### [2026-09-07T01:37:26.088Z] TOOL RESULT

```
===== POK
{
 "title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)",
 "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/indogermanisches01pokouoft",
 "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt",
 "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\\data\\ie\\pokorny&root=config",
 "notes": "Nourai's page numbe
===== PRT
{
 "title": "E. Partridge, Origins: A Short Etymological Dictionary of Modern English, New York 1958",
 "edition_found": "1958 (lending-only copies)",
 "kind": "archive_restricted",
 "url": "https://archive.org/details/originsshortetym00part (1958 1st ed.) ; originsetymologi0000part_j9t3 (4th ed. 1966) ; originsetymologi0000part (Routledge 2009) — all lending",
 "identifier": "originsshortetym00part (also originsshortetym0000unse, bwb_P8-AVM-445, 1958)",
 "local_file": null,
 "page_offset": null,
 "lookup_hint": "Borrow via IA lending; in-book search https://archive.org/details/originsshortetym00part?q=<word>. Entries are alphabetical with numbered sub-senses.",
 "notes": "RE-SEARCH 2026-09: 8 lending copies on archive.org, none open; HathiTrust search-only; Google no view. Borrow the 1958 copy to match Nourai's pagination."
}
===== SYN
{
 "title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949",
 "edition_found": "1949 (reprint scans, same pagination in all printings)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca",
 "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt",
 "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed page number line.",
 "notes": "Two other open copies: dictionaryofselectedsynonyms...buck_963_N, fock_a-dictionary-...; restricted: dictionaryofsele0000carl.",
 "cites": "page number of Buck, A Dictionary of Selected Synonyms (1949)"
}
===== SKT
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
===== BQT
{
 "title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)",
 "kind": "archive_djvu+local_scan_ocr",
 "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.com/file/8230741184/borhane_ghatee_jelde_4.pdf.html (م–ی, 553 pp), vol 5 https://s3.picofile.com/file/8230741300/borhane_ghatee_jelde_5.pdf.html (تعلیقات, Amir Kabir 5th pr. 1376, 293 pp). Same set behind login on ketabnak.com/book/55304-55307 and /58249.",
 "lookup_hint": "grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \\f; leaf N = N-th \\f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltex
===== SNS
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
===== HRN
{
 "title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893",
 "edition_found": "1893 (Google scan, Univ. Michigan)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/grundrissderneu00horngoog",
 "identifier": "grundrissderneu00horngoog",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt",
 "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.",
 "notes": "OCR of German Fraktur-free text is decent; Persian script is not OCRed.",
 "cites": "page number of Horn, Grundriss der neupersischen Etymologie (1893); entries are also numbered"
}
===== MON
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
  "/home/sfmqrb/git/rishe/data/verif
===== AHD
{
 "title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)",
 "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)",
 "kind": "archive_djvu+website+archive_restricted",
 "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only",
 "identifier": "watkins-american-heritage-dictionary-of-indo-european-roots-1985",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt",
 "page_offset": "1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.",
 "lookup_hint": "Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local
===== KLN
{
 "title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67",
 "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein",
 "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt",
 "page_offset": "KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.",
 "notes": "Other 1966 IA copies (comprehensiveety01klei/02klei etc.) are lending-only (401/403). local_files: /home/sfmqrb/git/rishe/data/verification/s
===== WLD
{
 "title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32",
 "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.39015066210397 (browser only from this host)",
 "identifier": "in.gov.ignca.20339 (Band 3); also in.ernet.dli.2015.106625 (Band 3 duplicate)",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927
===== IEC
{
 "title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87",
 "edition_found": "1984-1987 (complete, cols./pp. 1-1682)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987",
 "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt",
 "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.",
 "notes": "",
 "cites": "column/page number of Mann, An Indo-European Comparative Dictionary (1984–87)"
}
===== BRT
{
 "title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)",
 "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/altiranischeswr00bartgoog",
 "identifier": "altiranischeswr00bartgoog",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt",
 "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special transliteration is noisy - grep on a distinctive Latin gloss or the German meaning in quotes. Column numbers appear as standalone numbers at leaf tops.",
 "notes": "Nourai's Table IV says 1979; that is the unchanged reprint.",
 "cites": "column number (the Altiranisches Wörterbuch is numbered by column, two per page)"
}
===== PHD
{
 "title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971",
 "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/a-concise-pahlavi-dictionary",
 "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt",
 "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsianjoman.org/wp-content/uploads/2015/09/A-Concise-Pahlavi-Dictionary.pdf (8.4 MB).",
 "notes": "",
 "cites": "page number of MacKenzie, A Concise Pahlavi Dictionary (1971)"
}
===== NYB
{
 "title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)",
 "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg",
 "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt",
 "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates and 'Bthl.' refs.",
 "notes": " local_files: /home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt (Part II, pp. 1-286); /home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol1.txt (Part I, plain djvu.txt)",
 "local_files": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol1.txt"
 ],
 "cites": "page number of Nyberg, A Manual of Pahlavi, Part II Glossary (1974)"
}
===== ARY
{
 "title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.",
 "kind": "local_scan_ocr",
 "url": "",
 "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt"
 ],
 "page_offset": "printed page = pdf page + 1",
 "scans": [
  {
   "file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_aryanpur_kashani_rishehaye_hend_o_orupayi.pdf",
   "first_printed": 1,
   "last_printed": 546,
   "pdf_offset": -1,
   "lang": "fas+eng",
   "ocr_text": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt"
  }
 ],
 "notes": "Image-only PDF provided by the owner (2026-09-04). Use as an additional modern source alongside Wiktionary/Cheung/Hasandust when 
===== LEW
{
 "title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56",
 "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/lateinischesetym0000aloi",
 "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt",
 "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Latin headword in bold at line start. For 1938 pagination borrow lateinischesetym0000awal.",
 "notes": ""
}
===== LAT
{
 "title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951",
 "edition_found": "1951 (3rd ed.) - matches Nourai",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine",
 "identifier": "ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine (4th ed. 1959 lending-only: dictionnairetymo0000unse; another open copy: DictionnaireEtymologiqueDeLaLangueLatine)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt",
 "page_offset": "leaf = printed + 18 for most of the book (e.g. leaf 21 = p.3); drifts in places (leaf 219 = p.301 -> -82?? probably a mis-detected number) - grep the headword. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Latin headword in bold at line start followed by gender/declension, e.g. grep -n '^pater,'.",
 "notes": "Built from djvu.xml; large (4.6 MB)."
}
===== HUB
{
 "title": "H. Hübschmann, Persische Studien, Strassburg 1895",
 "edition_found": "1895 (Google scan)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/persischestudie00hbgoog",
 "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt",
 "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number.",
 "notes": "Built from djvu.xml (no hocr); OCR quality moderate.",
 "cites": "page number of Hübschmann, Persische Studien (1895)"
}
===== FSD
{
 "title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)",
 "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/in.ernet.dli.2015.147439",
 "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt",
 "page_offset": "vol1: leaf = p + 41..56 (drifts; e.g. leaf 87 = p.46, leaf 612 = p.556); vol3: leaf = p - 1466 (e.g. leaf 215 = p.1681); vol4: leaf = p - 2144..2148 (e.g. leaf 229 = p.2373); vol2 offset not reliably detected (pages ~ 700-1640) - grep the headword. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Headword in bold at line start with pronunciation; etymology in brackets at entry end '[< L. ...]'. Very large OCR (16 MB per vol); grep -n '^word' vol file.",
 "notes": "Nourai cites 1940; page numbers in the New Standard were stable 1913-1940s (single-volume pagination 1-2814 continues across the DLI volumes). local_files: /home/sfmqrb/git/rish
===== WEB
{
 "title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)",
 "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w",
 "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/WEB_vol1.txt",
 "page_offset": "not reliably detected (page_numbers.json sparse); grep headword. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Headword bold at line start; etymology in brackets. 2nd-edition pagination is the same across 1958-1983 printings, so a 1978 page number can be checked in the 1962 vol. 1 scan for words A-(mid alphabet); vol. 2 only via lending copies.",
 "notes": "",
 "cites": "page number of Webster's New Twentieth Century Dictionary, 2nd ed."
}
```


## [2026-09-07T01:37:35.894Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"===== POK_full lemma mā-ter\"\ngrep -n \"lemma: mā\" POK_full.txt | head -40\necho \"===== POK_full lemma mater\"\ngrep -n -i \"lemma: ma\" POK_full.txt | head -40"
}
```


### [2026-09-07T01:37:35.966Z] TOOL RESULT

```
===== POK_full lemma mā-ter
===== POK_full lemma mater
57036:Root / lemma: mahd- 
57042:Root/ lemma: mad-: wet; glossy, fat, well-fed, intoxicating : Root/ lemma: meA^w. honey, 
57113:Root / lemma: mahghos, -a 
57148:Root / lemma: mahgh- : mahgh- 
57154:Root/ lemma: mahgh-. mahgh-: to be able; to help; power, sorcerer : Root/ lemma: 
57194:Root / lemma: mahgh- 
57212:Root / lemma: mahg- 
57250:Root / lemma: maih-1 
57289:Root / lemma: maih-2 {moih-1) 
57304:Root / lemma: mahkh-o-s, -(s)lo- 
57324:Root / lemma: mahk- 
57344:Root / lemma: mahRo- or mohR-o- {*mahgho-) 
57367:Root / lemma: mahnd- 
57390:Root / lemma: mahnu-sor mohnu-s 
57430:Root / lemma: mahrtio- 
57445:Root / lemma: mahth-1ox mohth- 
57459:Root / lemma: maht-2 
57474:Root / lemma: mahu-ro- 
57496:Root / lemma: mazdo-s 
57510:Root / lemma: mahk(en)- 
57524:Root / lemma: mahk-1 
57546:Root / lemma: mahk-2 
57563:Root / lemma: mahR- : mahR- 
57589:Root / lemma: mah-1 
57654:Root / lemma: mah-2 
57685:Root / lemma: mah-no-, mah-ni- 
57703:Root / lemma: mahter- 
57758:Root / lemma: mah 3 
60185:lemma: mah-1 \ to becl<on with the hand; to deceive + with formants -ra-: 
60231:deception ', etc.; See Root / lemma: mah-1\ to beckon with tlie liand; to deceive + with 
61121:Root/ lemma: ma-r. Gen. ma-n-es, mQtos 
61374:Root / lemma: moruT- : ant, derived from Root / lemma: mai-1 : to cut down, work with a 
84297:pate(r)Qer\. patr-es, -ds: father', Root/ lemma: mater-: mother'. Root/ lemma: b'^rater-:
```


## [2026-09-07T01:37:37.634Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"== AHD watkins m2 / mater\"\ngrep -n -i \"^m[āaă]ter\" AHD_watkins1985.txt | head -20\ngrep -n -i \"mater-\" AHD_watkins1985.txt | head -20\necho \"== AHD mamma\"\ngrep -n -i \"^mā-\" AHD_watkins1985.txt | head"
}
```


### [2026-09-07T01:37:37.741Z] TOOL RESULT

```
== AHD watkins m2 / mater
154:A large number of kinship terms have been reconstructed. They are agreed in pointing to a society that was patriarchal, patrilocal (the bride leaving her household to join that of her husband’s family), and patrilineal (de- scent reckoned by the male line). “Father” and “head of the household” are one: peter-, with his spouse, the mater-. These terms are ultimately derived from the baby-talk sylla- bles pa(pa) and ma(ma), but they had a socio- logical significance in the Indo-European family over and above this, which is marked by the kinship-term suffix -ter-. Related terms are found for the grandfather (awo-) and the maternal uncle (*awon-), and corre- spondingly the term nepét- (feminine *nepti-) applied to both grandson (perhaps originally daughter’s son) and nephew (sis- ter’s son). English soON and DAUGHTER clearly reflect Indo-European *siénu- (from seue-') and dhughater-.
730:tive masculus, male, manly: MACHO, MALE, MASCULINE; EMASCULATE.] mat-. A kind of tool. Old English mattuc, mattock (prob- ably borrowed from Vulgar Latin *mattea): MATTOCK. [Pok. 2. mat- 700.] mater-. Mother. Based ultimately on the baby-talk form ma-2, with the kinship term suffix -fer-. 1. Germanic *méthar- in Old English mddor, mother: MOTHER}. 2. Latin mater, mother: MATER, MATERNAL, MATERNITY, (MATRICULATE), MATRIX, MATRON; MADREPORE, MATRI- MONY. 3. Greek métér, mother: METRO-; METROPOLIS. 4, Latin mdteriés, materia, tree trunk (< “matrix,” the tree’s source of growth), hence hard timber used in carpentry, hence (by a calque on Greek Aulé, wood, matter) substance, stuff, matter: MATERIAL, MATTER. 5. Greek compound Démétér, name of the goddess of produce, especially cereal crops (dé-, possibly meaning “earth”): DEMETER. [Pok. mdter- 700.] math-. Worm. With uncertain preform, but clearly re- lated, is Old English moththe, moth: motu. [Pok. 1. math- 700.] [Mawort-. Name of an Italic deity who became the god of war at Rome (and also had agricultural attributes), hence also the name of the planet Mars (doubtless from its red color, the color of blood). Latin Mars (stem Mart-), Mars: MARCH, MARS, MARTIAL, MARTIAN.] mazdo-. Pole, rod, mast. Germanic *mastaz in Old Eng- lish mest, mast: MAST}. [Pok. mazdo-s 701.] me-1. Oblique form of the personal pronoun of the first person singular. For the nominative see eg. 1. Germanic *mé- in Old English mé (dative and accusative): ME, MYSELF. 2. Possessive adjective “mei-no- in Germanic *min- in: a. Old English min, my: MINE?, My; b. Middle Dutch mijn, my: MYNHEER. [Pok. 1. me- 702.] me-2, In the middle of. 1. Suffixed form *me-dhi in Germanic *mid- in Old English mid, among, with: MID- WIFE. 2. Suffixed form *me-ta in Greek meta, between, with, beside, after: META-. See also medhyo-. [Pok. 2. me- 702.] mé-1, Expressing certain qualities of mind. Contracted from *meo-. 1. Suffixed o-grade form *mé6-to- in Ger- manic *méthaz in (i) Old English méd, mind, disposition: MooD! (ii) Old High German muot, mind, spirit, in German Gemiit, spirit, feelings, temperament: GEMUT- LICH, GEMUTLICHKEIT. 2. Perhaps Latin més (< *mé-s-), wont, humor, manner, custom: MORAL, (MORALE), MORES, MOROSE. [Pok. 5. mé- 704.] m6-2, To measure. Contracted from *meo-. I. Basic form mé-. 1. Suffixed form *mé-lo- in Germanic *mélaz in Old English m#l, “measure, mark, appointed time, time for eating, meal”: MEAL?; PIECEMEAL. 2. Suffixed form *mé-ti- in Latin métiri, to measure: MEASURE, (MEN- SURAL); (COMMENSURATE), DIMENSION, IMMENSE. 3. Possibly Greek metron, measure, rule, length, propor- tion, poetic meter (but this is referred by some to med-): METER!, METER?, (METER?), -METER, METRICAL, -METRY; DIAMETER, GEOMETRY, ISOMETRIC, METROLOGY, METRO- NOME. 4, Suffixed form *mé-trd- in Sanskrit mdtrd, a measure: MAHOUT. II. Extended and suffixed forms *mén-, *mén-en-, *mén-s-, *mén-dt-, moon, month (an ancient and universal unit of time measured by the moon). 1. Germanic *ménén- in Old English ména, moon: Moon; (Monpay). 2. Germanic *ménéth- in Old English ménath, month: MONTH. 3. Greek mén, méné, month: AMENORRHEA, CATAMENIA, DYSMENORRHEA, (MENARCHE), MENISCUS, MENOPAUSE. 4. Latin ménsis, month: MENSES, MENSTRUAL, (MENSTRUATE); BIMES- TRIAL, SEMESTER, TRIMESTER. [Pok. 3. mé- 703, ménot- 731. fen Big. Contracted from *meo-. 1. Suffixed (compara- tive) form *mé-is- in Germanic *maiz6n- in Old English mara, greater, and madre (adverb), more: MORE. 2. Suf- fixed (superlative) form *mé-isto- in Germanic *maista- in Old English m&st, most: Most. 3. Suffixed o-grade
1419:DEMENT men-1 DEMETER mater- DEMILUNE leuk- DEMIT (s)meit(a)- DEMIURGE da-, werg- DEMOCRACY da- DEMOLISH mé6- DEMON da- DEMONSTRATE men-! DEMOPHOBIA da- DEMOS da- DEMOTIC da- DEMUR mere- DEN dan- DENARIUS dekm DENARY dekm DENDRO- deru DENDRON deru DENIER? dekm DENIGRATE negW-ro- DENOMINATE no-men- DENOUEMENT ned- DENOUNCE neu-! DENSE dens-2 DENTAL dent- DENTATE dent- DENTI- dent- DENTICLE dent- DENTIFRICE bhréi- DENUDE nogw- DENY ne
== AHD mamma
```


## [2026-09-07T01:37:48.921Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -o \"ma-2[^.]*\\. [A-Z][^[]\\{0,400\\}\\[Pok[^]]*\\]\" AHD_watkins1985.txt | head -5\necho \"---- broader\"\ngrep -n -o \".\\{200\\}ma-2, Mother.\\{600\\}\" AHD_watkins1985.txt | head -3"
}
```


### [2026-09-07T01:37:50.170Z] TOOL RESULT

```
---- broader
```


## [2026-09-07T01:37:50.495Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"== POK_full mahter- entry (line 57703)\"\nsed -n '57703,57760p' POK_full.txt\necho \"== POK_full mah-2 (57654)\"\nsed -n '57654,57705p' POK_full.txt"
}
```


### [2026-09-07T01:37:50.564Z] TOOL RESULT

```
== POK_full mahter- entry (line 57703)
Root / lemma: mahter- 

Meaning: mother 

Note: based on a babble-word mah-, see there. 

Material: Old Indie matar-^moihef, Avestan matar-, Armenian ma/r6s. (Gen. maur= gr. 

|jr|Tp6(; etc.); Old Phrygian Nom. Akk. parap, paTspav, Gen. paTsps^; gr. Mnrrip, Doric 

Ijairip (with postponed nominative accent as Guyarrip); in addition hom. Ar||jr|Tr|p, 

Thessalian AappaTspi; alb. motre^ sister ' (originally ' the older sister representing 

mother's place '); Latin mater, -//75 'mother, wet nurse', Oscan maatrefs, Umbrian matrer 

'of a mother '; gall. (?) Marpspo ' mothers '; Old Irish /77a//7//'' mother' (cymr. modrydaf 



'beehive' with bydarv\es\. of wild bees' as 2. part); Old High German muoter, Old English 
modor. Old Icelandic /77od//'' mother'; Lithuanian /77d/e(Gen. Old Lithuanian motes, 
Lithuanian moters) 'woman, wife' (/77d/K/7a 'mother', motera^ female, woman'), Latvian 
/77a/e 'mother'. Old Prussian muti, /77c»//7e' mother' {pomatre' stepmother'); Old Church 
Slavic mati{Qev\. matere) 'mother'; Tocharian A macar, B macer. 

In derivatives (e.g. mahtruuii) compare: 

Old Indie matrka-^ maternal ', m. 'mother's brother', /77a//'/r5 'mother, grandmother'; but 
ncymr. modryb^ mother's sister', acymr. modrep-edP\., abret. motrep, nbret. moereb6s. 
( *matrok"'a, to ok"'- 'see', as ' looking like a mother '); 

gr. [jriTpa f. ' womb, uterus, marrow of the plant ', Latin matnx^ a mother in respect to 
propagation, a breeding-animal, of plants, the parent-stem, womb, matrix, a source, origin, 
cause ', Old High German muodar' belly of a serpent ', andd. moder. Old Frisian mother^ 
Brustbinde der Frauen ', Middle High German mueder. Modern High German Mieder, 



Armenian mauru, Gen. maurur stepmother ' ( *matruuia =) gr. priTpuici ' stepmother ', to 
/7-stem extended in Old English modrige. Old Frisian modire. Middle Low German modder 
'mother's sister' {*mddruuidn-. Old High German/77^c»/e/'5ds. reshaped aiter muofe/^), 
with lengthened grade forms *matrd[u]-. gr. (jnipajc;, -u)[F]oq, Doric jjarpux; ' uncle or 
grandfather on the mother's side', pHTpwiOf; ' maternal ' (meaning changes after Mnrrip); 

Latin matrona 'wife'; matertera 'mother's sister ' ( *matro-tera)\ materia, materies 'stuff, 
matter, material, timber, substance'; gall. FIN Matrona'nyer in France; region in France ' = 
cymr. GN Modroni. 

Slavic *matero-\n russ. /77a/e/'£y "extraordinary, big, large, strong, tight, firm', serb. mator 
'old, esp. of animals'. Old Bulgarian matertstvo^ rrpsapsTov ' (: Latin materies). 

References: WP. II 229 f., WH. II 49 ff., Berneker II 25, Trautmann 170 f. 
Page(s): 700-701 

Root / lemma: mah 3 

Meaning: mother (expr. root) 
== POK_full mah-2 (57654)
Root / lemma: mah-2 
Meaning: good, timely 



Material: With formants -no-0\d Latin manus' good ', /mman/'s 'temb\e\ adverbial mane, 

manrear\Y, matutinal'; 

Latin mane : Italian mattino : Spanish mahana : French matin : Corsican mane ; matina : 

Galician maha : Irish maidin : Portuguese manha : Sardinian Campidanesu mangianu ; 

mengianu > alb. mengjes^ morning' (special relation Sardinian = Albanian). 

here also Latin manesi. " the secluded souls ', later " underworld, death '; perhaps 

Phrygian [jriv 'secluded soul', pavia " KoAr) '; or belongs Latin manes to gr. |jr|viq, Doric 

Ijavig 'grudge'? compare S. 727. 

With dormant: Latin Matuta' the goddess of the early morning, the morning brightness, 
but also the maturity, the ripeness', matut/hus' matutinal ', maturus^ timely = mature, ripe, 
mellow, seasoned ' (based on *ma-tu-, perhaps 'good, suitable time'), Oscan Maatufs 
( *MatTs = ' dl Manes '); reduced grade perhaps Celtic *ma-ti- in Old Irish maith, cymr. mad, 
corn, mas. Middle Breton mat, nbret. mad^ good ' and gall. PN Matidonnus, Teuto-matos, 
also Old Irish maithid^ forgives '. 

References: WP. II 220 f., WH. II 27 f., 53 f. 
Page(s): 693 

Root / lemma: mah-no-, mah-ni- 

Meaning: wet, damp 

Material: Latin mano, -are^ to flow, run, trickle, drop, drip ', hence ' rise'; bret. Vannes man 

' moss, lichen', cymr. mawn^iurV from brit. *mdni-, from which borrowed Old Irish moini. ' 

moss, swamp, marsh, turf'; perhaps in addition ablaut, asachs. -mannia, -menn/a\n FIN 

and PN, as Throtmennia^ Dortmund ', etc. (under the influence of common Celtic -a7s-, -nt- 

> -nn-). 

References: WP. II 224, WH. II 30 f., J. Loth RC 42, 91 f. 

Page(s): 699-700 

Root / lemma: mahter- 

Meaning: mother
```


## [2026-09-07T01:37:55.652Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '57758,57800p' POK_full.txt"
}
```


### [2026-09-07T01:37:55.717Z] TOOL RESULT

```
Root / lemma: mah 3 

Meaning: mother (expr. root) 

Note: redupl. mahma, mahmma, partly (dissimilation?) mahna, /77a/7/7a of dubious age 

Material: Old Indie /77a 'mother'; 



Doric pa '|jr|T£p!' (in pa ya "o mother eartli', Aisch.), wliereof Ionian Attic paTa "motlier, 
wet nurse, midwife ', Doric 'grandmother'; derived Middle Low German moje^ mother's 
sister ', Old High German holz-muoja " witch '; 

Old Indie mama-vocatWe m. "uncle' (from *mama^ mother's sister'); npers. mam, 
mama, mamfmoihex'; 

Maybe vocative alb. mami^ mother', mamia' midwife '. 

Armenian /775/77 "grandmother' (gr. loanword as papl); gr. papipa baby word vocative, 
whereof Ionian Attic MOMMH mother', pappia "mother'; Latin 7775/77/775 nickname of affection 
"mama, ma, mommy, mom, mother', also " brisket ', mamilla^ nipple '; alb. meme Geg 
mame' mother'; Irish cymr. corn. bret. /775/77 "mother'. Old Irish mu/mmeloster mother' 
{*mammia)\ Modern High German Alemannian /775/77/77e "mother', changing through ablaut 
Old High German muoma' mother's sister'. Modern High German Muhme, Lithuanian 
mama, moma, Latvian mama ds.; russ. (etc.) /775/77a"mama, ma, mommy, mom, mother'; 
Hittite divinity Mamma; compare Asia Minor Mr|vr|, ngr. pavva "mother'. Old Icelandic 
/770/75 "mother', Middle Low German *mdne, mome^ mother's sister '. 

References: WP. II 221 f., WH. II 21 f., Traulmann 168; ma\s (?) base from mater- {see 

there). 

Page(s): 694 

Root / lemma: meM^i- meMNo- 

Meaning: middle 

Material: Old Indie madhya-, Avestan maidya-^ medial', Superl. Old Indie madhyama-, 

Avestan madema-' medial' (= Gothic miduma);
```


## [2026-09-07T01:38:12.909Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"===== SYN MOTHER\"\ngrep -n \"2\\.36\" SYN.txt | head -10\ngrep -n \"^MOTHER\" SYN.txt | head\necho \"===== SKT MOTHER\"\ngrep -n \"^MOTHER\" SKT.txt | head\necho \"===== SKT MAMMA\"\ngrep -n \"^MAMMA\" SKT.txt | head"
}
```


### [2026-09-07T01:38:12.998Z] TOOL RESULT

```
===== SYN MOTHER
1169:Lat. costa ‘rib’ and ‘side’ (12.36) > It. costa, Fr. céte (OFr. coste) ‘side’ and ‘coast’, Sp. cuesta ‘slope’ but costa ‘coast’, Rum. coastd ‘rib, side, coast’. OFr. coste > ME coste ‘side’ and ‘coast’, NE coast; > Du. kust, MLG kost > Sw. kust; > NHG kiiste > Dan. kyst. The Gme. loanwords, in contrast to the Ro- mance words, are fully specialized to ‘coast’. REW 2279. Falk-Torp 612.
1852:Grk. “EpeBos ‘place of nether darkness (myth.), Skt. rajas- ‘dim space, cloud, etc’. Walde-P. 2.367. Feist 399.
1998:4. Goth. rign, OE regn, etc., general Gme., etym. dub., perh. (rek- beside reg-?) : ON rakr ‘wet’, Lat. rigare ‘moist- en, water’ (with 7 fr. cpds.), etc. Walde- P. 2.365. Falk-Torp 887. Feist 397.
2255:| CHAPTER 2 MANKIND: SEX, AGE, FAMILY RELATIONSHIP 9.1 Man! (Human Being) 2.47 GRANDMOTHER 9.91 Man? (vs. Woman) 2.48 GRANDSON 2.92 Woman 2.49 GRANDDAUGHTER 2.93 MALE’ 2.51 UNcLE 9.94 TeMALE 2.52 AUNT 9.942 Sex 2.53 NEPHEW | 9.25 Boy 2.54 NIECE 9.26 GIRL 2.55 CousIN | 2.27 CHILD 2.56 ANCESTORS 2.28 INFANT 2.57 DESCENDANTS 231 HUSBAND 2.61 Fatuer-1n-Law ~ 2.32 Wire 2.62 Morser-in-Law 2.33 Marry 2.63 Son-1n-Law 2.34 Marriage; WEDDING 2.64 DauGuHTEr-in-LAw 2.35 FaTHER 2.65 BrotuEr-in-Law 2.36 MoTHER 2.66 SisteR-1n-Law | 2.37 PARENTS 2.71 STEPFATHER 2.41 Son 2.72 STEPMOTHER 2.42 Daucuter 2.73 STEPSoN | 2.43 Cuiup (Son or Daughter) 2.74 STEPDAUGHTER 2.44 BroTuHEr 2.75 ORPHAN 2.45 SISTER 2.76 Wipow 2.452 BrotHEer(s) AND SISTER(s) 2.81 RELATIVES 2.46 GRANDFATHER 2.82 FamiIny 2.1 MAN! (Human Being) oy ae por Goth. manna Lith.  Zmogus, pl. Zmonés iy ae eee s oN maor, gumi Lett. cilveks It. heinb - an. —menneske ChSl. elovékit Tr. iter an menniska SCr. Eoujek Sp. hombre ME man(n), guma Boh. tlovtk Rum. om man Pol. czlowiek Tr. duine NE man Russ. elovek Nir. duine Du. mensch Skt.  manu-, purusa- W. dyn OHG man, mannisco, gomo Av. __masya-, masyaka-, Br. den MHG mensch OPers. martiya- NHG mensch
2781:MANKIND: SEX, AGE, FAMILY RELATIONSHIP 103 2.35 2.36 2.37 FATHER MOTHER PARENTS
2813:2.36. ‘Mother’. 1. IE *mdter-, prob.
5405:Skt. roman-, loman- (b), prob. : Ir. ruamnae, gl. lodix (meaning here?), NIr. riaimneach ‘long hair, horsehair, fishing line’, also Ir. riiainne ‘a hair’, ron, W. rhawn ‘horsehair’, Br. reun ‘coarse hair, bristles’. Walde-P. 2.361.
5492:4, Lith. ragas, Lett. rags (OPruss. ragis ‘hunting-horn’), ChSl. rogt, etc., general Balto-Slavic, without outside connections. Walde-P. 2.367.
5876:(only in epds.), IE *sek”- ‘point out, say, see’. Walde-P. 2.366, 377 ff. Pedersen 2.621.
5877:W. llygad, Br. lagad, prob. (with Br. a for u by assim.) : W. llwg ‘bright’, go-lwg ‘sight’, Grk. Neboow ‘see’, Skt. lok-, loc- ‘look, see’, locana- ‘eye’, etc. Walde-P. 2.381, 411. Pedersen 2.36.
===== SKT MOTHER
===== SKT MAMMA
```


## [2026-09-07T01:38:15.084Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"===== PHD mad/madar/matak/mayag\"\ngrep -n \"^m[āa]d \" PHD.txt | head\ngrep -n \"^m[āa]dar\" PHD.txt | head\ngrep -n \"^m[āa]dag\" PHD.txt | head\ngrep -n \"^m[āa]y\" PHD.txt | head\ngrep -n \"^m[āa]diy\" PHD.txt | head\necho \"--- context\"\ngrep -n -i \"mother\" PHD.txt | head -20"
}
```


### [2026-09-07T01:38:15.182Z] TOOL RESULT

```
===== PHD mad/madar/matak/mayag
2693:mad dēwānag.
127:mayānjīg ... add arbiter. for | !"?mez- read ! *mēz-, v. 'mēzišn, mistan.
465:may [HS < A hmr ?; mdy | M my, № ~] wine.
466:mayān [mdy’n' | М my’n, N miyān] middle; among, between. ~ag [-k! | N ~a] middling, average.
467:mayšnjig [mdy'ncyk! | N miyānji] mediator, intermediary. ~th: mediation.
468:mayg [КМСА < A ату; так! | N ~] locust.
469:māyišn [m'dfn!'] copulation.
4778:may appear written as * Q35
--- context
437:ma [AL < À °l | M m, N ~] not (prohibitive). ~ agar [N magar] perhaps; lest. mad [AM < A ?m-y, v. madar | M md] mother.
439:~ith: femininity. *madag [mtk' | (M myg, N māya)] essence, substance. ~ig [-yÀ!] essential. ~war [-w/] essential, especial, principal. madan [mtn! | M mdn] come. madār [т comer. mādar [AMYtl < А т-у; mtl | M mdr, N ~] mother. imādayān [m!tgd?n! | М m'dy'n] book. *mādayān [m tyd?n'] essence, basis, core; essential, chief. mādayār [m tgd’l] steward; (chess) rook, castle. mādišt [m’tyst'] *matter, protoplasm. mādīyān [m’tyg?n | N ~] mare. may [my | N ~] hole, pit. magas [mks | P mgs, N ~] fly. ~ i angubén: honey-bee. magind [mkn'd | M mgyn(d)] shield, protection.
2853:mother mad(ar).
```


## [2026-09-07T01:38:28.900Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nd=open('PHD.txt',encoding='utf-8',errors='replace').read()\npages=d.split('\\f')\nfor i,p in enumerate(pages):\n    if 'mādīyān' in p or 'mādar [' in p:\n        print('leaf',i,'printed',i-21)\n        print(p[:3000])\n        break\nEOF"
}
```


## [2026-09-07T01:38:29.236Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SYN p.103 area 2.36\"\nsed -n '2813,2860p' SYN.txt"
}
```


### [2026-09-07T01:38:30.312Z] TOOL RESULT

```
leaf 77 printed 56
 lābakkar [Pfkkl] suppliant.
— h: supplication. lajan [/cn! | N ~] mud, slime. larzidan, larz- [ilc-ytn' | P Irz-, N ~] shiver, tremble. laškar [ISk] | N ~] army.
laSkarig 53
~ig [-yk! | N ~i] soldier.
~igih : soldiering. lawzénag [lwcynk' | N ~ina] almond sweetmeat, marzipan. *lipi [/pyh] a minute (of arc).
M
ma [AL < À °l | M m, N ~] not (prohibitive). ~ agar [N magar] perhaps; lest. mad [AM < A ?m-y, v. madar | M md] mother.
!mádag [NKB < А ngb; m'tk! | (M myg), N mada] female.
~ith: femininity. *madag [mtk' | (M myg, N māya)] essence, substance. ~ig [-yÀ!] essential. ~war [-w/] essential, especial, principal. madan [mtn! | M mdn] come. madār [т comer. mādar [AMYtl < А т-у; mtl | M mdr, N ~] mother. imādayān [m!tgd?n! | М m'dy'n] book. *mādayān [m tyd?n'] essence, basis, core; essential, chief. mādayār [m tgd’l] steward; (chess) rook, castle. mādišt [m’tyst'] *matter, protoplasm. mādīyān [m’tyg?n | N ~] mare. may [my | N ~] hole, pit. magas [mks | P mgs, N ~] fly. ~ i angubén: honey-bee. magind [mkn'd | M mgyn(d)] shield, protection.
mānbed
mah [B YRH < А b-yrh;mh| = М, N ~] moon, month; cal. 12th day.
mahig [m’hyk' | M m'hyg, N mahi] fish; astr. Pisces.
māhīgān [BYRH-, m'hykEn! | M whyg’n, N māhiyān] month.
mahist [msst!, mhst! | M mhyst, N ~] greatest. makóg [mkwk' | M mkwg, N mako(k)] boat. mālīdan [m’lytn' | N ~] = muštan.
man [L < А l-y | M mn, N ~] I, me.
тап [mn | = M] house, dwelling.
!mán-, у. тапдап.
?màn- [m^n- | = M] live, dwell. ~išn: dwelling, sojourn.
män- [m?n- | = M, N ~] resemble.
manag [m?nk
```


### [2026-09-07T01:38:30.368Z] TOOL RESULT

```
=== SYN p.103 area 2.36
2.36. ‘Mother’. 1. IE *mdter-, prob.
starting fr. a nursery word of the pa type (above, p. 94) orig. pd, reduced to pa before the accent. Walde-P. 2.4. Here belong the Grk., Lat., Ir., Gme., and Indo-Iranian words, also Arm. hair, and Toch, A pacar, B pacer. In Balto-Slavic it is completely replaced. 2. Nursery words that have become oe usual terms. Type baba (above, p. ) in It. babbo, now a serious rival of padre, nes atta, tata (above, p. 94) in Rum. an ., Br. tad, Goth. atta (So reg., Vs. ihe) te and here not of earthly » Lith. tévas, Lett. tévs, OPruss.
taws, ChSl. otict , 3 , ete. (all the Balto- Slavic forms), Hitt. fae aad
starting fr. a nursery word of the ma type. Walde-P. 2.229. Here belong the Grk., Lat., Ir., Gme. (except Goth aipei), Balto-Slavic, and Indo-Iranian forms, also Arm. mair, and Toch. A macar, B macer. But Lith. moté became ‘woman’, and as ‘mother’ was replaced by the deriv. motyna.
2. Nursery words that have become the usual terms. Type mama (above, p. 94, Walde-P. 2.221) in It. mamma a serious rival of madre, and W., Br. mam.
Goth. aipei, prob. new fem. formed fr. some nursery word similar to, though not identical with, atta ‘father’. Feist 28.
Digitized by Arya Samaj Foundation Chennai and eGangotri
104 SELECTED INDO-EUROPEAN SYNONYMS
2.37. Words for ‘parents’ are fr. verbs for ‘beget’ or ‘bear’ (4.71, 72); fr. words for ‘old’; or are pl. or du. forms (the lat- ter, of course, more orig.), or derivs., of words for ‘father’, or rarely ‘mother’.
1. Grk. roxets (so reg. Hom.), or aor. pple. rexdvres : rixrw ‘beget, bear’ (4.71).
Grk., NG yovets : yiyvouat ‘be born’, yevvaw ‘beget, bear’ (4.71).
2. Lat. parentés (also ‘ancestors’, late also ‘relatives’), pres. pple. of par- in parere ‘bear, beget’ (4.72). Hence Rum. parinti ‘parents’, Fr. parents formerly ‘parents’ and ‘relatives’ (> ME paren- tes, NE parents), now ‘relatives’ (as ‘parents’ replaced by pére et mére), as also It. parenti, Sp. parientes. REW 6233.
Lat. patrés (as also Grk. rarépes) was commonly used for ‘forefathers’ and oc- casionally in late times for ‘parents’. Hence Sp. padres.
Lat. genitor ‘begetter, father’ : gig- nere ‘beget’, etc. Hence It. genitori.
3. Ir. tuistidi, NIv. tuismhightheoiri : Ir. do-fuismim ‘beget, bear’ (4.71).
W. rhieni (formerly also ‘ancestors’), epd. rhi-eni : gent ‘be born’, Lat. gig-
nere, etc., formed like Grk. mpéyovor ‘an- cestors’. Pedersen 2.533. Br. tad ha mam, after Fr. pére et mére,
4. Goth. bérusjés, orig. a nom. pl. fem. perf. act. pple. of bairan ‘bear’, For the fem., cf. Skt. mataradu, below. Feist 87 f.
Goth. fadrein ‘family’ and ‘parents’, sg. coll. (also pl. fadreina), deriv. of fadar ‘father’.
ON fedgin, deriv. of fadzr ‘father’.
Dan. foreldre, Sw. fordldrar (in the older language ‘forefathers’), OE ealdras, Du. ouders, OHG altiron, NHG eltern, all fr. the Gme. forms for ‘older’.
5. Lith. tévaz, pl. of tévas ‘father’. Lith. gimdytojaz : gimdyti ‘bear, be- get’ (4.71).
Lett. vecaki, fr. vecs ‘old’ (influence of *
NHG eltern prob.). ChSl. roditeli, ete. (all the Slavic words) : roditi ‘beget, bear’ (4.71).
6. Skt. pitardu, Av. pitara (once, Barth. 905), Skt. matarau, both ellipti- cal duals of pitar- ‘father’ or mdtar- ‘mother’, also copulative dual Skt. ma- taradpitara.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar ee
| |
. CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
MANKIND: SEX, AGE, FAMILY RELATIONSHIP 105
2.41 2.42 SON DAUGHTER
Grk. — tros, iets Ouyarnp
NG viés (yutds) Ouyarépa, Kopn
Lat.  filius, ndtus fila i
It. figlio, figliolo figlia, fighiola
Fr. fils fille
Sp. hijo hija
Rum. jiu Sited
Ir. mace ingen
Nir. mac ingheann
W. mab merch
Br. mab merc’ h
Goth. sunus dauhtar
ON sunr, sonr dottir
Dan. sn datter
Sw. son dotter
OE sunu dohtor
ME sune, sone daughter
```


## [2026-09-07T01:38:38.537Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nfor f,leaf,label in [('SKT.txt',356,'SKT p.336'),('HRN.txt',234,'HRN p.213')]:\n    pages=open(f,encoding='utf-8',errors='replace').read().split('\\f')\n    print('=====',label,'leaf',leaf,'of',len(pages))\n    print(pages[leaf][:2500])\nEOF"
}
```


## [2026-09-07T01:38:39.581Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT matar\"\ngrep -n \"mātar\" BRT.txt | head -20\necho \"=== BRT Mutter\"\ngrep -n \"'Mutter'\" BRT.txt | head -20"
}
```


### [2026-09-07T01:38:39.727Z] TOOL RESULT

```
===== SKT p.336 leaf 356 of 657
ritory,  a  wild  flower R^on  walU.  (F.-L.)  PtUilory trit&ry,  M.  E  pariiorii.—O,  F. ,  •pcllttofjr;'  Cot.  vL.  parUtaria, \  kul  oi pariftariur,  belonging  to m  faruf;  Stem  oi paries  (above). u  (F.-U-Gk.)  M.£./aW/fA/. MJW.^L.  jltsnrrMi.*Gk.  ro^ix/a, iiJiood :  hence,  an  ecclesiastical BpLv^puixoT,  neighbourint^.^Gk. 1^  ofxvr,  house,  abode,  allied  to i.  Der,  paruhicncr,  formed  by r  (needlessly)  to  M.  E  pariuktH Wrwitntmt  a  parishioner. hlAL  (U-Gk.)  U  pawAia/if. Ifilii,  lame  MUfarada  (above). :  tee  Par.
idoaed  gTomid.  (E)    Parkm^
a  F.  sficUing ;  bat  the  word
contraction  of  M.  E.
r,  A-S- Ptamu,  peamx
S.  p«trroe  is  formed,
•*r  (»  in  htileck)  from
enclo3«,    lock,   fasten.
/  U  seen  in  the  use  of
and  pmrrtm   as  equivalent
PARSNEP.
forms,  in  the  same  sense.  (Cf.  G.  sperrtn, to  shut.)  The  verb,  meaning  *  to  fasten with  a  spar  ot  bar/  is  formed  from  the  sb. Bpar  ( 0.  q.  v.  p.  The  word  is  common to  Teutonic  tongues ;  as  in  Du./Vr^,  Sued. Dan.  park,  G.  p/crck,  whence  not  only  F. part,  Ital.  parvo.  Span,  parque,  but  also Irish  and  Gael,  pairc,  W.  pari  and  paru*g (  -  E.  parrot),  Bret.  park.
paddock  (2),  a  small  enclosure.  <E.) Not  an  old  word ;  used  by  Evelyn  ;  a  cor- ruption of  M.  E.  parrok,  spelt  parrocke  in Palsgrave.    (So  t\^o poddish  io\ porridge.'^
Parley^  Parliament,  Parlotir;  see Parable.
Parlous ;  see  Perfl.
Parochial ;  <^e  FarlalL
Parody ;  see  Ode.
Parole ;  sec  Parable.
Faronymous ;  see  OnomatopoBia.
Paroxysm  ;  sec  Oxygen.
Parricide :  see  PatemaL
Parrot.  (F.  -  L.  -  Gk.)  F.  /erro/,  of which  the  lit  sense  is  '  little  Peter,*  given to  the  bird  as  a  nickname ;  see  Cotgrave. Also  written  Pitrrot,  both  forms  being  from Herrt,  Peter.  — L.  Pttrum,  ace.  of  Pttrus, Peter. —  Gk.  Wrpof,  a  stone,  rock;  also  Peter. I>er.  F.  perro>iuet,  borrowed  from  Span. ptriikito  or  periquito.  dimin.  of  Pfrito, I'eier;  sec  FarnQuito.  %  The  F.  word is  prob.  imitated  or  borrowed  from  Spaa, or  Portuguese.
Parry ;  see  Fare.
Parse ;  see  Part.
Parses,  an  adherent  of  the  old  Persian religion,  in  India.  (Pers.)  Pcrs.  pdrH,  a Persian.  —  Pers.  Pdrs,  Persia.
poach  (I),  a  fruit.  (F.  -  L.  -  Pert.'; M.  E  pickt.  -  O.  F.  pischi,  a  peach.  -  L. ptrsicHm,  a  peach ;  so  called  from  growing oD  the  Persua  arbor^  Persian 
===== HRN p.213 leaf 234 of 412
— 213 -
Np. /es-em ist eine Analogiebildung nach dem Muster
von nivSsem, nivisten; dasselbe gilt von phlv. l(i)8tan,
Käs. V. lissdfiy lissian, Kurd. listin, alistin, listnöväy
M. ISstin (H.-Sch.) sind Lehnworte.
M.
955. mä wir', ND^N (Is. 1, 9), vergl. -nidn (Enclit.).
Käs. (hnö, hamd, höm6 (d. i. *rfma).
ap. amä/am ((ien. Plur.); aw. aAmöA-o- 'unser'; päz.
emä; ai. asrndka-,
oss. d. t. ma/ 'wir, uns* (IH^^).
956. niädei; mrul (Patet's) 'Mutter, inäch, mfidlne 'weib-
lich, mädiydn 'Stute' ^), milkiyän 'Henne'^).
ap. ^mätar- in hamätil 'von der gleichen Mutter ;
aw. rndtar-; phlv. inät, mätar 'Mutter, mätak Veib-
lich', arm. LW. matak 'Weibchen'; ai. wätdr-; arm.
mair (H. No. 187).
kurd. mak {*mädk) 'Mutter, mOdek 'Büffelkuh'; af;'.
mar; oss. d. mäde, madä, t. mod, meid (175); bei. mät,
n. mad-j was 'Mutter (234), LW. maday, n. maday
'weiblich' (230) ; si^n. mod, minj. rnüya (vergl. g. maije,
Käs. K. maij möyä),
957. mäS Treude, Vergnügen'.
Zu ai. Vernäh', mähe (einmal), sonst mahdyati 'er-
freuen , ergötzen ; sich ergötzen' (N ö 1 d e k e , mündliche
Mitteilung).
ai. V^mah' ist wohl von mah- 'gross' abgeleitet (dies
ist auch Leumann's Meinung); vergl. besonders
mahfydtS ursprünglich, *er tut, als wenn er gross wäre*.
958. märe, mar 'Rechnung.
aw. 2 l^mar- 'sich erinnern', vergl. np. amar
(No. 47).
') LW. kurd. mäyen (H.-Sch.); bei. müdyän^ n. fnaf)in,
mäzin (231).
*J Wohl *müdkiyän^ vergl. kurd. mük.
```


### [2026-09-07T01:38:39.816Z] TOOL RESULT

```
=== BRT matar
=== BRT Mutter
```


## [2026-09-07T01:38:51.583Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"mother\\.\" SKT.txt | head -20\necho \"--- Mother, a female parent\"\ngrep -n -i \"female parent\" SKT.txt | head -20"
}
```


### [2026-09-07T01:38:51.645Z] TOOL RESULT

```
4934:•t  oiw  Mother.
10884:name,  due  to  the  existence  of  such  terms madtx-jc/va,  honeysuckle  (lit.  moth wood),  madrrdHitiv,  worxibine  (lit  molV bush),  madrt-pcrla,  mother  of  pearl.  Hcri ma*frt  is  from  L.  mafrtm,  ace  <4  maftf mother;  see  Mother.  Pora  U  from  Gl wSipoz,  a.  light  friable  stone,*  also  a  stalid tile.  ^  Itut  the  word  has  certainly  bed mtdefstaiHi  (prob.  misundtrttocd)  as  coa nccted  witn  pert,  whence  na  merool scientific  terms  such  as  taitm-pora.  tnbi pora^  dfnti-fora. gtmmUporn,  'Scientific' etymology  is  usually  clumsy,  and  frC quently  wrong.  We  may  conclude  t E.  fere  has  been  substituted  for  Gk. by  conftision.
11002:f/ia  ma,  a  mere  repetition  of  ma,  an  m> fnnliDe  iyllable.  Many  other  lan^ia^es have  something  like  it ;  cf.  F.  ma>r.JM, Span.  Du.  and  G.  mama,  Ital.  and  L, tnnmum^  a  child's  word  for  mother.
11220:Maternal.    (F.  -  L.)     F.  matm Low  L.  materttaiis.^X^  mattrmu, ing  to  a  mother.  —  L.  maler,  moKt naie  with  Molhar.
11221:matriolde,  murderer  of  a ••L.)    F.  matricieUt  adj.,  '  mo Cot.  —  L  motruida,  a  matricide.  — crude  form  of  mater,  mother ;  c slay;  sec  CsMura.  %  We  also  used cuic  to  represent  L.  matrUidimm^,  the of  a  mother.
11227:of  mater,  «  mother.
12513:Nun.  (L.)  M.  E.  and  A.S.  mwne.^ Low  L.  nunna,  nonria.  a  nun  ;  orig.  a  title of  respect;  oldcsit  sense,  '  mother.*  It  an- swers to  L.  ttouuus,  father,  also  a  monk, •f  <^Jk,  rfjKvr;,  aunt ;  Skt.  nand^  mother,  a famili.-vr  word  used  by  children.  Formed like  ma-ma,  da-Ha  {daddy)^  and  the  like. Der.  MUMtter-yj  from  U,  V.  rtfitittert'e,  which from  O.  F.  twnne  =  L.om  L.  ncnna*
20528:Uterine,  bom  by  the  tame  mother  of different  father.  (F.-L.)  F.  utehn,  '< the  wumb.  bom  of  one  mother  ;*  Cot.*] uterinus,  bora  of  one  mother.— L.  utam womb.
23803:Begum,  in  the  E.  Indies,  a  ladv  of  the highest  rank.  (Pers.  — Turk,  ana  Arab.) Pcrs.  bf^m.  a  queen,  lady  of  rank  ;  lit. '  mother  of  the  governor.' — Turk,  be^^  be/, a  bey,  governor;  Arab,  u/n,  umm,  mother.
--- Mother, a female parent
```


## [2026-09-07T01:38:53.197Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT search\"\ngrep -n \"mAtar\\|matar-\\|mātar\\|matar\" BRT.txt | head -20\necho \"=== BRT any m entries\"\ngrep -c \"\" BRT.txt\nhead -20 BRT.txt"
}
```


### [2026-09-07T01:38:53.272Z] TOOL RESULT

```
=== BRT search
11658:•  j.,  g.  Jitay-  f.  "Lefaen':  daya  mi  Stars  . . 33U  %räittm  äsu  °tlm  .  .  pouru  °tlm  Y. Ö2.4.  a)  als  Adj.  'lebendig':  apascä vä  .  .  matard  'tayS  (VP.)  V.JÄ  £.
19461:Zum  ai.  V.  mtthele  'sie  schwanken  hin  und her'(?)»),  got  inmaidj'an  'immatare' (usw.).  — VgL  M«äö.,  mSiö;  Gdn.  BB.  15.  257.  — Pü.:  andar  mikan.  —  0  RV.  /.  113-  3i  im Gegens.  lu  laslhaiufy.  SSVa^/a  freilich /o/rw- fararn  Aimilah.
28628:j  N.  42;  —  spa  .  .  stamantm  kl  mai  nyä- saym  .  .  dasimm  hl  gaeiTtn  .  .  Aöyum  kl \gaosfm  upa^Wfrfsayitt  .  .  doTimtn  Al 'paßyqm  .  .  kaoyqm  hl  paiiyqm  upa.- ksr^ntay^n  .  .  dum^mcil  Al  (zu  a)  upa.- '^lionsaym  V.  13. 30  ff,;  8.  40,  5. 1 7  ff.  (oft), 49,  H.2.  18,  36;  —  Aavatianö  (sd.)  äaityS gatuÜ  .  .  Aaffyaj  *Al^^  *nalmat  Omatars R  7p;  *7P'^  Yl/o.  ioo',  126,  Ä  38,  V. 79.  2;  —  nairika  .  .  airime  (sd.)  gätüm ^?  (fem,;  zu  ß)  nisAihalta  V.i6.&;g.^^ (mask,);  —  ahmi  nairi . .  b^m/ayän/i  fsd.) /l . ,  mänh^m^a  hvarfca  aamca  Al{za  a) bfr^Jaim  V, 7.  52;  —  sünahe  .  .  asti  sl haHn  ya%a  a^aurune  V,  13.  44;  44'; —  yS  ga'hanqm  *anu.tnaiti  (sd.)  *afm.- mainyete . .  anyS  vä  hl  (zu  a)  daAmB  srvth ga%ä  dalaiti  N.  25;  —  azdibji. .  *usäan3m h  i (Plnr.)  alat  k^rmaot  Y.  6. 50; — *Aixsa»e . .  drvatqm  .  .  anyqm   i4?(PIur.)  avarptqta
=== BRT any m entries
30725
Google
This  is  a  digital  copy  of  a  book  that  was  prcscrvod  for  gcncrations  on  library  shclvcs  bcforc  it  was  carcfully  scannod  by  Google  as  pari  of  a  projcct
to  make  the  world's  books  discoverablc  online.
It  has  survived  long  enough  for  the  Copyright  to  expire  and  the  book  to  enter  the  public  domain.  A  public  domain  book  is  one  that  was  never  subject
to  Copyright  or  whose  legal  Copyright  term  has  expired.  Whether  a  book  is  in  the  public  domain  may  vary  country  to  country.  Public  domain  books
are  our  gateways  to  the  past,  representing  a  wealth  of  history,  cultuie  and  knowledge  that's  often  difficult  to  discover.
Marks,  notations  and  other  maiginalia  present  in  the  original  volume  will  appear  in  this  flle  -  a  reminder  of  this  book's  long  journcy  from  the
publisher  to  a  library  and  finally  to  you.
Usage  guidelines
Google  is  proud  to  partner  with  libraries  to  digitize  public  domain  materials  and  make  them  widely  accessible.  Public  domain  books  belong  to  the public  and  we  are  merely  their  custodians.  Nevertheless,  this  work  is  expensive,  so  in  order  to  keep  providing  this  resource,  we  have  taken  Steps  to prcvcnt  abuse  by  commercial  parties,  including  placing  lechnical  restrictions  on  automated  querying. We  also  ask  that  you:
+  Make  non-commercial  use  ofthefiles  We  designed  Google  Book  Search  for  use  by  individuals,  and  we  request  that  you  use  these  files  for personal,  non-commercial  purposes.
+  Refrain  fivm  automated  querying  Do  not  send  automated  queries  of  any  sort  to  Google's  System:  If  you  are  conducting  research  on  machinc translation,  optical  character  recognition  or  other  areas  where  access  to  a  laige  amount  of  text  is  helpful,  please  contact  us.  We  encouragc  the use  of  public  domain  materials  for  these  purposes  and  may  be  able  to  help.
+  Maintain  attributionTht  GoogXt  "watermark"  you  see  on  each  flle  is essential  for  informingpcoplcabout  this  projcct  and  hclping  them  lind additional  materials  through  Google  Book  Search.  Please  do  not  remove  it.
+  Keep  it  legal  Whatever  your  use,  remember  that  you  are  lesponsible  for  ensuring  that  what  you  are  doing  is  legal.  Do  not  assume  that  just because  we  believe  a  book  is  in  the  public  domain  for  users  in  the  United  States,  that  the  work  is  also  in  the  public  domain  for  users  in  other countries.  Whether  a  book  is  still  in  Copyright  varies  from  country  to  country,  and  we  can'l  offer  guidance  on  whether  any  speciflc  use  of any  speciflc  book  is  allowed.  Please  do  not  assume  that  a  book's  appearance  in  Google  Book  Search  mcans  it  can  bc  used  in  any  manner anywhere  in  the  world.  Copyright  infringement  liabili^  can  be  quite  severe.
Äbout  Google  Book  Search
Google's  mission  is  to  organizc  the  world's  Information  and  to  make  it  univcrsally  accessible  and  uscful.   Google  Book  Search  hclps  rcadcrs discover  the  world's  books  while  hclping  authors  and  publishers  rcach  ncw  audicnccs.  You  can  search  through  the  füll  icxi  of  ihis  book  on  the  web
at|http: //books.  google  .com/l
db,Google
db,Google
db,Google
```


## [2026-09-07T01:39:02.686Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -o \".\\{60\\}M[au][tl]t[e0o]r.\\{60\\}\" BRT.txt | head -30"
}
```


### [2026-09-07T01:39:02.734Z] TOOL RESULT

```
3092:  Wasser,  rufen  wir  an  als  die  träch- tigen und  die  Mutter-  und  die  melken Kühe,  die  fiir  den  Armen  sorgen,  d
14146: j.  driwray-  f.  'Flecken,  Mal'  (nur Komp.).  a)  bes. 'Muttermal' :  mä  dhra .  .  °wil  . .  mSia.am  anyqm  daxstanqm 
16972:  lo.  4;  —  '%ry3t  haca zavi/i (sd.)  V./5,6.  a)  sva. 'Mutterleib': aniaräj  nafmät  '^risva  uruhuidAva  (sd.) V.  5.  S
19749:vasttm  tanu.ftn- %attqm  "wenn  der  Vater . .  oder  die  Mutter stirbt,  wie  lang  soll  man  für  sie  die  Trauer- frist
19992:statt  Akk.)  *mimar?xl3ite  '"damit such  dein  Kind  (im  Mutterleib)  zu  töten  I' Dann  versucht  das  Mädchen  ihr  Kind
20278: F.  S):  ezmä- yün,  Hmüli^ai),  (zu  Vr.  //):  mäiatiA  'Mutter- schaft'; s.  noch  No.  4-  —  ')  Nach  Aia>R£AS bei  Hüs
20293:aiiä  .  .  'larS (VP.)  /aayff  (sd.)  Y.  JÄ  5;  —  von  Mutter- tieren :  apatca  vä  aztfäl  . .  'Urqlüä  (AP.) ..  agft
27319:  pm- dh-t  «...  —  5)  Them.  —  «)  Ersetzt  noTiat der  Mutterstelle  Y.  31.  zo.  —  7)  So  verbinde ich  troll  ZDMG. 
27736:rB  barüryät  Itaca  gapi/i( jSs-AoiH.)^^ "..  von  deiner  Mutter  ward  ich  angerufen" V.  ig.  6;  —  airyamantm  . .  yS 
27816:ger  Zar.  Du  bist  der  Sohn I'ourui'aspas.  Von  deiner  Mutter  ward ich  angerufen.  Schwör  ab  die  . .  mazd. Religion
29429:ind  missluDgcn. ■  p.  hainätar-  Adj.  'der  die  selbe  Mutter hat':  bardiya^ . .  '13  hamapita  ka''bU}iyahyä Bh.  /.
```


## [2026-09-07T01:39:08.194Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '20255,20300p' BRT.txt"
}
```


### [2026-09-07T01:39:08.239Z] TOOL RESULT

```
1166
•  j.  maäyäka-  m.  'Mensch*:  aaaßain\ syao'^nanam  yüt  vpnzinii  'ka  V,  75. 3; 2-3^  7-SS',5-».  ^7-3.  YtÄii,  23,  70.54,! i4.s,%  FrD.j,  Nik._j;  —  *ka  dagoayatS\ Yt.  14.  54;  —  paravB  (sd.)  ar  'ka  V.  i8.i;\ P,  22(?);  —  yaZsqmea  parS  °ka  .  .  gairi- nam  nämam  datarg  Wtig.C;  S.$i,  V./j.a, 6,' 77.  3,  1S.5;  —  usikUftata  -ka  (VP.)  V. JÄ16;   —   :^afsata   'k&nhs  FrW.10.4a;
—  t^'afsa  danys  (sd)  'ka  (VS.)  V.  18.16; -—  am?SaRt  pars  ava^ke  isitUi  °kSßkS AQg.41;  —  zara^ustrS  ys  paoiryS  'kB staota  aJftnVtij.iB; — yahmi  ssire mihrH.' drujS  . .  'käahö  Yljo.  80;  —  Aanjama- R>m  . .  hakra  mainyaoi^S  yasata^byS  .  . hahra  vahi^talibyS  'kaäbysy. 2.30;  S^ViZ.;
—  tum  aks  vahistasca  mihra  ahi  'kafibyS Yt/O.agjSo;  —  nmänShu  'kanqmy.62.1;
—  kar)taHt..yH  myrSire  sarahu  'kanqm Yt.  10. 40;  —  k»m  . .  'ka  (IS.?)  dagbs  aoüf (sd.)  yasaiU  V.  ly.  i.
Abteil,  aus  maSya-.  ~  Pü.:  martum.
•  j.  masyäna-  m.  sva.  maJ^a-i  saranu- iiialO  'nahe  Vyl.4-
Ableit  ans  maiya-t    Wertlo».
•  j.  maäyö.Jata-  Adj.  'von  Menschen  ge- tötet*: yai  am  yä  spö.Jatala  (sd.)  .  .  'fala
V.7.3-
Pü.:  martumän  iai,   erl.:  pa  dälaslärämaitdän 'von  solchen  mit  richterlicher  Gewalt'.
■  j.  maäyö.vaDha-  Adj.  'den  Menschen bekleidend,  ihm  zur  Kleidung  dienend': ustrake .  .gathäus  »vatthake  "des  Kamels . ., das  mit  seinen  Zottelhaaren  dem  Menschen zur  Kleidung  dient"  Yt.7^11.
*vaBha'  ra-,  zum  V.  iaiah:    —    ai.  vgl.  adki- väsi-  m.  —  NpO. :  mardumän  Uhtar.
•  j.  niaäy5.sästa.-sastö.tBma-  Adj.  'der unter  den  Sastar  der  Menschen  der  ärgste Sästar  ist' :  'm?m  janät , .  'niitn  tba^ayäl Yt  J.  14.
Zu  sästar-,  eine  wertlose  Missbildung.
•  j.  *karapanS  ra%ioyainam  buxtä  mähe" FrW.  2.  3.
•  j.,g.  (,p.)  'mä(y)- V,  'messen'.  Fraes. 27 maya-;  Perf.  i  mim-.  —  PPfP,  'mita-, •mlta-,  maia-,  PFP.  'mi^wa-,
i)  'messen,  bilden,  bauen':  am»sa  spitUa e&ät  milta  aiat  büta  kaca  vaahaot  inana- t^Aaj". .  gebildet  und  hervorgegangen  aus . ." Vr.  77. 12;  —  'mita-.  2)  'ausmessen mit  — ,  vergleichen':  'mthwa-.
mit  ä  Med.  'sich  erproben,  als  tUchtig  I
erweisen,  seine  BeMiigung  ausweisen': amsts  xT  aus  yava^a  . ,  "der  ist  erprobt für  immer  . ."  ¥.7.39;  —  am3ta  F.tf; —  II  ha^a  paruviyalcr  ämätä  amahy  "vor Alteis  haben  wir  uns  als  tUchtig  erwiesen*' Bh.  7. 3  ■',  a)  'seine  Befähigung  erweisen an  — '  (Dat.):  AatSrS*^  paurvS  Smayänte masäayasnaHbyS  vS  daffvayasna^ibyS  väf . .  darvayamaiibyB  paurvS  . .  SmayayatUa (3POM.)  yaäsa  , .  "an  welchen  von  beiden sollen  sie  zunächst  ihre  Befähigung  (zur Chirurgie)  zu  erweisen  suchen,  an  Af.  oder D.7  . .  An  D.  sollen  sie  eher  ihre  Be- fähigung zu  erweisen  suchen  als  . ,"  V. 7. 36£;  —  ungrammatisch:  itsit  staotanqm yesnyanqm  amats  vJsperafavS{%o\[häsae,'a^ "der  nicht  die  Befähigung  erwiesen  hat  fUr den  Vortrag  der  StY.  (und)  der  VR."  Yt
70.  133.
mit  frä  i)  'als  Norm  au&tetlen,  an- ordnen, befehlen';  yät  ySsia  framTma%a (3PPfA.)-'>  ya  Moiya . .  vaxlmtz dafvdsuitä (sd.)  "seitdem  ihr  das  verfügt  habt, dass . ."  Y.  J2. 4",  s)  Med.  'sich  messen, erproben  an  — ':  'framata-.  3)  'ver- bilden, umbilden,  verwandeln  in  — '  (Instr.): yal  barata  aursm  mainySm  framitim aspahe  kshrpa  "dass  er  den  AM.  ritt,  den in  Rossgestalt  verwandelten"  Yt75. 29.
mit  vJ^  'missbilden,  umstalten':  vX- mlta',
ai.  miTnile;  mitik;  np.  patmäyad  'er  misit', »üBiöj'flrf'er  teiel'.  ätiaöj'.irf 'er erptobt';  ows. amain  'erbaoen.  —  PO.  (in  V./,  F.  S):  ezmä- yün,  Hmüli^ai),  (zu  Vr.  //):  mäiatiA  'Mutter- schaft'; s.  noch  No.  4-  —  ')  Nach  Aia>R£AS bei  HüsiNG  KZ.  3S.  255  ist  statt  ämäiä  viel- mehr ädälä  (zu  'ätj/a-)  lu  lesen.  In  Bh.  /.  3 sind  die  drei  ersten,  in  Bh.  a  der  zweite Buchstabe  lerstSrt  —  ')  Statt  iaiäraiiiyi.  — J'  S  3S4\  »■  lOcl'  vai>räai%ä.  —  0  ke  .  .  al frä!  mimht  vartmct,  erl:  tuS  afe  frifil  vai mtniht  api  3  vinSt  iartatt  varleiüt.  —  S)  Vgl, noch  "iiimä.
.  j.  '«a(^)-  f.  'Mass'.  {mam  V.5.60,
61 :  lies  avi.mqm;  —  "mäi,  "mä  F.  6:  sbes.j
KompEX  (s.  n^moiR,  yiAa-m^m).  —  Zum  V.
mäj'):  —  ai.  ma(y)-  f.  —  Pü.;  fiaimä>t(ai).
•  j.  "mal  F.  6.
Angebt.  'Mass',  nach  Pü. :  patmän.  Die  Beleg- stelle vlsp>m  mäi  (Pä-:  karvisp  patmän,  aber NpB.:  tamäm  mäi)  aaiike  ist  aus  visptmäi a^ukt  verderbt;  t.  Ny.  4-  !$■  Yt  10.  5.
•  j.  mä-£im  neg.  Part,  'verstärktes  'ma '/*^',  mit  Imp."':  slaomaca  raxar^a  (sd.)
dby  Google
baranta  .  .  m°  gjrxSni  pärayantu ''  kaia
ahmai  nmanSt  Yty.  157.
ai.  vgL  m&läm  neg.  Put.  —  Vgl.  mAaMm.  — <)  BeguDsligt  durch  den  Imp.  der  voiher- gehenden  positiven  Säue.
•  j.  mäta-  Adj-,  PPfP.:  s.  'otjO")-. KämpE.
•  j.  'mätar-  m.  'der  misst,  Messer':   Vöi
KompE.  —  Ziun  V.  mö(^)..  —  ai,  milar-  m.  ■ —  PQ.:  palmän  'MaKs'.  —  ')  Bei  der  Viel-  i deutigkeit  des  Anigangs  'la  nicht  sicher  be- stimmbar.
•  ].,  g.  (,  p.)  'mätar-  f.  'Mutter*:  yai  pits .  .  'ta  vä  paradrUyäti  hat  a^qm  upa.- manaytn  (sd.)  pukrS  haia  pilarvm  duyta^ haca  Uanm  V.  12. 1 ;  3,  F.  2,  6;  —  pita  tl (näml.  asöis)yS  ahurB  masdh . .  °la  ärmaifi/ brata  .  .  Yt.  77.  16;  —  apaiiä  .  .  'larS (VP.)  /aayff  (sd.)  Y.  JÄ  5;  —  von  Mutter- tieren :  apatca  vä  aztfäl  . .  'Urqlüä  (AP.) ..  agft^a  (sd.)  Y.jtf.5.
KompE.  —  ai.  mätär-  f.,  np,  mädar.  —  Pii, : niälar;  s.  noch  No.  I.  —  •)  Zu  Y.  jS.  5 werden  die  Worte  von  Pii.  als  EN.  genommen und  traniskribirl  1  dabei  zu  mäOrqi  die  Erl.: äf  andar  hamiandUniA  (Sü,:  samiandhi)  i  an narSn  u  mälaiäit  idxmäk  (Samenflüssigkeit); lu  mälare  jSayS  die  Erl.:  lä  (Milch);  vgl.  lu ma^tanl-  *).
•  p.  mä-tya'*  neg.  Konjn.  mit  Konjv.; 1)  hinter  einem  regierenden  Satz  mit  ava- hyarädiy  'dass  nicht,  damit  nicht':  ava- hyarädiy  naiy  nipistam  tn'  hyi^  . .  avahyH paruv  *%aday^  (sd.)  Bh,  4-8;  —  ava- hyarädty{sA.)  käram  aväjamyä''  "tya^mam xsnäsätiy  (sd.)  tyt^ . .  Bh.  i,  13,  2)  ohne regierenden  Satz,  sva,  V/Ä:  /j-a*  manä kartam  varnavatäm  ^uväm  m°  *draujT- yshy  {s^)  Bh.  ^.  6;  —  tuvam  kä  hya* aparam  itnäm  diptm  vainähy  . .  m'  vika- nähy  "du,  wer  es  auch  sei,  der  du  später diese  Inschrift  sehen  wirst  . .,  zerstöre  sie nicht"  Bh.4. 15.
j.  "«DO-gm  Vyt.  JO;  %.  "aita.in'.
•  j.  mä-3a  prohib.  Part,  'und  nicht,  neve', den  oder  die  letzten  von  zwei  oder  mehr gleichgeordneten  Satzteilen  mit  'ma  '/tij' einleitend  und  anschliessend;  i)  mit  Inf.: mä  ns  npB  duMananhe  mä'>  ..m'  nS  ahmt
fi-iüäiü  (sd.)  yS  ..  m'  nS  . .  Y.65.  7;  — mä  apaima  ..  mä  manaaha  mä' ia'^aiina  paitt./ime (sd.)  Vr.22. 3.  i)  mit Ellipse  des  Verbs:  mn  iuyama  ssdreÄricö
mä* . .  m'  (näml.  'soll  es  geschehen")  ya/ «J  uyra.bäxäu!  nivana^  Yt  10, 75.
KompA.   —    Pü.!  mä.    —    i)  So  K7a;  NA.
```


## [2026-09-07T01:39:22.755Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\npages=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(len(pages))\nfor i in range(482,492):\n    t=pages[i]\n    print('=== leaf',i, repr(t[:120]))\nEOF"
}
```


## [2026-09-07T01:39:23.774Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor f in incoming/BQT/BQT_v3_pages.txt incoming/BQT/BQT_v4_pages.txt; do\necho \"##### $f\"\ngrep -n \"مادر\\|مایه\\|ماده\" $f | head -5\ndone"
}
```


### [2026-09-07T01:39:24.078Z] TOOL RESULT

```
903
=== leaf 482 'viate,  prolix. Derivatives:  liquid,  n.,  liquidate  (q.v.),  liquid-ly, adv.,  liquid-ness,  n.\nLiquidambar,  n.,  a '
=== leaf 483 'like.  —  Gk.  XtfloeiSrjp,  ‘like  a stone’,  compounded  of  XtHop,  ‘stone’,  and -oeiSvjp,  ‘like’,  fr.  cISop,  ‘f'
=== leaf 484 '  cp.  delivery.\nDerivative:  liveri-ed,  adj.\nlivery,  adj.,  resembling  liver.  —  Formed  fr.  liver, ‘secreting  or'
=== leaf 485 'ri,  ‘to wrestle,  struggle,  strive,  contend’,  lit.  ‘to  twist, intertwine’,  Lith.  lugnas,  Lett,  lugt,  ‘flexibl'
=== leaf 486 'e’,  which  prob.  stands  for  *grl- bhos  and  is  cogn.  witn  MHG.  krebe,  ‘basket’, ON.  kiarf,  kerfi,  ‘bundle’,'
=== leaf 487 'ongitudinis,  ’length’.  See  prec. word.\nDerivatives :  longitudinal,  n.,  longitudinal-ly,  adv. longshoreman,  n.  —'
=== leaf 488 ' small  parrot  of  New  Guinea  and  Aus¬ tralia.  —  Malay  luri,  ‘a  kind  of  parrot’,  var.  of niiri.\nlose,  intr'
=== leaf 489 ' to  ON.  liggja,  Swed.  ligga, Dan.  ligge,  OE.  began  etc.,  ‘to  lie’.  See  lie,  ‘to recline’.\nDerivatives:  low'
=== leaf 490 'ux,  gen.  lucis,  ‘light’.  See  lucent  and  -ule.\nluculent,  adj.,  clear,  lucid.  —  ME.,  fr.  L.  luculen- tus,  '
=== leaf 491 "  border',  and  with  E. limp,  adj.  and  v.  (qq.v.)  Cp.  limb, ‘edge’.  Cp.  also lunch.\nDerivatives:  lump,  tr.  "
```


### [2026-09-07T01:39:25.202Z] TOOL RESULT

```
##### incoming/BQT/BQT_v3_pages.txt
19:‏بسرمایه کتاپفروشی ابن سینا- تهران‎
111:زبان فارسی * . بسرمایهٌ کتابفروشی زرار - تهران ۱۳۷۳ شمسی .
424:۲ رك: ‎Sys‏ ۱۵ همن ماده . ۸ رك: شمارژ۱ همین ماده - ونیز «شاج»
617:کرانمایه هم‌هت - و نام لحتی باشد ازسیلحن
1933:‎OLE‏ - بروزن مایه ؛ بسسنی میوه باشد
##### incoming/BQT/BQT_v4_pages.txt
20:بسرمایه کتابفروشی اين سینا- تهران
491:عربی واز جالب دیگن ترکی باشد وآترادونخمه ماد - بسکون دال . مغقف مادر است
511:۴ در : مادندر ۳ مادراندر - و نیز « ماد » ( پارسی باستان ۸12412 «پهلوی ۸/82
519:۰ مادر - بفتح سوم ۳ ماد ۳ مار (ه.م.). پهلوی 3212۲ ۰ 1221 از010212. حالت
521:کاها22 ( ماده ) , هندی باستان - 132147 , ارمنی ۳281۳ ۰ کردی 6ا2 ( 220۷ ۵ )
```


## [2026-09-07T01:39:36.264Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\npages=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,p in enumerate(pages):\n    if re.search(r'^mamma,', p, re.M) or re.search(r'^mater,', p, re.M) or re.search(r'^mother,', p, re.M) or re.search(r'^matrix,',p,re.M):\n        print('=== leaf',i,'~p',(i-12)*2)\n        for m in re.finditer(r'^(mamma,|mater,|matrix,|mother,|maternal,|material,|matter,|matrimony,|metropolis,|mammal,).{0,900}', p, re.M):\n            print(m.group(0)[:900]);print('---')\nEOF"
}
```


### [2026-09-07T01:39:37.772Z] TOOL RESULT

```
=== leaf 499 ~p 974
mamma,  n.,  mammary  gland,  milk-secreting  or-
---
=== leaf 508 ~p 992
mater,  n.  1)  mother  ( colloq .);  2)  either  of  the  two membranes  of  the  brain  ( pia  mater  and  dura mater).  — -  L.  mater,  ‘mother’.  See  mother, materfamilias,  n„  the  mother  of  a  family.  —  L. mater  familias,  compounded  of  mater,  ‘mother’, and  familias,  ancient  gen.  of  familia,  ‘family’. See  mater  and  family  and  cp.  paterfamilias, material,  adj.  —  ME.,  fr.  Late  L.  mdterialis,  ‘of matter’,  fr.  L.  materia,  ‘wood,  timber,  stuff, matter’.  See  matter  and  cp.  materiel. Derivatives:  material,  n.,  material-ism,  n.,  ma- terial-ist,  n.,  material-ist-ic,  adj.,  material-ist-ic- al-Iy,  adv.,  material-ity,  n.,  material-ize,  tr.  and intr.  v.,  material-iz-ation,  n.,  material-ly,  adv., material-ness,  n.
---
maternal,  adj.  —  ME.,  fr.  MF.  (=  F.)  maternel, fr.  L,  mdternus,  ‘of  a  mother’,  fr.  mater.  See mother  and  adj.  suff.  -al.
---
=== leaf 509 ~p 994
matrix,  n.,  womb.  —  L.  matrix,  ‘womb,  matrix.
---
=== leaf 540 ~p 1056
mother,  n.,  a  female  parent.  —  ME.  moder,  fr. OE.  modor,  rel.  to  OS.  modar,  ON.  modir,  Dan., Swed.  moder,  OFris.  moder,  ‘mother’,  Du.  moe- der,  OHG.,  MHG.  muoter,  G.  Mutter,  and cogn.  with  OI.  mat  dr- ,  Toch.  A  mdcar,  B  macer. Arm.  mair  (gen.  maur),  Gk.  :j.r,rr,p,  Dor.  pa- TY)p,  ‘mother’,  Alb.  motre,  ‘sister’,  orig.  ‘the elder  sister’,  i.e.  ‘the  sister  replacing  the  mother’, L.  mater,  OIr.  mdthir,  OSlav.  mati,  Lett,  mate, ‘mother’,  Lith.  mote,  OPruss.  muti,  ‘wife’.  All these  words  derive  fr.  I.-E.  *mdter-,  which  is traceable  to  child’s  lip  word  ma-.  Cp.  mater, maternal,  maternity,  matrimony,  matrix,  ma¬ tron,  matter,  metropolis,  Demeter,  metronymic, maieutic,  cummer.
---
```


## [2026-09-07T01:39:46.389Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\npages=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in [486,499,505,508,509,540]:\n    p=pages[i]\n    nums=re.findall(r'\\b(8\\d\\d|9\\d\\d|10\\d\\d|11\\d\\d)\\b', p)\n    print(i, nums[:12], '|', p[:80].replace('\\n',' '))\nEOF"
}
```


### [2026-09-07T01:39:47.709Z] TOOL RESULT

```
486 ['904'] | e’,  which  prob.  stands  for  *grl- bhos  and  is  cogn.  witn  MHG.  krebe,  
499 ['929'] | aught. malleolus,  n.,  one  of  the  two  rounded  projecting bones  on  each  
505 ['940', '941', '1062'] | —  L.  maritalis,  ‘of  mar¬ riage',  fr.  maritus,  ‘a  married  man,  husband’
508 [] | nis, ‘chewing,  mastication’,  fr.  masticatus,  pp.  of masticare.  See  mastic
509 ['948', '949'] | o  measure’.  See  meter,  ‘poetical  rhythm’, and  cp.  words  there  referred 
540 ['1008', '1009'] | odHeb.  mdshdbhah,  a  fem.  noun formed  from  the  masc.  noun  moshdbh.  See
```


## [2026-09-07T01:39:56.740Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\npages=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\np=pages[509]\nfor m in re.finditer(r'^(matrix,|matrimony,|matter,|matron,|maternity,).{0,700}', p, re.M):\n    print(m.group(0)[:700]);print('---')\np=pages[499]\nfor m in re.finditer(r'^(mamma,|mammal,|mammary,).{0,500}', p, re.M):\n    print('[p.929]',m.group(0)[:500]);print('---')\nEOF"
}
```


### [2026-09-07T01:39:58.050Z] TOOL RESULT

```
matrix,  n.,  womb.  —  L.  matrix,  ‘womb,  matrix.
---
matron,  n.,  a  married  woman.  —  ME.  matrone, fr.  MF.  (=  F.)  matrone,  fr.  L.  matrdna,
---
[p.929] mamma,  n.,  mammary  gland,  milk-secreting  or-
---
[p.929] mammary,  adj.,  pertaining  to  the  mammae  or breasts. — Formed  with  adj.  suff.  -ary  fr.  mamma, ‘mammary  gland’.
---
```


## [2026-09-07T01:40:01.103Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\npages=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\np=pages[509]\ni=p.find('matrix,')\nprint(p[max(0,i-1500):i+2500])\nEOF"
}
```


### [2026-09-07T01:40:02.343Z] TOOL RESULT

```
o  measure’.  See  meter,  ‘poetical  rhythm’, and  cp.  words  there  referred  to. matranee,  n.,  a  female  sweeper;  a  female  servant (India).  —  Flind.  mehtardnd,  mehtrani,  fr.  Pers. mihtarani,  ‘female  sweeper’,  fem.  of  mihtar, ‘sweeper’.  See  mehtar.
matrass,  n.,  a  glass  vessel  with  a  long  neck.  —  F. matras,  prob.  fr.  Arab.  mdtarah,  ‘leathern  bottle, skin,  vase’.
matri-,  combining  form  meaning  ‘mother  .  L. main-,  from  the  stem  of  mater,  gen.  mdtris, ‘mother’.  See  mater.
matriarch,  n.,  a  mother  who  rules  her  family  or tribe.  —  Formed  fr.  matri-  on  analogy  of  patri¬ arch  (q.v.)
Derivatives:  matriarch-al,  adj.,  matriarch-ate, n.,  matriarch-ic,  adj.,  matriarch-y,  n.
Matricaria,  n.,  a  genus  of  plants,  the  wild  camo¬ mile  (hot.)  —  ModL.,  fr.  L.  matrix,  ‘womb’  (see matrix) ;  so  called  for  the  reputed  medicinal  val¬ ue.  For  the  ending  see  suff.  -ia. matricidal,  adj.  —  See  next  word  and  adj.  suff.  -al. matricide,  n.,  one  who  kills  his  mother.  L.  ma- tricida,  compounded  of  matri-  and  - clda ,  killer  , fr.  caedere,  ‘to  kill’.  See  -cide,  ‘killer  . matricide,  n.,  the  act  of  killing  one’s  own  mother. —  L.  matricidium,  compounded  of  matri-  and -cidium,  ‘killing-,  fr.  caedere,  ‘to  kill’.  See  -cide, ‘killing’.
matricular,  adj.  - —  Formed  with  adj.  suff.  -ar  fr.
Late  L.  matricula.  See  matriculate, matriculate,  tr.  and  intr.  v.  —  Late  L.  matriculd- tus,  pp.  of  matriculdre,  ‘to  register',  fr.  L. matricula,  ‘register’,  dimin.  of  L.  matrix ,  gen. matricis.  See  matrix,  and  -ule  and  verbal  suff,-ate. Derivatives:  matriculat-ion,  n.,  matriculat-or ,  n., matriculat-ory,  adj.
matrilineal,  adj.,  pertaining  to,  or  descended from,  the  maternal  line.  —  Compounded  of  L. mater,  gen.  matris,  ‘mother’,  and  tinea,  ‘line’. See  mother,  line  and  adj.  suff.  -al.
Derivative:  matrilineal-ly,  adv. matrimonial,  adj.  —  MF.  (=  F.),  fr.  Late  L.  md- trimonidlis,  fr.  L.  matrimonium.  See  next  word and  adj.  suff.  -al.
Derivative:  matrimonial-ly,  adv. matrimony,  n.,  1)  wedlock;  2)  a  card  game. ME.  matrimoine,  matrimony,  fr.  OF.  matre- moine,  matrimoine,  ft.  L.  matrimonium,  mar¬ riage,  matrimony’,  formed  fr.  mater,  gen.  mdtris, ‘mother’,  with  suff.  - mdnium .  See  mother  and -mony.
matrix,  n.,  womb.  —  L.  matrix,  ‘womb,  matrix.
948
source,  origin’,  formed  fr.  mater,  gen.  mdtris, ‘mother',  on  analogy  of  nutrix,  ‘wet-nurse, nurse'.  See  mother.  For  the  sense  development of  L.  matrix  (fr.  mater,  ‘mother’)  cp.  Gk.  p.r)tpa, ‘uterus,  womb’,  which  derives  fr.  moth-
er’,  and  OHG.  muodar,  ‘belly’  (whence  G. Mieder,  ‘bodice’),  which  is  rel.  to  OHG.  muoter, ‘mother’  (cp.  metralgia).
matron,  n.,  a  married  woman.  —  ME.  matrone, fr.  MF.  (=  F.)  matrone,  fr.  L.  matrdna,
‘a  married  woman,  wife,  matron’,  fr.  mater, ‘mother’ ;  see  mother.  For  the  formation  of  the word  cp.  L.  patronus,  ‘protector,  patron’,  fr. pater,  ‘father’  (see  patron)  and  Belldna,  ‘the goddess  of  war’,  fr.  bellum,  ‘war’  (see  Bellona). Derivatives:  matron-age,  n.,  matronal  (q.v.), matron-hood,  n.,  matron-ize,
```


## [2026-09-07T01:40:08.115Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\npages=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\np=pages[509]\ni=p.find('matter,')\nprint(p[i-200:i+1400])\nprint(\"=========== mamma leaf499\")\nq=pages[499]\nj=q.find('mamma,')\nprint(q[j-300:j+1600])\nEOF"
}
```


### [2026-09-07T01:40:09.405Z] TOOL RESULT

```
ter  im  Arabischen,  p.  137.  Aram. tlmar  is  rel.  to  Heb.  taman,  ‘he  hid,  concealed’ (whence  matmon,  ‘treasure’,  lit.  ‘something  hid¬ den’),  Akkad,  tamaru,  ‘to  cover  with  earth’, matter,  n.  • —  ME.  matere,  fr.  OF.  matere  (F.  ma- tiere),  fr.  L.  materia,  ‘wood,  timber,  stuff,  mat¬ ter’,  formed  fr.  L.  mater,  ‘mother’,  as  transla¬ tion  of  Gk.  uXt),  ‘wood,  forest,  timber,  stuff, matter’.  See  mother  and  cp.  Madeira,  madrier. L.  materia  is  not  cogn.  with  Arm.  mair,  ‘pine, cedar’,  mairi,  ‘forest’.
Derivative:  matter,  intr.  v. matter  of  fact.  —  Loan  translation  of  L.  resfacti. Cp.  G.  Tatsache,  which  is  the  loan  translation of  E.  matter  of  fact.
Derivative:  matter-of-fact,  adj.
Matthew,  masc.  PN.  —  F.  Mathieu,  fr.  Late  L. Matthaeus,  fr.  Gk.  MxTOafoc,  fr.  Maxffia;, contraction  of  MxxTaffla;,  fr.  Heb.  Mattiyyah, shortened  form  of  Mattithyah,  Mattithyahu,  lit. ‘gift  of  the  Lord’.  For  the  first  element  cp.  Heb. mattdth,  ‘gift’,  and  see  Nathan,  for  the  second see  Elijah  and  cp.  words  there  referred  to.  The form  Max-Halo?  is  due  to  change  of  suff.  Cp. Matthias.  Cp.  also  matico.
Matthias,  n.  - —  Late  L.,  fr.  Gk.  MaxlIia?,  fr.
Heb.  Mattiyyah.  See  Matthew, mattock,  n.  —  ME.  mattok,  fr.  OE.  mattuc,  fr. VL.  * matteuca ,  which  is  rel.  to  L.  mateola, ‘mallet’.  See  mace,  ‘a  staff’,  and  cp.  words  there referred  to.
949
Derivative:  mattock,  tr.  v. mattoid,  n.,  a  person  of  abnormal  mind  verging on  insanity.  
=========== mamma leaf499
 possessed’,  which  is  rel.  to  Ethiop.  ma- laka,  ‘he  possessed’,  Arab,  malik,  Heb.  melekh, Aram,  melekh,  malkd ,  Akkad,  maliku,  malku , ‘king’.  Cp.  malik,  the  first  element  in  Melchior, Melchizedek,  and  the  second  element  in  Alche- milla.
mamilla,  n.  —  See  mammilla, mamma,  also  mama,  n.,  mother.  —  Formed  with reduplication  from  infants'  babbling  *ma-, whence  also  Gk.  pippa  (voc.),  utxp.pT;,  ‘moth¬ er,  grandmother;  mother’s  breast’,  pappla, ‘mother’,  L.  mamma,  ‘mother,  midwife,  grand¬ mother;  mother’s  breast,  nipple’,  ModPers. mam,  mama,  ‘mother’,  Alb.  meme,  Gheg  mame, ‘mother’,  Russ,  mama,  Lith.  mama,  moma,  Lett. mama,  ‘mother’,  OHG.  muoma,  MHG.  muome, G.  Muhme,  ‘mother's  sister’,  F.  maman,  Sp. mama,  Ir.,  W.,  Co.,  Bret,  mam,  ‘mother’,  OIr. muimme,  ‘foster-mother’.  In  its  unreduplicated form,  infants'  babbling  *ma-  (whence  OI.  ma, ‘mother’.  Dor.  Gk.  pa  (voc.),  ‘mother’)  serves as  a  basis  to  OI.  matar.  Dor.  paTTjp,  Gk.  pTj-rrjp, L.  mater,  etc.  ‘mother’.  See  mother  and  cp. words  there  referred  to.
mamma,  n.,  mammary  gland,  milk-secreting  or-
mammal
manu
gan  of  mammals  (normally  only  in  females).
L.  mamma,  ‘breast’,  identical  with  mamma, ‘mother’.  See  prec.  word, mammal,  n.  —  See  Mammalia.
Mammalia,  n.  pi.  - —  ModL.,  coined  by  Linnaeus in  1758  fr.  Late  L.  mammalia ,  neut.  pi.  of  mam- malis ,  ‘pertaining  to  the  breast’,  fr.  L.  mamma, ‘breast’.  See  mamma,  ‘mammary  gland’,  and adj.  suff.  -al.
Derivatives:  mammal-ian,  adj.  and  n.,  mammal- ity,  n.
mammaliferous,  adj.,  containing  mammalian  re¬ mains  ( geol .)  —  Compounded  of  mammal  and -ferous.
mammalogy,  n.,  the  study  of  mammals.  Com¬ pounded  of  ModL.  Mammalia  and  Gk.  -Xoyta, fr.  -X6yo?,  ‘one  who  speaks  (in  a  certa
```


## [2026-09-07T01:40:27.474Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"== BQT v4 context lines 480-530 with pdf page tags\"\nawk 'NR>=470 && NR<=535' incoming/BQT/BQT_v4_pages.txt | grep -n \"pdf page\" \necho \"---- show 505-525\"\nsed -n '505,525p' incoming/BQT/BQT_v4_pages.txt\necho \"==== grep pdf page tags near\"\ngrep -n \"pdf page\" incoming/BQT/BQT_v4_pages.txt | sed -n '1,20p'"
}
```


## [2026-09-07T01:40:28.091Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"== SNS matar\"\ngrep -n -i \"m[āa]tar\\|mādar\\|mother\" SNS.txt SNS_pages.txt | head -20"
}
```


### [2026-09-07T01:40:28.779Z] TOOL RESULT

```
== BQT v4 context lines 480-530 with pdf page tags
8:[pdf page 16]
59:[pdf page 17]
---- show 505-525
۷ - يك روز صد فیلهٌ تازی وماخچی با ساز ز رکه داد بمردان کارزار؟

مختاری غزئوی « رشیدی >.

۸ معرب آن نیز « ماخور » « تفس > . ‎٩‏ - رد : مالیخولیا .

۴ در : مادندر ۳ مادراندر - و نیز « ماد » ( پارسی باستان ۸12412 «پهلوی ۸/82
(شهرستانهای ایران بند ۲۷) نام قومی است‌آربایی ایرانی نژاد که در ابتدای قرن هفتم یا آخر
قرن هشتم ق.م. دولت ماد را تأسیس کردند » نختین پادشاه این قوم دیوکی 5ع6اها] (۷۰۸-
۵ قمم. ) و آخرین پادشاه آستیاکی - ایخ توویگو است ( 6۵۶-۵۸۶ قم ) این سلله
پدست کوروش هغامنشی منقرض شد ( ایران باستان ج۱ ص ۱۹۸ بیعد ). - و سکن این قوم

بقیه درحاشيةٌ صفحة۱۹۳۶

۰ مادر - بفتح سوم ۳ ماد ۳ مار (ه.م.). پهلوی 3212۲ ۰ 1221 از010212. حالت
فاعلی از - 32218۲ « بارتولمه ۱۱۹۷ ۲ « تیب رکه اس ۸-۱۶۷ > ۰ اوستا - 122487 » آرهنی ع
کاها22 ( ماده ) , هندی باستان - 132147 , ارمنی ۳281۳ ۰ کردی 6ا2 ( 220۷ ۵ )
(مادر ) » 12246 (کاومیش‌ماده)» افغانی 3307 ۰ استی 2206 , 5224 ۰ 3230 :180
بلوچی 21 ۰ ظ2221 ۰ 28 (مادر) ۰ ع 23428 ۰ ق8452 (مژت) . خغنی 1384
منجی 322 « اسشق ۹۵۹ »کیلکی 12247 ؛ زی که يك با چند بچه زاییده . والده . ام.

==== grep pdf page tags near
1:[pdf page 1]
2:[pdf page 2]
23:[pdf page 3]
36:[pdf page 4]
61:[pdf page 5]
95:[pdf page 6]
140:[pdf page 7]
174:[pdf page 8]
208:[pdf page 9]
252:[pdf page 10]
294:[pdf page 11]
312:[pdf page 12]
350:[pdf page 13]
400:[pdf page 14]
426:[pdf page 15]
477:[pdf page 16]
528:[pdf page 17]
565:[pdf page 18]
614:[pdf page 19]
659:[pdf page 20]
```


### [2026-09-07T01:40:28.869Z] TOOL RESULT

```
== SNS matar
SNS.txt:4544:m J d:^ii UiM>. 1167)matar: MP*** matar: ^ **l 
SNS_pages.txt:2888:  m d:^ii UiM>. 1167)matar: MP***                                             ^
SNS_pages.txt:2889:                                                            matar:                        **l
```


## [2026-09-07T01:40:46.208Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nd=open('incoming/BQT/BQT_v4_pages.txt',encoding='utf-8',errors='replace').read()\nparts=re.split(r'\\[pdf page (\\d+)\\]', d)\npg={}\nfor i in range(1,len(parts),2):\n    pg[int(parts[i])]=parts[i+1]\nfor n in (14,15,27,45):\n    t=pg.get(n,'')\n    print('########## pdf',n,'=> printed ~',n+1919)\n    print(t[:1800])\nEOF"
}
```


### [2026-09-07T01:40:47.480Z] TOOL RESULT

```
########## pdf 14 => printed ~ 1933

گقتار یست وچهارم
از کناب بردان قاطع درحرف میم با حروف تجی مبتنی
بر بیست و هشت بیان و محتوی بر يك هزار و یست
لت و کنابت
بیان اول
در هیم یا الف معتمل بر دوست ۲۷و چهارده لغت و کنامت
* ماپروین ۱ « بابای فارسی,مخنف | ماء پروین است وآن بیخی باشد که دفع سموم
(۷) خم ۱: دوصد .
5 م (میم) - حرف بیست وهشتم از القبای فارسی و حرف بیست وچهارم ازالفبای عربی
( آبتث ) و سیزدهم از حروف ابجد , و در حاب جمل آنرا چهل گیرند . این حرف‌کاء به‌«ن»
بپدل شود . - م ( مفتوح ) 132 چون برسر فعل امر درآید : نهی سازد : مکوه مخور ء هزلیده
ولیز برسرفعل دعائی‌درآ ید : هباد » مبادا. رك: مه - لیزهم» ضمیراول‌شخص مفرذباشد(رك : دیباچه
موّلف س‌بط - که » کو ) » درپهلوی 3 ( ضمیر اول شخص مفرد ) « اولوالا 2۹۳ >.
۹ - رل : ماء پروین . : _
ما - پهلوی 27020 (ما) » پارسی باستان 2۳3220 ؛ اوستا ۳98 212822اوراق
تورفان نیب رکه ص ۷ ۰ پازند 42 . هندی باستان - 8877462 ‎٩‏ اسشق ۹۵۵
آستی 3322« که . است ۰۱۲۹ » در لهج بهودیان ایرانی 2892 ۰ کردی 6 ۰ 338 ۰ 126
« ابا س 4*۹ > شهمیرزادی وکیلکی 3832 » دزفولی 0۳200 ۰ خواناری 132102 « سالنامة
کلپایگان 2۷ > . ر4 : دارمستتر . تتیعات چ۱ ی ۱۱۱ ۰ شیر اول شخص‌جمم
( متکلم مع‌الغیر ) وآن ضمیر منفصل است ,گاء در حالت فاعلی باشد :
ما نگوییم بدو میل بناحق تکنیم جامةٌ کس سیه و دلق خوذ ازرق نکنیم.
« حافظ شیرازی س ۲۹۱ ۰
- وگاه در حالت مفعولی : ما راگفت - وگاه درحالت اضافی :
چو بنیاد ایجاد ها برفناست بم رک کسی شادمانی خطاست.
سمدی غیرازی . رك : دستور قیفهی ج ٩ص‏ 42۸۸

########## pdf 15 => printed ~ 1934

مایون ۱۹۳۲۳
و زهر عقرب و مارکند و آنرا بعربی جدوار ‎٩‏ ماج - بسکون جیم . بمعنی ماه باشد
خوانند . چه درفارسی جیم وها بهم تبدیل مییابد وعربان

مابون ؟ - با بای ابجد بروزن‌سایون, | قمرخوانند ‎٩‏ - و بمعنی راوی و روایت کننده
نام علتی است - و حیز و مخنت و پشت پاییرا | هم هست ۷ - و نام راوی رودکی (۲) شاعرلیز
هم میگورند و در عربی لیز همین معنی‌دارد چه بوده است ۸ .
مفمول ۴ ابنه است, وابنه علتی باشد در موضع ماچ ‎٩‏ - بسکون جیم فارسی » بعمنی
مخصوص . بوسه است که بعربی قبله کوبند ‏

ماقر نگ ؟ « بکر تا ورای قرشغت ماچوچه - با هر دو جیم فارسی بر
و سکون نون و کاف فارسی , چلپاسه را کوبند | وزن ماسوچه (۳) . ظرفی باشد لوله دار که با
و بعضی کوبند سام ابرص اشت که نوعی ازچلیاسه آن (4) شربت و دارو در کلوی اطفال ريزند.
باشد . چون شکم او را بشکافند و بر کزندکی ماچ وموچ *0(۱) ۰ با میم بروزن
عقرب نپند در ساعت درد ساکن شود . قاچ و قوچ ‎)٩(‏ ۰ بممنی بوس و لوی باشد بعنی

ماتور نگ * - با قوقانی بواو رسدء | بوسیدن ولیسیدن چنانکه کربه کند بچه خودرا.
و رای بی نقطةٌ مفتوح بنون وکاف فارسی زده » ماخ - پسکون خای نقطه‌دار ».زر قلب
بمعنی‌سوسمار است وآن جاتوری باشد که شافعی فاسره راکوبند -ومردم سفله ودون همت وکمینه
مذهبان خورند و عربان ضب خوانند . بموش | و خسیس و منافق را نیز کفته‌اند - وبمعنی‌مردم
خرما شاهتی دارد لیکن ازوبزرکه‌تر است . پیه پیر و حقیر هم آمده است ند
اورا (۱) زنان بجهت فربه شدن خورند - ماخادیپون - با ثاك بالف کشدء

() چش :آنرا". () چك : رودگی . () چش : ماسوجه .

() چك : بان . (ه) چك : ماج وموج ؛ چش : ماچ و موج .

() چك : قاج وقوج ؛ چش : فاج وقوح -

۱ رك : جدوار . ۴ - (عر) ابنه بشیه ابنا . متهم کرد او را بچیزی ؛ مابون
متهم » و صاحب قاموی گفته که لفظ مأبون در خین وشر هن دو متعمل میشود ... لیکن اکر
آنرا مطلق استعمال کنند مراد ازآن متهم بشر باشد فقط .> «منتهی آلارب» در فارسی تصرفی در
معنی آن کرده‌اند . ۴ - مراد اسم مفعول است . ۴ -قس : مانورنگه .

8 -قی : مانرنگه ۹ -لفتی در «ماء» (غ.م.) ( رك : فهرس
########## pdf 27 => printed ~ 1946

ماش‌هندی ۱۹۸4
وآن افزاری است زرگران‌مگران وآهنگران | وکر نون و تحتانی بواوکشیده و بنون زده .
راء وعربان کلبتان خوانند - وآهنیرا نیز کوبند | بلفت بونانی نام درختی است که بارزد سم آن
که فتبلةٌ تفنگه را در آن محکم‌کنند و آنش | درخت است وآن صمخ را بعربی قنه کویند.
پرنفنکه زنند - و يك حصه ازدوازده حص‌تولچه ماع -بر وزن زاغ » نوعی از مرغابی
را نی زکوبند و تولچه دو مثفال ونیم است ۱ - | اس وآن سیاه میباشد
دمرچیز را یز کویند که بقدر مان باشد. و بعربی مایکون (۱) ۵
ماش هندی - غلهایست عودی رنگه 1 ی تن
8 و بترکی نننلداق ‏ ون
پاندام کندم کوجچکی و. آترا بسربی حب الفلت | میکوبند؟ و ازکوشت اک و پر هش
خوانند بکس قاق . او بوی لجن میآیید -
ماشیا > بروزن باقیا. حشیش ارتغامونی۲ و بمعنی میخ ولزم هم ماغ
است وآن رستنیی باشد مانند خشخاش وپشیرازی | گفته‌اند ‎٩‏ وآن‌بخاری باشد بیارتیره و ملاصق
مامیای سرخ کویندش . بروی زمین وآنرا بمربی زباب خوانند - وئوعی
ماشیوه - با تتابی مجهول وفتح واو ا زکبوتر هم هست که هردو بال وکردن و سینةٌ
بر وزن نادیده ۰ بممنی ماشوء باشد که پرویزن | اوسرخ‌میباشد وسپزهم میشود و اسیزآ تراسپزماغع
وترشی پالا باشد . و سرخ آنرا سرخ ماغ میگوبند .
ماص ۲ < بسکون صاد بی‌لقطه »بمعنی ماقه - بر وزن شافه » چوبی را کویند
ماه است که بعربی قمن میگوبند , لیکن معلوم | که در پس در خانه نهند تا درکشوده انگردد.
نیت که پلفت کجا است . ماقوت - بروزن باقوت . نام نوعی از
ماطو نیون - با طای حطی‌بواورسیده | حلوا (7) باشد وآیرا هاقوآی هم میکویند۹ -
() چك » چش : مالیکون - () چش : نام حلوائی .
۱- يك حصه از دوازده حصة تولةٌ هندی (دو متقال ونیم) . درین معنی هندی است
که در طب فارسی داخل شده « فرهنگه نظام > . رك : ماهه . ۴ - رك4 : ارغاموتی .
۴ - بدانکه ماس پمعنی‌قمرسنسکرت است«چك ۹۸۳ ح» . صحیح «مای» (مانسکربت
5) « وبلیامز ۶ ۳:۸۱ > است . ۴ - هندی باستان - 22081 ( نوعی پرنده آبی )
( عوبشمان 210۸460 . ۰۳۸ ۳) اسشق ۹۹۱ *. «ماغ ‏ هرغی باشد سیاه فام و بیشتن
درآب نعیند . دقیقی (طوسی) کوید :
ای خرو مبارك باراکجا بود جای
########## pdf 45 => printed ~ 1964

ماهیانه ۱۹۹۲۳
ماهیانه ۱ < بر وزن رازبانه ۰ آنچه خوانند .
ماه در ماه دروجه مواجب و مقرری یکی دهند ماهی زرد. ۷ ازماهی باه
در ماه دروجه مواجب و مقرری + ی هی‌ددین " - نوعی ازماهی باشد
همچوسالیاله که سال در سال میدهند - و بمعلی | که درمیان ربکه پید! شود و چنان ساحب‌قوت
ماهیابه هم‌آمده است وآن نان خورشی باشد که | باشد که درمیان ریگ دمکز و پاتزده کر بدود
از ماهی سازند ۴ . و آن در نواحی بغداد و ملك سند بهم میرسد
ماهیچه - بر وزن بازیچه » آنچه از | وآترا بموض سقنقور بکاربرند ۸ ۰ ویستی کوبند
خمیر به پاریکی ریسمان مالند وپزند ۴ و آ شش ۲ ماهی زرین همان سقنقور است .
ماهیجه مشهور است . ۰
جه مشهور ماهی زهره - پوست بیخ کیاهی
ماهی‌دان * بر وزن جاویدان » | است بفایت میاه ماد جگر ماهی وآئرا بعریی
حوض (۱) راکوبند ۴ . سمالمك وشیکران الحوت خوانند . اکرقدری
ماهی‌ دانه 8 - بروزن‌جاوبدانه, بیمنی| از آن‌درآب ریزند ماهیانی که درآب باشند مت
ماهودانه است که حب‌الملوك باشد و آن میوهة شوند وتمام بررویآبآ ند » ومعرب‌آن ماهی-
درخت شباب است . زهرج باشد ‎٩‏ -
ماهیر بیان" (۷) - بنتم‌رای قرعت ماهی سپهر - بکسرسین وبای‌فارسی,
وسکون بای ابجد و تحتانی بالف کشیده و بنون | آشاره ببرج حوت است وآن برجی باشد ازیروج
زده,ملخ دربابیر 1 کویند که بز بان عرپی‌جرادالبحی | دوازده کانهٌ فلکی .
(۵2 خم۳:۱+ آب ۰ () چش : رببان . (۱)
۱- از : ماه ( شهرعریی ) ی ( واسطه )۳ انه ( پسوند بت ) » قسی : ماخوار ,
۲ - باین هعنی ظ . مصحف « ماهیابه » است .
۴ - بغال نان که با در سفره شد بی‌خورد و پی خوایم
بزلف رشته کز این چرخ چون ماهیچه در تام .
بمحاق اطضه « فرهنگ نظام > - واکنون بمعنی قطعهٌ گوشت دارای عصب و رباط که بعربی‌عضله
کوبند استممال شود . « فرهنگه نظام > و فرهنگستان « مایچه » را بمعنی عضله تجویز کرده
است « واژه های نو . ۱۳۱۹ ض ۷۹ و۰۱۱۷
۴ - همیدون کوثر ادر ژرق ماهی دان تو بودی
بخلوت هر شبی حور دکن مهمان تو بودی.
و رك : جهانگیری . « فرخی سیتالی ص ۸۲۹ ۰
۵ *ماخودانه (ه.م.) * ماهوب دانه . ۹ -از: ماهی(صورت‌اضافه) + رییان
و رییان مخقف « آربی
```


## [2026-09-07T01:40:59.535Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nd=open('incoming/BQT/BQT_v4_pages.txt',encoding='utf-8',errors='replace').read()\nparts=re.split(r'\\[pdf page (\\d+)\\]', d)\npg={}\nfor i in range(1,len(parts),2):\n    pg[int(parts[i])]=parts[i+1]\nimport sys\nfor n in sorted(pg):\n    t=pg[n]\n    for w in ['ماده','مایه','مامان','ممه','ماما ','ماکیان','مادیان','مادگان']:\n        if w in t and n<80:\n            print(n, n+1919, w, '|', [l.strip()[:70] for l in t.split('\\n') if w in l][:2])\nEOF"
}
```


### [2026-09-07T01:41:00.771Z] TOOL RESULT

```
2 1921 مایه | ['بسرمایه کتابفروشی اين سینا- تهران']
16 1935 ماده | ['کاها22 ( ماده ) , هندی باستان - 132147 , ارمنی ۳281۳ ۰ کردی 6ا2 ( 220۷', '(مادر ) » 12246 (کاومیش\u200cماده)» افغانی 3307 ۰ استی 2206 , 5224 ۰ 3230 :']
17 1936 ماده | ['0 ماده - بفتح دال (درلیجةٌ مرکزی بکر آن) » پهلوی 312121 ( موّنت) «اوتو', '۱ کردی 332461 (کاومیش ماده ) + کردی ع 33206 ( مت ) « ژابا ی ۰۲۸۵']
18 1937 ماده | ['غلط است . در فرهنکه اسدی نخجوانی (حاشیه) مبنوبد : «ماراء ماده بختی بود', 'دیگرصفت ماده برای آن معنی\u200cندارد \u200f آنوقت صاحب برهان « مارا > را « ماراب']
22 1941 ماده | ['ماده - بر وزن چاره » بممنی حاب | که از چوب بردیوار وغیرآن اقتد ۷ - ومخ']
24 1943 مایه | ['مازه درد ۷ - درد پشت راکویند . | دیگر مایه ای که بر شپرزند ماست گویند ']
29 1948 ماده | ['۹ «مادیان (ه.م.) ( لغة ) * ماده (۸.م.) .۶ فاب ۱ص ۲۲۹ >']
29 1948 ماکیان | ['ماکیان : ۹ ۱۹۶۹۳', 'ماکیان بردد کردن - کنایه از | وآرا از هفت مغز سازند که مقز بادام و مغز']
29 1948 مادیان | ['ماگیان ۱ - بر وزن مادیان . مزغ | لام حلوائی است که ازبرنج پزند وآن درک', '۹ «مادیان (ه.م.) ( لغة ) * ماده (۸.م.) .۶ فاب ۱ص ۲۲۹ >']
31 1950 ماما  | ['۱ - بونانی 33612818712 \u200e٩\u200f اشتینگای > . ؟ -قی : ماما ۰ مامی » لیتوانی', '8 30۵ (مادر) . املاوی کلیسیابی 38778 ( ماما ) » آلبانی 136116 » وخی']
44 1963 ماکیان | ['ازماهی اشنه سازند وآنرا بعربی صحنات کویند. ماهیان - بر وزن ماکیان » جم']
47 1966 ماده | ['مایون ؟ بروزن قارون » ماده کاوی | وضخامتی باشد - وبزبان گیلان جماعتی ر', '- و ماد عرحیوانر گوبند عموماً و ماده شتر را مایة صدق - یک ماد بی ضله']
47 1966 مایه | ['ماپندر ۱ - بنتح ناله بروزن\u200cآهنگر, مایه دار * - با دال ابجد بر وزن', 'مایه ؟ » بنتح ثالت , بممنی\u200cمقدار باشد مایة شب - کنایه آزسیاهی و تارریک']
68 1987 ماده | ['میباغد چنانکه ربشةٌ آن بمنزلهٌ موی\u200cسراوست , | بخورد فرزند نن و اکن از ', 'نروماده دست\u200cد رگردن هم کرده وپایها دریکدیگر ماده ۸']
69 1988 مایه | ['عربان اسان المین خواتد \u200e٩.\u200f بماند - و شخصیرا نیز کوبند که ست وفرومایه']
70 1989 مایه | ['۲ - بسنده کند زین\u200cجهان مرز خوش بداند مگر مایه و ارز خوش .']
71 1990 ماده | ['آماده و مپیاکرده وکنار های آنرا بلند ساخته | پرده پوش » بمعتی کوش موش ']
73 1992 ماکیان | ['اوستا 339798108 ( پرنده » ماکیان ) « بارتولمه ۱۱۷۲ * « نیب رکه س ۱۵۳ ۰']
```


## [2026-09-07T01:41:15.936Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nd=open('incoming/BQT/BQT_v4_pages.txt',encoding='utf-8',errors='replace').read()\nparts=re.split(r'\\[pdf page (\\d+)\\]', d)\npg={}\nfor i in range(1,len(parts),2):\n    pg[int(parts[i])]=parts[i+1]\nfor n in (17,29,31,47):\n    print('########## pdf',n,'=> Moin printed',n+1919,' Nourai',n+1917)\n    print(pg[n][:2200])\nEOF"
}
```


### [2026-09-07T01:41:17.268Z] TOOL RESULT

```
########## pdf 17 => Moin printed 1936  Nourai 1934

مادر آب وآش -۱۹۳
مادر آب و آتش - بکسر راق ‏ | خوانند . خوردن‌آن قوت باه دهد .
قرشت » کنایه ا زگربه کنندة بسوز است پمنی مادده ؟ - بکر ثاك و فتح رابع,نام
شخص ی که از روی سو زکربه کند . آولایتی است در عغرب زمین -
مادر باع - بکر رای قرشت (۰)۱ ماد‌ندر ۴ » با نون ودال ایجدیروزن
کنایه از زمین است که بعربی ار کوبند ‎٩‏ - | غارتگر , مغفف مادر اندر است که زن پدر
وباغ را هم کفته‌اند بطریق اضافه , باعتبار اشجار | باشد .3۶
و اثمار پمتی درختها و میوه‌ها - ماد - بنکون رای قرشت. معروف‌است
مادردخت جم دال ابجد وسکون | که بزبان عرمی حیه کوبند ۴ - و مخفف مادر
خای نخذ و نای قرشت , تودربر! کوبند و آن | هم هت که والده باشد ‎٩‏ - و مخفف میار هم
تخمی باشد ریزه و آنرا در صفاهان قدومه (۷) هت (۳) که نعی و منع از آوردن باشد ‎٩‏ -
() خم ۱ : رایع « () خم۱: قدامه - ۳) خم۱: میباشد .
‎٩‏ - مادرباغ سترون شد و زادن بگذاشت . الوری آبیوردی «رشیدی» .
۴ - چنین نامی در معجم‌البلدان و نخبةالدهی نیامده , ظ . مصحف « مارد» > ناحیه‌ای
وسیع از نواحی اندلی ازاعمال قرطبه ۶ معجم‌البلدان » است ۳ 816۲108 * فهرست نغبة‌الدهر»
و رك : فهرست دو فجلد حلل‌السندسية . ۴ - مخقف مادراندر (ه.م.) :
جهانا چه بینی تو از بچگان که‌که مادری گاه مادندری .
رودکی سمرقندی « رشیدی > .
۴ - پهلوی 132۴ ۰ قی : سانسکریت - 13278 ۶ نیب رکه ص ۱۸۵ > و رک : باروچا
س۳۱۳. این كلمة سانسکریت بمعنی میراننده وکشنده است» بنابراین باكلمة آوستابی 7221722
بمعنی زبانکار وتباه کننده یکی است » ازمصدر 13387 اوستایی و پارسی باستان بمعنی مردن «فاب
٩می‏ ۱۹۸ ورك : هرمزدنامه ص ۳۸4؛ کردی 128۳ « ژابا صس ۳۸۵ » ؛ جانوری‌ازخز ند کان.
دارای بدنی دراز و قابل المطاف . بدون دست و پا . بیشترآنها مولد زهر‌های کشنده‌اند و تعداد
دندم‌های آنها بسیار است ولی جناغ ندارند . * -کیلکی 334۳ (مادر ) ۰ لری(اطراف
بروجرد ) 1387 «شهیدی» , در اراك ( سلطان آباد ) 3387 « مکی تراد > . رك : هادر .
‎٩‏ - بند الف 2۳ - 138 .
0 ماده - بفتح دال (درلیجةٌ مرکزی بکر آن) » پهلوی 312121 ( موّنت) «اوتوالا
۱ کردی 332461 (کاومیش ماده ) + کردی ع 33206 ( مت ) « ژابا ی ۰۲۸۵
رك : مادر » و رك : دارمتتر . تتبعات اج ۱ص ۱۱۶ ج ۷ص ‎٩۲‏ ؛ عونت » مقابل فر:
عهر بهتر از ماء » ليك بافظ هادهآمد یکی و دیگر نر. « سای غزئوی ص۲۲۰
بقیه از حاشية صفحةٌ ۱۹۴۳۳
( عراق عجم وآذربایجان ) را نیز «ماد» مینامیدند » وهمین‌کلمه است که در پپلوی و پارسی(ونیز
درتعریب) «ماه» شده . ابوربحان بیرونی درکتاب‌الجماهر (ص ۲۰۵ ) نوشته : * ماه عبارتست 
########## pdf 29 => Moin printed 1948  Nourai 1946

ماکیان : ۹ ۱۹۶۹۳
ماگیان ۱ - بر وزن مادیان . مزغ | لام حلوائی است که ازبرنج پزند وآن درکیلان
خانگیر | کویند که مادیتهٌ خروس باشد ۴ . متعارف است , و بعن ی کوبند حلواگی‌است خعك
ماکیان بردد کردن - کنایه از | وآرا از هفت مغز سازند که مقز بادام و مغز
غامت بخل و لپایثت خت باشد . کردکان و زرد آلو و شفتالو و پسته و فندق
ماکیان زاغ دنب - کدابه از وچلفوزه باشد - و خرمای قسب را نیز کوبند -
شب است که بعربی لیل خوانند . وبکاف فارسی پستی تیب ی زکویندکه آلت
۰ ۰ : ی ی امد ۸ .,
مالان ۴ با لام ال و قح نون مالك دینار کاف و دا
وسکونکاف. شفترنگه رأگویند وآن میوه‌است یک اف و دال
شیه بشتتالو . ایجد . نام شخصی بوده از اولیاءال ‎٩‏ .
مالای ۴ « بسکون بای حطی, مشدة مالمکا ۱۰ بامیم وکاف بروزن پابرجاء
میالای است که متع از آلوده کردن باشد بعنی بمعنی اول‌مالکانه است وآن حلوائی باش د که در
آلوده مکن . ۱ کیلان از براج پزند .
مال بخ بخش - بروزن تاج‌پخش ۰ نم مال ناطق - یکی تالك وطای حطیٍ
روز هشتم است از ماههای ملکی - وممنیدبگ | کنابه از سپ واشتن وکاو و امثال آن‌باشد۱۱
خود معلوم است 8 . - وکنایه از زر وسیم سکه‌دار هم هنت ۱۳.
۲ 1 ۹
اس مت
نقطه بلفت پوانی‌پسمنی سیاه است که یض‌سنین | نوی از جاپاسه است که آن راسام برش
باشد . میگوبند .
مالگانه ۷ با کاف بروزن شاخانه , مالول ۴ با واومجهول‌پروزن‌شاقول,
۹ «مادیان (ه.م.) ( لغة ) * ماده (۸.م.) .۶ فاب ۱ص ۲۲۹ >
۴ - تو نزد همه‌کس چو ماکیانی اکنون تن خود را خرو یکردی.
عمارة مروزی « لغت فری صس ۳۷۹ >.
۴ -ظ . مصحف « خالانك > . کیلکی 58416081 ( هلو شفتالو ).
۴ -رك : آلودن . 8 یی بخشندة مال ( آسم فاعل مرخم ) -
‎۹٩‏ - بونانی 326185 (سیاء ) « اشتینگای » . رل : مالیخولیا .
۷ مالک ۵ رشیدی > « مالکانه , هفت مغزبود . حلوایی خشك است. ابوالعپا ی گفت:
کار من خوب کرد بی‌سلتی هرکه او طمع مالکان هکند .>
رك : مالمکا . « لفت فری 4۹۷ .
۸ - بدین معتی « لکانه > است « رشیدی > وبا « سب > در معنی پیشین به « نیب >
تصحیف شده . ‎٩‏ - ابویحیی مالكین دینارصری از راوبان حدیث » مردی پرهیز کار بود
که از کب خوش ارتزاق میکرد و مصاحف می‌نوشت و اجرت می‌ستد . وی در جره‌یال۱۳۱
قمری درگذشت « اعلام زرکلی ج ۳ ص ۸۲۹ - *- رك : مالکانه -
۱ ناطق (عر ) بمعنی حیوان » در مقابل سامت بمعنی زر و سیم استعمال شود : ماله
ناطق ولاصامت » یعنی او را نه حبوانی است نه مالی دیگر « منتهی‌الارب > -
۴- بان معنی«سامت» است به ناطق(که مقابلآست). ر4:ح۱۱. ۰ 9۴ ر4: ماکول.
(برهان قاطع ۳۴۱)

########## pdf 31 => Moin printed 1950  Nourai 1948

مالیطرنا م۱۹۶۸
کوبند بوتانی ات .38 خوانند, وصعترا کرچه باسین بی‌نقطه است لیکن
مالیطر فا ۱ « بفتح طای حطی‌وسکون | درکتب طبی بصاد نوشته‌اند تا بشمین مشتبه‌نشود.
رای قرشت و لون بالف کشیده . و پلفت بونانی | خوردن‌آن درطمام ضمف‌چشم را نافع باشد وقوت
زاج سیاه باشد و آن را زاج کفشگران اس باصره را نگاه دارد -
میگوشد؛ وبحذف مانی‌هم آمده است که ملیطرنا مامهستان « بفتح ثالك ‏ و کسرهایروزن
باشد. + ناوکستان . دوائی است که آنرا ساذج هندی
ها » بروزن لام » مادرراگوبند وبمرپی | کوبند و آن برکی است مانند بر که کردکان
والده و ام خوانند ۲ .28 و در روی آب پیدا میشود . بخورآن بجه را از
مامك * بروزن ناوك . مصفر هام است نگ بزیرآورد(؟) -
که مادر باشد پستی ماد رک - و مادر را هم مامیشا ؟ - با ناك بتتای‌رسید. دای
میگوبند ۴۳ .#* متلئه بالف کشیده , بلفت سربانی نام رستنیی‌باشد
مامون « بروزن (۱) هامون . نوعی‌از بفایت بیمزه ودرآب بهم میرسد ودر قاضات بکار
پودنه کوهی باشد و آلرا بس‌بی صعتر الجمام | برند و عصارة آنرا شیاف مامینا خوانند .
() چك : بوزن . () چش : آرد . ۹
۱ - بونانی 33612818712 ‎٩‏ اشتینگای > . ؟ -قی : ماما ۰ مامی » لیتوانی
8 30۵ (مادر) . املاوی کلیسیابی 38778 ( ماما ) » آلبانی 136116 » وخی
.۰ سربکلی 33282 (مادر بز رکه) . افغانی 12181 (عمه » خاله) ۰ بونانی114772302 ۰
6 ( ماما » مادربز رکه ) . لاتینی 33870382 » 17121212118 ( ماما + مادربز رکه ) ۰
آلمانی عالی قدیم 30002 . 3301 ( عمه . خاله ) «اسشق ۹۹۳ > ۰ پازند 133878(مادر)
* باروچا ۰۳۱۱
شاد الا بدر مر که نه‌یینی مردم بکر جز در رحم مام نیابی دختر.
انوری ابیوردی درقصیدء راجع بحملهٌ غزان . « فرهنگه نظام » -
۴ - از : هام (هم.) + که ( پوند تحبیب و تصفیر ) .
۴ - ممیتا « دزی ج ۲ اس چ۹۱ ۰ 80818106۳ (ف) ۸« دزی جس ۲:۵0
0 مالیدن - بفتح دال » اوستا - 33872 » 1287628111 ( جاروب شده ) » پهلوی
2 ] ۸۵۵ ۰ 2۳2 ] فقاطعهل .۰ متفه ] هط۵5ل , ۵ط22720(9 ( جماع ) ۰
(جناع کردن). 2211088 ۰ 332[)1(808 ؛ هندی باستان- 2:۲2 , [ع12279180
( پاك کردن ) »کردی 2 3.3110 ( جارو ب کردن ) بلوچی 2 و2212 . 22160285
( ساییدن ‏ مالیدن , مخلوط کردن ) » استی 323۳218 ( جاروب کردن ) « اسشق ۹۹۲ 4
دست کشیدن روی چیزی ۰ چبزی را دردست مکرر فغار دادن » دوچیز را بهم فشاردادن » مشت
ومال دادن » چیزی را ( مانند رنگه , روغن ) روی جم ی کشیدن .
2 ماما.- رك : مام ؛ در تهرانی 3387528 (قابله . مام‌ناف) » در افغانی 112132 (دائی,
خال ) در فارسی آدیی بمعتی مادر است :
هت مامات اسب و باپا خر تو مشواتر 
########## pdf 47 => Moin printed 1966  Nourai 1964

ماکده نه ۱۹۹۸۳-
ماه نه - بکر نون وظهورها » | دستگاه و نامان هم هست - و ابنیاد هر چیز را
بممنی ماتده سالار است که سفره چی باشد - یز گوبند ۷ .۸
ماپندر ۱ - بنتح ناله بروزن‌آهنگر, مایه دار * - با دال ابجد بر وزن
بممنی مادر اسر اس ت که زن پدر باشد ‏ لاله زار » هر چیز را کویند که با او کندکی
مایون ؟ بروزن قارون » ماده کاوی | وضخامتی باشد - وبزبان گیلان جماعتی را گویند
بو دکه فریسون را شیر میداد و آورا پرمایون‌هم که در عغب لشکر می ایستند و آلها را بترکی
میگویند . چندوال خوانند .
مایه ؟ » بنتح ثالت , بممنی‌مقدار باشد مایة شب - کنایه آزسیاهی و تارریکی
چنانکه گویند « چه مایه ؟ » بعنی چه مقدار ۴ | شب باشد .
- و ماد عرحیوانر گوبند عموماً و ماده شتر را مایة صدق - یک ماد بی ضله
خصوماً 8 - و بمعنی مایون هم هست که کاوی | وسکون دال وقاف ؛کنایه از آبابکرین‌آبی‌فحاقه
بوده و فربدون را شیر میداد٩‏ - و بممنی | است *۱.
۹ - از : مای ( مادر )ل ندر ** مادندر ** مادراندر: قاطمه را عایشه مایندراست . ناصر
خسرو بلخی « رشیدی > . ۳ - درشاهنامه این صورت نیامده , مصحف « برمایون >»(۸.م.)
است . و رك : رشیدی . ۴ - بپلوی 712212 ( جوهی . ماد اولی ) * تاوادبا ۱۹۳ >
نیز بمعنی ماده ‏ شپیء مادی وبمعتی ماده » مادینه «اونوالا ۵۱۱ و ۵۱۲ . هرن کوبد : من
مستقدم که « مابه » فارسی و 13216۲168 لاتینی ازريشةٌ - 1081 ( فس: 13216۳ ( مادر ) )
مشتق باشند . قس : کبری 1226 ( مادر ) [ رك : مادر ] و ممکن است « ماده > ( با دال
مشدد ) عربی ازین ریشه باشد ؟ * اسشق + رك :ح ۰۷
۴ - چه مایه رنج کشیدم زیار تا این‌کار بآب دیدء و خون چگ کرفت قرار ؟
رضی نیشابوری « رشیدی > « فرهنگه نظام >.
عماده . رك: ۳ ‎٩‏ - درشاهنامه این‌سورت نیامده. مصحف «یرمایه»(ه.م.)
< برمایون است . ۷ - ودماده» , مادت,باسطلاح فیلسوفان: «وهرپذبرایی که بپذیرفته‌ای
هستی وی تمام شود و بفعل شود » آن پذبر! را هیولی خوانند و مادت خوانند . و بپارسی مایه
خوانند » وآن پذبرفته راکه اسر وی بود صورت خوانند .> « دانشنامة علائی . بخش دوم مصحح
تگارسه ی ۰۱۰ ۸- و نیز نام یکی از شش آواز موسیقی ( معرب آن نیز مایه
« دزی ج ۲ص ۵۹۷ 4) :
عراق و كوچك آمد اصل مایه ز اسقاهان ( اصل: اصفهان ) وزنگوله‌است. سلمك.
بنقل" «رشیدی > .
‎٩‏ از : مایه‌ملوار [ دازنده).
۶۰ لغب آپویکر « صدیق > بود .
```


## [2026-09-07T01:41:42.793Z] TOOL CALL #33: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 3
}
```


### [2026-09-07T01:41:42.818Z] TOOL RESULT

```


```


## [2026-09-07T01:41:44.515Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor w in \"مامان\" \"ممه\" \"مایه\" \"ماکیان\" \"مادیان\"; do\necho \"##### $w\"\ngrep -o -m5 \".\\{0,80\\}$w.\\{0,160\\}\" MON_part1.txt MON_part2.txt 2>/dev/null | head -6\ndone"
}
```


### [2026-09-07T01:42:01.277Z] TOOL RESULT

```
##### مامان
##### ممه
##### مایه
##### ماکیان
##### مادیان
```


## [2026-09-07T01:42:05.669Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nls -la MON_part1.txt MON_part2.txt; head -c 600 MON_part2.txt; echo; echo \"=== adena\"\nls -la incoming/MON/ 2>/dev/null; grep -c \"مادر\" incoming/MON/MON_2vol_Adena_v1_djvu.txt 2>/dev/null"
}
```


### [2026-09-07T01:42:05.748Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 4377831 Sep  4 14:06 MON_part1.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 4331421 Sep  4 14:06 MON_part2.txt
معین» محمد» ۱۲۹۱ ۱۳۵۰. 


۰ 
۳ 


فرهنگ معین / محمد معین. -- تهران: آدنا: کتاب راه نو ۰۱۲۸۱ 


۲ج 
(دوره) :964-7252-51-2 :158 
(ج.۲) 964-7252-53-6 :158۷ (ج.۱) 964-7252-52-8 :5۳81] 
فهر ستنویسی بر اساس اطلاعات فیپا. 
۱. فارسی -- واژه‌نامه‌ها. الف. عنوان. 
۴۵ف ۲۹۵۴/۸۷ ۳112 ۳ فا ۴ 
۱۳۸۱ 
کتابخانه ملی ایران ۷۹۵ - ۸۱م 


انتشارات آدنا 
فر هنگ دوجلدی معین 
گردآورنده عزیزالته علیزاده 
�
=== adena
total 48692
drwxrwxr-x  2 sfmqrb sfmqrb     4096 Sep  4 14:06 .
drwxrwxr-x 23 sfmqrb sfmqrb     4096 Sep  4 14:06 ..
-rw-rw-r--  1 sfmqrb sfmqrb 20113727 Sep  4 14:06 MON_2vol_Adena_v1_archive.pdf
-rw-rw-r--  1 sfmqrb sfmqrb  4377831 Sep  4 14:06 MON_2vol_Adena_v1_djvu.txt
-rw-rw-r--  1 sfmqrb sfmqrb 21014767 Sep  4 14:06 MON_2vol_Adena_v2_archive.pdf
-rw-rw-r--  1 sfmqrb sfmqrb  4331421 Sep  4 14:06 MON_2vol_Adena_v2_djvu.txt
84
```


## [2026-09-07T01:42:11.828Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor w in \"مامان\" \"ممه\" \"مایه\" \"مادر\" \"ماده\"; do echo \"### $w\"; grep -c \"$w\" MON_part1.txt MON_part2.txt; done"
}
```


### [2026-09-07T01:42:13.187Z] TOOL RESULT

```
### مامان
MON_part1.txt:4
MON_part2.txt:9
### ممه
MON_part1.txt:10
MON_part2.txt:20
### مایه
MON_part1.txt:113
MON_part2.txt:87
### مادر
MON_part1.txt:84
MON_part2.txt:100
### ماده
MON_part1.txt:276
MON_part2.txt:312
```


## [2026-09-07T01:42:18.055Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### مامان\"; grep -n \"مامان\" MON_part2.txt | head -12\necho \"### ممه\"; grep -n \"ممه\" MON_part2.txt | head -20"
}
```


### [2026-09-07T01:42:18.134Z] TOOL RESULT

```
### مامان
43100:مامان: مق (۱.) (در زبان کودکان) مادر» 
43104:رفبقه‌های خود را مامان خطاب کنند (در این 
43105:صورت غالا مامان جون (جان) گویند.) ب - 
43106:روسپیان خانم رئیس و سردستة خود را مامان 
43109:مامانی: -7227181 [فر. ف.] (ص‌نسد.) چبز 
45461:روز تولد بیغامیر و امامان و مبعت. 
60885:و امامان که از گناه مبرا هستند؛ ج. معصو مین . 
76957:بغمبران؛ امامان و پارسایان. 
80085:برای کسی که تازه مرده با برای امامان شیعه). 
### ممه
2465:هممهمه و فش باد. آواز و بانگ آلات 
43585:و تسممه). طول این 
50259:از صفات ذمممه و مقابل ان اتصاف به 
51513:مداهنه: روحعط)ممهط00۵2 [ع. مداهنه ] 
56809:مسسلحه: (می‌دتناممه (ع. مسلحه | (.) 
64847:کوچکث شاه ممهور شده و مقید بر ثبت در 
65508:ممه: (۱۵۱۸)۵ [تر .] (۱.) (به زبان کودکان) 
65509:پستان. ممه را لولو برد: به هنگام از شیر 
65520:ممهل 
65523:ممه را لولو برد. (مج.) فایده و امر نیک 
65526:ممهد: ۵حططخصهه [ع.] (امف.) بهن کرده 
65530:ممهور. ۲ ااز مهر ] (به صبفا امف. ع. 
65531:ص.) مهر شده. ضح. ممهور اسم مفعول از 
66432:منزه: طمععمممه [ع.] (اسف.) پاک کرده 
66434:منزه: طعسعممهه [ع.] (افا.) باکك کننده. 
66636:امده. (ف.) ضممه شده؛» ببوسته. لو لو 
85931:داشت (مرآت البلدان ج ۱ضممهً ص ۲۹) 
85956:البلدان ج ۱ ضمممهً ص ۲۸). 
88811:هاونان: ممه۰2 ).٩(‏ یکی از هشت متام 
91697:هممهمهه: (ع-)مسعطصهده [ع. همهمه ] (ا.)
```


## [2026-09-07T01:42:24.108Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '43095,43115p' MON_part2.txt\necho \"==========\"\nsed -n '65500,65530p' MON_part2.txt"
}
```


### [2026-09-07T01:42:24.219Z] TOOL RESULT

```
ماماجيم‌جیم: ]۰-۱ (امر .) (عسم.) 
نوعی حلوا از جنس حلوا جوزی که آن را 
بصورت قرص‌های پهن و نازک (به بزرگی 
نان شیرمال و نازکتر از آن) سازند و روی 
آن کنجد با شاهدانه باشند. (فر عا.جما.) 
مامان: مق (۱.) (در زبان کودکان) مادر» 
والده. (ص.) (ف.) هر چیز خوب؛ قشنگك؛ 
دلیسند. شخص خوش جنس و بزرگوار. 
(اصط. فاحشه خانه‌ها). الف - مردان 
رفبقه‌های خود را مامان خطاب کنند (در این 
صورت غالا مامان جون (جان) گویند.) ب - 
روسپیان خانم رئیس و سردستة خود را مامان 
گویند. 

مامانی: -7227181 [فر. ف.] (ص‌نسد.) چبز 
خوب و قشنگ و دوست داشتتی. . شسحص 
خوش جنس و بزرگوار. 

مامایی: 7۱20۱87 (حامص.) ماما بودن» 
قابلگی. 

==========

ممنون: ۱۱۳۹۱۱ [ع.] (امف.) نعمت داده و 
منت نهاده. 

ممو ۵: 010002۷۷۸۱ [ع] (امف.) زراندوده» 
آب زر داده. خوش ظاهر و بد باطن. درو غ 
راست‌نما. 

ممه: (۱۵۱۸)۵ [تر .] (۱.) (به زبان کودکان) 
پستان. ممه را لولو برد: به هنگام از شیر 
گرفتن کودکان؛ نوک بستان مادر را سیاه 
کنند و چیزی تلخ مالند» چون بچه خواهد 


۱۸۲۲ 


فر هنک فارسی معین 


ممهل 


ممه را لولو برد. (مج.) فایده و امر نیک 
متوقع از بین رفت. 

ممهد: ۵حططخصهه [ع.] (امف.) بهن کرده 
شد ۵ تک کنر ده کسم آندق: آماده کر ده؛ 
مهیا (به دو معنی). 

ممهور. ۲ ااز مهر ] (به صبفا امف. ع.
```


## [2026-09-07T01:42:39.853Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nd=open('SNS_pages.txt',encoding='utf-8',errors='replace').read()\npages=d.split('\\f')\nprint('leaves',len(pages))\nfor i,p in enumerate(pages):\n    if '1167)matar' in p or 'matar:' in p:\n        print('=== leaf',i)\n        print(p[:1500])\nEOF"
}
```


### [2026-09-07T01:42:41.407Z] TOOL RESULT

```
leaves 243
=== leaf 42
  ar                               Ll. c^-,Li uL*}\
                                                        }
                                                                                                                                                                  ,Uj^b*.L.;i                                 OT

Haurvatat       S Ameretat by       y- ,J                         .bS        *JLI*..
                                                                        ir
tlirji P.     y/adia. Bombay. 1888.
 amardat      :^    {AiWb 143-4) amaratStSt,-amaratat:-i
   i/TT ^.Y/TV^.T1-T6-6-r/)0^               1   t />T   ^   •
                                                                A/1 ^ -f J,* ^./
     -_t+ j'jj.1) .ojljj.ljj^l      l>i jUj«I
                                                                                                                                                                     1/6 <S ./->>>*-;       BaBxt&rls V
                                                :araurd3d-it                  f*- "

                                                                                                                                               (o-ib-iW                  I***) o^>» T ramoxtan:              mcyix
                                                                                                     ilWii*.                ^rawxtn            :    >;L           (wir.        Wan.   1,40) hmwxth: J**              A
                       rA.
```


## [2026-09-07T01:42:48.007Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '4535,4555p' SNS.txt\necho \"======\"\npython3 - <<'EOF'\nd=open('SNS_pages.txt',encoding='utf-8',errors='replace').read()\npages=d.split('\\f')\nfor i,p in enumerate(pages):\n    if '1167)' in p or '1167 )' in p:\n        print('leaf',i)\n        j=p.find('1167')\n        print(p[max(0,j-600):j+600])\nEOF"
}
```


### [2026-09-07T01:42:49.247Z] TOOL RESULT

```
.*A^i£ r A. l >i«. li-lj a A :haradadist3n: \vw"H*» fr 
•j'jo. 1 (>j j M/ .>i) d5dist3n + ^ ),.„„,[ 

■r/n«* ir/A^ m-wr-vr/r^ (t, 



•j>>U:madar, "'My-tl : >» ^w* 
m J d:^ii UiM>. 1167)matar: MP*** matar: ^ **l 
(*i*. *ta».IH,57)m»dr, m'd: jL Wrm wan.H, 3 9) 
u-n/ivJ u-ir/w^ )«v^ Y J >>v; m at , V 

n-n/iv^ .o'jJUimadarSn, 3 My, tl 5 n: ^\.M 






A"W»M 
======
leaf 42
                                                                                                                                             Uanfcer.               160      hFhoj-. o T uv'jj*
                         r/n«* ir/A^ m-wr-vr/r^                                    (t,
                                                                                                                      <c*-l*i»^T :3ra0xt                    SstSd         :   csU^ " 1^*lfe : amoxted:   \wifcMX

                                  •j>>U:madar, "'My-tl                   :    >»     ^w*
    J
  m d:^ii UiM>. 1167)matar: MP***                                             ^
                                                            matar:                        **l
(*i*.    *ta».IH,57)m»dr, m'd: jL Wrm                                                                        >;£.( araoz            jl   j> y.uki fr ^U. J*») .o^T am6zed: v**^^ W
                                                                                                                                                                     -                      :

                                      wan.H, 3 9)
```


## [2026-09-07T01:42:58.181Z] TOOL CALL #41: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/méh₂tēr",
 "prompt": "Give the full reconstruction, gloss, root/derivation analysis (is it from *méh₂- 'mother' nursery word plus the kinship suffix *-ter-?), and the list of descendants especially Proto-Iranian/Avestan, Latin, Germanic, Greek. Quote key wording."
}
```


## [2026-09-07T01:43:00.041Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%85%D8%A7%D8%AF%D8%B1",
 "prompt": "Give the Persian etymology of مادر: Middle Persian form, Old/Proto-Iranian, PIE, and any cited sources (Hasandust, MacKenzie, Cheung). Also any Persian entries for مادر meaning mother."
}
```


### [2026-09-07T01:43:04.417Z] TOOL RESULT

```
# Proto-Indo-European *méh₂tēr ("Mother")

## Full Reconstruction
**\*méh₂tēr** (feminine; oblique stem **\*méh₂tr-**)

## Gloss & Meaning
"Mother"

## Root/Derivation Analysis
The etymology involves debate among linguists. Donald Ringe suggests it "may be a nursery word or Lallwort," proposing **\*mah₂tḗr** as most likely. Traditionally, scholars viewed it as "a combination of a nursery word \*ma ('mother') and the agentive nominal suffix \*-tḗr." However, evidence suggests "a genuine verbal root 'to nurse, to mother'" may exist instead, with the root being **\*méh₂-** containing a laryngeal.

## Key Descendants

**Proto-Iranian:** \*máHtā

**Latin:** materies, materia (both meaning "material")

**Germanic:** \*mōdēr

**Greek:** \*mā́tēr (Proto-Hellenic)

Additional descendants include Proto-Celtic (\*mātīr), Proto-Balto-Slavic (\*mā́ˀtē), Armenian (mayr), and Proto-Tocharian (\*mācer).
```


### [2026-09-07T01:43:04.843Z] TOOL RESULT

```
# Persian Etymology of مادر (Mother)

## Etymology Chain

**Middle Persian**: 𐭬𐭠𐭲𐭥 (mādar)

**Old Persian**: 𐎶𐎠𐎫𐎠 (mātā)

**Proto-Iranian**: *máHtā

**Proto-Indo-Iranian**: *máHtā

**Proto-Indo-European**: *méh₂tēr

## Source Citations

The Wiktionary entry provides this lineage: "From Middle Persian mādar, from Old Persian mātā, from Proto-Iranian *máHtā... from Proto-Indo-Iranian *máHtā... from Proto-Indo-European *méh₂tēr."

No specific citations to Hasandust, MacKenzie, or Cheung appear in the provided content.

## Persian Entry

**مادر** (mādar / mâdar) - mother, mama
- Plural: مادران (mādarān / mâdarân)
- Tajik spelling: модар (modar)

The entry includes extensive inflection tables and derived terms reflecting maternal relationships across Persian dialects.
```


## [2026-09-07T01:43:14.818Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%85%D8%A7%DB%80",
 "prompt": "Any Persian entry for ماده (māda/mādde) 'female' — its etymology (Middle Persian mādag?) and note the distinct Arabic مادّه 'matter'."
}
```


## [2026-09-07T01:43:15.747Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/mother",
 "prompt": "Give the etymology of 'mother': Old English modor, PIE *mater-, the nursery-word origin, and mention of Latin mater, Greek meter, Avestan/Sanskrit matar. Quote key phrases."
}
```


### [2026-09-07T01:43:16.140Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-07T01:43:21.053Z] TOOL RESULT

```
# Etymology of "Mother"

The word "mother" traces back through multiple linguistic layers:

**Old English Origin:**
"Middle English _moder_, from Old English _modor_" derives from Proto-Germanic *mōdēr, which spread across Germanic languages (Old Saxon _modar_, Dutch _moeder_, German _Mutter_).

**Proto-Indo-European Root:**
The ultimate source is PIE *mater-, a widespread kinship term found across ancient languages including Latin _māter_, Greek _mētēr_, and Sanskrit _matar-_.

**Nursery-Word Theory:**
According to the source, "this is '[b]ased ultimately on the baby-talk form *mā- (2); with the kinship term suffix *-ter-.'" This explains why similar forms appear universally—the root emerges from infant vocalization patterns common to human speech development.

**Comparative Evidence:**
The term appears consistently across Indo-European languages, suggesting an ancient origin predating the divergence of language families, reinforcing the baby-talk hypothesis as the foundation for this fundamental kinship word.
```


## [2026-09-07T01:43:27.344Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%85%D8%A7%D8%AF%D9%87",
 "prompt": "List the Persian entries for ماده: (a) māde 'female' — its etymology (Middle Persian mādag?), (b) mādde 'matter, material' from Arabic مادة. Quote the etymologies."
}
```


## [2026-09-07T01:43:29.096Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%85%D8%A7%DB%8C%D9%87",
 "prompt": "Give the Persian etymology of مایه (māye) 'leaven, essence, capital, substance' — Middle Persian form (māyag?), and any Proto-Iranian/PIE connection or link to مادر / *māter-."
}
```


### [2026-09-07T01:43:31.295Z] TOOL RESULT

```
# Persian Entries for ماده

## (a) māde 'female'

**Etymology:** "From Middle Persian NKḆ, mʾtk' (mādag), from Proto-Iranian *māta-ka- ('female creature'), from *māta- ('female'), from *máHtā ('mother')."

## (b) mādde 'matter, material'

**Etymology:** "Borrowed from Arabic مَادَّة (mādda)."

The first sense traces to ancient Iranian roots meaning "female," while the second represents a later Arabic loanword referring to physical substance or materials.
```


### [2026-09-07T01:43:35.938Z] TOOL RESULT

```
# Persian Etymology of مایه (māya/mâye)

Based on the Wiktionary entry, here's the etymological information:

## Middle Persian Origin

The word is "inherited from Middle Persian" with the form **mʾtk' /mādag/** meaning "essence, substance." There's also a Manichaean Middle Persian variant **mʾyg /māyag/**.

## Proto-Iranian Connection

The meaning "leaven" derives from Proto-Iranian ***(ham)mātaka(naH)*** meaning "(of) same material, mix." This connects to cognates across Iranian languages including Sogdian, Khwarezmian, Gurani, Zazaki, and Kurdish variants.

## Relation to *māter-

The document does not establish a direct connection between مایه and *māter- (the Indo-European root for "mother"). While both terms have ancient roots, the etymology section traces مایه specifically through the "essence/substance" sense via Middle Persian, rather than linking it to maternal terminology or Indo-European roots beyond Proto-Iranian.

The word's semantic range—from "essence" to "leaven" to "capital"—all flow from this Proto-Iranian root concept of "sameness" or "mixing."
```


## [2026-09-07T01:43:52.786Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"===== NYB glossary\"\ngrep -n \"^mād\\|^māt\\|^mātar\\|^mādar\\|^māyag\\|^mādag\" NYB_vol2_glossary.txt | head -20\necho \"--- nyb mother\"\ngrep -n -i \"mother\" NYB_vol2_glossary.txt | head -10\necho \"===== IEC Mann\"\ngrep -n \"^m[āa]ter-\\|^mahter\\|^mater-\\|^ma-ter\" IEC.txt | head -10\ngrep -n -o \"^m[āa]t[eē]r.\\{0,300\\}\" IEC.txt | head -10"
}
```


### [2026-09-07T01:43:54.040Z] TOOL RESULT

```
===== NYB glossary
2496:mātag-dān, mätiyän [m’tgd’n'] "that. which contains the kernel, the core, or substance and essence of a th., or funda- mentals, basic principles, etc.": 1. docu- ment; original and authentic, canonical text 1101; in titles: book, 108. 110. 111. — 2. the main body, the centre of an army, as opposed to the right and the left flank, the lifeguards of the king 119°. — From mätak (v.s. v. matakik) + -dan (cf zén-dan and NP); mätak-dän > mätag- dàn with -kd- > -yó-. This etymological
2498:mātag-dān
4913:māda-: Mād
--- nyb mother
63:"M, ’MY-: ’IMMI my mother
616:ärak ['k'; Prth STR’] side: ‘L LBR’ STR? outwards HajA:9 = 0 beh ärak, MPrth ^w byh rg (A-H III s. v. byh); tar matist — in the line of his maternal grandmother 3610-11; cas. obl. ~-éh: 6 dašn ārakēh + . . from Av. (193) arada-; MPrthPrs ?rg, ?rg.
1045:burtär [bwlt?l] 1. carrier, bearer, v. dén-~ framän-», nam-~. — 2. mother 372, 4018. 4319-28, 4416,
1247:dayak [d'yk'] mother 321%, — Kurd da (Edmonds, Kurdoev, Mardüx), däya (Mardüx); Sivand deyö, diyd, Abdūi dov ‘mother’ (Žukovskij, Matertaly II 331; his 6 = à); Bal dài ‘nurse, maid servant’, NP däyah ‘nurse, foster-mother, mid- wife’; Arm. lw. dayeak ‘nurse’. From Av. (724) 'däy- ‘to tend (cattle). Cf Benve- niste, JA 228, 1936, 196.
1371:Dugdáv [dwkt'wb'] n. pr., Zartux&t's mother 4112, 425.824, 432, 47°92, — Av. (748) Duydo.va-.
1470:évar ['dwl; 3% incorrectly y bl] adj. true [duat ~, with the gl. kū ke mat zat a true daughter, i.e. whom the mother has born PR 135-$:] adv. verily, certainly 38. — FrP 25: ’dwl : *ywl. Paz. čvar; NP ävar ‘true, certain’. V. also ēvarihā.
1515:Frähim Rwānly Zčiš [Paz.] tFrahin Rvänän Zčiš [*pl’hyn' lw’n'n' zwyš] n. pr. the mother of Zartuxst’s mother 371.5, — ‘The wife of Frahim Rwandan’, i.e. of Frähim of the Rwän clan, v. zētš. The perpendicular stroke after -ān- in Paz. Rwäng (confirmed by the now edited MS) is certainly only a reminiscence of the Phl. spelling, which sometimes sepa- rates the ending -än from its noun in this way, and has no significance. The husband's name is given in BdA p. 236}? as Ferahumruvänän, in BdJ 804 as Fra- humrava, both in Paz.
1806:ham-bavisnéh [hm YHWWN-Snyh] con- ception, with special regard to Zartuxšt: pas hac ~ i Zartuxét andar burtär mat 4320-21, the v.n. of the expression used 4317: han mart 6 ham bit ke Zartuxst that man who was Z. ‘came together’, 1. e., at the coition of his parents all the different earthly and heavenly elements which constituted his personality were brought together in his mother’s womb from different parts in different ways.
2154:kāc [k’c] would that ...: — ka (v. A. 5 in fine) man hac mätar nē zat hom would that I had not been born by my mother 2111-12, _ NP käc, kaj, or kāš ki.
2495:mat [m’t'; ^M] eas. obl. mätar [m’tl; "MY-tl] mother: cas. rect. mat (common- ly ^M) subj. 229. 394 [m?t']. 482°. 497.21, 633. 116*%; used as cas. obl. 36°. 4714. 6522-26; .. cas. obl. mätar (commonly ’MY-tl) gen. 124. 43°?. 6513; after prep. 2111, 224 (both m*tl). - Common Ir.
===== IEC Mann
10382:māter- (3) (?) ‘pad, coating MHG muoder, müeder, m. n. ‘corselet (mod. Mieder); OFris. mother, n. id.; if related to mäter (1), cf. Lat. måtrix, Gk. métrà and G Perl-mutter, E mother-of-pearl. (In sense of “lees, dregs’ cf. E mother, Du. moer (2) and Fr. mère de vinaigre, Moravian z-matetely *mouldy'. The semantic link is obscure)
10369:mātēr (màter-, mātr) (1) ‘mother’. Cf. maté and mati. WP II, 229 Skt. matt; Ober matar; Per. madar; Oss. cf. mad, madà; Tokh. macar, B macer; Arm. majr, gs mawr, ab. s. marb; Myc. matere(i), ds; Gk. méter, gs métrós; Doric mater; Phryg. māte- res, pl.; Alb. motër 'sister'!; Lat. mater, gs matris; Osc. ma
10382:māter- (3) (?) ‘pad, coating MHG muoder, müeder, m. n. ‘corselet (mod. Mieder); OFris. mother, n. id.; if related to mäter (1), cf. Lat. måtrix, Gk. métrà and G Perl-mutter, E mother-of-pearl. (In sense of “lees, dregs’ cf. E mother, Du. moer (2) and Fr. mère de vinaigre, Moravian z-matetely *mouldy'. Th
```


## [2026-09-07T01:43:54.942Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nd=open('incoming/WLD/WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read()\nparts=re.split(r'\\[pdf page (\\d+)\\]', d)\npg={}\nfor i in range(1,len(parts),2):\n    pg[int(parts[i])]=parts[i+1]\nprint('pages',min(pg),max(pg))\n# find matar\nfor n in sorted(pg):\n    if re.search(r'm[āa]t[eē]r-|mātér|mātér', pg[n]) and 220<=n<=250:\n        print(n, pg[n][:300].replace('\\n',' '))\nEOF"
}
```


### [2026-09-07T01:43:56.142Z] TOOL RESULT

```
Exit code 1
Traceback (most recent call last):
  File "<stdin>", line 7, in <module>
ValueError: min() iterable argument is empty
```


## [2026-09-07T01:44:08.762Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nhead -3 incoming/WLD/WLD_Bd2_pages.txt | cut -c1-200\necho \"-----\"\ngrep -c \"pdf page\" incoming/WLD/WLD_Bd2_pages.txt\npython3 - <<'EOF'\nd=open('incoming/WLD/WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read()\npages=d.split('\\f')\nprint('leaves',len(pages))\nimport re\nfor i,p in enumerate(pages):\n    if re.search(r'mater-|m[āa]t[eē]r', p) and 220<i<260:\n        print('=== leaf',i)\n        print(p[:1200])\n        break\nEOF"
}
```


## [2026-09-07T01:44:09.750Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"== NYB matak\"\ngrep -n \"matakik\\|^mātak\\|mätak\" NYB_vol2_glossary.txt | head -10\necho \"== IEC mater full\"\nsed -n '10369,10382p' IEC.txt"
}
```


### [2026-09-07T01:44:09.951Z] TOOL RESULT

```
                ALOIS WALDE


-----
0
leaves 725
=== leaf 225
                                             ma-                                        221


vergleicht Ficklll^SlO (zw.) mit ir. maith auch ags. mad-miindi^ ahd.
mammuntl „freundlich, mild, zahm“.
  Mit den kelt. Worten verbindet Fick II ^ 199 zw, (s. auch Boisacq s. v.)
gr. f^iatiQ *fieyag, riveg im rov paodecog Hes., das aber als „gro6“ eher
zu *me^ „gro6, ansehnlich“ gehort, wie auch kelt. ^rnati- eigentlich „*gro6
= tiichtig^^ sein konnte (Strachan KZ. 33, 304, Brugmann I^ 176). Ganz
fraglich ist, ob dazu mit Abtonung ^mo-to-^ acymr. maut, ncymr. baivd „Dau*-
men‘' {mod-rivy          mit einem zu   „binden'^ gehorigen 2. Glied, Peder-
sen KG. II 16), mbret. meut^ nbret. meud „Daumen“ gehore (ir. mtr „FingeF‘
bleibt trotz Zupitza KZ. 35, 259,  Pedersen KG. I 134 f., 296 fern;                s,   auch
u. mCth „lang‘0'     Woran wieder arm. main „Finger“ (niatani
fallig anklingt,wenngleich arm. f statt t zu erwarten ware (Lit. bei Peder-
sen KZ. 39, 388; seine Annahme von idg. Wechsel d:t\m Auslaut benahme
der Vergleichung aber ihre Uberzeugungskraft).
   Da6 ai. mdta'^ga- als Beiwort des Elephanten eigentlich der „groBe,
Starke'' bedeute (Petersson Fran fil. foreningen i Limd,
```


### [2026-09-07T01:44:10.005Z] TOOL RESULT

```
== NYB matak
391:a-mätak [-NKB] non-female 1041”. — V. matak.
2496:mātag-dān, mätiyän [m’tgd’n'] "that. which contains the kernel, the core, or substance and essence of a th., or funda- mentals, basic principles, etc.": 1. docu- ment; original and authentic, canonical text 1101; in titles: book, 108. 110. 111. — 2. the main body, the centre of an army, as opposed to the right and the left flank, the lifeguards of the king 119°. — From mätak (v.s. v. matakik) + -dan (cf zén-dan and NP); mätak-dän > mätag- dàn with -kd- > -yó-. This etymological
2505:matak [NKB; m’tk'] female: gor ~ 112-4 (m’tk'); ~ karp 5717; čvak nar u čvak m 949-10.,,.., a-~ female... non-female 1041617, — Arm. lw. matak; MPrs m’yg (!); Paz. mädagi = abstr. mätakeh (SGV VIII, 16) and = mātakīk (ibd. XV, 27); NP mddah: from mat (g. v.).
2506:mätakik [m?tkyk] belonging to, con- sisting of, materials: cis i ~ kart things made of materials — art handiwork 1189-339, — From mätak ‘the essential element of anything, its core, essence; materials’, Paz. madag (SGV XV, 53), but MPrs myg ‘substance, nature’ (A- H II); NP mäyah. Arab mäddat-“matter’ is borrowed from mddag, but Arabized through association with madda 'to ex- tend’. l
2507:mätak-var [m’tkwl] principal, essential, chief 8722. 10426. — Paz. mādavar; cf Arm. lw. matakarar < *mātaka-dāra- ‘administrator’; v. the preceding w. — Bailey, ZP 100, and BSOS XI, 1941, 796 sq.
3083:pat-sén [PWN syn'] breast bodice 5718, — DkM 63514-15: apar-ic 6 tē, Zartuxst, druž bē dvārēt mätak-karp, zarren-patsen (ku pistin-pin dārēt), v. pistan. — FrP 31 sénak, NP sinah ‘bosom, breast’.
6043:m’n’g: mānākēh m'ny: Mani m’yg: mätakik mgj: mazg
6705:mädagi: mätak, -kik mädavar: mätakvar mahest: mas mahést: mazdčsn mahi: mas
== IEC mater full
mātēr (màter-, mātr) (1) ‘mother’. Cf. maté and mati. WP II, 229 Skt. matt; Ober matar; Per. madar; Oss. cf. mad, madà; Tokh. macar, B macer; Arm. majr, gs mawr, ab. s. marb; Myc. matere(i), ds; Gk. méter, gs métrós; Doric mater; Phryg. māte- res, pl.; Alb. motër 'sister'!; Lat. mater, gs matris; Osc. maatreís, gs; Umb. matrer, gs; (?) Faliscan materei, ds; Olr. máthir, Ir. má- thair, gs máithre; Gaul. matre-bo, dpl.; W cf. modr-yb (“aunt', fr. *màtriqua); OHG muoter; OE moóor, ds meóer; ON móðir, gs móður & moeór; OCS materi beside mati, gs matere; Slovak mat, mati & mater; R mat, gs materi; Li. móte, gs móters & móteris, f. ‘woman’; cf. móčia ‘mother; Latv. (isophone) materes, pl. Cmotherwort', bot.)
måter- (2) ‘wood, timber, substance Skt. cf. matr, f. 'firestick'; Arm. majr (2) ‘pine, cedar'; majri, gs -vo, ab. s. -eav “forest'; Lat. materies, gs -iei, and materia, -iae, f. “branch, timber, matter, substance’; R cf. materój ‘sea- soned, hardened'; materét, v. ‘harden, get
mast- — matios, om, 9
10
15
20
25
30
35
40
45
736
seasoned, grow’; cf. Moscow dialectal matéryj (big, robust, hale, hardy, aged, hard, virgin, of land’. AP: ESR Ja.). A parallel form is seen in Lat. maturus "mature: OCS mator, adj. ‘old’. (Isophones: Du. moeder-kruid, E mother-wort, Latv. màteres, bot.)
māter- (3) (?) ‘pad, coating MHG muoder, müeder, m. n. ‘corselet (mod. Mieder); OFris. mother, n. id.; if related to mäter (1), cf. Lat. måtrix, Gk. métrà and G Perl-mutter, E mother-of-pearl. (In sense of “lees, dregs’ cf. E mother, Du. moer (2) and Fr. mère de vinaigre, Moravian z-matetely *mouldy'. The semantic link is obscure)
```


## [2026-09-07T01:44:24.350Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nd=open('incoming/WLD/WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read()\npages=d.split('\\f')\nfor leaf in (232,233,234):\n    print('##### leaf',leaf,'printed ~',leaf-4)\n    print(pages[leaf][:2600])\nEOF"
}
```


### [2026-09-07T01:44:25.555Z] TOOL RESULT

```
##### leaf 232 printed ~ 228
228                         iuag(h)-   — mat- oder mot-
ii[iag(h)-   „etwas.Kleines“??
    Alb. module „Erbse‘‘, lit. moHs „Kleinigkeit‘' (Pedersen KZ. 36, 335 zw.)
lit. 7nazas „klein‘\ mdftnfi   „klein macben, verringern'' (Wood Mod. Phil.
11, 31 8f. vergleicht mdzas nicht uberzeugend mit nhd. mdhtln),


maghn- „Knabe, Jungling, nnverheiratet'' und zugehorige Pem.-Bldgn.
   Av. mayava- „unYerheiratet“ (Bartholomae Airan. Wb. 1111); kelt. "^magiis
(s. zum Vokalismus Pokorny KZ. 45, 73)     in gall. Magii-rix^ ir. (Ogam)
magu, air. mang, mug „Sklave'‘; corn, matv^ bret. mao „Jungling, I)iener“,
cymr. meu-dwy „Ein8iedler‘^ (eig. „Diener Gottes“); Pem. com. mowcs
„Madchen“, bret. maouez „Prau''; kelt. -mo- Ableitung in air. mam, mdam
,jugum, servitus“ (Lit. bei Liden BB. 21, 99, der es aber selber unrichtig
zu germ. *makdn stellt, s. *mag- „kneten“); Abstraktum kelt. *magot-acta
jjJungferaschaft, junge Weiblichkeit'* (weitergebildet aus ^maghotis     =  got.
magaps) in ir. ingen maccdacht ,junges erwachsenes Madchen^^, air. ro-
macdact gl. „superadulta“, acorn, mahtheid „virgo‘‘, mcorn. maghteth, maghtyth,
ds., bret. matez „Dien8tmadchen“ (gegen Verbindungen dieser Pormen mit
air. macc, cymr. mah „Sohn“ s. Yf. Tiber alteste sprachl. Beziehungen zw.
Kelten und Italikern 60ff.) got. magus „Knabe“, aisl. mqgr „Sohn, junger
                                 ;


Mann“, as. magu „Knabe“, ags. magu               Sohn, Mann“; Pem. ^ma{y)wJ
in got. mawi „Madchen“ (gen. maujds\ aisl.             (Acc. mey) „Madchen‘‘,
Demin, got. mawilo^ aisl. meyla, ags. meowle „kleines Madchen'^; Abstractum
*maghotis „junge Weiblichkeit^', woraus konkret „Madchen“, in got. magaps
,
 junge Prau“, ags. mmgep (engl. maid)^ as. magath^ ahd. magad^ nhd. Magd^
Demin. Mddchen, Die kelt.- germ. Yerkniipfung nach Pick II ^ 198. Air.
macc „Sohn“ usw. nach Pokorny (KZ. 45, 363) Koseform zu magu-,
   Nicht haltbare andere Gruppierungen bei Zupitza Gutt. 65 f., Wiedemann
BB. 28, 62; iiber got. megs usw. s. vielmehr u. megJi- „wohlge8innf‘, liber
got. magan „verm6gen“ u.            „k6nnen“ mit letzterem will auch Brug-
                                                 ;

mann IP. 38, 140 f. unsere Sippe zusammenbringen nach Bed.-Yerhaltnissen
wie ai. hdla-m ,, Kraft, Starke''; hald-li „ Junge, Kind“, doch weist das zu
mclgJi- gehorige gr. f^ifjyog^        nicht so sehr auf das kraftige, als auf
das geschickte     Konnen als Bei-Kern dieser Wz. jnagJi- „konnen".

1.   mat- oder mot- in Worten fur nagendes, beifiendes Gewurm oder Uno-e-
                                                              
##### leaf 233 printed ~ 229
                                                         ;:




                                     mat-     — mater-                                229

2. mat- etwa „Hacke, Schlagel“.
  Ai. matyd- n. „Egge oder Kolben oder dgl/*, matikrta- j,geeggt oder
gewalzt“; lat. mateola „Werkzeug zum Einschlagen in die Erde“ (im Eoman.
lebt nicht deminuiertes *mattea „Keule% s. Meyer-Liibke EEWb. 396); abg.
motyka „Hacke“ (Bugge und Bezzenberger BB. 14, 57, Persson Wzerw. 34);
ahd. (gl.) medda „Pflug‘‘ (Lehmann AfneuereSpr. 119, 188), mit germ, it
(aus           ags. maitoc, engl. mattock „Hacke“, ahd. stein-me^zo „Steinmetz^‘
(s.   Vf. LEWb.^ u. maicilis, sowie u,
                                   mad-         wo iiber Methvurst usw.
und gegen Sommer IF. 11, 265 f. Parallelwz. mad- „hauend schneiden“}.

mat^r- „Mutter“, beruht auf dem Lallwort                      s.   d.    (Kretschmer Einl,
    353 ff.; verkehrt Wiedemann BB. 27, 219f.).
   Ai. mafdr- „Mutter“, av. matar-, arm. (Hiibschmann Arm. St. I 41, Arm.
Gr. I 472) mair ds. (Gen, maur         gv, juyxQog usw.); gr. /xyprjQ, dor. ^djrjQ
(mit verschobenem Nominativakzent, wie ^vyatyg^ s. Vendryes Msl. 13, 139
aber acc. -xeQa); alb. 7notr6 „Schwester‘' (ursprgl. „die altere, Mutterstelle ver-
tretende Schwester‘^ G. Meyer BB. 8, 190, Alb. Wb. 287 f.); lat. mater, -tris,
osk. maatreis, u. matrer „matris“; gall. MaxQE^o „Matribus‘^; air. maihir
„Mutter'' (cymr. ^nodrydaf „Bienenstock“ mit hydaf „Nest wilder Bienen‘‘
als 2. Glied); ahd. nmoter, ags. mMor, aisl. modr „Mutter'^; lit. moU (g.
7notcrs)    „Weib, Ehefrau^^ {mofyna „Mutter‘^, 7noterd „Prauenzimmer, Weib“),
lett.         „Mutter“, apr.      mothe            {pomatre               abg.
math (gen. matere) „Mutter“.
   Curtius 333, Delbriick Verwandtschaftsnamen 450 fF. passim^ Pick I ^ 508,
      199, III^ 323 usw.; an Ableitungen vgl.
   ai. mdtrka- „mutterlich^‘, m. ^Mutters Bruder“, ynatrka „Mutter, GroB-
mutter"* im Formans nicht gleichzusetzen mit ncymr. modryh „Mutters-
schwester'^, acymr. lyiodrep-ed PL, abret. motrep^ nbret. moereb ds. (^matrcpid ;
s.    Brugmann    I, 474 f., der freilich nicht befriedigend Zs. mit 6i^i\.,sehen‘‘

als „wie eine Mutter aussehend^^ annimmt, Pedersen KG. II 33).
   Gr. juijtQa „Gebarmutter (diese Bed. auch z. B. in russ. yndtka), Mark
der Pfianzen'^ lat, matrix „Gebarmutter; Zuchttier^, ahd. muodar „Bauch
einer Schlange‘‘, and. yndder^ afries, mother „Brustbinde der Frauen^, mhd.
wiueder, nhd. Mieder\
   arm. ynaiiru^ gen. maurui „Schwiegermutter^‘ (Hubschmann Arm. Gr. I
472 Gdf, "^mcdrimid =) gr. /LtrjjQvid „S
##### leaf 234 printed ~ 230
                                 i




230                                        mater     mad-


„Baiiliolz,    Holz iiberhaupt, Geholz^" (Fr. Muller SB Ak. Wien 122, 4; Fick P
508 zw.,       SolmsenBPhW. 1902, 1140, Meringer IF. 16, 141, Yf. LEm.^
s.   V.),   wozu Meillet Et. 407, Lewy KZ, 40, 562, Berneker II 25 auch russ.
materoj „au6erordentlich, groB, stark^ stammig, fest“, serb. mator „alt, bes.
Yon Tieren“ (vgl. abg. star^ „alt“ aus „*stammig“), abg. materhstvo ^^ttqeg-
Peiov^\ mmatoreiThy   mmalerevh „betagt‘* stellen. Als Bed.-Entw. Yermutet
Berneker Yom Baum gesagt „Mutterbaum, SchoBlinge treibend^' (Ygl. die
Bed. „Gnind8tock“ in den Ableitungen Yon               von Tieren „Muttertier'‘,
daher „ausgewaclisenes reifes TieP^, darnach allgemein stark'' und „alt“.
                                                             ,,


Doch erweckt dasdabei anzunehmende vollige Yerblassen der ursprunglichen
Beziehung auf nur das weibliehe Tier wenig Yertrauen und bote eine
Baum- Oder Holzbezeichnung nach dem Yerhaltnis bqvov’ loyvQov: dgvg;
Lewy aaO.) jedenfalls eine natiirlichere Grundlage filr die si. Bed. ..groB,
alt". Da auch arm. mairi^ das nach Liden IF. 18, 493 genauer „Wald von
Nadelholz, von Zedern, Fichten" bedeutet und eine Ableitung von mair
„pinus, abies, cedrus; pineus, abiegnus, cedrinus" ist, auf eine Baumbezeich-
nung weist (Lidens Yerb. des arm. Wortes mit aisl. meidr                    lat.
meta leuchtet aber nicht ein), ferner ai. inatarl-^van- „der Name des ind.
Prometheus" wahrscheinlich als „materiae foetus, aus dem Eeibholz ge-
borenes Feuer" gedeutet wird (Fay KZ. 45, 134), und endlich fur lat.
materia eine Bed.-Ent. von „Gebarmutter" zu „Mark der Baume" (wie bei
juijrga) und weiter zu „Bauholz" mindestens nicht wahrscheinlicher ist als
die Yerb. mit den obigen Worten, ist wohl ein idg. Baumname mater- zu
erschliefien; ob dazu auch gall, juaragig TcaXiovri eldog Strabo, juaSaoeig-
jiXaTvrega Xoyyidia Hes., Medio-inatrici wenn soviel wie ^Mittenwaldler" ?
(Fickl^508 zw., LewyaaO. Bed. ware wie bei dogv; anders Fick 1P200).
                                      ;


   Abweichend stellt Petersson, Fran fil. foreningen i Lund, Sprakl. uppsatser
 lY (1915), 128 die slav. Sippe unter Trennung von materia und von maii{i)
 zu ^dng „fiEyag^\ air. maith „gut" (und ai. mdiaraga- Beiwort des Elephanten,
das „stark, groB" bedeute); aber die formantische tTbereinstimmung emp-
fiehltobige Auffassung.

 mater- ..Baumname":        s.   u.       mater- „Mutter“.


mad- „na6, triefen; auch von Fett triefen, volisaftig, fett. geniastet";    iia-
```


## [2026-09-07T01:44:38.576Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nd=open('incoming/WLD/WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read()\npages=d.split('\\f')\nfor leaf in (225,226):\n    t=pages[leaf]\n    i=t.find('Lallwort')\n    print('##### leaf',leaf,'printed',leaf-4, 'Lallwort at',i)\n    if i>0: print(t[max(0,i-1800):i+900])\nEOF"
}
```


### [2026-09-07T01:44:39.891Z] TOOL RESULT

```
##### leaf 225 printed 221 Lallwort at 1316
                                             ma-                                        221


vergleicht Ficklll^SlO (zw.) mit ir. maith auch ags. mad-miindi^ ahd.
mammuntl „freundlich, mild, zahm“.
  Mit den kelt. Worten verbindet Fick II ^ 199 zw, (s. auch Boisacq s. v.)
gr. f^iatiQ *fieyag, riveg im rov paodecog Hes., das aber als „gro6“ eher
zu *me^ „gro6, ansehnlich“ gehort, wie auch kelt. ^rnati- eigentlich „*gro6
= tiichtig^^ sein konnte (Strachan KZ. 33, 304, Brugmann I^ 176). Ganz
fraglich ist, ob dazu mit Abtonung ^mo-to-^ acymr. maut, ncymr. baivd „Dau*-
men‘' {mod-rivy          mit einem zu   „binden'^ gehorigen 2. Glied, Peder-
sen KG. II 16), mbret. meut^ nbret. meud „Daumen“ gehore (ir. mtr „FingeF‘
bleibt trotz Zupitza KZ. 35, 259,  Pedersen KG. I 134 f., 296 fern;                s,   auch
u. mCth „lang‘0'     Woran wieder arm. main „Finger“ (niatani
fallig anklingt,wenngleich arm. f statt t zu erwarten ware (Lit. bei Peder-
sen KZ. 39, 388; seine Annahme von idg. Wechsel d:t\m Auslaut benahme
der Vergleichung aber ihre Uberzeugungskraft).
   Da6 ai. mdta'^ga- als Beiwort des Elephanten eigentlich der „groBe,
Starke'' bedeute (Petersson Fran fil. foreningen i Limd, Sprakl. uppsatsen
lY 128), ist unerwiesen; iiber russ. materoj „gro6, stark" usw. s. u. mater-
.jMutter".


3. Ilia Lallwort fiir „Mutter", redupl. mania, manimE; z. T. (Dissimilation?)
        nianA manna zweifelhaften Alters. Obwohl das unred. ma die Gdlage
        von mater- (s. d.) ist, konnen seine einzelsprachlichen Belege aus "^mater-
        neugebildete Lallworte sein.
  Ai.     ma „Mutter": np. mam^ mama^ maml „Mutter";
  dor. jud                  (in   yd yd   „o Mutter Erde", Aesch.),   wovon jon. att.
yata „Mutter, Amme, Hebamme", dor. „Gro6mutter" (Delbriick Yerwandt-
schaftsnamen 451; s. zur Form u. ^auos „Gro6vater“) abgeleitet mnd. moie
                                                              ;


„Mutterschwester", ahd. holz-muoja „Hexe“ (Fick III * 323).
  Ai. mama- m. „Onkel" (von ^niama „Mutterschwester")       arm. mam    ;



„Gro6mutter" (gr. Lw. wie jmp nach Hiibschmann Arm. Gr. I 341?); gr.
ydyya Lallvokativ, wovon jon. att. ydyyr} Mutter" (Solmsen Beitr. I 268),
        
##### leaf 226 printed 222 Lallwort at -1
```


## [2026-09-07T01:44:46.690Z] TOOL CALL #53: WebFetch

```json
{
 "url": "https://www.ahdictionary.com/word/indoeurop.html",
 "prompt": "Find the entries for the roots \"māter-\" and \"mā-2\" (or ma-). Quote them in full, including the derivative lists (Germanic, Latin, Greek, materies/materia) and the Pokorny page references."
}
```


## [2026-09-07T01:44:47.801Z] TOOL CALL #54: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/material",
 "prompt": "Give the etymology of 'material' and of Latin materia/materies — including whether it derives from mater 'mother' and the \"tree's source of growth / trunk\" sense, and the calque on Greek hyle."
}
```


### [2026-09-07T01:44:51.695Z] TOOL RESULT

```
I cannot locate the entries for "māter-" and "mā-2" in the provided document. The content shown contains Indo-European roots beginning with letters A through B, ending partway through the B section. The roots you're seeking, which would appear under the M section, are not included in this excerpt.

To find these entries, you would need to access the complete appendix or jump to the M section using the navigation links shown at the top of the document.
```


### [2026-09-07T01:44:53.961Z] TOOL RESULT

```
# Etymology of "Material"

**Material (adj./n.):**
The word entered English in the mid-14c. from Old French *material* and Late Latin *materialis*, meaning "of or belonging to matter."

**Latin *materia*:**
According to the source, *materia* derives from *mater* ("origin, source, mother"), following etymologists de Vaan and Watkins. The Latin term originally meant "substance from which something is made" and also "hard inner wood of a tree."

**Greek Influence:**
The sense development in Latin philosophy was influenced by Greek *hylē* (meaning "wood, firewood; material in general"), which Aristotle employed for the philosophical concept of "matter." This represents a semantic calque—the Greek concept of fundamental substance was mapped onto the existing Latin word.

**Meaning Evolution:**
Early senses included "subject matter" (c. 1200), then expanded to "physical substance generally" (mid-14c.), and later "important, relevant" (late 15c.), particularly in legal contexts.

The etymological chain thus connects the root concept of "mother/source" through the physical sense of tree wood to abstract philosophical notions of material substance, paralleling Greek philosophical terminology.
```


## [2026-09-07T01:45:01.496Z] TOOL CALL #55: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%85%D8%A7%D9%85%D8%A7%D9%86",
 "prompt": "Give the Persian entry for مامان (māmān) — its meaning and etymology. Is it from French maman, or a native nursery word? Quote the etymology exactly."
}
```


## [2026-09-07T01:45:03.418Z] TOOL CALL #56: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%F0%90%AC%A8%F0%90%AC%81%F0%90%AC%99%F0%90%AC%80%F0%90%AC%AD",
 "prompt": "Give the Avestan entry 𐬨𐬁𐬙𐬀𐬭 (mātar) — meaning, etymology (Proto-Iranian *máHtā, PIE *méh₂tēr), and descendants."
}
```


### [2026-09-07T01:45:05.372Z] TOOL RESULT

```
# Persian Entry for مامان (māmān)

**Meaning:** An informal word for "mother" (mama), primarily used in Iranian Persian urban dialects.

**Etymology:** The word is borrowed from French. According to the entry:

> "Borrowed from French _maman_. Displaced _ننه_ (nana / nane) in most urban dialects of Iran."

So مامان is **not** a native nursery word, but rather a loanword from French that has replaced the earlier Persian term "nana/nane" in modern Iranian usage.
```


### [2026-09-07T01:45:07.789Z] TOOL RESULT

```
# Avestan 𐬨𐬁𐬙𐬀𐬭 (mātar)

## Meaning
This feminine noun means "mother."

## Etymology
The word derives from Proto-Iranian *máHtā, which itself comes from Proto-Indo-European *méh₂tēr. The entry notes cognates including Old Persian mātā and Sanskrit mā́tṛ.

## Linguistic Descendants
While the page doesn't explicitly list modern descendants, the etymological chain shows this root produced the word for "mother" across Indo-European languages. The entry demonstrates connections to forms in Armenian, Greek, Slavonic, Latin, and English (through "mother").

## Declension
The word follows a feminine declension pattern with forms documented for nominative, accusative, and other cases across singular and plural numbers in the ancient language.
```


## [2026-09-07T01:45:12.814Z] TOOL CALL #57: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/metropolis",
 "prompt": "Give the etymology of 'metropolis' and 'metropolitan' — Greek mētēr 'mother' + polis 'city', and the route into English (Late Latin metropolis, ecclesiastical use)."
}
```


## [2026-09-07T01:45:14.062Z] TOOL CALL #58: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/mammal",
 "prompt": "Give the etymology of 'mammal' and Latin mamma 'breast' — including that mamma is a reduplication of the baby-talk syllable ma, and Linnaeus's Mammalia (1758)."
}
```


### [2026-09-07T01:45:17.805Z] TOOL RESULT

```
# Etymology of Metropolis and Metropolitan

**Metropolis** (noun, 1530s) derives from Late Latin *metropolis*, which comes from Greek. The word combines two Greek elements: *meter* meaning "mother" and *polis* meaning "city."

**Metropolitan** (noun, mid-14c.) follows the same Greek roots through Late Latin *metropolitanus*. In Greek, *metropolis* literally meant "mother city" – referring to a "parent state of a colony" or "capital city." The ecclesiastical sense emerged in church terminology, where a "metropolitan" was "a bishop having general superintendency over other bishops of his province."

Both terms entered English through Late Latin during the medieval and early modern periods. The secular meaning of metropolis as "chief town or capital city of a province" became established by the 1580s, though earlier English alternatives included *metropol* (late 14c.) and *metropolitan* (mid-15c.).

The compound structure—combining the concept of "mother" with "city"—reflects the ancient practice of colonial cities maintaining hierarchical relationships with their founding urban centers.
```


### [2026-09-07T01:45:18.498Z] TOOL RESULT

```
# Etymology of Mammal

**Mammal** entered English in 1826 as an Englished form of Modern Latin *Mammalia*, which Linnaeus coined in 1758 to classify animals that nurse their young.

The term derives from Late Latin *mammalis* ("of the breast"), which itself comes from Latin *mamma* meaning "breast." The word *mamma* is "a reduplication of *\*ma-* that is nearly universal among the Indo-European languages," likely originating as a natural sound in infant vocalization, "perhaps imitative of sound made while sucking."

This same root gave rise to the word for mother across numerous languages—Greek *mamme*, Persian *mama*, Russian *mama*, German *Muhme*, and French *maman*—reflecting how babies' earliest sounds became the foundation for terms of maternal address across Indo-European cultures.
```


## [2026-09-07T01:45:28.362Z] TOOL CALL #59: Bash

```json
{
 "command": "for u in \\\n 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/méh₂tēr' \\\n 'https://en.wiktionary.org/wiki/مادر' \\\n 'https://en.wiktionary.org/wiki/ماده' \\\n 'https://en.wiktionary.org/wiki/مایه' \\\n 'https://en.wiktionary.org/wiki/مامان' \\\n 'https://en.wiktionary.org/wiki/𐬨𐬁𐬙𐬀𐬭' \\\n 'https://www.etymonline.com/word/mother' \\\n 'https://www.etymonline.com/word/material' \\\n 'https://www.etymonline.com/word/metropolis' \\\n 'https://www.etymonline.com/word/mammal' ; do\n python3 tools/fetch_source.py \"$u\" --note 'page 316, root Mâ/Mâ-ter, verification of mother/mater/mamma/materia/metropolis chain' 2>&1 | tail -2\ndone"
}
```


### [2026-09-07T01:45:33.260Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/e0c6188092245b43.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9d6cff32cba19e8c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/98f56314cc731e8c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d851a920aad42d02.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b3622d78f120dc15.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/205b2ed92cf8de05.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/791f9c06a1140af9.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/cdca59476264b582.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d74bc3d8ecf10c9b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8ea93767c5bc7a5d.txt
```


## [2026-09-07T01:46:04.828Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\npages=open('SKT.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('leaves',len(pages))\nfor i,p in enumerate(pages):\n    if 'Mother.' in p and 'Moth' in p:\n        pass\nfor i,p in enumerate(pages):\n    if re.search(r'Mother,? *\\(E', p) or 'Mother. (E.)' in p or 'Mother, a female' in p:\n        print('leaf',i); print(p[:1200]); break\n# locate 'Maternal' leaf\nfor i,p in enumerate(pages):\n    if 'Maternal.' in p:\n        print('=== Maternal leaf',i, 'header:', p[:120].replace('\\n',' '))\nEOF"
}
```


### [2026-09-07T01:46:06.016Z] TOOL RESULT

```
leaves 657
=== Maternal leaf 298 header: Maoerata. Maas  (j),  the  celebration  of  the  Eucha- rist ;  see  Sllaaile. Uaasacre.  (F.  -  O.  Low  G.  ?)  F mas
```


## [2026-09-07T01:46:16.855Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\npages=open('SKT.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (296,298,300,302,304,306,308,310,354,356,358):\n    p=pages[i]\n    nums=re.findall(r'\\b(2\\d\\d|3\\d\\d)\\b',p[:400])\n    print(i,nums[:6],'|',p[:100].replace('\\n',' '))\nEOF"
}
```


### [2026-09-07T01:46:18.157Z] TOOL RESULT

```
296 [] |  E. markis.  —  O.  F.  marJh's,  later  marquis.  *  a marqaene,  goveranur  of  a  frontirc  town 
298 [] | Maoerata. Maas  (j),  the  celebration  of  the  Eucha- rist ;  see  Sllaaile. Uaasacre.  (F.  -  O.
300 [] |   as  Spaa,  dtsmajar, to  dismay,  ttrriiy.  The  O.  F.  dtsmaytr was  early  supplanted  by  esma
302 [] |   tmdicus  (above)  ;  meduatt. meditate.  <L.)  From  pp.  of  L- meditari,  to  ponder  :  a  freq
304 [] |  mien,  look.  (F.-Ilal.-L,)  F.  mim, 'the  look;'  Cot.  —  U.1I.  mina  (Sclieler, LitlTtTl,  the
306 [] | .  metaJ.^ O.  F.  mttal.  *  L.  me/ailum,  a  mine,  metal. —  Gk-  fUraKXaf,  a  cave*  minei  mi
308 [] |  mi/d*.  A.S. miide.  +  Du.  mild,  Icel.  mi/dr,  Dan.  Swcd. G.  mi/d;  Goth,  miliis,  only  in 
310 [] | .)  F.  a^mirtr.^V  ad- mirari,  to  wonder  it  —  L.  aJ,  at ;  miron, to  wonder  (above). marwl
354 [] | IvfrfAort  a  plane  surface, ;.  af  lafovAor,  on  the  giouod,  from  Jni. sad  «i8or,  the  grcf
356 [] | ritory,  a  wild  flower R^on  walU.  (F.-L.)  PtUilory trit&ry,  M.  E  pariiorii.—O,  F. ,  •pcllt
358 [] |   OD  whom  all  libels  are 1*1000.  From  ihs  oaiuc  of  a ome,  whose  atall  was  frerjucnted h
```


## [2026-09-07T01:46:31.396Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\npages=open('SKT.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in range(300,320):\n    p=pages[i]\n    m=re.search(r'Mother.{0,700}', p, re.S)\n    if m and 'A.S.' in m.group(0)[:300]:\n        print('leaf',i); print(m.group(0)[:800]); break\nelse:\n    for i in range(300,325):\n        if 'Mother' in pages[i]:\n            j=pages[i].find('Mother')\n            print('leaf',i,'>>',pages[i][j-100:j+700])\n            print('-----')\nEOF"
}
```


### [2026-09-07T01:46:32.747Z] TOOL RESULT

```
leaf 306 >> a state  ;  the  city  of  a  primate.  »  Gk.  jiv^J for  M^rrjp,  a  mother ;  ir^^n,  a  aXj.  « Mother  and  PoUoe.
Mettle ;  see  UetoL
Mew  (I),  10  cry  as  a  cat  \%^  ¥•' mawen;  a  word  of  imitative  oftgia.4*N mow,  Arab,  mua,  mewing  of  a  cat MwW,  from  F.  mianUr,  to  mew.
mew  (j),  a  scagnU.  (E.)    M.K.I A.  S.  m4»v,  amew.-f  Du.  wutuw.  lud Dan.  maage,  Swed.  mAJte^  G.  m^vn, the  mew  or  cry  of  the  biid.
Mew  (3),  a  cage  for  bawk«t  ftfti pi  oi  mrw\  see  Mutable.
Mewl ;  sec  Menr  (1).
Mewaj  M<  Mutable.
MEZZOTINTO
ktlxUo :  see  H»dium
pollution,    infectioDS    mBtter.
.)     Gk.  fiamita,  a  sUia.»Gk.  fuaivuv,
tin.
�
-----
leaf 318 >> tk  --  K.  mawk\  CtttM of  the  foim  which  appears  as  A.  S. Du.  G.  madt,  maggot  (nbove).
Mother  ( I ).  a  female  parent. mcdtr.  A.  S.  mSJtr,  mtUor,  a chitnge  from  d  to  M  seems  n infIucncc-+Du.  mocder,  Icel.  ■ Swed.  modtt\  C.  mutter,  IriJ. matkair,  Russ.  mati,  Lithuan mater,  Gk.  t^njp,  Skt.  mdtd,  mdtii.  %  A formed  with  Aryan  suflix  -/ar(oi'lheacn' from  ^MA,  orig.  to  meaaure;  cf.  Skt. to  measure.  Orig.  ftense  uncenam,  |icl '  manager  *  of  the  nousehold.
mother  (a),   hysterical    pasnoo.  (t In   King  Lear,  ii.  4.  i,(f.      Sfclt  m»Jff Palsgrave:    and    the    same    woni    at  t above. 4'Dn'  moidtr,  a  mother,  womtv  b| terical  passion ;  cf.  G  mutttrittc. mother-
-----
leaf 319 >> 
-----
```


## [2026-09-07T01:46:57.751Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"===== LAT mater\"\ngrep -n -o \"^mater,.\\{0,800\\}\" LAT.txt | head -3\necho \"===== LAT materies\"\ngrep -n -o \"^materi[eē]s.\\{0,700\\}\" LAT.txt | head -3\ngrep -n -o \"^mamma,.\\{0,500\\}\" LAT.txt | head -3\necho \"===== LEW mater\"\ngrep -n -o \"^mater.\\{0,600\\}\" LEW_1910.txt | head -4\ngrep -n -o \"^mamma.\\{0,400\\}\" LEW_1910.txt | head -3"
}
```


### [2026-09-07T01:46:58.981Z] TOOL RESULT

```
===== LAT mater
===== LAT materies
36832:materies, -ria, -rium, 5407 *mSteriamen ( fr. merrain), 5408 *mdteria-
36013:mamma, -ae f.: "maman" et "mamelle"; d'ou "protub^rance en forme
51084:mamma, mamilla, etc.) qui dans lal.du droit a pris le sens de "pu¬
63107:mamma, pappa. M.L.85y6. Cf. Tatius?
===== LEW mater
14636:materoj II 51, 54
14637:materosa (alt) II 52
```


## [2026-09-07T01:47:05.132Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -o \"m[aā]ter, *-tris.\\{0,900\\}\" LAT.txt | head -3\necho \"---- materies entry\"\ngrep -n -o \"materi[eē]s, *-[a-z]*.\\{0,900\\}\" LAT.txt | head -5\necho \"---- matrix\"\ngrep -n -o \"matrix,.\\{0,500\\}\" LAT.txt | head -3\necho \"=== LEW\"\ngrep -n -o \"m[aā]ter *,.\\{0,700\\}\" LEW_1910.txt | head -3\ngrep -n -o \"materi[eē]s.\\{0,600\\}\" LEW_1910.txt | head -3"
}
```


### [2026-09-07T01:47:08.160Z] TOOL RESULT

```
---- materies entry
ugrep: error: error at position 72
x93)s, *-[a-z]*(?:[^\n\x80-\xbf][\x80-\xbf]*){0,900}
                       exceeds complexity limits___/


---- matrix
=== LEW
```


## [2026-09-07T01:47:11.985Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"mater\" LAT.txt | grep -i \"mère\\|mere\\|nourr\" | head -8\necho \"----\"\nsed -n '36013,36030p' LAT.txt\necho \"==== search materies block\"\ngrep -n \"materies\" LAT.txt | head -10"
}
```


### [2026-09-07T01:47:12.065Z] TOOL RESULT

```
36740:corpore, ou il designe la branche mere, le troirc principal; materies .
36846:De meme que mdter designe la nourrice, materies a quelquefois le
----
mamma, -ae f.: "maman" et "mamelle"; d'ou "protub^rance en forme
de mamelle" (Pline 17,118). Mot du langage enfantin, cf. Varr., Cato
uel de pueris educandis (14) ap.Non.81,4, cum cibum ac potionem buas
ac pappas uocent, et matrem mammam, patrem tatam. Terme de tendresse
qui designe aussi la £rand'maman ou la nourrice. Se retrouve dans
gr. ndqqio, (xcc^iat); y,ap,|ictKu 9 o<;, p,a(xp,av ouxelv, ^ap,p,o0pe7txoS; et CGL V
115,10 mamme (= pioquxrj?): nona, i.-e. auia.
L'irlaadais a nam "maman" et muimme "mere nourriciere", 1 'alba-
nais meme "mere". A cote, il y a un type a voyelle longue; bulg. et
russe mdma, pol. mama, lit. moma. "maman" et v.h.a. muoma "tante mater-
nelle". Sur le groupe de v.h.a.amma, v. lat.amma (avec 1 1 observation
generale) et amita. Le sens et la forme des mots de ce genre sont
instables.
Diminutif mamilla: mamelle, tette; robinet (Varr., R. R. 3,14, 3 ) •
Usite de tout temps. Les 1 . romanes ont garde mamma au sens de "mamam",
reservant le sens de "sein, mamelle" a mamilla, M.L.5377 et 5376;
cf. aussi ags. mamme; iri. mamn.
Derives et composes: i° de mamma: - 5 s: donner (ou prendre) le
==== search materies block
33861:a materies "bois de construction", cf. Plin.10,306, cornus non potest
33862:uideri materies propter exilitatem, sed lignum, et Dig.33,1,53. De
36740:corpore, ou il designe la branche mere, le troirc principal; materies .
36826:non potest uideri materies propter exilitatem, sed lignum. C'est a
36832:materies, -ria, -rium, 5407 *mSteriamen ( fr. merrain), 5408 *mdteria-
36834:Dans la 1 .commune, materies s'est dit ensuite de toute espece de
36846:De meme que mdter designe la nourrice, materies a quelquefois le
```


## [2026-09-07T01:47:18.148Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '36700,36760p' LAT.txt\necho \"########\"\nsed -n '36820,36855p' LAT.txt"
}
```


### [2026-09-07T01:47:18.213Z] TOOL RESULT

```
ploi du mot inclinent a penser que c'est une tranacription du grec
p,aa(CT)aop,at,, plutot qu'un denominatif de mansus, prononce *ut asus,
comme l'a suppos^ Cavallin, Philol.91 (1936), p.467. la graphie mans 5
de Non.148,10 pourrait avoir ete influencee par mansus. Cf. le suivant.
Certainea formea romanes suppoaent submassQre , M.l.8379.
mastico, -as: = p,aortx i ^ w (Pelag., Apul.). Le verbe a ete rang<S na-
turellement dans lea formations, de type populaire, en -ic 5 , cf.
morsico, et eat demeur^ dans lea 1 . romanes, M.L.5398. D'oit: masticatio ;
immasticatus (Cael. Aur.); praemastico.
mastic(h)e, -es; mastix (- tex), -icis f.: formea tardives latiniaeea
de gr. p,acTT!/XH "mastic", et demeurees dans lea 1 . romanes, M.L.5399.
mastigo, -as: fouetter (ital.). Denominatif de mastix = gr.pAOTi.^,
cf. mastigia (Pl.) = [lacmyCac;.
mastruca, -ae f.: vetement de peau. Le mot et la chose sont venus
de Sardaigne a Rome (cf. Quint.1,S,8): 1 'origine en est probablement
phenicienne. On trouve aussi lea graphiea mastruga, manstruca, manstructa
(Pl. Poe.1313 ), manstruga. Derive: mastrucatus.
masturbor, -aris (et mas turbo): cf. CGL II 1*7,44 mas turbat: ma-
nuturbat, Secpei, xai Secpexou. "Eaxt-v Se prjiia xtnvov. Mot vulgaire
(Martial). M.L.5400. Peut-etre deformation de nacrxpOTteuco? Derivas:
masturbator-, masturbio f. (Mart.).
masucius, -I m.: v. mando.
matara, -ae {mataris,-is, materis) f.: javeline gauloise. Mot
celtique (Sisenna, sar). M.L.540*.
mataxa (met-),-ae f.: fil, cordon. D 4 rive: metaxarius. De gr.
p,exa^a; depuia Lucii. Panroman, aauf roumain. M.L.5403.
matella: v. matula.- Gya -
mater
mateola, -ae f.: baton, manche de la houe? Mot de Caton, Agr.
45,3, cum taleam demittes, pede taleam opprimito. Si parum descendet,
malleo aut mateola adigito. - Technique et rare. M.L,5435a matteola
et 54«5 *mattea ?
On rapproche v.sl .motyka "houe", skr .matydm "herse", etc. S'il
y a un original commun, il est risque de le restituer.
mSter, -trls f.: mere. Correspond a pater. Terne general, qui
peut ae dire dea animaux (A 1 'encontre de genetrix et mamma), cf.Varr.,
R.R. 3 , 4 , porci cum matribus (sena conserve dans beaucoup de formes
dialectales romanes, cf. M.L., s„u. ), meme dea plantes, cf. Vg., G. 3 ,33,
hic plantas tenero abscindens de corpore matrum', Plih. 13,33, superiores
eiusdem rami in excelsum enicant, siluosa multitudine, uasto matris
corpore, ou il designe la branche mere, le troirc principal; materies .
Par image, mater a pu s'employer au sena de "can.se, origine, source",
etc.; cf. n,T]Tpo7i;oXi, £. — Mater designant la mere qui nourrit 1 'enfant,
le mot peut aervir a nommer ausai la nourrice. Il comporte, comme
pater, une idee de reapect, et a'ajoute au nom d'une deesse, comme
pater au nom d'un dieu, pour 1 'honorer sana que 1 'idee de maternite
soit necessairement impliquee dans 1 'appellation: Vesta mater. Mater
est souvent accompagne du gen. familiae (-lias): sur le modele de pater
familias, cf. P.F.113,37, et May-Becker, Prdcis p.38, "Le titre de
mSter familias dont elle [la femme] est honoree a eu des significations
diverses, mais il n'a jamais implique, comme celui de pater familias,
1 'idee de la puissance exercee sur d'autres". De meme matrimonium
"maternite legale, mariage" et a 1'epoque imperiale "femmes mariees,
epouses" (au pl.collectif matrimonia, comme seruitia, e.g. Tac.A.
3,13, fin) est forme d'apres patrimOnium et n'implique jamaia l'id 4 e
de propriet^, ni de droit sur les choses. Enfin 1 'absence d'un adj.
*matrius correspondant a patrius 8'explique par 1'impossibilite pour
la femme, dans 1'ancien droit patriarcal, de posseder et de tester.
* L'adjectif de mater eat' maternus, forme avec le suffixe -no- marquant
1 'origine, cf. acernus, eburnus, etc. Usite de tout temps. Panroman,
sauf roumain, M.L.540G; cf. 5410 *materndlis, 5411 *maternio, 5430
########
1 'arbre par opposition a 1 'ecorce ou aux feuilles, cf. Coi.5,11,4,
(arbor) inter corticem et materiem', 4,31,3, uitis in materiem fron¬
demque effunditur. Comme c'est cette partie de 1 'arbre qui fournit
le bois de charpente, mdteries en est ainsi arrive a prendre, dans
la langue des charpentiers, le sens de "bois", et specialement de
"bois de construction" par opposition a lignum, cf. Plin.16,306, cornus
non potest uideri materies propter exilitatem, sed lignum. C'est a
ce sens que se rapportent les derives:
materiarius "relatif a la charpente", materio,-as "munir d'une
charpente", materior "se procurer du bois" (joint k frumentor, C 4 s.
B.G.7,73), m dteridtus, mdteridtib, materiatura, materiola, mSterlnus,
etc., et les formes supposees par les derives romans, cf. M.L.5409
materies, -ria, -rium, 5407 *mSteriamen ( fr. merrain), 5408 *mdteria-
mentum.
Dans la 1 .commune, materies s'est dit ensuite de toute espece de
mat^riaux: uXr) ^oXojv r) ctXXcov Ttvaiv; materiam superabat opus dit Ov.
M. 3 ,s; et il a servi a rendre le gr. uXt| dans son sens figure de "ma¬
tiore, cause, sujet, origine": materiam artis eam dicimus in qua
omnis ars et facultas, quae conficitur ex arte, uersatur, Cic.Inu.
qui nourrit; arbre ^ui produit des rejetons, tronc
.Aug.94,11; cf. gr. n,T]Tpcc), et par suite "matricule,
:f. mdtTicula); 3 ° matrice (= gr. niytpoc, sens non attestg6»5 -
maturus
ijS» 1 ?» MateriSs a fini par designer la "matiore" par opposition A
1'esprit, dans la 1. philosophique et religieuse: de la, a basse epoque,
mdteridlis, -liter, et immaterialis.
De meme que mdter designe la nourrice, materies a quelquefois le
sens de "aliment"; ainsi Celse 8,i0,39sqq., imbecillissimam materiam
esse omnem caulem oleris. - Ancien (Cat., P1.), usuel.
matertera: v. mater.
matla: mot de glossaire; — intestina (.-nae), unde matiarii dicuntur
qui eadem tractant aut uendunt, CGL V 329,7. On a aussi mattia; mat<t)iola,
Ttepiqopa (in capite de escis). Conserve dans quelques dialectes romans,
M.L.5418. Peut-etre identique a mattea "friandise", di^ja signale par
Varr., L.L.5,188, emprunte au gr. p.axTUTi, matteola Arn.7,831. Pour
matiSrius , v. macellum.
```


## [2026-09-07T01:47:30.300Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"== HUB 956\"\ngrep -n -o \"956\\..\\{0,400\\}\" HUB.txt | head -5\necho \"== HUB madar\"\ngrep -n -o \".\\{0,100\\}m[aä]dar.\\{0,250\\}\" HUB.txt | head -8\necho \"== ARY latin index mater\"\ngrep -n -i \"mater\\|MADAR\" incoming/ARY/ARY_latin_index_pages.txt | head -10"
}
```


### [2026-09-07T01:47:33.513Z] TOOL RESULT

```
== HUB 956
6892:956.
== HUB madar
ugrep: error: error at position 96
?:[^\n\x80-\xbf][\x80-\xbf]*){0,250}
       exceeds complexity limits___/


== ARY latin index mater
941:J Mater Thay Bae pls (ARES) cysts esl oy co lie y oblast
13276:MACER -(TOKHARIAN B) B 5 MADAR, MAD PAHLAVI) 5 shy
13283:MAT’ s(RUSSIAN) (gy 5 MATER HLATIN) 3
13388:Ggghs ages ya oT ghb ele ab Gp MATER) "al guts iy OT stats gis St st
13569:BARNHART: MATERIA, MATER = (LATIN) 73
13570:(MATTER) 642,(MATERIAL) 640 MATIETRE (FRENCH) Wil 3
13571:‘MACKENZIE: (MATTER) 123 MATERIA (SPANISH) glib
13572:AMINDAROV: (CAPITAL) 196} * MATERIA H(TALIAN) .g\3t!
13573:Vary MAFF seb aly MATERIA —-:(PORTUGUESE) J
13574:V4APY ge eFA dares a6 Cit MATERIE = (¢3Y 5!)(GERMAN) git
```


## [2026-09-07T01:47:40.758Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR<=13600 && /\\[pdf page/ {p=$0; n=NR} END{}' incoming/ARY/ARY_latin_index_pages.txt >/dev/null\npython3 - <<'EOF'\nimport re\nlines=open('incoming/ARY/ARY_latin_index_pages.txt',encoding='utf-8',errors='replace').read().split('\\n')\ncur=None\nfor i,l in enumerate(lines,1):\n    m=re.match(r'\\[pdf page (\\d+)\\]', l.strip())\n    if m: cur=int(m.group(1))\n    if i in (13276,13283,13388,13569,13574):\n        print(i,'pdf page',cur,'|',l[:160])\nEOF"
}
```


### [2026-09-07T01:47:42.083Z] TOOL RESULT

```
13276 pdf page 455 | MACER -(TOKHARIAN B) B 5 MADAR, MAD PAHLAVI) 5 shy
13283 pdf page 456 | MAT’ s(RUSSIAN) (gy 5 MATER HLATIN) 3
13388 pdf page 459 | Ggghs ages ya oT ghb ele ab Gp MATER) "al guts iy OT stats gis St st
13569 pdf page 465 | BARNHART: MATERIA, MATER = (LATIN) 73
13574 pdf page 465 | V4APY ge eFA dares a6 Cit MATERIE = (¢3Y 5!)(GERMAN) git
```


## [2026-09-07T01:47:49.360Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nlines=open('incoming/ARY/ARY_pages.txt',encoding='utf-8',errors='replace').read().split('\\n')\ncur=None\nhits=[]\nfor i,l in enumerate(lines,1):\n    m=re.match(r'\\[pdf page (\\d+)\\]', l.strip())\n    if m: cur=int(m.group(1))\n    if 'MATER' in l or 'مادر' in l:\n        hits.append((cur,i,l.strip()[:170]))\nfor h in hits[:30]: print(h)\nEOF"
}
```


### [2026-09-07T01:47:50.687Z] TOOL RESULT

```
(6, 107, 'پوست هستند ولی زبان مادری بیشتر آنها یک زبان هند و اروپایی (یعنی اسپانیایی) است. :')
(12, 302, 'همریشه» همگی دارای بک معنی نیستند. واژه\u200cهای معدودی مانند «مادر» و دماه» و «گاو» در همه')
(16, 412, '۸ کهن مادر,زبانهای |سپانیایی و ایتالیایی و پرتغالی و غیره هم هست. بدین روش کم کم بیشتر زبانهای')
(36, 1000, 'خانوادگی آنها بر پایه\u200cی خانواده (پدر و مادر و فرزندان)» خانواده\u200cی گسترده (پدر بزرگ\u200cها و دایی\u200cها')
(38, 1053, 'فرزندان و دوردازی دشمنان و پیماری\u200cها هم بود. نیمه خدایی بودن شاه (معمولاً با مادرش الهه بود یا')
(45, 1274, '«مادر) یا «گاوه با «بوغ) معنی واژه\u200cهای همریشه در زیانهای هند و اروپایی امروزی کاملدً یکی و')
(129, 3778, '۱ چم این وازه در لیتوانی: ولد» پدر پا مادر.')
(158, 4628, 'پدر و مادر پدران (به چم / ۱۵۹')
(459, 13651, '۱ این واژه\u200cی کودکانه تقریاً در تمام زبان\u200cهای هند و اروپایی وجود دارد و رابطه\u200cی آن پا آمادر" و پستان "تیه"')
(459, 13652, 'آشکار است ولی واجریشه\u200cی آن با واجریشه\u200cی "مادر" (۸) فرق دارد. علت نایابی آن در متون زبان\u200cهای')
(459, 13655, '۳ ضمناً واژه\u200cی 7 در لاتین به چم "مادر بزرگ" بکار رفته.')
(465, 13845, 'واژه\u200cها (و واژه\u200cهای مشابه در دیگر زبان\u200cهای هند و اروپایی) همه از واجریشه\u200cی "مادر" (۸137870 ,۸173 آمدهاند')
(477, 14192, '۱ بازگشت به: مادر,')
```


## [2026-09-07T01:48:01.387Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nd=open('incoming/ARY/ARY_pages.txt',encoding='utf-8',errors='replace').read()\nparts=re.split(r'\\[pdf page (\\d+)\\]', d)\npg={}\nfor i in range(1,len(parts),2): pg[int(parts[i])]=parts[i+1]\nfor n in (459,465):\n    print('##### ARY pdf',n,'printed',n+1)\n    print(pg[n][:2000])\nEOF"
}
```


### [2026-09-07T01:48:03.772Z] TOOL RESULT

```
##### ARY pdf 459 printed 460

۰ | مان (به چم *خان* و "خانه" مثلاً در "خان‌ومان», يا «خانمان»)

۸۸ کورن والی (1ل007/15): 3
لهستانی (۳0/./317): ۸۸ آلبانی (الفاقام: هید ,شرجمید
روسی (0لفا59لا): ۸ هتیت ۱ با خلااقهل<
چک (2800): ۱۷۸3/2۸ بفاها( ای
اسلوا کی (81-07/۸0): ۸۸۸ پسگشت‌ها 5
لیتوانی لالم ۳

ق۱۸۸۵ ,9۶۸ 7 0۸۸3131۸ دی ما
لتونی (لتی) (۸771۸00ل): ۵/۸ 7 (۸31۸ا) نما مره
.ایرلندی کهن (7اکلقا صا0): 9 (متختهمی) :00/5
0 مفاق۸۸ 8 (۸1۸(131۸) درا اده نج
ولزی (7ل8.5): ۸ ۸ :0ب مهار
برتونی (8670/7): انا برهان قاطع : 1۹۳۸
یادداشت.
۱ این واژه‌ی کودکانه تقریاً در تمام زبان‌های هند و اروپایی وجود دارد و رابطه‌ی آن پا آمادر" و پستان "تیه"
آشکار است ولی واجریشه‌ی آن با واجریشه‌ی "مادر" (۸) فرق دارد. علت نایابی آن در متون زبان‌های
کهن شاید این باشد که این واژه بچه گانه است.
۳ چم این واژه در افغانی و آلمانی کهن: خاله» عمه,
۳ ضمناً واژه‌ی 7 در لاتین به چم "مادر بزرگ" بکار رفته.
ارستایی (/47857۸): 3۵91۸0۸ ,۴۸۸120۸ آرمنی (47۸4221400):
پارسی باستان((۳878/4 072). 1۸3۷1۷۸ (1۸-83) ,اب1۸
پهلری (۲1هالنهه): برنانی (0680): 001۸ ,001408
0 ,31۸018139 راتقاز لاتین (7100ا): 0 ,0015
کردی (80[157ن0). ت2۸ فرانسه (7ل۳۳5۸): 0
تخاری ۸ (۸ ۷(فلق70721۸): 74 ات7۸ اسپانیایی (5۳۸۸/[5[7): 2000
تخاری 8 (8 /(ل7077۸7): پرتغالی (۳071701838): 2000
-لل782 ملق +/(18 ایسلندی کهن (7۸0 یه )+
سانسکریت (54(/97/7): 20 738
02۸8 بتتات نهد ,رق۸ادتنجوم) ساکسونی کهن (240077 02م: ۳۸/8۸۸

##### ARY pdf 465 printed 466

۶ ال
پسگشت‌ها 5 8 (۸115016) ۱۳/0/5
زان 000010 بر رها 1 (5 0۸083 34
7 هت‌وناین 7 فرهنگ ممینارایلا بر ۶۳۷۴۴ ۳۷۴۵
135 :۸6 ما0 : و ت
یادداشت: 5
۱ بازگشت به: موش.
۲ چم این واژه در سانسکریت: خایه,
۳ واجریشه‌ی شناسان معتقدند که واژه‌ی "مایچه" (که شاید در اصله آمرشچه" رده است) با واژه‌ی "موش" خوبشی
دار د و بهمین دلیل واژه‌ی ماهیچه در لاتین (18ن1ت۸108601) مصفر واژه‌ی 11118 به معنی "موش * است. دلیل این
خویشی» شباهت شکسل ساهیچه‌ی دوسر و "موش" است. فمن در زبان‌های ارمنی و یوتانی واژه‌های
و18 ۸5(با ۸1385) دو چم دارند: مرش و عضله.
۴ واژه‌های ژرمنی این فهرست همه از لاتین مشتق شده‌اند.
پهلوی (4ال2۸): 81۸7۸۲ ,۸127015717 8ب ۱۱۳۹
کر دی (ل68۵15): 55331۸18 ,2/۸5
سانسکریت (7ل8۸4(80): ۸ پسگشت‌ها 5
یرنانی 0580): 3 700 مهو
لاتین (47100): 16۵78 بف1137893 اک این انا
فرانسه (۳2۸۴(4): اب ۱۷۳۱۱ 40 (تفت23 ان هه ره رین
اسپانیایی (5۸(18[7): با 3 (01۸1788) تمد هم
ایتالیایی (/(۵لل): ۱۸788۸ ۰ | 196 جتفتاهی) ۸
پرتغالی (۳07001895), ۸7۸۸ برهان قاطع + ۴ و ۱۹۳۴
آلمانی (//087/44)(از لاتین) ‏ 11۸۲882 لغت نامه دهخدا: ۱
انگلیسی (6۸/01/5):(از فرانسه‌ی کهن) فرهنگ معین : ۶و ۳۶۴۸
یادداشت:
برخی از واجریشه شناسان معتقدند که واژه‌ی فارسی "مایه" با واژه‌ی لاتین 31۸781۸ خریشی دارد و هر دوی این
واژه‌ها (و واژه‌های مشابه در دیگر زبان‌های هند و اروپایی) همه از واجریشه‌ی "مادر" (۸137870 ,۸173 آمدهاند
ضننا واژه‌ی آماده" هم از همین واجريشه است. شاید واژه‌ی عربی ماد" هم اصلاً از یک زبان هند و اروپایی اخذ
```


## [2026-09-07T01:48:12.767Z] TOOL CALL #71: Bash

```json
{
 "command": "sed -n '1,140p' tools/verify_check.py"
}
```


### [2026-09-07T01:48:12.803Z] TOOL RESULT

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


## [2026-09-07T01:48:46.298Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -o \"hamātā.\\{0,200\\}\" KNT.txt | head -5\ngrep -n -o \"m[āa]t[āa]-\\?.\\{0,160\\}\" KNT.txt | grep -i \"mother\" | head -5\ngrep -n -i \"mother\" KNT.txt | head -8"
}
```


### [2026-09-07T01:48:47.567Z] TOOL RESULT

```
1918:matar- ‘having the same mother’; tigra- zauda- "wearing pointed caps’; wéd-marsiyu-
1600:$129, Hapiotogy is the loss of one of two similar sequences of sounds, each containing at least one consonant and one vowel, or one vowel and at least one consonant: thus English min- eralogy from *mineralology. OP has one certain example, hamátü from *hama-māiā ‘having the same mother’, cf. hama-pilà ‘having the same father’, where no haplology is possible. A second example, probable but less certain, is duvarfim from *dvar-varðim ‘door-cover’, = ‘colonnade’. Possibly also arštā- ‘rectitude’ from *arSta-td-, but cf. Lex. s.v.; and didiy ‘see thou’, if redupli- cated pres. imv. *dht-dhi-dht rather than aor. шту. *dhi-dhi.
1918:all lands’; hama-pitar- ‘having the same father’; ha-matar- ‘having the same mother’; tigra- zauda- "wearing pointed caps’; wéd-marsiyu-
2209:OP nom. mätä ‘mother’ in hamaté ‘having the 4
2210:same mother’, Skt: mata, Gk. (Dor.) ратар, Lt. mater. OP nom. brátà ‘brother’, Skt. bhraid, Gk. ¢parno ‘clan-brother’, Lt. frater! OP gen. pica’, Gk. татр, Lt. patris, from *potr-os or -es, unlike Skt. pitis from *potrs.
2699:J. With the idea of hama- ike’ in compounds: DB 1.30 Лата hamapilà Kabūjiyahyā ‘having the same mother and father as Cambyses’; the position of the genitive after the adjectives sug- gests that this is a dative use rather than a true genitive use (cf. §309)?
3568:610. 1.26-35. Saith Darius the King: This is what was done by me after that I became king. A son of Cyrus, Cambyses by name, of our family— he was king here. Of that Cambyses there was a brother, Smerdis by name, having the same mother and the same father as Cambyses. After- wards, Cambyses slew that Smerdis. When Cambyses slew Smerdis, it did not becomeknown to the people that Smerdis had been slain. After- wards, Cambyses went to Egypt. When Cambyses. had gone off to Egypt, after that the people be- came evil. After that the Lie waxed great in the country, both in Persia and in Media and in the other provinces,
5759:madtar- sb. ‘mother’: Av. matar-, Skt. matdr-, Gk. Dor. ратар, Lt. mäter, pIE nom. *maté, stem *máler- ($154.П): in hamdtar-.
```


## [2026-09-07T01:49:01.197Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '6885,6900p' HUB.txt\necho \"=== HUB 'Mutter'\"\ngrep -n -o \".\\{0,80\\}Mutter.\\{0,160\\}\" HUB.txt | head -8"
}
```


### [2026-09-07T01:49:04.183Z] TOOL RESULT

```
mddavar = phi. mdtakvar 'special, principal, essential'
Shk. 257, Min; Gl. 137; Marbaigan u.' s. w., siehe § 87.
Ueber den Wechsel von y und d siehe § 94.
§ 89. Nach § 84, b ist ap. rt im Phi. als rt geblieben,
im Paz. und Np. zu rd geworden. Diese Kegel ist durch
eine so grosse Ajizahl von Beispielen sicher gestellt, dass
^) Dieser Uebergang ist sonst dialektisch bezeugt, ygl. Horn
Nr. 956.
*) Vgl. wegen r aus t jiid. tat. moiru *Stute' aiis *moryun = np.
madiydn *Stute* aus *mat%kdn.— 195 -
die scheinbaren Ausnahmen von derselben ihren besonderen
Grund haben mtissen. Scheinbar ist namlich ap. rt in einigen
Fallen im Persischen in Ar, hi iibergegangen ; so in:
phi. ahlav (oder ahrav) *fromm' H. p. 264 = zd. asa-
van-, ap. *artavan'\ aber phi. ahlav ist specifisch parsisch
und ap. arta- im Np. regelrecht durch ard- vertreten (vgl.
=== HUB 'Mutter'
ugrep: error: error at position 83
bf][\x80-\xbf]*){0,160}
                       \___exceeds complexity limits
```


## [2026-09-07T01:49:13.936Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"§ 94\" HUB.txt | head\necho \"---\"\nawk 'NR>=7290 && NR<=7360' HUB.txt | grep -n -i \"may\\|mat\\|mad\" | head -20\necho \"--- find mayag\"\ngrep -n \"m[aä]yag\\|m[aä]jag\\|mayah\\|m[aä]tak\" HUB.txt | head -20"
}
```


### [2026-09-07T01:49:15.195Z] TOOL RESULT

```
6887:Ueber den Wechsel von y und d siehe § 94.
7169:§ 94. Ap. d vor y, m, n ist geschwunden: may ein
7822:') Durch EinfluBs der andern Participia auf -ta, ygl. § 94.— 220 -
9241:siehe oben p. 101 und § 94.
9468:(afgh.) Hilmand, s. § 94 und 88. Mehrfach findet sich / in
9985:§ 94. ap. d gesohwunden 202—203
---
--- find mayag
6884:— phi. mdtak 'essential', madagi = phi. matakik particular,
8722:Paz. und Np. (vgl. paz. madavar = phi. matakvar Shk. 257 ;
```


## [2026-09-07T01:49:17.943Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '6870,6890p' HUB.txt"
}
```


### [2026-09-07T01:49:17.989Z] TOOL RESULT

```
*Fisch\ phi. mOhik = zd. masya-, skr. matsya-.
Urspr. tt war. schon iran. zu si geworden : mast 'trunken
= skr. matia- u. s. w., vgl. § 109, d. Vor andern Konso-
nanten als t war t schon im Iranischen zu d^ geworden,
siehe § 95. — Idg. kH^ kH, pt, st = iran. st, xt, ft^ st
= np. st, xty.ft. st siehe §'83, b sowie Kap. 14, 19, 23, 26.
Der llebergang von t zu 7 (vgl. Hilmand = zd. haeftimant-)
ist afghanisch.
Der Auf klarung bedarf nbch der wirkliche oder schein-
bare Uebergang ^) von intervokalischem t (das zu d werden
miisste) in y: pdytz — pdyez 'Herbst* = paz. padez Min.
61. 159, jud. tat. poriz^), phi. patez oder patec? (siehe oben
p. 37); maya *StoflF, Substanz, Summe, Kapital', arab. mad-
dat 'Stoflf, Materie' (afgh. LW. mada *a matter), paz. madag
— phi. mdtak 'essential', madagi = phi. matakik particular,
mddavar = phi. mdtakvar 'special, principal, essential'
Shk. 257, Min; Gl. 137; Marbaigan u.' s. w., siehe § 87.
Ueber den Wechsel von y und d siehe § 94.
§ 89. Nach § 84, b ist ap. rt im Phi. als rt geblieben,
im Paz. und Np. zu rd geworden. Diese Kegel ist durch
eine so grosse Ajizahl von Beispielen sicher gestellt, dass
```


## [2026-09-07T01:57:03.900Z] TOOL CALL #76: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/mk316.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW_PIE = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/m%C3%A9h%E2%82%82t%C4%93r\"\nW_MADAR = \"https://en.wiktionary.org/wiki/%D9%85%D8%A7%D8%AF%D8%B1\"\nW_MADE = \"https://en.wiktionary.org/wiki/%D9%85%D8%A7%D8%AF%D9%87\"\nW_MAYE = \"https://en.wiktionary.org/wiki/%D9%85%D8%A7%DB%8C%D9%87\"\nW_MAMAN = \"https://en.wiktionary.org/wiki/%D9%85%D8%A7%D9%85%D8%A7%D9%86\"\nW_AVMATAR = \"https://en.wiktionary.org/wiki/%F0%90%AC%A8%F0%90%AC%81%F0%90%AC%99%F0%90%AC%80%F0%90%AC%AD\"\nE_MOTHER = \"https://www.etymonline.com/word/mother\"\nE_MATERIAL = \"https://www.etymonline.com/word/material\"\nE_METROPOLIS = \"https://www.etymonline.com/word/metropolis\"\nE_MAMMAL = \"https://www.etymonline.com/word/mammal\"\n\nroot_refcheck = [\n {\"ref\": \"POK:694\", \"status\": \"partial\",\n  \"note\": \"Pokorny 694 is 'mā-3, Meaning: mother (expr. root), Note: redupl. māmā, māmmā ... Material: Old Indic mā ‘mother’ ... npers. mām, māmā, māmī ‘mother’ ... Latin mamma ... mamilla ‘nipple’ ... Page(s): 694' (POK_full.txt l.57758ff, grep 'lemma: mah 3'). It therefore supports the Mā- half of the root box, but glosses it ‘mother’, not ‘breast’; Pokorny's separate lemma 'mahter-, Meaning: mother, Note: based on a babble-word mah-, see there ... Page(s): 700-701' is where Mā-ter belongs, i.e. p.700-701 and not 694.\"},\n {\"ref\": \"PRT:386,863\", \"status\": \"not_checked\",\n  \"note\": \"Partridge, Origins (1958) — no open copy: all 8 archive.org copies are lending-only per data/verification/sources/refs_online.json (kind 'archive_restricted'), and there is no local OCR.\"},\n {\"ref\": \"SYN:103\", \"status\": \"supports\",\n  \"note\": \"Buck 2.36 on printed p.103 (SYN.txt l.2813): ‘2.36. ‘Mother’. 1. IE *māter-, prob. ... starting fr. a nursery word of the ma type. Walde-P. 2.229. Here belong the Grk., Lat., Ir., Gme. ... and Indo-Iranian forms’ and ‘2. Nursery words that have become the usual terms. Type mama (above, p. 94, Walde-P. 2.221) in It. mamma ... and W., Br. mam.’ Nourai's own remark (‘probably started as a nursery word and became a usual term’) is a paraphrase of exactly these two headings.\"},\n]\n\nroot_consulted = [\n {\"src\": \"WLD\", \"where\": \"Bd. II 221 (§3 mā) and Bd. II 229 (matēr-)\", \"stance\": \"supports\",\n  \"note\": \"WLD_Bd2_pages.txt leaf 225 (printed 221): ‘3. mā Lallwort für ‚Mutter‘, redupl. mama, mammā ... Obwohl das unred. mā die Grundlage von māter- (s. d.) ist ... Ai. mā ‚Mutter‘; np. mām, māmā, māmī ‚Mutter‘’; leaf 233 (printed 229): ‘matēr- ‚Mutter‘, beruht auf dem Lallwort mā-, s. d. ... Ai. mātār-, av. mātar-, arm. mair ... gr. mētēr, dor. mātēr ... lat. mater, -tris’. Both halves of Nourai's root box are thus real and correctly linked.\"},\n {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. māter-\", \"stance\": \"partial\",\n  \"note\": \"AHD_watkins1985.txt l.730: ‘māter-. Mother. Based ultimately on the baby-talk form ma-2, with the kinship term suffix -ter-. 1. Germanic *mōthar- ... 2. Latin māter ... 3. Greek mētēr ... 4. Latin māteriēs, materia, tree trunk (< “matrix,” the tree’s source of growth) ... [Pok. māter- 700.]’ Supports the structure of the whole chart but calls -ter- the KINSHIP suffix, not an agent suffix, so Nourai's gloss ‘feeder (of the family)’ is his own.\"},\n {\"src\": \"IEC\", \"where\": \"Mann, pp. 735–736 s.v. mātēr (1) and māter- (2)\", \"stance\": \"partial\",\n  \"note\": \"IEC.txt l.10369: ‘mātēr (māter-, mātr) (1) ‘mother’ ... WP II, 229 Skt. mātā; ... Per. mādar; Oss. mad, madä; Tokh. mācar ... Gk. métēr ... Lat. mater’, but Mann sets up a SEPARATE root ‘māter- (2) ‘wood, timber, substance’ ... Lat. materies ... materia’, i.e. he does not put Latin materia under ‘mother’ as Nourai (and Watkins) do.\"},\n]\n\nn1 = {\n \"id\": 1, \"lang\": \"Avestan\", \"words\": \"mâtar\", \"verdict\": \"confirmed\",\n \"derivation\": \"Avestan mātar- f. ‘mother’ is the regular Iranian reflex of PIE *méh₂tēr (nom. *mātē, stem *māter-) via Proto-Iranian *máHtā: the PIE laryngeal *h₂ is lost with lengthening of the vowel, and *-ter- is retained. It is attested in the Younger Avesta (V. 12.1 yaṭ pitā vā mātā vā parəiriθyāiti ‘if father or mother dies’, Yt. 17.16, Y. 38.5 of animal mothers). Old Persian has the same stem, preserved only in the haplologised compound hamātā < *hama-mātā ‘having the same mother’ (Bisitun I 30, of Smerdis and Cambyses). Sanskrit mātár-, Greek Doric mātēr, Latin māter are the exact cognates, so the arrow root → Avestan is correct.\",\n \"derivation_fa\": \"اوستایی mātar- «مادر» بازماندهٔ قاعده‌مند هندواروپایی آغازین *méh₂tēr است که از راه ایرانی باستان *máHtā به اوستا رسیده؛ حنجرهٔ هندواروپایی افتاده و در عوض واکه کشیده شده است. این واژه در اوستای نو (وندیداد ۱۲،۱) گواهی دارد و در پارسی باستان تنها در ترکیب hamātā «همان مادری» (سنگ‌نوشتهٔ بیستون) مانده است. بارتولومه (فرهنگ ایرانی باستان، ستون ۱۱۶۷) و کنت همین را می‌گویند؛ پس این پیوند در نمودار نورایی درست است.\",\n \"sources\": [W_AVMATAR, W_PIE],\n \"ref_check\": [\n   {\"ref\": \"POK:694\", \"status\": \"partial\", \"note\": \"Pokorny p.694 (mā-3) does NOT list Avestan mātar-; the Avestan form stands in the neighbouring lemma 'mahter-' … 'Old Indic matar- ‘mother’, Avestan matar-, Armenian mayr … Page(s): 700-701' (POK_full.txt l.57703ff). So the claim is right but the page number should be 700.\"},\n   {\"ref\": \"SKT:336\", \"status\": \"partial\", \"note\": \"Skeat's entry is real but not on p.336 of the edition on disk: 'Mother (1), a female parent. [M.E.] moder. A.S. mōdor … + Du. moeder, Icel. mōðir … L. mater, Gk. mētēr, Skt. mātā, mātṛ … formed with Aryan suffix -tar (of the agent) from √MĀ, orig. to measure … Orig. sense uncertain, perhaps ‘manager’ of the household' — SKT.txt leaf 318, i.e. printed p. ~298 of the 1911 impression (leaf = printed+20); leaf 356 = p.336 is the 'Parity–Parsee' page. Content supports Av./Skt. mātar- as source of ‘mother’, but Skeat's own etymology is √MĀ ‘to measure’, i.e. ‘manager’, not Nourai's ‘feeder’.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"col. ~1167 (leaf with column header 1166)\", \"stance\": \"supports\",\n    \"note\": \"BRT.txt l.20293ff: '²mātar- f. ‘Mutter’: yaṭ pitā … ⁰tā vā parəiriθyāiti … V. 12.1 … KompE. — ai. mātár- f., np. mādar. — Pü.: mātar'. Bartholomae himself links Avestan mātar- with Pahlavi mātar and NP mādar, exactly Nourai's chain #1→#2→#3.\"},\n   {\"src\": \"KNT\", \"where\": \"Old Persian Lexicon s.v. mātar-; §129 (haplology)\", \"stance\": \"supports\",\n    \"note\": \"KNT.txt l.5759: 'mātar- sb. ‘mother’: Av. mātar-, Skt. mātár-, Gk. Dor. mātēr, Lt. māter, pIE nom. *mātē, stem *māter- (§154.II): in hamātar-'; l.1600: 'OP has one certain example, hamātā from *hama-mātā ‘having the same mother’'.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. II 229\", \"stance\": \"supports\",\n    \"note\": \"'Ai. mātār- ‚Mutter‘, av. mātar-, arm. mair ds.' (WLD_Bd2_pages.txt leaf 233).\"}\n ]\n}\n\nn2 = {\n \"id\": 2, \"lang\": \"Pahlavi\", \"words\": \"mâtar; matak; mâdiyânag, mâyag\", \"verdict\": \"confirmed\",\n \"derivation\": \"All three Pahlavi items are real and all go back to Av./OIr. mātar-. (a) mātar ‘mother’: MacKenzie has 'mād [AM < A ʾM-Y, v. mādar | M md] mother' and 'mādar [AMYtl; mtl | M mdr, N ~] mother' — the Aramaic heterogram ʾM(Y) masks an inherited word; mād is the nominative-derived short form, mādar the oblique stem mātar-, exactly as Nyberg describes ('māt [mʾT; ʾM] cas. obl. mātar [mʾtl; ʾMY-tl] mother … Common Ir.'). (b) mātak/mādag [NKB; mʾtkʹ] ‘female’ = *māta-ka-, a -ka- derivative of māt(ar) ‘mother’, borrowed into Armenian as matak ‘fēmella’ (Nyberg: 'from māt (q.v.)'). (c) the same -ka- formation in the abstract sense ‘the essential element of anything, its core, essence; materials’ gives Pahlavi mātak / (Manichaean) māyag [my g] with the intervocalic t > y development, whence NP māya; mātag-dān / mātīyān is Nyberg's 'that which contains the kernel, the core, or substance and essence of a thing' — Nourai's 'mādiyānag: essence'. Nourai's spelling matak (short a) for mātak is the book's usual loose transcription, not a different word.\",\n \"derivation_fa\": \"هر سه صورت پهلوی واقعی اند و همه به mātar- ایرانی باستان بازمی‌گردند: ۱) māt / mātar («مادر»؛ مکنزی ص ۵۶ و نیبرگ، با نوشتار هزوارش ʾM/ʾMY-tl)؛ ۲) mātak «ماده، موّنث» که پسوند -ak (ایرانی باستان -ka-) بر ستاک «مادر» افزوده شده و به ارمنی هم وام رفته است (matak)؛ ۳) همین mātak در معنای «جوهر، مادّهٔ اولی»، که با ابدال t میان‌واکه‌ای به y صورت māyag گرفته (در فارسی میانهٔ مانوی my g) و mātag-dān / mātīyān نیبرگ «آن که مغز و جوهر چیزی را دربر دارد» همان «mādiyānag» نورایی است. ادعای نورایی درست است؛ تنها «matak» را باید mātak (با الف کشیده) خواند.\",\n \"sources\": [W_MADE, W_MAYE, W_MADAR],\n \"ref_check\": [\n   {\"ref\": \"BQT:1933\", \"status\": \"supports\",\n    \"note\": \"Nourai's BQT pagination runs two pages behind the Ibn Sina scan on disk (his 1946/1964 = our 1948/1966), so BQT:1933 = the mādar page, our printed 1935 = BQT_v4 pdf page 16. Mo'in's footnote there: 'مادر – بفتح سوم = ماد = مار (ه.م.). پهلوی mātar, mād … حالت فاعلی از -mātar «بارتولمه ۱۱۶۷»، اوستا -mātar، ارمنی mayr، هندی باستان -mātar … افغانی mor، آسی mad…، بلوچی mās…' — i.e. Pahlavi mātar/mād from Avestan mātar-, precisely the arrow drawn.\"},\n   {\"ref\": \"SNS:237\", \"status\": \"partial\",\n    \"note\": \"Tavoosi's Shayast-ne-Shayast glossary entry 1167 is on disk: '1167) matar: MP mātar … mādar, mʾTY-tl … (Wan. III, 57) mʾdr, mʾd … 1168) mādarān, mʾdy-tlʾan' (SNS.txt l.4544). The entry says exactly what the arrow says (Pahlavi mātar with spellings mʾTY-tl, mʾdr, mʾd). The printed page number cannot be confirmed: the OCR of SNS is largely unreadable and refs_online.json records 'page offset not determined'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"p. 56 (leaf 77) s.vv. mād, mādag, mādar, mādayan, mādīyān\", \"stance\": \"supports\",\n    \"note\": \"MacKenzie: 'mād [AM < A ʾM-Y, v. mādar | M md] mother. ¹mādag [NKB < A nqb; mʾtkʹ | (M myg), N māda] female. ~īh: femininity. *mādag [mtkʹ | (M myg, N māya)] essence, substance … mādar [AMYtl < A ʾm-y; mtl | M mdr, N ~] mother … *mādayān [mʾtydʾnʹ] essence, basis, core; essential, chief … mādīyān [mʾtygʾn | N ~] mare.' Every Pahlavi word in the node is there, with the NP outcomes māda / māya / mādar / mādīyān.\"},\n   {\"src\": \"NYB\", \"where\": \"Part II Glossary s.vv. māt/mātar, mātak, mātakik, mātag-dān\", \"stance\": \"supports\",\n    \"note\": \"'māt [mʾTʹ; ʾM] cas. obl. mātar [mʾtl; ʾMY-tl] mother … Common Ir.'; 'matak [NKB; mʾtkʹ] female … Arm. lw. matak; MPrs mʾyg (!) … NP mādah: from māt (q.v.)'; 'mātakik … From mātak “the essential element of anything, its core, essence; materials” … but MPrs myg “substance, nature” … NP māyah. Arab māddat- “matter” is borrowed from mādag, but Arabized through association with madda “to extend”'; 'mātag-dān, mātīyān [mʾtgdʾnʹ] “that which contains the kernel, the core, or substance and essence of a th.” … From mātak + -dān'.\"},\n   {\"src\": \"BRT\", \"where\": \"col. ~1167\", \"stance\": \"supports\", \"note\": \"'Pü.: mātar' appended to the Avestan mātar- entry — Bartholomae's own Pahlavi gloss of the Avestan word.\"}\n ]\n}\n\nn3 = {\n \"id\": 3, \"lang\": \"Persian\", \"words\": \"mâdar «مادر»; mâdeh «ماده»; mâyeh «مایه» (extra: مام ، ماما ، مادگان ، مادیان ، ماکیان)\", \"verdict\": \"confirmed\",\n \"derivation\": \"مادر mādar continues Pahlavi mādar/mātar with the regular NP voicing of intervocalic -t- to -d- (Av. mātar- > MP mātar/mādar > NP mādar; Tajik modar); the by-forms mād and mār are recorded by Horn and Mo'in. ماده māda ‘female’ = MP mātak/mādag < *māta-ka- ‘female (creature)’, with the usual loss of final -k > -a(h); it is NOT the Arabic مادّه mādda ‘matter’, which is a separate homograph (and which Nyberg and Hübschmann think is itself an Arabicised borrowing of Pahlavi mādag re-shaped on the Arabic root m-d-d ‘extend’). مایه māya ‘origin, essence, leaven, capital’ = the same mātak in its abstract sense, through the intervocalic t > y route that Hübschmann sets out (§88: 'māya ‘Stoff, Substanz, Summe, Kapital’ … paz. mādag = phl. mātak ‘essential’'). The extra words follow: مام/ماما are the inherited nursery doublets (Pokorny 694 lists npers. mām, māmā, māmī); مادگان (attested mādagāna in Nezami's Haft Paykar, the quotation in the JSON) and مادیان ‘mare’ < MP mādīyān < *mātikāna-, and ماکیان ‘hen’ < *mādkīyān (Horn no. 956 n.2: 'Wohl *mādkiyān, vergl. kurd. mūk'), all -yān derivatives of mādag ‘female’. The one point on which sources diverge is مایه: Horn, Hübschmann, Nyberg, Mo'in and Aryanpur put it under ‘mother’, while Wiktionary derives the ‘leaven’ sense from Proto-Iranian *(ham)mātaka(naH) ‘(of) the same material, mix’ — still the same *māta- stem, so the arrow stands.\",\n \"derivation_fa\": \"«مادر» دنبالهٔ فارسی میانهٔ mādar/mātar است؛ t میان‌واکه‌ای ایرانی باستان در فارسی میانه و نو به d نرم شده (mātar > mādar؛ تاجکی modar) و صورت‌های کوتاه «ماد» و «مار» را هرن و معین آورده‌اند. «ماده» از mātak/mādag پهلوی (< *māta-ka-) است و ربطی با «مادّه‌»ٔ عربی ندارد — برعکس، نیبرگ و هوبشمان معتقدند همان «مادّه»ٔ عربی معرّب mādag پهلوی است که به ریشهٔ م‌د‌د ملحق شده است. «مایه» همان mātak در معنای جوهر است که با ابدال t میان‌واکه‌ای به y (هوبشمان، پارهٔ ۸۸) به دست آمده؛ معین در حاشیهٔ برهان قاطع نیز همین را از قول هرن می‌آورد. «مام، ماما» واژه‌های کودکانهٔ موروثی اند (پوکورنی ۶۹۴)، و «مادگان، مادیان، ماکیان» مشتقّات -یان از «ماده» اند (هرن، شمارهٔ ۹۵۶ و پانویس ۲: *mādkīyān). در مجموع ادعای نورایی درست است.\",\n \"sources\": [W_MADAR, W_MADE, W_MAYE],\n \"ref_check\": [\n   {\"ref\": \"BQT:1933,1946,1964\", \"status\": \"supports\",\n    \"note\": \"All three land on the right pages once Nourai's two-page offset is applied (his page = our printed page − 2). BQT_v4 pdf 16 (our 1935 = his 1933) = مادر with Mo'in's footnote 'Pahlavi mātar, mād … Avesta -mātar …'; pdf 17 (our 1936) = 'ماده – بفتح دال … پهلوی mātak (موّنث) … رک: مادر'; pdf 29 (our 1948 = his 1946) = ماکیان/مادیان with the footnote 'مادیان (ه.م.) = ماده (ه.م.)'; pdf 47 (our 1966 = his 1964) = مایه with the footnote 'پهلوی māyag (جوهر، مادّهٔ اولی) «تاوادیا ۱۹۳» … هرن گوید: من مستقدم که «مایه» فارسی و māteriēs لاتینی از ریشهٔ -māter (قس: māter «مادر») مشتق باشند'.\"},\n   {\"ref\": \"HRN:213\", \"status\": \"supports\",\n    \"note\": \"Horn no. 956 on printed p.213 (HRN.txt leaf 234) is a word-for-word match for the node: '956. mādar; mād (Patet’s) ‚Mutter‘, māda, mādīna ‚weiblich‘, mādiyān ‚Stute‘, mākiyān ‚Henne‘. ap. *mātar- in hamātā ‚von der gleichen Mutter‘; aw. mātar-; phlv. māt, mātar ‚Mutter‘, mātak ‚weiblich‘, arm. LW. matak ‚Weibchen‘; ai. mātár-; arm. mair', with n.2 'Wohl *mādkiyān, vergl. kurd. mūk'.\"},\n   {\"ref\": \"MON:3716\", \"status\": \"partial\",\n    \"note\": \"Mo'in's 6-volume pagination cannot be mapped online (refs_online.json: 'Page numbers cannot be mapped online'); the entries themselves were read in the 2-vol Adena OCR: 'مادر' and 'مایه' are present with Pahlavi tags, and the مادر/مایه etymologies Mo'in prints in Borhan-e Qate' (see BQT above) are his own footnotes. Content supports; page unverifiable.\"},\n   {\"ref\": \"SNS:237\", \"status\": \"partial\",\n    \"note\": \"Glossary entry 1167 gives 'mādar' beside Pahlavi mātar (SNS.txt l.4544) — supports the NP outcome; printed page not verifiable (see node #2).\"}\n ],\n \"consulted\": [\n   {\"src\": \"HUB\", \"where\": \"§88, printed pp. 194–195\", \"stance\": \"supports\",\n    \"note\": \"Hübschmann on the intervocalic t > y development: 'māya ‚Stoff, Substanz, Summe, Kapital‘, arab. maddat ‚Stoff, Materie‘ (afgh. LW. māda ‚a matter‘), paz. mādag = phl. mātak ‚essential‘, mādagī = phl. mātakik ‚particular‘, mādavar = phl. mātakvar ‚special, principal, essential‘'; footnote: 'Vgl. wegen r aus t jüd.-tat. moiru ‚Stute‘ aus *moryun = np. mādiyān ‚Stute‘ aus *mātikān' (HUB.txt ll.6880–6893).\"},\n   {\"src\": \"ARY\", \"where\": \"printed pp. 460 and 466\", \"stance\": \"supports\",\n    \"note\": \"Aryanpur under مایه (printed 466): 'برخی از واجریشه‌شناسان معتقدند که واژهٔ فارسی «مایه» با واژهٔ لاتین MATERIA خویشی دارد و هر دوی این واژه‌ها … همه از واجریشهٔ «مادر» (MĀ, MĀTER-) آمده‌اند؛ ضمناً واژهٔ «ماده» هم از همین واجریشه است' (ARY_pages.txt pdf 465); under مام/ماما (printed 460) he lists Av. MĀTAR / Pahlavi forms but warns 'واجریشهٔ آن با واجریشهٔ “مادر” (MĀ) فرق دارد'.\"},\n   {\"src\": \"MON\", \"where\": \"Farhang-e Farsi (2-vol Adena OCR) s.vv. مادر, مایه\", \"stance\": \"supports\",\n    \"note\": \"Mo'in's lexicon has both headwords with Pahlavi origin tags; his etymological notes on مادر/ماده/مایه are the Borhan-e Qate' footnotes quoted above.\"},\n   {\"src\": \"PHD\", \"where\": \"p. 56\", \"stance\": \"supports\",\n    \"note\": \"MacKenzie gives the New Persian outcomes explicitly in the entries: 'N māda', 'N māya', 'mādar … N ~', 'mādīyān … N ~'.\"}\n ]\n}\n\nn4 = {\n \"id\": 4, \"lang\": \"Germanic\", \"words\": \"môthar\", \"verdict\": \"confirmed\",\n \"derivation\": \"Proto-Germanic *mōþar- / *mōdēr 'mother' < PIE *méh₂tēr: PIE *t became Proto-Germanic *þ by Grimm's Law, and in West and North Germanic that *þ was then voiced and stopped between vowels, giving OE mōdor, OS modar, ON móðir, OHG muoter (with the regular OHG diphthongisation of ō to uo). Nourai's spelling 'môthar' is Watkins's *mōthar- copied verbatim from the AHD appendix, where th = þ.\",\n \"derivation_fa\": \"ژرمنی آغازین *mōþar-/*mōdēr «مادر» از *méh₂tēr هندواروپایی آغازین است: t هندواروپایی بر پایهٔ قانون گریم به þ بدل شده و سپس در ژرمنی غربی و شمالی میان دو واکه واک‌دار و انسدادی شده است (انگلیسی کهن mōdor، آلمانی عالی کهن muoter). نگارش «môthar» نورایی همان *mōthar- واتکینز است. ادعای نورایی درست است.\",\n \"sources\": [E_MOTHER, W_PIE],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt l.730 s.v. māter-: '1. Germanic *mōthar- in Old English mōdor, mother: MOTHER.' — Nourai's node is a direct copy.\"},\n   {\"ref\": \"KLN\", \"status\": \"supports\", \"note\": \"KLN_1966.txt leaf 540 (printed ~1008) s.v. mother: 'ME. moder, fr. OE. modor, rel. to OS. modar, ON. mōðir, Dan., Swed. moder, OFris. moder, Du. moeder, OHG., MHG. muoter, G. Mutter, and cogn. with OI. mātár- … L. mater … All these words derive fr. I.-E. *māter-, which is traceable to child’s lip word ma-.'\"}\n ],\n \"consulted\": [\n   {\"src\": \"SKT\", \"where\": \"leaf 318 (printed ~298) s.v. Mother (1)\", \"stance\": \"supports\",\n    \"note\": \"'Mother (1), a female parent. moder. A.S. mōdor … + Du. moeder, Icel. mōðir … G. mutter … L. mater, Gk. mētēr, Skt. mātā'.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. II 229\", \"stance\": \"supports\", \"note\": \"'ahd. muoter, ags. mōdor, aisl. mōðir ‚Mutter‘' listed under matēr-.\"}\n ]\n}\n\nn5 = {\n \"id\": 5, \"lang\": \"English\", \"words\": \"mother\", \"verdict\": \"confirmed\",\n \"derivation\": \"Old English mōdor > Middle English moder > modern mother. The intrusive -th- is a later English development (moder > mother, like fader > father, weder > weather), completed in the 16th century; the word is the direct native reflex of Germanic *mōþar-, never a borrowing.\",\n \"derivation_fa\": \"انگلیسی mother بازماندهٔ موروثی انگلیسی کهن mōdor است؛ از راه انگلیسی میانه moder، و تبدیل d به th در سدهٔ شانزدهم میلادی رخ داده (مانند fader > father). ادعای نورایی درست است.\",\n \"sources\": [E_MOTHER],\n \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference for this node; checked against Etymonline, Klein and Skeat instead.\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"printed ~1008 s.v. mother\", \"stance\": \"supports\", \"note\": \"'ME. moder, fr. OE. modor' (KLN_1966.txt leaf 540).\"},\n   {\"src\": \"SKT\", \"where\": \"leaf 318 s.v. Mother (1)\", \"stance\": \"supports\", \"note\": \"'moder. A.S. mōdor, mōdor, a change from d to th seems n[atural] influence' — Skeat notes the d > th shift.\"}\n ]\n}\n\nn6 = {\n \"id\": 6, \"lang\": \"Latin\", \"words\": \"mamma; mâter; mâtrix; mâteriěs, materia\", \"verdict\": \"confirmed\",\n \"derivation\": \"Two strands of the root box in one Latin node, both correct. (a) mamma 'breast; mother, wet-nurse, grandmother' is the reduplicated nursery form of *mā- (Pokorny 694; Varro ap. Non. 81,4 'cum cibum ac potionem buas ac pappas uocent, et matrem mammam, patrem tatam'), with the diminutive mamilla 'nipple' — this is where Nourai's 'Mā: breast' gloss actually comes from. (b) māter, mātris 'mother' is the regular Italic reflex of *méh₂tēr (Osc. maatreís, Umbr. matrer). mātrīx 'breeding animal, womb' is built on māter on the model of nūtrīx 'wet-nurse' (Klein p.948), matching Greek mḗtra 'womb'. māteriēs/materia is 'the mother-stock of a tree, the hard inner wood', hence 'timber', hence — by a calque on Greek hýlē 'wood; matter' in philosophical Latin — 'material, matter'; Ernout–Meillet: 'où il désigne la branche mère, le tronc principal'. Nourai's gloss 'tree's source of growth, trunk, also hard wood, material' is Watkins's wording verbatim.\",\n \"derivation_fa\": \"در این گره دو رشتهٔ ریشه کنار هم آمده‌اند و هر دو درست است: ۱) mamma «پستان؛ مادر، دایه» صورت دوگان‌شدهٔ واژهٔ کودکانهٔ *mā- است (پوکورنی ۶۹۴؛ وارو نیز گواهی می‌دهد) و همین منشأ معنای «پستان» در جعبهٔ ریشهٔ نورایی است؛ ۲) māter «مادر» بازماندهٔ قاعده‌مند *méh₂tēr است، mātrīx «زادار، دام ماده» بر قیاس nūtrīx ساخته شده (کلاین، ص ۹۴۸) و برابر mḗtra یونانی است؛ و māteriēs/materia نخست «تنهٔ درخت، چوب سخت» بوده و سپس در ترجمهٔ قرضی hýlē یونانی معنای «مادّه» گرفته است (ارنو‌میّه؛ دووان و واتکینز نیز materia را از māter می‌گیرند).\",\n \"sources\": [E_MATERIAL, E_MAMMAL],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt l.730 s.v. māter-: '2. Latin mater, mother: MATER, MATERNAL, MATERNITY, (MATRICULATE), MATRIX, MATRON; MADREPORE, MATRIMONY. … 4. Latin māteriēs, materia, tree trunk (< “matrix,” the tree’s source of growth), hence hard timber used in carpentry, hence (by a calque on Greek hŭlē, wood, matter) substance, stuff, matter: MATERIAL, MATTER.'\"},\n   {\"ref\": \"KLN:948\", \"status\": \"supports\", \"note\": \"Klein's printed p.948 (KLN_1966.txt leaf 509, page number '948' printed in mid-leaf) carries exactly the māter-family: 'matrix, n., womb. — L. matrix, “womb, matrix, source, origin”, formed fr. mater, gen. mātris, “mother”, on analogy of nutrix, “wet-nurse” … For the sense development of L. matrix (fr. mater, “mother”) cp. Gk. mḗtra, “uterus, womb”'; 'matter, n. — ME. matere, fr. OF. matere, fr. L. materia, “wood, timber, stuff, matter”, formed fr. L. mater, “mother”, as translation of Gk. hylē'; also matri-, matrimony, matron on the same page. Latin mamma is not on p.948 but on Klein's p.929 (leaf 499): 'mamma, also mama, n., mother. — Formed with reduplication from infants’ babbling *ma- … L. mamma, “mother, midwife, grandmother; mother’s breast, nipple”'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"LAT\", \"where\": \"Ernout–Meillet s.vv. mamma, māter, materies\", \"stance\": \"supports\",\n    \"note\": \"'mamma, -ae f.: “maman” et “mamelle” … Mot du langage enfantin, cf. Varr. … et matrem mammam, patrem tatam' (LAT.txt l.36013); 'māter, -tris f.: mère … même des plantes … uasto matris corpore, où il désigne la branche mère, le tronc principal; materies. Par image, mater a pu s’employer au sens de “cause, origine, source”, etc.; cf. mētropolis' (l.36740); on materies: 'la partie de l’arbre … le sens de “bois de construction” … il a servi à rendre le gr. hylē dans son sens figuré' (ll.36820–36846).\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. II 229–230\", \"stance\": \"partial\",\n    \"note\": \"Walde–Pokorny accept 'lat. matrix ‚Gebärmutter; Zuchttier‘' under matēr- 'Mutter', but hesitate over materia: they weigh a separate IE tree-name *mater- ('ist wohl ein idg. Baumname mater- zu erschließen') and cross-refer 'mater- ‚Baumname“: s. u. mater- ‚Mutter“'. Modern Latin etymology (de Vaan, Watkins, Etymonline) has come back to Nourai's/Watkins's view that materia is from māter.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann pp. 735–736\", \"stance\": \"partial\", \"note\": \"Mann keeps 'māter- (2) ‚wood, timber, substance‘ … Lat. materies … materia' apart from 'mātēr (1) ‚mother‘'.\"}\n ]\n}\n\nn7 = {\n \"id\": 7, \"lang\": \"French\", \"words\": \"\", \"verdict\": \"confirmed\",\n \"derivation\": \"Empty pass-through box: the French stage between Latin and the Persian loans below. The relevant French words are the nursery maman (< Latin mamma, reduplicated, first recorded 17th c. and the form actually borrowed into Persian) and, for the learned strand, mère < Latin māter and matière < materia. Latin mamma > French maman with the nasalised second syllable characteristic of French hypocoristics (cf. papa).\",\n \"derivation_fa\": \"این جعبهٔ خالی مرحلهٔ فرانسوی میان لاتین و وام‌واژهٔ فارسی است: فرانسوی maman (از mamma لاتینی، با دوگان‌سازی واژهٔ کودکانه) و نیز mère از māter و matière از materia. این گره فقط گذرگاه است و مشکلی ندارد.\",\n \"sources\": [E_MAMMAL, W_MAMAN],\n \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"no reference given by Nourai for this pass-through node.\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"printed p.929 s.v. mamma\", \"stance\": \"supports\", \"note\": \"Klein lists 'F. maman' among the reduplicated *ma- forms alongside L. mamma.\"},\n   {\"src\": \"LAT\", \"where\": \"s.v. mamma\", \"stance\": \"supports\", \"note\": \"'Les l. romanes ont gardé mamma au sens de “maman”, réservant le sens de “sein, mamelle” à mamilla' (LAT.txt l.36013ff).\"}\n ]\n}\n\nn8 = {\n \"id\": 8, \"lang\": \"Persian\", \"words\": \"(extra: مامان ، ممه)\", \"verdict\": \"disputed\",\n \"derivation\": \"Split verdict. مامان māmān is indeed a French loan: Wiktionary, 'Borrowed from French maman. Displaced ننه (nana/nane) in most urban dialects of Iran', and Mo'in tags the derivative مامانی as [فر. ف.] (French + Persian), i.e. built on a French base — it enters Persian in the Qajar/Pahlavi period through French-language schooling. ممه memeh 'breast (child language)' is NOT from French: Mo'in's Farhang-e Farsi marks it 'ممه: [تر.] (ا.) (به زبان کودکان) پستان', i.e. a Turkish loan (Turkish meme 'breast'), and the wider consensus (Klein, Etymonline) is that such forms are independent reduplications of the universal nursery syllable ma-, 'a reduplication of *ma- that is nearly universal among the Indo-European languages', not transmitted through Latin and French. So the arrow French → Persian holds for مامان only; for ممه modern scholarship prefers Turkish meme or a spontaneous nursery formation.\",\n \"derivation_fa\": \"در این گره دو واژه سرنوشت یکسان ندارند. «مامان» وام‌واژهٔ فرانسوی maman است که در دوران قاجار و پهلوی از راه مدارس فرانسه‌زبان وارد شد و در گویش شهری جای «ننه» را گرفت (ویکی‌واژه؛ معین نیز «مامانی» را [فر. ف.] می‌نویسد)؛ پس این پیکان درست است. امّا «ممه» فرانسوی نیست: معین آن را وام‌واژهٔ ترکی (meme) می‌داند و کلاین و اتیمانلاین این گونه صورت‌ها را دوگان‌سازی مستقل هجای کودکانهٔ ma- می‌شمارند، نه وامی از راه لاتین و فرانسه. پس پژوهش امروزی نیمی از این گره را رد می‌کند.\",\n \"sources\": [W_MAMAN, E_MAMMAL],\n \"ref_check\": [\n   {\"ref\": \"MON:3679,3716\", \"status\": \"partial\",\n    \"note\": \"Mo'in's 6-vol pages are not mappable online, but both entries were read in the 2-vol Adena OCR of Farhang-e Farsi: 'مامان: (ا.) (در زبان کودکان) مادر، والده' with 'مامانی: mamanī [فر. ف.]' (MON_part2.txt ll.43100, 43109) and 'ممه: [تر.] (ا.) (به زبان کودکان) پستان. ممه را لولو برد' (l.65508). Mo'in therefore backs the French origin for مامان but flatly contradicts it for ممه, which he marks Turkish.\"}\n ],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"s.vv. مامان, مامانی, ممه\", \"stance\": \"partial\", \"note\": \"see ref_check: [فر.] for the مامان family, [تر.] for ممه.\"},\n   {\"src\": \"KLN\", \"where\": \"printed p.929 s.v. mamma\", \"stance\": \"contradicts\",\n    \"note\": \"Klein treats ModPers. mam, mama as independent reflexes of the babbling *ma-, on a par with F. maman, Russ. mama, Lith. mama — not as loans from French: 'Formed with reduplication from infants’ babbling *ma-, whence also … ModPers. mam, mama, “mother” … F. maman'.\"},\n   {\"src\": \"BQT\", \"where\": \"vol. 4, our printed p.1950 (Nourai's ~1948) s.vv. مام, مامک, ماما\", \"stance\": \"contradicts\",\n    \"note\": \"Mo'in's footnote there sets the Persian nursery words beside their IE cognates without any French mediation: 'قس: ماما، مامی، لیتوانی mama (مادر)، اسلاوی کلیسایی mama، آلبانی memë … یونانی mammē، لاتینی mamma, mamilla … پازند māmā (مادر)'.\"}\n ]\n}\n\nn9 = {\n \"id\": 9, \"lang\": \"English\", \"words\": \"mammal, maternal, maternity, matrimony, matrix, matter, material\", \"verdict\": \"confirmed\",\n \"derivation\": \"All seven are Latinate, exactly as drawn. mammal (1826) < ModL. Mammalia, Linnaeus 1758, < Late L. mammālis 'of the breast' < L. mamma. maternal < MF. maternel < L. māternus; maternity < F. maternité < Med.L. māternitās; matrimony < ME. matrimoine < OF. matremoine < L. mātrimōnium (māter + -mōnium); matrix taken straight from L. mātrīx 'womb'; matter < ME. matere < OF. matere < L. materia; material < Late L. māteriālis. Watkins lists precisely this set of English words under māter-.\",\n \"derivation_fa\": \"همهٔ این هفت واژه لاتینی‌تبارند و همان که در نمودار آمده: mammal از Mammalia لاتین نو (لینه، ۱۷۵۸) از mamma؛ maternal، maternity، matrimony، material همه از راه فرانسهٔ میانه و لاتین متأخر؛ matrix مستقیماً از mātrīx؛ و matter از materia از راه فرانسهٔ کهن matere. واتکینز در پیوست AHD همین فهرست را زیر māter- می‌آورد؛ ادعای نورایی درست است.\",\n \"sources\": [E_MATERIAL, E_MAMMAL],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt l.730: 'MATER, MATERNAL, MATERNITY, (MATRICULATE), MATRIX, MATRON; MADREPORE, MATRIMONY … MATERIAL, MATTER' under māter-, and MAMMAL under mamma/ma-2 (l.1419 index: 'DEMETER mater-').\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"printed pp. 929, 946–949\", \"stance\": \"supports\",\n    \"note\": \"'Mammalia, n. pl. — ModL., coined by Linnaeus in 1758 fr. Late L. mammalia … fr. L. mamma, “breast”'; 'maternal, adj. — ME., fr. MF. (= F.) maternel, fr. L. māternus, “of a mother”, fr. mater'; 'material, adj. — ME., fr. Late L. māteriālis'; 'matrimony … fr. L. matrimonium'; 'matter, n. — ME. matere, fr. OF. matere … fr. L. materia'.\"},\n   {\"src\": \"SKT\", \"where\": \"leaf 298 s.v. Maternal\", \"stance\": \"supports\", \"note\": \"'Maternal. (F. – L.) F. maternel … Low L. maternalis … L. maternus, [belong]ing to a mother. — L. mater, mother; [cog]nate with Mother.' (SKT.txt l.11220).\"}\n ]\n}\n\nn10 = {\n \"id\": 10, \"lang\": \"Greek\", \"words\": \"mětěr\", \"verdict\": \"confirmed\",\n \"derivation\": \"Ancient Greek mḗtēr (Doric mā́tēr) 'mother' < PIE *méh₂tēr, with the Attic-Ionic change of inherited long ā to ē (hence Doric mātēr keeps the original vowel; the nominative accent is retracted, as in thugátēr). Nourai's extra gloss 'main, central' is not a sense of the bare noun but of its compounds and metaphors — mētrópolis 'mother city, parent state of a colony, capital', mḗtra 'womb', and mḗtēr used figuratively for 'source, origin' (Ernout–Meillet make the same observation for Latin māter, 'au sens de “cause, origine, source” … cf. mētropolis'). Nourai's transcription 'mětěr' uses his usual breve for the long ē.\",\n \"derivation_fa\": \"یونانی باستان mḗtēr (دوریک mā́tēr) «مادر» از *méh₂tēr است؛ الف کشیدهٔ موروثی در گویش آتیک‌ایونی به ē بدل شده و در دوریک مانده است. معنای افزودهٔ «اصلی، مرکزی» از خود واژه نیست بلکه از ترکیب mētrópolis «شهر مادر، پایتخت» و استعارهٔ «منشأ» می‌آید. ادعای نورایی درست است؛ تنها در گلّه‌نویسی کمی وسعت داده شده است.\",\n \"sources\": [E_METROPOLIS, W_PIE],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt l.730 s.v. māter-: '3. Greek mētēr, mother: METRO-; METROPOLIS.'\"}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. II 229\", \"stance\": \"supports\", \"note\": \"'gr. mētēr, dor. mātēr (mit verschobenem Nominativakzent, wie thugátēr)'; and for the extended sense 'Gr. mḗtra ‚Gebärmutter‘ … Mark der Pflanzen'.\"},\n   {\"src\": \"KLN\", \"where\": \"printed ~1008 s.v. mother\", \"stance\": \"supports\", \"note\": \"'cogn. with … Gk. mḗtēr, Dor. mātēr, “mother” … Cp. … metropolis, Demeter, metronymic'.\"}\n ]\n}\n\nn11 = {\n \"id\": 11, \"lang\": \"English\", \"words\": \"metro, metropolitan\", \"verdict\": \"confirmed\",\n \"derivation\": \"metropolitan (mid-14c.) < Late L. mētropolitānus < Gk. mētropolītēs, from mētrópolis 'mother city' (mḗtēr + pólis); it entered English first as an ecclesiastical title, 'a bishop having general superintendency over other bishops of his province', and only later took the secular sense. metro is a 20th-c. clipping of French (chemin de fer) métropolitain, the Paris underground railway (1900), so it reaches English through French but from the same Greek compound. The chain root → Greek → English is therefore right.\",\n \"derivation_fa\": \"metropolitan در سدهٔ چهاردهم میلادی از لاتین متأخر mētropolitānus و آن از یونانی mētrópolis «شهر مادر» (mḗtēr + pólis) وارد انگلیسی شده، نخست به معنای عنوان کلیسایی (متروپولیتان = اسقف اعزم) و سپس معنای غیردینی. metro کوتاه‌شدهٔ فرانسوی métropolitain (راه‌آهن زیرزمینی پاریس، ۱۹۰۰) است. پس پیکان ریشه ← یونانی ← انگلیسی درست است.\",\n \"sources\": [E_METROPOLIS],\n \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"no reference given by Nourai; checked against Etymonline and Klein.\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"printed ~1008 s.v. mother (cross-references) and s.v. metropolis\", \"stance\": \"supports\", \"note\": \"Klein's 'mother' entry ends 'Cp. … matter, metropolis, Demeter', i.e. he files metropolis under the same root.\"},\n   {\"src\": \"SKT\", \"where\": \"leaf 306 s.v. Metropolis\", \"stance\": \"supports\", \"note\": \"SKT.txt leaf 306: '… a state; the city of a primate. — Gk. mētro- for mētēr, a mother; polis, a city … See Mother and Police.'\"}\n ]\n}\n\nentry = {\n \"entry\": 0,\n \"root\": \"Mâ, Mâ-ter\",\n \"verdict\": \"plausible\",\n \"modern_form\": \"PIE *méh₂tēr 'mother' (Pokorny māter- 700–701; AHD māter-), itself built on the nursery word *mā- / *méh₂- 'mother' (Pokorny mā-3, 694)\",\n \"note\": \"Both halves of the root box are real reconstructions and the language label 'Indo-European' is right, but two details of the gloss are Nourai's own. (1) Pokorny's mā-3 (p.694, the page Nourai cites) is glossed 'mother (expr. root)', not 'breast'; the 'breast' sense comes only from the reduplicated derivatives (L. mamma 'mother’s breast, nipple', mamilla), so it is a back-projection. (2) 'Mā-ter: feeder (of the family)' with the cross-reference to Ter 3 analyses -ter- as the agent suffix. Watkins and Walde–Pokorny call it the KINSHIP suffix and offer no such gloss ('Based ultimately on the baby-talk form ma-2, with the kinship term suffix -ter-'); Skeat's older view was '√MĀ to measure', i.e. 'manager of the household'; and Wiktionary reports a minority modern view of a genuine verbal root *méh₂- 'to nurse, to mother' — which is the closest anyone comes to Nourai's 'feeder', but it is not the standard account. Also note the page numbers: 694 is mā-3, while māter- is Pokorny 700–701. Nourai's closing remark about a nursery word becoming the usual term is a paraphrase of Buck 2.36 (SYN:103), which he cites correctly. Everything downstream (Avestan–Pahlavi–Persian; Germanic; Latin; Greek) is sound; the one substantive error on the page is in node #8.\",\n \"note_fa\": \"ریشهٔ هندواروپایی آغازین *méh₂tēr «مادر» (پوکورنی ۷۰۰–۷۰۱) و واژهٔ کودکانهٔ *mā- (پوکورنی ۶۹۴) هر دو واقعی اند و برچسب «هندواروپایی» درست است؛ امّا دو نکتهٔ معنایی از خود نورایی است: یکی آنکه پوکورنی در ص ۶۹۴ mā-3 را «مادر» معنی کرده و نه «پستان» — معنای پستان تنها از مشتقّات دوگان‌شده (mamma, mamilla لاتینی) برمی‌آید؛ دوم آنکه تفسیر «mā-ter = خوراک‌دهندهٔ خانواده» پسوند -ter- را پسوند فاعلی گرفته، در حالی که واتکینز و والده‌پوکورنی آن را پسوند واژگان خویشاوندی می‌دانند و چنین معنایی نمی‌دهند (ویکی‌واژه دیدگاهی اقلیتی را گزارش می‌کند که *méh₂- را ریشهٔ فعلی «شیر دادن، مادری کردن» می‌گیرد). در مجموع ریشه با احتیاط پذیرفتنی است و همهٔ شاخه‌های پایین‌دست درست اند؛ تنها خطای جدی این صفحه در گرهٔ ۸ («ممه») است.\",\n \"sources\": [W_PIE, E_MOTHER],\n \"ref_check\": root_refcheck,\n \"consulted\": root_consulted,\n \"nodes\": [n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11],\n}\n\nout = {\n \"pdf_page\": 316,\n \"book_page\": 286,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-06\",\n \"entries\": [entry],\n}\n\nwith io.open('/home/sfmqrb/git/rishe/data/verification/page-316.json','w',encoding='utf-8') as f:\n    json.dump(out, f, ensure_ascii=False, indent=2)\n    f.write('\\n')\nprint('written')\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/mk316.py"
}
```


### [2026-09-07T01:57:05.521Z] TOOL RESULT

```
written
```


## [2026-09-07T01:57:08.860Z] TOOL CALL #77: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-316.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 316"
}
```


### [2026-09-07T01:57:10.139Z] TOOL RESULT

```
JSON OK
nodes verified: 11/11
node verdicts: {'confirmed': 10, 'disputed': 1}
root verdicts: {'plausible': 1}
ref checks: {'partial': 6, 'supports': 9, 'not_checked': 3}
books consulted: {'supports': 23, 'partial': 3, 'contradicts': 2} | by book: {'KLN': 6, 'WLD': 4, 'SKT': 4, 'BRT': 2, 'PHD': 2, 'MON': 2, 'LAT': 2, 'KNT': 1, 'NYB': 1, 'HUB': 1, 'ARY': 1, 'IEC': 1, 'BQT': 1}
```


## [2026-09-07T01:57:29.769Z] AGENT

Done. `data/verification/page-316.json` written; `verify_check.py 316` reports 11/11 nodes, 0 PROBLEM lines.

**Page 316 (book p. 286) — one entry, root "Mâ, Mâ-ter" [Indo-European]**

- Verdicts: root `plausible`; nodes **10 confirmed, 1 disputed**.
- Ref checks: 9 supports, 6 partial, 3 not_checked. Books consulted: POK, WLD, AHD(Watkins), IEC, SYN, KLN, SKT, LAT, BRT, KNT, PHD, NYB, HRN, HUB, BQT(v4 scan), MON, ARY, SNS + Wiktionary/Etymonline (10 URLs archived via `fetch_source.py`).

Findings:
- **ROOT `plausible`** — both *mā- and *māter- are real, but (a) Pokorny 694 (the page cited) glosses mā-3 "mother", not "breast" (the breast sense is only from reduplicated L. *mamma/mamilla*), and *māter-* is Pokorny **700–701**, not 694; (b) "Mā-ter: feeder (of the family)" treats *-ter-* as an agent suffix — Watkins and Walde-Pokorny call it the kinship suffix; Skeat's older view was √MĀ "measure" → "manager of the household". Wiktionary notes a minority view of a verbal root *méh₂- "to nurse", the closest support for "feeder".
- **#8 [Persian] مامان ، ممه ← French: `disputed`.** مامان is genuinely French *maman* (Wiktionary: "Borrowed from French maman. Displaced ننه"; Mo'in tags مامانی [فر. ف.]). But **ممه is not French**: Mo'in's Farhang-e Farsi marks it "ممه: [تر.]" — Turkish *meme* "breast" — and Klein/Etymonline treat such forms as independent reduplications of the universal nursery syllable *ma-.
- Notable positives: HRN:213 (Horn no. 956) matches node #3 word-for-word including *mādiyān*, *mākiyān* (< *mādkiyān); Hübschmann §88 (p.194) documents *mātak > māya*; Nyberg supplies *mātak* "essence" and *mātag-dān/mātīyān* = Nourai's "mâdiyânag"; Mo'in's BQT footnote on مایه cites Horn deriving NP *māya* and L. *māteriēs* from *māter-*.
- **BQT pagination note (useful for later pages):** Nourai's Borhan-e Qate' page numbers run **2 lower** than the Ibn Sina scan on disk — his 1933/1946/1964 = our printed 1935 (مادر)/1948 (ماکیان، مادیان)/1966 (مایه) = `BQT_v4` pdf pages 16/29/47. All three refs check out once that offset is applied.
- **SKT:336 (node #1) partial:** Skeat's "Mother" entry sits at leaf 318 ≈ printed p. 298 in the 1911 scan (p. 336 is the "Parity–Parsee" page); content supports the claim, page number does not match this edition.
- **No extraction errors** — the JSON is faithful to the chart; no `transcription_suspect` nodes (the breve-for-macron spellings *mětěr*, *mâteriěs* are Nourai's own house transcription).
