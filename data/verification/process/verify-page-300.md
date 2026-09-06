# Verification process log — verify-page-300


## [2026-09-06T22:35:56.715Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 300 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-300.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-300.json. Write /home/sfmqrb/git/rishe/data/verification/page-300.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 300` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T22:35:58.332Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T22:35:59.080Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T22:35:59.094Z] TOOL RESULT

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


## [2026-09-06T22:35:59.099Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-300.txt"
}
```


### [2026-09-06T22:35:59.108Z] TOOL RESULT

```
1	=== PDF page 300 (book page 270) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Lâ, Lâiô : roar, bark, bellow  (refs IEC:659; POK:651)
4	#1 (parent #0) [Persian] refs=IEC:659; MON:3549 | lâyîdan «لاییدن» : to express sorrow
5	#2 (parent #0) [Germanic] refs=AHD:1525 | lollen : to lull
6	  #3 (parent #2) [English] refs=AHD | lull
7	#4 (parent #0) [Latin] refs=AHD | lâmentum : expression of sorrow
8	  #5 (parent #4) [English] refs=AHD | lament
9	#6 (parent #0) [Greek] refs=AHD | lalein : to talk ; lalos : talkative
10	  #7 (parent #6) [English] refs=AHD | glossolalia, echolalia
11	--- entry 1 ---
12	ROOT [Akkadian] Ladunu : resin of a certain tree  (refs AHD:730)
13	#1 (parent #0) [Arabic] refs=None | 
14	  #2 (parent #1) [Persian] refs=KLN:855; MON:3523 | lâdan «لادن» : lotus, its good smell
15	    #3 (parent #2) [Greek] refs=BQT:1876; SKT:1286 | lâdon, lôtos
16	      #4 (parent #3) [Latin] refs=AHD:771 | lôtus
17	        #5 (parent #4) [English] refs=None | lotus
18	--- entry 2 ---
19	ROOT Lâiô -> redirect to Lâ
20	
```


## [2026-09-06T22:36:02.105Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-300.json",
 "description": "Read source JSON page 300"
}
```


### [2026-09-06T22:36:02.139Z] TOOL RESULT

```
{
  "pdf_page": 300,
  "book_page": 270,
  "entries": [
    {
      "root": {
        "name": "Lâ, Lâiô",
        "lang": "Indo-European",
        "refs": "IEC:659; POK:651",
        "gloss": "roar, bark, bellow"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "IEC:659; MON:3549",
          "words": [
            {"translit": "lâyîdan", "gloss": "to express sorrow", "script": "لاییدن"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "ملامتم مکنید ار دراز میلایم - بود که کشف شود حال بنده پیش شما",
            "poet": "Molavî"
          }
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD:1525",
          "words": [
            {"translit": "lollen", "gloss": "to lull", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "lull", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "lâmentum", "gloss": "expression of sorrow", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "lament", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD",
          "words": [
            {"translit": "lalein", "gloss": "to talk", "script": null},
            {"translit": "lalos", "gloss": "talkative", "script": null}
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
            {"translit": "glossolalia, echolalia", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Ladunu",
        "lang": "Akkadian",
        "refs": "AHD:730",
        "gloss": "resin of a certain tree"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Arabic",
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "KLN:855; MON:3523",
          "words": [
            {"translit": "lâdan", "gloss": "lotus, its good smell", "script": "لادن"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "نریزد از درخت ارس کافور - نخیزد از میان لاد لادن",
            "poet": "Manŭchehrî"
          }
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Greek",
          "refs": "BQT:1876; SKT:1286",
          "words": [
            {"translit": "lâdon, lôtos", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Latin",
          "refs": "AHD:771",
          "words": [
            {"translit": "lôtus", "gloss": null, "script": null}
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
            {"translit": "lotus", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Lâiô",
        "redirect": "Lâ"
      },
      "nodes": []
    }
  ]
}
```


## [2026-09-06T22:36:02.804Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-06T22:36:02.843Z] TOOL RESULT

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


## [2026-09-06T22:36:12.487Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json;d=json.load(open('refs_online.json'))\nfor k in ['IEC','POK','AHD','MON','KLN','BQT','SKT']:\n    print(k, json.dumps(d.get(k),ensure_ascii=False)[:800]);print()\n\""
}
```


## [2026-09-06T22:36:12.901Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"lā-\" AHD_watkins1985.txt | head -40"
}
```


### [2026-09-06T22:36:14.320Z] TOOL RESULT

```
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IE

POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<lea

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifier": "watkins-american-heritage-dictionary-of-indo-european-roots-1985", "local_file": "/home/sfmqrb/

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 74

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/82307409

SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Headword in caps at line start, e.g. grep -n '^TREE' SKT.t
```


### [2026-09-06T22:36:14.375Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T22:36:18.453Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"lament\" AHD_watkins1985.txt | head -20; echo ---; grep -n -i \"glossolalia\\|echolalia\" AHD_watkins1985.txt | head; echo ---; grep -n -i \"lallen\\|lallare\\|lull\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-06T22:36:18.516Z] TOOL RESULT

```
379:zero-grade form *dhra-gh- in: a. Greek tarassein (Attic tarattein), to confuse, disturb: ATARACTIC; b. Greek trakhus, rough: TRACHEA, TRACHOMA, TRACHYTE. [Pok. 1. dher- 251.] dher-2, To hold firmly, support. 1. Suffixed form *dher-mo- in Latin firmus, firm, strong: FARM, FERMATA, FIRM, FIRMAMENT; AFFIRM, CONFIRM, INFIRM, (INFIR- MARY). 2. Extended form *dhergh- possibly in Latin fortis, strong (but this is also possibly from bhergh-?). 3. Suffixed zero-grade form *dhr-ono- in Greek thronos, seat, throne (< “support”): THRONE. 4. Suffixed form *dher-mn in Sanskrit dharma, statute, law (< “that which is established firmly”): DHARMA. 5. Old Persian dar-, to hold (whence Persian -ddr, ‘“-holder’’): SIRDAR, TAHSILDAR, ZAMINDAR. [Pok. 2. dher- 252.] dher-3, To drone, murmur, buzz. Extended zero-grade form *dhrén- in: a. Germanic *drén- in Old English dran, drén, male honeybee: DRONE}; b. Greek thrénos, dirge, lament: THRENODY. [Pok. 3. dher- 255.] dhers-. To venture, be bold. 1. O-grade form *dhors- and zero-grade form *dhrs- respectively in Germanic *ders- and *durs- in Old English dearr and durst, first and third person singular present and past indicative of durran, to venture: DARE, (DURST). 2. Possibly Latin -festus in: a. infestus, hostile (? < “directed against”; in-, into, against; see en): INFEST; b. manifestus, palpable, evident (< “caught red-handed, grasped by the hand”; manus, hand; see man-2): MANIFEST. [Pok. dhers- 259.] dhés-. Root of words in religious concepts. Possibly an extension of dhé-'. 1. Suffixed form *dhés-yd in Latin fériae (Old Latin fésiae), holidays: FAIR?, FERIA. 2. Suf- fixed form *dhés-to- in Latin féstus, festive (> German Fest, festival): FEAST, (-FEST), (FESTAL), FESTIVAL, FES- TIVE, FESTOON, (FETE), FIESTA; (GABFEST), OKTOBER- FEST. 3. Suffixed zero-grade form *dhas-no- in Latin fanum, temple: FANATIC; PROFANE. 4. Possibly suffixed zero-grade form *dhas-o- becoming *dhes-o- in Greek theos (< *thes-os), god: THEO-; APOTHEOSIS, ATHEISM, ENTHUSIASM, PANTHEON, POLYTHEISM. [Pok. dhés- 259.] dheu-'. Also dheue-. The base of a wide variety of derivatives meaning “to rise in a cloud,” as dust, vapor, or smoke, and related to semantic notions of breath, various color adjectives, and forms denoting defective perception or wits. 1. Suffixed extended zero-grade form *dhii-mo- (<*dhua-mo-), smoke, in: a. Latin fimus, smoke: FUMAROLE, FUMATORIUM, FUMATORY, FUME; FUMARIC ACID, FUMIGATE, FUMITORY, PERFUME; b. Greek thumos, soul, spirit: -THYMIA; ENTHYMEME; c. Greek thumon, thumos, thyme (< “plant having a strong smell”): THYME. 2. Suffixed lengthened zero-grade form *dhi-li- in Latin filigd, soot: FULIGINOUS. 3. Ex- tended form *dheus- possibly in Germanic *dus- in: a. Old English dysig, foolish (< “stupefied,” “confused”): pD1zzy; b. Danish dase, to make drowsy, akin to the probable Scandinavian source of DOZE. 4. Suffixed ex- tended form *dheus-o- in Germanic *deuzam, breathing creature, animal, in: a. Old English déor, animal: DEER; b. Old Norse dyr, animal, deer: REINDEER. 5. Suffixed o-grade form *dhous-o in Slavic *dukh- in Russian dukh, breath, spirit: DUKHOBoR. 6. Variant extended form *dhwes- in nasalized form *dhwens- in Germanic *duns-, dust, meal, in: a. Germanic suffixed form *duns-to- in Old English dist, dust: pustT; b. Old Norse diinn, bird’s down (< “fine like dust”): DOWN?, DUVETYN; (EIDER- Down). 7. Extended zero-grade form *dhus- in Greek thuos, burnt sacrifice, incense (> Latin thus, incense), and ¢huia, cedar: THUJA, THURIBLE; (THURIFER). 8. Suf- fixed extended zero-grade form *dhus-ko- in: a. Ger- manic duskaz in Old English dox, twilight: Dusk; b. Latin fuscus, dark, dusky: OBFUSCATE. 9. Suffixed extended zero-grade form *dhus-no- in Welsh dwn, dull brown color, whence Old English dun(n), dark-brown: DUN2, 10. Zero-grade extended form *dhubh- in Greek tuphein (< *thuphein), to make smoke, and tuphios,
479:gar-. To call, cry. Expressive root. 1. Germanic *kar6, lament, hence grief, care, in: a. Old English cearu, care: CARE; b. adjective *karagaz, sorrowful, in Old English cearig, sorrowful: CHARY. 2. Celtic suffixed form *gar-(s)mn in Gaelic gairm, shout, cry, call: SLOGAN. 3. Suffixed form (with expressive gemination) *garr-iyo- in Latin garrire, to chatter: GARRULOUS. [Pok. gar- 352.]
548:gvhi-. Thread, tendon. Suffixed form *gwhi-slo- in Latin filum, thread: FILAMENT, FILAR, FILARIA, FILE!, FILLET,
590:kau-'. To howl (imitative). 1. Reduplicated suffixed form *ka-kau-ro- in Sanskrit cakorah, partridge: CHUKAR. 2. Reduplicated form *k6-kii-o- in Greek kdkuein, to wail, lament: Cocytus. [Pok. kau- 535.]
658:la-. Echoic root. 1. Middle Dutch Jollen, to mutter, akin to the Low German source of Middle English Jlollen, to loll: LOLL. 2. Middle Low German lollen, to lull, akin to the Low German source of Middle English Jud/en, to lull: LULL. 3. Old Norse lémr, loon: LOON}. 4. Latin lamen- tum, expression of sorrow: LAMENT. 5. Greek /alos, talk- ative: ECHOLALIA. 6. Greek Jalein, to talk: GLOSSOLALIA. [Pok. 1. la- 650.]
859:plak-2. To strike. 1. Nasalized variant forms *pla-n-k-, *pla-n-g- in: a. Germanic *flang- in Old Norse flengja, to flog, whip, akin to the Scandinavian source of Middle English flingen, to fling: FLING; b. Latin plangere, to strike (one’s own breast), lament: PLAINT, PLANGENT; COMPLAIN. C. suffixed form *plang-yo- in Greek plazein, to drive away, turn aside: PLANKTON. 2. Variant form *plag- in Latin plaga, a blow, stroke: PLAGUE. 3. Suf- fixed form *pldk-yo- in Greek pléssein, to beat, strike: PLECTRUM, -PLEGIA, PLEXOR; APOPLEXY, CATAPLEXY, PARAPLEGIA. [Pok. 2. pldk- 832.]
1118:wai. Alas (interjection). 1. Germanic *wai in Old English wd, wei, woe (interjection), alas: WOE; WELLAWAY. 2. Germanic *waiwalén in Old Norse vdla, véla, *veila, to lament, akin to the Scandinavian source of Middle English wailen, to wail: wat. [Pok. uai- 1110.]
1509:FicHu dhig¥- FICKLE pelg-2 FICTILE dheigh- FicTION dheigh- -FID_ bheid- FIDELITY bheidh- FIDUCIAL  bheidh- FIDUCIARY bheidh- FIELD pele-2 FIELDFARE wer-4 FIEND pé@(i)- FIERCE ghwer- Fiesta dhés- FIFE pipp- FIFTEEN penkWe FIFTH penkwe FIGHT pek-2 FIGMENT dheigh- FIGURE dheigh- FILAMENT gWhi- FILAR gWhi- FILARIA gWhi- FILE! gWhi- FILE? peig-1 FILES pu-2 FILIAL dh@(i)- FILIATE dhé(i)- FILIBUSTER pri- FILIFORM gWhi- FILIGREE gre-no-, g¥hi- FILL pele-1 FILLET gWhi- FILLY pau-
1728:LAMELLA | stele- LAMELLICORN ker-1 LAMENT [a-
---
658:la-. Echoic root. 1. Middle Dutch Jollen, to mutter, akin to the Low German source of Middle English Jlollen, to loll: LOLL. 2. Middle Low German lollen, to lull, akin to the Low German source of Middle English Jud/en, to lull: LULL. 3. Old Norse lémr, loon: LOON}. 4. Latin lamen- tum, expression of sorrow: LAMENT. 5. Greek /alos, talk- ative: ECHOLALIA. 6. Greek Jalein, to talk: GLOSSOLALIA. [Pok. 1. la- 650.]
1441:EsLis gWela-1 EBULLIENCE beu-! ECBOLIC gWele-1 ECCENTRIC kent- ECCHYMOSIS gheu- ECCLESIA kela-2 ECCRINE krei- ECEsIsS weik-1 ECHARD segh- ECHELON skand- ECHIDNA ang¥hi- ECHINO- ang¥hi- ECHINUS angVhi- ECHO (s)wagh- ECHOLALIA 1a- ECLAIR kelo-2 ECLAIRISSEMENT kelo-2 ECLAMPSIA [ap- ECLECTIC leg-! ECLIPSE leikw- ECLOSION kleu-3 ECOLOGY weik-1 ECONOMY weik-1 ECRU kreue-1 ECSTASY sta- ECTO- eghs ECTOSARC twerk- ECU skei- ECUMENICAL welk-1 ECZEMA yes- EDACIOUS ed- EDAPHIC sed-! EDDY eti EDELWEISS _athal-, kweit- EDEMA oid- EDENTATE dent- EDGE ak-
1561:GIVE ghabh- GLABELLA gladh- GLABROUS gladh- GLACE gel-3 GLACIAL gel-3 GLACIATE gel-3 GLACIER gel-3 GLACIS § gel-3 GLAD ghel-2 GLADIATE kel-1 GLADIATOR kel-1 GLAIR kele-2 GLAIVE kel-1 GLANCE? ghel-2 GLAND gWele-2 GLANDERS gWele-2 GLANDULAR gWel@-2 GLANS gWela-2 GLARE! ghel-2 GLAss ghel-2 GLAZE ghel-2 GLEAM ghel-2 GLEBE gel-1 GLEDE ghel-2 GLEE ghel-2 GLEED ghel-2 GLEET gel-! GLEG ghel-2 GLEY gel-! GLIADIN  gel-1 GLIB_ ghel-2 GLIDE ghel-2 GLIMMER ghel-2 GLIMPSE ghel-2 GLINT ghel-2 GLISSADE ghel-2 GLISTEN ghel-2 GLISTER ghel-2 GLITCH ghel-2 GLITTER ghel-2 GLOAMING ghel-2 GLOAT ghel-2 GLOBE gel-1 GLOBULE gel-1 GLOCHIDIUM glégh- GLOMERATE §el-1 GLOMERULE gel-1 GLoss! ghel-2 Gloss? glégh- GLOSSARY gldgh- GLOSSOLALIA glégh-, la- GLOTTIs glégh- GLOVE lep-2 GLOW ghel-2
---
658:la-. Echoic root. 1. Middle Dutch Jollen, to mutter, akin to the Low German source of Middle English Jlollen, to loll: LOLL. 2. Middle Low German lollen, to lull, akin to the Low German source of Middle English Jud/en, to lull: LULL. 3. Old Norse lémr, loon: LOON}. 4. Latin lamen- tum, expression of sorrow: LAMENT. 5. Greek /alos, talk- ative: ECHOLALIA. 6. Greek Jalein, to talk: GLOSSOLALIA. [Pok. 1. la- 650.]
1770:LUES leu-! LUFF lep-2 LUGUBRIOUS leug-2 LULL a=
```


## [2026-09-06T22:36:19.382Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^lā-\\|^la-\\|lā-.*schallnach\\|lallen\" POK_full.txt | head -30"
}
```


### [2026-09-06T22:36:19.434Z] TOOL RESULT

```
53927:Modern High German lallen^ babble '; Lithuanian laluotr babble ', russ. lala^ babbler ', 
76530:la-ll). Old English screadian^ peel, abscise ', *scread(e)i. "piece Zeug', skrudu. "dress' =
```


## [2026-09-06T22:36:24.188Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '53900,53960p' POK_full.txt"
}
```


### [2026-09-06T22:36:24.236Z] TOOL RESULT

```
gr. Anpoc; m. 'gossip, prank, trash, trumpery, of what is showy but useless, delirium ' 
(contains la- or le-), Aripsu) ' to be foolish or silly, speak or act foolishly, of a sick person, to 
be delirious '; unclear is the vocalism (onomatopoeic?) in Aapoq ' seagull' (compare 
Armenian /o/"' quail '); 

alb. /e/7'bark'; 

Latin lamentum^ lamentation ', /a/77e/7/5/7 "lament', latro, -are'bark, bay'; perhaps Oscan 
/amat/r' should be cursed '; 

Old Irish ITid {* leieti) ' accuse '; cymr. edliw{*ate-ITu-) 'rebuke'; 

Gothic lafloun^ be blasphemed ' (present *laian, Indo Germanic *le-)\ Old Norse /of., ' 
curlew, long-billed wading bird ', PI. lor, lomr^ sea diver, loud crying bird', compare isl. 
/o/77i//'' clamor, lamentation '; 



Lithuanian loju, /d//"bark, bay', Latvian laju, /a/'bark, bay, curse ', ladet^ curse '; ladet^ 
curse '; 

Old Church Slavic lajg, /ajat/'bark, bay, inveigh' etc. {/ajat/lor 7a// after the preterite 
stem, compare Lithuanian /djo). 

Reduplicated /a/(/Ja-: 0\d Indie lalalla^ babble '; gr. AaAoc; " gabby, gossipy, loquacious, 
garrulous, blithering ', AaAia 'gossip', KaKtud "babble', AaAayn ' prattle'; Latin lallo, -are^ to 
sing lalla ', lallus' a singing lalla or lullaby ' (compare PN Lalla, Lallia, Lallo, Lollia); 
Modern High German lallen^ babble '; Lithuanian laluotr babble ', russ. lala^ babbler ', 
etc. 

Maybe alb. laluc, lale^ people from the south (pejorative)' a Slavic loanword. 

Note: 

Lycian language < Carian lukk- " (a Leieg) *babbler ' : Luwian lulahf- " (a Leieg) *babbler ' 
< gr. AaAayn " light murmuring '. 

similar lei-, lul-^ lull, rock to sleep, swing' in: 

Old Indie lolatr moves to and fro ', lullta- "fluttering', lalatr walks daintily, plays, shows', 
lelayati^ sways, swings '; Latin lollum^ darnel, cockle, tares, dizziness exciting plant '; 

Maybe alb. lule^ flower, narcotic plant ', {*luludi) lulezoj^ blossom ' : Greek AouAou5i : 
Griko Salentino luludi^ flower '. 

Middle Low German lollen. Modern High German lullen, Lithuanian lelluou, lelluotr\u\\, 
craddle, swing', Latvian leluoju, leluot^\\j\\, cradle children'; in addition Lithuanian lells, lelys 
m. ' night raven, pitch black '; Latvian lells 6s. and " clumsy person'; serb. lelJaflluW, swing, 
cradle, dangle', Ijuljatr lull, swing, cradle ', russ. Ijulju^ little poplar = (traditional in 
lullabies) ', /e^a'aunt', etc.; in addition russ. lelek, poln. Czech lelek^ night raven, pitch 
black ' (see above Lithuanian lells). 

Maybe alb. lejlek^ stork ' < Turkish leylek' stork '. 

Perhaps here with Ar-extension: 

gr. AaoKU) (*AaK-aKU)), Aor. eAokov, Perf. AsAriKa, Doric AeAokq ' speak loudly, cry', 
Ar|K£U) Doric Aqk-) ds., AaK£p6(; Hes. ' gabby, gossipy, loquacious, garrulous, blithering ';
```


## [2026-09-06T22:36:25.107Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"lamentum\\|lämentum\\|lamen-\" POK_full.txt | head -20; echo \"=== IEC ===\"; grep -n \"^lā\\|^la-\\|lāiō\\|laio\" IEC.txt | head -30"
}
```


### [2026-09-06T22:36:25.181Z] TOOL RESULT

```
53907:Latin lamentum^ lamentation ', /a/77e/7/5/7 "lament', latro, -are'bark, bay'; perhaps Oscan 
=== IEC ===
1346:bhlaio “blow; blossom'. Cf. bhleio, bhlo-. Lat. flo, flare ‘blow; cast (metal); W cf. blaw, m. “flow, gush'; OE blowan “blow; blossom' beside blàwan Chlow See bhleio): MHG blüejen, blüewen, blüen ‘blossom’; bluo, blüe, s. id. (Cf. also (?) OE blóma “lump of cast metal"). The OE is ambig. cf. bhlo-
1370:bhlëið (2) “blow, inflate’. Cf. bhlaio. WP II,
2361:dol- (dolaio, -eið) ‘devise, shape, contrive’. Cf. dolos (1) Gk. cf. denom. dolóð ‘fake, trap’; Lat. dolō, āre ‘shape, trim’; Sw. tälja, id.; OCS cf. dly, gs dlüve ‘pickaxe’; dato ‘chisel’
2590:dundulo, io (dundulaio, dundino) ‘sway, rock; dangle, dandle, dally' Arm. tntnam ‘dandle, rock’; LLat. *dundu- lare, It. dondolare ‘dangle; twaddle; trifle, dally’; LG tünteln ‘dally’; sik — ‘swagger’; cf. Tunte *good-for-nothing'; G Zunze ‘slut’; Pol. cf. dyndac ‘dangle, bob’ (*-ü-)
4595:pl. ‘gobbling of a turkey’; Lith. gañdras ‘stork; Latv. gandrs, id. Cf. ghandh- and ghanser ghangh- ‘roar, how? Arm. gangad, a-st. ‘lament’; gangiwn ‘echo, rumble’, cf. also ganfiwn (*scream', fr. *ghan- ghtion); Gk. kagkházo ‘guffaw’; Icel. gagga ‘yelp’: Blg. cf. gágra ‘chatter’. (For OCS gognati ‘murmur’, see gang- (gong-). See next ghanghlaio ‘yell, bawl’. Cf. ghangh- Gk. kagkhaláo ‘guffaw’; Cz. huhlat ‘how? ghanser ‘gander. WP I, 536. Cf. ghandh-, etc. and next Lat. *hanser; anser, id.; MHG ganser; Cz. houser; Pol. gasior, id. ghansis (variant: £hansis) ‘goose’. WP I, 536 Skt. hamsih ‘kind of goose’; hamsáb ‘gander of some king’; Hindi hans 'goose'; Per. yàz, id.; Gk. khén, m.f. ‘goose; gander’; Olr. géiss, Ir. géis, gein ‘swan’; OHG gans, gp. ganso ‘goose’; LG gaus, pl. gáus; OE gos, pl. gës; Fris. goes, pl. gies; Du. gans; ON gás, pl. gæss, id. beside gassi ‘gander’; OCS gosi, pl. gosi; Li. (variant) žąsis; Latv. zoss, gs. zoss, gp. zosu, id.; Finn. LW hanhi, id. gharbhos, à ‘tuft, bundle, sheaf. Gk. kárphos, kárphē “hay, straw; bird?s nest’; OHG garba ‘sheaf’; Du. garf, garve, id.; LW in LLat. garba, Fr. gerbe; Li. cf. garbana *lock, curl’ ghargh- ‘shout, croak’. See next and cf. garg-, gorg-, gargh-. (Skt. ambig.) Skt. garhami, garhe ‘complain’; Arm. garga- tem ‘rave, twaddle’; Icel. garga, a-st. ‘croak, screech’; Li. (ambig.) gargu, eti and gargiu, - tí *cackle, gargle, snore', etc. See garg-, gorg- ghargholos 'gurgling; gurgle; hoarse speaker, gurgle’ etc. Cf. gargar- Skt. ghargharah, adj. ‘gurgling’, etc.); Gk. cf. karkhaléos ‘raucous’; MHG gargeln, v. ‘gargle, gurgle’; Li. (ambig.) gargalas ‘hoarse person’. See next gharghoros (ghorghoros) (1) 'gargling, gurgl- ing’, etc. Cf. ghargholos Skt. cf. ghargharah (ambig. cf. gharghol-); Gk. kárkharos (1) ‘raucous’ beside e-gde kérkho, v. "be hoarse’ (cf. ghergho); Li. cf. ambig. gařgas ‘gurgle; hoarseness’. Cf. garg-, ghergh- gharghoros (ghoerghoros) (2) (rough, sharp,
6665:kal- (3) (kalaio, kaleio) “call, name, summon, invite, accuse'. Skt. cf. usa-kalah ‘cockerel’; Hitt. cf. kalles- “invite, entice’; Gk. kaléo; Alb. kall ‘slander’; OLat. caló, are ‘call’, cf. concilium ‘council; Mir cf. cailech, mod. coileach ‘cockerel’ be- side Ir. caileachas (‘cocksfoot’, bot.); W cei- liog ‘cockerel’; OHG halon, v. ‘call, invite’; MHG haln, id.; Li. cf. kal-bà ‘speech’, kaltas, adj. ‘accused’; kaltis, ies, f. ‘accusation’; cf. also kalenti ‘gabble, as cranes’
8529:chinno, àre (metath. vocalism in Fr. chicaner fr. *cichannare), id.; OCS xoxotati, id.; OHG cf. (unshifted initial in) kachazzen, kichazzen khokhl- (1) (khokhlaio, khokhleuo) ‘gurgle, bubble, boil. Onomat. Gk. kokhlázo, id.; OCS xoxlujo, -ovati, id. See next khokhl- (2) “turbine, spool, whirring object, whirlwind'. Same as (1) ? Gk. kokhlías, m. “reel, spiral; OCS xoxiülü, xoxolü *whirlwind'
9370:la- (intensive px?) Gk. cf. là-makhos ‘very warlike’; la-katarátos ‘much reviled', etc.; OCS cf. la-godínü Ces, cellent’. See ghadh-); la-goditi, v. ‘suit; adore; be addicted to”; OPol. Lagoda OCz. lahoda, Cz. id. ‘titbit’; OCz. lahódka ‘drug’
9411:lādh- (?) “lying, lurking, resting’. Ambig. cf. lendh- Gk. lóthð (Dor. -à-) ‘lurk’; lethe, f., léthos, n. ‘forgetting’; cf. also a-l&thés (lit. 'unhidden', hence “evident, true’); MHG cf. (?) lette, wm (soil, loam’, fr. *ladhjo?) and Swiss lóter (flat, of wine”, fr. *ladhrio-?)
9421:lāg- (2) ? (leg-? legh-?) Per. ray ‘meadow, slope’; ON lækt, pl. lækir, m. ‘brook’; Alb. (ambig.) log, m. ‘green, grass plot’ (but Mod. Gk. lóggos ‘thicket, wood? is said to be fr. Slav. *logü as in Cz. luh “low- land meadow’. A variant of type *lag- may arise in Srb. laz, m. ‘field’; Slovak laz *upland', Cz. iaz ‘meadow’)
9436:láiskð (lasK-) (variant of laio, q.v.) Hitt. sar-lesk- ‘cry up, praise’; Alb. leh, lef ‘bark’; Gk. lásko, v. ‘howl, bay’
9501:lasKo (form of laio, w. extn. in -sK-) “bark? Gk. lasko; Alb. leh, lef, id.
9783:louonos, à (2) ‘cut, cutting; cutter’. Cf. leuis (2). Skt. lavanah, à, m. f. ‘cutter, reaper’; Gk. laion, n. (“ploughshare”, fr. *ləuiom)
10771:migh- ‘fog, drizzle, cloud”. Cf. mighla, migh- laio. WP II, 247 Skt. cf. mihirah (2) ‘cloud’; mih, f. ‘mist’; Per. miy ‘cloud’; Kurd mig ‘mist’; Oss. mig, Dig. megàå ‘cloud, fog, vapour; (prob. LW in) Arm. meg, gs migi, ab. s. migav, id.; Cz. cf.
10775:mighlaio, eio ‘be cloudy, be misty, drizzle’. Cf. migh-, mighlà Gk. cf. omikhlóo, id.; Alb. mjegulloj, id.; Fris. miggelje, v. ‘drizzle’; Cz. dial. mlžit, inf. *cloud over'; Li. miglóti, inf. id.; Latv. miglot, v. (sic!), id. (For Arm. mglim “get mouldy’ see mughlio)
12916:pipolos, à, us (pipl-) ‘flimsy, flighty, airy; flimsy object, fluff, tuft, fly, insect’. Cf. pipà. WP II, 107, and see piplaio, popil- Skt. pipluh, m. ‘mole, birthmark, freckle’; pipilih, f. ‘ant’; Hes. pípulos (a plant associated w. korudallós, -é); OS cf. fifol-daro "butter, fly; OE fifal-de, f. id. (see FK: Falter for other Gmc. forms); ON DI m. Dia f. *scat- terbrain'; fifili, m. ‘dandelion’; Cz. piple, pip- lice, n. f. ‘midge’ beside pipla, f. “kind of bor- age’; OPr. pipalins, acc. pl. m. ‘birds’. See next
19325:tuntoló (tuntuló, tuntlo) (2) ‘rumble, babble’. (Gk. Aib. type: tuntulaio) Gk. tuntlázo, v. ‘babble’; Alb. tunduliloj, v. ‘shake, rattle, dash’. Nominal types: Per. am- big. tundar ‘thunder’. Cf. Gk. túntlos, m. ‘twaddle’
19948:uelaio “fly, dash? Gk. eláo, v. “drive, ride, sail; Lat. volo, are, v. ‘fly’; (Gk. elelízo, v. (2), tr. “twist, whirl, shake, rally may represent a type *ueluel-)
20454:ulaio (ulàio) ‘surge, seethe’. Cf. ulm- and uln- (2). WP I, 303 Skt. cf. (?) vrà, f. “host, troop’; Alb. vloj (1) and valoj, v. ‘boil, ferment, seethe’; OCS vlajo, vlajati, v. ‘surge, billow’; Cz. vlaju, vlát, v. (wave, intr); Late vilàju, at, v. ((1) “roll about, intr.); (variant extension in) Go. wu- lan, v. ‘seethe, rage’; OE wyllan, v. (“boil', intr. beside wylian & wylwan, v. ‘roll’. Cf. ulu- with extns.
20476:(ule-, cf. uelaio. Zero-gde perh. in Gk. aleé, f. “flight, avoidance’; Fr. vol, It. volo, m. ‘flight’)
```


## [2026-09-06T22:36:31.211Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^lāiō\\|^laio\\|lāiō\" IEC.txt | head -20; echo \"=== ctx 9420-9445 ===\"; sed -n '9425,9445p' IEC.txt"
}
```


### [2026-09-06T22:36:31.274Z] TOOL RESULT

```
=== ctx 9420-9445 ===
laiuos ‘awry, left-handed, crooked; lefthand' WP II, 378 Gk. laiós “left-hand; sinister’; Lat. laevus, id.; Ir. laobh ‘crooked’; OCS. and com. SI. lévü ‘left-hand’
laið ‘roar, bellow, bark’. WP II, 377 Skt. rāyāmi, id.; Per. lāyam, id.; Oss. räin, räjun (w. short vowel: ‘bellow’); Arm. lam ‘weep’; Hitt. cf. sar-làmi ‘cry up, praise’; Lat. cf. la-mentum ‘weeping’; Hes. láe, 3s. (short vowel: *'resounds"); OIr. láaim, v. ‘utter’; Go.
lag- — laksos, us
10
20
25
30
35
40
660
laian (short vowel: *scorn?); ON lá, v. “blame”; MHG lüejen ‘bark’; OCS lajo, ati, id. and com. Sl.; Li. loju, loti, id. Nominal forms: R laj, Blg. laj ‘barking, scolding’; Ukr. taja, id.; Cz. láje, f. ‘mob, pack’; Li. lojà “abuse”
láiskð (lasK-) (variant of laio, q.v.) Hitt. sar-lesk- ‘cry up, praise’; Alb. leh, lef ‘bark’; Gk. lásko, v. ‘howl, bay’
lak- (1) ‘têar, rag’. Cf. lakt- (1) Gk. lakís, f. ‘rag, rip, têar’; Lat. cf. lacer, adj. ‘tearing, torn, ragged’; cf. lacinia (2) ‘rag’; Li. laka f. (?) “hole, opening’; cf. lakatas ‘rag’; lakišiai, pl. (a pricky planť; Latv. cf. lakats *kerchief, shawl
lak- (2) ‘kick’. Cf. lakt- (2) Gk. cf. láx (^with the heel". Ambig. cf. lag-); laktízo ‘kick’; Per. cf. lakd, s. ‘kick’; Lat. cf. lacertus “lizard?
lak- (3) “lap up, gulp, gobble’. WP II, 380 Arm. lakem, id.; lak ‘porridge, pap’; W (long- gde) llawg, f. ‘gulp’; OCS loco, lokati ‘lap’; R inf. lokàt, id.; Cz. lokat, id.; lok, m. ‘gulp’; Li. laku, làkti “lap up’; Latv. loku, lakt, id. (pres. tense fr. *lank-); laka ‘swill, mash’. (The composition of Gk. ko-lax, gs -lakos ‘flatterer’ is uncertain)
lak- (4) ‘shout, bawl, abuse’ Gk. aor. élakon, fut. lakēsomai ‘bark, shout, din’; OHG, OS lahan “abuse, scold’; OE lean, p.t. loh, log ‘blame’; cf. OE leahtor, m. ‘vice, evil’; Du. lachter, id. (beside OHG lastar, n. cf. also prob. Gk. lásthé ‘mockery, insult. Cf. also ON lostr “evil, wrong, harm")
lak- (or laK-? Cf. lako. Gk. ambig.) Gk. lēkéō ^womanize'; lëkó, gs lekoüs *phal- lus’; Skt. cf. raka ‘goddess of fertility’. (Doric: -à-)
laks- (?) jump; lumping horse’ It. lacca “leg, haunch’; cf. Lat. lacertus ‘fore- arm; leg-muscle; lizard, newt? (?); Sw. lägg, m. pl. -ar ‘calf, thigh-bone'; Ukr. cf. loSak, m. ‘colt, foal; loša ‘filly’; Latv. cf. lakstu, -it Sump’.
làks- (?) variant of lásik-, q. v. W cf. Iochi, 3s. fut. llawch ‘fondle, cherish’
laksos, us ‘loose, slack, limp, flabby’. WP IL, 712 Lat. laxus “loose; wide; open’; W Hac limp! m.
661
```


## [2026-09-06T22:36:32.632Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=53880 && NR<=53935' POK_full.txt | grep -n \"\" | head -5; echo \"=== page markers near ===\"; grep -n \"650\\|651\" POK_full.txt | awk -F: '$1>53700 && $1<54100' | head"
}
```


### [2026-09-06T22:36:34.279Z] TOOL RESULT

```
1:
2:References: WP. II 381, WH. I 757 f., different O'Rahilly Eriu 13, 152. 
3:
4:Page(s): 652 
5:
=== page markers near ===
53967:Page(s): 650-651 
54004:Page(s): 651
```


## [2026-09-06T22:36:49.483Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt BQT_v1.txt BQT_v2.txt incoming/BQT/BQT_v3_pages.txt incoming/BQT/BQT_v4_pages.txt incoming/BQT/BQT_v5_pages.txt; do echo \"--- $f\"; grep -n \"لاییدن\\|لائیدن\\|لاييدن\\|میلایم\\|لایید\" \"$f\" 2>/dev/null | head -5; done"
}
```


## [2026-09-06T22:36:51.380Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"--- HRN\"; grep -n -i \"lāīdan\\|layidan\\|lāyīdan\\|lāy\" HRN.txt | head -10; echo \"--- HUB\"; grep -n -i \"lāy\\|layidan\" HUB.txt | head -10; echo \"--- CHEUNG\"; grep -n -i \"\\*lā\\b\\|lāy\" CHEUNG.txt | head -20"
}
```


### [2026-09-06T22:36:53.140Z] TOOL RESULT

```
--- MON_part1.txt
4298:آلاییدن: «حل]-2137 (مصم.) (آلابید 
4299:آلاید» خواهد آلایید» بیالای» آلابنده؛ 
4300:آلاییده) آلودن. 
28583:پالاییدن: 0- 0212۷ [- بالودن - بالیدن] 
28584:(بالایید» پالاید» خواهد پالایید؛ بپالای؛ 
--- MON_part2.txt
37656:لاییدن: «:۱30-11 لاب (- لابه) + یدن: 
--- incoming/MON/MON_2vol_Adena_v1_djvu.txt
4298:آلاییدن: «حل]-2137 (مصم.) (آلابید 
4299:آلاید» خواهد آلایید» بیالای» آلابنده؛ 
4300:آلاییده) آلودن. 
28583:پالاییدن: 0- 0212۷ [- بالودن - بالیدن] 
28584:(بالایید» پالاید» خواهد پالایید؛ بپالای؛ 
--- incoming/MON/MON_2vol_Adena_v2_djvu.txt
37656:لاییدن: «:۱30-11 لاب (- لابه) + یدن: 
--- BQT_v1.txt
--- BQT_v2.txt
--- incoming/BQT/BQT_v3_pages.txt
49621:بدل شود. ۱ ۰۷۰ اسم فاعل مرخم ‎col‏ در کلمات مر کب: ‎Vege‏ ژاژلا. رك:لاییدن.
50434:‎Com) ‏اسم فاعل از «لاییدن»‎ - ٩
50442:2-۰ : لاییدن .
--- incoming/BQT/BQT_v4_pages.txt
6976:۴ -... کوینده ( اسم فاعل مرخم ). ‎٩‏ _ لالای ( لایند ) . ر4 : لاییدن .
--- incoming/BQT/BQT_v5_pages.txt
3541:حاشیه سطر ۷ - پس‌آزهپالاییدن» افزوده شود : هه پالیدن ۰
8643:«لاییدن» است .
```


### [2026-09-06T22:36:53.205Z] TOOL RESULT

```
--- HRN
--- HUB
--- CHEUNG
```


## [2026-09-06T22:36:58.709Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '37640,37670p' MON_part2.txt"
}
```


