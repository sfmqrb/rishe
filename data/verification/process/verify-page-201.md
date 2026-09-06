# Verification process log — verify-page-201


## [2026-09-06T14:51:35.889Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 201 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-201.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-201.json. Write /home/sfmqrb/git/rishe/data/verification/page-201.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 201` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T14:51:37.560Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T14:51:38.271Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T14:51:38.311Z] TOOL RESULT

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


## [2026-09-06T14:51:38.449Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-201.txt"
}
```


### [2026-09-06T14:51:38.485Z] TOOL RESULT

```
1	=== PDF page 201 (book page 171) ===
2	--- entry 0 ---
3	ROOT Gurdus -> redirect to Gurdos
4	--- entry 1 ---
5	ROOT Gurô -> redirect to Ger 4
6	--- entry 2 ---
7	ROOT Gurr -> redirect to Ger 4
8	--- entry 3 ---
9	ROOT [Indo-Schythian] Gŭysna : deer, stag  (refs ISS:74)
10	#1 (parent #0) [Avestan] refs=ISS:74 | gavasna : deer
11	  #2 (parent #1) [Pahlavi] refs=ISS:74; BQT:1754; UNV:56 | gw'zn, gavâzan
12	    #3 (parent #2) [Persian] refs=BQT:1754 | gavazn «گوزن» : deer
13	  #4 (parent #1) [Sogdian] refs=SOD:180 | gwzn : deer
14	--- entry 4 ---
15	ROOT [Semitic] Ğ.v.l : to take suddenly  (refs FVA:304)
16	#1 (parent #0) [Arabic] refs=FVA:304 | ğala : he took suddenly ; ğŭl : one who attacks suddenly, demon ; umme-ğîlân : "mother of demons", referring to desert bushes believed to nourish demons. ☞Umm
17	  #2 (parent #1) [Persian] refs=FVA:304; MON:4261; BQT:2023 | ğŭl «غول» : demon, large person ; ğâeleh «غائله» : difficulty ; moğîlân «مغیلان» : desert thorn bushes
18	  #3 (parent #1) [English] refs=KLN:48,655 | algol : the demon star ; ghoul : demon
19	
```


## [2026-09-06T14:51:41.356Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-201.json",
 "description": "Read source JSON for page 201"
}
```


### [2026-09-06T14:51:41.409Z] TOOL RESULT

```
{
  "pdf_page": 201,
  "book_page": 171,
  "entries": [
    {
      "root": {"name": "Gurdus", "redirect": "Gurdos"},
      "nodes": []
    },
    {
      "root": {"name": "Gurô", "redirect": "Ger 4"},
      "nodes": []
    },
    {
      "root": {"name": "Gurr", "redirect": "Ger 4"},
      "nodes": []
    },
    {
      "root": {
        "name": "Gŭysna",
        "lang": "Indo-Schythian",
        "refs": "ISS:74",
        "gloss": "deer, stag"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "ISS:74",
          "words": [
            {"translit": "gavasna", "gloss": "deer", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "ISS:74; BQT:1754; UNV:56",
          "words": [
            {"translit": "gw'zn, gavâzan", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "BQT:1754",
          "words": [
            {"translit": "gavazn", "gloss": "deer", "script": "گوزن"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 1,
          "lang": "Sogdian",
          "refs": "SOD:180",
          "words": [
            {"translit": "gwzn", "gloss": "deer", "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Ğ.v.l",
        "lang": "Semitic",
        "refs": "FVA:304",
        "gloss": "to take suddenly"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Arabic",
          "refs": "FVA:304",
          "words": [
            {"translit": "ğala", "gloss": "he took suddenly", "script": null},
            {"translit": "ğŭl", "gloss": "one who attacks suddenly, demon", "script": null},
            {"translit": "umme-ğîlân", "gloss": "\"mother of demons\", referring to desert bushes believed to nourish demons.", "see": ["Umm"], "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "FVA:304; MON:4261; BQT:2023",
          "words": [
            {"translit": "ğŭl", "gloss": "demon, large person", "script": "غول"},
            {"translit": "ğâeleh", "gloss": "difficulty", "script": "غائله"},
            {"translit": "moğîlân", "gloss": "desert thorn bushes", "script": "مغیلان"}
          ],
          "note": null,
          "quote": {
            "text": "دربیابان گر بشوق کعبه خواهی زد قدم - سرزنشها گر کند خار مغیلان غم مخور",
            "poet": "Hâfez"
          }
        },
        {
          "id": 3,
          "parent": 1,
          "lang": "English",
          "refs": "KLN:48,655",
          "words": [
            {"translit": "algol", "gloss": "the demon star", "script": null},
            {"translit": "ghoul", "gloss": "demon", "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
```


## [2026-09-06T14:51:41.793Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-06T14:51:41.844Z] TOOL RESULT

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


## [2026-09-06T14:51:47.365Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['ISS','FVA','UNV','SOD','BQT','MON','KLN','FVQ','AFA','AFM','PLA','LKT','HRN','HUB','PHD','NYB','BRT','ARY']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:600])\n    print()\n\"",
 "description": "Inspect refs metadata"
}
```


### [2026-09-06T14:51:49.026Z] TOOL RESULT

```
ISS {"title": "H. W. Bailey, Indo-Scythian Studies: Khotanese Texts VI (Prolexis to the Book of Zambasta), Cambridge 1967", "edition_found": "not found; Bailey's Dictionary of Khotan Saka (1979) downloaded as the closest substitute", "kind": "google_books_preview+archive_restricted", "url": "https://books.google.com/books?id=4upthUgWo9YC (CUP 2009 reprint, partial preview) ; HathiTrust mdp.39015034317936 (v.6, search-only) ; archive.org khotanesetexts0103bail (vols I-III only, lending)", "identifier": "dictionary-of-khotan-saka (substitute); khotanesetexts0103bail is vols I-III, lending-only", "lo

FVA {"title": "S.M. Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (dakhil), Tohi/Azadi 1368/1989", "kind": "catalog", "url": "https://openlibrary.org/works/OL4602367W (edition OL2012991M: Intisharat-i Islami 1368/1989, 582 pp)", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: no digital copy found.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: still no digital copy on any permitted platform. Library catalogues list the 1368 book under the variant title «فرهنگ ریشهٔ وام‌واژه‌های عربی (لغات عربی مستعمل در فارسی دخیل)» — reconcile with N

UNV {"title": "J. M. Unvala, King Husrav and his Boy: Pahlavi text and glossary, Paris (Geuthner) 1963 [orig. 'Der Pahlavi-Text Der König Husrav und sein Knabe', Heidelberg diss. 1917]", "edition_found": "1917 German dissertation edition (text + glossary); 1963 Paris ed. not found", "kind": "archive_djvu", "url": "https://archive.org/details/derpahlavitextde00unva", "identifier": "derpahlavitextde00unva", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/UNV.txt", "page_offset": "leaf = printed + 2 (e.g. leaf 9 = p.7); only 48 leaves. local file has \\f between leaves (0-based l

SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id=

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sou

AFA {"title": "S. Fraenkel, Die aramäischen Fremdwörter im Arabischen, Leiden 1886 (repr. Hildesheim 1962, same pagination)", "edition_found": "1886", "kind": "archive_djvu", "url": "https://archive.org/details/diearamischenfr00fraegoog", "identifier": "diearamischenfr00fraegoog (also bub_gb_SzdbAAAAQAAJ)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AFA.txt", "page_offset": "leaf = printed + 30 (e.g. leaf 38 = p.8). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",

AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/

PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 lea

LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-

NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it
```


## [2026-09-06T14:52:00.690Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"ysna\" ISS_alt_DKS.txt | head -40\necho \"=== gavazn/gavasna in BRT\"\ngrep -n -i \"gavasna\\|gav[ao]zn\\|gauuasna\" BRT.txt | head -20\necho \"=== PHD\"\ngrep -n -i \"gawazn\\|gwzn\\|gavazn\" PHD.txt PHD_mackenzie.txt | head -20\necho \"=== SOD\"\ngrep -n -i \"gwzn\\|γwzn\" SOD.txt | head -20"
}
```


### [2026-09-06T14:52:00.836Z] TOOL RESULT

```
<persisted-output>
Output too large (42.5KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/tool-results/b92377r5z.txt

Preview (first 2KB):
38:"Though in certain features Khotan Saka is more archaic than Avestan as ~an- in gyaysna- ‘sacrifice’, Avestan yasna-; ggüysna- ‘deer’, Av. gavasna-; as -zm- in rraysma, ‘rank’, Av. rasma-; as hvar- ‘eat’, Av. xvar-; as -dz- in dajs- ‘to burn’, Av. da-; in -rt- in Tumshuq Saka rorda- ‘given’, Khotan Saka koga- ‘given’, Av. -rt- but also -3-; yet Khotan Saka has transformed most intervocalic consonants (which Sogdian and Zoroastrian Pahlavi have retained), thus -p-, -b- to -v-, -t-, -d- to -y-, -h- to -g- or lost, -g- lost; -f-, --, -х- to -h-, later -#- lost (but often marked by а subscript hook), -sd- beside -d-, preverb fra- to ha-, prothesis of /- to initial vowel, frequent z-umlaut of a, d, ii, o (absent from Tumshuq Saka), loss of medial vowel as in gyasta- ‘worshipped one’, from yazata-, bidä ‘he bears’ from barati, ysidaa- ‘yellow’? from zaritaka- ; genitive plural -йпи, -ãni, later -@т, -; suffix -atáti-, to -ttd, -da, oblique -tte, -de; -йтаіа, to -àma, and in latest texts loss of nasal before the medial consonants -k-, -g-, -d-, -b-. At times several older Iranian forms coalesce in Khotan Saka. The convenience іп the older texts of using doubled sé and уу for the unvoiced consonant and the single £ and у for the voiced is not consistently employed, the one text may often have both doubled and single consonant.
376:adamgya- ' not taming, repressing’, V 117, 66vr uysnaurānu adamgya, BS anigraha-, to dam-' to tame’ in dim- :danda-.
556:avajsamätä ' dishonouring', BS nigralta-, v 115, 64v4-5 u adatyünu uysnaurüpu avajsamátà hàmdt(e), u niharkä nusthurd, BS dhürmikünam са sattvánám nigraho bhavati dhruvam ‘апа of the irreligious beings there will be dishonour and harsh punishment assuredly'; v 125, 64v5-6 и datyanu avajsamete jsa u niharkäna 'through dishonouring and punishment of the religious', BS dhürmnikandm ca nigraham. See pajsama-; suffix -àtd, see arütá ' envy’, s.v. are jsa.
...
</persisted-output>
```


## [2026-09-06T14:52:05.712Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"gg[uüū]ysna\" ISS_alt_DKS.txt | head -20"
}
```


### [2026-09-06T14:52:05.763Z] TOOL RESULT

```
38:"Though in certain features Khotan Saka is more archaic than Avestan as ~an- in gyaysna- ‘sacrifice’, Avestan yasna-; ggüysna- ‘deer’, Av. gavasna-; as -zm- in rraysma, ‘rank’, Av. rasma-; as hvar- ‘eat’, Av. xvar-; as -dz- in dajs- ‘to burn’, Av. da-; in -rt- in Tumshuq Saka rorda- ‘given’, Khotan Saka koga- ‘given’, Av. -rt- but also -3-; yet Khotan Saka has transformed most intervocalic consonants (which Sogdian and Zoroastrian Pahlavi have retained), thus -p-, -b- to -v-, -t-, -d- to -y-, -h- to -g- or lost, -g- lost; -f-, --, -х- to -h-, later -#- lost (but often marked by а subscript hook), -sd- beside -d-, preverb fra- to ha-, prothesis of /- to initial vowel, frequent z-umlaut of a, d, ii, o (absent from Tumshuq Saka), loss of medial vowel as in gyasta- ‘worshipped one’, from yazata-, bidä ‘he bears’ from barati, ysidaa- ‘yellow’? from zaritaka- ; genitive plural -йпи, -ãni, later -@т, -; suffix -atáti-, to -ttd, -da, oblique -tte, -de; -йтаіа, to -àma, and in latest texts loss of nasal before the medial consonants -k-, -g-, -d-, -b-. At times several older Iranian forms coalesce in Khotan Saka. The convenience іп the older texts of using doubled sé and уу for the unvoiced consonant and the single £ and у for the voiced is not consistently employed, the one text may often have both doubled and single consonant.
1916:ggüysna- 'stag, deer', V 142, тзг plur. ggīys(nya, BS G 36, 506 тгвар, Tib. ri-dvags; JS 16r1 dyadic rurd guysná ' the Ruru stag’; Ш 135, 371 giysna rina “іп stag form’ (with picture of a stag); 2 13:77 samu nade dastyau gguysnd зиргйї#й rrundi nijsaste ‘the man just showed the stag in his hands to the king Suprāśśa’. For Z 2:12 ggügno Кайро
5934:renders the Jass word oras in the Jass-Latin vocabulary in the MS of 1422, Oss. D. iras). This bözah could derive from *bvauza- (without -ya- suffix) from oldest *bagauza-. For the suffix -auza-, note Oss. D. k'aboza, І. K'abuz *branch' beside DI. &'abaz (occurring also in Oss. D. dngozd, I. dnguz 'walnut') Here too may belong п 100217 bvaiysya nüvai ‘Һе received (took) the liquor’, from bveysa- with suffix -ya-. Note as support for this origin of bözah that Turkish has bor ‘wine’ from Iran. *më8 (борӣ. muwBy, mwõw), as well as bágdni and buxsum from Iranian (see for the development of Iranian *madu- *intoxicant', the Silver Jubilee volume of the Zinbun- Kagaku-kenkyusyo 1954, Kyoto University, Madu, a contribution to the history of wine, pp. 1-11). For the adjective suffix -asana- assumed in "bagazana- bvaysua-, note the similar -asna- in *gavazna- ' antelope', Khotan Зака ggüysna-, N.Pers. gavazn, Av. gavasna-.
```


## [2026-09-06T14:52:08.346Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT gavasna\"; grep -n \"gavasna\\|gauuasna\\|gavazna\" BRT.txt | head\necho \"=== PHD\"; grep -n -i \"gawazn\\|gavazn\" PHD.txt PHD_mackenzie.txt | head\necho \"=== SOD gwzn\"; grep -n \"gwzn\" SOD.txt SOD_pages.txt | head\necho \"=== HRN\"; grep -n -i \"gawazn\\|gavazn\\|gûwazn\" HRN.txt | head\necho \"=== HUB\"; grep -n -i \"gawazn\\|gavazn\" HUB.txt | head"
}
```


### [2026-09-06T14:52:08.463Z] TOOL RESULT

```
=== BRT gavasna
6598:yä  oder_>'J(?)  vll.  sva.  'es  geschieht,  kommt vor,  dass  ..':  asit'i^  yä  *ayar3Aa^a  sparr/a (sd.)  YL/0.  laöGl.;  —  asti'*''  yS gavasnaAe (sd.)  snäuya  jya  Yt  10. 1 28  Gl.  III)  als j  Praedilcatsverbnm  (Kopula).  Das  Praedikat ist  I)  ein  Substantiv,  das  mit  dem  Subjekt im  Numerus  und  Kasus,  oder  ein  Adjektiv, das  auch  im  Genus  kongruirt.  A)  I  im Ap.  (die  Kopula  folgt  dem  Praedikat): adam  bardiyä'  amiy  .  .  adam  xsäya'iiya* amiy  Bh.  b,  h;c-f*,  h-j^,  Bh.  7.5,  11,  16', -■3>  S'  55.  13-  4.2*,  D.(t.4;  —  adam xsaya%iy£^  amiy  asagartaiy  ""uvaxstraAyä laumäyä  Bh.2.  i4,4.2,Bh.g,;  —  adamsäm xsäya^iyt^  äham  Bh. /.  6;  —  ka"bujiy<^ ,  .paruvam  idä  xsäya'^iya"  ähJ^  Bh. /.  10; —  g  *duvitäiaranam  (sd.)  vayam  xsäya- üyä  amahy  Bh.  j.  4;  —  tyaiy  paruvam xsäya'iiyä  aha"  Bh.  7.  4;  —  kalä  pa- ruviyata'  hyä  amäxam  taumä  xsäya'iiyä (sd.)  äh(^  Bh.  j.  3 ;  —  adam  pärta''  amiy D.  77. 3 ;  —  martiyJ^  Ayo*  draujana'' ahatiy  Bh.^.5,  14;  14,  5;  —  Äj'u*  daustä <Ua*.  .  hyi^  arika''  äha*  Bh. /.  8;  2.4,  6, 3-  II,  5.4;  —  tyaisaiy  fratamä  martiyä anusiyä  äha"täi'>  Bh.  ;.  13;  J.  7,  8,  11,  13, /.  7;  —  negirt:  ya^ä  naiy  arika"  äham Bh..:^.  13;  13  ^  —  ty^  adam  naiy  bardiya'' amiy    Bh.  7.  13.  B  [)    im   jAwr.    (Die
10173:•  j.gavasna-  m.  -?— :  asti  (Sp,  273  o.) yS  'nahe  mäuya  jya  Yt  10. 128  Gl.
11693:•  j.  ^yä-'>,  p.  _;t)'J-»>  £  'Sehne';  a)  im Fleisch  (nur  Komp.).  b)  des  Bogens: yat..'yä{^.)  navi^yan  (sd.)  Yt/0.ii3i —  as(i  yS  gavasnahe  (sd.)  snäuya  -ya (NS.)  Yt70.  laS.
27133:•  j.  snäuya-  Adj.  (fem.  "j-J-)  'aus  einer (Tierjaehiie  gefertigt':  asti  yS  gavasnahe (sd.)  'ya  jya  Yt.  70. 128  Gl.
=== PHD
PHD.txt:379:gawazn 36 góhrig
PHD.txt:380:gawazn [gw’sn' | N ~] deer. gawdar [0011 | N ~] calf. ģāw-dumb [g'bdwmb | N —dum] horn, trumpet. ģāw-mēš [TWR Amyš | N gā(w)mēš] buffalo. £áy-, v. ģādan. Gayómart [g”ywkmlt! = Av. gayó marata | (M gyhmwrd), N ~] the First Man. gaz [gc | N ~] tamarisk. gaz-, —išn, v. gazidan. gazag [gc’k'] biting. ģāzar [g'cl | N gázur] fuller, washerman. £azdum [gcdwm | N každum!] scorpion; astr. Scorpio. £azidag [ezytk! | N gazid] poll-tax. gazidan, gaz- [gc-, gz-ytn! | N ~] bite, sting. ~išn: biting. gëg [gdk' | M gyyg] thief. gēhān [gy)?>n! | = M, N gihān, jahān] world. ~ig [-yk'] worldly, mortal. -ģēn [-k(y)n! | M -gyn, N -gin] suffix forming adjectives of quality. gês [гуз | (M gyswg, N gēsū)] curls, locks. £étig [gytyk, gytydy | M gytyg, N géti] 1. the material world; 2. worldly. ~ig [-yk'] worldly. gil [ТУМА < A tym; gl | N ~] clay. gilag [g(y)lk! | N gila] complaint, lamentation. —-Obàr [wp] swallowing complaint, suffering in silence. ģilēn [T YN Ayn! | N gilin] (made of) clay. gilistag [g/ystk!] home, dwelling of demons. gir-, ~iSnig, v. griftan. gird [git! | M gyrd, N ~] round, circular; gathered. (9) — āmadan: gather, collect (intr.). — kardan: gather, collect (tr.). ~ih: roundness. girdag [gitk' | N ~a] disk, round. gisnag [gink' | P gyfng] short, small. ģišnīz [ginyc | N —] coriander. giyā(h) [gy^h, gy^h | (M gy'w), N ~] grass. ~izag [-yck'] a straw, blade of grass. gizistag [gcystk' | J w/Bzsth] accursed, hateful. gogird [оо | M gwgyrd, N ~] sulphur. ~ӧтапа [-’wmnd] sulphurous. gohr [gwhl | M gwhr, N gauhar] substance, essence, nature; jewel; stock, lineage. goóhrag [gwhlk'] = göhr. ~-danag [-d^m k!] physicist. 1g6hrig [gwhlyk'] natural, essential. *ģūhrīg [gw(’)hlyk'] equivalent, substitute, indemnity,
PHD.txt:1530:deer gawazn.
PHD.txt:5496:gawazn gannāgīh gannag gūhr 12yohrig
PHD_mackenzie.txt:2487:gawazn                                   36                              gOhrig
PHD_mackenzie.txt:2488:gawazn [gw'Z1l 1 I N ~] deer.
PHD_mackenzie.txt:6358: deer gawazn.                               destiny breh, brehenisn.
PHD_mackenzie.txt:10864:gawazn
=== SOD gwzn
=== HRN
=== HUB
3197:— Davon zu unterscheiden np. gavaz = gavazn 'cer-
3199:afgh. LW. gavazn 'an elk\ Vgl. auch afgh. gavaz
```


## [2026-09-06T14:52:21.156Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HUB context\"; sed -n '3185,3210p' HUB.txt\necho \"=== SOD deer\"; grep -n -i \"deer\\|گوزن\" SOD_pages.txt | head -20\necho \"=== SOD wzn\"; grep -n \"wzn\" SOD_pages.txt | head -20"
}
```


### [2026-09-06T14:52:21.239Z] TOOL RESULT

```
=== HUB context
u. s. w. aus V entstanden sei. Vgl. phi. gazitan ^^
paz. gazldan *to bite, sting, gazd(u)m 'Scorpion Gl.
and Ind. 259, 265, Shk. 246. Die Etymologie ist also
falsch.
888. Np. gdv *Rind' setzt einen ap. ace. sg. gdvam, eine
analogische Neubildung fiir alteres "^gdm = zd. gqm,
skr. gam voraus, wahrend np. go-^ gav = ap. gau- der
Composita (wie Gaubruva-) oder gav- der schwachen
Casus ist. — Das angefuhrte arm. gavazan heisst
*Stab, Hirtenstab, Gerte und ist = np. gavaz ^stimulus
quo asini et boves impelluntur , zd. gavdz- *Ochsen-
stachel', skr. go-djana- *Rinder-antreibend' (sc. 'Stock').
— Davon zu unterscheiden np. gavaz = gavazn 'cer-
vus, dama*, g. go gevezm *Hirsch* ZDMG. 36, 63 ^=
afgh. LW. gavazn 'an elk\ Vgl. auch afgh. gavaz
'Gemse'. — Fiir osset. t/og lies yog. — Zu gOivmes
'Buffer = zd. *gao-ma^a- 'Kuh-widder' fiige noch die
LW. bal. gatnes^ gvamSs 'Biififer, afgh. gavmes 'a male
buffalo*.
889. Dazu arm. gah 'Thron, Sessel, Sitz, Rang, Wiirde*
(alt und haufig).
890. Np. gac 'Kalk' = phi. paz. gad Shk. 245 = arab.
Jass 'Gips', syr. ges§a erweisen anl. g als urspriinglich.
Arab. pers. jfabstn gypsum' aus gr. yvifjogj yviptvog (nicht— 91 —
umgekehrt wie Prellwitz, Etym. Wb. der griech.
Sprache meint).
=== SOD deer
15353:                   deer                                                                                                              ■>jj
16592:                                                                  deer
38002:cummin     11563                         darkness    9488, 9490, 9492           deer    4079, 4517
=== SOD wzn
4754:331 "wzn'k S                                ?.
6654: 1017 >nyrwzn     B                                                     BSTBL; GMS 335, 1273; Frag. Len. 50, 6; MSP;
6657:        =>}nxrwzn, 'xrwzn                                         1028 >nyty: B                                Jji^j^
7170: 1187 'nxrwzn   M                            £j^fe>>                     anxaz ©impf. mnxz         ^'nxst-, }nyz-, *Yz-
7171:      anxar-wazan ©ob. -yy ^nyrwzn
9693:                                                                   STi 22.19; >wzntq\ Sund. AoFiii 73; AoFviii 1971
9709:2050 \vy(h)3 B, M, S                  bW *tf(<f)                  ozan     ©Parth. >wjn\ MP >wzn\ OP ava-jan-
9804:2074 'xrwzn M                                      ^j^JCul^               oxsipd
9806:     a(n)xar-wazan =»Jnyrwzn
10334: 2265 'ywznk**' B, S         ^-*.:: jj)dj^ <Ji* <-u;1*a ijyr^t    2278 >yzt M, C                    <^J jLOU-^ <u'V *ssf
10336:      ewzang Oywznkh) =*zng                                            public place, street, square
10339:2266 'ywznk'n B                                          ju;La    2279 'yzt* C                               4J>Ojb^>
10343:2267 }ywznk,y6 B, M, S                     jU*a <jljLa            2280 'yzt'ys M                                         c-
10344:     ewzangeS Cywznky5)                                                o/izdes Oyztys) ©Parth. *zdys\ MP ^zdys
10349:2268 'ywznkh => >ywznkc,)                                         2281 'yztys =* 'yzt^s
10350:2269 'ywznkyS =» 'ywznk'yS                                        2282 'yztyskt'k M                             ,d^o-«jSc>
15347:              4079 y>wzn        B                                  jj/
15351:                   yawazn       ©Khwar. Ywzn-> Khot. gguysna-, Oss.            wound
15352:                     qwazn ©inst. -'-, gen. pi. -}n ==*ywzn                     Sund. MHC    25,26,29, 31
16509:                                                                   xwecnak, xoycnak =>xwycnJk, xwzn'q
```


## [2026-09-06T14:52:21.624Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== DKS ggüysna entry context\"; sed -n '1910,1922p' ISS_alt_DKS.txt\necho \"=== BRT gavasna entry\"; sed -n '10170,10176p' BRT.txt"
}
```


