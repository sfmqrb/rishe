# Verification process log — verify-page-236


## [2026-09-06T15:39:21.867Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 236 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-236.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-236.json. Write /home/sfmqrb/git/rishe/data/verification/page-236.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 236` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T15:39:23.090Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T15:39:23.893Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T15:39:23.910Z] TOOL RESULT

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


## [2026-09-06T15:39:24.441Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-236.txt"
}
```


### [2026-09-06T15:39:24.464Z] TOOL RESULT

```
1	=== PDF page 236 (book page 206) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Kakis, Kakus, Kakîna : spike, prong  (refs IEC:599)
4	#1 (parent #0) [Persian] refs=IEC:599 | sagak «سگک» : buckle
5	#2 (parent #0) [Sanskrit] refs=IEC:599 | sakulah : spur on cow's hoof
6	--- entry 1 ---
7	ROOT Kakus -> redirect to Kakis
8	--- entry 2 ---
9	ROOT Kâl -> redirect to Kŭr
10	--- entry 3 ---
11	ROOT Kalwo -> redirect to Kelewo
12	--- entry 4 ---
13	ROOT [Indo-European] Kam 1 : to restrain  (refs IEC:466)
14	#1 (parent #0) [Persian] refs=IEC:466; MON:3076 | kamand «کمند» : halter
15	#2 (parent #0) [Greek] refs=IEC:466 | kĕmos : halter
16	  #3 (parent #2) [Latin] refs=IEC:466 | câmus : halter, yoke
17	#4 (parent #0) [Dutch] refs=IEC:466 | haam : halter
18	  #5 (parent #4) [English] refs=IEC:466 | hame : part of a harness
19	
```


## [2026-09-06T15:39:27.662Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-236.json",
 "description": "Read source JSON for page 236"
}
```


### [2026-09-06T15:39:27.699Z] TOOL RESULT

```
{
  "pdf_page": 236,
  "book_page": 206,
  "entries": [
    {
      "root": {
        "name": "Kakis, Kakus, Kakîna",
        "lang": "Indo-European",
        "refs": "IEC:599",
        "gloss": "spike, prong"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "IEC:599",
          "words": [
            {"translit": "sagak", "gloss": "buckle", "script": "سگک"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "IEC:599",
          "words": [
            {"translit": "sakulah", "gloss": "spur on cow's hoof", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {"name": "Kakus", "redirect": "Kakis"},
      "nodes": []
    },
    {
      "root": {"name": "Kâl", "redirect": "Kŭr"},
      "nodes": []
    },
    {
      "root": {"name": "Kalwo", "redirect": "Kelewo"},
      "nodes": []
    },
    {
      "root": {
        "name": "Kam 1",
        "lang": "Indo-European",
        "refs": "IEC:466",
        "gloss": "to restrain"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "IEC:466; MON:3076",
          "words": [
            {"translit": "kamand", "gloss": "halter", "script": "کمند"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "می نوش و جهان بخش که از زلف کمندت - شد گردن بد خواه گرفتار سلاسل",
            "poet": "Hâfez"
          }
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Greek",
          "refs": "IEC:466",
          "words": [
            {"translit": "kĕmos", "gloss": "halter", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Latin",
          "refs": "IEC:466",
          "words": [
            {"translit": "câmus", "gloss": "halter, yoke", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Dutch",
          "refs": "IEC:466",
          "words": [
            {"translit": "haam", "gloss": "halter", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": "IEC:466",
          "words": [
            {"translit": "hame", "gloss": "part of a harness", "script": null}
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


## [2026-09-06T15:39:28.362Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-06T15:39:28.405Z] TOOL RESULT

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


## [2026-09-06T15:39:31.974Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['IEC','MON','POK','WLD','AHD','KLN','SKT','SYN','LEW','LAT']:\n    print(k, json.dumps(d.get(k),ensure_ascii=False)[:600])\n\""
}
```


## [2026-09-06T15:39:33.216Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i -E \"kakis|kakus|kak[iî]na|sakula|sagak\" IEC.txt | head -50"
}
```


### [2026-09-06T15:39:33.824Z] TOOL RESULT

```
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves
LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt", "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f b
LAT {"title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951", "edition_found": "1951 (3rd ed.) - matches Nourai", "kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "identifier": "ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine (4th ed. 1959 lending-only: dictionnairetymo0000unse; another open copy: DictionnaireEtymologiqueDeLaLangueLatine)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt", "page_offset": "leaf = printed + 18 for mos
```


### [2026-09-06T15:39:33.911Z] TOOL RESULT

```
8538:Kakis, io (Kakus, os, à, Kakina) ‘spike, prong’. Cf. Kakolos and Kaks- WP I, 333 Skt. cf. $akuláh ‘spur on cow's hoof; Per. (dim. form) (?) sagak ‘buckle’; Alb. thek, pl. thaké (fringe'; pl. ʻawns’) beside thekén, f. ‘rye’; Li. Sakà ‘branch’; Sake ‘fork’
8540:kăksā imb, bough, stump, stake’. Cf. Kakis. (Variant: Kiāks-) Skt. $ákhà “branch, limb’; Per. cf. šāx (“branch’, fr. *Kjàks-); OCS cf. (Al soxa ‘stem, branch, stake’; Cz. socha ‘forked pole, plow-handle, statue”
8542:Kak- jump, start, tremble’. Cf. Kak- Skt. $SaS$ami “jump”, cf. sasáh ‘hare’; Arm. sasa- nim ‘tremble’; cf. (?) saws (&bold, spirited’, if fr. a type *KaKus). (Uncertain isophones include Lat. cassus ‘useless’, perh. fr. *Kadsos, Latv. sass ‘unripe’, and Li. Sá3as ‘rash, eczema, scab’, all of uncertain origin)
9138:Ksaks- (variant form of Káksa, q.v. and cf. Kakis “branch; peg, spike" etc.)
13881:quàquos, à, is, variant: quàqulos, quáquilos “a croaking bird’. WP I, 335. Cf. quàg-, quag- Skt. kàkah ‘crow’ beside kakolah ‘raven’; LLat. quácola ‘quail’ beside (gloss) quacoles, pl id.; Mir cáic, m., Ir. cág, m. ‘jackdaw’; Latv kakis, id. (Connexions of OHG wahtala, G Wachtel ‘quail uncertain. Cf. quiriquakos below)
```


## [2026-09-06T15:39:41.916Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 'Kakis, io' in p or ('kamos' in p.lower() and 'kemos' in p.lower()):\n        print('LEAF',i,'-> printed approx', (i-15)*2, (i-15)*2+1)\n# locate the leaf of a line number\nlines=t.split('\\n')\ndef leafof(lineno):\n    upto='\\n'.join(lines[:lineno])\n    return upto.count('\\f')\nprint('leaf of 8538:', leafof(8538))\nEOF"
}
```


## [2026-09-06T15:39:42.516Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -E \"Kam-|Kamos|kemos|kēmos|k[eĕ]mos|camus|câmus\" IEC.txt | head -40"
}
```


### [2026-09-06T15:39:44.064Z] TOOL RESULT

```
LEAF 339 -> printed approx 648 649
leaf of 8538: 339
```


### [2026-09-06T15:39:44.108Z] TOOL RESULT

```
6694:kam- (1) ‘tire, worry’ Gk. cf. kámno, id.; Li. kamuoti, id.; Latv. ka- mot, id. (and 'torment). (For Mod. Gk. kámo ‘do’, and Gk. kmētós ‘made, wrought", see Kam-. Br. kanv, kaun 'sorrow' may be iso- phonic)
6697:beside kamantai ‘wooden parts of bridle’. Cf. variant (*-à-) in Gk. kemós (Doric: -à-) (“hal- ter’. LW in Lat. camus). (OCS xomgotü ‘yoke’ is a LW of Gmc. consonantism, but untrace- able as such. Isophonic: Latvian kamanas, fpl. ‘sledge’: Li. kamanos)
8552:Skt. sale, mp. ‘shine’; Cz. sálat, inf. ‘shine, glow’. An uncertain variant in Lat. caleó, ere ‘be hot! is isolated, but see next entry Kaləd- (Kalod-, Kald-) ‘summer, year. (A form limited to Indo-Íran. Lat. equivalent uncertain). Cf. WP I, 429 Skt. Sarád, f. ('autumn'; in pl. 'years); Av. saroóo, m. ‘year’; Oss. sárd ‘summer’; Per. sal ‘year’; Lydian sardis, id. Uncertainly to Lat. calidus (“hot', an adj. extn. of caleo. See Kàl-) (Kalmos, is, variant of type KImos, q. v. Am- big. in OCS slama, R solóma, H szalma; MHG halm, sm. ‘stalk, haulm'; Du. helm, f. ‘bentgrass’; OE healm as MHG) Kam- "do act, toil, languish’. Cf. kam- (1) and cf. WP I, 387. (Gk. ambig.) Skt. Samyami "be active, toil; Gk. (ambig.) kámno, adj: kmetós (Doric -a-) (make; toil; languish’. Two wds? See kam- (1)); Mod. Gk. kámo ‘do’; Lat. cf. (?) camillus, -a “serving youth or maid at sacrifice) beside (?) camena *poetry, song” (speculations in WH:LEW & EM DELL). (Li. kamuoti, v. ‘weary, bother’ indicates *kam-) Kamios, io “peg, crook, yoke-peg, pintle'. See next Skt. Sámyà, f., yuga-Samyám, n. *yoke-peg'; Arm. sami, -vo, -vov ‘pole, rudder, beam’; samik, pl. form “yoke-peg'; Gk. cf. kámax, -akos “stake, pole, shaft ' Kamos, us (1) “with crumpled or broken horn'. Cf. WP I, 386 and Kamios above Skt. śámah ‘hornless’; Lat. camus, camur & camurus ‘with bent horn’; cf. Gallo-Lat. camox ‘chamois’. (For Lat. camur see WP I, 349) Kamos (2) ‘a fish’ W cf. cem-yw, pl. -ywion, m. ‘male salmon’; G cf. Ham-butte ‘halibut: R som “silure, sheat’; Li. šamas, id.; Latv. sams, id.; Finn. LW cf. sampi ‘sturgeon’ (?) (Kan- (1), variant of type kan-, see kanið and cf. kon-. Gk. ambig. Av. san- ‘destroy’; Gk. kaíno, fut. kanó ‘kill’. Ambig. cf. kanið in view of Cz. kon-, etc.) Kan- (2) ‘sing, hum, bark, echo’. Cf. WP I, 351 Tokh. A. kan ‘melody, rhythm’; Gk. cf. ei-
9043:Kómos, Kõmn- ‘resting, lying, situated; rest, lying, prostration, situation’. Cf. Kam-. (The Gk. evidence is ambiguous, cf. kam-; but the Skt. radical $am- Sam- con- tains semantic contradictions!) Skt. Sámyàmi, v. ‘rest, cease, be quiet? beside (short vowel) Sámah, adj. (1) “working”; (2) ‘tame’; m. ‘quietude’; Av. sàmo, adj. 'seda- tive’; sam-, v. ‘pacify’; Tadjik somon *tidiness,
```


## [2026-09-06T15:39:48.084Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '6690,6700p' IEC.txt && echo \"=== leaf ===\" && python3 - <<'EOF'\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nfor n in (6694,6697):\n    print(n, 'leaf', '\\n'.join(lines[:n]).count('\\f'))\nEOF"
}
```


### [2026-09-06T15:39:49.884Z] TOOL RESULT

```
kals- (2), form of kal- "hard etc. see kal- (4) and kalos (1) Lat. cf. callus “hard”; calleo, Gre ‘be hard, be tough”; Latv. kalstu, kaist ‘dry, wither; grow lean’; kalsens ‘emaciated’; Li. cf. kalstyti, v. ‘buttress’; Du. cf. be-helzen ‘enclose, contain’
kaltos, à (1) “pile, heap' Skt. cf. kattayami ‘pile up”; Br. kalzen ‘heap’; kalza, v. ‘pile’; Cor. calz, calj (-£), id.; G Halde (2) “pile of ore?
kaltos, à (2) (koltos?) ‘leaning; lean, slope, declivity'. Cf. WP I, 430 Skt. cf. katakab (dim. type: ‘slope’); OHG hald ‘inclined’; MHG halt (1) id.; G Halde (1) ‘slope’; Du. cf. hellen ‘tilt; ON halla, v.id.; MHG sich halden ‘sink’; ON hallr leaning, slope’; Li. kaltas ‘sloping, inclined"; káltis, v. “slope, lean’
kaluos, à “bald, bare; skull, head, hil. WP I, 447. Cf. WP I, 433 (Av. kaurvo “black? derives fr. koruos (3), q.v. > Gk. korós, id.); Per. (ambig.) kal ‘bald’; Lat. calvus ‘bald, bare’ beside calva ‘skull’; Osc. cf. Kalaviis (Calvius); MIr. calb ‘head’; Ir. calbh ‘hardness, baldness’; Li. kalvùs *elevat- ed. (Fris. holle ‘head’ may represent a vari- ant of type *kluon). See kluos
kam- (1) ‘tire, worry’ Gk. cf. kámno, id.; Li. kamuoti, id.; Latv. ka- mot, id. (and 'torment). (For Mod. Gk. kámo ‘do’, and Gk. kmētós ‘made, wrought", see Kam-. Br. kanv, kaun 'sorrow' may be iso- phonic)
kam- (2) ‘restrain’; kam-, kamont- “rein, bridle, horse-collar? Per. kamand ‘halter’; Du. baam: E hames ‘horse-collar’ beside MHG hamen, ON hemja
. ‘restrain’; Li. kamanos, kamunos *bridle-bit
beside kamantai ‘wooden parts of bridle’. Cf. variant (*-à-) in Gk. kemós (Doric: -à-) (“hal- ter’. LW in Lat. camus). (OCS xomgotü ‘yoke’ is a LW of Gmc. consonantism, but untrace- able as such. Isophonic: Latvian kamanas, fpl. ‘sledge’: Li. kamanos)
kam- (kom-?) (3) (suffix w. dat.) ‘for the sake of Skt. -kam (in kasmai-kam); OR -ko (in mné-ko. Variant -ka)
467
kām- ‘desire; desirous’. WP I, 325. See next Skt. kamah ‘wish’; kamam ‘gladly’; kamih *woman in love’; Av. kamo ‘desire’; Per. kàm, id.; Arm. kam, kamk, a-st. wd: kamav *willing- ly
=== leaf ===
6694 leaf 267
6697 leaf 268
```


## [2026-09-06T15:40:03.988Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in range(336,343):\n    nums=re.findall(r'^\\s*(\\d{3,4})\\s*$', pages[i], re.M)\n    print('leaf',i,'standalone nums:',nums)\nprint('---- leaf 339 head ----')\nprint(pages[339][:1500])\nEOF"
}
```


### [2026-09-06T15:40:05.735Z] TOOL RESULT

```
leaf 336 standalone nums: ['392', '593']
leaf 337 standalone nums: ['594', '595']
leaf 338 standalone nums: ['596']
leaf 339 standalone nums: ['598', '599']
leaf 340 standalone nums: ['600', '601']
leaf 341 standalone nums: ['602', '603']
leaf 342 standalone nums: ['604', '605']
---- leaf 339 head ----
all, sink, fail’; cf. caries (decay: Skt. Sadah “fall, shedding’) and cassus *'use- less?
kado “annoy, torment'. See kådos and next. WP I, 340, 378 & 513 Gk. kédo, id.; W coddi, 3s: *cawdd, id.; Cor. coedhy, id.; ON hóta ‘threaten? OCz sádati ‘smart, pain’; R cf. do-sadit', -sazdàt ‘annoy’; do-sada, f. ‘annoyance’
(Kad-, possible alternative to type kad-, q. v.)
Kādos, -es- ‘vexation’. See Kado. WP I, 340 & 378 Av. cf. sadra, f., sadrom, n. ‘distress’; Gk. kēdos (Doric: -à-), n. id.; Ir. cáidhe, f. 'blem- ish’; Br. koez ‘annoyance, regret, pain’; W cawdd, pl. coddion, m. ‘annoyance, insult;
kuókuo (kuuokuuo) — Kak-, Kakt-
25
30
35
40
45
598
chinno, àre (metath. vocalism in Fr. chicaner fr. *cichannare), id.; OCS xoxotati, id.; OHG cf. (unshifted initial in) kachazzen, kichazzen khokhl- (1) (khokhlaio, khokhleuo) ‘gurgle, bubble, boil. Onomat. Gk. kokhlázo, id.; OCS xoxlujo, -ovati, id. See next khokhl- (2) “turbine, spool, whirring object, whirlwind'. Same as (1) ? Gk. kokhlías, m. “reel, spiral; OCS xoxiülü, xoxolü *whirlwind'
Cor. coedh, m. “sorrow; OS cf. hoti, adj. (hostile, but of ambig. consonantism. See kad-); ON hót, npl., Sw. hot, n. (threats; threat, but see kad-); R cf. do-sàda “annoy- ance'
(Kadris, à (?), Katr- (?). See Katris, a. All evidence for this form ambig. Arm. sait, i-st. ‘edge of knife’; Oss. sart ‘chisel’: Alb. thadër, f. faxe-adze'. This is the only form indicating *Kadr- unambiguously. For Arm. sait cf. perhaps Skt. a$rih ‘edge’ by me- tath.)
Kaisros
```


## [2026-09-06T15:40:22.563Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== POK sakula/sakha ==\" && grep -n -i -E \"sakulá|śakula|sakula|çakula\" POK_full.txt AHD_watkins1985.txt SYN.txt 2>/dev/null | head -20; echo \"== POK kāk- Ast Pflock ==\"; grep -n -E \"k[ʼ̑̂]?āk-|kā̆k-|Ast, Pflock\" POK_full.txt | head -20"
}
```


### [2026-09-06T15:40:22.645Z] TOOL RESULT

```
== POK sakula/sakha ==
== POK kāk- Ast Pflock ==
```


## [2026-09-06T15:40:25.053Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== WLD Bd1 p333 area ==\"; grep -n -i -E \"sakula|çakulá|Sporn am Fuß|Klammer\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -20; echo \"== WLD Bd3 index ==\"; grep -n -i \"sakula\" WLD_band3.txt | head"
}
```


### [2026-09-06T15:40:25.150Z] TOOL RESULT

```
== WLD Bd1 p333 area ==
24200:schat in Klammern) „plaudern“ (Fick I 3 516, I 4 28, 390, Curtius 5 159, 
31049:klammern“), lett. kl'iistu , IT tit „(hangenbleiben), (wohin) gelangen, werden“, 
31063:Klammer“, alt kljuc-im,-iti ..biegen, krummen“ (usw., s. Berneker 528 f., 
33444:„umklammern, fest- und zusammenlialten". 
33503:den sein, gut passen" aus „umklammern, fest- und zusammenhalten" ent- 
33508:ai .gadhya- „festzuhalten“, a-gadhita- „angeklammert", pari-gadliita- ,.um- 
33509:klammert" (Sommer Hdb. 2 242 verbindet damit kaum richtig lat. mani- 
37069:„Draufgabe oder dgl." ist aufzugeben), liedera ,,Epheu" („klammernd"; zum 
38581:beclingan .,einklemmen, fesseln ', engl. cling „sieh anklammern, festhalten ; 
38583:klammern"), norw. mdartl. klengia „sich anklammern; verfolgen; klettem", 
38585:anklammern"), ahd. klinga , nhd. Klinge .,enge Schlucht, Klamm" (auch 
38688:fest anklammern"). nd. klateren, klatteren ds. (aber nhd. klettern samt 
38803:mhd. klamben ,fest zusammenfiigen, verklammern", klambe „Klemme, 
38804:Fessel, Klammer", anord. klambra, Membra „zwangen, einschlieBen", Mombr 
38805:„Schraubstock, Klenune, Enge“, mhd. klcmberen „verklammern“, mhd. nhd. 
38806:Klammer; engl. dambcr „klettern", eigentlich „sich festklammern", wie auck 
38814:zusammenziehen, zusammendrucken, einengen"; ahd . klampfer , Klammer", 
38825:klampe „Klumpen, Klotz * (nhd. Klampe ,, Klammer, Krampe, Haken, Klotz £ 
39041:anheften, anklammern )“, mndl. eleven ds. ; ahd. kliba, as. klira, ags. clife 
42448:sein ', oder besser zu ghulli [„vereinigen“ und] „umklammern, festhalten'; 
== WLD Bd3 index ==
```


## [2026-09-06T15:40:29.982Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(len(pages))\n# find page whose content has standalone 333\nfor i,p in enumerate(pages):\n    if re.search(r'^\\s*333\\s*$',p,re.M):\n        print('candidate leaf',i, p[:200].replace('\\n',' | '))\nEOF"
}
```


### [2026-09-06T15:40:32.490Z] TOOL RESULT

```
895
```


## [2026-09-06T15:40:34.868Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (340,345,350,355,360):\n    print('=== leaf',i,'===')\n    print(pages[i][:300])\nEOF"
}
```


### [2026-09-06T15:40:36.962Z] TOOL RESULT

```
=== leaf 340 ===
       )                                                          ,              .                                                                                                             :




332                                                                       qaul-. qul                qau
=== leaf 345 ===
              :




                                                                  qagli-                                                         337

     Alb. kets, kats „Ziege‘, k’ed-dt m. ,,Bocklein", geg. k'id-di ds. bleibt wohl
fern tvgl. G. Meyer Alb. Wb. 185, Pedersen                     
=== leaf 350 ===
           -




342                                                     qap-


,,Hafi" (docliauch u. *kad- „seelische Yerstimmung") ags. hcedre „sorg-
                          s.                                                   ;


               ahd. Imota „die Hut, Obhut, Bewachung", ags. hod, 
=== leaf 355 ===
                      -                                    -               -




   Vgl. Fick II 3 51, I 4 19, Curtius 5 148, Solmsen Beitr. I 198, Yf. LEWb. 2
u. caput-, fern bleibt lit. kopustas „WeiBkohlkopf“ (trotz Johansson IF. 14.

336; vielmehr wie nhd. kabis aus slav. kapusta wesentlich auf 
=== leaf 360 ===
352                                   qand-, squand- (s'lqend-


*kqp-to- zu gr. y.afinrj „Biegung“,
                              lit. kaihpas „Ecke, Winkel" (Wz. qamp-                       ;


Zubaty AfslPk. 16,396, Brugmann 1 2 583), auch schwerlich aus lat.-rom.
cantus „Ecke“ entlehnt.
  Auf Gr
```


## [2026-09-06T15:40:41.932Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (341,342):\n    print('=== leaf',i,'===')\n    print(pages[i])\nEOF"
}
```


### [2026-09-06T15:40:44.979Z] TOOL RESULT

```
=== leaf 341 ===
                       -                                                        ;                                      ,




                                               qau(e)la    :   quia           — kaq- (keq-V)                                    333

qua(A)la : quia ,,Gesehwulst; bes. Leibschaden. Leistenbruch".
    Gr. jon. y.ijfo], att. xd/.g „Geschwulst, bes. Leibschaden", yovgrovg-
y.)]h] „Leistenbruch" u. dgl., xala&i oyxovxai. Ay/uoi, Hes.. y.aJ.aga Syxos
                                                                          ’




Hes. (vokalisch sehr schwierig; jon. y.rjh] aus *y.af-e/.-a. att. ach. xti).-g. -a
aus xaf.-ek-dl Kretschmer KZ. 31, 471 f zw.; ist eher *xayaka gemeinsame
Gdf., mit Riickenverwandlung von uratt. *y.dja/.a zu *xd^ald durch Assi-
milation an das folgende a? Hirts, Abl. 38, Annahme sekundaren Ablauts
fiir att. yah] setzt irrtiimlich a voraus)

    anord. haull, ags. heala ahd. hoia ,,Leistenbnich“ ( *qau\d\lcL allenfalls
                                                 ,



*qDn.dy<l);           tiefstufig         ksl. Icyla „ds.‘
                                                                     ;

                                                                          ;
                                                                               russ ./did     ..ds. :   Knorren am Baunv.
                                     4                4
serb. kl la           ds.Fick I           377, III             66.
   Ir.   ciil,        cymr.    cil   lat. alius (Rozwadowsky Rozpr. Ak.
                                         „Riieken ;< und
Krak. II. Ser., tom X, 420 f., Pedersen KG. I 50. 2S3; ..die Krankheit ist
nach ihrem Sitz genannt", was aher sachlich niclit stimmt) s. vielmehr
unter (s)qeu ,.bedecken“.

kaq- (keq-?) r vermogen. helfen".
  Ai. cakndti „kann, ist im Stande,                                             hilft",    Desid. dk&ati          ,.hilft,   huldigt.
dient, lernt"',            t/iktl-       f.   „IIilfe",        rakrd- ..vermogend”, ray ml- ,,vermdgend.
hilfreich", ran f. „Yermogen, Hilfe"', cdka- m. ..Kraft. Hilfe", raka- ..kriiftig.
helfend; m. Heifer"', cukman-       Hilfe", rakvuru- ..stark" (wenn cikvd-, <;i Ir-
                                                          ,,


fan-. cikvas- „tiichtig, geschickt" bedeutete und z. B. nach Pedersen KZ.
36, 82 f., Uhlenbeck Ai. "VVb. 309 anzureihen ware, wiirde i trotzdem kaum
nach Pedersen aaO. die Bed.-Stufe zu rule- sein konnen wegen cak-\ eine
andere Bed. „Holzhauer“ gibt Wackernagel Ai. Gr. I 17 nach Bergaigne
Msl. 8, 356 a 6, aber mit unannehmbarer Etymologie)                av. sacaiti ,.ver-                      ;


steht sich worauf", Desid. sixsaiti lernt", saxta- = ai. raktd- „ vermogend".
                                                                     ,,


np. saxt ,,hart, fest, sehr". Ganz fraglich lat. car ala ,,Offiziers- oder Soldaten-
aufwiirter zu Felde".       Unsicher auch lit. kankii, kdkti ..wohin gelangen.
geniigen, hinreichen" (Reihenwechsel ?) und ags. harjan ..genitalia", mhd.
haejen       „Zuchtstier"            (..Potenz"?                s        u.    leak-      ..mannliche          Geschlechtsteile";.
Ebenso, weil nie ausl. -h-, sondern nur -g- bietend, die germ. Sippe aisl.
hngr .passend, geschickt". hagr m. ,.Lage. Verliiiltnis, Bequemlichkeit".
         ,



hnga ,.anordnen", hogr, hogr ..passend, bequem", hfit/r (*hahtu~) ..Art und
"SYeise"      (wiire          tu- St.         neben dem              ti-St.         ai.   <jakli-).     ahd. st. Ptc. ki-hagnt.
bihagan ..heiter", mhd. behagen ..passen, recht sein”. nhd. behagen. mlid.
hagr, m.     Behagen. ’Wohlgefallen", as. btliagon ..behagen. gefallen", ag*.
                 ..


onhagian ..passen, behagen", gehagian unpers. ..Gelegenheit sein"; unter
Annahme von ausl. -gh- vergleicht Zupitza Gutt. 104 sie mit prakr. ca
„ist fiihig“, Acokainschr. cughati ,,ist zu etwas bereit, willig". av. cayxl-
(^mit raf.idrom) ..Hilfe gewiihrend", Uig.nnan- n. ..Geschenk", lagvah- ..bietend.
gewiihrend" (Bartholomae Air. Wb. 576). die freilieh wiederuin in ihrem
e-Yokalismus nicht so unmittelbar zum germ, u u stimmen.                                        :




   Uber die von Bugge und Thurneysen mit hagr usw. verbundenen lat.
colnt-s, osk. kahad s. u. gagh- ..getlochtene Hiirde".

   Yanicek LEWb. 2 65, Fickl 4 41, 419. II 4 58 ir. odtl ..Kraft" bleibt fern ).
III 4 6S. Uhlb. Ai. "VYb. 301 (aber lit. Mtnk'mfi. dt. Hcngst s. u.                                              icily- ..springen-;.

Bgm. IF.          1   9. 385. Yf.        LE\Yb. 2 u. eanda. rohvs. Falk-Torp. u. hag. hgntlr. btfirc.

=== leaf 342 ===
334                                                qak   — kaq-      :   kaq-, ka[i]q   :   klq


qak- ..abmagern".
  Av. Icasu- ..klein. gering", komp. Sup. kasyah-, kasista- (aber gr. y.ay.6 g,
Hiibschmann Yokalsyst. 154, eher zu *kakka- ..cacare",; lit. nukusHi „ganz
entkraftet werden", nhd. huger (Trautmaun ZfdtAVtf. 7, 267, KZ. 43, 153;
andere Deutungen von huger s. bei Yf. LEWb. 2 u. craccntes, Berneker 133,
der es zw. mit russ. cachnufa ..dahinsiechen, abmagern" aus *qcq-s- ver-
bindet, das aber dehnstufige Kebenform von -ceznutb „schwinden, ver-
sehwinden" sein wird, mit eh statt s nach sochnutb sychnutb ,,vertrockneu“).                 ,




kak- ..mannliche Geschlechtsteile"?
  Ags. hagan „genitalia", mhd. lutgen „Zuchtstier", nhd. mdartl. h<gd ds.,
haksch           ,
                     Zuchtsehwein", nhd. hecken „sich paaren (von Vogeln)", engl. hatch,
ahd. hegidraosa ..Hode"                             (nicht        besser dariiber Siitterlin, s. u. koksa: und
Bezz.            GGA. 1S9S, 555: wegen                            der „Hagedriise am Halse" vielleicht zu
lit.   saibaudys ds.;                       doch
                                        „Schorf" keine befriedigende Bed.-
                                                    liefert       sciias
A^ermittlung mit „Hode"); vielleicht dazu    lett. leukale „Hodensack, penis“;

dagegen russ.-ksl. kocam „membrum virile' ist in dieser Bed. nur einmal           1




belegt und (wie alb. hots ds., G. Meyer Alb. Wb. 203) Ubertragung aus der
sonstigen Bed. „Kohlstrunk u. dgl." des AVortes (vgl. dt. vulgar Stengel").                                               ,,

    r
   A gl. Kluge 8 u. Hecke 2 , Zupitza Gutt. 104, Bezzenberger GGA. 1898,
                                                                           r
555, Berneker 527.     Unsicher, und auch wegen des beschriinkten A er-
breitungsgebietes kaum als sehr alt zu betrachten. Schrader ZfdtAVtf. 1 238 f.                                                 ,


stellt hagen hegel zu ai. caknoti „vermag", eakrd- „kraftig“, erwiigenswert.
                        ,


Vgl. aber Miihlenbach-Endzelin Lett.-D. AVb. II 137, Buga K. ir s. I 192.

 kaq-        :   kaq-, wahrscheinlich ka[i]q- : klq- mit koq- als Ablautneubildung von
         kueq-         aus „springen, hervorsprudeln, kraftig sich tummeln ‘.                                     !




       Gr.       y.rjy.ico                       y.dy.tor Idgovvag/oyai. Aaxcoveg
                                     ,,entspringe, sprudle hervor",
 lies., y.yyJg, -idog, dor. y.dy.fg         hervorsprudelnde (Blut; Purpursaft;
                                                             f.   ,,alles

ausbratendes Fett; Dampf)"; lit. soldi „springen, tanzen"; nasaliert ian-
                                                                   4
kt'ts ..Sink", sank inti ,,(ein Pferd) springen machen" (Fickl       420) und ahd.
henjist ags. h digest ..Hengst", aisl. hestr ..Pferd", eig. Sup. „am besten
                 ,




 springend, bespringend" (Lit. bei Falk-Torp u. hest'e
   Fur kaiq- klq- spricht das wohl thrak. phryg. oixiv(v)ig „Tanz der Satyrn
                             :




 zu Ehren des Dionysos" (zwar < bei den Lex., aber Eur. Cycl. 37 auch
 mit l meBbar; Fick Spracheinh. 415, Solmsen Beitr. 145 Anm. 1), w'ohl
 auch xly.vg „Kraft"', genauer ..Beweglichkeit, Frische", y.ly.vor zayvrio, la-
 yvoj Zonar., op. jon. ay.iy.vg -v og „schwach, schlapp" (Solmsen aaO., gegen
                                                         ,



 die in der Bed. unbefriedigende A^erbindung mit y.vog „fetus‘     AVz. keu-,                                         ,


 bei Curtius 5 157 f. u, a.).
    Zu scheiden von (y')qeq- ,,springen" (s. d ; auch Zupitza KZ. 37,401 be-
 trachtete aksl. skoko ,, Sprung' gegeniiber lit. soldi als einen Fall von
 westidg. Guttural im satem. Gebiete). Av. salaiti ..geht :zeitlich) voriiber
 (Fick aaO.. Zupitza aaO.. Prellwitz 2 219 f.) bleibt fern (s. Bartholomae
 BB. 13, 59, Airan. Wb. 1 553 f.). Aicht einleuchtend Fay IF. 32, 331 (y.rjy.ico                                                      :



 ai. mrayd- .,unaufhorlich, unversieglich" als „effundens‘-) und Pedersen KG.

 I 51            yJy.vg          :   ir.   rich ..weibliche        Brust".      cymr.       eig,   bret.   kik,           acorn,   chic
 „Fleisch").
```


## [2026-09-06T15:41:03.486Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls | head -60; echo ---; grep -c . POK_full.txt; grep -n -i -E \"Ast, Pflock|Pflock, Pfahl|śākhā|sakha|k.ak-\" POK_full.txt | head -20"
}
```


### [2026-09-06T15:41:03.580Z] TOOL RESULT

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
58425
31716:Armenian Ara/r "fire, glowing coals' (< *guro-, *gura-), krak-aran^ siove, hearth, fireplace, 
43943:"scurf' = bret. (Vannes) krah^ small hill, cusp, peak' {*krak-, *krakk-, perhaps through 
46058:Church Slavic (etc.) kracu, krakati 6s.; in addition slovz. krek {*krak-b) m. 'raven'. 
48742:manner)', diminutive (^ krak-al-ec) karkalec^ grasshopper' Slavic loanword. 
48970:Root / lemma: kuak- 
49514:Material: Old Indie sakhai. "bough' (: Gothic hoha, Armenian caA); sakala-xx\. n. "chip, 
49523:Indie sakha; after Meillet Esquisse2 36, Slave commun^ 23 f. rather from Indo Germanic 
49535:Gothic /7o/7a "plough' (= Old Indie sakha). Old High German huohili^ a small arable field 
49539:Lithuanian saAa "bough' (ablaut, with Old Indie sakha), sake^ fork ', saAa/ys "splinter' (: 
72889:because of Aryan A/? dubious: Old Indie sakha {sakhi-) ' fellow, comrade, friend',
```


## [2026-09-06T15:41:07.065Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '49500,49550p' POK_full.txt"
}
```


### [2026-09-06T15:41:07.119Z] TOOL RESULT

```
honor of the Dionysos ' (namely /by Lex., but Eur. Cycl. 37 also may be evaluated with /), 
probably also kTkuc; f. " power ', accurate " flexibility, briskness', kTkuu) tqxuvu), iaxuu) 
Zonar, ep. Ionian qkIku^, -\joc, 'weak, flabby'; 

