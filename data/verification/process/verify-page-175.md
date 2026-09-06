# Verification process log — verify-page-175


## [2026-09-05T20:49:40.630Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 175 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-175.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-175.json. Write /home/sfmqrb/git/rishe/data/verification/page-175.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 175` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T20:49:41.987Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T20:49:42.704Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T20:49:42.717Z] TOOL RESULT

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


## [2026-09-05T20:49:43.131Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-175.txt"
}
```


### [2026-09-05T20:49:43.149Z] TOOL RESULT

```
1	=== PDF page 175 (book page 145) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Ger 3 : to awaken  (refs POK:391)
4	#1 (parent #0) [Avestan] refs=POK:391 | gar 1 : to wake up ; â-gara-yeiti : wakes up
5	  #2 (parent #1) [Pahlavi] refs=POK:391 | vîgrâs : to awaken ; wiğrâd : awake
6	    #3 (parent #2) [Persian] refs=MON:621 | bîdâr «بیدار» : awake
7	#4 (parent #0) [Greek] refs=AHD | gregorious : awake, watchful
8	  #5 (parent #4) [Latin] refs=None | gregorious
9	    #6 (parent #5) [English] refs=None | Gregory, Gregorian
10	--- entry 1 ---
11	ROOT [Indo-European] Ger 4, Gurr, Gurô : to cry hoarsely, growl  (refs POK:383; IEC:308)
12	#1 (parent #0) [Persian] refs=MON:2411; IEC:308 | ğorridan «غرّیدن» : to growl | extra: غر ، غرّان ، غرّش
13	#2 (parent #0) [Sanskrit] refs=POK:383 | jaratĕ : to cry loudly
14	  #3 (parent #2) [Persian] refs=HRN:143; BQT:995 | zâr 2 «زار ۲» : cry | extra: زاری
15	#4 (parent #0) [Germanic] refs=AHD | krĕ, krô, kur : to cry, growl ; kranu : crane
16	  #5 (parent #4) [English] refs=IEC:308; AHD | crow, crack, croon, cur ; crane
17	#6 (parent #0) [Greek] refs=AHD:1516 | geranous : crane
18	  #7 (parent #6) [English] refs=AHD | geranium
19	#8 (parent #0) [Latin] refs=AHD; IEC:308 | grŭs : crane ; gurriô : churr, croon
20	
```


## [2026-09-05T20:49:47.015Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-175.json",
 "description": "Read source JSON for page 175"
}
```


### [2026-09-05T20:49:47.051Z] TOOL RESULT

```
{
  "pdf_page": 175,
  "book_page": 145,
  "entries": [
    {
      "root": {
        "name": "Ger 3",
        "lang": "Indo-European",
        "refs": "POK:391",
        "gloss": "to awaken"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:391",
          "words": [
            {"translit": "gar 1", "gloss": "to wake up", "script": null},
            {"translit": "â-gara-yeiti", "gloss": "wakes up", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "POK:391",
          "words": [
            {"translit": "vîgrâs", "gloss": "to awaken", "script": null},
            {"translit": "wiğrâd", "gloss": "awake", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "MON:621",
          "words": [
            {"translit": "bîdâr", "gloss": "awake", "script": "بیدار"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD",
          "words": [
            {"translit": "gregorious", "gloss": "awake, watchful", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Latin",
          "refs": null,
          "words": [
            {"translit": "gregorious", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "Gregory, Gregorian", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Ger 4, Gurr, Gurô",
        "lang": "Indo-European",
        "refs": "POK:383; IEC:308",
        "gloss": "to cry hoarsely, growl"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "MON:2411; IEC:308",
          "words": [
            {"translit": "ğorridan", "gloss": "to growl", "script": "غرّیدن"}
          ],
          "script_extra": "غر ، غرّان ، غرّش",
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "POK:383",
          "words": [
            {"translit": "jaratĕ", "gloss": "to cry loudly", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "HRN:143; BQT:995",
          "words": [
            {"translit": "zâr 2", "gloss": "cry", "script": "زار ۲"}
          ],
          "script_extra": "زاری",
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "krĕ, krô, kur", "gloss": "to cry, growl", "script": null},
            {"translit": "kranu", "gloss": "crane", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": "IEC:308; AHD",
          "words": [
            {"translit": "crow, crack, croon, cur", "gloss": null, "script": null},
            {"translit": "crane", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD:1516",
          "words": [
            {"translit": "geranous", "gloss": "crane", "script": null}
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
            {"translit": "geranium", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD; IEC:308",
          "words": [
            {"translit": "grŭs", "gloss": "crane", "script": null},
            {"translit": "gurriô", "gloss": "churr, croon", "script": null}
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


## [2026-09-05T20:49:47.150Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-05T20:49:47.185Z] TOOL RESULT

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


## [2026-09-05T20:50:07.100Z] TOOL CALL #5: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo --- && python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','AHD','IEC','MON','HRN','BQT','PHD','NYB','BRT','WLD','KLN','SKT','SYN','CHEUNG','ARY']:\n    v=d.get(k)\n    print(k, json.dumps(v,ensure_ascii=False)[:400])\n\""
}
```


## [2026-09-05T20:50:07.634Z] TOOL CALL #6: Bash

```json
{
 "command": "sed -n '1,60p' data/verification/page-124.json"
}
```


### [2026-09-05T20:50:08.868Z] TOOL RESULT

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
page-149.json
---
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
CHEUNG null
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root,
```


### [2026-09-05T20:50:08.902Z] TOOL RESULT

```
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
        },
        {
          "src": "AHD",
          "where": "Watkins 1985, s.v. dhē-¹",
          "stance": "supports",
          "note": "'To set, put. Contracted from *dheə.' Same gloss as Nourai's 'to do, set'."
        },
        {
          "src": "Wiktionary",
          "where": "Reconstruction:Proto-Indo-European/dʰeh₁-",
          "stance": "supports",
          "note": "'*dʰeh₁- (perfective): to do; to put, place.'"
        }
      ],
      "nodes": [
        {
          "id": 1,
          "lang": "Avestan",
          "words": "ma[n]dz-dha; ahura-mazdha",
          "verdict": "confirmed",
```


## [2026-09-05T20:50:14.265Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Page(s): 39[01]\" POK_full.txt | head -20; echo ---; grep -n \"Page(s): 38[34]\" POK_full.txt | head -20"
}
```


### [2026-09-05T20:50:14.406Z] TOOL RESULT

```
31694:Page(s): 390 
35681:Page(s): 390-391 
---
31334:Page(s): 383-385
```


## [2026-09-05T20:50:14.961Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"wachen, munter\\|heiser schreien\\|ger-4\\|ger-3\" POK_full.txt | head -30"
}
```


### [2026-09-05T20:50:15.020Z] TOOL RESULT

```
31336:Root / lemma: ger-3 
31503:Root / lemma: ger-3\ "to turn, wind' : Root/ lemma: (s)ker-3\ "to turn, bend'. 
31670:Root / lemma: ger-4, grei-
```


## [2026-09-05T20:50:22.641Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '31240,31350p' POK_full.txt"
}
```


### [2026-09-05T20:50:22.689Z] TOOL RESULT

```
1. Lithuanian gerse^ crane, heron '; after Risch (briefl.) contaminated from gerve ar\6 
genser, 

2. With formants -en-, to part with -u- and -g- extended: 

Armenian krunk' crane ' {*geru-n-g-); compare under Old High German kranuh; 

gr. yepHV Y£pavo(; Hes., y£pavo(; m. " crane ' and ' crane for lifting weights, esp. used in 
the theatre, quern, a fish '; 

gall, tarvos trigaranos (Inschr. about a bull with three plumes on the back); cymr. corn, 
bret. garan ( *gerenos) " crane '; 

Old High German kranuh {-ih). Old English cranoc, cornuc. Middle Low German kranek 
m. ( *granug-); 

Old English cran, asachs. krano. Middle High German krane. Modern High German 
Krahn ( *granon-) m.; in addition Old Icelandic trani^ crane ' (with /- instead of k- after trami 
" evil spirit, demon, evil supernatural being; devil '); 

Lithuanian garnysm. ' heron, stork ' {*gor-n-jos); Latvian garnsm. " heron '. 



3. With formants -6u- : -u-: 

Latin grus. Gen. gruisi. (later also m.) "a crane', therefrom ^r^e/ie 'of crane's call'; 

Modern High German westfal. krune^ crane '; see below Old High German kron, 

Lithuanian gerve, Latvian dzeJve, Old Prussian gerwei. " crane ' {*ger9uia)\ 

russ. -Church Slavic zeravb m. ( *gerduios), Serbo-Croatian zerav, wruss. z6rou{(jev\. 
zoraula); besides Serbo-Croatian zdralj{irom *zbravlb) and russ. zuravlb (Gen. zuravija). 

C. from the same ou-: au-: u-eyXev\s\ov\ also Old High German kron^ chatty, loquacious, 
talkative, garrulous, gossipy, prattling, logorrheic', ndd. krolen {*krauljan) 'loud cry', holl. 
kruilen^ coo ', krollen^ cry like cats ', Middle Low German kruschen^ screech, shriek, 
scream, squawk, cackle, croak, yell '. 

With /-extension redupl. Latin gingnre^ cackle, esp. from to geese '; 

perhaps (?) here gr. YiYYpa(;, YiYYpo(; m. ' Phoenician flute' etc.; 

Middle Irish grith, cymr. gryd^ scream ' {*gri-tu-s). Middle Irish grinnigud^ creaking of 
the arrow ' {*gri-n-d-) (common Celtic -ns-, -nt- > -nn-); 

Maybe alb. {*gri-n-d-) grindem ' scream, quarrel' 

Middle High German knschen^ screech, shriek, scream, squawk, cackle, croak, yell ', 
Middle Low German knten^cry, howl'. Middle High German /r/7"e/7 'sharp cry'. Modern High 
German kreiHen, Middle High German knsten. Modern High German kreisten. 

D. gra- in West Germanic nord. *kra- (with dnot changed to old a through recent 
imitation of the of a- a colored raven's croaking): Old High German kraen. Modern High 
German krahen. Middle Low German kreien. Old English crawanAs., Old High German 
hanacraf cock crow, call of a rooster; dawn, time of morning when roosters crow ', Old 
High German kra(w)a, kraia. Modern High German Krahe, Old Saxon kraia. Old English 
crawe6s., Lithuanian grioju, russ. -Church Slavic grajg, grajati^ croak, caw '. 

With guttural extension: 

Old Norse kraka^ccow', /rraA/"' raven'. Old English *cracian, cracettan^ croak, caw (of 
raven)'. Modern High German krachzen; Germanic -k- from Indo Germanic -^because of 



nir. grag^ croaking ' {*graggo-)\ Middle Low German krakelen^ cliatter, prattle, jabber; talk 
rapidly; talk nonsense '. 

With Indo Germanic A:-/ Latin gracu/us ']ack6a\N' , gracillo, -are^ gaggle, cackle, chitchat, 
talk, snicker (from chicken)'; 

Old High German kragil. Middle High German kreger gabby, gossipy, loquacious, 
garrulous, blithering ', Old High German kragilon^ babble, chatter'. Middle High German 
kragelen, kregeln^ gaggle, cackle, chitchat, talk, snicker'; 

russ. -Church Slavic gracu, grakatT croak, caw ', grbkatT coo (from the dove)'. 

E. With formant -g-, and from other hearing impressions: 

Old Indie ^a/75//" rages, roars, hums, bellows'; 

Armenian karkac^^\x\, fuss, noise'; 

Old English cracian, cearcian^ ring out; sound ', Old High German krahhon^ crack, 
creak'; 

Lithuanian girgzdziu, girgzdeti^creaV!. 

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
```


## [2026-09-05T20:50:22.852Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '31660,31720p' POK_full.txt; echo === ; sed -n '35640,35700p' POK_full.txt"
}
```


### [2026-09-05T20:50:22.905Z] TOOL RESULT

```
Exit code 1
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
jayarayantam^ the watching one ', Peri, jagara, participle Perf. f\VX. Jagaurvah-, jigaurvah-^ 
awake, watchful, wakeful', Kaus. a-garayeitT arouses, awakens ', with fra- inchoativ fra- 
y/7sa/77/70 "awakening' {*grhsk-), Kaus. fra-yra-yrayeiti, dissimil. fra-yra-rayeitT awakens'. 
Middle Persian k/^ass "awake', vTgrasenag^ livener'; 

gr. Eysipu) " awake ' (whether £- Adv. *e?compare eor din Avestan a-garayeiti ar\6 
above S. 280; different SchwyzerGr. Gr. I 6483), Aor. sypsTO, sypEaGai, Perf. s-ypn-yopa 
(for E-yn-yopa - compare Old Indicya-^a/a- with dem p from sypsaOai; Med. (late) s-yn- 
ysp-pai; of Perf. proceed from sypnyopTi " on guard ', sypnyopaic;); sypnaau) "watch' to 
*ypr|-T- (compare Avestan fra-srato^by awakening '); barely from *£ypriaKi(ji) (Schwyzer Gr. 
Gr. I 7082); 

alb. Tosc ngre {irorr\ which ngr^, Geg ngrei^\\i\. up, arouse, erect, awake, stretch a gun 
'{*n-gra-n-id), participle n-grite{*-grht-)\ 

presumably Old Norse karskr, /re/'s/r/'" fresh, agile, lively'. Middle Low German karsch 
"fresh, alert, awake, smart', Alemannian charzsch. 

References: WP. I 598 f., WH. I 429 f. 
Page(s): 390 



Root / lemma: g(e)u-lo- 

Meaning: glowing coals 

Note: 

Root / lemma: g(e)u-lo- : glowing coals derivded from Root / lemma: ker(9)-3\ to burn 

Material: With Asuffix: 

Irish guar coa\' (< *geulo- or * goulo); 

Old Icelandic kolu. " charcoal ', Old English colm. "coal', engl. coal. Old Frisian kolei.. 
Old High German kolom., also kolu.. Middle High German kolu., kol(e)xx\., kolei., Swiss 
c/7c»//e "gleam'. 

In addition with /"-suffix (or previously reshaped from *^^/c»- after Armenian hur^f\re'): 

Armenian Ara/r "fire, glowing coals' (< *guro-, *gura-), krak-aran^ siove, hearth, fireplace, 
glowing frying pan '. 

References: WP. I 563. other possibilities by W. Schuize Kl. Schr. 479. 
Page(s): 399 
(eval):1: == not found
```


## [2026-09-05T20:50:54.893Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=31100 && NR<=31240' POK_full.txt | head -80; echo \"=====LEMMA HEADERS=====\"; grep -n \"Root / lemma: ger\" POK_full.txt | head"
}
```


### [2026-09-05T20:50:57.933Z] TOOL RESULT

```
"scratch, scrape, grovel, truckle, creep'. Old Norse krafla^ grovel, truckle, creep ', krafsa 
"scratch, scrape, leicht anrijhren'. 

Maybe alb. kref, kreh (^ krefs) "comb, clean' 

with expressive intensification Danish Norwegian krabbe^ scratch, grapsen ' (and " 
scrabble, scribble, scrawl, scratch, grovel, truckle, creep ', originally " grovel, truckle, 
creep, while one gets stuck '), wherefore Old Norse krabbim.. Old English crabba. Middle 
Low German krabbe^ crab' and Old High German {krebiz), *krabita-, krebaz{o), asachs. 
krebit. Modern High German Krebs. - Ouite doubtful gr. ypopcpK; "sow' (better " the grunting 
'?) as nasal form. 

3. Besides *grb'^-{W\Vc\ expressive /?): 

Gr. YpicpaoGai ypacpsiv. /KdKUivzc,. oi 5£ ^usiv Koi apuaasiv Hes. (compare from sker-:gr. 
GKapTcpaoijai, Latin scrlbo), aypicpn, aypsTcpva " rake, gardening tool with a comb-like end; 
rack ' (a- from */?- "in', " carve, cut, mark by cutting or scratching '?); 



holl. kribbe/en' murmur', kr/be/en "\tch' , Middle High German md. knbe/n' kitzein (von 
der Sinuenlust) ', Modern High German kribbein, and with Germanic pp. Old High German 



kripfan^ rascfuIn^wieaemol^onacf^rBiTen ', Modern High German kripfen^ esp. of 
scratching a groove '; 

Latvian gnpsta^ scratch '. 

References: WP. I 606 f., Trautmann 87. 

See also: compare ^Teo^- "scratch, scrape', 57ei&^/;^o-5 "hornbeam". 

Page(s): 392 

Root / lemma: ger-1, gere- 
Meaning: to gather, put together 

Material: Gr. aysipu) (ayspw, HY^'Pa) gather; assemble' {*n-ger-Jd; a- weal< form from £v, 
also " collect, gather '?), gr. Doric a-^^t-mc, " collector, gatherer ', Aor. EypsTO " be 
gathered ', Infin. avpsoGai; ayopa, ayupic; "congregation, meeting', aYupTr|<; " collector, 
gatherer, beggar', a^oaioq, "hand, crooked, bent arm' (if from *a-YopaTO(;, with Aeolic op 
from r, for the formation compare naAaarn "flat hand'), YSPY^PC noAAa Hes., to YapYapci " 
swarm, flock; mass, crowd, heap'; 

broken reduplication *gre-g- in: 

Latin grex, gregism. "herd, troop, multitude, crowd'; 

Middle Irish graigu. (with secondary a). Gen. grega^ herd of horses ', cymr. corn. bret. 
gre6s:, because of Old Irish grafanni. " horse race ' {*grego-suendna) (common Celtic - 
ns-, -nt- > -nn-), barely borrowed from Latin; 

Maybe alb. {*grega) grigja " herd of sheep ' 

Balto-Slavic gur- from *gor- in: 

Lithuanian gurgulysm. " coagulation, thickening ', gurguolei. "bulk, mass, lump '; 
Maybe alb. gurgullonj^boW (liquid coagulation) ' 

Latvian gurste " bundle of flax ' {*gursti- from *gurt-sti-) = 

Maybe through metathesis alb. {*gursti) ^msM" handful, thin, emaciated; fist'; {*grisf) 
glisht, g/sM l\nger'. 

Slavic *gbrsfb in Old Church Slavic grbstb "fist, handful ', Old Russian gbrstb, Serbo- 
Croatian grst{P\. grsti) "hollow hand', poln. garsc6s., russ. gorstb6s.; russ. -Church Slavic 



pri-ghrbscai. ' handful ' {*gurstiS)\ Slavic *g-brtati bx\^ *ghrnQti {iroxw *ghrtnQti) in Serbo- 
Croatian grcem, grtati^ scrape together ', kir. pry-hortaty ds., poln. garnq'c6s.\ 

*gere- in Lithuanian gretaMv. " side by side, abreast '; 

remains far off Old Indie ^5/75/7 "troop, multitude, crowd', because not Indo Germanic 
(Kuiper Proto-Munda 54 f.). 

root extension grem-: 
=====LEMMA HEADERS=====
31075:Root / lemma: gerdo^- 
31136:Root / lemma: ger-1, gere- 
31216:Root / lemma: ger-2 
31336:Root / lemma: ger-3 
31503:Root / lemma: ger-3\ "to turn, wind' : Root/ lemma: (s)ker-3\ "to turn, bend'. 
31670:Root / lemma: ger-4, grei- 
34973:Root / lemma: gerrio^-, gixfo^- 
35605:Root / lemma: ger-, gera-, gre-
```


## [2026-09-05T20:51:03.194Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '31216,31245p' POK_full.txt; echo \"@@@@@\"; sed -n '35605,35625p' POK_full.txt; echo \"@@@@@\"; sed -n '35676,35690p' POK_full.txt"
}
```


### [2026-09-05T20:51:03.277Z] TOOL RESULT

```
Root / lemma: ger-2 

Meaning: to scream (in expr. forms) 

Material: A. Old Indicya/'a/e" it rushes, sounds, cracl<les, shouts \jara^ the rustling, 

murmuring ' (or to *gar- or *g"er-)\ perhaps gargara-h " a music instrument ' (yet see also 

*gal-\, 

alb. ngur6nJ^\\a\Ny (from wind); [actually hunguronJ^howX] 

Old Norse kaera, kaerda^ bring forward a matter, lodge a complaint, make a complaint to 
the proper authorities, accuse ' (derived from a lengthened gradeen /-stem *geri-)\ with 
consonant increase Old High German carron^ squeak, screech, clash, jangle, squeal, 
grate, jar, resound, rattle, creak ' (schw. V.), cherran {stem V.) "cry, creak'. Middle Low 
German kerren, karren ' creak' , Old English ceorran ' creak' {ceorung' lament, grumble, 
growl, complain, repine, snarl '), Norwegian karra^ coo, gaggle, cackle, chitchat, talk, 
snicker'. Old Norse kurra^ growl, murmur', kurr^ murmur, rumor'; 

Lithuanian gurti^ shrill, shriek, scream '; 

B. Here the name of crane: 

1. Lithuanian gerse^ crane, heron '; after Risch (briefl.) contaminated from gerve ar\6 
genser, 

2. With formants -en-, to part with -u- and -g- extended: 

Armenian krunk' crane ' {*geru-n-g-); compare under Old High German kranuh; 
@@@@@
Root / lemma: ger-, gera-, gre- 
Meaning: to rub; to be old; grain 

Note: also, esp. in formations with formants -no-, "corn, grain, seed ' (only NW-lndo 
Germanic); the oldest meaning seems to have been "rub' (hence " fruit grater, neatly 
pulverized, ground into fine particles; crushed '), intr.-pass. " become faded, from age or 
disease, malady'. 

Material: Old \x\6\c jarant-^ fragile, easily broken; unstable, dilapidated, old, graybeard' (= 
osset. zarond^o\(i\ gr. yspojv; compare also npers. zar^ graybeard, hag '),ya/'a//" makes 
fragile, easily broken; unstable, dilapidated, allows to grow old ' ("*rub, chafe '), jarana-^ 
frail, o\(i\jaras-i. (Nom. Sq. jarah, Indo Germanic -os) and Jam ^ age, grow older, 
senescence, aging process, process of growing older, age'; redupl. jarjara- "frail, 
breakable, decrepit ' (: gr. Y£pY£pi|jO(;); lengthened grade yara- " aging, maturing; growing 
older ' (= npers. za/'"weak, woeful, wretched, miserable ', zar^ graybeard, hag '; also in 
Aor. jarisuh); heavy basis in Old \n6\c Jar/man- m. " old age, senility ', jTryati, juryatT 
become fragile, easily broken; unstable, dilapidated, rotten, decayed, decomposed; brittle, 
grows old ', participle yi7/77a-, y7/77a- " fragile, easily broken; unstable, dilapidated, decrepit, 
antiquated, worn out, old, decompose, rotten, decayed, decomposed; brittle, old'; Avestan 
azarssant-^ noi aging, maturing ' (participle of s-Aor.), azarsma-'not decreasing, 
lessening, diminishing, declining ' (from *zarama-rr\. "the abandoned, depraved, unkempt, 
@@@@@
*graros {*gr-r6s) " pulverized, ground into fine particles; crushed ' is continual probably in 
Latin glarea {* grareja) ' gravel '; o'-present 'ig/'d-o'd perhaps in Gothic ^5/r/io/d/7 ' crunch '. 

References: WP. I 599 f., WH. I 605 f., 618 f., Trautmann 371 f., Schwyzer Gr. Gr. I 514, 
574, 682 under Anm. 5. 
Page(s): 390-391 

Root / lemma: geus- 

Meaning: to taste; to enjoy [' savor, enjoy, taste ', in the Germanic and Celtic 'choose', in 

Indo Iran, and Alban. 'love'] 

Material: Old \nd'\c Josat/, Jusate ' tastes, enjoys, loves 'Josayate^^here one finds
```


## [2026-09-05T20:51:17.922Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in POK_01.txt POK_02.txt POK_03.txt; do echo \"== $f\"; grep -n \"wach werden\\|heiser schreien\" $f | head; done"
}
```


## [2026-09-05T20:51:19.566Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"wigrās\\|wigras\\|wyglʾs\\|wygls\\|wigrāy\\|wixrās\" PHD.txt PHD_mackenzie.txt NYB_vol2_glossary.txt | head -20"
}
```


### [2026-09-05T20:51:19.603Z] TOOL RESULT

```
== POK_01.txt
== POK_02.txt
3561:mit  Geminata  -kk- idän.  skrukke  ,glucksen',  skrokke  ,plaudern',  woneben älter  dän.  krokke  , rufen,  von  Hühnern',  mnd.  krochen  ,grunzen;  heiser schreien  (vom  Raben)'.
== POK_03.txt
```


### [2026-09-05T20:51:19.670Z] TOOL RESULT

```
PHD.txt:384:ёгбһ [glwh | N guroh] group, crowd. gubrág [gwpl’k'] awake, alert, vigilant. ģubrās- [gwp/”s-] = wigras-, v. wigrádan. ģuftan, $0(w)- [YMRRWN-, YMLLWN-tn! < A ymlwn, V тЇ; gwptn', gwb- | M gwptn, gw-, N ~, gā(y)-] say, speak. ~išn: speech. ģuftār [gwpt?] | N ~] speaker. ~ih: (power of) speech. gugiin- [gwk’n- | M gwg^n-] destroy. gugar(i)dan, gugar- [gwk”/-(y)tn! | N guwár-idan] digest. tuģāy [gwk*dy | M gwg'y, N guwah] witness. ~ih: testimony. ģūh [gwh | N —] dung, excrement. guhrayénidan, guhrayén- [gw AP yn-ytn!] waken, arouse. gul [gwl | N ~] flower, rose. ботап [gwnmn! | = M, N ~] doubt. ~par [-A/] casting doubt. ~ig [-yk'] doubtful. ~ih, ~igih: doubt. gumardag [gwmltk'] appointee, deputy. ģumārdan, gumār- [gwm’l-tn' | М gwm'r-dn, N gumāštan, gumar-] appoint, commission, entrust. gumbad [gwmbt' | N ~] dome, fire-temple. £umég [gwmyk! | M gwmyg] mixture. guméxtan, gumēz- [gx”myhtn!, gwmyc- | M gwmyxtn, gwmyz-] mix. ~išn: mixing, mixture; = gumézagih. gumëzag [gwmyck'] mixture. ~th: the Mixture, (the duration of) this material world. Jgund [gwnd | = P] army, troop; group, gathering. *gund [gwnd | N ~] testicle. gung [g(w)ng | N ~] dumb. ģurbaģ [gwibk! | N ~a] cat. Бита [gwlt! | P gwrd, N ~] hero. lih: heroism, bravery. gurdag [gwltk! | N ~a] kidney. *gurdih [ewityh] (some piece of) armour. gurdwār [gwltw’!] befitting a hero. ёпгр [gwlg | N ~] wolf. gurganig [gw/g”nyk! | N ~i] of (the province) Gurgan. gursag [ewlsk] | N gurusna !] hungry. «ЛЬ: hunger. Suën [gvfn! | N ~] male. gusnag [gwšnk! | J gušna] hungry. Gušnasp [gwšn(*)sf] the second major Fire of Sasanian Eran, that of warriors. £yà$ [gyw'k! | M gy'g, N jay] place.
PHD.txt:651:wénig [wynyk! | M wynyg, N bini] nose. wénO£ [wynwk' | N bunü] lentil. wēš [zoy£ | = M, N béf] more. wé&ag [wysR! | N beta] thicket, wood. --estün [-st?n'] woodland. ~ig [-yk'] silvan. wēwag [wdpk! | N béwa] widow. 1wéxtan, wez- [NSSHWN-tn! < А V nsh; wyhtn', wyc- | P wyxt-, N bextan, béz-] sift, select, choose, separate, cleanse, purify, winnow. ~išn: selection. *wēxtan, wēz- [wyhtn!, wyc-] swing, brandish, throw, pour out. Wīdadafš [wydtpš = Av. wīdašafšū-| the south-western continent of the earth. widang [wtng | P wdng] trouble, distress, constraint. widār [xt' | N gudár] passage, entrance. widarag [wtlg | M wdr, N guàar] path, passage. widardan, wider- [wtitn!, wt(y)l- | M wd(y)r-, N guóar-] pass (by, away), cross, die. : ~išn(īh): passage, crossing, death. ~i$nig : transient. widārdan, widār- [xwt?/-tn! | M wyd’r-, N guóárdan] let pass, transport; endure, suffer. widārīdan [w?lytn'] = widardan. widaštan [wtstn' | N gušaštan] = widardan. widāxtan, widāz- [wt’hin', wtc- | (P wd’c-), N gudaxtan, gudāz-| melt, dissolve. widāzīhistan, widazih- [wt’cyh-stn'] be melted, dissolved. wider- , -išn(-īģ, -ih), v. widardan. widerān [wt(y)?n! | N guóarán) transient, dying. widest [zot(y)st! | N bidast] (hand) span (9 in.). ~ig [-yk'] span-sized, midget. widimās [wtym’s | (M wyd’m’s)] wonder, miracle. ~ig [-уА!] wonderful. ~ih: miracle. widimušt [wtymust | M wd(y)mwšt] astonished. ~ih: astonishment. *widwar [wytwl] contented, resigned, consoled. ~ih: contentment, resignation, consolation. wiftag [wyptk'] passive sodomite. wigrad [zogPt! | N bīdār] awake, alert. wigradan, wigras- [zog tn, wgl’s- | M wygr'd, wygr’s-] awaken, rouse. ~i$n(ih): awakening. wih-, v. wistan. wihan(ag) [zh?n(k)', (b-) | M wl?ng, N bahāna] cause, reason. wihēz- [wyhyc- | M twhyz-] move, progress. wihéz(ag) [wyhyc(k')] movement, progression.
PHD.txt:907:awake gubrag, wigrad. awaken wigradan; v. (a) rouse. awakening wigrāsišn(īh). aware agah.
PHD.txt:5222:nil, wir wirāy- wirāyišnīh wirāyišn wirdmandih wigrās- wigrāsišnīh
PHD_mackenzie.txt:2590:gubras- [gwpl's-] = wigras-, v. wigradan.
PHD_mackenzie.txt:5369:wigradan, wigras- [wgl'tn', wgZ>s- I M wygr'd, wygr's-] awaken, rouse.
PHD_mackenzie.txt:10244:wigras-
```


## [2026-09-05T20:51:39.284Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== HRN bīdār\"; grep -n -i \"bîdâr\\|bīdār\\|bidâr\\|bidār\\|vigrâd\\|vigrād\\|vīgrāδ\" HRN.txt | head; echo \"== HUB\"; grep -n -i \"bidâr\\|bīdār\\|bidār\\|vīγrāδ\\|vigrā\" HUB.txt | head; echo \"== HRN 143 area zar\"; grep -n \"zâr\\|zār\" HRN.txt | head -30"
}
```


### [2026-09-05T20:51:39.417Z] TOOL RESULT

```
== HRN bīdār
== HUB
== HRN 143 area zar
```


## [2026-09-05T20:51:40.702Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== CHEUNG gar/awake\"; grep -n \"gar\\b\" CHEUNG.txt | head -20; echo \"== CHEUNG *gar\"; grep -n \"^\\*gar\\|\\*gar 1\\|\\*gar 2\\|\\*gar 3\" CHEUNG.txt | head -20"
}
```


### [2026-09-05T20:51:40.784Z] TOOL RESULT

```
== CHEUNG gar/awake
291:l'ormuri de Baraki-Barak (Logar, Afghanistan)” (2003), and last, but not least, 
350:° Т only recently discovered that the root *gar” ‘to be/make warm’ has been preserved as verb in Oss. 
1558:‘shattered’, (?) Olrish -aid-begar ‘is dissolved’ 
3408:kindle, light a fire’, cited by Abaev, Le: 158 f. They rather contain the root *gar’ ‘to 
7652:*gar! ‘to rejoice’ 
7676:*gar? ‘to turn, wind’ 
7688:*NWIR: Kurd. (Kurm.) garin/gar-, (Sor.) garan/garé- ‘to wander, go (round), roam’, 
7698:*gart and *gar£". 
7707:* gar! ‘to heat, cook, kindle fire’ 
7721:основы *jara- от корня *gar- ‘гореть, xxeup'". 
7725:The verbal forms of *gar’ are only found in some modern Iranian dialects. The old 
7732:Lith. garéti ‘to burn’, Goth. brinnan, Engl. to burn, Alb. zien ‘cooks’, etc. 
7739:*gar^ ? ‘to coagulate, stiffen’ 
7749:9 In view of the very limited evidence, the existence of an Ir. root *gar- ‘to 
7819:*AVESTAN: (+ *abi-) YAv. auui gar- ‘to praise’ || (+ *a-) YAv. äyar- ‘to greet’ 
7845:‘curse, abuse’ || (+ *а-) NP алт (aZer) ‘cry, call’ (dial. borr.) || (+ *uz-) NP Zagar 
7849:assumed by Hasandoust, l.c. || NP Zagar ‘out-cry’ is probably a borrowing from 
7860:*SANSKRIT: gar ‘to praise, honour, welcome’ > EWAia I: 468 
7877:* gar? *to throw? 
7899:can also be interpreted as gar-zen *'throwing weapon’ ? 
== CHEUNG *gar
7652:*gar! ‘to rejoice’ 
7676:*gar? ‘to turn, wind’ 
7685:*gar4 ? 105 
7698:*gart and *gar£". 
7739:*gar^ ? ‘to coagulate, stiffen’ 
7817:*garH! ‘to greet, call’ 
7935:*garjl ? 109 
8002:*garf? ? ‘to assemble, gather’ 
8035:*garš2 ? ‘to knead, rub (?)’ 
8055:*gart ‘to turn’ 
8067:*garz 111 
8100:*gar”. It has probably been influenced by *yart. 
8113:*garz ‘to lament, weep’ 
55366:*gar', *gäz (s.v.), *Hram 
55495:*garH? (s.v.), *haic, *nab 
55517:*gar* (s.v.), *gauz (s.v.), 
55735:*gar’, *starH’, *stamb(H), 
55889:*garH!, *gauH, *huanH, 
55897:*garH? (s.v.), *Haz (s.v.), 
55984:*gart (s.v.), *Hmai’, *harH
```


## [2026-09-05T20:51:48.300Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && wc -l HRN.txt HUB.txt CHEUNG.txt && sed -n '1,15p' HRN.txt && echo \"=== search zar in HRN\" && grep -n -i \"zâr\\|zar,\" HRN.txt | head -20"
}
```


### [2026-09-05T20:51:48.367Z] TOOL RESULT

```
  23313 HRN.txt
  10982 HUB.txt
  58427 CHEUNG.txt
  92722 total
Google
This is a digital copy of a book that was prcscrvod for gcncrations on library shclvcs bcforc it was carcfully scannod by Google as pari of a projcct
to make the world's books discoverablc online.
It has survived long enough for the Copyright to expire and the book to enter the public domain. A public domain book is one that was never subject
to Copyright or whose legal Copyright term has expired. Whether a book is in the public domain may vary country to country. Public domain books
are our gateways to the past, representing a wealth of history, cultuie and knowledge that's often difficult to discover.
Marks, notations and other maiginalia present in the original volume will appear in this flle - a reminder of this book's long journcy from the
publisher to a library and finally to you.
Usage guidelines
Google is proud to partner with libraries to digitize public domain materials and make them widely accessible. Public domain books belong to the
public and we are merely their custodians. Nevertheless, this work is expensive, so in order to keep providing this resource, we have taken Steps to
prcvcnt abuse by commcrcial parties, including placing technical restrictions on automatcd qucrying.
We also ask that you:
+ Make non-commercial use ofthefiles We designed Google Book Search for use by individuals, and we request that you use these files for
personal, non-commercial purposes.
=== search zar in HRN
3543:arab. LW. tazar,
5801:'Gold'; phlv. zar, zartn; ai. hdri-, hiranya-,
```


## [2026-09-05T20:51:49.113Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '8113,8160p' CHEUNG.txt; echo \"=== awake\"; grep -n -i \"to be awake\\|'awake'\\|to wake\" CHEUNG.txt | head -20"
}
```


### [2026-09-05T20:51:49.187Z] TOOL RESULT

```
*garz ‘to lament, weep’ 

*AVESTAN: goroz- ‘to lament, weep’ => Liste: 19f. 

Pres. {1} athem.: IND. med. 1sg. OAv. garazdi/garazé (Y 32.9, Y 46.2), INJ. med. 3sg. OAv. garazda (Y 
29.1); Pres. {2} athem. red.: INJ. 3р1. OAv. (tr.!) jigorozat (Y 32.13); Pres. {3} them.: IND. med. 35р. 
YAv. gorozaite (Yt 10.53), OPT. med. 35р. YAv. gorezaeta (Yt 17.57 ff); Partic.: pres. {1} ҮАУ. 
%әгәғапа- 


112 *gau (*jau) 


*MIDDLE PERSIAN: MMP gry-, BMP gl(y)dy- /griy-/ ‘to weep’ (< OP *grad-ya-) || 
BMP glc- /garz-/ ‘to weep, lament’? (LW) || (+ *upa-) MMP ’bgrysn ‘moaning, 
crying’? = DMMPP: 164a, 10b 

Well attested: Pres.: IND. Isg. MMP gryym, 3sg. MMP “gryyd, 1р1. MMP gryy’m, 3pl. MMP gryynd, 
BMP glydynd, gldynd /griyénd/, BMP glcynd /garzénd/, SUBJ. 152. MMP gryy’n, etc. 

*PARTHIAN: grzysn ‘complaint’? = DMMPP: 165b 

*BACTRIAN: yipC- ‘to complain’ = S-W, Bact.: 189a 

*NWIR: NP giristan/giriy- ‘to weep’, NP gilah ‘complaint; lamentation’, Kurd. 
(Kurm.) giriZin/giriz- ‘to be grumpy, grumble, growl’, Awrom. gırawäy/gıraw- 
(LW), Bakht. girévistan “о weep, cry’, Gz. griye ‘weeping, lamenting’, Siv. ger-, 
gir-/gerd, gird ‘to lament’ 

*NEIR: Oss. I. qerzyn/qerzt, D. Serzun/gerzt ‘to groan’, Oss. I. gast, D. gast (orig. 
ppp. ?) ‘complaint, grief? 

*SANSKRIT: garh ‘to complain’ (RV+) = EWAia I: 475, 495 

9 An IE origin of this common IIr. root is uncertain. The Germanic and Irish forms 
cited by Pokorny (1.с.), OHG chlaga ‘complaint’, chlagön ‘to complain’ (etc.) and 
Olrish glam ‘cry, curse’, are probably from a substrate source, on which see 
Boutkan — Siebinga: 216. 

«PIE? > LIV: 187 | Pok.: 350 f. 


“IE COGNATES: — 
«REFERENCES: Horn 1893: 208, 204; MacKenzie 1966: 95; Abaev, Slovar’ П: 296 f., 269 Ё; WIM II/2: 
668; Vahman — Asatrian 1987: 90; WIM III: 108; Werba 1997: 179; Cabolov 2001: 386 


*gau (*Jau) ‘to increase’ 
=== awake
2147:(+ *fra-) ‘to wake up’ — Liste: 39 
2192:*SANSKRIT: bodh ‘to wake, awaken; to perceive, notice, heed’ (RV+) = EWAia II: 
11856:*Hgar ‘to be awake’ 
11858:*AVESTAN: YAv. yar- ‘to guard, watch’ || (+ *а-) caus. ‘to wake up [tr.]’ || (+ *fra-) 
11859:inch. ‘to awake’, caus. ‘to wake up [tr.]’ — Liste: 19 
11866:*MIDDLE PERSIAN: (+ *ui-) MMP wygr's-, BMP wgl’s- /wigras-/ ‘to wake, awaken’ 
11876:*PARTHIAN: (+ *ui-) wygr’s- ‘to wake, awaken’ || (+ *ham-) ’ngrysn ‘meditation’ 
11883:CSogd. wyr’s (intr./inch.) ‘to wake’, CSogd. wyrys, Sogd. wyr’ys (caus.-inch.) ‘to 
11890:*CHORESMIAN: y'r- ‘to protect, guard’, m/yr’s- (inch.) ‘to be awake, awake’ 
11893:*NWIR: Bal. gurit/gur- ‘to wake up with a start’ (with sec. -r-) || (+ *ui-) NP bidar, 
11897:yürayS-/yüraySta (caus.-inch.) ‘to wake up’, Oss. I. qal, D. igal ‘awake’ || (+ *ham-) 
11901:*SANSKRIT: jar ‘to wake up’ (RV+) > EWAia I: 574 
11909:«PIE *Higer- ‘to wake up’ = LIV: 245 | Pok.: 390 
11912:*IE COGNATES: Gr. £yeípo ‘I watch, to wake’, Alb. поте ‘to lift, to wake’ 
25445:*CHORESMIAN: (+ *fra-) т/гӨт- ‘to wake up’, mrO’my- (caus.) ‘to wake" = Samadi: 
30153:biysen- (biyan-) ‘to wake up’, OKh. biysañ- (caus.) ‘to waken? = SGS: 112, 119, 
55267:to be awake, 
58286:to wake up,
```


## [2026-09-05T20:51:52.990Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '11856,11915p' CHEUNG.txt"
}
```


### [2026-09-05T20:51:53.061Z] TOOL RESULT

```
*Hgar ‘to be awake’ 

*AVESTAN: YAv. yar- ‘to guard, watch’ || (+ *а-) caus. ‘to wake up [tr.]’ || (+ *fra-) 
inch. ‘to awake’, caus. ‘to wake up [tr.]’ — Liste: 19 

Perf.: IND. 3sg. YAv. jayara ‘is watching’ (N 19); Partic.: pres. inch. med. ? YAv. frayrisomna- (H 1.13), 
pres. caus. YAv. "fra. yäraiiant- (N 19), perf. YAv. jayauruuah- (Yt 10.7, etc.); Caus.: pres. IND. Isg. 
Y Av. а... gäraiiemi (Any 2), 3sg. YAv. “fra. yaraiieiti (V 18.22, N 19), OPT. 25р. YAv. fra gäraiiöis (N 
19) 

*MIDDLE PERSIAN: (+ *ui-) MMP wygr's-, BMP wgl’s- /wigras-/ ‘to wake, awaken’ 
=> DMMPP: 353b 

(+ *ui-) Pres.: IND. 3pl. BMP wgl’synd /wigrasénd/; Partic.: perf. pass. MMP wygr’d; Caus.: pres. 3sg. 
MMP "wygr'synyd, partic. MMP wygr'syn'g 


*Hhaus 173 


*PARTHIAN: (+ *ui-) wygr’s- ‘to wake, awaken’ || (+ *ham-) ’ngrysn ‘meditation’ 
= Ghilain: 82, 92 | DMMPP: 353b, 48a 

(+ *ui-) Pres.: SUBJ. 2sg. wygr’s’, IMPV. 2sg. wygr’s, 2pl. wygr’syd, 2pl. wygr’syd; Partic.: perf. pass. 
wygr’d(g), Caus.: pres. IND. 3sg. wygr’nyd 

*SOGDIAN: BSogd. y’r ‘to watch, guard’ || (+ *ui-) SSogd. wyr’s, BSogd. wyy’r’s, 
CSogd. wyr’s (intr./inch.) ‘to wake’, CSogd. wyrys, Sogd. wyr’ys (caus.-inch.) ‘to 
wake up, arouse’ 

Pres.: IND. 3pl. BSogd. y’r’nt || (+ *ui-) Well attested: Pres.: SUBJ. 3sg. BSogd. wyy’r’s’, IMPV. 2sg. 
SSogd. wyr’s (Sogd. Tales: 478), 2р1. CSogd. wyr’stt, Pret.: IND. 3pl. intr. MSogd. wyyr’tnd, etc. 


*CHORESMIAN: y'r- ‘to protect, guard’, m/yr’s- (inch.) ‘to be awake, awake’ 
c» Samadi: 75, 78 f. 

*NWIR: Bal. gurit/gur- ‘to wake up with a start’ (with sec. -r-) || (+ *ui-) NP bidar, 
Abyan. biyar, Gz. biyar, Jow. vi:dá:r ‘awake’ (with metath. & loss of -y- < *uryrad) 
*NEIR: Yzgh. Zir-/Zird ‘to think’, Yghn. yor- ‘to see’ (*Hgarua- ?) || (+ *uz-) Pash. 
zyör-, Zyör- ‘to guard, protect’ || (+ *ui-) Yghn. yürös-/yüröta (inch.) ‘to awake’, 
yürayS-/yüraySta (caus.-inch.) ‘to wake up’, Oss. I. qal, D. igal ‘awake’ || (+ *ham-) 
Oss. I. enqalyn/znqald, D. engzlun/engald ‘to suppose, think; to hope for’ (orig. 
*ja-pass.) || (+ *ham- ?) Pash. goral ‘to see’ 

*SANSKRIT: jar ‘to wake up’ (RV+) > EWAia I: 574 

Q According to Klingenschmitt 1982: 77, fn. 18, Iranian also continues a variant 
*H;greH- (i.e. Plr.*HgraH-) on account of Av. frayratu- ‘awakening’. This 
"variant", notably attested in inchoative formations, may actually reflect a formation 
with the IE suffix *-eH;- or *-eH;-. Av. frayratu- possibly goes back to (quasi-)IE 
*pro-H,grotu- ? 

«PIE *Higer- ‘to wake up’ = LIV: 245 | Pok.: 390 


*IE COGNATES: Gr. £yeípo ‘I watch, to wake’, Alb. поте ‘to lift, to wake’ 

*REFERENCES: KPF I: 147b; EVP: 23, 101, 11; Christensen, Contributions I: 157, 257; Lambton 1938: 
75b, 41b, 77b; Morgenstierne 1942: 98; Abaev, Slovar’ I: 162 ff., Andreev — PeSéereva: 258b, 259b f.;
```


## [2026-09-05T20:52:21.083Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -A18 \"^ger.-2\\|ger.-2\\. To cry\" AHD_watkins1985.txt | head -40; echo \"=== ger awake\"; grep -n -B2 -A12 \"To awake\\|ger-3\\|gerbh\" AHD_watkins1985.txt | head -60"
}
```


### [2026-09-05T20:52:21.163Z] TOOL RESULT

```
<persisted-output>
Output too large (36.3KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/tool-results/b5x6clv2m.txt

Preview (first 2KB):
494:vine, grape: GRAPE; c. Old French grapon, grapnel: GRAPNEL; d. Old French grape, a hook: GRAPPLE; e. Ital- ian dialectal grappa, vine stem, brandy: GRAPPA. 2. Old English crump, crumb, crooked, bent, stooping: CRUM- MIE, CRUMPET, (CRUMPLE). 3. Low German krimpen, to wrinkle: CRIMP!. 4. Middle Dutch crampe, hook, and Frankish *kramp, hook: cramMpP?. 5.Old High German krampfo, a cramp, akin to the Germanic source of Old French crampe, cramp: CRAMP!. 6. Old English crypel, a cripple: CRIPPLE. 7. Germanic *kreupan in Old English créopan, to creep: CREEP. 8. Middle Low German krink, a ring: CRINGLE. 9. Germanic *krengan in Old English cringan, to yield: CRINGE. 10. Middle Dutch crinkelen, akin to Middle English crinkelen, to make kinks in: CRINKLE. 11. Old Norse kriki, a bend, nook: CREEK. 12. Old Norse krékr, a hook: cRooOK. 13. Frankish *krok- (> Old French croc), a hook: CROCHET, (CROCKET), (CROQUET), (CROUCH); ENCROACH. 14. Old English crycc, (bent) staff, crutch: CRUTCH. 15. Old French crosse, crook: CROSIER, LACROSSE. 16. Middle Dutch crulle, curly: CRULLER, CURL. 17. Old English cranc-(stzf), a weaving implement: CRANK}. 18. Norwegian krake, a sickly beast, akin to the source of Middle English crok, an old ewe: cRocK3, 19. Old Norse karpa, to boast: CaRP!, 20. Middle Dutch kroes, curled, akin to the source of Old French grosele, gooseberry: GROSSULARITE. II. Words meaning ‘“‘a rounded mass, collection; a round object, vessel, container.” 1. Old English cruma, a frag- ment: CRUMB. 2. Frankish *kruppa, rump, akin to the Germanic source of Old French croup, rump: CROUP?, (CROUPIER), CRUPPER. 3. Old English cropp, cluster, bunch, ear of corn: crop. 4. Italian gruppo, an assem- blage: Group. 5. Old English crocc, pot: CROCK}. 6, Mid- dle Dutch cruyse, pot: CRUSE. 7. Old English cribb, manger: CRIB. 8. Old English cradel, cradle: CRADLE. 9. Frankish *kripja, cradle, akin to the Germanic source of Old French cre(s)che, crib: CRECHE. 10. Old English creet and Old Nors
...
</persisted-output>
```


## [2026-09-05T20:52:24.413Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"cry hoarsely\" AHD_watkins1985.txt | head; echo ===; grep -n \"GERANIUM\\|geranos\\|To awake\" AHD_watkins1985.txt | head"
}
```