### [2026-09-06T14:52:21.692Z] TOOL RESULT

```
=== DKS ggüysna entry context
naspuste skaunde käde 'the hairs besmeared, arranged, greatly piled up’; transferred meaning, п 4441-2 cvai cimüdvà айтайййпйїп 'what we preserved among the Cimudas'. Present -/-, -Iy- from -rd-, beside participle
-Ist- from either -rst- or -rst-. From base mard- and marz-, see cognates s.v. malys-. Also gumesta-.
ggumáta- ' measured, exact, fem. ggumācã-, V 164, 21113 hajü ssumütd saüod 'wise, trained, full of plans'; JS 11У3 ша yai dasid витӣ 'you were good, skilled, trained’, parallel to BS upāya-; JS гог: vijd yai dastá gūmā 'you were the skilled trained physician’ (BS vaidya-); 11 81:52-3 pakyairma dasta u вита ‘outstanding, skilled and tained s: Manj. 283 Али cayara dasta айтай "like skilled trained magician'; K 51:6:10 bvätarrji dastá Büma “skilled trained memory’; fem. v 87, 23r1 Hū mirāhīnai hará dye ggumacai у yude si 'he saw that pearly necklace, he felt sure that... .'; Z 2:65 tut hioyo boümata balysa ggumāce yande ' he, Buddha, makes that his own knowledge sure’. From vi-mätu- 'measured in details’, beside pamata- ' measured’, Av. В ,framāta- ‘skilled in medicine”, IE Рок. 703—4m-, O.Ind. mäti, mitd-; Av. ma-; müta-, mita-, mita-, Greek pévpov, Lat. mütior, mensus, O.Engl. т: ‘measure’. With negative, see аритӣіа-, N 14831 (lost fragment to v 101, 102bz), kye vara аита,
ggumai ‘at will’, Z 3:61 ggumai barindd биўїйпа graume pharu ' at will they carry away scented garlands’; Z 20:31 ggumai barindi banhya väte rrüva mura ' at will the birds carry away the intestines to the trees’; K 23:68-9 gumai hijsara dava ‘at will the wild beasts in their haunt’, parallel to ш 96-6 mürq hayarida nva hsama āşaijvā ' the birds sport at will in the pools’, Parallel in Sogd. Bud. ryzy'n 'at wil’, rzy'm, and O.Ind. svecchayá, sva- cchandah. From vi-maya- 'to experience with pleasure’, M.Parth.T. wm'dn 'to endure’, M.Pers.T. gum'y-, gwm'yd ‘endure’, Sogd. tmt ‘ће was’, to Av. maya-, müyü-, 'good state’, humaya- 'prosperous', N.Pers. humāyūn ‘auspicious’. The form in -ai is like Лага, hárstáya “іп reality’ from *hára-ftaya-. Parallel also in Av. Vid. 2:11 (of cattle) Атат anu ustim zaosam-ca 'ac- cording to their own will and pleasure’,
ggumerāñite ' presses’ ‚2 sir ttäna ggumerüiidte klaisino bei 'thereby it (the Buddha's teaching) crushes the poison of Aleíd-affliction'. From *vi-märaya-, formed like регайа- ‘to make to rain’, to base mar- ' crush, press’. See also Aamargya- ‘alleviation’, hamurdä ‘it crushes’. For pressure as ‘touch’, note Av. Yašt 1429 afó urvaesam mārayeite ' (the kara- fish) feels the turning of the water’, Zor.P. mārtan. Oss. D. lämarun, Y. lämaryn, lämärst 'to press out; DI, 'don-marän ‘weir’ ('holding back the water’); D. yezámard, I. gizdmar ‘torture’. Iranian mar- may derive from IE either Pok. 716 mel- 'to crush’, or Pok. 735-6 mer- ‘ќо rub away'; a third mar- is in sumar- ‘to count’, below.
gumesta- ‘rubbed’, for ggumälsta-, present gumal- 'be- smear’, V 34, I4b1r khara gumesta pam(jsa?)jj] 'five groomed asses’; ibid. 4 khara si nāsti ' he takes the asses’; : plur. gāūmaistāmdīūm ' we preserved’, s.v. ggumal-.
ggüysna- 'stag, deer', V 142, тзг plur. ggīys(nya, BS G 36, 506 тгвар, Tib. ri-dvags; JS 16r1 dyadic rurd guysná ' the Ruru stag’; Ш 135, 371 giysna rina “іп stag form’ (with picture of a stag); 2 13:77 samu nade dastyau gguysnd зиргйї#й rrundi nijsaste ‘the man just showed the stag in his hands to the king Suprāśśa’. For Z 2:12 ggügno Кайро
Egumáta-— ggürasa- 87
‘deer skin’ parallel to BS ajima-, read ggüsno with -i- (*ggüvsnya-). From *gavazna-, Ay. gavasnu-, Sogd. y'wan, plur. y'wsn'n, Zor.P. gu'zn, N.Pers. ватасп, Oss. D. уййапх, plur. ydüánztd, І. qüazm, quas, qdüüaz., Possibly named from the colour gau- :gu-' reddish yellow’, see s.v. gud-, as O.Ind. harini ‘antelope’, and eta-, eni ‘kind of antelope’; nor to gau- ' bovine".
güysma 'alternative(?)', Sid. тоогу khu hvamdye Jsahera ttauda süda güysma bāta hame 'when in a man's belly there arises hot (and) cold wind alternating'. Possibly from *ava-auz- ‘to change', to Oss. D. uozun, ozun, T. йтуп, üst 'to swing, rock, stagger’; uzgd-uzgd zyory ‘ће swims swingingly'; from auz-, a variant to vas- ' to move’, see bays-.
güra- ‘grapes’, Sid. 12г2 güra, BS mrdorka, Tib. rgum; 1 171, 87vs and 1 153, 63v5 hauska gira ' dry grapes’, BS drüksü. Compound 1153, 63v5 gürütca * water of grapes’. Adjective ш 41729 ysarūm gürdmai таи ' red (or yellow) grape wine'. From *angaura-, Zor.P., N.Pers. angūr. Suyni angür8, Yidya agidro, Munjani aglero; Yidya yiro ' cluster of grapes’.
güraká ‘шуша, part of mouth', Sid. 156v1 gürakd, Tib. lčehu &hun-ba in güraká hasvame Мий üchai ' the disease of swelling of the uvula’, BS gala-fundihà (#mdaha- ‘swelling of uvula’). See güra- ‘grape’.
güraphusta- ‘abundant’ from ' thickened, thick’, as baysga- ‘thick, many’, and Armen. bazoum “thick, much, numerous’; JS 2rz güraphusta vyamjana gai vrttá anvasta tthe figurative expressions abundant, the metre itself difficult! (BS оуапјапа-, wrtti-) From  *wi-frusta- ‘thickened, inspíssated', to base frau-d-; with traject -r-, as in Aarthistà < *fra-Üraxsati, and  nrhiya- < *mi- Üraxta-, пүїїййа- ni-Üraxíaya-. Hence  *guphrusta-, *gürphusta-, to güraphusta-; contrast Ürau-d- in hara- husta- 'thrust away? *fra-ürusta- to IE Pok. 1095-6 treud-, See also phrrümd 'inspissated milk’, BS Ailafa- from base frau- or frau-d-. To be set beside the base Jrau-š- 'to thicken’ in two uses, 1. culinary, N.Pers. farüsah, áfrüfah, Armen. lw hroufak, xrousak, "Talmud. Aram. 'brwik ‘а sweetmeat made of flour, butter and honey or sugar’; 2, of milk, N.Pers. furíah, firšah, haras, *huršah ‘thick milk, biestings', Zebaki filla < *frala, Sarikoli raxé; M.Pers.T. prwig 'thickening stuff' (G. Morgenstierne NTS s, 1932, 55; W. B. Henning, BSOS 9, 1937, 86; BSOAS 11, 1946, 719). Possibly to IE Pok. 802 pel- of ‘flour, dust, chaff’, Greek тгдАто$ ‘milk pap’, Lat, pult-, nom. sing. puls ' thick pap of flour’, pulmentum ‘condiment, sauce’, puluis ' dust', O.Ind, palava- ‘chaff’.
=== BRT gavasna entry
Z-v  (?).
•  j.  gavayan-  ra.  EN.  eines  Gläubigen: 'yniid  (GS.)  asaofiS  Yt.  1$.  96.
Das  ä  des  GS.  lässt  scbliessen,  dass  der Stamm  das  possessive  an-  enthält.  Also  eig. 'der  Büffel  hat';  s.  i\.girDayi-  m. ?  —  np.  jfivin (JusTi  NB.   113)  stimmt  nicht.
•  j.gavasna-  m.  -?— :  asti  (Sp,  273  o.) yS  'nahe  mäuya  jya  Yt  10. 128  Gl.
Vll.  Name  eines  Tiers;  dann:  "es  kommt  vor, dass  die  aus  einer  Tiersehne  gefertigte  Bogen- sehne von  einem  G.  ist".
•  j.  gav-a'äayana-  Adj.  'die  Wohnstätte [  der  Rinder  bildend,  von  Rindern  bewohnt':
avi  imitt  karh-arf  yat  x^anira%3m  ..  'tum ' .  .  mi^r^  .  .  ädmäiti  Yt.  lo.  15, '  •  j.  gav-a'äitay-  f.  'Wohnstätte  der  Rin- der': avi  imai  karrvar>  yat  x''anira>:>m.. gavasayaramisA.)  'lliiica  bassatyqm  mi^rö . .  ädi'jiiiti  Yt  10. 15.
```


## [2026-09-06T14:52:31.960Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR>=15200 && NR<=15360 && /pdf page/' SOD_pages.txt | tail -5\necho \"---\"\nsed -n '15340,15360p' SOD_pages.txt"
}
```


### [2026-09-06T14:52:34.811Z] TOOL RESULT

```
---
                                                                                  gen. pi. Ydty\ f. nom. Ydy
              4078 y'wsrS M                                     , 'jfju         wound, wounding, beating
                   yaw-sar5
                                                                                S W, C2, IV 18, 53V 5, 69R24 n p52.l8; Sund.
                   year of cow, cow's year
                   Gcrsh. Sogd. Cpds. 143a                                        MHC Ydy\ p25-6

              4079 y>wzn        B                                  jj/
       M;!
                                                                          4090 ya5(ak)
                                                                               y6-' S ©ob. -y, -} ^yS'kh, yd-
                   yawazn       ©Khwar. Ywzn-> Khot. gguysna-, Oss.            wound
                     qwazn ©inst. -'-, gen. pi. -}n ==*ywzn                     Sund. MHC    25,26,29, 31
                   deer                                                                                                              ■>jj
i i-
\l                 SCE 151, 354; BSTBL, Dhy. 36; GMS 375, 1230;           4091 y$-2 B, M
II:                  Bailey. Prolexis. 74                                      yaS ©<Av. gada-, Past. Yal ©pi YS'yst
                                                                               thief
             4080 y'y B
                                                                               TSP 6.14; SCE 312; GMS 1186; Mack. BSOAS
                   xay     ©3sg. impf.     =*y-\ x'y
```


## [2026-09-06T14:52:40.503Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR<=15347 && /\\[pdf page/ {p=$0; n=NR} END{print n\": \"p}' SOD_pages.txt"
}
```


### [2026-09-06T14:52:43.074Z] TOOL RESULT

```
:
```


## [2026-09-06T14:52:46.423Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -c $'\\f' SOD_pages.txt; grep -n \"pdf page\" SOD_pages.txt | head -3\npython3 - <<'EOF'\np=open('SOD_pages.txt',encoding='utf-8',errors='replace').read()\npages=p.split('\\f')\nfor i,pg in enumerate(pages):\n    if '4079' in pg and 'wzn' in pg:\n        print('leaf index',i)\n        break\nprint('total leaves',len(pages))\nEOF"
}
```


### [2026-09-06T14:52:48.079Z] TOOL RESULT

```
642
leaf index 227
total leaves 645
```


## [2026-09-06T14:52:58.099Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\np=open('SOD_pages.txt',encoding='utf-8',errors='replace').read()\npages=p.split('\\f')\nfor i in range(222,233):\n    txt=pages[i]\n    nums=re.findall(r'(?m)^\\s*(\\d{2,4})\\s*$',txt)\n    # first entry number\n    ents=re.findall(r'\\b(\\d{4})\\s+[\\wy\\'>]',txt)\n    print(i, 'standalone:',nums[:6],'ents:',ents[:3], ents[-3:] if ents else '')\nEOF"
}
```


### [2026-09-06T14:53:00.016Z] TOOL RESULT

```
222 standalone: ['157'] ents: ['1981', '3955', '3956'] ['1299', '3968', '3980']
223 standalone: ['158'] ents: ['3991', '3981', '3992'] ['3990', '4001', '4002']
224 standalone: ['159'] ents: ['4014', '4003', '4015'] ['4024', '4013', '1981']
225 standalone: [] ents: ['4025', '4036', '4026'] ['4047', '4048', '4035']
226 standalone: ['161'] ents: ['1445', '4049', '4062'] ['4072', '4060', '4061']
227 standalone: ['162'] ents: ['4073', '4074', '4086'] ['4084', '4095', '4085']
228 standalone: ['4119'] ents: ['4096', '4097', '4109'] ['4120', '4108', '1990']
229 standalone: [] ents: ['4121', '4133', '4134'] ['4144', '4132', '4145']
230 standalone: [] ents: ['4157', '4146', '4158'] ['4167', '4156', '4168']
231 standalone: ['18'] ents: ['4180', '4181', '4169'] ['4178', '4179', '4190']
232 standalone: [] ents: ['1401', '4201', '4191'] ['4199', '1981', '4200']
```


## [2026-09-06T14:53:06.524Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\np=open('SOD_pages.txt',encoding='utf-8',errors='replace').read()\npages=p.split('\\f')\nimport re\nfor i in (244,245,246):\n    t=pages[i]\n    print('=== leaf',i, re.findall(r'(?m)^\\s*(\\d{2,4})\\s*$',t)[:5])\n    print(t[:900])\nEOF"
}
```


### [2026-09-06T14:53:08.793Z] TOOL RESULT

```
=== leaf 244 ['179']
                                                              mm        ■MM



 179
                                                                                       ^                        Ywyrsny
        f r iendiself -wished )
                                                                      57.9, 11; GMS 229, 976nl"; W-Li, ii; -w, TSP
        TSP 2.151,6.91,8.18611 pl70                                   8.69; -K MDii
4479 Yw^y Ywyst*kw M                              LiT         4491 Ywyck'w'k" -» Ywyc^w'k, xwyckWk
     xute-xwistaku =»YwtYYwstk
     friend                                                   4492 Ywyck*wy *$ Ywy^k'w'k
                                                              4493 Ywyck kryny S                                  ojcsfdjl
     Gersh. TPS 1945, 148; Hen. JRAS 1944, 138.8,                  xweck-karene
       139 fn4
                            
=== leaf 245 ['11']
                                                                                                                   11



                                                                                                                   (J*


  ywys-
       east, sunrise                                         4512 ywy z*k(w) B           >^    j->)Ji-^ «U «j*r- «*=-W^
       TSP 17.4, 16, 20, 26, 31, 3.144; Hen. JRAS 1944,
          138.20; Frag. Len. 82 a 26                              xwezak(u), x5yze ? (ywzky ) ©adv.
                                                                  very, very much, extremely
  4503 ywys- B                          o>/is^'o>/3S
                                                                  GMS 234; Bcnv. Notcsi 36-7; BSTBL; VJ; TSP;
        xwes, xoys ©<Av. xvisa—, *xwisa\ MP xwyd
                                                                    S
=== leaf 246 ['181']
  181

        Lett. 5.30; Yydfip, Hen. BBB p63.523; BSOAS                   TSP 2.494 etc.; STii 7.5, 8; BSTBL, Intox. 12, 20,
         1965, 246                                                      29; Hen. Tales. 475.14, 28; Yyr'k, SCE 394; pi.
 4525 yymr B                                       >V
                                                                        Yyr>t, SCE 260                            vyyr
      y/ximor ?                                                  4535 yyr'k »sk'r- B                o^«>*-^ ^Ixlo-*
      thin
                                                                      xere-oskar-
         TSP 6,87 n p204
                                                                      OcOmake a fool
 4526 yyn{>) B                                         O'^jj          SCE 251, 267
      y/xen ?
      conscience ?
```


## [2026-09-06T14:53:24.736Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== UNV\"; grep -n -i \"gaw[a']zn\\|gavazn\\|gw'zn\\|gōzn\\|Hirsch\" UNV.txt | head -20\necho \"=== BQT v4 گوزن\"; grep -n \"گوزن\" incoming/BQT/BQT_v4_pages.txt | head -20\necho \"=== BQT v3\"; grep -n \"گوزن\" incoming/BQT/BQT_v3_pages.txt | head -5"
}
```


### [2026-09-06T14:53:24.845Z] TOOL RESULT

```
=== UNV
=== BQT v4 گوزن
671:کهآ ترا گوزن زر کارزار , شحاك مارانراگوبند .
1551:ماه چو شاخ گوزن - کنایه از | ودرعربی بممنی اوستاد باشد ‎٩‏ .
=== BQT v3
520:ها گوزن در هوا
37787:گوزن خالهای درشت دارد و شاخ او نیز همچو
37794:که جانور شبیه بگوزن باشد ۴ - وشخصی‌راییز
37820:جانوری باشد شبیه بگوزن و او را کونه پای حم
37824:. ‏است که جالور شبیه بگوزن باشد‎
```


## [2026-09-06T14:53:29.182Z] TOOL CALL #17: Bash

```json
{
 "command": "python3 tools/ref_page.py BQT:1754 2>&1 | head -60"
}
```


### [2026-09-06T14:53:37.362Z] TOOL RESULT

```
REF: BQT:1754  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 551  OCR-lang: fas

کیز ۱ -عو۱۷-
وچیزی را نی ز کویند که بدان طلا وکقره وامثال کیس - بکر اول وسکون نانی‌وسین
آرا بهم وصل‌کنند وآ ارابمریی‌لخيم‌خوانند۱ - | بی‌قطه » چین و شکنج راگوبند ۸ - و بریی
و بزیان عرمی بمعتی مکر و حیله - و اجنکه توبره وخر بطه را خوانند ‎٩‏ .
وجدال - وحایض شدن زن باشد ۲ * کیس ر گو نه *۱ - بفتح اول وثاك

کیدپا * با بای فارسی بروزن اژدها » | ونون آخر وسکون تالی ورای قرشت وکاف‌فارسی
تلم زلی است که پادشاء بردع بوده واو را نوشابه | بواو رسیده » نام دوائی است که آنرا بیونانی
میگقتند ومعرب آن قیدافه است ۴ . فولیون و بعریی جعده کوبند . برقان سیاه را
کیرخ - با اول بثافی رسیده ورای | #اقع است *
می‌قلهٌ مقتوح بضای نقطه‌دار زده » دوتختمیان کیسنه بدا < بروزن اشکنه‌بریمانیرا
پیوسته باغد وقرآن وکنتاب.برآن نپندویسریی | کوبندکه بوقت رشتن برآدوك پیچیده شود *
رحل خوانند ؛ وباین ممتی باکاف فارسی‌هم آمده کیسو؟۱- بنتح‌اول وسکون ثانی‌وتالك
است واسح آن است ۴ ۰ بو و کشیده » بمعنی کیر کونه است وآن‌دوائی
گیرو* - بر وزن پیرو . بممنی حفظ باشد که پس‌بی جمده کویند ۰
ونگاحداشتن وحصول چیزهایی باشد که پیش از کیسه بر دوخن - کنایه از توقع
اين در هن پوشیده بوده " داشتن بافراط باشد .
کیویات ۱ - بایای حلی بروزن | کیمه بصابون‌زدن - کنایه از
میهمان » بممتی فدا وقربان باشد وآن‌بدلیاست خر ج کردن وخالی نمودن باشد .
که خود را با دیگری را بدان ازبلا پرهاشد. کیسه‌دار - بروزن ریشه دارشخسیرا
که با اول بای کشیده وبزای‌رتل,ار | کوبند که چیزها بوقت ارزالی بخرد ونگاهدارد
زده » یمعثی تمد باشد ۷ وآنرا از پم مالند ودر ایام کرانی بفروشد ۱۴ .
و جرمی لید (۱) کویند . کیسه‌صورت کشادن- بسنی‌سخ
وود و << مم<نممممم<<وهم<ح<سوسس ی
(۱) خم ۱ :کید . ۱
سس سپ سششوششررروشوشوشششش سس
۱ - «بمعتی لیم طلا و نقره یبای موحده است ۰ « رشیدی ؟ .
۴ - ر4 : منتهی‌الارب » محیط المحیط » منتخب اللغه .
۴ - ر3 : قیدافه » ورك : رشیدی . ۴ - رك :کیرخ . 8 - ظ :کیره قسی: وس.
۹ - «کیربان بای حطی بوزن میهمان » در برهان قدا وقربان » واین تصحیف است.
صحیح کربان بوزن ومعتنی قربان (است) > «سراج اللغات بنقل فرهنگه نظام اج هسم.)
۷ - رك : جهانگیری » رشیدی ۰ ۸ - اکنون نیز 5آ8 بهمین ممنی است .
‎٩‏ - (عر)«کیس بالکس کي سیم وزر .> «منتهی‌الارب» . ۰ رك :کیسو.
۱- کته رسمان بردوك پیچپهدن بود چون خایه . عنصری (بلخی) کوید :
سر که‌تاید(باید . دهخدا) کته کیسته را دور باشد بتاوه کرسته را.» «لغت فری 2۸ ۰*4
«را د وکچی وفروهه وفرموك نیز خوانند .> «رشیدی» *
۴۳ ر3 : کر کونه » ورك : فهرست مغزن‌الادویه .
۴-کفرودین را نیت در بازار مشق" کینه‌داری چون خم کیسوی تو.
سنائی غز لوی«رشیدی؟.
(برهان قاطع ۲۲۴)
```


## [2026-09-06T14:53:49.801Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\nawk 'NR<=37800 && /pdf page/{p=$0} END{print p}' BQT_v3_pages.txt\nsed -n '37770,37830p' BQT_v3_pages.txt"
}
```


### [2026-09-06T14:53:51.885Z] TOOL RESULT

```
[pdf page 514]
‏خجته « ‎ca)‏ فری ۳۹ * .

‏۰-۴ کوین ‎Keo‏ .کدی نگازران باشد حکیم ‎Rese‏ گت :

‏وانگهی ‎Wass‏ کا زری سازد زتو.

‎. ‏کوتوال‎ : By -۴

‏شوید و کوید ترا در ز سکوین‌زرنگ.»
‎cal >‏ فری ۷۰۳۸۹ *.

‏۵ کوید ان - بنم اول و فتح پنجم . _ رث :کوفتن .
[pdf page 514]
AH
8. ‏باشند‎

کوتاه ‎VY‏ - جانوری است سا
گوزن خالهای درشت دارد و شاخ او نیز همچو
شاخ کوزن شاخ شاخ میباشد و اورا ‎ES‏ پای‌هم
‎eae‏ با یی ای - و بمنی خر ‎ast‏
‏آمده است باآنکه دست خ کوش کوتاه است له
پای او .

کو تاه ‎Mh‏ بمعنی کوناء پای‌است
که جانور شبیه بگوزن باشد ۴ - وشخصی‌راییز
کویند که بیارکوتاه قد باشد .

کوتاه ‎are‏ را کرنند که
از عواقب امور نیندیشد و ‎cle‏ اندیش نباشد
وغافل و صاحب غفلت ‎ath‏ - و بخیل و مك
دا یز گنه و کون نظرحم میگوشد :

‎is‏ ه بفتح اول و ثالث » بمعنی
کبوتر باشد و عربان حمام گوند ‎ny!‏ اول
هم کفته‌اند .

‎hase

‎AIS‏ ۴ « بروزن هوشنگهبسنی
کدنك است . وآن چوبی باشد ک هکازران ‎he‏
‏جامه را کوبند یمنی دقاقی کتند و آبرا کوتنك
گازر هم میگویند وبمربی مدقه خوانند.