Pedersen KG. I 51 places here (kTku(;:) Irish cTchi. " female breast', cymr. cig, bret. kik, 
acorn, c/7/ic "flesh'. 

References: WP. I 334, Hofmann Etym. Gr. Wb. 142, Kluge^i s. v. Hengst. 
Page(s): 522-523 

Root / lemma: Rak-2, nasalized Rank- 

Meaning: branch 

Material: Old Indie sakhai. "bough' (: Gothic hoha, Armenian caA); sakala-xx\. n. "chip, 

splinter, splinter, wooden log, schnitzel, shred' (: Lithuanian sakalys); sa/jku-m. " wooden 

nail, peg, plug, picket, pole, stick ' (: Old Church Slavic sgkb, cymr. ca/nc, Old Norse ha/); 

sakti-i. "spear, javelin' (: Old Irish cecht); 

Armenian c5A'"twig, branch', perhaps loanword from pers. sax6s., and these from Old 
Indie sakha; after Meillet Esquisse2 36, Slave commun^ 23 f. rather from Indo Germanic 
*ksakh-\ 

because of the meaning doubtful alb. //7e/re "fringe, tail ', compare after all the same 
meaning from Norwegian heker corner, tail' under *keg-, 

cymr. cainc{*kanku, compare i/-stem of Old Indie sarjku-), PI. cangau, mcymr. canghau 
"bough'. Middle Irish gee, nir. ^ea^" bough' (with secondary voiced-nonaspirated in aniaut), 
with -sk- suffix gallo-rom. *gascar/a {French Jachere) " arid land', actually " arable field ', 
Hubschmied Vox Rom. Ill 123^; Old Irish gescae^bN'\g, branch, bough'; with /-suffix Old 
Irish cec/7/ "plough' (probably as */r5/7/r-/c»- next-related to Old Indie sakti-); 

Gothic /7o/7a "plough' (= Old Indie sakha). Old High German huohili^ a small arable field 
'; nasalized Old Norse har^ oarlock' {*hanha, Finnish loanword), hse//^peg, plug, stick' 
{*hanhila-); 

Lithuanian saAa "bough' (ablaut, with Old Indie sakha), sake^ fork ', saAa/ys "splinter' (: 
Old Indie sakala-), saknis. Old Prussian sagn/st, Latvian sakne \oot'; Lithuanian sakarnis 



' brachiating ', Latvian sakarnis^ Wurzelenoe '; Old Church Slavic *SQkTD " a tender young 
twig, branch, shoot, sprout, sprig '; 

Slavic 5c»c/7a"club, cudgel (Old Church Slavic etc.), hook, plough (russ.), Gabelstange ' 
(poln.), poln. rozsocha^ forked bough'. Old Church Slavic pc»sc»c/7bm. "cudgel, club'. 

References: WP. I 335, Trautmann 297 ff., Specht Indo Germanic Dekl. 55, 254;
```


## [2026-09-06T15:41:27.081Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== HRN sagak/kamand ==\"; grep -n -E \"sagak|sagäk|kamand|kamänd\" HRN.txt HUB.txt CHEUNG.txt PHD.txt PHD_mackenzie.txt NYB_vol2_glossary.txt BRT.txt 2>/dev/null | head -30\necho \"== KLN hame/camus ==\"; grep -n -E \"^hame|hames|\\bcamus\\b|kemos|kēmos\" KLN_1966.txt SKT.txt | head -30"
}
```


### [2026-09-06T15:41:27.168Z] TOOL RESULT

```
== HRN sagak/kamand ==
PHD_mackenzie.txt:5944:amass handoxtan.                          archer kamandar.
PHD_mackenzie.txt:6102:bowman kamandar.                       Buddha but.
PHD_mackenzie.txt:9518:kamandar             \.ut-6~          kirih-               -~~
== KLN hame/camus ==
SKT.txt:2446:Bumboat.  (E.)  From  6um  and  boa/. Grig,  a  scavenger's  boat  on  the  Thames (A.  t).  1685);  afterwards  used,  to  supply vegetables  to  ^hipt-
KLN_1966.txt:6311:‘a  bending’.  See  camp,  n. camus,  camuse,  adj.,  short  and  flat  (said  of  the nose)  (obsol.)  —  F.  camus,  fern,  camuse,  ‘flat¬ nosed,  snub-nosed’,  formed  from  pejorative pref.  ca-  and  the  base  of  museau,  ‘muzzle,  snout’. See  muzzle.
KLN_1966.txt:17132:from  the  stem  of  dpotp-rdveLv,  ‘to  miss  the  mark, fail  of  one’s  purpose,  err,  sin’,  which  is  of  un¬ certain  origin  (for  sense  development  cp.  Heb. hatd'  ‘he  sinned’,  prop,  ‘he  missed  the  mark’); cp.  Nemertinea.  The  second  element  comes  fr. -Xoyop,  ‘one  who  speaks  (in  a  certain, manner); one  who  deals  (with  a  certain  topic)’ ;  see  -logy, hamburger,  n.,  1)  ground  beef;  2)  cooked  patty of  ground  beef;  3)  sandwich  made  of  such  a patty.  —  Short  for  Hamburger  steak;  named after  Hamburg  in  Germany, hame,  n.,  either  of  the  two  curved  pieces  lying round  the  collar  of  a  horse.  —  ME.  hame,  fr. OE.  hama,  ‘cover,  skin’,  rel.  to  MDu.  hamme, Du.  haam,  ‘collar  of  a  horse’,  ON.  hamr,  ‘skin, covering’,  OHG.  hamo,  of  s.m.,  OHG.  hemidi, ‘shirt’,  and  cogn.  with  OI.  samulyah,  ‘woolen shirt’;  fr.  I.-E.  base  *kam-,  *kem-,  ‘to  cover’. See  heaven  and  cp.  chemise, hamesucken,  n.,  assaulting  of  a  person  in  his  own dwelling  house.  —  ME.  hamsoken,  fr.  OE.  hdm- sden,  compounded  of  ham,  ‘home’,  and  socn, ‘attack’,  which  is  rel.  to  ON.  sdkn,  of  s.m.,  and to  OE.  secan,  ‘to  seek;  to  try  to  get,  attack’.  Cp. OFris.  hamsekenge,  ‘attack  on  a  house’,  G. Heimsuchung,  ‘visitation’,  and  see  home  and seek.
KLN_1966.txt:17133:hametz,  also  chametz,  n.,  leavened  food;  for¬ bidden  during  Passover  ( Jewish  religion).  — Heb.  hametz,  ‘that  which  is  leavened’,  from  the stem  of  the  verb  hametz,  ‘was  sour,  was  leaven¬ ed’,  which  is  rel.  to  Aram,  huma  ,  of  s.m.  (pas¬ sive  part.  hamta' ,  ‘leavened’),  Arab,  hamuda, ‘was  sour’.
KLN_1966.txt:17966:of  homo,  ‘man’.  See  homage, home,  n.  —  ME.  home,  hoom,  fr.  OE.  ham,  rel.  to OS.  hem,  ‘home’,  OFris.  hem,  ham,  ‘home,  vil¬ lage’,  ON.  heimr,  ‘residence,  world’,  heima, ‘home’,  Swed.  hem,  Dan.  hjem,  MDu.  heem, heim,  OHG.,  MHG.,  G.  heim,  ‘home’,  Goth. haims,  ‘village’,  and  cogn.  with  Gk.  xcopr),  ‘vil¬ lage’,  xoipav,  ‘to  lull,  put  to  sleep’,  Lith.  kaimas , OPruss.  caymis,  ‘village’,  OSlav.  semija,  Lith. seimyna,  Lett,  saime,  OPruss.  seimins,  ‘domestic servants’,  OIr.  coim,  coem,  ‘dear,  beloved’,  OW. cum,  ModW.  cu,  of  s.m.,  L.  -haemum  (a  Teut. loan  word)  in  Boihaemum,  ‘Bohemia’,  lit.  ‘home of  the  Boi’ ;  formed — with  -m-formative  element — fr.  I.-E.  base  *fcei-,  ‘to  lie,  settle  down’,  whence also  Goth,  heiwa-frauja,  ‘master  of  a  house’,  OE. hi  wan  (pi.),  ‘members  of  a  family’,  hiwen,  ‘family, household’,  OHG.  hi  wo,  ‘husband’,  hiwa,  ‘wife’, hiun  (pi.),  ‘married  couple’,  ON.  him,  ‘married couple,  household’,  OE.  higid,  hid,  ‘hide  of land’,  lit.  ‘land  (sufficient)  to  support  a  family’, OE.  hiw-rseden,  hi-red,  ‘family,  household', OHG.,  MHG.  hi-rat,  G.  Hei-rat ,  ‘marriage’, orig.  ‘care  of  the  house’  (the  second  element  of these  latter  words  means  ‘advice,  counsel’;  see rede,  n.),  and  L.  civis,  ‘citizen’.  See  civil  and cp.  the  first  element  in  comedy.  Cp.  also  ham, ‘hamlet’,  hamesucken,  hamlet,  haunt,  Henry, hide,  ‘measure  of  land’,  hind,  ‘farm  servant’, Bohemia.  Cp.  also  erne,  oom.
KLN_1966.txt:18220:humble, adj.  —  ME.  humble,  umble,  fr.  OF.  (=  F.) humble,  fr.  L.  humilem,  acc.  of  humilis,  ‘low, base,  humble’,  lit.  ‘on  the  ground’,  fr.  humus, ‘earth,  ground,  soil’.  See  humus  and  words  there referred  to  and  cp.  esp.  humiliate,  humility. Derivatives:  humble,  tr.  v.,  humble-tiess,  n., humbl-er,  n.,  humbl-ing,  n.,  humbl-y,  adv. humblebee,  n.,  a  bumblebee.  —  ME.  humbyl-bee, a  compound  whose  first  element  is  rel.  to  Dan. humle,  humlebi,  Swed.,  Norw.  humla,  MDu. hummel,  homel,  hommel,  Du.  hommel,  OHG. humbal,  MHG.  humbel,  hummel,  G.  Hummel, ‘humblebee’,  prop,  ‘the  humming  bee’.  See  hum, ‘to  utter  an  inarticulate  sound’,  and  freq.  suff. -le,  and  cp.  Czech  (mel,  Pol.  czmiel,  OPruss. camus,  Lith.  kamane,  ‘humblebee’,  which  are also  of  imitative  origin.  For  the  second  element in  ME.  humbyl-bee  see  bee. humble  pie,  pie  made  of  the  umbles  of  a  deer.  — For  umble  pie,  ‘pie  made  of  umbles’.  Cp.  umble pie,  umbles  and  see  numbles.  The  h  in  humble pie  is  due  to  a  confusion  of  umble  with  humble, ‘low’.
```


