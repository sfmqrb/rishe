# Verification process log — verify-page-367


## [2026-09-07T19:29:20.989Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 367 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-367.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-367.json. Write /home/sfmqrb/git/rishe/data/verification/page-367.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 367` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-07T19:29:23.086Z] AGENT

I'll start by reading the instructions.


## [2026-09-07T19:29:23.812Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-07T19:29:23.828Z] TOOL RESULT

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


## [2026-09-07T19:29:24.305Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-367.txt"
}
```


### [2026-09-07T19:29:24.322Z] TOOL RESULT

```
1	=== PDF page 367 (book page 337) ===
2	--- entry 0 ---
3	ROOT [Akkadian] Nitiru : natron; carbonate of soda  (refs AKD:61)
4	#1 (parent #0) [Hebrew] refs=AKD:61; KLN:1031 | nither, nether : natron
5	  #2 (parent #1) [Greek] refs=KLN:1049 | natron
6	    #3 (parent #2) [Arabic] refs=KLN:1031 | natrŭn
7	      #4 (parent #3) [Persian] refs=MON:4745 | natrûn «نطرون» : sodium
8	      #5 (parent #3) [Spanish] refs=KLN:1031 | natron
9	        #6 (parent #5) [English] refs=None | natron
10	    #7 (parent #2) [Latin] refs=KLN:1049 | nitrum : natron ; natrium : sodium
11	      #8 (parent #7) [French] refs=KLN | nitre : nitrate of potassium
12	        #9 (parent #8) [Persian] refs=MON:4880 | nîtrîc «نیتریک اسید» : nitric ; nîtrât «نیترات» : nitrate ; nîtrogen «نیتروژن» : nitrogen
13	        #10 (parent #8) [English] refs=AHD; KLN | nitre, nitrate, nitric, nitrogen, nitroglycerine
14	--- entry 1 ---
15	ROOT Nk -> redirect to Neku
16	--- entry 2 ---
17	ROOT [Indo-European] Nobh, Ombh, Mbh : nave, hub  (refs POK:314)
18	#1 (parent #0) [Avestan / Old Persian] refs=POK:314 | nâf, nâfah, nafa, nâfô : nave
19	  #2 (parent #1) [Persian] refs=KLN:1032; HRN:228; BQT:2100 | nâf «ناف» : nave ; nâfeh «نافه» : musk bag
20	#3 (parent #0) [Sanskrit] refs=SNS:258; POK:314 | nâbh, nâbhi : nave, family, race
21	#4 (parent #0) [Germanic] refs=AHD | nabo
22	  #5 (parent #4) [English] refs=None | nave, navel, auger
23	#6 (parent #0) [Latin] refs=AHD | umbilicus : navel
24	  #7 (parent #6) [English] refs=None | umbilicus
25	
```


## [2026-09-07T19:29:27.671Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-367.json",
 "description": "Read source JSON page 367"
}
```


### [2026-09-07T19:29:27.711Z] TOOL RESULT

```
{
  "pdf_page": 367,
  "book_page": 337,
  "entries": [
    {
      "root": {
        "name": "Nitiru",
        "lang": "Akkadian",
        "refs": "AKD:61",
        "gloss": "natron; carbonate of soda"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Hebrew",
          "refs": "AKD:61; KLN:1031",
          "words": [
            {"translit": "nither, nether", "gloss": "natron", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Greek",
          "refs": "KLN:1049",
          "words": [
            {"translit": "natron", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Arabic",
          "refs": "KLN:1031",
          "words": [
            {"translit": "natrŭn", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Persian",
          "refs": "MON:4745",
          "words": [
            {"translit": "natrûn", "gloss": "sodium", "script": "نطرون"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 3,
          "lang": "Spanish",
          "refs": "KLN:1031",
          "words": [
            {"translit": "natron", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "natron", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 2,
          "lang": "Latin",
          "refs": "KLN:1049",
          "words": [
            {"translit": "nitrum", "gloss": "natron", "script": null},
            {"translit": "natrium", "gloss": "sodium", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "French",
          "refs": "KLN",
          "words": [
            {"translit": "nitre", "gloss": "nitrate of potassium", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "Persian",
          "refs": "MON:4880",
          "words": [
            {"translit": "nîtrîc", "gloss": "nitric", "script": "نیتریک اسید"},
            {"translit": "nîtrât", "gloss": "nitrate", "script": "نیترات"},
            {"translit": "nîtrogen", "gloss": "nitrogen", "script": "نیتروژن"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 8,
          "lang": "English",
          "refs": "AHD; KLN",
          "words": [
            {"translit": "nitre, nitrate, nitric, nitrogen, nitroglycerine", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {"name": "Nk", "redirect": "Neku"},
      "nodes": []
    },
    {
      "root": {
        "name": "Nobh, Ombh, Mbh",
        "lang": "Indo-European",
        "refs": "POK:314",
        "gloss": "nave, hub"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "POK:314",
          "words": [
            {"translit": "nâf, nâfah, nafa, nâfô", "gloss": "nave", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "KLN:1032; HRN:228; BQT:2100",
          "words": [
            {"translit": "nâf", "gloss": "nave", "script": "ناف"},
            {"translit": "nâfeh", "gloss": "musk bag", "script": "نافه"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "SNS:258; POK:314",
          "words": [
            {"translit": "nâbh, nâbhi", "gloss": "nave, family, race", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "nabo", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "nave, navel, auger", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "umbilicus", "gloss": "navel", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "umbilicus", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
```


## [2026-09-07T19:29:28.292Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-07T19:29:28.331Z] TOOL RESULT

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


## [2026-09-07T19:29:36.258Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nfor k in ['AKD','KLN','MON','POK','HRN','BQT','SNS','AHD','WLD','IEC','SYN','BRT','KNT','PHD','NYB','LKT','SKT','FSD','WEB','LEW','LAT','ARY','HUB','RCH','FVQ','AFM','PLA','TAD','ARB','DEV','PHN']:\n    v=d.get(k)\n    print('==',k, json.dumps(v,ensure_ascii=False)[:700] if v else 'MISSING')\n\""
}
```


### [2026-09-07T19:29:37.607Z] TOOL RESULT

```
== AKD {"title": "H. Zimmern, Akkadische Fremdwörter als Beweis für babylonischen Kultureinfluss, Leipzig 1917 (2nd ed.)", "edition_found": "1915 first edition (1917 is the 2nd, enlarged ed.; pagination may differ slightly)", "kind": "archive_djvu", "url": "https://archive.org/details/akkadischefremdw00zimmuoft", "identifier": "akkadischefremdw00zimmuoft", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AKD.txt", "page_offset": "leaf = printed + 8 (e.g. leaf 21 = p.13). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Organised by semantic field; Akkadia
== KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO pri
== MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol 
== POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index 
== HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the 
== BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.c
== SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt"], "page_offset": "242 leaves; page offset not determined (OCR too poor to read printed numbers) — 
== AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifie
== WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.39015066210397 (browser only from this host)", "identifier": "in.gov.ignca.20339 (Band 3); also in.ernet.dli.2015
== IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Reconstruct
== SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<i
== BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between 
== KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archiv
== PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<ident
== NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Nourai's 'NYB' nu
== LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 'NNNN. word (language) meaning' - Lokotsch is usually cited by entry number, but Nourai cites pages.
== SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<i
== FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt", "page_offset": "vol1: leaf = p + 41..56 (drifts; e.g. leaf 87 = p.46, leaf 612 = p.556); vol3: le
== WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/WEB_vol1.txt", "page_offset": "not reliably detected (page_numbers.json sparse); grep headword. local
== LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt", "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.o
== LAT {"title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951", "edition_found": "1951 (3rd ed.) - matches Nourai", "kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "identifier": "ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine (4th ed. 1959 lending-only: dictionnairetymo0000unse; another open copy: DictionnaireEtymologiqueDeLaLangueLatine)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt", "page_offset": "leaf = printed + 18 for most of the book (e.g. leaf 21 = p.3); drifts in places (leaf 219 = p.301 -> -82?? probably a mis-detec
== ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image", "local_file": ["/home/sfmqrb/git/rishe/
== HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by parag
== RCH {"title": "J. Richardson, A Dictionary, Persian, Arabic and English, new ed. by F. Johnson, London 1829 (Lahore reprint 1984)", "edition_found": "1829 Johnson edition (DLI scan, 1814 leaves)", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.24303", "identifier": "in.ernet.dli.2015.24303 (other editions: 1806-10 a-dictionary-persian-arabic-and-english-vol.-i, india.history.resource.17812; 1852 Johnson dictionarypersia00johnuoft)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/RCH.txt", "page_offset": "leaf ~= printed + 93..94 (e.g. leaf 336 = p.242, leaf 587 = p.494); weakly detected, verify by grepping the page number. local file has \\f b
== FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ.txt"], "page_offset": "printed page = leaf − 17 (0-based \\f blocks in FVQ_pages.txt; 
== AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM.txt"], "page_offset": "19
== PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 leaves (pdftotext -layout, \\f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276).", "loo
== TAD {"title": "Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-hurufihi (2nd ed. Cairo 1932, ed. Yusuf Tuma al-Bustani; later Library of Lebanon reprint) — Nourai lists it under Arabic authors ('Unaysi T.'); its Table IV line was lost in the OCR", "kind": "archive_djvu", "url": "https://archive.org/details/TOB1932ARAR (1932 ed.); also https://archive.org/details/ar113lang79 and https://archive.org/details/elshandawily14640", "lookup_hint": "Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; inside.php search works.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD_pag
== ARB {"title": "al-Jawaliqi, al-Mu'arrab min al-kalam al-a'jami, Tehran 1966 (reprint of Ahmad M. Shakir's Cairo 1361/1942 edition)", "kind": "archive_djvu", "url": "https://archive.org/details/mo3rb (probably the Shakir edition) ; https://archive.org/details/almo3rab_gwaliqy_f_abduraheem (F. 'Abd al-Rahim ed., Damascus 1990) ; also uc1.aa0003615705 / AAlexandrina-148752 (Sachau's Leipzig 1867 ed.) ; text on shamela.ws", "lookup_hint": "Alphabetical Arabic headwords; grep in ARB_mo3rb.txt / ARB_abdulraheem.txt (raw, no page breaks); edition of mo3rb not confirmed — check its title page image.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/ARB_mo3rb.txt", "/home/sfmqrb/git
== DEV {"title": "L. M. Devic, Dictionnaire étymologique des mots français d'origine orientale, Paris 1876", "edition_found": "1876", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairety00devi", "identifier": "dictionnairety00devi (also dictionnairetym02devigoog, fr105comparative41)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/DEV.txt", "page_offset": "leaf = printed + 26 (pp. <80) to +30 (pp. >84), e.g. leaf 29 = p.3, leaf 118 = p.88. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "French headword in caps at line start.", "no
== PHN {"title": "A. P. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du turc, Paris 1866", "edition_found": "1866", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairetym01pihagoog", "identifier": "dictionnairetym01pihagoog (others: bub_gb_QnsSAAAAIAAJ, dictionnairetym00pihagoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHN.txt", "page_offset": "leaf = printed + 31 (e.g. leaf 33 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "French headword in caps at line start;
```


## [2026-09-07T19:29:42.825Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i 'nitiru\\|nitru\\|Natron\\|nitrum' AKD.txt | head -40"
}
```


### [2026-09-07T19:29:42.890Z] TOOL RESULT

```
985:nitiru  wohl   Natron,   nur  vereinzelt   zu   belogen,   wohl,   wie   liebr.  näter, arani.  nitro,  netrö,  griech.  vItqov,  Utqov  usw.,  Natron,  <C  ägypt.  ntrj.] akk.  si];l;ii  und  sHihttu  eine  Art  Alaun  :  >>  s^^r.  SekM}  [akk.  tß-
```


## [2026-09-07T19:29:43.763Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i '^natron\\|natron,\\|natrun\\|nitre\\b\\|nitrum\\|nitron' KLN_1966.txt | head -40"
}
```


### [2026-09-07T19:29:44.225Z] TOOL RESULT

```
4395:Banksia,  n.,  a  genus  of  Australian  evergreen trees.  —  Named  after  the  famous  English  na¬ turalist  and  traveler,  Sir  Joseph  Banks  (1743- 1820).  For  the  ending  see  suff.  -ia. banner,  n.  —  ME.  banere,  fr.  OF.  baniere  (F.  ban- nitre),  which  is  prob.  a  blend  of  WTeut.  *banda, corresponding  to  Goth,  bandwa,  bandwo,  ‘sign, signal’  (whence  also  It.,  OProveng,  banda,  ‘band, troop’.  Late  L.  bandum,  ‘banner’,  banderia,  ba- neria,  ‘place  where  the  banner  is  set  up’,  OPro¬ veng.  bandiera  (whence  It.  bandiera,  F.  han¬ dier)’.  Sp.  bandera),  ‘banner’,  and  of  OF.  ban, ‘public  proclamation’.  Goth,  bandwa,  prob.  de¬ rives  fr.  I.-E.  base  *bendh-,  ‘to  bind  .  See  band, ‘tie’,  and  cp.  band,  ‘troop’,  banderilla,  banderole, banish,  pandour.  For  the  etymol.  of  OF .  ban  see ban,  ‘edict’.  MHG.  banier(e)  (whence  G.  Banner and  Panier ),  ‘banner’,  is  an  OF.  loan  word.
25028:Natrix,  n.,  a  genus  of  snakes,  the  grass  snake (zool.)  —  L.  natrix,  ‘water  snake’.  See  adder, natrolite,  n.,  a  hydrous  silicate  of  sodium  and aluminum  (mineral.)  —  See  natron  and  -lite. natron,  n.,  native  sodium  carbonate  (chem.  and mineral)  —  Fr.  Sp.  natron,  fr.  Arab,  natrun,  fr. Gk.  vtTpov.  See  niter.
25473:Derivatives:  nit-t-er ,  n.,  nit-t-y,  adj. niter,  nitre,  n.,  nitrate  of  potassium  (chem.)  —  F. nitre,  fr.  L.  nitrum,  fr.  Gk.  vixpov,  ‘native  sodi¬ um  carbonate,  natron’,  fr.  Heb.  nether,  ‘carbon¬ ate  of  soda,  natron’  (stem  nithr-;  cp.  Aram. nithra).  Cp.  nitrogen,  natron, nithing,  n.,  a  cowardly  person  (archaic).  —  ME., fr.  OE.  niding,  ‘infamous  man’,  fr.  ON.  nidingr, fr.  nid,  ‘envy,  hatred’  (whence  also  Dan.  nid, ‘envy,  grudge,  jealousy’),  which  is  rel.  to  OE. nid,  ‘quarrel,  enmity,  hatred,  battle’,  OS.,  OFris. nith,  ‘hatred,  envy’,  Du.  nijd,  ‘envy’,  OHG.  nid, nidh,  nith,  ‘anger,  envy,  hatred’,  MHG.  nit,  nid, G.  Neid,  ‘envy,  grudge,  jealousy’,  Goth,  neifi, ‘ill-will,  envy,  jealousy’,  and  cogn.  with  OIr. nith,  ‘combat,  fight'.  Cp.  niddering. nitid,  adj.,  bright.  —  L.  nitidus,  ‘shining,  glitter¬ ing,  bright’,  fr.  nit  ere,  ‘to  shine’.  See  neat,  adj. niton,  n.,  a  chemical  element  —  A  Modi,  hybrid formed  on  analogy  of  argon  fr.  L.  nitere,  ‘to shine’  (see  neat,  adj.);  so  called  by  the  English chemist  Sir  William  Ramsay  (1 852- 1 9 1 6)  in  19 1 2, because  it  glows  in  the  dark, nitr-,  a  form  of  nitro-,  before  a  vowel, nitrate,  n.  (chem.),  1)  a  salt  of  nitric  acid;  2)  po¬ tassium  nitrate  or  sodium  nitrate.  —  Formed fr.  niter  with  chem.  suff.  -ate.
25475:nitric,  adj.,  1)  pertaining  to  niter;  2)  pertaining to  nitrogen;  3)  containing  nitrogen.  —  F.  nitri- que,  fr.  nitre.  See  niter  and  adj  suff.  -ic. nitride,  also  nitrid,  n.,  a  compound  of  nitrogen with  a  more  electropositive  element  (chem)  — Formed  fr.  niter  with  suff.  -id(e). nitrification,  n.,  the  act  of  nitrifying.  —  F.,  coined by  the  French  chemist  Guyton  de  Morveau (1737-1816)  in  1787.  See  niter  and  -fication. nitrify,  tr.  v.  1)  to  convert  into  niter;  2)  to  oxidize (ammonium  salts,  etc.)  into  nitrites  and  ni¬ trates  ;  3)  to  impregnate  with  nitrates  (chem.  and bacieriol)  —  F.  nitrifier  (see  niter  and  -fy);  first used  by  Thouvenel  in  1797. nitrite,  n.,  a  salt  of  nitrous  acid  (chem.)  — Formed  fr.  niter  with  suff.  -ite. nitro-,  before  a  vowel  nitr-,  combining  form  used in  the  senses:  1)  containing  nitrogen;  2)  con¬ taining  nitric  or  nitrous  acid.  —  Gk.  vixpo-  (cp. e.g.  vixpo-xouji;,  ‘producing  niter’),  fr.  vlxpov, ‘sodium,  carbonate’.  See  niter, nitro,  adj.,  containing  nitrogen.  —  From  nitro-.
25480:nitrous,  adj.,  1)  pertaining  to,  or  containing,  niter ; 2)  designating  a  compound,  in  which  the  ni¬ trogen  has  a  lower  valence  than  in  the  corre¬ sponding  nitric  compound  {chem.)  —  L.  nitrosus, ‘full  of  natron’,  fr,  nitrum,  ‘natron’.  See  niter and  -ous.
40277:-tron,  suff.  used  in  electricity  and  chemistry.  — Coined  from  the  ending  -tron  in  electron.  Cp. dynatron,  kenotron,  magnetron,  etc. trona,  n.,  sodium  carbonate  (mineral.)  Swed., fr.  Arab,  tron,  aphetic  for  natrun,  whence  na¬ tron  (q.v.)
```


## [2026-09-07T19:29:57.022Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==69' AKD.txt | head -60; echo \"=== check printed page marker\"; awk 'BEGIN{RS=\"\\f\"} /nitiru/{print NR}' AKD.txt"
}
```


## [2026-09-07T19:29:57.960Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i 'natrium\\|sodium,  n\\.' KLN_1966.txt | head -10"
}
```


### [2026-09-07T19:29:58.248Z] TOOL RESULT

```
murrd, arab    murr  O  griech.  fiv^^a  usw.,  3iyrrlie)).\  [akk.  lardii  :  hebr.
ncrd,  aram.  nardd,  griech.  vöqSos  usw.,  Narde,  wohl  <]  ind.  ndlddd.] [akk.  ladunu  jedenfalls  Premdw.  :  griech.  XtjSov,  h'jSavoy,  Ladanum;  dazu viell.  hebr.  löf.  dem  vieU.  auch  im  Aklc.  luffti  entspricht.]  akk.  a))iru
eine    Spezerei,    vieU.    zu    :    äfiß^a   O    arab.    'anbar)    Ambra   (Liquid- ambar).  [akk.  budulhii  :  hebr.  hddölnli,  griech   ßSfKliov,  Bdellium.]
15.  Mineralien.
akk.   huräm   Gold    (wolil    von    St.  l/rs  gelb   sein)  :  >  hebr.  Mriis,
      59  
auch  pliön.  und  Klmw-Inschr.  /?r.s.  Aus  dem  Semit.  ^  griech.  x9*"^ög. [Zu  sum.  gitsqi  Gold,  gehört  viell.  armen.  osM  Gold,  finn.  vaski  Kupfer,  Erz.]
akk.  Icaspii,  st.  c.  Msap  Silber,  Geld  :  >  wohl  hebr.  Msep,  lasp-, aram.  laspd,  lespä.     S.  auch  schon  oben  S.  17  f.  akk.  sarpii  Silber
(eig.  das  geläuterte,  von  sumqm  läutern,  schmelzen) :  >  südarab.  .>■;•/'  Silber, wie  wohl  überhaupt  der  St.  ^rp  i.  d.  Bed.  (Metalle)  läutern,  schmelzen, löten  im  Hebr.  und  Aram.  O  im  Arab.),  s.  schon  oben  S.  27.  Desgleichen wohl  auch  syr.  sarrfipd,  arab.  mirfif  Geldwechsler,  jüd.-aram.  sarrep  Geld wechseln,  wie  viell.  auch  (mit  sekundärem  Lautübergang)  syr.  'arrcp  Geld wechseln  (nebst  Ableitungen).  ayr.  sinn  eine  Art  Silber  geht  zurück
auf  den  bab.  Mondgott  Sin,  dem  das  Silber  als  Metall  eignet.
akk.  eril,  älter  auch  warn,  urspr.  wohl  Kupfer,  dann  Bronze  (wohl ■<^  sum.  urtid);  damit  viell.  zus.  hängend  idg.  Wörter  wie  mittelpers.  röd, altind.  lohd-,  lat.  raiidus  Kupfer.  akk.  siparrii  Kupfer  :  >  viell.
hebr.  sej^er  an  einigen  Stelleu  (Jes.  30,  8;  Hi.  19,  23;  Ex.  17,  14);  ferner arab.  sifr,  sufr.
akk.  anaJiu  Zinn  (wohl  <^  sum.  *anag,  belegt  anna,  amma,  nagga, niggi)  :  hebr.  'annk,  syr.  'anJchä  O  wohl  arab.  'finuk),  äth.  na'sk.  Dazu jedenfalls  armen,  anag,  skr.  näga.     Unsicher,  wo  ursprünglich  heimisch.
akk.  jmrzillu  Eisen  :  daraus  zunächst  wohl  ]>  hebr.  barsei,  in  N. pr. harsill-,  aram.  parsel,  })arz9lä  O  arab.  firzil  Eisenfessel),  südarab.  frzn. Unsicher,  wo  ursprünglich  heimisch,  viell.,  worauf  auch  die  Endung  -ill weisen  könnte,  im  nordösü.  Kleinasien.  akk.  suhhi  Rost  :  ]>  wohl  syr.
suhtä,  mand.  sfitä.
akk.  abcirti  angeblich  Magnesit i,  aber  wohl  doch  besser  Blei  :  ]>- wohl  aram.  'äbärä,  'ahbärä  Blei  O  arab.  'abär).  Hebr.  'öpäret  Blei,  das sicher  auch  dazu  gehört,  steht  formell  etwas  abseits,  desgl.  armen,  kapar Blei.     Unsicher,  wo  das  Wort  ursprünglich  heimisch.
akk.  esniarfi  wahrsch.  Bez.  eines  Edelmetalls  :  dazu  vieU.  hebr. Ijasmal  bei  Ez.,  sowie  ägypt.  hsrnn,  beides  vieU.  Silbergold,  Elektrum.
akk.   siibil   ein   Edelste
=== check printed page marker
71
```


### [2026-09-07T19:29:58.300Z] TOOL RESULT

```
3513:See  prec.  word  and  -ion. arrojadite,  n.,  a  phosphate  of  natrium,  ferrum, sodium,  etc.  —  Named  after  the  Brazilian  geo¬ logist  Dr.  Miguel  Arrojado  of  Lisbon.  For  the ending  see  subst.  suff.  -ite. arrondissement,  n.,  an  administrative  district  of
25027:natrium,  n.,  sodium  (chem.)  —  ModL.  See  natron and  chem.  suff.  -ium.
35799:sodio-,  combining  form  meaning  ‘sodic  and’.  — ModL.,  sodio-,  fr.  sodium.  See  next  word, sodium,  n.,  name  of  a  metallic  alkaline  element (chem.)  —  ModL.,  coined  by  the  English  chem¬ ist  Sir  Humphrey  Davy  (1778-1829)  fr.  soda; he  so  called  it  because  he  first  obtained  it  from caustic  soda.  For  the  ending  see  chem.  suff. -ium.
```


## [2026-09-07T19:30:05.229Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==71' AKD.txt"
}
```


### [2026-09-07T19:30:06.380Z] TOOL RESULT

```
ffälligem  q,  arab.  qaträn,  qitran).  akk.  wahrsch.  Jcuprrtu^  Schwefel,
dann  :  >  hebr.  goprtt,  aram.  guprlta,  kuhritä,  Jcebritä  O  arab.  kibrit).
akk.  uhtdu  eine  Alkalienart  :  ;>  syr.  'aJjla,  'vhlä  Lauge.  [akk.
1)  K.  996,  Rev.  10  ff.  (Harper  VI  570).  Es  ist  hier  anscheinend  vom  Erhitzen  des 6u?'a?ZM-Steines  die  Rede.  Daraus  darf  man  vielleicht  schließen,  daß  die  Babylonier  die eigenartige  Krystallhildung  des  Berylls  gekannt  und  verwertet  haben.
2)  Wörtl.  wohl  Schmiere,  von  kapärti  bestreichen,  beschmieren;  vgl.  dazu  unten  S.66.
3)  Jedenfalls  zu  trennen  von  jüd.-aram.  qerd  Wachs  <;^  griech.  xTj^öq.
4)  Die  Stelle  2  Maik.  1,  36  ist  natürlich  für  die  Etymologie  des  "Wortes  väip»a vollständig  belanglos.  5)  Wohl  ganz  zu  trennen  von  PI.  'etrSne  Räuoherwerk.
6)  Bab.  Exp.  Univ.  Penns.  XIV  Nr.  148,  52.  kupritu  könnte  einfach  WeiterbUdimg von  kupru  Erdpeoh,  sein.
      61      
nitiru  wohl   Natron,   nur  vereinzelt   zu   belogen,   wohl,   wie   liebr.  näter, arani.  nitro,  netrö,  griech.  vItqov,  Utqov  usw.,  Natron,  <C  ägypt.  ntrj.] akk.  si];l;ii  und  sHihttu  eine  Art  Alaun  :  >>  s^^r.  SekM}  [akk.  tß-
hat  Amanhn  wahrsch.  Amon-Salz  d.  i.  als  ä(x[^oiviax6v^  Sal  amnioniacum, urspr.  Steinsalz  aus  der  Libyschen  "Wüste,  also  wohl  in  Anleluiung  an  eine ägypt.  Bez.  entstanden.]
akk.  guhlu  Spießglanz,  Antimon,  Stibium  (als  Augenschminke)  : aram.  laMft  (^  spätliebr.  Mhal  die  Augen  schminken,  sowie  arab.  liuhl O  Alkohol),  äth.  hiehel).     Urspr.  Heimat  des  "Wortes  unsicher.  akk.
sadidu  wohl  aucli  Antimon ^  (als  Augenschminke)  :  >  aram.  sodnli'i. akk.  amämfi,  gleichfalls   ein  Schmink  mittel,  aber  viell.  pflanzlicher  Her- kunft.^    Davon  die  Bez.  der  Göttin  Istar  als  Amamitu  :  >  mand.  'Anin- mzt  als  Bez.  des  Planeten  Venus.
akk.  serser{r)i(,  rote  Paste  :  >  hebr.  säscr.  akk.  stjm  Paste  :
>  wohl  syr.  .iijjü  Paste,  sowie  sajäpä  Augensalbe  O  arab.  sijöf,  sowie armen,  vereinzelt  sup'ai),  wie  auch  das  i.  d.  Bed.  bestreichen,  einsalben,  wohl erst  denom.  Verbum  säp.
16.  Himuielsknnde,  Kalender,  Zählung.
Die  sum.-akk.  Namen  der  5  den  Alten  bekannten  Planeten,  bezeichnet nach  den  mit  den  entsprechenden  Sternen  verknüpften  babyl.  Göttern 1)  Nahikt  2)  Istar  {Dilhat,  Biitt,  Istar -halckabe ,  Nana,  Amänütu^), 3)  Nergal,  4)  Marduh  {Bei),  5)  Kaimonu,  sind  hauptsächlich  nur  im  aram. Sprachlcreise,  namentlich  von  den  Harraniern  und  Mandäern,  teilweise direkt  übernommen  worden,  als  1)  Nahö  u.  ä.,  2)  'Estarcl  u.  ä.  {Dilhat  u.a., Beltt,  Kaukabtd,  Nanai,  'AmnmJt),  3)  Nerrg,  4)  Bei  (Kaukahil),  5)  Kewän  ^. Dagegen  sind  sie  zu  den  Griechen  und  Eömeru  in  der  Form  von  Über- tr
```


## [2026-09-07T19:30:18.769Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json;d=json.load(open('refs_online.json'));print(d['KLN']['page_offset']);print(d['KLN'].get('lookup_hint'))\""
}
```


## [2026-09-07T19:30:19.966Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n 'nobh\\|ombh-\\|^enebh\\|embh' POK_01.txt | head -30; echo ---; grep -n 'nobh\\|ombh' POK_full.txt | head -20"
}
```


### [2026-09-07T19:30:20.062Z] TOOL RESULT

```
KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
```


### [2026-09-07T19:30:20.124Z] TOOL RESULT

```
3404:dhebh-,  dbebh-eu-  ^beschädigen;  verkürzen,  betrügen',  die  nasalierten  Fori (*dhembh-)  sind  als  proportionale  Neubildungen  nach  -^i-haltigen  Wurzel zu  verstehen.
4569:embhi-,  empi-  .Stechmücke.  Biene'?    Mit  tabuierendem  Wechsel  hhip?
4636:I.  {enehh-),  emhh-,  ombh-,  nobh-  (nebh-?),  rpbh-  ,NabeP,  mehrfach  mit i-Formantien. Ai.  ndbhya-  n.  ,Nabe^,  nähhi-  f.  , Nabel,  Nabe,  Verwandtschaft^,  näbhlla- n.  (unhelegt)  ,Schamgegend,  Nabelvertiefung';  av.  nahä-nazdista-  ,der  ver-  ' wandtschaftlich  nächststehende',  daneben  mit  ar.  ph:  av.  näfö,  npers.  näf ,Nabel';
4643:Vielleicht  hierher  ags.  umbor  ,kleines  Kind',  auch  der  ital.  VN  Umbri (*mbh-),  anderer  Ablaut  im  germ.  VN  Ämbrones  {*ombh-)  anders  Kretschmer Gl.  21,  116  f.
4645:2.  (enebh-):  nebh-,  emhh',mhh-  (Kontaminationsform  nembh-);  z.T.  emb-, omb-  aus  embh-,  ombh-  , feucht,  Wasser',  daraus  ,Dampf,  Dunst, Nebel,  Wolke'.
4676:nembh-:  ^^
---
```


## [2026-09-07T19:30:25.181Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} /ombh-, nobh-/{print \"LEAF \"NR; print}' POK_01.txt | head -60"
}
```


### [2026-09-07T19:30:26.348Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-07T19:30:29.964Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('POK_01.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i,l in enumerate(leaves):\n    if 'ombh-' in l and 'nobh-' in l:\n        print('LEAF(0-based)',i)\n        print(l[:4000])\n        break\nEOF"
}
```


### [2026-09-07T19:30:31.501Z] TOOL RESULT

```
LEAF(0-based) 327
'ijg  ,  jährig*,  TtgrjT-rjy , einjähriges  Lamm*  (zu  dor.  nqäxog  aus  *p.r^os?);  h-LavTÖg  ,Jahr'  (zu laveiv:  ,wenn   das  Jahr  ruht,  Jahreswende*??).  ^»y-
Tiefstufe  -n-  in:  .1-,
got.  fram  fair-n-in  jera,  SiS^  fer-n-un  gere,  mhd.  verne  ,im  vorigen  Jahre'j
lit.  jper-n-ai  ,im  vorigen  Jahre*,  lett.  p§rns  , vorjährig* ;  '""5^
russ.  dial.,  cech.  lo-ni  (^ol-ni)  , letztjährig*.
Specht  Dekl.  16  stellt  dazu  das  Pron.  en  in  gr.  evrj  , jener  (Tag  oder jenes  Jahr*?).
Schwyzer  Gr.  Gr.  I  424  mit  Anm.  5,  Feist  140  f.,  Specht  Dekl.  15  f.
en  ,siehe  da!^  '
Gr.  ^V,  ijrjVj  lat.  en  ,siehe  da!^ WP.  I  127,  WH.  I  403  f.
I.  {enehh-),  emhh-,  ombh-,  nobh-  (nebh-?),  rpbh-  ,NabeP,  mehrfach  mit i-Formantien. Ai.  ndbhya-  n.  ,Nabe^,  nähhi-  f.  , Nabel,  Nabe,  Verwandtschaft^,  näbhlla- n.  (unhelegt)  ,Schamgegend,  Nabelvertiefung';  av.  nahä-nazdista-  ,der  ver-  ' wandtschaftlich  nächststehende',  daneben  mit  ar.  ph:  av.  näfö,  npers.  näf ,Nabel';
315
oT.  dficpalög  (Nom.  PL  auch  o^LcpaUg)  ,Nabel,  Schildbuckel',  wohl  auch }j^i(pa'Asg  ;die  unreifen  Weinbeeren  oder  Oliven  oder  andere  Früchte'  (als nabelartig  vorgestülpte  Knöpfchen),  d^cpa-ug  ,der  Kelch  der  Eichel;
lat.  umbillcus  ,Nabel',  umhö,  -önis  , Schildbuckel';
air.  imhliu  ,Nabel'  {*emUlön-),  mir.  imlecan  ds.  (ein  Versuch  zur  Suffix- erklärung bei  Pedersen  KG.  I  495);
ahd.  nahüj  ags.  nafu^  aisl.  nof  ,Radnabe'  (auch  in  ahd.  naba-ger,  ags. nafu-gär,  aisl.  nafarr  ,grober  Bohrer'),  ahd.  nahalo,  ags.  nafela,  aisl.  naß ^Nabel';  dazu  nach  Liden  KZ.  61,  17  ahd.  amban,  amhon,  m.  (o-St.) ^Wanst',  as.  dmhön  ,abdomina',  Nom.  Akk.  PI.  eines  m.  ow-St.  (germ. ^amhan-,  idg.   *omhhon-)]
apr.  nahis  ,Nabe,  Nabel',  lett.  naba  ,Nabel'.
Vielleicht  hierher  ags.  umbor  ,kleines  Kind',  auch  der  ital.  VN  Umbri (*mbh-),  anderer  Ablaut  im  germ.  VN  Ämbrones  {*ombh-)  anders  Kretschmer Gl.  21,  116  f.
WP.  I  130,  EM  1122,   Specht  Dekl.  100.
2.  (enebh-):  nebh-,  emhh',mhh-  (Kontaminationsform  nembh-);  z.T.  emb-, omb-  aus  embh-,  ombh-  , feucht,  Wasser',  daraus  ,Dampf,  Dunst, Nebel,  Wolke'.
nebhos- :  ai.  ndbhas-  n.  ,Nebel,  Dunst,  Gewölk,  Luftraum,  Himmel', daneben  Wurzelflexion  im  dehnstuf.  f.  Plur.  ndbha/i(?)]  av.  nabah-  n.  PI. ,Lu
```