‏کو توال ه - با واو بروزن لوت‌ال»
نکه ‎tats‏ قلمه و شپر باشد و او را سر
هم میگویند و بعضی کوند اين ‎cad‏ هتدیياست
و فارسیان استعمال کرده‌اند چه کوت بهندی ‎sell‏
‏است .

‏کو ته ‎oe TY‏ مخنف کوتامیا است‌وآن
جانوری باشد شبیه بگوزن و او را کونه پای حم
‎a‏ - وخر کوش را نیز کفتماند .

‎wel tS ‏پاچه ۲ - مخنف‎ OS
. ‏است که جالور شبیه بگوزن باشد‎

‎onl hl = Jb is‏ بروز نكوچك
سال » بممنی ‎wh‏ باشد چه بال بمعتی قد
وقامت هم آمده است . گونند ‎Sop‏ لز چزایر

‏۱ - رك : کوته‌پا , کوناه باچه , کونه پاچه .
```


## [2026-09-06T14:54:01.854Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\ngrep -n \"کوزن\\|گوزن\" BQT_v3_pages.txt | sed -n '1,60p'"
}
```


### [2026-09-06T14:54:01.910Z] TOOL RESULT

```
520:ها گوزن در هوا
3173:‏چون کوزن وچون پلنکه وچون‌شترمرغ ولبنگه.
8367:‏از سم آهوان و کوزنان شیار کرد.
37787:گوزن خالهای درشت دارد و شاخ او نیز همچو
37788:شاخ کوزن شاخ شاخ میباشد و اورا ‎ES‏ پای‌هم
37794:که جانور شبیه بگوزن باشد ۴ - وشخصی‌راییز
37820:جانوری باشد شبیه بگوزن و او را کونه پای حم
37824:. ‏است که جالور شبیه بگوزن باشد‎
47790:ک هکوساله باشد - وبچةٌ کوزن را هم گفته اند
47820:و کوزن - و پوست کوساله - و نوعیازمرغابی۴
48025:‏نقطه‌دار. مشفف گوزنست ک هکاو کوهی‌باشد ۸ -
48044:‎» ۱۰۱ ‏«اوتوالا‎ 806 ۰۰ ۱٩۱ ‏پهلوی 602 > تاوادیا‎ ٩ . ‏:کوزن‎ Sy A
```


## [2026-09-06T14:54:06.642Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\nawk 'NR<=48025 && /pdf page/{p=$0;n=NR} END{print n, p}' BQT_v3_pages.txt\nsed -n '47990,48050p' BQT_v3_pages.txt"
}
```


### [2026-09-06T14:54:10.684Z] TOOL RESULT

```
47962 [pdf page 649]
‏قرنفل و مصطکی کند و بعربی‌اذخر وطیب‌العرب

‏(۱) خم۱: کورمور =
۱ کری (هم) و رك : گرسنه .

‏شکافنده ) .

‎. SS : ‏رك‎ - ۴

‎۸۵

‏خوانند 9 .
گو ز ‎cole‏ - ماستی راگونند که از
شیر کورخر باشد - و ماستی هم هست که صحرا
شینان سازند وآن ماست چکیده‌ایست که شبر
خام درآن داخل کنند و برهم زنند وخورند.
گودن ۱ - منم ‎Jl‏ و ثانی مجعول

‏وقتح ثالث وسکون نون ۰ بممنی‌حلقه زدن مردم

‏باشد ؛ و ‎gare‏ کویند ‎inh‏ معتی ‎SN TF‏

‏گور ‎pl‏ = بکر ‎eit‏ و فتح نون
و فا و سکون سین بی‌تقطه ‎Sab,‏ تن وبدن
آدمی است .

‏گوره - ‎ttt Jo! ate‏ نامقبیله‌ایست
در ملك هندوستان .

‏گوری ‎eee‏ اول پر وزن حوری ۰
بمعنی‌عشرت ونشاط وبمثرت ونشاط ‎yy‏ باشد-
و دویدن پمانندگورخر را هم گفته‌اند 5

‎ce = IF‏ اول و ثانی و سکون زای

‏نقطه‌دار. مشفف گوزنست ک هکاو کوهی‌باشد ۸ -
و بسکون ثانی » کردکان راکویند و معرب آن
جوز است ‎٩‏ — و ‎gin‏ اول هم بععنی ‎ATS‏
‏وهم بادی راکویند که با صدا از ‎aT pce ly‏
— و بدرا نیز کفته‌اند 9۶ که در مقابل تيك است

‏چه ه رکاه کوبند : « با نفزان فزی وبا کوزان

‏۴ - از : کور ( قبر ) ۲ شکاوته ( شکاونده

‏۴ - در «کورکانی ‎GEL‏ تازی توضیح داده شده .
© - کورکیاه ( ‎Andropogone‏ فر ) با کاء &«

‏از کندمیان صنمتی » از ‎OME Lee‏ » که خوشه‌های معطر دارد ‎IS?‏ کلاب ص ۲۹۷ >.
۷ - ترکی است . در جفتایی کوران ۰ کورن حلفه‌ای که لشکری در کرد چیزی‌تشکیل

‏دهد » توعی اردوی ‎Kin‏ بندی شده , که پوسیلةٌ گردونههابی که بشکل دایره تنظیم کنند
« جفتایی 41۸ . ۲ - از : کور (کورخر)-!-ی ( حاصل مصدر » اسم معنی) .

‎» ۱۰۱ ‏«اوتوالا‎ 806 ۰۰ ۱٩۱ ‏پهلوی 602 > تاوادیا‎ ٩ . ‏:کوزن‎ Sy A
‏طبری 8002 , مازسرانی کنونی 02[ « واژه نامه‎ ۰۰ ۳۹۹ ye ‏کردی 802 . ع12"نا8 « ژابا‎
) Juglans regia ‏جوز ؛ ص ( با‎ oT ‏شپمیرزادی 2لا36 , معرب‎ « 2002 AS. * ۱
) ‏قی : کردی 802 ( شیطان » شرور » بد‎ te . ‏تابتی ۰۱۷۹ ۲۱۰ * رك :کردو‎ «
. ‏«ژابا ص ۳۹۹ ؛ استممال مجازی است از معنی قبلی‎
[pdf page 650]
—N\aor—
```


## [2026-09-06T14:54:33.629Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\npython3 - <<'EOF'\nimport re\nt=open('BQT_v3_pages.txt',encoding='utf-8',errors='replace').read()\n# split by pdf page markers\nparts=re.split(r'\\[pdf page (\\d+)\\]', t)\npages={}\nfor i in range(1,len(parts),2):\n    pages.setdefault(int(parts[i]),'')\n    pages[int(parts[i])]+=parts[i+1]\nfor p in range(648,656):\n    print('=== pdf',p)\n    print(pages.get(p,'')[:1500])\nEOF"
}
```


### [2026-09-06T14:54:36.090Z] TOOL RESULT

```
=== pdf 648

۱۸۵۱

حمارالوحش خوانند ۱ . گوبند نگاه کردن بر
چم ارقوت چشم افزاید وصحت چشم‌رانگاهدارد
و منم ترول‌آن کند - و لقب پادشاهی هم ‎op‏
‏از ساسالی که او را بهرام ور میگفتند ۴ -
و بمعنی شراب و عش و عشرت هم بنظر آمده
‎on)‏

گور اب ‎Le‏ نای مجهول بر وزن

شوراب , نام شهری است که از مروشاه جان تا

با نجاچپارده روژ راء ‎col‏ -ومیدالیرا نیز گوبند
که بجهت اسب دوالی ساخته باشند - وگندی
که برسر قبرها میسازند ۴ - وچاقشور(۱) ‎SL‏
‏کوتاء یشمیرا یز کفته‌اند که بجهت دفع سرما
۳

درزیر موزه یوشند ومعرب‌آن جوراب است ۴ -
و زمین شوره زاری باشد در صحرا که ازدوربآب
مالد وآلرا سراب میگویند :

گورابه * ‎gli‏ مجهول بر وزن
رودابه :نام موضبی است که ‎Rese‏ پمران رستم
درآنجاست ‎ -‏ وگنبدی را لي زگوبند که بر سر
قبرها سازند .

گوراگور ۱ - منم کاف فارسی بر
وزن زوراژور » بمعتی زودازود است که مبالغه‌در

(۱) خم ۱ : چاخشور .

کورخان

زودی و ‎Gale‏ و تندی و تیزی باشد .

۰ ‏بتم اول و قح تالت‎ a WI
‏کوناء پشمی باشد که درزمستان‎ GL )۱( ‏چاقشور‎
‏در زیر کفش و موزء پوشند و معرب آن جورب‎
. ‏را هم کفته‌اند‎ wast ‏است - و کفش‎

گود بامف‌قون - بکرتات ‎als,‏
‏از آن ماهبی‌باشد که بوس‌علیهالسلام را قروبرده
بود ؛ و باين معنی بجای بای ابجد نون‌هم بنظر
آمده است .

گورب ‎aay - ٩ BL‏ است که
‎als‏ ای از خاشاك ‎ey‏ سازد مانند جوراب. واز
شاخهای درخت آویزد و او را پمریی وسعه
خوانند .

گور چشم - پارچه‌ای باشد ابریشمی
که بوقت بافتن چشم کورخر برآن نقس کنند
مانند پارچه‌ای که آنرا چشم بلبل خوانند وآترا
بعربی ممیر می‌خوانند (۲) بروزن مخیر.

گودخان - با خای قطه دار بروزن
مولتان » نام پادشاه چین باشد ‎٩‏ - و بهرام کور
را هم گفته‌اند ‎ate‏

)4( چك 
=== pdf 649

گوردین » با ادالابجند بروزن‌پوستین»
بمعنی کلیم و پلای باشد - و ‎Tale‏ پشمین رأنیز
گونند .

‎wis‏ ۱ + بضم اول و سکون انی
‎ot,‏ وسین بی‌نقطه ۰ بمعتی گری است که از
کرسنگی باشد .

‏گورشکاو ‎be FG‏ انی مجهول .
شخصی را کوبند که شبها کور و قبر را بشکافد
وکفن مرده را ببد و اورا عربان تباش میگویند
بروزن ‎FB‏ .

‎SF‏ = بروزن ‎thy‏ سنگه کازری
را گویند بعنی سنگی که کازران‌جامه برآن‌زشد
وشویند +
گور کانی ۴ با کاف فارسی بروزن
مولتانی » تیماج و سختیان را کوبند ؛ و با زای
نقطه‌دار و زای فارسی هردوآمده است .

‏گور گود » با ان فارسی بروزن
مورمور (۱) ۰ پمعنی کوراکور است که زود زود
و جلد جلد بادد ۴ - و توعی از پرنده همهست
که‌آنرا خرجل میگوبند .

‏گود گیاه - کیامی است که کورخر
‎LAT‏ برغبت تام خورد . و چون بخابند ‎Bye‏
‏قرنفل و مصطکی کند و بعربی‌اذخر وطیب‌العرب

‏(۱) خم۱: کورمور =
۱ کری (هم) و رك : گرسنه .

‏شکافنده ) .

‎. SS : ‏رك‎ - ۴

‎۸۵

‏خوانند 9 .
گو ز ‎cole‏ - ماستی راگونند که از
شیر کورخر باشد - و ماستی هم هست که صحرا
شینان سازند وآن ماست چکیده‌ایست که شبر
خام درآن داخل کنند و برهم زنند وخورند.
گودن ۱ - منم ‎Jl‏ و ثانی مجعول

‏وقتح ثالث وسکون نون ۰ بممنی‌حلقه زدن مردم

‏باشد ؛ و ‎gare‏ کویند ‎inh‏ معتی ‎SN TF‏

‏گور ‎pl‏ = بکر ‎eit‏ و فتح نون
و فا و سکون سین بی‌تقطه ‎Sab,‏ تن وبدن
آدمی است .

‏گوره - ‎ttt Jo! ate‏ نامقبیله‌ایست
در ملك هندوستان .

‏گوری ‎eee‏ اول پر وزن حوری ۰
بمعنی‌عشرت ونشاط وبمثرت ونشاط ‎yy‏ باشد-
و دویدن پمانندگورخر را هم گفته‌اند 5

‎ce = IF‏ اول و ثانی و سکون زای

‏نقطه‌دار. مشفف گوزنست ک هکاو کوهی‌باشد ۸ -
و بسکون ثانی » کردکان راکویند و معرب آن
جوز است ‎٩‏ — و ‎g
=== pdf 650

—N\aor—

کوزی (۱) مراد اين باشدکه با نیکان نیکی
و بایدان بدی - و بمعتی مقل هم آمده است
و بهترین ‎oT‏ مقل ازرق است ؛ و بسنی گویند
نبات مقل است یمنی علف مقل , و مقل صمفی
است که از ‎OF‏ بهم مبرسد - وبتر کی‌فصل پابیز
باشد .
وزاب ۱ - بنتح اول بروزن‌مهتاب.
آشیرا گویند که از کوشت و برنج و نخود
و گردکان پزند .

‎AIF‏ - بنم اول و سکون آخر که
زای نقطه‌دار ‎ath‏ , نام پرنده ات خوش آواز
شبیه به بلبل .

‎PTF‏ ۲ - بنتح اول و کاف
فارسی ۰ بروزن و معنی جوزاغند است که ممرب
‎oT‏ باشد , و ‎OT‏ شغتالوبی است خشك که درون
آترا از مخز گردکان پر کرده باشند .

‎POLI‏ - با انی مجهول و بای
‎aml‏ بر وزن بوستان » پاردم چاروا را گوبند .
وان چرم یا نواری ‎ath‏ که در زیر دم ستوران
گذارند ‎(x)‏ .

‏گوزبن ۴ © بفتح ‎Jol‏ و ضم پای‌ابجد.
درخت گردکان ‎an Sl,‏ ؛ و بضم اول هم درست
‎cal‏ +
‎Jal ho * IGF‏ بر وزن اوحد ,
بمعنی جمل باشد ‎OT,‏ جالوری است که س رکین

‏(۱) خم۱: کوز .
(4) چك » چش : میشود .
۱ - از :کوز ‎THF)‏

‏جوزاغند * جوزغند .

‏۴ - از :گوز (گردو) + بن ‎Gee)‏ .

‎(Jar) Boy 0‏ مازسرانی کنونی 286080 80 دواژء نامه کج
‎GY‏ : غوزه ‎Cpe)‏ = غوژه ‎Cpe)‏ گوزه (هم.) .

‏(۷) خم۱: زنند .
(ه) خم ۱ : مهایل . چش ؛ ‎Slee‏ .

‏۴ - از :کوز (گردو ) ۲ کند ‎(aT)‏ =
۴ - ظ . از :گوز ‎Gb Cabo)‏ (پسوند حفاظت) .

‏کوز کنا

‏را کلوله کند وغلطاند و ‎oye‏ (۳) .

‏گوژده - بنم اول و فتح ‎Sb‏ توعی
ازسمغ باشد که رنکه ‎OT‏ بمرخی زند و ازبوتة
خاری حاصل شود (4) که آنرا جهودانه‌میگویند
وبعربی عنزروت خوانند ؛ و بفتح زای فارسی‌هم
آمده است - ونیز جانوری باشد شبیه بملخ که
شبپا فرباد کند ‎٩۷‏ .

‏گود شکسته = کن‌ابه از آسمان
است .

‎gb ‏بفتح اول و 
=== pdf 651

کوزکند

گویند (۱) .
‎LPS‏ - با کاف فارسی بر وزن
نوشخند ۰ سخنان لاف ‎jy,‏ ودرو غ‌را گویند.
گود ‎CAP‏ - بنتح ال . بیخ کیاهی
است که در نظر چنان ‎UF Sauls‏ پنج شش
‎ast‏ کندم است که برهم چسییدماند و خوردن‌آن
منم آرزوی ‎Me‏ خوردن‌کند . گویند اگر يك
‎aL”‏ ازآن را با ده رطل عمل و ‎OT Shige‏
تيك درهم آمیز ند ودرظرفی-کرده سرآلرابگیر ند
در ساعت شراب رسيدة خوشگوار کردد و ‎OT‏
‏شراب فربهی آورد و قوت باء دهد و ‎NYT‏ معرب
کرده جوزجندم (۲) خوانشد .
گون ۱ - بنتح اول و انی و سکون
ه بفتح اول و انی و سکون
‎SM‏ ونون» ‎FF‏
‏ا زگاو کوهی باشد
وشاخهایاوبشاخهای
درخت خشك ‎att‏
‏مائد . کویندآب
کوشهای چشم او
ترباق‌زهرهاست_.

(۱) خم۱ : خوالند .

. ets ۱ ‏خم‎ (x)

)وا

گوده ۴ - با الی مجهول بروزن‌روزه.
‎GME‏ و غوزة خشخاش ‎May igs‏ ابربشم‌وامثال
‎faa SUT‏ و با زای فارسی هم آعده است .

گوذهر ۴ = بنتح اود و کس نانی
و قتح ‎elt‏ و سکون‌ها و رای فرشت ‎fade‏ ری
و ذنب راگوبند وآن دونقطة تقاطع فلك حامل
ومابل ‎pad‏ است و معرب‌آن جوزهر باشد .

گوده مح ‎Jol gee -f‏ ومیم‌وسکرن
خای نقطمدار , غلاف گل خرما راگویند.

گوز یه * ‎pie‏ اول بروزن‌لوزینه,
حلوائی ‎SaaS,‏ از مغ زکردکان پز ند .*

‎VOL‏ - مترون است کهبچة کاو
باشد - و بمعنی شتربچه و ‎SD‏ بچه و هر چیز
که‌آن کوچك و خورد سال ۷ ‎ath‏ هم‌هست چه
کوبمعنی‌خرد و کوچك‌نیز آمد» است۸ ؛ و کاهی
بطریق کنانه بجوانان بسمقل ‎Jol‏ عمرهم استعمال

‎(EUS OL gr‏ - کنابه از بیج
تور اس ت که برج دویم باشد از جملة دوازده‌برج

‏(۲) چش : - فلك ()

‏۱ - پپلوی 88722700 > اونوالا ۸۷ » ؛ ‎oF‏ معمولی جانوری است از ‎Bal gle‏ پر
شاخان از شخوار کنندکان ۰ که در جنگلپا زست کند . شاخهای ‎OT‏ هرسال می‌افتد
=== pdf 652

و۱۸۵ کوشلسب

فلك ‎#.(y)‏ است که مو کل ‎col‏ برمهمات‌خلوعالم ۴ . ول

گوسپند کشان - بنم کان ,روز | دوز چهاردهمازهرماه شمسی باشد وفارسیان درین
‎we‏ قربارا گویند ۷ . روزجشن کنند وعدسازند وآن‌را سیرسو رکویند

گوست ه بر وزن ‎on‏ کوفتگی ودرین روزسیربرادر ‎Shy‏ خوراد و گوشت رابا گیاء
کوفه‌شدسرا کویند؟ - وبسسنی کوی‌هر وت ی | و علف پزند نه با چوب وهیزم ‏ و گویش این
‎Hl‏ بز رکه باشد ۴ . ‎cols‏ امان یافتن از مس ‎Lay‏ جن است وبدان
‎os‏ دوای ‎yal pl‏ کنند که منسوب بجن‌است» ودرین

گوش ‎te‏ نی روزليك است فرزند بمکتب دادن وپیشه آموختن
ات ‎ARE‏ | تسش رتست
و بسن کنج )0 ‎“ES,‏ - و ‎tee‏ حفظ و ‎chiles‏ هم هسته .
همآمدماست- ونام‌فرشته‌ای ‎GS‏ گوشاسب ۱ - بنم اول و تالك بالف
(۱) چش : فلکی . ‎(x)‏ چش :کج ()
۱ - رك : التفپیم پیرونی س ۲۵۲ . ؟ - اسح « کوست» (ه.م.) است .

۴- اوستا - 88052 « بارتولمه ‎۶۸٩‏ > پهلوی ‎ns > BOSH‏ رکه ص ۸۳ >»پارسی
پاستان - ‎gausha‏ , هندی ‎ghosha - ott‏ ( صدا ) , کردی 80 ‎ghvagh gust.‏ ,
| 8005 » 405 . بلوچی ‎gdsh‏ , وخی ‎ghish . ghiish‏ « اسعق ۰۹:۳ .

۴ - اوستا ‎goush‏ » پپلوی ‎gush‏ ( لفة بمعنی کاو [ه.م.]) ‎ee‏ فرشتة نگهبان
چپارپایانست . لگهبانی روز چهاردهم هرماء با اين فرشته است . بقول بیرولی در < گوش روز ©
ازدیماء جشنی بوده است موسوم به « شیرسور * که درین روز سیر وشراب میخوردند و برای‌دقع
‎cle je Oke vl‏ ویژه با گوشت می‌پختند. زرتشتیان ‎pl‏ نیزاین روزرا « کوش» نامند.بیرولی
‎TH‏ جوش > ( معرب گوش ) و در سفدی « غش * و در خوارزمي « غوشت * آورده :

کوش روز ای تکار مشکین خال ‎59S‏ بربط بگیر و ليك بمال .
منود ‎ane‏ . ص ‎٩٩۲‏ >
‎Hy‏ : روزشماری بقلم لگارنده ی ۹-۳۲ کوش داشتن . ‎OS 
=== pdf 653

کوش افتادن
کنیده و ببین بی‌قطه و بای فارسی زده؛بسعنی
خواب دیدن باشد که عربان ‎BSUS‏ سوبمعنی
احتلام و شیطالی شدن هم هست - وجوالیرا نیز
گویند که حنوز خطش ندمیده باشد .

گوش افقادن ‎ate‏ از کر شدن
و ناشنودن گوش باشد .

گوشان - با ‎gh‏ مجهول بر وزن
جوشان » عیر و فشردة انگور را گویند .

گوشانه ۱ بروزن روزانه ۰ ‎wise‏
‏کوشه و کمینگاه باشد .

گوش آوای ‎Ga)‏ واو بالف
کشیده بتحتالی زده . شخصی را گوبند که هرچیز
شنود خوب ‎Spd‏ وبا کیرد .

گوش در - بکر بای ابجد وفتع
دال و سکون رای بی‌نقطه (۲) » بمعت ی کوش بر
آواز است که منتظر واتظا رکش باشد .

گلوش برداستی = کنابه ازناامید
خدن و ‎abd‏ نظرکردن از ‎Meal‏ باشد ؛ و در
جای دیگریمعتیاتظار کشیدن بنظرآمده است؟.

گوش بر در داشتی - کنابه از

(۱) چك . چش : کو شآوایی .

(۷) چش : رای قرشت .

۱ و۸

اتظار کنیدن و منتظر‌بودن باشد .

‎sh Ke ft AF‏ ابجدوسکون
سین بی‌تقطه و فتح تای قرشت ۰ نام شخصی بوده
که چون اسکندرذوالقرلین متوجه شهربابل میشد
در اثنای راء بکوهی رسید بی ‎ple‏ و در دامن
آنکوه دریابی بود ‎HL Se‏ بشکار مشفول
شدند و مردیرا بافتند بزرکه جثه ودرشت اعضا
و پر موی و پهن کوش ۰ گویند پهنی کوش او
بمثابه‌ای ‎Soy‏ چرنْ خواییدی ‎FlyFF eh‏
و گوش دیگر را لحاف کردی ؛ تزد اسکندر
آوردند . تحقیق احوال او کرد و نام او رایرسید
کفت که : مرا « کوش بستر > نهادند نام ۳ .

‏گوش یچ = ‎gan‏ کوتمال است -
و پارچه‌ای را نیز گوبند که بجهت دفع سرما بر
دورس و کوش پیچند .

‏گوش پیچیده = ‎ab‏ از ‎2S‏
‏باشد - و کوش مال داده را نیز گویند .

‏گوشت ۴ - پفتح اول و ثانی وسکون
ثالث و فوقانی » نام یکی از شش ‎BT‏ موسیقی
است که (۳) ‎OT‏ نوروز و مابه وسلمك و گوشت
وشهناز و کردانیه باشد .

=== pdf 654

۷7 ویر

گوشتاب ۱ - بر ‎Sy oi‏ (6۱.
بفعنی کوش پیچ است که کوشمال وپارچه‌ای‌باشد
که بردور گوش پیچند . .

گوشتاست = بسکون سین بی شله
و بای قازسی , بمعنی احتلام و شیطالی شدن
باشد ۴ - و ‎dite‏ مرغالرا نی زگوبند .

گوشت ‎EDT‏ ۴ - بنتح ها وسکون
تون و ‎ge‏ قلابیراگوین که بدان کوشت از
درون دنگ بیرون آرند - وغلیواج ‎wil” zal,‏
که زغن باشد .

گوشت [هنگ ۴ = بائاف فارسی,
بروزن ومعن ی کوشت آهنج است که قلاب گوشت
از ‎Ka‏ برآوردن - وغلیواج باشد .

گوشت وبا * ‎eae‏ رای فرشت‌وبای
ابجد بالف کشید» , غلیواج را کوبند که زغن
باشد و گوشت ربای (۲) هم کفته‌اند با تحتالی در
آخر » و گوشد ‎ILG‏ نر ‎ILE,‏ ماده میباشد
و بسضی شش ماه گفته‌اند - و قلاییر! نیز گوبند
که کوشت را بدان از ‎Kas‏ ببرون‌آورند .

گوش ‎٩ sole‏ © باخای نقطه‌دار(۳)

بالف کشیده و فتح را وسکون‌کاف + هرچیز که

(۱) چك . چش : بونقاب.
(۳) خم ۱ : - نقطه دار .

۱ - از ‎CEG ST:‏ (تابنده (با) تاییده) .

کوتدار
بدان کوش خارند - .وجانوری را لي زگوبندبسیار
پای که بگوش مردم رود و مردم را بی‌آرام ساژد
و با باشد که هلا ‎oS‏ و آنرا هزار پا هم
میگونند .
گوش ‎ONE‏ - کنایه از ‎Bg‏

کردن و مکت لمودن - وفک رکردن و درفکر

شدن باشد .

گوشن خبه - اين لت رادرفرهنک
جپانگیری بفتح رابع و بای ابجد بمعنی کوش
خارك آ ورده که میل ‎VSM FS‏ - وجاتوربسیار
پای باشدکه بر کوش رود وآنرااگوش خرله نیز
کوبند ؛ و باین معنی بجای بای ابجد بای‌حطی
حم پنظر آعده ‎col‏ اله‌اعلم ۸ .

گوش‌خز * بفتح خا و سکون زا
هر دو نقطمدار « جالوری است که آترا هزار پا
میگویند .

گوش خز اد - بفتح رابع‌وخامس
وسکون کاف ۰ بمعتی کوش‌خز است که هزار پا
باشد .

گوش خودده ‎abe‏ از کوشمال
خورده ‎atl‏ .

گوشداد ".- 
=== pdf 655

‎nh ply‏ معنی هم هست یمنی‌دگاهدار ومحافظت

‏گوش‌داشتن- بمعنی متوجه خدن
باشد ۱ - و کنایه از دیدن و نگاهداشتن (۱)
ونگاه گردن یز(۲) هست ۲ .

‏گوش ‎OI‏ - کنابه از مخنی و حرفی
بود که ‎Kr lS‏ شنیده شده ‎ath‏ ولیزسخنی
باشدکه بشخصی بگویند تا وقتی ازاوقات ‎Koo‏
‏بکارآن شخص با دنگری (۳)آبد 5

‏گوش صرای ‎ce‏ سین بی قله
ورای فرشت(4) بالف کشیده وتحتالی‌زده, کیرا
کوبندکه هرچه بشنود لیکو فه مکند.

‏گوشك ۴ - با ‎gt‏ مجپول بر وزن
‎ley‏ دو گوشت پاره را کوبند که برسرحلقوم
آدم ی که مجرای طمام است میباشد وآنرا بعربی
لوزتان خوانند - و صاحب ملازه را نیز گویند
و او را کام فرود آمده هم میگویند - و صفیر
گوش باشدکه بعربی اذن خوانند .

‎ASF‏ کره ۴ - مانی کوش کردن
است یعتی شنید - ونگاه داشت - و ‎MG‏ کرد
و دید .

‏رو و

‏گوش کرت ‎Gy ont sen‏
داشتن - و نگاه کردن باشد .

‏و ش گشتن «کنابه از سخن‌شنیدن
و متوجه شدن ‎Pach‏ .

‏گوش ‎PIES gare OT‏
است که کن‌ابه از سخن شنیدن و متوجه شدن
باشد .

‏گوش لب - بروزن ‎Ast‏ . آنکه
خطش هنوز ندمیده باشد + .

‏گوش ماهی - ‎dae‏ میکویند
و ‎OT‏ غلاف مروارید ‎ol‏ - و پیاله ای را نیز
کویندکه از صدف سازند .

‏گوش موش ه بکسر ‎tS. att‏
است کهآترا مرزنگوش‌خوانند ۷ وآن خوشبوی
میباشد و ‎FSS OT Ey‏ موش میمالد وبعرمی
آنان‌الفار خوانشد .

‏گوش ‎ONG‏ » بکس نون . کنابه
از سخن شنیدن ومتوجه شدن باشد - و کنابه‌از
ترك دادن و وا کذاشتن هم ‎Rice‏

‏گوشوادخ ‎CUS‏ - کنابه از ساء
نو باشد که ماء يك شبه است و بعریی هلال

‏(۱) چش : - ونگاه داشتن . ‎ey)‏ ۱ : هم .
(۳) چش : - با ینگری . (4) خو ۱ : - قرفت .
۱ - ودفت کردن» مواظبت کردن : «بدانك شیطان اهل کبابررا براهی‌باطل دعوت کرد ۰
کوش دارید تا درآن ‎atts
```


## [2026-09-06T14:54:47.677Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\npython3 - <<'EOF'\nimport re\nt=open('BQT_v3_pages.txt',encoding='utf-8',errors='replace').read()\nparts=re.split(r'\\[pdf page (\\d+)\\]', t)\npages={}\nfor i in range(1,len(parts),2):\n    pages.setdefault(int(parts[i]),'')\n    pages[int(parts[i])]+=parts[i+1]\nprint(pages[651][-1800:])\nEOF"
}
```


### [2026-09-06T14:54:51.791Z] TOOL RESULT

```
ابگیر ند
در ساعت شراب رسيدة خوشگوار کردد و ‎OT‏
‏شراب فربهی آورد و قوت باء دهد و ‎NYT‏ معرب
کرده جوزجندم (۲) خوانشد .
گون ۱ - بنتح اول و انی و سکون
ه بفتح اول و انی و سکون
‎SM‏ ونون» ‎FF‏
‏ا زگاو کوهی باشد
وشاخهایاوبشاخهای
درخت خشك ‎att‏
‏مائد . کویندآب
کوشهای چشم او
ترباق‌زهرهاست_.

(۱) خم۱ : خوالند .

. ets ۱ ‏خم‎ (x)

)وا

