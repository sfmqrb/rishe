# Verification process log — verify-page-102


## [2026-09-05T14:40:32.795Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 102 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-102.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-102.json. Write /home/sfmqrb/git/rishe/data/verification/page-102.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 102` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T14:40:34.383Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T14:40:35.086Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T14:40:35.104Z] TOOL RESULT

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


## [2026-09-05T14:40:35.343Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-102.txt"
}
```


### [2026-09-05T14:40:35.370Z] TOOL RESULT

```
1	=== PDF page 102 (book page 72) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Bu : lip, kiss  (refs POK:103; SYN:1113)
4	#1 (parent #0) [Persian] refs=POK:103 | bŭs «بوس» : kiss | extra: بوسیدن
5	#2 (parent #0) [Germanic] refs=AHD | kusjan : to kiss
6	  #3 (parent #2) [English] refs=AHD | buss : to kiss loudly
7	--- entry 1 ---
8	ROOT [Indo-Schythian] Bŭnai : naked, uncovered  (refs ISS:256)
9	#1 (parent #0) [Avestan] refs=ISS:256 | mağna : naked | NOTE: See "Nogw: naked" for another possible root
10	  #2 (parent #1) [Pahlavi] refs=ISS:256 | brahnak : naked
11	    #3 (parent #2) [Persian] refs=ISS:256; MON:517 | berehneh «برهنه» : naked | NOTE: See "Nogw: naked" for another possible root.
12	#4 (parent #0) [Sogdian] refs=ISS:256 | bğn`k, bğny : naked
13	--- entry 2 ---
14	ROOT Bŭqčâ -> redirect to Boqčâ
15	--- entry 3 ---
16	ROOT [Aramaic] Busmâ, Besmâ : perfume  (refs TAD:12; KLN:144)
17	#1 (parent #0) [Hebrew] refs=KLN:144 | bâsam : spice, balsam plant
18	  #2 (parent #1) [Greek] refs=KLN:144 | balsamon : balsam plant
19	    #3 (parent #2) [Arabic] refs=TAD:12; MON:567 | bašâm : perfume ; balsâm : balsam plant
20	      #4 (parent #3) [Persian] refs=MON:540,567 | balsâm «بلسام» : any resinous plant ; bašâm «بَشّام» : seed of a balsam plant
21	    #5 (parent #2) [Latin] refs=KLN:143 | balsamun : balsam
22	      #6 (parent #5) [English] refs=KLN:143 | balsam, balsamine, balm, embalm
23	--- entry 4 ---
24	ROOT B.w.s -> redirect to B.y.z
25	
```


## [2026-09-05T14:40:38.663Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-102.json",
 "description": "Read page 102 source JSON"
}
```


### [2026-09-05T14:40:38.701Z] TOOL RESULT

```
{
  "pdf_page": 102,
  "book_page": 72,
  "entries": [
    {
      "root": {
        "name": "Bu",
        "lang": "Indo-European",
        "refs": "POK:103; SYN:1113",
        "gloss": "lip, kiss",
        "note": "Kissing, as an expression of affection, is unknown among many races.  There is no conclusive evidence that kissing was known in the Indo-European times."
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "POK:103",
          "words": [
            {
              "translit": "bŭs",
              "gloss": "kiss",
              "script": "بوس"
            }
          ],
          "script_extra": "بوسیدن",
          "note": null,
          "quote": {
            "text": "رخ لاله چون گشت سندروس - به پیش سپهبد زمین داد بوس",
            "poet": "Ferdowsî"
          }
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {
              "translit": "kusjan",
              "gloss": "to kiss",
              "script": null
            }
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
            {
              "translit": "buss",
              "gloss": "to kiss loudly",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Bŭnai",
        "lang": "Indo-Schythian",
        "refs": "ISS:256",
        "gloss": "naked, uncovered"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "ISS:256",
          "words": [
            {
              "translit": "mağna",
              "gloss": "naked",
              "script": null
            }
          ],
          "script_extra": null,
          "note": "See \"Nogw: naked\" for another possible root",
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "ISS:256",
          "words": [
            {
              "translit": "brahnak",
              "gloss": "naked",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "ISS:256; MON:517",
          "words": [
            {
              "translit": "berehneh",
              "gloss": "naked",
              "script": "برهنه"
            }
          ],
          "script_extra": null,
          "note": "See \"Nogw: naked\" for another possible root.",
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Sogdian",
          "refs": "ISS:256",
          "words": [
            {
              "translit": "bğn`k, bğny",
              "gloss": "naked",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Bŭqčâ",
        "redirect": "Boqčâ"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Busmâ, Besmâ",
        "lang": "Aramaic",
        "refs": "TAD:12; KLN:144",
        "gloss": "perfume"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Hebrew",
          "refs": "KLN:144",
          "words": [
            {
              "translit": "bâsam",
              "gloss": "spice, balsam plant",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Greek",
          "refs": "KLN:144",
          "words": [
            {
              "translit": "balsamon",
              "gloss": "balsam plant",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Arabic",
          "refs": "TAD:12; MON:567",
          "words": [
            {
              "translit": "bašâm",
              "gloss": "perfume",
              "script": null
            },
            {
              "translit": "balsâm",
              "gloss": "balsam plant",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Persian",
          "refs": "MON:540,567",
          "words": [
            {
              "translit": "balsâm",
              "gloss": "any resinous plant",
              "script": "بلسام"
            },
            {
              "translit": "bašâm",
              "gloss": "seed of a balsam plant",
              "script": "بَشّام"
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 2,
          "lang": "Latin",
          "refs": "KLN:143",
          "words": [
            {
              "translit": "balsamun",
              "gloss": "balsam",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "English",
          "refs": "KLN:143",
          "words": [
            {
              "translit": "balsam, balsamine, balm, embalm",
              "gloss": null,
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "B.w.s",
        "redirect": "B.y.z"
      },
      "nodes": []
    }
  ]
}
```


## [2026-09-05T14:40:40.710Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','SYN','AHD','ISS','MON','TAD','KLN','WLD','IEC','BRT','PHD','NYB','HRN','HUB','SOD','ARY','BQT','SKT','FVQ','AFM','PLA','CHEUNG']:\n    print(k, json.dumps(d.get(k),ensure_ascii=False)[:400])\n\""
}
```


### [2026-09-05T14:40:42.266Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
ISS {"title": "H. W. Bailey, Indo-Scythian Studies: Khotanese Texts VI (Prolexis to the Book of Zambasta), Cambridge 1967", "edition_found": "not found; Bailey's Dictionary of Khotan Saka (1979) downloaded as the closest substitute", "kind": "google_books_preview+archive_restricted", "url": "https://books.google.com/books?id=4upthUgWo9YC (CUP 2009 reprint, partial preview) ; HathiTrust mdp.39015034317
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
TAD {"title": "Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-hurufihi (2nd ed. Cairo 1932, ed. Yusuf Tuma al-Bustani; later Library of Lebanon reprint) — Nourai lists it under Arabic authors ('Unaysi T.'); its Table IV line was lost in the OCR", "kind": "archive_djvu", "url": "https://archive.org/details/TOB1932ARAR (1932 ed.); also https://a
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in 
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.t
AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_page
PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/
CHEUNG null
```


## [2026-09-05T14:40:59.521Z] TOOL CALL #5: Bash

```json
{
 "command": "sed -n 1,200p data/verification/sources/SOURCE_MATRIX.md"
}
```


### [2026-09-05T14:40:59.611Z] TOOL RESULT

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


## [2026-09-05T14:41:00.370Z] TOOL CALL #6: Bash

```json
{
 "command": "ls data/verification/sources/refs/ && echo ---- && ls data/verification/ | head -50"
}
```


### [2026-09-05T14:41:00.421Z] TOOL RESULT

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
SKT.txt
SNS_pages.txt
SNS.txt
SOD_pages.txt
SOD.txt
SPG_keilinschriften1881.txt
SYN.txt
TAD_pages.txt
TAD.txt
tessdata
TLM.txt
UNV.txt
WEB_vol1.txt
WLD_band3.txt
ZAP.txt
----
agent
page-101.json
page-126.json
page-311.json
page-31.json
page-32.json
page-33.json
page-345.json
page-34.json
page-35.json
page-36.json
page-37.json
page-38.json
page-39.json
page-40.json
page-41.json
page-42.json
page-43.json
page-44.json
page-45.json
page-46.json
page-47.json
page-48.json
page-49.json
page-50.json
page-51.json
page-52.json
page-53.json
page-54.json
page-55.json
page-56.json
page-57.json
page-58.json
page-59.json
page-60.json
page-61.json
page-62.json
page-63.json
page-64.json
page-65.json
page-66.json
page-67.json
page-68.json
page-69.json
page-70.json
page-71.json
page-72.json
page-73.json
page-74.json
page-75.json
```


## [2026-09-05T14:41:06.439Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i \"Lippe, Ku\" POK_full.txt | head -20; echo ---; grep -n \"^bu-\\|bu-, bhu-\\|b̯u-\" POK_full.txt | head -20"
}
```


### [2026-09-05T14:41:06.508Z] TOOL RESULT

```
---
```


## [2026-09-05T14:41:07.542Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 -c \"\nimport json,sys\nd=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'))\nfor k in ['POK','SYN','AHD','ISS','TAD','KLN','MON']:\n    print('==',k); print(json.dumps(d[k],ensure_ascii=False,indent=1))\n\""
}
```


### [2026-09-05T14:41:09.259Z] TOOL RESULT

```
== POK
{
 "title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)",
 "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/indogermanisches01pokouoft",
 "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt",
 "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\\data\\ie\\pokorny&root=config",
 "notes": "Nourai's page numbers are Band I 1959 pages, which match these scans. Band II (1969 index) is at pokorny-indogermanisches-etymologisches-worterbuch-band-ii-1969 (djvu 200). local_files: /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt (pp. 1-348), /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_02.txt (pp. 349-770), /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_03.txt (pp. 771-1183); /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_full.txt (unpaginated database text with 'Page(s): N' per root)",
 "local_files": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_02.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_03.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_full.txt"
 ],
 "cites": "page number of Pokorny, Indogermanisches etymologisches Wörterbuch, Band I (1959)"
}
== SYN
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
== AHD
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
== ISS
{
 "title": "H. W. Bailey, Indo-Scythian Studies: Khotanese Texts VI (Prolexis to the Book of Zambasta), Cambridge 1967",
 "edition_found": "not found; Bailey's Dictionary of Khotan Saka (1979) downloaded as the closest substitute",
 "kind": "google_books_preview+archive_restricted",
 "url": "https://books.google.com/books?id=4upthUgWo9YC (CUP 2009 reprint, partial preview) ; HathiTrust mdp.39015034317936 (v.6, search-only) ; archive.org khotanesetexts0103bail (vols I-III only, lending)",
 "identifier": "dictionary-of-khotan-saka (substitute); khotanesetexts0103bail is vols I-III, lending-only",
 "local_file": null,
 "page_offset": "DKS: leaf = printed + 17..19 (e.g. leaf 158 = p.139). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Khotanese Texts VI itself is not online. Nourai's ISS page numbers cannot be checked directly; the Dictionary of Khotan Saka (headword at line start, Khotanese in transliteration, with 'Pok.' refs) covers the same etymological material and can verify the substance of a claim.",
 "notes": "Tried IA ('indo-scythian', 'zambasta', 'khotanese texts'), Google Books API. || RE-SEARCH 2026-09: preview only (Google Books partial view of the 2009 reprint — usable for spot checks); no open full text. A dokumen.pub upload exists (not used)."
}
== TAD
{
 "title": "Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-hurufihi (2nd ed. Cairo 1932, ed. Yusuf Tuma al-Bustani; later Library of Lebanon reprint) — Nourai lists it under Arabic authors ('Unaysi T.'); its Table IV line was lost in the OCR",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/TOB1932ARAR (1932 ed.); also https://archive.org/details/ar113lang79 and https://archive.org/details/elshandawily14640",
 "lookup_hint": "Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; inside.php search works.",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD.txt"
 ],
 "page_offset": "86 leaves (small book, ~80 printed pages); offset ≈ leaf − 4..6, verify against the printed numeral on the page image",
 "covers_etymology": true,
 "notes": "Arabic OCR fair. Nourai's exact edition unknown; the Beirut reprint reproduces the 1932 pagination."
}
== KLN
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
== MON
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


## [2026-09-05T14:41:12.836Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for n in 110 111 112; do echo \"=== leaf $n ===\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' POK_01.txt | head -60; done"
}
```


### [2026-09-05T14:41:14.666Z] TOOL RESULT

```
=== leaf 110 ===
,Beutel; Sack'^,  engl,  poke  ds.,  nhd.  dial.  Pfoch  ,Beutek',  ags.  pohha,  pocca  ,Sack, Beutel^,  engl,  pocket  ,Tasche^,  mndd.  nndd.  pogge,  pfugge  , Frosch,  Kröte;' Geschwulst  am  Unterleib  bei  Kühen  und  Stuten%  ags.  pocc  ,Blatter'',  nhd. (eigentlich  ndd.)  Pocke,  dial.  Pfoclie  ,Blatter^;  anord.  pükt  m.  ,Teufel', ags.  pRca,  pücel,  engl,  puck  ,Kobold*  (aus  dem  Germ,  stammt  ir.  püca , Gespenst*,  vielleicht  auch  lett.  pük'is  ,Drache*);  hochstufig  ndd.  pök  ,im Wuchs  zurückgebliebener  Mensch*,  norw.  mdartl.  pauk  ^kleiner,  schwäch- licher Mensch,  Knabe*  (über  got.  puggs  ,Beutel,  Geldbeutel*,  anord.  pimgi) ags.  puug  ds.  und  scaz-(p)fung  ,Geldbeutel*   s.  jedoch  Feist  385).
Mit  germ.  b:  mengl.  nengl.  big  (*bugja-)  ,dick,  groß,  aufgeblasen*;  norw. mdartl.  bugge  ,mächtiger  Mann*,  mengl.  bugge  (engl,  bug)  ,Rotzklumpen; Käfer,  Wanze;  Schreckgespenst*,  nhd.  mdartl.  högg{e)  ,Nasenbutzer,  Butzen am  Obst,  Schre.ckgespenst*.  Hierher  vermutlich  germ.  *buh-  (idg.  *bhuk-) in  ahd.  buhll  , Bühel*,  aisl.  böla  f.  ,Beule,  Schildbuckel*  (*buhlön-)  und  *b^k' (idg.  *blMg-)  in  Schweiz.  Bücki  ,Faß*,  engl,  bück  ,Waschkübel*  und  aisl. bükr  ,Bauch,  Leib*,  ags.  hüc  ,Bauch,  Krug*,  ahd.  bäh,  nhd.  Bauch,  dazu lett.  bugarains  ,höckerig*,  buga  ,hornlose  Kuh*,  budzis  ,Beule,  unreifes Obst*;  aber  lit.  bauzas  ,hornlos*,  bidys  ,Yogelscheuche,  Schreckbild*,  büzys ,Wanze,  Laus*,  büoze  , Keule,  Nadelkopf*  {üo  wohl  aus  öu,  vgl.  oben  S.  99
101
...    s  köiineu   balt.  i  als  einzelsprachliches    Formans  enthalten  und  auf al^r  unerweiterten  Wurzel  beruhen.
5-Erweiterung:
T*hhousto-,  vgl.  aisl.  heysti  ^Schinken'),  anord.  jpüss  ^Tasche^  BeuteP^  isl. üose  ags.  pusa,  posa,  ahd.  pfoso  ^Beutel';  mit  der  ursprünglicheren  Bed. .1)lasen^  aufblasen,  schwellen',  asch^ved.  pysa  ^schnauben',  mhd.  pfüsen schnauben,  niesen',  sich  pfüsen  ,sich  aufblähen',  nhd.  mdartl.  pfausen, ao-s.  pos  ,Schnupfen,  Wasserfall',  engl,  pose  ,Schnupfen',  mndd.  pusten /chnauben',  püster  ,Blasebalg',  nhd.  pusten  (eigentlich  ndd.)  mdartl.  pfau- sten  anord.  püstr  ,Ohrfeige'  (wie  frz.  soufflet  zu  souffler)]  norw.  pös, Ge- schwulst', peysa,  püsna  ,ansch wellen',  Schweiz,  pfüsig  ,gesch wollen',,  nhd. Pfausback,  mit  ndd.  Anlaut  Pausback  (
=== leaf 111 ===
daneben  Bausback  mit  germ,  b-^ s.  unten);  norw.  mdartl.  pusling  ,Knirps,  Kobold',  Schweiz.  Pfosi  ,Knirp^,. unbeholfener,  blöder  Mensch'  (,karz  und  dick');  norw.  püs,  peysa  ,Schlamm- pfütze',  anord.  pyss  ds.  (in   Ortsnamen).
Mit  germ.  h  (=  idg.  bli,  z.  T.  vielleicht  unverschobenes  oder  neues  6): ags.  bösom  (germ.  *büs-mo(n)-)j  ahd.  buosam,  mhd.  buosem,  bnosen,  nhd. BuseUy  mhd.  büs  , Aufgeblasenheit,  schwellende  Fülle',  büsen  ,schwelgen', nhd.  bausen  ,zechen,  schwellen',  Baus  ,abundantia,  tumor,  inflatio',  Baus- back, Bausch  ,ansch wellendes,  wulstiges  Kissen,  ausgestopfte  Brust',  mhd. büsch  ,Wulst,  Bausch',  anord.  busilkinna  .pausbackiges  Weib',  norw.  baus ,stolz,  übermütig,  heftig,  hitzig',  ahd.  bösi  ^hartherzig,  schlecht',  nhd.  böse, mengl.  basten,  nengl.  to  boast  ,großsprechen,  prahlen'  (,*sich  aufblähen'), nisl.  beysinn  ,dick,  weit  und  groß  (von  Kleidern)',  büstinn  ds.,  aisl.  beysti ,Schinken',  nhd.  mdartl.  Baust  ,Wulst',  bauste{r)n  ,schwellen',  ahd.  biost, nhd.  Biest-milch  (eigentlich  ,dicke  Milch'),  ags.  beost,  bysting,  engl,  beast- ings,  biestings  ds.,  norw.  mdartl.  budda  (*buzdön-)  ds,  (unsicherer  ist,  ob schwed.  mdartl.  huska  ,frisches,  aufgärendes  Bier'  und  das  damit  als  *heuza-^ verbundene  ahd.  bior,  ags.  beoi-  ,Bier'  als  das  , Aufschäumende,  Blasen- werfende' anzureihen  sei;  über  andere  Deutungen  von  Bier  s.  Kluge ^^ und  Weigand-Hirt).
Russ.  büchnuth  ,anschwellen,  quellen',  sloven.  bühnem,  bühniti  ,anschwellen, sich  aufblasen',  bühor  ,Wasserblase',  kasch.  buclia  , Hochmut'   (*bausä).
Verwandt  ist  wohl  auch  folgende  Gruppe,  deren  Bed.  ,hervorbrausen' aus  ,aufsch wellen'  entwickelt  sein  kann:  aisl.  bysia  ,mit  großer  Gewalt ausströmen';  norw.  mdartl.  boysa  ,hervorstürmen';  schwed.  busa  ,bestür- zen,  hervorstürzen';  ostfries.  büsen  ,gewaltsam  sein,  brausen,  lärmen,  stür-
m
102  •
men^  (und  .in  Saus  und  Braus   leben^;   vgl.  oben  mlid.  hüsen  ^schwelgen'), büsterlg  ^stürmisch^  aksl.  bysti-o  ^verschlagen^,  russ.  bijstryj  ^schnell;  scharf, sichtig;  reißend  von  der  Strömung*   {*bhüs-ro-). WP.  II  114  f.,  Trautmann  28,  39.
Lat.  bilis  (*bislis,  älter  Hi
=== leaf 112 ===
stlis)  f.  ^Galle'^;    cjmr.  bnstl  m.,  acorn.  bistel^ bret.  bestl  {His-tlo-,  -tli-)  ,Galle^;  gallo-rom.  *bistlos  (Wartburg). WP.  II  111,  WH.  I  105  f.
blat-  ,plappern  u.  dgl.  Schallbedeutungen^  sowie  ähnliche  Schallworte  schwer bestimmbaren  Alters.
Lat.  blaterö,  -äre  ,plappern,  dumm  daherschwatzen ;  auch  vom  GeschreiJ des  Kamels,  Widders,  Frosches^,  blatiöy  -Ire  ,plappern,  schwätzen^;
mndd.  'plad{d)eren  ^schwätzen,  plaudern^,  nndd.  pladdern  ,platschen,  be- spritzen^, schwed.  pladder  ,loses  Geschwätz^,  dän.  bladre  ,loses  Geschwätz treiben^,  älter  auch  ,platschen^,  mit  fehlender  Lautverschiebung  im  Schall- 'J' wort.  'X.
Ähnliche  Schall worte  sind  ndd.  ^Zapperen  {xi]idi.  plappern) j  m)[idi.  plappen^ und  blappenj  ahd.  blabizön  ,plappern'  und  mndd.  plüderen  , plappern' i (mhd.  plüdern,  nhd.  plaudern).
Vgl.   mit   z.  T.    ähnlicher    Bed.    hhltd-    , aufsprudeln,    schwatzen',    bhel- , schallen'    und   bal-,  bal-bal-  unter  baba-   (z.  B.  lit.  blebenti   mit  dem  nhd.^ plappern  ähnlicher  Bildung).
WP.  II  120,   WH.  I  109.
hie-  , blöken'.  Nachahmung  des  Schaflautes  mit  verschiedenen  gutturalen Erweiterungen;  im  Germ,  mit  infolge  steter  Neunachahmung  unter- bliebener Lautverschiebung.
Gr.  ßXrjxdoiiai  , blöken',  ß^r^xri  ,das  Blöken';  russ.  (usw.)  blekati  (alt),  1j] blekotdth  , blöken' ;  mndd.  bleken,  blöken  ,blöken,  bellen'  (daraus  nhd.  hVö-  ■% ken),.  aorw.  mdartl.  blskta  (*blekatjan)  ,blöken';  alb.  bVegerds  ds.
WP.  II  120  f.,  W^H.  I  95.   Vgl.  auch  bhU-  ,heulen'  usw.
blou'  (bblou-?),  plou'  ,Floh'.    Mit  k-  und  s-Suffixen  und  tabuierender  Um- stellung und  Anlautswechsel. Mit  p|:  ai.  phisl-,  arm.  lu  (*plus-),  alb.  plesht,  lat.  pülex  (*pusl-ex),  idg. *plouk-  in  ahd.  floh,  ags.  fleah.
Mit  b  (oder  bb?):  afgh.  vraBa,  gr.  yjvXXcc  (*blusiä),  balto-slav.  *blusä in  lit.  blusä,  lett.  blusa,  pr.  ON  Blus-kaym,  russ.-ksl.  bhcha,  skr.  büha, russ.   biochd.
Meillet  MSL.  22,  142,  539  f.,  Trautmann  35,  Specht  Dekl.  42  f.,  203,  235.
I
103
wo/.  , Knolle,  runde  Schwellung'.
Arm.  ^ö/^  , Radieschen',  gv.  ßolßög  , Zwiebel'  (auch  ßölßiTog^  dissimi- liert att.  ßohfog  ,Mist',  -wenn  etwa  ursprüngl.  von  Ziegen  oder  Pferden?), diüXogj  /^tD
```


## [2026-09-05T14:41:19.265Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==113' POK_01.txt"
}
```


### [2026-09-05T14:41:20.902Z] TOOL RESULT

```
A«?  , Erdscholle' 5  ai.  bdlha-ja-h  ,Eleusine  indica,  eine  Grasart', trenn  ,aus  Wurzelknollen  hervorkommend'?,  lat.  bulhus  , Zwiebel,  Bolle' ist  aus  ßolßoq  entlehnt.
Redukt.-stufig-  oder  mit  Assimil.  an  den  Vok.  der  2.  Silbe  arm.  falar Pustula,   boUa'.
WP.  11  Ulf»   ^^'^'  1   122.
brsngh-,  brongh'?  ,heiser'?
Gr.  ßqayxoq  , Heiserkeit',  ßqayxaco  ,bin  heiser',    air.  hrong{a)ide  ,heiser'; aber  g'r.  Aor.  eßqaxe  , krachte'  bleibt  wohl  fern. \VP,  I  683  f.,  II  119.
treuq-  , springen,  schnellen'.
Vielleicht  vereinigen  sich  so  gr.  ßgov-aog,  ßQevAog  (ßgavT-og),  ßgvycog  , Heu- schrecke' (ßgovxog  wohl  nach  ßqtxo)  , knirsche  mit  den  Zähnen',  und  sloven. hrknem,  brkniti,  hrkam,  bvkati,  brcati  ,mit  den  Füßen  stoßen,  ausschlagen, mit  den  Fingern  wegschnellen',  russ.  brykäth  ,mit  den  Hinterfüßen  aus- schlagen, klr.  brykdty  ^mutwillig  herumspringen,  laufen'  usw.
WP.  II  119,  Specht  Idg.  Dekl.  251  f.
bronk-  , einschließen,  einengen'.
Got.  anapraggan  , bedrängen'  zu  *pranga-  ,Beengung'  in  aschwed.  prang ,enge  Gasse',  mengl.  prange  ,Enge',  engl.  dial.  proug  , Tischgabel',  mndd. prangen  , drücken',  pranger  , Pfahl',  mhd.  pfrengen  ,einzwängen',  ahd. pfragina  , Schranke',  zu  lit.  branktas  m.  , Strangholz',  lett.  brankti  (lit.  Lw.) jfest  anliegend'.
WP.  II  119,  677  f.,  Feist  43,  Kluge  ^^  unter  Pranger.
bU'  ,Lippe,  Kuß',    als  Nachahmung  des  Kußlautes,    Sprengung   des  saugen- den Lippenverschlusses  nach   innen,    also   eigentlich  verschieden  von bu-j  bhii-  , aufblasen'  mit  normaler  Sprengung  nach  außen. Npers.  bösidan  ,küssen';  alb.  buze  ,Mund';   mir.  bus,  pus  , Lippe',  busöc, pusöc  ,Kuß'  (dazu  vermutlich  gall.  PN  Bussumäros  und  buMutton  ,Mündchen, Kuß');  nhd.  Buss  ,Kuß',  bussen  ,küssen',  Busserl  ,Kuß',  engl,  buss,  schwed. (mit  regelrechter  Lautverschiebung)  puss  ,Kuß';   lit.  bn6iüoti  , küssen',  buc den    Schall    des    Kusses    malende    Interjektion,    poln.    buzia    , Mündchen, Mäulchen;  Kuß'. WP.  I  113f.,  WH.  II  98.
Bh.
bhä-,  hhö'f  bhQ'  ,gläazen,  leuchten,  scheinen*.
Ai.  bhä  (in  Kompos.)  , Schein,  Licht,  Glanz',  hhäti  ,leuchtet,  (er-)scheint'' bhäti-hi  , Licht',  bhäna-m  n.  ,das  Leuchten,  Erscheinung'  (vgl.  air.  häii, ,vveiß',  ags.  bönian  , polieren'),  bhänü-h  , Licht,  Strahl,  Sonne'  (:  as.  banu-tj^ bhäma-h  , Licht,  Schein';  t
av.  bä-  , scheinen'  nur  mit  ä-  [aväntdm  ,den  gleichenden'),  frä  (fra- väiti  ,leuchtet  hervor')  und  vi-  (yi-bä-  , leuchten',  Benveniste  BSL.  32,  86  f.)^ vispö-bäm(ij)a-  , allglänzend',  bämya-  , licht,  glänzend',  bäirn-  m.  .Licht* Strahl';  ^
arm.  banam  (*bhä-n-)  , öffne,  enthülle'  (wenn  eigentlich  , zeige,  lasse  sicht- bar werden'),  Aor.  ba-t''si,  vgl.  gr.  cpah'ü)  und   alb.  bdj  ]
gv.  TtEcpriasTai  ,wird  erscheinen',  *-bJid-n-  im  Präse
```


## [2026-09-05T14:41:32.968Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i \"kussjan\\|kussa\\|cyssan\\|\\bbuss\\b\" AHD_watkins1985.txt | head -20; echo \"=== ku- ===\"; grep -n \"^ku-\\|^bu-\\|^bu\\b\" AHD_watkins1985.txt | head"
}
```


## [2026-09-05T14:41:32.984Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"16.2\\|KISS\" SYN.txt | head -20"
}
```


### [2026-09-05T14:41:33.038Z] TOOL RESULT

```
808:Grk. x#av (mostly poet. and in sense b), beside xayuai ‘on the ground’, xPapadds, xaundds ‘on the ground, low lying’; Lat. humus (mostly in sense b) beside humt ‘on the ground’, humilis ‘low’; Ir. diz, gen., ace. don ‘place’, early ‘earth’ (Pedersen 1.89, Vendryes, RC 40.437 ff.); Lith. Zemé, Lett. zeme, OPruss. semmin (acc. sg.), ChSl. zemlja, etc., general Balto-Slavic for ‘earth’ and ‘land’; Skt. ksam- (gen. usually jmas), Vedic and in sense b, esp. ‘earth’ vs. ‘sky’; Av. zam- (gen. zemo = Skt. jmas) ‘earth’ in all senses (Barth. 1662 ff.); Alb. dhe ‘earth’.
2773:Pol. wesele ‘wedding’, formerly ‘mer- riment’ : ChSI. veselije ‘merriment’ vese- li ‘merry’ (16.22), Briickner 607.
7720:Lett. vesels (hence veseliba ‘health’): ChSI. veseli ‘joyful, gay’ (16.22).
10393:’ cape, NE cope, OFr. cape). Ernout- i 1162. REW 1642. etym,? eee lenn, Gall. linna),
11867:5. Lith. asla, etym.? (connection with L. area or OHG asirih, BB 16.207, un- likely).
13311:an Gd drai ‘druid’, Gall. Z. celt. Ph. 16.277) ‘beam, shaft, wood’, Chsl.
16827:u-statt, Boh. pov-stati, Pol. pow-staé, Russ. v-stat’, Skt. ut-tha (= ud-stha), Av. us-std-. Barth, 1602.
17406:Rum. juca, orig. ‘play’ like Fr. jouer, etc. (16.27), but used also for ‘dance’, influenced by the double use of Slavic igrati (below, 6).
17438:ChSl. igrati ‘leap, spring, dance’ SCr. igrati ‘dance’, refl. ‘play’, general Slavic word for ‘play’ (16.27) : Skt. ej- ‘stir, move, tremble’, ON eikenn ‘wild raging’, etc. Walde-P. 1.11. Berneker 422.
17973:It. cacciare, Fr. chasser ‘drive away, drive’, also ‘hunt’ (3.81), fr. VLat. *captiare : capere ‘seize, take’. REW 1662.
21080:derivatives of It. costo, ete. ‘cost? (11.72), as It., Sp. costoso, OF r. costeus (> ME costouse > W. costus), Fr. cotteux, NE costly, NHG kostbar, etc. 1. Grk. zodvredjs, cpd. of zodb ‘much’ and last member fr. rédos ‘tax, toll, duty’ (11.69). Grk. riptos, fr. riuy ‘price’ (11.87). NG dxpiBés, fr. class. Grk. axpifis ‘exact, precise, accurate’ then (fr. ‘exact in money matters’) ‘parsimonious, stin- gy’ and hence ‘dear’ (as SCr. skup, be- low). 2. Lat. carus (> It., Sp. caro, Fr. cher) ‘dear’ = ‘beloved’ (16.28) and ‘ex- pensive’ (Plaut. in both senses). Rum. scump, fr. Slavic, cf. Bulg. ska- pu, etc. below, 6. 3. Ir. logmar, epd. of log ‘price’ and mar, mor ‘great’.
25217:It. alle volte (qualche volta, talvolta, etc.), Fr. quelquefois, parfois, Sp. a veces, algunas veces, Rum. citeodaté (dis- tributive cite and odatdé ‘once’, Tiktin 507 f.), uneori (Tiktin 1067, 1682); Ir. iar n-tairib, i n-aairib (Thes. 2.332.21, 23; war ‘hour, time’, 14.51), NIr. ar uaribh, amanna, W. weithiau, ambell waith, Br. a-wechou, gwechennou; ON, OE stundum, Dan., Sw., stundom, OE hwilum, hwile, ME while (cf. NED s.vv. whilom and while, adv. 1), MHG bi- wilen, under wilen, NHG bisweilen, zu- weilen, Dan. undertiden, Du. somtijds, NE sometimes; Lith. kartais, Lett. reizu reizem (Miihl.-Endz. 3.507); Pol. czasem.
25645:1. Ecclesiastical system. The Jews named only one day of the week, name- ly, the last, the Sabbath, Grk. caBBarov. The other days were merely numbered. Since the Sabbath was the distinctive sign of the week, it came to be used also in the sense ‘week’ (cf. 14.51). Hence in the New Testament pia caBBatwy (Mt. 28.1, etc.), 7 ula Tay caBBarwy (Mk. 16.2, etc.), also mpw7n cafBarov (Mk. 16.9),
25658:in Goth., and there are a few in West and North Gme. amid the usual planetary names. Goth. sabbato (mostly unin. flected but also with w- and i-stem forms) with and without dags = Grk. c4BBaroy Or juépa caBBarwy (but independently of the Grk. variation), pis dagis afarsab- baté = ris yds caBBarwy (Mk. 16.2), Srumin sabbatd = xpirn caBBarov (Mi. 16.9), fruma sabbatd = rpoc&BBaroy (Mk. 15.42), beside the borrowed paraskaiwé = mapacxevn (Mt. 27.62, Mk. 15.42),
27428:16.21 PuasE
27429:16.212 Purassz (in polite phrase) 16.22 Jor
27430:16.23 JoyrruL, GLAD
27431:16.24 Happy, Happiness
27432:16.25 Laueu (vb.); Size (vb.) 16.26 Puay (vb.)
27433:16.27 Love (sb.; vb.)
```


### [2026-09-05T14:41:33.045Z] TOOL RESULT

```
648:English hréowan, to distress, grieve: RUE!, RUTH. 2. Ex- tended o-grade form *krous- in Greek krouein, to strike: ANACRUSIS. [Pok. 3. kreu- 622.] kreup-. Scab; to become encrusted. 1. Germanic *hrub- in: a. Middle Low German ruffelen, to crumple, akin to the Germanic source of Middle English ruffelen, to ruffle, roughen: RUFFLE}; b. Germanic compound *ga-hrub- (*ga-, intensive prefix; see kom) in Middle Dutch grof, harsh: GRuFF. 2. Suffixed o-grade form *kroup-d in Serbo-Croatian krupa, groats (perhaps > German Graupe, barley): GRAUPEL. [Pok. kreup- 623.] kreus-. To begin to freeze, form a crust. 1. Suffixed zero-grade form *krus-to- in: a. Latin crusta, crust: CROUTON, CRUST, CRUSTACEAN, CRUSTACEOUS, CRUS- TOSE; b. Greek krustallos, ice: CRYSTAL, CRYSTALLINE, CRYSTALLO-. 2. Suffixed zero-grade form *krus-es- in Greek kruos, icy cold, frost: cryo-. [Pok. 1. B. kreu- 621.] kreut-. Also kreudh-. Reed. Germanic *hreuda- in Old English hréod, reed: REED. [Pok. kreut- 623.] kropo-. Roof. Germanic *hréfam in Old English hrdf, roof: ROOF. [Pok. krdpo- 616.] krut-. Musical instrument. 1. Germanic *Arut- in Old French rote, a stringed instrument: ROTE3, 2. Geminated form *krutté in Welsh crwth, an ancient Celtic instru- ment: CROwD?. [Pok. krut- 624.] ksero-. Dry. 1. Lengthened-grade form *kséro- in Greek xéros, dry: XERO-; ELIXIR, PHYLLOXERA, XEROPHTHAL- MIA. 2. Perhaps suffixed variant form “kseres-no- in Latin serénus, serene, bright, clear: SERENE. [Pok. ksero- 625.] ksun. Preposition and preverb meaning “with.” 1. Greek sun, xun, together, with: syN-. 2. Russian so-, s-, with, in sputnik, fellow traveler (see pent-): SPUTNIK. [In Pok. 2. sem- 902.] ku-. Hypothetical base of a variety of conceivably related Germanic words meaning “a hollow space or place, enclosing object, round object, lump,” and some other derivative denotations. 1. Germanic *kubdn-, hut, shed, room, in: a. Old English cofa, bedchamber, closet: COVE!; b. Middle Dutch cubbe, “pen, stall,” fish basket, akin to the probable source of CUBBY; C. Germanic compound *kubawald-, probably “house ruler,” household god (wald-, power; see wal-), in Middle High German kobolt, an underground goblin: COBALT, KOBOLD. 2. Germanic *kutam in Old English cot, cottage: COT?, (COTTAGE). 3. Germanic *kutdn- in Old English cote, shelter: CoTE!. 4. Germanic *k(e)ud- in: a. Old English codd, bag, husk: cop?; b. Old English cudele, cuttlefish (from its ink bag): CUTTLE. 5. Germanic k(e)ut- in Old English *cieter, intestines (probably > Middle English chiterling): cx1T- TERLINGS. 6. Germanic *kukk- in Middle English cok, haycock, pile of straw: cock?. 7. Germanic *kuk- in Old English cicen, chicken: CHICKEN. 8. Germanic *kugg- in Swedish kugge, cog, akin to the possible Scandinavian source of Middle English cogge, cog: coc}. 9. Germanic *kuggila in Old English cycgel, rod, cudgel: CUDGEL. 10. Germanic *keulaz in: a. Low German kielswin, keel- son: KEELSON; b. Middle Dutch iel, ship, keel of a ship: KEEL?, 11. Germanic *kijp- in Middle Dutch kipe, cask, tub, basket: COOPER. 12. Germanic *kunt- in Middle Low German kunte, vulva, akin to the Low German source of Middle English cunte, vulva: CUNT. 13. Germanic kird- in Icelandic kiird, to crouch, lie in wait, akin to the Scandinavian source of Middle English couren, to cower: COWER. 14. Possibly Old Norse kiiga, to oppress, akin to the probable source of cow?. [In Pok. géu- 393.] kus-. A kiss. Germanic *kussaz, a kiss, with denominative *kussjan in Old English cyssan, to kiss: Kiss. [Pok. ku-, kus- 626.] kwat-. To ferment, be sour. Possible root. Suffixed vari- ant form *kwét-so- in Common Slavic *kvasi in Russian kvas, kvass: Kvass. [Pok. kuat(h)- 627.] kwe, And (enclitic). Latin -que, and: SESQUI-, UBIQUITY. [Pok. kve 635.]
=== ku- ===
```


## [2026-09-05T14:41:40.193Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"BUSS\\|Buss\\b\" AHD_watkins1985.txt | head -10; echo \"=== sed context around index ===\"; sed -n '27425,27450p' SYN.txt"
}
```