### [2026-09-05T20:52:24.470Z] TOOL RESULT

```
Exit code 1
494:vine, grape: GRAPE; c. Old French grapon, grapnel: GRAPNEL; d. Old French grape, a hook: GRAPPLE; e. Ital- ian dialectal grappa, vine stem, brandy: GRAPPA. 2. Old English crump, crumb, crooked, bent, stooping: CRUM- MIE, CRUMPET, (CRUMPLE). 3. Low German krimpen, to wrinkle: CRIMP!. 4. Middle Dutch crampe, hook, and Frankish *kramp, hook: cramMpP?. 5.Old High German krampfo, a cramp, akin to the Germanic source of Old French crampe, cramp: CRAMP!. 6. Old English crypel, a cripple: CRIPPLE. 7. Germanic *kreupan in Old English créopan, to creep: CREEP. 8. Middle Low German krink, a ring: CRINGLE. 9. Germanic *krengan in Old English cringan, to yield: CRINGE. 10. Middle Dutch crinkelen, akin to Middle English crinkelen, to make kinks in: CRINKLE. 11. Old Norse kriki, a bend, nook: CREEK. 12. Old Norse krékr, a hook: cRooOK. 13. Frankish *krok- (> Old French croc), a hook: CROCHET, (CROCKET), (CROQUET), (CROUCH); ENCROACH. 14. Old English crycc, (bent) staff, crutch: CRUTCH. 15. Old French crosse, crook: CROSIER, LACROSSE. 16. Middle Dutch crulle, curly: CRULLER, CURL. 17. Old English cranc-(stzf), a weaving implement: CRANK}. 18. Norwegian krake, a sickly beast, akin to the source of Middle English crok, an old ewe: cRocK3, 19. Old Norse karpa, to boast: CaRP!, 20. Middle Dutch kroes, curled, akin to the source of Old French grosele, gooseberry: GROSSULARITE. II. Words meaning ‘“‘a rounded mass, collection; a round object, vessel, container.” 1. Old English cruma, a frag- ment: CRUMB. 2. Frankish *kruppa, rump, akin to the Germanic source of Old French croup, rump: CROUP?, (CROUPIER), CRUPPER. 3. Old English cropp, cluster, bunch, ear of corn: crop. 4. Italian gruppo, an assem- blage: Group. 5. Old English crocc, pot: CROCK}. 6, Mid- dle Dutch cruyse, pot: CRUSE. 7. Old English cribb, manger: CRIB. 8. Old English cradel, cradle: CRADLE. 9. Frankish *kripja, cradle, akin to the Germanic source of Old French cre(s)che, crib: CRECHE. 10. Old English creet and Old Norse kartr, wagon: CART. 11. Old English croft, small enclosed field: crort. [Pok. 3. ger- 385.] gerbh-. To scratch. 1. Germanic *kerban in Old English ceorfan, to cut: CARVE. 2. Zero-grade Germanic form *kurbiz in Old English cyrf, a cutting (off): KERF. 3. Variant form *grebh- in: a. Germanic *krab(b)- in Old English crabba, a crab: CRAB}; b. Germanic *krabiz- in Old French crevise, crayfish: CRAYFISH; C. perhaps Ger- manic *krab- in Old Norse krafla, to crawl: CRAWL. 4. Zero-grade form *grbh- in Greek graphein, to scratch, draw, write, and gramma (< *grbh-mn), a picture, writ- ten letter, piece of writing, and grammé, a line: GRAF- FITO, GRAM!, -GRAM, GRAMMAR, GRAPH, -GRAPH, -GRAPHER, GRAPHIC, -GRAPHY; AGRAPHA, AGRAPHIA, DIAGRAM, EPIGRAM, (EPIGRAPH), GRAPHITE, ICONOGRA- PHY, PARAGRAPH, PROGRAM, PSEUDEPIGRAPHA, TETRA- GRAMMATON, TOPOGRAPHY. [Pok. gerebh- 392.] [gerere. To carry, carry on, act, do. Latin verb of un- known origin. Oldest form ges-, past participle gestus. GERENT, GERUND, (GEST), GESTATION, (GESTICULATE), GESTURE, JEST; ARMIGER, BELLIGERENT, (CONGERIES), CONGEST, DIGEST, EGEST, INGEST, REGISTER, SUGGEST, VELIGER.] gere-'. To grow old. 1. Suffixed lengthened-grade form *géro-s- in Greek géras, old age: AGERATUM, CALOYER, GERIATRICS. 2. Suffixed form “gera-ont- in Greek geron (stem geront-), old man: GERONTO-. [Pok. ger- 390.] gere-2. To cry hoarsely; also the name of the crane. I, Words meaning “‘to cry hoarsely”; also words denoting the crow. 1, Germanic *kré- in: a. Old English crawe, a crow: CROW}; b. Old English crdwan, to crow: CROW?; c. Old English cracian, to resound: CRACK; d. Middle Dutch krdken, to crack: CRACKNEL; @. Old Norse kraka, a crow: CRAKE. f. Middle Dutch krdnen, to groan, la- ment: CROON. 2. Possibly (but more likely imitative) Germanic *kur(r)- in Old Norse kurra, to growl, akin to Middle English curre, cur: cur. II. Words denoting a
(eval):1: == not found
```


## [2026-09-05T20:52:34.704Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('AHD_watkins1985.txt',encoding='utf-8',errors='replace').read()\ni=t.find('gera-2. To cry hoarsely')\nif i<0: i=t.find('To cry hoarsely')\nprint(t[i:i+2200])\nprint('======GREGORY======')\nfor m in re.finditer('GREGORIOUS|Gregory|GREGARIOUS|egeirein|grégoros|EGERSIS',t):\n    print(t[max(0,m.start()-600):m.start()+400])\n    print('---')\nEOF"
}
```


### [2026-09-05T20:52:36.767Z] TOOL RESULT

```
To cry hoarsely; also the name of the crane. I, Words meaning “‘to cry hoarsely”; also words denoting the crow. 1, Germanic *kré- in: a. Old English crawe, a crow: CROW}; b. Old English crdwan, to crow: CROW?; c. Old English cracian, to resound: CRACK; d. Middle Dutch krdken, to crack: CRACKNEL; @. Old Norse kraka, a crow: CRAKE. f. Middle Dutch krdnen, to groan, la- ment: CROON. 2. Possibly (but more likely imitative) Germanic *kur(r)- in Old Norse kurra, to growl, akin to Middle English curre, cur: cur. II. Words denoting a
20
ghait-
crane. 1. Germanic *kran-, crane, in: a. Old English cran, crane: CRANE; b. Middle Low German kran, crane: CRANBERRY. 2. Extended form *grd- in Latin griis, crane: GRUS; PEDIGREE. 3. Suffixed variant form *gra-k- in Latin grdculus, jackdaw: GRACKLE. 4. Suffixed ex- tended form *gero-no- in Greek geranos, crane: GERA- nium. [Pok. 2. ger- 383.]
géu-. To bend. Proposed by some as the root of Greek guros, ring (which is more likely of unknown origin): GYRE, GYRO?, GYRO-; AUTOGIRO. [Pok. géu- 393.]
geue-. To hasten. Possibly the base of Germanic *kaur- Jan in Old Norse keyra, to drive: SKIJORING. [Pok. geu- 399.]
g(e)u-lo-. A glowing coal. Germanic *kulam, *kolam in: a. Old English col, a glowing coal: COAL, (COLLIE), (COL- LIER); b. probably dialectal Old French cholle, round lump, head: cHOLLA. [Pok. g(e)u-lo- 399.]
geus-. To taste, choose. 1. Germanic *keusan in: a. Old English céosan, cedsan, to choose: CHOOSE. b. Gothic *kausjan, to choose: CHOICE. 2. Zero-grade *gus- in Germanic *kuz-, becoming *kur- in Old Norse Valkyrja, “chooser of the slain,” Valkyrie (valr, the slain; see wele-2). 3. Suffixed zero-grade form *gus-tu- in: a. Latin gustus, taste: (GUST?), GUSTO; DISGUST, RAGOUT; b. Latin gustdre, to taste: DEGUST. [Pok. geus- 399.]
ghabh-. Also ghebh-. To give or receive. 1. Form *ghebh- in Germanic *geban in: a. Old English giefan, to give: GIVE; b. compound *far-geban (*far-, away; see per'), to give away, in Old English forgi(e)fan, to give, give up, leave off (anger), remit, forgive: FORGIVE. 2. Suf- fixed form *ghebh-ti-, something given (or received), in Germanic “giftiz in Old Norse gipt, gift, a gift: GIFT. 3. O-grade
======GREGORY======
thos, jaw: GNATHIC, -GNATHOUS; CHAETOGNATH 4, Variant form “g(h)enu- in Sanskrit hanu, jaw: HANUMAN. [Pok. 2. genu- 381.] gep(h)-. Also gebh-. Jaw, mouth. 1. Probably Germanic *kaf-, to gnaw, chew, in Old English ceaf, husks, chaff: CHAFF!, 2. Germanic *kabraz, “gnawer,” in Old English ceafor, ceafer, beetle: CHAFER; (COCKCHAFER). 3. Ger- manic *kéfalaz in Old English céafl, jaw, cheek: JOWL!. [Pok. geph-, gebh- 382.] ger-'. To gather. 1. Extended form *grem- in Germanic *kram- in Old English crammian, to stuff, cram: CRAM. 2. Reduplicated form *gre-g- in Latin grex (stem greg-), herd, flock: GREGARIOUS; AGGREGATE, CONGREGATE, EGREGIOUS, SEGREGATE. 3. Earliest forms “ager-, *ggor-d-, in Greek ageirein, to assemble, and aguris, agora, marketplace (> agoreuein, to speak): AGORA}; (AGORAPHOBIA), ALLEGORY, CATEGORY, PANEGYRIC. [Pok. 1. ger- 382.] ger-2. Curving, crooked; hypothetical Indo-European base for a variety of Germanic words with initial kr-. I. Words meaning to bend, curl; bent, 
---
LA gfe-no- GRANARY gre-no- GRANDILOQUENCE tolkw- GRANGE gre-no- GRANITE gr@-no- GRANT kerd-1 GRANULE gre-no- GRAPE ger-2 GRAPH gerbh- -GRAPH gerbh- -GRAPHER gerbh- GRAPHIC gerbh- GRAPHITE gerbh- -GRAPHY gerbh- GRAPNEL ger-2 GRAPPA ger-2 GRAPPLE ger-2 GRASP ghrebh-1 GRAss_ ghré- GRATE! grat- GRATE? kert- GRATEFUL gWere-3 GRATIFY gWere-3 GRATIS gWera-3 GRATITUDE gWero-3 GRATUITY gWera-3 GRAUPEL kreup- GRAVE! ghrebh-2 GRAVE? gwWera-2 GRAVES ghrebh-2 GRAVEL ghréu- GRAVID gWera-2 GRAVURE ghrebh-2 GRAY gher-3 GRAYWACKE wegh-
GREAT
GREAT ghréu- GREAVES ghrebh-2 GREEDY gher-5 GREEN ghré- GREET gher-2 GREGARIOUS ger-1 GRENADE gre-no- GRESSORIAL ghredh- GREYHOUND gher-3 GRID kert- GRIDDLE kert- GRIDIRON kert- GRIEF gWera-2 GRIEVE gWere-2 GRIM ghrem- GRIMACE ghrem- GRIME ghréi- GRIND ghrendh- Grip! ghreib- GRIPE ghreib- GRIPPE ghreib- GRISAILLE gher-3 GRISEOUS gher-3 GRISETTE gher-3 GRISLY ghréi- GRISON gher-3 GRisT ghrendh- GRIT ghréu- GRIZZLE gher-3 GROAT ghréu- GROATS ghréu- GROCER gWres- GROO
---
```


## [2026-09-05T20:52:50.537Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"gurri\\|gurrio\\|gurrō\\|gurr-\" IEC.txt | head -20; echo \"=== ger- entries in IEC\"; grep -n \"^ger-\\|^gerō\\|^gurr\" IEC.txt | head -20"
}
```


### [2026-09-05T20:52:50.597Z] TOOL RESULT

```
4519:guró, ið (gurr-) (1) ‘coo, croon; growl’. Cf. ghur- Per. yuram, yurram ‘roar’; Arm. cf. koriwn, gs korean ‘whelp’; Lat. euro ire ‘croon, churr’; MHG kurren ‘growl’; LG kurren, id.; G cf. Kurre *turkey-hen; heath-fowl ; LG cf. kurrig (2) ‘irate’; Eng. to churr, beside cur, n.; ON kurra ‘growl’ beside Mod. kyrja ‘chime- in, sing in chorus’; Sw. kurre ‘dog, cur’, cf. kurla, v. ‘croon’, korla, v. ‘rattle, in throat
=== ger- entries in IEC
5668:ger- (1) ‘glow’. Cf. &or- Arm. cf. cirani, -vo, -eav, adj. ‘scarlet’; Li. žē- riù, éti ‘glow’
```


## [2026-09-05T20:52:51.367Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"gurrio\\|gurrire\\|gurrit\" LEW_1910.txt LAT.txt | head -20"
}
```


### [2026-09-05T20:52:51.420Z] TOOL RESULT

```
LAT.txt:22684:ut catillones catillorum ligurritores)-, puis "corbeille a serrer l'ar-
LAT.txt:34050:gulSsus, catillo, Xixvoc (Gloss.); ligurritor,-tio; abligurrio.
LAT.txt:34069:fornation expressive ligurrio.
```


## [2026-09-05T20:53:04.402Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=4400 && NR<=4530' IEC.txt | grep -n \"\\[pdf page\\|^[0-9]\\{2,4\\}$\" | tail -20; echo \"=== markers style\"; grep -n \"pdf page\" IEC.txt | head -3; echo \"=== nearby lines\"; sed -n '4500,4525p' IEC.txt"
}
```


### [2026-09-05T20:53:06.385Z] TOOL RESULT

```
71:305
83:15
84:20
85:25
86:30
87:35
88:40
89:45
90:306
100:307
109:10
110:20
111:25
112:30
113:35
114:40
115:45
116:308
124:309
128:310
=== markers style
=== nearby lines
v. ‘twaddle’; gungroj (mutter; Cz. huhlat ‘hoot, how?
gun£os, à (variant of gungos, à (1)) ‘knot, bunch, hump' Skt. gufijah (2) ‘bunch’: guíija ‘shrub; berry’; Blg. gáz, Slovene: goza, Cz. huzo, OPol. gaz, R guz ‘rump, buttocks’. Ambig. is OE cynca “bunch, bundle; LG kunke ‘twist, knot (see gungos)
gup- (gupà, o(n), ios) *hiding-place, niche, closet'. WP I, 561 Skt. gup, adj. ‘hidden’; Gk. güpé ‘cranny’; MHG kobe “cave, stall, sty, cage, pit? (LW in Cz. koba ‘small room’, kobka 'cel); OE cofa ‘closet, ark, cave, den E cove; ON kofi “hut, cell; Du. cf. kof (?) “kind of boat: LG Kofen; G Koben “sty, hovel
gür- (1) “squat, idle, lounge ON kúra, MLG küren, G kauern, id.; E to cower; OSw. kura; Cz. hytit, id.; Li. güris idler”; j-gürinti (2) "be huddled'; güràties idle
gür- (?) (2) ‘cover Per. gür ‘tomb’; Sw. kur ‘awning’
gurdos, ios, us ‘swollen, proud, stout, brave, violent. (This form is often coincidental with type *gurdus ‘sluggish, ponderous, awkward’, etc. an extn. of type *gurus “heavy” with various extns. of type *guriu-, guruu-, gureio, gurnd-, etc.). WP I, 641, 649-650, II, 278 Skt. gudah (^ball. WP I, 614); Per. (ambig. OPer.?) gurd ‘hero’; Oss. qal (1) ‘proud’; Arm. cf. kord ‘rough’, beside nkrtem “try”?; OW. W gwrdd ‘stout, fierce; OCS grüdü ‘proud; horrid’; R. gordyj, Cz. hrdý ‘proud’; Blg. grád, gård ‘ugly’; Srb. gfd ‘ugly; gi- gantic'; OE cf. cyrten ‘intelligent’. (The near- homophone gurd-, q.v. seems to be present in Skt. jadah; Per. gül; Oss.Dig. $ála; Gk. bradús, LW in Lat. bardus; Lat. (Late-Lat. or Hispano-Lat.) gurdus; Li. gurdùs; Latv. gurds)
gurg-, gurgul- (1) ‘twist. Gk. cf. gúrg-athos (‘wicker basket. For -athos, cf. psi-°, kál-^; for *undh-, see uendh-; Big. grágulja ‘cucumber’; Icel. kyrkja ‘strangle’; Li. gurga, gurgulys ‘twist, kink’. (For Icel. kyrkjast, korka, see gurg-)
gunĝos, à — guu- (guuolos, guuios, iə)
10
20
25
30
35
40
45
308
gurg-, gurgul- (2) “throat, pipe; croak, growl, gurgle’, etc. Cf. ghurgh-, gurg-. WP I, 683. Variant: gurgur- Arm. cf. krkram 'croak; gabble'; Gk. gorgura ‘sewer’; Alb. gürgull “open throat; Lat. cf. gurgulio ‘throat; Blg. grágra, grágorja, v. (warble', fr. a variant *gurgur-); Li. gurgu, eti ‘growl’, guigulas ((2) ‘bubble’. Ambig. cf. ghurgh-)
gurmos, us (variant of grumos, q.v.) Skt. gülmah ‘shrub; cluster; gang’; OCS grümiü, gs -u ‘shrub’
gurnos ‘hard, hardness, knob, knot. Cf. WP I, 557 Arm. kur ‘firm, solid”, cf. kurn ‘back’, krnak, dim. ‘ridge’; Cz. cf. sou-hrn “set, group’; Li. gufnas *knuckle-bone, hip, ankle’; Latv. gürns “hip, loin’.
guró, ið (gurr-) (1) ‘coo, croon; growl’. Cf. ghur- Per. yuram, yurram ‘roar’; Arm. cf. koriwn, gs korean ‘whelp’; Lat. euro ire ‘croon, churr’; MHG kurren ‘growl’; LG kurren, id.; G cf. Kurre *turkey-hen; heath-fowl ; LG cf. kurrig (2) ‘irate’; Eng. to churr, beside cur, n.; ON kurra ‘growl’ beside Mod. kyrja ‘chime- in, sing in chorus’; Sw. kurre ‘dog, cur’, cf. kurla, v. ‘croon’, korla, v. ‘rattle, in throat
güro, ið, see gür- ‘squat, lounge’ as in MLG küren; Cz. hýřit; Li. gürinti
gurulos (?) “grain, crumb, kernel Du. korrel ‘grain, kernel; Li. gurulas (2) ‘crumb’; Fris. cf. gjin koarel ‘not a thing’
guu- (guuolos, guuios, io) (1) ‘hollow; ves- sel" Same as (2) (?) Arm. kur, i-st. ‘wooden bowl; trough; skiff; (kuç, gs kco ‘handful’ is prob. to *gudhstios, but of doubtful reconstruction); Gk. gua, guía (field; womb’; cf. gualós, adj. ‘hollow’; güalon ‘hollow, palm of the hand’; guále ‘cup’; and the cpds. eg-güus ((near, lit. “at hand"); eg-gáe (pledge, lit. in hand"); ég-gus *pledged'; Alb. guvé ‘hollow; cave’; LLat. and Sp. gubia, Port. goiva, Fr. gouge 'gouge- chisel; cf. Sp. gubia-dura ‘notch, channel’; MHG cf. o-gde kou, kouwe ‘hopper; hut at mine-shaft; (ambig.) kobel 'gully, chasm'; Icel. kuggur Choat" LW in E cog). (A pos-
309
sible cpd. is Gk. sípue “flour-bin”, if fr. *Kuit- guuia)
guu- (2) “bent; bend". Same as (1) (?) Arm. cf. kkim (‘be bent, fr. (?) *gusuio-); Gk. gúēs *plow-peg'; guiós, adj. “lame”; guion lower limb, knee’; a-guiá ‘turning, street
```