گوده ۴ - با الی مجهول بروزن‌روزه.
‎GME‏ و غوزة خشخاش ‎May igs‏ ابربشم‌وامثال
‎faa SUT‏ و با زای فارسی هم آعده است .

گوذهر ۴ = بنتح اود و کس نانی
و قتح ‎elt‏ و سکون‌ها و رای فرشت ‎fade‏ ری
و ذنب راگوبند وآن دونقطة تقاطع فلك حامل
ومابل ‎pad‏ است و معرب‌آن جوزهر باشد .

گوده مح ‎Jol gee -f‏ ومیم‌وسکرن
خای نقطمدار , غلاف گل خرما راگویند.

گوز یه * ‎pie‏ اول بروزن‌لوزینه,
حلوائی ‎SaaS,‏ از مغ زکردکان پز ند .*

‎VOL‏ - مترون است کهبچة کاو
باشد - و بمعنی شتربچه و ‎SD‏ بچه و هر چیز
که‌آن کوچك و خورد سال ۷ ‎ath‏ هم‌هست چه
کوبمعنی‌خرد و کوچك‌نیز آمد» است۸ ؛ و کاهی
بطریق کنانه بجوانان بسمقل ‎Jol‏ عمرهم استعمال

‎(EUS OL gr‏ - کنابه از بیج
تور اس ت که برج دویم باشد از جملة دوازده‌برج

‏(۲) چش : - فلك ()

‏۱ - پپلوی 88722700 > اونوالا ۸۷ » ؛ ‎oF‏ معمولی جانوری است از ‎Bal gle‏ پر
شاخان از شخوار کنندکان ۰ که در جنگلپا زست کند . شاخهای ‎OT‏ هرسال می‌افتد و سالبسد

‎oh,‏ شاخ اضافی درمی‌آید . ركك : گوز.

‏۴ - غوزه (هم.) ‏ غوژه , ‎Ny‏ کوزغه .

‏۴ ۰( معرب ) جوزهر ‎Cpe)‏ در پندهش فصل 0 ‎ae‏ ۷ «گوزهر» و « موش پریك»

‏با سیارات مریوط ‎tb‏ شده ضد ماه و خورشید میباشند « پورداود | ‎Le‏ ج٩‏ ص ۱۹۵ ‎٩‏ .

‏۴ - از :گوژه (هم) مخ (خرما) (هم.) .

‏نبت). بهلوی ‎guctnak‏ > اونوالا ‎٩۳‏ >

‏۵ - از: کوز(کردو) (- بنه(یوند
۰ - از :کو )= کاو) +-ساله [ از : سال

‎Olay > gasile ‏[(آلء) . کردی‎ dbrlingskalb— ] JUS ‏سبت) دارای‎ aye) a+

‏۱ یز کردی 0۵8816 « ژابا س ۳4۹ > و رل : اسشق ۰۹4۱

‎. ‏خرد سل‎ - ٩

‏۸ - سحيح نیت . وکو | < گاو] («م.) ‎gine‏ مطلق‌جانوران اعلی است .

‏+ طوژ ‏ رك : کرژ.
```


## [2026-09-06T14:54:59.027Z] TOOL CALL #23: Bash

```json
{
 "command": "python3 tools/ref_page.py BQT:1854 --image 2>&1 | tail -20"
}
```


## [2026-09-06T14:55:00.620Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN ghoul\"; grep -n \"^ghoul\\|ghoul, n\\|ghul, n\\|Arab. ghul\" KLN_1966.txt KLN_1971.txt | head\necho \"=== KLN algol\"; grep -n -i \"Algol\" KLN_1966.txt KLN_1971.txt | head"
}
```


### [2026-09-06T14:55:08.172Z] TOOL RESULT

```
قرلفل و مصطکی کند و بعربی‌اذخر وطیب‌العرب | چه هرکاهکوبند : « با نغزان نغزی وبا کوزان

۱( خم۱: کورمور ۰

۹ * کری (ه.م.) و رك : گرسنه . ۴ - از :کور ( قبر )+ شکاوته ( شکاونده
شکافنده ) - ۴ - در «کورکانی » با کاف تازی توضیح داده شده .

۴ -رك : کوراکور . * - کورکیاه ( ۸80۳۲0008086 فر ) با کاه مکی.
از کندمیان صنعتی » از دستةٌ غلات , که خوشه‌های معطر دارد «کل کلاب ص ۲۹۷ *.

‎٩‏ - ترکی است . در جغتابی کوران » کورن حلقه‌ای که لشکری درگرد چیزی‌تشکیل
دهد » نوعی اردوی سنگر بندی شده » که بوسيلهٌ کردونه‌هایی که پشکل دایره تنظیم کنند
« جفتابی ۰.۶۹۸ ۷ - از :گور (کورخر)+ی ( حاصل مصدر » اسم معنی) .

‏۸ -رك :کوزن - ‎٩‏ - پهلوی 882 « تاوادیا ۱۹۱ ۰ 8060 «اوتوالا ۱*۶۱ *۰
کردی 802 . 8*12 « ژابا س ۰۳۹۹ طبری 2082 » مازسرانی کنونی 182 « واژه نامه
۱ گیلکی 2007 » شهمیرزادی 3617 » معرب آن جوز ؛ * (.]آ 76812 1081288 )
« ثابتی ۱۷۹ ۰ *۲۱ > رك : گردو - ۴ قی : کردی 802 ( شیطان » شرور , بد )
« ژابا صس ۳۹۹ > ؛ استعمال مجازی است از معنی قبلی .
```


### [2026-09-06T14:55:08.256Z] TOOL RESULT

```
=== KLN ghoul
KLN_1971.txt:102371:ghoul, n., an evil demon who robs graves and 
=== KLN algol
KLN_1971.txt:11076:Algol, n., a fixed star in the constellation Per- 
KLN_1971.txt:11081:algolagnia, algoiagny, n., the feeling of pleasure 
KLN_1971.txt:11083:ModL. algolagnia, coined by Schrenck-Notzing 
KLN_1971.txt:11091:algology, n., the study of algae. — A hybrid coin- 
KLN_1971.txt:11095:Derivatives : algolog-ical, adj., algo log -ist, n. 
KLN_1971.txt:102373:took suddenly’. Cp. Algol. 
KLN_1971.txt:133747:algolagnia. 
KLN_1971.txt:181543:phycology, n., algology. — Lit. ‘the study of 
KLN_1966.txt:2184:Algol,  n.,  a  fixed  star  in  the  constellation  Per- seus  (astron.)  —  Lit.  ‘the  Demon  Star  ,  fr.  A***  * al-ghul,  ‘the  demon’,  fr.  al-,  ‘the’,  and  ghul, ‘demon’.  See  ghoul.
KLN_1966.txt:2185:algolagnia,  algolagny,  n.,  the  feeling  of  pleasure
```


## [2026-09-06T14:55:19.218Z] TOOL CALL #25: Bash

```json
{
 "command": "python3 tools/ref_page.py BQT:1854 --image 2>&1 | head -8; ls -la data/verification/sources/refs/ocr/BQT/ 2>/dev/null | tail -5"
}
```


### [2026-09-06T14:55:20.879Z] TOOL RESULT

```
(no exact page map; using offset -1205 -> pdf page 649; check the printed number and re-run with --pdf-page if off)
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1854.png
REF: BQT:1854  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 649  OCR-lang: fas

کوردن -۱۸۲-
گوردین - باادازابید بروزن‌پوستین, | خوانند 8 .
بمعن ی کلیم و پلای باشد - و جامة پشمین رانیز گورماست - ماستی راکویند که از
کوبند . شیر کورخر باشد - و مامتی هم هست که صحرا
-rw-rw-r--  1 sfmqrb sfmqrb   1606 Sep  4 14:54 72.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb 669351 Sep  5 01:38 733.png
-rw-rw-r--  1 sfmqrb sfmqrb   1152 Sep  5 01:39 733.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb 624515 Sep  5 16:20 902.png
-rw-rw-r--  1 sfmqrb sfmqrb   1658 Sep  5 16:20 902.vision.txt
```


## [2026-09-06T14:55:26.118Z] TOOL CALL #26: Bash

```json
{
 "command": "python3 tools/ref_page.py BQT:1854 --pdf-page 651 --image 2>&1 | head -40"
}
```


### [2026-09-06T14:55:28.256Z] TOOL RESULT

```
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1854.png
REF: BQT:1854  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 649  OCR-lang: fas

کوردن -۱۸۲-
گوردین - باادازابید بروزن‌پوستین, | خوانند 8 .
بمعن ی کلیم و پلای باشد - و جامة پشمین رانیز گورماست - ماستی راکویند که از
کوبند . شیر کورخر باشد - و مامتی هم هست که صحرا
گودس ۱ - بنم اول و سکون نانی شینان سازند وآن ماست چکیده‌است که شیر
و ثالك وسین بی‌قطه ۰ بمعنی گر است که از | خام درآن داخل کنند و برهم زنند وخورند.
کرسنگی باشد . گودن ؟ - بم اول وانانی مجعول
"گورشکاونه ؟ « با ای مجهول : ,وفتح ثالك وسکون نون » بمعنی‌حلقه زدن مردم
شخصی را کوبند که شبهپا کور و قبر را بشکافد باشد ؛ و بسی کویند باین معنی ترکی است.
و کفن مرده را ببرد و اورا عربان تباش میگوبند گور نفس - بکر نالك و فتح نون
بروزن نقاش . و فا و سکون سین بی‌تقطه .کنایه از تن وبدن
گودل - بروزن بوبك, سنکه‌کازری ۱ آدمی است .
را گوبند بعنی سنگی که کازران‌جامه برآن‌زاند گوره - بفتح اول‌وئالت, نام‌قبیله‌است
وشوند . در ملك هندوستان .
ور کانی ۴ - با کاف فارسی بروزن گوری - بم اول بر وزن حوری .
مولتانی , تیماج و سختیان راکویند ؛ و با زای بمعنی‌عشرت ونشاط وبعشرت ونشاط ارفتن باشد-
نقطه‌دار و زای فارسی هردوآمده است . و دوبدن بمانندکورخر را هم کفته‌اند ۷ .
گور گود - با کان فارسی بروزن | . کون - بفتح اول واثانی و سکون زای
مورمور (۱) » بمعنی کوراکور است که زود زود | نقطه‌دار» مخفف کوزنست که کاو کوهی باشد ۸ -
و جلد جلد باشد ۴ - و نوعی از پرنده هم‌هست. | و بسکون نانی »گردکان راگوبند و معرب آن
که‌آنرا خرجل میگویند . جوز است ‎٩‏ - و جم اول هم بمعن ی کر دکان
گمور گیاه - گیاهی است که کورخر ۲ وهم بادی راکویند که با صدا از راء پایین‌برآید
آنرا برغبت تمام خورد » و چون بخایند مزء | - و بدرا نیز گفته‌اند *۱ که در مقابل نيك است
قرلفل و مصطکی کند و بعربی‌اذخر وطیب‌العرب | چه هرکاهکوبند : « با نغزان نغزی وبا کوزان

۱( خم۱: کورمور ۰

۹ * کری (ه.م.) و رك : گرسنه . ۴ - از :کور ( قبر )+ شکاوته ( شکاونده
شکافنده ) - ۴ - در «کورکانی » با کاف تازی توضیح داده شده .

۴ -رك : کوراکور . * - کورکیاه ( ۸80۳۲0008086 فر ) با کاه مکی.
از کندمیان صنعتی » از دستةٌ غلات , که خوشه‌های معطر دارد «کل کلاب ص ۲۹۷ *.

‎٩‏ - ترکی است . در جغتابی کوران » کورن حلقه‌ای که لشکری درگرد چیزی‌تشکیل
دهد » نوعی اردوی سنگر بندی شده » که بوسيلهٌ کردونه‌هایی که پشکل دایره تنظیم کنند
« جفتابی ۰.۶۹۸ ۷ - از :گور (کورخر)+ی ( حاصل مصدر » اسم معنی) .
```


## [2026-09-06T14:55:36.376Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npdftoppm -f 651 -l 651 -r 200 -png -singlefile data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bqt1854 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


### [2026-09-06T14:55:38.944Z] TOOL RESULT

```
total 500
drwx------ 2 sfmqrb sfmqrb   4096 Sep  6 10:55 .
drwx------ 4 sfmqrb sfmqrb   4096 Sep  6 10:51 ..
-rw-rw-r-- 1 sfmqrb sfmqrb    264 Sep  6 10:53 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  92182 Sep  6 10:55 bqt1854.png
-rw-rw-r-- 1 sfmqrb sfmqrb  70083 Sep  6 10:52 pg204.png
-rw-rw-r-- 1 sfmqrb sfmqrb  77858 Sep  6 10:52 pg206.png
-rw-rw-r-- 1 sfmqrb sfmqrb  67371 Sep  6 10:53 pg207.png
-rw-rw-r-- 1 sfmqrb sfmqrb  59146 Sep  6 10:53 pg208.png
-rw-rw-r-- 1 sfmqrb sfmqrb 117034 Sep  6 10:54 pg215.png
```


## [2026-09-06T14:55:41.022Z] TOOL CALL #28: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bqt1854.png"
}
```


### [2026-09-06T14:55:41.052Z] TOOL RESULT

```

```


## [2026-09-06T14:55:58.471Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nmkdir -p ocr/BOOK\nsed -n '102365,102380p' KLN_1971.txt\necho \"=== 1966 ghoul\"; grep -n \"ghoul\" KLN_1966.txt | head"
}
```


## [2026-09-06T14:55:59.825Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== UNV gwzn\"; grep -n -i \"gaw\\|gav\" UNV.txt | head -20\necho \"=== UNV leaves\"; python3 -c \"\nt=open('UNV.txt',encoding='utf-8',errors='replace').read(); print(len(t.split(chr(12))))\""
}
```


### [2026-09-06T14:56:00.347Z] TOOL RESULT

```
geis-ka-fullr , ‘terrible*. Cp. aghast, ghastly. Cp. 
also the second element in Zeitgeist, 
ghostly, adj. — ME. gostly , fr. OE. gastlic , ‘spir- 
itual’. See ghastly. 

Derivatives: ghost-li-ly , adv., ghost-li-ness , n, 
ghoul, n., an evil demon who robs graves and 
feeds on the dead. — Arab, ghiil, fr. ghdla, ‘he 
took suddenly’. Cp. Algol. 

Derivatives: ghoul-ish , adj., ghoul-ish-ly , adv. 
ghurry, n., clepsydra, clock, watch, space of time, 
hour {India). — Hind, ghari, fr. OI. ghafika, 
‘water jar, pot’ (serving as a water clock), fr. 
ghafah, of s.m., which is of uncertain origin, 
ghyll, n., a ravine. — AN. Engl, dialectal var. 
=== 1966 ghoul
2184:Algol,  n.,  a  fixed  star  in  the  constellation  Per- seus  (astron.)  —  Lit.  ‘the  Demon  Star  ,  fr.  A***  * al-ghul,  ‘the  demon’,  fr.  al-,  ‘the’,  and  ghul, ‘demon’.  See  ghoul.
16106:Derivatives:  ghost-li-ly,  adv.,  ghost-li-ness,  n. ghoul,  n.,  an  evil  demon  who  robs  graves  and feeds  on  the  dead.  —  Arab,  ghul,  fr.  ghdla,  ‘he took  suddenly’.  Cp.  Algol.
16107:Derivatives:  ghoul-ish,  adj.,  ghoul-ish-ly,  adv. ghurry,  n.,  clepsydra,  clock,  watch,  space  of  time, hour  {India).  —  Hind,  ghari,  fr.  OI.  ghafika, ‘water  jar,  pot’  (serving  as  a  water  clock),  fr. ghafah,  of  s.m.,  which  is  of  uncertain  origin, ghyll,  n.,  a  ravine.  —  AN.  Engl,  dialectal  var. of  gill,  ‘ravine’;  introduced  into  English  by  the English  poet  William  Wordsworth  (1770-1850). giant,  n.  —  ME.  geant,  fr.  OF.  geant  (F.  geant), fr.  earlier  jaiant,  fr.  VL.  *gagantem,  acc.  of *gagas,  assimilated  vr.  L.  gigas,  ‘a  giant’,  fr. Gk.  ytya q,  ‘a  giant’,  fr.  I’tyat;,  'any  of  the  sons of  the  Earth  and  Tartarus’,  which  is  prob.  a pre-Hellenic  word.  Cp.  gigantic.
```


### [2026-09-06T14:56:02.052Z] TOOL RESULT

```
=== UNV gwzn
115:Hss. :  Handschriften. jAw. :  jungAwestisch.
420:u  varäz  n  gaväzan  n  gor  u  gäv  30.
=== UNV leaves
48
```


## [2026-09-06T14:56:13.608Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nfor kw in ['Algol,  n.,  a  fixed','ghoul,  n.,  an  evil']:\n    i=t.find(kw)\n    leaf=t.count('\\f',0,i)\n    print(kw[:12],'leaf',leaf)\n    # look for page numbers near\n    seg=t[max(0,i-3000):i+500]\n    print(re.findall(r'(?m)^\\s*(\\d{2,4})\\s*$',seg)[-6:])\nEOF\necho \"=== UNV leaf for gavazan\"\npython3 - <<'EOF'\nt=open('UNV.txt',encoding='utf-8',errors='replace').read()\ni=t.find('gaväzan')\nprint('leaf',t.count('\\f',0,i))\nprint(t[i-1500:i+300])\nEOF"
}
```


### [2026-09-06T14:56:15.522Z] TOOL RESULT

```
Algol,  n.,  leaf 37
['49']
ghoul,  n.,  leaf 353
[]
=== UNV leaf for gavazan
leaf 24
t  Umstellnng  der  ersten  beiden  Zeichen.  —  ^  Hss. 3-"-^3.  —  ^  Der  erste  Teil  unleserlich;  er  bezeichnet  wohl  eine  Art  ölliefernder  Frucht oder  Samen.  —  ^  Piss.  ^  Ergänzt  nach  §35,  40.  nsw.,  für  den  Zusammen¬
hang  imentb ehrlich.  —  ®  Hss.  —  '  Hss.  »3-",  das  AA^ort  ist  nur  halb  abgeschrieben. —  *  Fehlt  in  den  Hss.
«-  8.  Xo.  3.  —  ^  Der  erste  Teil  des  AA^orts  —  s.  auch  §  51  —  ist  mit  ai.  srda- Spieß,  Bratspieß’ zu  vergleichen.  Der  Ansgang  -ficak  aber  bhnbt  unklar.  Ob  -Jcol'?
21
[j]  8^  [-jj  10  ^  ^
[i]  an  x^as  [i]  murv  i  an  hac  brisian x’^astar  an  pnU  hac  u  x^astar  puU  hac
0  ))-^V  "^=1  J
.nazdisttar  dumb  ö  i
5'e)  -^ey  r  V
rast  pa  tis  pasandlt  mh-sähän  27.
o  ^
.  däU
^  ‘üü  Te"-^cj  ta
an  hac  :1m  pursit  framäyet  siftkar  28.
o  ^  -*(3^^  ^))9eyr  uo  -»
.  x^astar  katäm  i  göst  nihand  aivsart  pa  i
V  ^))yü  ‘üü  3^^  r^i
and  en  bavet  anösak  :1m  reiak  götvet  29.
o  3n  >  y*^
.  neivak  u  x^as  göst  liamäk
sem  feinen  Vogel  ist  das  vom ßtieken  das  Feinste,  und  vom Rüeken  [wieder]  ist  das  Fein¬ ste,  was  dem  Schwanz  am nächsten  ist/
27.  Der  König  der  Kö¬ nige  stimmte  zu  und  erklärte es  für  richtig.
28.  Drittens  geruht  er  zu fragen:  ‘Von  dem,  was  man in  Sülze  legt,  welches  Fleisch ist  das  feinste?'
29.  Es  sagt  der  Knabe: ‘Möget  Ihr  unsterblich  sein! All  dies  Fleisch  ist  fein  und gut:
u  varäz  n  gaväzan  n  gor  u  gäv  30.
3>ü>  [-’]
mes-gäv  u  sälak-evak  i  ^  ^  ^  ^  p]  nstr
o  2J5'^‘3  ■*  )
.  katakik  i  link  u  kataJäk  i  gor  u
n«  fvr  ■>  V  ^  ri
aspast  pa  ke  vnsn  i  gör  apäk  be  31.
30.  Das  Rind,  und  der
Wildesel,  und  der  Bergochs, und  der  Eber,  und  das  e
```