### [2026-09-05T14:41:40.254Z] TOOL RESULT

```
1013:STICKLE. 3. Suffixed form *stigh-o- in Greek stikhos, row, line, line of verse: STICH; ACROSTIC, CADASTER, DISTICH, HEMISTICH, ORTHOSTICHOUS, STICHOMETRY, STICHO- MYTHIA. III. O-grade form *stoigh-. 1. Suffixed form *stoigh-ri- in Germanic *staigri in Old English stéger, stair, step: STAIR. 2. Greek stoikheion, shadow line, element: STOICHIOMETRY. [Pok. steigh- 1017.] steip-. To stick, compress. 1. Germanic *séifaz in: a. Old English séff, rigid, stiff: stirF; b. Dutch stip, tip, point: STIPPLE. 2. Latin stipes, post, tree trunk: STIPE, STIPES. 3. Suffixed form *steip-d- in Latin stipdre, to compress, stuff, pack: STEEVE!, STEVEDORE; CONSTIPATE. [Pok. stéib(h)- 1015.] stel-. To put, stand; with derivatives referring to a standing object or place. I. Basic form *stel-. 1. Suffixed form *stel-ni- in Germanic “*stilli- in Old English stile, quiet, fixed: sTILL’. 2. Suffixed form “stel-yo- in Greek stellein, to put in order, prepare, send, make compact (with o-grade and zero-grade forms sfol- and stal-): APOSTLE, DIASTOLE, EPISTLE, PERISTALSIS, SYSTALTIC. II. O-grade form *stol-. 1. Suffixed form *sfol-no- in Germanic *stalla- in: a. Old English steall, standing place, stable: STALL; FORESTALL; b. Old French estal, place: INSTALLMENT!; Cc. Old French estalon, stallion: STALLION; d. Old Italian stallo, stall: PEDESTAL; e. Me- dieval Latin stallum, stall: INSTALL; f. Germanic denomi- native *stalljan in Old High German stellen, to set, place: GESTALT. 2. Suffixed form stol-6n- in Latin stolé, branch, shoot: STOLON. 3. Suffixed form *stol-ido- in Latin stoli- dus, “firm-standing,” stupid: sTOLID. 4. Suffixed form *stol-d- in Greek stolé, garment, array, equipment: STOLE}, III. Zero-grade form “*stj-. 1. Suffixed form *stl-to- in Latin stultus, foolish (< “unmovable, unedu- cated”): STULTIFY. 2. Suffixed zero-grade form “st/-no- in Germanic *stullén- in Old High German stollo, post, support (> German Stolle, Stollen, stollen): sTOLLEN. 3. Suffixed zero-grade form *stal-nd- in Greek stélé, pillar: STELE. IV. Extended form “stelg- in Germanic *stalk- in Norwegian dialectal stalk, stalk, akin to the source of Middle English stalk(e), stalk: sTALK’. V. Ex- tended form *steld- in: a. Germanic *stiltjon- in Low German and Flemish sfilte, stick, akin to the source of Middle English stilte, crutch, stilt: sTILT; b. zero-grade form “*stld- in Germanic *stult-, “walking on stilts,” strutting, in Old French estout, stout: stout. [Pok. 3. stel- 1019.] stele-. To extend. Zero-grade form “*sélo-. 1. Suffixed form *stlo-to- in Latin /atus, broad, wide: LATITUDE; DILATE. 2. Attributed by some to this root (but more likely of obscure origin) is Latin /aémina, place, layer: LAMELLA, OMELET. [Pok. 2. stel- 1018.] sten-. Narrow. Suffixed form *sten-wo- in Greek stenos, narrow: STENO-, STENOSIS. [Pok. 2. sten- 1021.] (s)tene-. To thunder. 1. Zero-grade form *stno- in Ger- manic *thunaraz in: a. Old English thunor (genitive thunres), thunder, Thor: THUNDER; THURSDAY; b. Middle Dutch doner, donder (> Dutch donder), thun- der: BLUNDERBUSS, DUNDERHEAD; C. Old Norse Thorr (older form Thunarr), “thunder,” thunder god: THOR. 2. O-grade form *tona- in Latin tondre, to thunder: TORNADO; ASTONISH, DETONATE, STUN. [Pok. 1. (s)ten- 1021.] ster-'. Stiff. I. O-grade form *stor-. 1. Suffixed form *stor-é- in Germanic *staren in Old English sfarian, to stare: STARE. 2. Suffixed form *stor-g- in: a. Germanic *starkaz in Old English stearc, hard, severe: STARK; b. Germanic denominative *starkjan in Old English *stercan (> Middle English starchen), to stiffen: STARCH. II. Full-grade form *ster-. 1. Germanic *sternjaz in Old English stierne, styrne, firm: STERN}. 2. Suffixed form *ster-ewo- in Greek stereos, solid: STERE, STEREO-; CHOLESTEROL. 3. Lengthened-grade form *s¢ér- in Greek stérizein, to support: STERIGMA. III. Zero-grade form *str-. 1. Extended form *strg- in Germanic *sturkaz in
1309:BITE bheid- BITTER bheid- BITTERN! beu-2 BITUMEN gWet-1 BIVOUAC ambhi, weg-2 BLACK bhel-1 BLACKMAIL méd- BLADDER bhié-2 BLADE bhel-3 BLAIN bhlei- BLAME bha-2 BLANCH bhel-1 BLANCMANGE bhel-1 BLAND mel-1 BLANDISH mel-1 BLANK bhel-1 BLANKET bhel-1 BLARE bhié-1 BLASPHEME bha-2 BLASPHEMOUS bha-2 BLAST bhlé-2 -BLAST melst- BLASTEMA melst- BLASTO- melst- BLASTULA melst- BLATHER bhlé-2 BLAZE! bhel-1 BLEACH bhel-1 BLEAK! bhel-1 BLEAK? bhel-1 BLEAT bhlé-1 BLEMISH bhel-1 BLENCH! bhel-1 BLEND bhel-1 BLENDE bhel-1 BLENNY mel-1 BLESBOK bhel-1, bhugo- BLIND bhel-1 BLINDFOLD bhel-1 BLINI mele- BLINTZ mele- BLISTER bhlei- BLITE mele- BLITZKRIEG bhel-1, gwere-2 BLOAT bhieu- BLOND bhel-1 BLOOM! bhel-3 BLOOM? bhel-3 BLOSSOM bhel-3 BLOW! bhié-2 BLOW3 bhel-3 BLUE bhel-1 BLUNDERBUSS (s)tene- BLUSH bhel-1 BOARD bherdh- BOAST! beu-1 BOAT bheid- BOATSWAIN bheid- BOCACCIO beu-1 BODE! bheudh- BODEGA dhé-1 BODHISATTVA bheudh-, es- BoER bheue-
=== sed context around index ===
16.15 Wonprr, ASTONISHMENT 16.16 Surprise
16.17 Fortune (Good or Bad) 16.18 Goop Fortune
16.19 MuisroRTUNE
16.21 PuasE
16.212 Purassz (in polite phrase) 16.22 Jor
16.23 JoyrruL, GLAD
16.24 Happy, Happiness
16.25 Laueu (vb.); Size (vb.) 16.26 Puay (vb.)
16.27 Love (sb.; vb.)
16.28 Drar
16.29 Kuss (vb.)
16.31 Pain, SUFFERING
16.32 Grier, Sorrow
16.33 AnxiEeTy
16.384 Recret (vb.), Repent 16.35 Pyrry (sb.)
16.36 Sap
16.37 Cry, WEEP
16.38 Tsar (sb.)
16.39 Groan (vb.)
16.41 Hares (sb.)
16.42 ANGER
In this chapter we need not be con- cerned with such moot questions as the definition and precise character of emo- tions; the differentiation of emotions, passions, moods, etc.; the selection of certain emotions as primary; the divi- sion into pleasant and unpleasant or other types of classification. The rela-
1084
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
16.43 Races, Fory
16.44 Envy, JEALousy
```


## [2026-09-05T14:41:48.671Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"16\\.29\" SYN.txt | head; "
}
```


### [2026-09-05T14:41:48.715Z] TOOL RESULT

```
27435:16.29 Kuss (vb.)
28127:16.29 KISS (vb.)
33150:of avat vs. Baoidebs, cf. Wackernagel, op. cit. 209 ff.), possibly : Skt. van- ‘win, gain’, etc. (Schwyzer, Glotta 6.86), but more prob. of pre-Greek origin. Cuny, Rev. ét. anc. 16.297. Debrunner in Ebert, Reallex. 4.2.527. Smieszek, Eos 31.547 ff.
```


## [2026-09-05T14:41:50.651Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '28110,28180p' SYN.txt"
}
```


### [2026-09-05T14:41:50.699Z] TOOL RESULT

```
16.28 DEAR Grk. gles Goth. liufs Lith.  mielas NG &yamnrés (pos) ON ljafr, kerr Lett. mil’ Lat. cdrus Dan. kar, elsket ChSl.  viizljublenii, Ljubi It. caro Sw. kar, alskad SCr. mio, drag Fr. cher OE léof, déore Boh. drahy, mily Sp. caro ME _sleve, dére Pol. luby, mity Rum. drag NE dear Russ. mil, dorog Ir. dil, coim, inmain Du. lief Skt. priya- NIr. — dilis, ionmhain OHG  liob Av. — frya-, frida- W. annwyl, cu, hoff MHG liep Br. _ ker, kaez NHG lieb, tener
The majority of words for ‘dear’ Se ‘beloved’) are connected with words for ‘love’ and have been included in the dis- cussion of the latter (16.26). The others, including some in which the earlier sense was ‘dear’ = ‘valuable, ex- pensive’ (11.88), are:
Ir. dil, etym. dub., perh. *dwe-li- :
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
*dwe-no- in Lat. bonus, OLat. duenos ‘good’. Vendryes, Miscell. K. Meyer, . 289. < Ir. céim (also ‘handsome, fine’), W. cu, MBr. cuff (NBr. kunv ‘gentle, Be fable’) : Lett. saime ‘family’, OB a OHG heim, ‘home’, etc. Walder. 1.259. Pedersen 1.58.
maniin Nir. jonmhain, perh. y lem fr. the root of menme igi Macbain 218. ee ‘nia dilis, also ‘faithful’, orig. ones ee this sense Olr. diless (cf. W. eae Ptr) epd. of neg. di- and -less ays * , W. llys-fab ‘stepson’ : Ir.
Wy, annwyl, etym.? Morris Jones 160
(but??).
Br. ker, MBr. quer, of Fr. cher. Henry 63. | Br, kaez (MBr. quaez ‘captive, un-
fr. a Norman form
fortunate’) ‘unfortunate, miserable’, Grk,  iAtw, Kuvew Goth. kukjan gid ON kyssa dsculari, savidri, ba- Dan. kysse sidre Sw. kyssa .  baciare OE cyssan .  embrasser, baiser ME kisse .  besar NE kiss Rum. sdruta Du. kussen »  pocaim OHG  kussen Nir, pogaim MHG_kiissen “ cusanie NHG kissen ' _pokat
Kissing, as an expression of affection or love, is unknown among many races, and in the history of mankind seems to - : later substitute for the more primi- i ERE of noses, sniffing, and lick- Zs na © partial agreement among words ele ae m some of the IE languages syllables. on Some common expressive # Lie pe 1S NO conclusive evidence mas late = aes Hnown in IE times. It Debably rea ndia, pad a Slavic group der, Reale ects the ‘lick’ kiss. Schra- Snifr. oe x S.v, Kuss. Hopkins, The B19 an Ancient India, JAOS Orient, Ber, Pal Der Kuss im alten 8s. Akad. 1934. 914 ff.
Digitized by Arya Samaj Foundation Chennai and eGangotri
; TEMPERAMENTAL, MORAL, AESTHETIC NOTIONS 1113
whence by affectionate commiseration ‘dear’ : W. caeth, Ir. cacht ‘slave’, Lat. captus ‘captive’, etc. Henry 57.
OE déore, ME dére, NE dear, also ‘precious, expensive’ (cf. 11.88) in OF and ME often ‘glorious, noble’ : ON dyrr ‘precious, noble’, OHG tiure ‘glori- ous, excellent, valuable’, NHG teuer ‘dear’ (in both senses), outside connec- tion dub. Falk-Torp 172. Weigand-H. 2.1040 fi.
SCr., Bulg. drag (> Rum. drag), Boh. drahy, Russ. dorog, also ‘precious, valu- able’, Pol. drogi, ChSl. drag only in the latter sense (cf. also Lett. dargs id., prob. loanword), etym.? Berneker 213.
16.29 KISS (vb.)
Lith. buéiuoti
Lett.  butuot, skipstit ChSl.  lobiizati, célovati SCr. Ujubitt, cjelivatz Boh.  Libatt (celovatz)
Pol. calowaé
Russ. celovat’
Skt. (cumb-)
Av. :
A distinction between the kiss of affec- tion and that of erotic love is sometimes made as in Latin (cf. Sciendum osculum religionis, savium voluptatis; quamvis quidam osculum filiis dari, uxori basium, scorto savium dicant, Serv. ad Verg.), but even here is not maintained and in general is ignored.
Several of the words for ‘kiss’, as already stated, are of imitative origin. One is from a ‘little mouth’. Some come, through church influence, from the kiss of ‘peace’ or ‘greeting’. In some the feeling of ‘love’ is the antecedent of its expression as ‘kiss’.
1. Derivs. of an expressive syllable ku
CC-O0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
1114 SELECTED INDO-EUROPEAN SYNONYMS
or kus (cf. the more obviously imitative bu, bus, below, 2). Gme. forms resisting the consonant shift by reason of the ex- pressive character, or influenced by the group Goth. kiusan, Grk. yebw etc. ‘try, taste’, or fr. a parallel gu, gus? Walde- P. 1.465. Feist 315.
Grk. xvvéw (aor. Hom. évoca, mostly poet., in prose replaced early by ¢.déw); Goth. kukjan, OF ris. kiikken; ON kyssa, OE cyssan (> W. sb. cusan, vb. cusanu), OHG kussen, etc. with sbs. ON koss, OE coss, OHG kus, etc.; Skt. cumb- (late, cf. below, 9); Hitt. kuwass- (Benveniste, MSL 33.189).
2. Derivs. of an imitative bu, bus, in words for ‘kiss’ and ‘lip’ or ‘mouth’. Widespread group not confined to IE languages, but mostly dial. or colloq. words not included in the list. Walde- P. 2.113f. Berneker 104. Miihl.- Endz. 1.344 f.
NE buss (sb. and vb.), NHG sb. buss, vb. bussen, Sp. buz (‘kiss of respect’, fr. Arab.), Pol. buzia, buziak; cf. Ir. bus, Alb. buzé, Rum. buzd ‘lip’. Here as regu- lar verbs for ‘kiss’ Lith. budiuoti, Lett. buéuot, beside Lith. bué an imitative ex- clamation inviting a kiss (NSB s.v.), perh. fr. NHG dial. forms like butschen and (Swiss) buésch ‘a kiss’.
Other collog. words of imitative orig., e.g. NE smack (with its Gmc. parallels); Rum. pupa (childish or derogatory) : It. poppa ‘breast’, poppare ‘suck’, etc. (Pusgariu 1403); Lett. skipstit, beside éupstit ‘suck’ (Miihl.-Endz. 3.908).
3. Grk. ¢iAéw ‘love’ (16.27), hence also ��show signs of love, kiss’ (Hdt.+-), with sb. $fAjya ‘a kiss’ (Aesch.+), NG pop. ¢:AG only ‘kiss’, sbs. g:Xé (fr. infin. gireiy), pidnua. Cf. Corn. a(m)me, MBr. affet ‘kiss’, prob. fr. Lat. amare ‘love’ (Henry 5; not in Loth, Mots lat.).
4. Lat. dsculdrz, fr. dsculum ‘a kiss’,
lit. ‘little mouth’, fr. ds ‘mouth’,
nout-M. 715. Ep Lat. sdviari, chiefly anteclass,, fy sdvium ‘a kiss’ (esp. in the erotic sites
as contrasted with Osculum), prob. by dissim. fr. *sudvium : sudvis ‘sweoy) ee 898. Kretschmer, Glotta
Lat. basidre (> It. baciare, Fr, batser Sp. besar), fr. basium (Catull.+) oe used like sdviwm, but eventually qi placing it and dsculum, source dub. (loanword fr. Celtic?), Ernout-M. 105. Walde-H. 1.97f. REW 971. Wart. burg 2.268 ff.
Fr. embrasser, fr. bras ‘arm’, orig. ‘take in the arms, embrace’, but also ‘kiss’ since 17th cent., and now replacing baiser in this sense (except with added lévres or the like, or as a noun; donner un baiser, etc.) owing to the obscene conno- tation which baiser has taken. REW 1256. Wartburg 2.268 ff. Bloch 1.61, 99.
Rum. sdruta, fr. Lat. salitare ‘greet’. Perh. semantic borrowing fr. Slavic (cf. ChSl. célovati, etc., below, 8), but not necessarily. Cf. OSp. saludar also ‘kiss’, and so formerly sometimes NE salute (NED s.v. 2, e). REW 7556. Tiktin 1369.
5. Ir. pocaim, NIr. pogaim, Br. pokat, fr. Ir. poc, Br. pok ‘a kiss’, fr. Lat. paz ‘peace’ in church uses like pacis dsculum dare, etc. Wendryes, De hib. voc. 167. Loth, Mots lat. 197. Pedersen 1.24, 202.
W. cusanu, above, 1.
.6. Gme. words, above, 1.
7. Lith. budiuoli, Lett.  buduol, above, 2. A, 7
8. ChSl. lobiizati (reg. for ‘kiss 7 Gospels), Russ. lobzat’ (obs. or archaic); SCr. dial. lobzat, lozbat, prob. ae lambere, OHG laffan ‘lick’, OF ee Jap up’ ete. Walde-P. 2.384. Bem ker 726 f.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
guorl0 ie
slovati ‘greet’ (cf. eae sound, ch oe at salatare fr. salus health’), well ike iiss’ (Supr. once, and later) i ‘elivatt, Boh. celovati, Pol. E Y ue celovat’. Berneker 123 f. ae piti ‘love’ and ‘kiss’ (like Grk. Ce Iibati ‘kiss’ (polibek ‘a kiss’) : a ? (16.27). Berneker
Digitized by Arya Samaj Foundation Chennai and eGangotri
N; T{EMPERAMENTAL, MORAL, AESTHETIC NOTIONS 1115
In Vedic, affection is expressed by ghra- ‘smell, sniff? (15.21), lih- ‘lick’ (4.59), and nizs- ‘approach, touch, em- brace, greet’ (ni-ns-, redupl. form of nas- ‘approach, join’, esp. in love : Grk. véo- pac ‘come back, return’, Goth. ganisan ‘be saved’, etc.; Walde-P. 2.334f.). These are often translated ‘kiss’, but only loosely. The true ‘kiss’ is some- times expressed, earlier than by cumb-,
9, Skt. cumb- (above, ly late occurrence.
ddyos, d5ivn, 740nHA, Goth. etc. ON xbvos, Bacave. Dan. . dolor Sw. _ dolore, sofferenza OE .  douleur, souffrance . dolor, padecimiento ME Rum. durere, suferin(d ’ imned, céssad NE pian, fulang Du. poen, dioddef OHG poan, gloaz MHG NHG
1) is of relative-
kins, l.c.
16.31 PAIN, SUFFERING
as ‘set mouth to mouth’.
Cf. Hop-
sair, winnd, balweins Lith. skausmas, kentéjimas, verkr, sdrsauki kantia smerte, lidelse Lett. sdpes, cieSana smdrta, lidande ChSl.  boléznt, strastt sar, @ce, warc, pro- SCr. bol, patnja wung Boh. _ bolest, utrpent sor, peine, suffrynge, Pol. bél, bolesé, cierpiente smerte Russ. bol’, stradanie pain, suffering Skt.  duhkha-, pida-, pijn, smart, lijden vedana- smerza, sér, pina Av. axti-, sadra; intt-, Gri-
smerze, sér, liden, pin(e)
schmerz, leiden, pein, qual
‘Pain, suffering’ is understood here as primarily physical, though most of the words may be used also for mental suf- fering, for which see also ‘grief, sorrow’ (16.32), NE pain is mostly, though not *clusively, physical, while conversely " peine is mostly mental. ie of the words for ‘emotion’ or e he are also used more specifically Dean as Grk. maGos, raOnua (not oo ve or had the latter sense a y (cf. 16.12, 16.13). Vibe for e pe rods belong with the Metialization oe may show more tfer ‘ufo. oe e latter. Thus NE low (though ces and also ‘endure, al- in the aay Semel but suffering OF ‘Suffer? ca ‘ zed Sense. The verbs uded in the discussion,
either here or in 16.12, 16.18. Several of these (but not all, by any means) cover also ‘bear, endure’, which in some is the primary sense. Some are connect- ed with words for ‘hard work, toil’.
1. Grk. adyos, etym. dub. Walde-P. 2.423 (rejected in Walde-H. 1.352).
Grk. é3ivn, most frequently in pl. ‘pains’, etym. dub. Walde-P. 1.768. Boisacq 685.
NG zrévos (with vb. zové ‘suffer’), in class. Grk. ‘hard work, toil’ (9.12).
NG Bacavo ‘torment, torture’, but pop. also ‘pain’ (esp. pl. ra Bacava), fr. Grk. Bacavos ‘touchstone’, whence ‘test, trial’, and ‘inquiry by torture’ of slaves, etc., and (NT) ‘torment, torture’, prob. loanword. Boisacq 115.
2. Lat. dolor (> It. dolore, Fr. douleur,
```


## [2026-09-05T14:42:10.581Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== HRN bosidan ==\"; grep -n -i \"bosid\\|bôsîd\\|büsîdan\\|busid\\|bos\\b\" HRN.txt | head -20; echo \"== HUB ==\"; grep -n -i \"bosid\\|busid\" HUB.txt | head -10; echo \"== CHEUNG bau ==\"; grep -n -i \"bōsīdan\\|bosidan\\|busidan\" CHEUNG.txt | head -10"
}
```


### [2026-09-05T14:42:10.655Z] TOOL RESULT

```
== HRN bosidan ==
2400:233. huden 'sein, Praes. buv-em'^ vergl. bos-em, bad; buvis, 0Ou)
8141:art: Bos Gaurus* (Spiegel, Ar. Periode 55); phlv. gör
== HUB ==
== CHEUNG bau ==
19921:(inch.) ‘to rot’, Kurd. (Kurm.) püc ‘rotten; useless’ || (+ *ham-) NP anbusidan/ 
40849:bosidan/bos-, 15
```


## [2026-09-05T14:42:12.054Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== BRT magna ==\"; grep -n \"mayna\\|magna\\|maγna\\|maɣna\" BRT.txt | head -20; echo \"== PHD brahnag ==\"; grep -n -i \"brahnag\\|brahnak\\|brahn\" PHD.txt PHD_mackenzie.txt | head -20; echo \"== NYB ==\"; grep -n -i \"brahnag\\|brahnak\" NYB_vol2_glossary.txt | head -10"
}
```


### [2026-09-05T14:42:12.134Z] TOOL RESULT

```
== BRT magna ==
4290:•  j.  an-aiwLvastra-  Adj.  'unbekleidet':! <Äa  nara  . .  mayna  . .  'ra  (ND.)  V.  Ä  10.
19550:Ableit.  aus  mayna-,  auffill,  Bildung;  vgl  HoRW GIrPh.  I  b.  146.  —  Pü.:  TÜSlai.  —  ')  Wo das  Wort  ganz  entstellt  isL
== PHD brahnag ==
PHD.txt:278:brahnag [b/(?)hnk' | M brhng, N barahna] naked.
PHD.txt:2885:naked brahnag.
PHD_mackenzie.txt:1615:brahnag [bW)hnk' 1M brhng, N bara/ma] naked.
PHD_mackenzie.txt:7124:month miih, mahigiin.                          naked brahnag.
PHD_mackenzie.txt:11094:brahnag                  \~~)      burd
PHD_mackenzie.txt:11098:brahnag                  \~~.-l    bum                             -6\)
== NYB ==
```


## [2026-09-05T14:42:15.398Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '19530,19570p' BRT.txt"
}
```


### [2026-09-05T14:42:15.447Z] TOOL RESULT

```
•  j.  'ma]^-  n.  Name  des  die  'neun Löcher"  enthaltenden  Reinigungsraumes*': pascaita  ava  tä  niikioöii  .  .  *anfarym arioim  'yahe  *pänntarem  haca  anyaHlyS mayaäbyö  "drauf  soll  (er)  ,  .  sich  zu denen  auf  die  andre  Seite  des  Reini- gungsraumes setzen,  die  von  den  andern
dby  Google
IUI  iraaja.-
(zuvor  bezeichneten   sechs)  Löchern  ge- sondert ist"  V.p.29''.
*)  Ein  nach  aussen  durch  dcei  parallele  Furcb- itriche  abgegrenztes  Rechteck  auf  dem  Bodeo, Von  6  zu  16  Schritt,  auf  der  langen  Mittellinie drei  Löcher  mit  Wasser  und  sechs  mit  Rinder- bam  enthaltend.  Der  Raum  ist  zunächst  in iwei  wieder  mit  je  drei  Furchstrichen  umzogene Abteilungen  getchiedeo,  eine  kleinere  mit  den Wasser-  und  eine  grössere  mit  den  Hamlöchern. In  der  letitem  Abteilung  ist  abermals  durch drei  Furcbstiiche  an  der  den  Wasserlöchern abgekehrten  Seite  eine  Unterabteilung  mit  drei Löchern  geschaffen.  Die  Furch  st  riebe  werden  zu je  dreien  gezogen  der  Reibe  nach  l)um  die  Unter' abteilung,  3)  um  die  grössere  Abteilung,  3]  um beide  Abteilungen,  4}  um  die  kleinere  Abteilung ; Tgl.  zu  antariiür.  Dann  werden  an  bestimmten Stellen  des  Raums  Steine  od.  dgl.  niedergelegt. Vgl.Sp.  10450.  und  dieZeichnungenbeiWESTSBE. /1J.43S  und  DsT.ZA.2.  l6z  (dessen  Erliulerungen aber  nicht  stimmen).  Abweichend  Sp.  Übers,  i, Tafel  Zur  Reinigungszeremonie  s.West  aO.431. Ableit.  aut  'BiaYo-(mit  Verschiebung  des  Wort- akzents?]!),  etwa  'Raum  mit  den  Lochern'. — Pü. :  msej.  —  ■)  D.  i.  er  soll  von  der  grossem Abteilung  (PüErL  pa  gömH)  in  die  kleinere gehen.  —  *)  Ob  etwa  miy"  zu  lesen?
•  p.  magav-  {:  j.  moyu-)  Adj.,  bezeichnet einen  medischen  Volksstamm,  fdr  den  die Priesterwürde  vorbehalten  war,  'magisch, Magier'*';  /  martiy^  'gu!  äht^  gaumSt<^ nätnii'  Bh./.ii;  13%  14^,  ^.2,  b;  —  gau- matam  tyam  'gum  Bh./.ijJ,  16,^18.
■>  LitteraluT  bei  Jn.  Zor.  ö. KompA.  (s,  miypi'\  —  Et?  Die  Herkunft  des Worts  aas  dem  Assjmschen  (ZDMG.5J'.  16S} wird  vunNÖLDEKE  (Brief  oj.  06. 03}undBez0LD (BriefoS.  06. 03)  bestritten.  —  mp.  maiüi,  np.
•  j.  Taa.ja.wa.-  Adj.  'unverheiratef:  näiri- vaite  . .  ahntäl  pourum  framraomi  .  .ya%a 'vs  fraväxsöit  "dem  beweibten  spreche  ich den  Vorrang  zu  vor  dem,  dass  einer  unver- heiratet altem  sollte"  V,  4. 47.
Ableit.  aus  *maTav-  m.  'cselebs'.  —  VgL  got. magus  'Knabe',  maga^s  'Jungfrau'  [usw.,  FiCK Wb.4  3.  198).  —  Fü.:  i  öi  i  läiriilmand  . . hal  i  i  pti  ..fräl  gdwim  . .  Hgön  Ufa  marfih fräl  raft  islel;  dazu  die  ErL:  in  tan  ntsl  'd.  i.; er  hat  kein  Weib*.
•  g.  maga'van-  Adj.  'der  zum  'Bund', zur  zardSsustr&^OR'o.  ReligionsgemeinschaÜ gehört,  Sündler':  hyat  tmzd>m  iarai:mirB •vabyB  Mst  para  "was  Zar.  den  Bündlern als  Lohn  in  Aussicht  gestellt  hat"  Y.5/.  15;  1 —  yä  srvye  pari  {iAi)  *'gaonO'1  Y.^.  7. 1
**matay-  iiia
Pü.  (zu  Y.jt):  fia  pmtm  iHo-pi,  oA.:  fa  oft- lak  vihih;  (zu  Y.  5/):   f  m  dn  n  dan  n  (^pü.: mimtvätil,  ob  ma-^kSni  —  ')  NA.  'gSutä;  s. auch  V.  //.  7. j.  maj'na-  Adj.   (fem.  *«J-)   i)  "nackt,
°Ha{ND.)  anaiv/i.- 'BS  apajpayai  vasfrä t  *tanBni  N.55"';  — oss,  lauter*:  'nS  Bia'^rä
I.  täjnäg,  gr. -    I)  Einmal
entblösst':  dva  t vasfra  V.S.io;  — Yt.j9.s6;  —  •«?« 'na  F.  II.         a)*bl N.2«
Ableit.   —  Vgl.  i
yvfiMc  (von  denen  jedei  ant  emi
laut  weist].     —    Pü.:  briknak.
mayari'.  —  »)  Text:  afasläk  ngö
•  j.  ma}^3nta-  Adj.  'nackt,  entblösst*: vari>ian/(as(sd.yit  'tasat  P.  //,  ■*!*.  tOf)  '*.
Ableit.  aus  mayna-,  auffill,  Bildung;  vgl  HoRW GIrPh.  I  b.  146.  —  Pü.:  TÜSlai.  —  ')  Wo das  Wort  ganz  entstellt  isL
•  j.  maxäl-  f.  'Fliege':  druxs  yä  nasus  .. nivSiryete  mqnaym  ahe  >fl5a  'syä  par^mm (sd.)  M.8.6'9;  23  PüZ.;  —  basvan 'sinam »rrfaitinatn  ava.Janyät  V.  14.  f>;  —  °H F.  II.       '[V.7.2  lies:' maxä.i^Är^a.].
KompA.  —  mp.  (Pü.)  maxi,  kurd,  mil,  aif. mal;  vgl.  ai.  mditiiä-  f.  'Biene',  np.  magas.
•  j.  *niaxäi.V«hrp-"  f  'Fliegengestalt':  a^a druxs  ya  nasus  upa.dvqtaiti  .  .  'kihrpa srr^aitya  V.  7.  %.
Pü.:  pa  maxi  karf.  —  ■)  NA.  trennt.
•  j.  maxäi.b3r«ta-  Adj.  'von  Riegen  ver- tragen, fortgeschleppt':  '0  nasu/  Y.S-i; j.  14  PüZ.;  —  aite  nasävö  ya  .  .  'taca nasui  V.  5. 4,
Pü. :  max!  buri.
•  j.  maxätay-  m.  EN.  eines  Gläubigen: sps.pt&ü  °Uis  alaonB  "des  Sp.,  Sohns  des M.  . ."  Yt  13.  116;  —  payanharo  'ieis aiaons  Yt.  13. 116.
Eig.  Bed.?
•  p.  maäya-  Adj.,  bezeichnet  ein  Volk'*: ima  dahySvJ'  fyä  adam  agarbäyam  , .  'yS (NPm.)  D.ff.3;  —  iyam  (sd.)  'ya  D./o(?).
')    liERODOT  4.  I9I;   ^ffi{iu(;   vgl.  JUSTI  GlrPh.
3.  455,  EMevek  GeichdA.  /,  281.
•  j.  C,  g.)  mata-  Adj.,  PPfP. :  s.  'mu;/-.  [P. 25:  lies  humata^
KompE.
•  j.  'matay-  f.  'Denken*.  [P,  25:  lies ar?m.maiti;  —  ^.41:  lies  /arS.maiii.]
KompE.  —  Zum  V.  'man;  —  ai.  matäy'  t
•  j.  »■''matay-''  m.  'Vorspning  (des  Gebirgs), promunturium':  aofistimca  ..  masdayama vaS)ySJ>m?jnia  upa  maillm ''  iantaahqin pqsl&./ra%anhfm  (sd.)  hl  kamir^tm  vlnä-
dby  Google
»113
hay?n  *'. .  sollen  die  M.  auf  einem  Vor- sprung des  Gebirgs'*  ihm  den  Kopf schinden  . ."  V.j.io.
Zam  V.  3man:  —  lat.  vgl.  monl-isil
```


## [2026-09-05T14:42:16.651Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i \"bauš\\|\\*bauc\\|bōs-\\|bos-\\b\" CHEUNG.txt | head -20; echo ===; sed -n '19900,19935p' CHEUNG.txt"
}
```


### [2026-09-05T14:42:16.703Z] TOOL RESULT

```
Exit code 1
(eval):1: == not found
```


## [2026-09-05T14:42:39.916Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i \"bosidan\\|bōsīdan\" CHEUNG.txt | head -20; echo \"---- page15 area ----\"; grep -n \"1\\. \\*bau\" CHEUNG.txt | head"
}
```


### [2026-09-05T14:42:39.977Z] TOOL RESULT

```
40849:bosidan/bos-, 15 
---- page15 area ----
```


## [2026-09-05T14:42:40.335Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"-- DKS bunai --\"; grep -n -i \"bunai\\|buṇai\\|bunaa\\|naked\" ISS_alt_DKS.txt | head -30"
}
```


### [2026-09-05T14:42:40.402Z] TOOL RESULT