### [2026-09-06T22:36:58.756Z] TOOL RESULT

```
لا یس: +۱ [ع. (افا.) بو شنده (.جامه): 


جامه بوشیدد. 

لابه: (-:۱20|- لاوه. خودستایی؛ تکر. 
درخواست. قس. لاف ] (.) اطهار نباز: 
تسضرع. النماس. به لاه نان کشتادن 
( کفودن): تضر ع التماش کرنشن: تسملق: 
جاپلوسی. به لابه دم جنباندن (جنانیدن): 
(کد.) تملق و چاپلوسی کرد 
خد عه : ِ ره فا از وفع سا 
یک کت ضطراب: قلق. قربان و صدقه. 
لابه گرد نیا (ص‌فا.) تضر ع کننده. متملق. 
چابلوس. فر ببنده. 

لاییدن: «:۱30-11 لاب (- لابه) + یدن: 
بس. مصدری مانوی پارتی: نامیدن دعا 
کردن. درخواست کردن).| تضرع کردن. 
وتو انشت گر ان : 

لاسیدن: «نل120 [- لافیدن| (مص‌ل.) 
خودستایی کردن؛ لاف و گراف گفتن 


لاپ: «:۱ |- لاف | (عم.) لاف و گزاف. 


۰ ۳ ۲ ۱ 
لی. شم بسا
```


## [2026-09-06T22:36:59.832Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"لاییدن\" incoming/BQT/BQT_v4_pages.txt | head; echo ===; sed -n '6960,6990p' incoming/BQT/BQT_v4_pages.txt; echo \"=== v5 ctx\"; sed -n '8630,8650p' incoming/BQT/BQT_v5_pages.txt"
}
```


### [2026-09-06T22:36:59.892Z] TOOL RESULT

```
Exit code 1
6976:۴ -... کوینده ( اسم فاعل مرخم ). ‎٩‏ _ لالای ( لایند ) . ر4 : لاییدن .
(eval):1: == not found
```


## [2026-09-06T22:37:15.700Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"--- CHEUNG lab\"; grep -n \"lāb\\|lʾb\\|LAB\\b\\|\\*lab\" CHEUNG.txt | head -20; echo \"--- MON page markers\"; grep -n \"^\\[pdf page\\|\\f\" MON_part2.txt | head -3; awk 'BEGIN{RS=\"\\f\"} {print NR\": \"substr($0,1,40)}' MON_part2.txt | head -3"
}
```


### [2026-09-06T22:37:17.240Z] TOOL RESULT

```
--- CHEUNG lab
--- MON page markers
1: معین» محمد» ۱۲۹۱ ۱۳۵۰.
```


## [2026-09-06T22:37:17.413Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"--- ARY latin index lay\"; grep -n -i \"LAYIDAN\\|LĀYĪDAN\\|LAY\" incoming/ARY/ARY_latin_index_pages.txt | head; echo \"--- ARY fa\"; grep -n \"لاییدن\\|لابه\" incoming/ARY/ARY_pages.txt | head"
}
```


### [2026-09-06T22:37:17.477Z] TOOL RESULT

```
--- ARY latin index lay
149:Seal th Togs te Uagh S try 905 cud al AB cglay aly 5) LT eS Fly
228:“(VA ginko «ght olay 4 CAF MIARA 64 SL MAIRYA ; gle MAR
248:Hb Sp jee ol ery ye y ght 9 41H J thew slays ls iI Fp
360:718 Obj olay! gta Ghat, / 19
371:Sea OL ZT Bay lay OWL yt y a aKa Gryh 99 gab Ob FossT ys ul
434:BI ee Aig glold A Si2 bog Lay 6 Las y coal y GUT y led Ig) ab ah)
542:“Bly PATRAS 2 Sale) tern soy Slay ceed Sn ee 2 Selly cxsley sels
578:| “gheo pe by GBs) 00 p Clg cal 2 F Gah GF yale Gleajly CHLt y olay!
589:(ANATOLIAN) yyJo3UT l paso glu slay)
594:Wace 5h s rey tab gs diay lig ly te San (LYCIANS) lay y (PALAICS)
--- ARY fa
4441:پالیدن, پالودن, پالاییدن / ۱۵۳
```


## [2026-09-06T22:37:35.714Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN1966 ladanum\"; grep -n -i \"ladanum\\|labdanum\\|ledanon\" KLN_1966.txt | head -10; echo \"=== KLN1966 lotus\"; grep -n -i \"^lotus\\|lotus, n\\.\" KLN_1966.txt | head -10"
}
```


### [2026-09-06T22:37:35.784Z] TOOL RESULT

```
=== KLN1966 ladanum
20927:Derivative:  laager,  intr.  v. labarum,  n.,  the  military  standard  of  the  late  Ro¬ man  Empire.  —  Late  L.  (whence  Byzant.  Gk. Xa(3apciv),  of  uncertain  etymology;  possibly  a Gaulish  word  cogn.  with  OS.  lappo,  OHG.  lap¬ pa,  ‘rag,  shred’,  OE.  Iseppa,  ‘tip,  end,  skirt,  dis¬ trict’  ;  see  lap,  ‘flap  of  a  garment’,  and  cp.  label. See  Walde-Hofmann,  LEW.,  I,  737. labdanum,  n.,  a  fragrant,  bitter  resin.  —  ML.  lab- danum,  fr.  L.  ladanum,  ledanum,  fr.  Gk.  XaSavov, XtjS avov,  fr.  XijSov,  ‘mastic’,  which  is  of  Sem. origin;  cp.  Akkad,  ladunu,  Arab,  ladan,  Heb. lot,  ‘labdanum’.  Pers.  ladan  is  an  Arabic  loan word.  Cp.  laudanum,  lotus, labefaction,  n.,  the  process  of  shaking;  downfall.
20992:lad,  n.  —  ME.  ladde,  ‘a  youth,  manservant’;  of unknown  origin, ladanum,  n.  —  L.  See  labdanum. ladder,  n.  —  ME.  laddre,  fr.  OE.  hlxder,  hlzedder, rel.  to  OFris.  hledere,  MDu.  ledere,  leder  (Du. leer),  Du.  ladder,  OHG.  leitara,  MHG.  leitere, leiter,  G.  Letter,  ‘ladder’,  fr.  I.-E.  base  *kli-,  ‘to slope,  incline’,  whence  also  Goth,  hleipra,  ‘tent’. See  lean,  v.,  and  cp.  climax,  clinical.
21243:Derivatives:  laudable-ness,  n.,  laudabl-y,  adv. laudaninc,  n.,  a  poisonous  alkaloid  (chem.)  — Formed  from  next  word  with  subst.  suff.  -ine. laudanum,  n.,  a  tincture  of  opium.  —  A  ModL. word  used  by  the  Swiss  alchemist  and  physician Paracelsus ;  prob.  a  var.  of  L.  ladanum.  See  lada- num,  labdanum.
21388:Ledum,  n.,  a  genus  of  plants,  the  Labrador  tea ( bot .)  —  ModL.,  fr.  Gk.  XvjSov,  the  plant  Cistus Cyprius.  See  ladanum.
22184:lotus,  n.  —  L.,  fr.  Gk.  Xcoto;,  name  of  various plants,  fr.  Heb.  lot,  ‘labdanum’.  See  labdanum and  cp.  the  first  element  in  Lotophagi  and  the second  element  in  melilot. loud,  adj.  —  ME.  loud,  fr.  OE.  hlud,  rel.  to  OS., OFris.  hlud,  MDu.  luut,  luud,  Du.  luid,  OHG. hlut,  lut,  MHG.  lut,  G.  luut,  ‘loud’,  fr.  I.-E.  pp. base  *klu-to-s,  whence  also  OI.  srutah,  Gk. xXut6<;,  ‘heard  of,  celebrated’,  L.  in-clutus,  in- clitus,  ‘celebrated,  famous’.  Arm.  lu,  ‘known’,
=== KLN1966 lotus
22184:lotus,  n.  —  L.,  fr.  Gk.  Xcoto;,  name  of  various plants,  fr.  Heb.  lot,  ‘labdanum’.  See  labdanum and  cp.  the  first  element  in  Lotophagi  and  the second  element  in  melilot. loud,  adj.  —  ME.  loud,  fr.  OE.  hlud,  rel.  to  OS., OFris.  hlud,  MDu.  luut,  luud,  Du.  luid,  OHG. hlut,  lut,  MHG.  lut,  G.  luut,  ‘loud’,  fr.  I.-E.  pp. base  *klu-to-s,  whence  also  OI.  srutah,  Gk. xXut6<;,  ‘heard  of,  celebrated’,  L.  in-clutus,  in- clitus,  ‘celebrated,  famous’.  Arm.  lu,  ‘known’,
```


## [2026-09-06T22:37:37.316Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SKT\"; grep -n -i \"ladanum\\|LOTUS\" SKT.txt | head -10; echo \"=== AHD watkins\"; grep -n -i \"ladanum\\|lotus\" AHD_watkins1985.txt | head -5; echo \"=== LKT\"; grep -n -i \"ladanum\\|lādan\" LKT.txt | head -10"
}
```


### [2026-09-06T22:37:37.392Z] TOOL RESULT

```
=== SKT
1280:Badger.  <K.-L.)  Spell  bayard  \ix  Sir T.  More;  a  nickname  iorxhc  brock.  M.E. baJger,  hagtr,  a  dealer  in  com,  or,  in  a  bad len&c,  ■  stealer  of  com,  because  the  animal was  supposed  to  steal  com ;  so  also  F. blainau,  a  ba/lgcr,  lit.  *com-stealer,*  from bi^t  com.  Badger  stands  for  bladger,  an- swering to  a  Low  L.  t^j\^  ablaiaiuarius*^ due  to  Low  L.  ablalum,  com.  Cf.  O.  F. btadier,  *  a  merchant,  or  ingrosser  of  com,* Cot.,  Low  L.  bliLiaritax  from  Low  L.  bla- dtim,  short  for  abladum,  ahiaium,  com. p.  I-ow  l^abfatum  signifies  'carried  com,* hence  '  stored  com  ;  from.  L.  ablatum, ncut.  of  abhtus,  carried  away.  «  L.  ah, away:  and  lotus,  put  for  tiattu,  borne, earned;  from  v^TAL.  to  lift.  €  Hut Dr.  Murray  sbcwii  that  ^W^r^s  animal  with a  baJgt  or  sthpe.
10013:Laudanum.  (L.  -  Gk.  -  Pers.)  Now a  preparation  of  opium,  but  formerly  ap- plied to  a  different  drug.  "Laudanum^ Ladanum,  Labdanum,  a  sweet- smelling transparent  gum  gathered  ftom  the  leaves of  Ciitus  Ledon,  a  shrxib,  of  which  they make  pomander,  it  smclLs  like  wine  mingled with  apices;'  Blount.  1674.  (Laudanum has  a  like  strong  smell).  oL.  IddiiHurn,  P^ dannm,  rain  from  the  shrub  la*la  |.Pliiiy).
10698:e  Cyrencaa  lotus,  the  eaters called  htopkagi»  <J)  the  lily
=== AHD watkins
=== LKT
3000:128(i.  Ar.  lädaii: 'Harziger  Gummi'  [aus  pers.  lädän 'Strauch';  vgl.  gr.  Xdbavov  Herod.  III, 112,  lat.  ladanuni];  hieraus  frz.  Udanon, ladanuni;  engl,  ladanum;  russ.  ladan 'Weihrauch,  wohlriechendes  Harz',  la- donka  'Riechkißchen',  (dial.)  ladan  mor- skoj  'Bernstein',  klruss.  ladan  'Weih- rauch', poln.  eech.  ladan  'Ladanum- strauch'.  [Mikl  SlEtWb  159  a.  Bern SlEtWb  682.
6097:Jacf/fc;  1296 ladanum  1286- lalang  54 /«mo  1302
7437:ladanum  1286 Za>'ia;  114 lazulum  1311
```


## [2026-09-06T22:38:03.364Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification && grep -ho \"SKT:[0-9]*\" ../extracted/batch/*.json | sort -t: -k2 -n | uniq -c | tail -20; echo \"=== count total\"; grep -ho \"SKT:[0-9]*\" ../extracted/batch/*.json | wc -l"
}
```


## [2026-09-06T22:38:03.989Z] TOOL CALL #22: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nprint(json.dumps(d['SKT'],ensure_ascii=False,indent=1))\nprint(json.dumps(d.get('LKT'),ensure_ascii=False,indent=1))\n\""
}
```


### [2026-09-06T22:38:05.122Z] TOOL RESULT

```
      1 SKT:340
      3 SKT:344
      1 SKT:354
      3 SKT:357
      3 SKT:360
      3 SKT:366
      2 SKT:372
      4 SKT:378
      1 SKT:384
      1 SKT:394
      1 SKT:454
      1 SKT:462
      2 SKT:468
      2 SKT:507
      1 SKT:542
      4 SKT:543
      1 SKT:578
      2 SKT:581
      1 SKT:592
      1 SKT:1286
=== count total
53
```


### [2026-09-06T22:38:06.844Z] TOOL RESULT

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
{
 "title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927",
 "edition_found": "1927",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/etymologische00lokoguat",
 "identifier": "etymologische00lokoguat",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt",
 "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Numbered entries: 'NNNN. word (language) meaning' - Lokotsch is usually cited by entry number, but Nourai cites pages. grep the oriental source word in transliteration or the number.",
 "notes": "",
 "cites": "entry number of Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs (1927)"
}
```


## [2026-09-06T22:38:15.095Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ndata=open('SKT.txt',encoding='utf-8',errors='replace').read()\n# find line 10013 offset\nlines=data.split('\\n')\noff=sum(len(l)+1 for l in lines[:10012])\nleaf=data.count('\\f',0,off)\nprint('leaf(0-based)',leaf,'-> printed page approx',leaf-20)\nprint(repr(lines[10010:10020]))\nEOF"
}
```


### [2026-09-06T22:38:16.794Z] TOOL RESULT

```
leaf(0-based) 263 -> printed page approx 243
['Laud,  to  praise.  (L.)  M.  E.  laudtn.  — L.  laudare,  to  praise.  »  L.  lamd;  stem  of laus,  praise.', "allow  (3),  to  approve  of.  (F.  —  \\.) M.  E.  ahuin.  —  O.  F  alouer,  later  atlouer^ to  approve  of.  — L.  allauddrt.^'L.  al*  (for ad),  to;  laudare,  to  praise.", 'Laudanum.  (L.  -  Gk.  -  Pers.)  Now a  preparation  of  opium,  but  formerly  ap- plied to  a  different  drug.  "Laudanum^ Ladanum,  Labdanum,  a  sweet- smelling transparent  gum  gathered  ftom  the  leaves of  Ciitus  Ledon,  a  shrxib,  of  which  they make  pomander,  it  smclLs  like  wine  mingled with  apices;\'  Blount.  1674.  (Laudanum has  a  like  strong  smell).  oL.  IddiiHurn,  P^ dannm,  rain  from  the  shrub  la*la  |.Pliiiy).', '■>  Gk.  ATjAaKoK,  AnSafoc  (same).  •  Gk* K^lov,  a  shrub.  —  Pen.  IJdan,  the  gum* herb  lada  (KichardsonV', 'Laugh  (E.)  M  £.  tau^Men,  Uhgken. A.  S.  hlehhan,  hlikan  (pt.  t.  klfh\\  to laugh.  4*  CHi-  la^eMen,  Icel.  ki^t;a,  Dan.  let, SwwL  U,  G.  iMkm,  Goth*  /Uo^on  <^  V', 'i', 'I', 'LAUNCH.', 'LAX', '<BmcULAH«Ai7»KARK:  c£. Gk.  tt4^*t9,  to  Ciw.  L.  trpciiart,  rtteirt, C  craJke,  trtak^  cr^k^  eiack,  dmtik,  Ac) Dtf.  lamgAUr,  A.  S.  kUaktar,']
```


## [2026-09-06T22:38:17.906Z] TOOL CALL #24: Bash

```json
{
 "command": "pdftoppm -f 300 -l 300 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg300 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


### [2026-09-06T22:38:20.804Z] TOOL RESULT

```
total 123080
drwx------ 5 sfmqrb sfmqrb    12288 Sep  6 18:38 .
drwx------ 4 sfmqrb sfmqrb     4096 Sep  6 16:32 ..
-rw-rw-r-- 1 sfmqrb sfmqrb   533122 Sep  6 17:21 afm41_a.png
-rw-rw-r-- 1 sfmqrb sfmqrb   508509 Sep  6 17:21 afm41_b.png
-rw-rw-r-- 1 sfmqrb sfmqrb   969829 Sep  6 17:21 afm41.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1322100 Sep  6 17:20 afm46.png
-rw-rw-r-- 1 sfmqrb sfmqrb   416305 Sep  6 17:20 afm46_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb      880 Sep  6 18:36 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  5157031 Sep  6 18:05 aiw.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    26688 Sep  6 18:20 ary377_bot_p294.png
-rw-rw-r-- 1 sfmqrb sfmqrb    71464 Sep  6 18:20 ary377_p294.png
-rw-rw-r-- 1 sfmqrb sfmqrb    71267 Sep  6 18:19 ary378_p294.png
-rw-rw-r-- 1 sfmqrb sfmqrb    25966 Sep  6 18:19 ary378_top_p294.png
-rw-rw-r-- 1 sfmqrb sfmqrb    76489 Sep  6 17:24 bqt1237_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   127656 Sep  6 18:17 bqt1267_foot_p294.png
-rw-rw-r-- 1 sfmqrb sfmqrb   362419 Sep  6 17:50 bqt1583_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   456331 Sep  6 16:54 bqt1594_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   105420 Sep  6 18:16 bqt27.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2824 Sep  6 16:59 bqt83_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb   703015 Sep  6 17:50 bqt_fn4.png
-rw-rw-r-- 1 sfmqrb sfmqrb   299015 Sep  6 17:50 bqt_fn.png
-rw-rw-r-- 1 sfmqrb sfmqrb   325427 Sep  6 17:50 bqt_n552.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   315487 Sep  6 17:50 bqt_n553.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   330101 Sep  6 17:50 bqt_n554.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   332775 Sep  6 18:33 bqtv2_289_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   560485 Sep  6 17:53 bqtv2_650_s.png
-rw-rw-r-- 1 sfmqrb sfmqrb   541712 Sep  6 17:53 bqtv2_651_s.png
-rw-rw-r-- 1 sfmqrb sfmqrb     9689 Sep  6 18:33 bqtv2_meta.json
-rw-rw-r-- 1 sfmqrb sfmqrb   726576 Sep  6 18:33 bqtv2_n289.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   729454 Sep  6 17:53 bqtv2_n650.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   702551 Sep  6 17:53 bqtv2_n651.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   100817 Sep  6 17:36 bqt_v3_111.png
-rw-rw-r-- 1 sfmqrb sfmqrb   110820 Sep  6 17:36 bqt_v3_112.png
-rw-rw-r-- 1 sfmqrb sfmqrb    91526 Sep  6 16:59 bqt_v3_83.png
-rw-rw-r-- 1 sfmqrb sfmqrb   137595 Sep  6 18:10 buck2.txt
-rw-rw-r-- 1 sfmqrb sfmqrb      146 Sep  6 18:10 buck3.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    64531 Sep  6 16:53 build261.py
-rw-rw-r-- 1 sfmqrb sfmqrb    60498 Sep  6 17:11 build269.py
-rw-rw-r-- 1 sfmqrb sfmqrb    97300 Sep  6 17:16 build270.py
-rw-rw-r-- 1 sfmqrb sfmqrb    52615 Sep  6 17:36 build275.py
-rw-rw-r-- 1 sfmqrb sfmqrb    74145 Sep  6 17:43 build278.py
-rw-rw-r-- 1 sfmqrb sfmqrb    72342 Sep  6 17:58 build283.py
-rw-rw-r-- 1 sfmqrb sfmqrb    28249 Sep  6 18:25 build290a.py
-rw-rw-r-- 1 sfmqrb sfmqrb    63778 Sep  6 18:33 build290b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    68833 Sep  6 18:30 build291.py
-rw-rw-r-- 1 sfmqrb sfmqrb     5043 Sep  6 17:05 c1.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3501 Sep  6 17:05 c2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    56424 Sep  6 17:05 c3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    78058 Sep  6 17:05 c4.png
-rw-rw-r-- 1 sfmqrb sfmqrb 60831599 Sep  6 18:01 cad_k.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb  2530822 Sep  6 18:01 cad_k.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    37980 Sep  6 17:16 c_av.png
-rw-rw-r-- 1 sfmqrb sfmqrb    29703 Sep  6 17:16 c_cros.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1174 Sep  6 17:16 c_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2612 Sep  6 18:28 c_germ.png
-rw-rw-r-- 1 sfmqrb sfmqrb    13418 Sep  6 18:28 c_greek.png
-rw-rw-r-- 1 sfmqrb sfmqrb     8430 Sep  6 18:28 c_ital.png
-rw-rw-r-- 1 sfmqrb sfmqrb    11245 Sep  6 18:28 c_katrang.png
-rw-rw-r-- 1 sfmqrb sfmqrb     6717 Sep  6 18:28 c_katvar.png
-rw-rw-r-- 1 sfmqrb sfmqrb    28872 Sep  6 18:28 c_katvar_zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb    95615 Sep  6 16:39 coord_pg262.png
-rw-rw-r-- 1 sfmqrb sfmqrb  8373934 Sep  6 18:09 cpd.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb   378445 Sep  6 18:09 cpd.txt
-rw-rw-r-- 1 sfmqrb sfmqrb     4560 Sep  6 16:39 crop_ak2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4014 Sep  6 16:39 crop_ak.png
-rw-rw-r-- 1 sfmqrb sfmqrb    25373 Sep  6 16:42 crop_alk.png
-rw-rw-r-- 1 sfmqrb sfmqrb    24852 Sep  6 17:04 crop_fr269.png
-rw-rw-r-- 1 sfmqrb sfmqrb    43238 Sep  6 16:55 crop_germ269.png
-rw-rw-r-- 1 sfmqrb sfmqrb    51654 Sep  6 17:04 crop_gk269.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2585 Sep  6 17:05 crop_gk271.png
-rw-rw-r-- 1 sfmqrb sfmqrb    64142 Sep  6 17:02 crop_gr267.png
-rw-rw-r-- 1 sfmqrb sfmqrb     6411 Sep  6 16:39 crop_gr.png
-rw-rw-r-- 1 sfmqrb sfmqrb    23559 Sep  6 16:42 crop_kohul.png
-rw-rw-r-- 1 sfmqrb sfmqrb    59386 Sep  6 16:39 crop_lat2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    51357 Sep  6 16:55 crop_latin269.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4761 Sep  6 16:39 crop_lat.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3974 Sep  6 16:37 crop_me2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3300 Sep  6 16:37 crop_me.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10236 Sep  6 16:39 crop_op2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4935 Sep  6 16:37 crop_op.png
-rw-rw-r-- 1 sfmqrb sfmqrb     5599 Sep  6 16:37 crop_pers.png
-rw-rw-r-- 1 sfmqrb sfmqrb    22007 Sep  6 17:10 crop_sak.png
-rw-rw-r-- 1 sfmqrb sfmqrb     5110 Sep  6 17:10 crop_sax.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4854 Sep  6 17:10 crop_shekar.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1249 Sep  6 17:05 crop_sirish.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30419 Sep  6 17:02 crop_skt267.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10043 Sep  6 16:58 crop_slav.png
-rw-rw-r-- 1 sfmqrb sfmqrb    24463 Sep  6 16:58 crop_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb  2144625 Sep  6 17:55 dmmpp.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    14732 Sep  6 18:27 e0.json
-rw-rw-r-- 1 sfmqrb sfmqrb    17126 Sep  6 17:54 e1.json
-rw-rw-r-- 1 sfmqrb sfmqrb    51742 Sep  6 18:33 e2.json
-rw-rw-r-- 1 sfmqrb sfmqrb  5301166 Sep  6 17:01 ediv.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb  1773345 Sep  6 17:01 ediv.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  1845041 Sep  6 18:04 gharib.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  3698758 Sep  6 17:50 IEC_full_djvu.txt
-rw-rw-r-- 1 sfmqrb sfmqrb      228 Sep  6 16:34 jscheck.js
-rw-rw-r-- 1 sfmqrb sfmqrb     4265 Sep  6 17:53 kapi_script.png
-rw-rw-r-- 1 sfmqrb sfmqrb   944060 Sep  6 18:06 kent_full.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   288525 Sep  6 18:07 kent_n222.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   285652 Sep  6 18:07 kent_n223.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   282304 Sep  6 18:07 kent_n224.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   268920 Sep  6 18:07 kent_n225.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb     1433 Sep  6 16:45 merge262.py
-rw-rw-r-- 1 sfmqrb sfmqrb    63035 Sep  6 16:56 mk265.py
-rw-rw-r-- 1 sfmqrb sfmqrb    73111 Sep  6 17:13 mk267.py
-rw-rw-r-- 1 sfmqrb sfmqrb    71564 Sep  6 17:08 mk268.py
-rw-rw-r-- 1 sfmqrb sfmqrb    41609 Sep  6 17:31 mk274.py
-rw-rw-r-- 1 sfmqrb sfmqrb    51778 Sep  6 17:32 mk276.py
-rw-rw-r-- 1 sfmqrb sfmqrb    46494 Sep  6 17:52 mk279.py
-rw-rw-r-- 1 sfmqrb sfmqrb    16605 Sep  6 17:54 mk280b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    17667 Sep  6 17:56 mk280c.py
-rw-rw-r-- 1 sfmqrb sfmqrb    43177 Sep  6 17:50 mk280.py
-rw-rw-r-- 1 sfmqrb sfmqrb    58322 Sep  6 17:51 mk282.py
-rw-rw-r-- 1 sfmqrb sfmqrb    63940 Sep  6 18:05 mk285.py
-rw-rw-r-- 1 sfmqrb sfmqrb    67974 Sep  6 18:09 mk286.py
-rw-rw-r-- 1 sfmqrb sfmqrb    60646 Sep  6 18:11 mk287.py
-rw-rw-r-- 1 sfmqrb sfmqrb    50446 Sep  6 18:33 mk292b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    14748 Sep  6 18:27 mk292.py
-rw-rw-r-- 1 sfmqrb sfmqrb    41011 Sep  6 18:29 mk294.py
-rw-rw-r-- 1 sfmqrb sfmqrb  8373934 Sep  6 17:00 mk.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb   378445 Sep  6 17:00 mk.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    11601 Sep  6 16:42 p262-g01.json
-rw-rw-r-- 1 sfmqrb sfmqrb    10625 Sep  6 16:43 p262-g02.json
-rw-rw-r-- 1 sfmqrb sfmqrb    19393 Sep  6 16:46 p262-g03.json
-rw-rw-r-- 1 sfmqrb sfmqrb    19959 Sep  6 16:44 p262-g04.json
-rw-rw-r-- 1 sfmqrb sfmqrb    12063 Sep  6 16:43 p262-g05.json
-rw-rw-r-- 1 sfmqrb sfmqrb    12051 Sep  6 16:44 p262-g06.json
-rw-rw-r-- 1 sfmqrb sfmqrb    12737 Sep  6 16:44 p262-g07.json
-rw-rw-r-- 1 sfmqrb sfmqrb    17259 Sep  6 16:46 p262-g08.json
-rw-rw-r-- 1 sfmqrb sfmqrb    17820 Sep  6 16:53 p262-g09.json
-rw-rw-r-- 1 sfmqrb sfmqrb    17855 Sep  6 16:45 p262-g10.json
-rw-rw-r-- 1 sfmqrb sfmqrb    14983 Sep  6 16:44 p262-g11.json
-rw-rw-r-- 1 sfmqrb sfmqrb    25352 Sep  6 16:46 p262-g12.json
-rw-rw-r-- 1 sfmqrb sfmqrb    17745 Sep  6 16:44 p262-g13.json
-rw-rw-r-- 1 sfmqrb sfmqrb   105748 Sep  6 16:39 p263hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb     5565 Sep  6 17:22 p275_krei_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb    53703 Sep  6 17:22 p275_pahlavi.png
-rw-rw-r-- 1 sfmqrb sfmqrb     7106 Sep  6 17:34 p279_greek.png
-rw-rw-r-- 1 sfmqrb sfmqrb    12970 Sep  6 17:34 p279_word.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3647 Sep  6 17:34 p279_xsaeta.png
-rw-rw-r-- 1 sfmqrb sfmqrb   130651 Sep  6 17:48 p283_arrow.png
drwxrwxr-x 2 sfmqrb sfmqrb     4096 Sep  6 18:02 p284
-rw-rw-r-- 1 sfmqrb sfmqrb    43108 Sep  6 17:51 p284_e0_fa.png
-rw-rw-r-- 1 sfmqrb sfmqrb    89734 Sep  6 17:51 p284_e0.png
-rw-rw-r-- 1 sfmqrb sfmqrb    59639 Sep  6 17:48 p284_e2b.png
-rw-rw-r-- 1 sfmqrb sfmqrb   106502 Sep  6 17:48 p284_e2.png
drwxrwxr-x 2 sfmqrb sfmqrb     4096 Sep  6 18:25 p289
-rw-rw-r-- 1 sfmqrb sfmqrb    54419 Sep  6 18:05 p289_labibi.png
drwxrwxr-x 2 sfmqrb sfmqrb     4096 Sep  6 18:33 p290
-rw-rw-r-- 1 sfmqrb sfmqrb     1476 Sep  6 18:11 p291_esfand.png
-rw-rw-r-- 1 sfmqrb sfmqrb    31043 Sep  6 18:11 p291_root.png
-rw-rw-r-- 1 sfmqrb sfmqrb    66777 Sep  6 16:42 pg261.png
-rw-rw-r-- 1 sfmqrb sfmqrb    84660 Sep  6 16:39 pg262.png
-rw-rw-r-- 1 sfmqrb sfmqrb    71156 Sep  6 16:38 pg263.png
-rw-rw-r-- 1 sfmqrb sfmqrb    92930 Sep  6 16:37 pg264hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    57862 Sep  6 16:35 pg264.png
-rw-rw-r-- 1 sfmqrb sfmqrb    13324 Sep  6 16:57 pg265_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb    86370 Sep  6 16:57 pg265.png
-rw-rw-r-- 1 sfmqrb sfmqrb    79922 Sep  6 16:42 pg266.png
-rw-rw-r-- 1 sfmqrb sfmqrb    70622 Sep  6 16:56 pg267.png
-rw-rw-r-- 1 sfmqrb sfmqrb    69592 Sep  6 16:52 pg268.png
-rw-rw-r-- 1 sfmqrb sfmqrb    71754 Sep  6 16:55 pg269.png
-rw-rw-r-- 1 sfmqrb sfmqrb   122626 Sep  6 16:58 pg270hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    87489 Sep  6 16:55 pg270.png
-rw-rw-r-- 1 sfmqrb sfmqrb   115300 Sep  6 17:05 pg271hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    66696 Sep  6 17:04 pg271.png
-rw-rw-r-- 1 sfmqrb sfmqrb    68566 Sep  6 16:58 pg272.png
-rw-rw-r-- 1 sfmqrb sfmqrb    66829 Sep  6 17:28 pg273_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb   157304 Sep  6 17:10 pg273hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    70615 Sep  6 17:27 pg273.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65586 Sep  6 17:18 pg274.png
-rw-rw-r-- 1 sfmqrb sfmqrb    80338 Sep  6 17:21 pg275.png
-rw-rw-r-- 1 sfmqrb sfmqrb    76740 Sep  6 17:15 pg276.png
-rw-rw-r-- 1 sfmqrb sfmqrb    44171 Sep  6 17:16 pg277.png
-rw-rw-r-- 1 sfmqrb sfmqrb    89267 Sep  6 17:26 pg278.png
-rw-rw-r-- 1 sfmqrb sfmqrb   168655 Sep  6 17:34 pg279hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    75777 Sep  6 17:34 pg279.png
-rw-rw-r-- 1 sfmqrb sfmqrb    82065 Sep  6 17:34 pg280.png
-rw-rw-r-- 1 sfmqrb sfmqrb    61535 Sep  6 17:39 pg281.png
-rw-rw-r-- 1 sfmqrb sfmqrb    70575 Sep  6 17:34 pg282.png
-rw-rw-r-- 1 sfmqrb sfmqrb    74784 Sep  6 17:47 pg283.png
-rw-rw-r-- 1 sfmqrb sfmqrb    81024 Sep  6 17:50 pg284hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    81024 Sep  6 17:51 pg284.png
-rw-rw-r-- 1 sfmqrb sfmqrb   144566 Sep  6 17:49 pg284_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    84487 Sep  6 17:53 pg285.png
-rw-rw-r-- 1 sfmqrb sfmqrb   106264 Sep  6 17:53 pg286hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    76099 Sep  6 18:10 pg286.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72442 Sep  6 17:59 pg287.png
-rw-rw-r-- 1 sfmqrb sfmqrb    53847 Sep  6 17:58 pg288.png
-rw-rw-r-- 1 sfmqrb sfmqrb    28862 Sep  6 18:27 pg289_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb    91779 Sep  6 18:26 pg289.png
-rw-rw-r-- 1 sfmqrb sfmqrb   187988 Sep  6 18:19 pg290hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    98901 Sep  6 18:18 pg290.png
-rw-rw-r-- 1 sfmqrb sfmqrb   105586 Sep  6 18:11 pg291hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    70592 Sep  6 18:10 pg291.png
-rw-rw-r-- 1 sfmqrb sfmqrb   103438 Sep  6 18:12 pg292.png
-rw-rw-r-- 1 sfmqrb sfmqrb    36312 Sep  6 18:20 pg294_p294.png
-rw-rw-r-- 1 sfmqrb sfmqrb   125960 Sep  6 18:28 pg295hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    77133 Sep  6 18:28 pg295.png
-rw-rw-r-- 1 sfmqrb sfmqrb    66500 Sep  6 18:33 pg297.png
-rw-rw-r-- 1 sfmqrb sfmqrb    52844 Sep  6 18:38 pg300.png
-rw-rw-r-- 1 sfmqrb sfmqrb   132637 Sep  6 18:38 sns_n155.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   129771 Sep  6 18:38 sns_n156.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   390669 Sep  6 18:10 syn_n1548.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   390669 Sep  6 18:10 syn_n1549.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   390669 Sep  6 18:10 syn_n1550.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   351684 Sep  6 18:35 tad_n59.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   342929 Sep  6 18:35 tad_n59_mid.png
-rw-rw-r-- 1 sfmqrb sfmqrb   242025 Sep  6 18:34 tad_n60_bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   282364 Sep  6 18:34 tad_n60.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   335678 Sep  6 18:34 tad_n60_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   276093 Sep  6 18:34 tad_n61.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   332662 Sep  6 18:34 tad_n62.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   334767 Sep  6 18:35 tad_n65.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   265879 Sep  6 18:35 tad_n65_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3698 Sep  6 18:19 zar_line.png
```


## [2026-09-06T22:38:26.046Z] TOOL CALL #25: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg300.png"
}
```


### [2026-09-06T22:38:26.374Z] TOOL RESULT

```