## [2026-09-06T14:56:26.754Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i in range(348,358):\n    nums=re.findall(r'(?m)^\\s*(\\d{2,4})\\s*$',leaves[i])\n    print(i, nums[:8], leaves[i][:60].replace('\\n',' '))\nEOF"
}
```


### [2026-09-06T14:56:28.524Z] TOOL RESULT

```
348 ['644', '646']  gaud,  n.,  ornamental  bead  (hist.)  —  Prob.  fr.  L. ga
349 ['646', '647'] ��.  For  the  first element  see  geo-.  The  second  eleme
350 ['648'] t,  race’.  See genns  and  verbal  suff.  -ate  and  cp.  g
351 ['650', '651'] v.,  gentlewoman-ly,  adj.,  gentle- woman-li-ness,  n. gent
352 [] cp. georgic. Derivatives:  Georgi-an,  adj.  and  n. georget
353 ['033'] of  garash  (Qal),  gerash  (Pi'el), ‘he  drove  out,  cast 
354 []  by  the English  poet  William  Wordsworth  (1770-1850). gi
355 ['658']   ancient  Hebrew  form of  this  letter  representing  the 
356 ['659', '660'] ost’.  See  gelid  and  adj. suff.  -al  and  cp.  glace,  g
357 ['661']   ^Xteiv,  ‘to  become  warm’, yXtocpo?,  ‘warm’,  yXixtvsiv
```


## [2026-09-06T14:56:39.177Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/ref_page.py BQT:2023 2>&1 | head -50"
}
```


### [2026-09-06T14:56:47.480Z] TOOL RESULT

```
(no exact page map; using offset -1917 -> pdf page 106; check the printed number and re-run with --pdf-page if off)
REF: BQT:2023  PDF: data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf page 106  OCR-lang: fas

۳۳ نفری
مفنده ۱ - بنم اول و ثالی و سکون | ولرم که شیشه گران بکاربرندوآ ترا سنگسلیمانی
نون وفتح‌دال ابجد. کرهی وکنده‌ای(۱)راگویند گویند و یگچ ريك شهرت دارد .
که بر اندام مردم از گوشت مانند کردکان شاه .
بر ۳ مر یر مغیالز ۴ - بکسر اول وبای حطی‌وزای
میآید ؛ و بعنی گره و کندهای (۲) کوچك را رو ما نی شاگردانه است وآن
کفته‌اند که درمیان گوغت وگاهی در زیرپوست . هوزیروزن مقراآاض », بمعمی ی ست وان
: | دوسه پولی‌است که بطربق انسام بعد ازاجرت‌استاد
اسپل ماهی‌میباشد و بعریی‌غده میگوبند ؛ وبعی بشاگر, هند ؛ - اول آمده ۱ ۹
هر کره وکنده (۱) را کوبند که در بدن آدمی ً مفلا ۲ ۳ ی
بهمرسد خواه كوچك و خواه بزرکك خواه درد لك - با لام بر وزن سلیمان » نام
کند و خواه درد نکند ؛ بلکه بعنی کفته اند | درختی است خار دار و بعربی آنرا ام‌غیلان (۳)
کره وکنده (۱) و دنبلی باشد که سار درد خواش ۴ . ۱
کند ‏ مغیلان باستان « کنیه از دیا
مغنیها ؟ - باسن بی‌نقطه بالف کشیده و رو زکار است .
بروزن مه سیما » کلی باشد سیاه رنگه وآنرا از مغیلان‌گاه - با کاف فارسی بر وزن
کوه کاشان آورند و آن ,مرقدیشا مانند بود - | سلیمان جاه » بممنی مفیلان باستاست که کنایه
و بعی کوبند سنگی است الوان و بسیار ست | از دنیا باشد .
بیان نوزدهم
در میم با فا مشتمل بر چهار لغت و کنایت
مفر ج گر ان (4) فلا -» کنایه از را نی زگویند .
فرشتگان وملالکه باشد - و ستاره‌ها و کواکب مقر س* - با را وسین‌بی نقطه وح ر کت
(۱) چش: کنده . (۷) چش : کندهای. (۳) چش : مغیلان (۱)
(4) چش : مفرح کران .
۹-« مفنده , دمل بود که برتن مردم برآید . عجدی ( مروزی ) گوید:
بردار درشتی ز دل خصم بثرمی بردوستی آندر نبد ای دوست مفنده »
لغت فرص ص 4۳۳ .۰
مصراع دوم در چاپ آروپا « نزدوستی اندرآید ای دوست مفنده » وآقای دهخداآ بر چنین تصحیح
کرده‌اند : کز پیه (دتبه ( بنج ید آی دوست مفنده؛ درهرحال آین‌کلمه وشاهد محل تامل‌است.
رك : مفند , غند . غنده -
۴ - مفناسیا (عر ) ۳ 332886916 (فر) « دزی ج ۲ ص۹۰4 > مأخون از ربونانی
98 لیدل واسکات ». کید دمنیزیوم » برنگه خاکه سفید. بی‌طعم » غیر قابل حل
درآب ,که آترا بمنزلةٌ ضد اسید و مپل بکار برند . ۴ - مصدف « ففیاز » (ه.م.) -
بفیاز (ه.م.) و رك : سراج اللغات بنقل فرهنگه نظام ج ۵ ص‌ها - ۴ - رك : ناح‌المروی
ج اص ۱۹۰ «طلح» . 8 - مصحف «مقرنی» (عر). رك : سراح‌اللغات بنقل فرهنگه‌نظام
ج ۵ ص‌ما . ور3ك : عقرنی .
```


## [2026-09-06T14:56:58.737Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\npython3 - <<'EOF'\nimport re\nt=open('BQT_v4_pages.txt',encoding='utf-8',errors='replace').read()\nparts=re.split(r'\\[pdf page (\\d+)\\]', t)\npages={}\nfor i in range(1,len(parts),2):\n    pages.setdefault(int(parts[i]),'')\n    pages[int(parts[i])]+=parts[i+1]\nfor p in sorted(pages):\n    if 'مغیلان' in pages[p]:\n        print('pdf',p, re.findall(r'(?m)^\\s*([۰-۹0-9]{3,4})\\s*$',pages[p])[:4])\nEOF"
}
```


### [2026-09-06T14:57:00.273Z] TOOL RESULT

```
pdf 106 []
```


## [2026-09-06T14:57:04.871Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\npython3 - <<'EOF'\nimport re\nt=open('BQT_v4_pages.txt',encoding='utf-8',errors='replace').read()\nparts=re.split(r'\\[pdf page (\\d+)\\]', t)\npages={}\nfor i in range(1,len(parts),2):\n    pages.setdefault(int(parts[i]),'')\n    pages[int(parts[i])]+=parts[i+1]\nfor p in range(98,116):\n    nums=re.findall(r'(?m)^\\s*([۰-۹]{3,4}|[0-9]{3,4})\\s*$',pages.get(p,''))\n    print(p, nums[:5])\nEOF"
}
```


### [2026-09-06T14:57:06.645Z] TOOL RESULT

```
98 []
99 []
100 []
101 []
102 []
103 []
104 []
105 []
106 []
107 []
108 []
109 []
110 []
111 []
112 []
113 []
114 []
115 []
```


## [2026-09-06T14:57:11.689Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nS=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad\npdftoppm -f 106 -l 106 -r 150 -png -singlefile data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf $S/bqt2023 && echo ok"
}
```


### [2026-09-06T14:57:13.660Z] TOOL RESULT

```
ok
```


## [2026-09-06T14:57:15.835Z] TOOL CALL #37: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bqt2023.png"
}
```


### [2026-09-06T14:57:15.862Z] TOOL RESULT

```

```


## [2026-09-06T14:57:39.408Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== LKT ghul/algol\"; grep -n -i \"algol\\|gûl\\|ghul\\|Ghul\" LKT.txt | head -10\necho \"=== SKT ghoul\"; grep -n -i \"ghoul\\|algol\" SKT.txt | head\necho \"=== WEB\"; grep -n -i \"^ghoul\\|ghoul, n\\|Algol\" WEB_vol1.txt | head\necho \"=== FSD\"; grep -rn -i \"ghoul\" FSD_vol2.txt | head -3\necho \"=== AFA ghul\"; grep -n -i \"gul\\b\\|Ghul\" AFA.txt | head -5\necho \"=== MON مغیلان\"; grep -n \"مغیلان\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt 2>/dev/null | head -10\necho \"=== MON غول\"; grep -c \"غول\" MON_part1.txt MON_part2.txt 2>/dev/null"
}
```


### [2026-09-06T14:57:39.570Z] TOOL RESULT

```
=== LKT ghul/algol
1807:Ein  Wüstengeist,  die  Mitte  zwischen Mensch  und  Ginn  [s.  hier  Nr.  723]  hal- tend, mit  menschlicher  Gestalt  und Eselsbeinen,  doch  häufig  seine  Gestalt wechselnd  [Lammens  Farük  870] ;  hier- aus frz.  la  goule  'ein  Ungeheuer';  aus dem  ar.  plr.  gailän  ergab  sich  frz. gailan  'dass.'.  —  Gtil  ist  auch  die  Be- zeichnung der  Meduse;  räs  al-gül  'Me- dusenhaupt' wurde  wegen  des  Wechsels seiner  Lichtstärke  der  Stern  ß  Persei genannt;  hieraus  der  Sternname  Algol. [Lammens  Rem  127/128.  Ideler  Sternu 88.    Devic  DEt  18.
=== SKT ghoul
23616:flertiani  bang  (t),  barbican?,  bashitw, LT,  caravan,  caravansary',  dervia  (der- bi.  divan,  durbar,  6rman,  ghoul,  bonri, leal,  jasmine  ijetsambe),  Lascar,  mohur,
=== WEB
5466:al-go-logiic al, a. pertaining to algology; of the nature of seaweeds or algae.
5467:al-gol/6-gist, n. a specialist in, or a student of, algology.
81705:ghoul (göl), n. [Ar. gh#l, a demon of the moun- tains. s
81709:ghoul’ish, a. demoniac; fiendish; like a ghoul.
=== FSD
FSD_vol2.txt:34574:goul,  re.  A   ghoul, gou'landt,  re.  Same  as  gowan.
FSD_vol2.txt:34766:gueule,  <   L,  gula,  throat.) gowle^,  ».  [.Archaic.]  A   ghoul,  gowlt.
FSD_vol2.txt:41712:hart’ssear,  n.  A   tropk’.il  .slinili  (Caca’ia  tkinia)  of  the  Ha-raii'’»al£Ka'so}iIdl,  1   ha-ran'»al«ru'^ird ;   2   hii-r;in'«al* family  Aifi'fmcc;c,  witli  lifsliy  stems  mid  lUtm-nate  leaves:  rii'shhl.M.  I.lteralJy  "Harun  (ho  Just”  C76&-S09),  the  Calif eabbageotree;  raniatiou^irci?.— liart’s=eyet,  n.  The  dit-  of  the  Saracens:  hero  of  the  Aru&iaa  A'iffte. tany.— Uart’sdhom.jz.  Tliebuelitiioiu  {Rkiiv'.nus cathar-  Ha-ru'pliite,  1   lia-rfl'fait;  2   ha-ra'nt,  n.  Bib.  1   Citron,  sli,  5. tic'us),  naturalized  in  the  Uniujcl  States  from  Jiurope.  ha-rus'pex,  1   iia-ros'peks;  3   ha-rus'pelcs,  n.  [-pi-ces,  1   -pi- —   hapt’s«tongue,  n.  A   poiypoiliacooiis  fern  (.Scolopen-  siz;  2 -pi-ces,  p/.l Rom.  Antiq.  A   soothsayer  or  diviner ’   ■   'll  xolopendrimn),  foinul  tliroughoul  the  cooler  reKions  who  interpreted  the  will  of  the  gods  from  inspection  of  the
=== AFA ghul
2068:schon durch das Französische, das hier die reguläre Laut-
5621:ebenso N.>Ie, da sie genau die regulären VocalTcrhältnisse
6178:das reguläre Laut'lquivaleut von hebr. ^^vT als ^i-^ »flech-
6584:die es dann wie ein reguläres arabisches Wort behan-
7753:regulären Yocalentsprechung müsste man bei arab. d ara-
=== MON مغیلان
=== MON غول
MON_part1.txt:87
MON_part2.txt:90
```


## [2026-09-06T14:57:50.594Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nhead -c 400 MON_part1.txt; echo; echo \"---\"; grep -c $'\\f' MON_part1.txt MON_part2.txt; grep -n \"pdf page\" MON_part1.txt | head -2\necho \"=== LKT entry\"; sed -n '1795,1815p' LKT.txt"
}
```


### [2026-09-06T14:57:52.287Z] TOOL RESULT

```
0 
2 


چم 
نسم ی 


تمه موی موم 
3 


ماما نا موس ملاس 
روم و3 


2 
7 
س 


همجمج مد هعرج ی وه جر ج مهو موجه و وید جع مج وی ۶ج و وم مب و وج 5 
ادا ما ما زو ماه مرو ماخ( نوم شام 4و منم مخ نامه مدش نامع 

مه مر وه ود 

3 ور 133131313 


هم مشب جج جب بیج چم �
---
MON_part2.txt:0
MON_part1.txt:0
=== LKT entry
N.  pr.,  ein  tk.  Stamm,  dessen  Angehörige von  den  Almohaden  in  Marokko  und Spanien  (1 130—1269)  zu  Henkersdiensten gebraucht  wurden ;  hieraus  mit  ar.  Art. pg.  algoz,  sp.  algoce  'Henker,  Scharf- richter', sp.  pg.  algozaria  'Grausamkeit, grausame  Handlung'.  [DE  128/129. Eguilaz  182.    ML  3826  a.
736.  Ar.  gubb:
'Brunnen',  auch  mit  häufigem  Wechsel von  ti  zu  i  ar.  gihh;  hieraus  mit  ar. Art.  kat.  aljub,  anxuh  'Gefängnis',  ara- gon.  alehup  'Zisterne',  pg.  aljube  'Ge- fängnis', enxotna  'unterirdisches  Verließ' ; sp.  algibe  'Zisterne;  Gefängnis',  pg. algive  'Brunnen',  valenc.  algip,  siz. gebbia  'Zisterne'.  [DE  125.  Eguilaz 181.    ML  3950.
737.  Ar.  gubba: 'Baumwollenes  Unterkleid'  [Dozy  V6tem i07ff.\;  hieraus  mit  verschiedenartiger Bedeutungsentwicklung :  it.  giuppa  (alt), giubba  'Jacke,  Wams',  frz.  jupe,  jupon 'Frauenrock,  Unterrock',  demin.  it.  giu- betto,  gitibetta,  augm.  it.  giuppone,  siz. jippuni;  prov.  jubo,  kat.  gipö,  sp.jubön, pg.  jubäo,  gibäo,  rum.  giubca  'langes Oberkleid  der  Bauern',  ^ubea,  sp.  aljuba,
chupa;  mhd.  schuhe,  nhd.  Schnube 'Frauenrock,  Frauenmantel',  disch.Joppe. Über  das  tk.  zybun  entstand  rum.  zibun, russ.  znpan,  zipun,  bulg.  zupan,  zabun, öech.  zupan,  aber  auch  russ,.  jubka,  jupka 'Unterrock',  bulg.  jupka,  poln.  jupa, serb.  dzuhe.  [DE  147.  Eguilaz  204. GrSVociSic  239.  Kluge  219  und  386. Goijajew  117  und  432.  Bern  SlEtWb 459/460.
738.  Tk.  giigutmek:
'Versüßen,  liebkosen'  [vgl.  giigük  'süß' vom  Stamme  süz,  süc,  cic  'süß,  lieb, schön' VämberyXktEt  Wh  S.  156,  Nr.  171]; hieraus  rum.  giugiuU  'liebkosen'  und Ableitungen.
739.  ir.  gnhä:
Der  orientalische  Eulenspiegel,  in  Nord- afrika Si  Goha  [vgl.  S.  Moulieras,  Les Fourberies  de  Si  Djeha.  Paris  1892],  bei den  Türken  als  Nasr  ed-din  Hoga  [vgl. Albert  Wesselski,  Der  HodschaNasreddin. I.  II.  Weimar  1911]  bezeichnet;  hier- aus rum.  ciuhä  'Scheuche,  Popanz',  russ. coha,  cuha  'albernes  Zeug',  bulg.  serb. coha,  hieraus  verkürzt  cus,  cuz  'Un- sinn, dummes  Zeug',  it.  (dial.  siz.)  giiicco 'dumm,  Dummkopf,  giucca,  giufä  'ko- mischer Kauz'.  —  Schon  bei  den  Arabern ist  Guhä  wegen  seiner  Dummheit  sprich- wörtlich geworden  [ahmak  min  guhä 'dummer  als  G.'  in  G.  W.  Freytag, Arabum  Proverbia  I,  403.  Nr.  175]. Vgl.  FR.  SCHWALLY  in  ZDMG  LVI, 237/238  und  ARTHUR  CHRISTENSEN in  Browne  Festschr  129/136.
740.  Per^.  gul:
'Rose'  [Horn  NpEt  S.  206,  Nr.  927],  tk. gill ;  hieraus  bulg.  gul,  serb.  dzul  'Rose'.
741.  Ar.  gül:
Ein  Wüstengeist,  die  Mitte  zwischen Mensch  und  Ginn  [s.  hier  Nr.  723]  hal- tend, mit  menschlicher  Gestalt  und Eselsbeinen,  doch  häufig  seine  Gestalt wechselnd  [Lammens  Farük  870] ;  hier- aus frz.  la  goule  'ein  Ungeheuer';  aus dem  ar.  plr.  gailän  ergab  sich  frz. gailan  'dass.'.  —  Gtil  ist  auch  die  Be- zeichnung der  Meduse;  räs  al-gül  'Me- dusenhaupt' wurde  wegen  des  Wechsels seiner  Lichtstärke  der  Stern  ß  Persei genannt;  hieraus  der  Sternname  Algol. [Lammens  Rem  127/128.  Ideler  Sternu 88.    Devic  DEt  18.
742.  Pers.  guläb: 'Rosenwasser'  [aus  pers.  gul  'Rose',  s. hier  Nr.  740,  und  ab  'Wasser',  s.  hier Nr.  5],  ebenso  ar.  guläb,  vulg.  guleb; hieraus  m\2L\..  jidapium  'eine  Art  Sirup, Kühltrank',  li.giulebbe,  giulebbo,giuleppo,
59
[Hebr.  gulgolQd.
prov.  frz.  julep,  sp.  julepe,  pg.  julepo. Dagegen  in  der  uisprüngliclien  Bedeu- tung russ.  guljaf  'Hundsrose',  guljafnaja u'oda  'Rosenwasser'.  [DE  293.  Eguilaz 434.  Devic  DEt  146.  ML  395"2.  Gor- jajew  84.
743.  Hebr.  gulgöl§ö:
'Schädel',  aram.  gulgalQ-ä;  hieraus  gr. foXyoQä,  das  in  den  Evangelien  als TÖiToq  Kpaviou  'Schädelstätte'  erklärt wird;  wahrscheinlich  hieß  der  Ort  so nach  den  zahlreichen  Schädeln  der  Hin- gerichteten, da  er  die  Richtstätte  bei Jerusalem  ist.  In  der  übertragenen  Be- deutung 'Leidensstätte,  Leidensweg'  ist das  hebr.-aram.  Wort  in  alle  europä- ischen Sprachen  übergegangen :  frz.  engl. golgoiha,  dtsch.  Golgatha  usw.  [Devic DEt  130.
744.  Ar.  grnlgnläu ;
Auch  gungulän  'Sesam';  hieraus  z.  T. mit  ar.  Art.  und  mit  häutigem  Über- gange der  Vokale  ä>  e>z:  sp.  aljon- joU,  ajonjoU,  pg.  gergelim,  zirgelim,  Irz. jugeoline,  gengili.  Da  aus  dem  Samen des  Sesams  eine  rötliche  Farbe  her- gestellt wurde,  ergab  sich  noch  sp. dnzolino,  frz.  zinzolin  'rötlich-violett'. [DE  146/147.  Devic  DEt  127/128  und 230.
```


## [2026-09-06T14:58:02.271Z] TOOL CALL #40: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-06T14:58:02.277Z] TOOL RESULT

```


```


## [2026-09-06T14:58:04.478Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nS=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad\npdftoppm -f 201 -l 201 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf $S/pg201 && echo ok"
}
```


### [2026-09-06T14:58:06.624Z] TOOL RESULT

```
ok
```


## [2026-09-06T14:58:08.879Z] TOOL CALL #42: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg201.png"
}
```


### [2026-09-06T14:58:09.233Z] TOOL RESULT

```

```


## [2026-09-06T14:58:09.229Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-06T14:58:17.898Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%AF%D9%88%D8%B2%D9%86",
 "prompt": "Give the full Persian etymology section for گوزن (gavazn) 'deer': Middle Persian form, Proto-Iranian reconstruction, Avestan/Khotanese/Sogdian cognates, and any cited scholars."
}
```


## [2026-09-06T14:58:19.521Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%BA%D9%88%D9%84",
 "prompt": "Give the Arabic etymology and definitions of غول (ḡūl), including the root غ و ل and the verb غال (ḡāla), and any Persian section for غول."
}
```


### [2026-09-06T14:58:25.326Z] TOOL RESULT

```
# Persian Etymology of گوزن (gavazn)

**Middle Persian Origin:**
The word derives from Middle Persian _𐭢𐭥𐭠𐭦𐭭_ (gʿʾzn /gawazn/, "deer").

**Proto-Iranian Reconstruction:**
The etymology traces to "Proto-Iranian _\*gavasna-_ ('deer'), perhaps from a suffixed form of _\*gā́wš_ ('cow') + _\*Hajáh_ ('goat')," or alternatively from the BMAC substrate.

**Avestan Cognate:**
The entry cites the Avestan parallel _𐬔𐬀𐬎𐬎𐬀𐬯𐬥𐬀_ (gauuasna).

**Scholarly References:**
The etymology credits Gamkrelidze and Ivanov (2010) for the Proto-Iranian analysis, and Michael Witzel (2016) for the BMAC substrate theory, published in the _Journal of the Association for the Study of Language in Prehistory_.
```


### [2026-09-06T14:58:26.946Z] TOOL RESULT

```
# Arabic Etymology and Definitions of غول (ḡūl)

## Etymology 1

**Root:** غ و ل (ḡ w l), connected to the verb غال (ḡāla), meaning "to seize."

**Definitions:**
1. Ape or orangutan (obsolete)
2. "Ghoul, desert demon"
3. Demon, jinn, goblin, monster
4. Ogre, cannibal, troll, oni, giant
5. Calamity or disaster

## Etymology 2

This represents the verbal noun of غال (ḡāla), denoting "taking away, snatching, seizing, grabbing."

## Persian Section

غول in Persian (borrowed from Arabic) means:
- Ghoul
- Giant
- Monster

The word also has obsolete Persian senses referring to a penfold for cattle, twin children, and an archaic form of "ear."
```


## [2026-09-06T14:58:32.681Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/ghoul",
 "prompt": "Give the full etymology of \"ghoul\" and of \"Algol\" if present (Arabic al-ghul, ghala 'he seized', William Beckford Vathek 1786)."
}
```


## [2026-09-06T14:58:34.203Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%85%D8%BA%DB%8C%D9%84%D8%A7%D9%86",
 "prompt": "Give the Persian etymology and meaning of مغیلان (moğilān), including its relation to Arabic أم غيلان (umm ghaylān)."
}
```


### [2026-09-06T14:58:36.232Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-06T14:58:37.468Z] TOOL RESULT