```
-- DKS bunai --
4103:pammastä ‘seized, held’, 11 4574. tta và hir-oi nārä pūra na pammastä yudá(mdd) buna và ava 'they could not at all hold wives, sons; they came here naked' (translation SDTV 111); JS 24v1 pura pemesti aysgam rraijsai рина ' the vulture seized the young ones with its sharp beak’; u 98:153 khu тайа ttu auska pada pemaistai na Jsa utca garausta ' how now he has followed the way to that abode (death?); but water has not drowned him'. From pari- marz- (see s.v. malys-) with -malsta-, -masta-, -mesta- < *түйа-.
4429:pašara- 'sun's heat, sunshine’, K 15017 Б byajárá tta tta khua pàjira baurá ' melt (2 plur.) all just às the sun's heat the snow’; Z 2:172 ysande samu kho ggarä ysarnai viidá ratanyo pasáru viri 'is beautiful just like the golden mountain covered with jewels in the sunshine’; Z 20:36 сӣ bile tcabriye pasáre jsa stauru paha ‘whose intestines are scattered, greatly rotted by the sunshine’, Z 22:254 gari rrustà pásáru vīrä ‘the mountain shines in the sun- shine’; Z 549 uysdemáte #šandau nastaudo ce pasáre jsa nütauda 'cools the heated ground which was burnt up by the sun's heat'; Z 5:80 tidná cu tterd pracai nátà kho Ju pásará stanye chaya ‘because such a cause (BS pratya- уа-) does not exist, just as shadow in sunshine’, =Manj. 237 ttaue си va prracai naista khu patera stanye сЩа)уа; Manj. 239 khu pafara bunai па asta ne và tte chayr bide
5476:bünaa- ‘naked’, SuvP. 71v3 (plur.) byelide büna vasta ће naked get clothes’, BS nagnài ca vastrāņi labliante, Z 2:13 bünai jsāte ‘he goes about naked’, п 44-56 būnai та sti ‘he is here naked’; п 4575 būnā và āva ' they came here naked’; 1t 98:16: bünà hvamdą 'naked men'. From *bagna-, Oss, DI. báyndg, D. báyan-vad І. báydm-vad 'bare-footed', D. báyén-sar, І. báydm-sar ‘bare-headed’, D. ron-báyd ' without girdle (-d < -n or possibly participle to base bag-), Sogd. Bud. Byn'k, Chr. булу, Chorasm. ВупуЁ Av. mayna-, Zor.P. brahnak, N.Pers. barahnah; Wanetsi йл. IE Pok. 769 nog"-, O.Ind. magnd-, Got. nagaps, Lit. nýogas, O.Slav. пай,
5477:bunai ‘darkness’, Manj. 239 khu pásara bunai na asta ne và tie сһауг bide 'as in sunshine, there is по darkness, nor is a shadow found’. From bau-:bu- ‘to shine’ beside bä- (as Greek pau- beside palve, O.Ind. ёлат-, vibhdva- ‘shining’ (adjective) beside #ha-; see IE Pok. 104-5), hence 'shining dimly'z'shadow! as O.Ind. chaya 'shining' and 'shadow', Av. saya-, see cognates s.v. Sühauja ' umbrella'. Note the parallel passage Manj. 237 khu pasera stanye chaya ‘as shadow being in sunshine’. Instead of base bu- *bunaka-, less acceptable would be *bünaka > *bünaa- with -ün- < -ün-. j
7006:yasta 'dress', SuvP. 71v3 byehide büna ойна 'the naked get clothes’, BS nagnàs ca vastrāni labhantu; 11 10515 pamye sara vàsta prrahauna ' he wore fine dress (dyadic)'; H 118:151 éreusta 'white-clad'; K. 6378v3 jastüüam vüstyüm sara їйзїа prrahauna ‘dress well-tailored from celestial clothes; Manj. 424 jastuña vàsta prraihána; Bed 45r4 vastyau hamisa 'with clothes’, BS vastra-. From base vali-, vas- (before £-) ‘to wear'; vasta- < *vastu- or vasta- with long -à- before two consonants (as kärra- ‘deaf’ < *harna-), to Av. vaste, vauhaiti, vastra-, *valiana- in Buyni win 'dress', Rosáni wn, as second component safēd-wēn ' with white clothes’, and Iska&mi wanjī ‘cloak’. IE Pok. 1172 ues-, O.Ind. vdste, vdsana-, vdstra-, Armen z-gest, Greek Evvutu, Lat. uestis, Got. wasjam, O.Engl. werian, Hittite uas-, ueš-, 'lTokhara B wastsī 'to dress’, А. wsāl,
7372:bare-foot one, he has no pain’. To 'bare-footed', note Baloéi iafad, азад, Brahüi lw fapüd, Waxi рид, from *fia- 'naked, bare', to IE Pok. 163 bhes-:bhs-, bhoso-, OHG Bar (*baza-), O.Engl. bær ‘bare’, Lit. bàsas, O.Slav. bosii 'bare-footed!, Armen. bok (*bhoso-go-), Greek y- in wiAés ‘bare’ to bhes- ‘rub off'. Note also Balóct pa, P'dipaà 'bare-footed' (from *fi-» *fai- > p'ai-, p'as-).
8483:haspünaka ‘striving’, 11 32:97 ttena гапат haspünaka küste dyāda hoasta hve "therefore where the strivers among the fighters saw (the truth), the chief one spoke’. From *fra-spigna-&ka to *fra-spugna- base spaik- or spaig- ‘to exert oneself’ (see haspij-, haspata) with -gna- as in paphünva- (-bugna-) vastünvü (-stagna-?) and bünaa- ' naked’ (*bagna-ka-), beside rrima- ‘oil’ < *raugna-.
8505:hümná- 'eyelash', Sid. r49r3 Аата rrühd kare bisa jindä "it cures all pain around the eyelashes’ (om. Tib.); nt 81:173 Лале gloss to Turkish kīräpīkä (kirpik) ' eye- lash'; E p. 357B khu ji häni kürca vatcai "like the eye- lashes, eyebrows, hair on cheek’ (see KT vi 442); ш 93:266 tcimeña }аїйй и haune streha hamüre ‘eyes are affected and the eyelashes become stiff’, The ‘eyelashes’ are named from base maik-, maig- ‘close the eyes', in N.Pers. mad, midah, mišapan, mušagān, Paraéi тшй, Вабёт miza, mišāš, hence here hamnü- (plural, Лапе, hañi, haune) can be traced to "z-migna- with loss of vowel of the base -müg- possibly through -mug- (as pamjs- ‘to wear clothes! from *patimuč-, participle památa-), where hā- could also derive from frà-:*frà- mignā- or *ü-mignü; -gn- resulted in -n- in būnaa- (*bagna-ka-) 'naked', see also Jaspūnaka- ‘strenuous’, and zrüna- ' oil! (*raugna-).
8508:hāma- 'raw, unbaked, uncooked’, Sid. 17v5 ttrehe tte häma stüna ‘raw. radishes', BS mülaka-, Tib. la-phug rjen-pa; Z 2068 hamá padānä ‘unbaked pot’, parallel BS ama-pütra-, āma-kumbha-, üma-bhajana- Pali amem pattam va; Sid. 122v2. lauma, Tib. rfen-pa; тп 18:29 huma büva ‘там root’. See also Айта? '(naked) barley’. From base ат-, *üma- 'raw', Pašto бт, Sogd. Bud. yu kw, N.Pers. xüm, Отт. хатё, Parāčī utm, Yidya хіт, Waxi ying, Oss. DI. хот (not attested in O.Persian, or Avestan). IE Pok. 777-8 om- ‘raw, bitter, sour’, O.Ind. amld-, ambld-, 'sour, sorrel’; amrd- ‘mango’, äma- ‘там’. See s.v. hamga- ‘sour’.
8513:hamai 'barley flour’, Sid. rs2ri Aümar, Tib, pag-zan 'barley meal’; ип 87:118 hamai hā vamathauñä 'the barley-flour must be stirred’; rr 85:67 ada hümat ' flour barley’; v 211393 hāmai tsue kū(sa} ‘bare barley, ground, kūsa-measures (number lost)’; ibid. tsue hämai kha 'ground barley, kha-measures (number lost)? with tsuta- ‘ground’ to corroborate the use of hāmai ' barley flour’. Here tsuta- for suta- ‘rubbed ground’, see cognates s.v. soy- ‘to grind’, with preverb t- as in Av. ikadía- ‘teaching’: Sogd. Bud. tAwi- ‘observe’. 11 71:7 и doüsd kūsa và hümai hajsemyari “апі get together twelve küsa-measures of barley-flour', Adjective, hami- паа-, Sid. gr3 hamina, Tib. phag-phye 'barley-four', BS saskuli- (variant sag-), =saskuli, -1, daskuli, -i ("large round cake of rice, sugar, sesame-seed cooked іп oil’). From hama- ‘raw’, Tib. rjen-pa, adjective hamaa- for ' (naked) barley’, Waxi уйл] ‘flour’ (*àümaci-). Hence not with Aamatei.
```


## [2026-09-05T14:42:58.416Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"-- HRN --\"; grep -n -i \"barahna\\|brahnak\\|bähnä\\|nackt\" HRN.txt | head -20; echo \"-- HUB --\"; grep -n -i \"barahna\\|brahnak\\|nackt\" HUB.txt | head -20; echo \"-- SOD --\"; grep -n -i \"βγn\\|bgn\\|Byn'k\\|naked\" SOD.txt | head -20"
}
```


### [2026-09-05T14:42:58.513Z] TOOL RESULT

```
-- HRN --
9958:teilung auch np. kurd. rut nackt, leer', das im Np.
-- HUB --
159:Phi. lutaJc wird (Gl. and Ind. p. 139) durch nackt* iiber-
-- SOD --
24680:naked 
24708:naked 
91953:naked    2576, 2580
```


## [2026-09-05T14:43:01.004Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '24670,24715p' SOD.txt; echo \"-- entries 2576/2580 --\"; grep -n \"^2576\\|^2580\\| 2576 \\| 2580 \" SOD.txt | head"
}
```


### [2026-09-05T14:43:01.076Z] TOOL RESULT

```
temple 

GMS  165,  509,  1183;  BBB;  Hen.  Tales.  473,  42; 
C2,  25R23,  25V  n  p62;  Sund.  AI  28,  1988,  180 

2576  pynJk    B  c^Jm^, 
Payne   ©*bagna-ka~y  Khwar.  ^/w'jk;  Oss. 

bdxndg    =*byny 
naked 
SCE  385;  Prolexis.  256 

2577  pynpt'nch    B  o*lT<oj  JV=r 
Payn-patanc 

sorceress 

SCE  250,  252 

2578  pynpt(w)   B,  S  (oU-^jaIT  «/^U 
payn-pat(u) 

sorcerer,  priest 

Anc.  Lett.  1.10;  SCE  255;  Hen.  BSOAS  28.250; 
MDii  pl70.5 

2579  pynwy(y)   M  (>^-^)>*U 
Pay-nawe   ©abl.  -nw)   =^pyynwy(y) 

new  moon 

GMS  1964;  BBB;  Gersh.  Sogd.  Cpds.  138  n  2,  146 

2580  byny   C  <ca^ 
Payne   (Pyny)  ©pi.  -t   =»Pyn'k 

naked 

Sogdica.  39.22;  STi  27.12,  18;  Sund.  AI  28,  1988, 
180 

2581  pyny    M  **  byny 

2582  pyp>wr    B,  M,  S  j/>p)j>u9  ^IjIji^  ««jljAli 
-- entries 2576/2580 --
24676:2576  pynJk    B  c^Jm^, 
24705:2580  byny   C  <ca^ 
91953:naked    2576, 2580
```


## [2026-09-05T14:43:11.335Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"^balsam\\|^balm\\|^embalm\\|^balsamine\\|balsamon\\|bāsām\\|besem\\|bosem\" KLN_1966.txt | head -20"
}
```


### [2026-09-05T14:43:11.389Z] TOOL RESULT

```
4305:balm
4820:beslaver,  tr.  v.  —  Formed  fr.  pref.  be-  and  slaver, besmear,  tr.  v.  —  Formed  fr.  pref.  be-  and  smear, besmirch,  tr.  v.  —  Formed  fr.  pref.  be-  and  smirch, besom,  n.  —  ME.  besum,  fr.  OE.  besma,  besema, rel.  to  OS.  besmo,  OFris.  besma,  MDu.  besem, bessem,  Du.  bezem,  OHG.  besmo,  besamo,  MHG. besme,  besem,  besen,  G.  Besen.  The  original meaning  is  ‘something  bound  or  twisted’,  fr. I.-E.  base  *bheidh-,  ‘to  bind,  twist’.  See  fisc. Derivatives :  besom,  tr.  v.,  besom-er,  n. besot,  tr.  v.,  to  make  sottish.  —  Formed  fr.  be- and  sot.
12915:embalm,  tr.  v.  —  OF.  (=  F.)  embaumer,  fr.  em-, en-,  ‘in’,  and  baiime,  ‘balm’.  See  em-  and  balm. Derivatives:  embalm-er,  n.,  embalm-ment,  n. embank,  tr.  v.  —  Formed  fr.  em-  and  bank,  ‘edge of  a  river’.
```


## [2026-09-05T14:43:13.536Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '4295,4320p' KLN_1966.txt"
}
```


### [2026-09-05T14:43:13.592Z] TOOL RESULT

```
Bairam,  n.,  the  name  of  two  Mohammedan  fes¬ tivals  following  the  fast  of  Ramadan.  — Turk. bairam.
bairn,  n.  (Scot.)  —  OE.  beam,  barn,  child’,  rel. to  bear,  ‘to  carry’  (q.v.)
Derivative:  bairn-ish,  adj. bait,  tr.  v.  —  ME.  baiten,  beyten,  fr.  ON.  be  it  a, ‘to  cause  to  bite’,  causative  of  bita,  ‘to  bite’ ;  rel. to  bxtan,  ‘to  bait’,  OS.  betian,  OHG.  beizzen, ‘to  bait’.  MHG.  beitzen,  ‘to  bait;  to  hawk’,  G. beizen,  ‘to  hawk;  to  cauterize,  etch’.  OE.  bee- tan,  OS.  betian,  etc.,  are  causatives  of  OE.  bitan, resp.  OS.  bitan,  OHG.  bi33an,  etc.,  and  lit.  mean ‘to  cause  to  bite’.  See  bite  and  cp.  words  there referred  to.
bait,  n.  —  ON.  beita,  ‘food’,  belt,  ‘pasture’,  fr. beita,  ‘to  cause  to  bite'  (see  prec.  word) ;  in  some meanings  derived  directly  fr.  prec.  word, baize,  n.,  a  coarse  woolen  cloth.  —  F.  bates,  pi.  of baie,  prop.  fem.  of  bai,  ‘bay  colored".  See  bay, ‘reddish’.
Derivative:  baize,  tr.  v.
bake,  tr.  and  intr.  v.  —  ME.  baken,  fr.  OE.  bacan, rel.  to  ON.  baka,  Swed.  baka,  Dan.  bage, MDu.  backen,  Du.  bakken,  OHG.  bahhan, backan,  MHG.,  G.  backen,  fr.  l.-E.  base  *hhdg-, ‘to  warm,  roast,  bake’,  whence  also  Gk.<ji<bYst.v, ‘to  roast’.  Cp.  batch,  batz  and  the  second  ele¬ ment  in  zwieback.  Base  *bhdg-  is  a  -^-enlarge¬ ment  of  base  *bhe-,  ‘to  warm' ;  see  bath. Derivatives:  bake,  n.,  bak-ed,  adj.,  baker  (q.v.), bak-ing,  n.,  bak-ing-ly,  adv. bakelite,  n.,  synthetic  resin.  —  Named  after  its inventor  Leo  Hendrik  Baekeland  (1863-1944). For  the  ending  see  subst.  suff.  -ite. baker,  n.  —  ME.  bakere,  fr.  OE.  bazeere,  fr.  bacan, ‘to  bake’.  See  bake  and  agential  suff.  -er  and cp.  baxter.
Derivative:  bak-erv,  n.
baksheesh,  n.,  a  gratuity ;  a  tip.  —  Pers.  bakhshish, lit.  ‘gift’,  a  derivative  of  the  verb  bukhshidan,  ‘to give’,  fr.  I.-E.  base  *bhag-,  ‘to  distribute,  share out’,  whence  also  OI.  bhdjati,  ‘assigns,  allots, apportions,  enjoys,  loves’,  bhagah,  'allotter,  dis¬ tributor,  master,  lord’,  Gk.  9ay£tv,  ‘to  eat’. See  -phagous  and  cp.  Bhaga  and  the  first  ele¬ ment  in  Bhagavadgita,  and  in  bahadur.
Balaena,  n.,  a  genus  of  whales,  the  Greenland whale.  —  L.  ballaena,  balaena.  See  baleen, balaghat,  balaghaut,  n.,  tableland  above  the  pas¬ ses  (Anglo-Ind.)  —  Formed  fr.  Pers.  bald, ‘above’,  and  Hind,  ghat,  ‘a  pass’, balalaika,  n.,  a  Russian  stringed  instrument  with a  triangular  body.  —  Russ,  balalaika,  which, according  to  Erich  Berneker,  Etymologisches
balan-
balm
Worterbuch  der  russischen  Sprache,  I,  p.40, Heidelberg,  1908-13,  is  rel.  to  Russ,  balabolit’, ‘to  chatter,  babble',  from  the  I.-E.  imitative  base *balb-,  whence  also  L.  balbus,  ‘stammering’.  See booby  and  cp.  words  there  referred  to. balan-,  form  of  balano-  before  a  vowel, balance,  n.  —  OF.  (=  F.)  balance,  fr.  L.  bi-, ‘two,  twice’,  and  VL.  *lancia,  fr.  L.  lanx,  gen. lands,  ‘plate,  dish;  scale  of  weighing  machine’, which  prob.  stands  for  *llnk-s,  fr.  I.-E.  base *iliq~,  ‘to  bend’,  whence  prob.  also  Gk.  k&aoq, Xexovt),  ‘dish’,  lt/pwc„  ‘slanting,  crosswise’, Xo E,6<;,  ‘slanting,  crooked,  bent’;  see  Walde- Hofmann,  LEW.,  I,  p.761  s.v.  lanx.  See  bi-  and loxo-  and  cp.  the  second  element  in  auncel.  Cp. also  Lecanium,  Lecidea,  lekane.  The  first  a  in balance  is  prob.  due  to  an  association  of  this word  with  F.  bailer,  ‘to  dance’,  fr.  Gk.  paXXeiv, ‘to  throw’  (see  ballistic).
Derivatives:  balance,  tr.  v.,  balanc-ed,  adj., balanc-er,  n.,  balanc-ing,  adj. balaniferous,  adj.,  acom-bearing.  —  Compound¬ ed  of  L.  balanus,  ‘acorn’,  and  L .ferre,  ‘to  bear, carry’.  See  balano-  and  -ferous. balano-,  before  a  vowel  balan-,  combining  form meaning  ‘acorn’.  —  Gk.  (JaXavo-,  (3aXav-,  fr. (3aXavo;,  ‘acorn’,  which  is  cogn.  with  L.  gldns, gen.  glandis,  ‘acorn’.  See  gland  and  cp.  the second  element  in  myrobalan. balanoid,  adj.,  acorn-shaped. —  Compounded  of balan-  and  Gk.  -osiSt^,  ‘like’,  fr.  elSop,  ‘form, shape’.  See  -oid.
balas,  n.,  a  variety  of  spinel  ruby.  —  F.  balais, fr.  Arab,  balakhsh,  fr.  Balakhshdn,  fr.  Pers. Badhakhshin,  name  of  a  region  in  Central  Asia (near  Samarkand),  where  this  variety  of  spinel ruby  is  found.
balatron,  n.,  jester,  buffoon.  —  L.  balatro,  gen. -onis,  of  Etruscan  origin;  not  related  to  L. blaterd,  ‘babbler’.
balaustine,  n.,  the  pomegranate  tree.  —  Formed with  suff.  -ine  fr.  Gk.  pocXaucmov,  ‘flower  of the  wild  pomegranate’,  a  word  of  Sem.  origin. Cp.  Aram,  balatz,  said  of  the  blossoming  of  the pomegranate  tree.  For  the  correspondence  of Greek  st  to  Semitic  s,  tz,  cp.  Gk.  e-rupa^,  fr. Heb.  tzdri  (see  sty  rax).  Cp.  baluster, balbriggan,  n.,  a  cotton  fabric  used  for  hosiery.  — Prop,  ‘fabric  made  in  Balbriggan  (in  Ireland)’, balbuties,  n.,  stammering  (med.)  —  Medical  L., fr.  L.  balbutire,  ‘to  stammer’,  fr.  balbus,  ‘stam¬ merer’,  from  the  I.-E.  imitative  base  *bal-,  ‘to stutter’.  See  booby  and  cp.  words  there  re¬ ferred  to.
balcony,  n.  —  It.  balcone,  formed  with  the  aug¬ mentative  suff.  -one  fr.  balco,  ‘scaffold’,  which is  borrowed  fr.  OHG.  balcho,  ‘beam’  (whence MHG.  balke,  G.  Balken,  ‘beam’).  See  balk, ‘beam’.
bald,  adj.  —  ME.  balled,  orig.  ‘white’,  fr.  I.-E. base  *bhel-,  ‘to  shine’,  whence  also  OI.  bhalam, ‘brightness;  forehead’,  Gk.  <paX6?,  ‘white’.
142
tpaXapop,  ‘having  a  patch  of  white’,  tpaXapip, ‘coot’  (so  called  from  a  white  spot  on  its  head), L.  fulica,  ‘coot’.  Alb.  bale,  ‘forehead’,  OSlav. belu,  ‘white’,  Lith.  balnas,  bdltas,  Lett,  bals, ‘pale’,  OE.  bal,  ‘a  blazing  fire,  a  funeral  pyre’, OHG.  belihha,  MHG.,  G.  belche,  ‘coot’.  Cp. balefire,  Beltane,  beluga,  blaze,  ‘flame’,  Fulica, full,  ‘to  thicken  cloth’,  Phalaris,  phalarope. Derivatives:  bald-en,  tr.  and  intr.  v„  bald-ish, adj.,  bald-ly,  adv.,  bald-ness,  n. baldachin,  n.,  canopy.  —  F.  baldaquin,  fr.  It.  bal- dacchino,  fr.  Baldacco,  ‘Bagdad’,  fr.  ML.  Bal- dac.  It.  baldacchino  orig.  denoted  richly  woven silk  stuff  brought  from  Bagdad.  Cp.  baudekin. balderdash,  n.,  1)  nonsense;  2)  a  poor  mixture  of liquors.  —  The  first  element  is  prob.  identical with  Dan.  balder,  ‘noise,  clatter’,  the  second  is the  English  word  dash.  Dan.  balder  is  rel.  to Dan.  baldre,  dial.  Norw.  baldra,  dial.  Swed. ballra,  MLG.,  earlier  Du.  balder en,  Dan.  buldre, Swed.  bullra,  ‘to  make  a  noise,  rattle’,  MHG. buldern,  G.  poltern,  ‘to  knock,  rattle,  bluster’. These  words  derive  from  a  dental  enlargement of  I.-E.  base  *bhel-,  ‘to  sound’,  whence  OE. bellan,  bylgan,  ‘to  bellow’.  See  bellow,  ‘to  make a  loud  noise’,  and  cp.  words  there  referred  to. baldric,  n.,  a  belt  worn  over  one  shoulder.  — ME.  baldric,  baudric,  haudry,  fr.  OF.  baldre, baldrei,  baldroi,  (whence  F.  baudrier  and  MHG. balderich),  fr.  L.  balteus,  ‘belt’.  See  belt  and  cp. words  there  referred  to.
Baldwin,  masc.  PN.  —  OF.  Baldoln  (F.  Bau- douin),  of  Teut.  origin.  Cp.  OHG.  Baldawin,  lit. ‘bold  friend’,  fr.  OHG.  bald,  ‘bold’,  and  wini, ‘friend’.  For  the  first  element  see  bold  and  cp. the  second  element  in  Theobald.  OHG.  wini, ‘friend’,  is  rel.  to  OE.  wine,  ON.  vinr,  ‘friend’, and  to  OE.  winnan,  ‘to  strive,  struggle,  fight’. See  win  and  wish  and  cp.  the  first  element in  Winfred  and  the  second  element  in  Edwin, bale,  n.,  bundle,  package.  —  ME.,  fr.  OF.  bale, balle  (F.  bade),  fr.  OHG.  balla,  ‘ball’.  See  ball ‘a  round  body’.
Derivatives:  bale,  tr.  v.,  bal-er,  n. bale,  n.,  misfortune.  —  ME.,  fr.  OE.  bealu,  bealo, balu,  ‘injury,  calamity’,  rel.  to  OS.  halo,  ‘evil’, ON.  bol,  ‘misfortune’,  OFris.  bealu,  ‘evil’,  OHG. halo,  ‘destruction’,  Goth,  balwjan,  ‘to  torment’, balweins,  ‘pain,  torture’,  balwa-wesei,  ‘wicked¬ ness’.
Derivatives:  bale-ful,  adj.,  bale-ful-ly,  adv.,  bale- ful-ness,  n.
bale,  n.,  bucket,  v.,  to  dip  water.  —  See  bail, ‘bucket’.
bale,  n.,  balefire.  —  OE.  beel.  See  balefire, baleen,  n.,  whalebone.  —  ME.  balene,  baleyne, ‘whale,  whalebone’,  fr.  OF.  baleine,  ofs.m.,  fr. L.  ballaena,  ‘whale’ ,  which  was  borrowed  fr.  Gk. (pdtXXocwa,  of  s.m.,  through  the  medium  of  the Illyrian  language,  a  fact  which  explains  the  tran¬ sition  of  Gk.  9  into  L.  b  (instead  of  p).  Gk. 9<iXXaiva  is  related  to  ipaXXAs,  ‘penis’,  fr.  I.-E.
143
```


