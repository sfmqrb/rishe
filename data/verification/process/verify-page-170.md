# Verification process log — verify-page-170


## [2026-09-05T20:38:14.566Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 170 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-170.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-170.json. Write /home/sfmqrb/git/rishe/data/verification/page-170.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 170` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T20:38:16.159Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T20:38:16.865Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T20:38:16.881Z] TOOL RESULT

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


## [2026-09-05T20:38:16.968Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-170.txt"
}
```


### [2026-09-05T20:38:16.980Z] TOOL RESULT

```
1	=== PDF page 170 (book page 140) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Geme, Gem : to marry  (refs POK:369)
4	#1 (parent #0) [Avestan] refs=POK:369; HRN:117; IEC:402 | jâma : kinship (daughter) ; zâmâ-tar : son-in-law ☞Ter 3
5	  #2 (parent #1) [Pahlavi] refs=MON:1487 | dâmât : bride groom
6	    #3 (parent #2) [Persian] refs=BQT:817 | dâmâd «داماد» : son-in-law, bride groom
7	#4 (parent #0) [Sanskrit] refs=IEC:402 | jâmâ : daughter
8	#5 (parent #0) [Greek] refs=AHD | gamos : wedding
9	  #6 (parent #5) [English] refs=AHD | -gamy, gamo-, polygamy
10	--- entry 1 ---
11	ROOT Geme-tar -> redirect to Ter 3
12	--- entry 2 ---
13	ROOT Gen -> redirect to Gnô
14	
```


## [2026-09-05T20:38:20.026Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-170.json",
 "description": "Read page 170 source JSON"
}
```


### [2026-09-05T20:38:20.070Z] TOOL RESULT

```
{
  "pdf_page": 170,
  "book_page": 140,
  "entries": [
    {
      "root": {
        "name": "Geme, Gem",
        "lang": "Indo-European",
        "refs": "POK:369",
        "gloss": "to marry"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:369; HRN:117; IEC:402",
          "words": [
            {"translit": "jâma", "gloss": "kinship (daughter)", "script": null},
            {"translit": "zâmâ-tar", "gloss": "son-in-law", "script": null, "see": ["Ter 3"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "MON:1487",
          "words": [
            {"translit": "dâmât", "gloss": "bride groom", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "BQT:817",
          "words": [
            {"translit": "dâmâd", "gloss": "son-in-law, bride groom", "script": "داماد"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "IEC:402",
          "words": [
            {"translit": "jâmâ", "gloss": "daughter", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD",
          "words": [
            {"translit": "gamos", "gloss": "wedding", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "-gamy, gamo-, polygamy", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {"name": "Geme-tar", "redirect": "Ter 3"},
      "nodes": []
    },
    {
      "root": {"name": "Gen", "redirect": "Gnô"},
      "nodes": []
    }
  ]
}
```


## [2026-09-05T20:38:20.728Z] TOOL CALL #4: Bash

```json
{
 "command": "sed -n 1,200p data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-05T20:38:20.763Z] TOOL RESULT

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


## [2026-09-05T20:38:43.191Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','HRN','IEC','MON','BQT','AHD','BRT','PHD','NYB','HUB','SYN','WLD','ARY','KLN']:\n    v=d.get(k)\n    print('==',k, json.dumps(v,ensure_ascii=False)[:700])\n\""
}
```


## [2026-09-05T20:38:43.300Z] TOOL CALL #6: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo --- && head -c 3000 data/verification/page-124.json"
}
```


### [2026-09-05T20:38:45.834Z] TOOL RESULT

```
== POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index 
== HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the 
== IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Reconstruct
== MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol 
== BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.c
== AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifie
== BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between 
== PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<ident
== NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Nourai's 'NYB' nu
== HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by parag
== SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<i
== WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.39015066210397 (browser only from this host)", "identifier": "in.gov.ignca.20339 (Band 3); also in.ernet.dli.2015
== ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image", "local_file": ["/home/sfmqrb/git/rishe/
== KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO pri
```


### [2026-09-05T20:38:45.880Z] TOOL RESULT

```
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
page-140.json
page-141.json
page-142.json
page-143.json
page-144.json
page-145.json
page-146.json
page-147.json
page-148.json
page-150.json
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
      "note_fa": "خودِ ریشه کاملاً درست است: پوکورنی در صفحات ۲۳۵–۲۳۹ مادهٔ dʰē-2 را با معنای «نهادن، قرار دادن» آورده و واتکینز در پیوست فرهنگ American Heritage همین را می‌گوید؛ مواد ایرانی نمودار (dāta-، ni-δaiti-، gao-δana-، dāman-) هم عیناً از همین مادهٔ پوکورنی است. سه لغزش در بخش یکم هست: ۱) صورت اوستایی «پنام» paiti.dāna- است نه paiti-dāma — خطای چاپی کتاب؛ ۲) apadāna پارسی باستان است نه اوستایی و معنایش «کاخ، تالار بار» است؛ ۳) پهلوی dastwar هیچ ربطی به این ریشه ندارد و هرن (ص ۱۲۷) و نیبرگ (ج۲ ص ۶۱) آن را ا
```


## [2026-09-05T20:38:51.833Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"zāmātar\\|zamatar\\|zāmātār\\|jāmātar\\|jamatar\" POK_full.txt | head -20; echo \"=== POK_01 leaf ===\"; awk 'BEGIN{RS=\"\\f\"} NR==378' POK_01.txt | head -60"
}
```


