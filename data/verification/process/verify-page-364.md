# Verification process log — verify-page-364


## [2026-09-07T19:29:12.851Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 364 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-364.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-364.json. Write /home/sfmqrb/git/rishe/data/verification/page-364.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 364` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-07T19:29:14.838Z] AGENT

I'll start by reading the instructions.


## [2026-09-07T19:29:15.672Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-07T19:29:15.684Z] TOOL RESULT

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


## [2026-09-07T19:29:16.063Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-364.txt"
}
```


### [2026-09-07T19:29:16.075Z] TOOL RESULT

```
1	=== PDF page 364 (book page 334) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Newo / Nu : new / new time, now  (refs POK:769,770; AHD:1531)
4	#1 (parent #0) [Avestan] refs=POK:769,770; KLN:1059; KNT:194; IEC:854 | nava 2 : new ; nŭ, nŭrem : now
5	  #2 (parent #1) [Persian] refs=BQT:2173; HRN:236 | now «نو» : new ; aknŭn, knŭn «اکنون ، کنون» : now
6	  #3 (parent #1) [Pahlavi] refs=MON:4859 | nîvěd : good news
7	    #4 (parent #3) [Persian] refs=IEC:842; MON:4859 | novîd «نوید» : good news
8	  #5 (parent #1) [Sogdian] refs=SOD:246 | nwr : now
9	#6 (parent #0) [Old Persian] refs=POK:770; KNT:194 | nŭram : now
10	#7 (parent #0) [Germanic] refs=AHD:1531 | neuja : new, now
11	  #8 (parent #7) [English] refs=None | new, now
12	#9 (parent #0) [Greek] refs=AHD | neos : new
13	  #10 (parent #9) [English] refs=None | neo-, neon
14	#11 (parent #0) [Latin] refs=AHD | novus : new
15	  #12 (parent #11) [English] refs=None | nova, novel, novice ; innovate, renovate
16	
```


## [2026-09-07T19:29:19.542Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-364.json",
 "description": "Read source JSON page 364"
}
```


### [2026-09-07T19:29:19.586Z] TOOL RESULT

```
{
  "pdf_page": 364,
  "book_page": 334,
  "entries": [
    {
      "root": {
        "name": "Newo / Nu",
        "lang": "Indo-European",
        "refs": "POK:769,770; AHD:1531",
        "gloss": "new / new time, now"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:769,770; KLN:1059; KNT:194; IEC:854",
          "words": [
            {"translit": "nava 2", "gloss": "new", "script": null},
            {"translit": "nŭ, nŭrem", "gloss": "now", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:2173; HRN:236",
          "words": [
            {"translit": "now", "gloss": "new", "script": "نو"},
            {"translit": "aknŭn, knŭn", "gloss": "now", "script": "اکنون ، کنون"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "MON:4859",
          "words": [
            {"translit": "nîvěd", "gloss": "good news", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Persian",
          "refs": "IEC:842; MON:4859",
          "words": [
            {"translit": "novîd", "gloss": "good news", "script": "نوید"}
          ],
          "note": null,
          "quote": {
            "text": "بیا که رایت منصور پادشاه رسید - نوید فتح و بشارت به مهر و ماه رسید",
            "poet": "Hâfez"
          }
        },
        {
          "id": 5,
          "parent": 1,
          "lang": "Sogdian",
          "refs": "SOD:246",
          "words": [
            {"translit": "nwr", "gloss": "now", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Old Persian",
          "refs": "POK:770; KNT:194",
          "words": [
            {"translit": "nŭram", "gloss": "now", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD:1531",
          "words": [
            {"translit": "neuja", "gloss": "new, now", "script": null}
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
            {"translit": "new, now", "gloss": null, "script": null}
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
            {"translit": "neos", "gloss": "new", "script": null}
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
            {"translit": "neo-, neon", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "novus", "gloss": "new", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 11,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "nova, novel, novice", "gloss": null, "script": null},
            {"translit": "innovate, renovate", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
```


## [2026-09-07T19:29:20.958Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','AHD','KLN','KNT','IEC','BQT','HRN','MON','SOD','WLD','SYN','PHD','NYB','HUB','ARY','SKT','FSD','WEB','CHEUNG']:\n    v=d.get(k)\n    print(k, json.dumps(v,ensure_ascii=False)[:400] if v else 'MISSING')\n\"",
 "description": "Inspect refs_online entries"
}
```


### [2026-09-07T19:29:22.333Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "loca
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in 
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
CHEUNG MISSING
```


## [2026-09-07T19:29:26.648Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; ls data/verification/sources/refs/ | head -80; echo ---; sed -n 1,80p data/verification/sources/SOURCE_MATRIX.md",
 "description": "List local refs and matrix head"
}
```


### [2026-09-07T19:29:26.702Z] TOOL RESULT

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


## [2026-09-07T19:30:04.431Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport re,io\nfor f in ['POK_full.txt','POK_01.txt','POK_02.txt','POK_03.txt']:\n    t=open(f,encoding='utf-8',errors='replace').read()\n    # find page markers\n    m=re.findall(r'\\[?(?:pdf )?page \\d+\\]?',t[:2000])\n    print(f, len(t), t.count('\\f'), m[:3])\nEOF"
}
```


## [2026-09-07T19:30:05.518Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','AHD','KLN','KNT','IEC','SOD','BQT','HRN','MON','BRT','PHD','NYB','ARY','SYN','WLD']:\n    v=d[k]\n    print('==',k)\n    for f in ['local_file','page_offset','lookup_hint','scans','cites','kind']:\n        if v.get(f): print('  ',f,':',str(v[f])[:500])\n\""
}
```


### [2026-09-07T19:30:05.721Z] TOOL RESULT

```
POK_full.txt 3967710 0 []
POK_01.txt 966268 363 []
POK_02.txt 1119436 433 []
POK_03.txt 1150862 429 []
```


### [2026-09-07T19:30:06.907Z] TOOL RESULT

```
== POK
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt
   page_offset : POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?bas
   cites : page number of Pokorny, Indogermanisches etymologisches Wörterbuch, Band I (1959)
   kind : archive_djvu
== AHD
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt
   page_offset : 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.
   lookup_hint : Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New Colleg
   cites : page number of the 1975/76 New College Edition; pp. 1505–1550 are the Indo-European roots appendix (look the root up by name)
   kind : archive_djvu+website+archive_restricted
== KLN
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt
   page_offset : KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
   cites : page number, continuous across the two volumes (1966–67)
   kind : archive_djvu
== KNT
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt
   page_offset : leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Lexicon (Part III, pp. 164 ff.) headwords are transliterated OP words at line start followed by part of speech, e.g. grep -n '^apadana-' ; section refs like '$147'. Nourai's page numbers should fall in 164-215 for lexicon citations.
   cites : page number of Kent, Old Persian (1953); the lexicon starts p. 164
   kind : archive_djvu
== IEC
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt
   page_offset : TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.
   cites : column/page number of Mann, An Indo-European Comparative Dictionary (1984–87)
   kind : archive_djvu
== SOD
   local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD.txt']
   page_offset : printed page ≈ leaf − 66 in SOD_pages.txt (0-based \f blocks; 645 leaves; English intro precedes)
   lookup_hint : Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get serv
   cites : entry number / page in Gharib's Sogdian dictionary
   kind : archive_djvu