## [2026-09-05T20:53:18.748Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('HRN.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('npages',len(pages))\n# leaf = printed + 21 -> printed 143 => leaf 164\nfor n in (163,164,165):\n    print('==== leaf',n)\n    print(pages[n-1][:1800])\nEOF"
}
```


### [2026-09-05T20:53:20.703Z] TOOL RESULT

```
npages 412
==== leaf 163
— 141 —
634. rönäSj röyenäs, röyen *Krapp, Färberröte*.
wa;^. uruddn, sar. aradSn,
Wohl zu aw. raoidita- 'rötlich' (No. 635).
rönäs ist aus röyenäs (im FJ zweifach belegt)
contrahirt; andere von den Wörterbüchern überlieferte
Formen wie roden, rüdeng, röynäs sind unbelegt.
635. (i)röT, rö 'Kupfer, röyln.
aw. raoidita- 'rötlich* (vd. 1, 3); phlv. rödlk geschr.
rötik (vd. 1 (8)), rod bezw. röi (AV.), royin (AV.) ;
skr. lohä'^) 'rötlich, Roterz, Kupfer.
bei. rod 'Kupfer (325).
636. {i)röT, rö 'Gesicht'.
aw. raoSa- 'Wuchs, Ansehen'; phlv. röd"^), hu]rod(i)s7i
(AV.); got. ludja 'Antlitz'.
Allgemein entlehnt im iranischen Gebiet und über
dasselbe hinaus.
637. reht 'Diener, Sklave'.
phlv. rasik.
Wohl zu ap. \/^raS'j np. resTden (No. 016)?
638. reffen 'ausgiessen, verschütten, Praos. rez-em, rPzis,
ni^TI (Qiss. Dan.), reze, vergl. hirezen \Soiho, Durch-
schlag.
g. retmün, Praes. herlfe; Käs. V. retdti.
aw. l/'ra^d-, ra^cayat *Si\isg\essen ; phlv. re//^/w, ircPt
(päz. rezed), rec(i)sfi; lat. liquäre; ai. [/'rcc,-, rindkil
bedeutet nur überlassen, räumen' (vergl. np. gurc/ten,
No. 914); arm. vergl. IKanem 'verlassen' (H. No. 132).
kurd. 7'etin 'ausgiessen'; oss. d. lejtm, t. iJjjn
'laufen, fliehen' (167) ; bei. reöag, n. rTsay (316), vergl.
princag 'pressen, auspressen' (443); wa/. varic-am,
sar. variiz-am 'müde werden , Causat. Verweilen lassen'.
Hierher gehört auch syr. LW. pnjN, arab. LW.
ihrtq 'Wasserkanne' (de Lagarde, Ges. Abb. 7).
*J SpiegePs Erklärung, Ar. Periode 35, ist lautlich pfanz uu-
niüglich.
2j Fiilaoli oder vielmehr nur graphisch rö/, Bund.
==== leaf 164
— 142 —
639. rlden *kacken', Praes. rii/^em, rtsten, rtm *), rime.
aw. l/^raf-, avi dim irita *kackt darauf (vd. 5, 1);
phlv. }*ttan, reman, remamh; ai. l/^re-, riyäti *frei
lassen, laufen lassen .
kurd. rltin *kacken'; oss. d. liyun, t. Hin (168); bei.
rii/ay (315).
610. vis (*m) *Bart', rese *Haai'\
aw. ra^sa- zweifelhaft (Hörn, ZDMG. 43, 33,
Jackson, Amer. Journ. of Philology, Vol. XI, 88);
phlv. res *Bart' (AV.), resak *Haar (vd. 7 (28) Gl).
kurd. ruh, ri *Bart'; afy. ^Ira (aus *riSa) bezw.
^ire; oss. d. re/e, t. rt/T (213); wa/. reyis, i^itr. ri/is,
rikis, minj. yarzd,
Vergl. Bartholomae, Studien II, 54, 55.
641. veH') 'Wunde, Geschwür, rese, resTde,
aw. ra^sah' 'Wunde', [/^rars-, ra^ayat 'verwunden ;
phlv. res, resiian ; ai. l^reS-, resat^ reHyati *versehrt
werden ; beschädigen'.
LW. kurd. m; bei. res 'Wunde' (225).
642. reg \Sand' (AM. 242 Zeile 9), rez (Käs. Z. ryz).
LW. (?) kurd. rik^ rig; afy. reg; bei. rek^ n.
re/ (317).
Bartholomae (ZDMG. 46, 301 No. XIX) stellt die
iranischen Worte zu ai. sikata- 'Sand', während sie
Geiger an aw. l/^rafx- (No. 638) anschliessen wollte.
643. rew 'Betrug, List* (Sahn. II, 735 Vers 939), rewäs,
reimen, rlmen 'betrügerisch'^).
ai. rip' 'Betrug* (l/"rep-, lep- 'anschmieren').
Vergl. fireften (No. 829).
») *liem', LW. kurd. afy. rim *Eiter*, bei rgm 'Eiter* (224), wa/.
rim *Schmutz\
2) Der Mftihülvokul ist bezeichnet AM. 231 Zeile 3.
*) *Repmetiy vergl. * Verlorenes Sprachgut* No. 83. Die Volks-
otyraologie macht das Wort zu einer Verkürzung von Ahrlmen. Da die
Bedeutung 'sclimutzig, unrein* dem Worte nach der Überlieferung nicht
zukommt, so wird man os nicht zu phlv. reman^ np. rim (oben No. 039)
zi(5licn dürfen.
==== leaf 165
- 143 -
z.
644. ^U", Praefix, w-2-, vergl. suparden (No. 697), siperT
(No. 703).
ap. US' {ustasana-) 'hinauf; aw. us-, uz- 'heraus,
empor ; phlv. uz- (auch w/-, uö- geschrieben); ai. ud,
oss. 'S, -is (216), e- in oss. z[mänfin *zusammenrühren,
vermischen (133) ist unsicher.
645. xäden *gebären ; geboren werden*, 'Praes. zay-em,
zad 'Geburt' {-zad, mlrzä), zaj^ zaje 'Wöchnerin*,
zOq ') junges Huhn', zeh * Junges, Kind', zehdan 'Uterus*,
zehistän 'Fehlgeburt, Placenta' (AM.), jüd.-pers. TIM
(Salemann, Litbl. f. or. Phil. II, 81), zatjlden.
aw. [/'zan-, zayata gebären; geboren werden, us
zayfAte, zata-; phlv. zatan, zay(i)sn, zak (aw. zqda-,
y. 42, 5 b); ai. [/"^aw-, Jdyate, ^ki\ jfati- *6eburt'; arm.
ein 'Geburt', cnanim 'erzeugen' (H. No. 136).
kurd. zain gebären ; af/. zez\edal geboren werden',
zez\avul 'erzeugen*, s'opmZ 'gebären'; oss. -eäwclr// 'wachsou*,
zayi (125); bei. zäyag, n. zay 'gebären, hervorbringen*
(423), 'Za/t 'Sohn' aus "^zatk (418) ; wa/. yäz-am, sar.
zay -am,
646. {\)xär 'Klagen', zäri^ zäre^), zandefi.
ai. 3 l/^ar-, jdrate 'rauschen, schnattern, rufen*,
afy. Sarai 'klagen'; oss. d. zarw?, t. zarin singen'
(128).
647. {^)»är 'schwach, elend*.
Wohl zu aw. [/'zar- 'altern' (vergl. np. zer, No. 655) ;
phlv. zär, zarth (Bund.).
648. zäl 'Greis, Greisin'.
aw. i^zar- altern', vergl. zaurvan-, zatirura-; ai.
1 l/yar-, jdra- 'alternd*.
*) Arm. LW. jag 'junger Hund*, syr. LW. j|T fdo Lagardo,
T
Ges. Abh. 41).
-) Xp. zävp (VuUcrs) ist vorloaon fius zäre.
```


## [2026-09-05T20:53:43.878Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"zarun\\|\\*zar\\b\\|zarin\" CHEUNG.txt | head -20"
}
```


### [2026-09-05T20:53:43.933Z] TOOL RESULT

```
3403:(Sor.) bZardin/bZer- are not connected with Oss. І. evzaryn/evzerst, D. evzarun/ 
3407:forms are unrelated to Oss. I. angaryn/enzerst, D. enzarun/enzarst (caus.) ‘to 
7717:Bart. laZör ‘live coal, charcoal’ || (+ *ham-) Oss. I. апзагуп/апҳаегѕі, D. enzarun/ 
30368:*NEIR: Oss. I. zælyn/zæld ‘to sound’, І. zaryn/zard, D. zarun/zard (caus.-iter.) ‘to 
30395:*zarš! ‘to be excited, delighted, rejoice’ 
30448:of *zar ‘to take, bring’ (= Skt. har) root and *kar&/*xrah. 
46365:avzarun/avzurst (D), 
47255:zarun/zard (D), 470
```


## [2026-09-05T20:53:46.108Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '30330,30395p' CHEUNG.txt"
}
```


### [2026-09-05T20:53:46.218Z] TOOL RESULT

```
*KHOTANESE: ysir- (ysad-) ‘to become old’ => SGS: 113 

*NWIR: NP zal PN (in Shahn.), also ‘old (wo)man’ 

*NEIR: Oss. z&rond ‘old’, Pash. zor (m.), хага (Ё), Yi. zor ‘old (of people)’ 

*MISC: Orm. zal ‘old’ (LW ?) 

*SANSKRIT: jar’ ‘to age, grow old’ (RV+) > EWAia I: 577 

© This root has an impeccable IE etymology. 

«PIE *gerH>- ‘to age, grow old’ = LIV: 165 f. | Pok.: 390 f. 

*IE COGNATES: Gr. eynpa ‘became old’, Gr. yfipag ‘old age’, Gr. yepwv (m.) ‘old 
man’, Arm. cer ‘old; old man’, OCS ss-zpreti “о ripen’ 

*REFERENCES: IIFL I: 413b; DKS: 346b; Abaev, Slovar’ IV: 304 f.; Werba 1997: 289 f.; NEVP: 103 


*zarHË ‘to bewail the deceased, 5: JS ex ull” 

*MIDDLE PERSIAN: MMP zryg, BMP zlyk /zarig/ 'sorrow, suffering! (LW) 
c DMMPP: 380a 

*PARTHIAN: Z'r, Zryg ‘sorrow, suffering? > DMMPP: 380a 

*KHOTANESE: LKh. ysär- ‘to sing’, ysera- ‘wretched’. 0 On ysirum ‘wretched’ (not 
‘loud’, DKS: 353a) see Skjerve, SVK I: 107. © SGS: 112 

*SOGDIAN: BSogd. z’ry, z’r’k, z’r’y ‘compassionate; pitiful’, CSogd. z’ry (indecl.) 
‘pitiful, pitiable, sympathetic’ 

*CHORESMIAN: zry- ‘to announce, reveal, speak about (sorrow)? > Samadi: 264 
*NWIR: NP zaridan ‘to weep, moan’ (LW), Bal. zarit/zar- ‘to be uneasy, pine for’, zar 
‘lament’? (< NP) || (+ *a-) Kurd. azar (f.) (Kurm.) ‘weeping, crying’, (Sor.) 
‘suffering’ 

*NEIR: Oss. I. zælyn/zæld ‘to sound’, І. zaryn/zard, D. zarun/zard (caus.-iter.) ‘to 
sing’ || (+ *aua-) Oss. I. uzalyn/uzeld ‘to nurse, tend; to coax; to show attention; to 
do something nice; to regale’ || (+ *a-) Oss. I. azelyn/azzld, D. azeelun/azaeld ‘to 
give sound, echo’ 

*MISC: Georg. (LW) zar-i ‘horror’, Abkh. (LW) a-zar ‘songs at memorial feast’ 

9 The Ir. forms appear to refer to the bewailing ceremony performed in memory/ 
honour of the deceased: this usually involves singing, comforting, calling and ritual 
lamentation (etc.). Ir. *zarH (connected to Skt. jar ‘to sing’ ?) should therefore be 
separated from *garH!, Skt. gar ‘to greet, praise’, which rather refers to the 
welcoming cermony given to a guest. 

«PIE *g(e)rH>- ‘to bewail the deceased (i.e. through lamenting, calling, singing (etc.) 
in honour/memory of the deceased)’ = LIV: 161 | Pok.: 352 

ЈЕ COGNATES: Gr. үйрос ‘voice’, Olrish -gair ‘to call’, OE cearu ‘sorrow, care’, 


Engl. care 
*REFERENCES: Abaev, Slovar’ I: 96 Ё; DKS: 349a f., 355a; Abaev, Slovar’ IV: 295 f., 23 f., 288 f£; 
Cabolov 2001: 105; Shahbakhsh: s.v. zar-; Korn 2005: 206, 379 


*zau 471 


*zarš! ‘to be excited, delighted, rejoice’
```


## [2026-09-05T20:54:02.258Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== MON ghorridan\"; grep -n \"غریدن\\|غرّیدن\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt 2>/dev/null | head -10"
}
```


### [2026-09-05T20:54:02.324Z] TOOL RESULT

```
== MON ghorridan
MON_part2.txt:992:بر آورنده؛ غرنده. (حا.) در حال غریدن» 
MON_part2.txt:1163:آمدن: فرش کردن؛ غریدن. ضضناک 
MON_part2.txt:1363:کلو پیچیدن. آوازی مهب دادن غریدن. 
MON_part2.txt:1541:غریدن: ۰۲-1۵:0:(اصت. مص‌ل.) (غربده 
MON_part2.txt:1593:غریو: ۰7۷« [قس. غریدن] (اصد.) بانگ و 
MON_part2.txt:2048:غطیط: (ع.] (مصل.) غریدن شش 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:992:بر آورنده؛ غرنده. (حا.) در حال غریدن» 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:1163:آمدن: فرش کردن؛ غریدن. ضضناک 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:1363:کلو پیچیدن. آوازی مهب دادن غریدن. 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:1541:غریدن: ۰۲-1۵:0:(اصت. مص‌ل.) (غربده
```


## [2026-09-05T20:54:04.070Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== ARY bidar\"; grep -n \"بیدار\" incoming/ARY/ARY_pages.txt | head -5; echo \"== ARY ghor\"; grep -n \"غریدن\\|غرّ\" incoming/ARY/ARY_pages.txt | head -5; echo \"== ARY zar\"; grep -n \"^.\\{0,40\\}زار\" incoming/ARY/ARY_pages.txt | head -5"
}
```


### [2026-09-05T20:54:05.679Z] TOOL RESULT

```
== ARY bidar
3755:.۰ معنی اين واژه در زبان‌های ژرمنی: بیدار» بیدار شدن» نظاره کردن.
4109:۲ | بیدار
9892:ز(زره اسب)؛ 2581287/۸0 (هشیار بیدار). به پندار من واژه‌ی "زندان" (پهلوی:2:)(210۸7
== ARY ghor
11464:فارسی (/۳58514): غرش غرنبه, غرمبه, غرنبیدن, غریدن ,01103571
11493:چم‌های این واژه در زبان‌های هند و اروپایی گوناگون: غریدن» آسمان غرنبه» خشمگین.
== ARY zar
258:هزارهی گذشته (به استتنای هجوم و ماندگری قبایل ترک و مجار و فنلاندی) تغییر زیادی نگرده است
287:جامعه‌ی هند و اروپایی حدود چهارهزار سال پیش از میلاد در ناحیه‌ی معینی وجود داشته و زبانهای
590:هند و اروپایی بنیادین (یعنی حدود ‎٩‏ هزار سال پیش) پپیگیری می‌شوند و اگر برای یک واژه‌ی
611:حدود ۲۵ هزار لوحه و خشت مکتوب (بّرنوشته) در دست است. این خشت‌ها و لوحه‌ها به حروف
669:هستند و جمعیت آنها بالغ بر حدود ۸۰۰ هزار است» به صورت جمهوری خود مختار (جزو روسیه) ‏
```


## [2026-09-05T20:54:11.818Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '1538,1546p' MON_part2.txt; echo \"=== ARY 4100-4120\"; sed -n '4100,4125p' incoming/ARY/ARY_pages.txt; echo \"=== ARY 11455-11500\"; sed -n '11455,11500p' incoming/ARY/ARY_pages.txt"
}
```


### [2026-09-05T20:54:11.917Z] TOOL RESULT

```
کردن» عدم آشنایی نمودن. ترسیدن طفل از 
شخصی ناشناس » وحشت کر دن. 

غریدن: ۰۲-1۵:0:(اصت. مص‌ل.) (غربده 


۰ موم ۰ 
فر هنک فار سی‌معین 

=== ARY 4100-4120
۶ اسلاوی کهن (1/#ما؟ للع #نانن) صا0): برهان قاطع + ۳۳۲
یا«داشت: ۰ " :
:۱ چم این واژه در زبان‌های لاتین و ایرلندی کهن و ولزی: درخت انگور) تاک.
چم این واژه در زبان اسلاوی: شاخه
1 . ۲- 8۸8۸87 ,53۸7 ,۸۸1۸83آ05 ربشه‌ی واژه‌های ژرمنی این واژه را از واجریشه‌ی هند و اروپایی
ملظ۷* با 15۸ ۷۷* می‌دانند ولی 3016018379 ضمن بحث در مررد واجربشه‌ی 1116۸ ۷۷* (صفحه‌ی
0) ذکری از واژه‌های رُرمنی این فهرست نمی‌کند و آنها را وابسته به واجریشه‌ی ۹۱۷۳۲ می‌داند (صفحه‌ی
112
[pdf page 141]
۲ | بیدار
یی
اوستایی (4۷37۸4): 8۸07۸ انگلیسی (4لولا62/0): ۱ 8 فاريریر
پیلری (/۸2۲م): ۰ ۷۲6۲۸۵0 ,0ققآم دانمارکی (3ل0۸(8): 0
سانسکریت (545877): ,8110 ,8003 سوئدی (51780/8[7): 8507۸
ا 7 80071۸77 باف800 هلندی (007614): 230
۱ یونانی (07680): ,۳517117011۸ اسلاوی کهن (72ما؟ لل#ناتل) 02
: 1 نا راد وان
لاتین (7/00ها): راردا روسی (/78514): پم ۳
گوتیک (ع0077/6): ۰ 8107۸0 ,81100۸1 لینوانی (204(141 ۰:07 8030۲ *
ابسلندی کهن ([( 5۸/0/0۷ صا۵): ایرلندی کهن (577ل#/ صان): زر رانا
81071۸
نورس کهن (۸07۹ 010): 210117۸ پسگشت‌ها 25
ساکسرنی کهن (5420000 ۰:00 100۸۷ 0 ۸۵080
فریزی کهن (/(54ل7۲ صا0): 8100۸ 2 (810) تا انا
1۸0۸ 3 (۷16۴۸0) اند رد ها
آلمانی کهن (/(028014 0[4اتز صاه): 3 (810) :0/708
=== ARY 11455-11500
لاتین (71ا): نران ۳۷ پسگشت‌ها کیت
فرانسه گهن (2۴8۸۷ 2ل0): 5 7 200۷0
انگلیسی (8۸/01187): (از فرانسه‌ی کهن) ۸۷5 0 (19تم) اک نیت نا
ایرلندی گهن (4ل5ل#/ 01): 7 (ناه25م) 02
8 ۸18۸7 لغت‌نامه دهخدا: 1۳۳۸
بادداشت:.
۱ چم این واژه در زبان‌های غیر از فارسی: متمهد» دایره) گردی.
۲ رابطه‌ی این واژه فارسی با واجریشه هند و اروپایی و دیگر واژه‌های این فهرست احتمالی است و بهمین دلیل در
جلو واجریشه‌ی هند و اروپایی (شاید) آمده است. :
فارسی (/۳58514): غرش غرنبه, غرمبه, غرنبیدن, غریدن ,01103571
اوستایی (/ل4887۸): ارات نی ساکسرنی کهن (/5420 ۰:00 68336
تلم . پهلری (الاماتلده: فرپزی کهن (/(۶۴/514 00): 0
ات یمس آلمانی کهن ((05704۸ 04]تز 012):
کردی (080/34): 61082010 ,ل(01781 63/۸ ,ات0
افغانی (پشتو) (//۸۳0۸): 65۸ آلمانی (058(/۸): رال
یونانی (07820): راما نارای اناد انگلیسی کهن (57اا8)0 012):
گریک (110ل007): هه لا اناد نی اناد ی
ایسلندی گهن (012۸۸0۷(ف5 صا): انگلیسی (7ل5انا2/0ق): ا اد
انا ی دانمارکی (0۸۸/5): 1
[pdf page 387]
۸ | فرت فرا-(به چم *پیش* *به سوی جلو)

نروژی (۸/07/0۸۸): ۰7۸ لتونی (لتی) (471۸4ما): ار دی ی
هلندی (01767): بانا 1۱ پروسی کهن (۲8۷:554۸ 2ا0): 08۲7۱۸1۳8
اسلاوی کهن (۷76اشا #67ناتل ضز): ۶

1 ,0۸1۳7 پسگشت‌ها_ ۹ اس ۸878625 ی
لهستانی (ناقنا۵): ۰ 630۸ ,0۸5 459 مت نا
روسی (/(554): 68016 ,نا۸/57ج 0 (01) +87
چکه ((286): : :3ل2(قل بر

7 ,1133۸1۸1 ,113/177 6 (1133088) باق (۸۵۸3)
صربی (/5278142): این 558 0
برهمی (80481/1401): 1107 4 (6873) :002/5
اسلرا کی (5.0140): 1180۸1 ,111150:15 9 (781058) ۸0
یتوانی (۵] 1727۸۸ ل): برهان قاطع : ۴ و ۱۴۰۹9۱۴۰۷
1 08۱3/1 فرهنگ معین : ۴و ۲۱۴۵
1 بادداشت.
چم‌های این واژه در زبان‌های هند و اروپایی گوناگون: غریدن» آسمان غرنبه» خشمگین.
چم این واژه در زبان یونانی: شیهه کشیدن. :
اوستایی (4887۸21)+ ۸۰ ,بش انگلیسی کهن (82701./57 0ا0): 3
پارسی باستان (4(۷ای۳22 صا0): اسلاوی کهن (ع1ما5 #لع#ناتن صام).
۰ وال7۸ ,ات8۸ +858
پهلری (۲7هاتزوه): 7 روسی (/0فاهکتا): -880
سانسکریت (6۸(/58077): +8۸8 ۴8۸ چک (280): 80
ارمنی (۸0/80/1401): 118۸ صربی (1۸/1ق55): ۳
```


## [2026-09-05T20:54:32.952Z] TOOL CALL #32: Bash

```json
{
 "command": "ls site/pages/175.jpg 2>/dev/null; pdftoppm -f 175 -l 175 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg175 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


## [2026-09-05T20:54:33.257Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '11400,11470p' incoming/ARY/ARY_pages.txt"
}
```


### [2026-09-05T20:54:35.107Z] TOOL RESULT

```
site/pages/175.jpg
total 20300
drwx------ 2 sfmqrb sfmqrb    4096 Sep  5 16:54 .
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
-rw-rw-r-- 1 sfmqrb sfmqrb   61639 Sep  5 16:53 build155.py
-rw-rw-r-- 1 sfmqrb sfmqrb   70485 Sep  5 16:53 build156.py
-rw-rw-r-- 1 sfmqrb sfmqrb   72953 Sep  5 16:48 build158.py
-rw-rw-r-- 1 sfmqrb sfmqrb   45662 Sep  5 16:49 build164.py
-rw-rw-r-- 1 sfmqrb sfmqrb   50404 Sep  5 16:53 build168.py
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
-rw-rw-r-- 1 sfmqrb sfmqrb   41788 Sep  5 16:53 p173_ital.png
-rw-rw-r-- 1 sfmqrb sfmqrb   32898 Sep  5 16:53 p173_op.png
-rw-rw-r-- 1 sfmqrb sfmqrb  671488 Sep  5 16:52 p600_350.png
-rw-rw-r-- 1 sfmqrb sfmqrb  139701 Sep  5 16:52 p600_foot2.png
-rw-rw-r-- 1 sfmqrb sfmqrb  183909 Sep  5 16:52 p600_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1717 Sep  5 16:52 p600_head2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5162 Sep  5 16:52 p600_head.png
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
-rw-rw-r-- 1 sfmqrb sfmqrb   52970 Sep  5 16:53 pg173.png
-rw-rw-r-- 1 sfmqrb sfmqrb   54907 Sep  5 16:54 pg175.png
-rw-rw-r-- 1 sfmqrb sfmqrb   44812 Sep  5 16:34 pg532.png
-rw-rw-r-- 1 sfmqrb sfmqrb  153161 Sep  5 16:34 pg532_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4868 Sep  5 16:14 prt.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  333088 Sep  5 16:16 sod135_c.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1817364 Sep  5 16:16 sod135.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  101641 Sep  5 16:15 sod136_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1892712 Sep  5 16:15 sod136.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   56398 Sep  5 16:26 write144.py
```


### [2026-09-05T20:54:35.150Z] TOOL RESULT

```
دانمارکی (۷184ل0۸): 0 9 (۴8۲۵۵۲2۴) ,ا12 (4(0۷)
سوئدی (9820154): ۳۸ 10 ملظ
نروژی (0/08۷501۸۸: دزن دک 8 (۲0۲) َ :01008
دی (01770): لدنوندها 5 (۵۷() وراد نج
اسلاوی کهن (4۲70ا5 #6نابل 2ل0): 6 (85600(128) ۸04/۸۸0
1 برهان قاطع + ۱۳۹۸
مّ
لهستانی (۳0/7534): 2۸
یادداشت: َ
واژه‌ی انگلیسی 2۸8 (انگلیسی کهن:01(881۸۸۲) نیز از همین واجریشه است. بازگشت به: دانتن ۰
اش 1
| مانکایس مروازای ارس ملگ
پهلری (1الل۳۸): ۸6 ,8508 لیتوانی راب7 560871 ,ت86
کردی (68/0154): ,81178 لنونی (لتی) ((7714): ۰ 53607 ,8761771
سانسکریت (5۸۸5807): رانا ۰
یونانی (6524ق07): ۸ ,2۷0
یی
[pdf page 385]
۶ | صد
پسگشت‌ها 5 1 (8۸79) درکن ار 0
۱ 6 تمه برهان قاطع : ۱۳۷
1 (8۸7/10) +12 02(/2 2/۸ 1 :
۱ ری
بادداشت:
چم این واژه در زبان‌های غبرایرانی این فهرست: ابزار بریدن پا خراشیدن.
اوستایی (۸8747): اند ان آلمانی کهن (05704۸2 27/04 012):
پهلری (7ا(۸): 7 ,8۸0 7 ,137310837
ارستی 05570 ۹ 520 آلمانی (0588(440): لا ان رال ۱:۱
کردی (0701571): زردن انگلیسی کهن (8۱60870 صز۵): 070
افغانی (پشتر) (4۳0۶/۸9۷7): بلقأ5 باه بل8۸ ۰" انگلیسی (50ل8/01): زا یدای
تخاری ۸ (۸ [(4ل70771۸): ای دانمارکی (2۸۸۷154): 111707۸ أ
تخاری 8 (8 (۸ل7۸ل707). اد ۱:۱ سوئدی (5(۴01577): 11108۸ ٍ
خشنی (707۸/895/): 57۸ نروژی (07۷501۸/: دی زا
سانسکریت (54۸/37/7): 511۸7۸ ,5۸7۸86 هلندی (0177677): زان رانا :۱ ۱
بونانی (0828): 8۸70 ,8۸30" اسلاوی کهن (۲70بما5 ناب صا0):
لاتین (710ا): اه زان
فرانسه (۳82(/0۶): 7 لهستانی (۳0//37): 6۸ ,8717
اسپانیایی (تل5۳۸15): 0270 روسی (ل55۸(ا#): 370
ایتالیایی (۸۷ال7۸): ده چککه (250(7)): زین
رومانی (۸2((/14۷): ان بلفاری (#مملقممانام. 370
پرتغالی (۳070017858)+ اد اسلرا کی (51.0744): 370
گوتیکد (0077/10): 10۸ لیتوانی (۸0الهفنا 23 7/.): 2۸5
ایسلندی کهن (010۸710/مو صاه): لنونی (لتی) (/71۵0ما): ردان
10 ایرلندی کهن (4لولطا صاه): اند اه
ساکسونی کهن (542:0۸ صا0): گالی ((8ل-انامه): اناد
,1111۱08010 ولزی (5.اع8): ایا
فریزی کهن (/هل5ل۶# صاه): برتونی (87570(0)+ ان ای
0 ,117050
[pdf page 386]
۹
: عن (به چم *برازت *8ه*) | ۳۸۷
پسگشت‌ها ندیه اد داد 6 (۲81) +قمهمنم 05
زر 2 2 تن لا
7 (1710880) ی پرهان قاطع ۱۳۳۳
آرمتی (9اق۸801): ۸
لاتین (71ا): نران ۳۷ پسگشت‌ها کیت
فرانسه گهن (2۴8۸۷ 2ل0): 5 7 200۷0
انگلیسی (8۸/01187): (از فرانسه‌ی کهن) ۸۷5 0 (19تم) اک نیت نا
ایرلندی گهن (4ل5ل#/ 01): 7 (ناه25م) 02
8 ۸18۸7 لغت‌نامه دهخدا: 1۳۳۸
بادداشت:.
۱ چم این واژه در زبان‌های غیر از فارسی: متمهد» دایره) گردی.
۲ رابطه‌ی این واژه فارسی با واجریشه هند و اروپایی و دیگر واژه‌های این فهرست احتمالی است و بهمین دلیل در
جلو واجریشه‌ی هند و اروپایی (شاید) آمده است. :
فارسی (/۳58514): غرش غرنبه, غرمبه, غرنبیدن, غریدن ,01103571
اوستایی (/ل4887۸): ارات نی ساکسرنی کهن (/5420 ۰:00 68336
تلم . پهلری (الاماتلده: فرپزی کهن (/(۶۴/514 00): 0
ات یمس آلمانی کهن ((05704۸ 04]تز 012):
کردی (080/34): 61082010 ,ل(01781 63/۸ ,ات0
افغانی (پشتو) (//۸۳0۸): 65۸ آلمانی (058(/۸): رال
یونانی (07820): راما نارای اناد انگلیسی کهن (57اا8)0 012):
```


## [2026-09-05T20:54:47.386Z] TOOL CALL #34: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg175.png"
}
```


### [2026-09-05T20:54:47.753Z] TOOL RESULT

```

```


## [2026-09-05T20:54:47.752Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-05T20:55:12.603Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== BRT gar wach\"; grep -n \"wach sein\\|erwachen\\|gāraiiemi\\|garayeiti\\|gārayeiti\\|jaγaurvå\\|frayrisa\" BRT.txt | head -15"
}
```


### [2026-09-05T20:55:12.676Z] TOOL RESULT

```
== BRT gar wach
12928:•  j.  'darat-  Adj.  'Acht  gebend,  über- wachend': dansla  (NS.)  dakat  *am3r^xs- yanüm  vTsfqm  yqm  astvaititn  gaS%qm "und  (sie)  überwachend  wird  er  die  gc- sammte  materielle  Lebewelt  unvergänglich machen"  Yt  ig.  94.
```