## [2026-09-05T20:38:52.599Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"gem\" AHD_watkins1985.txt | head -30"
}
```


### [2026-09-05T20:38:53.944Z] TOOL RESULT

```
35032:Material: Old Indie yaAa-/?' suitor, lover' {*gm-r6-s?)\ Old \r\(X\c jamatar-, Avestan zamatar- 
=== POK_01 leaf ===
```


### [2026-09-05T20:38:53.986Z] TOOL RESULT

```
<persisted-output>
Output too large (31.9KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/tool-results/bk5h50y3h.txt

Preview (first 2KB):
229:extended form. A form with an extension or enlargement, written solid.
234:gemination” (doubling of the final conso- nant), written solid.
479:gar-. To call, cry. Expressive root. 1. Germanic *kar6, lament, hence grief, care, in: a. Old English cearu, care: CARE; b. adjective *karagaz, sorrowful, in Old English cearig, sorrowful: CHARY. 2. Celtic suffixed form *gar-(s)mn in Gaelic gairm, shout, cry, call: SLOGAN. 3. Suffixed form (with expressive gemination) *garr-iyo- in Latin garrire, to chatter: GARRULOUS. [Pok. gar- 352.]
489:*klai-ni-, bright, pure, in: a. Old English cléne, pure, clean: CLEAN; b. Old English clénsian, to purify, cleanse: CLEANSE. 2. Extended and suffixed zero-grade form *glo-nd in Greek gléné, eyeball: EUGLENA. [Pok. gel- 366.] gel-3. Cold; to freeze. 1. Germanic *kaliz, coldness, in Old English c(iJele, chill: CHILL. 2. Germanic *kaldaz, cold, in Old English ceald, cold: COLD. 3. Germanic *kédl-, cool, in: a. Old English cdl, cold, cool: cooL; b. Germanic *koéljan, to cool, in Old English célan, to cool: KEEL’. 4. Suffixed form *gel-d- in Latin geldre, to freeze: GELA- TIN, GELATION, JELLY; CONGEAL. 5. Suffixed form *gel-u- in Latin gelu, frost, cold: GELID. 6. Probably suffixed zero-grade form *gl-k- in Latin glaciés, ice: GLACE, GLACIAL, GLACIATE, GLACIER, GLACIS. [Pok. 3. gel()- 365.] gembh-. Tooth, nail. I. Suffixed o-grade form *gombh-o-. 1. Germanic *kambaz, comb, in: a. Old English camb, comb: COMB, KAME; b. Old High German kamb, comb: CAM; c. Germanic denominative *kambjan, to comb, in Old English cemban, to comb: OAKUM, UNKEMPT. 2. Greek gomphos, tooth, peg, bolt: GoMPHosIS. II. Per- haps Germanic *kimb- in Old English cim-, cimb-, rim (only in compounds): CHIME?. III. Possibly suffixed form *gembh-ma in Latin gemma, bud, hence gem: GEM, GEMMA, GEMMATE, GEMMULE. [Pok. gembh- 369.] geme-. To marry. Suffixed zero-grade form “gmoa-o- in Greek gamos, marriage: GAMETE, GAMO-, -GAMOUS, -GAMY; GAMOSEPALOUS. [Pok. gem/(e)- 369.] gen-. To
...
</persisted-output>
```


## [2026-09-05T20:38:58.203Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '35010,35060p' POK_full.txt"
}
```


### [2026-09-05T20:38:58.254Z] TOOL RESULT

```
range ' (but about ndd. kimmesee above ur\6er gem-). Old English cemban. Old High 
German kemben ' comb' , Swiss chambe^ Kamm bei Hahnen '; in addition Bavarian sich 
kampe/n \quarre\ =) tear, rend, fight, squabble', with expressive p; 

Tocharian A kam, B /re/77e 'tooth'. 

Under a meaning mediation 'tooth' - ' like a small tooth of protrudent plant shoot ' one 
lines up the family of Lithuanian zembu, zembet/" gerrr\\nate' , Old Church S\a\/\c pro-zgbat/, 
pro-zgbngt/6s., Latin gemma {*gerrb^na) ' eye or bud in the grapevine or in trees; 
gemstone, precious stone ', Old High German champ ' the stalk of a cluster of grapes and 
similar plants; a bunch of berries, cluster of grapes ', Modern High German Kamm 
('dentated device '); the Lithuanian glottal stop is explainable through a lengthened grade 
present formation like sergmi, gelbmi, gelbu. 

References: WP. I 575 f., WH. I 588, Trautmann 369, Specht Dekl. 86 f. 
See also: see also under gep(h)-, geb^-. 
Page(s): 369 

Root / lemma: gem(e)- 

Meaning: to marry 

Material: Old Indie yaAa-/?' suitor, lover' {*gm-r6-s?)\ Old \r\(X\c jamatar-, Avestan zamatar- 

' man's daughter ', created after other relationship names in -/sa- extension, with a the 

second syllable after matar-; the basic root has been abbreviated *Jama-, compare 

Avestan zamaoya-^ brother of son-in-law ', also Old Indicya/r?/-/?' connected, related by 



blood ', fern, nachved. " feminine relatives, esp. daughter-in-law ', ved. vf-Jami-h) " relative 
by marriage \jama^ daughter-in-law '; 

gr YOM^w " marry ' (Akt. of man, husband, Med. from the wife, woman), eyriMCi (Doric 
£yc(|ja), y£yapr|-MC('; YC(M£Tr|<; " husband ', yapeTn, yapsiK;, -xboo, "wife", yapr|AiO(; " nuptial ', 
yapo(; m. " wedding '; yappp6(; {*gem-ro-) 'son-in-law'; 

Maybe alb. o'as/77e "wedding': gr. Ya(JO(; m. "wedding' common alb. gh- > o'-phoentic 
mutation. 

Latin gener-, /"ds. (for *gemer aiter genus, gens). 

References: WP. I 574 f., WH. I 590 f. 
Page(s): 369-370 

Root / lemma: gen-1, gene- gne- gno- 

Meaning: to bear
```


## [2026-09-05T20:39:16.674Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT zamatar ===\"; grep -n -i \"z[āa]m[āa]tar\\|zamaoya\\|zāmaoya\" BRT.txt | head -20; echo \"=== PHD damad ===\"; grep -n -i \"d[āa]m[āa]d\" PHD.txt PHD_mackenzie.txt | head -20; echo \"=== NYB ===\"; grep -n -i \"d[āa]m[āa]t\\|dʾmʾt\" NYB_vol2_glossary.txt | head"
}
```


### [2026-09-05T20:39:16.746Z] TOOL RESULT

```
=== BRT zamatar ===
=== PHD damad ===
PHD.txt:308:dahigān [dhywk’n' | N dihgān] countryman, farmer. dahliz [d^hlyc | (M dhryz), N ~] portico. dahm [d?hm] virtuous, pious; a full member of the Mazdean community, initiate. dahom [hwm | M dhwm, N ~] tenth. dalman [d”/mn' | N dál(man)] lammergeyer, eagle. dam- , ~išn, v. daftan. īdām [d”m | = M] creature, creation. здат [Pm | = M, N ~] tame animal. здат [d’m | P d’mg, N ~] net, snare, trap. dāmād [d?r?t! | M 424, N ~] bridegroom, son-in-law. ~ih: condition of a bridegroom, son-in-law. daménag [dmynk'] fan. damidan [dmytn'] = daftan. dān-, —išn, v. dānistan. -dàn [-d’n' | = M, N ~] suffix, -holder, -container. dàn(ag) [d”x(k)! | N ~a] seed, grain. Н dānāg [4>рА! | М dwg, N dana] knowing, wise. ША zn kh ~ih: knowledge, wisdom. ar dandàn [KK A < А kk’; dnd’n' | = M, N ~] tooth. dānistan, dān- [YDOYTWN-stn' < A У yd‘; d’n-stn' | M d^n-ystn, N ~] know. ~ign: knowledge. ~i8ndmand [- отпа) knowing. dar [BBA < A bb’; dl | M dr, N =] door; palace; chapter, subject. dar [d?] | M d@’r-, N ~] tree, gallows; wood. dar-, -išn, v. dāštan. -dār [-d'/| M -d’r, N ~] suffix, -holder, -keeper. Р darāy [dPg | J ~, N darāy] bell. *darak [dlk'] section, paragraph. darband [B B Abnd | N ~] gate. darbās [dips] palace. dard [dit! | M drd, N ~] pain. ~отапа [отла | M -wmnd, N ~mand] ill, suffering. dārēn [d'/yn! | М drwyn] wooden. darģāh [dig’s | N ~] doorway. dargardih [d*/krtyh | M d’rgyrdyh] crucifixion. dar-handarzbed [BB A-, dl-hndlcpt'] chamberlain. darigbed [dlykpt'] palace superintendent. *darmag [d?/mk!'] fine, delicate. darmān [dim?n! | M drmn, N ~] remedy, medicine. darridan, darr- [SDKWN-tn! < A V sdg; dl-ytn! | N <] split, tear. dàrüg [d"Iwk! | М drwg, N dari] drug, medicament. dār-wāzīg [Tlw cyk! | N dár-bàz] (pole-)acrobat. darz [dlc | N ~] seam. ~ig [-уА! | N darzi] tailor.
PHD.txt:1087:bridegroom damad.
PHD.txt:3731:son-in-law damad.
PHD.txt:5550:dāmādīh
PHD.txt:5551:dāmād
PHD_mackenzie.txt:1860:damad [d'm't I M d'm'd, N ,...,] bridegroom, son-in-law.
PHD_mackenzie.txt:6080:boldness wistaxih.                     bridegroom damad.
=== NYB ===
186:QDMTH (Prth): QODAM T EH in his presence, OAram QODAMAT prep. before, in the presence of, more common QODAM, v. MDM QYN? (Prth): v. KYN?
```


## [2026-09-05T20:39:18.416Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN grep damad ===\"; grep -n -i \"dâmâd\\|dāmād\\|damad\\|dàmàd\" HRN.txt | head -20; echo \"=== HRN leaf 138 (p.117) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==139' HRN.txt | head -70"
}
```


### [2026-09-05T20:39:20.040Z] TOOL RESULT

```
=== HRN grep damad ===
=== HRN leaf 138 (p.117) ===
— 117 —
Sicherheit etc.*, ursprünglich 'hüte dich vor diesem,
halte dich von diesem zurück', wovon dann zTnharT
und nach dem FS sogar zinhariden gebildet wurden?
Allerdings wüsste ich dann nicht die Messung von
zinhar als Amphimacrus bei FirdüsT zu erklären, die
mir jedenfalls (vergl. Indog. Forsch. II, 185) für
iranischen Ursprung des Wortes zu sprechen scheint
(anders Nöldeke, Pers. Stud. II, 46, dessen Erklärung
aus dem aramäischen *inT, wie er selbst zugiebt,
wegen des t Bedenken erregt).
528. danen 'Geschenk, Gabe'.
g. däsn.
phlv. dah(i)Sn ; vergl. padäsn (No. 265*'^'').
529. däy 'Brandmal*, dey.
aw. daya-\ phlv. däy (vd. 15 (48) Gl.); ai. ddha-
'Brand*, skr. ni]däghd' 'Hitze*, Sommer'; lit. dagä 'heisse
Zeit, Sommer.
LW. kurd. afy. däy; bei. däg, n. day (52).
580. {\)ääm 'Haustier, zahmes Tier.
ai. l/"rfam-, d!(^wyci^i"zähmen, zahm sein'; gr. öujiidATjQ
'Stier; lat. domäre; air. dam 'Ochs, Stier ; got. ga-
tamjan, nhd. zahm,
oss. vergl. domun 'zähmen' (108).
phlv. dam 'Geschöpf (aw. däman-) ist im Np. auf-
gegeben.
531. {?)däif¥i *Netz'.
ai. däman- 'Band, Fessel*.
afy. lüm; arm. LW. (?) damK 'N(?tz'.
532. dämäd 'Schwiegersohn; Bräutigam (Vis und Käniin,
S. 46, Vers 4 v. u. folg.)'.
g. zümäd; gel. zamä, zemö Schwager'; Käs. zUmo,
zümod, zümoi,
aw. zämätar- 'Schwiegersohn'; phlv. dämät; ai.
jdwätar-,
kurd. zawä; af/. zäm, zümgai; bei. zämcLS^, n. Jan-
wa^ (420).
```


## [2026-09-05T20:39:33.114Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT variants ===\"; grep -n \"zamatar\\|zãmãtar\\|zámátar\\|zàmàtar\\|zäraätar\\|Schwiegersohn\" BRT.txt | head -20"
}
```


### [2026-09-05T20:39:33.155Z] TOOL RESULT

```
=== BRT variants ===
11618:(Za/*äoTt75)  zweier  Gläubiger  r)  des  Mi- nisters Visiäspai,  Schwiegersohns  Zara- &aÄr<is">,  Bruders  FraSao^tra%  aus  der ^»j^flfamilie:  °pahe  AvSvaAe  (sd.)  Yt y- 1 03  j  — ya^rS  vS  a/sman[{sd.)  sSrtghänT ..  'pa  (VS.)  hvs^va  (sd.)  Y.  46,  17; 4g.  9 ;  —  tarn  ciitltn  'fS  hvB.gvS  tsldü :^armh  (sd.)  ala  vtnnti  Y.  5/.  18;  — yS  . .  bar?sma  */rasttrmte  ya%a  asava  °p5 */rastfrinaSa  ra/u/rif  li.Sg;  —  amava ya^a  °pü  Az.  2;  2;  Vyt_j;  —  yävaranä *frasaoslra  •/s(ND.)  ..ta  vannilcä (sd.)  . . Y./2, 7;  —  ao/i/a  tT  zarai:uslra  fralaos- tralibya  'pa^bya  Vyt.  //;  —  tarn  (näml. andvltn)  yazaia  -ps  yat  spShm  pairi.- avalnal . .  drvatqm  Yt  5.  68,  a)  °pafie aparamtahe  (sd.)  asaonS  Yt  ij.  127.
28086:AbleiL  aus  "säma-  m.,  svl.  ajmälat-;  afy. lümt).  iSulT.  (ar.  ?I3.)  und  iKed.  s.  tüitya-, itülmya-  und  WH.'Or.'  %  2228c.  —  I'ö.: äämät  'Schwiegersohn'.  —  ■)  D.  i.  'zäniai/ya; %  36S.  13.  Die  Hdss.  haben  i  statt  y.  — ')  Das  nicht  mit  Ggr.  ABayrAW.  20.  t.  194 gleich  j.  ämälar-,  np.  dämäd  gesetzt  werden kann;    dafür  wäre  *:ümör  zu  erwarten,    vgl.
28087:•  j.  zämätar-  m.  'Eidam,  Schwiegersohn': aäai>iiva  (,rä.m\.  asti  mihrB)  antan  'tara (AD.)  :^asura  ".  .  zwischen  Eidam  und Schwäher  Ytio.  116.
```


## [2026-09-05T20:39:33.821Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== IEC ===\"; grep -n \"jāmātar\\|jamatar\\|gemə\\|ĝemə\\|gamos\\|zamatar\" IEC.txt | head -20"
}
```


### [2026-09-05T20:39:33.872Z] TOOL RESULT

```
=== IEC ===
4008:gimol-, gimó, see geməl-, gemo
```


## [2026-09-05T20:39:44.107Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '28080,28092p' BRT.txt; echo \"=== find column marker ===\"; awk 'NR>=28060 && NR<=28100' BRT.txt | grep -n \"17[0-9][0-9]\\|16[0-9][0-9]\" | head"
}
```


## [2026-09-05T20:39:45.190Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 215 216 217; do echo \"=== IEC leaf $n ===\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' IEC.txt | grep -n -i \"gem\\|gam\\|jāmā\\|jama\" | head -20; done"
}
```


### [2026-09-05T20:39:45.938Z] TOOL RESULT

```
—  narqmca  'tanqmca  sqhyamnanqnt^a (sd.)  Y,  4-  S'i  —  ^^annatiuhaslimS  °tanqm Y.g.  4.  2)  'jetzt  vorhanden,  jetzig';  ya/ asti  airyanqm  dahyunqm  'tanqm  (GPf.) aziitanamca  (sd.)  Yt  ig.  56.
KompA.  —  ri'fP.  iura  V.  -.an-.  —  ai./i/a- Atlj.,    nip.  Siit;    rp.    vgl.  :.i</a.    —     Pü.;    :ä/,
•  j.  nsil  hväzaiö  nöii  "zäniti  FrD.  7.
•  j.  zänu.dräl|ah-  Adj.  (auch  fem.)  'im Vorstrecken  des  Kinns  bestehend':  aEvahe zl  .  .  anasaonS  v'l  (NSf.)  .  .  ü/riti^  (ßAy V.  16.  II.
*:iinav-  f.  'Kinn'');  vgl.  %\.  hänav-  f.,  np. zaiiiix.  —  Pii.;  züiiak  drahnäk.  —  ')  Vor- strecken des  Kinns  bei  gleichzeitigem  Streifen des  llandiückens  vom  Ilats  her  nach  dem Kinn  tu  drückt  in  Italien  Geringschätzung aus.  —  >)  Das  ä  ist  aufrälÜg;  man  hat  das Wort  dirtim  mit  'Knie'  übersetit  —  lulelil Gdn.  SPreussAW,  ig.  414:  'Kniestoss' -  und zu  ai.  j'iinit  n.,  np.  zitiii  gestellt  Aber  Pü. spricht  nicht  dafür  j  'Knie'  wäre  zänüi.
•  j.  *zämaoya-"  m.  'Bruder  des  Schwieger- sohns': 'yö  F.  20.
AbleiL  aus  "säma-  m.,  svl.  ajmälat-;  afy. lümt).  iSulT.  (ar.  ?I3.)  und  iKed.  s.  tüitya-, itülmya-  und  WH.'Or.'  %  2228c.  —  I'ö.: äämät  'Schwiegersohn'.  —  ■)  D.  i.  'zäniai/ya; %  36S.  13.  Die  Hdss.  haben  i  statt  y.  — ')  Das  nicht  mit  Ggr.  ABayrAW.  20.  t.  194 gleich  j.  ämälar-,  np.  dämäd  gesetzt  werden kann;    dafür  wäre  *:ümör  zu  erwarten,    vgl.
•  j.  zämätar-  m.  'Eidam,  Schwiegersohn': aäai>iiva  (,rä.m\.  asti  mihrB)  antan  'tara (AD.)  :^asura  ".  .  zwischen  Eidam  und Schwäher  Ytio.  116.
a\.jii>Mä/ar-  m.,  np.  Jämäd'1.  —  Vgl.  iJi?ia&ya; —  ■)  Ein  et.  Versuch  bei  vünISradke  IF. 4.  SS.
•  j.  zävar-  n.  '(physische)  Krafl,  Stärke': 'var»  aojaiia  Yt  13.  i ;  10.  62,  F.  20\  —  : aojas'a  zavanca"^  Y.  72.  6;  7J.  8,  Yt. i,sz.  a)  insbes.  a)  der  Ftlsse^;  yat kl  da'i^at  .  .  patave  'vars  YL  16.  7 ;  Y.  ^. a8;  —  apa  pälayä  "var>  (näml.  barahi) Yt  ro.  23.  b)  der  Rosse:  'van  dayä' hitaiibyö  Y.  57.  26;  Yt  iO.  1 1 ;  —  yS  mqm
z«mana-  1690
(näml.  asp>m)  'vart  nötf  jaityehi  (sd.)  Y. II.  2;  —  haamS  aiibis  ysi  ,  .  hita  toxstnli (sd.)  .  .  'var>  aojBsca  baxiaiti  Y.g.  22. Vgl.  tavoA:  —  np,  vgl.  zör  (woiu  Hbm.  PSt. 273)-  —  P5-:  SÄ-«.  Sü.  :fräimii\  mit  der  Erl.: iti  pädayofi.  —  <)  Das  erste  a  nach  %  2g4.  3. —  1)  Die  selbe  Verbindung  auch  im  Mp., iB.  Bd.  7.  g;  ei  u  tlr.  —  3)  Vgl.  Sü.  und unter  aojah-.  —  *)  Wofür  auch  fälschlich z  n  a  r  (sÄÄr),  ebenso  wie  umgekehrt  i  n  r  (zSr) für  iohSjö-  vorkommt;  s.  DsT,  ZA.  /.  Lxxvi No.  3.     Vgl.  No.  5-    ~    5)  Wie  für  taArS-,
•  j.  zära-  m.  'Galle':  'ras(HS.ya  F.^g. Vgl.  gr.  x»^»,-,  Bthl,  ZDMG.  j;.  155;  s.  noch No.  i.  —  Pü.:  zahrat.  —  ")  Oder  ist  das Wort  als  zSt's  a  lu  denken  und  j  lu  S  J04 n.  2  lu  stellen?  Der  idg.  NS.  *iA^/d  wUre wie  gr.  i.f^  gebildet  (BB.  //.  119,  125)  und verhielte  sich  zu  *j;jr^/-  (Sp.  523  o,)  wie  gr. afp  zu  lat.  i^rd-i  zur  Anlautsdilferenz  s.  Ugv. Grdr.  />.  545.  \.a.t. /ellis  enihält  doch  eher altes  ida.lsln,  wie  So.MMERLatl.aut&t'ornient. 394  "'iU-
=== find column marker ===
31:z«mana-  1690
```


### [2026-09-05T20:39:47.474Z] TOOL RESULT

```
=== IEC leaf 215 ===
3:guom- (guomos, ios, us) ‘coming, going’. Cf. guem-, gum- and next Skt. gamah, adj. ‘going’; m. ‘departure’; SWG kim “fitting, proper; Li. gàmas ‘nature’; gamuüs ‘productive’; Latv. cf. ne-gants, adj. ‘ugly’, fr. *ne-guomtos
4:guom- (variant of guom- q. v.) Av. gamo “foot, pace’; Per. gam, d Gk. bo- mós ‘platform, altar”; OE cweme ‘pleasant, ac- , ceptable'
=== IEC leaf 216 ===
=== IEC leaf 217 ===
```


## [2026-09-05T20:40:01.943Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 214 215 216 217; do echo \"=== leaf $n ===\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' IEC.txt | head -c 1200; echo; done"
}
```


### [2026-09-05T20:40:03.697Z] TOOL RESULT

```
=== leaf 214 ===
ly, comely’; ON kominn, pp. as adj. “of such a state’; beside Icel. kyn (^won- der’: Gk. gán-). (For the Gk. phonol. cf. guné, gána, baná)
365
gumsKo, inceptive-progressive to gumio, q. v. WP I, 675 Skt. gáččhāmi, beside gaččhah (family, kind", cf. Li. gimtis, Latvian: dzimts *sex"): Gk. báske ‘he went’; Li. gimstu, Latv. dzimstu "am born?
gumster- (gumter-) (?) “belly, stomach’. Cf. gem- (gm-) Skt. jatháram (belly... Vedic: 'cavity); Gk. gaster; Lat. venter
gumstis, variant of gumtis, q. v. Skt. cf. A-gástih ‘supergod, Hercules; MHG, Du. komst
gumtis *going, coming'. See next. WP I, 675 Skt. gátih; Av. aiwi-gaitis “departure”; Gk. bá- sis; Phryg. cf. nibatismós Ca dance’. Hes.); Lat. cf. in-ventio; Go. ga-qumps “assembly”; OHG kumft; Li. gimtis ‘race, sex’; Latv. dzimts, id.
gumtes (come, gone; coming, going’. Cf. gumtis. Variant gumtus Skt. gatáh; Av. gata; Gk. batós; Lat. in-ven- tus; Go. -kunds, cpds.; Li. gimtas ‘born’; Latv. dzimts ‘inborn, native’; dzimta ‘birth’. Variant in *-us: Skt. gatüh; Ober, gathu- ‘place’; Av. gātus, id.; Pers. gàh, id.; Lat. cf. in-ventus; Li. cf. gimtüves 'anniversary'
gunå �
=== leaf 215 ===
e, wm. ‘burly fellow
guólos ‘ball, lump’. Cf. guouolos Gk. bólos “lump, sod"; Pol. gata ‘ball; testicle’; Ukr. cf. halka ‘ball’; Cz. hálka “gall on plants’; Ukr. cf. za-halom “altogether”, lit. sin a ball
guom- (guomos, ios, us) ‘coming, going’. Cf. guem-, gum- and next Skt. gamah, adj. ‘going’; m. ‘departure’; SWG kim “fitting, proper; Li. gàmas ‘nature’; gamuüs ‘productive’; Latv. cf. ne-gants, adj. ‘ugly’, fr. *ne-guomtos
guom- (variant of guom- q. v.) Av. gamo “foot, pace’; Per. gam, d Gk. bo- mós ‘platform, altar”; OE cweme ‘pleasant, ac- , ceptable'
367
guoros, à ‘swallowing; throat; food, herb, poison; glutton'. Cf. guer-, gur-. WP I, 683 Skt. garáh “drinking, swallowing; drink, poi- son'; cpds. -garah (as Lat. -vorus); galáh (throat, neck', of ambig. cons.); Av. garð (poison; ambig. in sense of *throat"); Arm. cf. orkor, o-st. (throat! w. vocalism of Gk. bo- reus?); Gk. borós ‘gluttonous; eater’; borá, f. “food; cf. hellé-boros (bot.) and perh. bórues (unnamed animals in Libya) beside e-gde in Kér-beros; Lat. -vorus in cpds., and various plant-names in ver-, see under guer-; perh. also bell
=== leaf 216 ===
küt, küte, s. & wm. (putty: G Kitt)
guóu-eda (-édis, -odà, -dā) ‘ox, cattle, beef, cattle-fodder'. Cf. ed- and guou-sth- Oss. qáwwaz, qwaz, Dig. $àwanz ‘hind, doe: Alb. gjedh “head of cattle"; ON kjot, ds kjotvi ‘flesh’; Sw. kött, Norw. kjótt, Dan. köd, id. (vocalism obscure); OCS govedo "oy: OCz. hovéda, hovedina, f. “beef” beside Cz. havéd ‘vermin’ :
guoueió ‘vow, declare’ Gk. cf. bou-lë (if for *guou-lēų ‘taking of re- solution’, cf. léu-) Lat. voveo; Li. gaviü, eti (‘fasť, lit. vow"); Latv. gaveju, et, id.
guóuolos (guəuəl-) “head of cattle; bull, ox, buffalo". WP II, 112 Skt. golah ‘bull’; Hind. gaur ‘wild bull, bison’; Oss. gal ‘ox; bull; Gk. boübalos ‘buffalo’; Lat. (LW fr. Gk) bübalus, id., beside It. (from Umbrian) bufolo, id.; MIr. büáaball, id.; W bual, id. (both fr. Lat. but cf. also Ir. bólach, bólacht, bualacht ‘livestock’, fr. *guouol-a$-
369
to-); Alb. (LW via Lat.) buell, buall “buffalo”; Blg. güla ‘herd’. Of similar vocalism cf. Gk. bólos ‘sod’; Ir. bualtach *cowdung'
(guðuər (coll. type) ‘cattle’. Cf. guouolos. Only in Ir. buar cattle")
guouil- Lat. bovile (cowshed'; 
=== leaf 217 ===
'cattle-Crun' beside -pót&, -páte (in ois- “dung on sheep's rear); isophonic in Gk. boütes ‘herdsman’; bousé “female slave’ (used as cowgirl); Hes. bousía ‘a root resembling turnip’, MHG quot, quát, OE cwead, OFris. quad ‘dung’; adj. ‘bad’; LG (z-gde) küt ‘filth from entrails’; (Gmc. forms fr. *-dh- or *-tós, -tóm); Blg. cf. gutav ‘bad’; Li. gúotas “herd of small animals’; guotë, guo- Cià “orange-agaric”
guðutros, om (guutro-) (an association of COWS) Skt. gotrám 'cowshed'; LLat. cf. botrix *excre- ment’; W budr ‘filthy’
gur-, see gurus. A zero-gde element in Gk. br-iaros, br-ithüs, br-ómos; Lat. br-ütus; Latv. gr-üts
guràun, guràuon, guràán- ‘heavy stone, mill- stone'. WP I, 685. Cf. gurus Skt. gravan “heavy stone’; Per. garan, giran “heavy, dear; Arm. erkan ‘mill’; MIr. bráu, bró, gs. brón, id. beside Mir brón “burden, grief; W breuan ‘handmill’; Br. bréw ‘mill’. Cf. Lat. variant gravamen ‘grievance’
gurebhos, -es-, (gurebhmn, -ón) ‘foetus, in- fant, young animal’. WP I, 689 Gk. bréphos, n.; MHG krébe (?) ‘intestines’; OCS Zrébe beside Cz. hříbě *foal". (For Skt. gárbh
```


## [2026-09-05T20:40:13.750Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} /(^|\\n)[[:space:]]*40[0-4][[:space:]]*(\\n|$)/{print \"LEAF\",NR}' IEC.txt | head"
}
```


### [2026-09-05T20:40:15.405Z] TOOL RESULT

```
LEAF 233
LEAF 234
LEAF 235
```


## [2026-09-05T20:40:17.581Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 232 233 234; do echo \"=== leaf $n ===\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' IEC.txt; done | head -c 6000"
}
```


### [2026-09-05T20:40:19.262Z] TOOL RESULT

```
=== leaf 232 ===
d-? Cf. WP I, 527) Gk. cf. ai-gíthalos (orn. *tit'. Cf. auis (1)); Alb. (ambig.) dhí, def. dhija (goat, but cf. gid-); ME kid; Du. kid, kidde ‘pony’; ON kið, gp -a, ja, n. "d: Sw. kid, beside kidling, killing, id. (Eng. kid is prob. of Norse origin, note initial k-)
$ig- ^speck, jot Per cf. jtye, jiqqe ‘tuft, crest’; Gk. cf. gíg-arton “small grain, grapestone'; gigídion ('earthnut or sim.); R zga (jot, tittle’, in phr. ni zgi xléba ‘not a scrap of bread"); melju-zga ‘small fry’; G Kick-beere ‘gall on plants’; Srb. cf. zgeba ‘gnome’. (Isophonic: Li. Zigas 'goldbeetle")
2ig- (gigr-) ‘convulsion, sob; sob, hiccup, gasp' Arm. cf. ckram ‘sob’; Ir. gíogaim ‘squeak’; MHG kiche ‘asthma’; Sw. kikna ‘gasp’; kik- hosta *whooping-cough'
gig- (1) “look, peep’ NGer. kieken; Du. kijken; Icel. kíkja; Sw. kika, id.; Pol. cf. zez, zyz ‘squint’; zezem, adv. ‘asquint’
ĝibos, à — $leibh-
10
15
20
25
30
35
40
45
398
$18- (2) ‘teat Oss. dzidzi; Arm. cic, gs cci, i-st., id.; Slovene zizek, dim. id.; zízati (v. ‘suck’)
êg- (3) ‘spark, fire’. (Variant: ĝeig-)
Arm. cf. ccumb, gs ccmbo, o-st. ‘sulphur’, lit. (?) ‘cloud of sparks’, cf. Arm. amb ‘cloud’; Alb. cf. xixé ‘spark’; Li. Zize Celow heat. Lalis. Infantine wd. for ‘fire’. Cf. variant ZíeZ- iba ‘spark’, fr. *&e18-)
$í&éno (redup.) “bear”; mp. "become WP I,
576. Radical: 8en-, q.v. Av. zizan- ‘give birth’; cf. Skt. jajflih *germi- nating’; Arm. cf. cnim Cam born”, fr. *8enio); Gk. gígnomai, aor. egéneto; Lat. gigno, Gre, pf. genui ‘beget’; W cf. geni, inf. ‘be bofn’; MIr. gignid, 3s fut. ‘will be born": gainiur “am born?
2í2nosko (X2nos-) (intens.) ‘know’. Cf. ong- mi, ?nosKo. WP I, 577-80 Skt. cf. desid. jijfiase; Ober cf. xsnàs-, id.; Gk. gignósko, Epirote gnósko; Lat. a-, co-gnoscó, ére; Arm. cf. canucanem (^warn', fr. *$nosKno)
eiguha ‘tongue’. (Redup. of type guhuo, &u- huos, 2uhón-, etc.)
Skt. jihva; Av. hizu, hizva, hizvá-; OPer. izāva, hazvàn; Pehi. huzvan, hizvan: Per. zabàn; Oss. àvzag, dim. type
ilos, a, is “growth, stem, sprout’
Arm. ciy 'stem, blade of plant’; cil “bud, shoot panicle’; Thracian zila- “vine? beside Dacian -zila, -dila (in plant-names: a-zila, beside a- dila, proce-dila, tani-dila, doc-tila (sic), and dio-dela (sic) of uncertain composition, cf. porKos, tn-, tāk-, diu-); Ir. giol (2) “early grass”; MHG kil (2) ‘leek’; cf. Rum. (? substrate) zir- nå, f. ‘woody nightshade’. (Per. zire ‘caraway, aniseed' is ambig.)
gislos, is (gisol-) ‘pebble, shingle’
Per. cf. Zale “hail; dew" (?); Alb. zallé ‘pebble, shingle’; OHG kisil, MHG kisel, OE ceosel, ceosol, id.; G Kiesel "flint, silica, hail; kisseln, v. ‘hail’; Icel. kísill ‘silica’; OCS žali “shore? Srb. žal, id.
(&it-, variant of ĝid-, gidh-, q.v. WP I, 527. Cf. W gid, giten ‘kid’. Isophonic are MHG kit, gs kides; kide ‘sprout’; OE cip *mote")
£ieua, see Seu
&leibh- (variant of gleibh-, glibh-, q.v. "ad.
399
here’. Cf. Li. Zleibiü, "ti, v. ‘pilfer; grasp, un- derstand’. (Gmc. forms ambig.)
$lous, see £olou-
£naiuos (form of gnauos, $nauos? q.v. The parallel existence of two roots gn- ‘be born’ and gn- ‘know’ renders the semantics ambig.) Lat. naevus ‘birthmark’; OLat. gnaivo- (Fest. gnaevus); Osc. Gnaivs, a name; Olr. cf. gné (2) “form, beauty’; Ir. gnaoi ‘repute, liking, pleasure’; adj. ‘courteous, pleasant’; Ir. gné, pl. gnéithe ‘hallmark, characteristic’; cf. OE cnæwe, adj. ‘well-known’
8në-, alternative radical form of ĝnāu-, 2no-
mi, q. V. Alb. cf. njof, njoh (“know a person’, fr. *&nesk- or *&nåsk-); OHG cf. knāu (I know’, a past- present form of type novi, -gnoviin Lat.). (Lat. i-ghOrO, are seems to represents a type *n- &naus- but wt. certain cognate forms)
(£neub-, form of 8nib- or of gnib-, q. v. Only in Sw. njupa ‘pinch’; ut-njupen, adj. ‘notched’; Du. knieperig "stingy")
$neuguhó, io, form of gnāuið “press, squeeze’, q.v. Cf. $nuuà OE cnéowian 'futuere' beside cnüwian ‘crush’; Li. Zniaugiu, -ti, v. ‘throttle’; Latv. Znaudzu, Znaugt ‘squeeze’
?nibos, à, is, ios (variant of type gnib-, q.v.) W (ambig.) gnif, pl. ion ‘pain, anxiety’; Du. knijp ‘pinch’; G Kneife, Sw. 
=== leaf 233 ===
knipa ‘tongs’; Li. Zn$bis beside gnybis, m. ‘pinch’. Short vowel in G Kniff ‘pleat, tuck’; Sw. knippa, knippe ‘truss’. Verbal forms: MLG knipen; Du. knij- pen; Sw. knipa; G (not MHG) kneifen; Li. žnýbu, Znybti ‘pinch’; short vowel in Sw. knip- pa ‘to truss’. Cf. WP I, 581-2
$nibh- (or gnibh-), variant radical of gnib- (gnib-), q. v.
Gk. gníphon ‘miser’; W (ambig.) gnif ‘pang’; EMDu. knibbelen ‘nag’
$nobos (?nobil-, gnob-) (?) ‘knot, knob’. Cf. $nubh- (gnubh-). WP I, 581 Ir. (ambig.) gnobh ‘knot in wood’; OE cnapp, ON knappr, Sw. knapp, m. "button, knob, boss’. (Finn. nappula ‘peg’ seems to derive from a Gmc. form represented in OHG kne- bil ‘gag’)
$nó-mi, (£n-, $noio, $nou, $nou-) ‘know’. WP
 
8lous — £nósKo (£n-)
20
25
30
35
40
45
400
I, 577-80 Tokh. AB kna-; Gk. aor. égnon; OHG knāu ‘I know’; OE cnawan; OCS znajo; Li. Zinaü; Latv. zinu (aor.-pres.) ‘know’
£nómn-, nómn- ‘recognition, sign, name’. WP I, 577-80 Gk. gnoma; Lat. cf. co-gnomen; i-gnominia; OCS name ‘sign’; znamenije ‘token’; Li. cf. žinomas (knowledgeable; famous’: OCS zna- mü. Vowel -o- for *-uo-?)
-£nos, -nà (1) zero-grade extn. of ĝen-, q. v. and cf. £n-, ĝñmos Vedic nava-ja ‘new’; Gk. neo-gnós ‘newborn’; (uncertainly: á-gnos, a verbenacea with hot peppery fruit used as an anti-aphrodisiac, also called *monk's pepper’: Skt. sam-jfiam "a fra- grant yellow wood"); Lat. privi-gnus ‘stepson’; cf. beni-gnus, mali-gnus, and pi-gnus, -gnoris, (2) ‘son’ or “daughter”, if pi- is aphetic for *ep
```


## [2026-09-05T20:40:25.425Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 234 235; do echo \"=== leaf $n ===\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' IEC.txt; done | head -c 7000"
}
```


### [2026-09-05T20:40:27.207Z] TOOL RESULT

```
=== leaf 234 ===
znots ‘son-in-law’. WP I, 577-80
£nóu- (ndum, ?nouoi) theme of aor.-present ‘know’. Variant: £neu-? Lat. cf. novi, -gnovi; OHG knàu & NAIb. njo- va, id. (fr. *&$néu-?): ON kná “can, could’, vo- calism as for OHG and NAlb., cf. knia, v. (1) “consider”
ênu ‘knee’. See genu, 20nu Skt. sam-jfiub *knock-kneed'; Av. Znü-; Hitt. abl. sg. kanut ‘from the knee’; Gk. cf. i-gnüs, i-gnúë ‘hollow of the knee, ham, haunch’); pró-khnu Con the knees’, fr. *pros-Snu-); Go. cf. kuna-wida ‘fetter
$nuuó (variant of type *£neuuo, 2neuguho, gnáuió; gnti?- ‘press, penetrate’ W cf. gni “penetration; shock’; OE cnüwian ‘crush’; LG knuwwen, beside knuwen ‘jolt, jog’; Li. (isophonic) cf. Zniungü, Zniügti “be broken, lie flattened'
ên- zero-radical of type &en-, q.v. Cf. -8nos
enostis (£n-) — $nmos, à
20
25
30
35
40
45
402
(1) & (2) : Skt. cf. antar-ja ‘inbred’ Arm. cf. ajla-zan 'dif- ferent’; Gk. neo-gnos, etc.; Lat. privi-gnus; Go. sama-, alja-kuns; Sw. cf. sys-kon ('sib- lings’. See suesr-)
(8namos, variant form of type gnom-, cf. $nos-, etc.). See next OCS (and com. Sl.) znamü (Cknown'. Ambig.); Li. Zinomas; Latv. zinams, id.
$nàtos, variant of type 8notós, q.v.
Gk. cf. gnésios ‘genuine’; Li. Zinótas, Latv. zinàts *known', beside Li. pa-Zintas, id. (Skt. Celt. Gmc. & SI. forms ambig.); cf. Alb. njollë (“scar”, if for *gnatia)
$ndu-, theme of nouns and adjectives of
general sense ‘knowing’ Av. xšnav- “satisfactory”; OPer. xsnav- ‘notice’; Skt. cf. jfíatvam ‘intelligence’; MIr. gnó “love- ly, noble, ingenuous, notable’; m. “form, beau- ty’; OBr. -gnau- in am-gnau-bot ‘conscience’; W ad-na-bod ‘recognize’; Mod. Icel. knár 'cle- ver, smart’; Li. Zindvas, s. ‘expert; cf. Zináv- imas *witchcraft
£nodhos (gondhos) ‘jaw’. Cf. genus Gk. gnáthos; Phryg. kánados. Hes.; Li. Zán- das; Latv. zods, id.
$notos (gntos), form of type 8ntos ‘born’ and of type 8notós ‘known’
Lat. gnatus (Plaut), beside co-, a-gnitus (known', etc.); Cor. gnàs, f. ‘nature’; MHG cf. kunt, gs kundes ‘known’. WP I, 577-80
(&nou-, form of $nóu-, q.v.
Li. Zinaü 'I know”; Li. zinu, id. aor. pres. of type seen in OHG knàu)
(&n- “birth; kind”, etc. see &n-, etc.)
(8n- ‘knowledge’, etc. see $nó-, etc. Cf. Skt. à-jíía ‘authority’; Li. Latv. Zinià, zina “informa- tion")
(£n-mátr- 'son-in-law'. Only in Skt. jámatr, Av. zàmatar, Romani gamutro. See gnmros (?) and giros) š
fnmos, à ‘generation, mating’. Cf. gnros and next Skt. jàmà ‘daughter’; cf. jàmih ‘sibling; twin’; Av. jāma, n. ‘kinship’; Per. cf. dā- (in da-mad *son-in-law); Gk. gámos ‘marriage’; cf. gam- brós “male in-law?; Lat. cf. gemini (‘twins’, if for a type *&nmenoi); Br. cf. gév-er 'son-in-
403 law?
£nmros (?), cf. ĝnros Vedic cf. hapax (RV 4.3,9) jamaryah “related by marriage’; Gk. gambrós “male in-law?; Br. géver “son-in-law?
$nó-mi, -mn-, etc. see $nómi, etc.
Bugs, &nos-, see -£nos, $nós-
$not-, see ĝnõt-
nros ‘male in-law'. Cf. $nmros Alb. dhándérr, T dhëndër ‘son-in-law’; Lat. gener, id.
$iisos, variant of ĝnōs-, q.v. in Lat. gnàrus ‘skilful’. See 8ntós (2)
ntis (1) “birth, race’; 8ntós ‘born’. Cf. geno- tos. WP I, 576 Skt. jatih; jatáh ‘son’; Av. jaitis; zātō ‘born’; zZàtho ‘birth’; Per.-zad, cpds. ‘born’; Gk. cf. ne-gáteos “newly made"; Lat. prae- gnas, -gna- tis ‘pregnant’; pro-gnatus ‘offspring’: Gaul -gnàtos, in names; OHG kunt Q) ‘akin’; OE cypp ‘kinship, kinsman’; cynd ‘kind, origin, offspring’; cüp (2) ‘related; familiar
&ntis (2), 8ntus ‘knowledge’; £ntós “known. WP I, 576 Av. à-zaiíitis
=== leaf 235 ===
, zəntus ‘knowledge’; Oss. zond, id., zind ‘known’; Go. kunpi; kunps; OHG kunt, pp.; MHG kunde, künde, s.; OE cypp, s. beside cüp, pp.; Li. cf. pa-Zintis, f. *acquain- tance’; Latv. zinte, f. *witchcraft
?obho, ið ‘peck, poke, stab, obtrude’. WP I, 575 Skt. jábhe; Ir. gobaim; OE be-caefian (‘adorn’. Semantics obscure); E to chaff ‘tease’; LG cf. kawweln “quarrel'; kaffeln ‘crunch’; OCS zo- blo, zobati "eat": Cz. zobat ‘peck’; Li. (de nom.) Zabóti “fix bit in horse's mouth’; žab- ángai ‘trap’; pà-Zabas “wing of trawling-net'. See next Å
ĉobhos (1) ‘sharp twig, beak, spike’. Cf. WP I, 570 and gobho, io, gabh- Ir. gob ‘beak, snout; G Kebe ‘jaw, gill’; Cz. zob ‘beak’; Li. žābas, à, mf. ‘twig’
ĉĝobhos, is (2) ‘chickfeed, chaff OE ceaf *chaff; MLG kaf, Du. kaf, LG kaff, id.; OCS. R zobi, Srb. zob *oats'; Blg. zob ‘horse-fodder’
$obhul-, gobhlio- (variants of ĝobhos (1), q. V.). Ambig. cf. gabhəlos
$nmros — Gon-
15
20
25
30
35
40
45
404
OE cf. cæfl ‘muzzle, halter’; ON kefli “peg, gag’
2oibos (?) ‘twist, bend’ Per. ziv 'ship's worm; deceit’; Icel. keipar, mpl. ‘whims’; keipa, v. bend to an angle
(Gol see gel-). WP I, 623
ĉombos, is, us (1) ‘tuft, bush, head of hair Skt. jambüh, f., jambu, n. *rose-apple & tree"; Arm. cam, i-st. “head of hair’; cf. also camuk, dim. *pasque-flower'; ON kampar, mp. *whis- kers’
gombos (2) (?) “side, face? ON kampr, m. (2) “facing wall’; Li. Zambas (2) “side, lap of garment
gombho ‘show the teeth, chew, bite, stab, snap'. WP I, 575. See next, and cf. gembh- Skt. jáàmbhe ‘snap at; Per. zimam, zámidàn ‘chew’; Osset. zimbín ‘yaw; Arm. camem ‘chew’; Gk. denom. gomphóo ‘nail’; E dial. to cham ‘to chew’; Cz. zubit se “show the teeth, grin’; Big. zábja se “bare the teeth’; Li. Zámbu, Eti shoot, sprout
$ombhos 'spike, nail, tooth". Cf. gembh-, $ombho. WP I, 575 Skt. jáàmbhah “tooth, fang’; Per. zam ‘cheek, jaw’; Arm. cf. camak ‘dibble, grubber’; Tokh. A kam, B keme ‘tooth’; Gk. gómphos ‘spike, nail, tooth’; Alb. dhàmb, dhémp ‘tooth’; MHG kamp, gs kambes “comb, overhang, spiked collar for pigs’; OE camb, ‘comb, crest’, cammoc, dim. (‘rest harrow’: EME cam- mock); ON kambr, as OE; OCS (and com. Sl.) zobü ‘tooth’; Li. Zambas “jag, rib, seam, edge, wooden plow’; Latv. zobs ‘tooth’; Finn. LW hammas, pl. hampaat ‘tooth’. (Isophone Ir. gomh *pain")
$ombhros, is "a horned animal, bison’. Cf. $ombhos, 3embh- Thrac. zómbron, acc. sg. ‘bison’; Byzantine Gk. id. as LW; OCS zobri, m. id.; Cz. R zubr, id. (Here also isophonic ON gambr, gambrs gs.; gammr, gs gammrs ‘vulture’; Li. Zambris *plowshare? if the general sense is ‘horned, spiked’)
(ĉomos, ĝomn-, see Supt.)
ĝön- ‘angular, pointed; angle, chin, cheek". Cf. ĝen- (1) & (2) Gk. cf. gónios ‘angled’; gonía ‘corner’; tri-
405
gðnos ‘three-pointed’ pó-gon (“beard?, appar. for poK-, q. v. + -°); sià-gón «cheek, jowl’; MHG küene ‘bold’; OE cëne ‘sharp, clever, bold’; E keen. Cf. also Du. koon (‘cheek’,
```


## [2026-09-05T20:40:53.123Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BQT_v2_pages داماد ===\"; grep -n \"داماد\" BQT_v2_pages.txt | head -20; echo \"=== find page 817 tag ===\"; grep -n \"\\[pdf page\" BQT_v2_pages.txt | head -3"
}
```


### [2026-09-05T20:40:53.187Z] TOOL RESULT

```
=== BQT_v2_pages داماد ===
16316:   ‫‪ #‬داماد ‪ -‬پهلوی )‪ , 4072‬اوستا‪( 72]200282-‬داماد)‪ ,‬هندی‌باستان ‪,۲2420۳81-‬‬
16322:                          ‫‪.‬‬         ‫غازی که‌داماد او بود بخواهر ‪ ....‬شنیدم» «چهارمقاله طبحم دن صه؛ ‏‬
18775:‫داماد بخانة عروس میفرمتد ‪ -‬و مهری را نیز‬                        ‫دست بنرحن ‪ = ۱‬دستینه ای باشد‬
19440:                                                                                                     ‫عروی باشد که زن داماد است ‪.‬‬
26187:‫= بفتح نون مان‬                  ‫یریونه(‪۳۱۲‬‬                      ‫ابرانی که داماد طوس ویسر بعنگه بوده ‪ -‬ونام‬
26726:                                                              ‫وئام پر کی کاوس هم هت که داماد طوس بود‬
26765:                                                             ‫وس داماد طوس باشد و اودر‬
27894: ‫ر راو ند بقتح اول بر وزن دماوند »‬                            ‫تام پسرطوس‌بن لوذر(‪ )۱‬است و اوداماد کیکاوی‬
37584:‫و بمعتی رشته مروارید و رشتةٌ سوزن باشدخصوصاً‬          ‫بمهیمرسد ‪ -‬و بکر اول یمعتی هم‌داماد باشد‬
=== find page 817 tag ===
```


## [2026-09-05T20:40:53.857Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== MON part1 ===\"; grep -c \"داماد\" MON_part1.txt MON_part2.txt 2>/dev/null; grep -n \"داماد\" MON_part2.txt | head -5"
}
```


### [2026-09-05T20:40:53.932Z] TOOL RESULT

```
=== MON part1 ===
MON_part2.txt:16
MON_part1.txt:34
6434:که بر سر عروس و داماد ریزند؛ نثارسر 
21331:کان: وزیر. بادشاه. شوهره زوج. داماد. 
21353:داماد سودن دامادی. مجامعت؛ 7 
30937:جایی که برای نوعروس و داماد سازند؛ 
41782:عروسی داماد با هدبه‌ای به دیندار مادر
```


## [2026-09-05T20:40:58.182Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '16300,16325p' BQT_v2_pages.txt; echo \"=== page tags format ===\"; grep -n -m5 \"pdf page\\|^\\[.*page\" BQT_v2_pages.txt | head"
}
```


### [2026-09-05T20:40:58.242Z] TOOL RESULT

```
‫دامن بنددان گر تز بمعنی‌دامن‬                             ‫داهلث » بفتحثالث بر وزن کالك '‬
‫بدندان کردن است کنهابه از عجز و فروتنی‬                   ‫جانوران وحتی کوچك راگویند همچوخ رگوش‬
                                    ‫وگربختن باشد ‪.‬‬      ‫ورویاه وامثالآن ‪ -‬و مقنمه وسرانداز زنانرا هم‬

                                ‫‪.‬‬    ‫(‪ )۲‬چك‪ .‬چش ‪ :‬هم هت‬               ‫(‪ )۱‬چك ‪ :‬نخحیر را ‪.‬‬

  ‫» رام شدن) » بونانی ‪( 5618002‬کاو نر) ‪.‬‬               ‫رمدن‬
                                                          ‫‪ - ۱‬حندی باستان ‪( 0۳31 -‬کرا‬
   ‫)؛ در پپلوی ‪0۳84‬‬           ‫رمدن‬
                                 ‫لانبنی ‪ ( 6720۳10‬کاو نر‪ .‬ورزاو ) فس ‪ :‬استی ‪( 000۳0‬کرا‬
                     ‫(مخلوق) (اوستا ‪« )020180-‬اسشق ‪ ۰۳۵‬و ص ‪۲۷۲٩‬‏ ورك ‪ :‬مناس ‪. ۰۷۲:۲‬‬
  ‫‪ - ۴‬هندی باستان‪( 02008 -‬بند‪ .‬ریمان ‪ ,‬زنجیر) » افقانی ‪ , 0101‬ارمنی ع (‪)8‬‬
  ‫‪( 602‬تور) «امذق‪ .۱۳۰‬پهلوی ‪« 018‬مناس ‪۱۷۲‬؛ نیز تورماهیگیری ‪« :‬ماهی از دام جدا‬
  ‫شد ‪,‬روباه پیشتررفت وماهی خوردن گرفت» «سندبادنامه‪ .‬ظهیری‪ .‬طبع احمدآش ص ‪ ۸4‬طبری‬
               ‫رك ‪ :‬دامنی ‪.‬‬          ‫‪ ۰‬مازندرانی کنونی ‪ « 20062‬واژه نامه ‪. ۲۱4۰‬‬
                                       ‫‪۴‬‬                                                         ‫‪8‬‬
   ‫‪ #‬داماد ‪ -‬پهلوی )‪ , 4072‬اوستا‪( 72]200282-‬داماد)‪ ,‬هندی‌باستان ‪,۲2420۳81-‬‬
   ‫کردی ‪ › 62۷22‬اففانی‪ 0۳2‬و ‪, 128۳02‬بلوچی ‪ 012002‬و ‪ «04۵۷021‬اسدق ‪۲۳۵۰۰‬‬
   ‫‪,‬مشچه ‪20۳۵2‬؛‬
              ‫کیلگی‪ .4۳2‬اورامانی ‪« 01۷20182‬ك‪ .‬اورامان ‪ ۷۲۱۲۰‬دزفولی ‪ 010‬ک‬
   ‫مردیکه تازه جشن‌عروسی وی برپا شود ‪ ۰‬مرد تازه زن گرفته ‪.‬شوهر دختر شخص"‪ -‬شوهرخواهر‬
  ‫شخص‪ « :‬از ملطان عالم ‪ ۰.‬محم‌دین ملکشاه بدر همدان در واقعة امیر شهاب الدین قتلمش الب‬
                          ‫‪.‬‬         ‫غازی که‌داماد او بود بخواهر ‪ ....‬شنیدم» «چهارمقاله طبحم دن صه؛ ‏‬
              ‫‪#‬دامای = داهن (مخفف)‪ -‬بفتح سوم کنار پابین جامه(مقابل گریبان) ‪:‬‬
           ‫ابن کریباش کیرد آن دامن‪.‬‬                            ‫سک ودربان چوافتند غریب‬
   ‫دگلتان ‪. ۹۳۰‬‬
=== page tags format ===
```


## [2026-09-05T20:41:08.031Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\np='BQT_v2_pages.txt'\nd=open(p,encoding='utf-8',errors='replace').read()\nprint('formfeeds:',d.count('\\f'))\nimport re\nprint(re.findall(r'\\[[^\\]\\n]{0,40}page[^\\]\\n]{0,20}\\]',d)[:5])\n# find line 16316 -> which page\nlines=d.split('\\n')\nidx=16315\npre='\\n'.join(lines[:idx])\nprint('page index by formfeed:',pre.count('\\f'))\nEOF"
}
```


### [2026-09-05T20:41:09.736Z] TOOL RESULT

```
formfeeds: 683
[]
page index by formfeed: 277
```


## [2026-09-05T20:41:13.107Z] TOOL CALL #24: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nb=d['BQT']\nfor k,v in b.items(): print(k,':',str(v)[:900]); print()\n\""
}
```


### [2026-09-05T20:41:15.032Z] TOOL RESULT

```
title : Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)

kind : archive_djvu+local_scan_ocr

url : https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.com/file/8230741184/borhane_ghatee_jelde_4.pdf.html (م–ی, 553 pp), vol 5 https://s3.picofile.com/file/8230741300/borhane_ghatee_jelde_5.pdf.html (تعلیقات, Amir Kabir 5th pr. 1376, 293 pp). Same set behind login on ketabnak.com/book/55304-55307 and /58249.

lookup_hint : grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only t

local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verific

page_offset : vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017,

covers_etymology : True

notes : Persian OCR is mediocre: headwords and Mo'in's footnotes (e.g. '۱ - رك: ابر کوه', Pahlavi/Avestan Latin forms) are mostly readable but with many character errors; search with short substrings and tolerate errors. BQT_v1_pages.txt was built from the djvu.xml; BQT_v2_pages.txt from pdftotext -layout of the _text.pdf. Volumes 3–5 (roughly ح/خ–ی and the تعلیقات volume) are not online in full text; for those use Dehkhoda quotations of Borhan/Mo'in via vajehyab/abadis/parsi.wiki, or page images on noorlib (different edition). | Vols 3-5 scans (image only) in incoming/BQT; vols 1-2 have OCR text files BQT_v1_pages.txt / BQT_v2_pages.txt. Offsets verified by eye at several pages (v3 drifts by ~4 pages; page_map gives exact positions once built). || UPDATE: vols 3-5 now downloaded (image-only PDFs, verified as Mo'in's edition from title pages and the Latin footnotes) and OCRed locally. Image-only

scans : [{'volume': '3', 'file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', 'first_printed': 1208, 'last_printed': 1925, 'pdf_offset': -1205, 'page_map': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pagemap.json', 'lang': 'fas', 'ocr_text': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', 'ocr_note': '689/721 pdf pages OCRed (tesseract fas+eng, mediocre); pages are separated by form-feeds and tagged [pdf page N]; remaining pages via tools/ref_page.py'}, {'volume': '4', 'file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', 'first_printed': 1920, 'last_printed': 2475, 'pdf_offset': -1917, 'lang': 'fas', 'offset_note': 'printed = pdf+1917, checked at pdf 150 and 500', 'ocr_text': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming

cites : page number, continuous across the five volumes of Mo'in's edition (1342/1963 = Amir Kabir 1362 reprint); Mo'in's etymological footnotes are the cited material
```


## [2026-09-05T20:41:26.456Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nfor p in ['MON_part1.txt','MON_part2.txt']:\n    d=open(p,encoding='utf-8',errors='replace').read()\n    print('==',p,'ff:',d.count('\\f'),'len',len(d))\n    for m in re.finditer('داماد',d):\n        s=max(0,m.start()-200); print(repr(d[s:m.start()+200])[:420]); print('  leaf', d[:m.start()].count('\\f')); print('---')\nEOF"
}
```


### [2026-09-05T20:41:28.263Z] TOOL RESULT

```
<persisted-output>
Output too large (34.3KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/tool-results/bckmup9i6.txt

Preview (first 2KB):
== MON_part1.txt ff: 0 len 2611770
'ر. کالاها» متاع\u200cهاء استمه. \n(فد.) در اصطلاح حکما چیزی که فی نفسه \nموجود باشد و وجود دیگری از آن حاصل \nشود یعنی چیزی که وسیلةٌ حصول چیزی \nدیگر باشد. (پز.) موجبات و مقدمات مرض. \n(عم.) نقلی که سر عروس و داماد شاباش \nمی\u200cکنند. پندارند که هر کس آن را بردارد و \nبخورد سبب گشایش کارش می\u200cشود. (عر.) \nیکی از ارکان سه گانه را سبب نامند و اساب \nبر دو نوع است: سبب خفیف» مرکب از \nیکك متحرک و یک ساکن مانند: 
  leaf 0
---
'اصل است. \n\nاصولا: 0- ]تاو [ع. ۰] (ق.) اصلگ اساسا \nاصولی: 09011 [ع. .فد ۰] (ص\u200cنست.) مسوبت \nبه اصول. ببرو اصول و قواعد. دانشمند \nاصول (فقه). متکلم به اعتبار اينکه دربارة \nو \n\nاصهار: 92۲ [ع.] (مص\u200cل.) به دامادی \nبواسسن» \n\nاصهب: طفنمه [غ.] (ص.) موی سرح به \nسفیدی آسخته» ی که \n\nاصیل: 2511 [ع.] (ص.) نژاده» باگه \nوالاتبار» گهری» نجیب. (.) شبانگاه؛ ج. \nآصال. \n\nاصائت؛: ادقهه [ع. اضاء ] (مص م.) روشن 
  leaf 0
---
'ن. \nسادگیء بسیرنگی» بی\u200cنیرنگی. (شیم.) \n\n\nچگونگی جسم مفرد (بسیط). \n\nبساک: 0 تاجی که از گل\u200cها و \nریاحین و اسپرغم\u200cها و برگ مورد می\u200cساختند \nو پادشاهان و بزر کان و دلیران روزهای عید \nو جشن و مردمان در روز دامادی بر سر \nمی\u200cگذاشتند. ( گیا.) برجستگی دکمه مانند \nانتهای مبلة پرچم گل که مسحتوی دانه\u200cهای \nگرده می\u200cباشد. \n\nبسالت: ۱022 [ع. سالة ] (امص.) دلبری» \nدلاوری» یلی؛ شجاعت. \
  leaf 0
---
'رسی طبق \nمعمول «بلوا) رایج شد ه است. \n\nبلهاء: "7 (ع.] (ص.) مورنث ابله؛ زن کم \nخرده زن ساده دل. \n\nبله\u200cبر ان: «قتمنتله۱ (ص\u200cفا. امر.) (عسم.) \nصحبت\u200cها و قول و قرارهای قبل از عروسی \nس خائو اده\u200cهای عر وس و داماد. \n\nبپهوس. 0 ال ت سوالهوس ت \n6 ها ۳ سم \n\nابو الهو س | رص مر .۱ | وحن هو س سیار او دا \n\n\n0 آا: (ق. اشات) نله ون \n\nبلی: تا« (امص.) کهنگی» آوارگی. \nبلیارد: 0 (.) نام نوعی بازی ار
  leaf 0
---
...
</persisted-output>
```


## [2026-09-05T20:41:32.976Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"داماد:\" MON_part1.txt MON_part2.txt | head; echo ---; grep -o \"داماد[^\\n]\\{0,120\\}\" MON_part1.txt | head -20"
}
```


### [2026-09-05T20:41:34.967Z] TOOL RESULT

```
MON_part1.txt:59278:داماد: 0 (.) مردی که تازه جشن 
---
داماد شاباش 
دامادی 
دامادی بر سر 
داماد. 
داماد برپا می‌شود. 
داماد. 
داماد را بهم بسته گرد آن 
داماد نبا ر کنند. (نقد. 
دامادی یا بازگشتن از فتحی یا 
داماد رسانند. 
داماد در شب زفاف به عر وس دهد. (عم.) 
داماد با تاره وارد 
داماد ج. ححال. 
داماد. 
داماد: 0 (.) مردی که تازه جشن 
دامادی: ا 07 (حامص.) ازدواج» 
داماد پیش از عروسی به خانة 
داماد به خانهة 
داماد و عروس راه رود؛ شاه 
داماد
```


## [2026-09-05T20:41:42.693Z] TOOL CALL #27: Bash

```json
{
 "command": "sed -n '1,60p' tools/fetch_source.py"
}
```


## [2026-09-05T20:41:42.711Z] TOOL CALL #28: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-05T20:41:42.716Z] TOOL RESULT

```


```


### [2026-09-05T20:41:42.730Z] TOOL RESULT

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
        with urllib.request.urlopen(req, timeout=60) as r:
            status = r.status
            raw = r.read(4_000_000)
            ctype = r.headers.get("Content-Type", "")
            enc = "utf-8"
            m = re.search(r"charset=([\w-]+)", ctype)
            if m: enc = m.group(1)
            body = raw.decode(enc, errors="replace")
            if "html" in ctype or body.lstrip().lower().startswith("<!doctype html") or "<html" in body[:2000].lower():
                mt = re.search(r"(?is)<title>(.*?)</title>", body)
```


## [2026-09-05T20:41:47.025Z] TOOL CALL #29: Bash

```json
{
 "command": "for u in \"https://en.wiktionary.org/wiki/داماد\" \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/j́āmātā\" \"https://en.wiktionary.org/wiki/γάμος\" \"https://en.wiktionary.org/wiki/जामातृ\" \"https://www.etymonline.com/word/polygamy\"; do echo \"### $u\"; python3 tools/fetch_source.py \"$u\" --note \"page 170, root Geme/Gem: damad, zamatar, gamos, polygamy\" ; done"
}
```


### [2026-09-05T20:41:57.279Z] TOOL RESULT

```
### https://en.wiktionary.org/wiki/داماد
/home/sfmqrb/git/rishe/data/verification/sources/web/ce5ca6174cfa25b7.txt
### https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/j́āmātā
/home/sfmqrb/git/rishe/data/verification/sources/web/72755f863b6b50b0.txt
### https://en.wiktionary.org/wiki/γάμος
/home/sfmqrb/git/rishe/data/verification/sources/web/70173a6fba3573f3.txt
### https://en.wiktionary.org/wiki/जामातृ
/home/sfmqrb/git/rishe/data/verification/sources/web/35b34821ed9e6e82.txt
### https://www.etymonline.com/word/polygamy
/home/sfmqrb/git/rishe/data/verification/sources/web/e9b0d6e2201c3b03.txt
```


## [2026-09-05T20:41:59.405Z] TOOL CALL #30: Bash

```json
{
 "command": "cd data/verification/sources/web && echo \"=== damad ===\"; grep -n -A30 -i \"Persian\\[edit\\]\\|Etymology\" ce5ca6174cfa25b7.txt | head -60"
}
```


### [2026-09-05T20:41:59.447Z] TOOL RESULT

```
=== damad ===
76: Etymology 
77-
78- 2.3 
79- Pronunciation 
80-
81- 2.4 
82- Noun 
83-
84- 2.4.1 
85- Derived terms 
86-
87- 2.4.2 
88- Descendants 
89-
90- 2.5 
91- Further reading 
92-
93- 3 
94- Urdu 
95-
96- Toggle Urdu subsection 
97-
98- 3.1 
99: Etymology 
100-
101- 3.2 
102- Pronunciation 
103-
104- 3.3 
105- Noun 
106-
107- 3.3.1 
108- Declension 
109-
110- 3.4 
111- References 
112-
113- 3.5 
114- Further reading 
115-
116- Toggle the table of contents 
117-
118- داماد 
119-
120- 8 languages 
121-
122- বাংলা 
123- فارسی 
124- Bahasa Indonesia 
125- کٲشُر 
126- Kurdî 
127- Malagasy 
128- Русский 
129- Türkçe 
--
262: Etymology
263- [ edit ] 
264-
265- From Middle Persian [script needed] ( dʾmʾt' /⁠dāmād⁠/ ) , from Old Persian *𐎭𐎠𐎶𐎠𐎫𐎼 ( *d-a-m-a-t-r /⁠dāmātar-⁠/ ) , from Proto-Iranian *jā́mātā , from Proto-Indo-Iranian *ȷ́ā́mātā , from Proto-Indo-European *ǵem- ( “ to marry ” ) .
266-
```


## [2026-09-05T20:42:00.811Z] TOOL CALL #31: Bash

```json
{
 "command": "cd data/verification/sources/web && sed -n '255,330p' ce5ca6174cfa25b7.txt"
}
```


### [2026-09-05T20:42:00.855Z] TOOL RESULT

```
 Wikipedia fa 

 Alternative forms
 [ edit ] 

 دوماد ( dumâd ) ( eye-dialect ) 

 Etymology
 [ edit ] 

 From Middle Persian [script needed] ( dʾmʾt' /⁠dāmād⁠/ ) , from Old Persian *𐎭𐎠𐎶𐎠𐎫𐎼 ( *d-a-m-a-t-r /⁠dāmātar-⁠/ ) , from Proto-Iranian *jā́mātā , from Proto-Indo-Iranian *ȷ́ā́mātā , from Proto-Indo-European *ǵem- ( “ to marry ” ) .

 Cognate with Northern Kurdish zava , Pashto زوم ( zum ) , Avestan 𐬰𐬁𐬨𐬁𐬙𐬀𐬭 ( zāmātar ) , Sanskrit जामातृ ( jāmātṛ ) , Ancient Greek γαμβρός ( gambrós ) .

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /daː.ˈmaːd/ 

 ( Dari, formal ) IPA ( key ) : [d̪ɑː.mɑːd̪] 

 ( Dari, formal ) IPA ( key ) : [d̪ɑː.mɑːd̪] 
 ( Kabuli ) IPA ( key ) : [d̪ɑː.mɑːd̪] 

 ( Hazaragi ) IPA ( key ) : [d̪ɔː.mɔːd̪̥] 

 ( Iran, formal ) IPA ( key ) : [d̪ɒː.mɒːd̪̥] 

 ( Iran, formal ) IPA ( key ) : [d̪ɒː.mɒːd̪̥] 
 ( Tehrani ) IPA ( key ) : [d̪uː.mɒːd̪̥] 

 ( Tajik, formal ) IPA ( key ) : [d̪ɔ.mɔd̪] 

 Rhymes: -aːd 

 Readings

 Classical reading ? 

 dāmād

 Dari reading ? 

 dāmād

 Iranian reading ? 

 dâmâd

 Tajik reading ? 

 domod

 Audio ( Iran ) : ( file ) 

 Noun
 [ edit ] 

 Dari

 داماد 

 Iranian Persian

 Tajik

 домод 

 داماد • ( dāmād / dâmâd ) ( plural دامادها ( dāmād-hā / dâmâd-hâ ) , Tajik spelling домод ) 

 bridegroom 
 c. 1260s , Jalāl ad-Dīn Mohammad Rūmī , translated by Reynold A. Nicholson , مثنوی معنوی [ Masnavi-ye-Ma'navi ], volume V, verse 3720: گفت دختر را کزین داماد نو، خویشتن پرهیز کن حامل مشو. goft doxtar-râ k-az-in dâmâd -e now, xištan parhiz kon hâmel ma-šow He said to his daughter, "Guard yourself from this new bridegroom , do not become with child." 

 son-in-law 
 c. 977-1010 , ابوالقاسم فردوسی توسی [ Abū l-Qāsim Firdawsī Tūsī ], “ پادشاهی لهراسپ [ King Lohrâsp ]”, in شاهنامه [ šāhnāma , Shahnameh ]‎ [1] : یکی منظری پیش ایوان خویش، برآورده چون تخت رخشان خویش، به میدان شدندی دو داماد اوی، بیاراستندی دل شاد اوی. yeki manzari piš-e ivân-e xiš, bar-âvarde čon taxt-e roxšân-e xiš, be meydân šodandi do dâmâd -e uy, bey-ârâstandi del-e šâd-e uy. He erected a portico before his own palace, resembling his own shining throne; his two sons-in-law made their way to the square, and delighted his gladdened heart.
```


## [2026-09-05T20:42:07.832Z] TOOL CALL #32: Bash

```json
{
 "command": "cd data/verification/sources/web && grep -n -i -m1 -A40 \"Proto-Iranian\" 72755f863b6b50b0.txt | sed -n '1,80p'; echo \"=== size ===\"; wc -c 72755f863b6b50b0.txt"
}
```


### [2026-09-05T20:42:07.893Z] TOOL RESULT

```
1:URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/j́āmātā
2-FETCHED: 2026-09-05T20:41:49Z
3-STATUS: -1
4-TITLE: 
5-
6-FETCH FAILED: HTTP Error 404: Not Found
=== size ===
166 72755f863b6b50b0.txt
```


## [2026-09-05T20:42:12.647Z] TOOL CALL #33: Bash

```json
{
 "command": "python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/jáHmātā\" --note \"p170 PIr son-in-law\" >/dev/null; for u in \"https://en.wiktionary.org/wiki/%F0%AC%B0%F0%AC%81%F0%AC%A8%F0%AC%81%F0%AC%99%F0%AC%80%F0%AC%AD\" \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%C7%B5em-\"; do echo \"### $u\"; python3 tools/fetch_source.py \"$u\" --note \"page 170: Avestan zamatar / PIE gem-\"; done"
}
```


### [2026-09-05T20:42:15.517Z] TOOL RESULT

```
### https://en.wiktionary.org/wiki/%F0%AC%B0%F0%AC%81%F0%AC%A8%F0%AC%81%F0%AC%99%F0%AC%80%F0%AC%AD
/home/sfmqrb/git/rishe/data/verification/sources/web/b403eed51af6dba5.txt
### https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%C7%B5em-
/home/sfmqrb/git/rishe/data/verification/sources/web/3d624b2b263e7ff7.txt
```


## [2026-09-05T20:42:18.768Z] TOOL CALL #34: Bash

```json
{
 "command": "cd data/verification/sources/web && echo \"=== avestan zamatar ===\"; sed -n '1,10p' b403eed51af6dba5.txt; grep -n -i -A12 \"Etymology\" b403eed51af6dba5.txt | sed -n '1,60p' | tail -40; echo; echo \"=== PIE gem- ===\"; sed -n '1,8p' 3d624b2b263e7ff7.txt; grep -n -i -A25 \"Root\\|Derived terms\" 3d624b2b263e7ff7.txt | tail -50"
}
```


### [2026-09-05T20:42:18.851Z] TOOL RESULT

```
=== avestan zamatar ===
URL: https://en.wiktionary.org/wiki/%F0%AC%B0%F0%AC%81%F0%AC%A8%F0%AC%81%F0%AC%99%F0%AC%80%F0%AC%AD
FETCHED: 2026-09-05T20:42:15Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found
=== PIE gem- ===
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%C7%B5em-
FETCHED: 2026-09-05T20:42:15Z
STATUS: 200
TITLE: Reconstruction:Proto-Indo-European/ǵem- - Wiktionary, the free dictionary

Reconstruction:Proto-Indo-European/ǵem- - Wiktionary, the free dictionary 

 Jump to content 
155- Albanian: dhëndër , dhëndërr , dhandër — Gheg , dhândërr — Gheg 
156-
157- Proto-Hellenic: 
158- Ancient Greek: γαμβρός ( gambrós ) , γαβρός ( gabrós ) , γαμρός ( gamrós ) , γαββρός ( gabbrós ) , γαμερός ( gamerós ) Greek: γαμπρός ( gamprós ) 
159- Mariupol Greek: гамбро́с ( hambrós ) 
160-
161- Proto-Italic: *genros 
162- Latin: gener ( see there for further descendants )
163-
164- *ǵém-ti-s ~ *ǵm̥-téy-s ( “ matrimony ” ) 
165- Proto-Iranian: *ȷ́ā́mtiš 
166- Avestan: 𐬰𐬁𐬨𐬌𐬙𐬌 ( zāmiti , “ child-birth ” ) 
167-
168- Unsorted formations 
169- > ? Proto-Balto-Slavic: *źénˀtis , *źénˀtas ( “ son-in-law ” ) ( see there for further descendants )
170-
171- Hellenic:
172- Ancient Greek: γᾰ́μος ( gắmos ) ( see there for further descendants )
173- ⇒ γαμέω ( gaméō ) 
174-
175- Proto-Indo-Iranian: *ȷ́ā́mātā ( see there for further descendants )
176-
--
208: Proto-Indo-European roots 
209: Proto-Indo-European CeR-shaped roots 
210-
211- Hidden categories: Pages with etymon 
212- Proto-Indo-European entries with etymon 
213- Pages with entries 
214- Pages with 1 entry 
215- Sanskrit terms with non-redundant manual transliterations 
216-
217- This page was last edited on 23 August 2026, at 21:58.
218-
219- Definitions and other text are available under the Creative Commons Attribution-ShareAlike License ; additional terms may apply. By using this site, you agree to the Terms of Use and Privacy Policy. 
220-
221- Privacy policy 
222-
223- About Wiktionary 
224-
225- Disclaimers 
226-
227- Legal & safety contacts 
228-
229- Code of Conduct 
230-
231- Developers 
232-
233- Statistics 
234-
```


## [2026-09-05T20:42:21.035Z] TOOL CALL #35: Bash

```json
{
 "command": "cd data/verification/sources/web && sed -n '110,168p' 3d624b2b263e7ff7.txt"
}
```


### [2026-09-05T20:42:21.100Z] TOOL RESULT

```
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

 Root
 [ edit ] 

 *ǵem- [ 1 ] 

 to marry 

 Alternative reconstructions
 [ edit ] 

 *ǵemH- [ 2 ] [ 3 ] 

 Derived terms
 [ edit ] 

 Terms derived from the Proto-Indo-European root *ǵem- (20 c, 0 e) 

 *ǵm̥-rós ( “ son in law ” ) [ 1 ] [ 2 ] 
 > ? Proto-Albanian: *dzanra [ 4 ] ( or from *ǵem-tēr ) 
 Albanian: dhëndër , dhëndërr , dhandër — Gheg , dhândërr — Gheg 

 Proto-Hellenic: 
 Ancient Greek: γαμβρός ( gambrós ) , γαβρός ( gabrós ) , γαμρός ( gamrós ) , γαββρός ( gabbrós ) , γαμερός ( gamerós ) Greek: γαμπρός ( gamprós ) 
 Mariupol Greek: гамбро́с ( hambrós ) 

 Proto-Italic: *genros 
 Latin: gener ( see there for further descendants )

 *ǵém-ti-s ~ *ǵm̥-téy-s ( “ matrimony ” ) 
 Proto-Iranian: *ȷ́ā́mtiš 
 Avestan: 𐬰𐬁𐬨𐬌𐬙𐬌 ( zāmiti , “ child-birth ” ) 

 Unsorted formations
```


## [2026-09-05T20:42:27.810Z] TOOL CALL #36: Bash

```json
{
 "command": "python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/ȷ́ā́mātā\" --note \"p170 PII jamata\" ; python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/जामि\" --note \"p170 Skt jami\"; cd data/verification/sources/web && echo \"=== gamos ===\"; grep -n -i -B2 -A15 \"Etymology\" 70173a6fba3573f3.txt | grep -v \"^\\s*$\" | sed -n '1,60p'"
}
```


### [2026-09-05T20:42:30.842Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/4d65375f4e4371f1.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/53d2988b8b1b1106.txt
=== gamos ===
60-
61- 1.1 
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Noun 
69-
70- 1.3.1 
71- Declension 
72-
73- 1.3.2 
74- Derived terms 
75-
76- 1.3.3 
77- Related terms 
--
92-
93- 2.1 
94: Etymology 
95-
96- 2.2 
97- Pronunciation 
98-
99- 2.3 
100- Noun 
101-
102- 2.3.1 
103- Declension 
104-
105- 2.3.2 
106- Derived terms 
107-
108- 2.3.3 
109- Related terms 
--
195- [ edit ] 
196-
197: Etymology
198- [ edit ] 
199-
200- From Proto-Indo-European *ǵem- ( “ to marry ” ) . [ 1 ] 
201-
202- Pronunciation
203- [ edit ] 
204-
205- IPA ( key ) : /ɡá.mos/ → /ˈɣa.mos/ → /ˈɣa.mos/ 
206-
207- ( 5 th BCE Attic ) IPA ( key ) : /ɡá.mos/ 
208-
209- ( 1 st CE Egyptian ) IPA ( key ) : /ˈɡa.mos/ 
210-
211- ( 4 th CE Koine ) IPA ( key ) : /ˈɣa.mos/ 
212-
--
437- [ edit ] 
438-
439: Etymology
```


## [2026-09-05T20:42:32.991Z] TOOL CALL #37: Bash

```json
{
 "command": "cd data/verification/sources/web && echo \"=== PII jamata ===\"; grep -n -A40 \"Proto-Indo-Iranian$\\|Noun\" 4d65375f4e4371f1.txt | sed -n '1,70p'"
}
```


### [2026-09-05T20:42:34.460Z] TOOL RESULT

```
=== PII jamata ===
65: Noun 
66-
67- 1.2.1 
68- Inflection 
69-
70- 1.2.2 
71- Descendants 
72-
73- Toggle the table of contents 
74-
75- Reconstruction:Proto-Indo-Iranian/ ȷ́ā́mātā 
76-
77- Add languages 
78-
79- Reconstruction 
80-
81- Discussion 
82-
83- English 
84-
85- Read 
86-
87- Edit 
88-
89- View history 
90-
91- Tools 
92-
93- Tools
94-
95- move to sidebar 
96- hide 
97-
98- Actions
99-
100- Read 
101-
102- Edit 
103-
104- View history 
105-
--
131: Proto-Indo-Iranian
132- [ edit ] 
133-
134- Etymology
135- [ edit ] 
136-
137- From Proto-Indo-European *ǵem- ( “ to marry ” ) . Cognate with Ancient Greek γαμβρός ( gambrós ) , γάμος ( gámos ) (whence English -gamy ).
138-
139: Noun
140- [ edit ] 
141-
142- *ȷ́ā́mātā   m ( stem *ȷ́ā́mātr̥ ) 
143-
144- son-in-law 
145-
146- Inflection
147- [ edit ] 
148-
149- consonant stem
150-
151- singular
152-
153- dual
154-
155- plural
156-
157- nominative
158-
```


## [2026-09-05T20:42:36.882Z] TOOL CALL #38: Bash

```json
{
 "command": "cd data/verification/sources/web && grep -n -A30 \"Descendants\" 4d65375f4e4371f1.txt | sed -n '1,60p'; echo \"=== Skt jami ===\"; grep -n -A12 \"Etymology\" 53d2988b8b1b1106.txt | tail -30"
}
```


### [2026-09-05T20:42:36.945Z] TOOL RESULT

```
71: Descendants 
72-
73- Toggle the table of contents 
74-
75- Reconstruction:Proto-Indo-Iranian/ ȷ́ā́mātā 
76-
77- Add languages 
78-
79- Reconstruction 
80-
81- Discussion 
82-
83- English 
84-
85- Read 
86-
87- Edit 
88-
89- View history 
90-
91- Tools 
92-
93- Tools
94-
95- move to sidebar 
96- hide 
97-
98- Actions
99-
100- Read 
101-
--
221: Descendants
222- [ edit ] 
223-
224- Proto-Indo-Aryan: *ȷ́ā́mātā 
225- Sanskrit: जामातृ ( jā́mātṛ ) ( see there for further descendants )
226-
227- Proto-Iranian: *jā́mātā ( see there for further descendants )
228-
229- Retrieved from " https://en.wiktionary.org/w/index.php?title=Reconstruction:Proto-Indo-Iranian/ȷ́ā́mātā&oldid=88895624 "
230-
231- Categories : Proto-Indo-Iranian terms derived from the Proto-Indo-European root *ǵem- 
232- Proto-Indo-Iranian terms derived from Proto-Indo-European 
233- Proto-Indo-Iranian lemmas 
234- Proto-Indo-Iranian nouns 
235- Proto-Indo-Iranian masculine nouns 
236- Proto-Indo-Iranian consonant stem nouns 
237- iir-pro:Family 
238-
239- Hidden categories: Proto-Indo-Iranian entries without References header 
240- Proto-Indo-Iranian entries without References or Further reading header 
241- Pages with etymon 
242- Proto-Indo-Iranian entries with etymon 
243- Pages with entries 
244- Pages with 1 entry 
245- Sanskrit terms with non-redundant manual transliterations 
246-
247- This page was last edited on 28 December 2025, at 01:53.
248-
=== Skt jami ===
```


## [2026-09-05T20:42:41.172Z] TOOL CALL #39: Bash

```json
{
 "command": "python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/jā́mātā\" --note \"p170 PIr jamata descendants\"; cd data/verification/sources/web && f=$(python3 -c \"\nimport hashlib;print(hashlib.sha1('https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/jā́mātā'.encode()).hexdigest()[:16]+'.txt')\"); echo $f; grep -n -A30 \"Descendants$\" $f | tail -40; grep -n -A6 \"Etymology$\" $f | tail -15"
}
```


### [2026-09-05T20:42:44.659Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/c24b37d6b23fc7e2.txt
c24b37d6b23fc7e2.txt
221: Descendants
222- [ edit ] 
223-
224- Central Iranian:
225- Avestan: 𐬰𐬁𐬨𐬁𐬙𐬀𐬭 ( zāmātar ) 
226-
227- Northeastern Iranian:
228- ⇒ Sogdian: ( /⁠zāmātē⁠/ ) 
229- Manichaean script: 𐫉𐫀𐫖𐫤𐫀𐫏 ( zʾmtʾy ) 
230- Syriac script: ܢܐܩܬܐܝ ( zʾmtʾy ) 
231-
232- Southeastern Iranian:
233- Proto-Pathan: 
234- Pashto: زوم ( zum ) 
235-
236- Waneci: زوم ( zōm ) 
237-
238- Sanglechi: زنوذ ( zənūδ ) 
239-
240- Yidgha: زمے ( zamai ) 
241-
242- Northwestern Iranian:
243- Baluchi: زامات ( zāmāt ) 
244-
245- Kurdish:
246- Northern Kurdish: zava 
247- Central Kurdish: زاوا ( zawa ) 
248- Southern Kurdish: زاوا ( zawa ) 
249- Laki: زوما ( zuma ) 
250-
251- Medo-Parthian:
134: Etymology
135- [ edit ] 
136-
137- From Proto-Indo-Iranian *ȷ́ā́mātā .
138-
139- Noun
140- [ edit ]
```


## [2026-09-05T20:42:46.667Z] TOOL CALL #40: Bash

```json
{
 "command": "cd data/verification/sources/web && sed -n '250,290p' c24b37d6b23fc7e2.txt"
}
```


### [2026-09-05T20:42:46.720Z] TOOL RESULT

```
 Medo-Parthian:
 Caspian:
 Gilaki: زاما ( zāmā ) 

 Old Mazanderani: زوما ( zōmā ) 
 Mazanderani: زاما ( zāmā ) , زما ( zëmā ) 

 Old Median: *zāmātar 
 Middle Median: *zāmātad 
 Karingani: زوما ( zumā ) 

 Kermanic: zumā ( Nayini ) 

 Tafreshi: zāmā ( Ashtiani ) 

 Talysh: ( /⁠zāmā⁠/ ) 
 Arabic script: زاما 
 Latin script: zama 

 Vafsi: زاوا ( zāvā ) 

 Semnani: زوما ( zumā ) 

 Parthian: 𐫉𐫀𐫖𐫀𐫅 ( zʾmʾd /⁠zāmād⁠/ ) 

 Zaza-Gurani:
 Gurani: زەما ( zamā ) 

 Zazaki: zama ( zāmā ) 

 Southwestern Iranian:
 Old Persian: *dāmātar 
 Middle Persian: ( /⁠dāmād⁠/ ) 
 Manichaean script: 𐫅𐫀𐫖𐫀𐫅 ( dʾmʾd ) 
 Book Pahlavi script: [Book Pahlavi needed] ( dʾmʾt' ) 
 Classical Persian: داماد ( dāmād ) 
 Dari: داماد ( dâmâd ) 
 Iranian Persian: داماد ( dâmâd ) 
 Tajik: домод ( domod ) 
 → Alviri-Vidari: دماد ( domād )
```


## [2026-09-05T20:42:58.712Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HUB 532 ===\"; grep -n \"532\\.\" HUB.txt | head; echo \"=== HUB damad ===\"; grep -n -i \"dämäd\\|dāmād\\|damad\" HUB.txt | head"
}
```


### [2026-09-05T20:42:58.781Z] TOOL RESULT

```
=== HUB 532 ===
=== HUB damad ===
4027:dt gestern*, damad 'Brautigam, Schwiegersohn' u. s. w.
7837:1) damad *Schwiegersohn' ^= zd. zamatar-, skr. jama-
```


## [2026-09-05T20:42:59.252Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SYN son-in-law ===\"; grep -n -i \"son-in-law\" SYN.txt | head -10; echo \"=== KLN gamos ===\"; grep -n -i \"\\-gamy\\|gamos, marriage\\|gámos\" KLN_1966.txt | head -10"
}
```


### [2026-09-05T20:42:59.320Z] TOOL RESULT

```
=== SYN son-in-law ===
3421:2.63 SON-IN-LAW 2.64 DAUGHTER-IN-LAW
3517:4, Ir, cliamain ‘relation by marriage’, quotable for ‘father-, son-, and brother- in-law’ : clemnas ‘alliance by marriage’ (root connection?). Hence NIr. cliam- hain ‘son-in-law’ (dial. also ‘father- or mother-in-law’), and bainchliamhain ‘daughter-in-law’ (ban- ‘female’).
3519:5. Goth. mégs ‘son-in-law’, ON magr ‘father-, son-, or brother-in-law’, mag- kona ‘mother-, daughter-, or sister-in- law’, Sw. mdg (obs.), ODan., Norw. maag ‘son-in-law’ : OE m@g, OHG mag ‘relative’, all perh. (cf. Fr. beau-pére, etc.) : Lith. mégti ‘be pleasing’. Walde- P. 2.256. Feist 352.
3526:2. Grk. sevfepds, in Homer only ‘wife’s father’, later generalized at the expense of éxupds (and sometimes used also for ‘son-in-law, brother-in-law’), fem. evOepa : Skt. bandhu- ‘relative’, bandh- ‘bind’, IE *bhendh-. Walde-P. 2.152.
3542:9,63. ‘Son-in-law’. 1. Grk. yauBpes mostly ‘son-in-law’, but also ‘prother-in- law’, ‘father-in-law’, ‘relative | by, riage’, NG ‘bridegroom’, ‘son-in-law ©: ‘sister's husband’ : apes ‘marriage . From the same root also Skt. gamatar-, Av. zamatar-, with suffix as in pitar- matar-, etc. Walde-P. 1.574.
3544:3. W. daw, Br. deun, MBr. deuff, OCorn. dof : Ir. dam ‘a following, band’, Nir. damh ‘tribe, family’, with speciali- zation of ‘relative’ to ‘son-in-law’. Walde-P. 1.764. Pederson 1.48.
3568:2. Grk. yapBpds ‘son-in-law’ (2.63), also ‘husband’s or wife’s brother’, NG also ‘sister’s husband’.
3573:OE adum ‘son-in-law’ (2.63) also ‘sister’s husband’.
3701:’ OF mdagas, OHG maga : Goth. mégs ‘son-in-law’, ON magr ‘father-, son-, or brother-in-law’, etc. (2.61-2.66).
=== KLN gamos ===
2289:allogamy,  n.,  cross-fertilization  (hot.)  —  Com¬ pounded  of  alio-  and  Gk.  -yap-ia,  fr.  Ydn°c, ‘marriage’.  See  -gamy.
4038:autogamy,  n.,  self-fertilization  (bot.)  —  Com¬ pounded  of  auto-  and  Gk.  -yapua,  fr.  yapioc, ‘marriage’.  See  -gamy.
4964:bigamia,  a  hybrid  coined  fr.  L.  bi-  and  Gk. yay.o;,  ‘wedding,  marriage’,  which  is  rel.  to Y«(Ji.eLV,  ‘to  take  to  wife,  to  marry’,  yap.(3p6e, ‘son-in-law,  brother-in-law,  father-in-law’,  fr. I.-E.  base  *gem(e)-,  ‘to  marry’,  whence  also  OI. jamih,  ‘brother,  sister’,  jama,  ‘daughter-in-law’, jima-tar,  Avestic  zama-tar, ‘son-in-law’, h.gener (for  *gemer),  ‘son-in-law’  (for  the  change  of  m to  n  see  gener).  Cp.  Gamelion,  gamete,  gamo-, -gamy.  For  the  difference  in  meaning  between bigamy  and  digamy  see  digamy.
7884:cleistogamy,  n.,  self  fertilization  of  certain  closed flowers  ( bot .)  —  Compounded  of  cleisto-  and Gk.  -yapda,  fr.  y afio?,  ‘marriage’.  See  -gamy. Derivatives:  cleistogam-ic,  adj.,  cleistogam-ic: al-ly,  adv.
9818:Derivatives:  cryptodir-an,  cryptodir-ous,  adjs. cryptogam,  n.,  one  of  the  group  of  plants  which have  no  external  flowers  and  seeds.  —  F.  cryp¬ togame,  fr.  Gk.  xpuTrrop,  ‘hidden’,  and  ydcpiop, ‘marriage’.  See  crypto-  and  -gamy.
11314:dich-,  form  dicho-  befote  a  vowel, dichlamydeous,  adj.,  having  calyx  and  corolla (bot.)  —  Formed  with  suff.  -ous  fr.  Gk. gen.  x^apuSoq,  ‘mantle,  cloak’.  See  chlamys. dicho-,  before  a  vowel  dich-,  combining  form meaning  ‘in  two,  asunder’.  —  Gk.  8ixo-,  Six-, fr.  8ixa,  ‘in  two,  asunder,  apart  from,  separate¬ ly’,  which  is  rel.  to  Si?,  ‘twice’.  See  di-,  ‘two’, and  cp.  disso-  and  the  first  element  in  dittography . dichogamous,  adj.,  characterized  by  dichogamy (bot.)  —  See  next  word  and  -ous. dichogamy,  n„  maturation  of  the  stamens  and pistils  at  different  times  (bot.)  —  Compounded of  Gk.  8txa,  ‘in  two,  apart’,  and  yxpoc,  ‘mar¬ riage’.  See  dicho-  and  -gamy, dichotomous,  adj.,  branching  in  pairs  (bot.)  — See  next  word  and  -ous.
11386:digamous,  adj.,  married  for  a  second  time.  — Late  L.  digamus,  fr.  Gk.  Siyapop,  fr.  81-  (see  di-, ‘two’)  and  yapot;,  ‘marriage’.  See  -gamy  and -ous.
11387:digamy,  n.,  second  marriage  (in  contradistinction to  bigamy,  which  denotes  the  state  of  having two  wives  or  husbands  at  the  same  time).  —  Late L.  digamia,  fr.  Gk.  Siyapla,  ‘a  second  marriage’, fr.  81-  (see  di-,  ‘two’)  and  yapoi;,  ‘marriage’. See  -gamy  and  cp.  monogamy,  bigamy,  poly¬ gamy.
13123:Derivative:  endoderm-ic,  adj. endodontitis,  n„  inflammation  of  the  pulp  of  a tooth  called  also  pulpitis  (med.)  —  Medical  L., coined  fr.  end-,  odont-  and  suff.  -itis. endogamy,  n.,  marriage  within  the  tribe  or  clan (anthropol.)  —  Lit.  ‘in-marriage’;  compounded of  endo-  and  -gamy.  Cp.  exogamy.
14055:ex  officio.  —  L.,  ‘by  virtue  of  an  office’,  formed fr.  ex,  ‘out  of’,  and  abi.  of  officium,  ‘service; office’.  See  ist  ex-  and  office, exogamy,  n.,  marriage  outside  the  tribe  or  clan ( anthropo! .)  —  Lit.  ‘outside  marriage’;  com¬ pounded  of  exo-  and  -gamy.  Cp.  endogamy. Derivatives:  exogam-ic,  exogam-ous,  adjs. Exogenae,  n.pl.,  the  Dicotyledones  (bot.)  — ModL.,  lit.  ‘growing  outside’  (see  exo-  and
```


## [2026-09-05T20:43:13.451Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HUB ctx ===\"; sed -n '7830,7845p' HUB.txt; echo \"leaf:\"; python3 -c \"\nd=open('HUB.txt',encoding='utf-8',errors='replace').read().split('\\n')\npre='\\n'.join(d[:7836]); print(pre.count('\\f'))\"; echo \"=== SKT polygamy ===\"; grep -n -i \"polygamy\\|Polygamy\" SKT.txt | head -5"
}
```


### [2026-09-05T20:43:15.375Z] TOOL RESULT

```
=== HUB ctx ===
idg. ks =^ ap. xs, idg. kh ^= ap, s siehe Kap. 23; idg.
sk\ sk^h = ap. s siehe § 98, d und 104; idg. sm ^ ap. m
siehe § 154, c; idg. sn = zd. sn = ap. — ? siehe § 148, f.
Kapitel 20: ap. ^ und d = idg. g^, g^h,
(ap. zd = idg. s oder Dental + d, dh).
Ap. z und d {= iran, 2^ =^ idg. jr*, g^A) = np. 2: und rf.
§ 110. Ap. d (= iran. z) = np. d:
1) damad *Schwiegersohn' ^= zd. zamatar-, skr. jama-
tar"; 2) danad er weiss', ap. adana er wusste', gd. zanata
2. pi. ; skr. jfanati; 3) rfws^ 'Hand' = ap. dasta-, zd. zasta-^
skr. hasta-, arm. dast-ak, dasf-a-kert; 4) di? *Herz' = zd.
zered'^ zaredaya- (vd. 1,3), skr. Ard-, hrdaya-] 5) d(Js^
Treund' — dostar = ap. daustar-, vgl. zd. zaosa-, skr. y^/s ;
6) dahan 'Mund* = zd. zafan-^ 7) d^, df^ gestern = skr.
%as; darj/a *Meer' = ap. dray a- (oder drayah- ZDM6. 46,
298), zd. zrayah-, aber dial, zarah^); 9) ap. adam *ich' —
leaf:
230
=== SKT polygamy ===
1772:polygamy,  maniage  with  many (Gk.)     Gk.  ToAvya^itt.  —  Gk. marrying  many  (sec  Poly-)-
```


## [2026-09-05T20:44:35.449Z] TOOL CALL #44: Bash

```json
{
 "command": "ls site/pages/170.jpg 2>/dev/null; pdftoppm -f 170 -l 170 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg170 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


### [2026-09-05T20:44:37.531Z] TOOL RESULT

```
site/pages/170.jpg
total 17748
drwx------ 2 sfmqrb sfmqrb    4096 Sep  5 16:44 .
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
-rw-rw-r-- 1 sfmqrb sfmqrb    7816 Sep  5 16:35 c_am2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   14765 Sep  5 16:35 c_am3.png
-rw-rw-r-- 1 sfmqrb sfmqrb   10038 Sep  5 16:35 c_empty2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4123 Sep  5 16:34 crop_am.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4986 Sep  5 16:34 crop_arabic_refs.png
-rw-rw-r-- 1 sfmqrb sfmqrb    7702 Sep  5 16:34 crop_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb   16978 Sep  5 16:34 crop_morocco.png
-rw-rw-r-- 1 sfmqrb sfmqrb  944060 Sep  5 16:18 kent.txt
-rw-rw-r-- 1 sfmqrb sfmqrb     222 Sep  5 16:30 leaf.py
-rw-rw-r-- 1 sfmqrb sfmqrb   57617 Sep  5 16:20 mk129.py
-rw-rw-r-- 1 sfmqrb sfmqrb   74680 Sep  5 16:26 mk131.py
-rw-rw-r-- 1 sfmqrb sfmqrb   33365 Sep  5 16:25 mk133.py
-rw-rw-r-- 1 sfmqrb sfmqrb   42635 Sep  5 16:29 mk140.py
-rw-rw-r-- 1 sfmqrb sfmqrb   51288 Sep  5 16:30 mk143.py
-rw-rw-r-- 1 sfmqrb sfmqrb   11831 Sep  5 16:32 node4.png
-rw-rw-r-- 1 sfmqrb sfmqrb    7427 Sep  5 16:32 node7.png
-rw-rw-r-- 1 sfmqrb sfmqrb  944060 Sep  5 16:13 oldpers_djvu.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    6054 Sep  5 16:36 p152_e0left.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2672 Sep  5 16:36 p152_node2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   22067 Sep  5 16:29 part0.json
-rw-rw-r-- 1 sfmqrb sfmqrb   14156 Sep  5 16:22 part1.json
-rw-rw-r-- 1 sfmqrb sfmqrb   17147 Sep  5 16:44 part_a.json
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
-rw-rw-r-- 1 sfmqrb sfmqrb   86005 Sep  5 16:39 pg168.png
-rw-rw-r-- 1 sfmqrb sfmqrb   68420 Sep  5 16:42 pg169.png
-rw-rw-r-- 1 sfmqrb sfmqrb   37351 Sep  5 16:44 pg170.png
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


## [2026-09-05T20:44:40.778Z] TOOL CALL #45: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg170.png"
}
```


### [2026-09-05T20:44:41.112Z] TOOL RESULT

```

```


## [2026-09-05T20:44:41.108Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-05T20:44:56.755Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && grep -n \"داماد\" ARY_pages.txt | head -10; echo \"=== latin index ===\"; grep -n -i \"DAMAD\\|GEM\\|jamatar\" ARY_latin_index_pages.txt | head -10"
}
```


### [2026-09-05T20:44:56.813Z] TOOL RESULT

```
1022:بودندکه با تأید و تحت نظ رکاهتان انجام می‌شد. ضمناً ازدواج نوعی معامله هم بود: داماد یا ایل او به
9336:چم این واژه در زبان اسلاوی کهن: شوهر دختر والدین؛ داماد,
14655:سر دی (8(72/577): لراایا 4 (۸۱/8) داماد هم
15018:آلبانی (8۸/]41ظ.اهم): ال 6 (08۸0507) داماد ای
=== latin index ===
442:[esis Fe | Geman | Dah ——_—| St
545:f 9M cashen caojly ple b cy Sle slaeSly acean Geman cul 02g "AGRAS*
596:Set 9 (2A ST Ay ND CY eee ague) ogSegem slaglj & y (CUNEIFORM) ho
1082:Was aUT Mey sing ates SRar Gd gemFa parlgT wal py daisy chie
1961:Pe sabi ub, GOTI,GEMO (LITHUANIAN) gly)
2639:WATROBA (POLISH) gem) ENTERON, ENTERA (GREEK) gi y
5255:UT ela ysttes aBANTT-PAOCAH 103 gol glen 6b (Spa S53, 4) gem aoe
6609:CZWARTY (POLISH) gem) TURIVAS, CATURTHAS
7588:JAMATAR SANSKRIT) ey Suite ZAMATAR HAVESTAN) ikea 3\ :
7589:GAM, GAMEO- GREEK) gb y DAMAD, DAMAT — (PAHLAVI) 5 shy
```


## [2026-09-05T20:45:01.324Z] TOOL CALL #47: Bash

```json
{
 "command": "python3 tools/fetch_source.py \"https://www.sanskritdictionary.com/?iencoding=iast&q=j%C4%81m%C4%81&lang=sans&action=Search\" --note \"p170 Sanskrit jama gloss\" >/dev/null; python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/%E0%A4%9C%E0%A4%BE%E0%A4%AE%E0%A4%BE\" --note \"p170 Sanskrit jama\" >/dev/null; cd data/verification/sources/web && python3 - <<'EOF'\nimport hashlib\nfor u in [\"https://www.sanskritdictionary.com/?iencoding=iast&q=j%C4%81m%C4%81&lang=sans&action=Search\",\"https://en.wiktionary.org/wiki/%E0%A4%9C%E0%A4%BE%E0%A4%AE%E0%A4%BE\"]:\n    f=hashlib.sha1(u.encode()).hexdigest()[:16]+'.txt'\n    t=open(f,encoding='utf-8',errors='replace').read()\n    print('==',u,len(t)); print(t[:1500])\nEOF"
}
```


### [2026-09-05T20:45:03.816Z] TOOL RESULT

```
== https://www.sanskritdictionary.com/?iencoding=iast&q=j%C4%81m%C4%81&lang=sans&action=Search 186
URL: https://www.sanskritdictionary.com/?iencoding=iast&q=j%C4%81m%C4%81&lang=sans&action=Search
FETCHED: 2026-09-05T20:45:03Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 403: Forbidden
== https://en.wiktionary.org/wiki/%E0%A4%9C%E0%A4%BE%E0%A4%AE%E0%A4%BE 3467
URL: https://en.wiktionary.org/wiki/%E0%A4%9C%E0%A4%BE%E0%A4%AE%E0%A4%BE
FETCHED: 2026-09-05T20:45:03Z
STATUS: 200
TITLE: जामा - Wiktionary, the free dictionary