== BQT
   local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '
   page_offset : vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, 
   lookup_hint : grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf imag
   scans : [{'volume': '3', 'file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', 'first_printed': 1208, 'last_printed': 1925, 'pdf_offset': -1205, 'page_map': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pagemap.json', 'lang': 'fas', 'ocr_text': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', 'ocr_note': '689/721 pdf pages OCRed (tesseract fas+eng, mediocre); pages are separated by form-feeds a
   cites : page number, continuous across the five volumes of Mo'in's edition (1342/1963 = Amir Kabir 1362 reprint); Mo'in's etymological footnotes are the cited material
   kind : archive_djvu+local_scan_ocr
== HRN
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt
   page_offset : leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.
   cites : page number of Horn, Grundriss der neupersischen Etymologie (1893); entries are also numbered
   kind : archive_djvu
== MON
   local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incom
   lookup_hint : Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Aden
   cites : page number of Mo'in's six-volume Farhang-e Farsi; MON5:… / MON6:… = volume 5 / 6 (proper names)
   kind : website+archive_djvu
== BRT
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt
   page_offset : Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special transliteration is noisy - grep on a distinctive Latin gloss or the German meaning in quotes. Column numbers appear as standalone numbers at leaf tops.
   cites : column number (the Altiranisches Wörterbuch is numbered by column, two per page)
   kind : archive_djvu
== PHD
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt
   page_offset : leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsianjoman.org/wp-content/uploads/2015/09/A-Concise-Pahlavi-Dictionary.pdf (8.4 MB).
   cites : page number of MacKenzie, A Concise Pahlavi Dictionary (1971)
   kind : archive_djvu
== NYB
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt
   page_offset : Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates and 'Bthl.' refs.
   cites : page number of Nyberg, A Manual of Pahlavi, Part II Glossary (1974)
   kind : archive_djvu
== ARY
   local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt']
   page_offset : printed page = pdf page + 1
   lookup_hint : Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image
   scans : [{'file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_aryanpur_kashani_rishehaye_hend_o_orupayi.pdf', 'first_printed': 1, 'last_printed': 546, 'pdf_offset': -1, 'lang': 'fas+eng', 'ocr_text': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt'}]
   kind : local_scan_ocr
== SYN
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt
   page_offset : leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed page number line.
   cites : page number of Buck, A Dictionary of Selected Synonyms (1949)
   kind : archive_djvu
== WLD
   local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf', '/home/sfmqrb/git/rishe/data/veri
   page_offset : Band 3: leaf = printed + 6. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696).
   lookup_hint : Band 3 is the index (Wortregister by language) - it maps a word to 'Band, page' in vols 1-2, so it can at least confirm that a word is treated at the cited WP volume/page. For the actual entry text, use Pokorny 1959 (POK), whose entries cite 'WP. I 177' etc. and are essentially a revision of WP.
   cites : volume (WLD1 / WLD2) and page of Walde–Pokorny
   kind : archive_djvu
```


## [2026-09-07T19:30:11.495Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"Page(s): 769\" POK_full.txt; echo ---; grep -n \"Page(s): 770\" POK_full.txt; echo ---; grep -n \"lemma: neu\" POK_full.txt; grep -n \"lemma: nu\" POK_full.txt"
}
```


### [2026-09-07T19:30:11.559Z] TOOL RESULT

```
62986:Page(s): 769 
63052:Page(s): 769 
63106:Page(s): 769 
63115:Page(s): 769 
---
63064:Page(s): 770 
63110:Page(s): 770 
63121:Page(s): 770 
63135:Page(s): 770 
63171:Page(s): 770 
---
26525:/ lemma: neuos, -ios: new' + Root/ lemma: oRtd(u)\ eight'. 
26543:lemma: neuos, -ios: 'new' > gr. *£Fva-: zwd-zizc,. The shift k'^> p, g"'> b'\s a common gr.. 
26585:Root / lemma: neuos, -ios: new' + Root/ lemma: oRtd(u)\ eight'. 
61825:Root/ lemma: nas-: nose' derived from Root/ lemma: neu-ks-, neu-s-\ "to sniff, smell' 
62820:Root / lemma: neu-6^- {*he- neu-dy-) 
62835:Root / lemma: neu-d- {*he- neu-d-) 
62863:Root / lemma: neu-ks-, neu-s- {*he- neu-ks-) 
62869:Root/ lemma: nas-: nose' : Root/ lemma: neu-ks- neu-s-: "to sniff, smell' derived from 
62892:Root / lemma: neuk- {*he- neuk-) 
62910:Root / lemma: neu-1{*he- neu-f) 
62924:Root / lemma: neu-2{*he- neu-2) 
62953:Root / lemma: neuos, -ios i*he- neuos, -/os) 
63139:Root / lemma: nu- {*he- nu-)
```


## [2026-09-07T19:30:12.444Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"^newo-\\|^newos\\|^neu-\\|^nu-\\|^new\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-07T19:30:12.530Z] TOOL RESULT

```
785:neu-'. To shout. Suffixed (participial) o-grade form *now-ent-(yo-), “shouting,” in Latin niintius, “announc- ing,” hence a messenger, also a message, and ndéntium, message: NUNCIO; ANNOUNCE, DENOUNCE, ENUNCIATE, PRONOUNCE, RENOUNCE. [Pok. 1. neu: 767.] neu-2, To nod. 1. Latin *nuere, to nod (attested only in compounds), frequentative nutdre, to nod: NUTATION; INNUENDO. 2. Suffixed form *neu-men- in Latin niimen, “a nod,” hence “command,” divine power, deity: NUMEN. [Pok. 2. neu- 767.] neud-. To make use of, enjoy. Germanic *nautam, “thing of value, possession,” in: a. Old English néat, bovine
786:newn
```


## [2026-09-07T19:30:15.520Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '62953,63000p' POK_full.txt; echo \"=== nu- ===\"; sed -n '63139,63180p' POK_full.txt"
}
```


### [2026-09-07T19:30:15.595Z] TOOL RESULT

```
Root / lemma: neuos, -ios i*he- neuos, -/os) 
Meaning: new 

Material: Old Indie nava-, Avestan nava-'ueW, Kompar. navatara-{\ gr. v£(ji)T£po(;), gr. 
v£(F)oc;, Latin novus, Oscan Nuvlanuis' NolanTs ' (from *Nuvela= Latin Nola), Old 
Lithuanian navas. Old Prussian /7e'i/M/e'/7e/7 certain Nom. Sg. n. {*nawanjan\ Old Prussian 
/7ai//7s probably aiterjauns' young '), Old Bulgarian novb "new'; -/o-iorm Old Indie navya-, 
Ionian v£To(;, gall. Nevio-, Novio-dunum {' new castle '), Old Irish nue, cymr. newydd, abret. 
nouuid, neuued, bret. neuez, Gothic niujis. Old Icelandic nyr. Old High German Old Saxon 
niuwi. Old English nTwe, neowe, Lithuanian nau/as'ne\N'; Tocharian A nu, B nune6s., 
Hittite neua-6s.; with -/■o-forms gr. v£(F)ap6(;, Armenian nor'new' {*nouero-), Latin nover- 
ca " stepmother '; 

Maybe alb. njerka' stepmother ' a Latin loanword. 
Maybe aphesis alb. {*nouero-) re{iev(\.), /-/(masc.) "new'. 



gr. veaoo = Latin novare' make new| renovate; renew| refresh] change ' (therefrom novalis^ fallow- 
land; enclosed land| field, a field which is plowed for the first time or after one-year-old rest'; 
forms as in aequalis' equal| similar; uniform] level| flat; of the same age/generation/duration ', also " 
being of young age '); v£6Tr|<; = Latin novitas' restored state (as new); being new 
appointed/promoted; surprise; modern times '; Feminina with A- besides J-suffix (see Specht Indo 
Germanic Dekl.323 f.) lie consecutive formations the basic: Latin novTcius^ new| fresh; esp. 
of persons new to slavery '; russ. novikh " beginner; novice, neophyte; inexperienced person; trainee, 
recruit '; gr. vsa^ "young scoundrel '; Church Slavic novakt ' beginner; novice, neophyte; 
inexperienced person; trainee, recruit '; but vsaviac; " youngling ' from vsFo-av- "young 
Atmender' ; v£OXMO<; "new' see above S. 414. 

References: WP. II 324, WH. II 181, Trautmann 194. 

See also: Changing through ablaut nu' now' see there; s. also *e-neuen^ nine '. 

Page(s): 769 

Root / lemma: neik- : nlk- : nik- {*he- neik-) 

Meaning: to attack; to fight, rail 

Material: Gr. veTkoc; n. "quarrel, fight', veiksoj " quarrel, dispute, argue, fight, scold ', perhaps 

also viKP), Doric vTkq f. "victory', vIkqw " win'; Celtic (?) FIN Nicros^ Neckar '; Old English 

^e-/7^s/5/7 "quarrel' {*naihstian?)\ Balto Slavic *ninkd^ begin violently ' in Lithuanian - 

ninku, -nikti6s., Latvian n/kns'angry, irate', ablaut. /75/'i^s "violent', Lithuanian dial, neikom 

"very'. Old Prussian neikauf stroll ', Slavic *nikng, *nikngti\v\ Old Church Slavic vhz-nikngti 
=== nu- ===
Root / lemma: nu- {*he- nu-) 
Meaning: now 



Material: Old Indie nu, nu, Avestan nu'novj', Old Indie nutana-' present, current, young, new', 
nunam "now, yet, present ' (as Lithuanian nunal Old Church Slavic /7y/7e probably adv. 
solidified case of the Adj. *A7t7-/7c»- "present, current'), Avestan nuram, nurqm, ap. nuram6s. 
(shaped after aparem " from here on, hereafter '?); gr. vu, vuv, vuv "now, yet' (latter probably 
from *nu-m =) Latin num " nun noch, noch jetzt ', then base for questions, etiamnum " even 
now| stilll yet', nunc' now| todayl at present' {*num-ce) = Hittite k/'-nun ds., nu-per' recently! not 
long ago; in recent years/our own time; (SUPER) latest in series ', next to which nu- still in nu-dius 
tertius^* now is the third day ' (about Old Irish nu-, no-, mcymr. /7e^ Verbal-particle, see 
below /7e"not'); Gothic nu{nLn), Old Icelandic Old High German Old English /7j"now, yet, 
at present ', Middle High German Modern High German nu, previously from Late Middle 
High German time also nun; Lithuanian nu, Latvian nu' now'. Old Prussian in tei-nu' now, 
since; henceforth, from now on, from this time on ', Lithuanian nunaPnow' (see above); Old 
Bulgarian nb " yet ', nyne' now' (see above); Tocharian A nuB no enk\. " yet, because'; 
Hittite /7i/ (sentence-prefatory particle); k/-nun 'now, yet', nu-wa 'stWV, nu-kwit' numquid '; 
Gothic nauh'sWW, Old Frisian noch. Old Saxon Old High German noh Adverb "still, also 
now, yet' from *nu-k"e; about the conjunction " neither ... nor ' see above S. 757 under ne1. 

Indo Germanic nu\s probably zero grade to neuo- "new', compare Old Indie nutane- 
"present, current' and "new', gr. vsov ti " just, recently ', Old High German niwes {ady. Gen.), 
Lithuanian naujafiresh, recently '. 

Maybe alb. ta-ni'now' [ta- {a-te) "this, that' + */7/"now'] : Old Prussian in tei-nu: Skt. nu 

"now, just, but' [adv]; Go. nu'now' [adv] 

References: WP. II 340, WH. II 186 ff., Trautmann 201. 

Page(s): 770 

Root / lemma: od'^os, pd^eri{*he- pd^os) 

Meaning: under 

Material: Old Indie adhah ' under' (as preposition m. Akk. and Gen.), Avestan ado'under', 

Armenian dnd{rr\. Instr.) "under'. Old Icelandic undds., Tocharian A ahc'under, downwards,
```


## [2026-09-07T19:30:22.188Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"newo-\\|^nu-\\|nu-\\. Now\" AHD_watkins1985.txt | head; echo ===; sed -n '786,792p' AHD_watkins1985.txt | cut -c1-3000"
}
```


### [2026-09-07T19:30:22.248Z] TOOL RESULT

```
Exit code 1
123:A number of qualitative adjectives are at- tested that go back to the protolanguage. Some come in semantic pairs: sen-', “old,” and newo-, “new”; also sen-', “old,” and yeu-, “youthful vigor”; *tenu-, “thin” (under ten-), and tegu-, “thick”; g”era-?, “heavy,” and leg"h-, “light.” There are also the two prefixes su-, “good, well-,” and dus-, “bad, ill-,” in the Greek forms borrowed as EU- and pDys-. But normally adjectives of value judg- ments like good and bad are not widespread in the family and are subject to replacement; English good, Latin bonus, and Greek aga- thos have nothing to do with each other, and each is confined to its own branch of the family.
787:animal: NEAT2; b. compound form *ga-nauta- (*ga-, with, together; see kom), “he with whom one shares possessions,” companion, fellow, in (i) Middle Dutch ghenét, noot, fellow: MATELOTE (ii) Old High German ginéz, companion, in German Eidgenosse, confederate: HuGuEnot. [Pok. neu-d- 768.] newn. Nine. 1. Germanic *niwun, with variant *nigun, in Old English nigon, nine: NINE, NINETEEN, NINETY, NINTH. 2. Latin novem, nine (< *noven, with m for n by analogy with the m of septem, seven, and decem, ten): NOVEMBER, NOVENA; NONAGENARIAN. 3. Ordinal form *neweno- in Latin nénus, ninth: NONA-, NONES, NOON; (NONAGON), (NONANOIC ACID). 4. Prothetic forms *enewn, *enwn in Greek ennea, nine (> *ennewa, *enwa-): ENNEAD. [Pok. e-neuen 318.] newo-. New. Related to nu-. 1. Suffixed form *new-yo- in Germanic *neuja- in: a. Old English néowe, niwe, new: NEw; b. Old Norse njyr, new: SPAN-NEW. 2. Basic form *newo- in Greek newos, neos, new: NEO-, NEON, NEOTER- IC; MISONEISM. 3. Suffixed form “new-aro- in Greek nearos, young, fresh, contracted into néros, fresh (used of fish and of water), hence néron, water: ANEROID. 4. Basic form *newo- in Latin novus, new: NOVA, NOVATION, NOVEL!, NOVEL?, (NOVELTY), NOVICE; INNOVATE, REN- OVATE. 5. Suffixed form *new-er-ko- in Latin noverca, stepmother (< “she who is new”): NOVERCAL. [Pok. neuos 709.] ni. Down. 1. Suffixed form *ni-t- in Germanic *nith- in Old English nithan, neothan, below: BENEATH, UNDER- NEATH. 2. Suffixed (comparative) form *ni-tero-, lower, in Germanic *nitheraz in Old English nither, lower: NETHER. See compound root nizdo-. [In Pok. 1. en 311.] [niké. Victory. Greek noun of unknown origin. NIKE.] nizdo-. Bird’s nest. Compound root formed from ni + *sd-, zd-, zero-grade form of sed-; literally, “place where the bird sits down.” 1. Germanic *nist- in: a. Old English nest, nest: NEST; b. Germanic ‘*nistilon in Old English nestlian, to make a nest: NESTLE. 2. Latin nidus, nest: NICHE, NIDE, NIDUS; EYAS, NIDIFY. [In Pok. sed- 887.] nobh-. Also ombh-. Navel; later also “central knob,” boss of a shield, hub of a wheel. 1. Germanic *nabo in: a. Old English nafu, nafa, hub of a wheel: NAVE?; b. compound *nabé-gaizaz, tool for piercing wheel hubs (*gaizaz, spear, piercing tool; see ghaiso-), in Old Eng- lish nafogar, auger: AUGER. 2. Variant form *ombh- in Latin umbé, boss of a shield: uMBO. 3. Suffixed form *nobh-alo- in Germanic *nabalé in Old English nafela, navel: NAVEL. 4. Suffixed variant form *ombh-alo- in: a. Latin umbilicus, navel: UMBILICUS; NOMBRIL; b. Greek omphalos, navel: OMPHALOS. [Pok. 1. (enebh-) 314.] nogh-. Also enogh-, ongh-. Nail, claw. 1. Suffixed (diminutive) form *nogh-ela- in Germanic *nagla- in Old English negl, nail: NAIL. 2. Form *onogh- in Greek onux (stem onukh-), nail: ONYX; PARONYCHIA, PERIONYCHIUM, SARDONYX. 3. Variant form *ongh- in Latin unguis, nail, claw, hoof, with diminutive ungula, hoof, claw, talon (< ongh-eld-): UNGUIS. [Pok. onogh- 780.] nogv-. Naked. 1. Suffixed forms *nog’-eto-, *nog’-oto- in Germanic *nakweda-, *nakwada- in Old English nacod, naked: NAKED. 2. Suffixed form *nog~-edo- in Latin niidus, naked: NUDE, NUDI-; DENUDE. 3. Suffixed form *nog’-mo- differentiated or developed into Greek gum- nos, naked: GYMNASIUM, GYMNAST; GYMNOSOPHIST, GYMNOSPER\M. [Pok. nog¥- 769.] no-men-. Name. Earlier form *()noo-mn, zero-grade form *(g)na-men-. 1.Germanic *nam6n- in Old English nama, name: NAME. 2. Latin némen, name, reputation: NOMINAL, NOMINATE, NOUN; AGNOMEN, COGNOMEN, DENOMINATE, IGNOMINY, MISNOMER, NOMENCLATOR, NUNCUPATIVE, PRAENOMEN, (PRONOUN), RENOWN. 3. Greek onoma, onuma, name: ONOMASTIC, -ONYM, -ONYMY; ANONYMOUS, ANTONOMASIA, EPONYM, (EPON- YMOUS), EUONYMUS, HETERONYMOUS, HOMONYMOUS,
792:eal Latin énsis, sword: ENSIFORM. [Pok. nsi-s (ids nu-. Now. Related to newo-. 1. Old English ni, now: Now. 2. Latin nunc (< *nun-ce; -ce, a particle meaning “this,” “here”; see ko-), now: QUIDNUNC. [Pok. nu- 770.]
1245:-ANDRY ner-2 ANECDOTE d6- ANELE elaia ANEMO- ane- ANEROID newo- ANESTHESIA au-5 ANEURYSM were-! ANFRACTUOUS bhreg- ANGARY angelos ANGEL angelos ANGELIC angelos ANGELICA angelos ANGELUS angelos ANGER angh- ANGINA angh- ANGLE! = ank- ANGLE? §ank- ANGLE ank- ANGST angh- ANGUILLIFORM ang¥hi- ANGUINE ang¥hi- ANGUISH angh- ANHYDROUS wed-! ANIL nei-
1679:INNATE gene- INNER en INNOCENT nek=! INNOCUOUS_nek-1 INNOVATE newo- INNUENDO neu-2 INOCULATE okw- INORDINATE ar- INOSCULATE 6s- INOSITOL wei-1 INOTROPIC wei- INQUILINE kWel-1
1875:MIR mei-4 MIRACLE smei- MIRAGE smei- MIRE meu- MIRROR smei- MIRTH mregh-u- MIs-1_ mei-1, mei-2 MISADVENTURE gWa- MISANTHROPE ner-2 MISCEGENATION gene-, meik- MISCELLANEOUS meik- MISCHIEF kaput MISCIBLE meik- MISCREANT kerd-1 MISER miser MISERABLE miser MISERICORD kerd-1 MISERY miser MISFEASANCE dhé-1 MISHAP kob- MISNOMER nd-men- MISONEISM newo- MISPRISION ghend-, mei-1 MIss! mei-1 MISSEL THRUSH meigh- MISSILE (s)meit(9)- MISSION (s)meit(a)- MISSIVE (s)meit(e)- MIST meigh- MISTAKE mei-1 MISTER meg- MISTLETOE meigh- MISTRAL meg- MISTRESS meg- MITE! = mai-1
1908:NEED nau-! NEEDLE (s)né- NEFARIOUS dhé-1, ne NEGATE ne NEGLECT leg-1, ne NEGLIGEE ne NEGOTIATE ne NEGRO negW-ro- NEIGHBOR bheue-, néhw-iz NEITHER kWo-, ne NEKTON sna- NEMATO- (s)né- NEMESIS nem- NEO- newo- NEOGAEA gé@ NEON newo- NEONATE gene- NEOPHYTE bheue- NEOTERIC newo- NEPENTHE kWent(h)-, ne NEPHELINE nebh- NEPHELOMETER nebh- NEPHEW nepdot- NEPHOLOGY nebh- NEPHRO- negWh-ro- NEPOTISM nepot- NEREID nere- NEREIS nere- NEREUS nere- NERITIC nere- NERVE (s)neou- NESCIENCE ne, skei- NESS nas-
1912:NETTLE ned- NEURILEMMA wel-3 NEURO- (s)nee@u- NEUROGLIA gel-1 NEURON (s)neeu- NEUTER kWo-, ne NEVE sneigh- NEVER aiw-, ne NEW newo- NEWEL ken-5 NEXT néhw-iz NEXUS ned-
1938:NOVA newo- NOVACULITE kes-1 NOVATION newo- NOVEL! newo- NOVEL? newo- NOVELTY newo- NOVEMBER newn NOVENA newn NOVERCAL newo- NOVICE newo- NOW nu-
2178:REIGN reg-! REIMBURSE bursa REINDEER dheu-1, ker-1 REINFORCE bhergh-2 REITERATE i- REJECT yé- REJOICE gau- REJUVENATE yeu- RELAPSE leb-! RELATE tele- RELAX slég- RELAY slég- RELEGATE leg-1 RELENT lento- RELIEVE leg¥h- RELINQUISH leikw- RELUCENT leuk- RELUCT leug-! RELY leig-1 REMAIN men-3 REMAND man-2 REMARK merg- REMEDY med- REMEMBER (s)mer-! REMEX ere-! REMINISCENT men-! REMIT (s)meit(a)- REMORA mere- REMORSE mer-2 REMOTE meue- REMOVE meue- REMUDA mei-1 REMUNERATE mei-! RENAISSANCE gene- REND rendh- RENDER do- _ RENDEZVOUS wOS RENEGADE ne RENEGE ne RENITENT kneigh- RENOUNCE neu-! RENOVATE newo- RENOWN no-men- RENT! do- REPAIR! pere-1 REPAND pete- REPARTEE pere-2 REPAST pa- REPEAT pet- REPEL pel-6 REPENT2 rép-1 REPERTORY pere-! REPINE kWei-1 REPLENISH pele-! REPLETE pele-1 REPLEVIN plegan REPLICATE plek- REPORT per-2 REPOSE! paus- REPOSIT apo- REPREHEND ghend- REPRESENT e@S- REPRESS per-5 REPRIMAND per-5 REPRISAL ghend- REPRISE ghend- REPROACH pert REPROVE per? REPTILE rép-1 REPUBLIC ré- REPUDIATE (s)peud- REPUGN peuk- REPUTE peu-
(eval):1: == not found
```


## [2026-09-07T19:30:31.391Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"^new, adj\\|^new,\\|^now, adv\\|^now,\\|^neo-\\|^neon,\" KLN_1966.txt | head -20; echo \"=== leaf check ===\"; python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(len(t))\nfor i in (539,540,541,542):\n    print('---leaf',i, t[i][:200].replace('\\n',' | '))\nEOF"
}
```


### [2026-09-07T19:30:32.884Z] TOOL RESULT

```
25205:neo-,  combining  form  meaning  ‘new,  recent’.  — Gk.  veo-,  fr.  vioc,,  ‘new’,  for  *ver og,  fr.  I.-E. •newos,  ‘new’,  whence  also  Goth,  niujis,  OE. neowe,  ‘new’.  See  new  and  cp.  neon,  neoteric, Nerium,  the  first  element  in  neossine  and  the second  element  in  misoneist.
25217:neon,  n.,  name  of  a  gaseous  element  (chem.)  — ModL.,  lit.  ‘the  new  (element)’,  fr.  Gk.  veov. neut.  of  veo?,  new’  (see  neo-);  coined  by  the discoverers  of  this  element,  the  Scottish  chemist Sir  William  Ramsay  (1852-1916)  and  the  Eng¬ lish  chemist  Morris  William  Travers  (1872-1961) in  1898.  Cp.  krypton,  xenon.
25358:new,  adj.  —  ME.  newe,  new,  fr.  OE.  niwe,  neowe, rel.  to  OS.  niuwi,  niwi,  OFris.  nie,  MDu.  nieuwe, nuwe,  nie,  Du.  nieuw,  OHG.  niuwi,  MHG.  niuwe, G.  neu,  ON.  nyr,  Dan.,  Swed.,  Norw.  ny,  Goth. niujis,  ‘new’,  fr.  Teut.  base  *neuja-,  correspond¬ ing  to  l.-E.  base  *newo-,  *newio-,  *nowio-, whence  OI.  ndvah,  navyah,  Avestic  nava-,  Mod- Pers.  nau,  Toch.  A  hu,  B  h(u)we,  Hitt,  newash. Arm.  nor  (gen.  noroy),  Gk.  veo?  (for  *ve.Foc), ‘new’,  ve'xpoc (for*vEfotpo^),  ‘youthful  ,  L.  novus, OSlav.  novu,  OPruss.  neuwenen,  Lith.  naujas, Gaul,  novio-,  nevio-,  Olr.  nue,  W.  newydd,  Bret. newez,  ‘new’.  Cp.  now,  Neustria  and  the  first element  in  Newton.  Cp.  also  neo-,  nova,  novel, novercal,  novice,  nuncio,  innovate,  renovate.
=== leaf check ===
903
---leaf 539 he  family  Nymphalidae  ( entomol .)  — ModL.,  fr.  Gk.  Mopipci.  See  prec.  word, morpho-,  before  a  vowel  morph-,  combining  form meaning  ‘form,  shape’.  —  Gk.  p-opipo-,  [iopip-, fr.  [
---leaf 540 odHeb.  mdshdbhah,  a  fem.  noun formed  from  the  masc.  noun  moshdbh.  See  prec. word. | Moslem,  n.,  a  Mohammedan.  —  Arab,  muslim, | ‘a  believer  in  Islam’,  lit.  ‘one  who  has  submitted 
---leaf 541 adj.  —  See  moldy. | moulin,  n.,  a  nearly  vertical  shaft  in  a  glacier formed  by  surface  water  falling  through  a  crack in  the  ice  ( geol .)  —  F.,  lit.  ‘a  mill’,  fr.  Late  L. mo
---leaf 542 ing  mucin  (biochem.)  —  Coined  fr.  mucin  and -oid.  See  prec.  word. | Mucor,  n.,  a  genus  of  molds  (bot.)  —  ModL.,  fr.  L. mucor,  ‘mold,  moldiness',  rel.  to  mucere,  ‘to  be moldy
```


## [2026-09-07T19:30:39.657Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nfor kw in ['new,  adj.  —  ME.  newe','neo-,  combining  form','neon,  n.,  name  of  a  gaseous']:\n    i=t.find(kw); print(kw[:20],'leaf',t.count('\\f',0,i))\n# find 'now, adv'\nimport re\nfor m in re.finditer(r'now,\\s+adv',t):\n    print('now adv at leaf',t.count('\\f',0,m.start()), t[m.start():m.start()+400].replace('\\n',' '))\n    break\nEOF"
}
```


### [2026-09-07T19:30:41.051Z] TOOL RESULT

```
new,  adj.  —  ME.   leaf 559
neo-,  combining  fo leaf 87
neon,  n.,  name  of leaf 556
now adv at leaf 566 now,  adv.  —  ME.  nou,  nu,  fr.  OE.  /til,  rel.  to  ON. nu,  Dan.,  Swed.,  Du.  nu,  OS.,  OFris.  nu,  nu, OHG.,  MHG.  nu,  nu,  G.  nun,  Goth,  nu,  ‘now’, and  cogn.  with  OI.  nu,  nu,  nitnam,  Avestic  nil, OPers.  nuram,  Toch.  nu,  Hitt,  nuwa,  ‘now’,  Gk. vu,  vuv,  L.  nunc,  OSlav.  nyne,  Lith.  nu,  ‘now’, OIr.  nu-,  no-  (presential  pref.).  The  original meaning  of  t
```


## [2026-09-07T19:30:55.505Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in range(553,570):\n    nums=re.findall(r'\\b1[01]\\d\\d\\b',t[i])\n    head=t[i].strip().split('\\n')[0][:60]\n    print(i, nums[:6],'|',head)\nEOF"
}
```


### [2026-09-07T19:30:56.796Z] TOOL RESULT

```
553 ['1034', '1035'] | d  of  navis,  ‘ship’,  and agere,  ‘to  set  in  motion,  d
554 ['1036'] | n.,  that  part  of  the  body  which  joins  the head  to  
555 ['1039'] | MF.  (=  F.)  negatif  (fern. negative),  fr.  OF.  negatif,
556 ['1040'] | for  *ver og,  fr.  I.-E. •newos,  ‘new’,  whence  also  Got
557 [] | .  ve< pp4c,  ‘kidney’  (see  ne¬ phro-),  and  suff.  -it, 
558 [] | �blessed’.  See  nostal¬ gia.
559 ['1046'] | corpuscles  that is  neither  oxyphile  nor  basophile');  a
560 [] | s  (in  a  certain  manner); one  who  deals  (with  a  cert
561 [] | �.
562 [] | niter, nitro,  adj.,  containing  nitrogen.  —  From  nitro-
563 [] | See  nodule  and  -ous. nodus,  n.,  knot;  difficulty,  com
564 ['1054', '1066'] | before  the  ides’,  and  cp. words  there  referred  to.
565 ['1056', '1057'] | orman-ize,  intr. and  tr.  v.,  Norman-iz-ation,  n.
566 ['1058', '1059'] | Sir  Richard  Owen  (1804-92)  in  1848  fr. vcoxo.;  (also 
567 ['1080', '1060', '1061'] | alpha¬ bet. —  Gk.  vu,  shortened  fr.  Heb.  nun,  name  o
568 ['1062', '1063'] | numeralis,  ‘of  numbers’,  fr.  L.  numerus. See  number,  
569 ['1064'] | ), contraction  of  *noven-dinom,  ‘nine  days’,  fr. novem,
```


## [2026-09-07T19:31:07.547Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\ni=t.find('now,  adv')\nprint(t[i:i+900])\nprint('=== nova/novel ===')\nfor kw in ['nova,  n.','novel,  adj','novice,  n','innovate','renovate']:\n    j=t.find(kw)\n    print('\\n>>',kw, t[j:j+420].replace('\\n',' ') if j>0 else 'NOT FOUND')\nEOF"
}
```


### [2026-09-07T19:31:09.033Z] TOOL RESULT

```
now,  adv.  —  ME.  nou,  nu,  fr.  OE.  /til,  rel.  to  ON. nu,  Dan.,  Swed.,  Du.  nu,  OS.,  OFris.  nu,  nu, OHG.,  MHG.  nu,  nu,  G.  nun,  Goth,  nu,  ‘now’, and  cogn.  with  OI.  nu,  nu,  nitnam,  Avestic  nil, OPers.  nuram,  Toch.  nu,  Hitt,  nuwa,  ‘now’,  Gk. vu,  vuv,  L.  nunc,  OSlav.  nyne,  Lith.  nu,  ‘now’, OIr.  nu-,  no-  (presential  pref.).  The  original meaning  of  these  words  was  ‘newly,  recently’. They  derive  fr.  I.-E.  base  *nu,  which  is  rel.  to base  *newo-,  ‘new’.  See  new.
Derivatives:  now,  conj.  and  n. nowadays,  adv.,  at  the  present  time,  in  these times. — Compounded  of  now,  pref.  a-,  used  in the  sense  of ‘on’,  and  adv.  gen.  day's. nowel,  n.,  1)  newel;  2)  core  of  a  mold  for  casting large  hollow  objects.  —  A  var.  of  newel.
Nowel,  n.  —  A  var.  of  Noel, nowhere,  adv.,  —  ME.  nowher,  fr.  OE.
=== nova/novel ===

>> nova,  n. nova,  n.,  a  new  star  that  appears  suddenly  and then  grows  fainter  gradually  ( astron .) —  ModL., short  for  L.  nova  Stella,  ‘a  new  star’;  fern,  of novus,  ‘new’.  See  new  and  cp.  novel,  adj. novaculite,  n.,  a  hard  slate  used  for  whetstones {mineral.)  —  Formed  with  subst.  suff.  -ite  fr.  L. novacula,  ‘a  sharp  knife,  a  razor’,  a  noun  formed with  instrumental  suff.  -cul

>> novel,  adj novel,  adj.,  and verbal  suff.  -ate. Derivatives:  innovation  (q.v.),  innovat-ive,  in- novat-ory,  adjs. innovation,  n.  —  L.  innovatio,  gen.  -dnis,  fr.  in- novatus,  pp.  of  innovare.  Sec  prec.  word  and -ion. innoxious,  adj.,  harmless.  —  L.  innoxius,  ‘harm¬ less;  blameless,  innocent’,  fr.  in-,  ‘not’,  and noxius,  ‘harmful’.  See  noxious  and  cp.  innocent. Derivatives :  innoxious-Iy,

>> novice,  n novice,  nuncio,  innovate,  renovate. IU44 Derivatives:  new-ish,  adj.,  new-ly ,  adv.,  new¬ ness,  n. newberyite,  n.,  a  hydrated  magnesium  phosphate (mineral.)  —  Named  after  J.  Cosmo  Newhery  of Melbourne.  For  the  ending  see  subst.  suff.  -ite. newel,  n.,  1)  a  pillar  from  which  the  steps  of  a winding  stair  radiate;  2)  the  post  at  the  top  or bottom  of  a  stair.  —  ME.  nowel

>> innovate innovate,  intr.  v.  —  L.  innovatus,  pp.  of  innovare, ‘to  renew,  alter’,  fr.  in-,  ‘in’,  and  novare,  ‘to make  new’,  fr.  novus,  ‘new’.  See  novel,  adj.,  and verbal  suff.  -ate. Derivatives:  innovation  (q.v.),  innovat-ive,  in- novat-ory,  adjs. innovation,  n.  —  L.  innovatio,  gen.  -dnis,  fr.  in- novatus,  pp.  of  innovare.  Sec  prec.  word  and -ion. innoxious,  adj.,  harmless.  —  L.

>> renovate renovate. IU44 Derivatives:  new-ish,  adj.,  new-ly ,  adv.,  new¬ ness,  n. newberyite,  n.,  a  hydrated  magnesium  phosphate (mineral.)  —  Named  after  J.  Cosmo  Newhery  of Melbourne.  For  the  ending  see  subst.  suff.  -ite. newel,  n.,  1)  a  pillar  from  which  the  steps  of  a winding  stair  radiate;  2)  the  post  at  the  top  or bottom  of  a  stair.  —  ME.  nowell,  fr.  OF.  nouel, noiel  (
```


## [2026-09-07T19:31:17.724Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"nūram\\|nuram\\|n[uū]ram\" KNT.txt | head -20; echo \"=== leaf for p194 = 209 ===\"; python3 - <<'EOF'\nt=open('KNT.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(len(t))\nfor i in (208,209,210):\n    print('---leaf',i)\n    print(t[i][:1500])\nEOF"
}
```


### [2026-09-07T19:31:18.973Z] TOOL RESULT

```
=== leaf for p194 = 209 ===
232
---leaf 208
 Skt. jū- ‘press for- ward, impel quickly, excite, promote’, pres. jdvate ‘hastens’, caus. javayati. Cf. Ву. BSLP 332.152; Hz. AMI 4.127, 8.37-8, 65-6, ApI 366-7; Wb. МА 41.8320; Bailey, BSOS 7.292-4; Schaeder SbPAW 1935.502; Kent, Lg. 9.43, 231.
abi- + jav- caus. ‘promote, increase, add to’: abiyajüvayam 1st sg. imf. ($215) XPg 9; abijáva- yam (§23.1, $140.IIT) XPf 40.
jtyamna- pte. as adj. ‘growing old’, nt. as sb. ‘end’ ($109, $241): Av. Jyamna-, pte. to root }уй- ‘grow weak’, Skt. jinåti ‘grows old’. jiyamnam asn. DB 2.62.
ji- vb. ‘live’: Av. fait: (gay-, Bthl. AiW 502), Skt. Джай, Lt. vivit, pIE *g*īųeti (§216); see also gaiéd-, jiva-. ajivatam 3d du. imf. ($229) DSf 14; XPf 21. jwà 2d sg. imv. ($2371) DB 4.56, 75.
jiva- ad). ‘living’: Av. fva-, Skt. jivd-, Lt. vivos, pIE *g*iuo-, cf. *g*iuo- in Gk. Blos "life", *g*ig*o- in OEng. cwicu "living, NEng. quick (8101, $114, $150). See also 7й-. Jiva nsm. XPh 48, 54. jva-diy Аза 3 (dubious $22, 555.1; ef. JAOS 51.229, Scheil 21.93, Wb. AfOF 7.45). jivahya gsm. DB 5.19f, 35.
jü- vb., see jav-.
-{а- encl, demonst. pron. ‘this, it’: Av. Skt. ta-, ef. OP tya-. Only -tā apm., referring to patikarā,
185
in avabasa-a DB 4.72 (8133, $196; JAOS 62.272- 3).
{аита- sb. ‘family’ (8149.1): Av. taoxman-, NPers. tuzm, Skt. tokd-m ‘offspring’, tókman- tokma-s ‘young blade of barley’; -zm- became OP -hm- (5103.1, 5118.1), but remained in Med. (Ву. BSLP 31.2.76-9, Gr. $188; wrongly Mt. Gr. §75, Kent JAOS 35.329-31). taumd nsf. DB 1.8; 4.56, 58f
---leaf 209
it (§76.V, 5148.1). Cf. Gray, AJP 58.67; Hz. Klio 8.51, AMI 2.77; Hinz, ZDMG 95.227. lacaram asm. DPa 6; АР]. dacaram ($494) рва 3.
tanii- sb. ‘body, self’ (8$153.IT) Ау. tand-, Skt. tani-; cf. Debrunner, IF 52.136. Decl., 51831. lanüs nsf. DNb 33. lanüm asf. XPf 31.
| tar- vb. ‘cross over’: Av. tar-, Skt. tdratz, caus. türáyalt, Lt. trans pte. as prep. ‘across’, cf. NEng. through. See also fara. vi- + tar- ‘go across’, caus. ‘put across’: viya- larayam Ist sg. imf. (§215) DB 5.24f. viyatarayd- mā lst pl. imf. (5230.1) DB 1.88.
fara prep. with aec. ‘through’: Av. tarō, NPers. tär, Skt. ards; formed on root tar- (q.v.) similarly to para (q.v.). іста] DZe 12.
Táravà- sb. ‘Tarava’, a town in Persia; Elam. -F-ra-ü-ma, АКК. ta-ar-ma-. Тато nsf. DB 3.22.
larsa- pres. stem. of vb. ‘fear’, with Ласа + abl.: Av. tarasaiti, NPers. térsé5, pIE "is-ske-ti (831, $97, $212), ef. pIE *tres- in Skt. trdsati, Gk. тре, also *trem- *trep- in Lt. tremit ‘trembles (with fear)’, trepidus ‘agitated (with fear). Jarsatiy ($228.1) DPd 11f. iarsa"tiy 3d pl. (§232.1) DSe 38f. alarsa imf. DB 1.50f. atarsa” 3d pl. imf. (5232.0) DB 2.12°; DPe 9. tarsam 1st sg. inj. (8224, 5237) DPe 21.
tav- vb. ‘be strong’: Av. tav-, Skt. tu-, ef. Gk. ravpos ‘bull’, Lt. taurus. See also ulava-, tauman-, lawiyah-, lunuvat- (but cf. Hz. ApI 328-33). {йгауай ($122, 8123.2, $215) DNb 33f. atávayam Ist sg. imf. (5215) DNb 47.
taš- vb., see under tazš-; in ustafanà-.
Tigra- sb. ‘Tigra’, a fortress іп Armenia: Elam. ti-ig-ra ($1
---leaf 210
1) XPh 23.
tyam asi. DB 4.70f; DPd 7. tya as asf. (856.V) AmH 5; AsH 13°. tyà npf. DB 1.13, 18; 2.6; 4.33; DPe 9, 14f; DSf 45. tyaiy as npf. (§258.1V) = XPh 31. рё apf. DPe 7; DNa 17, 40; DSe 16. . tyaišām gpf. DSm 6°; XPh 15.
tya nsn. (M0) DB 1.27, 61, 67; 2.91; 3.10, 20, 58, 76; 4.1f, 42, 49°, 53; DNa 48; DNb 2, 11, 29, 54, 56; DSe 31, 43; DSf 36; DS} 5^; D8n 2^; DZe 9, 10; XPa 19; XPb 23; ХРЇ 26, 37, 46; XPg 4; XPh 42; XV 19; AjPa 26. tya-sém DB 1.19; DNa 20; DSe 19°; XPh 17. tya-maiy DNb 48; DSe 52°; DSf 19°; DSs 7^; XPa 19f; XPb 24, 30; XPe 13 bis; XPd 19; XPf 38, 47; X8e 5°; XV 27°; A!Pa 24°; A?He 20. tya-taiy DNb 58. tya-patiy XPa 15. (ya asn. DB 1.44, 72; 4.3, 40, 59, 75, 79; 5.2; DPh 4; DNb 22, 24; DSa 4; DSf 20f, 22°; рө) 2°, 4; DSI 3; DH 3; XPa 14, 15; XPf 41; XPh 43, 49, 52; A’Sa 5^; А4 3; А?На 7. [tya]- ат DNa 36f. tya-maiy DPh 8; DH 6. tya-patiy XPf 40f. {уала isn. DSf 42. {уй npn. in tyã- maiy DNb 13. tyä apn. DB 1.64; DNb 46, 49. tyā-diš DB 1.65.
(2) Def. art., ‘the’: ат asm. DB 1.50, 54, 57, . T8, 89, 95; 2.21, 25f, 35, 41, 46, 55, 61, 69, 87, 97^; 3.7, 18, 38, 46, 625, 67f; 481; DSe 39. tyam- iim DB 5.12".
іуйт asf. DB 1.69, 71; 4.87; DNa 59. tya as asf. ($56. V) AsH 9, A’Sc 6. tyaisám gpf. DPe 3f.
tya nsn. DNa 21; DSe 20°, 38; XPh 19. tya asn. DB 1.81; DSf 11 his; DSm 4° bis; DSp 2°, 8°; DZc 4 bis. tyanā isn. DB 1.23.
(3) Demonst. pron., ‘this’: буй ndm. DSf 14. шай apm. DB 3.73.
уа. conj. ‘that’, nt. sg. of preceding; cf.
similar uses of Gk. öre, Lt. quod,
```


## [2026-09-07T19:31:26.917Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"adv\\. ‘now’\\|‘now’\" KNT.txt | head; echo ===; python3 - <<'EOF'\nt=open('KNT.txt',encoding='utf-8',errors='replace').read().split('\\f')\nimport re\nfor i in range(212,222):\n    m=re.findall(r'\\b1[89]\\d\\b',t[i])\n    print('--leaf',i,m[:5],'|',t[i][:120].replace('\\n',' '))\nEOF"
}
```


### [2026-09-07T19:31:28.139Z] TOOL RESULT

```
Exit code 1
5615:nüram adv. ‘now’: Av. nürom; from pIE *ná ‘now’ (Av. nū, Skt. пй, Lt. nu-nc, NEng. now) + final of (pAr.) *düram ‘long’ (§148.1), cf. düraty. DB 4.53.
(eval):1: == not found
```


## [2026-09-07T19:31:31.985Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\ni=t.find('nüram adv')\nleaf=t.count('\\f',0,i)\nprint('leaf',leaf)\nimport re\nblk=t.split('\\f')[leaf]\nprint(re.findall(r'\\b\\d{3}\\b',blk)[:20])\nprint(blk[max(0,blk.find('nüram')-600):blk.find('nüram')+400])\nEOF"
}
```


### [2026-09-07T19:31:33.167Z] TOOL RESULT

```
leaf 217
['142', '142', '144', '269', '142', '185', '120', '136', '140', '191', '152', '268', '194', '146', '522', '130', '138', '148', '122', '151']
.1V). тарайту adv. DB 2.73; prep. with acc. DB 3.73.
nipisti- sb. ‘impression’: deriv. of ni- + paid- ($152.11).  [niplisftiya] Isf DB. 4.90 (conj. of Kent, JAOS 62.268).
194 OLD PERSIAN
niydka- sb. ‘grandfather’: Av. nyáka- ($146.- HI); ef. apaniyüka-. {nilyaka nom. DSI 13; [n*yd|kama (522; for -Кат-тату, $41, §52.1, $130, $138.I) asm. A’Sa 4.
niyaSadayam, see had-.
Nisdya- sb. ‘Nisaya’, a district in Media: Elam. nu-is-fa-ja, Akk. ni-is-sa-a-a (5116). Per- haps from ni- ‘down’ + sdya-, to root Av. st- say- Tie’, Skt. §-, Gk. кт. ‘Ties’, pIE *kei-. Nisdya nsm. DB 1.58. |
niXadayam, see had-.
nüram adv. ‘now’: Av. nürom; from pIE *ná ‘now’ (Av. nū, Skt. пй, Lt. nu-nc, NEng. now) + final of (pAr.) *düram ‘long’ (§148.1), cf. düraty. DB 4.53.
pä- vb. ‘protect’: Av. pà-, pres. рйи, РЫ. pátan, Skt. pà-, pres. pati (ablaut, §122). See also zíacapüvan-. apayaiy lst sg. imf. mid. (Ву. BSLP 33.2.151-2; Kent, Lg. 9.42; S71, $214, $233.1II; wrongly to Skt. pt- ‘swell’, Wb. ЖА 41.820-1) XPf 39. p
```


## [2026-09-07T19:31:39.859Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"^neu̯os\\|^neuos\\|^neṷos\\|^neu̯o\\|^nū\\b\\|^nu \\|^nū \" IEC.txt | head -20; echo \"=== search new gloss ===\"; grep -n \"'new'\\|“new”\" IEC.txt | sed -n 1,20p"
}
```


### [2026-09-07T19:31:39.937Z] TOOL RESULT

```
11717:neuosí-, see neuos and next Gk. cf. neosti ‘newly’; Olr. nós, m. ‘new custom, innovation’; Ir. nús, núas, nuadhas, m. ‘newness’; OCS novosti, f. ‘newness’; R novosti, fpl. ‘news’
11730:neuos (neuios, neuiios) ‘new’. (The iotaciz- ed forms are of comparative origin. Cf. nu, nün, neuáio, etc) WP II, 324 Skt. navah, navyab, naviyah ‘new, young, fresh’; Av. navo, id. Per. nau, id.; Oss. (dim. type) náwág, nwog, nog, id. beside nàw, Dig. näwä ‘newly turned land’; Tokh. ñu, B ñuwe ‘new’; Arm. nor, o-st., id. beside nori, gs norvo, ab. s. noreav (“precocious', fr. *neuio-); Hitt. newas, id.; Myc. newos, Gk. néos & neios, id.; Lat. novus; Praenestian nouios; Osc. nuv-; Lat. cf. also the name Novius; Olr. nue, nuie, nuae, nawe; Ir. nua, nuadh, nuaidhe, id. cf. naoidhe, mf ‘baby’; Gaul. (in names) Nevio-; OBr. niguid and -neuid (in a cpd.), id.; Br. névez, W newydd, Cor. noweth, id.; Go. niujis; OHG niuwi; OE niwe; Du. niewe; OFris. nie, Fris. nij; ON nyr, obl. nyj-; cpds. ny-; Norw. Sw. ny; OCS (and com. Sl.) novú; OLi. navas, Li. naujas, id. (the iota- cized forms derive from an earlier compara- tive). Adverbial forms: Gk. néon; Pol. nowo ‘newly’; Cf. also Lat. nuntio, äre “announce”, if from *neuom-guetio. See guet-)
=== search new gloss ===
```


## [2026-09-07T19:31:45.676Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport re\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\ni=t.find('neuos (neuios')\nleaf=t.count('\\f',0,i); print('neuos leaf',leaf)\npages=t.split('\\f')\nfor j in range(leaf-3,leaf+4):\n    print(j, re.findall(r'\\b8\\d\\d\\b',pages[j])[:8])\nEOF"
}
```


### [2026-09-07T19:31:47.124Z] TOOL RESULT

```
neuos leaf 471
468 ['838']
469 ['839', '840']
470 ['841', '842']
471 ['843', '844']
472 ['845', '846']
473 ['847', '848']
474 ['849', '850']
```


## [2026-09-07T19:31:52.441Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport re\npages=open('IEC.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor j in (470,476,477):\n    print('======== leaf',j, re.findall(r'\\b8\\d\\d\\b',pages[j])[:6])\n    print(pages[j][:2600])\nEOF"
}
```


### [2026-09-07T19:31:53.635Z] TOOL RESULT

```
======== leaf 470 ['841', '842']
an ‘search; attack’; ON nysa, v. ‘pry? beside njósna, v. ‘spy out, ferret out; R njüxat, Pol. niuchac, Srb. njüsiti, inf. ‘sniff, scent; Srb. njuh, m. *smell, scent
neuqu- (?) OHG niuwan, v. ‘crush, poung’; OCS njukati, inf. ‘exhort: (isophonic in Li. niaukiu, ti ‘cloud over; niauküs ‘overcast’, but cf. Li. niuksas, m. ‘jostle, bump)
neur- (nour-, nur-) ‘grim, gloomy’ Blg. njùra, mf. ‘curmudgeon, taciturn person’; Li. niaurùs ‘grim, taciturn’; niauroti, inf. ‘grow’; (o-gde in) R po-nüryj ‘grim, gloomy’;
841
po-nùriť, inf. “hang the head, look grim’; Latv. cf. nurdu, et ‘grow?
neusmn- (neusn-) ‘sign, recognition. Cf. neuuð (neuó) and neukso Gk. neüma, n. ‘nod, sign’; Lat. nümen, n. (1) "mod beside radical cernuus 'face-forward, face-downward'; cer-nuó, -nuaàre (‘hurtle for- ward’, fr. *Ker-, *Kor- “head? + *-neu-); ON cf. njósn, pl. -ir, f. ‘reconnaissance’. (The back- ground of OE néomian, v. is uncertain; que- ried: ‘resound’)
neusó ‘snuffle, sneeze’. (Variant of type neuks-, q. v.) MHG niesen, sv. 2. ‘sneeze’; R njüxat (‘sniff , ambig. neus- or neuks-); cf. also Ukr. njux, m. ‘sense of smel?
neuuó ‘nod, sign” (isophonic in some instan- ces with neuð ‘turn’, see neuo (1) below, and cf. neuos, nün Gk. neúo nod: Lat. nuo, ére, v. id.; cf. also (variant) niveo, ere (once): ‘wink’ beside con- niveo, id. Frequentative in Lat. nüto, are ‘nod’ (but also ‘totter, waver’, cf. neuo (1)). (Iso- phonic: Li. niauju, ti 'sunder)
neuaió (neueió, neuiio, neuió) “refresh, renew; turn up (land) for sowing'. Cf. neuos. Vbl. noun: neuámn Type *neuàio: Hitt. newa-(mi), id.; Gk. neáo, id.; Lat. novo, are, id. OHG niuwon, id. Type *neueio (-ieio): R nov&t, id.; Li. naujéti, inf. id. Type *neuijo, -jo: Ir. ath-nuadhaim, id. beside MIr. -nüigim, id.; MW & W ad- newyddu, inf. id.; Go. ana-niujan, id.; OE ed- niwian, id.; ON á-nyja, id.; OCS otü-novljo, -noviti, id.; Cz. ob-novit, inf. id.; (for the px. cf. Li. atnaüjinti, inf. id. A variant occurs in Phryg. or Mac. nebrízo (Cnevridzo") “prepare (soil) for sowing’. For the verbal noun cf. Gk. neóma: Lat. novamen
neuákos “novice, beginner. Cf. neuos, etc. Skt. navakab, navikah, id.; (LW fr. Skt. in Tokh. A nawak, B nawake, id.); Cz. Slovene novák, id.
neue (neue, neu, neu) ‘or, nor, and not, lest, but not, except, than’. Cf. ne, ue, áà-ue-ne, etc. Skt. no, adv. ‘not; Av. nava ‘not at all; Hitt. nawi, nawwi “not yet’; Lat. neve, neu ‘and not,
neusmn- (neusn-) — neuios (neuiios)
15
20
25
30
35
45
842
nor, lesť; cf. also non, noenu(m) (fno, not, fr. *ne-ue-ne E *ne-ge-num); Alb. cf. nuk (not, if fr. *neu-qu, but cf. ne-que); Ir. nó “
======== leaf 476 ['853', '854']
ic) ‘power; force; tyrant; (mod.) ‘obstinacy’
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
nor
======== leaf 477 ['855', '856']
d'. Cf. noudheio above. WP II, 316 Go. naups, obl. naud-, f. ‘need, force; MHG not, f. id. (and 'struggle); note, noete, adv. ‘perforce’; OE nied, f. n. as Go.; OCS nužda, f. (need? but Pol. nedza, Cz. nouze unrelat- ed). OCS oti nudí ‘forthwith’ (? here)
nřið ‘plunge’ Skt. cf. nirám, Av. nirom, n. ‘water’; Gk. cf. nár-talos, m. “a vessel; MHG noren, norn, v. ‘grovel, wallow’; OCS nro, nréti ‘dive into, enter’; Li. nyru & nirstu, inf: nirti, intr. ‘dive, plunge’; Latv. nirstu, nirt, v. id.; o-gde in Cz. notit, v. tr. *plunge, immerse'
nrt- (frenzy, wildness; frenzied, wild; be frenzied'. Skt. nrtyami, natami, pp: nartitah, v. "dance: Li. nirstu, inf: nirsti, v. ‘rage’; nirtüs ‘irascible’.
nú, nün, nūnai ‘so, now, well, then’. Cf. -peu-, -nu-. WP II, 340 Skt. nu, nū, nünam ‘now’; Av. nü, id.; Per. cf. ka-nün, ak-nün, id.; Tokh. A nu, B no “well,
855
now, so”; Hitt. nu, id. beside ki-nun (‘till now or “and now"); Gk. nün, nuni, nun, nu ‘well, now, so, then’; Cypr. nu (a sentence-link); It-Alb. ni (énow', fr. *nü) beside Alb. ta-ní, id. (cf. Scots: ‘the now); Lat. cf. nün-c ‘now’; G noch, cj. (yet, fr. *nu-qu-); OW neu, nu ‘now’; OHG nü; Go. nu; MHG nù ‘now’; ON nú, núna, OE nū, nūna, id.; OFris. nū, id.; Du. nou ‘well, soi: OCS Big. nú ‘but, yet; cf. also OCS nyné (‘now’, fr. *nünai); Li. nu, nu, nünai, id. beside nü “well, well now’; Latv. nu as Li. (Gk. nú, nún is described as a “particle of transition? by G. Curtius in "Accidence of Gk. Grammar’, 1872 as trans- lated by Wm. Smith, p. 125, § 386)
-nu-, verbal extension, see -neu- and cf. nü above Instant aspect in type *or-neu-, -nu- as in Skt. rnomi; Av. oronv-; (Arm. h-arnem: Gk. epór- nümi); Arm. arnum 'get', ostnum ('leap'. See SEM: AHGLC: pp 58-9); Gk. ornümi; Hitt.
arnumi. Factitive in Hitt. warnu(mi) *make
burn'; tepnu(mi) *make small, etc.
nud- (nudeió, nüdsko) ‘enjoy’. Cf. noud- MHG nutzen, nützen ‘use, enjoy’; OE not- ian, v. id.; nytt, f. ‘use, care’; Fris. nodzje, v. ‘hug, cuddle’; ON nytja, v. ‘milk’; nyt, pl. -jar, f. ‘use; milk’; G nutschen ‘quaff, imbibe’ beside nutzen, nützen as MHG: Li. nústu, inf: nústi, pf: núdau, v. “desire, lust after”
(nug- ‘stab’; nüg- ‘trifle, whim’ (?) See Supt: N and cf. snug-)
nün, nünai, see nü. Variants in Gk. kai nú ke; Lat. nunc; Olr. noch; Go. naüh; G noch; R nynče; Li. nu-gi, nu-jau, etc. A type *nu-per- arises in Lat. nü-per, OCS nü-pera, cj. "but
nüu- (nuu-, nu-) ‘suffering’. Cf. nàu- (2) Per. cf. navidan, inf. ‘lament’; Arm. (LW?) nvam, v. ‘lament; cf. nvay, adj. i-st. ‘frail’; nvayim, v. ‘faint’; Ir. cf. nuna, m. ‘hunger; W cf. niwed, pl. -eidiau, m.
```


## [2026-09-07T19:32:06.892Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for f in IEC.txt; do echo \"== $f\"; grep -n -i \"navid\\|nivid\\|nawid\\|niwed\\|nivēd\\|ni-uid\\|neuid\" $f | head -20; done"
}
```


### [2026-09-07T19:32:08.068Z] TOOL RESULT

```
== IEC.txt
11730:neuos (neuios, neuiios) ‘new’. (The iotaciz- ed forms are of comparative origin. Cf. nu, nün, neuáio, etc) WP II, 324 Skt. navah, navyab, naviyah ‘new, young, fresh’; Av. navo, id. Per. nau, id.; Oss. (dim. type) náwág, nwog, nog, id. beside nàw, Dig. näwä ‘newly turned land’; Tokh. ñu, B ñuwe ‘new’; Arm. nor, o-st., id. beside nori, gs norvo, ab. s. noreav (“precocious', fr. *neuio-); Hitt. newas, id.; Myc. newos, Gk. néos & neios, id.; Lat. novus; Praenestian nouios; Osc. nuv-; Lat. cf. also the name Novius; Olr. nue, nuie, nuae, nawe; Ir. nua, nuadh, nuaidhe, id. cf. naoidhe, mf ‘baby’; Gaul. (in names) Nevio-; OBr. niguid and -neuid (in a cpd.), id.; Br. névez, W newydd, Cor. noweth, id.; Go. niujis; OHG niuwi; OE niwe; Du. niewe; OFris. nie, Fris. nij; ON nyr, obl. nyj-; cpds. ny-; Norw. Sw. ny; OCS (and com. Sl.) novú; OLi. navas, Li. naujas, id. (the iota- cized forms derive from an earlier compara- tive). Adverbial forms: Gk. néon; Pol. nowo ‘newly’; Cf. also Lat. nuntio, äre “announce”, if from *neuom-guetio. See guet-)
11891:nüu- (nuu-, nu-) ‘suffering’. Cf. nàu- (2) Per. cf. navidan, inf. ‘lament’; Arm. (LW?) nvam, v. ‘lament; cf. nvay, adj. i-st. ‘frail’; nvayim, v. ‘faint’; Ir. cf. nuna, m. ‘hunger; W cf. niwed, pl. -eidiau, m. “harm? beside er-niw, pl. ion, m. id.; LG cf. nürig, adj. “hungry”; Cz. nyvy, adj. ‘languishing’; R u-nylyj, adj. ‘sad’
```


## [2026-09-07T19:32:08.781Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== PHD\"; grep -n -i \"^niw\\|niwēd\\|nēw \\|nēwag\\|nwyt\" PHD.txt | head -30; echo \"== NYB\"; grep -n -i \"nivēt\\|niw[ēe]t\\|nēvak\\|nēv \" NYB_vol2_glossary.txt | head -20"
}
```


### [2026-09-07T19:32:08.841Z] TOOL RESULT

```
== PHD
5187:niwistan winastag wanafšag winjisk nizār nizārīh nizārīh- nazd nazdikih nazdik wizend nazdist wizend wizand- wizandag
== NYB
1282:dile-nev [dly TB] 231? (2418.20), dil-nēv [dl TB] 297°. (301-5): "good of heart" = brave, gallant. — dile cas. obl. of dil, v. nev.
1585:frče [plyc] a surplus, or a remainder, a rest: martom (indir. obj.) — pat nēvakē- keh <i> hàn kunēnd i-šan andar gehän apäyisniktar veh dit to mankind they (the gods) will make a surplus above the felicity which in this world was seen by them as the most exquisite and the very best 10025-26 i. e., mankind will be given a felicity above the most exquisite and the very best felicity they experienced in this world. — Paz. fréz-, fréz- (v. next group) = BP /réc < *fraréc (haplology) < Olr *fra-raica- (from fra + ratk-, v. rertan), cf Skr prarecana- ‘surplus’, pra- reka- ‘abundance’, properly ‘what is pro- jecting’. To it belongs the vb. frčatan fréc- l. ‘to be over, to be left, after necessary expenses, as a gain or a rest’, 2. ‘to put aside what is surplus, to save’, or, ‘to increase by a surplus’. Cf (Paz.) ne neki frežašni . .. rà ‘not in order to add to the well-being’ SGV III, 24, Skr. v. subhasya visphitaye; har cé frēcēt hac all that is left of, or after BdA p. 1107 (plycyt' with the first y marked) = BdJ 397; PY 687; frčat ‘savings’ PVd. 379%. 1888 (comm.). Bthl., followed by others, read paréc- < *pari-raica-, identifying it with Sogd p’r’yc- ‘to leave, to abandon? (ZairWb 52; MIrM I, 14. II, 11.38 sq.) and adducing as a parallel Gr repuhehevujuevoc. However, the Paz. reading frēž is firm, unimpeachable and transparent, and as representing a living WIr tradition it 1s preferable to any reading based on Elr material (besides, Sogd p'r'yc- seems to
1868:times referring back to the rel. pron.: + hac hàn nēvakēktar bütan nē šāytst quo pulehrius esse non poterat, the most beautiful imaginable 715-19; — empha- sizing the interrog. ké : ké han he? who art thou, say! 5633, cf Syr mann < man-hü, Arab man dà, mà dä. — hàn 4 regularly intreduces the definite rel. attr. (v. s. v. 4; less often En 4, & i, 0$ 1): hàn i xue$ x" atas 518; han i pit framān 3'1?* sq.; hàn i anagr rošneh 3618; han + dēvān särenisn 3724-25 (NB: in this case not -išneh, but without hàn % it would be dévan särenisneh!); — replaces a subst. already mentioned: hir 4 mēnēi ... han + getäh the property of the heavenly world ... that of the material world 79%; ruvān hàn i kē? whose soul? answer: häni Kri- šāsp 312-4; — elliptic expressions: han 7 man my religious duty 53? (referring to what is already mentioned in l. 5, cf s. v. én), the full expression 1. 7-9: nē han à man apäyet yaštan & (this man here) frac yazēt; andar han i man in my house 3717-18; similarly 3618-20, 371; — hàm 4 governs a nominal clause: hac han % Zartuxšt andar han x“arrah because Z.was (in =) endowed with such a glory 481. — han occurs in a great many compound
1940:harvén [hlwyn'] attributive form. of har < harv; ~ kas everyone 64!9; v. also harvistén. — In Bal. (NW language) an adj. precedes its noun and generally takes the ending -én (-e), Longworth Dames, TBL 13 (Gilbertson did not hear the final nasal, BL 35, obs. 2). Cf nēvakēn and v.s. v. mēnūt.
2063:hu-órón [hw^wlwn'] “of good front side”: beautiful from in front; Zartux$t had seen Spandarmat ~ u *huparrön u hu- tarist beautiful from in front, from the reverse side (= from behind) and all round 5721, with the gl. ku hamäk giyäk nēvak būt pasēh [thus the text must be divided] ‘that is: she was beautiful in all parts (seen from) behind’. — FrO 3a apparently gives the Av. text underly- -ing this passage: hordca [read aordca] paräca tarasca, Phl örön u parón u tarist: hutarest [Paz.] pas hac hamäk kustak "in front and from the other side and all round: beautiful all round (seen from) behind and from all angels'. — The inter- pretation of Bthl (43, 641, 860) misses the point. V. örön, paron, *huparrön, hutarist and turist.
2131:jāyišn [y?dšn'], 70!? jahišn [yhšn'] For- tune, luck, dispensation 2?!. 145; ~ u zaman <i> brihenišn rād 14'?, v. zaman; murvāk ~ i névak augury (and) good Fortune (i.e., good Fortune revealed through augury) 18!; pat névak ~ <u> yazdän hayyārēh with good fortune and the help of the gods 121-4; 121°; pat ~ hayyārēh i pat martömän xrat veh For- tune (giving aid to =) favouring men, wisdom is the best thing [she gives] 7012-13, Skr. v. siddheh sahāyatāyai ma- nusyanam buddhih uttamā; cf ke [for ka] ~ hayyär pat martömän cis + xrat veh when Fortune (is a helper to =) favours men, wisdom is the best of things PT 675-5, with the explanation cé hakar par- kast xvāstak be šavēt aivāp cahārpād be mirét xrat bē mānēt for if wealth dwindles and is lost or animals die wisdom remains; pātixšāi han névaktar i... xrat u dānišn nēvak api-$ ~ hayyäreh apāk that ruler
2419:Phl mānēnak ‘belonging to the sphere man’, 1. e. ‘rain-bearing’, or, as a subst., the rain itself. Paz. substitutes āvgīna, based on a reading MY?-kynk': apakénak, Skr v. ratnäkrti ‘of jewel form’; accepted by Bailey, ZP 131 (‘crystal’), but not preferable. — I withdraw my reading *mānēvak given in the Index.
2515:matārēh abstr. v. n. of matan: pat nēvakēh aves FR 7017318; 0012.16.
2532:ménitan [mynytn'], opt. 2nd p. sg. meneš 3312, to think, with kū that, often ētūn ~ ku: 40° ete. (as to 469 sq. v. s. v. matar); parenthetically ménam this is my opinion 56%; imp. men! just think! lo and behold! 5815; — with an obj.: ahlä- yéh ~ to think righteousness, that which is righteous in an absolute sense 7873, opp. mitöxt (q. v.) ~; veh martom ~ to think well of, to be well disposed towards men 781, opp. tar (g. v.) ~; mēnam tē rād nēvakēh I mean well for thee 4721; et i tē
2685:névakéh beauty, bliss. 10413. also purr-nēvakēh.
2687:nēvakēn v. nēvak.
2688:Nēvak-gāv [ndwk' TWR?»] n. pr. one of the Ātwiyān (Aspikän) family 47°. névak-gohréh [ndwkgwhlyh] the quality of being of good substance 793.
2804:oi [LH], 6 [L] dem. and det. pron. this; also the pers. pron. of the 3d p.: he, she, it; when used adjectively placed before its headw.: 0? mart this man; det. 0% ke 6671; õi veh ke 223- mänäk(k)äi (g.v.) 6 či cigon ke ... 4182; 6% is the normal form, 0 is rare: 6 ydtuk 5412-18; 6 màn this palace (subj.) 5822-26, 6114.23; 6 kē he who 90? (e 5715 is prev. to mat l. 16); — gen. his, her, its: % õi placed after, or hän + oi placed before its headw.: han i õi mat 39%; — forms the def. rel. attr. (v. s. v. 2): O õi 4 tē pusar 5174; õi i äxtar sardār 2618 (but 2616 6 õi āzvar sardār); õi i dus-äkäh u vat-xàm mart 91U, etc.; changes an adj. into a subst.: õi i druvand the wicked man 7417; — pl. ētšān ['LH-š*n'] they, them, these, both cas. rect. and cas. obl., independant or adj.; ūtšān amäh hem kē we are those who, we belong to those beings that 5728-24; connected with a pl. in the cas. rect.: ūtšān hom these haoma- stalks 41!9 (subj.). 417? (dir. obj.); bē örsän gav dos milk these cows 42°; disan druž ... bē 6 došax" oftend 10228-24; to. gether with the cas. obl. pl.: pač paitiyära- keh + ... ētšān 12 axtarān 719; the con- struction is, however, unstable: ó?$ün-ic 12 aztarän (subj.) ... ravénd 8724-5; har nēvakēh 4 (obj.) ölsän axtarān (subj.) barščnd, oifün apäztarän haciš apparēnd
3004:44%; pat hamāk rēc 49°; asp 2... ke pat rče-E 70 frasang be čiyend-(h)E (v. āma- tan) 610-31; pat bavandakéh i 30 sal 561; pat hazārak sar 99° etc.; pat har za- màn 10472; pat har gah u zaman 71%; pat € bar at one time 328; pat hàn yavar* ka on the occasion when Pl:2; pat han afterwards; pat fratoméh, pat avdoméh, pat bundahisneh, pat frazam: v. below II. 9. — 3. instrumental: pat dast dästan; pat han + dašn pad frac škast 531-12; pat uzvan ...saxtan göbend 1069; pat zafar apāc jūtār bütan 48°; pat cašm dītan; pat hàn + 4 äyö- žišn rahy vāzēt 519-11; pat ap (4) zarr nipistak 107°; with abstract nouns: pat zór u hunar ...hecakhaccahul hixt 15%; personal 7129-21, - II. in a figurative sense: 1. to the benefit of, or to the detriment of: cé-§ pat man névakéh vas kart 351; pat fradandàn i man vizandkār bavend 143. — 2. causal: pat zor... i Šahpuhr kanicak avd sahist 158-9; <pat> patvand because of relationship 117°; api-t pat ruvän dusxtäreh eton bavēt cigón 45°; — as a reward for: har kasé pat han and kar u kirpak ... mizd pātdāšin dahénd 10324-25, — 3. concessive: in spite of, notwithstanding, e. g. dānākēh + Zartuxšt pat han 1 aparnäi dātēh 539. — 4. final: for, e.g. pat én kar frestit ku ... 139; pat kār-ē Sut estat 1417; pat pātdāšin 9519-13; pat han + hunuskän ken 50'-?; pat xvēšēh u āzātēh dātan 117°. — 5. pat nām i... in the name of; in oaths: by: pat x%arrah t Ohurmazd bag ... sdkand xuarčt (imp.) 2117-18; 5913.29, — 6. with regard to: pat dipireh u asvārēh ... ētēn frahast ku ... 226-27; pat cövegän ... cer u nipartak būt 315-16; drāžtar pat bālai u früx"tar pat pahnai 389-19; ka pat tan ētūn vazurg but hend +... 3229-27; 2 angust pat balas 93; pat nēvakēh apar-arZünik 921-15, — 7. distributive: pat 10 mart nān-ē ka xuarend sagr hend 86?1—?, — 8. in a great many ex- pressions and idioms in varying func- tions, e.g. in such idioms as refer to domination (over), struggle, fight eto. (with, against), accusation (3714), excuse
4195:visén [wsyn] all, in attributive position before its subst.: ~ giyäk everywhere 9718, — From vis, SW form of OAr visva-, OP visa-, Av. vispa- v.s. v. visp; as to vis: visen v.s.v. nēvak. — FrP Cod. S, XVII, 10 has ws(>n', ws?n'k (?) = visän, visänak (?) with the NP gl. wsf, wsfah.
4768:Pi, P2 = the Persepolis inscriptions in Pahlavi, v. MP I, p. XXIII; as to the new photographs of them put at my disposal by Professor H. Luschey v. Gloss. s.v. nēv and Türän. Quotation of lines: Pi: 2, P2:3 ete.
```


## [2026-09-07T19:32:16.152Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== PHD_mackenzie grep niw\"; grep -n -i \"niw\\|nêw\\|nēw\" PHD_mackenzie.txt | head -40"
}
```


### [2026-09-07T19:32:16.207Z] TOOL RESULT

```
== PHD_mackenzie grep niw
3727:nibeg [npyk I N niwe] writing, scripture, book.
3799:niwag [nw)k' I M nw)g, N nawii] music, song, melody.
3800:·niwe [nwyk' I (N nuwed)] good news.
3801:+niwey-, -isn, v. niwistan.
3802:+niweyenidan [mvykyn-ytn ] = niwistan.
3804:niwistan, +niwey- [nwstn', nwyd- I nwyk-] announce, consecrate.
5963:announce niwistan, niweyenidan.              win(n)iirisn, wirayisn(ih).
5964:announcement niweyisn(ih).                arranger diyenag.
6254:consecrate niwistan, niweyenidan.            coral wassad, xrohak.
7044:march (border) marz; ,.,., warden,         melody niwag.
7108:mistress kadagbiinug.                          music niwag.
7156:news, good'" niwe.                        paydag, rosnag.
7621:skull mastarg.                                song cegamag, niwag, srod.
10108:niwistan                            winahgarih
10122:nazdikih               AUwS,        niwey-
10124:nazoik                   ,~,        niwcy-                        -~\,
10125:wizend                   .,..s,     niweyen-                    -~1l\\
10126:nazdist                ,~,          niwcyenidan           \\~t'1)"
10127:wizcnd                    "'~'I     niwc, wandag
10135:                                    niweyisnih
10139:wizandisn              ,~tS' I      niweyisn
```


## [2026-09-07T19:32:28.542Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== CHEUNG vaid/nivaid\"; grep -n -i \"ni-vaid\\|nivaid\\|niwistan\\|\\*vaid\\|VAID\" CHEUNG.txt | head -20; echo; echo \"== NYB nev\"; grep -n \"^nēv\\|^nivēt\\|^nivēs\\|^nivēy\" NYB_vol2_glossary.txt | head -20"
}
```


### [2026-09-07T19:32:28.605Z] TOOL RESULT

```
== CHEUNG vaid/nivaid
7437:(supplet. y-), Isfah. undán/ (supplet. y-), Bakht. avedan, avaidan, awaidan / (supplet. 
43174:avedan, avaidan, 

== NYB nev
2687:nēvakēn v. nēvak.
```


## [2026-09-07T19:32:29.716Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport re\nt=open('PHD_mackenzie.txt',encoding='utf-8',errors='replace').read()\ni=t.find('niwe [nwyk')\nleaf=t.count('\\f',0,i)\nprint('leaf',leaf,'-> printed approx',leaf-21)\nblk=t.split('\\f')[leaf]\nprint(blk[:900])\nEOF"
}
```


### [2026-09-07T19:32:30.932Z] TOOL RESULT

```
leaf 81 -> printed approx 60
nihuftan                          60                             nizlr
nihuftan, nihumb- [nhwptn', nhwmh- I = M, N -] cover, hide, conceal,
    clothe.
nihumbidan [nhwmbytn ] = nihuftan.
                             '
+nikOhidan, nikOh- [nkwh-ytn I N -] blame, execrate.
                                   '
 -isn: blame.
 -isnig: blameworthy, execrable.
nil [nyll N -] indigo.
nilOpal [nylw(k)pl I N -, nilofar] lotus, water-lily.
nimfidan, nimly- [nmwtn', nm)d-I M nmwdn, nm)y-, N -] show, guide.
nirfs- [nlps-] wane, decrease.
 -isn: decrease, diminution.
nirmad [nylmt l ] profit, interest.
 -Omand [-)wmnd] profitable.
P nisag [nys)k 1 P nys)g] bright, splendid.
                   '
nis- [nys- I M nyys-ydn, J -] see, observe.
nisln-, v. nisastan.
nisan [nyen l I = M, N nUan] sign, mark, banner.
nisast [nsst l I N -] association.
nisastan, nisin- [YTYBWN-stn 1 < A ...; ytb; nsstn' I M nsst,
```


## [2026-09-07T19:32:36.068Z] TOOL CALL #27: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-07T19:32:36.074Z] TOOL RESULT

```


```


## [2026-09-07T19:32:40.897Z] TOOL CALL #28: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%86%D9%88%DB%8C%D8%AF",
 "prompt": "Give the full Persian etymology section for نوید (navid/nevid) verbatim: Middle Persian form, Proto-Iranian root, cognates, and any cited authorities (Hasandust, MacKenzie, Cheung)."
}
```


## [2026-09-07T19:32:41.946Z] TOOL CALL #29: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%86%D9%88#Persian",
 "prompt": "Give verbatim the Persian etymology of نو (now/nou) 'new': Middle Persian form, Old/Proto-Iranian, PIE root, and cited sources."
}
```


### [2026-09-07T19:32:46.726Z] TOOL RESULT

```
# Persian Etymology for نوید

Based on the Wiktionary article provided, here is the etymology section:

**Inherited from Middle Persian** *nwyk'* (*\*niwē*), derived from **Proto-Iranian** *\*wayd-*.

**Cognates include:**
- Manichaean Parthian *nwydg* (niwēdag, "good news")
- Parthian *nwyst* (niwist, "invited")

**Cited Authority:**
MacKenzie, D. N. (1971), "niwē", in *A concise Pahlavi dictionary*, Oxford University Press.

**Note:** The article does not cite Hasandust or Cheung for this entry—only MacKenzie is referenced as the scholarly source.
```


### [2026-09-07T19:32:49.316Z] TOOL RESULT

```
# Persian Etymology of نو (now/nou) 'new'

**Middle Persian:** 𐭭𐭥𐭪𐭩 (nōg)

**Old Persian:** 𐎴𐎺 (n-v /⁠nava⁠/)

**Proto-Iranian:** *náwah

**PIE Root:** *néwos

The entry states: "from Middle Persian _𐭭𐭥𐭪𐭩_ (nōg), from Old Persian _𐎴𐎺_ (n-v /⁠nava⁠/), from Proto-Iranian _*náwah_... ultimately from Proto-Indo-European _*néwos_"

This etymological chain is supported by comparative evidence from related languages including Northern Kurdish nû, Pashto nëway, and Sanskrit náva, among others documented in the source material.
```


## [2026-09-07T19:33:01.837Z] TOOL CALL #30: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A7%DA%A9%D9%86%D9%88%D9%86",
 "prompt": "Give verbatim the Persian etymology of اکنون (aknun) 'now' and any mention of کنون (kunun), Middle Persian forms, Old Persian nūram, and cited sources."
}
```


## [2026-09-07T19:33:02.570Z] TOOL CALL #31: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/n%C3%A9wos",
 "prompt": "Give the reconstruction, gloss, and the Iranian/Indo-Iranian descendants listed (Avestan, Old Persian, Middle Persian), plus references cited."
}
```


### [2026-09-07T19:33:07.402Z] TOOL RESULT

```
# Persian Etymology of اکنون (aknun)

Based on the Wiktionary page provided, here is the stated etymology:

## Direct Quote

"From _[نون](/wiki/%D9%86%D9%88%D9%86#Persian "نون")_, ultimately from [Proto-Indo-European](https://en.wikipedia.org/wiki/Proto-Indo-European_language "w:Proto-Indo-European language") _[\*nu](/wiki/Reconstruction:Proto-Indo-European/nu "Reconstruction:Proto-Indo-European/nu")_ ("now")."

## Additional Note

The entry acknowledges its own incompleteness: "This etymology is incomplete. You can help Wiktionary by elaborating on the origins of this term. Particularly: 'Where does the first element come from?'"

## What Is Missing

The document does not provide:
- Information about کنون (kunun) beyond listing it as an alternative form
- Middle Persian forms or Old Persian *nūram
- Cited scholarly sources documenting the etymological development

The etymology traces the word only to Proto-Indo-European *nu, with the origin of the initial element (ا-) remaining unexplained on this page.
```


### [2026-09-07T19:33:08.165Z] TOOL RESULT

```
# Proto-Indo-European *néwos

**Reconstruction:** *néwos

**Gloss:** "new"

**Iranian/Indo-Iranian Descendants:**
The page lists "Proto-Indo-Iranian: *náwas" with a note directing to "see there for further descendants." However, the specific Avestan, Old Persian, and Middle Persian descendants are not detailed on this particular page.

**References Cited:**
1. Wodtko, Dagmar S.; Irslinger, Britta; Schneider, Carolin (2008) - "Nomina im indogermanischen Lexikon" (Heidelberg: Universitätsverlag Winter), page 524

2. Dunkel, George E. (2014) - "Lexikon der indogermanischen Partikeln und Pronominalstämme" (Heidelberg: Universitätsverlag Winter), volume 2, page 581

3. Pokorny, Julius (1959) - "Indogermanisches etymologisches Wörterbuch," volume 2, page 769
```


## [2026-09-07T19:33:11.922Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"nwr\" SOD_pages.txt | head -20"
}
```


### [2026-09-07T19:33:11.968Z] TOOL RESULT

```
4701:321 Hwrt nwrtyy M                        c~if^joij             334 Vs M, S                      (u^^'y^'j^*^
4702:    awart-niwartc =*»w>rt-, *wrt nwrtyy                             axas ©= MP yrdyq ©pi. -t ^'y'ns, 'x's
9392: 1947 *wrt nwrtyy      M          *            c^-^jwij           osuxs Owswxs-) ^wswys-
9393:       awart-niwarte ^'wrt nwrtyy
19855:     strong ?, decisive ?, resembling ?,                                st. tnwrt- «»mwrt-
20343: 5789 nWtry ? -» ^mrtr                                            not written, unwritten
21299:     niwart(e) =»nw}rst-, nwrtyy, nwrt-                                noise
21326:     nu-yarPe/ak (nw yrp'y, nw yrPk)                               6142 nwr B, S, C            (u>>>^    jj)JU<o^i
21327:     ignorance                                                          nur (nwry) ©<Av. nurdm-, Khwar. nwr; Yaghn.
21331:                                                                        ob. nwry, BSTBL
21333:                                                          jjj>     6143 nwrcyq C                                   j^'^jf
21335:                                                                        nurcik =*nwr
21341:6131 nwh' C                                                       6144 nwrn'y B =* zwrn}k
21342:     nun                                                          6145 nwrt- M                     Cu^j> to>J?c£j*-
21348:                                                                       nwrtyy     M              3j<y ic£ j>- JU j> «-0*^
21349:                                                                       niwarte    ^Hvrt nwrtyy, nw}rt(y)
21355:          323; Hen. LW 94; C2, 91R5                               6147 nwry B ~* nwr
21356:                                                                  6148 nwryjy M, S                            J*&<*Jj*
21358:                                                                       nu~rez(c) ©ob. pi. -ty(y) ? =>nwryz
21363:                                                                  6149 nwryz B                                J^^- '^sJjr*
```


## [2026-09-07T19:33:13.807Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"aknūn\\|aknun\\|kanūn\\|kunūn\\|nūram\" HRN.txt | head -20; echo \"=== HRN leaf 257 (p236) ===\"; python3 -c \"\nt=open('HRN.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(len(t)); print(t[257][:1200])\""
}
```


### [2026-09-07T19:33:15.256Z] TOOL RESULT

```
=== HRN leaf 257 (p236) ===
412
- 236 —
1052. nÜH jetzt, nun', vergl. ekniln, kunün.
aw. nü, nürem jetzt', vergl. oss. d. mtr, t. njr 'nun'
(207); §iyn. nur, sar. nur *heute*; phlv. nun; ai.
nündm,
bei. nü^ nun jetzt, nun (270).
1053. uuved *frolie Botschaft.
Die übliche Erklärung aus ni -j- l^vaed-, vergl.
aw. niva^dayemij ist erstens wegen der auffälligen
Erhaltung des d bedenklich und zweitens scheint
wegen np. pizöhlden im PehlevT n(i)v(i)hmUan, nicht
n(i)vedinltan gelesen werden zu müssen (vergl. No. 314).
1054. nöylden 'klagen (Sahn. I, 183 Vers 986, Calc),
necä 'Klage', nevtden, vergl. nevaliden, nallden.
ai. i/'nav-, nünti, ndvate 'brüllen (von Tieren)'; vergl.
np. zlnüden (No. 672).
1055. ne (geschrieben neh) nicht'.
aw. na; päz. na\ ai. nd.
kurd. ne; af/. na; oss. d. ne, t. nä (201).
1056. nu (geschrieben nah) neun'.
ap. navama- 'neunter ; aw. nava, näuma-, naoina-
neunter; phlv. wawm; d^.,ndva; arm. iw« (H. No. 115).
kurd. ne(h), ne(h); aty, LW. nu{h); wa,/, siyn. ndo,
sangl. minj. nao, yayn. nau, sar. nev.
Np. nuhiim ist eine ganz junge Bildung, die man
nicht auf das PehlevT übertragen darf.
1057. nihäden ^hinlegen, hinsetzen', Praes. w/Ä-e/w, aber
neht (AM. 65 Zeile 10).
aw. ni + 1^2 da- {nidadät) 'h
```


## [2026-09-07T19:33:28.751Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('SOD_pages.txt',encoding='utf-8',errors='replace').read()\ni=t.find('6142 nwr B, S, C')\nleaf=t.count('\\f',0,i)\nprint('leaf',leaf,'printed ~',leaf-66)\nblk=t.split('\\f')[leaf]\nprint(blk[:200])\nj=blk.find('6142')\nprint('...')\nprint(blk[max(0,j-1500):j+600])\nEOF"
}
```


### [2026-09-07T19:33:30.172Z] TOOL RESULT

```
leaf 312 printed ~ 246
 nwc

 6125 nwc     C, S                                                 6140 nwmyk     S =* nwmyq
        noc (nwy) ©f. adj. =4nwy                                   6141 nwptfr'wcyk M             ^Ji
...
 nwc

 6125 nwc     C, S                                                 6140 nwmyk     S =* nwmyq
        noc (nwy) ©f. adj. =4nwy                                   6141 nwptfr'wcyk M             ^Jijj jx j i^J*j*\j
        new                                             y-y1*           nu-patfrawclk ©Parth. anabyad ©pi. -/
        BSTii 90925: C2, 61R 25; nwcK MDiii                               =»ptfr*wncyk

6126 nwy'wny =* nmy'wn'y                                                oubliette
                                                     j\& ij^
                                                                        BBB p88 756; GMS 1015, 1162
6127 nw yrp>k B
     nu-yarPe/ak (nw yrp'y, nw yrPk)                               6142 nwr B, S, C            (u>>>^    jj)JU<o^i
     ignorance                                                          nur (nwry) ©<Av. nurdm-, Khwar. nwr; Yaghn.
     TSP 2.335; VJ 381,393                                                nur

6128 nw yrp*y =» nw yrP»k                                               now
                                                                        ob. nwry, BSTBL
6129 nw yrpk =* nw yrP>k
                                                          jjj>     6143 nwrcyq C                                   j^'^jf
6130 nwgrwc M
```


## [2026-09-07T19:33:38.192Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; timeout 600 python3 tools/ref_page.py BQT:2173 2>&1 | head -60"
}
```


### [2026-09-07T19:33:43.268Z] TOOL RESULT

```
(no exact page map; using offset -1917 -> pdf page 256; check the printed number and re-run with --pdf-page if off)
REF: BQT:2173  PDF: data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf page 256  OCR-lang: fas

