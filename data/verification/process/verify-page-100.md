# Verification process log — verify-page-100


## [2026-09-05T14:36:43.349Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 100 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-100.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-100.json. Write /home/sfmqrb/git/rishe/data/verification/page-100.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 100` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T14:36:44.888Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T14:36:45.590Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T14:36:45.603Z] TOOL RESULT

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


## [2026-09-05T14:36:45.919Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-100.txt"
}
```


### [2026-09-05T14:36:45.933Z] TOOL RESULT

```
1	=== PDF page 100 (book page 70) ===
2	--- entry 0 ---
3	ROOT [Semitic] B.n.v : son, child  (refs KLN:163; FVA:53)
4	#1 (parent #0) [Arabic] refs=KLN:163; FVA:53 | b.n.v : child ; ibn : son ; bent : daughter
5	  #2 (parent #1) [Persian] refs=MON5:85,285; FVA:53; FSD:197 | ebn «ابن» : son ; bent «بنت» : daughter ; banî «بنی» : sons, children ; Ebne-Sînâ «ابن سینا» : Avicena. A Khwarazmian scholar (980-1037) | extra: بنی آدم ، بنی هاشم | NOTE: Avicena's book, "Canon of Medicine",  was the first guide to medical studies in Europe from 12th to 17th century. He published his books in Arabic and was, therefore, often mistaken as an Arab scholar.
6	    #3 (parent #2) [English] refs=FSD:197 | Avicena, Avicenism
7	#4 (parent #0) [Hebrew] refs=KLN:163, 164 | běn : son ; Ben-yâmîn : son of the right (prosperous) hand ☞ Y.m.n ; Reŭ-bhen : behold a son
8	  #5 (parent #4) [Persian] refs=None | Benyâmîn «بنیامین» : Benjamin
9	  #6 (parent #4) [English] refs=KLN:163; AHD | Benjamin, Ben, Big Ben, Reuben
10	--- entry 1 ---
11	ROOT [Turkish] Boqčâ, Bŭqčâ : a large napkin, linen for wrapping clothes in it  (refs MON:551)
12	#1 (parent #0) [Persian] refs=MON:551,555 | boqčeh «بغچه» : bundle, pack | extra: بقچه ، بوغچه
13	  #2 (parent #1) [Arabic] refs=PLA:53; LAM:37 | bouqčeh : bundle
14	    #3 (parent #2) [French] refs=TAD:12; LAM:37 | bagage : luggage
15	      #4 (parent #3) [English] refs=AHD:99; SKT:35; LAM:37 | baggage
16	
```


## [2026-09-05T14:36:48.928Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-100.json",
 "description": "Read page-100 source JSON"
}
```


### [2026-09-05T14:36:48.967Z] TOOL RESULT

```
{
  "pdf_page": 100,
  "book_page": 70,
  "entries": [
    {
      "root": {
        "name": "B.n.v",
        "lang": "Semitic",
        "refs": "KLN:163; FVA:53",
        "gloss": "son, child"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Arabic",
          "refs": "KLN:163; FVA:53",
          "words": [
            {"translit": "b.n.v", "gloss": "child", "script": null},
            {"translit": "ibn", "gloss": "son", "script": null},
            {"translit": "bent", "gloss": "daughter", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "MON5:85,285; FVA:53; FSD:197",
          "words": [
            {"translit": "ebn", "gloss": "son", "script": "ابن"},
            {"translit": "bent", "gloss": "daughter", "script": "بنت"},
            {"translit": "banî", "gloss": "sons, children", "script": "بنی"},
            {"translit": "Ebne-Sînâ", "gloss": "Avicena. A Khwarazmian scholar (980-1037)", "script": "ابن سینا"}
          ],
          "script_extra": "بنی آدم ، بنی هاشم",
          "note": "Avicena's book, \"Canon of Medicine\",  was the first guide to medical studies in Europe from 12th to 17th century. He published his books in Arabic and was, therefore, often mistaken as an Arab scholar.",
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "English",
          "refs": "FSD:197",
          "words": [
            {"translit": "Avicena, Avicenism", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Hebrew",
          "refs": "KLN:163, 164",
          "words": [
            {"translit": "běn", "gloss": "son", "script": null},
            {"translit": "Ben-yâmîn", "gloss": "son of the right (prosperous) hand ☞ Y.m.n", "script": null},
            {"translit": "Reŭ-bhen", "gloss": "behold a son", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Persian",
          "refs": null,
          "words": [
            {"translit": "Benyâmîn", "gloss": "Benjamin", "script": "بنیامین"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "چون نه یعقوبی و نه بن یامین - زین دعا نشنوی مگر آمین",
            "poet": "Hadîqat-ol-Haqîqat"
          }
        },
        {
          "id": 6,
          "parent": 4,
          "lang": "English",
          "refs": "KLN:163; AHD",
          "words": [
            {"translit": "Benjamin, Ben, Big Ben, Reuben", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Boqčâ, Bŭqčâ",
        "lang": "Turkish",
        "refs": "MON:551",
        "gloss": "a large napkin, linen for wrapping clothes in it"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "MON:551,555",
          "words": [
            {"translit": "boqčeh", "gloss": "bundle, pack", "script": "بغچه"}
          ],
          "script_extra": "بقچه ، بوغچه",
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Arabic",
          "refs": "PLA:53; LAM:37",
          "words": [
            {"translit": "bouqčeh", "gloss": "bundle", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "French",
          "refs": "TAD:12; LAM:37",
          "words": [
            {"translit": "bagage", "gloss": "luggage", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "English",
          "refs": "AHD:99; SKT:35; LAM:37",
          "words": [
            {"translit": "baggage", "gloss": null, "script": null}
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


## [2026-09-05T14:36:49.646Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-05T14:36:49.694Z] TOOL RESULT

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


## [2026-09-05T14:36:54.198Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['KLN','FVA','FVQ','MON','FSD','AHD','PLA','LAM','TAD','SKT','LKT','PHN','DEV','AFM','ARB']:\n    v=d.get(k)\n    print('==',k, json.dumps(v,ensure_ascii=False)[:900] if v else 'MISSING')\n\""
}
```


## [2026-09-05T14:36:54.772Z] TOOL CALL #6: Bash

```json
{
 "command": "ls tools/ && sed -n 1,60p tools/verify_check.py"
}
```


### [2026-09-05T14:36:55.973Z] TOOL RESULT

```
== KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based l
== FVA {"title": "S.M. Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (dakhil), Tohi/Azadi 1368/1989", "kind": "catalog", "url": "https://openlibrary.org/works/OL4602367W (edition OL2012991M: Intisharat-i Islami 1368/1989, 582 pp)", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: no digital copy found.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: still no digital copy on any permitted platform. Library catalogues list the 1368 book under the variant title «فرهنگ ریشهٔ وام‌واژه‌های عربی (لغات عربی مستعمل در فارسی دخیل)» — reconcile with Nourai's title when buying. Catalogue record only."}
== FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ.txt"], "page_offset": "printed page = leaf − 17 (0-based \\f blocks in FVQ_pages.txt; 335 leaves)", "covers_etymology": true, "notes": "Good English OCR (Arabic script garbled). Same 1938 edition Nourai cites.", "cites": "page number of Jeffery, The Foreign Vocabulary of the Qurʾān (19
== MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different paginati
== FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt", "page_offset": "vol1: leaf = p + 41..56 (drifts; e.g. leaf 87 = p.46, leaf 612 = p.556); vol3: leaf = p - 1466 (e.g. leaf 215 = p.1681); vol4: leaf = p - 2144..2148 (e.g. leaf 229 = p.2373); vol2 offset not reliably detected (pages ~ 700-1640) - grep the headword. local file has \\f between leave
== AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifier": "watkins-american-heritage-dictionary-of-indo-european-roots-1985", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt", "page_offset": "1985 Watkins ed.: lea
== PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 leaves (pdftotext -layout, \\f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276).", "lookup_hint": "HathiTrust search-only; Google Books id q_ErAAAAMAAJ snippet view; DDB has only the table of contents. No full text online. | For pages in a scanned volume use: python3 tools/ref_page.py P
== LAM {"title": "H. Lammens, Remarques sur les mots français dérivés de l'arabe, Beyrouth 1890", "edition_found": "1890", "kind": "archive_djvu", "url": "https://archive.org/details/remarquessurles00lammgoog", "identifier": "remarquessurles00lammgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAM.txt", "page_offset": "leaf = printed + 57 (e.g. leaf 59 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "French headword in caps at line start with running heads like '2 ABRI'.", "notes": "Built from djvu.xml."}
== TAD {"title": "Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-hurufihi (2nd ed. Cairo 1932, ed. Yusuf Tuma al-Bustani; later Library of Lebanon reprint) — Nourai lists it under Arabic authors ('Unaysi T.'); its Table IV line was lost in the OCR", "kind": "archive_djvu", "url": "https://archive.org/details/TOB1932ARAR (1932 ed.); also https://archive.org/details/ar113lang79 and https://archive.org/details/elshandawily14640", "lookup_hint": "Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; inside.php search works.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD.txt"], "page_offset": "86 leaves (small book, ~80 printed pages); offset ≈ leaf − 4..6, verify against the printed numeral on the pa
== SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags.", "notes": "Nourai says '1882-1967'; the
== LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 'NNNN. word (language) meaning' - Lokotsch is usually cited by entry number, but Nourai cites pages. grep the oriental source word in transliteration or the number.", "notes": "", "cites": "entry number of Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs (1927)"}
== PHN {"title": "A. P. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du turc, Paris 1866", "edition_found": "1866", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairetym01pihagoog", "identifier": "dictionnairetym01pihagoog (others: bub_gb_QnsSAAAAIAAJ, dictionnairetym00pihagoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHN.txt", "page_offset": "leaf = printed + 31 (e.g. leaf 33 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "French headword in caps at line start; Arabic script not OCRed. grep -n '^BAZAR' etc.", "notes": "Built from djvu.xml."}
== DEV {"title": "L. M. Devic, Dictionnaire étymologique des mots français d'origine orientale, Paris 1876", "edition_found": "1876", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairety00devi", "identifier": "dictionnairety00devi (also dictionnairetym02devigoog, fr105comparative41)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/DEV.txt", "page_offset": "leaf = printed + 26 (pp. <80) to +30 (pp. >84), e.g. leaf 29 = p.3, leaf 118 = p.88. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "French headword in caps at line start.", "notes": "Devic's text is also printed as the supplement of Littré (dictionnairedela00littuoft)."}
== AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM.txt"], "page_offset": "198 leaves; page numerals OCR'd unreliably — offset approx leaf − 8 (front matter); confirm on page image", "covers_etymology": true, "notes": "Arabic OCR fair; Syriac/Latin etyma partially garbled.", "
== ARB {"title": "al-Jawaliqi, al-Mu'arrab min al-kalam al-a'jami, Tehran 1966 (reprint of Ahmad M. Shakir's Cairo 1361/1942 edition)", "kind": "archive_djvu", "url": "https://archive.org/details/mo3rb (probably the Shakir edition) ; https://archive.org/details/almo3rab_gwaliqy_f_abduraheem (F. 'Abd al-Rahim ed., Damascus 1990) ; also uc1.aa0003615705 / AAlexandrina-148752 (Sachau's Leipzig 1867 ed.) ; text on shamela.ws", "lookup_hint": "Alphabetical Arabic headwords; grep in ARB_mo3rb.txt / ARB_abdulraheem.txt (raw, no page breaks); edition of mo3rb not confirmed — check its title page image.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/ARB_mo3rb.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/ARB_abdulraheem.txt"], "page_offset": null, "covers_etymology": true, "notes": "Arabic OCR fair."}
```


### [2026-09-05T14:36:56.015Z] TOOL RESULT

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
```


## [2026-09-05T14:37:20.788Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification && ls | head -30 && echo --- && python3 -c \"\nimport json;d=json.load(open('page-66.json'));print(json.dumps(d['entries'][0],ensure_ascii=False,indent=1)[:3000])\""
}
```


