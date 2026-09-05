# Verification process log — verify-page-173


## [2026-09-05T20:47:24.656Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 173 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-173.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-173.json. Write /home/sfmqrb/git/rishe/data/verification/page-173.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 173` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T20:47:26.404Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T20:47:27.115Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T20:47:27.129Z] TOOL RESULT

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


## [2026-09-05T20:47:27.248Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-173.txt"
}
```


### [2026-09-05T20:47:27.259Z] TOOL RESULT

```
1	=== PDF page 173 (book page 143) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Ger 1 : crooked, curved, round object  (refs POK:385)
4	#1 (parent #0) [Sanskrit] refs=POK:386 | grath, granth : knot
5	  #2 (parent #1) [Old Persian] refs=BQT:1803 | gratha : knot, tie ; gravatha : assemblage, group
6	    #3 (parent #2) [Persian] refs=BQT:1803; MON:3280 | gereh «گره» : knot
7	    #4 (parent #2) [Pahlavi] refs=VFO:25 | groh : group
8	      #5 (parent #4) [Persian] refs=MON | gorŭh «گروه» : group
9	#6 (parent #0) [Italian] refs=AHD:582,1516 | grappo : assemblage
10	  #7 (parent #6) [French] refs=None | groupe
11	    #8 (parent #7) [English] refs=None | group
12	#9 (parent #0) [Germanic] refs=AHD | grâppon : a hook used for harvesting grapes
13	  #10 (parent #9) [English] refs=None | grape
14	#11 (parent #0) [Old English] refs=AHD | 
15	  #12 (parent #11) [English] refs=None | cripple, creep, crutch, crank, crumb, crop, crib, cradle, cart
16	#13 (parent #0) [Dutch] refs=AHD | crulle | NOTE: This is a Middle Dutch word.
17	  #14 (parent #13) [English] refs=None | curl
18	
```


## [2026-09-05T20:47:30.612Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-173.json",
 "description": "Read source JSON for page 173"
}
```


### [2026-09-05T20:47:30.666Z] TOOL RESULT

```
{
  "pdf_page": 173,
  "book_page": 143,
  "entries": [
    {
      "root": {
        "name": "Ger 1",
        "lang": "Indo-European",
        "refs": "POK:385",
        "gloss": "crooked, curved, round object"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "POK:386",
          "words": [
            {"translit": "grath, granth", "gloss": "knot", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Old Persian",
          "refs": "BQT:1803",
          "words": [
            {"translit": "gratha", "gloss": "knot, tie", "script": null},
            {"translit": "gravatha", "gloss": "assemblage, group", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "BQT:1803; MON:3280",
          "words": [
            {"translit": "gereh", "gloss": "knot", "script": "گره"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 2,
          "lang": "Pahlavi",
          "refs": "VFO:25",
          "words": [
            {"translit": "groh", "gloss": "group", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Persian",
          "refs": "MON",
          "words": [
            {"translit": "gorŭh", "gloss": "group", "script": "گروه"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Italian",
          "refs": "AHD:582,1516",
          "words": [
            {"translit": "grappo", "gloss": "assemblage", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "French",
          "refs": null,
          "words": [
            {"translit": "groupe", "gloss": null, "script": null}
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
            {"translit": "group", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "grâppon", "gloss": "a hook used for harvesting grapes", "script": null}
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
            {"translit": "grape", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 0,
          "lang": "Old English",
          "refs": "AHD",
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 11,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "cripple, creep, crutch, crank, crumb, crop, crib, cradle, cart", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 0,
          "lang": "Dutch",
          "refs": "AHD",
          "words": [
            {"translit": "crulle", "gloss": null, "script": null}
          ],
          "note": "This is a Middle Dutch word.",
          "quote": null
        },
        {
          "id": 14,
          "parent": 13,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "curl", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
```


## [2026-09-05T20:47:32.733Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','AHD','BQT','MON','VFO','WLD','KLN','HRN','HUB','PHD','NYB','SKT','IEC','SYN','BRT','KNT','ARY','WEB','FSD','CHEUNG']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:400])\n\""
}
```


### [2026-09-05T20:47:34.497Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
VFO null
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "loca
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
CHEUNG null
```


## [2026-09-05T20:47:39.023Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'));print(sorted(d.keys()))\n\" ; echo ---; grep -rn \"VFO\" --include=*.md --include=*.json --include=*.txt data/verification/sources/ data/*.md 2>/dev/null | head -20; echo ---; ls data/verification/sources/refs/ | head -60"
}
```


## [2026-09-05T20:47:39.607Z] TOOL CALL #6: Bash

```json
{
 "command": "sed -n 1,200p data/verification/sources/SOURCE_MATRIX.md"
}
```


### [2026-09-05T20:47:41.129Z] TOOL RESULT

```
['AEF', 'AFA', 'AFM', 'AHD', 'AHM', 'AID', 'AIN', 'AKD', 'AKM', 'AMD', 'ARB', 'ARK', 'ARM', 'ARP', 'ARY', 'AVG', 'AWH', 'BLY', 'BQT', 'BRT', 'BST', 'CEL', 'DEV', 'DMO', 'DOZ', 'DRM', 'DVS', 'DZA', 'EAV', 'ETM', 'FAF', 'FFD', 'FIB', 'FNI', 'FRS', 'FSD', 'FSF', 'FVA', 'FVF', 'FVQ', 'FVS', 'FWE', 'GPL', 'HID', 'HJB', 'HRN', 'HUB', 'IEC', 'IRN', 'IRT', 'ISS', 'KAS', 'KFL', 'KGW', 'KLN', 'KNT', 'LAM', 'LAT', 'LEW', 'LKT', 'LST', 'MAG', 'MFL', 'MMF', 'MON', 'MPP', 'MZF', 'NAT', 'NFI', 'NYB', 'OEW', 'OXF', 'PEI', 'PHD', 'PHN', 'PLA', 'POK', 'PRT', 'RCH', 'ROE', 'SAP', 'SBK', 'SDQ', 'SHP', 'SIN', 'SKT', 'SLW', 'SNB', 'SNS', 'SOD', 'SOG', 'SOR', 'SPG', 'SYN', 'TAD', 'TLM', 'TTS', 'TYL', 'TZF', 'UNV', 'VDQ', 'VGH', 'VIE', 'VOP', 'VSF', 'WEB', 'WLD', 'ZAP', 'ZAW', 'ZFS', 'ZMA']
---
(eval):3: no matches found: --include=*.md
---
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
```


### [2026-09-05T20:47:41.164Z] TOOL RESULT

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


## [2026-09-05T20:48:13.748Z] TOOL CALL #7: Bash

```json
{
 "command": "grep -rIl \"VFO\" data/extracted/ 2>/dev/null | head; echo ---; grep -rIho \"VFO[^\\\"]\\{0,80\\}\" data/extracted/ 2>/dev/null | sort | uniq -c | sort -rn | head -20"
}
```


## [2026-09-05T20:48:13.922Z] TOOL CALL #8: Bash

```json
{
 "command": "ls tools/; echo ---; sed -n 1,40p data/verification/page-124.json"
}
```


### [2026-09-05T20:48:15.656Z] TOOL RESULT

```
data/extracted/batch/page-241.json
data/extracted/batch/page-494.json
data/extracted/batch/page-471.json
data/extracted/batch/page-173.json
data/extracted/batch/page-268.json
data/extracted/batch/page-44.json
data/extracted/batch/page-77.json
---
      2 VFO:24
      2 VFO:15
      1 VFO claims these are cognates of English \
      1 VFO:25
      1 VFO:23; MON:2211
      1 VFO:22; BQT:1090
      1 VFO:18 claims these words are related to English \
```


### [2026-09-05T20:48:15.694Z] TOOL RESULT

```
build_site.py
fetch_source.py
ganjoor.py
__pycache__
ref_index_latin.py
ref_index_pages.py
ref_locator
ref_ocr_book.py
ref_page.py
research.py
validate.py
verify_archive_sources.py
verify_check.py
verify_export_process.py
verify_publish.sh
---
{
  "pdf_page": 124,
  "book_page": 94,
  "verified_by": "claude-opus-5",
  "verified_on": "2026-09-05",
  "entries": [
    {
      "entry": 0,
      "root": "Dhě 2",
      "verdict": "confirmed",
      "modern_form": "PIE *dʰeh₁- 'to put, place; to do' (Pokorny 235-239 dʰē-2; Watkins/AHD dhē-¹)",
      "note": "The root box is right on all three counts. Pokorny's own lemma reads 'Root / lemma: dʰe-2, Meaning: to put, place, say' with 'Page(s): 235-239', so Nourai's 'Dhě 2 : to do, set' with POK:235 reproduces Pokorny's numbering and gloss exactly; Watkins in the AHD appendix has 'dhē-¹. To set, put. Contracted from *dheə ... [Pok. 2. dhē- 235]', and Wiktionary's reconstruction page glosses *dʰeh₁- 'to do; to put, place'. The Iranian material of the chart is likewise Pokorny's own: 'with full grade Avestan Old pers. dāta-', 'Avestan ni-δaiti- „laying down, putting away, hiding“', 'Avestan gao-δi- / gao-δana- „milk container“', 'Avestan dāman-, dąman- n. „site, creature“'. Three things in Part 1 need correcting rather than the root itself. (1) The Avestan mouth-veil is paiti.dāna-, not 'paiti-dâma' (node #3) — a misprint in the printed book, and one that Mo'in's footnote on the very page Nourai cites (Borhān p.418) refutes. (2) apa-dāna- (node #6) is Old Persian, not Avestan, and means 'palace, columned hall'; 'the concealed part of a palace' is Kent's etymological comparison with Skt. apadhā-, not the word's attested sense. (3) Pahlavi dast-war (node #13) does not belong to this root at all: Horn p.127, the page Nourai cites, and Nyberg II 61 both derive it from the root daṇs-/dąh- 'to teach', and Wiktionary offers only *dasta-bara- 'hand-bearer' or *danh- 'to teach'. A fourth, smaller point: the gloss 'to settle, to give' on node #11 mixes this root with PIE *deh₃- 'to give', a distinction Nourai's own reference FFD:52 (Abolghasemi p.52) draws explicitly. Two of the four boxes on the Persian side, the Sogdian box and both of the Persian outcomes of the law-branch check out completely, and Gharib's Sogdian entry γwδʾak even carries the Avestan etymology Nourai draws.",
      "note_fa": "خودِ ریشه کاملاً درست است: پوکورنی در صفحات ۲۳۵–۲۳۹ مادهٔ dʰē-2 را با معنای «نهادن، قرار دادن» آورده و واتکینز در پیوست فرهنگ American Heritage همین را می‌گوید؛ مواد ایرانی نمودار (dāta-، ni-δaiti-، gao-δana-، dāman-) هم عیناً از همین مادهٔ پوکورنی است. سه لغزش در بخش یکم هست: ۱) صورت اوستایی «پنام» paiti.dāna- است نه paiti-dāma — خطای چاپی کتاب؛ ۲) apadāna پارسی باستان است نه اوستایی و معنایش «کاخ، تالار بار» است؛ ۳) پهلوی dastwar هیچ ربطی به این ریشه ندارد و هرن (ص ۱۲۷) و نیبرگ (ج۲ ص ۶۱) آن را از ریشهٔ daṇs-/dąh- «آموختن» می‌گیرند. نکتهٔ کوچک‌تر آنکه معنای «دادن» در خانهٔ ۱۱ متعلق به ریشهٔ دیگر *deh₃- است و ابوالقاسمی در همان FFD:52 این دو را جدا کرده است. در مجموع، ادعای نورایی دربارهٔ خودِ ریشه درست است.",
      "sources": [
        "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/d%CA%B0eh%E2%82%81-"
      ],
      "ref_check": [
        {
          "ref": "AHD:1512",
          "status": "supports",
          "note": "Watkins's Indo-European appendix (local file AHD_watkins1985.txt line 375): 'dhē-¹. To set, put. Contracted from *dheə ... [Pok. 2. dhē- 235.]' — the same list Nourai cites by its 1975 New College page 1512 (roots are alphabetical over pp.1505-1550, so 'dhē-' falls in the right place); the copy on disk is the 1985 standalone reprint with different pagination."
        },
        {
          "ref": "POK:235",
          "status": "supports",
          "note": "POK_full.txt lines 22276-22510: 'Root / lemma: dʰe-2 / Meaning: to put, place, say' ... 'References: WP. I 826 ff ... Page(s): 235-239'."
        }
      ],
      "consulted": [
        {
          "src": "POK",
          "where": "pp.235-239, dʰē-2",
          "stance": "supports",
          "note": "supplies not only the root but every Iranian form of the chart: 'Avestan Old pers. data-', 'Avestan ni-δaiti- f. „laying down, putting away, hiding“', 'Avestan gao-δi- „milk container“', 'Avestan gao-δana- n. „milk container“', 'Avestan daman-, dąman- n. „site, creature“'."
        },
        {
          "src": "WLD",
          "where": "Bd. I pp.826-830 (p.828)",
          "stance": "supports",
          "note": "the parent article of Pokorny's; p.828 carries 'av. ni-δaiti- f. „das Niederlegen, Ablegen, Verbergen“', 'Ai. dhāna-m „Behälter“ ... av. gao-dana- n. „Milchgefäß“', 'av. dāman-, dąman- n. „Stätte, Wohnstätte; Geschöpf“'."
```


## [2026-09-05T20:48:19.649Z] TOOL CALL #9: Bash

```json
{
 "command": "ls data/; ls data/verification/ | head -40; ls data/verification/agent/"
}
```


### [2026-09-05T20:48:19.692Z] TOOL RESULT

```
ANOMALIES.md
extracted
EXTRACTION_SPEC.md
research
translations
verification
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
AGENT_INSTRUCTIONS.md
charts
queue.txt
```


## [2026-09-05T20:48:20.364Z] TOOL CALL #10: Bash

```json
{
 "command": "grep -rIn \"VFO\" --exclude-dir=extracted --exclude-dir=.git . 2>/dev/null | head -20"
}
```


### [2026-09-05T20:48:20.471Z] TOOL RESULT

```
<persisted-output>
Output too large (2.5MB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/tool-results/b81w5him8.txt

Preview (first 2KB):
data/translations/fa.json:741:"VFO claims these are cognates of English \"eagle\" and French \"aigle\" but does not provide any derivation.": "VFO مدعی است که این واژه‌ها با انگلیسی «eagle» و فرانسوی «aigle» هم‌ریشه‌اند اما هیچ اشتقاقی به دست نمی‌دهد.",
data/translations/fa.json:742:"VFO:18 claims these words are related to English \"pot\". Also see \"Pô 2\".": "VFO:18 مدعی است که این واژه‌ها با انگلیسی «pot» مرتبط‌اند. همچنین نگاه کنید به «Pô 2».",
data/verification/page-44.json:344:          "derivation": "Two things go wrong here. (i) The language label: arvā is not Avestan. It is a Pāzand form written in Avestan characters in the Middle-Persian Bundahišn — Horn no. 43 (HRN.txt printed p.10): 'āluh ‚Adler‘. phlv. āluh (Kārn. 59, Note 2), vergl. arvā (Bund.) in Zendbuchstaben'; Mo'in says the same at BQT p.58: «و نیز در بندهش (۱۴:۲۳) arvâ بمعنی عقاب آمده». Bartholomae's Altiranisches Wörterbuch has no arva-; the real Avestan words for 'eagle' are ərəzifya- (col. 354) and saēna-. (ii) The edge: as drawn the node descends from Latin aqua, which is impossible in both direction and family — an Iranian word cannot come out of Latin, and even as a shorthand for 'same root as' the connection fails, since Pahl. āluh/arvā goes back to PIr *Hr̥jifyáh < PIE *h₂rǵ-i-pt-ió-s (from *h₂erǵ- 'white, glittering', cf. Skt. r̥jipyá-, Gk. αἰγυπιός), not to *h₂ékʷeh₂ 'water'. Nourai's own NOTE concedes that his source VFO 'does not provide any derivation'.",
data/verification/page-44.json:348:              "ref": "VFO:15",
data/verification/page-44.json:350:              "note": "VFO = M. Ahmad Soltani, Vaj̱hgan-e Farsi dar Zabanha-ye Orupa'i, Tehran 1372/1993. refs_online.json has no record for VFO at all (value null) and no scan or copy exists in the local library or online; unverifiable. Nourai's own chart note already flags that VFO asserts the cognacy without any derivation."
data/verification/page-44.json:451:              "ref": "VFO:15",
...
</persisted-output>
```


## [2026-09-05T20:48:25.371Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"Page(s): 38[4-9]\" POK_full.txt | head -30"
}
```


### [2026-09-05T20:48:25.416Z] TOOL RESULT

```
31668:Page(s): 385-390
```


## [2026-09-05T20:48:26.078Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i \"^ger-\\|ger-2\\|ger-\\?2\\.\" AHD_watkins1985.txt | head -20; echo ===; grep -n -i \"curving, crooked\" AHD_watkins1985.txt | head"
}
```


### [2026-09-05T20:48:26.123Z] TOOL RESULT

```
Exit code 1
491:ger-?
492:TION), GENERIC, GENEROUS, GENRE, GENUS; CONGENER, (CONGENIAL), DEGENERATE, (ENGENDER), MISCEGENA- TION; b. Greek genos and genea, race, family: GENEAL- OGY, GENOCIDE, GENOTYPE, HETEROGENEOUS; c. Greek suffix -genés, ‘‘-born’”: -GEN, -GENY. 4. Suffixed full-grade form *gen-yo- in: a. Latin genius, procreative divinity, inborn tutelary spirit, innate quality: GENIAL!, GENIUS; b. Latin ingenium (in-, in; see en), inborn character: ENGINE, INGENIOUS. 5. Suffixed full-grade form *gen-d- in Latin indigena (indu-, within; see en), born in (a place), indigenous: INDIGEN, (INDIGENOUS). 6. Suffixed full-grade form *gena-wo- in Latin ingenuus (in-, in; see en), born in (a place), native, natural, freeborn: INGENUOUS. 7. Suffixed full-grade form *gen- men- dissimilated in Latin germen, shoot, bud, embryo, germ: GERM, GERMAN?, (GERMANE), GERMINAL, GERMI- NATE. 8. Suffixed full-grade form *gena-ti- in Greek genesis, birth, beginning: GENESIS, -GENESIS. 9. Redupli- cated form *gi-gn- in: a. Latin gignere (past participle genitus), to beget: GENITAL, GENITIVE, GENITOR, GENT!, (GINGERLY); CONGENITAL, PRIMOGENITURE, PROGENI- TOR, (PROGENY); b. Greek gignesthai, to be born: EPI- GENE. 10. Suffixed zero-grade form *-gn-o- in Latin benignus (bene, well; see deu-?), good-natured, kindly, and malignus (male, ill; see mel-5), evil-natured, malevo- lent: BENIGN, MALIGN. 11. Zero-grade form *gna- becom- ing *gnda- in Latin praegnds (prae-, before; see per’), pregnant: PREGNANT!. 12. Suffixed zero-grade form *gna-sko- becoming *gnd-sko- in Latin gndsci, ndsci (present participle ndscéns, past participle gndtus, nd- tus), to be born: NAIVE, NASCENT, NATAL, NATION, NA- TIVE, NATURE, NEE, NOEL; (ADNATE), AGNATE, COGNATE, CONNATE, ENATE, INNATE, NEONATE, PUISNE, (PUNY), RENAISSANCE. 13. Suffixed o-grade form *gon-o- in Greek gonos (combining form -gonos), child, procre- ation, seed: GONAD, GONO-; ARCHEGONIUM, EPIGONE. 14. Zero-grade form *gn- in Sanskrit ja- in krmi-ja-, “produced by worms” (see k*rmi-). [Pok. 1. gen- 373.] genu-'. Knee; also angle. 1. Variant form *gneu- in: a. Germanic *knewam in Old English cnéo, knee: KNEE; b. Germanic *knewljan in Old English cnéowlian, to kneel: KNEEL. 2. Basic form *genu- in Latin genii, knee: GENICULATE, GENUFLECT. 3. Suffixed variant form *gon-ya- in Greek gdnia, angle, corner: -GON, GONION; AMBLYGONITE, DIAGONAL, GONIOMETER, GONIOMETRY, ORTHOGONAL. [Pok. 1. genu- 380.] genu-2. Jawbone, chin. 1. Form *genw- in Germanic *kinnuz in Old English cin(n), chin: CHIN. 2. Basic form *genu- in Greek genus, chin: GENIAL. 3. Suffixed variant form *gna-dho- in Greek gnathos, jaw: GNATHIC, -GNATHOUS; CHAETOGNATH 4, Variant form “g(h)enu- in Sanskrit hanu, jaw: HANUMAN. [Pok. 2. genu- 381.] gep(h)-. Also gebh-. Jaw, mouth. 1. Probably Germanic *kaf-, to gnaw, chew, in Old English ceaf, husks, chaff: CHAFF!, 2. Germanic *kabraz, “gnawer,” in Old English ceafor, ceafer, beetle: CHAFER; (COCKCHAFER). 3. Ger- manic *kéfalaz in Old English céafl, jaw, cheek: JOWL!. [Pok. geph-, gebh- 382.] ger-'. To gather. 1. Extended form *grem- in Germanic *kram- in Old English crammian, to stuff, cram: CRAM. 2. Reduplicated form *gre-g- in Latin grex (stem greg-), herd, flock: GREGARIOUS; AGGREGATE, CONGREGATE, EGREGIOUS, SEGREGATE. 3. Earliest forms “ager-, *ggor-d-, in Greek ageirein, to assemble, and aguris, agora, marketplace (> agoreuein, to speak): AGORA}; (AGORAPHOBIA), ALLEGORY, CATEGORY, PANEGYRIC. [Pok. 1. ger- 382.] ger-2. Curving, crooked; hypothetical Indo-European base for a variety of Germanic words with initial kr-. I. Words meaning to bend, curl; bent, crooked, hooked; something bent or hooked. 1. Germanic *krdpp6n-, a hook, especially one used in harvesting grapes, in: a. Old High German krapfo, a hook: AGRAFFE; b. Old French graper, to harvest grapes, hence (back-formation) grape,
1219:AGIO al-1 AGITATE ag- AGLET ak- AGMINATE ag- AGNAIL angh- AGNATE gene- AGNI egni- _ AGNOMEN no-men- AGNOSIA gnd- AGO ghé- -AGOGUE ag- AGONY ag- AGORA! ger-1 AGORAPHOBIA ger-! AGRAFFE ger-2 AGRAPHA gerbh- AGRAPHIA gerbh- AGRARIAN agro- AGREE gWere-3 AGRESTAL agro- AGRIA agro- AGRICULTURE agfo- AGRIOECOLOGY agro- AGRIOLOGY agro- AGROSTOLOGY agro- AHIMSA ghei-i, ne AHRIMAN men-1
1334:CANDENT kand- CANDID kand- CANDIDA kand- CANDIDATE kand- CANDLE kand- CANDOR kand- CANESCENT kas- CANICULA kwon- CANINE kwon- CANKER kar-1 CANNABIS kannabis CANOROUS_ kan- CANT? kan- CANTABILE kan- CANTEEN kanto- CANTICLE kan- CANTILLATE kan- CANTO kan- CANTON kanto- CANTOR kan- CANVAS kannabis CANZONE kan- CAPABLE kap- CAPACIOUS kap- CAPE2 kaput CAPELLA kapro- CAPIAS kap- CAPITAL! kaput CAPITAL? kaput CAPITATE kaput CAPITATION kaput CAPITELLUM kaput CAPITULATE kaput CAPITULUM kaput CAPO! kaput CAPON skep- CAPRIC ACID kapro- CAPRICE kaput CAPRICORN kapro-, ker-1 CAPRIFIG kapro- CAPRIOLE kapro- CAPROIC ACID kapro- CAPSICUM kap- CAPSID kap- CAPSTAN kap- CAPSULE kap- CAPTAIN kaput CAPTION kap- CAPTIOUS kap- CAPTIVATE kap- CAPTIVE kap- CAPTOR kap- CAPTURE kap- CAR kers-2 CARAMEL kolem- CARAT ker-1 CARAVANSARY tere-2 CARBON ker-4 CARBUNCLE ker-4 CARCINO-  kar-1 CARCINOGEN kar-1 CARCINOMA kar-1 CARD? kars- CARDIA kerd-1 CARDIAC kerd-1 CARDIO- kerd-1 CARDOON kars- CARE gar- CAREEN kar-1 CAREER kers-2 CARESS ka- CARET kes-2 CARGO kers-2 CARICATURE kers-2 CARIES ker-5 CARILLON kWetwer- CARINA kar-1 CARIOLE kers-2 CARL karlaz CARLING karlaz CARMINATIVE kars- CARNAGE sker-1 CARNAL sker-1 CARNASSIAL_ sker-1 CARNATION sker-1 CARNET kWetwer- CARNIVAL legh-, sker-1 CARNIVOROUS = sker-1 CAROCHE kers-2 CAROL aulo- CAROTID ker-1 CAROUSE ud- CARP! ger-2 “CARP kerp- CARPAL kwerp- CARPEL kerp- CARPENTER kers-2 CARPET kerp- CARPO- kerp-
1335:-CARPOUS kerp- CARPUS kwerp- CARRION sker-1 CARROT ker-1 CARRY kers-2 CART ger-2 CARUNCLE = sker-1 CARVACROL ak- CARVE gerbh- CASCADE kad- CASCARA kwét- CASE! kad-
1398:coy kweie-2 CRAB! gerbh- CRACK gere-2 CRACKNEL gere-2 -CRACY  kar-1 CRADLE ger-2 CRAKE gere-2 CRAM ger-! CRAMBO skerbh- CRAMP! ger-2 CRAMP2 ger-2 CRANBERRY gere-2 CRANE
1399:CRANIUM ker-1 CRANK! ger-2 CRASH? ker-4 CRATE kert- CRATER kere- CRAW gWere-4 CRAWL! gerbh- CRAYFISH gerbh- CREATE ker-3 CREATINE kreue-1 CRECHE ger-2 CREDENCE kerd-1 CREDIBLE kerd-1 CREDIT kerd-1 CREDO kerd-1 CREDULOUS_ kerd-1 CREEK ger-2 CREEP ger-2 CREMATE ker-4 CREODONT kreue-1 CREOLE ker-3 CREOSOTE kreue-1, teus- CREPE sker-3 CREPITATE ker-2 CRESCENDO ker-3 CRESCENT ker-3 CRESS gras- CREST sker-3 CREVICE ker-2 CREW! ker-3 CRIB ger-2 CRIBRIFORM krei- CRICKET! ker-2 CRICOID  sker-3 CRIME krel- CRIMP! ger-2 CRIMSON k*rmi- CRINGE ger- CRINGLE ger-2 CRINITE sker-3 CRINKLE ger-2 CRINOLINE fino-, sker-3 CRIOSPHINX ker-1 CRIPPLE ger-2 CRISIS krei- CRISP sker-3 CRISPATE sker-3 CRISSUM sker-3 CRISTA sker-3 CRISTATE sker-3 CRITERION krei- CRITIC krei- CROCHET ger-2 CROCIDOLITE krek-1 CROCK! ger-2 GROCK® ger-? CROCKET ger-2 CROFT ger-2 CROMLECH léu-1, skerbh- CRONE sker-1 CROOK ger-2
1401:CROON gere-2 CROP ger-2 CROQUET ger-2 CROSIER ger-2 CROUCH ger-2 CROUP2 ger-2 CROUPIER ger-2 CROUTON kreus- crow! gere-2 cRow2 gere-2 CROWD! greut- CROWD? krut- CROWN sker-3 cRucIFY dhig’- CRUD greut- CRUDE kreue-1 CRUEL kreue-1 CRULLER ger-2 CRUMB ger-2 CRUMMIE ger-2 CRUMPET ger-2 CRUMPLE ger-2 CRUPPER ger-2 CRUSE ger-2 CRUST kreus- CRUSTACEAN kreus- CRUSTACEOUS kreus- CRUSTOSE kreus- CRUTCH ger-2 cRYO- kreus- CRYPT krau-. CRYPTIC krau- CRYPTO- krau- CRYSTAL kreus- CRYSTALLINE kreus- CRYSTALLO- kreus- CTENIDIUM pek-2 CTENOID pek-2 CTENOPHORE pek-2 CUBBY ku-
1404:CUPID kwép- CUPIDITY kwép- CUPOLA keu-2 CUPULE keu-2 CUR gere-2 CURATE cura CURATOR cira CURB sker-3 CURD greut- CURE cira CURETTE cira CURIA wWi-ro- CURIO cira CURIOUS cira CURL ger-2 CURRENT kers-2 CURRIER sker-1, CURSIVE kers-2 CURSOR kers-2 CURT sker-1 CURTAL sker-1 CURTILAGE gher-1 cuRTSY gher-* CURULE kers-2 CURVATURE sker-3 CURVE sker-3 CURVET sker-3 CUSHION koksa
1456:ENAMEL mel-1 ENAMOR amma ENANTIOMER §ant- ENANTIOMORPH ant- ENARTHROSIS at- ENATE gene- ENCAUSTIC kéu- ENCEINTE? kenk-1 ENCEPHALO- ghebh-el- ENCHANT kan- ENCHASE kap- ENCHIRIDION ghesor- ENCLAVE kleu-3 ENCLITIC klei- ENCOUNTER kom ENCROACH ger-2 ENCYCLICAL kwel-1 ENCYCLOPEDIA pau- END ant- ENDEAVOR ghabh- ENDEMIC da- ENDERGONIC werg- ENDOCARDIUM kerd-1 ENDOCRINE krei- ENDOERGIC werg- ENDORSE dorsum ENDOSTEUM ost- ENDOTHECIUM dhé-1 ENDOTHELIUM dhé@(i)- ENDOW do- ENDUE deuk-, eu-1 ENDURE deru ENEMA yé-
1565:GOAD ghei-1 GOAT ghaido- GOD gheu(e)- GODSEND sent- GOFFER webh- GOLD ghel-2 GOLIARD gWel-3 GOMPHOSIS gembh- -GON genu-! GONAD gene- GONFALON gWhen-1 GONIOMETER genu-1 GONIOMETRY genu-! GONION genu-! GONO- gena- coop ghedh- GOOSE! ghans- GORE! ghaiso- GORE? ghaiso- GORGE gWere-4 GORGET gWera-4 GORSE ghers- GOSHAWK ghans- GOSLING ghans- GOSPEL spel-3 GOSSIP s(w)e- GOUACHE akWa- GOWAN ghel-2 GRAB! ghrebh-1 GRABEN ghrebh-2 GRACE gWera-3 GRACKLE gera-2 GRADE ghredh- GRAFFITO gerbh- GRAIN gre-no- GRAM! § gerbh- GRAM? gre-no- -GRAM gerbh- GRAMA gras- GRAMINEOUS_ gras- GRAMMAR gerbh- GRAMPUS_peisk- GRANADILLA gfe-no- GRANARY gre-no- GRANDILOQUENCE tolkw- GRANGE gre-no- GRANITE gr@-no- GRANT kerd-1 GRANULE gre-no- GRAPE ger-2 GRAPH gerbh- -GRAPH gerbh- -GRAPHER gerbh- GRAPHIC gerbh- GRAPHITE gerbh- -GRAPHY gerbh- GRAPNEL ger-2 GRAPPA ger-2 GRAPPLE ger-2 GRASP ghrebh-1 GRAss_ ghré- GRATE! grat- GRATE? kert- GRATEFUL gWere-3 GRATIFY gWere-3 GRATIS gWera-3 GRATITUDE gWero-3 GRATUITY gWera-3 GRAUPEL kreup- GRAVE! ghrebh-2 GRAVE? gwWera-2 GRAVES ghrebh-2 GRAVEL ghréu- GRAVID gWera-2 GRAVURE ghrebh-2 GRAY gher-3 GRAYWACKE wegh-
1567:GREAT ghréu- GREAVES ghrebh-2 GREEDY gher-5 GREEN ghré- GREET gher-2 GREGARIOUS ger-1 GRENADE gre-no- GRESSORIAL ghredh- GREYHOUND gher-3 GRID kert- GRIDDLE kert- GRIDIRON kert- GRIEF gWera-2 GRIEVE gWere-2 GRIM ghrem- GRIMACE ghrem- GRIME ghréi- GRIND ghrendh- Grip! ghreib- GRIPE ghreib- GRIPPE ghreib- GRISAILLE gher-3 GRISEOUS gher-3 GRISETTE gher-3 GRISLY ghréi- GRISON gher-3 GRisT ghrendh- GRIT ghréu- GRIZZLE gher-3 GROAT ghréu- GROATS ghréu- GROCER gWres- GROOVE ghrebh-2 GROPE ghreib- GROSCHEN gWres- GROSS gWres- GROSSULARITE ger-2 GROSZ gWres-
1726:LAAGER legh- LABEL leb-! LABELLUM leb-2 LABIAL leb-2 LABILE leb-1 LABIUM leb-2 LABOR leb-1 LABRET leb-2 LABRUM leb-2 Lac! reg-3 LACCOLITH laku- LACERATE |@k- LACHRYMAL dakru- LACINIATE l@k- LACK leg-2 LACROSSE ger-2 LACTATE melg- LACTEAL melg- LACTESCENT melg- LACTO- melg- LADDER Klei- LADE kla-
(eval):1: == not found
```


## [2026-09-05T20:48:31.593Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('AHD_watkins1985.txt',encoding='utf-8',errors='replace').read()\ni=t.find('ger-2. Curving, crooked')\nprint(t[i:i+6000])\nEOF"
}
```


### [2026-09-05T20:48:33.489Z] TOOL RESULT

```
ger-2. Curving, crooked; hypothetical Indo-European base for a variety of Germanic words with initial kr-. I. Words meaning to bend, curl; bent, crooked, hooked; something bent or hooked. 1. Germanic *krdpp6n-, a hook, especially one used in harvesting grapes, in: a. Old High German krapfo, a hook: AGRAFFE; b. Old French graper, to harvest grapes, hence (back-formation) grape,
gerbh-
vine, grape: GRAPE; c. Old French grapon, grapnel: GRAPNEL; d. Old French grape, a hook: GRAPPLE; e. Ital- ian dialectal grappa, vine stem, brandy: GRAPPA. 2. Old English crump, crumb, crooked, bent, stooping: CRUM- MIE, CRUMPET, (CRUMPLE). 3. Low German krimpen, to wrinkle: CRIMP!. 4. Middle Dutch crampe, hook, and Frankish *kramp, hook: cramMpP?. 5.Old High German krampfo, a cramp, akin to the Germanic source of Old French crampe, cramp: CRAMP!. 6. Old English crypel, a cripple: CRIPPLE. 7. Germanic *kreupan in Old English créopan, to creep: CREEP. 8. Middle Low German krink, a ring: CRINGLE. 9. Germanic *krengan in Old English cringan, to yield: CRINGE. 10. Middle Dutch crinkelen, akin to Middle English crinkelen, to make kinks in: CRINKLE. 11. Old Norse kriki, a bend, nook: CREEK. 12. Old Norse krékr, a hook: cRooOK. 13. Frankish *krok- (> Old French croc), a hook: CROCHET, (CROCKET), (CROQUET), (CROUCH); ENCROACH. 14. Old English crycc, (bent) staff, crutch: CRUTCH. 15. Old French crosse, crook: CROSIER, LACROSSE. 16. Middle Dutch crulle, curly: CRULLER, CURL. 17. Old English cranc-(stzf), a weaving implement: CRANK}. 18. Norwegian krake, a sickly beast, akin to the source of Middle English crok, an old ewe: cRocK3, 19. Old Norse karpa, to boast: CaRP!, 20. Middle Dutch kroes, curled, akin to the source of Old French grosele, gooseberry: GROSSULARITE. II. Words meaning ‘“‘a rounded mass, collection; a round object, vessel, container.” 1. Old English cruma, a frag- ment: CRUMB. 2. Frankish *kruppa, rump, akin to the Germanic source of Old French croup, rump: CROUP?, (CROUPIER), CRUPPER. 3. Old English cropp, cluster, bunch, ear of corn: crop. 4. Italian gruppo, an assem- blage: Group. 5. Old English crocc, pot: CROCK}. 6, Mid- dle Dutch cruyse, pot: CRUSE. 7. Old English cribb, manger: CRIB. 8. Old English cradel, cradle: CRADLE. 9. Frankish *kripja, cradle, akin to the Germanic source of Old French cre(s)che, crib: CRECHE. 10. Old English creet and Old Norse kartr, wagon: CART. 11. Old English croft, small enclosed field: crort. [Pok. 3. ger- 385.] gerbh-. To scratch. 1. Germanic *kerban in Old English ceorfan, to cut: CARVE. 2. Zero-grade Germanic form *kurbiz in Old English cyrf, a cutting (off): KERF. 3. Variant form *grebh- in: a. Germanic *krab(b)- in Old English crabba, a crab: CRAB}; b. Germanic *krabiz- in Old French crevise, crayfish: CRAYFISH; C. perhaps Ger- manic *krab- in Old Norse krafla, to crawl: CRAWL. 4. Zero-grade form *grbh- in Greek graphein, to scratch, draw, write, and gramma (< *grbh-mn), a picture, writ- ten letter, piece of writing, and grammé, a line: GRAF- FITO, GRAM!, -GRAM, GRAMMAR, GRAPH, -GRAPH, -GRAPHER, GRAPHIC, -GRAPHY; AGRAPHA, AGRAPHIA, DIAGRAM, EPIGRAM, (EPIGRAPH), GRAPHITE, ICONOGRA- PHY, PARAGRAPH, PROGRAM, PSEUDEPIGRAPHA, TETRA- GRAMMATON, TOPOGRAPHY. [Pok. gerebh- 392.] [gerere. To carry, carry on, act, do. Latin verb of un- known origin. Oldest form ges-, past participle gestus. GERENT, GERUND, (GEST), GESTATION, (GESTICULATE), GESTURE, JEST; ARMIGER, BELLIGERENT, (CONGERIES), CONGEST, DIGEST, EGEST, INGEST, REGISTER, SUGGEST, VELIGER.] gere-'. To grow old. 1. Suffixed lengthened-grade form *géro-s- in Greek géras, old age: AGERATUM, CALOYER, GERIATRICS. 2. Suffixed form “gera-ont- in Greek geron (stem geront-), old man: GERONTO-. [Pok. ger- 390.] gere-2. To cry hoarsely; also the name of the crane. I, Words meaning “‘to cry hoarsely”; also words denoting the crow. 1, Germanic *kré- in: a. Old English crawe, a crow: CROW}; b. Old English crdwan, to crow: CROW?; c. Old English cracian, to resound: CRACK; d. Middle Dutch krdken, to crack: CRACKNEL; @. Old Norse kraka, a crow: CRAKE. f. Middle Dutch krdnen, to groan, la- ment: CROON. 2. Possibly (but more likely imitative) Germanic *kur(r)- in Old Norse kurra, to growl, akin to Middle English curre, cur: cur. II. Words denoting a
20
ghait-
crane. 1. Germanic *kran-, crane, in: a. Old English cran, crane: CRANE; b. Middle Low German kran, crane: CRANBERRY. 2. Extended form *grd- in Latin griis, crane: GRUS; PEDIGREE. 3. Suffixed variant form *gra-k- in Latin grdculus, jackdaw: GRACKLE. 4. Suffixed ex- tended form *gero-no- in Greek geranos, crane: GERA- nium. [Pok. 2. ger- 383.]
géu-. To bend. Proposed by some as the root of Greek guros, ring (which is more likely of unknown origin): GYRE, GYRO?, GYRO-; AUTOGIRO. [Pok. géu- 393.]
geue-. To hasten. Possibly the base of Germanic *kaur- Jan in Old Norse keyra, to drive: SKIJORING. [Pok. geu- 399.]
g(e)u-lo-. A glowing coal. Germanic *kulam, *kolam in: a. Old English col, a glowing coal: COAL, (COLLIE), (COL- LIER); b. probably dialectal Old French cholle, round lump, head: cHOLLA. [Pok. g(e)u-lo- 399.]
geus-. To taste, choose. 1. Germanic *keusan in: a. Old English céosan, cedsan, to choose: CHOOSE. b. Gothic *kausjan, to choose: CHOICE. 2. Zero-grade *gus- in Germanic *kuz-, becoming *kur- in Old Norse Valkyrja, “chooser of the slain,” Valkyrie (valr, the slain; see wele-2). 3. Suffixed zero-grade form *gus-tu- in: a. Latin gustus, taste: (GUST?), GUSTO; DISGUST, RAGOUT; b. Latin gustdre, to taste: DEGUST. [Pok. geus- 399.]
ghabh-. Also ghebh-. To give or receive. 1. Form *ghebh- in Germanic *geban in: a. Old English giefan, to give: GIVE; b. compound *far-geban (*far-, away; see per'), to give away, in Old English forgi(e)fan, to give, give up, leave off (anger), remit, forgive: FORGIVE. 2. Suf- fixed form *ghebh-ti-, something given (or received), in Germanic “giftiz in Old Norse gipt, gift, a gift: GIFT. 3. O-grade form “*ghobh- in Germanic *gab-ulam, some- thing
```


## [2026-09-05T20:49:05.001Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('POK_full.txt',encoding='utf-8',errors='replace').read()\ni=t.find('Page(s): 385-390')\nprint(t[max(0,i-16000):i+300])\nEOF"
}
```


### [2026-09-05T20:49:06.755Z] TOOL RESULT

```
^bend, bay', -kr/k/{irom which Middle English cr/ke, 
creke, nengl. creek) " curvature, bay'; 

perhaps Latvian gredzens^uv\Q\ 

b. In Indo Germanic -k. Old Church Slavic shgrbciti s§^ draw together, collect, 
assemble ', Bulgarian girca se' bend, curve, crook, pull myself together ', ^B/ra 'wrinkle', 
zg-brcen^ withered, shriveled, shrunk, dwindled ', serb. ^/r 'cramp'. 

Maybe nasalized alb. ngerg' cramp', ngerth 'k\nk', ngerthej, kthej 'turn', ktheter^ c\a\N' = 
Old Indie granth-, grathnami. Put. granthisyamT coil, bind, wind, tie, knot, fasten, join, 
attach, tie a knot ' (common -k > -th Albanian Celtic Old Indian) see below. 

Maybe alb. m. grethi, f. grenza' wasp, insect sriped with rings '. 

Maybe alb. gersheV plait, braid, three or more interwoven strands (of hair) ', Geg 
gershana, Tosc gershere ' scissors for cutting the braid '. 

Note: 

In Alb. highland it was a taboo cutting the hair, hence men like Aryan Persians had long 
hair = an old custom of matriarchy when men identified themselves with the mother 
goddess. In South Albania men still wear a womanish kilt like Scottish Celts. 

c. Nasalized: 



In Indo Germanic -Ar certainly Old Norse Ara "point, edge, angle ' {*krarihd) and probably 
also Germanic forms in -g. Old Norse kringrm. 'ring' = Middle High German krinc, -ges 
"ring, battlefield'. Modern High German Kring, Old Norse kringla^ ring of a circle, circle, 
compasses, instrument for drawing circles and measuring, calipers ', Middle Low German 
kringel(e)^r\v\i^, round pastry, cake ', Middle High German kr/nge/{an6 changing through 
ablaut krengel) ds.. Modern High German Kringef, Middle High German kranc, -ges' 
circle, ring, district, region, area ', Modern High German Swiss chranger curvature ', 
Middle High German krange/'nee6, tribulation' (from 'entanglement, curvature ') and "ring, 
circle'; Old Norse cranga " grovel, truckle, creep, trudge, lumber ', with figurative meaning 
krangr'^eak, fragile, easily broken; unstable, dilapidated '; Old English cr/nganlaW; 