```


## [2026-09-06T22:38:26.372Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-06T22:38:42.994Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"لادن\" MON_part2.txt | head -10; echo \"=== ctx\"; grep -n \"لادن\" MON_part2.txt | head -3 | cut -d: -f1 | while read n; do sed -n \"$((n-4)),$((n+4))p\" MON_part2.txt; echo ---; done"
}
```


## [2026-09-06T22:38:43.707Z] TOOL CALL #27: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:1876 --image 2>&1 | tail -40"
}
```


### [2026-09-06T22:38:44.800Z] TOOL RESULT

```
37793:لادن. کل (مطلقاً )؛ زهر. 
37796:لاادن: 7 (- لادن معر. + لادنة معر. + 
37808:همین خاصیت را دارند. منظور از لادنی که 
37816:ر هم ینام لادن و با شحرة اللادن خوانند. 
37817:غالبا صمغ قستوس را لادن عنبری می‌نامند. 
37819:صمغی خوشوی حاصل می‌کردد که لادن 
37831:شناخته شده است؛ گل لادن؛ ایو خنجر» 
39155:لادن» مشکك؛ کافور و غیره) که از آن گویی 
45674:آلادنهه [ع.] (افا) 
69602:و کل رگک‌ها قرار دارد (مانند گل لادن و گل 
=== ctx
اصل؛» پی؛ بیخ. لاد از لاد انکندن: زیر و زیر 
ردان لاد از لاد گشادن ( گشودن): خرات 
کردن؛ وبران کر دن. 
وت اون ز () توعی ار وی ها 
لادن. کل (مطلقاً )؛ زهر. 
لاد: ۱2۵ (- لاذ - معر. لاد لاذه] (ا.) دیبای 
ناز ک و تنک و نرم و خوش قماش. 
لاادن: 7 (- لادن معر. + لادنة معر. + 
لاذن] ( کا.) نام صمغی است خو شوی که از 
---
وت اون ز () توعی ار وی ها 
لادن. کل (مطلقاً )؛ زهر. 
لاد: ۱2۵ (- لاذ - معر. لاد لاذه] (ا.) دیبای 
ناز ک و تنک و نرم و خوش قماش. 
لاادن: 7 (- لادن معر. + لادنة معر. + 
لاذن] ( کا.) نام صمغی است خو شوی که از 
گیاه عشقه حاصل می‌شود و قاعده آور است. 
به همین جهت در طب قدیم آن را در زیر 
دامن زنی که قاعده‌اش بند آمده نود دود 
---


لاچین 
ام از او 
همین خاصیت را دارند. منظور از لادنی که 
ات ی وم لسوت 
خسووت آ رنه ال سس لا من است) 
لااذنه» لاذن. (گی.) نام صمغی که بویی 

---
```


### [2026-09-06T22:38:51.636Z] TOOL RESULT

```
لایدن -۱۸۷۶-
دادن را هم میگوبند ۱ - و چیزی رالی زکوبند | ولاغ باشد که بمعنی سخره و اظرافت است.
که از سر تا بیای چیزی به پیچند . لاجو رد ‎٩‏ ۰ بتح واو و سکون را
لا بیدن ۲ * بروزن ومعنی لافیدن(۱) | و دال بی‌نقطه » سنگی‌است کبود که ازآن نگین
است که سخنان زیاده از حد خودگفتن باشد - | انگشتر سازند و صلایه کرده بجپت مذعبان
و بمعنی پر گویی وهرز هگوبی هم هست. و نقاشان بعمل آورند و تفربح و تقویت کند
لاققق - با تحتالی بواو کشیده . نردبان | وبدخشی آن بهتر از دزماری باشد. .
وزینه پایه را لوبند ۴ - وبمعن ی گردنا همست لاجورد خم دنم خای نقطه دار
وآن چوبی باشد مخروطی ومیخی كوچك برسر | و اسکون یم ,کنایه ازآسمان است و آنرا خم
آن نصب کرده‌اند و اطفال ربسمانی برآن پیجند لاجورد هم میگویند .
و نوعی بر زمین اندازند که مدتی چرخ زند - لاجچوردی سقف « بمعنی‌لاجوردی
و تله را نیز گوبند که آلت گرفتار شدن‌حیوانات | خم است که کنایه از آسمان باشد .
است . لاجچوردینه خم ه بمعنی لاجوردی
لاچ » بروزن باج » مرادف رشوت است سفف است که کنایه ازآسمان باشد .
- و بمعنی برهنه و عربان باشد ۴ - وسگه‌ماده لاچی ۷ - بر وزن کاچی : قاقله باشد
را نی زکوبند 9 . وآنرا هال وهیل نیز گوبند و داخل ادویهٌ حاره
لاج « با جیم فارسی» بمعنی‌بازی وفریب | در طعام‌کنند ۰
69 چش : لایدن .
۱- بلابهگفت شبی میرمجلس تو شوم شدم برغبت خوبش شکمین غلام ونشد .
« حافظ شیرازی ص ۱۱۶ ۰
۴ - از : لاب ( لابه )+ یدن ( پوند مصدری ) ؛ لابه کردن :
بدار دنیا چون برفروخت آتش ظلم سکار آن بجهنم همی‌خورد چو لیم
چوخون وریم بپالوده خیره از مردم بدوزخ آندرلاید که‌خون‌دهندش ورم.
سوزنی سمرقندی 2 لغت نامه >.
دراوراق مانوی ( پارتی ) 1*0 ( نامیدن » دعاکردن , درخواست کردن ) * پارسی میانه (پهلوی)
فارسی : لابه ,م17 , 85805 , ... 86۳9180 ۷110416 0۲ 191 ۸ , 8 هندد1)
4 . 0 ,ا ). غغنی 169۷-870 ۰ سربکلی 16۷۷-810 (گفتگ و کردن » سخن کفتن ) « اسشق
همه
۴ - دست و زبان بدو نرسد کس را آری بماه پر ترسد لاتو .
فرخی سیستالی « لغت نامه > .
۴ - بر سرلور عشق بینی تاج اسر آن دم که عقق بینی لاج -
۱ مولوی بلخی رومی . مثنوی « لفت نامه » .
‎٩‏ عسلای لام :
نمی ترسم از دشمن وز خیالش که باشد دشمنش همچون سکه لاج.
مولوی بلخی رومی . مننوی « لغت نامه >
‎٩‏ لازوزد * لازورد ( مرب ) * 182111 ۳ 122781060 ( فر ) ورك : نغب ۹۹-۹۲
« لازورد ؟ . ۷ - اسم هندی هیل است « فهرست مغخزن‌الادوبه » ۳۳ آلاچی«لفت نامه».
( برهان قاطع ۲۳۷ )
```


## [2026-09-06T22:39:06.327Z] TOOL CALL #28: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:1876 --image 2>&1 | head -20"
}
```


### [2026-09-06T22:39:08.160Z] TOOL RESULT

```
(no exact page map; using offset -1205 -> pdf page 671; check the printed number and re-run with --pdf-page if off)
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1876.png
REF: BQT:1876  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 671  OCR-lang: fas

لایدن -۱۸۷۶-
دادن را هم میگوبند ۱ - و چیزی رالی زکوبند | ولاغ باشد که بمعنی سخره و اظرافت است.
که از سر تا بیای چیزی به پیچند . لاجو رد ‎٩‏ ۰ بتح واو و سکون را
لا بیدن ۲ * بروزن ومعنی لافیدن(۱) | و دال بی‌نقطه » سنگی‌است کبود که ازآن نگین
است که سخنان زیاده از حد خودگفتن باشد - | انگشتر سازند و صلایه کرده بجپت مذعبان
و بمعنی پر گویی وهرز هگوبی هم هست. و نقاشان بعمل آورند و تفربح و تقویت کند
لاققق - با تحتالی بواو کشیده . نردبان | وبدخشی آن بهتر از دزماری باشد. .
وزینه پایه را لوبند ۴ - وبمعن ی گردنا همست لاجورد خم دنم خای نقطه دار
وآن چوبی باشد مخروطی ومیخی كوچك برسر | و اسکون یم ,کنایه ازآسمان است و آنرا خم
آن نصب کرده‌اند و اطفال ربسمانی برآن پیجند لاجورد هم میگویند .
و نوعی بر زمین اندازند که مدتی چرخ زند - لاجچوردی سقف « بمعنی‌لاجوردی
و تله را نیز گوبند که آلت گرفتار شدن‌حیوانات | خم است که کنایه از آسمان باشد .
است . لاجچوردینه خم ه بمعنی لاجوردی
لاچ » بروزن باج » مرادف رشوت است سفف است که کنایه ازآسمان باشد .
- و بمعنی برهنه و عربان باشد ۴ - وسگه‌ماده لاچی ۷ - بر وزن کاچی : قاقله باشد
را نی زکوبند 9 . وآنرا هال وهیل نیز گوبند و داخل ادویهٌ حاره
```


## [2026-09-06T22:39:10.704Z] TOOL CALL #29: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1876.png"
}
```


### [2026-09-06T22:39:11.182Z] TOOL RESULT

```

```


## [2026-09-06T22:39:11.180Z] INPUT

[Image: original 1650x2546, displayed at 1296x2000. Multiply coordinates by 1.27 to map to original image.]


## [2026-09-06T22:39:37.227Z] TOOL CALL #30: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:1876 --image --pdf-page 673 2>&1 | head -30"
}
```


### [2026-09-06T22:39:39.357Z] TOOL RESULT

```
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1876.png
REF: BQT:1876  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 671  OCR-lang: fas

لایدن -۱۸۷۶-
دادن را هم میگوبند ۱ - و چیزی رالی زکوبند | ولاغ باشد که بمعنی سخره و اظرافت است.
که از سر تا بیای چیزی به پیچند . لاجو رد ‎٩‏ ۰ بتح واو و سکون را
لا بیدن ۲ * بروزن ومعنی لافیدن(۱) | و دال بی‌نقطه » سنگی‌است کبود که ازآن نگین
است که سخنان زیاده از حد خودگفتن باشد - | انگشتر سازند و صلایه کرده بجپت مذعبان
و بمعنی پر گویی وهرز هگوبی هم هست. و نقاشان بعمل آورند و تفربح و تقویت کند
لاققق - با تحتالی بواو کشیده . نردبان | وبدخشی آن بهتر از دزماری باشد. .
وزینه پایه را لوبند ۴ - وبمعن ی گردنا همست لاجورد خم دنم خای نقطه دار
وآن چوبی باشد مخروطی ومیخی كوچك برسر | و اسکون یم ,کنایه ازآسمان است و آنرا خم
آن نصب کرده‌اند و اطفال ربسمانی برآن پیجند لاجورد هم میگویند .
و نوعی بر زمین اندازند که مدتی چرخ زند - لاجچوردی سقف « بمعنی‌لاجوردی
و تله را نیز گوبند که آلت گرفتار شدن‌حیوانات | خم است که کنایه از آسمان باشد .
است . لاجچوردینه خم ه بمعنی لاجوردی
لاچ » بروزن باج » مرادف رشوت است سفف است که کنایه ازآسمان باشد .
- و بمعنی برهنه و عربان باشد ۴ - وسگه‌ماده لاچی ۷ - بر وزن کاچی : قاقله باشد
را نی زکوبند 9 . وآنرا هال وهیل نیز گوبند و داخل ادویهٌ حاره
لاج « با جیم فارسی» بمعنی‌بازی وفریب | در طعام‌کنند ۰
69 چش : لایدن .
۱- بلابهگفت شبی میرمجلس تو شوم شدم برغبت خوبش شکمین غلام ونشد .
« حافظ شیرازی ص ۱۱۶ ۰
۴ - از : لاب ( لابه )+ یدن ( پوند مصدری ) ؛ لابه کردن :
بدار دنیا چون برفروخت آتش ظلم سکار آن بجهنم همی‌خورد چو لیم
چوخون وریم بپالوده خیره از مردم بدوزخ آندرلاید که‌خون‌دهندش ورم.
سوزنی سمرقندی 2 لغت نامه >.
دراوراق مانوی ( پارتی ) 1*0 ( نامیدن » دعاکردن , درخواست کردن ) * پارسی میانه (پهلوی)
فارسی : لابه ,م17 , 85805 , ... 86۳9180 ۷110416 0۲ 191 ۸ , 8 هندد1)
4 . 0 ,ا ). غغنی 169۷-870 ۰ سربکلی 16۷۷-810 (گفتگ و کردن » سخن کفتن ) « اسشق
```


## [2026-09-06T22:39:49.479Z] TOOL CALL #31: Bash

```json
{
 "command": "D=data/verification/sources/refs/ocr/BQT && cp $D/1876.png $D/1874.png && pdftoppm -f 673 -l 673 -r 200 -png -singlefile data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf $D/1876 && ls -la $D | head"
}
```


### [2026-09-06T22:39:51.706Z] TOOL RESULT

```
total 41180
drwxrwxr-x  2 sfmqrb sfmqrb  12288 Sep  6 18:39 .
drwxrwxr-x 12 sfmqrb sfmqrb   4096 Sep  6 18:36 ..
-rw-rw-r--  1 sfmqrb sfmqrb 368375 Sep  4 13:39 0001.png
-rw-rw-r--  1 sfmqrb sfmqrb   1684 Sep  4 13:39 0001.txt
-rw-rw-r--  1 sfmqrb sfmqrb 534367 Sep  4 13:39 0049.png
-rw-rw-r--  1 sfmqrb sfmqrb   2677 Sep  4 13:39 0049.txt
-rw-rw-r--  1 sfmqrb sfmqrb   1076 Sep  4 15:27 103.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb 330101 Sep  6 17:59 1092.jpg
-rw-rw-r--  1 sfmqrb sfmqrb   2600 Sep  6 17:59 1092.vision.txt
```


## [2026-09-06T22:39:53.846Z] TOOL CALL #32: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1876.png"
}
```


### [2026-09-06T22:39:53.870Z] TOOL RESULT

```

```


## [2026-09-06T22:40:19.176Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ndata=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nlines=data.split('\\n')\nfor ln in (20927,22184):\n    off=sum(len(l)+1 for l in lines[:ln-1])\n    leaf=data.count('\\f',0,off)\n    print('line',ln,'leaf',leaf,'-> printed p ~',2*(leaf-12),'/',2*(leaf-12)+1)\nEOF"
}
```


### [2026-09-06T22:40:20.898Z] TOOL RESULT

```
line 20927 leaf 459 -> printed p ~ 894 / 895
line 22184 leaf 488 -> printed p ~ 952 / 953
```