जामा - Wiktionary, the free dictionary 

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
 Hindi 

 Toggle Hindi subsection 

 1.1 
 Pronunciation 

 1.2 
 Etymology 1 

 1.2.1 
 Noun 

 1.2.1.1 
 Declension 

 1.3 
 Etymology 2 

 1.3.1 
 Alternative forms 

 1.3.2 
 Noun 

 2 
 Rajbanshi 

 Toggle Rajbanshi subsection 

 2.1 
 Noun 

 Toggle the table of contents 

 जामा 

 5 languages 

 বাংলা 
 हिन्दी 
 Bahasa Indonesia 
 Malagasy 
 संस्कृतम् 

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

 See also: जमा and जामौ 

 Hindi
 [ edit ] 

 Pronunciation
 [ edit ] 

 ( Stand
```


## [2026-09-05T20:45:13.080Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && sed -n '7580,7595p' ARY_latin_index_pages.txt; echo \"=== nearest page tag ===\"; awk 'NR<=7595 && /pdf page/{l=$0;n=NR} END{print n\": \"l}' ARY_latin_index_pages.txt"
}
```


### [2026-09-05T20:45:15.001Z] TOOL RESULT

```
SKEAT: (TAME) 628 ZAHM, ZAHMEN — (GERMAN) (jlJT
MALLORY & ADAMS: DEMH- HOLD ENGLISH) 4 gdSt
AW ebb olay ‘TAM, TEMIAN
: leadlaak
B27 8s 45 92 o5ls col
ae
|
|
JAMATAR SANSKRIT) ey Suite ZAMATAR HAVESTAN) ikea 3\ :
GAM, GAMEO- GREEK) gb y DAMAD, DAMAT — (PAHLAVI) 5 shy
GENER LATIN) ga) ZAWAT (KURDISH) 2,6 |
GENORE (FRENCH) 4318 JAMATH, JANWATH :(BALUCHI) gz sh '
YERNO (SPANISH) lily! ZOM, ZOMGALI (AFGHAND (5) lil
i
[pdf page 263]
eile [VF
=== nearest page tag ===
7594: [pdf page 263]
```


## [2026-09-05T20:45:23.866Z] TOOL CALL #49: WebFetch

```json
{
 "url": "https://www.wisdomlib.org/definition/jama",
 "prompt": "What does Monier-Williams / Sanskrit dictionaries give for the feminine noun jāmā (जामा)? Quote the gloss (daughter / daughter-in-law?) and any entry for jāmi."
}
```


### [2026-09-05T20:45:29.284Z] TOOL RESULT

```
# Jāmā (जामा) Definitions

According to the Monier-Williams Sanskrit-English Dictionary cited in the article:

**Jāmā (जामा):** "f. a daughter"

The article also notes an alternative definition from the Benfey Sanskrit-English Dictionary:

**Jāmā (जामा):** "f. A daughter-in-law"

The document does not provide a separate dictionary entry for **jāmi** in the excerpts shown, though it is referenced as a related form ("Nebenform von _jāmi_") in the German glossary by Böhtlingk and Roth.
```


## [2026-09-05T20:45:39.075Z] TOOL CALL #50: Bash

```json
{
 "command": "python3 tools/fetch_source.py \"https://www.wisdomlib.org/definition/jama\" --note \"p170 Skt jama gloss (MW: a daughter)\" >/dev/null; cd data/verification/sources/refs && python3 -c \"\nd=open('PHD.txt',encoding='utf-8',errors='replace').read().split('\\n')\npre='\\n'.join(d[:307]); print('PHD leaf idx', pre.count('\\f'), '-> printed', pre.count('\\f')-21)\n\"; echo \"=== NYB ===\"; grep -n -i \"bridegroom\\|d'm't\\|damat\" NYB_vol2_glossary.txt | head -5"
}
```


### [2026-09-05T20:45:42.532Z] TOOL RESULT

```
PHD leaf idx 46 -> printed 25
=== NYB ===
186:QDMTH (Prth): QODAM T EH in his presence, OAram QODAMAT prep. before, in the presence of, more common QODAM, v. MDM QYN? (Prth): v. KYN?
4557:been married to Artaxsér) 9??, 1014 (twice). — Wikander, Mb 9-21. A love scene between a bridegroom (mérak, q.v.), twenty years old, and his bride (ztyānak), fifteen years old, is told in PR 91 sq.
```


## [2026-09-05T20:45:48.802Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nd=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (275,276,277,278):\n    p=d[i]\n    print('--- leaf',i,'first/last lines:')\n    ls=[l.strip() for l in p.split('\\n') if l.strip()]\n    print(ls[:2]); print(ls[-2:])\nEOF"
}
```


### [2026-09-05T20:45:50.642Z] TOOL RESULT

```
--- leaf 275 first/last lines:
['\u202bداغ سو\u202c                                                                                                            \u202bس\u202c', '\u202bری \u202a۱\u202c\u202c']
['\u202b\u200f\u202a . darn\u202cبلوچی \u202a 82۳20\u202cو \u202a . 082084\u202cوخی\u202a . 0۳2-۲10-2۷\u202cسربکلی \u202a« 0012-۲6۳0\u202cاسشق\u202c', '\u202bپنداشتن \u202a۰\u202c\u202c       \u202b؛ دارابردن » مالك بودن \u202a-\u202cتصرف کردن \u202a-\u202cنگاهداشتن\u202c                        \u202b\u202a۷\u202c\u202c']
--- leaf 276 first/last lines:
['\u202b”\u202a“AI\u202c\u202c                                                                                                          \u202bداغ شدن\u202c', '\u202bدالیز و\u202a٩\u202c\u200f تست س بای اد و فتح زای\u202c                                       \u202bداع شدن \u202a -\u202cبنایتآزرده شدن باشد\u202a.\u202c\u202c']
['\u202b\u202a .\u202cرك \u202a 3\u202cمزدستا\u202c                 \u202bاوستا کلمه\u200cای که شه یمه مزبور باشد نت\u202c             \u202bنك\u202c   \u202bوک در نامهای \u202a۱۳\u202c\u202c', '\u202bبرابر صفحهٌ \u202a. ۵۲۱\u202c\u202c']
--- leaf 277 first/last lines:
['\u202bدامن بدندا نکرفتن\u202c                                                                           \u202b\u202a ۷۱\u202cرس\u202c', '\u202bگفته\u200cاند \u202a. ۴\u202c\u202c     \u202bدام = بروزن رام» نقیض ددباشد که\u200cآن\u202c']
['\u202bدگلتان \u202a. ۹۳۰\u202c\u202c', '\u202bوبای کوه \u202a۰\u202c\u202c   \u202bدبال \u202a -\u202cکناره\u202a-\u202cچادربادبان کشتی\u202a -\u202cکنارة کو\u202c']
--- leaf 278 first/last lines:
['\u202bبح\u202c        \u202bیز\u202c', '\u202bسله وسبدی باشد بز رکه که دوچوب بدروطرف\u202c                        \u202bدامن بارفشاندن ک»نابه از سفر\u202c']
['\u202b\u202a = ۸\u202cدانج ابروج \u202a .\u202cیز دالج [\u202a 612\u202cقرائت شده\u200cولی\u200cشکل فارسی آن دانك \u202a616020\u202c\u202c', '\u202b\u202a ( e.e\u202cرایج\u200cتراست \u202a« .\u202cلك \u202a۲\u202cص \u202a.*۷\u202c\u202c               \u202b\u202a12040\u202c\u200f\u202c']
```


## [2026-09-05T20:45:59.050Z] TOOL CALL #52: Bash

```json
{
 "command": "timeout 300 python3 tools/ref_page.py BQT:817 --image 2>&1 | tail -20"
}
```


### [2026-09-05T20:46:01.201Z] TOOL RESULT

```
no scan of BQT covers printed page 817 (see 'scans' in refs_online.json)
```


## [2026-09-05T20:46:13.020Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && grep -n \"zāmātar\\|zamatar\\|jāmātar\\|jamatar\\|gamos\\|Y«ho\\|Schwiegersohn\" WLD_Bd1_pages.txt | head -20"
}
```