## [2026-09-07T19:30:49.565Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT\"; grep -n 'nāfah\\|näfah\\|nafah-\\|nāfō\\|nabā-nazdišta\\|naba-nazdista' BRT.txt | head -20; echo \"=== KNT\"; grep -n -i 'nāfa\\|nafa-\\|navel' KNT.txt | head -20; echo \"=== PHD\"; grep -n -i '^nāf\\|nāf \\|nāfag\\|navel' PHD.txt PHD_mackenzie.txt | head -20; echo \"=== NYB\"; grep -n -i 'nāf\\|navel' NYB_vol2_glossary.txt | head -20"
}
```


### [2026-09-07T19:30:49.650Z] TOOL RESULT

```
=== BRT
11513:Vgl.  ^\.  jagkatevan,  ja^knrvan  -.jaghnäfah.  — ')  Ob  V  nach  S  368.  17  für  iv  (s.  das  i\. jaghnrvaa)'t  Oder  wnrde  «  sonantisch  ge- sproclien?  Ein  Ausgleich  zwischen  'jayarn'' und  *jafnu}'  konnte  wohl  (sekundär)  lu  einer solchen  Form  (mit  son.  n)  ßhren.
18871:•  j.  nafah-  n.  'Verwandtschaft,  Familie': gayehe  (sd)  mar^hru}  . .  yaAmat  Aata  frä- ^wpTPsat  (näml.  aAurö  matda)  °/3'^  airya- nam  dahyunatn  Yt. /J.  87.
=== KNT
=== PHD
PHD.txt:494:nab [np | N nawa] grandson. nabānazdišt [nb”nzdšt! = Av. nabünazdista-] next of kin. паї [w | M mp] family. ~ag [-R! | N náf(a)] navel. !naft [npt! | = M, N ~] moist, damp; naphtha. *naft [npt'] descendant. nahang [жле] province. *nakkira [nkyl’y] denying, repudiating. ~yih: repudiation. nāl- [wl- | P (n’r-), N ~] groan, complain. nam [nm | N ~] moisture. nám [SM < A £m; m | = M, N ~] name, fame. namad [nmt' | N <) felt. námag [MGLTA < A melt: ттк! | M пто, N пата] book, letter. namak [nmk! | M nmyhk, N ~] salt. namāz [OSGDE < A sgdh; nm’c | = M, N ~] reverence, prostration, prayer. ~ burdan: pay homage. nām-burdār [л?т bwlt?l | N ~] heir, preserving the father's name. nāmčišt [?жт-, ŠMcst'], (pad) ~: in particular, especially. ~ig [-yk'] famous, well known.
PHD.txt:2893:navel nàfag.
PHD.txt:5256:nāfag, wazag wabar wābarīgānīh
PHD_mackenzie.txt:3642: . . . .ag [-k l I N naf(a)] navel.
PHD_mackenzie.txt:7133:mortar hawan; (lime) carGg.                    navel nMag.
=== NYB
1535:franāmišnēh [*pln?minyh] det. v. n. con- fession, creed: ētēn-aš ~ this is his con- fession of Faith 6215-16 (the v. n. is deter- mined by ētēn, hence the form in -čh). — Phl franāftan franäm- renders Av. (1362)
```


## [2026-09-07T19:30:50.358Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD\"; grep -n -i 'nobh\\|^nave\\|navel\\|auger' AHD_watkins1985.txt | head -20; echo \"=== HRN\"; grep -n 'nāf\\|näf' HRN.txt | head -20"
}
```


### [2026-09-07T19:30:50.425Z] TOOL RESULT

```
=== AHD
173:It was probably not long before the disper- sal of the Proto-Indo-European community that the use of the wheel and wheeled trans- port was adopted. Despite the existence of widespread word families, most terms relat- ing to wheeled vehicles seem to be metaphors formed from already existing words; they are not primitives or primary vocables. So the word for AXLE (aks-) may mean simply “a pivotlike juncture”; the NAVE or hub of the wheel (nobh-) is the same word as NAVEL. This is clearly the case with WHEEL itself, where the widespread *k(e)-k“l-o- is an ex- pressive derivative of a verb (k"el-') meaning “to revolve or go around.” Other words for “wheel” are dialectal and again derivative, like Latin rota from a verbal root ret-, “to run.” A root wegh-, “to go, transport in a vehicle” (WAGON), is attested quite early, though not in Hittite. This evidence for the late appearance of the wheel agrees with archaeological findings that date the distri- bution of the wheel in Europe to the latter
507:ghaiso-. A stick, spear. 1. Germanic *gaizaz in: a. Old English gar, spear: GORE}; (GARFISH), GARLIC; b. com- pound *nabé-gaizaz, tool for piercing wheel hubs (*nabd, hub; see nobh-); c. Old Norse geirr, spear (in geirfalki, gyrfalcon, akin to the source of Old French girfaut): GYRFALCON. 2. Germanic *gaizé in Old English gdra, corner, point of land: GORE?. [Pok. ghaiso- 410.]
787:animal: NEAT2; b. compound form *ga-nauta- (*ga-, with, together; see kom), “he with whom one shares possessions,” companion, fellow, in (i) Middle Dutch ghenét, noot, fellow: MATELOTE (ii) Old High German ginéz, companion, in German Eidgenosse, confederate: HuGuEnot. [Pok. neu-d- 768.] newn. Nine. 1. Germanic *niwun, with variant *nigun, in Old English nigon, nine: NINE, NINETEEN, NINETY, NINTH. 2. Latin novem, nine (< *noven, with m for n by analogy with the m of septem, seven, and decem, ten): NOVEMBER, NOVENA; NONAGENARIAN. 3. Ordinal form *neweno- in Latin nénus, ninth: NONA-, NONES, NOON; (NONAGON), (NONANOIC ACID). 4. Prothetic forms *enewn, *enwn in Greek ennea, nine (> *ennewa, *enwa-): ENNEAD. [Pok. e-neuen 318.] newo-. New. Related to nu-. 1. Suffixed form *new-yo- in Germanic *neuja- in: a. Old English néowe, niwe, new: NEw; b. Old Norse njyr, new: SPAN-NEW. 2. Basic form *newo- in Greek newos, neos, new: NEO-, NEON, NEOTER- IC; MISONEISM. 3. Suffixed form “new-aro- in Greek nearos, young, fresh, contracted into néros, fresh (used of fish and of water), hence néron, water: ANEROID. 4. Basic form *newo- in Latin novus, new: NOVA, NOVATION, NOVEL!, NOVEL?, (NOVELTY), NOVICE; INNOVATE, REN- OVATE. 5. Suffixed form *new-er-ko- in Latin noverca, stepmother (< “she who is new”): NOVERCAL. [Pok. neuos 709.] ni. Down. 1. Suffixed form *ni-t- in Germanic *nith- in Old English nithan, neothan, below: BENEATH, UNDER- NEATH. 2. Suffixed (comparative) form *ni-tero-, lower, in Germanic *nitheraz in Old English nither, lower: NETHER. See compound root nizdo-. [In Pok. 1. en 311.] [niké. Victory. Greek noun of unknown origin. NIKE.] nizdo-. Bird’s nest. Compound root formed from ni + *sd-, zd-, zero-grade form of sed-; literally, “place where the bird sits down.” 1. Germanic *nist- in: a. Old English nest, nest: NEST; b. Germanic ‘*nistilon in Old English nestlian, to make a nest: NESTLE. 2. Latin nidus, nest: NICHE, NIDE, NIDUS; EYAS, NIDIFY. [In Pok. sed- 887.] nobh-. Also ombh-. Navel; later also “central knob,” boss of a shield, hub of a wheel. 1. Germanic *nabo in: a. Old English nafu, nafa, hub of a wheel: NAVE?; b. compound *nabé-gaizaz, tool for piercing wheel hubs (*gaizaz, spear, piercing tool; see ghaiso-), in Old Eng- lish nafogar, auger: AUGER. 2. Variant form *ombh- in Latin umbé, boss of a shield: uMBO. 3. Suffixed form *nobh-alo- in Germanic *nabalé in Old English nafela, navel: NAVEL. 4. Suffixed variant form *ombh-alo- in: a. Latin umbilicus, navel: UMBILICUS; NOMBRIL; b. Greek omphalos, navel: OMPHALOS. [Pok. 1. (enebh-) 314.] nogh-. Also enogh-, ongh-. Nail, claw. 1. Suffixed (diminutive) form *nogh-ela- in Germanic *nagla- in Old English negl, nail: NAIL. 2. Form *onogh- in Greek onux (stem onukh-), nail: ONYX; PARONYCHIA, PERIONYCHIUM, SARDONYX. 3. Variant form *ongh- in Latin unguis, nail, claw, hoof, with diminutive ungula, hoof, claw, talon (< ongh-eld-): UNGUIS. [Pok. onogh- 780.] nogv-. Naked. 1. Suffixed forms *nog’-eto-, *nog’-oto- in Germanic *nakweda-, *nakwada- in Old English nacod, naked: NAKED. 2. Suffixed form *nog~-edo- in Latin niidus, naked: NUDE, NUDI-; DENUDE. 3. Suffixed form *nog’-mo- differentiated or developed into Greek gum- nos, naked: GYMNASIUM, GYMNAST; GYMNOSOPHIST, GYMNOSPER\M. [Pok. nog¥- 769.] no-men-. Name. Earlier form *()noo-mn, zero-grade form *(g)na-men-. 1.Germanic *nam6n- in Old English nama, name: NAME. 2. Latin némen, name, reputation: NOMINAL, NOMINATE, NOUN; AGNOMEN, COGNOMEN, DENOMINATE, IGNOMINY, MISNOMER, NOMENCLATOR, NUNCUPATIVE, PRAENOMEN, (PRONOUN), RENOWN. 3. Greek onoma, onuma, name: ONOMASTIC, -ONYM, -ONYMY; ANONYMOUS, ANTONOMASIA, EPONYM, (EPON- YMOUS), EUONYMUS, HETERONYMOUS, HOMONYMOUS,
1083:thresh, tread, wear out: TRITE, TRITURATE; ATTRITION, CONTRITE, DETRIMENT; b. Greek teréddn, a kind of biting worm: TEREDO. 2. Suffixed form *ter-et- in Latin teres (stem feret-), rounded, smooth: TERETE. 3. Suffixed form *ter-sko- in Germanic *therskan, *threskan, to thresh, tread, in: a. Old English therscan, to thresh: (THRASH), THRESH; b. Old English therscold, threscold, sill of a door (over which one treads; second element obscure): THRESHOLD. II. O-grade form *tor(a)-. 1. Greek toreus, a boring tool: TOREUTICS. 2. Suffixed form *tor(e)-mo-, hole, in Germanic *tharma in Old High German darm, gut: DERMA2. 3. Suffixed form *tor(g)-no- in Greek tornos, tool for drawing a circle, circle, lathe (> Latin tornus, lathe): TURN; (ATTORN), CONTOUR, (DE- TOUR), (RETURN). III. Zero-grade form *tr- in Germanic *thr- in Dutch drillen, to drill: DRILL’. IV. Variant form *tré-. 1.Germanic *thréw- in Old English thrdwan, to turn, twist: THROW. 2. Greek tréma, perforation: MONO- TREME, TREMATODE. 3. Suffixed form *tré-tu- in Ger- manic *thrédu-, twisted yarn, in Old English thréd, thread: THREAD. V. Extended form tri- (< “trig-). 1. Suf- fixed form *tri-dn-, probably in Latin tid, plow ox: SEPTENTRION. 2. Suffixed form *tri-dhlo- in Latin tribu- lum, a threshing sledge: TRIBULATION. VI. Various ex- tended forms. 1. Forms *tré-, *trau- in Greek trauma, hurt, wound: TRAUMA. 2. Form *tru- in Greek truma, trumé, hole: TRYMA. 3. Form *érib- in Greek tribein, to rub, thresh, pound, wear out (> ¢ripsis, a rubbing): DIATRIBE, TRIBOELECTRICITY, TRIBOLOGY, TRYPSIN. 4. Form *trdg- in Greek trégein, to gnaw: TROGON. 5. Form *¢rup- in Greek trupé, hole (> trupanon, auger): TREPAN!; TRYPANOSOME. 6. Form *trig- possibly in Old French truant, beggar: TRUANT. [Pok. 3. ter- 1071.] tera-2. To cross over, pass through, overcome. Variant *trd-, contracted from “traa-. I. Zero-grade form “*tr()-. 1. Germanic suffixed form *thur-ila- in Old English thyr(e)l, thyrel, a hole (< “a boring through”): THRILL; NOSTRIL. 2. Suffixed form *tra-kve in Germanic *thurh in Old English thurh, thuruh, through: THOROUGH, THROUGH. 3. Greek nek-tar, overcoming death ‘(see nek-'). 4, Zero-grade form *tre- and full-grade form *ter(a)- in Sanskrit tirati, tarati, he crosses over: AVATAR. Il. Variant form ‘*trd-. 1. Latin trans, across, over, be- yond, through (perhaps originally the present participle of a verb *trdre, to cross over): TRANS-, TRANSIENT, (TRANSOM). 2. Suffixed form *trd-yo- in Iranian thrdaya-, to protect, in Middle Persian srdyidhan, to protect, in Persian sardi, inn: CARAVANSARY. III. Extended form *tru-. 1. Suffixed form *tru-k- in Latin trux (stem truc-), savage, fierce, grim (< “overcoming,” “powerful,” “pene- trating”): TRUCULENT. 2. Suffixed nasalized form *tru-n-k-o- in Latin truncus, deprived of branches or limbs, mutilated, hence trunk (? < “overcome, maimed”): TRENCH, TRUNCATE, TRUNK. [Pok. 5. ter- 1075.] terkw-. To twist. Extension of tera-'. 1. Possible variant form *twjerk- in Germanic *thwerh-, twisted, oblique, in Old Norse thverr, transverse: THWART. 2. Suffixed (caus- ative) o-grade form *tork’-eyo- in Latin torquére, to twist: TORCH, TORMENT, TORQUE}, TORQUE?, TORSADE, TORT, TORTUOUS; CONTORT, DISTORT, EXTORT, NASTUR- TIUM, RETORT!, TORTICOLLIS. [Pok. terk- 1077.] terp-. To satisfy oneself. Greek terpein, to delight, cheer: TERPSICHORE. [Pok. terp- 1077.] ters-. To dry. 1. Suffixed zero-grade form *trs-t- in Germanic *thurs- in: a. suffixed form *thurs-tu- in Old English thurst, dryness, thirst: THIRST; b. Old Norse thorskr, cod (< “dried fish”), whence Norwegian torsk, tosk, cod, with dialectal variant tusk, cod, stockfish: cusk. 2. Suffixed form *ters-d- in Latin terra, “dry land,” earth (> French and Old French terre, earth, ground): TERRACE, (TERRAIN), TERRAN, TERRENE, TER- RESTRIAL, TERRIER, TERRITORY, TUREEN; FUMITORY, INTER, MEDITERRANEAN, PARTERRE, SUBTERRANEAN, TERRAQUEOUS, TERREPLEIN, TERRE-VERTE, TERRICO-
1137:derivatives violdre, to treat with force, and violentus, vehement: VIM, VIOLATE, VIOLENT. [In Pok. 3. wei- 1123.] weik-', Clan (social unit above the household). 1. Suf- fixed form *weik-slé in Latin villa, country house, farm: VILLA, VILLAGE, VILLAIN, VILLANELLE, (VILLEIN); (BI- DONVILLE). 2. Suffixed o-grade form *woik-o- in: a. La- tin vicus, quarter or district of a town, neighborhood: (VICINAGE), VICINITY; b. Greek oikos, house, and its derivative oikia, dwelling: ANDROECIUM, AUTOECIOUS, DIOCESE, DIOECIOUS, DIOICOUS, ECESIS, ECOLOGY, ECON- OMY, ECUMENICAL, HETEROECIOUS, MONOECIOUS, PAR- IsH, TRIOECIOUS. 3. Zero-grade form *wik- in Sanskrit vis-, dwelling, house, with derivative vaisyah, settler: Vaisya. [Pok. weik- 1131.] weik-2. In words connected with magic and religious notions (in Germanic and Latin). 1. Germanic suffixed form *wih-l- in Old English wigle, divination, sorcery, akin to the Germanic source of Old French guile, cun- ning, trickery: GUILE. 2. Germanic expressive form *wikk- in: a. Old English wicca, wizard, and wicce, witch: WITCH; b. Old English wiccian, to cast a spell: BEWITCH. 3. Possible suffixed zero-grade form *wik-t- imé in Latin victima, animal used as sacrifice, victim (although this may belong to another root *(a)wek- not otherwise represented in English): vicTiM. [Pok. 1. weik- 1128.] weik-3, To be like. 1. Suffixed variant form ‘*eik-on- in Greek eikdn, likeness, image: ICON, (ICONIC), ICONO-; ANISEIKONIA. 2. Prefixed and suffixed zero-grade form *n-wik-és, not like (*n-, not; see ne), in Greek aikés, unseemly: AECIUM. [Pok. 3. weik- 1129.] weik-4. Also weig-. To bend, wind. I. Form weig-. 1. Ger- manic *wik- in: a. Old English wice, wych elm (having pliant branches): wyCH ELM; b. Swedish viker, willow twig, wand, akin to the Scandinavian source of Middle English wiker, wicker: WICKER; C. Old Norse vikja, to bend, turn, probably akin to the Scandinavian source of Old North French wiket, wicket (< “door that turns”): WICKET. 2. Germanic *waikwaz in: a. Old Norse veikr, pliant: WEAK; b. Dutch week, weak, soft: WEAKFISH. 3. Germanic *wik6n-, “a turning,” series, in Old English wicu, wice, week: WEEK. II. Form *weik-. Zero-grade form *wik- in: a. Latin vix (genitive vicis), turn, situ- ation, change: VICAR, (VICARIOUS), VICE; VICISSITUDE; b. Latin vicia, vetch (< “twining plant”): veTCH. [Pok. 4. ueik- 1130.] weik-5, To fight, conquer. 1. Germanic “wik- in Old Norse vigr, able in battle: WIGHT2. 2. Nasalized zero-grade form *wi-n-k- in Latin vincere (past participle victus), to conquer: VANQUISH, VICTOR, VINCIBLE; CONVINCE, EVICT. [Pok. 2. weik- 1128.] weip-. To turn, vacillate, tremble ecstatically. 1. O-grade form *woip- in Germanic *waif- in Old Norse veif, waving thing, flag, probably akin to the Scandinavian source of Anglo-Norman waif, ownerless property: WAIF!, (WAIVE), (WAIVER). 2. Variant form *weib- in Germanic *wipjan, to move back and forth, in: a. Old English wipian, to wipe: WIPE; b. Old French guiper, to cover with silk: GUIPURE; c. Middle Dutch and Middle Low German wippen, to swing: WHIP. 3. Perhaps suffixed nasalized zero-grade form *wi-m-p-ila- in: a. Old English wimpel, covering for the neck (< “something that winds around”): WIMPLE; b. perhaps Middle Dutch wimmel, auger (< “that which turns in boring”): WIMBLE. 4. Suf- fixed zero-grade variant form *wib-ro- in Latin vibrdre, to vibrate: VIBRATE. [Pok. weip- 1131.] weis-. To flow. I. 1. Germanic *wisdn-, waisén- in Old English wdse, mire, mud: 00ZE?. 2. Taken by many as a derivative of this root, but probably an independent Indo-European word, is the suffixed form *wis-o- in Latin virus, slime, poison: VIRUS. 3. Extended zero-grade form *wisk- possibly in Latin viscum, mistletoe, birdlime: VISCID, VISCOUS. II. Attributed by some to this root, but more likely of obscure origin, are some Germanic words
1266:ASTERIATED | ster-3 ASTERISK ster-3 ASTERISM  ster-3 ASTEROID ster-3 ASTIGMATISM _ steig- ASTONISH (s)tena- ASTRAEA | Ster-3 ASTRAGAL ost- ASTRAGALUS ost- ASTRAL  ster-3 ASTRAPHOBIA | ster-3 ASTRINGE | streig- ASTRO-  Ster-3 ASTROBLEME gWele-1 ASTROLABE (s)lagW- ASTRONAUT nau-2 ASTRONOMER nem- ASTRONOMY nem- ASTUTE wes-3 ASTYLAR sta- ASUNDER sen-2 ASYNDETON dé- AT ad- ATARACTIC dher-1 ATAVISM atto-, awo- ATAXIA tag- ATHEISM dhés- ATHELING _ athal- ATLANTIC tele- ATLAS tele- ATMAN étmen- ATMOSPHERE wet-' ATOM tem- ATONE ol-no- ATRABILIOUS ter- ATRIUM ater- ATROCIOUS ter- ATROPHY threph- ATTACH steg- ATTACK steg- ATTAIN tag- ATTEND ten- ATTENUATE ten- ATTEST trei- ATTITUDE ap-! ATTO- okt6(u) ATTORN  tere-! ATTRACT tragh- ATTRITION tere-1 AUBADE albho- AUBURN = albho- AUCTION aug-1 AUDIBLE au-5 AUDIENCE au-5 AUDIENT au-5 AUDILE au-5 AUDING au-5 AUDIO- au-5 AUDIT au-5 AUDITOR au-5 AUDITORIUM § au-5 AUDITORY au-5 AUGEND aug-1 AUGER nobh- AUGHT! = aiw- AUGHT2 wekti- AUGITE aug-2 AUGMENT aug-1 AUGUR aug-t AUGUST aug-1 AUK el-2
1902:NATAL gene- NATANT sna- NATATION sna- NATATORIAL sna- NATATORIUM sna- NATES not- NATHELEsS to- NATION gene- NATIVE gene- NATURE gene- NAUGHT ne, wektl- NAUGHTY ne NAUSEA nau-2 NAUTCH ner-2 NAUTICAL nau-2 NAUTILUS nau-2 NAVAL nau-2 NAVE? nobh- NAVEL nobh-, nau-2 NAVIGATE ag-, nau-2 NAVY nau-2
1930:NODE ned- NODULE ned- NODUS ned- NOEL gene- NOESIS nous NOISE nau-2 NOISOME od-2 NOMA nem- NOMAD nem- NOMBRIL nobh- NOME nem- ie NOMENCLATOR kela-2, no-men- NOMINAL no-men- NOMINATE no-men- NOMOGRAM nem- NOMOGRAPH nem-
1975:OMNIBUS op-! OMNIFARIOUS dhé-1 OMNISCIENT skel- OMNIUM-GATHERUM op-! OMPHALOS nobh-
2432:UMBEL andho- UMBILICUS nobh- UMBO nobh-
=== HRN
2198:207. burnäf bernä Müngling', burnm 'Jugend, Kindheit',
9180:LW. '^.IJ-)) und np. näf zurückgehen. Das jüngere
11051:191. Hiiflfßnltan zufriedenstellen', snäfjm(i)sn, snäyTnitärlli,
11091:np. tenäfür erscheint nur in Pärsenschriften.
14414:nnäfi- 1015.
16461:näf I0-.JO.
```


## [2026-09-07T19:31:02.045Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('HRN.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i,l in enumerate(leaves):\n    if '1029.' in l or ' näf ' in l or 'näf ' in l:\n        pass\n# find leaf containing line 9180 context\nlines=t.split('\\n')\nprint('\\n'.join(lines[9160:9200]))\nEOF"
}
```


## [2026-09-07T19:31:03.413Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n '^ *1028\\.\\|^ *1029\\.\\|^ *1030\\.\\| 1029\\. ' HRN.txt | head; echo \"--- Horn entries near 'Nabel'\"; grep -n 'Nabel' HRN.txt | head -20"
}
```


### [2026-09-07T19:31:03.656Z] TOOL RESULT

```
Bartholomae meint nach briefl. Mitteilung, dass
nihuften sein h von np. niMti (No. 1058) bezogen
habe; ai. i^^göp- sei vielleicht eine Nebenform von
[y^göh^ und die dazu gestellten Formen stammten
also nur zum Teil von göpä- 'Hirt*. Vergl. auch
Johansson, Indog. Forsch. IL 50, 51. Jedenfalls
wird es schwer, mhffffeti gänzlich von \ ^göh- zu
trennen.
1060. nei 'Schilf, «af *Flöte\ näl; vergl. A-e/Te|wfl7, stlrjndT
Testflöte* '), seh^näi ; nnlze.
g. nad.
ap. *nada' 'Schilf; phlv. nai bezw. nad (PPGl);
ai. nadd-, nadd- Schilfrohr (Pischel, ZDMG. :U),
717 folg., Ved. Studien I, 183 folg.); arm. net Pfeil*
(H. No. 219)?
Die Lautverhältnisse sind noch nicht richtig er-
kannt. Np. nei, g. nad setzen unbedingt eine Urform
*nada- voraus ; neben dieser gab es eine zweite Form
*narda-, auf welche ai. nadd- (gr. LW. vdodo^*, hebr.
LW. '^.IJ-)) und np. näf zurückgehen. Das jüngere
skr. näld- ist persisches Lehnwort. Wie häufig,
erscheint dann auch eine gedehnte Form, np. näl^
ai. nädt-, die nicht mehr 'Schilf, sondern ein 'Musik-
instrument aus Rohr, Flöte* bezeichnet. Skr. Hald-
wird jüngere Form für nadd- sein, wie Pischel an-
nimmt, nalada- ist sanskritisirtes vd^öoq,
1061. ne 'nicht' (Öähn. I, 198 Anm. 2, Calc), vergl. nPsi
(No. 1066), niy[ayed,
ap. naiy 'nicht'; aw. nöit, na^ci-; päz. ne; ai. ncd.
oss. d. 7ie6i, t. ntci nichts' (201).
*) Kauk.-bergjüd. eürnai 'Schalmei*, russ. LW. zurna.
*) Die aus dorn Persiacbeii entlehnt sind.— 288 —
1062. niyä 'Grossvater, Ahne (Plur. myagän),
ap. aw. nyäka- *Grossvater , vergl. ap. apangäka'
Ahne'; phlv. nyok.
af;'. nlka *6rossvater, LW. niya 'Grossmutter*;
bei. näkü, n. nüxö 'Oheim* (258), fwl^ *Grossnuitter'
(250).
1063. niymn 'Scheide*.
ap. *nigama', vergl. skr. w^ + l^f/am-, mgamd-
```


### [2026-09-07T19:31:03.709Z] TOOL RESULT

```
8920:1028. nerm "weich, sanft', nerml,
8926:1029. ne^^d "nahe', nezdik^ nezdiki,
--- Horn entries near 'Nabel'
8853:1020. nfe/ 'Nabel', nafe,
8856:schaft*; phlv. nafak, f?^/ 'Nabel', vergl. N[a]f^[far'nai
8860:kurd. näw 'Nabel'; afy. nti^ nüm; oss. d. naffä;
```


## [2026-09-07T19:31:11.241Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '8840,8875p' HRN.txt; echo \"=== nearest page markers\"; awk 'NR>8700 && NR<8900 && /— *[0-9]+ *—/{print NR\": \"$0}' HRN.txt"
}
```


### [2026-09-07T19:31:12.533Z] TOOL RESULT

```
phlv. näcuk.
LW. kurd. näzik; afj'. näzak, vergl. vPnzaka; bei.
näzurk, n. näzuk.
1018. näsüdefi 'abmagern'.
aw. [/^nas-, nasy^iti verschwinden', Causat. 'ver-
schwinden machen'; phlv. na^mtan Vernichten' (P.-
Vend.) ; ai. l^nag-, ndgyati verschwinden, verderben'.
wa/. nüs-am, Hiyn. hinis-am sar. binäs-am Ver-
lieren*.
1019. näStä 'nüchtern' (AM. 216 Zeile 5), benästa (AM.
232 Zeile 2, 3), nastab, nastat,
na + ai. V^aQ-, agndti *essen', Nöldeke, münd-
liche Mitteilung, doch vergl. unter np. äs (No. 29).
1020. nfe/ 'Nabel', nafe,
g. nafk.
aw. nafah' 'Geschlecht*, vergl. nOfya^ 'Verwandt-
schaft*; phlv. nafak, f?^/ 'Nabel', vergl. N[a]f^[far'nai
(Gemme, ZDMG. 18 No. 37 (IV)).
>) Vergl. S. 197 Anm. 1.
2) Vergl. Bartholomae, BB. XVII, 133.— 229 —
kurd. näw 'Nabel'; afy. nti^ nüm; oss. d. naffä;
bei. napag, nafag, n. nafay (259).
aw. naba[nazdista', ai. ndhhi- etc. gehen auf indog. bh
zurück, während die übrigen Formen auf ph weisen.
lOS^O'»'» nak Vermischt, nicht pur, verunreinigt*.
phlv. andk *böse', anokih^).
lC^t21. noffäh plötzlich, unerwartet*.
aw. *anäkasa' *improvisus* ; phlv. anakäslhd 'un-
vermutet', vergl. np. (igäh (No. 40).
näl 'Schilf* siehe nei (No. 1060).
1-022. näm 'Name' 2).
ap. nOtnan- 'Name* ; aw. nquian- ; phlv. mim, nCLmik
berühmt*, nämlnltan (PPGrl.); ai. wamaw- ; arm. anim
(H. No. 24).
LW. (?) kurd. näw 'Name' ; afy. nüm ; bei. nam
(181) ; oss. (echt) t. nom, d. non (198).
=== nearest page markers
8749: Uorn. Orundriss <J. neup. Fltyniolo^ic. ],j— 226 —
8786: ') Seifenkraut; Ochsenurin.— 227 —
8824: 15*— 228 —
8859: 2) Vergl. Bartholomae, BB. XVII, 133.— 229 —
```


## [2026-09-07T19:31:28.195Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BRT.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i,l in enumerate(leaves):\n    if 'nafah-' in l or 'nāfya' in l or 'nabā-nazdišta' in l or 'naba-nazdista' in l:\n        print('LEAF',i, l[:2500])\n        print('-----')\nEOF"
}
```


### [2026-09-07T19:31:29.466Z] TOOL RESULT

```
LEAF 592 V.  15.21.
KompE.  —  Snpetl.  ta  ^niadyah-  •propior'  und zu  üsna-  'propinquus'.  —  ai.  nidkfha-  Adj., iDp.  nazdht.  —  zEt.  (ar.  *ncaäiil/ia-  tu  einem Praes.  3  *nä-tda-li,  lum  V.  »Airf-)  »gl.  ZDMG. 50.  686,  Bgu.  Grdr.»  /.  735.  —  Pfl.:  nazdist, (zu  Y.  33):  natäli.  —  ')  Hdi.  maidilla;  Pü.: fehlt.  —  ')  Abgesehen  von  den  luvor  aus- drucklich genannten.  PiiErl. :  afil  i  iapastän 'ram  Ort  der  Nacht  weg',  daher  DST.  ZA. 3.  142  >Ie  feu  du  campement';  s.  auch  Sp. Komm.  I.  367.
•  j.  nazdyö  Adv.  '(räumlich)  näher  zu  — , an  -'  (Akk.) :  w  mqm  upaMSia  "tritt  näher zu  mir  heran"  Yt.  27.  31;  21;  —  ..Aisvasca .  .  *ra%wyff.varsH  (sd.)  'yS  ahmt  aztm  yS ahurS . .  vlspahe  awhsus  astvaiB  *manasca *vacäsca  ^iyaeiina^a  yaSia  , .  ". .  bin  ich  . . den  Gedanken  und  Worten  und  Taten der  gesammten  Menschheit  näher  als  . ."
P.2Ä
ASn.  aus  'ntaäyoÄ-  Adj.,  Kompar.  zu  naidisla- IfiA.).  —  ai.  n/diyah  Adv.;  np.  »aji/ 'nahe'. — Pü. :  naxdiilar.
•  j.  naSta-  Adj.,  PPfP.:  s.  *nas: KompA.,  E.
•  j,  "^naStlLzamanä- ''  Adj.  (mask,  °na-) '(der  seinen  Verdienst  verloren  hat  sva.) der  sein  Brod  nicht  mehr  verdienf,  vom Hund:  yal  sünil  para.tri^ynti  'nasca pairistajcsudrasca  V.  ij.  50.
Pü. :  ha  miai'),  erl. :  o  änÜ  tu  ariit.  —  i)  So L4.  NA.  nisid',  worin  ich  eine  Ausgleichung mit  dem  folgenden  Wort  sehe.  —  ')  DsT.s Bemetkung  ZA.  3.  20E  No.  73  ist  mir  un- verständlich.
•  j.  "nahaowf^  N.<^:  -?-,
Pü.:  fehlt
•  j.  "lüuiti  As  aSe  ysi  mafyäAa  ^aranti framanyäe  V.  7.  55 :  —  ?  — .
Pü. :  ivnöi  hit  imäk  ic  martum  ha  -  iSi  dänel -  j^artt  frä/ea  msnii  bardtnm;  s,  daiu  Sp.
Komm.  I.  32Ö,  DsT.  ZA.  3.  110.
•  j.  näuma-  Adj.;  s.  unter  navama-.
],  nSumayäcil  V.  8.   l8i  lies  naomayaüi.
•  j.  nium^tn  Adv. :  s.  naoma-.
j.  näuya  Yt  l6.  3:  lies  nävaya.
•  j.  "yaAmi  gashe  k^sa  vasta  Aaoa  nara faha  mara  Ada  nä.tanasuä"  Yt.  i3. 8:  -?-■>.
»>  Ohne  Wert  GdN.  Stud,  /.  81.
•  g.,  j.  naidyah-  Adj.  'der  schwächere; unterliegend':  läiizl  nh  syaeäsanäil byenti.. hyat  as  *aoJä  'dyattAtm  "denn  durch  diese
Taten  setzen  sie"  uns'' in  Furcht , ,,  inso- fern er"'  stark  ist,  (mich)  den  schwächeren" Y.34.Z;  —  _v«5a  aojä  'dyanAtm  Y.j7. io'>;  —  'dy&tpAs  {Q&.)i^  gaotumahe  {%^) parS.yä  Yt /^.  16**.
Kompai.  aus  der  Basis  ar.  *nädh-;  vgl.  ai. nidh
-----
```