بیان بیست ویکم
در نون با نون مشتمل بر چپار لغت
افنگیه « بفتح اول بروزن سنکه, بسمنی | ازفراغ بدن جضورت یکی ازحیوانات‌دیگرجلوه کر
زشت وعیب وعار باشد۱ - وبلفت زند وپازند(۱) | شود ۰
ما کیان را گویند که‌مرغ‌خانگی است؟ -وبمعنی ننگ نام - بروزن و معنی جنکه‌نامه
جنگه وجدال هم‌آمده است ۴ . است چه‌شگه‌بمعنی جنکه وجدال‌هم آمده ات6
سار ؟ - بروزن سنگار . بممنی | - و نظم وش‌برا نیز کوبند که بطریق هجو و بد
مسخ است ومسخ در لغت کردیدن ازصورتی است | کوبی «عبب جوبی لوشته شده باشد.
صورت دیگر که بدتروقبیج‌تر ازصورت اول‌باشد» ننگین ۱ - بروزن سنگین .بمعنی‌عیب
و باصطلاح اهل تناسخ آست که روح اسانی مد | داز و ممیوب وزشت شده باشد ۷ .
بیان بیسمت ودوم
در نون با واو مشتمل بر یکصد و چپل و نه لغت و کنات
« بفتح اول و سکون ثانی » معروف ۱ است که نقیض کهنه باشد ۸ ؛ و باین معنی بنم
(۱) چك : ژند و پاژد . .
۱ ۱ - پپلوی 3228 (حیا وشرم » احسای شرم) ۶ لیب رکه ص۱۵۵ پاروچا .۰4۳۲۲
۴ -اظ . مصحف و مغفف « تنگربا » ۱8۵8۵7 ۰ ۸)8(880۲۷2. 718 » پپلوی
7۷ ( مرغ » ماکیان) رك : پونکر ص ۰۱۱۸ ۴ - باین معنی ظ . مصحف«جنك».
۴ - از دساثیر « فرهنکه دساتیر ص ۰۷۱-۲۷۰ 8 - ظ.ممحف «جنك نامهف
و رك : اشکه. ‎٩‏ - لز : شکه این (سبت) .. :
۷ - هت پاك وحلال و ننگین روی نه حرام وپلیت و رنگین روی -
سنائی غزنوی « رشیدی:».
۸ - 28۷ :* فهرست ولف > .881 در تلفظ ( متداول ) تبدیل بة 30۱۷ شده ( ر4 :
خوبشمان ۱۰۶۵) ؛ اوستابی -32۷8 ( تازه) » پهلوی 88۷81 . 2۵6 . پازند 2۵ ۰-هندی
باستان -38۷8۸ ۰ ارمنی. ۰807 اففانی 880 , 28۷81 : امتي38۷88 ۰ 3۷08 ۰ بلوچی ۰3۵۴
۰ خفنی 84 , سربکلی‌زل8 « اسشق ۱۰۸۵ > ؛ کرد 80 ۰ 260 (نازه) دژایا س۵۷۸:
که مارا مکش تا یکی لو اهثر بیاموزی از ما کت آید ببر.
فردوسی طوسی «* شاهنامةٌ بخ چ ٩ص‏ ۲۲ >
```


## [2026-09-07T19:33:55.320Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; timeout 900 python3 tools/ref_page.py BQT:2173 --image 2>&1 | tail -20"
}
```


### [2026-09-07T19:33:56.579Z] TOOL RESULT

```
صورت دیگر که بدتروقبیج‌تر ازصورت اول‌باشد» ننگین ۱ - بروزن سنگین .بمعنی‌عیب
و باصطلاح اهل تناسخ آست که روح اسانی مد | داز و ممیوب وزشت شده باشد ۷ .
بیان بیسمت ودوم
در نون با واو مشتمل بر یکصد و چپل و نه لغت و کنات
« بفتح اول و سکون ثانی » معروف ۱ است که نقیض کهنه باشد ۸ ؛ و باین معنی بنم
(۱) چك : ژند و پاژد . .
۱ ۱ - پپلوی 3228 (حیا وشرم » احسای شرم) ۶ لیب رکه ص۱۵۵ پاروچا .۰4۳۲۲
۴ -اظ . مصحف و مغفف « تنگربا » ۱8۵8۵7 ۰ ۸)8(880۲۷2. 718 » پپلوی
7۷ ( مرغ » ماکیان) رك : پونکر ص ۰۱۱۸ ۴ - باین معنی ظ . مصحف«جنك».
۴ - از دساثیر « فرهنکه دساتیر ص ۰۷۱-۲۷۰ 8 - ظ.ممحف «جنك نامهف
و رك : اشکه. ‎٩‏ - لز : شکه این (سبت) .. :
۷ - هت پاك وحلال و ننگین روی نه حرام وپلیت و رنگین روی -
سنائی غزنوی « رشیدی:».
۸ - 28۷ :* فهرست ولف > .881 در تلفظ ( متداول ) تبدیل بة 30۱۷ شده ( ر4 :
خوبشمان ۱۰۶۵) ؛ اوستابی -32۷8 ( تازه) » پهلوی 88۷81 . 2۵6 . پازند 2۵ ۰-هندی
باستان -38۷8۸ ۰ ارمنی. ۰807 اففانی 880 , 28۷81 : امتي38۷88 ۰ 3۷08 ۰ بلوچی ۰3۵۴
۰ خفنی 84 , سربکلی‌زل8 « اسشق ۱۰۸۵ > ؛ کرد 80 ۰ 260 (نازه) دژایا س۵۷۸:
که مارا مکش تا یکی لو اهثر بیاموزی از ما کت آید ببر.
فردوسی طوسی «* شاهنامةٌ بخ چ ٩ص‏ ۲۲ >
```


## [2026-09-07T19:33:59.661Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; ls -la data/verification/sources/refs/ocr/BQT/ 2>/dev/null | tail -20; find data/verification/sources/refs/ocr -name \"*2173*\" 2>/dev/null"
}
```


### [2026-09-07T19:33:59.722Z] TOOL RESULT

```
-rw-rw-r--  1 sfmqrb sfmqrb    3114 Sep  6 11:25 2417.txt
-rw-rw-r--  1 sfmqrb sfmqrb     561 Sep  6 11:25 2417.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  161891 Sep  6 11:16 2420.png
-rw-rw-r--  1 sfmqrb sfmqrb    3629 Sep  6 11:16 2420.txt
-rw-rw-r--  1 sfmqrb sfmqrb    2009 Sep  6 11:17 2420.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  153589 Sep  5 16:27 2427.png
-rw-rw-r--  1 sfmqrb sfmqrb    3424 Sep  5 16:27 2427.txt
-rw-rw-r--  1 sfmqrb sfmqrb    1757 Sep  5 16:28 2427.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb    2615 Sep  4 15:28 31.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  512022 Sep  5 16:12 333.png
-rw-rw-r--  1 sfmqrb sfmqrb    1339 Sep  5 16:12 333.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb    1508 Sep  4 15:27 58.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb    1931 Sep  4 15:02 70.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb    1606 Sep  4 14:54 72.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  669351 Sep  5 01:38 733.png
-rw-rw-r--  1 sfmqrb sfmqrb    1152 Sep  5 01:39 733.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  726576 Sep  6 18:36 829.png
-rw-rw-r--  1 sfmqrb sfmqrb     981 Sep  6 18:36 829.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  624515 Sep  5 16:20 902.png
-rw-rw-r--  1 sfmqrb sfmqrb    1658 Sep  5 16:20 902.vision.txt
data/verification/sources/refs/ocr/BQT/2173.png
data/verification/sources/refs/ocr/BQT/2173.txt
```


## [2026-09-07T19:34:05.100Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -c \"\nfrom PIL import Image\nim=Image.open('data/verification/sources/refs/ocr/BQT/2173.png'); print(im.size)\nw,h=im.size\nim.crop((0,int(h*0.60),w,h)).resize((int(w*1.4),int(h*0.40*1.4))).save('/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/bqt2173_foot.png')\nprint('ok')\""
}
```