## [2026-09-06T22:40:22.361Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== FSD lotus/ladanum\"; grep -n -i \"ladanum\" FSD_vol2.txt FSD_vol3.txt 2>/dev/null | head -5; echo \"=== WEB\"; grep -n -i \"ladanum\" WEB_vol1.txt | head -5; echo \"=== AKD ladunu\"; grep -n -i \"ladunu\\|ladan\" AKD.txt | head -10; echo \"=== FVQ\"; grep -n -i \"ladan\" FVQ.txt | head -5; echo \"=== AFM\"; grep -n \"لادن\" AFM.txt AFM_pages.txt 2>/dev/null | head -5; echo \"=== PLA\"; grep -n -i \"lādan\\|ladan\" incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt | head -5"
}
```


### [2026-09-06T22:40:22.480Z] TOOL RESULT

```
=== FSD lotus/ladanum
FSD_vol2.txt:38416:large  white  flowers  and  yielding  ladanum;  frequrady  ged'da.g.i  
FSD_vol2.txt:61481:1®  T-r  knlfe-handles.  rahit  and  6'.  ladanum.  (2)  An  Old  World  plant  of  the
FSD_vol2.txt:70616:num. [L.,  <   Gr.  Udanon,  <   lldon,  the  mastic,  <   Per.  ladan, shrub.]  lab'da-numf;  lau'da-numf.  —   lad'a-uum* bu.sh",  n.  Any  species  of  CUius  yielding  ladanum;  espe-
FSD_vol2.txt:72749:.   For  ^htidote,  see  OPIUM.  3.  Ladanum.  [Vm.  of  lada  peouhar  cry.  tube",  n.  A   tube  In  a   torpedo-boat  or  other  war-vessel,
FSD_vol2.txt:73997:Thomiau  Winter,  Feb.  4,  1868  p,  339.  [u.  u.  *   oo.  1888.1 [<  Gr.  lUon;  see  ladanum.]  —   le'dura-cam"pljor,  n. A   peculiar  camphor  (CuHsaO)  ohtalnecl  from  tho  leaves  of :!  .the  viiarrow-leaved  Labrador  tea  JLedum  paluatre)  or  wild rosema-y.
=== WEB
85446:gummi; Gr. kommi, gum.] f 1. a sticky substance given off by certain trees and plants, which dries into an uncrys- tallized, brittle mass soluble in water. | 2. any similar plant secretion, as resin. | 3. any plant gum processed for use in in- dustry, art, etc. 4. an adhesive, especially on the back of a postage stamp; glue; mucilage. 5. gum elastic; rubber. 6. any gum tree; also, its wood. 7. a part of a hollow gum log used as a beehive, trough, etc. [Dial.] 8. [pl.] overshoes or rubbers. 9, chewing gum. , acaroid gum or gum acaroides; a gum given off by certain species of Xanthorrhæa. gum ammoniac; ammoniac, a natural gum resin. ' gum anime or animi; same as anime. gum arabic or gum acacia; a gum usually de- rived from Acacia arabica and Acacia vera, used in medicine, in the manufacture of candy, etc. The East Indian variety is from Feronia elephantum. gum butea; a gum derived from Butea fron- dosa, used in medicine and the arts. gum dragon; gum tragacanth. gum elastic; same as caoulchouc. gum elemi; same as elemi. gum juniper; same as sandarac (resin). gum ladanum; the gum or resin of the Cistus ladaniferus. gum resin; a mixture of resin and gum. The gum resins do not flow naturally from plants, but are mostly extracted by incision, in the form of white, yellow, or red emulsive fluids, which dry and solidify. The most important species are olibanum, galbanum, scammony, gamboge, euphorbium, asafetida, aloes, myrrh, and ammoniac. gum sandarac; same as sandarac (resin). gum senegal; a gum resembling gum arabic, brought from Senegal, in Africa. gum tragacanth; a gum obtained from vari- ous Asiatic or east European shrubs and trees of the pea family: also tragacanth. gum, v.t.; gummed, pt., pp.; gumming, p$r. to coat,-unite, or stiffen with gum. gum, v.i. 1. to secrete or form gum. 2. to become sticky or clogged. gum an/i-m4l, the galago of Senegal, a lemur which feeds upon gums. gum/bd, n. [prob. of Indian or Negro origin.] 1. the okra plant. 2. the edible, sticky pods of this plant. 3. a soup thickened with unripe okra pods. 4. a fine, silty soil of the Western prairies, which becomes sticky and nonporous when wet: also gumbo soil. 5. a French patois spoken by Creoles and
100748:j/ron-weed, n. [so named from its hard stem.] a plant of the aster family, with clusters of red, purple, or white tubular flowers. Vron:wood, 7. any of many trees having very hard, heavy wood, as some species of trees of the genus Sideroxylon; also, the wood. W/ron-work, n. the parts of a building, vessel, carriage, etc. which consist of iron; anything _ made of iron. V/ron-work-ér, 7. 1. a person who makes iron or articles of iron. 2. a worker who builds the framework of _ Steel bridges, etc. Vron-works, n. pl. [also construed as sing.) an establishment where iron is manufactured, _, Wrought, or cast into ironwork. Vron-wort, n. 1.a plant of the genus Sideritis. 2. one of the hemp nettles, Galeopsis tetrahit T _„Or Galeopsis ladanum. a /ron-y (ürn-), a. 1. made or consisting of c iron; of the nature of iron; as, irony chains, trony particles. BY = 2. resembling iron; hard. BC i/r6n-y, n.; pl. i/ron-ies, [Fr. ironie; L. ironia; Bi Gr. eiréneza, dissimulation, irony, from eiron, a dissembler in speech, from eirein, to speak.]
104457:the royal cavalry standard carried before the Roman emperors in war, especially that first carried by Constantine, the first emperor to adopt Christianity: it usually bore the first two letters (XP) of the Greek Khristos (Christ). lab’/da-num, n. [ML.; L. ladanum, ledanum; Gr. ladanon, lédanon, from lédon, mastic; Ar.ladan; Per. lédan,) a dark resin obtained from certain varieties of the rockrose:
104458:also ladanum. lab-@-fac/tion, n. [L. labefactus,
105945:The difference between reason and revela- , wi i a z 1 tion—and in what sense the lalter is su- together math miin i S “laughing hyena; the spotted byari tralian i l perior. —Watts. Jaud, v.i. [ME. lauden; L. laudare, to praise, laughing jackass; Dacelo Biggs, an suggest i lat’t@r-day, a. of recent or present time; mod- “from laus, laudis, praise, glory.] to praise; to kingfisher with a ‘or; Kookaburra i ji ern. extol. Š ; ` > A, Sceloglaux H Lat’ter-day Saint, a Mormon. laud-a-bil/i-ty, n. the quality of being lauda- alee paste New Zealand org 1 l lat’tér-kin, ». a glazing tool, used, particu- ble; praiseworthiness; commendability. = RAEN oe a OTY. way; with laugh- l wines m poa kain won. tand able, a. [L. laudabilis, from laudare, to ug ingly, cór ine idicule; @ | at/tér-ly, adv. lately; of late; in time not lon raise. Pe Pe ject of ridicu past. X 7 : see 1. worthy of being lauded; praiseworthy; Peughline stock, n. an obj Ie lat/ter-math, n. the latter mowing; aftermath. commendable; as, laudable motives, laudable yty¢ ih’ ter n. (ME. laughter, lauhter; AS. hea {Dial.] actions. ae ave aate ‘from hlehhan, to laugh} id re- lat/ter-mést, a. last in succession; farthest to- 2. in medicine, such as indicates an im- of ine Notion of laughing or the soun I ward the rear. i proving condition; healthy; salubrious; nor- sulting fe lattice (-tis), n. [OFr. lattis, a lattice, from mal; as, laudable pus. [Obs.] 2 a matter for or cause of laughter: ticule, a latte; AS. læti, alath.] laud’à-ble-ness, 7. the quality of deserving Syn.—merriment, glee, derision, by 1. an openwork praise; praiseworthiness. cachinnation, contempt. i structure of wood, laud/a-bly, adv. in a manner deserving praise. J4ugh/tér-less, 4. without laughter. hedat: i 4 metal, etc. made by lau/da-nine, z. an alkaloid derived from 44 , 1 ne deserving to be laugar j l z crossing laths, rods, “opium. BEF läugh WODY G; efflorescent hydrous om E $ or bars, and forming lau/da-num, 1. [L. ladanum, labdanum.] Tau mon ai e e calcium: S° calle a network used as a “14. formerly, any of various preparations cate of adn coverer. screen, support, etc. ; containing opium. Laumont, its C1 [Obs r ofa as, the lattice of a 2. tincture of opium; a solution of opium in launce, 7. a balance. lance Jance.) 2”) out na algae l Hance, m (Mie Lot a pares . a window, door, 3. labdanum. [Obs.] small group dy, found in uncle Z ate, etc. screened da! ti ; ; _ and along, slender body, touy, sand 1 l by such a structure. lauda tion pl laut Coon a coastal waters: also lance, lan 2 ; 3. something re- praise; commendation * sand eel. [0bs-] ing. per Dra ER Ta BRE laud/A-tive, n. a panegyric. [Obs.] launce’gay, n: ^ PE bp aun cit | it Wonks as, in herald- lgud/a-tive, a. eulogistic; laudatory. - launch ot im launchers O r. an m i ry, a bearing of lgud/a-to-ry, a. containing or expressing n throw, hurl asa lance, from ta pon: | Grossbars, vertical LATTICE-WINDOW praise; tending to praise; eulogistic. ae 1 aof @w™ | nee horizontal. lauda (Day, pen which contains praise; * te to hurl, discharge: °F sen as tH la lat’tice, v.t.; latticed (-tist), pt., 3 - _ aculogy. S. w, etc.)- Š e forces ir. i ticing, ppr. 1. to R a eee laud/ér, n. one who praises. BA to a forth with Se into ts op lid? make a lattice of. laugh (laf or laf), v.i.; laughed (läft or laft), pt., catapult launched ube PS ati vesse afloat: ) "2. to cover or furnish with a lattice or lat- ppi laughing, ppr. [ME. laughen; AS. hleh- 3. to cause aI water; tO S° A ticework. an, hlikhan, to laugh; of imitative origin.] from the land into a pool fis pcs x noti : 1026 fate, far, fast, fall, final, care, at; méte, prey, hér, met; pine, marine, bird, pin; note, move, for, atom,
=== AKD ladunu
947:ncrd,  aram.  nardd,  griech.  vöqSos  usw.,  Narde,  wohl  <]  ind.  ndlddd.] [akk.  ladunu  jedenfalls  Premdw.  :  griech.  XtjSov,  h'jSavoy,  Ladanum;  dazu viell.  hebr.  löf.  dem  vieU.  auch  im  Aklc.  luffti  entspricht.]  akk.  a))iru
=== FVQ
=== AFM
AFM.txt:5744:والمسك واللادن والكافور 
AFM_pages.txt:3614:والمسك واللادن والكافورܒܝ <
=== PLA
17425:©>V - 1ädan: "Ladanumt pers. > griech > lat.
```


## [2026-09-06T22:41:02.948Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN lull\"; grep -n \"lull,  \" KLN_1966.txt | head -3; echo \"=== KLN lament\"; grep -n \"lament,  \" KLN_1966.txt | head -3; echo \"=== KLN lalein/glossolalia\"; grep -n -i \"glossolalia\\|echolalia\" KLN_1966.txt | head -3"
}
```


### [2026-09-06T22:41:03.026Z] TOOL RESULT

```
=== KLN lull
17966:of  homo,  ‘man’.  See  homage, home,  n.  —  ME.  home,  hoom,  fr.  OE.  ham,  rel.  to OS.  hem,  ‘home’,  OFris.  hem,  ham,  ‘home,  vil¬ lage’,  ON.  heimr,  ‘residence,  world’,  heima, ‘home’,  Swed.  hem,  Dan.  hjem,  MDu.  heem, heim,  OHG.,  MHG.,  G.  heim,  ‘home’,  Goth. haims,  ‘village’,  and  cogn.  with  Gk.  xcopr),  ‘vil¬ lage’,  xoipav,  ‘to  lull,  put  to  sleep’,  Lith.  kaimas , OPruss.  caymis,  ‘village’,  OSlav.  semija,  Lith. seimyna,  Lett,  saime,  OPruss.  seimins,  ‘domestic servants’,  OIr.  coim,  coem,  ‘dear,  beloved’,  OW. cum,  ModW.  cu,  of  s.m.,  L.  -haemum  (a  Teut. loan  word)  in  Boihaemum,  ‘Bohemia’,  lit.  ‘home of  the  Boi’ ;  formed — with  -m-formative  element — fr.  I.-E.  base  *fcei-,  ‘to  lie,  settle  down’,  whence also  Goth,  heiwa-frauja,  ‘master  of  a  house’,  OE. hi  wan  (pi.),  ‘members  of  a  family’,  hiwen,  ‘family, household’,  OHG.  hi  wo,  ‘husband’,  hiwa,  ‘wife’, hiun  (pi.),  ‘married  couple’,  ON.  him,  ‘married couple,  household’,  OE.  higid,  hid,  ‘hide  of land’,  lit.  ‘land  (sufficient)  to  support  a  family’, OE.  hiw-rseden,  hi-red,  ‘family,  household', OHG.,  MHG.  hi-rat,  G.  Hei-rat ,  ‘marriage’, orig.  ‘care  of  the  house’  (the  second  element  of these  latter  words  means  ‘advice,  counsel’;  see rede,  n.),  and  L.  civis,  ‘citizen’.  See  civil  and cp.  the  first  element  in  comedy.  Cp.  also  ham, ‘hamlet’,  hamesucken,  hamlet,  haunt,  Henry, hide,  ‘measure  of  land’,  hind,  ‘farm  servant’, Bohemia.  Cp.  also  erne,  oom.
22286:lull,  tr.  and  intr.  v.  —  ME.  lullen,  lollen,  of  imita¬ tive  origin.  Cp.  Swed.  lulla,  MLG.,  MDu.  lollen, G.  lullen,  'to  rock',  OI.  lolati,  'moves  to  and  fro’, lulitali ,  ‘swinging’,  lalati,  ‘skips,  frisks'.  All  these words  are  derivatives  of  the  I.-E.  imitative  base *lel-,  *lul-,  ‘to  move  to  and  fro’.  Cp.  loll,  Lollard, lollop.  Cp.  also  the  imitative  base  *lal-,  seen  in Gk.  XaXeiv,  ‘to  talk,  chat,  prattle’,  XaXoi ;,  ‘talk¬ ative,  loquacious’,  L.  lallare,  ‘to  sing  to  sleep,  to lull’ ;  see  Lalage  and  words  there  referred  to. Derivative:  lull,  n.
38045:tales,  n.,  1)  a  person  summoned  to  make  up  a deficiency  in  the  jury;  2)  a  writ  summoning such  a  person  to  serve  on  a  jury,  (law)  —  From L.  tales,  the  first  word  in  the  phrase  tales  de circumstantibus,  ‘such  of  the  bystanders',  pi. of  tails,  ‘such’,  which  is  formed  with  suff.  -I  fr. the  I.-E.  pron.  base  *to-,  Cp.  Gk.  TTjXiv.ot;,  ‘so old’,  OSlav.  lull,  ‘so’,  toliku,  ‘so  much’,  Russ. toliko,  ‘only’,  which  are  similarly  formed.  For other  derivatives  of  I.-E.  base  *to-  see  the  and words  there  referred  to.
=== KLN lament
8329:comely,  adj.  —  ME.  cumelich,  cumlich,  comeliche, comlich,  fr.  OE.  cymlie,  formed  with  suff.  -lie (see  like,  adj.),  fr.  cyme,  ‘fine,  beautiful,  splen¬ did’,  orig.  ‘frail,  delicate,  tender’,  which  is  rel. to  ME.  kime,  ‘weak,  delicate’,  OHG.  chumo, kiimd,  MHG.  kume,  ‘with  difficulty’,  OHG. chumig,  kumig,  ‘weak,  delicate’,  G.  kaum, ‘hardly,  scarcely’.  The  original  meaning  of  ME. kime  and  OHG.  chumig  was  ‘lamentable,  piti¬ able’;  cp.  OHG.  chuma,  ‘sorrow’,  OHG.  chu- mon,  ‘to  mourn’,  OS.  kumian,  ‘to  lament,  de¬ plore’.  All  these  words  are  derivatives  of  the I.-E.  imitative  base  *gou-,  *gow-,  ‘to  shout,  cry’ whence  also  OE.  ciegan  (for  orig.  *kaujan ),  ‘to call’,  cyta,  ‘kite’,  Ol.gavate,  ‘sounds,  resounds’, Gk.  yoav,  ‘to  wail,  groan,  weep’,  MLG.  kitten, ‘to  chatter,  babble,  prate’,  Lith.  gaudziii,  gausti, ‘to  howl’,  gaudas,  ‘lamentation’,  OSIav.  govoriti, ‘to  make  a  noise’,  Russ,  govorit',  Serb,  and Croat  ian^ovoWh,  Czech  hovoriti,  Slovak  hovorit’, ‘to  speak’,  OIr.  guth,  ‘voice’.  Cp.  kite.  The  word comely  was  influenced  in  meaning  by  an  as¬ sociation  with  come.
14703:figure,  tr.  and  intr.  v.  —  F.  figurer,  fr.  L.  figurare, ‘to  form,  shape’,  fr.  figura.  See  figure,  n.,  and cp.  configure,  disfigure,  prefigure,  transfigure. Derivative:  figur-ed,  adj. figurine,  n.,  a  small  figure;  a  statuette.  —  F.,  fr. It.  figurina,  dimin.  of  figura,  fr.  L.  figura.  See figure,  n.,  and  -ine  (representing  L.  -inus). fig  wart,  a  condyloma.  -  Cp.  OE./ic,  MHG.  vie, veig,  ‘the  piles’,  fr.  L.  ficus,  ‘fig  tree,  fig;  the piles’  (see  fig,  n  );  so  called  from  its  shape. Filago,  n.,  a  genus  of  plants  of  the  thistle  family (hot.)  —  ModL.,  fr.  L.  filum,  ‘thread’.  See  file, ‘collection  of  papers’.  Cp.  Gifola. filament,  n.,  a  fine  thread,  fiber.  —  F.,  fr.  ModL. filamentum,  fr.  Late  L.  filare,  ‘to  spin’.  See  file, ‘collection  of  papers’,  and  -ment.
14710:—  In  some  senses  fr.  F.  file,  ‘row’,  fr.  filer,  ‘to spin’,  fr.  Late  L.  filare,  ‘to  spin’  (whence  also It.  filare,  OProveng.  filar,  Sp.  hilar,  ‘to  spin’),  fr. L.  filum,  ‘thread’,  in  some  fr.  E.fil,  ‘thread’  (fr. L.  filum).  L.  filum  stands  for  I.-E.  base  *gwhis- lom  and  is  cogn.  with  Arm.  Jit,  ‘sinew,  string, line’,  Lith.  gysla,  ‘vein,  sinew’,  Lett,  dzisla, ‘vein’,  OPruss.  pette-gislo,  ‘vein  of  the  back’, OSIav.  zifa,  ‘vein’.  L.  funis,  ‘rope,  line,  cord’, is  not  cognate.  Cp.  Filago,  filament,  Filaria, filigree,  ficelle,  enfilade,  profile,  purfle.  Cp.  also hilum,  nihil.
=== KLN lalein/glossolalia
```


## [2026-09-06T22:41:03.720Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PLA ctx\"; sed -n '17415,17435p' incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt; echo \"=== AFM لاذن\"; grep -n \"لاذن\\|اللادن\" AFM.txt | head -5"
}
```


### [2026-09-06T22:41:03.784Z] TOOL RESULT

```
=== PLA ctx
rd. 


aiumart: "der Urmensch" mp. ale ps gayomart _ aw. gayo- 
marata 7, ar.) kaiumart. 


lädan 240 ladg 


©>V - 1ädan: "Ladanumt pers. > griech > lat. 


\ 
a) - läranf: ägypt. Ar. lärang = ar. näranf a. v. 2, 


a) - läzward: "Lapislazuli" pers. >.) lazward 3, 
lazulith: "Blauspat" (pers. ladschuward) 4 
Lapislazuli: Lasurstein, blauer Halbedelstein pers. > ar. > lat. 
lasieren: mit Lasur versehen pers. —>lat. roman. us 
=== AFM لاذن
5744:والمسك واللادن والكافور
```


## [2026-09-06T22:41:18.601Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ndata=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=data.split('\\f')\nfor i in (457,458,459,460):\n    t=leaves[i]\n    print('--- leaf',i, repr(t[:120]))\n    print('   tail:',repr(t[-120:]))\nEOF"
}
```


### [2026-09-06T22:41:20.560Z] TOOL RESULT

```
--- leaf 457 'yoav,  ‘to  wail, groan,  weep’,  yooq,  ‘wailing,  groaning,  weeping’, OE.  cyme,  ‘fine,  beautiful,  splendid’,  ori'
   tail: ' Cp.  ON. knoka,  ‘to  knock’,  which  is  also  imitative. Derivatives:  knock,  n.,  knock-er,  n. knoll,  n.,  top  o'
--- leaf 458 'f  a  small  hill.  —  ME.  knot,  fr.  OE. cnoll,  ‘hill  top,  hill’,  rel.  to  ON.  knollr,  ‘hilltop’, MLG.,  MHG.,'
   tail: ' cross  stamped  upon  it.  See  cross  and  -er. kriegspiel,  n.,  a  war  game.  —  G.  Kriegsspiel,  lit. ‘war  game’'
--- leaf 459 ',  fr.  Krieg,  ‘war’,  and  Spiel,  ‘game’. The  first  element  is  of  uncertain  origin.  For  the second  element  '
   tail: 'ing  form  denoting  1)  the  lips;  2)  la¬ bial  and.  —  Fr.  L.  labium,  ‘lip’.  See  labial, labiodental,  adj.,  '
--- leaf 460 'pertaining  to,  or  formed  with, the  lips  and  teeth.  —  Compounded  of  labio-  and dental.\nDerivative :  labioden'
   tail: 'ing  to  Laconia;  n.,  a  La¬ conian  or  Lacedaemonian.  —  See  Laconic  and suff.  -an.\nlaemus,  n.,  litmus.  —  Du'
```


## [2026-09-06T22:41:33.336Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ndata=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=data.split('\\f')\nfor i in (437,438,439):\n    t=leaves[i]\n    print('--- leaf',i, repr(t[:200]))\n    print('   tail:',repr(t[-150:]))\nEOF"
}
```


### [2026-09-06T22:41:36.146Z] TOOL RESULT

```
--- leaf 437 '  -ory fr.  L.  invocatus,  pp.  of  invocare.  See  invoke, invoice,  n.  —  Fr.  earlier  invoyes,  pi.  of  obsolete invoy,  ‘anything  sent’,  fr.  F.  envoy,  now  spelled envoi,  ‘a  sending’,  '
   tail: ',  adv.,  irenic-ism,  n., irenic-ist ,  n.\nirenicon,  n.  —  See  eirenicon.\nIresine,  n.,  a  genus  of  plants  of  the  amaranth family  ( bot .) '
--- leaf 438 ' —  ModL.,  fr.  Gk.  eEpeauovr),  ‘a wreath  of  olive  wound  round  with  wool’,  fr. slpo q,  ‘wool’,  which  is  rel.  to  gpiov,  ‘wool’  (see erio-) ;  so  called  in  allusion  to  the  woolly'
   tail: 'ng,  irrigating’,  fr.  irrigatus,  pp.  of  irrigare.  See prec.  word  and  -ion.\nDerivatives:  irrigation-al,  adj.,  irrigation-ist,  n. irrigativ'
--- leaf 439 'e,  adj.  —  Formed  with  suff.  -ive  fr.  L.\nirrigatus,  pp.  of  irrigare.  See  irrigate, irriguous,  adj.,  moist,  irrigated.  —  L.  irriguus, ‘watered,  wet’,  from  the  stem  of  irrigare. '
   tail: ',  as  equivalent  to  L.  -us, see  suff.  -ous.\nirritable,  adj.  —  L.  irritabilis,  ‘easily  excited’,  fr. irritare,  ‘to  excite’.  See  irrita'
```


## [2026-09-06T22:41:44.273Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ndata=open('KLN_1971.txt',encoding='utf-8',errors='replace').read()\nimport re\ni=data.find('labdanum')\nprint('found at',i,'of',len(data))\nleaf=data.count('\\f',0,i)\nprint('leaf',leaf,'total leaves',data.count('\\f'))\nprint(data[i-200:i+700].replace('\\n',' '))\nEOF"
}
```


### [2026-09-06T22:41:45.903Z] TOOL RESULT

```
found at 4761609 of 9828418
leaf 0 total leaves 0
ossibly a  Gaulish word cogn. with OS. lappo, OHG. lap-  pa , ‘rag, shred’, OE. Iseppa, ‘tip, end, skirt, dis-  trict’; see lap, ‘flap of a garment’, and cp. label.  See Walde-Hofmann, LEW., I, 737.  labdanum, n., a fragrant, bitter resin. — ML. lab-  danum , fr. L. ladanum, ledanum , fr. Gk. XaSavov,  XtqS avov, fr. XrjSov, ‘mastic’, which is of Sem.  origin; cp. Akkad, ladunu , Arab, ladan , Heb.  lot, ‘labdanum’. Pers. ladan is an Arabic loan  word. Cp. laudanum, lotus,  labefaction, n., the process of shaking; downfall.   — Formed with suff. -ion fr. L. labefactus , pp.  of labefacere, ‘to cause to totter, shake, over-  throw’, which is compounded of labi, ‘to slip,  slide, glide’, and facere,'" to make, do’. See labor  and fact and cp. next word.   label, n. — ME., fr. OF. label, lambel, ‘a strip’  (whence F. lambeau , ‘strip, rag, shred, tatter,  fragment, scrap’), prob. fr. Franki
```


## [2026-09-06T22:42:16.472Z] TOOL CALL #40: Bash

```json
{
 "command": "sed -n '1,60p' /home/sfmqrb/git/rishe/tools/fetch_source.py"
}
```


### [2026-09-06T22:42:16.513Z] TOOL RESULT

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


## [2026-09-06T22:42:25.534Z] TOOL CALL #41: Bash

```json
{
 "command": "for u in \\\n \"https://www.etymonline.com/word/lull\" \\\n \"https://www.etymonline.com/word/lament\" \\\n \"https://www.etymonline.com/word/lotus\" \\\n \"https://www.etymonline.com/word/ladanum\" \\\n \"https://www.etymonline.com/word/glossolalia\" \\\n \"https://www.etymonline.com/word/echolalia\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 300, roots Lâ / Ladunu: English node etymology\" ; done 2>&1 | tail -10"
}
```


### [2026-09-06T22:42:30.137Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/5c93acf4d136049e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/aa854c90cfc1fb78.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3092f0ce2efad943.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f8dd87284af62432.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f38d666665f7c6ba.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a5c4c0f052441091.txt
```


## [2026-09-06T22:42:30.518Z] TOOL CALL #42: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/%CE%BB%CE%AC%CE%B4%CE%B1%CE%BD%CE%BF%CE%BD\" \\\n \"https://en.wiktionary.org/wiki/%CE%BB%CF%89%CF%84%CF%8C%CF%82\" \\\n \"https://en.wiktionary.org/wiki/%CE%BB%CE%B1%CE%BB%CE%AD%CF%89\" \\\n \"https://en.wiktionary.org/wiki/lamentum\" \\\n \"https://en.wiktionary.org/wiki/%D9%84%D8%A7%DB%8C%DB%8C%D8%AF%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%D9%84%D8%A7%D8%AF%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%D9%84%D8%A7%D8%A8%D9%87\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 300, roots Lâ / Ladunu: Greek/Latin/Persian node etymology\" ; done 2>&1 | tail -10"
}
```


### [2026-09-06T22:42:36.233Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/c8ccc09bec9e2510.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9fa6b63538a8e178.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/cd6d8191764528f2.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/2d0fba3489465d87.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f9fd43eca6254598.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9a668ec268c2acf0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/544a3cce37d69654.txt
```


## [2026-09-06T22:42:38.938Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 5c93acf4d136049e aa854c90cfc1fb78 3092f0ce2efad943 f8dd87284af62432 f38d666665f7c6ba a5c4c0f052441091; do echo \"######## $f\"; head -c 1400 $f.txt | tr -s ' '; echo; done"
}
```


### [2026-09-06T22:42:40.766Z] TOOL RESULT

```
######## 5c93acf4d136049e
URL: https://www.etymonline.com/word/lull
FETCHED: 2026-09-06T22:42:27Z
STATUS: 200
TITLE: Lull - Etymology, Origin & Meaning

Lull - Etymology, Origin & Meaning 

 Search 
 Log in 

 Columns 
 Forum 
 Apps 
 Premium 

 Log in 

 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 Origin and history of lull 

 lull (v.) 

 early 14c., lullen "to calm or hush to sleep," probably imitative of lu-lu sound used to lull a child to sleep (compare Swedish lulla "to hum a lullaby," German lullen "to rock," Sanskrit lolati "moves to and fro," Middle Dutch lollen "to mutter"). Figurative use from 1570s; specifically "to quiet (suspicion) so as to delude into a sense of security" is from c. 1600. Related: Lulled ; lulling .
 also from early 14c. 

 lull (n.) 

 1650s as the name of a soothing drink, from lull (v.). The meaning "temporary period of quiet or rest amid turmoil or activity" is attested by 1751, originally figurative ("... the first appearance of a lull of his resentment ...," "Memoirs of a Coxcomb"); literal use by 1778, said to be a sailors' word, in reference to violent surf or storms.
 also from 1650s 

 Entries linking to lull 

 lullaby (n.) 

 "soothing song sung to infants," 1580s, noun use of the words lulley by (1560s), from Middle English lollai or lullay , a common burden in nursery songs, from lu
######## aa854c90cfc1fb78
URL: https://www.etymonline.com/word/lament
FETCHED: 2026-09-06T22:42:28Z
STATUS: 200
TITLE: Lament - Etymology, Origin & Meaning

Lament - Etymology, Origin & Meaning 

 Search 
 Log in 

 Columns 
 Forum 
 Apps 
 Premium 

 Log in 

 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 Origin and history of lament 

 lament (v.) 

 "express sorrow, utter words or sounds of grief" (intransitive), mid-15c., lamenten , a back-formation from lamentation or else from Old French lamenter "to moan, bewail" (14c.) and directly from Latin lamentari "to wail, moan, weep, lament," from lamentum "a wailing, moaning, weeping." The transitive sense of "mourn for, deplore" is attested by 1610s. Related: Lamented ; lamenter ; lamenting; lamentingly .
 also from mid-15c. 

 lament (n.) 

 1590s, "expression of sorrow or grief," from French lament and directly from Latin lamentum "a wailing, moaning, weeping" (see lamentation ). From 1690s as "a mourning song."
 also from 1590s 

 Entries linking to lament 

 lamentation (n.) 

 "act of bewailing, expression of sorrow," late 14c., lamentacioun , from Old French lamentacion "lamentation, plaintive cry," and directly from Latin lamentationem (nominative lamentatio ) "a wailing, moaning, a weeping," noun of action from past-participle stem of lamentari "to wail, moan, weep," from
######## 3092f0ce2efad943
URL: https://www.etymonline.com/word/lotus
FETCHED: 2026-09-06T22:42:28Z
STATUS: 200
TITLE: Lotus - Etymology, Origin & Meaning