```
# Etymology of Ghoul and Algol

**Ghoul** entered English in 1786 via William Beckford's orientalist novel *Vathek*. The term derives from Arabic *ghul*, meaning "an evil spirit that robs graves and feeds on corpses," which itself comes from the Arabic verb *ghala*, meaning "he seized."

**Algol**, a variable star in Perseus, carries the same Arabic root. Its name literally translates to "the Demon," from Arabic *al-ghul*. The star received this designation around the late 14th century, likely because its brightness visibly fluctuates every three days, distinguishing it from other bright stars in the constellation.

Both words showcase how Arabic terminology for supernatural beings entered English lexicon through literary and astronomical contexts.
```


## [2026-09-06T14:58:43.160Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A3%D9%85_%D8%BA%D9%8A%D9%84%D8%A7%D9%86",
 "prompt": "Give the Arabic entry for أم غيلان (umm ghaylān): meaning (acacia / thorn tree), etymology and relation to غول/غيلان."
}
```


## [2026-09-06T14:58:46.744Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D9%85%D8%BA%DB%8C%D9%84%D8%A7%D9%86/",
 "prompt": "Quote the فرهنگ معین and لغت‌نامه دهخدا entries for مغیلان — meaning and stated origin (e.g. from Arabic أم غیلان)."
}
```


### [2026-09-06T14:58:49.182Z] TOOL RESULT

```
# أم غيلان (Umm Ghaylān)

**Etymology:** The term literally means "mother of ghouls, that is the abode of ghouls," deriving from أُمّ (umm, "mother") and غيلان/غول (ghaylān/ghūl, "ghouls").

**Primary Meaning:** This Arabic noun refers to the gum arabic tree (_Vachellia nilotica_) or gum-bearing acacia (_Vachellia gummifera_), plants native to desert regions with characteristic thorny characteristics.

**Linguistic Connection:** The word combines the root أم with غيلان, where غيلان functions as a plural or related form of غول. The poetic or metaphorical naming—calling an acacia tree the "mother of ghouls"—reflects traditional Arabic nomenclature for desert plants.

**Historical Usage:** A 13th-century source describes it as "a spiky shrub of the desert, of many thorns," noting traditional medicinal and aromatic applications in Nubian contexts.
```


### [2026-09-06T14:58:53.294Z] TOOL RESULT

```
# مغیلان - Dictionary Entries

## فرهنگ معین (Farhang-e Moein)
**Quote:** "(مُ) [ع.] (اِ.) امُ غیلان، درختچة خاردار که در بیابان ها می روید."

**Translation:** A thorny shrub found in deserts, derived from Arabic أم غیلان.

## لغت‌نامه دهخدا (Dehkhoda Dictionary)
**Quote:** "مأخوذ از تازی، درختی خاردار که در مصر و عربستان فراوان"

**Translation:** Sourced from Arabic, this is a thorny tree abundant in Egypt and Arabia. The entry notes the original Arabic form أم غیلان means "mother of demons" (أم = mother; غیلان = plural of ghoul), as ancients believed desert demons sheltered beneath such shrubs to mislead travelers.
```


## [2026-09-06T14:59:00.104Z] TOOL CALL #49: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%BA%D8%A7%D8%A6%D9%84%D9%87/",
 "prompt": "Quote the فرهنگ معین and دهخدا entries for غائله — meaning and origin (Arabic)."
}
```


## [2026-09-06T14:59:01.399Z] TOOL CALL #50: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/gawasna",
 "prompt": "Does this reconstruction page exist? Give the Proto-Iranian reconstruction for 'deer' and its descendants (Avestan, Khotanese, Sogdian, Middle Persian, Persian)."
}
```


### [2026-09-06T14:59:03.729Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-06T14:59:05.046Z] TOOL RESULT

```
# غائله - Entries from Persian Dictionaries

**Dehkhoda Dictionary:**
The entry defines غائله as: "badness; corruption, evil, fault, difficulty, hardship, enmity; hidden hatred; calamity, misfortune, disaster; sudden misfortune."

**Amid Dictionary:**
This source presents a more concise definition: "evil and corruption; destruction, tumult; [archaic usage] hardship and harm."

**Origin:**
Both dictionaries trace the word's etymology to the Arabic root غول (ghoul), which carries meanings of "sudden seizure, destruction, and suffering."
```


## [2026-09-06T14:59:15.124Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN Hirsch\"; grep -n \"Hirsch\" HRN.txt | head -10\necho \"=== ARY گوزن\"; grep -n \"گوزن\" incoming/ARY/ARY_pages.txt | head -5\necho \"=== NYB gwzn\"; grep -n -i \"gawazn\\|gw'zn\\|gwzn\" NYB_vol2_glossary.txt | head\necho \"=== CHEUNG\"; grep -n -i \"gavazn\\|gawazn\" CHEUNG.txt | head -3\necho \"=== FVQ ghul\"; grep -n -i \"ghul\\|ghaul\" FVQ.txt | head -5\necho \"=== AFM غول\"; grep -n \"غول\\|غيلان\" AFM_pages.txt | head -8"
}
```


### [2026-09-06T14:59:15.268Z] TOOL RESULT

```
=== HRN Hirsch
=== ARY گوزن
=== NYB gwzn
=== CHEUNG
=== FVQ ghul
=== AFM غول
2271:)003 ] ( ܐܦܫܵܬܐ) وباحورا (ܒܚܘܪܐ) وزتور (ܬܢܘܪ̈ܐ) وداغول (تحلس)
2793:* (الصيدانة ) الغول والسرّئة الخاق ܟ 3 من ܚܐܘ اي أسود ومن دان وهي
4602:داغول هم
```


## [2026-09-06T14:59:24.005Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN gavaz\"; grep -n \"gavaz\\|gaväz\\|gawaz\" HRN.txt | head -5\necho \"=== ARY کوزن\"; grep -n \"کوزن\\|گوزن\" incoming/ARY/ARY_pages.txt incoming/ARY/ARY_latin_index_pages.txt | head -5\necho \"=== IRN گوزن\"; grep -n \"گوزن\\|کوزن\" incoming/IRN/IRN_pages.txt | head -5\necho \"=== SYN deer\"; grep -n \"gavazn\\|gawazn\" SYN.txt IEC.txt | head\necho \"=== TAD غول\"; grep -n \"غول\" TAD_pages.txt | head -5\necho \"=== DEV ghoul\"; grep -n -i \"goule\\|ghoul\\|algol\" DEV.txt PHN.txt | head -8"
}
```


### [2026-09-06T14:59:24.144Z] TOOL RESULT

```
=== HRN gavaz
7720:phlv. gö bezw. gav^ arm. LW. gavazan (echt hov *Kuh'
22227:! gavazan 888.
=== ARY کوزن
=== IRN گوزن
=== SYN deer
=== TAD غول
2146:                       ‫قراغول ‪ -‬ترك « فراغول » معناهرييئةوطليعة وخفير‬
=== DEV ghoul
DEV.txt:398:Algol.  Etoile  de  la  constellation  de  Persée,  remar- quable par  la  variabilité  de  son  éclat.  C'est  l'arabe  J^xJi nJ-glwûl ,  le  même  dont  nous  avons  fait  goule.  (Voy.  plus loin  ce  mot.)  Les  Arabes  appellent  Jj.x]i  ^jJ^  ras  al-gJwûL tête  de  la  goule,  la  tête  de  Méduse  que  Persée  tient  sus- pendue a  la  main.
DEV.txt:1436:Goule.  En  arabe,  J^  ghouL  ogre  ou  démon  qui  dé- vore les  bommes;  être  surnaturel  et  malfaisant  qui  pos- sède la  faculté  de  changer  de  forme.  Nous  avons  mis  le nom  au  féminin  et  nous  avons  fait  de  la  goule  un  monstre à  face  humaine  qui  se  repaît  de  cadavres.  Ghoîd  est  d'ori- gine persane.
DEV.txt:1893:na'-.  Enfin  Bocthor  traduit  orcanète  par  Jytl\  u=*^  hlnna al-ghoul,  ce  que  nous  rendrions  par  le  henné  du  diable. De  tout  cela  résulte  pour  moi  la  conviction  que  orcanète est  le  même  mot  arabe  que  henné.  (Voy.  ce  terme.)  Ajou- tons que  Chabré  établit  la  svnonvmie  des  deux  expressions alhanna,  el-hanne^.
DEV.txt:2562:Algol.
DEV.txt:3591:Goule.
DEV.txt:4972:»^lc  voy.  Algarade. iô;lc  voy.  Razzia. ^L£  voy.  Alchimie,  5. wj«ijs^  vov.  Gamache. cj!j£  voy.  Astronomie,  7. Jb^  voy.  Grabeler. <j.r£  voy.  Garbin. A^sLcjC  y>er,s.  voy.  (jourgaiidinc. ci^  voy.  Carafe. J\y£  voy.  Gazelle. J-..C  voy.  Ghazel. 8^>^  voy.  Razzia. Ixa-^  voy.  Astronomie,  (i. Jyc  voy.  Algol,  Goule. L^".^^  voy.  Grèbe.
PHN.txt:5397:GOULE, s. m. (a.)
PHN.txt:5404:spécialement au substantif goule le genre féminin ; mais son
```