## [2026-09-06T15:41:28.526Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== MON سگک/کمند ==\"; grep -n \"سگک\" MON_part1.txt MON_part2.txt BQT_v1_pages.txt BQT_v2_pages.txt 2>/dev/null | head -20; echo \"== kamand fa ==\"; grep -n \"کمند\" MON_part1.txt MON_part2.txt BQT_v2_pages.txt 2>/dev/null | head -20"
}
```


### [2026-09-06T15:41:28.611Z] TOOL RESULT

```
== MON سگک/کمند ==
MON_part2.txt:8743:فناء: 007 (ع. ف. فنا] (.) (کیا.) سگک 
MON_part1.txt:78799:سگک 1 ( کد.) حربص» سک طماع» اهل 
MON_part1.txt:78815:افاده. سگک و گربه: (عم.) دو کس که با 
MON_part1.txt:78894:سگک: 528-1 (ا.مسصف.) سک کوچک. 
== kamand fa ==
BQT_v2_pages.txt:2143:‫مهمیز » بمعنی کمند باشدو عرب مقود خوالند‬                                                         ‫باقلای تر یز ند‬
BQT_v2_pages.txt:2296:‫وزن مویز » بمعتی کمندیاشد‬          ‫جلیز سبر‬
BQT_v2_pages.txt:2325:  ‫_ « جله چون سماروغ بود‪ ».‬رك ‪ :‬لفت فری‬                                                   ‫(کمند) السب است ‪.‬‬
BQT_v2_pages.txt:3748:  ‫بکوهی در انداختن‪ .‬نظامیکنجوی‪.‬‬           ‫کمندی‬    ‫‪ - ۱‬ده چابك شد ابن چایکی تاختن‬
BQT_v2_pages.txt:5993: ‫چهند ب بفتح اول و ثالی بروزن کمند»‬
BQT_v2_pages.txt:7464:             ‫ابا زين وبیحان کمندی دراز ‪...‬‬                ‫مشد کرد چوبان و دوکره تاز‬
BQT_v2_pages.txt:9473:                                                          ‫و کنانه‬    ‫وکمند ریسمان بلند را همگفته الد‪-‬‬
BQT_v2_pages.txt:9959:                  ‫کمندی دشت بر گوران خباک‬                      ‫خدنگش بیشه برشیران قفص کرد‬
BQT_v2_pages.txt:11587: ‫خر فك ‪ -‬بروزن کمند‪ .‬کیاهی‌باشد مانشد‬                                                     ‫خرمنها بگدابی روند‬
BQT_v2_pages.txt:23990:‫رسام = با تشدید ثالی بر وزن قام »‬                           ‫ری ‪٩‬‏ و‪-‬طناب و کمند ورسن را لیز‬
BQT_v2_pages.txt:29004:               ‫مجیانند خون ازآ جا بمکد ‪.‬‬          ‫(‪ )۱‬است خودرا حاشق و دل او را بکمند خود‬
BQT_v2_pages.txt:31075: ‫رزغند = بروزن کمند › آواز پلند مهيب‬
BQT_v2_pages.txt:37907:    ‫=ر وزن کمنده رلگی‌باشدیزردی‬
MON_part1.txt:28730:رود؛ کمند» پالاهنگك» قباد» مقود. چرمی که 
MON_part1.txt:36124:کمند و زلف می‌باشد» پیچ و شکن. خلل» 
MON_part1.txt:48147:بر : 121012 [- جلو یز - جلیز ] (ا.) کمند» 
MON_part1.txt:48230:جلویز: 1۷2 (- جلبیز - جلیز ] (ا.) کمند» 
MON_part1.txt:55144:نداده باشند. چرم دباغت ناکرده. کمند 
MON_part1.txt:57367:تاب. چین و شکن (زلف» گیسو» کمند و 
MON_part1.txt:63390:جانوران؛ چرم. حیله» مکر. کمندهایی که در
```


## [2026-09-06T15:41:41.253Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '78890,78900p' MON_part1.txt; echo \"=== 78795 ===\"; sed -n '78795,78805p' MON_part1.txt"
}
```


### [2026-09-06T15:41:41.321Z] TOOL RESULT

```
آنکه دارای سری مانند سک باشد. قومی 
افسانه آمیز که سر افراد آن مانند سک بود. 
دنبابر ست» طالب دنبا: 

سگک: 528-1 (ا.مسصف.) سک کوچک. 
نوعی قلاب چهارگوش يا نیم‌دایره که برای 
بستن کفش,» پوتین و کمربند لباس بکار رود. 
سگ‌ماهی: آنقد (امر.) (جان.) یکی از 
ماهی‌های حلال گوشت و فلس‌دار و 
استخوانی بحر خزر که فلس‌هایش بزرگ 
است و به آسانی می‌افتد. قدش بین ۱۸ - 
=== 78795 ===
شکاری» سگ پلیس و سک خانوادگی که 
جهت حفظ و گاهی به عنوان تجمل 
نگهداری می‌شود؛ کلب. ترکیبات اسمی: 
سک آبی: (جان.) بیدست آش بچگان. 
سگک 1 ( کد.) حربص» سک طماع» اهل 
دنیا. سک آموخته: سک تعلیم يافتهء کلب 
صید» کلب معلم. سگ ابلق: (کد.) دنیا به 
اعتبار شب و روز. سک تازی: (جاد.) یکی 
از گونه‌های سکك شکاری است که دراز 
اندام و چابک است با شکم فرو رفته و سین 
بر آمده و پوزه‌اش تبز است (شرایط تاخت و
```


## [2026-09-06T15:41:42.368Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^کمند\" MON_part1.txt MON_part2.txt | head; echo \"=== search kamand headword ===\"; grep -n \"کمند:\" MON_part1.txt MON_part2.txt | head"
}
```


### [2026-09-06T15:41:42.444Z] TOOL RESULT

```
MON_part1.txt:36124:کمند و زلف می‌باشد» پیچ و شکن. خلل» 
MON_part1.txt:71400:کمند خود در آوردن. 
MON_part1.txt:85076:کمند و غیره). 
MON_part2.txt:26380:کمند وحدت. کمر هفت‌چشمه: کمرنندی 
MON_part2.txt:26516:کمند: ۵204 (.) رسمانی محکم که 
MON_part2.txt:26526:کمند افتادن: گر فتار کمند شدن. در بند 
MON_part2.txt:26528:کمند کردن. به اطاعت در آوردن» وادار به 
=== search kamand headword ===
MON_part2.txt:26516:کمند: ۵204 (.) رسمانی محکم که 
MON_part2.txt:26519:جانوران را بدان مقید کنند. خم کمند: ( کد.) 
MON_part2.txt:26521:می‌زند. زلف کمند: (اض.تشبیهی) زلف 
MON_part2.txt:26529:تسلیم کردن. حلقه کردن کمند: کمند رابه 
MON_part1.txt:83053:شا کمند: 4«مساةه () نمدی که از پشم
```


## [2026-09-06T15:41:54.497Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '26510,26535p' MON_part2.txt"
}
```


### [2026-09-06T15:41:54.547Z] TOOL RESULT

```
باشد و برای قلم‌گیری‌های یک نواخت 
وکشیدن خطوط بلند بکار رود؛ قلم نیز‌یی 
کم‌محلی: آ-اامطن-۲ آف. ع. اه 
دارای اعستار و اهمیت اندک سودن. 
کم توجهی» کم لطفی. 

کمند: ۵204 (.) رسمانی محکم که 
هنگام جنگ آن را بر کگُردن و کمر دشمن 
اندازند و وی را به بند در آورند و یا 
جانوران را بدان مقید کنند. خم کمند: ( کد.) 
خم زلف و گیسو که دور رخسار حلقه 
می‌زند. زلف کمند: (اض.تشبیهی) زلف 
مجعد همچون کمند. کمند وحدت: آلتی که 
از ریسمان» ابریشم يا تسمةٌ چرمین سازند و 
فقرا در گلو اندازند و با در کمر بندند و گاه 
در کمر و هر دو زانو انداخته بنشینند. به 
کمند افتادن: گر فتار کمند شدن. در بند 
افتادن گر فتار گشتن. به کمند کشیدن: گرفتار 
کمند کردن. به اطاعت در آوردن» وادار به 
تسلیم کردن. حلقه کردن کمند: کمند رابه 
پیچ و تاب در آوردن. فتاه یات با تحار 
از 

کم‌نظیر: ۱-221۳ [غ. ف. (ص‌مر.) کم 
مانند» کم مثل. بی‌مانند» بی‌مثل. 
کم‌وبیش: ۲۰-0-15 [- کماییش] (ق‌مر.)
```


## [2026-09-06T15:42:05.506Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== HRN/HUB kamand ==\"; grep -n -i \"kamand\" HRN.txt HUB.txt RCH.txt LKT.txt TTS* 2>/dev/null | head -20; echo \"== ARY ==\"; grep -n \"کمند\" incoming/ARY/ARY_pages.txt | head -10; echo \"== ARY sagak ==\"; grep -n \"سگک\" incoming/ARY/ARY_pages.txt | head -10; echo \"== ARY latin idx ==\"; grep -n -iE \"KAMAND|SAGAK\" incoming/ARY/ARY_latin_index_pages.txt | head -10"
}
```


### [2026-09-06T15:42:05.598Z] TOOL RESULT

```
== HRN/HUB kamand ==
(eval):1: no matches found: TTS*
== ARY ==
== ARY sagak ==
== ARY latin idx ==
```


## [2026-09-06T15:42:07.418Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== BQT sagak ==\"; grep -n \"سگک\" BQT_v1_pages.txt BQT_v2_pages.txt incoming/BQT/BQT_v3_pages.txt incoming/BQT/BQT_v4_pages.txt 2>/dev/null | head -10; echo \"== BQT kamand headword ==\"; grep -n \"کمند =\\|کمند ‪=\\|(کمند)\" incoming/BQT/BQT_v4_pages.txt incoming/BQT/BQT_v3_pages.txt 2>/dev/null | head -10"
}
```


### [2026-09-06T15:42:07.501Z] TOOL RESULT

```
== BQT sagak ==
== BQT kamand headword ==
```


## [2026-09-06T15:42:11.059Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls -la incoming/ARY/ incoming/BQT/ 2>&1 | head -30; echo \"=== ARY head ===\"; head -c 600 incoming/ARY/ARY_pages.txt; echo; echo \"=== v3 head ===\"; head -c 400 incoming/BQT/BQT_v3_pages.txt"
}
```


### [2026-09-06T15:42:11.127Z] TOOL RESULT

```
incoming/ARY/:
total 9468
drwxrwxr-x  3 sfmqrb sfmqrb    4096 Sep  4 14:06 .
drwxrwxr-x 23 sfmqrb sfmqrb    4096 Sep  4 14:06 ..
-rw-rw-r--  1 sfmqrb sfmqrb 8102112 Sep  4 14:06 ARY_aryanpur_kashani_rishehaye_hend_o_orupayi.pdf
-rw-rw-r--  1 sfmqrb sfmqrb  586473 Sep  4 14:06 ARY_latin_index_pages.txt
-rw-rw-r--  1 sfmqrb sfmqrb  960497 Sep  4 14:06 ARY_pages.txt
drwxrwxr-x  2 sfmqrb sfmqrb   20480 Sep  4 13:30 ARY_pages.txt.pages

incoming/BQT/:
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
=== ARY head ===
[pdf page 1]
6 و۵
هندواروبابی_ 1010 1۵ 1000]
۵9 (۸9ا

۲1۹۸۸۱
۱۸۸۵۱۱ ۸۵ ٩۵۱۱
۸:۱۸
۲۸۵۳۵۸۵
[pdf page 2]
نج ۰
۰ پیشگفتار ۳
پیش گفتار
هدف این کتاب نشان دادن ریشه‌ی هند و اروپایی واژه‌های فارسی ناب است. این هدف موجب
۳۳۱ سس
ویژگی‌های زیر شده است:
۱- هیچ واژه‌ی فارسی که ریشه‌ی هند و اروپایی آن ناشناخته است آورده نشده است. صدها
واژه‌ی فارسی وجود دارد که ریشه�
=== v3 head ===
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


## [2026-09-06T15:42:17.536Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in incoming/BQT/BQT_v3_pages.txt incoming/BQT/BQT_v4_pages.txt incoming/ARY/ARY_pages.txt; do echo \"== $f ==\"; grep -c \"کمند\" $f; grep -n \"کمند\" $f | head -5; echo \"-- sagak --\"; grep -n \"سگک\\|سگگ\\|سكك\" $f | head -5; done"
}
```


### [2026-09-06T15:42:19.448Z] TOOL RESULT

```
== incoming/BQT/BQT_v3_pages.txt ==
15
959:شا کمند۲۱-بايم بروزن پای‌بند. بمعنی
1000:و موی بز سیاه در هم آمیزند وبمالند شا کمند
4146:و ‎tile‏ رسن وکمند و امثال آنرا گوبند .
6261:شهفك = بر وزن کمند » بمعنی بهوش
7790:کمند باشد ‎oly‏ رسمالی‌است ‎wath‏
-- sagak --
18654:«خاقانی شروانی ۲۲۳-۲۲۲ (دروصف‌مناسككحج)».
28223:‎op!‏ لفت راساحب موبدالفضلا در سككلغات‌فارسی
== incoming/BQT/BQT_v4_pages.txt ==
5
6210:۴ - ز قتراك بگشاد خمکمند در آورد ناکه میاش بیئد .
9419:زهی از عثبر سارا تفوله کمند است این که داری پا نفوله ؟
12395:کور اگر چند بود لیرومند با پدستش گرفت با بکمند .
18236:درفقی همی برد پیکر کراز سپاهش کمندافکن ورزم سازء
18682:کمند عدو هنج از بغر کین فروهشته چون اژدهایی ز زین.
-- sagak --
== incoming/ARY/ARY_pages.txt ==
0
-- sagak --
```


## [2026-09-06T15:42:24.008Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '7780,7800p' incoming/BQT/BQT_v3_pages.txt; echo \"=== ARY کمن ===\"; grep -n \"کمن\" incoming/ARY/ARY_pages.txt | head -10; echo \"=== ARY سگ ===\"; grep -n \"سگ\" incoming/ARY/ARY_pages.txt | head -10"
}
```


### [2026-09-06T15:42:24.082Z] TOOL RESULT

```
‏تا شوشه شود ۰

. ‏مجهول بر وزن غول‎ Bt ‏ه با‎ SH
‏بمعثی دید و داست باشد که ازدیدن وداستن‎
‏و امر باین معنی هم‌هست یعنی ببین‎ - ٩ ‏است‎
‏و بدان 6 - و دام طایفه‌ای هم هنت مثل کرد‎
‏وار ۷ - و امر بشولیدن هم هست که از پربشان‎
‏ومتفرق ساز.‎ Sole pyr ‏کردن باشد‎

شو ‎OF‏ بنتح‌اول بروزن جولانبمعنی
کمند باشد ‎oly‏ رسمالی‌است ‎wath‏

شو لک" - باالیمجهول بروزن کرچك؛
اسب جلد و ‎as‏ ونیز رفتار را کوبند ۷ - و نام
مر کپ امفندیار هم بوده است - وبمعنی‌بادرسة
‎ju dy‏ هست و آن چرم با چوپ ‎oS‏ است
که در کلوی ‎a dys‏ سازید ۸

شو لمی * » بنم اول و ثانی_ مجهول

۴ مز » 5062 , 50۲۵ ,
=== ARY کمن ===
187:اسلامبولی و ترکی ترکمنی و آذری و غیره).
820:نگاشته شده‌اند. این دو زبان که متون و آثار تاریخی وابسته به آنها حدود صد سال پیش در ترکمنستان
=== ARY سگ ===
574:۱ طریق پیگیری پسگرایانه‌ی شکل واژه‌ها) تعبین کرده‌اند. نمونه‌ی زیر مسیر اینگونه بازسازی‌ها را در
580:نداشته تعیین دقیق آوا و معنی واژه‌های هند و اروپایی بنیادین فقط از روی پیگیری پسگرایانه و
938:همریشه‌ی مربوط به «اسب» و «گاوه و «گوسفندء و دسگ» و «خوکک؛). همریشگی واژه‌های متعدد
1199:خود را ذ کر می‌کند»کتاب او عملاً خواننده را از پسگشت به مأَذ او (که برخی امروزه نایاب هستند)
1371:دارد ولی هیچکدام از پسگشت‌های در دسترس من اشاره‌ای همریشه‌های ایرانی و سانسکریت این
1404:کردی (80/57): ۷ ,2 پسگشت‌ها ای دراد ۲
1412:پهلوی (۲هاتلهه): 17 باانتا۸7 پسگشت‌ها دای اد ادن ای
1430:پهلوی (۷هاتل۸ط): ۸1 پسگشت‌ها لامش اد ادن
1453:روسی ((5514(ا): دندید ۱۲۱۱۱ پسگشت‌ها اه دا دناد
1475:پرناتی 0888/0): .۲ 8۸ | پسگشت‌ها آشرد دا
```


## [2026-09-06T15:42:31.987Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"کمند\" incoming/BQT/BQT_v3_pages.txt; echo \"=== v4 hits ===\"; grep -n \"کمند\" incoming/BQT/BQT_v4_pages.txt"
}
```


### [2026-09-06T15:42:32.043Z] TOOL RESULT

```
959:شا کمند۲۱-بايم بروزن پای‌بند. بمعنی
1000:و موی بز سیاه در هم آمیزند وبمالند شا کمند
4146:و ‎tile‏ رسن وکمند و امثال آنرا گوبند .
6261:شهفك = بر وزن کمند » بمعنی بهوش
7790:کمند باشد ‎oly‏ رسمالی‌است ‎wath‏
14995:‏سه حاکمند ‎(USCS)‏ اینجا چون غلبه همه دزد
16772:‎٩‏ - زفتراك ‎LES‏ خمکمند
22441:کمند قادر اندازان تدارد ‎Bh Sage‏ شود کرجمع صدکا کل پربشانم نمی‌سازد.
27089:‏قاری ‎٩‏ . آمد و رستم او را ‎pe‏ کمندکرفت ‏ و کشت هب
36056:۵ کمند - بفتح اول و دوم + پهلوی ‎kamand‏
36061:آژدها کردار پیجان در کف رادش کمند
36063:فرخی ‎YE‏ «ترجمان‌البلاعه . بخش عکی‌ص۲۵ب». پایین: کمند؛ بالا:اسبی کا در کمندافتاده
37222:‎Sask ‏کمند. . افزاری‎ oi ge AT
44784:‎AP‏ بروزن کمند » بمعن یآسیب
51018:مه بکمندآورد ‎be‏ تو هر نقس
=== v4 hits ===
6210:۴ - ز قتراك بگشاد خمکمند در آورد ناکه میاش بیئد .
9419:زهی از عثبر سارا تفوله کمند است این که داری پا نفوله ؟
12395:کور اگر چند بود لیرومند با پدستش گرفت با بکمند .
18236:درفقی همی برد پیکر کراز سپاهش کمندافکن ورزم سازء
18682:کمند عدو هنج از بغر کین فروهشته چون اژدهایی ز زین.
```


## [2026-09-06T15:42:35.699Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '36040,36070p' incoming/BQT/BQT_v3_pages.txt; echo \"=== page tag ===\"; awk 'NR<=36056 && /\\[pdf page /{p=$0} END{print p}' incoming/BQT/BQT_v3_pages.txt"
}
```