Lotus - Etymology, Origin & Meaning 

 Search 
 Log in 

 Columns 
 Forum 
 Apps 
 Premium 

 Log in 

 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 Origin and history of lotus 

 lotus (n.) 

 a name given to various plants, not all related or alike, 1540s, from Latin lotus , from Greek lotos , a word used as a name for several plants before it came to mean Egyptian white lotus (a sense attested in English from 1580s). It is perhaps from Semitic (compare Hebrew lot "myrrh"). The plant bears a prominent part in the mythology of India, Egypt, China. The Homeric lotus later was held to be a North African shrub, from which "a kind of wine" [Century Dictionary] can be made. The name has also been given to several species of water-lilies and a bean that grows in water. The yogic sense is attested from 1848.

 It was believed to induce a dreamy forgetfulness, hence lotus-eater "one who finds pleasure in a listless life" (1812) is from Greek lotophagoi , mentioned in "Odyssey," book IX (see lotophagi ).
 also from 1540s 

 Entries linking to lotus 

 lotophagi (n.) 

 c. 1600, literally "lotus-eaters," from Greek lotophagoi (plural), from lotos (see lotus ) + -phagos "eating" (from P
######## f8dd87284af62432
URL: https://www.etymonline.com/word/ladanum
FETCHED: 2026-09-06T22:42:29Z
STATUS: 200
TITLE: Ladanum - Etymology, Origin & Meaning

Ladanum - Etymology, Origin & Meaning 

 Search 
 Log in 

 Columns 
 Forum 
 Apps 
 Premium 

 Log in 

 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 Origin and history of ladanum 

 ladanum 

 see laudanum .

 Entries linking to ladanum 

 laudanum (n.) 

 "tincture of opium," c. 1600, from Modern Latin laudanum (1540s), coined by Paracelsus for a medicine he mixed, supposed to contain gold and crushed pearls and many expensive ingredients, but probably owing its effectiveness to only one of them, opium.

 Perhaps from Latin laudare "to praise" (see laud ), or from Latin ladanum "a gum resin," from Greek ladanon , a word perhaps of Semitic origin. The word soon came to be used for "any alcoholic tincture of opium."

 Latin ladanum had been used in Middle English from late 14c. in reference to plant resins, especially of certain shrubs in Iberia used in medicinal treatments, but this is not regarded as the immediate source of the 16c. word.

 Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 Share ladanum 

 ‘ cite ’ 
 Page URL :
 https://www.etymonline.com/word/ladanum Copy 

 HTML Link :
 <a href="https://www
######## f38d666665f7c6ba
URL: https://www.etymonline.com/word/glossolalia
FETCHED: 2026-09-06T22:42:29Z
STATUS: 200
TITLE: Glossolalia - Etymology, Origin & Meaning

Glossolalia - Etymology, Origin & Meaning 

 Search 
 Log in 

 Columns 
 Forum 
 Apps 
 Premium 

 Log in 

 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 Origin and history of glossolalia 

 glossolalia (n.) 

 "gift of tongues, speaking in tongues, ability to speak foreign languages without having learned them," 1857 (earlier in German and Italian), from Greek glōssa "tongue, language" (see gloss (n.2)) + lalia "talk, prattle, a speaking," from lalein "to speak, prattle," echoic.
 also from 1857 

 Entries linking to glossolalia 

 gloss (n.2) 

 "word inserted as an explanation, translation, or definition," c. 1300, glose (modern form from 1540s; earlier also gloze ), from Late Latin glossa "obsolete or foreign word," one that requires explanation; later extended to the explanation itself, from Greek glōssa (Ionic), glōtta (Attic) "language, a tongue; word of mouth, hearsay," also "obscure or foreign word, language," also "mouthpiece," literally "the tongue" (as the organ of speech), from PIE *glogh- "thorn, point, that which is projected" (source also of Old Church Slavonic glogu "thorn," Greek glokhis "barb of an arrow").

 Glosses were common in the Middle
######## a5c4c0f052441091
URL: https://www.etymonline.com/word/echolalia
FETCHED: 2026-09-06T22:42:30Z
STATUS: 200
TITLE: Echolalia - Etymology, Origin & Meaning

Echolalia - Etymology, Origin & Meaning 

 Search 
 Log in 

 Columns 
 Forum 
 Apps 
 Premium 

 Log in 

 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 Origin and history of echolalia 

 echolalia (n.) 

 "meaningless repetition of words and phrases," 1876, from German (von Romberg, 1865), from Greek ēkhō (see echo (n.)) + lalia "talk, prattle, a speaking," from lalein "to speak, prattle," of echoic origin.
 also from 1876 

 Entries linking to echolalia 

 echo (n.) 

 mid-14c., "sound repeated by reflection," from Latin echo , from Greek ēkhō , personified in classical mythology as a mountain nymph who pined for love of Narcissus until nothing remained but her voice. It is from or related to ēkhē "sound," ēkhein "to resound," from extended form of PIE root *(s)wagh- "to resound" (source also of Sanskrit vagnuh "sound," Latin vagire "to cry," Old English swogan "to resound"). Related: Echoes . Also see echo chamber .

 Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 More to explore

 repetition 

 early 15c., repeticioun, "act of saying over again," from Old French repetition and directly from Latin r
```


## [2026-09-06T22:42:45.463Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in c8ccc09bec9e2510 9fa6b63538a8e178 cd6d8191764528f2 2d0fba3489465d87; do echo \"######## $f\"; sed -n '1,6p' $f.txt; grep -n -i -A6 \"Etymology\" $f.txt | head -40; echo; done"
}
```


### [2026-09-06T22:42:47.085Z] TOOL RESULT

```
######## c8ccc09bec9e2510
URL: https://en.wiktionary.org/wiki/%CE%BB%CE%AC%CE%B4%CE%B1%CE%BD%CE%BF%CE%BD
FETCHED: 2026-09-06T22:42:33Z
STATUS: 200
TITLE: λάδανον - Wiktionary, the free dictionary

λάδανον - Wiktionary, the free dictionary 

######## 9fa6b63538a8e178
URL: https://en.wiktionary.org/wiki/%CE%BB%CF%89%CF%84%CF%8C%CF%82
FETCHED: 2026-09-06T22:42:33Z
STATUS: 200
TITLE: λωτός - Wiktionary, the free dictionary

λωτός - Wiktionary, the free dictionary 
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Noun 
--
88: Etymology 
89-
90- 2.2 
91- Pronunciation 
92-
93- 2.3 
94- Noun 
--
174: Etymology
175- [ edit ] 
176-
177- Probably from a Semitic source common to Hebrew לוֹט ( lōṭ , “ myrrh ” , literally “ covering, envelope ” ) .
178-
179- Pronunciation
180- [ edit ] 
--
325: Etymology
326- [ edit ] 
327-
328- From Ancient Greek λωτός ( lōtós ) .
329-
330- Pronunciation
331- [ edit ] 

######## cd6d8191764528f2
URL: https://en.wiktionary.org/wiki/%CE%BB%CE%B1%CE%BB%CE%AD%CF%89
FETCHED: 2026-09-06T22:42:34Z
STATUS: 200
TITLE: λαλέω - Wiktionary, the free dictionary

λαλέω - Wiktionary, the free dictionary 
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Verb 
--
151: Etymology
152- [ edit ] 
153-
154- Uncertain. Perhaps a reduplicated form of Proto-Indo-European *leh₂- , with cognates including Latin lallō , Lithuanian laluoti , German lallen , English loll , and Welsh llolian . Could also simply be onomatopoeic. Beekes notes that the suffix -έω ( -éō ) is also present in other verbs pertaining to sound, such as κελαδέω ( keladéō ) and βομβέω ( bombéō ) .
155-
156- Pronunciation
157- [ edit ] 

######## 2d0fba3489465d87
URL: https://en.wiktionary.org/wiki/lamentum
FETCHED: 2026-09-06T22:42:34Z
STATUS: 200
TITLE: lamentum - Wiktionary, the free dictionary

lamentum - Wiktionary, the free dictionary 
62: Etymology 
63-
64- 1.2 
65- Noun 
66-
67- 1.2.1 
68- Declension 
--
148: Etymology
149- [ edit ] 
150-
151- From Proto-Italic *lāmentom , from Proto-Indo-European *leh₂- (expressive root։ to howl, cry, bark). [ 1 ] Cognate with lātrō , Ancient Greek λῆρος ( lêros ) , λάλος ( lálos ) , λάσκω ( láskō ) .
152-
153- Noun
154- [ edit ]
```


## [2026-09-06T22:42:56.056Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"### ladanon\"; grep -n -i \"ladanon\\|λάδανον\\|Semitic\\|Arabic\\|Persian\" c8ccc09bec9e2510.txt | head -20; wc -c c8ccc09bec9e2510.txt; echo \"### fa layidan\"; grep -n -i \"etymology\\|Parthian\\|Middle Persian\\|does not yet\" -A4 f9fd43eca6254598.txt | head -30; echo \"### fa ladan\"; grep -n -i \"etymology\" -A6 9a668ec268c2acf0.txt | head -30; echo \"### labe\"; grep -n -i \"etymology\" -A8 544a3cce37d69654.txt | head -40"
}
```


### [2026-09-06T22:42:56.143Z] TOOL RESULT

```
### ladanon
4:TITLE: λάδανον - Wiktionary, the free dictionary
6:λάδανον - Wiktionary, the free dictionary 
72: λάδανον 
228: Retrieved from " https://en.wiktionary.org/w/index.php?title=λάδανον&oldid=89104243 "
270: λάδανον 
3852 c8ccc09bec9e2510.txt
### fa layidan
### fa ladan
65: Etymology 
66-
67- 1.3 
68- Pronunciation 
69-
70- 1.4 
71- Noun 
--
149: Etymology
150- [ edit ] 
151-
152- Borrowed from Ancient Greek λᾱ́δᾰνον ( lā́dănon ) .
153-
154- Pronunciation
155- [ edit ] 
--
253: Arabic entries with etymology texts 
254- Pages using etymon with no ID 
255- Pages with entries 
256- Pages with 1 entry 
257-
258- This page was last edited on 10 June 2026, at 08:29.
259-
### labe
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Noun 
69-
70- Toggle the table of contents 
--
137: Etymology
138- [ edit ] 
139-
140- Inherited from Middle Persian [Book Pahlavi needed] ( lʾpk' /⁠lābag⁠/ ) . Compare Northern Kurdish lava .
141-
142- Pronunciation
143- [ edit ] 
144-
145- ( Classical Persian ) IPA ( key ) : /laː.ˈba/
```


## [2026-09-06T22:43:03.194Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"=== ladan file\"; sed -n '60,175p' 9a668ec268c2acf0.txt | tr -s ' \\n' ' \\n' | head -60; echo; echo \"=== layidan file\"; sed -n '1,60p' f9fd43eca6254598.txt | tr -s ' \\n' ' \\n' | head -30"
}
```


### [2026-09-06T22:43:03.242Z] TOOL RESULT

```
=== ladan file

 1.1 
 Alternative forms 
 1.2 
 Etymology 
 1.3 
 Pronunciation 
 1.4 
 Noun 
 1.4.1 
 Declension 
 1.5 
 References 
 Toggle the table of contents 
 لادن 
 3 languages 
 فارسی 
 Magyar 
 Русский 
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
 Arabic
 [ edit ] 
 Alternative forms
 [ edit ] 
 لَاذَن ( lāḏan ) , لَدَان ( ladān ) , لَذَان ( laḏān ) 
 Etymology
 [ edit ] 
 Borrowed from Ancient Greek λᾱ́δᾰνον ( lā́dănon ) .
 Pronunciation
 [ edit ] 

=== layidan file
URL: https://en.wiktionary.org/wiki/%D9%84%D8%A7%DB%8C%DB%8C%D8%AF%D9%86
FETCHED: 2026-09-06T22:42:35Z
STATUS: -1
TITLE: 
FETCH FAILED: HTTP Error 404: Not Found
```


## [2026-09-06T22:43:18.937Z] TOOL CALL #47: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/%CE%BB%CE%AE%CE%B4%CE%B1%CE%BD%CE%BF%CE%BD\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/leh%E2%82%82-\" \\\n \"https://www.ahdictionary.com/word/search.html?q=ladanum\" \\\n \"https://www.ahdictionary.com/word/search.html?q=lotus\" \\\n \"https://en.wiktionary.org/wiki/labdanum\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 300, roots La / Ladunu: Greek ledanon, PIE *leh2-, AHD ladanum/lotus\" ; done 2>&1 | tail"
}
```


### [2026-09-06T22:43:24.413Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/63879c739f93afd7.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1bf33d2aa426ebba.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b640890d56b2b45f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/70740dc8151632f0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5d5cc3d952e94060.txt
```


## [2026-09-06T22:43:27.981Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 63879c739f93afd7 1bf33d2aa426ebba 5d5cc3d952e94060; do echo \"######## $f\"; grep -n -i -A8 \"^ Etymology$\" $f.txt | head -30; done; echo \"######## AHD ladanum\"; grep -n -i \"ladanum\\|Semitic\\|Akkadian\" b640890d56b2b45f.txt | head -10; echo \"######## AHD lotus\"; grep -n -i \"lotus\\|Semitic\\|Hebrew\" 70740dc8151632f0.txt | head -10"
}
```


### [2026-09-06T22:43:29.785Z] TOOL RESULT

```
######## 63879c739f93afd7
156: Etymology
157- [ edit ] 
158-
159- A loan, originally from Semitic . Compare Akkadian 𒆷𒁷𒉡 ( ladinnu ) .
160-
161- Pronunciation
162- [ edit ] 
163-
164- IPA ( key ) : /lɛ̌ː.da.non/ → /ˈli.ða.non/ → /ˈli.ða.non/ 
######## 1bf33d2aa426ebba
######## 5d5cc3d952e94060
157: Etymology
158- [ edit ] 
159-
160- From Latin lādanum , from Ancient Greek λήδανον ( lḗdanon , “ gum ” ) , from λήδον ( lḗdon , “ rockrose ” ) , from a Semitic language; compare Akkadian 𒆷𒁷𒉡 ( ladinnu ) .
161-
162- Noun
163- [ edit ] 
164-
165- labdanum ( usually uncountable , plural labdanums ) 
######## AHD ladanum
1:URL: https://www.ahdictionary.com/word/search.html?q=ladanum
4:TITLE: American Heritage Dictionary Entry: ladanum
6:American Heritage Dictionary Entry: ladanum 
50: Indo-European & Semitic Roots Appendices
53: Semitic Roots 
######## AHD lotus
1:URL: https://www.ahdictionary.com/word/search.html?q=lotus
4:TITLE: American Heritage Dictionary Entry: lotus
6:American Heritage Dictionary Entry: lotus 
48: c. Any of several water lilies, especially Nymphaea caerula or N. lotus. 
49: d. An artistic representation of the flower or bud of any of various lotuses or similar plants.
51: 2. Any of several leguminous plants of the genus Lotus. 
52: 3. Greek Mythology a. A small Mediterranean tree or shrub whose fruit was eaten by the lotus-eaters.
57: lotus sacred lotus 
62: Indo-European & Semitic Roots Appendices
65: Semitic Roots
```


## [2026-09-06T22:43:33.755Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '40,60p' b640890d56b2b45f.txt | tr -s ' '; echo \"==== lotus\"; sed -n '44,62p' 70740dc8151632f0.txt | tr -s ' '"
}
```


### [2026-09-06T22:43:33.813Z] TOOL RESULT

```
 lad·a·num (l ă d  n- ə m) 
 Share: 

 Tweet 

 n. Variant of labdanum .

 The American Heritage® Dictionary of the English Language, Fifth Edition copyright ©2022 by HarperCollins Publishers. All rights reserved.

 Indo-European & Semitic Roots Appendices
 Thousands of entries in the dictionary include etymologies that trace their origins back to reconstructed proto-languages. You can obtain more information about these forms in our online appendices:
 Indo-European Roots 
 Semitic Roots 
 The Indo-European appendix covers nearly half of the Indo-European roots that have left their mark on English words. A more complete treatment of Indo-European roots and the English words derived from them is available in our Dictionary of Indo-European Roots .

 American Heritage Dictionary Products
 The American Heritage Dictionary, 5th Edition

 The American Heritage Dictionary of Idioms

==== lotus
 Tweet 

 n. 1. a. Either of two aquatic plants, Nelumbo nucifera of Asia and Australia with pink flowers, or N. lutea of eastern North America with pale yellow flowers, or their cultivated varieties, having large round leaves, fragrant many-petaled flowers, a round perforated seedpod, and fleshy rhizomes.
 b. The edible seed, leaf, or rhizome of either of these plants.
 c. Any of several water lilies, especially Nymphaea caerula or N. lotus. 
 d. An artistic representation of the flower or bud of any of various lotuses or similar plants.

 2. Any of several leguminous plants of the genus Lotus. 
 3. Greek Mythology a. A small Mediterranean tree or shrub whose fruit was eaten by the lotus-eaters.
 b. The fruit of this plant.

 [Latin l ō tus , name of several plants, from Greek l ō tos .]
 (click for a larger image) 
 lotus sacred lotus 
 Nelumbo nucifera 

 The American Heritage® Dictionary of the English Language, Fifth Edition copyright ©2022 by HarperCollins Publishers. All rights reserved.

 Indo-European & Semitic Roots Appendices
```


## [2026-09-06T22:43:42.911Z] TOOL CALL #50: Bash

```json
{
 "command": "python3 tools/fetch_source.py \"https://www.ahdictionary.com/word/search.html?q=labdanum\" --note \"page 300, root Ladunu: AHD etymology of labdanum/ladanum\" >/dev/null 2>&1; f=$(python3 -c \"import hashlib;print(hashlib.sha1('https://www.ahdictionary.com/word/search.html?q=labdanum'.encode()).hexdigest()[:16])\"); echo $f; sed -n '40,60p' data/verification/sources/web/$f.txt | tr -s ' '"
}
```


## [2026-09-06T22:43:44.182Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== WLD Bd2 lamentum/lallen\"; grep -n \"lamentum\\|lāmentum\" incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt | head -10"
}
```


### [2026-09-06T22:43:46.260Z] TOOL RESULT

```
efd093b76e0b5124

 lab·da·num (lăb  də-nəm) also lad·a·num (lăd  n-əm) 
 Share: 

 Tweet 

 n. A resin of certain Mediterranean rockroses of the genus Cistus, yielding a fragrant essential oil used in flavorings and perfumes. 

 [Middle English, from Medieval Latin lapdanum, labdanum , alteration of Latin lādanum , from Greek lēdanon, lādanon , from lēdon, *lādon , rockrose, of Semitic origin; akin to Old South Arabian ldn , probably a kind of rockrose, and Akkadian ladinnu, ladunu , labdanum; see ldn in the Appendix of Semitic roots .] 

 The American Heritage® Dictionary of the English Language, Fifth Edition copyright ©2022 by HarperCollins Publishers. All rights reserved.

 Indo-European & Semitic Roots Appendices
 Thousands of entries in the dictionary include etymologies that trace their origins back to reconstructed proto-languages. You can obtain more information about these forms in our online appendices:
 Indo-European Roots 
 Semitic Roots 
 The Indo-European appendix covers nearly half of the Indo-European roots that have left their mark on English words. A more complete treatment of Indo-European roots and the English words derived from them is available in our Dictionary of Indo-European Roots .

 American Heritage Dictionary Products
 The American Heritage Dictionary, 5th Edition
```


### [2026-09-06T22:43:46.302Z] TOOL RESULT

```
=== WLD Bd2 lamentum/lallen
```


## [2026-09-06T22:43:57.427Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ndata=open('IEC.txt',encoding='utf-8',errors='replace').read()\nlines=data.split('\\n')\ni=[n for n,l in enumerate(lines) if l.startswith('laiō')]\nprint('laio lines',i)\nfor ln in i:\n    off=sum(len(l)+1 for l in lines[:ln])\n    leaf=data.count('\\f',0,off)\n    print('leaf',leaf,'-> printed p ~',2*(leaf-15))\nEOF\necho \"=== WLD grep\"; grep -n -i \"lallen\\|lamentum\" incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt WLD_band3.txt incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt 2>/dev/null | head -10"
}
```


### [2026-09-06T22:43:59.114Z] TOOL RESULT

```
laio lines []
=== WLD grep
WLD_band3.txt:2011:Ewirnen wial, 665. erinan age. O68. kite ‘nd. oon, CUNrCTis Ape. iis. bufef mbel. U7). quira, quirmd ahd. G85, kuteln mhd. S60, iapel mond. 45. cult ahd. @72, ein fries. 669, kutle mnd. 560, quiat abd. Sat ea hull abd. BGO. bafen a cis. kdize mill. 635. kuistern fries, 669, hits mui. 650, gquifhean as. 6046. kuzsildén ahd. 553, quill ahi, 660, O71, quibs ,,Bebemons” mond. quoden ahd. 500, 671 G74. | ew jem ue, Of nd. Gil. caf ops. 561, quidderen nil. O73 cocgel ope. SOS. quarer engl. 74 eyry aps. (7 cuarin ages. 671 cyrme! ages. (i) quack, quacken 458 cyepan og. (45 quackalm nll, 671 cyt age qualia all. (1M), cula aga. Go ualhit as, OD. cvlwer age, wale nlul. B91. la mbhd, 350" qual . 690, la gualater mn. “01. fam mci. 156, quiln as. G81. labe-schwete. 402". nminion ages. (4k. labhe nhd. cial. S54* and. 874, labém oli, 442* see Ehe: 710. fade, foden mh. 352%. quartar abil. Si), dén ahi. 4" quers mbhd. 747. “lien ahd. 405* HG. ldunen. bair. 430 mbhd. 44. laffa ahd. 428". qua? ahd. 605, laffated hell, 432%, en nh, God. Iaffan abd. 354". cuted age. G00. -uffea mihi, 432*, <quchben mid, O74, Laffe nhd. 432". a ee mind. 660. rob. 42)". quik, quik ahd. 669 tee SOR reer SBF, ' : wea" ° owen . 71, loka sa 436". Quecke nhd. 6g, IchAa, laocha oll. 423* an abd. G9), lohian ,,Tnoh” ahd. 718*, quellan abil. G91. lahhéa, K ' queman ahd. 675. lake oli. 331" quena abd. 851. lak mnd. 712* cocods, clwjudw aga. G60. fake mnd. 422* queran ahd. 687. lach ml, querdar ahd. 653. liche ..Kerbe“ mud. 713* eee ee ahd. 644. lallen nha. 376°. queisen ea pics 48 aba, 434". =! Tr | = cuidu ngs. 672. lam aha. 154. ewtd, cteida age. 56D lompen mhd. 407". quicken nbd. 455. der mh. 382%, (437%),
incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt:6758:bata^ vielleicht onomatopoetisch fiir lappisches Lallen oder Erstaunen. 
incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt:6803:stottere^', sloven. Idbam, hdhdti „unverstan(ilich reden“, bdhljdfi „lallen“, 
incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt:6818:melnd, lallend", balbiitio „stamnile", ai. balbfithd-h Name feigentlich ,,Stamm- 
incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt:24435:Redupl. lal(l)d-: ai. lalallct „Laut eines Lallenden“, gr. Xdlog „ge- 
incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt:24438:lalh(S „das Trallern der Amme“, lit. laliUi „lallen“, russ. Jala „Schwatzer“ 
incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt:24439:(u. dgl. 8. Bemeker 688), nhd. lallen (anord, laJla „wie ein Kind beim Gehn 
incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt:27832:„stamineln, schwatzen, lallen“, klr. iepetdty „lallen, plarren“, abg. lopotiv^
```


## [2026-09-06T22:44:05.474Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '24425,24450p' incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt"
}
```


### [2026-09-06T22:44:05.517Z] TOOL RESULT

```
Zd f., pi. lor „Charadrius“ (Liden aaO. m. Lit., Falk-Torp 391, 1480; Gdf. 
aber unsicher, vielleicht aus Zdw?-, loiv-^ s. Wiedemann BB. 28, 54 in Be- 
richtigung von Bugge PBrB. 24, 58 : s. *Zc«- Schallwz.) : vielleicht anord. 
loynr „Meertaucher, ein Yogel mit sehr starkem und auffalligen Geschrei“, 
Ygl. anord. lomr „Geschrei, Wehklage‘' (oder der Yogelname zu schwed. 
lomma ,,schwerfMig und langsam gehn'" (s. Liden aaO.; s. auch Pick III ^ 
354 = Falk-Torp 634, 1507 unter lema^n ,,Lemming“ und 635, 1507 unter 
lerJee „Lerche''). — Ygl. Brugmann MU. I 39. Hubschmann Yoc. 106, Pers- 
son Wzerw. 13, 116, 198, Pick I ^ 119, 532, II* 249. 

Redupl. lal(l)d-: ai. lalallct „Laut eines Lallenden“, gr. Xdlog „ge- 
schwatzig'^, Xakia „Geschwatz“, XaXeco „sch\vatze“, kakay/j „leichtes Ge- 
murmeP, kakdCco, kakayeco ,,schwatze“, lat. lallo, -are „in den Schlaf singenA 
lalh(S „das Trallern der Amme“, lit. laliUi „lallen“, russ. Jala „Schwatzer“ 
(u. dgl. 8. Bemeker 688), nhd. lallen (anord, laJla „wie ein Kind beim Gehn 
wanken“ in etwas anderer Bedeutungswendung), alter dan. lalle auch „in 
Schlaf lullen*'. 

Ahnliche Lallworte fiir „in den Schlaf singen, einlullen, einwiegen, 
8chaukeln“ sind z. B. (vgl. Yf. LEWb.^ 439, Berneker 699f., 759 m. Lit.) 
russ. IJidjii „eia popeia!^ Ijiihlca „Wiege'', serb. ljuljati „einwiegenA lett. 
hdut „Yerwohnen‘*, nhd. hdlen, engl. lull „in den Schlaf singen‘‘, ai. lolntl 
„bewegt sich hin und her‘^, luUta-- ..bewegt, flatternd“, lat. lolium „Lolch, 
SchwindelhafeP^ (betaubende Pftanze); serb. leTijaii, leJjati „wiegen,
```


## [2026-09-06T22:44:06.976Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ndata=open('IEC.txt',encoding='utf-8',errors='replace').read()\nlines=data.split('\\n')\nfor n,l in enumerate(lines):\n    if l.startswith('laið') or l.startswith('láiskð'):\n        off=sum(len(x)+1 for x in lines[:n])\n        leaf=data.count('\\f',0,off)\n        print(n+1, l[:60],'| leaf',leaf,'-> p ~',2*(leaf-15),2*(leaf-15)+1)\nEOF"
}
```


### [2026-09-06T22:44:08.974Z] TOOL RESULT

```
9426 laið ‘roar, bellow, bark’. WP II, 377 Skt. rāyāmi, id.; Per. | leaf 371 -> p ~ 712 713
9436 láiskð (lasK-) (variant of laio, q.v.) Hitt. sar-lesk- ‘cry  | leaf 372 -> p ~ 714 715
```


## [2026-09-06T22:44:26.593Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ndata=open('IEC.txt',encoding='utf-8',errors='replace').read()\nleaves=data.split('\\f')\nimport re\nfor i in (369,370,371):\n    t=leaves[i]\n    nums=re.findall(r'(?m)^\\s*(\\d{3})\\s*$',t)\n    print(i,'page-like lines:',nums,'| first 60:',t[:60].replace('\\n',' '))\nEOF"
}
```


### [2026-09-06T22:44:28.164Z] TOOL RESULT

```
369 page-like lines: ['656'] | first 60: tv. suns, gs suna, gp sunu. Variant: Skt. Sunih; Av. sünis; 
370 page-like lines: ['658'] | first 60:  consistency in the evolu- tion of what is here represented 
371 page-like lines: ['659', '660'] | first 60: atsche “slut”, and Icel. laska, v. *damage'; laski 'flaw") l
```


## [2026-09-06T22:44:38.717Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in FRS_pages.txt FSF_pages.txt RCH.txt GPL.txt SBK.txt; do echo \"--- $f\"; grep -n \"لاییدن\\|لادن\\|لابیدن\" $f 2>/dev/null | head -3; done; echo \"=== RCH latin\"; grep -n -i \"ladan\\|layidan\" RCH.txt | head -5"
}
```


### [2026-09-06T22:44:40.366Z] TOOL RESULT

```
--- FRS_pages.txt
15667:                               ‫لادن "‬
15674:      ‫عبر دارد لادن‬     ‫گونة‬           ‫باشد چون او‬   ‫ازره صورت‬
15690: ‫‪ - ۲‬چ ؛ لادن جنسی است ازمجون برمتال دوشاب و گونه عبر دارد سیاه » س؛‬
--- FSF_pages.txt
3942:                   ‫لادن» مشک بید (برهان)‪:‬‬
3953: ‫سرانجمن سرو سایه فکن‬                              ‫در نسخه ‪۶‬بجای بان لادن‪:‬؛جولادن کجاوفور و‪»...‬‬
--- RCH.txt
--- GPL.txt
--- SBK.txt
=== RCH latin
9022:Resolving  a   question  of  law,  or  a   case  of  conscience. r\ii\  ujta  (from  ufladan)^  Falling.
9072:p   ttftadan^  (for  ufladan)  To  fall.  To  happen.
16231:U   bar  $ar.ipa  hladan,  To  stand  on  the  point  of  the
73966:A^fjJ  ladanat  (from  (^^),  Being  supple,  limber  (spear).
```


## [2026-09-06T22:44:41.022Z] TOOL CALL #57: Bash

```json
{
 "command": "for u in \"https://abadis.ir/fatofa/%D9%84%D8%A7%DB%8C%DB%8C%D8%AF%D9%86/\" \"https://abadis.ir/fatofa/%D9%84%D8%A7%D8%AF%D9%86/\"; do python3 tools/fetch_source.py \"$u\" --note \"page 300: Mo'in/Dehkhoda entry for لاییدن / لادن\"; done 2>&1 | tail -4"
}
```


### [2026-09-06T22:44:45.246Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/6e2c3eb3044ef8b7.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/91c1a2366ef084ec.txt
```


## [2026-09-06T22:44:48.355Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 6e2c3eb3044ef8b7 91c1a2366ef084ec; do echo \"#### $f\"; sed -n '1,5p' $f.txt; grep -n \"معین\\|دهخدا\\|لاییدن\\|لادن\" $f.txt | head -12; done"
}
```


### [2026-09-06T22:44:50.137Z] TOOL RESULT