## [2026-09-05T14:43:17.183Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '4321,4360p' KLN_1966.txt"
}
```


### [2026-09-05T14:43:17.237Z] TOOL RESULT

```
base  *bhel-,  ‘to  swell’.  See  ball,  ‘a  round  body’, and  cp.  Balaena,  balinger. balefire,  n.  —  OE.  bielfyr,  ‘funeral  fire’,  com¬ pounded  of  bxl,  ‘a  blazing  fire,  a  funeral  pile’, and  fyr,  ‘fire’.  The  first  element  is  rel.  to  ON.  bdl, ‘a  great  fire’,  fr.  I.-E.  base  *bhel-,  ‘to  shine’;  see bald.  For  the  second  element  see  fire, balinger,  n.,  a  whaleship  ( obsol .)  —  OF.  balen- gier,  ‘whaleship*,  fr.  baleine,  ‘whale’.  See  baleen, balk,  also  baulk,  n.,  ridge  of  land  left  unplowed between  furrows :  a  beam.  —  ME.  balke,  ‘beam’, fr.  OE.  balca,  ‘ridge  between  furrows,  beam, rafter’,  rel.  to  OS.  balko,  ON.  bjalki,  Dan.  bjelke, Swed.  bjdlke,  OFris.  balka,  OHG.  balko,  balcho, MHG.  balke,  G.  Balken,  ‘beam,  rafter’  (cp., with  vowel  gradation,  OE.  bolca,  ‘wooden gangway  of  a  ship’),  ON.  bolr,  ‘trunk  of  a  tree’ ; fr.  I.-E.  base  *bheleg-,  ‘beam,  plank’,  whence also  Gk.  tpaXzy?,  ‘trunk,  log;  line  of  battle, battle  array’,  cpaXtoit;,  ‘beam’,  L.  fulcire,  ‘to prop’,  fulcrum,  ‘bedpost’,  Lith.  balziena,  ‘cross¬ bar’,  Lett,  bdlziens,  ‘prop,  stay’.  Cp.  balcony. Cp.  also  block,  bole,  ‘trunk’,  bulk,  ‘projection’, debauch,  ebauchoir,  fulcrum,  phalange,  phalanx, planch,  planchet,  plancier,  plank.
Derivatives:  balk  v.  (q.v.),  balk-er,  n.,  balk-ing- ly,  adv.,  balk-y,  adj.
balk,  also  baulk,  tr.  v.,  to  hinder,  thwart;  intr. v.,  to  refuse.  —  Formed  fr.  prec.  word  and  lit. meaning  ‘to  put  a  beam  in  the  way’.  Cp.  bilk.
Balkanize,  tr.  v.  —  Coined  by  the  English  jour¬ nalist  and  editor  James  Louis  Garvin  (1 868- 1947)  in  allusion  to  the  political  condition  in  the Balkans  in  19 12-13.
ball,  n.,  a  round  body;  a  sphere.  —  ME.  bade, fr.  ON.  bbllr,  which  is  rel.  to  OHG.  hallo,  balla, MHG.  bade,  bal,  G.  Ball,  fr.  I.-E.  base  *bhel-, ‘to  swell’.  See  belly  and  cp.  Balaena,  bale, ‘bundle’,  baleen,  balinger,  balloon,  ballot,  bil¬ low,  bulk,  ‘size’,  and  the  first  element  in  bill- berry  and  in  pall-mall.
Derivatives:  ball,  tr.  v.,  to  form  into  a  ball, ball-er,  n.
ball,  n.,  a  party  for  social  dancing.  — -  F.  bal,  fr. OF.  bailer,  ‘to  dance’,  fr.  VL.  ballare,  fr.  Gk. ^xXXl^etv,  ‘to  dance’,  which  prob.  derives  fr. fWXXetv,  ‘to  throw’.  See  ballistic  and  cp.  ballad, ballerina,  ballet,  bayadere, ballad,  n.,  1)  a  sentimental  or  romantic  song;  2)  a narrative  song.  —  ME.  balade,  prop,  ‘a  song written  for  a  dance’,  fr.  OF.  balade  (F.  ballade), fr.  OProven?.  balada,  lit.  ‘dance’,  later  used  in the  sense  of  ‘dancing  song’,  fr.  balar,  ‘to  dance’. See  ball,  ‘party  for  dancing’, ballade,  n.  a  poem  with  three  stanzas  of  eight  or ten  lines  each  and  an  envoy  of  four.  —  F.  See prec.  word.
balladry,  n.,  ballad  poetry.  —  Formed  fr.  ballad with  suff.  -ry.
ballast,  n.,  heavy  material  used  to  steady  a  ship. —  Dan.  and  Swed.,  assimilated  fr.  earlier  bar- last  lit.  ‘bare  load’.  The  first  element  of  this
compound  is  rel.  to  the  E.  adjective  bare;  the second  is  rel.  to  last,  a  unit  of  weight. Derivatives:  ballast-er,  n.,  ballast-ing,  n. ballerina,  a  woman  ballet  dancer.  —  It.,  fr.  bal¬ lare,  ‘to  dance’.  See  ball,  ‘party  for  dancing’, ballet,  n.  —  F.,  fr.  It.  balletto ,  dimin.  of  ballo, ‘dance’.  See  ball  ‘party  for  dancing’,  and  -et. Derivative:  ballet,  tr.  v.
ballista,  n.,  an  ancient  military  engine  ( Roman antiq.)  —  L.,  fit.  ‘a  throwing  machine’,  fr.  Gk. piXXeiv,  ‘to  throw’.  See  next  word ballistic,  adj.,  pertaining  to  projectiles.  — Formed with  suff.  -istic  fr.  Gk.  fiaXXetv,  ‘to  throw’, which  stands  in  gradational  relationship  to (JoXfj,  floXoc,  ‘a  throw’,  fisXo?,  ‘bolt,  arrow, dart’,  lit.  ‘something  thrown’,  fr.  I.-E.  base *gwel-,  whence  also  OI.  apa-gurya-,  ‘swinging’, Avestic  ni-yra-'re,  ‘they  are  being  hurled  down’, Toch.  AB  kla-,  ‘to  fall’,  and  perhaps  also  OI. galati,  ‘trickles’,  OHG.  quellan,  MHG.,  G.  quel- len,  ‘to  well  up’.  Cp.  ball,  ‘party  for  dancing’, ballista,  amphibole,  amphibology,  anabolism, bdemnite,  Belostoma,  bolide,  bolometer,  boule, ‘council’,  catabolism,  devil,  diabolic,  discobolus, Eblis,  ecbolic,  Elaphebolion,  emblem,  embolism, emboly,  hyperbola,  hyperbole,  metabolism,  pa¬ rable,  parabola,  parlance,  parley,  parliament, parlor,  parol,  parole,  periblem,  problem,  scy- balum,  symbol,  Tribolium,  Tribulus. ballistics,  n.,  the  study  of  projectiles.  —  See  prec. word  and  -ics.
ballonet,  n.,  an  auxiliary  gas  or  air  bag  in  a  bal¬ loon  or  airship.  —  F.  ballonnet,  lit.  ‘a  small balloon’,  fr.  ballon.  See  next  word  and  -et. balloon,  n.  —  F.  ballon,  fr.  It.  pallone,  which  is formed  with  augment,  suff.  -one  fr.  palla,  ‘a ball’,  a  word  of  Teut.  origin;  see  ball,  ‘a  round body’,  and  -oon.  The  b  in  F.  ballon  (fr.  It.  pal¬ lone)  is  due  to  the  influence  of  F.  bade,  ‘ball’. Cp.  pallone.
Derivatives:  balloon,  tr.  and  intr.  v.,  and  the hybrid  noun  balloon-ist,  n. ballot,  n.  —  F.  ballotte,  fr.  It.  ballotta,  ‘little  ball’, dimin.  of  balla,  ‘ball’  (see  E.  ball,  ‘a  round body’);  so  called  in  allusion  to  the  small  balls formerly  dropped  into  the  voting  um. Derivatives:  ballot,  intr.  and  tr.  v.,  ballot-age (q-v.)
Ballota,  n.,  a  genus  of  plants  of  the  mint  family (bol.)  —  ModL.,  fr.  Gk.  paXXojTT),  ‘the  black horehound’;  of  unknown  origin, ballotage,  n.  —  F.  ballottage,  fr.  ballotter,  ‘to  bal¬ lot’,  fr.  ballotte.  See  prec.  word  and  -age. ballyhoo,  n.,  1)  outcry;  2)  noisy  advertising (slang).  —  Of  uncertain  origin;  possibly  fr. Ballyhooly,  a  village  in  County  Cork,  Ireland. Derivative :  ballyhoo,  tr.  and  intr.  v. ballyrag,  tr.  and  intr.  v.  —  A  variant  of  bullyrag, balm,  n.  —  ME.  basme,  baume,  fr.  OF.  bausme, baume  (F.  baume),  fr.  L.  balsamum,  ‘gum  of  the balsam  tree,  balsam’,  fr.  Gk.  (JtxXoajiov.  See balsam  and  cp.  embalm.
Balmoral
Derivatives:  balm-y,  adj.,  balm-i-ly ,  adv.,  balm- i-ness,  n.
Balmoral,  n.,  name  of  various  objects.  —  Named after  Balmoral  Castle  in  Scotland, balneal,  adj.,  pertaining  to  baths.  —  Formed  with adj.  suff.  -al  fr.  L.  balneum ,  balineum ,  ‘bath’,  fr. Gk.  paXxveiov,  of  s.m.,  which  is  of  uncertain origin.  Cp.  bagnio,  baignoire  and  the  first  ele¬ ment  in  bain-marie.
balneo-,  combining  form  meaning  ‘bath’.  —  Fr. L.  balneum,  ‘bath’.  See  balneal, balneology,  n.,  the  study  of  bathing.  —  Com¬ pounded  of  balneo-  and  Gk.  -Xoyla,  fr.  -Xoyo?, ‘one  who  speaks  (in  a  certain  manner) ;  one  who deals  (with  a  certain  topic)’.  See  -logy. Derivatives :  balneo  log-ic-al,  adj balneolog-ist,  n. balsam,  n.  — •  L.  balsamum,  ‘gum  of  the  balsam tree,  balsam’,  fr.  Gk.  (idXaapov,  fr.  Heb.  basdm, which  is  rel.  to  Heb.  bdsem,  Aram,  busmA,  Syr. besmd,  Arab,  bashdm,  ‘balsam,  spice,  perfume’. Cp.  balm,  embalm.
Derivatives:  balsam,  tr.  v., balsam-er, n., balsam¬ ic,  adj.  and  n.,  balsam-itic,  adj.,  balsam-ize, tr.  v.
Balsaminaceae,  n.  pi.,  a  family  of  plants  ( bot .)  — ModL.  See  next  word  and  -aceae. balsamine,  n.  the  garden  balsam.  —  F.,  fr.  Gk, [ixAax|xivr),  ‘the  balsam  plant’,  fr.  pdXaapov.  See balsam  and  -ine.
balteus,  n.,  girdle  or  belt  worn  by  ecclesiastic dignitaries.  —  L.,  of  Etruscan  origin,  Cp.  belt, baldric.
Balthasar,  masc.  PN.  —  F.,  fr.  L.,  fr.  Gk.  BaX- Txaap,  fr.  Heb.  Belt1 shat ztzar  (Dan.  10:1),  fr. Babyl.  Baldt-shar-usur,  lit.  ‘save  the  life  of  the king’.  In  Hebrew  the  name  has  been  assimilated in  form  to  that  of  Belshatztzar  (see  Belshazzar). baluster,  n.,  support  for  a  railing.  —  F.  balustre, fr.  It.  balaustro,  fr.  L.  balaustium, fr.Gk.  [JaXati- gzi'jv,  ‘flower  of  the  wild  pomegranate’,  a word  of  Syrian  origin  (see  balaustine);  so  called from  the  shape  of  the  capital.  Cp.  next  word and  banister.
Derivatives:  baluster-ed,  adj.,  balustrade  (q.v.) balustrade,  n.,  a  row  of  balusters.  —  Prop,  ‘a  set of  balusters’,  fr.  F.  balustrade,  fr.  It.  balaustrata, lit.  "provided  with  balusters’,  fr.  balaustro  (see prec.  word  and  -ade);  introduced  into  English by  the  diarist  John  Evelyn  (1620-1706). Derivatives:  balustrad-ed,  adj.,  balustrad-ing,  n.
bam,  tr.  and  intr.  v.,  to  bamboozle.  —  Abrevia- tion  of  bamboozle.
bambino,  n.,  a  little  child ;  an  image  of  the  infant Jesus.  —  It.,  ‘baby’,  dimin.  of  bambo,  ‘simple’, w  hich  is  of  imitative  origin, bamboo,  n.  —  Malay  bambu.  Cp.  Bambusa.
Derivative:  bamboo,  tr.  v. bamboozle,  tr.  v.,  1)  to  hoax;  2) to  confuse,  puzzle. —  Of  uncertain  origin.
Bambusa,  n.,  a  genus  of  bamboos  (hot.)  — -  ModL. See  bamboo.
ban,  tr.  v.,  to  prohibit;  to  curse  (archaic).  —  ME.
144
145
barmen,  fr.  OE.  barman,  ‘to  summon,  proclaim, command’,  rel.  to  ON.  banna,  ‘to  forbid,  pro¬ hibit’,  OHG.  batman ,  ‘to  command  or  forbid under  threat  of  punishment’,  MHG.,  G.  bannen, ‘to  put  under  the  ban,  banish,  expel,  curse’; formed  with  -n-  formative  element  fr.  I.-E.  base *bha-,  ‘to  speak,  tell,  say’,  whence  also  Gk. <ptxvat,  L.  fan,  ‘to  say’,  Arm.  ban,  ‘word’,  OIr. bann,  ‘law’.  See  fame  and  cp.  ban,  ‘edict’,  banish, banal,  bandit,  banns,  abandon,  aubain,  boon,  n., contraband.
ban,  n.,  edict.  —  ME.,  partly  fr.  bannen,  ‘to  sum¬ mon,  proclaim’  (cp.  ON.  bann,  ‘prohibition’, OHG.  ban,  ‘commandment  or  prohibition  under threat  of  punishment,  jurisdiction’,  MHG.  ban, G.  Bann,  ‘public  proclamation,  jurisdiction,  ban, ostracism,  curse’,  which  derive  fr.  ON.  banna, resp.  OHG.  bannan,  MHG.,  G.  bannen );  partly fr.  OF.  (==  F.)  ban,  ‘public  proclamation’,  fr. Frankish  *ban,  which  is  rel,  to  OHG.  ban (see  above).  See  ban,  v.
ban,  n.,  a  governor  of  Croatia.  —  Serbo-Croatian ban,  ‘lord,  master,  ruler’,  fr.  Pers.  ban,  ‘prince, lord,  chief,  governor’  (prob.  through  the  medium of  the  Avars).  As  a  suff.  -ban  (var.  -wan)  means ‘keeper,  guardian’.  Pers.  ban,  is  rel.  to  OPers. pa(y)-,  ‘to  guard,  protect’,  OI.  pdti,  ‘guards, protects’,  pand-,  ‘guarding,  protecting’  (see P.Horn,  GrundriB  der  neupersischen  Etymo- logie,  StraBburg,  1893,  No.  176).  See  food  and cp.  banat  and  the  second  element  in  durwaun and  in  satrap.
Bana,  n.,  son  of  Bali,  a  thousand  armed  giant (Hindu  mythol.)  —  OI.  Bdndh,  lit.  ‘arrow’,  prob. a  loan  word  fr.  Austroasiatic. banal,  adj.,  trite,  commonplace.  —  OF.  banal, fr.  ban,  ‘proclamation’.  See  ban,  ‘edict’.  Banal orig.  meant  ‘compulsory’,  whence  it  came  to denote  ‘common  to  all,  commonplace’, banal,  adj.,  pertaining  to  a  ban  or  the  banat.  — Formed  fr.  ban,  ‘governor’,  with  adj.  suff.  -al. banality,  n.,  1)  triteness;  2)  a  platitude.  —  F.  ba- nalite,  fr.  banal.  See  hanal,  ‘trite’,  and  -ity. banana,  n.  —  Sp.  and  Port.,  fr.  earlier  Congo¬ lese  banam.
banat,  also  banate,  n.,  the  district  governed  by  a ban.  —  A  hybrid  coined  fr.  ban,  ‘governor’  and suff.  -ate  (fr.  L.  -atus).  Cp.  G.,  F.  banat,  which are  of  the  same  meaning  and  origin, banausic,  adj.,  proper  for  an  artisan;  trivial.  — Gk.  pxvaucty.cq,  ‘relating  to  artisans’,  fr.  (Java-j- cnx,  ‘handicraft’,  fr.  [Hxvauaoc;,  ‘artisan’,  which is  of  uncertain  origin.  The  usual  explanation that  fliva’joo;  is  a  dissimilated  form  of voojaog,  and  compounded  of  (JxGvoe;,  ‘furnace, forge’,  and  auetv,  ‘to  dry’,  is  folk  etymology. Banbury  cake.  --  Named  after  Banbury  in  Ox¬ fordshire.
banc,  n.,  bench,  esp.  bench  on  which  judges  sit.  — E.  See  banco.
banco,  n.,  bank. —  It.,  fr.  Teut.  *banki-.  Cp.  ME. banke  and  see  bank,  bench.  Cp.  also  banc  and
the  last  element  in  charabanc,  mountebank, saltimbanco.
band,  n.,  a  tie.  —  ME.,  fr.  ON.  band,  rel.  to  OS., Swed.,  Du.,  G.  band,  OHG.,  MHG.  bant,  Goth. bandi,  lit.  ‘that  which  binds’,  fr.  I.-E.  base *bendh-,  ‘to  bind’,  whence  also  OI.  bandhdh,  ‘a tying,  fastening;  band,  bandage’,  Mir.  bainna, ‘bracelet’ ;  F.  bande,  ‘band’,  is  a  Teut.  loan  word. See  bind  and  cp.  bend,  bond.  Cp.  also  bandage, bandanna,  bandhava,  bandhu,  bandoleer,  and the  second  element  in  ribband,  ribbon,  roband, seerband.
Derivatives:  band,  tr.  and  intr.  v.,  band-ed,  adj., band-er,  n.,  band-ing,  n.
```


## [2026-09-05T14:43:37.737Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"-- TAD balsam --\"; grep -n \"بلسم\\|بلسان\\|بشام\\|بلسام\" TAD_pages.txt | head -20"
}
```


### [2026-09-05T14:43:37.784Z] TOOL RESULT

```
-- TAD balsam --
540:                                                            ‫وطيب ومنه البلسان‬
```


## [2026-09-05T14:43:38.479Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"-- AFA fraenkel --\"; grep -n -i \"balsam\\|busm\" AFA.txt | head -20; echo \"-- LKT --\"; grep -n -i \"balsam\" LKT.txt | head -10"
}
```


### [2026-09-05T14:43:38.537Z] TOOL RESULT

```
-- AFA fraenkel --
6200:meele der Ismaeliten »Würze , Balsam and Myrrhen** nach174
-- LKT --
851:293.  Hebr.  b§s§m: 'Balsamstaude,  Balsam',  eine  Handels- ware, welche  die  Griechen  nebst  dem Namen  von  den  Phöniziern  erhielten. Gr.  ßd\aa|nov,  lat.  balsamum;  hieraus  it. balsamo,  balsimo,  asp.  blasmo,  sp.  pg. balsamo,  prov.  balme,  frz.  bäume  [aber pikardisch  bäm  'Minze'],  rum.  baisam; dtsch.  Balsam,  ndl.  balsem,  engl,  bahn; russ.  bal'sam,  bulg.  serb.  poln.  baisam, cech.  baisam,  balzam.  —  Aus  demselben Grundwort  mlat.  bisamum,  dtsch.  Bisam, cech.  poln.  pizmo  'Moschus'.  —  Vgl. noch  Balsamine,  Impatiens  Balsamina, engl,  halsamine,  baisam.  [Kluge  34  u. 54.  G.  Schvveinfurth,  Über  Balsam  und Myrrhe  1893.
3474:mümija  'einbalsamierter  Leichnam'  ist in  dieser  Bedeutung  in  alle  europäischen Sprachen  übergegangen:  it.  mummia, fvz.  motnie,  mimiie,  sp.  momia,  pg.mumia, Adj.  sp.  momio  'abgemagert',  vam.mumie 'Mumie',  momie,  nioniue  'Vogelscheuche, Popanz';  engl,  tmunrny,  ndl.  mummie, dtsch.  Mumie;  russ.  murniju.  [Eguilaz 457.    ML  5743.    Kluge  317.
5724:Balsam  293
5725:Balsamine  293
6019:balsamine  293
6946:balsamo  293
7980:balsamo  293
10036:babuche  1625 iadrt  152 badana  316 badea  319 badian(a)  162 bagasa  171 daA«H  177 baladi  196 balaja  151 balajo  151 6aZc(5n  197 fcflWa  271 (de,en)  balde  271 baldequhi  170 fea/rfio  271 balsamo  293 bambu  209 banana  211 bandujo  273 bandullo  273 bango  213 barahunda  256 baraja(do)  225 barajar  225 baranda  223 barbacana  197 fcarca  2148 fcarrfa  228 bar da ja  229 bardaje  229 ftarrfo  228 barragän  250 barroco  364 6a<a  273
```


## [2026-09-05T14:43:46.700Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '520,560p' TAD_pages.txt; echo \"---- page tags near ----\"; awk 'NR<560 && /pdf page/{p=$0; l=NR} END{}' TAD_pages.txt; grep -n \"pdf page\" TAD_pages.txt | awk -F: '$1<560' | tail -5"
}
```


### [2026-09-05T14:43:48.566Z] TOOL RESULT

```
                                                                    ‫علاج الخبل‬
                             ‫بأعوت ‪ -‬ارامي ‪ 8‬باعونا » ممناه صلاةوطلبه‬
                 ‫فداادر‪-‬سي مركب منباغأي بستان وداد أي علال‬
                                                         ‫بغ‬
  ‫معناه قرون النول‬       ‫بأقللاء لي ‪ 3‬ايطالي فلاءعءع‪ 20‬من اليونانفي ‪5‬‬

‫بمجة ‪ -‬عامية أي صرة فن الثياب أصلبا منقطمتاعه أي جمعه السنرونقلت‬
                                               ‫من العرببة إلىانلمسْاروية ‪682‬مة‪0‬‬
 ‫بقدونس ‪ -‬اراي ‪ 2‬لاداتش » معناه بقل الانسان وهو بقل حار يو كل‬
                                                                          ‫م‬

               ‫يوئاني ‪90‬كاوم وهو شجر يشبه الاآس خشيه صاب‬              ‫نفس‬
 ‫بشسمات دفار بقسومات » وفى التركة ب«كمياد أ»صله من اللاتينية‬
                     ‫ش‬                      ‫معناه خير حور مر'ين‬      ‫قاأع ‪06218‬‬

                            ‫بلاس ‪ -‬فارسي « بلاس ‪ 6‬وهو المسح من شعر‬
‫بلاط ‪ -‬افظ لاتيني ختدداة‪21‬م معناه قصر أيدارالملك وليس هومأخوذا من‬
                                                  ‫ش‬          ‫البلاط الذي يفرش‬
 ‫لشم في اليونانية «مس«دولدة مأخوذ من الارامية ب«مما » أي عطر‬
                                                            ‫وطيب ومنه البلسان‬
 ‫بلنم ‏يوناني ‪501‬ههام معناه الهاب وهو أحد الاخلاط الاربعة وبطلق‬
                                                                      ‫على النفث‬
                               ‫يلور فارسي < ور » وهو زجاج أبيض‬
                         ‫فارسي وهو أغاظا اوتا العود ويام معئاة سطح‬     ‫م‬
‫من ‪0110‬م تفاح‬      ‫حت ابطالى ‪010002‬وم أي فاح ذهى ‪05 .‬‬               ‫ادو‬
                                ‫و‪ 0500‬من ذهب ويقال له‪ 2‬الاسبانية ‪10‬‬

                     ‫ترك ه باشك اولى» وهونباث مسبت منوم‬              ‫ابنج‬


                                   ‫بنجرة ‪ -‬فارسي « ينجره » أي شباك‬


‫العلاملكيير‪--‬فارسي ‪ 2‬بند ‪ 26‬ممنأه عقدة ورباط دعي كذا لانه‬
                                                                              ‫‪0‬‬
                                                           ‫ربط عل السهم‬

 ‫وشاه بندر معناه‬      ‫ىء‬
                       ‫طعلى‬
                          ‫اسفن‬
---- page tags near ----
```


## [2026-09-05T14:43:55.478Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"pdf page\\|\\[page\" TAD_pages.txt | head -5; echo \"--- formfeed count before line 540 ---\"; head -540 TAD_pages.txt | tr -cd '\\f' | wc -c"
}
```


### [2026-09-05T14:43:55.535Z] TOOL RESULT

```
--- formfeed count before line 540 ---
15
```


## [2026-09-05T14:44:04.638Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"-- MON balsam --\"; grep -n \"بلسام\\|بلسان\\|بشام\" MON_part1.txt | head -10; echo \"-- MON berehne --\"; grep -n \"برهنه\" MON_part1.txt | head -5; echo \"-- MON bus --\"; grep -n \"بوسیدن\\|بوس \" MON_part1.txt | head -5"
}
```


### [2026-09-05T14:44:04.718Z] TOOL RESULT

```
-- MON balsam --
8246:ص مر .) نو سنده و اطلاع دهنده پبشامد ها و 
24816:بلسان: ۷۵ (معر .] (۱.) (گا.) گیاهی از 
24822:ابوشام: بشام» بلسم مکه. درخت بلسان مکی. 
24824:آغاجی» بلسان من شجرالب‌لسم. ضسح .. 
24830:دانٌ این گیاه را حب البلسان نیز گویند و بنام 
24831:بلسان در تداوی مصرف می‌شود. (گیا.) 
24832:بلسان نام عام همه گیاهانی است که از آنها 
52703:چیزی. بشامدهاء حوادت. 
69139:در نقاشی بکار رود. روغن بلسان: روغنی که 
69140:از «بلسان» گرفته شود. (برای امتحان آن در 
-- MON berehne --
4856:کاذب است. پروتوپلاسم آنها برهنه و بدون 
10979:ماهیی است بزرگ و سر برهنه که دهانی 
27536:پاپتی: آا«م5م (ص‌مر.) (عم.) پا برهنه» یکث 
27905:کف پایش طویل و برهنه و انگشتانش نیز 
29422:بی‌خورش» ساده» تنها: نان پتی. برهنه 
-- MON bus --
6971:کسان بکار می‌رود. اتوبوس دو طبقه: 
6975:اتوبوس شهری: اتوبوسی که در شهر رفت و 
6983:بجایی. شغل آنکه اتوبوس می‌راند. شرکت 
17378:(مص م.) رشت و آلوده کردن نابوس کسی 
19250:توقف وسایط نقلیه (اتومبیل» اتوبوس
```


## [2026-09-05T14:44:06.314Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"-- BQT v1 --\"; grep -n \"برهنه\" BQT_v1_pages.txt | head -8; echo \"-- BQT bus --\"; grep -n \"بوسیدن\\|بوسه\" BQT_v1_pages.txt | head -8; echo \"-- BQT balsan --\"; grep -n \"بلسان\\|بشام\" BQT_v1_pages.txt BQT_v2_pages.txt | head -8"
}
```


### [2026-09-05T14:44:06.398Z] TOOL RESULT

```
-- BQT v1 --
32028:اسق بت و بمعنی دویم تهك ‌‌ حست که برهنه
32053:برهنه و عربان - وتهی وخالی ۰
-- BQT bus --
15104:اور سه شم اول بروزت بوسه ۰ بمعنی
21045:بندق‌شکستی «» کنابه از بوسه دادن
21432:سنبوسه و قطاب را کوبند - وبمعنی شتل ۴ حم
21536:لو س» با ناتی مجهول » مخنف بوسه
21537:است وبعربی قبله کویند ۱ - و بوسه کننده -
21553:بوسه شکستی - کناب از
21554:وبوسه کردن پرصدا باشد .
22787:۷ رگ : بوسیدن .
-- BQT balsan --
BQT_v1_pages.txt:17717:0 عمش ابوطالب با کاررانی بشام رفت . چون کاروان به بصری با فرب آن شهر رسید .
BQT_v1_pages.txt:20577:بلسان.؟ بروزن سرطان » نام درختی
BQT_v1_pages.txt:20587:بلسان بعد از لمحه‌ای مانتد دلمةٌ
BQT_v1_pages.txt:20590:دهن‌البلسان خوانند ؛ و موضعی که درخت بلان
BQT_v1_pages.txt:20593:و تخم آنرا حب‌البلسان کوبند. گرم و خشك
BQT_v1_pages.txt:25823:بشام - بر وزن سلام ؛ هر چیز نیره
```


## [2026-09-05T14:44:11.660Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== BQT balsan 20570-20600 ===\"; sed -n '20570,20600p' BQT_v1_pages.txt; echo \"=== BQT basham 25815,25835 ===\"; sed -n '25815,25835p' BQT_v1_pages.txt"
}
```


### [2026-09-05T14:44:11.724Z] TOOL RESULT

```
=== BQT balsan 20570-20600 ===
و شانان بدان سنکه اندازند . ۴
تلد ه ه با دال ابجد و حای هوزوح رکت
بلس ۹ ۷7۷
در فرهنگگ جپانگیری نام غله‌امت که از آن
هربسه بزند و دز آشها نز کنند و بعر یی عذص
خوانتد ۰ ودرسحاح‌الادوبه بمعتی تین ایض آمده
است که انجیرسفید باشد» و بلسن با زبادتی‌نون
بلسان.؟ بروزن سرطان » نام درختی
است مشهور درمصر . گوبند بمد. از طاوع‌شمری
نثتری که از آهن ساخته باشند بر ب رکث آن
بلعك
درخت فرو برند روغن از آن‌روان شود؛ با ینبه
جمم کنند» و بسنی کویند
شیشها در بر هرب رک یکه
نشتر زده اند بیاویز ند .
امتحان وی چنان ات 6
قطره‌ای برشیر کاو چکانند
بلسان بعد از لمحه‌ای مانتد دلمةٌ
پثیر سته شود » و بر آب چکانند و برهم زنتد
آب ماند هر نقنه گرد , و آنرا بعربی
دهن‌البلسان خوانند ؛ و موضعی که درخت بلان
آ»جاست باغ فرعون بوده است وا نرا عین‌الشمس
خواند؛و کوبند ازممجزء عیسی علیه‌السللام است؛
و تخم آنرا حب‌البلسان کوبند. گرم و خشك
است‌در دویم. کوفت رعشهرا نافع‌است» وبیدانجیر
نیز گفته‌اند .
بلساك . بکر اول و انی و سکون
ثالت و کاف » سیخ آهنی باشد که یکی آنرا
پپن کرده باشند برای نان از تنور جدا کردن -
و سیخ کباب را نیز گوبند - و پفتح اول و انی
پرستوك‌باشد وآنر! بمربی‌خطاف گونند ۵ ونم
=== BQT basham 25815,25835 ===
به پشت نوان برداشت* .
پش « بفتح ارل و سکون ثالی » موی
کردن وک کل اسب راگونند! - وطره‌ای که بر
سردستار و کم رگذارند و فش معرب آئست -
و نات وفرومایه از هرچیز باشد - وشبیفونظیر
و ماشدرا نیز کفته‌ادد ۴ - و بضم اول جفد را.
کونند ۴ وآن پرندم‌ایست نامبارگ و بکراول
مخف پیش باشد؟ .
بشام - بر وزن سلام ؛ هر چیز نیره
رتکه راگوشد ۱
یشان » بنتم اول » بررزن و عمنی‌چشان
ی
نوشته بودند بانال تقطه‌دار. ودر دوفرهنگهدیگی
- کفلهاتی گرد و یش و دم دراز بر وبال فریی و لاغر یفن
پوربپای جامی. «لنت نلمه» .
؟ ‏ رك : فتي ور : ص له از ده مولف. ۴ - ر: پشكه .
ط وق شقن  »‏ ظاعراً ميچيك از درسنی که صاحب برعان بهیتان داده
صحیم لیست چمخود اودر کلمهُ اعزار جشان» بعنی کرمةالبیناه میگوید معنی آن هزار کزاست
چدچشان بمعنی «کزه , باشد واگر اين دعوی صاحب پرها که میگوبد پثان « شان» است‌سحیح
اشدنلةکذرن لظکزر يچيك ستبکه هرد مسحفه کزه است وااملزت نم
, اوستا ۳2۳۵/04 ( پشت ) , پپلوی ۳۷15۳۸ . هندی باستانی ات۳۲5 , (قطاطویم‎ . ٩
```


## [2026-09-05T14:44:21.002Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '24810,24840p' MON_part1.txt"
}
```


### [2026-09-05T14:44:21.055Z] TOOL RESULT

```
بلده: (ه-)://:۱ (ع. بلدة] (۱.) واحد. بلد. 
شهر + ج. بلاد بلدان. ناحبه» زمین. 
لدیت: ۱۱۸0-۸۱ [ع.] (مسسص جه.) 
معرفت» شناسایی» آ گاهی؛ اطلاع. 
بلد به: (۵-)1۵01-1۷۷۸ ۱۱۵ [ع.] (ضن نشستت: ادتا 
ا) مونث ربلدی»: امور بلدبه. شهر داری. 
بلسان: ۷۵ (معر .] (۱.) (گا.) گیاهی از 
تيرة سدابیان که بصورت درختجه است و 
ذارای کاهای ت شاف هه اما 
این گیاه محتو ی مادة صمغی می‌باشند که در 
صورت خراش یا نیش حشرات این مادة 
صمغی زا خارج می‌شود؛ درخت للسان؛ 
ابوشام: بشام» بلسم مکه. درخت بلسان مکی. 
بلسم اسسرائیل» بلسن آغاجی؛ سلسان 
آغاجی» بلسان من شجرالب‌لسم. ضسح .. 


شم فرهنگ فارسی معین بلشویکك 


دانٌ این گیاه را حب البلسان نیز گویند و بنام 
بلسان در تداوی مصرف می‌شود. (گیا.) 
بلسان نام عام همه گیاهانی است که از آنها 
. استخراج می‌شو د. 
بلشو یک: 0۱516« [بالشو یک. بسیار؛ اکثر. 
چون پیروان لنین اکثریت را بدست آوردند» 
سدین ۳ نامیده شدند.] (ص.) طر فدار 
بلع: ات [ع.] (مص م.) فرو بردن» اوباشتن» 
اوباردن» فروخوردن» به گلو فرو بزدن. 
«تمساح‌اورا بلع کرد .0 
بلعچب: ادلمدهه [ع. - بوالعجب -
```


## [2026-09-05T14:44:31.642Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; ls site/pages/102.jpg 2>/dev/null; pdftoppm -f 102 -l 102 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg102 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


### [2026-09-05T14:44:34.761Z] TOOL RESULT

```
site/pages/102.jpg
total 31748
drwx------ 2 sfmqrb sfmqrb     4096 Sep  5 10:44 .
drwx------ 4 sfmqrb sfmqrb     4096 Sep  5 01:20 ..
-rw-rw-r-- 1 sfmqrb sfmqrb     4061 Sep  5 02:00 avestan.png
-rw-rw-r-- 1 sfmqrb sfmqrb     5971 Sep  5 02:13 baga.html
-rw-rw-r-- 1 sfmqrb sfmqrb   189420 Sep  5 02:15 bqt440_bottom.png
-rw-rw-r-- 1 sfmqrb sfmqrb   513902 Sep  5 02:15 bqt440.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   502834 Sep  5 02:02 bqt538_big.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    72705 Sep  5 02:02 bqt538_fn6.png
-rw-rw-r-- 1 sfmqrb sfmqrb    24595 Sep  5 02:02 bqt538_head2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    22593 Sep  5 02:02 bqt538_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb   207980 Sep  5 02:01 bqt538.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   282104 Sep  5 01:29 bqt733_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   669351 Sep  5 01:29 bqt733.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    17369 Sep  5 01:35 bqtv1_361_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb   470042 Sep  5 01:35 bqtv1_361.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   241161 Sep  5 01:36 bqtv1_398_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   482084 Sep  5 01:36 bqtv1_398.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   190109 Sep  5 01:35 bqtv1_399_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    53579 Sep  5 01:36 bqtv1_399_head2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1625 Sep  5 01:35 bqtv1_399_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb   510341 Sep  5 01:35 bqtv1_399.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    63555 Sep  5 01:43 build71.py
-rw-rw-r-- 1 sfmqrb sfmqrb     5214 Sep  5 02:23 build82a.py
-rw-rw-r-- 1 sfmqrb sfmqrb    53401 Sep  5 02:29 build82b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    19831 Sep  5 02:31 build82c.py
-rw-rw-r-- 1 sfmqrb sfmqrb    48417 Sep  5 10:19 build93.py
-rw-rw-r-- 1 sfmqrb sfmqrb     4811 Sep  5 02:00 bulca.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2950 Sep  5 10:15 c_anth.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2661 Sep  5 10:15 c_armonica.png
-rw-rw-r-- 1 sfmqrb sfmqrb    22149 Sep  5 01:51 c_belloth.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30227 Sep  5 09:50 crop_ambor.png
-rw-rw-r-- 1 sfmqrb sfmqrb    25024 Sep  5 09:50 crop_berijab_lat.png
-rw-rw-r-- 1 sfmqrb sfmqrb    39114 Sep  5 09:50 crop_berijan_ar.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65413 Sep  5 09:50 crop_persian_roast.png
-rw-rw-r-- 1 sfmqrb sfmqrb    23219 Sep  5 01:51 c_schyth.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3019 Sep  5 10:15 c_sus.png
-rw-rw-r-- 1 sfmqrb sfmqrb    38686 Sep  5 10:34 e0.95.json
-rw-rw-r-- 1 sfmqrb sfmqrb    58057 Sep  5 02:29 e0full.json
-rw-rw-r-- 1 sfmqrb sfmqrb     4446 Sep  5 02:23 e0.json
-rw-rw-r-- 1 sfmqrb sfmqrb    26175 Sep  5 10:38 e1.95.json
-rw-rw-r-- 1 sfmqrb sfmqrb   445959 Sep  5 01:37 hrn126_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1213019 Sep  5 01:37 hrn126.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   456157 Sep  5 01:37 hrn127_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1278807 Sep  5 01:37 hrn127.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    40966 Sep  5 01:40 mk67.py
-rw-rw-r-- 1 sfmqrb sfmqrb    58318 Sep  5 01:45 mk70.py
-rw-rw-r-- 1 sfmqrb sfmqrb    78619 Sep  5 02:02 mk73.py
-rw-rw-r-- 1 sfmqrb sfmqrb    68454 Sep  5 02:01 mk75.py
-rw-rw-r-- 1 sfmqrb sfmqrb    79383 Sep  5 02:19 mk78.py
-rw-rw-r-- 1 sfmqrb sfmqrb    52793 Sep  5 02:18 mk79.py
-rw-rw-r-- 1 sfmqrb sfmqrb    57729 Sep  5 02:31 mk81.py
-rw-rw-r-- 1 sfmqrb sfmqrb    58379 Sep  5 02:39 mk83.py
-rw-rw-r-- 1 sfmqrb sfmqrb    76819 Sep  5 02:39 mk84.py
-rw-rw-r-- 1 sfmqrb sfmqrb    25181 Sep  5 02:44 mk86.py
-rw-rw-r-- 1 sfmqrb sfmqrb    67712 Sep  5 10:03 mk87.py
-rw-rw-r-- 1 sfmqrb sfmqrb    66054 Sep  5 10:10 mk89.py
-rw-rw-r-- 1 sfmqrb sfmqrb    70790 Sep  5 10:04 mk90.py
-rw-rw-r-- 1 sfmqrb sfmqrb    48553 Sep  5 10:03 mk91.py
-rw-rw-r-- 1 sfmqrb sfmqrb    27206 Sep  5 10:38 mk95b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    39501 Sep  5 10:34 mk95.py
-rw-rw-r-- 1 sfmqrb sfmqrb    49433 Sep  5 10:35 mk96.py
-rw-rw-r-- 1 sfmqrb sfmqrb 18949704 Sep  5 02:30 mw1872.htm
-rw-rw-r-- 1 sfmqrb sfmqrb     3057 Sep  5 10:05 patch87.py
-rw-rw-r-- 1 sfmqrb sfmqrb    71589 Sep  5 10:41 pg100.png
-rw-rw-r-- 1 sfmqrb sfmqrb    68145 Sep  5 10:44 pg102.png
-rw-rw-r-- 1 sfmqrb sfmqrb    55169 Sep  5 01:30 pg67.png
-rw-rw-r-- 1 sfmqrb sfmqrb    57649 Sep  5 01:33 pg69.png
-rw-rw-r-- 1 sfmqrb sfmqrb    50966 Sep  5 01:33 pg69_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    77968 Sep  5 01:31 pg70.png
-rw-rw-r-- 1 sfmqrb sfmqrb    75801 Sep  5 01:29 pg71_300.png
-rw-rw-r-- 1 sfmqrb sfmqrb    71145 Sep  5 01:29 pg71.png
-rw-rw-r-- 1 sfmqrb sfmqrb   134140 Sep  5 01:44 pg72_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2377 Sep  5 01:44 pg72_afandi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    11769 Sep  5 01:47 pg72_fr2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2947 Sep  5 01:44 pg72_fr.png
-rw-rw-r-- 1 sfmqrb sfmqrb    49860 Sep  5 01:44 pg72.png
-rw-rw-r-- 1 sfmqrb sfmqrb    81180 Sep  5 01:47 pg73.png
-rw-rw-r-- 1 sfmqrb sfmqrb    56073 Sep  5 01:48 pg74.png
-rw-rw-r-- 1 sfmqrb sfmqrb   108877 Sep  5 01:51 pg75_400.png
-rw-rw-r-- 1 sfmqrb sfmqrb    20612 Sep  5 01:51 pg75_greeklatin.png
-rw-rw-r-- 1 sfmqrb sfmqrb    75134 Sep  5 01:51 pg75.png
-rw-rw-r-- 1 sfmqrb sfmqrb    66505 Sep  5 01:51 pg76.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65211 Sep  5 02:00 pg77.png
-rw-rw-r-- 1 sfmqrb sfmqrb   155334 Sep  5 02:00 pg78_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63822 Sep  5 01:59 pg78.png
-rw-rw-r-- 1 sfmqrb sfmqrb    59439 Sep  5 02:09 pg79.png
-rw-rw-r-- 1 sfmqrb sfmqrb    58953 Sep  5 02:08 pg80.png
-rw-rw-r-- 1 sfmqrb sfmqrb    99904 Sep  5 02:15 pg81.png
-rw-rw-r-- 1 sfmqrb sfmqrb    29321 Sep  5 02:20 pg82_bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    74477 Sep  5 02:20 pg82.png
-rw-rw-r-- 1 sfmqrb sfmqrb    56108 Sep  5 02:20 pg82_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   154129 Sep  5 02:25 pg83_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb     7123 Sep  5 02:26 pg83_apac.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4363 Sep  5 02:26 pg83_bohyah.png
-rw-rw-r-- 1 sfmqrb sfmqrb    67094 Sep  5 02:25 pg83.png
-rw-rw-r-- 1 sfmqrb sfmqrb    82358 Sep  5 02:23 pg84.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63329 Sep  5 02:25 pg85.png
-rw-rw-r-- 1 sfmqrb sfmqrb    31530 Sep  5 02:35 pg86.png
-rw-rw-r-- 1 sfmqrb sfmqrb    79874 Sep  5 09:47 pg87.png
-rw-rw-r-- 1 sfmqrb sfmqrb   134852 Sep  5 09:54 pg88_400.png
-rw-rw-r-- 1 sfmqrb sfmqrb    11747 Sep  5 09:54 pg88_e0spine.png
-rw-rw-r-- 1 sfmqrb sfmqrb    31391 Sep  5 09:55 pg88_join.png
-rw-rw-r-- 1 sfmqrb sfmqrb    98452 Sep  5 09:54 pg88.png
-rw-rw-r-- 1 sfmqrb sfmqrb    26700 Sep  5 09:54 pg88_spine.png
-rw-rw-r-- 1 sfmqrb sfmqrb   171528 Sep  5 02:45 pg89_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4628 Sep  5 02:45 pg89_ambor.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4924 Sep  5 02:45 pg89_berijan.png
-rw-rw-r-- 1 sfmqrb sfmqrb    80984 Sep  5 09:49 pg89.png
-rw-rw-r-- 1 sfmqrb sfmqrb    77182 Sep  5 09:48 pg90.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63799 Sep  5 09:55 pg91.png
-rw-rw-r-- 1 sfmqrb sfmqrb   157177 Sep  5 10:09 pg92_500.png
-rw-rw-r-- 1 sfmqrb sfmqrb     8494 Sep  5 10:09 pg92_avestan.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3476 Sep  5 10:09 pg92_pahlavi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    90918 Sep  5 10:07 pg92.png
-rw-rw-r-- 1 sfmqrb sfmqrb    93420 Sep  5 10:15 pg94.png
-rw-rw-r-- 1 sfmqrb sfmqrb    44047 Sep  5 10:16 pg94_sogd.png
-rw-rw-r-- 1 sfmqrb sfmqrb    49714 Sep  5 10:16 pg94_urvar.png
-rw-rw-r-- 1 sfmqrb sfmqrb    78178 Sep  5 10:11 pg95.png
-rw-rw-r-- 1 sfmqrb sfmqrb   163439 Sep  5 10:15 pg96_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72929 Sep  5 10:15 pg96.png
-rw-rw-r-- 1 sfmqrb sfmqrb   101597 Sep  5 10:41 pg99_400.png
-rw-rw-r-- 1 sfmqrb sfmqrb     8738 Sep  5 10:41 pg99_french.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65608 Sep  5 10:40 pg99.png
```


## [2026-09-05T14:44:38.531Z] TOOL CALL #36: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg102.png"
}
```


### [2026-09-05T14:44:38.912Z] TOOL RESULT

```

```


## [2026-09-05T14:44:38.910Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-05T14:44:48.138Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n '1,60p' tools/fetch_source.py"
}
```


### [2026-09-05T14:44:48.179Z] TOOL RESULT

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


## [2026-09-05T14:44:56.708Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; for u in \\\n \"https://en.wiktionary.org/wiki/بوسیدن\" \\\n \"https://en.wiktionary.org/wiki/buss\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/kussijaną\" \\\n \"https://en.wiktionary.org/wiki/برهنه\" \\\n \"https://en.wiktionary.org/wiki/βάλσαμον\" \\\n \"https://en.wiktionary.org/wiki/balsam\" \\\n \"https://en.wiktionary.org/wiki/بشام\" \\\n \"https://www.etymonline.com/word/buss\" ; do\n echo \"### $u\"; python3 tools/fetch_source.py \"$u\" --note \"page 102 verification (Bu / Bunai / Busma)\"; done"
}
```


### [2026-09-05T14:45:04.957Z] TOOL RESULT

```
### https://en.wiktionary.org/wiki/بوسیدن
/home/sfmqrb/git/rishe/data/verification/sources/web/ecf030988bc14718.txt
### https://en.wiktionary.org/wiki/buss
/home/sfmqrb/git/rishe/data/verification/sources/web/edfde12487c14c9b.txt
### https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/kussijaną
/home/sfmqrb/git/rishe/data/verification/sources/web/f3dfe25318cfbf71.txt
### https://en.wiktionary.org/wiki/برهنه
/home/sfmqrb/git/rishe/data/verification/sources/web/f4840fdfd469cbea.txt
### https://en.wiktionary.org/wiki/βάλσαμον
/home/sfmqrb/git/rishe/data/verification/sources/web/79ce64816fac35bc.txt
### https://en.wiktionary.org/wiki/balsam
/home/sfmqrb/git/rishe/data/verification/sources/web/a62165d7cd005ade.txt
### https://en.wiktionary.org/wiki/بشام
/home/sfmqrb/git/rishe/data/verification/sources/web/62e5f315114c257e.txt
### https://www.etymonline.com/word/buss
/home/sfmqrb/git/rishe/data/verification/sources/web/e63cb446f0b69a89.txt
```


## [2026-09-05T14:45:07.963Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; for f in ecf030988bc14718 edfde12487c14c9b f3dfe25318cfbf71; do echo \"##### $f\"; sed -n '1,120p' $f.txt | grep -v \"^$\" | head -60; done"
}
```


### [2026-09-05T14:45:09.396Z] TOOL RESULT

```
##### ecf030988bc14718
URL: https://en.wiktionary.org/wiki/بوسیدن
FETCHED: 2026-09-05T14:45:01Z
STATUS: 200
TITLE: بوسیدن - Wiktionary, the free dictionary
بوسیدن - Wiktionary, the free dictionary 
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
 Persian 
 Toggle Persian subsection 
 1.1 
 Etymology 
 1.2 
 Pronunciation 
 1.3 
 Verb 
 1.3.1 
 Conjugation 
 1.3.2 
 Related terms 
 1.4 
 References 
 Toggle the table of contents 
 بوسیدن 
 13 languages 
 Čeština 
 فارسی 
 Français 
 Magyar 
 Bahasa Indonesia 
 Kurdî 
 Кыргызча 
 Malagasy 
##### edfde12487c14c9b
URL: https://en.wiktionary.org/wiki/buss
FETCHED: 2026-09-05T14:45:02Z
STATUS: 200
TITLE: buss - Wiktionary, the free dictionary
buss - Wiktionary, the free dictionary 
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
 English 
 Toggle English subsection 
 1.1 
 Pronunciation 
 1.2 
 Etymology 1 
 1.2.1 
 Noun 
 1.2.1.1 
 Synonyms 
 1.2.2 
 Verb 
 1.2.2.1 
 Synonyms 
 1.2.2.2 
 Descendants 
 1.3 
 Etymology 2 
 1.3.1 
 Noun 
 1.4 
 Etymology 3 
 1.4.1 
 Noun 
 1.5 
##### f3dfe25318cfbf71
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/kussijaną
FETCHED: 2026-09-05T14:45:02Z
STATUS: 200
TITLE: Reconstruction:Proto-Germanic/kussijaną - Wiktionary, the free dictionary
Reconstruction:Proto-Germanic/kussijaną - Wiktionary, the free dictionary 
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
 Proto-Germanic 
 Toggle Proto-Germanic subsection 
 1.1 
 Etymology 
 1.2 
 Pronunciation 
 1.3 
 Verb 
 1.3.1 
 Inflection 
 1.3.2 
 Related terms 
 1.3.3 
 Descendants 
 1.4 
 References 
 Toggle the table of contents 
 Reconstruction:Proto-Germanic/ kussijaną 
 Add languages 
 Reconstruction 
 Discussion 
 English 
 Read 
 Edit 
 View history
```


## [2026-09-05T14:45:13.475Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; for f in ecf030988bc14718 edfde12487c14c9b f3dfe25318cfbf71 f4840fdfd469cbea; do echo \"##### $f\"; grep -n -A12 \"^ Etymology\" $f.txt | sed -n '1,80p'; echo; done"
}
```


### [2026-09-05T14:45:14.887Z] TOOL RESULT

```
##### ecf030988bc14718
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Verb 
69-
70- 1.3.1 
71- Conjugation 
72-
73- 1.3.2 
74- Related terms 
--
156: Etymology
157- [ edit ] 
158-
159- PIE word 
160- *bu 
161-
162- From imitative Proto-Indo-European *bu , compare Latin basium ( “ kiss ” ) , Welsh bus ( “ kiss, lip ” ) , and English buss ( “ kiss ” ) .
163-
164- Pronunciation
165- [ edit ] 
166-
167- ( Classical Persian ) IPA ( key ) : /boː.siː.ˈdan/ 
168-

##### edfde12487c14c9b
65: Etymology 1 
66-
67- 1.2.1 
68- Noun 
69-
70- 1.2.1.1 
71- Synonyms 
72-
73- 1.2.2 
74- Verb 
75-
76- 1.2.2.1 
77- Synonyms 
--
83: Etymology 2 
84-
85- 1.3.1 
86- Noun 
87-
88- 1.4 
89: Etymology 3 
90-
91- 1.4.1 
92- Noun 
93-
94- 1.5 
95: Etymology 4 
96-
97- 1.5.1 
98- Noun 
99-
100- 1.6 
101: Etymology 5 
102-
103- 1.6.1 
104- Noun 
105-
106- 1.6.2 
107- See also 
108-
109- 1.7 
110: Etymology 6 
111-
112- 1.7.1 
113- Verb 
114-
115- 1.8 
116- Anagrams 
117-
118- 2 
119- Estonian 
120-
121- Toggle Estonian subsection 
122-
--
124: Etymology 
125-
126- 2.2 
127- Pronunciation 
128-
129- 2.3 
130- Noun 
131-
132- 2.3.1 
133- Declension 
134-
135- 2.3.2 
136- Compounds 
--
169: Etymology 1 
170-
171- 5.1.1 
172- Noun 
173-
174- 5.1.1.1 
175- Derived terms 
176-
177- 5.1.2 
178- See also 
179-

##### f3dfe25318cfbf71
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Verb 
69-
70- 1.3.1 
71- Inflection 
72-
73- 1.3.2 
74- Related terms 
--
143: Etymology
144- [ edit ] 
145-
146- From *kussaz ( “ kiss ” ) +‎ *-janą . [ 1 ] 
147-
148- Pronunciation
149- [ edit ] 
150-
151- IPA ( key ) : /ˈkus.si.jɑ.nɑ̃/ 
152-
153- Verb
154- [ edit ] 
155-

##### f4840fdfd469cbea
62: Etymology 
63-
64- 1.2 
65- Adjective 
66-
67- 1.2.1 
68- References 
69-
70- 2 
71- Persian 
72-
73- Toggle Persian subsection 
74-
--
76: Etymology 
77-
78- 2.2 
79- Pronunciation 
80-
81- 2.3 
82- Adjective 
83-
84- 2.3.1 
85- Derived terms 
86-
87- 2.3.2 
88- Descendants 
--
165: Etymology
166- [ edit ] 
167-
168- Borrowed from Classical Persian برهنه .
169-
170- Adjective
171- [ edit ] 
172-
173- برهنه • ( bürehne ) 
174-
175- ( literary , poetic ) naked 
176- Synonym: چپلاق 
177-
--
186: Etymology
187- [ edit ] 
188-
189- From Middle Persian bl(ʾ)hnk' ( brahnag ) , [ 1 ] [ 2 ] from Proto-Iranian *bagnákah , with secondary - r -, from Proto-Iranian *bagná ( “ naked ” ) , [ 3 ] from Proto-Indo-Iranian *nagnás , from Proto-Indo-European *negʷ- ( “ naked ” ) ; see there for further information.
190-
191- Pronunciation
192- [ edit ] 
193-
194- ( Classical Persian ) IPA ( key ) : /ba.rah.ˈna/ 
195-
196- ( Dari, formal ) IPA ( key ) : [bä.ɾäɦ.ná] 
197-
198- ( Dari, formal ) IPA ( key ) : [bä.ɾäɦ.ná]
```