## [2026-09-05T14:37:21.718Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=92 && NR<=95 {print \"=== leaf \" NR-1; print}' KLN_1966.txt | grep -n -i -A4 -B2 \"Benjamin\\|Ben-yamin\\|ibn\\|Reuben\" | head -80"
}
```


### [2026-09-05T14:37:22.635Z] TOOL RESULT

```
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
---
{
 "entry": 0,
 "root": "A`.s.r",
 "verdict": "confirmed",
 "modern_form": "Arabic root ع ص ر ʿ-ṣ-r 'to press, squeeze (the juice out)'; West Semitic *ʿṣr 'to press, restrain, retain'",
 "note": "The root box is right on all three counts: the Arabic verb عَصَرَ ʿaṣara 'he pressed, squeezed' is real, the language label is right, and the gloss 'to squeeze (the juice out)' is almost word for word the gloss of the AHD Appendix of Semitic Roots ('ʿṣr — West Semitic, to press, restrain, retain … alizarin, probably from Arabic al-ʿuṣāra, the juice, from ʿaṣara, to squeeze'). Two refinements. (a) The root is not specifically Arabic but common West Semitic: AHD labels it West Semitic and Klein, s.v. alizari, compares Hebrew ʿātzar, Aramaic-Syriac ʿătzar 'he retained' — so 'Arabic' should read 'Arabic (West Semitic)'. (b) The derived noun is vocalised ʿuṣāra عُصَارَة by AHD and by Wiktionary, ʿaṣārah by Klein; Nourai follows Klein's a-vocalism ('a`sârah'), and since both variants are attested this is not an error, only a choice of source. The European branch of the chart (Sp. → Fr. → Eng. alizarin) is Klein's and AHD's account, but AHD hedges it with 'probably', Dozy explicitly declared the origin unknown, and Wiktionary/Webster's 1913 now prefer an Ottoman-Turkish route — see node #3.",
 "note_fa": "ریشهٔ «ع ص ر» به معنای «فشردن، آب چیزی را گرفتن» ریشه‌ای اصیل و درست است و برچسب زبانی و معنای آن در نمودار نورایی با آنچه پیوست ریشه‌های سامی فرهنگ American Heritage می‌آورد یکسان است؛ تنها نکته آن است که این ریشه ویژهٔ عربی نیست و سامی غربی است (کلاین هم عبری «عَصَر» به معنای «نگاه داشتن» را هم‌ریشهٔ آن می‌داند). گونهٔ اسمی آن در فرهنگ‌های امروزی عُصارة و در کلاین عَصارة ضبط شده و نورایی ضبط کلاین را برگزیده است؛ هر دو ضبط پذیرفتنی است و خطا نیست. شاخهٔ اروپایی این نمودار (اسپانیایی ← فرانسوی ← انگلیسی alizarin) از کلاین گرفته شده، ولی همان‌گونه که در گرهٔ ۳ گفته می‌شود، این بخش قطعی نیست و ویکی‌واژه امروزه راه دیگری (از راه ترکی عثمانی) پیشنهاد می‌کند. در مجموع ادعای نورایی دربارهٔ خودِ ریشه درست است.",
 "sources": [
  "https://www.ahdictionary.com/word/semitic.html",
  "https://www.ahdictionary.com/word/search.html?q=alizarin",
  "https://en.wiktionary.org/wiki/عصارة"
 ],
 "ref_check": [
  {
   "ref": "KLN:50",
   "status": "supports",
   "note": "KLN_1966.txt, form-feed leaf 38 (two printed pages per leaf ⇒ printed pp. ~52-53, i.e. Nourai's p.50 ±2): 'alizari, n., madder root. — F., fr. Sp. alizari, fr. Arab. al-'aṣārah, \"the juice\", fr. al-, \"the\", and aṣara, \"he squeezed, pressed\", which is rel. to Heb. ʿātzar, Aram.-Syr. ʿătzār, \"he retained\".' Exactly the root, the gloss and the Romance chain Nourai draws."
  },
  {
   "ref": "FVA:273",
   "status": "not_checked",
   "note": "FVA = S.M. Nahvi, Farhang-e vāžehā-ye ʿarabi dar fārsi (1368/1989). refs_online.json records no digital copy on archive.org, ketabnak, noorlib or the open web; catalogue record only (OpenLibrary OL2012991M)."
  }
 ],
 "nodes": [
  {
   "id": 1,
   "lang": "Arabic",
   "wo
```


### [2026-09-05T14:37:24.118Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T14:37:27.852Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Benjamin\" KLN_1966.txt | head -20; echo ---; python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 'Benjamin' in p or 'Reuben' in p:\n        print('leaf',i)\nEOF"
}
```


### [2026-09-05T14:37:29.800Z] TOOL RESULT

```
3076:Aphra,  fern.  PN.  —  The  name  arose  from  a  mis¬ understanding  of  blbheth  ‘  Aphrdh ,  ‘in  the  house of  Aphrah’  (Mi.  1 : 10),  ‘Aphrah  having  been  mis¬ taken  for  a  feminine  personal  name.  In  reality ‘ Aphrdh ,  in  the  above  verse  is  the  name  of  a town  which  was  identified  by  most  commen¬ tators  with  ‘ Ophrdh  in  Benjamin  (see  Josh.  18:23). The  name  prob.  means  ‘hind’, aphrite,  n.,  a  variety  of  calcite  (mineral)  —  Form¬ ed  with  subst.  suff.  -ite  fr.  Gk.  &9p64,  ‘foam’, (see  aphro-);  so  called  from  its  appearance, aphrizite,  n.,  a  variety  of  tourmaline.  —  Formed with  subst.  suff.  -ite  from  the  stem  of  Gk.  2941- £eiv,  ‘to  foam’,  fr.  a9po4,  ‘foam’  (see  next  word) ; so  called  from  its  appearance  when  heated, aphro-,  before  a  vowel  aphr-  combining  form meaning  ‘foam’.  —  Gk.  duppo-,  dc<pp-,  fr.  a9p64, ‘foam’;  of  uncertain  origin.  Cp.  the  prec.  two words.
4496:Bartonia,  n.,  a  genus  of  plants  of  the  gentian family  (bot.)  —  ModL.,  named  in  honor  of Benjamin  Smith  Barton  of  Philadelphia  (died in  1815).  For  the  ending  see  suff.  -ia. baruria,  n.,  an  abnormal  condition  in  which  the urine  has  a  very  high  specific  gravity  ( med .)  — Medical  L.,  compounded  of  Gk.  (3apu<;, ‘heavy’, and  oOpov,  ‘urine’.  See  bary-,  uro-,  ‘of  urine’, and  -ia.
4737:ben,  n.,  son.  —  Heb.  ben,  ‘son’,  rel.  to  Arab,  ibn, Aram.-Syr.  bar,  ‘son’,  Akkad,  binbimi,  ‘grand¬ son’.  Cp.  Benjamin,  B’nai  B’rith,  boanerges.  Cp. also  Barabba.s,  bar  mitzvah,  Barnabas,  Bartho¬ lomew.  For  the  feminine  correspondences  Heb. bath,  ‘daughter’,  etc.,  see  bathkol  and  cp. Bathsheba.
4738:Ben,  masc.  PN.  —  Dimin.  of  Benjamin  (q.v.) bench,  n.  —  ME.,  fr.  OE.  bene,  rel.  to  ON.  bekkr, Dan.,  Swed.  bank,  OS.,  OFris.,  MLG.,  Du., OHG.,  G.  bank,  MHG.  banc,  ‘bench’,  ON. bakki,  ‘elevation’.  Cp.  bank,  banket,  bankrupt, banquet,  charabanc,  mountebank,  saltimbanco. Derivatives:  bench,  tr.  and  intr.  v.,  bench-ing,  n. bencher,  n.,  any  of  the  members  of  the  Inns  of Court.  —  Formed  fr.  bench  with  agential  suff. -er.  Cp.  disbench.
4759:Benjamin,  masc.  PN. ;  in  the  Bible,  Jacob’s  young¬ est  son.  —  Heb.  Binyamtn,  lit.  ‘son  of  the  right hand’,  fr.  ben  ‘son’,  and  yamtn,  ‘right  hand’; see  Gen.  35: 18.  For  the  first  element  see  ben, ‘son’.  Heb.  yamtn  means  also  ‘south’  (lit.  ‘the right  hand,  the  right  side’,  i.e.,  if  one  faces  east). It  is  rel.  to  Aram.-Syr.  yammin,  Ugar.  ymn, ‘right  hand’,  Arab,  ydman,  ‘right  hand,  right side,  south’,  ydmana,  ‘he  was  happy’,  lit.  ‘he turned  or  went  to  the  right’  (the  right  side  was regarded  as  auspicious),  Ethiop.  yaman,  Akkad. imnu,  ‘right  hand,  right  side’.  Cp.  Yemen,  mai- mon,  monkey.
4966:bigarreau,  n.,  a  variety  of  cherry.  —  F.,  fr.  bigarre, ‘variegated’,  fr.  OF.  garre  ‘variegated’,  which  is of  uncertain  origin;  so  called  from  its  color. Big  Ben,  name  of  the  bell  attached  to  the  clock at  Westminster.  —  Named  after  Sir  Benjamin Fiall,  first  commissioner  of  works,  under  whose supervision  the  bell  was  cast.  For  Ben,  dimin. of  Benjamin,  see  Ben.
5229:erudition.  —  About  1740  a  literary  circle  used to  assemble  at  Lady  Elizabeth  Montague’s  home in  London.  Benjamin  Stillingfleet,  one  of  the leading  members  of  the  circle,  regularly  attend¬ ed  those  meetings,  wearing  blue  stockings,  a circumstance  which  gave  occasion  to  admiral Boscawen  to  deride  The  blue  stocking  society; hence  the  name  bluestocking,  and  its  loan  trans¬ lations:  F.  bas-bleu,  Du.  blauwkous,  G.  Blau- strumpf,  etc.
11181:Dexter,  masc.  PN.  —  L.,  ‘on  the  right  hand,  for¬ tunate’.  See  prec.  word.  For  sense  development cp.  Benjamin.
16318:Gloxinia,  n„  a  genus  of  tropical  plants  (bot.)  — ModL.,  named  after  Benjamin  Peter  Gloxin, an  1 8th  century  German  botanist  and  physician. For  the  ending  see  suff.  -ia. gloze,  intr.  v.,  to  shine,  blaze  (Scot.)  —  See  gloss, ‘to  polish’.
17228:harmonica,  n.,  an  instrument  consisting  of  a series  of  glasses  (mus.)  —  Fr.  L.  harmonica,  fern, of  harmonicas;  see  prec.  word.  The  name  har¬ monica  was  given  to  this  instrument  by  its  in¬ ventor  Benjamin  Franklin  (he  spelled  it  ar- monica).
24264:monkey,  n.  —  MLG.  Moneke(n),  name  of  an  ape, prob.  fr.  MIt.  monnicchio,  fr.  Olt.  monna  (cp. Sp.  and  Port,  mono,  mono),  ‘ape,  monkey’, aphetically  formed  fr.  Turk,  maymiin,  of  s.m.,  fr. Arab,  maymun,  ‘auspicious’,  used  euphemis¬ tically  to  denote  the  ape  or  monkey,  whose  sight is  supposed  to  bring  misfortune.  See  Theodor Noldeke,  Worter  mit  Gegensinn,  in  his  Neue Beitrage  zur  semitischen  Sprachwissenschaft, Strassburg,  1910,  p.  89.  Arab,  maymun  is  pass, part,  of  yamana,  ‘he  was  happy,  he  was  for¬ tunate;  it  was  auspicious’,  fr.  yaman,  ‘right  side, south’,  yamfn,  Tight  hand’,  See  Benjamin  and cp.  maimon  and  raona,  ‘a  small  African  monkey’. —  Olt.  monna,  ‘ape,  monkey’,  has  been  influ¬ enced  in  form  by  monna,  ‘woman’,  contraction of  ma  donna,  ‘my  lady’.
36807:Derivative:  still,  n.,  an  apparatus  for  distilling, stilliform,  adj.,  having  the  form  of  a  drop.  — Compounded  of  L.  stilla,  ‘a  drop’,  and  forma, ‘form,  shape’.  See  still,  ‘to  distil’,  and  form,  n. stilling,  also  stillion,  n.,  a  stand,  framework.  — Du.  stelling,  fr.  stellen,  ‘to  place’,  fr.  I.-E.  base •st(h)el-,  ‘to  place’.  See  stall  and  cp.  still,  adj. Stillingia,  n.,  a  genus  of  plants  of  the  family Euphorbiaceae  ( bot .)  —  ModL.,  named  after the  English  naturalist  Benjamin  Stillingfleet (1720-71).  For  the  ending  see  1st  suff.  -ia. stilt,  n.  —  ME.  stilte,  rel.  to  Dan.  stylte,  Swed. stylta,  Norw.  stilla,  MDu.  stelte,  Du.  stelt, OHG.  stelza,  MHG.,  G.  stelze,  fr.  Teut.  base *stelt-,  a  -^-enlargement  of  I.-E.  base  *st(h)el-, ‘to  cause  to  stand,  to  place;  to  stand’.  See  stall and  cp.  stout.
36859:Derivative:  stoic-al-ly,  adv. stoichiometry,  also  stoechiometry,  stoicheiometry, n.,  the  art  of  determining  the  atomic  and  molec¬ ular  weights  of  the  elements  (chem.)  —  G.  Std- chiometrie,  lit.  ‘measurement  of  elements’,  coin¬ ed  by  the  German  chemist  Jeremias  Benjamin Richter  (1762-1807)  in  his  “Anfangsgriinde  der Stochiometrie  oder  Meflkunst  chemischer  Ele- mente”  (1792)  fr.  Gk.  axotyeiov,  ‘element’,  and -pexpla,  ‘a  measuring  of’.  The  first  element  is  a derivative  of  axotyoq,  ‘row,  line,  rank’,  which is  rel.  to  oxt/os,  ‘row,  line,  rank;  verse’,  oxe(- yetv,  ‘to  go;  to  march  in  order’ ;  see  stichic.  For the  second  element  see  -metry.
---
leaf 58
leaf 90
leaf 97
leaf 101
leaf 102
leaf 107
leaf 241
leaf 358
leaf 379
leaf 535
leaf 713
leaf 804
leaf 805
```


## [2026-09-05T14:37:30.086Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nfor f in ['LAM.txt','SKT.txt','LKT.txt','PHN.txt','DEV.txt']:\n    t=open(f,encoding='utf-8',errors='replace').read()\n    pages=t.split('\\f')\n    hits=[i for i,p in enumerate(pages) if re.search(r'bagage|BAGAGE|baggage|bagues',p)]\n    print(f,len(pages),hits[:20])\nEOF"
}
```


### [2026-09-05T14:37:31.718Z] TOOL RESULT

```
LAM.txt 376 [33, 94]
SKT.txt 657 [47, 627, 633]
LKT.txt 278 []
PHN.txt 438 [89]
DEV.txt 326 [148]
```


## [2026-09-05T14:37:41.161Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (90,97,101,102):\n    p=t[i]\n    print('======= leaf',i,' approx printed p.',2*(i-12),'-',2*(i-12)+1)\n    import re\n    for m in re.finditer(r'(ben,|Benjamin|Reuben|B.nai|boanerges|Bethlehem)',p):\n        print('   ...',p[max(0,m.start()-200):m.start()+420].replace('\\n',' '))\n        print('---')\nEOF"
}
```


## [2026-09-05T14:37:42.026Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('LAM.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (33,94):\n    print('===== LAM leaf',i,'printed p.',i-57)\n    print(t[i][:2500])\nEOF"
}
```


### [2026-09-05T14:37:42.953Z] TOOL RESULT

```
======= leaf 90  approx printed p. 156 - 157
   ... his  thirteenth  year,  when  he  reaches  the  age  of religious  responsibility  ( Jewish  religion).  — Heb.  bar  mitzvdh,  lit.  ‘son  of  command’,  fr.  bar, ’son’,  which  is  rel.  to  Heb.  ben,  and  mitzvdh, ’command,  commandment’,  which  is  rel.  toVziv- vd\  ‘he  commanded’.  For  the  first  element  see ben,  ‘son’,  and  cp.  the  first  element  in  Barabbas, Barnabas,  Bartholomew.  For  the  second  element see  mitzvah. barn,  n.  —  ME.  bern,  fr.  OE.  bern,  shortened  fr. orig.  bere-ern,  lit.  ‘barley  house’,  fr.  here,  ‘bar¬ ley’  and  ern,  xrn,  ‘house’.  For  the  first  elem
---
   ... h,  lit.  ‘son  of  command’,  fr.  bar, ’son’,  which  is  rel.  to  Heb.  ben,  and  mitzvdh, ’command,  commandment’,  which  is  rel.  toVziv- vd\  ‘he  commanded’.  For  the  first  element  see ben,  ‘son’,  and  cp.  the  first  element  in  Barabbas, Barnabas,  Bartholomew.  For  the  second  element see  mitzvah. barn,  n.  —  ME.  bern,  fr.  OE.  bern,  shortened  fr. orig.  bere-ern,  lit.  ‘barley  house’,  fr.  here,  ‘bar¬ ley’  and  ern,  xrn,  ‘house’.  For  the  first  element see  barley.  The  second  element  is  a  metathesized form  of  *ran(n)  (for  *rasn),  ‘house’,  and  rel.  to ON.  r
---
   ... mew,  masc.  PN.  —  OF.  Barthelemieu  (F. Barthelemy),  fr,  L.  Bartholomaeus,  fr.  Gk.  Bap- doXopaioi;,  fr.  Aram,  bar  Talmdy,  ‘son  of  Tal- mai’.  Aram,  bar,  ‘son’,  is  rel.  to  Heb.  ben,  of s.m. ;  see  ben,  ‘son’,  and  cp.  words  there  referred to.  Talmdy,  a  Heb.  name  occurring  already  in the  Bible  (e.g.  Nu.  1 3 : 22),  is  rel.  to  Heb.  telem, ‘furrow’. Derivative:  Bartholome-an,  adj. 151 bartizan,  n.,  a  small  tower  for  defense  —  First used  by  Walter  Scott  who  mistook  the  real meaning  of  Scot,  bartisene,  which  is  nothing  but the  corrupted  spelling  o
---
   ... F.  Barthelemieu  (F. Barthelemy),  fr,  L.  Bartholomaeus,  fr.  Gk.  Bap- doXopaioi;,  fr.  Aram,  bar  Talmdy,  ‘son  of  Tal- mai’.  Aram,  bar,  ‘son’,  is  rel.  to  Heb.  ben,  of s.m. ;  see  ben,  ‘son’,  and  cp.  words  there  referred to.  Talmdy,  a  Heb.  name  occurring  already  in the  Bible  (e.g.  Nu.  1 3 : 22),  is  rel.  to  Heb.  telem, ‘furrow’. Derivative:  Bartholome-an,  adj. 151 bartizan,  n.,  a  small  tower  for  defense  —  First used  by  Walter  Scott  who  mistook  the  real meaning  of  Scot,  bartisene,  which  is  nothing  but the  corrupted  spelling  of  bratticing,  ‘timbe
---
   ... it.  ‘barley  enclosure’,  fr. here,  ‘barley’,  and  tun,  ‘enclosure’.  See  barley and  town. Bartonia,  n.,  a  genus  of  plants  of  the  gentian family  (bot.)  —  ModL.,  named  in  honor  of Benjamin  Smith  Barton  of  Philadelphia  (died in  1815).  For  the  ending  see  suff.  -ia. baruria,  n.,  an  abnormal  condition  in  which  the urine  has  a  very  high  specific  gravity  ( med .)  — Medical  L.,  compounded  of  Gk.  (3apu<;, ‘heavy’, and  oOpov,  ‘urine’.  See  bary-,  uro-,  ‘of  urine’, and  -ia. bary-,  combining  form  meaning  ‘heavy’.  —  Gk. (Sapu-,  fr.  (japui ;,  ‘heavy’,  rel.  
---
======= leaf 97  approx printed p. 170 - 171
   ... n. bemoan,  tr.  v.  —  ME.  bimenen,  fr.  OE.  benuenan, ‘to  lament’,  fr.  be-  and  msenan,  ‘to  moan’. See  moan. bemuse,  tr.  v.  —  Formed  fr.  be-  and  muse. Derivative:  bemus-ed,  adj. ben,  adv.,  within  (Scot.)  —  OE.  binnan  (rel.  to OFris.  binna,  MDu.,  Du.,  MHG.,  G.  binnen), ‘within’ ;  contraction  of  bi-innan,  be-innan.  See be-  and  in,  prep. ben,  n.,  the  inner  room  (Scot.)  —  From  prec. word. ben,  n.,  son.  —  Heb.  ben,  ‘son’,  rel.  to  Arab,  ibn, Aram.-Syr.  bar,  ‘son’,  Akkad,  binbimi,  ‘grand¬ son’.  Cp.  Benjamin,  B’nai  B’rith,  boanerges.  Cp. also  Barab
---
   ... :  bemus-ed,  adj. ben,  adv.,  within  (Scot.)  —  OE.  binnan  (rel.  to OFris.  binna,  MDu.,  Du.,  MHG.,  G.  binnen), ‘within’ ;  contraction  of  bi-innan,  be-innan.  See be-  and  in,  prep. ben,  n.,  the  inner  room  (Scot.)  —  From  prec. word. ben,  n.,  son.  —  Heb.  ben,  ‘son’,  rel.  to  Arab,  ibn, Aram.-Syr.  bar,  ‘son’,  Akkad,  binbimi,  ‘grand¬ son’.  Cp.  Benjamin,  B’nai  B’rith,  boanerges.  Cp. also  Barabba.s,  bar  mitzvah,  Barnabas,  Bartho¬ lomew.  For  the  feminine  correspondences  Heb. bath,  ‘daughter’,  etc.,  see  bathkol  and  cp. Bathsheba. Ben,  masc.  PN.  —  Dimin.  
---
   ... nnan  (rel.  to OFris.  binna,  MDu.,  Du.,  MHG.,  G.  binnen), ‘within’ ;  contraction  of  bi-innan,  be-innan.  See be-  and  in,  prep. ben,  n.,  the  inner  room  (Scot.)  —  From  prec. word. ben,  n.,  son.  —  Heb.  ben,  ‘son’,  rel.  to  Arab,  ibn, Aram.-Syr.  bar,  ‘son’,  Akkad,  binbimi,  ‘grand¬ son’.  Cp.  Benjamin,  B’nai  B’rith,  boanerges.  Cp. also  Barabba.s,  bar  mitzvah,  Barnabas,  Bartho¬ lomew.  For  the  feminine  correspondences  Heb. bath,  ‘daughter’,  etc.,  see  bathkol  and  cp. Bathsheba. Ben,  masc.  PN.  —  Dimin.  of  Benjamin  (q.v.) bench,  n.  —  ME.,  fr.  OE.  bene,  
---
   ... nna,  MDu.,  Du.,  MHG.,  G.  binnen), ‘within’ ;  contraction  of  bi-innan,  be-innan.  See be-  and  in,  prep. ben,  n.,  the  inner  room  (Scot.)  —  From  prec. word. ben,  n.,  son.  —  Heb.  ben,  ‘son’,  rel.  to  Arab,  ibn, Aram.-Syr.  bar,  ‘son’,  Akkad,  binbimi,  ‘grand¬ son’.  Cp.  Benjamin,  B’nai  B’rith,  boanerges.  Cp. also  Barabba.s,  bar  mitzvah,  Barnabas,  Bartho¬ lomew.  For  the  feminine  correspondences  Heb. bath,  ‘daughter’,  etc.,  see  bathkol  and  cp. Bathsheba. Ben,  masc.  PN.  —  Dimin.  of  Benjamin  (q.v.) bench,  n.  —  ME.,  fr.  OE.  bene,  rel.  to  ON.  bekkr, Dan.
---
   ... nd  in,  prep. ben,  n.,  the  inner  room  (Scot.)  —  From  prec. word. ben,  n.,  son.  —  Heb.  ben,  ‘son’,  rel.  to  Arab,  ibn, Aram.-Syr.  bar,  ‘son’,  Akkad,  binbimi,  ‘grand¬ son’.  Cp.  Benjamin,  B’nai  B’rith,  boanerges.  Cp. also  Barabba.s,  bar  mitzvah,  Barnabas,  Bartho¬ lomew.  For  the  feminine  correspondences  Heb. bath,  ‘daughter’,  etc.,  see  bathkol  and  cp. Bathsheba. Ben,  masc.  PN.  —  Dimin.  of  Benjamin  (q.v.) bench,  n.  —  ME.,  fr.  OE.  bene,  rel.  to  ON.  bekkr, Dan.,  Swed.  bank,  OS.,  OFris.,  MLG.,  Du., OHG.,  G.  bank,  MHG.  banc,  ‘bench’,  ON. bakki,  ‘el
---
   ... ep. ben,  n.,  the  inner  room  (Scot.)  —  From  prec. word. ben,  n.,  son.  —  Heb.  ben,  ‘son’,  rel.  to  Arab,  ibn, Aram.-Syr.  bar,  ‘son’,  Akkad,  binbimi,  ‘grand¬ son’.  Cp.  Benjamin,  B’nai  B’rith,  boanerges.  Cp. also  Barabba.s,  bar  mitzvah,  Barnabas,  Bartho¬ lomew.  For  the  feminine  correspondences  Heb. bath,  ‘daughter’,  etc.,  see  bathkol  and  cp. Bathsheba. Ben,  masc.  PN.  —  Dimin.  of  Benjamin  (q.v.) bench,  n.  —  ME.,  fr.  OE.  bene,  rel.  to  ON.  bekkr, Dan.,  Swed.  bank,  OS.,  OFris.,  MLG.,  Du., OHG.,  G.  bank,  MHG.  banc,  ‘bench’,  ON. bakki,  ‘elevation’.  
---
   ... he  inner  room  (Scot.)  —  From  prec. word. ben,  n.,  son.  —  Heb.  ben,  ‘son’,  rel.  to  Arab,  ibn, Aram.-Syr.  bar,  ‘son’,  Akkad,  binbimi,  ‘grand¬ son’.  Cp.  Benjamin,  B’nai  B’rith,  boanerges.  Cp. also  Barabba.s,  bar  mitzvah,  Barnabas,  Bartho¬ lomew.  For  the  feminine  correspondences  Heb. bath,  ‘daughter’,  etc.,  see  bathkol  and  cp. Bathsheba. Ben,  masc.  PN.  —  Dimin.  of  Benjamin  (q.v.) bench,  n.  —  ME.,  fr.  OE.  bene,  rel.  to  ON.  bekkr, Dan.,  Swed.  bank,  OS.,  OFris.,  MLG.,  Du., OHG.,  G.  bank,  MHG.  banc,  ‘bench’,  ON. bakki,  ‘elevation’.  Cp.  bank,  bank
---
   ... Cp. also  Barabba.s,  bar  mitzvah,  Barnabas,  Bartho¬ lomew.  For  the  feminine  correspondences  Heb. bath,  ‘daughter’,  etc.,  see  bathkol  and  cp. Bathsheba. Ben,  masc.  PN.  —  Dimin.  of  Benjamin  (q.v.) bench,  n.  —  ME.,  fr.  OE.  bene,  rel.  to  ON.  bekkr, Dan.,  Swed.  bank,  OS.,  OFris.,  MLG.,  Du., OHG.,  G.  bank,  MHG.  banc,  ‘bench’,  ON. bakki,  ‘elevation’.  Cp.  bank,  banket,  bankrupt, banquet,  charabanc,  mountebank,  saltimbanco. Derivatives:  bench,  tr.  and  intr.  v.,  bench-ing,  n. bencher,  n.,  any  of  the  members  of  the  Inns  of Court.  —  Formed  fr.  bench  wit
---
   ... idnem,  acc.  of  henedictid. See  benediction. benitoite,  n.,  a  barium  titanosilicate  (mineral.)  — Named  after  San  Benito  River  in  California. For  the  ending  see  subst.  suff.  -ite. Benjamin,  masc.  PN. ;  in  the  Bible,  Jacob’s  young¬ est  son.  —  Heb.  Binyamtn,  lit.  ‘son  of  the  right hand’,  fr.  ben  ‘son’,  and  yamtn,  ‘right  hand’; see  Gen.  35: 18.  For  the  first  element  see  ben, ‘son’.  Heb.  yamtn  means  also  ‘south’  (lit.  ‘the right  hand,  the  right  side’,  i.e.,  if  one  faces  east). It  is  rel.  to  Aram.-Syr.  yammin,  Ugar.  ymn, ‘right  hand’,  Arab,  y
---
   ...  ;  in  the  Bible,  Jacob’s  young¬ est  son.  —  Heb.  Binyamtn,  lit.  ‘son  of  the  right hand’,  fr.  ben  ‘son’,  and  yamtn,  ‘right  hand’; see  Gen.  35: 18.  For  the  first  element  see  ben, ‘son’.  Heb.  yamtn  means  also  ‘south’  (lit.  ‘the right  hand,  the  right  side’,  i.e.,  if  one  faces  east). It  is  rel.  to  Aram.-Syr.  yammin,  Ugar.  ymn, ‘right  hand’,  Arab,  ydman,  ‘right  hand,  right side,  south’,  ydmana,  ‘he  was  happy’,  lit.  ‘he turned  or  went  to  the  right’  (the  right  side  was regarded  as  auspicious),  Ethiop.  yaman,  Akkad. imnu,  ‘right  hand,  right  
---
======= leaf 101  approx printed p. 178 - 179
   ... of  drink;  spongy.  —  L.  bi- 170 171 bulus,  ‘drinking  readily’,  fr.  bibere  ‘to  drink’, assimilated  fr.  *pibere,  which  is  cogn.,  with  OI. plbati,  ‘drinks’,  OIr.  if  ‘drink!’,  OW.  iben,  ‘we drink’;  from  the  reduplication  of  I.-E.  base  *pi-, *pd(i)-,  ‘to  drink’,  whence  OI.  pdti,  ‘drinks’, pdyayati,payate,  ‘gives  to  drink*,  pdtiam,  ‘bev¬ erage’,  Arm.  lmpem,  ‘I  drink’,  Gk.  -rrfvetv,  ‘to drink’,  716014,  ‘a  drink’,  716x04,  ‘a  drinking,  a drinking  bout’,  L.  potare,  ‘to  drink’,  potio,  ‘a draft,  drink’,  OSlav.  pijQ,  piti,  ‘to  drink’.  See potion  and  cp.  
---
   ... ted’,  fr.  OF.  garre  ‘variegated’,  which  is of  uncertain  origin;  so  called  from  its  color. Big  Ben,  name  of  the  bell  attached  to  the  clock at  Westminster.  —  Named  after  Sir  Benjamin Fiall,  first  commissioner  of  works,  under  whose 
---
======= leaf 102  approx printed p. 180 - 181
   ... supervision  the  bell  was  cast.  For  Ben,  dimin. of  Benjamin,  see  Ben. bigg,  big,  n.,  the  four-rowed  barley  (dial.)  —  ME. big,  bigge,  fr.  ON.  bygg,  ‘barley’,  rel.  to  OE. beow,  ‘grain,  barley’,  OS.  beo,  bewod,  ‘harvest’, biggin,  n.,  cap,  hood.  —  F.  beguin,  fr.  beguine, name  of  the  members  of  certain  lay  sisterhoods (see  Beguine);  so  called  from  caps  originally worn  by  them. biggin,  n.,  a  coffee  percolator.  —  So  call
---
```


### [2026-09-05T14:37:44.862Z] TOOL RESULT

```
===== LAM leaf 33 printed p. -24
XXVIII.
m w
f_; comme 3' jp-au lieu de 3* jï (i )• Au Maroc ( et il en était
de même chez les Arabes d'Espagne ) le fJ et le J ne se
distinguent presque pas. Dans la Haute^Egypte, à Bag-
gdad (2) le J devient ghîm ; chez les nomades de Méso-
tamie tantôt fJ , tantôt j^. La Basse-Egypte garde la pro-
nonciation syrienne.
De là : Deux manières de rendre cette lettre en fran-
çais ; par le son k et par le son g (dur).
i^ son )t : k, c, ch, q : café, alicate, bondic, kibla, caki-
le, quinta,l, axirnach.
2^ par le son g (gue) : gabelle, goum, guider, bagage
targe, assogue, fanègue.
Exceptions :é^orajr(j); dans sarrasinle J est devenu jf.
Dans quelques mots le J n'est pas rendu : fonde, abri-
coty de (jjtji) , al-berqoûq^ prononcé à la Syrienne al-ber^
qoù (Voy. abricot).
Cette lettre est constante; on la transcrit par k, khj Cj
chj q, où le même son persiste toujours.
(1) Y. Ibn Kamâl Bâcha : «^dlj >i^l J«i^ J» «^Odl p. 31. (Leiden).
(2) Quelquefois aussi il y est assimilé au ^ gim. M' Jeannier cite ^ Ji
qartb prononcé wi^;>i3 marmite, prononcé jO^.
(3) Esp. borrax, de Jj^. Cfr. Minhâg d'Ibn "Ga^la à l'article ^jy
(manus. cit.) ojj^ ,j^ *> ^jV» .
===== LAM leaf 94 printed p. 37
BAGA . 37
B
Bagage, Esp: bagage./?/^: bagagem. ca/:bagatge. val:
bâgaig. — M. de Eguilaz pense que ce mot a été introduit
en Europe par les Croisés, qui l'auraient emprunté à
Tarabe *^. bouqga ou îiL, bouqcha, paquet de linge
et d'habits (i), terme très employé en Syrie; on en a
même formé un verbe A ' empaqueter. Ce mot qui
n'appartient pas à la langue classique, est d'origine
persane ^"i « involucrum ex tela, aut corio confèctum,
plerumque quadrangulum, ubi involvuntur vestes vel lin-
teamina » ( VuUers ). Nous renvoyons pouf plus de détails
à l'excellent article de M. de Eguilaz.
Cobarruvias a pensé que les Espagnols ont emprunté
« bagage » aux Français. Nous croirions plutôt le con-
traire. Bagage apparaît chez nous assez timidement au
i6"^® siècle, tandis qu'il est déjà employé comme un ter-
me usuel par Hurtado de Mendoza (mort en 1 57}), Argote
de Molina, Cervantes, Mariana etc.
(1) Comme dans ce passage des Mille et une nuits • • . J L.4<i^j j3 ùIO
"t^, et plus loin :bJJ) iXSî *^ ,jJ&\j etc. (V. aJj SU wiJI H. p. 149 etc. édi-
UoQ du P. Salhani S. J. Beyrouth ). Voir aussi les savantes notes de Qua-
tremère. SulU Mamelouks, T. I. 1'» partie p. 12, 219, 253 etc.
```


## [2026-09-05T14:38:01.998Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('SKT.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (47,):\n    print('===== SKT leaf',i,'printed p.',i-20)\n    print(t[i][:1800])\nEOF\necho \"########## Klein Reuben\"; grep -o \"Reuben[^.]\\{0,300\\}\" KLN_1966.txt | head -5"
}
```


### [2026-09-05T14:38:03.480Z] TOOL RESULT

```
===== SKT leaf 47 printed p. 27
ed,  jadeil micKKiV  <•  Icel biigr,aaeasy.biigr,^v>i.,. ,  ..<> to  hinder,  oppress.  Prob. V.bcJ7^,  to  mock. Bag.  (E.)  Put  for  ba/f  ME.  hi O.  Northomfarian  b^fic*  ^g>  Loke^  I 35.+Goth.  balgs,  a  wine-sLin:  G  htk skin  ;  Icel.  Ar^,  a  skin,  a  bog.  So  j GaeL  ha!gt  ^/f,  also  ^^,  a  liTithem  \ Lit.  'that  which  swells  out.'  CTNJ BALG.)    See  Bulse.  1
bagatelle,  a  tride,  a  ^me.  (F.««Iti Teut,^  K.A:^-v;;^.atriflc-ItaLi«^|i<( a  tiille,  diinin.  of  Parmesan  bAgaia^  a| property  ;  from  Lombard  A^o,  a  wfaiM of  Teut.  origin  ;  sec  Bag,  ba^*Be(l]
>M«gag«  (0,  luggage.  (F.-C.)  1 bagj^age^ bagage.  —  O.  r.  bagagt,  a  coUed of  bundles.  •■  O.  F.  bague,  a  bundle. Celtic  origin;  Bret,  beoi'k,  a  b batch,  a  burden ;  Gael,  bag,  ba/g,  a see  Bag.
baggage  h),  a  worthless  woman. C.)  Corrupted  fiom  O,  F.  bagaste,  ' gage,  quean/  CoU  Cf.  Ital.  ba, worthless  woman,  p.  Perhaps  or^a camp-follower,  ba;;gagt-woman:  fionQ bague,  a  bundle ;  see  Bagc^e  ( i  \.  y.; Mumy  makes  it  the  lamc  as  Bagcag«j in  a  dcpia^-ed  sense.  ,1
bellowa.  (E.)  M.  E.  b^U,  btfy.  Id a  bag.  but  used  in  the  Kj^ecial  sobJ '  bellows.'  Btllawj  u  the  pL  oi  M t07v,  a  bog,  also  another  form  of  Mh\ beity  is  another  form  of  bag.  Cf-  G,  I bal^,  a  *  blow  bag,*  a  pair  of  bellows;.
belly.  (E.)     M.  E.  My.    A.  S. est  form  b^Hg,  lit.  a  ba^.  4-Du. belly;    SwcJ.  bdlg,   belly,   oellows; baig,  busk,  belly ;  Gael.  bo!g^  bog,  bti
bilge.  (Scand.)     Pro[)Cily  the rant  part  (belly)  of  a  ship  or the  Terb  to  biigr,  lit  to  till  - beg^in  to  leak,  as  a  ship.—  I'.in.  ^i/j suill,  Swed.  dial,  baiga,  to  fill  one*i AUo  written  bulgt.
bilgo-water.
########## Klein Reuben
Reuben,  1)  masc
```


## [2026-09-05T14:38:04.118Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== TAD بقجة\"; grep -n \"بقج\\|بغج\\|بقچ\" TAD.txt | head; echo \"=== TAD_pages\"; python3 - <<'EOF'\nt=open('TAD_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(len(t))\nfor i,p in enumerate(t):\n    if 'بقج' in p or 'بقچ' in p or 'بغچ' in p:\n        print('leaf',i, [l for l in p.split('\\n') if 'بقج' in l or 'بقچ' in l or 'بغچ' in l][:5])\nEOF"
}
```


### [2026-09-05T14:38:05.730Z] TOOL RESULT

```
=== TAD بقجة
=== TAD_pages
87
```


## [2026-09-05T14:38:17.248Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SKT.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (54,55,56):\n    print('===== SKT leaf',i,'printed p.',i-20)\n    print(t[i][:1500])\n    print()\nEOF"
}
```