### [2026-09-07T19:34:06.681Z] TOOL RESULT

```
(1650, 2546)
ok
```


## [2026-09-07T19:34:09.250Z] TOOL CALL #39: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/bqt2173_foot.png"
}
```


### [2026-09-07T19:34:09.574Z] TOOL RESULT

```

```


## [2026-09-07T19:34:09.571Z] INPUT

[Image: original 2310x1425, displayed at 2000x1234. Multiply coordinates by 1.16 to map to original image.]


## [2026-09-07T19:34:35.898Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; mkdir -p data/verification/sources/refs/ocr/BQT; cat > data/verification/sources/refs/ocr/BQT/2173.vision.txt <<'EOF'\n[BQT vol.4 printed p. 2173 = BQT_v4_picofile.pdf page 256; read from ocr/BQT/2173.png by vision]\n\nSection heading: «بیان بیست و دوم / در نون با واو مشتمل بر یکصد و چهل و نه لغت و کنایات»\n\nHeadword: «نو «بفتح اول و سکون ثانی» معروف۸ است که نقیض کهنه باشد؛ و باین معنی ...»\nShahnameh citation at the foot: «که ما را مکش تا یکی نو هنر / بیاموزی از ما کت آید ببر» — فردوسی طوسی، شاهنامهٔ بخ ج۱ ص۲۲.\n\nMo'in's etymological footnote 8 (verbatim, Latin forms read off the image):\n«۸ - nau ، «فهرست ولف» ، nau. در تلفظ (متداول) تبدیل به now شده (رک: هوبشمان ۱۰۴۵)؛\nاوستایی nava- (تازه) ، پهلوی navak ، nōk ، پازند nō ، هندی باستان náva- ، ارمنی nor ،\nافغانی nau ، navai ، استی nāvāg ، nvog ، بلوچی nōk ، nōx ، شغنی náu ، سریکلی nūj ،\nاسحق ۱۰۴۵ ؛ کردی nū ، neū (تازه) دژابا ص ۴۲۴»\n\n(Same page, footnotes 1–7 belong to the preceding section «در نون با نون»: ننگ, ننگه, نناسار, ننگ‌نامه, ننگین.)\nEOF\necho saved; ls -l data/verification/sources/refs/ocr/BQT/2173.*"
}
```


### [2026-09-07T19:34:35.960Z] TOOL RESULT

```
saved
-rw-rw-r-- 1 sfmqrb sfmqrb 129763 Sep  7 15:33 data/verification/sources/refs/ocr/BQT/2173.png
-rw-rw-r-- 1 sfmqrb sfmqrb   2723 Sep  7 15:33 data/verification/sources/refs/ocr/BQT/2173.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   1264 Sep  7 15:34 data/verification/sources/refs/ocr/BQT/2173.vision.txt
```


## [2026-09-07T19:34:36.916Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== MON نوید\"; grep -n \"نوید\" MON_part1.txt MON_part2.txt | head -10; echo \"== MON نو =\"; grep -c \"\" MON_part1.txt MON_part2.txt"
}
```


### [2026-09-07T19:34:36.992Z] TOOL RESULT

```
== MON نوید
MON_part2.txt:55258:نوید. (عم.) مژدگانی انعام خبر خوش. 
MON_part2.txt:74243:نبید: 074« |- نوید ] (ا.) میزدگانی» نوید. 
MON_part2.txt:81140:نویدگر: ۰-2۲ (ص‌فا.) به مهمانی خواننده» 
MON_part2.txt:81143:نویدن: 2۷-1000 (- ناویدن] (مصل.) 
MON_part2.txt:81145:نویدن: بر حود پیچیدن. 
MON_part2.txt:86765:وعد: 20 [.] (مصم.) نوید دادن کسی را 
MON_part2.txt:86767:نویددهی. (.) وعدء خوش, نوید» مژده. 
MON_part2.txt:86769:وعد و وعید: نوید خیروشر. 
MON_part2.txt:86771:ود (0-)02 :۷2 [ع.] (.) نوید» مژده. 
MON_part1.txt:55795:مت. نوید. به مهمانی بردن شخصی پس از 
== MON نو =
MON_part2.txt:94500
MON_part1.txt:99339
```


## [2026-09-07T19:34:40.893Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '81130,81150p' MON_part2.txt"
}
```


### [2026-09-07T19:34:40.939Z] TOOL RESULT

```
تعالی» قر آن. 

نویان: 550« (- مغ. تر. - نویین - نوین] 
(.) امبر. فر مانده سیاه» سردار. ضح.- در 
عنوان سرداران مغول و ترک آید. 

لو ید: (0۷[066۷20 (.) خبر خوش» مژده؛ 
شارت. وعده نیکك. شارت دادن‌ه‌ضیافت» 
دعوت‌به مهمانی) مق. خرام. 

نویدگر: ۰-2۲ (ص‌فا.) به مهمانی خواننده» 
شارت دهنده به ضیافت. 

نویدن: 2۷-1000 (- ناویدن] (مصل.) 
جنبیدن» حرکت کردن. لرزیدن. بر خود 
نویدن: بر حود پیچیدن. 

نو یده. (0-)02[-۱3۲ (امف.) جنیده» حرکت 
کر ده. لر ز بده. 

نو یده: (6-)20۷-102 (امذ.) ناله کرده» زاری
```


## [2026-09-07T19:34:42.821Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D9%86%D9%88%DB%8C%D8%AF/",
 "prompt": "Quote the فرهنگ معین (Mo'in) entry for نوید verbatim, including any bracketed origin tag like [په.] or Pahlavi form, and also the دهخدا entry etymology if shown."
}
```


### [2026-09-07T19:34:50.130Z] TOOL RESULT

```
# نوید - Lexicographic Entry

## Farhang-e Mo'in (معین) Entry

According to the Mo'in dictionary, the entry reads:

"(نَ) (اِ.) ۱ - خبر خوش، بشارت. ۲ - وعدة نیک."

This translates to: "(n) 1 - good news, glad tidings. 2 - a good promise."

## Dehkhoda (دهخدا) Etymology

The Dehkhoda dictionary provides extensive etymological discussion, noting that نوید derives from the prefix "نِ" combined with the Avestan root "وئید" (waēd). The entry explains that this root relates to announcing or proclaiming, with the compound word ultimately signifying news or tidings of a positive nature. The dictionary emphasizes that the word encompasses not merely information, but specifically communications that bring joy or positive expectation.
```


## [2026-09-07T19:35:05.796Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== BRT nava neu\"; grep -n \"nava-\\s*,\\|‘neu’\\|'neu'\\|nūrəm\\|nurom\\|nürom\\|nüram\" BRT.txt | head -20; echo \"== BRT nivaed\"; grep -n -i \"nivaed\\|nivaēd\\|ni-vaēd\\|nivaēdaya\" BRT.txt | head"
}
```


### [2026-09-07T19:35:05.879Z] TOOL RESULT

```
== BRT nava neu
5050:'in  der  angegebenen  Weise':  U . ,  nüram %74väm  vamavatäm  ty<^  manä  kartam  °'hil *abava'"'>  ". ,  soll  dich  jetzt  überzeugen: was  von  mir  getan  wurde,  so  (wie  an- gegeben) geschah  es"  Bh.4.10;  —  ll^rf- käram  dUÜy  ..'>ä^  xmäsahidis  ada  (sd.)- taiy  .  .  D.  tf.4;  —  aAmiii  bityS  üjasal  .  . gSu^  iihrpa  ..'ha  äjasat\x.  14.6;  9-27*; ~ paiti  mqm  pinsaituka  ..  'ha  te  ar?hal  ^ vatihs  N.jS.T,  7,  Vyt.42;  —  pasca  hri- ,
7034:kniipfiiDg  eines  adversativen  Satzes  'aber; sondern;  vielmehr;  gleichwohl':  iha  main- yete  dus:^armä  .  .  ä'  az3M  manya  Yt.  10. losf.;  —  nöil  .  .  vispa  yasathahs  .  .  ä' .  .  aÄ'J  zara%uitro  Vt.  IJ.  ig;  5,  55  aSt^', N.55,  Y./0.8,  ig.  5;  —  iä  fi-avasays  .. aojistä  hinti  .  .  yä  .  ,  saosyaniqm  ä° anyalsqm  fravasayö  (sd.)  ,  ,  Yt.  jj.  17; N.  102;  —  nabänazdists  ä'  kavatqm  nana (sd.)  N.  Ig;  g,  67;  —  «/  zaotars  (sd) kairim  avAap. .  3'  AävanänS  (näral.  kairim a»Aat)  yat .  .  N.  72;  73-'j6,  66'';  —  apqm . .  yä  para  ahmäi  hist>nta  .  .  ä°  th  nüram p-aiacin/i  Yt.  13. 5:i(.;  56,  5S;  —  aat{^.  8) yahmäi  xsnBtS  bavaiti  mi^rS  ahmäi  jasaiti avaiäAe  ä'  yahmal  ibistd  bavaiti  . .  akmüi früiiinäayeiti  nmämmca  ..  Yt/o.S?; yaike  xsa'hriäa  nStt  aotfiri  ar?ka  . .  para akmat  yat  . .  ä°  yat  ..  ". .  bevor  . aber  als  . ."  Ytig.$$f.;  — yat  hf puhi iissaySi^e  .  .  ikaisö  anyö  .  .  ä°  anys Y.g.ia;  —  tarS.d»nanS  (sd.,  näml.  urv rayä  aahari)  .  .  ä°  up»ma  aisöJräjanAa N.po; —  navajcsaparfm  ..  aivii^äi kama  mazäräjaAlmW.^.^2;'^.46,47,5o; —  nöit  ahmt  nmäne  *sänaite  ä^rava  .  . ä'  .  .  sayänie  dahaksea  "nicht  werden  .  , geboren  .  .,  sondern  es  sollen  geboren werden  .."  Y.  //.6;  —  käu  .  .  yff  .  .  van- tasea  Aqm.räzayeili  .  .  aha  diin  upaJaosa^ yati  .  .  raZiayaca  (sd.)  .  .  ä'  yat  .  .  var>- saica  *hqm.räzayar>Aa  .  .  aat  (s.  7)  .  . pascana  apa.baröis  ". .  vielmehr  wenn  du dir  die  Haare  ordnest  .  .,  so  sollst  du dann  . ."  V.iy.2—4;  —  attm  vispanqm dämanqm  nipäta  ahmi  .  .  ä'  ('gleich- wohl') ma  nöit  masyäka  .  .  yazante  YL 10. 54.  a)  bes.  mit  a)  folgendem  _ya/  oder
14319:kyat  .  .  frqlta  Y.  43-^4-  zu  3)  /aiti aile  mihra  tava  yat  akurake  mazdä  V. 4.i.  II)  schwachtonige  (enklitische) Formen  stehen  i)  hinter  dem  ersten  Wort des  Satz-  oder  Versteils,  von  dem  sie  aber a)  durch  ein  oder  auch  zwei  andere Enklitika  getrennt  sein  können;  3)  unregel- mässig und  selten  in  andrer  Stellung. 1)  Akk,;  a)  II  imAp.;  zu  i):  a^ura^mazda äw»3ffi"  dauäa  biyl^  Bh.4.10,  16;  — tyi^  matiä  kartam,  varnavatäm  huväm Bh.4'6;  —  unsicher:  ♦•  nüram  %uväm vamavatäm    Bh.  4.  10.  b)    im   Aw.;
19295:a)  an  der  Spiue  des  SaU(teil)cs:  at  fra- vaxsyS  n'  *gUls4Um  (sd.)  n°  sraota  . .  n' Im  vls^a  . .  *matdänAs.dam  (sd.)  Y.  4:5, 1 ; 8;  —  ahuml  n°  na  avarS  (sd.)  Y.  2p. II*'.  b)  in  andrer  Stellung,  mit  i^t: tat  nS  nat^  vanlänl  {sA.)  Y.  57.  i;  — *a%a  *naäj'''  atnim  a^rapaitim  upBissit N. //(?).  b)  schwachtonig,  hinter  dem ersten  Wort  des  Satzes:  asUta  «■  aiAkai haca  VUai  gauÜ  öuyJt  Y.  6^0.  3 ;  —  us  n' aiiihäi  vTse  JamySl  as»m^a  .  .Y.60.3;  — para  »•  ahmst  haca  asanhalca  . .  axliat . . ^■9- Sil  —  *^'i  »°  P<ira  ahmst ..  paiti. - jasätiF  .  ,  Y.g.$$;  j.^n,  F.44;  — ya'^a n'  malysha  *xh/isti  Ä?»(?(sd.)  vTiävc^einti V.2.31;  —  yavat  »'  ah  .  .  P.42{?). ai.  n«,  «M,  gr.  n>  usw.  (i.  BoM.  GrGr,3  544).  — S.  auch  nüram.  —  Pii.r  nun;  i.  noch  No.  1. — I)  S.  na-  No,  3.  ~  »)  UnEtchn;  Hds.  iä%nm trvSaiuim ;  PQ. :  tlänäiHiar,  lässt  also  ttvX  aus.
22748:kaus.  BedeuL  'überzeugen,  ■aitisiv',  Med.  I J  MäfyJ' .  .paruv  *%aäayä* . .  nailim  vama- 1 vätaiy  duruxtain  (sd.)  *maniyätaiy  Bh.  4- S;  —  tya^  manu  kartam  varnavatam  1 "^uvam  mJ/yJ*  *draujTyähy  {^A.)  Bh.  4.  6; — . .  nüram  %uväm  vamavaiSm  ty<^  mann  \ kartam  ai'a3ij(sd.)..Bh.4. 10.'!  a)gAw.  | insbes.  vom  Überzeugen  auf  religiösem  1 Gebiet,  sva.  'zum  Glauben  bringen,  be- kehren'; nur  Int.,  Med:  tat  nS  ..  vaolä^ kisvS .  .y3  jvantd  vispSng  väuraya  ( 1 SOM.) ". .  auf  dass  ich  alle  Lebenden  überzeugen  , kann"  Y.jr.  3;  —  >43  (näml,  viääitis)  zT- pourül  ispnts  väuraitl  "sie  wird  ja  noch ' viele,  die  hören  wollen,  veranlassen  sich zu  bekehren"  Y.  47-  6.  ")  'bekehren zu  — '  (Akk.) :  ana  mahrH  matist>m  väitröi- maidl  xrafsträ  hizvä  "mittelst  dieses  (Ver- heissungs)  Wortes  wollen  wir  die  Xr.  (das Raubgesindel)  mit  unsrer  Zunge  zu  dem bekehren,  was  das  grösste  ist"  Y.  28. S-  {varänJ  Y.j^j.  4:    lies  livarünT,    s.
== BRT nivaed
```


## [2026-09-07T19:35:14.518Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"S.  auch  nüram\" BRT.txt; echo ===; python3 - <<'EOF'\nimport re\nt=open('BRT.txt',encoding='utf-8',errors='replace').read()\ni=t.find('S.  auch  nüram')\nleaf=t.count('\\f',0,i); print('leaf',leaf)\nblk=t.split('\\f')[leaf]\nprint(re.findall(r'\\b1[01]\\d\\d\\b',blk)[:10])\nprint(blk[max(0,i-t.rfind('\\f',0,i)-2500):][:60])\n# print segment around\nj=blk.find('S.  auch  nüram')\nprint(blk[max(0,j-2500):j+300])\nEOF"
}
```


### [2026-09-07T19:35:15.761Z] TOOL RESULT

```
Exit code 1
19295:a)  an  der  Spiue  des  SaU(teil)cs:  at  fra- vaxsyS  n'  *gUls4Um  (sd.)  n°  sraota  . .  n' Im  vls^a  . .  *matdänAs.dam  (sd.)  Y.  4:5, 1 ; 8;  —  ahuml  n°  na  avarS  (sd.)  Y.  2p. II*'.  b)  in  andrer  Stellung,  mit  i^t: tat  nS  nat^  vanlänl  {sA.)  Y.  57.  i;  — *a%a  *naäj'''  atnim  a^rapaitim  upBissit N. //(?).  b)  schwachtonig,  hinter  dem ersten  Wort  des  Satzes:  asUta  «■  aiAkai haca  VUai  gauÜ  öuyJt  Y.  6^0.  3 ;  —  us  n' aiiihäi  vTse  JamySl  as»m^a  .  .Y.60.3;  — para  »•  ahmst  haca  asanhalca  . .  axliat . . ^■9- Sil  —  *^'i  »°  P<ira  ahmst ..  paiti. - jasätiF  .  ,  Y.g.$$;  j.^n,  F.44;  — ya'^a n'  malysha  *xh/isti  Ä?»(?(sd.)  vTiävc^einti V.2.31;  —  yavat  »'  ah  .  .  P.42{?). ai.  n«,  «M,  gr.  n>  usw.  (i.  BoM.  GrGr,3  544).  — S.  auch  nüram.  —  Pii.r  nun;  i.  noch  No.  1. — I)  S.  na-  No,  3.  ~  »)  UnEtchn;  Hds.  iä%nm trvSaiuim ;  PQ. :  tlänäiHiar,  lässt  also  ttvX  aus.
(eval):1: == not found
```


## [2026-09-07T19:35:22.918Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport re\npages=open('BRT.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor k,b in enumerate(pages):\n    if 'S.  auch  nüram' in b:\n        leaf=k;break\nprint('leaf',leaf)\nfor j in (leaf-1,leaf,leaf+1):\n    print('--',j, re.findall(r'(?m)^\\s*(\\d{3,4})\\s*$',pages[j])[:8], re.findall(r'\\b1[01]\\d\\d\\b',pages[j])[:8])\nb=pages[leaf]\ni=b.find('S.  auch  nüram')\nprint(b[max(0,i-1200):i+100])\nEOF"
}
```


### [2026-09-07T19:35:24.209Z] TOOL RESULT

```
leaf 606
-- 605 [] []
-- 606 ['1089', '1090'] ['1088', '1089', '1090']
-- 607 [] []
r/nqmca  .  .  Y.
61.  4;  3-4'".
Zum  V.  Uar:  —  Vgl,  tüüarttay-.  —  Vi.:  pa ap£  barisnih.
•  j.  niz-bara^ay-  £  "Weg-,  Forttragen':
pasla  nasävS  'ät  "nachdem  der  Leichnam weggetragen  ist"  V.o. 33,  38,  41.
I      Zum  V.  'iar-i  vgl.  müirttay:  —  Pü.;  pas  kac
I      nasäi  afe  iarihük.
[•  j.,  g.  nQ  Adv.  'jetzt,  nun';  i)  starktonig;
dby  Google
1089
nmäna-I
1090
a)  an  der  Spiue  des  SaU(teil)cs:  at  fra- vaxsyS  n'  *gUls4Um  (sd.)  n°  sraota  . .  n' Im  vls^a  . .  *matdänAs.dam  (sd.)  Y.  4:5, 1 ; 8;  —  ahuml  n°  na  avarS  (sd.)  Y.  2p. II*'.  b)  in  andrer  Stellung,  mit  i^t: tat  nS  nat^  vanlänl  {sA.)  Y.  57.  i;  — *a%a  *naäj'''  atnim  a^rapaitim  upBissit N. //(?).  b)  schwachtonig,  hinter  dem ersten  Wort  des  Satzes:  asUta  «■  aiAkai haca  VUai  gauÜ  öuyJt  Y.  6^0.  3 ;  —  us  n' aiiihäi  vTse  JamySl  as»m^a  .  .Y.60.3;  — para  »•  ahmst  haca  asanhalca  . .  axliat . . ^■9- Sil  —  *^'i  »°  P<ira  ahmst ..  paiti. - jasätiF  .  ,  Y.g.$$;  j.^n,  F.44;  — ya'^a n'  malysha  *xh/isti  Ä?»(?(sd.)  vTiävc^einti V.2.31;  —  yavat  »'  ah  .  .  P.42{?). ai.  n«,  «M,  gr.  n>  usw.  (i.  BoM.  GrGr,3  544).  — S.  auch  nüram.  —  Pii.r  nun;  i.  noch  No.  1. — I)  S.  na-  No,  3.  ~  »)  UnEtchn;  Hds.  i
```