## [2026-09-05T20:55:14.203Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== NYB wigras\"; grep -n -i \"wigrās\\|wigras\\|vigrās\\|wyglʾs\\|wigrād\" NYB_vol2_glossary.txt | head -10; echo \"== MON1 bidar\"; grep -n \"بیدار\" MON_part1.txt | head -8"
}
```


### [2026-09-05T20:55:14.340Z] TOOL RESULT

```
== NYB wigras
6190:wygr's: vigrās-
== MON1 bidar
3669:گ .) نارون. (گیا ۰ سبیدار. 
6343:پگاه خیزانیدن» به وقت از خواب بیدار 
12686:استیفاظ: 7اه [ع.] (مص‌ل.) بیدار 
12689:بودن» بیدار شدن. هشیار بودن» هوشیار 
17176:تحار کف (امص.) آ گاهی بیداری. 
17205:احساسات و عواطف را در او بیدار و 
25060:برخیزانیدن. بیدار کردن از خواب. 
26823:بیخواب: اقا (ص‌مر.) بیدار. آنکه
```


## [2026-09-05T20:55:20.475Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"vigrās\\|vigras\\|vigrāt\\|vigrat\" NYB_vol2_glossary.txt | head -10; echo \"== BRT try2\"; grep -n -i \"wach\\b\\|erwecken\\|munter\" BRT.txt | head -15"
}
```


### [2026-09-05T20:55:20.539Z] TOOL RESULT

```
4137:vigräs- [wgl’s-] pres., to rouse a p. from sleep, from the dead: apäc vigräsend 10179; d(h) vigrasend 101°. — Av. (511) lgar-, v. guhräyenitan; MPrth wygr’s ‘to awake’, MPrs ‘to rouse from sleep’; Ver- bum 196; Ghilain 82, 92-93.
6190:wygr's: vigrās-
== BRT try2
2791:3.6.  a)  mit  Angabe  des  Ziels  a.)  Akk.  i^«n/«(sd.)  Y.  70.  i.  Ilj  in  schwach- 'wohin?',  ß)ai/rundAkk.'zuwem?,gegen|deiktischem  Sinn  'dieser,  der,  er'  I)  auf wen?',  t)  patiy  und  Akk,  'gegen  wen?'; '  Zuvorgenanntes  —  oder  durch  den  Zu- dädarsis..avam  adam  fräilayam  arminam\s,a.mmenh^T\g  Angedeutetes  — ,  Zuvorge- Bh,2,7;  10,  _y.i4,  5.1;  —  iaram  pilrsam  sagtes  (Wort  oder  Satz)  zurückweisend /raisayam  abiy  ('zu')  vistäspatn  Bh.  j.  ,1)  auf  ein  Nomen  a)  adjektivisch:  ae>/i i;  —  vahyazdäta''  .  .  käram  /rifisaya*^nar0  „yeztca  vao(ät  "sö  nii  V./5.3;  5.41; Aara^uvatim  .  .  abiy  ('gegen')  aziam  Bh. !  —  Atlucä  *aitaya  narä  .  .  °sö  zt  narö  .  . 3-9i  3i9i  i'j    —  pasäva''  adam    karam\'^.4.ifii.;    —    kanqm  ..  'sa  hana  Y.lj.
4965:aJs dessen  Konelat:  avam  käram..  °vaAya ksrahyä  .  .  tyam  z-ohyazdaiJ*  /räilayi^ Bh.5.  lof.;  —  nadi'tahaire^  .  .  udafiatata .  .  fasäve^  adam  .  .  asiyavam  abiy  "vam nadi'tabairam  kyi^  nabitkadrai'ari^  agau- batä  Bh. /. i6- 1 8;_j.  3, g,  14, 2. 4. 1  b) sub- stantivisch, auch  im  Sinn  unsres  schwach- tonigen  'er':  t3m  lafmeii . .  yatata  ahurö maxda , ,  aom  Jai'iyat  Yt  ^5. 1  —  3 ;  —  I  gau- mat^  . .  hauv  udapaiata  . .  pasäv<^  ATru* aHy..'vam  asiyav^  Bh.;.ii;  —  *utilmaiy amyaiiiy  vasiy  astiy  kartam  °v<^  .  .  naiy nifistam  Bh.  4.8;  —  tuvam  ks  hyc^ imäm  dipim  vainahy  .  .  imatvä  patikarä . .  yävä  (sd.)  *taumä  *ahatiy  *äva  °vaiy pariiarä  Bh.4-i5;  — ya'^a  «J  snaihi^. paiti.vaiaMt  'vat  paiti.päpayamnS  "..eine Waffe  .  ^  sich  dagegen  zu  decken  suchend' P.  2/;  —  afavatum  mahrka'^ni  aon äinrnta  strmca(sd.)\t ip.12.  a)l'insbes. ein  Nomen,  das  —  zum  selben  Satz  gc- höiig  —  sammt  Zubehör  unmittelbar Toraosgeht:  kSram  tyam  hamii'iyam  kyeT
6969:•  j.  ax'afnya-  Adj.  (fem.  yä-)  'schlaflos, immer  wach':  nairyqin  hnm.varntim  .  . 'yqm  Y.ß'J.S-
7206:•  j.  ax'afnya-  Adj.  (fem.  yä-)  'schlaflos, immer  wach':  nairyam  ham-ianitlm  . . °yqm  \.(>J.$.
7453:•  j.  a'sitö.gätav-  Adj.  (auch  fem.)  'auf dem  l^ger  ruhend':  nairyqm  hqm.variitlm . .  'tum  jayaurBm  ". .  die  auch  auf  dem Lager  ruhend  wach  ist"  V.  62.  5.
7946:.  .  antar?  tarn  asmammca  Yt/0.95,  H. /,  16;  —  vJspim  *mat  yat  juy3{sÄ.)  aahus ". .  all  das  was  . ."  H.2.  a.  II)  in schwach  deiktischem  Sinn  'dieser,  der' ; 1)  auf  Vorhergenanntes,  Vorausgehendes (Wort  oder  Sau)  zurückweisend;  1) jektivisch,  auf  ein  Nomen:  yasca  . ,  ■ vacS  (in  S  3)  «?']^  *vJsaite  framrüite  (sd.) Y.Ä4;  —  'ma  'ai  iceSa  vaiA  fm  %  z^)
10198:nät/rä  1)  Inkoh. 'aufwachen':  h3  s^af- iiä'ia  frayris>mnS  H.  /.  13;  —  x^a/ttät /rayris;»Nnauqmll.i.i3\ai.  2)Kaus. 'aufwecken': rt'fl.^Mi'  dahmät  aoxte *frii'i^  mä narf  *gärayBis  yat  ratus  frilsis  *äjasäl'^ vXiaiti  dim  frayrärayS  nOitfrayräyräyäti aliff  ratufris  *yd  jayära  "Ein  D.  sagt  zum andern:  'Weck  mich  auf,  Mann,  wenn  die Gebetastunde  kommt'.  Der  iibemimmts ihn  zu  wecken,  bringt  ihn  aber  nicht wach.  (Dann)  ist  der  r.,  der  wach  war" N.  ig;  —  sraesB  a^'Ö  aotn  mtnyim  fra- yrsrayeifi  pars.dari  tiqma  V.  /tS'.  33,
11507:•  j.  Jayäurvah-,  Jiyäurvah-  Adj.  'wach, wachsam':  mihr3m..a:i^afn3m  *jayäurva- t?h»m  Yt  10.  7  '';  —  mi^r?m  timatahä^a jiySurum  VtJO.  141;  7^,42;  —  naityqm ham.var3itlm  .  .  äsitS^ätüm  jayäurBm (ÄSf.)'>  \.62.S.  Yt75.39  (wo  •rum).
11798:i)  Inkofa.  'leer  sva.  schwach  werden, die  Fassung  verlieren':  yai  sulu/  (sd.) dayäj  äat  dasua  tusm  ". .  dann  verlieren die  D.  die  Fassung"  V.j,32.  2)  Kaus.
11799:'los  machen  sva.  loslassen,  fallen  lassen in  — '  {paili  mit  Akk.):  yö  bansma  *taosa- yäti'-^  draos  (sd.)  vS  paiti  ss'inma  "wer einen  Ä-Stengel  fallen  lässt  in  .  ."  N.  loo. mit  dpa  (Kaus.)  'leer  sva.  schwach, (Ohren)  stumpf  machen':  narqm  mii:rö.- drujqm  .  .  apa  gaola  taosayeiti  Vt/0.48. mit  upa  Kaus.  dnwS.  2 :  yS  .  .  vars- sas^a  hqm.räsaydti  . .  srvaica  upa^wsr»- sinti  a'ka  d'tm  *upa.taosayäti  *utiähva  dim ralsayaca  (sd.)  V.  17.2.
11897:auf  diese  Weise',  zurückweisend;  a)  avavat kavaim  ^armd  ya%a  yat  .  .  us./ravayBit (sd.)  . .  f  asti  kavalm  ifarmS  %rä^nm  . . Yt.  ig.  6Bi  b)  als  Korrelat  von  iya^ 'wie':  s?rao^  ita  astü  .  .  hyaf  paour- vXm  f  ust3mfm(sd.)cyt  Y.  56.  i,  Vr.  g. 7.  c)  bei  elliptischer  Ausdrucksweise im  Sinn  von  'das  (Gesagte)  gilt  ,  .':  Aaea hä  vaxiat  [.  .]  mailyai  xsape  palrisacäiti t°  Aatna  t°  *ami.gäme  ".  .  das  gilt  im Winter,  das  im  Sommer"  N.ji;  48',  103Q); —  tat^giiniakva  %rigamlm  f  lkaesaAe{sA.) f  *vtkayehe  f  arüaAe  f  arikavanS  F. 2jb.  7)  wie  unser  schwach  toniges  (zeit- liches und  räumliches)  'da'  zur  Belebung einer  Schilderung  (usw.):  na  t°  para.- irihyeiti  avi  jqfnavS  raonqm  a  f  mirTy^m .tisvazaitcupa  tarn  kiArptm  fratauAaraiü \..3t°  msnyim  utvazaite  ,  .  avi  bar^i- navs  gairinam  . .  nä  f  frasusaUi  .  .  upa
14140:•  j.  drij-av-,  g.  drigav-  :  g.  *dr^u-'^  Adj. (fem.  j.  rfrJrr-)" 'arm,  bedürftig,  schwach': yat  iprsnaoiti  'yaos  havat.masS (sA.)  manS ya^a  ..Y.lO.  13:13;  —yim  *'yBsat  (HS.) *a^.tial^  xbayäti  Yt/o.  84;  —  *'yaos asl>.tkaisaAe  P.  44;  —  ^rJySidyai  (sd.) •gäm  yüwt/lkfm  H.34-1;  —  sraoiB  'yäm 'krijß.t?ms  isA.)  \i..it.y,  —  *'yüm^n  °rT- vTmca  P.  26;  —  ys  -fagim  **rlvayasla " amaval  nmän>m  harnJästi  \.5~.io;  - tat  mäsdä  tavä  x/t^rtm  ya  .'r^hjyöi  däfij 'gaove*^  vahyg  "dein,  o  M.,  ist  die  Herrsch-
14384:•  j.  ^Tvay-  V,  'Furcht  erwecken;  —  hegen'. Praes.  a  %waya-,  3  %wya-.
14385:"Furcht  erwecken' :  %wyatit-  (nur  Ableit).
14907:•  j.  ^a\M{s.har)tar^  m.  'der  bewacht,  Be- wach«': tarn  vamänahe  paiW^  niSkanta ahi  aäruzam  "du  bist  der  Be-,  der  Über- wacher des  Gcmeindebeiirks  derer,  die.." Yt  10. 80.
```


## [2026-09-05T20:55:28.258Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '10180,10200p' BRT.txt"
}
```


### [2026-09-05T20:55:28.308Z] TOOL RESULT

```
Ableit.  —  Vgl.  väitryävariz:  —  Pu.:  *iir vat:ltrir.  —  ')  Hds.  gavJ  varj}.
•  j.  gavästrya-varaza-  n.  'Verrichten landwirtschaftlicher  Arbeit*:  'sa  F.  21.
lü.:  i-är  varzünlh.
•  j.  gavästryavarä't«ma-  Adj.   'der  die
dby  Google
511  gavaza-  -
landwirtschaftlichen  Arbeiten  am  besten vcmchtet":  aiihwS^attma  -mq  narqm asäunqm  Y.  7j.  i.
Pü. ;  kär  varvlärlum,  Sü. :  kätyakariftantak.
•  j.  gav-äza-  m.  'Gerät  zum  Antreiben des  Viehs',  Du.  'die  beiden  Geräte  z.  A, d.  V.',  d.  i,  'Stachel  und  Peitsche':  yalsqm
eayanam  västryehe  fSuyantS  .  .  gaväzista (sd.)  '-izs  (ND.)  \.  14.10.
np.  f,'aväs;  s.  Hbm.  AGr.  z.  126.  —  Pü. :  gJV
•  j.  gav-äzista-'*  Adj.  'der  das  Vieh  am besten  antreibt,  womit  man  das  Vieh  am besten  antreiben  kann':  'zistaQiD.)  ffava:;J (sd.)  "Stachel  und  Peitsche,  womit  man das  Vieh  am  besten  antreibt"  V.  ;4. 10.    1
Superl.  lum  V.  ai-».  —  Pü.:  unklar  (dadan  | k  o  a  r  •  ad  k).  —  '}  Da»  »offälliee  langje  ä  ^ iai   vll.    durch    xmiäza-    »eranlasst;    ».    aber  1
j.  gav5.slän°  V.  /J.  29 f.!  lies  gaosi',  i
•jC  g)  'gar- V. 'wachen'.  Praes.  22  +  14J
(Inkoh,)7r<ja-'',  z^jayäraya-'^,  3o(Kaus.) gäraya-,  7  +  30  (Kaus.)  yräraya-,  yräyrä- ya-i*;  Tert  1  /ayär-, ßyar-,jayar-.  —  Inf, gairf,  'yrärayd.
i)  "wachen':  aisS  ralufrH  *yS  jayüra N,  IQ  (s.  unten  zufrä-);  —  'hwqm  iarasca xsapan?m  ..  jayärayantim''  "dich  der dieNacht  überwacht"  Vyt.^/;  —  PPfA./a- ysurvak-,  jiysurvah-  sbes.  2)  'wachen über  — '  (Akk,):  s.  gain  Inf.
mit  ä  Kaus.  'wecken':  ä  %wä  ülar>m gärayemi  var^hJus  maiianhd  zao%rSbyö Any.i;  1'.
nät/rä  1)  Inkoh. 'aufwachen':  h3  s^af- iiä'ia  frayris>mnS  H.  /.  13;  —  x^a/ttät /rayris;»Nnauqmll.i.i3\ai.  2)Kaus. 'aufwecken': rt'fl.^Mi'  dahmät  aoxte *frii'i^  mä narf  *gärayBis  yat  ratus  frilsis  *äjasäl'^ vXiaiti  dim  frayrärayS  nOitfrayräyräyäti aliff  ratufris  *yd  jayära  "Ein  D.  sagt  zum andern:  'Weck  mich  auf,  Mann,  wenn  die Gebetastunde  kommt'.  Der  iibemimmts ihn  zu  wecken,  bringt  ihn  aber  nicht wach.  (Dann)  ist  der  r.,  der  wach  war" N.  ig;  —  sraesB  a^'Ö  aotn  mtnyim  fra- yrsrayeifi  pars.dari  tiqma  V.  /tS'.  33,
Vgl'  fti.  jäi^rli  "er  wachl',  woss.  rfal-Sänun 'wecken'.  S.  noch  Fü.  und  zajajiiiivaJi.  No.  3. —  Pu.  (luH.  /)!  /rä/  Z'ijp-äyisHUi),  (lu  V.  jS): Jräi  dn  p  r  äj'f/*)  -  in  der  np.  Paraphrase  bei Sp.  Komm.  I.  391:  bidär  gatdad -,  (w  N.)i anpr  ivilmh,  dnnpi  äj'/i«**«.  — OS.iBild. S  142  mil  JSCHMIDT  KZ.  J7.  34,  Bgm.  GrGr.3
'gar-  A  a
```


## [2026-09-05T20:55:42.166Z] TOOL CALL #39: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['MON','BQT','ARY','IEC','POK','AHD','HRN']:\n  print(k, json.dumps(d[k],ensure_ascii=False,indent=1)[:1500]); print('----')\n\""
}
```


### [2026-09-05T20:55:44.162Z] TOOL RESULT

```
MON {
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
  "/home/sfmqrb/git/rishe/data/ver
----
BQT {
 "title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)",
 "kind": "archive_djvu+local_scan_ocr",
 "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.com/file/8230741184/borhane_ghatee_jelde_4.pdf.html (م–ی, 553 pp), vol 5 https://s3.picofile.com/file/8230741300/borhane_ghatee_jelde_5.pdf.html (تعلیقات, Amir Kabir 5th pr. 1376, 293 pp). Same set behind login on ketabnak.com/book/55304-55307 and /58249.",
 "lookup_hint": "grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \\f; leaf N = N-th \\f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={
----
ARY {
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
 "notes": "Image-only PDF provided by the owner (2026-09-04). Use as an additional modern source alongside Wiktionary/Cheung/Hasandust when judging Persian arrows; cite as ARY:<page>. | full OCR text fas+eng (headwords in Persian and Latin 
----
IEC {
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
----
POK {
 "title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)",
 "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/indogermanisches01pokouoft",
 "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt",
 "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\\data\\ie\\pokorny&root=config",
 "notes": "Nourai's page numbers are Band I 1959 pages, which match these scans. Band II (1969 index) is at pokorny-indogermanisch
----
AHD {
 "title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)",
 "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)",
 "kind": "archive_djvu+website+archive_restricted",
 "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only",
 "identifier": "watkins-american-heritage-dictionary-of-indo-european-roots-1985",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt",
 "page_offset": "1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.",
 "lookup_hint": "Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English der
----
HRN {
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
----
```


## [2026-09-05T20:55:49.357Z] TOOL CALL #40: Bash

```json
{
 "command": "timeout 300 python3 tools/ref_page.py BQT:995 2>&1 | head -60"
}
```


### [2026-09-05T20:55:51.311Z] TOOL RESULT

```
no scan of BQT covers printed page 995 (see 'scans' in refs_online.json)
```


## [2026-09-05T20:55:54.145Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"pdf page\" BQT_v2_pages.txt | head -5; echo ...; grep -c \"\" BQT_v2_pages.txt; echo \"== find zar entry\"; grep -n \"زار : \" BQT_v2_pages.txt | head -20"
}
```


### [2026-09-05T20:55:54.220Z] TOOL RESULT

```
...
41071
== find zar entry
```


## [2026-09-05T20:56:01.098Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npp=t.split('\\f')\nprint('leaves',len(pp))\nimport re\nfor i in (0,1,2,300,440,445,450,455,460):\n    if i<len(pp):\n        s=pp[i].strip().replace('\\n',' | ')[:200]\n        print(i,'>>',s)\nEOF"
}
```


### [2026-09-05T20:56:02.889Z] TOOL RESULT

```
leaves 684
0 >> 
1 >> ‫‪7‬‬ |  |                           ‫رن‪۳‬‬ |     ‫نات‬ |       ‫ا م‬ |               ‫لض‌بال ‪ ۰ ۲۶‬رک‬ | ‫‪۱‬‬       ‫اسا تعدولیدیارتم و‬ |                                      ‫‪7‬‬ | ‫‪ ۰‬و زل رس
2 >> ‫م‬ ‫و‬ | ‫نآکو سخنیم بیاموزد مرا‬ |                        ‫د‬ ‫د‬ ‫ل‬ ‫ج‬ ‫م‬ ‫ة‬ ‫چ‬ ‫ا‬ ‫ی‬ ‫د‬ | ‫على ‪۰‬‬             ‫بند گر دا ند ‪۰‬‬                       ‫‪۳‬‬      ‫‪۳7‬‬ |  | ‫داربان مقدم
300 >> ‫رح‬ |  |  ‫ولام وسکون‌الی‬      ‫در لك ‪ = ۳‬تکراول‬                         ‫در لك = بقتح اول بروزن قدك‪,‬دستارجه‬ | ‫وکاف ‪ .‬جام کوناه قد آستن کوناه پیش واز را‬                 ‫رگاونند که رومال و
440 >> ‫هی ‪۷۹۳‬‬ |                                                                                                      ‫روغنای‬ |                                                  ‫کف‬        ‫واو‬ |       
445 >> ‫ره آورد‬                                                                                                     ‫ها‬    ‫سا‬ |  | ‫روبین خم است کهکوس و نقارة بزرکه باشد ‪.‬‬                       ‫روبین
450 >> ‫اس‬                                                                                                  ‫رىژك‬ |              ‫ماضی ریدن و لجاست کردن باشد ‪.‬‬                          ‫وآرزو و هوا وهوس
455 >> ‫گفتار یازدهم‬ |     ‫از کناب برهان قاحطمردرف زای تقطه‌دارباحروف تبجی‬ |                             ‫مبتنی برهیجده ‪ "۲‬بیان وم‬ |      ‫پحتاوینبصرد و هشتاد و يك‬ |                                   
460 >> ‫پر هه‬ |                                                                            ‫کنایه ازطعنه وسرزش باشد ‪.‬‬ |  |  ‫ز‬ |  ‫یر‬‫چ ه‬ |      ‫» بچ‬         ‫ق‬ |                   ‫ازن‬ |
```


## [2026-09-05T20:56:14.368Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npp=t.split('\\f')\n# find page numbers printed as persian digits at leaf starts\ndef digs(s):\n    m=re.findall(r'[۰-۹]{3,4}',s[:300])\n    return m\nfor i in range(430,470):\n    print(i, digs(pp[i]))\nEOF"
}
```


### [2026-09-05T20:56:16.120Z] TOOL RESULT

```
430 []
431 []
432 []
433 []
434 []
435 []
436 []
437 []
438 []
439 []
440 ['۷۹۳']
441 []
442 []
443 []
444 []
445 []
446 []
447 []
448 []
449 []
450 []
451 []
452 []
453 []
454 []
455 []
456 []
457 []
458 []
459 []
460 []
461 []
462 []
463 []
464 []
465 []
466 []
467 []
468 []
469 []
```


## [2026-09-05T20:56:21.408Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npp=t.split('\\f')\nimport re\nfor i in range(455,540):\n    s=pp[i]\n    if 'زاری' in s or re.search(r'زار\\b',s):\n        print('=== leaf',i)\n        # print lines containing زار\n        for ln in s.split('\\n'):\n            if 'زار' in ln: print('   ',ln.strip()[:160])\n        break\nEOF"
}
```


### [2026-09-05T20:56:23.229Z] TOOL RESULT

```
=== leaf 456
    ‫کم خورد وضعیف ونحیف و نانوان شده باشد ‪-‬‬                            ‫خورش‬       ‫مخفف زار‬           ‫‪ ۸‬د‬    ‫راحو رش‬
    ‫رك ‪ :‬زارخورش ‪.‬‬           ‫‪۵۸‬‬             ‫رك‪ :‬زاح‪.‬‬      ‫‪-‬‬    ‫‪۲‬‬         ‫سور‪.‬‬       ‫رکه‪ :‬زاج »‬        ‫‪-‬‬   ‫‪1‬‬
```


## [2026-09-05T20:56:34.058Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npp=t.split('\\f')\nhits=[]\nfor i,s in enumerate(pp):\n    m=re.findall(r'[۰-۹]{3,4}',s)\n    if m: hits.append((i,m[:4]))\nprint(len(hits))\nfor h in hits[:60]: print(h)\nEOF"
}
```


### [2026-09-05T20:56:35.853Z] TOOL RESULT

```
604
(1, ['۳۴۳۱'])
(3, ['۶۵۳۱', '۱۵۹۱', '۳۱۳۱', '۵۲۹۱'])
(4, ['۱۳۳۱', '۱۳۳۱', '۹۷۳۱', '۳۳۳۱'])
(5, ['۵۰۱', '۱۳۳۱', '۹۰۳۱', '۳۵۳۱'])
(9, ['۷۱۵', '۳۲۱', '۷۰۱', '۳۲۱'])
(10, ['۳۷۲', '۸۹۲'])
(11, ['۱۷۸۱', '۳۱۱', '۲۱۱', '۲۸۰'])
(12, ['۰۹۲', '۰۵۲', '۲۵۲', '۲۷۰'])
(13, ['۱۳۱', '۶۱۲', '۹۹۱', '۸۷۲'])
(14, ['۳۰۱'])
(15, ['۲۱۲', '۹۸۳'])
(16, ['۲۲۱', '۳۵۹', '۷۱۸', '۹۳۵'])
(17, ['۸۹۱', '۱۲۳۱', '۷۵۳', '۰۲۳۱'])
(18, ['۲۸۱', '۰۰۸۱', '۱۵۳', '۷۷۲'])
(19, ['۵۹۲۱', '۳۹۲۱', '۷۷۲', '۰۹۲'])
(20, ['۵۷۵۷', '۸۵۵۸', '۲۷۵۷', '۷۷۲'])
(21, ['۲۷۱'])
(24, ['۳۱۵', '۰۹۲', '۰۵۷', '۷۷۰'])
(25, ['۰۰۱'])
(26, ['۵۱۱'])
(27, ['۹۵۳'])
(28, ['۸۵۲', '۸۱۲'])
(29, ['۱۶۲', '۲۱۵۷', '۵۵۷'])
(30, ['۸۳۵', '۲۵۲'])
(31, ['۷۵۲', '۷۲۲'])
(32, ['۹۲۲', '۶۹۲', '۵۷۵', '۲۷۲۷'])
(33, ['۹۲۲'])
(34, ['۱۵۳'])
(35, ['۲۱۷'])
(37, ['۹۸۱'])
(38, ['۸۸۰', '۷۱۱'])
(39, ['۹۱۲', '۲۶۰', '۳۵۸', '۲۵۳'])
(40, ['۳۳۵', '۱۰۱۰', '۹۲۱۰', '۰۳۱'])
(41, ['۸۰۳', '۱۱۵۷', '۹۷۱', '۳۷۱'])
(42, ['۱۸۱', '۱۰۳', '۳۰۳', '۵۲۳'])
(43, ['۲۵۳', '۰۹۰'])
(44, ['۷۱۱', '۸۹۱'])
(45, ['۳۹۹', '۲۰۲', '۱۵۳'])
(46, ['۷۱۱', '۶۲۲'])
(48, ['۹۳۲', '۱۶۲', '۷۷۲', '۶۲۱'])
(49, ['۵۲۲', '۱۷۳', '۶۷۳', '۰۰۲'])
(50, ['۷۲۳۱', '۹۲۳۱', '۹۲۳۱', '۳۱۱'])
(51, ['۹۹۳'])
(52, ['۲۸۱'])
(53, ['۵۷۷', '۹۱۱', '۵۰۳۱', '۰۵۲۲'])
(54, ['۶۳۰', '۷۰۱', '۸۰۱'])
(55, ['۹۷۱', '۸۷۱', '۷۸۳', '۷۲۰'])
(57, ['۷۸۷', '۷۱۱', '۵۵۱', '۲۲۱'])
(58, ['۳۱۱'])
(59, ['۰۷۲', '۰۷۲'])
(60, ['۷۵۸', '۷۷۷', '۸۷۰', '۸۷۰'])
(61, ['۷۷۲', '۹۱۱', '۷۱۲', '۳۱۱'])
(62, ['۷۳۳', '۲۰۳', '۸۱۷'])
(64, ['۳۷۲', '۲۳۱'])
(65, ['۷۳۱۷', '۹۷۲', '۱۸۱', '۳۱۱'])
(66, ['۱۳۳', '۰۷۲'])
(67, ['۹۵۱', '۱۹۲', '۵۷۲۲', '۲۸۱'])
(68, ['۱۰۳', '۹۰۳', '۱۱۱'])
(69, ['۳۹۳', '۹۷۲', '۸۱۳'])
(70, ['۰۰۳', '۷۱۱', '۲۹۲', '۱۲۱۰'])
```


## [2026-09-05T20:57:13.502Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in BQT_v1_pages.txt BQT_v2_pages.txt incoming/BQT/BQT_v3_pages.txt incoming/BQT/BQT_v4_pages.txt; do echo -n \"$f leaves: \"; python3 -c \"\nimport sys;print(open('$f',encoding='utf-8',errors='replace').read().count('\\f')+1)\"; done"
}
```


### [2026-09-05T20:57:15.407Z] TOOL RESULT

```
BQT_v1_pages.txt leaves: 777
BQT_v2_pages.txt leaves: 684
incoming/BQT/BQT_v3_pages.txt leaves: 721
incoming/BQT/BQT_v4_pages.txt leaves: 553
```


## [2026-09-05T20:57:35.168Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npp=t.split('\\f')\nimport re\nfor i in (455,456,457):\n    s=pp[i]\n    s=re.sub(r'[‎‏‪-‮]','',s)\n    print('==== leaf',i)\n    print(s[:2500])\nEOF"
}
```


### [2026-09-05T20:57:36.863Z] TOOL RESULT

```
==== leaf 455
                                 گفتار یازدهم
    از کناب برهان قاحطمردرف زای تقطه‌دارباحروف تبجی
                            مبتنی برهیجده  "۲بیان وم
     پحتاوینبصرد و هشتاد و يك
                                       لفت و کنات



                                            بیان اول
        دژرای نقطه دار با الف مشتمل برهشتاد ونه لغت و کنات
خود را پرباد کند و دبگری چنان دستی برآن             » ۲پروزن باب» سمعنی‌صفت      #راب



رابگر  = ۴بکان فارسی » بر وزن                      ایا  - ۴بروزن‌باب؛ زبلسفوتپازد()0
   ومعتی زابغر است ونآرا زبلغ لیز کوبند .                               زر وطلا وزر سرخ باشد.


دهان | ولابت سیستان است ٩  -ونام قومی وجماعنی‌هم         ی
                                                          ک که
                                                             مضموم برای بی‌نقطة زده»آن باشد

                           ویاز لد ۱   ژد     ) (۱جك       (هژده).    :هرده   ) (۱چك


  حرف سیزدهم از الفبای فارسی وحرف بازدهم از القبای عربی (ابتت) و حرف            3 #
 باجزد » و«آزنرااء» و برای تشخیص « زای هوز » و «زای مثقوطه » و « زای معجمه »   هف
                                                                             اتم
  کوبند ودر حاب جمل هفت گیرند  .اين حرف به «ج» « ,چ» « .غ» و«س» بدل شود ر(که:
                                                            ص بح دیباچة مولف ) .
   - ۱از دساتیر و «زاییده» بمعنی موصوف ! «فرهنگه دساثیر  ۶ ۸4۹فاب ۱ص .۷4
       (( 07ر کت  :دابا )  ,بهلوی  , ۲02زر « بونکر  ۳۸و۸۰۱             هزه 3       ۴
  بپلوی
      ® -           = ۴زاشر («.م۲ ).              و = 5زایگر = زغر = زیگر (ھ.م.).
  .ام آن از نام قبِلهٌ آل ۷۷22ازهونهای سفید (حیتالیان) که‌این ناحیه را درقرن 0
  پنجم میلادی اشغال کردند  ۰مأخوذ است(مار کوارت .شهرستانهای ابراشهر«:»۸۸-۹۸غزنینوآن
   ناحیت هاکه بدوییوسته است همه رابزایلستان بازخوانند ( ) .حدردالمالم  ) ۹رکه  :زارل .

==== leaf 456
  ~~                                                                                                                       زایدن
 که نقیض بنده باشد  ۴۱و بممنی فرزند آدمی                                          هت  -ونام شعبه‌ایست از موسیقی .
زکارةبنیوده شده از اسب و خر و غیره نیز
                                     و                             رالیدن  = ۲پروزن خوایندن ,به‌عنی
ماضی     و    نمعتی زاییدن ۱       و    -0       ۲مده است
                                                                                  موصوف شدن باشد هفتی اصزفات .
زابیدن هم هست بعنی زایید  -۱۷و بمعنی سن                            راج س بر وزن باح  ۰معرب زاکه ۴
را تفر   سااشورده      هم گفته اند لهذا مردم          سال   و
                                                                   است » ۴وآن جوهری باشدکانی شبیه بنمك ۴۔
«بزاد برآمده» خوانند  -ودر عربی توشة راه را                        نوزابیده را لیزتا هفت روز زگاوحینده ؛
                                                                                                         وزن
                                               گونند ؟.۷                   و بابن ممنی با جیم فاردی هم آمده اتر
 راد خو  ۴بخاای نقطه‌دار ( )۱بر
   وزن نازیو  ۰پر فرتوت سالخوزده را گونند :
                                                                    شادی وجشن وسوری باشد که در هدگام زابیدن

 ازدخور -۱با واو سدوله و سکون                                                                      زنان وابام ولادت کنشد .
 رای فرشت  ۰سمعتی زادخواست که بیرسالخوردءٌ
                                                                    راچه یه بر وزن یاچه » بمعنی دوم
 یشندومعنی محذف واومعدوله‌هم گفته‌اند
                                    ابا
                                      فرتبوت                        زاج است که زن نوزاییده باشد * وبا جیم ابجد
                                       که»زادخر باشد .                                                        لمز درست است .

 رادخوست  ۰٩با واو ممروف بر                                         دمرخت
                                                                         راخل  -بر وزن داغل  ۰نا
 وزن نازیوست * بمعنی زادخور است که پبرسال                         زفوم است؛ وىجای خای نقطه دارجیم همگفتها ند
 رشخصی را نز گفته‌اند کهچىزى                 باشد ك   حورده                        ۰أله اعلم.            ولیکن به‌عی در<ت

 کم خورد وضعیف ونحیف و نانوان شده باشد -                            خورش       مخفف زار            ۸د    راحو رش
 و شخصی را نیز گونند که هر چه دارد صرف                              است بمع
==== leaf 457
     اززتشت                                                                                                               -
                                                                                                                          ی


باشد اعم      به اسزخن
                     نا-
                       راد دکهن                             ۹               ۵
                                                       ر ادسم = بفتح شین فرشت بر وزن
                                                                                       ۳     ۹۳                رده



                 از نك وید e .                        یاب است وبسی گویندام
                                                                          سدر
                                                                            ارخفمر.ناامپ
                                                                                       چا
 ناههبه از هردر
              رادۀ شش دکور                                              اچفدراسیاب است که پدرپدر باشد .
                           حهان واز مخلوفات است .      وزن لاجورد ؛
                                                                  ردم
                                                                    بمراذمر د  = ۴با
 راد هر یح = کنابه از آهن ات                           آزاد مرد است که جوان مرد و کریم                                       مخفف
 که ازان سیخ ومیخ وزنجیر وامثال آن‌سازند.                                                   باشد .٩           همت        صاحب
                                                                                                                             و
 داد س بروزن لار .بمعنی مکان روبیدن                    رادو بو ك  بابای ابجدبروزن تارویود.
 باشد همچو گلز ار ولاله‌زار وغله زاروعلف زار -         اسیاب           وئمام سرمابه و        تست       و       کنابه از هت
کے       و نمعتی البوهی و بیاری هم آمده است ٩
                                                                                                           و سامان باشد .
 وضمیف و سیف و خوار خوفیف  - ۷و الان                    f                                  روزن2           ۴         مدار
 وگربان -و گربه کردن بسوز را نیز گنته‌اند- ۸
                                                       زاداست           ساده  .بمعنی               =           ز ا۵ه


                                                                    شده وزایده باشد . ۴            یده
```


## [2026-09-05T20:57:58.610Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"بیدار:\" MON_part1.txt | head; echo \"---\"; grep -n \"بیدار\" MON_part1.txt | sed -n '1,40p' | grep -n \"\" | head -40"
}
```


### [2026-09-05T20:57:58.695Z] TOOL RESULT

```
26856:بیدار: 01427 (ص..) کسی که در خواب 
---
1:3669:گ .) نارون. (گیا ۰ سبیدار. 
2:6343:پگاه خیزانیدن» به وقت از خواب بیدار 
3:12686:استیفاظ: 7اه [ع.] (مص‌ل.) بیدار 
4:12689:بودن» بیدار شدن. هشیار بودن» هوشیار 
5:17176:تحار کف (امص.) آ گاهی بیداری. 
6:17205:احساسات و عواطف را در او بیدار و 
7:25060:برخیزانیدن. بیدار کردن از خواب. 
8:26823:بیخواب: اقا (ص‌مر.) بیدار. آنکه 
9:26856:بیدار: 01427 (ص..) کسی که در خواب 
10:28166:شبانروز عمدا بیدار باشد؛ پاسبان» نگهبان. 
11:38557:بیدار بودن. یکث یک اد گرفتن. (اسص.) 
12:43958:هوشیار شدن. (امص.) بیداری. بیدار مغزی» 
13:45289:(امص.) شب بیداری» شب زنده‌داری؛ ج. 
14:45674:تبقط: 12۷277 [ع.] (مص‌ل.) بیدار شدن از 
15:45675:خواب؛ هوشیار گردیدن. (امص.) بیداری؛ 
16:50049:بیداری» خواب سبکث» پینکی. 
17:50575:بو و و ریت دیدن. (مصل.) (کد.) بیدار 
18:51600:آن تخته می‌زد تا پاسبانان از صدای آن بیدار 
19:57680:نوم؛ مق. بیداری» یقظه. غفلت. پرز جامه 
20:66351:گویند و آنجه که در بیداری دست دهد 
21:74070:معین زنگ زند و خفته‌ای را بیدار سازد. 
22:74724:ساهر: 56 [ع.] (افا.) بیدار. 
23:81554:سهر: »22: [ع.] (مصل.) بیدار ماندن به 
24:83872:پیماید. شب بیدار. صاحب درد و رنج» 
25:83910:کسی که شب از خواب برخیزد و بیدار 
26:83960:بیدار. پارساء زاهد. عسس» شبگرد؛ داروغه. 
27:83964:شب راه رفتن یا سفر کردن. شب بیداری. 
28:86569:لحظهٌ معینی شخص خواییده را بیدار سازد. 
29:91163:آب؛ خواب» بیداری» ما کولات و 
30:92212:بیداری سربازان و دیگران نوازند. طبل
```


## [2026-09-05T20:58:02.643Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '26856,26866p' MON_part1.txt; echo \"=== ghorridan MON2\"; sed -n '1541,1545p' MON_part2.txt; echo \"=== search غر:\"; grep -n \"^غر\" MON_part2.txt | head -20"
}
```


### [2026-09-05T20:58:02.738Z] TOOL RESULT

```
بیدار: 01427 (ص..) کسی که در خواب 
نباشد؛ مق. خوایده. آ گاه» هوشیار» متنبه. 
سیداردل: ۵۵-.۷(ص‌مر) دلآگاه» 
هو شیار؛ مق. غافل. 

بسیدبرگ: :۱4 (امر.) (گیا.) برگ 
درخت بید. نوعی از پیکان تیر شبیه به برگث 
نك . 


بید خحت: ۱۵-0۷ [- بذخت - بغ‌دخت» 
=== ghorridan MON2
غریدن: ۰۲-1۵:0:(اصت. مص‌ل.) (غربده 


۰ موم ۰ 
فر هنک فار سی‌معین 
=== search غر:
682:غربال بند. فالگیر. 
885:غر: ۲(ص.) زن فاحشه؛ قحه. بد دل. مرد 
886:غر: ۸« [مخف. غرد] (.) خانهٌ چوبین و نثین؛ 
889:غر: :[- قر] (ا.) جنباندن جزو یا تمام بدن 
895:غروفر: غر و غمزه. آرایش و زینت. 
897:غر: :0:(ص.) شخصی که خصیه‌اش بز رگك 
904:غر: ۲ (اصت.) آواز غوکث» صدای وزغ. 
905:غر: 0:(ص.) ترکیده و شکسته. فرورفته بر 
908:غراء: 2 [ع. فو: غرا] (ص.) مونث 
923:غرابت: 73202۱ [ع. غرابه | (مص‌ل.) 
925:غرابت استعمال: (ص.) آوردن کلمهٌ مهجور 
932:غرابی: -7۵۲3 (ص‌نسه.) نوعی خرما. 
942:غرابیه: (۳9«)۵ه« (ع.] (ص‌نس. (.) 
946:غراچه: (۵-)۸۲5۵۵( [- غرچه | (ص.) نامر د» 
948:غرار: :۱*8 [ع.) (مصل.) گول خوردن» 
953:غرار: ۲ (ع.] (ص.) مکاره خداع» 
956:غرار: ۲ ابر بزی خرار» خرال» خارال.] 
958:غرارت: 2 [ع. غرارة] (مص‌ل.) غافل 
963:غراره: (0-)۲۵۲۵ هر (۱,) آب در دهن کردن و 
965:غراره: (۵۲2۲۵)۵ (ا.) نوعی از سلاح
```


## [2026-09-05T20:58:17.919Z] TOOL CALL #50: Bash

```json
{
 "command": "sed -n '1,40p' tools/fetch_source.py; echo ...; grep -n \"def main\\|argparse\\|print(\" tools/fetch_source.py | head -20"
}
```


### [2026-09-05T20:58:17.979Z] TOOL RESULT

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
...
29:def main():
36:        print(__doc__); return 2
47:        print(path); return 0
74:    print(path)
```


## [2026-09-05T20:58:29.035Z] TOOL CALL #51: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/%D8%A8%DB%8C%D8%AF%D8%A7%D8%B1\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%81ger-\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ger%CA%B0h%E2%82%82no-\" \\\n \"https://www.etymonline.com/word/geranium\" \\\n \"https://www.etymonline.com/word/crane\" \\\n \"https://www.etymonline.com/word/Gregorian\" \\\n ; do echo \"### $u\"; timeout 90 python3 tools/fetch_source.py \"$u\" --note \"page 175 (Ger 3 / Ger 4): PIE *h1ger- 'awake' and *gerh2- 'cry hoarsely/crane' chains\" ; done"
}
```


### [2026-09-05T20:58:33.460Z] TOOL RESULT

```
### https://en.wiktionary.org/wiki/%D8%A8%DB%8C%D8%AF%D8%A7%D8%B1
/home/sfmqrb/git/rishe/data/verification/sources/web/016a80311b8a0e7c.txt
### https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%81ger-
/home/sfmqrb/git/rishe/data/verification/sources/web/aebb52dafcfc90dc.txt
### https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ger%CA%B0h%E2%82%82no-
/home/sfmqrb/git/rishe/data/verification/sources/web/0e99ba8699bd1f15.txt
### https://www.etymonline.com/word/geranium
/home/sfmqrb/git/rishe/data/verification/sources/web/999431fa13b3646c.txt
### https://www.etymonline.com/word/crane
/home/sfmqrb/git/rishe/data/verification/sources/web/2724274659af69bd.txt
### https://www.etymonline.com/word/Gregorian
/home/sfmqrb/git/rishe/data/verification/sources/web/9bf6fbb1d2b73641.txt
```


## [2026-09-05T20:58:37.404Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 016a80311b8a0e7c aebb52dafcfc90dc 0e99ba8699bd1f15; do echo \"###### $f\"; head -c 100 $f.txt; echo; grep -n -i \"Persian\\|Middle Persian\\|awake\\|crane\\|Descend\" $f.txt | head -25; done"
}
```


### [2026-09-05T20:58:39.177Z] TOOL RESULT

```
###### 016a80311b8a0e7c
URL: https://en.wiktionary.org/wiki/%D8%A8%DB%8C%D8%AF%D8%A7%D8%B1
FETCHED: 2026-09-05T20:58:31Z
STA
57: Persian 
59: Toggle Persian subsection 
159: Persian
165: Metathesis from Middle Persian [script needed] ( wygrʼd /⁠wiγrād⁠/ ) , from Proto-Iranian *wi- + *Hgar- ( “ to be awake ” ) , the former from Proto-Indo-European *wí ( “ apart ” ) , the latter from Proto-Indo-European *h₁ger- ( “ to be awake, to awaken ” ) . Cognate with Sanskrit जागर्ति ( jāgarti ) , Ancient Greek ἐγείρω ( egeírō , “ to awaken ” ) , Albanian ngrē ( “ to lift, to wake ” ) . [ 1 ] 
170: ( Classical Persian ) IPA ( key ) : /beː.ˈdaːr/ 
212: Iranian Persian
218: awake ( not asleep ) 
219: c. 1915 , Abdul Hadi Dawi , Seraj al-Akhbar : چشم پرخوابت اگر بیدار می‌شد بد نبود، کلهٔ مستت اگر هشیار می‌شد بد نبود. češm-e por-xâb-at agar bidâr mi-šod bad na-bud, kalle-ye mastat agar hoš-yâr mi-šod bad na-bud. It would not be bad if your sleepy eyes became awake ; it would not be bad if your drunken head became sober. 
243: Borrowed from Classical Persian بیدار ( bēdār ) .
257: awake , wakeful ( not asleep ) 
264: بیدار کرنا ( bedār karnā , “ to make conscious of, to awaken ” , transitive ) 
268: بیداری ( bedārī , “ consciousness , awakening ” ) 
272: Categories : Persian terms inherited from Middle Persian 
273: Persian terms derived from Middle Persian 
274: Persian terms derived from Proto-Iranian 
275: Persian terms derived from Proto-Indo-European 
276: Persian terms inherited from Proto-Indo-European 
277: Persian terms with IPA pronunciation 
278: Rhymes:Persian/aːr 
279: Rhymes:Persian/aːr/2 syllables 
280: Persian lemmas 
281: Persian adjectives 
282: Persian terms with quotations 
283: Urdu terms borrowed from Classical Persian 
284: Urdu terms derived from Classical Persian 
###### aebb52dafcfc90dc
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%81ger-
FETCHED: 2026-
150: to wake up , awaken 
180: Ancient Greek: ἐγείρω ( egeírō , “ to wake up; to keep watch ” ) ( see there for further descendants )
184: Ancient Greek: ἐγρήγορα ( egrḗgora , “ is awake ” ) 
188: Vedic Sanskrit: जागार ( jāgā́ra , “ is awake; is watching ” ) 
191: Younger Avestan: 𐬘𐬀𐬖𐬁𐬭𐬀 ( jaγāra , “ is awake ” ) 
198: Proto-Iranian: *Hgāráyati ( see there for further descendants )
202: Proto-Iranian: *HgráHscati ( see there for further descendants )
205: ⇒ ? Latin: expergīscor ( “ to awake, wake up ” ) 
209: Proto-Iranian: *HgráHti ( see there for further descendants )
234: ^ Beekes, Robert S. P. ( 2011 ), Comparative Indo-European Linguistics: An Introduction , 2nd edition, revised and corrected by Michiel de Vaan , Amsterdam, Philadelphia: John Benjamins Publishing Company, page 126 : “ The roots *h₁ger- 'to awaken' and *kes- 'to comb', which are often used as counterarguments, are thought to have gotten their K from the zero-grade forms *h₁gr- and *ks- , where depalatalization would be regular. ” 
256: ^ Michele Bianconi, editor ( 2022 ), Ancient Indo-European languages between linguistics and philology: contact, variation, and reconstruction (Brill's studies in historical linguistics), Brill, →ISBN , page 290 : “ Compare the similar-sounding *h₁ǵer-i̯e/o- > ἐγείρω ‘awaken,rouse,stirup’ ” 
###### 0e99ba8699bd1f15
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ger%CA%B0h%E2%82%82no-
FETCHE
```


## [2026-09-05T20:58:46.909Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '140,215p' 0e99ba8699bd1f15.txt; echo \"######## ETYM crane\"; grep -n -i \"crane\\|grus\\|geranos\" 2724274659af69bd.txt | head -12; echo \"######## ETYM geranium\"; grep -n -i \"geran\" 999431fa13b3646c.txt | head -8; echo \"######## ETYM Gregorian\"; grep -n -i \"gregor\\|watchful\\|grēgor\" 9bf6fbb1d2b73641.txt | head -12"
}
```


### [2026-09-05T20:58:46.992Z] TOOL RESULT

```
######## ETYM crane
1:URL: https://www.etymonline.com/word/crane
4:TITLE: Crane - Etymology, Origin & Meaning
6:Crane - Etymology, Origin & Meaning 
21: Origin and history of crane 
23: crane (n.) 
25: large grallatorial bird with very long legs, beak, and neck, Old English cran , common Germanic (cognates: Old Saxon krano , Old High German krano , German Kranich , and, with unexplained change of consonant, Old Norse trani , Danish trane ), from PIE *gere-no- , suffixed form of root *gere- (2) "to cry hoarsely," also the name of the crane (cognates: Greek geranos , Latin grus , Welsh garan , Lithuanian garnys "heron, stork"). Thus the name is perhaps an echo of its cry in ancient ears.
27: Misapplied to herons and storks. The gray European crane was "formerly abundant in marshy places in Great Britain, and prized as food" [OED], but was extinct there through much of 20c.
31: crane (v.) 
33: 1799, of the neck, "to stretch or be stretched out," from crane (n.). As "to stretch or bend the neck," 1849. Earliest sense (1560s) is "to hoist with a crane." Related: Craned ; craning .
36: Entries linking to crane 
40: name of the fruit of several species of a swamp-growing shrub, 1640s, apparently an American English adaptation of Low German kraanbere , from kraan "crane" (see crane (n.)) + Middle Low German bere "berry" (see berry ). The reason for the name is not known; perhaps they were so called from fancied resemblance between the plants' stamens and the beaks of cranes.
48: "The fiery cross which in old times formed the rallying symbol in the Highlands of Scotland in any sudden emergency," Gaelic cranntara, cranntaraidh , also (by influence of crois "cross") croistara, croistaraidh , literally "the beam or cross of reproach," from crann "a beam, a shaft" (see crane (n.)) + tair "reproach, disgrace." "[S]o called because neglect of the symbol implied infamy" [Century Dictionary].
######## ETYM geranium
1:URL: https://www.etymonline.com/word/geranium
4:TITLE: Geranium - Etymology, Origin & Meaning
6:Geranium - Etymology, Origin & Meaning 
21: Origin and history of geranium 
23: geranium (n.) 
25: 1540s, from Latin geranium , from Greek geranion , the plant name, diminutive of geranos "crane" (cognate with Latin grus ; see crane (n.)). So called from shape resemblance of seed pods to cranes' bills; the native name in English also was cranebill . As a color name from 1842.
28: Entries linking to geranium 
32: large grallatorial bird with very long legs, beak, and neck, Old English cran , common Germanic (cognates: Old Saxon krano , Old High German krano , German Kranich , and, with unexplained change of consonant, Old Norse trani , Danish trane ), from PIE *gere-no- , suffixed form of root *gere- (2) "to cry hoarsely," also the name of the crane (cognates: Greek geranos , Latin grus , Welsh garan , Lithuanian garnys "heron, stork"). Thus the name is perhaps an echo of its cry in ancient ears.
######## ETYM Gregorian
1:URL: https://www.etymonline.com/word/Gregorian
4:TITLE: Gregorian - Etymology, Origin & Meaning
6:Gregorian - Etymology, Origin & Meaning 
21: Origin and history of Gregorian 
23: Gregorian (adj.) 
25: "pertaining to Gregory," from Late Latin Gregorianus , from Gregorius (see Gregory ). From c. 1600 of church music, in reference to Gregory I the Great (pope from 590-604), who traditionally codified it; 1640s in reference to new calendar (introduced 1582) from Pope Gregory XIII (1572-1585); due to Protestant resistance, the calendar was not introduced in England and the American colonies until 1752.
27: Entries linking to Gregorian 
29: Gregory 
31: masc. proper name, popular in England and Scotland by mid-12c. (Pope Gregory I sent the men who converted the English to Christianity), nativization of Late Latin Gregorius , literally "wakeful" (equivalent to Latin Vigilantius ), from Greek gregorios , a derivative of gregoros "to be watchful," from PIE root *ger- (2) "to be awake" (source also of Sanskrit jagarti "he is awake," Avestan agarayeiti "wakes up, rouses"). At times confused with Latin gregarius (see gregarious ).
35: "pertaining to or derived from Julius Caesar, 1590s, originally and especially in reference to the calendar system that began with his reforms in 46 B.C.E. (superseded by the Gregorian ). The masc. proper name is from Latin Iulianus , from Iulius . The Julianists were a sect of Monophysites who held the body of Christ to be incorruptible; they were named for their leader, Julian, bishop of Halicarnassus (early 6c.).
45: Bolsheviks overthrew the Provisional Government) happened Nov. 7, 1917, but because Russia had not at that time adopted the Gregorian...
83: Share Gregorian
```


## [2026-09-05T20:58:59.431Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '1,10p' 0e99ba8699bd1f15.txt; wc -l 0e99ba8699bd1f15.txt"
}
```


### [2026-09-05T20:58:59.472Z] TOOL RESULT

```
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ger%CA%B0h%E2%82%82no-
FETCHED: 2026-09-05T20:58:31Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found5 0e99ba8699bd1f15.txt
```


## [2026-09-05T20:59:03.934Z] TOOL CALL #55: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/grus#Latin\" \\\n \"https://en.wiktionary.org/wiki/%D8%BA%D8%B1%DB%8C%D8%AF%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%D8%B2%D8%A7%D8%B1#Persian\" \\\n ; do echo \"### $u\"; timeout 90 python3 tools/fetch_source.py \"$u\" --note \"page 175 Ger 4: Latin grus / Persian ghorridan / Persian zar\"; done"
}
```


### [2026-09-05T20:59:07.161Z] TOOL RESULT

```
### https://en.wiktionary.org/wiki/grus#Latin
/home/sfmqrb/git/rishe/data/verification/sources/web/a33b68806c486d3d.txt
### https://en.wiktionary.org/wiki/%D8%BA%D8%B1%DB%8C%D8%AF%D9%86
/home/sfmqrb/git/rishe/data/verification/sources/web/cda28db27cc9d2db.txt
### https://en.wiktionary.org/wiki/%D8%B2%D8%A7%D8%B1#Persian
/home/sfmqrb/git/rishe/data/verification/sources/web/2365de480d76080c.txt
```


## [2026-09-05T20:59:10.732Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"### grus\"; grep -n -i \"Latin\\|crane\\|gerh\\|Proto-Italic\" a33b68806c486d3d.txt | head -12; echo \"### ghorridan\"; grep -n -i \"Persian\\|onomat\\|Etymology\\|FAILED\" cda28db27cc9d2db.txt | head -12; echo \"### zar\"; grep -n -i \"Etymology\\|Middle Persian\\|lament\\|weep\\|FAILED\" 2365de480d76080c.txt | head -20"
}
```


### [2026-09-05T20:59:10.813Z] TOOL RESULT

```
### grus
1:URL: https://en.wiktionary.org/wiki/grus#Latin
91: Latin 
93: Toggle Latin subsection 
371: Latin
374: grūs (a crane) 
380: grua   f ( Late Latin ) 
387: Proto-Indo-European *gerh₂- 
391: Proto-Indo-European *gerh₂ōws der. 
396: Proto-Italic *grūs 
397: Latin grus 
399: From Proto-Italic *grūs , from Proto-Indo-European *gr̥h₂-ú-s (which apparently metathesized to *grúh₂s ), perhaps modified from *gerh₂ōws , in any case from the onomatopoeic root *gerh₂- ( “ to cry hoarsely ” ) which derived several words for birds, especially cranes and crows. [ 1 ] 
401: Cognate with Proto-Slavic *žeravь , Old Prussian gerwe , and Lithuanian gérvė , all meaning “ crane ” . Also related to English crane , but probably not to grouse (of unknown origin). See also Latin grāculus ( “ jackdaw, chough ” ) , Old Norse krákr ( “ raven, crow ” ) , and English crow .
### ghorridan
57: Persian 
59: Toggle Persian subsection 
127: Persian
139: Categories : Persian lemmas 
140: Persian verbs 
### zar
79: Etymology 
102: Etymology 1 
111: Etymology 2 
125: Etymology 
142: Etymology 1 
157: Etymology 2 
172: Etymology 3 
192: Etymology 1 
204: Etymology 2 
218: Etymology 
238: Etymology 1 
247: Etymology 2 
856: Etymology
859: Compare Middle Persian [script needed] ( zpl /⁠zafar⁠/ , “ mouth ” ) .
895: Etymology 1
1036: Etymology 2
1057: Etymology
1161: Etymology 1
1219: Etymology 2
1282: Etymology 3
```


## [2026-09-05T20:59:16.501Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '120,140p' cda28db27cc9d2db.txt; echo \"########## ZAR persian\"; python3 - <<'EOF'\nt=open('2365de480d76080c.txt',encoding='utf-8').read().split('\\n')\nfor i,l in enumerate(t):\n    if l.strip()=='Persian':\n        print('LINE',i)\nfor i,l in enumerate(t):\n    if 'Persian' == l.strip():\n        print('\\n'.join(t[i:i+60])); break\nEOF"
}
```


### [2026-09-05T20:59:37.880Z] TOOL RESULT

```
 Appearance

 move to sidebar 
 hide 

 From Wiktionary, the free dictionary

 Persian
 [ edit ] 

 Verb
 [ edit ] 

 غریدن • ( ġorridan ) ( present stem غر ( ġorr ) ) 

 to roar 

 Retrieved from " https://en.wiktionary.org/w/index.php?title=غریدن&oldid=84916517 "

 Categories : Persian lemmas 
 Persian verbs 
########## ZAR persian
LINE 186
LINE 1323
 Persian 

 Toggle Persian subsection 

 6.1 
 Etymology 1 

 6.1.1 
 Noun 

 6.1.1.1 
 Derived terms 

 6.1.1.2 
 Descendants 

 6.2 
 Etymology 2 

 6.2.1 
 Noun 

 6.2.1.1 
 Descendants 

 7 
 South Levantine Arabic 

 Toggle South Levantine Arabic subsection 

 7.1 
 Etymology 

 7.2 
 Pronunciation 

 7.3 
 Verb 

 7.3.1 
 Conjugation 

 8 
 Urdu 

 Toggle Urdu subsection 

 8.1 
 Pronunciation 

 8.2 
 Etymology 1 

 8.2.1 
 Noun 

 8.2.1.1 
 Derived terms 

 8.3
```


## [2026-09-05T20:59:39.929Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '1323,1400p' 2365de480d76080c.txt"
}
```


### [2026-09-05T20:59:39.965Z] TOOL RESULT

```
 Persian
 [ edit ] 

 Etymology 1
 [ edit ] 

 Ultimately from Proto-Iranian *jāráyati . See it for more.

 Noun
 [ edit ] 

 Dari

 زار 

 Iranian Persian

 Tajik

 зор 

 زار • ( zâr ) 

 groan 

 lament 

 Derived terms
 [ edit ] 

 زار زار ( zâr-zâr ) 

 Descendants
 [ edit ] 

 > Tajik: зор ( zor ) ( inherited ) 

 → Armenian: զար ( zar ) , զառ ( zaṙ ) 

 → Azerbaijani: zar 

 → Georgian: ზარი ( zari ) 

 → Gujarati: ઝાર ( jhār ) 

 → Hindustani: 
 Hindi: ज़ार ( zār ) 
 Urdu: زار ( zār ) 

 → Ottoman Turkish: زار ( zâr ) Turkish: zar 

 → Kazakh: зар ( zar ) 

 Etymology 2
 [ edit ] 

 Borrowed from Arabic زَهْر ( zahr ) .

 Noun
 [ edit ] 

 زار • ( zâr ) 

 die (for gambling)

 Descendants
 [ edit ] 

 → Armenian: զառ ( zaṙ ) 

 → Georgian: ზარი ( zari ) 

 South Levantine Arabic
 [ edit ] 

 Root
```


## [2026-09-05T20:59:48.491Z] TOOL CALL #59: Bash

```json
{
 "command": "timeout 90 python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/j%C4%81r%C3%A1yati\" --note \"page 175 Ger 4 node 3: Persian zar 'lament' proto-Iranian etymon\" && cd data/verification/sources/web && f=$(python3 -c \"import hashlib;print(hashlib.sha1('https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/j%C4%81r%C3%A1yati'.encode()).hexdigest()[:16])\") && sed -n '1,200p' $f.txt | grep -n -i \"etymology\\|Proto-Indo\\|Persian\\|Descend\\|FAILED\\|jar\\|zar\" | head -30"
}
```


### [2026-09-05T20:59:51.509Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/181ddd87f493a9da.txt
62: Etymology 
74: Descendants 
140: Etymology
```


## [2026-09-05T20:59:53.901Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '120,200p' 181ddd87f493a9da.txt"
}
```


### [2026-09-05T20:59:53.966Z] TOOL RESULT

```
 Print/export

 Download as PDF 
 Printable version 

 In other projects

 Appearance

 move to sidebar 
 hide 

 From Wiktionary, the free dictionary

 This Proto-Iranian entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.

 Proto-Iranian
 [ edit ] 

 Etymology
 [ edit ] 

 Secondary causative of *járati . [ 1 ] 

 Verb
 [ edit ] 

 *jāráyati 

 to be angered , vexed 

 to be tormented , pained 

 Inflection
 [ edit ] 

 aya-causative

 Sing.

 3rd

 *jāráyati 

 Plur.

 3rd

 *jāráyanti 

 Active voice

 Indicative

 Imperfect

 Imperative

 Subjunctive

 Optative

 Sing.

 1st

 *jāráyaH(mi) 

 *jāráyam 

 —

 *jāráyaHaH(ni) 

 *jāráyayam 

 2nd

 *jāráyahi
```


## [2026-09-05T21:00:01.865Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && python3 - <<'EOF'\nt=open('181ddd87f493a9da.txt',encoding='utf-8').read()\ni=t.find('Descendants',3000)\nprint(t[i-200:i+1500])\nEOF"
}
```


### [2026-09-05T21:00:03.685Z] TOOL RESULT

```
re ” ) [ 5 ] ( restored -d-? ) 
 Manichaean script: 𐫇𐫏𐫅𐫀𐫡𐫏𐫅 ( wydʾryd ) 
 → Parthian: 
 Manichaean script: 𐫇𐫏𐫅𐫀𐫡𐫏𐫍 ( wydʾryh /⁠widārē⁠/ , 2sg.pres. ) , 𐫇𐫅𐫀𐫡𐫏𐫗𐫅 ( wdʾrynd /⁠widārēnd⁠/ , 3pl.pres. ) 

 Descendants
 [ edit ] 

 Parthian: *zārdēd 
 → Middle Persian: *zārdēd 
 Persian: زاریدن ( zâridan ) [ 3 ] 

 References
 [ edit ] 

 ^ Rix, Helmut , editor ( 2001 ), “ *?*g̑ʰeRH-¹ ”, in Lexikon der indogermanischen Verben [ Lexicon of Indo-European Verbs ] (in German), 2nd edition, Wiesbaden: Dr. Ludwig Reichert Verlag, →ISBN , page 178 

 ↑ 2.0 2.1 Cheung, Johnny ( 2007 ), “ *zarH¹ 'to hurt, wound, anger' ”, in Etymological Dictionary of the Iranian Verb (Leiden Indo-European Etymological Dictionary Series; 2), Leiden, Boston: Brill, →ISBN , page 469 

 ↑ 3.0 3.1 Cheung, Johnny ( 2007 ), “ *zarH³ 'to bewail the deceased' ”, in Etymological Dictionary of the Iranian Verb (Leiden Indo-European Etymological Dictionary Series; 2), Leiden, Boston: Brill, →ISBN , page 470 

 ^ Gharib, B. ( 1995 ), “ 1411 ”, in Sogdian dictionary: Sogdian–Persian–English , Tehran: Farhangan Publications, page 55 

 ^ Cheung, Johnny ( 2007 ), “ *darH 'to have pain' ”, in Etymological Dictionary of the Iranian Verb (Leiden Indo-European Etymological Dictionary Series; 2), Leiden, Boston: Brill, →ISBN , page 61 

 Retrieved from " https://en.wiktionary.org/w/index.php?title=Reconstruction:Proto-Iranian/jāráyati&oldid=92152393 "

 Categories : Proto-Iranian terms derived from Proto-Indo-Iranian 
 Proto-Iranian terms derived from Proto-Indo-European 
 Proto-Iranian lemmas 
 Proto-Iranian verbs 
 Proto-Iranian aya-causative verbs 

 Hidden categories: Pages with entries 
 Pages with 1 entry 
 Parthian t
```


## [2026-09-05T21:00:43.253Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== LEW grus\"; grep -n \"^grus\\|grūs\\|grus,\\|gruere\" LEW_1910.txt | head -8; echo \"== LAT grus\"; grep -n \"grus\\b\" LAT.txt | head -8; echo \"== KLN crane\"; grep -n -i \"OE\\. cran\\|crane, .*OE\\|geranos\\|geranion\" KLN_1966.txt | head -8; echo \"== SKT crane\"; grep -n -i \"CRANE\\|GERANIUM\\|CROON\\|^CUR\" SKT.txt | head -12"
}
```


### [2026-09-05T21:00:43.369Z] TOOL RESULT

```
== LEW grus
10771:grusin II 448
== LAT grus
1202:Les formes romanes remontent A acrus,-a, -um (agrus) qu'on lit dans Mu-acedla
13417:conger, -grl m.(gonger nas., congrus, Gloss.; gungrus Prisc. GLK
13418:II 36,36; gongrus Charis. GLK 184,33): congre, angnille de «er. Ancien,
25476:en latin des noms d'animaux comme grus (v. ce mot) et graculus, le
27034:et grus', gr. ypu, ypu^co, etc.
39488:gr. tieX&C; (auXtoC "ocre ou vermillon", gaul. (?) melinus "color nigrus"
43377:onager (-grus) , -grl m.: emprunt au gr.ovaypoC, depuis Plaute.
44534:pager ( phager, p(h) agrus), -I m. : pagre? poisson mal d^terjnine
== KLN crane
9540:crane,  n.  —  ME.  crane,  crone,  fr.  OE.  cran,  rel. to  OS.,  OHG.  krano,  Du.  kraan,  MHG.  krone, OE.  cranoc .  cornoc,  Ml.G.  kranek,  OHG.  chra - nuh,  MHG.  krancch,  G.  Kranich,  ‘crane’,  and cogn.  with  Arm.  krunk,  Gk.  yspavo c,  Co.,  W., Bret,  garan,  ’crane’,  Lith.  garnys,  ‘heron,  stork’, gene.  Lett,  dzerve,  OPruss.  gerwe,  OSlav.  zeravi, ‘crane’,  L.  grus,  ’crane’.  All  these  words  derive from  the  I.-E.  imitative  base  *ger-,  ‘to  utter  a hoarse  cry'.  Co.  the  first  element  in  cranberry. Cp.  also  Geranium,  the  first  element  in  Grui- formes,  and  the  last  element  in  pedigree.  For  the sense  development  of  crane,  which  denotes  also ‘a  machine  for  raising  weights’  (so  called  from the  long  neck  of  the  instrument),  cp.  Gk. yzpa'jrjc,  ‘crane’  (in  both  senses  of  the  English word).
16051:Geraniaceae,  n.  pi.,  the  geranium  family  (bot.)  — ModL.,  formed  fr.  Geranium  with  suff.  -aceae. geraniaceous,  adj.  —  See  prec.  word  and  -aceous. Geranium,  n.,  a  genus  of  plants,  the  cranesbill (bot.)  —  L.  geranion,  geranium,  ‘cranesbill’,  fr. Gk.  Yepaviov,  of  s.m.,  fr.  yipoLvott,  ‘crane’,  which is  cogn.  with  L.  grits,  OE.  cran,  ‘crane’ ;  so  called because  the  fruit  resembles  a  cranesbill.  See crane  and  cp.  words  there  referred  to.’
27852:pedigree,  n.,  1)  genealogical  table;  2)  genealogy. —  ME.  pedegru,  fr.  MF.  pie  de  grue,  ‘crane’s foot’,  so  called  from  the  shape  of  the  genealogi¬ cal  mark  (,].)  used  to  denote  descent.  MF.  pii (F.  pied)  derives  fr.  OF.  pie,  fr.  L.  pedem,  acc. of  pes,  ‘foot’ :  see  foot  and  cp.  pedal.  F.  de,  ‘of, from’,  comes  fr.  L.  de,  ‘from,  away  from’;  see de-.  F.  grue  comes  fr.  L.  gruem,  acc.  of  grits, ‘crane’,  which  is  cogn.  with  Gk.  yccavoc,  OE. cran ;  see  crane.  The  form  of  the  English  word was  influenced  by  an  association  with  degree. Derivative:  pedigree,  tr.  v. pediment,  n.,  a  triangular  ornament  on  the  front of  buildings  ( archit .)  —  Altered  from  earlier periment,  which  is  prob.  a  corruption  of  pyr¬ amid  (q.v.)
== SKT crane
2946:Capatan.  (F.  — Span.— L.?)  )e.ci\btstan. ^Span.  (c^strantf,  <abrcstante,  an  cnijinc to  raise  weights.  £tym.  uncertain:  but Min&heu'B  Span.  Diet.  0^^3)  ba&  cabtt- itanti  as  the  form,  and  Monlaa's  £tym. Span.  Diet.  (i88i)  has  cabria,  a  crane, and  suggests  Span,  cobra  estantt,  a  fixed (permanent)  goat;  since  the  Span.  eain-A meana  (i)  goat,  (i)  a  machine  for  throw- ing large  clones.  Here  Sp.  ca^^a^L.  i-fl//tf» a  she-goat ;  sec  Oaper  ( i ) ;  and  estantc  =■ L.  sioHtem.  ace  of  x/iimj,  &taudiag,  from ttart,  to  staiid.
4233:CUrftw.  (F.  -  L.)  O.  F.  cavrejru (F-  (otivtr/fu\  a  6re-cover,  covcrit  g  of  hreSp time  for  pulUng  out  fires.  — O  F-  amrir^  to cover  ;  feu,  fire  {  =  L.  focHiH.  ace.  of  focus^ hearth,  fire) :  see  Foouo.
4504:CURE,
4520:Cur,    iScand.)       M    E    rwr»r.- dial,  kurrtt  a  dog   +  O.  Da. hoosc'tiog.     Nomeil  from  grovUug. kurra.  to  murmur.  gruiuUe.
4521:Curate ;  tec  Curo.
4523:Curd.    (.Ci     M.E.  /»r</.  a^» <mth,  grtUk,  GaeL  grtitk,  curds.. (*'wJ,  a  round  lump.
4524:Cure.    (F-L.1     O.  F   «/r»L atteiition.    ^A'iJ/allief!  *-^-  -•
4527:curat©.  (L.)    Low  L curate  :    turarttm    kfn/d  r » -      - wi'b  cure  of  souls.— L  rMni,  cuit,
4533:CURFEW.
4547:CURRY.
4556:curricle.  (L.)  L.  r«rrr'rw/»«i.  a  run- ning :  also,  a  light  car.  —  L  cnrrtn,  to  mn.
4557:cursive.  (L.)  Low  L  curjivus,  fluw- ing;  said  of  handwriting  —L.  r«r/-M/.  p(L of  cumrt,  to  run.
```


## [2026-09-05T21:00:51.408Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"gurr\" LAT.txt LEW_1910.txt KLN_1966.txt | head; echo \"== LAT grus entry\"; grep -n \"^grus\\|grus, gruis\\|gruis\" LAT.txt | head"
}
```


### [2026-09-05T21:00:51.486Z] TOOL RESULT

```
LEW_1910.txt:11560:gemeze I 148 gerren I 651 geslaht I 700 getwas I 102, 386, 480 gewande II 763 geweide II 802 gischen I 648 glast I 604 gla(t)z I 608 glesten I 604 glimen I 750 glitze I 603 glosten I 604 glucken I 606 glusten I 604 gran(e) I 414 grat, grete I 413 gra3z_ ,,SchoBling vom Nadelholz*‘ I 414, 616 gréllen I 651 grit, griten I 615 griul, griuwel IT 448 gruft I 297 grillen I 651 grunzen I 624 gruose I 616 gugel, gugerel I 298 gumpen I 499 gurren I 651 habernezzele I 158 hader, hadel I 200 hal I 142 ‘ hele I 196 handec I 252 har I 184 hatele I 183 hebamme I 55 heben I 159 hehse I 283 heie I 129 here, herewer I 169 herwén I 169 heswe I 156 hiezuo I 192 hilfa I 1 hilwe I 140 himelveste I 505 hiuweln, hiulen I 184
LAT.txt:22684:ut catillones catillorum ligurritores)-, puis "corbeille a serrer l'ar-
LAT.txt:34049:obscene come Xei)(U), (cf. cunnilingus, nencli lingi a)', ligurrius :
LAT.txt:34050:gulSsus, catillo, Xixvoc (Gloss.); ligurritor,-tio; abligurrio.
LAT.txt:34069:fornation expressive ligurrio.
LAT.txt:34599:cf. lingo, ligurrius, etc.
LAT.txt:66351:(Esch., Eur •), ope iteXcxvt}C3 uagurriS,—is "per otium uago" (d«).
KLN_1966.txt:16048:gerah,  n.,  i/20th  of  a  shekel  ( Hebrew  antiq.)  — Heb.  gerdh,  ‘bean;  the  i/2oth  part  of  the  shekel’, rel.  to  Akkad,  giru,  ‘1/20  of  a  shekel’,  and  to Heb.  gargar,  Aram.  garglrd,  ‘berry’,  Arab,  jar- jar,  ‘bean’,  Akkad,  gurgurru,  gingirru,  name  of a  plant.  Cp.  Gigartina.
KLN_1966.txt:16885:Derivative:  gurgle,  n.,  a  gurgling  sound, gurnard,  n.,  a  small  marine  fish  of  the  family Triglidae.  —  OF.  gornard,  gornart,  formed  with metathesis  fr.  OF.  gronir,  grognir,  fr.  L.  grun- nire,  ‘to  grunt’.  See  grunt  and  -ard.  The  fish  is so  called  because  it  emits  a  grunting  sound when  drawn  out  of  the  water, gurnet,  n.  —  A  var.  of  gurnard, gurry,  n„  a  little  fort  {India).  —  Hind,  garhi,
== LAT grus entry
27049:grds, -ls f. (aasc. dans Hor.S.3,8,87; noa. gruis dans Phbdre 1,
27063:grussus: saetosus, pilosus, hirsutus (Gl.). V. M.L.3881.
```


## [2026-09-05T21:00:54.251Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '27025,27062p' LAT.txt"
}
```


### [2026-09-05T21:00:54.320Z] TOOL RESULT

```
rabiare, glocis et glocito, etc. - Peut-etre faut-il rattacher a
grundiS, 1 'adj. grundulis ( 1 . grund i { is?), attest^ dans Non.114,39,
Grundules Lares dicuntur Romae constituti ob honorem porcae quae tri¬
ginta pepererat. Les formes en -nn- sont sans doute dialectales, cf.
Ernout, £I 4 m. dial., s.u. Cf. toutefois gannis, hinnis. La forme recente
grunium peut etre, comme le suggfere M.Niederaann, un postverbal de
*grunire, issu r^guliereaent de grunnire d' apros la loi de mamilla',
grunnire aurait 4±4 retabli d'apros grunnio, grunniunt.
L'un des aots en gr- indiquant des*bruits. Cf .garrio, grdculus
et grus', gr. ypu, ypu^co, etc.
*-gru 5 , -is, -ere. Attest^ seulement dans la glose sans doutegrQ»
- 506 -
corruapue gruit, invenit CGL V 439,15; 503,59, et dans lea coaposes:
i° congruS,-is: «e rencontrer, etre d'accord (de a£ae sens que
conuenire et coaae celui-ci peut s'eBpldyer peraonnelleaent et ia-
personnelleaent). Atteste depnis Plaute; classique, usuel. Se IA:
congruus (arck. et postclaas. ), congruentia (epoq.iap ,), congruenter
(Cic.), congruitis (Prisc. pour traduire <?up.f 3 cqux), et les contraires
excongruus (Syaa.), incongruus,-gruBns,-gruentia,-gruitis attestes
A 1 'epoque iap^riale.
3° ingruS,-is: se jeter sur, toaber sur. Terae de la langue aili-
taire (dejA dans Pl., Anp.336); ne se trouve ni dans Cic. ni dans
C 4 s. Sans derives.
Pas d'etyaologie sure.
grds, -ls f. (aasc. dans Hor.S.3,8,87; noa. gruis dans Phbdre 1,
8,7): grue. - Depuis Lucilius. Panroaan, M.L.3896 (et *gruilla 3883).
De IA: gruS,-is: crier (de la grue), cL P.F.8C,i3 gruere dicuntur grues,
ut sues grunnire.
Non originelleaent expressif qui a pris des foraes diverses dans
les differentes langues. La fomation en -u- du latin se retrouve,
avec un autre vocalisme, dans lit .girvi et dans v.russe Seravi (serbe
SerBv), II y a une foraation en -n-, avec des vocalisaes divers, dans
gall. garan (gaul. -lat. tri-garanos "aux trois grues"), v.angi. cran,
gr. Y®P av °C> ara. krunk \gen. kfnkan) [de *gSr- ou *g r-]. V.h.a.
chranuh , v.angi, cranoc , ont a la fois -n- et -u-. La racine seable
etre dissyllabique du type *gere~. Le g du groupe expressif *ger-
(cf. les aots a gr- initial indiquant des bruits) n 1 est pas g W ' gr*
yepavos, celt. *garano~.
```


## [2026-09-05T21:01:11.841Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && grep -n \"gurrio\\|gurrīre\\|gurrire\" WLD_Bd1_1930_dli_70244_djvu.txt | head; echo \"== ger heiser\"; grep -n -i \"heiser schreien\\|wach werden\\|wachen, munter\" WLD_Bd1_1930_dli_70244_djvu.txt | head"
}
```


### [2026-09-05T21:01:11.928Z] TOOL RESULT

```
== ger heiser
6106:293 (mit s-Yorschlag lit. s'dpti „schwach werden“, s'rfpnas „schwach“ ; 
19415:„feucht, milde, welk“, (ir)welhen ,,weich, schwach werden", mud. welen 
26293:Hiihnern“, mnd. krochcn ..grunzen; heiser schreien (vom Raben)”. 
34300:Lit. geibus „plump, ungeschickt 44 , geibstii, geibti „schwach werden, vor 
37223:2. ger- in Schallworten, bes. fur „heiser schreien" 
55055:drunyti „morsch, schwach werden, abschwachen.“
```


## [2026-09-05T21:01:16.403Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && sed -n '37223,37250p' WLD_Bd1_1930_dli_70244_djvu.txt; echo \"...\"; grep -n \"jarate\\|járate\\|jagarti\\|jäg\\|vīγrāδ\\|vigras\\|Kaus. a-gär\\|4\\. ger-\" WLD_Bd1_1930_dli_70244_djvu.txt | head -15"
}
```


### [2026-09-05T21:01:16.465Z] TOOL RESULT

```
2. ger- in Schallworten, bes. fur „heiser schreien" 

Ai. jdrafe ,rauscht, tont, knistert. ruft“, jara ..das Rauschen 1 - (oder zu 
*gfir- oder *g*< j r(a- x ) ; vielleicht gargara-li ,.ein Musikinstrument ' (dock 
siehe auch *gal -1; 

anord. kecra , kcerda ,,eine Sache vorbringen, Klage fiihren, anklagen" 
(von einem dehnstufigen /-St. *gcri- abgeleitet; dem Vergleich mit gr. 
yfjgvg. dor. yugvs, Wz. gar- ist der Yok. im Wege; gegen Fick 111 4 39 = 
Falk-Torp u. kjeere), mit Konsonantenseharfung (oder idg. -rs-??) ahd. 



kerran (st. Y.) „schreien, grunzen, wiehern, rauschen, knarren“, mnd. kerren , 
barren „knarren“, ags. ceorran „knarren“ ( ceorung „Klage, Murren"), norw. 
karra ,,girren, gackern“ (nicht zu gtir-), anord. hurra „laut reden, MiBver- 
gnfigen auBern“, kurr „Gemurmel, Gerficht", hum „knurren“, kura „Klage“ ; 

lit. gurti „gellen“; alb. (G, Meyer Alb. "Wb. 307) nguron vom Heulen 
des Windes; vielleicht (s. unter guer(a x )-) lit. girdas ,_,Gerficht !e u. dgl., arm. 
kardam als c//(-Erweiteruiig. 

Hierher der Kranichname, teils mit Formans -en-, teils mit -cm-, -u- 
gebildet (vgl. z. B. Curtius 5 175f., und zur Stammbildung bes. Solmsen 
Beitr. I 119f.): 

gr. yegrjV . . . yeoavos Hes. -’mavog „Kranich“ und „Krahn (zum Lasten- 
heben)“, gall, tarvos trigaranos (Inschrift fiber einem Stier mit drei Yogeln 
...
37665:Beiheft 162) vigras „erwacbe";
```


## [2026-09-05T21:01:21.708Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && sed -n '37640,37680p' WLD_Bd1_1930_dli_70244_djvu.txt"
}
```


### [2026-09-05T21:01:21.766Z] TOOL RESULT

```
Scblachtvieh" („mit herausgebogener Bauchhohle"? Falk-Torp u. krop; eher 
mischt sich die Sippe von dt. lcerben , mnd. krobben „kratzen“ ein, der vielleicht 
besser auch anord. krof n. „aufgeschnittener Korper geschlacbteter Tiere, 
Korper", kryfia „ausweiden“ zugeteilt werden, die sonst fur Kropf idg. -p- 
nahelegten; unklar ist die Etym. von schwed. kriiva „Kropf, Yormagen der 
Yogel"; s. Falk-Torp aaO. m. Lit. ; ein *krufta- „Ausbiegung, Hiigel" in mndl. 
krochtfe), kroft{e) „hervorragender Hiigel, hoher Sandgrund, Acker in den 
Diinen", ags. croft „kleines Feld" (Fick IIP 55). Vereinzelte germ. Formen mit 
Anl. rkr- s. bei Falk-Torp u. krop (kaum ursprgl. von der gibed. \Vz. \s\qer-). 

s-Erweiterung greu-s- : mbd. mnd. kriis „kraus, lockig"; mnd. Icruse 
„Gekrose, Bauchfett" (,,*das Krause"), mit germ, -au- nd. kros „Eingeweide 
von Gansen", mbd. ( ge)krtxse , nbd. Gekrose; nd. kriise ( *krusi -) „Runzel, Falte, 
Furche, Locke", holl. kreus „Falz in FaBdauben"; (ags. creas „zierlicb“?) ; 
ahd. mhd. Irol (-/?-) „kraus“ ( *kruzld -), mbd. krolQe ), kriille „Locke“, norw. 
krull ds.; norw. mdartl. kruslen , krusken „hinfallig“, nd. krusch „crispus“, 
mhd. krusp „kraus“, nhd. obd. kraust „kraus“ (Persson Beitr. 317). 

4-. ger- g(e)rei- „wachen, wecken". 

Ai. jurat? „erwacht“, jd-gur-ti „wacht“, pf. ja-gtlra , ptc. ja-gr-vcnhs- 
„nmnter, eifrig", jdgrvi- „aufmerksam, wach, munter", av. jaydrnyantjm 
„den wachenden", pf. jagdra, ppa. jagaurvah-, jigdurvah- „wach, wachsam", 
kaus. n-garayciti „weckt", mit /V«-inchoativ fra-yrisomnd „erwachend“, kaus. 
/ m-yrn-yrayeili, fra-yra-rayeiti ,,erweckt", mpers. (Bartholomae IF. 19, 
Beiheft 162) vigras „erwacbe"; 



ger-, gere- 


599 


gr. eyecgco „wecke“ (e- ist nach Brugmann II 2 3, 38 das Adv. *r, vgl. 0 
oder o in av. d-garayeiti ), aor. k'ygezo, eygsadat, pf. i-ygrj-yoga (fur e-yt]- 
yoga — vgl. ai. ja-gara — mit dem g von eygeo&ai Thurneysen IF. 19, 
176; med. i-yrj-yeg-juar, vom pf. gin gen auB eygrjyogzt „im Wachen", eygt)- 
yogaig), eyggcoa) „wache" [*eygyaMa> nach Meillet, s. Boisacq 212);
```


## [2026-09-05T21:01:50.851Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== HRN\"; grep -n -i \"b.dar\\|vigrat\\|wachen'\\|'wach\\|erwachen\" HRN.txt | head -15; echo \"== HUB\"; grep -n -i \"b.dar\\|vigra\\|wach\" HUB.txt | head -10"
}
```


### [2026-09-05T21:01:50.915Z] TOOL RESULT

```
== HRN
1885:173. hallden 'wachsen, zunehmen* (Sahn. I, S. 3 Vers 49),
1886:bäliä 'Wachstum*-'); vergl. guvöllden (No. 939).
1894:aw. [/'vard', vareöayanuha 'wachse'; ai. l/'t?ardA-,
1917:Nach FJ soll auch bälüden 'wachsen' bedeuten, wofür als Beweis
5475:614. rasten 'wachsen, Praes. röy-em, röylden, röyäniden,
5477:aw. |/>c/orf-, raoöahe 'wachsen'; phlv. rustan (bezw.
5719:zez\avul 'erzeugen*, s'opmZ 'gebären'; oss. -eäwclr// 'wachsou*,
9348:1078. vevd/kj 'Wachtel', rerdej, verflj, vertek.
9351:kurd. verdl, //arnfrr?^ 'Wachtel' (H.-Sch.); af/. vvaraz\
11153:209. va^sltiifi 'wachsen, anwachsen, zunehmen, häuttg;
11159:aw. \/^va/S' 'wachsen*; ai. [/"vaks-^ äüksat; got.
11160:vahsjmi 'wachsen*.
== HUB
320:69. Vor dieser Nummer konnte arts *Wachholder mit
322:mit denen Geiger bal. apurs 'Wachholder* zusammen-
468:*abidara- zurtick. Daher bleibt arm. ddar 'arredo, for-
720:nur vadar (PPGl. 2 und 232), nicht badar, das eine
721:Unform ist. Ap. abddaris gehort keinesfalls hierher
910:(Wrzl, bherai, schwach bhrt) entstanden ist. Das
1031:(also — *im Walde wachsend). Mir nicht wahrschein-
1199:274. Zu pas *Wache, Nachtwache' vgl. Nr. 341: pahra^
1262:dorrten das Fleisch der Wachteln an der Luff) und
1629:Wurzel war d^rah^ schwach trs, inchoat. trs,
```


## [2026-09-05T21:02:13.049Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"to roar\\|yurr\\|gurridan\\|to growl\" CHEUNG.txt | head -12"
}
```


### [2026-09-05T21:02:13.096Z] TOOL RESULT

```
2808:*IE COGNATES: Lat. fremö ‘I make a thud, mumble, moan’, MWelsh bref- ‘to roar’, 
7990:*SANSKRIT: ? garj ‘to roar’ (Ep.+) = EWAia III: 154 
8726:*grait/graiO ? ‘to roar, scold’ 
8727:*CHORESMIAN: ? Trd- ‘to bray’ || (+ *upa-) b’Trd- ‘to roar’ => Samadi: 80, 18 
8750:*KHOTANESE: LKh. огай- ‘to growl’ {hapax} => SGS: 31 
8753:(*ia-pres. ?) ‘to roar’ || (+ *ham-) BSogd. ’nyr’m, CSogd. ’yr’m ‘to slander’ 
8766:*NEIR: Pash. yar-ég/yar-ed- ‘to roar, thunder’, ? Wa. yar-/yard ‘to bark, growl’ (< 
8773:«PIE *g"rem- ‘to roar; to be angry’ > LIV: 204 | Pok.: 458 f. 
13219:raüda ‘lament’, ON rauta ‘to roar’, OE réotan ‘to complain, weep’ 
13233:*CHORESMIAN: rw- ‘to growl’ => Samadi: 173 
13240:*SANSKRIT: rav ‘to roar’ (RV+) > EWAia II: 439 
13245:«PIE *НзгеиН- ‘to roar’ = LIV: 306 | Pok.: 867
```


## [2026-09-05T21:02:15.341Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '8740,8790p' CHEUNG.txt"
}
```


### [2026-09-05T21:02:15.383Z] TOOL RESULT

```
«PIE? > LIV: – | Pok.: 384 


* gram “to thunder, roar; to anger’ 


*AVESTAN: YAv. gram- ‘to anger, ergrimmen’ = Liste: 21 

Partic.: pres. YAv. gramant- (Y 9.28), perf. pass. YAv. granta- (Yt 10.18 f., Yt 10.23, Yt 10.39 ff., etc.) 
*KHOTANESE: LKh. огай- ‘to growl’ {hapax} => SGS: 31 

*SOGDIAN: SSogd. ’yr’n-, BSogd. yr’ns (inch./intr.) ‘to get angry’, CSogd. угуп 
(*ia-pres. ?) ‘to roar’ || (+ *ham-) BSogd. ’nyr’m, CSogd. ’yr’m ‘to slander’ 

Pres.: IND. 35р. dur. CSogd. yryntq; Impf.: IND. 35р. BSogd. yr’ns; Pret.: IND. 3pl. SSogd. ’yr’nt’nt, 
Partic.: pres. BSogd. yr’nsn’y; Pass.: pret. SUBJ. 3sg. MSogd. yr’ndyy ’kt’t ‘should have been irritated’ 
(ВВВ: 37) || (+ *ham-) Pres.: IND. 3sg. "nyr'mt; Impf.: IND. 3pl. CSogd. myr’mnt, Partic.: pres. BSogd. 
*nyr’mn’y, MSogd. ’ngr’mnyy (Sogdica: 52) 

*CHORESMIAN: m/ym- ‘to coo, sing (of birds)’ = Samadi: 77 f. 

*NWIR: NP gurunbidan, Gz. qurumb-/qurumba ‘to thunder, roar’, NP garmidan ‘to 
thunder, roar, fly in a passion’, Bal. grandit/grand- (denomin.) ‘to thunder’, Bal. 
grand ‘thunder’ (Sims-Williams apud Shahbakhsh) 

*NEIR: Pash. yar-ég/yar-ed- ‘to roar, thunder’, ? Wa. yar-/yard ‘to bark, growl’ (< 
Pash. ?), Ishk. yorond-/yorost ‘to scold’, ? Oss. I. qyrnyn/qyrnd, D. girnun/girnd ‘to 
sing (along) in a diphonic song; to howl [of dogs]’ 

© The variant *gran- with final -n, attested in several ЕП. languages, is no doubt 
abstracted from the past participle, with final m > n / — T. Consequently, the 
postulation of a separate (IE) root *gr-en- (cf. SGS: 31) is therefore unnecessary. 
«PIE *g"rem- ‘to roar; to be angry’ > LIV: 204 | Pok.: 458 f. 

*IE COGNATES: Goth. gramjan, OHG gremmen ‘to become angry’, OE gremman ‘to 
scorn’, etc., NHG grimm, Engl. grim, Lith. gramu, etc. 

*REFERENCES: Paxalina 1959: 203; Sims-Williams 1976: 18, 60; Abaev, Slovar’ П: 333; WIM II/1: 81; 
Steblin-Kamenskij 1999: 185; NEVP: 32; Shahbakhsh: s.v. grand-; Korn 2005: 317, fn. 200 


*øraðH ‘to tie (a knot)’ 

*MIDDLE PERSIAN: BMP glyh /grih/ ‘knot’ 

*PARTHIAN: gryh ‘knot? = DMMPP: 164a 

*KHOTANESE: OKh. grantha-, gramtha-, LKh. gratha- ‘knot’ || (+ *ham-) OKh. 
hamgramtha-, LKh. hamgratha- ‘attachment’
```


## [2026-09-05T21:02:35.248Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('POK_02.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('leaves',len(t))\nfor n in (45,46,47,48):\n    s=t[n]\n    print('==== leaf',n,'(printed ~',n+344,')')\n    print(s[:700].replace('\\n',' | '))\nEOF"
}
```


### [2026-09-05T21:02:36.914Z] TOOL RESULT

```
leaves 434
==== leaf 45 (printed ~ 389 )
(über  ahd.  krüsel  , Schmelztiegel'  usw.  s.  Falk-Torp  unter  krus  m.  Nachtrag) zur  Erwägung  steht.  Über   nhd.  Kriechbaum  s.  Kluge  ^^  unter  Krieche. | 2.  Labialerweiterungen: | greu-p-:  gr.  ygvTtög  ,gekrümmt,  mit  einer  Adlernase',  ygVTtöa)  ,krümme', ygvyjj  ygVjtög  m.  , Greif  (nach  dem  krummen  Schnabel  und  den  krummen Fängen'),  nasaliert  ygvfxrtdvsLv'  ygvTtova&aL,  0vyy.d^7tT6Lv  Hes.,  wozu  wohl zunächst  ags.  usw.  krumh  , krumm'  (s.  oben  S.  387). | greu-b-:  hierher  vielleicht  schott.-gäl.  groban  ,top  or  point  of  a  hill' (*grubb-) ; | anord.  krjüpa,  ags.  creopan,  mnd.  krüpen  , kriechen'  (,*sich  krümmen wie  ein  Wurm'),  ags.  cryppan 
==== leaf 46 (printed ~ 390 )
rayeitl und  oben  S.  280 ;  anders  Schwyzer  Gr.  Gr.  1  648  ^)j  Aor.  eygsTo,  syQea^ai^ Perf.  i-ygrj-yoQa  (für  s-yrj-yoga  —  vgl.  ai.  jä-gdra  —  mit  dem  g  von " iygiad-ai]  Med.  (spät)  i-yrj-ysQ-fxac ]  vom  Perf.  gingen  aus  iyorjyoQxl  ,im Wachen',  iyQrjyoQaig) ;  iyQrjaao)  ^wache'  zu  ^ygr^-r-  (vgl.  av.  fra-^rätö  ,beim Erwachen');  kaum  aus  *iyQr]omcx)  (Schwyzer  Gr.  Gr.  I  708 2); | alb.    tosk.    ngre    (woraus   ngre),    geg.    ngrei   ,hebe   auf,    errichte,  wecke, spanne  ein  Gewehr'  (*n-grd-n-iö),  Partiz.  n-grite  {^-grl-t-)\ | vermutlich  anord.   karskr,   kerskr  , frisch,   lebhaft',   mnd.  karsch    , frisch, munter',  alem.  chärzsch.
==== leaf 47 (printed ~ 391 )
fe',  yvjgaXiog  (bei  Hes.  auch  yegaleog) ,alt';  att.  ygavg,  Gen.  yga{*f)6g  (hom.  Dat.  ygrj'C)  ,alte  Frau'  (hom.  ygr/vg wohl  spätere  Umschrift  eines  richtigen  *}grj{ß)Lg  nach  dem  gewöhnlichen ygavg) ;  vielleicht  in  Beziehung  zu  av.  zaurvan-  m.  , Greisenalter',  etwa ursprüngl.  Nom.  ^ger-us  :  Gen.  *g^rd-u-6s,  woraus  ygafog ;  s.  Schwyzer  Gr. Gr.  1,  574;  redupl.  ysgyegiixog  ,von  selbst  abfallende  oder  reife  Feige  oder Olive'  (s.  oben); | anord.  karl  ,Mann,  alter  Mann,  Ehemann,  freier  Mann'  =  ahd.  karal ds.,  mit  Ablaut  ags.  ceorl  , freier  Mann  der  niedrigsten  Klasse,  Ehemann^, engl,  churl  , Bauer,  Tölpel',  mnd.  kerle  , 
==== leaf 48 (printed ~ 392 )
hen',  ursprüngl.  , kriechen/ indem  man  sich  festhakt'),  wozu  anord.  krabbi  m.,  ags.  crabba,  mnd.  krabbe .  ,Krabbe'  und  ahd.  (krebiz),  *krabita-,  krebaz(o),  asächs.  krebit,  nhd.  Krebs.  — ^ Ganz  fraglich  gr.  ygö^q)ig  ,Sau'  (besser  ,die  Grunzende'?)  als  Nasalform. | 3.  Daneben  ^gribh-  (mit  expressivem  i?): Gr.  yqicpaad'ai '   ygacpsLv.  Aa%(ßveg.   oX    ös   ^vecv   'Aal   äiivaaeiv  Hes.  (vgl, | von  sker- :  gr.  oy.aQLq)aof.iai,  lat.  scribo),  äyQicpri,  dygelcfva  ,Harke,  Rechen* {ä-  aus  *7}-  ,iv',  ,einritzen'?); | holl.  kribbelen  ,murren',  kribelen  ,jucken',  mhd.  md.  kribeln  , kitzeln  (von; der  Sinnenlustj',  nhd.  kribbeln^  und  mit  ge
```


## [2026-09-05T21:03:12.726Z] TOOL CALL #72: Bash

```json
{
 "command": "sed -n '1,80p' tools/verify_check.py"
}
```


### [2026-09-05T21:03:12.760Z] TOOL RESULT

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


## [2026-09-05T21:03:14.889Z] TOOL CALL #73: Bash

```json
{
 "command": "sed -n '80,140p' tools/verify_check.py"
}
```


### [2026-09-05T21:03:14.932Z] TOOL RESULT

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


## [2026-09-05T21:04:32.023Z] TOOL CALL #74: Bash

```json
{
 "command": "grep -ho '\"translit\": \"[^\"]*ous\"' data/extracted/batch/page-*.json | sort | uniq -c | sort -rn | head -30"
}
```


### [2026-09-05T21:04:32.113Z] TOOL RESULT

```
      2 "translit": "oktô-pous"
      2 "translit": "medi-terrâneous"
      2 "translit": "gregorious"
      1 "translit": "zugon, zygos, sextarious"
      1 "translit": "zeal, jealous"
      1 "translit": "voracious, carnivorous"
      1 "translit": "viscous"
      1 "translit": "synonym, antonym, anonymous"
      1 "translit": "slavous"
      1 "translit": "serious"
      1 "translit": "number, numerous"
      1 "translit": "noxious, obnoxious"
      1 "translit": "notorious"
      1 "translit": "nerve, nervous"
      1 "translit": "mix, miscellaneous"
      1 "translit": "geranous"
      1 "translit": "enormous"
      1 "translit": "carnival, carnivorous"
      1 "translit": "bous"
      1 "translit": "amphibious"
```


## [2026-09-05T21:04:41.557Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"Gregorian\\|Gregorius\\|gregorios\\|grégoros\" KLN_1966.txt SKT.txt WEB_vol1.txt FSD_vol2.txt 2>/dev/null | head -8"
}
```


### [2026-09-05T21:04:41.620Z] TOOL RESULT

```
KLN_1966.txt:16663:grego,  n.,  a  short  cloak.  —  Port.  Grego  or  Sp. Griego,  ‘Greek’,  fr.  L.  Graecus.  See  Greek. Gregorian,  adj.  —  Lit.  ‘pertaining  to  Gregory’, fr.  Late  L.  Gregorianus,  fr.  Gregorius.  See  next word  and  -an.
KLN_1966.txt:16664:Gregory,  masc.  PN.  —  Late  L.  Gregorius,  fr.  Gk. rprjydpto^,  fr.  ypfjyopo?,  ‘watchful’,  which  is rel.  to  typfjyopa,  second  perfect  of  £ye(petv,  ‘to awaken’,  fr.  I.-E.  base  *ger-,  ‘to  be  awake’, whence  also  OI.  jagarti,  ‘he  is  awake’,  Avestic a-garayeiti,  ‘wakes  up,  arouses’.
WEB_vol1.txt:6454:Ambrosian chant; a mode of singi chanting introduced by St. Ambrose Teas superseded by the Gregorian chant. cy
WEB_vol1.txt:26402:Gregorian calendar; see under Gregorian.
WEB_vol1.txt:84447:Gregorian calendar; a corrected form of the Julian calendar, introduced by Pope Gregory XIII in 1582 and now used in most countries of the world: it provides for an ordinary year of 365 days and a leap year of 366 days every fourth even year, exclusive of century years, which are leap years only if exactly divisible by 400.
WEB_vol1.txt:84448:Gregorian chant; a mode of singing or chant- ing introduced by Pope Gregory I, less monotonous than the Ambrosian, which pre- ceded it; plain song, or plain chant.
WEB_vol1.txt:84449:Gregorian telescope; the first and most com- mon form of the reflecting telescope, invented by James Gregory (1638-1675), professor of mathematics in the university of St. Andrews.
WEB_vol1.txt:84450:Gregorian year; a year according to the Gregorian calendar. reil/lade, n. [etym. unknown.] coarse iron ore used in a Catalan forge.
```


## [2026-09-05T21:04:56.679Z] TOOL CALL #76: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg175.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/175.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/ | tail -3"
}
```


### [2026-09-05T21:04:56.764Z] TOOL RESULT

```
-rw-rw-r--  1 sfmqrb sfmqrb  78178 Sep  5 10:14 95.png
-rw-rw-r--  1 sfmqrb sfmqrb  72929 Sep  5 10:19 96.png
-rw-rw-r--  1 sfmqrb sfmqrb  65608 Sep  5 10:43 99.png
```


## [2026-09-05T21:12:12.871Z] TOOL CALL #77: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build175.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW_BIDAR = \"https://en.wiktionary.org/wiki/%D8%A8%DB%8C%D8%AF%D8%A7%D8%B1\"\nW_HGER  = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%81ger-\"\nW_GRUS  = \"https://en.wiktionary.org/wiki/grus#Latin\"\nW_GHOR  = \"https://en.wiktionary.org/wiki/%D8%BA%D8%B1%DB%8C%D8%AF%D9%86\"\nW_ZAR   = \"https://en.wiktionary.org/wiki/%D8%B2%D8%A7%D8%B1#Persian\"\nW_JAR   = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/j%C4%81r%C3%A1yati\"\nE_GER   = \"https://www.etymonline.com/word/Gregorian\"\nE_CRANE = \"https://www.etymonline.com/word/crane\"\nE_GERAN = \"https://www.etymonline.com/word/geranium\"\n\ndoc = {\n \"pdf_page\": 175,\n \"book_page\": 145,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-05\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"Ger 3\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *h₁ger- 'to wake up, be awake' (Pokorny '4. ger-, g(e)rēi- wachen, wecken', IEW pp. 389-390; Walde-Pokorny I 598 f.; LIV² 245)\",\n   \"note\": \"The root box is right on all three counts: a real Indo-European root, correctly labelled Indo-European, correctly glossed 'to awaken'. Pokorny's lemma is '4. ger-, g(e)rēi- „wachen, wecken“' and its parent article is Walde-Pokorny I 598 f.; the modern reconstruction adds the initial laryngeal, *h₁ger- (LIV² 245, Cheung's Proto-Iranian *Hgar-), which is why Beekes (Comp. IE Ling. p.126) discusses this very root under depalatalisation. Two small caveats. (1) The page: Pokorny's entry ends on p.390 — the OCR leaf for p.390 carries its Greek section (ἐγείρω, ἐγρήγορα, Alb. ngre, ON karskr) — while p.391 already belongs to the homonymous 'ger-, gerə-, grē- to rub; to be old' root; so POK:391 is one page late. (2) The numbering 'Ger 3' is Nourai's own; Pokorny numbers this root ger-4 and numbers the 'cry hoarsely' root of the next chart ger-2 — i.e. Nourai's 3/4 are the reverse of Pokorny's 4/2. Both Indo-European branches Nourai draws (the Iranian one ending in بیدار and the Greek-Latin one ending in Gregory) are standard: Klein s.v. Gregory derives the name from Gk. γρήγορος 'watchful' and cites Avestan ā-garayeiti in the same breath, exactly as the chart does. Note also that the odd-looking Greek/Latin form 'gregorious' (and 'geranous' in the next chart) is not a misprint but Nourai's fixed habit of writing classical -us/-os as -ous (cf. 'sextarious' for sextārius, 'medi-terrâneous' for mediterrāneus elsewhere in the book).\",\n   \"note_fa\": \"ریشهٔ هندواروپایی آغازین *h₁ger- «بیدار بودن، بیدار شدن» ریشه‌ای است پذیرفته‌شده: پوکورنی آن را با شمارهٔ ger-4 و معنای «wachen, wecken» در صفحهٔ ۳۹۰ آورده و والده‌ـ‌پوکورنی (جلد ۱، ص ۵۹۸ و بعد) همان را با صورت‌های اوستایی ā-garayeiti و فارسی میانهٔ vigrās گزارش کرده است؛ در بازسازی امروزی حنجره‌ای آغازین *h₁ نیز افزوده شده (LIV² ۲۴۵؛ چونگ: ایرانی آغازین *Hgar-). دو نکتهٔ کوچک: نخست آنکه ارجاع نورایی به صفحهٔ ۳۹۱ یک صفحه دیرتر است، چون صفحهٔ ۳۹۱ به ریشهٔ هم‌آوای «ساییدن؛ پیر شدن» اختصاص دارد؛ دوم آنکه شمارهٔ «Ger 3» از خودِ نورایی است و با شماره‌گذاری پوکورنی نمی‌خواند. هر دو شاخهٔ نمودار — شاخهٔ ایرانی که به «بیدار» می‌رسد و شاخهٔ یونانی‑لاتینی که به Gregory می‌رسد — درست است. صورت‌نویسی «gregorious» نیز غلط چاپی نیست، بلکه شیوهٔ همیشگی نورایی در نوشتن پایانهٔ ‑us/‑os کلاسیک به‌صورت ‑ous است. ادعای نورایی دربارهٔ خودِ ریشه درست است.\",\n   \"sources\": [W_HGER, E_GER],\n   \"ref_check\": [\n    {\"ref\": \"POK:391\", \"status\": \"partial\",\n     \"note\": \"Pokorny's root is real and is exactly Nourai's, but it stands one page earlier. POK_full.txt (starling dump) has 'Root / lemma: ger-4, grei- / Meaning: to grow; to awake ... References: WP. I 598 f., WH. I 429 f. / Page(s): 390'; the printed scan confirms it — POK_02.txt leaf 46 (= p.390) carries 'Perf. ἐ-γρή-γορα ... ἐγρήγορσις ... alb. tosk. ngre ... anord. karskr, kerskr „frisch, lebhaft“', i.e. the end of this entry, while leaf 47 (= p.391) is already the homonym 'ger-, gerə-, grē- to rub; to be old' (γραῦς, anord. karl, ags. ceorl).\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"IEW pp.389-390, '4. ger-, grēi-'\", \"stance\": \"supports\",\n     \"note\": \"'Meaning: to grow; to awake. Material: Old Indic jarate „awakened“, ja-gar-ti „wakes“ ... av. jaγārayantəm „the watching one“ ... Kaus. ā-garayeiti „arouses, awakens“ ... Middle Persian vīγrās „awake“ ... gr. ἐγείρω „awake“' (POK_full.txt lines 31670-31700).\"},\n    {\"src\": \"WLD\", \"where\": \"Bd. I 598 f.\", \"stance\": \"supports\",\n     \"note\": \"the parent article: '4. ger- g(e)rei- „wachen, wecken“. Ai. jarate „erwacht“, jā-gar-ti „wacht“ ... av. jaγārayantəm „den wachenden“ ... kaus. ā-garayeiti „weckt“ ... mpers. (Bartholomae IF. 19, Beiheft 162) vigrās „erwache“; gr. ἐγείρω „wecke“' (WLD_Bd1_1930_dli_70244_djvu.txt lines 37659-37680) — it contains all three of Nourai's Iranian/Greek boxes.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.vv. gerə-¹, gerə-²\", \"stance\": \"silent\",\n     \"note\": \"the 1985 Watkins appendix has no root meaning 'to awake' at all: between 'ger-²' (curving) and 'gerbh-' (to scratch) stand only 'gerə-¹. To grow old. [Pok. ger- 390]' and 'gerə-². To cry hoarsely [Pok. 2. ger- 383]'. No English word of the dictionary continues *h₁ger- (Gregory is a proper name), so the root is simply absent.\"},\n    {\"src\": \"CHEUNG\", \"where\": \"p.172 f., '*Hgar to be awake'\", \"stance\": \"supports\",\n     \"note\": \"'*Hgar „to be awake“ ... «PIE *H₁ger- „to wake up“ ⇒ LIV: 245 | Pok.: 390' with YAv. γar-, MP wigrās-, NP bidar in the same article.\"},\n    {\"src\": \"Wiktionary\", \"where\": \"Reconstruction:Proto-Indo-European/h₁ger-\", \"stance\": \"supports\",\n     \"note\": \"'*h₁ger-: to wake up, awaken', descendants Ancient Greek ἐγείρω / ἐγρήγορα, Vedic जागार (jāgā́ra), Younger Avestan 𐬘𐬀𐬖𐬁𐬭𐬀 (jaγāra 'is awake'), Proto-Iranian *Hgāráyati.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Avestan\", \"words\": \"gar 1; â-gara-yeiti\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Avestan has a root gar- (Younger Avestan spelling γar-, because Iranian *g- appears as γ- in these forms) 'to be awake, to keep watch': perfect jaγāra 'he is awake' (Nērangestān 19), perfect participle jaγāuruuah-/jiγāuruuah- 'awake, watchful' (Yt 10.7, of Miθra 'who watches over the whole material world'), inchoative fra-γrisəmna- 'awakening' (H 1.13). The causative stem is gār-aya-, so ā-gārayeiti 'wakes (someone) up, rouses' — Nourai's 'â-gara-yeiti', with the preverb ā- 'hither' plus the o-grade/lengthened causative *h₁gor-éye-ti, matching Sanskrit ā-jāgarayati and Greek ἐγείρω exactly. Bartholomae quotes the first person from the Āfrīnagān: 'ā θβā uštarəm gārayemi vaŋhə̄uš manaŋhō zaoθrābyō' ('I wake thee up ... with the libations of Good Thought'). The gloss 'to wake up' for the root and 'wakes up' for the causative is right, though strictly ā-gārayeiti is transitive 'wakes (another) up'.\",\n     \"derivation_fa\": \"در اوستا ریشهٔ gar-/γar- «بیدار بودن، پاییدن» شناخته است: ماضی نقلی jaγāra «بیدار است»، صفت مفعولی jaγāuruuah- «بیدار، هشیار» (یشت ۱۰٫۷ دربارهٔ مهر) و صورت آغازی fra-γrisəmna- «در حال بیدار شدن». ستاک سببی آن gār-aya- است، پس ā-gārayeiti «بیدار می‌کند» با پیشوند ā- ساخته شده و درست همان است که نورایی «â-gara-yeiti» نوشته؛ بارتولومه (فرهنگ ایرانی باستان، ستون ۵۱۱) نمونهٔ «ā θβā uštarəm gārayemi» را از آفرینگان می‌آورد. تنها نکتهٔ ریز آنکه ā-gārayeiti گذراست، یعنی «کسی را بیدار می‌کند»، نه «بیدار می‌شود». ادعای نورایی درست است.\",\n     \"sources\": [W_HGER],\n     \"ref_check\": [\n      {\"ref\": \"POK:391\", \"status\": \"partial\",\n       \"note\": \"the material is Pokorny's, but on p.390 (see the root-level ref_check): 'av. jaγārayantəm „the watching one“, Perf. jaγāra, participle Perf. jaγāuruuah-, jiγāuruuah- „awake, watchful“, Kaus. ā-garayeiti „arouses, awakens“' (POK_full.txt line ~31674).\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BRT\", \"where\": \"AiW col. 511-512, s.v. '1gar- V. wachen'\", \"stance\": \"supports\",\n       \"note\": \"'1gar- V. „wachen“. Praes. ... (Kaus.) gāraya-, ... Perf. jaγār-, jaγar-. 1) „wachen“: ... yō jaγāra N. 19 ... 2) „wachen über —“ ... mit ā Kaus. „wecken“: ā θβā uštarəm gārayemi vaŋhə̄uš manaŋhō zaoθrābyō Any. 1' (BRT.txt lines 10190-10200); the same article quotes the New Persian paraphrase of the passage as 'bīdār gardad'.\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. I 598\", \"stance\": \"supports\",\n       \"note\": \"'av. jaγārayantəm „den wachenden“, pf. jaγāra, ppa. jaγāuruuah-, jiγāuruuah- „wach, wachsam“, kaus. ā-garayeiti „weckt“, mit fra-inchoativ fra-γrisəmnō „erwachend“'.\"},\n      {\"src\": \"CHEUNG\", \"where\": \"'*Hgar', Avestan section\", \"stance\": \"supports\",\n       \"note\": \"'*AVESTAN: YAv. γar- „to guard, watch“ || (+ *ā-) caus. „to wake up [tr.]“ || (+ *fra-) inch. „to awake“ ... Caus.: pres. IND. 1sg. YAv. ā ... gāraiiemi (Any 2), 3sg. YAv. fra.γāraiieiti (V 18.22, N 19)'.\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Pahlavi\", \"words\": \"vîgrâs; wiğrâd\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Middle Persian wigrādan / wigrās- (Book Pahlavi wglʾtn', wglʾs-; Manichaean MP wygrʾd, wygrʾs-) 'to awaken, rouse', with past participle / adjective wigrād 'awake, alert'. The two forms Nourai prints are precisely MacKenzie's present and past stems: the present in -s- continues the Iranian inchoative *wi-HgraH-sca- (whence also Parthian wygrʾs-, Sogdian wyrʾs, Chorasmian myrʾs-), and wigrād continues the participle *wi-grāta-. The preverb is *wi- 'apart, away' (PIE *wí), which in this verb has the ingressive value 'to come out of sleep'. Pokorny and Walde-Pokorny cite the form under this very root, as 'mpers. vigrās „erwache“' after Bartholomae (IF 19, Beiheft 162) — literally Nourai's 'vîgrâs'.\",\n     \"derivation_fa\": \"فارسی میانه wigrādan / wigrās- (پهلوی کتابی wglʾtn'، wglʾs-؛ مانوی wygrʾd، wygrʾs-) «بیدار کردن، برانگیختن» و صفت wigrād «بیدار». دو صورتی که نورایی آورده دقیقاً ستاک حال و ستاک گذشتهٔ همین فعل در فرهنگ مکنزی است: ستاک حالِ ‑س‌دار بازماندهٔ صورت آغازیِ ایرانی *wi-HgraH-sca- است (پارتی wygrʾs-، سغدی wyrʾs) و wigrād از صفت مفعولی *wi-grāta-. پیشوند *wi- «جدا، دور» در اینجا معنای آغازی «از خواب درآمدن» می‌دهد. پوکورنی و والده‑پوکورنی نیز همین صورت را ذیل همین ریشه با نگارش «mpers. vigrās» آورده‌اند. ادعای نورایی درست است.\",\n     \"sources\": [W_BIDAR],\n     \"ref_check\": [\n      {\"ref\": \"POK:391\", \"status\": \"partial\",\n       \"note\": \"again the content is on p.390/WP I 598, but it is verbatim Nourai's form: WLD_Bd1 line 37665 'mpers. (Bartholomae IF. 19, Beiheft 162) vigrās „erwache“'; the starling text of Pokorny has 'Middle Persian vīγrās „awake“, vīγrāsēnag „livener“'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie 1971 p.91, s.v. wigrād / wigrādan\", \"stance\": \"supports\",\n       \"note\": \"'wigrād [wglʾt' | N bīdār] awake, alert. wigrādan, wigrās- [wglʾtn', wglʾs- | M wygrʾd, wygrʾs-] awaken, rouse. ~išn(īh): awakening.' (PHD.txt line 651) — both of Nourai's forms, with the same glosses.\"},\n      {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II (Glossary), s.v. vigrās-\", \"stance\": \"supports\",\n       \"note\": \"'vigrās- [wglʾs-] pres., to rouse a p. from sleep, from the dead: apāc vigrāsēnd 101.79; ā(h) vigrāsēnd 101.5. — Av. (511) 1gar-, v. guhrāyēnītan; MPrth wygrʾs „to awake“, MPrs „to rouse from sleep“; Verbum 196; Ghilain 82, 92-93' (NYB_vol2_glossary.txt line 4137) — Nyberg himself refers the word to Bartholomae's column 511, i.e. to Nourai's Avestan box.\"},\n      {\"src\": \"CHEUNG\", \"where\": \"'*Hgar', Middle Persian/Parthian section\", \"stance\": \"supports\",\n       \"note\": \"'*MIDDLE PERSIAN: (+ *ui-) MMP wygrʾs-, BMP wglʾs- /wigrās-/ „to wake, awaken“ ... Partic.: perf. pass. MMP wygrʾd ... *PARTHIAN: (+ *ui-) wygrʾs- „to wake, awaken“'.\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"Persian\", \"words\": \"bîdâr «بیدار»\", \"verdict\": \"confirmed\",\n     \"derivation\": \"New Persian بیدار bīdār (classical bēdār) 'awake' continues Middle Persian wigrād by three regular steps: initial w- becomes b- in New Persian (as wād > bād, wistan > bistan); the intervocalic spirant -γ- of *wiγrād is lost with compensatory lengthening of the vowel, *wiγrād > *wīrād; and -r- and -d- change places, *wīrād > bīdār. Cheung states exactly this ('NP bīdār ... with metath. & loss of -γ- < *wiγrād'), and the dialect forms he lists preserve the stages — Abyāne biyār, Gaz biyār, Jowšaqān vidār. MacKenzie's entry gives bīdār as the New Persian continuation of wigrād outright, and Bartholomae already noted that the New Persian paraphrase of the Avestan passage with ā-gārayeiti renders it 'bīdār gardad'. The meaning has not shifted at all: 'awake, not asleep', with the derived sense 'alert, aware' (Moʿin: 'کسی که در خواب نباشد؛ آگاه، هوشیار').\",\n     \"derivation_fa\": \"«بیدار» (در فارسی کلاسیک bēdār) دنبالهٔ مستقیم فارسی میانهٔ wigrād است با سه دگرگونی آواییِ قاعده‌مند: و آغازین در فارسی نو به ب بدل شده (مانند wād > باد، wistan > بستن)؛ سایشیِ ـغـ در *wiγrād افتاده و واکهٔ پیش از آن کشیده شده (*wīrād)؛ و سپس قلبِ (metathesis) ر و د روی داده و *wīrād به «بیدار» رسیده است. چونگ همین را می‌گوید («با قلب و افتادن ـγ‑ از *wiγrād») و گویش‌های ابیانه‌ای biyār، گزی biyār و جوشقانی vidār مرحله‌های میانی را نگاه داشته‌اند؛ ویکی‌واژه نیز «بیدار» را با قلب از فارسی میانهٔ wygrʾd می‌گیرد. مکنزی در برابر wigrād یکسره «N bīdār» می‌نویسد و بارتولومه هم ترجمهٔ فارسی بند اوستایی را «بیدار گردد» نقل می‌کند. معنا هیچ تحولی نیافته است. ادعای نورایی درست است.\",\n     \"sources\": [W_BIDAR],\n     \"ref_check\": [\n      {\"ref\": \"MON:621\", \"status\": \"partial\",\n       \"note\": \"only the two-volume Adena abridgement of Moʿin is on disk and it has no page mapping to the six-volume edition Nourai cites; the headword is there and matches the gloss — 'بیدار: (ص.) کسی که در خواب نباشد؛ مق. خوابیده. آگاه، هوشیار، متنبه' (MON_part1.txt line 26856) — but the abridgement drops the Latin-script Pahlavi etymology of the print edition, so p.621 could not be confirmed.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"CHEUNG\", \"where\": \"'*Hgar', NWIr. section\", \"stance\": \"supports\",\n       \"note\": \"'*NWIR: Bal. gurit/gur- „to wake up with a start“ ... || (+ *ui-) NP bidar, Abyan. biyar, Gz. biyar, Jow. vi:dá:r „awake“ (with metath. & loss of -γ- < *uiγrād)'.\"},\n      {\"src\": \"PHD\", \"where\": \"MacKenzie 1971, s.v. wigrād\", \"stance\": \"supports\",\n       \"note\": \"'wigrād [wglʾt' | N bīdār] awake, alert' — MacKenzie's '| N …' column is precisely the New Persian continuant, so he equates bīdār with MP wigrād.\"},\n      {\"src\": \"Wiktionary\", \"where\": \"s.v. بیدار, Persian\", \"stance\": \"supports\",\n       \"note\": \"'Metathesis from Middle Persian (wygrʾd /wiγrād/), from Proto-Iranian *wi- + *Hgar- („to be awake“), the former from Proto-Indo-European *wí („apart“), the latter from Proto-Indo-European *h₁ger-'.\"},\n      {\"src\": \"HRN\", \"where\": \"Grundriss (searched for b-dār/'wach')\", \"stance\": \"silent\",\n       \"note\": \"Horn has no entry for bīdār; grep of HRN.txt for 'b.dar', 'wach'', 'erwachen' returns only unrelated items (bālīden 'wachsen', rusten 'wachsen'), so the word is simply not treated in the Grundriss.\"},\n      {\"src\": \"ARY\", \"where\": \"p.142 (pdf leaf 141), headword بیدار\", \"stance\": \"supports\",\n       \"note\": \"Aryanpur gives بیدار an inherited Indo-European pedigree, listing اوستایی / پهلوی / سانسکریت / یونانی / لاتین / گوتیک / نورس کهن cognates in one entry (ARY_pages.txt lines 4109-4125; the Latin-script column of the OCR is badly garbled, but the language labels and the Persian headword are legible).\"},\n      {\"src\": \"BQT\", \"where\": \"Borhān + Moʿin's notes (not cited by Nourai for this node)\", \"stance\": \"silent\",\n       \"note\": \"no bīdār entry was consulted; Nourai cites only Moʿin here.\"}\n     ]\n    },\n    {\n     \"id\": 4, \"lang\": \"Greek\", \"words\": \"gregorious\", \"verdict\": \"confirmed\",\n     \"derivation\": \"The Greek word is γρήγορος grḗgoros 'awake, watchful' (and ἐγρήγορος), a back-formation from ἐγρήγορα egrḗgora, the reduplicated second perfect of ἐγείρω egeírō 'I awaken, rouse' (< *h₁ger-, with ἐ- from the adverb *e); from it Hellenistic and New-Testament Greek made the present γρηγορέω grēgoréō 'to be watchful, keep awake' (Mt 24.42), and from that the Christian personal name Γρηγόριος Grēgórios 'watchful'. Nourai's 'gregorious' is that name, written with his usual rendering of classical -ος/-us as -ous (compare 'geranous' in the chart below and 'sextarious' elsewhere in the book); it is not a misprint but it is also not a citable Greek form — the citable forms are γρήγορος and Γρηγόριος. The gloss 'awake, watchful' is exactly right, and the descent from the root is uncontroversial.\",\n     \"derivation_fa\": \"صورت یونانی γρήγορος grḗgoros «بیدار، هشیار» است که از ἐγρήγορα (ماضی نقلی مضاعف فعل ἐγείρω «بیدار کردن») ساخته شده؛ از آن در یونانیِ دورهٔ هلنی فعل γρηγορέω «بیدار ماندن، پاسبانی کردن» و سپس نام مسیحیِ Γρηγόριος «بیدار، هشیار» پدید آمده است. «gregorious» در کتاب همان Γρηγόριος است با شیوهٔ همیشگی نورایی در نوشتن پایانهٔ ‑ος/‑us به‌صورت ‑ous؛ پس غلط چاپی نیست، هرچند صورتی نیست که در منابع یونانی بتوان به آن استناد کرد. معنایی که داده («بیدار، هشیار») و پیوندش با ریشه هر دو درست است. ادعای نورایی درست است.\",\n     \"sources\": [E_GER, W_HGER],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"not_found\",\n       \"note\": \"the Watkins appendix on disk (1985 standalone edition of the same list) has no root for 'to awake': the alphabetical neighbours are 'gerə-¹. To grow old' and 'gerə-². To cry hoarsely', and no entry anywhere in the file contains Gregory, gregorios or egeirō. The 1976 New College appendix Nourai actually cites is not open online, so I cannot exclude that it carried a root there; Etymonline, which follows Watkins's numbering, does cite 'PIE root *ger- (2) „to be awake“' for Gregory.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"vol. I p.673, s.v. Gregory\", \"stance\": \"supports\",\n       \"note\": \"'Gregory, masc. PN. — Late L. Gregorius, fr. Gk. Γρηγόριος, fr. γρήγορος „watchful“, which is rel. to ἐγρήγορα, second perfect of ἐγείρειν „to awaken“, fr. I.-E. base *ger-, „to be awake“, whence also OI. jāgarti „he is awake“, Avestic ā-garayeiti „wakes up, arouses“' (KLN_1966.txt line 16664) — Nourai's whole chart in one paragraph.\"},\n      {\"src\": \"Etymonline\", \"where\": \"s.v. Gregory / Gregorian\", \"stance\": \"supports\",\n       \"note\": \"'nativization of Late Latin Gregorius, literally „wakeful“ (equivalent to Latin Vigilantius), from Greek gregorios, a derivative of gregoros „to be watchful“, from PIE root *ger- (2) „to be awake“ ... At times confused with Latin gregarius'.\"},\n      {\"src\": \"POK\", \"where\": \"IEW p.390\", \"stance\": \"supports\",\n       \"note\": \"'gr. ἐγείρω „awake“ ... Perf. ἐ-γρή-γορα ... of Perf. proceed from ἐγρήγορτι „on guard“, ἐγρηγορσις; ἐγρήσσω „watch“'.\"}\n     ]\n    },\n    {\n     \"id\": 5, \"lang\": \"Latin\", \"words\": \"gregorious\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Late Latin Gregorius, taken over from Greek Γρηγόριος when the name spread through the eastern and then the western Church in the 3rd-6th centuries (Gregory Thaumaturgus, Gregory of Nazianzus, Gregory of Nyssa, Pope Gregory I 590-604). Latin only substituted its own -ius for Greek -ιος; the word is a borrowing, not an inherited Latin form, and Nourai's arrow Greek → Latin is therefore right. The box carries no reference in the book, and again 'gregorious' is Nourai's -ous spelling of Gregorius. Note the trap Etymonline points out: Latin gregārius 'of the herd' (from grex) looks similar but belongs to a different root (*ger- 'to gather', Pokorny 382), and the two have been confused since antiquity.\",\n     \"derivation_fa\": \"لاتینی متأخر Gregorius وام‌واژه‌ای است از یونانی Γρηγόριος که همراه گسترش نام‌های مسیحی در سده‌های سوم تا ششم میلادی به لاتین راه یافت (گرگوریوس نازیانزی، گرگوریوس نیسایی، پاپ گرگوریوس یکم ۵۹۰–۶۰۴ م.)؛ لاتین تنها پایانهٔ ‑ιος یونانی را به ‑ius خود بدل کرده است. پس پیکان «یونانی ← لاتین» در نمودار درست است و این واژه وام‌گرفته است نه میراثی. «gregorious» باز همان شیوهٔ نگارش نورایی است. یادآوری: واژهٔ لاتینی gregārius «گله‌ای» (از grex) شبیه این نام است ولی از ریشهٔ دیگری (*ger- «گرد آوردن»، پوکورنی ۳۸۲) می‌آید و از دیرباز با آن اشتباه شده است. ادعای نورایی درست است.\",\n     \"sources\": [E_GER],\n     \"ref_check\": [\n      {\"ref\": \"None\", \"status\": \"not_checked\",\n       \"note\": \"the box carries no reference in the book; the claim was checked instead against Klein and Etymonline (see consulted).\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"vol. I p.673, s.v. Gregory / Gregorian\", \"stance\": \"supports\",\n       \"note\": \"'Gregorian, adj. — Lit. „pertaining to Gregory“, fr. Late L. Gregorianus, fr. Gregorius'; and s.v. Gregory 'Late L. Gregorius, fr. Gk. Γρηγόριος'.\"},\n      {\"src\": \"Etymonline\", \"where\": \"s.v. Gregorian\", \"stance\": \"supports\",\n       \"note\": \"'from Late Latin Gregorianus, from Gregorius (see Gregory)'.\"}\n     ]\n    },\n    {\n     \"id\": 6, \"lang\": \"English\", \"words\": \"Gregory, Gregorian\", \"verdict\": \"confirmed\",\n     \"derivation\": \"English Gregory is the nativised Late Latin Gregorius; it became common in England and Scotland by the mid-12th century, largely because Pope Gregory I had sent Augustine's mission to the English in 597. Gregorian is from Late Latin Gregorianus: used of church music from c.1600 (Gregorian chant, traditionally codified by Gregory I) and of the calendar from the 1640s (introduced by Gregory XIII in 1582, adopted in England and its colonies only in 1752). Both therefore carry the Greek sense 'watchful' fossilised in a name, which is why Latin writers glossed Gregorius with Vigilantius.\",\n     \"derivation_fa\": \"Gregory انگلیسی همان Gregorius لاتینی متأخر است که بومی شده؛ از میانهٔ سدهٔ دوازدهم میلادی در انگلستان و اسکاتلند رواج یافت، بیشتر از آن رو که پاپ گرگوریوس یکم در سال ۵۹۷ م. هیئت مبلغان را به انگلستان فرستاده بود. Gregorian از Gregorianus لاتینی است: از حدود ۱۶۰۰ م. دربارهٔ آواز کلیسایی (سرود گرگوری) و از دههٔ ۱۶۴۰ م. دربارهٔ گاه‌شمار (اصلاح پاپ گرگوریوس سیزدهم در ۱۵۸۲ م. که انگلستان تا ۱۷۵۲ م. آن را نپذیرفت). معنای یونانی «هشیار، بیدار» در این نام سنگ‌واره شده است؛ از همین رو نویسندگان لاتینی Gregorius را به Vigilantius برمی‌گرداندند. ادعای نورایی درست است.\",\n     \"sources\": [E_GER],\n     \"ref_check\": [\n      {\"ref\": \"None\", \"status\": \"not_checked\",\n       \"note\": \"no reference is printed in the box; checked against Klein, Webster and Etymonline instead (see consulted).\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"vol. I p.673\", \"stance\": \"supports\",\n       \"note\": \"'Gregorian, adj. — Lit. „pertaining to Gregory“, fr. Late L. Gregorianus, fr. Gregorius. See next word' / 'Gregory, masc. PN. — Late L. Gregorius, fr. Gk. Γρηγόριος'.\"},\n      {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century, s.v. Gregorian\", \"stance\": \"supports\",\n       \"note\": \"'Gregorian calendar; a corrected form of the Julian calendar, introduced by Pope Gregory XIII in 1582 ...'; 'Gregorian chant; a mode of singing or chanting introduced by Pope Gregory I' (WEB_vol1.txt lines 84447-84448) — confirms the two English uses Nourai lists.\"},\n      {\"src\": \"Etymonline\", \"where\": \"s.v. Gregory, Gregorian\", \"stance\": \"supports\",\n       \"note\": \"'masc. proper name, popular in England and Scotland by mid-12c. (Pope Gregory I sent the men who converted the English to Christianity)'.\"}\n     ]\n    }\n   ]\n  },\n  {\n   \"entry\": 1,\n   \"root\": \"Ger 4, Gurr, Gurô\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *gerh₂- 'to cry hoarsely' (Pokorny '2. ger-', IEW 383-385; Walde-Pokorny I 591 ff.; Watkins gerə-²), with Mann's expressive by-form *gur-/gurr-, *gurō (IEC 308)\",\n   \"note\": \"Both halves of the root box check out and both of Nourai's citations are exact. Pokorny's '2. ger- „to scream (in expr. forms)“' occupies pp. 383-385 — the page Nourai gives — and contains, in this order, Old Indic járate, the crane names (Gk. γέρανος, Lat. grūs, Arm. krunk, OHG kranuh, OE cran), and the *krē-/*krā- crow words; Mann's IEC col. 308 has the second headword Nourai prints, 'gurō, iō (gurr-) (1) „coo, croon; growl“', with Persian γuram, γurram, Latin gurriō, MHG kurren, English churr, cur, ON kurra. The modern reconstruction writes the root *gerh₂- and stresses that it is onomatopoeic (Wiktionary s.v. grūs: 'the onomatopoeic root *gerh₂- „to cry hoarsely“ which derived several words for birds, especially cranes and crows'; Ernout-Meillet, s.v. grūs: 'nom originellement expressif ... la racine semble être dissyllabique du type *gerə-'). That is also the caveat that runs through the whole chart: with an imitative root, formal agreement between branches proves much less than usual, which is why AHD marks cur 'more likely imitative' and why the Persian box (#1) can be no more than plausible. One node is positively wrong: Persian زار (#3) belongs to a different root (see there).\",\n   \"note_fa\": \"هر دو بخش ریشه درست است و هر دو ارجاع نورایی دقیق‌اند. مادهٔ «2. ger-» پوکورنی با معنای «به آواز خشن بانگ زدن» در صفحات ۳۸۳–۳۸۵ آمده — همان صفحه‌ای که نورایی داده — و در آن به‌ترتیب سنسکریت járate، نام‌های درنا (یونانی γέρανος، لاتین grūs، ارمنی krunk، آلمانی علیای کهن kranuh، انگلیسی کهن cran) و واژه‌های *krē-/*krā- «کلاغ» فهرست شده است؛ ستون ۳۰۸ فرهنگ مان نیز سرواژهٔ دوم نورایی را دارد: «gurō, iō (gurr-) „coo, croon; growl“» با فارسی γuram/γurram، لاتین gurriō، انگلیسی churr و cur. در بازسازی امروزی این ریشه *gerh₂- نوشته می‌شود و بر نام‌آوا (onomatopoeia) بودن آن تأکید می‌کنند. همین نکته هشدار اصلی این نمودار است: در ریشه‌های نام‌آوایی، شباهت صوری میان شاخه‌ها دلیل محکمی بر خویشاوندی نیست. یک خانه به‌روشنی نادرست است: «زار» فارسی (خانهٔ ۳) از ریشهٔ دیگری می‌آید (ذیل همان خانه توضیح داده شد).\",\n   \"sources\": [W_GRUS, E_CRANE],\n   \"ref_check\": [\n    {\"ref\": \"POK:383\", \"status\": \"supports\",\n     \"note\": \"POK_full.txt line 31216: 'Root / lemma: ger-2 / Meaning: to scream (in expr. forms) ... References: WP. I 591 ff., WH. I 583, 601 f., 615, 624 ... Page(s): 383-385' — Nourai's page and gloss exactly.\"},\n    {\"ref\": \"IEC:308\", \"status\": \"supports\",\n     \"note\": \"IEC.txt line 4519, on the leaf whose printed column number is 308: 'gurō, iō (gurr-) (1) „coo, croon; growl“. Cf. ghur- Per. γuram, γurram „roar“; ... Lat. gurriō, īre „croon, churr“; MHG kurren „growl“; ... Eng. to churr, beside cur, n.; ON kurra „growl“' — this is where Nourai's second and third root-names, 'Gurr, Gurô', come from.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"WLD\", \"where\": \"Bd. I 591 ff.\", \"stance\": \"supports\",\n     \"note\": \"'2. ger- in Schallworten, bes. für „heiser schreien“. Ai. járate „rauscht, tönt, knistert, ruft“, jara „das Rauschen“ (oder zu *gu̯er- oder *gʷerə-) ... Hierher der Kranichname ... gr. γέρανος „Kranich“' (WLD_Bd1 line 37223 ff.).\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. gerə-²\", \"stance\": \"supports\",\n     \"note\": \"'gerə-². To cry hoarsely; also the name of the crane. I. Words meaning „to cry hoarsely“; also words denoting the crow ... II. Words denoting a crane ... [Pok. 2. ger- 383.]' — same root, same Pokorny page.\"},\n    {\"src\": \"KLN\", \"where\": \"vol. I p.371, s.v. crane\", \"stance\": \"supports\",\n     \"note\": \"'All these words derive from the I.-E. imitative base *ger-, „to utter a hoarse cry“.'\"},\n    {\"src\": \"LAT\", \"where\": \"Ernout-Meillet p.505 f., s.v. grūs\", \"stance\": \"supports\",\n     \"note\": \"'Nom originellement expressif qui a pris des formes diverses dans les différentes langues ... La racine semble être dissyllabique du type *gerə-. Le g du groupe expressif *ger- ... n'est pas gʷ.'\"},\n    {\"src\": \"Wiktionary\", \"where\": \"s.v. grūs (Latin)\", \"stance\": \"supports\",\n     \"note\": \"'in any case from the onomatopoeic root *gerh₂- („to cry hoarsely“) which derived several words for birds, especially cranes and crows'.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Persian\", \"words\": \"ğorridan «غرّیدن» (+ غر ، غرّان ، غرّش)\", \"verdict\": \"plausible\",\n     \"derivation\": \"غرّیدن ġorrīdan 'to roar, growl' with its family غر ġorr, غرّان ġorrān 'roaring', غرّش ġorreš 'roar' is a genuine Persian word and not, despite the غ, an Arabic loan: Moʿin tags both غر and غریدن 'اصت.' (اسم صوت, sound-word), the label he uses for onomatopoeia, and gives no Arabic origin. Mann is Nourai's authority and does put it here: IEC 308 lists 'Per. γuram, γurram „roar“' under *gurō/gurr- beside Latin gurriō, MHG/LG kurren, ON kurra and English churr, cur. What cannot be shown is descent: no Iranian etymological dictionary reconstructs an Old Iranian verb for it (Cheung's nearest root, *gram 'to thunder, roar' < PIE *gʷʰrem-, Pokorny 458 f., yields NP غرنبیدن ġorombīdan and گرمیدن, not غرّیدن), Wiktionary's Persian entry gives the verb with no etymology at all, and the geminate -rr- and initial ġ- are the standard shape of Persian imitative verbs. So the resemblance to Latin gurriō and ON kurra is real but is most economically explained as parallel imitation of the same noise rather than as inheritance from a Proto-Indo-European lexeme — which is exactly the weakness of any 'root' of this kind.\",\n     \"derivation_fa\": \"«غرّیدن» با خانوادهٔ آن (غر، غرّان، غرّش) واژه‌ای اصیل فارسی است و با آنکه با «غ» نوشته می‌شود، معرّب یا وام‌واژهٔ عربی نیست: معین هم «غر» و هم «غریدن» را با نشانهٔ «اصت.» (اسم صوت) آورده، یعنی آن را نام‌آوا می‌داند و هیچ نشان عربی [ع.] برایش نمی‌گذارد. مأخذ نورایی، یعنی مان (ستون ۳۰۸)، همین‌جا آورده است: «Per. γuram, γurram „roar“» در کنار لاتین gurriō و نورس کهن kurra و انگلیسی churr و cur. آنچه اثبات‌پذیر نیست، «تبار» است: هیچ فرهنگ ریشه‌شناسی ایرانی فعل ایرانی باستانی برای آن بازنمی‌سازد (نزدیک‌ترین ریشه در چونگ، *gram «غریدن، خشمگین شدن» از *gʷʰrem-، پوکورنی ۴۵۸، به «غرنبیدن» و «گرمیدن» می‌رسد نه «غرّیدن»)، ویکی‌واژه هم برای آن ریشه‌شناسی ندارد، و تشدید «رّ» و «غ» آغازین درست همان ساختِ آشنای فعل‌های نام‌آوایی فارسی است. پس شباهت به gurriō لاتینی واقعی است اما محتمل‌تر آن است که هر دو زبان جداگانه از یک صدا واژه ساخته باشند. با احتیاط پذیرفتنی است.\",\n     \"sources\": [W_GHOR],\n     \"ref_check\": [\n      {\"ref\": \"MON:2411\", \"status\": \"partial\",\n       \"note\": \"the headword is in Moʿin — 'غریدن: (اصت. مص‌ل.) (غریده ...' (MON_part2.txt line 1541), and the same 'اصت.' tag on 'غر: (اصت.) آواز غوک، صدای وزغ' (line 904) — but only the two-volume Adena abridgement is on disk, which has no page correspondence to the six-volume edition, so p.2411 itself could not be verified.\"},\n      {\"ref\": \"IEC:308\", \"status\": \"supports\",\n       \"note\": \"'gurō, iō (gurr-) (1) „coo, croon; growl“ ... Per. γuram, γurram „roar“' (IEC.txt line 4519) — Mann does place the Persian verb under this root, exactly as the arrow claims.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"IEC\", \"where\": \"col. 308, s.v. gurō, -iō (gurr-)\", \"stance\": \"supports\",\n       \"note\": \"'Per. γuram, γurram „roar“ ... Lat. gurriō, īre „croon, churr“ ... ON kurra „growl“'.\"},\n      {\"src\": \"MON\", \"where\": \"s.vv. غر, غریدن\", \"stance\": \"partial\",\n       \"note\": \"'غریدن: (اصت. مص‌ل.)' and 'غر: (اصت.) آواز غوک، صدای وزغ' — Moʿin classes the word as an اسم صوت (onomatopoeia) and gives it no foreign-origin tag; he says nothing about Indo-European.\"},\n      {\"src\": \"ARY\", \"where\": \"pp.386-387, entry containing غرش، غرنبه، غرمبه، غرنبیدن، غریدن\", \"stance\": \"partial\",\n       \"note\": \"Aryanpur puts غریدن in one Indo-European entry with غرنبیدن and cognates in Avestan, Pahlavi, Kurdish (gurr-), Pashto and Greek, and his own gloss of the Greek member is 'شیهه کشیدن' (to neigh) — i.e. Greek χρεμετίζω, which belongs to *gʰrem-/*gʷʰrem- (Pokorny 458 f.), not to Pokorny 383. So he keeps the word Indo-European but hangs it on a different root than Nourai (ARY_pages.txt lines 11464, 11493).\"},\n      {\"src\": \"CHEUNG\", \"where\": \"s.v. *gram 'to thunder, roar; to anger'\", \"stance\": \"silent\",\n       \"note\": \"Cheung has no verbal root that would give غرّیدن; his *gram (PIE *gʷʰrem-, Pok. 458 f.) yields 'NP gurunbīdan ... NP garmīdan „to thunder, roar, fly in a passion“' — a different Persian verb.\"},\n      {\"src\": \"Wiktionary\", \"where\": \"s.v. غریدن\", \"stance\": \"silent\",\n       \"note\": \"the Persian entry gives only 'غریدن (ġorridan) (present stem غر (ġorr)) — to roar', with no etymology section.\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Sanskrit\", \"words\": \"jaratĕ\", \"verdict\": \"plausible\",\n     \"derivation\": \"Sanskrit járate (3sg. middle, RV) is real and does mean 'sounds, rustles, crackles, calls', and Pokorny does open his '2. ger-' article with it — Nourai's 'jaratĕ ... to cry loudly' is copied straight from there. But both Pokorny and, more explicitly, Walde-Pokorny hedge the attribution in the same sentence: 'Ai. járate „rauscht, tönt, knistert, ruft“, jara „das Rauschen“ (oder zu *gu̯er- oder *gʷerə-)'. The reason is that Sanskrit j- is ambiguous — it can continue plain *g palatalised before a front vowel, but also *ǵ and *gʷ — whereas the rest of this root's material (Gk. géranos, Lat. grūs, Lith. gérvė, OE cran) has an unambiguous plain velar. Modern Indo-Aryan lexicography (Mayrhofer EWAia I 574 and the derived literature, which Cheung follows) separates a Sanskrit jar- 'to sing, call' from jar- 'to wake' and jar- 'to grow old', and links the first with the *ǵerH₂-/*gʷerH- 'call, praise' family rather than with the crane root. So the form and gloss are right; the placement under this root is Pokorny's own, expressly uncertain.\",\n     \"derivation_fa\": \"سنسکریت járate (سوم‌شخص مفرد میانه، ریگ‌ودا) واژه‌ای واقعی است و معنایش «آوا می‌دهد، خش‌خش می‌کند، بانگ می‌زند» است، و پوکورنی نیز مادهٔ «2. ger-» را با همین واژه آغاز می‌کند؛ پس آنچه نورایی نوشته از همان‌جا گرفته شده است. اما پوکورنی و روشن‌تر از او والده‑پوکورنی در همان جمله تردید می‌کنند: «(oder zu *gu̯er- oder *gʷerə-)». علتش آن است که «ج» سنسکریت چندپهلوست و می‌تواند دنبالهٔ *g کامی‌شده، *ǵ یا *gʷ باشد، حال آنکه بقیهٔ مواد این ریشه (γέρανος یونانی، grūs لاتینی، gérvė لیتوانیایی، cran انگلیسی کهن) بی‌گمان از *g ساده‌اند. ریشه‌شناسی امروزی (مایرهوفر و به‌پیروی او چونگ) jar «سرودن، بانگ زدن» را از jar «بیدار شدن» و jar «پیر شدن» جدا می‌کند و آن را به خانوادهٔ *ǵerH₂- «خواندن، ستودن» می‌بندد. پس صورت و معنا درست است ولی جای‌دهی زیر این ریشه، حتی به گفتهٔ خود پوکورنی، قطعی نیست: با احتیاط پذیرفتنی است.\",\n     \"sources\": [W_GRUS],\n     \"ref_check\": [\n      {\"ref\": \"POK:383\", \"status\": \"supports\",\n       \"note\": \"the word is the first item of the entry on that page: 'Material: A. Old Indic járate „it rushes, sounds, crackles, shouts“, jara „the rustling, murmuring“ (or to *gu̯er- or *gʷer-)' (POK_full.txt line 31220) — support, but with Pokorny's own reservation attached.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"WLD\", \"where\": \"Bd. I 591\", \"stance\": \"partial\",\n       \"note\": \"'Ai. járate „rauscht, tönt, knistert, ruft“, jara „das Rauschen“ (oder zu *gu̯er- oder *gʷerə-)' — the parenthesis is the doubt.\"},\n      {\"src\": \"CHEUNG\", \"where\": \"s.v. *zarH 'to bewail the deceased' (note)\", \"stance\": \"partial\",\n       \"note\": \"'Ir. *zarH (connected to Skt. jar „to sing“ ?) should therefore be separated from *garH¹, Skt. gar „to greet, praise“' — Cheung treats Skt. jar 'to sing' as a separate, laryngeal-final root, not as part of the crane/crow root.\"},\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. gerə-²\", \"stance\": \"silent\",\n       \"note\": \"Watkins lists no Sanskrit member of this root at all — only Germanic, Latin and Greek forms.\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"Persian\", \"words\": \"zâr 2 «زار ۲» (+ زاری)\", \"verdict\": \"disputed\",\n     \"derivation\": \"The Persian word is right and so is the gloss — زار zār 'lament, moaning; wailing', with زاری zārī 'lamentation' and زاریدن zārīdan 'to weep, moan' — and the arrow is exactly what Horn writes on the page Nourai cites: 'zār „Klagen“, zārī, zāre, zārīden. ai. 3 √jar-, járate „rauschen, schnattern, rufen“; afγ. žaṛai „klagen“; oss. d. zarun, i. zarin „singen“' (Grundriss no. 646, p.143). Modern Iranian scholarship, however, puts the word under a different Proto-Indo-European root. Cheung reconstructs Iranian *zarH 'to bewail the deceased' (with Sogdian zʾry 'pitiful', MP/Parthian zārīg 'sorrow', Ossetic zarun 'to sing' — Horn's own comparanda) and derives it from PIE *ǵ(e)rH₂- 'to bewail (by lamenting, calling, singing in honour of the deceased)', Pokorny 352, not 383; Wiktionary derives زار and زاریدن from Proto-Iranian *jāráyati (the *ǵ-series that gives Iranian z-), citing Cheung 2007 pp.469-470. The decisive point is phonetic: New Persian z- can only continue a palatal *ǵ (Proto-Iranian *dz), whereas the root of this chart is a plain velar *g throughout (Gk. géranos, Lat. grūs, Lith. gérvė), which in Iranian would have given g- or ǰ-, never z-. Nourai's Sanskrit link survives only in the weak form in which Cheung states it ('connected to Skt. jar „to sing“ ?'). Note also that Pokorny's third homonym, 'ger-, gerə-, grē- to rub; to be old' (IEW 390-391), claims a different Persian zār — 'npers. zār „weak, woeful, wretched“, zar „graybeard“' — which is Horn's separate entry no. 647 'zār „schwach, elend“ ... aw. √zar- „altern“'; Nourai's numbering 'zār 2' correctly keeps the two apart.\",\n     \"derivation_fa\": \"خودِ واژه و معنای آن درست است — «زار» به معنی نالان و گریان، با «زاری» و «زاریدن» — و پیکان نمودار دقیقاً همان است که هرن در صفحهٔ ۱۴۳ (شمارهٔ ۶۴۶) نوشته: «zār „Klagen“, zārī, zārīden؛ سنسکریت √jar، járate „بانگ زدن“؛ پشتو žaṛai „ناله“؛ آسی zarun „سرودن“». اما ریشه‌شناسی امروزی این واژه را به ریشهٔ دیگری می‌بندد: چونگ ایرانی *zarH «سوگواری برای درگذشته» را بازمی‌سازد (با سغدی zʾry، پهلوی و پارتی zārīg «اندوه» و آسی zarun «سرودن») و آن را از هندواروپایی *ǵ(e)rH₂- (پوکورنی ۳۵۲) می‌گیرد، نه از پوکورنی ۳۸۳؛ ویکی‌واژه نیز «زار» و «زاریدن» را از ایرانی آغازین *jāráyati به‌استناد چونگ (صص ۴۶۹–۴۷۰) می‌آورد. دلیل قاطع آوایی است: «ز» فارسی نو تنها می‌تواند دنبالهٔ *ǵ کامی (ایرانی آغازین *dz) باشد، حال آنکه ریشهٔ این نمودار سرتاسر *g ساده است (γέρανος، grūs، gérvė) که در ایرانی به g یا ج می‌رسید نه به ز. افزون بر این، پوکورنی در صفحات ۳۹۰–۳۹۱ زیر ریشهٔ «ساییدن؛ پیر شدن» زارِ دیگری را می‌آورد («npers. zār „ناتوان، بیچاره“، zar „پیرمرد“») که همان مدخل جداگانهٔ ۶۴۷ هرن است؛ شمارهٔ «زار ۲» نورایی این دو را درست از هم جدا کرده است. در مجموع: پژوهش امروزی جای‌دهی نورایی را رد می‌کند.\",\n     \"sources\": [W_ZAR, W_JAR],\n     \"ref_check\": [\n      {\"ref\": \"HRN:143\", \"status\": \"supports\",\n       \"note\": \"Horn p.143 (HRN.txt leaf 165), entry '646. (1) zār „Klagen“, zārī, zāre, zārīden. ai. 3 √jar-, járate „rauschen, schnattern, rufen“; afγ. žaṛai „klagen“; oss. d. zarun, t. zarin „singen“' — precisely Nourai's Sanskrit→Persian arrow. (Horn's next entry, '647. (2) zār „schwach, elend“ ... aw. √zar- „altern“', is the homonym Nourai's '2' distinguishes.)\"},\n      {\"ref\": \"BQT:995\", \"status\": \"partial\",\n       \"note\": \"the Borhān entry is in the vol.-2 scan on disk (BQT_v2_pages.txt, leaf 457): 'زار: بر وزن لار. بمعنی مکان روییدن باشد همچو گلزار و لاله‌زار ... و ضعیف و نحیف و خوار و خفیف - و نالان و گریان - و گریه کردن بسوز را نیز گفته‌اند' — it supports the gloss 'cry' (نالان و گریان) but offers no etymology, and the scan's printed page numbers are not OCRed, so p.995 could not be confirmed (the leaf maps to roughly pp. 980-995 depending on the volume's front matter).\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"HRN\", \"where\": \"no. 646, p.143\", \"stance\": \"supports\",\n       \"note\": \"quoted above — Horn is the source of Nourai's arrow.\"},\n      {\"src\": \"CHEUNG\", \"where\": \"pp.470-471, '*zarH to bewail the deceased'\", \"stance\": \"contradicts\",\n       \"note\": \"'*NWIR: NP zārīdan „to weep, moan“ (LW) ... *NEIR: Oss. I. zælyn/zæld „to sound“, zaryn/zard, D. zarun/zard „to sing“ ... ¶ The Ir. forms appear to refer to the bewailing ceremony ... «PIE *ǵ(e)rH₂- „to bewail the deceased“ ⇒ LIV: 161 | Pok.: 352' — a different root and a different Pokorny page from Nourai's 383.\"},\n      {\"src\": \"Wiktionary\", \"where\": \"s.v. زار (Persian, Etymology 1) and Reconstruction:Proto-Iranian/jāráyati\", \"stance\": \"contradicts\",\n       \"note\": \"'زار (zâr): groan, lament. Ultimately from Proto-Iranian *jāráyati', whose page cites Cheung 2007 pp.469-470 (*zarH¹, *zarH³) and gives 'Parthian *zārdēd → Middle Persian → Persian زاریدن'.\"},\n      {\"src\": \"POK\", \"where\": \"IEW 390-391, 'ger-, gerə-, grē- to rub; to be old'\", \"stance\": \"partial\",\n       \"note\": \"'lengthened grade jāra- „aging, maturing“ (= npers. zār „weak, woeful, wretched“, zar „graybeard“)' — Pokorny does connect a Persian zār with an IE root, but it is the homonym meaning 'weak, wretched', under the 'grow old' root, not under 383.\"},\n      {\"src\": \"BQT\", \"where\": \"vol. 2 leaf 457, s.v. زار\", \"stance\": \"partial\",\n       \"note\": \"'... و نالان و گریان - و گریه کردن بسوز را نیز گفته‌اند' — the meaning is confirmed, the etymology is not treated.\"}\n     ]\n    },\n    {\n     \"id\": 4, \"lang\": \"Germanic\", \"words\": \"krĕ, krô, kur; kranu\", \"verdict\": \"confirmed\",\n     \"derivation\": \"These are Watkins's Germanic reconstructions under gerə-², reproduced by Nourai with his own vowel marks: Germanic *krē- (with the ablaut variant *krā-, Nourai's 'krô') in OE crāwe 'crow', crāwan 'to crow', cracian 'to resound', MDu. krāken, ON kraka, MDu. krānen 'to groan, lament'; Germanic *kur(r)- in ON kurra 'to growl'; and, for the bird, Germanic *kran- / *kranu- in OE cran, cranoc, OHG kranuh, MLG kranek, ON trani (with unexplained t-). Nourai's 'kranu' is the -u-stem variant (OHG kranuh < *kranuk-, OE cranoc) beside plain *kran-; Pokorny classes exactly these under his section 'B.2. With formant -en-, to part with -u- and -g- extended'. The one hedge worth recording is Watkins's own on the third form: '2. Possibly (but more likely imitative) Germanic *kur(r)- in Old Norse kurra, to growl, akin to Middle English curre, cur'.\",\n     \"derivation_fa\": \"این صورت‌ها بازسازی‌های ژرمنی واتکینز ذیل مادهٔ gerə-² هستند که نورایی با نشانه‌های واکه‌ای خودش نقل کرده است: ژرمنی *krē- (و گونهٔ آواگردانِ *krā- که نورایی krô نوشته) در انگلیسی کهن crāwe «کلاغ»، crāwan «بانگ خروس زدن»، cracian «طنین انداختن»، هلندی میانه krāken و krānen «نالیدن»، نورس کهن kraka؛ ژرمنی *kur(r)- در نورس کهن kurra «غرّیدن»؛ و برای نام پرنده ژرمنی *kran-/*kranu- در انگلیسی کهن cran و cranoc، آلمانی علیای کهن kranuh. «kranu» نورایی همان گونهٔ ستاک‑u است در کنار *kran- ساده، و پوکورنی نیز همین‌ها را در بخش «با پسوند ‑en-، بخشی با ‑u- و ‑g- گسترده» می‌آورد. تنها نکته آنکه خود واتکینز دربارهٔ سومین صورت می‌نویسد «شاید، ولی محتمل‌تر آنکه نام‌آوایی باشد». ادعای نورایی درست است.\",\n     \"sources\": [E_CRANE],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\",\n       \"note\": \"Watkins 1985 s.v. gerə-²: '1. Germanic *krē- in: a. Old English crāwe, a crow: CROW¹; b. Old English crāwan, to crow: CROW²; c. Old English cracian, to resound: CRACK; ... f. Middle Dutch krānen, to groan, lament: CROON. 2. Possibly (but more likely imitative) Germanic *kur(r)- in Old Norse kurra, to growl, akin to Middle English curre, cur: CUR. II. Words denoting a crane. 1. Germanic *kran-, crane, in: a. Old English cran, crane: CRANE ...'\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. gerə-²\", \"stance\": \"supports\", \"note\": \"quoted above; it is the direct source of Nourai's box.\"},\n      {\"src\": \"POK\", \"where\": \"IEW 383-385\", \"stance\": \"supports\",\n       \"note\": \"'Old High German kranuh (-ih), Old English cranoc, cornuc, Middle Low German kranek m. (*granug-); Old English cran, asachs. krano ... D. grā- in West Germanic nord. *krā-: Old High German krāen ... Old English crāwan'.\"},\n      {\"src\": \"KLN\", \"where\": \"vol. I p.371, s.v. crane\", \"stance\": \"supports\",\n       \"note\": \"'ME. crane, crone, fr. OE. cran, rel. to OS., OHG. krano, Du. kraan, MHG. krone, OE. cranoc, cornoc, MLG. kranek, OHG. chranuh ... All these words derive from the I.-E. imitative base *ger-'.\"}\n     ]\n    },\n    {\n     \"id\": 5, \"lang\": \"English\", \"words\": \"crow, crack, croon, cur; crane\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Each of the five is the standard descendant of the Germanic forms in the box above: crow (n.) < OE crāwe and crow (v.) < OE crāwan 'to make the cock's cry'; crack < OE cracian 'to make a sharp noise, resound'; croon < Middle Dutch krōnen 'to groan, lament', which entered English through Scots in the 15th century and only later acquired the sense 'to hum softly'; cur < Middle English curre, beside Old Norse kurra 'to growl' (Skeat: 'named from growling'); crane < OE cran, the bird, extended in the 14th century to the lifting machine — a metaphor Greek made independently, since γέρανος means both. The only qualification is the one Watkins prints for cur, 'more likely imitative', and Etymonline's remark on the bird name: 'Thus the name is perhaps an echo of its cry in ancient ears.'\",\n     \"derivation_fa\": \"هر پنج واژه دنبالهٔ قاعده‌مند صورت‌های ژرمنیِ خانهٔ پیشین‌اند: crow از انگلیسی کهن crāwe/crāwan؛ crack از cracian «طنین انداختن»؛ croon از هلندی میانه krōnen «نالیدن» که در سدهٔ پانزدهم از راه اسکاتلندی به انگلیسی رسید و بعدها معنای «زمزمه کردن» گرفت؛ cur از انگلیسی میانه curre در کنار نورس کهن kurra «غرّیدن» (اسکیت: «از غرّیدنش نام گرفته»)؛ و crane از انگلیسی کهن cran که در سدهٔ چهاردهم به «جرثقیل» نیز گسترش یافت — همان استعاره‌ای که یونانی γέρανος هم مستقلاً دارد. تنها قید کار، تردید واتکینز دربارهٔ cur («محتمل‌تر نام‌آوایی») و یادداشت اتیمانلاین است که نام درنا شاید بازتاب آوای خودِ پرنده باشد. ادعای نورایی درست است.\",\n     \"sources\": [E_CRANE],\n     \"ref_check\": [\n      {\"ref\": \"IEC:308\", \"status\": \"supports\",\n       \"note\": \"Mann's col. 308 has two of the five in the same article: 'Eng. to churr, beside cur, n.; ON kurra „growl“'.\"},\n      {\"ref\": \"AHD\", \"status\": \"supports\",\n       \"note\": \"Watkins 1985 s.v. gerə-² lists CROW¹, CROW², CRACK, CRACKNEL, CRAKE, CROON, CUR under I and CRANE, CRANBERRY under II — all five of Nourai's English words.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"vol. I p.371 (crane), p.1141 (pedigree)\", \"stance\": \"supports\",\n       \"note\": \"'crane, n. — ME. crane, crone, fr. OE. cran ... For the sense development of crane, which denotes also „a machine for raising weights“ ... cp. Gk. γέρανος „crane“ (in both senses of the English word).'\"},\n      {\"src\": \"SKT\", \"where\": \"Skeat, s.v. Cur\", \"stance\": \"supports\",\n       \"note\": \"'Cur. (Scand.) M.E. curre; dial. kurre, a dog + O. Da. kurre, a dog. Named from growling; [ON] kurra, to murmur, grumble.'\"},\n      {\"src\": \"Etymonline\", \"where\": \"s.v. crane (n.)\", \"stance\": \"supports\",\n       \"note\": \"'Old English cran, common Germanic ... from PIE *gerə-no-, suffixed form of root *gerə- (2) „to cry hoarsely“, also the name of the crane ... Thus the name is perhaps an echo of its cry in ancient ears.'\"}\n     ]\n    },\n    {\n     \"id\": 6, \"lang\": \"Greek\", \"words\": \"geranous\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Greek γέρανος géranos 'crane' (Homer, Il. 3.3, of the cranes' clamour; also 'crane for lifting weights' and, in Aristophanes, a fish). The form is *gerə-no- / *gerh₂-no-, the -en-/-no- suffix that this root uses for the bird all over the family — Welsh/Cornish/Breton garan, Armenian krunk (*geru-n-g-), OE cran, Gaulish tarvos trigaranos 'the bull with three cranes'. Nourai's 'geranous' is again his -ous spelling of a classical -ος ending, not a different word; the gloss 'crane' is correct.\",\n     \"derivation_fa\": \"یونانی γέρανος géranos «درنا» (هومر، ایلیاد ۳٫۳ دربارهٔ بانگ درناها؛ و نیز «جرثقیل»). ساختش *gerh₂-no- است، همان پسوند ‑en-/‑no- که این ریشه در سراسر خانوادهٔ هندواروپایی برای نام این پرنده به‌کار برده است: ولزی garan، ارمنی krunk، انگلیسی کهن cran، و گُلی tarvos trigaranos «گاو با سه درنا». «geranous» در کتاب باز همان شیوهٔ نگارش پایانهٔ ‑ος به‌صورت ‑ous است، نه واژه‌ای دیگر؛ و معنایی که داده درست است. ادعای نورایی درست است.\",\n     \"sources\": [E_GERAN],\n     \"ref_check\": [\n      {\"ref\": \"AHD:1516\", \"status\": \"supports\",\n       \"note\": \"the content is Watkins's, in the second half of gerə-²: '4. Suffixed extended form *gerə-no- in Greek geranos, crane: GERANIUM. [Pok. 2. ger- 383.]' The page 1516 belongs to the 1976 New College appendix (pp.1505-1550), which is not open online; the alphabetical position of the g-roots in that 46-page list is consistent with p.1516, and the copy on disk is the 1985 reprint with its own pagination.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"IEW 383\", \"stance\": \"supports\",\n       \"note\": \"'gr. γέρην · γέρανος Hes., γέρανος m. „crane“ and „crane for lifting weights, esp. used in the theatre, ... a fish“'.\"},\n      {\"src\": \"LAT\", \"where\": \"Ernout-Meillet, s.v. grūs\", \"stance\": \"supports\",\n       \"note\": \"'Il y a une formation en -n-, avec des vocalismes divers, dans gall. garan (gaul.-lat. tri-garanos „aux trois grues“), v.angl. cran, gr. γέρανος, arm. krunk'.\"},\n      {\"src\": \"KLN\", \"where\": \"vol. I, s.v. Geranium\", \"stance\": \"supports\",\n       \"note\": \"'fr. Gk. γέρανος „crane“, which is cogn. with L. grūs, OE. cran, „crane“'.\"}\n     ]\n    },\n    {\n     \"id\": 7, \"lang\": \"English\", \"words\": \"geranium\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Geranium entered English in the 1540s from Latin geranium, itself from Greek γεράνιον geránion, the diminutive of γέρανος 'crane' — the plant is named from the long beak-like seed-pod, which is why its native English name is cranesbill and the German is Kranichschnabel. Dioscorides already uses geránion as a plant name; Linnaeus took it over as the genus name in 1753. So the chain Greek → English of Nourai's arrow is right, with Latin as the (unshown) intermediary of the botanical Latin.\",\n     \"derivation_fa\": \"واژهٔ geranium در دههٔ ۱۵۴۰ م. از لاتینی geranium به انگلیسی رسیده و آن خود از یونانی γεράνιον، مصغّر γέρανος «درنا»، است: نام گیاه از میوهٔ دراز و منقارمانندش گرفته شده و به همین سبب نام بومی انگلیسی‌اش cranesbill «منقار درنا» است. دیوسکوریدس این نام گیاه را به کار برده و لینه در ۱۷۵۳ م. آن را نام جنس گیاه کرد. پس پیکان «یونانی ← انگلیسی» درست است، هرچند لاتین (لاتینِ گیاه‌شناسی) حلقهٔ میانی نشان‌داده‌نشده است. ادعای نورایی درست است.\",\n     \"sources\": [E_GERAN],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\",\n       \"note\": \"Watkins 1985 s.v. gerə-², II.4: 'Suffixed extended form *gerə-no- in Greek geranos, crane: GERANIUM' — GERANIUM is the English word the appendix hangs on the Greek form, exactly Nourai's arrow.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"vol. I, s.v. Geranium\", \"stance\": \"supports\",\n       \"note\": \"'Geranium, n., a genus of plants, the cranesbill (bot.) — L. geranion, geranium, „cranesbill“, fr. Gk. γεράνιον, of s.m., fr. γέρανος, „crane“ ... so called because the fruit resembles a cranesbill.'\"},\n      {\"src\": \"Etymonline\", \"where\": \"s.v. geranium\", \"stance\": \"supports\",\n       \"note\": \"'1540s, from Latin geranium, from Greek geranion, the plant name, diminutive of geranos „crane“ (cognate with Latin grus; see crane (n.)). So called from shape resemblance of seed pods to cranes' bills; the native name in English also was cranebill.'\"}\n     ]\n    },\n    {\n     \"id\": 8, \"lang\": \"Latin\", \"words\": \"grŭs; gurriô\", \"verdict\": \"plausible\",\n     \"derivation\": \"grūs, gruis f. 'crane' (from Lucilius on) is beyond doubt: Ernout-Meillet derive it from the same expressive root as garriō and grāculus and give the family Lith. gérvė, OCS žeravь, Welsh garan, OE cran, Gk. géranos; the Latin -u- formation is *gr̥h₂-u-s (metathesised, per Wiktionary, from *gerh₂ōws), and it gave Old French grue, hence English pedigree from pié de grue 'crane's foot'. The Latin verb of the crane's cry is gruere ('gruere dicuntur grues, ut sues grunnire', Paulus-Festus 86.13). Nourai's second form, gurriō 'churr, croon', is taken over from Mann (IEC 308, 'Lat. gurriō, īre „croon, churr“'), but it is not in the standard Latin dictionaries on disk: Ernout-Meillet and Walde's Lateinisches etym. Wörterbuch have no gurriō (they treat garriō, grunniō, gruō/gruere and gurgulio), and the form survives, if at all, only in the late glossary lists of animal noises. The box is therefore right for grūs and unverifiable beyond Mann for gurriō, which is why the node cannot be more than plausible; note also that grūs belongs to the crane half of the root and gurriō to the 'growl' half, which Nourai has correctly merged in his root name 'Ger 4, Gurr, Gurô'.\",\n     \"derivation_fa\": \"grūs, gruis (مؤنث) «درنا» از لوکیلیوس به بعد در لاتین گواهی شده و تردیدی در آن نیست: ارنو‑ می‌یه آن را از همان ریشهٔ نام‌آوایی garriō و grāculus می‌گیرند و با gérvė لیتوانیایی، žeravь اسلاوی کهن، garan ولزی، cran انگلیسی کهن و γέρανος یونانی می‌سنجند؛ ساخت ‑u دار لاتین *gr̥h₂-u-s است و همین واژه از راه فرانسهٔ کهن grue به انگلیسی pedigree (از pié de grue «پای درنا») رسیده است. فعل بانگ درنا در لاتین gruere است. اما صورت دوم، gurriō «غرّیدن، زمزمه کردن»، از مان (ستون ۳۰۸) گرفته شده و در فرهنگ‌های معتبر لاتین موجود در کتابخانهٔ محلی نیست: نه ارنو‑می‌یه و نه والده آن را ندارند (آن‌ها garriō، grunniō، gruō و gurgulio را می‌آورند) و این صورت، اگر هم باشد، تنها در فهرست‌های واژگانی متأخرِ آواهای جانوران دیده می‌شود. پس خانه برای grūs درست و برای gurriō تأییدناپذیر است: با احتیاط پذیرفتنی است.\",\n     \"sources\": [W_GRUS, E_CRANE],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\",\n       \"note\": \"Watkins 1985 s.v. gerə-², II.2: 'Extended form *grū- in Latin grūs, crane: GRUS; PEDIGREE' — supports grūs; the appendix says nothing about gurriō.\"},\n      {\"ref\": \"IEC:308\", \"status\": \"supports\",\n       \"note\": \"'Lat. gurriō, īre „croon, churr“' stands in Mann's article, so Nourai reproduces his source faithfully; the form's own attestation is the problem, not the citation.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"LAT\", \"where\": \"Ernout-Meillet pp.505-506, s.vv. gruō, grūs\", \"stance\": \"partial\",\n       \"note\": \"'grūs, -is f. ...: grue. — Depuis Lucilius. Panroman ... De là: gruō, -is: crier (de la grue), cf. P.F. 86,13 „gruere dicuntur grues, ut sues grunnire“ ... La racine semble être dissyllabique du type *gerə-.' The dictionary has grūs and gruere but no gurriō (grep of LAT.txt and LEW_1910.txt for 'gurr' returns nothing relevant).\"},\n      {\"src\": \"POK\", \"where\": \"IEW 384\", \"stance\": \"supports\",\n       \"note\": \"'3. With formants -ōu- : -u-: Latin grūs, Gen. gruis f. „a crane“, therefrom gruere „of crane's call“'.\"},\n      {\"src\": \"Wiktionary\", \"where\": \"s.v. grūs (Latin)\", \"stance\": \"supports\",\n       \"note\": \"'From Proto-Italic *grūs, from Proto-Indo-European *gr̥h₂-ú-s (which apparently metathesized to *grúh₂s), perhaps modified from *gerh₂ōws, in any case from the onomatopoeic root *gerh₂- („to cry hoarsely“)'.\"}\n     ]\n    }\n   ]\n  }\n ]\n}\n\nwith open('/home/sfmqrb/git/rishe/data/verification/page-175.json','w',encoding='utf-8') as f:\n    json.dump(doc,f,ensure_ascii=False,indent=2)\n    f.write('\\n')\nprint('ok')\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build175.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-175.json > /dev/null && echo \"JSON OK\" && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 175"
}
```


### [2026-09-05T21:12:15.354Z] TOOL RESULT

```
ok
JSON OK
nodes verified: 14/14
node verdicts: {'confirmed': 10, 'plausible': 3, 'disputed': 1}
root verdicts: {'confirmed': 2}
ref checks: {'partial': 5, 'not_found': 1, 'not_checked': 2, 'supports': 10}
books consulted: {'supports': 33, 'silent': 5, 'partial': 7, 'contradicts': 2} | by book: {'KLN': 7, 'CHEUNG': 6, 'Etymonline': 5, 'POK': 5, 'Wiktionary': 4, 'WLD': 2, 'PHD': 2, 'HRN': 2, 'ARY': 2, 'BQT': 2, 'AHD': 2, 'LAT': 2, 'BRT': 1, 'NYB': 1, 'WEB': 1, 'IEC': 1, 'MON': 1, 'SKT': 1}
```


## [2026-09-05T21:12:15.883Z] AGENT

You've hit your session limit · resets 7:40pm (America/Toronto)