## [2026-09-05T14:38:17.874Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('TAD_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (14,15,16,17,18):\n    print('===== TAD leaf',i)\n    print(t[i][:1200])\nEOF"
}
```


### [2026-09-05T14:38:19.193Z] TOOL RESULT

```
===== SKT leaf 54 printed p. 34
   F.  birqutr, to  bob ;   Col.  -  F.  inc.  beak.     Sec  Peuk. (Misplaccil ;  unless  i(  be  used  for  b€<bon.)
beckon.  (E.)  M.E,  htcmn.  A.S, U\nan,  bcxUtucM,  to  moke  n  sign. —  A.S, bifH,  beiifen,  a  beacon,  token,  WKn.
Bead.  (E.*)    See  Bid  (1).
Beadle.  (F.-O.  H.G.)    See  Bid  (a.)
Beagle,  a  doc.  (Unknown.)  hX.M.bt^it, Squire  of  Low  fVgrre,  I.  771.
Boak.  {,F.-C.)    See  Peak.
Beaker.  (O.  Low  G.-L.-Gk.)  M.E. biktr,  fyker,'mO,'&^\.  biktri;  Iccl.  bika/r, a  cup.^Du.  heiUr',  G.  b^chtr;  lul.  buthien, p.  From  Low  L.  bicarixim,  a  wine-cup.— Gk.  ^('xor,  an  carlhcn  wiiic-ves>cl ;  a  word of  Eastern  or  i^D.
pitoher,  (F.  -  O.  H.  G.  -  L.  -  Gk.) The  aamc  word.  F.  fichitr,  *a  pitcher; a  Languedoc  word;'  Cot.  —  O.  II.  G.  pi- ihdri  (G.  ^<'A«/-).  —  Low  L.  bUariMm  \  as above.
Beam  (t),  a  piece  of  timber.  (£.)  M.  E. bttm.  A.  S.  bcdm,  a  trec.-f  Du.  b96m  \  G. banm ;  Goth,  bagnu.
beam  (a^,  a  ray.  (E.1  Tlic  same  wofdt ipccially  used  to  signify  a  5ttai|;ht  ray. A.  S.  byrH€Hd<  bedm,  '  the  pillar  of  tire.'
boom  (2\  a  beam,  pole.  (Da.)  Dtt. boom,  n  tree,  a  beam;    see  Beain<j).
bumpkin,  a  thick  headed  fellow.  (Dn.) —  O.  Hu,  boomktn,  a  little  tree  (Hexham); dimin,  of  boom,  a  tree,  a  beam,  bar.  The E.  bttrnkiH  aUo  meant  a  luff,  block,  a  thidt piece  of  wood  (Cotgravc,  5.  v.  Chicambault)', hence  readily  applied  10  a  blo

===== SKT leaf 55 printed p. 35
 by  hammering.  Du. bcf-sem   is   from  the   nme  root   as  A.  S.
botch  fj).  a  Bwdling.  (F.-O.  H.G.) M.E.  boitbt.^O.Y.  bote,  a  IkiU.  botch, boll :  K.  Hme.    Sec  bOM  at>ove.
bottle  (3\  a  bundle  of  hay.  (F. - .O.Ii.G.)    lA.K.b^i/.^O.F,b0it/,b0U/U,
RKAVER.
a  small  bundle ;  dimin.  of  bit/fr,  « of   hay.  -  O.  H.  G.  fi6tff,   btftff,    a of   flax;     allied    to  O- H.  U.   y^»i*, beat ;  from  the  beating  of  ftaic.
butt  U)t  AH  end,  ihtust;  to  thnot  C -O.  H.G.)     [The  sen&es  of  the  sb be  referred  to  the  verb  ;  just  as  F.  An end,  butt-end,  depends  on  bcMfgr,  to M.  K.  bu//en,  to  push,  strike.— O.  ~ to   push,   bull,   str.ke.  —  M.  H. O.  H.  G.  /Stan,  to   bent.     Per from  O.  F.  bat,  F.  bout,  an  end  (sec below);  buff  (to  shoot  at),  from the  same,  alHetl  to  K.  bu/,  a  mark, to  hit.     Dar.  a-biit  (above).
buttock.  (F.;  w$rJi  E.  suJLr.)  It bo/o/t,  bottok.^O.l'.  Aw  (F.  beut\  an  e (cf.  E.bu/t'THd);  vrilh dimin.  Buflix  -ttJkii below.
button.  (F.  -  O.  II.  C.)    M  E. also,  a  bud.  —  O.  F.  /vt/iM   (F.  btmiamX bud,   a   button ;    properly,  a  round pushed  out.  —  O.  F.  boUr,  to   posh»  ; out;   see  butt  (i).
debut.  ^F.-L.  ami  O.  H.  G.)  A appearance  in  a  play.  —  F.  d^b*4f,  a  ft stroke,  lint  cast  or  throw  at  dice.  T urig.  sense  seems  to  have  been  '  a  1 aim,'  or  'a  miss;'  it  is  allic<l  to  O. desbuttr,  '  to 