## [2026-09-07T19:31:33.437Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '18855,18900p' BRT.txt; echo \"=== col markers nearby\"; awk 'NR>18800 && NR<18960 && /^[0-9]{3,4}$|^ *[0-9]{3,4} *$/{print NR\": \"$0}' BRT.txt"
}
```


### [2026-09-07T19:31:34.641Z] TOOL RESULT

```
•  j.  "nahaowf^  N.<^:  -?-,
Pü.:  fehlt
•  j.  "lüuiti  As  aSe  ysi  mafyäAa  ^aranti framanyäe  V.  7.  55 :  —  ?  — .
Pü. :  ivnöi  hit  imäk  ic  martum  ha  -  iSi  dänel -  j^artt  frä/ea  msnii  bardtnm;  s,  daiu  Sp.
Komm.  I.  32Ö,  DsT.  ZA.  3.  110.
•  j.  näuma-  Adj.;  s.  unter  navama-.
],  nSumayäcil  V.  8.   l8i  lies  naomayaüi.
•  j.  nium^tn  Adv. :  s.  naoma-.
j.  näuya  Yt  l6.  3:  lies  nävaya.
•  j.  "yaAmi  gashe  k^sa  vasta  Aaoa  nara faha  mara  Ada  nä.tanasuä"  Yt.  i3. 8:  -?-■>.
»>  Ohne  Wert  GdN.  Stud,  /.  81.
•  g.,  j.  naidyah-  Adj.  'der  schwächere; unterliegend':  läiizl  nh  syaeäsanäil byenti.. hyat  as  *aoJä  'dyattAtm  "denn  durch  diese
Taten  setzen  sie"  uns'' in  Furcht , ,,  inso- fern er"'  stark  ist,  (mich)  den  schwächeren" Y.34.Z;  —  _v«5a  aojä  'dyanAtm  Y.j7. io'>;  —  'dy&tpAs  {Q&.)i^  gaotumahe  {%^) parS.yä  Yt /^.  16**.
Kompai.  aus  der  Basis  ar.  *nädh-;  vgl.  ai. nidhilä-  Adj.  'bedrängt,  hilfsbedürftig',  ksL naida  'Not';  s.  dam  Roth  ZDMG.  25.  330, Gdn.  KZ.  ag.  5S4-  —  Pü.:  naadtn  dahUn {yiiiT.-a  DsT.  ZA.  1.  253).  —  »  'sie  uns',  d.  i. der  Irrlehrer  (Pii.  erl.  richtig  airamSy,  s.  unter iay-)  und  seine  Anbänger  mich  {Zara^ui/ra} und  meine  Anhänger.  Im  Folgenden  bat  Zar. nur  den  Irrlehrer  allein  und  sich  selbst  im Auge,  daher  er  nun  den  Sing,  braucht:  "er .  .  den  schwächeren".  —  ')  Aus  Y.  _j^  8 beruh  ergenommen.  —  3)  Man  erwartete  °ar>A', wie  aber  nur  minderwertige  Hds.  bieten.  VII. war  auch  hier  die  Erinnerung  an  Y.  34.  8 wirksam,  s.  No.  2.  —  4)  Zu  Darabs  Ansicht  ■ s.  unter  gaoUma-.
•  j.  näfa-  m.  'Nabel' :  °/S¥.3  g.  a)  'Ver- wandtschaft, Familie':  Aaväi  kscit  '/ai''> havayäi  vise  Aaväi  zantave  Aavayäi  äaiA- Aave  "jede  für  ihre  Familie  . ."  Yt  13.66; —  *yavata  Ai  °/e  *x"ahwan/tä  (sd.)  N,  I7.
KompE;  AbleiL  (s.  auch  •nä/aina-).  —  VgL nä/ah-  und  itaiämadii/a:  —  np.  »ä/  'Nabel* ; ai.  Tgl.  näMqy-  f.  'Nabel',  s.  dazu  S  2j  b.  — Pü.:  Hä/ai.  —  I)  Sonst  erscheint  in  dieser  Zu- sammenstellung nmäna-  n.  'Haus',  sd.  mit  *).
•  j.  nafah-  n.  'Verwandtschaft,  Familie': gayehe  (sd)  mar^hru}  . .  yaAmat  Aata  frä- ^wpTPsat  (näml.  aAurö  matda)  °/3'^  airya- nam  dahyunatn  Yt. /J.  87.
Vgl.  näfa-.  —  I)  Allenfalls  AP.  aus  ♦nä/-  f.. Tgl.  ai.  nabh-  l.
•  j,  näfya-  Adj.  familienangehörig,  ge- schlechtsverwandt"': druatam  °/lm  fbatSs
VytJ7  (?)'>■
KompA.  —  Ableit.  aus  näfO'.  —  ■)  Gdn.s Erklärung,  VSt.  2.  19  ('adelig')  ist  verfehlt; vgl.  oa/fl.  No.  1  und  Pü.  zu  aä/yS.liu-,  — «)  Vgl.  Y.  63.  7.
•  j.  näfyö.karSta-  Adj.  'von  Familien- angehörigen, Geschlechtsverwandten  be- wirkt, \eiAXÜ.3£,A':paitistätJe  'taAe  lbag£at»hs Yt.  13. 120.
•  j.  näfyö.tbis-  Adj.  'der  die  Familien- angehörigen, Geschlechts  verwandten  be- feindet'; inä  nS . .  dusrfta»a»Ae . .  mä  'IbÜe Y.  65.  7.
Pü. ;  nSf  bes,  crL;  kt  patuiandätt  bistl.
•  p.  nima",  nämä"  Adv.:  s,  näman-.
•  j.,  g.,  p.  näman-,  j.  n^tnan-"  n.  "Name":
äat  hi  'ma  fradai^yh  atr».dät)m  vä  . . Aqmät  va  ii/rf.dä/aAe  (sd.)   'ma  V. /Ä53;
dby  Google
1063  lumoan-  AI
Vd,/}";  —  ya^qmca  pars  mafyaia  ahoi- ta^a^a{&A.)..gaitinqm  'mqm{AS.)  däian Yt  IQ.  6;  —  yä  vs  vamtkU  (nämL  äp5) ahurS  mazdä  *°mqm'^  dadäi  .  .  täii  vi yazamaiäl  Y.  ^JÄ  4;  —  tq  yazsi  ifaii •w»ir/(IPO  pairicä  jasüi  (sd.)  vanta  Y. 57,22;  —  hyat  vä  töi  'manqtn  vözObm atan  . .  tä  äjoj  pairijasumaidi  Y.  j6'.  3;
—  anusS  ipfnti  vaakBi  sflräU  'mqn  (als IP.)  äiii^a  Y.  75.  1,  Vr.  tf.  i;  —  'tSm  .  . ahüirys  °«Är(als  IS.)  magda.vars  (sd.) . . yasamaiäf  Y.jj.^;  —  'mini  spu  yaza- maide  YtJ^,  79:79';  —  kaAe  nS  ila •ma  ayairydiiSp.  512  m.)  Yty.50;  — ahmä^m  'ma  . .  yat  amsSanqm  spintanqm tat  asH  mq^rake    spmiahe  amavästtmim
•  Yt7.3; — frsit  mg  tat  'ma  framrüm  Yt /.  S;  — yasia  me  .  .  tmi  •inlnli  (als  AP.) drfftJayS  . .  Yt/.  16;  11,  15;  —  ^vjsqs *taia  imi  'msnü  (als  NP.)  parltas^a  '.  . vismie  Yt /.  19;  —  l&sca  mg  °ma  (AP.) abaya^a  Yti5. 49,  50;  —  gSusca  'ma mazdaoätfm  Yt  Ä  2 ;  —  'mSni  amslanqtn sptnianqm  Ytrf-a;  7;  —  sPaitka  va  duyta va  'va'ni  V.  14. 15  (?) -ö.  a)  AS.  und  LS. (im  Sinn  des  IS.)^*  als  Adv.  'mit  Namen'; i)  im  jAw.  AS.  nqma,  hinter  dem  Nom. propr.ä':  iar^zahi ..yat  vaolii^A^ häkairJm °ffio  Yt/0.88;  12-7,  i^-SS';  — pairikayai .  .yS  duzyairya  yqm  mafyaka  . .  Auyäiryqm 'ma  ao/aiti!  (sd.)  YtÄ  51;  V. /j.  z,  6;  — tturf/S  .  .  yim  ma^aka  .  .  kahrkatas  'ma ac/ai/e  (sd.)  V.iS.i$;  17.31  —  vayui  bä 'ma  äkmi  Yt  75.  43 ;  43-48  (oft),  /.  7,  8, 12—15  (oft);  —  vairil yB  haosrava  'ma YtJp-sö;  59,62,  7.30,7^,129',  142,74. 59*,  V, /i".  15;  —  ar?dvi  'ma  apa  V.7.16;
—  ahm.ye^he.raocä  'ma  aiaonS  /ravalXm Yty.i2o;i2o'; — hinter  demNom.appelL: vJzari^  dagvs  'ma  N.ig.ii).  2)  Bim Ap.  LS-,  uzw.  a)  näma",  b)  namä";  ersteres folgt  dem  Namen  eines  mask.  oder  neutr., letzteres  dem  eines  fem.  Appellativs*'; a)  nämtf;  sowohl  der  Name  als  das Appellativum  stehen  unter  allen  Umständen im  Nominativ'';  al  das  Appellativum  geht voraus :  i  martiytr  magui  ähJ'  gaumntJ' •wo"  Bh.J.ii;  i6',  2.3,  5,  6,  i4,^-3.  S.  I3. 5,1'; — avahyS  k<^büjiyakya  bräta  bardiyt^ °m^  ak(^  "illius  Cambysis  firater  Bardiyas nomine  erat"  Bh.7. 10.  ast)  statt  des Appellativs  erscheint  i'*:  7  gaumäti^  'ma' äh<^  hauv  adurujiyj'  Bh.^  a ;  2*.       ß)  das
Appellativ    folgt:    *parg<^    'mii'    kauft^ avadä  , .  Bh,j,  7;  7. 11;  —  tOzäm^  'mii' vardanam  Bh,  7. 19;  2.3,  6,  12,  16,^.1,  5. 6,  8,  2.  7;   —  AaÜa  piravJ'  •««"  rauür D.77. 3".        7)  ohne  Appellativ;  wir  über- setzen dann  'einer  namens  , .'  oder  'ein  ge- wisser"*': kt^baßya*  °»w"  kärausptth^^ .. püruvam  ida  lüäya^iyi^  aAi/'  'Bh.i.io;  — taxmaspad^  'md'  mSd(^  manä  b(^dakt^ Bh.2.i4;io,j.3,6,q,  i4,^i8*,S.7.      Ohne Wert:     darayj'vcTus     vistaspakya     'mi^ /«ä'a*    Ao.  7.  2;   2.        b)    nätm/*;    das Appellativ  folgt:  hauv  udapatalä  habiraav dubali^  -ff/j"  äahyaus  haca  avadasa^  Bh. J-»3;3.  5.  »o.  ^-»S-i-ö,  10, 11, 13;— /«fra* -Ma"  dida  arminiyaiy  avadä  hamaranam akunav<i'  Bb.2,8;  9,   7.13, _j. 9,  11. KompA.  (n^iH'),  E.  —  tä.  tUiman-  n.,  np.  nän. —  P6,i  näm;  s.  nOch  No.  3.  —  >>  Nur  in  nfiu, aber  hier  stets.  —  >)  So  alle  Hds.,  mit  jinei Ausnahme,   J  3,   wonach  NA.  'oif  bietet  — 3)    Fü.:    nndeaüichi    a/ä^i  addpnark  ann (Jamaspji  Gloss.  569  u.)  paakann.  —   1)  S. No.  6.  —  5)  Von  dem  es  nur  durch  ein  Ed- klitikum  getrennt  sein  kann.  — ')  Die  Frage, wie     ap.    t^amf    beim     mask.    nnd     neutr., rfiamt^  beim  fem.  Appellativum   formal   and syntaktisch    zu    fassen    sei,    ist    noch  nicht gelöstj  luletit  darüber  FoY  IF.  la.  171,   wo weitre  Litt.  —    7)  S.  No.  9.-8)  Vgl.  FOV aO.   174.  -^  9)  Fovs  Fassung  von  ßiräva*  aU Abi.,  aO.  176  halte  ich  nicht  für  richtig;  ich verlange  auch  hier  den  Nom.j   s.  Sp.  907  o.
•  j.  "näyaäta  N.  4(5'',
Pa.i  fehlt  —  0  DsT.  liest  nä  yaHa.
j.  ava  niyn'ifiTm  P,  Jj:  lies  0x10.10/0/1/!!».
•  j.,  p.  nav-  f.  'Schiff"'.
KompA.  (s.  nmäta-);  Ableit  —  ai.  tiav-  f., np.  Mäti,  —  ')  S.  übrigens  näviyä-  No.  1.
•  3.  nävaya-  Adj.  (fem.  °ya-)  'schiffbar',  Be- zeichnung fli essenden  Wassers  von  grösserer Breite  und  Tiefe:  airysJayatam  ..yahmya apö  'y&  p^n%wi/  XiaoiartAa  %waxi?nU Yt  10. 14;  —  . .  'hraotS.siacS  apa  taänä 'yä  Yt/J.  ro;  — pxavS /raoirisyBti  tarasca apB  'ya  (APf.)  V.  14. 16;  7<y.  74;  —  tyaäa *nä  buyat . ,  hupirihwe  a/s*'ya''>  Yt.i6.y,
—  apqm  vä  'yanqm  paiti pfntBsYt.11.^;
—  dasanqm  apqm  'yanqm  aojS  ytÄ24; 74-39;  —  'yayai  .  .  ape  N.  ^7;  67;  — yai  nSit  spa  . ,  mag^e  va  cäiti  va  vaimi va  urüili  va  ape  va  'yä  (GSf.)  pai&yaiie
V.i?-37-
Ableit  ans  *näv:  —  Statt  «äviya-  getchr., S  S6S.  n  b;  vgl.  No.  I.  —  Pü.!  äfi  i  nis ISi'),  eri.  (in  V.  t4):  ktdd»  ;  äfiän  fia dan.    —    ')  So  J 10;    NA.   nach   Fl  nättya.
ob,Google
:o6s
=== col markers nearby
```


## [2026-09-07T19:31:47.090Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KNT naf\"; grep -n -i 'naf' KNT.txt | head -10; echo \"=== MON natrun\"; grep -n 'نطرون\\|نطرن' MON_part1.txt MON_part2.txt incoming/MON/*.txt 2>/dev/null | head -10; echo \"=== MON nitrogen\"; grep -n 'نیتروژن\\|نیترات\\|نیتریک' MON_part1.txt MON_part2.txt incoming/MON/*.txt 2>/dev/null | head -10"
}
```


### [2026-09-07T19:31:47.179Z] TOOL RESULT

```
=== KNT naf
1213:pIE *nek-to-, OP vi-nasta- ‘damage’; for cognates, see Lex. s.v. naf-.
2938:(a) In optative clauses explanatory of kdma ‘de- sire’, introduced by tya ‘that’: kariyaiš DNb 9, 11; einafayai$ DNb 20; frabiyaiš ОМ 21 (without tya).
4127:19 2 : parsàmiy : паа : kama : tya : mar^üya 20 : vinaflayais : naipatimà : ava : Каша : yadi 21 y : vináfayais : naiy : frafiyaiS : martiya : 22 tya : рау : martiyam : (айу :ava : mam : 23 палу : varnavataiy : yátà : uradanám : hadu 24 рат : àxinautiy : martiya : tya : kunau 25 tiy : yad'ivà : abaratiy : anuv : tauman
=== MON natrun
=== MON nitrogen
MON_part2.txt:7347:فسفات‌ها با نیترات نقره رسوب زرد فسقات 
MON_part2.txt:18254:نیترات پتاسیم است. کاسنی در تداوی به 
MON_part2.txt:25909:و در ظرفی مقداری اسیدنیتریک (تیزاب) 
MON_part2.txt:29384:در اسید نیتریکک به خوبی حل می‌شود. گالن 
MON_part2.txt:42576:تیزاب (اسید نیتریک) می‌دهند. تیزاب محل 
MON_part2.txt:78449:نیترات نقره و بخار اکسید ازت حاصل 
MON_part2.txt:79534:جوش حل می‌شود). ۲ - نیترات‌ها - که 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:7347:فسفات‌ها با نیترات نقره رسوب زرد فسقات 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:18254:نیترات پتاسیم است. کاسنی در تداوی به 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:25909:و در ظرفی مقداری اسیدنیتریک (تیزاب)
```


## [2026-09-07T19:31:48.578Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in BQT_v1_pages.txt BQT_v2_pages.txt incoming/BQT/BQT_v3_pages.txt incoming/BQT/BQT_v4_pages.txt incoming/BQT/BQT_v5_pages.txt; do echo \"== $f\"; grep -c 'ناف' $f 2>/dev/null; done"
}
```


### [2026-09-07T19:31:49.851Z] TOOL RESULT

```
== BQT_v1_pages.txt
97
== BQT_v2_pages.txt
90
== incoming/BQT/BQT_v3_pages.txt
54
== incoming/BQT/BQT_v4_pages.txt
104
== incoming/BQT/BQT_v5_pages.txt
15
```


## [2026-09-07T19:32:05.823Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && head -3 BQT_v4_pages.txt; echo ...; grep -n '\\[pdf page' BQT_v4_pages.txt | head -3; echo \"=== search 2100\"; grep -n '۲۱۰۰\\|2100' BQT_v4_pages.txt | head -10; echo \"=== v5\"; grep -n '۲۱۰۰' BQT_v5_pages.txt | head -5"
}
```


### [2026-09-07T19:32:05.900Z] TOOL RESULT

```
[pdf page 1]
[pdf page 2]
ه
...
1:[pdf page 1]
2:[pdf page 2]
23:[pdf page 3]
=== search 2100
3082:( موفلط عزطهو2۳ , 8۳8621007 30106 ) < ژابا ی ۳۹۵ مرکب از : مرک + موش
3982:۱- هز . 22255789۳2 ۰ 210016 ( آلوچه ) ‎٩‏ بونکر ۱۱۵ *. درعربیمشمش
18064:۵8۵۲۵۳ ؛ کردی -600 , 126۷۷۰ ؛ استی -31 ۰ 30 . بلوچی 02100 , -11230 ۰ -/8۷ظ۵ ؛
19318:4 و اسح 1182۷87982 است . ظ . ازکلمةٌ عبری 02۳82100 [8808. هبل
20986:(2100 «عقار ۱۶۹ف» (ر: ارقان) برناً شم اول وفتح دوم و سوم مشدد * ات ایک
=== v5
```


## [2026-09-07T19:32:12.178Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && awk 'NR>=18000 && NR<=18110' BQT_v4_pages.txt; echo \"=== pdf page tag before\"; awk 'NR<=18064 && /\\[pdf page/{p=$0} END{}' BQT_v4_pages.txt; grep -n '\\[pdf page' BQT_v4_pages.txt | awk -F: '$1<18064' | tail -2"
}
```


### [2026-09-07T19:32:13.454Z] TOOL RESULT

```
میوه در زبانهای کنونی ارویا به جزء اخیر آن که « پرسیکا > باشد خوانده میشود : 086126
(فر) , ط0626 (انکه) , 8۶1۲81965 (آلم) وجز اینها. « هرهزد نامه مس 4 > ؛هلو 067۳5102
از انواع بادامیها ( 802284816608 ) است که هسته‌های آن ناهموار و پوست میوء آن کرددار
است و جنسهای آن بنام شلیر وانجیری خوانده میشود . « کل کلاب سس ۲۲۹ *.
۴ - ر4 : هلوچین - ۴ -کیلکی 8126018 ( بهمین معنی ). ور : هلو,
8 - مخفف « هلاغل» . ۲ ۰۳ حلهلون , زعرور است» * تحفةٌ حکیم موْمن».
۷ - « هلیانه ‏ شاه ترج است ‎٩.‏ تحفةً حکیم موّمن > .
۸ - هز. 290۳۳8802 ( رد : مشمعا ) پهلوی 81۵6۵1۴ [ 81021 ] خواندء
شده معنیآلوچه. رك: پونکر ص ۱۱۵ ؛ کلم متن مصحف همین لغت پهلوی است .
[pdf page 444]
۱۳۹۱۳ حلیوی
هلیدن ۱ - بکراول وفتح‌دال بروزن | مانندبر که رازیانه دا رجوج
نهیمن. بستی گذاشتن و فروگذاعتن بایر۴ .| باشد - طبیخ‌آلرا و
هده ۲ بخوردسگه بدهند ۳ ی
بش * - بفتح اول بروزن کشیش > | سکه را بکند ی نموم هن
نام مرغی باشد مردارخوار : گویند ءربی‌است. 5 ۳7 ی
هليك ۴ - با سای مجبول بر وزن ۲ هایوی؟ - نود
شريك , بلغت زند و پازند(۱) زردآلو وقیی را | بکسر اول وثانی ۱
کویند ۰ سکون تحتانی ۱ ۷
هلیو . بفتح اول وکسرئانی و سکون مجهول وواومک ور چم لور ام
نحار رده که ما یی.
تحتالی و واو » سبدیرا کوبند که از چوب و لی 9 ۹ ی رال نو و :+
بافند و چیزها درآن کنند؛ وبسکون ثانی‌پروزن کردان بازی را نهر۸ نا
پدرو و بکسر اول پروزن غربو بنظر آمده ره ۰
ات ‎٩‏ . ۹ رس 7 وی
دون بازی گفته‌اند وآن چرخی‌باشد که طفلان
هلیون؟٩‏ بروزن آذیون » گیاهی‌است از چوب و خلاشه سازند و برآب روان گذارند
که آنرا مارچوبه و هارکیا خواند. بر که آن ۱ تا آب آنرا بگرش‌آورد و ایشان تماشا کنند.
(۱) چك: ژد و پاژند ۱
‎٩‏ صهفتن (م.) ؛ ربشةٌ اوستایی 18762 (گذاشتن . رهاکردن » ول کردن):پازند
0 ۵۸11485 ۰ ۵۸1۵4 « اسعق ۱:۹۷ [ رك : هشتن ] بهلوی -اظ ( هشتن ) +
صومازط ۲۸ ( بهلم ) رك : اونوالا ۱۶۵ ؛کردی 0118 (کذاشتن . رهاکردن » اجازه دادن )
« ژابا س ۹-۶۸۸ کلپایگانی 781 - 1ظ (بهل) « قاسمی >.
۴ - درختی که اکنون گرفتست پای بنیروی شخصی درآید زجای
و گر «مچنان رو زگاری حلی بگردوش از بیخ برنگلی.
« کلستان س ۲۱ >
۴ لش (وم.) ۴ - پهلوی 81۵8 ۰ 8106. رك : یولکر س۵۱. قی:هلو
(و.م.) ‏ خلو (ه.م.) وقی: 0811 (آلوچه) در نور وکجور و 13211181۳ (آل و کك) فرنور و کجور
«ثابتی ص ۲۲۰ . 8 - « هلیو , بوزن بدخو: سبد باشد . کذافی‌المژید ؛ و بوزن غربو
یز بنظر رسیده » «سروری» و رك : رشیدی - نیز * هلیوی (ء.م.) « رشيدي *.
‎٩‏ - (ءر) « هلیون ( بکسراول و فتح سوم ). هوبالعربية الیرامع ؛ وبالیوبانية هاسونج,
و بعجمية الانداس‌الاسفاراج , و بقال له ایض سقارج .> « عقار ۱۱۱ ۳2 2806۳86 ( فر) ‏
وناهدن01710 ۸۶027280۶ . نام عمومی‌آن در مصر » سوربه وایران « هلیون » است « عقار
‎٩ ۹‏ «معلیو * عولك (کردکان بازی ) « رشیدی» ۳ حیلوی ۳ هولك (کردکان
بازی ) ۸« جهانگیری > سروری هلیوی , هیلوی وهولك را بمعی « چرخی که از چوب بازند
و پر آب هند و بآن بازي کنند » نوشته است .
[pdf page 445]
بیان چهاردهم
در های هوز با میم هشتمل بر شصت و شش لفت و کنایت

هم < بفتح اول و سکون ثانی » بمعنی همادی ۲ « یفتح اول بروژن جمادی,
دیگر ویکجا و یکدایگروهمه باشد ۱ - وبمعنی | کلی راگویند که همگی و تمامی باشد.
لیزهم هست که بع‌بی ایضاً کوبند۱ - وبا تغدید همادیان ۲ - بروزن غرابیان بممنی
ثانی » در عربی مرادف غم است و آن دلگیری کلیات باشد که در برابر جزئیات است.
وآزردگی بود که سببی نداشته باشد.3# همار ‎٩‏ - بفتح‌اول بروژن بعارءیمعتی

هماد ؟ بفنح اول بروزنجماد.یمعنی | اندازه باشد - و حاب را ای ز گویند که شمردن
همه وجمیع (۱) وکل باشد . چیزی باشد .

)0( چش : جمم.

۱ هرن کوید : 1167 ( همچنین » همانگاه ). بمنزلهٌ پیشوند -12213 ( در شمر
«هام» نیز آمده ). ۵68۰ ( باهم » با ) ۰ قی : بهم 0610612 (باهم )؛ -6122 600-۰ . پارسی
باستان -11210 ؛ اوستا -113770 وغیره؛ بهلوی 32810 , -118172 ؛ هندی باستان -5210 ؛ آر‌نی
۵8۵۲۵۳ ؛ کردی -600 , 126۷۷۰ ؛ استی -31 ۰ 30 . بلوچی 02100 , -11230 ۰ -/8۷ظ۵ ؛
وخی -28 ۰ شغنی 28-۰817 ۰ سربکلی -1720 10-۰ .۰ « اسدق ۱۱*۲ . هوبشآن کوید :
-2۳ ( در تر کیب مانند همایه . همشیره وغیره ) پمعنی هم ( اشتراك را رساند ) ۳ پارسی
باستان -38128 (هم) ( -۳۵380118۳ [هم پدر] ) ۰ اوستا -112۳82 و -132818 .«هوبشمان
7۹ هم در ثرکیبات پیدوند اشتراکست ( افادة اشتراك در آسم مابمد کند) ؛ کردی ع
(یز) , 1361۵ ( هر همه ). ۵150 « ژابا ص *40 ۲ و رك : ژابا ی 42۷ ؛کیلکی 270
(هم) . در نفیرمدبدی معروف بکغف‌الاسرار ( ج۰۱ مصحح علی اصفر حکمت ) «هام» بجای هم
آمده : هام‌دیداری ۳ همدیداری(معا,ته) ( کغف‌الاسرارج۱می۳۳). هام نام هم‌نام (سمی) (ز]
سه). وار ویی‌ورامین «هامواره» بجای همواره‌آمده است (رك : هامواره) +

۴ - برماختة فرقةٌ آذرکیوان . رك : همادی » همادیان .

۴ - برساختهٌ فرفهٌ آذرکیوان . در فرهنگه دساتیر (صس ۲۷۵) آمده : « همادی بفتح
اول » بمعنی کلی‌است که برابر جزئی باشد , بدانکه فرق میان «همه» که بممتی کل و «همادی»
که بمعنی کلی‌است ازچند وجه بود ( درینجا فرق کل وکلی.! بیان کند ).> رك : هماده‌همادیان.

۳ - جمع : همادی (ه.م.) برساختهٌ فرقهٌ آذرکیوان « فرهنگه دسانیر م۵ ۰.۲۷

8 - ارمنی ع 38۳327 ( عدد . پرداخت حاب . تفویم و نخمین ) » از آن است
0 (میشمارم » تخمین میکنم) < پارسی باستان -۵1187۳2 از -112۲8] -0283 6
ی :مر (عدد) . شمار » آمار [ ونیز «امار» ]. سانکریت -5708۲ , وس : 58087 -5880
( بغاطرآوردن . درخاطر واشتن ). 528171872728 ( ذکر » باد ) 53818127888-۰ (شمردن
[دواب] ) ۰ هوبشمان ی ۱*۵ ذبل ۲۱۱۶۱ و ول : هماره +

+ هما «همای (ه.م.) ( برهان قاطع ۳۹۸ )
[pdf page 446]
۳۹۳۳ عماطا
همار|۱ < بروزن صاری, بمعنی‌همواره | همتا و انباز و شريك و رفیق باشد * - و بختح
وهمیشه و دایم باشد ۴ - و درهندی بمعنی مارا | اول و تشدید ثانی‌بروزن عبای, ذرعریی‌شی ردرفده
است بعنی از ماست وتملق بما دارد. راگوند .
هماره * بروزن خراره » بمعنی همار همال ۹ « بفتح ارل بر وژن شمال ء
است که اندازه وشمار وحاب باشد ۴ - ومغفف | بمعنی قربن و همتا وشريك و لباز وشبه وماند.
همواره هم‌هست پمتی همیشه و دایم ۴ . باشد ؛ و بضم اول هم آمده است .8
هماس « بضم اول بروزن قطای,بممنی همانا۲ - بفتح ارل وثالی وتون هردو
‎٩‏ #هماره (وم.) * هنواره (هم.):
۴ -کزیده چهارتوست بدو درجها نهان همارا بآخشیج همارا بکارزلر ۰
,ودکی سمرقندی « لغت فری ص ۰۴۱۹
۴ <فبار (ویم ‎ )‏ اماره (ه.م.) ۴ «هواره (ه.م.) ور : همارا :
مرکب اقبال تو هماره بزین باد پا قدرت فراز چرخ برین باد -
کبال‌الدین اسماعیل « رشیدی» * فرهتکه‌نظلم».
و ر4 : لت فری ص ۵۱۱ - 8 _- «همای , انباز بود» ۵ رشیدی » [ بدون ذکر شاهد]
ظ. مصحف «همال » (ه.م.) ‎٩‏ <هامال (ه.م.) ؛ پهلوی 13281831 ( شخريك » انباز ) "
« نیب رکه ص۹۲ > * اونوالا ۳۰۵»؛ 132۳87021 3 منای‌س ۲۷۹ »؛ کردی 186۲۷81 , ۳80۷2
( رفق , غریك ) «ژاباص 44۷». اسدی کوبد: « همال , همتا و همیاز پمتی لباز بود.پوشکور
( بلخی ) کوید :
دل من پرآزار از آن بدسگال ند دست من چیره بر بدهمال .
آغاجی گوید : ۰
=== pdf page tag before
18009:[pdf page 444]
18046:[pdf page 445]
```


## [2026-09-07T19:32:21.685Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && grep -n 'ناف' BQT_v4_pages.txt | head -40"
}
```


### [2026-09-07T19:32:21.734Z] TOOL RESULT

```
446:مذهبان خورند و عربان ضب خوانند . بموش | و خسیس و منافق را نیز کفته‌اند - وبمعنی‌مردم
482:عربان مسیف‌الغراب ۱ خوانند و بیخ آنرا نافوخ ماخور - بر وزن لاهور . خرابات را
661:هلیون کوبند (۱). دفع‌سموم جانوران کز ندمومار مار دو ز بان «کنایه ازمردم منافق
719:مادمهره - مهرء‌است که بامارمیباشد | کوبند . بغار آن دود سر را نافع است.
873:ماسی ۴ * بروزن عاصی ۰ بی‌پروا وبی | است ‎٩‏ . خوردن آن با عل عرق‌الشارا نافع
1103:رای قرشت و لون بالف کشیده . و پلفت بونانی | خوردن‌آن درطمام ضمف‌چشم را نافع باشد وقوت
1132:2 ماما.- رك : مام ؛ در تهرانی 3387528 (قابله . مام‌ناف) » در افغانی 112132 (دائی,
1136:۵ مام لاف - قابله « رشیدی > و مخقف آن ماناف (ه.م.)
1143:نافع است و آنرا بعربی بقلةالخطاطیف و شجرة | هم هست بعنی بگذار و باش و بمان ۴ - و شبه
1178:کویندو جرمی قابله خوانند - و بمعنی ناف‌هم باطل‌السحر است, هر که باخود دارد سحر پروی
1192:۴ - مخفف « مام ناف » همین معنی « رشیدی > + - از : مان ( ماندن )
1512:ماهار ۴ - بروزن ناهار , بممنی مپار | وضمادش بواسیر را نافع است .
2070:محموده ۱ - بر وزن فرموده . نام | کزندکی عقرب را نافع باشد .
2155:.و غیر ذی حیات ۲ . کردن - و چسبیدن - و نافرمانی کردن و عاق
2589:مرداسنگ ۱ « یم اول » بمعنی | خوردن آن با شراب کزندکی جانوراترا نافع
2791:وکارزا رکردن مرد باشد درنهایت شدت - وبکسر دل را نافع باشد .
2948:خوانند ۴ . منافع او بسیار است اگر بال او را وبمعنی کبوترنامه‌بر هم آهده است ! وبدو معنی
3207:مار وعقرب را نافع است . و نون مفتوح بکاف زده . نام دوائی است که
3472:۴ - مژدگانی بده ای خلوتی‌نافه گشای1 که زسحرای ختن آهوی مشکین‌آمد.
3536:کله و شکوه و شکایت باشد ۴ - و بیخ کیاهی | برص وبهق طلاکنندنافع باشد. وبا عل‌پربشهای
3735:دوائی‌است که بربهق وبرص طلاکنند نافع باشد. | نراشند ۸ - ويك مشت ازهرچیز رالیز کفته‌اند؛
3826:است . کوبند ناف ۹ وبکس اول هم‌آمده است .
4158:وا مقل ۰ < بنت اول بروزن مقل «بستی نکندء ودرد یت را نیز نافع‌است وهمچنین درد
4280:2 شم اول وف زند. پواسیررا نافع است - وهفت تخمة‌بز
4281:مقرنس ۴ -بنم اول وفتح ثانی ویون | سازند. بواسیررا نافع است - وهفت تخمهٌپزوری
4587:ی | میچسباند - وکنایه از مردم منافق وزراق وغدار
5390:نقری و ورمهای گرم را نافع است - کوبندجانوری وس ار ۳
6100:بخورد مصروع دهند نافع بود .
6595:لم قبه ایست از منافات غزلین -وولایتی است | باشد -
6858:۴ - رك : ناف . ۴ - از : نا (نفی , سلب )4 خاست (از خاستن) بمعنی خیز
7287:پایة سقف داررا کویند ؛ و بعشی پوشش‌سرنردبان ناف برغم ددن -آن‌است که‌ماماچه
7288:راکفته اند که بربام خانه سازند تا برف و باران اگربوقت پریدن ناف طنل غمگین وبیدماغ باشد
7290:ناغهست ۱ - با غین نقطه‌دار و تحتانی | « ناف او را بغم زده‌اند » و یا درساعت بد پريده
7292:تغمی باشد سرخ رنگه . معده و جگر سرد را ناف خالگ * - بیستی ناف ار است
7293:نافم بود . که کنایه از مکهٌ معظمه باشد .
7300:ناف ارض - کنایه از مکهٌ معظمه بنظرآمده است ۷ .
7302:ناف برخوشی‌زدن - آست که ناف ددن « بروزن لاف زدن , بسسنی
7303:اگر ماماچه در وقت بریدن ناف طفل بوزایید, | لاف بریدن باشد ۸ ۰
7304:خوشحال باشد وبخوشحالی بیرد آن طفل پبوسته ناف مین * - پمنی ناف خاك است
7305:خوشوقت بوده بخوشحالی بگذراند , کوبند «ناف |. که کنایه از که معظمه باشد .
```


## [2026-09-07T19:32:27.478Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && awk 'NR>=7280 && NR<=7360' BQT_v4_pages.txt; echo \"=== pdf tags\"; grep -n '\\[pdf page' BQT_v4_pages.txt | awk -F: '$1<7290' | tail -2; grep -n '\\[pdf page' BQT_v4_pages.txt | awk -F: '$1>7290' | head -2"
}
```


### [2026-09-07T19:32:28.816Z] TOOL RESULT

```
*- ۶ ناغوش » حربآب فروبردن بود از مردم » ومرغ را نی زکوبند . لبیب ی کوید :
کرد گرداب مکرد ارت نیاموخت‌شنا که‌شوی غرقه چو ناگاهی داغوش‌خوری.»
« لت فرس می ۳۲۷۰
[pdf page 183]
اغول ۱۰۳
وغوطه خوردن را نی ز کوبند . او را به خوشی زهه‌اند » وهمچنین اگردرساعت
فاغول - بروزن شاغول » بردبان وزینه | يك بریده باغن. ٍ
پایة سقف داررا کویند ؛ و بعشی پوشش‌سرنردبان ناف برغم ددن -آن‌است که‌ماماچه
راکفته اند که بربام خانه سازند تا برف و باران اگربوقت پریدن ناف طنل غمگین وبیدماغ باشد
بهایین نیاید . آن کود که همیشه غمگین خواهد بود . کوبند
ناغهست ۱ - با غین نقطه‌دار و تحتانی | « ناف او را بغم زده‌اند » و یا درساعت بد پريده
وسین بی‌نقطه وفوقانی » بمعتی لارمشغك است که | باشند ۴ .
تغمی باشد سرخ رنگه . معده و جگر سرد را ناف خالگ * - بیستی ناف ار است
نافم بود . که کنایه از مکهٌ معظمه باشد .
اف ۴ - بروزن‌کاف . معروف است که نا هخته ۱ :
7 0 ارهخته ۱ -» با فای مفتوح » هردم
سوراع وسط شکم باشد - ووسط ومهان هرچیز ادب و زشت روی باشد چه فرهخته بمعنی‌ادب
۰ اب رس ۰ ۹
ات را وا تقو
:۵۱ ۳ ۰ است - ویممی‌بی‌ادبی - ورشت روی
ناف ارض - کنایه از مکهٌ معظمه بنظرآمده است ۷ .
است ۴ . ۳ و
ناف برخوشی‌زدن - آست که ناف ددن « بروزن لاف زدن , بسسنی
اگر ماماچه در وقت بریدن ناف طفل بوزایید, | لاف بریدن باشد ۸ ۰
خوشحال باشد وبخوشحالی بیرد آن طفل پبوسته ناف مین * - پمنی ناف خاك است
خوشوقت بوده بخوشحالی بگذراند , کوبند «ناف |. که کنایه از که معظمه باشد .
۱ - فارسی است ومعرب‌آن دز « ناغیست > ۳ بارمشك « دزی اج ص ۹۳۷ 4.
؟ - اوستا -22]2 ۸« بارتولمه ۱*۹۲ سانسکریت 220171 ۰ نزديك - 82۳008
(بان , خانواده) « لیب ر که ص ۱۵۳ , پپلوی 22 (ناف) , اففانی80 ۰ 32018 ۰ استی ]۰32
بلوچی 23038 . 54۳28 ۰ 23880 . رک : اسشق ۱۶۲۰ ۰ کردی 82۷۷ ( ناف » درون ) »
۷ ( کفل ) « ژابا ی 2۱۵ > نیز در اوستا -8802 (ناف) ۰- 38821 ۰ 320137 ۰ پارسی
باستان و ساسکریت - 884021 . لاتینی ۰6008 آلمانی 3872061 , انگلیی22۷61 . فارسی:
لاف , تافه » نواده » نبیر » نبیره « بشتها ۲ ص ‎0٩‏ ح > ؛ قن : نواده , نیین » لبیره .
توان بحلق فروبردن استخوان درغت (درست) ولی شکم بدرد چون بگیرد اندر ناق.
« کلتان ص 4۳ >.
۴ ناف زمین ۳ ناف خاك < ناف عالم. قدما برآن بودند که‌مکه درم رکز زمین «اقع
است . پا آنگه ملمانان همه نواحی زمین بهنگام نماز روی بدانکنند -
۴ - ناف توبرغم زدند , غم‌خورخافانیا ۱ کانکه جهان‌را شناخت غمکده شد جان او.
خاقانی شروالی ص ۶۳۷۳ ۰
- ناف ار ۳ ناف زمین ۳ ناف عالم . ‎٩‏ از: ۷ (نفی » ملب ) +
فرهخته (ه.م.) ۷ - بدو معنی اخیر ۰« فرهختگی > صحیح است .
۸ - پوصفش خرد بست لقش ضمیرم بندخش زد اندیشه ناف زباام .
طالب آملی « بهار عمجم >.
۰ باق آرش ۳ یاف خا که ۳ ناف عالم ۰
[pdf page 184]
یه باقور
ناف شب -کنایه ازسف شب است ۱ | و بتختابی زده » کنایه ا زکنده دهان است بمنی
چه ناف بممنی وسط ومیان هم آمده است. شخصی که دهان اوبو ی کند - وسُخن چین وسام
ناف عالم ۴ - پستی‌باف زمین است | راهم میگوبند ‏
که کنایه از مکةٌ معظمه باشد . ناف هفته - کنایه از روز سه شنبه
نافوخ ۴ - با فای بوا و کشید. وبغای | است که (۱) دروسط هفته واقع است ‎٩‏ +
نقطه‌دارزده , پاغت امل‌بقداد پیخ سوسن‌سحرائی ناه هش یافتن - کنایه از بلنه
است و زنان بجهت فربهی کار برند .3 ۳ دک ام 1 ایه از ی
تاقة آق « بسی نانه آهوی یی ۱ آدازگی ولیکنامی و شهرت بافتن ونام تيك بهم
است چه‌آف بممنی آهوی مغك باشد ۴ رسانیدن باشد .
ست چه اس دممتی آعوی وه نا فا ره ۲
ناف آهی «» معرون است* -وکنایه ار ود < با اف بر وزن شایود؛ بسنی
از موی خوشبوی باشد که زلف و کا کل معشوق ام بردار اآمت ۷ یمنی آنچه از آن درجاها باز
است . . کوبند - و بای بز رکه را هم کفته‌اند که کرنای
ناقه بوی - با بای ابجد بواو کشیده | باشد ۸ - و درعریی صوراسرافیل را خوانشد ۸ .
() خم۱ : چه .
۱ لاف شب از مغك فروشان اوست .. ماء لو از حلقه بگوشان اوست .
نظامی کنجوی ۶ کنجینه ص ۰۱۵۲
۲ * ناف ارش » باق خا که * ناف زمین :
قدم بر اسر ناف عالم لهاد با نافه‌کز ناف عالم کشاد .
نظامی کنجوی * گنجیته س ۱۹۲ ۰