### [2026-09-05T20:46:13.073Z] TOOL RESULT

```
54629:                                  ..Schwiegersohn* ',                 -
54631:gloss, gent a Schwiegersohn *, Kiedermann Mel. Meillet 109 f., teils nach genus                                                    ,
54646:des Schwiegersohns *, auch ai. jiuni „verschwistert, verwandt* fern, nachved.                                                 -
54660:,, Schwiegersohn   (ebenfalls nach den Yerwandtschaftsnamen auf-fer? Oder
54667:lat. gloss, genta ..Schwiegersohn   (s. o. *gem-ta), lit. 1 an fas ,, Schwiegersohn" ;
54671:aksl. zetb   „Schwiegersohn, Schwager, Schwiegervater".                             Siehe aber        S.   577!
54692:daB eine Bezeichnung des Schwiegersohns als „Geschlechtsangehorigen oder
72308:relationship", acymr. dauu „cliens“, ncymr. daw, dawf „Schwiegersohn“
```


## [2026-09-05T20:46:15.913Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && sed -n '54636,54670p' WLD_Bd1_pages.txt; echo \"=== page tag ===\"; awk 'NR<=54660 && /pdf page/{l=$0;n=NR} END{print n\": \"l}' WLD_Bd1_pages.txt"
}
```


### [2026-09-05T20:46:17.670Z] TOOL RESULT

```
Gdf. * jpudfo-s) ai .jamutar-. a v. sumatar ,,Tochtermann *, nach den andern
                                        ;
                                                                                                                 -