```
#### 6e2c3eb3044ef8b7
URL: https://abadis.ir/fatofa/%D9%84%D8%A7%DB%8C%DB%8C%D8%AF%D9%86/
FETCHED: 2026-09-06T22:44:43Z
STATUS: 200
TITLE: لاییدن - معنی در دیکشنری آبادیس

4:TITLE: لاییدن - معنی در دیکشنری آبادیس
6:لاییدن - معنی در دیکشنری آبادیس 
10: لاییدن
16: لغت نامه دهخدا
18: لاییدن. [ دَ ] ( مص )لائیدن. نالیدن. ( برهان ). عوعو کردن سگ : 
38: فرهنگ معین
51: لاییدن چند معنا دارد. ۱. گفتن ۲. نالیدن ۳. عوعو و پاس سگ و ۴. هرزه گویی و چرند درایی ( چرت و پرت گفتن ) 
69: آبادیس از سال 1385 فعالیت خود را در زمینه فن آوری اطلاعات آغاز کرد. نخستین پروژه آبادیس، سایت دیکشنری آبادیس بود. دیکشنری آنلاین آبادیس از ابتدا تاکنون تغییرات بسیاری کرده و ویژگی های مختلفی به آن اضافه شده است. آبادیس افزونه ای کاربردی برای مرورگرهای فایرفاکس و کروم و اپلیکیشن موبایل طراحی کرده است که میتوانید از لینک های بالا دانلود کنید. دیکشنری آبادیس شامل بخش هایی نظیر دیکشنری به زبان های مختلف از جمله انگلیسی، فارسی، عربی و همچنین بیست دیکشنری تخصصی با تلفظ انگلیسی و آمریکایی، ترجمه مخفف و کلمات اختصاری، مترجم آنلاین متن، لغتنامه دهخدا، فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راهنمای انتخاب اسم و ... می باشد. 
#### 91c1a2366ef084ec
URL: https://abadis.ir/fatofa/%D9%84%D8%A7%D8%AF%D9%86/
FETCHED: 2026-09-06T22:44:45Z
STATUS: 200
TITLE: لادن - معنی در دیکشنری آبادیس

4:TITLE: لادن - معنی در دیکشنری آبادیس
6:لادن - معنی در دیکشنری آبادیس 
10: لادن
19: اسم: لادن (دختر) (فارسی، یونانی) (طبیعت، گل) (تلفظ: lādan) (فارسی: لادن) (انگلیسی: ladan) 
23: لغت نامه دهخدا
25: لادن. [ دِ ] ( اِخ ) یکی از سه شعبه مشرقی رود گنگ.( تحقیق ماللهند ص 131 ) .
26: لادن. [ دَ ] ( اِ ) لاذَن. عنبر عسلی. جنسی بود از معجونات و عطربرسان دوشاب. سیاه و خوشبوی بود ( نسخه ای از لغت نامه اسدی ). جنسی است از معجون بر مثال دوشاب و گونه ای عنبردار رسیده. ( نسخه اسدی ). جنسی است از معجونهای خوشبو برنگ سیاه. ( حاشیه فرهنگ اسدی نخجوانی ). نوعی از عطر و بوی خوش بود و بر شکل دوشاب بسته باشد. ( صحاح الفرس ). نوعی از مشمومات است یعنی بوی کردنی و آن مانند دوشاب سیاه باشد و آن را عنبر عسلی گویند و در داروها بکار برند و آن از زمین ریگستان حاصل می شود به این طریق که گیاهی که از زمین آن بروید به لادن آغشته باشد و بز آن گیاه را دوست می دارد و بهنگام چرا ریش و موی بز بدان آلوده می شود بعد از آن جدا می سازند و آنچه بر ریش بز آلوده باشد بهتر از آن است که بر موی ران و اعضای دیگر. گویند اگر در زیر دامن زنی که بچه مرده در شکم داشته باشد بخور کنند بچه مرده از مشیمه بیرون آید. ( برهان ). لادن معروف و از مشمومات ( و از جمله ادهان است ). ( نزهةالقلوب ). جنسی است از معجونهای خوشبوی به رنگ سیاه چون عنبر و آنچه بدان ماند. ( اوبهی ). صاحب ذخیره خوارزمشاهی لادن را از عطرها شمارد و گوید گرم است به درجه دویم و خشک به درجه اول لطیف و محلل و منضج و علت های رحم را سودمند بود و موی سیاه و قوی گرداند و ریش را نافع بود و برویاند. ابن سینادر قانون آرد: هورطوبة یتعلق بشعر المعزّی الراعیة و لحاها. ( قانون چ تهران ج 1 ص 203 ). ابوریحان در صیدله گوید عربی است و به فارسی او را لادنه گویند و به هندی تبتر گویند. جالینوس گوید نباتی است که از او لادن سازند و او را نبات لادن گویند و گفته است لغت صحیح رومی اوقیستوس بود. یحیی و حسکی گویند لادن انواع است و جمله او را از شام نقل کنند و آنچه از جزیره قبرس حاصل شود نیکوتر بود نوعی از او سیاه رنگ بود به لون قار. بوی او به بوی عنبر ماند اوریباسیوس گوید نیکوترین آن است که رنگ اوبه سبزی مایل بود و خوشبوی باشد و چون به آب اندازند بگدازد و به دست چسبد. ریگ و خاک جزو او نباشد و به راتینج مشابه بود و قبرسی را اکثر این صفات بود. «جالینوس » در میامر آورده که اطبا را اتفاق است که لادن از ریش بز گشن متولد شود. روفس گوید نوعی از لادن در زمین عرب و حبشه و سند و هند از موی زنخ بز متکون شود از ماده و نر و اختصاص به گشن نکرده و گویند لذتی که در طعم اوست به آن سبب است که برگ نبات قیسوس را لذتی هست و بز را به آن الفت تمام باشد و در وقت چرا کردن دهنیتی که در او است بر موی زنخ او جمع شود پس گوید نباتی است که او را قسطس گویند و بز را بااو الفتی تمام باشد و چون بخورد شیره آن نبات در موی او جمع آید لادن آن بود. «ص » و «ارجانی » گوید. «گرم است در دوم و خشک است در اول لطیف است و اندک قبضی در او باشد با اخلاط غلیظ بیامیزد و تحلیل کند اعلال رحم را مفید است مشیمه بیرون آورد و موی بر اعضا برویاند و درشت کند، و بیخ آن محکم کند و از ریختن نگاهدارد و مسامات موی را تسدید کند. ( ترجمه صیدنه ابوریحان ). حکیم مؤمن گوید رطوبتی است که از درخت کوهی حاصل می شود بقدر درخت انار و شبیه به درخت دبق و برگش عریض و به هم متصل و رقیق و صلب و گلش مایل به سرخی و ثمرش مانند زیتون و در جوف آن دانه سیاه باریکی و رطوبت غلیظی که از ساق و برگ او جمع کنند. و بهترین اقسام آن را لادن عنبری نامند و هر چه از آن رطوبت بر موی بز و گوسفند در حین چریدن آن نبات چسبد و از آن جدا کنند زبون تر از قسم اول و هرچه بر سُم مراعی چسبد و با خاک و ریگ آمیخته باشد زبون تر از همه است و بعضی تصریح کرده اند که رطوبت مذکور از قسوس که نوعی از لبلاب است بر موی مراعی می چسبد و بهترین او نرم و خوشبوی سیاه مایل به سرخی و سبزی است در دوم گرم و در اول خشک و لطیف و جاذب و با قوه قابضه و منضج قوی و محلل و مفتح دهن رگها و مدر بول و حیض و عرق و شیر و مخرج جنین و مشیمه و مقوی معده و رافع فواق و دردهای بارده و با شراب قابض طبع و طلای او جهت دردسر و صلابة معده و جگر و التیام زخمهای کهنه و با شراب جهت آثار قروح و آبله و فرزجه او جهت صلابت رحم و اختناق و احتباس حیض و با روغن گل که بر یافوخ اطفال طلا کنند جهت تقویت آن و رفع غثیان و سیلان آب دهان و با پیه خوک و پیه گاو جهت ورم مقعد و درد آن و حقنه او و با روغن گل جهت سحج بارد و طلای او با روغن گل جهت سوختگی آتش و با روغن مورد جهت تقویت موی و منع ریختن آن و بخور او جهت گریزانیدن هوام مؤثر و چون زن بعد از بول کردن به آن بخور کند پس در حال بازبول آید آن زن قابل حمل خواهد بود و الا فلا و مضرسفل و آشامیدن او موجب کرب و مصلحش سنبل رومی و قدر شربتش تا یکدرهم است و روغن لادن که یک وقیه او را در یک رطل روغن زیتون و کنجد حل کرده روز دیگر بر آتش خاکستر گذارند که قریب به سدس آن روغن بسوزد جهت برودت اعضا و تقویت معده و زکام رطوبی و سیاه کردن موی و تقویت آن بغایت مفید است. ( تحفه حکیم مؤمن ). صاحب اختیارات بدیعی گوید: نیکوترین آن چرب خوشبوی بود که لون آن به زردی زند و هیچ رمل در وی نبود و در روغن حل شود و ثفل نداشته باشد و طبیعت آن گرم بود در آخردرجه اول و گویند در آخر درجه دوم و وی تر بود و گویند سرد و قابض بود و این قول ضعیف است و گویند خشک بود و جوهر وی بغایت لطیف بود و در وی قبضی اندک بود منضج رطوبات غلیظه بود و قوت بن موی بدهد و برویاند و به روغن مورد موی را نگاهدارد و اما بر داءالثعلب و داءالحیة ممکن نیست و معالجه آن داروهای دیگر بود که تحلیل بسیار در ایشان بود و اگر لادن در زیر دامن بخور کنند بچه مرده از مشیمه بیرون آورد و چون با شراب بیاشامند شکم ببندد و بول براند و بلغم پاک کند و مقدار مأخوذ از وی تا نیم مثقال بود و ملین صلابت معده بود و قوت آبستنان بدهد چون ضعف و سردی در ایشان بود و اگر در روغن گل حل کنند و در گوش چکاننددرد آن زایل کند و اگر با روغن بابونه یا شبت حل کنند بر هر وجعی که بود بمالند نافع بود و اگر در روغن گل طلا کنند یا بر یافوخ کودکان یعنی میان سر، که به شیرازی جان دانه گویند نزله و سرفه را نافع بود و چون با پیه خوک حل کنند و بر ورم مقعد نهند درد ساکن کند و چون با گل حل کرده حقنه کنند سحج را نافع بود وگویند مضر بود بسفل و مصلح آن سنبل الطیب بود. ( اختیارات بدیعی ). صمغی است که از گیاه سستوس کریتی گرفته می شود و قدیمیان از ریش بزهائی که در میان این علف چرا می کردند این صمغ را می گرفتند و فعلاً از لباس اشخاصی که از میان علفها می گذرند و یا از کفشهای ایشان می گیرند. خلاصه لادن در قدیم الایام در طب بسیار استعمال میشد لکن در این اواخر اعتنائی بدان نکردند. ( قاموس کتاب مقدس ) : بیشتر بخوانید ... 
30: ناحیه ایست از نواحی خاوری زاهدان واقع در جنوب باختر میرجاوه . شاید نام [ لادن ] در شاهنامه اشاره باین محل باشد .
32:( اسم ) ۱- نام صمغی است خوشبوی که از گیاه عشقه حاصل میشود و قاعده آور است . بهمین جهت در طب قدیم آنرا در زیر دامن زنی که قاعده اش بند آمده بود دود میکردند زیرا بخارات حاصل از آن نیز همین خاصیت را دارند . منظور از لادنی که در کتب قدیم و اشعار شعرا بعنوان صمغ خوشبوی آورده شده همین لادن است لاذنه لاذن : نریزد از درخت ارس کافور نخیزد از میان لاد لادن . ( منوچهری . د . چا. ۲ ) ۶۶ : ۲- نام صمغی که بویی مطبوع دارد و از گیاه قستوس حاصل میشود . بهمین جهت گاهی گیاه قستوس را هم بنام لادن و یا شجره اللادن خوانند . غالبا صمغ قستوس را لادن عنبری مینامند . ۳- از گونه ای کاج بنام پیسه اکسلسا صمغی خوشبوی حاصل میگردد که لادن نامیده میشود . ۴- گیاهی از تیر. شمعدانی ها که دارای ساق. پیچنده است . برگهایش نسبه پهن و گلهایش رنگ نارنجی خاصی دارند . انساج این گیاه بویی تند ومطبوع شبیه بوی تره تیزک دارند . اصل این گیاه از آمریکای جنوبی خصوصا کشور پرو میباشد و از آنجا به نقاط دیگر برده شده است در آمریکای جنوبی بشکل یک گیاه پایا میزید ولی در کشورهای دیگر از جمله ایران گیاه یکسال. زینتی بشمار میرود . در حدود ۳٠ گونه از این گیاه شناخته شده است گل لادن ابوخنجر طرطور الباشا .
35: فرهنگ معین
42:* لادن سیبی: (زیست شناسی ) یک قسم لادن که ریشه اش دارای غده هایی شبیه سیب زمینی است. 
46: {Tropaeolum} [زیست شناسی- علوم گیاهی] سرده ای از لادنیان یک یا چندسالۀ علفی با حدود 80 گونه که بومی امریکای جنوبی و مرکزی هستند و تعدادی از گل های معروف باغچه ای را شامل می شوند؛ گل هایشان معمولاً زیبا و رنگ آنها اغلب بسیار روشن است و دارای پنج گلبرگ و تخمدان سه ...
```


## [2026-09-06T22:45:35.502Z] TOOL CALL #59: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-06T22:45:35.539Z] TOOL RESULT

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


## [2026-09-06T22:46:16.333Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT && cat > 1874.vision.txt <<'EOF'\n[read from the page image by vision; printed page number ۱۸۷۴ = BQT vol. 3 scan (BQT_v3_picofile.pdf) pdf page 671]\nRunning head: لاییدن\n\nColumn entries (right column):\n«لاییدن ۲ ـ بروزن و معنی لافیدن(۱) است که سخنان زیاده از حد خود گفتن باشد ـ و بمعنی پرگویی و هرزه‌گویی هم هست.»\n\nFootnotes at the foot of the page:\n«(۱) چ ش : لابیدن .»\n«۲ ـ از : لاب ( لابه ) + یدن ( پسوند مصدری ) ؛ لابه کردن :\n بدار دنیا چون برفروخت آتش ظلم / سگار آن بجهنم همی‌خورد چو لئیم\n چو خون و ریم بپالوده خیره از مردم / بدوزخ اندر لاید که خون دهندش ورم.\n سوزنی سمرقندی « لغت نامه ».\n در اوراق مانوی ( پارتی ) lʾb ( نامیدن ، دعا کردن ، درخواست کردن ) = پارسی میانه (پهلوی) rʾb ، فارسی : لابه ،\n (Henning, A list of Middle Persian ..., BSOS, IX, 1, p. 84) ، سغدی lów-am ، سریکلی lew-am ( گفتگو کردن ، سخن گفتن ) « اسحق ۹۵۲ ».»\n\n[used for: page 300 (book p.270), root \"Lâ, Lâiô\", node #1 Persian lâyîdan — Mo'in's etymological footnote derives لاییدن from لاب/لابه + -یدن, comparing Manichaean Parthian lʾb \"to name, pray, request\", Sogdian lów-, Sarikoli lew- \"to speak\".]\nEOF\ncat > 1876.vision.txt <<'EOF'\n[read from the page image by vision; printed page number ۱۸۷۶ = BQT vol. 3 scan (BQT_v3_picofile.pdf) pdf page 673 — note: tools/ref_page.py's default offset (-1205) lands on printed 1874; use --pdf-page 673]\nRunning head: لادن\n\nEntry (right column, top):\n«لادن ۱ ـ بر وزن دادن ، نوعی از مشمومات است یعنی بوی کردنی و آن مانند دوشاب سیاه میباشد و آنرا عنبر عسلی گویند و در دواها بکار برند و آن از زمین ریگستان حاصل میشود باین طریق که گیاهی که از آن زمین روید بلادن آغشته باشد و بز آن گیاه را دوست میدارد و بهنگام چرا ریش و موی بز بدان آلوده میشود بعد از آن جدا میسازند ، و آنچه بر ریش بز آلوده باشد بهتر از آن است که بر موی ران و اعضای دیگر . گویند اگر در زیر دامن زنی که بچهٔ مرده در شکم داشته باشد بخور کنند بچهٔ مرده از مشیمه بیرون آید ۲ .»\n«لادنه ـ بکسر ثالث و فتح نون ، گیاهی باشد که از پوست ساق آن ریسمان سازند.»\n\nFootnote 1 (Mo'in's etymological note at the foot of the page):\n«۱ ـ معرّب آن لادن ، لاذن ، لاذنة ، شجرةاللادن ، لاتینی ladanum ، ciste = lède با lédum ، یونانی lâdanon « دزی ج۲ ص ۵۲۴ » ، آشوری ladunu ، عبری lôtem « عقار ۲۰۸ ف » . لادن ، شیرهٔ درختی است از نوع پیچک ، این شیره اگر از بر گیاه‌های درخت بزمین فرو چکد و با خاک در آمیزد کم ارزش‌تر است . در اشعار آمده : « بخیزد از میان لاد لادن » ، از لاد بمعنی خاک و گل است ، همان زمین آغشته بشیره یا صمغ لادن مقصود است . رک : هرمزدنامه ۱۵۸ـ۱۶۶ .»\nFootnote 2: «۲ ـ امروزه لادن نام قسمی گل است ( Tropaeolum majus , Capucine ) از خانوادهٔ Tropéolacées ...»\n\n[used for: page 300 (book p.270), root \"Ladunu\", node #3 Greek lâdon/lôtos — Mo'in equates NP لادن with Latin ladanum, Greek lâdanon, Assyrian (Akkadian) ladunu, Hebrew lôtem; he gives no Persian→Greek arrow and no lôtos.]\nEOF\nls -la 1874.vision.txt 1876.vision.txt"
}
```


### [2026-09-06T22:46:18.261Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 1449 Sep  6 18:46 1874.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 2421 Sep  6 18:46 1876.vision.txt
```