۴ - تافوخ » در بغداد . ربعةٌ 812101 (ض) ( بیخ «لبوث « تحفةٌ حکیم موّمن >) را
کوبند . اين البیظار (1» 8۲۶ 8) : اصله پسمی النافوخ بالنون ببغداد وتتممله الشاء کثیراً
بیقداد للمن و فی‌غمرالوجه لنحین اللون و هو عندهم (8 ۳ ببوادیها ) کئیی یباع مته المن
پااً بثلة دراهم ( اپن‌البیظار ]1 ۰ 0۸۹ 4 ) . رك : دزی ج ۲ ص ۹۹۵ :۲+

۴ رد4 : آف . 8ب رك : نافه .

- ‏از دکر روز هفته آن به بود ناف هفته مگر سه خنبه بود‎ - ٩

نظامی کنجوی « هفت پبکر . چاپ آرمفان س ۶۲۱۶ ۰

۷ -اظ . مصحف « نامور» (۸.م.) ۸ - (صر) « ناقور » شاخ دمیذل ی که صور
باشد . مته قوله تعالی: واذا اش فی‌الناقور » ای فی‌الصور .» « منتهی‌الارب > +

=== pdf tags
7245:[pdf page 182]
7283:[pdf page 183]
7324:[pdf page 184]
7371:[pdf page 185]
```


## [2026-09-07T19:32:47.274Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && awk '/\\[pdf page 17[5-9]\\]|\\[pdf page 18[0-6]\\]/{p=1;print \"----\"$0;getline;print;getline;print;p=0}' BQT_v4_pages.txt"
}
```


### [2026-09-07T19:32:48.503Z] TOOL RESULT

```
----[pdf page 175]
نلداغتی -۹۲-
مفلی وپربشان وبینوا هم هست ۱ - و مردم بی | باشد معروف ‎٩‏ - وبعریی‌آتش راکویند .
----[pdf page 176]
سس خی ناردین
نار پستان ۱ » بسکون ناك , دختری | وشیش وکنه را هم کفته‌اند ۷ - و بزبان هندی
----[pdf page 177]
نارریاب - ۷۹8
سنبل رومیراکوبند ۱ وآن زرد رنگه میباشد. | شیرین بود -اونام نوایی است از موسیقی.
----[pdf page 178]
وه مس بارنکه
رمادپالبال خوانند. 38 بعریی رمان مصری خوانند وخاسیت آن نزديك
----[pdf page 179]
طردگی خمدها

----[pdf page 180]
اما نها نازیری
ماشد جل وپلیل9 - و زبالةٌ ترازورا نیز کویند؛ | باشد - وبلفت هندی زیر کوبن د که درمقابل‌مرد
----[pdf page 181]
بازد مها
نازگ ۱ - بنم ثاك و سکون کاف . گفته‌اند که بعربی سنور خوانند .3۴
----[pdf page 182]
- ۹۹ داغوش
اسر اپش ۱ - زبان حال را گویند | باشتا و باهار اک که ازسباح باز چیزی نخوردن
----[pdf page 183]
اغول ۱۰۳
وغوطه خوردن را نی ز کوبند . او را به خوشی زهه‌اند » وهمچنین اگردرساعت
----[pdf page 184]
یه باقور
ناف شب -کنایه ازسف شب است ۱ | و بتختابی زده » کنایه ا زکنده دهان است بمنی
----[pdf page 185]
مالزمی ی -۹۱۱۹.
ناقوسی - بر وزن طاوسی » نام نوایی | خصوصاً ۴ - و نوعی از امرود هم هست که ازآن
----[pdf page 186]
۳ باگولرد
کنته شد ۱ که در فارسی جیم و ها بهم تبدیل نا گزدان * « با زیادتی الف و نون »
```


## [2026-09-07T19:32:57.931Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && grep -n 'نافه' BQT_v4_pages.txt | sed -n '1,30p'"
}
```


### [2026-09-07T19:32:57.981Z] TOOL RESULT

```
3472:۴ - مژدگانی بده ای خلوتی‌نافه گشای1 که زسحرای ختن آهوی مشکین‌آمد.
7344:قدم بر اسر ناف عالم لهاد با نافه‌کز ناف عالم کشاد .
7352:۴ رد4 : آف . 8ب رك : نافه .
7366:کرش آلسکه ) ثر قرار دارد و درآن معك (ه.م.) وجود دارد ( بهمین مناسبت آنرا « نافه »
12559:نیفه امالةٌ « تافه » ات و نافه آنچه سبت بناف دارد و نافةٌ مغك را از ین جهت نافه کوبند .
20494:هم آمده است؟ وبعربی‌تمنی کوبند ‏ باقه؟۴ « بنتح ثالك بروزن نافه. کمشده
20546:۱ - نافهراکیمخت رنگین‌سرزشها کرد و گفت:
```


## [2026-09-07T19:33:01.072Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && awk 'NR>=7355 && NR<=7372' BQT_v4_pages.txt"
}
```


### [2026-09-07T19:33:02.243Z] TOOL RESULT

```
نظامی کنجوی « هفت پبکر . چاپ آرمفان س ۶۲۱۶ ۰

۷ -اظ . مصحف « نامور» (۸.م.) ۸ - (صر) « ناقور » شاخ دمیذل ی که صور
باشد . مته قوله تعالی: واذا اش فی‌الناقور » ای فی‌الصور .» « منتهی‌الارب > +

2 لافه - بفتح فاء (درلهجةٌ کنونی بکسر). پهلوی 0218 ( ناف ‎ )‏ بلوجی ۰22028
68 ۲و2 ( اس ) « اسعق ۱۶۲۰ :کردی 220۵1 ( ناف ) , ارمنی 38081 (کيه
معك ) » افنانی ع 24۳2 ( کي مشغك ) « هوبشمان ۱۶۲۰ »۰ ایضاً کردی 386 ( باف ) »
غاد , 22۶6۵ , 22۷6 ,زد , 2206 , لری 820016 «ژاباسی ۶۱۵ [ رك :
ناف ] :کیسه ای مشکین باندازه تخم مرغی که در زیر پوست شکم آهوی ختا ( 166۶ 132186
کرش آلسکه ) ثر قرار دارد و درآن معك (ه.م.) وجود دارد ( بهمین مناسبت آنرا « نافه »

ند).
بی ناقهٌ مشکه و دیبای لغز کزایشان فروده شود هوش ومغز.
نظامی کنجوی « کنجینه ی ۰۲۱۵۳
[pdf page 185]
مالزمی ی -۹۱۱۹.
```


## [2026-09-07T19:33:12.795Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN nave/navel/auger\"; grep -n '^nave,\\|^nave¹\\|^navel,\\|^auger,' KLN_1966.txt | head; echo; grep -n -A2 'nave,  n\\.,  the  hub\\|navel,  n\\.\\|auger,  n\\.' KLN_1966.txt | head -20"
}
```


### [2026-09-07T19:33:12.866Z] TOOL RESULT

```
=== KLN nave/navel/auger
25058:navel,  n.  —  ME.,  fr.  OE.  nafela,  rel.  to  ON.  nafli, Dan.,  Swed.  navle,  OFris.  navla,  MDu.  navel, navele,  Du.  navel,  OHG.  nabalo,  MHG.,  G. nabel,  fr.  I.-E.  base  *ombh-,  ndbh-,  *mbh-, whence  also  OI.  ndbhyam,  ‘nave  (hub)’,  nabhih, ‘navel,  nave,  relationship',  nabhilam,  ‘umbilical depression',  Avestic  naba-nazdishta,  ‘next  of kin’,  Avestic  nafa,  ModPers.  ndf,  Gk.  ofipaXo?, ‘navel;  boss  of  a  shield,  knob’,  L.  umbilicus, ‘navel;  umbilical  cord’,  umbo,  ‘boss  of  a  shield’, OPruss.  nabis,  ‘nave,  navel’,  Lett,  naba,  ‘navel’, OIr.  imbliu  (gen.  imblenri),  Mir.  imlecan,  ‘na¬

3951:mythol .)  —  Formed  with  suff.  -an  fr.  L.  Augeas, fr.  Gk.  AuyEia?,  ‘Augeas’. augelite,  n.,  a  hydrous  aluminum  phosphate  (min¬ eral.)  —  Lit.  ‘the  bright  stone’,  formed  with combining  form  -lite  fr.  Gk.  auyif),  ‘light  of  the sun,  brightness’.  See  augite. auger,  n.  —  ME.  auger,  earlier  nauger,  fr.  OE. nafugar,  which  is  compounded  of  nafu,  ‘nave  of a  wheel’  and  gar,  ‘spear’;  see  nave  and  gore,  ‘a triangular  piece  of  land’.  The  loss  of  the  initial n  is  due  to  a  misdivision  of  ME.  a  nauger  into an  auger.  For  similar  misdivisions  cp.  adder  and words  there  referred  to.
3952-Derivative:  auger-er,  n.
3953-aught,  n.  —  ME.  auht,  fr.  OE.  awiht,  dwiht,  lit. ‘ever  a  whit’,  fr.  a,  6,  ‘ever,  always’,  and  wiht, ‘creature,  thing’.  See  aye,  ‘ever’,  and  wight  and cp.  naught.
--
25057:navarch,  n.,  commander  of  a  fleet  (Ancient  Greek history).  —  L.  navarehus ,  more  correctly  nauar- chus,  fr.  Gk.  vauapyo?,  ‘the  master  of  a  vessel’, which  is  compounded  of  vau?,  ‘ship’,  and apy<k,  ‘leader,  chief,  ruler’.  See  naval  and  -arch, nave,  n.,  the  central  part  of  a  church.  —  L.  navis, ‘ship’.  See  naval  and  cp.  nef. nave,  n.,  the  hub  of  a  wheel.  —  ME.,  fr.  OE.  nafu, rel.  to  OS.  naba,  ON.  ndf. ,  Dan.  and  Swed.  nav, MLG.,  MDu.  nave,  Du.  naaf,  OHG.  naba, MHG.,  G.  nabe,  ‘nave’,  and  to  OE.  nafeta,  etc., ‘navel’,  and  cogn.  with  OI.  ndbhyam,  OPruss. nabis,  ‘nave’.  The  nave  of  the  wheel  was  com¬ pared  to  the  navel  of  the  body.  See  next  word and  cp.  words  there  referred  to.  Cp.  also  auger. For  sense  development  cp.  OI.  nabhih,  OPruss. nabis,  ‘nave,  navel’.
25058:navel,  n.  —  ME.,  fr.  OE.  nafela,  rel.  to  ON.  nafli, Dan.,  Swed.  navle,  OFris.  navla,  MDu.  navel, navele,  Du.  navel,  OHG.  nabalo,  MHG.,  G. nabel,  fr.  I.-E.  base  *ombh-,  ndbh-,  *mbh-, whence  also  OI.  ndbhyam,  ‘nave  (hub)’,  nabhih, ‘navel,  nave,  relationship',  nabhilam,  ‘umbilical depression',  Avestic  naba-nazdishta,  ‘next  of kin’,  Avestic  nafa,  ModPers.  ndf,  Gk.  ofipaXo?, ‘navel;  boss  of  a  shield,  knob’,  L.  umbilicus, ‘navel;  umbilical  cord’,  umbo,  ‘boss  of  a  shield’, OPruss.  nabis,  ‘nave,  navel’,  Lett,  naba,  ‘navel’, OIr.  imbliu  (gen.  imblenri),  Mir.  imlecan,  ‘na¬
25059-1033
25060-vel’.  Cp.  nave,  'hub  of  a  wheel’.  Cp.  also  om- phalo-,  omphalos,  umbilicus,  umbo,  nombril. navew,  n.,  1)  the  wild  turnip;  2)  the  rape  (rare)  — F.  naveau,  fr.  OF.  navel,  fr.  VL.  *napellus,  dim. of  napus,  ‘a  kind  of  turnip’,  fr.  Gk.  vami,  ‘mus¬ tard’,  which  is  prob.  of  Egyptian  origin.  (For the  sense  development  of  L.  napus  from  Gk. va7tu  it  should  be  borne  in  mind  that  the  mus¬ tard  plant  and  the  turnip  resemble  each  other  in form.)  Cp.  neep  and  sinapism,  the  first  element in  napiform  and  the  second  element  in  parsnip and  in  turnip.
```


## [2026-09-07T19:33:14.439Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HUB\"; grep -n 'nāfa\\|näfa\\|Nabel' HUB.txt | head -10; echo \"=== SYN navel\"; grep -n -i 'navel' SYN.txt | head -10; echo \"=== IEC\"; grep -n 'nobh\\|nābhi\\|nabō' IEC.txt | head -10"
}
```


### [2026-09-07T19:33:14.563Z] TOOL RESULT

```
=== HUB
1661:naftafig *Mitte des Leibes' (beim Pferd, eigentl. *Nabel-
3546:1020. Dazu kurd. noheh 'Nabel' (Socin , kurd. Samml. II, 339),
3548:Soukry p. 44, 7 v. u.) = np. ndfa 'Nabel, Moschus-
6509:naf, nafa 'Nabel', phi. nafak, bal. napag, nb. nafay,
6510:zd. na/d 'Nabel' ZPGl. p. 10, 'Geschlecht' yt. 13, 87 (=
6511:arisch "^naphas-) neben zd. nabanazdista-, skr. nabhi- *Nabel
=== SYN navel
3740:Av. nafa- ‘navel’ and ‘family, kin- dred’: Skt. nabhi- ‘navel’ and ‘relation- ship’, Grk. du¢ands ‘navel’, etc. Walde- P. 1.130. Barth. 1062.
5201:NAvEL
6448:P. 2.80. Stokes 54. 351. 4.43 NAVEL Grk budards Goth. Lith. bamba NG adadéds ON naflt Lett. mnaba Lat. umbilicus Dan. navle ChSl.  papiikit, papit It. bellico Sw. navle SCr. pupak Ir. nombril OE nafola Boh. pupek Sp. ombligo ME _navele Pol. pepek Rum. buric NE + navel Russ. pupok Ir. ambliu, imlecan Du. navel Skt. nabhi- Nir.  imleacan OHG  nabalo Av. nafa- W. bogail MHG nabel(e) Br. begel NHG nabel Most of the words for ‘navel’ belong | cela ‘little buckle’? So Henry 29,
23158:Lett. bamba, also bumba (but the lat- ter rather ‘ball, bomb’, etc.?), cf. Lith. bamba ‘navel’, bumbulis ‘bubble’, bum- buras ‘bud’, Pol. babel ‘bubble, blister’, Boh. boubel ‘bubble’, Skt. bimba- ‘sphere, orb, disc, rounded part of the body’, etc., all prob. based on a syllable imitative of the sound made with puffed- up cheeks. Walde-P. 2.107f. Miuhl.- Endz, 1.261.
=== IEC
5758:$nobos (?nobil-, gnob-) (?) ‘knot, knob’. Cf. $nubh- (gnubh-). WP I, 581 Ir. (ambig.) gnobh ‘knot in wood’; OE cnapp, ON knappr, Sw. knapp, m. "button, knob, boss’. (Finn. nappula ‘peg’ seems to derive from a Gmc. form represented in OHG kne- bil ‘gag’)
11784:nobh- ‘nave, navel, hub, centre’. WP I, 130 Skt. nábhyam, n. id.; Av. nabis, f. ‘navel’; Per. naf ‘navel, middle; Oss. Dig. naffä ‘navel; OHG naba, f. “hub, nave’; OE nafu, d. ON nof, f. id. OHG cf. nabalo, wm. ‘navel’; OE nafela, wm. id. beside nafeóa, wm. ‘thub’; Latv. LW naba ‘nave’; Finn. LW napa ‘navel, hub’. (Latv. naba also = ‘navel; axle- tree, crossbar of plow’)
11785:nobhesos (nebhos, -es-?) ‘centre-bit of drill (9). Cf. nobh- above ON nafarr, ds: nafri, m. *gimlet'; Cz. nebozez, id.
```


## [2026-09-07T19:33:25.197Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>25400 && NR<25500 && /^10[0-9][0-9]$/{print NR\": \"$0}' KLN_1966.txt; echo \"=== around natron\"; awk 'NR>24980 && NR<25070 && /^10[0-9][0-9]$/{print NR\": \"$0}' KLN_1966.txt"
}
```


### [2026-09-07T19:33:26.574Z] TOOL RESULT

```
=== around natron
25059: 1033
```


## [2026-09-07T19:33:26.692Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\nimport re\nleaves=t.split('\\f')\nfor i,l in enumerate(leaves):\n    if 'ombh' in l and ('nobh' in l or 'Nabel' in l):\n        print('LEAF',i)\n        print(l[:2500]);print('======')\nEOF"
}
```


### [2026-09-07T19:33:27.967Z] TOOL RESULT

```
LEAF 138
130                enedh-, endh-               — (enebh-) ombh-, nObh- (nebh-?), mbh
                                                               a
enedh-, eudh- „gehn, liervorkommen                                 .




  gr. av-yvo dev, ev-yvo&e „kommt (kam) hervor,                                      steigt        empor, sprudelt
empor“ (at/ua, y.vlaij; Horn.) ensv-rjvo'de {fkayyrj eigentlich „hervorgekommen
sein“ = „sich worauf befinden“; e laiov „sich worfiber verbreiten“ Horn.),
ep. y.aTev-tjvode        (   y.ovig , xo/nat, ,.herabfluten“),                  nagev-yvode („sich nahern“)
vielleicht    dor.-kret.-arkad.                      fjvOov,   ptc.      ev&cbv,    „kam‘ (att. lldelv wohl
                                                                                               :




daraus durch Kreuzung mit ij/.v()or von elev&co, wahrend Schulze Festschr.
f. Jagie 343   Anm. L [Zitat nach Jacobsohn KZ. 43, 170] el&eTv aus ek-dveTv
durch lautliche Aufsaugung des v durchs dunkle 2 erklaren will; fiber
andere Auffassungen von h’fttiv s. Prellwitz BB. 23, 75, Boisacq 242, Brug-
mann-Thumb GrGr. 4 95, 344 nicht iiberzeugend fiber avrjvode Prellwitz 2 40);
                                                 ;



   pali andhati ,.geht“; mit Tiefstufe *ndh- wahrscheinlich hierher ai adhvan-                            .



m. = av. advent- m. „Weg, Pfad, Bahn“, wozu vielleicht              mit r- neben                   —
M-Suffix     —
             ai. adhvard-h „religiose Handlung, lieiliger Dienst“ (ursprgl. „Gang

— feierlicher Gang — Feier“, vgl. dt. „begebn“ von gottesdienstlichen Feiern)
     qnchtrr m. „eine Art Schneeschuh“ (* ndhuro - mit Suffixablaut gegen-
     isl.

fiberadhvava- aus *ndhueru-; nicht wahrscheinlicher dachte Falk-Torp 5f.
an Bezieliung zu germ, mid „entgegen“ als „was entgegengesetzt wird,
was den StoB auffangen soll“) Johansson IF. 3, 203 ff. und S, IS Iff.

1.    (euebli-)    ombh-, nobli- (nebh-?), mbh- „Nabel                                -
                                                                                          ‘,   mehrfach mit Z-For-
        mantien.
      As. ndbliya- n. „Nabe“, nabhi- f. „Nabel, Nabe, Yerwandtschaft“, nablnla- n.
funbelegt)  ,,Schamgegend, Nabelvertiefung“ av. uabd-nazdista- „der ver-    ;



wandtschaftlich naehststehende“,  daneben mit ar. ph av. nufa-, np. naf
„Nabel“; gr. o/uipcdog „Nabel, Schildbuckel“, wohl auch opcpay.e? „die un-
reifen Weinbeeren oder Oliven oder andere 
======
LEAF 582
                                    ;                                                                                              ;




574                                                                              gem;e)-


begriff ..tabulatum ', vgl. auchmnd. nnd. kimme {mm aus mb) „Zarge, am
                                                 --




Fasse das iiberstehende Ende der Dauben vom Boden an, am Schiff der
auBere Rand, wo der Boden aufhort und die Seiten sicb zu erheben an-
fangen; Horizont" (kaum als „Umfassung“ zu unserem gem-bh -), mndl.
kimme mengl. chimbe scbwed. mdartl. kimb(e) auch „Daube“ (Falk-Torp
                ,                                            ,


509 verweist auf anord. Jcambr „Kamm, gezackter Rand' und lit. sambas                                                    -'




..Balkenkante". die aber zu idg. gembh-, gombhos „beifien, Zahn“ gehoren);
ferner weisen wohl auf „Block (als Fessel)“, nicht auf „Fessel schlecht-
      --
hin   auch (s. Zupitza Cfutt. 147, Berneker 327) ahd. kembil „columbar
(Fesselblock)",   hump „compes“, gakampit „compeditus“, nhd. mdartl.
Kamp e), Kamme ,.Holzer, die Tieren um den Hals gelegt werden, damit
sie nicht die Ziiune durchbrechen“; dazu auch anord. Icumbr, trekumbr
,,Holzklotz“, mit p mhd. nhd. kumpf „gestutzt, stumpf       (also nicht aus
                                                                                                                     -
                                                                                                                         *



...zusammengedriickt"), engl. chump „kurzes unformliches Stiick, Holzklotz"
(unwahrscheinlich dagegen ist mir, daB auch norw. hump „KloB“, kamp
„knollig rand'* ihre Bed. aus „Baumstumpf, Stumpfchen iiberhaupt" ent-
wickelt haben sollten). —
  DaB                in       mhd. kumber                        ,
                                                                     nhd.   hammer            (roman,,   s.   Kluge 8 267) auch ein
echt germ. Komponent stecke, wird durch norw. mdartl. kumra seg „seufzen,
stohnen             -'*
                              —
            trotz der Bed.-Beruhrung mit lat. gemere   nicht erwiesen.                                         —                   —
   AuBerhalb des Germ, fehlen Spuren der Labialerweiterung: gr. yopcpog
                    '


„Pflock             - -

           lit. gembe  „Hagel zum Aufhiingen“ ist (trotz Persson Beitr. 81
                       
======
LEAF 583
                                   gembh-, gmbh-, gombhos                                                      575

(*ge»w-tos; -nt- gegeniiber bewahrtem nit im schleifenden simtas „hundert"),
aksl. zetb   „Schwiegersohn, Schwager, Schwiegervater".                             Siehe aber        S.   577!
  Daneben aknliche Ableitungen von *gen- „gignere“                   :   lett. sniidts „Schwieger-

sohn, Schwager" (Bed. nach einer Entsprechung von                            lit.   Icntasf),       ai. jndti-h

„Yerwandter“, gr. yvcoro „Yerwandter, Bruder", got. hnops „Gescklecht“,
wie andrerseits lit. gent'is „Yerwandter“ mit <j nach gimti (s. unter (Jicm-
„kommen“).
  Ygl. Curtius 546 f., Aanicek Lat. EWb. 2 78, und bes. Delbriick Yerwandt-
schaftsnamen 536, v. Bradke aaO., Schrader IF. 17, 11 ff., Yf. LEWb. 2 337 f.,
Brugmann Grdr. II 2 1, 335; abweichend friiher ders. I 2 405, Johansson
BB. 18, 39. Ablaut genid- (Dehnstufe gem- im Ar., kaum erst durch Ein-
mischung eines jci- von gen-), geme-, genid L    Beziehung zu *gem- zusam-
                                                        .



menpressen (paaren) ist trotz des g unserer Wz. denkbar, wenn dieses durch
friihe Anlehnung an gen- „gignere" (s. die obigen Beriihrungen) an Stelle
von g eingedrungen ist. Gegen die auch lautlich bedenkliche Auffassung
unserer gein-FovvnQn als *gen- -f- »»-Suffix spricht auch von seiten der Bed,,
daB eine Bezeichnung des Schwiegersohns als „Geschlechtsangehorigen oder
Zeugers" nur von einem Mutterrecht aus einwandfrei ware.


gemhli-,     gmbh- „beifien, zerbeiBen", gombhos ,,Zahn".
   Ai. jambliate,      tiefstufig jdbhatc       „schnappt", Ivaus.-Iter. jambhdyati                        ,   zer-
nialmt",     av.   zsmbayaclwom „ihr zermalmt",             alb.   bemp „es schmerzt mich“
(Pedersen KZ. 36, 334), aksl. zcba_, zqbsti „zerreifien“, arm. (nach Bugge
KZ. 32, 11, Pedersen KZ. 39, 361) vielleicht cxmem „kaue“, cameli „Kinn-
lade, Wange, Mund“ (- emb iiber -omb-, -sm- zu -am- ?)
   ai. jamblia-h  „Zahn, pi. GebiB" 'janibhya-k ,,Schneide- oder Backenzalm"),
                                            (



gr.   yogupog  palin' (auch „Pflock usw.“, siehe Anm.) ; yopcpiog scil. obovg
„Backenzahn‘, alb. hemp, bestimmt bembi, geg. bajn(p), best, bqmbi ,.Zahn“
(G. Meyer Alb. Wb. 83), aksl. zqbb „Zahn“, lett. sitobs „Zakn“, lit. lambas
„Balkenkante („scharf gezahnt oder gleichsam beiBend ')
                   ‘



   alid. leanib, ags. comb ,,Kamm ‘ („gezahnt“), ano
======
```


## [2026-09-07T19:33:34.864Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>25350 && NR<25560 && /^ *10[0-9][0-9] *$/{print NR\": [\"$0\"]\"}' KLN_1966.txt"
}
```


### [2026-09-07T19:33:36.036Z] TOOL RESULT

```
25394: [1046]
```


## [2026-09-07T19:33:40.080Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>25390 && NR<25700 && /^ *1[0-9][0-9][0-9] *$/{print NR\": [\"$0\"]\"}' KLN_1966.txt"
}
```


### [2026-09-07T19:33:41.295Z] TOOL RESULT

```
25394: [1046]
25568: [1054]
25634: [1056]
25635: [1057]
25668: [1058]
25669: [1059]
```


## [2026-09-07T19:33:53.662Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SNS\"; grep -n 'nāf\\|näf\\|nābh\\|nabh' SNS_pages.txt SNS.txt 2>/dev/null | head -10; echo \"=== SOD sogdian\"; grep -n 'nāf\\|ناف' SOD.txt 2>/dev/null | head -5; echo \"=== NYB naf\"; grep -n 'nāfak\\|nafak\\|nāf ' NYB_vol2_glossary.txt | head -10"
}
```


### [2026-09-07T19:33:53.743Z] TOOL RESULT

```
=== SNS
SNS.txt:14504:^i^^Unabh-r^^^^af-: ^^V nafah- : fc. 
SNS.txt:15679:nambh-, nabh- 
SNS.txt:28545:nambh-nabh- 282/3 
SNS_pages.txt:10244:                                               I, 38)  .*!,                                       ^i^^Unabh-r^^^^af-: ^^V nafah-                                                              :       fc.
SNS_pages.txt:11258:invinahtar:                        .^Irf-.vinShtarsV^-*                             nabh-         CHSf^Shah tj\ napta-
SNS_pages.txt:14894:                                                               prayah 126/7                 nambh-nabh- 282/3
=== SOD sogdian
=== NYB naf
```


## [2026-09-07T19:33:58.083Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '10235,10255p' SNS_pages.txt; echo \"=== pdf tag\"; grep -n '\\[pdf page' SNS_pages.txt | awk -F: '$1<10244' | tail -2"
}
```


### [2026-09-07T19:33:59.268Z] TOOL RESULT

```
                                                                                                                           •flo/IT^               u/A^ .ijy.^lj :vazag:                                     4d>M


  „>d :/-li        {AiUb.1409) vita- iL^J^-va-jl vata-:b-                                                                                               (o^>«) «Jb rnafag: 5^1
      (Mir.   Man. 111,62) w'd : ^L (Mir. Man.
                                               I, 38)  .*!,                                       ^i^^Unabh-r^^^^af-: ^^V nafah-                                                              :       fc.

                                                 .T/1T^           If/W-S     .ly.Jl,     (1)      \6/\.<S.Wr>Man. II, 60)                         n'f:^ Miw                           .   1062)


                                     .TT/T^.^-W^'vaa-it:                         l-«"

                                                                                                  (patSt I pasSmanlh)
                                                                                                                      *JM*+ J\fil t*lp>l $ ^u t U*ap
                                                                                                                                 :


=== pdf tag
```