Yerwandtschaftsnamen auf -tar- geschaffene Erweiterung, mit a der zweiten
Silbe nach matar-; zugrunde liegt kiirzeres *jama-, vgl. av. zamaoya ,,Bruder
                                                         -
des Schwiegersohns *, auch ai. jiuni „verschwistert, verwandt* fern, nachved.                                                 -
                                                                                                                              ',


„weibliche Yerwandte, bes. Sehwiegertochter '*, ved. rijami- etwa „ver-                             -




schwagert**, jama ^Schwiegertochter            alb. tosk.    <3 aider,   geg. dander
                                                                                         1-
                                                                                              ;


,, Schwiegersohn   (ebenfalls nach den Yerwandtschaftsnamen auf-fer? Oder
                                            *



Kr euzung der gleich zu nennenden ABildungen mit der obigen /-Bildung?j
                                                                            --
lat. gloss, genta ..Schwiegersohn   (s. o. *gem-ta), lit. 1 an fas ,, Schwiegersohn" ;
                                   gembh-, gmbh-, gombhos                                                      575

(*ge»w-tos; -nt- gegeniiber bewahrtem nit im schleifenden simtas „hundert"),
=== page tag ===
:
```


## [2026-09-05T20:47:00.165Z] TOOL CALL #55: Bash

```json
{
 "command": "cd data/verification/sources/web && grep -n -i -A6 \"polygamy (n\" e9b0d6e2201c3b03.txt | head -30; echo \"===\"; grep -n -i \"polygamia\\|1590\\|from Greek\" e9b0d6e2201c3b03.txt | head -10"
}
```


### [2026-09-05T20:47:00.221Z] TOOL RESULT

```
23: polygamy (n.) 
24-
25- "marriage with more than one spouse," 1590s, from Late Latin polygamia , from Late Greek polygamia "polygamy," from polygamos "often married," from polys "many" (see poly- ) + gamos "marriage" (see gamete ). The word is not etymologically restricted to marriage of one man and multiple women (technically polygyny ), but often used as if it were. Related: Polygamist; polygamize .
26-
27- In Christian countries, when a man has more wives than one, or a woman more husbands than one, at the same time, he or she is punishable for polygamy ; but if there was a separate marriage with each the first marriage would be valid notwithstanding the subsequent ones, and the later ones would be void. The offense of contracting the subsequent marriage is now termed 
28- bigamy . But polygamy in the form of polygyny is allowed in some countries, especially among Mohammedans, and was held a matter of faith and duty by the Mormons. [Century Dictionary, 1895]
29- also from 1590s 
===
25: "marriage with more than one spouse," 1590s, from Late Latin polygamia , from Late Greek polygamia "polygamy," from polygamos "often married," from polys "many" (see poly- ) + gamos "marriage" (see gamete ). The word is not etymologically restricted to marriage of one man and multiple women (technically polygyny ), but often used as if it were. Related: Polygamist; polygamize .
29: also from 1590s 
35: "sexual protoplasmic body," 1880, coined 1878 by German cytologist Eduard Strasburger (1844-1912), the widespread attribution of the word's coinage to Mendel being apparently erroneous. From Greek gamete "a wife," gametes "a husband," from gamein "to take to wife, to marry," from PIE root *gem(e)- "to marry" (source also of Greek gambros "son-in-law, father-in-law, brother-in-law;" Sanskrit jamih "brother, sister," jama daughter-in-law;" Avestan zama-tar "son-in-law;" Latin gener "son-in-law"). See also -gamy . The seventh month of the ancient Attic calendar (corresponding to late January and early February) was Gamelion , "Month of Marriages." Related: Gametal .
39: 1780, "condition of having many wives, marriage or cohabitation of one man with more than one woman at the same time," from Greek poly gynēs "having many wives," from polys "many" (see poly- ) + gynē "woman, wife" (from PIE root *gwen- "woman"). Related: Polygynous .
```


## [2026-09-05T20:47:05.311Z] TOOL CALL #56: Bash

```json
{
 "command": "python3 tools/fetch_source.py \"https://abadis.ir/fatofa/داماد/\" --note \"p170 Moin entry damad (MON:1487)\" ; f=$(python3 -c \"\nimport hashlib;print(hashlib.sha1('https://abadis.ir/fatofa/داماد/'.encode()).hexdigest()[:16]+'.txt')\"); grep -n -i -m3 -A6 \"معین\" data/verification/sources/web/$f | head -40"
}
```


### [2026-09-05T20:47:08.642Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/2f987fae4ff0206e.txt
58: فرهنگ معین
59-
60- [ په . ] (اِ. ) ۱ - مرد تازه زن گرفته . ۲ - شوهر دختر یا خواهر. 
61-
62- فرهنگ عمید
63-
64- ۱. مردی که تازه زن گرفته و عروسی کرده: مجو درستی عهد از جهان سست نهاد / که این عجوزه عروس هزار داماد است (حافظ: ۹۰ ).
--
142:فرهنگ فارسی معین
143-فرهنگ فارسی هوشیار
144-
145- شاه بالا
146-
147- معادل کلمه داماد در ترکی = کورَکَن ، گورکان
148-
--
210: آبادیس از سال 1385 فعالیت خود را در زمینه فن آوری اطلاعات آغاز کرد. نخستین پروژه آبادیس، سایت دیکشنری آبادیس بود. دیکشنری آنلاین آبادیس از ابتدا تاکنون تغییرات بسیاری کرده و ویژگی های مختلفی به آن اضافه شده است. آبادیس افزونه ای کاربردی برای مرورگرهای فایرفاکس و کروم و اپلیکیشن موبایل طراحی کرده است که میتوانید از لینک های بالا دانلود کنید. دیکشنری آبادیس شامل بخش هایی نظیر دیکشنری به زبان های مختلف از جمله انگلیسی، فارسی، عربی و همچنین بیست دیکشنری تخصصی با تلفظ انگلیسی و آمریکایی، ترجمه مخفف و کلمات اختصاری، مترجم آنلاین متن، لغتنامه دهخدا، فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راهنمای انتخاب اسم و ... می باشد. 
211-
212- لینک ها 
213-
214- حقوق این سامانه وابسته به دیکشنری آبادیس می باشد. 
215-
216- استفاده از نوشتارهای این دیکشنری، با ذکر منبع، آزاد است.
```


## [2026-09-05T20:47:16.771Z] TOOL CALL #57: Bash

```json
{
 "command": "sed -n '1,80p' tools/verify_check.py"
}
```


### [2026-09-05T20:47:16.814Z] TOOL RESULT

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


## [2026-09-05T20:47:18.838Z] TOOL CALL #58: Bash

```json
{
 "command": "sed -n '80,140p' tools/verify_check.py"
}
```


### [2026-09-05T20:47:18.879Z] TOOL RESULT

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


## [2026-09-05T20:50:57.993Z] TOOL CALL #59: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk170.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\n\nroot_entry = {\n  \"entry\": 0,\n  \"root\": \"Geme, Gem\",\n  \"verdict\": \"confirmed\",\n  \"modern_form\": \"PIE *ǵem- (alternative reconstruction *ǵemH-) 'to marry'\",\n  \"note\": \"The root box is right on all three counts. Pokorny's lemma reads 'Root / lemma: gem(e)- , Meaning: to marry , Page(s): 369-370', and its material is exactly the material of this chart (Skt. jāmātar-, Av. zāmātar-, Gk. gámos, gambrós, Lat. gener); Watkins in the AHD appendix has 'geme-. To marry. Suffixed zero-grade form *gmo-o- in Greek gamos, marriage: GAMETE, GAMO-, -GAMOUS, -GAMY [Pok. gem(e)- 369]', which is where Nourai's Greek and English boxes come from verbatim. Wiktionary reconstructs the same root *ǵem- 'to marry' (alt. *ǵemH-). Two things are worth saying across the whole chart. (1) The Avestan box's first word, jāma, is not an attested Avestan form: it is the short stem that Walde-Pokorny I 574 ('zugrunde liegt kürzeres *jāma-') and Mann IEC 402 ('Av. jāma, n. kinship') posit behind zāmātar-; in Avestan phonology it would have to appear as *zāma-, which is precisely what Bartholomae reconstructs from the attested derivative zāmaoya- 'brother of the son-in-law' (AiW 1691). Nourai copied Mann's Indic-style spelling and Mann's language label with it. (2) The d- of Pahlavi dāmāt / Persian dāmād against Avestan z- is not an irregularity: it is the regular South-west Iranian (Old Persian) treatment of Proto-Iranian *ȷ́ (< PIE *ǵ/*ǵʰ), the same correspondence as dast : Av. zasta-, dānestan : Av. zan-, del : Av. zərəd-, dahān : Av. zafan-, which Hübschmann sets out as a list in Persische Studien §110 with dāmād as his first example. The chart is therefore correct as drawn, only the Avestan box needs the caveat above.\",\n  \"note_fa\": \"ریشه کاملاً درست است: پوکورنی در صفحهٔ ۳۶۹–۳۷۰ مادهٔ gem(e)- را با معنای «ازدواج کردن» آورده و مواد همین ماده در فرهنگ او دقیقاً همان چیزی است که نمودار نشان می‌دهد (سنسکریت jāmātar-، اوستایی zāmātar-، یونانی gámos و gambrós، لاتینی gener)؛ واتکینز در پیوست فرهنگ American Heritage نیز «geme- ازدواج کردن … یونانی gamos» را با ارجاع به همان صفحهٔ پوکورنی آورده و ویکی‌واژه ریشه را *ǵem- بازسازی می‌کند. دو نکته دربارهٔ کل نمودار گفتنی است: نخست آنکه واژهٔ jāma در جعبهٔ «اوستایی» صورتی اوستایی و شاهددار نیست، بلکه ستاک کوتاهی است که والده-پوکورنی (ج۱ ص۵۷۴) و مان (ص۴۰۲) در پسِ zāmātar- بازسازی کرده‌اند و در اوستایی می‌بایست *zāma- باشد (بارتولومه آن را از zāmaoya- «برادرِ داماد» استنتاج می‌کند)؛ نورایی املای هندی مان را با همان برچسبِ زبانی رونویسی کرده است. دوم آنکه «د» در dāmād در برابر «ز» اوستایی بی‌قاعده نیست، بلکه بازتاب منظم پارسی باستان و شاخهٔ جنوب‌غربی ایرانی از *ȷ́ ایرانی آغازین است؛ همان تناظری که در دست/zasta-، دانستن/zan-، دل/zərəd-، دهان/zafan- دیده می‌شود و هوبشمان در «مطالعات فارسی» بند ۱۱۰ فهرست کرده و نخستین نمونه‌اش همین داماد است.\",\n  \"sources\": [\n    W + \"Reconstruction:Proto-Indo-European/ǵem-\",\n    \"https://www.etymonline.com/word/polygamy\"\n  ],\n  \"ref_check\": [\n    {\"ref\": \"POK:369\", \"status\": \"supports\",\n     \"note\": \"POK_full.txt (search 'Root / lemma: gem(e)-'): 'Root / lemma: gem(e)- | Meaning: to marry | Material: Old Indic jāmātar-, Avestan zāmātar- ... created after other relationship names in -tar- extension, with ā of the second syllable after mātar-; the basic root has been abbreviated *jāma-, compare Avestan zāmaoya- brother of son-in-law ... gr. gámos m. wedding; gambrós (*gem-ro-) son-in-law; Latin gener ... References: WP. I 574 f. | Page(s): 369-370'. Nourai's root name, language label, gloss and page are all Pokorny's own.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"WLD\", \"where\": \"Bd. I p. 574 (incoming/WLD/WLD_Bd1_pages.txt, grep 'Schwiegersohn')\", \"stance\": \"supports\",\n     \"note\": \"'ai. jāmātar-, av. zāmātar- \\\"Tochtermann\\\", nach den andern Verwandtschaftsnamen auf -tar- geschaffene Erweiterung, mit ā der zweiten Silbe nach mātar-; zugrunde liegt kürzeres *jāma-, vgl. av. zāmaoya \\\"Bruder des Schwiegersohns\\\" ... ved. vi-jāmi- ... jāmā \\\"Schwiegertochter\\\"' — the source Pokorny himself refers to (WP I 574 f.).\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. geme- (AHD_watkins1985.txt)\", \"stance\": \"supports\",\n     \"note\": \"'geme-. To marry. Suffixed zero-grade form *gmo-o- in Greek gamos, marriage: GAMETE, GAMO-, -GAMOUS, -GAMY; GAMOSEPALOUS. [Pok. gem(e)- 369.]'\"},\n    {\"src\": \"IEC\", \"where\": \"Mann p. 402 (IEC.txt, leaf 234)\", \"stance\": \"partial\",\n     \"note\": \"Mann has no root entry *ĝem-; he files the family under noun stems: '(ĝn̥-mātr- son-in-law. Only in Skt. jāmātr̥, Av. zāmātar, Romani gamutro)' and 'ĝn̥mos, ā generation, mating ... Skt. jāmā daughter; cf. jāmiḥ sibling, twin; Av. jāma, n. kinship; Per. cf. dā- (in dā-mād son-in-law); Gk. gámos marriage'. Same family, different presentation.\"},\n    {\"src\": \"SYN\", \"where\": \"Buck 2.63 'Son-in-law' (SYN.txt)\", \"stance\": \"supports\",\n     \"note\": \"'Grk. gambrós ... : gámos marriage. From the same root also Skt. jāmātar-, Av. zāmātar-, with suffix as in pitar-, mātar-, etc. Walde-P. 1.574.'\"},\n    {\"src\": \"KLN\", \"where\": \"s.v. bigamy (KLN_1966.txt)\", \"stance\": \"supports\",\n     \"note\": \"'Gk. gamos, wedding, marriage, which is rel. to gamein, to take to wife, to marry, gambros ... fr. I.-E. base *gem(e)-, to marry, whence also OI. jāmiḥ, brother, sister, jāmā, daughter-in-law, jāmātar-, Avestic zāmātar-, son-in-law, L. gener (for *gemer)'.\"}\n  ],\n  \"nodes\": []\n}\n\nnodes = []\n\nnodes.append({\n  \"id\": 1,\n  \"lang\": \"Avestan\",\n  \"words\": \"jâma; zâmâ-tar\",\n  \"verdict\": \"plausible\",\n  \"derivation\": \"zāmātar- (Nourai prints it 'zâmâ-tar') is a genuine Young Avestan noun 'son-in-law': Bartholomae, AiW col. 1691, 'j. zāmātar- m. \\\"Eidam, Schwiegersohn\\\"', attested Yt 10.116 antarə zāmātrəm zāsurəmca 'between son-in-law and father-in-law'. It continues Proto-Iranian *ȷ́ā́mātā < Proto-Indo-Iranian *ȷ́ā́mātā < PIE *ǵem-, the PIE palatal *ǵ giving Indo-Iranian *ȷ́ and then Avestan z (Skt. jāmātṛ-, with the same -tar- kinship suffix taken over from pitar-, mātar-, and the ā of the second syllable analogical to mātar-, as Walde-Pokorny I 574 explains). The first word of the box, jāma 'kinship (daughter)', is the problem: no Avestan *jāma- is attested, and Avestan phonology cannot produce j- here. It is the short base stem *jāma- that Walde-Pokorny I 574 posits behind zāmātar- ('zugrunde liegt kürzeres *jāma-') and which Bartholomae, working inside Avestan, reconstructs as *zāma-, inferred from the attested derivative *zāmaoya- 'brother of the son-in-law' (AiW 1691, F. 20). Nourai's immediate source is Mann IEC 402, who prints 'Av. jāma, n. kinship' with the Indic j-; Nourai copied both the form and the label. Read as 'Old Iranian/Indo-Iranian *ǵāma- (Av. *zāma-)' the box is right; read literally as Avestan it is not.\",\n  \"derivation_fa\": \"zāmātar- (که نورایی «zâmâ-tar» نوشته) واژه‌ای اصیل در اوستای متأخر به معنی «داماد» است؛ بارتولومه در «فرهنگ ایرانی باستان» ستون ۱۶۹۱ آن را با شاهدِ یشت ۱۰/۱۱۶ «antarə zāmātrəm zāsurəmca» (میان داماد و پدرزن) آورده است. این واژه دنبالهٔ ایرانی آغازین *ȷ́ā́mātā و هندوایرانی *ȷ́ā́mātā از ریشهٔ *ǵem- هندواروپایی است؛ کامِ هندواروپایی *ǵ در هندوایرانی *ȷ́ و سپس در اوستایی «ز» شده است (سنسکریت jāmātṛ-)، و پسوند -tar- و کشیدگی مصوت هجای دوم به قیاس mātar- و pitar- افزوده شده است (والده-پوکورنی ج۱ ص۵۷۴). اما واژهٔ نخست این جعبه، jāma، در اوستایی شاهد ندارد و اصلاً از نظر آوایی در اوستایی با «ج» ممکن نیست؛ این همان ستاک کوتاهِ بازسازی‌شدهٔ *jāma- است که والده-پوکورنی در پسِ zāmātar- می‌گذارد و بارتولومه در چارچوب اوستایی آن را *zāma- بازسازی می‌کند (بر پایهٔ zāmaoya- «برادرِ داماد»). مأخذ مستقیم نورایی مان (ص۴۰۲) است که خود نوشته «Av. jāma, n. kinship»؛ نورایی هم صورت و هم برچسب زبانی را رونویسی کرده است. اگر جعبه را «ایرانی باستان *zāma-» بخوانیم درست است، اگر لفظاً «اوستایی jāma» بخوانیم نادرست.\",\n  \"sources\": [\n    W + \"Reconstruction:Proto-Iranian/jā́mātā\",\n    W + \"Reconstruction:Proto-Indo-Iranian/ȷ́ā́mātā\"\n  ],\n  \"ref_check\": [\n    {\"ref\": \"POK:369\", \"status\": \"supports\",\n     \"note\": \"Pokorny 369: 'Old Indic jāmātar-, Avestan zāmātar- \\\"son-in-law\\\" ... the basic root has been abbreviated *jāma-, compare Avestan zāmaoya- \\\"brother of son-in-law\\\"' — supports zāmātar- and shows that *jāma- is a reconstructed base, not an Avestan word.\"},\n    {\"ref\": \"HRN:117\", \"status\": \"supports\",\n     \"note\": \"Horn, Grundriss p. 117 no. 532 (HRN.txt, leaf 139): 'dāmād \\\"Schwiegersohn; Bräutigam\\\" ... aw. zāmātar- \\\"Schwiegersohn\\\"; phlv. dāmāt; ai. jāmātar-; kurd. zawā; afgh. zām, zūmgai; bel. zāmās' — the exact chain Avestan zāmātar- > Pahlavi dāmāt > NP dāmād that the chart draws.\"},\n    {\"ref\": \"IEC:402\", \"status\": \"partial\",\n     \"note\": \"Mann p. 402 (IEC.txt leaf 234) is the source of both words of the box: 'ĝn̥mos, ā ... Skt. jāmā daughter ... Av. jāma, n. kinship; Per. cf. dā- (in dā-mād son-in-law); Gk. gámos marriage' and '(ĝn̥-mātr- son-in-law. Only in Skt. jāmātr̥, Av. zāmātar, Romani gamutro)'. It supports the gloss 'kinship' but Mann's 'Av. jāma' with j- is his own slip; every Iranist source has z-.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"BRT\", \"where\": \"Bartholomae AiW col. 1691 (BRT.txt lines 28086-28087)\", \"stance\": \"partial\",\n     \"note\": \"'j. zāmātar- m. \\\"Eidam, Schwiegersohn\\\": ... antarə zāmātrəm zāsurəmca Yt 10.116' with 'ai. jāmātar-, np. dāmād' — confirms the Avestan word; the neighbouring entry '*zāmaoya- m. \\\"Bruder des Schwiegersohns\\\"' is derived 'Ableitung aus *zāma- m.' (asterisked), i.e. Bartholomae knows no Avestan jāma/zāma as an attested word.\"},\n    {\"src\": \"WLD\", \"where\": \"Bd. I p. 574\", \"stance\": \"partial\",\n     \"note\": \"'ai. jāmātar-, av. zāmātar- \\\"Tochtermann\\\" ... zugrunde liegt kürzeres *jāma-, vgl. av. zāmaoya' — the short stem is explicitly a reconstruction, not an Avestan lemma.\"},\n    {\"src\": \"SYN\", \"where\": \"Buck 2.63\", \"stance\": \"supports\",\n     \"note\": \"'Skt. jāmātar-, Av. zāmātar-, with suffix as in pitar-, mātar-' — supports the -tar- formation of the attested word.\"}\n  ]\n})\n\nnodes.append({\n  \"id\": 2,\n  \"lang\": \"Pahlavi\",\n  \"words\": \"dâmât\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"Middle Persian dāmād 'bridegroom, son-in-law' is written dʾmʾt' in Book Pahlavi (hence Nourai's transliteration dâmât) and dʾmʾd in Manichaean script, which shows the second consonant was already voiced /d/. MacKenzie, Concise Pahlavi Dictionary p. 25: 'dāmād [dʾmʾt' | M 424, N ~] bridegroom, son-in-law', with the abstract dāmādīh 'condition of a bridegroom'. It does not come from the Avestan word itself but from the South-west Iranian cognate: Old Persian *dāmātar- (Wiktionary; unattested but required by the reflex), where Proto-Iranian *ȷ́ regularly yields Old Persian d against Avestan z — Hübschmann, Persische Studien §110 (p. 220) opens his list of that correspondence with exactly this word: 'Ap. d (= iran. z) = np. d: 1) dāmād \\\"Schwiegersohn\\\" = zd. zāmātar-, skr. jāmātar-; 2) dānad ...; 3) dast \\\"Hand\\\" = ap. dasta-, zd. zasta-; 4) dil \\\"Herz\\\" = zd. zərəd-'. The Old Iranian agent-noun ending -tar was reduced in Middle Persian (*-tar > -d, as in the whole -tar class), giving dāmād; the Parthian cognate keeps z-: zʾmʾd /zāmād/.\",\n  \"derivation_fa\": \"فارسی میانهٔ dāmād «داماد» در پهلوی کتابی dʾmʾt' نوشته می‌شود (از همین‌رو آوانویسی نورایی dâmât است) و در خط مانوی dʾmʾd، که نشان می‌دهد همخوان پایانی همان زمان واک‌دار بوده است؛ مکنزی در «فرهنگ کوچک پهلوی» ص۲۵ آورده: «dāmād [dʾmʾt'] bridegroom, son-in-law» با مشتق dāmādīh. این واژه از خودِ صورت اوستایی نمی‌آید، بلکه از همتای جنوب‌غربی آن، یعنی پارسی باستان *dāmātar-، که در آن *ȷ́ ایرانی آغازین به‌قاعده در پارسی باستان «د» می‌دهد در برابر «ز» اوستایی؛ هوبشمان در بند ۱۱۰ «مطالعات فارسی» (ص۲۲۰) فهرست این تناظر را با همین واژه آغاز می‌کند: «dāmād = اوستایی zāmātar-، سنسکریت jāmātar-؛ dast = اوستایی zasta-؛ dil = اوستایی zərəd-». پسوند فاعلی -tar ایرانی باستان در فارسی میانه به -d کاهش یافته است؛ صورت پارتی همان zāmād با «ز» است. ادعای نورایی درست است.\",\n  \"sources\": [W + \"داماد\", W + \"Reconstruction:Proto-Iranian/jā́mātā\"],\n  \"ref_check\": [\n    {\"ref\": \"MON:1487\", \"status\": \"supports\",\n     \"note\": \"Mo'in's entry, checked online (abadis.ir/fatofa/داماد, section فرهنگ معین): 'داماد [په.] (اِ.) ۱- مرد تازه زن گرفته. ۲- شوهر دختر یا خواهر' — the tag [په.] is Mo'in's 'Pahlavi', and the first gloss is exactly Nourai's 'bride groom'. The print edition's Latin Pahlavi form dāmāt and the page number 1487 could not be checked (the six-volume Farhang-e Farsi is not online page-by-page; the one-volume OCR on disk, MON_part1.txt line 59278, has the entry but its origin tag is lost in the OCR).\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"PHD\", \"where\": \"MacKenzie p. 25 (PHD.txt leaf 46)\", \"stance\": \"supports\",\n     \"note\": \"'dāmād [dʾmʾt' | M 424, N ~] bridegroom, son-in-law. ~ih: condition of a bridegroom, son-in-law.'\"},\n    {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II (NYB_vol2_glossary.txt)\", \"stance\": \"silent\",\n     \"note\": \"grep for dāmād / dʾmʾt / 'bridegroom' finds only a passing mention of a bridegroom (mērak) in the note at p. ~118; the glossary has no dāmād lemma.\"},\n    {\"src\": \"HRN\", \"where\": \"Horn no. 532, p. 117\", \"stance\": \"supports\", \"note\": \"'phlv. dāmāt' stands in Horn's entry between aw. zāmātar- and the modern dialect forms.\"},\n    {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien §110, p. 220 (HUB.txt leaf 230)\", \"stance\": \"supports\",\n     \"note\": \"'Ap. d (= iran. z) = np. d: 1) dāmād \\\"Schwiegersohn\\\" = zd. zāmātar-, skr. jāmātar-' — the sound law that licenses the d-.\"},\n    {\"src\": \"ARY\", \"where\": \"Aryanpur, Latin index pdf p. 262-263 (ARY_latin_index_pages.txt lines 7588-7590)\", \"stance\": \"supports\",\n     \"note\": \"the index card for داماد lists 'JAMATAR (SANSKRIT) / ZAMATAR (AVESTAN) / GAM, GAMEO- (GREEK) / DAMAD, DAMAT (PAHLAVI) / GENER (LATIN) / ZAWA (KURDISH) / GENDRE (FRENCH) / ZOM, ZOMGALI (AFGHAN)' — an independent modern Persian source giving precisely Nourai's set of cognates.\"}\n  ]\n})\n\nnodes.append({\n  \"id\": 3,\n  \"lang\": \"Persian\",\n  \"words\": \"dâmâd\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"New Persian داماد dāmād 'son-in-law; bridegroom' is the direct continuation of Middle Persian dāmād, unchanged except for the New Persian reading of the final consonant as -d; it is in the language from the beginning of the classical period (Ferdowsi, Shāhnāma, 'do dāmād-e uy'; Rumi, Masnavi V 3720). Both senses of the chart are attested from the start: 'son-in-law' in Ferdowsi, 'bridegroom' in Rumi, and Borhān-e Qāṭeʿ glosses it 'مردی که تازه جشن عروسی وی برپا شود؛ مرد تازه زن گرفته؛ شوهر دختر شخص؛ شوهر خواهر شخص'. The colloquial Tehrani dumād and the dialect form دوماد are secondary raisings of the first ā. Persian is the only Iranian language with d-: all others keep z- (Parthian zāmād, Sogdian zʾmtʾy, Baluchi zāmāt, Kurdish zavā/zawā, Gilaki zāmā, Pashto zum), which is what makes dāmād a diagnostic South-west (Persid) form.\",\n  \"derivation_fa\": \"«داماد» در فارسی نو دنبالهٔ مستقیم فارسی میانهٔ dāmād است و جز خوانش همخوان پایانی تغییری نکرده؛ از آغاز دورهٔ کلاسیک در زبان هست: فردوسی «به میدان شدندی دو دامادِ اوی» (به معنی شوهرِ دختر) و مولوی «از این دامادِ نو» (به معنی نوداماد). هر دو معنای نمودار کهن‌اند و برهان قاطع نیز آن را چنین معنی می‌کند: «مردی که تازه جشن عروسی وی برپا شود، مرد تازه زن گرفته، شوهر دخترِ شخص، شوهر خواهرِ شخص». گونهٔ گفتاری «دوماد/دومادِ» تهرانی افراشتگی ثانوی مصوت نخست است. نکتهٔ مهم آنکه فارسی تنها زبان ایرانی با «د» آغازین است و دیگر زبان‌ها «ز» را نگاه داشته‌اند (پارتی zāmād، سغدی zʾmtʾy، بلوچی zāmāt، کردی زاوا، گیلکی زاما، پشتو زوم)؛ همین ویژگی داماد را نشانهٔ گویش جنوب‌غربی (پارسی) می‌کند. ادعای نورایی درست است.\",\n  \"sources\": [W + \"داماد\", \"https://abadis.ir/fatofa/داماد/\"],\n  \"ref_check\": [\n    {\"ref\": \"BQT:817\", \"status\": \"supports\",\n     \"note\": \"Borhān-e Qāṭeʿ, Moʿin's edition, vol. 2, leaf 277 of BQT_v2_pages.txt (printed ≈ p. 817-820 by the file's stated offset of leaf+543±3; the running head is too damaged in the OCR to read the numeral). Moʿin's etymological footnote: '# داماد ـ پهلوی dāmāt، اوستا zāmātar- (داماد)، هندی‌باستان jāmātar-، کردی zavā، افغانی zūm و ...، بلوچی zāmās و ...، گیلکی zamā، اورامانی ...، دزفولی ...' with the entry text 'مردیکه تازه جشن عروسی وی برپا شود، مرد تازه زن گرفته، شوهر دختر شخص، شوهر خواهر شخص'. That is the chart's Avestan > Pahlavi > Persian chain and both of the chart's glosses.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"HRN\", \"where\": \"Horn no. 532, p. 117\", \"stance\": \"supports\",\n     \"note\": \"'532. dāmād \\\"Schwiegersohn; Bräutigam (Vis und Rāmin S. 46)\\\" ... aw. zāmātar-; phlv. dāmāt; ai. jāmātar-' plus the dialect forms g. zūmād, gel. zamā, Kāš. zūmo.\"},\n    {\"src\": \"HUB\", \"where\": \"Persische Studien §110, p. 220\", \"stance\": \"supports\",\n     \"note\": \"'np. dāmād \\\"Schwiegersohn\\\" = zd. zāmātar-, skr. jāmātar-' heads the list of np. d = av. z.\"},\n    {\"src\": \"MON\", \"where\": \"Farhang-e Farsi s.v. داماد (via abadis.ir)\", \"stance\": \"supports\",\n     \"note\": \"'[په.] (اِ.) ۱- مرد تازه زن گرفته. ۲- شوهر دختر یا خواهر' — Moʿin marks the word Pahlavi.\"},\n    {\"src\": \"ARY\", \"where\": \"Aryanpur, Latin index pdf p. 262-263\", \"stance\": \"supports\",\n     \"note\": \"داماد indexed with ZAMATAR (Avestan), DAMAD/DAMAT (Pahlavi), JAMATAR (Sanskrit), GAM/GAMEO- (Greek), GENER (Latin).\"}\n  ]\n})\n\nnodes.append({\n  \"id\": 4,\n  \"lang\": \"Sanskrit\",\n  \"words\": \"jâmâ\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"Sanskrit jāmā f. is a real word and Monier-Williams glosses it exactly as the chart does, 'a daughter' (Benfey and Böhtlingk-Roth prefer 'daughter-in-law', and Pokorny 369, Walde-Pokorny I 574 and Klein all render it 'Schwiegertochter / daughter-in-law' — the sense wavers because the stem denotes a female relative by marriage or blood generally). It belongs to the same ā-stem *ǵm̥-mo-/*ǵeh₂m- family as jāmi- 'related by blood; sister, daughter-in-law' and vi-jāmi- 'related by marriage', beside the -tar- derivative jāmātṛ- 'son-in-law'. PIE palatal *ǵ > Indo-Iranian *ȷ́ > Sanskrit j, so jāmā is the Indo-Aryan match of the reconstructed Old Iranian *zāma- of node #1. Nourai's gloss 'daughter' and his reference are Mann's: IEC 402 s.v. ĝn̥mos, 'Skt. jāmā daughter'.\",\n  \"derivation_fa\": \"jāmā در سنسکریت واژه‌ای واقعی است و مونیه-ویلیامز دقیقاً همان معنایی را می‌دهد که نمودار آورده: «دختر» (بنفی و بوتلینگ-روت «عروس/زن‌پسر» ترجیح می‌دهند و پوکورنی ص۳۶۹، والده-پوکورنی ج۱ ص۵۷۴ و کلاین نیز آن را Schwiegertochter می‌آورند؛ این نوسان معنایی از آن است که این ستاک به‌طور کلی خویشاوند مؤنث سببی یا نسبی را می‌رساند). این واژه با jāmi- «خویشاوند، خواهر» و vi-jāmi- «خویشِ سببی» هم‌ستاک است و jāmātṛ- «داماد» مشتق -tar- همین ستاک است. کامِ *ǵ هندواروپایی در هندوایرانی *ȷ́ و در سنسکریت «ج» می‌شود، پس jāmā همتای هندوآریایی همان *zāma- ایرانی باستانِ جعبهٔ شمارهٔ ۱ است. معنا و مأخذ نورایی از مان (ص۴۰۲: «Skt. jāmā daughter») گرفته شده است. ادعای نورایی درست است.\",\n  \"sources\": [\"https://www.wisdomlib.org/definition/jama\"],\n  \"ref_check\": [\n    {\"ref\": \"IEC:402\", \"status\": \"supports\",\n     \"note\": \"Mann p. 402 (IEC.txt leaf 234): 'ĝn̥mos, ā \\\"generation, mating\\\" ... Skt. jāmā \\\"daughter\\\"; cf. jāmiḥ \\\"sibling; twin\\\"' — word, language and gloss as in the chart.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"Pokorny 369\", \"stance\": \"partial\",\n     \"note\": \"'ai. jāmi-ḥ \\\"connected, related by blood\\\", fem. \\\"female relatives, esp. daughter-in-law\\\", ved. vi-jāmi-ḥ \\\"relative by marriage\\\", jāmā \\\"daughter-in-law\\\"' — same word, gloss 'daughter-in-law' rather than 'daughter'.\"},\n    {\"src\": \"WLD\", \"where\": \"Bd. I p. 574\", \"stance\": \"partial\", \"note\": \"'jāmā \\\"Schwiegertochter\\\"' — likewise 'daughter-in-law'.\"},\n    {\"src\": \"KLN\", \"where\": \"s.v. bigamy\", \"stance\": \"partial\", \"note\": \"'OI. jāmiḥ, brother, sister, jāmā, daughter-in-law'.\"},\n    {\"src\": \"web (Monier-Williams via wisdomlib)\", \"where\": \"wisdomlib.org/definition/jama\", \"stance\": \"supports\",\n     \"note\": \"'Jāmā (जामा): f. a daughter' (Monier-Williams), with Benfey's 'a daughter-in-law' given as the alternative — Nourai's/Mann's gloss is the MW one.\"}\n  ]\n})\n\nnodes.append({\n  \"id\": 5,\n  \"lang\": \"Greek\",\n  \"words\": \"gamos\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"Ancient Greek γάμος (gámos) m. 'wedding, marriage' is the Greek continuant of the same root: PIE *ǵem- with the o-grade/zero-grade noun formation *ǵm̥-o- (Watkins: 'Suffixed zero-grade form *gmo-o- in Greek gamos'), beside the denominative γαμέω 'to take to wife, marry' and γαμβρός (*gem-ro-) 'son-in-law, brother-in-law', the exact word-equation of Latin gener (< *gemer, remade after genus) and Albanian dhëndër. Attested from Homer on and the ordinary Greek word for a wedding; it is the source of the whole learned -gamy vocabulary. Pokorny 369 and Klein both list γάμος in this root, and Wiktionary derives γάμος 'from Proto-Indo-European *ǵem- (to marry)'.\",\n  \"derivation_fa\": \"γάμος یونانی باستان «عروسی، ازدواج» دنبالهٔ همان ریشه است: از *ǵem- هندواروپایی با ساخت اسمی *ǵm̥-o- (واتکینز: «صورت درجهٔ صفرِ پسونددار *gmo-o- در یونانی gamos»)، در کنار فعل مشتق γαμέω «زن گرفتن» و γαμβρός (< *gem-ro-) «داماد» که برابر دقیق gener لاتینی (< *gemer، به قیاس genus بازساخته) و dhëndër آلبانیایی است. این واژه از هومر به بعد شاهد دارد و واژهٔ معمول یونانی برای عروسی است و سرچشمهٔ همهٔ ترکیب‌های علمی با -gamy. پوکورنی (ص۳۶۹)، کلاین و ویکی‌واژه همگی آن را زیر همین ریشه می‌آورند. ادعای نورایی درست است.\",\n  \"sources\": [W + \"γάμος\", W + \"Reconstruction:Proto-Indo-European/ǵem-\"],\n  \"ref_check\": [\n    {\"ref\": \"AHD\", \"status\": \"supports\",\n     \"note\": \"Watkins/AHD appendix s.v. geme-: 'Suffixed zero-grade form *gmo-o- in Greek gamos, marriage: GAMETE, GAMO-, -GAMOUS, -GAMY; GAMOSEPALOUS. [Pok. gem(e)- 369.]' — Nourai's Greek and English boxes are this entry.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"Pokorny 369\", \"stance\": \"supports\",\n     \"note\": \"'gr. γαμέω \\\"marry\\\" ... γαμέτης \\\"husband\\\", γαμετή \\\"wife\\\", γαμήλιος \\\"nuptial\\\", γάμος m. \\\"wedding\\\"; γαμβρός (*gem-ro-) \\\"son-in-law\\\"'.\"},\n    {\"src\": \"KLN\", \"where\": \"s.v. bigamy / gamete (KLN_1966.txt)\", \"stance\": \"supports\",\n     \"note\": \"'Gk. gamos, wedding, marriage, which is rel. to gamein, to take to wife, to marry ... fr. I.-E. base *gem(e)-, to marry'.\"},\n    {\"src\": \"SYN\", \"where\": \"Buck 2.63\", \"stance\": \"supports\", \"note\": \"'Grk. gambrós ... : gámos \\\"marriage\\\". From the same root also Skt. jāmātar-, Av. zāmātar-.'\"},\n    {\"src\": \"WLD\", \"where\": \"Bd. I p. 574 f.\", \"stance\": \"supports\", \"note\": \"the Greek material (γάμος, γαμβρός) stands in the same article as the Indo-Iranian words, WP I 574 f. (cited by Pokorny).\"}\n  ]\n})\n\nnodes.append({\n  \"id\": 6,\n  \"lang\": \"English\",\n  \"words\": \"-gamy, gamo-, polygamy\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"English -gamy and the combining form gamo- are learned borrowings of Greek -γαμία / γαμο- (from γάμος), taken over through Latin and French in the scientific vocabulary of the 16th-19th centuries: polygamy 1590s < Late Latin polygamia < Late Greek πολυγαμία 'polygamy', from πολύγαμος 'often married' (πολύς 'many' + γάμος); bigamy 13th c. through Old French bigamie from Medieval Latin bigamia; the botanical and biological terms (cryptogam, monogamy, endogamy, exogamy, cleistogamy, dichogamy) are 17th-19th-century coinages on the same element, and gamete was coined in 1878 by Eduard Strasburger from Greek γαμετή 'wife'. Nourai's box is Watkins' own list of English outcomes under geme-.\",\n  \"derivation_fa\": \"پسوند -gamy و جزء ترکیبی gamo- در انگلیسی وام‌واژه‌های عالمانه از یونانی -γαμία و γαμο- (از γάμος) هستند که از راه لاتینی و فرانسه در واژگان علمی سده‌های شانزدهم تا نوزدهم وارد شده‌اند: polygamy در دههٔ ۱۵۹۰ از لاتینی متأخر polygamia و آن از یونانی متأخر πολυγαμία «چندهمسری» (πολύς «بسیار» + γάμος)؛ bigamy از راه فرانسهٔ کهن bigamie؛ و اصطلاحات گیاه‌شناسی و زیست‌شناسی (cryptogam، monogamy، endogamy، exogamy) ساخت‌های نوی سده‌های هفدهم تا نوزدهم بر همین جزءاند؛ gamete را نیز اشتراسبورگر در ۱۸۷۸ از γαμετή «همسر» ساخت. فهرست این جعبه عیناً همان فهرستی است که واتکینز زیر مادهٔ geme- آورده است. ادعای نورایی درست است.\",\n  \"sources\": [\"https://www.etymonline.com/word/polygamy\"],\n  \"ref_check\": [\n    {\"ref\": \"AHD\", \"status\": \"supports\",\n     \"note\": \"Watkins s.v. geme-: '... in Greek gamos, marriage: GAMETE, GAMO-, -GAMOUS, -GAMY; GAMOSEPALOUS' — Nourai's '-gamy, gamo-, polygamy' is a direct transcription of this.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"Klein s.v. bigamy, digamy, endogamy, exogamy, cryptogam, allogamy (KLN_1966.txt)\", \"stance\": \"supports\",\n     \"note\": \"'digamy, n., second marriage — Late L. digamia, fr. Gk. digamia ... See -gamy and cp. monogamy, bigamy, polygamy'; 'allogamy ... compounded of allo- and Gk. -gamia, fr. gamos, marriage. See -gamy.'\"},\n    {\"src\": \"SKT\", \"where\": \"Skeat s.v. polygamy (SKT.txt)\", \"stance\": \"supports\",\n     \"note\": \"'polygamy, marriage with many (Gk.) — Gk. πολυγαμία — Gk. marrying many (see Poly-)'.\"},\n    {\"src\": \"web (Etymonline)\", \"where\": \"etymonline.com/word/polygamy\", \"stance\": \"supports\",\n     \"note\": \"'polygamy (n.) \\\"marriage with more than one spouse,\\\" 1590s, from Late Latin polygamia, from Late Greek polygamia ... from polys \\\"many\\\" + gamos \\\"marriage\\\" (see gamete)'; the gamete entry gives 'PIE root *gem(e)- \\\"to marry\\\" (source also of ... Avestan zama-tar \\\"son-in-law\\\")'.\"}\n  ]\n})\n\nroot_entry[\"nodes\"] = nodes\n\nout = {\n  \"pdf_page\": 170,\n  \"book_page\": 140,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-05\",\n  \"entries\": [root_entry]\n}\n\nwith io.open(\"/home/sfmqrb/git/rishe/data/verification/page-170.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(out, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"ok\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk170.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-170.json >/dev/null && echo JSON_OK && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 170"
}
```


### [2026-09-05T20:51:00.411Z] TOOL RESULT

```
ok
JSON_OK
nodes verified: 6/6
node verdicts: {'plausible': 1, 'confirmed': 5}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 7, 'partial': 1}
books consulted: {'partial': 5, 'supports': 17, 'silent': 1} | by book: {'WLD': 3, 'KLN': 3, 'SYN': 2, 'HRN': 2, 'HUB': 2, 'ARY': 2, 'POK': 2, 'BRT': 1, 'PHD': 1, 'NYB': 1, 'MON': 1, 'web (Monier-Williams via wisdomlib)': 1, 'SKT': 1, 'web (Etymonline)': 1}
```


## [2026-09-05T20:51:13.821Z] TOOL CALL #60: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport json,glob\nidx={}\nfor l in open('data/verification/sources/web/index.jsonl',encoding='utf-8'):\n    try: r=json.loads(l)\n    except: continue\n    idx[r['url']]=r.get('status')\nd=json.load(open('data/verification/page-170.json'))\nurls=set(d['entries'][0].get('sources',[]))\nfor n in d['entries'][0]['nodes']: urls|=set(n.get('sources',[]))\nfor u in sorted(urls): print(idx.get(u,'NOT ARCHIVED'), u)\nEOF"
}
```