## [2026-09-06T14:59:33.446Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '7712,7726p' HRN.txt; echo \"---22220\"; sed -n '22222,22232p' HRN.txt"
}
```


### [2026-09-06T14:59:33.513Z] TOOL RESULT

```
kurd. geriyän 'spazieren, sich wenden; bei. LW.
gardag , n. garday umkehren , umwenden (70) ; sar.
yirs-am, yerd-ao etc.
887. (/am Schritt'.
aw. gäma- 'Schritt'; phlv. gäm.
888. f/äv llind', gö, gög 'Kalb' {^gavaka-)'''), göban 'Hirte'.
Kä§. V. K. Z. (/ö, Q. göb,
ap. vergl. Gau[brüva'j Fioß^vag; aw. gäv- Rind';
phlv. gö bezw. gav^ arm. LW. gavazan (echt hov *Kuh'
H. No. 148); ai. gdi^-,
kurd. gä 'Rind'; af/. yvä\ oss. d. yog, t. qiig 'Kuh'
(93); bei. gök, n. gö/ *Rind, Kuh, Ochse (123); wa/.
yäu, yü, sar. Jaw, siyn. /do, sangl. minj. ydo, yayn. gova;
vergl. sar. yubün, af/. yö6a 'Hirte*.
np. gävmes 'Büffel' : phlv. gavmes (Bund.), arm. LW.
---22220
(/«« 653.
! yanem 653.
^ar/ 657.
gahi 211.
i (/ar«?< 243.
! gavazan 888.
; gazpen 124.
I gerezman 906l>'«'.
■ ges 950.
///» 242.
'■' goin 946.
```


## [2026-09-06T14:59:41.749Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%DA%AF%D9%88%D8%B2%D9%86' --note 'page 201, root Gŭysna: Persian gavazn deer, MP gawazn, Proto-Iranian *gavasna-, Av. gauuasna-' 2>&1 | tail -2\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%BA%D9%88%D9%84' --note 'page 201, root Ğ.v.l: Arabic ghul from root غ و ل / verb ghala; Persian borrowing' 2>&1 | tail -2\npython3 tools/fetch_source.py 'https://www.etymonline.com/word/ghoul' --note 'page 201: English ghoul 1786 Beckford Vathek < Arabic ghul < ghala; Algol' 2>&1 | tail -2\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%A3%D9%85_%D8%BA%D9%8A%D9%84%D8%A7%D9%86' --note 'page 201: Arabic umm ghaylan acacia = mother of ghouls' 2>&1 | tail -2\npython3 tools/fetch_source.py 'https://abadis.ir/fatofa/%D9%85%D8%BA%DB%8C%D9%84%D8%A7%D9%86/' --note 'page 201: Mo\\'in and Dehkhoda on مغیلان < Arabic ام غیلان' 2>&1 | tail -2\npython3 tools/fetch_source.py 'https://abadis.ir/fatofa/%D8%BA%D8%A7%D8%A6%D9%84%D9%87/' --note 'page 201: Dehkhoda/Amid on غائله < Arabic root غول' 2>&1 | tail -2"
}
```


### [2026-09-06T14:59:43.498Z] TOOL RESULT

```
Exit code 1
(eval):7: unmatched '
```


## [2026-09-06T14:59:52.178Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%DA%AF%D9%88%D8%B2%D9%86' --note \"page 201, root Guysna: Persian gavazn deer, MP gawazn, Proto-Iranian *gavasna-, Av. gauuasna-\" 2>&1 | tail -2\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%BA%D9%88%D9%84' --note \"page 201, root G.v.l: Arabic ghul from root gh-w-l / verb ghala; Persian borrowing\" 2>&1 | tail -2\npython3 tools/fetch_source.py 'https://www.etymonline.com/word/ghoul' --note \"page 201: English ghoul 1786 Beckford Vathek from Arabic ghul from ghala; Algol\" 2>&1 | tail -2\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%A3%D9%85_%D8%BA%D9%8A%D9%84%D8%A7%D9%86' --note \"page 201: Arabic umm ghaylan acacia = mother of ghouls\" 2>&1 | tail -2\npython3 tools/fetch_source.py 'https://abadis.ir/fatofa/%D9%85%D8%BA%DB%8C%D9%84%D8%A7%D9%86/' --note \"page 201: Moin and Dehkhoda on moghilan from Arabic umm ghaylan\" 2>&1 | tail -2\npython3 tools/fetch_source.py 'https://abadis.ir/fatofa/%D8%BA%D8%A7%D8%A6%D9%84%D9%87/' --note \"page 201: Dehkhoda/Amid on ghaeleh from Arabic root gh-w-l\" 2>&1 | tail -2"
}
```


### [2026-09-06T14:59:58.116Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/0efffa3118453ab5.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/cfffc866fac64304.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9a8e9d6d2ef91f7e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/af1f15fa9a4adcc0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/450910c42adcd2a7.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c3b4cf78edc6596a.txt
```


## [2026-09-06T15:00:22.583Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr\nmkdir -p BQT BOOK\ncat > BQT/1854.vision.txt <<'EOF'\n[read from image: BQT_v3_picofile.pdf pdf page 651 = printed page ۱۸۵۴ (1854); note ref_page.py's default offset (-1205) is 2 too large for vol. 3 — correct is pdf = printed − 1203]\n\nگوزن ۱ - بفتح اول و ثانی و سکون ثالث ونون، نوعی از گاوکوهی باشد و شاخهای او به شاخهای درخت خشک شده ماند. گویند آب گوشهای چشم او تریاق زهرهاست.\n[با تصویر یک گوزن، زیرنویس: گوزن]\n\nfootnote:\n۱ - پهلوی gavâzan «اونوالا ۸۷»؛ گوزن معمولی جانوری است از خانوادهٔ پرشاخان از نشخوارکنندگان، که در جنگلها زیست کند. شاخهای آن هرسال می‌افتد و سال بعد یک شاخ اضافی درمی‌آید.\n\n(other headwords on the page: گوزکند، گوزگندم، گوزه، گوزهر، گوزه‌مخ، گوزینه، گوساله، گوسالهٔ فلک)\nEOF\ncat > BQT/2023.vision.txt <<'EOF'\n[read from image: BQT_v4_picofile.pdf pdf page 106 = printed page ۲۰۲۳ (2023)]\n\nمغیلان - با لام بر وزن سلیمان، نام درختی است خاردار و بعربی آنرا امّ‌غیلان (۳) خوانند ۴.\nمغیلان باستان - کنایه از دنیا و روزگار است.\nمغیلان‌گاه - با کاف فارسی بر وزن سلیمان‌جاه، بمعنی مغیلان باستان است که کنایه از دنیا باشد.\n\nfootnote:\n۴ - رک: تاج‌العروس ج۲ ص۱۹۰ «طلح».\n(۳) چش: مغیلان\n\n(no entry for غول or غائله on this page; those are in the غ section of vol. 3)\nEOF\ncp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg201.png BOOK/201.png\ncp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bqt1854.png BQT/1854.png\ncp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bqt2023.png BQT/2023.png\nls BQT/1854* BQT/2023* BOOK/201.png"
}
```


### [2026-09-06T15:00:24.412Z] TOOL RESULT

```
BOOK/201.png
BQT/1854.png
BQT/1854.txt
BQT/1854.vision.txt
BQT/2023.png
BQT/2023.txt
BQT/2023.vision.txt
```


## [2026-09-06T15:00:35.256Z] TOOL CALL #57: Bash

```json
{
 "command": "sed -n '1,120p' tools/verify_check.py"
}
```


### [2026-09-06T15:00:35.294Z] TOOL RESULT

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


## [2026-09-06T15:00:56.679Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification\npython3 - <<'EOF'\nimport json\nd=json.load(open('page-202.json'))\nfor e in d['entries'][:1]:\n    print(json.dumps(e, ensure_ascii=False, indent=1)[:3500])\nEOF"
}
```


### [2026-09-06T15:00:58.411Z] TOOL RESULT

```
{
 "entry": 0,
 "root": "Gwa, Gwâ, Gwen 2",
 "verdict": "confirmed",
 "modern_form": "PIE *gʷem- 'to go, to come' (with the collateral root *gʷeh₂- / *gʷā- 'to step, go'); Pokorny IEW 463-465",
 "note": "Pokorny's entry, which begins on p.463 exactly as Nourai cites, is headed 'gʷā-, gʷem- „gehen, kommen; zur Welt kommen, geboren werden“; gʷm̥-ti-s f., gʷem-tu-s m. „Gang, Schritt“', and it is deliberately a double entry (I. gʷā-, II. gʷem-), which is why Nourai's box carries two names, 'Gwa, Gwâ'. His third name 'Gwen 2' reflects the *gʷem- > *gʷen- variant Pokorny himself notes ('Unthematisch *(e)-gʷem-t (> *e-gʷen-t)', and Latin advenam / veniō with -n- for -m-); it is not a separate root in any modern handbook, so it is Nourai's own labelling convenience rather than an error of substance. Watkins/AHD 1985 heads the same material 'gʷā-. Also gʷem-. To go, come'; Cheung splits it into *gaH¹ (PIE *gʷeh₂-, Pok. 463 f.) and *gam¹ (PIE *gʷem-, Pok. 464 f.). The gloss 'to walk, to step, to come, to go' is an accurate rendering. Two words in the chart do not belong to this root: Avestan 'gâv' in node 6 (a misprint) and 'thamân' in node 12 (an unidentifiable form), and one Persian word, nîyâm (node 3), is derived by modern scholarship from a different root (*ni-dā-, not *ni-gam-). Everything else on the page is standard, well-attested Iranian etymology.",
 "note_fa": "جعبهٔ ریشه درست است: پوکورنی در صفحهٔ ۴۶۳ فرهنگ خود مدخل «gʷā-, gʷem-» را با معنای «رفتن، آمدن؛ به جهان آمدن، زاده شدن» آورده و همان‌جا نام‌های gʷm̥-ti-s و gʷem-tu-s «گام، رفتار» را می‌افزاید؛ پس هر دو صورت «Gwa/Gwâ» و «Gwem» از یک مدخل‌اند و برچسب «هندواروپایی» و معنای «راه رفتن، گام برداشتن، آمدن، رفتن» درست است. نام سوم «Gwen 2» گونهٔ *gʷen- است که خود پوکورنی (در *e-gʷen-t و در veniō لاتین) یاد کرده و در کتاب‌های امروزی ریشهٔ جداگانه‌ای به شمار نمی‌رود؛ این نام‌گذاری از خود نورایی است نه خطای علمی. واتکینز (پیوست AHD) نیز همین ماده را «gʷā-, also gʷem-: رفتن، آمدن» آورده و چونگ آن را به دو ریشهٔ *gaH¹ و *gam¹ بخش کرده است. در سراسر این صفحه تنها سه لغزش هست: صورت «gâv» در گرهٔ ۶ (غلط چاپی)، صورت «thamân» در گرهٔ ۱۲ (صورتی که در هیچ فرهنگی یافت نشد) و واژهٔ «نیام» در گرهٔ ۳ که پژوهش امروزی آن را از ریشهٔ دیگری (*ni-dā-) می‌داند.",
 "sources": [
  "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/gʷem-"
 ],
 "ref_check": [
  {
   "ref": "POK:463",
   "status": "supports",
   "note": "POK_02.txt line 1790 (the leaf whose running numbers are 463-465): 'gʷā-, gʷem- „gehen, kommen; zur Welt kommen, geboren werden“; gʷm̥-ti-s f., gʷem-tu-s m. „Gang, Schritt“, Verbaladjektiv gʷm̥-to-s. I. gʷā-: ... 2. gʷem-: ...'. The same pages carry 'av. gātu-s „Ort, Liegerstatt, Sessel, Thron“, apers. gāθu- ds.', 'av. gā-man- n. „Schritt“', 'av. jantu (*gʷem-tu-)' and 'av. jasaiti „er geht“' — i.e. Pokorny 463 alone underwrites the root box and nodes 1, 2 and 6."
  }
 ],
 "consulted": [
  {
   "src": "WLD",
   "where": "Bd. I 675-677 (WLD_Bd1 djvu line 42665 ff., running head 'gʷem-, gʷā-')",
   "stance": "supports",
   "note": "'gʷem-, gʷā-' … 'ai. gātram „Glied, Körper“; ai. gātu- „Gang, Weg, Raum, Ort“, av. gātu-s „Ort, Platz; Liegerstatt, Sessel, Thron“, ap. gāθu … ai. vi-gāman- n. „Schritt“ … av. gāman- n. „Schritt“'. This is the source Pokorny 463 abridges (Buck cites it as 'Walde-P. 1.675 ff.')."
  },
  {
   "src": "AHD",
   "where": "Watkins 1985, g-list (AHD_watkins1985.txt line ~539)",
   "stance": "supports",
   "note": "'gʷā-. Also gʷem-. To go, come. 1. Germanic *kum
```


## [2026-09-06T15:01:44.303Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HENNING\"; grep -n \"wzn\\|gavazn\" HENNING_selected_papers.txt | head -5\necho \"=== NYB gaw\"; grep -n \"gāw\\|gaw \" NYB_vol2_glossary.txt | head -3\necho \"=== PHN GOULE\"; sed -n '5395,5412p' PHN.txt\necho \"=== AFM ام غيلان\"; grep -n \"أم غيلان\\|ام غيلان\\|مغيلان\" AFM_pages.txt TAD_pages.txt ARB_mo3rb.txt 2>/dev/null | head -5\necho \"=== PLA ghul\"; grep -n -i \"ġūl\\|gul\\b\" incoming/PLA/PLA_pages.txt | head -3"
}
```


### [2026-09-06T15:01:44.427Z] TOOL RESULT

```
=== HENNING
5370:(112) }('=)[(113) "}wznyin 00 ‘rd'w{(114) Ke)tg 00 qyrdg'n 00 af (115) {mbr]'spnd oo "bysr dydym oo (116)] pymwg oo hpt yw 00 cwntts *hwngr (L17\(ky wad] (b)ynyd "wd wad wyihyd o0(118) )s ky ‘o twam ‘'y (119) Jt 20) | 'z'ryd oo Kk’ gylg (121)}pd "bxi'y{in) (122) ] dst (Fry. e, second page) (123)}pya{ (124) Jarystt')L. « Ikyag wi((125)[qyrbdkr'n) qxs'n @’hw()('n) (126) dd 00 bwd ky 'w "wadya{'n #)(127) ngnd oo jhwd qyrbg 'wd be{g kyrl](128) 00 hynd ky xwyl: yed 00 nym (@[yw] (129) nym yzd qwnynd 00 rw.[(130) ‘wznyin oo ‘stwf (131)hpt dyw'n "b((132)( .. Jeg "be{(138) o&(mn)l
5824:(Col, B) (traces of three lines) (18) why ny bwd hyd (19) 'wt'n pd wyptgyh (20) ‘wh (pjem'd kw pd (21) h'n drwzn p'dxi'yy (22) j’yd’'n hyd 'im’h (23) (yx) (blewysp nyja’d (24) } ‘wy
6019:(Second page) (11) [flembdyy "ywst (12) ptywit kt’ndt p'rty (13) [? Sywy](@n x jw'nmye pend (14) [t)y weynyy rktyy xw (15) [! ptslod cn ‘nxrwznyy (16) ptfsttyy ‘styb (17) (In rad ink) (p}tmnbys* iii fomb3y wy8B'y (One line left blank) (18) (Zn red ink) [y8}t (yy8)w 'ys'mndyb (19) (Im red ink) \y) way “Bmy bytylyy Byym (20) PRIN’ ty L
15059:(99-100) ‘yet, pre’, gpy8. The +f of ‘yet “row” or " street" forms part of the word, see the passages below; wrongly BBB., 122; BSOAS,, XI, 721 Chr, Sogd. 'yst, too, in singular — “street” (Lentz translated as  Plitze ") On prs’ “side” sce the preceding note; pri’kh, as “rib”, in P 7, 57. ‘The vor for “ shop, stall”, gay8 = *kopit (1), recalls Pers. ube (Man. MPers.kurbog, Arm. krpak, eto.)—Cf. M 108, 10 (very broken passage) a]m'nyt "nzrwzn Buvtyt (—) ‘yett "ty qpybtt (| ] "ty 8x7. OF greater importan fragment M548, a miser ained a different recension, but one very close to the one published here, of the “ story of the world”
=== NYB gaw
=== PHN GOULE
étymologistes ont pu trouver entre gouffre et le latin fptrges.%
18Û GOU
GOULE, s. m. (a.)
J^ [g^^â/j, au pluriel (^>^ [ghtlân\ et Jt^T [àghwâï]^ ogre.
^om d'une espèce de démon qui, selon la mythologie orien-
tale, habite les forêts, attaque les animaux et les hommes, et
se nourrit de cadavres. — Ce mot vient du verbe arabe Jl^
[gf^l\ fondre sur quelqu'un ou sur quelque chose, VaUaquer subi-
tement et remporter. — Plusieurs dictionnaires français donnent
spécialement au substantif goule le genre féminin ; mais son
correspondant arabe, qui est ici au masculin, se dit, en gé-
néral, de tout démon malfaisant et capable de prendre diverses
formes. — Toutefois le féminin arabe de J^ [^^'<>ti^] ogre peut
s'écrire Jil^ [g'AoiUat] ogresse, et autoriser en français l'emploi
de goule au féminin.
GOULOT, s. m. (p.)
y)i [guelou] gorge, gosier; col d'un vase, d'une bouteille. — Au-
trefois on disait goulet; mais aujourd'hui ce dernier terme n'est
=== AFM ام غيلان
=== PLA ghul
428:           pers.     g        ar.          2.    B.:     pers.       *gol&in >ar.                   gulßin
3790:       aw.           pußra       mit       der     Bed.         "Sohn",        analog      v.     ar.     ne       guläm     "Sohn,        Sklave"
5166:JP- Zul:           "Blume"           aus dem pers. Ygol i <—Imp.)r gul —Taw.                                     varzsa       Dar.
```


## [2026-09-06T15:09:30.390Z] TOOL CALL #60: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk201.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW_GAVAZN = \"https://en.wiktionary.org/wiki/%DA%AF%D9%88%D8%B2%D9%86\"\nW_GHUL = \"https://en.wiktionary.org/wiki/%D8%BA%D9%88%D9%84\"\nW_UMM = \"https://en.wiktionary.org/wiki/%D8%A3%D9%85_%D8%BA%D9%8A%D9%84%D8%A7%D9%86\"\nE_GHOUL = \"https://www.etymonline.com/word/ghoul\"\nA_MOGH = \"https://abadis.ir/fatofa/%D9%85%D8%BA%DB%8C%D9%84%D8%A7%D9%86/\"\nA_GHAE = \"https://abadis.ir/fatofa/%D8%BA%D8%A7%D8%A6%D9%84%D9%87/\"\n\nISS74 = {\n \"ref\": \"ISS:74\",\n \"status\": \"supports\",\n \"note\": \"Bailey's 'Indo-Scythian Studies VI (Prolexis to the Book of Zambasta)' itself is not on disk, but its p.74 is independently vouched for: Gharib's Sogdian Dictionary, entry 4079 (SOD_pages.txt leaf 227 = printed p.162) gives \\\"γ'wzn B / γawazn ©Khwar. γwzn-, Khot. gguysna-, Oss. qwazn ... deer\\\" and cites as its authority exactly 'Bailey, Prolexis, 74'. Bailey's own Dictionary of Khotan Saka (ISS_alt_DKS.txt, pp.87-88) repeats the same material: \\\"ggūysna- 'stag, deer' ... From *gavazna-, Av. gavasna-, Sogd. γ'wzn, plur. γ'wzn'n, Zor.P. gwzn, N.Pers. gavazn, Oss. D. γüænzæ\\\". So ISS:74 is the right page for the whole Khotanese-Avestan-Sogdian-Pahlavi-Persian set.\"\n}\n\nDKS_ROOT = {\n \"src\": \"ISS_alt_DKS\",\n \"where\": \"Bailey, Dictionary of Khotan Saka, pp.87-88 s.v. ggūysna- (ISS_alt_DKS.txt line 1916)\",\n \"stance\": \"partial\",\n \"note\": \"\\\"ggūysna- 'stag, deer' ... From *gavazna-, Av. gavasna-, Sogd. γ'wzn, ... Zor.P. gwzn, N.Pers. gavazn ... Possibly named from the colour gau- : gu- 'reddish yellow' ... nor to gau- 'bovine'.\\\" Supports every word in the chart, but makes the Khotanese form a REFLEX of *gavazna-, not the ancestor of the Avestan word as Nourai's box implies.\"\n}\n\nentry3 = {\n \"entry\": 3,\n \"root\": \"Gūysna\",\n \"verdict\": \"plausible\",\n \"modern_form\": \"Proto-Iranian *gavazna- 'deer, stag' (Wiktionary: *gavasna-); the form printed in Nourai's root box is its Khotan-Saka reflex ggūysna-\",\n \"note\": \"Every word in this chart is real and the family is uncontroversial — Khotanese ggūysna-, Avestan gauuasna-, Sogdian γ'wzn, Middle Persian gawazn, New Persian گوزن, Ossetic qūаzn — and Bailey (DKS 87-88), Gharib (SOD 4079) and Wiktionary all set them under one etymon *gavazna-. What is wrong is the SHAPE of the tree. Nourai puts the Khotanese word (labelled with Bailey's term 'Indo-Schythian') in the root box and hangs Avestan under it, then Pahlavi and Sogdian under Avestan. In modern terms all five are parallel reflexes of Proto-Iranian *gavazna-; none descends from another. The etymology of the etymon itself is unsettled: Bailey suggests a colour word gau-/gu- 'reddish-yellow' (like Skt. hariṇī 'antelope'), Gamkrelidze-Ivanov a compound of *gá̄wš 'cow' + *Hajáh 'goat', and Witzel (2016) a BMAC substrate word; the -asna-/-azna- suffix is the same one Bailey isolates in *bagazana- > bvaysua-. Nourai gives no PIE root, which is right, since the word has none secure. Gloss 'deer, stag' is exactly Bailey's.\",\n \"note_fa\": \"جعبهٔ ریشه در این نمودار صورت ختنی (سکایی ختن) ggūysna- «گوزن» است که نورایی به پیروی بیلی آن را «هندوسکایی» می‌نامد. این واژه واقعی است و معنای «گوزن، گوزن نر» هم درست است، امّا ریشه نیست: در ریشه‌شناسی امروزی همهٔ این صورت‌ها — ختنی ggūysna-، اوستایی gauuasna-، سغدی γ'wzn، فارسی میانهٔ gawazn و فارسی نو گوزن — بازماندهٔ موازی یک ستاک ایرانی باستان *gavazna- اند و هیچ‌یک از دیگری مشتق نشده است. خود این ستاک ریشهٔ مطمئنی ندارد: بیلی آن را به رنگ‌واژهٔ gau-/gu- «زردسرخ» می‌برد، گامکرلیدزه و ایوانوف آن را ترکیب *gāuš «گاو» + *Hajāh «بز» می‌دانند و ویتزل آن را وام‌واژه‌ای از زیرلایهٔ BMAC می‌شمارد. پس ادعای نورایی در مادّهٔ واژگان درست است و فقط در جهت پیکان‌ها با احتیاط پذیرفتنی است. نکتهٔ دیگر: ارجاع BQT:1754 در هر دو گرهٔ فارسی میانه و فارسی نو نادرست است؛ مدخل «گوزن» در برهان قاطع در صفحهٔ ۱۸۵۴ است، یعنی یک رقم در خود کتاب اشتباه چاپ شده است.\",\n \"sources\": [W_GAVAZN],\n \"ref_check\": [ISS74],\n \"consulted\": [\n   DKS_ROOT,\n   {\"src\": \"BRT\", \"where\": \"Bartholomae, Altiranisches Wörterbuch, s.v. gavasna- (BRT.txt line 10173)\",\n    \"stance\": \"partial\",\n    \"note\": \"\\\"j. gavasna- m. -?-: asti yō gavasnahe snāuya jya Yt.10.128 Gl. Vll. Name eines Tiers; dann: 'es kommt vor, dass die aus einer Tiersehne gefertigte Bogensehne von einem G. ist'.\\\" Bartholomae has the Avestan word but expressly leaves its meaning open ('-?-', 'probably the name of an animal'); the gloss 'deer' comes from Bailey, not from the Avestan text.\"},\n   {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary p.36 (PHD.txt line 380)\",\n    \"stance\": \"supports\",\n    \"note\": \"\\\"gawazn [gw'zn' | N ~] deer\\\" — the Pahlavi and New Persian ends of the chain, with the very spelling gw'zn Nourai prints.\"}\n ],\n \"nodes\": []\n}\n\nentry3[\"nodes\"] = [\n {\n  \"id\": 1, \"lang\": \"Avestan\", \"words\": \"gavasna\",\n  \"verdict\": \"plausible\",\n  \"derivation\": \"Younger Avestan gauuasna- (Bartholomae's transcription gavasna-) is a hapax: it occurs only in the Pahlavi gloss to Yasht 10.128, in the phrase asti yō gavasnahe snāuya jya 'there is a bowstring made of the sinew of a g.'. Bartholomae (AiW s.v.) therefore prints it with '-?-' and says only 'probably the name of an animal'. The gloss 'deer' that Nourai gives is Bailey's, secured comparatively: Khotanese ggūysna-, Sogdian γ'wzn, Zoroastrian Pahlavi gwzn, NPers. gavazn and Ossetic γüænzæ/qūаzn all mean 'deer/stag', so *gavazna- must have meant that and the Avestan hapax is its Old Iranian form. Phonetically Av. -sn- : Khot. -sn- : Sogd./MP -zn- is the regular pair (voiceless before the suffix in Avestan spelling, voiced elsewhere); Khotanese ggū- for *gava- is the normal loss of intervocalic -v- with contraction and u-colouring (compare Khot. gyaysna- 'sacrifice' : Av. yasna-). The arrow from Nourai's Khotanese-shaped root box to Avestan should be read the other way round: Avestan is the oldest attestation, Khotanese a much later reflex of the same *gavazna-.\",\n  \"derivation_fa\": \"صورت اوستایی gauuasna- (خوانش بارتولومه: gavasna-) تنها یک‌بار در حاشیهٔ پهلوی یشت ۱۰ بند ۱۲۸ آمده است: asti yō gavasnahe snāuya jya «زهی هست که از پی چارپایی به نام g. ساخته شده». به همین سبب بارتولومه در «Altiranisches Wörterbuch» معنای آن را با علامت پرسش می‌آورد و تنها می‌گوید «احتمالاً نام جانوری است». معنای «گوزن» از راه مقایسه به دست آمده است: ختنی ggūysna-، سغدی γ'wzn، پهلوی gwzn، فارسی گوزن و آسی قوازن، همه به معنای گوزن‌اند. دگرگونی آوایی منظّم است: خوشهٔ -sn- اوستایی در شاخهٔ غربی و سغدی به -zn- واک‌دار بدل می‌شود. در مجموع واژه واقعی است ولی معنای آن در متن اوستا قطعی نیست؛ ادعای نورایی با احتیاط پذیرفتنی است.\",\n  \"sources\": [W_GAVAZN],\n  \"ref_check\": [ISS74],\n  \"consulted\": [\n    {\"src\": \"BRT\", \"where\": \"AiW s.v. gavasna- (BRT.txt line 10173); cross-refs s.v. jyā- (line 11693) and snāuya- (line 27133)\",\n     \"stance\": \"partial\",\n     \"note\": \"\\\"j. gavasna- m. -?-: asti yō gavasnahe snāuya jya Yt.10.128 Gl.\\\" and, s.v. snāuya-, \\\"'aus einer (Tier)sehne gefertigt': asti yō gavasnahe 'ya jya\\\". Word confirmed, meaning left open.\"},\n    {\"src\": \"ISS_alt_DKS\", \"where\": \"Bailey, DKS pp.87-88 and the introduction (ISS_alt_DKS.txt lines 38, 1916)\",\n     \"stance\": \"supports\",\n     \"note\": \"In the preface Bailey lists as evidence of Khotanese archaism \\\"ggūysna- 'deer', Av. gavasna-\\\", and the entry itself reads \\\"From *gavazna-, Av. gavasna-\\\" — i.e. Bailey equates precisely these two forms.\"},\n    {\"src\": \"AVG\", \"where\": \"Jackson, Avesta Grammar (AVG.txt, grep 'gavasna'/'gauuasna')\",\n     \"stance\": \"silent\",\n     \"note\": \"The word does not occur; Jackson's grammar has no lexicon of hapax nouns.\"}\n  ]\n },\n {\n  \"id\": 2, \"lang\": \"Pahlavi\", \"words\": \"gw'zn, gavâzan\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"Book Pahlavi <gw'zn'> is read gawazn by MacKenzie (CPD p.36: \\\"gawazn [gw'zn' | N ~] deer\\\"); the older reading gavāzan, which Nourai prints as his second form, is Unvala's and is the one Mo'in repeats in his footnote to Borhan-e Qate' s.v. گوزن (\\\"پهلوی gavâzan «اونوالا ۸۷»\\\"). Both render one word: Proto-Iranian *gavazna- > MP gawazn, with the Avestan-type cluster -sn- voiced to -zn- between sonorants and the anaptyctic vowel of the older reading (gavāzan) merely an editorial way of pronouncing the consonant cluster of the Aramaeogram-free spelling. The word is attested in running text: Unvala's edition of 'King Husrav and his Boy' §30 lists the best meats, u varāz u gavāzan u gōr u gāv, which he translates 'der Eber, und der Bergochs, und der Wildesel, und das Rind'. Strictly, MP gawazn is not descended from Avestan gauuasna- but is its Middle-Western-Iranian sister; the chart's arrow is a genealogical shorthand.\",\n  \"derivation_fa\": \"در پارسی میانه (پهلوی کتابی) این واژه به صورت <gw'zn'> نوشته می‌شود؛ مکنزی در «فرهنگ کوچک پهلوی» ص ۳۶ آن را gawazn می‌خواند و معنای «گوزن» می‌دهد؛ خوانش کهن‌تر gavāzan از اونوالاست و معین نیز در حاشیهٔ برهان قاطع (ذیل «گوزن»، ص ۱۸۵۴) همین را می‌آورد: «پهلوی gavâzan «اونوالا ۸۷»». هر دو یک کلمه‌اند: از ایرانی باستان *gavazna-، با واک‌دارشدن -sn- به -zn-. این واژه در متن پهلوی «خسرو و ریدک» بند ۳۰ آمده است: u varāz u gavāzan u gōr u gāv. تنها نکته آنکه پهلوی فرزند اوستایی نیست بلکه خواهر آن است؛ پیکان نمودار را باید به معنای «همان واژه در دورهٔ بعدی» خواند.\",\n  \"sources\": [W_GAVAZN],\n  \"ref_check\": [\n    ISS74,\n    {\"ref\": \"BQT:1754\", \"status\": \"not_found\",\n     \"note\": \"Wrong page. BQT p.1754 (BQT_v3_picofile.pdf pdf page 551; printed page = pdf page + 1203 in vol.3) is at the very end of the کاف section — کیس، کیدپا، کیرخ، گیرو، کیسو — and has nothing on deer. The گوزن entry is on printed p.1854 (pdf page 651; image saved to sources/refs/ocr/BQT/1854.png, transcript in 1854.vision.txt): \\\"گوزن ۱ - بفتح اول و ثانی و سکون ثالث ونون، نوعی از گاوکوهی باشد...\\\", with Mo'in's footnote \\\"۱ - پهلوی gavâzan «اونوالا ۸۷»\\\". So the reference is off by exactly 100 — a misprint in Nourai for BQT:1854, and the page he wanted does support both the Pahlavi form and the Persian word.\"},\n    {\"ref\": \"UNV:56\", \"status\": \"partial\",\n     \"note\": \"Unvala's 1963 Paris edition (with the glossary paginated as Nourai cites) is not available; the 1917 Heidelberg original is on disk (UNV.txt). There gavāzan stands in the text itself, §30 on printed p.21 (UNV.txt leaf 24): \\\"u varāz u gavāzan u gōr u gāv 30.\\\", translated 'Das Rind, und der Wildesel, und der Bergochs, und der Eber'. So Unvala does have the word with Nourai's vocalisation, but I cannot confirm his page 56; note that Mo'in, citing the same book for the same word, gives 'Unvala 87'.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD p.36 (PHD.txt line 380; PHD_mackenzie.txt line 2488) and the English-Pahlavi index s.v. 'deer' (PHD.txt line 1530)\",\n     \"stance\": \"supports\",\n     \"note\": \"\\\"gawazn [gw'zn' | N ~] deer\\\"; index: \\\"deer gawazn.\\\" MacKenzie's spelling gw'zn' is letter-for-letter Nourai's gw'zn.\"},\n    {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II (Glossary) — grep 'gawazn', 'gw'zn', 'gwzn'\",\n     \"stance\": \"silent\",\n     \"note\": \"No hit; Nyberg's glossary covers only the texts printed in Part I, which do not contain the word.\"},\n    {\"src\": \"ISS_alt_DKS\", \"where\": \"Bailey, DKS p.88 s.v. ggūysna-\",\n     \"stance\": \"supports\",\n     \"note\": \"\\\"...Sogd. γ'wzn, plur. γ'wzn'n, Zor.P. gwzn, N.Pers. gavazn\\\" — Bailey's 'Zor.P. gwzn' is exactly Nourai's Pahlavi spelling.\"}\n  ]\n },\n {\n  \"id\": 3, \"lang\": \"Persian\", \"words\": \"gavazn «گوزن»\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"New Persian گوزن gavazn 'deer, stag' continues Middle Persian gawazn unchanged except for the ordinary NP treatment of the MP -w- as -v-; the cluster -zn is preserved, as in ژرف -type learned words, because it is word-final. Borhan-e Qate' (ed. Mo'in) p.1854 defines it \\\"نوعی از گاوکوهی باشد و شاخهای او به شاخهای درخت خشک‌شده ماند\\\" ('a kind of mountain ox whose antlers are like the branches of a dry tree') and prints a woodcut of a stag; Mo'in's own footnote derives it from Pahlavi gavâzan after Unvala. Hübschmann, Persische Studien no.888, insists on separating this word from the homophonous gavāz/Armenian gavazan 'ox-goad, staff': \\\"Davon zu unterscheiden np. gavaz = gavazn 'cervus, dama'\\\" — which is what Nourai does too, since he keeps them on different pages. Ossetic γüænzæ / qūаzn and the Khwarezmian γwzn- cited by Gharib show the same etymon outside Persian.\",\n  \"derivation_fa\": \"«گوزن» در فارسی نو دنبالهٔ بی‌واسطهٔ پارسی میانهٔ gawazn است و جز بدل‌شدن w میانی به v دگرگونی نیافته است. برهان قاطع (به تصحیح معین) در ص ۱۸۵۴ می‌نویسد: «نوعی از گاوکوهی باشد و شاخهای او به شاخهای درخت خشک‌شده ماند» و تصویر گوزنی را هم چاپ کرده؛ معین در حاشیه آن را از پهلوی gavâzan گرفته است. هوبشمان در «مطالعات فارسی» شمارهٔ ۸۸۸ تأکید می‌کند که این واژه را باید از «گواز» (میخ‌گاورانی، ارمنی gavazan «عصا») جدا دانست. ادعای نورایی درست است؛ تنها شمارهٔ صفحهٔ برهان قاطع (۱۷۵۴ به جای ۱۸۵۴) غلط چاپ شده است.\",\n  \"sources\": [W_GAVAZN],\n  \"ref_check\": [\n    {\"ref\": \"BQT:1754\", \"status\": \"not_found\",\n     \"note\": \"Same misprint as in node #2: p.1754 of Borhan-e Qate' is in the کیس/گیس stretch at the end of کاف; the گوزن entry with its stag woodcut and Mo'in's Pahlavi footnote is on p.1854 (image at sources/refs/ocr/BQT/1854.png). Read as BQT:1854 the citation fully supports the node.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"BQT\", \"where\": \"Borhan-e Qate', ed. Mo'in, p.1854 s.v. گوزن (vol.3 scan, pdf page 651)\",\n     \"stance\": \"supports\",\n     \"note\": \"\\\"گوزن ۱ - ... نوعی از گاوکوهی باشد و شاخهای او به شاخهای درخت خشک‌شده ماند\\\"; footnote \\\"۱ - پهلوی gavâzan «اونوالا ۸۷»؛ گوزن معمولی جانوری است از خانوادهٔ پرشاخان از نشخوارکنندگان\\\".\"},\n    {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien no.888 (HUB.txt line 3197)\",\n     \"stance\": \"supports\",\n     \"note\": \"\\\"Davon zu unterscheiden np. gavaz = gavazn 'cervus, dama', g. go gevezm 'Hirsch' ZDMG.36,63 = afgh. LW. gavazn 'an elk'. Vgl. auch afgh. gavaz 'Gemse'.\\\" Hübschmann confirms the word and its meaning and expressly separates it from gavāz 'ox-goad'.\"},\n    {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no.888 (HRN.txt line 7720) and index (line 22227)\",\n     \"stance\": \"silent\",\n     \"note\": \"Horn's no.888 treats gāv 'Rind' and cites Armenian gavazan only as a loan meaning 'staff'; he has no entry for gavazn 'deer'. It is precisely this gap that Hübschmann's no.888 fills.\"},\n    {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e Rishe-ha — grep گوزن/کوزن in ARY_pages.txt and ARY_latin_index_pages.txt\",\n     \"stance\": \"silent\",\n     \"note\": \"No hit; the word is not among Aryanpur's headwords (or the OCR of the page is too poor to show it).\"}\n  ]\n },\n {\n  \"id\": 4, \"lang\": \"Sogdian\", \"words\": \"gwzn\",\n  \"verdict\": \"plausible\",\n  \"derivation\": \"The Sogdian word is real, but the standard rendering of it is γ'wzn (Gharib's transliteration; Bailey writes Sogd. γ'wzn, plur. γ'wzn'n), pronounced γawazn. Gharib, Sogdian Dictionary no.4079 (printed p.162) gives: \\\"γ'wzn B / γawazn ©Khwar. γwzn-, Khot. gguysna-, Oss. qwazn ©inst. -'-, gen.pl. -'n ⇒*γwzn / deer\\\", with references to the Buddhist Sogdian texts (SCE 151, 354; Dhy.36; GMS 375, 1230) and to Bailey's Prolexis p.74. Nourai's 'gwzn' drops the initial gamma-marker and the ‘alef of the Sogdian spelling; it is in fact the Khwarezmian shape γwzn- and Bailey's 'Zor.P. gwzn', not the Sogdian one, so the form as printed is a loose transliteration rather than a citable Sogdian spelling. The derivation is otherwise sound: Sogd. γawazn < Proto-Iranian *gavazna-, with initial g- spirantised to γ- (the regular Sogdian treatment) and -sn- voiced to -zn-. As with Pahlavi, Sogdian is a sister of Avestan, not its daughter.\",\n  \"derivation_fa\": \"صورت سغدی این واژه در فرهنگ سغدی بدرالزمان قریب (مدخل ۴۰۷۹، ص ۱۶۲) γ'wzn است، خوانده می‌شود γawazn، به معنای «گوزن»؛ قریب همانجا خوارزمی γwzn-، ختنی gguysna- و آسی qwazn را هم‌ریشهٔ آن می‌شمارد و به بیلی، Prolexis ص ۷۴ ارجاع می‌دهد. آنچه نورایی نوشته (gwzn) نشانهٔ آغازین γ و الف را ندارد و در واقع صورت خوارزمی/پهلوی است نه سغدی؛ پس آوانویسی سهل‌انگارانه‌ای است. از نظر آوایی راه درست است: g آغازین ایرانی باستان در سغدی به سایشی γ بدل می‌شود و -sn- واک‌دار می‌گردد. نشانی «SOD:180» نیز نادرست است (ص ۱۸۰ دربارهٔ مدخل‌های ywys-/ywyc- است).\",\n  \"sources\": [W_GAVAZN],\n  \"ref_check\": [\n    {\"ref\": \"SOD:180\", \"status\": \"not_found\",\n     \"note\": \"Wrong locus. Gharib's entry for the word is no.4079 on printed p.162 (SOD_pages.txt leaf 227; printed page = leaf − 65 here, checked against the running numbers 157-162 on leaves 222-227): \\\"4079 γ'wzn B ... γawazn ©Khwar. γwzn-, Khot. gguysna-, Oss. qwazn ... deer ... Bailey, Prolexis, 74\\\". Printed p.180 (leaf 245) carries the unrelated entries γwys-, γwyz'k(w), γwyck-. Content-wise Gharib fully supports the node; only the page number is wrong (and it is not an entry number either, since the entry is 4079).\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"SOD\", \"where\": \"Gharib, Sogdian Dictionary no.4079, p.162 (SOD_pages.txt line 15347 ff.)\",\n     \"stance\": \"supports\",\n     \"note\": \"\\\"4079 γ'wzn B / γawazn ©Khwar. γwzn-, Khot. gguysna-, Oss. qwazn ©inst. -'-, gen. pl. -'n ⇒*γwzn / deer / SCE 151, 354; BSTBL, Dhy.36; GMS 375, 1230; Bailey, Prolexis, 74\\\".\"},\n    {\"src\": \"ISS_alt_DKS\", \"where\": \"Bailey, DKS p.88 s.v. ggūysna-\",\n     \"stance\": \"supports\",\n     \"note\": \"\\\"From *gavazna-, Av. gavasna-, Sogd. γ'wzn, plur. γ'wzn'n, Zor.P. gwzn, N.Pers. gavazn\\\" — note that Bailey's bare 'gwzn' is the Pahlavi, not the Sogdian, form.\"},\n    {\"src\": \"HENNING\", \"where\": \"Henning, Selected Papers — grep 'wzn', 'gavazn'\",\n     \"stance\": \"silent\",\n     \"note\": \"Only unrelated Manichaean strings ('wznyyn, 'nxrwzn); Henning's Sogdian papers on disk do not discuss the deer word.\"}\n  ]\n }\n]\n\nFVA304 = {\"ref\": \"FVA:304\", \"status\": \"not_checked\",\n \"note\": \"FVA = S.M. Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (1368/1989). refs_online.json records that no digital copy exists on any permitted platform (re-searched 2026-09), and there is no local file, so p.304 cannot be inspected.\"}\n\nentry4 = {\n \"entry\": 4,\n \"root\": \"Ğ.v.l\",\n \"verdict\": \"plausible\",\n \"modern_form\": \"Arabic root غ-و-ل (ġ-w-l) 'to seize, snatch away, carry off suddenly'; verb غالَ (ġāla), verbal noun غَوْل (ġawl)\",\n \"note\": \"The root and its gloss are right for ARABIC: Wiktionary, Klein, Pihan and Devic all analyse غول ġūl as a deverbal of غال ġāla 'to seize, take suddenly' (Pihan p.180: \\\"Ce mot vient du verbe arabe ġāla, fondre sur quelqu'un ou sur quelque chose, l'attaquer subitement et l'emporter\\\"). What is over-stated is the label 'Semitic'. غ-و-ل is not a root reconstructed for Proto-Semitic in the standard literature: there is no accepted Hebrew, Aramaic or Akkadian cognate, and the one Semitic word sometimes compared, Akkadian gallû 'underworld demon' (itself a Sumerian loan, gal5-lá), belongs to a different root and is not the source of ġūl. Fraenkel's Die aramäischen Fremdwörter has no ġūl, i.e. he did not consider it an Aramaism. So the box should read 'Arabic', not 'Semitic'; everything hanging under it is correct. Nourai's own reference FVA:304 could not be consulted (no copy of Nahvi's dictionary exists digitally).\",\n \"note_fa\": \"ریشهٔ عربی غ-و-ل به معنای «ربودن، ناگهان گرفتن و بردن» درست است و فعل «غالَ» و مصدر «غَوْل» پایهٔ همهٔ مشتقّات این نمودار است؛ پیان (ص ۱۸۰) هم می‌نویسد «این واژه از فعل عربی غال آمده است: ناگهان بر کسی تاختن و او را بردن». امّا برچسب «سامی» درست نیست: این ریشه در زبان‌های سامی دیگر (عبری، آرامی، اکدی) هم‌ریشهٔ پذیرفته‌شده‌ای ندارد و اکدی gallû «دیو جهان زیرین» خود وام‌واژه‌ای سومری و از ریشه‌ای دیگر است. فرنکل نیز «غول» را در شمار وام‌واژه‌های آرامی نیاورده است. پس بهتر بود جعبهٔ ریشه «عربی» نام می‌گرفت؛ بقیهٔ نمودار درست است.\",\n \"sources\": [W_GHUL, W_UMM],\n \"ref_check\": [FVA304],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein, CEDEL p.655 s.v. ghoul (KLN_1966.txt line 16106) and p.48 s.v. Algol (line 2184)\",\n    \"stance\": \"supports\",\n    \"note\": \"\\\"ghoul, n., an evil demon who robs graves and feeds on the dead. — Arab. ghūl, fr. ghāla, 'he took suddenly'. Cp. Algol.\\\" Klein's gloss of the verb is word-for-word Nourai's 'to take suddenly'.\"},\n   {\"src\": \"PHN\", \"where\": \"Pihan, Dictionnaire étymologique... p.180 s.v. GOULE (PHN.txt line 5397)\",\n    \"stance\": \"supports\",\n    \"note\": \"\\\"GOULE, s.m. (a.) ġūl, au pluriel ġīlān et aġwāl, ogre... Ce mot vient du verbe arabe ġāl, fondre sur quelqu'un ou sur quelque chose, l'attaquer subitement et l'emporter.\\\"\"},\n   {\"src\": \"AFA\", \"where\": \"Fraenkel, Die aramäischen Fremdwörter im Arabischen — grep 'ġūl', 'gul', 'Ghul'\",\n    \"stance\": \"silent\",\n    \"note\": \"No entry: Fraenkel does not list غول among Arabic words of Aramaic origin, which is one reason for treating the root as Arabic rather than pan-Semitic.\"},\n   {\"src\": \"AFM\", \"where\": \"Addi Shir, al-Alfāẓ al-fārisiyya al-muʿarraba — grep غول/غيلان in AFM_pages.txt\",\n    \"stance\": \"silent\",\n    \"note\": \"No entry; Addi Shir does not claim غول as a Persian loan into Arabic — consistent with Nourai's direction of borrowing (Arabic → Persian).\"}\n ],\n \"nodes\": []\n}\n\nentry4[\"nodes\"] = [\n {\n  \"id\": 1, \"lang\": \"Arabic\", \"words\": \"ğala; ğŭl; umme-ğîlân\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"All three items are standard Arabic. (1) غَالَ ġāla (root غ-و-ل, hollow verb, impf. yaġūlu, verbal noun ġawl) 'to seize, snatch away, carry off suddenly, destroy'. (2) غُول ġūl, pl. ġīlān / aġwāl, the deverbal noun: 'that which snatches suddenly' → the shape-shifting desert demon of pre-Islamic and later Arabic lore that waylays travellers; already in Qur'an 37:47 the word ġawl is used of wine's power to 'carry away' the senses, which shows the concrete sense of the root. (3) أُمّ غيلان umm ġaylān, literally 'mother of the ghouls', the popular Arabic name of the thorny desert acacia (Vachellia nilotica / gummifera), so called because the demons were thought to lurk in its shade; ġaylān here is the plural of ġūl, and ġīlān / ġaylān vary in the sources. Nourai's spelling 'ğîlân' is the usual Persianate reading of the same plural.\",\n  \"derivation_fa\": \"هر سه صورت عربی و معمول‌اند: ۱) «غالَ» فعل اجوف از ریشهٔ غ-و-ل (مضارع یَغُولُ، مصدر غَوْل) به معنای «ناگهان ربودن، بردن، هلاک کردن»؛ ۲) «غول» (جمع: غیلان، أغوال) اسم از همین فعل، یعنی «رباینده»، و در فرهنگ عرب دیو بیابانی دگردیس‌پذیر که راهگذران را گمراه می‌کند؛ ۳) «أمّ غیلان» تحت‌اللفظ «مادر غولان»، نام عامیانهٔ درختچهٔ خاردار بیابانی (طلح، اقاقیای صمغی)، زیرا می‌پنداشتند غولان در سایهٔ آن پناه می‌گیرند. ترجمهٔ نورایی از هر سه درست است و ادعای او تأیید می‌شود.\",\n  \"sources\": [W_GHUL, W_UMM],\n  \"ref_check\": [FVA304],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"Klein, CEDEL p.655 s.v. ghoul (KLN_1966.txt line 16106)\",\n     \"stance\": \"supports\",\n     \"note\": \"\\\"Arab. ghūl, fr. ghāla, 'he took suddenly'\\\" — the derivation ġūl < ġāla exactly as Nourai draws it.\"},\n    {\"src\": \"PHN\", \"where\": \"Pihan p.180 s.v. GOULE (PHN.txt line 5397)\",\n     \"stance\": \"supports\",\n     \"note\": \"\\\"ġūl, au pluriel ġīlān et aġwāl, ogre. Nom d'une espèce de démon qui... habite les forêts, attaque les animaux et les hommes, et se nourrit de cadavres. — Ce mot vient du verbe arabe ġāl...\\\" Confirms both the verb and the plural ġīlān that underlies umm-ġīlān.\"},\n    {\"src\": \"LKT\", \"where\": \"Lokotsch, Etym. Wörterbuch no.741 'Ar. ġūl', p.59 (LKT.txt line 1807)\",\n     \"stance\": \"supports\",\n     \"note\": \"\\\"Ein Wüstengeist, die Mitte zwischen Mensch und Ginn haltend, mit menschlicher Gestalt und Eselsbeinen, doch häufig seine Gestalt wechselnd... aus dem ar. Plur. ġailān ergab sich frz. gailan.\\\"\"},\n    {\"src\": \"AFA\", \"where\": \"Fraenkel — grep for ġūl\",\n     \"stance\": \"silent\",\n     \"note\": \"Not listed among the Aramaic loanwords; no Semitic cognate offered.\"}\n  ]\n },\n {\n  \"id\": 2, \"lang\": \"Persian\", \"words\": \"ğŭl «غول»; ğâeleh «غائله»; moğîlân «مغیلان»\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"All three are Arabic loans in Persian, borrowed after the conquest and fully naturalised. (1) غول ġūl keeps the Arabic form and meaning 'demon, ogre'; the extended Persian sense 'a huge person, giant' is a native development from the folkloric image (Wiktionary's Persian section: 'ghoul, giant, monster'). (2) غائله ġāʾila is the feminine active participle of the same hollow verb, غائلة 'that which snatches away' → 'calamity, sudden misfortune, trouble'; Dehkhoda and Amid both refer it to غول with the sense 'sudden seizure, destruction, affliction', and modern Persian uses it in غائلهٔ ... را خواباندن 'to quell a disturbance'. Nourai's transliteration 'ğâeleh' renders the Persian pronunciation ġāʾele of غائله. (3) مغیلان moġīlān is Arabic أمّ غیلان umm ġaylān contracted in Persian mouths: the initial أُمّ is reduced and univerbated with the following word (umm-ġīlān > muġīlān > moġīlān), so the tree name became a single Persian word for the desert thorn-bush of the Hejaz pilgrimage route — the خار مغیلان of Hafez's line quoted in the chart. Mo'in's dictionary marks it \\\"[ع.] امّ غیلان، درختچهٔ خاردار که در بیابان‌ها می‌روید\\\" and Borhan-e Qate' p.2023 says of it \\\"نام درختی است خاردار و بعربی آنرا امّ‌غیلان خوانند\\\".\",\n  \"derivation_fa\": \"هر سه واژه وام‌واژهٔ عربی‌اند که پس از اسلام وارد فارسی شده‌اند. «غول» به همان صورت و معنای عربی مانده و معنای افزودهٔ «آدم درشت‌هیکل» تحول معنایی درون‌فارسی است. «غائله» اسم فاعل مؤنّث همین فعل است (غائلة «رباینده») که در فارسی به معنای «فتنه، گرفتاری، بلای ناگهانی» به کار می‌رود؛ دهخدا و عمید نیز آن را به ریشهٔ «غول» بازمی‌گردانند. «مغیلان» کوتاه‌شدهٔ «أمّ غیلان» است: در تلفّظ فارسی جزء نخست فروکاسته و با جزء دوم یکی شده است (umm-ġīlān > moġīlān)، و همین «خار مغیلان» است که در بیت حافظ آمده است. معین ذیل مغیلان می‌نویسد: «(مُ) [ع.] (اِ.) امّ غیلان، درختچهٔ خاردار که در بیابان‌ها می‌روید» و برهان قاطع (ص ۲۰۲۳): «نام درختی است خاردار و بعربی آن‌را امّ‌غیلان خوانند». ادعای نورایی درست است.\",\n  \"sources\": [W_GHUL, W_UMM, A_MOGH, A_GHAE],\n  \"ref_check\": [\n    FVA304,\n    {\"ref\": \"MON:4261\", \"status\": \"supports\",\n     \"note\": \"The 6-vol Amir Kabir Farhang-e Farsi is not on disk with its printed pagination, so p.4261 itself could not be turned; but the text of Mo'in's entry, read through abadis.ir (بخش فرهنگ معین), is: \\\"مغیلان (مُ) [ع.] (اِ.) امّ غیلان، درختچهٔ خاردار که در بیابان‌ها می‌روید\\\" — the [ع.] tag and the explicit امّ غیلان are precisely the claim of Nourai's arrow. Given that m- words fall in Mo'in's third lexicon volume, p.4261 of the continuous pagination is in the right place.\"},\n    {\"ref\": \"BQT:2023\", \"status\": \"partial\",\n     \"note\": \"Verified on the page image (BQT_v4_picofile.pdf pdf page 106, printed ۲۰۲۳; saved as sources/refs/ocr/BQT/2023.png / 2023.vision.txt). It carries \\\"مغیلان - با لام بر وزن سلیمان، نام درختی است خاردار و بعربی آنرا امّ‌غیلان خوانند\\\" (with the footnote \\\"رک: تاج‌العروس ج۲ ص۱۹۰ «طلح»\\\") plus مغیلان باستان and مغیلان‌گاه. So it supports the third word only; غول and غائله are in the غ section of vol.3, not on this page.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"BQT\", \"where\": \"Borhan-e Qate', ed. Mo'in, p.2023 s.v. مغیلان (vol.4 scan, pdf page 106)\",\n     \"stance\": \"supports\",\n     \"note\": \"\\\"مغیلان - با لام بر وزن سلیمان، نام درختی است خاردار و بعربی آنرا امّ‌غیلان خوانند\\\"; the following entries مغیلان باستان and مغیلان‌گاه show how thoroughly the word was naturalised.\"},\n    {\"src\": \"MON\", \"where\": \"Mo'in, Farhang-e Farsi s.v. مغیلان, read via abadis.ir\",\n     \"stance\": \"supports\",\n     \"note\": \"\\\"(مُ) [ع.] (اِ.) امّ غیلان، درختچهٔ خاردار که در بیابان‌ها می‌روید\\\"; Dehkhoda on the same page adds \\\"مأخوذ از تازی، درختی خاردار که در مصر و عربستان فراوان\\\" and explains امّ غیلان as 'mother of demons'.\"},\n    {\"src\": \"PLA\", \"where\": \"Asbaghi, Persische Lehnwörter im Arabischen — grep 'ġūl'/'gul'\",\n     \"stance\": \"silent\",\n     \"note\": \"Asbaghi lists only Persian → Arabic loans and has no غول, i.e. no support for the opposite direction of borrowing that Devic once suggested.\"},\n    {\"src\": \"AFM\", \"where\": \"Addi Shir — grep غول/غيلان/مغيلان in AFM_pages.txt\",\n     \"stance\": \"silent\",\n     \"note\": \"No entry; Addi Shir does not treat غول or مغیلان as Arabicised Persian.\"}\n  ]\n },\n {\n  \"id\": 3, \"lang\": \"English\", \"words\": \"algol; ghoul\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"Both are Arabisms, but by very different routes. ALGOL (β Persei) is the Arabic star-name رأس الغول ra's al-ġūl 'the head of the ghoul' — Ptolemy's Gorgon's head that Perseus holds — shortened in the medieval Latin star lists to al-ġūl and current in English from the late 14th century; Ideler and Lammens (via Lokotsch no.741) note that the name stuck because the star's brightness visibly changes every three days, so it looked 'demonic'. Klein p.48: \\\"Algol... Lit. 'the Demon Star', fr. Arab. al-ghūl, 'the demon', fr. al-, 'the', and ghūl, 'demon'.\\\" GHOUL is a literary import of 1786: William Beckford's oriental novel 'Vathek' took it from the French goule of Galland's and Petis de la Croix's Arabian Nights, ultimately Arabic غول ġūl (Lokotsch: \\\"hieraus frz. la goule 'ein Ungeheuer'; aus dem ar. Plur. ġailān ergab sich frz. gailan\\\"). The two English words are therefore doublets of one Arabic noun, exactly as Nourai's box implies by putting them together under KLN:48,655.\",\n  \"derivation_fa\": \"هر دو واژهٔ انگلیسی از همان «غول» عربی‌اند ولی از دو راه. Algol نام ستارهٔ بتای برّساوش است، کوتاه‌شدهٔ «رأس الغول» (سر غول = سر مدوسا در دست پرسئوس)، که از راه فهرست‌های اختری لاتینی قرون میانه در سدهٔ چهاردهم میلادی به انگلیسی راه یافت؛ این نام را از آن رو بر آن نهادند که روشنایی‌اش هر سه روز تغییر می‌کند. ghoul وام‌واژه‌ای ادبی و متأخر است: در ۱۷۸۶ ویلیام بکفورد در رمان شرقی‌ماب «Vathek» آن را از goule فرانسوی (ترجمهٔ هزار و یک شب گالان) گرفت. کلاین (ص ۴۸ و ۶۵۵) هر دو را دقیقاً همین‌گونه می‌آورد؛ ادعای نورایی و ارجاعش هر دو درست است.\",\n  \"sources\": [E_GHOUL, W_GHUL],\n  \"ref_check\": [\n    {\"ref\": \"KLN:48,655\", \"status\": \"supports\",\n     \"note\": \"Both pages check out in the 1966 two-volume Klein. p.48 (KLN_1966.txt line 2184, leaf 37, whose running number is 49): \\\"Algol, n., a fixed star in the constellation Perseus (astron.) — Lit. 'the Demon Star', fr. Arab. al-ghūl, 'the demon', fr. al-, 'the', and ghūl, 'demon'. See ghoul.\\\" p.655 (line 16106, leaf 353, running numbers 653-658 on leaves 353-355): \\\"ghoul, n., an evil demon who robs graves and feeds on the dead. — Arab. ghūl, fr. ghāla, 'he took suddenly'. Cp. Algol.\\\"\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"LKT\", \"where\": \"Lokotsch no.741 'Ar. ġūl', p.59 (LKT.txt line 1807)\",\n     \"stance\": \"supports\",\n     \"note\": \"\\\"...hieraus frz. la goule 'ein Ungeheuer'... — Ġūl ist auch die Bezeichnung der Meduse; rās al-ġūl 'Medusenhaupt' wurde wegen des Wechsels seiner Lichtstärke der Stern β Persei genannt; hieraus der Sternname Algol.\\\"\"},\n    {\"src\": \"DEV\", \"where\": \"Devic, Dict. étym. des mots français d'origine orientale, s.vv. Algol and Goule (DEV.txt lines 398, 1436)\",\n     \"stance\": \"partial\",\n     \"note\": \"\\\"Algol... C'est l'arabe al-ġwûl, le même dont nous avons fait goule... Les Arabes appellent ras al-ġhoul, tête de la goule, la tête de Méduse que Persée tient suspendue à la main.\\\" Supports the route, but Devic adds \\\"Ghoul est d'origine persane\\\" — an 1876 guess with no Persian etymon behind it, rejected by Klein, Pihan, Lokotsch and Wiktionary, all of whom keep ġūl inside Arabic ġ-w-l.\"},\n    {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century Dictionary s.v. ghoul (WEB_vol1.txt line 81705)\",\n     \"stance\": \"supports\",\n     \"note\": \"\\\"ghoul (gōl), n. [Ar. ghūl, a demon of the mountains]\\\" — same Arabic etymon, slightly different gloss of the demon.\"},\n    {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict. (SKT.txt line 23616)\",\n     \"stance\": \"partial\",\n     \"note\": \"Skeat has no entry for ghoul but lists it in his tally of words of Persian/oriental origin (\\\"...divan, durbar, firman, ghoul, houri...\\\"), i.e. he records the borrowing without an etymology.\"}\n  ]\n }\n]\n\nout = {\n \"pdf_page\": 201,\n \"book_page\": 171,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-06\",\n \"entries\": [entry3, entry4]\n}\nimport io\nwith io.open('data/verification/page-201.json','w',encoding='utf-8') as f:\n    json.dump(out, f, ensure_ascii=False, indent=1)\n    f.write('\\n')\nprint('written')\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk201.py"
}
```


### [2026-09-06T15:09:32.760Z] TOOL RESULT

```
written
```


## [2026-09-06T15:09:37.789Z] TOOL CALL #61: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-201.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 201"
}
```


### [2026-09-06T15:09:40.018Z] TOOL RESULT

```
JSON OK
nodes verified: 7/7
node verdicts: {'plausible': 2, 'confirmed': 5}
root verdicts: {'plausible': 2}
ref checks: {'supports': 4, 'not_found': 3, 'partial': 2, 'not_checked': 2}
books consulted: {'partial': 3, 'supports': 14, 'silent': 8} | by book: {'ISS_alt_DKS': 3, 'BQT': 2, 'LKT': 2, 'BRT': 1, 'AVG': 1, 'PHD': 1, 'NYB': 1, 'HUB': 1, 'HRN': 1, 'ARY': 1, 'SOD': 1, 'HENNING': 1, 'KLN': 1, 'PHN': 1, 'AFA': 1, 'MON': 1, 'PLA': 1, 'AFM': 1, 'DEV': 1, 'WEB': 1, 'SKT': 1}
```


## [2026-09-06T15:09:49.668Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"AVG:\"; grep -c -i \"gavasna\\|gauuasna\" AVG.txt\necho \"ARY:\"; grep -c \"گوزن\\|کوزن\" incoming/ARY/ARY_pages.txt incoming/ARY/ARY_latin_index_pages.txt\necho \"PLA gul:\"; grep -n \"ġūl\\|Gul\\b\\|ġul\" incoming/PLA/PLA_pages.txt | head -3"
}
```


### [2026-09-06T15:09:49.752Z] TOOL RESULT

```
AVG:
0
ARY:
incoming/ARY/ARY_latin_index_pages.txt:0
incoming/ARY/ARY_pages.txt:0
PLA gul:
```


## [2026-09-06T15:10:08.802Z] AGENT

Done. `/home/sfmqrb/git/rishe/data/verification/page-201.json` written; `verify_check.py 201` reports **7/7 nodes, 0 PROBLEM lines** (5 confirmed, 2 plausible; both roots plausible; ref checks: 4 supports, 2 partial, 3 not_found, 2 not_checked).

**Page 201 (book p. 171)** — 3 redirects skipped (Gurdus, Gurô, Gurr); 2 real entries.

- **Gŭysna "deer"** — all words genuine (Khot. ggūysna-, Av. gauuasna-, Sogd. γ'wzn, MP gawazn, NP گوزن), all under Proto-Iranian *gavazna-. Root marked *plausible*: Nourai puts the Khotanese **reflex** in the root box and hangs Avestan under it; modern view makes all five parallel branches. Av. node *plausible* because Bartholomae glosses gavasna- "-?-" (hapax in the Pahlavi gloss to Yt 10.128); the meaning is Bailey's comparative inference. Sogdian node *plausible*: the citable Sogdian form is γ'wzn (Gharib 4079), not Nourai's "gwzn" (which is actually Bailey's Zor.P./Khwar. shape).
- **Ğ.v.l "to take suddenly"** — root marked *plausible* only because the label should be "Arabic", not "Semitic": غ-و-ل has no accepted Proto-Semitic cognate set (Akkadian gallû is a different, Sumerian-derived root; Fraenkel doesn't list it). All 3 nodes confirmed: ġāla > ġūl, umm ġaylān > Persian مغیلان, غائله; English Algol (< رأس الغول, late 14c) and ghoul (Beckford's *Vathek* 1786 via Fr. goule).

Citation errors **in the printed book** (verified against the page image — the JSON extraction is faithful in every respect):
- `BQT:1754` (nodes 2 and 3 of entry 3) should be **BQT:1854** — p. 1754 is in the کیس/گیس stretch; گوزن with its stag woodcut and Mo'in's footnote "پهلوی gavâzan «اونوالا ۸۷»" is on p. 1854.
- `SOD:180` should be **SOD p. 162 / entry 4079** — p. 180 has γwys-/γwyc- entries.
- `UNV:56` unconfirmable (1963 Paris ed. unavailable); the word is in the 1917 ed. at §30, p. 21, and Mo'in cites "Unvala 87" for the same form.
- `FVA:304` not checkable — no digital copy of Nahvi's dictionary exists.

**No extraction errors to fix.** New artifacts: `sources/refs/ocr/BQT/1854.{png,vision.txt}`, `2023.{png,vision.txt}`, `sources/refs/ocr/BOOK/201.png`, and 6 archived web sources (Wiktionary گوزن/غول/أم غيلان, Etymonline ghoul, abadis مغیلان/غائله). Nothing committed.