## [2026-09-07T19:34:06.314Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SNS_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nprint('total leaves',len(leaves))\ncum=0\nfor i,l in enumerate(leaves):\n    n=l.count('\\n')+1\n    if cum<=10244<=cum+n:\n        print('leaf(0-based)',i)\n    cum+=n\nEOF"
}
```


### [2026-09-07T19:34:07.581Z] TOOL RESULT

```
total leaves 243
leaf(0-based) 145
```


## [2026-09-07T19:34:20.913Z] TOOL CALL #40: Bash

```json
{
 "command": "ls site/pages/367.jpg 2>/dev/null; pdftoppm -f 367 -l 367 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg367 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/"
}
```


### [2026-09-07T19:34:22.650Z] TOOL RESULT

```
site/pages/367.jpg
total 31160
drwx------ 2 sfmqrb sfmqrb     4096 Sep  7 15:34 .
drwx------ 4 sfmqrb sfmqrb     4096 Sep  7 11:48 ..
-rw-rw-r-- 1 sfmqrb sfmqrb     8635 Sep  7 12:07 318-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   101267 Sep  7 12:07 318-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    61586 Sep  7 12:18 320-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   115970 Sep  7 12:18 320hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    86272 Sep  7 12:18 320-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    13284 Sep  7 12:18 320-zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb   107524 Sep  7 12:27 328-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    43713 Sep  7 12:35 331-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   135301 Sep  7 12:35 331-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    52382 Sep  7 12:41 333-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    88345 Sep  7 12:41 333-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    68568 Sep  7 12:43 335-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   105946 Sep  7 12:43 335-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   111897 Sep  7 13:57 340hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    24993 Sep  7 13:57 340-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    92337 Sep  7 13:59 342-mid.png
-rw-rw-r-- 1 sfmqrb sfmqrb    92697 Sep  7 13:56 343hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30778 Sep  7 13:56 343-mid.png
-rw-rw-r-- 1 sfmqrb sfmqrb    61503 Sep  7 13:52 346-zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb    81599 Sep  7 14:37 350-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    99691 Sep  7 14:40 351-mid.png
-rw-rw-r-- 1 sfmqrb sfmqrb   115624 Sep  7 14:43 355-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    85914 Sep  7 14:35 358hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    19549 Sep  7 14:35 358-mid.png
-rw-rw-r-- 1 sfmqrb sfmqrb    74812 Sep  7 14:35 358-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1579505 Sep  7 14:24 afm76.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1055262 Sep  7 14:23 afm77.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1297 Sep  7 15:29 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    14937 Sep  7 11:56 arrows.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1413 Sep  7 12:27 box1b.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1385 Sep  7 12:27 box1.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1132 Sep  7 12:27 box2b.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1988 Sep  7 12:27 box2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    85949 Sep  7 11:57 bqt2002_a.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72256 Sep  7 11:58 bqt2002_f1.png
-rw-rw-r-- 1 sfmqrb sfmqrb   161214 Sep  7 11:57 bqt2002_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   153966 Sep  7 13:44 bqt2014_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   299343 Sep  7 15:34 bqt2173_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63319 Sep  7 12:40 build333.py
-rw-rw-r-- 1 sfmqrb sfmqrb    83643 Sep  7 12:12 build.py
-rw-rw-r-- 1 sfmqrb sfmqrb     7075 Sep  7 12:13 c331_av1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10759 Sep  7 12:13 c331_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    11800 Sep  7 14:19 c355_arab2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     7474 Sep  7 14:19 c355_conn.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10501 Sep  7 14:19 c355_runik2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     7270 Sep  7 14:19 c355_runik.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3537 Sep  7 11:53 c_migare2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1829 Sep  7 11:53 c_migare3.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2261 Sep  7 11:53 c_migare4.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3958 Sep  7 11:53 c_migare.png
-rw-rw-r-- 1 sfmqrb sfmqrb    46690 Sep  7 13:44 crop_av3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    40759 Sep  7 13:44 crop_heb.png
-rw-rw-r-- 1 sfmqrb sfmqrb    94819 Sep  7 13:44 crop_pers0.png
-rw-rw-r-- 1 sfmqrb sfmqrb    19652 Sep  7 11:53 c_semita2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2639 Sep  7 11:53 c_semita.png
-rw-rw-r-- 1 sfmqrb sfmqrb    40259 Sep  7 11:50 ferdowsi2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30950 Sep  7 11:51 ferdowsi3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    28946 Sep  7 11:51 ferdowsi4.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4298 Sep  7 11:50 ferdowsi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    78732 Sep  7 13:40 ffd32.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30152 Sep  7 15:34 ffd77_bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    61328 Sep  7 15:34 ffd77.png
-rw-rw-r-- 1 sfmqrb sfmqrb    61328 Sep  7 13:44 ffd82.png
-rw-rw-r-- 1 sfmqrb sfmqrb     9383 Sep  7 11:55 masjid.wiki
-rw-rw-r-- 1 sfmqrb sfmqrb    33701 Sep  7 12:04 mk319a.py
-rw-rw-r-- 1 sfmqrb sfmqrb    46151 Sep  7 12:09 mk319b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    51516 Sep  7 12:09 mk322.py
-rw-rw-r-- 1 sfmqrb sfmqrb    61981 Sep  7 12:06 mk323.py
-rw-rw-r-- 1 sfmqrb sfmqrb    63978 Sep  7 12:35 mk330.py
-rw-rw-r-- 1 sfmqrb sfmqrb    64100 Sep  7 12:34 mk331.py
-rw-rw-r-- 1 sfmqrb sfmqrb    90456 Sep  7 12:42 mk332.py
-rw-rw-r-- 1 sfmqrb sfmqrb    99976 Sep  7 12:34 mk334.py
-rw-rw-r-- 1 sfmqrb sfmqrb    57252 Sep  7 12:38 mk337.py
-rw-rw-r-- 1 sfmqrb sfmqrb    83271 Sep  7 13:58 mk338.py
-rw-rw-r-- 1 sfmqrb sfmqrb    74349 Sep  7 13:57 mk340.py
-rw-rw-r-- 1 sfmqrb sfmqrb    59512 Sep  7 13:57 mk341.py
-rw-rw-r-- 1 sfmqrb sfmqrb    82502 Sep  7 13:57 mk342.py
-rw-rw-r-- 1 sfmqrb sfmqrb    66284 Sep  7 13:55 mk343.py
-rw-rw-r-- 1 sfmqrb sfmqrb    58811 Sep  7 13:57 mk344.py
-rw-rw-r-- 1 sfmqrb sfmqrb    36436 Sep  7 13:51 mk348b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    20510 Sep  7 13:47 mk348.py
-rw-rw-r-- 1 sfmqrb sfmqrb    67410 Sep  7 14:53 mk353.py
-rw-rw-r-- 1 sfmqrb sfmqrb    87481 Sep  7 14:40 mk354.py
-rw-rw-r-- 1 sfmqrb sfmqrb    38634 Sep  7 14:34 mk358.py
-rw-rw-r-- 1 sfmqrb sfmqrb    61503 Sep  7 13:42 navak2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3021 Sep  7 13:42 navak.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1525 Sep  7 13:41 p342_box2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1759 Sep  7 13:41 p342_box3.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1703 Sep  7 13:41 p342_box.png
-rw-rw-r-- 1 sfmqrb sfmqrb   108903 Sep  7 13:41 p342hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10531 Sep  7 13:39 p343_lat.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30408 Sep  7 13:39 p343_mus.png
-rw-rw-r-- 1 sfmqrb sfmqrb   103027 Sep  7 14:19 p355hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    86505 Sep  7 14:27 p358_av.png
-rw-rw-r-- 1 sfmqrb sfmqrb   114524 Sep  7 14:19 p358hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    37883 Sep  7 14:20 p358_q2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    36134 Sep  7 14:20 p358_q3.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4274 Sep  7 14:19 p358_quote.png
-rw-rw-r-- 1 sfmqrb sfmqrb    21223 Sep  7 13:47 part1.json
-rw-rw-r-- 1 sfmqrb sfmqrb    37635 Sep  7 12:04 part_a.json
-rw-rw-r-- 1 sfmqrb sfmqrb    58545 Sep  7 12:09 part_b.json
-rw-rw-r-- 1 sfmqrb sfmqrb     5736 Sep  7 14:43 patch354.py
-rw-rw-r-- 1 sfmqrb sfmqrb    97817 Sep  7 11:50 pg318hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    62558 Sep  7 11:50 pg318.png
-rw-rw-r-- 1 sfmqrb sfmqrb    67293 Sep  7 11:54 pg319.png
-rw-rw-r-- 1 sfmqrb sfmqrb   146848 Sep  7 12:01 pg320hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    80891 Sep  7 12:00 pg320.png
-rw-rw-r-- 1 sfmqrb sfmqrb    71522 Sep  7 12:00 pg321.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72193 Sep  7 11:57 pg323.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65279 Sep  7 11:49 pg324.png
-rw-rw-r-- 1 sfmqrb sfmqrb    55902 Sep  7 11:58 pg326.png
-rw-rw-r-- 1 sfmqrb sfmqrb   163982 Sep  7 11:53 pg327hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    73619 Sep  7 11:52 pg327.png
-rw-rw-r-- 1 sfmqrb sfmqrb    69765 Sep  7 12:12 pg329.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72757 Sep  7 12:13 pg330.png
-rw-rw-r-- 1 sfmqrb sfmqrb   128240 Sep  7 12:13 pg331hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    94945 Sep  7 12:12 pg331.png
-rw-rw-r-- 1 sfmqrb sfmqrb    75312 Sep  7 12:17 pg332.png
-rw-rw-r-- 1 sfmqrb sfmqrb   104609 Sep  7 12:27 pg333hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    70886 Sep  7 12:26 pg333.png
-rw-rw-r-- 1 sfmqrb sfmqrb    41782 Sep  7 12:18 pg334_bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    97297 Sep  7 12:18 pg334.png
-rw-rw-r-- 1 sfmqrb sfmqrb    58407 Sep  7 12:18 pg334_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    88659 Sep  7 12:22 pg335.png
-rw-rw-r-- 1 sfmqrb sfmqrb    57846 Sep  7 12:31 pg336.png
-rw-rw-r-- 1 sfmqrb sfmqrb    60414 Sep  7 12:19 pg337.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65267 Sep  7 13:37 pg338.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63922 Sep  7 13:44 pg339.png
-rw-rw-r-- 1 sfmqrb sfmqrb   111897 Sep  7 13:44 pg340hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    64116 Sep  7 13:39 pg341.png
-rw-rw-r-- 1 sfmqrb sfmqrb    75149 Sep  7 13:40 pg342.png
-rw-rw-r-- 1 sfmqrb sfmqrb    64151 Sep  7 13:39 pg343.png
-rw-rw-r-- 1 sfmqrb sfmqrb    60735 Sep  7 13:42 pg344.png
-rw-rw-r-- 1 sfmqrb sfmqrb   168870 Sep  7 13:42 pg346hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    76794 Sep  7 13:39 pg346.png
-rw-rw-r-- 1 sfmqrb sfmqrb    59757 Sep  7 14:29 pg349.png
-rw-rw-r-- 1 sfmqrb sfmqrb    70743 Sep  7 14:25 pg350.png
-rw-rw-r-- 1 sfmqrb sfmqrb    86553 Sep  7 14:25 pg351.png
-rw-rw-r-- 1 sfmqrb sfmqrb    69045 Sep  7 14:18 pg355.png
-rw-rw-r-- 1 sfmqrb sfmqrb    78195 Sep  7 14:27 pg357.png
-rw-rw-r-- 1 sfmqrb sfmqrb    49496 Sep  7 14:19 pg358.png
-rw-rw-r-- 1 sfmqrb sfmqrb    76202 Sep  7 15:29 pg362.png
-rw-rw-r-- 1 sfmqrb sfmqrb    66511 Sep  7 15:33 pg363.png
-rw-rw-r-- 1 sfmqrb sfmqrb    59224 Sep  7 15:34 pg367.png
-rw-rw-r-- 1 sfmqrb sfmqrb        0 Sep  7 13:36 queue.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  3120575 Sep  7 14:24 skeat1882.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  2985742 Sep  7 14:25 skeatdli.txt
-rw-rw-r-- 1 sfmqrb sfmqrb       49 Sep  7 14:29 sns_0022.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb       49 Sep  7 14:29 sns_0158.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb       49 Sep  7 12:17 sns53.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4676 Sep  7 14:29 sns_meta.json
-rw-rw-r-- 1 sfmqrb sfmqrb   135853 Sep  7 14:30 sns_n157.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   129673 Sep  7 14:30 sns_n159.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   113320 Sep  7 14:30 sns_n21.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    35039 Sep  7 12:17 sns_n53.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    35039 Sep  7 12:17 sns_n54.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  1021826 Sep  7 12:18 sns_p54.png
-rw-rw-r-- 1 sfmqrb sfmqrb 12288786 Sep  7 12:18 sns_text.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb      341 Sep  7 13:46 s.py
-rw-rw-r-- 1 sfmqrb sfmqrb   116699 Sep  7 14:30 t1.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb     1308 Sep  7 11:54 v2001.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    27253 Sep  7 12:02 z_maqd2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63140 Sep  7 12:02 z_maqd3.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4293 Sep  7 12:01 z_maqd.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2895 Sep  7 12:01 z_meh.png
-rw-rw-r-- 1 sfmqrb sfmqrb    25378 Sep  7 12:01 z_mezna2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    33685 Sep  7 12:01 z_mezna.png
```


## [2026-09-07T19:34:27.557Z] TOOL CALL #41: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg367.png"
}
```


### [2026-09-07T19:34:27.962Z] TOOL RESULT

```

```


## [2026-09-07T19:34:27.957Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-07T19:34:38.169Z] TOOL CALL #42: Bash

```json
{
 "command": "sed -n '1,40p' tools/fetch_source.py"
}
```


### [2026-09-07T19:34:38.209Z] TOOL RESULT

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
```


## [2026-09-07T19:34:44.789Z] TOOL CALL #43: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/natron\" \\\n \"https://en.wiktionary.org/wiki/niter\" \\\n \"https://en.wiktionary.org/wiki/%CE%BD%CE%AF%CF%84%CF%81%CE%BF%CE%BD\" \\\n \"https://en.wiktionary.org/wiki/%D9%86%D8%B7%D8%B1%D9%88%D9%86\" \\\n \"https://www.etymonline.com/word/natron\" \\\n \"https://www.etymonline.com/word/nitre\" \\\n ; do python3 tools/fetch_source.py \"$u\" --note \"page 367, root Nitiru: natron/niter chain Egyptian>Hebrew>Greek>Latin/Arabic>Spanish/French>English\" ; done 2>&1 | tail -20"
}
```


### [2026-09-07T19:34:52.051Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/2502d44a2ed41e31.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5465ff25f58627f1.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6eb7e33232e142f3.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3e08486e2b774a00.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/29cdee00bbc6ce80.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/acf863178a0dc612.txt
```


## [2026-09-07T19:34:55.026Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 2502d44a2ed41e31 5465ff25f58627f1 6eb7e33232e142f3 3e08486e2b774a00; do echo \"===== $f\"; grep -n -i -A8 'Etymology' $f.txt | head -50; done"
}
```


### [2026-09-07T19:34:56.257Z] TOOL RESULT

```
===== 2502d44a2ed41e31
62: Etymology 
63-
64- 1.2 
65- Noun 
66-
67- 1.2.1 
68- Related terms 
69-
70- 1.2.2 
--
93: Etymology 
94-
95- 3.2 
96- Pronunciation 
97-
98- 3.3 
99- Noun 
100-
101- 3.3.1 
--
113: Etymology 
114-
115- 4.2 
116- Noun 
117-
118- 4.2.1 
119- Synonyms 
120-
121- 4.2.2 
--
133: Etymology 
134-
135- 5.2 
136- Noun 
137-
138- 5.2.1 
139- Synonyms 
140-
141- 5.2.2 
--
233: Etymology
234- [ edit ] 
235-
236: Etymology tree
237-
238- Egyptian nṯr 
239-
240- Proto-Afroasiatic *-i ? 
241- Egyptian -j 
242-
===== 5465ff25f58627f1
65: Etymology 
66-
67- 1.3 
68- Pronunciation 
69-
70- 1.4 
71- Noun 
72-
73- 1.4.1 
--
175: Etymology
176- [ edit ] 
177-
178- From Middle English niter , nitere , nitre , nytre , from Old French nitre , from Latin nitrum ( “ native soda, natron ” ) , from Ancient Greek νίτρον ( nítron ) . Ultimately from Egyptian nṯrj ( “ natron ” ) . Doublet of natron and trona . Compare also natrium , nitrogen . Compare reconstructed Proto-Germanic *lauþrą ( “ nitre ” ) related to Modern English lye .
179-
180- Pronunciation
181- [ edit ] 
182-
183- Rhymes: -aɪtə(ɹ) 
===== 6eb7e33232e142f3
65: Etymology 
66-
67- 1.3 
68- Pronunciation 
69-
70- 1.4 
71- Noun 
72-
73- 1.4.1 
--
157: Etymology
158- [ edit ] 
159-
160-Borrowed from Semitic . Compare Hebrew נֶתֶר ( néṯer , “ washing soda ” ) , all ultimately from Egyptian nṯrj : 
161-
162- [ 1 ] 
163-
164- Pronunciation
165- [ edit ] 
===== 3e08486e2b774a00
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Noun 
69-
70- 1.3.1 
--
88: Etymology 
89-
90- 2.3 
91- Noun 
92-
93- 2.3.1 
94- Descendants 
95-
96- 2.4 
--
105: Etymology 
106-
107- 3.2 
108- Pronunciation 
109-
110- 3.3 
111- Noun 
112-
113- 4 
--
119: Etymology 
120-
121- 4.2 
122- Pronunciation 
123-
124- 4.3 
125- Noun 
126-
127- Toggle the table of contents 
--
196: Etymology
197- [ edit ] 
198-
199: Etymology tree
200-
201- Egyptian nṯr 
202-
203- Proto-Afroasiatic *-i ? 
204- Egyptian -j 
205-
```


## [2026-09-07T19:34:59.505Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"===== natron wikt\"; sed -n '230,300p' 2502d44a2ed41e31.txt; echo; echo \"===== نطرون wikt\"; sed -n '190,270p' 3e08486e2b774a00.txt"
}
```


### [2026-09-07T19:34:59.559Z] TOOL RESULT

```
===== natron wikt

 Wikipedia 

 Etymology
 [ edit ] 

 Etymology tree

 Egyptian nṯr 

 Proto-Afroasiatic *-i ? 
 Egyptian -j 

 Egyptian nṯrj der. 
 Semitic bor. 
 Ancient Greek νίτρον ( nítron ) bor. 
 Arabic نَطْرُون ( naṭrūn ) der. 
 Spanish natrón bor. 
 French natron bor. 
 English natron 

From French natron , from Spanish natrón , from Arabic نَطْرُون ( naṭrūn ) , from Ancient Greek νίτρον ( nítron , “ nitre ” ) , ultimately from Egyptian nṯrj ( “ natron ” ) : 

 Doublet of niter and trona .

 Noun
 [ edit ] 

 natron ( uncountable ) 

 ( mineralogy ) A crystalline mixture of hydrous sodium carbonate and sodium bicarbonate , with the chemical formula Na 2 C O 3 · 10 H 2 O .
 1931 , Aristotle, translated by E.W. Webster, Meteorologica , Bk. IV, ch. 6 : Natron and salt are soluble by liquid, but not all liquid but only such as is cold. Hence water and any of its varieties melt them, but oil does not. 

 1974 , Lawrence Durrell , Monsieur , Faber & Faber, published 1992 , page 242 : You know the mysterious idols they were supposed to set up to worship in their chapters – were they really human heads treated with natron after the Ancient Egyptian pattern – idols of Persian or Syrian provenance? 

 Related terms
 [ edit ] 

 natrium 

 Descendants
 [ edit ] 

 → Urdu: نیٹرون ( naiṭron ) 

 Anagrams
 [ edit ] 

 nonart , nonrat 

 Danish
 [ edit ] 

 Noun
 [ edit ] 

 natron   c ( singular definite natronen , not used in plural form ) 

 ( chemistry ) sodium hydrogen carbonate , sodium bicarbonate , NaHCO 3 .

 ( chemistry , obsolete ) sodium hydroxide , NaOH.

 References
 [ edit ] 

 Den Store Danske 

 French
 [ edit ] 

 Etymology

===== نطرون wikt
 [ edit ] 

 Arabic Wikipedia has an article on: نطرون 

 Wikipedia ar 

 Etymology
 [ edit ] 

 Etymology tree

 Egyptian nṯr 

 Proto-Afroasiatic *-i ? 
 Egyptian -j 

 Egyptian nṯrj der. 
 Semitic bor. 
 Ancient Greek νίτρον ( nítron ) bor. 
 Arabic نطرون 

 Borrowed from Ancient Greek νίτρον ( nítron ) .

 Pronunciation
 [ edit ] 

 IPA ( key ) : /natˤ.ruːn/ 

 Noun
 [ edit ] 

 نَطْرُون • ( naṭrūn )  m 

 ( mineralogy ) natron ; soda 

 Declension
 [ edit ] 

 Declension of noun نَطْرُون ( naṭrūn )

 singular

 basic singular triptote 

 indefinite

 definite

 construct

 informal

 نَطْرُون 
 naṭrūn 

 النَّطْرُون 
 an-naṭrūn 

 نَطْرُون 
 naṭrūn 

 nominative

 نَطْرُونٌ 
 naṭrūnun 

 النَّطْرُونُ 
 an-naṭrūnu 

 نَطْرُونُ 
 naṭrūnu 

 accusative

 نَطْرُونًا 
 naṭrūnan 

 النَّطْرُونَ 
 an-naṭrūna 

 نَطْرُونَ
```


## [2026-09-07T19:35:15.132Z] TOOL CALL #46: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%83n%C3%B3b%CA%B0-\" \\\n \"https://en.wiktionary.org/wiki/%D9%86%D8%A7%D9%81\" \\\n \"https://en.wiktionary.org/wiki/%D9%86%D8%A7%D9%81%D9%87\" \\\n \"https://en.wiktionary.org/wiki/nave\" \\\n \"https://en.wiktionary.org/wiki/auger\" \\\n \"https://en.wiktionary.org/wiki/umbilicus\" \\\n \"https://www.etymonline.com/word/nitrogen\" \\\n ; do python3 tools/fetch_source.py \"$u\" --note \"page 367, root Nobh/Ombh/Mbh: PIE navel-hub root, Persian naf/nafeh, English nave/navel/auger, Latin umbilicus\" ; done 2>&1 | tail -20"
}
```


### [2026-09-07T19:35:26.258Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/fd148ddc72a3f8a0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9b839564841c8895.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/21224c5d389d7c4d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9b56aa605b646ce2.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/be15b48bc5c8089e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e9e35070662c520b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e6a7ea7e5ca59842.txt
```


## [2026-09-07T19:35:29.540Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in fd148ddc72a3f8a0 9b839564841c8895 21224c5d389d7c4d; do echo \"######## $f\"; head -c 400 $f.txt; echo; grep -n -i 'Etymology$' -A 25 $f.txt | head -70; done"
}
```


### [2026-09-07T19:35:31.022Z] TOOL RESULT

```
######## fd148ddc72a3f8a0
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%83n%C3%B3b%CA%B0-
FETCHED: 2026-09-07T19:35:16Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found
######## 9b839564841c8895
URL: https://en.wiktionary.org/wiki/%D9%86%D8%A7%D9%81
FETCHED: 2026-09-07T19:35:17Z
STATUS: 200
TITLE: ناف - Wiktionary, the free dictionary

ناف - Wiktionary, the free dictionary 

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
940: Etymology
941- [ edit ] 
942-
943- This etymology is incomplete. You can help Wiktionary by elaborating on the origins of this term. 
944-
945- From Proto-Indo-European *h₃nebʰ- ( “ navel ” ) . Compare Avestan 𐬥𐬁𐬟𐬋 ( nāfō ) , Sanskrit नाभि ( nābhi ) , English navel .
946-
947- Pronunciation
948- [ edit ] 
949-
950- ( Classical Persian ) IPA ( key ) : /ˈnaːf/ 
951-
952- ( Dari, formal ) IPA ( key ) : [nɑːf] 
953-
954- ( Dari, formal ) IPA ( key ) : [nɑːf] 
955- ( Kabuli ) IPA ( key ) : [nɑːf] 
956-
957- ( Hazaragi ) IPA ( key ) : [nɔːf] 
958-
959- ( Iran, formal ) IPA ( key ) : [nɒːf] 
960-
961- ( Tajik, formal ) IPA ( key ) : [nɔf] 
962-
963- Rhymes: -aːf 
964-
965- Readings
--
1029: Etymology
1030- [ edit ] 
1031-
1032- Borrowed from Classical Persian ناف ( nāf ) . Doublet of نابھی ( nābhi ) . Related to English navel .
1033-
1034- Pronunciation
1035- [ edit ] 
1036-
1037- ( Standard Urdu ) IPA ( key ) : /nɑːf/ 
1038-
1039- Noun
1040- [ edit ] 
1041-
1042- ناف • ( nāf )  f ( Hindi spelling नाफ़ ) 
1043-
1044- navel 
1045- Synonym: نابھی ( nābhi ) 
1046-
1047- Retrieved from " https://en.wiktionary.org/w/index.php?title=ناف&oldid=92120348 "
1048-
1049- Categories : Arabic terms belonging to the root ن و ف 
1050- Arabic lemmas 
1051- Arabic verbs 
1052- Arabic form-I verbs 
1053- Arabic hollow form-I verbs 
1054- Arabic form-I verbs with و as second radical 
######## 21224c5d389d7c4d
URL: https://en.wiktionary.org/wiki/%D9%86%D8%A7%D9%81%D9%87
FETCHED: 2026-09-07T19:35:18Z
STATUS: 200
TITLE: نافه - Wiktionary, the free dictionary

نافه - Wiktionary, the free dictionary 

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
 Spe
138: Etymology
139- [ edit ] 
140-
141- From ناف ( nâf , “ navel ” ) , as the glands are located around the deer’s navel.
142-
143- Pronunciation
144- [ edit ] 
145-
146- ( Classical Persian ) IPA ( key ) : /naː.ˈfa/ 
147-
148- ( Dari, formal ) IPA ( key ) : [nɑː.fá] 
149-
150- ( Dari, formal ) IPA ( key ) : [nɑː.fá] 
151- ( Kabuli ) IPA ( key ) : [nɑː.fá] 
152-
153- ( Hazaragi ) IPA ( key ) : [nɔː.fá] 
154-
155- ( Iran, formal ) IPA ( key ) : [nɒː.fé] 
156-
157- ( Tajik, formal ) IPA ( key ) : [nɔ.fá] 
158-
159- Rhymes: -a 
160-
161- Readings
162-
163- Classical reading ?
```


## [2026-09-07T19:35:37.725Z] TOOL CALL #48: Bash

```json
{
 "command": "python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%83neb%CA%B0-\" --note \"page 367, root Nobh: Wiktionary PIE *h3nebh- 'navel'\"; python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/navel\" --note \"page 367, English navel from PIE nobh-\""
}
```


### [2026-09-07T19:35:39.948Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/2d5823018158525a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/dd4d131cd22591d4.txt
```


## [2026-09-07T19:35:43.258Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"#### PIE h3nebh\"; sed -n '1,6p' 2d5823018158525a.txt; grep -n -i -m1 -A40 'Root$\\|Etymology$' 2d5823018158525a.txt | head -60"
}
```


### [2026-09-07T19:35:44.447Z] TOOL RESULT

```
#### PIE h3nebh
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%83neb%CA%B0-
FETCHED: 2026-09-07T19:35:39Z
STATUS: 200
TITLE: Reconstruction:Proto-Indo-European/h₃nebʰ- - Wiktionary, the free dictionary

Reconstruction:Proto-Indo-European/h₃nebʰ- - Wiktionary, the free dictionary 
131: Root
132- [ edit ] 
133-
134- *h₃nebʰ- [ 1 ] [ 2 ] 
135-
136- hub 
137-
138- navel 
139-
140- Derived terms
141- [ edit ] 
142-
143- Terms derived from the Proto-Indo-European root *h₃nebʰ- (11 c, 0 e) 
144-
145- *h₃émbʰ-ō ~ *h₃m̥bʰ-nés [ 3 ] [ 4 ] 
146- Proto-Germanic: *ambô ( see there for further descendants )
147-
148- Proto-Italic: *omβō [ 4 ] 
149- Latin: umbō ( see there for further descendants )
150-
151- *h₃nēbʰ-o- ~ *h₃nēbʰ-eh₂- [ 5 ] 
152- Armenian:
153- Old Armenian: անիւ ( aniw , “ wheel ” ) ( see there for further descendants )
154-
155- *h₃nobʰ-eh₂ [ 6 ] 
156- Proto-Balto-Slavic: *nabāˀ 
157- Latgalian: noba 
158-
159- Latvian: naba 
160-
161- Proto-Germanic: *nabō ( see there for further descendants )
162-
163- → Proto-Finnic: *napa ( see there for further descendants )
164-
165- *h₃nóbʰ-i-s [ 6 ] 
166- Proto-Balto-Slavic: *nabis 
167- Old Prussian: nabis 
168-
169- Proto-Indo-Iranian: *Hnā́bʰiš 
170- Proto-Indo-Aryan: *Hnā́bʰiṣ 
171- Sanskrit: नाभि ( nā́bhi ) ( see there for further descendants )
```


## [2026-09-07T19:35:47.145Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '171,240p' 2d5823018158525a.txt"
}
```


### [2026-09-07T19:35:47.188Z] TOOL RESULT

```
 Sanskrit: नाभि ( nā́bhi ) ( see there for further descendants )

 *h₃nóbʰ-ōl 

 *h₃nóbʰ-yo-m 
 Proto-Indo-Iranian: *Hnábʰyam 
 Proto-Indo-Aryan: *Hnábʰyam 
 Sanskrit: नभ्य ( nábhya ) 

 *h₃nṓbʰ-s ~ *h₃nebʰ-és 
 Proto-Indo-Iranian: *Hnā́ps ~ *Hnabʰás 
 Proto-Iranian: *Hnā́fah ( see there for further descendants )

 References
 [ edit ] 

 ^ Pokorny, Julius ( 1959 ), “ 1. (enehh-), emhh-, ombh-, nō̆bh- (nēbh-?), m̥bh- ”, in Indogermanisches etymologisches Wörterbuch [ Indo-European Etymological Dictionary ] (in German), volume 1, Bern, München: Francke Verlag, pages 314-315 

 ^ Kölligan, Daniel ( 2018 ), “Chapter XX: Proto-Indo-European”, in Klein, Jared S., Joseph, Brian D. , Fritz, Matthias , editors, Handbook of Comparative and Historical Indo-European Linguistics: An International Handbook (Handbücher zur Sprach- und Kommunikationswissenschaft [ Handbooks of Linguistics and Communication Science ] ; 41.2 ), volume 3, Berlin; Boston: De Gruyter Mouton, →ISBN , § The lexicon of Proto-Indo-European, page 2267 : “ *h₃nebʰ- ” 

 ^ Kroonen, Guus ( 2013 ), “*amban-”, in Etymological Dictionary of Proto-Germanic (Leiden Indo-European Etymological Dictionary Series; 11 )‎ [1] , Leiden, Boston: Brill , →ISBN , page 24 

 ↑ 4.0 4.1 De Vaan, Michiel ( 2008 ), “ umbō ”, in Etymological Dictionary of Latin and the other Italic Languages (Leiden Indo-European Etymological Dictionary Series; 7), Leiden, Boston: Brill, →ISBN , page 639 

 ^ Martirosyan, Hrach ( 2010 ), Etymological Dictionary of the Armenian Inherited Lexicon (Leiden Indo-European Etymological Dictionary Series; 8), Leiden and Boston: Brill, pages 89–90 

 ↑ 6.0 6.1 Kroonen, Guus ( 2013 ), “*nabō-”, in Etymological Dictionary of Proto-Germanic (Leiden Indo-European Etymological Dictionary Series; 11 )‎ [2] , Leiden, Boston: Brill , →ISBN , pages 380-381 

 Retrieved from " https://en.wiktionary.org/w/index.php?title=Reconstruction:Proto-Indo-European/h₃nebʰ-&oldid=92151502 "

 Categories : Proto-Indo-European lemmas 
 Proto-Indo-European roots 
 Proto-Indo-European HReC-shaped roots 

 Hidden categories: Pages with etymon 
 Proto-Indo-European entries with etymon 
 Pages with entries 
 Pages with 1 entry 
 Sanskrit terms with non-redundant manual transliterations 

 This page was last edited on 23 August 2026, at 21:55.

 Definitions and other text are available under the Creative Commons Attribution-ShareAlike License ; additional terms may apply. By using this site, you agree to the Terms of Use and Privacy Policy. 

 Privacy policy 

 About Wiktionary 

 Disclaimers 

 Legal & safety contacts 

 Code of Conduct 

 Developers 

 Statistics 

 Cookie statement 

 Mobile view 

 Search 

 Search 

 Toggle the table of contents 

 Reconstruction:Proto-Indo-European/ h₃nebʰ-
```


## [2026-09-07T19:35:58.554Z] TOOL CALL #51: Bash

```json
{
 "command": "python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/Hn%C3%A1%CC%81fah\" --note \"page 367, Proto-Iranian *Hnafah > Av. nafo, MP naf, NP naf\" ; python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/Hn%C4%81%CC%81fah\" --note \"page 367, Proto-Iranian *Hnafah variant spelling\""
}
```


### [2026-09-07T19:36:02.042Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/4513d9204e04aca6.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b3fab51ee48c10cd.txt
```


## [2026-09-07T19:36:05.324Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 4513d9204e04aca6 b3fab51ee48c10cd; do echo \"### $f\"; sed -n '1,6p' $f.txt; grep -n -m1 -A45 'Noun$' $f.txt | head -60; done"
}
```


### [2026-09-07T19:36:06.519Z] TOOL RESULT

```
### 4513d9204e04aca6
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/Hn%C3%A1%CC%81fah
FETCHED: 2026-09-07T19:36:00Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found### b3fab51ee48c10cd
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/Hn%C4%81%CC%81fah
FETCHED: 2026-09-07T19:36:02Z
STATUS: 200
TITLE: Reconstruction:Proto-Iranian/Hnā́fah - Wiktionary, the free dictionary

Reconstruction:Proto-Iranian/Hnā́fah - Wiktionary, the free dictionary 
142: Noun
143- [ edit ] 
144-
145- *Hnā́fah [ 1 ] 
146-
147- navel 
148-
149- kin 
150-
151- Inflection
152- [ edit ] 
153-
154- masculine a-stem
155-
156- singular
157-
158- dual
159-
160- plural
161-
162- nominative
163-
164- *Hnā́fah
165-
166- *Hnā́fā(w)
167-
168- *Hnā́fāh(ah)
169-
170- vocative
171-
172- *Hnā́fa
173-
174- *Hnā́fā(w)
175-
176- *Hnā́fāh(ah)
177-
178- accusative
179-
180- *Hnā́fam
181-
182- *Hnā́fā(w)
183-
184- *Hnā́fānh
185-
186- instrumental
187-
```


## [2026-09-07T19:36:09.867Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n -m1 -A40 'Descendants' b3fab51ee48c10cd.txt | head -50; echo \"==== etymology\"; grep -n -m1 -A10 'Etymology$' b3fab51ee48c10cd.txt"
}
```


### [2026-09-07T19:36:11.185Z] TOOL RESULT

```
71: Descendants 
72-
73- 1.3 
74- References 
75-
76- Toggle the table of contents 
77-
78- Reconstruction:Proto-Iranian/ Hnā́fah 
79-
80- Add languages 
81-
82- Reconstruction 
83-
84- Discussion 
85-
86- English 
87-
88- Read 
89-
90- Edit 
91-
92- View history 
93-
94- Tools 
95-
96- Tools
97-
98- move to sidebar 
99- hide 
100-
101- Actions
102-
103- Read 
104-
105- Edit 
106-
107- View history 
108-
109- General
110-
111- What links here 
==== etymology
137: Etymology
138- [ edit ] 
139-
140- Thematicized from *Hnā́fš ~ *Hnabáh , from Proto-Indo-Iranian *Hnā́ps ~ *Hnabʰás , from Proto-Indo-European *h₃nṓp-s ~ *h₃nebʰ-és , from *h₃nebʰ- ( “ navel ” ) +‎ *-s .
141-
142- Noun
143- [ edit ] 
144-
145- *Hnā́fah [ 1 ] 
146-
147- navel
```


## [2026-09-07T19:36:14.422Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && awk '/^ Descendants$/{f=1} f&&NR>250{print} NR>420{exit}' b3fab51ee48c10cd.txt | head -60"
}
```


### [2026-09-07T19:36:15.903Z] TOOL RESULT

```
 Middle Persian: ( /⁠nāf⁠/ , “ family ” ) 
 Manichaean script: 𐫗𐫀𐫛 ( nʾp ) 
 Book Pahlavi script: [Book Pahlavi needed] ( nʾp ) 
 ⇒ Middle Persian: ( /⁠nāfag⁠/ ) 
 Manichaean script: 𐫗𐫀𐫛𐫃 ( nʾpg ) 
 Book Pahlavi script: [Book Pahlavi needed] ( nʾpg ) 
 Persian: ناف ( nâf ) 

 → Old Armenian: նահա-պետ ( naha-pet ) 

 References
 [ edit ] 

 ^ Novák, Ľubomír ( 2013 ), Problem of Archaism and Innovation in the Eastern Iranian Languages (PhD dissertation) ‎ [1] , Prague: Univerzita Karlova v Praze, filozofická fakulta 

 Retrieved from " https://en.wiktionary.org/w/index.php?title=Reconstruction:Proto-Iranian/Hnā́fah&oldid=92171945 "

 Categories : Proto-Iranian terms derived from Proto-Indo-Iranian 
 Proto-Iranian terms derived from Proto-Indo-European 
 Proto-Iranian lemmas 
 Proto-Iranian nouns 
 Proto-Iranian masculine a-stem nouns 
 ira-pro:Anatomy 

 Hidden categories: Pages with entries 
 Pages with 1 entry 
 Sogdian term requests 
 Central Kurdish terms with non-redundant manual transliterations 
 Middle Persian term requests 
 Middle Persian terms with redundant script codes 
 Requests for Book Pahlavi script for Middle Persian terms 

 This page was last edited on 24 August 2026, at 00:45.

 Definitions and other text are available under the Creative Commons Attribution-ShareAlike License ; additional terms may apply. By using this site, you agree to the Terms of Use and Privacy Policy. 

 Privacy policy 

 About Wiktionary 

 Disclaimers 

 Legal & safety contacts 

 Code of Conduct 

 Developers 

 Statistics 

 Cookie statement 

 Mobile view 

 Search 

 Search 

 Toggle the table of contents
```


## [2026-09-07T19:36:21.912Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 29cdee00bbc6ce80 acf863178a0dc612 e6a7ea7e5ca59842; do echo \"#### $f\"; sed -n '1,5p' $f.txt; grep -n -i -m3 -B2 -A12 'natron\\|nitre\\|nitrogen' $f.txt | head -40; echo; done"
}
```


### [2026-09-07T19:36:23.497Z] TOOL RESULT

```
#### 29cdee00bbc6ce80
URL: https://www.etymonline.com/word/natron
FETCHED: 2026-09-07T19:34:51Z
STATUS: 200
TITLE: Natron - Etymology, Origin & Meaning

1:URL: https://www.etymonline.com/word/natron
2-FETCHED: 2026-09-07T19:34:51Z
3-STATUS: 200
4:TITLE: Natron - Etymology, Origin & Meaning
5-
6:Natron - Etymology, Origin & Meaning 
7-
8- Search 
9- Log in 
10-
11- Columns 
12- Forum 
13- Apps 
14- Premium 
15-
16- Log in 
17-
18- Advertisement Remove Ads 

#### acf863178a0dc612
URL: https://www.etymonline.com/word/nitre
FETCHED: 2026-09-07T19:34:52Z
STATUS: 200
TITLE: Nitre - Etymology, Origin & Meaning

1:URL: https://www.etymonline.com/word/nitre
2-FETCHED: 2026-09-07T19:34:52Z
3-STATUS: 200
4:TITLE: Nitre - Etymology, Origin & Meaning
5-
6:Nitre - Etymology, Origin & Meaning 
7-
8- Search 
9- Log in 
10-
11- Columns 
12- Forum 
13- Apps 
14- Premium 
15-
16- Log in 
17-
18- A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 

#### e6a7ea7e5ca59842
URL: https://www.etymonline.com/word/nitrogen
FETCHED: 2026-09-07T19:35:26Z
STATUS: 200
TITLE: Nitrogen - Etymology, Origin & Meaning

1:URL: https://www.etymonline.com/word/nitrogen
2-FETCHED: 2026-09-07T19:35:26Z
3-STATUS: 200
4:TITLE: Nitrogen - Etymology, Origin & Meaning
5-
6:Nitrogen - Etymology, Origin & Meaning 
7-
8- Search 
9- Log in 
10-
11- Columns 
12- Forum 
13- Apps 
14- Premium 
15-
16- Log in 
17-
18- Advertisement Remove Ads
```