### [2026-09-05T20:51:15.781Z] TOOL RESULT

```
200 https://abadis.ir/fatofa/داماد/
NOT ARCHIVED https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ǵem-
200 https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/ȷ́ā́mātā
200 https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/jā́mātā
200 https://en.wiktionary.org/wiki/γάμος
200 https://en.wiktionary.org/wiki/داماد
200 https://www.etymonline.com/word/polygamy
200 https://www.wisdomlib.org/definition/jama
```


## [2026-09-05T20:51:21.198Z] TOOL CALL #61: Bash

```json
{
 "command": "python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ǵem-\" --note \"page 170, root Geme/Gem: PIE root page\" && python3 - <<'EOF'\nimport json\nidx={}\nfor l in open('data/verification/sources/web/index.jsonl',encoding='utf-8'):\n    try: r=json.loads(l)\n    except: continue\n    idx[r['url']]=r.get('status')\nprint(idx.get(\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ǵem-\"))\nEOF\npython3 tools/verify_check.py 170"
}
```


### [2026-09-05T20:51:23.714Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/ca565c62a0003296.txt
200
nodes verified: 6/6
node verdicts: {'plausible': 1, 'confirmed': 5}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 7, 'partial': 1}
books consulted: {'partial': 5, 'supports': 17, 'silent': 1} | by book: {'WLD': 3, 'KLN': 3, 'SYN': 2, 'HRN': 2, 'HUB': 2, 'ARY': 2, 'POK': 2, 'BRT': 1, 'PHD': 1, 'NYB': 1, 'MON': 1, 'web (Monier-Williams via wisdomlib)': 1, 'SKT': 1, 'web (Etymonline)': 1}
```


## [2026-09-05T20:51:41.875Z] AGENT

Page 170 (book p. 140) verified; `verify_check.py 170` reports 0 PROBLEM lines.

**Counts** — 1 entry (2 redirects skipped: Geme-tar → Ter 3, Gen → Gnô). Root: 1 confirmed. Nodes: 6/6 done — 5 confirmed, 1 plausible. Ref checks: 7 supports, 1 partial. 24 `consulted` entries (POK, WLD, AHD, IEC, SYN, KLN, BRT, HRN, HUB, PHD, NYB, MON, ARY, SKT, Etymonline, Monier-Williams).

**Findings**
- Root *Geme, Gem* "to marry" POK:369 is verbatim Pokorny ("Root/lemma: gem(e)- … Meaning: to marry … Page(s) 369-370"); Watkins/AHD `geme-` and Wiktionary *ǵem- agree. Greek gamos, Sanskrit jāmā ("a daughter" in Monier-Williams — exactly Mann IEC 402, Nourai's source), Pahlavi dāmāt (MacKenzie p. 25) and Persian داماد all check out; Moʿin's footnote in Borhān (vol. 2, leaf 277 ≈ printed 817-820) gives Nourai's whole chain word for word.
- No `disputed`, no `transcription_suspect`, **no extraction errors** — I rendered PDF p. 170 and the JSON matches the printed chart exactly (including "zâmâ-tar" and "jâma").
- Only soft spot, node #1 (Avestan), marked `plausible`: **jâma is not an attested Avestan word.** It is the short stem Walde-Pokorny I 574 posits behind zāmātar- ("zugrunde liegt kürzeres *jāma-"), which in Avestan would be *zāma- (Bartholomae AiW 1691 infers it from zāmaoya- "brother of the son-in-law"). Nourai took both the j- spelling and the "Avestan" label straight from Mann IEC 402 ("Av. jāma, n. kinship") — Mann's own slip, faithfully copied. zāmātar- itself is fully confirmed (AiW 1691, Yt 10.116).
- Worth recording for the reader: the d- of dāmād vs Avestan z- is *not* an irregularity but the regular South-west Iranian reflex of Proto-Iranian *ȷ́ — Hübschmann, Persische Studien §110 (p. 220) heads his list of that correspondence with dāmād, alongside dast : zasta-, del : zərəd-, dahān : zafan-.
- MON:1487's page number is unverifiable (the 6-vol Farhang-e Fārsi is not online page-by-page; the local one-volume OCR lost the origin tag), but Moʿin's entry itself was checked via abadis.ir: "داماد [په.] … مرد تازه زن گرفته" — Pahlavi tag and "bridegroom" gloss as claimed.

All eight web pages cited are archived via `fetch_source.py`. The file is written but not committed.