### [2026-09-06T15:42:37.292Z] TOOL RESULT

```
چشم تو بر دلم ‎le‏ کمی .
خروی ‎cab?‏ فری ۵۲۳ ‎٩‏ .

۴ - کمیت‌بن زید بن خئیس اسدی شاعر هاشمیان از مردم کوفه ( تولد ‎٩۶‏ - وفات

۴ - (عر) «کمیت کزبیر » اسب ‎So‏

۰۹ ۰. ) رك : اعلام زر کلی ج ۳ ص ۸۱ .
سرخ فش و دم سیاه... ومی‌سرخ سیاهیآمیز .» «منتهی‌آلارب » رلك: تعلیقات لوروزنامه‌س+۱۳.
6 کمانچه . ۲ — ‎pve‏ «کمیخت » ‎col‏ پپلوی 800012120 (مخلوط
کردن ) « دهارله ۳۱۰ » رك :کمیز ؛ کمخت . ۲ - محیح «کیز» ‎Cpa)‏ است اما
حکیم مژمن در تحفه در ضل « الکاف مع‌النون > ورده گوید : « کمیز اسم فارسی بولست *.
۸ -(عر ) «کمین کامیر » قوم پنهان نشیننده بقصد دشمن در جنگه و دخل در آمور
بئوع ی که مفپوم نگردد .» < منتهی‌الارب *. .۰ ‎٩‏ - در فارسی از :کم ین (پسودیبت)؛
کمترین ‏ کوچك :
یگذار که ‎pee‏ تا در صف ‎eat OS ay‏
۵ کمند - بفتح اول و دوم + پهلوی ‎kamand‏
‎Wyss!‏ ۲4۸۷ ۰ کردی ‎komen‏ ( طتاب بااکره متحرك )
‎bly?‏ ی ۰۳:۲ ؛ دام وائابی که در ‎Ke‏ بر گردندشمن
با د. شکار بر گردن حیوان می‌انداختند و او را بجاب خود
‎eS ye‏ :
آژدها کردار پیجان در کف رادش کمند
چون عصای‌موسی‌اندر کف موسی کشته‌مار.
فرخی ‎YE‏ «ترجمان‌البلاعه . بخش عکی‌ص۲۵ب». پایین: کمند؛ بالا:اسبی کا در کمندافتاده

> گلتان س ۳۹ ۰

[pdf page 491]
-۱۹۸- oS
. ۴ ‏کمتر | وکمترین وفرومایه باشد‎ cae ‏گهینه ۱ ه بروزن سفینه,‎

=== page tag ===
[pdf page 490]
```


## [2026-09-06T15:42:50.819Z] TOOL CALL #30: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-06T15:42:50.825Z] TOOL RESULT

```


```


## [2026-09-06T15:42:54.617Z] TOOL CALL #31: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%A9%D9%85%D9%86%D8%AF",
 "prompt": "Give the Persian entry for کمند (kamand): etymology, meaning, any Middle Persian / Proto-Iranian forms cited, and which sources (Hasandust, Cheung, etc.) are cited."
}
```


## [2026-09-06T15:42:55.781Z] TOOL CALL #32: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CE%BA%CE%B7%CE%BC%CF%8C%CF%82",
 "prompt": "Give the Ancient Greek entry for κημός: meaning, etymology, Doric form, and any note on Latin camus being borrowed from it."
}
```


### [2026-09-06T15:42:59.671Z] TOOL RESULT

```
# Persian Entry: کمند (kamand)

**Etymology:** Derived from Middle Persian 𐭪𐭬𐭭𐭣 (kmnd /kamand/).

**Meaning:** A lasso or noose.

**Historical Citation:** The word appears in Jalāl ad-Dīn Mohammad Rūmī's Masnavi-ye-Ma'navi (c. 1260s), where "دام مکر او کمند شیر بود" demonstrates its use meaning a snare or noose.

**Note:** No Middle Persian or Proto-Iranian scholarly sources (such as those by Hasandust or Cheung) are cited in this Wiktionary entry. The entry only references the Middle Persian form itself without citing academic etymological sources.
```


### [2026-09-06T15:43:02.846Z] TOOL RESULT

```
# κημός (kēmós)

**Meaning:** This Ancient Greek noun refers to several related items: a muzzle for led horses, a nosebag for horses, cloth used by bakers to cover the nose and mouth, a wicker vessel (weely), the funnel-shaped top of a voting urn, or a female ornament.

**Etymology:** The origin remains "unexplained." Proposed connections to Old Armenian, Lithuanian, Russian, and Middle High German terms exist but are problematic. Furnée instead suggests derivation "from a Pre-Greek source common to χάβος and χαμόν."

**Doric Form:** The alternative Doric form is κᾱμός (kāmós).

**Latin Borrowing:** The entry notes that Latin cāmus descends from this Greek term, indicating it was borrowed into Latin.

**Grammar:** It's a masculine noun of the second declension with the genitive κημοῦ.
```


## [2026-09-06T15:43:07.234Z] TOOL CALL #33: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/hame",
 "prompt": "Give the full etymology of English \"hame\" (part of a horse collar), including Middle Dutch/Dutch haam and any PIE root."
}
```


## [2026-09-06T15:43:07.959Z] TOOL CALL #34: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/hame",
 "prompt": "Give the English noun \"hame\" (part of a harness): etymology, Middle Dutch/Dutch haam, Proto-Germanic and PIE root cited."
}
```


### [2026-09-06T15:43:11.509Z] TOOL RESULT

```
I appreciate your question, but I must be direct: the web page content you've provided is only the header, navigation, and footer of Etymonline.com. It contains no actual etymological entries or definitions—including no information about "hame" or its origins through Middle Dutch/Dutch "haam" or any Proto-Indo-European roots.

To obtain the etymology you're seeking, you would need to visit etymonline.com directly and search for "hame" to see the full entry with its linguistic history and source materials.
```


### [2026-09-06T15:43:14.289Z] TOOL RESULT

```
# English "Hame" Etymology

**Etymology 2** traces this harness component through the following path:

From "Middle Dutch _[hame](#Middle_Dutch)_ ('horse collar, harness, fishnet')" to "Proto-Germanic _[\*hamô](/wiki/Reconstruction:Proto-Germanic/ham%C3%B4)_ ('fishnet, collar for a horse')" and ultimately to "Proto-Indo-European _[\*ḱom-](/w/index.php?title=Reconstruction:Proto-Indo-European/%E1%B8%B1em-&action=edit&redlink=1)_ ('part of a harness')."

The word reached English through Middle Dutch borrowing, becoming the term for "metal or wooden pieces of a horse collar to which the traces...are attached."
```


## [2026-09-06T15:43:25.865Z] TOOL CALL #35: WebSearch

```json
{
 "query": "Sanskrit śakula शकुल meaning Monier-Williams"
}
```


## [2026-09-06T15:43:27.104Z] TOOL CALL #36: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B3%DA%AF%DA%A9",
 "prompt": "Is there a Persian entry for سگک (sagak)? Give meaning and etymology if present."
}
```


### [2026-09-06T15:43:31.328Z] TOOL RESULT

```
# Persian Entry for سگک (sagak)

Yes, there is a Persian entry for this word. According to the Wiktionary page:

**Meaning:** The term سگک (sagak) is a noun meaning "buckle" (the fastening device).

**Etymology:** The page does not provide etymological information about the word's origins or derivation.

The entry notes the plural form is سگک‌ها (sagak-ha), and includes an image of a palladium-plated belt buckle as a visual reference.
```


### [2026-09-06T15:43:31.983Z] TOOL RESULT

```
Web search results for query: "Sanskrit śakula शकुल meaning Monier-Williams"

Links: [{"title":"Shakuli, Śakuli, Śakulī: 3 definitions","url":"https://www.wisdomlib.org/definition/shakuli"},{"title":"Monier-Williams Sanskrit-English Dictionary --स","url":"https://sanskrit.inria.fr/MW/295.html"},{"title":"Shakula, Śakula, Sakula, Sakulā, Sākulā, Śākula, Sākula: 16 definitions","url":"https://www.wisdomlib.org/definition/shakula"},{"title":"Monier-Williams Sanskrit-English Dictionary, 1899","url":"https://www.sanskrit-lexicon.uni-koeln.de/scans/MWScan/2014/web/index.php"},{"title":"Monier-Williams: A Sanskrit-English Dictionary","url":"https://gretil.sub.uni-goettingen.de/gretil/6_sres/2_dict/mwse_u.htm"},{"title":"Monier Williams Sanskrit-English Dictionary (online)","url":"https://www.sanskrit-lexicon.uni-koeln.de/scans/MWScan/2020/web/webtc/indexcaller.php"},{"title":"Monier-Williams Sanskrit Dictionary 1899 Advanced","url":"https://www.sanskrit-lexicon.uni-koeln.de/scans/MWScan/2020/web/webtc2/index.php"},{"title":"A Sanskrit English Dictionary : Monier-williams, Monier, Sir : Free Download, Borrow, and Streaming : Internet Archive","url":"https://archive.org/details/in.ernet.dli.2015.31959"},{"title":"Monier-Williams Sanskrit English Dictionary Page 0498","url":"http://www.ibiblio.org/sripedia/ebooks/mw/0400/mw__0498.html"},{"title":"Monier-Williams Sanskrit Dictionary 1899 List","url":"https://www.sanskrit-lexicon.uni-koeln.de/scans/MWScan/2020/web/webtc1/index.php"}]

Based on the search results, Śakula (शकुल) refers to a kind of fish, perhaps 'the gilt-head'. More specifically, in Dharmashastra terminology, Śakula refers to the fish-species Heteropneustes fossilis. 

Additionally, it can also mean a kind of spur-like projection behind the hoof of an ox or cow.

These definitions come from the Monier-Williams Sanskrit-English Dictionary and related Sanskrit lexical sources, which contain references to the Vājasaneyi-saṃhitā, Atharva-veda, and Mahābhārata among other classical texts.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-06T15:43:37.770Z] TOOL CALL #37: WebFetch

```json
{
 "url": "https://www.wisdomlib.org/definition/shakula",
 "prompt": "Quote the Monier-Williams definitions of Śakula (शकुल), especially any sense about a spur-like projection behind the hoof of an ox or cow, and the text references."
}
```


## [2026-09-06T15:43:39.067Z] TOOL CALL #38: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%B3%DA%AF%DA%A9/",
 "prompt": "Give the Dehkhoda and Mo'in (فرهنگ معین) entries for سگک: definitions and any etymology/origin tag."
}
```


### [2026-09-06T15:43:42.944Z] TOOL RESULT

```
# Śakula: Spur-like Projection Definition

According to the Monier-Williams Sanskrit-English Dictionary, **Śakula** has the following sense:

> "a kind of spur-like projection (behind the hoof of an ox or cow)"

**Text references cited:**
- Vājasaneyi-saṃhitā
- Additional occurrences in comparative texts

The dictionary entry notes this definition alongside the primary meaning of the term as a type of fish, indicating the word had dual applications in Sanskrit literature—referring both to an aquatic creature and to a particular anatomical feature found on bovine hooves.
```


### [2026-09-06T15:43:45.807Z] TOOL RESULT

```
# Dehkhoda and Mo'in Entries for سگک

**Dehkhoda Dictionary:**
"مصغر سگ یا گیاهی باشد که بار و میوه آن گرهی است کوچک و پرخار که در جامه آویزد"
(a diminutive of dog, or a plant whose fruit is a small, thorny knot that clings to clothing)

Also includes: "نوعی از قلاب" (a type of clasp/hook)

**Mo'in Dictionary:**
"نوعی قلاب چهار - گوش یا نیم دایره یا گرد برای بستن کفش ، کیف ، کمربند و..."
(a four-sided, semicircular, or round clasp used for fastening shoes, bags, belts, etc.)

**Etymology:** Both entries mark the term as "(اِمصغ)" — a diminutive form, suggesting its origin as a small version of سگ (dog).
```


## [2026-09-06T15:44:08.898Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== POK kamanos/kemos ==\"; grep -n -i -E \"kamanos|kamanas|kemos|camus|hemja\" POK_full.txt | head -20; echo \"== AHD watkins ==\"; grep -n -i -E \"\\bkam-|hame|camus|kemos|śakula|sakula\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-06T15:44:08.965Z] TOOL RESULT

```
== POK kamanos/kemos ==
45184:Old Norse hemja {hamda) "curb, restrain, hinder, hamper', hemiir leg fetter', ham/at " 
45202:kamuoti^ press together, stuff, kamanos^ leathery bridle, rein', kemuras ^ grape' , 
45218:festival to honor of the Dionysios '; gr. Kr||j6(; ( */ra/770S because of Latin loanword camus) 
49846:Latin caleo, -ere 'warm, be hot, glow', caMus 'warm, hot', ca/or' warmth, heat'; 
== AHD watkins ==
382:blind: TYPHUS; TYPHLOSOLE. 11. Extended form *dheubh., “beclouded in the senses,” in suffixed o-grade form *dhoubh-o- in: a. Germanic *daubaz in Old English déaf, deaf: DEAF; b. nasalized form *dhu-m-bho- in Germanic *dumbaz in Old English dumb, dumb: pumps; c. Germanic *diibén- in Old English *dife, dove (< “dark-colored bird”): DOVE!. 12. Extended zero-grade form *dhwel- in: a. Germanic *dwelan, to go or lead astray, in Old English dwellan, to deceive (but influenced in sense by cognate Old Norse dvelja, to tarry): DWELL; b. Germanic *dulaz in (i) Old English dol, dull: DoL- DRUMS (ii) Middle Low German dul, dull: (DOLT), DULL. 13. Extended zero-grade form *dhwes- in Greek suffixed form *th(wjes-es-, smoke, whence Greek *th(w)es-es-yon, becoming theion, brimstone, sulfur: THIO-, THION-. 14. Perhaps Old English docce, dock (< “dark-colored plant”): Dock‘. 15. Perhaps Irish did, pipe: DUDEEN. [Pok. 4. dheu- 261.] dheu-2. To flow. Germanic *dauwaz, dew, in: a. Old English déaw, dew: DEW; b. compound *melith-dauwaz, “honeydew” (see melit-). [Pok. 1. dheu- 259.] dheu-’. To become exhausted, die. 1. Suffixed o-grade form *dhou-to- in Germanic *daudaz in Old English déad, dead: DEAD. 2. Suffixed o-grade form *dhou-tu- in Germanic *dauthuz in Old English déath, death: DEATH. 3. Suffixed o-grade form *dhow-yo- in Old Norse deyja, to die: DIE}. 4. Suffixed extended zero-grade form *dhwi-no- in Germanic *dwinan in Old English dwinan, to diminish, languish: DWINDLE. [Pok. 2. dheu- 260.] dheub-. Deep, hollow. 1. Germanic *deupaz in Old Eng- lish déop, deep: DEEP, DEPTH. 2. Germanic expressive denominative *duppjan in Old English dyppan, to im- merse, dip: pip. 3. Parallel root form *dheubh- in Ger- manic *deub-, *dub- in verb *diibjan in Old English dyfan, to dip, and difan, to sink, dive: pivE. [Pok. dheu-b- 267.] dheubh-. Wedge, peg, plug. Germanic *dub- in: a. Old English dubbian, to tap, strike (with a sword): DUB); b. Low German dubben, to hit: puB?; c. Germanic di- minutive *dub-ila- in Middle Low German dével, peg: DOWEL. [Pok. dheubh- 268.] dheugh-. To produce something of utility. 1. Germanic extended form *duht- in Old English dyhtig, dohtig, strong (< “useful”): DOUGHTY. 2. Suffixed form *dheugh- os- in Greek teukhos (< *theukhos), gear, anything produced, tool: HEPTATEUCH, HEXATEUCH, PENTA- TEUCH. [Pok. dheugh- 271.] dhghem-. Earth. 1. Suffixed zero-grade form *(dh)ghm-on-, “earthling,” in Germanic *gumén- in Old English guma, man: BRIDEGROOM. 2. O-grade form *dhghom- in Greek khthon, earth: CHTHONIC; AUTOCH- THON. 3. Zero-grade form *dhghm- in Greek khamai, on the ground: CHAMAEPHYTE, CHAMELEON, CHAMOMILE, GERMANDER. 4. Suffixed o-grade form *(dh)ghom-o- in Latin humus, earth: HUMBLE, (HUMILIATE), (HUMILITY), HUMUS; EXHUME, INHUME, TRANSHUMANCE. 5. Suffixed o-grade form *(dh)ghom-on-, “earthling,” in: a. Latin homé, human being, man: HOMAGE, HOMBRE!, HOMINID, HOMO!, HOMUNCULUS, OMBRE; BONHOMIE, HOMICIDE; b. (in part) Latin himdnus, human, kind, humane: HUMAN, (HUMANE). 6. Suffixed form *(dh)ghem-ya in Russian zemlya, land, earth: SIEROZEM, ZEMSTVO. 7. Full-grade form *(dh)ghem- in Persian zamin, earth, land: ZAMINDAR. [Pok. ghdhem- 414.] dhghut-. Fish. Greek ikhthus, fish: 1cHTHYO-. [Pok. ghdha- 416,] dhgh(y)es-. Yesterday. Suffixed (comparative) form (dh)ghes-ter- in Germanic “ges-ter- in Old English geo- stran, giestran, “yester-”: YESTER-, (YESTERDAY). [Pok. ghdhies 416.] dhgvhei-. To perish, die away. Zero-grade form *dhgvhi- in Greek phthinein, to die away: PHTHISIS. [Pok. gthdhei(a)- 487.)
578:kamer-. To bend; a vault. 1. Greek kamara, a vault: (CABARET), CAMARILLA, (CAMERA), CHAMBER, (COM- RADE); (BICAMERAL). 2. Persian kamar, waist, girdle, oat something arched: CUMMERBUND. [Pok. kam-er- 524.
581:BIT), GAMBOL, (GAMBREL), (GAMMON3), (JAMB). 2. Suf- fixed form *kamp-ulo- in Greek kampulos, bent: CAMPYLOTROPOUS. [Pok. kam-p- 525.] kan-. To sing. 1. Germanic *han(e)ni in Old English hen(n), hen: HEN. 2. Latin canere, to sing (> cantdre, to sing): CANOROUS, CANT?, CANTABILE, CANTICLE, CANTIL- LATE, (CANTO), CANTOR, CANZONE, CHANT; ACCENT, DESCANT, ENCHANT, (INCANTATION), INCENTIVE, PRE- CENTOR, RECANT. 3. Latin oscen, a singing bird used in divination (< *obs-cen, “one that sings before the au- gurs”; ob-, before; see epi): OSCINE. 4. Suffixed form *kan-men- in Latin carmen, song, poem: CHARM}. [Pok. kan- 525.] kand-. To shine. 1. Suffixed (stative) form *kand-é- in Latin candére, to shine: CANDENT, CANDID, (CANDIDA), (CANDIDATE), CANDLE, CANDOR; INCANDESCE. 2. Latin transitive *candere, to kindle, in compound incendere, to set fire to, kindle (in-, in; see en): (INCENDIARY), IN- CENSE. [Pok. kand- 526.] kannabis. Hemp. Late Indo-European word borrowed from an unknown source. 1. Germanic *hanipiz in Old English henep, henep, hemp: HEMP. 2. Greek kannabis, hemp: CANNABIS, (CANVAS). kanto-. A corner, a bending. Celtic *cantos, rim, border, in Latin cantus, canthus, iron ring around a carriage wheel, a wheel, rim (> Italian canto, corner): CANTEEN, CANTON; DECANT. [Pok. kan-tho- 526.] kap-. To grasp. I. Basic form *kap-. 1. Germanic *haf- in Old English hefeld, thread used for weaving, heddle (a device which grasps the thread): HEDDLE. 2. Germanic *haftjam in Old English heft, handle: Harr. 3. Form *kap-o- in Germanic *habai-, *habén in Old English habban, to have, hold: HAVE. 4. Germanic hafigaz, “containing something,” having weight, in Old English hefig, heavy: HEAVY. 5. Germanic *hafnd-, perhaps “place that holds ships,” in Old English hefen, a haven: HAVEN. 6. Germanic habukaz in Old English h(e)afoc, hawk: HAWK}, 7, Latin combining form -ceps (< *kap-s), “taker.” II. Suffixed form *kap-yo-. 1. Germanic *hafjan in Old English hebban, to lift: HEAVE. 2. Latin capere, to take, seize, catch: CABLE, CAPABLE, CAPACIOUS, CAPIAS, CAPSTAN, CAPTION, CAPTIOUS, CAPTIVATE, CAPTIVE, CAP- TOR, CAPTURE, CATCH, (CHASE!); ACCEPT, ANTICIPATE, CONCEIVE, DECEIVE, EXCEPT, INCEPTION, (INCIPIENT), INTERCEPT, INTUSSUSCEPTION, MUNICIPAL, NUNCUPA- TIVE, OCCUPY, PARTICIPATE, PERCEIVE, PRECEPT, RE- CEIVE, (RECOVER), RECUPERATE, (RX), SUSCEPTIBLE. III. Suffixed form *kap-s- in Latin capsa, repository, case: CAISSON, CAPSICUM, CAPSID, CAPSULE, CASE2, CHASE?, CHASES, CHASSIS, CHESS?; ENCHASE. IV. Length- ened-grade variant form *kdép-. 1. Germanic *hof- in compound *bi-hdf, “that which binds,” requirement, obligation (*bi-, intensive prefix; see ambhi), in: a. Old English behdf, use, profit, need: BEHOOF; b. Old English behéfian, to have need of: BEHOOVE. 2. Greek k6pé, oar, handle: copePpop. Compare ghabh-. [Pok. kap- 527.] kap(h)o-. Hoof. Lengthened-grade form kdp(h)-o- in Germanic *héfaz in Old English Adf, hoof: Hoor. [Pok. kapho- 530.] kapro-. He-goat, buck. Latin caper, he-goat (> capra, she-goat): CABRILLA, CABRIOLET, CAPELLA, CAPRIOLE, CHEVRON; CAPRIC ACID, CAPRICORN, CAPRIFIG, CAPROIC ACID. [Pok. kapro- 529.] kaput. Head. 1. Germanic *haubidam, *haubudam, in Old English héafod, head: HEAD. 2. Latin caput, head (> Italian capo, head): CABEZON, CADET, CAPE?, CAPITAL, CAPITAL, CAPITATE, CAPITATION, CAPITELLUM, CAPITU- LATE, CAPITULUM, CAPO!, CAPRICE, CAPTAIN, CATTLE, CAUDILLO, CHAPITER, CHAPTER, CHIEF, CHIEFTAIN; BI- CEPS, CHAMFRON, DECAPITATE, KERCHIEF, MISCHIEF, OCCIPUT, PRECIPITATE, RECAPITULATE, SINCIPUT, TRI- ceps. [Pok. kap-ut- 529.] kar-', Hard. I. Variant form ker-. 1. Suffixed o-grade form *kor-tu- in Germanic *harduz in: a. Old English hard,
986:(s)peud-. To push, repulse. 1. Latin pudére, to feel shame: PUDENCY, PUDENDUM; IMPUDENT. 2. Latin repu- dium, a casting off, divorce (re-, off; see re-): REPUDIATE. [In Pok. péu- 827.]
1094:tkei-. To settle, dwell, be home. 1. Suffixed o-grade form *()koi-mo- in Germanic *haimaz, home, in: a. Old Eng- lish hdm, home: HOME; b. Old Norse heimr, home: NIFLHEIM; C. Middle Dutch hame, hame (< “covering”): HAME; d. Old French ham, village, home: HAMLET; e. Germanic *haimatjan, to go or bring home, in Old French hanter, to frequent, haunt: HAUNT. 2. Zero-grade form *tki- in Greek kti- in ktizein, to found, settle: AMPHYCTYONY. 3. Probable zero-grade form *tki- in Latin si- in suffixed form *si-tu- in situs, location: SITUATE, SITUS. [Pok. 1. hei- 589, Athei- 539.] to-. Demonstrative pronoun. For the nominative singular see so-. 1. Germanic *thé- in: a. Old English thé, thy (instrumental case), by the: THE!, THE?; NATHELESS; b. Middle Dutch de, the: pEcoy. 2. Germanic *thauh, “for all that,” in Old Norse thd, though, akin to the Scandinavian source of Middle English though, though: THOUGH. 3. Germanic *thasi- in Old English thes, this, this: (THESE), THIS. 4. Germanic *thana- in Old English thanne, thenne, thenne, than, then: THAN, THEN. 5. Ger- manic *thanana- in Old English thanon, thence: THENCE. 6. Germanic *thér in Old English ther, thér, there: THERE. 7. Germanic *thathro in Old English theder, thider, thither: THITHER. 8. Germanic nomina- tive plural *thai in Old English tha and Old Norse their, they: THEY. 9. Germanic genitive plural *thaira in Old Norse their(r)a, theirs: THEIR. 10. Germanic dative plural *thaimiz in Old Norse theim and Old English thém, them: THEM. 11. Extended neuter form *tod- in: a. Ger- manic *that in Old English thet, that: THAT, (THOSE); b. Greek to, the: TAUTO-. 12. Germanic *thus- in Old English thus, thus: THUS. 13. Adverbial (originally accu- sative) form *tam in Latin tandem, at last, so much (> Anglo-Norman tant): TANDEM, TANTAMOUNT. 14. Suf- fixed reduced form *t-dli- in Latin tdlis (plural tdlés), such: TALES. [Pok. 1. to- 1086.] tolky-. To speak. Metathesized form *tlokv- in Latin loqui, to speak: LOCUTION, LOQUACIOUS; ALLOCUTION, CIRCUMLOCUTION, COLLOQUIUM, (COLLOQUY), ELOCU- TION, GRANDILOQUENCE, INTERLOCUTION, MAGNIL- OQUENT, OBLOQUY, PROLOCUTOR, SOLILOQUY, VENTRILOQUISM. [Pok. tolk¥- 1088.] tong-. To think, feel. 1. Germanic *thank6n in: a. Old English thancian, to thank: THANK; b. Old English thencan, to think: THINK. 2. Germanic *(ga)thauht- (*ga-, collective prefix; see kom) in Old English (ge)- thoht, thought: THOUGHT. 3. Germanic factitive *thunk- Jan in Old English thyncan (third person singular present indicative thyncth), to seem: METHINKS. [Pok. 1. tong- 1088.] tragh-. To draw, drag, move. Rhyming variant dhragh-. Latin trahere, to pull, draw: TRACT!, TRACTABLE, TRAC- TION, TRAIL, TRAIN, (TRAIT), TREAT; ABSTRACT, AT- TRACT, CONTRACT, DETRACT, DISTRACT, EXTRACT, PORTRAY, PROTRACT, RETRACT, SUBTRACT. [Pok. tragh- 1089.] treb-. Dwelling. 1. Zero-grade form *trb- in Germanic *thurp- in Old English thorp, village, hamlet: THORP. 2. Latin trabs, beam, timber: TRABEATED, TRABECULA, TRAVE; ARCHITRAVE. [Pok. treb- 1090.] trei-. Three. I. Nominative plural form *treyes. 1. Ger- manic *thrijiz in Old English thrie, thréo, thri, three, with its derivatives thriga, thriwa, thrice, and thritig, thirty, and thréotine, thirteen: THREE, THRICE, THIRTY, THIRTEEN. 2. Latin trés (> Italian tre and French trois), three: TREY, TRIO; TRAMMEL, TRECENTO, TREPHINE, TRIUMVIR, TROCAR. II. Zero-grade form *tri-. 1. Suffixed form *tri-tyo- in: a. Germanic *thridjaz, third, in (i) Old English thrid(d)a, thirdda, third: THIRD (ii) Old Norse thrithi, third: RIDING?; b. Latin tertius (neuter tertium), third: TERCEL, TERCET, TERTIAN, TERTIARY, TIERCE; SESTERCE. 2. Latin évi-, three: TRI-, TRIPLE. 3. Greek t7i-, three: TRI-; TRICLINIUM, TRICROTIC, TRIDACTYL, TRI- GLYPH, TRITONE. 4. Sanskrit tri, three: TRIMURTI.
1342:CENTROBARIC gWere-2 CENTUM dekm CENTURY dekm CEPHALIC ghebh-el- CEPHALO- ghebh-el- -CEPHALOUS ghebh-el- CERAMIC ker-4 CERASTES ker-! CERATODUS dent-, ker-1 CERATOID ker-! CEREAL ker-3 CEREBELLUM ker-1 CEREBRUM ker-1 CERES ker-3 CERTAIN krei- CERVINE ker-1 CERVIX ker-1 CESSION ked- CESSPOOL spirare cEsTus! kent- CEsTUS? kae-id- CHAETA ghait- CHAETOGNATH genu-2, ghait- CHAFE dhé-1, kele-1 CHAFER gep(h)- CHAFF! gep(h)- CHAIR sed-1 CHALAZA gheled- CHALAZION gheled- CHALCID ghelegh- CHALCOCITE ghelegh- CHALCOPYRITE ghelegh- CHALCOsIS ghelegh- CHALICE kal-1 CHALLENGE kel-8 CHALONE ghé- CHAMAEPHYTE dhghem- CHAMBER kamer- CHAMELEON dhghem- CHAMFER bhreg- CHAMFRON kaput CHAMOMILE dhghem-, mélon CHANCE kad- CHANCEL carcer CHANCELLOR carcer CHANCRE kar-1 CHANGE skamb- CHANT kan-
1579:HAG2 kau-2 HAGGARD kagh- HAGGLE kau-2 HAGIO- yag- HAIL! kaghlo- HAIL? kailo- HAKE keg- HALBERD bhardha, kelp- HALE! kailo- HALE? kele-2 HALF skel-1 HALIBUT bhau- HALL kel-2 HALLOW kailo- HALO-  Sal-1 HALT! kel-3 HALT? kel-1 HALTER! kelp- HALTER? § sel-4 HAM konemo- HAMADRYAD deru, sem-! HAME_ tkei- HAMLET tkei- HAMMER ak- HANDIWORK kom HANDSEL sel-3 HANG konk- HANKER konk- HANUMAN genu-2 HAP kob- HAPLESS kob- HAPLOID pel-3, sem-1 HAPPEN kob- HAPPY kob- HARANGUE koro- HARBINGER koro- HARBOR koro- HARD kar-1 HARDS_ kes-! HARDY! = kar-1 HARE kas- HARM kormo- HARMONY ar- HARNESS _nes-1 HARPOON  serp-1 HARPSICHORD ghere- HARQUEBUS keg- HARRY koro- HART ker-1 HARTEBEEST ker-1 HARUSPEX ghere- HARVEST kerp- HASH! =skep- HASLET ghasto- HASTATE ghasto- HAT kadh- HATCHET skep- HATE kad- HATRED ar-, kad- HAUBERK kWel-1 HAUGH kel-2 HAUGHTY al-3 HAUL kele-2 HAULM kolem- HAUNT tkei- HAUSTELLUM aus-2 HAUSTORIUM aus-2 HAUTBOY al-3, busk- HAVE kap- HAVEN kap- HAW2 kagh- HAWK! kap- HAWKER keu-2 HAWSE kWel-1 HAWSER al-3 HAY kau-2 HAZEL koselo- HE! ko-
```


## [2026-09-06T15:44:09.701Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== SYN halter/bridle ==\"; grep -n -i -E \"camus|kemos|kamanos\" SYN.txt LEW_1910.txt LAT.txt | head -20"
}
```