## [2026-09-05T14:45:25.857Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; echo \"#### buss\"; sed -n '190,240p' edfde12487c14c9b.txt; echo \"#### etymonline buss\"; grep -n -i \"buss\" e63cb446f0b69a89.txt | head -20"
}
```


### [2026-09-05T14:45:25.917Z] TOOL RESULT

```
#### buss
 References 

 6 
 Norwegian Nynorsk 

 Toggle Norwegian Nynorsk subsection 

 6.1 
 Etymology 1 

 6.1.1 
 Pronunciation 

 6.1.2 
 Noun 

 6.1.2.1 
 Derived terms 

 6.1.3 
 See also 

 6.2 
 Etymology 2 

 6.2.1 
 Noun 

 6.3 
 Etymology 3 

 6.3.1 
 Alternative forms 

 6.3.2 
 Noun 

 6.4 
 Etymology 4 

 6.4.1 
 Noun 

 6.5 
 References 

 7 
 Scots 

 Toggle Scots subsection 

#### etymonline buss
1:URL: https://www.etymonline.com/word/buss
4:TITLE: Buss - Etymology, Origin & Meaning
6:Buss - Etymology, Origin & Meaning 
21: Origin and history of buss 
23: buss (n.) 
25: "a kiss," 1560s; probably of imitative origin, as are Welsh and Gaelic bus "kiss, lip," French baiser "kiss" (12c., from Latin basiare ), Spanish buz , German dialectal Buss , Turkish bus , Persian busa , Hindi bosa .
28: buss (v.) 
30: "to kiss," 1570s, from buss (n.). Related: Bussed ; bussing .
32: Kissing and bussing differ both in this,
34: We busse our wantons, but our wives we kisse.
39: Entries linking to buss 
41: bussing (n.) 
43: "kissing," 1570s, verbal noun from buss (v.).
55: "Skiddo," she cried, "you stingy cuss," "You're looking for a jitney buss."...
85: Share buss 
89: https://www.etymonline.com/word/buss Copy 
92: <a href="https://www.etymonline.com/word/buss">Etymology of buss by etymonline</a> Copy 
95: Harper, D. (n.d.). Etymology of buss. Online Etymology Dictionary. Retrieved September 4, 2026, from https://www.etymonline.com/word/buss Copy 
98: Harper Douglas, "Etymology of buss," Online Etymology Dictionary, accessed September 4, 2026, https://www.etymonline.com/word/buss. Copy 
101: Harper, Douglas. "Etymology of buss." Online Etymology Dictionary, https://www.etymonline.com/word/buss. Accessed 4 September, 2026. Copy
```


## [2026-09-05T14:45:31.760Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; echo \"#### greek balsamon\"; grep -n -B2 -A10 \"Etymology$\" 79ce64816fac35bc.txt | sed -n '1,60p'; echo \"#### balsam en\"; grep -n -A8 \"Etymology 1$\\|^ Etymology$\" a62165d7cd005ade.txt | sed -n '1,60p'"
}
```


### [2026-09-05T14:45:33.548Z] TOOL RESULT

```
#### greek balsamon
160- βλᾰ́σᾰμον ( blắsămon ) — poetic 
161-
162: Etymology
163- [ edit ] 
164-
165- Of Semitic origin, borrowed from Hebrew בָּשָׂם ( bāśām , “ sweet spice, sweet smell ” ) , [ 1 ] the consonant sequence in Greek being explained as an attempt of rendering שׂ ( ś ) sounding back then [ɬ] ; the semantic development may later have been attached to Aramaic and Ancient North Arabian .
166-
167- Pronunciation
168- [ edit ] 
169-
170- ( Attic , etc. ) : 
171-
172- IPA ( key ) : /bál.sa.mon/ → /ˈβal.sa.mon/ → /ˈval.sa.mon/ 
#### balsam en
366: Etymology
367- [ edit ] 
368-
369- Borrowed from Latin balsamum , from Ancient Greek βάλσαμον ( bálsamon , “ balsam ” ) , of Semitic origin ( Hebrew בושם ( “ spice, perfume ” ) ); compare Old English balsam , balsamum ( “ balsam, balm ” ) , Doublet of balm and desman . Not related to balsa .
370-
371- Pronunciation
372- [ edit ] 
373-
374- ( UK ) enPR : bôlʹsəm , IPA ( key ) : /ˈbɔːl.səm/ 
--
783: Etymology
784- [ edit ] 
785-
786- From Old Norse balsamr , from Latin balsamum , from Ancient Greek βάλσαμον ( bálsamon , “ balsam ” ) .
787-
788- Noun
789- [ edit ] 
790-
791- balsam   c ( singular definite balsammen , plural indefinite balsammer ) 
--
858: Etymology
859- [ edit ] 
860-
861- From Malay balsam , from English balsam , from Latin balsamum , from Ancient Greek βάλσαμον ( bálsamon , “ balsam ” ) , of Semitic origin ( Hebrew בושם ( “ spice, perfume ” ) ).
862-
863- The word displaced balsêm , the loanword-cognate from Dutch balsem .
864-
865- Pronunciation
866- [ edit ] 
--
905: Etymology
906- [ edit ] 
907-
908- From Old Irish balsam(m) , balsaim(e) , from Latin balsamum , from Ancient Greek βάλσαμον ( bálsamon ) .
909-
910- Noun
911- [ edit ] 
912-
913- balsam   m ( genitive singular balsaim ) 
--
1024: Etymology
1025- [ edit ] 
1026-
1027- Etymology tree
1028-
1029- Proto-Semitic *buśm- 
1030- Hebrew בָּשָׂם bor. 
1031- Ancient Greek βάλσαμον ( bálsamon ) bor. 
1032- Latin balsamum lbor. 
--
1101: Etymology
1102- [ edit ] 
1103-
1104- Etymology tree
1105-
1106- Proto-Semitic *buśm- 
1107- Hebrew בָּשָׂם bor. 
1108- Ancient Greek βάλσαμον ( bálsamon ) bor. 
1109- Latin balsamum lbor. 
--
```


## [2026-09-05T14:45:42.633Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; grep -n -A12 \"^ Etymology\" 62e5f315114c257e.txt | sed -n '1,60p'; echo \"---- any Arabic section ----\"; grep -n \"Arabic\\|Persian\\|بشام\\|Commiphora\" 62e5f315114c257e.txt | head -30"
}
```


### [2026-09-05T14:45:42.697Z] TOOL RESULT

```
---- any Arabic section ----
1:URL: https://en.wiktionary.org/wiki/بشام
4:TITLE: بشام - Wiktionary, the free dictionary
6:بشام - Wiktionary, the free dictionary 
57: Arabic 
59: Toggle Arabic subsection 
69: بشام 
128: Arabic
197: Retrieved from " https://en.wiktionary.org/w/index.php?title=بشام&oldid=85315787 "
199: Categories : Arabic lemmas 
200: Arabic nouns 
201: Arabic masculine nouns 
202: Arabic nouns with basic triptote singular 
235: بشام
```


## [2026-09-05T14:45:44.601Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; sed -n '125,175p' 62e5f315114c257e.txt"
}
```


### [2026-09-05T14:45:44.645Z] TOOL RESULT

```
 From Wiktionary, the free dictionary

 Arabic
 [ edit ] 

 Noun
 [ edit ] 

 بَشَام • ( bašām )  m 

 alternative form of بَيْلَسان ( baylasān ) 

 Declension
 [ edit ] 

 Declension of noun بَشَام ( bašām )

 singular

 basic singular triptote 

 indefinite

 definite

 construct

 informal

 بَشَام 
 bašām 

 الْبَشَام 
 al-bašām 

 بَشَام 
 bašām 

 nominative

 بَشَامٌ 
 bašāmun 

 الْبَشَامُ 
 al-bašāmu 

 بَشَامُ 
 bašāmu 

 accusative
```


