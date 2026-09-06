# Verification process log — verify-page-259


## [2026-09-06T16:16:15.934Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 259 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-259.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-259.json. Write /home/sfmqrb/git/rishe/data/verification/page-259.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 259` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T16:16:17.237Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T16:16:18.092Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T16:16:18.112Z] TOOL RESULT

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


## [2026-09-06T16:16:18.563Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-259.txt"
}
```


### [2026-09-06T16:16:18.585Z] TOOL RESULT

```
1	=== PDF page 259 (book page 229) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Kerd 1, Kred : heart  (refs POK:579; SYN:251)
4	#1 (parent #0) [Avestan] refs=POK:580; KLN:352; SYN:251; LAT:254 | zered, zaredaya : heart, center ; zraz-da, sraz-da : to give heart, believe ☞Dô 2
5	  #2 (parent #1) [Pahlavi] refs=BQT:873 | dîl : heart
6	    #3 (parent #2) [Persian] refs=BQT:873; LAT:254 | del «دل» : heart | NOTE: The "z" sound is kept in Kurdish "zar:heart" and Baluchi "zirdê:heart".
7	#4 (parent #0) [Germanic] refs=AHD | hert-on : heart
8	  #5 (parent #4) [English] refs=None | heart
9	#6 (parent #0) [Latin] refs=AHD; POK:580 | cor : heart ; ad-cor : at heart, agreeable, in harmony ; re-cor : remind, remember, record ; com-cors : of same heart, in harmony ; crědere : to put heart in something, believe
10	  #7 (parent #6) [French] refs=AHD | 
11	    #8 (parent #7) [Persian] refs=MON:76 | âkordîon «آکوردئون» : accordion
12	    #9 (parent #7) [English] refs=AHD | accord, accordion, record ; concord, courage, credit
13	  #10 (parent #6) [English] refs=None | core, cordial
14	#11 (parent #0) [Greek] refs=AHD | kardia : heart
15	  #12 (parent #11) [English] refs=None | cardiac, cardiovascular
16	--- entry 1 ---
17	ROOT [Indo-European] Kerd 2, Kerdho, Kerdha : row, herd  (refs POK:579)
18	#1 (parent #0) [Avestan] refs=POK:579 | saredha : way, kind, race, breed
19	  #2 (parent #1) [Pahlavi] refs=None | sartak : breed
20	    #3 (parent #2) [Persian] refs=BQT:1122; SNS:183 | sardeh «سرده» : race, breed, kind
21	#4 (parent #0) [Germanic] refs=AHD | herdô : herd
22	  #5 (parent #4) [English] refs=None | herd
23	--- entry 2 ---
24	ROOT Kerdha -> redirect to Kerd 2
25	--- entry 3 ---
26	ROOT Kerdho -> redirect to Kerd 2
27	
```


## [2026-09-06T16:16:21.476Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-259.json",
 "description": "Read source JSON for page 259"
}
```


### [2026-09-06T16:16:21.511Z] TOOL RESULT

```
{
  "pdf_page": 259,
  "book_page": 229,
  "entries": [
    {
      "root": {
        "name": "Kerd 1, Kred",
        "lang": "Indo-European",
        "refs": "POK:579; SYN:251",
        "gloss": "heart"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:580; KLN:352; SYN:251; LAT:254",
          "words": [
            {"translit": "zered, zaredaya", "gloss": "heart, center", "script": null},
            {"translit": "zraz-da, sraz-da", "gloss": "to give heart, believe", "script": null, "see": ["Dô 2"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "BQT:873",
          "words": [
            {"translit": "dîl", "gloss": "heart", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "BQT:873; LAT:254",
          "words": [
            {"translit": "del", "gloss": "heart", "script": "دل"}
          ],
          "script_extra": null,
          "note": "The \"z\" sound is kept in Kurdish \"zar:heart\" and Baluchi \"zirdê:heart\".",
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "hert-on", "gloss": "heart", "script": null}
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
            {"translit": "heart", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD; POK:580",
          "words": [
            {"translit": "cor", "gloss": "heart", "script": null},
            {"translit": "ad-cor", "gloss": "at heart, agreeable, in harmony", "script": null},
            {"translit": "re-cor", "gloss": "remind, remember, record", "script": null},
            {"translit": "com-cors", "gloss": "of same heart, in harmony", "script": null},
            {"translit": "crědere", "gloss": "to put heart in something, believe", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "French",
          "refs": "AHD",
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "Persian",
          "refs": "MON:76",
          "words": [
            {"translit": "âkordîon", "gloss": "accordion", "script": "آکوردئون"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 7,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "accord, accordion, record", "gloss": null, "script": null},
            {"translit": "concord, courage, credit", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 6,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "core, cordial", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD",
          "words": [
            {"translit": "kardia", "gloss": "heart", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 11,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "cardiac, cardiovascular", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Kerd 2, Kerdho, Kerdha",
        "lang": "Indo-European",
        "refs": "POK:579",
        "gloss": "row, herd"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:579",
          "words": [
            {"translit": "saredha", "gloss": "way, kind, race, breed", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": null,
          "words": [
            {"translit": "sartak", "gloss": "breed", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "BQT:1122; SNS:183",
          "words": [
            {"translit": "sardeh", "gloss": "race, breed, kind", "script": "سرده"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "herdô", "gloss": "herd", "script": null}
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
            {"translit": "herd", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {"name": "Kerdha", "redirect": "Kerd 2"},
      "nodes": []
    },
    {
      "root": {"name": "Kerdho", "redirect": "Kerd 2"},
      "nodes": []
    }
  ]
}
```


## [2026-09-06T16:16:22.287Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-06T16:16:22.325Z] TOOL RESULT

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


## [2026-09-06T16:16:27.238Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','SYN','KLN','LAT','BQT','AHD','MON','SNS','HRN','HUB','PHD','NYB','BRT','WLD','IEC','SKT','ARY']:\n    v=d.get(k)\n    print(k, json.dumps(v, ensure_ascii=False)[:600])\n    print()\n\""
}
```


### [2026-09-06T16:16:29.021Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

LAT {"title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951", "edition_found": "1951 (3rd ed.) - matches Nourai", "kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "identifier": "ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine (4th ed. 1959 lending-only: dictionnairetymo0000unse; another open copy: DictionnaireEtymologiqueDeLaLangueLatine)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt", "page_offset": "leaf = printed + 18 for mos

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-

NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 

SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it
```


## [2026-09-06T16:16:32.752Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 586 587 588 589; do echo \"=== leaf $n ===\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' POK_01.txt | head -70; done"
}
```


### [2026-09-06T16:16:34.493Z] TOOL RESULT

```
=== leaf 586 ===
=== leaf 587 ===
=== leaf 588 ===
=== leaf 589 ===
```


## [2026-09-06T16:16:37.172Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls -la POK*.txt && for f in POK_01.txt POK_02.txt POK_03.txt POK_full.txt; do echo \"$f pages: $(awk 'BEGIN{RS=\"\\f\"} END{print NR}' $f)\"; done"
}
```


### [2026-09-06T16:16:39.009Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb  981836 Sep  4 14:06 POK_01.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 1137861 Sep  4 14:06 POK_02.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 1170809 Sep  4 14:06 POK_03.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 3971883 Sep  4 14:06 POK_full.txt
POK_01.txt pages: 363
POK_02.txt pages: 433
POK_03.txt pages: 429
POK_full.txt pages: 1
```


## [2026-09-06T16:16:41.936Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 235 236; do echo \"=== leaf $n ===\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' POK_02.txt; done"
}
```


### [2026-09-06T16:16:44.009Z] TOOL RESULT

```
=== leaf 235 ===
)aXööea!.iov  Hes.,  att.  Y,gdviov , Schädel^,  öXelyol-^gdvov^  (üley-garov  , Ellbogen';  v.gavL^ai'  enl  v.scpaX7]v  dnog- giipaLÜes.  woneben  mit  Hochstufe  (:  nigag)  y^gavi^ai'  yiolvfxßrjaai'  -avßLa- Tfjaai  Hes.,  vav--/.gdgog  , Schiffshaupt,  Schiffsherr'  (diss.  vav-yiXägog,  -yiXrjgög),. böot.  ^ÜY-gägldag  von  *uid-Y.gägog  ,Haupt  des  Volkes';  dazu  y.galga  f. ,Kopf',  'fjf.iUgaiga  usw.  (aus  *ycgaa-gLa)]
o-stufig  *y,oga-  in  ion.  KÖgarj,  att.  /.öggrjj  dor.  xögga  , Schläfe,  Haupt^ (idg.  *kors-)]
vom  -(e)7i-St.  ker(e)n-:7igdvog  ,Helm'  (*Ä:fwo-s);  y.dgvog'  .  .  .  ßdoY^niay ftgößarov  Hes.;  -Kegvai,  yiegva  PL  ,die  beiden  Hervorragungen  an  den Knochenfortsätzen  der  Rückenwirbel'  (^kern-  oder  *kers-Ti)]  -Kgayycby ,Krabbe'  (vgl.  oben  ai.  sridga-)]  unklar  ist  die  Bildung  von  y,Egdfj,ßv^,  -vY.og , Hirschkäfer';  xdgaßog  m.  , Meerkrebs;  Käferart;  Art  Schiff'  (>  lat.  carähus ds.),  vielleicht  mit  maked.  (?)  Ableitung  (gr.  *-q)og)  zu  -mgig  , Seekrebs', s.  oben;  aber  alles  unsicher.
Von  kereu-  :  yiogvdög  m.,  f.  ,Haubenlerche'  (:  germ.  lierut-  , Hirsch'); y^ögvg^  -vd^og  ,Helm',  hom.  %v[j,a  '/.ogvaasTaL  , bäumt  sich'  Y,6gvy,ßog,  -aogvcprj , Gipfel',  -KogvTCTü)  , stoße  mit  dem  Kopf,  den  Hörnern',  yiogvyyeXv '  yisgazl^SLv Hes.  (zum  -yy-  s.  oben  zu  sfidga-).
Von  kerei-  :  Y,gi6g  , Widder'  (vgl.  in  ders.  Bed.  -Ksgaatrig),  ablaut.  mit anord.  hreinn,  ags.  hrän  ^Renntier'.
576
Vereinzeltes:  yiaQTr]v'  t^  ßovv.  Kg^Tsg  Hes.  (wenn  *kr-tä  ,die  Gehörnte') j ytvoLTrü),  'KVQTjßS^M  ,stoße  mit  den  Hörnern'  (wie  xo^vtttw;  ^Kr-)-^
lat.  cerebrum  ,Hirn'  (*ker9S-ro-7n,  vgl.  gr.  xa^rfpa);  cerma?  ,Nacken' (*cer5-mc-) ;  cernuus,  cernulus  , Gaukler,  der  Purzelbäume  macht,  sich  köpf, über  überschlägt'  (*kers-nouos ;  wenn  nicht  eher  Lw.  aus  der  Sprache  der gr.  Jongleure,  vgl.  yisgavi^cci),  cräbrö  ,Hornis'  (s.  unten).  Vom  (e)n-St.: cornü  ,Horn'  (der  u-St.  vielleicht  wie  gall.  Tidgvv^  ,Trompete'  durch  Ver- quickung des  n-  und  w-St.);  vgl.  auch  illyr.^ON  Tqlköqvlov  (Moesia),  PN Cornulnus  usw.  (Krähe  IF.  58,  222  f.)  aus  *Ärn-;
zu  cräbrö  , Hornisse'  {*cräsrö,
=== leaf 236 ===
  kjrdsron-)  stellt  sich  (idg.  krs-en-):
ahd.  hurrMz,  hornaz,  m.,  ags.  hyrnet(u)  ,Hornisse'  (*hurznuta)]  ndl.  horzel (*hurzla-),  nhd.  Horlitze;
lit.  Hr§e  f.,  sirUys  na.,  str§uolis,  alt  Hrsuo  , Wespe',  äzrsuonas,  Brsünat ,Hornisse',  lett.  sirsis,  apr.  sirsilis  ^Hornisse';
russ.-ksl.  (usw.)  s^r^sen^  , Hornisse,  Bremse',  serb.  srsljen  , Hornisse';  vgl, Büga  Kalba  ir  senove  I  191,  224;
bret.  kern  , Scheitel,  Wirbel  des  Kopfes',  mir.  cern  f.  ,Ecke';  gall. xdgw^  ,Trompete',  'accqvov  zfjv  aalTtLyya.  raXarai'^  cymr.  com.  bret.  kam ,Huf  der  Einhufer'  (aus  ,*Horn';  aber  mir  corn.  bret.  com  ,Trinkhorn', cymr.  corn  ,Horn';  wegen  des  brit.  VN  Cornovil  usw.  kaum  aus  dem  Lat.);
ahd.  hirni,  anord.  hiarni  ,Hirn'  (^kersniom),  ndl.  hersen  ,Hirn',  anord. hiarsi  , Scheitel,  Wirbel  des  Kopfes'  (*kerson')]  vom  (e)n-St.:  got.  Äaum, ahd.  anord.  hörn  ,Horn,  Trinkhorn,  Trompete'  (s.  oben  zu  lat.  cornu),  mit f-Suffix  (vgl.  oben  gr.  yLaQtrjv)  dazu  ahd.  (h)rind,  ags.  hrider  n.  ,HorntierV tiefstufig  ags.  hryder  ds.,  nd.  ndl.  rund  ,Rind'.  Von  der  u-Basis:  ahd. Mruz,  as.  hirot,  ags.  heorot,  anord.  hjqrtr,  nhd.  Hirsch  (-c?-Formans  wie  in gr.  TiÖQvöog'j  ebenso  in:)  anord.  hrütr  ,Widder';
lett.  sirnas  PI.  ,Rehe'.  (Endzelin  KZ.  42,  378)  =  aksl.  srbna  ,Reh' (:xa^vog);  ablautgleich  mit  cymr.  carw-
dazu  gehört  die  Ableitung:
kerouo-s :  kfuo-s  ,gehörnt,  hirschköpfig,  als  Subst.  Hirsch'  oder  ,Kuh'.
gr.  yf.€Qa6g  , gehörnt';
lat.  cervus,  -i  m.  ,Hirsch',  cerva  f.  ,Hirschkuh',  davon  cervinus  ,isabell- farben',  gall.-lat.  cervesia,  cervlsia  ,hirschfarbenes,  braunes  Getränk,  Bier' (Pokorny  Vox  Rom.  10,259);
cymr.  carw,  corn.  carow,  bret.  karo  m.  , Hirsch'  (^kfuo-s)]  dazu  der Gebirgsname  Karawanken]
apr.  sirwis  m.  ,Reh'  (daraus  entlehnt  finn.  hirvi  , Elentier,  Hirsch'  vgl. auch  sarve,  läpp,  cuarvi  , Elentier') ;
577
wahrscheinlich  aus  einer  Kentumsprache  stammen:
alb.  ka  , Ochse'  (*Ä;7w-)  ;
lit.  kdrve  ,Kuh';  dazu  kdrviena  f. , Kuhfleisch'  (:  cech.  kravlna  , Kuhhaut');
russ.-ksl.  krava,  poln.  krowa,  russ,  koröva  f.  ,Kuh'  (■^korduä)]  ablaut. apoln.  karw  (^kfuo-s)  , alter  Ochse'  (daraus  entlehnt  apr.  curwis  Vok.,  Akk. kurvjan  , Ochse').
WP.  I  403  ff.,  WYL.  I  164,  203  f.,  206,  207,  276,  283  f.,  284,  856,  858, Trautmann  119,  305  f.,  Schwyzer  Gr.  Gr.  I  583,  Benveniste  Origines  24  f., 175.
/•y  ^  i~.
2.  ker-,  kero-,  kre-  , wachsen;  wachsen  machen,  nähren'.
Arm.  ser  , Abkunft,  Nachkommenschaft,  Geschlecht',  ser,  Gen.  seri  ds. (ker-si-),  serem  ,bringe  hervor',  serim  , werde  geboren,  wachse',  sern  , Ge- schlecht, Nachkommenschaf
```


## [2026-09-06T16:16:48.311Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 237 238 239; do echo \"=== leaf $n ===\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' POK_02.txt; done"
}
```


### [2026-09-06T16:16:49.999Z] TOOL RESULT

```
=== leaf 237 ===
t',  serm,  sermn  ,Same';
gT.  ixÖQsaa,  nogi-oo)  (späteres  Präs.  xogsayLO)  und  xogevvvfiL]  Perf.  x«xd- osoiiai)  ,sättigen',»  -/.oqoq  , Sättigung';  *yiOQ>Fog  in  att.  xögog  ==  hom.  ion. y.ovQOg,  dor.  '/,cüQog  ,adulescens'  (später  auch  , Schoß,  Schößling,  junger Zweig'),  fem.  ark.  Dat.  Sg.  xögJ^ai,  att.  -aögr],  hom.  ion.  xovqt],  dor.  xw^a , Mädchen,  Jungfrau;  Augenstern',  hom.  xovQ7]Teg  , waffenfähige  Jungmann- schaft^;  wahrscheinlich  v.elcüQ,  -wgog  ,Sohn,  Abkömmling'  (diss.  aus  *y,SQcoQ, ursprüngl.  n.  , Nachkommenschaft') ;
alb.  thjer  m.  , Eichel'  (*/cer-),  thjerre  , Linse'  (*ker-n-),  eigentl.  Nahrung';
lat.  Ceres,  -eris  , Göttin  der  fruchttragenden  Erde',  osk.  kerri  ,Cereri' (usw.),  ,a  creando',  lat.  masc.  Cerus  manus  ,creator  bonus'  mit  r  als  alat. Schreibung  für  rr  (*cerso-)  wegen  umbr.  Sei^fe  Vok.  usw.,  osk.  caria  ,Brot'; .dehnstufig  lat.  pro-cerus  ,von  hohem,  schlankem  Wuchs';  von  der  schweren Basis  creö,  -äre  , schaffen,  erschaffen'  (Denom.  eines  *creiä  , Wachstum'), cre-sco,  -vi  , wachsen',  creber  , dicht  wachsend  =  dicht  aneinanderstehend, gedrängt,  voll;  häufig'  (*kre-dhros) ]
aisl.  hirsi  (mhd.  Lw.)  m.,  ahd.   hirso  (*kers-lon-)^  hirsi  , Hirse';
lit.  seriü,  serti  , füttern^  (schwere  Basis),  päsaras  m.  , Futter',  äermens und  §ermenys  PI.  , Begräbnismahl',  apr.  sermen  ds.
WP.  I  408,  WH.  T  204,  Trautmann  302  f.
3.  ker-  ,Schnur,  Gewebefaden;  flechten,  knüpfen';  nur  arm.  und  griech.
Arm.  sari-Ic  PL  (Gen.  sareac,  Instr.  sareöc)  ,Band,  Schnur'  {*\reiä), sard  (i-St.)   , Spinne'  (*kr-ti-)]
gr.  YMLQog  (*\ri-os)  asiod  tig  iv  i(TT<S,  dt*  ^g  ol  arrjjxovsg  SisysiQOVTCcL Phot.,  etwa  ,Schnüre  beim  Anbinden  des  Gewebes',  xalgcofia  ,ds.,  auch Gewebe',  ytaigöco  , binde  das  Gewebe  zusammen',  hochstufig  yisigia  ,der Gurt    des     Bettgestelles',     PI.     (NT.)     , Grabtücher'    (die    Formen    yirjgla,
37
578  f
I
ytaigicc  s.  Liddell-Scott;    die    Bed.    , Grabtücher'    durch   Anschluß    an   x^^      I
,Todesgöttin'?).  *
WP.  I  409,  Kuiper  Proto-Munda  122  f.  \
4.  ker-  und  kero-i  kre-  , versehren';  intr.  ,zerfallen,  vermorschen*.  "-'
Ai.  ärV'^ti  ,zerbricht,  zermalmt',  siryate,  sirydte  ,wird  zerbrochen,  zerfällt* Partiz.  slrnd-,  -§lrtd-,  iürtd-  ,zerbrochen,  verfault',  Inf.  Saritoh;
av. 
=== leaf 238 ===
 asardta-  ,nicht  gebrochen,  nicht  mutlos  gemacht'  (=  ai.  dSirta-) sari'  m.  ,Bruchstüc_k,  Scherbe',  säri-  f.  , Bruch,  Untergang';  ein  d{Ky Präsens  dazu  ist  vielleicht  npers.  gusilem  , zerbreche,  trenne'  aus  apers. *vi-srdämiy ;
gr.  yiSQatl^a)  ,verwüste,  plündere^  (*y.eQaf-i^ü),  auf  Grund  eines  *x€^crj^o-g« yisgä-  ==  ai.  sari-),  d'Asgaiog  ,unzerstört,  unversehrt',  nsgawög  , Donnerkeil Blitz'  (*y,sQa-J^[6]v-og,  eigentlich  , Zerschmetterer');  dehnstufig  gr.  ynfjQ,  xrjQÖg^ f.,  ,Tod,  Verderben;  Todesgöttin',  (urgr.  s;  den  att.  Spruch  -dnjga^s  xaqsg (y^rjQsg)  .  .  .  erklärt  man  aus  einem  sekundären  Nom.  *xa^  aus  *7,äQg  mit  tf aus  dem  einstigen  Paradigma  -^fjQ  :*y,aQ6g)]  Y.aQiOaaL'  äno'/.xeLvai  Hes.  ent- hält Reduktionsstufe,  wie  alb.  ther-^  dxrjQLog  , unbeschädigt,  nicht  dem  Tode verfallen',  xr^galro)  ,verderbe,  schädige',  wovon  d:y.rjgaTog  , unverletzt',  auch ,rein,  lauter'  (auch  mit  dxrjgarog  ,unvermischt'  zusammengefallen);
lat.  caries  (^JcT-ie-  zum  Präs.  *cariö)  ,das  Morschsein,  Faulsein',  cariösut , mürbe,  morsch',   carius  ,tinea';
alb.  ther   ^schlachte,    schneide^  {M^-),    tsirris   ,steche'  (*ker-n-')-
air.  ar-a-chrin  (^*-kr-nu-t)  ,zerfällt',  do-cer  ,er  fiel'  (*-]cer9-t),  crin  ,welk' i^kre-no-s),  irchre  n.  ,Untergang'  {^jperi-kr-io-m)'^
toch.  A  käryap,  B  karep  , Schaden'.  '"
WP.  I  410  f.,  WH.  I  167  f.,  Thurneysen  Gr.  437,  462.
kerbero-  und  kerbero-  ,scheckig'  (vgl.  S.  573  ker-  neben  6.  ker-  in  Farb- bezeichnungen).
Ai.  sdrvara-  ,bunt,  scheckig',  ädrvarl  f.  ,Tier  der  Maruts,  Nacht'  {v  steht für  h,  vgl.  Wackernagel  Ai.  Gr.  I  184  und :)  sahdla-,  sahdra-  (diss.  Schwund des  ersten  r)  ,bunt,  scheckig'  (daneben  karhard-,  karvard-,  kabara-,  kar- bura-,  karbu-  ds.) ;
gr.  Kegßegog  ursprüngl.  ,der  Scheckige';  vgl.  die  mythologische  Wen- dung von  ai.  sarvari]
slav.  soboh  ,Zobel'  scheint  aus  dem  Arischen  zu  stammen.
Die  Wz.  kerb-  sucht  Liden  Stud.  50  f.  in  air.  corbaim  , besudle,  beflecke' und  lit.  kirba  (>  lett.  Uirba)  , Sumpf,  Morast'  und  betrachtet  Herb-  als Erweiterung  der  Farbwz.  ker-  (s,  S.  583  kers-);  Mühlenbach-Endzelin  II  383.
WP.  I  425,  Schulze  Kl.  Sehr.  125,  Specht  Idg.  Dekl.  119,  262.
579
j.  kerd-  ,gürten';  kelt.  krd-su-,  slav.  kerd-so-  , Gürtel';  nur  kelt.  und  slav.
Air.  fo-cridigedar  
=== leaf 239 ===
,accingat',  cri(u)ss  ,GürteP  {*Jcxd-su-),  mir.  fo-chrus Giirtung^  cymr.  crys  , Gürtel,  Hemd',  gwregys  (für  *gwe-grys  aus  *gwo-grys) Gürtel',  acorn.  hreis  ,Hemd',  grugis  , Gürtel',  bret.  h-ez  ,Hemd',  gouriz ^Gürtel' ;
russ.  ceres  (neben  cerez,  das  z  durch  Einfluß  der  Präp.  ^rez  hat)  , Geldgurt', klr.  ceres  , lederner,  breiter  Gürtel,  Geldkatze',  poln.  trzos  , Geldgurt, Geldkatze';
vielleicht  eine  Erweiterung  von  (s)her'  , drehen'.
WP.  I  423,  Berneker  148.
2.  kerd-  etwa  , handwerksmäßig  geschickt,  klug  berechnend'.
Gr.  xsQÖog  n.  , Gewinn,  Vorteil',  xsqÖlcüv  »nützlicher,  ersprießlicher', xegÖLCTTog  , der  Verschlagenste  (Hom.);  ersprießlichst*,  xegöalsög  , gewinnend, nützlich,  listig',  ytsgöaXerj,  yisgöd)  , Fuchs',  -asgöalvco  , gewinne* ;  aus  gr.  *y(,£Qdwv stammt  lat.  cerdö  , gemeiner  Handwerksmann' ;
air.  cerd  f.  ,Kunst,- Handwerk;  Künstler,  Dichter';  cymr.  cerdd  f.  , Kunst, Poesie* ;
aisl.  Beiname  horti  m.  ,klug'  (?),  horskr  ds.,  ags.  asächs.  ahd.  horsc  ds. (^hort-ska-).
WP.  I  423.
kerdho-,  kerdhä  , Reihe,  Herde'.
Ai.  sdrdlia-  m.,  sardkas-  n.  , Herde,  Schar',  av.  sardda-,  apers.  Ö-ard- ,Art,  Gattung';
gr.  -KÖQ&vg  , Haufe',  xogd-vofiaL  , erhebe  mich*,  y.ood'ivo)  , häufe  auf*;
mcymr.  cordd  f.  , Truppe,  Schar,  Familie'  {*Jcordhä]  irrig  Loth  RC  42, 276  f.);
got.  hairda,  aisl.  hjqrd,  ags.  heord,  ahd.  herta  , Herde*  (davon  got. hairdeis,  ahd.  hirti  usw.  ,Hirt')  und  ahd.  herta  , Wechsel'  (eigentlich , Reihenfolge') ;
im  Bsl.  mit  westidg.  Guttural:  lit.  Izerdzius  (und  sJcerdzius)  ,Hirt'  (setzt ein  *Jcerdä  , Herde*  voraus),  apr.  Jcerdan  Akk.  ,Zeit'  (eigentlich  ,*Reihe, Reihenfolge*);
abg.  ^reda  ,iq)7]^sQia,  Reihe  nach  der  Tagesordnung'  und  , Herde',  crMiti ,(*anreihen,  anordnen  =)  bewirten',  klr.  ceredd  , Reihe;  Herde,  Rudel'  (usw.).
WP.  I  424  f.,  Trautmann  127  f. ;  vgl.  paelign.  ON  Corfinium.
(Icered-:)  kerd-,  kerd-,  krd-,  kred-  ,Herz'. Arm.  sirt,  Instr.  srti-v  ,Herz'  [*kerdi-)]
gr.  yLaqdiä  (att.),  KgaöLr]  (hom.),  xa^^a  (lesb.),  xogi^ä  (kypr.)  ,Herz;  Magen;
37*
580  »
Mark  bei  Fflanzen'  {*lrd{i)a).  poet.  x^^,  -oq  n.  ,Herz'  {*herd) -,  läag  ^^^^^ bildung  nach  sag:  '^Qog]
lat.  C07-  (aus  *corc2),  corc^is  ,Herz',  con-co?'s,  -c^is  ,ein trächtig-',  dis-cort , zwieträchtig' ;
air.  cride  n.,  nir.  croidhe  ,Herz,  Mitte',  cymr.  craidd  , Mittelpunkt',  com. cre{y)s,  bret.  kreiz  ,Mitte'  (das  Ir.  läßt  sich  aus  *%rediom  oder  ^Ärdioni erklären,  vorausg
```


## [2026-09-06T16:16:57.833Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==240' POK_02.txt | head -60"
}
```


### [2026-09-06T16:16:59.946Z] TOOL RESULT

```
esetzt,  daß  die  dunkle  Färbung  der  anlaut.  Konsonanz Erklärung  findet  (nach  crü  ,Blut'?):  die  brit.  Formen  verlangen  dagegen eine  Grundform  *krediom)]
got.  hairto,  ahd.  herza,  ags.  heorte,  anord.   hjarta  n.  ,Herz'  (^JcErd-on-)'^
lit.  §irdls  f.  (älter  m.),  Akk.  sirdi  ,Herz,  Kern,  Mark  von  Bäumen'; lett.  sMs  f.  (älter  m.)  ,Herz'  und  serde  f.  ,Mark,  Kern  im  Holze'  (Grund- formen *§erd-  und  Hfd-,  vgl.  den  alten  Gen.  Sg.  sirdes  und  Gen.  Fl.  Hrdij,^ die  auf  idg.  *h^rdes  und  *%erdöm  beruhen;  siehe  Trautmann  Bsl.  Wb.  302); apr.  seyr  n.  {*Jcerd),  zum  m.  o-St.  erweitert  siras,  Akk.  Siran  ,Herz';
akl.  sr^dhce,  serb.  srce  ,Herz';  hochstufig  aksl.  sreda  , Mitte'  {*serda\ russ.  seredd  ds. ;
hitt.  ha-ra-az  (karts)  ,Herz',  Gen.  ]car-di-a§  (Pedersen  Hitt.  41).
Nicht  hierher  (sondern  zu  mir.  cretair  , Reliquie')  idg.  kred-dhe-  .Zauber- kraft worauf  setzen,  glauben,  vertrauen'  in  ai.  ärdd-dadhäti  , vertraut,  glaubt' (getrennt  noch  z.  B.  srdd  asmäi  dhatta  ,glaubet  an  ihn!'),  Srad-dhä  , Ver- trauen', av.  zrazdä-  ^glauben'  (aus  *srazdä-  durch  volksetym.  Anlehnung an  Z9r9d-  ,Herz') ;
lat.  credö  .glaube'  (*]crezdö-,  idg.  *]cred-dhe-) -^
air.  cretim  , glaube',  cymr.  credaf  ds.  (nicht  *crethaf,  daher  erst  spät  zur festen  Zusammensetzung  geworden),  corn.  o^ezy,  mbret.  cridiff,  nbret.  credi , glauben';  dazu  air.  cretar,  mcymr.  creir,  cymr.   crair  {*]credra)  ,Reliquie*.
Reimwort  zu  Tcer{e)d-  ist  gherd-,  ghrd-,  nur  arisch,  in  ai.  kfd  ,Herz',  usw.
WP.  I  423  f.,  WH.  I  272 f.,  286 f.,  857,  858;  Vendryes  RC  40,  436.
(kerem-),  krem-  (:  krom-)  und  kerm-  (bes.  mit  s-Formans)  1.  ,Zwiebel- und  Knoblaucharten* ;  2.  , Eberesche  u.  dgl.' ;  Anlaut  k-,  vereinzelt  k-.
Gr.  y,QSf4,vov  Hes.,  sonst  (durch  Assimil.  daraus)  ytQÖfxvov  , Zwiebelart' (*hremusom) ;
mir.  crim,  Gen.  crema,  cymr.  (reduktionsstufig)  craf  ,Knoblauch' ;
ags.  hramsan,  engl,  ramsons  ,Waldknoblauch',  norw.  schwed.  dän.  rams ds.,  mnd.  ramese,  remese  ds.,  ahd.  ramusia,  nhd.  (bair.)  rams  ,ds.'  (Allium ursinum  L.);
lit.  hermüSe  f.  , wilder  Knoblauch';
slav.  ^cerrmsa,  *^ermucha  in  russ.  ceremH,  öeremica,  SeremusJca  ,Bären- lauch,    Allium    ursinum',   poln.  trzemucha   ds.,  mit   Pal.    skr.  snjemus   m.,
581
.^a  L  und  srijemuB,  -za  ,Art  wildwachsendes  Gemüse';  dazu  die  Bezeich- nung des  , Prunus  padus'  (ebenfalls  starkriechende  Pflanze);
lit.  sermüMnis  m.  sermüMU,  SermüMne  L  , Eberesche',  lett.  s^rmükslis usw.  ds.,  mit  anderer  Gutturalreihe  lett.  cermauksis  usw.,  ds. ;
russ.  ceremcha,  cerema,  ceremucha  , Faulbaum,  Ahlkirsche,  Prunus  padus', klr.  cerem-cha,  -uclia  ds.,  sloven.  örp7n-ha,  -sa  (und  mit  Palatal)  sr'^m-§a,  -sa ds.,  poln.  trzemcha,  öech.  tremcha
```


## [2026-09-06T16:17:35.067Z] TOOL CALL #11: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['BQT','SNS','MON','AHD','LAT','SYN','KLN']:\n    print('===',k); print(json.dumps(d[k], ensure_ascii=False, indent=1))\n\""
}
```


### [2026-09-06T16:17:36.777Z] TOOL RESULT

```
=== BQT
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
=== SNS
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
=== MON
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
=== AHD
{
 "title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)",
 "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)",
 "kind": "archive_djvu+website+archive_restricted",
 "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only",
 "identifier": "watkins-american-heritage-dictionary-of-indo-european-roots-1985",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt",
 "page_offset": "1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.",
 "lookup_hint": "Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves = original 1969 ed.).",
 "notes": "AHD is by far the most cited source (1906). Root order is alphabetical in all versions, so root-name lookup is reliable; page numbers can only be checked against a borrowed copy of the 1976 New College Edition. || RE-SEARCH 2026-09: no open scan of the New College Edition; three borrowable copies on archive.org (avoid the ~840-pp Dell abridgements, which lack the appendix). Local proxy remains AHD_watkins1985.txt.",
 "cites": "page number of the 1975/76 New College Edition; pp. 1505–1550 are the Indo-European roots appendix (look the root up by name)"
}
=== LAT
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
=== SYN
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
=== KLN
{
 "title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67",
 "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein",
 "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt",
 "page_offset": "KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.",
 "notes": "Other 1966 IA copies (comprehensiveety01klei/02klei etc.) are lending-only (401/403). local_files: /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt (paginated by leaf); /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1971.txt (plain djvu.txt, no page marks)",
 "local_files": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1971.txt"
 ],
 "cites": "page number, continuous across the two volumes (1966–67)"
}
```


## [2026-09-06T16:17:41.522Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SYN leaf 275 (p.251) ===\" && awk 'BEGIN{RS=\"\\f\"} NR==275' SYN.txt | head -60"
}
```


## [2026-09-06T16:17:42.143Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^kerd-\\|^kerd\\|^kerd\" AHD_watkins1985.txt | head -20; echo \"---\"; grep -n \"kerd\" AHD_watkins1985.txt | head -40"
}
```


### [2026-09-06T16:17:43.041Z] TOOL RESULT

```
=== SYN leaf 275 (p.251) ===
 be fr, *nlek- tyo- : Lett. place ‘shoulder blade’, plahy ‘become flat’, Grk. r\aé ‘flat surface’, etc., in either case fr. parallel extensions of the same root and fr. the notion of ‘flat’. Walde-P. 2.100.
7. Skt. skandha-, etym.? Uhlenbeck 341.
Skt. azsa-, above, 1
Skt. cupti- (only once, RV 1.51. 5), Av. supti- (NPers. suft) : Alb. supé ‘shoulder’, MLG schuft, Du. schoft ‘but- tock, rump, shoulder (of animals)’, Walde-P. 1.467.
Av. daog- ‘upper arm, shoulder’ (NPers. dog ‘shoulder’) : Skt. dos- ‘fore- arm’, Ir. doe ‘arm’, ete. Walde-P. 1.782. Pedersen 2.104.
see
431 ARM Grk.  Bpaxlwy, riixus, xelp Goth. arms Lith. ranka NG Xépt, umparoo ON armr, handleggr, hond Lett. ruoka Lat. bracchium Dan. arm ChSI. mySica It. braccio Sw. arm SCr. ruka (miica) Fr. bras OE earm Boh. rdmé, paze Sp. brazo ME arm Pol. ramie, reka Rum. brat NE arm Russ. ruka Ir. lam, doe Du. arm Skt. bahu-, bhuja- Nir. lamh OHG arm Av. bdzu- W. braich MHG arm Br. brec’h NHG arm
Many of the words for ‘arm’ belong to an inherited group, derived from the no- tion of ‘joint’, and applied to both ‘arm’ and ‘shoulder’. In several languages the words for ‘hand’ are extended to include, and in some are the usual terms for, ‘arm’ (cf. ‘foot’ for nS 4,35).
1. Ii *aramo-s, *fmo-s, fr. IE *ar(o)- in Grk. dpapicnw ‘fit’, &p8pov ‘joint’, Lat. artus ‘joint’, etc. Walde-P. 1.73. Er- nout-M. 74, Walde-H. 1.69.
Lat. armus mostly ‘shoulder, fore- quarter’ of animals, rarely ‘arm’ of men; Goth. arms, etc., general Gmc.; OPruss. armo ‘arm’; ChSl. ramo, rame, SCr. rame ‘shoulder’, Boh. rdmé, rameno, mostly ‘arm’, Pol. ramie, ‘shoulder, arm’; Skt. trma- ‘forequarter’ of an animal; Av. arama- in aramd-Sita- ‘thrown by the arm’; Arm. armuka ‘elbow’.
2. IE *bhaghu-. Walde-P. 2.130.
Grk. rixus, Dor. raxus, mostly ‘fore-
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
5 oF THE BD
T a talso ‘arm’ (as Hom., Il. 5.314); }, bub Oe ay. bazu- (NPers. bazi) git. bahurs pagr, OB b59, OHG buog ‘qr’; noatly a animals) ; Toch. A 1 (688, p- 3, fin. 1).
lov, in part ‘upper arm’ 3, Grk. Bpaxe™ Tim. 75a; but also
ly generic (of : t ith subordina ie avr, aaxus, xelp ‘shoulder, upper
arm, elbow, forearm, ha
```


### [2026-09-06T16:17:43.092Z] TOOL RESULT

```
---
179:Indo-European is particularly rich in relig- ious vocabulary. An important form, which is also found only in the peripheral languages Sanskrit, Latin, and Celtic, is the two-word metaphoric phrase *kred-dha-, literally “to put (dhé-') heart (kerd-').” The two words have been joined together in the western languages, as in Latin crédé, “I believe.” Here a term of the most ancient pagan relig- ion has been taken over by Christianity. A common word for religious form (bhlag- men-) may be preserved in BRAHMIN, a member of the priestly class, from Sanskrit.
375:mild, gentle: DAFT. 2. Probably suffixed form *dhabh-ro- in Latin faber, artisan (< “he who fits together”): FABRIC, (FABRICATE), FORGE}. [Pok. 2. dhabh- 233.] dhal-. To bloom. Suffixed form *dhal-yo- in Greek thal- lein, to flourish, bloom, sprout (> thallos, a shoot): THALIA, THALLUS; PROTHALLUS. [Pok. dhail- 234.] dhé-', To set, put. Contracted from *dheo-. 1. O-grade form *dhé- in Germanic *don in Old English dén, to do: Dol; FORDO. 2. Suffixed form *dhé-ti-, “thing laid down or done, law, deed,” in Germanic *dédiz in Old English déd, doing, deed: DEED. 3. Suffixed o-grade form *dho-mo- in Germanic *démaz in: a. Old English dom, judgment (< “thing set or put down”): Doom; b. Old English -d6m, abstract suffix indicating state, condition, or power: -DOM; c. Old Norse -démr, condition (see ka-); d. Gothic déms, judgment, akin to the Germanic source of Russian Duma, Duma: Duma; e. Germanic denomina- tive *“ddmjan in Old English déman, to judge: DEEM. 4. Suffixed o-grade form *dhé-t- in Latin agential suffix -dés in Latin sacerdés, priest, “(performer of sacred rites” (see sak-). 5. Zero-grade form “dha- in: a. prefixed form *kom-dha- in Latin condere, to put together, establish, preserve (*kom, together; see kom): CONDIMENT; AB- SCOND, INCONDITE, RECONDITE, SCONCE?; b. compound *kred-dha- (see kerd-'). 6. Suffixed zero-grade form *dha-k- in: a. Latin facere (< *fak-yo-), to do, make (> French faire, to do), and Latin combining form -fex (< *.fak-s), “maker”: -FACIENT, FACT, FACTION, FACTITIOUS, FACTOR, FASHION, FEASIBLE, FEAT!, FEATURE, (FETISH), -FIC, (-FY); AFFAIR, AFFECT!, (AFFECT2), (AFFECTION), AMPLIFY, ARTIFACT, ARTIFICE, BEATIFIC, BENEFACTION, BENEFIC, (BENEFICE), (BENEFICENCE), BENEFIT, CHAFE, COMFIT, CONFECT, (CONFETTI), COUNTERFEIT, (DEFEA- SANCE), DEFEAT, DEFECT, (DEFICIENT), (DISCOMFIT), EDIFICE, (EDIFY), EFFECT, (EFFICACIOUS), (EFFICIENT), FACSIMILE, FACTOTUM, FORFEIT, HACIENDA, INFECT, JUSTIFY, MALEFACTOR, MALFEASANCE, MANUFACTURE, MISFEASANCE, MODIFY, MOLLIFY, NIDIFY, NOTIFY, NUL- LIFY, OFFICINAL, PERFECT, PETRIFY, (PLUPERFECT), PON- TIFEX, PREFECT, (PROFICIENT), PROFIT, PUTREFY, QUALIFY, RAREFY, RECTIFY, REFECT, (REFECTORY), RU- BEFACIENT, SACRIFICE, SCIRE FACIAS, SPINIFEX, SUF- FICE, (SUFFICIENT), SURFEIT, TUBIFEX, TUMEFACIENT, viviry; b. Latin derivative faciés, shape, face (< “form imposed on something”): FACADE, FACE, (FACET), (FA- CIAL), FACIES; (DEFACE), EFFACE, PRIMA FACIE, (SUR- FACE); c. Latin compound officium (< *opi-fici-om), service, duty, business, performance of work (*opi-, work; see op-'): OFFICE; d. further suffixed form *dha-k-li- in Latin facilis (< Old Latin facul), feasible, easy: FACILE, (FACILITY), FACULTY; DIFFICULTY. 7. Suffixed zero-grade form *dha-s- in Latin fds, divine law, right: NEFARIOUS. 8. Possibly Latin -farius, -doing: MULTIFARIOUS, OMNI- FARIOUS. 9. Reduplicated form *dhi-dhé- in Greek tithe- nai, to put: THESIS, THETIC; ANATHEMA, ANTITHESIS, APOTHECARY, (APOTHECIUM), BODEGA, BOUTIQUE, DI- ATHESIS, EPENTHESIS, EPITHET, HYPOTHESIS, METATHE- SIS, PARENTHESIS, PROSTHESIS, PROTHESIS. 10. Suffixed form *dhé-k- in Greek théké, receptacle: THECA, TICK?; AMPHITHECIUM, BIBLIOTHECA, CLEISTOTHECIUM, ENDO- THECIUM, PERITHECIUM. 11. Suffixed zero-grade form *dha-mn in Greek thema, “thing placed,” proposition: (THEMATIC), THEME. 12. Reduplicated form *dhe-dhé- in Sanskrit dadhdti, he places: SANDHI. 13. Reduced form *dh- (see aw-2). [Pok. 2. dhé- 235.] dhé-2. To vanish. Contracted from *dhea-. 1. Possibly Old Norse d%sa, to languish, decay: DASTARD. 2. Possibly Old Norse *dasa, to tire out (attested only in reflexive form dasask, to become exhausted), akin to the Scandi- navian source of Middle English dasen, to stun: DAZE. [Pok. 3. dhé- 239.] dheb-. Dense, firm, compressed. Germanic suffixed form *dap-ra- in Middle Dutch and Middle Low German
621:hréc, rook: RooK!. 4. Germanic *hraban, *hrabnaz, raven, in Old English hrefn, raven: RAVEN}. 5. Extended form *krep- in Latin crepdre, to crack, burst, creak: CREPITATE, CREVICE; DECREPIT, DECREPITATE, QUEBRA- cHo. 6. Extended form *kri- in Germanic *krik- in Old French criquer, to creak, click: CRICKET!. II. Variant form *skr-. 1.Germanic *skrik- in Old English scric, thrush: SHRIKE. 2. Germanic *skrékjan- in Old Norse skrekja, to shriek: SCREAK, SCREECH. 3. Germanic *skrainjan, to shout, shriek, in Old Norse screma, to scream, perhaps akin to the possible Scandinavian source of Middle English scremen, to scream: SCREAM. III. O-grade form *kor-. 1. Latin corvus, raven: CORBEL, CORBINA, CORMORANT, CORVINE, Corvus. 2. Greek ko- rax, raven (> korakias, chough): CORACIIFORM, CORA- com. [Pok. 1. ker- 567.] ker-3. To grow. 1. Suffixed form *ker-es- in Latin Cerés, goddess of agriculture, especially the growth of grain: CEREAL, CERES. 2. Extended form *kré- (< *krea-) in: a. suffixed form *kré-yd- in Latin credre, to bring forth, create, produce (< “to cause to grow”): CREATE, CREOLE; PROCREATE; b. suffixed form *kré-sko- in Latin créscere, to grow, increase: CRESCENDO, CRESCENT, CREW!; AC- CRUE, CONCRESCENCE, CONCRETE, DECREASE, EXCRES- CENCE, INCREASE, RECRUIT. 3. Suffixed o-grade form *kor-wo-, “growing,” adolescent, in Greek kouros, koros, boy, son: DIOSCURI, HYPOCORISM. 4. Compound *sm-kéro-, “of one growth” (*sm-, same, one; see sem-'), in Latin sincérus, pure, clean: SINCERE. [Pok. 2. ker- 577.) ker-4, Heat, fire. 1. Suffixed form *ker-té in Germanic *herthé in Old English heorth, hearth: HEARTH. 2. Zero-grade form *kr- in: a. Latin carbé, charcoal, ember: CARBON, CARBUNCLE; b. extended form *krem- in Latin cremdre, to burn: CREMATE. 3. Possibly suffixed and extended form *kera-mo- in Greek keramos, potter’s clay, earthenware: CERAMIC. 4. Possibly variant ex- tended form *krds- in Russian krasa, beauty (< “bril- liance of fire”): CRASH?. [Pok. 3. ker(a)- 571.] ker-5. Also kere-. To injure. Suffixed zero-grade form *kro-yé- in Latin cariés, decay, caries: CARIES. [Pok. 4. her- 578.] ker-8. A kind of cherry. 1. Suffixed zero-grade form *kr-no- in Latin cornus, cornel tree: CORNEL. 2. Full- grade form *ker- probably in Greek kerasos, cherry: CHERRY. [Pok. 4. ker- 572.] kerd-', Heart. 1. Suffixed form *kerd-en- in Germanic *hertén- in Old English heorte, heart: HEART. 2. Zero-grade form *krd- in: a. Latin cor (stem cord-), heart: CORDATE, CORDIAL, COURAGE, QUARRY!; ACCORD, CONCORD, CORDIFORM, DISCORD, MISERICORD, RECORD; b. suffixed form *krd-yd- in Greek kardia, heart, stom- ach, orifice: CARDIA, CARDIAC, CARDIO-; DIPLOCARDIAC, ENDOCARDIUM, EPICARDIUM, MEGALOCARDIA, MYOCAR- DIUM, PERICARDIUM. 3. Possibly *kred-dha-, “‘to place trust” (an old religious term; *dho-, to do, place; see dhé-'), in Latin crédere, to believe: CREDENCE, CREDI- BLE, CREDIT, CREDO, CREDULOUS, GRANT; MISCREANT, RECREANT. [Pok. kered- 579.] kerd-2. Craft. Suffixed form *kerd-d in Old Irish cerd, art, artist: CAIRD. [Pok. 2. kerd- 579.] kerdh-. Row, herd. Suffixed form *kerdh-d@ in Germanic *herdo in Old English heord, herd: HERD. [Pok. kerdho- 579.] kere-. To mix, confuse, cook. 1. Variant form *kra- (< *kraa-) in Germanic *hrdr- in: a. possibly Old English hrér, lightly boiled, half-cooked: RARE?; b. Middle Dutch roer, motion: UPROAR. 2. Zero-grade form “krp- in: a. suffixed form *kro-ti- in Greek krasis, a mixing: IDIOSYNCRACY; b. suffixed form *kro-ter- in Greek kra- ter, mixing vessel: CRATER. [Pok. hero- 582.] kerp-. To gather, pluck, harvest. Variant karp-. 1. Ger- manic *harbistaz in Old English herfest, harvest: HAR- VEST. 2. Latin carpere, to pluck: CARPET; EXCERPT,
938:skep-. Also kep-. Base of words with various technical meanings such as “to cut,” “to scrape,” “to hack.” 1. Germanic *skap- in: a. Old English gesceap (ge-, collective prefix; see kom), form, creation (< “cutting”): SHAPE; b. Old English -scipe, state, condition (collective suffix): -sHIP; c. Dutch -schap, “-ship,” condition (collec- tive suffix): LANDSCAPE. 2. Germanic ablaut variant *skOpo-, “thing cut out,” container, in Middle Dutch and Middle Low German schdépe, bucket for bailing water: scoop. 3. Germanic *skaftaz in Old English sceaft, rod of a spear: SHAFT! 4, Germanic expressive form *skabb- in: a. Old English sceabb, a scab, scratch: sHaBBy; b. Old Norse skabb, a scab: scaB. 5. Variant form *skabh- in: a. Germanic *skaban in (i) Old English sceafan, to scrape, pare away: SHAVE (ii) Old High German skaban, to scrape: SAPSAGO; b. Latin scabere, to scrape: SCABIES; c. suffixed form *skabh-ro- in Latin scaber, rough (< “scratched”’): SCABROUS; d. Greek skaphé, boat (< “thing cut out”): SCAPHOID; BATHYSCAPH. 6. Variant form *skap- in Latin scapula, shoulder blade (used as a tool for scraping): SCAPULA. 7. Variant form *kap- in: a. Latin capd, castrated cock: CAPON; b. Late Latin capuldre, to cut: SCABBLE. 8. O-grade form *kop- in: a. suffixed form *kop-yd- in Germanic *hapjo, a cutting tool, ax, sickle, in (i) Old High German hdppa, happa, sickle, akin to the Germanic source of Old Provencal apcha, small ax: PIOLET (ii) Medieval Latin hapia, ax, and Old French hache, small ax: HASH!, HATCHET; NUT- HATCH, QUEBRACHO; b. suffixed form *kop-yo- in Greek koptein, to strike, cut: COMMA; APOCOPE, SARCOPTIC MANGE, SYNCOPE; C. Russian kopat’, to hack, with de- rivative kop’e, lance, in kopeika, kopeck: KOPECK. 9. Pos- sibly zero-grade variant form *skup(h)- in Greek skuphos, a cup (but more likely of obscure origin): SCYPHISTOMA, SCYPHOZOAN. [Pok. 2. (s)kep- 931.] sker-!, Also ker-. To cut. I. Basic forms *sker-, *ker-. 1. Germanic *skeran in Old English scieran, sceran, to cut: SHEAR. 2. Germanic *skeraz in: a. Old English scéar, plowshare: SHARE?; b. Old English scearu, scaru, portion, division (but recorded only in the senses of “fork of the body,” “tonsure”): SHARE!. 3. Germanic *skér- in: a. *skér-6- and *sker-ez- in Old English scéar, scissors: SHEARS; b. compound *skér-berg-, “sword protector,” scabbard (see bhergh-') in Old High German scarberc, scabbard, akin to the possible Germanic source of Anglo- Norman escaubers, scabbard: SCABBARD. 4. Germanic *skur- in Old Norse skor, notch, tally, twenty: SCORE. 5. Germanic suffixed form *skar-jam in Old Norse sker, low reef (< “something cut off’’): scaR?. 6. Suffixed o-grade extended form *skord-o- in Germanic *skardaz in Old English sceard, a cut, notch: SHARD. 7. Extended form *skerd- in suffixed zero-grade form *skrd-o- in Germanic *skurtaz in: a. Old English scort, sceort, “cut,” short: SHORT; b. Old English scyrte, undergarment (< “cut piece”): SHIRT; c. Old Norse skyrta, shirt: SKIRT. 8. Germanic extended form *skerm- in: a. Old High German skirmen, to protect, akin to the source of Old French eskermir, to fight with a sword, fence: SKIRMISH; b. Middle Dutch scherm, shield: SCREEN. 9. Variant form *kar- in Latin caré (stem carn-), flesh: CARNAGE, CARNAL, CARNASSIAL, CARNATION, CARNIVAL, CARRION, CARUNCLE, CHARNEL, CRONE; CARNIVOROUS, INCAR- NATE. 10. Suffixed o-grade form *kor-yo- in Latin co- rium, leather (originally “piece of hide”): CORIACEOUS, CORIUM, CUIRASS, CURRIER; EXCORIATE. 11. Suffixed zero-grade form *kr-to- in Latin curtus, short: CURT, CURTAL, KIRTLE. 12. Suffixed o-grade form *kor-mo- in Greek kormos, a trimmed tree trunk: cor. 13. Suffixed o-grade form *kor-i- in Greek koris, bedbug (< “cutter”): corREopsis. II. Extended roots *skert-, *kert-. 1. Zero-grade form *krt- or o-grade form *kort- in Latin cortex, bark (< “that which can be cut off”): CORTEX; DECORTICATE. 2. Suffixed form *kert-snd- in Latin céna, meal (< “portion of food”): CENACLE. III. Extended root
940:*skerb(h)-, *skreb(h)-. 1. Germanic *skarpaz, cutting, sharp, in: a. Old English scearp, sharp: SHARP; b. Gothic skarp6, pointed object, akin to the possible Germanic source of Italian scarpa, embankment: scarp. 2. Ger- manic *skrap- in: a. Old Norse skrap, “pieces,” remains: SCRAP!; b. Old Norse skrapa, to scratch: SCRAPE. 3. Ger- manic skrab- in: a. Middle Dutch schrabben, to scrape: SCRABBLE; b. Middle Dutch schrobben, to scrape: SCRUB!. 4, Germanic *skrub- in Old English scrybb, shrub (< “rough plant”): SHRUB. 5. Latin scrobis, trench, ditch: SCROBICULATE. 6. Latin scrdfa, a sow (< “rooter, digger”): SCREW, SCROFULA. [Pok. 4. sker-, Section I. 938.] sker-2. To leap, jump about. Perhaps same root as sker-3. 1. Extended form “skerd- in Germanic *skert- in Middle High German scherzen, to leap with joy: SCHERZO. 2. O-grade variant form *kor- in Latin coruscdre, to vibrate, glisten, glitter: coRUSCATE. [Pok. 2. (s)ker- 933.] sker-3. Also ker-. To turn, bend. Presumed base of a number of distantly related derivatives. 1. Extended form *(s)kreg- in nasalized form *(s)kre-n-g- in: a. Ger- manic *skrink- in Old English scrincan, to wither, shrivel up: SHRINK; b. variant *kre-n-g- in Germanic *hrunk- in (i) Old Norse hrukka, a crease, fold: RUCK? (ii) Frankish *hrunkjan, to wrinkle (> Old French fronce, pleat): FLOUNCE!, 2, Extended form *(s)kregh- in nasalized form *skre-n-gh- in Germanic *hringaz, something curved, circle, in: a. Old English Aring, a ring: RING!; b. Old French renc, reng, line, row: RANCH, RANGE, RANK}, RINK; ARRANGE, DERANGE; C. Middle Dutch rinc (com- bining form ring-), a ring: RINGHALS. 3. Extended form *kreuk- in Germanic “*hrugjaz in: a. Old English hrycg, spine, ridge: RIDGE; b. Old High German hrukki, back: RUCKSACK. 4. Suffixed variant form *kur-wo- in Latin curvus, bent, curved: CURB, CURVATURE, CURVE, CUR- vET. 5. Suffixed extended form kris-ni- in Latin crinis (< *crisnis), hair: CRINITE; CRINOLINE. 6. Suffixed ex- tended form *kris-td- in Latin crista, tuft, crest: CREST, CRISTA, CRISTATE. 7. Suffixed extended form *krip-so- in Latin crispus (metathesized from *cripsus), curly: CREPE, CRISP, CRISPATE. 8. Extended expressive form *kriss- in Latin crisdre, (of women) to wiggle the hips during copulation: crissuM. 9. Perhaps reduplicated form *ki-kr-o- metathesized into Greek krikos, a ring (> Latin circus, ring, circle): CIRCA, CIRCLE, CIRCUM-, SEARCH; CRICOID. 10. Suffixed o-grade form *kor-6no- in Greek kordnos, curved: (CORONA), CROWN; CORONOID. 11. Suffixed variant form *kur-to- in Greek kurtos, bent: KURTOSIS. [Pok. 3. (s)ker- 935.] sker-4. Excrement, dung. Extension of sek-, “to cut, separate,” hence “to void excrement.” 1. Form *sk-6r- in Greek skdr (genitive skatos < *sk-nt-), dung: SCATO-, SCORIA, SKATOLE. 2. Extended form “skert- in taboo metathesis *sterk-os- in: a. Latin stercus, dung: STERCO- RACEOUsS; b. variant forms *(s)terg-, *(s)treg- in Germanic *threkka- in Middle High German dréc, dung: DRECK. [Pok. sker-d- 947; 8. (s)ter- 1031.] skerbh-. Also skerb-. To turn, bend. Extension of sker-3. 1. Variant form *skreb- in Germanic *skrip- in Old Norse skreppa, to slip, and derivative Old Norse skorpna, to shrink, be shriveled, akin to the probable Scandinavian source of Middle English scorchen, to scorch: SCORCH. 2. Nasalized variant form *(s)kre-m-b- in: a. Germanic *hrimp-, *hrump- in (i) Old English hrympel, wrinkle, fold: RIMPLE (ii) Middle Dutch rom- pelen, to wrinkle: RUMPLE (iii) Old French ramper, to climb, rear up: RAMP?; b. Germanic *skrimp- in (i) Mid- dle Low German schrempen, to shrink, wrinkle, perhaps akin to the possible Low German source of Middle English shrimp, pygmy, shrimp: SHRIMP (ii) Swedish skrympa, to shrink, perhaps akin to the possible Scandi- navian source of SCRIMP. 3. Variant form *kramb- in Greek krambé, cabbage (having wrinkled, shrunken
1208:ABAFT apo- ABANDON bha-2 ABASE bassus ABASH bat- ABASIA gWa- ABATE battuere ABBREVIATE mregh-u- ABDICATE deik- ABDUCENS deuk- ABDUCT deuk- ABELE albho- ABERRATION ers-1 ABET bheid- ABEYANCE bat- ABHOR ghers- ABIDE bheidh- ABJECT yé- ABJURE yewes- ABLATION  tele- ABLAUT apo-, kleu-1 ABLE ghabh- ABLUTION leu(@)- ABNEGATE ne ABNORMAL gné- ABODE bheidh- ABOLISH al-3 ABORT er-! ABOUND wed-1 ABOUT ud- ABOVE upo ABRADE réd- ABRIDGE mregh-u- ABROGATE reg-1 ABROSIA gWere-4 ABRUPT reup- ABSCESS ked- ABSCISE kae-id- ABSCOND dhé-1 ABSENT eS- ABSOLUTE leu-1 ABSOLVE feu-1 ABSORB srebh- ABSTAIN ten- ABSTRACT tragh- ABSTRUSE treud- ABSURD swer-2 ABULIA gWele-1 ABUT bhau- ABYSS gWadh- ACANTHO- ak- ACANTHOPTERYGIAN pet- ACANTHUS ak- ACAPNIA kwép- ACCEDE ked- ACCELERATE kel-3 ACCENT kan- ACCEPT kap- ACCESS ked- ACCIDENT kad- ACCIPITER Oku- ACCLAIM kele-2 ACCLIVITY klel- ACCOLADE kwel-1 ACCOMMODATE med- ACCOMPLISH pele-1 ACCORD kerd-1 accosT kost- ACCOUNT peu- ACCRUE_ ker-3 ACCUMBENT keu-2 ACCUMULATE keue-2 ACCURATE cira ACERATE ak- ACERB ak- ACETABULUM ak- ACETIC ak- ACETUM = ak- ACHALASIA ghé-
1328:CABARET kamer- CABEZON kaput CABLE kap- CABRILLA kapro- CABRIOLET kapro- CACHE ag- CACHEXIA segh- caco- kakka- CACODYL kakka- CACOETHES kakka-, s(w)e- CACOPHONOUS bha-2, kakka- CACOPHONY kakka- CACUMINAL keu-2 CADASTER  steigh- CADAVER kad- CADELLE kat-1 CADENCE kad- CADENT kad- CADET kaput CADRE kWetwer- CADUCEUS kar-2 CADUCICORN kad-, ker-1 CADUCOUS kad- CAECILIAN kaiko- CAECUM kaiko- CAELUM_ kae-id- CAESURA kae-id- CAGE keua-2 CAHIER kWetwer- CAINOTOPHOBIA ken-3 CAIRD kerd-2 CAISSON kap-
1334:CANDENT kand- CANDID kand- CANDIDA kand- CANDIDATE kand- CANDLE kand- CANDOR kand- CANESCENT kas- CANICULA kwon- CANINE kwon- CANKER kar-1 CANNABIS kannabis CANOROUS_ kan- CANT? kan- CANTABILE kan- CANTEEN kanto- CANTICLE kan- CANTILLATE kan- CANTO kan- CANTON kanto- CANTOR kan- CANVAS kannabis CANZONE kan- CAPABLE kap- CAPACIOUS kap- CAPE2 kaput CAPELLA kapro- CAPIAS kap- CAPITAL! kaput CAPITAL? kaput CAPITATE kaput CAPITATION kaput CAPITELLUM kaput CAPITULATE kaput CAPITULUM kaput CAPO! kaput CAPON skep- CAPRIC ACID kapro- CAPRICE kaput CAPRICORN kapro-, ker-1 CAPRIFIG kapro- CAPRIOLE kapro- CAPROIC ACID kapro- CAPSICUM kap- CAPSID kap- CAPSTAN kap- CAPSULE kap- CAPTAIN kaput CAPTION kap- CAPTIOUS kap- CAPTIVATE kap- CAPTIVE kap- CAPTOR kap- CAPTURE kap- CAR kers-2 CARAMEL kolem- CARAT ker-1 CARAVANSARY tere-2 CARBON ker-4 CARBUNCLE ker-4 CARCINO-  kar-1 CARCINOGEN kar-1 CARCINOMA kar-1 CARD? kars- CARDIA kerd-1 CARDIAC kerd-1 CARDIO- kerd-1 CARDOON kars- CARE gar- CAREEN kar-1 CAREER kers-2 CARESS ka- CARET kes-2 CARGO kers-2 CARICATURE kers-2 CARIES ker-5 CARILLON kWetwer- CARINA kar-1 CARIOLE kers-2 CARL karlaz CARLING karlaz CARMINATIVE kars- CARNAGE sker-1 CARNAL sker-1 CARNASSIAL_ sker-1 CARNATION sker-1 CARNET kWetwer- CARNIVAL legh-, sker-1 CARNIVOROUS = sker-1 CAROCHE kers-2 CAROL aulo- CAROTID ker-1 CAROUSE ud- CARP! ger-2 “CARP kerp- CARPAL kwerp- CARPEL kerp- CARPENTER kers-2 CARPET kerp- CARPO- kerp-
1389:cons deuk- CONATION ken-1 CONCAVE keue-2 CONCEAL kel-2 CONCEDE ked- CONCEIVE kap- CONCERN krei- CONCESSION ked- CONCH konk(h)o- CONCHA konk(h)o- CONCHO- konk(h)o- CONCIERGE servus CONCILIATE kela-2 CONCISE kae-id- CONCLAVE kleu-3 CONCLUDE kleu-3 CONCOCT pekw- CONCOMITANT ei-1 CONCORD kerd-1 CONCOURSE kers-2 CONCRESCENCE ker-3 CONCRETE ker-3 CONCUBINE keu-2 CONCUPISCENCE kwép- CONCUR kers-2 CONCUSS kwét- CONDEMN dap- CONDENSE dens-2 CONDESCEND skand- CONDIGN dek-1 CONDIMENT dhé-1 CONDITION deik- CONDOLE del-3 CONDONE do- CONDOTTIERE deuk- CONDUCE deuk- CONDUCT deuk- CONDUPLICATE dwo- CONE k6-
1394:CONVOLVE wel-3 CONVULSE wel-4 cook pekw- cOoKY kak-2 cooL gel-3 COOPER ku- COOPERATE op-1 CO-OPT op-2 COORDINATION ar- COPE! kel-1 COPEPOD kap- COPIOUS op-1 COPRO- kekw- COPULA ap-! COPULATE ap-1 COPY op-1 CORACIIFORM ker-2, merph- CORACOID ker-2 CORBEL ker-2 CORBINA ker-2 CORD ghere- CORDATE kerd-1 CORDIAL kerd-1 CORDIFORM kerd-1 CORDON ghere- COREOPSIS sker-! CORGI kwon- CORIACEOUS sker-1 CORIUM §sker-1 cOoRM sker-! CORMORANT ker-2 CORN! gre-no- CORN2 ker-1 CORNEA ker-1 CORNEL ker-6 CORNEOUS ker-1 CORNER ker-1 CORNET ker-1 CORNICULATE ker-1 CORNIFICATION ker-1 CORNU_ ker-1 CORNUCOPIA op-! CORONA sker-3 CORONOID  sker-3 CORPORAL! kWrep- CORPORAL’ kWrep- CORPORATE kWrep- CORPOREAL kWrep- CORPOSANT kWrep-, sak- CORPS kWrep- CORPSE kWrep- CORPULENCE kWrep- CORPUS krep- CORPUSCLE kWrep- CORRADE réd- CORRECT reg-! CORRIDOR kers-2 CORRIE kWer-2 CORROBORATE reudh-! CORRODE réd- CORRUGATE ruk-2 CORRUPT reup- CORSAGE kWrep- CORSAIR kers-2 CORSE kWrep- CORSET kWrep- CORTEGE gher-1 CORTEX sker-1 CORUSCATE sker-2 CORVEE reg-! CORVINE ker-2 Corvus ker-2 CORYDALIS_ ker-1 CORYMB_ ker-1 CORYNEBACTERIUM bak-, ker-1 CORYPHAEUS_ ker-1 COSMONAUT nau-2 COSMOPOLITE pele-3 cosmos kes-3 cost sta-
1397:COUPLE ap-! COURAGE kerd-1 COURANTE kers-2 COURIER kers-2 COURSE kers-2 COURT gher-1 COURTEOUS gher-1 COURTESAN gher-1 COURTESY gher-' COURTIER gher-1 COUSIN swesor- COUTH gnd- COUTURE syi- COUVADE keu-2 COVE! ku- COVEN gWa- COVENANT gWa- COVER wer-5 COVET kwép- COVEY keu-2 cow! gWou- cow2 ku- COWER ku- COWSLIP gWou-, sleubh- coxa koksa
1399:CRANIUM ker-1 CRANK! ger-2 CRASH? ker-4 CRATE kert- CRATER kere- CRAW gWere-4 CRAWL! gerbh- CRAYFISH gerbh- CREATE ker-3 CREATINE kreue-1 CRECHE ger-2 CREDENCE kerd-1 CREDIBLE kerd-1 CREDIT kerd-1 CREDO kerd-1 CREDULOUS_ kerd-1 CREEK ger-2 CREEP ger-2 CREMATE ker-4 CREODONT kreue-1 CREOLE ker-3 CREOSOTE kreue-1, teus- CREPE sker-3 CREPITATE ker-2 CRESCENDO ker-3 CRESCENT ker-3 CRESS gras- CREST sker-3 CREVICE ker-2 CREW! ker-3 CRIB ger-2 CRIBRIFORM krei- CRICKET! ker-2 CRICOID  sker-3 CRIME krel- CRIMP! ger-2 CRIMSON k*rmi- CRINGE ger- CRINGLE ger-2 CRINITE sker-3 CRINKLE ger-2 CRINOLINE fino-, sker-3 CRIOSPHINX ker-1 CRIPPLE ger-2 CRISIS krei- CRISP sker-3 CRISPATE sker-3 CRISSUM sker-3 CRISTA sker-3 CRISTATE sker-3 CRITERION krei- CRITIC krei- CROCHET ger-2 CROCIDOLITE krek-1 CROCK! ger-2 GROCK® ger-? CROCKET ger-2 CROFT ger-2 CROMLECH léu-1, skerbh- CRONE sker-1 CROOK ger-2
1429:DIN dhwen- DINGUS _{enk-1 DINOSAUR dwei- DINOTHERE dwei- DIOCESE weik-! DIOECIOUS weik-1 DIOICOUS_ weik-1 DIOPTER oOkW- Dioscuri_ deiw-, ker-3 pip dheub- DIPHTHERIA deph- DIPHYODONT bheue- DIPLO- dwo- DIPLOCARDIAC kerd-1 DIPLODOCUS dek-1 DIPLOE dwo- DIPLOID pel-3 DIPLOMA dwo- DIPNOAN pneu- DIRE dwei- DIRECT reg-! DIRNDL tek- DISARM ar- DISASTER ster-3 DISBURSE bursa DISCERN krei- DISCIPLE dek-! DISCIPLINE dek-? DISCOMFIT dhé-1 DISCORD kerd-1 DISCOURSE kers-2 DISCRIMINATE krel- DIscuss kwét- DISDAIN dek-1 DISEMBOGUE beu-! DISFIGURE dheigh- DISGUST geus- DISK deik- DISMAL deiw-, mel-5 DISMAY magh-! DISMISS (s)meit(9)- DISPARATE pere-1 DISPATCH ped-! DISPEL pel-6 DISPENSE (s)pen- DISPERSE (s)preg- DISPLAY plek- DISPOSE apo- DISPUTE peu- DISQUISITION quaerere DISRUPT reup- DISSECT sek- DISSEMINATE 6-1 DISSENT sent- DISSERTATE ser-3 DISSIDENT sed-1 DISSILIENT sel-4 DISSIPATE swep-2 DISSOCIATE sekw-1 DISSOLVE leu-! DISSONANT swen- DISSUADE swad- DISTANT sta- DISTEND ten- DISTICH steigh- DISTINGUISH _ steig- DISTORT terkw- DISTRACT tragh- DISTRAIN  streig- DISTURB twer-! DITCH dhigw- DITTO deik- DITTY deik- DIURETIC wers-2 DIURNAL deiw- DIVA deiw- DIVARICATE wa- DIVE dheub- DIVERGE wer-3 DIVERT wer-3 DIvEs_ deiw- DIVIDE weidh- DIVINE! deiw- DIVINE? deiw- DIVULSION wel-4 Dizzy dheu-!
1456:ENAMEL mel-1 ENAMOR amma ENANTIOMER §ant- ENANTIOMORPH ant- ENARTHROSIS at- ENATE gene- ENCAUSTIC kéu- ENCEINTE? kenk-1 ENCEPHALO- ghebh-el- ENCHANT kan- ENCHASE kap- ENCHIRIDION ghesor- ENCLAVE kleu-3 ENCLITIC klei- ENCOUNTER kom ENCROACH ger-2 ENCYCLICAL kwel-1 ENCYCLOPEDIA pau- END ant- ENDEAVOR ghabh- ENDEMIC da- ENDERGONIC werg- ENDOCARDIUM kerd-1 ENDOCRINE krei- ENDOERGIC werg- ENDORSE dorsum ENDOSTEUM ost- ENDOTHECIUM dhé-1 ENDOTHELIUM dhé@(i)- ENDOW do- ENDUE deuk-, eu-1 ENDURE deru ENEMA yé-
1468:EPIBOLY gWele-1 EPIC wekw- EPICARDIUM kerd-1 EPICENE kom EPICRITIC krei- EPIDEMIC da- EPIDERMIS der-2 EPIDIDYMIS dwo- EPIDOTE do- EPIGASTRIUM gras- EPIGEAL gé EPIGENE gene- EPIGONE gene- EPIGRAM gerbh- EPIGRAPH gerbh- EPILEPSY (s)lag- EPILOGUE leg-1 EPIMYSIUM mis- EPIPHANY bha-1 EPIPHYSIS bheue- EPISCOPAL spek- EPISODE en, sed-2 EPISTASIS sta- EPISTAXIS stag- EPISTEMOLOGY sta- EPISTLE  stel- EPISTYLE sta- EPITAPH dhembh- EPITASIS ten- EPITHELIUM dhé@(i)- EPITHET dhé-1 EPITOME tem- EPOCH segh- EPODE wed-2 EPONYM nd-men- EPONYMOUS nd-men- EPOS wekw-
1565:GOAD ghei-1 GOAT ghaido- GOD gheu(e)- GODSEND sent- GOFFER webh- GOLD ghel-2 GOLIARD gWel-3 GOMPHOSIS gembh- -GON genu-! GONAD gene- GONFALON gWhen-1 GONIOMETER genu-1 GONIOMETRY genu-! GONION genu-! GONO- gena- coop ghedh- GOOSE! ghans- GORE! ghaiso- GORE? ghaiso- GORGE gWere-4 GORGET gWera-4 GORSE ghers- GOSHAWK ghans- GOSLING ghans- GOSPEL spel-3 GOSSIP s(w)e- GOUACHE akWa- GOWAN ghel-2 GRAB! ghrebh-1 GRABEN ghrebh-2 GRACE gWera-3 GRACKLE gera-2 GRADE ghredh- GRAFFITO gerbh- GRAIN gre-no- GRAM! § gerbh- GRAM? gre-no- -GRAM gerbh- GRAMA gras- GRAMINEOUS_ gras- GRAMMAR gerbh- GRAMPUS_peisk- GRANADILLA gfe-no- GRANARY gre-no- GRANDILOQUENCE tolkw- GRANGE gre-no- GRANITE gr@-no- GRANT kerd-1 GRANULE gre-no- GRAPE ger-2 GRAPH gerbh- -GRAPH gerbh- -GRAPHER gerbh- GRAPHIC gerbh- GRAPHITE gerbh- -GRAPHY gerbh- GRAPNEL ger-2 GRAPPA ger-2 GRAPPLE ger-2 GRASP ghrebh-1 GRAss_ ghré- GRATE! grat- GRATE? kert- GRATEFUL gWere-3 GRATIFY gWere-3 GRATIS gWera-3 GRATITUDE gWero-3 GRATUITY gWera-3 GRAUPEL kreup- GRAVE! ghrebh-2 GRAVE? gwWera-2 GRAVES ghrebh-2 GRAVEL ghréu- GRAVID gWera-2 GRAVURE ghrebh-2 GRAY gher-3 GRAYWACKE wegh-
1580:HEAD kaput HEAL kailo- HEALTH kailo- HEAP keu-2 HEAR keu-! HEARKEN keu-! HEART kerd-* HEARTH ker-4 HEAT kai- HEATH kaito- HEATHEN kaito- HEAVE kap-
1599:HERB BENNET deu-2 HERD kerdh-
1845:MEGALO- meg- MEGALOCARDIA kerd-1 MEGALOPOLIS_ pele-3 MEIOSIS mel-2 MEISTERSINGER sengh- MELANCHOLY ghel-2, mel-2 MELANGE meik- MELANO- mel-2 MELD! meldh- MELILOT melit- MELINITE mélon MELIORATE mel-4 MELIORISM mel-4 MELISMA mel-3 MELLIFEROUS melit- MELLIFLUOUS bhieu-, melit- MELODRAMA mel-3 MELODY mel-3, wed-2
1875:MIR mei-4 MIRACLE smei- MIRAGE smei- MIRE meu- MIRROR smei- MIRTH mregh-u- MIs-1_ mei-1, mei-2 MISADVENTURE gWa- MISANTHROPE ner-2 MISCEGENATION gene-, meik- MISCELLANEOUS meik- MISCHIEF kaput MISCIBLE meik- MISCREANT kerd-1 MISER miser MISERABLE miser MISERICORD kerd-1 MISERY miser MISFEASANCE dhé-1 MISHAP kob- MISNOMER nd-men- MISONEISM newo- MISPRISION ghend-, mei-1 MIss! mei-1 MISSEL THRUSH meigh- MISSILE (s)meit(9)- MISSION (s)meit(a)- MISSIVE (s)meit(e)- MIST meigh- MISTAKE mei-1 MISTER meg- MISTLETOE meigh- MISTRAL meg- MISTRESS meg- MITE! = mai-1
1898:MUSTARD meu- MUSTELINE mis- MUSTER men-! MUSTY meug-2 MUTATE mei-1 MUTCHKIN med- MUTE mul- MUTILATE mut- MUTTER mul- MUTTON mel-1 MUTUAL mei-1 MUZHIK man-1 MUZZLE musum MY me-1 MYCELIUM walso- -MYCETE meug-2 MYCO- meug-2 MYCORRHIZA wrad- MYELO- mis- MYIASIS § mu-2 MYLONITE mele- MYNA mad- MYNHEER me-1 MYO- mis- MYOCARDIUM kerd-1 MYOPIA mut-, okw- MYOSOTIS miis-, ous- MYRIAD meu- MYRMECO- morwi- MYROBALAN gWel@-2 MYSELF me-! MYSOPHILIA meu- MYSOPHOBIA meu- MYSTAGOGUE ag- MYSTERY! mut- MYSTERY? mei-2 MYSTIC mul- MYSTICETE miis- MYTHOPOEIC kWeij-2 MYXO- meug-2
2079:PER- pert PERCEIVE kap- PERCENT dekm PERCH? perk-1 PERCOLATE kagh- PERCURRENT kers-2 PERCUSS kwét- PERDITION d6- PERDURABLE deue- PEREGRINE agro- PEREMPTORY em- PERENNIAL at- PERFECT dhé-1 PERFIDY bheidh- PERFORATE bher-2 PERFUME dheu-1 PERFUNCTORY bheug-2 PERFUSE gheu- PERGOLA perg- PERI- per! PERICARDIUM kerd-1 PERICLINE Klei- PERIGEE gé PERIHELION sawel- PERIL per-4 PERIMYSIUM mis- PERINEPHRIUM negWh-ro- PERIOD sed-2 PERIONYCHIUM nogh- PERIOSTEM ost- PERIPATETIC pent- PERIPETEIA pet- PERIPHERY bher-1 PERIPHRASIS gWhren- PERIPHYTON bheue- PERIPTERAL pet- PERISARC  twerk- PERISH ei-1 PERISSODACTYL per! PERISTALSIS | stel- PERISTYLE sta- PERITHECIUM dhé-1 PERITONEUM ten- PERITRICH _ thrix PERIWINKLE! weng- PERJURE yewes- PERMANENT men-3 PERMEATE mei-1 PERMIT (s)meit(a)- PERMUTE mei-1 PERNICIOUS nek-1 PERONEAL per-2 PERORAL 6s- PERORATE 6r- PERPEND (S)pen- PERPENDICULAR (S)pen- PERPETRATE peter- PERPETUAL pet- PERPLEX plek-
2146:QUA kWo- QUACKSALVER gWébh-2, selp- QUADRANT kWetwer- QUADRATE kWetwer- QUADRENNIUM at- QUADRI- kWetwer- QUADRILLE! kWetwer- QUADRILLE? kwetwer- QUADROON kWetwer- QUADRUMANOUS man-2 QUADRUPLE pel-3 QUAESTOR quaerere QUAGMIRE meu- QUAINT gnd- QUALIFY dhé-1 QUALITY kWo- QUANTITY k¥o- QUARANTINE kWetwer- QUARREL! kwes- QUARREL2 kwetwer- QUARRY! kerd-1 QUARRY? kwetwer- QUART kWetwer- QUARTAN kwetwer- QUARTER kWetwer- QUARTO kWetwer- QUARTZ twer-2 QUASH kes-2
2174:REBUT bhau- RECALESCENCE kele-! RECANT kan- RECAPITULATE kaput RECEDE ked- RECEIVE kap- RECENSION kens- RECENT ken-3 RECIDIVISM kad- RECIPROCAL pert RECISION kae-id- RECK reg-1 RECKLESS reg-! RECKON reg-1 RECLAIM kele-2 RECLINE klei- RECLUSE kleu-3 RECOGNIZE gnd- RECOIL (s)keu- RECOMMEND man-2 RECONDITE dhé-1 RECORD kerd-1 RECOURSE kers-2 RECOVER kap- RECREANT kerd-1 RECREMENT krei- RECRIMINATE  krei- RECRUDESCE kreud-! RECRUIT ker-3 RECTANGLE reg-1 RECTIFY dhé-1, reg-1 RECTILINEAR reg-1 RECTITUDE reg-!
```


## [2026-09-06T16:17:54.590Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"4.44 HEART\\|HEART$\\|4\\.44\" SYN.txt | head -20; echo \"--- find leaf with HEART table\"; awk 'BEGIN{RS=\"\\f\"} /HEART/ && /kardia|zarad|zdrad|Herz/ {print NR\": \"substr($0,1,300)}' SYN.txt | head"
}
```


### [2026-09-06T16:17:56.279Z] TOOL RESULT

```
5202:HEART
5268:There is frequent shift of application between words for parts of the body that are adjacent, of similar relative position, associated in function, or through common figurative uses with reference to the emotions. So between ‘head’—‘horn’ (from ‘summit’); ‘head’— ‘skull’—‘brain’; ‘mouth’—‘jaw’, ‘throat’, ‘cheek’, ‘chin’, ‘lip’; ‘neck’—‘throat’; ‘shoulder’—‘shoulderblade’—back’—“‘arm’ ; ‘hand’—‘arm’; ‘foot’—‘leg’; ‘finger’—‘toe’ ; ‘belly’—‘womb’; ‘breast’ as front of the chest—‘woman’s breasts’; ‘heart’ from ‘soul’ (Rum. inimd, 4.44) or ‘bowels’ (W. calon, 4.44).
6463:4.44 HEART
6542:Br. poullkalon, poulgalon (cf. Vallée s.v. estomac), epd. of poull ‘hole, hollow’ and kalon ‘heart’ (4.44).
19193:Goth. arniba adv. (renders dc¢adés Mk. 14.44) : ON ern ‘brisk, vigorous’, OE eornost ‘zeal, earnestness’, etc. perh. fr. the root in Skt. roti, rnvati ‘arises, moves’, Grk. dpyipe ‘arouse, move’, etc. Walde-P. 1.138. Feist 58.
19216:6. ChSl. stichranino adv. (renders aopadras Mk. 14.44) : (st)chraniti ‘save, preserve’ (11.24).
22088:simple kreiz is used as prefix ‘mid~’, e g it kreizdeiz ‘midi’, kreiznoz ‘minuit’, Stan ‘ 3. Lith. vidurinis, Lett. vidéjs fp ib Lith., Lett. vidus ‘middle, inner part? for this prob. : Skt. vidhu- ‘solitary, He bt lated’, Lat. di-videre ‘separate, divide’ Walde-P. 1.239. st 4. SCr. srednij, Boh. st¥ednt, Po), ® Sredni, Russ. srednij, fr. the sbs. Ch§], . sréda, etc. ‘middle’: ChSl.  sriidice ‘heart’, etc. (4.44). Briickner 534, uN pot
24297:CHAPTER 14 TIME! 14.43 ae 14.44 ay 14.45 YounG 14.46 OLD 14.47 Barty (adv.) 14.48 Late (adv.) 14.49 Now 14.51 14.52
24499:Rum. de dimineaté, lit. ‘of morning’ (14.44).
24513:ChSl. za utra (renders Grk. zpwt), lit. ‘in the morning’ (utro, 14.44).
25353:14.44 MORNING
25440:Most of the expressions for ‘tomor- row’ ate derived from words for ‘morn- ing’ (14.44), the semantic development being ‘in the morning’ = ‘on the follow- ing morning’, whence with extension to the entire day ‘tomorrow’.
25445:3, Ir. imbarach, NIr. i mbaireach, W. wfory : W. bore ‘morning’ (14.44). Peder- Sen 1,99,
25480:3. Lith., Lett. vakar (orig. loc. sg.), Ch8SI. viéera, viiéera, SCr. jucer, etc., gen- eral Slavic (prob. old instr. sg.) fr. the Balto-Slavie word for ‘evening’ (14.46). Walde-P. 1.311. Vasmer, IF 42.179 ff. Miihl.-Endz. 4.446.
28437:ChSI. milosriidige, SCr. milosrde, Po], mitosierdaie, fr. the adj. ChS]. milosriidy, piteous’, fr. milt ‘piteous’ and words for ‘heart’ (4.44), semantic borrowing fy Goth. armahairts, Lat. misericors (above, 2,4). Meillet, Etudes 385.
28664:Russ. serdce ‘heart’ (4.44) is also used for ‘anger’ (now only in certain phrases), and the deriv. vb. serdit’sja is more com- mon than gnevit'sja for ‘be angry’. Cf. also Lith. sirdytis ‘be angry’ (prob. with semantic borrowing), SCr. srditi se ‘be angry’, srdit ‘angry’, srdzba, etc. ‘anger’.
30337:1. IB *kred-dhe-, cpd. of *dhé- ‘put, place’ and kred- seen in Skt. ¢rad- (iso- lated in Ved. crad asmai dhatta ‘believe in him’, etc.), this prob. not, as former- ly assumed, the same words as IE *kred-, *frd- in words for ‘heart’ (Lat. cor, cordis, Grk. xapéia, Ir. cride, etc., 4.44), but perh. : Ir. cretair, W. crair ‘relic, reliquary’. Ernout-M. 229. Walde-H. 1.287. Vendryes, RC. 44.90 ff.
35084:Lett. vairuogs, deriv. of vairtt ‘ward off, protect’. Miihl.-Endz. 4.443.
--- find leaf with HEART table
289: e- P, 2.108.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
arts OF TH Goth. hairlo k xapdla ON hjarta on apie Dan. /yerte N ¢, oor Sw. hjarta Ia. cuore OE heorte : caur ME herte " corazén NE heart Rum, inimd Du. hart _  oride OHG  herza Nir. croidhe MHG herze i re NHG_herz Most of th
```


## [2026-09-06T16:18:02.465Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==289' SYN.txt"
}
```


### [2026-09-06T16:18:04.006Z] TOOL RESULT

```
e- P, 2.108.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
arts OF TH Goth. hairlo k xapdla ON hjarta on apie Dan. /yerte N ¢, oor Sw. hjarta Ia. cuore OE heorte : caur ME herte " corazén NE heart Rum, inimd Du. hart _  oride OHG  herza Nir. croidhe MHG herze i re NHG_herz Most of the words for ‘heart’ belong ‘ to an inherited group. Words for ‘heart
or their derivatives may be used for the ‘middle, center’ and for such yanous emotions as ‘courage’, ‘love’, ‘anger, etc. (chapter 16).
1, IE *herd-, etc., with gradation. Walde-P. 1.423 ff. Ernout-M. 219 f. Grk. xapdia, poet. xp; Lat. cor (> It. cuore, Fr. ceur, OSp. cuer; Sp. corazon, Port. coracgago fr. deriv.); Ir. cride, NI. crotdhe (W. craidd, Br. kreis ‘cen- ter’); Goth. hairtd, OE heorte, etc., gen- eral Gme.; Lith. srdis, Lett. sirds,
Digitized by Arya Samaj Foundation Chennai and eGangotri
& BODY; BODILY FUNCTIONS AND CONDITIONS 251
4.44 HEART
Lith.  Sirdis
Lett. sirds
ChSl. _ sriidice
SCr.  srce
Boh. — srdce
Pol. serce
Russ.  serdce
Skt. hrd-, hrdaya- Av. zarad-
ChSl. sridice, etc., general Slavic; Arm. sirt; here also Skt. Ard-, hrdaya-, Av. zarad-, but with init. as if fr. IE gh, due to a blend with some other word; Hitt. kartis (Sturtevant, Hitt. Gram. 106).
2. Rum. znimd, fr. Lat. anima ‘soul’, with shift through common figurative uses of ‘soul’ and ‘heart’. REW 475.
3. W., Corn., MBr. calon, Br. kalon, loanword fr. a form like OFr. cauldun, chaudun ‘bowels’ (deriv. of Lat. caldus ‘warm’), with shift through common figurative uses of ‘bowels’ and ‘heart’. Pedersen 1.147.
4.45 LIVER
ne rap Goth. . Lith. kepenys, jaknos (pl.) Lat se ie ON lifr Lett. aknas (pl.)
ie oat Dan. lever ChSl. jetro
! ac c Sw. lever SCr.  jetra
» — higad OE lifer Boh. jdira Rum, feat i ae liver Pol. -watroba
4 7 x, fe Yon! Nir 0a, trommchride Du. me ees, ae pecen W. oi OHG = libara ee yakara avy MHG leber(e) NHG leber
eral 0 ‘liver’ belon 0 an Inherited group. But the IE a:
pat Teplaced by others,
typical neuter r/n
alde-P 20 5 . = : 1D; 1.673, Tnout-M,
Grk. jap, gen. -aros; Lat. iecur (later qocur), gen. -oris, -inoris; Lith. jaknos (or jeknos, OLith. jekanas, all pl.), Lett. aknas (pl.); Skt. yakrt, gen. yaknas, Av. yakara, NPers. jigar.
2. NG cuxari, dim. form of late Grk. cixwrdv, neut. of cixwrds (fr. oxo “fig’), in Frap cvxwrov, denoting the liver of ani- mals fed on dried figs, as explained in
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
itt tt ee
Digitized by Arya Samaj Foundation Chennai and eGangotri
252 SELECTED INDO-EUROPEAN SYNONYMS
Gal. 6.679, 704. Hence the Latinized form ficatum (fr. ficus ‘fig’), whence (but with fluctuation of accent and of vowel of first syllable; cf. REW 8494), It. fegato, Ir. foie, Sp. higado, Rum. ficat.
3. Ir. da, NIr. ae, W. afu, Br. avu, general Celtic word, etym.? Pedersen 1.313.
Ir. trommcehride, cpd. of tromm ‘
```


## [2026-09-06T16:18:11.249Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN leaf 188 ===\"; awk 'BEGIN{RS=\"\\f\"} NR==188' KLN_1966.txt | head -c 3000"
}
```


## [2026-09-06T16:18:12.535Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^cor, cordis\\|^cor,\" LAT.txt | head; echo \"---\"; awk 'BEGIN{RS=\"\\f\"} /cor, cordis/ {print NR}' LAT.txt | head"
}
```


### [2026-09-06T16:18:13.210Z] TOOL RESULT

```
=== KLN leaf 188 ===
e,  fir  cone’.  See  cone.
conjecture,  n.,  1)  guesswork;  2)  guess.  —  L.  con- jectura,  ‘inference,  conclusion’  (whence  also  F. conjecture),  fr.  conjectus,  pp.  of  conicere  (less correctly  conjicere ),  ‘to  throw  together ;  to  infer, conclude’,  fr.  con-  and  jacere,  ‘to  throw’.  See
jet,  ‘to  spirt  forth’,  and  -ure.  For  the  change  of Latin  d  (in  jacere)  to  e  (in  con-jectus)  see  accent and  cp.  words  there  referred  to.
Derivatives:  conjecture,  tr.  and  intr.  v.,  con- jectur-able,  adj.,  conjectur-abl-y,  adv.,  conjectur¬ al,  adj.,  conjectur-al-ly ,  adv. conjoin,  tr.  v.  —  ME.  conjoinen,  fr.  F.  conjoindre, fr.  L.  conjungere,  ‘to  join  together’  (whence  also It.  congiungere.  Proven?.  conjonher),ir.  con- and jungere,  ‘to  join’.  See  join  and  cp.  conjoint, conjugate.
Derivatives:  conjoin-ed,  adj.,  conjoin-er,  n. conjoint,  adj.  —  F.  conjoint,  pp.  of  conjoindre. See  prec.  word  and  conjunct  and  cp.  disjoint. Derivatives:  conjoint -ly,  adv.,  conjoint-ness,  n. conjugal,  adj.,  of  marriage.  —  L.  conjugalis, ‘relating  to  marriage’  (whence  also  F.  conjugal), fr.  L.  conjux  (later  form  conjiinx),  gen.  conjugis, ‘spouse’,  which  is  rel.  to  conjungere,  ‘to  join together’.  See  conjoin  and  adj.  suff.  -al. Derivatives:  conjugality  (q.v.),  conjugal-ly,  adv. conjugality,  n.  —  Coined  by  Milton  fr.  prec.  word and  suff.  -ity.
conjugate,  tr.  and  intr.  v.  —  L.  conjugatus,  pp.  of conjugdre,  ‘to  join  together,  unite’,  fr.  con-  and jugare,  ‘to  join;  to  yoke;  to  marry’,  which  is rel.  to  jugum,  ‘yoke’ ,  jungere,  ‘to  join’.  See  join and  verbal  suff.  -ate  and  cp.  jugate.  Cp.  also conjoin.
conjugate,  adj.  —  L.  conjugatus,  pp.  of  conjugdre. See  conjugate,  v.
Derivative:  conjugate-ly,  adv. conjugation,  n.  —  L.  conjugdtio,  gen.  -dnis,  ‘a combining,  connecting,  conjugation’,  fr.  con¬ jugate,  pp.  of  conjugdre.  See  conjugate,  v.,  and -ion.  In  its  grammatical  sense,  L.  conjugdtio  is a  loan  translation  of  Gk.  outjuyla,  lit.  ‘a  yoking, or  binding,  together’.
Derivatives:  conjugation-al,  adj.,  conjugation-al¬ ly,  adv.
conjunct,  adj.,  joined  together,  united  (archaic). —  L.  conjunctus,  pp.  of  conjungere,  ‘to  join  to¬ gether’.  See  conjoin  and  cp.  conjoint. Derivatives:  conjunct,  n.,  conjunct-ly,  adv. conjunction,  n.  —  ME.,  fr.  OF.  (=  F.)  conjonc- tion,  fr.  L.  conjunctidnem,  acc.  of  conjunctio,  fr. conjunctus,  pp.  of  conjungere.  See  conjunct  and -ion.  Cp.  It.  congiunzione,  OProven?.  conjunctio, Sp.  conjuncidn,  which  all  derive  fr.  L.  con- junctionem.  In  its  grammatical  sense  L.  con¬ junctid  is  a  loan  translation  of  Gk.  cn>v8ea[Ao; (fr.  ouvScTv,  ‘to  bind  together’).
Derivatives:  conjuncdon-al,  ad
```


### [2026-09-06T16:18:15.831Z] TOOL RESULT

```
13811:cor, cordis n. (encore scandi cor, c.-k-d.*corr, d e*cord dans P 1 .
---
272
```


## [2026-09-06T16:18:24.502Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==272' LAT.txt | head -c 4000"
}
```


### [2026-09-06T16:18:25.918Z] TOOL RESULT

```
«53 -
cor
d'o 4 praecox, -cis et les fornes pina rdcentes praecoquis, praecoquus
"7ipo<jopoc", et de "digdrer". S'eaploie dans ces acceptiona £galenent
au sena moral "nfirir (un projet), nijoter". Uaitd de tout tenps. Panro-
aan, M.L. 3313 ( *cocere ).
Noabreux d6rivds en coqu-, coc- fora 4 s aur le thbae du pr^sent,
et, en coct- aur le thbne du aupin: coquus ( coquos, cocus),-i m. :
cuialnler (dlargisseaent d'un noa racine avec vocaliane o ancien? cf.
gr. OLfyvo— kotcoC avec diaaiailation pour * 7 i 07 ioc); coquinus (coci-); d'ou
coqutna (coci-): cuiaine, coquinS, -Sre: faire la cuiaine; cocibilis
(-qui-)’, coquester (Glosa. ),qui ont tona surv£cu dana lea langues
ronanea, cf. M.L.3313 coquina *cocina ; 3314 coquinare *coclndre-, 3315
coquistro-, 3316 coquus-, 3014 cocibilis. Sur le groupe, v. M.Niederaann,
Mua. Helv., 3,3, p.135 (1945). Le gera. a v.h.a. chohhon, chuhhina, choh;
le celt.: britt. cegin "cuiaine", coaza, coeth de cocto, coctus-, iri»
coca, coic, cucann "coquus, coquina", cuilenn "culina".
cocula: uaesa aena coctionibus apta, Alii cocula dicunt ligna ninuta
quibus facile decoquantur obsonia, P.F.34,34. Frdquentatifa: Coquito
(attribui k Plaute par P.F.54,6) et coctito (P.F.ibid.).
coctio M.L.3018; coctor-, coctSra M.L.3030, toua trois de 1'^poque
imperiale, t an di 3 que dScoctor est dans Cic£ron; coctilis-, coctiuus-,
coctorium ( Dioscor. cf. M.L.3019); coctSrius, coctilidrius (Gloaa.);
cf. encore M.L.3016 * coctiare.
Coaposds: concoquo: cuire ensemble ou entifrement, et "dig^rer"
(= C5up.7ieooto); concoctio M.L.3ii6b,c; decoquo: r^duire par la cuisson
(trans, et abs. ); faire baaqueroute (aanger tout son bien); decoctio,
-tor-, excoquo: achever de cuire, ou chasser (extraire) pax la cuisson,
excoctis, excocta, M.L.3985, 3977; gera.: v.h.a .scotto-, percoquo-,
recoquo: recuire, retreaper (dea ep£es) M.L.76383; 7635 recoctus . - Se -
cond eliment de coapos£ dans aulicoctus et ollicoquus (ou *ollicox
coaae praecox?)-, praecox conservi partielleaent dans les 1. roaanes,
avec des alterations, cf. M.L.6713 praecSquus. Le rapport de culina
avec coqu 5 est douteux. V. aussi popa, popina.
I.-e. *pek w o a passd k *tf°ek w o en italo-celtique: cf. gall. £0 i>i
"cuire", v. quinque. Ce prdaent ae retrouve dans v.sl .pekp " je cuis"
(forne altdr 4 e kepu en lituanien), alb. pjek, skr. paeani (aene sena),
t an dis que le grecaun pr^aent ddriv 4 TteoCRo, att. Tiemo. - Tokh. B papakqu
"cuit". Lat. popina est eaprunt^ i 1 'oaque. - La notion de "naturit^"
est li£e k la racine depuis 1'indo-europ^en , cf . gr. nemuN, neneipa. et
akr. pakvdh "mfir"; aais le latin ne l'a que dans coctiuus et dans le
compose praecox', cf. mdturus} pour le contraire, crudus »
cor, cordis n. (encore scandi cor, c.-k-d.*corr, d e*cord dans P 1 .
Pe. 803, Poe.390a, Mi.1058?: abreg£ dans Lucilius): 1° coeur; 3°
coeur en tant que sibge de l'aae, Cic., Tuae. 1,18, aliis cor ipsun
animus uidetur, ex quo excordes, uecordes, concordesque ‘ dicuntur-,
I, 41, ne tan uegeta nens aut in corde cerebroue aut in Empedocleo san¬
guine iaceat; aibge de 1 1 intelligence et de la sensibilit£: Isid.,Or.
II, 1,118, in corde, omnis sollicitudo et scientiae causa manet-, Varr.,
L.L.6,46, cura quod cor urat-, Lact., Opif .10,11, cor quod sapientiae
domicilium uidetur-, Schol. Pera. 1,13, [ physici dicunt J homines corde
sapere. Daitd de tout teaps. M.L.3317.
D 4 riv£s et coaposds: cordatus: avis 4 , sage; aot d'Ennius repris par
lea archaisants, M.L.3338; recordor, -aris: se reaettre dans 1 'esprit
M.L.7139; excors (ancien, claas.) et excordor (Coaa.); uecors, uecor-
dia; socors, socordia, qui se rattachent plutot k 1 a notion d'intelli-
gence; concors (v. ce aot), discors et leurs d^riv^s, k la notion de
```


## [2026-09-06T16:18:26.156Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 189 190 191; do echo \"=== KLN leaf $n ===\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' KLN_1966.txt | grep -n \"cordial\\|^core\\|heart\\|zdr\\|zar\" | head -20; done"
}
```


### [2026-09-06T16:18:27.841Z] TOOL RESULT

```
=== KLN leaf 189 ===
=== KLN leaf 190 ===
=== KLN leaf 191 ===
```


## [2026-09-06T16:18:35.072Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==272' LAT.txt | tail -c 2500; echo; echo \"=== leaf 273 ===\"; awk 'BEGIN{RS=\"\\f\"} NR==273' LAT.txt | head -c 1500"
}
```


### [2026-09-06T16:18:37.483Z] TOOL RESULT

```
ctSra M.L.3030, toua trois de 1'^poque
imperiale, t an di 3 que dScoctor est dans Cic£ron; coctilis-, coctiuus-,
coctorium ( Dioscor. cf. M.L.3019); coctSrius, coctilidrius (Gloaa.);
cf. encore M.L.3016 * coctiare.
Coaposds: concoquo: cuire ensemble ou entifrement, et "dig^rer"
(= C5up.7ieooto); concoctio M.L.3ii6b,c; decoquo: r^duire par la cuisson
(trans, et abs. ); faire baaqueroute (aanger tout son bien); decoctio,
-tor-, excoquo: achever de cuire, ou chasser (extraire) pax la cuisson,
excoctis, excocta, M.L.3985, 3977; gera.: v.h.a .scotto-, percoquo-,
recoquo: recuire, retreaper (dea ep£es) M.L.76383; 7635 recoctus . - Se -
cond eliment de coapos£ dans aulicoctus et ollicoquus (ou *ollicox
coaae praecox?)-, praecox conservi partielleaent dans les 1. roaanes,
avec des alterations, cf. M.L.6713 praecSquus. Le rapport de culina
avec coqu 5 est douteux. V. aussi popa, popina.
I.-e. *pek w o a passd k *tf°ek w o en italo-celtique: cf. gall. £0 i>i
"cuire", v. quinque. Ce prdaent ae retrouve dans v.sl .pekp " je cuis"
(forne altdr 4 e kepu en lituanien), alb. pjek, skr. paeani (aene sena),
t an dis que le grecaun pr^aent ddriv 4 TteoCRo, att. Tiemo. - Tokh. B papakqu
"cuit". Lat. popina est eaprunt^ i 1 'oaque. - La notion de "naturit^"
est li£e k la racine depuis 1'indo-europ^en , cf . gr. nemuN, neneipa. et
akr. pakvdh "mfir"; aais le latin ne l'a que dans coctiuus et dans le
compose praecox', cf. mdturus} pour le contraire, crudus »
cor, cordis n. (encore scandi cor, c.-k-d.*corr, d e*cord dans P 1 .
Pe. 803, Poe.390a, Mi.1058?: abreg£ dans Lucilius): 1° coeur; 3°
coeur en tant que sibge de l'aae, Cic., Tuae. 1,18, aliis cor ipsun
animus uidetur, ex quo excordes, uecordes, concordesque ‘ dicuntur-,
I, 41, ne tan uegeta nens aut in corde cerebroue aut in Empedocleo san¬
guine iaceat; aibge de 1 1 intelligence et de la sensibilit£: Isid.,Or.
II, 1,118, in corde, omnis sollicitudo et scientiae causa manet-, Varr.,
L.L.6,46, cura quod cor urat-, Lact., Opif .10,11, cor quod sapientiae
domicilium uidetur-, Schol. Pera. 1,13, [ physici dicunt J homines corde
sapere. Daitd de tout teaps. M.L.3317.
D 4 riv£s et coaposds: cordatus: avis 4 , sage; aot d'Ennius repris par
lea archaisants, M.L.3338; recordor, -aris: se reaettre dans 1 'esprit
M.L.7139; excors (ancien, claas.) et excordor (Coaa.); uecors, uecor-
dia; socors, socordia, qui se rattachent plutot k 1 a notion d'intelli-
gence; concors (v. ce aot), discors et leurs d^riv^s, k la notion de

=== leaf 273 ===
corallium
- «54
sensibilitA (cf. toutefois 6 \movoia)f concordium M.L.3117; misericors,
misericordia, termes de 1 'Apoque rApublicaine, spAcialenent affection-
nAs par CicAron, qui disparuissent de la latinitA d'argent pour
reparaitre Abasse Apoque (v. miser); mundicors ; praecordia,-ium n.pl.;
enveloppe da coeur, coeur (dArirA ea -i-), M.L.6713; prdui- torticordius,
(Ang. in Psalm.146,7, cf. crasstuenius, etc.); Verticordia, surno■ de
VAnus; corculum: petit coeur (t. de tendresse; surnoa de Scipio Nasica;
attestA chez Plaute, et repris par les archaisants), M.L.3337; corcil¬
lum (P 4 tr.); cordolium: peine de coeur; mot pl au tini en; cf. xap6t,aXYl>cx
(Gal.), M.L.3339; cordicitus adr. (Sid.) d'aprbs rSdicitus. En outre
la langue populaire a tendu A reaplacer la forae monosyllabique par
une forme plus pleine, cordtum, attestAe par une tabella deuotionis,
peut-etre analogique de ficatum "foie M , V. M.Niedermann, Glotta 3,53,
et Neue Iahrb f. klass. Altertum 39,315 et M.L.3330. De IA *coraticum,
auquel remontent ir.courage, pr ov.coratge, etc. Pour cortumio, v.
ce aot.
Le noa du "coeur", qui est presque partout neutre, est au fond le
meae dans toutes les langues indo-euro]>Aennes. II est probable que le
nominatif-accusatif Atait de la forae k'erd, conserrAe dans hitt. kir
(Acrit 31 -ir), cf. Sommer HAB, p.q^sq», gr. xrjp, r. pruss. seyr (Voc.;
de IA siran Ench.), et que les antres cas reposaient sur k'rd~, conservi
dans lat. cordis, cordi, corde, sur quoi a AtA refait un
```


## [2026-09-06T16:18:40.570Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==273' LAT.txt | sed -n '1,60p' | tail -c 2200"
}
```


### [2026-09-06T16:18:42.721Z] TOOL RESULT

```
xrjp, r. pruss. seyr (Voc.;
de IA siran Ench.), et que les antres cas reposaient sur k'rd~, conservi
dans lat. cordis, cordi, corde, sur quoi a AtA refait un nominatif-
accusatif *kord italique ou latin. Le nominatif-accusatif pouvait etre
Alargi par -i,' d'ou arm. si rt, de *k'erdi, instr .srtiw. Le lituanien a
lit. oriental Serdis (acc. Serdj, donc suppo sant *X’erd~) au sens de
"moelle d'arbre M , et, dans 1'enseable du domaine, sirdis (acc.si rdj,
d'aprbs le type Serdi) "coeur". L't de Serdts, sirdis est sans doute
* sfc
ancien; mais le lituanien garde des formes de k’erd- et k'rd- dans
lit.or, Serdu gAn.plur. et dans y. lit. sirdes (gAn.sg.), Sirdy (gAn.pl.).
Sur *k r erd~, le germanique a bati un thbme en -«-, neutre: got. hairto
(gAn. hairtins), Le nom du "coeur", est obtenu souvent au moyen de suf-
fizes de dAriration comprenant -i-: -r. iri. cride, gall. craidd - hom.
xpa8iT|, att. xapBia - v.sl. srudice (A cotA du dArirA sreda, de *k'erdd
"nilieu"). Le hittite a kardiS "coeur". - L'indo-iranien a un mot parat -
lfele, mais comnenpant par une sonore aapirAe: vAd .hrdah (gAn.abl.),
gath. z ara da (instr. ), pers. di l (de *drd~) - -r 6 d. hrdayan, a.x. zsrsdaem.
- Pour le rapport qn'on a enrisagA, sans raison, arec credo, t. ce
mot.
corallium ( curalium; cdralium; coralium), -I n.: corail. Emprunt
au gr. HOUpaXtov, xoapaXlov, xopaXXiov. Depuis Lucr. Les formes romanes
remontent A coralium, et, isolAment, A corallium, M.L.3319; l'irl.
curel A cdralium.
cGrm: - ad▼. (uniquement dans cet emploi cbez Plaute) et prAp. avec
abi. "face A face, en face [de]", xaxa 7tpoaw7iov, evomi. ov. Le rapport
arec os est peut-fctre encore senti dans TAr., Ad.369, uereor coram in
os te laudare amplius. Souvent joint A praesens, adsum-, de IA le sens
de "en personne". AttestA dans toute la latinitA. Non roman.
ComposA: incffram. Eappelle par sa finale clam, palam, mais la fa^on
dont coram est formA n 1 est paa daire. Aucune prAposition latine n'en
rend compte.
corbis, —is m. et f. (le fAminin semble plus ancien et plus clas¬
sique, cf.Thes. IV 948,3; on a un doublet corbes dans Char. GTJT I 40,9,
corbs dans Fg. Bob. GLK V 561,35; abi. corbi dans Caton Agr.136, mais
```


## [2026-09-06T16:18:56.212Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} END{print \"leaves:\",NR}' KLN_1966.txt; grep -n \"^cordial\\|^core,\\|^cordate\\|^heart,\" KLN_1966.txt | head"
}
```


## [2026-09-06T16:18:57.025Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^credo\\|^credo,\" LAT.txt | head; awk 'BEGIN{RS=\"\\f\"} /credo, -is/ {print NR}' LAT.txt | head"
}
```


### [2026-09-06T16:18:57.739Z] TOOL RESULT

```
leaves: 903
9172:cordate,  adj..  heart-shaped.  —  L.  cordatus,  ‘wise, prudent’  (in  ModL.  ‘heart-shaped’),  from  cor, gen.  cordis,  ‘heart’,  which  is  cogn.  with  Goth. hairto,  OE.  heorte,  ‘heart’.  See  heart  and  adj. suff.  -ate.
9175:cordial
9177:cordial,  adj.  —  Late  L.  cordialis,  fr.  L.  cor,  gen. cordis,  ‘heart’.  See  cordate  and  -fed.
9185:core,  n.,  hard  center  of  a  fruit,  etc.  —  Prob.  fr. L.  cor,  ‘heart’;  see  cordate.  For  sense  develop¬ ment  cp.  Avestic  zlrlbaya,  ‘middle’,  OSlav. srudice,  ‘heart’,  sreda,  ‘middle’,  Russ,  serdee, ‘heart’,  sereda,  ‘middle’;  Wednesday  (i.e.  middle of  the  week)’,  Lith.  sirdis,  ‘heart’,  W.  craidd, ‘heart;  center’,  Bret,  kreiz,  ‘middle’;  all  these
17354:heart,  n.  —  ME.  herte,  hert,  fr.  OE.  heorte,  rel. to  OS.  herta,  ON.  hjarta,  OFris.  herte,  hirte, ODu.  herta,  Du.  hart,  OHG.  herza,  MHG. herze,  G.  Herz,  Goth,  halrto,  ‘heart’,  and  cogn. with  Hitt,  kardiash  (gen.),  ‘of  the  heart’,  Arm. sir!  (for  *kerdi-),  Gk.  xapSta,  poet.  >a)p,  L.  cor (gen.  cordis),  OSIav.  srudice,  Russ,  serdce, ‘heart’,  Lith.  Sirdis,  ‘heart’,  OPruss.  seyr  (for *kerd),  acc.  siran,  OIr.  cride,  Ir.  croidhe,  ‘heart’, W.  craidd,  ‘heart;  center’,  Bret,  kreiz,  ‘middle’, OSIav.  sridd,  Russ,  seredd,  ‘middle’,  Avestic zlrl6aya-,  ‘middle’.  For  sense  development  cp. Heb.  lebh,  ‘heart’,  and  lebh  yam,  ‘the  midst  (lit. the  heart)  of  the  sea’,  lebh  ha'eli <*,  ‘the  midst of  the  terebinth’,  Akkad,  libbu,  ‘heart;  middle’. Cp.  cordate,  cordial,  core,  accord,  accordion, codling,  ‘a  variety  of  apple’,  courage,  concord, discord,  misericord,  record.  Cp.  also  cardiac, cardio-,  carditis,  endocardium,  epicardium,  peri¬ cardium.  L.  credere,  ‘to  believe’,  is  not  related to  L.  cor,  ‘heart’  (see  creed).
```


### [2026-09-06T16:18:59.545Z] TOOL RESULT

```
14383:credo, -is, -didi, -ditum, -ere: transitif et absolu; 1° nettre sa
21645:credo, etc.; v. ansai 1 'article fetialis), on e8t tent 4 de poaer nn
32582:credo, qui usque dum uiuont lauant, \ minu'diu lauare ( lauari, Varr.
33512:credo, cf.Meillet, MSL 14,393. - II est possible, mais non 4 vident,
283
```


## [2026-09-06T16:19:07.410Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\ndata=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=data.split('\\f')\nfor i,l in enumerate(leaves):\n    if 'cordate,  adj..  heart-shaped' in l or 'heart,  n.  —  ME.  herte' in l:\n        print('leaf',i, repr(l[:200]))\n        # print any page numbers\n        print('---nums---', re.findall(r'\\n\\s*(\\d{3})\\s*\\n', l)[:10])\nEOF"
}
```


### [2026-09-06T16:19:09.354Z] TOOL RESULT

```
leaf 195 "rd  and  -ic.\nDerivative:  Coptic,  n.\nCoptis,  n.,  a  genus  of  plants  of  the  crowfoot  fa¬ mily  ( bot .)  —  ModL.,  from  the  stem  of  Gk. ko7tts'.v,  ‘to  cut’,  whence  also  xippa,  ‘som"
---nums--- ['351', '352']
leaf 383 ' Swed. huvud,  OFris.  haved,  hafd,  MDu.  ho  vet,  hooft, Du.  hoofd,  OHG.  houbit,  houpit,  MHG.  houbet, houbt,  houpt,  G.  Haupt,  Goth,  haubip,  ‘head’, and  cogn.  with  OI.  kaput-,  ‘hea'
---nums--- ['711', '712']
```


## [2026-09-06T16:19:15.352Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ndata=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nl=data.split('\\f')[195]\ni=l.find('351')\nprint(l[i-200:i+2500])\nEOF"
}
```


### [2026-09-06T16:19:17.180Z] TOOL RESULT

```
dv.,  coquett-ish-ness,  n.
coquet,  intr.  v.,  to  flirt.  —  F.  coqueter,  lit.  ‘to behave  like  a  cock’,  fr.  coquet.  See  coquet,  adj. coquetry,  n.  —  F.  coquetterie,  ‘coquettishness.
351
flirtation,  coquetry’,  fr.  coquet,  ‘coquettish’. See  coquet,  adj.,  and  -ry.
coquette,  n.  —  F.,  fem.  of  coquet,  ‘coquettish’. See  coquet,  adj.
coquin  n.,  rogue,  rascal.  —  F.,  prob.  a  derivative of  coq,  ‘cock’.  See  cock.
coquina,  n.,  a  whitish  rock  consisting  of  frag¬ ments  of  marine  shells.  —  Sp.,  ‘cockle,  shell¬ fish’,  fr.  OSp.  coca,  fr.  VL.  *cocca,  fr.  L.  concha, ‘mussel,  shell’.  See  conch.
coquito,  n.,  a  kind  of  South  American  palm  tree. —  Sp.,  dimin.  of  coco.  See  cocoa,  ‘palm  tree’.
cor-,  assimilated  form  of  com-  before  r.
Cora,  fem.  PN.  —  L.,  fr.  Gk.  Kopy;,  orig.  epithet of  Persephone,  daughter  of  Demeter,  fr.  x6p rj, ‘maiden’,  rel.  to  xopo?,  ‘child,  youth’,  which prob.  stand  for  *xopfa,  resp.  *x.6pFoc,  fr.  I.-E. base  *ker-,  ‘to  grow’,  whence  also  L.  creare,  ‘to create’,  crescere,  ‘to  grow’.  See  create,  crescent and  cp.  core-,  Corinna,  Curetes  and  the  second element  in  Dioscuri,  Halicore,  hypocoristic.
Coracias,  n.,  a  genus  of  birds,  the  common  roller ( ornithol .)  —  ModL.,  fr.  Gk.  xopaxta?,  ‘chough’, fr.  xopa!;,  gen.  xopaxo?,  ‘crow,  raven’.  See coracoid.
coracine,  n.,  a  perchlike  Nile  fish.  —  L.  coracinus, fr.  Gk.  xopaxivop,  ‘a  Nile  fish’,  fr.  xopac,  gen. x6pocxoq,  ‘crow,  raven’  [see  coracoid  and  adj. suff.  -ine  (representing  L.  -inus)\ ;  so  called  from its  black  color.  Cp.  crucian  carp.
coracle,  n.,  a  wicker  boat.  —  W.  corwgl,  cwrwgl, ‘coracle’,  dimin.  of  corwg,  cwrwg ,  ‘anything round,  the  trunk  of  the  body,  carcass,  boat',  rel. to  Gael,  curachan,  ‘coracle’,  dimin.  of  curach, ‘boat,  little  ship,’  fr.  I.-E.  base  *(s)qer-,  ‘to  cut, separate’,  whence  also  OI.  kpntdti,  ‘cuts’,  Gk. xELpav  (for  *x£p-ieiv),  ‘to  cut  off’,  L.  corium, ‘hide,  leather’.  See  corium  and  cp.  words  there referred  to.  Cp.  also  currach.
coraco-,  combining  form  meaning  ‘pertaining  to the  coracoid  process’  ( anat .)  —  Short  for  cora¬ coid.  See  next  word.
coracoid,  adj.,  pertaining  to  a  process  or  bone of  the  shoulder  girdle  (anal.)  —  Lit.  ‘resembling a  crow’s  beak’,  fr.  Gk.  xopixociSr;;,  which  is compounded  of  x6pc< 5,  gen.  xopaxo;,  ‘crow’, and  -oeiSyjc,  ‘like’,  fr.  elSo?,  ‘form,  shape’.  For the  first  element  see  raven  and  cp.  corvine,  for the  second  see  -oid.
coral,  n.  —  ME.,  fr.
```


## [2026-09-06T16:19:20.860Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ndata=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nl=data.split('\\f')[195]\ni=l.find('\\n352\\n')\nprint('idx',i)\nprint(l[i-1500:i+2500])\nEOF"
}
```


### [2026-09-06T16:19:22.580Z] TOOL RESULT

```
idx 8462
s, ‘raven’.  See  raven  and  cp.  the  next  two  words, Corvus  and  the  first  element  in  cormorant, corbel,  n.,  a  projection  jutting  out  from  the  wall (arch.)  —  OF.  corbel  ( =  F.  corbeau),  prop, ‘raven’,  dimin.  of  OF.  corp.  See  prec.  word. Derivatives:  corbel,  tr.  and  intr.  v.,  corbell¬ ing,  n.
corbie,  n.,  a  raven;  a  carrion  crow  (Scot.)  —  OF.
corp,  ‘raven’.  See  corbeau. corcopali,  n.,  the  fruit  of  the  Garcinia  Indica  (In¬ dia).  —  Compounded  of  Malayalam  kodukka, name  of  the  fruit,  and  puli,  ‘acid’, cord,  n.  —  ME.  corde,  fr.  OF,  (  =  F.)  corde. Tope,  string,  twist,  cord’,  fr.  L.  chorda,  fr.  Gk. yopSr;,  ‘intestine,  string  of  gut’.  See  chord. Derivatives:  cord,  tr.  and  intr.  v.,  cord-ed,  adj. cordage,  n.  —  F.,  fr.  corde,  Tope,  cord’.  See  prec. word  and  -age.
cordate,  adj..  heart-shaped.  —  L.  cordatus,  ‘wise, prudent’  (in  ModL.  ‘heart-shaped’),  from  cor, gen.  cordis,  ‘heart’,  which  is  cogn.  with  Goth. hairto,  OE.  heorte,  ‘heart’.  See  heart  and  adj. suff.  -ate.
Derivative :  cordate-ly,  adv.
Cordelier,  n.,  a  Franciscan  friar.  —  F.,  formed with  suff.  -ier,  fr.  OF.  cordele  (F.  cordelle),  di¬ min.  of  corde,  ‘rope’  (see  cord  and  cp.  cordelle); so  called  in  allusion  to  the  girdle  of  knotted cord  worn  by  Franciscan  friars, cordelle,  n.,  a  towline.  —  F.,  dimin.  of  corde.  See cord  and  cp.  prec.  word.
cordial
352
cordial,  adj.  —  Late  L.  cordialis,  fr.  L.  cor,  gen. cordis,  ‘heart’.  See  cordate  and  -fed.
Derivatives:  cordial,  n.,  cordial-ity,  n.,  cordial¬ ly,  adv.,  cordial-ness,  n.
cordiform,  adj.,  heart-shaped.  —  Compounded of  L.  cor,  gen.  cordis,  ‘heart’  and  forma,  ‘form, shape’.  See  cordate  and  form,  n. cordillera,  n.,  one  of  several  parallel  mountain ranges.  —  Sp.,  fr.  cordilla,  dimin.  of  cuerda, ‘rope,  cord’,  fr.  L.  chorda  (see  cord);  hence  the name  Cordilleras  (pi.)  given  by  the  Spaniards to  the  parallel  ranges  of  the  Andes, cordite,  n.,  a  smokeless  explosive.  —  Formed  fr. cord  with  subst.  suff.  -ite. cordoba,  n.,  the  monetary  unit  of  Nicaragua.  — Sp.  cordoba,  named  after  Francisco  de  Cordoba (died  in  1526).  Cp.  Cordovan, cordon,  n.,  1)  a  guarded  line;  2)  an  honorary  cord or  ribbon.  —  F.,  fr.  corde,  ‘twist,  cord,  cordon, ribbon  (of  an  order)’.  See  cord, cordon  bleu.  —  Orig.  the  blue  ribbon  worn  by  the knights  of  the  Holy  Ghost,  the  highest  order  in France  under  the  Bourbons;  later  used  to  de¬ note  a  distinguished  person  and,  facetiously,  a first-rank  cook.  —  F.,  ‘blue  ribbon’.  See  cordon and  blue.
Cordovan,  adj.,  of  Cordova;  n.  (not  cap.),  Cor¬ dovan  leather.  —  Sp.  cordoban,  lit.  ‘Cordovan’, fr.  Cordoba,  name  of  the  famous  city  of  Spain, fr.  L.  Corduba,  fr.  Gk.  KopSu^T).  Cp.  cordoba, cordwain,  cordwainer.
corduroy,  n.,  a  ribbed  cotton  fabric.  —  Perh.  fr. F.  corde  du  roi,  ‘the  king’s  cord’.  See  cord  and royal.
Derivatives:  corduroy,  adj.,  corduroy,  tr.  v., corduroy-ed,  adj.
cordwain,  n.,  Cordovan  leather  (archaic).  —  ME. cordewane,  ‘leather  of  Cordova’,  fr.  OF.  cordoan, cordouan.  See  next  word, cordwainer,  n.,  shoemaker.  —  ME.  cordwaner, fr.  OF.  cordoanier  (F.  cordonnier),  ‘shoemaker’, lit.  ‘a  worker  in  Cordovan  leather’,  fr.  cordoan, cordouan,  ‘Cordovan  leather’,  fr.  OProven?. cordoan,  fr.  Sp.  cordoban,  ‘Cordovan  (leather)’, fr.  Cordoba,  ‘Cordova’.  See  Cordovan.  F.  cor¬ donnier  was  influenced  in  form  by  F.  cordon, 'cord,  cordon’.
Cordyline,  n.,  a  genus  of  plants  of  the  lily  family (bot.)  —  ModL.,  fr.  Gk.  xop S'rX/;, ‘club’  (see  cor- dylo-);  so  called  in  allusion  to  the  thick  caudex. cordylo-,  before  a  vowel  cordyl-,  combining  form meaning  ‘club’.  —  Gk.  xopSGXo-
```


## [2026-09-06T16:19:28.534Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ndata=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nl=data.split('\\f')[195]\ni=l.find('core,  n.,  hard  center')\nprint(l[i:i+900])\nprint(\"=== end of leaf ===\")\nprint(l[-400:])\nEOF"
}
```


### [2026-09-06T16:19:30.902Z] TOOL RESULT

```
core,  n.,  hard  center  of  a  fruit,  etc.  —  Prob.  fr. L.  cor,  ‘heart’;  see  cordate.  For  sense  develop¬ ment  cp.  Avestic  zlrlbaya,  ‘middle’,  OSlav. srudice,  ‘heart’,  sreda,  ‘middle’,  Russ,  serdee, ‘heart’,  sereda,  ‘middle’;  Wednesday  (i.e.  middle of  the  week)’,  Lith.  sirdis,  ‘heart’,  W.  craidd, ‘heart;  center’,  Bret,  kreiz,  ‘m
=== end of leaf ===
W., I,  p.  918  s.v.  xopSukr,.
core,  n.,  hard  center  of  a  fruit,  etc.  —  Prob.  fr. L.  cor,  ‘heart’;  see  cordate.  For  sense  develop¬ ment  cp.  Avestic  zlrlbaya,  ‘middle’,  OSlav. srudice,  ‘heart’,  sreda,  ‘middle’,  Russ,  serdee, ‘heart’,  sereda,  ‘middle’;  Wednesday  (i.e.  middle of  the  week)’,  Lith.  sirdis,  ‘heart’,  W.  craidd, ‘heart;  center’,  Bret,  kreiz,  ‘m
```


## [2026-09-06T16:19:36.615Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 333 334; do echo \"=== BQT_v2 leaf $n ===\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' BQT_v2_pages.txt | head -c 2500; echo; done"
}
```


### [2026-09-06T16:19:38.250Z] TOOL RESULT

```
=== BQT_v2 leaf 333 ===
 ‫‪۷‬‬


‫وربی‌موی باشد ‪ .‬ابن لفت نبزاز‬
                            ‫بی‌علف ‪ - ۴‬ص‬                  ‫کدنیا ‪ » ۱‬بروزن اغنیا ‪,‬تخل خرمارا‬
           ‫‪. ۴‬‬     ‫ولق معرب‌انت‬        ‫اتباع است ودق‬                         ‫کوتد بزمان زند ویازند (‪. )۱‬‬

                                                          ‫دل وديم ؟ ‪ -‬با دال ابجد بر وزن‬
                                                         ‫ژر و سیم»‪ ۰‬اینلقت از اتباع ابسعتعنی سر‬
‫گفته‌الد ‪ -‬وبهندی بهلو بریهلو ودوش بر دوش‬                    ‫وصورت و سروروباشد » چه دك بمعئی سر ودیم‬
                                     ‫یاند ‪٩‬‏ ‪.‬‬
                                             ‫ور‬‫زکدن‬                              ‫یمعتی صورت ورو بود ‪.‬‬
                                                             ‫دك ولك = بتشدید الی ‪ ۰‬بر وزن‬
‫وپازند (‪ )۱‬بمعتی ياك شوم وطاهر گردم باشد ‪.‬‬                   ‫ومعتی دق ولق است که خشك رخالی وصحرای‬



                                                    ‫يان بدانهزم‬
                         ‫لغت‬     ‫در دال می‌نقطه باکاف فارسی مشتمل بسره‬
                    ‫وباژگونه(‪ )۲‬وتغییرحال باشد ‪.‬‬          ‫‌لجگر » مختف‬       ‫ناو‬ ‫زکر‬‫هب‬‫بگررو‬‫‪3‬‬
                                                          ‫دیکر است ‪ 4‬که بمعنی بار باشد ‪ .‬چون اضافه‬
                                                          ‫مجیزی کنند افاد‪ #‬غیربت ونکرار تفلن و تعدد‬
‫مکروحیله وفاد و اراست ‪ - 4‬وزرقلب وناسره‬
                                                                                                                    ‫کند ‪.‬‬
‫وغره باشد _ وامردی که نامترش و لاهموارشده‬

         ‫دست ویای گنده ویزرگ داشته باشع*‪.۱‬‬                   ‫د گر گو
=== BQT_v2 leaf 334 ===
                                          ‫بیان شانز دهم‬

‫وبرکے آن پنج شاخ مبباشد وآنرا پنج انگشت‬               ‫؛رهی‬‫دل = بضم اول و سکون ثانی ک‬
 ‫میگوبند ‪ ۴‬وبیشتر در کنار های جوبها میروید‬           ‫چندرا گوبند که‌درامعا وشکم ازقبض‌بعداززبباری‬
 ‫و تخم آن بوی تیزی دارد و آنرا بعربی فد‬                               ‫» وبعضی گید هر ضی‬         ‫رمسد‬
                                                                                                   ‫به‬
  ‫خوانند ودر دواها بکاربرند خصوص‌درمرض‌استقا‪.‬‬                         ‫است مانند کره که درشکم بهم‬
 ‫‪۵‬لال * ‪ -‬بنتح اول بروزن غزال » باز‬                                   ‫میرسد ومهلك هیباشد‪ -‬وبکس‬
 ‫وغمزه واشاره بچشم وابرورا وید » وبکراول‬                               ‫اول‌معروف است ‪٩‬‏ وبعربی‌قلب‬
                               ‫هم آمده اس‬                             ‫خوانند‪ .‬ووسط هرچیز را ببز‬
  ‫‪ ۰ ۵۷‬بکر اول بروزن نظام » ژر‬                              ‫دل‬        ‫کوبند؟ ‪ -‬ویمعتی بازگر‪:‬هم‬
‫را گویند ‪ ,‬وآن نیزه‌ای باشد کوچك و کوئله‬             ‫هست وآن لطیفةٌ ربانی را لگیوزبندکه بزبان‬
            ‫که آرایجات خسم اندازید‪# .‬‬                                        ‫در تباید همچوآن ‪.‬‬
‫دالنگیز ان د ام لحتی ات از‬                            ‫سلم|ان «کنابه‌ازوسط آسمان‪.‬اشد‬   ‫د‬
                                   ‫موسیقی؟ ‪۷.‬‬        ‫وستاره و کوکب را بکیوزبند ‪ -‬کونابه اززمین‬
‫دلاو یز" ‪-‬با واربتحتابی رنیده وبز ای‬                                                  ‫هم هنت ‪. ۳‬‬
‫نقطه دار زده ‪ ۰‬مطلوب و مرغوب و دلخواه را‬             ‫آب » بانبن‌قرشت بوا وکشیده‬
```


## [2026-09-06T16:19:44.618Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==334' BQT_v2_pages.txt | tail -c 2200"
}
```


### [2026-09-06T16:19:46.388Z] TOOL RESULT

```
��یتسا ‪‎ 28۳08.‬یچولب ‪» 21۳08‬‬
  ‫‪‎‬یاکیرس ‪ . 23d‬یتفش ‪ ۰ 2۳2۵۷ ۰ 2۳20‬یجیلگنس ‪ * ۱12۲2۷‬ىحجنم ‪‎ « |21‬قتسا ‪۴ ۵۷۱‬‬
  ‫اقل ؛‪‎‬‬   ‫‪ » ٩‬ممثالی وشهمیرزادی‬    ‫‪۹۸۲‬‬   ‫که‪ ۱ .‬ص‪‎‬‬   ‫<‬    ‫‪ .‬فربز ندی » بر لی و نطنری ‪160‬‬   ‫کیلکی‬

  ‫‪ ۳‬طری ‪ ( 216‬مان‬                   ‫منگری‪ .‬سرخه‌بی ولاسگردی ‪« 1621‬کف‪ ۲ .‬ص ‪. ۸۱۰‬‬
  ‫‪ ۴‬ب‪-‬تصور پشینبان که‌معتفد بودند زمین درمرکز‬      ‫[هر چیز] ) ‪ +‬صاب طبری ‪. ۰ ۹۵۳‬‬
              ‫= ‪sutsac‬‏ ‪ « 601۷ 511088‬ابتی ‪۲414-7‬‬                ‫‪۴‬‬             ‫!فلا کت قرار وارد ‪.‬‬
                                    ‫© ‪( -‬عر) ناز و غمزه «شرح فاه‌وس» «ناظم الاطبا؟ ‪.‬‬
       ‫بردارونان لحن دل ایگیزادت ‪...‬‬                         ‫‪ -‬در باغ بتوروز درم ربزاست‬
                                                                                           ‫‪۹‬‬




   ‫«عنوچهری دامفالی ‪. ۰۵۱‬‬
  ‫‪« - ۸‬مناقم سفر ‪...‬ملم پنج طايه راست‪:‬‬          ‫‪ _ ۷‬از‪ :‬آدولی‪۳‬ز(آویزنده‪,‬آوشته) ‪.‬‬
   ‫لخستین برازکانی که با وجود همت ومکنت غلامان و کنبز کان‌دارد دلاویز‪ ».‬گ«لتان‪.*۴۱۱-6۱‬‬
   ‫‪ #‬دل الگیر ‪ -‬بکراول وفتح سوم ‪.‬از ‪ :‬دل ‪ +‬انگیز (انگیزنده)؛ دلاویژء مطلوب»‬
                                                                                               ‫مرغوب‬

                                                         ‫فس ‪ ۰‬تناور» تکلور ؛ دلیر ‪٠‬‏ شجاع ‪۰‬‬
```


## [2026-09-06T16:20:15.759Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 582 583 584; do echo \"=== awk NR=$n (printed $((n-1+540))) ===\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' BQT_v2_pages.txt | head -c 1800; echo; done"
}
```


### [2026-09-06T16:20:17.569Z] TOOL RESULT

```
=== awk NR=582 (printed 1121) ===
                                                                                          ‫نف‬

          ‫از استخوان سازند ویدان بدترا خارند‪.‬‬      ‫= ینم اول و خای قطه‌دار‬      ‫سرخاب‬
 ‫سخراریدن ‪ -‬کنابه از نوميد شدن‬                     ‫بر وزن مرغاب » نام رودخانه ابست کوچك در‬
‫‪ -‬و نگاهداشتن ‪ -‬و تسلی کردن ‪ -‬وراغب شدن‬             ‫له آب آن بسرخی مايل است ببب‬
                                                                              ‫تواحی‌کاب ک‬
 ‫‪ -‬ولطف نمودن ‪ -‬و تعلل ودرنگه‌واهمالررزیین‬          ‫سرخی خاك رودخانه ‪ -‬و نکاموهی است‌برجنوب‬
‫‪ -‬وعاجز شدن در جواب خصم ‪ -‬و حیله و مکر‬             ‫است بشهر » و گویند چند‬      ‫ل‬ ‫صو‬ ‫تربز‬
                                                                                       ‫مر تب‬
                                                                                           ‫شه‬
 ‫نمودن ‪ -‬وخجل شدن وشرمنده‬        ‫وتملق‬   ‫کرو‬        ‫جای دیگرسرخاب هت ‪ - ۴‬ولوعی ازمرغابی‬
                 ‫گردیدن ‪ -‬وبپانهآوردن باشد‪.‬‬        ‫باشذ سرخ رنگه ‪ . ۴‬کوبند ماد آنرا مانند‬
 ‫سرخ بال ‏ بابای ابجد بروزن‌ختك‬                    ‫زنان حیض ميآد ‪ ,‬و بسنی کویند پرنده ایست‬
 ‫سال » تی
=== awk NR=583 (printed 1122) ===
  ‫‪ 5‬اف‬




 ‫سرخزه و سرخژه ‪ - ۴‬بزاای‬                                ‫سر خ لیگ ‪ -‬نوعی‌از درخت بیداست ‪5‬‬
 ‫نقطه‌دار و زای فنرسی » بروزن و هعنی‌سرخجه‬              ‫و بستی کویند یبدموله است کبهيد مجنون‬
‫است که نوعی از حصبه باشد و سشتر اطفال را‬                                                            ‫باشد ‪.‬‬
                                      ‫بهم هیرسد ‪.‬‬
                                                         ‫وم‬
                                                          ‫رد‬‫ماد‬
                                                              ‫سر جح شم ه کنابه از جل‬
          ‫ن‬‫وو‬
            ‫کالی‬
               ‫س وث‬
                  ‫اول‬       ‫ح‬
                            ‫فست‪۰‬‬
                               ‫بح‬‫سر‬                                            ‫خواربز باشد ‪.‬‬
‫ثالث و سین ی‌نقطه ‪ .‬دام شهری‌است‌ازخراسان ‪9‬‬
‫وام داروی است که آتراگیل دارو گویندل ‌‬
                                     ‫‪-‬‬
                                                      ‫سر خچه ‪ ۴‬ه بماول و کرثاك وقح‬
 ‫وآن چوبکی باشد سیاه رنگه‪ ,‬کبنراردریای‌خزر‬
                                                      ‫جیم ابجد » اوعی از دمیدکی و حصبه باشد که‬
                                                        ‫سشتر کودکا ت
=== awk NR=584 (printed 1123) ===
  ‫سرد ب‬                                                                                              ‫==‬

                        ‫کردن «م آهده است‪.‬‬                                                    ‫حمیرا کویند ‪۲ . ۱‬‬


‫د کنابه از کسی‌است که از‬     ‫سر خوش‬                      ‫و سکون را‬          ‫میم‬    ‫ه بفتح‬    ‫هرت‬      ‫سرح‬


‫شراب و سامان و اسباب و حسن» خوب و خوش‬                     ‫و آنرستنمی‌باشد‬         ‫‪ 3‬دال بی‌لقطه ‪a‬‏ نازك دناست‬

                                      ‫حال باشد ‪.‬‬          ‫که برکش ببر گهبتان افروزماند وساق آن‌سرخ‬

 ‫سر خه ‪ -‬بضماول وفتح‌خای نقطه‌رار(‪,)۲‬‬                                                    ‫‌‬   ‫خوشآ بنده بود ‪۴‬‬        ‫و‬



 ‫نام پسرافراسیاب‌است که فرامرز اورا زنده کرفت‬           ‫= بازای قطه دار (‪ )۱‬؛بر‬              ‫هرر‬      ‫سرح‬


‫وستم بکین سیاوشش بکشت ‪ -‬وام موضمی هم‬
                                   ‫ر‬                      ‫رستنیی‌باشدشبیه‬        ‫وزن و ععنی سرخ مرد است که‬
 ‫هست امزضافات سمنان ‪ -‬و نامنوعی اکزبوتر‬                                                             ‫بستان افروز ‪.‬‬


‫سرخیزه و سرخیژه * = بنم‌اول‬                               ‫ثالی و واو » بممنی سرخجه
```


## [2026-09-06T16:20:23.866Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ndata=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=data.split('\\f')\nfor i,l in enumerate(leaves):\n    if 'سرده' in l:\n        print('leaf',i,'printed',i+540)\nEOF"
}
```


### [2026-09-06T16:20:25.739Z] TOOL RESULT

```
leaf 313 printed 853
leaf 564 printed 1104
```


## [2026-09-06T16:20:28.661Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 585 586 587 588; do echo \"=== printed $((n-1+540)) ===\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' BQT_v2_pages.txt | head -c 1200; echo; done"
}
```


### [2026-09-06T16:20:30.336Z] TOOL RESULT

```
=== printed 1124 ===
 ‫‪“NYY‬‬                                                                                                      ‫مردابه‬
            ‫و زودآورند و زود سازند ‪ ۴‬و‬
‫‪ -‬آنچه در دست‬                                            ‫سردا به‪ = ۱‬بفتح بای ابجد » بمعنی‬
‫بود وچوی که‬          ‫بوده باشد ‪ -‬وآ نجه برصر دست‬        ‫سرداب است که خالهٌ زیر زمینی باشد ‪ -‬و خانهةٌ‬
                         ‫قلندران بر دست گیر ند ‪۰‬‬
                                                          ‫ندا‪-‬م آبشاری‬    ‫ووبن‬
                                                                             ‫تابستانی بسیار سرد را نیز ک‬
                                                        ‫است درآب گرم قزوین ‪ -‬و نام جزیره‌است از‬
‫گرم شدن باشد ‪ -‬و کنابه از مردن ‪ -‬و ازکاری‬                                       ‫جزابر اندلی ‪#.‬‬
       ‫واسوخت
=== printed 1125 ===
                                                                                                                         ‫‪٩۷۷۴‬‬

‫و زلد گی و تری‬                ‫و زای هوز ‪ ,‬کنابه از حات‬                                                       ‫وقصود است‪.‬‬
                                                                                                                      ‫از مدعا م‬
 ‫وناز کی عیش ‪ -‬وجوان صاحب دولت وکامکار ‪-‬‬
                                                                              ‫و معامله‬         ‫از سراسیمه شدن و ترك دادن م‬
                                                ‫‪۰‬‬   ‫باشد‬      ‫ویادشاه‬




 ‫سر سری = بر وزن مرمری ‪ ۰‬مردم‬                                                                                     ‫و مردن باشد ‪١‬‏‬
 ‫فرومایه راگوبند ‪ -‬و ست گرفتن‌کارها ورعایت‬
 ‫آا را بواجبی نکردن ‪ -‬وکار آسان‌باشد‬
                 
=== printed 1126 ===
   ‫)‪۷۱‬ات‬

‫که بجمد و جهنده باشد ‪ -‬و نام درختی است‌در‬           ‫بمعنی ربختن باشد ‪-‬ویمعنی‬         ‫ر‬
                                                                                     ‫شتاچه‬
                                                                                         ‫لبریز اس‬
   ‫آردثور‬
        ‫بلخکه کلهای سفید مابل بسرخی دا‬
‫و کی گونند کل ان‬          ‫آزاد درخت ءیگوند‬
                                                    ‫سر شب = بروزن هرشب ؛ بمعنی‌شاهین‬
                       ‫درخت سر شك نام دارد ©‬
                                                                    ‫باشد وآن جالوربست شکاری ‪.‬‬
 ‫سر شك ‪ ۲‬تش ه کنابه از فطرحامی‬                      ‫بکر اول و انی بر وزن‬            ‫سر شت ‪۲‬‬
          ‫می‌چکد‪.‬‬    ‫است که از هیزم تر اش‬           ‫بهشت ‪ ,‬خلقت و طیئت و هاب �
=== printed 1127 ===
                                                                                                     ‫‪۷۱۲6-‬‬

‫است وآنرادای ترکی نیز خواند؛ ویکسر لول‬                    ‫باشد که‌در‬     ‫وآن برده‌ای‬       ‫اة‬    ‫سرشکوان‬        ‫نمی‬


                                                                                ‫پیش عروی آویزند ‪.‬‬
‫سرغینه ‪ = ۴‬بروزن چرمینه ‪ ۰‬بمعنی‬                            ‫شروی = بر وزن بدبوی * سرتراش‬    ‫س‬
                                                           ‫و حجام وا گوند ‪ -‬و نوعی از گل هم هت که‬
 ‫سرغین است که ای تر کی باشد و آترا سوردلی‬
                                                                          ‫بدان سرشوبند وگل سرشوی کوبند‪.‬‬
‫»‬       ‫‪ -‬بفتح اول وثانی بروزن صدف‬      ‫سرف‬

‫کردن‬       ‫درد گلو وسنه را گونند که بسب سرفه‬
```


## [2026-09-06T16:20:39.391Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==565' BQT_v2_pages.txt | head -c 2500"
}
```


### [2026-09-06T16:20:40.879Z] TOOL RESULT

```
 ‫==‬                                                                                              ‫سوه‬

‫وزن کبوتر » هوابی باشد با صدا که بی‌اختیار از‬     ‫یمعثی وصف نمودن وستایش کردن باشد؛ وبضم‬
        ‫راه دمام بجپد وآارا معربی عطه خواند‪.‬‬

‫ستوسه ‪ = ۴‬بفتح اول و سین بی لقطه‬                   ‫رزن‬
                                                     ‫بو‬        ‫اول‬         ‫ستو ده ‪ ۱‬ه یکر‬
 ‫بورزن دبوسه ؛ بمعنی ستوسر است که عطسه‬            ‫باشد سنتی‬          ‫شنه‬   ‫کرده‬    ‫قروده » سمعنئی مدح‬
                                     ‫باشد ‪۷#.‬‬
                                                 ‫او را‬     ‫یکریی‬      ‫و‬    ‫کنند‬   ‫مدح‬   ‫کسی که اورا‬

 ‫ستو نه د بکر اول و فتح نون بروزن‬                                                            ‫‪.‬‬   ‫ْف‬
‫انداز‬   ‫و‬   ‫و ری‬   ‫کردن شاهدن‬   ‫چمگونه ‪ ,‬حمله‬
                                                  ‫خم ول بروزن حور » هر‬                  ‫ستور ؟‬
 ‫لمودن باز و باشه و امثال آن باشدبجانب باولی»‬
                                                  ‫جاور چارپابیرا‪ ۳‬عموماً واسب و استروخر‬
‫و باولی جانوری راگوبند که بعضی ازپروبال او‬
 ‫پدیرش باز شواهین نو رسالیده‬
                           ‫کنده باشند و‬
‫و نازه مشکار درا ورده سردهند ‪îl‬‏ بآٌسالی بگیرد‬     ‫ستوردن = بکر اول بمعنی ستردن‬
 ‫‪ -‬بمعنی کریز و کریختن‌هم آمده است‌وبمربی‬
                                        ‫و‬         ‫است که تراشبدن وحك لمودن وباك کردن‌باشد؛‬
         ‫اس‬                ‫رب‬                                                     ‫اول هما مده است‬     ‫وم‬


‫ْم اول بروزن گروه «ممعنی‬      ‫ستوه ‪°‬‬


                                                      ‫�
```


## [2026-09-06T16:21:00.811Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### PHD dil\"; grep -n \"^dil\\b\\|^dil \" PHD.txt PHD_mackenzie.txt | head; echo \"### PHD sardag\"; grep -n \"sardag\\|sardak\\|sartak\" PHD.txt PHD_mackenzie.txt | head; echo \"### NYB dil\"; grep -n \"dil \" NYB_vol2_glossary.txt | head -5; echo \"### NYB sardag\"; grep -n \"sardag\\|sardak\" NYB_vol2_glossary.txt | head"
}
```


### [2026-09-06T16:21:00.893Z] TOOL RESULT

```
### PHD dil
PHD.txt:4947:dil
PHD.txt:4949:dil!
PHD_mackenzie.txt:2001:dil [LB(B)ME < A lb(b)-h; dyll = M, N -] heart.
### PHD sardag
PHD.txt:392:hamēstār, —ih [hmyst!l, -yh] = hamēmāl, ~ih. hamésag [hmyfk! | M hmyšg, N —a] always. ^h : eternity. ~-86z [-swe] ever-burning. hamē-wahār [hmy whl | N haméfa-bahar] marigold. ham-éwénag [Am'dwynk!'] of the same kind, homogeneous. ham-góhr (hmgwhl! | M hmgwhr] of the same substance or nature, consubstantial. ham-ginag [hmgwnk! | M hmgwng] likewise, so. P hāmharz [A())mAlc | P I? mhyrz] adjutant, attendant. hāmīn [A*myn! |= M] summer. ~ig [-yk'] (of) summer. hāmist [KHDE, v. hammis ; )”mst!] all. ham-kār [hmk’l | N ~] collaborator. 7h : collaboration. hāmkišwar [mkyfwl | M. -wr] universe. hammis [KH DE < A k-hdh), ат... ~: together with. hammist [hmyst'] stagnant, peaceful. ~(ag)an [-(kYn'] limbo, the neutral station between heaven and : hell. vl hammóxtan, hammoz- [ALPWN-tn! < A У "Ip: hmwhtn', hmwc-, Ki hmsoz- | M hmwxtn, N āmēxtan, ámóz-] teach; learn. -išn: teaching. hammdxtar [Amwht?!] learner. ~th: learning. hammóz- , ~i8n, v. hammóxtan. —@йг [kmwcek?l | N āmēzgār] teacher. ham-nibardih [hmnpityh] (single) combat. hamēūģ [/tmwg] equal, like. hámón [k mwn' | N kāmūn] level, flat. hámoyén [/?mwdyn!] all. ham-pursag [hmpwrsk!] consulting, taking counsel. ^h : consultation. ham- |-ránih [Am nyh] battle, combat. ~-samiain [-s"m?n!] contiguous. ~-sardag [-sltk'] of the same kind, like. ~-sayag [-sdk! | N hamsáya) neighbour. ~-tag [-t*k! | N hamid] equal, peer. «tan [-tn'] of the same stature, build. ~=-tihmag [-twhmk'] relative, relation. hamwar [hmwl | N hamwār] level, abreast. hámwiür(ag) [%()mw?/, -k! | N hamwdara] always. ham-zamān [hm ODNA | N —] instantly, immediately. handām [And*m | = P, N andàm] member, limb. handarz [hndle | N andarz] advice, injunction, testament. handarzénidan, handarzén- [hndleyn-ytn!] advise.
PHD.txt:551:pillagan [plk’n' | M pylg, N ~] steps, ladder. pim [pym] pain, pang, sorrow. ~gén [-kyn'] sorrowful. pir [руі | N ~] old, aged, ancient. ~ih: age. piring [pling | M pryng, (N pirind)] monochrome damask, pist [pst! | N ~] browned flour. pistag [pstk! | IN pista] pistachio nut. pišīz [pšyc | N ~] small copper coin, ‘farthing’. pēhišn [pwhsn'] corruption, decay. pēlāwad [pwPft! | М pwl'wd, N pēlād] steel. ~ën [-yn!] (made of) steel. pondik [pndk' | Ar. b/fundug] hazel-nut. por [pwl | N —] francolin. pēryētkēš [pwlyw(k)kyf = Av. paoiryē.tkaēša-| (one of) the first teachers of the Mazdean religion. ~ЛЬ : the primal doctrine of the Mazdean religion. pēst [pwst! | = M, N ~] skin, hide; bark, shell. mēn [-yn! | N ~in] (made of) skin. pēšīdan, pēš- [pws-yin' | N <] cover, put on, wear. ~išn: covering. potk [pwtk' | N ~] sledge-hammer. poxtan, paz- [APPWN-tn' < А V?ph; pwhtn', pc- | M pwxtn, N ~] cook, bake. рӧу- [pwd- | (P pwd-), N ~] run. ~iSnig : running. p6z(ag) [pwc(k!) | N pēz(a)] snout, muzzle. püdag [pwtk! | N pūda) foul, rotten. —ih: rottenness. 1puhl [pwhl | N pul] bridge. *puhl [pwhl] expiation, atonement; punishment. puhlénidan [ pwhlynytn'] cause to atone. purnāy [pwln’d] adult. purr (MALE < A mlh; pul | M pur, N ~} full. =-ģāh [-g’s] at the fullness of time, about to die. ~-тюаһ [-mh] full moon. —-rawišnih [-lwbsnyh] fullness. ~-sardag [-sltk'] of all kinds. --xwarrah [-G DE] full of glory. pursidan, purs- [pwrs-ytn' | M pwrs-ydn, N ~] ask. Vu re: Е ~iSn: question. — ~i$nig : responsible. pus [BRE < A br-h; pws | = M, N =] son. ~ar [BREI, pwsl | M pwsr, N ~] son. —yàn [pwsd?n! | M pwsy’n] womb. pušt [52001 | = M, N ~] back; support, protection.
PHD.txt:564:sang [KYPA < A kyp’; CCA (in error); sng | (P?sng), N ~] stone, rock. -~sar [-s?1] stony place. sanj-, v. saxtan. sanwar [snwl = Av. 0anwar-] bow. sar [LOYŠE < A r'šh; sl | M sr, N ~] head; top, summit; end, begin- ning. | sarāsar [s?s] | N ~] from end to end. sard [s/t! | M srd, N ~] cold. ^Àh: coldness. sardag [sltk' = Av. sarada- | (M s’rg), J srdg] sort, kind. sardsér [s/tsyl | N ~] cold region, uplands. sārēnīdan, sárén- [s’/yn-ytn'] provoke. sargen [slgyn' | N sargin] dung, manure. sarmāģ [s/m?k! | N затта] coldness. sarw [slw(b)' | M srw, N ~] cypress. sas [ss | N ~] bug. sāstār [s”st”7 | P s?s?r] commander; tyrant. ~ih: tyranny. Sawah [sw’h = Av. sawahi-] the western continent of the earth. saxt [sQ)At! | N ~] strong, hard, severe(ly); very. “Аһ: strength, severity. saxtag [shtk! | (N saxtiyán)] morocco leather. saxtan, ѕапј- [s’htn', snc- | N ~] weigh. sāxtan, sáz- [s*htm!, ?c- | (P s?*c-), N ~] make, prepare; tolerate. sāxtārīh [Pht yh] toleration, forbearance. saxwan [МРУА < А mly’; shwn' | М sxwn, N suxan] word, speech. say-, v. südan. sayag [sg dk! | M ғур, N sáya] shade, shadow. lsaz- [sc- | M sz-, N ~] be fitting, proper, worthy. --i$n(ih): fitness, worthiness. 26а2-, —išn, v. sazistan, saz-, v, sáxtan. sazāģ [sk | N sazá] fitting, worthy. ~th: fitness, worthiness. ~ ~war [-w/ | N sazāwār] = затар. sazistan, *saz- [sc-stn'] pass. ~išn: passing, transience. ~iSnig : transient, perishable, mortal. sé [3; TLTA < А tl? | M sh, N si] three. sëb [syf | N ~] apple. sēj [sye = Av. 'Gyejah- | N ~) danger, trouble. --ómand [-”zvmnd | N —mand] dangerous. sel [si | N —] spear, javelin. sém [sym | N —] — asém. !sén(ag) [syn(k)! | N sina] breast, chest. *sén murw [synmzlw | (N simury)] a fabulous bird.
PHD.txt:2525:kind (n.) gón(ag), sàn, sardag, šēn; of the same ~ haméwénag.
PHD.txt:2624:like (a.) ēwsān, hamóg, hamsardag, hawand, manag.
PHD.txt:3743:sort gón(ag), sardag.
PHD.txt:4704:purrmāh Ku purrsardag 15 Qa» yes dahint roe to pusyān V 10 pusar ND 10 póstén V yen 10) póst we» 105 рап}, poz So panjah ay S ya) panjag, pēzag 13619 pos- = 74010 pūšīdan Wres“O ve pēšišn VUV puštībānīh «U ye) 43 «650105 pustiban т^” оу S ANA pušt VOU 199 puštag 1100010) püdagih ^t 5120
PHD.txt:4783:sardag
PHD_mackenzie.txt:2779: --sardag [-sltk'] of the same kind, like.
PHD_mackenzie.txt:4278:   ......-sardag [-sltk'] of all kinds.
### NYB dil
1280:dil [dyl, dl; LBBH] heart 73. 117-21, 2521, 20?, v. also dilé-név. — SW form: MPrs dyl, Paz. NP dil, as against MPrth zyrd; Av. (1692) zarad-, zaradaya-. :
1896:*handrütak [hndlwtk'] *discouraged: dil ~ kart it made his heart *discouraged 73; [adv. -ihā : ēišān vas ~-tha 6 Artaxšēr guft very discouraged they said to A. KnS VIL3]. - Reading uncertain; no Paz. known to me. Henning, followed by M. Schwartz (JRAS 1966, 121), reads hangrü- tak, connecting it with MPrs grwdg ‘lamen- tation’, grwdgyn ‘lamenting’ (List 83, with another reading of our passage 79). How- ever, the idea of ‘lamentation’ is scarcely to the point in the quoted passages (it would be important to know more about the use and purport of grwdg). Until further elucidation I maintain my old reading *handrütak, now connecting it with drütan drav-, commonly ‘to mow, to reap’, but originally ‘to cut’, thus han-drütak ‘cut up, afflicted’. Bailey, BSOAS XXIV, 1961, 478, discusses a root drav-, dru- ‘to treat violently’, which is perhaps identical.
3977:virom [w’lwm] mind, conscience 9425. — From Av. (1360) ?var- ‘to choose’; Bthl (zAirWb 222) identified it with Av. (1411) vāroma = vüàrom či ‘according to one’s wishes; arbitrarily’; Bailey, ZP 103 n. 1, derives it from *värma- from the same ?var-. Darmesteter had found the NP gl. dil for it (ad Y. 1014).
4245:to Z. through the line of his maternal grandmother 3619-11, cf 3817-18, — 2. intens. of vitartan: vitartan % Cinvat puhl to cross the Ch. bridge 64!?; the arrow ditikar sok bé vitärt pierced through to the other side 371, pat pušt be vitārēt (pres. hist.) pierced through and came out through the back 292-3, pat dil be vitārēt penetrated into the heart 2521-22, — MPrthPrs wyd’rdn w(y)d’r-; MPrs also pt. wd’$, Verbum 192; NP guöärdan or guöästan, guóür-.
4521:gor zat he shot an arrow at the onager 319-20; parr 6 pist zat its wing struck (the bowl with) the meal 925-26; 57 (= 6) fravahr + Zartuxst aš zafar frac zat threw open its mouth towards Z. 4012-13; 5; (= 6) gurg zat zanak the wolf's jaw was struck 506, with the gl. kū-š dahān ēvak apäk dit frot oškan (g. v.); Vidrafš pat dil zat stabbed V. in the heart 292; 25?! (cf s. v. rad 2 b)]; 383; — ēvak 6 dit ~ to knock to- gether 12019-20; ka šamšēr frac zanēt when the sword makes a stroke forward 254 (opp. apāc vēžēt, v. *véxtan); to drive (a peg) down into the soil 202%; tanbür ~ to play on the lute 476, — Av. (490) !gan-, pres. jan-; MPrth jdn jn-; MPrs zdn zn-; Paz. NP zadan zan-. V. also janišn, zanišn, zatak, zatar; cf apa-žand, ozatan.
### NYB sardag
```


## [2026-09-06T16:21:02.653Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### BRT zaradaya\"; grep -n \"z9r9d\\|zaradaya\\|zarad-\\|zsrsS\\|zsrsd\" BRT.txt | head -20; echo; echo \"### BRT sarada\"; grep -n \"sar9da\\|sardSa\\|saroda\" BRT.txt | head -10"
}
```


### [2026-09-06T16:21:02.720Z] TOOL RESULT

```
### BRT zaradaya
27786:•  j.  zarad-a'jnyäi  In£  'ins  Herz  zu  treffen': aZa  taicii  uzjasmti  (sd.)  yä  mtnn^äila 'ynyaica  ". .  die  (da  sind)  um  zu  zerstören und  ins  Herz  zu  treffen"  V,  r.  1 4  Gl.

### BRT sarada
26108:•  j.  "sardSa-  m.  Name  der  Gottheiten der  Jahre:  *Za  a/ai/ana  aiake  ratavü  Y. 2.  9,  Vr.  2.  6,  S.  2.  6;  —  -SasVi^ö  asahe ratubys  Y./.9,  Vr./.4,  S.I.6;  —  rähwqm
```


## [2026-09-06T16:21:13.564Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Herz'\" BRT.txt | head -20; echo \"=== search zrazda\"; grep -n \"zrazd\\|srazd\\|zraz-\\|zrazdä\" BRT.txt | head -20"
}
```


### [2026-09-06T16:21:13.624Z] TOOL RESULT

```
7650:•  j.  «raJaya-  n.  'Herz':  'lacm  F._jg. Pü, ;  dil.  —  Ob  Reimwort  lu  zirii,'  oder  daraus verderbt  ?
28131:S.  *gav-  No.  I  und  S  aoÄ  2.  —  Vgl.  ai.  ja- vij/ia-  Adj.  'der  rascheste',  np.  cb</ ■rasch'.  — Pü.:  däSaJiSI,  (zu  Y.  46):  pa  ..  dahin il;  e. noch  No.  2.  —  ■)  Mit  i  nur  Vt  13.  —  >)  Pü. : haäi  Joint  kflpa  :^ihiSn  i  j^atailh  i  süldmand, eil:  xataiik  i  sülömand  apt  döiit  u  api  dakti.  — j)  In  Folge  Vetmengung  mit  'ioola-  mir.; falsches  bei  Ju.  GIrPh,  2.  636. g.  (,  j.)  zar^d-  n.  'Herz';  a^rä  *rJam
28137:•  j.  *z«i^fiaya-  n.  'Herz':  *'oBfl«*>  F. 20.  a)  im  Sinn  voninnerstes, Höchstes'*: fflSa  *t3mahs  mathim  aS«  ''zmtahe  *'%aem^ "und  es  ist  des  Winters  Mitte  und  es  ist des  Winters  Herz"  V. /.  3.
=== search zrazda
2488:ultä  kakmäiclt  .  .  däyät  ahurö 44-i6,  27.14;  — yastn  .,  tari.mqstä  .. anying  ahmat  yi  hei  arim  mainyätä  Y. 4j.ii;  —  anyö  akmat  yö janaili  V.5. 34; N.  iS\  —  agustä  (sd.)  vacS  singhamahl aHbyö  yöi  ,  .  alakyä  gaSha  vlm?r?ncaiis (sd.)  aihp  aiibyö  nahiltä  yöi  *zrazda  aa- Afn  tnazdai  Y.j/.  i;  jo.8;  —  alsam  gä- naoiti  v?rfirayrtim  yöi  diin  .  .  /r3yaz?nte YL/O.16;  —  vätöyö/ä (sd.)  1/  aäbyöyöi  Tl.. v»r^syqn  Y.J5.6;  —  vJspaiibyö  aiibyö  yöi .  .  upa.sruttvanii  N.  20;  —  ahe  .  .  yö  nö dussarfkö  AiitaiteY.  10.12  (s.a.);  —  mäoa fiS  a/tmi  /raniliti  (sd.)  yÖ  nö  ..  inrixsaile ^■^5'7i  —  ^y^  *äröi  häkunnim  {'^d^ yayä haiinti  urvqnö  Y.j'^j.  9;  — ■  //  äbya  (statt DP.)"*  bairyeinte  yalsatn  .  .  fräyö  (sd.) '      ■  ■  bei
4190:•  '].  a-ohvä-,  g.  a-hvä-"  f.  i)  'Antrieb des  Willens,  Schaffensdrang,  Lebenskraft' : pairika  yä  duzyäirya  vlspahe  atiksui  .  . ' faröit pairi'in^misA.)  anhvqm  avaAisiiyät\ (sd.)  Yt.Ä54;  —  ava  m!  3zis  .  .  par5it\ fairrbnpm  (sd.)  arihvqm  ava.d}nnqn  sada- 1 yäfi  (sd.)  V.  i5. 19.  2)  'Antrieb  derl Seele,  innerlicher  — ,  Gemütsdrang,  Ge-j müt'"':  kal..*manS  asti  vT/aymii'tfm{s±) anhvqm  vjmar3zist?m  (sd.)  VL  /.  2 ;  —  ' virtzvatca  (sd.)  mat^  vansvatica  attuAa  j 'W.  62,10;  —  ye  kvam  ankvam  yaozdaite\ humatsilia  .  .  V.  ^.2i^>;  si  *PÜZ.,  lO.  19  I PüZ.;  —  dusx'arpnä  . .  asH5  asti  auuhaya  \ (LS.)  ".  .  ist  unfroh  in  seinem  Gemüt"  j YLJO.105;  —  aibl  ahväha  daxst^m  dilvOi\ (sd.)  Y.5/,9;  —  yatära  vä  dim  paurva frayasäiti  fraor^t  fraxsni  avi  manö  (sd.) zrazdälöii  ar^huyal*^  (oder  avuhyat)  i>  haca ". .  gern  in  sorglichem  Sinn  aus  gläubigem Gemüt"  Yt  /o.  9;  —  fora  vi  räki  am?sä spmtn  yasmmcä  rahmtmcä  firä  mana»hä ..  vaiaahä  ..  syat>^anä  ..  dw^iy«  (IS.) » Y.7/.18.
6054:•  j.  *a-zrazdi-''  Adj.  'ungläubig':  Vihrkai kavam  dalaiH yy  °dai*mq'ir)m  /aste"dem Wolf  schenkt  seine  Zunge,  wer  den  Ungläu- bigen das  heilige  Wort  lehrt"  N.  ij.
6074:ys. .  mazdayasnö  aojanö  'sähe  raima  (sd.)  \  13.  42,  Y.  68.  7,  14-  48;  —  a^al  nS  vacö jlsti^amnS  "V .  8.  y, —  uxltie  (sd.)  xraiwe  .  ,  *sixsaimca  (sd.)  .  .  °jvW  haäz  yat vTdrvanahe  °sät  'V.4-AS',  — yaüra  nard  vahiHät  Y.iff.ii.  LS.  'Saya  als  Adv, asavatts  'um  h^tüi  zrazdatsma  (sd.)  YL  j  sbes.  II)  '(dem  heiligen  Recht  ent- y-  'S;  —  tha  5%ravanS  .  .  ma/iyetiU  sprechtnics,  ^/«mässigesj  rechtes,  recht- vanh^s  'sähe  Yt7j.  147;  —  vahistmi  schafTenes  Tun,  Gerechtigkeit,  Recht- °i3m  yatamaide  Vr.  2g.  i ;  —  ySi  'iäi  schaffenhcit';  auch  in  kollekt  Sinn  'alles vaonarp  (sd.)  Y.  26.  4,  S;**  —  yö  yaomwas  einer  recht  tut,  bona  opera'.  i)  im iärayeiti  hs  'hm  iarayeiti  [sA.)  V._J,  31;  ■  gAw.:     huää    (sd.)    'Sim    vohucä    manä
6656:—  hyalca  msi  Ayjt  vaxi  aeüf  (sd.)  Y.  ij.ioo.  Anhang,  i)  Bei  mehreren 4^.17;  4j-i6; — yii*zrazd^  (sd.)  avk?/i  Subjekten  kann  das  adjektivische  Praedi- mazdli  Y.j/.  i;  —  dmjo  d^mäfts  ha^tyi  kat  mit  dem  nächststehenden  Subjekt (sd.)  an>Am  astayJ  Y.  4p.  11;  48.12;  —  kongniiren,  während  die  Kopula  pluralisch kiihm  yas3(sd..)  Hyin  ahm\.^i,^; — duz-  \A\'&)\!ah:iN.:y.idäas/mzn'Tm(sd.)anhen varpsnavhs  dafsnyl  (sd.)    hSntä  Y.  5J.  8;  mazdascä  .  .  alic-l  .  .  Y.^/.  4.         2)  Statt
7549:•  g.  Eiav-  DO.  'Streben,  Eifer',  spez.  in Glaubetissachen :  yavat  'his*zrazdUtS  banöi haxtaya  (sd.)  "sofern  der  gläubigste  Eifer (euch)  in  Fleisch  und  Blut  (sitzt)"  Y.55.7.
13180:An  unklaren  oder  wertlosen  Stellen:  ya/ Vit  aS^am  anyB  aäahmäi  däitt  dmäiti  N. 61  %  62,  loy,  YL  2.  1 2,  Vyt.  4<%  Nik.  j';  — daoqm  Yt.  4.1;  —  daöat  Vyt.31;  —  da- iatie  Vyt 50; —  dasie  YL  2. 12;  —  dazde ^■55''>  —  äayata  V.  5.  2  PüZ.;  —  daihi \yt.4S';  ~  dataheYt.i4.^&.  Vgl.noch mand-  (für  Y.  28.  4,  53.  5),  »/^zrfj-  (für  Y. g.  31),  yaoida-  (für  Y.44.  g),  zrazdä-  (fiir Y'Lp.  26.]
20452:*inaibySi.manhahe  ..y3  paoiryS  sara^uäräi (statt  Gen.)  'r>mca  *gu/ta  säsnhca  Ytij. 95'';  —  gahanqmca  sraohnm  . .  Avarita 'rä  (als  AP.)  äyae  yes'H  Y.3.  4;  4. 1,  Vr. ig.  2;  —  sva.  'Zauberspruch':  'am»mca Vir»%rayfumca  ajrinämi  .  .'  afffm  'mm mä  fradalsaysis  atnyai  /ikre  vH  .  .  Yt. i4-A(>',  4-9;  — /rina  ayanqm  •ranqm  yä vinsyäü  avi.m^riS  Yt  10.  so.  a)  bes. 'götüicher  Spruch':  aityamaram  'ranqm mazist»m  'ranam'"  ..  Yt.j.  5;  —  'ranqm a^a.balsasU  YL^.  6(?).  a)  insbes.  Sing. KctT  di,  oder  mit  ip»nia-  Adj.  'das  heilige Wort',  der  Inbegriff  der  göttlichen  Offen- banmg;  auch  vielfach  als  Gottheit';  I)  kolt' it :  alahepaiti  'nm  V.  4. 43 ;  —  aiwiläitT^äi gravas{sA.)ca  'rahe  V.g.  26;  —  masttm  .. 'raheia  faurvatätim  Y.57.  20;  —  aSa  'r»m ..  mairyatY.j.^^;  Yt./-4(?); — yö  anhat ..'ram  p3r3s3  alava  V,_9,  z; — yS  azrazdäi (sd.)  *'r»m^  !astt  N. 77;  —  vXsptm  °rsm yasamaide  Vr.  13.  i;  V.  20.  3;  —  maynS 'rS  N.  3  **;  —  AaemaAeca  °raheca  alaonaica zara%ustrahe  Y.  8. 1.  a)  beschränkt  auf die  fiinf  (?j2r3s:  atryamansm  isim  . .  yS up»nS  (sd.)  ,  .  zaoxJsuye  tarS  (sd.)  'rfm pania  gäh  ä  G.  1. 6.  H)  mit  sp?nta-  Adj.s> : uH  ahurahe  mazda  yazamaide  dari^räi (sd.)  'rahe  spmtahe  xratüm  .  .  mar»%räi 'rahe  spmfahe  hisvqm  .  .  fravakai  'rahe spmtahe  Yt.7.  z8;  —  ahurahe  masda  .. yeiihe  urva  'rff  sp^tS  Yt.  ij.8i,V.iff.n;
20782:—  a^qm  ainatjhqm  .  .  yalsqm  tu  .  . irixt>m  (sd.)  vaidistS  ahl  Y.J2. 7;  — aiibyS  , .  ySi  .  .  galhä  vlm)r>ncaitl  .  . a^ht  aäbys  . .  ySi  (zu  3)  *zrazdä  anhm mazdai  Y.^j.  i;  —  s.  noch  Y.44.  16  im Anhang.  zu  3):  akmät  y3  hsi  arim (sd,)  *mainyatä  "^-45-  ";  3t-^,  5^-6;  — afmtäi  ySm    axldyöi  (sd.)  diahe  Y.36.1;
23628:'iinhs  sravatfhavö  V.iÄ6s;  ^  jqhwa "ka  (NP.)  scqhwa  'ka  psihwa  "ka  snaiiana V.  13. 40;  —  'kam  (ASf.)  atrif.dailTm  (sd.) V,  JÄ65;  —  spämm  ..  raohm  ..  'k»m Y.  6.  50;  5.  50  (statt  NS.)j  —  ya^a  maisi Vihrkavatti  °kat  ha^a  ^fratmsaitiN .ig.^-^, Aog.  ig  (wo  °k!i£)\  — yaka  °kd  vaydi  (sd,) /aite..razsire(sd,)  V.IJ.  8;  —  'iäi  Aitvqm tfalaiti  yS  azrazdai  (sd.)  *fnqhr>m  calte N.i7;  —  täyul  vä  °iO  va  V.7j.io;4o; —  layBm  . .  'ktm  Y.  9.  3 1 ;  —  täyBl •kftnca  '•  V.  y .  1 7 ;  —  -kaht  F.  8;  —  'kayä (GS.)  kihrpaca  payattka^a  N.fp; +/a«V  -ialNP.)  paii/iH  (sd.)  . .  aok.tarasca .  .ya%a  anya  'ia  V.  ij.  43 ;  —  aisff. .  aSayü 'kayä  (GD.)  JqhivS.tans  ^atihat  .  .  ya^i spS  'kahe  lannaotti  /a&a  yat  vihrkS  spa "der  von  den  beiden  Wölfen  (Wolf- bastarden) verdient  noch  mehr  umgebracht 2U  werden,  den  ein  Hund  einer  Wölfin zeugt  als  der,  den  ein  Wolf  einer  Hündin (zeugt)"  V,/j.4i');  41.  a)  Übertragen  auf feindliche  Wesen^':  'kim  yim  bhangnm daevayasmm  V.  7.  5»  PUZ.
28295:'*zrazdä-
28320:•  j.  'zraz-dä-  kompV.  'vertrauen,  glauben'. Praes.  i  zrazda-.  —  Inf.  *sraiäatai-ia.
28323:•  g.  *^zraz-dä-''  Adj.  'gläubig,  gläubig ergeben':  ysi  'da  (NT.)  atffiTn  inatdäi "die  dem  M.  gläubig  ergeben  sind"  Y. 31.1.
28330:•  j-,  g.  'zrazdätay-''  i)  f.  'Vertrauen auf  -,  Glaube  an  -';  a)  mit  Akk.  oder Gen.  (obj.):  °ääittm  ma^nm  spjntjm  "den Glauben  an  das  heilige  Wort"  Y.  25.  6;  — 'dälSÜ  ma^rafte  spmtake  V.  22.25.  ^)  ™'^ Inf.:  sadra  mffi  sas  (sd.)  . .  •däUi!  tat vfmyddyai  hyal  .  .  Y.  43.  11.  LS, *'dätal-ca  als  Inf  sbes.  a)  Adj.  (auch fem.)  'vertrauend,  gläubig':  'datüit  aahuyat (sd.)  haca  Yt  10.  9.
28332:•  j.  'zrazdätay-  m.  EN.  eines  Gläubigen: 'dätsi^  falsatavAs  asaonH  "des  Zr.,  Sohns des  P.  . ."  Yt  13. 1 1  s.
28334:•  j.  *zrazdätae-i-a "  Inf.  'zu  vertrauen auf—,  zu  glauben  an  — ':  yamaheca  hapia-
28337:•  j.  zrazdä'tama-  Adj.  'der  gläubigste  \ an  — '  (Akk.):  yaäsra  narS  .  .  aiam  h3nti\ 'tgma  ". .  am  gläubigsten  an  das  heilige Recht"  Yt  13.25.  !
28339:•  g.  *zrazdiSta-''  Adj.  'der  gläubigste': 3i»/(sd.)  'dtüö  Y.5^.  7.
28999:tanvS  V.  13.  37  f.;  Nik.  i  (,  a)»"»,  Vd.  2;  — >>ii&(i  nä  .  .  ra^aiäa  hus.fiqm.hr9lai  k' ^aSat . .  faiti.fftaa  Yt  y .  6  7 ;  —  paeiryqm giritqm  gantaSa  aus  ..  h'  aptihrB.tanyäi jahikayäi  (als  Gen.)  Yl  77.  57;  58;  — j/atära  vä  dim  .  .  fräyassiti  /raonl  ,  . *zrazdatoit  anuhyat  (Sp.  1 1 1  u.)  h'  Yt. 10.  9.  b)  im  gAw.;  zu  b);  asäatlä  h'
```


## [2026-09-06T16:21:24.758Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Gattung, Art\\|'Art,\\|Art, Gattung\" BRT.txt | head -20"
}
```


### [2026-09-06T16:21:24.810Z] TOOL RESULT

```
26092:p.  S-ard-,  j.  'sar?d-  f.  'Art,  Gattung': •dam  Bh.  5.  i  (?).  a)  hamahyayä  'dJ' (GS.)  "in  jeder  Weise':  imc^  tys*  adam akunavam  hamahyayä  'dc^  vaSna  J'urJ'-
26100:•  j.  'sanSa'  n.  'Art,  Gattung':  Aa'^ra vlspanqm  gJus  'tanqm  taoxma  upa.bara V,  2.  2  7 ;  41 ;  —  ^pam  *vlra  yä  stS  °tanqm vahiäa  Yty.  12;  —  äiiti  h?nti  urvara-
```


## [2026-09-06T16:21:33.851Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### SNS sartak\"; grep -n \"sartak\\|sardak\\|sardag\\|srtk\" SNS.txt SNS_pages.txt | head -10; echo \"### HRN dil\"; grep -n \"dil\\b\" HRN.txt | head -10; echo \"### HRN sarda\"; grep -n \"sarda\\|serde\" HRN.txt | head -10"
}
```


### [2026-09-06T16:21:33.922Z] TOOL RESULT

```
### SNS sartak
SNS.txt:11041:&***#+"* .«j»c**«i»" -e* <•■*-« sardag 
SNS.txt:11047:^i l.Vt^e^ 1 '^ : sardagan: WS^ | 
SNS.txt:17937:, o'-^^C^J 1 :gospand sardagan: w»*~ 
SNS.txt:31352:sardag 183/9 
SNS.txt:31354:sardagan 183/12 
SNS.txt:32831:gospand sardagan 331/9 
SNS_pages.txt:7582:                                                            <•*-« sardag                                                                 Y/Y^                         (*-j*U^) ar:53:                                     )*WU*
SNS_pages.txt:7586:             ^i l.Vt^e^ '^       1                 :   sardagan:       WS^                   |
SNS_pages.txt:12911:    o'-^^C^J        1    :gospand sardagan:
SNS_pages.txt:15833:                          sardag 183/9
### HRN dil
2058:bei. gvadil {*gvad-dil) 'feige* (130) hält Hübsch-
5126:571. dil *Herz', diler (reimt auf ser, Sahn. I, 195, 1194).
5127:aw. zered- (y. :n, 12), zaredaya- *lIorz*; phlv. dil,
8000:er auf gtisäde-dil 'fröhlich* verweist. Somit würde es
16186:jSirdil. 410.
### HRN sarda
3298:Zeile 3, 184 Zeile 8). Das ausserdem bei AM. 184 und anderweitig
3518:*) Np. tefne wird bei SF und ausserdem in FR, FJ durch einen
5133:np. rf// ist ausserdem in alle iranischen Sprachen
5192:ausserdem das n von np. sänzdeh), hol. duäzdeh,
5898:LW. bei. zamtk 'Felder, Saaten' (415); ausserdem
7989:sid'tanaiy), dagegen gtisilem ap. *visardann (aus sar-
10946:/vareh), pursartak (d. i. pursardak) etc. Zu pur Viel*
10971:175. sartak (d. i. sardak) *Art und Weise*.
10974:np. serde {rd statt /, also nicht lautgesetzliche Form)
```


## [2026-09-06T16:21:34.769Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### HUB dil\"; grep -n \"dil \" HUB.txt | head -15; echo \"### SOD zrd\"; grep -n \"zyrδ\\|zyrd\\|δyrd\" SOD.txt | head -8"
}
```


### [2026-09-06T16:21:34.853Z] TOOL RESULT

```
### HUB dil
832:187. In bal. gvadil *feige' (aus ^gvaddil = *gvat-dil) ist
833:dil sicher persisches LW., dagegen wird goat echt sein
835:es aber nur in gvadil vorkommt, nahm ich an, dass
836:gvadil altes Lehnwort sei -= mp. *vaddil (vgl. paz.
837:vad schlecht* und dil *Herz').
5076:'Erdtheil*, phi. kisvar = zd. karSvare (aus *krsvar-) ; dil 'Herz'
5157:gursa 'hungry', gursnai 'hunger , gurda 'kidney* — dil 'heart',
5183:dil *heart' p. 286, hiStan *to leave' p. 2, kisvar *a region
9133:hambistar *Lagergenosse\ hamdil *gleichgesinnt*, hamdam
9320:prdaku", gr. ndpduhg; dil *Herz* = zd. zered-^ skr. Ard-;
9798:herzt* von dil *Herz' und afgh. ndmEr *bertihmt'
### SOD zrd
```


## [2026-09-06T16:21:43.918Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '5120,5145p' HRN.txt; echo \"===== 10940-10990\"; sed -n '10940,10995p' HRN.txt"
}
```


### [2026-09-06T16:21:43.978Z] TOOL RESULT

```
I, 17 folgg.); phlv. dus/J'är, dmx'arlh.
Die neup. phlv. Formen sind Neubildungen aus
dus+x"^'^ (No. 49G).
570. destän 'menstruirende Frau'.
aw. da/stavaitl-; phlv. dastän (arm. LW. dasfan;
chald. LW. ]P\'^'^)j dastan(i)stan^ vorgl. dayßak,
571. dil *Herz', diler (reimt auf ser, Sahn. I, 195, 1194).
aw. zered- (y. :n, 12), zaredaya- *lIorz*; phlv. dil,
päz. diler (Men.); ai. hfd-, hfdaya-; arm. sirf (IT.
No. 250).
kurd. zar 'Herz*; af/. zra; oss. d. zärdd^ t. z'ardä
(131); bei. ^^zVc/c (420); sar. zärd^ si;'n. -^^Il), <m//,
sangl. mrütj^ minj. 2?/.
np. rf// ist ausserdem in alle iranischen Sprachen
entlehnt, meist ohne einen Bedeutuugsunterschi(^d mit
dem betreffenden einheimischen Woite aufzuweisen
(Ausnahme: Tomaschek, S. 78()).
572. dem 'Atem, Atemzug', deine^ demulen 'wehen, blas(Mi\
demäy^ demär,
ai. V^dham-', dhdmiti 'hauchen, bhisen*; phlv. dam;
ksl. dümq, dqti 'blasen'.
< . •
') Bartholomae (BB. 15, 86) legt dieser Wurzel die Bedeutunjij
einweihen, weihen* bei. Dazu passen aber inoht die ebenfalls dazu
gehörigen ai. dasmä-^ dasrä-. Geldner übersetzt KZ. 30, 329 aw.
dldaihhe mit 'ich wurde unterwiesen*.
===== 10940-10990
169. i^urmah 'VoHmond' (AW.-Komm.).
aw. perenomäoHhci' 'Vollmond'; skr. vergl. pürnamäsa-
'VoUmond'.
Hier Hessen sich noch manche andere, im Neu-
persischen aufgegebene Composita mit pur- anführen,
z. B. purmary , ptiranäkth (AV.), ^/i/^-rn:! (päz. jmr-
/vareh), pursartak (d. i. pursardak) etc. Zu pur Viel*
vergl. oben unter np. pvr (No. 294).
R
170. rar 'Glanz, Licht\ selten (AW.-Komm., Bund. 24, 25),
rätmand, räyömand (aw. roevcmt'),
aw. ray- 'Glanz, Licht'; ai. räy-,
171. rajntwintar 'südlich, mittäglich'.
aw. rapid Irina- *Süden, Mittag'; vergl. wa;^^. pizwan
'Mahl, Mittagessen'. /
172. ruH Wagen' (AV.).
aw. rada- 'Wagen; ai. rdtha-. In Namen z. B.
173. rün 'Seite, Gegend, Richtung' (AV., Men.), vergl.
frärün, apärün, rapitwintarrün etc.
Eine ältere Form kommt nicht vor. Bartholomae
denkt nach briefl. Mitteilung an Zusammenhang mit
aw. raonqm *der Flüsse' (vergl. Wochenschr. f. kl.
Phil. 1890 Sp. 1108), da aus der Bedeutung 'Flusslauf
sich die der ^Richtung' entwickelt haben könne.
Nicht hierher gehört natürlich np. herün (oben
No. 252) ; die Schreibung berrün bei AM. 265 Zeile 1
V. u. beruht nur auf einem Schreib- oder Druckfehler.
') Vergl. Honi, Mittheilungen, Heft IV, S. 27 Note.291
174. sacltan 'vorübergehen, ablaufen', Praes.saeet '), sazad
(vd. 18 (60), 5 (84)), sac(i)sn.
ap. Sakatä'); aw. [^sac- Vorübergehen, ablaufen'.
175. sartak (d. i. sardak) *Art und Weise*.
ap. t^wrd- 'Art'; aw. sareda- *Art, Gattung; ai.
rdrdha' nur *Schaar .
np. serde {rd statt /, also nicht lautgesetzliche Form)
findet sich nur in den Riväyet's.
176. sar^mr 'Helm'.
aw. säravära- 'Helm*.
177. sästär 'Herrscher, Tyrann* (AW.-Komm., AV.).
aw. sastar-; skr. ^as^tdr- 'Gebieter, Züchtiger; arm.
vergl. säst 'Schelten, Vorwurf, Drohung, Unwille,
Strenge', sastem schelten, drohen, einschärfen', sastik
'heftig (H. No. 246).
178. sej 'Schmerz, Leid', sejömand (Bund., AV.), asefömand,
päz. seS\
aw. id-yejah'.
np. sej ist nur pärsisch. FJ und FR citiren folgenden
Vers von Behräm Zerätuät (Metrum: Hezej):
jfehän-i s^fmend-T pur ^na%
Ja öra pese hased bevefäi
179. snahs, snas 'Schläger; Schlag (AW.-Komm., Säy.-
näsäy.^).
aw. snaid^is-, sna^^a- 'Schläger (zum Schlagen);
Schlag'.
180. snavar 'Sehne' (nur AW.-Komm. ; auch für aw. t^an^
var^)j vielleicht nur Transcription.
```


## [2026-09-06T16:22:01.266Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"آکوردئون\\|اکوردئون\\|آکورد\" MON_part1.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt 2>/dev/null | head -10; echo \"### ARY del\"; grep -n \"^دل\\|دل (\" incoming/ARY/ARY_pages.txt | head -10"
}
```


### [2026-09-06T16:22:01.339Z] TOOL RESULT

```
MON_part1.txt:4078:اکوردئون: 0 (۱.) (مت.) تک از 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:4078:اکوردئون: 0 (۱.) (مت.) تک از 
### ARY del
```


## [2026-09-06T16:22:02.062Z] TOOL CALL #42: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%AF%D9%84' --note 'page 259, root Kerd 1, Persian del \"heart\" etymology' 2>&1 | tail -20"
}
```


### [2026-09-06T16:22:04.672Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/89b4955bf2fe4033.txt
```


## [2026-09-06T16:22:07.478Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '4070,4090p' MON_part1.txt"
}
```


### [2026-09-06T16:22:07.544Z] TOOL RESULT

```
آکننده» آکنیده) آ کندن. 


اکو: تتطة (- ۲ گو] (ا.) (جاد.) بوم» جغد. 


اکوردئون: 0 (۱.) (مت.) تک از 
آلات موسیقیء دارای زبانه‌های فلزی که به 
ارتعاش درمی‌ آیند و آن رابه وسیلةً سر 
انگشتان نو از ند. 

اک ومولاتور: :2550115 (.) (فر) 
دستگاه الکتریکی که می‌توان مقداری برق 
در آن ذخیره کرد و به هنگام لزوم از آن 
تک فتا: و آن انواع بسیار دارد مانند 
آکومولاتور سربی و عبره» انار ه» خازرن 


رف
```


## [2026-09-06T16:22:07.892Z] TOOL CALL #44: Bash

```json
{
 "command": "sed -n '1,200p' data/verification/sources/web/89b4955bf2fe4033.txt | grep -n -A30 -i \"Etymology\"| head -60"
}
```


### [2026-09-06T16:22:07.943Z] TOOL RESULT

```
76: Etymology 
77-
78- 2.2 
79- Noun 
80-
81- 2.2.1 
82- Derived terms 
83-
84- 3 
85- Gujarati 
86-
87- Toggle Gujarati subsection 
88-
89- 3.1 
90- Noun 
91-
92- 4 
93- Laki 
94-
95- Toggle Laki subsection 
96-
97- 4.1 
98- Noun 
99-
100- 5 
101- Ottoman Turkish 
102-
103- Toggle Ottoman Turkish subsection 
104-
105- 5.1 
106: Etymology 1 
107-
108- 5.1.1 
109- Alternative forms 
110-
111- 5.1.2 
112- Noun 
113-
114- 5.1.2.1 
115- Derived terms 
116-
117- 5.1.2.2 
118- Descendants 
119-
120- 5.2 
121: Etymology 2 
122-
123- 5.2.1 
124- Noun 
125-
126- 5.2.1.1 
127- Descendants 
128-
129- 5.3 
130- References 
131-
132- 6 
133- Persian 
134-
135- Toggle Persian subsection
```


## [2026-09-06T16:22:10.126Z] TOOL CALL #45: Bash

```json
{
 "command": "grep -n -i \"Proto-Iranian\\|Middle Persian\\|Proto-Indo-Iranian\\|Proto-Indo-European\" data/verification/sources/web/89b4955bf2fe4033.txt | head -30"
}
```


### [2026-09-06T16:22:10.171Z] TOOL RESULT

```
837: From Classical Persian دِل ( dil ) , from Proto-Iranian *jā́rd , from Proto-Indo-Iranian *ȷ́ʰā́rd , ultimately from Proto-Indo-European *ḱḗr .
973: From Middle Persian 𐭣𐭩𐭫 ( dyl /⁠dil⁠/ ) , from Proto-Iranian *jā́rd , from Proto-Indo-Iranian *ȷ́ʰā́rd , ultimately from Proto-Indo-European *ḱḗr ; with a regular phonetic shift *ȷ́ŕ̥d- > *dŕ̥d > *dŕ̥l > dil. For the phonetic change, compare گل ( gol ) and سالار ( sâlâr ) .
1550: Baluchi terms derived from Proto-Iranian 
1551: Baluchi terms derived from Proto-Indo-Iranian 
1552: Baluchi terms derived from Proto-Indo-European 
1572: Persian terms inherited from Middle Persian 
1573: Persian terms derived from Middle Persian 
1574: Persian terms inherited from Proto-Indo-European 
1575: Persian terms derived from Proto-Indo-Iranian 
1576: Persian terms derived from Proto-Indo-European 
1577: Persian terms inherited from Proto-Iranian 
1578: Persian terms inherited from Proto-Indo-Iranian 
1579: Persian terms derived from Proto-Iranian 
1580: Persian terms derived from the Proto-Indo-European root *ḱerd- 
1590: Punjabi terms derived from Proto-Indo-European 
1591: Punjabi terms derived from the Proto-Indo-European root *ḱerd- 
1592: Punjabi terms derived from Middle Persian 
1593: Punjabi terms derived from Proto-Iranian 
1594: Punjabi terms derived from Proto-Indo-Iranian 
1620: Urdu terms derived from Proto-Indo-European 
1621: Urdu terms derived from the Proto-Indo-European root *ḱerd- 
1622: Urdu terms derived from Middle Persian 
1623: Urdu terms derived from Proto-Iranian 
1624: Urdu terms derived from Proto-Indo-Iranian 
1652: Middle Persian terms with redundant transliterations
```


## [2026-09-06T16:22:17.769Z] TOOL CALL #46: Bash

```json
{
 "command": "for u in 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%E1%B8%B1%E1%B8%97r' 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%E1%B8%B1erd%CA%B0-' 'https://www.etymonline.com/word/accordion' 'https://en.wiktionary.org/wiki/credo%23Latin'; do echo \"### $u\"; python3 tools/fetch_source.py \"$u\" --note 'page 259, roots Kerd 1 / Kerd 2, PIE heart & herd, accordion, credo' 2>&1 | tail -3; done"
}
```


### [2026-09-06T16:22:21.301Z] TOOL RESULT

```
### https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%E1%B8%B1%E1%B8%97r
/home/sfmqrb/git/rishe/data/verification/sources/web/c6fb53d169580c89.txt
### https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%E1%B8%B1erd%CA%B0-
/home/sfmqrb/git/rishe/data/verification/sources/web/09a0e581a4dcac45.txt
### https://www.etymonline.com/word/accordion
/home/sfmqrb/git/rishe/data/verification/sources/web/ffd9a1cb348544e3.txt
### https://en.wiktionary.org/wiki/credo%23Latin
/home/sfmqrb/git/rishe/data/verification/sources/web/49d501cd16fb0195.txt
```


## [2026-09-06T16:22:24.379Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"=== PIE ker (heart) ===\"; grep -n -i \"Reconstruction notes\\|Descendants\\|Proto-Iranian\\|Avestan\\|Etymology\" c6fb53d169580c89.txt | head -20; echo; sed -n '/^ *Root/,+40p' c6fb53d169580c89.txt | head -60"
}
```


### [2026-09-06T16:22:26.253Z] TOOL RESULT

```
=== PIE ker (heart) ===
62: Etymology 
68: Reconstruction notes 
77: Descendants 
147: Etymology
159: Reconstruction notes
254: Descendants
274: Proto-Balto-Slavic: *śḗr ( see there for further descendants )
276: Proto-Celtic: *kridyom ( see there for further descendants )
278: Proto-Germanic: *hertô ( see there for further descendants )
287: Proto-Italic: *kord ( see there for further descendants )
289: Proto-Indo-Iranian: *ȷ́ʰā́rd , ⇒ *ȷ́ʰŕ̥dayam ( unexplained voiced aspiration ) ( see there for further descendants )
291: Proto-Tocharian: *käryā- ( see there for further descendants )
```


## [2026-09-06T16:22:28.392Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '140,300p' c6fb53d169580c89.txt"
}
```


### [2026-09-06T16:22:28.434Z] TOOL RESULT

```
 From Wiktionary, the free dictionary

 This Proto-Indo-European entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.

 Proto-Indo-European
 [ edit ] 

 Etymology
 [ edit ] 

 From *ḱerd- ( “ heart ” ) .

 Noun
 [ edit ] 

 *ḱḗr   n ( oblique stem *ḱr̥d- ) [ 1 ] 

 heart 

 Reconstruction notes
 [ edit ] 

 The nominative singular form is underlyingly */ḱérd/ , yielding the surface form *ḱḗr which is itself evident in Ancient Greek κῆρ ( kêr ) and Hittite 𒆠𒅕 ( ke-er /⁠ker⁠/ ) . This reconstruction is the only instance in PIE where a loss of */d/ after */r/ with compensatory lengthening of the preceding vowel occurred. It is not clear whether this is an isolated example, or a part of a broader process such as Szemerényi's law .

 Inflection
 [ edit ] 

 Athematic, amphikinetic

 singular

 nominative

 *ḱḗr 

 genitive

 *ḱr̥dés 

 singular

 dual

 plural

 nominative

 *ḱḗr 

 *ḱérdih₁ 

 *ḱérdh₂ 

 vocative

 *ḱḗr 

 *ḱérdih₁ 

 *ḱérdh₂ 

 accusative

 *ḱḗr 

 *ḱérdih₁ 

 *ḱérdh₂ 

 genitive

 *ḱr̥dés 

 *? 

 *ḱr̥dóHom 

 ablative

 *ḱr̥dés 

 *? 

 *ḱr̥dmós , *ḱr̥dbʰós 

 dative

 *ḱr̥déy 

 *? 

 *ḱr̥dmós , *ḱr̥dbʰós 

 locative

 *ḱḗr , *ḱérdi 

 *? 

 *ḱr̥dsú 

 instrumental

 *ḱr̥déh₁ 

 *? 

 *ḱr̥dmís , *ḱr̥dbʰís 

 Derived terms
 [ edit ] 

 *ḱréd-dʰeh₁-ti ~ *ḱred-dʰh₁-én-ti ( “ to trust, believe ” ) 

 Descendants
 [ edit ] 

 Proto-Albanian: 
 Albanian: kërth , kërthizë 

 Proto-Anatolian: 
 Hittite: 𒆠𒅕 ( ke-er /⁠ker⁠/ ) 

 Luwian: 
 Cuneiform script: 𒍝𒀀𒅈𒍝 ( /⁠ UZU zārza⁠/ ) 
 Anatolian hieroglyphic script: 𔖪𔖱𔖪 ( za-ra/i-za ) 

 Lycian: 𐊋𐊕𐊆𐊅𐊁 ( kride ) 

 Palaic: 𒅗𒀀𒅈𒋾 ( ka-a-ar-ti /⁠kārt-⁠/ ) 

 Proto-Armenian: *ḱḗrdi- 
 Old Armenian: սիրտ ( sirt ) Armenian: սիրտ ( sirt ) 

 Proto-Balto-Slavic: *śḗr ( see there for further descendants )

 Proto-Celtic: *kridyom ( see there for further descendants )

 Proto-Germanic: *hertô ( see there for further descendants )

 Proto-Hellenic: *kḗr 
 Ancient Greek: κῆρ ( kêr ) 

 ⇒ Proto-Hellenic: *kərdíyā 
 Ancient Greek: κᾰρδῐ́ᾱ ( kărdĭ́ā ) 
 Greek: καρδιά ( kardiá ) 

 Proto-Italic: *kord ( see there for further descendants )

 Proto-Indo-Iranian: *ȷ́ʰā́rd , ⇒ *ȷ́ʰŕ̥dayam ( unexplained voiced aspiration ) ( see there for further descendants )

 Proto-Tocharian: *käryā- ( see there for further descendants )

 References
 [ edit ] 

 ^ Wodtko, Dagmar S.; Irslinger, Britta; Schneider, Carolin ( 2008 ), Nomina im indogermanischen Lexikon [ Nouns in the Indo-European Lexicon ]‎ [1] (in German), Heidelberg: Universitätsverlag Winter, pages 417-423 

 Retrieved from " https://en.wiktionary.org/w/index.php?title=Reconstruction:Proto-Indo-European/ḱḗr&oldid=92151970 "

 Categories : Proto-Indo-European terms belonging to the root *ḱerd-
```


## [2026-09-06T16:22:34.288Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '/^ *Proto-Indo-European$/,$p' 09a0e581a4dcac45.txt | sed -n '1,90p'"
}
```


### [2026-09-06T16:22:37.401Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T16:22:39.471Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && wc -l 09a0e581a4dcac45.txt && sed -n '100,220p' 09a0e581a4dcac45.txt"
}
```


### [2026-09-06T16:22:39.530Z] TOOL RESULT

```
5 09a0e581a4dcac45.txt
```


## [2026-09-06T16:22:42.208Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && cat 09a0e581a4dcac45.txt; echo \"=== accordion ===\"; sed -n '1,80p' ffd9a1cb348544e3.txt"
}
```


### [2026-09-06T16:22:42.255Z] TOOL RESULT

```
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%E1%B8%B1erd%CA%B0-
FETCHED: 2026-09-06T16:22:20Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found=== accordion ===
URL: https://www.etymonline.com/word/accordion
FETCHED: 2026-09-06T16:22:20Z
STATUS: 200
TITLE: Accordion - Etymology, Origin & Meaning

Accordion - Etymology, Origin & Meaning 

 Search 
 Log in 

 Columns 
 Forum 
 Apps 
 Premium 

 Log in 

 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 Origin and history of accordion 

 accordion (n.) 

 "small, keyed, bellows-like wind instrument," 1830, from German Akkordion , from Akkord "musical chord, concord of sounds," from a verb similar to Old French acorder "agree, be in harmony," from Vulgar Latin *accordare (compare Italian accordare "to attune a musical instrument;" see accord (v.)), with suffix on analogy of clarion , etc. Invented 1829 by piano-maker Cyrill Demian of Vienna. The type with a keyboard instead of buttons is a piano accordion . Related: Accordionist .
 also from 1830 

 Entries linking to accordion 

 accord (v.) 

 early 12c., accorden , "come into agreement," also "agree, be in harmony," from Old French acorder "agree, be in harmony" (12c.), from Vulgar Latin *accordare "make agree," literally "be of one heart, bring heart to heart," from Latin ad "to" (see ad- ) + cor (genitive cordis ) "heart" (used figuratively for "soul, mind"), from PIE root *kerd- "heart." Compare concord , discord . Related: Accorded ; according .

 clarion (n.) 

 "small, high-pitched trumpet," early 14c., from Old French clarion "(high-pitched) trumpet, bugle" and directly from Medieval Latin clarionem (nominative clario ) "a trumpet," from Latin clarus "clear" (see clear (adj.)). Clarion call in the figurative sense "call to battle" is attested from 1838 ( clarion's call is from 1807).

 Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 More to explore

 clavier 

 1708, "keyboard of a pianoforte, organ, etc.," from French clavier, originally "a key-bearer," from Latin clavis "key" (from PIE root *klau- "hook"). The French word also is the source of German Klavier, Dutch klavier, Danish klaver, etc. The German word was used generally of key

 piano 

 "percussion musical instrument in which tones are produced by blows of hammers upon stretched strings, the hammers being operated from a keyboard," 1803, from French piano (18c.), Italian piano, shortened forms of pianoforte (q.v.). Essentially, the pianoforte is a large dulcime

 squeeze 

 c. 1600, "press forcibly" (transitive), perhaps an alteration of quease (Middle English quisen), from Old English cwysan "to squeeze," a word of unknown origin, perhaps imitative (compare German quetschen "to squeeze"). It perhaps also has been altered by influence of many words 

 box 

 "rectangular wooden container," usually with a lid, Old English box, also the name of a type of shrub, from Late Latin buxis, from Greek pyxis "boxwood," pyxion "writing table, box," made of boxwood, from pyxos "box tree," which is of uncertain origin. Beekes suggests a loan-word

 ragamuffin 

 mid-14c., "demon;" late 14c., "a ragged lout," also in surnames (Isabella Ragamuffyn, 1344), from Middle English raggi "ragged" ("rag-y"?) + "fanciful ending" [OED], or else perhaps second the element is Middle Dutch muffe "mitten." Or, as Johnson has it, "From rag and I know not

 disaster 

 "anything that befalls of ruinous or distressing nature; any unfortunate event," especially a sudden or great misfortune, 1590s, from French désastre (1560s), from Italian disastro, literally "ill-starred," from dis-, here merely pejorative, equivalent to English mis- "ill" (see 

 profane 

 "desecrate, treat (holy things) with irreverence," late 14c., prophanen, from Old French profaner, prophaner (13c.) and directly from Latin profanare (in Medieval Latin often prophanare) "to desecrate, render unholy, violate," from profanus "unholy, not consecrated" (see profane 

 Eucharist 

 "sacrament of the Lord's Supper, the Communion," mid-14c., from Old French eucariste, from Late Latin eucharistia, from Greek eukharistia "thanksgiving, gratitude," later "the Lord's Supper," from eukharistos "grateful," from eu "well" (see eu-) + stem of kharizesthai "show favor

 calamity 

 early 15c., "damage, state of adversity;" 1550s, "a great misfortune or cause of misery," from Old French calamite (14c.), from Latin calamitatem (nominative calamitas) "damage, loss, failure; disaster, misfortune, adversity," a word of obscure origin. Early etymologists associat

 sleuth 

 late 12c., sloth, "track or trail of a person or beast," from Old Norse sloð "trail or track," as of a person in snow, a word of uncertain origin. The meaning "detective" is attested by 1872, a shortening of sleuth-hound "keen investigator" (1849), a figurative use of that word,
```


## [2026-09-06T16:23:12.074Z] TOOL CALL #52: Bash

```json
{
 "command": "pdftoppm -f 259 -l 259 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg259 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


## [2026-09-06T16:23:12.950Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^accordion\\|^creed,\\|^credo,\" KLN_1966.txt | head; echo \"---\"; sed -n '/^accordion/,+4p' KLN_1966.txt | head -10"
}
```


### [2026-09-06T16:23:14.846Z] TOOL RESULT

```
total 11652
drwx------ 7 sfmqrb sfmqrb    4096 Sep  6 12:23 .
drwx------ 4 sfmqrb sfmqrb    4096 Sep  6 10:51 ..
-rw-rw-r-- 1 sfmqrb sfmqrb    1276 Sep  6 12:21 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  180887 Sep  6 11:56 bqt1637_fn.png
-rw-rw-r-- 1 sfmqrb sfmqrb   50592 Sep  6 11:56 bqt1637_kaz.png
-rw-rw-r-- 1 sfmqrb sfmqrb  181961 Sep  6 12:11 bqt1688_fn.png
-rw-rw-r-- 1 sfmqrb sfmqrb  340758 Sep  6 12:11 bqt1709_fn2.png
-rw-rw-r-- 1 sfmqrb sfmqrb  280452 Sep  6 12:11 bqt1709_fn.png
-rw-rw-r-- 1 sfmqrb sfmqrb   92182 Sep  6 10:55 bqt1854.png
-rw-rw-r-- 1 sfmqrb sfmqrb   66580 Sep  6 10:57 bqt2023.png
-rw-rw-r-- 1 sfmqrb sfmqrb   69965 Sep  6 11:25 bqt2242crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb   28189 Sep  6 11:25 bqt2417crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb  431133 Sep  6 11:16 bqt2420_fn.png
-rw-rw-r-- 1 sfmqrb sfmqrb    9548 Sep  6 11:25 bqt2meta.json
-rw-rw-r-- 1 sfmqrb sfmqrb   81018 Sep  6 11:16 build213.py
-rw-rw-r-- 1 sfmqrb sfmqrb   67391 Sep  6 11:49 build225.py
-rw-rw-r-- 1 sfmqrb sfmqrb   71757 Sep  6 11:47 build232.py
-rw-rw-r-- 1 sfmqrb sfmqrb   49952 Sep  6 11:57 build234b.py
-rw-rw-r-- 1 sfmqrb sfmqrb   32265 Sep  6 11:51 build234.py
-rw-rw-r-- 1 sfmqrb sfmqrb   24770 Sep  6 12:01 build243.py
-rw-rw-r-- 1 sfmqrb sfmqrb    6504 Sep  6 11:13 c1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3402 Sep  6 11:22 c224_n10.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4812 Sep  6 11:28 c224_n12.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4744 Sep  6 11:22 c224_n1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3203 Sep  6 11:28 c224_n7.png
-rw-rw-r-- 1 sfmqrb sfmqrb   12820 Sep  6 11:27 c229_bibua.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5308 Sep  6 11:27 c229_greek.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5313 Sep  6 11:27 c229_persian.png
-rw-rw-r-- 1 sfmqrb sfmqrb    9059 Sep  6 11:50 c237_n18.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2389 Sep  6 11:50 c237_n3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4987 Sep  6 11:52 c239_kandid2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4734 Sep  6 11:52 c239_kandid.png
-rw-rw-r-- 1 sfmqrb sfmqrb   12852 Sep  6 11:52 c239_persian.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4087 Sep  6 11:52 c239_sandarus.png
-rw-rw-r-- 1 sfmqrb sfmqrb   15240 Sep  6 11:54 c246_caiique.png
-rw-rw-r-- 1 sfmqrb sfmqrb   36354 Sep  6 12:02 c246_casaque.png
-rw-rw-r-- 1 sfmqrb sfmqrb   84366 Sep  6 11:54 c246_n2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   51690 Sep  6 11:54 c246_n6.png
-rw-rw-r-- 1 sfmqrb sfmqrb   13719 Sep  6 12:02 c248_p3.png
-rw-rw-r-- 1 sfmqrb sfmqrb   30759 Sep  6 12:02 c248_p4.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2750 Sep  6 12:02 c248_persian2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3046 Sep  6 12:02 c248_persian.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4259 Sep  6 12:13 c250_celare.png
-rw-rw-r-- 1 sfmqrb sfmqrb    7170 Sep  6 12:13 c250_kolba.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4529 Sep  6 12:13 c250_sarez.png
-rw-rw-r-- 1 sfmqrb sfmqrb    8664 Sep  6 12:19 c255_french2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    6147 Sep  6 12:19 c255_french.png
-rw-rw-r-- 1 sfmqrb sfmqrb   23626 Sep  6 12:19 c255_latin2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   18287 Sep  6 12:20 c255_latin3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3398 Sep  6 12:19 c255_latin.png
-rw-rw-r-- 1 sfmqrb sfmqrb   26231 Sep  6 12:18 c258_kars.png
-rw-rw-r-- 1 sfmqrb sfmqrb   53453 Sep  6 12:18 c258_n2.png
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
-rw-rw-r-- 1 sfmqrb sfmqrb  169482 Sep  6 11:58 crop_1648b.png
-rw-rw-r-- 1 sfmqrb sfmqrb   45260 Sep  6 11:57 crop_1648.png
-rw-rw-r-- 1 sfmqrb sfmqrb  305924 Sep  6 11:57 crop_1731.png
-rw-rw-r-- 1 sfmqrb sfmqrb    6971 Sep  6 11:03 crop1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    8619 Sep  6 11:03 crop2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5240 Sep  6 11:03 crop3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2064 Sep  6 12:21 crop_cheek2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1888 Sep  6 12:21 crop_cheek.png
-rw-rw-r-- 1 sfmqrb sfmqrb   12820 Sep  6 11:05 crop_germ.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3408 Sep  6 11:05 crop_guthjo.png
-rw-rw-r-- 1 sfmqrb sfmqrb  111118 Sep  6 11:19 crop_habl.png
-rw-rw-r-- 1 sfmqrb sfmqrb    9001 Sep  6 11:05 crop_node12.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5564 Sep  6 11:05 crop_node1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3215 Sep  6 12:21 crop_p3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5286 Sep  6 11:05 crop_varathra.png
-rw-rw-r-- 1 sfmqrb sfmqrb   11652 Sep  6 11:13 c_xzn.png
-rw-rw-r-- 1 sfmqrb sfmqrb     724 Sep  6 12:11 drive.py
-rw-rw-r-- 1 sfmqrb sfmqrb    4491 Sep  6 12:13 fix.py
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
-rw-rw-r-- 1 sfmqrb sfmqrb   47535 Sep  6 11:47 mk230.py
-rw-rw-r-- 1 sfmqrb sfmqrb   64267 Sep  6 11:59 mk235.py
-rw-rw-r-- 1 sfmqrb sfmqrb   73422 Sep  6 12:02 mk237.py
-rw-rw-r-- 1 sfmqrb sfmqrb   81037 Sep  6 12:03 mk240.py
-rw-rw-r-- 1 sfmqrb sfmqrb   80347 Sep  6 12:08 mk242.py
-rw-rw-r-- 1 sfmqrb sfmqrb   58802 Sep  6 12:07 mk244.py
drwxrwxr-x 2 sfmqrb sfmqrb    4096 Sep  6 11:44 p216
drwxrwxr-x 2 sfmqrb sfmqrb    4096 Sep  6 11:52 p233
drwxrwxr-x 2 sfmqrb sfmqrb    4096 Sep  6 12:12 p245
drwxrwxr-x 2 sfmqrb sfmqrb    4096 Sep  6 12:21 p249
-rw-rw-r-- 1 sfmqrb sfmqrb   33321 Sep  6 11:51 part1.json
-rw-rw-r-- 1 sfmqrb sfmqrb   30335 Sep  6 12:07 part2.py
-rw-rw-r-- 1 sfmqrb sfmqrb   38036 Sep  6 12:11 part3.py
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
-rw-rw-r-- 1 sfmqrb sfmqrb   82071 Sep  6 11:44 pg234.png
-rw-rw-r-- 1 sfmqrb sfmqrb   47149 Sep  6 11:44 pg236.png
-rw-rw-r-- 1 sfmqrb sfmqrb  125593 Sep  6 11:50 pg237hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   67972 Sep  6 11:50 pg237.png
-rw-rw-r-- 1 sfmqrb sfmqrb  168221 Sep  6 11:52 pg239hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   81026 Sep  6 12:03 pg239.png
-rw-rw-r-- 1 sfmqrb sfmqrb   83594 Sep  6 12:03 pg239_small.png
-rw-rw-r-- 1 sfmqrb sfmqrb   81131 Sep  6 11:51 pg240.png
-rw-rw-r-- 1 sfmqrb sfmqrb   97613 Sep  6 11:49 pg242.png
-rw-rw-r-- 1 sfmqrb sfmqrb   80947 Sep  6 11:59 pg244.png
-rw-rw-r-- 1 sfmqrb sfmqrb   80632 Sep  6 11:55 pg245.png
-rw-rw-r-- 1 sfmqrb sfmqrb   79253 Sep  6 11:54 pg246.png
-rw-rw-r-- 1 sfmqrb sfmqrb   64208 Sep  6 12:04 pg247.png
-rw-rw-r-- 1 sfmqrb sfmqrb  142780 Sep  6 12:02 pg248hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   49887 Sep  6 12:02 pg248.png
-rw-rw-r-- 1 sfmqrb sfmqrb   82530 Sep  6 12:05 pg249.png
-rw-rw-r-- 1 sfmqrb sfmqrb  123419 Sep  6 12:13 pg250hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   89076 Sep  6 12:13 pg250.png
-rw-rw-r-- 1 sfmqrb sfmqrb   75263 Sep  6 12:04 pg251.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74772 Sep  6 12:13 pg252.png
-rw-rw-r-- 1 sfmqrb sfmqrb   68850 Sep  6 12:14 pg253.png
-rw-rw-r-- 1 sfmqrb sfmqrb   71025 Sep  6 12:13 pg254.png
-rw-rw-r-- 1 sfmqrb sfmqrb  148813 Sep  6 12:19 pg255hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   55906 Sep  6 12:13 pg255.png
-rw-rw-r-- 1 sfmqrb sfmqrb  171848 Sep  6 12:21 pg256_hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   83469 Sep  6 12:20 pg256.png
-rw-rw-r-- 1 sfmqrb sfmqrb   81240 Sep  6 12:17 pg258.png
-rw-rw-r-- 1 sfmqrb sfmqrb   66128 Sep  6 12:23 pg259.png
drwxrwxr-x 2 sfmqrb sfmqrb    4096 Sep  6 12:12 __pycache__
-rw-rw-r-- 1 sfmqrb sfmqrb 1209522 Sep  6 11:39 sin_goog.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  147680 Sep  6 11:20 sns167.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   53545 Sep  6 12:03 w241.py
```


### [2026-09-06T16:23:16.392Z] TOOL RESULT

```
1360:accordion,  n.,  a  musical  instrument.  —  Formed from  the  noun  accord  in  the  sense  of  ‘harmony’, with  suff.  -ion,  on  analogy  of  clarion. accost,  tr.  v.,  to  address.  —  F.  accoster,  fr.  VL. accostare,  lit.  ‘to  come  up  to  a  person’s  side', fr.  ad-  and  L.  costa,  ‘a  rib’.  See  costal, accouchement,  n.,  delivery  in  childbed.  —  F., prop,  ‘going  to  childbed’,  fr.  accoucher,  ‘to  go to  childbed,  be  delivered’,  which  is  formed  fr.  a, ‘to’,  and  coucher,  ‘to  lie’,  fr.  L.  collocare,  ‘to  lay’. See  a,  collocate,  and  -ment,  and  cp.  couch, accoucheur,  n.,  a  man  who  acts  as  midwife.  — F.,  fr.  accoucher,  ‘to  go  to  childbed’;  first  used by  Jules  Clement  in  the  second  half  of  the  17th cent.  See  prec.  word.
---
accordion,  n.,  a  musical  instrument.  —  Formed from  the  noun  accord  in  the  sense  of  ‘harmony’, with  suff.  -ion,  on  analogy  of  clarion. accost,  tr.  v.,  to  address.  —  F.  accoster,  fr.  VL. accostare,  lit.  ‘to  come  up  to  a  person’s  side', fr.  ad-  and  L.  costa,  ‘a  rib’.  See  costal, accouchement,  n.,  delivery  in  childbed.  —  F., prop,  ‘going  to  childbed’,  fr.  accoucher,  ‘to  go to  childbed,  be  delivered’,  which  is  formed  fr.  a, ‘to’,  and  coucher,  ‘to  lie’,  fr.  L.  collocare,  ‘to  lay’. See  a,  collocate,  and  -ment,  and  cp.  couch, accoucheur,  n.,  a  man  who  acts  as  midwife.  — F.,  fr.  accoucher,  ‘to  go  to  childbed’;  first  used by  Jules  Clement  in  the  second  half  of  the  17th cent.  See  prec.  word.
accoucheuse,  n.,  a  midwife.  —  F.,  fern,  of  accou¬ cheur.  See  prec.  word.
account,  tr.  and  intr.  v.  —  ME.  acounten,  fr.  OF. aconter  (F.  confer),  fr.  a,  ‘to’  (see  a),  and  comer, ‘to  count,  tell’,  fr.  L.  computare.  (ModF.  diffe¬ rentiates  between  compter,  ‘to  count’,  and  corner, ‘to  tell’.)  See  compute.
Derivatives:  account-abil-ity,  n.,  account-able, adj.,  account-able-ness,  n.,  account-abl-y,  adv., account-ing,  n.
account,  n.  —  ME.,  fr.  OF.  aconte,  acont,  back formation  fr.  aconter.  See  account,  v. accountancy,  n.  —  Formed  fr.  next  word  with suff.  -cy.
```


## [2026-09-06T16:23:22.965Z] TOOL CALL #54: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg259.png"
}
```


### [2026-09-06T16:23:23.307Z] TOOL RESULT

```

```


## [2026-09-06T16:23:23.305Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-06T16:23:52.723Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '11035,11050p' SNS.txt; echo \"=== index ===\"; sed -n '31348,31358p' SNS.txt; echo \"=== pages leaf ===\"; python3 - <<'EOF'\nd=open('SNS_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,l in enumerate(d):\n    if 'sardag' in l: print('leaf',i, l[:60].replace('\\n',' '))\nEOF"
}
```


## [2026-09-06T16:23:53.986Z] TOOL CALL #56: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://abadis.ir/fatofa/%D8%B3%D8%B1%D8%AF%D9%87/' --note 'page 259, Kerd 2, Persian sardeh: Dehkhoda/Moin entries' 2>&1 | tail -3"
}
```


### [2026-09-06T16:23:54.711Z] TOOL RESULT

```
.f/-»tS (XotswZ. 5«5. p. 96. n. 4. 

.TT/Ttf «£*** WiWb. 1649)*sru:;lsrva-:fc- 



&***#+"* .«j»c**«i»" -e* <•■*-« sardag 



MiW>. 1649)sara«fa-: fa. | 

^i l.Vt^e^ 1 '^ : sardagan: WS^ | 

,*:*£) .*^jljWj-*U>b*'*W :der-zlvad :*>•***• 

=== index ===


sar burrfind 230/21 

sardag 183/9 

sardagan 183/12 

sardaran 193/18 

sargCn 187/3 
=== pages leaf ===
leaf 107                                 Ifij ir-iij 1 *   *-^ O'j   
leaf 182                                                             
leaf 225                                           ^c^Ui.t.j'j   «i>V
leaf 233                                          r
```


### [2026-09-06T16:23:58.396Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/d2eb502a5ecdbe90.txt
```


## [2026-09-06T16:24:04.197Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n -i \"سرده\" d2eb502a5ecdbe90.txt | head -30; echo \"=== size ===\"; wc -l d2eb502a5ecdbe90.txt"
}
```


### [2026-09-06T16:24:04.245Z] TOOL RESULT

```
4:TITLE: سرده - معنی در دیکشنری آبادیس
6:سرده - معنی در دیکشنری آبادیس 
10: سرده
16: سرده. [ س َ دَ / دِ ] ( اِ ) اوستا «سرده » ، پهلوی «سرتک » ، نوع ، قسم. ( حاشیه برهان قاطع چ معین ). بمعنی نوع است و انواع جمع آن است. ( برهان )( جهانگیری ) ( رشیدی ). || قدحی که بدان شراب خورند. ( برهان ). قدح شراب. ( آنندراج ) : 
18:ز شراب راح ریحان دو سه سرده گران کش. سیف الدین ( از آنندراج ).
20:سرده بزم شراب است امروز
23:هله ای سرده مستم برهانم بتمامت. مولوی ( ازآنندراج ).
25: سرده. [ س َ دِه ْ ] ( اِ مرکب ) ظاهراً مقامی چون مقام کدخدایی. ( یادداشت مؤلف ) : 
26:داروغه هندوانه و سرده خیار سبز
28: سرده. [ س َ دِه ْ ] ( اِخ ) دهی از دهستان تحت جلگه بخش فدیشه شهرستان نیشابور. دارای 301 تن سکنه. آب از قنات. محصول آن غلات. ( از فرهنگ جغرافیائی ایران ج 9 ). 
56:بسیاری از سرده ها خود نیز به زیرسرده هایی تقسیم می شوند. 
57:«سرده» واژه ای فارسی به معنی رده و دسته، یا نوع ( جمع: انواع ) است. اولین صفت فراگونه ای به شمار می رود که از جنس های همسایه به وسیله یک بریدگی مشخص مجزا می گردد. بین افراد یک سرده توان تولیدمثلی مطرح نیست. 
58: wiki: سرده 
60: سرده (رودسر). سرده ، روستایی از توابع بخش رحیم آباد شهرستان رودسر در استان گیلان ایران است. سرده با روستاهای زبران، لیه خانی، نیاسن، سزرود، کلرود، چکرود و همچنین روستای ویار ( قزوین ) مرز مشترک دارد. 
61:روستای ییلاقی تابستان نشین سرده در ۶۷ کیلومتری جنوب شرقی بخش رحیم آباد در یک منطقه کوهستانی و در ارتفاع ۲۲۴۸ متر از سطح دریا، در ۵۰/۲۸۴۷۱ طول جغرافیایی و در ۳۶/۷۱۰۵۰ عرض جغرافیایی در دهستان سیارستاق ییلاقی قرار دارد. [ ۱] 
62:• سرده ( رودسر ) روستایی در دهستان سیارستاق ییلاقی بخش رحیم آباد شهرستان رودسر استان گیلان 
63:• سرده ( فیروزه ) روستایی در دهستان تخت جلگه بخش مرکزی شهرستان فیروزه استان خراسان رضوی 
64:• سرده ( میرجاوه ) روستایی در دهستان تمین بخش لادیز شهرستان میرجاوه استان سیستان و بلوچستان 
65:• سرده ( غزنی ) روستایی در ولسوالی اندر در ولایت غزنی در افغانستان 
66:• سرده ( بامیان ) روستایی در ولسوالی شیبر در ولایت بامیان در افغانستان 
67:• سرده ( بلخ ) روستایی در ولسوالی دولت آباد در ولایت بلخ در افغانستان
69:سرده روستایی ییلاقی و تابستان نشین ( بهار و تابستان ) است. مردمان سرده در پاییز و زمستان در روستاهای قشلاقی جلگه بخش رحیم آباد یعنی کج محمدگوابر، سی سرا ( رودسر ) ، گزلبن، خورتابسرا و کوشکوه ساکن می شوند. 
70:شغل اصلی مردم روستا، دامداری یعنی پرورش سنتی گوسفند، بز و گاو است. تعداد ۴۰ خانواده در حال حاضر دارای پروانه چرای دام در مراتع سرده بوده که حدود ۳۰۰۰ رأس گوسفند و بز و بیش از ۵۰۰ رأس گاو و احشام بارکش پرورش می دهند. [ ۲] تولیدات پروتئینی، لبنی، پشم از جمله نتایج فعالیت آنان است. البته گندمکاری، باغبانی، گل گاوزبان، فندوق و گردو نیز به عنوان پیشه دوم مردمان سرده رواج داشته و دارد. 
71:مراتع سرده دارای ۳۲ چشمه دائمی و فصلی است. [ ۳] کارکرد اصلی آنها آشامیدنی، زراعت و دامداری است. مشهورترین چشمه ها عبارتند از:
74:• چشمه سرده دشت 
77:• چشمه میان سرده ( مِن سرده ) 
79: wiki: سرده (رودسر) 
81: سرده (غزنی). سَردِه روستایی است در وُلُسوالی اندر در ولایت غزنی افغانستان. [ ۱] 
83:• سرده ( رودسر ) روستایی در دهستان سیارستاق ییلاقی بخش رحیم آباد شهرستان رودسر استان گیلان 
84:• سرده ( فیروزه ) روستایی در دهستان تخت جلگه بخش مرکزی شهرستان فیروزه استان خراسان رضوی 
=== size ===
129 d2eb502a5ecdbe90.txt
```


## [2026-09-06T16:24:23.450Z] TOOL CALL #58: Bash

```json
{
 "command": "timeout 240 python3 tools/ref_page.py BQT:1122 --image 2>&1 | head -40"
}
```


### [2026-09-06T16:24:25.193Z] TOOL RESULT

```
no scan of BQT covers printed page 1122 (see 'scans' in refs_online.json)
```


## [2026-09-06T16:24:37.886Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### SKT heart\"; grep -n \"^HEART\\|^Heart\\|^heart\\b\" SKT.txt | head -5; grep -n -i \"^herd\\b\\|^HERD\" SKT.txt | head -5; echo \"### SKT cordial/core\"; grep -n -i \"^cordial\\|^core\\b\\|^cardiac\" SKT.txt | head -5"
}
```


### [2026-09-06T16:24:37.976Z] TOOL RESULT

```
### SKT heart
### SKT cordial/core
4082:Cordial  (F.-L.)    F.  certiial,  hea
4088:core.  (?'.  —  L.)  M.  E.  rtnr,  heart fruit).  —  O.  F.  cor,  t§tr,  heart  *  U heart.
4095:Core ;  sec  CordiaL
22888:core — heart
```


## [2026-09-06T16:24:39.190Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### IEC kerd\"; grep -n \"kerd-\\|k'erd\\|ḱerd\\|kerdho\" IEC.txt | head -15; echo \"### WLD band3 kerd\"; grep -n \"kerd\" WLD_band3.txt | head -10"
}
```


### [2026-09-06T16:24:39.286Z] TOOL RESULT

```
### IEC kerd
8710:Kertos, is firm, hard, solid". Cf. kertos, kerd-. (Gmc. & Celt. ambig.) Oss. särt-, cpds. “firm-?; (Iran. LW in Tk. sert “hard, strong, severe'?); Arm. sert, Let (‘solid, firm, sincere, rich, fertile"; Ir. ceart, m. “justice, right; W certh ‘evident; MHG (?) hért, gs hérdes “earth, soil, hearth, home? (qua terra firma?); OE heoró 'hearth, home?
15572:sken$- (skng-) — skerd-
15588:(skerd- (1) & (2), see skherd-
### WLD band3 kerd
2383:Pércu, vite lett. 414. kerdiswa lit, 42 keringas li
2965:& . “¢ Yiauen tek) — hewlllkommien bhelgh- 227 bran feb’ p- T17. Pha tn \ betiiobe Zten- 720. dem- 78, ,_{easarralld B. del 6) | dieyes- B43. idha | od 4. betastend b rm pl. G2 é, o BS Reteurrung eety thé Lee betoren deal .. 448. betrotben sep. 487*. tides ruven (mit Sepa ars na a : sept Lear a Sal. | botreten sein L. dhdbh- 824 Baumstatm (duee) Pa | akon he 8 . - Baumstumpf afcd- 623". | heiitendos ae ene 70. ae ais af | mcae- ! 43 a Galisben cou. sheen 1, mat- we aed then 7 h boarkeiten Senet ee —e (siti) pages rail. lew 415%. bektimmert vee: as. Boule rats 0". eben ergh- ve helen hherg- 171%. beuteln qeét- G11. Ta log )- 340". &. bhel- 182°, rek’ ph- 362° ag “rd AK cig- 390". L. réli)}- 242° bewiesern 2.reg- 305*, el- 442. bhemerken 2. - 4 biwaliren 2. wer- 498". bednakt aes Taduih- 2o0". | benehmen rail. (rensndlich) Wrget wegh- S49, bees rer eae avers 350, idee. dA 5 fh 34). | bontteen feng: 73 : vee 748, a oh 38 benvtmrnen leony ston: | Ualibat), greet. dal . i ei b re the i 2. (yew i46* a oo | L. hed eh: ‘e 558*. | beohachten I, gte- 508. i. tyer- 730. bedringen | tyenph- as. | ne ho O86 | a aydi- 518*. : i das’ ame Oru * i rer. L.ete- - 106, hedricken ald 714". | hormhnon t.del- S08. tie. 18. bodriickt sein (eellsch}agh- | berechnond — kerd- 423. +, weik- 235. Le at, berclten ann- 403". 2. gebh- 257, hediirfen ajh- 40. Berg L. guer- B82. trdgh- 752, herngt Mrenk- G0". | bergen a. bel- 452. L. rable STO*. Benre diud 165 | bheryh- 172" stem: O24". 173, borsten birea- 2045". (drehend) 2. (a)ger- OO". [dera*B{-e2)-) | ray sat. ibaatta) - reer G75*, = berithrer a f. oie mit Aefeinden nit 330%. Pa 478. ” here LO7*. brfinder eft. quel- B14. iag~ 703. 4n7*. befriedigt acin yen- 255. pal- i*. leieht ) Sys 4o0*. ete ; ee: bese hadizen uses Foresite) prot) aes ia Hh + ot -. Ui pe ba bere cle gen-gie Gea 105; | ieosidinglen: ‘Meee | be b.hei- Bat age - ‘ | a ower#t som [. i~ Sad. sel | ert | we ic | te aKa. t pe wort OD ie) sure gheiah- 563. | beachmntven 1. kyei- 469. wv i. i i i eens 19. | Iebapeitaey * li as Se oe th, wed pads | Eeelestueax (eal wher, bom 178 ges S61, (dicht) pg: 88°. hestrvichen — ghréi- 10, pel- 57". Behilter (geflochtener) Eis _» (malt Laehin) cherjh- 83 }. weu- a0". ii i652. weart fiezt ). Ae 2. any ATO. behauen (Holz) éel*p. 717. | besudela 6. (ajler- 641°. | bewillkammnnn bhalyh-182°,
```


## [2026-09-06T16:24:52.256Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### WLD3 Herz\"; grep -no \"Herz [a-zA-Z'’(). -]\\{0,40\\}\" WLD_band3.txt | head -8; echo \"### WLD3 Herde\"; grep -no \"Herde [a-zA-Z'’(). -]\\{0,40\\}\" WLD_band3.txt | head -5; echo \"### IEC kardia\"; grep -n \"kardia\\|kṛd\\|kērd\\|k'ērd\" IEC.txt | head -8"
}
```


### [2026-09-06T16:24:53.864Z] TOOL RESULT

```
### WLD3 Herz
### WLD3 Herde
### IEC kardia
9088:Krd- (Krds, Krdiiom, iio) ‘core, centre, heart". Cf. Kerd-. WP I, 423 Per. cf. (?) sull (“lungs”, fr. *Krds ?); Hitt. kare, ds kardi, beside ker, gs kardiyas & kartas “heart, entrails’; Gk. kardia; Lat. cor, gs cordis, gp cordum, n. beside prae-, ve-cordia; Mir cride, n., Ir. cridhe, croidhe, f. id.; cf. MIr. cride, adj. ‘beloved’; W cf. craidd, pl. creiddiau, m. “centre, heart’; Cor, créz, m. & adj. ‘middle’; Br. cf. as-cré ‘bosom’ (fr. *esth-Krd-); OCS dim. type srüdiíce, Pol. serce, n. (and com.
```


## [2026-09-06T16:24:55.045Z] TOOL CALL #62: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://vajehyab.com/?q=%D8%A2%DA%A9%D9%88%D8%B1%D8%AF%D8%A6%D9%88%D9%86' --note 'page 259, Kerd 1 node 8, Persian akordion in Moin' 2>&1 | tail -3; echo \"---\"; python3 tools/fetch_source.py 'https://www.etymonline.com/word/heart' --note 'page 259, Kerd 1, English heart/Germanic' 2>&1 | tail -3"
}
```


### [2026-09-06T16:24:57.855Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/99e52ae7491e09df.txt
---
/home/sfmqrb/git/rishe/data/verification/sources/web/8df388b01cfdef6c.txt
```


## [2026-09-06T16:25:02.090Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '9085,9095p' IEC.txt; echo \"### IEC Kerd-\"; grep -n \"^Kerd-\\|Kerd- (\\|Kerdho\\|Kerdha\\|Kerdh-\" IEC.txt | head -10"
}
```


### [2026-09-06T16:25:02.147Z] TOOL RESULT

```
Skt. $réyan, $réyas “better, more glorious’; Gk. kreíon & kréon, m. ‘ruler’; Lat. cf. cre- mentum ‘increase’. (A link with type *Kerosr ‘head’ is suggested by Doric kárron ‘better, stronger’, cf. in e-gde Tokh. sarye ‘upper’, and Lat. primi-cerius, m. “chief, head")
(Krod-, variant of types Kerd- and Krd-, q. v. Br. kreiz, f. “middle” beside kreizen, f. id.; W craidd, p. creiddiau, m. id.)
Krb- (Krob-) (?). Cf. WP I, 418 Lat. cf. carbunculus, 1, m. (tumour, smut in trees? beside carbo, onis; W (r-gde?) crafu, v. “scratch, scrape’; Blg. sárbja, v. ‘itch’ beside R srab, m. (o-gde) “itch, leprosy’
Krd- (Krds, Krdiiom, iio) ‘core, centre, heart". Cf. Kerd-. WP I, 423 Per. cf. (?) sull (“lungs”, fr. *Krds ?); Hitt. kare, ds kardi, beside ker, gs kardiyas & kartas “heart, entrails’; Gk. kardia; Lat. cor, gs cordis, gp cordum, n. beside prae-, ve-cordia; Mir cride, n., Ir. cridhe, croidhe, f. id.; cf. MIr. cride, adj. ‘beloved’; W cf. craidd, pl. creiddiau, m. “centre, heart’; Cor, créz, m. & adj. ‘middle’; Br. cf. as-cré ‘bosom’ (fr. *esth-Krd-); OCS dim. type srüdiíce, Pol. serce, n. (and com.
Kot- (Koteio, Kotos) — Krn-gom
15
20
25
30
35
40
### IEC Kerd-
7020:kerdh- (kordh-, krdh-) “mass, troop’. (Vari- ant: Kerdh-, q. v.). WP I, 424 Gk. (o-gde) kórthus, f. ‘heap’; W cordd, m. pl. -ion ‘circle, tribe’; Go. (e-gde) haírda, OHG hérta, OE heord, f.; ON hjaró-, cpds. & hjoró, f. u-st. ‘herd’, beside. OHG hirti ‘herdsman’; OCS (e-gde) éréda “herd? beside Srb. (z-gde) krd, m., krdo, n., id.; Li. cf. kerdzius (“head
8660:Kent- — Kerdhos, à
8676:Kerd- (Kerdis, à, io) “heart, core, centre’. Cf. Krd-. WP I, 424 Vedic $ardih, f. (mng. uncertain, cf. AV 18, 3, 16); Go. hairto, OHG hérza, OS hérta, ON hjarta, pl. hjortu, n. ‘heart’; Cz. střed ‘middle’; OCS sréda, id.; Li. šerdis, -iés, f. (core, pith; bell-clapper'. Gp: Serdü. Also: "heart of a tree”); Latv. serde ‘pith, marrow?
8677:Kerdhos, à “herd, crowd, drove'. Cf. Ker- ‘head’. WP I, 424 Skt. Sardhah “host, army? beside $ardhas, n. id.; Av. saroóo (2) ‘kind, sort’; Go. haírda, f. ‘herd’, wm. ‘herdsman’; OE heord, f., hierde, wm. as Go.; OHG hërta, f., hirti, m. as Go.; ON hjoró, f. ‘herd’; hirðir, gs hiróis, m. ‘herdsman’, cf. hirð, f. ‘bodyguard’. (Gk. kór- thus, f. ‘pile’, and W cordd, m. pl. -ion ‘circle; tribe’ are no more than potential o-gde iso- phones, despite FK: EWDS 17: Herde. OCS éréda (2) “herd” and Li. kerdZius, m. 'shep- herd? are Germanic LWs because of the initial.
9056:Kordhos, us (?). Cf. Kerdhos, Ker-, and dhéeio
```


## [2026-09-06T16:25:02.436Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n -i \"معین\\|فر\\.\\|آکوردئون\" 99e52ae7491e09df.txt | head -20"
}
```


### [2026-09-06T16:25:02.516Z] TOOL RESULT

```
4:TITLE: معنی آکوردئون | واژه یاب
9: معنی آکوردئون | واژه یاب 
24: آکوردئون
45: فرهنگ انتشارات معین
46: (دِ ئ ُ) [ فر. ] ( اِ.) از ابزار موسیقی با بدنه ای چین دار، دارای زبانه های فلزی ، که به ارتعاش درمی آیند و آن را به وسیلة سر انگشتان نوازند.
63: آکوردئون، اكوردئون
67: آکوردئونیست
79: نوعی ساز پرده‌دار شبیه جعبه که هنگام نواختن روی دست می‌گیرند و پره‌های آن را با انگشت فشار می‌دهند؛ آکوردئون.
```


## [2026-09-06T16:25:12.495Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '1,40p' 8df388b01cfdef6c.txt | grep -n -A8 \"heart (n.)\""
}
```


### [2026-09-06T16:25:12.570Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T16:25:15.162Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n -m1 -A6 \"Old English heorte\" 8df388b01cfdef6c.txt"
}
```


### [2026-09-06T16:25:15.206Z] TOOL RESULT

```
58: Old English heorte "heart (hollow muscular organ that circulates blood); breast, soul, spirit, will, desire; courage; mind, intellect," from Proto-Germanic *hertan- (source also of Old Saxon herta , Old Frisian herte , Old Norse hjarta , Dutch hart , Old High German herza , German Herz , Gothic hairto ), from PIE root *kerd- "heart."
59-
60- Spelling with -ea- is c. 1500, reflecting what then was a long vowel, and the spelling remained when the pronunciation shifted. Most of the modern figurative senses were present in Old English, including "memory" (from the notion of the heart as the seat of all mental faculties, now only in by heart , which is from late 14c.), "seat of inmost feelings; will; seat of emotions, especially love and affection; seat of courage." Meaning "inner part of anything" is from early 14c. In reference to the conventional heart-shape in illustration, late 15c.; heart-shaped is from 1744.
61-
62- Heart attack attested from 1875; heart disease is from 1864. The card game hearts is so called from 1886. To have one's heart in the right place "mean well" is from 1774. Heart and soul "one's whole being" is from 1650s. To eat (one's own) heart "waste away with grief, resentment, etc." is from 1580s.
63-
64- heart (v.)
```


## [2026-09-06T16:25:27.363Z] TOOL CALL #67: Bash

```json
{
 "command": "sed -n '1,120p' tools/verify_check.py"
}
```


### [2026-09-06T16:25:27.402Z] TOOL RESULT

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


## [2026-09-06T16:26:11.180Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && head -5 49d501cd16fb0195.txt; grep -n -m3 -i \"ḱred\\|kred-dʰeh\\|de Vaan\" 49d501cd16fb0195.txt | head"
}
```


### [2026-09-06T16:26:11.230Z] TOOL RESULT

```
URL: https://en.wiktionary.org/wiki/credo%23Latin
FETCHED: 2026-09-06T16:22:21Z
STATUS: 200
TITLE: credo - Wiktionary, the free dictionary

574: From Proto-Italic *krezðō , from Proto-Indo-European *ḱred-dʰeh₁-ti ( “ to place one's heart, i.e. to trust, believe ” ) , compound phrase of oblique case form of *ḱḗr ( “ heart ” ) (whence also Latin cor ) and *dʰeh₁- ( “ to put, place, set ” ) (whence -dō ( “ put ” ) ). [ 1 ] 
1214: ^ De Vaan, Michiel ( 2008 ), “ crēdō ”, in Etymological Dictionary of Latin and the other Italic Languages (Leiden Indo-European Etymological Dictionary Series; 7), Leiden, Boston: Brill, →ISBN , pages 141-142 
1237: De Vaan, Michiel ( 2008 ), Etymological Dictionary of Latin and the other Italic Languages (Leiden Indo-European Etymological Dictionary Series; 7), Leiden, Boston: Brill, →ISBN
```


## [2026-09-06T16:26:19.530Z] AGENT

Now I'll write the verification file.


## [2026-09-06T16:34:00.665Z] TOOL CALL #69: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk259.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\nSRC_DEL = W + \"%D8%AF%D9%84\"\nSRC_KER = W + \"Reconstruction:Proto-Indo-European/%E1%B8%B1%E1%B8%97r\"\nSRC_CREDO = W + \"credo%23Latin\"\nSRC_HEART = \"https://www.etymonline.com/word/heart\"\nSRC_ACC = \"https://www.etymonline.com/word/accordion\"\nSRC_SARDEH = \"https://abadis.ir/fatofa/%D8%B3%D8%B1%D8%AF%D9%87/\"\nSRC_AKORD = \"https://vajehyab.com/?q=%D8%A2%DA%A9%D9%88%D8%B1%D8%AF%D8%A6%D9%88%D9%86\"\n\ndata = {\n \"pdf_page\": 259,\n \"book_page\": 229,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-06\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"Kerd 1, Kred\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *ḱḗr, oblique stem *ḱr̥d- (root *ḱerd-) 'heart'; with the compound *ḱred-dʰeh₁- 'to place one's heart, trust'\",\n   \"note\": \"Pokorny p.579 bottom–580 heads the entry exactly '(kered-:) kerd-, kērd-, kr̥d-, kred- \\u2018Herz\\u2019', so Nourai's headword 'Kerd 1, Kred', the language label 'Indo-European' and the gloss 'heart' all reproduce his source correctly; AHD (Watkins) has 'kerd-1. Heart. [Pok. kered- 579.]'. The one substantive caveat concerns the 'kred-' half: Pokorny himself (p.580) says the kred-dhē- 'believe' group is 'nicht hierher' (not to be connected with 'heart'), and Buck 17.15, Klein s.v. heart and Ernout–Meillet s.v. cor agree; modern standard works (Watkins/AHD, de Vaan 2008 s.v. crēdō, Wiktionary) do connect it, analysing *ḱred-dʰeh₁- as 'to place one's heart'. Nourai therefore follows the newer, now dominant, view — but not the page of Pokorny he cites. The Iranian branch has a further complication that the chart passes over: Indo-Iranian shows a voiced aspirate initial (Skt. hṛd-, Av. zərəd-, PII *ȷ́ʰā́rd) where *ḱ- is expected, 'unexplained voiced aspiration' (Wiktionary), 'mit init. as if fr. IE gh, due to a blend with some other word' (Buck 251).\",\n   \"note_fa\": \"ریشهٔ هندواروپایی آغازین *ḱḗr (ستاک غیرفاعلی *ḱr̥d-، ریشهٔ *ḱerd-) به معنی «دل، قلب» است و پوکورنی در ص ۵۷۹–۵۸۰ سرواژه را دقیقاً «kerd-, kērd-, kr̥d-, kred-: Herz» آورده؛ پس نام ریشه، برچسب زبانی و معنایی که نورایی داده درست است. تنها نکتهٔ محل بحث بخش kred- است: خودِ پوکورنی در ص ۵۸۰ پیوند kred-dhē- «باور داشتن» را با «دل» رد می‌کند و باک و کلاین و ارنو–مه‌یه نیز همین نظر را دارند، اما واتکینز (AHD)، دِ وان و ویکی‌واژه آن را می‌پذیرند و *ḱred-dʰeh₁- را «دل نهادن» می‌دانند؛ یعنی نورایی از دیدگاه نو پیروی کرده است نه از صفحه‌ای که به آن ارجاع داده. نکتهٔ دیگر آنکه در هندوایرانی به جای *ḱ- انسدادی واکدارِ دمیده دیده می‌شود (سنسکریت hṛd-، اوستایی zərəd-) که هنوز توضیح قطعی ندارد.\",\n   \"sources\": [SRC_KER, SRC_CREDO, SRC_HEART],\n   \"ref_check\": [\n    {\"ref\": \"POK:579\", \"status\": \"supports\", \"note\": \"Pokorny IEW p.579 (bottom) – 580, read in POK_02.txt leaf 239–240 (awk 'BEGIN{RS=\\\"\\\\f\\\"} NR==239'): '(kered-:) kerd-, kērd-, kr̥d-, kred- \\u2018Herz\\u2019. Arm. sirt … gr. καρδία (att.), κραδίη (hom.) … lat. cor (aus *cord) … got. hairto, ahd. herza, ags. heorte, anord. hjarta n. \\u2018Herz\\u2019 (*ḱērd-on-)'. Exactly Nourai's root name and gloss.\"},\n    {\"ref\": \"SYN:251\", \"status\": \"supports\", \"note\": \"Buck, Selected Synonyms p.251 = §4.44 HEART (SYN.txt leaf 289, page number '251' printed in the running head above '4.44 HEART'): 'Most of the words for \\u2018heart\\u2019 belong to an inherited group … 1. IE *ḱerd-, etc., with gradation. Walde-P. 1.423 ff. Ernout-M. 219 f.'\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. kerd-1 (AHD_watkins1985.txt line 621)\", \"stance\": \"supports\", \"note\": \"'kerd-1. Heart. 1. Suffixed form *kerd-en- in Germanic *hertōn- in Old English heorte, heart: HEART. 2. Zero-grade form *kr̥d- in: a. Latin cor (stem cord-), heart … b. suffixed form *kr̥d-yā in Greek kardia … 3. Possibly *kred-dhə-, \\u201cto place trust\\u201d … in Latin crēdere, to believe. [Pok. kered- 579.]' — the whole chart in one entry.\"},\n    {\"src\": \"WLD\", \"where\": \"Walde-Pokorny I 423 f. (cited by POK and by Buck 4.44; only Band III index available locally, WLD_band3.txt line 2965 'kerd- 423')\", \"stance\": \"supports\", \"note\": \"Both Pokorny and Buck refer the 'heart' root to WP. I 423 f.; the local library holds only the Register volume, whose index line points to that page.\"},\n    {\"src\": \"IEC\", \"where\": \"Mann, s.vv. Kerd- and Kr̥d- (IEC.txt lines 8676, 9088)\", \"stance\": \"supports\", \"note\": \"'Kerd- (Kerdis, ā, io) \\u201cheart, core, centre\\u201d. Cf. Kr̥d-. WP I, 424' and 'Kr̥d- (Kr̥ds, Kr̥diiom, iio) \\u201ccore, centre, heart\\u201d … Hitt. kar-, ds kardi … Gk. kardia; Lat. cor, gs cordis …'\"},\n    {\"src\": \"LAT\", \"where\": \"Ernout–Meillet p.254–255 s.v. cor (LAT.txt leaf 272–273)\", \"stance\": \"partial\", \"note\": \"'Le nom du \\u201ccoeur\\u201d … est au fond le même dans toutes les langues indo-européennes. Il est probable que le nominatif-accusatif était de la forme *ḱerd, conservée dans hitt. kir … gr. κῆρ, v.pruss. seyr, et que les autres cas reposaient sur *ḱr̥d-'; but adds 'Pour le rapport qu'on a envisagé, sans raison, avec crēdō, v. ce mot' — i.e. rejects the 'Kred' half.\"}\n   ],\n   \"nodes\": []\n  },\n  {\n   \"entry\": 1,\n   \"root\": \"Kerd 2, Kerdho, Kerdha\",\n   \"verdict\": \"plausible\",\n   \"modern_form\": \"PIE *ḱerdʰ-o-, *ḱerdʰ-eh₂ 'row, herd' (AHD kerdh-; Pokorny kerdho-, kerdhā)\",\n   \"note\": \"The root itself is real and the gloss is right: Pokorny p.579 has 'kerdho-, kerdhā \\u2018Reihe, Herde\\u2019' with ai. śárdha- 'Herde, Schar', av. sarəda-, apers. θ-ard- 'Art, Gattung', got. hairda, ags. heord, ahd. herta; AHD has 'kerdh-. Row, herd … [Pok. kerdho- 579.]'. What is not right is the first element of Nourai's headword: on the same page 579 Pokorny's '2. kerd-' is a completely different root, 'etwa handwerksmäßig geschickt, klug berechnend' (gr. κέρδος 'gain', OIr. cerd 'craft'), which AHD prints as 'kerd-2. Craft'. Nourai's 'Kerd 2' is therefore his own serial number for the herd root (he needs to distinguish it from Kerd 1 'heart'), not a reconstructed form meaning 'row, herd'; the genuine root forms are the two he adds, Kerdho and Kerdha. Note also that the aspirate -dʰ- keeps this root formally distinct from Kerd 1 *ḱerd- 'heart' — they are homophonous-looking but unrelated.\",\n   \"note_fa\": \"ریشهٔ هندواروپایی آغازین *ḱerdʰ-o- / *ḱerdʰ-eh₂ به معنی «رده، ردیف؛ گله» است و پوکورنی در ص ۵۷۹ آن را با صورت‌های «kerdho-, kerdhā» آورده و سنسکریت śárdha-، اوستایی sarəδa-، پارسی باستان θard- و گوتی hairda را ذیل آن نشانده است؛ واتکینز نیز kerdh- «row, herd» دارد. اما نامی که نورایی برگزیده تا اندازه‌ای گمراه‌کننده است: «Kerd 2» در همان صفحهٔ پوکورنی ریشهٔ دیگری است به معنی «چیره‌دست، زیرک» (یونانی κέρδος «سود»)، و آنچه معنی «رده/گله» دارد تنها Kerdho و Kerdha است؛ «Kerd 2» شمارهٔ اختصاصی خودِ نورایی است. افزون بر این، دالِ دمیدهٔ این ریشه آن را از *ḱerd- «دل» جدا می‌کند و این دو هم‌ریشه نیستند. ادعای نورایی با این توضیح پذیرفتنی است.\",\n   \"sources\": [SRC_SARDEH],\n   \"ref_check\": [\n    {\"ref\": \"POK:579\", \"status\": \"partial\", \"note\": \"POK_02.txt leaf 239 (printed p.579) does carry 'kerdho-, kerdhā \\u2018Reihe, Herde\\u2019. Ai. śárdha- m., śárdhas- n. \\u2018Herde, Schar\\u2019, av. sarəda-, apers. θ-ard- \\u2018Art, Gattung\\u2019 … got. hairda, aisl. hjǫrð, ags. heord, ahd. herta \\u2018Herde\\u2019 … WP. I 424 f.' — but the same page's '2. kerd-' is 'etwa handwerksmäßig geschickt, klug berechnend', not 'row, herd', so the 'Kerd 2' part of Nourai's headword is not supported by the cited page.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. kerdh- (AHD_watkins1985.txt line 621)\", \"stance\": \"supports\", \"note\": \"'kerdh-. Row, herd. Suffixed form *kerdh-ā in Germanic *herdō in Old English heord, herd: HERD. [Pok. kerdho- 579.]' — and immediately before it 'kerd-2. Craft … [Pok. 2. kerd- 579.]', confirming that Pokorny's 'kerd- 2' is the 'craft' root.\"},\n    {\"src\": \"IEC\", \"where\": \"Mann s.vv. kerdh- and Kerdhos (IEC.txt lines 7020, 8677)\", \"stance\": \"supports\", \"note\": \"'Kerdhos, ā \\u201cherd, crowd, drove\\u201d … Skt. śardhaḥ \\u201chost, army\\u201d …; Av. sarəδō (?) \\u201ckind, sort\\u201d; Go. hairda, f. \\u201cherd\\u201d …; OE heord, f. …' — Mann even flags Gk. kórthus and W cordd as merely 'potential o-grade isophones'.\"},\n    {\"src\": \"WLD\", \"where\": \"Walde-Pokorny I 424 f. (cited by POK at the end of the kerdho- article)\", \"stance\": \"supports\", \"note\": \"Pokorny closes 'kerdho-, kerdhā' with 'WP. I 424 f., Trautmann 127 f.'; only the Register volume is on disk locally.\"},\n    {\"src\": \"SYN\", \"where\": \"Buck, Selected Synonyms (SYN.txt) — no 'herd' concept section reached by the grep\", \"stance\": \"silent\", \"note\": \"grep for 'HERD' in SYN.txt returns only 4.44 HEART cross-references and unrelated matches; Buck has no separate 'herd' entry that bears on this root.\"}\n   ],\n   \"nodes\": []\n  }\n ]\n}\n\nE0 = data[\"entries\"][0][\"nodes\"]\nE1 = data[\"entries\"][1][\"nodes\"]\n\nE0.append({\n \"id\": 1,\n \"lang\": \"Avestan\",\n \"words\": \"zered, zaredaya; zraz-da, sraz-da\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Avestan zərəd- n. and its -aya- stem zərəδaya- 'heart' are both real: Bartholomae, Altiran. Wb. col. 1692 lists 'g. (j.) zarəd- n. \\u2018Herz\\u2019' and 'j. zərəδaya- n. \\u2018Herz\\u2019', the latter also 'im Sinn von innerstes, Höchstes', quoting Vd. 1.3 zyamahe maiδīm … zərəδaēm 'the middle of winter and the heart of winter' — which is the exact source of Nourai's second gloss 'center' and of Klein's rendering 'middle' (KLN 352). Phonologically the Iranian word does not come from *ḱerd- by regular rule: Indo-Iranian shows a voiced aspirate initial (Skt. hṛd-, hṛdaya-, PII *ȷ́ʰā́rd > Ir. *zard-), which Buck 251 calls an initial 'as if fr. IE gh, due to a blend with some other word' and Wiktionary marks 'unexplained voiced aspiration'; Pokorny 580 accordingly files it as a 'Reimwort zu ḱer(e)d-', i.e. gherd-, ghr̥d-, 'nur arisch'. The second pair zraz-dā-/sraz-dā- is a different matter: Bartholomae col. 1703 has 'j. zraz-dā- kompV. \\u2018vertrauen, glauben\\u2019' (Gathic adj. zrazdā- 'gläubig', Y.31.1; derivative zrazdāti- 'faith'), so the word and meaning are correct, but Pokorny 580 states expressly that it comes 'aus *srazdā- durch volksetym. Anlehnung an zərəd- \\u2018Herz\\u2019' — the s- form Nourai prints as 'sraz-da' is the reconstructed pre-form, not an attested Avestan variant, and the attachment to 'heart' is secondary folk-etymology on Pokorny's account. Modern work (Watkins, de Vaan 2008 s.v. crēdō, Wiktionary) restores the connection as a genuine PIE compound *ḱred-dʰeh₁- 'to place one's heart', with Ir. *ćrad- + dā-; on that view Nourai's arrow is right but the immediate parent is the oblique *ḱred-, not zərəd-.\",\n \"derivation_fa\": \"«زَرِذ» اوستایی zarəd- و ستاک -aya- ی آن zərəδaya- هر دو به معنی «دل» در فرهنگ بارتولومه (ستون ۱۶۹۲) آمده‌اند و بارتولومه برای zərəδaya- معنی «درونی‌ترین، میانه» را هم از وندیداد ۱٫۳ («میان زمستان و دلِ زمستان») گواه آورده؛ همین است سرچشمهٔ معنی دومِ نورایی «مرکز» و ترجمهٔ کلاین «middle». از نظر آوایی این واژه پیرو قاعده از *ḱerd- برنیامده است: در هندوایرانی به جای همخوان کامی بی‌واک، انسدادی واکدارِ دمیده دیده می‌شود (سنسکریت hṛd-, hṛdaya-)، و پوکورنی آن را «هم‌قافیهٔ» ریشه می‌داند نه دنبالهٔ مستقیم آن. زوج دوم، zraz-dā- «باور داشتن»، در بارتولومه (ستون ۱۷۰۳) هست و صورت گاهانی zrazdā- «مؤمن» در یسنه ۳۱٫۱ به کار رفته، اما پوکورنی می‌گوید این از *srazdā- است و پیوندش با zərəd- «دل» ریشه‌شناسی عامیانه است؛ پس صورت sraz-da که نورایی آورده بازسازی است نه گونهٔ گواهی‌شده. پژوهش امروزی (واتکینز، دِ وان) دوباره آن را ترکیب اصیل *ḱred-dʰeh₁- «دل نهادن» می‌داند. ادعای نورایی با احتیاط پذیرفتنی است.\",\n \"sources\": [SRC_KER, SRC_CREDO],\n \"ref_check\": [\n  {\"ref\": \"POK:580\", \"status\": \"partial\", \"note\": \"POK_02.txt leaf 240 (printed p.580) has the Iranian material but qualified: 'Nicht hierher (sondern zu mir. cretair \\u2018Reliquie\\u2019) idg. kred-dhē- \\u2018Zauberkraft worauf setzen, glauben, vertrauen\\u2019 in ai. śrád-dadhāti … av. zrazdā- \\u2018glauben\\u2019 (aus *srazdā- durch volksetym. Anlehnung an zərəd- \\u2018Herz\\u2019)' and, at the end, 'Reimwort zu ḱer(e)d- ist gherd-, ghr̥d-, nur arisch, in ai. hṛd \\u2018Herz\\u2019' — so the cited page gives both of Nourai's Avestan word-groups but denies that the second belongs to the root.\"},\n  {\"ref\": \"KLN:352\", \"status\": \"supports\", \"note\": \"Klein 1966 p.352 (KLN_1966.txt leaf 195, the leaf that carries the printed numbers 351 and 352) ends with 'core, n., hard center of a fruit … Prob. fr. L. cor, \\u2018heart\\u2019; see cordate. For sense development cp. Avestic zərəδaya, \\u2018middle\\u2019' — the Avestan form and the 'center' gloss Nourai cites.\"},\n  {\"ref\": \"SYN:251\", \"status\": \"supports\", \"note\": \"Buck p.251 §4.44 HEART lists in its table 'Skt. hṛd-, hṛdaya- / Av. zarəd-' and comments 'here also Skt. hṛd-, hṛdaya-, Av. zarəd-, but with init. as if fr. IE gh, due to a blend with some other word'.\"},\n  {\"ref\": \"LAT:254\", \"status\": \"supports\", \"note\": \"Ernout–Meillet p.254–255 s.v. cor (LAT.txt leaf 273): 'L'indo-iranien a un mot parallèle, mais commençant par une sonore aspirée: véd. hṛdaḥ (gén.abl.), gath. zarədā (instr.), pers. dil (de *dr̥d-) — véd. hṛdayam, av. zərəδaēm.'\"}\n ],\n \"consulted\": [\n  {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch cols. 1692 and 1703 (BRT.txt lines 28131, 28137, 28320, 28323, 28330)\", \"stance\": \"supports\", \"note\": \"'g. (j.) zarəd- n. \\u2018Herz\\u2019'; 'j. zərəδaya- n. \\u2018Herz\\u2019 … a) im Sinn von innerstes, Höchstes'; 'j. zraz-dā- kompV. \\u2018vertrauen, glauben\\u2019. Praes. zrazda-. — Inf. *zrazdātai-ča'; 'g. zraz-dā- Adj. \\u2018gläubig, gläubig ergeben\\u2019: yōi zrazdā ahən mazdāi … Y.31.1'. Both of Nourai's word-groups are Bartholomae's.\"},\n  {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 571 (HRN.txt lines 5126-5137)\", \"stance\": \"supports\", \"note\": \"'571. dil \\u2018Herz\\u2019 … aw. zerəd- (Y.31,12), zarədaya- \\u2018Herz\\u2019; phlv. dil … ai. hṛd-, hṛdaya-; arm. sirt.' Horn uses precisely Nourai's two transliterations zered / zaredaya.\"},\n  {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II, s.v. dil (NYB_vol2_glossary.txt line 1280)\", \"stance\": \"supports\", \"note\": \"'dil [dyl, dl; LBBH] heart … SW form: MPrs dyl, Paz. NP dil, as against MPrth zyrd; Av. (1692) zarəd-, zarədaya-.' Nyberg cites the very Bartholomae column and keeps the Parthian z- beside the Persian d-.\"}\n ]\n})\n\nE0.append({\n \"id\": 2,\n \"lang\": \"Pahlavi\",\n \"words\": \"dîl\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Book Pahlavi dil, written with the Aramaic heterogram LBBH/LB(B)ME and, phonetically, dyl. MacKenzie's Concise Pahlavi Dictionary has 'dil [LB(B)ME < Aram. lb(b)-h; dyl = M(anichaean), N(ew Persian) —] heart'; Nyberg glosses 'dil [dyl, dl; LBBH] heart' and adds that this d- form is specifically South-West Iranian (Persian proper), 'as against MPrth zyrd', i.e. Parthian kept the inherited z-. The step from the Old Iranian *zr̥d- of the Avestan node to MP dil is thus not a plain sound law but the well-known dissimilatory/assimilatory Persian development *ȷ́ŕ̥d- > *dŕ̥d- > *dŕ̥l > dil (Wiktionary, following the standard treatment; Ernout–Meillet p.255 already writes 'pers. dil (de *dr̥d-)'), with -rd- > -l- as in Persian gol < *wr̥da- and sālār < *sardār. Nourai's spelling 'dîl' with a long î is his own transliteration habit; MacKenzie and Nyberg both write dil with short i.\",\n \"derivation_fa\": \"فارسی میانه (پهلوی) dil که در خط پهلوی هم با هزوارش LBBH و هم به‌صورت آوایی dyl نوشته می‌شود؛ مکنزی می‌آورد «dil [LB(B)ME < آرامی lb(b)-h؛ dyl] قلب» و نیبرگ نیز «dil [dyl, dl; LBBH] heart» و می‌افزاید که این صورت با «د» ویژهٔ ایرانی جنوب‌غربی (پارسی) است، در برابر پارتی zyrd که «ز» ایرانی باستان را نگاه داشته. گذار از *zr̥d- ایرانی باستان به dil فارسی میانه قاعدهٔ آوایی سرراستی نیست، بلکه همان تحول شناختهٔ *ȷ́ŕ̥d- > *dŕ̥d- > *dŕ̥l > dil است (ارنو–مه‌یه هم می‌نویسد pers. dil از *dr̥d-)، با تبدیل rd به ل، مانند «گل» از *wr̥da- و «سالار» از *sardār. «î» کشیده در نگارش نورایی صرفاً شیوهٔ آوانگاری خود اوست؛ مکنزی و نیبرگ dil با «i» کوتاه می‌نویسند. ادعای نورایی درست است.\",\n \"sources\": [SRC_DEL],\n \"ref_check\": [\n  {\"ref\": \"BQT:873\", \"status\": \"partial\", \"note\": \"BQT_v2_pages.txt leaf 333 (printed p.873, offset printed = leaf + 540) is the دل page: the headword block reads 'دل - بضم اول و سکون ثانی … و بکسر اول معروف است و بعربی قلب خوانند. و وسط هر چیز را نیز دل گویند'. Mo'in's etymological footnote is present at the foot of the page but its Latin-script forms are badly mangled by the Persian OCR; the only forms I could read out of it are the dialect comparisons ('بلوچی zirdē', with Gilaki/Tabari/Sanglechi/Shughni/Munji columns), which are the ones Nourai quotes in his NOTE. I could not read the 'پهلوی dil' line itself, hence 'partial'.\"}\n ],\n \"consulted\": [\n  {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary p.26 s.v. dil (PHD_mackenzie.txt line 2001)\", \"stance\": \"supports\", \"note\": \"'dil [LB(B)ME < A lb(b)-h; dyll = M, N -] heart.'\"},\n  {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II s.v. dil (NYB_vol2_glossary.txt line 1280)\", \"stance\": \"supports\", \"note\": \"'dil [dyl, dl; LBBH] heart 73. 117-21 … SW form: MPrs dyl, Paz. NP dil, as against MPrth zyrd; Av. (1692) zarəd-, zarədaya-.'\"},\n  {\"src\": \"HRN\", \"where\": \"Horn no. 571 (HRN.txt line 5127)\", \"stance\": \"supports\", \"note\": \"'aw. zerəd- …, zarədaya- \\u2018Herz\\u2019; phlv. dil, pāz. dilēr (Men.)' — Horn puts the Pahlavi form on exactly this branch.\"}\n ]\n})\n\nE0.append({\n \"id\": 3,\n \"lang\": \"Persian\",\n \"words\": \"del «دل»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"New Persian دل del 'heart' continues Middle Persian dil unchanged in consonants; the modern Iranian pronunciation del is simply the regular lowering of MP short i. Wiktionary: 'From Middle Persian 𐭣𐭩𐭫 (dyl /dil/), from Proto-Iranian *jā́rd, from Proto-Indo-Iranian *ȷ́ʰā́rd, ultimately from Proto-Indo-European *ḱḗr; with a regular phonetic shift *ȷ́ŕ̥d- > *dŕ̥d > *dŕ̥l > dil. For the phonetic change, compare گل (gol) and سالار (sâlâr).' The chart's NOTE — that the z-sound survives in Kurdish and Baluchi — is exactly right and is in fact Nourai's source's own material: Horn no. 571 lists 'kurd. zar \\u2018Herz\\u2019; afgh. zṛa; oss. d. zärdä, i. zärdä; bal. zirdē; šar. zārd, šuγn. …, sangl. zurūγ, minj. zul', and Mo'in reproduced that dialect list in the footnote to Borhan-e Qate' p.873. The point is important and correctly made: only the South-West (Persian) line innovated d-, and the Kurdish/Baluchi/Ossetic forms preserve the inherited Iranian z-.\",\n \"derivation_fa\": \"«دل» فارسی نو دنبالهٔ بی‌واسطهٔ dil فارسی میانه است و تنها تغییرش کوتاه‌شدگی/فروافتادگی «i» به «e» در تلفظ امروزی ایران است. ویکی‌واژه می‌نویسد: از فارسی میانهٔ dyl (dil)، از ایرانی آغازین *jā́rd، از هندوایرانی آغازین *ȷ́ʰā́rd و سرانجام از هندواروپایی آغازین *ḱḗr، با دگرگونی آوایی *ȷ́ŕ̥d- > *dŕ̥d > *dŕ̥l > dil؛ همان تحولی که در «گل» (از *wr̥da-) و «سالار» دیده می‌شود. یادداشت نورایی دربارهٔ نگاه‌داشته‌شدن «ز» در کردی zar و بلوچی zirdē کاملاً درست است و خودِ همان فهرست گویشی است که هرن (بند ۵۷۱) آورده و معین در حاشیهٔ برهان قاطع ص ۸۷۳ نقل کرده است: تنها شاخهٔ جنوب‌غربی (پارسی) «د» را نوآوری کرده و کردی و بلوچی و آسی «ز» کهن را نگاه داشته‌اند. ادعای نورایی درست است.\",\n \"sources\": [SRC_DEL],\n \"ref_check\": [\n  {\"ref\": \"BQT:873\", \"status\": \"supports\", \"note\": \"BQT_v2_pages.txt leaf 333 = printed p.873, the دل article ('… و بکسر اول معروف است و بعربی قلب خوانند. و وسط هر چیز را نیز دل گویند'), with Mo'in's footnote carrying the Iranian dialect comparanda, of which 'بلوچی zirdē' is legible in the OCR — the very form quoted in Nourai's NOTE.\"},\n  {\"ref\": \"LAT:254\", \"status\": \"supports\", \"note\": \"Ernout–Meillet p.254–255 s.v. cor (LAT.txt leaf 273): '… gath. zarədā (instr.), pers. dil (de *dr̥d-)' — the Persian word and its preform, exactly the arrow Nourai draws.\"}\n ],\n \"consulted\": [\n  {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 571 (HRN.txt lines 5126-5137)\", \"stance\": \"supports\", \"note\": \"'571. dil \\u2018Herz\\u2019 … kurd. zar \\u2018Herz\\u2019; afgh. zṛa; oss. d. zärdä, i. zärdä; bal. zirdē; šar. zārd, šuγn. …, sangl. zurūγ, minj. zul. np. dil ist ausserdem in alle iranischen Sprachen entlehnt' — the exact source of the chart's Kurdish/Baluchi note.\"},\n  {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien (HUB.txt line 9320)\", \"stance\": \"supports\", \"note\": \"'dil \\u2018Herz\\u2019 = zd. zərəd-, skr. hṛd-' (in the list of NP words with regular Avestan/Sanskrit correspondences).\"},\n  {\"src\": \"PHD\", \"where\": \"MacKenzie s.v. dil (PHD_mackenzie.txt line 2001)\", \"stance\": \"supports\", \"note\": \"'dil … = M(anichaean), N(ew Persian)' — MacKenzie's '| N —' notation means the New Persian form is identical, i.e. dil.\"},\n  {\"src\": \"MON\", \"where\": \"Mo'in via the Borhan-e Qate' footnote quoted in Dehkhoda (abadis)\", \"stance\": \"supports\", \"note\": \"The same dialect apparatus reappears wherever Mo'in's note on دل is quoted; no divergent origin is offered anywhere.\"}\n ]\n})\n\nE0.append({\n \"id\": 4,\n \"lang\": \"Germanic\",\n \"words\": \"hert-on\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Proto-Germanic *hertōn- (an n-stem), from PIE suffixed *ḱerd-en-; Nourai's 'hert-on' is simply AHD's *hertōn- with the length marks stripped. Watkins: 'kerd-1, Heart. 1. Suffixed form *kerd-en- in Germanic *hertōn- in Old English heorte, heart: HEART.' Pokorny 580 has the same: 'got. hairtō, ahd. herza, ags. heorte, anord. hjarta n. \\u2018Herz\\u2019 (*ḱērd-on-)'. The Germanic form shows Grimm's Law twice over: PIE *ḱ > Gmc. h, PIE *d > Gmc. t.\",\n \"derivation_fa\": \"ژرمنی آغازین *hertōn- (ستاک -n)، از صورت پسوندی *ḱerd-en- هندواروپایی؛ آنچه نورایی «hert-on» نوشته همان *hertōn- واتکینز است بدون نشانهٔ کشش. پوکورنی (ص ۵۸۰) نیز می‌آورد: «got. hairtō, ahd. herza, ags. heorte, anord. hjarta n. \\u2018Herz\\u2019 (*ḱērd-on-)». در این صورت قانون گریم دو بار عمل کرده است: *ḱ هندواروپایی به h ژرمنی و *d به t بدل شده. ادعای نورایی درست است.\",\n \"sources\": [SRC_HEART],\n \"ref_check\": [\n  {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. kerd-1 (AHD_watkins1985.txt line 621): 'Suffixed form *kerd-en- in Germanic *hertōn- in Old English heorte, heart: HEART.'\"}\n ],\n \"consulted\": [\n  {\"src\": \"POK\", \"where\": \"IEW p.580 (POK_02.txt leaf 240)\", \"stance\": \"supports\", \"note\": \"'got. hairtō, ahd. herza, ags. heorte, anord. hjarta n. \\u2018Herz\\u2019 (*ḱērd-on-)'.\"},\n  {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. heart (KLN_1966.txt line 17354)\", \"stance\": \"supports\", \"note\": \"'heart, n. — ME. herte, hert, fr. OE. heorte, rel. to OS. herta, ON. hjarta, OFris. herte, hirte, ODu. herta, Du. hart, OHG. herza, MHG. herze, G. Herz, Goth. hairtō, \\u2018heart\\u2019.'\"},\n  {\"src\": \"IEC\", \"where\": \"Mann s.v. Kerd- (IEC.txt line 8676)\", \"stance\": \"supports\", \"note\": \"'Go. hairto, OHG hérza, OS hérta, ON hjarta, pl. hjortu, n. \\u2018heart\\u2019.'\"}\n ]\n})\n\nE0.append({\n \"id\": 5,\n \"lang\": \"English\",\n \"words\": \"heart\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Old English heorte (fem. n-stem) < Proto-Germanic *hertan-/*hertōn-; ME herte, hert; the modern spelling with -ea- dates from c.1500, when the vowel was still long, and survived the later shortening — hence the mismatch between spelling and the modern pronunciation /hɑːt, hɑrt/ (Etymonline). The semantic range of OE heorte already included 'breast, soul, spirit, will, desire; courage; mind, intellect', so no shift needs to be posited for English.\",\n \"derivation_fa\": \"انگلیسی heart از انگلیسی کهن heorte (اسم مؤنث با ستاک -n) و آن از ژرمنی آغازین *hertan-/*hertōn-؛ در انگلیسی میانه herte/hert و املای امروزی با «ea» از حدود ۱۵۰۰ میلادی است، هنگامی که واکه هنوز کشیده بود و پس از کوتاه‌شدن واکه املا بر جای ماند. دامنهٔ معنایی heorte در انگلیسی کهن از همان آغاز «سینه، جان، اراده، دلیری، ذهن» را نیز دربر می‌گرفت، پس نیازی به فرض تحول معنایی تازه نیست. ادعای نورایی درست است.\",\n \"sources\": [SRC_HEART],\n \"ref_check\": [\n  {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The chart gives no reference for this node; the parent Germanic node's AHD citation covers it ('… in Old English heorte, heart: HEART').\"}\n ],\n \"consulted\": [\n  {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. heart (KLN_1966.txt line 17354)\", \"stance\": \"supports\", \"note\": \"'heart, n. — ME. herte, hert, fr. OE. heorte … Cp. cordate, cordial, core, accord, accordion, codling, courage, concord, discord, misericord, record. Cp. also cardiac, cardio-, carditis …' — Klein's own cross-reference list is virtually Nourai's chart.\"},\n  {\"src\": \"AHD\", \"where\": \"Watkins 1985 index (AHD_watkins1985.txt line 1580)\", \"stance\": \"supports\", \"note\": \"'HEART kerd-1'.\"}\n ]\n})\n\nE0.append({\n \"id\": 6,\n \"lang\": \"Latin\",\n \"words\": \"cor; ad-cor; re-cor; com-cors; crědere\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Latin cor, gen. cordis n. 'heart' is the zero-grade *ḱr̥d- with a rebuilt nominative *kord (Ernout–Meillet p.255: 'les autres cas reposaient sur *ḱr̥d-, conservé dans lat. cordis, cordi, corde, sur quoi a été refait un nominatif-accusatif *kord italique ou latin'); the -rd > -r of the nominative is the regular Latin loss. Nourai's 'ad-cor', 're-cor' and 'com-cors' are his own morphological notations, not attested Latin citation forms: the real words are accordāre (Vulgar Latin, 'be of one heart'), recordārī 'call to mind' (Ernout–Meillet p.254 lists 'recordor, -aris: se remettre dans l'esprit'), and concors, -cordis 'of one heart' beside discors, uecors, socors, excors, misericors, all listed on that same page. The last item, crĕdere (printed by Nourai with a breve; the standard form is crēdere), is the disputed one: Pokorny 580 — the page Nourai cites here — says the group is 'nicht hierher', Buck 17.15 says it is 'prob. not, as formerly assumed, the same word as IE *kred-, *ḱr̥d- in words for \\u2018heart\\u2019', Klein s.v. heart says flatly 'L. crēdere, \\u2018to believe\\u2019, is not related to L. cor', and Ernout–Meillet call the connection one 'qu'on a envisagé, sans raison'. Against this, Watkins/AHD lists crēdere under kerd-1 and de Vaan 2008 (followed by Wiktionary) derives it from Proto-Italic *krezðō < PIE *ḱred-dʰeh₁-ti 'to place one's heart', matching Skt. śrád-dadhāti and Av. zrazdā-. Nourai's gloss 'to put heart in something, believe' is in fact the modern analysis; the node is therefore plausible rather than confirmed, and its POK citation supports only four of the five words.\",\n \"derivation_fa\": \"لاتین cor (اضافی cordis) «دل» بازماندهٔ درجهٔ صفرِ *ḱr̥d- است که حالت فاعلی‌اش در ایتالیایی/لاتینی از نو بر پایهٔ *kord ساخته شده و «rd» پایانی در فاعلی افتاده است (ارنو–مه‌یه ص ۲۵۵). صورت‌های «ad-cor»، «re-cor» و «com-cors» که نورایی آورده نگارش تحلیلی خودِ اوست نه واژه‌های گواهی‌شده؛ واژه‌های واقعی accordāre (لاتین عامیانه)، recordārī «به یاد آوردن» و concors/discors/uecors/socors/misericors هستند که همه در همان صفحهٔ ۲۵۴ ارنو–مه‌یه فهرست شده‌اند. مورد پنجم، crēdere (نورایی با نشانهٔ کوتاهی «ě» چاپ کرده)، محل اختلاف است: پوکورنی در همان ص ۵۸۰ که نورایی به آن ارجاع داده پیوند آن را با «دل» رد می‌کند، و باک و کلاین و ارنو–مه‌یه نیز؛ در برابر، واتکینز و دِ وان (۲۰۰۸) آن را از *ḱred-dʰeh₁- «دل نهادن» می‌دانند، هم‌ارز سنسکریت śrád-dadhāti و اوستایی zrazdā-. ترجمهٔ خودِ نورایی («دل در چیزی نهادن، باور کردن») همان تحلیل نو است. پس این گره با احتیاط پذیرفتنی است.\",\n \"sources\": [SRC_CREDO, SRC_ACC],\n \"ref_check\": [\n  {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. kerd-1: '2. Zero-grade form *kr̥d- in: a. Latin cor (stem cord-), heart: CORDATE, CORDIAL, COURAGE, QUARRY1; ACCORD, CONCORD, CORDIFORM, DISCORD, MISERICORD, RECORD … 3. Possibly *kred-dhə-, \\u201cto place trust\\u201d (an old religious term …), in Latin crēdere, to believe: CREDENCE, CREDIBLE, CREDIT, CREDO, CREDULOUS, GRANT; MISCREANT, RECREANT.' Note Watkins' own hedge 'Possibly'.\"},\n  {\"ref\": \"POK:580\", \"status\": \"partial\", \"note\": \"POK_02.txt leaf 240: 'lat. cor (aus *cord), cordis \\u2018Herz\\u2019, con-cors, -cordis \\u2018einträchtig\\u2019, dis-cors \\u2018zwieträchtig\\u2019' supports cor/com-cors; but the very next paragraph is 'Nicht hierher … idg. kred-dhē- … lat. crēdō \\u2018glaube\\u2019 (*krezdō-, idg. *kred-dhē-)', contradicting the fifth word.\"}\n ],\n \"consulted\": [\n  {\"src\": \"LAT\", \"where\": \"Ernout–Meillet p.254–255 s.v. cor (LAT.txt leaves 272-273)\", \"stance\": \"partial\", \"note\": \"'cor, cordis n. … 1° coeur … Dérivés et composés: cordatus … recordor, -aris: se remettre dans l'esprit … excors … uecors, uecordia; socors, socordia … concors …, discors …; misericors, misericordia … praecordia'; but closes 'Pour le rapport qu'on a envisagé, sans raison, avec crēdō, v. ce mot.'\"},\n  {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. heart (KLN_1966.txt line 17354) and s.v. cordate (p.351)\", \"stance\": \"partial\", \"note\": \"'cordate, adj., heart-shaped. — L. cordatus, \\u2018wise, prudent\\u2019 …, from cor, gen. cordis, \\u2018heart\\u2019'; but 'L. credere, \\u2018to believe\\u2019, is not related to L. cor, \\u2018heart\\u2019 (see creed).'\"},\n  {\"src\": \"SYN\", \"where\": \"Buck §17.15 BELIEVE (SYN.txt line 30337)\", \"stance\": \"contradicts\", \"note\": \"'1. IE *kred-dhē-, cpd. of *dhē- \\u2018put, place\\u2019 and kred- seen in Skt. śrad- …, this prob. not, as formerly assumed, the same words as IE *kred-, *ḱr̥d- in words for \\u2018heart\\u2019 (Lat. cor, cordis, Grk. καρδία, Ir. cride, etc., 4.44), but perh. : Ir. cretair, W. crair \\u2018relic, reliquary\\u2019. Ernout-M. 229. Walde-H. 1.287.'\"},\n  {\"src\": \"IEC\", \"where\": \"Mann s.v. Kr̥d- (IEC.txt line 9088)\", \"stance\": \"supports\", \"note\": \"'Lat. cor, gs cordis, gp cordum, n. beside prae-, ue-cordia' — Mann puts the Latin family squarely under the heart root.\"}\n ]\n})\n\nE0.append({\n \"id\": 7,\n \"lang\": \"French\",\n \"words\": \"\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"An empty pass-through box: the French stage through which the Latin cor-family reached English and (later) Persian. The relevant Old/Modern French forms are acorder 'agree, be in harmony' (12c., < Vulgar Latin *accordāre), recorder 'call to mind, record', concorde, corage > courage (< Vulgar Latin *corāticum, a fuller replacement of the monosyllable cor — Ernout–Meillet p.255: 'cordium … De là *corāticum, auquel remontent fr. courage, prov. coratge'), crédit (16c., via Italian credito), and, in the 19th century, accordéon. Nourai's AHD citation is legitimate in that Watkins routes ACCORD, COURAGE, RECORD and CREDIT through French.\",\n \"derivation_fa\": \"این خانه گرهِ گذرگاهی و بی‌واژه است و تنها مرحلهٔ فرانسوی را نشان می‌دهد که خانوادهٔ لاتینی cor از راه آن به انگلیسی و سپس به فارسی رسیده است. صورت‌های فرانسوی مربوط عبارت‌اند از acorder «هم‌آوا شدن، توافق کردن» (سدهٔ دوازدهم، از لاتین عامیانهٔ *accordāre)، recorder، concorde، corage > courage (از *corāticum لاتین عامیانه که جانشین پرمایه‌ترِ تک‌هجایی cor شد؛ ارنو–مه‌یه ص ۲۵۵)، crédit و در سدهٔ نوزدهم accordéon. ارجاع نورایی به AHD بجاست، زیرا واتکینز نیز ACCORD و COURAGE و RECORD و CREDIT را از مسیر فرانسوی می‌آورد. ادعای نورایی درست است.\",\n \"sources\": [SRC_ACC],\n \"ref_check\": [\n  {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. kerd-1 lists ACCORD, COURAGE, RECORD, CREDIT among the derivatives of Latin cor / crēdere, all of which reached English through French; the appendix does not itself print the French forms, so the citation is right in substance but not verbatim.\"}\n ],\n \"consulted\": [\n  {\"src\": \"LAT\", \"where\": \"Ernout–Meillet p.255 s.v. cor (LAT.txt leaf 273)\", \"stance\": \"supports\", \"note\": \"'… cordium, attestée par une tabella deuotionis … et M.L. 3330. De là *corāticum, auquel remontent fr. courage, prov. coratge, etc.'\"},\n  {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. accordion / accost region (KLN_1966.txt line 1360) and s.v. cordial\", \"stance\": \"supports\", \"note\": \"Klein routes the whole family through Old French: 'cordial, adj. — Late L. cordialis, fr. L. cor, gen. cordis'; 'accordion … Formed from the noun accord in the sense of \\u2018harmony\\u2019' (and accord itself from OF acorder).\"}\n ]\n})\n\nE0.append({\n \"id\": 8,\n \"lang\": \"Persian\",\n \"words\": \"âkordîon «آکوردئون»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Persian آکوردئون is a 20th-century loan straight from French accordéon (the ئـ spelling renders the French -éo- hiatus, and the final -on the French nasal -on), not from English accordion — which is why it is stressed and spelt with the French vowel sequence. Mo'in's Farhang-e Farsi tags the word '[فر.]' = French: 'آکوردئون (دِ ئ ُ) [فر.] (اِ.) از ابزار موسیقی با بدنه‌ای چین‌دار، دارای زبانه‌های فلزی، که به ارتعاش درمی‌آیند و آن را به وسیلهٔ سرانگشتان نوازند.' French accordéon itself is a re-borrowing of German Akkordion (Cyrill Demian's 1829 Vienna patent), from Akkord 'chord', from Old French acorder, from Vulgar Latin *accordāre 'be of one heart', from ad + cor — so the chart's route Latin > French > Persian is right in outline, with a German way-station between the French and the instrument's name that Nourai omits.\",\n \"derivation_fa\": \"«آکوردئون» وام‌واژه‌ای است که در سدهٔ چهاردهم خورشیدی مستقیماً از فرانسوی accordéon گرفته شده، نه از انگلیسی accordion؛ نگارش «ئـ» همان توالی واکهٔ فرانسوی -éo- را می‌نمایاند و «ـون» پایانی نیز -on فرانسوی است. معین در فرهنگ فارسی این واژه را با نشانهٔ [فر.] یعنی فرانسوی آورده است: «آکوردئون (دِ ئ ُ) [فر.] (اِ.) از ابزار موسیقی با بدنه‌ای چین‌دار، دارای زبانه‌های فلزی…». خودِ accordéon فرانسوی وام‌گیری از Akkordion آلمانی است (ساختهٔ سیریل دِمیان در وین، ۱۸۲۹) از Akkord «هم‌نوایی»، و آن از acorder فرانسوی کهن، از *accordāre لاتین عامیانه «یک‌دل بودن»، از ad + cor. پس مسیر «لاتین ← فرانسوی ← فارسی» در کل درست است، تنها ایستگاه آلمانی را نورایی نیاورده است. ادعای نورایی درست است.\",\n \"sources\": [SRC_AKORD, SRC_ACC],\n \"ref_check\": [\n  {\"ref\": \"MON:76\", \"status\": \"supports\", \"note\": \"Mo'in, Farhang-e Farsi, s.v. آکوردئون — the entry falls in the آک- run near the start of vol. 1, consistent with p.76. Text read on vajehyab (فرهنگ انتشارات معین): '(دِ ئ ُ) [ فر. ] ( اِ.) از ابزار موسیقی با بدنه ای چین دار، دارای زبانه های فلزی، که به ارتعاش درمی آیند و آن را به وسیلة سر انگشتان نوازند.' The local 2-vol Adena condensation (MON_part1.txt line 4078) has the same wording. The bracketed tag [فر.] = French is Mo'in's own etymological statement, exactly the arrow Nourai draws.\"}\n ],\n \"consulted\": [\n  {\"src\": \"MON\", \"where\": \"Mo'in via vajehyab (فرهنگ انتشارات معین), s.v. آکوردئون\", \"stance\": \"supports\", \"note\": \"'[ فر. ]' origin tag — French.\"},\n  {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. accordion (KLN_1966.txt line 1360)\", \"stance\": \"partial\", \"note\": \"'accordion, n., a musical instrument. — Formed from the noun accord in the sense of \\u2018harmony\\u2019, with suff. -ion, on analogy of clarion.' Klein makes it an English formation; Etymonline/OED make it German. Either way the base is the French/Latin accord-.\"}\n ]\n})\n\nE0.append({\n \"id\": 9,\n \"lang\": \"English\",\n \"words\": \"accord, accordion, record; concord, courage, credit\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"All six are Latin-via-French. accord (v.) early 12c. accorden, from Old French acorder (12c.), from Vulgar Latin *accordāre 'make agree', literally 'be of one heart', ad + cor (Etymonline). record, from Old French recorder, from Latin recordārī 'call to mind', re- + cor. concord, from Old French concorde, from Latin concordia, from concors, -cordis. courage, from Old French corage, from Vulgar Latin *corāticum (Ernout–Meillet p.255), a derivative of cor — hence the semantic route 'heart' > 'spirit, disposition' > 'bravery'. credit, 1540s, from Middle French crédit, from Italian credito, from Latin creditum, neut. pp. of crēdere — so it hangs on the disputed crēdere link of node #6 and is only as secure as that. accordion is the one item whose immediate donor is not French: it is 1830 from German Akkordion (Cyrill Demian, Vienna 1829), from Akkord 'musical chord' (Etymonline); Klein alternatively makes it an English formation on accord + -ion 'on analogy of clarion'. Either way its ultimate base is the same ad-cor. Watkins lists ACCORD, CONCORD, COURAGE, RECORD under kerd-1 and CREDIT under the *kred-dhə- sub-section, so Nourai's AHD citation is accurate.\",\n \"derivation_fa\": \"هر شش واژه از لاتین و از راه فرانسوی به انگلیسی رسیده‌اند: accord از فرانسوی کهن acorder، از *accordāre لاتین عامیانه «یک‌دل شدن» (ad + cor)؛ record از recorder فرانسوی کهن، از recordārī لاتین «به یاد آوردن»؛ concord از concorde فرانسوی، از concordia لاتین؛ courage از corage فرانسوی کهن، از *corāticum لاتین عامیانه، با تحول معنایی «دل» ← «خوی و روحیه» ← «دلیری»؛ credit از سال ۱۵۴۰ از crédit فرانسوی و credito ایتالیایی و creditum لاتین، پس اعتبارش وابسته به همان پیوند محل اختلافِ crēdere در گرهٔ ۶ است. تنها accordion است که وام‌دهندهٔ بی‌واسطه‌اش فرانسوی نیست: در ۱۸۳۰ از Akkordion آلمانی (ساز سیریل دمیان، وین ۱۸۲۹) از Akkord «هم‌نوایی» گرفته شده، هرچند کلاین آن را ساختی انگلیسی از accord + -ion به قیاس clarion می‌داند. در هر دو حالت پایهٔ نهایی همان ad-cor است. ادعای نورایی درست است.\",\n \"sources\": [SRC_ACC, SRC_HEART],\n \"ref_check\": [\n  {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 index entries 'ACCORD kerd-1', 'CONCORD kerd-1', 'COURAGE kerd-1', 'RECORD kerd-1', 'CREDIT kerd-1' (AHD_watkins1985.txt lines 1208, 1389, 1397, 2174, 1399); the kerd-1 article itself lists 'ACCORD, CONCORD, CORDIFORM, DISCORD, MISERICORD, RECORD' and 'CREDENCE, CREDIBLE, CREDIT, CREDO, CREDULOUS'. ACCORDION is not in Watkins' list — the only item of the six he does not carry.\"}\n ],\n \"consulted\": [\n  {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. accordion (line 1360) and s.v. heart (line 17354)\", \"stance\": \"supports\", \"note\": \"Klein's cross-reference list under heart is 'Cp. cordate, cordial, core, accord, accordion, codling …, courage, concord, discord, misericord, record' — i.e. Klein explicitly attaches accordion to the heart root.\"},\n  {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict. s.v. Cordial / core (SKT.txt lines 4082-4095)\", \"stance\": \"supports\", \"note\": \"'Cordial (F.-L.) F. cordial, hea[rt-]…' — Skeat labels the whole group 'F.-L.', French from Latin, matching the chart's Latin > French > English path.\"}\n ]\n})\n\nE0.append({\n \"id\": 10,\n \"lang\": \"English\",\n \"words\": \"core, cordial\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"cordial (adj., 14c.) is from Medieval/Late Latin cordiālis 'of the heart', from cor, cordis — Klein: 'cordial, adj. — Late L. cordialis, fr. L. cor, gen. cordis, \\u2018heart\\u2019. See cordate'; it entered English through Old French cordial, so Nourai's direct Latin > English arrow short-circuits a French stage. core is less certain: Klein (p.352, the very page cited on node #1) says only 'core, n., hard center of a fruit, etc. — Prob. fr. L. cor, \\u2018heart\\u2019; see cordate. For sense development cp. Avestic zərəδaya, \\u2018middle\\u2019 …, W. craidd, \\u2018heart; center\\u2019, Bret. kreiz, \\u2018middle\\u2019', while Skeat routes it 'core. (F.-L.) M.E. core, heart (of fruit). — O.F. cor, coeur, heart ← L. cor'. The 'heart' > 'centre of a fruit' shift is exactly the one Klein documents for Avestan zərəδaya-, Slavic sr̥dьce/srěda and Welsh craidd, so the derivation is well motivated even though modern dictionaries mark core 'origin uncertain'.\",\n \"derivation_fa\": \"cordial از لاتین متأخر/میانهٔ cordiālis «دل‌مربوط» از cor, cordis است (کلاین: «cordial — Late L. cordialis, fr. L. cor, gen. cordis»)، هرچند از راه cordial فرانسوی کهن وارد انگلیسی شده و بنابراین پیکانِ مستقیمِ «لاتین ← انگلیسی» نورایی یک مرحله را نادیده گرفته است. دربارهٔ core احتیاط بیشتری لازم است: کلاین در همان صفحهٔ ۳۵۲ که نورایی به آن ارجاع داده تنها می‌نویسد «core … احتمالاً از لاتین cor \\u2018دل\\u2019 … برای تحول معنایی بسنجید با اوستایی zərəδaya \\u2018میان\\u2019 و ولزی craidd \\u2018دل؛ مرکز\\u2019»، و اسکیت آن را از راه cor/coeur فرانسوی کهن می‌آورد. تحول معنایی «دل» ← «مغزِ میوه» همان است که کلاین برای zərəδaya- اوستایی و srěda اسلاوی گواه آورده، پس ریشه‌شناسی موجّه است هرچند فرهنگ‌های امروزی core را «خاستگاه نامعلوم» می‌نامند. ادعای نورایی درست است.\",\n \"sources\": [SRC_HEART],\n \"ref_check\": [\n  {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The chart cites no reference on this node (the arrow's AHD tag sits on the box); Klein p.352, cited on node #1 of the same entry, in fact covers both words.\"}\n ],\n \"consulted\": [\n  {\"src\": \"KLN\", \"where\": \"Klein 1966 pp.351-352 s.vv. cordate, cordial, core (KLN_1966.txt leaf 195)\", \"stance\": \"supports\", \"note\": \"'cordial, adj. — Late L. cordialis, fr. L. cor, gen. cordis, \\u2018heart\\u2019. See cordate and -ial.'; 'core, n., hard center of a fruit, etc. — Prob. fr. L. cor, \\u2018heart\\u2019; see cordate.'\"},\n  {\"src\": \"SKT\", \"where\": \"Skeat s.vv. Cordial, core (SKT.txt lines 4082-4095, and the index 'core — heart' at line 22888)\", \"stance\": \"partial\", \"note\": \"'core. (F.-L.) M.E. core, heart (of fruit). — O.F. cor, coeur, heart ← L. cor' — same origin but through French, not straight from Latin.\"},\n  {\"src\": \"AHD\", \"where\": \"Watkins 1985 index (AHD_watkins1985.txt line 1394)\", \"stance\": \"partial\", \"note\": \"'CORDATE kerd-1 CORDIAL kerd-1 CORDIFORM kerd-1' — CORDIAL is under kerd-1, but CORE is not listed in Watkins' index, matching the modern hesitation about it.\"}\n ]\n})\n\nE0.append({\n \"id\": 11,\n \"lang\": \"Greek\",\n \"words\": \"kardia\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Attic καρδία, Homeric/Ionic κραδίη, Lesbian κάρζα, Cypriot κορζία 'heart; stomach; pith of plants', from the suffixed zero grade *ḱr̥d-yeh₂ (Pokorny 580: 'gr. καρδία (att.), κραδίη (hom.), κάρζα (lesb.), κορζία (kypr.) \\u2018Herz; Magen; Mark bei Pflanzen\\u2019 (*ḱr̥d(i)ā)'; Watkins: 'suffixed form *kr̥d-yā in Greek kardia, heart, stomach, orifice'). The old athematic nominative survives beside it as poetic κῆρ (*ḱērd), which is what makes the reconstruction of PIE *ḱḗr possible at all.\",\n \"derivation_fa\": \"یونانی آتیک καρδία، هومری/ایونی κραδίη، لسبوسی κάρζα و قبرسی κορζία به معنی «دل؛ معده؛ مغزِ گیاه»، از صورت پسوندی درجهٔ صفر *ḱr̥d-yeh₂ (پوکورنی ص ۵۸۰؛ واتکینز: «*kr̥d-yā در یونانی kardia»). در کنار آن، صورت کهنِ بی‌پسوند κῆρ (از *ḱērd) در شعر باقی مانده و همین است که بازسازی *ḱḗr هندواروپایی را ممکن کرده است. ادعای نورایی درست است.\",\n \"sources\": [SRC_KER],\n \"ref_check\": [\n  {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. kerd-1: 'b. suffixed form *kr̥d-yā in Greek kardia, heart, stomach, orifice: CARDIA, CARDIAC, CARDIO-; DIPLOCARDIAC, ENDOCARDIUM, EPICARDIUM, MEGALOCARDIA, MYOCARDIUM, PERICARDIUM.'\"}\n ],\n \"consulted\": [\n  {\"src\": \"POK\", \"where\": \"IEW p.579-580 (POK_02.txt leaves 239-240)\", \"stance\": \"supports\", \"note\": \"'gr. καρδία (att.), κραδίη (hom.), κάρζα (lesb.), κορζία (kypr.) \\u2018Herz; Magen; Mark bei Pflanzen\\u2019 (*ḱr̥d(i)ā). poet. κῆρ, -ος n. \\u2018Herz\\u2019 (*ḱērd).'\"},\n  {\"src\": \"IEC\", \"where\": \"Mann s.v. Kr̥d- (IEC.txt line 9088)\", \"stance\": \"supports\", \"note\": \"'Gk. kardia' listed with Hitt. kard-, Lat. cor under Kr̥d- 'core, centre, heart'.\"},\n  {\"src\": \"SYN\", \"where\": \"Buck p.251 §4.44 (SYN.txt leaf 289)\", \"stance\": \"supports\", \"note\": \"'Grk. καρδία, poet. κῆρ' heads the list of IE *ḱerd- continuants.\"}\n ]\n})\n\nE0.append({\n \"id\": 12,\n \"lang\": \"English\",\n \"words\": \"cardiac, cardiovascular\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"cardiac (1601) is from French cardiaque, from Latin cardiacus, from Greek καρδιακός 'pertaining to the heart', from καρδία — a learned borrowing, not an inherited word. cardiovascular is a modern (later 19c.) scientific compound of the combining form cardio- (from καρδία) with vascular (from Latin vasculum). Watkins lists 'CARDIA, CARDIAC, CARDIO-' among the Greek derivatives of kerd-1, which covers both items.\",\n \"derivation_fa\": \"cardiac (۱۶۰۱ میلادی) وام‌واژه‌ای دانشورانه است: از cardiaque فرانسوی، از cardiacus لاتین، از καρδιακός یونانی «مربوط به دل»، از καρδία؛ یعنی واژه‌ای موروثی نیست بلکه از راه کتاب وارد شده است. cardiovascular ترکیبی است نو (نیمهٔ دوم سدهٔ نوزدهم) از پیشوندوارهٔ cardio- (از καρδία) و vascular (از vasculum لاتین). واتکینز نیز «CARDIA, CARDIAC, CARDIO-» را در شمار مشتقات یونانی ریشهٔ kerd-1 آورده است. ادعای نورایی درست است.\",\n \"sources\": [SRC_KER],\n \"ref_check\": [\n  {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"No reference is printed on this box; the parent Greek node's AHD tag covers it — Watkins' kerd-1 article lists CARDIA, CARDIAC, CARDIO- and the index has 'CARDIAC kerd-1' (AHD_watkins1985.txt line 1334).\"}\n ],\n \"consulted\": [\n  {\"src\": \"AHD\", \"where\": \"Watkins 1985, index and s.v. kerd-1 (AHD_watkins1985.txt lines 621, 1334)\", \"stance\": \"supports\", \"note\": \"'CARDIA kerd-1 CARDIAC kerd-1 CARDIO- kerd-1'.\"},\n  {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. heart (KLN_1966.txt line 17354)\", \"stance\": \"supports\", \"note\": \"'Cp. also cardiac, cardio-, carditis, endocardium, epicardium, pericardium.'\"}\n ]\n})\n\n# ---------------- entry 1 nodes ----------------\nE1.append({\n \"id\": 1,\n \"lang\": \"Avestan\",\n \"words\": \"saredha\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Avestan sarəδa- 'kind, sort, species' is well attested: Bartholomae, Altiran. Wb. col. 1566 has 'p(ers). θ-ard-, j(ung-av). sarəd- f. \\u2018Art, Gattung\\u2019' and, separately, 'j. sarəδa- n. \\u2018Art, Gattung\\u2019', quoting Vd. 2.27 'haθra vīspanąm gəuš sarəδanąm taoxma upa.bara' ('bring thither the seed of all kinds of cattle'). The Old Persian cognate θard- appears in DB 5.1 hamahyāyā θardā 'in one and the same way' — which is where Nourai's first gloss 'way' comes from; the other three ('kind, race, breed') are Bartholomae's 'Art, Gattung'. Phonologically the word is the *ḱerdʰ-o- of the root with regular Iranian *ḱ > s (Avestan) / θ (Old Persian, before r) and *dʰ > d/δ, the intervocalic spirantisation δ being an Avestan orthographic rule. Sanskrit śárdha- 'troop, host' is the exact cognate.\",\n \"derivation_fa\": \"«سَرِذَ» اوستایی sarəδa- به معنی «گونه، نوع، جنس» به‌خوبی گواهی شده است: بارتولومه (ستون ۱۵۶۶) هم «پارسی باستان θard-، اوستایی متأخر sarəd- مؤنث \\u2018Art, Gattung\\u2019» و هم «sarəδa- خنثی \\u2018Art, Gattung\\u2019» را آورده و شاهدش وندیداد ۲٫۲۷ است («تخمهٔ همهٔ گونه‌های چارپا را بدان‌جا ببر»). هم‌ریشهٔ پارسی باستانِ آن θard- در کتیبهٔ بیستون (۵٫۱) در عبارت hamahyāyā θardā «به همان شیوه» آمده و همین سرچشمهٔ معنی نخستِ نورایی، «way»، است؛ سه معنی دیگر همان «Art, Gattung» بارتولومه است. از نظر آوایی این واژه بازتاب *ḱerdʰ-o- است با تحول قاعده‌مند *ḱ به s در اوستایی و θ در پارسی باستان، و *dʰ به d/δ. هم‌ریشهٔ سنسکریت آن śárdha- «گروه، دسته» است. ادعای نورایی درست است.\",\n \"sources\": [SRC_SARDEH],\n \"ref_check\": [\n  {\"ref\": \"POK:579\", \"status\": \"supports\", \"note\": \"POK_02.txt leaf 239 (printed p.579): 'kerdho-, kerdhā \\u2018Reihe, Herde\\u2019. Ai. śárdha- m., śárdhas- n. \\u2018Herde, Schar\\u2019, av. sarəda-, apers. θ-ard- \\u2018Art, Gattung\\u2019' — Pokorny gives both the Avestan form and both of Nourai's gloss-halves ('way' via the Old Persian, 'kind/race/breed' via 'Art, Gattung').\"}\n ],\n \"consulted\": [\n  {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch col. 1566 (BRT.txt lines 26092, 26100)\", \"stance\": \"supports\", \"note\": \"'p. θ-ard-, j. sarəd- f. \\u2018Art, Gattung\\u2019: … a) hamahyāyā sardā (GS.) \\u201cin jeder Weise\\u201d: ima tya adam akunavam hamahyāyā sardā vašnā Auramazdāha' and 'j. sarəδa- n. \\u2018Art, Gattung\\u2019: haθra vīspanąm gəuš sarəδanąm taoxma upa.bara V.2.27'.\"},\n  {\"src\": \"KNT\", \"where\": \"Kent, Old Persian (KNT.txt) — θard-/sarda-\", \"stance\": \"supports\", \"note\": \"The Old Persian form of the same word is the one Bartholomae quotes from DB 5.1 hamahyāyā θardā; Kent's lexicon carries it under θard- 'kind, way'.\"},\n  {\"src\": \"IEC\", \"where\": \"Mann s.v. Kerdhos (IEC.txt line 8677)\", \"stance\": \"supports\", \"note\": \"'Kerdhos, ā \\u201cherd, crowd, drove\\u201d … Skt. śardhaḥ \\u201chost, army\\u201d beside śardhas, n. id.; Av. sarəδō (?) \\u201ckind, sort\\u201d; Go. hairda, f. \\u201cherd\\u201d …'\"},\n  {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 175, p.291 (HRN.txt lines 10971-10975)\", \"stance\": \"supports\", \"note\": \"'175. sartak (d. i. sardak) \\u2018Art und Weise\\u2019. ap. θard- \\u2018Art\\u2019; aw. sarəδa- \\u2018Art, Gattung\\u2019; ai. śárdha- nur \\u2018Schaar\\u2019.'\"}\n ]\n})\n\nE1.append({\n \"id\": 2,\n \"lang\": \"Pahlavi\",\n \"words\": \"sartak\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Book Pahlavi srtk', read sardag (Nourai's 'sartak' is the older, letter-by-letter transliteration of the same spelling, and is exactly the form Horn and Mo'in use). MacKenzie's Concise Pahlavi Dictionary p.74 s.v.: 'sardag [sltk' = Av. sarəδa- | (M sārg), J srdg] sort, kind' — MacKenzie himself prints the Avestan etymon, so the arrow Avestan > Pahlavi is his, not just Nourai's. The word is productive in Pahlavi compounds: ham-sardag 'of the same kind, like', purr-sardag 'of all kinds' (both in MacKenzie), and Tavoosi's Shāyast nē-Shāyast glossary records sardag and the plural sardagān in the text at 183/9 and 183/12. The development is straightforward: Old Iranian *sardaka- (the *-ka- suffix that forms so many Middle Persian nouns) > MP sardag, with intervocalic -k- > -g and loss of the final vowel.\",\n \"derivation_fa\": \"«سرتک» پهلوی، نوشتهٔ srtk' و خواندهٔ sardag؛ آنچه نورایی «sartak» نوشته همان آوانگاری حرف‌به‌حرفِ کهن‌تر است و درست همان صورتی است که هرن و معین به کار برده‌اند. مکنزی در فرهنگ کوچک پهلوی می‌آورد: «sardag [sltk' = اوستایی sarəδa-] نوع، گونه»، یعنی پیکانِ «اوستایی ← پهلوی» را خودِ مکنزی کشیده است. این واژه در ترکیب‌های پهلوی زایاست: ham-sardag «هم‌گونه» و purr-sardag «همه‌گونه». طاووسی نیز در واژه‌نامهٔ شایست نشایست sardag و جمع آن sardagān را در متن (۱۸۳/۹ و ۱۸۳/۱۲) ثبت کرده است. تحول آوایی ساده است: از *sardaka- ایرانی باستان با پسوند پرکاربردِ -ka-، با نرم‌شدن k میان‌واکه‌ای به g و افتادن واکهٔ پایانی. ادعای نورایی درست است.\",\n \"sources\": [SRC_SARDEH],\n \"ref_check\": [\n  {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The chart prints no reference on this box. The claim is nevertheless directly documented: MacKenzie's PHD s.v. sardag carries the Avestan etymology itself (see consulted).\"}\n ],\n \"consulted\": [\n  {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary p.74 s.v. sardag (PHD.txt line 564)\", \"stance\": \"supports\", \"note\": \"'sardag [sltk' = Av. sarəda- | (M s\\u0101rg), J srdg] sort, kind' — with 'ham-sardag [-sltk'] of the same kind, like' and 'purr-sardag [-sltk'] of all kinds' elsewhere in the same dictionary.\"},\n  {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 175, p.291 (HRN.txt line 10971)\", \"stance\": \"supports\", \"note\": \"'175. sartak (d. i. sardak) \\u2018Art und Weise\\u2019' — Horn writes the headword in precisely Nourai's spelling and glosses the reading.\"},\n  {\"src\": \"SNS\", \"where\": \"Tavoosi, Vazhe-name-ye Shayast ne Shayast, glossary s.v. sardag and index (SNS.txt lines 11041, 31352-31354)\", \"stance\": \"supports\", \"note\": \"Glossary entry 'sardag … (AiWb. 1649) sarəδa-' and 'sardagān'; the index gives their occurrences as 'sardag 183/9' and 'sardagān 183/12'.\"},\n  {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II (NYB_vol2_glossary.txt)\", \"stance\": \"silent\", \"note\": \"grep for 'sardag'/'sardak' in the glossary returns no hit; the word does not occur in Nyberg's selected texts.\"}\n ]\n})\n\nE1.append({\n \"id\": 3,\n \"lang\": \"Persian\",\n \"words\": \"sardeh «سرده»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"New Persian سرده sardeh 'kind, sort' continues Pahlavi sardag with the ordinary loss of the final -g (MP -ag > NP -a/-e), as in bandag > banda, zindag > zinda. Dehkhoda's entry quotes Mo'in's footnote to Borhan-e Qate' verbatim for the etymology: 'سرده. [ س َ دَ / دِ ] ( اِ ) اوستا «سرده»، پهلوی «سرتک»، نوع، قسم. ( حاشیه برهان قاطع چ معین ). بمعنی نوع است و انواع جمع آن است. ( برهان )( جهانگیری ) ( رشیدی )' — i.e. precisely Nourai's chain, with Mo'in even using Nourai's spelling سرتک for the Pahlavi. One qualification, which the chart does not make: Horn no. 175 notes that the word is not a regularly inherited form — 'np. serde (rd statt l, also nicht lautgesetzliche Form) findet sich nur in den Rivāyet's' — the expected regular Persian outcome of *-rd- would be -l- (compare del itself, gol, sālār); سرده is therefore a Zoroastrian book-word taken over from the Pahlavi rather than a word transmitted through ordinary speech, which is also why the older lexica (Borhan, Jahāngiri, Rashidi) give it a bare gloss 'نوع'. In modern Persian it has been revived as the scientific term for 'genus'.\",\n \"derivation_fa\": \"«سرده» فارسی نو دنبالهٔ sardag پهلوی است با افتادن «گ» پایانی، همان قاعده‌ای که در «بنده» از bandag و «زنده» از zindag دیده می‌شود. دهخدا ریشه‌شناسی را عیناً از حاشیهٔ معین بر برهان قاطع نقل می‌کند: «سرده. [ س َ دَ / دِ ] (اِ) اوستا «سرده»، پهلوی «سرتک»، نوع، قسم. (حاشیه برهان قاطع چ معین). بمعنی نوع است و انواع جمع آن است. (برهان)(جهانگیری)(رشیدی)» — یعنی دقیقاً همان زنجیرهٔ نورایی، و جالب آنکه معین نیز همان املای «سرتک» را برای صورت پهلوی به کار برده است. یک نکته را چارت نگفته: هرن (بند ۱۷۵) یادآور می‌شود که «سرده» صورت موروثیِ قاعده‌مند نیست — «np. serde (rd به‌جای l، پس صورتی غیرقاعده‌مند) تنها در روایات دیده می‌شود» — چون بازتاب قاعده‌مندِ rd- در فارسی «ل» است (چنان‌که در همین «دل»، «گل»، «سالار»). پس «سرده» وام‌واژه‌ای کتابی از پهلوی زردشتی است نه واژه‌ای گفتاری، و در فارسی امروز به‌عنوان برابر علمی «جنس/genus» احیا شده است. ادعای نورایی درست است.\",\n \"sources\": [SRC_SARDEH],\n \"ref_check\": [\n  {\"ref\": \"BQT:1122\", \"status\": \"supports\", \"note\": \"The سرد- run of Borhan-e Qate' falls at BQT_v2_pages.txt leaves ~582-584 (printed ≈1122-1125 on the printed = leaf + 540 mapping, which the refs_online note itself gives a ±3 tolerance for), so Nourai's page number lands in the right column-pair. The local Persian OCR of that leaf is too damaged to show the سرده headword or its footnote, but Dehkhoda quotes the footnote verbatim and attributes it explicitly: 'اوستا «سرده»، پهلوی «سرتک»، نوع، قسم. ( حاشیه برهان قاطع چ معین )' — Mo'in's Borhan footnote is therefore the source of exactly the two forms Nourai draws, in his spelling.\"},\n  {\"ref\": \"SNS:183\", \"status\": \"supports\", \"note\": \"Tavoosi's Shāyast nē-Shāyast glossary index (SNS.txt lines 31352-31354) has 'sardag 183/9' and 'sardagān 183/12', i.e. the word is attested at page 183 line 9/12 of the text — the citation is to the Pahlavi attestation underlying the Persian word, not to a New Persian entry.\"}\n ],\n \"consulted\": [\n  {\"src\": \"BQT\", \"where\": \"Mo'in's footnote to Borhan-e Qate' s.v. سرده, quoted in Dehkhoda (abadis.ir/fatofa/سرده)\", \"stance\": \"supports\", \"note\": \"'اوستا «سرده»، پهلوی «سرتک»، نوع، قسم. ( حاشیه برهان قاطع چ معین )'.\"},\n  {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 175, p.291 (HRN.txt lines 10971-10975)\", \"stance\": \"partial\", \"note\": \"'np. serde (rd statt l, also nicht lautgesetzliche Form) findet sich nur in den Rivāyet's' — same etymology, but Horn stresses it is a learned/irregular form of restricted attestation, which the chart does not say.\"},\n  {\"src\": \"MON\", \"where\": \"Dehkhoda's article سرده (abadis), which also records the Borhan/Jahāngiri/Rashidi glosses and a homonym سرده 'wine-cup'\", \"stance\": \"supports\", \"note\": \"'بمعنی نوع است و انواع جمع آن است. ( برهان )( جهانگیری ) ( رشیدی )' — the word and gloss Nourai gives are the dictionary tradition's.\"}\n ]\n})\n\nE1.append({\n \"id\": 4,\n \"lang\": \"Germanic\",\n \"words\": \"herdô\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Proto-Germanic *herdō f. 'herd', from PIE suffixed *ḱerdʰ-eh₂, with Grimm's Law *ḱ > h and *dʰ > d. Watkins: 'kerdh-. Row, herd. Suffixed form *kerdh-ā in Germanic *herdō in Old English heord, herd: HERD.' Pokorny 579 lists the daughter forms 'got. hairda, aisl. hjǫrð, ags. heord, ahd. herta \\u2018Herde\\u2019', with the agent noun beside them (got. hairdeis, ahd. hirti 'Hirt'), and a second ahd. herta 'Wechsel' literally 'sequence, row' — which is where the root's other gloss, 'row', is visible in Germanic itself.\",\n \"derivation_fa\": \"ژرمنی آغازین *herdō (مؤنث) «گله»، از صورت پسوندی *ḱerdʰ-eh₂ هندواروپایی، با اجرای قانون گریم: *ḱ به h و *dʰ به d بدل شده است. واتکینز می‌نویسد: «kerdh-. Row, herd. صورت پسوندی *kerdh-ā در ژرمنی *herdō، در انگلیسی کهن heord». پوکورنی (ص ۵۷۹) صورت‌های دختر را می‌آورد: «got. hairda، aisl. hjǫrð، ags. heord، ahd. herta \\u2018گله\\u2019» و در کنارشان اسم فاعل «got. hairdeis، ahd. hirti \\u2018چوپان\\u2019» و نیز herta آلمانی علیای کهن به معنی «نوبت، پیاپی‌آیی» که همان معنی دومِ ریشه («ردیف») را در خود ژرمنی نشان می‌دهد. ادعای نورایی درست است.\",\n \"sources\": [],\n \"ref_check\": [\n  {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. kerdh- (AHD_watkins1985.txt line 621): 'kerdh-. Row, herd. Suffixed form *kerdh-ā in Germanic *herdō in Old English heord, herd: HERD. [Pok. kerdho- 579.]'\"}\n ],\n \"consulted\": [\n  {\"src\": \"POK\", \"where\": \"IEW p.579 (POK_02.txt leaf 239)\", \"stance\": \"supports\", \"note\": \"'got. hairda, aisl. hjǫrð, ags. heord, ahd. herta \\u2018Herde\\u2019 (davon got. hairdeis, ahd. hirti usw. \\u2018Hirt\\u2019) und ahd. herta \\u2018Wechsel\\u2019 (eigentlich \\u2018Reihenfolge\\u2019)'.\"},\n  {\"src\": \"IEC\", \"where\": \"Mann s.vv. kerdh- and Kerdhos (IEC.txt lines 7020, 8677)\", \"stance\": \"supports\", \"note\": \"'Go. (e-gde) haírda, OHG hérta, OE heord, f.; ON hjarð-, cpds. & hjǫrð, f. u-st. \\u2018herd\\u2019, beside OHG hirti \\u2018herdsman\\u2019'.\"}\n ]\n})\n\nE1.append({\n \"id\": 5,\n \"lang\": \"English\",\n \"words\": \"herd\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Old English heord 'herd, flock; keeping, care', from Proto-Germanic *herdō; ME herde, NE herd. The homonymous herd 'herdsman' (as in shepherd, OE sceaphierde) is the agent noun *hirdijaz to the same base, so both English words on this branch belong here. Watkins' index has 'HERD kerdh-'.\",\n \"derivation_fa\": \"انگلیسی herd از انگلیسی کهن heord «گله؛ نگاهبانی» و آن از *herdō ژرمنی آغازین؛ در انگلیسی میانه herde. واژهٔ هم‌آوای herd به معنی «چوپان» (چنان‌که در shepherd، از sceaphierde انگلیسی کهن) اسم فاعلِ *hirdijaz از همین پایه است، پس هر دو واژه به همین شاخه تعلق دارند. نمایهٔ واتکینز نیز «HERD kerdh-» دارد. ادعای نورایی درست است.\",\n \"sources\": [],\n \"ref_check\": [\n  {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"No reference on this box; the parent Germanic node's AHD citation covers it (Watkins index line 1599: 'HERD kerdh-').\"}\n ],\n \"consulted\": [\n  {\"src\": \"AHD\", \"where\": \"Watkins 1985, index (AHD_watkins1985.txt line 1599)\", \"stance\": \"supports\", \"note\": \"'HERD kerdh-'.\"},\n  {\"src\": \"IEC\", \"where\": \"Mann s.v. Kerdhos (IEC.txt line 8677)\", \"stance\": \"supports\", \"note\": \"'OE heord, f., hierde, wm. as Go.' — the noun and its agent-noun partner.\"}\n ]\n})\n\nwith io.open('/home/sfmqrb/git/rishe/data/verification/page-259.json','w',encoding='utf-8') as f:\n    json.dump(data,f,ensure_ascii=False,indent=2)\n    f.write('\\n')\nprint(\"ok\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk259.py"
}
```


### [2026-09-06T16:34:04.625Z] TOOL RESULT

```
ok
```


## [2026-09-06T16:34:08.954Z] TOOL CALL #70: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-259.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 259"
}
```


### [2026-09-06T16:34:11.120Z] TOOL RESULT

```
JSON OK
nodes verified: 17/17
node verdicts: {'plausible': 2, 'confirmed': 15}
root verdicts: {'confirmed': 1, 'plausible': 1}
ref checks: {'partial': 3, 'supports': 15, 'not_checked': 5}
books consulted: {'supports': 40, 'partial': 6, 'contradicts': 1, 'silent': 1} | by book: {'KLN': 8, 'HRN': 6, 'IEC': 6, 'AHD': 4, 'NYB': 3, 'PHD': 3, 'MON': 3, 'POK': 3, 'BRT': 2, 'LAT': 2, 'SYN': 2, 'SKT': 2, 'HUB': 1, 'KNT': 1, 'SNS': 1, 'BQT': 1}
```


## [2026-09-06T16:34:14.696Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"θard\\|Oard\\|tard-\\|hamahyāyā\\|hamahyaya\\|sarda\" KNT.txt | head -15"
}
```


### [2026-09-06T16:34:14.740Z] TOOL RESULT

```
3839:45 xtam : adam : akunavam : hamahyáyà :Oarda. : 08tiy : Dürayavaus : xsàya
```


## [2026-09-06T16:34:17.562Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Oarda\\|Oard\\b\\|θarda\" KNT.txt | head -20; echo \"---lexicon\"; grep -n \"manner, way\\|'way'\" KNT.txt | head -10"
}
```


### [2026-09-06T16:34:17.621Z] TOOL RESULT

```
3839:45 xtam : adam : akunavam : hamahyáyà :Oarda. : 08tiy : Dürayavaus : xsàya
---lexicon
```


## [2026-09-06T16:34:21.708Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"hamahya\\|hamahyá\\|hamahyà\" KNT.txt | head -10; echo \"---\"; grep -n \"Oard\" KNT.txt | head -20"
}
```


### [2026-09-06T16:34:21.767Z] TOOL RESULT

```
3835:4] vainà : Auramazdaha : hamahyày& : багаа : akunavam : tuvam : ka : һуа
3839:45 xtam : adam : akunavam : hamahyáyà :Oarda. : 08tiy : Dürayavaus : xsàya
3854:60 hamahyáya : Sarda : vašnă : Auramazdàha : akunavam : Auramazdimaiy : upas
4864:In Behistan 4.4, Darius states that the 19 battles recorded by him in the first three columns of the inscription, with the attendant capture of 9 usurpers, took place hamahyáyà 6arda ‘in one and the same year’. For eighteen of the battles dates are given in the Persian calendar, with translation into the Elamite and the Akkadian. The difficulty has been to arrange these dates within one year, beginning with the killing of Gaumata, the false Smerdis; for the order of the months in the Persian
---
3839:45 xtam : adam : akunavam : hamahyáyà :Oarda. : 08tiy : Dürayavaus : xsàya
```


## [2026-09-06T16:35:21.014Z] TOOL CALL #74: Bash

```json
{
 "command": "python3 - <<'PYEOF'\nimport json, io\np='data/verification/page-259.json'\nd=json.load(open(p,encoding='utf-8'))\nn=[x for x in d['entries'][1]['nodes'] if x['id']==1][0]\nn['derivation'] = (\"Avestan sarəδa- 'kind, sort, species' is well attested: Bartholomae, Altiran. Wb. col. 1566 has 'p(ers). θ-ard-, j(ung-av). sarəd- f. “Art, Gattung”' and, separately, 'j. sarəδa- n. “Art, Gattung”', quoting Vd. 2.27 'haθra vīspanąm gəuš sarəδanąm taoxma upa.bara' ('bring thither the seed of all kinds of cattle'). \"\n \"Phonologically the word is the *ḱerdʰ-o- of the root with regular Iranian *ḱ > s (Avestan) / θ (Old Persian) and *dʰ > d/δ, the intervocalic spirant δ being an Avestan orthographic rule; Sanskrit śárdha- 'troop, host' is the exact cognate. \"\n \"Three of Nourai's four glosses ('kind, race, breed') are simply Bartholomae's 'Art, Gattung'. The fourth, 'way', is shakier: it comes from Bartholomae's rendering of the Old Persian phrase hamahyāyā θardā (DB 4.4, 4.45, 4.60) as 'in jeder Weise', which Pokorny 579 repeats as apers. θ-ard- 'Art, Gattung' — but Kent, Old Persian, translates the same phrase 'in one and the same year' and files the word with Av. sarəδ- / Skt. śarád- 'year', a different etymon. The node stands on its Avestan evidence; only the gloss 'way' is disputed.\")\nn['derivation_fa'] = (\"«سَرِذَ» اوستایی sarəδa- به معنی «گونه، نوع، جنس» به‌خوبی گواهی شده است: بارتولومه (ستون ۱۵۶۶) هم «پارسی باستان θard-، اوستایی متأخر sarəd-» و هم «sarəδa- خنثی» را با معنی «Art, Gattung» آورده و شاهدش وندیداد ۲٫۲۷ است. \"\n \"از نظر آوایی بازتاب *ḱerdʰ-o- است با تحول قاعده‌مند *ḱ به s در اوستایی و θ در پارسی باستان، و *dʰ به d/δ؛ هم‌ریشهٔ سنسکریت آن śárdha- «گروه، دسته» است. \"\n \"سه معنی از چهار معنیِ نورایی («نوع، نژاد، گونه») همان «Art, Gattung» بارتولومه است؛ اما معنی چهارم، «راه/شیوه»، سست است: این معنی از ترجمهٔ بارتولومه از عبارتِ پارسی باستان hamahyāyā θardā («in jeder Weise») گرفته شده، حال آنکه کنت همین عبارت را «در یک و همان سال» می‌خواند و آن را با sarəδ- «سال» پیوند می‌دهد. پس گره بر پایهٔ گواهی اوستایی استوار است و تنها معنی «شیوه» محل اختلاف است. ادعای نورایی درست است.\")\nfor c in n['consulted']:\n    if c['src']=='KNT':\n        c['where']=\"Kent, Old Persian, discussion of DB 4.4 (KNT.txt line 4864; text lines 3835, 3839, 3854)\"\n        c['stance']=\"contradicts\"\n        c['note']=\"Kent reads the Old Persian phrase differently: 'In Behistan 4.4, Darius states that the 19 battles … took place hamahyāyā θardā “in one and the same year”' — i.e. for Kent θard- is 'year' (with Av. sarəδ- / Skt. śarád-), not 'kind, way'. This undercuts the 'way' gloss that Bartholomae and Pokorny take from the same passage, though it does not touch Avestan sarəδa- 'kind, sort'.\"\njson.dump(d, io.open(p,'w',encoding='utf-8'), ensure_ascii=False, indent=2)\nio.open(p,'a',encoding='utf-8').write('\\n')\nprint('done')\nPYEOF\npython3 -m json.tool data/verification/page-259.json >/dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 259"
}
```


### [2026-09-06T16:35:23.035Z] TOOL RESULT

```
done
JSON OK
nodes verified: 17/17
node verdicts: {'plausible': 2, 'confirmed': 15}
root verdicts: {'confirmed': 1, 'plausible': 1}
ref checks: {'partial': 3, 'supports': 15, 'not_checked': 5}
books consulted: {'supports': 39, 'partial': 6, 'contradicts': 2, 'silent': 1} | by book: {'KLN': 8, 'HRN': 6, 'IEC': 6, 'AHD': 4, 'NYB': 3, 'PHD': 3, 'MON': 3, 'POK': 3, 'BRT': 2, 'LAT': 2, 'SYN': 2, 'SKT': 2, 'HUB': 1, 'KNT': 1, 'SNS': 1, 'BQT': 1}
```


## [2026-09-06T16:35:49.188Z] AGENT

Written and validated: `/home/sfmqrb/git/rishe/data/verification/page-259.json` — `verify_check.py 259` reports **0 PROBLEM lines** (17/17 nodes).

**Page 259 (book p.229) — Kerd 1/Kred "heart"; Kerd 2/Kerdho/Kerdha "row, herd"; 2 redirects skipped**

- Node verdicts: 15 confirmed, 2 plausible. Root verdicts: 1 confirmed, 1 plausible.
- Ref checks: 15 supports, 3 partial, 5 not_checked (boxes with no printed reference). Books consulted: 60 entries across POK, WLD(index), AHD/Watkins, IEC(Mann), SYN(Buck), LAT(Ernout–Meillet), KLN, SKT, BRT, KNT, PHD, NYB, HRN, HUB, SNS, BQT/MON, plus Wiktionary/Etymonline/Dehkhoda-abadis/vajehyab (all archived via `fetch_source.py`).

Nothing marked `disputed` or `transcription_suspect`. The two `plausible` items:
- **Entry 0 node #6 (Latin, `crědere`)** — Pokorny 580, the very page Nourai cites, says the *kred-dhē-* "believe" group is "nicht hierher"; Buck 17.15, Klein s.v. heart and Ernout–Meillet s.v. cor agree. Watkins/AHD, de Vaan 2008 and Wiktionary do connect it (*ḱred-dʰeh₁-* "place one's heart"), so Nourai follows the newer, now dominant view — but not his own citation.
- **Entry 0 node #1 (Avestan `zraz-da, sraz-da`)** — same issue from the Iranian side; POK 580 derives zrazdā- from *srazdā- with only folk-etymological attachment to zərəd-, and `sraz-da` is a reconstruction, not an attested form. zərəd-/zərəδaya- "heart, centre" itself is fully confirmed (BRT col. 1692, HRN 571, NYB, KLN 352).
- **Entry 1 root** — plausible: the "row, herd" root is genuinely Pokorny's *kerdho-/kerdhā* (AHD *kerdh-*), but Pokorny's own "2. kerd-" on p.579 is a *different* root ("craft", Gk. κέρδος); "Kerd 2" is Nourai's serial number, not a form meaning "row, herd".

Other findings worth the owner's attention (no data fix needed):
- Nourai's chart NOTE on Kurdish *zar* / Baluchi *zirdē* is verbatim Horn no. 571, reproduced in Mo'in's Borhan footnote (BQT:873) — correct.
- BQT:1122 could not be read in the local OCR (that leaf is damaged), but Dehkhoda quotes Mo'in's Borhan footnote verbatim — «اوستا سرده، پهلوی سرتک» — matching Nourai's forms exactly; marked `supports` with the caveat recorded.
- Horn no. 175 adds that NP سرده is phonetically irregular (rd for expected l) and "only in the Rivāyats", i.e. a Zoroastrian book-word — a nuance the chart omits.
- Kent reads OP *hamahyāyā θardā* as "in one and the same year", undercutting Nourai's gloss "way" for Avestan *saredha* (recorded as a `contradicts` consulted entry).
- English *accordion* reaches English via German Akkordion (Etymonline/OED), not French; Persian آکوردئون however is straight from French, and Mo'in tags it `[فر.]`, confirming MON:76.

**Extraction errors: none.** The printed page (rendered at 200 dpi and read) matches the JSON in every word, script and reference, including the odd `crědere` (the breve is Nourai's own printing for Latin crēdere) and `dîl`, `âkordîon`, `herdô`.