### [2026-09-06T15:44:09.755Z] TOOL RESULT

```
== SYN halter/bridle ==
LAT.txt:2159:sed hortantis aduerbiun adeo ut plerumque "age facite" dicamus, et
LAT.txt:9087:camum, -I n.(camus m.): 7top.cc xo ex xpcGuiv; sorte de bifere. Mot
LAT.txt:9093:camus, -I m. : muselibre, Emprunt au gr.xccp.6c (ion. att. XT|p,oc) .- 163-
LAT.txt:12267:bles d’etre appel^s sous les armes: et partes populi classes uocamus
LAT.txt:12270:48,88, classes clipeatas antiqui dixerunt, quos nunc exercitus uocamus;
LAT.txt:13260:conferentia quam rustice uocamus confriuam, F.Muller, Mnea., 58,94,
LAT.txt:14223:uocamus cotonea et graece Cydoriea, e Creta insula aduecta j mais peut
LAT.txt:15435:de hominibus dicamus, et cibo et lauctcro intellegimus, uel alterutro-,
LAT.txt:16429:dicamus, diuos ex hominibus factos... sed Varro et Ateius contra sen¬
LAT.txt:16791:meliore; unde et usus est ut sine commemoratione noctis numerum dicamus
LAT.txt:29835:cf.Lucr. 1,439, scilicet hoc id erit uacuun quod inane nocamus), de
LAT.txt:36330:uocamus, quod eo aqua in trulleum effundatur. Unde manalis lapis
LAT.txt:40989:pariers latins "les reins", cf. Fest.348>3S> rienes^quos nunc uocamus,
LAT.txt:45015:panuclam uocamus... est tumor quoque inguinum; ex formae similitudine
LAT.txt:45054:mammae de qua exit lac, unde factum est ut dicamus infantibus papa,
LAT.txt:47166:uocamus', petulans, pcp. d’un verbe *petulS (cf. postulS, ustuit):
LAT.txt:48697:peluem uocamus, F.aDfi,^ (et P.F.387,14); polybrum, quod Graeci vep-
LAT.txt:48698:vt,(3a, nos trullium uocamus. Liuius (Od.5): "argenteo polybro, aureo
LAT.txt:49554:sum" dicamus. Sert de pcp. k bib 5 ; de meme adpStus (Pl., Amp.aSa).
LAT.txt:53214:rien est signale par Festus, 343,33: rienes quos nunc uocamus, antiqui
```


## [2026-09-06T15:44:24.504Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '45160,45230p' POK_full.txt"
}
```


### [2026-09-06T15:44:24.556Z] TOOL RESULT

```
Root/ lemma: kema-, koma-, kma-{* hank-mh(e)nos)\ piece, derived from Root/ lemma: 

aR-, oR-\ sharp; stone. 

Material: Gr. aKjjrivoc; " without Imbift, hungry', OKpa (Aeolic) vnarsia, £v5£ia Hes.; zero 

grade KO|ju)aa ysfjouaa Hes.? 

Latvian kumuoss^ t(\o\sq\, mouthful' (-^/77-reduced grade; the ending -i/oss from -ansas 
perhaps through hybridization with a *kan[d]s-as = Old Church Slavic kqsi) 'piece, morsel, 
mouthful'? compare MiJhlenbach-Endzelin Latvian-D. Wb. II 313); 

ndd. ham, hamm'b'\te, morsel, mouthful, piece, cut'. 

References: WP. I 389. 
Page(s): 557-558 

Root / lemma: kem-1 

Meaning: to press, squeeze 

Material: Armenian k'amerio press, squeeze, wring; to filter, make flow'; 

Old Norse hemja {hamda) "curb, restrain, hinder, hamper', hemiir leg fetter', ham/at " 
Ruderband ', Middle High German hemmen and hamen^\r\\n6er, hamper', sal- Franconian 
chamian^ clamp, press'. Old Frisian /7e/77/r75 "hinder'. Modern High German dial, ham, 
hamen " horse collar ' (compare that maybe from a Gothic *hamands hemmend " 
hindering ' borrowed Slavic *chomgt-b, russ. etc. chomuf-b " horse collar '); Middle Low 
German ham. Old English hamm^ enclosed piece of land', ndd. hamme^ fenced field'. Old 



English engl. herr{m) "edge, hem', engl. to hem {in) "to hem, gird, border, envelop, 
surround'; 

Old Norse hafna^ abandon, give up from ' ("*be restrained '), causative hefna^ avenge '; 
with labial Middle English hamperen, engl. to hamper '\r\\n6er, bother, annoy' (: Old 
Prussian kumpinna^ hindered ', kumpint^moye, displace'); (under the influence of 
common Celtic -ns-, -nt- > -nn-). 