## [2026-09-06T22:47:33.345Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ndata=open('AKD.txt',encoding='utf-8',errors='replace').read()\nlines=data.split('\\n')\nn=946\noff=sum(len(l)+1 for l in lines[:n])\nprint('leaf',data.count('\\f',0,off))\nprint(lines[n][:400])\nEOF\necho \"=== LEW lamentum\"; grep -n \"lamentum\" LEW_1910.txt LAT.txt 2>/dev/null | head -5\necho \"=== SKT lament\"; grep -n \"^Lament\\|Lament\\.\" SKT.txt | head -3\necho \"=== WEB glossolalia\"; grep -c \"glossolalia\" WEB_vol1.txt\necho \"=== ARY ladan\"; grep -n \"لادن\" incoming/ARY/ARY_pages.txt | head -3\necho \"=== AFA\"; grep -n -i \"ladan\\|lādan\" AFA.txt | head -5\necho \"=== PHD lab\"; grep -n \"lʾp\\|lābag\\|lāb \" PHD.txt PHD_mackenzie.txt NYB_vol2_glossary.txt 2>/dev/null | head -5"
}
```


### [2026-09-06T22:47:35.402Z] TOOL RESULT

```
leaf 68
ncrd,  aram.  nardd,  griech.  vöqSos  usw.,  Narde,  wohl  <]  ind.  ndlddd.] [akk.  ladunu  jedenfalls  Premdw.  :  griech.  XtjSov,  h'jSavoy,  Ladanum;  dazu viell.  hebr.  löf.  dem  vieU.  auch  im  Aklc.  luffti  entspricht.]  akk.  a))iru
=== LEW lamentum
LAT.txt:4051:ansata: iaculamentum cum ansa.
LAT.txt:8587:rite: -v. Sofer, p.37; calamentum: branche sfeche (Colum.).
LAT.txt:10306:d'eau"; castellatim-, cas te l lamentum: sorte de boudin, ou de piat en
LAT.txt:22425:d'oi *fllandaria 339 aa; filamentum, flldtura M.L. 3393 a, fllStim-, cf.
LAT.txt:32048:lamentum, -i n. (usit^ au pl., d'ou le fem.sg. lamenta dans Pacuvius
=== SKT lament
9882:Lament,  vb.  (F.  -  L.)  F. L.  lammtari,  lo  wail.  *  L.  lamemti mournful  cry;  from  the  base  la-,  to a  cry ;  cf.  la-ttare.  to  bark.  Cf.  also laiate,  to  bark,  scold ;  Gk.  ^«iy.  to (^  RA.)     Der.  lament^  sb.
=== WEB glossolalia
0
=== ARY ladan
8090:آلمانی (7(ف054): لادنی ایا 300 (800 ار بر 270430
=== AFA
6215:des Ladanon (ib. 112); so die Märchen, die die schlauen
=== PHD lab
```


## [2026-09-06T22:47:46.142Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== LAT ctx\"; sed -n '32045,32055p' LAT.txt; echo \"=== AFA ctx\"; sed -n '6205,6225p' AFA.txt; echo \"=== SKT page\"; python3 - <<'EOF'\ndata=open('SKT.txt',encoding='utf-8',errors='replace').read()\nlines=data.split('\\n')\noff=sum(len(l)+1 for l in lines[:9881])\nprint('leaf',data.count('\\f',0,off),'-> p',data.count('\\f',0,off)-20)\nEOF\npython3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'))\nfor k in ['AKD','AFA','LAT','WLD']: print(k, d[k].get('page_offset'))\""
}
```


### [2026-09-06T22:47:47.815Z] TOOL RESULT

```
=== LAT ctx
leurs que le latin a developpe le type k infixe nasal. - En baltique
et slave, il y a une racine parallble avec -k-: lit. lakti "lecher"
(en pariant d'animaux), serbe Ibkati "laper", etc.
lamentum, -i n. (usit^ au pl., d'ou le fem.sg. lamenta dans Pacuvius
R 3 175): lamentation( s). Correspond a gr. ©prjvoc. — Ancien, usuel.
D<?nominatif: lanentor,-aris (et k basse 4 poque lamento, panroman,
sauf roumain, M.L.48O7): se lamenter; et ses derives, lamentatio,
-tor,-trix,-tdbilis,-tdrius (Pl.Ca.yC, cf. datarius, manifestarius),
etc.; illamentatus (Vulg. = cbcXaucrxoc, do7iev0rixoc). .
Pour le sens, lamentum, qui est souvent analyse en *ld-men-to-m,
d'une racine *l 3 - avec suffixe d'instrument, ne va qn'avec arm. lam
=== AFA ctx
und Silber an Salomo**. II. Cliron. 9, 14. Die Königin
▼on Saba kommt zu Salomo mit Kameelen, die Gewürze,
Gold in Menge und edles Gestein tragen (ib. v. 1); »und
nicht fanden ihres Gleichen die Gewürze , die Sabsis Königin
dem König Salomo brachte" lib. v. 9).
Aber der Besitz und Erwerb dieser Herrlichkeiten war
mit grossen Gefahren verknüpft. Schreckliche Schlangen be-
wachten den Weihrauch (Herod. Hl. 109); gewaltige Vögel
die in Sümpfen wachsende Kasia (ib. 110); gefahrvoll war
die Gewinnung des Kinnamomon (ib. 111) mühevoll die
des Ladanon (ib. 112); so die Märchen, die die schlauen
Araber den Fremden erzahlten, um sie vom Eintritte in
ihr Land abzuschrecken. Doch der grosse Macedonier, der
halb Asien sich unterworfen hatte, konnte dadurch nicht
abgehalten werden , seinen Blick auch auf das schätzereiche
Arabien zu richten. Aber über den Vorbereitungen zu ei-
nem Zuge dorthin ereilte ihn der Tod (Strabo Lib. XVI.
785).
Nicht spärlicher wird der Preis Arabiens , als es mit der
Ausbreitung der römischen Macht in das helle Licht der
Geschichte eintritt. Von den Schätzen der glücklichen Ara-
=== SKT page
leaf 260 -> p 240
AKD leaf = printed + 8 (e.g. leaf 21 = p.13). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
AFA leaf = printed + 30 (e.g. leaf 38 = p.8). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
LAT leaf = printed + 18 for most of the book (e.g. leaf 21 = p.3); drifts in places (leaf 219 = p.301 -> -82?? probably a mis-detected number) - grep the headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
WLD Band 3: leaf = printed + 6. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696).
```


## [2026-09-06T22:48:02.395Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ndef leafpage(path,line,off,label):\n    data=open(path,encoding='utf-8',errors='replace').read()\n    lines=data.split('\\n')\n    o=sum(len(l)+1 for l in lines[:line-1])\n    leaf=data.count('\\f',0,o)\n    print(label,'leaf',leaf,'-> printed p',leaf-off)\nleafpage('AFA.txt',6215,30,'AFA')\nleafpage('incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt',24435,5,'WLD Bd2')\nEOF"
}
```


### [2026-09-06T22:48:04.202Z] TOOL RESULT

```
AFA leaf 204 -> printed p 174
WLD Bd2 leaf 0 -> printed p -5
```


## [2026-09-06T22:48:10.325Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"lal(l)\" incoming/WLD/WLD_Bd2_pages.txt | head -5; grep -n \"Redupl. lal\" incoming/WLD/WLD_Bd2_pages.txt | head -3"
}
```


### [2026-09-06T22:48:10.396Z] TOOL RESULT

```
24810:   Redupl. lal(l)d-: ai. lalallct „Laut eines Lallenden“, gr. Xdlog „ge-
24810:   Redupl. lal(l)d-: ai. lalallct „Laut eines Lallenden“, gr. Xdlog „ge-
```


## [2026-09-06T22:48:13.992Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR<=24810 && /\\[pdf page/ {p=$0} END{}' incoming/WLD/WLD_Bd2_pages.txt; grep -n \"\\[pdf page\" incoming/WLD/WLD_Bd2_pages.txt | awk -F: '$1<24810' | tail -2; echo \"--- start of the la- article\"; grep -n \"^ *lā-\\|Schallwurzel\\|Schallwz\" incoming/WLD/WLD_Bd2_pages.txt | awk -F: '$1>24350 && $1<24440' | head"
}
```


### [2026-09-06T22:48:15.845Z] TOOL RESULT

```
--- start of the la- article
```


## [2026-09-06T22:48:19.096Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && head -3 incoming/WLD/WLD_Bd2_pages.txt; grep -c \"\" incoming/WLD/WLD_Bd2_pages.txt; grep -n \"377\" incoming/WLD/WLD_Bd2_pages.txt | awk -F: '$1>24500 && $1<25100' | head; sed -n '24770,24790p' incoming/WLD/WLD_Bd2_pages.txt"
}
```


### [2026-09-06T22:48:20.849Z] TOOL RESULT

```
                ALOIS WALDE


47596
24824:                                                 la-,   lai-,   la[i]-dh-                              377
Jajati ,bellen, schiinpfen“ (a. auch Berneker687 und 694 iiber slav. lafa^
             5


latv^)^ lit. lojti, loti^ lett. lat „bellen''; alb. Veh „be]le^' (G. Meyer Alb. Wb.

240) got. Jailoun „sie schmahten“ (Praes. wohl ^lojan^ s. Streitberg Got.
       ;


El.    ® 76 Anm. 1        keine Stiitze fiir */e- ist anord. la „tadelii‘', da = alid.
                             ;


Jaha72^ z. B. Cleasby-Yigfusson Diet.               s. v,
                                                            ;
                                                                grm. lilo- = idg. Ida- sicher in nhd.
kiirnt. Jilen „brullen,        YomEinde“); mir. liim .^klage aa“                                 kaum niit
idg.       Ii-   als Tiefstufe zu *Za/o nach Wiedemann BB. 28, 58).
     Gr. ArjQog ,jalbernes Geschwatz, Possen, Tand'^, ?,i]Q£Co „schwatze“ (urgr.
```


## [2026-09-06T22:48:32.341Z] TOOL CALL #67: Bash

```json
{
 "command": "tail -20 data/verification/sources/web/index.jsonl | python3 -c \"\nimport sys,json\nfor l in sys.stdin:\n    d=json.loads(l); print(d['status'], d['url'])\""
}
```


### [2026-09-06T22:48:34.350Z] TOOL RESULT

```
200 https://en.wiktionary.org/wiki/%CE%BB%CE%B1%CE%BB%CE%AD%CF%89
200 https://en.wiktionary.org/wiki/lamentum
-1 https://en.wiktionary.org/wiki/%D9%84%D8%A7%DB%8C%DB%8C%D8%AF%D9%86
200 https://en.wiktionary.org/wiki/%D9%84%D8%A7%D8%AF%D9%86
200 https://en.wiktionary.org/wiki/%D9%84%D8%A7%D8%A8%D9%87
200 https://en.wiktionary.org/wiki/%CE%BB%CE%AE%CE%B4%CE%B1%CE%BD%CE%BF%CE%BD
200 https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/leh%E2%82%82-
200 https://www.ahdictionary.com/word/search.html?q=ladanum
200 https://www.ahdictionary.com/word/search.html?q=lotus
200 https://en.wiktionary.org/wiki/labdanum
200 https://www.ahdictionary.com/word/search.html?q=labdanum
200 https://abadis.ir/fatofa/%D9%84%D8%A7%DB%8C%DB%8C%D8%AF%D9%86/
200 https://abadis.ir/fatofa/%D8%B4%D8%A8%D8%AF%DB%8C%D8%B2/
200 https://vajehyab.com/moein/%D8%B4%D8%A8
200 https://abadis.ir/fatofa/%D9%84%D8%A7%D8%AF%D9%86/
-1 https://www.academia.edu/35394163/_SWIran_didā_fortress_walled_residence_in_Iranian_Toponymy_by_Garnik_Asatrain
-1 https://en.wiktionary.org/wiki/%E0%A4%B0%E0%A5%8C%E0%A4%A8%E0%A4%95%E0%A5%BC
-1 https://forum.wordreference.com/threads/persian-rustaki-and-latin-rusticus-rustic.3399756/
-1 https://forum.wordreference.com/threads/persian-etymology-of-rostam.3387039/
200 https://en.wiktionary.org/wiki/%D8%A2%D8%AA%D8%B4
```


## [2026-09-06T22:48:38.894Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && wc -c 1bf33d2aa426ebba.txt; grep -n -i \"does not have\\|no entry\\|Descendants\\|Root\\|bark\\|howl\" 1bf33d2aa426ebba.txt | head -12"
}
```


### [2026-09-06T22:48:38.950Z] TOOL RESULT

```
6746 1bf33d2aa426ebba.txt
62: Root 
71: Root 
138: This Proto-Indo-European entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.
143: Root
148: to bark , howl 
166: (The following are either from this root, as if "to bark/shriek" > "to tear" or some other relation from strong sound to tearing, or this root should be separated.)
183: Terms derived from the Proto-Indo-European root *leh₂- (bark) (16 c, 0 e) 
220: Proto-Balto-Slavic: *lā́ˀtei ( see there for further descendants )
222: Root
261: Terms derived from the Proto-Indo-European root *leh₂- (concealed) (23 c, 0 e) 
307: Proto-Indo-European roots 
308: Proto-Indo-European ReH-shaped roots
```


## [2026-09-06T22:48:42.159Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '143,175p' 1bf33d2aa426ebba.txt | tr -s ' '"
}
```


### [2026-09-06T22:48:42.207Z] TOOL RESULT

```
 Root
 [ edit ] 

 *leh₂- [ 1 ] 

 to bark , howl 

 Extensions
 [ edit ] 

 *leh₂-k- [ 2 ] 
 *leh₂-k-?- 
 Proto-Hellenic: 
 Ancient Greek: λᾱκέω ( lākéō ) , ληκέω ( lēkéō ) 

 *l̥h₂-k-sḱéti 
 Proto-Hellenic: 
 Ancient Greek: λάσκω ( láskō ) 

 *l̥h₂-k-ero- 
 Proto-Hellenic: *lakerós 
 Ancient Greek: λακερός ( lakerós ) 

 (The following are either from this root, as if "to bark/shriek" > "to tear" or some other relation from strong sound to tearing, or this root should be separated.)

 *l̥h₂-n̥-k- 
 Proto-Italic: *lank?nō 
 Latin: lancinō 

 *l̥h₂-k-ero- 
 Proto-Italic: *lakeros 
 Latin: lacer , lacerō
```


## [2026-09-06T22:54:16.572Z] TOOL CALL #70: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk300.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\nEO = \"https://www.etymonline.com/word/\"\nAHD = \"https://www.ahdictionary.com/word/search.html?q=\"\n\ndoc = {\n \"pdf_page\": 300,\n \"book_page\": 270,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-06\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"Lâ, Lâiô\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *leh₂- 'to bark, howl' (older notation *lā-; Pokorny 1. lā- 650-651, Walde-Pokorny II 377 'lā-, lāi-, lā[i]-dh-')\",\n   \"note\": \"The root is real, the language label is right and the gloss is right. Nourai's double headword 'Lâ, Lâiô' reproduces exactly the two shapes the literature uses: Pokorny's bare 1. lā- (an onomatopoeic/Schallwurzel article, pp. 650-651) and Mann's verbal entry laiō 'roar, bellow, bark' (IEC 659). Modern reconstruction is *leh₂-, with the laryngeal explaining the long ā of Lat. lāmentum, Lith. lóti, OCS lajati. Two caveats that matter for the branches below: (a) Pokorny and Walde-Pokorny treat the reduplicated lal(l)ā- (Gk. λάλος, λαλέω, Lat. lallāre) and the 'lull/rock' group lei-, lul- (MLG lollen, NHG lullen, Eng. lull) as sub-sections of the same expressive article, whereas Klein separates the imitative base *lel-, *lul- 'to move to and fro' from *lal-; (b) with echoic roots parallel independent creation can never be excluded, as Beekes notes for λαλέω. Nourai's gloss 'roar, bark, bellow' is Mann's wording verbatim.\",\n   \"note_fa\": \"ریشهٔ هندواروپایی آغازین *leh₂- (نگارش کهن‌تر *lā-) به معنی «پارس کردن، زوزه کشیدن، بانگ زدن» ریشه‌ای است آوایی/تقلیدی (Schallwurzel) که پوکورنی آن را در صفحات ۶۵۰–۶۵۱ و والده-پوکورنی در جلد دوم ص ۳۷۷ زیر «lā-, lāi-, lā[i]-dh-» آورده‌اند؛ مان (IEC ۶۵۹) همان را به صورت فعلی laiō «غریدن، بانگ زدن، پارس کردن» ثبت کرده است. عنوان دوگانهٔ نورایی «Lâ, Lâiô» درست همین دو صورت کتاب‌های مرجع است و معنایی که داده نیز واژه‌به‌واژه از مان گرفته شده. تنها نکتهٔ احتیاطی این است که در ریشه‌های تقلیدی امکان پیدایش مستقل واژه‌ها در هر زبان همیشه هست (بیکس دربارهٔ λαλέω همین را می‌گوید) و نیز شاخهٔ «lul-/lel-» (انگلیسی lull) را کلاین ریشه‌ای جدا می‌داند. در مجموع ادعای نورایی دربارهٔ خود ریشه درست است.\",\n   \"sources\": [W+\"Reconstruction:Proto-Indo-European/leh%E2%82%82-\", W+\"lamentum\", W+\"%CE%BB%CE%B1%CE%BB%CE%AD%CF%89\"],\n   \"ref_check\": [\n    {\"ref\": \"IEC:659\", \"status\": \"supports\",\n     \"note\": \"Mann, IEC: 'laiō ‘roar, bellow, bark’. WP II, 377  Skt. rāyāmi, id.; Per. lāyam, id.; Oss. räin, räjun ...; Arm. lam ‘weep’; ... Lat. cf. la-mentum ‘weeping’ ...' (IEC.txt line 9426). The leaf carrying this entry is leaf 371 of the archive.org scan, which prints the folio numbers 659 and 660, so the citation is on the page.\"},\n    {\"ref\": \"POK:651\", \"status\": \"supports\",\n     \"note\": \"Pokorny's article '1. lā-' (POK_full.txt, the block ending 'Page(s): 650-651'): 'Latin lamentum ‘lamentation’, lamentari ‘lament’, latro, -are ‘bark, bay’ ... Lithuanian loju, loti ‘bark, bay’ ... Reduplicated lal(l)a-: gr. λάλος ... Latin lallo, -are ... Middle Low German lollen, Modern High German lullen'. p. 651 falls inside the article.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"WLD\", \"where\": \"Bd. II p. 377 (running head 'la-, lai-, la[i]-dh- 377', WLD_Bd2_pages.txt line 24824)\", \"stance\": \"supports\",\n     \"note\": \"'Redupl. lal(l)ā-: ai. lalallā ‘Laut eines Lallenden’, gr. λάλος ‘geschwätzig’, λαλιά, λαλέω ‘schwatze’, lat. lallo, -are ‘in den Schlaf singen’ ... nhd. lallen'; and 'Ähnliche Lallworte für ‘in den Schlaf singen, einlullen’ ... nhd. lullen, engl. lull'. This is the WP II 377 that Mann cites.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins appendix s.v. la- (AHD_watkins1985.txt line 658)\", \"stance\": \"supports\",\n     \"note\": \"'la-. Echoic root. 1. Middle Dutch lollen ... 2. Middle Low German lollen, to lull ... 4. Latin lamentum, expression of sorrow: LAMENT. 5. Greek lalos, talkative: ECHOLALIA. 6. Greek lalein, to talk: GLOSSOLALIA. [Pok. 1. la- 650.]' — the whole chart of entry 0 is this one article.\"},\n    {\"src\": \"KLN\", \"where\": \"s.v. lull (KLN_1966.txt line 22286, printed p. ~897)\", \"stance\": \"partial\",\n     \"note\": \"'All these words are derivatives of the I.-E. imitative base *lel-, *lul-, ‘to move to and fro’ ... Cp. also the imitative base *lal-, seen in Gk. λαλεῖν ... L. lallare' — Klein keeps *lul- and *lal- apart instead of gathering them under one lā-.\"},\n    {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. lamentum (LAT.txt line 32048)\", \"stance\": \"supports\",\n     \"note\": \"'lamentum, qui est souvent analysé en *lā-men-to-m, d'une racine *lā- avec suffixe d'instrument' — the same root, with the -mentum suffix.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Persian\", \"words\": \"lâyîdan\", \"verdict\": \"plausible\",\n     \"derivation\": \"NP لاییدن lāyīdan is a real verb and its meaning sits exactly on the root: Dehkhoda glosses it 'لائیدن. نالیدن. (برهان). عوعو کردن سگ' — 'to moan, lament' AND 'to bay/bark (of a dog)' — and Mo'in's own summary gives 'گفتن / نالیدن / عوعو و پاس سگ / هرزه‌گویی'. Mann is the direct warrant for the arrow: under laiō 'roar, bellow, bark' he lists 'Per. lāyam' beside Skt. rāyati, Oss. räjun, Arm. lam, Lith. lóti (IEC 659), i.e. an inherited *lā-ye/o- present, Old Iranian *rā-/*lā- > MP *lāy- > NP lāy-īdan with the regular NP infinitive in -īdan. The competing account is Mo'in's: in his Farhang (s.v. لاییدن) and in his footnote to Borhan-e Qate' p. 1874 he analyses the verb as denominal, لاب/لابه lāb(a) 'entreaty, supplication' + -īdan, comparing Manichaean Parthian lʾb 'to name, pray, request' (Henning, BSOS IX/1 p. 84), MP lābag (whence NP لابه, cf. Wiktionary), Sogdian lów-, Sarikoli lew- 'to speak'; Borhan's own head-gloss is 'بروزن و معنی لافیدن ... پرگویی و هرزه‌گویی' beside the variant لابیدن. The two accounts both start from expressive 'sound/speech' material and could converge (a *lā-b- extension of the same echoic base), but they are not the same derivation, so the arrow is plausible rather than proved. Nourai's gloss 'to express sorrow' = Dehkhoda's نالیدن.\",\n     \"derivation_fa\": \"«لاییدن» فعلی است واقعی؛ دهخدا آن را «لائیدن. نالیدن. (برهان). عوعو کردن سگ» معنی می‌کند و معین نیز «گفتن، نالیدن، عوعو و پاس سگ، هرزه‌گویی» آورده است — یعنی درست همان دو معنای «بانگ/پارس» و «ناله» که در ریشهٔ هندواروپایی *leh₂- هست. پشتوانهٔ مستقیم پیکان نورایی مان است که در IEC ۶۵۹ زیر laiō صورت «Per. lāyam» را در کنار سنسکریت rāyati و اوستی räjun و لیتوانیایی lóti آورده؛ بر این پایه ستاک ایرانی *lā-ya- در فارسی میانه *lāy- و در فارسی نو با پسوند مصدری ‌ـیدن «لاییدن» شده است. اما معین در فرهنگ خود و در حاشیهٔ برهان قاطع (ص ۱۸۷۴) آن را مشتق از «لاب/لابه» + «ـیدن» می‌داند و با پارتی مانوی lʾb «نامیدن، دعا کردن، درخواست کردن»، فارسی میانه lābag، سغدی lów- و سریکلی lew- «سخن گفتن» می‌سنجد؛ در برهان معنی سرواژه «پرگویی و هرزه‌گویی» و صورت دیگرش «لابیدن» است. هر دو تبیین از مادهٔ آوایی «صدا/سخن» آغاز می‌شود ولی یکی نیستند؛ پس ادعای نورایی با احتیاط پذیرفتنی است.\",\n     \"sources\": [\"https://abadis.ir/fatofa/%D9%84%D8%A7%DB%8C%DB%8C%D8%AF%D9%86/\", W+\"%D9%84%D8%A7%D8%A8%D9%87\"],\n     \"ref_check\": [\n      {\"ref\": \"IEC:659\", \"status\": \"supports\",\n       \"note\": \"'laiō ‘roar, bellow, bark’. WP II, 377  Skt. rāyāmi, id.; Per. lāyam, id.' (IEC.txt line 9426, leaf 371 = printed pp. 659-660) — Mann's 'Per. lāyam' is precisely this node.\"},\n      {\"ref\": \"MON:3549\", \"status\": \"partial\",\n       \"note\": \"Mo'in's entry exists and reads 'لاییدن: [= لاب (= لابه) + یدن؛ قس. مصدری مانوی پارتی: نامیدن، دعا کردن، درخواست کردن] تضرع کردن' (MON_part2.txt line 37656) — it confirms the word and the meaning but derives it from لابه, not from the IE echoic root. The page number could not be checked: the archive.org scan of Mo'in carries no page markers, but the alphabetical position (لادن at MON:3523, لاییدن at MON:3549) is internally consistent.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BQT\", \"where\": \"vol. 3, printed p. 1874 = BQT_v3_picofile.pdf pdf page 671 (image + reading saved as ocr/BQT/1874.png, 1874.vision.txt)\", \"stance\": \"partial\",\n       \"note\": \"Head entry 'لاییدن ۲ ـ بروزن و معنی لافیدن است که سخنان زیاده از حد خود گفتن باشد ـ و بمعنی پرگویی و هرزه‌گویی هم هست'; Mo'in's footnote 2: 'از: لاب (لابه) + یدن (پسوند مصدری) ... در اوراق مانوی (پارتی) lʾb (نامیدن، دعا کردن، درخواست کردن) = پارسی میانه (پهلوی) rʾb، فارسی: لابه (Henning, BSOS IX, 1, p. 84)، سغدی lów-am، سریکلی lew-am (گفتگو کردن، سخن گفتن)'.\"},\n      {\"src\": \"MON\", \"where\": \"Farhang-e Farsi s.v. لاییدن (MON_part2.txt line 37656)\", \"stance\": \"partial\", \"note\": \"same denominal etymology as the Borhan footnote; meaning 'تضرع کردن'.\"},\n      {\"src\": \"HRN\", \"where\": \"Grundriss (HRN.txt), grep 'lāy', 'layidan', 'lāī'\", \"stance\": \"silent\", \"note\": \"Horn has no article for this verb.\"},\n      {\"src\": \"HUB\", \"where\": \"Persische Studien (HUB.txt), grep 'lāy'\", \"stance\": \"silent\", \"note\": \"no entry.\"},\n      {\"src\": \"CHEUNG\", \"where\": \"Etymological Dictionary of the Iranian Verb (CHEUNG.txt), grep '*lā', 'lāb'\", \"stance\": \"silent\", \"note\": \"Cheung has no root *lā-/*lāb- for this verb.\"},\n      {\"src\": \"ARY\", \"where\": \"Aryanpur, ARY_pages.txt / ARY_latin_index_pages.txt, grep 'لاییدن', 'LAY'\", \"stance\": \"silent\", \"note\": \"not treated.\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Germanic\", \"words\": \"lollen\", \"verdict\": \"plausible\",\n     \"derivation\": \"The form is real but the label is loose: lollen is Middle Low German (and Middle Dutch lollen 'to mutter'), a medieval attestation, not a Proto-Germanic reconstruction, so 'Germanic' in the box should be read as 'Low German'. AHD, Nourai's source, prints '2. Middle Low German lollen, to lull, akin to the Low German source of Middle English lullen, to lull: LULL' — i.e. it makes lollen a cognate of, not the ancestor of, English lull, which is what the arrow to node #3 claims. Pokorny (650) lists 'Middle Low German lollen, Modern High German lullen' inside the lei-, lul- 'lull, rock to sleep, swing' sub-section of the lā- article, and Klein assigns lull/lollen to a separate imitative base *lel-, *lul- 'to move to and fro' (comparing Skt. lolati 'moves to and fro'), not to *lā-/*lal-. The word and its sense 'to hum, mumble, lull' are beyond doubt; the attachment to this root and the parent-child arrow are the loose parts.\",\n     \"derivation_fa\": \"صورت lollen واقعی است اما برچسب «ژرمنی» دقیق نیست: این واژه آلمانی سفلای میانه (و هلندی میانه lollen «زیر لب گفتن») است، یعنی صورتی از دورهٔ میانه، نه بازسازی ژرمنی آغازین. خودِ AHD که مأخذ نورایی است می‌نویسد lollen «هم‌ریشهٔ» سرچشمهٔ انگلیسی میانهٔ lullen است نه نیای آن؛ پوکورنی نیز آن را در زیرشاخهٔ lei-/lul- «لالایی گفتن، تکان دادن» از همان مقالهٔ lā- آورده و کلاین یکسره آن را به مادهٔ تقلیدی جداگانهٔ *lel-/*lul- می‌برد. بنابراین اصل واژه درست است ولی پیوند آن به این ریشه و جهت پیکان با احتیاط پذیرفتنی است.\",\n     \"sources\": [EO+\"lull\"],\n     \"ref_check\": [\n      {\"ref\": \"AHD:1525\", \"status\": \"supports\",\n       \"note\": \"The Watkins IE-roots appendix of the AHD New College Edition runs pp. 1505-1550, so p. 1525 is the la- neighbourhood; our copy (the 1985 standalone reprint of the same list) reads 'la-. Echoic root ... 2. Middle Low German lollen, to lull, akin to the Low German source of Middle English lullen, to lull: LULL' (AHD_watkins1985.txt line 658).\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"1. lā-, p. 650 (POK_full.txt, the lei-/lul- paragraph)\", \"stance\": \"partial\",\n       \"note\": \"'similar lei-, lul- ‘lull, rock to sleep, swing’ in: ... Middle Low German lollen, Modern High German lullen, Lithuanian lelluoti ‘lull, cradle, swing’' — inside the lā- article, but flagged as a separate 'similar' formation.\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. II p. 377-378\", \"stance\": \"partial\", \"note\": \"'Ähnliche Lallworte für ‘in den Schlaf singen, einlullen, einwiegen, schaukeln’ ... nhd. lullen, engl. lull' — again grouped as look-alikes rather than as regular descendants.\"},\n      {\"src\": \"KLN\", \"where\": \"s.v. lull (KLN_1966.txt line 22286)\", \"stance\": \"contradicts\",\n       \"note\": \"'ME. lullen, lollen, of imitative origin. Cp. Swed. lulla, MLG., MDu. lollen, G. lullen ... derivatives of the I.-E. imitative base *lel-, *lul-' — a different base from *lā-/*lal-.\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"English\", \"words\": \"lull\", \"verdict\": \"confirmed\",\n     \"derivation\": \"English lull is first attested early 14c. as lullen 'to calm or hush to sleep' (Etymonline), of imitative origin — the lu-lu sound used over a cradle — with the Low German/Dutch relatives lollen, lulla, lullen. AHD explicitly ends its la- article with 'LULL', so the chart's Low German → English arrow is the AHD's own arrangement, and Klein's ME lullen 'of imitative origin' agrees on everything except the label of the base. Sense development inside English: 'hush to sleep' (14c.) > figurative 'quiet suspicion' (c. 1600) > noun 'temporary calm' (1650s/1751).\",\n     \"derivation_fa\": \"واژهٔ انگلیسی lull نخستین بار در آغاز سدهٔ چهاردهم به صورت lullen «آرام کردن، به خواب کردن» گواهی شده و خاستگاه آن تقلید آوای «لو-لو»یی است که بر گهواره می‌خوانند؛ هم‌خانواده‌های آن آلمانی سفلای میانه lollen، سوئدی lulla و آلمانی lullen‌اند. AHD نیز مقالهٔ la- را با همین واژه به پایان می‌برد، پس آرایش نمودار از خود AHD گرفته شده و کلاین هم آن را «با خاستگاه تقلیدی» می‌داند. ادعای نورایی در این گره درست است.\",\n     \"sources\": [EO+\"lull\"],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\",\n       \"note\": \"AHD_watkins1985.txt line 658 s.v. la-: '... akin to the Low German source of Middle English lullen, to lull: LULL'; the index line 'LULL la-' (line 1770) confirms the assignment.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"s.v. lull (KLN_1966.txt line 22286)\", \"stance\": \"supports\", \"note\": \"'lull, tr. and intr. v. — ME. lullen, lollen, of imitative origin' (base named *lel-, *lul-).\"},\n      {\"src\": \"SKT/etymonline\", \"where\": \"Etymonline s.v. lull\", \"stance\": \"supports\", \"note\": \"'early 14c., lullen ‘to calm or hush to sleep,’ probably imitative of lu-lu sound used to lull a child to sleep (compare Swedish lulla ..., Middle Dutch lollen ‘to mutter’)'.\"}\n     ]\n    },\n    {\n     \"id\": 4, \"lang\": \"Latin\", \"words\": \"lâmentum\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Latin lāmentum (usually pl. lāmenta) 'a wailing, moaning' is the instrument-noun *leh₂-men-to-m of this very root: Ernout-Meillet analyse it as '*lā-men-to-m, d'une racine *lā- avec suffixe d'instrument', Wiktionary reconstructs Proto-Italic *lāmentom < PIE *leh₂- 'expressive root: to howl, cry, bark', and Pokorny lists 'Latin lamentum, lamentari' together with Lat. lātrāre 'to bark' under 1. lā-. Nourai's spelling lâmentum correctly marks the long ā (from the laryngeal), and his gloss 'expression of sorrow' is AHD's wording verbatim. Denominative verb lāmentārī, whence the whole English family.\",\n     \"derivation_fa\": \"واژهٔ لاتینی lāmentum (بیشتر جمع: lāmenta) «شیون، زاری» درست همان ساخت ابزاری *leh₂-men-to-m از این ریشه است: ارنو-مه‌یه آن را «*lā-men-to-m از ریشهٔ *lā- با پسوند ابزار» تحلیل می‌کنند و ویکی‌واژه ایتالیک آغازین *lāmentom را از *leh₂- «زوزه کشیدن، فریاد زدن، پارس کردن» می‌گیرد؛ پوکورنی نیز lamentum و lamentari را در کنار lātrāre «پارس کردن» زیر همین ریشه آورده است. آوانگاری نورایی (â) درست کشیدگی ā را نشان می‌دهد که از لارنگال به جا مانده. ادعای نورایی درست است.\",\n     \"sources\": [W+\"lamentum\"],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\",\n       \"note\": \"AHD_watkins1985.txt line 658 s.v. la-: '4. Latin lamentum, expression of sorrow: LAMENT' — Nourai's gloss is copied from here word for word.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"1. lā-, pp. 650-651\", \"stance\": \"supports\", \"note\": \"'Latin lamentum ‘lamentation’, lamentari ‘lament’, latro, -are ‘bark, bay’'.\"},\n      {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. lamentum (LAT.txt line 32048)\", \"stance\": \"supports\", \"note\": \"'lamentum, -i n. ... lamentation(s). Ancien, usuel. ... souvent analysé en *lā-men-to-m, d'une racine *lā- avec suffixe d'instrument'.\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. II p. 377\", \"stance\": \"supports\", \"note\": \"the lā- article of WP II 377, which is the reference Mann gives for laiō.\"}\n     ]\n    },\n    {\n     \"id\": 5, \"lang\": \"English\", \"words\": \"lament\", \"verdict\": \"confirmed\",\n     \"derivation\": \"English lament (v.) is mid-15c. lamenten, a back-formation from lamentation or taken directly from Old French lamenter (14c.) and Latin lāmentārī 'to wail, moan', denominative of lāmentum; the noun lament follows in the 1590s from French lament / Latin lāmentum. Skeat states the same chain and takes it back to the root: 'Lament, vb. (F.-L.) ... L. lamentum, mournful cry; from the base la-, to cry'. So Latin lāmentum → (Old French) → English lament is uncontroversial.\",\n     \"derivation_fa\": \"فعل انگلیسی lament در میانهٔ سدهٔ پانزدهم به صورت lamenten پدیدار می‌شود، یا به عنوان اشتقاق پس‌ساز از lamentation یا مستقیماً از فرانسهٔ کهن lamenter (سدهٔ چهاردهم) و لاتینی lāmentārī «زاری کردن» که خود فعلِ برساخته از lāmentum است؛ اسم lament در دههٔ ۱۵۹۰ از فرانسه/لاتین وارد شده. اسکیت هم همین زنجیره را می‌آورد و آن را تا «مادهٔ la- به معنی فریاد زدن» پی می‌گیرد. ادعای نورایی درست است.\",\n     \"sources\": [EO+\"lament\"],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt s.v. la-: '4. Latin lamentum ...: LAMENT'; index line 'LAMENT la-' (line 1728).\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"SKT\", \"where\": \"Skeat, Concise, printed p. 240 (SKT.txt line 9882, leaf 260)\", \"stance\": \"supports\",\n       \"note\": \"'Lament, vb. (F. - L.) F. [lamenter], L. lamentari, to wail. — L. lamentum, mournful cry; from the base la-, to cry; cf. latrare, to bark, scold; Gk. λαλέω'.\"},\n      {\"src\": \"etymonline\", \"where\": \"s.v. lament\", \"stance\": \"supports\", \"note\": \"'mid-15c., lamenten, a back-formation from lamentation or else from Old French lamenter ... and directly from Latin lamentari ... from lamentum'.\"}\n     ]\n    },\n    {\n     \"id\": 6, \"lang\": \"Greek\", \"words\": \"lalein; lalos\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Gk. λαλέω (inf. λαλεῖν) 'to talk, chatter, prattle' and λάλος 'talkative' belong to the reduplicated shape lal(l)ā- of the root: Pokorny prints them under 1. lā- ('Reduplicated lal(l)a-: Old Indic lalalla ‘babble’; gr. λάλος ‘gabby, loquacious’, λαλιά ‘gossip’ ... Latin lallo, -are'), and Walde-Pokorny II 377 has the same paragraph. Wiktionary (after Beekes) is a shade more cautious: 'Uncertain. Perhaps a reduplicated form of Proto-Indo-European *leh₂-, with cognates including Latin lallō, Lithuanian laluoti, German lallen ... Could also simply be onomatopoeic' — but for an echoic root that caveat does not change the picture, since 'independent onomatopoeia' and 'inherited echoic root' are the same material. Both of Nourai's words and both of his glosses are AHD's, verbatim.\",\n     \"derivation_fa\": \"یونانی λαλέω (مصدر λαλεῖν) «سخن گفتن، وراجی کردن» و λάλος «پرگو» به گونهٔ مضاعف‌شدهٔ lal(l)ā- از همین ریشه بازمی‌گردند؛ پوکورنی آن‌ها را زیر «۱. lā-» و در بند «Redupl. lal(l)ā-» در کنار سنسکریت lalalla و لاتینی lallāre آورده و والده-پوکورنی (ج ۲ ص ۳۷۷) نیز همان را دارد. ویکی‌واژه به پیروی از بیکس محتاط‌تر است و می‌گوید «شاید صورت مضاعف *leh₂- باشد یا صرفاً نام‌آوا»؛ اما در ریشه‌های تقلیدی این دو گزینه عملاً یکی‌اند. هر دو واژه و هر دو معنایی که نورایی آورده عیناً از AHD گرفته شده و ادعای او درست است.\",\n     \"sources\": [W+\"%CE%BB%CE%B1%CE%BB%CE%AD%CF%89\"],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\",\n       \"note\": \"AHD_watkins1985.txt line 658 s.v. la-: '5. Greek lalos, talkative: ECHOLALIA. 6. Greek lalein, to talk: GLOSSOLALIA' — Nourai's node reproduces both entries.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"1. lā-, p. 650\", \"stance\": \"supports\", \"note\": \"'Reduplicated lal(l)a-: ... gr. λάλος ‘gabby, gossipy, loquacious’, λαλιά ‘gossip’, λαλέω ... Latin lallo, -are'.\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. II p. 377\", \"stance\": \"supports\", \"note\": \"'Redupl. lal(l)ā-: ... gr. λάλος ‘geschwätzig’, λαλιά ‘Geschwätz’, λαλέω ‘schwatze’'.\"},\n      {\"src\": \"KLN\", \"where\": \"s.v. lull, cross-reference (KLN_1966.txt line 22286)\", \"stance\": \"supports\", \"note\": \"'the imitative base *lal-, seen in Gk. λαλεῖν ‘to talk, chat, prattle’, λάλος ‘talkative, loquacious’, L. lallare'.\"}\n     ]\n    },\n    {\n     \"id\": 7, \"lang\": \"English\", \"words\": \"glossolalia, echolalia\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Both are learned 19th-century compounds built on Gk. λαλιά 'talk, prattle' (from λαλεῖν), not inherited words: glossolalia 'speaking in tongues' 1857 (earlier in German and Italian) = γλῶσσα 'tongue' + -lalia; echolalia 'meaningless repetition of words' 1876, taken from German (coined by von Romberg 1865) = ἠχώ 'echo' + -lalia. AHD's index accordingly files ECHOLALIA under la- and GLOSSOLALIA under both glōgh- and la-, exactly as the chart draws the arrow from the Greek box.\",\n     \"derivation_fa\": \"هر دو واژه ساخته‌های علمی سدهٔ نوزدهم بر پایهٔ یونانی λαλιά «سخن، پرگویی» (از λαλεῖν) هستند، نه واژه‌های موروثی: glossolalia «به زبان‌ها سخن گفتن» از ۱۸۵۷ (پیش‌تر در آلمانی و ایتالیایی) از γλῶσσα «زبان» + ‌lalia؛ و echolalia «تکرار بی‌معنی واژه‌ها» از ۱۸۷۶، برگرفته از آلمانی (ساختهٔ فون رومبرگ ۱۸۶۵) از ἠχώ «پژواک» + ‌lalia. نمایهٔ AHD نیز ECHOLALIA را زیر la- و GLOSSOLALIA را زیر glōgh- و la- می‌آورد؛ پس ادعای نورایی درست است.\",\n     \"sources\": [EO+\"glossolalia\", EO+\"echolalia\"],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\",\n       \"note\": \"AHD_watkins1985.txt index lines: 'ECHOLALIA la-' (line 1441) and 'GLOSSOLALIA glōgh-, la-' (line 1561), matching the article's items 5 and 6.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"etymonline\", \"where\": \"s.v. glossolalia; s.v. echolalia\", \"stance\": \"supports\",\n       \"note\": \"'glossolalia (n.) ... 1857 ..., from Greek glōssa ‘tongue, language’ + lalia ‘talk, prattle, a speaking,’ from lalein ‘to speak, prattle,’ echoic'; 'echolalia (n.) ... 1876, from German (von Romberg, 1865), from Greek ēkhō ... + lalia'.\"},\n      {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century, vol. 1 (WEB_vol1.txt), grep 'glossolalia'\", \"stance\": \"silent\", \"note\": \"0 hits — the volume on disk does not reach the entry.\"}\n     ]\n    }\n   ]\n  },\n  {\n   \"entry\": 1,\n   \"root\": \"Ladunu\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"Akkadian ladunu / ladinnu 'ladanum, the gum of the rockrose (Cistus)'\",\n   \"note\": \"The root word is real and the language label is right. AHD (5th ed., s.v. labdanum, the successor of the 1975 entry Nourai cites) gives '... from Greek lēdanon, lādanon, from lēdon, *lādon, rockrose, of Semitic origin; akin to Old South Arabian ldn ... and Akkadian ladinnu, ladunu, labdanum; see ldn in the Appendix of Semitic roots', and Wiktionary s.v. λήδανον: 'A loan, originally from Semitic. Compare Akkadian 𒆷𒁷𒉡 (ladinnu)'. Nourai's gloss 'resin of a certain tree' is right (the shrub is the rockrose, Cistus creticus/ladanifer, not a tree in the strict sense). One caveat: Zimmern (AKD p. 60) regards the Akkadian word as itself a Fremdwort, so 'Akkadian' is the oldest written attestation of a Semitic/Arabian culture word rather than certainly its birthplace. The chart's real problem is further down (node #3), where two different Semitic words, ladanum and lōtos, are put on one string and routed through Persian.\",\n   \"note_fa\": \"سرواژهٔ اکدی ladunu / ladinnu «صمغ درختچهٔ لادن (Cistus)» واقعی است و برچسب زبانی درست. فرهنگ American Heritage در چاپ پنجم ذیل labdanum می‌نویسد واژه از یونانی lēdanon/lādanon و آن از lēdon «گل لادن» با خاستگاه سامی است و با عربی جنوبی باستان ldn و اکدی ladinnu/ladunu پیوند دارد؛ ویکی‌واژه نیز ذیل λήδανον می‌گوید «وام‌واژه‌ای با خاستگاه سامی، قس. اکدی ladinnu». تنها نکته آن که زیمرن (ص ۶۰) خودِ واژهٔ اکدی را نیز وام‌واژه می‌داند، پس «اکدی» کهن‌ترین گواهیِ نوشتاری یک واژهٔ فرهنگیِ سامی/عربی است نه لزوماً زادگاه آن. اشکال اصلی نمودار در گرهٔ شمارهٔ ۳ است که دو واژهٔ سامیِ جداگانه (ladanum و lōtos) را در یک رشته و از راه فارسی به یونانی می‌برد.\",\n   \"sources\": [AHD+\"labdanum\", W+\"%CE%BB%CE%AE%CE%B4%CE%B1%CE%BD%CE%BF%CE%BD\", W+\"labdanum\"],\n   \"ref_check\": [\n    {\"ref\": \"AHD:730\", \"status\": \"supports\",\n     \"note\": \"p. 730 of the AHD New College Edition (1975/76) falls in the L pages of the dictionary body, where labdanum/ladanum stands; that volume is not on disk, but the same house's current text (ahdictionary.com s.v. labdanum, archived) reads '[Middle English, from Medieval Latin lapdanum, labdanum, alteration of Latin lādanum, from Greek lēdanon, lādanon, from lēdon, *lādon, rockrose, of Semitic origin; akin to Old South Arabian ldn ... and Akkadian ladinnu, ladunu, labdanum]' — the Akkadian etymon Nourai puts in the root box.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"AKD\", \"where\": \"Zimmern, Akkadische Fremdwörter, printed p. 60 (AKD.txt leaf 68)\", \"stance\": \"partial\",\n     \"note\": \"'[akk. ladunu jedenfalls Fremdw.: griech. λῆδον, λήδανον, Ladanum; dazu viell. hebr. lōṭ, dem viell. auch im Akk. luṭṭu entspricht.]' — the Akkadian-Greek equation is exactly Nourai's, but Zimmern calls the Akkadian word itself a loan.\"},\n    {\"src\": \"KLN\", \"where\": \"s.v. labdanum (KLN_1966.txt line 20927, printed p. ~895)\", \"stance\": \"supports\",\n     \"note\": \"'ML. labdanum, fr. L. ladanum, ledanum, fr. Gk. λάδανον, λήδανον, fr. λῆδον, ‘mastic’, which is of Sem. origin; cp. Akkad. ladunu, Arab. ladan, Heb. lot, ‘labdanum’.'\"},\n    {\"src\": \"BQT\", \"where\": \"vol. 3, printed p. 1876, Mo'in's footnote 1 (ocr/BQT/1876.png, 1876.vision.txt)\", \"stance\": \"supports\",\n     \"note\": \"'معرّب آن لادن، لاذن، لاذنة، شجرةاللادن، لاتینی ladanum ... یونانی lâdanon «دزی ج۲ ص ۵۲۴»، آشوری ladunu، عبری lôtem' — Mo'in too puts Akkadian ('Assyrian') ladunu at the head of the family.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Arabic\", \"words\": \"\", \"verdict\": \"plausible\",\n     \"derivation\": \"The box is deliberately empty in the book — a pass-through for the Arabic form that carries the word from Akkadian to Persian. The word meant is Arabic لاذَن lāḏan (also لادن ladan, لَدَان ladān, لَذَان laḏān) 'ladanum, the gum of the rockrose'; Klein cites it in exactly this position ('cp. Akkad. ladunu, Arab. ladan, Heb. lot'). That an Arabian word for the resin existed very early is beyond doubt: Herodotus 3.112 already describes how the Arabs gather λήδανον and gives λάδανον as their own form of the name (Fraenkel, Aram. Fremdwörter p. ~174, discusses this passage), and AHD points to Old South Arabian ldn. What is not settled is the direction of the arrow: Wiktionary's Arabic entry derives لاذن from Ancient Greek λάδανον (so Greek → Arabic), while Klein/AHD have the Semitic word feed Greek. Nourai's Akkadian → Arabic is therefore one defensible reading of a genuinely disputed link, not an established fact.\",\n     \"derivation_fa\": \"این خانه در کتاب عمداً تهی است و تنها حلقهٔ واسطهٔ عربی میان اکدی و فارسی را نشان می‌دهد؛ واژهٔ مورد نظر عربی «لاذَن / لادن» (و صورت‌های لَدان، لَذان) به معنی صمغ گیاه لادن است و کلاین آن را درست در همین جایگاه می‌آورد. وجود این واژه در عربستان از دیرباز مسلم است: هرودوت در کتاب سوم بند ۱۱۲ از گردآوری λήδανον به دست عرب‌ها سخن می‌گوید و صورت عربی λάδανον را نقل می‌کند، و AHD به عربی جنوبی باستان ldn اشاره دارد. اما جهت وام‌گیری قطعی نیست: ویکی‌واژه عربی لاذن را وام‌گرفته از یونانی λάδανον می‌داند، حال آن که کلاین و AHD واژهٔ سامی را سرچشمهٔ یونانی می‌شمارند. پس پیکان «اکدی ← عربی» نورایی یکی از خوانش‌های پذیرفتنی است، نه امری مسلم.\",\n     \"sources\": [W+\"%D9%84%D8%A7%D8%AF%D9%86\", AHD+\"labdanum\"],\n     \"ref_check\": [\n      {\"ref\": \"(none cited)\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference for this pass-through box; the claim was checked against Klein, AHD and Wiktionary instead (see consulted).\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"s.v. labdanum (KLN_1966.txt line 20927)\", \"stance\": \"supports\", \"note\": \"'... which is of Sem. origin; cp. Akkad. ladunu, Arab. ladan, Heb. lot, ‘labdanum’.'\"},\n      {\"src\": \"AFA\", \"where\": \"Fraenkel, Aramäische Fremdwörter, p. ~174 (AFA.txt leaf 204)\", \"stance\": \"partial\",\n       \"note\": \"'gefahrvoll war die Gewinnung des Kinnamomon (ib. 111), mühevoll die des Ladanon (ib. 112); so die Märchen, die die schlauen Araber den Fremden erzählten' — Fraenkel treats ladanon as an Arabian trade product known from Herodotus III.112, but has no Aramaic etymology for it.\"},\n      {\"src\": \"AFM\", \"where\": \"Addi Shir (AFM.txt line 5744)\", \"stance\": \"silent\", \"note\": \"no headword; لادن occurs only inside a quoted list 'والمسك واللادن والكافور'.\"},\n      {\"src\": \"FVQ\", \"where\": \"Jeffery, Foreign Vocabulary of the Qur'an (FVQ.txt), grep 'ladan'\", \"stance\": \"silent\", \"note\": \"not a Qur'anic word, no entry.\"},\n      {\"src\": \"Wiktionary\", \"where\": \"s.v. لادن (Arabic)\", \"stance\": \"contradicts\", \"note\": \"'Borrowed from Ancient Greek λᾱ́δᾰνον (lā́dănon).' — the reverse direction.\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Persian\", \"words\": \"lâdan\", \"verdict\": \"plausible\",\n     \"derivation\": \"NP لادن lādan is real and is described at length by Borhan-e Qate' (p. 1876): 'نوعی از مشمومات است ... مانند دوشاب سیاه ... و آن را عنبر عسلی گویند' — the dark, honey-like fragrant gum collected from the beards of goats that browse the rockrose; Manuchehri's line quoted in the chart ('نخیزد از میان لاد لادن') is genuine. The route Arabic → Persian is Klein's explicit statement, 'Pers. ladan is an Arabic loan word', and Biruni in the Ṣaydana (quoted by Dehkhoda s.v. لادن) says of it 'عربی است و به فارسی او را لادنه گویند'. Against that, Lokotsch (no. 1286) writes 'Ar. lādan ... [aus pers. lādān ‘Strauch’]' and Asbaghi (PLA p. 240) files lādan among Persian words in Arabic with the route 'pers. > griech. > lat.' — so the borrowing direction is genuinely contested and the node is plausible, not confirmed. The gloss is the weak point: لادن is the ladanum gum, not the lotus; Mo'in's second footnote on the same page notes that today گل لادن is the nasturtium (Tropaeolum majus, Capucine). Nourai's 'lotus' looks back-formed from the Greek lōtos he hangs beneath it.\",\n     \"derivation_fa\": \"«لادن» واژه‌ای است واقعی در فارسی و برهان قاطع (ص ۱۸۷۶) آن را چنین وصف می‌کند: «نوعی از مشمومات است ... مانند دوشاب سیاه ... و آن را عنبر عسلی گویند»؛ یعنی صمغ خوشبوی تیره‌ای که از ریش بزهای چرندهٔ گیاه لادن می‌گیرند، و بیت منوچهری که در نمودار آمده اصیل است. راه «عربی ← فارسی» را کلاین صریح می‌گوید («فارسی ladan وام‌واژه‌ای عربی است») و ابوریحان بیرونی در صیدنه (به نقل دهخدا) می‌نویسد «عربی است و به فارسی او را لادنه گویند». در برابر، لوکوچ (شمارهٔ ۱۲۸۶) عربی لادن را از فارسی lādān می‌گیرد و اصبغی (ص ۲۴۰) آن را در شمار واژه‌های فارسیِ عربی‌شده با مسیر «فارسی ← یونانی ← لاتینی» می‌آورد؛ پس جهت وام‌گیری واقعاً محل اختلاف است. اشکال دیگر معنایی است: لادن صمغ خوشبوست نه نیلوفر آبی (lotus)؛ معین در پانوشت دوم همان صفحه یادآور می‌شود که «گل لادن» امروز نام Tropaeolum majus است. معنای «lotus» ظاهراً از روی λωτός یونانیِ گرهِ پایین‌تر ساخته شده است.\",\n     \"sources\": [\"https://abadis.ir/fatofa/%D9%84%D8%A7%D8%AF%D9%86/\"],\n     \"ref_check\": [\n      {\"ref\": \"KLN:855\", \"status\": \"partial\",\n       \"note\": \"Klein's labdanum article says exactly what the arrow says — 'Pers. ladan is an Arabic loan word' (KLN_1966.txt line 20927) — but it stands on leaf 459 of the 1966 two-volume scan, i.e. printed p. ~895 (the L section opens on that leaf); p. 855 of that edition is in the 'ir-/is-' range (leaf 438 = p. 853). The page number appears to be mis-keyed, or taken from the 1971 one-volume edition, whose scan carries no page markers and could not be checked.\"},\n      {\"ref\": \"MON:3523\", \"status\": \"supports\",\n       \"note\": \"Mo'in's Farhang has the entry: 'لادن ... (اِ) نام صمغی است خوشبوی که از گیاه عشقه حاصل می‌شود و قاعده‌آور است ... لاذنه، لاذن' with the same Manuchehri verse (MON_part2.txt line 37796 ff.). Page number not verifiable (the archive scan of Mo'in has no page markers), but the alphabetical spacing to MON:3549 (لاییدن) is consistent.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BQT\", \"where\": \"vol. 3, printed p. 1876 (ocr/BQT/1876.png + 1876.vision.txt; reachable as pdf page 673 of BQT_v3_picofile.pdf, not the tool's default 671)\", \"stance\": \"supports\",\n       \"note\": \"Head entry 'لادن ـ بر وزن دادن، نوعی از مشمومات است ... و آن را عنبر عسلی گویند'; footnote 1 equates it with Latin ladanum, Greek lâdanon, Assyrian ladunu, Hebrew lôtem.\"},\n      {\"src\": \"MON\", \"where\": \"s.v. لادن (MON_part2.txt line 37796)\", \"stance\": \"supports\", \"note\": \"'نام صمغی است خوشبوی که از گیاه عشقه حاصل می‌شود' — gum, not lotus.\"},\n      {\"src\": \"PLA\", \"where\": \"Asbaghi, Persische Lehnwörter im Arabischen, p. 240 (PLA_asbaghi_1988_ia_djvu.txt line 17425)\", \"stance\": \"contradicts\",\n       \"note\": \"'لادن - lādan: ‘Ladanum’ pers. > griech. > lat.' — Asbaghi makes Persian the source, not the borrower.\"},\n      {\"src\": \"LKT\", \"where\": \"Lokotsch no. 1286 (LKT.txt line 3000)\", \"stance\": \"contradicts\",\n       \"note\": \"'1286. Ar. lādan: ‘Harziger Gummi’ [aus pers. lādān ‘Strauch’; vgl. gr. λάδανον Herod. III, 112, lat. ladanum]' — again Persian → Arabic.\"},\n      {\"src\": \"ARY\", \"where\": \"Aryanpur (ARY_pages.txt), grep 'لادن'\", \"stance\": \"silent\", \"note\": \"no entry.\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"Greek\", \"words\": \"lâdon, lôtos\", \"verdict\": \"disputed\",\n     \"derivation\": \"Two different words are put in one box and both are hung on Persian, which modern scholarship rejects. (a) λάδανον / λήδανον (from λῆδον, *λάδον 'rockrose') is first attested in Herodotus 3.112 (5th c. BCE), where it is expressly an Arabian product and λάδανον is quoted as the Arabs' own form — centuries before New Persian existed. AHD derives it 'from lēdon, *lādon, rockrose, of Semitic origin; akin to Old South Arabian ldn ... and Akkadian ladinnu, ladunu'; Wiktionary s.v. λήδανον: 'A loan, originally from Semitic. Compare Akkadian ladinnu'; Klein the same. So the Greek word comes from the Semitic side of the chart directly, not through Persian lādan (which Klein calls an Arabic loan). Older handbooks do print the Persian route — Skeat s.v. Laudanum '(L.-Gk.-Pers.)', Funk & Wagnalls '[L., < Gr. ladanon, < ladon, the mastic, < Pers. ladan, shrub]', Webster 'Ar. ladan; Per. ladan', Lokotsch 1286, Asbaghi PLA 240 — so Nourai is following a real, but now superseded, 19th/early-20th-century tradition. (b) λωτός is a separate borrowing and has nothing to do with lādan: Wiktionary, 'Probably from a Semitic source common to Hebrew לוֹט (lōṭ, ‘myrrh’)'; Klein s.v. lotus, 'fr. Gk. λωτός ... fr. Heb. lot, ‘labdanum’'; Etymonline, 'perhaps from Semitic (compare Hebrew lot ‘myrrh’)'. At most it is a cousin of ladanum within Semitic, never a descendant of the Persian word. Verdict for the node: disputed (worst of the two words); the semantic bridge 'lādan = lotus' in node #2's gloss exists only to make this box work.\",\n     \"derivation_fa\": \"در این خانه دو واژهٔ جداگانه در یک قاب نهاده و هر دو به فارسی بسته شده‌اند، و پژوهش امروزی هر دو پیوند را رد می‌کند. نخست λάδανον/λήδανον (از λῆδον «گیاه لادن») که کهن‌ترین گواهی‌اش هرودوت کتاب سوم بند ۱۱۲ (سدهٔ پنجم پیش از میلاد) است و همان‌جا فرآورده‌ای عربی خوانده شده و صورت λάδανον را از زبان عرب‌ها نقل می‌کند — یعنی سده‌ها پیش از پیدایش فارسی نو؛ AHD آن را «از lēdon با خاستگاه سامی، هم‌ریشه با عربی جنوبی باستان ldn و اکدی ladinnu/ladunu» می‌داند و ویکی‌واژه هم «وامی با خاستگاه سامی». پس یونانی مستقیماً از سوی سامیِ همین نمودار آمده، نه از راه «لادنِ» فارسی که خودِ کلاین آن را وام‌واژه‌ای عربی می‌شمارد. البته فرهنگ‌های کهن‌تر (اسکیت، فانک و واگنالز، وبستر، لوکوچ ۱۲۸۶، اصبغی) همان مسیر فارسی را می‌آورند، پس نورایی سنتی واقعی ولی امروز کنارگذاشته‌شده را دنبال کرده است. دوم λωτός که وام‌گیری جداگانه‌ای است و ربطی به لادن ندارد: ویکی‌واژه «احتمالاً از سرچشمه‌ای سامی، هم‌ریشه با عبری לוֹט lōṭ «مُر»» و کلاین «از عبری lot». بنابراین حکم این گره: رد شده (disputed).\",\n     \"sources\": [W+\"%CE%BB%CE%AE%CE%B4%CE%B1%CE%BD%CE%BF%CE%BD\", W+\"%CF%89%CF%84%CF%8C%CF%82\".replace(\"%CF%89\",\"%CE%BB%CF%89\"), AHD+\"labdanum\", EO+\"lotus\", EO+\"ladanum\"],\n     \"ref_check\": [\n      {\"ref\": \"BQT:1876\", \"status\": \"partial\",\n       \"note\": \"The cited page is right and does carry the Greek form: Mo'in's footnote 1 to لادن, 'لاتینی ladanum ... یونانی lâdanon «دزی ج۲ ص ۵۲۴»، آشوری ladunu، عبری lôtem' (image ocr/BQT/1876.png, reading in 1876.vision.txt; note the page is pdf page 673 of BQT_v3_picofile.pdf, two leaves past ref_page.py's default). But Mo'in lists the forms as an equation across languages headed by Akkadian, draws no Persian → Greek arrow, and never mentions lōtos — his Hebrew comparandum is lôtem.\"},\n      {\"ref\": \"SKT:1286\", \"status\": \"not_found\",\n       \"note\": \"Skeat's Concise Etymological Dictionary has c. 660 pages, so there is no p. 1286 (this is the only SKT citation above 592 in the whole book). Skeat's relevant entry is 'Laudanum. (L. - Gk. - Pers.)' on p. 240 (SKT.txt line 10013), which does route the word through Persian: 'L. ladanum ... Gk. λήδανον, λάδανον ... Gk. λῆδον, a shrub. — Pers. lādan'. The number 1286 is exactly Lokotsch's entry number for this word ('1286. Ar. lādan ... [aus pers. lādān]', LKT.txt line 3000), so the citation looks like a mis-keyed LKT:1286.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"AHD\", \"where\": \"ahdictionary.com s.v. labdanum (archived)\", \"stance\": \"contradicts\",\n       \"note\": \"'from Greek lēdanon, lādanon, from lēdon, *lādon, rockrose, of Semitic origin; akin to Old South Arabian ldn ... and Akkadian ladinnu, ladunu' — Semitic → Greek, no Persian link.\"},\n      {\"src\": \"KLN\", \"where\": \"s.v. labdanum and s.v. lotus (KLN_1966.txt lines 20927, 22184)\", \"stance\": \"contradicts\",\n       \"note\": \"'fr. Gk. λάδανον, λήδανον, fr. λῆδον ... which is of Sem. origin ... Pers. ladan is an Arabic loan word'; and 'lotus, n. — L., fr. Gk. λωτός, name of various plants, fr. Heb. lot, ‘labdanum’' — the two Greek words come from Semitic, and Persian is a terminal branch.\"},\n      {\"src\": \"LKT\", \"where\": \"no. 1286 (LKT.txt line 3000)\", \"stance\": \"supports\",\n       \"note\": \"'Ar. lādan ... [aus pers. lādān ‘Strauch’; vgl. gr. λάδανον Herod. III, 112, lat. ladanum]' — the old Persian-source view that Nourai's arrow follows; it also supplies the Herodotus reference.\"},\n      {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls, s.v. labdanum (FSD_vol2.txt line 70616)\", \"stance\": \"supports\",\n       \"note\": \"'[L., < Gr. ladanon, < ladon, the mastic, < Per. ladan, shrub.]' — same older tradition.\"},\n      {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century, s.v. labdanum (WEB_vol1.txt line 104457)\", \"stance\": \"partial\",\n       \"note\": \"'[ML.; L. ladanum, ledanum; Gr. ladanon, ledanon, from ledon, mastic; Ar. ladan; Per. ladan]' — lists Arabic and Persian side by side without deciding the direction.\"},\n      {\"src\": \"SKT\", \"where\": \"Skeat, Concise, p. 240 s.v. Laudanum (SKT.txt line 10013)\", \"stance\": \"supports\",\n       \"note\": \"'(L. - Gk. - Pers.) ... Gk. λῆδον, a shrub. — Pers. lādan, the gum-herb lada (Richardson)'.\"},\n      {\"src\": \"Wiktionary/Beekes\", \"where\": \"s.v. λήδανον and s.v. λωτός\", \"stance\": \"contradicts\",\n       \"note\": \"λήδανον: 'A loan, originally from Semitic. Compare Akkadian ladinnu'; λωτός: 'Probably from a Semitic source common to Hebrew לוֹט (lōṭ, ‘myrrh’)' — two independent Semitic loans, neither via Persian.\"}\n     ]\n    },\n    {\n     \"id\": 4, \"lang\": \"Latin\", \"words\": \"lôtus\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Latin lōtus (also lōtos) 'lotus, a plant name' is simply the Greek λωτός taken over by the Latin poets and naturalists (Vergil, Pliny) with the usual ō for Greek ω and the second-declension ending -us for -ος; AHD prints '[Latin lōtus, name of several plants, from Greek lōtos]'. The homograph lōtus 'washed' (perfect participle of lavāre) is a different word and unrelated. Note that the Greek → Latin step is uncontroversial; only the step above it (Persian → Greek) is not.\",\n     \"derivation_fa\": \"لاتینی lōtus (و lōtos) صرفاً همان λωτός یونانی است که شاعران و طبیعی‌نویسان لاتین (ویرژیل، پلینی) وام گرفتند، با تبدیل معمول ω یونانی به ō و پایانهٔ ‌os- به ‌us- در صرف دوم؛ AHD می‌نویسد «[لاتینی lōtus، نام چند گیاه، از یونانی lōtos]». همانند‌نویسِ lōtus «شسته» (اسم مفعول lavāre) واژه‌ای دیگر و بی‌ربط است. این حلقهٔ یونانی ← لاتینی بی‌گفت‌وگو درست است؛ تنها حلقهٔ بالاتر (فارسی ← یونانی) پذیرفتنی نیست.\",\n     \"sources\": [AHD+\"lotus\", EO+\"lotus\"],\n     \"ref_check\": [\n      {\"ref\": \"AHD:771\", \"status\": \"supports\",\n       \"note\": \"p. 771 of the AHD New College Edition is the lotus entry in the dictionary body (not on disk); the current AHD text, archived from ahdictionary.com s.v. lotus, reads '[Latin lōtus, name of several plants, from Greek lōtos.]' — exactly this arrow.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"s.v. lotus (KLN_1966.txt line 22184)\", \"stance\": \"supports\", \"note\": \"'lotus, n. — L., fr. Gk. λωτός, name of various plants, fr. Heb. lot, ‘labdanum’.'\"},\n      {\"src\": \"etymonline\", \"where\": \"s.v. lotus\", \"stance\": \"supports\", \"note\": \"'from Latin lotus, from Greek lotos, a word used as a name for several plants ... It is perhaps from Semitic (compare Hebrew lot ‘myrrh’).'\"},\n      {\"src\": \"SKT\", \"where\": \"Skeat, Concise (SKT.txt line 10698)\", \"stance\": \"partial\", \"note\": \"'the Cyrenaean lotus, the eaters called lotophagi' — Skeat treats the plant name without an etymology beyond Greek.\"}\n     ]\n    },\n    {\n     \"id\": 5, \"lang\": \"English\", \"words\": \"lotus\", \"verdict\": \"confirmed\",\n     \"derivation\": \"English lotus is a straight learned borrowing of Latin lōtus, first used in the 1540s as a name for various plants and from the 1580s specifically for the Egyptian white lotus; the yogic sense is 1848 (Etymonline). The Homeric λωτός of the lotus-eaters gives English lotophagi and lotus-eater (1812). No intermediate French form is needed, and the chart's Latin → English arrow is right.\",\n     \"derivation_fa\": \"واژهٔ انگلیسی lotus وام‌گیری مستقیم و کتابی از لاتینی lōtus است: نخستین کاربردش در دههٔ ۱۵۴۰ برای چند گیاه گوناگون و از دههٔ ۱۵۸۰ به‌ویژه برای نیلوفر سفید مصری، و معنای یوگایی آن از ۱۸۴۸ است. λωτός هومری (خوراک لوتوس‌خواران) نیز lotus-eater انگلیسی (۱۸۱۲) را به دست داده است. حلقهٔ لاتینی ← انگلیسی در نمودار درست است.\",\n     \"sources\": [EO+\"lotus\"],\n     \"ref_check\": [\n      {\"ref\": \"(none cited)\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference for this box; checked against Etymonline and AHD (see consulted).\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"etymonline\", \"where\": \"s.v. lotus\", \"stance\": \"supports\",\n       \"note\": \"'a name given to various plants, not all related or alike, 1540s, from Latin lotus, from Greek lotos ... (a sense attested in English from 1580s) ... The yogic sense is attested from 1848.'\"},\n      {\"src\": \"AHD\", \"where\": \"ahdictionary.com s.v. lotus\", \"stance\": \"supports\", \"note\": \"'[Latin lōtus, name of several plants, from Greek lōtos.]'\"},\n      {\"src\": \"KLN\", \"where\": \"s.v. lotus (KLN_1966.txt line 22184)\", \"stance\": \"supports\", \"note\": \"'lotus, n. — L., fr. Gk. λωτός ...'\"}\n     ]\n    }\n   ]\n  }\n ]\n}\n\nwith io.open('/home/sfmqrb/git/rishe/data/verification/page-300.json','w',encoding='utf-8') as f:\n    json.dump(doc, f, ensure_ascii=False, indent=2)\n    f.write('\\n')\nprint('ok')\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk300.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-300.json >/dev/null && echo JSON-OK && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 300"
}
```


### [2026-09-06T22:54:18.888Z] TOOL RESULT

```
ok
JSON-OK
nodes verified: 12/12
node verdicts: {'plausible': 4, 'confirmed': 7, 'disputed': 1}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 9, 'partial': 3, 'not_checked': 2, 'not_found': 1}
books consulted: {'partial': 7, 'silent': 8, 'contradicts': 7, 'supports': 22} | by book: {'KLN': 7, 'etymonline': 4, 'POK': 3, 'WLD': 3, 'SKT': 3, 'BQT': 2, 'MON': 2, 'ARY': 2, 'WEB': 2, 'LKT': 2, 'AHD': 2, 'HRN': 1, 'HUB': 1, 'CHEUNG': 1, 'SKT/etymonline': 1, 'LAT': 1, 'AFA': 1, 'AFM': 1, 'FVQ': 1, 'Wiktionary': 1, 'PLA': 1, 'FSD': 1, 'Wiktionary/Beekes': 1}
```


## [2026-09-06T22:54:24.847Z] TOOL CALL #71: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/page-300.json'))\nfor e in d['entries']:\n    for n in e['nodes']:\n        if n['id']==3 and e['entry']==1: print(n['sources'])\n\""
}
```