## [2026-09-07T19:35:31.884Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport re\npages=open('BRT.txt',encoding='utf-8',errors='replace').read().split('\\f')\npat=re.compile(r'n[üu]ram|n[üu]r[oa]m')\nfor k in range(600,615):\n    b=pages[k]\n    cols=re.findall(r'(?m)^\\s*(1[01]\\d\\d)\\s*$',b)\n    hits=[m.start() for m in pat.finditer(b)]\n    if hits: print('leaf',k,cols[:4],'hits',len(hits))\n# print nūram headword region on leaf 607+\nfor k in range(606,610):\n    b=pages[k]\n    for m in pat.finditer(b):\n        s=b[max(0,m.start()-200):m.start()+400]\n        if 'Adv' in s or 'jetzt' in s:\n            print('=== leaf',k, re.findall(r'(?m)^\\s*(1[01]\\d\\d)\\s*$',b)[:4])\n            print(s); break\nEOF"
}
```


### [2026-09-07T19:35:33.168Z] TOOL RESULT

```
leaf 606 ['1089', '1090'] hits 2
=== leaf 606 ['1089', '1090']
tiF  .  ,  Y.g.$$;  j.^n,  F.44;  — ya'^a n'  malysha  *xh/isti  Ä?»(?(sd.)  vTiävc^einti V.2.31;  —  yavat  »'  ah  .  .  P.42{?). ai.  n«,  «M,  gr.  n>  usw.  (i.  BoM.  GrGr,3  544).  — S.  auch  nüram.  —  Pii.r  nun;  i.  noch  No.  1. — I)  S.  na-  No,  3.  ~  »)  UnEtchn;  Hds.  iä%nm trvSaiuim ;  PQ. :  tlänäiHiar,  lässt  also  ttvX  aus.
•  p.  nuram"',  j.,  g.  'nurain,  j, Adv.  'jetzt,  gegenwärtig':  ysi  para  ahmSi harne  gStvS  .  .  hifhitta  .  .  äat  tl  'rqnt fravtttinti  Yt.  /J.  57  f.;  S4j  S6;  —  »ic/»  mE Java  avanhe  'rim  ml  hara  upastqm  Yt. 5.  63;  —  A
```


## [2026-09-07T19:35:39.458Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport re\npages=open('BRT.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor k in range(575,600):\n    b=pages[k]\n    for m in re.finditer(r\"nava-\",b):\n        s=b[max(0,m.start()-150):m.start()+350]\n        if 'neu' in s.lower():\n            print('=== leaf',k, re.findall(r'(?m)^\\s*(1[01]\\d\\d)\\s*$',b)[:4])\n            print(s.replace('\\n',' '))\n            break\nEOF"
}
```


### [2026-09-07T19:35:40.752Z] TOOL RESULT

```
=== leaf 583 []
  'aufs  neue':  .fu^a  xä  ..  apqm /a',inii  'ra  Yt.  Ä  5. aL  Hffia-  Adj.,  np.'r'W.  —  Pi;  näi.  —  •)  D.  L nat-a  (NPn.)  +/J  (NPn.). •  nava-karia-  n.  'durch  nenn  parallele Furchstriche  hergestellte  Abgrenzung*:  's'fm frakäravdti  Yt.  4-  6. VgU  "intarla-. •  j.  iiava.^ya-  il  "Langenausdehnung von  neun  Schritten,  neun  Schrittlängen': "krigäim  w/3ptm  'gäim  paitynpim  V.6,40. Pü.:  9  .^--i"!. •  j.  navajti^par- n.  'Zeit  lon  neun Käch- ten':  yat  hl  nai'a  xs
```


## [2026-09-07T19:35:47.634Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport re\npages=open('BRT.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor k in (582,583,584):\n    print(k, re.findall(r'\\b10\\d\\d\\b',pages[k])[:10])\nb=pages[583]\ni=b.find(\"'aufs  neue'\")\nprint(b[max(0,i-1600):i+120].replace('\\n',' '))\nEOF"
}
```


### [2026-09-07T19:35:48.896Z] TOOL RESULT

```
582 []
583 []
584 ['1050', '1050']
neu,  frisch': vurärmH  (sd.)  rivärsku  'va  (NSC)  <?/>'  .  - "ra  (NPn.stattf-)  a^viz-i  -ra  (NPn.) Äraräs.i 'vata''>  Ö.JisataJasaKsA.')\.2i.y  a)  IS. "i'd  als  Adv.  'aufs  neue':  .fu^a  xä  ..  apqm /a',inii  'ra  Yt.  Ä  5. aL  Hffia-  Adj.,  np.'r'W.  —  Pi;  näi.  —  •)  D.  L nat
```


## [2026-09-07T19:35:55.470Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== HUB nau/neu\"; grep -n \"nau\\b\" HUB.txt | head -10; echo; echo \"== HUB leaf for 1045?\"; grep -c \"\" HUB.txt; python3 -c \"\nt=open('HUB.txt',encoding='utf-8',errors='replace').read().split('\\f'); print('leaves',len(t))\""
}
```


### [2026-09-07T19:35:56.736Z] TOOL RESULT

```
== HUB nau/neu
422:schrieben sein ^) und so dem np. uifndn genau ent-
1714:424. Tax afgh. LW. jiift genau, richtig, Paar gehort
3001:sg. masc.) wurde paz. freh = np. firih genau ent-
3611:1045. Wird nau (now) gesprochen, wie die Ipt. saw, rau
4416:^) Aber np. nau *neu' = zd. nava- etc.- 127 -
4528:= np. i genau entspricht, so konnte auch noch in andern
5832:jau) H. 428: nau neu' H. 1045; sau *geh*, ipt. zu savam;
7105:y lM,8st sich nicht genau bestimmen. In altparthischer Zeit
8148:Laute genau unterscheidet, tritt hier erganzend ein.

== HUB leaf for 1045?
10983
leaves 300
```


## [2026-09-07T19:35:56.884Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== SYN NEW\"; grep -n \"^15.94 NEW\\|15.9. NEW\\| NEW$\\|NEW \" SYN.txt | head -10"
}
```


### [2026-09-07T19:35:58.164Z] TOOL RESULT

```
== SYN NEW
24410:TIME 957 14.18 NEW ; Goth. niujis Lith. naujas
```


## [2026-09-07T19:36:05.493Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"--- HUB 3605-3618\"; sed -n '3605,3618p' HUB.txt; echo; echo \"--- HUB 5828-5836\"; sed -n '5828,5836p' HUB.txt; echo; echo \"--- HUB 4412-4420\"; sed -n '4412,4420p' HUB.txt"
}
```


## [2026-09-07T19:36:05.519Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '24400,24440p' SYN.txt"
}
```


### [2026-09-07T19:36:05.567Z] TOOL RESULT

```
Av. dyu- ‘duration, age’, cf. Lat. aelas (above, 2).
lok —i-_t mp t——- BS 7 > onl
Br. With but few
exceptions the words for ‘ew’ and those for ‘young’ (14.14) be- Jong to inherited groups POUNE to IE words for ‘new’ and ‘young’ respectively. put the Grk. word of the ‘new’ group yas used chiefly, from the earliest times, for ‘young’, and the Lett. ‘young’ word serves also for ‘ew’. Furthermore, ‘young’, though primarily used of living things, is freq. applied by analogy to such objects as moon, month, and other periods of time, wine, etc. So NE young (NED s.v. 5), and similarly in other languages.
1, IE *newo- (a), *newyo- (b). Walde- P, 2.324, Ernout-M. 681.
a) Grk. véos (chiefly ‘young’, but also in part ‘new’; NG ‘new’ only in phrases like rt véa; ‘what news?’); Lat.
Sy ae the words for ‘young’ belong Y exten tited group. The others come from th Sion from ‘new’ (Grk. véos) or
© notion of ‘tender’.
*yuw en- (a), *yuwnko- (b),
Digitized by Arya Samaj Foundation Chennai and eGangotri
TIME 957 14.18 NEW ; Goth. niujis Lith. naujas
' aivos, VEO ON ngr Lett. jauns o gov 1¥05 Dan. ny ChSl.  novit ist. novus Sw. ny SCr. nov
nuovo oe OE nive Boh. novy
A neuf, 22 ME __newe Pol. nowy
nuevo NE new Russ. novyj Rum: nou aide Du. nieuw Skt. nava-, navya-~ if wield Er . OHG niuwi Av. nava- ae MHG  niu(we) V. Has NHG zeu
novus (hence the Romance words; dim. Lat. novellus > Fr. nouveau); ChSI. novi, etc., general Slavic; Skt., Av. nava-; Toch. A wu (SSS 47); b) Ir. nie (older née, naue), W. newydd, Br. nevez, and with d-suffix Ir. naide, NIr. nuadh; Goth. niujis, etc., general Gmc.; Lith. naujas; Skt. navya-.
2. Grk. xawés : Skt. kanina- ‘young’, Lat. recéns ‘fresh, recent’, Ir. cinim ‘spring from, descend’, ChSl. na-éeii ‘begin’, etc. Walde-P. 1.397f. Boisacq 391 f.
Hence, through cpd. xawvoupyns (: épyov ‘work’) ‘newly made’, xatvobpytos (5th. cent. a.p.+), in NG the pop. word for ‘new’.
3. Lett. jauns ‘young’ (14.14) also
?
‘new’.
6a 14.14 YOUNG NG. id Goth. juggs Lith. jaunas Lat, hee ON ungr Lett. jauns io Dan. ung ChSl. junit hr, he Sw. ung SCr. mlad 8p, Hote OE —geong Ha ria Rum, : ME yong ‘ol.  mlody h Ag in, june NE young Russ. molodoj, junyj NI, ig Du. jong Skt.  yuvan-, kanina- uf teuane OHG jung Av. yuvan- = Fs Mo jung
comp. *yeu-yes- fr. simple *yeu-. Walde- P. 1.200. Ernout-M. 509. Walde-H. 1.735. Falk-Torp 1334.
a) Lat. tuvenis (> Romance words; but Rum. june sb. ‘young man’, as adj.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
+ oa
Digitized by Arya Samaj Foundation Chennai and eGangotri
958 SELECTED INDO-EUROPEAN SYNONYMS
due to Fr. influence); Lith. jaunas, Lett. jauns, ChSI. junit (positive not in Gospels, but junéji = 6 vedrepos, Lk. 15.12), Russ. junyj, Bulg., Slov. jun; Skt., Av. yuvan-, ytin- (Av. quotable only as sb. ‘young man’); b) Ir. dac, dc, Nit. 69, W. iewanc, Br. yaouank; Goth. juggs, ON ungr, etc., general Gmc.; cf. Lat. iuvencus, -a ‘steer, heifer’, Umbr. tuenga ‘iuvencas’, Skt. yuvaca- ‘youth- ful’,
2. Grk. véos, orig. ‘new’ (cf. 14.13), but chiefly ‘young’ from Hom. to the present day.
3. Rum. tindr, fr. Lat. tener ‘delicate tender’, and also often ‘of tender age? (cf. tener? ‘the young, boys’), but this use strengthened by the similar develop- ment in Bulg., SCr. mlad (below). Ernout-M. 1029. REW 8645.
4, Bulg., SCr. mlad, Boh. mlady, Pol, mtody, Russ. molodoj (also OPruss, malda- ‘young’) = ChSl. mlady ‘ten- der’ (of the branch of the fig tree) : Lat, mollis, Skt. mrdu- ‘soft, tender’, ete, Walde-P. 288 f. Berneker 2.70.
5. Skt. kanina- : Grk. xauvés ‘new’, etc. (14.13).
14.15 OLD
Grk. adatés, dpxatos, Goth. fairneis, alpeis, Lith.  senas
yépwv sineigs Lett. veces NG madtés, apxatos ON forn, gamall ChSl.  vettichit, slarit Lat. velus, senex Dan. gammel : SCr. star It. vecchio Sw. gammal Boh. _ stary Fr. vieux (ancien) OE eald, gamol Pol. stary Sp. viejo ME old Russ.  staryj Rum. vechiu, batrin NE old (ancient) Skt. jirna-, sana-, vrddha- Tr. sen Du. oud Av. hana- NIr. _ aosta, crionna, sean- OHG | allt, firni W. hen MHG allt, virne Br. koz, hen- NHG alt
Most of the words for ‘old’ are used alike for ‘old’ vs. ‘new’ and ‘old’ vs. ‘young’, and this is to be understood in the following, except as otherwise noted. But a few are used wholly or chiefly in the latter sense, esp. of old persons; and this was the orig. application of many of the others, as indicated by their etym.
1. TB *sen-. Walde-P. 2.494. Er- nout-M. 922 f.
Lat. senex (of living things, mostly persons); Ir. sen, NIr. sean, W. hen (Br. hen- as prefix, as often Ir. sen- and most- ly NI. sean-); Goth. sineigs, super. sin- ista (only of persons, ‘rpecBirns, mpeoBbre- pos’); Lith. senas, Skt. (Ved.) sana- (opp. to nava- and yuvan-), sanaya-, Av.
hana- (quotable only for old persons); Arm. hin; cf. Grk. é&os ‘of last year’,
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
```


### [2026-09-07T19:36:05.575Z] TOOL RESULT

```
--- HUB 3605-3618
osset. Erzahlungen p. 62. Skr. namata- Tilz' ist LW.
1043. In phi. anaumet (sprich anomef) ist die Anlaut-
schreibung beibehalten. Np. naumed (= afgh. LW.
naurmd) ist eine neue Zusammensetzung aus na und
umU. Vgl. naumed Fird. I, 133, Z. 2.
1044. Lallwort.
1045. Wird nau (now) gesprochen, wie die Ipt. saw, rau
{soUy rou),
1046. Heisst na/vdxtan urspriinglich : streicheln, streichen,
schlagen'? Es bedeutet ein Instrument spielen (oder
schlagen), singen; schmeicheln, streicheln, liebkosen'.
Dazu auch nava 'Melodic, Gesang , arm. nuag *Melodie,
Lied*, nuagem singe, spiele ?
1047. Die Pehleviform nap (geschrieben napl Hajiab5d-In-

--- HUB 5828-5836
'Eanal, R5hre' H. 1024; nuvazdah neunzehn H. 1048, navad
neunzig'^) H. 1049; navardldan *zusammenwickeln' H. 1050;
havan *M5rser* H. 1089; yavar 'Stossel* H. 1125 u. s. w.
Auslautendes av wird au {ou) gesproclien : jan 'Gerste* (afgh.
jau) H. 428: nau neu' H. 1045; sau *geh*, ipt. zu savam;
seltener o: td = tu *du\ zd. tava. Ueber v zwischen Vokalen
siehe ferner Kap. 10.
Ebenso im Armenischen : Artavazd - zd. asavazdah-^
gr. ^Agxaovoi^dric^ lat. Artavazdes; Xosrov = pers. Xusrav,

--- HUB 4412-4420
*) Muwaffaq hat duvam *der zweite* 4, 16, 17; 5, 18 neben
say urn *der dritte' 263, 11, caharum *der vierte' 5, 9.
*) Anlaut. va- ist sonst zu ba- geworden.
*) So bei Sal. Shuk. p. 39, bei Vullers navad.
^) Aber np. nau *neu' = zd. nava- etc.- 127 -
b) Einigemal durch Assimilation an folgendes u :
ustux^an *Knochen', phi. astiix^'an zu zd. ast- 'Knochen ;
huzurg 'gross' aus ^h\,^vuzurk = *vazurk (§ 53) = ap. vazrka-;
vaxsUr = vuxmr 'Prophet' = phi. vaxSvar u. s. w.
```


## [2026-09-07T19:36:15.134Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY; grep -n \"نوید\" ARY_pages.txt | head; echo \"== نو headword\"; grep -n \"^نو \\|^نو$\\|نو (\" ARY_pages.txt | head -20; echo \"== latin index NEW\"; grep -n -i \"NEWOS\\|NEU-\\|NOW\" ARY_latin_index_pages.txt | head -10"
}
```


### [2026-09-07T19:36:16.476Z] TOOL RESULT

```
600:از این رو آینده‌ی پژوهشها وابسته به هند و اروپالیان نوید بخش است.
14923:۴ / نواء نوانیدن, نویدن (به چم "نغمه* *خواندن" *نالیدن*)
14931:فارسی (/(۳8۶14): نواء نوانیدن, نویدن (به چم"نغمه آخواندن "نالیدن)
== نو headword
67:نو موم ۱ ی
613:میانه (حدود ۱۵۰۰ تا ۱۳۵۰ پیش از میلاد) وهتیت نو (حدود ۱۳۵۰ تا ۱۲۰۰ پیش از میلاد) نوشته ..
== latin index NEW
2584:Now ENGLISH) JS NONAM, NU, NU:(SANSKRIT) <4 Suite
2593:BARNHART: (NOW) 712 NYNI (BOHEMIAN) (gos y
2595:MACKENZIE: (NOW) 125 NU MATVUN) (8) ih
2598:SEAT: (Now) 408 NU, KLNUN HITTITE) cen
2599:AMINDAROV: (NOW) 261
3490:MACKENZIE: (SNOW) 133 VAPATI, VAPRA :(SANSKRIT) 2 Sale
3502:BFS ilall (SNOW : pL S) SNAW 5545 Sil NIVIS, NIK ig) IPH sp, SSNEZA !
7621:MACKENZIE: (KNOW) 121 KAN, KUNNA
11187:BARNHART: (KNOW) 569 HOLD ENGLISH) 4S gli
11189:MACKENZIE: KNOW ENGLISH) 5 SS}
```


## [2026-09-07T19:36:22.360Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY; sed -n '2570,2605p' ARY_latin_index_pages.txt; echo \"=== pdf page tag ===\"; awk 'NR<=2605 && /\\[pdf page/ {p=$0} END{}' ARY_latin_index_pages.txt; grep -n \"\\[pdf page\" ARY_latin_index_pages.txt | awk -F: '$1<2605' | tail -3"
}
```


### [2026-09-07T19:36:23.580Z] TOOL RESULT

```
rie type Sas EPEDANOS GREER) gly
‘FA gba opts LITHUANIAN) gle) |
ieetloal
agg oy Seiler 5 29 059 onl
Rowena thon |
NU, NACH GOTHIC) S55 NU, NUREM MAVESTAN) gl)
HOLD SCANDINAVIAN) S444) NURAM — (OLD PERSIAN) skal oJ,
NO NUN PAHLAVI) 53h
NU HOLD SAXON) (pS pS NUR, NIR HOSSETIC) .go0\
NU HOLD FRISIAN) 4S 62 NIHA, NAKA (KURDISH) 53,5
(OLD HIGH GERMAN) nS gis NU, NUN (BALUCHD) > jb
NU, NU NEN AFGHANI) (¢-*),glail
NUN (GERMAN) gist NU -(TOKHARIAN A) A 5,55
no OLD ENGLISH) oS g-Sil NO, (TOKHARIAN B) B 5 55
Now ENGLISH) JS NONAM, NU, NU:(SANSKRIT) <4 Suite
NU SWEDISH) G4 yo NY, NYN, NUN, NU = (GREEK) by
NU (NORWEGIAN) 533 NUNC, NUNE, NUM, NU-:(LATIN) 33
NU (DUTCH) gece MAINTENANT (FRENCH) 4ui\
[pdf page 92]
|
AY 1 Casas Wha she’ pf 4) abel
‘REFERENCES thy OLD CHURCH SLAVIC) 5.5 s%e\
POKORNY. SSOS*~S~S~«S NYNE, NU
BARNHART: (NOW) 712 NYNI (BOHEMIAN) (gos y
DELAMARRE: = (MAINTENANT) 258 NU, NUNAI LITHUANIAN) gp}
MACKENZIE: (NOW) 125 NU MATVUN) (8) ih
BUCK: 962-963 (TEINU — (OLD PRUSSIAN) oS +3.
ONTONS: Wow) sts INDORSA (OLD IRISH) gS ga 2!
SEAT: (Now) 408 NU, KLNUN HITTITE) cen
AMINDAROV: (NOW) 261
TYP gIVIF 5 100 1 ebi dby
feetlsab
sda pl tigety & Wil OL 22 Sly cal ee
, sere ga A GIS US 32 05a onl
[MORTAL tee lyr |
UN-KUNTHS GOTHIC) S56 AMERETAT:(OLD PERSIAN) Slut) oj),
=== pdf page tag ===
2534:[pdf page 90]
2560:[pdf page 91]
2588:[pdf page 92]
```


## [2026-09-07T19:36:32.251Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY; grep -n -i \"NAVA, NAVYA\\|(NEW)\\|NEWOS\\|NAWA\" ARY_latin_index_pages.txt | head -15"
}
```


### [2026-09-07T19:36:32.302Z] TOOL RESULT

```
9706:ZA)NDAN 25 he) “ShLi3" Bedls ce shy 4 (shy hts) ZENAWAND 4(Cl 6,3) ZENABZAR
11188:DELAMARRE: _ (CONNALTRE) 257 CNAWAN, CNEOW
14600:REFERENCES boky NAMASH, NAWASH aazuce ea
14668:ONIONS: (NEW) 608 POKORNY: ae 769
14669:SkeaT: gh (NEW) 399 BARNHART: (NEW) 702
14671:MACKENZIE: *_(NEW) 125
```


## [2026-09-07T19:36:35.478Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY; sed -n '14630,14680p' ARY_latin_index_pages.txt; grep -n \"\\[pdf page\" ARY_latin_index_pages.txt | awk -F: '$1<14680' | tail -2"
}
```


### [2026-09-07T19:36:36.762Z] TOOL RESULT

```
YYVER-TYVEE hice aalicadd NJANJA RUSSIAN) .g+5,
| NENI :(BULGARAIN) 5 ,\6,
[pdf page 502]
aS VWuIOVv
orf cases
dentlsay
sh (ISO) GAT 345 29 la cal
Bap hb 6 sy OY5 22 05s cal
(OLD HIGH GERMAN) of galT NAVO, NAVA AVESTAN) gle 3)
NIUWE OLD PERSIAN) ikal go
NEU (GERMAN) glaST NEUWENEN, NAUNS
NIWE, — (OLD ENGLISH) oS 53S) NOG, NAVAK, NOK, (PAHLAVI) 5 sha
NEOWE, NIOWE NO
NEW ENGLISH) S31 NVOG, NAVAG , HOSSETIC) go 3\
NY (DANISH) Sails NU, NEU (KURDISH) 63,5
NY (SWEDISH) 548 y> NOK, NOX 4BALUCHD) gu
NY :(NORWGIAN) 5355 NAU, NAVAL, — :(AFGHANI) (24) gail
NIEUW DUTCH) gata NAWE
(OLD CHURCH SLAVIC) oA Ge! NU s(TOKHARIAN A) A 5)\05
Novo RuwWE, NUNE:(TOKHARIAN 8) B sj)
NOWY POLISH) ging’ NAvas, NAVYAS :(SANSKRIT) cy Sunile
NOVYJ, NOVIKU — (RUSSIAN) 9 NOR AREMIAN) «|
Novy CZECH) Sop NEOS, NEIOS A(GREER) gli,
NOV (SERBIAN) 9 NOVUS, NOUVARE — (LATIN) 3
Novy :(BOHEMIAN) gus 1 NOUVEAU, NEUF — (FRENCH) 413
Novy (SLOVAK) Se NUEVO, NUEVA (SPANISH) libel, gx
NADJAS, NAVAS :(LITHUANIAN) il NUOVO |. (ITALIAN) ue :
NUE MOLD IRISH) op 85 p\ Nov “EN RUMANIA) gles
NOVIO AGALISH) J NOVO, NOVA (PORTUGUESE) J 4
NEWYDD WELSH) 5) NIUJIS GOTHIC) S38
NEVEZ HBRETON) 3.352 (OLD SCANDINAVIAN) 45(5-1—\
NUADH GAELIC) SIE NYR
NEWAS HITTITE) ca NIUWL (OLD SAXON) aS pS
NIE NT (OLD FRISIAN) 6 6.)
———— |
[pdf page 503]
Coagh' oul e" Paaditgg wou Daslidy [OF
BUCK: : 987 REFERENCES hy
ONIONS: (NEW) 608 POKORNY: ae 769
SkeaT: gh (NEW) 399 BARNHART: (NEW) 702
ORs alas , seb oly DELAMARRE: (NOUVEAU) 229
MACKENZIE: *_(NEW) 125
: jeebloal
22383 gst COgSN ie 4) ANDs by *NEU> ob yh gta See aly Y glial s te zy orl
(esl gail ya" aad’ pe 44) Gangs Gasilyad ys PERSIAN) yyubb
|
| NUALL (OLD IRISH) 24S 543 ,\ NAD- 4AVESTAN) «glun)
NIWAG, (PAHLAVI) 5 shy
REFERENCES entheg NIWEYENIDAN, NIWISTAN
POKORNY, ~SO*~CS~*~CS~S~«S NEWA (RURDISH) 52,5
DELAMARRE: (CRIER) 271 NU (TOKHARIAN B) B os Js
14632:[pdf page 502]
14665:[pdf page 503]
```


## [2026-09-07T19:36:51.280Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY; sed -n '14670,14700p' ARY_latin_index_pages.txt"
}
```


### [2026-09-07T19:36:51.332Z] TOOL RESULT

```
ORs alas , seb oly DELAMARRE: (NOUVEAU) 229
MACKENZIE: *_(NEW) 125
: jeebloal
22383 gst COgSN ie 4) ANDs by *NEU> ob yh gta See aly Y glial s te zy orl
(esl gail ya" aad’ pe 44) Gangs Gasilyad ys PERSIAN) yyubb
|
| NUALL (OLD IRISH) 24S 543 ,\ NAD- 4AVESTAN) «glun)
NIWAG, (PAHLAVI) 5 shy
REFERENCES entheg NIWEYENIDAN, NIWISTAN
POKORNY, ~SO*~CS~*~CS~S~«S NEWA (RURDISH) 52,5
DELAMARRE: (CRIER) 271 NU (TOKHARIAN B) B os Js
ACKENZIE: (MELODY) 123, NAVATE, NAUTI (SANSKRIT) 2 Sie
i MALLORY & ADAMS: NUAG, NUAGEM —(AREMIAN) ya!
(ANNOUCNCE) 102 NEDA, NEDON (GREEK) gli y
AMINDAROV: (MELODY) 253| © NUNTIUS, NUNTIUM = (LATIN) 3Y
} ThAs gYIVE gtYed sabi oly NAUJU LATVIAN) (.o3),g 9)
|
| owt look
nnn they ply ig O45 22 59 al >
ets tic |
\ NAVAT, NAVAD (PAHLAVI) 5 NAVAITI AVESTAN) geo)
NUD, NEHVID, (KURDISH) 53,5 NAVATI. (OLD PERSIAN) ally gos)
=
[pdf page 504]
O90 | apy

NINETY ENGLISH) gud} NAWE, NEHVED

NEGENTIG s(DUTCH) gicla NAVE, NAWI — :(AFGHANI) (4), silat
DZIEWIECDZIESIAT (POLISH) (gl) NVIT, NAVATL. (SANSKRIT) cy Sule
DEYATDESYAT ——_-(RUSSIAN) yay, INNUSOUN ARMENIAN)
```


## [2026-09-07T19:37:03.897Z] TOOL CALL #59: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/now",
 "prompt": "Give verbatim the etymology of \"now\" (Old English forms, PIE root) and any note relating it to \"new\"."
}
```


## [2026-09-07T19:37:04.969Z] TOOL CALL #60: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/novice",
 "prompt": "Give verbatim the etymology of \"novice\", and if present on the page any of novel, nova, innovate, renovate."
}
```


### [2026-09-07T19:37:07.555Z] TOOL RESULT

```
# Etymology of "Now"

**Old English Form:** Old English *nu* "at the present time, at this moment, immediately"

**PIE Root:** PIE *\*nu* "now" (also found in Sanskrit, Avestan, Old Persian, Hittite, Greek, Latin, Old Church Slavonic, Lithuanian, and Old Irish)

**Relation to "New":** The etymology notes that the word may have originally meant "newly, recently," suggesting a possible connection to the root of the word "new." However, this is presented as speculation ("Perhaps originally...and related to the root of new").
```


### [2026-09-07T19:37:09.104Z] TOOL RESULT

```
# Etymology of "Novice"

**Novice** originates from the mid-14th century, derived from Old French *novice* meaning "beginner," which came from Medieval Latin *novicius*. This Latin term meant "newly imported, newly arrived, inexperienced," particularly when describing slaves, and stems from Latin *novus*, meaning "new."

The word initially referred to "probationer in a religious order" but expanded by the early 15th century to mean "inexperienced person, one new to his circumstances." By the 1520s, it functioned as an adjective meaning "having the character of a beginner; befitting a novice."

---

**Regarding other terms:** The page does not contain etymologies for *novel*, *nova*, *innovate*, or *renovate*.
```


## [2026-09-07T19:37:19.694Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; for u in \\\n 'https://en.wiktionary.org/wiki/%D9%86%D9%88%DB%8C%D8%AF' \\\n 'https://en.wiktionary.org/wiki/%D9%86%D9%88' \\\n 'https://en.wiktionary.org/wiki/%D8%A7%DA%A9%D9%86%D9%88%D9%86' \\\n 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/n%C3%A9wos' \\\n 'https://abadis.ir/fatofa/%D9%86%D9%88%DB%8C%D8%AF/' \\\n 'https://www.etymonline.com/word/now' \\\n 'https://www.etymonline.com/word/novice' ; do\n timeout 120 python3 tools/fetch_source.py \"$u\" --note 'page 364, root Newo/Nu: new/now, navid, aknun, English derivatives' 2>&1 | tail -2\ndone"
}
```


## [2026-09-07T19:37:22.516Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; pdftoppm -f 364 -l 364 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg364 && ls -l /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg364.png"
}
```


### [2026-09-07T19:37:24.403Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/d34aae87047dc46f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8ef258014702116d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/7344713975ed1dbc.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ba97b4fb306b1533.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0463db1df1ba3576.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5f9940ef7a312a5c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e096f88c1df69c59.txt
```


### [2026-09-07T19:37:26.210Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 49805 Sep  7 15:37 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg364.png
```


## [2026-09-07T19:37:28.943Z] TOOL CALL #63: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg364.png"
}
```


### [2026-09-07T19:37:29.300Z] TOOL RESULT

```

```


## [2026-09-07T19:37:29.298Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-07T19:37:38.859Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n 1,120p tools/verify_check.py"
}
```


### [2026-09-07T19:37:38.900Z] TOOL RESULT

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