in Indo Germanic -g: Old English cranc-staer a weaver's device ', crencestre' weaver ', 
Middle English crinkled' twiddled, twisted, rotated, revved, revolved ', engl. cr/nk/e'bend, 
curvature, crease, rumple, wrinkle; make a rustling sound ', crank' lever, handle, curvature 
' (as Modern High German Swiss chrank), older also cranke' spool ', mndd. krunke' 
crease, wrinkle, frill, ruffle; frizziness, curliness; ruff, holl. kronkeF crease ', krinkel' loop, 
noose, snare, crease, wrinkle', Norwegian krenkja " dislocate, luxate, crick '; with the 
meaning-development to " bent from disease, malady ': Old High German krankolon " 
stumble, trip; transgress, go astray, lose one's way, become weak ', Middle High German 
krank' narrow, tight, slim, slender, thin, small, weak'. Modern High German krank. Old 
English cranc'weak, fragile, easily broken; unstable, dilapidated ', as well as Old English 
crincan' fall in battle, die in battle, die in combat, die in war'("*bend in agony'); 

in Indo Germanic -^(not -^ point at Baltic *grenzid' turn, twist, rotate ' in Lithuanian 
gr^ziu, gr^ztT turn, twist, rotate, drill, wimble, bore a hole ' (Iter, gr^zyti), gr/ztu, grizti' 
retrovert, turn back, return, go or come back ', grjzte' roll of flax ' = Latvian grTzte " the 
twisted together ', Latvian griezu' turn, rotate ' (= Lithuanian gr^ziu), Lithuanian grqztas 
"borer'. Old Prussian granst/s6s. (Lithuanian gr^zulas' shaft, pole, rod, beam; long 
revolving bar used to transfer motion or torque to gears or other parts ' presumably 
likewise from " cord, rope, hank, halter, rope with a noose for hanging criminals '). 

2. Dental extensions: 

a. gr-et{h)-: 0\d English cradolm. " cradle ' {*kradula-' the plaited '), Old High German 
Ara/Zo "basket' {*kraddan-), krezzo. Middle High German krezze. Modern High German 
Kratze " pannier ' ( *krattian). (common -k > -th Albanian Celtic Old Indian) 

b. Nasalized: 



Old Indie granth-, grathnami, Fut. granthisyamr coil, bind, wind, tie, knot, fasten, join, 
attach, tie a knot ', participle grath/ta-^\N\nde6, knotty, conglobated', granthf-hm. "knot, 
joint, intumescence ', grantha-h 'knot', grath/n- 'sc\r\em\ng, deceptive', grath/'/a- 'ray\ng, 
mad'; but ghata- "bulk, mass, troop, multitude, crowd' is not a root. (Kuiper Proto-Munda 
55 f.). (common -k > -th Albanian Celtic Old Indian) 

c. ger-d, gr-ed-, nasalized grend-: 

Old Irish grinne {*grend-n-io-) "bundle, fagot, bunch, fascis'; (common Celtic -ns-, -nt- > 
nn-). 

Old Norse kartr. Old English crgetxw. " cart ' (probably " twisted carriage basket '), 
probably also Old Norse kart-nagF deformed, twisted nail', Norwegian kartm. " unripe 
fruit, knag'. East Frisian /rAe/ "shrunk fruit'. Middle High German Are/7ze "basket'. Old High 
German kranz. Modern High German Kranz, 

Lithuanian grand/'s {reduced grade grundis) " bracelet, iron ring, hoarfrost of wheel, 
round cheesecake ', Old Prussian grandis " the ring in the plow which connects the plow 
crossbeam with the front rack ', Latvian gruods' s\bxV. twiddled, twisted, rotated, revved, 
revolved, drall'; 

poln. grQdacsiQ' turn, rotate '. 

3. Labial extensions: 

a. ger-b\ gr-dd^-: 

Old Indie grapsa-h, glapsa-h " bundle, tussock ', next to which with Middle Indie 
development from * grpsa-h guccha-h and as hypersanskrit. back-formation gutsa-h' 
tussock, bundle, bunch '; belongs probably better to S. 455. 

Middle High German kreberw. {*kreban-) "basket; intestines, entrails ', Old Saxon 
kribbia. Old High German krippa. Old English cribb " crib, manger ', in Modern High 
German (and Holl.) also " wattle fence on shores, fish snaring net, verge of a roof with 
brushwood bundles ' (^^^^H additional form Middle Low German krubbe, Old English 
cryb; with Germanic -pp-: Modern High German Swiss chrup(e) " crib, manger ', as on the 
other hand also Old High German kripfa); 

Middle Low German kerve' weir, net'. Old Norse kiarf, kerf(i)v\. "bundle, fascicle, sheaf. 
Old Swedish kaerve' grain bundle, fascicle, sheaf, Swedish dial, /ra/v" basket', isl. karfa, 



korv'baskeV (but Modern High German Korb, Middle Low German /ro/fnevertlieiess 
probably only loanword from Latin corbis). 

In addition behaves perhaps gr. ypTcpo(; " shopping bag, fishing net; somewhat 
complicated, riddle ' (whereas with n: ypTno(; "fishing net', ypTn£U(; ' fisherman '), as scr- 
Tbo, aKap-T-(po(; to *5Ae/"-"cut, clip'. 

b. gertj-, with revelation of the meaning " crinkle, wrinkle, shrivel, shrink due to excess 
dryness, wrinkle up, cramp ', but also for other kinds of of bending: 

Old Irish ^eA-^ac/? "wrinkly'; 

Old Prussian ^aA-^/s 'mountain', Lithuanian garbana {see below) and garbanai. " hair 
lock '; 

Maybe poln. garble si^^io hump' : alb. kerrus'to hump', kurriz\ hunchbacked) spine' 

Note: 

Root / lemma: ger-3\ "to turn, wind' : Root/ lemma: (s)ker-3\ "to turn, bend'. 

in addition ablaut. Old Church Slavic grbbt "dorsum, cramp', grbbo-nos'b " crooked- 
nosed ', russ. gorb^ hump, hunchback, hunch, outgrowth, elevation, back', sloven, grb, 
g'rba^ hunch, hump, hunchback, wrinkle', grbatT make hunchbacked, crook, furrow '; 

nisi, korpai. "wrinkle, crease ', korpna^ contract, shrivel '; 

a heavy basis, perhaps *ger9b- (?), seems the base from Armenian karth " fishhook, 
hook; knee bow, popliteus, shinbone, leg' {*gfpti-) and Lithuanian garbanat " curl '; 
Berneker 368. 

c. Nasalized: 

Old High German krim(p)fan. Middle High German krimpfen. Middle Low German 
krimpen^ shrink up, shrink ' = Old Norse kreppa {krapp) "pull together'. Middle High 
German kr/mpr crooked; cramp'; Old English crompeM' crumpled, wrinkled ', Old High 
German krampf writhed, crooked, humped ', substantivized krampf(o)^ crarc\'^\ krampf 
hook ', ndd. (and as loanword Modern High German) Krampe^ hook for closing ', Old 
Saxon Ar5/r7/7^c»y) "cramp', Kaus. Middle High German krempfen {*krampjan) = Old Norse 
kreppa {sc\r\\N. V.) "pull together'. New Swedish krumpen^ wizened ', Old Norse kropna 



{*krumpna) " shrink up, become stiff, Old English crump, Old High German krumpf 
writhed, crooked, humped '. 

Besides Old English crumb. Old Saxon krumb. Old High German krump. Modern High 
German krumm presumably for Indo Germanic ^-root from gr. YPUfjnavsiv vpunouaGai, 
auYKaijnTEiv Hes., yPutt6(; "crooked' (see S. 389 under B. 2.); 

Latvian grumbf gotten wrinkled ', grurnbulatns^ jolting '; 

Maybe alb. grumbullonJ^'^vW together', grumbulF'^We, heap' 

Lithuanian grumbu, grubau, ^/'i/M(analogical nasalized form for *grumbau, *grumbti) " 
jolting, hard or become insensible ', grubus {ior *grumbus) " jolting, hard'; 

Old Church Slavic ^/ipi6'b'i5iu)Tr|<;, unlearned, untaught, ill-mannered ', russ. grubyj 
"rough, coarse, raw', poln. ^/ig-i?/ 'wrinkly, rough, adverse ', poln. grqba, gr^bai. 'elevation, 
hill, boundary '; 

d. grep- or gfejrsp- {compare above S. 387 *ger9b-) in Middle Low German krappe 
'hook, claw, talon '; 

maybe alb. grep^Y^ooV^ 

holl. krapi. 'cramp'. Old High German krapfo^bev\\. claw, talon, hook'. Modern High 
German Krapfen^ hook; pastry of such form ' (Germanic pp, besides Germanic -bb- in:) 
Old High German krapo. Middle High German krape'hook', Swedish dial, krab be '\r\ookior 
the search in water '; 

maybe alb. Geg krrabe, Tosc kerrabe^ crookeA stick of the shepherd' 

Old Norse krappr^ or\<^ , holl. krap6s.. Modern High German Bavarian krapf 
'unprepossessing, small', Swiss chrapf strong' ('*thickset)'; Old High German Modern 
High German Kraff{irorr\ cramping the muscles). Old Saxon kraff. Old English craefV 
power, skillfulness, art ', Old Norse krgptr, kraptrm. ' power, witchcraft ', compare Old 
Norse krgfi. ' demand ', Are^a 'arrogate'. Old English crafianAs.; Norwegian kravrw. ' Ice 
crust ' (besides Old Norse krapr\., krapiru. ds.; 'wither, shrivel, shrink due to excess 
dryness, wrinkle up '; nord. -p- probably for root form with Indo Germanic b). 

4. 5-extension *gre-s-, only Germanic: Old High German kresan^ grovel, truckle, creep ', 
Norwegian Dialectal krasen 'weak, frail '; presumably Old Saxon Old High German kresso 



' goby, small fish ', Modern High German Kresse, Kress//ng 6s.; *ger-s- probably in 
Norwegian karra^ shrivel, shrink due to excess dryness, wrinkle up, friz, curl '. 

Besides from the /-extension *gr-ei-2\so *gr-ei-s-\v\ Middle High German krJsen, kreis^ 
grovel, truckle, creep '. 

B. root form gr-eu-\ gru-mo-^ scraped together ': 

gr. YpO ' little dirt under the nail ' (i.e. ' what settles while scratching under the nail '); 

Norwegian kryr hump, hunchback ' {*kru-li-? *kruvila-'7), dial, also skryl, kryla^ 
KrummriJckig sein ' (also gryla), Swedish dial, krylas i hop^ creep together ', Norwegian 
dial. krylt{grylt, skrylt) " hunchback person' (the forms with g- belong together with Old 
Norse grufa^ sich vornijberbeugen, auf der Nase liegen ', Modern High German Swiss 
gruben, groppen, gruppen ' crouch down, stoop ' to a versch. root with Germanic g-)\ 

with the meaning ' crooked claw, talon, mit gekrallten Fingern zusammenscharren ': Old 
Saxon krauwil. Old High German krouwiT claw, talon, fork with crooked points ', Modern 
High German KrauelAs., Old High German krouwon. Modern High German krauen. Old 
Frisian krawia aciuaWy " scratch, scrape with crooked fingers '; 

with formants -/770-;gr. ypO|j£a, -eia, -aia "junk, trash, trumpery, offish small fry, also 
pouch, bag or chest for old clothes ' (similarly the /^-derivative ypuTr) 'junk, offish small fry, 
woman's dressing-case or vanity-bag, prob. a workman's tool-bag, frippery ', ypOToSoKn 
"lumber room'), actually " scraped together '; 

Latin grumus^ a little heap, hillock of earth ' (as earth scraped together); 

Middle High German Modern High German Krume; with Cr. Old English crumam., mnl. 
krume (ablaut, krome), holl. kruim " crumb ' ("what one scratches from the hard crust '), isl. 
krumr, kraumr, Swedish kram, inkram {inkrom) " intestines, entrails of birds and fish, 
crumbs '. 

1. guttural extension greu-g-\n. Old Irish gruc, nir. ^/i/^ "wrinkle' {*gruggu-), Middle Irish 
grucanach^ corrugated '; 

maybe alb. {*greu-g-) krunde^ crumb, bread crumbs ' common alb. -g- > -d-. 