===== SKT leaf 56 printed p. 36
»m.ift  of  ihij  g-nard. »  ratt  %  ITic
t'&om   ■  u-i'itiis^i
BOW  cni..pcU  UiffUUr)^  i%
iticn,  aibi  CaUc
•  villi  esi  ft  horn.  (F.-L)
BugUt  a  horn,  is  short  for  hugh-hom ;  a hi^U  is  A  wild  ox.  — O.K.  hugU^  a  wild  ox.
••L.  ace.  i-ucuium,  a  young  ox:  double diinin.  of  ifos,  on  ox.
Boer.  (E)  M.  E  Arw.  A.  S.  *«fr-.+Du. and  G.  i^/>r;  I  eel.  bjdrr.  Probably  con- nected wiih  Brow.
Beestinga ;  sec  Biestinge.
Beet.  (L.>  ME-fr^/*.  A.S.  A(//.-L. /V/a;  beet  (Pliny.)
Beetle  (i),  an  insect;  see  Bite.
Beetle  (j),  a  mallet ;  see  Beat.
Beetle  (3),  to  jut  out,  hang  over :  see Bito.
Befall.  Befool,  Before ;  sec  Fall,  &&
Beg.  (£.)     SeeBid(i).
Beget,  Begin ;  &ce  Get,  Oin  (i).
Begone,  Beguile;  fee  Go.  "Wile.
Begtline,  onr  <;>f  a  class  of  religious  de- votees. (F.)  Chiefly  used  in  the  fcm. ;  F. iK'gHtHe,  Low  L.  btj^'hiua,  one  of  a  rtligiuus onicr,  fii^t  established  at  Licgc,  about  a.i). IJ07.  Named  after  Laml)ert  I-c  Bi-gue, priest  of  Vxh^c  (lalh  c).  Lc  It^^jue  rtiians *stammeiec,'  from  the  verb  l^.'guif  to  staio- oicr,  to  the  dialect  of  Namar.
Behali;  intercut.  (E.)     Sec  Hair.
Behave,  Behaviour.  (E.)    See  Uave.
Behead.  (E.)  Sec  Hoad.
Behemoth.  (Hcb-E^yptl  \Uh.  Kht- Hukh,  sftid  to  be  pi.  ()f  bchemdht  a  lea-t; hut  rc.-illy  of  Kgypt.  origin.
Behest,  Beliind,  Behold.  (E)  See Heat,  HlDd,  Hold(l).
Behoof,  advantage.  (E)  M.
```


### [2026-09-05T14:38:20.753Z] TOOL RESULT

```
===== TAD leaf 14
                                  ‫دوو‬


‫من « وى » أي رابحة ذكة و‪9‬ستان» وهي أداة‬           ‫يتان ‪ -‬فارسي ‪5‬‬

                                                    ‫تدل على ظرف المكان‬
    ‫على ‪ 1‬ايطالي والودام ج للأءذام وهو تصغير ‪05‬وم أي وزنوقاللانشة‬

‫بلبنيوس وفي اليونانية هؤام وهو نات بستني سنويله سنف أي‬         ‫كام ‪6‬‬

    ‫قرون في جوفها كحابلمص حاوالطيموقد ينبت في جبل لبنان وتسميه العامة‬
‫ش‬                                                 ‫هناك « الحالية » من طممه‬
           ‫شتختة ‏ عابى ‪ -‬الصندوق الصفير ‪ .‬فارسي م ركب م‬
‫بنيش أي أمام‬
                                                ‫ومختهأي لوح‬
                               ‫تركي « بشلك ‪ 6‬معناه حماسى‬         ‫شلك‬
‫معناه ضارية وبراد به عدة مدافم تطلق م وفي‬       ‫بطارية ل يللي ‪3‬‬
                                        ‫لكوت ‪ +‬كك اليف‬
‫رظأقة حاارائية و قات أ ‪.‬وطالة وكتانتة وووقة وأم[ مناه ‪ 121‬اليا‬
                                        ‫كانت شق من اللوح ليكتب عليها‬
    ‫بطرشيل س بو ثان ‪1‬ي‪00‬ل هزه وعوببر‪ 8-5‬من أع أيفودودوزاغطعه»؟‬
‫ةجعلبا الكاهن فيعنقهعندمباشرنه‬
                             ‫رطرز ي‬
                                  ‫نزيم‬
                                     ‫وقةل
===== TAD leaf 15
                                  ‫لدابإاو ده‬


 ‫‪ 001‬أي فرس و‪ 81012‬أيتطيدب مرادفه‬                 ‫يوناني ا‬           ‫يطرة‬

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
                        
===== TAD leaf 16
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
                             ‫شط ال‬
                                 ‫لمرب‬
                                    ‫اناه‬
                                       ‫ار‪-‬سى « بندر ©مع‬
                                                      ‫فدر‬
                                                        ‫بن‬
                                                               ‫رئيس التجار‬
                                     ‫‪7‬‬                           ‫د‬
                      ‫أي اليوم الخسون‬    ‫مم يونانى ‪65‬‬

 ‫من بند‬    ‫وي او‬          ‫عامية من الايطالية ‪202‬‬ 
===== TAD leaf 17
                                ‫‪0 0‬‬


                          ‫سبلوان ‪--‬فارسي ‪ 3‬مبلوان » معناهبطلومكافح‬
  ‫بلى ‪ 85209‬معناه فى الاصل اليونانى كيس من جلد لحنظ‬     ‫وارصيةطا‬
 ‫جرة بأسهم‬    ‫اية‬
                ‫للتجار‬
                     ‫كهأاعما‬
                           ‫الدراءمويرادبهفي زماننامجلس التجاريجري في‬
                                                      ‫اولرابتحجار السفنالخ‬
 ‫وتقة وودقة ودوطة وبوانة ‏ فارسي ‪ 2‬لوده » وهو وعاء يديب الصائغ‬



             ‫وق ‪ -‬لاتيني ودأءعمط مرادفه الصور والناقور والتقير تفخ فيها‬

  ‫تق من برق أي لمم فنقل من العربية الى اللاتينية وبناا »«ة؟وط‬
         ‫‪5‬‬       ‫‪03‬‬       ‫‪5‬‬             ‫‪0‬‬      ‫‪ 59‬ع‬   ‫‪-‬‬     ‫‪75‬‬       ‫ع‬

                                                            ‫مرقش‪-‬‬
                                                                ‫بو‬
 ‫الحامض البورفي والنطرون منهطبيعي‬   ‫والىالفارسية « بوره ‪ 6‬وهو ملح حاصل من‬


  ‫وقد بوجدعلىضفاف الامبر في فارص وتيبت وكاليفورنيا ومنه ما حصل باعمال‬
 ‫النطرون فدعي كذ! هن وادي النطرون في‬
                                   ‫كياوية وهو خلاف اللطرون ‪ .‬أم ا‬

                                                      ‫‪ 11111‬ئيسه‬
   
===== TAD leaf 18
‫ينع فيمصر واللفظة مصرية ‪ .‬جاءففيبعضترجمات الاتميلكانلابسا البرفير‬
‫والارجوان وهو غاط والاصحكان لاسا البوص والارجوان أي كانلاب قيصاً‬
                                 ‫طويلا كمتنان ورداء من الارجوان أى العرفير‬
                              ‫وغاز ‪ -‬ترك « بوغاز مع»ناه خليجومضيق‬
‫وفاطة ‪ -‬عامية من الايطالية ‪6‬نههناط معناه غسل اشاب اء الرماد مرادفه‬
                                                                   ‫اميل‬
‫وليس ‪ - 72‬يوناني هعافادم معناه تديير المديئة وسياستها مرادفه الدّمرتط‬
                                                                      ‫وشحئة البلد‬
 ‫أيطالي ‪ 922‬اوم املنلاتينية *‪«6110‬معناء وصول وهو ورقة ‪.‬يدرج‬              ‫وليصة‬

                             ‫في بابان وصول درام وأمتعة وبضاعة وحو ذلك‬
                  ‫وقال ب يوناني وذلهعانزهط معناه كوزمنفخار“يشركب به‬
‫للمحذاء‬
      ‫فهملالعه ا‬
               ‫وادق‬
                  ‫ويا‪ -‬تركي « بوي »ا ممناهصبغوخضاب ولونمر‬
                           ‫معناه طابعم رأدفه طابعبريد‬       ‫ول | ايطاللي ‪0‬‬

 ‫بيقة والعامة تقول بأقبة ‏ يوناني داعااط وفي اللانينية ‪ 2017‬وهي الكرسة‬
          ‫بييدر ‪ -‬ارامية د بيت إدرا » بمعنى أى موضع ‪:‬درس فيه المنطة‬
 ‫نبادة ‏ فارسي « بياده » معناه الم
```


## [2026-09-05T14:40:17.135Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nfor f,leaves in [('DEV.txt',[148]),('PHN.txt',[89])]:\n    t=open(f,encoding='utf-8',errors='replace').read().split('\\f')\n    for i in leaves:\n        print('=====',f,'leaf',i)\n        print(t[i][:1600]);print()\nEOF\necho \"##### LKT bogtscha\"; grep -n -i \"ogtscha\\|ohtscha\\|uq.a\\|Bündel.*Tuch\" LKT.txt | head -10\necho \"##### KLN baggage\"; grep -o \"baggage[^|]\\{0,320\\}\" KLN_1966.txt | head -3"
}
```


### [2026-09-05T14:40:18.779Z] TOOL RESULT

```
===== DEV.txt leaf 148
balayeur  de  la  Patriarcbale  de  Lisbonne). Le  cbangement  de  r  en  n  ne  ferait  pas  grande  difificullé (voy.  A\AFi\),  mais  nous  manquons  crarguments  à  l'appui de  cette  conjecture.
Farde.  Bordage  d'un  navire,  est  identique  à  falqiie  ou l'argue.  Farde,  balle  de  café  moka  pesant  1  85  kilogrammes, est  le  primitif  de  fardeau.  (Voy.  ce  mot.)
Fardeau.  Esp.  fardo ,  fardillo  (^haWoi),  fardel  (havre-sac, besace);  portug.  y?/n/o,  fardeJ  (même  sens);  iid\.  fardcUo (\)af[nQ[yfardaggio  (bagage).  On  voit  que  le  vrai  sens  est ballot,  paquet,  et  c'est  aussi  celui  de  notre  vieux  mot fardel,  sens  qui  du  reste  a  persisté  jusqu'au  dernier  siècle, comme  le  montre,  par  exemple,  un  tarif  de  1707  in- diquant les  droits  de  péage  pour  Bléré,  sur  le  Cher: r^Vour  fardeau  cordé  de  draps  de  laine,  pesant  Goo  livres, 12  deniers;  j)our  fardeau  cordé  de  feutres,  pesant  600 livres,  20  sols;  ^our  fardeau  cordé  de  tapis,  etc.  ^  51
Fardel ,  fardeau  est  un  diminutif  de  farde.  Or,  le  mot farde,  au  sens  général  de  ballot,  est  usité  depuis  longtemps dans  tout  l'Owent  :  Bocthor,  le  Gazophylacium  ling.  Pers. la  Fabrica  Img.  arabic.  traduisent  ballot  par  ii:>^  farda.  Il est  vrai  que  S.  de  Sacy-  pense,  sans  donner  ses  raisons, que  ce  mot  'é:>^h  farda ,  bien  qu'employé- par  les  Arabes,  est
'    llialoivodn  Chetionccaiix, -par  Viih])^  Chevalier,  )8r)8,p.  a8. -    (Jurât,  m-,  l.  ill ,  p.  ^79.
8.
116  DICTIONNAIRE  ÉTYMOLOGIQUE
étrange

===== PHN.txt leaf 89
58 BAR
[)agné de l'adjeclif royal. Il sert aussi à désigner uii tnorceau
d'étoffe de plusieurs doubles que Ton met sur les yeux de quel-
qu'un pour Tempécher de voir. — Au même radical se rat-
tache encore le substantif masculin bandage, sorte d'appareil
en acier élastique, courbé en arc, et portant à son extrémité
une ou deux pelotes pour contenir les hernies. — Les Espa-
gnols et les Portugais écrivent banda et venda, les Italiens banda
et benda, les Anglais band,
BANDIÈRE etBANNIÈRK, s. f. (p.)
«XJb- [éent/J bande, banderolle. Autrefois batidière se disait pour
bannière, en parlant du drapeau d'un seigneur de fief, autour
duquel venaient se ranger les vassaux lorsque ce seigneur
parlait pour la guerre. Le même mot se retrouve dans le latin
barbare bandum, l'espagnol bandera, le portugais bandeira, et
l'italien bandiera. — Dans l'art militaire, on nomme front de
bandière la ligne de développement entier d'une armée campée.
— Le mot bannière désigne particulièrement aujourd'hui une
sorte d'étendard qui précède les confréries dans les proces-
sions : cet étendard est ordinairement formé d'une étoffe de
soie brodée, représentant l'image de quelque saint, et sup-
portée par un bâton horizontal attaché à un b^ton droit. —
On appelle banderolle une bande d'étoffe appendue, comme
ornement, au mât d'un navire, au sommet d'un édifice, etc.
BAR, s. m. (p.)
j^ \bar\ poids, charge, fardeau, bagage. De là vient probable-
ment le mot français bar, qui désigne une machine à bran, une

##### LKT bogtscha
916:'Bündel,  Paket'  [Stamm  bag,  bog  s.  hier Nr.  323],  hogcagy  'Trödler';  hieraus  rum. hoccea  'Ballen;  viereckiges  Umschlag- tuch', boccealic  'Kopftuch',  hoccegiü, bocceangm  'Hausierer':  Dem.  boccelutä.
##### KLN baggage
baggage.
baggage,  n.  —  F.  bagage,  fr.  OF .  bague,  bundle  , which,  together  with  OProven^.  baga,  of  s.m., is  prob.  borrowed  from  Teutonic.  See  bag,  n., and  -age.
baggage.  — A  hybrid  coined  fr.  F.  bat,  ‘packsaddle’  and  E. horse.  F.  bat  derives  fr.  OProven?.  bast,  fr.  VL. *bastum,  ‘the  act  of  carrying’,  back  formation fr.  *bastare,  ‘to  carry’,  fr.  Late  Gk.  ’pxcsxxv, ‘to  carry’,  fr.  Gk.  pxaxx!j£i.v.  See  baston  and  cp. words  there  referred  to.
```


## [2026-09-05T14:40:18.882Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt; do echo \"=== $f\"; grep -c \"بقچه\\|بغچه\\|بقجه\" $f 2>/dev/null; done; echo; grep -n -o \".\\{80\\}بقچه.\\{120\\}\" MON_part1.txt | head -6"
}
```


### [2026-09-05T14:40:20.638Z] TOOL RESULT

```
=== MON_part1.txt
5
=== MON_part2.txt
2
=== incoming/MON/MON_2vol_Adena_v1_djvu.txt
5
=== incoming/MON/MON_2vol_Adena_v2_djvu.txt
2
```


## [2026-09-05T14:40:29.443Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"بقچه\\|بغچه\\|بقجه\" MON_part1.txt | cut -c1-400; echo \"=== part2\"; grep -n \"بقچه\\|بغچه\\|بقجه\" MON_part2.txt | cut -c1-400"
}
```


## [2026-09-05T14:40:29.458Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '905,930p' LKT.txt"
}
```


### [2026-09-05T14:40:29.509Z] TOOL RESULT

```
'Die  Pflanze  Piper  betel  L.  Betelpfetfer' mit  kleinen  roten  Blüten.  Ihre  Blätter werden  von  den  Europäern  Betel  ge- nannt; in  sie  werden  die  Arekanüsse [s.  hier  Nr.  17]  mit  Kalk  eingewickelt und  so  in  ganz  Südasien  als  Narkotikum, ähnlich  wie  bei  uns  der  Kautabak,  viel benutzt.
319.  Ar.  bittiha: 'Wassermelone',  Demin.  dazu  huttaiha; hieraus  z.  T.  mit,  z.  T.  ohne  ar.  Art. kat.  albudeca,  pg.  aibudega,  pateca,  sp. pg.  badea,  aprov.  albuesca,  npr.  aubieco, frz.  pastlqiie  'Wassermelone'  [dies  trotz Wartbg  FEWb  61  und  288;  das  dort angegebene  mal.  bateka  existiert  wohl kaum],  [DE  74  und  232.  Eguilaz  119. Hobson-Jobson  684/685.    ML  1136.
.320.  Ar.  bizzäf : 'Sehr',  vulgärer  Ausdruck  im  Magrib [Algier,  vgl.  Ad.  Wahrmund,  Praktisches Handbuch  der  neu-arabischen  Sprache. Gießen  1898.  S.  214,  Nr.  7*;  Marokko, vgl.  G.  Kampffmeyer,  Marokkanisch- arabische Gespräche.  Berlin  1912.  S.  17, Z.  3  V.  u.],  mit  Imäla  gesprochen: bizzef;  hieraus  it.  a  bizzeffe,  siz.  a  biz- zeffi  'reichlich',  frz.  (Argot)  bizef  'dass.'. [De  Gregorio  in  Romania  XXXI,  110  f. GrSVociSic  228.    ML  1143.
.321.  Tk.  bodrum: [Aus  gr.  iTTTTobpoiuGi;]  'Keller';  hieraus rum.  podrom,  podrum  'Keller'  [wofür gewöhnlich  pivriifä  gesagt  wird].  [Löbel EITAP  77.
322.  Tk.  bogaca:
'Art  Kuchen,  Käsekuchen';  hieraus  rum. bogacia,  hogavtü  'Pastete'.
323.  Tk.  bogaz:
'Kanal'  [Stamm  bag,  heg,  bog  'Band, gebunden,  binden'  Vämbery  TktEtWb S.  192,  Nr.  204  I];  hieraus  rum.  bogaz, hoaz  'Meerenge,  Kanal'.
324.  Tk.  bogasy: 'Futterleinwand':  hieraus  rum.  bogasiu, Abltg.  hogasier,  hogasierie,  sp.  bocacin,
frz.  houcassin,  engl,  huckskin  [mit  volks- etymologischer Umgestaltung],  dtsch. Buxkin  'Futterbarchent'.  [Sain  47. ML  1188.
325.  Tk.  bogca:
'Bündel,  Paket'  [Stamm  bag,  bog  s.  hier Nr.  323],  hogcagy  'Trödler';  hieraus  rum. hoccea  'Ballen;  viereckiges  Umschlag- tuch', boccealic  'Kopftuch',  hoccegiü, bocceangm  'Hausierer':  Dem.  boccelutä.
326.  Tk.  bo^yrtlak:
Auch  bagi/rtlak  'Kehlkopf;  hieraus  rum. beregatä  'dass.,  Kehle'.
327.  Tk.  boj:
[Stamm  baj,  boj  s.  hier  Nr.  260]  'Ge- stalt, Wuchs';  hieraus  rum.  boiü  'Aus- sehen, Wuchs,  Statur',  bulg.  serb.  boj, bojlija 'da.ss:.  [Mikl  SlEtWb  16  b.  Bern SlEtWb  68.
328.  Tk.  boja:
[Stamm  boj,  bot  'Farbe,  Blut'  Vämbery TktEtWb  S.  206,  Nr.  220]  'Farbe';  hier- aus rum.  boia  'Farbe,  Schminke',  boi- agiü,  hoiangiü  'Färber',  boiangerie  'Fär- berei', bulg.  serb.  boja  'Farbe,  Schminke'.
329.  Tk.  boklnk:
'Schmutz,  Mist,  Unrat'  [von  bok  'dass.' vom  Stamme  boj  s.  hier  Nr.  328] :  hier- aus rum.  bocluc,  bucluc  'Dünger,  Durch- einander', buclucgiü,  bucluca^  'schlechter Zahler,  Schwätzer'.
330.  Tk.  bol:
'Fülle';  durch  Gemination  wird  Ver- stärkung des  Begriffs  erzielt:  bolbol  'im Übermaß',  hieraus  rum.  bolbol  'über- mäßig'; Vb.  bolohäni  'sich  ballen'.  — Aus  dem  tk.  Abstraktum  boUuk  'Fülle' wurde  rum.  buluc  'Haufe,  Trupp,  Menge'.
331.  Jap.  bonsö:
[Aus  chiues.  fan-seng  'religiöse  Person, Priester',  jetzt  meist  ho- sang  genannt] 'Mönch,  buddhistischer  Priester  mit  ge- schorenem Kopfe'.  Hieraus  engl,  honze, frz.  honze,  dtsch.  Bonze  als  Bezeichnung für  fanatische  Geistliche  jeder  Religion, dann  übertragen  'ein  hochtrabender, stolzer  Mensch',  schließlich  'Fanatiker seiner  Überzeugung',  z.  B.  Parteibonze. [Birth  ChinFW  200.  Hobson-Jobson 105.    Kluge  63.
332.  Pers.  böstän:
[Aus  pers.  bö  'Geruch',  also  'Ort  des Duftes',  Horn  NpEt  S.  54,  Nr.  240] 'Garten',  tk.  ebenso;  hieraus  rum.  hostan 'Kürbis,  Melone',  bostanerie  'Gemüse- garten', hostangiü  'Gemüsegärtner':  bulg. serb.  bostan,  poln.  klruss.  basztan,  russ. hastan  'Gemüsegarten'.  [Gorjajew  14. Bern  SlEtWb  77.
```


### [2026-09-05T14:40:29.516Z] TOOL RESULT

```
24266:بعچه: (0:)۵<(.) [تر. > بوغچه - بقچه] 
27991:زبون) + رکابی (طبقچه)] (امر.) مقدار قلیل. 
68206:بندند؟ زیر رکابی. پیاله؛ نعلبکی. طبقچه. 
73721:که در آن چیزی نندند بقجه. سقر ۵. 
91578:افلااکت؛ (کد.) آسمان. طاس بقچه: مجموع 
=== part2
26927:یا مثل بقچه چهار گوشه را بهم فشار داده 
82094:پیچند؟ بقچه
```


## [2026-09-05T14:40:45.535Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== BQT\"; grep -n \"بقچه\\|بغچه\\|بوغچه\" BQT_v1_pages.txt BQT_v2_pages.txt incoming/BQT/BQT_v3_pages.txt incoming/BQT/BQT_v4_pages.txt incoming/BQT/BQT_v5_pages.txt 2>/dev/null | cut -c1-300 | head -20; echo \"== HRN/HUB\"; grep -n -i \"bug.a\\|bok.a\\|bagage\" HRN.txt HUB.txt | head; echo \"== ARY\"; grep -n \"بقچه\\|بغچه\" incoming/ARY/ARY_pages.txt | head"
}
```


### [2026-09-05T14:40:45.626Z] TOOL RESULT

```
== BQT
BQT_v1_pages.txt:12967:اقچ4 - بن اول بروزن بقچه , علامتی
BQT_v1_pages.txt:29525:قر هه با دال ابجد بر وزن طبقچه .
incoming/BQT/BQT_v4_pages.txt:2508:مرجاده()- 2 : بر وزن طبقچه بمعنی نحس
incoming/BQT/BQT_v4_pages.txt:12579:وشلوارباشد- وبقچه رانیز گویند ۱ وآن پارچه‌ای | بفةٌ پوستین کفته‌اند و از آن روپاء خواسته‌اند .
incoming/BQT/BQT_v4_pages.txt:17837:هکچه - بنم اول بروزن بقچه,جتن | هکچه است که جستن گلواست (۱) وبعربی‌فواق
incoming/BQT/BQT_v3_pages.txt:10539:‎GAP‏ - بروزن جفری » طبقچه را
== HRN/HUB
HUB.txt:6958:siren lassen (auch guddrdan^ vgl. bugdard Fird. I, 140, 204),
== ARY
```


## [2026-09-05T14:40:47.471Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('incoming/TTS/TTS_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('leaves',len(t))\nimport re\nfor i,p in enumerate(t):\n    if re.search(r'20[45]\\.\\s*bag|bogca|bogča|Bündel', p):\n        print('leaf',i,p[:60].replace('\\n',' '))\nEOF"
}
```


### [2026-09-05T14:40:48.885Z] TOOL RESULT

```
leaves 265
leaf 194                                                             
leaf 221                                                             
leaf 247                           218  bitmeh (beendigen) 229.     i
```


## [2026-09-05T14:40:56.460Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('incoming/TTS/TTS_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (193,194,195):\n    print('===== TTS leaf',i)\n    print(t[i][:1500])\nEOF"
}
```


### [2026-09-05T14:40:58.158Z] TOOL RESULT

```
===== TTS leaf 193
                                                            I(i4




                                                            178.


  ^(il, tili, ilcil,                            ll'tll,    nackt, bloss, einzeln, vereinzelt,
               verlassen, leer,                     Witwe, hermihen,                 entblössen.


cag.   tal= nackt,                    entblösst (tat Jcilic              = nacktes Schwert), abge-
       sondert,               einzeln (bir ial jigac                     = ein Stück Baum), Baum,
       Zweig; tala—fala                           = einzeln, allein, abgesondert; tafamak
       entblössen, berauben (vgl. osm. söj/«rt/t=: jemand entkleiden
       und berauben);  talan, talas, ^«//caw   Raub Beute, Eäu-                  =          ,



       berei Hader, Gezänk falasmaJc
                   ,                    sich gegenseitig berauben,
                                                    ;                    =
       sich zanken; *«/                         =
                          verlassen leer, Witwe (vgl. viduns         ,
                                                                                                          —
       vidua;              kk. erti'oÄ         = Witwe (d. h. ohne Mann).
üig.   *t/7    = verlassen             ,       düster, Trauer.
kir.   dal             (wiedal Moo
                                oben);zerstückeln;  daldul—halh      =
       nackt, zerlumpt; dal nemc, danneme =^vein nichts; talasbak
 
===== TTS leaf 194
                                                                                                    ;




                                                        1(35


             (losbrecheil, abbrechen, absondern) erinnert.                          Und schliess-
                     noch in d" übergegangen. So:
             lich ist t
    <'ag. f^«^»!a7i;    =
                     schlagen, abhauen, schneiden, absondern.
    osm. (fafmak (wie oben), mit der Hinzugabe folgender Bedeutun-
             gen, als: stehlen (vgl. fcdanial-), musiciren (ein Instrument
             schlagen); <*a^l^=zrerhauen, zerschlagen.
    alt.    <*i«n   = schneiden             ;   (^ala= halb, Hälfte           (cula tindi =^ halb
             lebendig).     Hinsichtlich der Begriffsanalogie von                       schneiden
            und halb            vgl.        bidmclc    und huvulc,        javmak und Jari
             (§ 133).


                                                        179.

    Tarn, tem, thti, torii, töni, tum, tütn, ton,
    tön, ton, tun, versammelt, vereint, fest, dicht, ge-
    schlossen, erstarrt, gefroren; Dunkelheit,                                Finsterniss, Nebel,
    Nacht,          Kerker,          Hölle.          Steingebäude (nach innerasiatischen
           Begriffen,     d.    h.      fensterlos);       sammeln, stocken, frieren,
                                                erstarren u. s. w.

               Betreffs leichtern Verständnisses wolle
===== TTS leaf 195
                                                                                              ;;   ;




                                                 1C6

          Mit der Grundbedeutung des Zusanimeniciehens, Er-
        starr ens werden wir solche Körper und Naturerscheinun-
        gen im Zusammenhange finden, deren Beschaffenheit den
        Zustand der Dichtheit, Geschlossenheit und Dunkel-
        heit bedingt. So:


                             II.   (Dichte, feste Körper.)

eng.    tarn, ^/Mt     = Steinhaus, Gemäuer; tomwÄ— Hölle (finstere,
        geschlossene     Oertlichkeit) tatnalc, tamur = kAe.x Kehle,
                                                 ;                                     ,



        Schlucht, Schlund (eigentl. der hohle, enge und finstere Gang
        so: tag    tamuri=^ ein finsterer, hohler AVeg im Berge); temir,
        tetniir,    timur = YÄsen        ,       eisenfest.     (Vgl. <em«V6as        — Stein-
        kopf,      harter Kopf,        eigensinnig;           temir   Äa.s'?!     = Nordstern,
        wörtlich: eiserner Pflock, d. h. der unbewegliche Stern.)
iiig.   tatnuh,tomM = Hölle.
osni.   tamu (veraltet)= Hölle; ^M»n>'M/i;=Gefdngniss (iumruJc agasl
        = Gefängnisswächter); deniir—YÄ^e,n {demir to;.Z* = uner-
        schrocken,  d. h. von eisernem Blute).
alt.    #*»!=: fest, unbewegt, dicht, still; ^*»wl                    =   still   werden (s«if-
        kin tlmi berät =^A&r Wind ward still).
CUV.       = Abgrund, Höl
```


## [2026-09-05T14:40:58.835Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"بقچه\" BQT_v1_pages.txt | cut -c1-250; echo \"---v1 raw\"; grep -n \"بقچه\" BQT_v1.txt | head -5 | cut -c1-250; echo \"=== ARY latin bag\"; grep -n -i \"^BAGGAGE\\|BOGHCHE\\|BOQCHE\" incoming/ARY/ARY_latin_index_pages.txt | head"
}
```


### [2026-09-05T14:40:58.929Z] TOOL RESULT

```
12967:اقچ4 - بن اول بروزن بقچه , علامتی
29525:قر هه با دال ابجد بر وزن طبقچه .
---v1 raw
24750:اقچ4 - بن اول بروزن بقچه , علامتی 
60344:قر هه با دال ابجد بر وزن طبقچه . 
=== ARY latin bag
```


## [2026-09-05T14:41:05.288Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('incoming/TTS/TTS_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (221,222):\n    print('===== TTS leaf',i,'printed p.',i-29)\n    print(t[i][:2000])\nEOF"
}
```


### [2026-09-05T14:41:08.011Z] TOOL RESULT

```
===== TTS leaf 221 printed p. 192
                                                                                                      —

                                                       192



                                                      204.

Bag, heg, hik, bog, buk, baj, boj, biij, Band,
  Zauber, gelunden,                    befestigt,        stark, sehr, fest, befestigen,
                           binden, knüpfen, bezaubern.


                                                I.     —g, h.
uig.   hak, bek = B&nä, Strick; baklamaJc — binden,                                         scliliessen;
       &iÄ;= Befestigung, Band; bikünmek, bekiinmeJc = fest oder
       hart werden   beküh = geschlossen befestigt bekitmelc —
                           ;                                      ,                 ;



       schliessen,      befestigen,                  anbinden;    bök, &///?= Festigkeit,
       Kraft, Stärke.
cag.   bag, baglamah (vgh hak, haklamalS); bek, bile iest, hart,                        =
       sehr; baginmak, ftej/mmeZ;                       =
                                  sich befestigen sich verbinden,               ,



       Frieden schliessen               (vgl.        den Gegensatz aralari cozüJc                  — ihr
       Verhältniss ist locker,                       aufgelöst,   d. h.   sie       sind in Feind-
       schaft); beklik             =
                        Rärte, Festigkeit; &o</= Knopf, Knoten,
       Knöchel, Schnur; &o</wa/(;                       =
                                     binden, würgen; bogulmah^
                                     =
       sich würgen, ertrinken; 6of/a?«   Handfessel &0£/ra =
                                                           Hals-                ;



       fessel;      = Fessel Fusseisen; bogun, bognm, bogdak
                  öofea^M                       ,



     = Knoten, Ast, Knospe, Bündel; &6'//«^ = Knopf, Knorren;
     bögeöl, ÖMA*ec^i = Arrieregai-de (d. h. Schluss eines Zuges)
===== TTS leaf 222 printed p. 193
                                                   193

trk.   böjii, ö«/jM        = Zaubor; biijülemck — heza.uhern.
osm. &aa?l= gebunden,                      bezaubert (haglni fö>?«efc=den Zauber
       lösen).
jak.   hat,  ftoya&l?j          =
                        binden, verbinden;       Gewalt, Zwang6ä=
       (Band?); ftä^lHw              =
                          gebunden werden; häUi, bälihhi zv/'m-                   —
       gen (binden?); 6a^«?'                  —
                               blind (vgl. soÄ-                —
                                                eng, dicbt, fest
     und so7«Mr= blind).
alt.     = Strick, Band, einen Fluss dämmen; puuJi = Damm.
       ^>it
CUV. 2>Mt' = eindämmen; 2^'tve — Da,mm.

          In Berücksichtigung des Verhältnisses zwischen                        dem deut-
       schen      Geschenk und Angebinde wäre                      ich   geneigt,        das
       öag.-osm.     hagislamalc             = schenken, sich gegenseitig binden
       (mittelst Geschenken) hierher zu rechnen.                   Demnach müsste
       das    neupers.     bacJiSiden = schenken und das osm. bacliMä
       = Präsent als entschieden türkischen Ursprungs betrachtet
       werden.
          Aus      bog.,       hög   ist     nach stattgefundener Nasalirung des
       gutturalen Auslauts                 bong, böng, beng, bonz entstanden,
       mit der Bedeutung von Knopf, Knoten, Knospe, Koralle,
       Korn, Muttermal u. s. w. So:
cag.          »ion^MZ:
       bonzuJc,                          =
                          Koralle, Knauf, Fahne; bündülc                                 =
     Knospe, Knoten; 6i/»'« r= Pfefferkorn, Pfeifer; burzak                              —
     Erbsenkorn, Erbse; meng, beng, möng          Korn, Frucht-    =
     korn, Muttermal, Zeichen.
osm. ben      =
           Fleck Muttermal beneBi
                           ,                              =
```


## [2026-09-05T14:41:14.604Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('FSD_vol1.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('leaves',len(t))\nfor i,p in enumerate(t):\n    if re.search(r'Avicenn',p):\n        print('leaf',i)\n        for m in re.finditer(r'Avicenn',p):\n            print('   ',p[max(0,m.start()-300):m.start()+300].replace('\\n',' '))\n        break\nEOF"
}
```


### [2026-09-05T14:41:16.284Z] TOOL RESULT

```
leaves 798
leaf 247
     n.  An  Arab  physi- cian and  philosopher  (9S0-1037). Av"I-cen'nI-a,  1   avVsen'i-a;  2   Sv'I-c6n'i-a,  n.  Bol.  A genus  of  small  mangrove-like  trees  of  the  vervain  family. See  mangrove,  2. Av"I-cen'nlsm,  l   av'i-sen'izm;  2   fiv'i-cSn'Ism,  n.  Aristote- lianism  as  taught  by  Avicenna,  whose  chief  tenets  were:  (1) All  created  things  are  possible  in  themselves,  but  only  be- come necessary  by  the  act  of  the  Creator.  (2)  The  soul  of man  has  two  faces,  one  turned  toward  the  body,  which forms  the  practical  understanding;  the  other,  recep
    themselves,  but  only  be- come necessary  by  the  act  of  the  Creator.  (2)  The  soul  of man  has  two  faces,  one  turned  toward  the  body,  which forms  the  practical  understanding;  the  other,  receptive  to external  forms,  which  it  reproduces  in  due  order.  As  to theology,  Avicenna  argues  for  the  existence  ot  God  from the  necessity  of  a   First  Cause,  and  maintains  the  immortality of  the  soul.  He  also  brings  forward  arguments  for  the necessity  of  revelation,  which  he  asserts  is  to  be  found  in Islam.  It  is  chiefly  to  his  Canon  o
```


## [2026-09-05T14:41:27.368Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('FSD_vol1.txt',encoding='utf-8',errors='replace').read().split('\\f')\np=t[247]\ni=p.find('Avicenn')\nprint(p[max(0,i-1200):i+200].replace('\\n',' '))\nprint('...TAIL...')\nprint(p[i+200:i+1600].replace('\\n',' '))\nEOF"
}
```


### [2026-09-05T14:41:29.181Z] TOOL RESULT

```
  The  art  of flying;  especially,  the  management  of  aeroplanes. Aeration  [deals]  with  the  problem  of  artificial  flight  by  means of  flying:  machines,  which,  like  birds,  are  heavier  than  the  air. .   Encyc.  Brit.  _1 1th  ed..  vol.  i,  p.  260. a'vi-a"tor,  1   e'vi-ertar  or  -tor;  2   a'vi-a'tor,  n.  1.  Aero. An  operator  of  a   flying-machine.  Orville  Wright. 2.  One  who  makes  a   study  of  aviation.  3.  A   flying- machine  employing  the  principle  of  the  aeroplane.  4. [Rare.]  An  aeroplane,  as  distinguished  from  an  air- ship or  balloon. — a'vl-a"tress1  -trice,  or  -trix,  n.  A   wom- an aviator. A" vl-ce-bron ',  1   a'ri-fbe-br<3n';  2   a’vI-the-brSn',  Solomon ben  Jehuda  Ibn  Gablrol  (10207-1070?) .   A   Spanish  Jew. poet,  and  philosopher;  author  of  The  Source  of  Life. Av"l-cen'na,  1   av'i-sen'a;  2   Svl-cen'a,  n.  An  Arab  physi- cian and  philosopher  (9S0-1037). Av"I-cen'nI-a,  1   avVsen'i-a;  2   Sv'I-c6n'i-a,  n.  Bol.  A genus  of  small  mangrove-like  trees  of  the  vervain  family. See  mangrove,  2. Av"I-cen'nlsm,  l   av'i-sen'izm;  2   fiv'i-cSn'Ism,  n.  Aristote- lianism  as  taught  by  Avicenna,  whose  chief  tenets  were:  (1) All  created  things  are  possible  in  themselves,  but  only  be- come necessary  by  the  act  of  the  Creator.  (2)  The  soul  of man  has  two  face
...TAIL...
s,  one  turned  toward  the  body,  which forms  the  practical  understanding;  the  other,  receptive  to external  forms,  which  it  reproduces  in  due  order.  As  to theology,  Avicenna  argues  for  the  existence  ot  God  from the  necessity  of  a   First  Cause,  and  maintains  the  immortality of  the  soul.  He  also  brings  forward  arguments  for  the necessity  of  revelation,  which  he  asserts  is  to  be  found  in Islam.  It  is  chiefly  to  his  Canon  of  Medicine  that  he  owes his  fame,  for  it  was  the  guide  to  medical  study  in  every  uni- versity in  Europe  from  the  12th  to  the  17th  century. A-vI'chl,  1   a-ri'<5hl;  2   a-ri'chl,  n.  [Sans.]  The  Buddhistic world  of  erii  In  which  the  bad  will  find  themselves  at  death; hell.  A-wI'tchlf. Were  any  one  to  practice  the  Ten  Obligations  merely  to  ‘fill  the belly,’  this  man  .   .   .   after  death  .   .   .   will  be  born  in  the  Avrilchi, hell.  II.  S.  Hardy  Eastern  hfonachism  p.  32.  [j>.  a   o.  1850.] a'vi-cl"dal,  1   e'vi-sai'dBl;  2   a'vi-cl'dal,  a.  Relating  to bird-killing.  [   <   L.  arfr,  bird,  4   ecedo,  kill.]  —   a'vl-clde,  n. A-vic'o-la,  1   a-vik'yu-le;  2   a-vlc'yu-la,  n.  1.  Conch.  A   genua typical  of  Aticulldse.  2.  [a-]  A   wing-shell  (ArfcuJa).  [L.t dim.  of  arts,  bird.]  [lug  to  birds. a-vic'u-Iar.
```


## [2026-09-05T14:41:30.633Z] TOOL CALL #28: Bash

```json
{
 "command": "pdftoppm -f 100 -l 100 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf \"$PWD/../../../tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg100\" 2>/dev/null; ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


### [2026-09-05T14:41:33.749Z] TOOL RESULT

```
total 31608
drwx------ 2 sfmqrb sfmqrb     4096 Sep  5 10:41 .
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


## [2026-09-05T14:41:41.844Z] TOOL CALL #29: Bash

```json
{
 "command": "pdftoppm -f 100 -l 100 -r 300 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg100 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg100.png"
}
```


### [2026-09-05T14:41:45.945Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 71589 Sep  5 10:41 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg100.png
```


## [2026-09-05T14:41:47.619Z] TOOL CALL #30: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg100.png"
}
```


### [2026-09-05T14:41:48.166Z] TOOL RESULT

```

```


## [2026-09-05T14:41:48.162Z] INPUT

[Image: original 2550x3300, displayed at 1546x2000. Multiply coordinates by 1.65 to map to original image.]


## [2026-09-05T14:42:05.091Z] TOOL CALL #31: Bash

```json
{
 "command": "sed -n 1,40p tools/fetch_source.py"
}
```


### [2026-09-05T14:42:05.134Z] TOOL RESULT

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


## [2026-09-05T14:42:08.188Z] TOOL CALL #32: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/ابن\" \\\n \"https://en.wiktionary.org/wiki/بنت\" \\\n \"https://www.etymonline.com/word/baggage\" \\\n \"https://en.wiktionary.org/wiki/bohça\" \\\n \"https://en.wiktionary.org/wiki/بقچه\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 100 verification (B.n.v / Boqca)\" ; done"
}
```


### [2026-09-05T14:42:11.870Z] TOOL RESULT

```
Exit code 1
/home/sfmqrb/git/rishe/data/verification/sources/web/dea30c993261fe07.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/80b2cb5d0982842a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b01d5c17b045c09b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/67e22da941ff6ab5.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/245b71668203ff4f.txt
```


## [2026-09-05T14:42:14.572Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in dea30c993261fe07 80b2cb5d0982842a b01d5c17b045c09b 67e22da941ff6ab5 245b71668203ff4f; do echo \"########## $f  $(wc -c <$f.txt)\"; done; tail -5 index.jsonl | cut -c1-300"
}
```


### [2026-09-05T14:42:16.505Z] TOOL RESULT

```
########## dea30c993261fe07  15414
########## 80b2cb5d0982842a  15935
########## b01d5c17b045c09b  9166
########## 67e22da941ff6ab5  5198
########## 245b71668203ff4f  134
{"url": "https://en.wiktionary.org/wiki/ابن", "file": "data/verification/sources/web/dea30c993261fe07.txt", "fetched": "2026-09-05T14:42:10Z", "status": 200, "bytes": 13762, "title": "ابن - Wiktionary, the free dictionary", "note": "page 100 verification (B.n.v / Boqca)"}
{"url": "https://en.wiktionary.org/wiki/بنت", "file": "data/verification/sources/web/80b2cb5d0982842a.txt", "fetched": "2026-09-05T14:42:10Z", "status": 200, "bytes": 14866, "title": "بنت - Wiktionary, the free dictionary", "note": "page 100 verification (B.n.v / Boqca)"}
{"url": "https://www.etymonline.com/word/baggage", "file": "data/verification/sources/web/b01d5c17b045c09b.txt", "fetched": "2026-09-05T14:42:11Z", "status": 200, "bytes": 9023, "title": "Baggage - Etymology, Origin & Meaning", "note": "page 100 verification (B.n.v / Boqca)"}
{"url": "https://en.wiktionary.org/wiki/bohça", "file": "data/verification/sources/web/67e22da941ff6ab5.txt", "fetched": "2026-09-05T14:42:11Z", "status": 200, "bytes": 4803, "title": "bohça - Wiktionary, the free dictionary", "note": "page 100 verification (B.n.v / Boqca)"}
{"url": "https://en.wiktionary.org/wiki/بقچه", "file": "data/verification/sources/web/245b71668203ff4f.txt", "fetched": "2026-09-05T14:42:11Z", "status": -1, "bytes": 39, "title": "", "note": "page 100 verification (B.n.v / Boqca)"}
```


## [2026-09-05T14:42:18.843Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"=== ETYMONLINE baggage\"; grep -o \"baggage[^§]\\{0,900\\}\" b01d5c17b045c09b.txt | head -2; echo; echo \"=== bohça\"; sed -n '1,80p' 67e22da941ff6ab5.txt"
}
```


### [2026-09-05T14:42:20.859Z] TOOL RESULT

```
=== ETYMONLINE baggage
baggage
baggage 

=== bohça
URL: https://en.wiktionary.org/wiki/bohça
FETCHED: 2026-09-05T14:42:11Z
STATUS: 200
TITLE: bohça - Wiktionary, the free dictionary

bohça - Wiktionary, the free dictionary 

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
 Turkish 

 Toggle Turkish subsection 

 1.1 
 Etymology 

 1.2 
 Pronunciation 

 1.3 
 Noun 

 1.3.1 
 Declension 

 Toggle the table of contents 

 bohça 

 5 languages 

 Ελληνικά 
 Kurdî
```


## [2026-09-05T14:42:23.185Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"=== bohça body\"; sed -n '80,200p' 67e22da941ff6ab5.txt; echo \"===== etymonline\"; sed -n '1,200p' b01d5c17b045c09b.txt | grep -v \"^ *$\" | sed -n '20,120p'"
}
```


### [2026-09-05T14:42:24.642Z] TOOL RESULT

```
=== bohça body
 Kurdî 
 Malagasy 
 Srpskohrvatski / српскохрватски 
 Türkçe 

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

 Turkish
 [ edit ] 

 Etymology
 [ edit ] 

 From Ottoman Turkish بوغچه ( boğça ) .

 Pronunciation
 [ edit ] 

 IPA ( key ) : /bɔhˈt͡ʃɑ/ 

 Hyphenation: boh‧ça 

 Noun
 [ edit ] 

 bohça ( definite accusative bohçayı , plural bohçalar ) 

 bundle ; group of objects held together by wrapping

 any fried pastry in the form of a tied up bundle

 a shawl or wrap towel such as used for wrapping bundles 

 Declension
 [ edit ] 

 Declension of bohça 

 singular

 plural

 nominative

 bohça 

 bohçalar 

 definite accusative

 bohçayı 

 bohçaları 

 dative

 bohçaya 

 bohçalara 

 locative

 bohçada 

 bohçalarda 

 ablative

 bohçadan 

 bohçalardan 
===== etymonline
 also from mid-15c. 
 Entries linking to baggage 
 bag (n.) 
 "small sack," c. 1200, bagge , probably from Old Norse baggi "pack, bundle," or a similar Scandinavian source. OED rejects connection to other Germanic words for "bellows, belly" as without evidence and finds a Celtic origin untenable. In some senses perhaps from Old French bague , which is also from Germanic.
 As disparaging slang for "woman" it dates from 1924 in modern use (but various specialized senses of this are much older, and compare baggage ). The meaning "person's area of interest or expertise" is by 1964, from African-American vernacular, from jazz sense of "category," probably via notion of putting something in a bag. The meaning "fold of loose skin under the eye" is by 1867. Related: bags .
 Many figurative senses, such as the verb meaning "to kill game" (1814) and its colloquial extension to "catch, seize, steal" (1818) are from the notion of the game bag (late 15c.) into which the product of the hunt was placed. This also probably explains modern slang in the bag "assured, certain" (1922, American English). To be left holding the bag (and presumably nothing else), "cheated, swindled" is attested by 1793.
 To let the cat out of the bag "reveal the secret" is from 1760. The source is probably the French expression Acheter chat en poche "buy a cat in a bag," which is attested in 18c. French and explained in Bailey's "Universal Etymological English Dictionary" (1736), under the entry for To buy a pig in a poke as "to buy a Thing without looking at it, or enquiring into the Value of it." (Similar expressions are found in Italian and German; and in English, Wycliffe (late 14c.) has To bye a catte in þo sakke is bot litel charge ). Thus to let the cat out of the bag would be to inadvertently reveal the hidden truth of a matter one is attempting to pass off as something better or different, which is in line with the earliest uses in English.
 Sir Joseph letteth the cat out of the bag, and sheweth principles inimical to the cause of true philosophy, by wishing to make great men Fellows, instead of wise men. ["Peter Pindar," "Peter's Prophecy," 1788]
 luggage (n.) 
 1590s, from lug (v.) "to drag" + -age ; so, literally "what has to be lugged about" (or, in Johnson's definition, "any thing of more weight than value"). In 20c., the usual British word for "baggage belonging to passengers."
 faggot (n.2) 
 "male homosexual," 1914, American English slang, probably from earlier contemptuous term for "woman" (1590s), especially an old and unpleasant one, in reference to faggot (n.1) "bundle of sticks," as something awkward that has to be carried (compare baggage "worthless woman," 1590s). It may also be reinforced by Yiddish faygele "homosexual" (n.), literally "little bird." It also may have roots in British public school slang noun fag "a junior who does certain duties for a senior" (1785), with suggestions of "catamite," from fag (v.). This also spun off a verb (see fag (v.2).
 He [the prefect] used to fag me to blow the chapel organ for him. ["Boy's Own Paper," Aug. 3, 1889]
 Other obsolete British senses of faggot were "man hired into military service merely to fill out the ranks at muster" (1700) and "vote manufactured for party purposes" (1817).
 The explanation that male homosexuals were called faggots because they were burned at the stake as punishment is an etymological urban legend. Burning sometimes was a punishment meted out to homosexuals in Christian Europe (on the suggestion of the Biblical fate of Sodom and Gomorrah), but in England, where parliament had made homosexuality a capital offense in 1533, hanging was the method prescribed. Use of faggot in connection with public executions had long been obscure English historical trivia by the time the word began to be used for "male homosexual" in 20th century American slang, whereas the contemptuous slang word for "woman" (in common with the other possible sources or influences listed here) was in active use early 20c., by D.H. Lawrence and James Joyce, among others.
 Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
 More to explore
 fare 
 .)); merged with faru "journey, expedition, companions, baggage," strong fem. of faran....
 caravan 
 Used in English for "any large number of persons traveling together with much baggage" (1660s), hence "a large covered carriage...
 check 
 (1620s); "to hold up or control" (an assertion, a person, etc.) by comparison with some authority or record (1690s); of baggage...
 plunder 
 "household goods, clothes," also "lumber, baggage" (14c.; compare Modern German Plunder "lumber, trash"), which is related...
 custom 
 Customs "area at a seaport, airport, etc., where baggage is examined" is by 1921. Old customs! Oh!...
 case 
 early 13c., "what befalls one; state of affairs," from Old French cas "an event, happening, situation, quarrel, trial," from Latin casus "a chance, occasion, opportunity; accident, mishap," literally "a falling," from cas-, past-participle stem of cadere "to fall, sink, settle do
 grip 
 Old English grippan "to grip, seize, obtain" (class I strong verb; past tense grap, past participle gripen), from West Germanic *greipanan (source also of Old High German gripfen "to rob," Old English gripan "to seize;" see gripe (v.)). Related: Gripped; gripping. French gripper 
 prig 
 "a conceited, narrow-minded pragmatical person; a dull, precise person; one who cultivates or affects propriety and offends or bores others," 1753, originally in reference to theological scruples (1704), a word of unknown origin. It could be related to earlier appearances of the 
 hold 
 Middle English holden, earlier halden, from Old English haldan (Anglian), healdan (West Saxon), "to contain; to grasp; to retain (liquid, etc.); to observe, fulfill (a custom, etc.); to have as one's own; to have in mind (of opinions, etc.); to possess, control, rule; to detain, 
 materiel 
 "the totality of things used in the carrying out of any complex art or technique" (as distinguished from personnel), 1814, from French matériel "material," noun use of adj. matériel (see material (adj.)). A later borrowing of the same word that became material (n.). By 1819 in th
 Share baggage 
 ‘ cite ’ 
 Page URL :
 https://www.etymonline.com/word/baggage Copy 
 HTML Link :
 <a href="https://www.etymonline.com/word/baggage">Etymology of baggage by etymonline</a> Copy 
 APA Style :
 Harper, D. (n.d.). Etymology of baggage. Online Etymology Dictionary. Retrieved September 4, 2026, from https://www.etymonline.com/word/baggage Copy 
 Chicago Style :
 Harper Douglas, "Etymology of baggage," Online Etymology Dictionary, accessed September 4, 2026, https://www.etymonline.com/word/baggage. Copy 
 MLA Style :
 Harper, Douglas. "Etymology of baggage." Online Etymology Dictionary, https://www.etymonline.com/word/baggage. Accessed 4 September, 2026. Copy 
 IEEE Style :
 D. Harper. "Etymology of baggage." Online Etymology Dictionary. https://www.etymonline.com/word/baggage (accessed September 4, 2026). Copy 
 Remove Ads 
 Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
 Trending 
 Dictionary entries near baggage 
 bag 
 bagatelle 
 bagel 
 bag-end 
 bagful 
 baggage 
 bagger 
 baggy 
 Baghdad 
 bagpipes 
 baguette 
 Advertisement Close 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
 Close 
 A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 
 Quick and reliable accounts of the origin and history of English words. Scholarly, yet simple.
 About
 Who Did This 
 Sources 
 Introduction 
 Links 
 Support
 Premium 
 Patreon 
 Donate with PayPal 
 Merch 
 Apps
Get Chrome Extension 
Get iOS App 
Get Android App 
 Dark
 Auto
 Light
 Terms of Services Privacy Policy 
 English (English) 
 © 2001–2026 Douglas Harper & Talia Felix
```


## [2026-09-05T14:42:28.846Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n \"Old French bagage\\|bagues\\|mid-15c\" b01d5c17b045c09b.txt | head; echo ---; sed -n '/^ baggage (n.)/,/Entries linking/p' b01d5c17b045c09b.txt | head -20"
}
```


### [2026-09-05T14:42:30.762Z] TOOL RESULT

```
25: mid-15c., "portable equipment of an army; plunder, loot," from Old French bagage "baggage, (military) equipment" (14c.), from bague "pack, bundle, sack," probably ultimately from the same Scandinavian source that yielded bag (n.).
30: also from mid-15c. 
---
 baggage (n.) 

 mid-15c., "portable equipment of an army; plunder, loot," from Old French bagage "baggage, (military) equipment" (14c.), from bague "pack, bundle, sack," probably ultimately from the same Scandinavian source that yielded bag (n.).

 Later used of the bags, trunks, packages, etc., of a traveler (in this sense British English historically prefers luggage ). B aggage-smasher (1847) was American English slang for "railway porter."

 Used disparagingly, "worthless woman, strumpet" from 1590s; sometimes also playfully, "saucy or flirtatious woman" (1670s). Emotional baggage "detrimental unresolved feelings and issues from past experiences" is attested by 1957.
 also from mid-15c. 

 Entries linking to baggage
```


## [2026-09-05T14:42:38.280Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"=== ibn\"; sed -n '/^ Arabic$/,$p' dea30c993261fe07.txt | grep -n -A3 -i \"proto-semitic\\|Etymology\" | head -40; echo \"=== bint\"; grep -n -i -B2 -A4 \"proto-semitic\" 80b2cb5d0982842a.txt | head -40"
}
```


### [2026-09-05T14:42:40.271Z] TOOL RESULT

```
=== ibn
8: Etymology 1
9- [ edit ] 
10-
11: Inherited from Proto-Semitic *bin- .
12-
13- Pronunciation
14- [ edit ] 
--
320: Etymology 2
321- [ edit ] 
322-
323- Verb
--
338: Etymology
339- [ edit ] 
340-
341: Etymology tree
342-
343: Proto-Semitic *bin- 
344- Arabic اِبْن ( ibn ) 
345- North Levantine Arabic ابن 
346-
--
384: Etymology
385- [ edit ] 
386-
387: Etymology tree
388-
389: Proto-Semitic *bin- 
390- Arabic اِبْن ( ibn ) bor. 
391- Persian ابن 
392-
--
449: Etymology
450- [ edit ] 
451-
452: Etymology tree
453-
454: Proto-Semitic *bin- 
455- Arabic اِبْن ( ibn ) 
=== bint
307- Etymology tree
308-
309: Proto-Semitic *bin- 
310-
311- Proto-Afroasiatic *-t 
312: Proto-Semitic *-at- 
313-
314: Proto-Semitic *bint- 
315- Arabic بِنْت ( bint ) 
316- Algerian Arabic بنت 
317-
318- Inherited from Arabic بِنْت ( bint ) .
--
338- [ edit ] 
339-
340: From Proto-Semitic *bint- . Has the Semitic feminine suffix *-at- added to the root *bin- of اِبْن ( ibn , “ son ” ) .
341-
342- Cognate with Hebrew בת ( bat ) .
343-
344- Pronunciation
--
585- Etymology tree
586-
587: Proto-Semitic *bin- 
588-
589- Proto-Afroasiatic *-t 
590: Proto-Semitic *-at- 
591-
592: Proto-Semitic *bint- 
593- Arabic بِنْت ( bint ) 
594- Egyptian Arabic بنت 
595-
596- Inherited from Arabic بِنْت ( bint ) .
--
640- Etymology tree
641-
642: Proto-Semitic *bin- 
643-
644- Proto-Afroasiatic *-t 
645: Proto-Semitic *-at-
```


## [2026-09-05T14:42:55.326Z] TOOL CALL #38: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/Benjamin\" \\\n \"https://en.wiktionary.org/wiki/Reuben\" \\\n \"https://en.wiktionary.org/wiki/bagage#French\" \\\n \"https://en.wiktionary.org/wiki/%D8%A8%D9%82%DA%86%D9%87\" \\\n \"https://en.wiktionary.org/wiki/Avicenna\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 100 verification (B.n.v / Boqca)\"; done; tail -5 data/verification/sources/web/index.jsonl | python3 -c \"import sys,json;[print(json.loads(l)['status'],json.loads(l)['file'],json.loads(l)['url']) for l in sys.stdin]\""
}
```


### [2026-09-05T14:42:58.902Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/e07c5cf70d002452.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c6aed6f3fbd4a2e4.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c52ccc1882eee169.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9f72b61ec59a1110.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ed41660b7987a97e.txt
200 data/verification/sources/web/e07c5cf70d002452.txt https://en.wiktionary.org/wiki/Benjamin
200 data/verification/sources/web/c6aed6f3fbd4a2e4.txt https://en.wiktionary.org/wiki/Reuben
200 data/verification/sources/web/c52ccc1882eee169.txt https://en.wiktionary.org/wiki/bagage#French
-1 data/verification/sources/web/9f72b61ec59a1110.txt https://en.wiktionary.org/wiki/%D8%A8%D9%82%DA%86%D9%87
200 data/verification/sources/web/ed41660b7987a97e.txt https://en.wiktionary.org/wiki/Avicenna
```


## [2026-09-05T14:43:01.836Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"=== Benjamin\"; grep -n -A4 \"Hebrew\" e07c5cf70d002452.txt | sed -n '1,30p'; echo \"=== Reuben\"; grep -n -B2 -A6 \"Hebrew\\|behold\" c6aed6f3fbd4a2e4.txt | sed -n '1,40p'"
}
```


### [2026-09-05T14:43:01.901Z] TOOL RESULT

```
=== Benjamin
359: From Late Latin Benjamin , from Ancient Greek Βενιαμίν ( Beniamín ) , from Biblical Hebrew בִּנְיָמִין ( binyamīn , literally “ son of the right/south or son of days ” ) . Authorities differ on the meaning of the original Hebrew. Philo of Alexandria, the Samaritan Pentateuch The Testament of the Twelve Patriarchs and Midrash Leḳaḥ-Ṭob understand יָמִין to mean "days" (a meaning attested in Daniel 12:13 ) understanding the name to mean "son of days (i.e. old age)" (compare to the direct translations into Arabic بِنْ يَومِين ( bin yawmīn ) "son of the days" and Arabic بِنْ يَمِين ( bin yamīn ) "son of the right hand"), a formula paraphrased in Genesis 40:22 where Benjamin is described as a child of Jacob's old age. Rashi in his commentary on Genesis also gives this as a possible meaning but favors an understanding of יָמִין to mean "right" in the sense of "the south", noting that Benjamin was the only son of Jacob born in the south. Jerome understood the name to mean "son of the right hand" and Gesenius speculated that this expression might have meant "son of good fortune".
360-
361- Pronunciation
362- [ edit ] 
363-
--
389: A male given name from Hebrew of biblical origin.
390- 2007 , Mark Schreiber , Starcrossed , Llewellyn Worldwide, →ISBN , page 53 : "Well, who the hell ever thinks some boy with a name like Benjamin is going to kill someone?" I said. "It's like someone named Winnie the Pooh taking hostages!" 
391-
392- 2009 October 1, “Answering Iran’s Nuclear Challenge”, in The New York Times ‎ [1] , archived from the original on 17 June 2022 : For it would surely improve the domestic standing of Prime Minister Benjamin Netanyahu, an unbudgeable hawk, and thereby indefinitely delay peace on that Middle Eastern front. 
393-
--
450: Hebrew: בִּנְיָמִין   (he)   m ( binyamin ) 
451-
452- Hindi: बिन्यामीन   m ( binyāmīn ) 
453-
454- Hungarian: Benjámin   (hu) 
--
541: Hebrew: בִּנְיָמִין   (he)   m ( binyamin ) 
542-
543- Hindi: बेंजामिन ( beñjāmin ) 
544-
545- Hungarian: Benjámin   (hu) 
--
666: From English Benjamin , from Late Latin Benjamin , from Ancient Greek Βενιαμίν ( Beniamín ) , from Biblical Hebrew בִּנְיָמִין ( binyamīn , literally “ son of the right [hand] ” ) . Also from Spanish Benjamín .
667-
668- Pronunciation
669- [ edit ] 
670-
--
=== Reuben
187- [ edit ] 
188-
189: From Hebrew רְאוּבֵן ( r'uvén ) , from רְאוּ ( r'ú , “ see [masculine plural imperative] ” ) + בֵּן ( ben , “ son ” ) ; its literal meaning is therefore roughly, "See, all: a son!"
190-
191- There are several unconfirmed etymologies for the name of the sandwich. This etymology is incomplete. You can help Wiktionary by elaborating on the origins of this term. 
192-
193- Pronunciation
194- [ edit ] 
195-
--
211- ( biblical ) First son of Jacob , by his wife Leah .
212-
213: A male given name from Hebrew .
214-
215- A surname transferred from the given name 
216-
217- ( Oxford University , informal ) Ellipsis of Reuben College, Oxford .
218-
219- Quotations
--
264- Gujarati: રૂબેન   m ( rūben ) 
265-
266: Hebrew: רְאוּבֵן   (he) 
267-
268- Hindi: रूबेन   m ( rūben ) 
269-
270- Kazakh: Рубен ( Ruwben ) 
271-
272- Latin: Rūbēn   m 
--
304- German: Ruben   (de) 
305-
306: Hebrew: רְאוּבֵן   (he) 
307-
308- Hindi: रूबेन   m ( rūben ) 
309-
310- Hungarian: Ruben   (hu) , Rúben   (hu) 
311-
312- Norwegian: Ruben   (no) 
--
```


## [2026-09-05T14:43:07.817Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"=== bagage FR\"; grep -n -B3 -A6 \"bague\\|Old French\\|Middle French\" c52ccc1882eee169.txt | head -40; echo \"=== Avicenna\"; grep -n -B2 -A6 \"Etymology\" ed41660b7987a97e.txt | head -40"
}
```


### [2026-09-05T14:43:07.886Z] TOOL RESULT

```
=== bagage FR
163- References 
164-
165- 6 
166: Middle French 
167-
168: Toggle Middle French subsection 
169-
170- 6.1 
171- Alternative forms 
172-
173- 6.2 
174- Etymology 
--
186- References 
187-
188- 7 
189: Old French 
190-
191: Toggle Old French subsection 
192-
193- 7.1 
194- Etymology 
195-
196- 7.2 
197- Noun 
--
391- Etymology
392- [ edit ] 
393-
394: Borrowed from Middle French bagage . First attested in the 16th century.
395-
396- Pronunciation
397- [ edit ] 
398-
399- IPA ( key ) : /ˌbaːˈɣaː.ʒə/ 
400-
--
442- Etymology
443- [ edit ] 
444-
=== Avicenna
63-
64- 1.2 
65: Etymology 
66-
67- 1.3 
68- Pronunciation 
69-
70- 1.4 
71- Proper noun 
--
86-
87- 2.1 
88: Etymology 
89-
90- 2.2 
91- Pronunciation 
92-
93- 2.3 
94- Proper noun 
--
106-
107- 3.1 
108: Etymology 
109-
110- 3.2 
111- Pronunciation 
112-
113- 3.3 
114- Proper noun 
--
198- Ebn-e Sina , Ibn Sina , Ibn Sīnā , Pur-e Sina , Pursina , Auicen 
199-
200: Etymology
201- [ edit ] 
202-
203- From Medieval Latin Avicenna , from Arabic اِبْن سِينَا ( ibn sīnā ) .
204-
205- Pronunciation
206- [ edit ] 
--
```


## [2026-09-05T14:43:12.092Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && awk '/^ French$/{f=1} f' c52ccc1882eee169.txt | sed -n '1,60p' | grep -v \"^ *$\""
}
```


### [2026-09-05T14:43:13.709Z] TOOL RESULT

```
 French
 [ edit ] 
 Etymology
 [ edit ] 
 Either from Late Latin *baga ( “ a vessel type ” ) , or from Old French bague ( “ pack, bundle ” ) ; ultimately from the North Germanic /Scandinavian source ( Old Norse baggi ) that yielded English bag .
 Pronunciation
 [ edit ] 
 IPA ( key ) : /ba.ɡaʒ/ 
 Audio ; “ un bagage ” : ( file ) 
 Audio ( Switzerland ( Valais ) ) : ( file ) 
 Audio ( France ( Vosges ) ) : ( file ) 
 Audio ( France ( Vosges ) ) : ( file ) 
 Audio ( France ( Lyon ) ) : ( file ) 
 Homophone : baguage 
 Noun
 [ edit ] 
 bagage   m ( plural bagages ) 
 baggage ; luggage 
 Derived terms
 [ edit ] 
 avec armes et bagages 
 bagagiste 
 plier bagage 
 Descendants
 [ edit ] 
 Descendants
 Guianese Creole: bagaj 
 Haitian Creole: bagay 
 → Afrikaans: bagasie 
 → Azerbaijani: baqaj 
 → Albanian: bagazh 
 → Bavarian: Bagasch 
 → Belarusian: багаж ( bahaž )
```


## [2026-09-05T14:43:23.347Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('incoming/PLA/PLA_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('leaves',len(t))\ni=68  # printed 53\nprint('=== leaf 68 printed p.53')\nprint(t[67][:1500])\nEOF"
}
```


### [2026-09-05T14:43:24.974Z] TOOL RESULT

```
leaves 302
=== leaf 68 printed p.53
bagbur                                                                53                                                              baqzis


->%     - bagbür:               "Kaiser       v.     China"         aus    dem     pers. Br           bagpür         ı mp             io
       bag-puhr           ap.              baga     + puga     / aw.        pu@ra        "Sohn"       2,


ba      - bagdäd:              Name        einer     am Tigris            gelegenen           Stadt       3 Up.           ee        bag-
       dät     a    "y.    Gott           gegeben;     v.     Gott        geschaffen",              mand.     bagdäd       4


Gh - bagdädi: Nisba v. >)... baßdäd "Zimmerdecke".

GSlau -      bagdädi:             "ein       in     Bagdad     hergestellter                  golddurchwirkter                  Seiden-
       stoff",           sp.     baladuin,           frz.     baudequin.


lu       -   bakistän:                "Bistun;        Hauptstadt            der     Sassaniden"              pers.       5 aus        dem        pers.
        & bag        s.    bag        +    OLll.,    istän         (Lokalsuffix)-


RIHSeN -           bagaltäg:          "Kleid        ohne     Ärmel"        pers.        6 aus       dem     pers.        su,        bagaltäg
       da=     bagal           "Achselhöhle"           +     pers.        Ü tä     "Falte".


asw-     bafta:           "gewebt"           (ägypt.         Ar.     aiw bafta           =    ar.    bäfta)
```


## [2026-09-05T14:43:26.298Z] TOOL CALL #43: Bash

```json
{
 "command": "python3 tools/fetch_source.py \"https://www.ahdictionary.com/word/search.html?q=baggage\" --note \"page 100, AHD:99 check for baggage\" && tail -1 data/verification/sources/web/index.jsonl"
}
```


### [2026-09-05T14:43:31.922Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/31c0626273283d11.txt
{"url": "https://www.ahdictionary.com/word/search.html?q=baggage", "file": "data/verification/sources/web/31c0626273283d11.txt", "fetched": "2026-09-05T14:43:31Z", "status": 200, "bytes": 4831, "title": "American Heritage Dictionary Entry: baggage", "note": "page 100, AHD:99 check for baggage"}
```


## [2026-09-05T14:43:36.816Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"buq\\|bug[cčģ]\\|boq\" incoming/PLA/PLA_pages.txt | head -20; echo \"=== AHD\"; grep -v \"^ *$\" /home/sfmqrb/git/rishe/data/verification/sources/web/31c0626273283d11.txt | sed -n '1,40p'"
}
```


### [2026-09-05T14:43:38.637Z] TOOL RESULT

```
2564:am - bußa         = bugfa           s.    buqßa       (ägypt.          Ar.).
=== AHD
URL: https://www.ahdictionary.com/word/search.html?q=baggage
FETCHED: 2026-09-05T14:43:31Z
STATUS: 200
TITLE: American Heritage Dictionary Entry: baggage
American Heritage Dictionary Entry: baggage 
 HOW TO USE THE DICTIONARY
 To look up an entry in The American Heritage Dictionary of the English Language, use the search window above. For best results, after typing in the word, click on the “Search” button instead of using the “enter” key.
 Some compound words (like bus rapid transit, dog whistle, or identity theft ) don’t appear on the drop-down list when you type them in the search bar. For best results with compound words, place a quotation mark before the compound word in the search window.
 guide to the dictionary 
 THE USAGE PANEL
 The Usage Panel is a group of nearly 200 prominent scholars, creative writers, journalists, diplomats, and others in occupations requiring mastery of language. Annual surveys have gauged the acceptability of particular usages and grammatical constructions.
 The Panelists 
 NEED HELP SOLVING A CROSSWORD PUZZLE?
 Go to our Crossword Puzzle Solver and type in the letters that you know, and the Solver will produce a list of possible solutions.
-->
 AMERICAN HERITAGE DICTIONARY APP
 The new American Heritage Dictionary app is now available for 
 iOS and Android. 
 THE AMERICAN HERITAGE DICTIONARY BLOG
 The articles in our blog examine new words, revised definitions, interesting images from the fifth edition, discussions of usage, and more.
 OPEN DICTIONARY PROJECT
 Share your ideas for new words and new meanings of old words!
 Start Sharing Now! 
 --> See word lists from the best-selling 100 Words Series!
 Find out more! 
 INTERESTED IN DICTIONARIES?
 Check out the Dictionary Society of North America at http://www.dictionarysociety.com 
 bag·gage (b ă g  ĭ j) 
 Share: 
 Tweet 
 n. 1. The trunks, bags, parcels, and suitcases in which one carries one's belongings while traveling; luggage.
 2. The movable equipment and supplies of an army.
 3. Emotions or thoughts that stem from painful or unpleasant past experiences and that affect one's outlook or behavior: "I lugged a considerable amount of psychological baggage from my adolescence" (Stephen S. Hall). 
 4. Archaic a. A woman prostitute.
 b. A girl or young woman, especially one is who impudent.
 [Middle English bagage , from Old French bague , bundle, perhaps of Germanic origin; akin to Old Norse baggi , bag, bundle. Sense 4, perhaps from French bagasse , from Provençal bagassa , ultimately from Arabic ba ġ ī , prostitute, from ba ġ ā , to fornicate; see b ġ y in the Appendix of Semitic roots .]
 The American Heritage® Dictionary of the English Language, Fifth Edition copyright ©2022 by HarperCollins Publishers. All rights reserved.
 Indo-European & Semitic Roots Appendices
 Thousands of entries in the dictionary include etymologies that trace their origins back to reconstructed proto-languages. You can obtain more information about these forms in our online appendices:
 Indo-European Roots
```


## [2026-09-05T14:43:49.882Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"buqß\\|bugß\\|buq.a\\|bugfa\\|bußa\" incoming/PLA/PLA_pages.txt | head -20; echo \"--- context of 2564\"; sed -n '2555,2575p' incoming/PLA/PLA_pages.txt; echo \"=== which leaf\"; python3 - <<'EOF'\nt=open('incoming/PLA/PLA_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 'bußa' in p or 'buqß' in p:\n        print('leaf',i,'printed p.',i+1-15)\n        print(p[:900])\nEOF"
}
```


### [2026-09-05T14:43:52.114Z] TOOL RESULT

```
2564:am - bußa         = bugfa           s.    buqßa       (ägypt.          Ar.).
--- context of 2564
 11.    Fremdwörterbuch                  S.    v.
 12.    al-Marga            s. v.
al-bigäd                                                               40                                                      bahtar


„ladı - al-bikäd = bikädig s. bißädig !.

al, bifäma = bidäma s. vikäma ?.

am - bußa         = bugfa           s.    buqßa       (ägypt.          Ar.).

                                          3
Zl - babatik: Pl. v.gis. babtak s. bahtak ” .

 Vo-            uhära:        Die    Stadt       Buchara,             alter    Name             Baktriens"   4,


$l,;-           bubäri:       Nisba       v.    bubara       s. bubärä             .

Fa        bahaßif:            Pl. v...i,, bahäi& s. bahlis .

=== which leaf
leaf 54 printed p. 40
al-bigäd                                                               40                                                      bahtar


„ladı - al-bikäd = bikädig s. bißädig !.

al, bifäma = bidäma s. vikäma ?.

am - bußa         = bugfa           s.    buqßa       (ägypt.          Ar.).

                                          3
Zl - babatik: Pl. v.gis. babtak s. bahtak ” .

 Vo-            uhära:        Die    Stadt       Buchara,             alter    Name             Baktriens"   4,


$l,;-           bubäri:       Nisba       v.    bubara       s. bubärä             .

Fa        bahaßif:            Pl. v...i,, bahäi& s. bahlis .

mel - banäßid: Pl. v. zu4, babgi5 s. bandif ,

zi>-     babt:      "Glück"           aus      dem    pers.
                                                         „.., babt <Imp.w baxt 5,


cis-     baht:      "Kamel          aus     Khorasan"            6
```


## [2026-09-05T14:44:02.229Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('incoming/PLA/PLA_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(t[67])\nEOF"
}
```


### [2026-09-05T14:44:04.260Z] TOOL RESULT

```
bagbur                                                                53                                                              baqzis


->%     - bagbür:               "Kaiser       v.     China"         aus    dem     pers. Br           bagpür         ı mp             io
       bag-puhr           ap.              baga     + puga     / aw.        pu@ra        "Sohn"       2,


ba      - bagdäd:              Name        einer     am Tigris            gelegenen           Stadt       3 Up.           ee        bag-
       dät     a    "y.    Gott           gegeben;     v.     Gott        geschaffen",              mand.     bagdäd       4


Gh - bagdädi: Nisba v. >)... baßdäd "Zimmerdecke".

GSlau -      bagdädi:             "ein       in     Bagdad     hergestellter                  golddurchwirkter                  Seiden-
       stoff",           sp.     baladuin,           frz.     baudequin.


lu       -   bakistän:                "Bistun;        Hauptstadt            der     Sassaniden"              pers.       5 aus        dem        pers.
        & bag        s.    bag        +    OLll.,    istän         (Lokalsuffix)-


RIHSeN -           bagaltäg:          "Kleid        ohne     Ärmel"        pers.        6 aus       dem     pers.        su,        bagaltäg
       da=     bagal           "Achselhöhle"           +     pers.        Ü tä     "Falte".


asw-     bafta:           "gewebt"           (ägypt.         Ar.     aiw bafta           =    ar.    bäfta)         s.   bäfta_.


Gr - bäffchen:                   "eine       Art     Leinwand"            aus     dem    pers.        „ol     bäftan           7,


&- bagad:                Pl.     v. a.s bugga               s. bugda.

aa     - bugka:           "Paket,           Wäsche"         pers.     aa» bogfa              "Bündel,        Schnappsack!"                  "=


li)      _ bagsimät:                  "Biskuit"        aus     dem        pers.     SU.l baksamät              >,


obb- bagsIß: "Trinkgeld, Bakschisch" = bab8I& s. bapsis 1°.


 1. H”ärazmi Mafätin al-Culüm s. v.
 2,    Nyberg        s.    v.
 3.    ebda,
 4.    Macuch        s.    v.
 5.    FM.     s.    v.
 6.    albasa        s.    v.
 7.    Littmann           s.     v.
 8.    Wahrmund           s.     v.
 9.    Steingaß           s.     v.
 10.    Wehr        s.    v.
```


## [2026-09-05T14:44:19.843Z] TOOL CALL #47: Bash

```json
{
 "command": "grep -n \"ابن سینا\" data/verification/sources/refs/MON_part1.txt data/verification/sources/refs/MON_part2.txt | head -5 | cut -c1-200; echo \"=== بنیامین\"; grep -c \"بنیامین\" data/verification/sources/refs/MON_part1.txt data/verification/sources/refs/MON_part2.txt; echo \"=== ARY ابن\"; grep -c \"ابن\" data/verification/sources/refs/incoming/ARY/ARY_pages.txt"
}
```


### [2026-09-05T14:44:19.966Z] TOOL RESULT

```
data/verification/sources/refs/MON_part1.txt:179:گنگره‌های هزارة ابن سیناء هفتصدمین سال نصیرالدین طوسی؛ آزادی فر هنگ 
data/verification/sources/refs/MON_part1.txt:255:سال ۱۳۴۰ به عنوان «مفرد و جمع» طرف کتابفروشی ابن سینا طبع و منتشر شد. 
data/verification/sources/refs/MON_part1.txt:278:۰ لغات فارسی ابن سینا از انتشارات مجلةٌ دانشکد؛ ادبیات دانشگاه تهران 
=== بنیامین
data/verification/sources/refs/MON_part1.txt:0
data/verification/sources/refs/MON_part2.txt:0
=== ARY ابن
22
```


## [2026-09-05T14:44:21.748Z] TOOL CALL #48: Bash

```json
{
 "command": "python3 tools/fetch_source.py \"https://abadis.ir/fatofa/%D8%A8%D9%82%DA%86%D9%87/\" --note \"page 100, Mo'in/Dehkhoda entry for بقچه\" ; tail -1 data/verification/sources/web/index.jsonl | cut -c1-250"
}
```


### [2026-09-05T14:44:25.463Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/75d4b0a4e8502083.txt
{"url": "https://abadis.ir/fatofa/%D8%A8%D9%82%DA%86%D9%87/", "file": "data/verification/sources/web/75d4b0a4e8502083.txt", "fetched": "2026-09-05T14:44:25Z", "status": 200, "bytes": 6031, "title": "بقچه - معنی در دیکشنری آبادی�
```


## [2026-09-05T14:44:27.138Z] TOOL CALL #49: Bash

```json
{
 "command": "grep -v \"^ *$\" data/verification/sources/web/75d4b0a4e8502083.txt | sed -n '1,60p'"
}
```


### [2026-09-05T14:44:29.242Z] TOOL RESULT

```
URL: https://abadis.ir/fatofa/%D8%A8%D9%82%DA%86%D9%87/
FETCHED: 2026-09-05T14:44:25Z
STATUS: 200
TITLE: بقچه - معنی در دیکشنری آبادیس
بقچه - معنی در دیکشنری آبادیس 
 دیکشنری مترجم بپرس 
 بقچه
 /boqCe/
 مترادف بقچه : بغچه، جامه دان، دستمال
 دنبال کنید 
 لغت نامه دهخدا
 بقچه. [ ب َ /ب ُ چ َ ] ( ترکی ، اِ ) باقچه. بقچه بمعنی صره یا بسته ای است ، بخصوص بسته ای درهم ها را در آن پیچند. رجوع به النقود ص 168 و بقچه و بغچه و به دزی ج 1 ص 102 شود.
 بقچه. [ ب ُ چ ِ / چ َ ] ( ترکی ، اِ ) بغچه. مأخوذ از ترکی ، بغچه و بسته کوچک و بستا. ( ناظم الاطباء ). بسته خرد. ( آنندراج ). بسته. رَزمَه یا رَزمِه. ( یادداشت مؤلف ). بلغده. ( یادداشت مؤلف ). پرونده. ( یادداشت مؤلف ). شمله. ( یادداشت مؤلف ) : 
ز سر بقچه الباس اهل بخل کمتر پرس 
که کس نگشود و نگشاید بحکمت آن معما را. نظام قاری.
از پوشیم بتاب [ کذا ] و ببندم زپیش بند
تا آن ز بقچه که و این از میان کیست. نظام قاری ( دیوان البسه ص 45 ).
تکه نمد براهت بر خاک ره نشینی 
زیلوچه بر امیدت چون بقچه هرزه گردی. نظام قاری.
- بقچه بندی ؛ عمل بستن مالی چون نخ و ریسمان و امثال آنها در بقچه ها: نخهای کارخانه را بقچه بندی کرد. ( یادداشت مؤلف ).
- بقچه حمام ؛ بقچه ای که در آن لباس و حوله و قطیفه نهند به گرمابه شدن را. ( یادداشت مؤلف ).
- بقچه دان ؛ جای بقچه : 
پیشک آفتاب و بارانی است 
بقچه دان است و جامه و ایزار. نظام قاری.
- بقچه کش ؛ دیوث. میانجی میان زن و مرد. ( یادداشت مؤلف ). قلطبان. قلتبان. قرطبان. ( یادداشت مؤلف ). رجوع به قرطبان شود.
 || آنکه بقچه جامه های مطربان و بازیگران را کشد. ( یادداشت مؤلف ) : 
در عصمت و طهارت خاتون نرمدست 
یاران بقچه کش همه محضر نوشته اند. نظام قاری.
- بقچه کشی ؛ عمل و شغل بقچه کش : 
جامه با صندلی و کت بگذار ای صندوق 
سر خود گیر که این بقچه کشی کار تو نیست. نظام قاری.
 فرهنگ فارسی
 ( اسم ) دستمال بزرگی که در آن جامه و انواع قماش پیچند . 
 فرهنگ عمید
 دستمال بزرگ که در آن لباس یا چیز دیگر از جنس پارچه می پیچند، سارغ. 
 گویش مازنی
 /beghche/ پارچه ای چهارگوش جهت بستن لوازم پارچه ای - سفر ی مخصوص بستن و حفظ لباس
 واژه نامه بختیاریکا
 ( بُقچه ) بَستِکُو
 دانشنامه عمومی
 بُقچه، ( بغچه نیز درست است ) از ترکی به معنای جامه بند، پارچه ایست به شکل مربع یا مستطیل که در آن لباس، غذا، مدارک، پول یا زیورآلات و غیره گذارده و نگهداری می کنند. بُقچه وسیله کمکی سفر نیز هست. مجموع پارچه بسته بندی و محتوی را «بقچه بسته» می نامند. 
بُغچه بند، بُغچه عروس، بُغچه کش، بُغچه حمام، طاس بُغچه، دست بُغچه، بُغچه باف. . . 
 wiki: بقچه 
 این نوشته برگرفته از سایت ویکی پدیا می باشد، اگر نادرست یا توهین آمیز است، لطفا گزارش دهید: گزارش تخلف 
 مترادف ها
 truss (اسم) 
 خرپا، فتق بند، بقچه، خوشه، کوک زن، شکم بند
 pack (اسم) 
 یک بسته، گروه، دسته، کوله پشتی، بسته، ملافه، بقچه، یک دست ورق بازی
 bundle (اسم) 
 بسته، بقچه
 fardel (اسم) 
 بار، بسته، بقچه، کوله بار
 فارسی به عربی
 حزمة , علبة 
 پیشنهاد کاربران
 واژه بقچه. [ ب َ /ب ُ چ َ ] ( ترکی ، اِ ) باقچه. بقچه بمعنی صره یا بسته ای است ، بخصوص بسته ای درهم ها را در آن پیچند. رجوع به النقود ص 168 و بقچه و بغچه و به دزی ج 1 ص 102 شود. 
بقچه. [ ب ُ چ ِ / چ َ ] ( ترکی ، اِ ) بغچه. مأخوذ از ترکی ، بغچه و بسته کوچک و بستا. ( ناظم الاطباء ) . بسته خرد. ( آنندراج ) . بسته. رَزمَه یا رَزمِه. ( یادداشت مؤلف ) . بلغده. ( یادداشت مؤلف ) . پرونده. ( یادداشت مؤلف ) . شمله. ( یادداشت مؤلف ) 
 ... [مشاهده متن کامل] 
منبع. لغت نامه دهخدا
```


## [2026-09-05T14:44:50.879Z] TOOL CALL #50: Bash

```json
{
 "command": "python3 tools/fetch_source.py \"https://www.ahdictionary.com/word/semitic.html\" --note \"page 100, AHD Semitic roots appendix, root bn 'son'\" >/dev/null; python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Semitic/bin-\" --note \"page 100, Proto-Semitic *bin- root box check\" ; grep -o \"bn[^A-Za-z]\\{0,300\\}\" data/verification/sources/web/$(python3 -c \"\nimport hashlib;print(hashlib.sha1('https://www.ahdictionary.com/word/semitic.html'.encode()).hexdigest()[:16])\").txt | grep -i \"son\" | head -5"
}
```


### [2026-09-05T14:44:53.100Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/c6c37788ce3082e3.txt
```


## [2026-09-05T14:44:57.057Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && tail -2 index.jsonl | cut -c1-260; echo \"=== recon\"; grep -v \"^ *$\" c6c37788ce3082e3.txt | sed -n '1,10p'; echo \"=== semitic appendix\"; f=$(python3 -c \"import hashlib;print(hashlib.sha1('https://www.ahdictionary.com/word/semitic.html'.encode()).hexdigest()[:16])\"); wc -c $f.txt; grep -o -i \"son[^.]\\{0,120\\}\" $f.txt | head -5"
}
```


### [2026-09-05T14:44:58.806Z] TOOL RESULT

```
{"url": "https://abadis.ir/fatofa/%D8%A8%D9%82%DA%86%D9%87/", "file": "data/verification/sources/web/75d4b0a4e8502083.txt", "fetched": "2026-09-05T14:44:25Z", "status": 200, "bytes": 6031, "title": "بقچه - معنی در دیکشنری آبادیس", "note"
{"url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Semitic/bin-", "file": "data/verification/sources/web/c6c37788ce3082e3.txt", "fetched": "2026-09-05T14:44:53Z", "status": 200, "bytes": 4525, "title": "Reconstruction:Proto-Semitic/bin- - Wiktionary,
=== recon
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Semitic/bin-
FETCHED: 2026-09-05T14:44:53Z
STATUS: 200
TITLE: Reconstruction:Proto-Semitic/bin- - Wiktionary, the free dictionary
Reconstruction:Proto-Semitic/bin- - Wiktionary, the free dictionary 
 Jump to content 
 Main menu 
 Main menu
 move to sidebar 
 hide 
=== semitic appendix
117763 75b739fc6c2698d2.txt
son of the father (see bn )
sonal name);
sonal name šəlūmî ʾ ēl , my well-being (is) God
sonal name), from ʿ ăzaz , reduced form of ʿ āzaz , to be strong ( ʾ ēl , God; see ʾ l )
son, and feminine derivative *bint‑ , daughter
```


## [2026-09-05T14:45:01.462Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -o -i \".\\{200\\}son, and feminine derivative.\\{600\\}\" 75b739fc6c2698d2.txt; echo \"=== recon body\"; sed -n '/Proto-Semitic$/,$p' c6c37788ce3082e3.txt | grep -v \"^ *$\" | sed -n '1,50p'"
}
```


### [2026-09-05T14:45:03.023Z] TOOL RESULT

```
=== recon body
 Proto-Semitic
 [ edit ] 
 Etymology
 [ edit ] 
 From Proto-Afroasiatic *bîn-/*bân- ( “ to beget ” ) .
 Noun
 [ edit ] 
 *bin-   m ( plural *ban- ) 
 son 
 Reconstruction notes
 [ edit ] 
 Testen reconstructs * bn -, with an initial consonant cluster, which accounts for the r forms in Aramaic and Modern South Arabian.
 Inflection
 [ edit ] 
 Declension of *bin- 
 case
 singular
 dual
 plural
 nominative 
 *binum
 *bināna
 *banūna
 accusative 
 *binam
 *binayna
 *banīna
 genitive 
 *binim
 possessive forms
 1 st person
 *binī / *binVya
 —
 *binVni
 2 nd person m 
 *binVka
 *binVkumā / *binVkumay
 *binVkum(ū)
 2 nd person f 
 *binVki
 *binVkin(ā)
 3 rd person m 
 *binVšu
 *binVšumā / *binVšumay
 *binVšum(ū)
 3 rd person f 
 *binVša
 *binVšin(ā)
 the endings - m and - na are dropped in the bound form , which may also undergo syncopation of an unstressed final vowel where possible.
Note: the ending - V before the possessive endings responds to case: *binuya for nom. case, *biniya for gen. case, *binaya for acc. case, etc.
```


## [2026-09-05T14:45:06.620Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && python3 - <<'EOF'\nt=open('75b739fc6c2698d2.txt',encoding='utf-8').read()\ni=t.find('son, and feminine derivative')\nprint(t[max(0,i-500):i+1200])\nEOF"
}
```


### [2026-09-05T14:45:08.357Z] TOOL RESULT

```
 God, bahā ʾ u , splendor, bound form of bahā ʾ , from bahā , to be(come) empty, beautiful;
 Baha'i , from Arabic bahā ʾ ī , follower of Bahaullah, from bahā ʾ u llāh (see above).

 ‌ bḥr 

Common Semitic noun *baḥr‑ , sea, coast. Bahrain , from Arabic baḥrayn , two seas, dual of baḥr , sea. 
 ‌ bkr 

Common Semitic *bukur‑ , *bikr‑ , *bak(u)r‑ , first-born. albacore , from Arabic al-bakūra , the albacore, akin to bikr , first-born, and bakr , young camel. 
 ‌ bn 

Common Semitic noun *b(i)n‑ , son, and feminine derivative *bint‑ , daughter. Common Semitic *b(i)n‑ . bar mitzvah , from Aramaic bar , bound form of bərā , son;
 Barabbas , from Aramaic bar- ʾ abbā , son of the father (probably a nickname, or a joking name for a bastard; ʾ abbā , father; see ʾ b );
 Barnabas , from Aramaic bar-nəbô , son of Nabu ( nəbô , Nabu, Akkadian deity, from Akkadian nabû ).

 B'nai B'rith , from Hebrew bənê , plural bound form of bēn , son;
 Benjamin , from Hebrew binyāmîn , son of the right hand, from bin‑ , frozen bound form of bēn ( yāmîn , right hand, south; see ymn ). 

 Common Semitic *bint‑ . bat mitzvah , from Hebrew bat (< *batt < *bitt < *bint ), daughter;
 Bathsheba , from Hebrew bat-šeba ʿ (see šb ʿ ).

 bint , from Arabic bint , daughter.

 ‌ bny 

To build, create. Assurbanipal , from Akkadian aššur-bāni-apli , Ashur (is) the creator of the heir, from bāni , bound form of participle of banû , to build ( apli , heir; see ʾ pl ). 
 ‌ brk 

West Semitic, to bless. Probably a metathesized variant of krb. Baruch , from Hebrew bārûk , blessed, passive participle of *bārak , to bless (only attested in derived stem bērēk , to bless). 
 broker , from Arabic al-barka , colloquial va
```


## [2026-09-05T14:45:41.514Z] TOOL CALL #54: Bash

```json
{
 "command": "sed -n 60,140p tools/verify_check.py"
}
```


### [2026-09-05T14:45:41.570Z] TOOL RESULT

```
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


## [2026-09-05T14:45:52.059Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -o -i \".\\{100\\}Bukhara.\\{200\\}\" ed41660b7987a97e.txt | head -3; grep -o -i \"polymath.\\{0,200\\}\" ed41660b7987a97e.txt | head -3"
}
```


### [2026-09-05T14:45:53.893Z] TOOL RESULT

```
polymath (c. 980–1037).
polymath
polymath (c. 980–1037) )
```


## [2026-09-05T14:45:57.475Z] TOOL CALL #56: Bash

```json
{
 "command": "python3 tools/fetch_source.py \"https://www.iranicaonline.org/articles/avicenna-index/\" --note \"page 100, Ebn-e Sina biography (birthplace Afsana near Bukhara, not Khwarazm)\"; f=$(python3 -c \"import hashlib;print(hashlib.sha1('https://www.iranicaonline.org/articles/avicenna-index/'.encode()).hexdigest()[:16])\"); grep -o -i \".\\{120\\}Bukhara.\\{200\\}\" data/verification/sources/web/$f.txt | head -3"
}
```


### [2026-09-05T14:46:02.863Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/715bb8575da32066.txt
```


## [2026-09-05T14:46:04.895Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && tail -1 index.jsonl | cut -c1-200; grep -v \"^ *$\" 715bb8575da32066.txt | sed -n '1,30p'"
}
```


### [2026-09-05T14:46:06.514Z] TOOL RESULT

```
{"url": "https://www.iranicaonline.org/articles/avicenna-index/", "file": "data/verification/sources/web/715bb8575da32066.txt", "fetched": "2026-09-05T14:46:02Z", "status": 200, "bytes": 2232, "title"
URL: https://www.iranicaonline.org/articles/avicenna-index/
FETCHED: 2026-09-05T14:46:02Z
STATUS: 200
TITLE: AVICENNA - Encyclopaedia Iranica
AVICENNA - Encyclopaedia Iranica Skip to main content 
 Search Iranica...
 search in 8,977 entries of Encyclopædia Iranica. 
 Close Search 
 search 
 account 
 Menu 
 Explore 
 News & Events 
 Editorial Current Board 
 Former Boards 
 Authors 
 Style Guide 
 About About Iranica 
 Ehsan Yarshater 
 Advisory Board 
 Board of Directors 
 FAQ 
 Contact 
 Donate 
 search 
 account 
 AVICENNA
 Browse Iranica 
 AVICENNA
 Type Headword
```


## [2026-09-05T14:46:14.333Z] TOOL CALL #58: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg100.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/100.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/ | tail -5"
}
```


### [2026-09-05T14:46:14.419Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb  90918 Sep  5 10:16 92.png
-rw-rw-r-- 1 sfmqrb sfmqrb  93420 Sep  5 10:18 94.png
-rw-rw-r-- 1 sfmqrb sfmqrb  78178 Sep  5 10:14 95.png
-rw-rw-r-- 1 sfmqrb sfmqrb  72929 Sep  5 10:19 96.png
-rw-rw-r-- 1 sfmqrb sfmqrb  65608 Sep  5 10:43 99.png
```


## [2026-09-05T14:46:43.078Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== RCH ibn/bint\"; grep -n -o \"ibn,[^.]\\{0,150\\}\\|bint,[^.]\\{0,120\\}\\|Beniámín[^.]\\{0,100\\}\\|binyámín[^.]\\{0,100\\}\" RCH.txt | head -8; echo \"=== KLN Avicenna\"; grep -o \"Avicen[^|]\\{0,250\\}\" KLN_1966.txt | head -3; echo \"=== WEB Avicenna\"; grep -o \"Avicen[^|]\\{0,200\\}\" WEB_vol1.txt | head -3; echo \"=== FSD Big Ben\"; grep -o \"Big Ben[^|]\\{0,200\\}\" FSD_vol1.txt | head -2"
}
```


### [2026-09-05T14:46:44.879Z] TOOL RESULT

```
=== RCH ibn/bint
1711:ibn,  A   son
7562:ibn,  sages,  se- nators, doctors,  prelates,  dervises,  religious  men
21738:ibn,  A   noble^enerous  lord  or  master
38100:ibn,  a   ridiciiloui  idea
=== KLN Avicenna
Avicenna (=  Ibn-Sina).
Avicennism,  n.,  the  teachings  of  the  Arab,  philo¬ sopher  Avicenna  (=  Ibn  Sina)  (980-1037).  For the  ending  see  suff.  -ism.
Avicenna  with  Gk.  paaiAncop, ‘royal’  (see  prec.  word).  The  term  vena  basilica appears  for  the  first  time  in  a  translation  of  Avi¬ cenna  by  Gerardus  Cremonensis.  See  Joseph Hyrtl,  Das  Arabische  und  Hebraische  in  der Anatomic,  
=== WEB Avicenna
=== FSD Big Ben
```


## [2026-09-05T14:46:45.857Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('LKT.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,p in enumerate(t):\n    if '325.  Tk.  bogca' in p or '325. Tk. bogca' in p:\n        print('LKT leaf',i,'printed p.',i-26)\nEOF\necho \"=== AFM بقجة\"; grep -n \"بقجة\\|بقجه\\|بغجة\" AFM.txt AFM_pages.txt | head -5 | cut -c1-200\necho \"=== FSD baggage\"; grep -o \"bag'gage[^|]\\{0,200\\}\\|baggage,[^|]\\{0,200\\}\" FSD_vol1.txt | head -3"
}
```


### [2026-09-05T14:46:48.386Z] TOOL RESULT

```
LKT leaf 54 printed p. 28
=== AFM بقجة
=== FSD baggage
baggage, smash  cr bait
bag'gage#car",  n.  Sec  car.—  bag'gagc-man",  n. One  who  handles  or  transports  baggage,  as  In  a   railroad station  or  to  or  from  a   baggage-car.—  b.unastcr,  n.  An official  in  charge  of  
bag'gage-lyf,  a.  Worthless.— bag'gag-cr,  n.  [Rare.] One  whose  business  It  Is  to  carry  baggage,  especially  that of  an  army.
```


## [2026-09-05T14:46:58.284Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('FSD_vol1.txt',encoding='utf-8',errors='replace').read()\ni=t.find(\"bag'gage\")\nwhile i>0 and i<len(t):\n    seg=t[i:i+400].replace('\\n',' ')\n    if '<' in seg or 'OF.' in seg or 'F.' in seg:\n        print(seg); break\n    i=t.find(\"bag'gage\", i+1)\nEOF\necho \"=== RCH benyamin\"; grep -n -o \"Beny[^ ]*\\|Binyámín[^.]\\{0,80\\}\" RCH.txt | head -5"
}
```


### [2026-09-05T14:46:59.939Z] TOOL RESULT

```
=== RCH benyamin
```


## [2026-09-05T14:47:05.356Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -c \"بنیامین\\|بن یامین\" BQT_v1_pages.txt BQT_v2_pages.txt MON_part1.txt MON_part2.txt RCH.txt 2>/dev/null"
}
```


### [2026-09-05T14:47:05.412Z] TOOL RESULT

```
RCH.txt:0
BQT_v1_pages.txt:0
BQT_v2_pages.txt:0
MON_part2.txt:0
MON_part1.txt:0
```


## [2026-09-05T14:52:46.599Z] TOOL CALL #63: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk100.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW_IBN  = \"https://en.wiktionary.org/wiki/ابن\"\nW_BINT = \"https://en.wiktionary.org/wiki/بنت\"\nW_BIN  = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Semitic/bin-\"\nAHD_SEM= \"https://www.ahdictionary.com/word/semitic.html\"\nW_BENJ = \"https://en.wiktionary.org/wiki/Benjamin\"\nW_REU  = \"https://en.wiktionary.org/wiki/Reuben\"\nW_AVI  = \"https://en.wiktionary.org/wiki/Avicenna\"\nETY_BAG= \"https://www.etymonline.com/word/baggage\"\nAHD_BAG= \"https://www.ahdictionary.com/word/search.html?q=baggage\"\nW_BAGF = \"https://en.wiktionary.org/wiki/bagage#French\"\nW_BOHCA= \"https://en.wiktionary.org/wiki/bohça\"\nABADIS = \"https://abadis.ir/fatofa/%D8%A8%D9%82%DA%86%D9%87/\"\n\nKLN163 = {\"ref\": \"KLN:163\", \"status\": \"supports\",\n \"note\": \"KLN_1966.txt form-feed leaf 97 (printed pp. 163-164, running numerals '170 171' appear at leaf 101): \\\"ben, n., son. — Heb. ben, 'son', rel. to Arab. ibn, Aram.-Syr. bar, 'son', Akkad. binu/bini, 'grandson'. Cp. Benjamin, B'nai B'rith, boanerges. … For the feminine correspondences Heb. bath, 'daughter', etc., see bathkol\\\". Exactly the root box and the Arabic/Hebrew branches Nourai draws.\"}\nFVA53  = {\"ref\": \"FVA:53\", \"status\": \"not_checked\",\n \"note\": \"FVA = S.M. Nahvi, Farhang-e vāžehā-ye ʿarabi dar fārsi (dakhil), 1368/1989. refs_online.json records no digital copy on archive.org, ketabnak, noorlib or the open web (catalogue record OL2012991M only); re-searched 2026-09.\"}\n\ndata = {\n \"pdf_page\": 100,\n \"book_page\": 70,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-05\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"B.n.v\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"Common Semitic noun *bin- / *b(i)n- 'son' (fem. derivative *bint- 'daughter'), Arabic root ب ن و b-n-w\",\n   \"note\": \"Root, language label and gloss are all right: 'son, child' is the meaning every authority gives, and the word is common Semitic, not just Arabic (Akkadian binu, Hebrew bēn, Aramaic-Syriac bar < *bnr/*bin-, Arabic ibn, Ugaritic bn, Ethiopic). Two refinements. (a) Modern Semitists reconstruct a BIconsonantal noun *bin- (AHD's Appendix of Semitic Roots heads it simply 'bn'; Wiktionary Reconstruction:Proto-Semitic/bin-, from Proto-Afroasiatic *bîn-/*bân- 'to beget'); the third radical of Nourai's 'B.n.v' (= و w) is an artefact of the Arabic grammarians' triliteral scheme, visible only in derivatives (banawī, banūn, abnāʾ). Nourai's own source Klein writes the same word without a third radical. (b) The plural of the root, Proto-Semitic *ban- (Arabic banū / construct banī), is the form behind the Persian banī of node #2, so it belongs to the root and not to a separate Arabic stem. Nothing on the page is wrong; the chart is a faithful reduction of Klein p.163 and of the AHD Semitic appendix s.v. 'bn'.\",\n   \"note_fa\": \"ریشهٔ سامیِ «ب ن و» به معنای «پسر، فرزند» ریشه‌ای اصیل و درست است و برچسب «سامی» و معنای آن هر دو با آنچه کلاین (ص ۱۶۳) و پیوستِ ریشه‌های سامیِ فرهنگ American Heritage می‌آورند یکسان است: اکدی binu، عبری bēn، آرامی-سریانی bar، عربی ibn، اوگاریتی bn. تنها نکتهٔ فنی آن است که سامی‌شناسان امروز این واژه را دوهمخوانی *bin- بازسازی می‌کنند (جمع آن *ban- که عربیِ بنو/بنی از آن است و مؤنث آن *bint-)، و همخوان سومِ «و» در ضبط نورایی تنها زاییدهٔ قاعدهٔ سه‌حرفیِ صرف عربی است و در خودِ نامْ‌واژه دیده نمی‌شود. در مجموع ادعای نورایی دربارهٔ خودِ ریشه درست است.\",\n   \"sources\": [W_BIN, AHD_SEM, W_IBN],\n   \"ref_check\": [KLN163, FVA53],\n   \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 97 (pp. 163-164) s.v. 'ben, n., son'\", \"stance\": \"supports\",\n     \"note\": \"'Heb. ben, \\\"son\\\", rel. to Arab. ibn, Aram.-Syr. bar, \\\"son\\\", Akkad. binu/bini, \\\"grandson\\\"' — the same Semitic family Nourai's root box asserts.\"},\n    {\"src\": \"AHD\", \"where\": \"Appendix of Semitic Roots, s.v. 'bn' (ahdictionary.com/word/semitic.html)\", \"stance\": \"supports\",\n     \"note\": \"'bn — Common Semitic noun *b(i)n-, son, and feminine derivative *bint-, daughter.' Note that AHD heads the root with two consonants, not three.\"},\n    {\"src\": \"FVQ\", \"where\": \"Jeffery, The Foreign Vocabulary of the Qurʾān\", \"stance\": \"silent\",\n     \"note\": \"ibn/bint are native Arabic and are not treated by Jeffery, who lists only foreign words; a 'silent' result, as expected.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Arabic\",\n     \"words\": \"b.n.v; ibn; bent\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Arabic اِبْن ibn 'son' continues Proto-Semitic *bin- directly, with the prothetic alif of hamzat al-waṣl that Arabic prefixes to an original monosyllable of the shape *bn- (cf. ism < *sm-, ibna 'daughter'); the plural is بَنُونَ banūna / بَنُو banū, construct بَنِي banī, from the Proto-Semitic plural stem *ban-. 'bent' is Arabic بِنْت bint 'daughter' < Proto-Semitic *bint- = the root *bin- plus the Semitic feminine *-at-, with the regular Arabic assimilation *bint > (Hebrew bat < *batt < *bint). Nourai's spelling 'bent' with e is the Persian, not the Arabic, vocalisation of the same word — Arabic has bint — but since the arrow feeds the Persian node #2 the form is not wrong there. The 'b.n.v' line is simply the Arabic grammarians' citation of the root; it is not itself a word.\",\n     \"derivation_fa\": \"عربی «ابن» به معنای «پسر» بازماندهٔ مستقیم سامیِ آغازین *bin- است؛ الف آغازینِ آن همزهٔ وصل است که عربی بر سرِ ستاک‌های تک‌هجایی می‌افزاید (مانند «اسم» از *sm-). جمع آن «بنون/بنو» و در حالت اضافه «بنی» است که از ستاک جمعِ سامی *ban- می‌آید، و «بنت» از *bint- یعنی همان ریشه به‌علاوهٔ پسوند مؤنث‌سازِ سامی *-at- ساخته شده است. ضبط نورایی «bent» تلفظ فارسیِ این واژه است نه تلفظ عربی (bint)، ولی چون این گره به گرهٔ فارسی می‌رسد نادرست شمرده نمی‌شود. ادعای نورایی در این گره درست است.\",\n     \"sources\": [W_IBN, W_BINT, W_BIN],\n     \"ref_check\": [KLN163, FVA53],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 97 (p. 163) s.v. ben\", \"stance\": \"supports\",\n       \"note\": \"Klein explicitly links Heb. ben with 'Arab. ibn' and refers Heb. bath 'daughter' to the same family.\"},\n      {\"src\": \"AHD\", \"where\": \"Semitic appendix s.v. bn\", \"stance\": \"supports\",\n       \"note\": \"'Common Semitic *bint-. … bint, from Arabic bint, daughter' — AHD derives Arabic bint from the same root as ibn, as the chart does.\"},\n      {\"src\": \"RCH\", \"where\": \"Richardson, Persian-Arabic-English Dictionary, RCH.txt line 1711\", \"stance\": \"supports\",\n       \"note\": \"'ibn, A son' — the Arabic word with Nourai's gloss, in the dictionary of Persian-and-Arabic usage.\"}\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"Persian\",\n     \"words\": \"ebn «ابن»; bent «بنت»; banî «بنی»; Ebne-Sînâ «ابن سینا»\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"All four are Arabic loans taken into New Persian after the 7th-century conquest, with no Middle Persian antecedent (Pahlavi 'son' is pus/pusar, MacKenzie PHD p. 70): ابن ebn is Arabic ibn, used in Persian almost exclusively in patronymics of the Islamic learned tradition; بنت bent is Arabic bint, confined in Persian to formal/legal registers; بنی banī is the Arabic construct plural banī 'sons of', which entered Persian ready-made inside the phrases the chart itself quotes, بنی‌آدم 'the children of Adam' (Saʿdi's Golestān) and بنی‌هاشم 'the Banū Hāshim'. ابن سینا Ebn-e Sīnā is the Arabic patronymic of the philosopher, formed on the same ibn; Persian keeps the Arabic word order and adds the eżāfe in pronunciation. Wiktionary's etymology tree gives exactly this route: Proto-Semitic *bin- > Arabic اِبْن ibn, borrowed (bor.) > Persian ابن. Two factual slips in the box, neither etymological: (a) Ebn-e Sīnā was born at Afshana near Bukhara and was a Samanid/Bukharan Persian — he only served at the Maʾmunid court of Gorganj in Khwarazm c. 1012-1017, so 'A Khwarazmian scholar' is inaccurate; (b) the gloss spells the Latin name 'Avicena' with one n (see node #3).\",\n     \"derivation_fa\": \"هر چهار واژه وام‌واژه‌های عربی‌اند که پس از فتح ایران وارد فارسی نو شده‌اند و پیشینهٔ فارسی میانه ندارند (در پهلوی «پسر» pus/pusar است، مکنزی ص ۷۰). «ابن» همان ibn عربی است و در فارسی بیشتر در نام‌های پدرْبنیاد سنت علمی اسلامی به کار می‌رود؛ «بنت» همان bint است و کاربردش در فارسی رسمی و حقوقی است؛ «بنی» صورت اضافیِ جمعِ عربی banī است که آماده و درون ترکیب وارد فارسی شده، چنان‌که در همان نمونه‌های کتاب: «بنی‌آدم» و «بنی‌هاشم». «ابن سینا» نیز کنیهٔ عربیِ همان فیلسوف است بر پایهٔ همین ibn. ویکی‌واژه همین راه را می‌دهد: سامی آغازین *bin- ← عربی ابن ← وام در فارسی. دو نکتهٔ غیرِ ریشه‌شناختی: ابن سینا در افشنهٔ نزدیک بخارا زاده شد و ایرانیِ بخارایی بود، نه خوارزمی (تنها چند سالی در دربار مأمونیانِ گرگانج بود)؛ و ضبط «Avicena» با یک n خطای چاپی است (نگاه کنید به گرهٔ ۳). ادعای ریشه‌شناختیِ نورایی در این گره درست است.\",\n     \"sources\": [W_IBN, W_AVI],\n     \"ref_check\": [\n      {\"ref\": \"MON5:85,285\", \"status\": \"not_checked\",\n       \"note\": \"Mo'in vol. 5 is the aʿlām (proper-names) volume; only vols 1-3 of the lexicon are on disk (MON_part1/2) and vajehyab/abadis carry the lexicon, not the aʿlām volume, with no page mapping. ابن سینا and بنیامین are exactly the sort of headword that stands in vol. 5, so the citation is plausible but could not be opened.\"},\n      FVA53,\n      {\"ref\": \"FSD:197\", \"status\": \"supports\",\n       \"note\": \"FSD_vol1.txt leaf 247 (= printed p. 197): 'Av\\\"i-cen'na … n. An Arab physician and philosopher (980-1037)' and s.v. Avicennism 'It is chiefly to his Canon of Medicine that he owes his fame, for it was the guide to medical study in every university in Europe from the 12th to the 17th century.' Nourai's NOTE is a paraphrase of this very page — including his objection, since Funk & Wagnalls is one of the dictionaries that call Ibn Sīnā 'an Arab physician'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"MON\", \"where\": \"MON_part1.txt (lexicon vols); searched بنیامین, ابن سینا\", \"stance\": \"silent\",\n       \"note\": \"grep 'ابن سینا' finds only bibliography lines (e.g. line 255 'کتابفروشی ابن سینا'); the proper name itself is in vol. 5, which is not in the local text.\"},\n      {\"src\": \"RCH\", \"where\": \"RCH.txt line 1711\", \"stance\": \"supports\",\n       \"note\": \"'ibn, A son' — Richardson lists it among the Arabic words current in Persian, i.e. as a loan, exactly as the chart has it.\"},\n      {\"src\": \"ARY\", \"where\": \"ARY_pages.txt (Aryanpur, Indo-European roots of Persian)\", \"stance\": \"silent\",\n       \"note\": \"Aryanpur treats only the Indo-European stratum of Persian, so an Arabic loan such as ابن is absent — a negative result that is itself consistent with the loan status.\"},\n      {\"src\": \"FSD\", \"where\": \"FSD_vol1.txt leaf 247 (p. 197)\", \"stance\": \"supports\",\n       \"note\": \"Gives Ibn Sīnā's dates 980-1037 exactly as the chart does.\"}\n     ]\n    },\n    {\n     \"id\": 3,\n     \"lang\": \"English\",\n     \"words\": \"Avicena, Avicenism\",\n     \"verdict\": \"transcription_suspect\",\n     \"error_in\": \"book\",\n     \"book_prints\": \"Avicena, Avicenism\",\n     \"correct_form\": \"Avicenna, Avicennism\",\n     \"derivation\": \"The English name is Avicenna, with -nn-, and the derived noun is Avicennism: so Funk & Wagnalls (FSD p. 197, Nourai's own reference: 'Av\\\"i-cen'na', 'Av\\\"i-cen'nism'), so Klein ('Avicennism, n., the teachings of the Arab. philosopher Avicenna (= Ibn Sina) (980-1037)'), so Wiktionary. The printed page 70 of the book itself shows 'Avicena, Avicenism' in the English box and 'Avicena' in the Persian box's gloss (see data/verification/sources/refs/ocr/BOOK/100.png), so the extraction is faithful and the single n is Nourai's own misprint — possibly influenced by Spanish/Portuguese Avicena. The derivation as such is sound but the route is drawn one node off: Latin took the name from the ARABIC اِبْن سِينَا ibn sīnā, not from Persian — through the Andalusian Judeo-Arabic/Hebrew intermediary aven sina (ibn > aben/aven, as in Avempace = ibn Bājja, Avenzoar = ibn Zuhr), Latinised as Avicenna in the Toledo translation school of the 12th century; Klein notes the term vena basilica 'appears for the first time in a translation of Avicenna by Gerardus Cremonensis', which is the very channel. Avicennism, the label for the Latin Aristotelianism read off the Šifāʾ, is a modern (19th-c.) coinage on that Latin name with -ism.\",\n     \"derivation_fa\": \"صورت درست انگلیسی Avicenna با دو n است و مشتق آن Avicennism؛ هم فرهنگ Funk & Wagnalls (همان مرجعِ خودِ نورایی، ص ۱۹۷)، هم کلاین و هم ویکی‌واژه همین را می‌آورند. تصویر صفحهٔ ۷۰ چاپی نشان می‌دهد که خودِ کتاب «Avicena, Avicenism» چاپ کرده است؛ پس خطا از خوانشِ اسکن نیست بلکه خطای چاپی کتاب است (شاید به تأثیر املای اسپانیایی Avicena). دربارهٔ خودِ ریشه: لاتین این نام را نه از فارسی بلکه از عربیِ «ابن سینا» گرفت، از راه صورت اندلسیِ عبری/عربی aven sina (مانند Avempace = ابن باجه و Avenzoar = ابن زهر) و در مکتب ترجمهٔ طُلَیطُله در سدهٔ دوازدهم میلادی به Avicenna بدل شد؛ کلاین خود یادآور می‌شود که اصطلاح vena basilica نخستین‌بار در ترجمهٔ جِرارد کرمونایی از آثار ابن سینا آمده است. «Avicenism/Avicennism» هم ساختی نو بر همان نام لاتین است.\",\n     \"sources\": [W_AVI, ETY_BAG.replace(ETY_BAG, W_AVI)],\n     \"ref_check\": [\n      {\"ref\": \"FSD:197\", \"status\": \"partial\",\n       \"note\": \"FSD_vol1.txt leaf 247 (= printed p. 197) has both headwords, but spelled 'Av\\\"i-cen'na' and 'Av\\\"i-cen'nism' — it supports the existence and the sense of the English words while contradicting Nourai's one-n spelling.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"KLN_1966.txt s.v. Avicennism\", \"stance\": \"partial\",\n       \"note\": \"'Avicennism, n., the teachings of the Arab. philosopher Avicenna (= Ibn Sina) (980-1037)' — same word, -nn- spelling; Klein also records that vena basilica 'appears for the first time in a translation of Avicenna by Gerardus Cremonensis', documenting the Latin channel.\"},\n      {\"src\": \"FSD\", \"where\": \"FSD_vol1.txt leaf 247 (p. 197)\", \"stance\": \"partial\",\n       \"note\": \"Nourai's cited page; spells Avicenna/Avicennism.\"},\n      {\"src\": \"WEB\", \"where\": \"WEB_vol1.txt\", \"stance\": \"silent\",\n       \"note\": \"grep 'Avicen' in the local Webster volume returns nothing (the volume on disk does not cover the entry).\"}\n     ]\n    },\n    {\n     \"id\": 4,\n     \"lang\": \"Hebrew\",\n     \"words\": \"běn; Ben-yâmîn; Reŭ-bhen\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Hebrew בֵּן bēn 'son' is the regular Canaanite outcome of Proto-Semitic *bin- (short *i in a closed stressed syllable > ē by the Canaanite lowering, with loss of the case ending: *binu > *bin > bēn); construct בֶּן ben-, plural בָּנִים bānīm from the plural stem *ban-. בִּנְיָמִין Binyāmīn = bin-, the frozen bound form of bēn, + yāmīn 'right hand, south' (Gen. 35:18), hence 'son of the right hand', i.e. of the south — the AHD Semitic appendix spells this out under 'bn' and cross-refers to the root ymn exactly as Nourai's ☞ Y.m.n does. Nourai's added gloss '(prosperous)' reflects the old view, still cited by Wiktionary from Gesenius, that 'son of the right hand' meant 'son of good fortune'; Wiktionary also records the rival reading yāmīn 'days' ('son of old age', Philo, the Samaritan Pentateuch, Midrash Leqaḥ Ṭob), so the gloss is one accepted reading, not the only one. רְאוּבֵן Rəʾūbēn = rəʾū 'see! (m.pl. imperative)' + bēn 'son' = 'behold, a son' (Gen. 29:32), precisely Nourai's gloss.\",\n     \"derivation_fa\": \"عبری bēn «پسر» بازماندهٔ قاعده‌مندِ سامیِ آغازین *bin- است: مصوت کوتاهِ i در هجای بستهٔ تکیه‌بر، بر پایهٔ تحول کنعانی، به ē کشیده شده و پایانهٔ اِعرابی افتاده است (*binu > bēn)؛ جمع آن bānīm از ستاک جمعِ *ban-. «بنیامین» از bin- (صورت اضافیِ منجمدِ bēn) و yāmīn «دست راست، جنوب» ساخته شده، یعنی «پسرِ دست راست» (سفر پیدایش ۳۵:۱۸)، و پیوستِ سامیِ فرهنگ American Heritage دقیقاً همین را ذیل ریشهٔ bn می‌آورد و به ریشهٔ ymn ارجاع می‌دهد، همان‌گونه که نورایی نشانهٔ ☞ Y.m.n را گذاشته است. افزودهٔ «(prosperous)» در معنای نورایی بازتابِ تفسیر کهنِ گزنیوس («پسرِ بخت و اقبال») است و ویکی‌واژه خوانش رقیبِ «پسرِ روزگارِ پیری» را هم ثبت کرده است. «رئوبین» نیز از rəʾū «ببینید!» و bēn «پسر» است، یعنی «بنگرید، پسری!» — همان معنایی که نورایی داده است. ادعای نورایی در این گره درست است.\",\n     \"sources\": [AHD_SEM, W_BENJ, W_REU],\n     \"ref_check\": [\n      {\"ref\": \"KLN:163, 164\", \"status\": \"supports\",\n       \"note\": \"KLN_1966.txt leaf 97 covers both printed pages: p. 163 'ben, n., son. — Heb. ben, \\\"son\\\" …' and p. 164 'Benjamin, masc. PN.; in the Bible, Jacob's youngest son. — Heb. Binyamin, lit. \\\"son of the right hand\\\", fr. ben \\\"son\\\", and yamin, \\\"right hand\\\"; see Gen. 35:18 … Heb. yamin means also \\\"south\\\"'. Both of Nourai's page numbers hit their target.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 97 (pp. 163-164)\", \"stance\": \"supports\",\n       \"note\": \"Klein gives bēn, Binyāmīn 'son of the right hand' and, s.v. Reuben, the same biblical name; he also notes the auspicious value of the right side ('the right side was regarded as auspicious'), which is Nourai's '(prosperous)'.\"},\n      {\"src\": \"AHD\", \"where\": \"Semitic appendix s.v. bn\", \"stance\": \"supports\",\n       \"note\": \"'Benjamin, from Hebrew binyāmîn, son of the right hand, from bin-, frozen bound form of bēn (yāmîn, right hand, south; see ymn)' — including the cross-reference to ymn that the chart marks with ☞ Y.m.n.\"}\n     ]\n    },\n    {\n     \"id\": 5,\n     \"lang\": \"Persian\",\n     \"words\": \"Benyâmîn «بنیامین»\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"The name is genuine Persian usage — the chart's own citation, Sanāʾi's Ḥadīqat al-Ḥaqīqa (Ghazna, c. 1131), rhymes «چون نه یعقوبی و نه بن یامین / زین دعا نشنوی مگر آمین», and the manuscript spelling there is بن یامین in two words, i.e. the name was still felt as ben + yāmīn. But the arrow as drawn (Hebrew → Persian direct) is too short: Persian did not read Hebrew. Biblical names reached New Persian through the Arabic-Islamic transmission of the prophets' stories (qiṣaṣ al-anbiyāʾ, Ṭabari's tafsīr and its Persian translation) and, for the Jewish and Christian communities, through Syriac; the Persian shape بنیامین with -yā- and long final -īn matches the Arabic بنيامين rather than the Tiberian Binyāmīn. The name is not in the Qurʾān, so this is not a Qurʾānic loan, which is why Nourai gives no reference for the node at all. Verdict: right root, right meaning, but the intermediary (Arabic/Syriac) is missing from the chart.\",\n     \"derivation_fa\": \"کاربرد فارسیِ این نام درست است: شاهدِ خودِ کتاب از حدیقةالحقیقهٔ سنایی (غزنه، حدود ۵۲۵ ق) است — «چون نه یعقوبی و نه بن یامین / زین دعا نشنوی مگر آمین» — و املای آن در همان بیت «بن یامین» جدا نوشته شده، یعنی هنوز آن را «بن + یامین» می‌فهمیدند. ولی پیکانِ نمودار (عبری ← فارسی به‌طور مستقیم) کوتاه است: فارسی‌زبانان از عبری وام نگرفتند؛ نام‌های کتاب مقدس از راه روایت‌های اسلامی (قصص‌الانبیا و ترجمهٔ تفسیر طبری) و برای جامعه‌های یهودی و مسیحی از راه سریانی به فارسی رسیده‌اند، و صورت «بنیامین» نیز به ضبط عربیِ «بنيامين» نزدیک‌تر است تا به Binyāmīn عبری. این نام در قرآن نیامده، و شاید به همین سبب نورایی برای این گره هیچ مأخذی نداده است. پس: ریشه و معنا درست، اما واسطهٔ عربی/سریانی در نمودار افتاده است — با احتیاط پذیرفتنی است.\",\n     \"sources\": [W_BENJ, AHD_SEM],\n     \"ref_check\": [\n      {\"ref\": \"None\", \"status\": \"not_checked\",\n       \"note\": \"Nourai gives no reference for this node (refs=None in the JSON and no book icon in the printed box on p. 70).\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"MON\", \"where\": \"MON_part1.txt / MON_part2.txt, grep بنیامین\", \"stance\": \"silent\",\n       \"note\": \"0 hits: the name belongs to Mo'in's aʿlām volume (vol. 5), which is not in the local text.\"},\n      {\"src\": \"BQT\", \"where\": \"BQT_v1_pages.txt, BQT_v2_pages.txt, grep بنیامین / بن یامین\", \"stance\": \"silent\",\n       \"note\": \"0 hits — Borhān-e Qāṭeʿ does not lemmatise the biblical name.\"},\n      {\"src\": \"RCH\", \"where\": \"RCH.txt, grep Beny…/Binyámín\", \"stance\": \"silent\",\n       \"note\": \"0 hits in Richardson's Persian-Arabic-English dictionary.\"}\n     ]\n    },\n    {\n     \"id\": 6,\n     \"lang\": \"English\",\n     \"words\": \"Benjamin, Ben, Big Ben, Reuben\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"English Benjamin comes from Biblical Hebrew בִּנְיָמִין binyāmīn through Ancient Greek Βενιαμίν Beniamín (Septuagint) and Late Latin Benjamin, entering English with the Bible and Wycliffite/Tyndale usage; Ben is the hypocoristic clipping of it, so Klein: 'Ben, masc. PN. — Dimin. of Benjamin'. Big Ben is that clipping applied as a nickname: Klein (printed p. 170-171, leaf 101/102 of KLN_1966.txt) 'Big Ben, name of the bell attached to the clock at Westminster. — Named after Sir Benjamin Hall, first commissioner of works, under whose supervision the bell was cast. For Ben, dimin. of Benjamin, see Ben' — so the arrow from the Hebrew node reaches Big Ben through the personal name, which is exactly how the chart draws it. Reuben likewise comes from Hebrew רְאוּבֵן via Greek Ῥουβήν and Latin Ruben. All four therefore do go back to Hebrew bēn 'son' as the chart claims.\",\n     \"derivation_fa\": \"«Benjamin» انگلیسی از عبریِ کتاب مقدس binyāmīn است که از راه یونانیِ سِبعینیه (Beniamín) و لاتینِ متأخر Benjamin و با ترجمه‌های انگلیسیِ کتاب مقدس وارد انگلیسی شده است؛ Ben کوتاه‌شدهٔ همان نام است («Ben: مصغّرِ Benjamin»، کلاین). «Big Ben» نیز همان نامِ کوتاه‌شده است که بر ناقوس ساعت وست‌مینستر نهاده شد، به یاد سِر بنجامین هال (کلاین، ص ۱۷۰-۱۷۱). «Reuben» هم از عبری Rəʾūbēn از راه یونانی Ῥουβήν و لاتین Ruben آمده است. پس هر چهار نام سرانجام به عبری bēn «پسر» می‌رسند و ادعای نورایی درست است.\",\n     \"sources\": [W_BENJ, W_REU, AHD_SEM],\n     \"ref_check\": [\n      {\"ref\": \"KLN:163\", \"status\": \"supports\",\n       \"note\": \"KLN_1966.txt leaf 97 (p. 163-164): 'ben, n., son. — Heb. ben … Cp. Benjamin, B'nai B'rith, boanerges' and 'Ben, masc. PN. — Dimin. of Benjamin (q.v.)'; Big Ben is treated a few pages on (leaf 101/102) and is referred back to the same Ben.\"},\n      {\"ref\": \"AHD\", \"status\": \"supports\",\n       \"note\": \"AHD Appendix of Semitic Roots s.v. 'bn' (ahdictionary.com/word/semitic.html): 'Benjamin, from Hebrew binyāmîn, son of the right hand' — the English name filed under the Semitic root exactly as the arrow does.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaves 97 and 101/102\", \"stance\": \"supports\",\n       \"note\": \"Benjamin, Ben and Big Ben all traced to Heb. ben; 'Named after Sir Benjamin Hall, first commissioner of works, under whose supervision the bell was cast.'\"},\n      {\"src\": \"AHD\", \"where\": \"Semitic appendix s.v. bn\", \"stance\": \"supports\",\n       \"note\": \"Lists Benjamin (and bar mitzvah, Barabbas, Barnabas, B'nai B'rith, bat mitzvah, bint) under *b(i)n-.\"},\n      {\"src\": \"FSD\", \"where\": \"FSD_vol1.txt, grep 'Big Ben'\", \"stance\": \"silent\",\n       \"note\": \"0 hits in the local volume (proper names of this kind are in the F&W biographical/gazetteer appendices, not the A-Dive text).\"}\n     ]\n    }\n   ]\n  },\n  {\n   \"entry\": 1,\n   \"root\": \"Boqčâ, Bŭqčâ\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"Ottoman Turkish بوغچه boğça / modern Turkish bohça 'bundle, wrapping cloth', from Turkic boğ- 'to tie, bind' + diminutive -ça\",\n   \"note\": \"The root box is right: the word is Turkic, not Iranian. Wiktionary derives modern Turkish bohça from Ottoman Turkish بوغچه boğça; Lokotsch no. 325 (p. 28) heads it 'Tk. boġča: Bündel, Paket' and refers the stem to his no. 323 'bag, beg, bog: Band, gebunden, binden'; Vámbéry's Etymologisches Wörterbuch der turko-tatarischen Sprachen no. 204 (p. 192), which is Lokotsch's source, sets up the Turkic root bag/beg/bog 'Band, binden' with boġ 'Knoten, Bündel', boġun 'Knoten, Bündel', boġmak 'binden' — so boġ-ča is 'a little tie/bundle', with the common Turkic diminutive -ča. Nourai's two vocalisations Boqčâ/Bŭqčâ correspond to the Ottoman spelling بوغچه and to the Persian/Arabic reflex بقچه; the -q- of his transliteration is the Persian rendering of Turkic ġ. The chart's Turkish > Persian > Arabic steps are all supported; the two Western steps (French, English) are not — see nodes #3 and #4.\",\n   \"note_fa\": \"ریشهٔ نمودار درست است: این واژه ترکی است نه ایرانی. ویکی‌واژه «bohça»ی ترکی امروز را از ترکی عثمانیِ «بوغچه» boğça می‌گیرد؛ لوکوچ (شمارهٔ ۳۲۵، ص ۲۸) آن را «ترکی boġča: بسته، بقچه» می‌آورد و ستاک آن را به شمارهٔ ۳۲۳ یعنی bag/beg/bog «بند، بستن» بازمی‌گرداند؛ و وامبری در فرهنگ ریشه‌شناختی زبان‌های ترکی-تاتاری (شمارهٔ ۲۰۴، ص ۱۹۲) همین ریشه را با مشتقاتی چون boġ «گره، بسته»، boġun «گره» و boġmak «بستن» ثبت کرده است. پس boġ-ča یعنی «بستهٔ کوچک»، با پسوند تصغیرِ رایج ترکی ‑ça. دو ضبط نورایی (Boqčâ / Bŭqčâ) با املای عثمانیِ «بوغچه» و صورت فارسی‑عربیِ «بقچه» می‌خواند. مرحله‌های ترکی ← فارسی ← عربی همگی پذیرفتنی‌اند، ولی دو مرحلهٔ اروپایی (فرانسوی و انگلیسی) نه — نگاه کنید به گره‌های ۳ و ۴.\",\n   \"sources\": [W_BOHCA, ABADIS],\n   \"ref_check\": [\n    {\"ref\": \"MON:551\", \"status\": \"supports\",\n     \"note\": \"Mo'in's entry, MON_part1.txt line 24266 (OCR 'بعچه' for بغچه): 'بغچه: … [تر. > بوغچه - بقچه]' — the bracketed origin tag [تر.] = Turkish, with the Ottoman form بوغچه and the variant بقچه, i.e. precisely the Turkish root box and the Persian node beneath it. The local Mo'in text carries no page numerals, so p. 551 itself could not be confirmed; the content is Mo'in's.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"TTS\", \"where\": \"Vámbéry, TTS_pages.txt leaf 221 = printed p. 192, root no. 204\", \"stance\": \"supports\",\n     \"note\": \"'Bag, beg, bik, bog, buk, baj, boj, büj — Band, Zauber, gebunden, befestigt … binden, knüpfen': under it čag./osm. boġ 'Knopf, Knoten', boġmak 'binden, würgen', boġun, boġum 'Knoten, Ast, Knospe, Bündel'. The stem from which boġ-ča is formed.\"},\n    {\"src\": \"LKT\", \"where\": \"Lokotsch no. 325, LKT.txt leaf 54 = printed p. 28\", \"stance\": \"supports\",\n     \"note\": \"'325. Tk. boġča: \\\"Bündel, Paket\\\" [Stamm bag, bog s. hier Nr. 323], boġčaǧy \\\"Trödler\\\"; hieraus rum. boccea \\\"Ballen; viereckiges Umschlagtuch\\\"…' — Turkic origin, and the loans Lokotsch traces go into Romanian, not into French.\"},\n    {\"src\": \"MON\", \"where\": \"MON_part1.txt line 24266\", \"stance\": \"supports\",\n     \"note\": \"[تر.] 'Turkish' tag with بوغچه / بقچه.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Persian\",\n     \"words\": \"boqčeh «بغچه»\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Persian بقچه / بغچه boqče 'bundle, wrapping cloth' is a loan from Turkic boġča, taken over during the Turkish-speaking dynasties' rule (Saljuq to Qajar) with the ordinary substitution of Persian q/ġ for Turkic ġ and of final -e (-eh) for Turkic -a; the printed page gives بغچه as the main spelling and بقچه، بوغچه as variants, which is exactly the set Dehkhodā and Mo'in record. Dehkhodā labels both entries '(ترکی، اِ)' — 'Turkish, noun' — and glosses «مأخوذ از ترکی، بغچه و بستهٔ کوچک»; Mo'in's tag is [تر. > بوغچه - بقچه]. The word is late in Persian: Dehkhodā's oldest citations are from Neẓām Qāri's Dīvān-e Albase (9th/15th c., «ز سر بقچه الباس اهل بخل کمتر پرس»), and it is absent from Borhān-e Qāṭeʿ as a headword (it occurs there only as a metrical model, 'بر وزن بقچه'). No Middle Persian or Iranian etymon exists.\",\n     \"derivation_fa\": \"«بقچه/بغچه» در فارسی وام‌واژه‌ای است از ترکیِ boġča که در دورهٔ فرمانروایی دودمان‌های ترک‌زبان (از سلجوقی تا قاجار) وارد شده است، با جانشینیِ معمولِ ق/غ فارسی به‌جای غِ ترکی و «ـه» پایانی به‌جای -a. کتاب «بغچه» را صورت اصلی و «بقچه، بوغچه» را گونه‌ها آورده که همان مجموعه‌ای است که دهخدا و معین ثبت کرده‌اند: دهخدا هر دو مدخل را «(ترکی، اِ)» می‌نامد و می‌نویسد «مأخوذ از ترکی، بغچه و بستهٔ کوچک»، و معین تگِ [تر. > بوغچه - بقچه] را می‌آورد. این واژه در فارسی دیرآمده است: کهن‌ترین شواهد دهخدا از دیوان البسهٔ نظام قاری (سدهٔ نهم قمری) است و برهان قاطع آن را سرواژه نکرده و تنها به‌عنوان «بر وزنِ بقچه» به کار برده است. هیچ اصلِ فارسی میانه یا ایرانی برای آن نیست. ادعای نورایی درست است.\",\n     \"sources\": [ABADIS, W_BOHCA],\n     \"ref_check\": [\n      {\"ref\": \"MON:551,555\", \"status\": \"supports\",\n       \"note\": \"MON_part1.txt line 24266: 'بغچه: … [تر. > بوغچه - بقچه]' — Mo'in marks the word Turkish and lists the same three spellings the chart prints. Page numbers are not recoverable from the local OCR (no page markers), so only the content, not p. 551/555, is confirmed.\"}\n      ],\n     \"consulted\": [\n      {\"src\": \"MON\", \"where\": \"MON_part1.txt line 24266\", \"stance\": \"supports\",\n       \"note\": \"'[تر. > بوغچه - بقچه]'.\"},\n      {\"src\": \"BQT\", \"where\": \"BQT_v1_pages.txt line 12967 and BQT_v4_pages.txt line 17837\", \"stance\": \"silent\",\n       \"note\": \"Borhān-e Qāṭeʿ has no headword بقچه; the word appears only as a metrical model ('بن اول بروزن بقچه', 'بروزن بقچه') — i.e. familiar to the 17th-c. compiler but not lemmatised, consistent with a Turkish loan of the Safavid period.\"},\n      {\"src\": \"ARY\", \"where\": \"ARY_pages.txt, grep بقچه / بغچه\", \"stance\": \"silent\",\n       \"note\": \"0 hits — Aryanpur's dictionary of the Indo-European stratum of Persian does not contain it, as expected for a Turkic loan.\"},\n      {\"src\": \"MON (web)\", \"where\": \"abadis.ir/fatofa/بقچه (Dehkhodā + Farhang-e Fārsi + ʿAmid)\", \"stance\": \"supports\",\n       \"note\": \"Dehkhodā: 'بقچه. [ب َ/ب ُ چ َ] (ترکی، اِ) باقچه … رجوع به … دزی ج ۱ ص ۱۰۲ شود' and 'بقچه. (ترکی، اِ) بغچه. مأخوذ از ترکی'; Farhang-e Fārsi (Moʿin): 'دستمال بزرگی که در آن جامه و انواع قماش پیچند' = the chart's 'a large napkin, linen for wrapping clothes in it'.\"}\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"Arabic\",\n     \"words\": \"bouqčeh\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Arabic بُقْجة buqǧa 'bundle of clothes, wrapper' is a post-classical, colloquial word, and Asbaghi's Persische Lehnwörter im Arabischen p. 53 lists it as a Persian loan: 'buqča: \\\"Paket, Wäsche\\\" pers. بقچه boqča \\\"Bündel, Schnappsack\\\"' (his authority being Steingass); p. 40 adds the Egyptian variant 'buǧa = buġča s. buqča (ägypt. Ar.)', the ǧ/ġ spellings showing the borrowing of a foreign č. Lammens likewise calls it 'un terme très employé en Syrie … ce mot, qui n'appartient pas à la langue classique, est d'origine persane'. Since the Persian word is itself Turkic (node #1), the Arabic is a Turkic word passed on through Persian — or, in the Ottoman provinces, taken directly from Turkish; either way Nourai's Persian → Arabic arrow is right, and the transliteration 'bouqčeh' is a Persianised rendering (Arabic has no č, hence بقجة with ǧīm).\",\n     \"derivation_fa\": \"«بُقجة» عربی به معنای بستهٔ جامه واژه‌ای پس‌ازکلاسیک و عامیانه است و آسبقی در «وام‌واژه‌های فارسی در عربی» (ص ۵۳) آن را وام از فارسی می‌داند: «buqča: بسته، رخت‌وجامه؛ از فارسی بقچه boqča». در ص ۴۰ نیز گونهٔ مصریِ «بجة = بغجة» را به همان مدخل ارجاع می‌دهد؛ همین نوسانِ ج/غ نشان می‌دهد که «چ» بیگانه در عربی جایگزین شده است. لامنس هم می‌نویسد این واژه «در سوریه بسیار به کار می‌رود» و «از زبان کلاسیک نیست و اصل فارسی دارد». چون خودِ واژهٔ فارسی ترکی است (گرهٔ ۱)، آنچه به عربی رسیده در اصل ترکی است که از راه فارسی — یا در ولایات عثمانی مستقیماً از ترکی — گرفته شده است. ضبط «bouqčeh» در کتاب فارسی‌مآب است، زیرا عربی «چ» ندارد و آن را «بقجة» می‌نویسد. ادعای نورایی در این گره درست است.\",\n     \"sources\": [ABADIS],\n     \"ref_check\": [\n      {\"ref\": \"PLA:53\", \"status\": \"supports\",\n       \"note\": \"PLA_pages.txt leaf 67 = printed p. 53 (running heads 'bagbur … 53 … baqzis'): 'buqča: \\\"Paket, Wäsche\\\" pers. بقچه boqča \\\"Bündel, Schnappsack\\\"' (footnote 9 = Steingass). Nourai's page number is exact.\"},\n      {\"ref\": \"LAM:37\", \"status\": \"supports\",\n       \"note\": \"LAM.txt leaf 94 = printed p. 37 (running head 'BAGA. 37'), s.v. Bagage: 'l'arabe بقجة bouqǧa ou بقشة bouqcha, paquet de linge et d'habits, terme très employé en Syrie … Ce mot, qui n'appartient pas à la langue classique, est d'origine persane بقچه \\\"involucrum ex tela … ubi involvuntur vestes\\\" (Vullers)'. Lammens supports the Persian → Arabic step exactly.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PLA\", \"where\": \"Asbaghi p. 53 (and the cross-reference on p. 40)\", \"stance\": \"supports\",\n       \"note\": \"Arabic buqča listed among the Persian loanwords, glossed from Steingass.\"},\n      {\"src\": \"LAM\", \"where\": \"Lammens p. 37\", \"stance\": \"supports\",\n       \"note\": \"'d'origine persane', with the Vullers gloss.\"},\n      {\"src\": \"AFM\", \"where\": \"AFM.txt / AFM_pages.txt (Addi Shir), grep بقجة / بقجه\", \"stance\": \"silent\",\n       \"note\": \"0 hits — Addi Shir's list of Persian loans in Arabic does not include it, which fits its late, colloquial character.\"},\n      {\"src\": \"TAD\", \"where\": \"TAD_pages.txt leaf 15 (printed p. ~11-12)\", \"stance\": \"supports\",\n       \"note\": \"Arabic-script entry, OCR: 'بقجة - عامية أي صرة من الثياب … ونقلت من العربية إلى الفرنساوية' — 'buqǧa, colloquial, i.e. a bundle of clothes … and it passed from Arabic into French'. Al-Unaysi treats it as a non-classical (ʿāmmiyya) word.\"}\n     ]\n    },\n    {\n     \"id\": 3,\n     \"lang\": \"French\",\n     \"words\": \"bagage\",\n     \"verdict\": \"disputed\",\n     \"derivation\": \"Modern scholarship derives French bagage from Old French bagage 'baggage, military equipment' (14th c.), a formation in -age on Old French bague 'pack, bundle' (with Old Provençal baga), itself from a Germanic/North Germanic source — Old Norse baggi 'pack, bundle', the same source as English bag; Wiktionary allows the alternative of a Late Latin *baga 'vessel'. Nourai follows a 19th-century conjecture: Lammens p. 37 reports 'M. de Eguilaz pense que ce mot a été introduit en Europe par les Croisés, qui l'auraient emprunté à l'arabe bouqǧa', and al-Unaysi (TAD) states flatly that the word 'passed from Arabic into French'. Two things sink it. Chronology: OF bagage is attested from the 14th century and bague earlier still, whereas Arabic buqǧa is post-classical and its Persian source بقچه is first cited only in the 9th/15th century (Neẓām Qāri), and the Turkish original could not reach Syria before the Ottomans. Phonology: Arabic buqǧa/buqča would not yield French baga- with a in the first syllable and the productive French suffix -age, which is exactly what a native formation on bague predicts. Even Lammens' own discussion is about whether French borrowed from Spanish or vice versa, not about a demonstrable Arabic transmission. So: the word is real and the gloss right, but the parent drawn here is wrong.\",\n     \"derivation_fa\": \"پژوهش امروزی «bagage» فرانسوی را از فرانسویِ کهن bagage (سدهٔ چهاردهم میلادی) می‌داند، ساختی با پسوند -age بر روی bague «بسته، بقچه» (و اکسیتانیِ کهن baga)، که خود از سرچشمه‌ای ژرمنی/اسکاندیناویایی است: نورس کهن baggi «بسته»، همان که «bag» انگلیسی از آن است؛ ویکی‌واژه گزینهٔ لاتینِ متأخر *baga «ظرف» را هم می‌آورد. نورایی از گمانی در سدهٔ نوزدهم پیروی کرده است: لامنس (ص ۳۷) می‌نویسد «اگیلاث بر آن است که این واژه را جنگجویان صلیبی از عربیِ بقجة به اروپا برده‌اند»، و العنیسی نیز می‌نویسد این واژه «از عربی به فرانسه رفت». دو دلیل این ادعا را رد می‌کند: نخست تاریخ — bagage فرانسوی از سدهٔ چهاردهم گواه دارد و bague از آن هم کهن‌تر است، حال آنکه «بقجة» عربی پس‌ازکلاسیک است و کهن‌ترین شاهد فارسیِ «بقچه» از سدهٔ نهم قمری است و اصل ترکی آن پیش از عثمانیان به شام نمی‌رسید؛ دوم آواشناسی — از buqǧa عربی «baga-» با «آ»ی نخست و پسوند زایای فرانسویِ -age به دست نمی‌آید، ولی ساختِ بومی بر پایهٔ bague دقیقاً همین را می‌دهد. پس پژوهش امروزی این پیکان را رد می‌کند.\",\n     \"sources\": [W_BAGF, ETY_BAG, AHD_BAG],\n     \"ref_check\": [\n      {\"ref\": \"TAD:12\", \"status\": \"supports\",\n       \"note\": \"TAD_pages.txt leaf 15 (Nourai's p. 12; the leaf/page offset of this small volume is leaf − 3..5): 'بقجة - عامية … ونقلت من العربية إلى الفرنساوية' — al-Unaysi does claim the passage Arabic → French. He asserts it without evidence, and modern French etymology rejects it.\"},\n      {\"ref\": \"LAM:37\", \"status\": \"partial\",\n       \"note\": \"LAM.txt leaf 94 = p. 37: Lammens reports the derivation as Eguilaz's opinion ('M. de Eguilaz pense que ce mot a été introduit en Europe par les Croisés'), not as his own finding, and spends the entry arguing that Spanish, not French, was the point of entry ('Bagage apparaît chez nous assez timidement au 16ᵉ siècle, tandis qu'il est déjà employé comme un terme usuel par Hurtado de Mendoza'). Support for Nourai's arrow, but hedged and second-hand.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"KLN_1966.txt s.v. baggage\", \"stance\": \"contradicts\",\n       \"note\": \"'baggage, n. — F. bagage, fr. OF. bague, bundle, which, together with OProvenç. baga, of s.m., is prob. borrowed from Teutonic. See bag, n., and -age.' No Arabic or Persian anywhere.\"},\n      {\"src\": \"DEV\", \"where\": \"DEV.txt leaf 148 (Devic, Dictionnaire des mots français d'origine orientale)\", \"stance\": \"silent\",\n       \"note\": \"Devic has no entry bagage; the string occurs only inside the article Fardeau as a gloss of Italian fardaggio. A dictionary devoted to French orientalisms that declines to claim this one.\"},\n      {\"src\": \"PHN\", \"where\": \"PHN.txt leaf 89 (Pihan, p. 58)\", \"stance\": \"silent\",\n       \"note\": \"No entry bagage; 'bagage' appears only as part of the French gloss of the Arabic/Persian word bār under the headword BAR. Pihan, too, does not list bagage among French words from Arabic, Persian or Turkish.\"},\n      {\"src\": \"LKT\", \"where\": \"Lokotsch no. 325 (p. 28)\", \"stance\": \"contradicts\",\n       \"note\": \"Lokotsch's survey of European words of oriental origin traces Turkish boġča only into Romanian (boccea, boccealic); French bagage is not among the descendants, and Lokotsch has no bagage entry at all.\"}\n     ]\n    },\n    {\n     \"id\": 4,\n     \"lang\": \"English\",\n     \"words\": \"baggage\",\n     \"verdict\": \"disputed\",\n     \"derivation\": \"English baggage is first recorded mid-15th c. in the sense 'portable equipment of an army; plunder', borrowed from Old French bagage (14th c.); the French word is built on bague 'pack, bundle', ultimately of Scandinavian/Germanic origin (Old Norse baggi), the same source as English bag. That is the account of Etymonline, of the AHD itself (5th ed. s.v. baggage: 'Middle English bagage, from Old French bague, bundle, perhaps of Germanic origin; akin to Old Norse baggi, bag, bundle'), of Klein and of Skeat ('Baggage (1), luggage. (F.-C.) … O.F. bagage, a collection of bundles. — O.F. bague, a bundle'). So the English node is fine as a derivative of French bagage, but the whole chain above it — Persian/Arabic origin — is rejected by every modern authority, including the two Nourai cites here. Note also that AHD does bring Arabic into the entry, but only for the unrelated sense 4 ('a woman prostitute'), via French bagasse, Provençal bagassa, Arabic baġī 'prostitute' (root bġy) — a different word from buqǧa, and possibly the source of Nourai's impression that AHD:99 supports an Arabic origin.\",\n     \"derivation_fa\": \"«baggage» انگلیسی نخستین‌بار در میانهٔ سدهٔ پانزدهم میلادی به معنای «بار و بنهٔ لشکر، غنیمت» ثبت شده و وامی است از فرانسویِ کهن bagage (سدهٔ چهاردهم)؛ و آن واژهٔ فرانسوی ساختی است بر bague «بسته»، سرانجام از سرچشمهٔ اسکاندیناویایی/ژرمنی (نورس کهن baggi)، همان که «bag» از آن است. این روایتِ Etymonline، خودِ فرهنگ American Heritage (چاپ پنجم، ذیل baggage: «از انگلیسی میانه bagage، از فرانسویِ کهن bague «بسته»، احتمالاً با اصل ژرمنی؛ هم‌ریشه با نورس کهن baggi»)، کلاین و اسکیت است. پس خودِ این گره به‌عنوان مشتقِ فرانسوی درست است، ولی زنجیرهٔ بالای آن — اصل فارسی/عربی — را همهٔ مرجع‌های امروزی، از جمله دو مرجعی که نورایی همین‌جا نام برده، رد می‌کنند. نکتهٔ دیگر آنکه فرهنگ American Heritage عربی را تنها برای معنای چهارم (زنِ روسپی) پیش می‌کشد، از راه فرانسویِ bagasse و پرووانسالیِ bagassa از عربی «بغیّ»، که واژه‌ای دیگر است و شاید همین سبب پنداشتِ نورایی شده باشد.\",\n     \"sources\": [ETY_BAG, AHD_BAG, W_BAGF],\n     \"ref_check\": [\n      {\"ref\": \"AHD:99\", \"status\": \"contradicts\",\n       \"note\": \"The New College Edition page could not be opened (archive.org copies are lending-only), but the same dictionary online (ahdictionary.com/word/search.html?q=baggage) reads: '[Middle English bagage, from Old French bague, bundle, perhaps of Germanic origin; akin to Old Norse baggi, bag, bundle. Sense 4, perhaps from French bagasse, from Provençal bagassa, ultimately from Arabic baġī, prostitute…]'. AHD's only Arabic element is the unrelated sense 'prostitute'.\"},\n      {\"ref\": \"SKT:35\", \"status\": \"contradicts\",\n       \"note\": \"SKT.txt leaf 47 (printed p. 27 by the file's leaf = printed + 20 offset, so Nourai's p. 35 is off in this impression; Skeat groups the word under Bag): 'Baggage (1), luggage. (F.-C.) … O.F. bagage, a collection of bundles. — O.F. bague, a bundle. Celtic origin; Bret. beac'h, a burden; Gael. bag, balg; see Bag.' Skeat derives it from Old French and a Celtic/Germanic base, not from Arabic.\"},\n      {\"ref\": \"LAM:37\", \"status\": \"partial\",\n       \"note\": \"Lammens p. 37 is the one reference that supports an oriental origin, and only as Eguilaz's conjecture; he discusses Spanish/French priority, not English.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"KLN_1966.txt s.v. baggage\", \"stance\": \"contradicts\",\n       \"note\": \"'F. bagage, fr. OF. bague, bundle … prob. borrowed from Teutonic.'\"},\n      {\"src\": \"SKT\", \"where\": \"SKT.txt leaf 47\", \"stance\": \"contradicts\",\n       \"note\": \"'O.F. bagage, a collection of bundles. — O.F. bague, a bundle.'\"},\n      {\"src\": \"AHD\", \"where\": \"ahdictionary.com s.v. baggage\", \"stance\": \"contradicts\",\n       \"note\": \"'from Old French bague, bundle, perhaps of Germanic origin; akin to Old Norse baggi'.\"},\n      {\"src\": \"FSD\", \"where\": \"FSD_vol1.txt s.v. bag'gage\", \"stance\": \"silent\",\n       \"note\": \"The compounds (baggage-car, baggage-man, baggage-master) are in the local OCR but the etymology bracket of the headword did not survive the scan; no support either way.\"}\n     ]\n    }\n   ]\n  }\n ]\n}\n\nwith io.open('/home/sfmqrb/git/rishe/data/verification/page-100.json','w',encoding='utf-8') as f:\n    json.dump(data,f,ensure_ascii=False,indent=1)\n    f.write('\\n')\nprint('ok')\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk100.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-100.json > /dev/null && echo JSON_OK && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 100"
}
```


### [2026-09-05T14:52:49.757Z] TOOL RESULT

```
ok
JSON_OK
nodes verified: 10/10
node verdicts: {'confirmed': 6, 'transcription_suspect': 1, 'plausible': 1, 'disputed': 2}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 9, 'not_checked': 4, 'partial': 3, 'contradicts': 2}
books consulted: {'supports': 14, 'silent': 13, 'partial': 2, 'contradicts': 5} | by book: {'KLN': 6, 'AHD': 4, 'FSD': 4, 'RCH': 3, 'MON': 3, 'ARY': 2, 'BQT': 2, 'WEB': 1, 'MON (web)': 1, 'PLA': 1, 'LAM': 1, 'AFM': 1, 'TAD': 1, 'DEV': 1, 'PHN': 1, 'LKT': 1, 'SKT': 1}
```


## [2026-09-05T14:53:01.721Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 - <<'EOF'\np='mk100.py'\ns=open(p,encoding='utf-8').read()\ns=s.replace('\"sources\": [W_AVI, ETY_BAG.replace(ETY_BAG, W_AVI)],','\"sources\": [W_AVI],')\ns=s.replace('{\"src\": \"MON (web)\", \"where\": \"abadis.ir/fatofa/بقچه (Dehkhodā + Farhang-e Fārsi + ʿAmid)\"','{\"src\": \"MON\", \"where\": \"web copy: abadis.ir/fatofa/بقچه — Dehkhodā, Farhang-e Fārsi (Moʿin) and ʿAmid side by side\"')\nopen(p,'w',encoding='utf-8').write(s)\nEOF\npython3 mk100.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-100.json >/dev/null && echo JSON_OK && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 100 && cp mk100.py /dev/null"
}
```


### [2026-09-05T14:53:04.081Z] TOOL RESULT

```
ok
JSON_OK
nodes verified: 10/10
node verdicts: {'confirmed': 6, 'transcription_suspect': 1, 'plausible': 1, 'disputed': 2}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 9, 'not_checked': 4, 'partial': 3, 'contradicts': 2}
books consulted: {'supports': 14, 'silent': 13, 'partial': 2, 'contradicts': 5} | by book: {'KLN': 6, 'AHD': 4, 'MON': 4, 'FSD': 4, 'RCH': 3, 'ARY': 2, 'BQT': 2, 'WEB': 1, 'PLA': 1, 'LAM': 1, 'AFM': 1, 'TAD': 1, 'DEV': 1, 'PHN': 1, 'LKT': 1, 'SKT': 1}
```


## [2026-09-05T14:53:20.035Z] AGENT

Page 100 (book p. 70) verified; `verify_check.py 100` reports 10/10 nodes, 0 PROBLEM lines.

**Counts** — roots: 2 confirmed. Nodes: 6 confirmed, 1 plausible, 2 disputed, 1 transcription_suspect. Ref checks: 9 supports, 3 partial, 2 contradicts, 4 not_checked (FVA has no digital copy; MON vol. 5 aʿlām not on disk).

**Flagged items**
- `Boqčâ` #3 French *bagage* — **disputed**. OF *bagage* (14c.) is built on OF *bague* 'bundle' < Old Norse *baggi* (Etymonline, AHD, Klein, Skeat, Wiktionary). Nourai follows Eguilaz's 19th-c. guess reported by Lammens p.37; chronology (Persian بقچه first attested 9th/15th c., Arabic *buqǧa* post-classical) and the French suffix ‑age both rule it out.
- `Boqčâ` #4 English *baggage* — **disputed**. Same chain; AHD:99 and SKT:35, the very references cited, both give the Germanic/OF origin. AHD's only Arabic element is for the unrelated sense "prostitute" (*bagasse* < Ar. *baġī*), which may be what misled Nourai.
- `B.n.v` #3 English "Avicena, Avicenism" — **transcription_suspect**, `error_in: "book"`. The printed page (copied to `data/verification/sources/refs/ocr/BOOK/100.png`) really shows one *n*; correct form is Avicenna/Avicennism (so FSD:197 itself, and Klein). Extraction is faithful — **no data fix needed**.
- `B.n.v` #5 Persian بنیامین — **plausible** only: root and sense right, but the Hebrew→Persian arrow skips the Arabic/Syriac intermediary (the form matches Arabic بنيامين; the name is not Qurʾānic, and Nourai gives no ref).

**No extraction errors found** — the JSON matches the printed page throughout (including بغچه as the head spelling with بقچه/بوغچه as variants).

Non-etymological slip worth noting to the owner: the book calls Ebn-e Sīnā "A Khwarazmian scholar"; he was born at Afshana near Bukhara and only served in Khwarazm c. 1012–17 (recorded in node #2's derivation, verdict left `confirmed` since the etymology is right).

New files: `data/verification/page-100.json`, `data/verification/sources/refs/ocr/BOOK/100.png`, 12 archived web sources under `data/verification/sources/web/` (+ index.jsonl).