## [2026-09-07T19:36:27.216Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 29cdee00bbc6ce80 acf863178a0dc612 e6a7ea7e5ca59842; do echo \"#### $f\"; grep -n -i 'Egypt\\|Greek nitron\\|νίτρον\\|Latin nitrum\\|French nitrogène\\|Hebrew' $f.txt | head -8; done"
}
```


### [2026-09-07T19:36:28.478Z] TOOL RESULT

```
#### 29cdee00bbc6ce80
25: "native carbonate of sodium," 1680s, from French natron (1660s), which is said to be directly from Arabic natrun , itself from Greek nitron , itself possibly of Eastern origin (see nitre ). Medieval Latin and Paracelsus (16c.) had a form anatron , from Arabic with the article assimilated ( an-natron ). It is the source of the chemical symbol Na for sodium and the word-forming element natro- , used in the names of minerals to indicate the presence of sodium.
32: c. 1400, "native sodium carbonate" (a sense now obsolete), from Old French nitre (13c.), from Latin nitrum , from Greek nitron , which is possibly of Eastern origin (compare Hebrew nether "carbonate of soda;" Egyptian ntr ). Originally a word for native soda, but also associated since the Middle Ages with saltpeter (potassium nitrate) for obscure reasons; this became the predominant sense by late 16c.
54: Egypt 
56: Old English Egipte "the Egyptians," from French Egypte, from Greek Aigyptos "the river Nile, Egypt," from Amarna Hikuptah, corresponding to Egyptian Ha(t)-ka-ptah "temple of the soul of Ptah," the creative god associated with Memphis, the ancient city of Egypt. Strictly one of th
#### acf863178a0dc612
58: c. 1400, "native sodium carbonate" (a sense now obsolete), from Old French nitre (13c.), from Latin nitrum , from Greek nitron , which is possibly of Eastern origin (compare Hebrew nether "carbonate of soda;" Egyptian ntr ). Originally a word for native soda, but also associated since the Middle Ages with saltpeter (potassium nitrate) for obscure reasons; this became the predominant sense by late 16c.
65: "native carbonate of sodium," 1680s, from French natron (1660s), which is said to be directly from Arabic natrun , itself from Greek nitron , itself possibly of Eastern origin (see nitre ). Medieval Latin and Paracelsus (16c.) had a form anatron , from Arabic with the article assimilated ( an-natron ). It is the source of the chemical symbol Na for sodium and the word-forming element natro- , used in the names of minerals to indicate the presence of sodium.
#### e6a7ea7e5ca59842
25: colorless, odorless gaseous element, 1794, from French nitrogène , coined 1790 by French chemist Jean Antoine Chaptal (1756-1832), from Greek nitron "sodium carbonate" (see nitro- ) + French gène "producing," from Greek -gen "giving birth to" (see -gen ). The gas was identified in part by analysis of nitre. An earlier name for it was mephitic air (1772), and Lavoisier called it azote (see azo- ). It forms about 78% of the weight of the Earth's atmosphere. Related: Nitrogenic; nitrogenous .
40: before vowels nitr- , word-forming element used scientifically and indicating nitrogen, nitrate, or nitric acid; from Greek nitron (see nitre ).
```


## [2026-09-07T19:36:45.129Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== LKT\"; grep -n -i 'natron\\|natrun\\|nitron\\|nitrum' LKT.txt | head -10; echo \"=== DEV\"; grep -n -i 'natron\\|nitre' DEV.txt | head -10; echo \"=== PHN\"; grep -n -i 'NATRON\\|NITRE' PHN.txt | head -10; echo \"=== SKT\"; grep -n -i 'nitre\\|natron' SKT.txt | head -10; echo \"=== AFM/FVQ/PLA\"; grep -n 'نطرون' AFM.txt FVQ.txt incoming/PLA/PLA_pages.txt TAD.txt ARB_mo3rb.txt 2>/dev/null | head -10"
}
```


### [2026-09-07T19:36:45.247Z] TOOL RESULT

```
=== LKT
982:[Aus  pers.  büräh]  'Borax,  borsaures Natron';  hieraus  mit  gleicher  Bedeutung sp.  borraj,  pg.  borax  [auch  tincal],  frz. borax,  it.  borrace;  ndl.  engl,  borax, dtsch.  Borax;  russ.  bulg.  bura,  serb. poln.  boraks.  cech.  borax.  [DE  241. Devic  DEt  70.
3601:'Natron'  [Prov.  25,20;  Jer  2.22;  wohl wie  aram.  niträ  aus  äg.  ntrj.],  hieraus gr.  vixpov,  lat.  nitrum  und  mit  lat.  sal zusammengesetzt:  it.  salnitro,  pg.  sp. salitre,  rum,  ^alitru;  dtsch.  Salniter, (dial.)  Saliter;  cech.  sahii/tr,  sanytr,  poln. saletra,  russ.  stlitra,  serb.  saliira  'Sal- peter'. Aus  ar.  natrün  ergab  sich  frz. engl.  7iatron,  dtsch.  Natron  und  mit  ar. Art.  sp.  anatron.
5852:3^a&ofe  1542 Nadir  1565 Nankint'gJ  1554 Naphtha  1538 J^a/-(/e  1548 Natron  1567 JV^afscfe  1530 Neschires  j.  127 iST/if/r/M  1569 Nirwana  1573 Nischan  1574
6105:nargeela  1556 I  narghile  1556 i  nargileh  1556 I  natron  1567 I  nautch  1530 I  »let'Z  1568
6635:narguilS  1556 j  natron  1567
7440:naphtha  1538 wj^er  1568 nitrum  1567 nucha  1579 nuphar  1570
9972:almojarife  1519 almojarra  1439 almojatre  1581 alnirineda  1511 almoraduj  1411 ahnotacen  1503 almozal(l)a  1511  a almucio  1520 almud  1490 almuecin  1485 almuidano  1485 aloque(ro)  803 aloqueria  803 alpargata  243 alpicoz  576 alquequenge  1016 alqueria  1096 alquez  1174 alquifol  1227 aquilar  1181 alquile(r)  1181 alquhnia  1157 alquitara  1130 alqmtrdn  1128 altramuz  2115 alubia  1333 «Zmc^cZ  2142 aluquete  2153 aZfaci/  2160 amacena  476 amalgama  1378 amapola  762  d amargaza  829 amarillo  70 mnbar  78 amoscarse  1436 amuco  71 amtileto  866 amusco  1515  a anacal(o)  1545 anadel  1566 «w«/?/  1537 anafre  130 anatron  1567 anazea  1583 andamio  520 annafe  130 ante(ado)  1305 antimonio  918 anzarote  86 afiacal  1545 anacea  1583 anaciar  1583 anafil  1537 öw«7  1568 «/Itr  1568 arac  92 arambel  811 arancel  1428 arfceZW  dial.  204 arhollön  204 arcaditz  988
=== DEV
283:Alcali.  Esp.  et  port,  alcali.  De  l'arabe  JkiJÎ  al-qali,  cendres de  soude  ou  la  plante  elle-même.  Dans  certaines  régions du  midi  de  la  France,  on  réserve  le  nom  de  caliou  aux cendres  de  sarments  de  vigne.  Le  nitre  est  quelquefois  ap- pelé algali  par  nos  alchimistes.
297:8.  Alaurat,  nitre,  corruj)tion  de  (^)^-^^  (d-bunraq ,  bo- rax. Les  deux  sels  sont  souvent  confondus  :  cwVllronitrum est  spuma  nitri,  quod  arabice  dicitur  baurach.  w  (Lex.  (dcli.)
307:i3.  AJp^aïi,  nitre,  est  le  même  mot  (\ue  alcali.
1834:Natron.   Esp.  anatron.  De  l'arabe  (j^4aj  natroim,  avec
2723:Anaton ,  voy.  Natron.
2724:Anatron,  esp.  voy.  Natron.
4033:Nataron,  voy.  Natron,
4034:Natron.
5124:AàU  pers.  voy.  Naffe. NyiLj  voy.  Nacairo. cjoU  voy.  Nabab. L^  voy.  Nabalhéeti. *JLJ>  voy.  Nabca. j-Ls?  voy.  Alchimie,  66. frUç  voy.  Nuque. ^yàr^j  voy.  Neskhi. ^jj— «J  voy.  Nizeré. rj.LùJ  voy,  Alcbimie,  yo. (jUu  per.f.  voy.  Nichan. ^^jLj  voy.  Natron. -Uàj  voy.  Nizam. wJaj  voy.  Nadir. >jl3  voy.  Noria.
=== PHN
2523:vyy [iatwfl^] nitre, en persan ij^ [boûrah]. — Borax est le
7932:NATRON, s. m. (a.)
7938:grande quantité de natron. — Autrefois on écrivait également
7939:ANATRON , et celte variante représente le même mot arabe , pré-
10772:Natron, s. m. (a.) — S'écrivait autrefois aussi anatron 288
=== SKT
12318:Kitro.  (F.  -  L.  -  Gk.  -  ArnbO  F.  niirt. —  L.  ni/rwm. —  Gk.  w't/jok.  —  Arab,  nitnin^ natriirt,  natron,  native  alkaline  salt. {Nitrt  and  natron  arc  doublets,  but  applied to  different  substances.)  Dar.  mtiv-gen, that  which  produces  nitre,  from  7(1'',  base of  Ti'Tv*!*-,  to  produce.
16432:(E.;  owJF.-L.)  Pot  for or  $aitjelar,  where  telar  is  an for  'sall-hohkr;'  so  that  the be  saii  is  superfluous.  O.  F.  saliere, tp.Il->ellrr  ; '  Cot.  •>  L.  salarium,  salt- Ir  (to  late  L.) ;  from  L.  salarius.  adj.. ^ng  lo  salt*L.jay,salL  See  salary fw). t-petro,  nitre.  (E.;  am/ F.  —  L.  aku/ Fnt  for  OF.  sal/tstrr,  «It.petre •  L,  taJ  f^ir^,  salt  of  the  rock. tai,  aalli   Gk.  Wr^,    a  rock;    sec
23691:BvM    Latin  from    Creek  from JMper,  myrrh,  nitre. from  Italian  from  Latin  from ^Arakie:  diaper.
=== AFM/FVQ/PLA
TAD.txt:590:والى الفارسية « بوره 6 وهو ملح حاصل من الحامض البورفي والنطرون منه طبيعي 
TAD.txt:592:كياوية وهو خلاف اللطرون . أما النطرون فدعي كذ! هن وادي النطرون في 
AFM.txt:834:( البورق) اضئاف مالم وجلى وارمنى ومصري وهو النطرون معرب بوره ومنة
```


## [2026-09-07T19:36:59.692Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '3590,3610p' LKT.txt; echo \"=== leaf\"; python3 - <<'EOF'\nt=open('LKT.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\ncum=0\nleaves=t.split('\\f')\nc=0\nfor i,l in enumerate(leaves):\n    n=l.count('\\n')+1\n    if c<=3601<=c+n:\n        print('leaf(0-based)',i,'-> printed page',i-26)\n    c+=n\nEOF"
}
```


### [2026-09-07T19:37:01.203Z] TOOL RESULT

```
Ar.  nawäla.]
1562.  Ar  iianäla:
'Hütte';  hieraus  mit  Imäla  [ä  >  e]  asp. nagnela  'Hütte,  armseliKS  Bude';  lat. mai>äUa,  magälia  'Hütten'  geht  auf  dass. semitsdie  VVt.  zurück,  hieraus  pgr.  mal- ha  'Schäterhütte'  [Cnnstancio  Dicc  670  c]. [DE  323.    Eguilaz  462/463.    ML  5223.
1563.  Pers.  näz:
'Vergnügen,  Freude'  [Horn  NpEt  S.  228, Nr.  1017],  tk.  ebenso  'Ziererei';  hieraus rum.  7iaz,  naznri  "A-dSs  ,  Nasenrümpfen'.
1564.  Ar.  iiazar:
'Anblick ;  Wohlwollen,  Gunst',  ebenso tk. ;  hieraus  rum.  nazar  'Gewogenheit',
1565.  Ar  uazTr:
'��hnlich,  entgegengesetzt  gelegen',  nazlr as-sanit  'dem  Zenit  entgegengesetzt'; hieraus  kat.  sp.  pg.  frz.  rum.  nadir  'Fuß- punkt'; M.nadiro;  dtsch.  Nadir,  engl.wa- dir  'dem  Zenit  entgegengesetzter  Punkt'. [DE  323.   Eguilaz  462.   Devic  DEt  174.
1566  Ar.  nazzär: 'Inspektor;  Admiral,  Hauptmann,  An- führer' [vom  Vb.  nazara  'anblicken', s.  hier  Nr.  1564];  hieraus  mit  ar.  Art. und  Imäla  [ä  >  e]  sp.  anadel  'Haupt- mann', pg.  annodem,  anadel  [Gonstan- cio  Dicc  75  a]  'Hauptmann  der  Bogen- schützen', siz.  (alt)  annadaru,  nadaru 'öffentlicher  Eichmeister',  Nh.anadarari 'Gewichte  und  Maße  prüfen'.  [DE  189. Eguilaz  461.    Gr  S  Voci  Sic  242.
1567.  Hebr.  neOer:
'Natron'  [Prov.  25,20;  Jer  2.22;  wohl wie  aram.  niträ  aus  äg.  ntrj.],  hieraus gr.  vixpov,  lat.  nitrum  und  mit  lat.  sal zusammengesetzt:  it.  salnitro,  pg.  sp. salitre,  rum,  ^alitru;  dtsch.  Salniter, (dial.)  Saliter;  cech.  sahii/tr,  sanytr,  poln. saletra,  russ.  stlitra,  serb.  saliira  'Sal- peter'. Aus  ar.  natrün  ergab  sich  frz. engl.  7iatron,  dtsch.  Natron  und  mit  ar. Art.  sp.  anatron.
1568.  Sskr.  nilas:
'Schwarz',  [aus  der  Zusammenstellung 'schwarz  wie  die  Nacht'  wurde  'schwärz- lich' und  schließlich]  'bläulich'  [titlas  <^ *nihlas  *nihras,  also  dasselbe  Wort wie  lat.  nigtr  <^  *niher  <^  *nihrus], ebenso  Tpers. mlä  'Indigo',  ar.  nila  'dass.'; hieraus  mit  ar.  Art.,  der  dem  folgenden n  assimiliert  wird,  sp.  anil,  anir,  kat. antßl,  pg.  anil,  frz.  anil;  ndl.  anijl,  engl. anile,  neel  'Indigo';  dtsch.  Anilin,  ein Farbstoff,  der  i.  J.  182i6  bei  der  Destil- lation von  Indigo  entdeckt  und  i.  J.  1884 aus  dem  Steinkohlenteer  hergestellt %vurde.  —  Vgl.  noch  angloind.  neelwalla 'Indigopflanzor',  neel-kothee  'Indigo- pflanzung'. [DE  196.  Eguilaz  269.  ML 5923,    Hobson-Jobson  31.
1569.  Pers.  nilgävv:
Eine  Antilope  Portax  pictus  Pallas  mit schieferblauem  Kleide,  die  in  Persien und  Nordindien  vorkommt  [aus  pers. nll  'blau',  s.  hier  Nr.  1568,  und  gätv 'Kuh,  Rind'  Horn  NpEt  S.  1 98,  Nr.  888] ; hieraus  frz.  nilgant,  nylghaut;  dtsch. Nilgau,  engl,  nilghau,  nylghau.  [Devic DEt  176.
1570.  Pers.  nTlflfär:
Eine  Wasserpflanze  Nymphaea  alba  'See- rose' [aus  pers.  m/  'blau',  s.  hier  Nr.  1568, und  nüfär  'Seerose',  woraus  der  botn- nische  Namen  Nuphar  luteum],  ar.  nai- nüfar,  vulg.  nenüfar;  hieraus  sp.  kat. it.  nenufar,  frz.  nenufar,  rum.  nenufär, nufär  'Wasserrose'.  Das  Wort  wurde zuerst  i.  J.  1534  durch  den  Botaniker Otto  BRUNFELS  ins  Frz.  eingeführt. [DE824.  Eguilaz464.  DevicDEt  175/176, Lammens  Rem  181/182.
1571.  Pers.  nlmtäii:
[Aus  pers.  new  'Hälfte,  halb'  Horn NpEtS.  239,  Nr.  1069,  und  tän  'Körper, Leib'  ebenda  S.  88,  Nr.  393],  tk.  mit Metalhesis  tninian  'wattierte  Weste  mit Ärmeln' ;  hieraus  rum.  mintean  'wat- tiertes Wams'.
1572.  Mal.  nipa:
=== leaf
leaf(0-based) 148 -> printed page 122
```


## [2026-09-07T19:37:09.858Z] TOOL CALL #59: Bash

```json
{
 "command": "for u in \"https://vajehyab.com/moein/%D9%86%D8%B7%D8%B1%D9%88%D9%86\" \"https://abadis.ir/fatofa/%D9%86%D8%B7%D8%B1%D9%88%D9%86/\" \"https://abadis.ir/fatofa/%D9%86%DB%8C%D8%AA%D8%B1%D9%88%D8%AC%D9%86/\" \"https://vajehyab.com/moein/%D9%86%DB%8C%D8%AA%D8%B1%D9%88%D8%AC%D9%86\"; do python3 tools/fetch_source.py \"$u\" --note \"page 367, Persian natrun/nitrogen: Mo'in entry (MON:4745, MON:4880)\"; done 2>&1 | tail -8"
}
```


### [2026-09-07T19:37:13.936Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/9f92ed65f7552e0c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/73bd7b50ee348bb1.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4e7db07694a71add.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5e1cff52adad3665.txt
```


## [2026-09-07T19:37:17.994Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 9f92ed65f7552e0c 73bd7b50ee348bb1 4e7db07694a71add 5e1cff52adad3665; do echo \"##### $f\"; sed -n '1,5p' $f.txt; grep -n 'نطرون\\|نیتروژن\\|معین\\|فر\\.' $f.txt | head -12; echo; done"
}
```


### [2026-09-07T19:37:19.245Z] TOOL RESULT

```
##### 9f92ed65f7552e0c
URL: https://vajehyab.com/moein/%D9%86%D8%B7%D8%B1%D9%88%D9%86
FETCHED: 2026-09-07T19:37:11Z
STATUS: -1
TITLE: 


##### 73bd7b50ee348bb1
URL: https://abadis.ir/fatofa/%D9%86%D8%B7%D8%B1%D9%88%D9%86/
FETCHED: 2026-09-07T19:37:12Z
STATUS: 200
TITLE: نطرون - معنی در دیکشنری آبادیس

4:TITLE: نطرون - معنی در دیکشنری آبادیس
6:نطرون - معنی در دیکشنری آبادیس 
10: نطرون
16: نطرون. [ ن َ ] ( معرب ، اِ ) بوره ارمنی. ( منتهی الارب ) ( ناظم الاطباء ) ( از ذخیره خوارزمشاهی ). بورق. ( المنجد ). قسمی از بورق ارمنی است و در صنعت صابون سازی به کار است. ( از متن اللغة ). بورق ارمنی. ( منتهی الارب ) ( از نزهةالقلوب ) ( از اقرب الموارد ). بورق احمر. ( تحفه حکیم مؤمن ). گروهی گفته اند بوره ارمنی است و گروهی گفته اند سنگی است که به روزگار چون آهک می شود، وی را اندر داروهاء بیرون به کار دارند و نباید خوردن. ( یادداشت مؤلف از ذخیره خوارزمشاهی ). به رومی او را افراسیمون گویند، بشر گوید: آن بوره سوخته است ، و به سندی او را قطراوس گویند، و گفته اند: نطرون بوره ای است که از قاین به اطراف برند و رنگ او سرخ است ، ابوزید بلخی گوید در کتاب کیمیا که : آن بوره ارمنی است دو نوع است : یک نوع سفید است و سبک و به خانه زنبور مشابهت دارد، و نوع دیگر پارها باشد تنک ؛ رازی در کتاب خود آورده است که : در خمیر نان به کار برند آنچه سفید بود او را نطرون گویند. ( از ترجمه صیدنه ). 
25:(یا: وادی نطرون) مجموعه ای از هشت دریاچه، واقع در وادی نطرو یا درۀ شمالی، در صحرای لیبی، مصر، به فاصلۀ ۱۰۰کیلومتری غرب قاهره۵. شهرت این منطقه به سبب چهار صومعۀ آن است، که از کتابخانه های آن ها دست نوشته های ارزشمند بسیاری به مجموعه های اروپایی افزوده شده است. wikijoo: نطرون 
40: آبادیس از سال 1385 فعالیت خود را در زمینه فن آوری اطلاعات آغاز کرد. نخستین پروژه آبادیس، سایت دیکشنری آبادیس بود. دیکشنری آنلاین آبادیس از ابتدا تاکنون تغییرات بسیاری کرده و ویژگی های مختلفی به آن اضافه شده است. آبادیس افزونه ای کاربردی برای مرورگرهای فایرفاکس و کروم و اپلیکیشن موبایل طراحی کرده است که میتوانید از لینک های بالا دانلود کنید. دیکشنری آبادیس شامل بخش هایی نظیر دیکشنری به زبان های مختلف از جمله انگلیسی، فارسی، عربی و همچنین بیست دیکشنری تخصصی با تلفظ انگلیسی و آمریکایی، ترجمه مخفف و کلمات اختصاری، مترجم آنلاین متن، لغتنامه دهخدا، فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راهنمای انتخاب اسم و ... می باشد. 

##### 4e7db07694a71add
URL: https://abadis.ir/fatofa/%D9%86%DB%8C%D8%AA%D8%B1%D9%88%D8%AC%D9%86/
FETCHED: 2026-09-07T19:37:13Z
STATUS: -1
TITLE: 


##### 5e1cff52adad3665
URL: https://vajehyab.com/moein/%D9%86%DB%8C%D8%AA%D8%B1%D9%88%D8%AC%D9%86
FETCHED: 2026-09-07T19:37:13Z
STATUS: -1
TITLE:
```


## [2026-09-07T19:37:27.924Z] TOOL CALL #61: Bash

```json
{
 "command": "for u in \"https://abadis.ir/fatofa/%D9%86%DB%8C%D8%AA%D8%B1%D9%88%DA%98%D9%86/\" \"https://abadis.ir/fatofa/%D9%86%DB%8C%D8%AA%D8%B1%D8%A7%D8%AA/\"; do python3 tools/fetch_source.py \"$u\" --note \"page 367, Persian nitrogen/nitrate: Mo'in/Dehkhoda entry (MON:4880)\"; done; cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in $(tail -2 index.jsonl | python3 -c \"import sys,json;[print(json.loads(l)['file']) for l in sys.stdin]\"); do echo \"##### $f\"; sed -n '1,5p' $f; grep -n 'نیتروژن\\|نیترات\\|فرانسه\\|فر\\.' $f | head -10; done"
}
```


### [2026-09-07T19:37:31.924Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/1950f78c5106fd04.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b8e4274247f2ae66.txt
##### data/verification/sources/web/1950f78c5106fd04.txt
sed: can't read data/verification/sources/web/1950f78c5106fd04.txt: No such file or directory
ugrep: warning: data/verification/sources/web/1950f78c5106fd04.txt: No such file or directory
##### data/verification/sources/web/b8e4274247f2ae66.txt
sed: can't read data/verification/sources/web/b8e4274247f2ae66.txt: No such file or directory
ugrep: warning: data/verification/sources/web/b8e4274247f2ae66.txt: No such file or directory
```


## [2026-09-07T19:37:35.300Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 1950f78c5106fd04 b8e4274247f2ae66; do echo \"##### $f\"; sed -n '1,5p' $f.txt; grep -n 'نیتروژن\\|نیترات\\|فرانسه\\|(فر' $f.txt | head -8; echo; done"
}
```


### [2026-09-07T19:37:36.478Z] TOOL RESULT

```
##### 1950f78c5106fd04
URL: https://abadis.ir/fatofa/%D9%86%DB%8C%D8%AA%D8%B1%D9%88%DA%98%D9%86/
FETCHED: 2026-09-07T19:37:30Z
STATUS: 200
TITLE: نیتروژن - معنی در دیکشنری آبادیس

4:TITLE: نیتروژن - معنی در دیکشنری آبادیس
6:نیتروژن - معنی در دیکشنری آبادیس 
10: نیتروژن
19: نیتروژن. [ رُ ژِ ] ( فرانسوی ، اِ ) ازت. رجوع به ازت شود. 
35: نیتروژِن ( به انگلیسی: Nitrogen ) یا اَزُت ( به فرانسوی: Azote ) یکی از عنصرهای شیمیایی در جدول تناوبی است که نشان شیمیایی آن N و عدد اتمی آن ۷ است. نیتروژن معمولاً به صورت یک گاز، نافلز، دو اتمی بی اثر، بی رنگ، بی مزه و بی بو است که ۷۸٪ جو زمین را دربر گرفته و عنصر اصلی در بافت های زنده است. نیتروژن ترکیبات مهمی مانند آمونیاک، اسید نیتریک و سیانیدها را شکل می دهد. 
36:گاز نیتروژن درصَد عمده ای از هوای اطراف ما را تشکیل می دهد. از گاز نیتروژن می توان به منظور کاهش یا از بین بردن اُکسایش ( اکسیداسیون ) مواد غذایی استفاده کرد. 
37:نیتروژن از گروه غیرفلزات بوده و دارای بار الکترون منفی ۳٫۰ می باشد. نیتروژن پنج الکترون در پوسته خود داشته و در نتیجه در اکثر ترکیبات سه ظرفیتی است. نیتروژن خالص یک گاز بی اثر و بی رنگ است و ۷۸٪ جو زمین را به خود اختصاص داده است. در ۶۳K منجمد شده و در ۷۷K به صورت مایع، به مادهٔ سرمایشی معروف سرمازا ( Cryogen ) تبدیل می شود. 
38:به طور کلی چرخه نیتروژن به زبان ساده عبارت است از: نیتروژنِ هوا به هنگام آذرخش به اکسید نیتروژن تبدیل شده و در باران حل شده و جذب خاک می شود؛ در خاک این ترکیبات، توسط باکتری ها به موادی تبدیل می شوند که به وسیله گیاهان جذب می شوند. حیوانات از جمله سگ هار و سگ پاچه گیرحیوانات با خوردن گیاهان، نیتروژن را وارد بدن خود می کنند، با مردن و تجزیه اندام حیوانات، دوباره نیتروژن وارد هوا می شود. 

##### b8e4274247f2ae66
URL: https://abadis.ir/fatofa/%D9%86%DB%8C%D8%AA%D8%B1%D8%A7%D8%AA/
FETCHED: 2026-09-07T19:37:31Z
STATUS: 200
TITLE: نیترات - معنی در دیکشنری آبادیس

4:TITLE: نیترات - معنی در دیکشنری آبادیس
6:نیترات - معنی در دیکشنری آبادیس 
10: نیترات
19: نیترات. ( فرانسوی ، اِ ) در شیمی به معنی نمک یا استر اسید نیتریک است ، آن را ازتات هم می گویند. ( فرهنگ اصطلاحات علمی ). نام عام همه املاح اسید نیتریک است ، ترکیبی که از اسید نیتریک با یک فلز یا یک باز نتیجه می شود . ( فرهنگ فارسی معین ).
20:- نیترات ِ آمونیم ؛ نمکی است سفید و متبلور، بر اثر گرما تجزیه می شود و به عنوان ماده منفجره مورد استعمال دارد. ( فرهنگ اصطلاحات علمی ).
21:- نیترات ِ باریم ؛ ملحی که از اسید نیتریک با فلز باریم نتیجه می شود و مانند همه نیترات ها در آب محلول است. ( فرهنگ فارسی معین ).
22:- نیترات ِ پتاسیم ؛ نمکی است سفید و متبلور و محلول در آب ، در پزشکی مورد استعمال دارد در تهیّه باروت نیز به مصرف می رسد، نیترات پتاسیم طبیعی را شوره نیز می گویند. ( فرهنگ اصطلاحات علمی ).
23:- نیترات ِ دارژان ؛ نیترات نقره. سنگ جهنم. رجوع به سنگ جهنم شود.
```


## [2026-09-07T19:38:04.196Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== BQT natrun\"; grep -n 'نطرون' BQT_v1_pages.txt BQT_v2_pages.txt incoming/BQT/BQT_v*_pages.txt 2>/dev/null | head -5; echo \"== RCH\"; grep -n -i 'natrun\\|natrūn' RCH.txt | head -5; echo \"== LEW nitrum\"; grep -n -i 'nitrum' LEW_1910.txt LAT.txt | head -8; echo \"== LEW umbilicus\"; grep -n -i 'umbilicus' LEW_1910.txt LAT.txt | head -6"
}
```


### [2026-09-07T19:38:04.313Z] TOOL RESULT

```
== BQT natrun
== RCH
95706:A   nitrun  ox  natrun^  'Siive.  Natron.  Native  alkaline  salt.
== LEW nitrum
LAT.txt:41581:nitrum, -I n.: nitre. Emprunt latinise au gr. vixpov, lui-meme
== LEW umbilicus
LAT.txt:11676:gloss. de Placide, GLK V 13,33, par granum mali punici aut umbilicus
LAT.txt:69495:umbilicus: t. le suirant.
LAT.txt:69501:D4rir4s: umbilicus : nombril} et par analogie tont objet circulaire,
LAT.txt:69506:des dAformations dirersea, cf.M.L.9»4S umbilicus, et imbiUcus',
LAT.txt:69510:des formes populaires: umbilicus n'a pas seulement un suffixe de
LAT.txt:69520:A c 8tA de nabdlo "nombril". L'A 14 nent -I- de umbilicus se retroure
```


## [2026-09-07T19:38:07.697Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '41578,41590p' LAT.txt; echo \"-----umbo/umbilicus\"; sed -n '69490,69530p' LAT.txt"
}
```


### [2026-09-07T19:38:07.782Z] TOOL RESULT

```
nixor,-dris (poet., Lucr., Vg.), intensif de nitor', ad-, co- (y. co¬
nor), e-, in-, ob-, re- (l. imperiale, = resisto, aduersor), sub-nitor ;
praenisus (Gl.).
nitrum, -I n.: nitre. Emprunt latinise au gr. vixpov, lui-meme
emprunt 4 a 1 'egyptien. Derives latins: nitraria f.; nitratus, nitreus,
nitrosus.
nix, niuls (t) f.: neige. - Ancien, usuel. Panroman. M.L.S93C.niuit (t) ap. Pac., Paul.4 (Noa.507,39), sagittis niuit, plumbo et
saxis grandinat, "il .neige". Certalnea fanes romanes aupposent aassi
*niuBre, M.L.593°b et *niuicdre (~gs), M.L.5934.
D 4 riv£s et compos^s: niuSlis: de neige; niudrius, usit£ surtout dana
niuBriu* colu*, niudrius saccus "filtre a neige"; M.1.5931 niuaria ;
niudtus : -a aqua ; niueus, cf.M-L.Q3O6 subniueus ; niuSsus : neigeux,
M.L.5935; niuSscB, -is (tardif): devenir blanc de neige; niuifer
-----umbo/umbilicus
uraber -brl m.: vari4t4 de mouton issue du croisenent du mouf-
flon et de la brebis (Plin . 0 , ly y ). Forme peu sfire; est-ce le nom13 IT
umbra
propre Umber ? Cf. Umber (canis) Vg., Ae.xa, 753 > u. porcus Cat. 39, n,'
etc.). • t
umbilicus: t. le suirant.
umbS,' -Snis m.: toute pibbe falsant saillie »ur une surface,
surtout ronde ou conique} ,d'oh dirers sens sp 4 ciaux dans les 1 .
techniques: bosse de bonclier; pii de la toge faieant saillie sur
la poitrine, pierre de parement fornant le rebord du trottoirj bornej
conde, et c• Cf.Rich, s.u. ,
D4rir4s: umbilicus : nombril} et par analogie tont objet circulaire,
entre autres: i° bont du cylindre autour duquel Atait roulA un lirre
ancien (sene calquA de grec ojAcpaXoC?)} 9 ° tige mAtallique formant
le nilieu d'un cadran solaire} 3° sorte de coquillage} 4 u. Veneris
"nonbril de V 4 nus», piante. - Ancien, technique. Panroman,^avec
des dAformations dirersea, cf.M.L.9»4S umbilicus, et imbiUcus',
9044 *umbiliculus. - DdrirAs: umbilicaris', onbilical} umbilicatus:
ombiliquA.
Comme le nom de l'"ongle", celni du "nombril" affecte sourent
des formes populaires: umbilicus n'a pas seulement un suffixe de
dAriration a -1-, comme ungula (r. unguis), mais un second suffixe
complexe *- iko-, de forme thAmatique, correapondant A -ik-. La forme
principale est indiquAe par 1'indo-iranien: skr .nabhih "nombril,
moyeu", a x. nabi-nazdista- "le plus proche du nonbril", c.-A-d."le
plus proche parent", cf. 1at. proximus (rAd. nabhih sert ausa i a designer
la parentA )} le dArirA neutre ndbhyam signifie seulement "moyeu".
L'iranien a une forne populaire a *—ph—: ar. n 3 f 5 "nombril" (pers.
nSf),n 5 fya- "de famille". Le double sens de "nombril" et "moyeu"
se retroure dans r.pruss. nabis et 'en geraqniqu-e: r.h.a.nobo "moyeu"
A c 8tA de nabdlo "nombril". L'A 14 nent -I- de umbilicus se retroure
dans r.h.a. nabalo, r.irl. imb liu, gr.opiqxxXoC} pour le oaractbre de
cet AlAment, cf.ungula', r. Chantraine, format ion des noms en^gr.
ancien, $.346. Le cp de 6\upa\oc peut reposer sur *ph ou sur bh.
L»o prothAtique de umbilicus, qui est exceptionnel, sans doute popu¬
laire, est comparable A delui de unguis } dans les deux cas, il se
retroure en grec} le d 4 rir 4 umb5, qui n'a Ijas le^ suffixe I, le pr 4 sente
aussi (le sens de umbd existe dans gr. ©(tcpaXoc). VAd.nSbhi $ et gr.
oiicpaXoc) ont 4t4 largement employAs par la langue religieuse} ceci
4 claire sans doute un rers parodiqu* de-Plaute, Men.xSjS* Dies quiaem
iam ad umbilicum est dimidiatus mortuus. Les formes aberrantes sl.
```


## [2026-09-07T19:38:17.698Z] TOOL CALL #65: Bash

```json
{
 "command": "sed -n '1,120p' tools/verify_check.py"
}
```


### [2026-09-07T19:38:17.740Z] TOOL RESULT

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


## [2026-09-07T19:38:23.387Z] TOOL CALL #66: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg367.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/367.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/ | head"
}
```


### [2026-09-07T19:38:23.463Z] TOOL RESULT

```
total 16480
drwxrwxr-x  2 sfmqrb sfmqrb   4096 Sep  7 15:38 .
drwxrwxr-x 13 sfmqrb sfmqrb   4096 Sep  7 13:51 ..
-rw-rw-r--  1 sfmqrb sfmqrb  71589 Sep  5 10:46 100.png
-rw-rw-r--  1 sfmqrb sfmqrb 104864 Sep  4 19:03 101.png
-rw-rw-r--  1 sfmqrb sfmqrb  68145 Sep  5 10:49 102.png
-rw-rw-r--  1 sfmqrb sfmqrb  79623 Sep  5 10:55 103.png
-rw-rw-r--  1 sfmqrb sfmqrb  78826 Sep  5 10:59 104.png
-rw-rw-r--  1 sfmqrb sfmqrb  82500 Sep  5 11:05 105.png
-rw-rw-r--  1 sfmqrb sfmqrb  55270 Sep  5 11:03 106.png
```


## [2026-09-07T19:38:25.729Z] AGENT

Now let me write the verification file.