## [2026-09-05T14:46:03.787Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"-- NYB brahn --\"; grep -n -i \"brhnk\\|brahn\\|barahn\" NYB_vol2_glossary.txt NYB.txt | head; echo \"-- SKT balm/balsam --\"; grep -n -i \"^balm\\|^balsam\\|balsamum\" SKT.txt | head; echo \"-- AFA balasan --\"; grep -n \"بلسان\\|بلسم\" AFA.txt | head; echo \"-- AFM --\"; grep -n \"بلسان\\|بشام\" AFM_pages.txt | head; echo \"-- FVQ --\"; grep -n -i \"balsam\\|bashām\" FVQ.txt | head"
}
```


### [2026-09-05T14:46:03.889Z] TOOL RESULT

```
-- NYB brahn --
NYB_vol2_glossary.txt:1029:brihčnak [blyhyn’k] one who destines fate 7722, | brihčnišn [blyhynšn'] the act of destining fate, predestination, destiny 14!?. 16? (gl. with apäyet butan, v. apäyistan). 69°. — Paz. brehinešn (birhinasn, barahnašni). brihčnitan l. to destine, to predestinate, of Ohurmazd 36%, 41"; mà hakar-am hac apargar nč brihénit ēstēt kū perhaps it has not been predestined for me (from =) by Fate 137-8; 1319? with inf. — 2. to create: brihčnit u dāt 77%; with hac ‘from’ of the matter from which Q93.6.7.12 9033.17.23. 945.25—26, 9518, 106%. = Paz. brehinidan, Skr. v. (vi-)nir-md-, srj- (Mx, SGV). - Den. of brih.
NYB_vol2_glossary.txt:6474:barahnašni: brihēnišn
-- SKT balm/balsam --
1357:Balm.  (F.-L.-Gk.)  A  modified  ipell- inf; ;  M.  E.  ikiume.  —  O.  F.  hausme.  -■  L. baisamum.'^Gk.  &^(ra^v,  fragrant  resin of  the  /lAXutt/iOf,  or  bal&.im-trcc.  Prob. Semitic;  d  Heb.  Msdm,  balsam.
1358:balsam.  (L.  — Gk.)  L.  dalsamum ;  as ■bove.
1606:balm,  a  child.  (E.)    M.  E.  *arw.   A.S.
22850:balm— balsam, barb  (^i) — beard, base— basis.
-- AFA balasan --
-- AFM --
-- FVQ --
```


## [2026-09-05T14:46:04.506Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"-- ARY bus --\"; grep -n \"بوسیدن\\|بوس\" incoming/ARY/ARY_pages.txt | head -10; echo \"-- ARY berehne --\"; grep -n \"برهنه\" incoming/ARY/ARY_pages.txt | head -5"
}
```


### [2026-09-05T14:46:04.588Z] TOOL RESULT

```
-- ARY bus --
3910:مس بوس» بوسه» پرسیدن / ۱۳۵
4489:فارسی (2885]4۸): پالیز, فالیز, جالیز, پردیس (به چم "باغ" ابوستان)
8335:۲ چم این واژه در زبان پرنانی: اخم‌آلود» عبوس. 9 دا
-- ARY berehne --
```


## [2026-09-05T14:46:10.852Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '3895,3925p' incoming/ARY/ARY_pages.txt; echo \"--- latin index ---\"; grep -n -i \"BUS\\b\\|BU \\|kiss\" incoming/ARY/ARY_latin_index_pages.txt | head -10"
}
```


### [2026-09-05T14:46:10.915Z] TOOL RESULT

```
لا ((ل7مل: 8 ,710 ,ال روسی (554(0): 871 ,817 ,87
فرانسه (7677ق۳8): 35 ,318 چکه (4ل0220): 7 بلاق
اسپانیایی (4ل8۳۸2]8): ات5 صربی (4ل887814): 71
ایتالیایی (لفتم7). 285888 بظ باتا۴ بوهمی (1ل80/78(/14): 7
رومانی (۸/۸/1۸(۷). ۴71 ,[5 اسلواکی (87.0144): 7 8 8
پرتغالی (۳07701282): 3 ند | لیترانی (040/40ب077: ات8 ,803
گوتبکد (0071710): 1۸ لتونی (لتی) (/۸4771۵): ار
ایسلند یکهن (5010/۸7/00 صان): پروسی کهن (28-3514(۷ 00): ,ات80
30 ری ند ناراد
ساکسونی گهن ((54240 صا0): 21 ایرلندی کهن (للولق/ 012): تاتا87 ,3 17ناظ
20 ولزی (لاع#): 802
[pdf page 134]
نج
مد
گررا ی
مس بوس» بوسه» پرسیدن / ۱۳۵
برتوئی (87270(0): ,ف257 3 (85) :۸۸0027213
آلبانی (1۸2لمقلم): 857 63536 تاه
1 (85) :010/3
پسگشت‌ها 5 2 (83) 7
6 ۶00/00 9 (88) 0
2
ککد (7۶2) :28
بادداشت: ی ۱
در اکثر زبان‌های هند و آروپایی برای صرف فعل (کارواژ) "بودن" از دو واجریشه‌ی -88* و -8871* هم لاد
می‌شود (بازگشت به: هست). ا
لانین (47100ا)(شاید) ,381510 1
ا ند ۱ نا تونی (لتی) (/11۸مل): ادا دا ۱
فرانسه (۳/82۸/67)(شاید) ادن ۱3۹ اپرلندی میانه (ول1 ها21102): 215
۱ اسپانیایی (52015) (شاید) 8590 ,802 6
۱ ابتالیایی (/۸ال17۸)(شاید) ای ۱ ولزی (3ل8ا): 218
--- latin index ---
207:SHEL 5 92 (She oly CoV gury}) CENTUM pr SUELS 9 (BU 592k gata
221:22 GAbUs fark Wyte gp! ly Yas (MALLORY, 56-63) Sgr gerd ke Cur
309:pens Ob ysl y sta Kole gaat y2 (COGNATE) ay ar slrosly saan bus
722:BUS HS tle Db 19 (IK phates 4) alas} yea pb GeSlyagey ygelctleel OT
800:Bu lbs y(TOCHARIAN A) A os jib ol Janta cation pgs 05g 1 SUL 5 cx!
1045:999° Fi93 957 es) dle BUS pas Jp 05 IG yp Selon gh, py HT»
1052:| trees LT AOU ue seskutCib ses pally phubus
1088:SNA 9 pa tt MET BU gp 92 9 Sh Sy Cool od SF shee bade slat gl ,
1295:BF pp MEAN jet 4 S46 39 WEL5 gal Oke ably 0245 9 3b5 wll de Gebel bus |
1543:ABU phyla UT fly col
```


## [2026-09-05T14:46:19.903Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"بوسه\" incoming/ARY/ARY_pages.txt | head -10; echo \"---\"; awk 'NR>=3850 && NR<=3912' incoming/ARY/ARY_pages.txt | grep -n \"pdf page\""
}
```


### [2026-09-05T14:46:21.654Z] TOOL RESULT

```
3910:مس بوس» بوسه» پرسیدن / ۱۳۵
---
26:[pdf page 133]
57:[pdf page 134]
```


## [2026-09-05T14:46:32.039Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== BQT buse ===\"; sed -n '21530,21560p' BQT_v1_pages.txt; echo \"=== BQT berehne ===\"; sed -n '32020,32060p' BQT_v1_pages.txt"
}
```


### [2026-09-05T14:46:32.095Z] TOOL RESULT

```
=== BQT buse ===
نود دنه _ سس وزن روزشه . میمون را
7
۴ - شاکرد تو میباشم
۴ - مخقف بواوزار هه مواقرار.
۵ بوزرجمهر - رك : بزرگمهر .
۱ رك ؛ بوز .- ۳۷۷ -
لو س» با ناتی مجهول » مخنف بوسه
است وبعربی قبله کویند ۱ - و بوسه کننده -
رامر بپوسیدن هم‌هست- و بائانی ممروف سخنی
- وفروننی را گویند .۶
نوستان افر وز- کلی اس 9
آنرا تاج خروس کویند بسبب شباهتی که بدان
«أرو ۳
بوستان گل نمای- کنابه‌از آسمان
هاشث .
توسحاق » با حای حطی بروزن
روستاق: عطلاخه‌ای باشنف ۴ ونام‌کانی است ۵ زحمله
کانهای فیروزة نیشابور که فیروزه آنرابوسحافی
وبواسحاقی هردو میگوبند ۴ -وبسحاق اطعمه را
بتحتانی ۳ 7 زده.نام 1 تیاو ره
- کیلکی علاط .
بوشاصب
دوازده مقام موسیقی ۵ .۳
بوسه شکستی - کناب از
وبوسه کردن پرصدا باشد .
و یه بفتح اود و کسر نانی و سکون
شین قرشت » بمعنی تفدیر باشد کد قدرت داشئن
است - و بسکون انی کر و فر و خود نمابی را
کوبند ۱ - و منم اول و کسر انی ۰ بمعنی
هستی وبودن وبعربی کون خوانند ۷ - وسکون
نانی شیافی باشد که از دربند می‌آورند و آن را
=== BQT berehne ===
فردوسی طوسی» گفتار رستم باسفندیار .
و کوبروارمفرب بقزوین وساوهطول آن ازهشرق‌بمغزب (غر قآ باد تا فدروژ کوه) ۲۹۰ وعرض‌ازشمال
بجنوب (ا زگردنة کندوان تا درباچهُ ق) *۱۲ کیلومتر و صساحت آن فربب ۳۱۰۰۰ کیلو متر
مربع است. شهرتهران پابئخت ابران دربن ابالت است. درفدیم نهران عکیاز فربه‌ه‌ای کوچكری
بوده» اصطخری وابن‌حوفل ومسمودی نام‌تهران را در کتب خود ذ کر کرده‌اند. «جقرافای سیاسی .
کیهان ۳۱۱- ۳۹۹. درسال ۱۲۱۰ آغا محمدخال قاجار آنرا باشخت ابران فرارداد . جمیت
نپران قوب ۱۰۰۰۰۰۰ نن است. راجم‌بوجه اشتفاق نهران وسور مختلف تلفظ و کتابت آن» رك:
بقبه درصفحةٌ ۰۳۹تهمك - بر وزن لك لك , مصفر تهم
اسق بت و بمعنی دویم تهك ‌‌ حست که برهنه
وعربان - وتهی وخالی باشدا .<
بهمو درس - بنتح اول نامشخصی است
که او وا تهمورث دیو ند می خوانند؟ ت ورنفی
تهمیشه » بر وزن اندیشه . نام
پشته است در دارالم‌رز نزديك‌به بشه نارون؟ .
هو - منم اول و نانی » بروزنوهعنی
تفواست که آب دهن - وآب دهن انداخثن باشد
ویک اول مخمقف تسهواست ۹ وآن برنده‌است
خبیه بکيك. ایک نکوچکتراست از کیال
4 و بالا » بیمنی زیر و زبرباشد که
تحت و فوق است - و کنابه از اضطراب
و وف تپك رتپيك (ذیل: نهی).
وبیتراری هم ست وحصول مطلس دو سرامرد
باق فزکلاسک وا
ی - بکسر اول و نانی و سکون
تحتانی نام شپری و مدینه است* - و یمعنی
خالی۷ هم‌هست که در مقابل پراست۸ » و باین
معنی بفتح اول وضم اول هم گفنه‌اند .
بهیته - بر وزن همشه , نام شهری
است که فربدرن پوسنه و دام جر آنجا
می بوده . ۱
نهیگاه - ما ین شکم وپهلو را کویند.
تهی و تهاكث ۰ با ای فرشت و ها
بروزن زمی و فلكث» این‌لفت ازاتباع است بمعنی
برهنه و عربان - وتهی وخالی ۰
۴ در اوستا ۱۲۷۳2 31100[ ؛ جزو
سفق نمعدی يك فسم -ت.
زب
۵ سرله: نهو.
ا ورف *سشق ۰ ۰
۵ تهمورث - رك : نهمورسی .
شه ارصفحه ۵۳۸
```


## [2026-09-05T14:46:42.786Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"بر هنه\\|برهنة\\|برهنه\\|برهند\\|بربنه\" BQT_v1_pages.txt BQT_v2_pages.txt BQT_alt_v1.txt | head -20"
}
```


### [2026-09-05T14:46:42.851Z] TOOL RESULT

```
BQT_alt_v1.txt:2604:خاصه انگلیسپا » در طول چند ماه تسلط برهند ما غذ و ادله‌ای برای این 
BQT_alt_v1.txt:4885:مولف‌جهانگیری گوید: «باستان ... دوعمنی دارد : اول کهنه وگذشته وقدیم ودبربنه را گویند 
BQT_alt_v1.txt:60356:وبرهنه و عربان هم هت . 
BQT_alt_v1.txt:60465:است ت وب نمفت دوم تهك حم هست که برهنه 
BQT_alt_v1.txt:60499:برهنه و عربان - وتهی وخالی ۰ 
BQT_v1_pages.txt:1911:خاصه انکلیسپا » در طول چند ماه تسلط برهند مآخذ و ادله‌ای رای این
BQT_v1_pages.txt:32028:اسق بت و بمعنی دویم تهك ‌‌ حست که برهنه
BQT_v1_pages.txt:32053:برهنه و عربان - وتهی وخالی ۰
BQT_v2_pages.txt:7873:  ‫باط و متاع ‪ -‬گرفتن ناخن وستردن موی ‪« :‬نگوبی که‌دوبدن و برهنه بودن و ناخن ناچیدن‬
BQT_v2_pages.txt:9514:                                                                     ‫برهنه تنی بکدرم وکام‬
BQT_v2_pages.txt:23196:                  ‫تالت هم بنظر ا مده است ‪۰‬‬       ‫رضم‬                     ‫کردن ‪ -‬وبرهنه شدن باشد ‪.‬‬
BQT_v2_pages.txt:23535: ‫چون‌صابون کف بآروردجامه بدان شویندخصوصاً‬                     ‫گوبند ‪ -‬وم اول تهی دست وبینوا ‪ -‬وبرهنه‬
BQT_v2_pages.txt:31789:     ‫کدایی میکرد ما بکار کسی می پرداخت و نادان و برهنه بود وشمیده گران و سکداران ومسمون‬
```


## [2026-09-05T14:46:48.739Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"بره ‌\\|^بره\\|برهمن\\|برهوت\" BQT_v1_pages.txt | head -10"
}
```


### [2026-09-05T14:46:48.791Z] TOOL RESULT

```
118:برهان قاطم متعلق بکتابغان؛ ملی نپران (خم ۱) مورخ بسال ۱۰۶۳ هجری
1670:برهان وحاشیه .ابر اهیم پور داود
1885:برهان‌رااصلاح کر ده ازروی خود دسانیر آسمانی‌ارزش ومعنی [ نبا رانگاشته
1970:برهبةٌ آنپاست منبع ومأخذ اوچه بوده است ؟ ممکن است تصور شود که او
2764:برهان متفاوت است» زیرا که حروف اولرا باب قرارداده وحروف آخررا
2804:برهان‌قاطع وانتقادات عدیده شدهاست. مداز [ نکه‌در او اخر قرن
2878:برهان قاطم> و «نیخ‌نیز > و د«تیخ تيزتر > وغیر آنبا مشتمل بررد وانتقاد
3178:برهان تقل شده است ؟ :
3368:برهان و حواشی آن . ۷ - فاموی کتاب مقدس : تارح . ۰
3548:برهان جامع
```


## [2026-09-05T14:47:02.836Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"برهنه\" incoming/BQT/BQT_v3_pages.txt incoming/BQT/BQT_v4_pages.txt incoming/BQT/BQT_v5_pages.txt 2>/dev/null | head -20"
}
```


### [2026-09-05T14:47:02.908Z] TOOL RESULT

```
incoming/BQT/BQT_v4_pages.txt:473:برهنه [ظ ۳ نبهره] بود و مردم دون همت را کویند که همتی ماخ دارد .»:
incoming/BQT/BQT_v4_pages.txt:2176:سبك نيك زن سوی چاکر ( خانه ) دوید برهنه باندام من ( او ) در مخید ‏ >
incoming/BQT/BQT_v4_pages.txt:4599:فرمود خاك بربزید در نیم روز پرخاکش کردند. | سروپا برهنه و بیپوش و مت الهی را کوبند -
incoming/BQT/BQT_v4_pages.txt:13978:بروزن سمندر, بمعنی آنطرف وآنجاب و آسو | قرشت » بمعتی برهنه وعریان باشد ؛ وبضم اول
incoming/BQT/BQT_v4_pages.txt:13999:۸ -ورپوشنه (ه.م.) ۸ - «ورت بالفتح برهنه که « رت * نیز کویند » وظاهراً
incoming/BQT/BQT_v4_pages.txt:19069:«داود ازپی اوزاستر شد, هوازی نگاه کرد زن اوریا را بدید برهنه برسن حوض ایستاده اسرسرای
incoming/BQT/BQT_v3_pages.txt:3918:و برهنه دندان و صاحب قوت و زورمند باشد »
incoming/BQT/BQT_v3_pages.txt:7420:‏سر برهنه که نا بهد برم‎ - ۴
incoming/BQT/BQT_v3_pages.txt:10676:چو برهته و برهنه‌جو و بعربی ‎OM year Toke‏
incoming/BQT/BQT_v3_pages.txt:15860:‏(هم) « غوشت . برهنه ‎ay‏ مادرزاد . رودکی (سمرقندی ) گفت:
incoming/BQT/BQT_v3_pages.txt:25962:‏چوکاسموی گیاهان او برهنه زب رکه چو شاخ بید درختان او تهي از بار.»‎
incoming/BQT/BQT_v3_pages.txt:32498:۴ - دختر رز برهنه آونگان
incoming/BQT/BQT_v3_pages.txt:32703:‎٩‏ - پای پاکیزه برهنه به ببی
incoming/BQT/BQT_v3_pages.txt:46712:‏برهنه کرده باشد .
incoming/BQT/BQT_v3_pages.txt:47405:‎. ‏است و برهنه همچو کتگار‎ ST
incoming/BQT/BQT_v3_pages.txt:49668:- و بمعنی برهنه و عربان باشد ‏ - وسگه‌عاده
incoming/BQT/BQT_v3_pages.txt:50878:ست که بمعنی برهنه و عریان باشد .
incoming/BQT/BQT_v3_pages.txt:51006:‏- لفت ‎em‏ اول ‎iat‏ ور و برهنه سمل شود. ‎fF‏ رك : ح آخرصفحه قبل .
```


## [2026-09-05T14:47:08.431Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"بر هنه\\|برهنه:\\|برهنه (\\|برهنگی\" MON_part1.txt | head -10; echo \"--- around 'برهنه' generic ---\"; grep -n \"برهنه\" MON_part1.txt | head -20"
}
```


### [2026-09-05T14:47:08.531Z] TOOL RESULT

```
26163:ما کبان‌ها که دارای گردنی بر هنه و گوشتی و 
27498:پابر هنه: )۲2۱92 0۸-.ج (ص مر .) 
47531:جرده: (م-)2[ (.) برهنگی. 
52077:بر هنه. 
94136:عاری: 217 [ع.] (افا. ص.) بر هنه» لخت؛ ج. 
95905:عریان: 2 (ع.] (ص.) لخت» بر هنه. 
99049:( کم.) (ف.) لخت» بر هنه. 
--- around 'برهنه' generic ---
4856:کاذب است. پروتوپلاسم آنها برهنه و بدون 
10979:ماهیی است بزرگ و سر برهنه که دهانی 
27536:پاپتی: آا«م5م (ص‌مر.) (عم.) پا برهنه» یکث 
27905:کف پایش طویل و برهنه و انگشتانش نیز 
29422:بی‌خورش» ساده» تنها: نان پتی. برهنه 
33343:نباشد. بی‌ارزش» ببهوده. از برهنه پوستین 
33659:بهلوان را با زدن کمان برهنه کند بعنی تمام 
36293:طریق که با سر برهنه یکك گوش را به دست 
38040:بیراسته شدن. برهنه شدن. (امص.) بی‌زنی. 
38056:برهنه کردن. تیغ برکشیدن (غم.) (اسص.) 
41605:برهنه کردن. 
45326:برهنه» عریان. 
52171:کفش راه رود؛ با برهنه) ج. حفاة (حفات). 
53305:حسر : 11857 [ع.] (مص م.) برهنه کردن. 
66050:از اسب و مانند آن. برهنه شدن. ظاهر کردن 
66575:برهنه» لخت» عربان. تهی» خالی. 
75410:گل‌هایش کاملا برهنه و دون جام و کاسه و 
76441:سرش برهنه است؛ آنکه کلاه و دستاری بر
```


## [2026-09-05T14:47:10.469Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '52070,52082p' MON_part1.txt"
}
```


### [2026-09-05T14:47:10.526Z] TOOL RESULT

```
دریابنده را حاسه و جمع آنها را حواس 
نامند. (شفا ۲۹۷۵۲۹۵:۱) فرع. سج.) 
حاسد: 4 (ع.] (افا.) رشکک برنده؛ 
رشکین. بدخواه» بداندیش» بدسگال؛ ج. 
اد حسده. (غم.)» حاسد ین. 

حاسر: و۳( [ع.] (رص.) بی‌زره» بی خود. 
بر هنه. 

حاشا: 545« [ع.] (ق. کلم انکار) هرگ 
مبادا؛ نه چنین است. (ف.) (.) انکار. دبوار 
حاشا بلند است: به سهولت می‌توان موضوع 
ر انکار کرد.
```


## [2026-09-05T14:47:24.687Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 tools/fetch_source.py \"https://abadis.ir/fatofa/بلسام/\" --note \"page 102, Busma root: is Persian بلسام a real word (Dehkhoda/Moin)\"; f=$(ls -t data/verification/sources/web/*.txt | head -1); echo \"$f\"; grep -n \"بلسام\\|بلسان\" \"$f\" | head -20"
}
```


### [2026-09-05T14:47:27.704Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/bef6213ad76b57ce.txt
data/verification/sources/web/bef6213ad76b57ce.txt
1:URL: https://abadis.ir/fatofa/بلسام/
4:TITLE: بلسام - معنی در دیکشنری آبادیس
6:بلسام - معنی در دیکشنری آبادیس 
10: بلسام
16: بلسام. [ ب ِ ] ( ع اِ ) برسام. ( منتهی الارب ). برسام ، که علت و مرض مشهوری است. ( از ذیل اقرب الموارد از لسان ). رجوع به برسام شود.
```


## [2026-09-05T14:47:32.938Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n '6,60p' data/verification/sources/web/bef6213ad76b57ce.txt"
}
```


### [2026-09-05T14:47:32.979Z] TOOL RESULT

```
بلسام - معنی در دیکشنری آبادیس 

 دیکشنری مترجم بپرس 

 بلسام

 دنبال کنید 

 لغت نامه دهخدا

 بلسام. [ ب ِ ] ( ع اِ ) برسام. ( منتهی الارب ). برسام ، که علت و مرض مشهوری است. ( از ذیل اقرب الموارد از لسان ). رجوع به برسام شود. 

 پیشنهاد کاربران

 پیشنهادی ثبت نشده است. شما اولین نفر باشید
 + عکس و لینک 

 دیکشنری آبادیس

 آبادیس از سال 1385 فعالیت خود را در زمینه فن آوری اطلاعات آغاز کرد. نخستین پروژه آبادیس، سایت دیکشنری آبادیس بود. دیکشنری آنلاین آبادیس از ابتدا تاکنون تغییرات بسیاری کرده و ویژگی های مختلفی به آن اضافه شده است. آبادیس افزونه ای کاربردی برای مرورگرهای فایرفاکس و کروم و اپلیکیشن موبایل طراحی کرده است که میتوانید از لینک های بالا دانلود کنید. دیکشنری آبادیس شامل بخش هایی نظیر دیکشنری به زبان های مختلف از جمله انگلیسی، فارسی، عربی و همچنین بیست دیکشنری تخصصی با تلفظ انگلیسی و آمریکایی، ترجمه مخفف و کلمات اختصاری، مترجم آنلاین متن، لغتنامه دهخدا، فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راهنمای انتخاب اسم و ... می باشد. 

 لینک ها 

 حقوق این سامانه وابسته به دیکشنری آبادیس می باشد. 

 استفاده از نوشتارهای این دیکشنری، با ذکر منبع، آزاد است. 

 © 2006-2026 abadis.ir
```


## [2026-09-05T14:47:51.817Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"-- LEW --\"; grep -n \"balsamum\" LEW_1910.txt | head -5; echo \"-- LAT --\"; grep -n \"balsamum\" LAT.txt | head -5; echo \"-- WEB balsam --\"; grep -n -i \"^balsam\\b\\|balsamum\" WEB_vol1.txt | head -5; echo \"-- FSD --\"; grep -n -i \"balsamum\" FSD_vol1.txt | head -3"
}
```


### [2026-09-05T14:47:51.932Z] TOOL RESULT

```
-- LEW --
-- LAT --
899:ralem ent en parenthese, dont le sens est "et la chose se serait passee ainsiababalsamum
909:ababalsamum,—! n.: forme vulgaire pour opobalsamum (emprunt de la 1.
6822:balsamum,-! n.: baume, et "baumier". Emprunt au gr.paXoap.ov dont
-- WEB balsam --
15416:bal/ly-hoo”, n. [after Ballyhooly, village in County Cork, Ireland.]} F 1. loud talk; noisy uproar. (Cot oa s _2. loud, exaggerated, or sensational adver- — tising or propaganda. [Colloq.} bal’/ly-hoo”, v.t. and v.i. ballyhooed, pl., p ballyhooing, ppr. to advertise or sponte 9 sensational, showy methods. [Colloq] bal’ly-rag, v.t. to bullyrag. {Obs.| ae balm (bim), n. (ME. baume; OFr. basme balsamum, from Gr. balsamon, bals: } 1. an aromatic gum resin obtained from — certain trees and used as a medicine; ba! o 2. any fragrant ointment or aromat: for healing or anointing. Š 3. anything which heals, soothes, o: gates pain or mental distress. 3 4. in botany. the name of several plants, particularly of the herb Me: cinalis. balm, v.t. 1. to anoint with balm, í thing medicinal. [Obs.| 2. to soothe; to mitigate: to chaic.] bal-ma-caan’ (-kan’), n. [after Inverness, Scotland.] a loose raglan sleeves. Eo balm’ apple. same as balsam balm/i-f¥, v.t. to rend a bälm’i-ly, adv. in a b: bälm’i-ness, z. the q
15423:_ resting on cylindrical floats. bal’/sim, n. [AS. balsam; L. balsamum, from
15426:BALSAM needles and cone
15428:balsam of Peru; a product of a tree grow AE; k G n in tropical America (Myroxylon eae: used as an expectorant and stomachic. balsam of Saturn; an ointment compounded f acetate of lead dissolved in turpentine and ey Pane che oduct of
15439:2. containing or yielding balsam. bal-sam/ic, n. a soothing or demulcent medi- Cine, of a smooth and oily consistency. bal-sam/ic-Al-ly, adv. in a balsamic manner. bal-sim-if/ér-ous, a. [L. balsamum, balsam, and ferre, to bear.] producing balsam,
-- FSD --
34476:balm  of  a   thousand  flowers.  [   <   OF.  bausme,  <   L.  bal samum;  see  balsam,  n.]  balmef;  baulmct;  haumf. —   Abraham’s  balm,  the  chaste-tree.— balm'sap"ple,  n. See  balsam-apple,  under  balsam.— b.^crlcket,  n.  A European  cicada  ( Cicada  orni).—  b.  of  Gilead.  1.  A   small Oriental  evergreen  tree  ( Balsamodcndron  or  Commiphora opobalsamum,  or  B.  gtleadense)  of  the  myrrh  family  (Bur- seracex),  or  an  aromatic  reslnou3  exudation  obtained  from It  and  formerly  held  In  great  repute  in  medicine,  b.  of Mecca*;  balsam  of  Gilead*.  2.  The  American  balsam- flr  (Abies  balsamed)  or  the  balm  obtained  from  it.  o'po- bal"sam*.  3.  The  cultivated  balsam-poplar  ( Populus balsamifcra.  var.  candicans ).  4.  Anything  that  palliates, alleviates,  or  cures  grief  or  pain.  o.  [Local,  U.  S.l  Whisky distilled  without  government  license  —   b.  of  heaven,  the California  laurel  —   bastard  b.,  any  plant  of  the  genus  Me- Uttls of  the  mint  family  (Menthacex) .—  Molucca  b.,  a   curi- ous garden  flowering  plant  (Moluccella  Ixvis)]  shell-flower. See  Moluccella.  #   ,   „
34500:Bals.,  a&br.  Balsamum  (balsam),  Balmorals.  ... bal'sa,  1   bei'se;  2   bal'sa,  n.  [Sp.]  1.  A   tropical  Ameri- can tree  ( Ochroma  lagopus )   of  the  mallow  family (Afnfrace^),  with  very  light  wood,  called  corkwood. 2.  A   sailing  raft  made  of  Ught  logs  fastened  together by  a   platform,  or  (in  later  forms)  of  inflated  skins  and metal  cylinders.  3.  A   catamaran.
34566:bodies.  [   <   L.  balsamum,  <   Gr.  balsamon,  balsam-tree.]  _
```


## [2026-09-05T14:48:00.011Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"bōsīdan\\|bosidan\\|bōs-\\|bws-\" CHEUNG.txt | head; echo \"----\"; grep -n \"‘to kiss’\\|to kiss\" CHEUNG.txt | head -10"
}
```


### [2026-09-05T14:48:00.075Z] TOOL RESULT

```
2159:*PARTHIAN: bws- (inch.) ‘await, wait for, expect’ || (+ *pati-) pdbws- ‘to desire, 
2303:united, composed’, MMP hmbws-, BMP hanbws- /hambus-/ (inch.) ‘to come into 
34407:hmbws-, 17 
35188:hanbws- /hambüs-/, 17 
36030:bws-, 14 
36218:pdbws-, 14 
40849:bosidan/bos-, 15 
----
2160:yearn’ || (+ *ham-) ’mbwy- ‘to kiss’ = Ghilain: 65, 80 | DMMPP: 118a, 269a, 39a 
2181:*NWIR: NP bösidan/bös-, Abyan. busoya/bus-, Khuns. bus-/busa ‘to kiss’, Ham. 
2182:busayän/bus- ‘to kiss, embrace’, NP bös(ah), Kurd. (Kurm.) bösa (m.), Qohr. busa, 
2189:*MISC: (+ *ham-) Arm. (LW) hamburem ‘to kiss’, Arm. (LW) hamboyr ‘kiss’ (< 
2196:root *bau-: bu-, *ba-, *bä- ‘to kiss’ (cf. Pokorny: 103), which is probably 
2201:ba Cidöw ‘to kiss’ do not show the typical affricatisation of Plr. *b-. 
17067:Kurd. (Kurm.) mötin, miZtin, miZin/miZ-, (Sor.) miZin/miZ- ‘to suck; to kiss’, 
56870:to kiss
```


## [2026-09-05T14:48:02.069Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '2170,2205p' CHEUNG.txt"
}
```


### [2026-09-05T14:48:02.115Z] TOOL RESULT

```
*baud2 15 


Well attested: Pres.: IND. 3sg. BSogd. ptßyöty, CSogd. ptbydty, 3р1. CSogd. ptbydnt, MSogd. ptyByö’nd 
(GMS: $622), OPT. 3sg. ptByó y; Impf.: IND. 3sg. CSogd. ptybyd, MSogd. ptyBy6 (Sogdica: 31), 3pl. 
CSogd. ptybydnt, Fut.: IND. 2sg. CSogd. ptbydyq’; Partic.: perf. pass. CSogd. ptbstyt (pl.) ‘sensible, 
notable’, BSogd. ptBystk 


*NWIR: NP bösidan/bös-, Abyan. busoya/bus-, Khuns. bus-/busa ‘to kiss’, Ham. 
busayän/bus- ‘to kiss, embrace’, NP bös(ah), Kurd. (Kurm.) bösa (m.), Qohr. busa, 
Varz. bus ‘kiss’ 

*NEIR: (+ *ham-) Oss. I. zeembudyn, D. ambodun ‘to sense, feel’. 0 Pash. Iwast-/lwal- 
‘to read’ is probably unrelated, cf. NEVP: 46. The reconstruction *ni-bauda-, 
suggested in EVP: 41, is semantically unsatisfactory, on which see *HuadH. 

*MISC: (+ *ham-) Arm. (LW) hamburem ‘to kiss’, Arm. (LW) hamboyr ‘kiss’ (< 
Pth.) 

*SANSKRIT: bodh ‘to wake, awaken; to perceive, notice, heed’ (RV+) = EWAia II: 
233 

© Rastorgueva — Edel’man, ESIJa П: 136 ff., reconstruct a separate, onomatopoetic 
root *bau-: bu-, *ba-, *bä- ‘to kiss’ (cf. Pokorny: 103), which is probably 
unnecessary. The Pth. form provides us with the clue to the origin of NP 
bösidan/bös- (etc.), which appears to be an inchoative formation of *baud (as 
reiterated by Weber 1970: 107 f.). The other forms cited in support of the root 
*bau-: bu-, *ba-, *bà- are not compelling either. M. bay-/boy-, Yi. boh-/bohay-, Sh. 
ba Cidöw ‘to kiss’ do not show the typical affricatisation of Plr. *b-. 

«PIE *b"eud"- ‘to become attentive, be awake, perceive’ => LIV: 83 f. | Pok.: 150 ff. 
*IE COGNATES: Gr. x£$00 ‘I proclaim, summon’, Gr. леъӨорол (med.) ‘I learn, 
hear’, Olrish ad-bond- ‘to proclaim, declare’, OCS bljusti ‘to take care, look after’,
```


## [2026-09-05T14:48:50.694Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n '1,120p' tools/verify_check.py"
}
```


### [2026-09-05T14:48:50.736Z] TOOL RESULT

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


## [2026-09-05T14:49:00.077Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; for u in \"https://www.etymonline.com/word/balm\" \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/bagnáh\"; do echo \"### $u\"; python3 tools/fetch_source.py \"$u\" --note \"page 102 verification (balsam chain / *bagna- naked)\"; done; tail -3 data/verification/sources/web/index.jsonl"
}
```


### [2026-09-05T14:49:02.410Z] TOOL RESULT

```
### https://www.etymonline.com/word/balm
/home/sfmqrb/git/rishe/data/verification/sources/web/e7996af531c60e9b.txt
### https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/bagnáh
/home/sfmqrb/git/rishe/data/verification/sources/web/2cfb3dc919ae0b68.txt
{"url": "https://abadis.ir/fatofa/بلسام/", "file": "data/verification/sources/web/bef6213ad76b57ce.txt", "fetched": "2026-09-05T14:47:27Z", "status": 200, "bytes": 1364, "title": "بلسام - معنی در دیکشنری آبادیس", "note": "page 102, Busma root: is Persian بلسام a real word (Dehkhoda/Moin)"}
{"url": "https://www.etymonline.com/word/balm", "file": "data/verification/sources/web/e7996af531c60e9b.txt", "fetched": "2026-09-05T14:49:01Z", "status": 200, "bytes": 7040, "title": "Balm - Etymology, Origin & Meaning", "note": "page 102 verification (balsam chain / *bagna- naked)"}
{"url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/bagnáh", "file": "data/verification/sources/web/2cfb3dc919ae0b68.txt", "fetched": "2026-09-05T14:49:02Z", "status": -1, "bytes": 39, "title": "", "note": "page 102 verification (balsam chain / *bagna- naked)"}
```


## [2026-09-05T14:49:04.676Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; grep -n -i \"balm (n\" -A6 data/verification/sources/web/e7996af531c60e9b.txt | head -20"
}
```


### [2026-09-05T14:49:04.722Z] TOOL RESULT

```
23: balm (n.) 
24-
25- c. 1200, basme , "oily, resinous aromatic substance exuding naturally from shrubs of the genus Commiphora," from Old French basme , baume , balme "balsam, balm" (12c., Modern French baume ), from Latin balsamum , from Greek balsamon "balsam," from Hebrew (Semitic) basam "spice," which is related to Aramaic busma , Arabic basham "balsam, spice, perfume." The spelling was refashioned 15c.-16c. on the Latin model. Compare balsam .
26-
27- As the name of a tree which yields the substance, it is attested from late 14c.; from mid-15c. it was extended to various fragrant garden herbs. Also by extension, "any aromatic preparation used in healing wounds or soothing pain, or as a perfume or in anointing" (late 14c.). Hence the transferred sense of "healing or soothing influence" (1540s). Biblical Balm of Gilead (esteemed for its medicinal properties) is from Coverdale (Jeremiah viii.22); the Hebrew word there is tsori , which was rendered in Septuagint and Vulgate as "resin" (Greek rhētinē , Latin resina ).
28- also from c. 1200 
29-
```


## [2026-09-05T14:49:10.201Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; mkdir -p data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg102.png data/verification/sources/refs/ocr/BOOK/102.png && ls -la data/verification/sources/refs/ocr/BOOK/ | head"
}
```


### [2026-09-05T14:49:12.524Z] TOOL RESULT

```
total 2684
drwxrwxr-x 2 sfmqrb sfmqrb   4096 Sep  5 10:49 .
drwxrwxr-x 9 sfmqrb sfmqrb   4096 Sep  5 01:38 ..
-rw-rw-r-- 1 sfmqrb sfmqrb  71589 Sep  5 10:46 100.png
-rw-rw-r-- 1 sfmqrb sfmqrb 104864 Sep  4 19:03 101.png
-rw-rw-r-- 1 sfmqrb sfmqrb  68145 Sep  5 10:49 102.png
-rw-rw-r-- 1 sfmqrb sfmqrb  86203 Sep  4 19:03 126.png
-rw-rw-r-- 1 sfmqrb sfmqrb 105296 Sep  4 19:03 311.png
-rw-rw-r-- 1 sfmqrb sfmqrb  96466 Sep  4 19:03 33.png
-rw-rw-r-- 1 sfmqrb sfmqrb  99093 Sep  4 19:03 39.png
```


## [2026-09-05T14:49:26.378Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"-- WLD Bd1 --\"; grep -n \"Lippe, Kuß\\|Lippe,  Kuß\\|bosidan\\|büsidan\" incoming/WLD/WLD_Bd1_pages.txt | head -10; echo \"-- IEC bu --\"; grep -n \"^bu-\\|bū-\\|to kiss\" IEC.txt | head -10"
}
```


### [2026-09-05T14:49:26.453Z] TOOL RESULT

```
-- WLD Bd1 --
-- IEC bu --
1844:bhübh- “a hooting animal’. WP II, 112 Arm. bbun (/noise', fr. *bhübhon); Lat. bübon (owl, w. assimilated consonants) beside bū- bulo, are (onomat. *büb-); MIr. cf. búbaire,
1902:bhükos ‘hummer, roarer'. Cf. WP II, 184 & 112 Lat. fücus ‘bee, drone’; ON by ‘bee’; OCS bykü ‘bull’; OCz. cf. bykati ‘bellow’; Li. bū- kas “bull; bittern'
```


## [2026-09-05T14:49:29.390Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"Kuß\" incoming/WLD/WLD_Bd2_pages.txt | head -10; echo \"--- search bosidan in WLD Bd2 ---\"; grep -n -i \"bosidan\\|büsidan\\|buzë\\|buze\" incoming/WLD/WLD_Bd2_pages.txt | head -10"
}
```


### [2026-09-05T14:49:29.467Z] TOOL RESULT

```
--- search bosidan in WLD Bd2 ---
9402:siidbal. bojag „offnen, losen, losbinden^*, als pers. Lw. arm. buzem „heile,
```


## [2026-09-05T14:49:35.132Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"Kuß\\|Kuss\" incoming/WLD/WLD_Bd1_pages.txt | head -10; echo \"-- pages tag check --\"; grep -n \"pdf page\" incoming/WLD/WLD_Bd1_pages.txt | sed -n '110,125p'"
}
```


### [2026-09-05T14:49:35.199Z] TOOL RESULT

```
-- pages tag check --
```


## [2026-09-05T14:49:37.581Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; ls -la incoming/WLD/; head -5 incoming/WLD/WLD_Bd1_pages.txt; wc -l incoming/WLD/WLD_Bd1_pages.txt"
}
```


### [2026-09-05T14:49:37.954Z] TOOL RESULT

```
total 146212
drwxrwxr-x  2 sfmqrb sfmqrb     4096 Sep  4 14:06 .
drwxrwxr-x 23 sfmqrb sfmqrb     4096 Sep  4 14:06 ..
-rw-rw-r--  1 sfmqrb sfmqrb  2993454 Sep  4 14:06 WLD_Bd1_1930_dli_70244_djvu.txt
-rw-rw-r--  1 sfmqrb sfmqrb 42256714 Sep  4 14:06 WLD_Bd1_1930_dli_70244_text.pdf
-rw-rw-r--  1 sfmqrb sfmqrb  4327601 Sep  4 14:06 WLD_Bd1_pages.txt
-rw-rw-r--  1 sfmqrb sfmqrb  2417287 Sep  4 14:06 WLD_Bd2_1927_dli_106624_djvu.txt
-rw-rw-r--  1 sfmqrb sfmqrb 94865800 Sep  4 14:06 WLD_Bd2_1927_dli_106624_text.pdf
-rw-rw-r--  1 sfmqrb sfmqrb  2833963 Sep  4 14:06 WLD_Bd2_pages.txt
            GOVERNMENT OF INDIA
 ARCHEOLOGICAL SURVEY OF INDIA

               CENTRAL
            ARCHEOLOGICAL
81974 incoming/WLD/WLD_Bd1_pages.txt
```


## [2026-09-05T14:49:43.746Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i \"küssen\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt | head -10"
}
```


### [2026-09-05T14:49:43.821Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T14:49:47.949Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"kiss\" IEC.txt | head -10"
}
```


### [2026-09-05T14:49:47.994Z] TOOL RESULT

```
910:baĝāið (bagið) “kiss” Fris. patsjen; Cz. bozati, id.
1001:bud- (1), budio “lip; lips, mouth’. WP II, 114 Gk. cf. bázen, Hes. buzón “close together’; cf. poppüzo (‘smack the lips’, fr. *bud-budio); Alb. buzë ‘lip’, substrate in Rum. buză, wd: Big. büza ‘cheek’, and cf. Pol. buzia (“little mouth’, fr. *boud-); also E to pout and Fr. bouder, and cf. Slovak bozk “kiss? (fr. *bu- diko-)
5743:Per. cf. Zale “hail; dew" (?); Alb. zallé ‘pebble, shingle’; OHG kisil, MHG kisel, OE ceosel, ceosol, id.; G Kiesel "flint, silica, hail; kisseln, v. ‘hail’; Icel. kísill ‘silica’; OCS žali “shore? Srb. žal, id.
7202:kikis, iə ʻa chirping bird, screecher’. WP I, 451. See next and kīk- Skt. kikih “blue jay’; Hes. kíkka ‘hen’; Gk. kissa “jay”; Ir. ciochán (‘titmouse’, fr. *kikon); Br. cf. kégin ‘jay’; Fris. hij ‘plover’; Slovene ček ‘mountain-finch’; Latv. kikis ‘hawk’ beside kikuts, m. ‘woodcock’, kikuts ‘water-snipe’; Li. cf. kikilis ‘chaffinch’ and kikutis, gs -čio ‘woodcock’
8768:Skt. (?) Siksami 'attempt'; (?) Si$ami, SiSimi ‘bestow’; Arm. skem, hskem “watch, be alert’; sksnum, aor. sksaj ‘begin’ beside sksanim, id.; Gk. cf. kissó, gs. -oos. f. ‘itch, longing"; (Hes. kiko queried: ‘fetch, ge? seems to contain the fragment Ki- *hither"); Blg. sáskam ‘incite dogs’; R cf. ü-síkat,, v. id.
8770:Kikios (Kiksnos, io) “twist, rope, lasso, band, thong, leather'. WP I, 451 Skt. Sikyam ‘noose, cord, carrier-sling'; Arm. čvan, -i, -av ‘cord’; Gk. kissós ‘ivy’; Li. Sik$nà ‘strap’; cf. SikSnys, m. "bat (?); Latv. siksna ‘strap’
9372:labiom, io (laburom, labs-) ‘lip’. Cf. labudiom & lobos, & cf. WP II, 431, 714 Per. lab “lip, brink’; OLat. labia, Lat. labium & labrum ‘lip’; Ger. Laffe ‘chatterbox’ beside OHG lefs, leffur, m. ‘lip’; Sw. läpp, m. "lip, spout’; cf. (variant) Kurd lews ‘lower lip, blub- ber-lip and OCS lobüzü ‘kiss’. Verbal deri- vatives: OHG laffen, gi-lepphen ‘lick’; MHG laffen, leffen, id.; Sw. lüppja ‘lick, sup; OE leppan “feed titbits. Long-gde in Cz. lábat, v. Jap up’
9388:labudios, io, iom, cf. labiom Gk. cf. lábuzos, f. (a spice-plant, so-named from shape of leaves?); Ger. Lefze, f. lip’; OCS lobüzü, m. *kiss'
13748:puk- “fit, enclose, hug, embrace, encircle’. WP II, 82 Av. pusa, f. ‘diadem’; Per. puse, id.; Gk. cf. púka, adv. ‘close-fitting’; puknós, pukinós, adj. ‘compact’; cf. ám-pux, gs: -pukos, m & f ‘chap- let, fr. ámbh-^); (late Gk. also ‘tyre’); Alb. puth, v. ‘kiss’; pér-puth, v. “fit close’; MIr. (*phuk-) poc, s. *kiss'; Br. poki, inf. id.
```


## [2026-09-05T14:50:32.235Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'NR>=19440 && NR<=19560' BRT.txt | grep -n -E \"^[0-9]{3,4}$|^ *[0-9]{3,4} *$\" ; echo \"---\"; sed -n '19540,19552p' BRT.txt | cat -A | grep -o \"1[0-9][0-9][0-9]\" | head"
}
```


### [2026-09-05T14:50:34.358Z] TOOL RESULT

```
29:107
31:1108
---
```


## [2026-09-05T14:53:24.554Z] TOOL CALL #71: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk102.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\n\ndata = {\n \"pdf_page\": 102,\n \"book_page\": 72,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-05\",\n \"entries\": []\n}\n\n# ---------------- entry 0 : Bu ----------------\ne0 = {\n \"entry\": 0,\n \"root\": \"Bu\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE (imitative/expressive) *bu- 'lip, kiss' — Pokorny, IEW 103; Walde-Pokorny I 113 f.\",\n \"note\": (\"Pokorny I 103 has the root verbatim as Nourai gives it: \\\"bu- 'Lippe, Ku\\u00df', als Nachahmung des Ku\\u00dflautes, \"\n   \"Sprengung des saugenden Lippenverschlusses nach innen, also eigentlich verschieden von bu-, bh\\u016b- 'aufblasen'\\\", with \"\n   \"\\\"Npers. b\\u014ds\\u012bdan 'k\\u00fcssen'; alb. buze 'Mund'; mir. bus, pus 'Lippe'; nhd. Buss 'Ku\\u00df', engl. buss; lit. bu\\u010di\\u00fcoti\\\". \"\n   \"Language label ('Indo-European') and gloss ('lip, kiss') are therefore exactly Pokorny's. Two caveats: (a) this is an \"\n   \"expressive/nursery formation, not an inherited root with regular correspondences \\u2014 Buck (SYN 1114) calls bu, bus and ku, kus \"\n   \"two separate imitative groups, and Mann (IEC 1001) reconstructs the group as *bud- 'lip, mouth' without the Persian word; \"\n   \"(b) Nourai's root NOTE is a close paraphrase of Buck p.1113 ('Kissing, as an expression of affection or love, is unknown among many \"\n   \"races ... There is no conclusive evidence that kissing was known in IE times'), so SYN:1113 is the source of the note, not of an arrow. \"\n   \"The two Germanic arrows below (kusjan, buss) are where the entry goes wrong, not the root box.\"),\n \"note_fa\": (\"\\u0631\\u06cc\\u0634\\u0647\\u0654 *bu- \\u062f\\u0631 \\u0647\\u0646\\u062f\\u0648\\u0627\\u0631\\u0648\\u067e\\u0627\\u06cc\\u06cc \\u0622\\u063a\\u0627\\u0632\\u06cc\\u0646 \\u06cc\\u06a9 \\u0633\\u0627\\u062e\\u062a \\u062a\\u0642\\u0644\\u06cc\\u062f\\u06cc (\\u0646\\u0627\\u0645\\u200c\\u0622\\u0648\\u0627) \\u0627\\u0633\\u062a \\u0628\\u0647 \\u0645\\u0639\\u0646\\u06cc \\u00ab\\u0644\\u0628\\u060c \\u0628\\u0648\\u0633\\u0647\\u00bb. \"\n   \"\\u067e\\u0648\\u06a9\\u0648\\u0631\\u0646\\u06cc \\u062f\\u0631 \\u0635\\u0641\\u062d\\u0647\\u0654 \\u06f1\\u06f0\\u06f3 \\u0647\\u0645\\u06cc\\u0646 \\u0631\\u06cc\\u0634\\u0647 \\u0631\\u0627 \\u0628\\u0627 \\u0647\\u0645\\u06cc\\u0646 \\u0645\\u0639\\u0646\\u06cc \\u0622\\u0648\\u0631\\u062f\\u0647 \\u0648 \\u0641\\u0627\\u0631\\u0633\\u06cc \\u00ab\\u0628\\u0648\\u0633\\u06cc\\u062f\\u0646\\u00bb\\u060c \\u0622\\u0644\\u0628\\u0627\\u0646\\u06cc\\u0627\\u06cc\\u06cc buz\\u00eb \\u00ab\\u062f\\u0647\\u0627\\u0646\\u00bb\\u060c \"\n   \"\\u0627\\u06cc\\u0631\\u0644\\u0646\\u062f\\u06cc \\u0645\\u06cc\\u0627\\u0646\\u0647 bus \\u00ab\\u0644\\u0628\\u00bb \\u0648 \\u0627\\u0646\\u06af\\u0644\\u06cc\\u0633\\u06cc buss \\u0631\\u0627 \\u0630\\u06cc\\u0644 \\u0622\\u0646 \\u0646\\u0634\\u0627\\u0646\\u062f\\u0647 \\u0627\\u0633\\u062a\\u061b \\u067e\\u0633 \\u0628\\u0631\\u0686\\u0633\\u0628 \\u0632\\u0628\\u0627\\u0646\\u06cc \\u0648 \\u0645\\u0639\\u0646\\u06cc\\u0627\\u06cc \\u062c\\u0639\\u0628\\u0647\\u0654 \\u0631\\u06cc\\u0634\\u0647 \\u062f\\u0631\\u0633\\u062a \\u0627\\u0633\\u062a. \"\n   \"\\u0627\\u0645\\u0627 \\u0628\\u0627\\u06cc\\u062f \\u062f\\u0627\\u0646\\u0633\\u062a \\u06a9\\u0647 \\u0627\\u06cc\\u0646 \\u06af\\u0648\\u0646\\u0647 \\u0631\\u06cc\\u0634\\u0647\\u200c\\u0647\\u0627\\u06cc \\u062a\\u0642\\u0644\\u06cc\\u062f\\u06cc \\u062a\\u0627\\u0628\\u0639 \\u062f\\u06af\\u0631\\u06af\\u0648\\u0646\\u06cc\\u200c\\u0647\\u0627\\u06cc \\u0622\\u0648\\u0627\\u06cc\\u06cc \\u0645\\u0646\\u0638\\u0645 \\u0646\\u06cc\\u0633\\u062a\\u0646\\u062f\\u061b \\u0628\\u0627\\u06a9 (\\u0635 \\u06f1\\u06f1\\u06f1\\u06f4) \\u062f\\u0648 \\u06af\\u0631\\u0648\\u0647 bu/bus \\u0648 ku/kus \\u0631\\u0627 \"\n   \"\\u062c\\u062f\\u0627 \\u0645\\u06cc\\u200c\\u0634\\u0645\\u0627\\u0631\\u062f. \\u06cc\\u0627\\u062f\\u062f\\u0627\\u0634\\u062a \\u0646\\u0648\\u0631\\u0627\\u06cc\\u06cc \\u062f\\u0631\\u0628\\u0627\\u0631\\u0647\\u0654 \\u0646\\u0627\\u0634\\u0646\\u0627\\u062e\\u062a\\u0647 \\u0628\\u0648\\u062f\\u0646 \\u0628\\u0648\\u0633\\u0647 \\u062f\\u0631 \\u062f\\u0648\\u0631\\u0627\\u0646 \\u0647\\u0646\\u062f\\u0648\\u0627\\u0631\\u0648\\u067e\\u0627\\u06cc\\u06cc \\u0639\\u06cc\\u0646\\u0627\\u064b \\u0628\\u0631\\u06af\\u0631\\u062f\\u0627\\u0646 \\u0635\\u0641\\u062d\\u0647\\u0654 \\u06f1\\u06f1\\u06f1\\u06f3 \\u0628\\u0627\\u06a9 \\u0627\\u0633\\u062a. \"\n   \"\\u062f\\u0631 \\u0645\\u062c\\u0645\\u0648\\u0639 \\u0627\\u062f\\u0639\\u0627\\u06cc \\u0646\\u0648\\u0631\\u0627\\u06cc\\u06cc \\u062f\\u0631\\u0628\\u0627\\u0631\\u0647\\u0654 \\u062e\\u0648\\u062f \\u0631\\u06cc\\u0634\\u0647 \\u062f\\u0631\\u0633\\u062a \\u0627\\u0633\\u062a\\u061b \\u0627\\u0634\\u06a9\\u0627\\u0644 \\u062f\\u0631 \\u062f\\u0648 \\u067e\\u06cc\\u06a9\\u0627\\u0646 \\u0698\\u0631\\u0645\\u0646\\u06cc \\u0627\\u0633\\u062a.\"),\n \"sources\": [W+\"%D8%A8%D9%88%D8%B3%DB%8C%D8%AF%D9%86\", \"https://www.etymonline.com/word/buss\"],\n \"ref_check\": [\n   {\"ref\": \"POK:103\", \"status\": \"supports\",\n    \"note\": \"POK_01.txt leaf 113 (= printed p.103): \\\"bu- 'Lippe, Ku\\u00df', als Nachahmung des Ku\\u00dflautes ... Npers. b\\u014ds\\u012bdan 'k\\u00fcssen'; alb. buze 'Mund'; mir. bus, pus 'Lippe' ... nhd. Buss 'Ku\\u00df', bussen 'k\\u00fcssen' ... engl. buss ... lit. bu\\u010di\\u00fcoti 'k\\u00fcssen'. WP. I 113f.\\\" (awk 'BEGIN{RS=\\\"\\\\f\\\"} NR==113' POK_01.txt)\"},\n   {\"ref\": \"SYN:1113\", \"status\": \"supports\",\n    \"note\": \"SYN.txt line 28127 ff., section 16.29 KISS, printed pp.1113-1114: \\\"Kissing, as an expression of affection or love, is unknown among many races ... There is no conclusive evidence that [kissing] was known in IE times\\\" \\u2014 verbatim the source of Nourai's root note; the word list is on p.1114.\"}\n ],\n \"consulted\": [\n   {\"src\": \"SYN\", \"where\": \"16.29, pp.1113-1114\", \"stance\": \"partial\",\n    \"note\": \"Buck separates \\\"1. Derivs. of an expressive syllable ku or kus (cf. the more obviously imitative bu, bus, below, 2)\\\" from \\\"2. Derivs. of an imitative bu, bus, in words for 'kiss' and 'lip' or 'mouth' ... NE buss, NHG buss, Sp. buz, Pol. buzia; cf. Ir. bus, Alb. buz\\u00eb, Rum. buz\\u0103 'lip'\\\" \\u2014 supports the root but not Nourai's Germanic branch.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985, root list s.v. kus-\", \"stance\": \"contradicts\",\n    \"note\": \"AHD_watkins1985.txt line 648: \\\"kus-. A kiss. Germanic *kussaz, a kiss, with denominative *kussjan in Old English cyssan, to kiss: KISS. [Pok. ku-, kus- 626.]\\\" \\u2014 Watkins has no *bu- root at all and 'buss' does not appear in his English index (grep BUSS finds only BLUNDERBUSS).\"},\n   {\"src\": \"IEC\", \"where\": \"Mann, col. s.v. bud- (1) (IEC.txt line 1001)\", \"stance\": \"partial\",\n    \"note\": \"\\\"bud- (1), budio 'lip; lips, mouth'. WP II, 114 ... Alb. buz\\u00eb 'lip' ... Pol. buzia ('little mouth') ... Slovak bozk 'kiss' (fr. *bu-diko-)\\\" \\u2014 same family, reconstructed with a -d- extension and without the Persian word.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. I 113 f. (as cited by Pokorny)\", \"stance\": \"silent\",\n    \"note\": \"Pokorny's own reference for the root is \\\"WP. I 113f.\\\"; the local OCR of Walde-Pokorny (WLD_Bd1_pages.txt, WLD_Bd2_pages.txt) returns nothing for 'K\\u00fcssen'/'Ku\\u00df' \\u2014 the German scan is too poor to confirm the page directly.\"}\n ],\n \"nodes\": []\n}\n\ne0[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Persian\", \"words\": \"b\\u016bs\",\n \"verdict\": \"plausible\",\n \"derivation\": (\"NP \\u0628\\u0648\\u0633 b\\u014ds 'a kiss', \\u0628\\u0648\\u0633\\u0647 b\\u014dsa, verb \\u0628\\u0648\\u0633\\u06cc\\u062f\\u0646 b\\u014ds\\u012bdan (Middle Persian written bwsytn'). Pokorny p.103 cites exactly \"\n   \"\\\"Npers. b\\u014ds\\u012bdan 'k\\u00fcssen'\\\" as the Iranian member of the imitative *bu- group, and Wiktionary follows him: \\\"From imitative \"\n   \"Proto-Indo-European *bu, compare Latin basium 'kiss', Welsh bus 'kiss, lip', and English buss\\\". So the arrow as drawn has good support. \"\n   \"But the modern standard for Iranian verbs disagrees: Cheung, Etymological Dictionary of the Iranian Verb (2007) p.15 s.v. *baud\\u2082 \"\n   \"'to sense, feel' takes NP b\\u014ds\\u012bdan/b\\u014ds- to be an inchoative *baud-sa- of that root, pointing to Parthian pdbws- 'to desire, yearn' and \"\n   \"'mbwy- 'to kiss' and to the Parthian loan in Armenian hamboyr 'kiss', hamburem 'to kiss', and says of the onomatopoeic root \"\n   \"*bau-: bu- of Rastorgueva-Edel'man (ESIJa II 136 ff., who follow Pokorny 103) that it is \\\"probably unnecessary\\\". The word and the \"\n   \"meaning are certain; only the choice between 'imitative *bu-' and 'inchoative of *baud-' is open, hence plausible rather than confirmed. \"\n   \"The script_extra \\u0628\\u0648\\u0633\\u06cc\\u062f\\u0646 and the Ferdowsi line (\\\"... \\u0628\\u0647 \\u067e\\u06cc\\u0634 \\u0633\\u067e\\u0647\\u0628\\u062f \\u0632\\u0645\\u06cc\\u0646 \\u062f\\u0627\\u062f \\u0628\\u0648\\u0633\\\") are correct usage of the noun.\"),\n \"derivation_fa\": (\"\\u00ab\\u0628\\u0648\\u0633\\u00bb/\\u00ab\\u0628\\u0648\\u0633\\u0647\\u00bb \\u0648 \\u0645\\u0635\\u062f\\u0631 \\u00ab\\u0628\\u0648\\u0633\\u06cc\\u062f\\u0646\\u00bb \\u062f\\u0631 \\u0641\\u0627\\u0631\\u0633\\u06cc \\u0646\\u0648 \\u0627\\u0632 \\u0641\\u0627\\u0631\\u0633\\u06cc \\u0645\\u06cc\\u0627\\u0646\\u0647 b\\u014ds\\u012bdan (\\u0646\\u0648\\u0634\\u062a\\u0647\\u0654 bwsytn') \\u0645\\u06cc\\u200c\\u0622\\u06cc\\u062f. \"\n   \"\\u067e\\u0648\\u06a9\\u0648\\u0631\\u0646\\u06cc (\\u0635 \\u06f1\\u06f0\\u06f3) \\u0647\\u0645\\u06cc\\u0646 \\u0641\\u0639\\u0644 \\u0631\\u0627 \\u0630\\u06cc\\u0644 \\u0631\\u06cc\\u0634\\u0647\\u0654 \\u062a\\u0642\\u0644\\u06cc\\u062f\\u06cc *bu- \\u0622\\u0648\\u0631\\u062f\\u0647 \\u0648 \\u0648\\u06cc\\u06a9\\u06cc\\u200c\\u0648\\u0627\\u0698\\u0647 \\u0646\\u06cc\\u0632 \\u0647\\u0645\\u06cc\\u0646 \\u0631\\u0627 \\u062a\\u06a9\\u0631\\u0627\\u0631 \\u0645\\u06cc\\u200c\\u06a9\\u0646\\u062f\\u061b \\u067e\\u0633 \\u067e\\u06cc\\u06a9\\u0627\\u0646 \\u0646\\u0648\\u0631\\u0627\\u06cc\\u06cc \\u067e\\u0634\\u062a\\u0648\\u0627\\u0646\\u0647 \\u062f\\u0627\\u0631\\u062f. \"\n   \"\\u0627\\u0645\\u0627 \\u0686\\u0648\\u0646\\u06af (\\u06f2\\u06f0\\u06f0\\u06f7\\u060c \\u0635 \\u06f1\\u06f5) \\u062f\\u0631 \\u0641\\u0631\\u0647\\u0646\\u06af \\u0631\\u06cc\\u0634\\u0647\\u200c\\u0634\\u0646\\u0627\\u062e\\u062a\\u06cc \\u0641\\u0639\\u0644 \\u0627\\u06cc\\u0631\\u0627\\u0646\\u06cc\\u060c \\u0628\\u0648\\u0633\\u06cc\\u062f\\u0646 \\u0631\\u0627 \\u0635\\u06cc\\u063a\\u0647\\u0654 \\u0622\\u063a\\u0627\\u0632\\u06cc (inchoative) \\u0627\\u0632 \\u0633\\u062a\\u0627\\u06a9 *baud- \\u00ab\\u062f\\u0631\\u06cc\\u0627\\u0641\\u062a\\u0646\\u060c \"\n   \"\\u062d\\u0633 \\u06a9\\u0631\\u062f\\u0646\\u00bb \\u0645\\u06cc\\u200c\\u062f\\u0627\\u0646\\u062f (\\u0642\\u06cc\\u0627\\u0633 \\u067e\\u0627\\u0631\\u062a\\u06cc pdbws- \\u00ab\\u062e\\u0648\\u0627\\u0633\\u062a\\u0646\\u00bb \\u0648 'mbwy- \\u00ab\\u0628\\u0648\\u0633\\u06cc\\u062f\\u0646\\u00bb\\u060c \\u0648 \\u0648\\u0627\\u0645\\u200c\\u0648\\u0627\\u0698\\u0647\\u0654 \\u0627\\u0631\\u0645\\u0646\\u06cc hamboyr \\u00ab\\u0628\\u0648\\u0633\\u0647\\u00bb) \\u0648 \\u0631\\u06cc\\u0634\\u0647\\u0654 \\u062a\\u0642\\u0644\\u06cc\\u062f\\u06cc \\u0631\\u0627 \\u00ab\\u0632\\u0627\\u06cc\\u062f\\u00bb \\u0645\\u06cc\\u200c\\u062e\\u0648\\u0627\\u0646\\u062f. \"\n   \"\\u067e\\u0633 \\u062e\\u0648\\u062f \\u0648\\u0627\\u0698\\u0647 \\u0648 \\u0645\\u0639\\u0646\\u06cc \\u062f\\u0631\\u0633\\u062a \\u0627\\u0633\\u062a\\u060c \\u0648\\u0644\\u06cc \\u0627\\u062f\\u0639\\u0627\\u06cc \\u0646\\u0648\\u0631\\u0627\\u06cc\\u06cc \\u0641\\u0642\\u0637 \\u00ab\\u0628\\u0627 \\u0627\\u062d\\u062a\\u06cc\\u0627\\u0637 \\u067e\\u0630\\u06cc\\u0631\\u0641\\u062a\\u0646\\u06cc\\u00bb \\u0627\\u0633\\u062a.\"),\n \"sources\": [W+\"%D8%A8%D9%88%D8%B3%DB%8C%D8%AF%D9%86\"],\n \"ref_check\": [\n   {\"ref\": \"POK:103\", \"status\": \"supports\",\n    \"note\": \"POK_01.txt leaf 113: \\\"Npers. b\\u014ds\\u012bdan 'k\\u00fcssen'\\\" stands first in the list of reflexes of bu- 'Lippe, Ku\\u00df'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"CHEUNG\", \"where\": \"p.15 s.v. *baud\\u2082 (CHEUNG.txt lines 2181-2201; index line 40849 'bosidan/bos-, 15')\", \"stance\": \"contradicts\",\n    \"note\": \"\\\"*NWIR: NP b\\u014dsidan/b\\u014ds-, Abyan. busoya/bus- ... 'to kiss' ... Rastorgueva - Edel'man, ESIJa II: 136 ff., reconstruct a separate, onomatopoetic root *bau-: bu-, *ba-, *b\\u0101- 'to kiss' (cf. Pokorny: 103), which is probably unnecessary. The Pth. form provides us with the clue to the origin of NP b\\u014dsidan/b\\u014ds- (etc.), which appears to be an inchoative formation of *baud\\u2082\\\".\"},\n   {\"src\": \"BQT\", \"where\": \"vol.1, s.v. \\u0628\\u0648\\u0633 (BQT_v1_pages.txt line 21536)\", \"stance\": \"supports\",\n    \"note\": \"\\\"\\u0628\\u0648\\u0633\\u060c \\u0628\\u0627 \\u0648\\u0627\\u0648 \\u0645\\u062c\\u0647\\u0648\\u0644\\u060c \\u0645\\u062e\\u0641\\u0641 \\u0628\\u0648\\u0633\\u0647 \\u0627\\u0633\\u062a \\u0648 \\u0628\\u0639\\u0631\\u0628\\u06cc \\u0642\\u0628\\u0644\\u0647 \\u06af\\u0648\\u06cc\\u0646\\u062f ... \\u0645\\u0631 \\u0628\\u0648\\u0633\\u06cc\\u062f\\u0646 \\u0647\\u0645 \\u0647\\u0633\\u062a\\\" \\u2014 confirms b\\u014ds (w\\u0101w-i majh\\u016bl, i.e. \\u014d) as a shortening of b\\u014dsa, and the verb b\\u014ds\\u012bdan; no etymology given.\"},\n   {\"src\": \"HRN\", \"where\": \"grep 'bosid'/'busid' in HRN.txt\", \"stance\": \"silent\",\n    \"note\": \"Horn's Grundriss has no numbered entry for b\\u014ds\\u012bdan (the only hit, no. 233 line 2400, is b\\u016bdan 'sein' where 'bos-em' is quoted only as a rhyme/paradigm parallel).\"},\n   {\"src\": \"HUB\", \"where\": \"grep 'bosid'/'busid' in HUB.txt\", \"stance\": \"silent\",\n    \"note\": \"H\\u00fcbschmann, Persische Studien: no hit for the verb.\"},\n   {\"src\": \"MON\", \"where\": \"2-vol Adena condensation (MON_part1.txt)\", \"stance\": \"silent\",\n    \"note\": \"The condensed Mo'in OCR has no \\u0628\\u0648\\u0633/\\u0628\\u0648\\u0633\\u06cc\\u062f\\u0646 headword (only \\u0627\\u062a\\u0648\\u0628\\u0648\\u0633 etc.); the 6-vol Farhang is not online.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 2, \"lang\": \"Germanic\", \"words\": \"kusjan\",\n \"verdict\": \"disputed\",\n \"derivation\": (\"The Germanic verb is *kussjan\\u0105 (Nourai's 'kusjan' with one -s- is a simplified spelling), a denominative of the noun \"\n   \"*kussaz 'a kiss', continued in Gothic kukjan, Old Norse kyssa, Old English cyssan > English kiss, Old High German kussen > German k\\u00fcssen. \"\n   \"That much is right. What is wrong is the parent: AHD \\u2014 the very reference Nourai cites \\u2014 puts it under a different root: Watkins 1985 \"\n   \"\\\"kus-. A kiss. Germanic *kussaz, a kiss, with denominative *kussjan in Old English cyssan, to kiss: KISS. [Pok. ku-, kus- 626.]\\\", i.e. \"\n   \"Pokorny p.626, not p.103; and Watkins has no *bu- root at all. Buck 16.29 (p.1114) likewise keeps \\\"derivs. of an expressive syllable ku \"\n   \"or kus\\\" apart from \\\"derivs. of an imitative bu, bus\\\", noting the Germanic forms resisted the consonant shift because of their expressive \"\n   \"character. Two independent imitative bases, not one: the arrow *bu > Gmc kusjan is not supported by any of Nourai's own sources.\"),\n \"derivation_fa\": (\"\\u0641\\u0639\\u0644 \\u0698\\u0631\\u0645\\u0646\\u06cc \\u0622\\u063a\\u0627\\u0632\\u06cc\\u0646 *kussjan\\u0105 (\\u0646\\u0648\\u0631\\u0627\\u06cc\\u06cc kusjan \\u0645\\u06cc\\u200c\\u0646\\u0648\\u06cc\\u0633\\u062f) \\u0627\\u0632 \\u0646\\u0627\\u0645 *kussaz \\u00ab\\u0628\\u0648\\u0633\\u0647\\u00bb \\u0633\\u0627\\u062e\\u062a\\u0647 \\u0634\\u062f\\u0647 \\u0648 \\u062f\\u0631 \\u06af\\u0648\\u062a\\u06cc kukjan\\u060c \"\n   \"\\u0627\\u0646\\u06af\\u0644\\u06cc\\u0633\\u06cc \\u06a9\\u0647\\u0646 cyssan (\\u0627\\u0645\\u0631\\u0648\\u0632 kiss) \\u0648 \\u0622\\u0644\\u0645\\u0627\\u0646\\u06cc k\\u00fcssen \\u0628\\u0627\\u0632\\u0645\\u0627\\u0646\\u062f\\u0647 \\u0627\\u0633\\u062a\\u061b \\u062a\\u0627 \\u0627\\u06cc\\u0646\\u062c\\u0627 \\u062f\\u0631\\u0633\\u062a \\u0627\\u0633\\u062a. \\u0627\\u0645\\u0627 \\u067e\\u062f\\u0631 \\u0627\\u06cc\\u0646 \\u0648\\u0627\\u0698\\u0647 *bu- \\u0646\\u06cc\\u0633\\u062a: \\u062e\\u0648\\u062f \\u0645\\u0646\\u0628\\u0639\\u06cc \\u06a9\\u0647 \\u0646\\u0648\\u0631\\u0627\\u06cc\\u06cc \"\n   \"\\u0627\\u0631\\u062c\\u0627\\u0639 \\u0645\\u06cc\\u200c\\u062f\\u0647\\u062f (AHD/\\u0648\\u0627\\u062a\\u06a9\\u06cc\\u0646\\u0632) \\u0622\\u0646 \\u0631\\u0627 \\u0630\\u06cc\\u0644 \\u0631\\u06cc\\u0634\\u0647\\u0654 \\u062c\\u062f\\u0627\\u06af\\u0627\\u0646\\u0647\\u0654 *kus- (\\u067e\\u0648\\u06a9\\u0648\\u0631\\u0646\\u06cc \\u0635 \\u06f6\\u06f2\\u06f6) \\u0645\\u06cc\\u200c\\u0622\\u0648\\u0631\\u062f \\u0648 \\u0627\\u0635\\u0644\\u0627\\u064b \\u0631\\u06cc\\u0634\\u0647\\u200c\\u0627\\u06cc \\u0628\\u0647 \\u0646\\u0627\\u0645 *bu- \\u0646\\u062f\\u0627\\u0631\\u062f\\u061b \\u0628\\u0627\\u06a9 \\u0646\\u06cc\\u0632 \\u062f\\u0648 \\u0647\\u062c\\u0627\\u06cc \"\n   \"\\u062a\\u0642\\u0644\\u06cc\\u062f\\u06cc ku/kus \\u0648 bu/bus \\u0631\\u0627 \\u062c\\u062f\\u0627 \\u0645\\u06cc\\u200c\\u062f\\u0627\\u0646\\u062f. \\u067e\\u0633 \\u067e\\u0698\\u0648\\u0647\\u0634 \\u0627\\u0645\\u0631\\u0648\\u0632\\u06cc \\u0627\\u06cc\\u0646 \\u067e\\u06cc\\u06a9\\u0627\\u0646 \\u0631\\u0627 \\u0631\\u062f \\u0645\\u06cc\\u200c\\u06a9\\u0646\\u062f.\"),\n \"sources\": [W+\"Reconstruction:Proto-Germanic/kussijan%C4%85\"],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"contradicts\",\n    \"note\": \"AHD_watkins1985.txt line 648: \\\"kus-. A kiss. Germanic *kussaz, a kiss, with denominative *kussjan in Old English cyssan, to kiss: KISS. [Pok. ku-, kus- 626.]\\\" \\u2014 the form is there, the parentage is not.\"}\n ],\n \"consulted\": [\n   {\"src\": \"SYN\", \"where\": \"16.29 \\u00a71, p.1114\", \"stance\": \"contradicts\",\n    \"note\": \"\\\"1. Derivs. of an expressive syllable ku or kus (cf. the more obviously imitative bu, bus, below, 2). Gmc. forms resisting the consonant shift by reason of the expressive character ... Goth. kukjan, OFris. kukken; ON kyssa, OE cyssan ..., OHG kussen, etc. with sbs. ON koss, OE coss, OHG kus\\\".\"},\n   {\"src\": \"POK\", \"where\": \"p.626 (root ku-, kus-) vs p.103 (bu-)\", \"stance\": \"contradicts\",\n    \"note\": \"Pokorny's bu- entry on p.103 lists no Germanic *kussjan; the Germanic 'kiss' verb is his separate ku-, kus- on p.626 (as Watkins' bracket \\\"[Pok. ku-, kus- 626]\\\" records).\"},\n   {\"src\": \"KLN\", \"where\": \"s.v. kiss (1966)\", \"stance\": \"contradicts\",\n    \"note\": \"Klein derives kiss from OE cyssan, ON kyssa, OHG kussen < Gmc *kussjan, an imitative base of its own, with no connection to buss.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 3, \"lang\": \"English\", \"words\": \"buss\",\n \"verdict\": \"disputed\",\n \"derivation\": (\"English buss 'a kiss' (n. 1560s, v. 'to kiss' 1570s) is real and the gloss 'to kiss loudly' matches its usage \"\n   \"(\\\"We busse our wantons, but our wives we kisse\\\"), but it does not come from Germanic *kussjan \\u2014 that gives English kiss. \"\n   \"Buss belongs to the imitative bu-group of the root box itself: Pokorny p.103 lists \\\"nhd. Buss 'Ku\\u00df', bussen 'k\\u00fcssen', Busserl ... \"\n   \"engl. buss, schwed. puss\\\" under bu-, and Etymonline says buss is \\\"probably of imitative origin, as are Welsh and Gaelic bus 'kiss, lip', \"\n   \"French baiser (from Latin basiare), Spanish buz, German dialectal Buss, Turkish bus, Persian busa, Hindi bosa\\\"; Buck p.1114 groups it \"\n   \"with NHG buss, Sp. buz, Pol. buzia. The 16th-century English word is probably reinforced by (or taken from) continental forms of this type. \"\n   \"So the node's word belongs on this chart, but the drawn edge Germanic kusjan > English buss is wrong.\"),\n \"derivation_fa\": (\"\\u0648\\u0627\\u0698\\u0647\\u0654 \\u0627\\u0646\\u06af\\u0644\\u06cc\\u0633\\u06cc buss \\u00ab\\u0628\\u0648\\u0633\\u0647\\u060c \\u0628\\u0648\\u0633\\u06cc\\u062f\\u0646 \\u0628\\u0627 \\u0635\\u062f\\u0627\\u00bb (\\u0646\\u062e\\u0633\\u062a \\u06f1\\u06f5\\u06f6\\u06f0\\u0645) \\u0648\\u0627\\u0642\\u0639\\u06cc \\u0627\\u0633\\u062a\\u060c \\u0627\\u0645\\u0627 \\u0627\\u0632 *kussjan \\u0698\\u0631\\u0645\\u0646\\u06cc \\u0646\\u0645\\u06cc\\u200c\\u0622\\u06cc\\u062f\\u061b \\u0628\\u0627\\u0632\\u0645\\u0627\\u0646\\u062f\\u0647\\u0654 \"\n   \"*kussjan \\u062f\\u0631 \\u0627\\u0646\\u06af\\u0644\\u06cc\\u0633\\u06cc \\u0647\\u0645\\u0627\\u0646 kiss \\u0627\\u0633\\u062a. buss \\u0628\\u0647 \\u0647\\u0645\\u0627\\u0646 \\u06af\\u0631\\u0648\\u0647 \\u062a\\u0642\\u0644\\u06cc\\u062f\\u06cc *bu- \\u062a\\u0639\\u0644\\u0642 \\u062f\\u0627\\u0631\\u062f\\u061b \\u067e\\u0648\\u06a9\\u0648\\u0631\\u0646\\u06cc \\u062f\\u0631 \\u0635 \\u06f1\\u06f0\\u06f3 \\u062e\\u0648\\u062f engl. buss \\u0648 \\u0622\\u0644\\u0645\\u0627\\u0646\\u06cc Buss \\u0631\\u0627 \\u0630\\u06cc\\u0644 \\u0647\\u0645\\u06cc\\u0646 \"\n   \"\\u0631\\u06cc\\u0634\\u0647 \\u0622\\u0648\\u0631\\u062f\\u0647 \\u0648 \\u0627\\u062a\\u06cc\\u0645\\u0648\\u0644\\u0627\\u06cc\\u0646 \\u0622\\u0646 \\u0631\\u0627 \\u0646\\u0627\\u0645\\u200c\\u0622\\u0648\\u0627 \\u0645\\u06cc\\u200c\\u062e\\u0648\\u0627\\u0646\\u062f \\u0648 \\u062d\\u062a\\u06cc \\u0641\\u0627\\u0631\\u0633\\u06cc busa \\u0631\\u0627 \\u06a9\\u0646\\u0627\\u0631 \\u0622\\u0646 \\u0645\\u06cc\\u200c\\u0646\\u0634\\u0627\\u0646\\u062f. \\u067e\\u0633 \\u062c\\u0627\\u06cc \\u0648\\u0627\\u0698\\u0647 \\u062f\\u0631 \\u0627\\u06cc\\u0646 \\u0646\\u0645\\u0648\\u062f\\u0627\\u0631 \\u062f\\u0631\\u0633\\u062a \\u0627\\u0633\\u062a\\u060c \"\n   \"\\u0648\\u0644\\u06cc \\u067e\\u06cc\\u06a9\\u0627\\u0646\\u06cc \\u06a9\\u0647 \\u0622\\u0646 \\u0631\\u0627 \\u0627\\u0632 \\u0698\\u0631\\u0645\\u0646\\u06cc kusjan \\u0645\\u06cc\\u200c\\u06af\\u06cc\\u0631\\u062f \\u0646\\u0627\\u062f\\u0631\\u0633\\u062a \\u0627\\u0633\\u062a.\"),\n \"sources\": [\"https://www.etymonline.com/word/buss\", W+\"buss\"],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"not_found\",\n    \"note\": \"Watkins 1985 has no entry or index line for BUSS (grep 'BUSS' in AHD_watkins1985.txt returns only BLUNDERBUSS); the 1976 New College appendix is not open online, but since Watkins has no *bu- root the citation cannot support this arrow.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"p.103 s.v. bu-\", \"stance\": \"partial\",\n    \"note\": \"\\\"nhd. Buss 'Ku\\u00df', bussen 'k\\u00fcssen', Busserl 'Ku\\u00df', engl. buss, schwed. (mit regelrechter Lautverschiebung) puss 'Ku\\u00df'\\\" \\u2014 buss belongs to the root, but directly, not through the Germanic 'kiss' verb.\"},\n   {\"src\": \"SYN\", \"where\": \"16.29 \\u00a72, p.1114\", \"stance\": \"partial\",\n    \"note\": \"\\\"NE buss (sb. and vb.), NHG sb. buss, vb. bussen, Sp. buz ('kiss of respect', fr. Arab.), Pol. buzia, buziak; cf. Ir. bus, Alb. buz\\u00eb, Rum. buz\\u0103 'lip'.\\\"\"},\n   {\"src\": \"KLN\", \"where\": \"1966, s.v. buss\", \"stance\": \"partial\",\n    \"note\": \"Klein treats buss as of imitative origin, comparing G. dial. Buss and F. baiser \\u2014 not as a descendant of the Germanic kiss verb.\"}\n ]\n})\ndata[\"entries\"].append(e0)\njson.dump(data, open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/e0.102.json','w'), ensure_ascii=False, indent=1)\nprint(\"ok\", len(json.dumps(data)))\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk102.py"
}
```