## [2026-09-07T19:38:50.927Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== PHD nog\"; grep -n \"^nog \\|nog \\[nwk\" PHD_mackenzie.txt | head -5; echo \"== PHD nun\"; grep -n \"^nun \\[\" PHD_mackenzie.txt | head -5; echo \"== SKT new/now\"; grep -n \"^New\\.\\|^Now\\.\\|^New,\\|^Now,\" SKT.txt | head -8; echo \"== LEW novus\"; grep -n \"^novus\\|novus,\" LEW_1910.txt | head -5; echo \"== LAT novus\"; grep -n \"^novus\" LAT.txt | head -5"
}
```


### [2026-09-07T19:38:51.038Z] TOOL RESULT

```
== PHD nog
3822:nog [1l'1:ck l I 1\'1 nwg, N llfl'lv] new, recent.
== PHD nun
3827:nun [KON < A k<ll I M, J nwn] now.
== SKT new/now
== LEW novus
== LAT novus
```


## [2026-09-07T19:38:52.007Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD; python3 - <<'EOF'\nimport re\nt=open('WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('leaves',len(t))\nfor p in (324,340):\n    leaf=p+5\n    b=t[leaf]\n    print('==== printed',p,'leaf',leaf)\n    print(b[:700])\nEOF"
}
```


### [2026-09-07T19:38:53.333Z] TOOL RESULT

```
leaves 725
==== printed 324 leaf 329
                             ;




                                                   neuqs-   — neud-                                       325

nlukiaii, niuJcti, a.\xch nak-stil, -an,                       ^^vemschen, dumpfes Getose machen^*,
apsmidtikii „sich bew61keii“,                     lett.   aprauldes ds, lit. Pt. praet. apsmidukfs
„besudelt, unordentlich“.
     luscus   kann auf Grund eines Hiiq-sko „zu leuch ten anfangen, dammem“
zu                  da die ^i-Formen nicbt aus Z- herleitbar sind; s. iiber
       leiiq- „leucbten'',

noch andere Deutungen Vf. LEWb.^ s. v., Liden IF. 19, 368 Anm. 1 die                                  ;


germ. Sippe Yon mhd. Im^en „lauern, betriig
==== printed 340 leaf 345
                                                                             ;




                                                   E.

rab- Ton „Ungestum, Wut ergriffen sein"'?
   Lat. rabies                Tollheit*^, rabio^    -ere   „toll   sein,   wuten“ beruhrfc sich
in der Bed. sehr nahe mit ai. rdhhas- n, „Ungestuin, Gewalt^^, rabhasd- „mld,
ungestum, gewaltig“, sqrabdha- „wutend“ (Vanicek 233, Fick             118, 525j,
dock sind die ind. Worte andrerseits nicht zu trennen von rdbJiaie „erfa6t,
halt sich fest“       =
                    Idbhate, lambhate „erfa6i:, ergreift“, gr. Xafi^dvo), eiktjcpa
„ergreifen“ usw. („wiiteDd“ also = „angepackt, besessen, ergriffen", vgl. mir.
re
```


## [2026-09-07T19:39:02.559Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD; python3 - <<'EOF'\nt=open('WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor leaf in (328,344):\n    b=t[leaf]\n    print('==== leaf',leaf)\n    print(b[:1400])\n    print('...')\nEOF"
}
```


### [2026-09-07T19:39:03.854Z] TOOL RESULT

```
==== leaf 328
                                                                                                              ,




324                                            ne^os, -los   — neuq-
  Ygl.     bes.    Brugmann          IF. 13,       153 (der auch neuqs- „wittern“ anreihen
will,doch s. d.).
   Ganz bedenklich            ist    die   Yermutung (Prellwitz u. vovg),                   dafi   etwa von
j.gedankenvoll nicken^^ aus auch anzureihen sei gr. voog, vovg „Sinn, Yer-
st:and“, voso) „nehine wabr, gedenke'*' (wozu Brugmann IF. 19, 2I3f., auch
m-vvTog  jjVerstandig^' usw, stellen mochte, doch s. u. pen „erforschen‘*,
und IF. 30, 37 If. ansprechender), sowie gortyn. vvvajuai ,,kann“ (als „ver-
stehe mich worauf').     Andrerseits ist freilich fiir vovg auch die Yerbindung
mit  got. sniitrs,  aisl. snotr, ahd. snotiar „weise, klug'^, nhd. mdartl.
schnodderig „altklug, vorlaut“ (L. Meyer KZ. 5, 368, Hirt Abl. 120     gegen                       —
dessen Heranziehung von dt. sinnen unter "^sencuo- s. Yf. LEWb. u. sentio                                 —
Prellwitz ^       s. v.)   kaum (von den bei Feist G\Yb. 243 erwahnten
                                     richtig
Deutungen ist Grienbergers SBAk.Wien 142, YIII 195 Zsstellung mit ahd.
snusen „schneuzen'' beachtenswert, vgl. vir emnnctae naris),

iienos, “ios „neu“.
   Ai. ndva-, av. nava- „neu'‘, gr. veog, lat. novas,          
...
==== leaf 344
340                                         nog^o- Oder uag^o-   — nu-

483 ala s-Pormen mit anguis usw. verbunden) s. z. B. Kluge 8, 401, Falk-
Torp u. snog ( ahd. snachan „kriechen'‘, nir. snaighim „krieche'').
                         :




  Peterssons IF. 23, 392 f. Gdwz. nog^ „schaben“ hat keine Gewahr.

nog"o- Oder nagHo- „Baum“?
   Ai. naga- m. „BauiD, Berg“ aisl. nqlckui m., ahd. nahho, as. naco, ags.
                                                   :




naca „Nacheii‘‘, urspr. „Einba\iiii^‘ ? Liden Stud. 31 f. (gegen Verb, der germ.
Worte mit nati- „Schiff'')» Aber lit. nogna „Heft des Schwertes“, ndglas
(noklas) „Degengriff‘' kaum als „Holz“ hieher.
   TJnter Ausscheidung you ai. naga- verbindet Petersson IF. 23, 392 ff.,
24, 259 Nachen^ nogna, ndglas mit apr. nognan „Leder“ (doch s. naq- „Feir‘),
lat. novacula „Schermesser“ (doch s. Ices „kratzen''), ve^gog „Hirschkalb'‘
(sei „UDgehoriit“ aus „glatt, abgeschabt“) und idg. nog]^- „nackt‘' nicht uber-
zeugend unter einer lediglich konstruierteu Gdbed. „schaben“,
   Unhaltbar iiber Nachen Zupitza Gutt. 92.

not-, not- „Hinterbacke, Hinterer, Iiiicken“?
  Gr. v&Tog, vcorov „Eucke]i“, ablautend mit lat. natis, meist pi. nates „Hmter-
backe, Hinterer“? (Curtius 320).     Sehr unsicher got. notin d. sg. „Schiflfs-
hinterteiP        {-t-       aus        Ficklll^ 298; andere Versuche verzeichnet
                         
...
```


## [2026-09-07T19:39:09.712Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD; python3 -c \"\nt=open('WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nb=t[344]; i=b.find('nu-')\nprint(b[-1800:])\""
}
```


### [2026-09-07T19:39:10.972Z] TOOL RESULT

```
 34, 225, LUA- 1916, 30 f.) s. Charpentier IF. 35, 256.

nu- „nun“ und ahnliche Formen.
   Ai. nU, av. nu „nun“,                  ai.   nftfana- „jetzig, jung, neu“   nilndm „jetzt, nun‘‘
(wie      nunal, aksl. nyne wohl adv. erstarrter Kasus eines Adj. ^riU-no-
       lit,

„jetzig“) av. nUrom, niirqm, ap. niiram ds. (nach surom „fruhmorgens“ ge-
bildet? Oder in Be*, zu veagog, arm. norfy, gr. vv, vvv, vvv ,.jetzt'' (letztere
YTohl aus ^nU-m =) lat. nam „nun noch, noch jetzt“,                       dann Stiitze fur Fragen
(Lit. bei Vf.      LEWb.^ s. v., etian^mim „noch imraer“, 'imnc ,.jetzt, nun“ (^num-
ce),  woneben nu noch in midius iertius *„nun ist der dritfce Tag"'; (fiber
air.          w
             -5 mcymr.        Yerbal-Partikel, s. u, ne „nicht“); got. nu {nfiT)
aisl. ahd. ags. nU ,.jetzt, nun", mhd. nhd, nU^ seit spatmhd. Zeit erst auch

nm (zur Erklarung s. Brugmann II ^ 3, 99 Iff.): lit, nil, lett. nu „nun‘-, apr.
in tei-nu „nunmehr“ (s. Trautmann Apr. 447), lit. nunai „nun“ (s. o); abg.
m „aber“, nym „nun“                     (s. o.).

  Fur got. nauh „noch“ macht Brugmann Dem. 66 Anm., IF. 33, 174f. die
Auffassung nduh [^noii-q^e) wahrscheinlich, wozu ahd. as noh „noch“ mit
Kurzung aus ^noh (vgl. got, pduh ahd. doJi); mit letzterem ist wohl wieder
                                                       :



ahd. as. noh „neque“ identisch (s. Brugmann II ^ 3, 1 005).
  Idg. nu ist wohl Tiefstufe zu neiw- „neu“, vgl. ai. mitane- ,,jetzig*^ und
„neu“; weitere Yerwandtschaft mit dem Pron.-St.no (z. B. Fick I^ 100,
Persson aaO.) ware denkbar.
  Vgl. Curtius 318 f., Osthoff MU. lY, 272, Schmidt PL 219 Anm., Kretsch-
mer KZ. 31, 337, 365, Bechtel Hptprobl. 149ff., Persson IP. 2, 206, 238 Anm.
1, 251 ausfiihrlich (auch zur Yerwendung) Brugmann II ^ 3, 991 ff.
```


## [2026-09-07T19:39:17.491Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== SKT\"; grep -n -i \"NEW\\. *(E\\.)\\|NEW\\.\\s*A\\.S\\|NEW, adj\\|^NEW\\b\" SKT.txt | head -8; grep -n \"NOW\\.\" SKT.txt | head -5; echo \"== LEW keys\"; grep -n -i \"novus\" LEW_1910.txt | head -5; grep -n -i \"novus\" LAT.txt | head -5"
}
```


### [2026-09-07T19:39:17.581Z] TOOL RESULT

```
== SKT
32:NEW  YORK HARPER   &    BROTHERS.    PUBLISHERS
12254:New;  see  Nov.
12256:New&ngled,  News  ;  see  Now.
12478:new£(Ln£led,  fond  of  novelty.  (E.) The  d  has  been  a>:)dcd.  M.  £.  rtrwe/angtl, t.  e.  fond  of  what  is  new.  Compounded  of nruv,  new,  vtd/ang^/,  ready  to  catch,  from A.  S.  /angm,  pp.  of  /it«,  to  catch.  The Buflix  •//  is  the  same  as  in  A.  S.  tpnc-oly (ond    of    speflking,    talkalive^    &c.     See
17306:Sinew.  (E.)  M.  E,  sinen^e.  A.  S.  tinn. 4-Du.  (^vrmf ;  Dan.  x^n^;  Sytc6.  stna\  G. tfhnt;  also  IceL  sin,  lit.  'that  which binds ;  *  cf.  Skt  si,  to  bind.
21524:WINNOW.
== LEW keys
```


## [2026-09-07T19:39:27.252Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; ls -l LEW_1910.txt LAT.txt SKT.txt FSD_vol3.txt WEB.txt 2>/dev/null; echo; grep -n -i \"novus\\|nouus\" LEW_1910.txt LAT.txt | head; echo \"--- LEW sample\"; sed -n '1,5p' LEW_1910.txt; echo \"--- nov in LEW\"; grep -n \"^nov\" LEW_1910.txt | head"
}
```


### [2026-09-07T19:39:27.338Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 13277749 Sep  4 14:06 FSD_vol3.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  4618386 Sep  4 14:06 LAT.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   627390 Sep  4 14:06 LEW_1910.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  2656202 Sep  4 14:06 SKT.txt

LAT.txt:121:adjectifs essentiels comme nouus, uetus, priscus, iuuenis,
LAT.txt:265:De m$me, des adjectifs comme nouus et uetus, iuuenis et
LAT.txt:6471:de nouus, cre 4 peut-etre d'aprfes aestas-, autumnalis (atteste des
LAT.txt:8612:qui eat la formation normale des abatraits en -tds, cf.nouus, nouitds,
LAT.txt:16342:denuo: r.nouus.
LAT.txt:40055:nouus suitur, P.F.i3i,i8. Sans antre exemple. La glose de Scaliger,
LAT.txt:41970:son homonymie avec le d£nominatif de nouus , oa, suivant 1'hypothbse
LAT.txt:41985:noufilis: v. nouus .
LAT.txt:42019:nouus
LAT.txt:42040:(v. nouus) *enses,-idis (cf. insideS, et obses, praeses)', le changement
--- LEW sample
eae hee ne
ee
Duquesne University:
joe Kt re |
* ee . ¥
--- nov in LEW
4398:nove IL 391
4414:nove (aéol.) I 103, IT 748
7486:nov. n (air.) IT 179
```


## [2026-09-07T19:39:30.094Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '42019,42045p' LAT.txt"
}
```


### [2026-09-07T19:39:30.141Z] TOOL RESULT

```
nouus
-is m. : neuf as, Varr., L.L. 5 , 169•
Nouem fournit aussi le premier terme des multiples: nondgintd: quatre-
vingt-dix, M.L.5953, qui a donne de nombreux derives: nonagenarius,
nondgeni, nSnagesimus, nondgessis, nonagies; nongenti,-ae,-a ( nonin¬
genti ): neuf cents; d'ou nongenarius noningentenarius , etc.
Nouem repond exactement a iri. noin, got .niun, skr. nava, zd nava,
et, avec prothese et alteration secondaire, a gr. evvea. L'ordinal
nonus a. n, a. Ia diff 4 rence de dec imus j ceci montre que la nasale
finale du non de nombre "neuf" etait n et non m; et, en effet, le
vieux prussien a newints "neuvieme" en face de dessimts "dixieme";
l'« du celtique (iri. nomad, etc.) et de 1 1 indo-iranien (skr. navamdh,
etc.) est analogique. Comme la formation de septimus, octduus, decimus,
le type de 1 'ordinal nSnus est plus ancien que les formes a suffixe
-to- des dialectes de la region centrale, v. pruss. newints, got .niunda,
hom. ev(F)a.TOC.
Sur le second element de nundinus, v. dies.
Nouensidgs, Nouensiles: ^pithote appliquee a une categorie de
dieux, qu'on oppose aux di Indigetes, et qui, d f apres Varron, L.L.
5,74, serait d'origine sabinp: Feronia, Minerua, Nouensides a Sabinis',
cf. le marse nouesede. Fouensides est peut-etre un compose de nou-
(v. nouus) *enses,-idis (cf. insideS, et obses, praeses)', le changement
de d en l, que l'on donne souvent comme "sabin", est peut-etre sim-
plement du a 1'influence du suffixe en -ilis et les ad j. en -ensilis.
La forme la plus ancienne est en -ides (Varr.); Nouensiles n'apparait
qu'a partir de Tite-Live.
nouerca, -ae f.: seconde femme prise par un veuf, belle-mere,
```


## [2026-09-07T19:39:34.006Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"^nouus, -a, -um\\|^nouus,\\|nouus, -a\" LAT.txt | head; echo ---; awk 'NR>=42060 && NR<=42130' LAT.txt | grep -n \"nouus\" ; sed -n '42046,42120p' LAT.txt | head -80"
}
```


### [2026-09-07T19:39:35.242Z] TOOL RESULT

```
42060:nouus,-a,-um: nouveau, neuf; au superlatif nouissimus "le der-
---
1:nouus,-a,-um: nouveau, neuf; au superlatif nouissimus "le der-
38:a commence a s'employer avec le sens de nouus, d'ou le titre de Nouel-
50:ves nouvellement aequis. Renforcement de nouus au dire d'Alfenus
53:Nouicius est a nouus comme empticius (qui 8'emploie egalement
maratre. - Attest^ depuis Pl. (Ps.314). Conservi seulement en mac< 5 donien
nuearca, cf.M.L.5970 ndvSrca. La graphie tardive nouarca a subi sano
doute l f influence de mots grecs comme monarca.
Derivas: nouercalis (postclass.); nouercor,-ari: se conduire en
belle-mbre (Sid.).
Sans doute de nouer(i)ca, derive de nouus, cf.gr.ve(F )apo£ et
uitricus de *uit(e)ricus et patricus . L'etymologie qui suppose nouerca
form<? sur un imaginaire *materca tire de matercula est invraisemblable,
matercula etant derive directement de mater avec le suffixe de dimi-
nutif -colo—, et jamais les sujets parlants n'ont pu concevoir 1’idee
d'un mot *materca. - M.Otrebski, Eos, 33 (ly^y), p.371 et suiv., dmet
une autre hypothese.
V. nouus .
noulcius: v. le suivant.
nouus,-a,-um: nouveau, neuf; au superlatif nouissimus "le der-
nier", souvent substantive. - Usit 4 de tout temps; panroman. M.L.
597 »«
Derives et composes: nouitds', nouo,-as "innover" et "renouveler"
puis "changer" dans la 1 . politique n. r£s, ou siraplement nouare
"changer le regime"; dans la 1 . rustique: nouStus ager "champ laboure
de nouveau", cf. gr. veocoo, veaxoC; dans la 1 . de la rhetor, nouare uer-
ba "creer de nouveaux mots". Composes: innouS, innoudtiSj renouo,
M.L.7313; renoudtid, -tor, -tiuus', renoudmen (Ov.); nouilUnium (Vulg.).
Nouius,-i, prenestin Nouios CIL I 8 561 m.: nom propre, surtout
suditalique. Les 1 . romanes supposent aussi un nom commun nouius
"nouveau marie" et "fiance", M.L.S 97 1 »794
ndx
nuper, sans doute anci en adj., cf. Pl., Cap.? 1 ^, recens captum hominem,
nuperum, nouicium; de *nouo-paros (cf. pauper), dont le no m.nuper,
comme deinceps , a'est cristallise dans 1'emploi adverbial avec le
sens de "nouvellement, recemment" (peut - etre d'aprbs semper). Toutefois
nuper peut etre un ancien adverbe, formi de nu + per, v.num, et 1'ad-
jectif plautinien formi analogiquement sur pauper . De nuper il existe
un superlatif nuperrime (Cic., Rhet. ad lier.), sur lequel a sans doute
ete cree le superi, de 1 *adj. nuperrimus.
dSnud, de de nouo , cf. gr. ex xcxi,vt}S, "de nouveau", e.g. Pl.M0.117,
aedificantur aedes totae denuo, puis "une seconde fois", et, comme
rursus, "en sens inverse". Souvent joint expletivement a des verbes
en re-: Pl.P0e.79, reuortor rursus denuo Carthaginem,
noudlis adj.: terne de la 1. rustique (cf.arudlis, riu&lis, dualis),
cf. Varr., L.1.5,39: ager restibilis qui restituitur ac reseritur quot¬
quot annis; contra qui intermittitur, a nouando, noualis: substo
noualis (terra) f. ou noudle (solum) n.: novale, jachere; cf.gr. veios
et ses composes. Demeure dans les 1 . romanes, M.L.59CC. Une parente
avec nouacula est peu vraisemblable (cf. noudtus).
nouellus : diminutif usite surtout dans la 1. rustique (cf.uetulus,
dans Pl.As.340 asinos... uetulos; Cic.Lael.C7 equis... uetulis; Fin.
5,39 uetula arbor oppose a nouella), ou il 8’applique aux animaux et
aux plantes: n. capra, Varr., R.R.2,3,2; nouellae uineae , id., ibid.
1,31,1; nouella, -ae (sc. uitis) "nouvelle vigne", cf. roumain nuia
11 j eime branche". Ce n'est qu'a basse epoque sous 1 'Empire que nouellus
a commence a s'employer avec le sens de nouus, d'ou le titre de Nouel-
lae (scii, constitutiones) et la creation de nouellitas par Tertullien;
de nouella provient le britt.nwaIZ. Nouellus a conserve son premier
sens dans certains dialectes romaons, ainsi logoud. noe$t}u "jeune boeuf",
a coti du sens giniral de "nouveau", qu'atteste le franvais par ex.,
cf. M.L.59C7. Les derives ont tous un sens technique: nouellUster
(-trum 1linum "vin nouveau"), nouelletum: piant de vignes nouvelles
veocpuxetov; noue Ilo,-as: planter de nouvelles vignes; et renouello
(Coi.).
Cf. aussi le non propre osque Niivellum "Nouellum", a cote de Ndla
et de Nuvlanus = NSlanl.
nouici.us: novice. Autre terme technique; se dit surtout des esclar
ves nouvellement aequis. Renforcement de nouus au dire d'Alfenus
ap. Geli. 7 , 5 ,1. Substantivi nouicium (sc .uerbum) n.: innovation dans
le langage, nouveauti. M.L.S 97 oa J nouiciolus (Tert.).
Nouicius est a nouus comme empticius (qui 8'emploie egalement
d' esclaves, cf. Pitr. Sat .47,12), suppos i tic ius sontia emptus, suppo¬
situs ; sur cette formation, v. Stolz-Leumann, Lat. Gr.°, p.194.
Nouus ripond a gr. veoC (de veFoc), skr. navah, av. nava-, v.sl.
novil, lit. navas . Le nom propre Nouius ripond h. iri. nue, geXl.newydd
( gaul. Novio-), got. niuj is , lit. naujas, skr. ndvyah, gr. ion. veioC. Dans
nouerca, il y a un dirivi d*un dirivi en —ro—, marquant opposition
de deux; on a de meme gr. veotpoS, et, en arminien, nor (gin .noroy)
est 1 'adj ectif sigr.ifiant "nouveau". Le dirivi veoxqC est fait comme
```


## [2026-09-07T19:39:43.097Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"recent\\.  (E\\.)\\|NOV,  new\\|^Nov\\b\\|neos,  new\\|veo?,  new\" SKT.txt | head -10; echo ---; grep -n \"Novel\\.\\|Novice\\.\\|Nova\\.\" SKT.txt | head -8"
}
```


### [2026-09-07T19:39:43.182Z] TOOL RESULT

```
---
```


## [2026-09-07T19:39:47.616Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i \"novice\" SKT.txt | head -6; echo ---; grep -n -i \"new, adj\\|new, recent\\|Teut. type \\*niwjoz\\|niwjoz\\|nuwe,  niwe\" SKT.txt | head -8"
}
```


### [2026-09-07T19:39:47.677Z] TOOL RESULT

```
12481:novice,  a  beginner.  ( F,  —  L. )  F.  novict. —  L.  moMt'^ius,  itauitius,  new,  fresh,  a novice.  wL.  ncuus,  new.  Der.  noviti-aiet from  F.  fwvitmf,  'the  estate  of  a  novice/ Cot.,  from  Low  L,  ncuidatus,  sb.
14724:Jan.  aprrndit)  is  from  Low  L. r.  a  learner  of  a  trade,  a  novice.
19763:Tiro,  Tyro,  a  novice.  (L-)  L.  tire,  a novice,  recniit  %  The  nsual  spelling wilh^  is  absurd.
---
```


## [2026-09-07T19:39:54.715Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '12470,12485p' SKT.txt; echo \"=== now ===\"; grep -n \"now,  at  this\\|Now,  at\\|now,  adv\" SKT.txt | head -5"
}
```


### [2026-09-07T19:39:54.775Z] TOOL RESULT

```
ice. •Gk,  vto-v.  new;  ^vr-^v,
.  |^*wt>,  from  ^««y,lo  grow,
Allied  to  Be.
.*tl    (L -Gk.)    L.   Mott'
r»vr«^mff,    novel.   —  Gk.
iparstive  of  Woi,  new;   sec
M.  E.  MTUv;   A.  S.   mhv4.
ntfiwe.  ^  ^"*  "'Vmw,  Icel.  iiyr,  Dan. Swcd.  ir^,  Goth,  ftiujisy  G.  m/m,  L.  iuk^nj, W.  ttcivydd,  Irish  and  Gael.  nuaJh,  Lithnao. fUxujsUi  Kuss.  ftffvuii,  Gk.  Wor,  Skt.  nm/a, ncwr,  Cf.  Skt.  ntitana,  new.  All  from base  NU,  i.  e.  now ;  n<w  means  '  that  which is  now,"  rccciiL
new£(Ln£led,  fond  of  novelty.  (E.) The  d  has  been  a>:)dcd.  M.  £.  rtrwe/angtl, t.  e.  fond  of  what  is  new.  Compounded  of nruv,  new,  vtd/ang^/,  ready  to  catch,  from A.  S.  /angm,  pp.  of  /it«,  to  catch.  The Buflix  •//  is  the  same  as  in  A.  S.  tpnc-oly (ond    of    speflking,    talkalive^    &c.     See
news,  tidings,  (£.)     Formerly  newes,  s.      ^| pi.,  liL  new  things,  first  used  aboat  a.  d.      ^| 1500.     It  is  a  tra.ns1ation  of  F,  iMifSv/Aei, news,  pi.  of  O.  K.  ntnv/,  new.
novel  (K.  -  L.)  O.  F.  navri  (F. ffnwtvdM),  —  L.  n^nuUus,  new,  dimiu,  of H^wMj.new.  Seenew(above).  'Dvt,nffvtt'ty^ from  O.  F.  twvtiittitt  from  L.  ace.  nouefii- tattm,  newness.
novice,  a  beginner.  ( F,  —  L. )  F.  novict. —  L.  moMt'^ius,  itauitius,  new,  fresh,  a novice.  wL.  ncuus,  new.  Der.  noviti-aiet from  F.  fwvitmf,  'the  estate  of  a  novice/ Cot.,  from  Low  L,  ncuidatus,  sb.
renew.  (L.  and  E.)  From  L.  rt- again ;  and  E.  N<rw.
renovate.  (L.)  From  L.  rtncuatux, pp.  o(  renouarf,  to  renew.  —  L.  «-,  again  ; MiTtiUJ,  new.
Noway,  Noways.  Nowhere,  No- wise; see  No  (i).
Noxious.  (L.)  L.  noxiui,  hurtful.  * L.  ncxa,  hurt.  —  L.  noftrtt  10  hurt ;  cf.  n^:x, destruction.     (VNAK.)
=== now ===
```


## [2026-09-07T19:40:25.316Z] AGENT

Now I'll write the verification file.


## [2026-09-07T19:45:50.899Z] TOOL CALL #76: Bash