## [2026-09-07T19:45:45.768Z] TOOL CALL #67: Write

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/page-367.json",
 "content": "{\n  \"pdf_page\": 367,\n  \"book_page\": 337,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-07\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Nitiru\",\n      \"verdict\": \"disputed\",\n      \"modern_form\": \"Egyptian nṯrj 'natron' (the Akkadian word nitiru is itself a borrowing of it, not the source of the family)\",\n      \"note\": \"The word Nourai puts at the head of the chart is real: Zimmern (AKD p.61, §15 'Mineralien') lists 'nitiru wohl Natron, nur vereinzelt zu belegen'. But Zimmern prints the whole entry in square brackets — his notation for a culture word that is NOT an Akkadian export — and says explicitly 'wohl, wie hebr. nāter, aram. nitrō, netrō, griech. νίτρον, λίτρον usw., Natron, < ägypt. ntrj'. That is, Akkadian nitiru is a sibling borrowing from Egyptian, not the ancestor of Hebrew nether. Every modern authority agrees: Ernout-Meillet ('nitrum … emprunt latinisé au gr. νίτρον, lui-même emprunt à l'égyptien'), Lokotsch no.1567, Etymonline ('Egyptian ntr'), Wiktionary (etymology tree Egyptian nṯr > nṯrj > Semitic > Gk νίτρον). So the root box should read Egyptian nṯrj (Coptic ⲛⲓⲧⲣⲟⲛ), with Akkadian nitiru and Hebrew néṯer as two independent Semitic-area borrowings of it. The chain below the root (Semitic > Greek > Latin/Arabic > French/Spanish > English/Persian) is otherwise sound, and the gloss 'natron; carbonate of soda' is right. Chart-internal error: the Greek node prints 'natron' where Greek in fact has νίτρον/λίτρον — see node #2.\",\n      \"note_fa\": \"سرریشهٔ این نمودار در واقع مصری باستان nṯrj «ناترون، کربنات سدیم» است، نه اکدی. تسیمرن در «وام‌واژه‌های اکدی» (ص ۶۱) واژهٔ اکدی nitiru را در قلاب گذاشته و خود می‌نویسد که این واژه، مانند عبری nāter و آرامی nitrō و یونانی νίτρον، از مصری nṯrj آمده است؛ پس اکدی nitiru هم‌سطح و هم‌وامِ عبری است و نیای آن نیست. ارنو-میه، لوکوچ (شمارهٔ ۱۵۶۷) و ویکی‌واژه نیز همین را می‌گویند. بنابراین ادعای نورایی در مورد سرریشه نادرست است و باید مصری باستان بنشیند؛ اما بقیهٔ زنجیره (سامی › یونانی › لاتینی و عربی › فرانسه و اسپانیایی › انگلیسی و فارسی) درست است. معنای «ناترون، کربنات سدیم» هم درست است.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/natron\",\n        \"https://en.wiktionary.org/wiki/niter\",\n        \"https://www.etymonline.com/word/natron\",\n        \"https://www.etymonline.com/word/nitre\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"AKD:61\", \"status\": \"partial\", \"note\": \"AKD.txt, leaf 71 (the printed '61' stands immediately above the line): '[akk. nitiru wohl Natron, nur vereinzelt zu belegen, wohl, wie hebr. näter, aram. nitrō, netrō, griech. νίτρον, λίτρον usw., Natron, < ägypt. ntrj.]'. Page and word are exactly Nourai's, but Zimmern derives BOTH the Akkadian and the Hebrew from Egyptian nṯrj — he does not make Akkadian the source.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"LKT\", \"where\": \"no. 1567, p. ~122 (leaf 148)\", \"stance\": \"contradicts\", \"note\": \"'1567. Hebr. neθer: Natron [Prov. 25,20; Jer 2,22; wohl wie aram. niṭrā aus äg. nṯrj], hieraus gr. νίτρον, lat. nitrum …' — Lokotsch heads the family with Hebrew and traces it to Egyptian; no Akkadian at all.\"},\n        {\"src\": \"LAT\", \"where\": \"s.v. nitrum (Ernout-Meillet)\", \"stance\": \"contradicts\", \"note\": \"'nitrum, -ī n.: nitre. Emprunt latinisé au gr. νίτρον, lui-même emprunt à l'égyptien.' — the ultimate source is Egyptian.\"},\n        {\"src\": \"KLN\", \"where\": \"p. 1049 s.v. niter\", \"stance\": \"partial\", \"note\": \"'fr. Gk. νίτρον … fr. Heb. nether, \\\"carbonate of soda, natron\\\" (stem nithr-; cp. Aram. nithra)' — Klein stops at Hebrew and knows no Akkadian stage.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Hebrew\",\n          \"words\": \"nither, nether\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Biblical Hebrew נֶתֶר néṯer 'washing soda, natron' (Prov. 25:20 'vinegar upon nitre'; Jer. 2:22), oblique stem niṯr-, beside Aramaic niṭrā/neṯrō. The word is a Late-Bronze-Age culture loan from Egyptian nṯrj 'natron' (nṯr 'divine' + adjectival -j, i.e. 'the divine/purifying salt' used in mummification), which reached Canaan through the Egyptian natron trade of the Wadi Naṭrūn lakes. Nourai's two spellings 'nither, nether' are simply the construct/oblique stem niṯr- and the absolute néṯer. What is wrong is only the arrow's source: Hebrew néṯer does not come from Akkadian nitiru — the two are parallel borrowings of the same Egyptian word (Zimmern AKD 61, Lokotsch 1567).\",\n          \"derivation_fa\": \"عبری کتاب مقدس נֶתֶר (néṯer) «ناترون، جوش‌شیرین طبیعی» (امثال ۲۵:۲۰ و ارمیا ۲:۲۲) با ستاک مایل niṯr-، در برابر آرامی niṭrā. این واژه وام‌واژه‌ای فرهنگی از مصری nṯrj «ناترون» است (از nṯr «خدایی» + پسوند صفتی ‎-j‎، یعنی «نمکِ پاک‌کنندهٔ خدایان» که در مومیایی به کار می‌رفت) و از راه بازرگانی ناترون دریاچه‌های وادی‌النطرون به کنعان رسیده است. دو نگارش نورایی (nither/nether) همان ستاک مایل و صورت مطلق‌اند. ادعای نورایی دربارهٔ خودِ واژه درست است، ولی وام‌گیری از اکدی نیست: عبری و اکدی هر دو مستقیماً از مصری وام گرفته‌اند.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/niter\", \"https://www.etymonline.com/word/nitre\"],\n          \"ref_check\": [\n            {\"ref\": \"AKD:61\", \"status\": \"partial\", \"note\": \"AKD.txt leaf 71: '… wohl, wie hebr. näter, aram. nitrō, netrō, griech. νίτρον … < ägypt. ntrj' — Zimmern names hebr. nāter on the cited page, but as a co-borrowing from Egyptian, not as a descendant of Akkadian.\"},\n            {\"ref\": \"KLN:1031\", \"status\": \"partial\", \"note\": \"KLN_1966 line 25028 (p.1031) s.v. natron: 'Fr. Sp. natron, fr. Arab. natrun, fr. Gk. νίτρον. See niter.' The Hebrew stage is given on p.1049 s.v. niter ('fr. Heb. nether'), not on p.1031.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"LKT\", \"where\": \"no. 1567\", \"stance\": \"supports\", \"note\": \"'Hebr. neθer: Natron [Prov. 25,20; Jer 2,22; wohl wie aram. niṭrā aus äg. nṯrj], hieraus gr. νίτρον, lat. nitrum' — Hebrew néṯer < Egyptian nṯrj, and Greek out of Hebrew.\"},\n            {\"src\": \"KLN\", \"where\": \"p. 1049 s.v. niter\", \"stance\": \"supports\", \"note\": \"'fr. Heb. nether, \\\"carbonate of soda, natron\\\" (stem nithr-; cp. Aram. nithra)' — both of Nourai's spellings are Klein's.\"},\n            {\"src\": \"SKT\", \"where\": \"s.v. Nitre (SKT.txt line 12318)\", \"stance\": \"partial\", \"note\": \"'F. nitre — L. nitrum — Gk. νίτρον — Arab. nitrun, natrun, natron' — Skeat wrongly routes Greek through Arabic and omits the Hebrew/Egyptian stage; superseded.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Greek\",\n          \"words\": \"natron\",\n          \"verdict\": \"transcription_suspect\",\n          \"derivation\": \"The Greek word is νίτρον nítron (also Doric/older λίτρον lítron), 'native soda, natron', attested from Herodotus and the Hippocratic corpus onward and used by Aristotle (Meteorologica IV.6); it was borrowed from a Semitic form of the Egyptian word (Hebrew néṯer / Aramaic niṭrā) in the archaic-classical period, Greek ι rendering the Semitic short e/i and the Semitic ṯ/ṭ being taken over as τ. There is no Greek *natron: that a-vocalism is the Arabic-Spanish reflex (naṭrūn > natrón), which is what the daughter boxes of this very node correctly show. The printed page 337 does show 'natron' in the Greek box, so the extraction is faithful and the slip is Nourai's own: he has back-projected the modern form 'natron' onto Greek. Read νίτρον (nitron) and the whole chart works: νίτρον > Lat. nitrum > Fr. nitre, and νίτρον > Arab. naṭrūn > Sp. natrón.\",\n          \"derivation_fa\": \"صورت یونانی این واژه νίτρον (nítron) و در گونهٔ دوری λίτρον است، به معنی «ناترونِ طبیعی»، که از هرودوت و بقراط به بعد گواهی دارد و ارسطو نیز در «هواشناسی» (۴:۶) آن را به کار برده است؛ یونانی آن را از صورتی سامی از واژهٔ مصری (عبری néṯer / آرامی niṭrā) وام گرفته و ι یونانی به‌جای e/i کوتاهِ سامی و τ به‌جای ṯ/ṭ نشسته است. یونانی هیچ‌گاه *natron نداشته؛ واکهٔ a از راه عربی نَطرون و اسپانیایی natrón پدید آمده که خودِ نورایی در خانه‌های پایین‌تر همان را آورده است. تصویر صفحهٔ ۳۳۷ نشان می‌دهد که در خانهٔ یونانی «natron» چاپ شده است، پس خوانش اسکن درست بوده و خطا از خودِ کتاب است (نورایی صورت نوین را به یونانی برگردانده). صحیح: νίτρον.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%CE%BD%CE%AF%CF%84%CF%81%CE%BF%CE%BD\",\n            \"https://en.wiktionary.org/wiki/natron\",\n            \"https://www.etymonline.com/word/nitre\"\n          ],\n          \"error_in\": \"book\",\n          \"book_prints\": \"natron\",\n          \"correct_form\": \"νίτρον (nítron), Doric λίτρον\",\n          \"ref_check\": [\n            {\"ref\": \"KLN:1049\", \"status\": \"contradicts\", \"note\": \"KLN_1966 line 25473 (between the page markers 1046 and 1054, i.e. p.~1049) s.v. niter: 'fr. L. nitrum, fr. Gk. νίτρον, \\\"native sodium carbonate, natron\\\", fr. Heb. nether'. Klein's Greek form is νίτρον, not natron — the reference Nourai cites gives the correct form, so the misprint is his.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"LKT\", \"where\": \"no. 1567\", \"stance\": \"contradicts\", \"note\": \"'hieraus gr. νίτρον, lat. nitrum' — Lokotsch too has only νίτρον.\"},\n            {\"src\": \"AKD\", \"where\": \"p. 61\", \"stance\": \"contradicts\", \"note\": \"Zimmern writes 'griech. νίτρον, λίτρον usw.' — the two attested Greek shapes, neither with a.\"},\n            {\"src\": \"LAT\", \"where\": \"s.v. nitrum\", \"stance\": \"contradicts\", \"note\": \"'Emprunt latinisé au gr. νίτρον' (Ernout-Meillet).\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Arabic\",\n          \"words\": \"natrŭn\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Arabic نَطْرُون naṭrūn 'natron, soda', a Hellenistic-period loan of Greek νίτρον taken over by the Egyptian-Arabic mineral and soap trade; the Greek short ι was heard as a, the emphatic ṭ substitutes for Greek τ next to r (as regularly in Arabic loans from Greek), and the noun was fitted to the Arabic faʿlūn/quTrūn shape with -ūn, exactly as qaṭrān 'tar' beside Greek κέδρος. The Wadi Naṭrūn ('Natron Valley') lakes west of Cairo, the classical source of the mineral, carry the same word. From Arabic it went on to Spanish (with and without the article: natrón, anatrón) and to French/English natron. Nourai's transliteration natrŭn with a breve is the book's way of writing the long ū of naṭrūn.\",\n          \"derivation_fa\": \"عربی نَطْرُون وام‌واژه‌ای از یونانی νίτρον است که در دورهٔ هلنیستی از راه تجارت مواد معدنی و صابون‌سازی مصر به عربی رسیده: ι کوتاه یونانی به a بدل شده، τ در همسایگی r به طای مفخّم (ط) تبدیل شده — چنان‌که در وام‌واژه‌های یونانی در عربی معمول است — و واژه به قالب فَعْلُون درآمده، درست مانند قَطران. نام «وادی‌النطرون» در غرب قاهره، که کانِ کلاسیک این مادّه است، از همین واژه است. از عربی به اسپانیایی (natrón و با حرف تعریف anatrón) و از آن‌جا به فرانسه و انگلیسی رفته است. آوانگاری «natrŭn» در کتاب همان نَطرون با ūی کشیده است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%86%D8%B7%D8%B1%D9%88%D9%86\",\n            \"https://en.wiktionary.org/wiki/natron\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN:1031\", \"status\": \"supports\", \"note\": \"KLN_1966 line 25028 (p.1031) s.v. natron: 'Fr. Sp. natron, fr. Arab. natrun, fr. Gk. νίτρον' — Arabic naṭrūn out of Greek, exactly the arrow drawn.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"LKT\", \"where\": \"no. 1567\", \"stance\": \"supports\", \"note\": \"'Aus ar. naṭrūn ergab sich frz. engl. natron, dtsch. Natron und mit ar. Art. sp. anatron.'\"},\n            {\"src\": \"AFM\", \"where\": \"AFM.txt line 834 s.v. (البورق)\", \"stance\": \"silent\", \"note\": \"Addi Shir mentions النطرون only inside the entry on بورق ('وهو النطرون معرب بوره') — he treats bawraq as arabized Persian būra and gives no etymology for naṭrūn itself; so no Persian claim on the word.\"},\n            {\"src\": \"TAD\", \"where\": \"TAD.txt lines 590-592\", \"stance\": \"partial\", \"note\": \"al-Unaysi distinguishes بورق from النطرون and connects النطرون with 'وادي النطرون' in Egypt — Egyptian, not Persian or Akkadian, provenance.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Persian\",\n          \"words\": \"natrûn «نطرون» : sodium\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"New Persian نطرون naṭrūn is the Arabic word taken over unchanged (spelled with ط, the tell-tale Arabic orthography); Dehkhoda marks it معرب, i.e. an Arabic form, and glosses it 'بورهٔ ارمنی … بورق' with citations from Muntahā al-arab, the Ẕaḵīra-ye Ḵᵛārazmšāhī and the Persian Ṣaydana — that is, it entered Persian through the medieval Arabic pharmacological and alchemical literature (9th-12th c.), not through everyday speech. The route Greek > Arabic > Persian that Nourai draws is therefore right. Only the gloss is loose: نطرون means 'natron, native soda', not 'sodium' (سدیم/سدیوم is the modern element name; Latin natrium supplies only the chemical symbol Na). Nourai's MON:4745 is in Mo'in vol. 4 (foreign words), which is not in the local library, so the citation itself could not be opened.\",\n          \"derivation_fa\": \"«نطرون» در فارسی همان واژهٔ عربی است که بی‌تغییر گرفته شده و املای آن با «ط» نشانهٔ روشنِ معرّب بودن است. دهخدا آن را «(معرب، اِ)» می‌داند و «بورهٔ ارمنی … بورق» معنی می‌کند و از منتهی‌الارب، ذخیرهٔ خوارزمشاهی و ترجمهٔ صیدنه شاهد می‌آورد؛ یعنی این واژه از راه متون داروشناسی و کیمیای عربی سدهٔ سوم تا ششم به فارسی رسیده است. پس مسیر یونانی › عربی › فارسی که نورایی کشیده درست است. تنها معنی‌گذاری او دقیق نیست: نطرون «ناترون/کربنات سدیم طبیعی» است، نه «سدیم» (که در فارسی سدیم/سدیوم است و نشانِ شیمیایی Na آن از natrium لاتینی نو گرفته شده). صفحهٔ مورد استناد (معین ۴۷۴۵، جلد چهارم) در کتابخانهٔ محلی نیست.\",\n          \"sources\": [\n            \"https://abadis.ir/fatofa/%D9%86%D8%B7%D8%B1%D9%88%D9%86/\",\n            \"https://en.wiktionary.org/wiki/%D9%86%D8%B7%D8%B1%D9%88%D9%86\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"MON:4745\", \"status\": \"not_checked\", \"note\": \"Mo'in vol. 4 (foreign words, pp. ~4300-5000) is not among the local scans (only the 2-vol. Adena abridgement, which has no نطرون: grep 'نطرون' MON_part1/2.txt → no hit) and page numbers cannot be mapped on vajehyab/abadis.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"abadis.ir/fatofa/نطرون (Dehkhoda + Mo'in section)\", \"stance\": \"supports\", \"note\": \"'نطرون. [ن َ] (معرب، اِ) بوره ارمنی. (منتهی الارب)… بورق. (المنجد)' — tagged معرب, i.e. from Arabic, with medieval pharmacological sources.\"},\n            {\"src\": \"RCH\", \"where\": \"RCH.txt line 95706\", \"stance\": \"supports\", \"note\": \"Richardson's Persian-Arabic-English dictionary: 'A nitrun or natrun, ناطرون. Natron. Native alkaline salt.' — marked 'A' (Arabic) in a Persian dictionary.\"},\n            {\"src\": \"BQT\", \"where\": \"grep 'نطرون' in BQT_v1..v5_pages.txt\", \"stance\": \"silent\", \"note\": \"Borhan-e Qateʿ has no نطرون entry at all — it is a learned Arabic technical word, not part of the Persian lexicon Borhan records.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Spanish\",\n          \"words\": \"natron\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Spanish natrón 'natron' is an Arabic loan of naṭrūn from the Andalusi/medieval apothecary vocabulary; the doublet anatrón (Medieval Latin and Paracelsus anatron) shows the Arabic definite article agglutinated, an-naṭrūn, the standard sign of an Iberian Arabism. Klein makes Spanish the immediate source of the English word, which is why Nourai draws Spanish here. The caution: the older Iberian and French lexicographers (Lokotsch 1567, Devic, Pihan) record only anatrón for Spanish and let French/English take natron straight from Arabic, and Etymonline dates English natron to the 1680s from French natron (1660s). So the Spanish node is real but is one of two competing routes rather than the certain one.\",\n          \"derivation_fa\": \"اسپانیایی natrón وام‌واژه‌ای عربی از نَطرون است که از راه واژگان داروسازی اندلس و سپس اروپا رفته؛ گونهٔ دیگرش anatrón (در لاتینی میانه و در آثار پاراسلسوس anatron) با حرف تعریف عربی چسبیده است (an-naṭrūn) که نشانهٔ همیشگی عربی‌واژه‌های شبه‌جزیرهٔ ایبری است. کلاین اسپانیایی را سرچشمهٔ بی‌واسطهٔ واژهٔ انگلیسی می‌داند و نورایی نیز همین را کشیده است. با احتیاط پذیرفتنی است: لوکوچ (۱۵۶۷)، دِویک و پیان برای اسپانیایی تنها anatrón را ثبت کرده‌اند و فرانسه و انگلیسی را مستقیم از عربی می‌گیرند، و اتیمولاین natron انگلیسی را دههٔ ۱۶۸۰ از فرانسهٔ natron (۱۶۶۰) می‌داند.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/natron\",\n            \"https://www.etymonline.com/word/natron\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN:1031\", \"status\": \"supports\", \"note\": \"KLN_1966 line 25028 (p.1031): 'natron, n., native sodium carbonate — Fr. Sp. natron, fr. Arab. natrun, fr. Gk. νίτρον' — Klein's 'Fr. Sp.' = 'from Spanish', so Spanish natron < Arabic naṭrūn, and English out of Spanish.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"LKT\", \"where\": \"no. 1567\", \"stance\": \"partial\", \"note\": \"'Aus ar. naṭrūn ergab sich frz. engl. natron … und mit ar. Art. sp. anatron' — Lokotsch's Spanish form is anatrón, and he does not make Spanish the donor of the English word.\"},\n            {\"src\": \"DEV\", \"where\": \"DEV.txt line 1834 s.v. Natron\", \"stance\": \"partial\", \"note\": \"'Natron. Esp. anatron. De l'arabe نطرون natroun' — Devic likewise gives Spanish anatrón only.\"},\n            {\"src\": \"PHN\", \"where\": \"PHN.txt lines 7932-7939, p. 288\", \"stance\": \"partial\", \"note\": \"Pihan s.v. NATRON, s.m. (a.): '… Autrefois on écrivait également ANATRON, et cette variante représente le même mot arabe' with the article — a French Arabism, no Spanish intermediary.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"English\",\n          \"words\": \"natron\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"English natron 'native sodium carbonate' is first recorded in the 1680s. Klein derives it from Spanish natron (hence Nourai's arrow), and Wiktionary keeps the Spanish stage but inserts French: Arabic naṭrūn > Spanish natrón > French natron (1660s) > English natron. Etymonline and Lokotsch skip Spanish and give French natron, itself 'said to be directly from Arabic natrun', as the donor. The word therefore certainly reaches English from a Romance intermediary of the Arabic form, but the immediate donor is more probably French than Spanish; Nourai's arrow is the minority (Klein's) analysis.\",\n          \"derivation_fa\": \"انگلیسی natron «کربنات سدیم طبیعی» از دههٔ ۱۶۸۰ گواهی دارد. کلاین آن را از اسپانیایی natron می‌گیرد و نورایی همین را آورده است؛ ویکی‌واژه مرحلهٔ اسپانیایی را نگه می‌دارد ولی فرانسه را نیز می‌افزاید: عربی نَطرون › اسپانیایی natrón › فرانسهٔ natron (۱۶۶۰) › انگلیسی. اتیمولاین و لوکوچ اسپانیایی را حذف می‌کنند و فرانسه را — که خود «بی‌واسطه از عربی» است — وام‌دهنده می‌دانند. پس واژه بی‌گمان از یک زبان رومی به انگلیسی رسیده، اما وام‌دهندهٔ بی‌واسطه بیشتر فرانسه است تا اسپانیایی؛ خوانش نورایی همان خوانش اقلیّتِ کلاین است. با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/natron\",\n            \"https://en.wiktionary.org/wiki/natron\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives this node no reference; it hangs on the KLN:1031 citation of its Spanish parent.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"p. 1031 s.v. natron\", \"stance\": \"supports\", \"note\": \"'Fr. Sp. natron, fr. Arab. natrun' — English straight from Spanish, as drawn.\"},\n            {\"src\": \"LKT\", \"where\": \"no. 1567\", \"stance\": \"partial\", \"note\": \"'Aus ar. naṭrūn ergab sich frz. engl. natron' — French and English out of Arabic, no Spanish link.\"},\n            {\"src\": \"SKT\", \"where\": \"SKT.txt line 12318 s.v. Nitre\", \"stance\": \"partial\", \"note\": \"'(Nitre and natron are doublets, but applied to different substances.)' — Skeat confirms the doublet relation of nitre/natron but routes both through Arabic.\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"Latin\",\n          \"words\": \"nitrum : natron ; natrium : sodium\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Latin nitrum 'natron, native soda' (Pliny, Vitruvius) is a straight Latinization of Greek νίτρον — Ernout-Meillet: 'nitrum, -ī n.: nitre. Emprunt latinisé au gr. νίτρον, lui-même emprunt à l'égyptien' — with the Latin derivatives nitrāria, nitrātus, nitrōsus and, compounded with sal, the Romance sal nitri > It. salnitro, Sp. salitre 'saltpetre'. That word is correctly placed. natrium, however, is not Latin at all but Modern Latin: Klein, 'natrium, n., sodium (chem.) — ModL. See natron and chem. suff. -ium', i.e. it was coined in the early 19th century (Berzelius' Natrium, whence the symbol Na) on natron, the Arabic-Spanish branch, not on nitrum. Putting it in the Latin box under Greek is thus a conflation of a classical word with a 19th-century chemists' neologism from the other branch of the same chart.\",\n          \"derivation_fa\": \"لاتینی nitrum «ناترون» (در پلینیوس و ویتروویوس) صورت لاتینی‌شدهٔ یونانی νίτρον است؛ ارنو-میه: «وام‌واژهٔ لاتینی‌شده از νίτρον که خود از مصری است»، با مشتقات nitrāria، nitrātus، nitrōsus و ترکیب sal nitri که ایتالیایی salnitro و اسپانیایی salitre «شوره» از آن است. این بخش درست است. اما natrium هرگز لاتینی کلاسیک نیست، بلکه لاتینی نو است: کلاین می‌نویسد «natrium: سدیم (شیمی) — لاتینی نو، بنگرید به natron». این واژه را در آغاز سدهٔ نوزدهم (برتسلیوس) بر پایهٔ natron ساخته‌اند — یعنی از شاخهٔ عربی-اسپانیایی، نه از nitrum — و نشانِ شیمیایی Na از آن است. پس گذاشتن آن در خانهٔ لاتینی زیر یونانی، درهم‌آمیختنِ واژه‌ای کلاسیک با برساختهٔ شیمی‌دانان سدهٔ نوزدهم است. با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/natron\",\n            \"https://en.wiktionary.org/wiki/niter\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN:1049\", \"status\": \"partial\", \"note\": \"KLN_1966 line 25473 (p.~1049) s.v. niter: 'F. nitre, fr. L. nitrum, fr. Gk. νίτρον' — supports nitrum < νίτρον. But natrium is treated at p.1031 (line 25027): 'natrium, n., sodium (chem.) — ModL. See natron and chem. suff. -ium', so the cited page does not support natrium as Latin, and Klein derives it from natron, not nitrum.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"LAT\", \"where\": \"LAT.txt line 41581 s.v. nitrum\", \"stance\": \"supports\", \"note\": \"'nitrum, -ī n.: nitre. Emprunt latinisé au gr. νίτρον, lui-même emprunt à l'égyptien. Dérivés latins: nitraria f.; nitratus, nitreus, nitrosus.'\"},\n            {\"src\": \"LKT\", \"where\": \"no. 1567\", \"stance\": \"supports\", \"note\": \"'hieraus gr. νίτρον, lat. nitrum und mit lat. sal zusammengesetzt: it. salnitro, pg. sp. salitre …'\"},\n            {\"src\": \"KLN\", \"where\": \"p. 1031 s.v. natrium\", \"stance\": \"contradicts\", \"note\": \"'ModL.' — natrium is a modern coinage from natron, not a Latin word inherited from nitrum.\"}\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"French\",\n          \"words\": \"nitre : nitrate of potassium\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Old French nitre is attested from the 13th century, a learned borrowing of Latin nitrum with the usual Latin -um > French -e; the word first meant 'native soda' and only from the late 16th century, through alchemical usage, settled on saltpetre = potassium nitrate, which is Nourai's gloss. On nitre the French chemists then built the whole modern vocabulary: nitrique (1787), nitrate, nitrifier, nitrification (Guyton de Morveau 1787) and nitrogène (coined 1790 by J. A. Chaptal, nitron + -gène 'producing'), which is how the family passes on to English and Persian in the two boxes below.\",\n          \"derivation_fa\": \"فرانسهٔ کهن nitre از سدهٔ سیزدهم گواهی دارد و وام‌واژه‌ای عالمانه از لاتینی nitrum است با تبدیل معمولِ ‎-um‎ لاتینی به ‎-e‎ فرانسوی. نخست به معنی «ناترون» بود و تنها از پایان سدهٔ شانزدهم، در کاربرد کیمیاگران، به معنی «شوره/نیترات پتاسیم» درآمد — همان معنایی که نورایی آورده است. شیمی‌دانان فرانسوی بر پایهٔ nitre همهٔ واژگان نوین را ساختند: nitrique (۱۷۸۷)، nitrate، nitrifier و nitrification (گیتون دو مورو، ۱۷۸۷) و nitrogène (ساختهٔ ژان‌آنتوان شاپتال در ۱۷۹۰ از nitron + گونهٔ ‎-gène‎ «زایا»). ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/nitre\",\n            \"https://www.etymonline.com/word/nitrogen\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN\", \"status\": \"supports\", \"note\": \"KLN_1966 line 25473 s.v. niter/nitre: 'F. nitre, fr. L. nitrum'; line 25475 s.v. nitric: 'F. nitrique, fr. nitre'; nitrification 'F., coined by the French chemist Guyton de Morveau (1737-1816) in 1787'. Klein is cited without a page here and the pages found (1049-1050) say exactly this.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"DEV\", \"where\": \"DEV.txt lines 283, 297, 307\", \"stance\": \"partial\", \"note\": \"Devic discusses only the Arabic words confused with nitre in French alchemy (algali, alaurat < al-bawraq) — he does not treat nitre itself, since it is a Latin-Greek word, not an Arabism: silent on the arrow but consistent with it.\"},\n            {\"src\": \"SKT\", \"where\": \"SKT.txt line 12318\", \"stance\": \"supports\", \"note\": \"'Nitre. (F. – L. – Gk. – Arab.) F. nitre. — L. nitrum. — Gk. νίτρον' — French from Latin, as drawn (Skeat's further Arabic step is wrong).\"}\n          ]\n        },\n        {\n          \"id\": 9,\n          \"lang\": \"Persian\",\n          \"words\": \"nîtrîc «نیتریک اسید» : nitric ; nîtrât «نیترات» : nitrate ; nîtrogen «نیتروژن» : nitrogen\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"All three are 20th-century French loans in Persian, taken over when Iranian secondary and medical education was built on French models (Dar al-Fonun and after), which is why they keep the French shapes nitrique/nitrate/nitrogène rather than the English ones and why the -ژ- of نیتروژن renders French [ʒ] in -gène. Dehkhoda/Mo'in tag them accordingly: 'نیتروژن. [رُ ژِ] (فرانسوی، اِ) ازت' and 'نیترات. (فرانسوی، اِ) … (فرهنگ فارسی معین)'. Note the doublet situation: alongside the French loans Persian also has the older Arabic-mediated ازت (French azote, Lavoisier's name for the same element) and the native شوره for saltpetre. اسید in نیتریک اسید is itself the French/English acide/acid.\",\n          \"derivation_fa\": \"این سه واژه وام‌واژه‌های فرانسوی سدهٔ چهاردهم/بیستم‌اند و در دورهٔ برپایی آموزش نوین ایران (دارالفنون و پس از آن) که الگوی آموزشی و اصطلاح‌شناسی آن فرانسوی بود به فارسی آمدند؛ به همین سبب صورت فرانسوی nitrique/nitrate/nitrogène را نگه داشته‌اند نه صورت انگلیسی را، و «ژ» در «نیتروژن» همان [ʒ] فرانسوی در ‎-gène‎ است. دهخدا و معین نیز همین را می‌گویند: «نیتروژن. [رُ ژِ] (فرانسوی، اِ) ازت» و «نیترات. (فرانسوی، اِ) … (فرهنگ فارسی معین)». نکته اینکه فارسی در برابر این‌ها «ازت» (از azote فرانسوی) و «شوره» را هم دارد که دوگانهٔ همان مفاهیم‌اند. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://abadis.ir/fatofa/%D9%86%DB%8C%D8%AA%D8%B1%D9%88%DA%98%D9%86/\",\n            \"https://abadis.ir/fatofa/%D9%86%DB%8C%D8%AA%D8%B1%D8%A7%D8%AA/\",\n            \"https://www.etymonline.com/word/nitrogen\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"MON:4880\", \"status\": \"partial\", \"note\": \"The print page (Mo'in vol. 4, foreign words) is not in the local library, but the online Mo'in/Dehkhoda text of both headwords is explicit and is quoted from Mo'in by name: 'نیترات. (فرانسوی، اِ) … ترکیبی که از اسید نیتریک با یک فلز یا یک باز نتیجه می‌شود. (فرهنگ فارسی معین)'; 'نیتروژن. [رُ ژِ] (فرانسوی، اِ) ازت'. So Mo'in does tag them French, as the arrow requires; only the page number is unverifiable.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"abadis.ir/fatofa/نیتروژن and /نیترات (فرهنگ معین section)\", \"stance\": \"supports\", \"note\": \"both tagged '(فرانسوی، اِ)', the نیترات gloss attributed to فرهنگ فارسی معین.\"},\n            {\"src\": \"BQT\", \"where\": \"grep 'نیتر' in BQT_v1..v5_pages.txt\", \"stance\": \"silent\", \"note\": \"Borhan-e Qateʿ (17th c.) naturally has none of these; MON_part2.txt uses نیترات/اسید نیتریک freely in definitions (lines 7347, 25909, 79534) but as modern chemistry vocabulary without etymology.\"}\n          ]\n        },\n        {\n          \"id\": 10,\n          \"lang\": \"English\",\n          \"words\": \"nitre, nitrate, nitric, nitrogen, nitroglycerine\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English niter/nitre appears c. 1400 in the sense 'native sodium carbonate' from Old French nitre (13th c.); the rest are 18th-19th century adoptions of the French chemical vocabulary built on it: nitric from F. nitrique (see Klein s.v. nitric, 'F. nitrique, fr. nitre'), nitrate from F. nitrate (or formed on niter with -ate), nitrogen 1794 from F. nitrogène (Chaptal 1790), and nitroglycerine 1857 from the combining form nitro- (Greek νιτρο-) + glycerine. All five therefore go back through French nitre to Latin nitrum and Greek νίτρον, as drawn.\",\n          \"derivation_fa\": \"انگلیسی nitre/niter در حدود ۱۴۰۰ م. به معنی «کربنات سدیم طبیعی» از فرانسهٔ کهن nitre (سدهٔ ۱۳) وارد شده است؛ باقی واژه‌ها وام‌گیری سدهٔ هجدهم و نوزدهم از واژگان شیمی فرانسه‌اند: nitric از nitrique فرانسوی (کلاین: «F. nitrique, fr. nitre»)، nitrate از nitrate فرانسوی، nitrogen در ۱۷۹۴ از nitrogène (ساختهٔ شاپتال در ۱۷۹۰) و nitroglycerine در ۱۸۵۷ از پیش‌وندِ nitro- (یونانی νιτρο-) + glycerine. پس هر پنج واژه از راه فرانسه به لاتینی nitrum و یونانی νίτρον می‌رسند؛ ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/nitre\",\n            \"https://www.etymonline.com/word/nitrogen\",\n            \"https://en.wiktionary.org/wiki/niter\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"not_checked\", \"note\": \"Nitre is a Semitic/Egyptian loanword, so it has no entry in the AHD Indo-European appendix (grep 'nitr' AHD_watkins1985.txt → nothing); Nourai's 'AHD' must point to the main dictionary body, which is not in the local library (the local AHD file is the Watkins 1985 IE-roots volume only).\"},\n            {\"ref\": \"KLN\", \"status\": \"supports\", \"note\": \"KLN_1966 lines 25473-25480 (pp.1049-1050): 'niter, nitre, n., nitrate of potassium — F. nitre, fr. L. nitrum'; 'nitrate — Formed fr. niter with chem. suff. -ate'; 'nitric — F. nitrique, fr. nitre'; 'nitro-, before a vowel nitr- … Gk. νιτρο-, fr. νίτρον'.\"\n            }\n          ],\n          \"consulted\": [\n            {\"src\": \"SKT\", \"where\": \"SKT.txt line 12318 s.v. Nitre\", \"stance\": \"supports\", \"note\": \"'Der. nitro-gen, that which produces nitre, from γεν-, base of γίγνομαι, to produce.'\"},\n            {\"src\": \"LKT\", \"where\": \"no. 1567 and the chronological word-list (LKT.txt lines 5852, 6105, 7440)\", \"stance\": \"supports\", \"note\": \"Lokotsch dates 'Natron 1567' and 'nitrum 1567' in the European loan-chronology and derives them from the Hebrew/Egyptian word via Greek and Latin.\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 2,\n      \"root\": \"Nobh, Ombh, Mbh\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *h₃nebʰ- 'navel, hub' (ablaut grades *h₃nobʰ-, *h₃embʰ-/*h₃m̥bʰ-)\",\n      \"note\": \"Pokorny IEW pp. 314-315 heads the entry '1. (enebh-), embh-, ombh-, nō̆bh- (nēbh-?), m̥bh- \\\"Nabel\\\", mehrfach mit l-Formantien' — Nourai's three shapes 'Nobh, Ombh, Mbh' are three of Pokorny's own ablaut grades, the language label 'Indo-European' is right, the gloss 'nave, hub' is Pokorny's 'Nabel' plus the derived wheel-hub sense, and POK:314 is the exact page (in POK_01.txt the entry begins at the foot of the page whose next marker is '315'). Walde-Pokorny I 130 has the identical heading; Watkins/AHD prints 'nobh-. Also ombh-. Navel; later also \\\"central knob\\\", boss of a shield, hub of a wheel. [Pok. 1. (enebh-) 314.]' Modern reconstruction adds the initial laryngeal — Wiktionary and Kölligan (2018) write *h₃nebʰ-, with *h₃nobʰ-eh₂ > PGmc *nabō, *h₃nóbʰ-i-s > Skt nābhi-, *h₃nṓbʰ-s ~ *h₃nebʰ-és > PIr. *Hnā́fah, *h₃émbʰ-ō > Lat. umbō — but that is a notational refinement of exactly this root, not a different one.\",\n      \"note_fa\": \"ریشهٔ هندواروپایی آغازین *h₃nebʰ- «ناف، توپیِ چرخ». پوکورنی (صفحه‌های ۳۱۴-۳۱۵) سرواژه را چنین می‌آورد: «(enebh-), embh-, ombh-, nō̆bh- (nēbh-?), m̥bh- «Nabel»» — یعنی سه صورتی که نورایی آورده (Nobh, Ombh, Mbh) همان گونه‌های آواگردیِ خودِ پوکورنی است، برچسب «هندواروپایی» درست است و معنای «ناف/توپی» نیز درست. والده-پوکورنی (جلد ۱، ص ۱۳۰) همین سرواژه را دارد و واتکینز در پیوستِ AHD می‌نویسد «nobh-، همچنین ombh-: ناف؛ سپس برجستگی میانی، ناف سپر، توپی چرخ». ریشه‌شناسی امروزی حنجریِ آغازی را می‌افزاید (*h₃nebʰ-) و گونه‌های آواگردی را چنین می‌دهد: *h₃nobʰ-eh₂ › ژرمنی *nabō، *h₃nóbʰ-i-s › سنسکریت nābhi-، *h₃nṓbʰ-s ~ *h₃nebʰ-és › ایرانی آغازین *Hnā́fah، *h₃émbʰ-ō › لاتینی umbō. این تنها اصلاحِ نگارشی همان ریشه است. ادعای نورایی درست است.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%83neb%CA%B0-\",\n        \"https://en.wiktionary.org/wiki/navel\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:314\", \"status\": \"supports\", \"note\": \"POK_01.txt leaf 327 (the page marker '315' follows a few lines below, so the entry opens on p.314): '1. (enehh-), emhh-, ombh-, nobh- (nebh-?), m̥bh- ,Nabel', mehrfach mit i-[= l-]Formantien.' Nourai's page is exact.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"WLD\", \"where\": \"Bd. I p. 130 (WLD_Bd1_pages.txt leaf 138, header '130')\", \"stance\": \"supports\", \"note\": \"'1. (enebh-) ombh-, nobh- (nebh-?), mbh- \\\"Nabel\\\", mehrfach mit l-Formantien' — the same heading Pokorny later reprinted.\"},\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. nobh-\", \"stance\": \"supports\", \"note\": \"'nobh-. Also ombh-. Navel; later also \\\"central knob,\\\" boss of a shield, hub of a wheel. … [Pok. 1. (enebh-) 314.]' — same root, same cross-reference to Pokorny 314.\"},\n        {\"src\": \"IEC\", \"where\": \"IEC.txt line 11784\", \"stance\": \"supports\", \"note\": \"Mann: 'nobh- \\\"nave, navel, hub, centre\\\". WP I, 130. Skt. nábhyam n.; Av. nabis f. \\\"navel\\\"; Per. naf \\\"navel, middle\\\"; Oss. Dig. naffä; OHG naba f. \\\"hub, nave\\\"; OE nafu …'\"},\n        {\"src\": \"SYN\", \"where\": \"Buck, ch. 4.43 NAVEL (SYN.txt lines 3740, 6448)\", \"stance\": \"supports\", \"note\": \"'Av. nafa- \\\"navel\\\" and \\\"family, kindred\\\": Skt. nabhi- \\\"navel\\\" and \\\"relationship\\\", Grk. ὀμφαλός \\\"navel\\\", etc. Walde-P. 1.130. Barth. 1062.' — Buck's comparative table lists exactly Nourai's set (OE nafola, ME navele, NE navel, Lat. umbilicus, Av. nafa-, Skt. nabhi-).\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan / Old Persian\",\n          \"words\": \"nâf, nâfah, nafa, nâfô : nave\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"All four forms are Avestan, and Bartholomae's Altiranisches Wörterbuch col. 1062 has them together: 'j. nāfa- m. \\\"Nabel\\\"; g. a) \\\"Verwandtschaft, Familie\\\" … Vgl. nāfah- und nabānazdišta-: np. nāf \\\"Nabel\\\"'; 'j. nafah- n. \\\"Verwandtschaft, Familie\\\"' (Yt. 13.87); 'j. nāfya- Adj. \\\"familienangehörig\\\"'. nāfō is the nominative singular of the s-stem (Pokorny quotes 'av. nāfō'). The Iranian -f- where the cognates show -bh- (Skt nābhi-, Av. nabā-nazdišta-) puzzled Horn ('gehen auf indog. bh zurück, während die übrigen Formen auf ph weisen') and Ernout-Meillet ('L'iranien a une forme populaire à *-ph-'); the modern explanation is that -f- was generalized from the nominative *Hnā́fš < *h₃nṓbʰ-s, where *bʰ+s devoiced regularly, and the stem was then thematized as Proto-Iranian *Hnā́fah. The one thing to correct: the label 'Old Persian'. No Old Persian word for 'navel' is attested — Kent's lexicon has no nāfa- (the OP naf-/naθ- of DNb is 'to harm'); the forms are Avestan only, with the Old-Iranian stage reconstructed.\",\n          \"derivation_fa\": \"هر چهار صورت اوستایی‌اند و بارتولمه در «فرهنگ ایرانی باستان» ستون ۱۰۶۲ همه را کنار هم آورده است: «nāfa- (مذکر) «ناف»، در گاهانی «خویشاوندی، خاندان» … مقایسه کنید با nāfah- و nabā-nazdišta-؛ فارسی نو ناف»؛ «nafah- (خنثی) «خویشاوندی، خاندان»» (یشت ۱۳:۸۷)؛ «nāfya- «خویشاوند»». صورت nāfō همان نهادی مفردِ ستاکِ ‎-s‎ است که پوکورنی نیز «av. nāfō» می‌آورد. اینکه در ایرانی «ف» آمده در جایی که سنسکریت nābhi- و اوستایی nabā-nazdišta- «bh» دارند، هرن را به شگفت آورده بود («صورت‌های دیگر بر ph دلالت دارند») و ارنو-میه هم آن را «صورت عامیانه با *-ph-» خوانده؛ توضیح امروزی این است که «ف» از حالت نهادیِ *Hnā́fš ‹ *h₃nṓbʰ-s (که در آن bʰ+s قانوناً بی‌واک شده) به همهٔ صرف گسترش یافته و سپس ستاک به‌صورت ایرانی آغازین *Hnā́fah درآمده است. تنها نکتهٔ نادرست برچسبِ «پارسی باستان» است: هیچ واژهٔ پارسی باستان برای «ناف» گواهی ندارد و در واژه‌نامهٔ کنت چنین واژه‌ای نیست (naθ- در کتیبهٔ داریوش به معنی «آسیب رساندن» است).\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/Hn%C4%81%CC%81fah\",\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%83neb%CA%B0-\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:314\", \"status\": \"supports\", \"note\": \"POK_01.txt leaf 327: 'av. nabā-nazdišta- \\\"der verwandtschaftlich nächststehende\\\", daneben mit ar. ph: av. nāfō, npers. nāf \\\"Nabel\\\"' — Pokorny p.314/315 gives Av. nāfō and NP nāf under this root, exactly as drawn. He labels them Avestan and Modern Persian; he says nothing about Old Persian.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"col. 1062 (BRT.txt lines 18878-18893, the marker '1063 nāman-' follows)\", \"stance\": \"supports\", \"note\": \"'• j. nāfa- m. \\\"Nabel\\\": g. a) \\\"Verwandtschaft, Familie\\\" … Vgl. nāfah- und nabānazdišta-: — np. nāf \\\"Nabel\\\"; ai. vgl. nābhya- \\\"Nabel\\\"' and '• j. nafah- n. \\\"Verwandtschaft, Familie\\\" … Yt. 13.87'. All of Nourai's Avestan forms, on the column Mo'in also cites.\"},\n            {\"src\": \"KNT\", \"where\": \"Kent, Old Persian lexicon (grep 'naf' KNT.txt)\", \"stance\": \"silent\", \"note\": \"No OP nāfa-/nāf 'navel'; the only naf-/naθ- in Kent is the verb of DNb 20 vināθayaiš 'you should do harm'. The 'Old Persian' half of the node label is unsupported.\"},\n            {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. umbilicus (LAT.txt lines 69515-69522)\", \"stance\": \"supports\", \"note\": \"'L'iranien a une forme populaire à *-ph-: av. nāfa \\\"nombril\\\" (pers. nāf), nāfya- \\\"de famille\\\"' — the same Avestan set, with the -f- noted as the Iranian peculiarity.\"},\n            {\"src\": \"PHD\", \"where\": \"MacKenzie p. 57 s.v. nāf (PHD.txt line 494)\", \"stance\": \"supports\", \"note\": \"'nāf [w | M mp] family. ~ag [-g | N nāf(a)] navel' — the Middle Persian continuation of the Avestan word, with both the 'family' and the 'navel' senses, exactly the intermediate stage the arrow to Persian passes through.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"nâf «ناف» : nave ; nâfeh «نافه» : musk bag\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"NP ناف nāf 'navel; hub of a wheel; middle, centre' continues Middle Persian nāf (Manichaean nʾp) 'family' / nāfag 'navel' — MacKenzie p.57: 'nāf … family. ~ag … navel' — from Proto-Iranian *Hnā́fah; the Old-Iranian long ā and final -ah were lost in the regular MP apocope (*Hnāfah > nāf), and NP inherits the Pahlavi form unchanged, while nāfag lost its -g in the usual NP way (MP -ag > NP -a/-e), giving نافه. The kinship sense of the Avestan and Pahlavi word survives in NP نواده/نبیره 'grandchild, descendant' (Mo'in's note in Borhan-e Qateʿ lists نواده، نبیر، نبیره beside ناف، نافه), and the 'centre' sense in the idioms ناف زمین/ناف عالم = Mecca. نافه is a straightforward semantic derivative: the musk pod of the Moschus deer sits under the belly skin at the navel — Borhan's footnote spells it out: 'کیسه‌ای مشکین به‌اندازهٔ تخم مرغی که در زیر پوست شکم آهوی خطا قرار دارد و در آن مشک وجود دارد (به همین مناسبت آن را نافه گویند)'. Cognate dialect forms confirm the whole set: Kurdish nāw/nāfik, Ossetic naffä, Baluchi napag/nafag/nafay, Armenian nafat 'musk pod' (borrowed from Persian).\",\n          \"derivation_fa\": \"«ناف» فارسی نو دنبالهٔ فارسی میانهٔ nāf (مانوی nʾp) «خاندان» و nāfag «ناف» است — مکنزی، ص ۵۷: «nāf … خاندان؛ nāfag … ناف» — و آن از ایرانی آغازین *Hnā́fah می‌آید؛ پایانهٔ ‎-ah‎ ایرانی باستان در فارسی میانه افتاده (*Hnāfah › nāf) و فارسی نو همان صورت پهلوی را نگه داشته است، و nāfag با فرسایش معمولِ ‎-ag‎ پهلوی به ‎-e‎ فارسی نو، «نافه» شده است. معنای «خویشاوندی» که در اوستایی و پهلوی بود، در «نواده، نبیر، نبیره» بازمانده است — حاشیهٔ معین بر برهان قاطع (ص ۲۱۰۰) همین‌ها را کنار «ناف» و «نافه» می‌آورد — و معنای «میان/مرکز» در «ناف زمین» و «ناف عالم» (کنایه از مکه). «نافه» گسترشِ معنایی سادهٔ «ناف» است: کیسهٔ مشک آهوی مشکی زیر پوست شکم و نزدیک ناف است؛ حاشیهٔ برهان قاطع می‌گوید «کیسه‌ای مشکین به‌اندازهٔ تخم‌مرغی که در زیر پوست شکم آهوی خطا قرار دارد و در آن مشک وجود دارد (به همین مناسبت آن را «نافه» گویند)». صورت‌های گویشی هم‌ریشه نیز این را تأیید می‌کنند: کردی nāw/nāfik، آسی naffä، بلوچی napag/nafag، ارمنی nafat (وام از فارسی). ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%86%D8%A7%D9%81\",\n            \"https://en.wiktionary.org/wiki/%D9%86%D8%A7%D9%81%D9%87\",\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/Hn%C4%81%CC%81fah\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN:1032\", \"status\": \"supports\", \"note\": \"KLN_1966 lines 25057-25058: 'nave, n., the hub of a wheel' (p.1032) and 'navel, n. … fr. I.-E. base *ombh-, nābh-, *mbh-, whence also OI. nābhyam \\\"nave (hub)\\\", nābhih \\\"navel, nave, relationship\\\", … Avestic naba-nazdishta \\\"next of kin\\\", Avestic nafa, ModPers. nāf …' (the page marker 1033 stands at line 25059, so nave is p.1032). Klein lists ModPers. nāf under this root, as the arrow requires.\"},\n            {\"ref\": \"HRN:228\", \"status\": \"supports\", \"note\": \"HRN.txt line 8853, on the page whose marker '— 228 —' stands at line 8824: '1020. nāf \\\"Nabel\\\", nāfe, — g. nafk. — aw. nafah- \\\"Geschlecht\\\", vergl. nāfya- \\\"Verwandtschaft\\\"; phlv. nafak, nāf \\\"Nabel\\\" … kurd. nāw \\\"Nabel\\\"; afgh. nūm; oss. d. naffā; bal. napag, nafag, n. nafay.' Horn's entry no. 1020 covers BOTH of Nourai's words (nāf and nāfe) on exactly p.228.\"},\n            {\"ref\": \"BQT:2100\", \"status\": \"supports\", \"note\": \"BQT vol.4 pdf page 183 = printed p.2100 (page marker '- ۹۹' on pdf 182 and the arithmetic pdf+1917 both fix it): the ناف entry, with Mo'in's footnote 2: 'اوستا nāfa- «بارتولمه ۱۰۶۲»؛ سانسکریت nābhi- … پهلوی nāf (ناف) … کردی nāw (ناف، درون) … نیز در اوستا nāfah-، nāfya-؛ پارسی باستان و سانسکریت nābhi-، لاتینی umbo، آلمانی Nabel، انگلیسی navel. فارسی: ناف، نافه، نواده، نبیر، نبیره'. This single footnote is in effect Nourai's whole chart; the نافه footnote follows on p.2101.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie p.57 (PHD.txt line 494) and the English index (line 2893)\", \"stance\": \"supports\", \"note\": \"'nāf [w | M mp] family. ~ag [-g | N nāf(a)] navel'; index: 'navel nāfag'. The MP stage of both Persian words.\"},\n            {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien, p.162 (HUB.txt lines 6509-6511) and p.~44 (line 3548)\", \"stance\": \"supports\", \"note\": \"'nāf, nāfa \\\"Nabel\\\", phl. nafak, bal. napag, nb. nafay, zd. nāfa \\\"Nabel\\\" ZPGl. p.10, \\\"Geschlecht\\\" yt. 13,87 (= arisch *naphas-) neben zd. nabānazdišta-, skr. nābhi- \\\"Nabel\\\"'; and 'np. nāfa \\\"Nabel, Moschus(beutel)\\\"' — Hübschmann has the musk-bag sense explicitly.\"},\n            {\"src\": \"BQT\", \"where\": \"vol.4 printed p.2101 (pdf 184), footnote to نافه\", \"stance\": \"supports\", \"note\": \"'نافه - بفتح فاء (در لهجهٔ کنونی بکسر). پهلوی nāfa (ناف) … ارمنی nafat (کیسهٔ مشک)، افغانی nāfa (کیسهٔ مشک) «هوبشمان ۱۶۲» … کیسه‌ای مشکین … در زیر پوست شکم آهوی خطا … (بهمین مناسبت آنرا «نافه» گویند)' — nāfeh from nāf, with the musk-bag semantics spelled out.\"},\n            {\"src\": \"NYB\", \"where\": \"grep 'nāf' NYB_vol2_glossary.txt\", \"stance\": \"silent\", \"note\": \"Nyberg's glossary (limited to his text selection) has no nāf entry — a silent result, not a contradiction.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Sanskrit\",\n          \"words\": \"nâbh, nâbhi : nave, family, race\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Sanskrit नाभि nā́bhi- f. means both 'navel' and 'nave (hub) of a wheel' and, by the same metaphor of kinship radiating from a centre, 'relationship, family' (Pokorny: 'nābhi- f. \\\"Nabel, Nabe, Verwandtschaft\\\"'); beside it stand नभ्य nábhya- n. 'nave of a wheel' and the (unattested but reconstructed) nābhīla- n. 'pubic region, navel cavity'. Ernout-Meillet note that Skt nābhiḥ 'sert aussi à désigner la parenté', which is Nourai's 'family, race'. His 'nâbh' is the bare stem nābh- as cited in the comparative literature (Bartholomae 'ai. nabh- f.'), not a separate word. The forms preserve the inherited voiced aspirate *bʰ regularly (*h₃nóbʰ-i-s > Proto-Indo-Iranian *Hnā́bʰiš > Skt nā́bhi-), which is precisely why they differ from the Iranian -f- forms of node #1.\",\n          \"derivation_fa\": \"سنسکریت नाभि (nā́bhi-، مؤنث) هم «ناف» است و هم «توپیِ چرخ»، و با همان استعارهٔ خویشاوندی که از یک مرکز پراکنده می‌شود، «نسبت، خاندان» نیز معنی می‌دهد؛ پوکورنی می‌نویسد: «nābhi- (مؤنث) «ناف، توپی، خویشاوندی»»، و در کنارش नभ्य (nábhya-، خنثی) «توپی چرخ» و nābhīla- «ناحیهٔ زیر شکم، گودی ناف» را می‌آورد. ارنو-میه نیز یادآور می‌شود که nābhiḥ «برای نامیدن خویشاوندی هم به کار می‌رود» — همان «family, race» نورایی. صورت «nâbh» او همان ستاکِ برهنهٔ nābh- است که در ادبیات مقایسه‌ای نقل می‌شود (بارتولمه: «ai. nabh- f.»)، نه واژه‌ای جداگانه. در سنسکریت *bʰ هندواروپایی قانوناً نگه داشته شده (*h₃nóbʰ-i-s › هندوایرانی آغازین *Hnā́bʰiš › nā́bhi-) و همین سبب تفاوت آن با «ف» ایرانی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%83neb%CA%B0-\",\n            \"https://en.wiktionary.org/wiki/navel\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:314\", \"status\": \"supports\", \"note\": \"POK_01.txt leaf 327: 'Ai. nābhya- n. \\\"Nabe\\\", nābhi- f. \\\"Nabel, Nabe, Verwandtschaft\\\", nābhīla- n. (unbelegt) \\\"Schamgegend, Nabelvertiefung\\\"' — all three of Nourai's glosses ('nave, family, race') on the cited page.\"},\n            {\"ref\": \"SNS:258\", \"status\": \"not_found\", \"note\": \"SNS (Tavoosi's glossary of Shayast ne Shayast) does have the word — SNS_pages.txt line 10244 / SNS.txt line 14504: an entry 'nāfag' citing 'av. nafah-, nāf-' and 'Barth. 1062' — but the printed page cannot be mapped: refs_online.json says of SNS 'page offset not determined (OCR too poor to read printed numbers)', and the hit sits on 0-based leaf 145 of 243, so p.258 cannot be confirmed or refuted. Note also that a Pahlavi text-glossary is an odd authority for a Sanskrit form.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"WLD\", \"where\": \"Bd. I p. 130\", \"stance\": \"supports\", \"note\": \"'As.[= Ai.] nābhya- n. \\\"Nabe\\\", nābhi- f. \\\"Nabel, Nabe, Verwandtschaft\\\", nābhīla- n. (unbelegt) \\\"Schamgegend, Nabelvertiefung\\\"' — the same three senses.\"},\n            {\"src\": \"KLN\", \"where\": \"p. 1033 s.v. navel\", \"stance\": \"supports\", \"note\": \"'OI. nābhyam \\\"nave (hub)\\\", nābhih \\\"navel, nave, relationship\\\", nābhilam \\\"umbilical depression\\\"'.\"},\n            {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. umbilicus\", \"stance\": \"supports\", \"note\": \"'La forme principale est indiquée par l'indo-iranien: skr. nabhiḥ \\\"nombril, moyeu\\\" … (réd. nabhiḥ sert aussi à désigner la parenté); le dérivé neutre nābhyam signifie seulement \\\"moyeu\\\".'\"},\n            {\"src\": \"SYN\", \"where\": \"Buck 4.43 (SYN.txt line 3740)\", \"stance\": \"supports\", \"note\": \"'Skt. nabhi- \\\"navel\\\" and \\\"relationship\\\" … Walde-P. 1.130. Barth. 1062.'\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Germanic\",\n          \"words\": \"nabo\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"'Nabo' is the Proto-Germanic reconstruction *nabō f. 'hub of a wheel' (< PIE *h₃nobʰ-eh₂), the form Watkins prints as 'Germanic *nabo' — hence Nourai's spelling — and which appears in the daughters as OHG naba, OS naba, OE nafu/nafa, ON nöf, MDu. nave, Du. naaf, MHG/G Nabe, Dan./Swed. nav; the derivative *nabalō (PIE *h₃nobʰ-alo-) gives OHG nabalo, OE nafela, ON nafli, G Nabel 'navel'. Kroonen's Etymological Dictionary of Proto-Germanic (pp. 380-381) reconstructs *nabō- for the same set, and Finnish napa 'navel, hub' is an early loan from it. Note that Nourai's arrow makes the Germanic form a direct daughter of the root, which is correct: Germanic keeps the o-grade *nobh- with the *bʰ > b of Grimm's law and the ā-stem ending.\",\n          \"derivation_fa\": \"«nabo» همان بازسازیِ ژرمنی آغازین *nabō (مؤنث) «توپیِ چرخ» است (از *h₃nobʰ-eh₂ هندواروپایی) — واتکینز نیز «Germanic *nabo» می‌نویسد و نورایی همان را آورده — که در زبان‌های دختر چنین بازمانده است: آلمانی علیای باستان naba، انگلیسی باستان nafu/nafa، نورسی کهن nöf، هلندی naaf، آلمانی Nabe، دانمارکی و سوئدی nav؛ و مشتقِ *nabalō (از *h₃nobʰ-alo-) آلمانی علیای باستان nabalo، انگلیسی باستان nafela، نورسی nafli و آلمانی Nabel «ناف» را داده است. کرونن در «فرهنگ ریشه‌شناسی ژرمنی آغازین» (ص ۳۸۰-۳۸۱) همین *nabō- را بازمی‌سازد و napa فنلاندی وام‌واژه‌ای کهن از آن است. ژرمنی درجهٔ o ریشه (*nobh-) را نگه داشته و *bʰ بر پایهٔ قانون گریم به b بدل شده است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%83neb%CA%B0-\",\n            \"https://en.wiktionary.org/wiki/nave\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt s.v. nobh-: '1. Germanic *nabo in: a. Old English nafu, nafa, hub of a wheel: NAVE²; b. compound *nabō-gaizaz, tool for piercing wheel hubs …: AUGER. … 3. Suffixed form *nobh-alo- in Germanic *nabalō in Old English nafela, navel: NAVEL.' Watkins' 'Germanic *nabo' is verbatim Nourai's node.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"p. 315\", \"stance\": \"supports\", \"note\": \"'ahd. naba, ags. nafu, aisl. nöf \\\"Radnabe\\\" (auch in ahd. naba-ger, ags. nafu-gār, aisl. nafarr \\\"grober Bohrer\\\"), ahd. nabalo, ags. nafela, aisl. nafli \\\"Nabel\\\"'.\"},\n            {\"src\": \"IEC\", \"where\": \"IEC.txt line 11784\", \"stance\": \"supports\", \"note\": \"Mann s.v. nobh-: 'OHG naba, f. \\\"hub, nave\\\"; OE nafu, ON nöf, f. id. … Finn. LW napa \\\"navel, hub\\\"'.\"},\n            {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. umbilicus\", \"stance\": \"supports\", \"note\": \"'en germanique: v.h.a. nabo \\\"moyeu\\\" à côté de nabalo \\\"nombril\\\"' — the OHG form in the very shape Nourai prints.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"English\",\n          \"words\": \"nave, navel, auger\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"All three descend from the Germanic node. (1) nave 'hub of a wheel' < ME nave < OE nafu (Klein p.1032). (2) navel < ME navel < OE nafela, the *-alo- derivative (Klein p.1033). (3) auger is the interesting one: OE nafugār, a compound of nafu 'nave' + gār 'spear, piercing tool' (Watkins' *nabō-gaizaz, 'tool for piercing wheel hubs'), i.e. literally a hub-borer; ME nauger then lost its initial n- by false division of 'a nauger' as 'an auger' — the same metanalysis that produced adder from OE nǣdre and umpire from noumpere. Nourai is right to attach all three to the Germanic hub-word, and it is worth noting the English homograph nave 'central part of a church' is unrelated (< Latin nāvis 'ship').\",\n          \"derivation_fa\": \"هر سه واژه از خانهٔ ژرمنی می‌آیند. ۱) nave «توپی چرخ» از انگلیسی میانهٔ nave و آن از انگلیسی باستان nafu (کلاین، ص ۱۰۳۲). ۲) navel از انگلیسی میانهٔ navel و آن از انگلیسی باستان nafela، همان مشتقِ ‎*-alo-‎ (کلاین، ص ۱۰۳۳). ۳) auger شنیدنی‌ترین است: انگلیسی باستان nafugār، مرکب از nafu «توپی» و gār «نیزه، ابزار سوراخ‌کن» (بازسازیِ واتکینز: *nabō-gaizaz «ابزار سوراخ کردن توپیِ چرخ»)، یعنی «مته‌ای برای توپیِ چرخ»؛ سپس در انگلیسی میانه «a nauger» به‌غلط «an auger» بخش شد و «ن» آغازی افتاد — همان بخش‌بندیِ نادرستی که adder را از nǣdre و umpire را از noumpere ساخت. ادعای نورایی درست است. یادآوری: nave به معنی «شبستان کلیسا» واژهٔ دیگری است و از nāvis لاتینی «کشتی» می‌آید.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/nave\",\n            \"https://en.wiktionary.org/wiki/auger\",\n            \"https://en.wiktionary.org/wiki/navel\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives this node no reference; it rests on the AHD citation of its Germanic parent, which does list NAVE², NAVEL and AUGER under nobh-.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. nobh- and the index (lines 1266, 1902, 2432)\", \"stance\": \"supports\", \"note\": \"index entries 'AUGER nobh-', 'NAVE² nobh-', 'NAVEL nobh-, nau-²', 'UMBILICUS nobh-' — the same three English words, plus the note that NAVE¹ 'church' belongs to nau-².\"},\n            {\"src\": \"KLN\", \"where\": \"pp. 1032-1033 s.v. nave, navel; p. 82 s.v. auger\", \"stance\": \"supports\", \"note\": \"'nave, n., the hub of a wheel. — ME., fr. OE. nafu … The nave of the wheel was compared to the navel of the body'; 'auger, n. — ME. auger, earlier nauger, fr. OE. nafugar, which is compounded of nafu \\\"nave of a wheel\\\" and gar \\\"spear\\\" … The loss of the initial n is due to a misdivision of ME. a nauger into an auger.'\"},\n            {\"src\": \"SYN\", \"where\": \"Buck 4.43 NAVEL (SYN.txt line 6448)\", \"stance\": \"supports\", \"note\": \"the table lists 'OE nafola, ME navele, NE navel, Du. navel, OHG nabalo, NHG nabel' under one heading with 'Av. nafa-, Skt. nabhi-'.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Latin\",\n          \"words\": \"umbilicus : navel\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Latin umbilīcus 'navel' (and by analogy any small round boss: the knob of a book-roll, the gnomon of a sundial, umbilīcus Veneris the plant navelwort) is the *ombh-/*m̥bh- grade of the root with two suffixes, the -l- of ungula-type body-part words plus a thematic *-ko-, i.e. *h₃m̥bʰ-el-iko-; beside it stands the suffixless umbō, -ōnis 'boss of a shield' (< *h₃émbʰ-ō, so de Vaan 2008 p.639). Ernout-Meillet make the point Nourai's arrow needs: 'L'élément -l- de umbilicus se retrouve dans v.h.a. nabalo, v.irl. imbliu, gr. ὀμφαλός' and 'L'o prothétique de umbilicus, qui est exceptionnel, sans doute populaire, est comparable à celui de unguis' — that is, umbilīcus is a regular member of this root's family, and the initial u- is the prothetic vowel of the *ombh- grade (Nourai's second root shape). Greek ὀμφαλός is the exact cognate.\",\n          \"derivation_fa\": \"لاتینی umbilīcus «ناف» (و به قیاس، هر برجستگی گِردِ کوچک: سرِ چوبِ طومار، شاخصِ ساعت آفتابی، umbilīcus Veneris نامِ گیاهی) بر پایهٔ درجهٔ *ombh-/*m̥bʰ- ریشه ساخته شده، با دو پسوند: همان ‎-l-‎ی که در نام‌های اندام (مانند ungula) دیده می‌شود و پسوند ‎*-ko-‎، یعنی *h₃m̥bʰ-el-iko-؛ و در کنارش umbō, -ōnis «نافِ سپر» بی‌پسوند (از *h₃émbʰ-ō، بنا بر دِ فان ۲۰۰۸، ص ۶۳۹). ارنو-میه همان نکته‌ای را می‌گویند که این پیکان به آن نیاز دارد: «عنصر ‎-l-‎ در umbilicus در آلمانی علیای باستان nabalo، ایرلندی کهن imbliu و یونانی ὀμφαλός نیز هست» و «uی آغازی umbilicus حنجری‌زاد و عامیانه است، مانند unguis». پس umbilīcus عضو قانونیِ همین خانواده است و «او»ی آغازی همان درجهٔ ombh- است که نورایی در سرریشه آورده. یونانی ὀμφαλός هم‌ریشهٔ دقیق آن است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/umbilicus\",\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%83neb%CA%B0-\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt s.v. nobh-: '2. Variant form *ombh- in Latin umbō, boss of a shield: UMBO. … 4. Suffixed variant form *ombh-alo- in: a. Latin umbilicus, navel: UMBILICUS; NOMBRIL; b. Greek omphalos, navel: OMPHALOS.' Exactly the arrow drawn, and the reason Nourai's root box lists Ombh and Mbh.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"p. 315\", \"stance\": \"supports\", \"note\": \"'lat. umbilīcus \\\"Nabel\\\", umbō, -ōnis \\\"Schildbuckel\\\"' listed directly under the root, with 'EM 1122' as the cross-reference.\"},\n            {\"src\": \"LAT\", \"where\": \"LAT.txt lines 69495-69525 s.v. umbō/umbilicus\", \"stance\": \"supports\", \"note\": \"'umbilicus: v. le suivant … Dérivés: umbilicus: nombril … La forme principale est indiquée par l'indo-iranien: skr. nabhiḥ … L'élément -l- de umbilicus se retrouve dans v.h.a. nabalo, v.irl. imbliu, gr. ὀμφαλός … L'o prothétique de umbilicus … est comparable à celui de unguis'.\"},\n            {\"src\": \"SYN\", \"where\": \"Buck 4.43 (SYN.txt line 6448)\", \"stance\": \"supports\", \"note\": \"'Lat. umbilicus' heads the Romance column (It. bellico, Fr. nombril, Sp. ombligo, Rum. buric) in the NAVEL table of this root.\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"English\",\n          \"words\": \"umbilicus\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English umbilicus is a learned 17th-century adoption of Latin umbilīcus, taken straight from the Latin with no change and used as an anatomical term for the navel (with the adjective umbilical, from Medieval Latin umbilīcālis, in 'umbilical cord'). Watkins' index confirms the descent by listing 'UMBILICUS nobh-'. The popular Romance descendant of the same Latin word came into English separately as the heraldic nombril 'centre point of a shield', through Old French nombril (Latin umbilīcus > *umbilīculus > OF lombril, nombril).\",\n          \"derivation_fa\": \"انگلیسی umbilicus وام‌واژه‌ای عالمانه از سدهٔ هفدهم است که بی‌هیچ تغییری از لاتینی umbilīcus گرفته شده و اصطلاحی کالبدشناختی برای «ناف» است (با صفتِ umbilical از لاتینی میانهٔ umbilīcālis در «بند ناف»). فهرست واتکینز نیز «UMBILICUS nobh-» را می‌آورد و همین تبار را تأیید می‌کند. دنبالهٔ عامیانهٔ همان واژهٔ لاتینی جداگانه و از راه فرانسهٔ کهن nombril به انگلیسی رسیده است (اصطلاح نشان‌شناسیِ nombril «نقطهٔ میانی سپر»). ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/umbilicus\",\n            \"https://en.wiktionary.org/wiki/navel\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"No reference on this node; it depends on the AHD citation of its Latin parent, whose index entry 'UMBILICUS nobh-' covers the English word.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 index (line 2432) and s.v. nobh-\", \"stance\": \"supports\", \"note\": \"'UMBILICUS nobh-', 'UMBO nobh-', 'NOMBRIL nobh-' — the English words derived from the Latin branch.\"},\n            {\"src\": \"KLN\", \"where\": \"p. 1033 s.v. navel (cross-references)\", \"stance\": \"supports\", \"note\": \"'Cp. also omphalo-, omphalos, umbilicus, umbo, nombril' — Klein groups the English learned borrowings with navel under the same base *ombh-, nābh-, *mbh-.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\n"
}
```


### [2026-09-07T19:45:45.800Z] TOOL RESULT

```
File created successfully at: /home/sfmqrb/git/rishe/data/verification/page-367.json (file state is current in your context — no need to Read it back)
```


## [2026-09-07T19:45:48.993Z] TOOL CALL #68: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-367.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 367"
}
```


### [2026-09-07T19:45:50.843Z] TOOL RESULT

```
JSON OK
nodes verified: 17/17
node verdicts: {'confirmed': 11, 'transcription_suspect': 1, 'plausible': 5}
root verdicts: {'disputed': 1, 'confirmed': 1}
ref checks: {'partial': 4, 'contradicts': 1, 'supports': 11, 'not_checked': 5, 'not_found': 1}
books consulted: {'supports': 33, 'partial': 8, 'contradicts': 4, 'silent': 5} | by book: {'LKT': 7, 'KLN': 6, 'LAT': 6, 'SKT': 4, 'BQT': 3, 'SYN': 3, 'MON': 2, 'DEV': 2, 'PHD': 2, 'POK': 2, 'AHD': 2, 'AKD': 1, 'AFM': 1, 'TAD': 1, 'RCH': 1, 'PHN': 1, 'BRT': 1, 'KNT': 1, 'HUB': 1, 'NYB': 1, 'WLD': 1, 'IEC': 1}
```


## [2026-09-07T19:46:12.848Z] AGENT

Verification file written: `/home/sfmqrb/git/rishe/data/verification/page-367.json`. `python3 tools/verify_check.py 367` → 17/17 nodes, **0 PROBLEM lines**.

**Page 367 (book 337) — 2 non-redirect entries, 17 nodes**
- Node verdicts: 11 confirmed, 5 plausible, 1 transcription_suspect. Root verdicts: 1 disputed, 1 confirmed.
- Ref checks: 11 supports, 4 partial, 1 contradicts, 1 not_found, 5 not_checked. 50 `consulted` entries across 22 books.

**disputed**
- ROOT `Nitiru` (Akkadian): the head of the chart is wrong. Zimmern AKD p.61 prints the entry in square brackets and says Akkadian *nitiru*, Hebrew *nāter*, Aramaic *niṭrō* and Greek νίτρον all come **from Egyptian nṯrj** — Akkadian is a sibling borrowing, not the ancestor. Lokotsch 1567, Ernout-Meillet s.v. *nitrum*, Etymonline and Wiktionary agree. Root box should read Egyptian nṯrj.

**transcription_suspect**
- Entry 0 node #2 [Greek] `natron` → correct form is νίτρον (Doric λίτρον). `error_in: "book"` — the printed page 337 does show "natron", so the extraction is faithful; Nourai back-projected the modern a-vocalism (which is the Arabic/Spanish reflex) onto Greek. Klein p.1049, the reference he cites, has νίτρον. Page PNG saved to `data/verification/sources/refs/ocr/BOOK/367.png`.

**plausible (worth the owner's eye)**
- #4 Persian نطرون glossed "sodium" — it means 'natron/native soda'; Dehkhoda tags it معرب. #5/#6 Spanish→English *natron*: Klein's route, but Lokotsch/Devic/Pihan give Spanish *anatrón* and Etymonline routes English via French. #7 Latin box: *nitrum* is fine, but *natrium* is Modern Latin coined on *natron* (Klein p.1031 "ModL."), not classical Latin from *nitrum*. Entry-2 #1: forms are Avestan only — no Old Persian word for 'navel' is attested (Kent silent), so the "Old Persian" half of the label is unsupported.

**No extraction errors found** — the JSON matches the printed page everywhere, including the Persian scripts (نطرون، نیتریک اسید، نیترات، نیتروژن، ناف، نافه).

Notable ref-page confirmations: POK:314, WLD I 130, HRN:228 (entry no.1020, covers both *nāf* and *nāfe*), BRT col.1062, KLN:1031/1032/1049, AKD:61, and **BQT:2100** = vol.4 pdf p.183, whose Mo'in footnote is essentially Nourai's whole second chart. Only `SNS:258` could not be located (SNS has a *nāfag* entry citing Barth. 1062, but the scan's page offset is undetermined), and MON:4745/4880 are in Mo'in vol. 4, absent from the local library — checked instead against the online Mo'in/Dehkhoda text, which tags نیترات/نیتروژن "(فرانسوی)" and attributes the gloss to فرهنگ فارسی معین.