Balto Slavic *kama-{r\. "clump' in Latvian kamsm. "clump', in addition Lithuanian 
kamuoti^ press together, stuff, kamanos^ leathery bridle, rein', kemuras ^ grape' , 
kam/enasm. "stem', Latvian Aa/77^c»/' torment, smite, plague', Lithuanian kamuolys, 
Latvian kamuolis^ ball, tangle, knot '; ablaut. Latvian c§mu(o)rsm. "grape', extended 
Lithuanian kemsu, kimsti^ stuff, Latvian kemsu, A7/77S/ (Lithuanian loanword) "ds.', also " 
devour', Lithuanian kamsa^ crush, squash, corduroy, brushwood road '; 

russ. kom "clump', komftb " clench together ', serb. kdm " husks of grapes ' (" what 
remains of the pressed grapes '); in addition russ. komelt m. 'thick end of a rod ', poln. 
komelm. "knag' {*kamlia-), russ. komuljai. "clump', serb. kominai. " husks of grapes '; in 
ablaut Slavic *k-bmy. Gen. *k-bmene'(r\. in Czech A/77e/7 "stem'; as " be pressed ' 
presumably also Slavic *cbma\v\ serb. cama^ boredom, weariness ', camati^ wait with 
displeasure, hold on'; Old Church Slavic di^s/b "dense' (= Lithuanian A//775/as "stuffed'). 

Doubtful is Perssons (Beitr. 159) apposition from gr. KdJMU(;, -u0O(; " bundle, truss of hay, 
branch of laurel, placed before the gates, reed-bed ', kojjjoc; " revel, carousal, merry- 
making, concrete, band of revelers, the ode sung at one of these festive processions, 
festival to honor of the Dionysios '; gr. Kr||j6(; ( */ra/770S because of Latin loanword camus) 
"muzzle' is not compatible in vocalism. 

References: WP. I 388 f., Trautmann 115, 126. 
Page(s): 555 

Root / lemma: kem-2 

Meaning: to buzz 

Material: Old Indie camara- m. " Wild Yak '; 

Middle High German Modern High German hummen. Modern High German hummein,
```


## [2026-09-06T15:44:48.343Z] TOOL CALL #42: Bash

```json
{
 "command": "ls site/pages/236.jpg 2>/dev/null; pdftoppm -f 236 -l 236 -r 200 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg236 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


## [2026-09-06T15:44:49.164Z] TOOL CALL #43: WebSearch

```json
{
 "query": "ریشه‌شناسی کمند حسن‌دوست فرهنگ ریشه‌شناختی فارسی میانه kamand etymology"
}
```


### [2026-09-06T15:44:51.186Z] TOOL RESULT

```
site/pages/236.jpg
total 6352
drwx------ 3 sfmqrb sfmqrb    4096 Sep  6 11:44 .
drwx------ 4 sfmqrb sfmqrb    4096 Sep  6 10:51 ..
-rw-rw-r-- 1 sfmqrb sfmqrb     792 Sep  6 11:43 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   92182 Sep  6 10:55 bqt1854.png
-rw-rw-r-- 1 sfmqrb sfmqrb   66580 Sep  6 10:57 bqt2023.png
-rw-rw-r-- 1 sfmqrb sfmqrb   69965 Sep  6 11:25 bqt2242crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb   28189 Sep  6 11:25 bqt2417crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb  431133 Sep  6 11:16 bqt2420_fn.png
-rw-rw-r-- 1 sfmqrb sfmqrb    9548 Sep  6 11:25 bqt2meta.json
-rw-rw-r-- 1 sfmqrb sfmqrb   81018 Sep  6 11:16 build213.py
-rw-rw-r-- 1 sfmqrb sfmqrb   21021 Sep  6 11:41 build232.py
-rw-rw-r-- 1 sfmqrb sfmqrb    6504 Sep  6 11:13 c1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3402 Sep  6 11:22 c224_n10.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4812 Sep  6 11:28 c224_n12.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4744 Sep  6 11:22 c224_n1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3203 Sep  6 11:28 c224_n7.png
-rw-rw-r-- 1 sfmqrb sfmqrb   12820 Sep  6 11:27 c229_bibua.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5308 Sep  6 11:27 c229_greek.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5313 Sep  6 11:27 c229_persian.png
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
drwxrwxr-x 2 sfmqrb sfmqrb    4096 Sep  6 11:44 p216
-rw-rw-r-- 1 sfmqrb sfmqrb   17907 Sep  6 11:25 part1.json
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
-rw-rw-r-- 1 sfmqrb sfmqrb   47149 Sep  6 11:44 pg236.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1209522 Sep  6 11:39 sin_goog.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  147680 Sep  6 11:20 sns167.jpg
```


### [2026-09-06T15:45:00.141Z] TOOL RESULT

```
Web search results for query: "ریشه‌شناسی کمند حسن‌دوست فرهنگ ریشه‌شناختی فارسی میانه kamand etymology"

Links: [{"title":"(PDF) نقد فرهنگ ریشه‌شناختی زبان فارسی [نوشتۀ دکتر محمد حسن‌دوست Review of \"An Etymological Dictionary of the Persian Language,\" by M. Hassandoust]","url":"https://www.academia.edu/24471058/%D9%86%D9%82%D8%AF_%D9%81%D8%B1%D9%87%D9%86%DA%AF_%D8%B1%DB%8C%D8%B4%D9%87_%D8%B4%D9%86%D8%A7%D8%AE%D8%AA%DB%8C_%D8%B2%D8%A8%D8%A7%D9%86_%D9%81%D8%A7%D8%B1%D8%B3%DB%8C_%D9%86%D9%88%D8%B4%D8%AA%DB%80_%D8%AF%DA%A9%D8%AA%D8%B1_%D9%85%D8%AD%D9%85%D8%AF_%D8%AD%D8%B3%D9%86_%D8%AF%D9%88%D8%B3%D8%AA_Review_of_An_Etymological_Dictionary_of_the_Persian_Language_by_M_Hassandoust_"},{"title":"فرهنگ ریشه‌شناختی فارسی، محمد حسن‌دوست، 1393 تهران، فرهنگستان زبان و ادب فارسی، دورۀ پنج جلدی","url":"https://lsi-linguistics.ihcs.ac.ir/article_1976.html"},{"title":"فرهنگ ریشه‌شناختی زبان فارسی - ویکی‌پدیا، دانشنامهٔ آزاد","url":"https://fa.wikipedia.org/wiki/%D9%81%D8%B1%D9%87%D9%86%DA%AF_%D8%B1%DB%8C%D8%B4%D9%87%E2%80%8C%D8%B4%D9%86%D8%A7%D8%AE%D8%AA%DB%8C_%D8%B2%D8%A8%D8%A7%D9%86_%D9%81%D8%A7%D8%B1%D8%B3%DB%8C"},{"title":"محمد حسن‌دوست - ویکی‌پدیا، دانشنامهٔ آزاد","url":"https://fa.wikipedia.org/wiki/%D9%85%D8%AD%D9%85%D8%AF_%D8%AD%D8%B3%D9%86%E2%80%8C%D8%AF%D9%88%D8%B3%D8%AA"},{"title":"حسن‌دوست: نوشتن «فرهنگ ریشه‌شناختی زبان فارسی» 16 سال زمان برد - ایبنا","url":"https://www.ibna.ir/news/232985/%D8%AD%D8%B3%D9%86-%D8%AF%D9%88%D8%B3%D8%AA-%D9%86%D9%88%D8%B4%D8%AA%D9%86-%D9%81%D8%B1%D9%87%D9%86%DA%AF-%D8%B1%DB%8C%D8%B4%D9%87-%D8%B4%D9%86%D8%A7%D8%AE%D8%AA%DB%8C-%D8%B2%D8%A8%D8%A7%D9%86-%D9%81%D8%A7%D8%B1%D8%B3%DB%8C-16-%D8%B3%D8%A7%D9%84-%D8%B2%D9%85%D8%A7%D9%86-%D8%A8%D8%B1%D8%AF"},{"title":"ایبنا - حسن‌دوست: نوشتن «فرهنگ ریشه‌شناختی زبان فارسی» 16 سال زمان برد","url":"http://www.ibna.ir/fa/doc/shortint/232985/%D8%AD%D8%B3%D9%86-%D8%AF%D9%88%D8%B3%D8%AA-%D9%86%D9%88%D8%B4%D8%AA%D9%86-%D9%81%D8%B1%D9%87%D9%86%DA%AF-%D8%B1%DB%8C%D8%B4%D9%87-%D8%B4%D9%86%D8%A7%D8%AE%D8%AA%DB%8C-%D8%B2%D8%A8%D8%A7%D9%86-%D9%81%D8%A7%D8%B1%D8%B3%DB%8C-16-%D8%B3%D8%A7%D9%84-%D8%B2%D9%85%D8%A7%D9%86-%D8%A8%D8%B1%D8%AF"},{"title":"کمند - معنی در دیکشنری آبادیس","url":"https://abadis.ir/fatofa/%DA%A9%D9%85%D9%86%D8%AF/"},{"title":"محمد حسن دوست نویسنده کتاب فرهنگ ریشه شناختی زبان فارسی(5جلدی) | ایران کتاب","url":"https://www.iranketab.ir/profile/23034-mohammad-hasandust"},{"title":"فرهنگ ریشه‌شناختی زبان فارسی | راهک","url":"https://raahak.com/?p=942"}]

Based on the search results, here's what I found about your query:

## فرهنگ ریشه‌شناختی زبان فارسی (Etymological Dictionary of Persian Language)

Farhang-e Risheshenasi-ye Zaban-e Farsi (Etymological Dictionary of the Persian Language) is a specialized dictionary for Persian etymology authored by Mohammad Hasandoust, published in five volumes in 1393 (2014/2015) by the Academy of Persian Language and Literature.

The book was recognized as a distinguished work in the 33rd edition of Iran's Book of the Year Award in the "Ancient Languages" category.

### About Middle Persian and Etymology in the Dictionary

Hasandoust's main work was to trace the history and background of each Persian word, initially identifying the origin of each Persian word in Middle Persian or Pahlavi and its older form in ancient Iran, then tracing the etymological root of the word.

### About the Word "Kamand" (کمند)

Kamand is a rope used in warfare that is thrown around an enemy's neck and pulled, and sometimes a person or thing is thrown upon it and pulled toward oneself. In Pahlavi it appears as "kamand" and in Kurdish as "kaman" (a rope with a movable knot).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-06T15:45:03.330Z] TOOL CALL #44: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg236.png"
}
```


### [2026-09-06T15:45:03.676Z] TOOL RESULT

```

```


## [2026-09-06T15:45:03.674Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-06T15:45:19.615Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== LEW camus ==\"; grep -n \"camus\" LEW_1910.txt | head -5; echo \"== SKT hame ==\"; grep -n -E \"hame\\b|Hame\" SKT.txt | head -5; echo \"== WEB hame ==\"; grep -n -oE \".{200}hame, n.{300}\" WEB_vol1.txt | head -3; echo \"== FSD hame ==\"; grep -n -oE \".{100}\\bhame\\b.{300}\" FSD_vol2.txt | head -3"
}
```


## [2026-09-06T15:45:20.883Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== SYN bridle/halter ==\"; grep -n -oE \".{0,150}halter.{0,250}\" SYN.txt | head -6; echo \"== IEC Kakolos ==\"; grep -n \"Kakolos\" IEC.txt | head -5"
}
```


### [2026-09-06T15:45:26.566Z] TOOL RESULT

```
== LEW camus ==
== SKT hame ==
15980:S:  tee  B«al  (i). to.    (L.)      From  pp.  of  L.  rt- Tcject.  —  L.  rc/>u*iium,  a  casting t  of  what  one  is  ashamed  of.— r :  /wi/',  base  of  p%niert,  to  feel Utior,  shame, t ;  see  FaffUimi. see  Pulsate . sec  Putative. Require ;  sec  Query. ,  Bequito ;  uc  Quiofc. S  ice  Bear  (j>. Be,  Beannouae.  a  bat   (E.) liXr,  %  bat;  from  the  flapping L—A.  S.   kr^ran,    to   agitate, motion,   allied   to   hr6r,  adj., U>.  a  mouse.     Cf.  prov.  V..JlUUr- flutter-mouse  or  bat. ard;  sec  Bear  (j). d,    to    repeal.     (F.-L.)      F.   rt- ^cancel:  Cot  L.  rt-jcituftn,  to Biul.  ••  L.    rt',    back  ;    scindere, ■ied  to  Sohiinu     (y^KID.) p.    to    cut    off.     (L)       L.    ab- n  cut  off.
17030:tGoth,  skarnfa,  shame,  Skt  kshan, .  (VSKA.) led.  (E.)  \.S.  dscamod,  pp.  of 'an,  to  put  to  shame  — AS.  a-,  ex- 1^  jtamiatt,  to  shame,  from  scamtt, tL§  Or  for  AS.  ofjcamod.  with  tbc HiK  (with  prefix  ff/*-.  off.  rcry). SL  (E.)  Northeni  E.iAow.  a&hamc, je  (hence,  trick).  '  \N  heea's  sham  is hose  fault  is  it?  Whitby  Gloiisar)'. «l.  sk0mm  (stem  Maavm-),  shame, De,  outrage.
17031:mefikoed.  modest.  (E.>  Comtp- |f  M.  £  tkatfu/ast,  modest.  —  A.  S. ■i  lit  Ann  in  iluune,  i.e.  in  modesty. ■inimii,  shame,  modesty ;  /<»/,  fast, KeFait Duuy,  Shamoy ;  see  Obamoia.
21720:Vam,  a  laqge  esculent  tober.  (Port.) Port,  inhame,  a  yam  (i.iltr^).  Remoter origin  udJcoowd  ;  btU  not  Euro^eaa.
== WEB hame ==
== FSD hame ==
67799:  and  seeds  massed  in kidneyshape.— k.*form,  a.  Kidney-shaped.— k.  dink,  n.  A link  on  a   hame  to  which  the  pole  is  attached  by  a   chain.—  k, » llpt,  a.  Hare-Upped.— k. -paved,  po.  [Eng.]  Paved  with cobblestones.— k. -piece,  n.  A   earn  which  has  the  appear- ance of  a   kidney.—  k.  potato,  any  kidney-shaped  potato.— kid'ney-root",  «.  J.  A   dioecious  shrub  (B
```


### [2026-09-06T15:45:30.735Z] TOOL RESULT

```
== SYN bridle/halter ==
ugrep: error: error at position 84
xbf][\x80-\xbf]*){0,250}
                        \___exceeds complexity limits


== IEC Kakolos ==
8537:Kakolos, om, is (Kakilis) ‘chip, splint’. Cf. WP I, 335 Skt. Sákalah, -am ‘splint; log’; Alb. (alleged) thekél, f. ‘peg, wedge, twig’; Li. Sakalys, m. ‘chip, splint. See next
8538:Kakis, io (Kakus, os, à, Kakina) ‘spike, prong’. Cf. Kakolos and Kaks- WP I, 333 Skt. cf. $akuláh ‘spur on cow's hoof; Per. (dim. form) (?) sagak ‘buckle’; Alb. thek, pl. thaké (fringe'; pl. ʻawns’) beside thekén, f. ‘rye’; Li. Sakà ‘branch’; Sake ‘fork’
```


## [2026-09-06T15:45:37.514Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/haam",
 "prompt": "Give the Dutch entry for haam: meaning (\"horse collar\"?) and etymology, including Middle Dutch and Proto-Germanic forms."
}
```


## [2026-09-06T15:45:39.278Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://etymologiebank.nl/trefwoord/haam1",
 "prompt": "What is the etymology of Dutch 'haam' (horse collar)? Quote what the dictionaries (EWN, Vercoullie, Franck-van Wijk) say, including any comparison with Lithuanian kamanos or Greek kemos."
}
```


### [2026-09-06T15:45:41.703Z] TOOL RESULT

```
# Dutch Entry for "Haam"

**Meaning:** A horse collar made of wood or leather for draught animals. A dated, rare sense also refers to a type of fishing net with a handle.

**Etymology:** The word traces back through several language stages:
- From Middle Dutch *hame*
- From Old Dutch *\*hamo*
- From Proto-West Germanic *\*hamō*
- From Proto-Germanic *\*hamô*, meaning "horse collar"

The term has cognates across Germanic languages and represents an ancient word for this essential piece of animal equipment used in farming and transport.
```


### [2026-09-06T15:45:46.801Z] TOOL RESULT

```
# Etymology of Dutch 'haam'

## Primary Etymological Sources

The major Dutch etymological dictionaries trace *haam* to Germanic roots meaning "covering" or "wrapping":

**EWN (Philippa et al.)** states the word derives from a "oorspr. betekenis 'bedekking, omhulling'" and connects it to Proto-Germanic *\*haman-* 'bedekken' (to cover), relating it to words like *hemd* (shirt) and *lichaam* (body).

**Franck-van Wijk (1936)** explains that across its various meanings, *haam* fundamentally means "omhulsel" (covering/wrapper), connecting it to Old High German *-hamo*, Middle High German *hame*, and Old Norse *hamr*.

**Vercoullie (1925)** suggests the original sense was uncertain but possibly derived from a Germanic root meaning "angular" (*ham*), though this explanation is less developed.

## Indo-European Comparison

Notably, the sources acknowledge but **do not affirm** comparisons with Greek *kēmós* (muzzle for horses) or Lithuanian equivalents. Van Wijk mentions these possibilities but concludes the Germanic "covering" etymology remains more probable. The EWN explicitly states that "zekere niet-Germaanse verwantschappen zijn er niet" (certain non-Germanic connections do not exist).
```


## [2026-09-06T15:46:13.436Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== CHEUNG kam ==\"; grep -n -E \"^\\*kam|kamān|kaman\" CHEUNG.txt | head -10; echo \"== HRN kamān ==\"; grep -n -i -E \"kaman|kemend|kamand\" HRN.txt HUB.txt NYB_vol2_glossary.txt PHD.txt | head -10; echo \"== SOD ==\"; grep -n -i \"kmnd\\|kamand\" SOD.txt | head -5"
}
```


### [2026-09-06T15:46:13.525Z] TOOL RESULT

```
== CHEUNG kam ==
15377:*kamp ‘to bend’ 
24237:CSogd. šm-, Sym- with Germ. *skam&- ‘to shame, be ashamed’, Goth. skaman, ON 
53459:skaman, 371 
== HRN kamān ==
PHD.txt:424:kaman [kin’n' | = M, N ~] bow. 5; 7 ~dar [-d'] | N ~] archer, bowman. ha er mae 4 ba kamar [kml | N —] waist; belt, girdle. ~-band [-bnd | N ~] belt. kāmģār [Emil | P k?*mg?*r, N ~] powerful, absolute. kamist [Amyst'] least. —jh: pad ~ih, at least. kāmistan, kām- [YCBEN-stn' < A ysbh, V shh; k*m-(y)stnt M k*m-yst] want, desire. kám|-rawág [km izvb*k! | N ~rawa] successful. ~-Z1(w)isn [-zywsn'] free, independent. kam-zór [kmzwl | N ~] weak. ~ih: weakness. kan-, v. kandan, kanar [kwl | N ~] side, edge; embrace. ~ag [-k' | M kr?rg, N ~a] edge, limit, boundary. --agómand [-k’wmnd | M -gwmnd] limited, finite. kandan, kan- [HPLWN-tn! < А V hpr; kn-dn', -tn! | M knd, N ~] dig; raze, destroy. kanig [knyk! | M knyg] girl, maid. kanizag [knyck! | M knycg, N kaniz(ak)] — kanig. kantigr [kntgl] quiver. kāpūr [ро | Ar. kāfūr] camphor. kar-, v. kardan. 1Kar [21 | M Pr, N ~] work, deed, affair. ~ framüdan: put to use. 2kàr [%'7], pl. —àn: (other) people. зкаг [%'/] butter. kār-, v. kištan. karafs [klips | N ~] celery. kār-āgāh [РА | N ~] skilled, experienced. ~ih: skill, experience. karak [krk! | N ~] quail. karan [kľn' | P bein, N ~] side, edge, end, limit. kārawān [%?/zv?x! | P k*rw'n, N kārwān] caravan, military column. ~ig [-yk! | N ~7] caravaneer, traveller. karb [klp] priest hostile to Zoroaster. karbāš [5/0 | N karbas, etc.] lizard. karbunag [k/pnk!, klbnk'] lizard. kard [krt! | M kyrd, N ~] action; matter, affair. кага [SK YN A < A skyn’; Kit! | N ~] knife. ikardag [kltk!] division, section, portion. *kardag [krtk!, kltk! | N karda] action. kārdāg [k'/d?k'] traveller, wanderer, migrant. kardaģān [Art-, Rlt&?n! | M kyrdg”n) action. kardagàár [Artk?l | M kyrdg’r, № ~] mighty. C 6084 E
PHD.txt:1059:bow (weapon) drón, kaman, sanwar.
== SOD ==
38526:kamande  (k'nVnty)
```


## [2026-09-06T15:46:13.898Z] TOOL CALL #50: WebSearch

```json
{
 "query": "Persian kamand lasso etymology Middle Persian kamand Hasandust \"kamān\" bend Iranian root"
}
```


### [2026-09-06T15:46:23.038Z] TOOL RESULT

```
Web search results for query: "Persian kamand lasso etymology Middle Persian kamand Hasandust "kamān" bend Iranian root"

Links: [{"title":"Persian Submitted Names (page 2) - Behind the Name","url":"https://www.behindthename.com/submit/names/usage/persian/2"},{"title":"Browse Submitted Names - Behind the Name","url":"https://www.behindthename.com/submit/names/usage/persian/length/6"},{"title":"Middle Persian literature","url":"https://en.wikipedia.org/wiki/Middle_Persian_literature"},{"title":"Category:Middle Persian language - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Category:Middle_Persian_language"},{"title":"\"lasso\" meaning in English","url":"https://kaikki.org/dictionary/English/meaning/l/la/lasso.html"},{"title":"کمند - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%DA%A9%D9%85%D9%86%D8%AF"},{"title":"Persian Online – Grammar & Resources » Middle Persian","url":"https://sites.la.utexas.edu/persian_online_resources/history-of-the-language/middle-persian/"},{"title":"Middle Persian","url":"https://en.wikipedia.org/wiki/Middle_Persian"},{"title":"lasso - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/lasso"}]

Based on the search results, I can provide you with information about the etymology of Persian "kamand" (lasso):

The Persian word کمند (kamand) comes from Middle Persian 𐭪𐭬𐭭𐭣 (kmnd /kamand/). The word means "rope, cord, lasso, noose" in Persian.

The search results confirm the connection to Middle Persian, and the word is documented in classical Persian literature—it appears in Jalāl ad-Dīn Mohammad Rūmī's Masnavi from around the 1260s.

However, the search results do not contain specific information about the further etymological details you mentioned, such as Hasandust's analysis, the connection to "kamān" meaning "bend," or the broader Iranian root derivation. To find detailed etymological analysis including those sources and connections, you may need to consult specialized etymological dictionaries or academic works on Iranian languages.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-06T15:46:26.641Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '38520,38532p' SOD.txt"
}
```


### [2026-09-06T15:46:26.693Z] TOOL RESULT

```
jL»&JJj  f   *^>- 


4644  k'm'ntk   B 
kamande  (k'nVnty) 
well-wisher,  liking 
TSP  5.75;  Frag.  Len.  71,  8 

4645  k'm'nty  -*  k'm'ntk 

4646  k'mS'r-   S  *=»  k>m-
```


## [2026-09-06T15:46:35.813Z] TOOL CALL #52: Bash

```json
{
 "command": "for u in \\\n 'https://en.wiktionary.org/wiki/%DA%A9%D9%85%D9%86%D8%AF' \\\n 'https://en.wiktionary.org/wiki/%CE%BA%CE%B7%CE%BC%CF%8C%CF%82' \\\n 'https://en.wiktionary.org/wiki/hame' \\\n 'https://en.wiktionary.org/wiki/haam' \\\n 'https://etymologiebank.nl/trefwoord/haam1' \\\n 'https://www.wisdomlib.org/definition/shakula' \\\n 'https://abadis.ir/fatofa/%D8%B3%DA%AF%DA%A9/' \\\n 'https://en.wiktionary.org/wiki/%D8%B3%DA%AF%DA%A9' ; do\n python3 tools/fetch_source.py \"$u\" --note 'pdf page 236, roots Kakis / Kam 1: sagak, sakulah, kamand, kemos, camus, haam, hame' 2>&1 | tail -2\ndone"
}
```


### [2026-09-06T15:46:42.927Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/b61890ccfad60159.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/dc9240414329c793.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6d98a5961b8a5c1e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/77cfaeaae4fe4eca.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/984e38cc97656da8.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8dde7f5c34bc5589.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9ed5048275a4a4ec.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/14db54952755b9c8.txt
```


## [2026-09-06T15:47:00.606Z] TOOL CALL #53: Bash

```json
{
 "command": "sed -n '1,80p' /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-06T15:47:00.654Z] TOOL RESULT

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


## [2026-09-06T15:47:02.608Z] TOOL CALL #54: Bash

```json
{
 "command": "sed -n '80,140p' /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-06T15:47:02.652Z] TOOL RESULT

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


## [2026-09-06T15:47:08.005Z] TOOL CALL #55: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg236.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/236.png && echo copied"
}
```


### [2026-09-06T15:47:08.074Z] TOOL RESULT

```
copied
```


## [2026-09-06T15:51:50.699Z] TOOL CALL #56: Bash

```json
{
 "command": "cat > /home/sfmqrb/git/rishe/data/verification/page-236.json <<'JSONEOF'\n{\n  \"pdf_page\": 236,\n  \"book_page\": 206,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-06\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Kakis, Kakus, Kakîna\",\n      \"verdict\": \"plausible\",\n      \"modern_form\": \"PIE *ḱāk- / *ḱank- 'branch, peg, spike' (Pokorny 523; WP I 335); Mann's *Kakis/*Kakus/*Kakinā are his own stem-variants of it\",\n      \"note\": \"The chart copies Mann (IEC 599) verbatim, including his stem set 'Kakis, io (Kakus, os, ā, Kakina)' and the gloss 'spike, prong'. Mann's capital K = PIE palatal *ḱ, and his entry cross-refers to Kakolos 'chip, splint' and Kaks- 'branch, bough' with 'Cf. WP I, 335' — i.e. this whole cluster is Pokorny's root ḱāk-2 (nasalized ḱank-) 'branch', IEW 523, whose material is Skt. śākhā 'bough', śakala- 'chip', śaṅku- 'peg, stake, wooden nail', śakti- 'spear', Lith. šakà 'branch', šakė 'fork', Alb. thekër, Goth. hōha 'plough'. The root family is therefore real and the language label 'Indo-European' is right; what is NOT standard is Mann's specific i-/u-/-īnā-stem reconstructions, which no other handbook sets up, and the narrowing of the gloss from 'branch, bough' to 'spike, prong'. Verdict plausible rather than confirmed. The two branches Nourai hangs on it are the two weakest items in Mann's own entry: he marks the Persian with '(?)' himself.\",\n      \"note_fa\": \"ریشهٔ نورایی «Kakis, Kakus, Kakîna» عیناً از فرهنگ تطبیقی هندواروپایی مان (IEC، ص ۵۹۹) گرفته شده است؛ حرف بزرگ K در نظام مان نشانهٔ کامی‌شدهٔ *ḱ است. این مجموعه در حقیقت گونه‌های ستاکیِ ریشهٔ هندواروپایی آغازین *ḱāk- / *ḱank- «شاخه، میخ، چوب» است که پوکورنی در ص ۵۲۳ فرهنگ خود (و والده‑پوکورنی، ج ۱ ص ۳۳۵) با شواهد سنسکریت śākhā «شاخه»، śaṅku- «میخ چوبی»، śakala- «تراشه»، لیتوانیایی šakà «شاخه» و šakė «چنگک» آورده است. پس خودِ ریشه و برچسب زبانی درست است، ولی بازسازی‌های ستاکیِ ویژهٔ مان (‑is/‑us/‑īnā) و تنگ‌کردنِ معنی از «شاخه» به «خار، نوک تیز» در هیچ مرجع دیگری نیست؛ از این رو داوری «با احتیاط پذیرفتنی».\",\n      \"sources\": [\n        \"https://www.wisdomlib.org/definition/shakula\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"IEC:599\", \"status\": \"supports\", \"note\": \"Mann, IEC.txt line 8538, leaf 339 of the local scan (= printed pp. 598–599, confirmed by the standalone folio numbers '598'/'599' on that leaf): 'Kakis, io (Kakus, os, à, Kakina) \\\"spike, prong\\\". Cf. Kakolos and Kaks- WP I, 333  Skt. cf. śakuláh \\\"spur on cow's hoof\\\"; Per. (dim. form) (?) sagak \\\"buckle\\\"; Alb. thek, pl. thaké \\\"fringe\\\"; Li. šakà \\\"branch\\\"; šakė \\\"fork\\\"'. Root name, gloss, page and both daughter nodes are exactly what the chart shows.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"POK\", \"where\": \"IEW 523, 'Root/lemma: ḱāk-2, nasalized ḱank-', POK_full.txt line ~49508\", \"stance\": \"partial\", \"note\": \"'Meaning: branch. Material: Old Indic śākhā f. \\\"bough\\\" (: Gothic hōha, Armenian cʿakʿ); śakala- \\\"chip, splinter\\\"; śaṅku- \\\"wooden nail, peg, plug, picket, pole, stick\\\"; śakti- \\\"spear, javelin\\\" … Lithuanian šakà \\\"bough\\\", šakė \\\"fork\\\" … References: WP. I 335'. The root exists with this comparanda but is glossed 'branch', not 'spike, prong', and Pokorny has neither śakula- nor Persian sagak.\"},\n        {\"src\": \"WLD\", \"where\": \"Bd. I pp. 333–334 (WLD_Bd1_pages.txt leaves 341–342)\", \"stance\": \"not_found\", \"note\": \"Mann's cross-reference 'WP I, 333' is wrong for this entry: printed pp. 333–334 of Walde-Pokorny I carry qau(e)lā 'Geschwulst', kaq- 'vermögen, helfen', qak- 'abmagern' and kak- 'männliche Geschlechtsteile' — nothing about branches or spikes. The right page is WP I 335, which is what Mann himself cites two lines earlier for Kakolos (IEC.txt line 8537).\"},\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985, IE roots appendix\", \"stance\": \"silent\", \"note\": \"grep of AHD_watkins1985.txt for kak-/ḱāk-/śakula finds no root of this shape; Watkins' appendix has no entry covering Skt. śākhā/śaṅku, so the AHD list is simply silent here.\"},\n        {\"src\": \"IEC\", \"where\": \"IEC.txt line 8537 (same leaf 339)\", \"stance\": \"supports\", \"note\": \"The adjacent entry 'Kakolos, om, is (Kakilis) \\\"chip, splint\\\". Cf. WP I, 335  Skt. śákalah, -am \\\"splint; log\\\"; Alb. thekél \\\"peg, wedge, twig\\\"; Li. šakalys \\\"chip, splint\\\". See next' shows that Mann himself files Kakis inside the ḱāk- 'branch' family.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Persian\",\n          \"words\": \"sagak «سگک»\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"NP سگک sagak is the ordinary word for the metal buckle of a belt or shoe strap. Formally, Mann's proposal is not impossible: PIE palatal *ḱ regularly gives Old Iranian *s- (cf. *ḱatam > OP θata-/Av. satəm, NP sad), and an intervocalic *-k- of a pre-form *saka-ka- would voice to -g- in Middle Persian, so *ḱak-a-ka- > MP *sagak > NP sagak would be phonetically regular. But there is no Old or Middle Iranian antecedent on record — MacKenzie's CPD and Nyberg's glossary have no sagak — and Persian lexicography reads the word the other way round: Dehkhodā glosses it 'مصغّر سگ' (diminutive of sag 'dog'), and Moʿin marks it '(اِ.مصغّر)' and gives 'سگ کوچک' as the first sense and the buckle as the second, i.e. a metaphorical diminutive of سگ 'dog' exactly like English mechanical 'dog' (a gripping catch) or Persian زبانه 'tongue' for the buckle's prong. Mann himself brackets the item '(dim. form) (?)'. Since the standard Persian dictionaries prefer a different origin, the arrow root→sagak is disputed; the word and its gloss 'buckle' are correct.\",\n          \"derivation_fa\": \"«سگک» در فارسی نو به معنی قلاب فلزی کمربند و بند کفش است. از نظر آوایی پیشنهاد مان نشدنی نیست: کامیِ *ḱ هندواروپایی در ایرانی باستان به s بدل می‌شود (مانند *ḱatam > اوستایی satəm، فارسی «صد») و ‑k‑ میان دو واکه در فارسی میانه نرم و به g بدل می‌شود، پس *ḱak‑a‑ka‑ > فارسی میانهٔ *sagak > «سگک» قاعده‌مند می‌بود. اما هیچ صورت ایرانی باستان یا میانه‌ای از آن گواهی نشده (در فرهنگ پهلوی مکنزی و واژه‌نامهٔ نیبرگ نیست) و واژه‌شناسی فارسی راه دیگری می‌رود: دهخدا آن را «مصغّر سگ» می‌داند و معین نیز با نشانهٔ (اِ.مصغّر) نخست «سگ کوچک» و سپس «نوعی قلاب چهارگوش یا نیم‌دایره» می‌آورد؛ یعنی سگک را کاربردی استعاری از «سگ» می‌گیرند، درست مانند dog در اصطلاح فنی انگلیسی به معنی گیره. خودِ مان هم این مدخل را با «(؟)» مشکوک نشان داده است. بنابراین پیوند سگک به ریشهٔ «خار/نوک» را پژوهش امروزی رد می‌کند، هرچند خود واژه و معنی «قلاب» درست است.\",\n          \"sources\": [\n            \"https://abadis.ir/fatofa/%D8%B3%DA%AF%DA%A9/\",\n            \"https://en.wiktionary.org/wiki/%D8%B3%DA%AF%DA%A9\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"IEC:599\", \"status\": \"supports\", \"note\": \"IEC.txt line 8538: 'Per. (dim. form) (?) sagak \\\"buckle\\\"'. Mann does list it under Kakis exactly as drawn — but with his own query mark, which Nourai's chart drops.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"Farhang-e Fārsi s.v. سگک (MON_part1.txt line 78894)\", \"stance\": \"contradicts\", \"note\": \"'سگک: (اِ.مصغّر) سگ کوچک. نوعی قلاب چهارگوش یا نیم‌دایره که برای بستن کفش، پوتین و کمربند لباس بکار رود' — Moʿin classes it grammatically as a diminutive of سگ 'dog', not as an inherited *ḱak- derivative.\"},\n            {\"src\": \"BQT\", \"where\": \"Borhān-e Qāteʿ with Moʿin's footnotes (grep of BQT_v1/v2/v3/v4_pages.txt for سگک)\", \"stance\": \"silent\", \"note\": \"No headword سگک in Borhān-e Qāteʿ, hence no Moʿin etymological footnote for it.\"},\n            {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD, k-/s- sections (PHD.txt, PHD_mackenzie.txt)\", \"stance\": \"silent\", \"note\": \"grep for 'sagak'/'sgk' yields nothing; no Middle Persian antecedent is recorded, so the chain root → MP → NP cannot be filled in.\"},\n            {\"src\": \"HRN\", \"where\": \"Horn, Grundriss der neupersischen Etymologie\", \"stance\": \"silent\", \"note\": \"grep of HRN.txt (and HUB.txt) for 'sagak' returns nothing — Horn and Hübschmann do not treat the word.\"},\n            {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e Rishe-hā-ye Hend-o-Orupāyi (ARY_pages.txt)\", \"stance\": \"silent\", \"note\": \"grep for سگک finds nothing; only the front matter of this scan is OCRed, so the silence is partly a limitation of the text.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Sanskrit\",\n          \"words\": \"sakulah\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The word is Skt. śakula- (the chart's 'sakulah' is Nourai's usual undiacriticised transliteration of Mann's śakuláḥ; the printed page shows 'sakulah', so the extraction is faithful). Monier-Williams gives it two senses: 'a kind of fish' (Vājasaneyi-Saṃhitā, Atharvaveda, Mahābhārata) and 'a kind of spur-like projection (behind the hoof of an ox or cow)' — the latter is exactly the gloss on the chart, so the word and meaning check out. The attachment to *ḱāk- is Mann's own: PIE *ḱ > Indic ś is regular, and the formation matches śakala- 'chip, splinter' which Pokorny (IEW 523) does file under ḱāk-2 'branch', so a *ḱak-ula- 'little prong' beside *ḱak-ala- 'little chip' is a reasonable formation. But neither Pokorny nor Walde-Pokorny lists śakula- at all, and the fish sense (the far commoner one) suggests the two may be homonyms. Hence plausible, not confirmed.\",\n          \"derivation_fa\": \"واژهٔ سنسکریت śakula- است («sakulah» در نمودار همان آوانگاری بی‌نشانهٔ نوراییِ śakuláḥ مان است؛ در صفحهٔ چاپی هم «sakulah» آمده، پس خطای خوانش اسکن در کار نیست). مونیه‑ویلیامز دو معنی می‌دهد: «گونه‌ای ماهی» (در وājasaneyi‑saṃhitā، اتهرَوَه‌ودَه و مهابهاراتَه) و «برجستگی خارمانند در پشت سُم گاو» — و همین معنی دوم است که نورایی آورده؛ پس واژه و معنی درست است. پیوند آن به ریشهٔ *ḱāk- اما از خودِ مان است: بدل‌شدن *ḱ هندواروپایی به ś هندی قاعده‌مند است و ساخت śakula- با śakala- «تراشه» می‌خواند که پوکورنی (ص ۵۲۳) آن را زیر همین ریشه آورده است؛ ولی نه پوکورنی و نه والده‑پوکورنی śakula- را اصلاً ذکر نکرده‌اند و معنی رایج‌ترِ «ماهی» احتمال هم‌آوایی دو واژهٔ جداگانه را پیش می‌کشد. از این رو داوری: با احتیاط پذیرفتنی.\",\n          \"sources\": [\n            \"https://www.wisdomlib.org/definition/shakula\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"IEC:599\", \"status\": \"supports\", \"note\": \"IEC.txt line 8538 (leaf 339 = pp. 598–599): 'Skt. cf. śakuláh \\\"spur on cow's hoof\\\"'. Word, gloss and page as cited; note Mann's own hedge 'cf.'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"IEW 523 s.v. ḱāk-2 (POK_full.txt ~line 49514)\", \"stance\": \"partial\", \"note\": \"Lists 'śakala- m. n. \\\"chip, splinter, splinter, wooden log\\\" (: Lithuanian šakalys)' and 'śaṅku- m. \\\"wooden nail, peg, plug, picket, pole, stick\\\"' under this root, but not śakula-; so the formation-type is confirmed while this particular word is not.\"},\n            {\"src\": \"WLD\", \"where\": \"Walde-Pokorny I 333–335 (WLD_Bd1_pages.txt leaves 341–343)\", \"stance\": \"not_found\", \"note\": \"śakula- does not appear on the pages Mann cites; grep of WLD_Bd1 for 'sakula'/'çakula' returns nothing.\"},\n            {\"src\": \"SYN\", \"where\": \"Buck, Dictionary of Selected Synonyms\", \"stance\": \"silent\", \"note\": \"Buck has no entry for 'spur/hoof-projection'; grep for śakula returns nothing.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985\", \"stance\": \"silent\", \"note\": \"no root of the shape *ḱak- and no Sanskrit śakula- anywhere in the appendix.\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 4,\n      \"root\": \"Kam 1\",\n      \"verdict\": \"plausible\",\n      \"modern_form\": \"PIE *kem- 'to press, squeeze, restrain' (Pokorny 555 kem-1; WP I 388 f.)\",\n      \"note\": \"Nourai's 'Kam 1: to restrain' is Mann's entry 'kam- (2) \\\"restrain\\\"; kam-, kamont- \\\"rein, bridle, horse-collar\\\"' (IEC 466). Note the numbering shift: Mann's kam- (1) is 'tire, worry' and it is his kam- (2) that Nourai renumbers as 'Kam 1' — the chart's content, not its label, is what matches. Mann's kam- (2) is Pokorny's kem-1 'to press, squeeze' (IEW 555), whose material includes ON hemja 'curb, restrain', MHG hemmen 'hinder', NHG dial. ham, hamen 'horse collar', MLG ham, and Lith. kamanos 'leathery bridle, rein', kamuoti 'press together' — i.e. the 'restrain' → 'bridle/collar' semantics of the chart is genuine handbook doctrine. Two of Nourai's four branches, however, are not: Pokorny explicitly ejects Greek kēmós from the root, and the Persian branch rests on Mann alone. Root, language label and gloss are otherwise sound.\",\n      \"note_fa\": \"ریشهٔ «Kam 1: بازداشتن» در کتاب نورایی همان مدخل «kam- (2)» مان (IEC ص ۴۶۶) است؛ توجه کنید که شمارهٔ نورایی با مان نمی‌خواند: kam- (1) نزد مان «خسته‌کردن» است و آنچه نورایی «Kam 1» می‌نامد kam- (2) اوست. این ریشه با «kem‑1: فشردن، چلاندن» پوکورنی (ص ۵۵۵؛ والده‑پوکورنی ج ۱ ص ۳۸۸ به بعد) یکی است که شواهدش نورس باستان hemja «مهار کردن»، آلمانی میانه hemmen «بازداشتن»، آلمانی گویشی ham/hamen «یوغِ گردنِ اسب»، و لیتوانیایی kamanos «افسار چرمی» است؛ پس گذارِ معناییِ «بازداشتن ← افسار/یوغ» که نمودار نشان می‌دهد بنیاد کتابی دارد. با این حال دو شاخه از چهار شاخهٔ نورایی استوار نیست: پوکورنی صریحاً kēmós یونانی را از این ریشه بیرون می‌گذارد و شاخهٔ فارسی تنها بر مان تکیه دارد. برچسب زبانی و معنیِ ریشه درست است؛ داوری: با احتیاط پذیرفتنی.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/%CE%BA%CE%B7%CE%BC%CF%8C%CF%82\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"IEC:466\", \"status\": \"supports\", \"note\": \"Mann, IEC.txt line 6697, leaf 268 of the local scan, on which the folio number '467' is printed (so the leaf carries pp. 466–467, matching the citation): 'kam- (2) \\\"restrain\\\"; kam-, kamont- \\\"rein, bridle, horse-collar\\\"  Per. kamand \\\"halter\\\"; Du. haam: E hames \\\"horse-collar\\\" beside MHG hamen, ON hemja \\\"restrain\\\"; Li. kamanos, kamunos \\\"bridle-bit\\\" beside kamantai \\\"wooden parts of bridle\\\". Cf. variant (*-ā-) in Gk. kemós (Doric: -ā-) \\\"halter\\\". LW in Lat. camus.' Every node of the chart is on this one page.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"POK\", \"where\": \"IEW 555, 'Root/lemma: kem-1, Meaning: to press, squeeze' (POK_full.txt ~line 45184)\", \"stance\": \"partial\", \"note\": \"'Old Norse hemja (hamda) \\\"curb, restrain, hinder, hamper\\\" … Middle High German hemmen and hamen \\\"hinder, hamper\\\" … Modern High German dial. ham, hamen \\\"horse collar\\\" … Lithuanian kamuoti \\\"press together, stuff\\\", kamanos \\\"leathery bridle, rein\\\"'. Supports the root and the Germanic/Baltic material, but ends: 'gr. κημός (*kamos because of Latin loanword camus) \\\"muzzle\\\" is not compatible in vocalism' — i.e. Pokorny rejects the Greek branch Nourai draws.\"},\n        {\"src\": \"WLD\", \"where\": \"Walde-Pokorny I 388 f. (cited by Pokorny at IEW 555)\", \"stance\": \"supports\", \"note\": \"Pokorny's own 'References: WP. I 388 f., Trautmann 115, 126' for kem-1; the Germanic 'horse collar' words are already gathered there.\"},\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985 (AHD_watkins1985.txt)\", \"stance\": \"contradicts\", \"note\": \"Watkins has no root *kam-/*kem- 'restrain'; his index line reads 'HAME  tkei-', and the root tkei- 'to settle, dwell, be home' includes 'c. Middle Dutch hame, hame (< \\\"covering\\\"): HAME'. So the AHD appendix assigns the harness word to an entirely different root.\"},\n        {\"src\": \"IEC\", \"where\": \"IEC.txt line 6694 (same leaf 268)\", \"stance\": \"partial\", \"note\": \"Mann's kam- (1) is 'tire, worry' (Gk. kámnō, Li. kamuoti), so Nourai's label 'Kam 1' does not correspond to Mann's numbering even though the content is Mann's kam- (2).\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Persian\",\n          \"words\": \"kamand «کمند»\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"NP کمند kamand is a lasso/noose — Moʿin: 'رسمانی محکم که هنگام جنگ آن را بر گردن و کمر دشمن اندازند و وی را به بند در آورند و یا جانوران را بدان مقید کنند' ('a stout rope thrown in battle round the neck and waist of the enemy to bind him, or used to tether animals'); Nourai's English gloss 'halter' is Mann's word, and understates it. The word is old: Moʿin's etymological footnote in Borhān-e Qāteʿ (vol. 3) writes 'کمند … پهلوی kamand … کردی komen (طناب با گره متحرک)', and Wiktionary likewise derives it from Middle Persian 𐭪𐭬𐭭𐭣 kamand; it is common from Ferdowsi and Farroxi onward (the chart quotes Hāfez: 'می نوش و جهان بخش که از زلف کمندت / شد گردن بدخواه گرفتار سلاسل'). What is not independently attested is the further step to PIE *kem- 'press, restrain': neither MacKenzie's CPD nor Nyberg records a Pahlavi kamand (Wiktionary's MP form is a back-projection from Book Pahlavi spelling), Horn, Hübschmann and Cheung are silent, and no handbook analyses the -and. A derivation from *kam- 'restrain' with an -and formation is semantically apt ('the restrainer'), but rests on Mann alone; hence plausible.\",\n          \"derivation_fa\": \"«کمند» در فارسی نو ریسمانی است با گرهٔ روان — معین می‌نویسد: «رسمانی محکم که هنگام جنگ آن را بر گردن و کمر دشمن اندازند و وی را به بند در آورند و یا جانوران را بدان مقید کنند»؛ برگردان انگلیسیِ نورایی («halter» = افسار) از مان گرفته شده و رساننده نیست. واژه کهن است: در حواشی معین بر برهان قاطع (ج ۳) آمده «کمند … پهلوی kamand … کردی komen (طناب با گرهٔ متحرک)» و ویکی‌واژه نیز آن را از فارسی میانهٔ kamand می‌گیرد؛ در شعر فارسی از فرخی و فردوسی تا حافظ (بیتِ نقل‌شده در نمودار) پرکاربرد است. اما گام بعدی، یعنی پیوند به ریشهٔ هندواروپاییِ *kem- «فشردن، بازداشتن»، گواه مستقلی ندارد: در فرهنگ پهلوی مکنزی و واژه‌نامهٔ نیبرگ صورت پهلوی kamand نیامده، هرن و هوبشمان و چونگ خاموش‌اند و هیچ مرجعی پسوند ‑and را تحلیل نکرده است. ساختِ «کمند = بازدارنده» از نظر معنایی مناسب است ولی تنها به مان تکیه دارد؛ پس: با احتیاط پذیرفتنی.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%DA%A9%D9%85%D9%86%D8%AF\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"IEC:466\", \"status\": \"supports\", \"note\": \"IEC.txt line 6697 (leaf 268, printed pp. 466–467): 'Per. kamand \\\"halter\\\"' stands first in Mann's material for kam- (2) 'restrain', exactly as the chart draws it.\"},\n            {\"ref\": \"MON:3076\", \"status\": \"partial\", \"note\": \"The entry exists (MON_part2.txt line 26516, Farhang-e Fārsi vol. 3): 'کمند: … رسمانی محکم که هنگام جنگ آن را بر گردن و کمر دشمن اندازند … خم کمند … زلف کمند …'. It supports the word and its sense but carries NO origin bracket (no [په.] tag) and no etymology, so it cannot support the arrow from a PIE root. The printed folio number is illegible in this OCR, so 3076 itself could not be confirmed.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BQT\", \"where\": \"Borhān-e Qāteʿ ed. Moʿin, vol. 3, pdf p. 490 of BQT_v3_picofile.pdf (incoming/BQT/BQT_v3_pages.txt line 36056)\", \"stance\": \"partial\", \"note\": \"Footnote to the headword: 'کمند - بفتح اول و دوم، پهلوی kamand … کردی komen (طناب با گره متحرک)'; the entry body reads 'دام و طنابی که در جنگ بر گردن دشمن یا در شکار بر گردن حیوان می‌انداختند و او را بجای خود می‌کشیدند'. Moʿin gives a Pahlavi antecedent and a Kurdish cognate but no Indo-European root.\"},\n            {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD (PHD.txt line 424, k- section)\", \"stance\": \"silent\", \"note\": \"The k- run has 'kaman [kmn' | M, N ~] bow', 'kamandar [-d'r] archer, bowman', 'kamar waist; belt' — but no kamand 'lasso'. MacKenzie does not record the Middle Persian word.\"},\n            {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II (Glossary)\", \"stance\": \"silent\", \"note\": \"grep of NYB_vol2_glossary.txt for 'kamand' returns nothing.\"},\n            {\"src\": \"HRN\", \"where\": \"Horn, Grundriss (HRN.txt); Hübschmann, Persische Studien (HUB.txt)\", \"stance\": \"silent\", \"note\": \"grep for 'kamand'/'kamānd' in both returns nothing; neither treats the word.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"Cheung, Etymological Dictionary of the Iranian Verb (CHEUNG.txt)\", \"stance\": \"silent\", \"note\": \"the only *kam- root indexed is '*kamp \\\"to bend\\\"' (line 15377); there is no Iranian verbal root *kam- 'restrain' from which kamand could be built.\"},\n            {\"src\": \"SOD\", \"where\": \"Gharib, Sogdian Dictionary no. 4644 (SOD.txt line 38526)\", \"stance\": \"silent\", \"note\": \"the only similar Sogdian form, k'm'ntk 'well-wisher, liking', belongs to kām 'desire', not to a 'restrain' root; Sogdian has no cognate of kamand.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Greek\",\n          \"words\": \"kĕmos\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Greek κημός (Ionic-Attic kēmós, Doric κᾱμός kāmós) is real and means 'muzzle for a led horse, nose-bag', also 'wicker weel' and 'funnel-shaped top of a voting urn'. Two things are wrong with the chart. (a) The vowel: the book prints 'kĕmos' with a breve, marking a short e, but the word has eta, i.e. long ē (Mann prints simply 'kemós'); this is a slip of Nourai's diacritic, faithfully extracted. (b) The derivation: Pokorny states flatly at IEW 555, at the end of kem-1, 'gr. κημός (*kāmos because of the Latin loanword camus) \\\"muzzle\\\" is not compatible in vocalism' — the Doric ā cannot be reconciled with the e-vocalism of the Germanic-Baltic set, so he excludes it from the root. Beekes' Etymological Dictionary of Greek (followed by Wiktionary) calls the origin 'unexplained', rejecting the Armenian, Lithuanian, Russian and MHG comparisons and suggesting with Furnée a Pre-Greek source shared with χάβος/χαμόν. So the arrow root → kēmos is disputed: the word is not derivable from *kem- 'restrain' and is probably a substrate word.\",\n          \"derivation_fa\": \"واژهٔ یونانی κημός (ایونی‑آتیک kēmós، دوری κᾱμός) واقعی است و «پوزه‌بند اسب، توبرهٔ خوراک» و نیز «سبد ماهیگیری» و «سرِ قیف‌مانند صندوق رأی» معنی می‌دهد. دو اشکال در نمودار هست: نخست آنکه کتاب «kĕmos» با نشانهٔ کوتاهی چاپ کرده، حال آنکه واژه با «اتا» و کشیده است (مان خودش ساده «kemós» می‌نویسد) — لغزشِ نشانه‌گذاری خودِ نورایی است، نه خطای خوانش اسکن. دوم و مهم‌تر: پوکورنی در پایان مدخل kem‑1 (ص ۵۵۵) صریح می‌گوید «κημός یونانی (که به سببِ وام‌واژهٔ لاتینی camus باید *kāmos باشد) از نظر واکه با این ریشه نمی‌خواند» و آن را بیرون می‌گذارد؛ بیکس نیز (و به پیروی او ویکی‌واژه) خاستگاه آن را «توضیح‌ناپذیر» می‌داند و با فورنه آن را واژه‌ای پیش‑یونانی هم‌خانوادهٔ χάβος و χαμόν می‌شمارد. پس این پیکان را پژوهش امروزی رد می‌کند.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%CE%BA%CE%B7%CE%BC%CF%8C%CF%82\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"IEC:466\", \"status\": \"supports\", \"note\": \"IEC.txt line 6697: 'Cf. variant (*-ā-) in Gk. kemós (Doric: -ā-) \\\"halter\\\". LW in Lat. camus.' Mann does put kēmos here, but only as an ablaut 'variant', and it is precisely this that Pokorny had already rejected.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"IEW 555, end of kem-1 (POK_full.txt line ~45218)\", \"stance\": \"contradicts\", \"note\": \"'gr. Kημός (*kamos because of Latin loanword camus) \\\"muzzle\\\" is not compatible in vocalism' — an explicit rejection of the link Nourai draws.\"},\n            {\"src\": \"WLD\", \"where\": \"Walde-Pokorny I 388 f. (Pokorny's source for kem-1)\", \"stance\": \"contradicts\", \"note\": \"Pokorny's discussion, including the dismissal of κημός and of Persson's attempt to attach κάμαξ/κῶμος, reproduces WP I 388 f.; the Greek word is not admitted into the root there either.\"},\n            {\"src\": \"LAT\", \"where\": \"Ernout-Meillet, DELL p. 163 s.v. camus (LAT.txt line 9093)\", \"stance\": \"partial\", \"note\": \"'camus, -ī m.: muselière. Emprunt au gr. κᾰμός (ion.-att. κημός)' — confirms the Greek word and its Doric ā, but treats it only as the donor of the Latin word, offering no IE root.\"},\n            {\"src\": \"IEC\", \"where\": \"IEC.txt line 6697\", \"stance\": \"partial\", \"note\": \"Mann is the only book in the local library that files κημός under a 'restrain' root, and even he hedges it as a 'variant'.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Latin\",\n          \"words\": \"câmus\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Latin cāmus 'muzzle, halter' (Nourai's circumflex marks the long ā; the added gloss 'yoke' comes from the late/Vulgate use of camus for the bit or curb, e.g. Vulg. Ps. 31:9 'in camo et freno'). It is a straight loan from Greek, and specifically from the Doric-Aeolic form κᾱμός rather than Ionic-Attic κημός: Ernout-Meillet, DELL p. 163, 'camus, -ī m.: muselière. Emprunt au gr. κᾰμός (ion.-att. κημός)', and Pokorny IEW 555 uses the very existence of Latin camus to prove that the Greek base vowel was ā. The loan is old enough (Plautus-era contact with the Greek South-Italian colonies, where Doric was spoken) that the ā was taken over unchanged; there is also a neuter by-form camum. So the edge Greek → Latin drawn by Nourai is exactly right, even though the node above it (the Greek word's own origin) is not.\",\n          \"derivation_fa\": \"لاتینی cāmus «پوزه‌بند، افسار» (نشانهٔ ^ در نگارش نورایی همان کشیدگیِ ā است؛ معنی افزودهٔ «یوغ» از کاربرد متأخر و کتاب‌مقدسی camus برای دهانه و لگام می‌آید، مانند مزامیر ۳۱:۹ «in camo et freno»). این واژه وام‌واژه‌ای است از یونانی و دقیقاً از گونهٔ دوری κᾱμός نه ایونی‑آتیکِ κημός: ارنو و مه‌یه در فرهنگ ریشه‌شناختی لاتین (ص ۱۶۳) می‌نویسند «camus, -ī m.: muselière. Emprunt au gr. κᾰμός (ion.-att. κημός)»، و پوکورنی (ص ۵۵۵) نیز از همین وام‌گیری برای اثبات کشیدگیِ ā در صورت یونانی بهره می‌گیرد. وام‌گیری چندان کهن است (تماس رومیان با مستعمره‌های دوری‌زبانِ جنوب ایتالیا) که ā بی‌دگرگونی وارد لاتین شده است. پس پیکان یونانی ← لاتین در نمودار درست است، هرچند خودِ گرهِ بالادستی درست نیست.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%CE%BA%CE%B7%CE%BC%CF%8C%CF%82\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"IEC:466\", \"status\": \"supports\", \"note\": \"IEC.txt line 6697: '… Gk. kemós (Doric: -ā-) \\\"halter\\\". LW in Lat. camus' — Mann explicitly calls Latin camus a loanword ('LW') from the Greek word, which is the arrow drawn.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"LAT\", \"where\": \"Ernout-Meillet, DELL p. 163 (LAT.txt lines 9087, 9093)\", \"stance\": \"supports\", \"note\": \"'camum, -ī n. (camus m.): φορβειά ἐκ σχοινίων; sorte de bifère. Mot …' and 'camus, -ī m.: muselière. Emprunt au gr. κᾰμός (ion.-att. κημός). - 163 -'. Direct confirmation of the borrowing.\"},\n            {\"src\": \"POK\", \"where\": \"IEW 555 (POK_full.txt line ~45218)\", \"stance\": \"supports\", \"note\": \"Pokorny reconstructs the Greek etymon as '*kāmos because of Latin loanword camus', i.e. he too treats camus as borrowed from Greek.\"},\n            {\"src\": \"LEW\", \"where\": \"Walde, Lateinisches etymologisches Wörterbuch, 2nd ed. 1910 (LEW_1910.txt)\", \"stance\": \"silent\", \"note\": \"grep for 'camus' in the local 1910 scan returns no hit (the OCR of the c- section is poor); could not be used either way.\"},\n            {\"src\": \"KLN\", \"where\": \"Klein, CEDEL (KLN_1966.txt line 6311)\", \"stance\": \"silent\", \"note\": \"Klein's only 'camus' is the unrelated English/French adjective camus 'flat-nosed' (from pejorative ca- + the base of museau); he has no entry for the Latin harness word.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Dutch\",\n          \"words\": \"haam\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Dutch haam is the wooden or leather collar of a draught horse (also, obsolete, a hand fishing-net) < Middle Dutch hame < Old Dutch *hamo < Proto-West-Germanic *hamō < Proto-Germanic *hamô. Nourai's gloss 'halter' is loose — it is the collar, not the head-stall. On the root, the books split. Pokorny (IEW 555, kem-1 'to press, squeeze') does gather the Germanic harness words here — 'Modern High German dial. ham, hamen \\\"horse collar\\\"', MLG ham, beside ON hemja 'curb, restrain' and Lith. kamanos 'leathery bridle' — which is essentially Nourai's chart. The Dutch tradition takes the other line: EWN (Philippa et al.) gives the original sense as 'bedekking, omhulling' and ties haam to Proto-Germanic *haman- 'to cover' with hemd 'shirt' and lichaam 'body', adding that 'zekere niet-Germaanse verwantschappen zijn er niet'; Franck-van Wijk (1936) likewise reduces all senses to 'omhulsel' (cf. OHG -hamo, MHG hame, ON hamr 'skin, slough') and mentions the comparison with Gk. kēmós and the Lithuanian words only to leave it unaffirmed. Klein reaches the same conclusion from the English side (base *kam-, *kem- 'to cover'). So the derivation is defensible on Pokorny's authority but is not the majority Germanic view: plausible.\",\n          \"derivation_fa\": \"«haam» هلندی یوغِ چوبی یا چرمینِ گردنِ اسبِ بارکش است (و در کاربرد کهنه، نوعی تور دستی ماهیگیری): از هلندی میانهٔ hame، هلندی باستان *hamo، ژرمنیِ غربی آغازین *hamō و ژرمنیِ آغازین *hamô. برگردانِ «halter» (افسار) در نمودار دقیق نیست؛ این واژه به یوغِ گردن اشاره دارد نه به دهنه. دربارهٔ ریشه، مراجع دو دسته‌اند: پوکورنی (ص ۵۵۵، ریشهٔ kem‑1 «فشردن») همین واژه‌های ژرمنیِ مربوط به یراقِ اسب را زیر این ریشه می‌آورد — آلمانی گویشی ham/hamen «یوغِ گردنِ اسب»، آلمانیِ سفلای میانه ham، در کنار نورس hemja «مهار کردن» و لیتوانیایی kamanos «افسار چرمی» — که همان نمودار نورایی است. اما سنت ریشه‌شناسی هلندی راه دیگری می‌رود: فرهنگ EWN معنی نخستین را «پوشش، غلاف» می‌داند و haam را به ژرمنیِ آغازین *haman- «پوشاندن» و هم‌ریشه با hemd «پیراهن» و lichaam «تن» می‌بندد و می‌افزاید «هم‌ریشگیِ قطعیِ غیرِژرمنی در کار نیست»؛ فرانک‑فان‌وایک نیز همهٔ معانی را به «غلاف» بازمی‌گرداند و مقایسه با κημός یونانی را تأیید نمی‌کند. کلاین هم از سوی انگلیسی به همین نتیجه می‌رسد (پایهٔ *kam-/*kem- «پوشاندن»). پس ادعای نورایی با تکیه بر پوکورنی دفاع‌پذیر است ولی رأی اکثریتِ ژرمنی‌شناسان نیست: با احتیاط پذیرفتنی.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/haam\",\n            \"https://etymologiebank.nl/trefwoord/haam1\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"IEC:466\", \"status\": \"supports\", \"note\": \"IEC.txt line 6697: 'Du. haam: E hames \\\"horse-collar\\\" beside MHG hamen, ON hemja \\\"restrain\\\"' — Mann lists Dutch haam under kam- (2) 'restrain' just as the chart draws it (the OCR reads 'baam' for haam).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"IEW 555 s.v. kem-1 (POK_full.txt line ~45184)\", \"stance\": \"supports\", \"note\": \"'Modern High German dial. ham, hamen \\\"horse collar\\\" … Middle Low German ham, Old English hamm \\\"enclosed piece of land\\\"' listed beside ON hemja 'curb, restrain' — the Germanic harness words are inside the 'press/restrain' root.\"},\n            {\"src\": \"KLN\", \"where\": \"Klein, CEDEL s.v. hame (KLN_1966.txt line 17132)\", \"stance\": \"contradicts\", \"note\": \"'rel. to MDu. hamme, Du. haam, \\\"collar of a horse\\\", ON. hamr, \\\"skin, covering\\\", OHG. hamo … and cogn. with OI. śamulyaḥ, \\\"woolen shirt\\\"; fr. I.-E. base *kam-, *kem-, \\\"to cover\\\"' — Klein's root is 'cover', not 'restrain'.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. tkei- and index 'HAME tkei-'\", \"stance\": \"contradicts\", \"note\": \"'c. Middle Dutch hame, hame (< \\\"covering\\\"): HAME' under the root tkei- 'to settle, dwell, be home' — a third assignment, again away from *kem- 'restrain'.\"},\n            {\"src\": \"DOZ\", \"where\": \"Dozy, Oosterlingen (DOZ.txt)\", \"stance\": \"silent\", \"note\": \"the Dutch orientalisms list has nothing on haam, as expected for an inherited Germanic word.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"English\",\n          \"words\": \"hame\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English hame 'either of the two curved pieces of wood or metal lying round a draught horse's collar, to which the traces are attached' first appears c. 1300 as ME hame, and the borrowing from Dutch that Nourai draws is the standard account: OED/Wiktionary derive it from Middle Dutch hame 'horse collar, harness, fishnet' (< Proto-Germanic *hamô), and Watkins' AHD appendix likewise cites 'Middle Dutch hame … : HAME'. The route fits the Anglo-Flemish trade and the heavy influx of Low Countries agricultural vocabulary into eastern-English farming terms in the 13th-14th c.; the word is almost always used in the plural (hames), which is the form Mann quotes. The one dissenting handbook is Klein, who takes ME hame as inherited from OE hama 'cover, skin' and treats MDu. hamme/Du. haam as merely related — but that only shifts inheritance vs. borrowing within the same Germanic word-family, and does not affect the arrow as drawn. The gloss 'part of a harness' is accurate. The node's verdict concerns the Dutch → English edge, which is confirmed; the ultimate root remains as uncertain as at node #4.\",\n          \"derivation_fa\": \"واژهٔ انگلیسی hame «هر یک از دو تکهٔ خمیدهٔ چوبی یا فلزی که بر گِردِ یوغِ گردنِ اسبِ بارکش می‌نشیند و بندهای مال‌بند به آن بسته می‌شود» نخستین بار حدود ۱۳۰۰ میلادی به صورت انگلیسی میانهٔ hame دیده می‌شود، و همان وام‌گیری از هلندی که نورایی رسم کرده رأی معیار است: فرهنگ آکسفورد و ویکی‌واژه آن را از هلندی میانهٔ hame «یوغِ گردنِ اسب، یراق، تور ماهیگیری» (از ژرمنیِ آغازین *hamô) می‌گیرند و پیوستِ واتکینز در فرهنگ American Heritage نیز «Middle Dutch hame … : HAME» می‌آورد. مسیرِ وام‌گیری با داد و ستد انگلیس و فلاندر و سرازیر شدن انبوهِ واژگان کشاورزیِ سرزمین‌های پست به گویش‌های خاورِ انگلستان در سده‌های ۱۳ و ۱۴ می‌خواند؛ واژه تقریباً همیشه جمع (hames) به کار می‌رود، همان صورتی که مان نقل کرده است. تنها مخالف، کلاین است که hame را ارثی از انگلیسی کهنِ hama «پوشش، پوست» می‌داند و صورت‌های هلندی را تنها «مرتبط» می‌شمارد؛ اما این اختلاف میان «ارث» و «وام» در درونِ یک خانوادهٔ واژگانیِ ژرمنی است و پیکانِ نمودار را باطل نمی‌کند. معنی «بخشی از یراق» درست است؛ داوریِ این گره به پیکان هلندی ← انگلیسی مربوط است که تأیید می‌شود، وگرنه ریشهٔ نهایی همان‌قدر نامطمئن است که در گرهٔ ۴.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/hame\",\n            \"https://en.wiktionary.org/wiki/haam\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"IEC:466\", \"status\": \"partial\", \"note\": \"IEC.txt line 6697 reads 'Du. haam: E hames \\\"horse-collar\\\"'. Mann does put the two side by side (his colon marks the comparison) but does not himself state that English borrowed from Dutch; the borrowing arrow is Nourai's addition — a correct one, but not literally in the cited page. Note also that Mann quotes the plural 'hames', the chart the singular 'hame'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein, CEDEL s.v. hame (KLN_1966.txt line 17132)\", \"stance\": \"partial\", \"note\": \"'hame, n., either of the two curved pieces lying round the collar of a horse. — ME. hame, fr. OE. hama, \\\"cover, skin\\\", rel. to MDu. hamme, Du. haam, \\\"collar of a horse\\\"' — same word-family, but inherited from Old English rather than borrowed from Dutch.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985, root tkei- and index line 'HAME tkei-'\", \"stance\": \"partial\", \"note\": \"'c. Middle Dutch hame, hame (< \\\"covering\\\"): HAME' — supports the Middle Dutch source of the English word (Nourai's arrow) while assigning it to a different PIE root.\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etymological Dictionary (SKT.txt)\", \"stance\": \"silent\", \"note\": \"grep for a headword 'hame' in the local scan returns only unrelated matches (inhame, shame); the Concise edition has no entry for the harness word.\"},\n            {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls New Standard Dictionary (FSD_vol2.txt line 67799)\", \"stance\": \"supports\", \"note\": \"the word is current in the dictionary's compounds — 'k. link, n. A link on a hame to which the pole is attached by a chain' (s.v. kidney-…) — confirming the sense 'part of a harness' but with no etymology at that place.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\nJSONEOF\npython3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-236.json > /dev/null && echo \"JSON OK\" && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 236"
}
```


### [2026-09-06T15:51:54.737Z] TOOL RESULT

```
JSON OK
nodes verified: 7/7
node verdicts: {'disputed': 2, 'plausible': 3, 'confirmed': 2}
root verdicts: {'plausible': 2}
ref checks: {'supports': 6, 'partial': 2}
books consulted: {'contradicts': 5, 'silent': 15, 'partial': 6, 'not_found': 1, 'supports': 4} | by book: {'POK': 4, 'AHD': 3, 'KLN': 3, 'BQT': 2, 'PHD': 2, 'HRN': 2, 'WLD': 2, 'LAT': 2, 'MON': 1, 'ARY': 1, 'SYN': 1, 'NYB': 1, 'CHEUNG': 1, 'SOD': 1, 'IEC': 1, 'LEW': 1, 'DOZ': 1, 'SKT': 1, 'FSD': 1}
```


## [2026-09-06T15:52:14.662Z] AGENT

Done. `data/verification/page-236.json` written; `verify_check.py 236` reports 7/7 nodes, 0 PROBLEM lines.

**Page 236 (book p. 206) — 2 entries (Kakis, Kam 1), 7 nodes; 3 redirects skipped**

- Node verdicts: confirmed 2, plausible 3, disputed 2. Root verdicts: plausible 2.
- Both roots are Mann's (IEC), verified on the exact cited pages: IEC.txt leaf 339 = printed pp. 598–599 (`Kakis, io (Kakus, os, ā, Kakina) 'spike, prong'`) and leaf 268 = pp. 466–467 (`kam- (2) 'restrain'`). Numbering caveat: Nourai's "Kam 1" is Mann's **kam- (2)**; Mann's kam- (1) is 'tire, worry'.
- Underlying standard roots: Kakis = Pokorny ḱāk-2 'branch' (IEW 523), Kam 1 = Pokorny kem-1 'press, squeeze' (IEW 555) — hence "plausible" not "confirmed" (Mann's stem-sets and narrowed glosses are his own).

Disputed:
- **Kakis #1, Persian سگک sagak 'buckle'** — Dehkhodā and Moʿin both parse it as a diminutive of سگ 'dog' (Moʿin tags it اِ.مصغّر, first sense "small dog"); no Old/Middle Iranian antecedent exists. Mann himself marks the item "(?)", which the chart drops.
- **Kam 1 #2, Greek kĕmos** — Pokorny IEW 555 explicitly ejects it: "gr. κημός (*kāmos because of Latin loanword camus) 'muzzle' is not compatible in vocalism"; Beekes/Wiktionary call it unexplained, probably Pre-Greek.

Other notes worth the owner's eye (not extraction errors):
- The book prints **kĕmos** with a breve (short e); the word has eta, long ē. Nourai's own diacritic slip, faithfully extracted.
- Latin câmus ← Greek is solid (Ernout-Meillet DELL p. 163: "Emprunt au gr. κᾰμός"). Dutch haam / English hame: Pokorny supports the 'restrain' root, but EWN, Franck-van Wijk, Klein and Watkins all prefer a 'covering' / *tkei- origin — recorded as plausible/confirmed with the split explained.
- MON:3076 checked as **partial**: the کمند entry exists in Moʿin vol. 3 with the right sense but carries no origin bracket and no etymology; the folio number is illegible in the OCR so 3076 itself is unconfirmed. Moʿin's Borhān-e Qāteʿ footnote (vol. 3, pdf p. 490) does give "پهلوی kamand، کردی komen".
- Mann's own cross-reference "WP I, 333" for Kakis is wrong — WP I 333–334 has no such root; the right page is WP I 335, which Mann cites correctly one entry earlier.

**No extraction errors**: the printed page (copied to `data/verification/sources/refs/ocr/BOOK/236.png`) matches the JSON node-for-node, including "sakulah", "kĕmos", "câmus", "haam", "hame" and the Hāfez couplet.