```json
{
 "command": "python3 - <<'PYEOF'\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\n\ndef n(**kw): return kw\n\nentry = {\n \"entry\": 0,\n \"root\": \"Newo / Nu\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *néwos 'new' (Pokorny 769) beside its ablauting zero-grade adverb *nu 'now' (Pokorny 770)\",\n \"note\": (\"The root box is correct on all three counts. Pokorny 769 has 'Root/lemma: neuos, -ios — Meaning: new' \"\n   \"(Old Indic nava-, Avestan nava-, Gk. ve(F)os, Lat. novus, Goth. niujis, OE nīwe …), and Pokorny 770 has \"\n   \"'Root/lemma: nu- — Meaning: now' (Skt. nu/nū, Av. nū, Av. nūrəm/nūrąm, OP nūram, Gk. νυ/νῦν, Lat. num/nunc, \"\n   \"Goth. nu, OE nū …). Pokorny himself joins the two exactly as Nourai's double box does: 'Indo Germanic nu is \"\n   \"probably zero grade to neuo- \\\"new\\\", compare Old Indic nūtana- \\\"present, current\\\" and \\\"new\\\"' (POK 770), and \"\n   \"Walde-Pokorny II 340 says the same ('Idg. nu ist wohl Tiefstufe zu neuo- \\\"neu\\\"'). Watkins' AHD list is even \"\n   \"more explicit: 'newo-. New. Related to nu-.' and 'nu-. Now. Related to newo-.' The label 'Indo-European' and \"\n   \"the glosses 'new' / 'new time, now' are therefore right; the only quibble is the spelling of the reconstruction \"\n   \"(Nourai's 'Newo/Nu' for *néwos / *nu, without the *-s and the accent). \"\n   \"Layout note on the printed page: to the right of the Old Persian nūram box there is an EMPTY box with an arrow \"\n   \"running into it (no language label, no words) — an artefact of the book's layout; the extraction correctly \"\n   \"produced no node for it. The running head prints 'Newo | Newo'.\"),\n \"note_fa\": (\"ریشهٔ هندواروپایی آغازین *néwos «نو، تازه» (پوکورنی، ص ۷۶۹) و صورت بی‌درجهٔ (تهی‌درجهٔ) آن *nu «اکنون» \"\n   \"(پوکورنی، ص ۷۷۰). پیوند این دو ریشه ساختهٔ نورایی نیست: خودِ پوکورنی می‌نویسد که *nu به احتمال زیاد درجهٔ تهیِ \"\n   \"*neuo- «نو» است و والده‑پوکورنی (ج ۲، ص ۳۴۰) و واتکینز در پیوستِ ریشه‌های هندواروپاییِ AHD («newo-. New. \"\n   \"Related to nu-») نیز همین را می‌گویند. پس عنوان زبان (هندواروپایی) و هر دو معنی درست است و ادعای نورایی در \"\n   \"کادر ریشه پذیرفتنی است؛ تنها ایرادِ کوچک، شکلِ آوانگاریِ ریشه است که باید *néwos / *nu نوشته شود.\"),\n \"sources\": [W+\"Reconstruction:Proto-Indo-European/n%C3%A9wos\", \"https://www.etymonline.com/word/now\"],\n \"ref_check\": [\n   {\"ref\": \"POK:769\", \"status\": \"supports\",\n    \"note\": \"POK_full.txt line 62953 ff.: 'Root / lemma: neuos, -ios … Meaning: new … Old Indic nava-, Avestan nava- \\\"neu\\\" … gr. v£(F)oc;, Latin novus … Gothic niujis, Old English nTwe … References: WP. II 324 … Page(s): 769'. Exactly Nourai's root and gloss.\"},\n   {\"ref\": \"POK:770\", \"status\": \"supports\",\n    \"note\": \"POK_full.txt line 63139 ff.: 'Root / lemma: nu- … Meaning: now … Avestan nu \\\"now\\\" … Avestan nuram, nurqm, ap. nuram … Page(s): 770', and 'Indo Germanic nu is probably zero grade to neuo- \\\"new\\\"' — i.e. Pokorny licenses the combined 'Newo / Nu' box.\"},\n   {\"ref\": \"AHD:1531\", \"status\": \"supports\",\n    \"note\": \"The 1975/76 New College appendix page cannot be opened (lending-only scans), but Nourai's AHD is Watkins' root list, and the 1985 standalone edition (AHD_watkins1985.txt line 787) has 'newo-. New. Related to nu-. …' and (line 792) 'nu-. Now. Related to newo-. 1. Old English nū, now: NOW. 2. Latin nunc … [Pok. nu- 770.]' — the same two roots, same relation.\"}],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"pp. 769 (neuos, -ios) and 770 (nu-)\", \"stance\": \"supports\",\n    \"note\": \"grep -n 'lemma: neuos' / 'lemma: nu-' POK_full.txt; the nu- entry ends 'References: WP. II 340, WH. II 186 ff., Trautmann 201.'\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. II p. 324 (neuos, -ios) and p. 340 (nu-)\", \"stance\": \"supports\",\n    \"note\": \"incoming/WLD/WLD_Bd2_pages.txt leaf 328: 'iienos, \\\"ios „neu\\\". Ai. ndva-, av. nava- \\\"neu\\\", gr. veog, lat. novas'; leaf 344: 'nu- „nun\\\" und ahnliche Formen. Ai. nū, av. nu „nun\\\" … av. nūrom, niirqm, ap. niiram ds. … Idg. nu ist wohl Tiefstufe zu neiw- „neu\\\"'.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. newo- and nu-\", \"stance\": \"supports\",\n    \"note\": \"'newo-. New. Related to nu-. 1. Suffixed form *new-yo- in Germanic *neuja- … 2. Basic form *newo- in Greek newos, neos … 4. Basic form *newo- in Latin novus'; 'nu-. Now. Related to newo-.'\"},\n   {\"src\": \"SYN\", \"where\": \"Buck §14.13 'NEW', p. 957\", \"stance\": \"supports\",\n    \"note\": \"'1. IE *newo- (a), *newyo- (b). Walde-P. 2.324, Ernout-M. 681 … Skt., Av. nava-; Toch. A ñu … Goth. niujis, etc., general Gmc.; Lith. naujas' (SYN.txt line 24410 ff.).\"},\n   {\"src\": \"IEC\", \"where\": \"Mann pp. 843-844 (neuos) and 855 (nú, nūn, nūnai)\", \"stance\": \"supports\",\n    \"note\": \"'neuos (neuios, neuiios) \\\"new\\\". (Cf. nu, nün, neuáio, etc.) WP II, 324 Skt. navah … Av. navo, id. Per. nau, id.' (leaf 471 = pp. 843-844); 'nú, nün, nūnai \\\"so, now, well, then\\\" … Skt. nu, nū, nünam \\\"now\\\"; Av. nü, id.; Per. cf. ka-nün, ak-nün, id.' (leaf 477 = p. 855).\"}],\n \"nodes\": []}\n\nnodes = entry[\"nodes\"]\n\nnodes.append({\n \"id\": 1, \"lang\": \"Avestan\", \"words\": \"nava 2; nŭ, nŭrem\", \"verdict\": \"confirmed\",\n \"derivation\": (\"Both Avestan forms are real and correctly glossed. Av. nava- adj. 'neu, frisch' (Bartholomae, \"\n   \"Altiranisches Wörterbuch col. ~1046-1048, where he adds 'ai. nava- Adj., np. nau') is the regular Iranian \"\n   \"reflex of PIE *néwos: PIE *e > Indo-Iranian a, *w kept before a vowel, thematic *-os > Av. -a. Nourai's '2' is \"\n   \"his own homonym index, distinguishing this nava- 'new' from nava- 'nine' (< PIE *newn̥), which is the right \"\n   \"distinction to make — Bartholomae likewise has two nava- headwords. The adverbs are the zero-grade *nu: Av. nū \"\n   \"'jetzt, nun' (Bartholomae col. 1089-1090, 'j., g. nū Adv. \\\"jetzt, nun\\\" … S. auch nūram. — Pahl. nūn') and the \"\n   \"extended Av. nūrəm / nūrąm 'jetzt, gegenwärtig' (col. 1090, entered together with OP nūram). Nourai's 'nŭrem' \"\n   \"renders nūrəm with e for schwa, his standard practice, so the form is right; the breve on ŭ stands for his long ū. \"\n   \"Kent explains the -ram as taken over from *dūram 'long', i.e. nū + -ram.\"),\n \"derivation_fa\": (\"در اوستایی دو ستاکِ جدا از این ریشه هست و هر دو در کتاب درست آمده است: nava- «نو، تازه» \"\n   \"(بارتولومه، فرهنگ ایرانی باستان، ستون ۱۰۴۶ به بعد، با یادکردِ «فارسی نو nau») که بازماندهٔ قاعده‌مندِ \"\n   \"*néwos هندواروپایی است (e هندواروپایی در هندوایرانی به a بدل می‌شود و w میان‌واکه‌ای برجا می‌ماند)؛ و \"\n   \"قیدِ nū «اکنون» با صورتِ گسترده‌ترِ nūrəm / nūrąm «اکنون، در حال حاضر» (ستون ۱۰۸۹–۱۰۹۰) که همان درجهٔ \"\n   \"تهیِ *nu است. عددِ «۲» پس از nava نشانه‌گذاری خودِ نورایی برای جدا کردن این واژه از nava- «نُه» است و \"\n   \"درست است. آوانگاریِ «nŭrem» همان nūrəm است (ə را با e نوشته‌اند). ادعای نورایی در این کادر درست است.\"),\n \"sources\": [W+\"Reconstruction:Proto-Indo-European/n%C3%A9wos\"],\n \"ref_check\": [\n   {\"ref\": \"POK:769,770\", \"status\": \"supports\",\n    \"note\": \"POK 769 lists 'Avestan nava- \\\"ueW\\\" [neu]' under *neuos; POK 770 lists 'Avestan nu \\\"now\\\" … Avestan nuram, nurqm' under *nu-.\"},\n   {\"ref\": \"KLN:1059\", \"status\": \"partial\",\n    \"note\": \"KLN_1966.txt leaf 566 carries printed pp. 1058-1059, and p. 1059 is s.v. 'now': 'now, adv. — ME. nou, nu, fr. OE. nū … cogn. with OI. nu, nū, nūnam, Avestic nū, OPers. nūram, Toch. nu, Hitt. nuwa \\\"now\\\"'. So the cited page supports the nū/nūrəm half of the box; Klein's Avestan nava- ('Avestic nava-, ModPers. nau') stands on p. 1044 s.v. 'new', not on 1059.\"},\n   {\"ref\": \"KNT:194\", \"status\": \"supports\",\n    \"note\": \"KNT.txt leaf 217 (printed p. 194, the page number '194 OLD PERSIAN' running head is on the leaf): 'nūram adv. \\\"now\\\": Av. nūrəm; from pIE *nū \\\"now\\\" (Av. nū, Skt. nū, Lt. nu-nc, NEng. now) + final of (pAr.) *dūram \\\"long\\\"'.\"},\n   {\"ref\": \"IEC:854\", \"status\": \"partial\",\n    \"note\": \"Mann's relevant entry 'nú, nün, nūnai \\\"so, now, well, then\\\" … Av. nü, id.; Per. cf. ka-nün, ak-nün' is on p. 855 (IEC.txt leaf 477 = pp. 855-856), one page after Nourai's 854; his 'neuos' entry is on pp. 843-844. Content supports the box, the page number is off by one.\"}],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"col. ~1046-1048 s.v. nava- ; col. 1089 s.v. nū ; col. 1090 s.v. nūram/nūrəm\", \"stance\": \"supports\",\n    \"note\": \"BRT.txt leaf 583: '… \\\"neu, frisch\\\" … nava- Adj., np. nau'; leaf 606: 'j., g. nū Adv. \\\"jetzt, nun\\\" … S. auch nūram. — Pahl. nūn' and 'p. nūram, j., g. nūrəm, j. Adv. \\\"jetzt, gegenwärtig\\\"'.\"},\n   {\"src\": \"KNT\", \"where\": \"p. 194 s.v. nūram\", \"stance\": \"supports\",\n    \"note\": \"'nūram adv. \\\"now\\\": Av. nūrəm; from pIE *nū \\\"now\\\" … + final of (pAr.) *dūram \\\"long\\\"' — confirms both Av. nū and Av. nūrəm.\"},\n   {\"src\": \"ARY\", \"where\": \"printed pp. 503-504 (NEW) and pp. 92-93 (NOW)\", \"stance\": \"supports\",\n    \"note\": \"incoming/ARY: the *newo- entry lists 'NAVO, NAVA (AVESTAN)' with Pahlavi 'NOG, NAVAK, NOK, NO'; the *nu- entry lists 'NU, NUREM (AVESTAN)', 'NURAM (OLD PERSIAN)', 'NUN (PAHLAVI)' — the same two Avestan branches Nourai draws.\"}]})\n\nnodes.append({\n \"id\": 2, \"lang\": \"Persian\", \"words\": \"now; aknŭn, knŭn\", \"verdict\": \"confirmed\",\n \"derivation\": (\"Both Persian items descend from the two Avestan/Old Iranian forms above, though (as always in these \"\n   \"charts) the Middle Persian stage is not drawn. (a) NP نو now/nou 'new': Old Iranian *nawa- was extended with the \"\n   \"adjectival suffix *-ka- to *nawaka- > MP nōg (spelled nwk', MacKenzie p. 60 'nōg … new, recent'), and MP -ōg lost \"\n   \"its final -g in New Persian, giving نو nō, pronounced with the diphthong now/nou (Hübschmann, Persische Studien \"\n   \"§1045: 'Wird nau (now) gesprochen, wie die Ipt. saw, rau'; and §-note 'Aber np. nau \\\"neu\\\" = zd. nava-'). \"\n   \"Compare the still-transparent compound نوروز nowrūz < MP nōg-rōz. (b) NP اکنون aknūn / کنون kunūn 'now': the \"\n   \"core نون nūn is the regular Persian reflex of Old Iranian *nū / *nūram — Bartholomae already gives 'Pahl. nūn' \"\n   \"for Av. nū, and MacKenzie p. 60 has 'nun [KON < Aramaic k'n] now' — so the Iranian adverb survives with an \"\n   \"Aramaic-derived spelling in Pahlavi and as نون in Persian. The prefixed elements are less secure: Horn (no. 1052) \"\n   \"simply cross-refers 'nūn … vergl. eknūn, kunūn', Mann (p. 855) lists 'Per. cf. ka-nün, ak-nün', and Wiktionary \"\n   \"flags the first element as unexplained. The chart's claim — that the نون of اکنون/کنون continues Av. nū/nūrəm — \"\n   \"is what all of these sources say.\"),\n \"derivation_fa\": (\"«نو» فارسی از ایرانی باستانِ *nawaka- (صورتِ پسوندی *nawa- + -ka-) است که در فارسی میانه nōg \"\n   \"(نوشتهٔ nwk'؛ مکنزی ص ۶۰) شده و با افتادنِ گِ پایانی در فارسی نو به «نو» بدل گشته است؛ هوبشمان در پژوهش‌های \"\n   \"فارسی (بند ۱۰۴۵) می‌نویسد که این واژه nau/now تلفظ می‌شود و همان nava- اوستایی است. حاشیهٔ معین بر برهان \"\n   \"قاطع (ص ۲۱۷۳) نیز همین زنجیره را می‌آورد: «اوستایی nava- (تازه)، پهلوی navak، nōk». دربارهٔ «اکنون / کنون»، \"\n   \"هستهٔ «نون» بازماندهٔ *nū / nūram ایرانی باستان است (بارتولومه برای nū اوستایی صورتِ پهلوی nūn را می‌دهد و \"\n   \"مکنزی ص ۶۰ «nun … now» را ثبت کرده)؛ ولی خاستگاهِ جزءِ آغازیِ «اَک-/کَـ-» همچنان روشن نیست (هرن، بند ۱۰۵۲؛ \"\n   \"مان ص ۸۵۵ «ka-nün, ak-nün»). ادعای نورایی درست است، تنها حلقهٔ فارسی میانه در نمودار نیامده است.\"),\n \"sources\": [W+\"%D9%86%D9%88\", W+\"%D8%A7%DA%A9%D9%86%D9%88%D9%86\"],\n \"ref_check\": [\n   {\"ref\": \"BQT:2173\", \"status\": \"supports\",\n    \"note\": \"Fetched with tools/ref_page.py BQT:2173 (vol. 4, pdf p. 256; image + vision transcript saved to data/verification/sources/refs/ocr/BQT/2173.png/.vision.txt). The page opens the section «در نون با واو» with the headword «نو «بفتح اول و سکون ثانی» معروف است که نقیض کهنه باشد». Mo'in's footnote 8 reads: «nau … در تلفظ (متداول) تبدیل به now شده (رک: هوبشمان ۱۰۴۵)؛ اوستایی nava- (تازه)، پهلوی navak، nōk، پازند nō، هندی باستان náva-، ارمنی nor، افغانی nau, navai، استی nāvāg, nvog، بلوچی nōk, nōx، شغنی náu، سریکلی nūj … کردی nū, neū» — precisely Nourai's Avestan nava- → Persian now, with the Pahlavi step supplied.\"},\n   {\"ref\": \"HRN:236\", \"status\": \"supports\",\n    \"note\": \"HRN.txt leaf 257 = printed p. 236: '1052. nūn \\\"jetzt, nun\\\", vergl. eknūn, kunūn. aw. nū, nūrem \\\"jetzt\\\", vergl. oss. d. nur, t. njr \\\"nun\\\" (207); šiγn. nur, sar. nur \\\"heute\\\"; phlv. nūn; ai. nūnám …'. The cited page carries exactly the aknūn/kunūn ← Av. nū/nūrəm claim.\"}],\n \"consulted\": [\n   {\"src\": \"HUB\", \"where\": \"Persische Studien §1045 and §53-note (p. 127)\", \"stance\": \"supports\",\n    \"note\": \"HUB.txt line 3611: '1045. Wird nau (now) gesprochen, wie die Ipt. saw, rau (sou, rou)'; line 4416 footnote: 'Aber np. nau \\\"neu\\\" = zd. nava- etc.'; line 5832: 'Auslautendes av wird au (ou) gesprochen: … nau \\\"neu\\\" H. 1045'. This is the §1045 Mo'in cites in BQT.\"},\n   {\"src\": \"PHD\", \"where\": \"MacKenzie p. 60 s.v. nōg and nun\", \"stance\": \"supports\",\n    \"note\": \"'nog [nwk' | M nwg, N nōw] new, recent.' and 'nun [KON < A k'n | M, J nwn] now.' — the two Middle Persian links the chart leaves implicit.\"},\n   {\"src\": \"BQT\", \"where\": \"vol. 4 p. 2173, Mo'in's footnote 8\", \"stance\": \"supports\",\n    \"note\": \"«اوستایی nava- (تازه)، پهلوی navak، nōk … کردی nū, neū»; see the vision transcript at data/verification/sources/refs/ocr/BQT/2173.vision.txt.\"},\n   {\"src\": \"HRN\", \"where\": \"no. 1052, p. 236\", \"stance\": \"supports\",\n    \"note\": \"'nūn \\\"jetzt, nun\\\", vergl. eknūn, kunūn. aw. nū, nūrem \\\"jetzt\\\" … phlv. nūn'.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann p. 855 s.v. nú, nün, nūnai\", \"stance\": \"supports\",\n    \"note\": \"'Skt. nu, nū, nünam \\\"now\\\"; Av. nü, id.; Per. cf. ka-nün, ak-nün, id.' — Mann puts both Persian adverbs under *nu.\"},\n   {\"src\": \"ARY\", \"where\": \"printed pp. 92-93, root NOW\", \"stance\": \"supports\",\n    \"note\": \"Aryanpur's NOW entry gives 'NU, NUREM (AVESTAN) / NURAM (OLD PERSIAN) / NUN (PAHLAVI) / NUR, NIR (OSSETIC) / NIHA, NAKA (KURDISH)' with references Pokorny, MacKenzie (NOW) 125, Buck 962-963, Skeat 408.\"}]})\n\nnodes.append({\n \"id\": 3, \"lang\": \"Pahlavi\", \"words\": \"nîvěd\", \"verdict\": \"disputed\",\n \"derivation\": (\"The word is real but the arrow is wrong. Middle Persian niwē 'good news' is well attested \"\n   \"(MacKenzie, Concise Pahlavi Dictionary p. 60: 'niwē [nwyk' | (N nuwēd)] good news'), and it belongs to the verb \"\n   \"MP niwistan, niwēy- (also niwēyēnīdan) 'to announce, consecrate' (MacKenzie p. 60), i.e. to the Old Iranian \"\n   \"compound *ni-vaid- / *ni-waid- 'to make known, announce' (Avestan ni-vaēdaya- 'to announce'), from PIE *weyd- \"\n   \"'to see, know' — the same root as Skt. vindáti, Gk. οἶδα, Eng. wit. It has nothing to do with *néwos 'new'; the \"\n   \"n-v- resemblance to nava-/now is accidental, and 'good news' is a semantic invitation to the mistake. Horn \"\n   \"states the correct etymology on the very page Nourai cites for the box above (no. 1053, p. 236): 'nuved \\\"frohe \"\n   \"Botschaft\\\". Die übliche Erklärung aus ni + √vaed-, vergl. aw. nivaēdayemi…' (Horn only queries the retention of \"\n   \"-d-, not the root). Wiktionary derives نوید from 'Middle Persian nwyk' (*niwē), from Proto-Iranian *wayd-', \"\n   \"citing MacKenzie and comparing Manichaean Parthian nwydg (niwēdag) 'good news' and Parthian nwyst 'invited' — \"\n   \"the Parthian -d- form is where Nourai's -d- spelling belongs. Aryanpur, independently, files MP niwāg, \"\n   \"niwēyēnīdan, niwistan under PIE *neu- 'to cry, shout' (Pokorny 767, with Lat. nuntius) — also not under *newos. \"\n   \"On the form itself: MacKenzie's headword is niwē; the -d appears in Parthian niwēdag and in NP نوید, so Nourai's \"\n   \"'nîvěd' is a legitimate (if not MacKenzie's) Middle Iranian citation form, not a misprint.\"),\n \"derivation_fa\": (\"واژه هست، ولی پیوندش نادرست است. فارسی میانهٔ niwē «خبر خوش» (مکنزی، فرهنگ کوچک پهلوی، ص ۶۰: \"\n   \"«niwē [nwyk'] good news») به فعلِ پهلویِ niwistan / niwēy- «آگاهانیدن، اعلام کردن» بازمی‌گردد و آن از \"\n   \"ترکیبِ ایرانی باستانِ *ni-vaid- است (اوستایی ni-vaēdaya- «اعلام کردن») از ریشهٔ هندواروپایی *weyd- «دیدن، \"\n   \"دانستن» — نه از *néwos «نو». همانندیِ صوریِ nav-/niw- و معنیِ «خبر» زمینهٔ این ریشه‌شناسی عامیانه را فراهم \"\n   \"کرده است. هرن در همان صفحه‌ای که نورایی برای کادرِ بالا به آن ارجاع می‌دهد (بند ۱۰۵۳، ص ۲۳۶) صریحاً می‌نویسد: \"\n   \"«توضیحِ رایج از ni + √vaēd- است، سنجیده شود با اوستاییِ nivaēdayemi». ویکی‌واژه هم آن را از ایرانی آغازینِ \"\n   \"*wayd- می‌گیرد و پارتیِ مانویِ nwydg (niwēdag) «خبر خوش» را هم‌ریشه می‌شمارد. بنابراین پژوهش امروزی این \"\n   \"شاخه را از ریشهٔ «نو» جدا می‌کند.\"),\n \"sources\": [W+\"%D9%86%D9%88%DB%8C%D8%AF\", \"https://abadis.ir/fatofa/%D9%86%D9%88%DB%8C%D8%AF/\"],\n \"ref_check\": [\n   {\"ref\": \"MON:4859\", \"status\": \"partial\",\n    \"note\": \"The 6-volume Mo'in cannot be paginated from any scan available here, so page 4859 itself is unverifiable; the entry text is: MON_part2.txt line 81140 area «نوید … (اِ.) خبر خوش، مژده؛ بشارت. وعدهٔ نیک …», and the same entry on abadis.ir (فرهنگ معین) reads «(نَ) (اِ.) ۱ - خبر خوش، بشارت. ۲ - وعدهٔ نیک». Mo'in gives the gloss Nourai uses but no Pahlavi antecedent and no link to nava- 'new'; on the same page abadis reproduces Dehkhoda, who derives نوید from نِ + Avestan «وئید» (waēd-).\"}],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie p. 60 s.v. niwē / niwistan\", \"stance\": \"partial\",\n    \"note\": \"'niwē [nwyk' | (N nuwēd)] good news.' — confirms the Pahlavi word and the NP descendant, but files it with 'niwistan, +niwēy- [nwstn', nwyd- | nwyk-] announce, consecrate', i.e. under the verb 'announce', not under nōg 'new' (which is a separate headword on the same page).\"},\n   {\"src\": \"NYB\", \"where\": \"Part II Glossary, grepped for nivēt / niwēt / niwēy\", \"stance\": \"silent\",\n    \"note\": \"grep -n 'nivēt|niw[ēe]t|niwēy' NYB_vol2_glossary.txt returns nothing (only nēvak 'good' and its compounds); Nyberg's glossary covers only his text selection, so it neither supports nor contradicts.\"},\n   {\"src\": \"HRN\", \"where\": \"no. 1053, p. 236\", \"stance\": \"contradicts\",\n    \"note\": \"'1053. nuved \\\"frohe Botschaft\\\". Die übliche Erklärung aus ni + √vaed-, vergl. aw. nivaēdayemi, ist erstens wegen der auffälligen Erhaltung des d bedenklich…' — Horn knows only the ni + vaid- etymology; nava- 'new' is not even considered.\"},\n   {\"src\": \"ARY\", \"where\": \"printed p. 504, root *NEU-\", \"stance\": \"contradicts\",\n    \"note\": \"Aryanpur's *NEU- entry lists 'NAD- (AVESTAN) / NIWAG, NIWEYENIDAN, NIWISTAN (PAHLAVI) / NEWA (KURDISH) / NAVATE, NAUTI (SANSKRIT) / NUNTIUS, NUNTIUM (LATIN)' with refs MacKenzie (MELODY) 123 and Mallory & Adams (ANNOUNCE) 102 — i.e. he too keeps the 'announce' family away from his *newo- 'new' entry (p. 503).\"}]})\n\nnodes.append({\n \"id\": 4, \"lang\": \"Persian\", \"words\": \"novîd\", \"verdict\": \"disputed\",\n \"derivation\": (\"The Middle Persian → New Persian step drawn here is itself correct and regular: MP niwē(d) / \"\n   \"Parthian niwēdag > NP نوید navīd/nuwēd 'good news, glad tidings, promise of good' (Mo'in: «خبر خوش، مژده؛ \"\n   \"بشارت. وعدهٔ نیک»), with MP -ē- surfacing as Persian -ī- (written ی) and the verbal noun keeping the -d of the \"\n   \"present stem nwyd-. The Hafez couplet quoted in the box is genuine (opening of the ghazal بیا که رایت منصور \"\n   \"پادشاه رسید / نوید فتح و بشارت به مهر و ماه رسید) and illustrates the sense 'tidings of victory'. What is wrong \"\n   \"is the branch's attachment: نوید does not belong to *néwos 'new' at all. It continues *ni-vaid- 'announce' \"\n   \"(Av. ni-vaēdaya-), PIE *weyd- 'know, see' — so Wiktionary (Proto-Iranian *wayd-, citing MacKenzie), Horn no. 1053, \"\n   \"and Dehkhoda (نِ + اوستایی وئید waēd-) all agree; Aryanpur instead assigns MP niwistan to PIE *neu- 'shout, cry' \"\n   \"(with Lat. nuntius), which is again outside the 'new' family. Whichever of those two is preferred, Nourai's root \"\n   \"for this branch is not supported.\"),\n \"derivation_fa\": (\"گامِ فارسی میانه ← فارسی نو در همین کادر درست است: niwē(d) پهلوی / niwēdag پارتی به «نوید» \"\n   \"فارسی بدل شده («خبر خوش، مژده، بشارت؛ وعدهٔ نیک» به گفتهٔ معین) و ē فارسی میانه در فارسی نو به ی کشیده بدل \"\n   \"گشته است؛ بیتِ حافظ در کادر («بیا که رایت منصور پادشاه رسید / نوید فتح و بشارت به مهر و ماه رسید») نیز \"\n   \"اصیل است. ولی جای این شاخه در نمودار نادرست است: «نوید» هیچ پیوندی با ریشهٔ *néwos «نو» ندارد و بازماندهٔ \"\n   \"*ni-vaid- «آگاهانیدن، اعلام کردن» است (اوستایی ni-vaēdaya-) از ریشهٔ *weyd- «دیدن، دانستن»؛ همین را ویکی‌واژه، \"\n   \"هرن (بند ۱۰۵۳) و دهخدا (نِ + وئیدِ اوستایی) می‌گویند و آریان‌پور نیز آن را زیر *neu- «بانگ زدن» (با nuntius \"\n   \"لاتین) می‌آورد. پس پژوهش امروزی ادعای نورایی را در این شاخه رد می‌کند، هرچند خودِ واژه و معنایش درست است.\"),\n \"sources\": [W+\"%D9%86%D9%88%DB%8C%D8%AF\", \"https://abadis.ir/fatofa/%D9%86%D9%88%DB%8C%D8%AF/\"],\n \"ref_check\": [\n   {\"ref\": \"IEC:842\", \"status\": \"not_found\",\n    \"note\": \"IEC.txt leaf 470 = printed pp. 841-842; that page holds Mann's entries neuqu-, neur-, neusmn-, neusō, neuuō, neuaiō, neuākos and neue — no Persian navīd/nuwēd anywhere, and no 'good news' word. (The nearest thing is 'neusmn- (neusn-) \\\"sign, recognition\\\"' and 'neuuō \\\"nod, sign\\\"', which are Pokorny's neu- 'nod/sign' family, not *newos.) Nourai's page reference cannot be made to yield نوید; grep -n -i 'navid|nivid|nawid|niwed' IEC.txt returns only 'nüu- … Per. cf. navidan, inf. \\\"lament\\\"' (p. 855), a different word.\"},\n   {\"ref\": \"MON:4859\", \"status\": \"partial\",\n    \"note\": \"Mo'in has the entry («نوید … خبر خوش، مژده؛ بشارت. وعدهٔ نیک», MON_part2.txt line 81140; abadis.ir فرهنگ معین «(نَ) (اِ.) ۱ - خبر خوش، بشارت. ۲ - وعدهٔ نیک») but the six-volume pagination cannot be checked from the scans on disk, and Mo'in offers no etymology tying it to nava- 'new'.\"}],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"s.v. نوید (via abadis.ir, فرهنگ معین; MON_part2.txt)\", \"stance\": \"partial\",\n    \"note\": \"«(نَ) (اِ.) ۱ - خبر خوش، بشارت. ۲ - وعدة نیک» — gloss identical to the chart, etymology absent.\"},\n   {\"src\": \"HRN\", \"where\": \"no. 1053, p. 236\", \"stance\": \"contradicts\",\n    \"note\": \"Horn's entry for np. nuved 'frohe Botschaft' knows only 'ni + √vaed-, vergl. aw. nivaēdayemi'.\"},\n   {\"src\": \"PHD\", \"where\": \"MacKenzie p. 60\", \"stance\": \"partial\",\n    \"note\": \"'niwē [nwyk' | (N nuwēd)] good news' — MacKenzie himself gives the New Persian outcome nuwēd, confirming the MP→NP link but placing it with niwistan 'announce'.\"},\n   {\"src\": \"ARY\", \"where\": \"printed p. 504, root *NEU-\", \"stance\": \"contradicts\",\n    \"note\": \"Persian نوا/نوید family listed under PIE *NEU- with Pahlavi NIWAG, NIWEYENIDAN, NIWISTAN and Lat. NUNTIUS; Aryanpur's *newo- 'new' entry (p. 503) does not contain it.\"}]})\n\nnodes.append({\n \"id\": 5, \"lang\": \"Sogdian\", \"words\": \"nwr\", \"verdict\": \"confirmed\",\n \"derivation\": (\"Sogdian nwr (nur), attested in the Buddhist, Christian and Manichaean corpora, means 'now' and is \"\n   \"the regular Sogdian continuation of Old Iranian *nūram — the very form Nourai's Avestan box supplies as nūrəm. \"\n   \"Gharib's Sogdian Dictionary, entry 6142 on printed p. 246, prints 'nwr B, S, C — nur (nwry) © <Av. nūrəm-, \"\n   \"Khwar. nwr; Yaghn. nur — now', i.e. she derives it from Avestan nūrəm exactly as the chart does, and adds the \"\n   \"Khwarezmian and Yaghnobi cognates. Phonologically Old Iranian *nūram lost its final syllable in Sogdian (as \"\n   \"regularly with unstressed final -am), leaving nwr; the oblique nwry is the same word with the Sogdian light-stem \"\n   \"ending. Note that Sogdian 'new' is a different word, nwc/nōč (Gharib no. 6125), so the Sogdian box rightly hangs \"\n   \"on the 'now' half of the double root.\"),\n \"derivation_fa\": (\"سغدیِ nwr (nur) «اکنون» بازماندهٔ قاعده‌مندِ *nūram ایرانی باستان است؛ قریب در فرهنگ سغدی \"\n   \"(مدخل ۶۱۴۲، ص ۲۴۶) می‌نویسد: «nwr B, S, C — nur (nwry) < اوستایی nūrəm-، خوارزمی nwr، یغنابی nur — now»، \"\n   \"یعنی درست همان پیوندی که نورایی کشیده است. هجای پایانیِ بی‌تکیهٔ -am در سغدی افتاده و nwr مانده است. \"\n   \"شایان ذکر است که «نو» در سغدی واژهٔ دیگری است (nwc/nōč، مدخل ۶۱۲۵)، پس این کادر به‌درستی به شاخهٔ «Nu» \"\n   \"(اکنون) وابسته است. ادعای نورایی درست است.\"),\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"SOD:246\", \"status\": \"supports\",\n    \"note\": \"SOD_pages.txt leaf 312 (printed p. 246, per the stated offset leaf−66): '6142 nwr B, S, C — nur (nwry) © <Av. nurdm-, Khwar. nwr; Yaghn. nur … now … ob. nwry, BSTBL'. Both the page number and the derivation from Av. nūrəm are Nourai's.\"}],\n \"consulted\": [\n   {\"src\": \"SOD\", \"where\": \"Gharib no. 6142, p. 246\", \"stance\": \"supports\",\n    \"note\": \"'nwr … nur … <Av. nūrəm-, Khwar. nwr; Yaghn. nur … now'; cf. no. 6125 'nwc … nōč … new' for the unrelated Sogdian word for 'new'.\"},\n   {\"src\": \"BRT\", \"where\": \"col. 1090 s.v. nūram / nūrəm\", \"stance\": \"supports\",\n    \"note\": \"'p. nūram, j., g. nūrəm, j. Adv. \\\"jetzt, gegenwärtig\\\"' — the Old Iranian source form Gharib points to.\"}]})\n\nnodes.append({\n \"id\": 6, \"lang\": \"Old Persian\", \"words\": \"nŭram\", \"verdict\": \"confirmed\",\n \"derivation\": (\"Old Persian nūram 'now' is attested once, in Darius' Bisitun inscription (DB 4.53), and is correctly \"\n   \"glossed and correctly hung directly on the *nu root. Kent's lexicon, p. 194 — the page Nourai cites — reads \"\n   \"'nūram adv. \\\"now\\\": Av. nūrəm; from pIE *nū \\\"now\\\" (Av. nū, Skt. nū, Lt. nu-nc, NEng. now) + final of (pAr.) \"\n   \"*dūram \\\"long\\\" (§148.1), cf. dūraiy. DB 4.53', i.e. OP nūram = *nū plus the -ram of *dūram taken over by \"\n   \"analogy. Bartholomae enters the Old Persian and the Avestan forms in one article (col. 1090: 'p. nūram, j., g. \"\n   \"nūrəm, j. Adv. \\\"jetzt, gegenwärtig\\\"'), and Pokorny 770 lists 'Avestan nuram, nurqm, ap. nuram' with the same \"\n   \"analogical explanation ('shaped after aparəm?'). Nourai's breve on ŭ again stands for long ū.\"),\n \"derivation_fa\": (\"پارسی باستانِ nūram «اکنون» یک بار در سنگ‌نوشتهٔ بیستون دربندِ DB 4.53 آمده است و در نمودار \"\n   \"درست معنی و درست به شاخهٔ *nu بسته شده. کنت در واژه‌نامهٔ پارسی باستان، ص ۱۹۴ (همان صفحه‌ای که نورایی \"\n   \"ارجاع داده) می‌نویسد: «nūram قید «اکنون»: اوستایی nūrəm؛ از *nū هندواروپایی + پایانهٔ *dūram «دراز» به قیاس». \"\n   \"بارتولومه (ستون ۱۰۹۰) هر دو صورتِ پارسی باستان و اوستایی را در یک مدخل آورده و پوکورنی (ص ۷۷۰) نیز \"\n   \"«av. nūrəm, nūrąm, ap. nūram» را ثبت کرده است. ادعای نورایی درست است.\"),\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"POK:770\", \"status\": \"supports\",\n    \"note\": \"POK_full.txt s.v. nu-: 'Avestan nuram, nurqm, ap. nuram ds. (shaped after aparem \\\"from here on, hereafter\\\"?)' — Page(s): 770.\"},\n   {\"ref\": \"KNT:194\", \"status\": \"supports\",\n    \"note\": \"KNT.txt leaf 217, running head '194 OLD PERSIAN': 'nūram adv. \\\"now\\\": Av. nūrəm; from pIE *nū \\\"now\\\" … + final of (pAr.) *dūram \\\"long\\\" (§148.1) … DB 4.53'.\"}],\n \"consulted\": [\n   {\"src\": \"KNT\", \"where\": \"p. 194 s.v. nūram\", \"stance\": \"supports\", \"note\": \"see the quotation above; the only OP attestation given is DB 4.53.\"},\n   {\"src\": \"BRT\", \"where\": \"col. 1090\", \"stance\": \"supports\", \"note\": \"'p. nūram, j., g. nūrəm, j. Adv. \\\"jetzt, gegenwärtig\\\"'.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. II p. 340 s.v. nu-\", \"stance\": \"supports\",\n    \"note\": \"'av. nūrom, niirqm, ap. niiram ds. (nach surom „fruhmorgens\\\" gebildet?)' — Walde-Pokorny hesitates between *dūram and *sūrəm as the model, but the *nu- ancestry is the same.\"}]})\n\nnodes.append({\n \"id\": 7, \"lang\": \"Germanic\", \"words\": \"neuja\", \"verdict\": \"plausible\",\n \"derivation\": (\"The form is right, the double gloss is not. Proto-Germanic *niwjaz (Nourai's 'neuja', Klein's \"\n   \"'Teut. base *neuja-') is the suffixed *new-yo- form of PIE *néwos, whence Gothic niujis, Old Norse nýr, OHG \"\n   \"niuwi, Old Saxon niuwi, OE nīwe/nēowe 'new' — Watkins: 'Suffixed form *new-yo- in Germanic *neuja- in: a. Old \"\n   \"English nēowe, niwe, new: NEW'. But Germanic 'now' is NOT from *niwjaz: it is Gmc *nu (Gothic nu, ON nú, OHG/OE \"\n   \"nū, German nun), the bare zero-grade adverb *nu, which Watkins keeps in a separate article ('nu-. Now. Related \"\n   \"to newo-. 1. Old English nū, now: NOW'). So the Germanic box conflates two distinct Germanic words that \"\n   \"correspond to the two halves of Nourai's own double root; the arrow from the root is fine, the gloss 'new, now' \"\n   \"should be split.\"),\n \"derivation_fa\": (\"صورت درست است، ولی معنیِ دوگانه نه. ژرمنی آغازینِ *niwjaz (همان «neuja»ی نورایی) صورتِ \"\n   \"پسوندیِ *new-yo- از *néwos است و گوتیِ niujis، نورسِ باستان nýr، آلمانی علیای باستان niuwi و انگلیسی باستان \"\n   \"nīwe/nēowe «نو» از آن است. اما «now» ژرمنی از *niwjaz نیامده؛ آن بازماندهٔ قیدِ *nu است (گوتی nu، انگلیسی \"\n   \"باستان nū، آلمانی nun) که واتکینز در پیوستِ AHD مدخلی جداگانه به آن داده است. پس این کادر دو واژهٔ جداگانهٔ \"\n   \"ژرمنی را در هم آمیخته است؛ فلشِ ریشه درست است ولی معنیِ «new, now» را باید دو پاره کرد. ادعای نورایی با \"\n   \"احتیاط پذیرفتنی است.\"),\n \"sources\": [\"https://www.etymonline.com/word/now\"],\n \"ref_check\": [\n   {\"ref\": \"AHD:1531\", \"status\": \"partial\",\n    \"note\": \"The 1976 appendix page is not openable, but Watkins 1985 (AHD_watkins1985.txt line 787) supports the 'new' half — 'newo-. New. … 1. Suffixed form *new-yo- in Germanic *neuja- in: a. Old English néowe, niwe, new: NEW; b. Old Norse nyr, new: SPAN-NEW' — while placing 'now' under a separate root (line 792: 'nu-. Now. … 1. Old English nū, now: NOW'). So AHD does not license the 'now' gloss on *neuja-.\"}],\n \"consulted\": [\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. newo- §1 and nu- §1\", \"stance\": \"partial\", \"note\": \"see the quotation above.\"},\n   {\"src\": \"KLN\", \"where\": \"p. 1044 s.v. 'new' and p. 1059 s.v. 'now'\", \"stance\": \"partial\",\n    \"note\": \"'new, adj. — ME. newe, fr. OE. niwe, neowe, rel. to OS. niuwi, niwi … Goth. niujis, \\\"new\\\", fr. Teut. base *neuja-, corresponding to I.-E. base *newo-, *newio-, *nowio-'; but 'now, adv. — ME. nou, nu, fr. OE. nū … They derive fr. I.-E. base *nu, which is rel. to base *newo-'. Klein separates the two Germanic words.\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict., s.v. new\", \"stance\": \"supports\",\n    \"note\": \"'M. E. newe; A. S. nīwe, nēowe. + Du. nieuw, Icel. nýr, Dan. Swed. ny, Goth. niujis, G. neu, L. novus … Gk. νέος, Skt. nava, new … All from base NU, i.e. now; new means \\\"that which is now, recent\\\"' — Skeat even draws the *newo-/*nu link Nourai's box assumes, but does so at the root, not inside Germanic.\"}]})\n\nnodes.append({\n \"id\": 8, \"lang\": \"English\", \"words\": \"new, now\", \"verdict\": \"plausible\",\n \"derivation\": (\"English new is the direct descendant of the Germanic box: OE nīwe/nēowe > ME newe > new, with OE \"\n   \"-īw-/-ēow- monophthongised and the final -e lost in Middle English (Skeat s.v. new: 'M. E. newe; A. S. nīwe, \"\n   \"nēowe'). English now, however, comes from OE nū > ME nou/nu > now — the inherited adverb *nu, not from *niwjaz: \"\n   \"'now, adv. — ME. nou, nu, fr. OE. nū, rel. to ON. nú, … Goth. nu, \\\"now\\\" … They derive fr. I.-E. base *nu, \"\n   \"which is rel. to base *newo-' (Klein p. 1059), and Etymonline likewise gives OE nū and PIE *nu, adding only \"\n   \"that it was 'perhaps originally \\\"newly, recently\\\" and related to the root of new'. So both English words do \"\n   \"belong to Nourai's double root, but 'now' hangs on the Nu half directly and not under Germanic *neuja-; the \"\n   \"verdict is plausible rather than confirmed only because of that misrouting.\"),\n \"derivation_fa\": (\"«new» انگلیسی بازماندهٔ مستقیمِ کادرِ ژرمنی است: انگلیسی باستان nīwe/nēowe > انگلیسی میانه \"\n   \"newe > new. اما «now» از انگلیسی باستان nū می‌آید (nū > nou > now) که همان قیدِ ارثیِ *nu است و نه از \"\n   \"*niwjaz؛ کلاین (ص ۱۰۵۹) و اتیمانلاین هر دو آن را زیر *nu می‌آورند و تنها می‌افزایند که «شاید در آغاز به \"\n   \"معنی تازه/به‌تازگی بوده و با ریشهٔ new پیوند دارد». پس هر دو واژه به کادرِ دوگانهٔ ریشه تعلق دارند، ولی \"\n   \"«now» باید یکسر به شاخهٔ Nu بسته شود، نه به ژرمنیِ *neuja-. ادعای نورایی با احتیاط پذیرفتنی است.\"),\n \"sources\": [\"https://www.etymonline.com/word/now\"],\n \"ref_check\": [\n   {\"ref\": \"(none)\", \"status\": \"not_checked\",\n    \"note\": \"The book gives no reference for this English box (refs=None in the JSON, and no book icon on the printed page); the claim is checked against Klein, Skeat and Etymonline under 'consulted'.\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"p. 1044 s.v. new; p. 1059 s.v. now\", \"stance\": \"partial\",\n    \"note\": \"'new, adj. — ME. newe, new, fr. OE. niwe, neowe … fr. Teut. base *neuja-'; 'now, adv. — ME. nou, nu, fr. OE. nū … fr. I.-E. base *nu, which is rel. to base *newo-. See new.'\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat s.v. new (and index 'New; see Nov.', 'Newfangled, News; see Now')\", \"stance\": \"supports\",\n    \"note\": \"'M. E. newe; A. S. nīwe, nēowe … All from base NU, i.e. now; new means \\\"that which is now, recent\\\"'.\"}]})\n\nnodes.append({\n \"id\": 9, \"lang\": \"Greek\", \"words\": \"neos\", \"verdict\": \"confirmed\",\n \"derivation\": (\"Greek νέος 'new, young' is the inherited thematic adjective *néwos with regular loss of \"\n   \"intervocalic *-w- in Attic-Ionic: *néwos > *νέϝος (still written in Mycenaean ne-wo and reflected in Klein's \"\n   \"'Gk. νέος (for *νέϝος)') > νέος. Pokorny 769 lists 'gr. v£(F)oc;' among the direct reflexes and Watkins has \"\n   \"'Basic form *newo- in Greek newos, neos, new: NEO-, NEON, NEOTERIC'. Buck (§14.13) notes the Greek semantic \"\n   \"peculiarity — νέος is 'chiefly \\\"young\\\", but also in part \\\"new\\\"' — so Nourai's gloss 'new' is the correct \"\n   \"etymological sense even though 'young' is the commoner Greek usage. Ernout-Meillet s.v. nouus likewise equates \"\n   \"'gr. νέος (de νεϝος)' with Latin nouus.\"),\n \"derivation_fa\": (\"یونانیِ νέος «نو، جوان» همان صفتِ ارثیِ *néwos است با افتادنِ قاعده‌مندِ w میان‌واکه‌ای در \"\n   \"گویشِ آتیک‑ایونی: *néwos > *νέϝος (که در میسنیِ ne-wo هنوز نوشته می‌شود) > νέος. پوکورنی (ص ۷۶۹) و واتکینز \"\n   \"هر دو آن را بازماندهٔ مستقیمِ ریشه می‌شمارند. باک (بندِ ۱۴٫۱۳) یادآور می‌شود که νέος در یونانی بیشتر «جوان» \"\n   \"به کار رفته و «نو» معنیِ ریشه‌شناختیِ آن است؛ پس معنیِ دادهٔ نورایی درست است. ادعای نورایی درست است.\"),\n \"sources\": [W+\"Reconstruction:Proto-Indo-European/n%C3%A9wos\"],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"Watkins 1985 s.v. newo-, §2: 'Basic form *newo- in Greek newos, neos, new: NEO-, NEON, NEOTERIC; MISONEISM' — the Greek box and its English box together.\"}],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"p. 769\", \"stance\": \"supports\", \"note\": \"'gr. v£(F)oc;' listed with Old Indic nava-, Av. nava-, Lat. novus as a direct reflex of *neuos.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck §14.13, p. 957\", \"stance\": \"supports\",\n    \"note\": \"'a) Grk. véos (chiefly \\\"young\\\", but also in part \\\"new\\\"; NG \\\"new\\\" only in phrases like τι νέα; \\\"what news?\\\")'.\"},\n   {\"src\": \"KLN\", \"where\": \"p. 1040 s.v. neo-\", \"stance\": \"supports\",\n    \"note\": \"'neo-, combining form meaning \\\"new, recent\\\". — Gk. veo-, fr. vioc, \\\"new\\\", for *νεϝος, fr. I.-E. *newos, \\\"new\\\", whence also Goth. niujis, OE. neowe, \\\"new\\\"'.\"}]})\n\nnodes.append({\n \"id\": 10, \"lang\": \"English\", \"words\": \"neo-, neon\", \"verdict\": \"confirmed\",\n \"derivation\": (\"Both are learned borrowings from Greek νέος. neo- is the combining form, taken over through Latin \"\n   \"into the scientific vocabulary of the 18th-19th c. (Klein p. 1040: 'neo-, combining form meaning \\\"new, recent\\\". \"\n   \"— Gk. νεο-, fr. νέος, \\\"new\\\", for *νεϝος, fr. I.-E. *newos'). neon is Modern Latin, literally 'the new \"\n   \"(element)', from the neuter νέον, and the naming event is documented: 'coined by the discoverers of this \"\n   \"element, the Scottish chemist Sir William Ramsay (1852-1916) and the English chemist Morris William Travers \"\n   \"(1872-1961) in 1898' (Klein p. 1040 s.v. neon) — the neuter form was suggested by Ramsay's son. Watkins lists \"\n   \"NEO-, NEON, NEOTERIC and MISONEISM under newo- §2, exactly as the chart draws.\"),\n \"derivation_fa\": (\"هر دو وام‌واژهٔ عالمانه از یونانیِ νέος هستند. «neo-» جزءِ پیشوندیِ ترکیب‌های علمی است \"\n   \"(کلاین، ص ۱۰۴۰: «neo- از یونانیِ νέος، از *newos هندواروپایی») و «neon» لاتینِ نو است، لفظاً «(عنصرِ) نو»، \"\n   \"از صورتِ خنثای νέον؛ کلاین تاریخِ نام‌گذاری را هم می‌دهد: ویلیام رمزی و موریس تراورس در سال ۱۸۹۸ آن را \"\n   \"برساختند. واتکینز نیز NEO- و NEON را زیر مدخلِ newo- می‌آورد. ادعای نورایی درست است.\"),\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"(none)\", \"status\": \"not_checked\",\n    \"note\": \"No reference is printed in this box; checked against Klein and Watkins under 'consulted'.\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"p. 1040 s.v. neo- and neon\", \"stance\": \"supports\",\n    \"note\": \"'neon, n., name of a gaseous element (chem.) — ModL., lit. \\\"the new (element)\\\", fr. Gk. veov, neut. of veo?, \\\"new\\\" (see neo-); coined by the discoverers of this element, the Scottish chemist Sir William Ramsay … and the English chemist Morris William Travers … in 1898. Cp. krypton, xenon.'\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. newo- §2; index entries 'NEO- newo-', 'NEON newo-'\", \"stance\": \"supports\",\n    \"note\": \"'Basic form *newo- in Greek newos, neos, new: NEO-, NEON, NEOTERIC; MISONEISM' (and the reverse index lines 'NEO- newo- … NEON newo-').\"}]})\n\nnodes.append({\n \"id\": 11, \"lang\": \"Latin\", \"words\": \"novus\", \"verdict\": \"confirmed\",\n \"derivation\": (\"Latin nouus, -a, -um 'new' is the inherited *néwos with *-ew- kept (unlike Greek): the older \"\n   \"Praenestine form nouios and the proper name Nouius show the *-yo- variant beside it. Ernout-Meillet s.v. nouus \"\n   \"put it plainly: 'Nouus répond à gr. νέος (de νεϝος), skr. návaḥ, av. nava-, v.sl. novŭ, lit. navas', with the \"\n   \"derivatives nouitās, nouāre 'to renew', nouālis, nouellus, nouicius, innouō, renouō — the whole set that feeds \"\n   \"the English box below. Pokorny 769 has 'Latin novus, Oscan Nuvlanuis … Praenestian nouios' and refers to \"\n   \"Walde-Hofmann II 181; Watkins §4 'Basic form *newo- in Latin novus, new'.\"),\n \"derivation_fa\": (\"لاتینِ nouus «نو» همان *néwos است با نگه‌داشتِ -ew- (برخلافِ یونانی که w را انداخته)؛ صورتِ \"\n   \"کهنِ پرِنستیِ nouios و نامِ Nouius گونهٔ *-yo-دارِ آن را نشان می‌دهد. ارنو و مییه در ذیلِ nouus می‌نویسند: \"\n   \"«nouus برابرِ یونانیِ νέος (از νεϝος)، سنسکریتِ návaḥ، اوستاییِ nava-، اسلاویِ کهنِ novŭ، لیتوانیِ navas» و \"\n   \"مشتقاتِ nouitās، nouāre، nouellus، nouicius، innouō، renouō را می‌آورند که همان‌ها به کادرِ انگلیسیِ زیر \"\n   \"خورده‌اند. پوکورنی (ص ۷۶۹) نیز آن را در شمارِ بازمانده‌های مستقیم آورده است. ادعای نورایی درست است.\"),\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"Watkins 1985 s.v. newo- §4: 'Basic form *newo- in Latin novus, new: NOVA, NOVATION, NOVEL1, NOVEL2, (NOVELTY), NOVICE; INNOVATE, RENOVATE' — the Latin box plus its English box in one line.\"}],\n \"consulted\": [\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. nouus (LAT.txt line 42060 ff.)\", \"stance\": \"supports\",\n    \"note\": \"'nouus,-a,-um: nouveau, neuf … Nouus répond à gr. veoC (de veFoc), skr. navah, av. nava-, v.sl. novil, lit. navas. Le nom propre Nouius répond à iri. nue, gall. newydd (gaul. Novio-), got. niujis, lit. naujas, skr. návyah, gr. ion. veioC.' Also lists 'Composés: innouō, innouātiō, renouō … nouellus … nouicius'.\"},\n   {\"src\": \"POK\", \"where\": \"p. 769\", \"stance\": \"supports\",\n    \"note\": \"'Latin novus, Oscan Nuvlanuis \\\"Nolanīs\\\" … Praenestian nouios … References: WP. II 324, WH. II 181'.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. II p. 324\", \"stance\": \"supports\", \"note\": \"'iienos, \\\"ios „neu\\\". Ai. ndva-, av. nava- „neu\\\", gr. veog, lat. novas …'\"}]})\n\nnodes.append({\n \"id\": 12, \"lang\": \"English\", \"words\": \"nova, novel, novice; innovate, renovate\", \"verdict\": \"confirmed\",\n \"derivation\": (\"All five are Latin-based and all go back to nouus. nova (astron.) is Modern Latin, short for nova \"\n   \"stella 'a new star', fem. of nouus (Klein p. 1044 s.v. nova). novel comes from Old French novel < Latin nouellus, \"\n   \"the diminutive of nouus ('novel (F. — L.) O. F. novel … L. nouellus, new, dimin. of nouus', Skeat), the noun \"\n   \"'novel' via Italian novella 'tale'. novice is Old French novice < Medieval/Late Latin nouicius 'newly imported, \"\n   \"newly arrived, inexperienced' (said especially of newly acquired slaves — Ernout-Meillet: 'nouicius: novice … \"\n   \"se dit surtout des esclaves nouvellement acquis'), first English sense 'probationer in a religious order' (mid \"\n   \"14th c.), 'inexperienced person' by the early 15th c. (Etymonline). innovate < Latin innouāre 'to renew, alter' \"\n   \"(in- + nouāre 'to make new') and renovate < renouāre 'to renew', both 16th c. learned borrowings. Klein's 'new' \"\n   \"entry closes with exactly this list: 'Cp. also neo-, nova, novel, novercal, novice, nuncio, innovate, renovate.'\"),\n \"derivation_fa\": (\"هر پنج واژه از راهِ لاتین به انگلیسی رسیده‌اند و همه به nouus بازمی‌گردند: «nova» لاتینِ نو \"\n   \"و کوتاه‌شدهٔ nova stella «ستارهٔ نو» است؛ «novel» از فرانسهٔ کهنِ novel از لاتینِ nouellus (مصغّرِ nouus) و \"\n   \"نامِ ادبیِ آن از ایتالیاییِ novella «داستان»؛ «novice» از فرانسهٔ کهنِ novice از لاتینِ nouicius «تازه‌آمده، \"\n   \"بی‌تجربه» (که به گفتهٔ ارنو–مییه بیشتر دربارهٔ بردگانِ تازه‌خریده به کار می‌رفت) که در انگلیسیِ میانه نخست \"\n   \"«نوآموزِ رهبانی» و سپس «تازه‌کار» شد؛ و «innovate / renovate» از innouāre و renouāre لاتین. کلاین در پایانِ \"\n   \"مدخلِ new همین فهرست را می‌آورد: «Cp. also neo-, nova, novel, novercal, novice, nuncio, innovate, renovate». \"\n   \"ادعای نورایی درست است.\"),\n \"sources\": [\"https://www.etymonline.com/word/novice\"],\n \"ref_check\": [\n   {\"ref\": \"(none)\", \"status\": \"not_checked\",\n    \"note\": \"No reference printed in this box; checked against Klein, Skeat, Ernout-Meillet and Etymonline under 'consulted'.\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"p. 1044 (new; nova) and the innovate/renovate entries\", \"stance\": \"supports\",\n    \"note\": \"'nova, n., a new star … — ModL., short for L. nova Stella, \\\"a new star\\\"; fem. of novus, \\\"new\\\". See new'; 'innovate, intr. v. — L. innovatus, pp. of innovare, \\\"to renew, alter\\\", fr. in-, \\\"in\\\", and novare, \\\"to make new\\\", fr. novus, \\\"new\\\"'; and the 'new' entry's cross-reference list 'Cp. also neo-, nova, novel, novercal, novice, nuncio, innovate, renovate.'\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat s.v. novel, novice, renovate\", \"stance\": \"supports\",\n    \"note\": \"'novel (F. — L.) O. F. novel … L. nouellus, new, dimin. of nouus'; 'novice, a beginner. (F. — L.) F. novice. — L. nouicius, nouitius, new, fresh, a novice. — L. nouus, new'; 'renovate. (L.) From L. renouatus, pp. of renouare, to renew. — L. re-, again; nouus, new.'\"},\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. nouus (nouellus, nouicius, innouō, renouō)\", \"stance\": \"supports\",\n    \"note\": \"'nouicius: novice. Autre terme technique; se dit surtout des esclaves nouvellement acquis'; 'Composés: innouō, innouātiō, renouō … renouātiō'.\"}]})\n\nout = {\"pdf_page\": 364, \"book_page\": 334, \"verified_by\": \"claude-opus-5\",\n       \"verified_on\": \"2026-09-07\", \"entries\": [entry]}\n\nwith io.open(\"data/verification/page-364.json\",\"w\",encoding=\"utf-8\") as f:\n    json.dump(out, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"written\", len(json.dumps(out)))\nPYEOF\npython3 -m json.tool data/verification/page-364.json > /dev/null && echo \"JSON ok\"\npython3 tools/verify_check.py 364"
}
```