### [2026-09-05T14:53:28.017Z] TOOL RESULT

```
ok 20863
```


## [2026-09-05T14:55:32.414Z] TOOL CALL #72: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk102b.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\nP='/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/e0.102.json'\ndata=json.load(open(P))\n\ne1 = {\n \"entry\": 1,\n \"root\": \"Bŭnai\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"Khotanese Saka būnaa- / būnai 'naked' < Proto-Iranian *bagna-ka- (ultimately PIE *negʷ-/*nogʷ- 'naked', with irregular Iranian n- > b-)\",\n \"note\": (\"The root box is Bailey's Khotanese word, and 'Indo-Scythian' is simply Bailey's own name for Khotanese Saka (the title of the \"\n   \"series Indo-Scythian Studies), so the language label is idiosyncratic but not wrong. Bailey, Dictionary of Khotan Saka, s.v. būnaa- \"\n   \"'naked': \\\"SuvP. 71v3 (plur.) byehide būna vasta 'the naked get clothes' ... Z 2:13 būnai jsāte 'he goes about naked' ... From *bagna-, \"\n   \"Oss. D. bæγnæg ..., Sogd. Bud. βγn'k, Chr. βγny, Chorasm. βγnyk, Av. maγna-, Zor.P. brahnak, N.Pers. barahnah ... IE Pok. 769 nogʷ-, \"\n   \"O.Ind. magna-, Goth. nagaþs, Lit. nuogas, O.Slav. nagŭ\\\" — i.e. Nourai's whole chart, node for node, comes from this one paragraph. \"\n   \"Two corrections of substance: (a) the Avestan, Pahlavi/Persian and Sogdian words are SISTER reflexes of Proto-Iranian *bagna(ka)-, not \"\n   \"descendants of the Khotanese form, so the tree shape overstates the relation; (b) the NOTE 'See Nogw: naked for another possible root' \"\n   \"presents the two as alternatives, but modern scholarship makes them one and the same: Wiktionary (s.v. برهنه) derives Proto-Iranian \"\n   \"*bagná from Proto-Indo-Iranian *nagnás from PIE *negʷ- 'naked' — Bailey himself already wrote 'IE Pok. 769 nogʷ-' in this very entry. \"\n   \"The b- of the Iranian branch is an irregular (dissimilatory/taboo) replacement of *n-, and Avestan m- a further step from that b-. \"\n   \"Also note Bailey has a homonym būnai 'darkness' (from bau-/bu- 'to shine'), which is a different word.\"),\n \"note_fa\": (\"جعبهٔ ریشه در اصل واژهٔ ختنی (سکایی) būnaa-/būnai «برهنه» است و برچسب «هندواسکیتی» همان نامی است که بیلی بر ختنی می‌نهاد \"\n   \"(عنوان مجموعهٔ Indo-Scythian Studies). بیلی در فرهنگ ختن سکا ذیل būnaa- می‌نویسد: «از *bagna-؛ آسی bæγnæg، سغدی βγn'k، خوارزمی βγnyk، \"\n   \"اوستایی maγna-، پهلوی brahnak، فارسی نو برهنه»؛ یعنی سراسر این نمودار از همین یک بند گرفته شده است. دو نکته: نخست آنکه واژه‌های اوستایی و \"\n   \"پهلوی و سغدی «هم‌ریشه»اند نه «برآمده» از صورت ختنی، و پیکان‌ها را باید بازتاب یک ستاک مشترک ایرانی باستان *bagna-ka- دانست. دوم آنکه \"\n   \"یادداشت نورایی این ریشه را «جایگزین احتمالی» ریشهٔ Nogw می‌شمارد، حال آنکه پژوهش امروزی هر دو را یکی می‌داند: *bagná ایرانی از \"\n   \"*nagnás هندوایرانی و آن از *negʷ- هندواروپایی است و ب آغازین جانشین نامنظم ن است.\"),\n \"sources\": [\"https://en.wiktionary.org/wiki/%D8%A8%D8%B1%D9%87%D9%86%D9%87\"],\n \"ref_check\": [\n   {\"ref\": \"ISS:256\", \"status\": \"supports\",\n    \"note\": (\"Indo-Scythian Studies VI (Prolexis to the Book of Zambasta) is not online, but the cited page is independently confirmed: \"\n      \"Gharib, Sogdian Dictionary no. 2576 'βγn'k ... ©*bagna-ka-, Khwar. βγnyk; Oss. bæγnæg ... naked' cites exactly 'SCE 385; Prolexis. 256'. \"\n      \"Bailey's own Dictionary of Khotan Saka s.v. būnaa- (ISS_alt_DKS.txt line 5476) repeats the same etymology and the same list of cognates.\")}\n ],\n \"consulted\": [\n   {\"src\": \"ISS_alt_DKS\", \"where\": \"Bailey, Dictionary of Khotan Saka, s.v. būnaa- (line 5476)\", \"stance\": \"supports\",\n    \"note\": \"\\\"būnaa- 'naked' ... From *bagna-, Oss. DI. bæγnæg ... Sogd. Bud. βγn'k, Chr. βγny, Chorasm. βγnyk, Av. maγna-, Zor.P. brahnak, N.Pers. barahnah; Wanetsi būn. IE Pok. 769 nogʷ-, O.Ind. magna-, Got. nagaþs, Lit. nuogas, O.Slav. nagŭ\\\".\"},\n   {\"src\": \"ISS_alt_DKS\", \"where\": \"s.v. haspūnaka, hāmnā- (lines 8483, 8505)\", \"stance\": \"supports\",\n    \"note\": \"Bailey twice gives the phonology explicitly: \\\"-gn- resulted in -n- in būnaa- (*bagna-ka-) 'naked'\\\" — so Khotanese būnaa- < *bagnaka- with -gn- > -n-.\"},\n   {\"src\": \"POK\", \"where\": \"p.769 nogʷ- (as cited by Bailey)\", \"stance\": \"partial\",\n    \"note\": \"Bailey files the group under Pokorny's nogʷ- 'naked' (p.769) — the same root as Nourai's cross-referenced 'Nogw' entry, which shows the two are not competing etymologies.\"}\n ],\n \"nodes\": []\n}\n\ne1[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Avestan\", \"words\": \"mağna\",\n \"verdict\": \"plausible\",\n \"derivation\": (\"Young Avestan maγna- adj. 'naked, stripped' is real and correctly glossed: Bartholomae, Altiranisches Wörterbuch \"\n   \"(col. ~1111, s.v.) \\\"j. maγna- Adj. (fem. *-ā-) 1) 'nackt, entblösst': ava … vastra … V.5.10 … Yt.17.56\\\", and he adds the comparison \"\n   \"\\\"vgl. … oss. bæγnæg … gr. γυμνός\\\" and the Pahlavi rendering of the Zand: \\\"Pü.: brahnak\\\". The relation to the root box is therefore \"\n   \"well founded — Bailey lists Av. maγna- among the reflexes of *bagna- — but it is a cognate, not a descendant of a Khotanese word: \"\n   \"Proto-Iranian *bagna- gives Khotanese būnaa-, Sogdian βγn'k, Ossetic bæγnæg, and Avestan maγna- with a further dissimilatory b- > m- \"\n   \"before the nasal (b…n > m…n). Because the direction of the arrow is wrong (and because some scholars, e.g. those who compare Skt. \"\n   \"magna- 'sunk' or take maγna- with γuna-, hesitate over the m-), the node is plausible rather than confirmed.\"),\n \"derivation_fa\": (\"صفت اوستایی متأخر maγna- «برهنه، عریان» واقعی است؛ بارتولومه در فرهنگ ایرانی باستان (ستون ۱۱۱۱ حدوداً) آن را «nackt, \"\n   \"entblösst» معنی می‌کند، با آسی bæγnæg و یونانی γυμνός می‌سنجد و برگردان پهلوی زند آن را brahnak می‌آورد. پیوند این واژه با جعبهٔ ریشه درست \"\n   \"است، اما نه به‌صورت «فرزندی»: maγna- و būnaa- ختنی و βγn'k سغدی هر سه بازتاب یک ستاک ایرانی باستان *bagna- اند، و م آغازین اوستایی حاصل \"\n   \"همگونی/ابدال ب به م پیش از ن است (b…n > m…n). پس جهت پیکان نادرست است و ادعای نورایی «با احتیاط پذیرفتنی» است.\"),\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"ISS:256\", \"status\": \"supports\",\n    \"note\": \"Not directly readable (Prolexis is not online), but Bailey's parallel entry (DKS s.v. būnaa-) names \\\"Av. maγna-\\\" in the *bagna- list, so the cited page evidently does the same.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch, s.v. maγna- (BRT.txt line ~19548, between the column marks 1107/1108 and the next)\", \"stance\": \"supports\",\n    \"note\": \"\\\"j. maγna- Adj. … 'nackt, entblösst': ava … vastra V.5.10; — Yt.17.56 … Vgl. … oss. bæγnæg, gr. γυμνός … Pü.: brahnak\\\" — gives both the meaning and, in the Pahlavi gloss, Nourai's next node.\"},\n   {\"src\": \"BRT\", \"where\": \"s.v. maγnanta- (BRT.txt line 19550)\", \"stance\": \"supports\",\n    \"note\": \"\\\"j. maγnanta- Adj. 'nackt, entblösst' … Ableit. aus maγna-, auffäll. Bildung; vgl. Horn GIrPh. I b. 146. — Pü.: rūšak\\\" — a second Avestan derivative of the same stem.\"},\n   {\"src\": \"ISS_alt_DKS\", \"where\": \"s.v. būnaa-\", \"stance\": \"supports\",\n    \"note\": \"Bailey groups \\\"Av. maγna-\\\" with Khotanese būnaa-, Sogd. βγn'k and Zor.P. brahnak under *bagna-.\"},\n   {\"src\": \"ARY\", \"where\": \"grep برهنه / maγna in ARY_pages.txt\", \"stance\": \"silent\",\n    \"note\": \"Aryanpur's Persian IE-roots dictionary yields no hit for this family in the OCR.\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 2, \"lang\": \"Pahlavi\", \"words\": \"brahnak\",\n \"verdict\": \"plausible\",\n \"derivation\": (\"Middle Persian brahnag 'naked' is well attested: MacKenzie, Concise Pahlavi Dictionary p.19 \\\"brahnag [b(l)hnk' | M brhng, \"\n   \"N barahna] naked\\\" (Book Pahlavi bl(ʾ)hnk', Manichaean brhng), and it is the standing Pahlavi rendering of Avestan maγna- in the Zand \"\n   \"(Bartholomae's \\\"Pü.: brahnak\\\"). But that Zand equivalence is a translation, not a phonological descent: brahnag cannot come out of \"\n   \"maγna- (Avestan -γn- would give MP -yn-/-hn- with no r, and Middle Persian in any case continues Old Persian, not Avestan). The modern \"\n   \"account is that MP brahnag reflects Proto-Iranian *bagnákah 'naked' with a secondary, unexplained -r- (Wiktionary, s.v. برهنه, \"\n   \"\\\"from Middle Persian bl(ʾ)hnk' (brahnag), from Proto-Iranian *bagnákah, with secondary -r-, from Proto-Iranian *bagná\\\"). So the word \"\n   \"and the family are right, the arrow from Avestan is not.\"),\n \"derivation_fa\": (\"فارسی میانه brahnag «برهنه» به‌خوبی گواهی شده است: مکنزی در فرهنگ کوچک پهلوی می‌آورد «brahnag [bl(ʾ)hnk' | مانوی brhng، \"\n   \"فارسی نو برهنه] naked»؛ و همین واژه برگردان همیشگی maγna- اوستایی در زند است (بارتولومه: Pü. brahnak). اما این برابری زندی ترجمه است نه \"\n   \"تحول آوایی: از maγna- به brahnag نمی‌توان رسید (خوشهٔ -γn- اوستایی در فارسی میانه ر نمی‌زاید، و فارسی میانه دنبالهٔ پارسی باستان است نه \"\n   \"اوستایی). دیدگاه امروزی: brahnag بازتاب *bagnákah ایرانی باستان است با ر افزودهٔ ثانوی. پس واژه درست است ولی پیکان اوستایی←پهلوی نادرست.\"),\n \"sources\": [\"https://en.wiktionary.org/wiki/%D8%A8%D8%B1%D9%87%D9%86%D9%87\"],\n \"ref_check\": [\n   {\"ref\": \"ISS:256\", \"status\": \"supports\",\n    \"note\": \"Bailey's parallel entry (DKS s.v. būnaa-) lists \\\"Zor.P. brahnak\\\" in the *bagna- group; the Prolexis page evidently gives the same list, since Gharib cites Prolexis 256 for the Sogdian member.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary, s.v. brahnag (PHD.txt line 278; English index line 2885 'naked brahnag')\", \"stance\": \"supports\",\n    \"note\": \"\\\"brahnag [b/(?)hnk' | M brhng, N barahna] naked.\\\" — Book Pahlavi spelling with -l- for -r-, Manichaean brhng, New Persian barahna.\"},\n   {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II (glossary)\", \"stance\": \"silent\",\n    \"note\": \"grep 'brahn'/'brhnk' in NYB_vol2_glossary.txt gives only brihēnīdan 'to predestine' (line 1029) — the word does not occur in Nyberg's text selection.\"},\n   {\"src\": \"ISS_alt_DKS\", \"where\": \"s.v. būnaa-\", \"stance\": \"supports\",\n    \"note\": \"\\\"Av. maγna-, Zor.P. brahnak, N.Pers. barahnah\\\" listed together under *bagna-.\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 3, \"lang\": \"Persian\", \"words\": \"berehneh\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"NP برهنه, classical barahna, modern colloquial berehne 'naked' (Nourai's 'berehneh' is the modern pronunciation) continues \"\n   \"Middle Persian brahnag directly: MP -ag > NP -a/-e (as in zindag > zinde, murdag > morde), and the initial cluster br- is broken by an \"\n   \"anaptyctic vowel (brahnag > barahna). MacKenzie's entry already gives the equation \\\"brahnag … N barahna\\\". Wiktionary: \\\"From Middle \"\n   \"Persian bl(ʾ)hnk' (brahnag), from Proto-Iranian *bagnákah, with secondary -r-, from Proto-Iranian *bagná 'naked', from Proto-Indo-Iranian \"\n   \"*nagnás, from Proto-Indo-European *negʷ- 'naked'\\\"; Ottoman/Turkish بورهنه bürehne is a loan from Classical Persian. The immediate edge \"\n   \"Pahlavi > Persian, which is what this node asserts, is correct; the note 'See Nogw for another possible root' is answered above — \"\n   \"*negʷ- is not an alternative but the ultimate source of the same word.\"),\n \"derivation_fa\": (\"«برهنه» (کلاسیک barahna، امروزی berehne) مستقیماً دنبالهٔ فارسی میانهٔ brahnag است: پسوند -ag فارسی میانه در فارسی نو به \"\n   \"-ه بدل شده (مانند zindag > زنده، murdag > مرده) و خوشهٔ آغازین br- با واکهٔ میانجی شکسته شده است (brahnag > barahna). مکنزی خود برابری \"\n   \"«brahnag … فارسی نو برهنه» را می‌آورد و ویکی‌واژه زنجیره را چنین می‌دهد: فارسی میانه brahnag < ایرانی باستان *bagnákah (با ر ثانوی) < \"\n   \"*bagná < هندوایرانی *nagnás < هندواروپایی *negʷ-. پس این حلقه از نمودار درست است، و یادداشت «ریشهٔ دیگر: Nogw» در واقع همان ریشهٔ نهایی \"\n   \"همین واژه است، نه رقیب آن.\"),\n \"sources\": [\"https://en.wiktionary.org/wiki/%D8%A8%D8%B1%D9%87%D9%86%D9%87\"],\n \"ref_check\": [\n   {\"ref\": \"ISS:256\", \"status\": \"supports\",\n    \"note\": \"Bailey's list (DKS s.v. būnaa-) ends \\\"...Zor.P. brahnak, N.Pers. barahnah\\\" — precisely this node.\"},\n   {\"ref\": \"MON:517\", \"status\": \"not_checked\",\n    \"note\": \"Mo'in's six-volume Farhang is not online and the two-volume Adena condensation (MON_part1.txt) has no برهنه headword in the OCR (only compounds such as پابرهنه); vajehyab/abadis cannot be mapped to page 517.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"s.v. brahnag\", \"stance\": \"supports\",\n    \"note\": \"\\\"brahnag … N barahna\\\" — MacKenzie explicitly equates the Middle Persian word with New Persian barahna.\"},\n   {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' (BQT_v1..v5_pages.txt)\", \"stance\": \"silent\",\n    \"note\": \"No برهنه headword found in the OCR of any volume (Borhan is arranged by final letter, so it belongs in the hāʾ chapter; the word occurs only inside other entries, e.g. v.1 line 32053 'برهنه و عریان - و تهی و خالی' s.v. تهی).\"},\n   {\"src\": \"HRN\", \"where\": \"Horn, Grundriss\", \"stance\": \"silent\",\n    \"note\": \"grep 'barahna'/'brahnak'/'nackt' in HRN.txt returns only no. 9958 on rut 'nackt, leer' — Horn has no entry for barahna.\"},\n   {\"src\": \"MON\", \"where\": \"2-vol Adena condensation\", \"stance\": \"silent\",\n    \"note\": \"no برهنه headword in the OCR.\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 4, \"lang\": \"Sogdian\", \"words\": \"bğn`k, bğny\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"Both Sogdian forms are correctly cited and correctly glossed. Gharib, Sogdian Dictionary, no. 2576: \\\"βγn'k (Buddhist) \"\n   \"βaγnē … ©*bagna-ka-, Khwar. βγnyk; Oss. bæγnæg … naked. SCE 385; Prolexis. 256\\\", and no. 2580: \\\"βγny (Christian) βaγnē, pl. -t, \"\n   \"= βγn'k … naked. Sogdica 39.22; STii 27.12, 18\\\". βγn'k is the Buddhist Sogdian spelling of *bagnaka- with the productive -āk suffix, \"\n   \"βγny the Christian Sogdian spelling of the same word (Sogdian -ē < -aka-). As with the other branches, these are sister reflexes of \"\n   \"Proto-Iranian *bagna(ka)- rather than descendants of the Khotanese form; but since Sogdian βγn'k preserves the -γn- that Khotanese lost \"\n   \"(būnaa- < *bagnaka-), the Sogdian word is in fact the most conservative member of the group.\"),\n \"derivation_fa\": (\"هر دو صورت سغدی درست نقل شده‌اند. غریب در فرهنگ سغدی شمارهٔ ۲۵۷۶ می‌آورد: «βγn'k (سغدی بودایی) βaγnē، از *bagna-ka-، \"\n   \"خوارزمی βγnyk، آسی bæγnæg، «برهنه»؛ منابع: SCE 385؛ Prolexis 256» و شمارهٔ ۲۵۸۰: «βγny (سغدی مسیحی) … همان βγn'k». صورت بودایی املای \"\n   \"‑'k و صورت مسیحی املای ‑y از یک واژه‌اند (سغدی ‑ē از ‑aka‑ کهن). این واژه‌ها نیز هم‌ریشهٔ صورت ختنی‌اند نه برآمده از آن؛ اما چون سغدی \"\n   \"خوشهٔ ‑γn‑ را نگه داشته و ختنی آن را به ‑n‑ ساده کرده، صورت سغدی کهن‌ترین چهرهٔ این واژه است. ارجاع نورایی به Prolexis 256 با ارجاع غریب \"\n   \"دقیقاً می‌خواند.\"),\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"ISS:256\", \"status\": \"supports\",\n    \"note\": \"Independently corroborated: Gharib no. 2576 (SOD.txt line 24676) cites \\\"Prolexis. 256\\\" for exactly this word — i.e. Bailey's Prolexis p.256 does contain the Sogdian βγn'k 'naked'.\"}\n   ],\n \"consulted\": [\n   {\"src\": \"SOD\", \"where\": \"Gharib, Sogdian Dictionary nos. 2576 and 2580 (SOD.txt lines 24676, 24705)\", \"stance\": \"supports\",\n    \"note\": \"no. 2576 \\\"βγn'k B … ©*bagna-ka-, Khwar. βγnyk; Oss. bæγnæg … naked … SCE 385; Prolexis. 256\\\"; no. 2580 \\\"βγny C … = βγn'k … naked\\\"; the English index (line 91953) lists 'naked 2576, 2580'.\"},\n   {\"src\": \"ISS_alt_DKS\", \"where\": \"s.v. būnaa-\", \"stance\": \"supports\",\n    \"note\": \"\\\"Sogd. Bud. βγn'k, Chr. βγny\\\" — Bailey cites both spellings, exactly the pair in this node.\"}\n ]\n})\ndata[\"entries\"].append(e1)\njson.dump(data, open(P,'w'), ensure_ascii=False, indent=1)\nprint(\"ok entries:\", len(data[\"entries\"]))\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk102b.py"
}
```


### [2026-09-05T14:55:34.594Z] TOOL RESULT

```
ok entries: 2
```


## [2026-09-05T14:58:25.362Z] TOOL CALL #73: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk102c.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\nP='/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/e0.102.json'\ndata=json.load(open(P))\n\nGRK=\"https://en.wiktionary.org/wiki/%CE%B2%CE%AC%CE%BB%CF%83%CE%B1%CE%BC%CE%BF%CE%BD\"\nBAL=\"https://en.wiktionary.org/wiki/balsam\"\nBALM=\"https://www.etymonline.com/word/balm\"\nBASH=\"https://en.wiktionary.org/wiki/%D8%A8%D8%B4%D8%A7%D9%85\"\nABD=\"https://abadis.ir/fatofa/%D8%A8%D9%84%D8%B3%D8%A7%D9%85/\"\n\ne3 = {\n \"entry\": 3,\n \"root\": \"Busmâ, Besmâ\",\n \"verdict\": \"plausible\",\n \"modern_form\": \"Aramaic busmā / Syriac besmā 'fragrance, spice, perfume', from Proto-Semitic *buśm-\",\n \"note\": (\"The two forms are real and correctly identified: Klein (1966) s.v. balsam names \\\"Heb. bāsām, which is rel. to Heb. bésem, \"\n   \"Aram. busmā, Syr. besmā, Arab. bashām, 'balsam, spice, perfume'\\\" — Nourai's 'Busmâ' is the Aramaic, 'Besmâ' the Syriac form, and both \"\n   \"belong to the Semitic root b-ś-m 'to be fragrant'. The gloss 'perfume' is right. What is only 'plausible' is making Aramaic the head of \"\n   \"the tree: Wiktionary's etymology tree for balsam starts one step higher, at Proto-Semitic *buśm-, from which Hebrew bāśām and Aramaic \"\n   \"busmā both descend, and it is the Hebrew (or a Canaanite/Phoenician) form, not the Aramaic one, that Greek borrowed. Lokotsch no. 293 \"\n   \"says the same: \\\"Hebr. bɛsɛm 'Balsamstaude, Balsam', eine Handelsware, welche die Griechen nebst dem Namen von den Phöniziern erhielten\\\". \"\n   \"So the root box should read Proto-Semitic (or Northwest Semitic) rather than Aramaic; everything below it is essentially right.\"),\n \"note_fa\": (\"هر دو صورت واقعی‌اند: کلاین ذیل balsam می‌نویسد «عبری bāsām که با عبری bésem، آرامی busmā، سریانی besmā و عربی bašām خویشاوند \"\n   \"است»؛ پس «بسما» صورت آرامی و «بسما/بِسما» صورت سریانی از ریشهٔ سامی b-ś-m «خوشبو بودن» است و معنی «عطر» درست است. اما نشاندن آرامی در رأس \"\n   \"درخت تنها «با احتیاط پذیرفتنی» است: درخت ریشه‌شناسی ویکی‌واژه از سامی آغازین *buśm- آغاز می‌کند که عبری bāśām و آرامی busmā هر دو از آن‌اند، \"\n   \"و یونانی نیز صورت عبری/کنعانی را وام گرفته است نه آرامی را؛ لوکوچ (شمارهٔ ۲۹۳) هم می‌گوید یونانیان این کالا را با نامش از فنیقیان گرفتند. \"\n   \"پس بهتر بود جعبهٔ ریشه «سامی آغازین» می‌بود؛ بقیهٔ نمودار درست است.\"),\n \"sources\": [BAL, GRK, BALM],\n \"ref_check\": [\n   {\"ref\": \"TAD:12\", \"status\": \"supports\",\n    \"note\": (\"al-Unaysi, Tafsir al-alfaz al-dakhila, leaf 16 of TAD_pages.txt (= printed p.~12), s.v. بلسم: \"\n      \"«بلسم في اليونانية βάλσαμον مأخوذ من الارامية بسما، أي عطر وطيب، ومنه البلسان» — 'balsam: in Greek balsamon, taken from Aramaic \"\n      \"busmā, i.e. perfume and fragrance; and from it (comes) al-balasān'. That is Nourai's root, his gloss and his Greek node in one line.\")},\n   {\"ref\": \"KLN:144\", \"status\": \"supports\",\n    \"note\": \"Klein 1966 p.144 s.v. balsam: \\\"L. balsamum … fr. Gk. βάλσαμον, fr. Heb. bāsām, which is rel. to Heb. bésem, Aram. busmā, Syr. besmā, Arab. bashām, 'balsam, spice, perfume'.\\\" (KLN_1966.txt leaf containing pp.144-145.)\"}\n ],\n \"consulted\": [\n   {\"src\": \"LKT\", \"where\": \"Lokotsch no. 293 (LKT.txt line 851)\", \"stance\": \"partial\",\n    \"note\": \"\\\"Hebr. bɛsɛm: 'Balsamstaude, Balsam', eine Handelsware, welche die Griechen nebst dem Namen von den Phöniziern erhielten. Gr. βάλσαμον, lat. balsamum; hieraus it. balsamo … dtsch. Balsam, ndl. balsem, engl. balm\\\" — same chain, but headed by the Hebrew/Phoenician form, not the Aramaic.\"},\n   {\"src\": \"KLN\", \"where\": \"1966 p.144 s.v. balsam\", \"stance\": \"partial\",\n    \"note\": \"Klein makes the Semitic words 'related', i.e. cognates of one root, and derives Greek from Hebrew — he does not derive Hebrew from Aramaic.\"},\n   {\"src\": \"AFA\", \"where\": \"Fraenkel, Die aramäischen Fremdwörter im Arabischen\", \"stance\": \"silent\",\n    \"note\": \"grep 'balsam'/'busm' in AFA.txt yields nothing usable (only a Bible-quotation line 6200); Fraenkel has no entry for بلسان in the OCR.\"}\n ],\n \"nodes\": []\n}\n\ne3[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Hebrew\", \"words\": \"bâsam\",\n \"verdict\": \"plausible\",\n \"derivation\": (\"Biblical Hebrew בָּשָׂם bāśām 'spice, balsam, balsam tree' (also בֹּשֶׂם bośem, plural besāmīm; Exodus 30:23, Song of Songs \"\n   \"5:1) is real and correctly glossed 'spice, balsam plant'. But no source derives it FROM Aramaic. Klein p.144 writes that Heb. bāsām \"\n   \"\\\"is rel. to Heb. bésem, Aram. busmā, Syr. besmā, Arab. bashām\\\" — a set of cognates from the common Semitic root b-ś-m; Wiktionary's \"\n   \"tree puts Proto-Semitic *buśm- above them all. Etymonline (s.v. balm) is identical: \\\"Hebrew (Semitic) basam 'spice', which is related \"\n   \"to Aramaic busma, Arabic basham\\\". Since Hebrew is if anything the older attestation (10th-6th c. BCE) and Aramaic busmā the later, the \"\n   \"arrow is at best a shorthand for 'both from the same Semitic root'. Nourai's transliteration bâsam for bāśām also loses the śin (ś, \"\n   \"originally a lateral [ɬ]), which matters for the Greek node below.\"),\n \"derivation_fa\": (\"عبری کتاب‌مقدسی בָּשָׂם bāśām «ادویه، بلسان، درخت بلسان» (نیز בֹּשֶׂם bośem؛ سفر خروج ۳۰:۲۳) واقعی است و معنی داده‌شده درست. \"\n   \"اما هیچ منبعی آن را «از» آرامی نمی‌گیرد: کلاین می‌گوید عبری bāsām «هم‌ریشهٔ» عبری bésem، آرامی busmā، سریانی besmā و عربی bašām است، و \"\n   \"ویکی‌واژه همهٔ آن‌ها را از سامی آغازین *buśm- می‌داند؛ اتیمولاین نیز همین را می‌گوید. چون گواهی عبری کهن‌تر از آرامی است، این پیکان تنها \"\n   \"کوتاه‌نوشتی برای «هر دو از یک ریشهٔ سامی» است. افزون بر این، آوانگاشت bâsam حرف «سین» ویژه (śin، در اصل [ɬ]) را نشان نمی‌دهد و همین حرف \"\n   \"است که چهرهٔ یونانی واژه را توضیح می‌دهد. پس: با احتیاط پذیرفتنی.\"),\n \"sources\": [BAL, BALM],\n \"ref_check\": [\n   {\"ref\": \"KLN:144\", \"status\": \"partial\",\n    \"note\": \"Klein p.144 has the Hebrew word and the Aramaic word, but as cognates: \\\"fr. Heb. bāsām, which is rel. to Heb. bésem, Aram. busmā, Syr. besmā, Arab. bashām\\\" — not Hebrew < Aramaic.\"}\n ],\n \"consulted\": [\n   {\"src\": \"LKT\", \"where\": \"no. 293\", \"stance\": \"partial\",\n    \"note\": \"Lokotsch takes the Hebrew word as the source of the Greek one, with no Aramaic intermediary.\"},\n   {\"src\": \"KLN\", \"where\": \"1966 p.144 s.v. balsam\", \"stance\": \"partial\",\n    \"note\": \"as quoted in ref_check: 'rel. to', i.e. cognate.\"},\n   {\"src\": \"FVQ\", \"where\": \"Jeffery, Foreign Vocabulary of the Qurʾān\", \"stance\": \"silent\",\n    \"note\": \"grep 'balsam'/'basham' in FVQ.txt: no entry (the word is not Qurʾānic).\"}\n ]\n})\n\ne3[\"nodes\"].append({\n \"id\": 2, \"lang\": \"Greek\", \"words\": \"balsamon\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"Ancient Greek βάλσαμον bálsamon 'the balsam tree (Commiphora opobalsamum) and its resin' (Theophrastus, Hist. Plant. IX; \"\n   \"poetic variant βλάσαμον) is a Semitic loan taken over with the trade in the resin. Wiktionary: \\\"Of Semitic origin, borrowed from Hebrew \"\n   \"בָּשָׂם (bāśām, 'sweet spice, sweet smell'), the consonant sequence in Greek being explained as an attempt at rendering שׂ (ś) sounding \"\n   \"back then [ɬ]\\\" — i.e. the lateral fricative ś was heard by Greeks as -ls-, which is why bāśām comes out as bál-samon. Lokotsch (no. 293) \"\n   \"adds the channel: the Greeks got the ware and its name from the Phoenicians. Klein p.144 gives the same derivation. Nourai's arrow \"\n   \"Hebrew > Greek and his gloss 'balsam plant' are both correct.\"),\n \"derivation_fa\": (\"یونانی باستان βάλσαμον «درخت بلسان و صمغ آن» (تئوفراستوس) وام‌واژه‌ای سامی است که همراه خودِ کالا وارد یونانی شده. \"\n   \"ویکی‌واژه: «از عبری בָּשָׂם bāśām وام گرفته شده؛ خوشهٔ همخوانی ‑ls‑ در یونانی کوششی است برای نشان‌دادن حرف שׂ (ś) که در آن روزگار [ɬ] \"\n   \"تلفظ می‌شد» — یعنی «سین» جانبی سامی در گوش یونانی «ل + س» شنیده شده و از bāśām صورت bál-samon پدید آمده است. لوکوچ (۲۹۳) راه انتقال را \"\n   \"فنیقیان می‌داند و کلاین نیز همین را می‌گوید. پس ادعای نورایی در این حلقه درست است.\"),\n \"sources\": [GRK, BAL],\n \"ref_check\": [\n   {\"ref\": \"KLN:144\", \"status\": \"supports\",\n    \"note\": \"Klein p.144 s.v. balsam: \\\"L. balsamum … fr. Gk. βάλσαμον, fr. Heb. bāsām\\\" — exactly this arrow.\"}\n ],\n \"consulted\": [\n   {\"src\": \"LKT\", \"where\": \"no. 293\", \"stance\": \"supports\",\n    \"note\": \"\\\"eine Handelsware, welche die Griechen nebst dem Namen von den Phöniziern erhielten. Gr. βάλσαμον, lat. balsamum\\\".\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat s.v. Balm (SKT.txt line 1357)\", \"stance\": \"supports\",\n    \"note\": \"\\\"L. balsamum. — Gk. βάλσαμον, fragrant resin of the βάλσαμος, or balsam-tree. Prob. Semitic; cf. Heb. bāsām, balsam.\\\"\"},\n   {\"src\": \"TAD\", \"where\": \"al-Unaysi, leaf 16 (~p.12)\", \"stance\": \"supports\",\n    \"note\": \"«بلسم في اليونانية βάλσαμον مأخوذ من الارامية بسما» — the Arabic lexicographer likewise routes the Greek word from the Semitic one.\"}\n ]\n})\n\ne3[\"nodes\"].append({\n \"id\": 3, \"lang\": \"Arabic\", \"words\": \"bašâm; balsâm\",\n \"verdict\": \"disputed\",\n \"derivation\": (\"Two words with two different histories, and the chart puts both under the Greek node. (1) بَلْسَم balsam / بَلَسَان balasān \"\n   \"'balsam, the balsam tree and its resin' IS the Greek word, taken into Arabic through Syriac/Greek medical and pharmacological literature \"\n   \"(the -ān of balasān is the usual Arabic adaptation of Greek -on); al-Unaysi (TAD, leaf 16) states it outright and adds «ومنه البلسان» \"\n   \"'and from it (comes) al-balasān'. For this word Nourai's arrow is right. (2) بَشَام bašām is NOT a Greek loan: it is the inherited Arabic \"\n   \"cognate of Hebrew bāśām, from the same Semitic root b-š/ś-m, and denotes the balsam tree (Commiphora gileadensis) growing in the Hijaz \"\n   \"and Yemen — Wiktionary treats بَشَام as an alternative form of بَيْلَسان, and Klein p.144 and Etymonline (s.v. balm) both list \\\"Arab. \"\n   \"bashām\\\" as merely 'related to' Heb. bāsām, i.e. a cognate, not a borrowing. The glosses are also slipped: bašām is the tree, not \"\n   \"'perfume', and balsām/balasān is the resin/plant. Hence disputed for the node: one of the two words did not come by the route drawn.\"),\n \"derivation_fa\": (\"در این گره دو واژه با دو تاریخ متفاوت زیر یک پیکان نشسته‌اند. نخست «بَلْسَم/بَلَسان» که همان واژهٔ یونانی است و از راه \"\n   \"نوشته‌های پزشکی سریانی‑یونانی به عربی رسیده (پسوند ‑ان در بلسان برگردان معمول ‑ون یونانی است)؛ العنیسی در همان صفحه می‌گوید «ومنه البلسان»؛ \"\n   \"پس برای این واژه پیکان نورایی درست است. دوم «بَشام» که وام‌واژهٔ یونانی نیست، بلکه صورت اصیل عربی از همان ریشهٔ سامی b-š-m و هم‌ریشهٔ عبری \"\n   \"bāśām است و نام درخت بلسان حجاز و یمن (Commiphora) است؛ کلاین و اتیمولاین هر دو آن را تنها «هم‌ریشه» با عبری می‌خوانند نه وام‌گرفته از \"\n   \"یونانی. افزون بر این، معنی‌ها جابه‌جا شده‌اند: بشام نام درخت است نه «عطر». پس پژوهش امروزی این حلقه را برای «بشام» رد می‌کند.\"),\n \"sources\": [BASH, BALM, BAL],\n \"ref_check\": [\n   {\"ref\": \"TAD:12\", \"status\": \"partial\",\n    \"note\": \"al-Unaysi (leaf 16 ≈ p.12) supports the Greek origin of بلسم/بلسان («بلسم في اليونانية βάλσαμον مأخوذ من الارامية بسما ... ومنه البلسان»), but says nothing that would make بشام a Greek loan.\"},\n   {\"ref\": \"MON:567\", \"status\": \"not_checked\",\n    \"note\": \"Mo'in's 6-vol Farhang is not online; the 2-vol condensation (MON_part1.txt line 24816 ff.) has بلسان as the headword and lists «ابوشام، بشام، بلسم مکه، درخت بلسان مکی» as its synonyms, but has no page 567 to check.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"1966 p.144 s.v. balsam\", \"stance\": \"contradicts\",\n    \"note\": \"\\\"Heb. bāsām, which is rel. to Heb. bésem, Aram. busmā, Syr. besmā, Arab. bashām\\\" — Arabic bashām is a cognate of the Hebrew word, not a descendant of Greek βάλσαμον.\"},\n   {\"src\": \"AFM\", \"where\": \"Addi Shir, al-Alfāẓ al-fārisiyya al-muʿarraba\", \"stance\": \"silent\",\n    \"note\": \"grep بلسان/بشام in AFM_pages.txt: no entry (Addi Shir covers Persian loans, and this word is not Persian).\"},\n   {\"src\": \"LKT\", \"where\": \"no. 293\", \"stance\": \"partial\",\n    \"note\": \"Lokotsch traces the Greek word through Latin into the European languages and does not treat بشام.\"},\n   {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' vol.1 s.v. بشام (BQT_v1_pages.txt line 25823)\", \"stance\": \"contradicts\",\n    \"note\": \"«بشام - بر وزن سلام؛ هر چیز تیره‌رنگ را گویند» — Borhan knows بشام only as 'anything dark-coloured', not as 'perfume'.\"}\n ]\n})\n\ne3[\"nodes\"].append({\n \"id\": 4, \"lang\": \"Persian\", \"words\": \"balsâm; bašâm\",\n \"verdict\": \"plausible\",\n \"derivation\": (\"The direction Arabic > Persian is right — Persian took these plant names from Arabic pharmacology — but the forms and \"\n   \"glosses need correction. The Persian words actually attested are بلسان balasān and بلسم balsam: Mo'in (2-vol condensation, s.v. بلسان) \"\n   \"marks it «[معر.]» (Arabicized/borrowed) and defines it as a shrub of the rue family whose incisions yield a gum, with the synonyms \"\n   \"«ابوشام، بشام، بلسم مکه، درخت بلسان مکی»; Borhan-e Qate' vol.1 s.v. بلسان describes the Egyptian tree, the tapping of its resin \"\n   \"(دهن‌البلسان) and its seed (حب‌البلسان). Nourai's بلسام is not attested in that sense: Dehkhoda's only بلسام entry is «بلسام [بِ] (ع اِ) \"\n   \"برسام … علت و مرض مشهوری است», i.e. a variant of برسام 'pleurisy/delirium' (itself Persian بر + سام). And بشام in Persian is the balsam \"\n   \"TREE (Mo'in's synonym list), while Borhan glosses بشام as 'anything dark-coloured'; 'seed of a balsam plant' is حب‌البلسان. So: right \"\n   \"route, shaky forms and glosses.\"),\n \"derivation_fa\": (\"جهت وام‌گیری (عربی ← فارسی) درست است؛ فارسی این نام‌های گیاهی را از داروشناسی عربی گرفته است. اما صورت‌ها و معنی‌ها نیاز \"\n   \"به اصلاح دارند: آنچه در فارسی گواهی شده «بلسان» و «بلسم» است. معین ذیل «بلسان» آن را «معرّب» می‌نامد و گیاهی از تیرهٔ سدابیان می‌داند که \"\n   \"با خراش صمغ می‌دهد و مترادف‌هایش را «ابوشام، بشام، بلسم مکه، درخت بلسان مکی» می‌آورد؛ برهان قاطع نیز ذیل «بلسان» درخت مصری و روغن آن \"\n   \"(دهن‌البلسان) و دانه‌اش (حب‌البلسان) را شرح می‌دهد. صورت «بلسام» در این معنی گواهی ندارد: تنها مدخل «بلسام» در لغت‌نامهٔ دهخدا «بلسام [بِ] \"\n   \"(ع اِ) برسام … علت و مرض مشهوری است» است، یعنی گونه‌ای از «برسام». «بشام» هم در فارسی نام خودِ درخت است نه «دانهٔ آن» (دانه = حب‌البلسان)، \"\n   \"و برهان آن را «هر چیز تیره‌رنگ» معنی کرده است. پس: راه درست، صورت و معنی لغزان.\"),\n \"sources\": [ABD, BAL],\n \"ref_check\": [\n   {\"ref\": \"MON:540,567\", \"status\": \"not_checked\",\n    \"note\": \"The six-volume Mo'in is not online. In the two-volume Adena condensation the relevant headword is بلسان (MON_part1.txt line 24816): «بلسان: [معر.] (ا.) (گیا.) گیاهی از تیرهٔ سدابیان … ابوشام، بشام، بلسم مکه، درخت بلسان مکی»; there is no بلسام headword, so the pages 540/567 could not be verified.\"}\n ],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"2-vol condensation s.v. بلسان (MON_part1.txt line 24816 ff.)\", \"stance\": \"partial\",\n    \"note\": \"Mo'in has بلسان marked «معر.» with بشام among its synonyms — supports the Arabic origin, but not the form بلسام.\"},\n   {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' vol.1 s.v. بلسان (line 20577) and بشام (line 25823)\", \"stance\": \"partial\",\n    \"note\": \"«بلسان: بروزن سرطان، نام درختی است مشهور در مصر … و آن را بعربی دهن‌البلسان خوانند … و تخم آن را حب‌البلسان گویند»; «بشام: بر وزن سلام، هر چیز تیره‌رنگ را گویند».\"},\n   {\"src\": \"ARY\", \"where\": \"Aryanpur\", \"stance\": \"silent\",\n    \"note\": \"no entry for بلسان/بلسام in the OCR (the book covers inherited Indo-European vocabulary, not Semitic loans).\"}\n ]\n})\n\ne3[\"nodes\"].append({\n \"id\": 5, \"lang\": \"Latin\", \"words\": \"balsamun\",\n \"verdict\": \"transcription_suspect\",\n \"derivation\": (\"The Latin word is balsamum, -ī n. 'balsam, the balsam tree', a straight borrowing of Greek βάλσαμον: Ernout-Meillet, \"\n   \"Dictionnaire étymologique de la langue latine (LAT.txt line 6822) \\\"balsamum,-ī n.: baume, et 'baumier'. Emprunt au gr. βάλσαμον\\\"; \"\n   \"Klein and Skeat give the same. The chart prints balsamun with final -n, which is not a possible Latin nominative-accusative of a \"\n   \"second-declension neuter (-um); it is a slip halfway between Greek -on and Latin -um. The printed page (pdf p.102, 'Latin ⌷ KLN:143 | \"\n   \"balsamun : balsam') shows the error already in the book, so the extraction is faithful. Apart from the misprint the derivation is \"\n   \"correct and uncontroversial: Greek βάλσαμον > Latin balsamum (Pliny, NH XII.111 ff.), whence Late Latin/Old French forms below.\"),\n \"derivation_fa\": (\"واژهٔ لاتین balsamum (خنثای صرف دوم) است و مستقیماً از یونانی βάλσαμον وام گرفته شده؛ ارنو-مه‌یه می‌نویسند: «balsamum, -ī: \"\n   \"baume، و نیز درخت آن. وام از یونانی βάλσαμον». آنچه کتاب چاپ کرده، یعنی balsamun با نون پایانی، در لاتین ممکن نیست (پایانهٔ درست ‑um است) \"\n   \"و صورتی است نیم‌یونانی نیم‌لاتینی. تصویر صفحهٔ ۱۰۲ نشان می‌دهد که همین غلط در خودِ کتاب چاپ شده است؛ پس خطای چاپی کتاب است نه خطای خوانش \"\n   \"اسکن. جز این لغزش، حلقهٔ یونانی ← لاتین درست و بی‌مناقشه است.\"),\n \"error_in\": \"book\",\n \"book_prints\": \"balsamun\",\n \"correct_form\": \"balsamum\",\n \"sources\": [BAL, BALM],\n \"ref_check\": [\n   {\"ref\": \"KLN:143\", \"status\": \"partial\",\n    \"note\": \"The material is in Klein, but on p.144, not 143: the leaf containing pp.144-145 of KLN_1966.txt has \\\"balm, n. — ME. basme, baume, fr. OF. bausme, baume (F. baume), fr. L. balsamum … fr. Gk. βάλσαμον\\\" and \\\"balsam, n. — L. balsamum … fr. Gk. βάλσαμον, fr. Heb. bāsām\\\"; p.143 ends at baleen. Klein spells the Latin word balsamum throughout.\"}\n ],\n \"consulted\": [\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. balsamum (LAT.txt line 6822)\", \"stance\": \"supports\",\n    \"note\": \"\\\"balsamum,-ī n.: baume, et 'baumier'. Emprunt au gr. βάλσαμον\\\" (with the vulgar variant ababalsamum for opobalsamum at line 909) — the Latin form has -um.\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat s.v. balsam (SKT.txt line 1358)\", \"stance\": \"supports\",\n    \"note\": \"\\\"balsam. (L. — Gk.) L. balsamum; as above\\\".\"},\n   {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century s.v. balsam (WEB_vol1.txt line 15423)\", \"stance\": \"supports\",\n    \"note\": \"\\\"bal'sam, n. [AS. balsam; L. balsamum, from …]\\\".\"}\n ]\n})\n\ne3[\"nodes\"].append({\n \"id\": 6, \"lang\": \"English\", \"words\": \"balsam, balsamine, balm, embalm\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"All four are correct, though two of them reach English through French rather than straight from Latin, which the chart's \"\n   \"single Latin>English arrow flattens. (a) balsam was taken directly from Latin balsamum (Old English already had balsam/balsamum; \"\n   \"Klein p.144: \\\"balsam, n. — L. balsamum\\\"). (b) balm is the same word by the French route: Klein \\\"balm, n. — ME. basme, baume, fr. OF. \"\n   \"bausme, baume (F. baume), fr. L. balsamum\\\"; Etymonline dates it c.1200 as basme and notes \\\"the spelling was refashioned 15c.-16c. on \"\n   \"the Latin model\\\", which is why modern balm has an unpronounced -l-. (c) embalm is Old French embaumer (em- 'in' + baume), 14th c., \"\n   \"literally 'to put balm in' (Klein s.v. embalm). (d) balsamine 'garden balsam, Impatiens' is from French balsamine, from Greek βαλσαμίνη \"\n   \"(Klein p.144 s.v. balsamine; Lokotsch no. 293 lists Balsamine/Impatiens Balsamina, engl. balsamine). Skeat and Webster agree.\"),\n \"derivation_fa\": (\"هر چهار واژه درست‌اند، هرچند دوتای آن‌ها نه یکراست از لاتین بلکه از راه فرانسه به انگلیسی رسیده‌اند و نمودار این میانجی را \"\n   \"نشان نمی‌دهد. balsam مستقیماً از لاتین balsamum گرفته شده (انگلیسی کهن هم balsam داشت). balm همان واژه است از راه فرانسه: انگلیسی میانه \"\n   \"basme/baume از فرانسهٔ کهن bausme/baume از لاتین balsamum؛ اتیمولاین آن را از حدود ۱۲۰۰م می‌داند و می‌گوید املای آن در سده‌های ۱۵–۱۶ به \"\n   \"قیاس لاتین بازسازی شد، و از همین رو «ل» در تلفظ امروزی خوانده نمی‌شود. embalm از فرانسهٔ کهن embaumer «بلسان‌اندود کردن، مومیایی کردن» است. \"\n   \"balsamine نیز از فرانسهٔ balsamine و آن از یونانی βαλσαμίνη. کلاین، اسکیت و لوکوچ همگی همین را می‌گویند؛ ادعای نورایی درست است.\"),\n \"sources\": [BALM, BAL],\n \"ref_check\": [\n   {\"ref\": \"KLN:143\", \"status\": \"partial\",\n    \"note\": \"Correct in substance, one page off: in KLN_1966 the entries balm, balsam, balsamine stand on p.144 (\\\"balm, n. — ME. basme, baume, fr. OF. bausme, baume … fr. L. balsamum … fr. Gk. βάλσαμον. See balsam and cp. embalm\\\"; \\\"balsamine, n. the garden balsam. — F., fr. Gk. βαλσαμίνη, 'the balsam plant', fr. βάλσαμον\\\"), and embalm on p.500 (\\\"embalm, tr. v. — OF. (= F.) embaumer, fr. em-, en-, 'in', and baume, 'balm'\\\"), while p.143 ends with baleen.\"}\n ],\n \"consulted\": [\n   {\"src\": \"SKT\", \"where\": \"Skeat s.v. Balm / balsam (SKT.txt lines 1357-1358)\", \"stance\": \"supports\",\n    \"note\": \"\\\"Balm. (F.-L.-Gk.) A modified spelling; M.E. baume. — O.F. bausme. — L. balsamum. — Gk. βάλσαμον … Prob. Semitic; cf. Heb. bāsām, balsam.\\\"\"},\n   {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls s.v. balm (FSD_vol1.txt line 34476)\", \"stance\": \"supports\",\n    \"note\": \"\\\"[< OF. bausme, < L. balsamum; see balsam, n.]\\\", with 'b. of Gilead … Commiphora opobalsamum'.\"},\n   {\"src\": \"WEB\", \"where\": \"Webster's s.v. balm (WEB_vol1.txt line 15416)\", \"stance\": \"supports\",\n    \"note\": \"\\\"balm (bäm), n. (ME. baume; OFr. basme … balsamum, from Gr. balsamon …)\\\".\"},\n   {\"src\": \"LKT\", \"where\": \"no. 293\", \"stance\": \"supports\",\n    \"note\": \"\\\"dtsch. Balsam, ndl. balsem, engl. balm … Vgl. noch Balsamine, Impatiens Balsamina, engl. balsamine, balsam\\\".\"}\n ]\n})\n\ndata[\"entries\"].append(e3)\nout='/home/sfmqrb/git/rishe/data/verification/page-102.json'\njson.dump(data, open(out,'w'), ensure_ascii=False, indent=1)\nprint(\"written\", out, \"entries:\", len(data[\"entries\"]))\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk102c.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-102.json > /dev/null && echo \"JSON OK\" && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 102"
}
```