Old High German kriochan^ grovel, truckle, creep ', Modern High German kriechen, 
ablaut, krauchen^ duck, slip, crouch, grovel, truckle, creep ', Krauch^ road curve ' (Middle 
English crouchen, engl. crouch "duck, stoop', is French loanword). Middle Dutch kroke 



'wrinkle, crease ', holl. kreuk ds. {*kruki-), Middle Dutch crooc' hair lock ' ( *krauka-), 
Norwegian krjuka {krauk-) " shrink up, grovel, truckle, creep ', kruka^ crouch, squat ', 
kr0kla, krykla^ crippled tree, invalid creature, osseous fragility '; in addition probably as 
"staff with crooked handle, grasp' Norwegian dial, krykkia. Old English crycei., nengl. 
crutch. Old High German krucka. Middle High German krucke, asachs. krukka " crutch ' 
(Germanic *krukjd)\ perhaps Middle High German M/c/?© (Modern High German Krauche), 
Old Saxon kruka. Old English c/t7ce "crock, pitcher' (compare above Old High German 
kruog). Old English crocc, crocca. Old Norse krukka'pot, pan', therefore certainly also old 
close relationship to gr. Kpiooodq "crock, pitcher' from *Kpu)Ki6q (about Old High German 
kruser crucible, melting pot ' etc. s. Falk-Torp under krusm. addendum) stands to the 
consideration. About Modern High German Kriechbaum s. Kluge'''' under Krieche. 

2. Labial extensions: 

greu-p-:QX. ypunoq " hook-nosed, aquiline, hooked, writhed, crooked, humped, with a 
curved nose ', ypOnou) " bend, crook ', ypuijj, ypOnoq m. " griffin (Griffin (after the crooked 
beak and the crooked claws), a bird, part of a ship's tackle, or anchor '), nasalized 
YpupnavEiv ypunouoGai, ouyKapnTSiv Hes., wherefore probably at first Old English etc. 
krumb^ crooked' (see above S. 387). 

greu-b-:here perhaps Scots Gaelic groban "top or point of a hill' {*grubb-)\ 

Old Norse krjupa. Old English creopan. Middle Low German krOpen^ grovel, truckle, 
creep ' ("*curve like a worm '), Old English cryppan^ba\N, bend'. Modern High German 
Dialectal sich krupfen " crook oneself ' (Swiss chrupfen "somewhat a bit bend so that it 
gets a roundish deepening '), Middle Low German kroppen^ bend crooked ', Norwegian 
kr0ypa {*kraupjan) "crook'; Old Norse kryppai. " hump, hunchback ', kryppil. Old English 
cryper cripple ', Middle Low German kropelds. (holl. kreupef. Middle High German 
krup(p)el. Modern High German Kruppelirom Ndd.), zero grade Old English creeper 
cripple '; Old English crepp^ bundle of berries or flowers, ear, goiter, crop '; with 
expressive intensification: Old High German krepf crop, bird's head ', Middle Low 
German Ayo/? "swelling, blister, hunch, outgrowth, crop. Bird's head; trunk, (toter) body', 
only in latter meaning Old Norse /r/'o/?/?/'" trunk'; 

maybe alb. Geg kryja, Tosc krye^ (round) head ' 

with simple it'.OId Norse krefu. "trunk, killed animal body ', kryfia^ disembowel '; a *krufta- 
" curvature, hill' in Middle Dutch krechf\\\\\, farmland, field in the dunes ', Old English creft 
"small field'; 



Lithuanian probably ^mit*//?©//" stagger, stumble', grub(l)asxr\. "rough bumpiness, hillock'. 

3. s- Extension greu-s-:W\66\e High German Middle Low German M7s' frizzy, curly '; 
Middle Low German kruse " chitterlings, belly fat' ('*the frill, ruffle '); with Germanic -au- 
ndd. kros^ Intestine of geese ', Middle High German (ge)kroese. Modern High German 
Gekrose, ndd. kruse {*krusi-) "wrinkle, crease, furrow, curl ', holl. kreus^ fold in staves '; 
Old English cress "dainty'. West Frisian kreas^ frilly '; Old High German Middle High 
German krol{-lf-) " frizzy ' {*kruzla-). Middle High German krol(le), krulle^ curl ', Norwegian 
kru//6s.; Norwegian Dialectal kruslen, krusken^ frail ', ndd. krusch' curled ', Middle High 
German krusp^ frizzy ', Modern High German obd. krausC frizzy '. 

References: WP. I 593 ff., WH. 623, Trautmann 94 f., 97, 99 f. 
Page(s): 385-390 

Root / lemma: ger-4, grei- 
Meaning: to grow; to awake 

Material: Old \r\d'\c jarate ' awakened', ja-gar-t/^ wakes', Perf. ja-gara, part\c\p\e ja-gr-vams- 
"alert, awake, smart, keen, eager' , Jagrv/- ^ attentive, sleepless, alert, awake, smart', av. 
jayarayantam^ the watching o
```


## [2026-09-05T20:49:13.758Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('POK_full.txt',encoding='utf-8',errors='replace').read()\ni=t.find('Page(s): 385-390')\nj=t.rfind('Root / lemma: ger-3',0,i)\nprint(t[j-200:j+2500])\nEOF"
}
```


### [2026-09-05T20:49:15.552Z] TOOL RESULT

```
inkly'; 

Old Prussian ^aA-^/s 'mountain', Lithuanian garbana {see below) and garbanai. " hair 
lock '; 

Maybe poln. garble si^^io hump' : alb. kerrus'to hump', kurriz\ hunchbacked) spine' 

Note: 

Root / lemma: ger-3\ "to turn, wind' : Root/ lemma: (s)ker-3\ "to turn, bend'. 

in addition ablaut. Old Church Slavic grbbt "dorsum, cramp', grbbo-nos'b " crooked- 
nosed ', russ. gorb^ hump, hunchback, hunch, outgrowth, elevation, back', sloven, grb, 
g'rba^ hunch, hump, hunchback, wrinkle', grbatT make hunchbacked, crook, furrow '; 

nisi, korpai. "wrinkle, crease ', korpna^ contract, shrivel '; 

a heavy basis, perhaps *ger9b- (?), seems the base from Armenian karth " fishhook, 
hook; knee bow, popliteus, shinbone, leg' {*gfpti-) and Lithuanian garbanat " curl '; 
Berneker 368. 

c. Nasalized: 

Old High German krim(p)fan. Middle High German krimpfen. Middle Low German 
krimpen^ shrink up, shrink ' = Old Norse kreppa {krapp) "pull together'. Middle High 
German kr/mpr crooked; cramp'; Old English crompeM' crumpled, wrinkled ', Old High 
German krampf writhed, crooked, humped ', substantivized krampf(o)^ crarc\'^\ krampf 
hook ', ndd. (and as loanword Modern High German) Krampe^ hook for closing ', Old 
Saxon Ar5/r7/7^c»y) "cramp', Kaus. Middle High German krempfen {*krampjan) = Old Norse 
kreppa {sc\r\\N. V.) "pull together'. New Swedish krumpen^ wizened ', Old Norse kropna 



{*krumpna) " shrink up, become stiff, Old English crump, Old High German krumpf 
writhed, crooked, humped '. 

Besides Old English crumb. Old Saxon krumb. Old High German krump. Modern High 
German krumm presumably for Indo Germanic ^-root from gr. YPUfjnavsiv vpunouaGai, 
auYKaijnTEiv Hes., yPutt6(; "crooked' (see S. 389 under B. 2.); 

Latvian grumbf gotten wrinkled ', grurnbulatns^ jolting '; 

Maybe alb. grumbullonJ^'^vW together', grumbulF'^We, heap' 

Lithuanian grumbu, grubau, ^/'i/M(analogical nasalized form for *grumbau, *grumbti) " 
jolting, hard or become insensible ', grubus {ior *grumbus) " jolting, hard'; 

Old Church Slavic ^/ipi6'b'i5iu)Tr|<;, unlearned, untaught, ill-mannered ', russ. grubyj 
"rough, coarse, raw', poln. ^/ig-i?/ 'wrinkly, rough, adverse ', poln. grqba, gr^bai. 'elevation, 
hill, boundary '; 

d. grep- or gfejrsp- {compare above S. 387 *ger9b-) in Middle Low German krappe 
'hook, claw, talon '; 

maybe alb. grep^Y^ooV^ 

holl. krapi. 'cramp'. Old High German krapfo^bev\\. claw, talon, hook'. Modern High 
German Krapfen^ hook; pastry of such form ' (Germanic pp, besides Germanic -bb- in:) 
Old High German krapo. Middle High German krape'hook', Swedish dial, krab be '\r\ookior 
the search in water '; 

maybe alb. Geg krrabe, Tosc kerrabe^ crookeA s
```


## [2026-09-05T20:49:19.693Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"ger-3\" POK_full.txt | head; echo ===; python3 - <<'EOF'\nt=open('POK_full.txt',encoding='utf-8',errors='replace').read()\nimport re\nfor m in re.finditer(r'Root / lemma: ger-3', t):\n    print(m.start(), repr(t[m.start():m.start()+400]))\nEOF"
}
```


### [2026-09-05T20:49:21.716Z] TOOL RESULT

```
Exit code 1
31336:Root / lemma: ger-3 
31503:Root / lemma: ger-3\ "to turn, wind' : Root/ lemma: (s)ker-3\ "to turn, bend'. 
(eval):1: == not found
```


## [2026-09-05T20:49:23.698Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '31330,31360p' POK_full.txt"
}
```


### [2026-09-05T20:49:23.756Z] TOOL RESULT

```
In addition perhaps russ. gr6chot^6\v\, fuss, noise, crash, blast, loud laughter' as new 
onomatopoeic words. 

References: WP. I 591 ff., WH. I 583, 601 f., 615, 624, Specht Dekl. 48, Trautmann 87, 94. 
Page(s): 383-385 

Root / lemma: ger-3 

Meaning: to turn, wind 

Material: A. Old Indie guna-h ( *gr-n6-s) " the single thread of a string, line, cord; stain ' {dvi- 

, //7-^i//7a- actually " consisting of two, three threads '); 

Maybe alb. guna^ fleecy attire of the shepherd ' 

Old Indie garta-h " carriage seat of the chariot' ('*from rods twisted seat, carriage basket '), 

compare with formants -/770-Old Norse karmr^ parapet, defensive wall, protective wall in 

front of a trench ', Swedish karm " back, part of a chair support from wickerwork, carriage 

basket ' (*gor-mo-s^ wickerwork '). 

1. guttural extensions: 



a. In Indo Germanic -g. presumably gr. YupYC(66(; " wicker-basket, creel, twisted basket 
from willows, weir, fish-snaring net ' (-u-reduced vowel, ending as in kqAqGoc; ' basket 
narrow at the base, esp. for wool, for fruit, (carried in procession in honour of Demeter),
```


## [2026-09-05T20:49:32.084Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== PHD grih/grōh\"; grep -n -i \"grih\\|gr[oō]h\" PHD.txt PHD_mackenzie.txt | head -20; echo \"== NYB\"; grep -n -i \"grih\\|glyh\\|gr[oō]h\" NYB_vol2_glossary.txt | head -20; echo \"== HRN\"; grep -n -i \"girih\\|gih\\|Knoten\" HRN.txt | head -25"
}
```


### [2026-09-05T20:49:32.165Z] TOOL RESULT

```
== PHD grih/grōh
PHD.txt:382:*g5k4n [gwk’n'] details. Lc um ~ig [-yk'] detailed; precisely. (sassa tu) ģūmēz [gwmyc | N giméz] bull's urine (as ritual purifier). ģgūmēz- [gwmyc- | N giméz-] urinate. gön [gwa' | N gün] colour, complexion. ~ag [-k' | M geng, N güna] = gön ; sort, kind, form. gor [gwl | N ~] onager, wild ass. göspand [K YNA < А апу ? ; gwspnd | N ~] (small) cattle, sheep. ~-tihrag [-cyhlk'] holding the seed of cattle. ģūstān [gwst^n!] cattle-stall, cowshed. 1858 [gws | = M, N ~J ear. *GÓ68 [guš | N ~] cal. 14th day. tūšag [gwsk' | N ~a] corner. ģēošūsrūd [rwi^wslwt! = Av. gaošū.srūta-| acquired, learnt. 5051 [BSLYA < A bsr’; рой! | N ~] meat, flesh. ģūšwār [gwštw] | N ~] ear-ring. ģūw-, ~išn, v. ģuftan. gowag [swb k! | М gw'g, N goya] speaking, eloquent; speaker. *ģoūwizār [gwwc'[] explicit, in detail. göy [gwd | N ~] ball. göz [gwc | N ~] walnut. ~énag [gwzynk! | N gózina) a walnut sweetmeat. Gözihr [gwcyhl | Ar. jawzahr] astr. the Dragon. ~ dumb: the descending node of the moon. ~ sar: the ascending node of the moon. grab [22р | P grb] womb. grāmag [gľmk! | P gr’mg] possessions, wealth. grāmig [gľmyk! | M grmyg, N girāmī] treasured, dear. ~ih: affection, respect. 1$raw [giwb! | P grww] cane. *ģraw [glwb' | N giraw] pledge, security. ~ih, ~(a)g4n [glwk’n' | M grug*n, N giraugān] = *graw. grayidan, gray- [gl?d-yin' | P gry-, N gtráy-] lean, incline; intend, desire. ģriftan, gir- [OHDWN-tn' < A V?hd; glptn!, gyl- | M grypt, gyr-, N giriftan, ~] take, hold, restrain. «išnīģ : tangible. griftār [gipt?l | N gir~] held, taken; captive. ~Omand [-'wmnd) tangible. grih [glyh | N girth] knot. lgriw [CWLE < A swr-h; glyw'] neck, throat. ?0riw [CWLE, glyw' | M gryw] self, soul. sgriw [glyw! | P gryw, N girī(b)] a grain measure, modius, peck. griwag [glywk!' | N giriwa] hill, ridge. ģrīwbān [g/ywp?n! | N girībān] neck-guard, gorget. griyistan, griy- [BK YWN-stn'< A У bky; gld-stn! | M gryy-stn, N giristan, giry-] weep, cry.
PHD.txt:383:groh 38 буар
PHD.txt:2164:group dastag, groh, gund.
PHD.txt:2537:knot grih.
PHD.txt:3515:satiety sagrih.
PHD.txt:4787:darridant sagr sagrih sëm
PHD.txt:5376:garānīh darhandarzbed yarranidan garan yarranisn gramigih gramig grāmag drāyīdan, grāyīdan drāz, grāb draxt griy- grih dargūh garasman 1 3uriw griwag grīwbān driyos driyöšīh darigbed dilér drëm griyistan
PHD_mackenzie.txt:2579:grih [glyh I N ginh] knot.
PHD_mackenzie.txt:6315:crow. groh.                                date xorma.
PHD_mackenzie.txt:6720:group dastag, groh, gund.                harmful pad-zyan, resken, zyangar,
PHD_mackenzie.txt:6932:knot grih.                                leader parwinag, pesiir, pesobiiy,
PHD_mackenzie.txt:7482:roof askob.                                satiety sagrih.
PHD_mackenzie.txt:8965:                            \~        sagrih
PHD_mackenzie.txt:10247:wigrih;isnih
PHD_mackenzie.txt:10538:drubustih       ~~'4)~             grih
== NYB
586:a-pérozgareh [?pylweglyh] the state of not being victorious; pat — without vic- tory, unsucecessfully 6112. — V. peröz and peröz-kar.
7175:gurčh: groh
== HRN
3731:eng', tmigih 'Enge'; arm. fanjr 'dicht' (H. No. 110).
7202:Verse {bih und girih). Ich stelle das Wort zu den
9341:d%l ez ieregihä hedln Wf söi
10915:164. piyak *Knoten in 9'pi/ak (vd. 9 (41)).
10916:aw. pi/a- 'Knoten' in nava.pi/a--). Vielleicht nur
12387:girih 164,
16036:gihan nsa
16299:jfi'giHtii 491.
```


## [2026-09-05T20:49:39.723Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== PHD line 383 context\"; sed -n '383,386p' PHD.txt | cut -c1-1500; echo; echo \"== PHD_mackenzie grōh entry\"; grep -n \"groh \\[\" PHD_mackenzie.txt | head; grep -n -i \"glwh\" PHD_mackenzie.txt | head"
}
```


### [2026-09-05T20:49:39.796Z] TOOL RESULT

```
== PHD line 383 context
groh 38 буар
ёгбһ [glwh | N guroh] group, crowd. gubrág [gwpl’k'] awake, alert, vigilant. ģubrās- [gwp/”s-] = wigras-, v. wigrádan. ģuftan, $0(w)- [YMRRWN-, YMLLWN-tn! < A ymlwn, V тЇ; gwptn', gwb- | M gwptn, gw-, N ~, gā(y)-] say, speak. ~išn: speech. ģuftār [gwpt?] | N ~] speaker. ~ih: (power of) speech. gugiin- [gwk’n- | M gwg^n-] destroy. gugar(i)dan, gugar- [gwk”/-(y)tn! | N guwár-idan] digest. tuģāy [gwk*dy | M gwg'y, N guwah] witness. ~ih: testimony. ģūh [gwh | N —] dung, excrement. guhrayénidan, guhrayén- [gw AP yn-ytn!] waken, arouse. gul [gwl | N ~] flower, rose. ботап [gwnmn! | = M, N ~] doubt. ~par [-A/] casting doubt. ~ig [-yk'] doubtful. ~ih, ~igih: doubt. gumardag [gwmltk'] appointee, deputy. ģumārdan, gumār- [gwm’l-tn' | М gwm'r-dn, N gumāštan, gumar-] appoint, commission, entrust. gumbad [gwmbt' | N ~] dome, fire-temple. £umég [gwmyk! | M gwmyg] mixture. guméxtan, gumēz- [gx”myhtn!, gwmyc- | M gwmyxtn, gwmyz-] mix. ~išn: mixing, mixture; = gumézagih. gumëzag [gwmyck'] mixture. ~th: the Mixture, (the duration of) this material world. Jgund [gwnd | = P] army, troop; group, gathering. *gund [gwnd | N ~] testicle. gung [g(w)ng | N ~] dumb. ģurbaģ [gwibk! | N ~a] cat. Бита [gwlt! | P gwrd, N ~] hero. lih: heroism, bravery. gurdag [gwltk! | N ~a] kidney. *gurdih [ewityh] (some piece of) armour. gurdwār [gwltw’!] befitting a hero. ёпгр [gwlg | N ~] wolf. gurganig [gw/g”nyk! | N ~i] of (the province) Gurgan. gu
£yag-rob 39 hamband-
e--rób [-lwp | N jārē(b)] broom. geän [HY A < А hy’; yn! | M gy’n, N jan] soul, ghost. ~ kandan: give up the ghost; moment of death. ~-abespar [-^5sp?! | N jān-sipār] reckless, desperate; devoted. ~ig [-yk! | M -yg] spiritual; vital. | ~war [-wl | (P -br), N jánwar] animate; animal.

== PHD_mackenzie grōh entry
2588:gr~h [glwh I N guroh] group, crowd.·
```


## [2026-09-05T20:49:40.806Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== HRN 164\"; sed -n '10905,10930p' HRN.txt; echo \"== HRN around 7202\"; sed -n '7190,7215p' HRN.txt"
}
```


### [2026-09-05T20:49:40.916Z] TOOL RESULT

```
== HRN 164
aw. payah' *Milch* (ai. päyas-; af;'. pai; wa;^^. pdi,
si>'n. päi, sar. pöi geronnene Milch, Lab, Quark') ist
schon im Mittelpersischen verschwunden.
np. pmü, pinük (soll gleiche Vokalquantität wie
minö, *menö haben ^), also *pP.nö) *saure Milch, frischer
Käse' ist nicht belegt'; gehört hierher auch np. pemr
*Käse' (phlv. panPr , vd. 7 (191); LW. kurd. penJr;
af/. panlr; bei. paiier (196); wa/. pamr, sar. paver),
pemrek *Malva rotundifolia (deutsch 'Käsepappel'),
AM. 106 Zeile 4 v. u.V
164. piyak *Knoten in 9'pi/ak (vd. 9 (41)).
aw. pi/a- 'Knoten' in nava.pi/a--). Vielleicht nur
umschreibend (glossirt durch g(i)ris, np. c/irih).
165. p{i)sn 'Nahrung (vd. 16 (17) Gl.).
aw. pidim- 'Nahrung (vd. 13 (79)). Statt ]yisn?
166. pit 'Nahrung, Speise (y. 9 (36)).
aw. pitu- 'Speise'; ai. pitü-,
oss. d. fid, t. fid 'Fleisch' (284); sangl. pudaf
'Fleisch' (?).
167. pitet (Men., K. 43), pUetiklh (AV.), patet, patettklh,
patetlha (Pehlv.-Vend.) 'Reue, Patet'.
aw. paititi- 'Reue'. Kommt neupersisch (pitet) nur
als pärsischer t. t. in Pärsenschriften vor; vergl. arm.
LW. bdzpayit 'Sündensühnung aus ap. V)azapatiti'
(Hübschmann, Liter. Centrbl. 1892 No. 45 Sp. 1627).
168. *pöi9n 'Durst' in apöisn 'nicht dürstend' (Men., Bund.,
== HRN around 7202
(Barthol omae, briefl. Mitteilung)'').
') Sähu. IIT, 1662 V. 2904 reimt ftiröxt auf uedöxt
^) Darmesteter (At. ir. II, 154) hatte an aw. dnnma.fraotö
13, 14) '(Iriving down the clouds* gedaclit; die Neuausj^abe hat
ma.frutö* Eine andere, ebenso unwahrsclieinlicho liltymologie stammt
Goldiger, KZ. 25, S. 515 Note 12 (np. furöd ^ aw. fraonf).— \Si -
826. ftHh viel, mehr.
aw. vergl. fräyäo, fraesta-; phlv. fr ah, f rahist
(Päz. freh^ frehest), ursprünglich freh^ vergl. freh[dätär
(AV.).
Die Aussprache ßrih (nicht fireh) bezeugen die
Keime der beiden bei Vullers s. v. mitgeteilten
Verse {bih und girih). Ich stelle das Wort zu den
von Andreas erklärten bih, kih, mih (No. 241).
827. ferl *lieb, schön .
aw. frya- geliebt, Freund*; ai. pnyä-,
828. feryäd *Hilfe; Hilferuf, Klage.
aw. fraöäia- ^Gedeihen, Förderung' (yt. 13, 68);
phlv. frayät bezw. fradät 'Hilfe*.
Die mittelpersische Bedeutung *Hilfe* findet sich
auch noch im Neupersischen, z. ß. AM. 43 Zeile 6, 82
Zeile 1 V. u., Öähn. I, 126 Vers Uli (NB. wohl un-
echter Vers).
LW. kurd. af/. feryad-, bei. paryat 'Geschrei* (199).
Anders Fr. Müller, WZKM. 5, 353.
829. fireften 'betrügen*, Praes. fireb-em , ßreb 'Betrug*,
```


## [2026-09-05T20:49:52.398Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== ARY گره\"; grep -n \"گره\" incoming/ARY/ARY_pages.txt | head -20; echo \"== ARY گروه\"; grep -n \"گروه\" incoming/ARY/ARY_pages.txt | head -20"
}
```


### [2026-09-05T20:49:52.457Z] TOOL RESULT

```
== ARY گره
770:سرتاسر اروپای غربی «انگلیسی و فرانسه و اسپانیا) و اروپای مرکزی نشیمند بودند و لشگرهای آنان تا
11684:چم این واژه در زبان یونانی: گره,
== ARY گروه
231:این دوگروه حا کی از وجود خاستگاه هند و اروپائیان در حدود مرز میان این دو گروه است.
957:یکی از سه اندیشه‌ی بالا بودند. ۱-نوما پامپیلیوس (۳01/211179 111۸ که بنیانگذا رگروه‌های !
10531:چم اين واژه ذر زبان ابرلندی کهن و ولزی: گروه» گروه سربازان.
10532:چم این واژه در ازبان‌های ژرمنی: گله» دسته‌ی گوسپند یاگاو» گروه.
```


## [2026-09-05T20:49:53.692Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== HUB\"; grep -n -i \"girih\\|Knoten\" HUB.txt | head -20; echo \"== CHEUNG grant\"; grep -n -i \"granth\\|grant\\|\\*granθ\\|knot\" CHEUNG.txt | head -20"
}
```


### [2026-09-05T20:49:53.765Z] TOOL RESULT

```
== HUB
3297:Hierher nach Fr. Miiller, WZKM. 8, 189 np. ffiHh 'Knoten'
7233:8. oben p. 66; girth 'Knoten = ap. ^gra&a- (oben p. 93).
9777:zirih ist hier girih *Knoten (vgl. p. 93) zu er-
== CHEUNG grant
73:use is granted by Brill provided that 
135:with a grant from the Netherlands Organization for Scientific Research (NWO) for a 
1748:(+ *fra-) ‘to offer, grant’ => Kent: 200a 
2232:Partic.: pres. MMP bwyy’g ‘fragrant’ || (+ *ham-) Partic.: pres. MMP hwmbwy’g ‘smelling’; Inf.: BMP 
2239:*PARTHIAN: bwy- ‘to be fragrant’? = Ghilain: 65 | DMMPP: 119a 
2243:*KHOTANESE: ОКЪ. bü(d)- (buv-) ‘to be fragrant’ = SGS: 103 
2376:*NWIR: Bal. bog ‘joint, knot’ 
2514:*NWIR: NP baxsudan/baxSsay- ‘to grant, bestow’, Gur. (Kand.) bas ‘give !’, Ham. 
2519:*MISC: Orm. bas-/b(as)’ék ‘to give, grant’ = bax-/baxók ‘to offer, pardon’ 
3997:*BACTRIAN: àa- ‘to give, assign, grant, allot, assign’ || (+ *para-) napaña- ‘to sell’ 
4038:*IE COGNATES: Hitt. /da-/ ‘to take’, Gr. ёіёори ‘I give, grant’, Lat. dare, OCS dati, 
4156:*KHOTANESE: dama- ‘bond’, dima- ‘tie, knot’ 
7384:come’ || (+ *upa-) *bg’m- (caus.) ‘to grant’ || (+ *uz-) ‘zgd (pret. stem) ‘to gone 
8749:Partic.: pres. YAv. gramant- (Y 9.28), perf. pass. YAv. granta- (Yt 10.18 f., Yt 10.23, Yt 10.39 ff., etc.) 
8782:*øraðH ‘to tie (a knot)’ 
8784:*MIDDLE PERSIAN: BMP glyh /grih/ ‘knot’ 
8786:*PARTHIAN: gryh ‘knot? = DMMPP: 164a 
8788:*KHOTANESE: OKh. grantha-, gramtha-, LKh. gratha- ‘knot’ || (+ *ham-) OKh. 
8795:*SOGDIAN: BSogd. yr’ns ‘knot, bond, joining’ 
8801:*NWIR: Bal. grancit/granc- (denomin.) ‘to tie, knot’, NP girih, Bal. garanc, Kurd. gire
```


## [2026-09-05T20:50:00.715Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '8775,8815p' CHEUNG.txt"
}
```


### [2026-09-05T20:50:00.761Z] TOOL RESULT

```
*IE COGNATES: Goth. gramjan, OHG gremmen ‘to become angry’, OE gremman ‘to 
scorn’, etc., NHG grimm, Engl. grim, Lith. gramu, etc. 

*REFERENCES: Paxalina 1959: 203; Sims-Williams 1976: 18, 60; Abaev, Slovar’ П: 333; WIM II/1: 81; 
Steblin-Kamenskij 1999: 185; NEVP: 32; Shahbakhsh: s.v. grand-; Korn 2005: 317, fn. 200 


*øraðH ‘to tie (a knot)’ 

*MIDDLE PERSIAN: BMP glyh /grih/ ‘knot’ 

*PARTHIAN: gryh ‘knot? = DMMPP: 164a 

*KHOTANESE: OKh. grantha-, gramtha-, LKh. gratha- ‘knot’ || (+ *ham-) OKh. 
hamgramtha-, LKh. hamgratha- ‘attachment’ 


x 


*SOGDIAN: BSogd. yr’ns ‘knot, bond, joining’ 


*gZar ? (*gzar ?) 123 


*NWIR: Bal. grancit/granc- (denomin.) ‘to tie, knot’, NP girih, Bal. garanc, Kurd. gire 
(Ё), Zaz. gire- (in giré-dayis ‘to fetter, tie, bind’), Abyan. gerah (Ё), Abz. gere, Anar. 
gireh, Ard. gire, Gz. gire, Jow. gere, Siv. gire ‘knot’ 

*NEIR: Yi. yuréX, Yzgh. yəraw0, ? Oss. І. ælxync’, D. ælxij (formally puzzling), 
(from early NP) Bart. zirix, Rosh. jiréx, Sariq. Z(i)rex, Wa. Zirox ‘knot’. © Pash. 
yaral ‘to twist, spin’ (EVP: 27) may not belong here: s.v. *gart. 

*SANSKRIT: granth' ‘to tie a knot" = EWAia I: 504 

Q A convincing IE etymology for this (Dir. root is wanting. The Germanic nominal 
forms, ? OHG kratto ‘basket’, OE cradol, Engl. cradle, NHG Kranz (m.) ‘wreath, 
garland’ often cited as cognates are unattractive: are they rather loanwords from a 
"substrate" source ?
```


## [2026-09-05T20:50:02.517Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== HUB 3290-3300\"; sed -n '3290,3300p' HUB.txt; echo \"== HUB 7225-7240\"; sed -n '7225,7240p' HUB.txt; echo \"== HUB search grabha/gratha\"; grep -n \"gra&a\\|graGa\\|gra9a\\|grafta\" HUB.txt | head"
}
```


### [2026-09-05T20:50:02.587Z] TOOL RESULT

```
== HUB 3290-3300
auch grpan, grapanak *Tasche*) '), wahrend phi. grtvpdn
Phi. Vd. p. 172, Z. 3 'Halsberge = zd. *grTva'pana'
*Nackenschiitzer bedeutet. Zd. gr%va- ist 'der Nacken
eines Berges am Thor der HoUe = phi. grfvak, das
Fr. Muller, WZKM. 6, 190 mit Recht = np. garlva,
giriva mens depressus, collis' setzt. Vgl. afgh. grava,
gr^a fem. *the collar-bone, the collar of a dress*.
Hierher nach Fr. Miiller, WZKM. 8, 189 np. ffiHh 'Knoten'
= ap. *gra&a- zu skr. grath Verkniipfen'.
915. Np. ffirtntan, ipt. girl, pr. giryam (nach Vullers,
Radices etc., vgl. phi. g(i)ryan Ql. and Ind. 264), phi.
== HUB 7225-7240
gahavorak *Sessel, Sanfte, Bett' (5. Jhd.) ; cahdr Vier , paz.
cihdr = zd. cad ward; cihil 'vierzig = zd. dadwaresatem;
Gdh 'Brunnen , phi. cdh PN. 84, ap. '^cdd^-, zd. odt^ ^) ; sdh
*J Ueber den Weohsel von altiran. ^ und i aus urspr. t (je nach-
dem ij, V Oder «', u, at, an etc. auf t folgten) siehe ZDMG. 44, 555.— 204 —
'Konig', phi. sah (vgl. s{a)hpuhr der Inschriften des 3. Jhd.,
saansaan des Ammian = np. sahanSdh) = 2i^. xsdya^iya-;
rah *Weg', paz. rah, ami. rah, phi. ras = ap. "^rad^a-^;
8. oben p. 66; girth 'Knoten = ap. ^gra&a- (oben p. 93).
Hier erscheint fiir ap. ^ im Phi. Arm. Paz. und Np.
uberall A, dagegen 5 nur im Phi. bei gas, gasvarak und
ras^), wo die andern Sprachen gleiehfalls h haben (arm.
gah, gahavorak, rah). Also ist s hier nur historische
Schreibung und in der altesten Zeit &, spater aber h zu
sprechen. Vgl. KZ. 24, 386 und unten Kap. 18.
In LehnwSrtern aus dem Avesta trat fiir & ein:
== HUB search grabha/gratha
1283:= ap. patiy gemein haben, dass aber phi. patgraftan,
3298:= ap. *gra&a- zu skr. grath Verkniipfen'.
7233:8. oben p. 66; girth 'Knoten = ap. ^gra&a- (oben p. 93).
8930:patgraftan oben p. 38; varzdv = varzgav H. 197. Ganz
```


## [2026-09-05T20:50:16.252Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'));print(json.dumps(d['BQT'],ensure_ascii=False,indent=1));print(json.dumps(d['MON'],ensure_ascii=False,indent=1))\""
}
```


### [2026-09-05T20:50:18.103Z] TOOL RESULT

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


## [2026-09-05T20:50:25.297Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT; grep -n \"\\[pdf page 59[4-9]\\]\\|\\[pdf page 60[0-4]\\]\" BQT_v3_pages.txt | head; echo ===; awk '/\\[pdf page 598\\]/,/\\[pdf page 601\\]/' BQT_v3_pages.txt | head -80"
}
```


### [2026-09-05T20:50:27.082Z] TOOL RESULT

```
Exit code 1
43484:[pdf page 594]
43551:[pdf page 595]
43640:[pdf page 596]
43702:[pdf page 597]
43778:[pdf page 598]
43874:[pdf page 599]
43972:[pdf page 600]
44055:[pdf page 601]
44144:[pdf page 602]
44244:[pdf page 603]
(eval):1: == not found
```


## [2026-09-05T20:50:29.478Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT; sed -n '43778,43880p' BQT_v3_pages.txt"
}
```


### [2026-09-05T20:50:29.532Z] TOOL RESULT

```
[pdf page 598]
ور ات

گرماوه ۱ بر وزن جلفاوه » بمعنی
کرمابهات که حمام باشد .

گرا فزای ۲ - بکر فا . نام ماه
سیم است از سال ملکی .

گرهاله - بر وزن ده ساله » دوائی
باشد ‎Gy‏ مردار ‎Cee‏ و درمرهمها بکاربرند.
کوشت را بروبانده واکر ‎ob‏ بسایند و درزیر
بغل و هرجا که عرق ‎OT‏ بدیو باشد بمالند ‎Sy‏
‏آنرا ‎aye‏ وبیونالی مولویدانا خوانند .

گرمالیل ۴ > بر وزن عزرائیل, نام
پادشاء زادمایست و او مطبخی ضحاكك بود. گوشد
هر روز دوکس را ‎sh‏ میدادند تا مغز سر ‎Ole!‏
‏را بجهت ‎cle‏ دوشهای ضحاك مرهم سازد و او
هر روزمغز سر مك کسدا با مغز سریك کوسفند
‎be‏ میکرد و يك کس آزاد میشمود , و گوبند
کردان صحرائی‌ازتسل آزاد کردهای گرمائبل‌اند.

گرم خیژ ۴ - کنابه از مردم سحر
خیز و زود بیدار شونده و سك روح و ‎she‏
‏و چابك و تیزرو باشد - و صوفی - ونمازشب کن
‎ty‏ نیز گفته‌اند .

گرم 3لان ۵ - عاشقان ودلسوختگان
را گونند .

گرم دوان ۱ - ‎os‏ از ‎has‏
‏وبشتاب روند کان‌باشد -وعاشقان بی‌صبر-وسالعان
‎Ve‏ را هم گفته‌اند .

‎asa ۱‏ («.م.)
۴ 1 : کرمائیل » ارمائیل .
۵ - جمع : گرم دل .

‏کرمیخ

‏گرهلگ - بروزن زردگ » باقلاید رآب
جوشانیده را گوبند۷ - ولوعی از خربزییش‌رس
باشد - رصغیرکرم هم هست :

‏گرهگاه - بروزن بزمکاه » بمعنی
میان روز باشد که هوا در نهایت گرمی‌است۸ +

‏گرم کرت - کنابه از ‎ks‏ کردن
وتعجیل نمودن - وحرص ساختن- وبقهر ‎ite‏
‏درآوردن باشد .

‏گرم سر ۵ ‎=o‏ کنابه ازمحنت‌وراحت
و سخت وسست وشدت ورخا وبدی ونیکی‌وامتال
ایتها باشد .

‏گرم و سر۵‌چرخ -کنابه از ‎BOT‏
‏وماء وحوادث فلکی باشد .

‏گرهه * ‎pe‏ وزن نرمه . هر میوء
‎ate‏ راکوبند عموماً - و خربزة ‎ates‏ را
‎«Lopes‏

‏گرمه لیز ‎ue!‏ بای ابجد بر وزن
رستخیز + غربال سوراخ تنگه را گوبند .

‏گرمه و یز . با واو بروژن و معتی
کرمه بیز است که غربال سوراخ‌تنگه را کوبند.

‏گر هیخ ‎oT‏ بنم اول ‎ee Song‏

‎Ger,‏ بز رکه چوبین با آهنین که بر دوسر طویله

‏برزمین فروبرند و رسمالی برآنها بسته اسبافرا
بدان ریسمان بندند .

‏۴ - از :رما فزای ( فزاینده ) .
۴ از ‎pete SF:‏ ( خیزنده ) .
‎٩‏ - جمع :گرم رو ( رونده ) .

‏۲ - در فاری ‎garmak‏ لوط « علوی © :

‎JT‏ برمك در کرم کرمك فروش این درند

‏این سخن ‎Hey‏ تم یکویمکههست‌این‌مشتهر.
بحاق‌اطممه .

‏۸ > بك کرمگاه ‎yt‏ غلامان ومقدعان محمودی ... پیاده نزديك امیررمعودآمدند...»

‎putt (‏ بیهقی مصحح فیاش ص ۱۳4 ) .
54 :کرمك . ‎am te‏
۴- قی :کل ‎pre‏ ( در تداول ) .

‏مه ویز ‎Ce»)‏

‏۲۷ کرمه بیز (هم)
[pdf page 599]
کر می‌خونابه .
گر می خو نابه = کتابه از ‎he‏
‏وشتاب وتصجیل درکربه باشد .

گر نج - بضم اول ‎Ty‏ ثانی وسکون
نون و جیم » بممنی چین وشکنج باشد- و کنج
```


## [2026-09-05T20:50:37.362Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT; awk 'NR>=43972 && NR<=44400' BQT_v3_pages.txt | grep -n \"گره\\|گروه\" | head -30; echo \"=== pages 600-603 head\"; sed -n '43972,44060p' BQT_v3_pages.txt"
}
```


### [2026-09-05T20:50:38.982Z] TOOL RESULT

```
12:گره ۴ ‎ee‏ اول و ثانی بر وزن
16:گروهه نم اول و ثالث مجهول
59:‏۴ - پهلوی ]8۲6 ( دسته , گروه ) ۰ ارمنی ع 8۳0 ( ملت » جمعیت ): بلوچی
66:‏۱ - «آفتاب زرد سلطان از سراپرده بدرآمد , کمان گروهه‌ای در دست .۰ « چهارمقالةً
90:گرهبر ‎Gel‏ وثالی‌وسکون‌ها
95:گره بر ‎OU‏ - یک اول ‎gilts‏ کنابه
100:‎oP‏ گره - کنابه از مشکل بر
103:‏گره بر گوش ددن هت کنابه از
106:‏گرهچه ۴ = بکر اود و فتح جیم
109:‏گره 999 = ‎wl S‏ از ذخیره نهادن
114:‎. ‏:گره ب رگره‎ dy ٩
117:من خود بگرهچة کیابی
125:فی: کردی8870616 (مفصل, بند وبت) ‎UN?‏ ص۳۵۵. ورث: گرهه.
130:‏گره گردات - نم نومی از بازی
132:گره گوشت » بکر اود و ‎Ls‏
140:وثالی» مخفف ‎any ST‏ است که کلوله و گروه‌مردم
154:‏۴ - از :گره ۲ بر ( برنده ) ‎pe)‏ باه ) .
183:کره باشد ۵ مطلقاً اعم از گره رسمان و چوب
=== pages 600-603 head
[pdf page 600]
۱۳

فارسی بروزن خروشان, آلت تناسل را گویندا -
‎Ks‏ اولوفتح ثانی» کر وکردتی رآبعنی‌مهون
- وبمعنی بنده وصد هم پنظرآمده است ۴ .

گر و گر « بفتح اول و اف فارسی
بروژن ‎HF‏ یکی از نامهای‌خدای‌تمالی است‌ومعنی
‎OT‏ مرادبخش باشد .

گره ۴ ‎ee‏ اول و ثانی بر وزن
‎ag‏ جماعت مردم را کوبند و بعربی قوم
خوانند .

گروهه نم اول و ثالث مجهول
و فتح ها ۰ بروزن و معنی کلوله است مطلقاً ۵
‎UIT Is‏ رسمانی وخواه ‎UIT‏ توپ و تفنگه
‎UIT,‏ بازی ‎VIS,‏ خمیرنان و پنبه و ‎DMT‏
‏کمان کرومه ۱ وامثال ‎OF‏ باشد وبعربی‌جلاهق
خوانند و کلولةحلوالی‌باشد که‌عربان کمب الفز ال
کوبند - و بمعنی کروه و جماعت مردمنیز آمده
است - و بکسر اول » بمعنی‌دکچی باشد و آن

۱ رك : فرهنگ نظام .
۳ - ش هکم ‎ae‏ هوشی تافته جان

کره
‎UIT‏ رسمانی‌است که دروقت رشتن بردوثپیجد
‎Ques‏ تصیله خوانند ۷ .
گردی = ‎Jy) pn‏ وسکون ثانی‌وئاث
بتحتانی کشیده . نام یکی از خویشان افرسیاب
است که در کشتن ‎OS He‏ کرد و حیلها
انگیخت و او را کروی زره ليز کوبند ۸ ۰
گرو ین * = ‎IG‏ وفتح ثانی,
به‌عنی ایمان آوردن وسر باطاعت نهادن‌وپذبرفتن
و بردل محبت واطاعت شخصیراکره بستن باشد.
‎Soo”‏ اول و ‎GU‏ و ظهور ها »
معروفست اعم ازینکه دررسمان با درخت‌رامثال
آن و از جایبی بر آمده
باشد ویعربی عقد هگوبند ‎STS ۱٩‏
-وتخم خاری هم هت که
بدان پوست را دیاغت کنند ‎Ss‏
‏وآنرا بعربی قرط خوانند- ودلرا هم گفته‌اند که
عربان پال گویند - و بمشی مشکل هم بنظر

بچندین حرتش جای ی کرو کان .
امیرخسرو دهلوی «رشیدی» .

۴ ک رکر , ظ . از : 8870 (82۲پرستیدن) [فس: گرزمان ] دراصد ‎chy‏ نام ‎has‏
‏از دعاهای زرتشتیان» نام ۷۳« ک رکر» ونام۷ «کر و کر» آمده . رك : خرده اوستا . شهمرران .

‎oes‏ ۱۳۰۸ ص۳.
فرزند تو امروز ‎oy‏ جاهل و عاصی

‏فردات چه فرباد رسد پیش ‎IIS‏
‏« ناصرخروبلخی. دیوان ص۱۷۳*.

‏۴ - پهلوی ]8۲6 ( دسته , گروه ) ۰ ارمنی ع 8۳0 ( ملت » جمعیت ): بلوچی
1 , ایرالی باستان - ‎ogravathva‏ « تیب ‎oS‏ ص ‎at‏ » کردی ‎kuruh‏ (اجتماع اشضاس)

‏«ژابا صس ۳۳۱ .

‏۵ - قی :کلوله , غلوله . مخفف ‎OT‏ «کرهه ».

‏۱ - «آفتاب زرد سلطان از سراپرده بدرآمد , کمان گروهه‌ای در دست .۰ « چهارمقالةً

‏نظامی عروضی چاپ اول نگارنده ص ‎VT‏

‏نوشته :

‏۲ - رك : رشیدی . محشی تچك ‎(crt)‏

‎al «‏ داست که لفظ تصیله بمعنی د کچی درکتب متمارفة لغت عربی بنظر نرسیده ,اما

‎des‏ بمعنی ریسمالی که ازدولك برآید ؛ نوشته‌اند , و این بمنی حطلوب یعنی ‏ دکچی‌صریح‌تست
و بدین معتیآنچه درلفت عرب موضوع و درکتب متداوله مسطور گشته لفظ وشیمه ووجاجه‌است.
چنانکه برمتتبع پوشیده نست .* ۸ _ ‎(Gur bt 21113 —) Guréy‏ رلك: فهرست ولف.
‎virravistan _ ٩‏ ( از ‎virrav_‏ ) (باور کردن » کمان کردن). ‎varbistan wij‏
از اوستا - ۷۵۲ « بارتولمه ۱۳۹ » « تب رکه ص ۲44 » و ‎Dy‏ : اسشق - هوبشمان ‎ANY‏
‏۶ پهلری ‎grab‏ « تاوادبا ص ۱۹۱ :۲ ‎oS) hit os Sue‏ » عفد ازدواج) « ژابا
ص ۲۹۱ > . از پارسی باستان - ‎ogratha‏ , سانسکریت 8۲842 ( بستن ) «هوبشمان ‎Ate‏

[pdf page 601]
پر
آمده است ۱ چه کره کشا بسنی مشکل کشا
‎ash‏ - و بفتح اول وثالی و خفای ها . ‎ghee‏ را
کوبند و آن ظرفی باشد بجهت آب آوردن .
```


## [2026-09-05T20:50:54.961Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n 1,60p tools/ref_page.py"
}
```


### [2026-09-05T20:50:55.022Z] TOOL RESULT

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


## [2026-09-05T20:50:57.417Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; timeout 600 python3 tools/ref_page.py BQT:1803 --image 2>&1 | tail -40"
}
```


### [2026-09-05T20:50:59.282Z] TOOL RESULT

```
REF: BQT:1803  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 598  OCR-lang: fas

سا کرمیخ
گرماوه ۱ « بر وزن جلفاوه » بمعنی گرمك < بروزن زرد » باقلای‌درآب
کومابم.است که حمام باشد . جوشانیده را کویند۷ - ولوعی از خریزةییش‌ری
گرها فزای ؟ « بکر فا نام ماه | باشد - وتصفیرکرم هم هست. -
گرهاله - بر وزن ده ساله , دوائی | میان روز باشد که هوا در نهایت کرمی‌است۸ .
باشد برنگه مردار سنکه و درمرهمها بکاربرند. گرم کردن - کنایه از شتاب کردن
کوشت را بروباند» واگر باب بسایند و درزیر | وتعجیل نمودن - وحررص ساختن- وبقهر وغض
بفل و هرجاکه عرق آن بدیو باشد بمالند بوی | درآوردن باشد .
آنرا ببرد وبیونانی مولوبدانا خوانند . گرم سرد - کنابه ازمحنت‌وراحت
گرمائیل ۴ * بر وزن عزرائیل, نام | و سخت وست وشدت ورخا وبدی ونیکی‌وامتال
یادشاه زادماست و او مطبخی شحالد بود. گوبند ابنها باشد .
هر روز دوکس را باو میدادند تا مغز اسر ایشان گرم وسرد چرخ «کنابه از آفتاب
را بجهت علت دوشهای ضحاك مهم سازد و او وماءه وحوادث فلکی باشد .
هر روزمغز سر يك کس‌را با مغز سريك کوسفند گرمه * - بر وزن نرمه . هر میوة
مهیا میکرد و يك کس آزاد مینمود » وکوبند شرس رآگویند ها و خرره مر را
کردان صحرائی‌ازدل‌آزاد کردهای گرمائبل‌اند. ۱ مد عموط - و کریزه دی 2
.»۴ کش : خصوصا .
گرم خیز ۴ - کنایه از مردم محر مه بیز *۱- سا بای | زن
هر ار شونده و سك یز ۰" ب بای ابجد بر وزن
خیز و زود بیدار شونده و سبك روح و جلد ی اخ تژگه ۱ :
ی ۰ 8 . رستخیز » غربال سوراخج راکوبند .
و چابك و تیزرو باشد - و صوفی - ونمازش ب کن ۱ ۹۹
را نز گفته‌اند . گرمه‌و یز ۰۱۱ با راو بروزن وهمنی
گرم دلان * « عاشقان ودلوختگان گرمه بیز است که غربال سوراخ‌تنگه را کویند.
راکویند . گرهیخ - بطم اول بروز نکلمیخ,
گرم دوان ۱ - کنابه از تعجیل | میخ بزرکه چوبین با آهنین که بر دوسر طویله
وبشتاب روند گان‌باشد -وعاشقان بی‌سبر-وسالکان | برزمین فروبرند و ریسمانی برآنها بسته اسپافرا
۱ کرمابه (ه.م.) ۴ - از :گرما + فزای ( فزاینده ) -
۴ - ر4 : کرمائیل . ارمائیل . ۴ - از :کرم+خیز ( خیزنده ) .
8 - جمع : گرم دل . ‎٩‏ - جمع :کرم رو ( رونده ) .
۷ - در فاری 527326 11 ‌ علوی 6
آل برهك در کرم کرمك فروش این درند این سخن نرمك نمی کوب کههت این مشتهر.
بعهاق‌اطممه ۰
۸ اد يك کرمگاه این غلامان ومقدمان محمودی ... پیاده نزديك امیرممودآمدند...»
( تاریخ بیهقی مصحح فیاضش ص ۱۳4۵ ) ۰ ۱
‎٩‏ -قس :گرمك . ۶۴ کرمه ویز (هم.) ۹۱ کرمه یز (هم.)
۴د-قی :کل مخ )۱ در تداول ( ۰
```


## [2026-09-05T20:51:06.913Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -c \"\nimport json;m=json.load(open('data/verification/sources/refs/incoming/BQT/BQT_v3_pagemap.json'))\nmm=m.get('map',m)\nfor p in ['1798','1800','1801','1802','1803','1804','1805','1806','1807','1810']:\n    print(p, mm.get(p))\n\" 2>&1 | head"
}
```


### [2026-09-05T20:51:09.045Z] TOOL RESULT

```
1798 None
1800 None
1801 None
1802 None
1803 None
1804 None
1805 None
1806 None
1807 None
1810 None
```


## [2026-09-05T20:51:12.968Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -c \"\nimport json;m=json.load(open('data/verification/sources/refs/incoming/BQT/BQT_v3_pagemap.json'));print(type(m), list(m)[:5] if isinstance(m,dict) else m[:3])\nmm=m.get('map',{}) if isinstance(m,dict) else {}\nks=sorted(mm, key=lambda x:int(x)); print(len(ks), ks[:5], ks[-5:])\nprint({k:mm[k] for k in ks if 1795<=int(k)<=1812})\n\""
}
```


### [2026-09-05T20:51:50.819Z] TOOL RESULT

```
<class 'dict'> ['pdf', 'pdf_pages', 'offset_mode', 'anchors', 'map']
592 ['1210', '1211', '1212', '1213', '1214'] ['1920', '1921', '1922', '1923', '1924']
{'1797': 592}
```


## [2026-09-05T20:51:56.810Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -c \"\nimport json;m=json.load(open('data/verification/sources/refs/incoming/BQT/BQT_v3_pagemap.json'));mm=m['map']\nks=sorted(mm,key=int)\nsel=[k for k in ks if 1780<=int(k)<=1830]\nprint([(k,mm[k]) for k in sel])\nprint(m.get('offset_mode'), str(m.get('anchors'))[:300])\n\""
}
```


### [2026-09-05T20:51:58.957Z] TOOL RESULT

```
[('1780', 577), ('1781', 578), ('1782', 579), ('1783', 580), ('1784', 581), ('1785', 582), ('1786', 583), ('1787', 584), ('1788', 585), ('1789', 586), ('1790', 587), ('1791', 588), ('1792', 589), ('1793', 590), ('1797', 592), ('1819', 616), ('1820', 617), ('1821', 618), ('1822', 619), ('1823', 620), ('1824', 621), ('1825', 622), ('1826', 623), ('1827', 624), ('1828', 625), ('1829', 626), ('1830', 627)]
1203 34
```


## [2026-09-05T20:52:04.965Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; timeout 900 python3 tools/ref_page.py BQT:1803x --pdf-page 600 --image 2>&1 | tail -5; echo \"---try proper---\"; timeout 900 python3 tools/ref_page.py BQT:1803 --pdf-page 600 --image 2>&1 | tail -6"
}
```


### [2026-09-05T20:52:06.783Z] TOOL RESULT

```
expected ABBR:page (e.g. BQT:918 or MON5:528)
---try proper---
بعهاق‌اطممه ۰
۸ اد يك کرمگاه این غلامان ومقدمان محمودی ... پیاده نزديك امیرممودآمدند...»
( تاریخ بیهقی مصحح فیاضش ص ۱۳4۵ ) ۰ ۱
‎٩‏ -قس :گرمك . ۶۴ کرمه ویز (هم.) ۹۱ کرمه یز (هم.)
۴د-قی :کل مخ )۱ در تداول ( ۰
```


## [2026-09-05T20:52:12.847Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; ls data/verification/sources/refs/ocr/BQT/ | head; mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad; pdftoppm -f 600 -l 600 -r 200 -png -singlefile data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bqt_pdf600 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


### [2026-09-05T20:52:15.053Z] TOOL RESULT

```
0001.png
0001.txt
0049.png
0049.txt
103.vision.txt
1225.png
1225.txt
1225.vision.txt
1275.png
1275.txt
total 18968
drwx------ 2 sfmqrb sfmqrb    4096 Sep  5 16:52 .
drwx------ 4 sfmqrb sfmqrb    4096 Sep  5 16:02 ..
-rw-rw-r-- 1 sfmqrb sfmqrb   68775 Sep  5 16:43 ary440.png
-rw-rw-r-- 1 sfmqrb sfmqrb  752374 Sep  5 16:12 bqt362_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  624515 Sep  5 16:12 bqt362.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb 1032029 Sep  5 16:13 bqt362_mid.png
-rw-rw-r-- 1 sfmqrb sfmqrb  385716 Sep  5 16:13 bqt363_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  338175 Sep  5 16:13 bqt363_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb  692415 Sep  5 16:13 bqt363.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  956665 Sep  5 16:11 bqt553_foot2.png
-rw-rw-r-- 1 sfmqrb sfmqrb  746413 Sep  5 16:11 bqt553_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  512022 Sep  5 16:10 bqt553.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  154316 Sep  5 16:07 bqt_bot389.png
-rw-rw-r-- 1 sfmqrb sfmqrb  168738 Sep  5 16:07 bqt_bot390.png
-rw-rw-r-- 1 sfmqrb sfmqrb  520653 Sep  5 16:07 bqt_n389.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  527392 Sep  5 16:07 bqt_n390.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  100925 Sep  5 16:52 bqt_pdf600.png
-rw-rw-r-- 1 sfmqrb sfmqrb   67648 Sep  5 16:29 build128.py
-rw-rw-r-- 1 sfmqrb sfmqrb  105345 Sep  5 16:30 build132.py
-rw-rw-r-- 1 sfmqrb sfmqrb   62948 Sep  5 16:36 build134.py
-rw-rw-r-- 1 sfmqrb sfmqrb   56126 Sep  5 16:29 build136b.py
-rw-rw-r-- 1 sfmqrb sfmqrb   13830 Sep  5 16:22 build136.py
-rw-rw-r-- 1 sfmqrb sfmqrb   66341 Sep  5 16:28 build139.py
-rw-rw-r-- 1 sfmqrb sfmqrb   53260 Sep  5 16:29 build142.py
-rw-rw-r-- 1 sfmqrb sfmqrb   76989 Sep  5 16:32 build145.py
-rw-rw-r-- 1 sfmqrb sfmqrb   50861 Sep  5 16:34 build148b.py
-rw-rw-r-- 1 sfmqrb sfmqrb   21485 Sep  5 16:29 build148.py
-rw-rw-r-- 1 sfmqrb sfmqrb   17908 Sep  5 16:44 build151a.py
-rw-rw-r-- 1 sfmqrb sfmqrb   15986 Sep  5 16:46 build151b.py
-rw-rw-r-- 1 sfmqrb sfmqrb   11172 Sep  5 16:47 build151c.py
-rw-rw-r-- 1 sfmqrb sfmqrb   19592 Sep  5 16:50 build151d.py
-rw-rw-r-- 1 sfmqrb sfmqrb    6433 Sep  5 16:50 build151z.py
-rw-rw-r-- 1 sfmqrb sfmqrb   51529 Sep  5 16:51 build152.py
-rw-rw-r-- 1 sfmqrb sfmqrb   51266 Sep  5 16:51 build154.py
-rw-rw-r-- 1 sfmqrb sfmqrb   72953 Sep  5 16:48 build158.py
-rw-rw-r-- 1 sfmqrb sfmqrb   45662 Sep  5 16:49 build164.py
-rw-rw-r-- 1 sfmqrb sfmqrb   31872 Sep  5 16:51 build168.py
-rw-rw-r-- 1 sfmqrb sfmqrb    7816 Sep  5 16:35 c_am2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   14765 Sep  5 16:35 c_am3.png
-rw-rw-r-- 1 sfmqrb sfmqrb   10038 Sep  5 16:35 c_empty2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4123 Sep  5 16:34 crop_am.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4986 Sep  5 16:34 crop_arabic_refs.png
-rw-rw-r-- 1 sfmqrb sfmqrb    7702 Sep  5 16:34 crop_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb   16978 Sep  5 16:34 crop_morocco.png
-rw-rw-r-- 1 sfmqrb sfmqrb  163996 Sep  5 16:46 gar2.png
-rw-rw-r-- 1 sfmqrb sfmqrb  124975 Sep  5 16:47 gar3.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77205 Sep  5 16:46 gar.png
-rw-rw-r-- 1 sfmqrb sfmqrb  944060 Sep  5 16:18 kent.txt
-rw-rw-r-- 1 sfmqrb sfmqrb     222 Sep  5 16:30 leaf.py
-rw-rw-r-- 1 sfmqrb sfmqrb   57617 Sep  5 16:20 mk129.py
-rw-rw-r-- 1 sfmqrb sfmqrb   74680 Sep  5 16:26 mk131.py
-rw-rw-r-- 1 sfmqrb sfmqrb   33365 Sep  5 16:25 mk133.py
-rw-rw-r-- 1 sfmqrb sfmqrb   42635 Sep  5 16:29 mk140.py
-rw-rw-r-- 1 sfmqrb sfmqrb   51288 Sep  5 16:30 mk143.py
-rw-rw-r-- 1 sfmqrb sfmqrb   57696 Sep  5 16:46 mk153.py
-rw-rw-r-- 1 sfmqrb sfmqrb   49505 Sep  5 16:50 mk157.py
-rw-rw-r-- 1 sfmqrb sfmqrb   30384 Sep  5 16:51 mk170.py
-rw-rw-r-- 1 sfmqrb sfmqrb    4344 Sep  5 16:49 n12b.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3969 Sep  5 16:49 n12.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2692 Sep  5 16:49 n16.png
-rw-rw-r-- 1 sfmqrb sfmqrb   11831 Sep  5 16:32 node4.png
-rw-rw-r-- 1 sfmqrb sfmqrb    7427 Sep  5 16:32 node7.png
-rw-rw-r-- 1 sfmqrb sfmqrb  944060 Sep  5 16:13 oldpers_djvu.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    6054 Sep  5 16:36 p152_e0left.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2672 Sep  5 16:36 p152_node2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   22067 Sep  5 16:29 part0.json
-rw-rw-r-- 1 sfmqrb sfmqrb   14156 Sep  5 16:22 part1.json
-rw-rw-r-- 1 sfmqrb sfmqrb   17147 Sep  5 16:44 part_a.json
-rw-rw-r-- 1 sfmqrb sfmqrb   15703 Sep  5 16:46 part_b.json
-rw-rw-r-- 1 sfmqrb sfmqrb   10974 Sep  5 16:47 part_c.json
-rw-rw-r-- 1 sfmqrb sfmqrb   19420 Sep  5 16:50 part_d.json
-rw-rw-r-- 1 sfmqrb sfmqrb   53212 Sep  5 16:08 pg130_bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74748 Sep  5 16:08 pg130.png
-rw-rw-r-- 1 sfmqrb sfmqrb  107108 Sep  5 16:08 pg130_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   80793 Sep  5 16:15 pg131.png
-rw-rw-r-- 1 sfmqrb sfmqrb   46793 Sep  5 16:20 pg133.png
-rw-rw-r-- 1 sfmqrb sfmqrb   87739 Sep  5 16:10 pg134.png
-rw-rw-r-- 1 sfmqrb sfmqrb   66991 Sep  5 16:16 pg135.png
-rw-rw-r-- 1 sfmqrb sfmqrb   68320 Sep  5 16:08 pg136_300.png
-rw-rw-r-- 1 sfmqrb sfmqrb   63248 Sep  5 16:08 pg136.png
-rw-rw-r-- 1 sfmqrb sfmqrb   45014 Sep  5 16:12 pg137.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74330 Sep  5 16:11 pg138.png
-rw-rw-r-- 1 sfmqrb sfmqrb   70436 Sep  5 16:10 pg140.png
-rw-rw-r-- 1 sfmqrb sfmqrb   63658 Sep  5 16:13 pg144.png
-rw-rw-r-- 1 sfmqrb sfmqrb   89133 Sep  5 16:09 pg145.png
-rw-rw-r-- 1 sfmqrb sfmqrb   60631 Sep  5 16:11 pg147.png
-rw-rw-r-- 1 sfmqrb sfmqrb   81770 Sep  5 16:20 pg148.png
-rw-rw-r-- 1 sfmqrb sfmqrb   72186 Sep  5 16:30 pg149.png
-rw-rw-r-- 1 sfmqrb sfmqrb  131595 Sep  5 16:32 pg151_hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   96854 Sep  5 16:29 pg151.png
-rw-rw-r-- 1 sfmqrb sfmqrb  154426 Sep  5 16:36 pg152_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb   62516 Sep  5 16:35 pg152.png
-rw-rw-r-- 1 sfmqrb sfmqrb   39131 Sep  5 16:28 pg153.png
-rw-rw-r-- 1 sfmqrb sfmqrb   63033 Sep  5 16:30 pg154.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77057 Sep  5 16:32 pg155.png
-rw-rw-r-- 1 sfmqrb sfmqrb  101504 Sep  5 16:43 pg156.png
-rw-rw-r-- 1 sfmqrb sfmqrb  169880 Sep  5 16:34 pg158_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb   80624 Sep  5 16:34 pg158.png
-rw-rw-r-- 1 sfmqrb sfmqrb  124379 Sep  5 16:31 pg159_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb   27814 Sep  5 16:31 pg159.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4694 Sep  5 16:31 pg159_word.png
-rw-rw-r-- 1 sfmqrb sfmqrb  168057 Sep  5 16:34 pg161_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb   76745 Sep  5 16:34 pg161.png
-rw-rw-r-- 1 sfmqrb sfmqrb  110270 Sep  5 16:42 pg162_400.png
-rw-rw-r-- 1 sfmqrb sfmqrb   76438 Sep  5 16:42 pg162.png
-rw-rw-r-- 1 sfmqrb sfmqrb    8523 Sep  5 16:42 pg162_verse.png
-rw-rw-r-- 1 sfmqrb sfmqrb   25911 Sep  5 16:32 pg163.png
-rw-rw-r-- 1 sfmqrb sfmqrb   59398 Sep  5 16:33 pg164.png
-rw-rw-r-- 1 sfmqrb sfmqrb   61265 Sep  5 16:40 pg165.png
-rw-rw-r-- 1 sfmqrb sfmqrb  116877 Sep  5 16:46 pg167.png
-rw-rw-r-- 1 sfmqrb sfmqrb   86005 Sep  5 16:39 pg168.png
-rw-rw-r-- 1 sfmqrb sfmqrb   68420 Sep  5 16:42 pg169.png
-rw-rw-r-- 1 sfmqrb sfmqrb   37351 Sep  5 16:44 pg170.png
-rw-rw-r-- 1 sfmqrb sfmqrb  120612 Sep  5 16:49 pg171_450.png
-rw-rw-r-- 1 sfmqrb sfmqrb   73551 Sep  5 16:43 pg171.png
-rw-rw-r-- 1 sfmqrb sfmqrb   44812 Sep  5 16:34 pg532.png
-rw-rw-r-- 1 sfmqrb sfmqrb  153161 Sep  5 16:34 pg532_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4868 Sep  5 16:14 prt.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  333088 Sep  5 16:16 sod135_c.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1817364 Sep  5 16:16 sod135.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  101641 Sep  5 16:15 sod136_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1892712 Sep  5 16:15 sod136.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   56398 Sep  5 16:26 write144.py
```


## [2026-09-05T20:52:22.600Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad; pdftoppm -f 600 -l 600 -r 350 -png -singlefile /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf p600_350; python3 -c \"\nfrom PIL import Image\nim=Image.open('p600_350.png'); print(im.size)\nw,h=im.size\nim.crop((0,0,w,int(h*0.10))).save('p600_head.png')\nim.crop((0,int(h*0.72),w,h)).save('p600_foot.png')\n\"; ls -la p600*.png"
}
```


### [2026-09-05T20:52:27.438Z] TOOL RESULT

```
(1925, 2971)
-rw-rw-r-- 1 sfmqrb sfmqrb 671488 Sep  5 16:52 p600_350.png
-rw-rw-r-- 1 sfmqrb sfmqrb 183909 Sep  5 16:52 p600_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   5162 Sep  5 16:52 p600_head.png
```


## [2026-09-05T20:52:29.546Z] TOOL CALL #37: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p600_foot.png"
}
```


### [2026-09-05T20:52:29.570Z] TOOL RESULT

```

```


## [2026-09-05T20:52:41.167Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad; python3 -c \"\nfrom PIL import Image\nim=Image.open('p600_350.png'); w,h=im.size\nim.crop((0,int(h*0.58),w,int(h*0.76))).save('p600_foot2.png')\nim.crop((0,0,w,int(h*0.07))).resize((w,int(h*0.07))).save('p600_head2.png')\n\""
}
```


### [2026-09-05T20:52:43.272Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T20:52:45.538Z] TOOL CALL #39: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p600_foot2.png"
}
```


### [2026-09-05T20:52:45.563Z] TOOL RESULT

```

```


## [2026-09-05T20:53:00.519Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; ls site/pages/173.jpg 2>/dev/null; pdftoppm -f 173 -l 173 -r 300 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg173 && python3 -c \"\nfrom PIL import Image\nim=Image.open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg173.png');print(im.size)\""
}
```


### [2026-09-05T20:53:02.984Z] TOOL RESULT

```
site/pages/173.jpg
(2550, 3300)
```


## [2026-09-05T20:53:05.190Z] TOOL CALL #41: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg173.png"
}
```


### [2026-09-05T20:53:05.694Z] TOOL RESULT

```

```


## [2026-09-05T20:53:05.689Z] INPUT

[Image: original 2550x3300, displayed at 1546x2000. Multiply coordinates by 1.65 to map to original image.]


## [2026-09-05T20:53:14.053Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad; python3 -c \"\nfrom PIL import Image\nim=Image.open('pg173.png')\nim.crop((580,780,1300,1030)).resize((1440,500)).save('p173_ital.png')\nim.crop((580,440,1450,620)).resize((1740,360)).save('p173_op.png')\n\""
}
```


### [2026-09-05T20:53:16.161Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T20:53:18.544Z] TOOL CALL #43: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p173_ital.png"
}
```


### [2026-09-05T20:53:18.563Z] TOOL RESULT

```

```


## [2026-09-05T20:53:35.066Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== NYB grōh\"; grep -n -i \"gr[ôöo]h\\|gravaθ\\|gravath\" NYB_vol2_glossary.txt | head -10; echo \"== NYB p84 region?\"; grep -n \"glwh\" NYB_vol2_glossary.txt | head"
}
```


### [2026-09-05T20:53:35.130Z] TOOL RESULT

```
== NYB grōh
6617:gröh: ~
7175:gurčh: groh
== NYB p84 region?
1719:grah [glwh] troop, company, with the indef. art. ~-ë [~+1] 84. - = Paz.; NP guroh.
```


## [2026-09-05T20:53:36.993Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== KLN group\"; grep -n \"gruppo\" KLN_1966.txt KLN_1971.txt | head; echo \"== KLN grape\"; grep -n -i \"krappa\\|krāppa\\|grape, \" KLN_1966.txt | head; echo \"== SKT group/grape/curl\"; grep -n -i \"^group\\|gruppo\\|crulle\\|krul\" SKT.txt | head"
}
```


### [2026-09-05T20:53:37.080Z] TOOL RESULT

```
== KLN group
KLN_1971.txt:106715:group, n. — F. groupe , fr. It. gruppo, ‘group’, 
KLN_1966.txt:16766:group,  n.  —  F.  groupe,  fr.  It.  gruppo,  ‘group’, orig.  'cluster,  packet,  knot’,  fr.  OProven?. grop,  ‘knot’,  which  derives  fr.  Teut.  *kruppa, ‘a  rounded  lump  or  mass’.  See  crop. Derivatives :  group,  tr.  and  intr.  s.,group-ed,  adj. group-ing,  n.
== KLN grape
9534:cramp,  n.,  a  bent  piece  of  iron.  —  MDu.  crampe, cramp,  rel.  to  OHG.  kramph,  ‘bent,  crooked’, ON.  krappr  (for  *krampr),  ‘strait,  narrow’,  and in  gradational  relationship  to  Du.  and  LG. krimpen ,  OHG.  krimphan,  ‘to  curve,  shrink  . Cp.  prcc.  word.  Cp.  also  crimp,  v.,  crumple  and grape,  grapple,  grapnel.
16574:grape,  n.  —  OF.  grape,  grappe,  ‘hook ;  a  bunch of  grapes'  (whence  F.  grappe,  "a  bunch  of grapes'),  fr.  OF.  craper,  graper,  ‘to  seize  with  a hook;  to  gather  grapes',  which  is  of  Teut.  ori¬ gin.  Cp.  MDu.  crappe,  OHG.  krapfo,  ‘a  hook’, G.  Krapfen,  ‘fritter’,  OHG.  krampho.  ‘an  iron hook’.  OF.  grapin,  ‘hook’  (whence  F.  grappin, ‘grapnel, hook’), derives  fr. OF. g rape. Cp.OProv- entp.,  Sp.  grapa.  It.  grappa,  ‘hook’,  which  are also  Teut.  loan  words.  See  cramp,  ‘a  bent  piece of  iron’,  and  cp.  words  there  referred  to.  Cp. also  agraffe.
16591:-graphy, combining  form  denoting:  i) processes of  writing,  drawing,  representing,  recording,  as in  phonography ;  2)  names  of  descriptive  scien¬ ces,  as  in  geography.  —  F.  or  G.  -graphie,  fr. L.  -graphia,  fr.  Gk.  -ypacpta,  ‘description  of’, fr.  vpa-peiv,  ‘to  write’.  See  -graph  and  -y  (rep¬ resenting  Gk.  -la),  and  cp.  -graphia. grapnel,  n.,  a  small  hook.  —  ME.  grapenel,  di- min.  formed  fr.  OF.  grapin,  ‘hook’.  See  grape. Derivative :  grapnel,  tr.  v. grapple,  n.,  grappling  iron,  grapnel.  —  OF.  *gra - pelle,  dimin.  of  grape,  ‘hook’.  See  grape  and  cp. prec.  word.
40947:uva,  n.,  a  grape,  a  grapelike  fruit  (bot.)  —  L.  uva, prob.  fr.  I.-E.  *oiwa-,  *liwa-,  *iwa-,  ‘berry,
== SKT group/grape/curl
```


## [2026-09-05T20:53:55.494Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n 1,50p tools/fetch_source.py"
}
```


### [2026-09-05T20:53:55.534Z] TOOL RESULT

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
```


## [2026-09-05T20:53:56.606Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '1714,1724p' NYB_vol2_glossary.txt; echo \"== IEC\"; grep -n -i \"granth\\|grantha\" IEC.txt | head; echo \"== SYN knot\"; grep -n -i \"girih\\|granth\" SYN.txt | head"
}
```


### [2026-09-05T20:53:56.690Z] TOOL RESULT

```
85
gukai
kaft. Pagliaro’s reading dar-andarzpat is unacceptable. Cf gurtéh.
gristan [glystn; BKYWN-stn'] . griy- (BKYWN-], pt. pret. 3d p. grist [glyst', BKYWN-st'], to weep, to cry, to lament 111’. 7418-26 (Paz. substitutes here vagined, cf vàng); be ~ to burst out crying 1138. 3417.18, 511.4, �� gristan < *griy-istan formed from the pres. griy- < *grady-; * grad- SW form of garz-, v. girzitan and gil-. Ps. pt. glydyt = gliyit, pres. glydty = griyet; MPrs pres. gryy-; NP giristan giry-. Verbum 204 sq.
griv [SWLH] neck 271.3, 6514-17, — Av. (530) grivà-; NP giri; giri-bän ‘collar’, girivah ‘a low hill’. Cf gri-kaft and s. v. gurtēh.
grah [glwh] troop, company, with the indef. art. ~-ë [~+1] 84. - = Paz.; NP guroh.
guftan [gwptn'] gēb- [YMLLWN-,YMR- RWN-; 3d p. sg. gwbyt 128%, gwbyt' 9923, 1021, gwpyt' 2315 göbet], opt. 2nd p. sg. gobeš [YMRRWN-yš] 6012, pt. always gwpt' = guft: to say, to tell, to utter, to pronounce, to recite, passim; with 6 ‘to’, apar, rād (53) ‘concerning, of’ (patiš 6614); followed by direct speech introduced by ku, passim; with a
predicative: Hesm havand i Ahriman guft éstet H. is said to be equal to:
A. 6818: 7719-20, 7913-14-16, 8756.27 sq. 1068-9; with acc. c. inf. 11119, — authoritative religious sayings are in- troduced by the formulas cigon den göbet kü (36-54, passim), with hat instead of kū (387-8. 4325-26, 4414-15, 503-5), pat han + den gūbēt kü (43155), cigon ët i den gobet ku (533-24 ete.), seldom andar den guft estet ku 80"; regularly guft ēstēt is used of traditional, extracanonical sayings: 621-2, 6614. 6819. 6923, 7012, 1061-1, — with božišn, passax” and other subst., v. these; — apāc ~ to repeat 521-22; — apar ~ to utter loudly 45?!; — frže ~ to pro- nounce 581-?; v. also peš. — OP gaub-;
MPrs guftn gwy-; Paz. guftan, pres. 3d p. góéd, góid, gčend, gčind; NP guftan guy; the typical SW vb. for saying, as against NW vac-, v. vdeišneh.
guftär [gwpt']]: frāc ~ possessing the faculty of speech 38**. 3912-14,
== IEC
4354:grondhos, à (gronth-) ‘mass, tuft, bunch? Skt. cf. granthah, ih ‘knot’; Gk. grónthos ‘balled fist, punch’; Cor. gron ‘mass, bunch’; Br. cf. (?) grunn ‘mass, pile’; W (?) grwn, pl. grynau (fridge, baulk’, but cf. grondos, above); Latv. (ambiguous) grods ‘tightly twisted, knotted’
== SYN knot
13913:SCELLANEOUS PHYSICAL ACTS, ETC. 551 wisCE 9.192 KNOT (sb.) : Lith. mazgas aur knutr Lett. mazgs oe Dan. knude ChSl.  (qzlii) sae Sw. knut SCr.  uzao tod OE cnolta Boh. _uzel cud ME knotte Pol. wezel aD NE knot Russ. — uzel 7 Du. knoop Skt. — granthi- snaidm OHG knodo, knoto, knopf Av. pee snaidhm MHG  knode, knote, knopf NHG knoten
13921:7. Skt. granthi- : grath-‘tie’, this perh. : OE cradel ‘cradle’, OHG kratto ‘bas- ket’, fr. an extension of *ger- in words based on the notion of ‘twist, wind’. Walde-P. 1.593 ff. (595).
19695:11.45 PURSE Grk.  Badddvriov Goth. puggs Lith. — (pinigu) ma(K)x NG rouyyl ON sj0or, pungr Lett. naudas ) ma(i)ing Lat. marsupium, crumina Dan. pung ChSl.  vitlagaliSte It. borsa Sw.  pung SCr.  novéarka Fr. bourse OE stod, pung Boh. méec, vdéek (na Sp. bolsa ME spurs pentze) Rum. pungd NE purse (cod) Pol. worek (na Pieniqdze) Ir. Braue Du. (geld)buidel, beurs Russ. koSelek Nir. sparan OHG - seckil, scazfung, pfoso Skt. granthi- W. purs, cod MHG seckel, biutel Av. ne, Br. yalc’h NHG (geld)beutel
19738:7. Skt. granthi- ‘knot’ (9.192), used also of a knot in a corner of a garment for carrying coins, is the nearest approach to ‘purse’.
31813:Skt. nighantu-, a term applied to the old Vedic glossaries, a Mid. Ind. form of *nir-grantha- : Skt. grantha- ‘text’, granth- ‘tie’. Uhlenbeck 148. Wacker- nagel, Altind. Gram. 1.167. For the two Skt. words, see also Zachariae, Grd. indo-ar. Phil. 1.3B.1 f.
32536:18.61 BOOK Grk.  BbBros, BiBAlov Goth. bdkds Lith. knyga NG BtBXlov ON bok Lett. gramata Lat. liber Dan. bog ChSl. kinigy It. libro Sw. bok SCr. knjiga Tr. livre OE bic Boh. kniha Sp. libro ME book Pol. ksiqzka Rum. carte NE book Russ. kniga Ir. lebor Du. _boek Skt.  pustaka-, grantha- Nir.  leabhar OHG  buoh Av. a eens W. llyfr MHG buoch Br. leur NHG buch
32549:Skt. grantha-, lit. ‘tying, binding, knot’, whence ‘a joining together, com- position’ and ‘treatise, book’ : granth- ‘fasten, arrange, compose’. Walde-P. 1.595.
32625:Ir. (scriptur) Du. letterkunde Russ. . literatura, slovesnost’ Ni. litridheacht OHG (giscrip, scrift) Skt. grantha-, cdstra-
32645:6. Skt. grantha- ‘composition, literary production, book’ (18.61).
32651:Grk. ovyypadets Dan.  forfatter, skribent Lith. raSytojas NG avyypadebs, Aoyoré- Sw. skriftstallare, for- Lett. rakstnieks xens fattare SCr.  spisatelj, knjizeunik Lat.  scriptor, auctor OE writere Boh. _ptivodce, spisovatel It. autore, scriptore ME autor, writer Pol. autor, pisarz Fr. auteur, écrivain NE author, writer Russ. avtor, pisatel’ Sp. autor, escritor Du. schrijver Skt. grantha-kara-, -krt- Rum. scriitor, autor OHG _ scriptor Tr. augtor, scribnid MHG ithtare Nir. -ughdar, scriobnoir NHG verfasser, schrifisteller W. awdur Br. skrivagner
```


## [2026-09-05T20:54:04.320Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD; ls; grep -n \"grathnami\\|granth\\|grathn\" WLD_Bd1_1930_dli_70244_djvu.txt | head -10"
}
```


### [2026-09-05T20:54:04.371Z] TOOL RESULT

```
WLD_Bd1_1930_dli_70244_djvu.txt
WLD_Bd1_1930_dli_70244_text.pdf
WLD_Bd1_pages.txt
WLD_Bd2_1927_dli_106624_djvu.txt
WLD_Bd2_1927_dli_106624_text.pdf
WLD_Bd2_pages.txt
37201:Faust“ (das nicht besser zu ai. grantha-h „Knoten, Gefiige“ gestellt wird, 
37418:granth-, grathmlmi , fut. granthi&ynmi ..winden, kniipfen, einen Knoten bin- 
37420:granthi-h m. „Knoten, Gelenk, Anschwellung", grcintlia-h „Knoten“, grathtn- 
38660:,,Wange, Ivnoten, Anscliwellung, Beule, Kropf' (nicht mind. = granthah
```


## [2026-09-05T20:54:08.640Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD; sed -n '37405,37430p' WLD_Bd1_1930_dli_70244_djvu.txt; echo \"=== find page marker\"; grep -n \"\\[pdf page\" WLD_Bd1_pages.txt | head -3; python3 - <<'EOF'\nimport re\nt=open('WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\ni=t.find('grathmlmi')\nif i<0:\n    i=t.find('granth-, grath')\nprint(i)\n# find nearest preceding page tag\nj=t.rfind('[pdf page',0,i)\nprint(t[j:j+40])\nEOF"
}
```


### [2026-09-05T20:54:10.683Z] TOOL RESULT

```
grritnsfc ,, Strang aus gedrehten Baumzweigen. zum Binden und Hiingen" 
r'lit. ggrzulas „Deichsel" vermutlich ebenfalls aus , .Strang"'). — Ygl. Liden 
Stud. I 2 f. m. Lit. 

Dentalerveiterungen: 

idg. *yi-et(Ji)-. nasaliert * grmth : ags. crndol m. ..Wiege" ( *kradnhi - „ge- 
Hoehtenes"), ahd. kratto ,,Korb" (*km<lltin-), I rcz :o. mhd. krczzr, nhd. 



Krdtse „Korb“ ( *krattian , -tt aus oder zur Wzf. mit idg. d ?) ; ai. 

granth-, grathmlmi , fut. granthi&ynmi ..winden, kniipfen, einen Knoten bin- 
den", ptc. grathitd- , gewunden, verseblungen, knotig, zusammengeballt", 
granthi-h m. „Knoten, Gelenk, Anschwellung", grcintlia-h „Knoten“, grathtn- 
„rankevoll“, gratbila- ; ,yerriickt“, mit mind. Lautentw. ghatnte ,,sich ver- 
binden, vereinigen mit; eifrig bescliaftgt sein", kaus. ,.zusammenfiigen, zu- 
stande bringen". 

Das mit grnntha-h scheinbar sich deekende gr. ygovdog „Faust“ dagegen 
zu *ger-, *grcm „fassen". 

idg. *ger-d, *gr-cd -, nasaliert *grend- : anord. kartr. ags. era:! m. „Wagen“ 
(wohl „geflochtener "Wagenkorb", wohl auch anord. Jcurt-nngl, norw. kart m. 
„unreife Frucht, Knorren", ostfries. kret „verschrumpfte Frucht" 'also nieht 
=== find page marker
2912266
```


## [2026-09-05T20:54:20.320Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; for u in \"https://en.wiktionary.org/wiki/گره\" \"https://en.wiktionary.org/wiki/گروه\" \"https://en.wiktionary.org/wiki/group\" \"https://en.wiktionary.org/wiki/grape\" \"https://en.wiktionary.org/wiki/curl\"; do timeout 120 python3 tools/fetch_source.py \"$u\" --note \"page 173, root Ger 1: check derivation\" ; done"
}
```


## [2026-09-05T20:54:22.410Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; for u in \"https://www.etymonline.com/word/group\" \"https://www.etymonline.com/word/grape\" \"https://www.etymonline.com/word/curl\" \"https://en.wiktionary.org/wiki/%E0%A4%97%E0%A5%8D%E0%A4%B0%E0%A4%A8%E0%A5%8D%E0%A4%A5%E0%A4%BF\"; do timeout 120 python3 tools/fetch_source.py \"$u\" --note \"page 173, root Ger 1: check derivation\"; done"
}
```


### [2026-09-05T20:54:24.591Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/61b7b3523dc1366b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6668bc110af63a3b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/913d6934e1fb9724.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/46f0fad95e30ab06.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/06ec0e19b2bf67ca.txt
```


### [2026-09-05T20:54:34.162Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/c82e599f618bf3af.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/2e533a083ede9901.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1fc472c392096550.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ab4a25d8da39eb54.txt
```


## [2026-09-05T20:54:36.741Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; for f in 61b7b3523dc1366b 6668bc110af63a3b; do echo \"##### $f\"; grep -n -i -A6 \"Etymology\" $f.txt | head -60; done"
}
```


### [2026-09-05T20:54:38.360Z] TOOL RESULT

```
##### 61b7b3523dc1366b
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Noun 
--
151: Etymology
152- [ edit ] 
153-
154- From Proto-Iranian *graθH- ( “ to tie (a knot) ” ) , from Proto-Indo-Iranian *grantH- ( “ to tie (a knot) ” ) , and cognate with Sanskrit ग्रन्थ् ( granth , “ to tie (a knot) ” ) and with Northern Kurdish girê ( “ knot ” ) with further origin uncertain. The traditional derivation from Proto-Indo-European *gre(n)tH- ( “ to tie ” ) (itself a hypothetical extension of Proto-Indo-European *ger- ( “ to twist ” ) ) would make the root cognate with Proto-Germanic *kradô ( “ wicker basket ” ) , whence English cradle ; however, this is not certain, as the Germanic word could very well be of substrate origin instead.
155-
156- Pronunciation
157- [ edit ] 
##### 6668bc110af63a3b
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Noun 
--
154: Etymology
155- [ edit ] 
156-
157- Inherited from Middle Persian 𐭢𐭥𐭥𐭤 ( glwh’ /⁠grōh⁠/ , “ group, crowd ” ) , possibly from Proto-Indo-European *ger- ( “ to twist, wind (into a mass) ” ) and cognate with گره ( gereh , “ knot, tie ” ) , as well as Sanskrit ग्रन्थ् ( granth , “ to tie, string together ” ) . [ 1 ] Compare English group .
158-
159- Pronunciation
160- [ edit ]
```


## [2026-09-05T20:54:44.762Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; sed -n '150,230p' 6668bc110af63a3b.txt"
}
```


### [2026-09-05T20:54:44.805Z] TOOL RESULT

```
 Persian
 [ edit ] 

 Etymology
 [ edit ] 

 Inherited from Middle Persian 𐭢𐭥𐭥𐭤 ( glwh’ /⁠grōh⁠/ , “ group, crowd ” ) , possibly from Proto-Indo-European *ger- ( “ to twist, wind (into a mass) ” ) and cognate with گره ( gereh , “ knot, tie ” ) , as well as Sanskrit ग्रन्थ् ( granth , “ to tie, string together ” ) . [ 1 ] Compare English group .

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /ɡu.ˈroːh/ 

 ( Dari, formal ) IPA ( key ) : [ɡʊ.ɾoːʱ] 

 ( Dari, formal ) IPA ( key ) : [ɡʊ.ɾoːʱ] 
 ( Kabuli ) IPA ( key ) : [ɡʊ.ɾoː] 

 ( Hazaragi ) IPA ( key ) : [ɡu.ɾʊː] 

 ( Iran, formal ) IPA ( key ) : [ɡ̥o.ɹuːʱ] 

 ( Tajik, formal ) IPA ( key ) : [ɡu.ɾɵʰ] 

 Rhymes: -oːh 

 Readings

 Classical reading ? 

 gurōh

 Dari reading ? 

 gurōh

 Iranian reading ? 

 goruh

 Tajik reading ? 

 gurüh

 Audio ( Iran ) : ( file ) 

 Noun
 [ edit ] 

 Dari

 گُروه 

 Iranian Persian

 Tajik

 гурӯҳ 

 گروه • ( gurōh / goruh ) ( plural گُروه‌ها , or گُروهان , Tajik spelling гурӯҳ ) 

 group ( of countries, people, etc. ) 
 گروه ۱+۵ ― goruh -e panj be alâve-ye yek ― P5+1 
 c. 1260s , Jalāl ad-Dīn Mohammad Rūmī , translated by Reynold A. Nicholson , مثنوی معنوی [ Masnavi-ye-Ma'navi ], volume III, verse 2752: ما نه زان پیلان گولیم ای گروه / که اضطراب ماه آردمان شکوه mā na z-ān pīlān-i gōl-ēm ay gurōh / ki iztirāb-i māh āradmān šikōh ( Classical reading ) O company [of prophets], we are not [to be reckoned] among those stupid elephants who are terrified by the disturbance of the Moon. 

 Derived terms
 [ edit ] 

 گُروهی ( gurōhī ) 

 Descendants
 [ edit ] 

 Tajik: гурӯҳ ( gurüh ) 

 → Chagatai: کروه ( krwh /⁠gurūh⁠/ ) 
 Uyghur: گۇرۇھ ( guruh ) 

 Uzbek: guruh
```


## [2026-09-05T20:54:49.202Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; grep -n -i \"Hasandust\\|References\" -A8 6668bc110af63a3b.txt | sed -n 1,40p; echo \"=== gereh readings\"; sed -n '150,200p' 61b7b3523dc1366b.txt"
}
```


### [2026-09-05T20:54:49.264Z] TOOL RESULT

```
77: References 
78-
79- Toggle the table of contents 
80-
81- گروه 
82-
83- 11 languages 
84-
85- فارسی 
--
251: References
252- [ edit ] 
253-
254- ^ Nourai, Ali ( 2011 ), “Ger 1”, in An Etymological Dictionary of Persian, English and other Indo-European Languages , page 143 
255-
256- Retrieved from " https://en.wiktionary.org/w/index.php?title=گروه&oldid=92291467 "
257-
258- Categories : Persian terms inherited from Middle Persian 
259- Persian terms derived from Middle Persian 
=== gereh readings

 Etymology
 [ edit ] 

 From Proto-Iranian *graθH- ( “ to tie (a knot) ” ) , from Proto-Indo-Iranian *grantH- ( “ to tie (a knot) ” ) , and cognate with Sanskrit ग्रन्थ् ( granth , “ to tie (a knot) ” ) and with Northern Kurdish girê ( “ knot ” ) with further origin uncertain. The traditional derivation from Proto-Indo-European *gre(n)tH- ( “ to tie ” ) (itself a hypothetical extension of Proto-Indo-European *ger- ( “ to twist ” ) ) would make the root cognate with Proto-Germanic *kradô ( “ wicker basket ” ) , whence English cradle ; however, this is not certain, as the Germanic word could very well be of substrate origin instead.

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /ɡi.ˈrih/ 

 ( Dari, formal ) IPA ( key ) : [ɡɪ.ɾɪ́ʱ] 

 ( Dari, formal ) IPA ( key ) : [ɡɪ.ɾɪ́ʱ] 
 ( Kabuli ) IPA ( key ) : [ɡɪ.ɾɪ́] 

 ( Hazaragi ) IPA ( key ) : [ɡi.ɾí] 

 ( Iran, formal ) IPA ( key ) : [ɡʲe.ɹéʱ] 

 ( Tajik, formal ) IPA ( key ) : [ɡi.ɾéʱ] 

 Rhymes: -ih 

 Readings

 Classical reading ? 

 girih

 Dari reading ? 

 gireh

 Iranian reading ? 

 gereh

 Tajik reading ? 

 gireh

 Noun
 [ edit ] 

 گره • ( girih / gereh ) ( Tajik spelling гиреҳ ) 

 knot 

 tie
```


## [2026-09-05T20:55:05.233Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; for f in c82e599f618bf3af 2e533a083ede9901 1fc472c392096550; do echo \"##### $f\"; head -c 3000 $f.txt | tail -c 2200; echo; done"
}
```


### [2026-09-05T20:55:07.773Z] TOOL RESULT

```
##### c82e599f618bf3af
ds.

 Origin and history of group 

 group (n.) 

 1690s, originally an art criticism term, "assemblage of figures or objects forming a harmonious whole in a painting or design," from French groupe "cluster, group" (17c.), from Italian gruppo "group, knot," which probably is, with Spanish grupo , from a Germanic source, from Proto-Germanic *kruppaz "round mass, lump," part of the general group of Germanic kr- words with the sense "rounded mass" (such as crop (n.).

 Extended to "any assemblage, a number of individuals related in some way" by 1736. Meaning "pop music combo" is from 1958. As it was borrowed after the Great Vowel Shift in English, the pronunciation of the -ou- follows French rather than English models.
 also from 1690s 

 group (v.) 

 "form into a group or groups," 1718 (transitive), 1801 (intransitive), from group (n.). Related: Grouped ; grouping .
 also from 1718 

 Entries linking to group 

 crop (n.) 

 Old English cropp "head or top of a sprout or herb, any part of a medicinal plant except the root," also "bird's craw" (the common notion is "protuberance"), cognate with Old High German kropf , Old Norse kroppr .

 "The word has a remarkable variety of special senses ..." [Century Dictionary]. OED writes that "OE. had only sense 1. 'craw of a bird' and 3. 'rounded head or top of a herb'; the latter is found also in High German dialects (Grimm, Kropf , 4 c ); the further developments of 'head or top' generally, and of 'produce of the field, etc.' appear to be exclusively English."

 Meaning "grain and other cultivated plants grown and harvested" (especially "the grain yield of one year") is from early 14c. (in Anglo-Latin from early 13c.). Probably this sense development is via the verbal meaning "cut off the top of a plant" (c. 1200).

 From the notion of "top" comes the sense "upper part of a whip," hence "handle of a whip" (1560s), hence "a kind of whip used by horsemen in the hunting field" (1857). "It is useful in opening gates, and differs from the common whip in the absence of a lash" [Century Dictionary].

 General sense of "anything gathered when ready or in season" is from 1570s. Meaning "a thick, short head of hair" is from 1795. M
##### 2e533a083ede9901
rapfo "hook;" also see cramp (n.2)). The original notion thus perhaps was "vine hook for grape-picking." The vine is not native to England. The word replaced Old English winberige "wine berry." Spanish grapa , Italian grappa also are from Germanic.

 also from mid-13c. 

 Entries linking to grape 

 cramp (n.2) 

 early 15c., "metal bar bent at both ends," from Middle Dutch crampe or Middle Low German krampe , from Proto-Germanic * kramp-. It is thus the same word as cramp (n.1). Metaphoric sense of "something that confines or hinders" is attested by 1719.

 grapefruit (n.) 

 1814, from grape + fruit . Said to have been so called for its taste, or perhaps because it grows in clusters. Perhaps a marketing name; it was known by various names ( pomelo , shaddock ) before the current one emerged. The fruit itself was known since 1693 (in Hans Sloane's catalogue of Jamaican plants); presumably it originated in Jamaica from chance hybrids between other cultivated citrus. An ornamental plant chiefly at first, not much eaten until late 19c.

 grapeshot 
 grapevine 
 grapnel 
 grappa 
 See All Related Words (6) 

 Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 More to explore

 grapeshot 

 also grape-shot, 1747, from grape + shot (n.). So called for its appearance. Originally simply grape (1680s), a collective singular. The whiff of grapeshot was popularized in English from 1837, from Carlyle's history of the French Revolution (in which book it was a chapter title)

 grapevine 

 also grape-vine, 1736, from grape + vine. Meaning "a rumor; a secret or unconventional method of spreading information" (1863) is from the use of grapevine telegraph as "secret source of information and rumor" in the American Civil War; in reference to Southerners under northern 

 Shiraz 

 As the name for a red wine made from a type of grape grown in the Rhône valley of France, it is recorded from 1908, from...French syrah, the name apparently being altered in English on the mistaken notion that the grape was brought to Europe from...The Iranian place name is said to be from Elamite sher "good" + raz "grape."...

 raisin 

 "dried
##### 1fc472c392096550
URL: https://www.etymonline.com/word/curl
FETCHED: 2026-09-05T20:54:33Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 504: Gateway Timeout
```


## [2026-09-05T20:55:12.276Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; grep -n -m1 -B3 -A6 \"Origin and history of grape\" 2e533a083ede9901.txt; cd /home/sfmqrb/git/rishe; timeout 120 python3 tools/fetch_source.py \"https://www.etymonline.com/word/curl\" --note \"page 173, node 14 curl < Middle Dutch crulle\"; sleep 1"
}
```


### [2026-09-05T20:55:15.038Z] TOOL RESULT

```
18- Advertisement Remove Ads 
19- Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
20-
21: Origin and history of grape 
22-
23- grape (n.) 
24-
25- mid-13c., "a grape, a berry of the vine," also collective singular, from Old French grape "bunch of grapes, grape" (12c.), probably a back-formation from graper "steal; grasp; catch with a hook; pick (grapes)," from a Frankish or other Germanic word, from Proto-Germanic *krappon "hook," from a group of Germanic words meaning "bent, crooked, hooked" (cognates: Middle Dutch crappe , Old High German krapfo "hook;" also see cramp (n.2)). The original notion thus perhaps was "vine hook for grape-picking." The vine is not native to England. The word replaced Old English winberige "wine berry." Spanish grapa , Italian grappa also are from Germanic.
26-
27- also from mid-13c. 
/home/sfmqrb/git/rishe/data/verification/sources/web/1fc472c392096550.txt
```


## [2026-09-05T20:55:18.096Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; grep -n -m1 -A8 \"Origin and history of curl\" 1fc472c392096550.txt; echo \"=== wikt curl\"; grep -n -m1 -A6 \"Middle Dutch\\|Etymology\" 06ec0e19b2bf67ca.txt | head -30"
}
```


### [2026-09-05T20:55:18.160Z] TOOL RESULT

```
=== wikt curl
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Noun
```


## [2026-09-05T20:55:20.822Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; head -5 1fc472c392096550.txt; echo ---; grep -n -i \"crulle\\|krul\\|metathes\" 06ec0e19b2bf67ca.txt | head"
}
```


### [2026-09-05T20:55:20.877Z] TOOL RESULT

```
URL: https://www.etymonline.com/word/curl
FETCHED: 2026-09-05T20:54:33Z
STATUS: -1
TITLE: 

---
220: From metathesis of Middle English crulle ( “ curled, curly ” ) , of uncertain origin but probably from an unrecorded Old English word or from Middle Dutch crul , crulle ( “ curl ” ) , ultimately from Proto-Germanic *kruzlǭ ( “ bent or crooked object, curl ” ) , connected to *krūsą ( “ curl ” ) , of unknown origin. [ 1 ] 
222: Cognate with Saterland Frisian Krulle ( “ curl, lock ” ) , West Frisian krul ( “ curl ” ) , Dutch krul ( “ curl ” ) , German Low German Krull ( “ curl ” ) , dialectal German Krolle ( “ curl ” ) , Danish krølle ( “ curl ” ) , Norwegian Bokmål krøll ( “ curl ” ) . Related also to Saterland Frisian Kruus ( “ curl ” ) , German kraus ( “ frizzy, crumpled, curly ” ) , Danish krus ( “ curl ” ) , Swedish krusa ( “ to crimp, curl ” ) . Compare also Gothic 𐌺𐍂𐌹𐌿𐍃𐍄𐌰𐌽 ( kriustan , “ to grind, crush, gnash ” ) .
379: Dutch: krul   (nl)   m or f , lok   (nl) 
959: Categories : English words derived through metathesis
```


## [2026-09-05T20:55:27.999Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== KLN curl\"; grep -n -m2 \"curl,  n\\|curl, n\" KLN_1966.txt | head; python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\ni=t.find('curl,  n')\nprint(t[i-200:i+700])\nEOF"
}
```


## [2026-09-05T20:55:29.816Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== SKT\"; grep -n -m3 \"Curl\\|Grape\\|Group\" SKT.txt | head; python3 - <<'EOF'\nt=open('SKT.txt',encoding='utf-8',errors='replace').read()\nfor w in ['GROUP,','GRAPE,','CURL,']:\n    i=t.find(w)\n    print('###',w,i)\n    print(t[i:i+500] if i>0 else '')\nEOF"
}
```


### [2026-09-05T20:55:29.840Z] TOOL RESULT

```
== KLN curl
9968:curl,  tr.  and  intr.  v.  —  ME.  curlen,  metathesized fr.  ME.  crullen,  fr.  crul,  ‘curly’,  which  is  rel.  to Norw.  krull,  Dan.  krolle,  E.  Fris.  krul,  krulle, MDu.  crulle,  crolle,  crul,  Du.  krul,  ‘curl’,  Norw. krulla,  Dan.  krolle,  MDu.  crullen,  crollen,  Du. krullen,  ‘to  curl’,  MHG.  krol,  ‘curly’,  E.  Fris. krillen,  ‘to  bend,  twist’.  Cp.  cruller.  For  the metathesis  of  ME.  crullen  to  curlen  cp.  curd. Derivatives:  curl,  n.,  curl-ed,  adj.,  curl-ed-ly, adv.,  curl-ed-ness,  n.,  curl-er,  n.,  curbing,  n.  and adj.,  cur l-y,  curl-i-ness,  n. curlew,  n.,  any  of  several  kinds  of  wading  birds.
ullen,  crollen,  Du. krullen,  ‘to  curl’,  MHG.  krol,  ‘curly’,  E.  Fris. krillen,  ‘to  bend,  twist’.  Cp.  cruller.  For  the metathesis  of  ME.  crullen  to  curlen  cp.  curd. Derivatives:  curl,  n.,  curl-ed,  adj.,  curl-ed-ly, adv.,  curl-ed-ness,  n.,  curl-er,  n.,  curbing,  n.  and adj.,  cur l-y,  curl-i-ness,  n. curlew,  n.,  any  of  several  kinds  of  wading  birds.
—  OF.  corlieu,  courlicu  (F.  courlis),  of  imitative origin.
curmudgeon,  n.,  a  churlish,  surly,  ill-tempered
386
387
person.  —  Of  unknown  origin.
Derivatives :  curmudgeon-ish,  curmudgeon-ly, adjs.
curr,  intr.  v.,  to  make  a  murmuring  sound,  to purr.  —  Of  imitative  origin, currach,  curragh,  n.,  a  coracle.  —  Ir.  currach, ‘boat,  little  ship’,  rel.  to  Gael,  curach,  of  s.m., W.  corwgl,  cwrwgl,  ‘coracle’.  See  coracle, currant,  n.,  1)  a  small  seedless  raisi
```


### [2026-09-05T20:55:31.532Z] TOOL RESULT

```
== SKT
7939:Grapnel.  Grapple ;  see  Grape.
23980:curl,  criip,  wind,  cum;'  Sewel.  Bailey dcfioe*  crewei  as  *  two-twisted  worsted.*  See Curl.
### GROUP, -1

### GRAPE, -1

### CURL, -1
```


## [2026-09-05T20:55:35.664Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('SKT.txt',encoding='utf-8',errors='replace').read()\nimport re\nfor w in ['Group.','Grape.','Curl.']:\n    for m in re.finditer(re.escape(w),t):\n        s=t[m.start()-120:m.start()+420]\n        if 'F.' in s or 'Du.' in s or 'Ital' in s:\n            print('###',w); print(s.replace('\\n',' ')); print(); break\nEOF"
}
```


### [2026-09-05T20:55:37.477Z] TOOL RESULT

```
### Curl.
&  b\o«  <sa  liic  cm- curl,  criip,  wind,  cum;'  Sewel.  Bailey dcfioe*  crewei  as  *  two-twisted  worsted.*  See Curl. Cringle,  u  iron  ring.  <Sciuid.)  Icel. kringia,  a  circle ;  cf.  Jtrittgar,  pL,  the pollies  of  a  dra^-net.  Allied  lo  Du.  kring, A  circle.  Swed.  kring.  prep,,  around;  also Co  Crinkle.  Crank  (i),  and  Cringe. Crumpet,  a  kind  of  soft  bread -cake. (W.)  Prob.  from  W.  erempog  lalso  cramm^ ivyeh),  a  [ULDcake.  a  fritter. Crxiety,  ill-tempered.  (E.)  Prob.  for tunty,  i.e.  cur
```


## [2026-09-05T20:55:41.017Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i \"gruppo\\|groupe\" SKT.txt | head; echo ===; grep -n -i -m5 \"Curl,\\s*to\" SKT.txt | head; echo ===; grep -n \"Grape,\" SKT.txt | head"
}
```


### [2026-09-05T20:55:41.083Z] TOOL RESULT

```
Exit code 1
(eval):1: == not found
```


## [2026-09-05T20:55:43.912Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i \"gruppo\" *.txt | head; echo \"-- grape in FSD/WEB --\"; grep -n -i \"gruppo\" FSD_vol2.txt WEB_vol1.txt 2>/dev/null | head"
}
```


### [2026-09-05T20:55:44.009Z] TOOL RESULT

```
AHD_watkins1985.txt:494:vine, grape: GRAPE; c. Old French grapon, grapnel: GRAPNEL; d. Old French grape, a hook: GRAPPLE; e. Ital- ian dialectal grappa, vine stem, brandy: GRAPPA. 2. Old English crump, crumb, crooked, bent, stooping: CRUM- MIE, CRUMPET, (CRUMPLE). 3. Low German krimpen, to wrinkle: CRIMP!. 4. Middle Dutch crampe, hook, and Frankish *kramp, hook: cramMpP?. 5.Old High German krampfo, a cramp, akin to the Germanic source of Old French crampe, cramp: CRAMP!. 6. Old English crypel, a cripple: CRIPPLE. 7. Germanic *kreupan in Old English créopan, to creep: CREEP. 8. Middle Low German krink, a ring: CRINGLE. 9. Germanic *krengan in Old English cringan, to yield: CRINGE. 10. Middle Dutch crinkelen, akin to Middle English crinkelen, to make kinks in: CRINKLE. 11. Old Norse kriki, a bend, nook: CREEK. 12. Old Norse krékr, a hook: cRooOK. 13. Frankish *krok- (> Old French croc), a hook: CROCHET, (CROCKET), (CROQUET), (CROUCH); ENCROACH. 14. Old English crycc, (bent) staff, crutch: CRUTCH. 15. Old French crosse, crook: CROSIER, LACROSSE. 16. Middle Dutch crulle, curly: CRULLER, CURL. 17. Old English cranc-(stzf), a weaving implement: CRANK}. 18. Norwegian krake, a sickly beast, akin to the source of Middle English crok, an old ewe: cRocK3, 19. Old Norse karpa, to boast: CaRP!, 20. Middle Dutch kroes, curled, akin to the source of Old French grosele, gooseberry: GROSSULARITE. II. Words meaning ‘“‘a rounded mass, collection; a round object, vessel, container.” 1. Old English cruma, a frag- ment: CRUMB. 2. Frankish *kruppa, rump, akin to the Germanic source of Old French croup, rump: CROUP?, (CROUPIER), CRUPPER. 3. Old English cropp, cluster, bunch, ear of corn: crop. 4. Italian gruppo, an assem- blage: Group. 5. Old English crocc, pot: CROCK}. 6, Mid- dle Dutch cruyse, pot: CRUSE. 7. Old English cribb, manger: CRIB. 8. Old English cradel, cradle: CRADLE. 9. Frankish *kripja, cradle, akin to the Germanic source of Old French cre(s)che, crib: CRECHE. 10. Old English creet and Old Norse kartr, wagon: CART. 11. Old English croft, small enclosed field: crort. [Pok. 3. ger- 385.] gerbh-. To scratch. 1. Germanic *kerban in Old English ceorfan, to cut: CARVE. 2. Zero-grade Germanic form *kurbiz in Old English cyrf, a cutting (off): KERF. 3. Variant form *grebh- in: a. Germanic *krab(b)- in Old English crabba, a crab: CRAB}; b. Germanic *krabiz- in Old French crevise, crayfish: CRAYFISH; C. perhaps Ger- manic *krab- in Old Norse krafla, to crawl: CRAWL. 4. Zero-grade form *grbh- in Greek graphein, to scratch, draw, write, and gramma (< *grbh-mn), a picture, writ- ten letter, piece of writing, and grammé, a line: GRAF- FITO, GRAM!, -GRAM, GRAMMAR, GRAPH, -GRAPH, -GRAPHER, GRAPHIC, -GRAPHY; AGRAPHA, AGRAPHIA, DIAGRAM, EPIGRAM, (EPIGRAPH), GRAPHITE, ICONOGRA- PHY, PARAGRAPH, PROGRAM, PSEUDEPIGRAPHA, TETRA- GRAMMATON, TOPOGRAPHY. [Pok. gerebh- 392.] [gerere. To carry, carry on, act, do. Latin verb of un- known origin. Oldest form ges-, past participle gestus. GERENT, GERUND, (GEST), GESTATION, (GESTICULATE), GESTURE, JEST; ARMIGER, BELLIGERENT, (CONGERIES), CONGEST, DIGEST, EGEST, INGEST, REGISTER, SUGGEST, VELIGER.] gere-'. To grow old. 1. Suffixed lengthened-grade form *géro-s- in Greek géras, old age: AGERATUM, CALOYER, GERIATRICS. 2. Suffixed form “gera-ont- in Greek geron (stem geront-), old man: GERONTO-. [Pok. ger- 390.] gere-2. To cry hoarsely; also the name of the crane. I, Words meaning “‘to cry hoarsely”; also words denoting the crow. 1, Germanic *kré- in: a. Old English crawe, a crow: CROW}; b. Old English crdwan, to crow: CROW?; c. Old English cracian, to resound: CRACK; d. Middle Dutch krdken, to crack: CRACKNEL; @. Old Norse kraka, a crow: CRAKE. f. Middle Dutch krdnen, to groan, la- ment: CROON. 2. Possibly (but more likely imitative) Germanic *kur(r)- in Old Norse kurra, to growl, akin to Middle English curre, cur: cur. II. Words denoting a
KLN_1971.txt:106715:group, n. — F. groupe , fr. It. gruppo, ‘group’, 
KLN_1966.txt:16766:group,  n.  —  F.  groupe,  fr.  It.  gruppo,  ‘group’, orig.  'cluster,  packet,  knot’,  fr.  OProven?. grop,  ‘knot’,  which  derives  fr.  Teut.  *kruppa, ‘a  rounded  lump  or  mass’.  See  crop. Derivatives :  group,  tr.  and  intr.  s.,group-ed,  adj. group-ing,  n.
WEB_vol1.txt:4547:2. injured in one’s legal rights. ighted. aggrouped (-grépt’), pl., Pp. aggrouping, ppr. [Fr. agrouper; It. agerup- pare; a, to, and gruppo, a knot, heap, group | to bring together; to group. $
WEB_vol1.txt:84959:group, n. (Fr. groupe; It. gruppo, a knot. lump, group; of Germanic origin; compare G. kropf, a bunch, a crop.]
WEB_vol1.txt:85074:gruppo
WEB_vol1.txt:85083:grunting ly, grun/tle, v.i. to grunt; to sulk. grunt/ling, n. a young hog. gruppo, n. [It.] in music, 4
SYN.txt:23711:13.192. Note on other words for a col- lective body (of persons, animals, or things). NE group (fr. Fr. groupe, fr. Ital. gruppo : groppo ‘knot’), in earliest use an art term (group of sculptured or painted figures), has become the most nearly generic term; but even this is not applied to animals. For the most part, instead of any generic term, there is a wealth of individualistic terms, differ- entiated according to the object re- ferred to. Thus, to illustrate from one language only, though a parallel variety may be seen elsewhere, note the follow- ing NE words (excluding military terms like battalion, brigade, squadron, etc., and otherwise far from exhaustive), with their most familiar applications (these are not exclusive; in fact, most of those commonly used of certain animals are sometimes used also of others and of persons). For the etymology and range of use, cf. NED. :
-- grape in FSD/WEB --
WEB_vol1.txt:4547:2. injured in one’s legal rights. ighted. aggrouped (-grépt’), pl., Pp. aggrouping, ppr. [Fr. agrouper; It. agerup- pare; a, to, and gruppo, a knot, heap, group | to bring together; to group. $
WEB_vol1.txt:84959:group, n. (Fr. groupe; It. gruppo, a knot. lump, group; of Germanic origin; compare G. kropf, a bunch, a crop.]
WEB_vol1.txt:85074:gruppo
WEB_vol1.txt:85083:grunting ly, grun/tle, v.i. to grunt; to sulk. grunt/ling, n. a young hog. gruppo, n. [It.] in music, 4
```


## [2026-09-05T20:55:52.213Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('WEB_vol1.txt',encoding='utf-8',errors='replace').read()\nimport re\nfor pat in [r'grape, n\\.', r'curl, v\\.', r'curl, n\\.', r'crumb, n\\.', r'cradle, n\\.', r'cripple, n\\.']:\n    m=re.search(pat,t)\n    print('###',pat, bool(m))\n    if m: print(t[m.start():m.start()+400].replace('\\n',' '))\nEOF"
}
```


### [2026-09-05T20:55:55.041Z] TOOL RESULT

```
### grape, n\. True
grape, n. [OFr. grape, grappe, a bunch ter of grapes, from O.H.G. or clus. deen)” J G. chrapho, a hook, 1. any of various small, ro: skinned, juicy fruits, generally pues Booth. green, growing in clusters on a wood: Ted, or grapes are na raw, gea to make wine, o dried to make raisins: they inaa berries. y are classified ag 2. any of various vines bearin grapevine, 3. a dark purplish red. 4, [pl.] 
### curl, v\. False
### curl, n\. False
### crumb, n\. False
### cradle, n\. False
### cripple, n\. False
```


## [2026-09-05T20:56:19.439Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i \"gratha\\|granth\\|grav\" KNT.txt | head -15; echo \"== BRT\"; grep -n -i \"granθ\\|gran0\\|grantha\" BRT.txt | head"
}
```


### [2026-09-05T20:56:19.497Z] TOOL RESULT

```
327:$1. OLD Persian is the name applied to the Persian language used in the cuneiform inserip- tions of the Achaemenian dynasty; it can be localized as the language of southwestern Persia, or Persis in the narrower sense, and was the vernacular speech of the Achaemenian rulers. The OP inscriptions are commonly accompanied also by translations into Elamite and Accadian, en- graved in other types of cuneiform writing, and sometimes by an Aramaic version or an Egyptian hieroglyphic version. Linguistically, OP belongs to the Iranian branch of Indo-Iranian or Aryan, which is one of the main divisions of the Indo- European family of languages.
412:$3. Tne ScmrPr or THE Or» Persian IN- SCRIPTIONS 18, a8 we have said, of the cuneiform type: that is, the characters are made of strokes Which can be impressed on soft materials by a stylus having an angled end. The OP inscrip- tions, being on hard materials, must have been made with engraving tools with which the strokes
477:(Hamadan) in Media; though the two kings are spoken of in them only as ‘king in Parsa = Persis’, which was quite distinct from Media. They may have been set up in the time of Artaxerxes П as part of an anti-Cyrus propaganda, since Cyrus the Great had dethroned Arsames, and Cyrus the Younger came very near de- feating and killing Artaxerxes II at Cunaxa (cf. JAOS 66.206-12). The gold tablet A?Hc may have been a third in the same series; all three are in Old Persian only. *Cf. especially Schaeder, SbPAW 1931.636-42. 4 They are hardly to be ascribed to Cyrus the Younger, despite Wb. ZDMG 48.653-65 (cf. also KIA lxvii-bax) on CMa, which alone was known to him; for the opposing view, cf. Hz. Klio 8.1 ff. * Though perhaps not much used by him. The other three known inscriptions of Cyrus the Great are in Akkadian; but Strabo 15.3.7-8 (page 730), on the authority of Onesicritus, states that the tomb of Cyrus at Pasargadae bore at least two inscriptions, one being bilingual, Greek and Persian. We need attach no importance to the identification of the languages by Onesicritus, but the account indicates that Cyrus had inscriptions engraved in more than one language; in which case it is unlikely that his own vernacular was omitted. Cf. JAOS 66.206-12; but also Hinz, ZDMG 96.343-9.
790:unless indeed the engraver has omitted the word -
793:$54. ALTERATION OF CHARACTERS BY OMIS- SION OR ADDITION OF A STROKE sometimes occurs, altering the value; the error may be either in original engraving, or in the reading by the modern observer:
1165:Other examples of OP 0 from pIE Ё are to be seen in akala-, 6urd-, da"d-, Guxra-, Gravahara-, and perhaps in @digurci-, Oalagu-, Üarimi-; see Lex. s.vv.
1204:593. PIE $t (from Ё or ў + f) became pAr. &, and then plran. š, OP and Av. š, and Skt. st; these clusters are seen in derivatives with a t-sufhx: pIE *pik-to-, OP ni-pista- ‘engraved’; *peik-t- in
1305:pIE *peik-s- in OP (aor) niy-apaišam “1 en- graved’, cf. Skt. piádtz ‘he cuts, adorns’,
2608:$238. THe INFINITIVE occurs in OP only in the present active, with the suffix -tanazy, the ancestor of the NPers, infinitive ending -tän or -ddn: carta- naiy ‘to do’, to kar-; ka*tanaty ‘to dig’, to kan-, cf. NPers. kdndén; bartanaiy ‘to bear’, to bar-; тїраї {апаш ‘to engrave’, to nt-paid-. The c- of cartanaty is evidence for the -e- ablaut-grade in this formation ($98); NPers. kárdün ‘to do’ has k- gen- eralized from the rest of the paradigm.-In form,
2824:! Bv. TPS 1945.610 suggests that the engraver acci- dentally omitted martiyé before tyaišaiy, and then in- serted it after fratama when he noticed the omission. * Cf. the similar usage in Latin: Caesar, BG 1.12 quae pars civitatis Helvétiae insignem calamitatem populo Ro- mano intulerat, ea princeps poends solvit, ? The same use occurs also in Latin: Cic. ad Fam. 12.23.2 legionibus . . . {чаз sibi concilüre pecüniü cogitabat eüsque ad urbem addücere.
3295:DB = Dans, BeursTAN: The inscription of Behistan, trilingual, is inscribed on the face of a gorge in the cliff rising on the left-hand side of the main caravan route from Baghdad to Teheran, about 65 miles before reaching Hamadan. Here, at the height of about 225 feet (obliquely 322 feet) above the road, the last 100 feet being steep and difficult, rock-climbing—the final portion being in part cut smooth by Darius's orders, to prevent access by vandals—sculptures and accompanying inscriptions are engraved in the natural rock. The panel of the sculptures contains at the left the standing figure of Darius, with two attendants behind him; his right foot is firmly planted on the prostrate figure of Gaumata. Beyond Gaumata stand m line the captive rebels, 9 in number, with hands tied behind their backs and a rope around their necks linking them together. Above, there is a figure of the God Ahuramazda. The inscrip- tions in OP, Elam., and Akk. occupy the free parts of the panel and its lower margin, as well as the spaces below, to right, to left, and diagonally below to the left. These have suffered both from erosion by water torrents and by limestone in- crustations deposited by water in and over the engraved characters. Further damage was suffered
3323:Tm. Lex. 43-8 (1908); Wb. Grab, in AbkSGW 29.1.1-54 and 8 Plates (1911); Wb. KIA xviu-xx, 86-99 (1911); Tm. The Grave of King Darius at Naksh-i-Rustam, in Madrassa Jubilee Volume 108-72 (1914); Hz. ZDMG 80.244 (1926; on Ara- maie version), AMI 3.8 (1931), ApI 4.18 No. 4 and Plates 3-5 (1938; some fragments of a second сору of DNb, found at Persepolis, on Plate 5); Kent, Lg. 15.160-77 (1939); Sen, OPI 96-107, 240-51 (1941); Kent, JNES 4.39-52, 232-3 (1945); Bv. TPS 1945.39-50 (1946); GGCameron, Per- sepolis Treasury Tablets 29 (1948; on Aramaic version); Hinz, Orientalia [Rome] 1950 No. 4 (shortly to appear).
3359:Хра = Xerxes, PERsEPOLIS A: Trilingual, each version in 20 lines, in 4 copies designated aa, ab, ac, ad, differing only slightly in line di- vision, engraved on the inner walls of the great doorway; our text follows aa. Tm. Lex. 38-40 (1908); Wb. KIA xxiii, 106-9 (1911); Sen, OPI 138-40 (1941).
3544:Our text of DB is based essentially on KT's examina- fion and edition, supplemented by the examinations of the original by Jackson and Cameron. The notes inelude the additional characters and words recorded as visible by RI., and by WB from Wb.'s reading of Rs squeezes. In the text are embodied Cameron’s readings, 80 far as they are available through his kindness; Cameron re- moved the limestone incrustations that had covered many of the engraved characters, and succeeded in establishing the original text of a number of passages that had previously been in part unreadable and had been
3768:Notes to DB III: 99akaiam KT. "hamigiyóà KT. “naraidiy KT. “Margavaibis KT. “Agiyddiyahya KT. *wadaya RI., KT, Cameron; not yaudádà nor yutiyà with Foy, пог Ma*dayé with Hz. Ap] 244-9; but see Lex. s.v. *yada-. *frataram Cameron, confirmed by the Elamite ir- pi; this does away with the fratarta of КІ. and KT. “y KT. *&hata R1., КТ; во also in 51; cf. $36. IVe. "RI. lost a line here by haplography; corrected by KT. “agaubala is engraved ашта, KT. “рйи RIL, KT, Wb. KIA; perhaps to be read дите, with Justi ZDMG 51.240, HK, Tm., because of Elam. gan-du-ma-+, but see Wb. KIA 144, © abara is engraved ато, KT. ? mas[;5ta Ri.;
== BRT
```


## [2026-09-05T20:56:21.588Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; timeout 120 python3 tools/fetch_source.py \"https://www.etymonline.com/word/cart\" --note \"page 173, node 12: cart from ON kartr vs OE craet\"; sleep 1; timeout 120 python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/gra%CE%B8H-\" --note \"page 173, node 2: Proto-Iranian graθH\""
}
```


### [2026-09-05T20:56:25.444Z] TOOL RESULT

```
Exit code 1
/home/sfmqrb/git/rishe/data/verification/sources/web/7e367c5ffe187829.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/73ea4e8361760e6b.txt
```


## [2026-09-05T20:56:31.464Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -c \"grath\" KNT.txt; grep -n \"grath\" KNT.txt | head; echo \"== wikt PIr page\"; head -20 /home/sfmqrb/git/rishe/data/verification/sources/web/73ea4e8361760e6b.txt; echo; echo \"== etymonline cart\"; grep -n -m1 -A6 \"Origin and history of cart\" /home/sfmqrb/git/rishe/data/verification/sources/web/7e367c5ffe187829.txt"
}
```


### [2026-09-05T20:56:31.536Z] TOOL RESULT

```
0
== wikt PIr page
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/gra%CE%B8H-
FETCHED: 2026-09-05T20:56:25Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found
== etymonline cart
54: Origin and history of cart 
55-
56- cart (n.) 
57-
58- c. 1200, "two-wheeled vehicle," usually for one horse and often without springs, from Old Norse kartr or a similar Scandinavian source, akin to and replacing Old English cræt "cart, wagon, chariot," perhaps originally "body of a cart made of wickerwork, hamper" and related to Middle Dutch cratte "woven mat, hamper," Dutch krat "basket," Old English cradol (see cradle (n.)).
59-
60- Many old allusions are from the cart being used to convey offenders to the gallows (and sometimes serving as a drop for hangings) or for public exposure, especially of lewd women, either in the cart or tied to its tail. Compare tumbrel . To put the cart before the horse in a figurative sense "reverse the natural or proper order of things" is from 1510s in those words; the image in other words dates to mid-14c.: put the plow (sull) before the oxen .
```


## [2026-09-05T20:56:39.178Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; timeout 120 python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/gruppo\" --note \"page 173 node 6: Italian gruppo vs printed grappo\"; timeout 120 python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/grappo\" --note \"page 173 node 6: does Italian grappo exist\""
}
```


### [2026-09-05T20:56:41.792Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/80769e8c581fae19.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/eea1f80007727136.txt
```


## [2026-09-05T20:56:45.104Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; echo \"### gruppo\"; grep -n -m2 -A4 \"Etymology\" 80769e8c581fae19.txt | sed -n 1,30p; echo \"### grappo\"; grep -n -i -m3 -A5 \"Italian\\|Etymology\" eea1f80007727136.txt | head -40; wc -c eea1f80007727136.txt"
}
```


### [2026-09-05T20:56:45.193Z] TOOL RESULT

```
### gruppo
62: Etymology 
63-
64- 1.2 
65- Noun 
66-
--
81: Etymology 
82-
83- 3.2 
84- Pronunciation 
85-
### grappo
57: Italian 
58-
59: Toggle Italian subsection 
60-
61- 1.1 
62- Noun 
63-
64- 1.2 
--
74: Italiano 
75- Malagasy 
76-
77- Entry 
78-
79- Discussion 
2093 eea1f80007727136.txt
```


## [2026-09-05T20:56:48.043Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; sed -n '80,140p' eea1f80007727136.txt; echo \"#### gruppo etym\"; sed -n '95,160p' 80769e8c581fae19.txt"
}
```


### [2026-09-05T20:56:48.096Z] TOOL RESULT

```
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

 Italian
 [ edit ] 

 Noun
 [ edit ] 

 grappo   m ( plural grappi ) 

 bunch 
 Synonyms: grappolo , graspo 

 Anagrams
#### gruppo etym
 3.3.3 
 Descendants 

 3.4 
 Further reading 

 Toggle the table of contents 

 gruppo 

 24 languages 

 Català 
 Deutsch 
 Ελληνικά 
 Esperanto 
 Suomi 
 Français 
 Magyar 
 Հայերեն 
 Bahasa Indonesia 
 Ido 
 Italiano 
 日本語 
 한국어 
 Kurdî 
 Lombard 
 Malagasy 
 Монгол 
 Norsk bokmål 
 Polski 
 Русский 
 Sängö 
 Tagalog 
 Türkçe 
 中文 

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
```


## [2026-09-05T20:56:51.217Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; grep -n -i \"Italian\" -A25 80769e8c581fae19.txt | grep -n -i \"kruppaz\\|Germanic\\|Etymology\\|gruppo   m\\|group\" | head -20; echo ---; awk '/^ Italian$/{f=1} f' 80769e8c581fae19.txt | head -40"
}
```


### [2026-09-05T20:56:52.937Z] TOOL RESULT

```
6:81- Etymology 
57:190: Italian gruppo ( literally “ group ” ) .
64:197- ( cycling ) Synonym of groupset .
77:210- group 
86:219- Etymology
107:240- group , cluster , party , team , covey 
125:337: Italian terms derived from Proto-Germanic 
---
 Italian
 [ edit ] 

 Italian Wikipedia has an article on: gruppo 

 Wikipedia it 

 Etymology
 [ edit ] 

 From Vulgar Latin *cruppus , (cf. Renaissance Latin grupus ).

 Pronunciation
 [ edit ] 

 IPA ( key ) : /ˈɡrup.po/ 

 Audio : ( file ) 

 Rhymes: -uppo 

 Hyphenation: grùp‧po 

 Noun
 [ edit ] 

 gruppo   m ( plural gruppi ) 

 group , cluster , party , team , covey 

 ( sports ) pack 

 ( cycling ) peloton 

 ( music ) band 
 Synonyms: gruppo musicale , band 

 Coordinate terms
 [ edit ]
```


## [2026-09-05T20:57:02.106Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -o \"گروه[^ ]\\{0,4\\} \\?[[(][^]]\\{0,25\\}\" MON_part1.txt | head -8; echo \"== gereh\"; grep -n -o \"گره [^\\n]\\{0,60\\}\" MON_part1.txt | head -8"
}
```


## [2026-09-05T20:57:03.729Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; timeout 150 python3 tools/fetch_source.py \"https://abadis.ir/fatofa/گره/\" --note \"page 173 node 3: Mo'in entry for گره\" ; timeout 150 python3 tools/fetch_source.py \"https://abadis.ir/fatofa/گروه/\" --note \"page 173 node 5: Mo'in entry for گروه\""
}
```


### [2026-09-05T20:57:03.789Z] TOOL RESULT

```
48412:گروهی. (ا.) گر وه. مردم بسیار که 
92140:گروه (از 
== gereh
141:گره دورة برهان قاطع که به تصحیح و تحشیة ایشان رسیده از طرف 
6213:گره : بر ابرو افکندن و نظایر آن: ابرو 
6485:گره 
11119:گره قشون. 
17131:گره نی (نای). هر چیز مجوف مانند 
17203:گره یک قطعه را 
17547:گره و مانند آن). 
23486:گره
```


### [2026-09-05T20:57:10.443Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/bbb1b1eabacbfdce.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/951a94220d6afd77.txt
```


## [2026-09-05T20:57:13.128Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '92138,92145p' MON_part1.txt; echo ...; sed -n '6483,6492p' MON_part1.txt; echo \"== 23486\"; sed -n '23484,23492p' MON_part1.txt"
}
```


### [2026-09-05T20:57:13.216Z] TOOL RESULT

```
یک قرن از زمان یا یست سال. گروه (از 
مردم یباملخ). مهرةٌ پشت. لت» لنگه» 
طبق: بودام) [ع.] (حر. اض.) وفق» مطایق. بر 
طق: موافق» مطایق. ضسح.- لازم الاضافه 
است. 

...


اینه: (ع-)معده [ع. ابنه ] (ا.) گره» عقده» گره 
ای و 3 
آن. دژکک ساق» قوزکث آن. سر حلقوم شتر 
(.) دشمنی» عداوت» کینه. عیب» آهوه 
تباهی» وصمت. بماری ضد طبع. یک نوع 
خارش و بیماری که در مقعد بروز می‌کند و 
خود کشد تا با او آن کند که با زنان کنند. 

== 23486
(برهان قاطم). امید سته: امید محال. سته 
گهواره فنا: (کد.) اسیر محنت دنیا و گرفتار 
دنیا. در سته: در مقفل. کار سته: کارگره 
حورده. 


بسته‌بند ی: ]-0270-(02۵۱2)6 (حامص.) 
عمل بستن اشیا (مانند میوه و غیره) بصورت 
جعبه‌ها و قوطی‌ها و مانند 1
```


## [2026-09-05T20:57:16.731Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; for f in bbb1b1eabacbfdce 951a94220d6afd77; do echo \"##### $f\"; head -6 $f.txt; grep -n -i -m3 -A6 \"معین\" $f.txt | head -40; done"
}
```


### [2026-09-05T20:57:18.446Z] TOOL RESULT

```
##### bbb1b1eabacbfdce
URL: https://abadis.ir/fatofa/گره/
FETCHED: 2026-09-05T20:57:08Z
STATUS: 200
TITLE: گره - معنی در دیکشنری آبادیس

گره - معنی در دیکشنری آبادیس 
20: گره. [ گ ِ رِه ْ ] ( اِ ) پهلوی ، گره کردی ، گری ( گره ، عقد ازدواج ) ظاهراً از پارسی باستان ، گرثه . سانسکریت ، گرث ( بستن ). ( حاشیه برهان چ معین ). معروف است اعم از اینکه در ریسمان باشد یا درخت و امثال آن و از جایی برآمده باشد و به عربی عقده گویند. ( برهان ). بند و انگله باشد. ( صحاح الفرس ) : 
21-و چوب وی... نرم بود چنانکه بر او گره توان افکندن. ( حدود العالم ).
22-و دیگر که دارد همان او زره 
23-کجا گیو زد بر گریبان گره. فردوسی.
24-برزم اندرآید بپوشد زره 
25-یکی جوشن از بر ببندد گره. فردوسی.
26-بیاورد خفتان و خود و زره 
--
64: فرهنگ معین
65-
66- (گَ رَ ) [ معر. ] (اِ. ) ظرف آب ، سبو.
67- (گِ رِ ) (اِ. ) واحد طول قدیم مساوی ۱۱۶ ذرع .
68- (گِ رَ یا رِ ) [ په . ] (اِ. ) ۱ - پیچیدگی و درهم شدگی نخ و ریسمان یا چیز دیگر. ۲ - برآمدگی هایی از ساقه که برگ ها روی آن قرار دارند. ۳ - مشکل ، گرفتاری . ، ~بر ابرو زدن کنایه از: رو ترش کردن ، عبوس شدن . 
69-
70- فرهنگ عمید
--
253:• فرهنگ فارسی، محمد معین، انتشارات امیر کبیر، تهران، ۱۳۷۵
254-• غلط ننویسیم، ابوالحسن نجفی، مرکز نشر دانشگاهی، تهران، ۱۳۸۶
255-• فرهنگ کوچک زبان پهلوی، دیوید نیل مکنزی، ترجمه مهشید فخرایی، پژوهشگاه علوم انسانی و مطالعات فرهنگی، تهران، ۱۳۷۹
256-
257- منابع • https://fa.m.wikipedia.org/wiki/زبان_فارسی_باستان 
258- عقده
259-
##### 951a94220d6afd77
URL: https://abadis.ir/fatofa/گروه/
FETCHED: 2026-09-05T20:57:10Z
STATUS: 200
TITLE: گروه - معنی در دیکشنری آبادیس

گروه - معنی در دیکشنری آبادیس 
23: گروه. [ گ ُ ] ( اِ ) پهلوی ، گره ( دسته ، گروه ). ارمنی ، گره ( ملت ، جمعیت ). بلوچی ، گرف . ایرانی باستان ، ظاهراً گروثوه . کردی ، کوروه ( اجتماع اشخاص ). ( حاشیه برهان چ معین ).جماعت مردم را گویند و به عربی قوم خوانند. ( غیاث ) ( برهان ). جماعة از مردم و غیره از سایر حیوانات. ( آنندراج ). جماعت مردم و غیر آن. ( انجمن آرا ). طائفه. جمعیت. دسته. امت. ثله. رهط. زمره. حزب. فرقه. فریق. فئه. عصبه. فوج. قبیله : و مغرب وی گروهی از خرخیزیانند. ( حدود العالم ). و کوفیانند و ایشان هفت گروهند و هر گروهی را مهتری است. ( حدود العالم ).
24-ای خواجه چرا جداشده ستی ز گروه 
25-چونانکه ز جمع تره ها خود خروه. ابوعلی صاحبی.
26-یکی غار بود اندر آن برزکوه 
27-بدو سخت نزدیک و دور از گروه. فردوسی.
28-همانگاه سیمرغ برشد به کوه 
29-بمانده برو چشم سام و گروه. فردوسی.
--
50: فرهنگ معین
51-
52- (گُ ) [ په . ] (اِ. ) ۱ - دسته ، جمعیت . ۲ - امت ، فرقه . ۳ - واحدی از سربازان شامل ۹ نفر. ۴ - امتیاز کارمند از جهت مدرک تحصیلی و سابقة کار که خود به چند پایه تقسیم می شود. ۵ - اصطلاحی است که در دانشگاه ها به جای کلمة انگلیسی دپارتمان یعنی جزوی از دانشگاه 
53-
54- فرهنگ عمید
55-
56- ۱. جماعت.
--
236:منبع فرهنگ فارسی معین
237-واژگان مترادف و متضاد
238-
239- خیل
240-
241- خوش آن گروه که مست بیان یکدیگرند 
242-ز جوش فکر می ارغوان یکدیگرند
```


## [2026-09-05T20:57:46.358Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad; python3 -c \"\nfrom PIL import Image\nim=Image.open('p600_350.png'); w,h=im.size\nim.crop((0,0,w,140)).save('p600_top.png')\n\"; for p in 598 599 600 601; do pdftoppm -f $p -l $p -r 350 -png -singlefile /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf t$p; python3 -c \"\nfrom PIL import Image;im=Image.open('t$p.png');w,h=im.size;im.crop((0,0,w,150)).save('top$p.png')\"; done; python3 -c \"\nfrom PIL import Image\nims=[Image.open('top%d.png'%p) for p in (598,599,600,601)]\nw=max(i.width for i in ims); H=sum(i.height for i in ims)\nout=Image.new('RGB',(w,H),'white'); y=0\nfor i in ims: out.paste(i,(0,y)); y+=i.height\nout.save('tops.png')\""
}
```


### [2026-09-05T20:57:54.705Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T20:57:57.100Z] TOOL CALL #77: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/tops.png"
}
```


### [2026-09-05T20:57:57.116Z] TOOL RESULT

```

```


## [2026-09-05T20:58:04.547Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad; python3 -c \"\nfrom PIL import Image\nims=[]\nfor p in (598,599,600,601):\n    im=Image.open('t%d.png'%p); w,h=im.size\n    ims.append(im.crop((0,120,w,330)))\nw=max(i.width for i in ims); H=sum(i.height for i in ims)\nout=Image.new('RGB',(w,H),'white'); y=0\nfor i in ims: out.paste(i,(0,y)); y+=i.height\nout.save('tops2.png')\""
}
```


### [2026-09-05T20:58:06.768Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T20:58:09.109Z] TOOL CALL #79: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/tops2.png"
}
```


### [2026-09-05T20:58:09.132Z] TOOL RESULT

```

```


## [2026-09-05T20:58:16.580Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n 1,120p tools/verify_check.py"
}
```


### [2026-09-05T20:58:16.618Z] TOOL RESULT

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


## [2026-09-05T20:59:19.709Z] TOOL CALL #81: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; mkdir -p data/verification/sources/refs/ocr/BOOK data/verification/sources/refs/ocr/BQT\ncp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg173.png data/verification/sources/refs/ocr/BOOK/173.png\ncp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p600_350.png data/verification/sources/refs/ocr/BQT/1803.png\ncat > data/verification/sources/refs/ocr/BQT/1803.vision.txt <<'EOF'\n[Borhan-e Qate', ed. Mo'in, printed page 1803 = PDF page 600 of BQT_v3_picofile.pdf\n (NOT pdf 598: the running heads read 1801 = pdf 598, 1802 = pdf 599, 1803 = pdf 600,\n 1804 = pdf 601, i.e. printed = pdf + 1203 in this region; the earlier cached 1803.txt\n was the OCR of pdf 598 = printed 1801. Running head of this page: «گره».)\n Transcribed from the page image by a vision model, 2026-09-05.]\n\nHeadwords on the page (col. 1 -> col. 2):\n  گروه ۴ - بضم اول و ثانی بر وزن شکوه ، جماعت مردم را گویند و بعربی قوم خوانند .\n  گروهه ۵ - ... بروزن و معنی کلوله است مطلقاً ...\n  گروی ۸ - ... نام یکی از خویشان افراسیاب ...\n  گرویدن ۹ - ... بمعنی ایمان آوردن و سر باطاعت نهادن و پذیرفتن ...\n  گره ۱۰ - بکسر اول و ثانی و ظهور ها ، معروفست اعم ازینکه در ریسمان یا در درخت و امثال\n        آن ... و بعربی عقده گویند ... و بمعنی مشکل هم بنظر آمده است ...\n\nMo'in's etymological footnotes (bottom of the page), verbatim:\n\n  ۴ - پهلوی grôh ( دسته ، گروه ) ، ارمنی ع groh ( ملت ، جمعیت )، بلوچی grôf ،\n      ایرانی باستان - *gravathva « نیبرگ ص ۸۴ »، کردی kuruh (اجتماع اشخاص)\n      « ژابا ص ۳۳۱ » .\n\n  ۵ - قس : کلوله ، غلوله . مخفف آن «گروهه» .\n\n  ۸ - Guröy ( = Guröi Zirih ) رك : فهرست ولف .\n\n  ۹ - virravistan ( از virrav_ ) (باور کردن ، گمان کردن)، پازند varöistan\n      از اوستا - var ، « بارتولمه ۱۳۶۰ » ، « نیبرگ ص ۲۴۴ » و رك : اشتق - هوبشمان ۹۱۲ .\n\n  ۱۰ - پهلوی grah « تاوادیا ص ۱۶۱ : ۲ »، کردی ghiri (گره ، عقد ازدواج) « ژابا\n      ص ۳۶۱ » ، از پارسی باستان - *gratha ، سانسکریت grath ( بستن ) « هوبشمان ص۹۳ » .\n\n[Both footnotes are the pages Nourai cites as BQT:1803 for his Old Persian box\n (gratha, gravatha), for Persian گره and, through MON, for گروه.]\nEOF\nls -la data/verification/sources/refs/ocr/BQT/1803* data/verification/sources/refs/ocr/BOOK/173.png"
}
```


### [2026-09-05T20:59:19.810Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb  52970 Sep  5 16:59 data/verification/sources/refs/ocr/BOOK/173.png
-rw-rw-r-- 1 sfmqrb sfmqrb 671488 Sep  5 16:59 data/verification/sources/refs/ocr/BQT/1803.png
-rw-rw-r-- 1 sfmqrb sfmqrb   3681 Sep  4 14:06 data/verification/sources/refs/ocr/BQT/1803.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   2218 Sep  5 16:59 data/verification/sources/refs/ocr/BQT/1803.vision.txt
```


## [2026-09-05T21:08:27.086Z] TOOL CALL #82: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build173.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW = \"https://en.wiktionary.org/wiki/\"\n\nentry = {\n  \"entry\": 0,\n  \"root\": \"Ger 1\",\n  \"verdict\": \"confirmed\",\n  \"modern_form\": \"PIE *ger- 'to turn, wind; curving, crooked' (Pokorny 3. ger- 385-390; Watkins/AHD ger-² 'curving, crooked')\",\n  \"note\": \"The root box is right on all three counts. Pokorny's lemma reads 'Root / lemma: ger-3 / Meaning: to turn, wind' with 'Page(s): 385-390', so Nourai's POK:385 is the first page of exactly that article; Watkins's appendix has 'ger-2. Curving, crooked; hypothetical Indo-European base for a variety of Germanic words with initial kr- ... [Pok. 3. ger- 385.]' and organises the material in two halves, 'I. Words meaning to bend, curl; bent, crooked, hooked' and 'II. Words meaning a rounded mass, collection; a round object, vessel, container' — which is where Nourai's three-part gloss 'crooked, curved, round object' comes from. ('Ger 1' is Nourai's own numbering, not Pokorny's; Pokorny's ger-1 is 'to gather', ger-2 'to cry hoarsely', ger-4 'to grow up'.) Every Germanic/Romance box of the chart is one of Watkins's numbered items, and the Indo-Iranian branch is Pokorny's own dental extension. Three things need correcting, all of them in the printed book rather than in the extraction (the JSON reproduces page 143 faithfully — checked against the page image, saved as data/verification/sources/refs/ocr/BOOK/173.png). (1) Node #6 'Italian grappo : assemblage' should be gruppo: Watkins reads 'Italian gruppo, an assemblage: GROUP', and Klein, Webster and Buck all give gruppo; Italian grappo exists but means 'bunch (of grapes)'. (2) Node #9 'Germanic grâppon' should be *krāppōn-: Watkins prints '*krāppōn-, a hook, especially one used in harvesting grapes', and a Germanic form of this root must begin with k- by Grimm's law. (3) Node #2's second word, 'gravatha', is Mo'in's Old Iranian *gravath va — the footnote on the very page Nourai cites (Borhān p.1803, note 4) reads 'ایرانی باستان *gravathva «نیبرگ ص ۸۴»', and it is labelled Old Iranian there, not Old Persian. Nourai's Iranian material is otherwise exactly Mo'in's: note 10 of the same page gives 'از پارسی باستان *gratha ، سانسکریت grath (بستن) «هوبشمان ص۹۳»'.\",\n  \"note_fa\": \"خود ریشه درست است: پوکورنی در صفحات ۳۸۵–۳۹۰ مادهٔ ger-3 را با معنای «پیچیدن، تابیدن» آورده و واتکینز در پیوست فرهنگ American Heritage همان را ger-2 «curving, crooked» می‌نامد و مادهٔ خود را به دو بخش «خمیده/قلاب‌مانند» و «تودهٔ گرد، ظرف» بخش می‌کند؛ پس معنای سه‌جزئی نورایی عیناً از همین جاست. شمارهٔ «Ger 1» از آنِ خود نورایی است نه پوکورنی. سه لغزش در نمودار هست و هر سه از خودِ کتاب است نه از خوانش اسکن: ۱) ایتالیایی grappo باید gruppo باشد؛ ۲) صورت ژرمنی grâppon باید *krāppōn- باشد، زیرا g هندواروپایی بر پایهٔ قانون گریم در ژرمنی به k بدل می‌شود؛ ۳) صورت gravatha در حاشیهٔ معین (برهان قاطع ص ۱۸۰۳ حاشیهٔ ۴) *gravathva است و «ایرانی باستان» خوانده شده، نه پارسی باستان. در کل، ادعای نورایی دربارهٔ خود ریشه درست است.\",\n  \"sources\": [\n    \"https://en.wiktionary.org/wiki/%DA%AF%D8%B1%D9%87\",\n    \"https://en.wiktionary.org/wiki/%DA%AF%D8%B1%D9%88%D9%87\"\n  ],\n  \"ref_check\": [\n    {\"ref\": \"POK:385\", \"status\": \"supports\",\n     \"note\": \"POK_full.txt line 31336ff: 'Root / lemma: ger-3 / Meaning: to turn, wind' ... 'References: WP. I 593 ff., WH. 623, Trautmann 94 f., 97, 99 f. / Page(s): 385-390'. Page 385 is the first page of the article, so Nourai's POK:385 points at the right lemma; the gloss he gives ('crooked, curved, round object') is Watkins's rendering of it rather than Pokorny's German 'drehen, winden'.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"pp.385-390, ger-3\", \"stance\": \"supports\",\n     \"note\": \"the article supplies almost every box of the chart: 'Old Indic granth-, grathnami ... granthi-h m. ‚knot, joint, intumescence‘, grantha-h ‚knot‘' (dental extension, p.386); 'Old Norse kartr, Old English craet m. ‚cart‘'; 'Old English cribb ‚crib, manger‘'; 'ags. cradol m. ‚Wiege‘'; 'Old English cryppel cripple', 'Old English creopan to creep'; 'Old English crycc, nengl. crutch'; 'Middle High German krol(le), krulle ‚curl‘' (p.389).\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. ger-²\", \"stance\": \"supports\",\n     \"note\": \"'ger-2. Curving, crooked; hypothetical Indo-European base for a variety of Germanic words with initial kr-. I. Words meaning to bend, curl; bent, crooked, hooked ... II. Words meaning “a rounded mass, collection; a round object, vessel, container.” ... [Pok. 3. ger- 385.]' (AHD_watkins1985.txt line 492ff).\"},\n    {\"src\": \"WLD\", \"where\": \"Bd. I 593-595\", \"stance\": \"supports\",\n     \"note\": \"the parent article of Pokorny's; the dental-extension paragraph reads 'idg. *gr-et(h)-, nasaliert *grenth-: ags. cradol m. ‚Wiege“ (*kradula- ‚geflochtenes“), ahd. kratto ‚Korb“ ... ai. granth-, grathnami, fut. granthisyami ‚winden, knüpfen, einen Knoten binden“' (WLD_Bd1_1930_dli_70244_djvu.txt lines 37410-37421).\"},\n    {\"src\": \"SYN\", \"where\": \"Buck 9.192 note 7 and 13.192\", \"stance\": \"supports\",\n     \"note\": \"'Skt. granthi- : grath- ‚tie‘, this perh. : OE cradel ‚cradle‘, OHG kratto ‚basket‘, fr. an extension of *ger- in words based on the notion of ‚twist, wind‘. Walde-P. 1.593 ff. (595)' — the same root and the same hedge ('perh.'); and 13.192 'NE group (fr. Fr. groupe, fr. Ital. gruppo : groppo ‚knot‘)'.\"},\n    {\"src\": \"IEC\", \"where\": \"Mann col. s.v. grondhos\", \"stance\": \"partial\",\n     \"note\": \"Mann sets up an independent IE noun 'grondhos, á (gronth-) ‚mass, tuft, bunch‘ Skt. cf. granthah, ih ‚knot‘; Gk. grónthos ‚balled fist, punch‘; Cor. gron ‚mass, bunch‘' rather than deriving it from *ger-, i.e. he keeps the Indic word but not Pokorny's derivation of it.\"}\n  ],\n  \"nodes\": []\n}\n\nN = entry[\"nodes\"]\n\nN.append({\n  \"id\": 1, \"lang\": \"Sanskrit\", \"words\": \"grath, granth\", \"verdict\": \"plausible\",\n  \"derivation\": \"The Sanskrit material is real: the verbal root granth-/grath- 'to tie (a knot), string together' (present grathnāti, future granthiṣyati), participle grathita- 'knotted', with the nouns granthi- m. 'knot, joint, swelling' and grantha- 'knot' (later 'composition, book' — a text being 'tied together'). Pokorny puts exactly these forms under ger-3 as its nasalised dental extension: '2. Dental extensions: a. gr-et(h)-... b. Nasalized: Old Indic granth-, grathnāmi ... granthi-h m. ‚knot, joint‘, grantha-h ‚knot‘', beside Old English cradol and Old High German kratto ‚basket‘ — material printed on p.386, the page Nourai cites. So the arrow root→Sanskrit is Pokorny's own, and Walde-Pokorny I 595 and Buck 9.192 say the same. It is only 'plausible' because the newest specialist treatments hedge: Cheung (2007: 123, s.v. *graθH) writes 'A convincing IE etymology for this (Ir.) root is wanting. The Germanic nominal forms, ? OHG kratto ‚basket‘, OE cradol, Engl. cradle, NHG Kranz ... often cited as cognates are unattractive: are they rather loanwords from a \\\"substrate\\\" source?', and Wiktionary calls the derivation from *gre(n)tH- < *ger- 'traditional' but 'not certain'. Nourai's gloss 'knot' belongs strictly to the noun grantha-/granthi-, not to the verbal root.\",\n  \"derivation_fa\": \"ریشهٔ سنسکریت granth-/grath- «گره زدن، بستن» (حال grathnāti) و اسم‌های granthi- «گره، بند» و grantha- «گره» به‌راستی موجودند و پوکورنی در همان صفحهٔ ۳۸۶ که نورایی یاد کرده، آن‌ها را زیر ریشهٔ ger-3 و به صورت گسترش‌یافتهٔ دندانی با خیشومی‌شدگی (*gre-n-th-) آورده است؛ والده–پوکورنی (ج۱ ص ۵۹۵) و باک نیز همین را می‌گویند. اما چونگ (۲۰۰۷، ص ۱۲۳) تصریح می‌کند که ریشهٔ هندواروپایی قانع‌کننده‌ای برای این ریشه در دست نیست و همریشه‌های ژرمنی شاید وام‌واژهٔ زیرلایه باشند؛ از این‌رو ادعای نورایی با احتیاط پذیرفتنی است.\",\n  \"sources\": [\"https://en.wiktionary.org/wiki/%DA%AF%D8%B1%D9%87\"],\n  \"ref_check\": [\n    {\"ref\": \"POK:386\", \"status\": \"supports\",\n     \"note\": \"POK_full.txt, ger-3 (pp.385-390), the dental-extension paragraph that falls on p.386: 'b. Nasalized: Old Indic granth-, grathnami, Fut. granthisyami ‚coil, bind, wind, tie, knot, fasten‘, participle grathita- ‚winded, knotty‘, granthi-h m. ‚knot, joint, intumescence‘, grantha-h ‚knot‘'.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"WLD\", \"where\": \"Bd. I 595\", \"stance\": \"supports\",\n     \"note\": \"'ai. granth-, grathnami, fut. granthisyami ‚winden, knüpfen, einen Knoten binden“ ... granthi-h m. ‚Knoten, Gelenk, Anschwellung“, grantha-h ‚Knoten“' — and a warning that Gk. gronthos 'Faust', which looks identical, belongs elsewhere ('zu *ger-, *grem ‚fassen“').\"},\n    {\"src\": \"CHEUNG\", \"where\": \"p.123 s.v. *graθH\", \"stance\": \"partial\",\n     \"note\": \"keeps Skt. granth 'to tie a knot' as the Indic cognate ('*SANSKRIT: granth ‚to tie a knot” = EWAia I: 504') but rejects the IE anchoring: 'A convincing IE etymology for this (Ir.) root is wanting ... OHG kratto ‚basket”, OE cradol ... are unattractive: are they rather loanwords from a \\\"substrate\\\" source?'\"},\n    {\"src\": \"SYN\", \"where\": \"Buck 9.192 note 7\", \"stance\": \"supports\",\n     \"note\": \"'Skt. granthi- : grath- ‚tie‘, this perh. : OE cradel ‚cradle‘, OHG kratto ‚basket‘, fr. an extension of *ger- in words based on the notion of ‚twist, wind‘.'\"},\n    {\"src\": \"IEC\", \"where\": \"Mann s.v. grondhos\", \"stance\": \"partial\",\n     \"note\": \"'grondhos, á (gronth-) ‚mass, tuft, bunch‘ Skt. cf. granthah, ih ‚knot‘' — an IE etymon is set up, but as an independent noun, not as an extension of *ger-.\"}\n  ]\n})\n\nN.append({\n  \"id\": 2, \"lang\": \"Old Persian\", \"words\": \"gratha; gravatha\", \"verdict\": \"transcription_suspect\",\n  \"derivation\": \"Neither word is attested in the Old Persian corpus: Kent's lexicon (KNT.txt) has no gratha and no gravatha, and Bartholomae has no Avestan match either — both are starred reconstructions, and Nourai prints them without the asterisk. (i) *graθa- 'knot' is Hübschmann's: Persische Studien p.93 'Hierher nach Fr. Müller, WZKM. 8, 189 np. girih ‚Knoten“ = ap. *graθa- zu skr. grath ‚verknüpfen“', repeated on p.204 in the chapter on OP θ > NP h ('girih ‚Knoten“ = ap. *graθa- (oben p. 93)'); Mo'in copied it into the Borhān footnote Nourai cites. Modern reconstruction is the same shape but Proto-Iranian rather than Old Persian: Cheung 2007 p.123 *graθH 'to tie (a knot)', Wiktionary Proto-Iranian *graθH- < Proto-Indo-Iranian *grantH-, the -n- of Skt. granth- being the nasal infix that Iranian lost. (ii) 'gravatha' is a misprint. Mo'in's note 4 on Borhān p.1803 reads 'ایرانی باستان *gravathva «نیبرگ ص ۸۴»' — *gravath-va, with a final -va that Nourai's form drops (Dehkhoda quotes the same footnote as 'ایرانی باستان، ظاهراً گروثوه'). Mo'in also calls it Old Iranian, not Old Persian, and prefixes it with 'ظاهراً' ('apparently'), so it is a guess even in the source. The book page (image at data/verification/sources/refs/ocr/BOOK/173.png) does print 'gravatha', so the extraction is faithful. Finally, the two words do not belong in one box: *graθa- is the etymon of گره and *gravathva that of گروه, and no source derives the second from the first.\",\n  \"derivation_fa\": \"هیچ‌یک از این دو صورت در کتیبه‌های پارسی باستان گواهی نشده است (در واژه‌نامهٔ کنت نیست) و هر دو بازساخته‌اند؛ نورایی ستارهٔ بازساخت را نیاورده است. صورت *graθa- «گره» از هوبشمان (مطالعات فارسی، ص ۹۳) است که معین در حاشیهٔ برهان قاطع نقل کرده؛ بازساخت امروزین همین صورت است ولی به‌نام «ایرانی آغازین»: چونگ *graθH «گره زدن». اما gravatha خطای چاپی کتاب است: حاشیهٔ ۴ برهان قاطع ص ۱۸۰۳ می‌نویسد «ایرانی باستان *gravathva (نیبرگ ص ۸۴)»، یعنی با پایانهٔ -va که در کتاب افتاده است؛ افزون بر آن معین آن را «ایرانی باستان» و با قید «ظاهراً» آورده، نه پارسی باستان. تصویر صفحهٔ ۱۴۳ کتاب نشان می‌دهد که خوانش اسکن درست است و خطا از خودِ کتاب است.\",\n  \"error_in\": \"book\",\n  \"book_prints\": \"gratha : knot, tie / gravatha : assemblage, group\",\n  \"correct_form\": \"Old Iranian *graθa- (Proto-Iranian *graθH-) 'knot'; Old Iranian *gravathva 'group' (Mo'in, after Nyberg p.84)\",\n  \"sources\": [\n    \"https://en.wiktionary.org/wiki/%DA%AF%D8%B1%D9%87\",\n    \"https://abadis.ir/fatofa/%DA%AF%D8%B1%D9%88%D9%87/\"\n  ],\n  \"ref_check\": [\n    {\"ref\": \"BQT:1803\", \"status\": \"partial\",\n     \"note\": \"The page is right (running head «گره»; printed 1803 = pdf page 600 of BQT_v3_picofile.pdf, NOT pdf 598 as the offset table suggests — the running heads read 1801/1802/1803/1804 on pdf 598/599/600/601; transcription saved to data/verification/sources/refs/ocr/BQT/1803.vision.txt). Footnote 10 supports the first word exactly: 'پهلوی grah «تاوادیا ص ۱۶۱» ... از پارسی باستان *gratha ، سانسکریت grath (بستن) «هوبشمان ص۹۳»'. Footnote 4 differs from Nourai on the second: 'پهلوی grôh (دسته، گروه) ... ایرانی باستان *gravathva «نیبرگ ص ۸۴»' — *gravathva, and Old Iranian, not Old Persian.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"HUB\", \"where\": \"Persische Studien pp.93 and 204\", \"stance\": \"supports\",\n     \"note\": \"p.93: 'Hierher nach Fr. Müller, WZKM. 8, 189 np. girih ‚Knoten“ = ap. *graθa- zu skr. grath ‚verknüpfen“' (HUB.txt line 3298); p.204, in the list of OP θ that give NP h: 'girih ‚Knoten“ = ap. *graθa- (oben p. 93)' (line 7233). This is the actual origin of Nourai's box.\"},\n    {\"src\": \"KNT\", \"where\": \"Old Persian lexicon\", \"stance\": \"silent\",\n     \"note\": \"grep of KNT.txt for 'grath' returns 0 hits: neither gratha nor gravatha is attested in the Achaemenid inscriptions, so 'Old Persian' can only mean 'reconstructed Old Iranian'.\"},\n    {\"src\": \"CHEUNG\", \"where\": \"p.123 s.v. *graθH\", \"stance\": \"partial\",\n     \"note\": \"gives the same consonant skeleton but as a Proto-Iranian verbal root: '*graθH ‚to tie (a knot)” — MIDDLE PERSIAN: BMP glyh /grih/ ‚knot”; PARTHIAN: gryh ‚knot”; KHOTANESE: OKh. grantha-, LKh. gratha- ‚knot”; SOGDIAN: BSogd. γrʾans ‚knot, bond”; NP girih'. No *gravathva anywhere.\"},\n    {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch\", \"stance\": \"silent\",\n     \"note\": \"no Avestan granθ-/graθa- entry found (grep for 'grantha', 'granθ' returns nothing), i.e. the Old Iranian form has no Avestan witness.\"}\n  ]\n})\n\nN.append({\n  \"id\": 3, \"lang\": \"Persian\", \"words\": \"gereh\", \"verdict\": \"confirmed\",\n  \"derivation\": \"گره gereh (classical girih) 'knot' goes back to Middle Persian grih, written glyh in Book Pahlavi: MacKenzie's dictionary has 'grih [glyh | N girih] knot' and Nyberg's glossary the by-form 'grah [glwh]'. The Old Iranian antecedent is *graθa-/*graθH- (Hübschmann p.93; Cheung 2007: 123), with the regular western Iranian development θ > h between the Old and Middle periods — Hübschmann treats girih on p.204 as one of his standard examples of that change (beside rāh < *raθa-, šāh < xšāyaθiya-, چاه < *čāθ-). The a of *graθa- is raised and an anaptyctic vowel breaks the initial cluster gr- > gi-/ge-, giving MP grih [gi'rih] > NP girih, modern Tehran gereh; cognates are Parthian gryh, Sogdian γrʾans, Khotanese grantha-, Kurdish girê, Balochi garanc. Nourai's Persian script and gloss are both right.\",\n  \"derivation_fa\": \"«گره» از فارسی میانهٔ grih (به خط پهلوی glyh) است؛ مکنزی می‌آورد: 'grih [glyh | N girih] knot'. صورت ایرانی باستان آن *graθa- (چونگ: *graθH) است و تبدیل ث ایرانی باستان به هٔ فارسی همان دگرگونی آوایی است که در راه (*raθa-)، شاه (xšāyaθiya-) و چاه دیده می‌شود — هوبشمان در ص ۲۰۴ همین واژه را نمونهٔ این قاعده آورده است. خوشهٔ آغازین gr- با مصوت میانجی شکسته و girih > گِرِه شده است. همریشه‌ها: پارتی gryh، سغدی γrʾans، کردی girê. ادعای نورایی درست است.\",\n  \"sources\": [\n    \"https://en.wiktionary.org/wiki/%DA%AF%D8%B1%D9%87\",\n    \"https://abadis.ir/fatofa/%DA%AF%D8%B1%D9%87/\"\n  ],\n  \"ref_check\": [\n    {\"ref\": \"BQT:1803\", \"status\": \"supports\",\n     \"note\": \"Borhān p.1803 (pdf 600), headword 'گره ... معروفست اعم ازینکه در ریسمان یا درخت و امثال آن ... و بعربی عقده گویند' with Mo'in's note 10 'پهلوی grah ... از پارسی باستان *gratha ، سانسکریت grath (بستن) «هوبشمان ص۹۳»'.\"},\n    {\"ref\": \"MON:3280\", \"status\": \"partial\",\n     \"note\": \"The six-volume Farhang-e Farsi is not online, so the page number could not be checked; the entry itself is on vajehyab/abadis and reads 'گره (گِ رَ یا رِ) [په .] (اِ.) ۱ - پیچیدگی و درهم شدگی نخ و ریسمان ...' — the tag [په.] = Pahlavi is Mo'in's own statement of the origin Nourai draws.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"PHD\", \"where\": \"MacKenzie p.37 s.v. grih\", \"stance\": \"supports\",\n     \"note\": \"'grih [glyh | N girih] knot' (PHD_mackenzie.txt line 2579) — the Middle Persian link that the chart leaves out between the Old Iranian etymon and New Persian.\"},\n    {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II, glossary\", \"stance\": \"partial\",\n     \"note\": \"Nyberg reads the same Book-Pahlavi spelling as 'grah [glwh] troop, company ... NP guroh' for the group-word; for the knot-word his transliteration convention differs, but Mo'in's footnote 10 cites Tavadia p.161 for Pahlavi grah 'knot'.\"},\n    {\"src\": \"HRN\", \"where\": \"Grundriss no. 164\", \"stance\": \"partial\",\n     \"note\": \"Horn has no independent article on girih; he only mentions it as the gloss of an Avestan word: 'piyak ‚Knoten“ in aʹpiŷak (vd. 9 (41)). aw. piŷa- ‚Knoten“ ... Vielleicht nur umschreibend (glossirt durch g(i)ris, np. girih)' (HRN.txt line 10915) — confirms the word and its meaning, not the etymology.\"},\n    {\"src\": \"CHEUNG\", \"where\": \"p.123 s.v. *graθH\", \"stance\": \"supports\",\n     \"note\": \"lists 'NP girih' among the New West Iranian continuants of *graθH beside 'BMP glyh /grih/', i.e. the same chain Nourai draws.\"}\n  ]\n})\n\nN.append({\n  \"id\": 4, \"lang\": \"Pahlavi\", \"words\": \"groh\", \"verdict\": \"plausible\",\n  \"derivation\": \"Middle Persian grōh 'group, crowd' is solid: MacKenzie 'grōh [glwh | N gurōh] group, crowd', Nyberg's glossary 'grah [glwh] troop, company, with the indef. art. ~-ē ... NP guroh'. What is only 'plausible' is the arrow: Nourai takes grōh out of the same Old Persian box as *graθa- 'knot', but no source derives the group-word from the knot-word. Mo'in, whose footnote is Nourai's ultimate source, gives them separate etymologies on the same page — note 10 'از پارسی باستان *gratha' for گره, note 4 'ایرانی باستان *gravathva «نیبرگ ص ۸۴»' for گروه — and hedges the second with 'ظاهراً'. Cheung's *graθH entry lists no grōh. The semantic step 'tie, bind' → 'band, troop' is of course natural (compare It. gruppo 'knot' → 'group' in the other half of this very chart, and English band), and Wiktionary states it — 'Inherited from Middle Persian glwhʾ /grōh/, possibly from Proto-Indo-European *ger- ‚to twist, wind (into a mass)” and cognate with گره' — but its footnote for that claim is Nourai's own book (Ger 1, p.143), so it is not independent evidence.\",\n  \"derivation_fa\": \"فارسی میانهٔ grōh «دسته، گروه» قطعی است: مکنزی 'grōh [glwh | N gurōh] group, crowd' و نیبرگ 'grah [glwh] troop, company ... NP guroh'. اما پیکانی که نورایی از خانهٔ *gratha «گره» به این خانه می‌کشد پشتیبانی مستقیم ندارد: معین در همان صفحه دو ریشهٔ جداگانه می‌آورد و برای گروه می‌نویسد «ایرانی باستان، ظاهراً *gravathva». تحول معنایی «بستن/گره» به «دسته، جمعیت» طبیعی است (همان‌گونه که gruppo ایتالیایی از «گره» به «group» رسیده) و ویکی‌واژه نیز همین را می‌گوید، اما مأخذِ ویکی‌واژه در همین ماده خودِ کتاب نورایی (ص ۱۴۳) است و استدلال دوری پدید می‌آورد. پس: با احتیاط پذیرفتنی است.\",\n  \"sources\": [\"https://en.wiktionary.org/wiki/%DA%AF%D8%B1%D9%88%D9%87\"],\n  \"ref_check\": [\n    {\"ref\": \"VFO:25\", \"status\": \"not_checked\",\n     \"note\": \"VFO = M. Ahmad Soltani, Vāžgān-e Fārsi dar Zabānhā-ye Orupā'i (Tehran 1372/1993). refs_online.json has no record for VFO (value null); no copy exists in the local library and none was found online, so the reference is unverifiable — as on pages 44 and 77, where the same abbreviation appears.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"PHD\", \"where\": \"MacKenzie p.37 s.v. grōh\", \"stance\": \"supports\",\n     \"note\": \"'grōh [glwh | N guroh] group, crowd' (PHD_mackenzie.txt line 2588); the English-Pahlavi index adds 'group dastag, grōh, gund'.\"},\n    {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II, glossary s.v. grah\", \"stance\": \"supports\",\n     \"note\": \"'grah [glwh] troop, company, with the indef. art. ~-ē [~+1] 84. - = Paz.; NP guroh' (NYB_vol2_glossary.txt line 1719) — the word, its Book-Pahlavi spelling and the New Persian outcome, but no Old Iranian etymon.\"},\n    {\"src\": \"BQT\", \"where\": \"p.1803 note 4 (Mo'in)\", \"stance\": \"partial\",\n     \"note\": \"'پهلوی grôh (دسته، گروه)، ارمنی groh (ملت، جمعیت)، بلوچی grôf، ایرانی باستان *gravathva «نیبرگ ص ۸۴»، کردی kuruh' — supports the Pahlavi form and an Old Iranian etymon, but a different one from the knot-word.\"},\n    {\"src\": \"CHEUNG\", \"where\": \"p.123 s.v. *graθH\", \"stance\": \"silent\",\n     \"note\": \"the Proto-Iranian knot-root article lists MP grih, Parthian gryh, Sogdian γrʾans and NP girih but no grōh/guroh, i.e. Cheung does not connect the group-word with it.\"}\n  ]\n})\n\nN.append({\n  \"id\": 5, \"lang\": \"Persian\", \"words\": \"gorŭh\", \"verdict\": \"confirmed\",\n  \"derivation\": \"گروه, classical gurōh, modern Iranian goruh 'group, company', is the straightforward continuation of Middle Persian grōh [glwh]: the Pahlavi initial cluster gr- takes the usual anaptyctic u (grōh > gurōh), and Middle Persian long ō survives as ō in Dari and Tajik (gurōh, گوروه/гурӣҳ) but is raised to ū in Iranian Persian (goruh), the same ō > ū raising as in شیر / خون or MP rōz > Ir. Pers. ruz. Mo'in tags the word [په.] 'Pahlavi', Borhān's own note 4 gives 'پهلوی grôh', and it is attested from the earliest New Persian (Ferdowsi, and Rūmi's 'ما نه زان پیلان گولیم ای گروه'), with the loan-descendants Chagatai/Uzbek guruh. Nourai's transliteration 'gorŭh' with the breve is his notation for that raised vowel; script and gloss are right.\",\n  \"derivation_fa\": \"«گروه» دنبالهٔ مستقیم فارسی میانهٔ grōh است: خوشهٔ آغازین gr- با مصوت میانجی u شکسته و gurōh شده، و واو مجهول (ō) که در دری و تاجیکی مانده، در فارسی ایران به واو معروف (ū) بدل شده است — همان دگرگونی که rōz > روز دارد. معین آن را با نشانهٔ [په.] یعنی پهلوی می‌آورد و حاشیهٔ برهان قاطع نیز «پهلوی grôh». واژه از کهن‌ترین متون فارسی (فردوسی، مولوی) گواهی دارد. ادعای نورایی درست است.\",\n  \"sources\": [\n    \"https://en.wiktionary.org/wiki/%DA%AF%D8%B1%D9%88%D9%87\",\n    \"https://abadis.ir/fatofa/%DA%AF%D8%B1%D9%88%D9%87/\"\n  ],\n  \"ref_check\": [\n    {\"ref\": \"MON\", \"status\": \"supports\",\n     \"note\": \"no page given by Nourai; Mo'in's entry (vajehyab/abadis, Farhang-e Farsi) reads 'گروه (گُ) [په .] (اِ.) ۱ - دسته، جمعیت . ۲ - امت، فرقه ...' — the [په.] tag is exactly the Pahlavi origin the arrow draws.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"PHD\", \"where\": \"MacKenzie s.v. grōh\", \"stance\": \"supports\",\n     \"note\": \"'grōh [glwh | N guroh] group, crowd' — MacKenzie himself gives the New Persian outcome.\"},\n    {\"src\": \"BQT\", \"where\": \"p.1803, headword گروه + note 4\", \"stance\": \"supports\",\n     \"note\": \"'گروه - بضم اول و ثانی بر وزن شکوه، جماعت مردم را گویند و بعربی قوم خوانند' with note 4 'پهلوی grôh (دسته، گروه)'.\"},\n    {\"src\": \"NYB\", \"where\": \"glossary s.v. grah\", \"stance\": \"supports\",\n     \"note\": \"'... = Paz.; NP guroh' — Nyberg equates the Pahlavi word with New Persian guroh directly.\"}\n  ]\n})\n\nN.append({\n  \"id\": 6, \"lang\": \"Italian\", \"words\": \"grappo\", \"verdict\": \"transcription_suspect\",\n  \"derivation\": \"The word behind French groupe is Italian gruppo 'knot, cluster, group', not grappo. Watkins, the reference Nourai cites, prints it under ger-2 II.4: 'Italian gruppo, an assemblage: GROUP' — 'an assemblage' is verbatim Nourai's gloss, so the box is a copy of that line with the vowel misprinted. Klein: 'group, n. — F. groupe, fr. It. gruppo, ‚group‘, orig. ‚cluster, packet, knot‘, fr. OProvenç. grop, ‚knot‘, which derives fr. Teut. *kruppa, ‚a rounded lump or mass‘'; Webster: 'group, n. [Fr. groupe; It. gruppo, a knot, lump, group; of Germanic origin; compare G. kropf]'; Buck 13.192: 'NE group (fr. Fr. groupe, fr. Ital. gruppo : groppo ‚knot‘)'. Italian grappo does exist — it means 'bunch (of grapes)', synonym of grappolo/graspo, and belongs with Watkins's item I.1e 'Italian dialectal grappa, vine stem' — but it is not the source of groupe and does not mean 'assemblage'. A second, substantive point: the arrow is drawn straight from the Indo-European root to Italian, whereas gruppo is a Germanic loan in Romance (Vulgar Latin *cruppus ← Proto-Germanic *kruppaz 'round mass'), so it reaches the root only through Germanic — the same *kr- family as crop in node #12. The printed page (BOOK/173.png) really does read 'grappo', so this is the book's error, not the extraction's.\",\n  \"derivation_fa\": \"واژهٔ پشتِ groupe فرانسوی، ایتالیایی gruppo «گره، خوشه، دسته» است نه grappo. خودِ مأخذی که نورایی یاد کرده (پیوست AHD) می‌نویسد: 'Italian gruppo, an assemblage: GROUP' — یعنی حتی معنای خانه عیناً از همان سطر گرفته شده و فقط مصوت غلط چاپ شده است؛ کلاین، وبستر و باک هم همین gruppo را دارند. grappo در ایتالیایی هست ولی معنایش «خوشهٔ انگور» است. نکتهٔ دوم آنکه gruppo خود وام‌واژه‌ای ژرمنی در زبان‌های رمانس است (لاتین عامیانه *cruppus از ژرمنی آغازین *kruppaz)، پس پیکان مستقیم از ریشه به ایتالیایی، حلقهٔ ژرمنی را جا انداخته است. تصویر صفحه نشان می‌دهد خطا از چاپ کتاب است.\",\n  \"error_in\": \"book\",\n  \"book_prints\": \"grappo : assemblage\",\n  \"correct_form\": \"gruppo\",\n  \"sources\": [\n    \"https://www.etymonline.com/word/group\",\n    \"https://en.wiktionary.org/wiki/gruppo\",\n    \"https://en.wiktionary.org/wiki/grappo\"\n  ],\n  \"ref_check\": [\n    {\"ref\": \"AHD:582,1516\", \"status\": \"partial\",\n     \"note\": \"The appendix page is right in substance — Watkins ger-2 II.4 'Italian gruppo, an assemblage: Group' (AHD_watkins1985.txt line 494), and in the 1975 New College edition the alphabetical root list runs pp.1505-1550, so ger- falls at about p.1516 as cited; p.582 is the dictionary entry 'group' in that edition. But the reference says gruppo, not the grappo Nourai prints — hence 'partial'. (Local copy is the 1985 standalone reprint, whose pagination differs.)\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. group\", \"stance\": \"contradicts\",\n     \"note\": \"'group, n. — F. groupe, fr. It. gruppo, ‚group‘, orig. ‚cluster, packet, knot‘, fr. OProvenç. grop, ‚knot‘, which derives fr. Teut. *kruppa, ‚a rounded lump or mass‘. See crop.' — gruppo, and a Germanic (not directly IE) source.\"},\n    {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century, s.v. group\", \"stance\": \"contradicts\",\n     \"note\": \"'group, n. [Fr. groupe; It. gruppo, a knot, lump, group; of Germanic origin; compare G. kropf, a bunch, a crop.]' (WEB_vol1.txt line 84959).\"},\n    {\"src\": \"SYN\", \"where\": \"Buck 13.192\", \"stance\": \"contradicts\",\n     \"note\": \"'NE group (fr. Fr. groupe, fr. Ital. gruppo : groppo ‚knot‘), in earliest use an art term (group of sculptured or painted figures)'.\"}\n  ]\n})\n\nN.append({\n  \"id\": 7, \"lang\": \"French\", \"words\": \"groupe\", \"verdict\": \"confirmed\",\n  \"derivation\": \"French groupe is a 17th-century borrowing from Italian gruppo, taken over with the technical vocabulary of painting and sculpture (a 'group' of figures in a composition) during the Italian ascendancy in the arts; Italian -uppo is rendered -oupe, and the word is masculine in both languages. Klein: 'group, n. — F. groupe, fr. It. gruppo'; Etymonline dates the French word to 17c. and the English borrowing to the 1690s. The chart's arrow Italian → French is therefore right, whatever the misprint in the parent box.\",\n  \"derivation_fa\": \"واژهٔ فرانسوی groupe در سدهٔ ۱۷م از ایتالیایی gruppo وام گرفته شده است، در زمینهٔ اصطلاحات نقاشی و پیکره‌سازی (مجموعهٔ پیکره‌ها در یک ترکیب)؛ -uppo ایتالیایی در فرانسه -oupe شده است. کلاین و Etymonline همین مسیر را می‌دهند؛ پیکان نمودار درست است.\",\n  \"sources\": [\"https://www.etymonline.com/word/group\"],\n  \"ref_check\": [\n    {\"ref\": \"None\", \"status\": \"not_checked\",\n     \"note\": \"Nourai gives no reference for this box; it is covered by the AHD citation of its parent (Watkins ger-2 II.4 'Italian gruppo, an assemblage: GROUP', the French stage being implicit in that etymology).\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. group\", \"stance\": \"supports\",\n     \"note\": \"'F. groupe, fr. It. gruppo, ‚group‘' — exactly the Italian → French step.\"},\n    {\"src\": \"WEB\", \"where\": \"Webster s.v. group\", \"stance\": \"supports\",\n     \"note\": \"'[Fr. groupe; It. gruppo, a knot, lump, group ...]'; cf. also 'aggroup ... [Fr. agrouper; It. aggruppare; a, to, and gruppo, a knot, heap, group]' (WEB_vol1.txt line 4547).\"}\n  ]\n})\n\nN.append({\n  \"id\": 8, \"lang\": \"English\", \"words\": \"group\", \"verdict\": \"confirmed\",\n  \"derivation\": \"English group is attested from the 1690s and was, as Buck notes, first an art-critical term — 'assemblage of figures or objects forming a harmonious whole in a painting or design' — taken from French groupe; the general sense 'any assemblage, a number of individuals related in some way' follows by 1736, the verb by 1718. Because the borrowing is post-Great-Vowel-Shift, -ou- is pronounced in the French way (/gruːp/) rather than as in house. Klein, Webster, Buck and Etymonline all give the same three-step chain It. gruppo > F. groupe > E. group, which is Nourai's chain.\",\n  \"derivation_fa\": \"واژهٔ انگلیسی group از دههٔ ۱۶۹۰ میلادی گواهی دارد و نخست اصطلاحی در نقد هنری بوده (مجموعهٔ پیکره‌ها در یک تابلو)، وام‌گرفته از فرانسوی groupe؛ معنای عامّ «دسته، گروه» از ۱۷۳۶. چون وام‌گیری پس از دگرگونی بزرگ مصوت‌ها رخ داده، ou به شیوهٔ فرانسوی /uː/ خوانده می‌شود. ادعای نورایی درست است.\",\n  \"sources\": [\"https://www.etymonline.com/word/group\"],\n  \"ref_check\": [\n    {\"ref\": \"None\", \"status\": \"not_checked\",\n     \"note\": \"No reference in the box; the parent's AHD citation covers it ('Italian gruppo, an assemblage: GROUP').\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. group\", \"stance\": \"supports\",\n     \"note\": \"'group, n. — F. groupe, fr. It. gruppo ... Derivatives: group, tr. and intr. v., group-ed, adj., group-ing, n.'\"},\n    {\"src\": \"SYN\", \"where\": \"Buck 13.192\", \"stance\": \"supports\",\n     \"note\": \"'NE group (fr. Fr. groupe, fr. Ital. gruppo : groppo ‚knot‘), in earliest use an art term ..., has become the most nearly generic term.'\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins ger-2 II.4\", \"stance\": \"supports\",\n     \"note\": \"'Italian gruppo, an assemblage: Group.'\"}\n  ]\n})\n\nN.append({\n  \"id\": 9, \"lang\": \"Germanic\", \"words\": \"grâppon\", \"verdict\": \"transcription_suspect\",\n  \"derivation\": \"The gloss is copied word for word from Watkins ('Germanic *krāppōn-, a hook, especially one used in harvesting grapes'), but the form is printed with g-, which no Germanic form of this root can have: PIE *g- gives Germanic *k- by Grimm's law, which is precisely why this whole family appears in English with kr-/cr- (creep, crop, crutch) while its Romance borrowings keep gr-. The attested cognates are Middle Dutch crappe, Old High German krapfo 'hook', Modern German Krapfen, Old Norse krappr; Pokorny sets them up as extension 3.d 'grep- or g(e)rəp-' of ger-3 (Middle Low German krappe 'hook, claw'). Etymonline: grape 'from a Frankish or other Germanic word, from Proto-Germanic *krappon ‚hook”'; Webster: '[OFr. grape, grappe ... from O.H.G. chrapho, a hook]'. So the entry should read Germanic (Frankish) *krāppōn-. The book page prints 'grâppon', so the extraction is faithful and the error is Nourai's — apparently a silent normalisation of the initial to the g- of his root name 'Ger'.\",\n  \"derivation_fa\": \"معنای این خانه عیناً از واتکینز گرفته شده ('Germanic *krāppōn-, a hook, especially one used in harvesting grapes')، اما صورت با g چاپ شده است و این در ژرمنی ممکن نیست: بر پایهٔ قانون گریم، *g هندواروپایی در ژرمنی به k بدل می‌شود — به همین سبب این خانواده در انگلیسی با cr- پدیدار می‌شود (creep، crop، crutch) و فقط وام‌واژه‌های رمانسی gr- دارند. صورت‌های گواهی‌شده: هلندی میانه crappe، آلمانی علیای کهن krapfo «قلاب»، نوروژی کهن krappr. خطا از خود کتاب است، نه از خوانش اسکن.\",\n  \"error_in\": \"book\",\n  \"book_prints\": \"grâppon : a hook used for harvesting grapes\",\n  \"correct_form\": \"Germanic (Frankish) *krāppōn- 'hook'\",\n  \"sources\": [\"https://www.etymonline.com/word/grape\"],\n  \"ref_check\": [\n    {\"ref\": \"AHD\", \"status\": \"partial\",\n     \"note\": \"Watkins ger-2 I.1: 'Germanic *krāppōn-, a hook, especially one used in harvesting grapes, in: a. Old High German krapfo, a hook: AGRAFFE; b. Old French graper, to harvest grapes, hence (back-formation) grape, vine, grape: GRAPE' (AHD_watkins1985.txt lines 492-494) — the gloss is verbatim, the initial consonant is not.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"pp.387-388, ger-3 extension 3.d\", \"stance\": \"supports\",\n     \"note\": \"'d. grep- or g(e)rəp- ... in Middle Low German krappe ‚hook, claw, talon‘; holl. krap ‚cramp‘, Old High German krapfo ‚bent claw, talon, hook‘, Modern High German Krapfen ... Old Norse krappr' — all with k-.\"},\n    {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. grape / cramp\", \"stance\": \"supports\",\n     \"note\": \"'grape, n. — OF. grape, grappe ... fr. OF. craper, graper, ‚to seize with a hook; to gather grapes‘, which is of Teut. origin. Cp. MDu. crappe, OHG. krapfo, ‚a hook‘, G. Krapfen ...'\"},\n    {\"src\": \"WEB\", \"where\": \"Webster s.v. grape\", \"stance\": \"supports\",\n     \"note\": \"'grape, n. [OFr. grape, grappe, a bunch or cluster of grapes, from O.H.G. ... chrapho, a hook]'.\"}\n  ]\n})\n\nN.append({\n  \"id\": 10, \"lang\": \"English\", \"words\": \"grape\", \"verdict\": \"confirmed\",\n  \"derivation\": \"English grape (mid-13c.) is not a direct Germanic inheritance but comes through French: Old French grape/grappe 'hook; bunch of grapes' is a back-formation from graper 'to seize with a hook, gather grapes', itself from the Frankish *krāppōn- of the parent box; the notion is the vine-hook used at the vintage, and the borrowed word displaced native Old English winberige 'wine-berry' (the vine not being grown in England). Watkins states the same route ('Old French graper, to harvest grapes, hence (back-formation) grape, vine, grape: GRAPE'), as do Klein, Webster and Etymonline; Spanish grapa and Italian grappa 'hook' are parallel borrowings of the same Germanic word. The chart's single arrow Germanic → English is thus right in substance but silently omits the Old French stage, which is where the sense 'grape' (rather than 'hook') arose.\",\n  \"derivation_fa\": \"واژهٔ انگلیسی grape (از میانهٔ سدهٔ ۱۳م) میراث مستقیم ژرمنی نیست بلکه از راه فرانسه آمده است: فرانسهٔ کهن grape/grappe «قلاب؛ خوشهٔ انگور» که از فعل graper «با قلاب گرفتن، انگور چیدن» پس‌ساخته شده و خود آن از فرانکی *krāppōn- «قلاب تاک‌بری» است؛ این وام‌واژه جای واژهٔ بومی انگلیسی کهن winberige را گرفت. نمودار درست است اما حلقهٔ فرانسهٔ کهن را نیاورده است.\",\n  \"sources\": [\"https://www.etymonline.com/word/grape\"],\n  \"ref_check\": [\n    {\"ref\": \"None\", \"status\": \"not_checked\",\n     \"note\": \"no reference in this box; the parent box's AHD citation carries it: Watkins ger-2 I.1.b 'Old French graper, to harvest grapes, hence (back-formation) grape, vine, grape: GRAPE'.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. grape\", \"stance\": \"supports\",\n     \"note\": \"'grape, n. — OF. grape, grappe, ‚hook; a bunch of grapes‘ (whence F. grappe) ... which is of Teut. origin ... Cp. OProvenç., Sp. grapa, It. grappa, ‚hook‘, which are also Teut. loan words.'\"},\n    {\"src\": \"WEB\", \"where\": \"Webster s.v. grape\", \"stance\": \"supports\",\n     \"note\": \"'[OFr. grape, grappe, a bunch or cluster of grapes, from O.H.G. chrapho, a hook]'.\"}\n  ]\n})\n\nN.append({\n  \"id\": 11, \"lang\": \"Old English\", \"words\": \"\", \"verdict\": \"confirmed\",\n  \"derivation\": \"An empty pass-through box: Nourai uses it to collect the native English words of the root, whose common ancestor is not one Old English word but the whole set of Old English kr-/cr- formations Watkins lists under ger-2 — crypel, crēopan, crycc, cranc-(stæf), cruma, cropp, cribb, cradol, cræt. Labelling that set 'Old English' is legitimate: every one of them is attested in Old English, and the initial cr- is the regular Germanic outcome of PIE *gr- (Grimm's law), which is what makes the box the Germanic-inherited counterpart to the Romance-borrowed Italian/French branch above it.\",\n  \"derivation_fa\": \"این خانه تهی است و فقط نقش واسطه دارد: نورایی واژه‌های بومی انگلیسی این ریشه را یکجا زیر «انگلیسی کهن» آورده است. نیای مشترک آن‌ها یک واژه نیست، بلکه مجموعه‌ای از صورت‌های انگلیسی کهن است که واتکینز زیر ger-2 برمی‌شمرد: crypel، crēopan، crycc، cranc-stæf، cruma، cropp، cribb، cradol، cræt. آغازهٔ cr- دقیقاً برآیندِ قانون گریم از *gr- هندواروپایی است.\",\n  \"sources\": [],\n  \"ref_check\": [\n    {\"ref\": \"AHD\", \"status\": \"supports\",\n     \"note\": \"Watkins ger-2 lists the Old English members explicitly: 'Old English crypel, a cripple', 'Germanic *kreupan in Old English crēopan, to creep', 'Old English crycc, (bent) staff, crutch', 'Old English cranc-(stæf), a weaving implement', 'Old English cruma, a fragment', 'Old English cropp, cluster, bunch, ear of corn', 'Old English cribb, manger', 'Old English cradel, cradle', 'Old English cræt and Old Norse kartr, wagon'.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"pp.386-389, ger-3\", \"stance\": \"supports\",\n     \"note\": \"the same Old English forms are Pokorny's: 'ags. cradol m. ‚Wiege“', 'Old English cribb ‚crib, manger“', 'Old English cræt m. ‚cart“', 'Old English cryppel ‚cripple“', 'Old English creopan ‚creep“', 'Old English crycc'.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins ger-2 I and II\", \"stance\": \"supports\",\n     \"note\": \"'hypothetical Indo-European base for a variety of Germanic words with initial kr-' — exactly the box's function.\"}\n  ]\n})\n\nN.append({\n  \"id\": 12, \"lang\": \"English\",\n  \"words\": \"cripple, creep, crutch, crank, crumb, crop, crib, cradle, cart\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"All nine are Watkins's own English outcomes of ger-2 and each has the Old English etymon the parent box implies: cripple < OE crypel (Pok. 'Old English crēper cripple' under greu-b-); creep < OE crēopan (Gmc *kreupan, Pok. greu-b- 'Old Norse krjúpa, Old English creopan ‚creep“'); crutch < OE crycc '(bent) staff' (Pok. greu-g- 'Old English crycce, nengl. crutch', a 'staff with crooked handle'); crank < OE cranc-(stæf) 'weaving implement' (Pok. 'Old English cranc-stæf ‚a weaver's device“'); crumb < OE cruma 'fragment' (Pok. B. gr-eu- 'Old English cruma ‚crumb“, what one scratches from the hard crust'); crop < OE cropp 'cluster, bunch, ear of corn' (Pok. greu-b- 'Old English cropp ‚bundle of berries or flowers, ear, goiter, crop“'); crib < OE cribb 'manger' (Pok. ger-bʰ- 'Old English cribb ‚crib, manger“'); cradle < OE cradol (Pok. *gr-et(h)- '*kradula- ‚the plaited“'). The one that needs a footnote is cart: Watkins writes 'Old English cræt and Old Norse kartr, wagon: CART', but the actual Middle English carte is generally taken from the Norse word — Etymonline, 'c. 1200 ... from Old Norse kartr or a similar Scandinavian source, akin to and replacing Old English cræt' — so its parent box would more accurately be Old Norse. The semantics throughout are the root's two halves: 'bent/hooked' (cripple, creep, crutch, crank) and 'rounded mass / plaited container' (crumb, crop, crib, cradle, cart).\",\n  \"derivation_fa\": \"هر نه واژه در فهرستِ خودِ واتکینز ذیل ger-2 آمده‌اند و هر یک نیای انگلیسی کهن دارد: cripple < crypel، creep < crēopan، crutch < crycc «عصای خمیده»، crank < cranc-stæf، crumb < cruma، crop < cropp، crib < cribb، cradle < cradol (پوکورنی: *kradula- «بافته‌شده»). دو نیمهٔ معنایی ریشه در همین فهرست پیداست: «خمیده/قلاب‌مانند» و «تودهٔ گرد، سبدِ بافته‌شده». تنها cart نیاز به توضیح دارد: هرچند انگلیسی کهن cræt وجود داشته، صورت انگلیسی میانهٔ carte را بیشتر وام از نوروژی کهن kartr می‌دانند. در مجموع ادعای نورایی درست است.\",\n  \"sources\": [\"https://www.etymonline.com/word/cart\"],\n  \"ref_check\": [\n    {\"ref\": \"None\", \"status\": \"not_checked\",\n     \"note\": \"no reference in this box; its parent cites AHD, and Watkins's ger-2 entry names all nine words in capitals (CRIPPLE, CREEP, CRUTCH, CRANK, CRUMB, CROP, CRIB, CRADLE, CART).\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"AHD\", \"where\": \"Watkins ger-2 I.2-18, II.1-11\", \"stance\": \"supports\",\n     \"note\": \"'6. Old English crypel, a cripple: CRIPPLE. 7. Germanic *kreupan in Old English crēopan, to creep: CREEP ... 14. Old English crycc, (bent) staff, crutch: CRUTCH ... 17. Old English cranc-(stæf) ... CRANK' and 'II. 1. Old English cruma, a fragment: CRUMB ... 3. Old English cropp ... CROP ... 7. Old English cribb, manger: CRIB. 8. Old English cradel, cradle: CRADLE. 10. Old English cræt and Old Norse kartr, wagon: CART.'\"},\n    {\"src\": \"POK\", \"where\": \"pp.386-389\", \"stance\": \"supports\",\n     \"note\": \"'Old Norse kartr, Old English cræt m. ‚cart“ (probably ‚twisted carriage basket“)'; 'Old English cruma ‚crumb“ (‚what one scratches from the hard crust“)'; 'Old English crycce, nengl. crutch'; 'ags. cradol m. ‚Wiege“ (*kradula- ‚das Geflochtene“)'.\"},\n    {\"src\": \"KLN\", \"where\": \"Klein s.v. cramp/crop\", \"stance\": \"partial\",\n     \"note\": \"Klein groups the same kr- family ('cramp ... rel. to OHG. kramph ‚bent, crooked“ ... Cp. also crimp, crumple and grape, grapple, grapnel') but, in the manner of his dictionary, does not always carry them back to a single IE root.\"}\n  ]\n})\n\nN.append({\n  \"id\": 13, \"lang\": \"Dutch\", \"words\": \"crulle\", \"verdict\": \"confirmed\",\n  \"derivation\": \"Nourai's own note is the correction: the form is Middle Dutch, not modern Dutch (modern Dutch is krul). Middle Dutch crulle/crul 'curly' is item I.16 of Watkins's ger-2 ('Middle Dutch crulle, curly: CRULLER, CURL'), and Pokorny puts the family under the s-extension greu-s- on p.389: 'Old High German Middle High German krol(-ll-) ‚frizzy“ (*kruzla-). Middle High German krol(le), krulle ‚curl“, Norwegian krull'. Proto-Germanic *kruzlō̄ gives Middle Dutch crulle by the regular West Germanic rhotacism-plus-assimilation zl > ll, and the whole set (MDu. crul, MHG krolle, Norw. krull, Dan. krølle) belongs together. The book's own NOTE that this is a Middle Dutch word is right and should be kept.\",\n  \"derivation_fa\": \"خودِ نورایی در یادداشت تصریح کرده که این واژه هلندی میانه است نه هلندی نو (در هلندی امروز krul است) و همین درست است. صورت crulle «مجعد، فر‌خورده» در پیوست واتکینز (بند I.16) و در پوکورنی (ص ۳۸۹، گسترش greu-s-: 'Middle High German krol(le), krulle ‚curl“') آمده است؛ از ژرمنی آغازین *kruzlō̄ با دگرگونی zl > ll. ادعای نورایی درست است.\",\n  \"sources\": [\"https://en.wiktionary.org/wiki/curl\"],\n  \"ref_check\": [\n    {\"ref\": \"AHD\", \"status\": \"supports\",\n     \"note\": \"Watkins ger-2 I.16: 'Middle Dutch crulle, curly: CRULLER, CURL' — including the 'Middle' that Nourai's box relegates to a note.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"p.389, ger-3 B.3 greu-s-\", \"stance\": \"supports\",\n     \"note\": \"'Old High German Middle High German krol(-ll-) ‚frizzy“ (*kruzla-). Middle High German krol(le), krulle ‚curl“, Norwegian krull ds.'\"},\n    {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. curl\", \"stance\": \"supports\",\n     \"note\": \"lists the cognate set 'Norw. krull, Dan. krolle, E. Fris. krul, krulle, MDu. crulle, crolle, crul, Du. krul, ‚curl‘ ... MHG. krol, ‚curly‘'.\"}\n  ]\n})\n\nN.append({\n  \"id\": 14, \"lang\": \"English\", \"words\": \"curl\", \"verdict\": \"plausible\",\n  \"derivation\": \"The English word is certainly this family, and the mechanism is the striking one: metathesis of r and the vowel. Middle English crul(le) 'curly' and the verb crullen were re-ordered to curl(en) in the 14th-15th c. — Klein: 'curl, tr. and intr. v. — ME. curlen, metathesized fr. ME. crullen, fr. crul, ‚curly‘ ... For the metathesis of ME. crullen to curlen cp. curd'; the same shift produced curd from crud and, later, bird from brid. What is only 'plausible' is the arrow as drawn, Middle Dutch → English: Klein says ME crul is 'related to' MDu. crulle rather than taken from it, and Wiktionary writes 'From metathesis of Middle English crulle ‚curled, curly“, of uncertain origin but probably from an unrecorded Old English word or from Middle Dutch crul, crulle', ultimately Proto-Germanic *kruzlō̄. So the word may be native English rather than a Dutch loan; either way it goes back to the same Germanic *kruzl-, and Watkins's ger-2 I.16 files CURL under Middle Dutch crulle exactly as Nourai does.\",\n  \"derivation_fa\": \"واژهٔ انگلیسی curl بی‌گمان از همین خانواده است و سازوکار آن قلب (metathesis) است: انگلیسی میانهٔ crul/crullen در سده‌های ۱۴–۱۵م به curl/curlen دگرگون شده، همان دگرگونی که crud > curd و brid > bird را پدید آورده است (کلاین). اما پیکان «هلندی میانه ← انگلیسی» قطعی نیست: کلاین می‌گوید crul انگلیسی «هم‌ریشهٔ» crulle هلندی است نه وام‌گرفته از آن، و ویکی‌واژه آن را «شاید از واژه‌ای ناشناخته در انگلیسی کهن یا از هلندی میانه» می‌داند. پس با احتیاط پذیرفتنی است.\",\n  \"sources\": [\"https://en.wiktionary.org/wiki/curl\"],\n  \"ref_check\": [\n    {\"ref\": \"None\", \"status\": \"not_checked\",\n     \"note\": \"no reference in the box; the parent's AHD citation covers it — Watkins ger-2 I.16 'Middle Dutch crulle, curly: CRULLER, CURL'.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. curl\", \"stance\": \"partial\",\n     \"note\": \"'curl, tr. and intr. v. — ME. curlen, metathesized fr. ME. crullen, fr. crul, ‚curly‘, which is rel. to Norw. krull, Dan. krolle ... MDu. crulle, crolle, crul, Du. krul, ‚curl‘' — 'related to', not 'from', the Middle Dutch word.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins ger-2 I.16\", \"stance\": \"supports\",\n     \"note\": \"'Middle Dutch crulle, curly: CRULLER, CURL' — the arrow Nourai draws.\"},\n    {\"src\": \"POK\", \"where\": \"p.389\", \"stance\": \"supports\",\n     \"note\": \"puts MHG krol(le), krulle 'curl' and its Norwegian and Low German kin under the greu-s- extension of ger-3, i.e. inside this root.\"}\n  ]\n})\n\ndoc = {\n  \"pdf_page\": 173,\n  \"book_page\": 143,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-05\",\n  \"entries\": [entry]\n}\n\nimport io\nwith io.open(\"/home/sfmqrb/git/rishe/data/verification/page-173.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(doc, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"ok\", len(N))\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build173.py"
}
```


### [2026-09-05T21:08:29.404Z] TOOL RESULT

```
ok 14
```


## [2026-09-05T21:08:33.415Z] TOOL CALL #83: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -m json.tool data/verification/page-173.json > /dev/null && echo \"JSON OK\"; python3 tools/verify_check.py 173"
}
```


### [2026-09-05T21:08:35.150Z] TOOL RESULT

```
JSON OK
nodes verified: 14/14
node verdicts: {'plausible': 3, 'transcription_suspect': 3, 'confirmed': 8}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 5, 'partial': 4, 'not_checked': 6}
books consulted: {'supports': 28, 'partial': 8, 'silent': 3, 'contradicts': 3} | by book: {'KLN': 8, 'POK': 5, 'CHEUNG': 4, 'WEB': 4, 'AHD': 4, 'SYN': 3, 'PHD': 3, 'NYB': 3, 'BQT': 2, 'WLD': 1, 'IEC': 1, 'HUB': 1, 'KNT': 1, 'BRT': 1, 'HRN': 1}
```


## [2026-09-05T21:08:43.169Z] TOOL CALL #84: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 - <<'EOF'\nimport json,urllib.parse\nd=json.load(open('data/verification/page-173.json'))\nurls=set()\ndef walk(o):\n    if isinstance(o,dict):\n        for k,v in o.items():\n            if k=='sources': urls.update(v)\n            else: walk(v)\n    elif isinstance(o,list):\n        for i in o: walk(i)\nwalk(d)\nidx=[json.loads(l) for l in open('data/verification/sources/web/index.jsonl',encoding='utf-8')]\nhave={}\nfor r in idx: have[r['url']]=r.get('status')\nfor u in sorted(urls):\n    n=urllib.parse.unquote(u)\n    st = have.get(u, have.get(n,'MISSING'))\n    print(st, u)\nEOF"
}
```


### [2026-09-05T21:08:45.353Z] TOOL RESULT

```
200 https://abadis.ir/fatofa/%DA%AF%D8%B1%D9%87/
200 https://abadis.ir/fatofa/%DA%AF%D8%B1%D9%88%D9%87/
200 https://en.wiktionary.org/wiki/%DA%AF%D8%B1%D9%87
200 https://en.wiktionary.org/wiki/%DA%AF%D8%B1%D9%88%D9%87
200 https://en.wiktionary.org/wiki/curl
200 https://en.wiktionary.org/wiki/grappo
200 https://en.wiktionary.org/wiki/gruppo
200 https://www.etymonline.com/word/cart
200 https://www.etymonline.com/word/grape
200 https://www.etymonline.com/word/group
```


## [2026-09-05T21:09:02.978Z] AGENT

Page 173 (book p. 143), single entry — root **Ger 1** [Indo-European] "crooked, curved, round object", 14 nodes. Verified file written, `verify_check.py 173` → 14/14 nodes, **0 PROBLEM lines**.

Verdicts: root confirmed · nodes 8 confirmed, 3 plausible, 3 transcription_suspect. Ref checks: 5 supports, 4 partial, 6 not_checked. Books consulted: POK, WLD, AHD/Watkins, SYN (Buck), IEC (Mann), KLN, WEB, HUB, KNT, BRT, PHD, NYB, HRN, CHEUNG, BQT.

Root confirmed: Pokorny "ger-3, to turn, wind, Page(s) 385-390" = Nourai's POK:385; Watkins "ger-²  Curving, crooked … II. a rounded mass … [Pok. 3. ger- 385]" is the source of the three-part gloss.

transcription_suspect (all `error_in: "book"` — the JSON reproduces p. 143 faithfully; page image saved to `data/verification/sources/refs/ocr/BOOK/173.png`):
- #2 Old Persian **gravatha** — Mo'in's footnote on the very page cited (Borhān 1803 n.4) reads *gravathva* (Nyberg p.84) and labels it *Old Iranian*, not Old Persian; also neither word is attested in Kent (both are starred reconstructions printed unstarred).
- #6 Italian **grappo** — should be *gruppo*; Watkins ("Italian gruppo, an assemblage: GROUP"), Klein, Webster and Buck all have gruppo; Italian grappo means "bunch of grapes".
- #9 Germanic **grâppon** — should be *krāppōn-* (Watkins's own form); Germanic cannot have g- from PIE *g- (Grimm).

plausible: #1 Skt. granth under *ger- (Pokorny/WLD/Buck yes, Cheung 2007:123 and Wiktionary call the IE anchoring uncertain); #4 Pahlavi grōh drawn out of the knot-box (Mo'in gives it a separate etymon; Wiktionary's supporting note cites Nourai himself — circular); #14 curl (Klein: ME crul "related to", not from, MDu crulle).

No extraction errors: everything in `page-173.json` matches the printed page.

Two data notes for you: (1) VFO (Soltani) remains unavailable — `refs_online.json` has it as null, so VFO:25 is `not_checked` as on pages 44/77. (2) `tools/ref_page.py BQT:1803` renders the **wrong** page — printed 1803 is pdf 600, not 598 (running heads 1801/1802/1803/1804 = pdf 598/599/600/601, i.e. printed = pdf+1203 in that region, while the pagemap anchor '1797': 592 implies +1205). I saved the correct transcription to `data/verification/sources/refs/ocr/BQT/1803.vision.txt` and replaced `1803.png`; the stale `1803.txt` (OCR of p. 1801) is still there.