### [2026-09-07T19:45:52.576Z] TOOL RESULT

```
written 71018
JSON ok
nodes verified: 12/12
node verdicts: {'confirmed': 8, 'disputed': 2, 'plausible': 2}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 9, 'partial': 5, 'not_found': 1, 'not_checked': 3}
books consulted: {'supports': 27, 'partial': 6, 'silent': 1, 'contradicts': 4} | by book: {'KLN': 5, 'ARY': 4, 'BRT': 3, 'PHD': 3, 'HRN': 3, 'SKT': 3, 'KNT': 2, 'WLD': 2, 'AHD': 2, 'POK': 2, 'LAT': 2, 'HUB': 1, 'BQT': 1, 'IEC': 1, 'NYB': 1, 'MON': 1, 'SOD': 1, 'SYN': 1}
```


## [2026-09-07T19:46:01.360Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; mkdir -p data/verification/sources/refs/ocr/BOOK; cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg364.png data/verification/sources/refs/ocr/BOOK/364.png; git status --short | head"
}
```


### [2026-09-07T19:46:02.657Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-07T19:46:05.611Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; git status --short"
}
```


### [2026-09-07T19:46:05.672Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-07T19:46:09.164Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; git status --porcelain --untracked-files=all -- data/verification | head -20; echo \"---ignored?\"; git check-ignore -v data/verification/page-364.json data/verification/sources/refs/ocr/BOOK/364.png"
}
```


### [2026-09-07T19:46:10.389Z] TOOL RESULT

```
---ignored?
.gitignore:9:data/verification/sources/refs/	data/verification/sources/refs/ocr/BOOK/364.png
```


## [2026-09-07T19:46:14.589Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; ls -l data/verification/page-364.json; git log --oneline -1; git status | head -20; cat .gitignore | head -20"
}
```


### [2026-09-07T19:46:14.661Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 53785 Sep  7 15:45 data/verification/page-364.json
20e351f Verify page 368 (Nogh/nâxon, nail; Nôğ/nâz, nâzok, nugae)
On branch verified
nothing to commit, working tree clean
# regenerable from the PDF via pdftoppm (see tools/)
data/pages/

# built site (regenerate with tools/build_site.py)
site/risheh.html
__pycache__/

# Verification: OCR texts of copyrighted reference works (local audit copies only)
data/verification/sources/refs/
```


## [2026-09-07T19:46:20.829Z] TOOL CALL #81: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; git log --oneline -3 -- data/verification/page-364.json; echo ---; git diff HEAD --stat -- data/verification/page-364.json; echo \"--- md5\"; md5sum data/verification/page-364.json; git show HEAD:data/verification/page-364.json | md5sum"
}
```


### [2026-09-07T19:46:20.961Z] TOOL RESULT

```
20e351f Verify page 368 (Nogh/nâxon, nail; Nôğ/nâz, nâzok, nugae)
---
--- md5
4b359aea5e30e1dfbe3845ff9f0d7bd9  data/verification/page-364.json
4b359aea5e30e1dfbe3845ff9f0d7bd9  -
```


## [2026-09-07T19:46:45.367Z] AGENT

Done. `data/verification/page-364.json` written; `python3 tools/verify_check.py 364` reports 12/12 nodes, **0 PROBLEM lines** (it was swept into commit `20e351f` by the coordinator's commit, byte-identical).

**Page 364 (book 334) — root "Newo / Nu" [Indo-European] "new / new time, now"**

- Root: **confirmed** (POK 769 *neuos "new" + POK 770 *nu- "now"; Pokorny and Walde-Pokorny II 340 themselves call *nu the zero grade of *neuo-, and Watkins writes "newo-. New. Related to nu-.")
- Node verdicts: **8 confirmed, 2 plausible, 2 disputed**; ref checks: 9 supports, 5 partial, 1 not_found, 3 not_checked (unreferenced English boxes)

Disputed:
- **#3 Pahlavi nîvěd "good news"** — real word (MacKenzie p. 60 "niwē [nwyk' | N nuwēd] good news") but wrongly hung on Av. nava- "new"; it belongs to MP niwistan/niwēy- "announce" < *ni-vaid- (Av. ni-vaēdaya-), PIE *weyd-. Horn no. 1053 on the very page Nourai cites for #2 (HRN:236) says "ni + √vaed-"; Wiktionary: Proto-Iranian *wayd-, cf. Parthian nwydg; Aryanpur files it under *neu- "shout" instead. Either way, not *newos.
- **#4 Persian novîd نوید** — the MP→NP step in the chart is correct (and the Hafez couplet is genuine), but the whole branch is misattached for the same reason. Dehkhoda: نِ + Avestan وئید.

Plausible (gloss/routing quibbles, not errors of fact):
- **#7 Germanic neuja "new, now"** and **#8 English "new, now"** — *niwjaz gives only "new"; "now" is Gmc *nu / OE nū, which Watkins and Klein keep under the separate *nu- root, i.e. it should hang on the Nu half directly, not under *neuja-.

Reference notes for the owner (not extraction errors):
- **IEC:842 (node #4) = not_found** — Mann pp. 841-842 hold neuqu-/neur-/neusmn-/neuuō/neuaiō/neuākos/neue; no navīd anywhere. Mann's usable pages are 843-844 (*neuos) and 855 (nú, nūn, "Per. cf. ka-nün, ak-nün").
- **IEC:854** is off by one (the nú/nūn entry is p. 855); **KLN:1059** is the "now" page (Avestic nū, OPers. nūram) — the Avestan nava- half is on KLN p. 1044.
- **MON:4859** unverifiable (no page-mapped scan of the 6-vol Mo'in); entry text checked via MON_part2 and abadis.
- **BQT:2173** is a bullseye — Mo'in's footnote 8 gives «اوستایی nava- (تازه)، پهلوی navak، nōk …»; image + vision transcript saved to `data/verification/sources/refs/ocr/BQT/2173.png` / `2173.vision.txt`.

Extraction: **faithful, no errors**. One layout note — the printed page has an empty box (no language, no words) with an arrow into it to the right of the Old Persian nūram box; the extraction correctly produced no node for it. Page image kept at `data/verification/sources/refs/ocr/BOOK/364.png` (gitignored dir).