### [2026-09-06T22:54:26.458Z] TOOL RESULT

```
['https://en.wiktionary.org/wiki/%CE%BB%CE%AE%CE%B4%CE%B1%CE%BD%CE%BF%CE%BD', 'https://en.wiktionary.org/wiki/%CE%BB%CF%89%CF%84%CF%8C%CF%82', 'https://www.ahdictionary.com/word/search.html?q=labdanum', 'https://www.etymonline.com/word/lotus', 'https://www.etymonline.com/word/ladanum']
```


## [2026-09-06T22:54:30.842Z] TOOL CALL #72: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport json,io\np='data/verification/page-300.json'\nd=json.load(open(p))\ns=json.dumps(d,ensure_ascii=False,indent=2)\ns=s.replace('\"src\": \"SKT/etymonline\"','\"src\": \"etymonline\"').replace('\"src\": \"Wiktionary/Beekes\"','\"src\": \"Wiktionary\"')\nopen(p,'w',encoding='utf-8').write(s+'\\n')\nEOF\npython3 tools/verify_check.py 300"
}
```


### [2026-09-06T22:54:32.663Z] TOOL RESULT

```
nodes verified: 12/12
node verdicts: {'plausible': 4, 'confirmed': 7, 'disputed': 1}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 9, 'partial': 3, 'not_checked': 2, 'not_found': 1}
books consulted: {'partial': 7, 'silent': 8, 'contradicts': 7, 'supports': 22} | by book: {'KLN': 7, 'etymonline': 5, 'POK': 3, 'WLD': 3, 'SKT': 3, 'BQT': 2, 'MON': 2, 'ARY': 2, 'WEB': 2, 'Wiktionary': 2, 'LKT': 2, 'AHD': 2, 'HRN': 1, 'HUB': 1, 'CHEUNG': 1, 'LAT': 1, 'AFA': 1, 'AFM': 1, 'FVQ': 1, 'PLA': 1, 'FSD': 1}
```


## [2026-09-06T22:54:39.474Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT && ls -la 187*.??? 187*.txt 2>/dev/null; head -2 1876.txt 2>/dev/null"
}
```


### [2026-09-06T22:54:39.537Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 454639 Sep  5 16:55 1870.png
-rw-rw-r-- 1 sfmqrb sfmqrb   4381 Sep  5 16:56 1870.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   4381 Sep  5 16:56 1870.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 385446 Sep  6 18:39 1874.png
-rw-rw-r-- 1 sfmqrb sfmqrb   1449 Sep  6 18:46 1874.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   1449 Sep  6 18:46 1874.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  91864 Sep  6 18:39 1876.png
-rw-rw-r-- 1 sfmqrb sfmqrb   3726 Sep  6 18:38 1876.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   3726 Sep  6 18:38 1876.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   2421 Sep  6 18:46 1876.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   2421 Sep  6 18:46 1876.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 442264 Sep  4 15:37 1878.png
-rw-rw-r-- 1 sfmqrb sfmqrb   4418 Sep  4 15:37 1878.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   4418 Sep  4 15:37 1878.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 418415 Sep  6 18:51 1879.png
-rw-rw-r-- 1 sfmqrb sfmqrb   3781 Sep  6 18:51 1879.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   3781 Sep  6 18:51 1879.txt
REF: BQT:1876  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 671  OCR-lang: fas
```


## [2026-09-06T22:54:52.676Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT && sed -i '1s|.*|REF: BQT:1874  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 671  OCR-lang: fas|' 1876.txt && mv 1876.txt 1874.txt && timeout 900 python3 tools/ref_page.py BQT:1876 --image --pdf-page 673 2>&1 | head -8"
}
```


### [2026-09-06T22:54:54.401Z] TOOL RESULT

```
python3: can't open file '/home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/tools/ref_page.py': [Errno 2] No such file or directory
```


## [2026-09-06T22:54:56.581Z] TOOL CALL #75: Bash

```json
{
 "command": "timeout 900 python3 tools/ref_page.py BQT:1876 --image --pdf-page 673 2>&1 | head -8"
}
```


### [2026-09-06T22:55:02.329Z] TOOL RESULT

```
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1876.png
[transcription from the page image; OCR text in data/verification/sources/refs/ocr/BQT/1876.txt]
[read from the page image by vision; printed page number ۱۸۷۶ = BQT vol. 3 scan (BQT_v3_picofile.pdf) pdf page 673 — note: tools/ref_page.py's default offset (-1205) lands on printed 1874; use --pdf-page 673]
Running head: لادن

Entry (right column, top):
«لادن ۱ ـ بر وزن دادن ، نوعی از مشمومات است یعنی بوی کردنی و آن مانند دوشاب سیاه میباشد و آنرا عنبر عسلی گویند و در دواها بکار برند و آن از زمین ریگستان حاصل میشود باین طریق که گیاهی که از آن زمین روید بلادن آغشته باشد و بز آن گیاه را دوست میدارد و بهنگام چرا ریش و موی بز بدان آلوده میشود بعد از آن جدا میسازند ، و آنچه بر ریش بز آلوده باشد بهتر از آن است که بر موی ران و اعضای دیگر . گویند اگر در زیر دامن زنی که بچهٔ مرده در شکم داشته باشد بخور کنند بچهٔ مرده از مشیمه بیرون آید ۲ .»
«لادنه ـ بکسر ثالث و فتح نون ، گیاهی باشد که از پوست ساق آن ریسمان سازند.»
```


## [2026-09-06T22:55:07.025Z] TOOL CALL #76: Bash

```json
{
 "command": "ls -la data/verification/sources/refs/ocr/BQT/187{4,6}* && git status --short | head -30"
}
```


### [2026-09-06T22:55:09.008Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 385446 Sep  6 18:39 data/verification/sources/refs/ocr/BQT/1874.png
-rw-rw-r-- 1 sfmqrb sfmqrb   3726 Sep  6 18:54 data/verification/sources/refs/ocr/BQT/1874.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   1449 Sep  6 18:46 data/verification/sources/refs/ocr/BQT/1874.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  91864 Sep  6 18:39 data/verification/sources/refs/ocr/BQT/1876.png
-rw-rw-r-- 1 sfmqrb sfmqrb   4101 Sep  6 18:55 data/verification/sources/refs/ocr/BQT/1876.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   2421 Sep  6 18:46 data/verification/sources/refs/ocr/BQT/1876.vision.txt
?? data/verification/page-295.json
?? data/verification/page-300.json
```


## [2026-09-06T22:55:26.590Z] AGENT

Done — page 300 (book p. 270) verified; `verify_check.py 300` shows 0 PROBLEM lines.

**Counts** — 2 entries, 12 nodes. Node verdicts: 7 confirmed, 4 plausible, 1 disputed. Both root boxes confirmed. Ref checks: 9 supports, 3 partial, 1 not_found, 2 not_checked (boxes with no refs).

**Disputed**
- *Ladunu* #3 Greek `lâdon, lôtos` — two unrelated words in one box, both hung on Persian. λάδανον/λήδανον is already Arabian in Herodotus 3.112 (5th c. BCE) and is Semitic per AHD ("Old South Arabian ldn … Akkadian ladinnu, ladunu"), Klein and Wiktionary — not from New Persian lādan (which Klein calls an Arabic loan). λωτός is a separate Semitic loan (Hebrew lōṭ "myrrh"), never from lādan. Nourai follows the older Skeat / Funk & Wagnalls / Webster / Lokotsch / Asbaghi tradition, now superseded.

**Plausible (noted, not flagged)** — *Lâ* #1 Persian لاییدن (Mann IEC 659 has "Per. lāyam", but Mo'in derives it from لاب/لابه + -یدن, cf. Parthian lʾb); *Lâ* #2 "Germanic" lollen (actually Middle Low German, and AHD makes it a cognate of, not ancestor of, lull); *Ladunu* #1 Arabic (Wiktionary reverses the direction, Greek → Arabic); *Ladunu* #2 Persian lādan (gloss "lotus" is wrong — it is the ladanum gum; modern گل لادن = nasturtium).

**No extraction errors.** The PDF page image matches the JSON everywhere, including the odd citations below.

**Citation problems in the printed book (Nourai's own, not the extraction)**
- `SKT:1286` (Greek node): Skeat's Concise has ~660 pp., so no such page; his actual entry is *Laudanum* p. 240. 1286 is exactly Lokotsch's entry number for this word — almost certainly a mis-keyed `LKT:1286`. It is the only SKT citation above 592 in the whole book.
- `KLN:855` (Persian lādan): Klein's *labdanum* article, which says verbatim what the arrow claims, stands at p. ~895 (leaf 459); p. 855 is in the "ir-/is-" range.

**Tooling note for the coordinator:** `tools/ref_page.py` BQT offset is 2 pages low in this range — `BQT:1876` resolved to pdf page 671 = printed 1874. Correct page is pdf 673; I fixed the cache (`ocr/BQT/1874.png|txt|vision.txt` and `1876.png|txt|vision.txt` now hold the right pages) and noted the corrected pdf page in the ref_check.