### [2026-09-05T14:58:28.081Z] TOOL RESULT

```
written /home/sfmqrb/git/rishe/data/verification/page-102.json entries: 3
JSON OK
nodes verified: 13/13
node verdicts: {'plausible': 5, 'disputed': 3, 'confirmed': 4, 'transcription_suspect': 1}
root verdicts: {'confirmed': 2, 'plausible': 1}
ref checks: {'supports': 6, 'contradicts': 1, 'not_found': 1, 'not_checked': 3, 'partial': 4}
books consulted: {'contradicts': 6, 'supports': 19, 'silent': 11, 'partial': 8} | by book: {'BQT': 4, 'KLN': 4, 'LKT': 4, 'MON': 3, 'ISS_alt_DKS': 3, 'SKT': 3, 'HRN': 2, 'SYN': 2, 'POK': 2, 'BRT': 2, 'ARY': 2, 'PHD': 2, 'WEB': 2, 'CHEUNG': 1, 'HUB': 1, 'NYB': 1, 'SOD': 1, 'FVQ': 1, 'TAD': 1, 'AFM': 1, 'LAT': 1, 'FSD': 1}
```


## [2026-09-05T14:58:33.153Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'NR<=12915' KLN_1966.txt | tr -cd '\\f' | wc -c; sed -n '12900,12920p' KLN_1966.txt | grep -o \"^[0-9]\\{3\\}$\" ; awk 'NR>=12880 && NR<=12930' KLN_1966.txt | grep -oE \"\\b(49[0-9]|50[0-9])\\b\" | head"
}
```


### [2026-09-05T14:58:35.202Z] TOOL RESULT

```
279
512
513
```


## [2026-09-05T14:58:39.834Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 - <<'PY'\nimport json\np='data/verification/page-102.json'\nd=json.load(open(p))\nn=[x for x in d['entries'][2]['nodes'] if x['id']==6][0]\nrc=n['ref_check'][0]\nrc['note']=rc['note'].replace(\"and embalm on p.500\", \"and embalm on p.512/513 (KLN_1966.txt leaf with the page marks 512/513)\")\njson.dump(d, open(p,'w'), ensure_ascii=False, indent=1)\nprint(rc['note'][:300])\nPY\npython3 tools/verify_check.py 102 | tail -3"
}
```


### [2026-09-05T14:58:42.503Z] TOOL RESULT

```
Correct in substance, one page off: in KLN_1966 the entries balm, balsam, balsamine stand on p.144 ("balm, n. — ME. basme, baume, fr. OF. bausme, baume … fr. L. balsamum … fr. Gk. βάλσαμον. See balsam and cp. embalm"; "balsamine, n. the garden balsam. — F., fr. Gk. βαλσαμίνη, 'the balsam plant', fr.
root verdicts: {'confirmed': 2, 'plausible': 1}
ref checks: {'supports': 6, 'contradicts': 1, 'not_found': 1, 'not_checked': 3, 'partial': 4}
books consulted: {'contradicts': 6, 'supports': 19, 'silent': 11, 'partial': 8} | by book: {'BQT': 4, 'KLN': 4, 'LKT': 4, 'MON': 3, 'ISS_alt_DKS': 3, 'SKT': 3, 'HRN': 2, 'SYN': 2, 'POK': 2, 'BRT': 2, 'ARY': 2, 'PHD': 2, 'WEB': 2, 'CHEUNG': 1, 'HUB': 1, 'NYB': 1, 'SOD': 1, 'FVQ': 1, 'TAD': 1, 'AFM': 1, 'LAT': 1, 'FSD': 1}
```


## [2026-09-05T14:58:48.904Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"brahnag\" PHD_pages.txt | head -3; grep -n \"pdf page\" PHD_pages.txt | head -3"
}
```


### [2026-09-05T14:58:48.963Z] TOOL RESULT

```
1615:brahnag [bW)hnk' 1M brhng, N bara/ma] naked.
7124:month miih, mahigiin.                          naked brahnag.
11094:brahnag                  \~~)      burd
```


## [2026-09-05T14:58:51.689Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'NR<=1615' PHD_pages.txt | tr -cd '\\f' | wc -c; awk 'NR>=1560 && NR<=1660' PHD_pages.txt | grep -oE \"^\\s*[0-9]{1,3}\\s*$\" | head"
}
```


### [2026-09-05T14:58:53.933Z] TOOL RESULT

```
40
```


## [2026-09-05T14:59:00.579Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 - <<'PY'\nimport json\np='data/verification/page-102.json'\nd=json.load(open(p))\nn=[x for x in d['entries'][1]['nodes'] if x['id']==2][0]\nn['derivation']=n['derivation'].replace(\"MacKenzie, Concise Pahlavi Dictionary p.19 \",\"MacKenzie, Concise Pahlavi Dictionary s.v. brahnag \")\njson.dump(d, open(p,'w'), ensure_ascii=False, indent=1)\nprint(n['derivation'][:200])\nPY\npython3 tools/verify_check.py 102 | head -3; git -C /home/sfmqrb/git/rishe status --short"
}
```


### [2026-09-05T14:59:02.746Z] TOOL RESULT

```
Middle Persian brahnag 'naked' is well attested: MacKenzie, Concise Pahlavi Dictionary s.v. brahnag "brahnag [b(l)hnk' | M brhng, N barahna] naked" (Book Pahlavi bl(ʾ)hnk', Manichaean brhng), and it i
nodes verified: 13/13
node verdicts: {'plausible': 5, 'disputed': 3, 'confirmed': 4, 'transcription_suspect': 1}
root verdicts: {'confirmed': 2, 'plausible': 1}
 M data/verification/sources/web/index.jsonl
?? data/verification/page-102.json
?? data/verification/sources/web/05a271aafb1a0bff.txt
?? data/verification/sources/web/07fbd11449f9d7a8.txt
?? data/verification/sources/web/0945a820aeb989eb.txt
?? data/verification/sources/web/0fa547e391100612.txt
?? data/verification/sources/web/16d2f66aea778b19.txt
?? data/verification/sources/web/2cbebb2fd375ff22.txt
?? data/verification/sources/web/3f9c3997d7d9a9a3.txt
?? data/verification/sources/web/74f77df8a2510c40.txt
?? data/verification/sources/web/79ce64222e9cb1b5.txt
?? data/verification/sources/web/887e5e750369dcaa.txt
?? data/verification/sources/web/8d224578ae15d350.txt
?? data/verification/sources/web/92320d4cc191add4.txt
?? data/verification/sources/web/aab5e5692825f204.txt
?? data/verification/sources/web/b72cc012ea3476d4.txt
?? data/verification/sources/web/ba4704aa53949e8c.txt
?? data/verification/sources/web/d6418b07671b1447.txt
?? data/verification/sources/web/e9013f7855d8b8db.txt
?? data/verification/sources/web/f34b4a81558c5bf4.txt
```


## [2026-09-05T14:59:11.671Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; ls -la data/verification/sources/web/ | grep -E \"ecf030988bc14718|edfde12487c14c9b|f3dfe25318cfbf71|f4840fdfd469cbea|79ce64816fac35bc|a62165d7cd005ade|62e5f315114c257e|e63cb446f0b69a89|bef6213ad76b57ce|e7996af531c60e9b\"; echo \"--- count untracked ---\"; git status --short | wc -l"
}
```


### [2026-09-05T14:59:11.739Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb    2665 Sep  5 10:45 62e5f315114c257e.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    7706 Sep  5 10:45 79ce64816fac35bc.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   29972 Sep  5 10:45 a62165d7cd005ade.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    2540 Sep  5 10:47 bef6213ad76b57ce.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    5240 Sep  5 10:45 e63cb446f0b69a89.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    7177 Sep  5 10:49 e7996af531c60e9b.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   17799 Sep  5 10:45 ecf030988bc14718.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   20759 Sep  5 10:45 edfde12487c14c9b.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    5611 Sep  5 10:45 f3dfe25318cfbf71.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    5839 Sep  5 10:45 f4840fdfd469cbea.txt
--- count untracked ---
20
```


## [2026-09-05T14:59:17.910Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; git status --short -- data/verification/sources/web/ | head -30; echo \"---\"; git check-ignore -v data/verification/sources/web/ecf030988bc14718.txt; git log --oneline -1"
}
```


### [2026-09-05T14:59:21.622Z] TOOL RESULT

```
 M data/verification/sources/web/index.jsonl
?? data/verification/sources/web/0196beb4dc1c9663.txt
?? data/verification/sources/web/05a271aafb1a0bff.txt
?? data/verification/sources/web/07fbd11449f9d7a8.txt
?? data/verification/sources/web/0945a820aeb989eb.txt
?? data/verification/sources/web/0fa547e391100612.txt
?? data/verification/sources/web/16d2f66aea778b19.txt
?? data/verification/sources/web/2cbebb2fd375ff22.txt
?? data/verification/sources/web/3c11181a82ef3402.txt
?? data/verification/sources/web/3e3fd35e43a90ab9.txt
?? data/verification/sources/web/3f9c3997d7d9a9a3.txt
?? data/verification/sources/web/74f77df8a2510c40.txt
?? data/verification/sources/web/79ce64222e9cb1b5.txt
?? data/verification/sources/web/887e5e750369dcaa.txt
?? data/verification/sources/web/8d224578ae15d350.txt
?? data/verification/sources/web/92320d4cc191add4.txt
?? data/verification/sources/web/aab5e5692825f204.txt
?? data/verification/sources/web/b72cc012ea3476d4.txt
?? data/verification/sources/web/ba4704aa53949e8c.txt
?? data/verification/sources/web/d6418b07671b1447.txt
?? data/verification/sources/web/e9013f7855d8b8db.txt
?? data/verification/sources/web/f34b4a81558c5bf4.txt
---
0df03ec Verify page 98 (Bhugo/boz, Bhun/bon)
```


## [2026-09-05T14:59:33.890Z] TOOL CALL #81: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 - <<'PY'\nimport json\np='data/verification/page-102.json'\nd=json.load(open(p))\nfor c in d['entries'][1]['consulted']:\n    if 'Wanetsi' in c['note']:\n        c['note']=c['note'].replace(\"N.Pers. barahnah; Wanetsi būn. IE Pok. 769\", \"N.Pers. barahnah; [Waneci, OCR unclear] IE Pok. 769\")\njson.dump(d, open(p,'w'), ensure_ascii=False, indent=1)\nprint([c['note'][:200] for c in d['entries'][1]['consulted']][0])\nPY\npython3 tools/verify_check.py 102 | head -2; python3 -m json.tool data/verification/page-102.json >/dev/null && echo \"JSON OK\"; wc -c data/verification/page-102.json"
}
```


### [2026-09-05T14:59:36.736Z] TOOL RESULT

```
"būnaa- 'naked' ... From *bagna-, Oss. DI. bæγnæg ... Sogd. Bud. βγn'k, Chr. βγny, Chorasm. βγnyk, Av. maγna-, Zor.P. brahnak, N.Pers. barahnah; [Waneci, OCR unclear] IE Pok. 769 nogʷ-, O.Ind. magna-,
nodes verified: 13/13
node verdicts: {'plausible': 5, 'disputed': 3, 'confirmed': 4, 'transcription_suspect': 1}
JSON OK
59857 data/verification/page-102.json
```


## [2026-09-05T14:59:57.540Z] AGENT

Page 102 (book p. 72) verified — `data/verification/page-102.json` written, `verify_check.py 102` reports 13/13 nodes and **0 PROBLEM lines**.

Verdicts: nodes — 4 confirmed, 5 plausible, 3 disputed, 1 transcription_suspect; roots — 2 confirmed, 1 plausible. Ref checks: 6 supports, 4 partial, 1 contradicts, 1 not_found, 3 not_checked. 22 books consulted (POK, SYN, AHD/Watkins, IEC, WLD, CHEUNG, BRT, PHD, NYB, SOD, Bailey DKS, HRN, HUB, BQT, MON, ARY, KLN, SKT, LKT, LAT, FSD, WEB, TAD, AFM, FVQ, AFA).

Disputed / flagged:
- **Bu → Germanic "kusjan"** — AHD, the reference Nourai cites, puts *kussjan under a *separate* root: Watkins "kus-. A kiss … [Pok. ku-, kus- 626]"; Buck 16.29 keeps ku/kus and bu/bus apart. Wrong parent.
- **Bu → kusjan → English "buss"** — buss belongs to the *bu- group directly (Pokorny p.103 lists "engl. buss"; Etymonline: imitative, cf. Sp. buz, G. dial. Buss, Pers. busa). The Germanic kiss-verb yields *kiss*, not *buss*.
- **Busmâ → … → Arabic "bašâm"** — Klein p.144 and Etymonline make Arabic bašām a *cognate* ("rel. to") of Hebrew bāśām, not a loan from Greek; only بلسم/بلسان is the Greek word. Glosses also slipped (bašām = the balsam tree, not "perfume").
- **Latin "balsamun"** (transcription_suspect, `error_in: book`) — correct form is *balsamum* (Ernout-Meillet, Klein, Skeat, Webster). The printed page (pdf p.102) shows "balsamun", so the extraction is faithful; page PNG copied to `data/verification/sources/refs/ocr/BOOK/102.png`.

Other findings worth the owner's eye (not extraction errors):
- Persian **bŭs** is only *plausible*: Cheung 2007 p.15 derives bōsīdan/bōs- as an inchoative of *baud₂ "to sense" (Pth. pdbws-, ʾmbwy-, Arm. hamboyr) and calls the imitative root "probably unnecessary".
- Entry 1 is lifted whole from Bailey's *bagna- paragraph (Bailey, DKS s.v. būnaa-); Avestan maγna-, Pahl. brahnag and Sogd. βγn'k are **sister reflexes**, not descendants, and the chart's note "See Nogw for another possible root" is answered by Wiktionary/Bailey: *bagná < PII *nagnás < PIE *negʷ- — same word, not a rival etymology. ISS:256 independently corroborated via Gharib no. 2576 ("Prolexis. 256").
- Persian «بلسام» (node 3/#4) is unattested in the sense given: Dehkhoda's only بلسام = برسام "pleurisy"; the real Persian forms are بلسان/بلسم (Mo'in, Borhan). Nourai's own form, printed as such — a data issue only if the owner wants the gloss corrected.
- KLN:143 should be KLN:144 (balm/balsam/balsamine are on p.144; embalm on p.512/513).

**No extraction errors found** — the JSON matches the printed page throughout.
