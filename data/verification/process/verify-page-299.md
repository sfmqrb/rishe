# Verification process log — verify-page-299


## [2026-09-06T22:35:24.492Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 299 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-299.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-299.json. Write /home/sfmqrb/git/rishe/data/verification/page-299.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 299` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T22:35:25.959Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T22:35:26.737Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T22:35:26.752Z] TOOL RESULT

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


## [2026-09-06T22:35:26.922Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-299.txt"
}
```


### [2026-09-06T22:35:26.934Z] TOOL RESULT

```
1	=== PDF page 299 (book page 269) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Kwri, Qwri : to buy  (refs POK:648)
4	#1 (parent #0) [Avestan / Old Persian] refs=FFD:50 | xrî : to buy
5	  #2 (parent #1) [Persian] refs=POK:648; KLN:1241; SYN:817; BQT:743 | xarîdan «خریدن (خرید ، خریدار)» : to buy, accept
6	#3 (parent #0) [Sanskrit] refs=POK:648; BQT:743 | krî : to buy
7	#4 (parent #0) [Sogdian] refs=SOD:167 | xr`yn : to buy
8	#5 (parent #0) [Greek] refs=KLN:1241 | priamus : redeemed
9	  #6 (parent #5) [English] refs=None | Priam : king of Troy in Greek mythology
10	--- entry 1 ---
11	ROOT [Indo-European] Kwsep : darkness  (refs POK:649)
12	#1 (parent #0) [Avestan] refs=POK:649; DRM2:161 | xšap : night ; xšâfniya : night meal ; xšapan : nightly
13	  #2 (parent #1) [Persian] refs=MON; BQT:1229,1239; HRN:169; SYN:992 | šab «شب» : night ; šabdîz «شبدیز» : a "dark colored" horse ☞Deik ; šabestan «شبستان» : "place for holding the night", bed ☞Sta ; šâm «شام (شامگاه)» : dinner, night | extra: شبگیر ، شبگرد ، شبرنگ ، شباهنگ
14	#3 (parent #0) [Sogdian] refs=SOD:29,432 | `xšp : night ; xš`m : evening
15	--- entry 2 ---
16	ROOT Kyô -> redirect to Ki 2
17	
```


## [2026-09-06T22:35:30.687Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-299.json",
 "description": "Read source JSON page 299"
}
```


### [2026-09-06T22:35:30.721Z] TOOL RESULT

```
{
  "pdf_page": 299,
  "book_page": 269,
  "entries": [
    {
      "root": {
        "name": "Kwri, Qwri",
        "lang": "Indo-European",
        "refs": "POK:648",
        "gloss": "to buy"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "FFD:50",
          "words": [
            {"translit": "xrî", "gloss": "to buy", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "POK:648; KLN:1241; SYN:817; BQT:743",
          "words": [
            {"translit": "xarîdan", "gloss": "to buy, accept", "script": "خریدن (خرید ، خریدار)"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "او علم نمی شنید ، لب بربستم - او عقل نمی خرید ، دیوانه شدم",
            "poet": "Abŭ-Sa`îd Abol-Khayr"
          }
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "POK:648; BQT:743",
          "words": [
            {"translit": "krî", "gloss": "to buy", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Sogdian",
          "refs": "SOD:167",
          "words": [
            {"translit": "xr`yn", "gloss": "to buy", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Greek",
          "refs": "KLN:1241",
          "words": [
            {"translit": "priamus", "gloss": "redeemed", "script": null}
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
            {"translit": "Priam", "gloss": "king of Troy in Greek mythology", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Kwsep",
        "lang": "Indo-European",
        "refs": "POK:649",
        "gloss": "darkness"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:649; DRM2:161",
          "words": [
            {"translit": "xšap", "gloss": "night", "script": null},
            {"translit": "xšâfniya", "gloss": "night meal", "script": null},
            {"translit": "xšapan", "gloss": "nightly", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "MON; BQT:1229,1239; HRN:169; SYN:992",
          "words": [
            {"translit": "šab", "gloss": "night", "script": "شب"},
            {"translit": "šabdîz", "gloss": "a \"dark colored\" horse", "script": "شبدیز", "see": ["Deik"]},
            {"translit": "šabestan", "gloss": "\"place for holding the night\", bed", "script": "شبستان", "see": ["Sta"]},
            {"translit": "šâm", "gloss": "dinner, night", "script": "شام (شامگاه)"}
          ],
          "script_extra": "شبگیر ، شبگرد ، شبرنگ ، شباهنگ",
          "note": null,
          "quote": {
            "text": "نه شیرین تر ز شیرین خلق دیدم - نه چون شبدیز شبرنگی شنیدم",
            "poet": "Nezâmî"
          }
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Sogdian",
          "refs": "SOD:29,432",
          "words": [
            {"translit": "`xšp", "gloss": "night", "script": null},
            {"translit": "xš`m", "gloss": "evening", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Kyô",
        "redirect": "Ki 2"
      },
      "nodes": []
    }
  ]
}
```


## [2026-09-06T22:35:30.751Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-06T22:35:30.786Z] TOOL RESULT

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


## [2026-09-06T22:35:35.850Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','FFD','KLN','SYN','BQT','SOD','MON','HRN','DRM','DRM2']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:600])\n    print()\n\""
}
```


### [2026-09-06T22:35:38.123Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

FFD {"title": "Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ماده-های-فعلهای-فارسی-دری-محسن-اب/ -> https://dl.eliteraturebook.com/app/public/attachments/6925d29630b83.PDF (free PDF site; grey)", "lookup_hint": "Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/download): nothing; only a related paid e-book 'واژگان زبان فارسی دری' (fidibo). ketabnak.com/book/45024 is a different book (فهرست فعلهای فارسی).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/s

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id=

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

DRM {"title": "J. Darmesteter, Études iraniennes, 2 vols., Paris 1883", "edition_found": "1883 both tomes in one scan", "kind": "archive_djvu", "url": "https://archive.org/details/etudesiraniennes00darm", "identifier": "etudesiraniennes00darm (t.1 alone: tudesiranienne01darmuoft; t.2 alone: darmesteter-etudes-sur-la-langue-la-litterature-les-croyances-de-la-perse-ancienne)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/DRM.txt", "page_offset": "Tome I: leaf = p + 22 (e.g. leaf 26 = p.4); Tome II (starts ~leaf 364): leaf = p + 364 (e.g. leaf 368 = p.4). Nourai does not say w

DRM2 null
```


## [2026-09-06T22:35:41.719Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','FFD','KLN','SYN','BQT','SOD','MON','HRN']:\n    v=d.get(k)\n    print('==',k, '| page_offset:', v.get('page_offset'))\n    print('   local:', v.get('local_file'))\n    print('   hint:', str(v.get('lookup_hint'))[:400])\n\""
}
```


### [2026-09-06T22:35:43.517Z] TOOL RESULT

```
== POK | page_offset: POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   local: /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt
   hint: Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-d
== FFD | page_offset: 115 leaves (PDF pages); printed page = PDF page − 5 (PDF 40 = p.35). 2nd printing 1385 of the same Qoqnus setting (ISBN 964-311-015-X).
   local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_asmaneketab.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_pages_faseng.txt']
   hint: Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/download): nothing; only a related paid e-book 'واژگان زبان فارسی دری' (fidibo). ketabnak.com/book/45024 is a different book (فهرست فعلهای فارسی).
== KLN | page_offset: KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   local: /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt
   hint: Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
== SYN | page_offset: leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   local: /home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt
   hint: Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed page number line.
== BQT | page_offset: vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').
   local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt']
   hint: grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metada
== SOD | page_offset: printed page ≈ leaf − 66 in SOD_pages.txt (0-based \f blocks; 645 leaves; English intro precedes)
   local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD.txt']
   hint: Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id
== MON | page_offset: None
   local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt']
   hint: Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/ab
== HRN | page_offset: leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   local: /home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt
   hint: Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.
```


## [2026-09-06T22:35:47.836Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"Page(s): 648\" POK_full.txt | head -20\necho \"---649---\"\ngrep -n \"Page(s): 649\" POK_full.txt | head -20\necho \"---lemma kwrei---\"\ngrep -n -i \"lemma: k.*rei\" POK_full.txt | head -20\necho \"---ksep---\"\ngrep -n -i \"lemma:.*ksep\\|lemma:.*sep-\" POK_full.txt | head -20"
}
```


### [2026-09-06T22:35:47.938Z] TOOL RESULT

```
53508:Page(s): 648 
---649---
52437:Page(s): 649 
53162:Page(s): 649 
53549:Page(s): 649 
53578:Page(s): 649 
---lemma kwrei---
47070:Root/ lemma: kei-\ to move, go, departure, *die, derived from Root/ lemma: Rei-1\ to lie 
48281:Root / lemma: krei-1 
48306:Root / lemma: krei-2, kreig-, kreik- 
53463:Root / lemma: k''rei-{*k''ehur-) Note: common Proto Germanic -u- > -u-, -y-, -/-. 
---ksep---
53551:Root / lemma: Irsep- (?) {*g''sehup-) 
73921:Root / lemma: sep-
```


## [2026-09-06T22:35:50.130Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '53460,53600p' POK_full.txt"
}
```


### [2026-09-06T22:35:50.187Z] TOOL RESULT

```
Wackernagel-Debrunner 3, 558 ff. 
Page(s): 644-648 

Root / lemma: k''rei-{*k''ehur-) Note: common Proto Germanic -u- > -u-, -y-, -/-. 

Meaning: to buy 

Grammatical information: present kTi-na-mi 

Material: Old Indie knnati^ buys ' (/"after Ar/Ta- participle; ved. also A/7/7a//according to 

poetic meter, as also Pali kinati), Infin. kretum, kraya-^ purchase, purchase price'; npers. 

xandan^\i\yi'\ 

gr. Tipiapai " buy '; 

Old Irish cren(a)im {*k"'ri-na-mi) "I buy', Konj. ni-cna{*k"riiat), crJth^ payment, purchase 
', cnthid^ fond of buying '; cymr. prynu' receive, ransom, to purchase the freedom of; 
sometimes, to set free for a ransom ' (3. Sg. acymr. prinit), corn, prenne, perna, bret. prena 
"buy', cymr. prid{= Irish crlth) ' mortgage, pledge, pawn '; 

Maybe alb. blenj^ buy ' : corn, prenne, perna, bret. prena^b\}Y [common lllyrian Celtic k"- 
>p-. 

Middle Irish tochra^ the wooing ' ("*purchasing of the bride'), t-ind-s-cran. ' purchase price 
for the bride' (seems *k"rqio-= Old Indie kraya-), cymr. g(w)o-br^ price, guerdon, reward, 
recompense, prize, trophy ', corn, gober, bret. gobrds., cymr. also go-brwyds. {-wy- 
suffix); verbal noun Akk. Middle Irish CAe/icc (formal after reicc^ sell ', whereat s. 



Thurneysen Gr. 454), Old Irish fochr(a)icc\. " guerdon, reward, recompense, prize, trophy 



Old Lithuanian (Gen.) krieno' price for guarantee, price for engagement ', Latvian 
kriens, krienis^ present to the bride ', also Lithuanian kraTtis^ dowry, dowry of the bride'; 

Old Russian krbnuti, krenuti^buy\ Infin. kriti, russ. -Church Slavic once also u-kri-jen-b 
{*u-krbjen-b) " bought ' without the present nasal; 

Tocharian A /r^/yar 'trade', kuryart^ trader ', B karyor' purchase ', keryorttau^ trader '. 

References: WP. I 523 f., Trautmann 142, MiJhlenbach-Endzelin II 284, Kuiper Nasalpras. 

197. 

Page(s): 648 

Root / lemma: ICfmi-i^ k^ehurmi-) Note: common Proto Germanic -u- > -u-, -y-, -/-. 

Meaning: worm, grub 

Note: 

-/77- suffix lllyrian Greek stem formation. 

Material: Old Indie /r//77/-"worm, maggot '; np. A//777 'worm'; 

alb. krimp{krim-bi), Geg kri/m ds.; (common alb. -w- > -y-, -i-) 

Also alb. kermiir snail ' : Lithuanian kirmele^ worm ' (common Polish alb. y > e) 

Old Irish cru/m'\Norm', Proto Irish k"rimi-, cymr. pryf, corn. ds. 'worm', bret. prenv6s.; 
gall. FIN *Primia> Modern High German Pfrimm, Primantia> Modern High German Prims, 

Old Prussian g/rm/s{\eg. kirmis) ' maggot '; Lithuanian kirmism. f. etc. ds., Latvian 
cirminsrw. ds., Latvian cermet ' worm, mawworm, hook-worm, bot, helminth ' 
MiJhlenbach-Endzelin I 378 under 386; 

sloven, dr/77' carbuncle, red gemstone, finger worm ', poln. czerh{io'c *czerrhl compare 
Serbo-Croatian crn ' metallic oxide, rust ' for *crirR) ' worms in the rotting meat ', czermieh 
' Dragon tea ', czermiowka^ morel, nightshade, any of various herbs and shrubs of the 
genus Solanum '; 

in addition Adj. -formation of Slavic *cbrmbrrb 'red'. Old Bulgarian crbmbnb 'red', 
crbmbnovati s§^ turn crimson ' etc.; 



the e-lengthened grade seems to exist in Latvian cermet ' eartJiworm ', cerme'\Norm'; 
besides si. *cbrmb is found *cbrvb with peculiar vi- suffix: Old Bulgarian crbvb "worm', russ. 
cervbeic; compare Lithuanian *skirvis^ ant '? 

References: WP. I 523, Trautmann 134, Specht KZ. 65, 212 f., Indo Germanic Dekl. 45, 

181. 

Page(s): 649 

Root / lemma: Irsep- (?) {*g''sehup-) 

Meaning: dark 

Material: Old Indie ksap, /rsa/Oa "night", Avestan xsap- "darkness"; common Old Indie gh- > 

ks- : Old pers. gh- > xs- : npers. xs- > s- 

gr. ijJEcpac;, ijjscpoc; n. " darkness", iiJ£(pap6(;, i|j£(pr|v6c; "dark"; Kvscpac; " darkness"; 

Note: 

common gr. k''s->ps-. 

Maybe alb. Geg mshef, Tosc fsheh^\\\6e (in the dark)" common Old Indie gh- > ks- : alb. 

/r"/?- > ph- > f- 

5v6(po(; " darkness ", later Yv6(po(; ds., hom. 5vo(p£p6(; "dark", ioSvscpnq " dark (as the 

flower), purple-dark "; ^ocpoq " darkness", ^ocpspoq "dark". 

common Old Indie gh- > ks- : lllyrian-alb. - hom. gh- > d-, z- 

The changing gr. aniaut based on taboo images. 

References: WP. I 524 f., WH. I 289, Specht Indo Germanic Dekl. 1 1 . 
Page(s): 649 

Root / lemma: /ab^- {*/ehdb^-) 

Meaning: to grab, hold 

Material: Old Indie labhate, lambhate, rabhate{Pexi. lalabha) " grasps, seizes ", labha-xx\. " 

the obtaining, profit, gain, benefit, advantage", rabhas-n. " impetuousness, hastiness, 

force, might", rabhasa-'wM, boisterous, vast, grand"; 

gr. Aacpupov "booty", apcpi-Aa(pn(; "wide, big, large"; 

Lithuanian /ob/sm. "blessing, possession, richness ", /oM" become rich ", ablaut, /abas 
m. "blessing", also " good ", Latvian Old Prussian /abs^ good ". 

References: WP. II 385, Trautmann 148, Kuiper Nasalpras. 148 f. 



Page(s): 652
```


## [2026-09-06T22:36:09.340Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT xri ===\"\ngrep -n \"xrī\\|xri-\\|xrīnāiti\\|xrinaiti\" BRT.txt | head -30\necho \"=== BRT xsap ===\"\ngrep -n \"xšap\\|xšapan\\|xšafn\" BRT.txt | head -40"
}
```


### [2026-09-06T22:36:09.401Z] TOOL RESULT

```
=== BRT xri ===
=== BRT xsap ===
```


## [2026-09-06T22:36:10.771Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN priam ===\"\ngrep -n -i \"^Priam\\|priamai\\|πρίαμαι\" KLN_1966.txt | head -20\necho \"=== KLN 1971 priam ===\"\ngrep -n -i \"priam\" KLN_1971.txt | head -20"
}
```


### [2026-09-06T22:36:10.843Z] TOOL RESULT

```
=== KLN priam ===
30223:Priam,  n.,  king  of  Troy  and  husband  of  Hecuba (Greek  mythol.)  —  L.  Priamus,  fr.  Gk.  IIpix[zo;, ‘Priam’,  a  name  prob.  meaning  ‘redeemed’,  and rel.  to  irpixcribu,  ‘to  buy’,  fr.  I.-E.  base  *qwri-, ‘to  buy’,  whence  also  OI.  krinati,  ‘buys’,  Mod- Pers.  xaridan,  ‘to  buy’,  Oir.  crenaim,  ‘I  buy’, crith,  ‘purchase’,  Russ.-Church-Slav.  krinuti,  ‘to buy’,  Toch.  A  kuryar,  ‘trade’,  B  karyor,  ‘pur¬ chase’.
=== KLN 1971 priam ===
40617:Cassandra, n., daughter of Priam, king of Troy. 
111224:Priam and Hecuba, and the greatest Trojan 
111232:Hecuba, n., principal wife of Priam and mother 
111551:Helenus, n., a soothsayer, son of Priam, king of 
112595:and see in it a reference to Paris, son of Priam 
119504:descendant, of Priam’, etc.). Cp. -idae. 
186603:Polydorus, n., the youngest son of Priam (Greek 
187050:Polyxena, n., daughter of Priam and Hecuba and 
191071:Priam, n., king of Troy and husband of Hecuba 
191072:(Greek my t hoi.) — L. Priamus, fr. Gk. nplajioi;, 
191073:‘Priam’, a name prob. meaning ‘redeemed’, and
```


## [2026-09-06T22:36:18.043Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\ndata=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\ni=data.find('Priam,  n.,  king')\nleaf=data[:i].count('\\f')\nprint('leaf',leaf,'approx printed page', (leaf-12)*2, 'to', (leaf-12)*2+1)\nEOF\necho \"=== BRT sample ===\"\nhead -c 600 BRT.txt\necho\necho \"=== grep xsap variants ===\"\ngrep -n -i \"xsap\\|hsap\\|ksap\" BRT.txt | head -20"
}
```


### [2026-09-06T22:36:19.911Z] TOOL RESULT

```
leaf 662 approx printed page 1300 to 1301
=== BRT sample ===
Google
This  is  a  digital  copy  of  a  book  that  was  prcscrvod  for  gcncrations  on  library  shclvcs  bcforc  it  was  carcfully  scannod  by  Google  as  pari  of  a  projcct
to  make  the  world's  books  discoverablc  online.
It  has  survived  long  enough  for  the  Copyright  to  expire  and  the  book  to  enter  the  public  domain.  A  public  domain  book  is  one  that  was  never  subject
to  Copyright  or  whose  legal  Copyright  term  has  expired.  Whether  a  book  is  in  the  public  domain  may  vary  country  to  country.  Public  domain  books
are  our  gateways  
=== grep xsap variants ===
2550:äJffj  ti  'take  paiti  ..  V.22.2f.;  —  Da.'  aoAvo  (Stvetx.)  yal  as/tainti  Y.i^.6  \isw.; in  Verbindung  mit  anya-  Du.  (s.  i  b):  —  'tagsam  sünam  ..yimpasuiJiaurvamca.. asUm^mastrrfttqm  vispacayö*>nastr?inqm  i  V./^J.S;  —  'farahqm  urvaranqm  yat  ätri.- amqsta  fsd.)  ''i^arö.cikaya  *°le  anye  cika- ■  ciirranqm  V,4',75;  —  'ttm  ratümca  .. yatö  "wenn  einer  ,  .  und  wenn  einer  ,  .  \yim  maiaydhanmaim  A.j.3(?).  b)  sub- vcrletzt,  so  sollen  sie  dies  und  jenes  . ."  stasA\v\&c\\- 'ta(^T>.)äb3r3ta*sraosiivariza F,_jc  b)  adjektivisch:  j'iT/fl/ire'a/ara.-  vicarayaDm  "die  beiden,  der  .^.  und  der iri^yeiti  kva  "tarn  xsapan»m  . .  *vanAaiti  Sr.  .  ."  N.  jcf ;  —  cval  'te  (ADn.)  stai- "wenn  ein  Gläubiger  stirbt,  wo  weilt  asi\tiüa  bar>iis^a  ..  nasus  .,  fräsnaoiti dem  Tä^  (des  Todes)  . ."  H.  2.  i;  — yö  "..  die  beiden,  das  Bett  und  das  Polster .." . .  upairi  kunanm  (sdL)  manö  baräi  i-up^m  V.  7.9;  — ■  azim  °ta  (APn.)  zaota  zlsJi  (sd.) 'tfm  paiti  zmämm  aUariin  uri'a  kllayäi  ..  /rasrao^r?mca  /ragl>r>mca  . .  Vr._j.7; (sd.)  "wenn  einer  . .,  so  . .  während  der  —  't^m  nitamim  As'>rjm  '^rivacahim  (sd.) ganzen  Zelt  (seiner  Cberhebung)  .  ."P.  "id  minimum  Aj^/um:  triverbe"  F.  27b; J7.  a)  wo    wir   'solch'   brauchen:  yö  —  haomü  kutö  .  .  ava    'te  ahuta  .  .  "ge-
2660:•  p.  aiva-,  j.,  g.  aeva-,  j.  oiva-'*  Zw. (fem,  'vn-)  'ein*  i)  als  eig.  Zw.,  im  Gegens. zu  anderen  Zw.  oder  einer  beliebigen Mehrheit  'ein;  einzig,  allein' :  tilm  '*  . .  di'a . .  tisrö  F.  /;  —  nöit  . .  °vo  nvit  dva  mit '^räyS  nöit  fräyankö  Y.44\  —  'vake  .  . *al>ntaoyaAe  .  .  dvaya  .  .  'irayqm  V.  iS. 11;  ^.0^,108;  —  ^riS"  may^m  (sd.)  .. dva  ..  *öiin'^ '^  \. 16.12;  • —  zayante  .  . dasa  puira  >rayä  . .  ^rHyÖ  .  ,  ^rJyS  .  . »ra  (statt  NSm.)  Az.5;  Vyt^i  —  'vqmvä avi  xsapan>in  äuyS  vä  pancäsahm  va  Yt Ali;  —  'va  (IS.)  'iritva  akmiil  masye- Aim  .  .  dva  iriA-a  .  .  ^ribyö  ^rih'aiifyö V,  2. 1 1  f.;  —  cvaf  .  .  yaam  (sd.)  frabaräti
2663:dva   danart  .  .  'va    (statt   ASn.!)    danan  ayar»   äjasaiti  °va  vä  xsapa  Aog.  5/;  —
3140:•  j.  a-xsapan-  f.  'Abenddunkel,  "xsafni x/afnJm  is>mn~'  "im  Abenddunkel  sich das  Abendmahl  suchend"  Yt  14.  zo.
3684:sa3^3rJ{iA.)  . .  ya  ..  vav}r?SSi  pairlJült ..  yäia  var?^aitg  '/LcTblJ  Y.  25,4;  — ai^qmät  ä  ahtnJ  .  .  vTci>3i  (sd.)  -/)"■■>  Y. j2. 8.  a)  mit  Neg.;  'nicht  hinfort  mehr, länger":  »»3  ^I^ä  *fX  äsbävayal  (sd.)  Y. Jt.i7.  3)  'auch,  gar,  besonders',  das vorherg.  Wort  hervorhebend:  maS^a  .  . pirs^u  'pi  ffi/ajii/Vjy  "die  Wolken,  die  sich gar  weithin  verbreiten"  YLA40;  io.44; —  \daraiy  'piy  "gar  fernhin"  X.7. 2;  D, 6'.a,  4";  —  ai'e  °pi  dai'jyanlS  "'äx£  y^a^ besonders  hinsehend"  Yt/0.45;  45;  — *avat  'pi  ya^a  . .  "soviel  gerade  (,  eben) aIs.."V.ö'.io;22,Äa3,J7.7.  I^Praen. 1)  mit  Akk.  a)  'über  —  hin';  a)  zeitlich: dar>-^3mHt  °pi  zrvätam  Y.  6-1. 3 ;  Yt  i^. aö,  ß)  räumlich:  vTspqmHl  'pi  imqm  sqm Y. 57.33; — liuire fraväitUßA.)  tq%ryqm  °pi xSapamm  Yt  74. 1 3 ;  —  yavat  anu  "pi  *i}iti garayS  visasiar?  vlsptm  aval  °pi..  "so  gross der  Raum  ist,  über  den  hin  sich  die  üerge erstrecken,  über  all  den  Raum  hin  . ." Yt. 7p.8.  b)  'bei':  k?m  ksm  °pi  nmäm "bei  Jedem  im  Haus"  Yt.  5. 102.  2)  mit Lok.  'bei',  zeitlich:  mi^nm ..yahmi  ssire m%%rS.dru}5  'pi  %n<isi  paun'a{sA.)  masyS- kunhs  ". .  bei  dessen  Gericht  . ."  Yt.  lo. 8of?).  3)  mit  Instr.  'nach',  zeitlich: s.  aipi  tä,  aipi  taiS  bes.  III)  Praev. {m\\.kan',  karat-,  gart-,  gam-,  vai-,  varpi- ua.).  [IIBh.4.8:  lies  utämaty^'»; —  Y.
3716:•  j.  aipLdvipiara-  Adj.  (fem.  'ra-)  "wolkig,  |  (eben)  zur  Nachkommenschaft  gelangt  ist, neblig';  xsaps  va  *tq%Tyh  °rayS  "oder  in|(jüngst)geborenliat', von FrauemnJiWiffm finsterer,  nebliger  Nacbt"  Yt//.4-  \yqm  °ram  .  .  anasaxtqm  (sd.)  V,  J5.8;  —
3932:•  j.  aiwi'Stay-  f.  1)  'Studium',  uzw.  spez. der  heiligen  Texte  der  jBozi/ischeQ  Reli- gion: nSit  mi  apqm  ä^rava  °til  (AP,)') ''virmye  (sd.)  daitihava  carlt  (sd.)  Y.  *j. 24.  2)  'Lesen,  Vorlesen',  spez.  liturgi- sches, Lesen  der  Liturgie;  cvat  *°lim''> parayap  "irixsapanm  ka>rähm{sd.)'a.4-
4575:•  j.  'an'tara-  Adj.  'der  innere,  innen  be- findlich': 'r^m  ür^Mfii  nmanahe  "ins  Innere des  Hauses"  V.6'.43;  —  'rat  W.  2.^0 PüZ.  a)  'rat  naimax  'innerhalb',  mit folg.  1)  Gen.,  z)  Lok.,  3)  Instr.,  4)  Akk., uzw.  a)  räumlich,  b)  zeitlich:"  1  a)  a'  n- hsirake  N.  Go;  104';  —  *a'  n°  *yujyastHs N.  -ji  T'*j  —  a'  W  aEi3.drajahyehe  N. Ii()',  —  a'  n°  '^rigämyt/ie  N. 65.  1  b)  a- II'  tiava.xsaparahe  V.  5. 43.  !  a)  a'  11° barj''irisi'a  y.^.^i.  3  a)  a'  n'  brrat.- byqm  V.  Ä41,  42,  g.  15,  16.  4  a)  a' tr  aSe  pa>a  "auf  diesen  Wegen"  V.  8. 104.  4b)  a°  11°  triilzär.ljaAlm'V.^.^y, —  a-  n' yanJräßV.O.a,  3,  7.77.  Tai fialinät  N.^.^3).  Ta  N.JOi(?);  —  'nm N.pj(?).
4637:H'  nava.xsaparaAeV.  $.4^.  ;  a)  a' fi'
4701:•  j.  a-marant-  Adj.  (ohne  Obj.)  '(die  vor- geschriebenen Gebete)  sich  nicht  ins  Ge- dächtais zurückrufend,  nicht  in  Gedanken wiederholend':  yö  saite  haurvqm  taras^a xsapaiigm   ayaztmnö  asrilvayamnS  'rS  V.
4820:—  zu' :  xshms  asamqm  unänö  pärayeinii . .  avi  garS  nmänam  V.  75.32;  —  x3  patti apqm  paräiti  .  .  a^ra  . .  V.  jj.  51;  — xraosyS-taraca  (sd.)  .  .  hv5  urva  paräiti par3.asnäi  amihe  yaia  . .  V,  13. 8;  —  ya- tärö  paurvs  us>hiUaiti  paräiti  vahiltahe atshsus  y .  iS.^d.  2)  'aus  (dem  Haus) gehen  auf  — ,  zum  Zweck  der  Verrichtung von-'  (Akk.):  *kat!lmS  timänahe  a'iauru- fi9m{sd.)  pärayäf^''  N.  /;—  para  paoiryö äiti  (näml.  a^aururitm)  para  bityö  aiti para  "hrityS  äiti  aita  paräyaiti  ycc^a gae'^äbyS  *k)nti  "es  geht  der  erste  (auf Priesterdienst)  aus  . .  der  zweite  . .  der dritte.,;  es  gehen  die  weg,  die  (zum  Schutz) für  den  Hausstand  da'gelassen  worden) sind"  N, 2 (?)"'; — katärsm  *ä'irava  ctiauru- n>m  Vä  parayat  galiaiiqm  vä  asp^nns (sd.)  avat  N.^;  —  katärS  a'^aurun?rn ''parayat  nSirika  vä  nmätiSpaitiH  väi yezica  vä  ga^hä  vTmä  (sd.)  *katarascit ''parayat  N.  5;  *5";  —  *cvät  ''aiwtstXm parayap  'irixsapar>m  .  .  yS  haoys  (sd.)  . . paräiti  nsit  .  .  anaiwistim  (sd.)  ästryanti N.  4.  a)  mit  haca  und  Instr.:  cval  .  . äiirava  a'iaurumm  haca  ^gafi^äbis^para' yat  N,  4-  3)  'sich  an  etwas  (Akk.) machen':  yö  nar)m  ..  kasyat»he{%d.)  sanhai daoaili  vl^va  aval  hava  xraiwa  paräiti "—  wissentlich  mit  voller  Absicht  macht  er sich  daran— "V,  15- 2.  4)  'hingelangen zu  — '  sva.  'sich  verschaffen':  ffi.j(Akk.),. kaine-.tarS  äaxit^m  pärayät  tarS  ap»mca urvarqmfa  yezica  . .  tarS  (sd.)  daxst>m paräiti  . .  "nicht  soll  das  Mädchen  heim- lich sich  die  Regel  (wieder)  verschaffen, heimlich  sich  Wasser  und  Kraut  verschaf- fen .."  V.i5,9f.
4869:•  ).  ayan-,  j-,  g.  ayar-  n.  'Tag';  a) Gegensatz  zur  Nacht:  *oim  . .  'yar>  (NS.) tYjasaiti  .  .  a?va  v3  xsapa  Aog.  J/;  ■ — ai»ke  'yan  (GS.)  .  .  airikh  xsaj>ö  \t.  i .-iZ, i/.S;  Vyt.J0(?);  —  hamahe  °yqn  hamayn 1-3  xsa/w  Y.  S7-3I,  Yt.ÄS4;  '  10.  iij  (f), Vyt^f?);  —  vlspsU  'yqnia  (AP.)  xlaf- nas.'a  Y.  57. 1 7,  Yl  /.  i  i  ;  —  *frayaire  "yan (LS.)  bavaiti  (sd.j  hubai,rü  .  .  aia  apare 'y<pi  ■-  Aog.  35;  —  */rayarfne  vä  uza- yariu^fsd.)  va  *'yan''>  N.5;  —  dvadasati- hiinm  (sd.)  asü  *ayrim  °yar)  F.  27  b 27b;  —  °yqn  (LS.)  va  varstafsö  var»t3.vTrt [sd.)JaiJnti  V.S.^.  b)  als  der  Zeitraum von  Sonnenaufgang  zu  Sonnenaufgang: iiz£.a  yan  mainyenie yaty3r)N.2.^\ ^räyö  yara''  Vd.  ly;  <),  if),  si;  —  pasca xsavaidim  (sd.)  yaranqm^a'''  Vd.  f)\  11, '5>  '9  '■  c)  sva.  festgesetzter,  bestimmter Tag:  myazdahe  ''ya''''  (LS.)  "am  Tag  des My:'  N. Si-,  "y:;  *^jj  —  kaia  (sd.)  yiri (AP.)  daxiärS  .  .  drfs  Y.  43-  T,  —  yan ami^näitii&d.)  juye  tanus  Aog.^j.  d) 'Zeit':  vUpI  'yärj  (AP.)  dangö.jyäiöU (sd.)  .  .  "alle  Tage  . ."  Y.  43-  2.
4905:•  j.  a-yaz9mna-  Adj.  'nicht  betend':  y^ saSte  haurvqm  tarüsca  xsapamm  °«5| ". .  ohne  zu'beten"  V.JÄs;—  mitAkk. 'zu  -':  yüi  °na  am>Ss  sp>nl!"ä\t  nicht  zu den  ASp.  beten"  Vyt  12.
5038:I  xsaparäl  us  lanam   snayaeta  us  . .  pattt Yt 73.25.        [s!  noch  avi&ia  No.  5],       \°%a  yaozdayqn  (sd.)  "nach  drei  Nachten Ableit.  -  Pü.  (lu  V.  4)i  an,  (lu  H.  3,  N.  15):  \  soll  man  den  Leib  waschen  . .;  auf  diese
5739:•  j.  a-sä£ayant-  Adj.  'nicht  lehrend';  ys saite  haurvqm  iarasca  xsapanim  ayaztmnö ..  asixsJ  asJäzyS  . .  "..  nicht  lernend,  nicht lehrend  . ."  V.  iS.  5.
5920:•  j.  a-sravayant-  Adj,  'nicht  vortragend, aufsagend,  rezitirend';  a)  mit  Akk.:  yB gaisS  (NS.)  'yS  tiaimpm  yäri.dräjJ  "wer  die G.  ein  halbes  Jahr  lang  nicht  aufsagt" N.  44;  41-45''.  b)  ohne  Obj.  '(die vorgeschriebenen  Gebete)  nicht  sprechend': yS  salte  haurvqm  tarasca  xsapatum  ayo' Z)mns  °yif  amarä  V.  /Ä  5 ;  —  *frasrävüy3 rüiufris  tidit  *'°yS'^  N.  104.
6962:i)  die  Richtung  auf  den  Sprechenden  zu angebend  'her,  heran,  herzu',  nur  in  äca paraca  'her  und  fort'  sva.  'hin  und  her, hin  und  zurück'*':  'hrixsaparim  hahräkgm (sd.)  *xh'ai  xsa/nd  aca  paraia  N.4;  — pairika  ,  .  3ca  paraca  dvaraiH  YtÄ  54; —  v?r>^raynpm  ..  yö ..  äca  paraca  p}r?- saite  Yt.14.4-j.  ")  anschliessend  'dazu, dazu  auch,  und  auch':  a?s^  zi  vnxs  . . */ramrva»ö  a  vacO  afiunS  vairyö  fraoxtd .  .  spanvanti  H. /.4;  —  hä  hama  pairi- säiU  frapaya  (sd.)  daühus  ä  upaosatfh- väsca  Yt ig.\\  —  yS  H  axtÜ  akmäi  yJm axtsysi  (sd.)  dstihg  ^.36.  i ;  —  'kwSi  as *ärmaitis  ^w!  ä  gStt^  tasä  (sd.)  as  Y.31. 9.  a)  wiederholt  'et  ,  .  et',  nach- gestellt: akunm  mazdqm  amruyi  (sd.) nmänake  nmänS.patsis  ratüm  ä  viss  Tlspa- tsis  ratüm  ä'  .  .  daiähupatOts  ratüm  3 Y.  lg.  I.  a)  in  Verbindung  mit  (vor-
6998:Akk.  nebeneinander  -...hl  urvarum  vaAisütii ahüm  frapärayetii  . .  a  vahUtat  ataAaot  a . .  asat  a  . .  raocSbyS  Y.ig.d.  '  b)  zeit- lich: Jravasayö  . .  ya  haca  gayai  mariisnat a  saosyaiitat  virnHrayria^  Y. 26.10;  — pu^rJ . .  apara.iri^inis  *S  da/a('*^  vttataoi (sd)  Yt/J.ii,2i,  28;—  apqm..fratii.. haca  Aä  vaxist  S  ^hü'-^^  /rsfmSJatSil pairi.sacaiti  li.48;  Yt.5.91,  V.13.1;  — S  maioyat  xsapai  N.  50,46;  —  a  darsyai \x^ä.l>airyat  (sd)  Y.  60.6;  —  vTsp?m  ä ahmst  sbes.  c)    'in,   bei',    räumlich;
7222:\-,  g-",  P-'*.  ä,  j.  »flä),  j.,  g.  a"4>  I)  Adv. )  die  Richtung  auf  den  Sprechenden  zu ngebend  'her,  heran,  herzu',  nur  in  tua paraca  'her  und  fort'  sva.  'hin  und  her, hin  und  zurück''':  %rixsapar3m  hairähm (sd.)  *xsfas  xsafnö  äca  paraiä  N.4;  — pairika  .  .  Sca  paraca  dvaraiti  Yt.  Ä54;
7609:•  j,  »-var«zyant-  Adj.  i)  mit  Akk,  'nicht wirkend,  begehend':  'zinbyd^"^  pascaila araiwya  syaoina  V.J.  40.  2)  ohne Obj.  'sich  nicht  übend  (tn  den  Werken der  Religion)';  yö  saite  haurvqm  tarasca xsapamm  ayazsmns  . .  'zyö  ".  ,  ohne  zu beten  . .  ohne  sich  (im  Guten)  zu  üben" V./&S-
```


## [2026-09-06T22:36:28.104Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== headword xsap ===\"\ngrep -n \"^•.*xsap\\|^• .*xsaf\\|^•.*xsafn\" BRT.txt | head -20\necho \"=== xsafnya ===\"\ngrep -n \"xsafnya\\|xsafniya\\|xsafnim\\|xsafno\" BRT.txt | head -10\necho \"=== xri kaufen ===\"\ngrep -n \"kaufen\" BRT.txt | head -20\necho \"=== xri- headword ===\"\ngrep -n \"^•.*xri\\|xrinaiti\\|xrTnaiti\\|xrl-\" BRT.txt | head -20"
}
```


### [2026-09-06T22:36:28.222Z] TOOL RESULT

```
=== headword xsap ===
2660:•  p.  aiva-,  j.,  g.  aeva-,  j.  oiva-'*  Zw. (fem,  'vn-)  'ein*  i)  als  eig.  Zw.,  im  Gegens. zu  anderen  Zw.  oder  einer  beliebigen Mehrheit  'ein;  einzig,  allein' :  tilm  '*  . .  di'a . .  tisrö  F.  /;  —  nöit  . .  °vo  nvit  dva  mit '^räyS  nöit  fräyankö  Y.44\  —  'vake  .  . *al>ntaoyaAe  .  .  dvaya  .  .  'irayqm  V.  iS. 11;  ^.0^,108;  —  ^riS"  may^m  (sd.)  .. dva  ..  *öiin'^ '^  \. 16.12;  • —  zayante  .  . dasa  puira  >rayä  . .  ^rHyÖ  .  ,  ^rJyS  .  . »ra  (statt  NSm.)  Az.5;  Vyt^i  —  'vqmvä avi  xsapan>in  äuyS  vä  pancäsahm  va  Yt Ali;  —  'va  (IS.)  'iritva  akmiil  masye- Aim  .  .  dva  iriA-a  .  .  ^ribyö  ^rih'aiifyö V,  2. 1 1  f.;  —  cvaf  .  .  yaam  (sd.)  frabaräti
3140:•  j.  a-xsapan-  f.  'Abenddunkel,  "xsafni x/afnJm  is>mn~'  "im  Abenddunkel  sich das  Abendmahl  suchend"  Yt  14.  zo.
3687:•  j.  aipi.awra-  Adj.  (fem.  °rä-)  'bewölkt': iq'iryaiHt  haca  xsafnS  .  .  "rayü  Yt  14.. 31  •>.
3716:•  j.  aipLdvipiara-  Adj.  (fem.  'ra-)  "wolkig,  |  (eben)  zur  Nachkommenschaft  gelangt  ist, neblig';  xsaps  va  *tq%Tyh  °rayS  "oder  in|(jüngst)geborenliat', von FrauemnJiWiffm finsterer,  nebliger  Nacbt"  Yt//.4-  \yqm  °ram  .  .  anasaxtqm  (sd.)  V,  J5.8;  —
3932:•  j.  aiwi'Stay-  f.  1)  'Studium',  uzw.  spez. der  heiligen  Texte  der  jBozi/ischeQ  Reli- gion: nSit  mi  apqm  ä^rava  °til  (AP,)') ''virmye  (sd.)  daitihava  carlt  (sd.)  Y.  *j. 24.  2)  'Lesen,  Vorlesen',  spez.  liturgi- sches, Lesen  der  Liturgie;  cvat  *°lim''> parayap  "irixsapanm  ka>rähm{sd.)'a.4-
4575:•  j.  'an'tara-  Adj.  'der  innere,  innen  be- findlich': 'r^m  ür^Mfii  nmanahe  "ins  Innere des  Hauses"  V.6'.43;  —  'rat  W.  2.^0 PüZ.  a)  'rat  naimax  'innerhalb',  mit folg.  1)  Gen.,  z)  Lok.,  3)  Instr.,  4)  Akk., uzw.  a)  räumlich,  b)  zeitlich:"  1  a)  a'  n- hsirake  N.  Go;  104';  —  *a'  n°  *yujyastHs N.  -ji  T'*j  —  a'  W  aEi3.drajahyehe  N. Ii()',  —  a'  n°  '^rigämyt/ie  N. 65.  1  b)  a- II'  tiava.xsaparahe  V.  5. 43.  !  a)  a'  11° barj''irisi'a  y.^.^i.  3  a)  a'  n'  brrat.- byqm  V.  Ä41,  42,  g.  15,  16.  4  a)  a' tr  aSe  pa>a  "auf  diesen  Wegen"  V.  8. 104.  4b)  a°  11°  triilzär.ljaAlm'V.^.^y, —  a-  n' yanJräßV.O.a,  3,  7.77.  Tai fialinät  N.^.^3).  Ta  N.JOi(?);  —  'nm N.pj(?).
4701:•  j.  a-marant-  Adj.  (ohne  Obj.)  '(die  vor- geschriebenen Gebete)  sich  nicht  ins  Ge- dächtais zurückrufend,  nicht  in  Gedanken wiederholend':  yö  saite  haurvqm  taras^a xsapaiigm   ayaztmnö  asrilvayamnS  'rS  V.
4869:•  ).  ayan-,  j-,  g.  ayar-  n.  'Tag';  a) Gegensatz  zur  Nacht:  *oim  . .  'yar>  (NS.) tYjasaiti  .  .  a?va  v3  xsapa  Aog.  J/;  ■ — ai»ke  'yan  (GS.)  .  .  airikh  xsaj>ö  \t.  i .-iZ, i/.S;  Vyt.J0(?);  —  hamahe  °yqn  hamayn 1-3  xsa/w  Y.  S7-3I,  Yt.ÄS4;  '  10.  iij  (f), Vyt^f?);  —  vlspsU  'yqnia  (AP.)  xlaf- nas.'a  Y.  57. 1 7,  Yl  /.  i  i  ;  —  *frayaire  "yan (LS.)  bavaiti  (sd.j  hubai,rü  .  .  aia  apare 'y<pi  ■-  Aog.  35;  —  */rayarfne  vä  uza- yariu^fsd.)  va  *'yan''>  N.5;  —  dvadasati- hiinm  (sd.)  asü  *ayrim  °yar)  F.  27  b 27b;  —  °yqn  (LS.)  va  varstafsö  var»t3.vTrt [sd.)JaiJnti  V.S.^.  b)  als  der  Zeitraum von  Sonnenaufgang  zu  Sonnenaufgang: iiz£.a  yan  mainyenie yaty3r)N.2.^\ ^räyö  yara''  Vd.  ly;  <),  if),  si;  —  pasca xsavaidim  (sd.)  yaranqm^a'''  Vd.  f)\  11, '5>  '9  '■  c)  sva.  festgesetzter,  bestimmter Tag:  myazdahe  ''ya''''  (LS.)  "am  Tag  des My:'  N. Si-,  "y:;  *^jj  —  kaia  (sd.)  yiri (AP.)  daxiärS  .  .  drfs  Y.  43-  T,  —  yan ami^näitii&d.)  juye  tanus  Aog.^j.  d) 'Zeit':  vUpI  'yärj  (AP.)  dangö.jyäiöU (sd.)  .  .  "alle  Tage  . ."  Y.  43-  2.
4905:•  j.  a-yaz9mna-  Adj.  'nicht  betend':  y^ saSte  haurvqm  tarüsca  xsapamm  °«5| ". .  ohne  zu'beten"  V.JÄs;—  mitAkk. 'zu  -':  yüi  °na  am>Ss  sp>nl!"ä\t  nicht  zu den  ASp.  beten"  Vyt  12.
5739:•  j.  a-sä£ayant-  Adj.  'nicht  lehrend';  ys saite  haurvqm  iarasca  xsapanim  ayaztmnö ..  asixsJ  asJäzyS  . .  "..  nicht  lernend,  nicht lehrend  . ."  V.  iS.  5.
5920:•  j.  a-sravayant-  Adj,  'nicht  vortragend, aufsagend,  rezitirend';  a)  mit  Akk.:  yB gaisS  (NS.)  'yS  tiaimpm  yäri.dräjJ  "wer  die G.  ein  halbes  Jahr  lang  nicht  aufsagt" N.  44;  41-45''.  b)  ohne  Obj.  '(die vorgeschriebenen  Gebete)  nicht  sprechend': yS  salte  haurvqm  tarasca  xsapatum  ayo' Z)mns  °yif  amarä  V.  /Ä  5 ;  —  *frasrävüy3 rüiufris  tidit  *'°yS'^  N.  104.
7609:•  j,  »-var«zyant-  Adj.  i)  mit  Akk,  'nicht wirkend,  begehend':  'zinbyd^"^  pascaila araiwya  syaoina  V.J.  40.  2)  ohne Obj.  'sich  nicht  übend  (tn  den  Werken der  Religion)';  yö  saite  haurvqm  tarasca xsapamm  ayazsmns  . .  'zyö  ".  ,  ohne  zu beten  . .  ohne  sich  (im  Guten)  zu  üben" V./&S-
8299:•  j.  upa.maltim  Absol.,  mit  äste  Inf  'es ist  zu  warten,  abzuwarten  bis  zu  — ',  mit Angabe  der  Dauer  des  Wartens  durch Akk.  und  seines  Endpunkts  durch  Instr. oder  Lok.  eines  Nom.  act.:  cval  dräj3  up- äsfe  x^anmti  gamca  yaomca  maiuca  "wie lang  soll  bis  zum  Genuss  von . .  gewartet werden?"  V.5,53;  54;  —  äial  drajö  up' äste  paseil  %rtxsaparat  yütö  gatus  yätö (s(L)  . .  "wie  lang  soll  man  nach  den  drei Tagen  warten  bis  zur  Verwendung  .  ." ^■i-SS;  S^-        [V.^j.ao:  lies  upa  mai/lm.]
10786:•  j.  xsapan-;.rÄy9i- f.,  n.'''Nacht';  a)  im Gegensatz  zum  Tag":  i'ira  vä  asni  i^ra vä  '/ne(LS.)'i  V.4.1;  G.J.T,  Yt.i.9,  16;
10808:•  j.   xsafnya-   n.    'Nacht-,    Abendmahl':
12207:•  j-i  g-  t^mah-  n.  i)  'Finsternis,  Dunkel', Sing,  und  Plur.:  ks  kvSpä  raochslä  (sd.) dät  'mhs<ä  Y.  44.5; — ydisra  nSit  xsapa nSii  °ma  Yt  10.50;  —  dartgSm  3ys(sd.) 'matjAs  Y.JJ.30;  —  mihr^m  ..'manbääa^^ Jiyäurum  ". .  den  im  Dunkel"  wachsamen" Yt  io.  141;  —  'mauAqm  vä  *aiwi^ati (sd.)  V. A4;  —  paitiltJOe  'maakqm  Y.
12235:•  j.  t^Oxya-  i)  Adj.  (fem.  yä-)  'dunkel, finster':  °fyam  aipi  xsapanim  Yi.  14.  13; —  'ryasäi  (GSf)'>  kala  xsafnS  "auch in  finstrer  Nacht"  Yt.  1^31,  ib'.  10;  — xfapa  vä  *'ryä  (GSf,)"  aipi.dziqnaraya YL//.  4.         3)  n.  'Dunkel'  (nur  Ableit).
13608:•  j.  dazdra-n.  — ?— :  ^'hrixsapanm  'rim
14580:•  '].  STi.ayar-  n.  'Zeit  von  drei  Tagen': As  ava%a  vazata  °nm  ^ri.x/apanm''' ", .  drei  Tage  und  Nächte  hindurch"  Yt 5.62;  S.22;  —  °r3m  ^rijxsapanm^'  tanüm frasnayayanta  "während  dreier  Tage  .  ." Yt/o.iaa;  V.p.sö.
17255:•  j.  bi.ayar-  n.  'Zeit  von  zwei  Tagen': °r>m^^  bi.xsafanm  lanum  frasnayayatita "während  zweier  Tage  . ."  Yt.  io.  122.
=== xsafnya ===
10808:•  j.   xsafnya-   n.    'Nacht-,    Abendmahl':
=== xri kaufen ===
=== xri- headword ===
12827:•  j-  y<^01  «i«  dava  ^itsii  uxriltif  P. 54:  -  ?  -.
```


## [2026-09-06T22:36:41.395Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== CHEUNG xrai/xri ===\"\ngrep -n -i \"xrai\\|\\*xrī\\|xrīn\\|to buy\" CHEUNG.txt | head -30"
}
```


### [2026-09-06T22:36:41.450Z] TOOL RESULT

```
=== CHEUNG xrai/xri ===
8675:‘to buy; to take’, Semn. -git-/-gir-, Sang. -gird/gin-, Shamerz. -gít-/girám-, Lasg. 
8682:Yi. yurv-/yurd-, M. yürv-/yoruvd-, yuruvd ‘to buy’, Wa. Jərəv-, јәгәү-/(ә)гәуп-, 
11501:ersinaen- ‘to buy’, NP arz ‘price, value’ 
12569:nos-/nöta- ‘to take (away); to buy; to seize, catch’ 
14314:*NWIR: (+ *4-) ? Semn. h-ài-C-ài-, b-di(-)88- ‘to buy, take’ 
19569:*NEIR: ? Pash. pirawdal ‘to buy’. Ф The verb is no longer quoted in МЕУР. 
23603:*IE COGNATES: Lat. prae-stinare ‘to buy, fix (a price)’, de-stinäre ‘to fix (in position, 
28789:446 *xraiH 
28815:*xraiH ‘to buy’ 
28817:*MIDDLE PERSIAN: MMP xryn- (BMP ZBNN-) ‘to buy’, MMP xyr- ‘to buy; trust’ 
28822:*KHOTANESE: ggän- (gin-) ‘to buy’ || (+ *us-) uysgär(n)- (iysge-) ‘to redeem’ 
28825:*SOGDIAN: SSogd. xryn, BSogd. xr’yn ‘to buy’ || (+ *upa-) MSogd. prxyy ‘payment, 
28833:*CHORESMIAN: т/хп- ‘to buy’ || (+ *us-) m/sxn- ‘to buy (oneself) off, redeem 
28836:*BACTRIAN: Xıp- ‘to buy, acquire’ || (+ *a-) axpıvo ‘purchase’ || (+ *ui-) ouxpuvo, 
28847:xarn-/xarnt ‘to buy’ || (+ *a-) ? Oss. І. arxajyn/arxajd ‘to function; to attempt, exert’. 
28857:*MISC: Orm. $еп-, sun-/sunók, Sin-/¥ Tyék ‘to buy’ = $én-/Sénók 
28859:*SANSKRIT: kray ‘to buy’ (RV, AV+) > EWAia I: 410 
28861:«PIE *K"reiH;- ‘to buy, purchase’ = LIV: 395 f. | Pok.: 648 
28864:Olrish crenaid, Toch. B käry-, kär-nä-sk-, ORuss. krsnuti, krenuti ‘to buy’, OLith. 
55114:*xraiH (s.v.), *xrap! 
55826:to buy 
55886:*xraiH
```


## [2026-09-06T22:36:42.683Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD\nawk 'BEGIN{RS=\"\\f\"} NR==55' FFD_pages.txt | head -60\necho \"=====PDF page 55 (printed 50)=====\""
}
```


### [2026-09-06T22:36:44.424Z] TOOL RESULT

```
[pdf page 55]
وا فعلهای فارسی دری
خرامیدن
«خرامید» ماد ماضی جعلی است. از مادهٌ مضارع ساخته شده است.
: «خرام» < فارسی میانه 337370 < ایرانی باستان 3+737-8*. برای ۵ > آرای. 3
پیشوند فعلی است. ۳370 صورت بالاندةٌ ريشهٌ 77870 است و 77870(«گامبرداشتن» معنی
می‌دهد.
خریدن
خرید < فارسی میانه 7770 < ایرانی باستان 3۳7-1۵*. برای 14 -> آراست. 77 صورت
ضعیف 727 است و آن به معنی «خریدن» است.
خر + فارسی‌میانةٌ مانوی 37. 77 در فارسی‌میانهٌ مانوی و «خر» در فارسی دری‌به این
سبب به وجود آمده‌اند که تصور شده «خرید» مادهٌ ماضی جعلی است و با حذف ۲4مادة
مضارع به وجود می آید. مادةٌ مضارع 3374 در فارسی میانه 778 است» از ایرانی باستان
8 83 نشاته‌ای بوده که برای ساختن ماده مضارع از ريشه به کار می‌رفته است ->
بریدن,
خزیدن
«خزید» ماده ماضی جعلی است. از مادهٌ مضارع ساخته شده است.
خز < پهلوی اشکانی 382. فارسی میانهٌ مانوی 782 < ایرانی باستان ۶۵2-۵
3-2 برای 2 > آرای. 2 صورت افزوده و 7 صورت ضعیف ريشه هستند. 1817 به
معنی «خزیدن» است.
خست + فارسی‌میانه 3881 < ایرانی باستان 3۵9-1۵*. برای 18-> آراست. 740 صورت
اصلی 8 است. 4 پیش از 1به 8 بدل شده است. ريشةٌ 24 به معنی «پاره کردن» است.
خفت < فارسی میانه 911 < ایرانی باستان ۳۵۶-۵". برای 1۵ -> آراست. 1:۸0

=====PDF page 55 (printed 50)=====
```


## [2026-09-06T22:36:52.548Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '28810,28870p' CHEUNG.txt"
}
```


### [2026-09-06T22:36:52.599Z] TOOL RESULT

```
*PIE — > LIV: – | Pok.: 

*REFERENCES: Abaev, Slovar’ II: 219 f. 


*xraiH ‘to buy’ 

*MIDDLE PERSIAN: MMP xryn- (BMP ZBNN-) ‘to buy’, MMP xyr- ‘to buy; trust’ 
с DMMPP: 365a 

Pres.: IND. 3sg. MMP xrynyd,2pl. MMP xyryd; Partic.: perf. pass. MMP xryd 

*KHOTANESE: ggän- (gin-) ‘to buy’ || (+ *us-) uysgär(n)- (iysge-) ‘to redeem’ 
= SGS: 28, 15 

*SOGDIAN: SSogd. xryn, BSogd. xr’yn ‘to buy’ || (+ *upa-) MSogd. prxyy ‘payment, 
wages’ (Sogd.Tales: 466) || (+ *us-) BSogd. sxr’n ‘to rebuy’ || (+ *pati-) CSogd. 
ptxryn ‘to hire’ 

Pres.: OPT. 25р. SSogd. xryny, IMPV. 2sg. BSogd. xr’yn; Impf.: IND. 1sg. SSogd. xr’ynw, 3sg. SSogd. 
xr’yn; Pret.: tr. IND. 3sg. BSogd. xr’yt ö’rt, Inf.: SSogd. xryt || (+ *us-) Inf.: BSogd. sxr’yn’y || (+ *pati-) 
Impf.: IND. 3sg. CSogd. ptyxryn 

*CHORESMIAN: т/хп- ‘to buy’ || (+ *us-) m/sxn- ‘to buy (oneself) off, redeem 
(oneself)’ || (+ *pari-) prxn- ‘to hire’ = Samadi: 236, 188, 158 

*BACTRIAN: Xıp- ‘to buy, acquire’ || (+ *a-) axpıvo ‘purchase’ || (+ *ui-) ouxpuvo, 
ouxpnyavo, oryapnyavo ‘hire, rent” = S-W, Bact.: 231b, 184a, 214a 

*NWIR: Widely attested: NP xaridan/xar-, Kurd. kirin/Kir-, Zaz. herinayis/herinen-, 
Abyan. heria/ -hrin-, Abz. rida/rén-, Anar. -hrit/ (impv.) ihrin, Fariz. -haeri-/-hrin-, 
Gz. (Drin-/Drint, Gil. (Rsht.) hecen/hin-, Isfah. irintän/irin-, Jow. bam-ehri/a-hrif-, 
Meim. bem-heri/a-hrin-, Khuns. irn-/rit, (LW) xer-, Nn. ri/-rin-, Natan. -yar1-/-yar-, 
Qohr. hirida/hrin-, Semn. -irüt-, Sang. be-rsindan, Yar. -häri-/-hrin-, Soi ba-xrid- ‘to 
buy’ 

*NEIR: Oss. І. elxenynmalxed, D. ælxænun/ælxæd, Yghn. xirin-/xirita-, Yzgh. 
xarn-/xarnt ‘to buy’ || (+ *a-) ? Oss. І. arxajyn/arxajd ‘to function; to attempt, exert’. 
Q The stem vowel -æ- of Oss. I. elxanyn, etc. is inserted through paradigmatic 


*xrau 447 


remodelling. || The meaning of Oss. I. arxajyn may have originally been *‘to cause 
to purchase something’. 

*MISC: Orm. $еп-, sun-/sunók, Sin-/¥ Tyék ‘to buy’ = $én-/Sénók 

*SANSKRIT: kray ‘to buy’ (RV, AV+) > EWAia I: 410 

«PIE *K"reiH;- ‘to buy, purchase’ = LIV: 395 f. | Pok.: 648 

*IE COGNATES: Gr. лріосӨол ‘to strike a bargain’, (Myc.) qi-ri-ja-to ‘he bought’, 
Olrish crenaid, Toch. B käry-, kär-nä-sk-, ORuss. krsnuti, krenuti ‘to buy’, OLith. 
krienas (m.) ‘purchase price’ 

*REFERENCES: Horn 1893: 106 f.; KPF I: 137, 207b, 244a; Ivanow 1926: 420; IIFL I: 409b; Christensen, 
Contributions I: 63, 157, 257; Abrahamian 1936: 130; Lambton 1938: 41b, 77b; Abaev, Slovar’ I: 73;
```


## [2026-09-06T22:37:01.448Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SOD xr'yn ===\"\ngrep -n \"xr’yn\\|xr'yn\\|xryn\" SOD_pages.txt | head -20\necho \"=== SOD xsp night ===\"\ngrep -n \"’xsp\\|'xsp\\|xs’m\\|xs'm\" SOD_pages.txt | head -20"
}
```


### [2026-09-06T22:37:01.518Z] TOOL RESULT

```
=== SOD xr'yn ===
15720:     xarin (yryn-?) ©Skt. krinati =*xryn-
15726:     xarlne ©<*xrinene ©pres. part. =»xryny                     BSTBL, Dhu. 77, 174, Dhy. 361; TSP 2.83, 1112,
15737:     xarit ©pt. st. ^yr'yn-, xryn-, yr'ycCh)                     Intox. 8; Yrp'kK TSP 2, 714; Yrpyk\ TSP
26804:8003 ptxryn- C                         o^J'^JJ'^J'^
26805:     patx(a)rin ©<*pati-xrin       ©impf. ptyxryn                     Anc. Lett. 5.5, 30, 3sg. subj. ptxwstH "will have
27044:8092 ptyxryn- C                                                            GMS 475, 1637; 622; VJ 2b; TSP 21.17; BBB f83;
27046:     patixrin ©impf. =»ptxryn-
34501:         ' Tedesco. ZII 2.35f; BBB 531; GMS 603, 848; STi      10642 xryny C                              ** <« jUT < ju^ jO
34561:10641 xryn- S, C                                       ^_J^          STi 63.8, 84.7; STii 3.16, 37, 48, 5.10, 12, 21, 28;
=== SOD xsp night ===
5789: 712 >Ys,m    S(MD)=» xs'm                                         lamentation, crying
5860:     (o)xsap <§)<*xsapa ©f.n. -h, ob. -yh ^'xsp-,                                                            -I ioJjU^S iali-
11742:       -^PrtVx                                                     2796 brxs'mnty                               v^   \*jIjuL*
13228:3314 exs'm     M       :j^)(jj^^      <^L~ <h jt <f)f±>- ^jjh
34540:                                                                     xs'm M, C                      '^jnj£j&
34551:10640 xrycyq                                                   10650 xs'm xwrnyy M                            ^i^lip^li
34956:    10773 xwrynyy        M                cjjj^- <0->j>^- J^- >>         xwas-amande ©ace. -tw ^wxs'mnty
35978:11100 yxs'mnty C                                    j*}jm            GMS 121, 245, 976; Sogdica. 35.8; Hen. Texts.
35979:      yaxsamande ©ace. yxs'mntw
```


## [2026-09-06T22:37:03.502Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BQT v2 leaf 200 (p.743) خریدن ===\"\ngrep -n \"خریدن\" BQT_v2_pages.txt | head -20\necho \"=== which leaf ===\"\npython3 - <<'EOF'\nd=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(len(d))\nfor i,p in enumerate(d):\n    if 'خرید' in p and 190<i<215:\n        print('LEAF',i, p[:80].replace('\\n',' '))\nEOF"
}
```


### [2026-09-06T22:37:05.400Z] TOOL RESULT

```
=== BQT v2 leaf 200 (p.743) خریدن ===
11831:  ‫‪ ۸‬رك ‪:‬خنده رش‪-.‬‬               ‫‪ - ۲‬اسم‌مفعولاز «خریدن»‪.‬‬                        ‫« المعجم شمس قيس ص ‪.*۱۳۳‬‬
11845:  ‫دیوتکی ‪ ۸۶۱‬از ‪ :‬خری ‪٣‬‏ دن (یسوند مصدری ) ‪ .‬جزو اول درساتسکرت ‪۲K‬‏ ( خریدن )‬
27785:                                       ‫خریدن باشث ‪.‬‬
=== which leaf ===
684
LEAF 201   ‫خرش‬
```


## [2026-09-06T22:37:11.494Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\ntxt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\nlines=txt.split('\\n')\n# find leaf of line 11845 (1-based)\nfor target in (11831,11845):\n    upto='\\n'.join(lines[:target])\n    print('line',target,'-> leaf', upto.count('\\f'))\npages=txt.split('\\f')\nfor i in (198,199,200,201,202):\n    p=pages[i]\n    print('=== LEAF',i,'===')\n    print(p[:1500])\nEOF"
}
```


### [2026-09-06T22:37:13.457Z] TOOL RESULT

```
line 11831 -> leaf 201
line 11845 -> leaf 201
=== LEAF 198 ===
                                                                                           ‫خر لوب‬

 ‫قوت باصره دهد وحافظه را زیاده کند ‪ -‬وبکر‬            ‫و قلیا سازند ‪٩‬‏ ؛ و بایمعنی بجای حرف دویم‬
‫اول مخفف خیرو است و آکنلی باشدکهآ نرا‬               ‫زای قطه دار همآمده _وخشتکاری اطراف باعحه‬

 ‫خبازی گوبند ؛ و باینمعنی ضم‌اول گهفمته‌اند‬                        ‫کونارصفه وابوانرا نگیوزبند ‪. ۴‬‬
 ‫نند کی جانورانرا نافع است و بعربی‬
                                 ‫آز‬
                                  ‫تخم گ‬             ‫خر نوب ‪ » ۴‬بر وزن مرغوب » چند‬
‫بذرالخرو خوانند ‪ -‬و بکر اول وسکون نانی‪,‬‬             ‫قم میباشد ‪ :‬لبطی و شامی و هندی ‪ .‬نبعلی را‬
   ‫ن‬
   ‫گلقیسر‬
        ‫بزبان بسضی اعزربان » بمعنی مط‬              ‫بفارسی کبر خوانند وآن رستنیی باشد خاردار که‬
 ‫باشد همچو خروالدبك که سر کین خروی است‬              ‫پرورده کنند و خورند و آنرا کور نیز گوند‬

 ‫نه نپند نافع باشد‪.‬‬
                  ‫ویاسگك‬
                       ‫بدک‬
                         ‫دگزن‬
                            ‫وآترا بر‬                                          ‫وبعربی‌بنبوت وقضم (‪)۱‬‬
  ‫وخروالفارکه سرگین موش امت » چون‬                                             ‫فرش‌خوانند "وشامیر |‬
 ‫بر داءالثعلب طلا کنتد سودمند بود » همچنین‬                                    ‫بفارسی کورزه )‪ (۱‬و‬
 ‫‪.‬ویند‬
     ‫کرین کرگك باشد ک‬
                    ‫خروالذئب که س‬                                              ‫بشیرازی کورلكکازرونی‬
‫اکر قدری ( ‪ ) ۲‬از آن بر ریسمانی که از‬      
=== LEAF 199 ===
 ‫خروك‬                                                                                                                        ‫‪۷‬‬    ‫‪۱‬‬


                                                     ‫لگیوزبند ‪.‬‬        ‫خرودان = با زای هوز بر وزن‬
‫‪ -‬بضم اول وفتح رابم» بمعنی‬                   ‫ورسه‬
                                                ‫ج‬                                     ‫خروشان » پهلوانی بوده ازتورانبان ‪3.‬‬

‫دویم خروسك است که پارژ گوشت ميان فرح‬                                   ‫خر وسان طاوس دم د کنابه‬
‫زنان ‪ -‬ویوست يار مرن کرمردان باشد وبربدن‬                                                            ‫از صراحیهای شراب باشد ‪.‬‬
                                 ‫آها (‪ )۱‬سنت‌است ؟ ‪.‬‬
                                                                       ‫خروسكت ‪ -‬بنالك مجپول ‪ ۰‬صفیر‬
‫‪ = ۴‬نم اول و ثانی وسکون‬                      ‫خروش‬                      ‫خروی است ‪ -‬و نام جانوری است سرخ رنگه‬
‫‪,‬گه و فرباد‬
          ‫ان‬‫الث مجهول وشین قرشت (ب‪)۲‬‬                                   ‫وییشتر درحمامپا بهم میر سد ‪ -‬گوشت باره‌ای را‬
‫باگربه باشد‪ -‬وبانگه بی گربه رایز کویند؟ ‪۶#‬‬                             ‫نیزگوبند که فر دهن فرح زنان میباشد و آبرا‬

‫خروك = بفتح‌اول وثانی بواو رسیده‬                                      ‫بزر که‬           ‫وسك‬
                                                                                         ‫خیرکه‬
                                                                                             ‫» 
=== LEAF 200 ===
   ‫ره‬      ‫سل‬                                                                                         ‫خروه‬

 ‫فقیرآنرا با خرما بکوبند وبخوردد ؛ بواینمعتی‬         ‫والث مجهول بر‬
                                                                 ‫‪ -‬نم اول ث‬                  ‫خروه‬
‫باتشدید(‪)۲‬ثانی همآمدمو(‪ ۳)۱‬نچه‌از کنجد باشد‬          ‫وزن گروه » بمعنی خروس است که بعربی دبك‬
                                                                 ‫خوالند ‪ -‬وتاج خروس را گیفزته‌اند ‪.‬‬
 ‫و بعربی‬    ‫وآنچه از بيد انجیر نود خرء بدانجر‬
                                                     ‫خرو هك = با ها بروزن خروسك ‪۰‬‬
 ‫کب‌الخروع گوبند ‪ -‬و بفتح اول و ضم الی‬
 ‫و اظهار ها » بمعتی نور باشد مطلفاًاعمازپرتو‬
                                                          ‫بمعنی بسداست که بعربی مرجان گویند ‪. ۴‬‬
 ‫چراغ وآش وآفتاب ؛ وعصنیی باینمعنی ْم اول‬            ‫بضم اول بر وزن گروهه ‪.‬‬               ‫خر و هه‬
 ‫داهج کي و اقا هاکر ا چنانجه گوبند‬                   ‫شپتار میان‌فرج زنان‌باشد‪ - ۴‬وجانوری را‬
                                                     ‫ادان بکرنار دام بندند تا جانوران‬                 ‫ا‬
 ‫برخاق‬     ‫خره نوراست از اند تمالی که قامز مود‬
                                                      ‫‪۸‬‬        ‫عربی‬
                                                                  ‫دیگر فرب خورده در دام افثند و‬
‫رباست بعضی بربعضی کنند‬           ‫خانل ناوریق‬
                                           ‫و بد‬                                              
=== LEAF 201 ===
  ‫خرش‬                                                                                                 ‫سم پات‬

 ‫و بمعنی شوم ونحس و نامبارك همآمده است‬               ‫جانور کی است که‌هرچه‌برزمین افتدبخوردوبعربی‬
                ‫وابوان وصفه را گنفزتەاند ‪.‬‬          ‫وبن دکه‬
                                                          ‫‪-‬علتی را دگیز‬
                                                                      ‫اورا ارضه خوانند ‪٩‬‏ و‬
 ‫خربدار گیر ‪ -‬کنابه ازچیزی‌است‬                           ‫موی را بریزاند ‪٩‬‏ ‪ -‬و مرضی است کهوشت‬
 ‫آرا‬‫که آ رارواجی باشد وزود فروخته شود و‬              ‫اب وبینی را بتحلیل برد ‪ -‬ویضم‌اول وفتح‌ثالی‬
 ‫بنعارفبقیه‌خوانند وقیضآ اراکاسدہ کو نی ‌‪.‬‬           ‫باتشدید‪ .‬صدا وآوازی باشد که بسبب گلوفشردن‬
 ‫خریدہ ‪ - ۷‬بفتح اولبر وزن درس‬                            ‫م‬
                                                         ‫‪-‬و‬‫اوزخکولوابیدن از یی مردم برآید بض‬
              ‫معروف است که بیع شده باشد ‪-‬‬
                                                    ‫اول و انی و اظهار ها‪ .‬مضفف خروه است که‬
‫و کنیزكد به‬

                ‫لارسیده رایز گویند ‪۲‬‬     ‫ردختسر‬      ‫خروی بائد ‪ - ۴‬و جالوران وحشی را نیز‬
                                                                                   ‫گوشد ‪.‬‬
 ‫ور‌تالی‌وسکون‬
             ‫خر لش ‪ -‬بفتح اول کس‬
                                                    ‫از پنج‬          ‫بکحصه‬        ‫=‬     ‫حرة ار دشر‬
‫است ‪۰‬‬    ‫تحتالی و شن فرشت‪ .‬مخفف‌خنده رش‬

 ‫وآن کی بائد
=== LEAF 202 ===
                                              ‫ان هشتم‬
              ‫بر شانزده لفت‬            ‫نقطه دار مشتما‪5‬‬           ‫در خای نقطه دار ‪ ۳‬رای‬


‫شتم باشد از شهر بور‬   ‫ست ازسال ملکی ونام روزه‬               ‫حز ‪ -‬بفتح اول و سکون انی » بلندی‬
‫بنا برفاعده‬     ‫‪۳‬‬‫ماه قدم وان روز حشن مغان‬                   ‫بیرون رانرا ‪ - 73‬ویمعنی نشسته براه رفتن‬
‫چون نام‬       ‫کلبه که مبان ابشان معمول استکه‬                ‫هم هت چنانکه طفلان روند ‪ - ۱‬و با تشدید‬
‫ماه وروز موافق آید جشن کنند ‪ ۰‬وبعضی گوبند‬                    ‫تافی » در عربی جانوریست معروف که از پوست‬
‫نام‌روز هیجدهم است ازشهر بورماه وعضی نام روز‬                                              ‫أن بوستین سازند؟ ‪-‬‬
‫گسفیتمداندانه(‪ )۱‬اعل‪٩‬‏ ‪ -‬وفصلی‌استاز فصول‬                                                 ‫وجامةٌ ایریشمی را نیز‬
                                                                                                   ‫کفته اند ‪. ۴‬‬
‫وبعربی‌خرردف گویند ‪ -‬ویمعنی خزیدن‬              ‫ار‬
‫مبنجیاببیهس‌تدگریرفتن‌هم‌هست ‪ - ۷‬وزردشدن‬                                                ‫ازها؟ ہے بر‬
                                                                                                  ‫خ‬
                      ‫برکف درخت را نگیوزیند ‪.‬‬                                              ‫خیری‬     ‫وزن قواها ‪.‬‬
                                                                                          ‫صحرابی است » وآن‬
‫خزدو ك ‪ - 4‬با دال ایجد بر وزن‬
```


## [2026-09-06T22:37:21.943Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\ntxt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=txt.split('\\f')\nprint(pages[201][1200:])\nEOF"
}
```


### [2026-09-06T22:37:23.583Z] TOOL RESULT

```
                                                                   ‫گوشد ‪.‬‬
 ‫ور‌تالی‌وسکون‬
             ‫خر لش ‪ -‬بفتح اول کس‬
                                                    ‫از پنج‬          ‫بکحصه‬        ‫=‬     ‫حرة ار دشر‬
‫است ‪۰‬‬    ‫تحتالی و شن فرشت‪ .‬مخفف‌خنده رش‬

 ‫وآن کی بائد که از روی تمسخر واستهزاء پرو‬            ‫حصهٌ فاری است ‪» ۴‬ونام‌شرری نبیوزده ازبناهای‬
 ‫خنده کنند‪ - ۸‬وخنده‌ای‌رایز کوبن دکه لزروی‬           ‫اردشیر که بهمن من اسفندبار باشد ؛ وباینعنی‬
                                                                                     ‫با تشدید ثالی هم گفتماند ‪۰‬‬
 ‫تمخر وآستهزا‪ :‬وفوی نود ‪ -‬وبائاكك مجهول‬
‫بمعنی خراش باشد که اخزراشیدن است یستی‬                    ‫نی و فاتحلك‬
                                                                   ‫اول‬
                                                                     ‫وما‬
                                                                       ‫خهراث‪ -‬من‬
‫يوست از بدن برداعتن ‪٩‬‏ ‪ -‬وامر باشمعتی حم‬
                                                     ‫و سکون‌کاف » مخفف خروهك است که ممه‌نی‬
 ‫هست بعنی بخراش وپوست ازاندامش بکن ‪٩‬‏ ‪-‬‬                                     ‫مرجان باشد ‪#. ۴‬‬
 ‫وبکراول؛ کدبانو وخانون خانه رااگویشد ‪۶٩-‬‏‬           ‫خری س بکسراول والیبتحتانی کشیده‬
                ‫وضم اول بمعنی پادشاه و‬
‫ربکزه کودخدا باشد‬                                    ‫مخفف خبری است‪ .‬و آن‌کلی باشد زردرنگ‬
               ‫کودیانو را کنفزته‌اند *‪4 .۱‬‬           ‫پربر که‌میان سیاه نورآاهمیشه بهارنیز گوینده ‏‬
                            ‫‪.‬‬   ‫‪:‬آردشی‬       ‫» چش‬   ‫چك‬    ‫(‪)۲‬‬           ‫می ‪.‬‬          ‫‪+‬‬   ‫‪:‬‬   ‫چش‬    ‫(‪)۱‬‬


  ‫« این کورة اردشبر‬   ‫‪۴‬‬           ‫‪.‬‬   ‫خروی‬    ‫رکک‪:‬خروه»‬        ‫‪۴‬‬                 ‫رک‪ :‬خوره ‪.‬‬           ‫‪۱‬‬

   ‫خوره‌منسوست باردشیربن بابك ومبداً بعمارت فیروزآباکدردست‪.‬؟ «فارسنامهٌان‌البلخی‪۲۳۱‬ممد»‪.‬‬
   ‫‪ «۱ ۱‬همجتانك زنساحب‬                   ‫رك ‪ :‬خیری ‪.‬‬           ‫‪۵‬‬            ‫‪.‬‬        ‫؟خ‏رركو‪:‬حك‬
  ‫جمال دربعضی ملابی خوبتر تماید وکنیزك بیش بها در بضی معارض خربدار گیرتر آید ‪> ...‬‬
  ‫‪ ۸‬رك ‪:‬خنده رش‪-.‬‬               ‫‪ - ۲‬اسم‌مفعولاز «خریدن»‪.‬‬                        ‫« المعجم شمس قيس ص ‪.*۱۳۳‬‬
  ‫«‪۲۲‬خر‪:‬یش بعنی پوستش از اندام بناخن بازگیر‪.‎‬‬
                                            ‫‪ - ٩‬اسدی گوبد « لفت فری ‪۲۰‬‬
                                                                                                   ‫خسرو ی کف‪: ‎‬‬
  ‫جهاا بافتی کامت کنون زین بیش مخرمشم‪.* ‎‬‬                ‫جپان برشبه داود است ومن چون اورباکشتم‪.‬‬
  ‫بست دیگری که اسدی از فر دوسی‌آورده (و درآن خرهبشینه آ مده) یداست‬                        ‫و‬   ‫ازین طت‬
        ‫‪ °‬مصحف فخدیش» («‪.‬م‪۲ ).‬‬                      ‫شیدن است ‪ ,‬لفتی درخراشدن ‪.‬‬
                                                                             ‫بر‬‫که مصدر خ‬
                                                           ‫‪.‬‬       ‫‪:‬وره‬
                                                                      ‫* خرة کیالی ‪ -‬رکه خ‬
  ‫طابنعکاربا ‪» ۷۲۲‬‬        ‫د‪0‬ه«ش‪.‬‬
                               ‫ن‪72‬‬
                                 ‫ب‪011‬‬
                                    ‫* خرهدن ‪ -‬فتح اول و چپارم ‪ .‬پهلوی ‪21‬‬
  ‫دیوتکی ‪ ۸۶۱‬از ‪ :‬خری ‪٣‬‏ دن (یسوند مصدری ) ‪ .‬جزو اول درساتسکرت ‪۲K‬‏ ( خریدن )‬
   ‫«هوبشمان ‪ « > ۲۸4‬افا ‪ :‬اس ‪ ۱۲۰‬کردی ‪ « 81161‬اسفا اضاً » ‪ ,‬طبری ‪2071711521‬‬
                ‫(میخرم) «واژه نامه ‪۸۱۳٩+‬‏ ستدن چیزیبا برداختن‌بهای آن» مقابل‪:‬فروختن ‪.‬‬
                                                           ‫‪ #‬خحریشیلی ‪ -‬رکه ‪ :‬خرش ‪.‬‬
```


## [2026-09-06T22:37:38.143Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\ntxt=open('SOD_pages.txt',encoding='utf-8',errors='replace').read()\nlines=txt.split('\\n')\nfor t in (15720,5860,34561,34540,13228):\n    print('line',t,'-> leaf',('\\n'.join(lines[:t])).count('\\f'),'~printed p.',('\\n'.join(lines[:t])).count('\\f')-66)\nprint('----context 15715-15740----')\nprint('\\n'.join(lines[15712:15742]))\nprint('----context 5850-5870----')\nprint('\\n'.join(lines[5850:5872]))\nprint('----context 34550-34575----')\nprint('\\n'.join(lines[34535:34575]))\nEOF"
}
```


### [2026-09-06T22:37:40.095Z] TOOL RESULT

```
line 15720 -> leaf 232 ~printed p. 166
line 5860 -> leaf 94 ~printed p. 28
line 34561 -> leaf 499 ~printed p. 433
line 34540 -> leaf 499 ~printed p. 433
line 13228 -> leaf 196 ~printed p. 130
----context 15715-15740----
        Yirek ©ob. -yh; -y\ -y    =*yryk, yr*y                  (ro)know, GcOunderstand, (to)take
      mud, clay, muddy
                                                                GMS 485; AVS 108; YrSfi}<Yrfl-6y 2pl. impv.
     SCE 160; TSP 2.275; BSTBL, Vim. 0,28; Yryyk>                 TSP 2.676; Hen. Textes. YrSf
       yYsyfitk, "mud-milky" Vim. 25                      4206 yrb-    C => yrp-
4197 yr>yn- B, S                               0-b>
                                                          4207 yrpwk     B =» yrp>k
     xarin (yryn-?) ©Skt. krinati =*xryn-
     (to)buy                                              4208 yrp^ky' B =* yrp'ky'
      VJ 1319; TSP 2.230 & etc.; MDii A-5, 24, B-         4209 yrp* B                             S >> <^>lf 7 <jxh
        8R6; Bailey. Prolexis. 69; AVS 97                       yarpa, yor|3a (yrph) ©f. n. =»yrp'k
                                                                understanding, knowledge
4198 yr>yn,k B                              >_>
     xarlne ©<*xrinene ©pres. part. =»xryny                     BSTBL, Dhu. 77, 174, Dhy. 361; TSP 2.83, 1112,
     buyer, purchaser                                             6.41, 63
     TSP 2.775; GMS 475, 895                              4210 YrPJk B, M, S                  (jy >ui* j>)jt\ <Ub
4199 yr>ynt(n) B                                               yarPak, yorPak (yrb'q) ©ace. -w, pi. -?-, ob. pi.
                                               ^>
     yarind ? ©Khot. gran-; MP grn'g; BaL gar and                -ty ^mntyrP'k, yrP*
                                                               wise, intelligent
     roar ing ^yryn-1
       ©pp.                                                    GMS 989, 1237; BSTBL; TSP; BBB; Frag. Len.;
     TSP 13.21; Benv. JA 1955, 301; S W, IIJ 1976, 60            STi 40.1, 43.15, 6.8; Sund. AoFviii 1981 p215;
4200 yr>yt- B                                    0x>             BSTi 202; C2 gloss. xrfii(% STii 10.53; BSTBL,
     xarit ©pt. st. ^yr'yn-, xryn-, yr'ycCh)                     Intox. 8; Yrp'kK TSP 2, 714; Yrpyk\ TSP
 yrb'q

           2.1068; Yrfi'kw, Hen. Tales. 480.1; MSP b 130;     4224 yrpV        S =* yrPy
           YrjPku YrVqu TSP 8.24; Tales. 467.60; BBB          4225 yrpV B                        «wf 7 ij>€ 7 <o^j
           f90; STii 4.42, 10.5; STi 6.8; C2 gloss.                yarPaw, yarP(a)u ©n. adv. prcs. inf.
----context 5850-5870----
 735 >Ysnyrkc,) B                                       uUj
       (o)xsnirk ? Oysnyrkh) =^xsnyrk(>1                           VJ 6a, 1029; BBB plOl; Tales. 486.22; GMS 243
       mark, target                                            747 >ysyptk B, S                               ^
       GMS 976 nl; TSP 7.198, 22.7; BSTBL, Dhy.                    (o)xsi(3de OysyPty) ©Yaghn. xsift-, Khwar.
         85(N), 154, 224, 333; -\ Dhy. 226; pi. -tt Dhy.             xwflcy =>xsyPt
         371; -w, Karab. Insc. 19.7; -h, VV-Li 71                  milky, milk
 736 'ysnyrkh S => >Ysnyrk(,)                                     BSTBL, Vim. 25; VJ 6", 1029; BBB plOl cl8
 737 >Ysp- B,S                                    ^           748 >ysypty =» 'ysyptk
                                                              749 »Ysy8 S
     (o)xsap <§)<*xsapa ©f.n. -h, ob. -yh ^'xsp-,                                                            -I ioJjU^S iali-
                                                                   axse5 =^xsy5, ys'yS, xsy5
       night                                                       king, commander
               ()) TSP; BSTBL; SCE; MDii; Frag. Len.;
       GMS xsp157;                                                 Hen. Talcs. 481.31; W-Li
         Frag. 2a. 11            ?                            750 'ysywn =» ^sy'wn, 'ys^ywn
 738 'yspck => 'yspcykk                                       751 'ysywn'k B, S
                                                                                                           —j -J i J3j~* ie\~-

 739 'yspcykk S                            aL^JL^^                 (o)xscwane Oysywn'y, 'ysywnk) ©pi. -}yf; ob.
     (o)xsapcik Oyspck)                                              pi. ->y/y =*Pyy *ysywny, 'xsywnCy), 'ysywny,
     black stone, agate
     MDiii 74 n4; MDii pl43.8; Frag. 2a.ll                           ,ys,ywn>k,
----context 34550-34575----
10637 xryc M                                             x>          C2, 60R24; trans, pret. xsd>r-% BSTi 250; Gersh.
                                                                       JRAS 1946, 183
         xaric ©<*xritl ^yr'ycdi)
         purchase                                              10648 evening
                                                                     xs'm M, C                      '^jnj£j&
         BBB 567; Tales. 470.56                                      xsam Cysto) ©Av. xsafnya\ ParthJam
10638 xrycq => xrycyq
                                                                     STi 81.7; GMST313
10639 xrycqy> C                                  *}<*S^jj
      xarickya                                                 10649 x^m xwr-      C                              a>j^-f^
      adultery                                                       xsam xur

         STi 4.8; AoFi 230.8; "purchasable" AoFviii                  (fo)have dinner
           1981, 219                                                 Sund. AoFviii 1981, 23V 6 pl86

10640 xrycyq                                                   10650 xs'm xwrnyy M                            ^i^lip^li
                   C                       .AiOj^jj                  xsam-xurne
         xaricik, xarick (xrycq) =*yTyyck}
                                                                     supper
         prostitute, whore                                           GMS 911
         GMS 976; STi 19.9, 12; C2, 48V18; ob. pi.
                                                               10651 xs'wn     C                           ojjS^J^U^
           xrycyqty, C2, 102V25; BSTii 83125; S W, C2
                                                                     xsawan, xson ^'xsWn
        n pl77, 178; +sm>ryty, adj. "lewd"                           power, rule, authority
10641 xryn- S, C                                       ^_J^          STi 63.8, 84.7; STii 3.16, 37, 48, 5.10, 12, 21, 28;
         xarin ^yr'yn-                                                 BSTi 267; C2 gloss.
         (to)buy, (repurchase
                                                                                                                  xsywny(y)
433


10652 xs>wnd>r C                                    \3J*j             rule, realm
      xsondar ? (xs'wnS'r) ©ob. -y; pi. -/                            STii 1.43; GMS 132
        ^xs'wnS'r                                              10666 xswny C                                     jlLaL-Jj^U^
      ruler                                                          xsswane,
                                                                     ruler, kingxsewane
       C2 gloss. p232, ob. -y, 102R28, pi. -f, 26 R4-5;
         BSTii B27.55, 829.28; CII 1990 G3                            STii 1.17, 18, 3.9; GMS 132, 1086
10653 xs'wne'r    S =» xs>wnd)r
```


## [2026-09-06T22:37:53.382Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\ntxt=open('HRN.txt',encoding='utf-8',errors='replace').read()\npages=txt.split('\\f')\nprint(\"### HRN leaf 190 (printed 169) ###\")\nprint(pages[190][:2500])\nEOF"
}
```


## [2026-09-06T22:37:54.691Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\ntxt=open('SYN.txt',encoding='utf-8',errors='replace').read()\npages=txt.split('\\f')\nfor pr in (817,992):\n    leaf=pr+24\n    print(\"###### SYN printed\",pr,\"leaf\",leaf,\"######\")\n    print(pages[leaf][:2200])\nEOF"
}
```


### [2026-09-06T22:37:55.458Z] TOOL RESULT

```
### HRN leaf 190 (printed 169) ###
— 169 —
Stützhülz (am Joch)'); arm. .sami\/v 'Stirnliolz des
Ochsenjoches (de Lagarde, No. 19:^8) i).
Xp. sim *Silber , sitnm 'silbern' (phlv. usltn, astnnn)
dagegen ist bekanntlich griechisches Lehnwort (vergl.
zuletzt Nöldeke, Pers. Stud. II, 45).
765. sl/inury 'Greif, Adler; N. pr.', vergl. STn\duxt,
aw. saenö mereyö- *Adler' ; phlv. stnmuro, seiw murük
(Yätkrtr-r Zar. S. ()4).
ai. ^ijefui' Talke*; arm. ein milvus (H. No. 280).
S,
766. Süx 'Zweig, Ast; Hörn (des Stieres), Greweih'.
ai. rdkhä' 'Zw^eig, Ast*; phlv. säk (West 111, 118
Note 1), natak]sak (Bund.) d. i. säx; arm. cu/ (H.
No. 279); lit. szakfi.
LW. kurd. säy; aty. ^ä/; bei. mh 'Hörn, afrt/ 'Ast*;
wa;K. soZ/, sar. so^ 'Zweig', wa;!r. mo, sar. xdo 'Geweih'.
Vergl. zuletzt Bartholomae, Studien II, 41 folgg.
767. Häd 'fröhlich, heiter , sadt,
ap. siyäti- 'Behagen, Freude*^); aw. säiti-; phlv. sät,
sätlh; lat. vergl. quietus, quies.
088. äncad 'Stille', d. ancayim, t. ancain *ruhen* (24).
768. Hiiiu 'Abendmahlzeit, Nachtessen*.
aw. x^^f^W^'"'» phlv. säm (y. 61 (19) = 62, 7).
LW. kurd. säm *Abend'; af;^. süme Zeit zwischen
Mitternacht und Tagesanbruch; Nachtessen, Leichen-
schmaus', mä\xäm 'Abend' (?); bei. säm 'Hauptmahlzeit,
Abendessen* (259); sar. /?/w, yidg. säm.
') Nichts wesentlich Neues bringt Bugge, KZ. H2, 24.
Als Betonung von aw. simä" muss natürlich oxytonale angenommen
werden. Das Wort ist mit den von Bartholomae, BB. XVII, 114 folg.
gesammelten zusammen zu beurtheilen.
*) Und wohl auch zugleich *Wohnstätte*, vergl. Bartholomae,
Arische Forschungen, II, 102.
```


### [2026-09-06T22:37:57.005Z] TOOL RESULT

```
###### SYN printed 817 leaf 841 ######
�� (9.65) reg. renders also Grk. apybpiov as ‘money’.
SCr. novac ‘coin, money’, esp. in lat- ter sense pl. novet, fr. nov ‘new’, orig. re- ferring to the ‘new coinage’ as contrasted to the old, then extended. Rjetnik Akad. 8.243 f.
Boh. penize, Pol. pieniadze : ChSI. pénezi ‘denarius’, fr. the Gmc., see above, 4.
Russ. den’gi, pl. of den’ga ‘a copper coin’ (> Pol. dziega), loanword fr. a widespread oriental group of terms for ‘money’ or various coins, as Kasan. tenk’e, Kirg. tenge, etc. Berneker 183 f. Lokotsch 478.
7. Several of the Skt. words for ‘prop- erty’ or ‘wealth’ are sometimes rendered ‘money’, most commonly dhana- (11.41), but evidence of actual money is late. For early substitutes, see Zimmer, AJ- tind. Leben 259.
Av. §aéta- ‘wealth’ (11.42) is in certain passages rendered ‘Geld’ by Bartholo- mae and ‘argent’ (also ‘trésor’) by Dar- mesteter, but there is no certain refer- ence to actual money in the Avesta, and the payments enumerated in Vd. 7.41 ff. are in terms of domestic animals.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
rip D mynt ; v an. ramus (mone) Sw. nut moncla OE monnate ME J * moneda NE coin » moneda, ban Du.  munt
jon, piosa MHG miinze bath NHG miinze
fc, vopones orig. ‘anything uae ‘ thy custom’, then esp. Oe lega var) rei’ deriv. of vouifw practice tel
’ (21.11). gs custom’ : vOHOS ‘custom, law’ (
Walde-P. 2.330 f. 9, Lat. nummus, prob, an early loan- mond fr, Grk. vdziyos ‘customary, “a ail:vbwzs, ete, (above). Sicil. Grk. votyyos would then be in turn fr. the Italic form. Ernout-M. 686 f. late Lat. monéla, orig. a surname of Juno, then the temple where she was yorshiped and where money was coined, hence ‘place of coinage, mint’, in later use also the ‘die or stamp for coining’ and esp. the ‘coin’ itself. Hence the com- mon European words, It. moneta, Fr. nonnaie (> Br. moneiz, ME moneye), ets Rum. monedd; OE mynet, “a me MLG munt (> late ON, muniza pee : Due punt OBG a a NHG miinze (> i Pol. Russ, moneta. Er-
Nout-M, ker 2.76, oa. Falk-Torp 745. Berne-
Rum, 4
,.  ¥4n, N
###### SYN printed 992 leaf 1016 ######
; | at ited types with suffix -to- or
H Falde?. 1.753. Brugmann, Grd. dio |
99.53 ip. Gtk. rplros, Toch. A trit. _ is Lat. tertius (> It. terzo, ae etc.); W- iryddydd, Br. trede; i “ii etc. general Gmce.; Lith. a Lett. tresars (OPruss. tirtis, but oe ); ChSl. éretiz, etc., general
so lirts an Skt irltya-, Av. Orilya-, OPers.
pritiya-.
9, Ir. tiers, Sp. tercio (fr. Lat. tertius)
were specialized to ‘a third’ (fraction), the former replaced by trotsiéme, with the same new formation as the other or- dinals (orig.? Meyer-Liibke, rz. Gram. 2.177); the latter by tercero, like Ofr. lercier, fr. Lat. terliarius (cf. Sp. primero, Fr. premier fr. Lat. primarius). Rum. al ireilea, fem. a treia, formed fr. the cardinal with preceding article and nom.-aee, sg. of the postpositive article. Tktin, Rum. Elementarbuch 97. ot Ir iris(s), tres, fr. *tristo- or Insli- in form like Lat. testis ‘witness’ - *erstis, *tristis, Walde-P. 1.753. i 2.185. Thurneysen, Gram. ... aie formed after Iv. an, ourth’, etc., with suffix ~m- Silat ae the ordinals for 7, 9, 10. Soe t. (rivet with suffix -eto- after et ‘fifth’, ete. Pedersen 2.135. 13.43. “A thirg?
Dressed by 9 ae (fraction) is often ex-
ene or phrase containin ae for ‘third’ and the word oe taken in c terms are so transparent, 18.49 ag peinection with 13.23 and Or the pote no further comment. ath ee 18 used alone, either in derstog ‘Ng with the word for part 8) op j as Lat. tertia beside tertia © neuter (or later inde-
QUANTITY AND NUMBER
igitized by Arya Samaj Foundation Chennai and eGangotri
943
clinable) form. Among such forms, Fr. tiers, Sp. tercio are now specialized to the fractional sense since their replacement as ordinals by troisiéme, tercero (13.42); and Skt. tfttya- neut. is distinguished by the accent from the ordinal trttya-.
There are also some derivs. formed with various suffixes from the ordinal or cardinal, as follows:
1. Lat. triéns, -ntis ‘a third’ in gen- eral, but esp. ‘a third of an as’, a particip- ial deriv. like quadrdns, sextdns, etc. Thurneysen, IF 39.201.
2. Rum. treime ‘trinity’ and ‘a third’, deriv. of the cardinal with suffix -ime fr. Lat. -tmen. Meyer-Liibke, Rom. Gram. 2.486.
3. Ir. trian, NIr. trian,
```


## [2026-09-06T22:38:07.519Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\ntxt=open('SYN.txt',encoding='utf-8',errors='replace').read()\npages=txt.split('\\f')\nimport re\nfor i,p in enumerate(pages):\n    if re.search(r'11\\.8[0-9]\\s+BUY|BUY\\b', p) and 'sell' in p.lower():\n        print('leaf',i, p[:200].replace('\\n',' '))\nprint('---night---')\nfor i,p in enumerate(pages):\n    if re.search(r'14\\.4[0-9]\\s+NIGHT|\\bNIGHT\\b', p) and ('nox' in p or 'xšap' in p or 'naktos' in p):\n        print('leaf',i, p[:200].replace('\\n',' '))\nEOF"
}
```


### [2026-09-06T22:38:09.519Z] TOOL RESULT

```
leaf 885 sneis, OHG asni ‘hireling’ (utcOwrés, Jn. 10.12, 18), OF esne ‘sery- ant’, root connection dub. Walde-P. 1.77, 161. Feist 59. NED s.v. earn, vb.1, OHG ferdiendn (Notker), irthionsn (Otfr.), MHG, NHG, 
---night---
leaf 1068  for ‘day’, | Gall. lat. (Calendar of Coligny) : ChSI. tainly those of the large inherited | léto ‘year, summer’ (14.73). Walde-P. ze denoted the -bright ‘day’ vs. | 2.427. Pedersen 1.133. Thurneysen,
```


## [2026-09-06T22:38:11.832Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\ntxt=open('SYN.txt',encoding='utf-8',errors='replace').read()\npages=txt.split('\\f')\nprint(\"### leaf 1068 ###\")\nprint(pages[1068][:3000])\nEOF"
}
```


### [2026-09-06T22:38:14.344Z] TOOL RESULT

```
### leaf 1068 ###
 for ‘day’, | Gall. lat. (Calendar of Coligny) : ChSI.
tainly those of the large inherited | léto ‘year, summer’ (14.73). Walde-P. ze denoted the -bright ‘day’ vs. | 2.427. Pedersen 1.133. Thurneysen, ie Kit and only secondarily (like ‘sum- | Gram..35, 180. Pokorny KZ 50.43 if ne ss ‘winters’ for ‘years’) the com- (taking lae as of different orig., but cf. wehensive 94-hour ‘day’ (for which | Vendryes, RC 42.234 f.). Dan., Sw. have distinctive forms). 4. Goth. dags, ON dagr, OE deg, 1. Derivs. of IE *dei- ‘shine’, rare in | OHG fag, etc. general Gmc. (also derivs. verbal forms (Skt. 3sg. imperf. adzdet, Goth. fidur-dogs ‘of four days’, OE dégor etc.), but widespread in words for ‘sky, | ‘day’, ON degr ‘12-hour period, day or heaven’ as Skt. nom. sg. dydus and the | night’, Dan. dégn, Sw. dygn (the last two personified Grk. Zebs, Lat. Iupiter, Iovis; denoting the 24-hour day), etym. dub., ‘god’ as Skt. deva-, Lat. deus, etc.; and | but perh. (despite phonetic difficulties ‘ay’. Walde-P. 1.772 ff. Ernout-M. | with the gutturals) : Lith. dagas ‘(sum- 268 ff. Walde-H. 1.350. Here as ‘day’. | mer-) heat’, OPruss. dagis ‘summer’, Skt. a) IE *dyeu-, *diw-, etc. nidagha- ‘heat, summer’, fr. the root Lat, digs (> It. di, OF r. di, Sp. dia, | *dheg*h- in Skt. dah-, Lith. degti, etc., Rum. zi); Ir, dia, die, W. dydd, Br. | ‘burn’, and also (with init. doublets, as deiz; Skt, diva- (in dive dive ‘day by day’, | Skt. agru-, Lith. asara : Grk. daxpu otherwise divasa-); Arm. tiw. Lat. deriv. | Goth. tagr ‘tear’, etc.), Skt. ahan-, Ay. adj. diurnus ‘of the day’, late sb. diur- | azan ‘day’. Walde-P. 1.849 f. Walde- mm > Fr. jour, Prov., Cat. jorn; It. | H. 1.467. Falk-Torp 183, 176. Feist ee vs. di perh. due to lit. influence | 113. ea or Fr. REW 2632, 2700.| 5- Skt. gat Caisse ae il ae 3.71f., 105f. Bonfante, | instr. sg. ahna, etc.), Av. se . Sg. “74 59.877 ff. (with refs.). asni, etc.), see above, 4, with reis. b) With nasal suffix. Av. ayan- (nom. sg. ayara, gen. 8g. aes Lett. diena; ChSl. dint, ete., | war ete., neut r/n stem. like Skt eral Slavies Skt. di in epds.): | 2a" above), prob. : Grk. fier ‘in the Me ed (eap. in epds.); ning’, Goth. air, ON ar, etc., ‘early’, » tre-denus ‘triduum’, Goth. sin- he eee z
leing ‘daily’ Goth. jer, Av. yara ‘year’, etc. Walde-P. 2. Grk. ane ; 113}. Dor, a ‘népa, Dor. dutpa, poet. Fuap, OPers. rauca (xSapava raucapativa
Toot a ‘ Arm. awr (*admor) ‘day’, | ‘either by night or by day’, 1 rauéa ‘one
329 “ction? Walde-P. 1.53. Boi- day’, etc.) : Av. raoéah- ‘light’, Skt. ruc- ae ‘shine’, Grk. devxds ‘bright’, Lat. lax “laithe, beside Iae, laa, NIr. Ia, | ‘light’, ete. Walde-P. 2.308 ff.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
H ;
Digitized by Arya Samaj Foundation Chennai and eGangotri
SELECTED INDO-EUROPEAN SYNONYMS
14.42 NIGHT Grk. vot Goth. nahis Lith. naktis ; NG voxra ON noatt Lett. nakts ; Lat. nox Dan. nat ChSl.  noStt i It. notte Sw. natt SCr. noé jj Fr. nuit OE nitht Boh. noc Ft Sp. noche ME night
```


## [2026-09-06T22:38:19.388Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\ntxt=open('SYN.txt',encoding='utf-8',errors='replace').read()\npages=txt.split('\\f')\np=pages[1069]\ni=p.find('NIGHT')\nprint(pages[1068][-500:])\nprint(\"=== leaf 1069 ===\")\nprint(p[:2500])\nEOF"
}
```


### [2026-09-06T22:38:21.414Z] TOOL RESULT

```
H ;
Digitized by Arya Samaj Foundation Chennai and eGangotri
SELECTED INDO-EUROPEAN SYNONYMS
14.42 NIGHT Grk. vot Goth. nahis Lith. naktis ; NG voxra ON noatt Lett. nakts ; Lat. nox Dan. nat ChSl.  noStt i It. notte Sw. natt SCr. noé jj Fr. nuit OE nitht Boh. noc Ft Sp. noche ME night Pol. noc Rum. noapte NE night Russ. not! i Ir. adatg (nocht) Du. nacht Skt. ratrz., ksap-, nakt- 8 NIr. _ oidhche OHG = naht Av. OPers, 2Sap- W. nos MHG naht Br. noz NHG nacht tl Most of the words for ‘night’ belo
=== leaf 1069 ===
ng general Slavic; Ved. nakt- (nom. Sg. nak, to an inherited group, pointing clearly | acc. sg. naktam), nakti- (class. Skt. only ( to an IE word for ‘night’. In Irish, ex- | adv. naktam ‘by night’, cf. Wackernagel, cept for an adv. relic, and in Indo- | Altind. Gram. 3.233 ff.); Alb. naté;— \ Iranian, except in Vedic and a classical | with e-grade Hitt. nekuz ‘evening’, : Skt. adv. relic, the old word was dis- | nekuzi ‘goes to bed’ (Sturtevant, Hitt, lL placed by others, but’ elsewhere has per- | Gloss. 108). i sisted as the usual word to the pres- 2. Ir. adaig, aidche, NIr. oidhche, ent day. etym. dub. Walde-P. 1.34. Walde-H. : 1. IE *nokt(t)-. Walde-P. 2.337 ff. | 1.61. Stokes 326. ( Ernout-M. 682. Sturtevant (connect- 3. Skt. rdtri- : Grk. Anr&, Dor. Aard ; ing this group and that for ‘naked’, | ‘Leto, mother of Apollo and Artemis’, : 4,99) JAOS 52.10, Hitt. Gram. 122 f, orig. personification of the night, perh. Grk. vit, vuerés, NG vixra (v prob. | fr. the root in Grk. \6w ‘be hidden’, fr. a reduced grade); Lat. nox, noctis | ete. Walde-P. 2.377. Boisacq 555. n (> Romance words); Ir. nocht (in in- | Uhlenbeck 248. Y nocht ‘tonight’), W. nos, Br. noz; Goth. Skt. ksap-, Av. xap-, rfapan-, xSapar-, Mi nahis, ON ndtt, etc., general Gmc.; Lith. | OPers. xsap- (Barth. 548 f.) : Grk. pédas, naktis, Lett. nakts; ChSl. nostt, etc., | pédos ‘darkness’. Walde-P. 1.524 f. h q ‘ 14.48 DAWN Grk. dus, Sp8pos Goth. : Lith. auSra, brékSta x NG aby}, xapépyara, ON — dagan, dagsbrin Lett. rita blazma, rila Xapavyy Dan.  dagning, daggry krésla, ausma D Lat. aurora, prima liz Sw.  dagning, gryning ChSl. rano(adv.), -brézgi, di It. alba, aurora OE degréd, degrima, zore (pl.) Fr. ube, aurore dagung SCr. ora, svanuce 1 Sp. alba, aurora ME  dawing, dawning, Boh.  svitdnt, risvit Rum. zori, auroré dayrawe, etc. Pol. Swit, brzask, zorza Tr. dedal NE dawn, daybreak Russ. zarja, razsvel i) Nir. fainne an lae Du. —dageraad Skt.  ugas-, aruna-, pra- D W. = gwawr OHG = morgenrot, -rata, bhata- i Br. goulou-deiz, tarz tagarat Ay. uSah-, astir- ! an deiz MHG morgenrét, -rale,
tagerat
NHG morgenrot, -réte, tagesanbruch, mor- gendimmerung
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
‘dawn’ denote strictly the unrise, but some of be extended to cover ‘sun- en (morning ’- ' They are most- juding the inherited group, con- Md with words meaning grow bright, pectee * ht’, or ‘white, gray, red’, or in with the word for ‘day’.
8 ‘ist before §
ry few cases i IE *ausos-, etc., fr
```


## [2026-09-06T22:38:32.730Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\ntxt=open('SYN.txt',encoding='utf-8',errors='replace').read()\npages=txt.split('\\f')\nfor i,p in enumerate(pages):\n    if 'BUY' in p and ('krinati' in p or 'kriṇāti' in p or 'xarīdan' in p or 'zaridan' in p or 'emo' in p):\n        print('leaf',i)\n        print(p[:2600])\n        print('~~~~')\nEOF"
}
```


### [2026-09-06T22:38:34.556Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T22:38:37.715Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"11\\.8[0-9] *BUY\\|BUY *Grk\\|11\\.83\" SYN.txt | head -20\necho \"---\"\ngrep -n \"krinati\\|kriṇāti\\|krīnāti\\|xaridan\\|xarīdan\" SYN.txt | head -20"
}
```


### [2026-09-06T22:38:37.777Z] TOOL RESULT

```
18738:11.83 Trav (vb.)
20825:11.81 BUY
20874:4. Lat. caupo ‘petty tradesman, huck- ster, tavern-keeper (Plautus), itself of unknown origin, is the probable, though not undisputed, source of the wide- spread Gmc. group of words for ‘trade, buy, sell, tradesman’, etc., whence also the Slavic verb for ‘buy’. Cf. the Gmc. loanwords based on Lat. mango ‘dealer, trader’ (11.83, 11.84). Ernout-M. 465 f. Walde-H. 1.189. Falk-Torp 521. Feist 309. Berneker 647. Stender-Petersen 374 ff.
20895:‘trade’ fr. ‘travel’ (above, 2 and 11.83, 11.84), more prob. a new act. (cf. Cret.
20900:11.83 TRADE (vb.)
20940:f the words for ‘merchant, It. commerciante, Fr. commercant, Sp., pee are connected with those for | Rum. comerciante, fr. It. commerciare, talemay, or ‘market place’, dis- | ete. ‘trade’ (11.83).
20944:a ean between éuaropos Oh, aan aa M. I. Finkelstein, be en merchant? (Plut.+, ‘edler’, fy small tradesman’ or . TParyHaTebopar ‘trade’ (11.83). (1ugy) | "74lor, fr. ‘mercart ‘trade’
20945:lat. neqaisn (11.83), me” ft. negotiari ‘trade’ through Bi Nee also Rum. negustor
20949:W. masnachydd, fr. masnachu ‘trade’ (11.83).
20952:4. ON kaupmadr, Dan. kgbmand, Sw. képman, OE céapman, ME chapman, Du. koopman, OHG, MHG koufman, NHG kaufmann, fr. ON kaupa, OE céa- pan, OHG koufen, etc. ‘trade’ (11.83), with words for ‘man’.
20953:Sw. handlare, NHG hédndler, fr. Sw. handla, NHG handeln ‘trade’ (11.83).
20955:NE trader, tradesman, fr. vb. trade (11.83).
20962:(11.83), and prekijas, fr. preké ‘mer- chandise’, both neologisms, given by NSB s.v. kupéius.
20964:Lett. tirguotajs, also tirguonis, fr. lirguot ‘trade’ (11.83).
20979:SCr. trgovac, Russ. torgovec, fr, SCr irgovati, Russ. torgovat' ‘trade’ (11.83), Boh. obchodntk, fr. obchoditi ‘trade (11.83).
20981:Lat. mercatus ‘trade’ and ‘market place’ (> It. mercato, Fr. marché, Sp. mercado) : mercari ‘trade’ (11.83). REW 5516.
34277:1. Grk. répyn : répynue ‘sell’ (11.83), hence the female slave sold for prostitu- tion. Walde-P. 2.40. Boisacq 805.
---
```


## [2026-09-06T22:38:41.253Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '20825,20880p' SYN.txt\necho \"=== leaf of line 20825 ===\"\npython3 -c \"\nlines=open('SYN.txt',encoding='utf-8',errors='replace').read().split('\\n')\nprint(('\\n'.join(lines[:20825])).count('\\f'))\n\""
}
```


### [2026-09-06T22:38:43.112Z] TOOL RESULT

```
11.81 BUY
c dvéopat, AOT- erprauny, aa &yopasw NG aryopaso Lat. mere It. comprare Fr. acheter
; comprar ae cumpara Ir. crenim, cennaigim NIr. ceannuighim W. prynu Br. prena Goth. bugjan ON  kaupa Dan. kj¢be Sw. képa OE bycgan ME i bugge NE buy, purchase Du.  koopen OHG koufen MHG koufen NHG kaufen Lith. pirktt Lett. pirkt ChSl. kupitt SCr. kupiti Boh. kupiti Pol. kupié Russ. kupit’ ae kri- (pan-)
Vv. :
Digitized by Arya Samaj Foundation Chennai and eGangotri
817
11.82 SELL
mwrkw, BOF. dredouny, perf. rémpapac
TrOVAa
vendere
vendere
vendre
vender
vinde
renim, recaim
diolaim (reicim)
guerthu
gwerza
frabugjan
selja
selge
sdlga
sellan
selle
sell
verkoopen
jirkoufen
verkoufen
verkaufen
parduoli
parduot
prodati
prodati
prodati
przedaé
prodat’
vi-kri-
krieno (gen.) ‘pretium pro sponsis’, Lett. kriens ‘bridal gift’, Toch. B kdry- ‘trade’ (vb.), sbs. A kuryar, B karyor ‘trade’, A kuryart ‘trader’ (SSS 6, 12).
2. IE *per-, prob. the same ultimately as that in words for ‘pass through, trav- el’, as Grk. zepdw, Goth. faran, ete. Walde-P. 2.40. Pedersen 2.339, 596.
Grk. wépynut, aor. éxépaca, in Hom. always ‘sell abroad’ (esp. captives), as prose word for ‘sell’ most common in mid., as perf. wérpapat, Jon. mémpnuat, hence new pres. mirpaoxopuat, later act. mumpackw; Ir. renim ‘sell’, also vbl. n. reic, whence recaim, Nir. reicim (now less common than diolaim for simple ‘sell’, but Gael. reic the usual word); Lith. pirkti, Lett. pirkt ‘buy’.
3. Derivs. of nouns for ‘price’, etc.
CC-O0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
818 SELECTED INDO-EUROPEAN SYNONYMS
Grk. &péonat the usual word for ‘buy’ in the present (aor. éxptduny, above, 1), Cret. dvéw ‘sell’, fr. dvos ‘price’, avn ‘buy- ing, purchase’ : Skt. vasna-m ‘price’, Lat. venum (or vénus?, nom. not quotable) ‘sale’ whence venum dare, vendere ‘sell’ (> the Romance words), IH *wes-no-, etc., fr. a root *wes- seen in Hitt. was- ‘buy’, ussniya- ‘sell’. Walde-P. 1.311. Ernout-M. 1086. Sturtevant, Hitt. Gloss. 171, 178.
Grk. é&yopétw ‘frequent the market place’, then ‘buy’ (Aristoph.+, gradual- ly replacing dvéopar), fr. dyopd ‘market- place’ (11.85).
Ir. cennaigim, NIr. ceannuighim ‘buy’, fr. cennach ‘purchase’ or cennatge ‘trad- er’ (11.84).
W. gwerthu, Br. gwerza ‘sell’, fr. W. gwerth ‘value, price, sale’, Br. gwerz ‘sale’, prob. : Goth. wairhb, OHG werd, ete. ‘value, price’ (11.87), Lat. vertere ‘turn’, etc. Walde-P. 1.275. Pedersen 2.526.
ChSI. véniti se ‘be sold’ (rendering mwrtonat Mt. 10.29, Lk. 12.6) : véno ‘dowry’, Grk. voy ‘wedding-gift’. Walde-P. 1.256, 312.
4. Lat. caupo ‘petty tradesman, huck- ster, tavern-keeper (Plautus), itself of unknown origin, is the probable, though not undisputed, source of the wide- spread Gmc. group of words for ‘trade, buy, sell, tradesman’, etc., whence also the Slavic verb for ‘buy’. Cf. the Gmc. loanwords based on Lat. mango ‘dealer, trader’ (11.83, 11.84). Ernout-M. 465 f. Walde-H. 1.189. Falk-Torp 521. Feist 309. Berneker 647. Stender-Petersen 374 ff.
Goth. kaupén ‘carry on business’ (rpayparebecba, Lk. 19.3), ON kaupa ‘bargain, trade, buy’, sb. kaup ‘bargain, pay’, Dan. kjgbe, Sw. képa ‘buy’, OF céapan ‘trade, bargain’, rarely ‘buy’, sb. céap ‘bargain, trade, market, price’ (NE
adj. cheap), Du. koopen ‘buy’, verkoopen ‘sell’, OHG koufen (koufon, chaufan etc.) ‘trade, buy, sell’, firkoufen ‘sell? sb. kauf ‘bargain, trade’, koufo ‘trades. man’, NHG kaufen ‘buy’, verkaufen ‘sell’, etc. Hence, prob. through a Goth *kaupjan, ChSl. kupiti, ete., general Slavic for ‘buy’.
5. ‘Buy’ fr. ‘take, obtain’.
Lat. emere, orig. ‘take’ (11.18).
It. comprare, OF r. comperer, Sp. com- prar, Rum. cumpdra, fr. Lat. com-parare ‘prepare, provide, obtain’. Ernout-M, 735. REW 2094.
Fr. acheter, OProv. acapter, OIt. ac- cattare, fr. VLat. *accaptare, a recomposi- tion of acceptdre ‘take, receive’ after captare ‘strive to seize’, REW 65. Wartburg 1.12.
=== leaf of line 20825 ===
885
```


## [2026-09-06T22:38:52.004Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\ntxt=open('SYN.txt',encoding='utf-8',errors='replace').read()\npages=txt.split('\\f')\nprint(pages[884][-2500:])\nEOF"
}
```


### [2026-09-06T22:38:53.832Z] TOOL RESULT

```
 dd- = Skt. dha- ‘put, place’ (ef. Skt. dhana- ‘property, wealth, money’ fr. same root). Barth. 733. Otherwise (: Skt. ddtra- ‘share, property’, fr. da- ‘sive’) Walde-P. 1.715.
Chk 11.79 EARN yg Sonnet &prupae Goth Lith Inyti, uzdirbli NG sto, Bydte ee ith. pelnyti, uzdir : Merére vinna Lett. pelnit quadagnare Dan. _fortjene Chsl. .... g gner Sw.  fortjdna SCr. zaraditi Thin ganar OE (ge)earnian Boh. vydélati 1 Mtatiga te erne, arne Pol.  zapracovaé, zarobié ce : earn Russ. zarabotat’ a *a0lhruighin Gua verdienen by, il ferdienin, (g)arnén gounit MHG verdienen, arnen ‘Bam’ jn : NHG  verdienen (NE cam he sense of ‘get by labor’ in many 2928, earn one’s Y Jabor’ | probably the case also where no words
read, etc.) is erely covered by or ‘gain’. This is
ni the ANguages MOre generic * oe
are entered in the list. Where there are more distinctive terms, they are mostly based on the notion of labor or service.
CC-O0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
816 SELECTED INDO-EUROPEAN SYNONYMS
Even where there are such, the use of ‘get’ or the like may be the more collo- quial, e.g. NE how much do you get a day?
1. Grk. pucbodopiw and picbapvéw, epds. of prods ‘wages’ with dopéw ‘carry, bear’ or &pvupar ‘win, gain’, are used for ‘receive wages, work for wages’, but not with other object of the amount earned.
Grk. xréounat ‘get, obtain’ (11.16) or &pvupat ‘win, gain’ would cover ‘get by labor, earn’.
NG xepditw, or xepdatvw, fr. Képdos ‘gain, profit’ (11.73), is ‘gain’ by busi- ness or by labor.
NG Byéfa, aor. @Byana (fr. Grk. exBar- dw) ‘take out’, etc., also ‘earn’, as Byatw 76 Wout pov ‘I earn my bread’.
2. Lat. merére ‘deserve, gain, earn’ : Grk. pépos ‘share’, pelpouar ‘receive one’s share’, etc. Walde-P. 2.690. Ernout- M. 609f. Walde-H. 2.75 f.
It. guadagnare, Fr. gagner, Sp. ganar, Rum. cistiga, all ‘gain’ and ‘earn’, see sb. ‘gain, profit’ (11.78).
3. NIr. saothruigim ‘labor’ and ‘earn’, fr. saoth- beside saothar ‘labor’ (9.12) and ruigim = rigim ‘reach, attain’, Ir. rigim ‘stretch out, extend’ (: Lat. regere ‘di- rect, rule’, etc.; Pedersen 2.598 ff.).
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
W. ennill ‘gain, earn’, fr, ; ‘gain’ (11.73). ie i Br. gounit ‘gain, earn’, fr. sb. ; ‘gain’ (11.78). vg
4, ON vinna ‘work’ (9.18), ‘gain, win’ also ‘earn’. ;
OE (ge)earnian, ME erne, arne, NE earn, OHG arnén, garnén, MHG arnen (‘earn’ and ‘reap’) : Goth. asans ‘hay- vest’, Goth. a
```


## [2026-09-06T22:39:05.815Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD ===\"\ngrep -n -i \"xrīdan\\|xrīd\\|xrīn\\|šab \\|šab,\\|^šab\\|šām\\|šabestān\\|šabistān\" PHD_mackenzie.txt | head -30\necho \"=== PHD2 ===\"\ngrep -n -i \"xrid\\|xrin\\|sab \\|sam \\|sabestan\" PHD.txt | head -30"
}
```


### [2026-09-06T22:39:05.869Z] TOOL RESULT

```
=== PHD ===
=== PHD2 ===
574:Sab [LYLY A < А Қу); sp | M ib, N ~] night. Bai. NSQ^ ~ag [ФА | N ~a] 1. jet, obsidian; 2. . . . -nights-long. ~estan [ipst?n! | N ~] gynaeceum, private apartments.
583:šāh [MLKA < A mlk’; th | M £h, N <] king. „ān šāh [MLK Ап MLKA | N ~] king of kings. 7--balüt [shbiwt' | N ~] chestnut. ~-дапар [-d’nk' | N —dàna] hemp-seed. ~-esprahm [-splhm | N ~isparam] basil royal. Sahigan [#hyhk'n' | M Phyg^n] palace. šahr [štr' | M £r, N ~] land, country; city. ~estan [MDYNA < A mdyn’; Str'st?n' | M #šhrs Pn, N ~] province; capital, city. Sahrewar [štrywr | N ~] Best Rule, the third Amahraspand, guardian of metals; cal. 6th month; 4th day. šahryār [ftr'd?] | M shry’r, № ~] lord, sovereign, ruler. ~ih ; dominion, reign, sovereignty. šāhwār [š%w?/ | P ?hw’r, N ~] royal, kingly. Sakar [fA] | M šgr, N ~] sugar. salwar [ilw] | N ~] trousers. šām [Pm | = P, N ~] evening meal, supper. Sambalidag [smblytk' | N šambalīd, -lila] fenugreek. šamšēr [smsyl | N ~] sword. бап [in' | N ~] hemp. &ünag [P?^nk! | N ~a] 1. comb; 2. pitchfork; 3. shoulder-blade. šanēn [snyn'] hempen. šarm [т | M #m, N ~] shame. ~-gah [-g*s | N ~] pudenda. ~gén [-k(y)n! | N ~gin] ashamed. &asab [р | (P Shrb)] satrap. ^Agàn [-yk’n'] satrapal. šast [60| M šst, N ~] sixty. šaš [STA < A st | M f, N ~] six. šaw-, v. Sudan. *Sawag [swb’k'] bat, flittermouse. šāyendaģ [^ dyndk!] able, worthy. ~ih: ability, worthiness. šāyistan, šāy- [P?d-stn! | M P?y-, N ~] be able; be worthy. šāyēd [P?(d)yt! | N šāyad] one can, it is possible. šāzdah [cdh | М ?zdh, N sanzdah] sixteen. бер [ғур | N ~] declivity. šēb- [šyp- | M syb, N ~] move quickly; be confused. ~&g [PR' | N —à] swift, nimble; viper. ~išn: confusion. šēd [у | N ~] bright; sorrel (horse). *šēdā [угу] bliss. šēr, v. Sagr. šēwan [£fywn! | N ~] lament. šiftālūg [spi?lwk! | (P šyft ‘milk’), N šaftālū] peach. šiftēnaģ [šp:ynk! | (P £yftyn ‘sweet’)] a sweetmeat.
661:2xān [/?п! | P л?п] spring, source. хапар [BYTA < A рур; h'nR! | N хапа] = іхап. xandidan, xand- (*GHBHWN-yitn' < A V ghk, or У *ghqh; hnd-ytn' | (M xnyst), N —] laugh. xānīg [/?nyk! | M x?nyg, N xàni] = *xān. xar (HMRA < А hmr’; hl | N ~] donkey, ass. хаг [P1 | M ær, N ~] thorn. xar-buz [hibwe | M xrbwz] oryx. xar-g68 [higws | N ~] rabbit, hare. хаготапа [/PPwmnd] thorny. xār-pušt [/?Ipwst! | N ~] porcupine, hedgehog. xastan [hstn' | M xst, N ~] wound, injure. xašën [hsyn! | N хайл] (dark) blue. хауар [Pd(y)k! | N xdya] egg. ~-dés [-dys] oval, egg-shaped. xayüg [Ah )dwk! | N xayū] saliva, spittle. xaz [hz | N —] marten. xém [лут] nature, character. xëšm [?yfm, hfm | M xysm, N xifm] anger; the demon Wrath. --én [-ya! | M -yn) angry. xindag [hyndk' | M xyndg] ill, sick. ~th: illness, sickness. xir [C BW! < А sbw; hyl | M хут] thing, matter. xirs [hls | N ~] bear. xišt [Ast! | (P hystyg), N ~] brick. хбё [hwk' | N xwk, xóy] nature, character, disposition. x6n [DM YA < А dm’; һит! | M хоп, N хип] blood. xormā [TE A tmryn; hwlm’k' | N ~] date. xrad [hit! | M xrd, N xirad] wisdom, reason. ~ig, ~Omand [-yā!, тиа | N -mand] wise. xrafstar [hlpst] = Av. xrafstra-] reptile, noxious creature. xridan, xrin- [ZBNN-tn! < A V zbn| M xryd, xryn-, N xaridan, (xar-)] buy. xróhak [hlwhk' | N ~] coral. xrēs [DYLK A < A dkr’; hlws | P xrws, N xurós] cock. xróstan [Alwstn! | M xrwst] call, cry. xüb [hwp | M xwb, N ~] good. ~th: goodness. xuftan, xufs- [HLMWN-tn! < А У Ыт; hwptn', hwps- | М xwpt, N xuftan, xusp-] sleep. xūg [HZWL УА < А hzyr; hwk' | N ~] pig. xükar(ag) [hwkl(k') | N xūkara] hedgehog. xumb [kwmb! | M xwmb, N ~] jug, pitcher. xunak [hwnk' | M xwnk, N xunuk] happy; cool. xurdruš [kwldlwš, -dlpš = Av. xrwidruf] ‘with a bloody club’ (epithet of Xēšm, later misinterpreted as *ul-draff ‘*with raised banner’).
1129:buy xridan.
2183:gynaeceum Sabestan.
```


## [2026-09-06T22:39:07.311Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HUB xarid ===\"\ngrep -n -i \"xarīdan\\|xaridan\\|xrīnāti\\|kriṇāti\" HUB.txt | head -20\necho \"=== HUB sab ===\"\ngrep -n -i \"šab\\b\\|sab 'Nacht'\\|Nacht\" HUB.txt | head -30"
}
```


### [2026-09-06T22:39:07.370Z] TOOL RESULT

```
=== HUB xarid ===
6048:skr. bhrjj; xaridan *kaufen* (F. i. 8h. xirtdan), skr. ptc.
=== HUB sab ===
714:164. Da bd^, wie in den Nachtragen bemerkt ist, nicht
1199:274. Zu pas *Wache, Nachtwache' vgl. Nr. 341: pahra^
1584:61). In den Nachtragen erwahnt Horn (zu tofndan
1852:469. In den Nachtragen wird saxudan zerkratzen' (afgh.
2231:ptc. duyd u. s. w. (Nachtrjlge zu Nr. Ill meiner Etym.
2503:680. In den Nachtragen bemerkt Horn sehr richtig, dass
2638:735. In den Nachtrftgen wird richtig bemerkt, dass surod
2698:748. Lies so, sot = phi. sdk. Vgl. die Nachtrage bei
2891:796. Lies zd. *xsaodraka" und ^xSaoda- (vgl. die Nachtrage
4634:(ace.) 'das Nachtliche* yt. 14, 20, aber xsafmm (ace.) 'das
6249:*Nacht*, ap. xsapa-va; sitab *Eile', arm. stap; farbih 'fett',
7261:pud^'a-; pahra^) 'Wache, arm. pah 'Nachtwache, Wache,
8291:gos *Ohr = ap. gausa-; dds *letzte Nacht', zd. daosa-
8303:a) im Anlaut: sOm 'Nachtessen, zd. xsofnya-; sdh
8305:zd. xsi; sab 'Nacht* = ap. xsapa-iva) 'des Nachts'; sas
8361:*Nacht*; snorh 'Gnade' = zd. xsnaod^ra-; snum 'Freude' in
9058:Auslaut: ^a/ *Hitze' = zd. tafnu-, tafnah-; sdm^) *Nacht-
```


## [2026-09-06T22:39:23.511Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\ntxt=open('DRM.txt',encoding='utf-8',errors='replace').read()\npages=txt.split('\\f')\nprint('total leaves',len(pages))\nfor leaf in (525,526,524):\n    print('#### leaf',leaf,'####')\n    print(pages[leaf][:1800])\nEOF"
}
```


### [2026-09-06T22:39:25.613Z] TOOL RESULT

```
total leaves 756
#### leaf 525 ####
0
pur  se  trouve  dans  l’inscription  pehlvie  de  Naqshi  Rustam, ligne  6   '.  Aucune  explication,  que  je  sache,  n’a  été  présentée de  ce  terme.
La  lecture  vaçpûr,  attestée  d’ailleurs  par  l’orthographe  sassa- nide  i,  n’est  point  primitive  :   a   représente  un  ancien  i,  viçpûr. Ce  mot,  en  effet,  n’est  autre  chose  que  le  zend  vîçô-puthra, littéralement  «fils  de  maison,  Bar-bîtâ-» ,   puthra  étant  rendu par  son  dérivé  pur,  pehlvi  sassanide  pûhr.
Dans  ma  traduction  du  Vendidad  j’ai  rendu  vîçô-puthra  comme s’il  signifiait  vîç-patôis puthra,  «   the  son  of  the  lord  of  a   borough  » (VII,  43  [114])  :   cette  traduction  n’est  pas  admissible.  Le  passage où  paraît  ce  mot  est  un  tarif  du  salaire  du  médecin,  selon  la  di- gnité des  malades  qu’il  soigne  :   voici  ce  tarif  :
pour  un  prêtre
chef  de  nmcîna  (maison)
chef  de  vîç  (bourg)
chef  de  zaîitu  (ville)
chef  de  daliyu  (province)
une  bénédiction, la  valeur  d’un  bœuf  de  der- nière qualité, la  valeur  d’un  bœuf  de  qua- lité moyenne, la  valeur  d’un  bœuf  de  pre- mière qualité, la  valeur  d’un  chariot  h   qua- tre chevaux.
femme  d’un  chef  de  nmcîna femme  d’un  chef  de  vîç femme  d’un  chef  de  zaîitu femme  d’une  chef  de  dahyu
un  vîçô-puthra
valeur  d’une  ânesse. valeur  d’une  vache, valeur  d’une  jument, valeur  d’une  chamelle.
valeur  d’un  bœuf  de  pre- mière qualité.
Le  vîçô-puthra  ne  peut  être  le  fils  d’un  chef  de  vîç,  puisqu’il est  estimé  à   un  taux  plus  élevé  que  lui  :   il  vaut  un  chef  de zaîitu,  c’est-h-dire  qu’il  vient  immédiatement  après  le  chef  de dahyu,  le  chef  de  province,  comme  dans  l’énumération  sassa-
1.  Ecrit  avec  mater  lectionis  :
#### leaf 526 ####
ç  pûç  pat, '■  put  est  sans  aucune  doute  amené  par  l’analogie  des termes  précédents  :   mân-mdnpat,  vîç-mçpat,  zand-zandpat ,   matâ- dahyûpat.  La  traduction  de  vîçô-puthra  est  exclusivement  vîç- pûç  :   pûç  est  un  doublet  bien  connu  de  pûhr  et  de  puçar;  il  re- présente comme  eux  put  lira,  et  vîç-pûç  est  un  doublet  de  viçpûr et  comme  lui  désigne  un  degré  de  noblesse.  Quel  degré?
vîçô-puthra  se  rencontre  ailleurs  dans  l’Avesta.  C’est  un  titre donné  à   Thraêtaona  :   il  est  appelé  :   vîçô-puthrô  âthwyanôish  vîçô çûrayâo  ( Yt .   V,  23  et  passages  parallèles).  Ou  traduit  généra- lement :   «Thraêtaona,  fils  de  la  maison  d’Àthwya,  maison  puis- sante »;  en  réalité,  il  y   a   là  un  titre  technique  :   «Thraêtaona, le  vîçô-puthra  de  la  puissante  maison  d’Athwya».
Nous  traduirons  :   «Thraêtaona,  l’héritier  (ou  le  chef)  de  la puissante  maison  d’Àthwya  »   :   l'exact  équivalent  européen serait  infant.
Le  vîçô-puthra,  le  viçpûr,  le  Bar-hit iî  est  l’héritier  d’une  vîç; mais  ici  il  faut  prendre  le  mot  dans  sou  sens  le  plus  haut  et le  plus  spécial  :   une  grande  maison.  C’est  le  fils  aîné  d’une grande  famille,  peut-être  bien  le  fils  aîné  des  dahyu-paiti,  des shatardar,  puisque  c’est  le  titre  immédiatement  inférieur.  11  ne désigne  pas  une  fonction  présente,  et,  en  cela,  il  est  en  dehors de  la  hiérarchie;  mais  il  implique  une  fonction  dans  l’avenir. Ceci  nous  permet  de  nous  retrouver  dans  les  emplois  très  com- plexes du  mot  vîç  :
1°  Sens  premier,  comme  en  sanscrit,  maison  :   c’est  le  sens qu’il  a   dans  vish-haurva ,   le  nom  du  chien  «garde  de  maison».
2°  Sens  administra
#### leaf 524 ####
yâ XXXII,  13;  cf.  encore  LII,  6;  XL1V,  1   etc.).
BAR,  SOUFFLER  (FLARE,  TO  BLOW).
(Soc.  de  Linçj.  IV,  219.)
Barenti vâ  (   Vendiclad,  VIII,  4 [12])  :   «   ou  pendant  qu’il  vente  ». Le  sens  est  établi  par  le  contexte  et  la  tradition;  par  le  con-
1.  Aêshma  est  le  nom  de  la  colère  et  du  daêva  de  la  colère.
2.  Le  zend  bànayen  prouve  en  même  temps  que  M.  Curtius  a   raison  de défendre  contre  la  racine  ghnn  l’indépendance  du  grec  (pdvoç  (Etymohyie grecque ,   31-'  éd.,  p.  280).  L’Irlandais  a   la  même  racine  ben  :   di-bnim,  je  tue.
139
texte  :   vu  refit  i   và  çnaêzhenti  vd  bareüti  vu,  «   pendaut  qu  il  pleut,
ou  qu  il  neige,  ou  qu’il   »;  par  la  tradition  :   $4  ne),
pun  buland  vât  damak  «pendant  souffle  violent  du  vent».
Il  semble  que  le  traducteur  ait  reconnu  dans  bareiiti  le  persan il  a   eu  tort,  car  jbJo,  littéralement  «élevé»,  dérive  de berezant  et  est  une  variante,  quant  à   la  racine,  de  (I,  §   71); mais  il  a   d’ailleurs  conservé  la  parfaite  conscience  du  vrai  sens et  senti  pour  cela  le  besoin  d’ajouter  vât  damak;  il  faut  donc faire  abstraction  de  son  étymologie,  qui  est  fausse,  et  retenir sa  paraphrase,  qui  est  juste.
Quant  h   l’étymologie,  elle  nous  est  donnée  par  le  latin  pire, l’anglais  to  blow.
BARBÎTÂ,  VAÇPÛR,  VÎÇÔ -PUTHRA.
Le  mot  Barbîtâ  désigne  une  classe  de  nobles  dans  la  hiérar- chie sassanide.  11  se  trouve  dans  l’inscription  pehlvie  deSaporl (240-270)  a   Hàjîâbâd  :   lûînî  shatardaràn  va  barbîtân  va  vazar- kân  va  âzâtan  ',  «en  présence  des  princes2,  des  Barbîtâ,  des grands  et  des  nobles».
Barbîtâ  est  clairement  un  araméen  Xff2
```


## [2026-09-06T22:39:31.078Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"khshap\\|xshap\\|kshap\\|çhap\\|xsap\\|nuit\" DRM.txt | sed -n '1,40p'"
}
```


### [2026-09-06T22:39:31.130Z] TOOL RESULT

```
228:Un  certain  nombre  de  savants  contestent  encore  la  valeur  r au  signe  i   et  le  lisent,  s’appuyant  d’ailleurs  sur  la  tradition,  n au  lieu  de  r.  Mais  comme  d’ailleurs  il  est  certain  que  dans  les mots  contestés  la  valeur  étymologique  du  son  est  r ,   ils  sont obligés  d’admettre  un  changement  étrange  de  r   en  n,  qui  serait propre  au  pehlvi  et  qui  aurait  disparu  en  persan.  Une  pareille perturbation  dans  le  système  phonétique  d’une  langue,  sur  un point  unique  et  pour  une  période  unique,  est  une  chose  qu’il n’est  possible  d’admettre  que  forcé  par  les  preuves  de  fait.  Je crois  utile  d’étudier  ici  la  question  de  près,  parce  qu’elle  n’em- porte rien  moins  que  la  question  de  savoir  s’il  y   a   eu,  ou  non, continuité  naturelle  dans  le  développement  des  sons  de  la  langue persane,  ou  si,  seule  des  langues  étudiées  jusqu’ici,  elle  se  sous- trait à   cette  loi,  ce  qui  du  même  coup  ébranlerait  l’autorité  de toute  loi  phonique  dans  ce  domaine.
526:Dans  cette  expression  Mallcân  malkâ,  ou  tous  les  éléments  for rnels  sont  aryens,  —   le  signe  du  pluriel  et  la  place  des  termes, —   rien  a   la  rigueur  qui  dépasse  les  limites  possibles  de  l’influence étrangère  :   il  n’y  aurait  rien  d’impossible  à   priori  que  le  titre de  malkâ  eût  été  adopté  par  les  Persans  et  fût  devenu  national  : et  pourtant  l’on  voit  par  l’exemple  d’Ammien  que,  même  dans cette  mesure  modeste,  la  thèse  du  sémitisme  réel  est  contraire aux  faits.  Pour  le  peuple,  pour  le  soldat,  par  suite  pour  la  langue vivante,  le  roi  des  rois  était,  non  pas  Malkân  malkâ,  mais  Shâhân shâh  :   le  vieux  titre  des  Achéménides,  Khshayathiyânâm  khsha- yatkiya ,   parvenu  jusqu’à  nous  sous  la  forme  moderne ne  s’est  pas  éteint  dans  l’intervalle  sur  les  lèvres  du  peuple  pour faire  place  à   un  calque  sémitique,  et  le  saanman  des  soldats  de Sapor  rétablit  le  lien  de  continuité  entre  le  titre  ancien  et  le  titre moderne,  à   la  face  du  décevant  Malkân  malkâ,  des  inscriptions.
1412:khshap,  nuit  shah
1490:p.  gausha,  oreille *dausha,  la  nuit maêsha,  mouton aêsha,  soc  2 dtish-  mal raésha,  blessure aoshô,  la  mort çraêshay-,  mêler Çraosha
1586:Le  pehlvi  shâm,  persan  flL,  repas  du  soir,  traduit  le  zend khshafniya  qui  a   le  même  sens  (F.  LXI,  3   9)  -   ;   la  forme  perse  de khshafnya  serait  *khsliapniya,  le  perse  n’assimilant  pas^i  devant n,  comme  l’indique  le  persan  tab,  chaleur,  devant  le  zend  tafna, peut-être  aussi  le  persan  khvâb,  sommeil,  devant  le  zend  hvafna. Le  n   de  *khshapnya  s’est  répercuté,  comme  par  épenthèse, devant  la  labiale,  d’où  *klishamp-nya  ou  *khshamf-nya ,   *khsham- nya,  *khshâm.  Le  mot  shâm  s’emploie  aussi  au  sens  de  «soir», et,  quoique  dérivé  d’un  adjectif  de  klishapan  et  non  pas  de khshapan  même,  est  phonétiquement  dérivé  des  éléments  de klishapan ,   le  suffixe  ya  étant  tombé  :   c’est  par  suite  un  doublet de  shah,  nuit3.
1653:*khshathra-dâta , khshap,  nuit
1654:*khshap-nya.  repas  du  soir  £tx> khshudra,  semence khshtra,  lait  iJje  shîr
2594:Les  désinences  étant  tombées  en  persan,  il  n’y  a   plus  à   distin- guer de  thème.  Tous  les  thèmes  sont  égaux  devant  la  syntaxe. Le  thème  mardi ,   homme,  ;y«,  dérivé  d’un  thème  en  a,  martiya, le  thème  mai,  vin,  dérivé  d’un  thème  en  u,  madhu , le  thème  bûm,  terre,  dérivé  d’un  thème  en  i,  bûmi, le  thème  shab,  nuit,  dérivé  d’un  thème  en  p,  khshap,
2611:shab,  nuit
3571:imsliab,  cette  nuit  ;   imam  khshapam.
4506:est  donc  le  signe  du  présent  parce  qu’il  représente  directement l’idée  de  continuité  :   «il  fait»,  signifie  littéralement
4734:1.  D’où  l’imparfait  en  préposant  le  signe  de  la  continuité  pelilvi
4857:«Peut-être  que  cette  nuit  le  coq  ne  chantera  pas»  (littérale- ment «ne  chante  pas»).
4884:jonctif et  en  indicatif  présent  proprement  dit,  <y  marquant littéralement  la  manifestation  de  l’action,  ^   marquant littéralement  la  continuité  de  l’action.
4895:L’imparfait  a   été  formé  du  prétérit,  comme  l’indicatif  pré- sent l’est  de  l’aoriste,  en  préfixant  le  signe  de  la  continuité hamê,  me  (ou  en  postfixant  le  signe  de  continuité  é)  : me,  hamê  burdam  yy  ^0,  je  portais burdam-ê
5229:Paraît  hier  ;   parandôsh  la  nuit  d’hier,  hier  soir.
5237:Dôsh  (jiy,  primitivement  «la  nuit»  (z.  daosha ),  a   pris  le  sens de  «la  nuit  d’hier,  hier  soir».
5240:Hanûz  d’où  (§  240)  «   encore  »,  de  *anûc,  formé  de  anu qui  indique  suite,  continuité  (vol.  II,  114).
5252:de  nuit.
5364:an  :   substantifs  primaires  : khshapan,  nuit.
5617:sliaban-  dans  le  composé  ;   shabanrôz ,   jour  et  nuit,  de
6108:shabîna  de  nuit,  de  shah,
6837:z.  haptô-iringa,  les  sept  ours. thriçatô-zima,  trois  cents  ans. thri-khshaparem,  trois  nuits.
6982:nuit.
7047:§   *299.  —   Type  zend  :   thri-khshaparem  :   trois  nuits.
7048:Parsi  :   çadiç;  ce  mot  désigne  l’ensemble  des  trois  nuits  qui suivent  la  mort  :   çadiç  est  une  fausse  lecture  du  pelilvi  çitôsh -Ois?",  dans  lequel  ?   représente  un  d   primitif  :   çi-dôsh,  t rois-nuits.
7694:au  grand  plaisir  du  lecteur.  Je  m’étonne,  pour  ma  part,  que l’on  n’ait  pas  encore  songé  à   rattacher  les  Partîtes  h   ces  proto- Scythes  il  la  mode  :   la  révolte  d’Arsace  serait  le  réveil  de  la nationalité  scythique  ou  accadienne,  et  cet  exemple  de  la  con- tinuité historique  sourirait,  sans  doute,  à   l’esprit  philosophique de  notre  temps.
8225:aêtadha  lie  uzbaodhâm  tanûm  nidaidhyan,  bikhshaparem  vâ tbriksbaparem  vâ  mâzdrâjahîm  vâ,  vîçpem  â   ahmât  yat  frâ vayô  patàn ,   frâ  urvara  ukhshyân,  nyâonco  apa  tacin  (1.  apô tacin)',  uç  vâtô  zâm  haêcayât  «là  ils  déposeront  le  corps  ina- nimé, soit  deux  nuits,  soit  trois  nuits,  soit  un  mois  durant,  jus- qu’à ce  que  de  l’avant  les  oiseaux  prennent  leur  volée  (pour revenir),  que  les  plantes  reprennent  leur  poussée,  les  eaux  basses leur  coulée,  et  que  le  vent  qui  se  lève  dessèche  la  terre  »   (   Vend.
8626:Vend.  XVIII,  5   (12).  Yô  çaêtc  haurvâm  taraçca  khshapanem ayazemnô  açrâvayô  amarô  everezyô  açikhshô  açâcayô  jayâi
8631:cinvat-ushtânem  diwzhat  haca  âthrava  çanhaitê.  <   Celui  qui  dort la  nuit  entière,  d’un  bout  à   l’autre,  sans  dire  le  Yaçna ,   sans dire  les  cantiques1,  sans  réciter  les  prières,  et  sans  accomplir
8723:De  même  l’Avesta  donne  le  titre  de  adhaoya  (=  *adabhya) au  dieu  Mithra,  qui  certes  y   a   droit,  puisqu’il  a   dix  mille  re- gards, dix  mille  espions,  puisqu’il  voit  tout,  et  qu’Ahura  lui  a bâti  une  demeure  sur  cette  montagne  resplendissante  où  n’arri- vent ni  nuit,  ni  ténèbres,  ni  vent  froid,  ni  vent  chaud,  ni  ma- ladie aux  mille  morts,  ni  souillure  créée  des  daêvas,  ni  nuée
8782:1.  Celui  qui  voit  l’aurore  avant  tous  les  autres  (Haug:,  Das  arhtzehnle Capitel  des  Vendidad,  p.  7,  note  14).  Comparer  le  nom  hébreu  du  coq, '1-D ,   l’intelligent  :   le  rituel  hébreu  remercie  Dieu  d’avoir  donné  au  coq l’intelligence  de  distinguer  le  .jour  de  la  nuit.  Voir  notre  Fragment  d'un Commentaire  sur  le  Vendidad,  ch.  XVIII.
8811:Khshaf m/a,  dérivé  de  khshapan  -   khshaf  nô}  nuit,  signifie  «noc- turne», et  hàm  pacaiti  khshafnîm  signifie  «fait  cuire  (le  repasj du  soir».
8813:Khshafnya  étant  le  repas  du  soir,  il  est  naturel  de  faire  de çûirya  le  repas  du  matin.  D’ailleurs  çûra  est  précisément  une épithète  usuelle  de  l’aurore  :   çûrâm  upa  ushâohliem,  et  l’on  trouve ailleurs  encore  les  deux  mots  opposés  l’un  à   l’autre  en  parlant de  l’alternative  du  jour  et  de  la  nuit  :
8814:«   L’oiseau  Vâraghna  (le  corbeau;  voir  vol.  I,  59,  n.  1),  le  plus rapide  des  oiseaux,  le  plus  léger  des  êtres  qui  volent,  s’en  va tout  joyeux  à   l’instant  où  l’aube  perce,  désirant  que  la  nuit ne  soit  plus  nuit  et  que  le  monde  sans  aurore  ait  l’aurore  : uklishafni  khshafnîm  içemnô  açûiri  çûirîm  içemnô »   ( Yt .   XIV,  20).
9565:P.  155.  «   Certains  individus  sont  forcés  au  temps  de  la  pleine lune  (le  choix  du  moment  se  lie-t-il  à   la  croyance  précédente?) de  se  transformer  en  loups  garoux.  Le  mal  les  prend  toujours la  nuit;  lorsqu’ils  eu  sentent  les  approches,  ils  s’agitent,  sortent de  leur  lit,  sautent  par  la  fenêtre  et  vont  se  précipiter  dans  une fontaine  ou  dans  un  puits,  d’où  ils  sortent  quelques  instants après,  revêtus  d’une  peau  blanche  ou  noire  que  le  diable  leur a   donnée.  Dans  cet  état  ils  marchent  très  bien  à   quatre  pattes, passent  la  nuit  à   courir  les  champs  et  à   hurler  dans  chaque village  qu’ils  traversent.  A   l’approche  du  jour,  ils  reviennent à   la  fontaine,  y   déposent  leur  enveloppe  et  rentrent  chez  eux, où  ils  tombent  souvent  malades  de  fatigue»  (Gautier, Statistique de  la  Charente  -   Inférieure,  1839.  p.  234).  Cette  croyance,  qui court,  paraît-il,  les  campagnes  de  la  Charente-Inférieure,  est venue  là  d’Arcadie  par  l’intermédiaire  de  Pline  :   «Evanthes inter  auetores  Graeciae  non  spretus  tradit  Arcadas  scribere, ex  gente  Anti  cujusdam,  sorte  familiae  lectum,  ad  stagnum quoddam  regionis  ejus  duci,  vestituque  in  quercu  suspenso trausnatare,  atque  abire  in  deserta,  transfigurarique  in  lupum, et  cum  eeteris  ejusdem  generis  congregari  per  annos  novem. Quo  in  tempore  si  homine  se  abstinuerit,  reverti  ad  idem  stag- num; et  quum  transnataverit,  effigiem  recipere,  ad  pristinum habitum  addito  novem  annorum  senio.  Id  quoque  Fabius, eamdem  recipere  vestem  »   (VIII,  34).  Il  n’est  guère  possible de  douter  devant  l’identité  des  deux  récits  que  le  paysan  delà
11018:yadi  tat  prâptam  asti  nova  tat  prâptam  asti samidhâmca  atha  çushkânâm  nirîxitânâm  bhârakam  âkarpa- maryâdam  shûlam  atha  kakshapramânam  sthûlam  atha  ha- stayos  pramânam  sthûlam  guror  gpham  samânayet.
```


## [2026-09-06T22:39:39.702Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\ntxt=open('DRM.txt',encoding='utf-8',errors='replace').read()\nlines=txt.split('\\n')\npages=txt.split('\\f')\nfor t in (1412,1586,1653,2611,8811):\n    leaf=('\\n'.join(lines[:t])).count('\\f')\n    print('line',t,'leaf',leaf)\n# find printed page numbers near leaves\nfor leaf in range(158,168):\n    p=pages[leaf]\n    nums=re.findall(r'^\\s*(\\d{2,3})\\s*$', p, re.M)\n    print(leaf, nums[:5], p[:60].replace('\\n',' '))\nEOF"
}
```


### [2026-09-06T22:39:41.858Z] TOOL RESULT

```
line 1412 leaf 101
line 1586 leaf 109
line 1653 leaf 111
line 2611 leaf 149
line 8811 leaf 547
158 ['130'] de  là  *kôfkhâ, kôfhâ. C’est  à   la  première  de  ces  de
159 ['131'] risés,  dans  lesquels rien  ne  révèle  au  Persan  la  fon
160 []  de  prépositions  ou  de  postpositions. Autrement  dit,  l
161 ['132'] ya,  non  de  ya. 9* 132 Dans  la  période  intermédiaire  l
162 ['133']  qu’à  mieux  détacher  la  personne  qui  est  le sujet  de
163 ['134'] insi  pour  les  noms les  plus  communs: homme ma  rd 5r° p
164 ['135'] rda, de  toute  espèce. En  persan,  et  déjà  en  pchlvi,  
165 ['136'] 42), comme  *dauçtar,  p.  écrit  daushtar. 136 duzhgainti, 
166 ['137'] t  le  plus  savoureux  ;   z.  livarezishta 3. I)c  ces  fo
167 ['138'] est  un  comparatif,  formé  du  nom ancien  Mâzana.  C'est
```


## [2026-09-06T22:39:51.139Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\ntxt=open('DRM.txt',encoding='utf-8',errors='replace').read()\npages=txt.split('\\f')\nfor leaf in (545,546,547):\n    p=pages[leaf]\n    print('#### leaf',leaf,'nums',re.findall(r'^\\s*(\\d{2,3})\\s*$',p,re.M)[:4],'####')\n    print(p[:1600])\nEOF"
}
```


### [2026-09-06T22:39:52.708Z] TOOL RESULT

```
#### leaf 545 nums [] ####
in de  la  forêt!
«Frappe  tout  ce  qui  hurle  autour  de  moi  (parikroçam) ,   casse les  os  au  krkadâçu! 1   »
La  suite  des  idées  est  claire.  Le  poète  a   sommeil,  il  veut dormir  en  paix,  il  demande  à   Indra  de  faire  taire  tout  ce  qui trouble  les  dormeurs,  l’àne  qui  brait,  le  vent  qui  remue  la  forêt, le  krkadâçu.  Si  le  krkadâçu  védique  rappelle  par  son  nom  le kahrkatâç  zend,  le  sens  que  ce  dernier  lui  prête  cadre,  autant que  possible,  avec  le  contexte  :   la  fable  de  la  Vieille  femme  et des  Deux  Servantes  prouve  que  les  gens  amis  du  sommeil  n’ont pas  grande  tendresse  pour  le  coq.  Le  krkadâçu  est  comme  le coq  un  personnage  bruyant,  méritant  d’être  cité  parmi  les  pari- kroça,  et  se  livrant  précisément  à   l’acte  exprimé  par  ce  verbe kruç  «   clamare  »,  qui  a   donné  son  nom  au  coq  en  persan  moderne, khurûç
Phonétiquement,  le  rapprochement  d e   kahrkatâç e t   d e krkadâçu offre  une  difficulté  assez  grave;  je  ne  parle  pas  de  la  différence  de ahr  à   r,  ahr  (c.-à-d.  ar )   étant  l’équivalent  de  r   :   je  veux  parler  de la  différence  des  consonnes,  t   dans  l’un,  d   dans  l’autre,  l’un  se ramenant  à   un  type  * karkadâçu,  l'autre  à   un  type  *   karkatâcu  (?).
Je  crois  que  le  type  primitif  est  *karkadâçu  et  que  le  mot zend  en  est  une  corruption,  hypothèse  facile  à   admettre  dans des  mots  de  cette  nature,  et  corroborée  par  le  morceau  suivant, parallèle  au  passage  du  Vendidad  résumé  a
#### leaf 546 nums ['160'] ####
omme  à   son  secours  contre  les  attaques  d’Azi.
160
doute  «dont  la  voix  est  aigue  comme  un  couteau».  Mais  c’est la  une  dénomination  bien  étrange  et  il  est  d’ailleurs  a   remar- quer que  le  nom  de  karetô-dàçush  n’est  pas  donné,  ainsi  que c’était  le  cas  avec  kakrkatâç ,   comme  un  nom  de  mauvais  augure  ; il  paraît  bien  par  le  contexte  que  le  nom  n’emporte  rien  de désobligeant  pour  l’honneur  de  l’oiseau  sacré.
11  existe  de  ce  morceau  une  traduction  pehlvie1,  qui  mal- heureusement manque  de  clarté  :   «l’oiseau karetô-dàçush-»  est  tra- duit zak  murv  i   kartak  dânishn  man  dar  kart  yeqôyemûnît  »,  ce  qui semble  signifier  «qui  connaît  l’action2 3  qui  est  faite».  Karetô est  donc  traité  comme  le  participe  de  kar,  faire  et  dàçu  est  tra- duit comme  parent  de  dâo  «qui  sait»,  de  dàhah  «science»,  de dâhishta  «très  savant»,  de  dàçtva  «enseignement,  règle».  On peut  douter  au  premier  abord  que  cette  traduction  de  dàçu repose  sur  une  tradition  authentique;  car  la  racine  de  dâo , dàhah,  dâhishta,  dàçtva,  est  en  s   primitif,  zend  dah  et  non  daç. Cependant  il  a   pu  exister  en  zend,  à   côté  de  dah,  une  racine synonyme  daç,  parallèle  au  latin  doc-eo,  et  le  fait  que  le  nom  de karetô-dàçush  est  un  nom  honorable  fortifie  encore  le  témoignage de  la  tradition,  car  karetô-dâçu  devient  le  synonyme  ou  plutôt le  complément  de  parôdarsh  :   le  coq  est  à   la  fois  celui  qui  voit le  premier  l’aurore  (parôdar
#### leaf 547 nums [] ####
ubliée  plus  bas  parmi  les  Traductions  indigènes.
2.  Ce  qui  se  passe;  peut-être  «ce  qu’il  y   a   à   faire».  On  pourrait  songer aussi  à   kartak  au  sens  de  chapitre  de  l’Avesta  :   ainsi  Karshiptan  récite l’Avesta  dans  la  langue  des  oiseaux  ( Buiulchesh ,   XIX,  16);  le  coq  serait un  prêtre  qui'  récite  :   Parôdarsh  est  d’ailleurs  le  prototype  du  coq  muezzin des  Musulmans.  Mais  la  suite  de  la  glose  se  traduit  difficilement  dans  cette hypothèse.
3.  Kahrka  peut  être  une  onomatopée  :   cocorico;  le  coq  s’appelle  en sanscrit  krkavûku  «celui  (pii  crie  krka »;  le  perdrix  s’appelle  krkara,  kra kara,  «qui  fait  1er,  kra ».  Dû çu,  dans  le  nom  primitif,  signifie  peut-être «qui  donne,  c.-à-d.  qui  fait  entendre»  fdûçj.
un
d’autre  part  par  une  transformation  artificielle  en  karetô-dâçu, qui  v   infuse  un  sens  nouveau  tout  à   I   honneur  de  Parôdarsh.
KILSHAFNIM  et  ÇUIRIM  :   et
(Soc.  de  Ling.  V,  7G.)
Vîcpaîàhyô  çrirtî vi  baraiti  yaêibyô  aêm  hàm  pacaiti  khshafnîmca çûirîmca  (Yç.  LXI,  18).
«   Atar  (le  Feu)  adresse  la  parole  a   tous  ceux  pour  qui  il  cuit le  lcJishafnya  et  le  cûrya  » .
Khshaf m/a,  dérivé  de  khshapan  -   khshaf  nô}  nuit,  signifie  «noc- turne», et  hàm  pacaiti  khshafnîm  signifie  «fait  cuire  (le  repasj du  soir».
Khshafnîm  est  rendu  en  pehlvi  par  le  groupe  poo,  qui  est susceptible  théoriquement  de  lectures  multiples;  mais  une  seule concorde  avec  le  sens  et  s’impose  immédiatement  :   c’est  la
```


## [2026-09-06T22:39:59.529Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\npython3 - <<'EOF'\ntxt=open('BQT_v3_pages.txt',encoding='utf-8',errors='replace').read()\npages=txt.split('\\f')\nprint('leaves',len(pages))\nfor i in range(15,40):\n    p=pages[i]\n    head=p[:120].replace('\\n',' ')\n    print(i, 'printed~',i+1209, head)\nEOF"
}
```


### [2026-09-06T22:40:01.252Z] TOOL RESULT

```
leaves 721
15 printed~ 1224 [pdf page 16] سنننه  ‎OL!‏ را شاء و تر کستان را خان میگوندوبسنی ‎ate alos ea‏ باشد - و غل وغشی را نیز کوبند که در طلا ون
16 printed~ 1225 [pdf page 17] اروان  ‎Sys‏ است که جاور سخ نکوی باشد.  ‏شاروان © بر وزن کاروان , مخفف شادروان است که پردة بز رک و شامیانه
17 printed~ 1226 [pdf page 18] {ATTY  شاشه ه بر ون ‎tle‏ » معروف است که بول و گمیز باشد ۱ - و ‎Ory Feiner‏ وترشح ‎Gs‏ آمده است .  شاشیدن 
18 printed~ 1227 [pdf page 19] شا کمونی مالند ؛ وبس یکوند ‎WT‏ که از یشم کوسفند و موی بز سیاه در هم آمیزند وبمالند شا کمند خوالند .  شا ک
19 printed~ 1228 [pdf page 20] ATTA  ‎SL‏ ۱ » بروزن قالی. شلتوفرا کوشد که برنج از پوست برليامده ‎wth‏  ‎HY JL‏ » با ‎alist‏ بالف کنیده ‎c
20 printed~ 1229 [pdf page 21] شاد ۲۳۰ ات  شا له ۱ = بروزن ‎le‏ معروفت‌وآن  چیزی باشد که از چوب و غیره سازاد و بدان‌رش سس رزلف و کیو راپر
21 printed~ 1230 [pdf page 22] ۱۳ ات  شانه‌سر ۱۵ صفیر ‎als‏ سراست که  شانه کاری » ‎at‏ از در آوختن بکسی باشد یعنی با ‎OT‏ شخص درمقام زدوخ
22 printed~ 1231 [pdf page 23] که ازآن راهپا وشمبها جدا شود - وفام‌جالوری ‎col‏ در هندوستان - ‎ply‏ جامه‌ای و پارچه‌اییست که از هند آورند
23 printed~ 1232 [pdf page 24] پات شاء خرگاه میتا  شاه بانگ ۱ - بنتم ون و سکون کاف »گیاهی امت دوابی و آنرا بتازی بنفج الکلاب خوانند " ومم
24 printed~ 1233 [pdf page 25] شاه دارو شاه ‎gale‏ ه امی است که جمشید بشراب انگوری گذاشته است»وسبب آن بود که چون الگور درزمان چمشید بهم ر
25 printed~ 1234 [pdf page 26] سلفننهه  شاهد لعمر ك ‎gine‏ شاهد فاستقم است که اشاره بحضرت رسالت پناه صلوات‌العلیه ‎Vash aT,‏ .  شاه دراه 
26 printed~ 1235 [pdf page 27] Sob ‏شاه قام = با قاف بالف کشیده بروزن‎ ‏است که کسی‌خود را دربازی‌شطر نج‎ oT ‏شادکام‎ ‏زبون بیند حریف را پ
27 printed~ 1236 [pdf page 28] -۱۲۳۷-  سوجای ‎gid‏ پادشاهان ‎ath‏ - ونوعی ازعمارت هم هت +  شاه نیم رود ۲ ‎aus.‏ از آفتاب است - و والی و ح
28 printed~ 1237 [pdf page 29] شایسته ۱ - بکرستای‌بروزن‌آهته بمعتی اول شابان است که سزاوار ولایق ودرخور ‎ath‏ . ‎Heals‏ بود ۴ - ایکون واو
29 printed~ 1238 [pdf page 30] ات شایکه - بکر ‎at‏ و فتح کاف .لام خاریست که صمغ آلرا عنزروت خوالند و در مرهمها یکار برند. شابورد ۱  بر وز
30 printed~ 1239 [pdf page 31] شب افروز  شب افروذ = ‎cl see‏ که جربی قمر خوالند چه شب ازو فروزان و دوشن میگردد - و کرم شب تاب را ليز کوبن
31 printed~ 1240 [pdf page 32] -۲۸۱ ۱ چارپابان و کوسفندان را نیز گویشد که شب در آنجا باشند ۱ - و ‎gin‏ اول جا ‎ling‏ راعی باشد که کوسفندا
32 printed~ 1241 [pdf page 33] شب پره ‎opus‏ و شب پر له ‎che‏ ‏که مرغ عیسی باشدوبمربی خفاش خوانند. کوبندچون‌ار را بکشند وبرزها رکودکان پش
33 printed~ 1242 [pdf page 34] سم) ۷ اح  خوانند؛وباین معنی‌بکراول وئألی‌هم آمده‌است.  شب ‎eo‏ وزن مهتاب " ماه را کوبند و بعربی قمر خوالند
34 printed~ 1243 [pdf page 35] اقب در ‎ole‏ دادث  شب در ‎ole‏ دادن - کنابه از وعده کردن و خامن دادن باشد اعم از آنکه کفب با پیشتر ‎oles‏ 
35 printed~ 1244 [pdf page 36] ۷۲]  شبر نگ ۱ ‎p=‏ وزن خرچتگه » دام اسب سیاوش بوده ‎eee‏ ره بزردی ‎ule‏ - و فام مکی است سیاه و آرا شبه کوب
36 printed~ 1245 [pdf page 37] مردم را بشهر بازآورد ؛ چون نزديك رسید شب در آمد و راء کم کردند . پس بفرمود تا آتش بیاری بر افروختند و مردم
37 printed~ 1246 [pdf page 38] پاع) ات  بمعنی آشیان است که جا ‎pling‏ مرغان باشد. شیگو ۱ - با اف فارسی و واو مجپول بروزن بدکو » فام مهتر 
38 printed~ 1247 [pdf page 39] شبوز  شیور ۱ ۰ بنتع اول و ضم انی مشدد وسکون واو و رای قرشت (۱) بمعنی 22980 اس ت که نفیر باشد و بسربی نیز ه
39 printed~ 1248 [pdf page 40] ۱۲۸  و سقوطر جزیرهایست ‎Chap‏ بسواحل یمن ۱ - و ام مسجونی هم هست که آنرا در شب خورند وخوابند ۴ . شبیاز ه ۴
```


## [2026-09-06T22:40:13.641Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\npython3 - <<'EOF'\ntxt=open('BQT_v3_pages.txt',encoding='utf-8',errors='replace').read()\npages=txt.split('\\f')\nimport re\nfor kw in ['شبدیز','شبسنان','شبستان','شبگیر','شباهنگ','شبرنگ']:\n    print('##',kw)\n    for i,p in enumerate(pages[:80]):\n        if kw in p:\n            print('  leaf',i,'printed~',i+1209)\nEOF"
}
```


### [2026-09-06T22:40:15.282Z] TOOL RESULT

```
## شبدیز
  leaf 34 printed~ 1243
  leaf 35 printed~ 1244
## شبسنان
## شبستان
  leaf 33 printed~ 1242
  leaf 35 printed~ 1244
  leaf 36 printed~ 1245
## شبگیر
  leaf 37 printed~ 1246
## شباهنگ
  leaf 31 printed~ 1240
## شبرنگ
  leaf 35 printed~ 1244
```


## [2026-09-06T22:40:21.125Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\npython3 - <<'EOF'\ntxt=open('BQT_v3_pages.txt',encoding='utf-8',errors='replace').read()\npages=txt.split('\\f')\nfor i in (19,20,21,22,23):\n    print('#### leaf',i,'printed~',i+1209,'####')\n    print(pages[i][:2000])\nEOF"
}
```


### [2026-09-06T22:40:23.962Z] TOOL RESULT

```
#### leaf 19 printed~ 1228 ####
[pdf page 20]
ATTA

‎SL‏ ۱ » بروزن قالی. شلتوفرا کوشد
که برنج از پوست برليامده ‎wth‏

‎HY JL‏ » با ‎alist‏ بالف کنیده
‎cds‏ بای حطی ‎SaaS MIE»‏ برنج‌زار

‏باشد .0

‎CLL‏ با میم بالف کشیده و خای
تقطمدار (۱)ساکن » نام بوعی ازغله است‌ودانهای
‎oT‏ بفایت کوچك میباشد - وسینه‌بند زنالوا لیز
کوبند.و آن‌پارچدای باشد که زنان پستانهای‌خود
را ‎was oly‏ ۴ .

‏شاماخچه ۴ ‎et phe‏ فارسی »
‎gees‏ دوم شاماخ است که سینه‌بند ‎QU;‏ باشد.

‏شامار با رای بی‌نقطه بر وزن ‎Nk‏
‏ام موضعی است که کروهی از کبران درآن‌توطن
دارند؟ ؛ و باين معتی‌با زای نقطه‌داربروزن آواژ

‏آمده است .

‎Sku‏ « بروزن چالاك ۰ جامةٌ کوچکی
)4( چك : وخا .

‏را کون دکهمردم دررفت کار کردن پوعتصوسیته
بند زباترا هم گنته اند 9 .

‏شاما کچه ۱ ® بر وزن و ‎we‏
‏شاماخجه است که سیثه بند زهان باشد .

‏شاها کی ۷ بروزن ‎SNe‏ سینه
بند زان ‎wath‏

‏شامس ‎oS‏ بکس میم وسکون سین
بی‌شقطه . نام یکی از جزایر بودان است؛وباشین
نقطهدار هم‌آمده است.

‎°

‎the ‏وزن داموی‎ no Sn gald
Ab ‏بلدی است از بلاد بونان ؛ و بستی گوبند‎

‎+ cole po
‏شاهه = بروزن جامه ۰ مقتمه ورویاکی‎
. ‏باشد که زدان بر سر کنند‎

‏شان » بر وزن ‎ME sob‏ زبور صلرا
کوبندکه درآن ‎Le‏ باشد*۱ - و ‎le dies‏
مقید است که از هندوستان آورند - و مشقف

‏۱ - سانسکریت ‎Shali‏ (برنج وغلات مشابه آن) « وبلیامز۱:۱۰۹۸» درمازسران زراعت
‎oy‏ را «شالی» کوبند . «فرهنگهنظام». ‏ ۴ -رله:شاماخچه»شماخ. وقس:شماخیه«جهانگیری».

‏ورك : شا .
شاماکچه )0( = شماخچه «جهانگیری» .

‏شاماخج » شاماخچه , شاماکی . ‎٩‏ = شاماخجه ‎Cem)‏

‏۴ از : ‎cue‏ (هم.) +-چه ‎igs)‏ تصفیر) = ساماخچه ۶ ساما که .
۴ - ظ.مصحف «شابهار» («م.) .

‏6 رد :
۷ از : تاماك-ی ‎(os)‏

‎OT ‏در مجمع الجزایر | دارای ۷۱۰۰۶ سکته و‎ slp ‏جزیره‌ای‎ ‘Samos= A

‏موطن فیثاغوری بود :

‎. ‏بکی‌شهربار اندرو شادکام‎ le ‏یکی شهر شامس‎ nk

‏عنصری بلخی. ‎cd?‏ فری ۲۰۵ ‎٩‏ -

‎: wld, ‏نیز 51185 513202 «رحدت»‎ ta Sy ole  .یماش‎ tr ٩

‏زبد گر ‎abs Ss‏ تومذرشز آفربنش له

‏که ممذورست ومارا ‎cat‏ چون دحل‌عل شاش.

‏« خاقانی شروانی ۲۱۸ .

‏# شام - اوستا - ‎xshafniya‏ » پهلوی ‎sham‏ (غذای شب) «تاوادیاه>۱«اونوالا

‏۹ , کردیع 510800 (عصرءشب ) ‎ShOme gist.‏ (زمان فاصله بين لیمشب
#### leaf 20 printed~ 1229 ####
[pdf page 21]
شاد ۲۳۰ ات

شا له ۱ = بروزن ‎le‏ معروفت‌وآن

چیزی باشد که از چوب
و غیره سازاد و بدان‌رش سس
رزلف و کیو راپردازدهند ‎ABBE‏
‏سوافزاریاست جولاعگایرا
که تارهای‌رسمان رااز ‎OT‏ شانه(سه‌فم)
‎asta‏ بمنواییکه در وقت بافتن دونار ییکجا
و پپلوی هم واقع نشود -
و بمعتی شان ‎Jee‏ و ‎BS‏
‎yy‏ هپهست ۷ - ‎cary‏
‎pty‏ اسب رالیز کویند -
واستخوان کتفراهم‌میگوند.
‎als‏ سره ‎anus‏ شانه سر
راگویند» وآن پرنده ایست معروف ۸ .

ایثان هم هست که ضمیر جمح غایب باشد ۷ -
ودر عربی ۴ بمعنی قدر ومرتبه وش وکت‌وعظمت
- وحال وفکر والدیشه و کاروبار باشد - و بیم
داه شتن از چیزی را هم گویند - و کاهی بجای
‎bid‏ حق عم گنته میشود چنانکه میگوبند « این
‎aT‏ در ‎ols‏ او ‎Jul‏ شده است» یمنی در حق او
آمده است

‎BL‏ ۴ - بر وزن ‎ails‏ » یعئی زلت
وکا کل را شاه کند .

‏شاندن ‎pe‏ وزن ماندن . بمعنی شاله
کردن باشد ۴ - ومشفف ‎Quiles‏ و شالیدن هم
هت 6 .#

‎Hi‏ ه بر وزن اوك ۰ سنکه دان
‎ory‏ دان مرغارا کوشد .

‏- پهلوی حم 0 - پارسی‌باستان ‎sham‏ «اسشق ۰.۷۹۹ درفارسی «شان»م رکب

‏است از وه .+ ون جمع‌آن 0 ‎als)‏ : مان ‎von‏ «هوبشمان ۰۷۰۹ . رله: ‎Sedge‏

‎je bela‏ . - (عر) «شأن ‎cal‏ « کاروحال . ‎Os?‏ جمع ... وجست وجوی

‏وجستن ودربافتن وکین - وکردن ‎TUES‏ موجب خوبی‌ورونق حال وکارباشد وخبردادن»

‏«منتبی الارب» . درفارسی بجای شأن . ‎shan‏ تلفظ کنند. خاقانی‌شروانی درفصيدة شینبه پس از
میت مذ کور درح ۰ ‎ate‏ قبل گوید «دیوان خاقانی ۰۲۱۸ :

‏و گرچه‌تحل وقتی‌نوش بارد ‎mts‏ دارد . توآن منک رکه اوحی ربك آمد وحی درشاش.

‏۴ - رك : شالدن.
‎ole - ۴‏ بآب‌وفاروی عدل میشوید فك بدست ظفی جمد مك میشاند .
الوری اییوردی . «فرهنگه ‎Glin‏ .
© - بدسگال تو راجه دارد ‎Ole‏ شانده در دل ز غم ‎Me‏ از تو

‏سوزی‌سمرفندی. «فرهنك ‎Hellas‏

‎Shak yey. 65-2 ‏اروپابی)‎ yas) ‏حند وژرمانی‎ « (ate) 50202 ‏پهلوی‎ - ۱

‏بلوجی ع ‎shandg‏ (قتوی اسب) « ‎geet‏ ۰۷۷۱ , اورامانی ‎SHADE‏ ( دوششیب کوه ) «قد.

‏اورامان ‎Ley‏ = ۷ مد ان( م.) : ۷ - پرنده‌ای از نوع کنجشك دارای منقار
پاربگ و دراز باندام سارسیاه ودارای بکدسته 2 (بشکل ‎(ct‏ پرسر .

‎os fs #‏ - بفتح دال » اوستا ‎xshvash . dasa‏ ,پهلوی ‎shdacdah‏ کردی ع

‎, 9202021 ‏پازد‎ cvye geet? ‏پدبدآمده‎ Gogh? ‏(ن) در ش
#### leaf 21 printed~ 1230 ####
[pdf page 22]
۱۳ ات

شانه‌سر ۱۵ صفیر ‎als‏ سراست که

شانه کاری » ‎at‏ از در آوختن
بکسی باشد یعنی با ‎OT‏ شخص درمقام زدوخورد
‎als‏ .

‎SH‏ پاس ‎gee‏ را کوبند که
جولاهگان بر هر دوسرآن سوزنها محکم سازند
و درپیش خود برپپنای‌کار بت کنند.

‏شانی ۲ © بر ون مانی " زر ودرم ده
هفت ۴ راکویند » ‎Oy‏ در قدیم رایج بوده.

‏شاور ان = بروزن خاوران » ‎Sst‏
‏وولایتی است از شروان ۴

‎OG GLE‏ » بنتح اك و سکون‌زای هوز
و دال ابجد (۱) » خارسفیدی باشد شبیه بدرمنه
‎ce inn rire‏ ای مثلثه ‎wing‏

‏شاوغر = بفتح ‎of‏ نقطه‌دار بر وزن
کاوسر ء ام ‎uy‏ "است از ماوراء النهر که
ساکنان آلجا پیشتر جولاهه باشند وبریکطرف
‎oF‏ ولایت بیابان ریک است که کافران در ‎OF‏
‏مقام دارند ‎٩‏ - و بای رومی را نیز گفته‌اند که
‎pe‏ برادر کوچك کرنا ‎ath‏ وآنرا نای‌روین هم
خوالند . _

‏(۱) چك :- ابجد .

‏۱ - رك: شاله سر .
چون برادرت داد در يك شعر
سنایی غزنوی. «فرهنك ‎«lls‏

‏۴ - «شاوران ‎dad‏ شروان است ...» «حدود ۹۵ .رث:شابران.

‎824۳12 ot ‏»پارسی‎ shahs lp - ۷

‏فری ۱44 ۲ ره : شاپور .

‏شاو فی - بسکون ثالك و دون بتحتالی
کشیده .کپوار» پوش را گویند » بعنی چادری
که بر روی کهوارة اطفال پوشند و بعربی معور
خوانند .

‏شاوود ‏ با راو بروزن ومعتی‌شاپور
است * » و او پادشاهی بود ازآل اشك‌بن‌بافت-
و شخصی را بيز گویند که ‎le‏ عاشق و ممشوق
میالجی ‎ath‏ و ‎GaSe Wyld flag‏ برساند.

‏شاه ۷ © بروزن‌ماه, بمعنی اصل‌وخداوند
‎ach‏ وچون پادشاهان ‎cont‏ بمردمان‌اصل‌وخداوند
باشند ابشان را شاء خوانند - وداماد را یز شاه
‎Su ST‏ شوهر دختر کسی باشد ۸ - و یکی‌از
آلات شطرنج را هم شاه میگونند - و کشت
کردن شاه شطرنج را ‎hi ja‏ و کشت بکسی
‎IT‏ باسطلاح شطرج بازان‌آن است که‌مهره‌ای
از مپرهای شطرنج را درخانه‌ای گذارند که‌بحسب
حرکت آن مپره شاه درخانةٌ اوشته باشدوشاه
خوانند بعنی بر خیز ‎WEN‏ من - و هرچی زکه
‎S97 wT‏ وخوبی بحصب صورت ومعنی از"
امثال خود امتیاز ‎ath‏ همچوشاهباز و شاهرا‌وشاه
کار وشاء کاسه و شاه توت وشاه بالوت وشاه‌تره
وشاء سوار وشاه‌باز و ‎old‏ رود وشاء‌تیر وشاه‌الجیر
و شاءآ لو وامثال آن - وراه کشاده را پیز گوند

‎: ‏(هم)‎ gle oF

‏بهر هشتاد ‎cy‏ چل شالی +

‏؟ ‏ رك : ده هفقت .

‎ca: ‏رك‎ _ ۵

‏« بارتولمه ۵۵۳ > . شاه کلمه ایست متعلق بزبان جنوب غربی
#### leaf 22 printed~ 1231 ####
[pdf page 23]
که ازآن راهپا وشمبها جدا شود - وفام‌جالوری
‎col‏ در هندوستان - ‎ply‏ جامه‌ای و پارچه‌اییست
که از هند آورند - و بزبان عریی کوسفند را
کویشد ‎lity‏ جمع آدت ۰۱

شاهاب ؟ » بز وزن. دایاب : رنگه
سرخی باش دکه ‎Ls je‏ اول از کل کاژیرء کشند

شاه اسپرغم ؟ ‎leu ya jan a‏
راکویند و آنرا بعربی خیمران خوانشد ‎BaF.‏
‏ضیمران پیش از زمان انوشیروان لبود . روزی
آوشیروان بدبوان مظالم نشته بود وبارعام‌داده»
مار بزرکی اززیر تخت او برآمدچنانکه‌حاضران
را از دیدن او خوف بهمرسید قسد او کردددمنك
فرمود : « بگذارید شابد طلامه‌ای داشته ‎Cash‏
‏بر اثر او برفتند بکنار چاهی رسیدند . مار بر
کنار چاء حلقه زد (۱) ‎AIT.‏ بدرون رفت وبر
‎aT‏ . چون درآن چاه دگاه کردند ماری دید لد
مرده افتاده وعفربی لیش برو بند کرده » لیزهء‌ای
ازبالای چاه برپشت آن عقرب فرو بردندوهه‌چنان
پنزديك مك آوردند , واز حال هار ولیشعقرب
ملك راآ گاه گردانیدند . چون یکال بگذشت
‎e‏ در آن روز ملك شسته ‎ay‏ ودیوان مظالم
می‌پرسید (۲) 6 همان مار بنزديك‌سربرملك آمد
و از دهن خود قدری تخم ‎clam‏ بریخت وبرفت.
‎SS‏ فرمود آن‌نشم را کاشتند » ازآن شاب
اسپرغم بر آمد و انوشیروان پبوسته ز کام داشت
ازبویدن و خوردن ‎oT‏ برطرف شد ۴ ,وخواس
‎shay oT‏ است خصوصاً رعاف و بواسیر خولی‌راء

(۱) چش : زد .

. ‏چك : می‌برسید‎ (y)

lye

و اگر قدری از تخم آن با شکر بسابند وبزیر
بغل مالند بوی بغل را ‎Gaby‏ سازد .

شاه اسیر ۵ * » همان تاءاسپرغم‌است
که ربحان و خمران باشد.

شاه اسپر هم ۷ باها .بروژن‌ومعنی
شاء اسپرغم است که ربحان باشد.

شاه اسفرهم ۲ - بافا بر وزن
ومعنی شاه اسپرهم است. ۱

شاه اسر - بفتح همزه و سکون فا
و سین بی ‎hi‏ (۳) مفتوح برای قرشت زده »
‎deel‏ گویند و آنرا بعربی اکلیل‌الملك
خواند ۸ .

شاه ‎el‏ = بکر ثالث » کنایه از
آفتاب عالمتاب است.

شاه انحیر ‎gee‏ از ‎col nil‏
‎Vi,‏ انجیر وزبری هم خوانند.

شاه باز * ‎be‏ بای ابجد بروزن کار
ساز ۰ بازی باشد سفید و بزرکه و پادشاهان با
‎oT‏ شکار کنند ‎UT,‏ بتر کی تموغان خوانند .

شاه ‎Vb‏ 5 بالام الف» بمعنی‌همدوش
است و بتر کی ساقدوش خوانند » و آن شخصی
باشد که بقد و بالا و سن وسال موافق ‎Wath‏
‏قد و بالا وسن وسال کسیکه اورا داماد مبکنند
و او را ‎js‏ مانشد داماد آراسته کرده همراه‌داماد
‎Ue‏ عروی برند .

(۳) چ
#### leaf 23 printed~ 1232 ####
[pdf page 24]
پات شاء خرگاه میتا

شاه بانگ ۱ - بنتم ون و سکون
کاف »گیاهی امت دوابی و آنرا بتازی بنفج
الکلاب خوانند " وممرب آن شاه بانج است.

شاه پر ‎pine FP‏ بای فارسی + مخفف
شاه اسپرم است. وآن ربحانی باشد کوچك‌ب رکه
و عربان ضیمران ‎als‏ .

شاه بسته؟ - بنم بای ابجد وفتح سین
‎op‏ لقطه » درایی است که بعربی اکلرالملك
خوالند .
شاه ‎=f bh‏ بای ایجد و لام
‎gly‏ رسیده و ‎lle‏ حطلی زده * نومی از بلوط

‎Shes‏ مشدد » نام سبزم‌ایست _ پفایت سبز و خرم
و درطعم » الدکی تلخ است ودر دواها کار برند
خصوص جرب و خارش
را نافع است و ممرب
‎oF‏ شیطرح‌باشدوبعربی
بقلةالملك خوانند .
شاه تیر -
بافوقالی‌بر وزن‌باد گیر ۰
چویی بز رکه باشد که
‎Gi.‏ خاله را بدان

‏پوشند . شاه تره
شاه ‎be ۷ gle‏ جیم بالف کشیده بر

‏سموم را ‎GU‏ است وزن عادبان » نام ولایت مروباشد,ومروشیرست

‏ومثاله راسود ‎tans‏ قدیم از خرامان ‏

‏و آنرابعربی‌بلوط- شاه چینی ‎he‏ جیم فارسی ‎doing‏

‏الملك . و برومی چینی » صار؛ کیاهی است چینی ؛ و بعضی

‏قطل (۱)خوانند. ‎ST‏ حنای آنجا را با سرکه مسرشند
شاه بوی- و آلرا شاه ‎gue‏ میگوبند . طلاکردن ‎OT‏ درد

‏بروژن‌مامروی» بمعنی شاه بلوط سر وا ببرد .

‏شاه خاور - بکس ‎at‏ ۰ کنابه از
خورشید است .
شاه خرگاه میتا - بمعنی‌شاه خاور

‏است که کنابه از خورشید باشد .

‏عنبر است؛ بسنی کویند که آن از کاوبهم‌میرسد
چنانکه مك ازآهو ؛ و بضی کوبند موم صل
‎gk»‏ است ۵ .

‏شاه آره ۱ ‎poe‏ فوفالی و رای بی

‏(۱) چك : تطل . رد : قطل .

‏اسر دابانگ - مصحف‌ | مخفف «شاه سیرم» ( ۰۵ ۰) ‎(dle st) ans Boe‏ وراه :
شاه افر. ۴ شاه بالوت (رك : شاه درهمین کناب) , پهلوی )58۳0810 «اوبوالا۱۵۳» .معرب

‏آن هم «شاء بلوط» «تنی» ‏ ۷656۵ ‎Castanea”‏ » تابتی ‎VAN‏ ؛ درختی ازدستةٌ بلوطهاء

‏کلهای ‎OT BL‏ سه‌تابی وتشکیل سه‌میوه میدهدکه در پیاله‌ای خار دار قرار گرفته و خوراکی

‏است ‎PHT IS?‏ ۷۷۷ . 6 - «شاه بوی » عبر باشد .رودکی (سمرقندی) گوبد :
بی قی.ت است شکر ازآن دولبان اوی کاسد شد از دو زلفش بازار شاه بوی.»

‎+ ‏فرس ۱۹ © ورگ : خرده اوستاص6ع ۱ح ورك : عنبن‎ cal?

‎Fumaria = ‏وتیطرج‎ ٩ ‏شیتره.ممرب‌آن «شاه‌ترج» «دزی‌جاص 0۲:۷۱۷*نضس‎ J

‏ازتیرث نزديك بکو کناربان, دارای کلهای نامنظم وب رکپای‌بربده است که چون بادست لرم کنند
بوی درد میدهد . « ک
```


## [2026-09-06T22:40:32.975Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\npython3 - <<'EOF'\ntxt=open('BQT_v3_pages.txt',encoding='utf-8',errors='replace').read()\npages=txt.split('\\f')\nfor i in (30,35):\n    print('#### leaf',i,'printed~',i+1209,'####')\n    print(pages[i])\n    print()\nEOF"
}
```


### [2026-09-06T22:40:34.539Z] TOOL RESULT

```
#### leaf 30 printed~ 1239 ####
[pdf page 31]
شب افروز

شب افروذ = ‎cl see‏ که
جربی قمر خوالند چه شب ازو فروزان و دوشن
میگردد - و کرم شب تاب را ليز کوبند - و نام
ماه دهم است از مال ملکی .

شبالنگ = بفتح لام وسکون ‎IE yy‏
فارسی ۰ نخچیر (۱) را کوبند و ‎oT‏ جانورانی
باتند که آنها را شکار کنند مانند آهو و قوچ
سحرایی وبز و کاو کوهی وامثال آن.

شبان ۲ ‎ene‏ اول و الی بالف کشیده
وبنون‌زده » چویانرا کوبند که چراننده ومحافطت
کننده کوسفند باشد و اورا ‎eats‏ راعی خوانند؛
و باینمعنی بفتح اول شهرت دارد و درست است
- و ‎dsl ch‏ شب پره را کویند و آنرا مرغ
عیسی هم خوالند - و جمع شب هم‌هست که‌شبها
باشد لیکن برخلاف ‎old‏ .

شب آنبوی ۴ ‎cee‏ او و سکون
نون و بای ابجد ‎gly‏ رسیده و بتحتالی زد», گل
شب بوی ‎ath‏ وآن زرد رنگ میشود و بعربی
منئور خوانند بضم ثای مثلثه .

. ‏نخجیر‎ : ote )۱(

ی

شبان قر یب - ام مرغیت ‎tS‏
‏شبیه بباشه و بسی کوبند شبیه بفراشتروك است
- وبسنی مرغ عسی را شبان فريبك خوانند ۴.
مجمللاگویند چنان بروی زمین‌شیند ‎PS‏ کس
او را ‎ate‏ پندارد که قوت برخاستن و بربدن
ندارد وهمین که پیش اوروند پرخاسته اندگراهی
پرواز رکند و بازبنشیند وهرچند اینکس پیش‌رود
او چند ‎pad‏ پرواز کند وبنشیند .

شبان قر ییک ۴ » همان شبان‌فریب
است که مرغ کوچك شبیه بباشه باشد.

شبان‌فر بو * « با واو . بروزن‌ومعنی
‎ols‏ فرب است که پر ند #بان بازی ده‌باشد.

شبان فر 39 ۲ با واو » بر وزن
و معنی شبان فربيك باشد.

شبا نکاره = با کان بالف کشیده وفتح
رای قرشت » ولایتی است ازفاری ۷ - ونام دهی
است از ‎Vy‏ طوی.

شبا نگاه 4 با کاف فارسی بر وزن
جهاشاه, به‌عنی درآهدن شب باشد ‎٩‏ -وجایگاه

۱ - پهلوی ‎shupan‏ .ابرانی ‎ofshu_pavan_ ott‏ «نب ‎cry oS‏ ارمنی ع

6 (ارستا - 2210 . تات[۵۶5), کردی 512۷۵۲ . ‎us!‏ 520۳ (چریان) ,5۳22021
) چویان‌بسر). بلوچی ‎shipank‏ و 5۳02۷۵۵ , ‎Shafank‏ » وخی ‎shpiin‏ ر ‎shiipiin‏
‏هرن چوپان و ‎Olt‏ را از ‎eh‏ ربشه میداند ولی هوبشمان آنرا جدا میشمارد « اسشق - هوبدمان
۰ ور : هرن «اسفا ۱ :۷ص ‎doy OVA‏ شوان ‎hye‏ ۴ - از : شب(- البوی ( از :
ابویدن زهم) = شب بوی (ه.م) ۰

۴ = شبان فربورك » شبان ‎ty dy slim ۴ dep‏ شبان فربب .

Cpa) deg ols ٩ Gee) ‏فرب‎ ole ©

۲ - ناحیتی از دشتستان فاری ۰ بطول 4۰ وبعرض ۲8 کیلومتر . ازشمال ومفرب محدوو
است به‌اهور میلاتی وحیات داود و از مشرق به زیره و دالکی وازجنوب به انگالی » مصول‌آن
غلات‌وخرما: مر ‎OTT‏ ده کهنه (4۰۰ خانوار) و ‎۷٩‏ فربه دارد .«جفراةیای سیاسی. ‎ANDES‏

‎A‏ - هرن «ن > را در ‎Gy shor‏ و «بانگاه» و « شبان بوی» و > شبان ور » اثر تلفظ
قدیم ‎xshapan. ty!)‏ = شب) میداد «اسشق ‎٩۷۷۵‏ ( رك : شب ) وممکن است الف ونون
چمع ‎٩ wath‏ - کاء ( پسوددازمان )است : «شبانگاهی که دزدان باز آمدند ...نختن

‏دشمتی که درس ایشان ناختنآورد , خواب‌بود .۲ « گلستان ‎LEVY‏


#### leaf 35 printed~ 1244 ####
[pdf page 36]
۷۲]

شبر نگ ۱ ‎p=‏ وزن خرچتگه » دام
اسب سیاوش بوده ‎eee‏ ره
بزردی ‎ule‏ - و فام مکی است سیاه و آرا
شبه کوبند . چون ‎Ty‏ نهند بسوزد و بوی
قط ‎RS‏ ۱

شبروآن ۴ - کنابه از ثب بیداران
و سالکان باشد - و کنایه از عس و دزد و عیار
هم هنت .

شبست = بکر اول و الی وسکون‌سین
بی نقطه و فوقالی ۰ چیزیرا گوبند که بر طبع
کران و داخوش‌آید ؛ وباين ‎gine‏ باشیننقطه‌دار
هم بنظرآمده است و با زشت ‎aii‏ کرده‌اند ۴
و این هم درست است چه در فارسی سین بی‌لقطه
ونقطه‌دار بهم تبدیل می‌بایند.

شبستان * » ‎iar‏ ثب خاله است که
حرم ‎cle‏ پادشاهان و خلونخانه و خوایگاه
ملوك وسلاطین پاش ودر مساجد شبستان‌جایی را

(۱) چك

ارمائل - (0) چش

a ‏شب‎

کوبند که دروشان وفیر ‎ole!‏ در آن عبادت

کنند ‎ety‏ لیز باب روند.

UE pty yt iG ٩ ‏سده‎ vom
‏چهسده‌بمعنی‎ ath ‏بمعنیآتش بلند‎ » Sank ‏و دال‎
‏شب دهم بهمن ماماست‎ OT ‏آش بلند است ۷ و‎
‏اين‌آن است که چون فردون بر‎ Lat ‏و وجه‎
as ‏وخدم ونزدیکان او را‎ cdl ‏ضحاك دست‎
0 ‏طباخی داشت ارمائیل‎ abe oT ‏میکشت از‎
com ‏نام که مردمانرا کنتتی و مفز سرایشان را‎
cet Opts pope ‏بیرون کردی‎ dws ‏ماران‎
‏خواست که اورا بعقوبت تمام بکشد. ارمائیل(۱)‎
oe ‏گفت هرروز بك کس را از آن دوک سکه‎
(9) ‏میدادند که بکشم آزاد میکردم و درعوض‌او‎
‏مفز سکوسفند داخل می‌نمودم ۰ توباید که‌بامن‎
als as ‏باور‎ Sly ‏معافات یکی بجایآوری‎
‏بکره دماوند برده‌اند . فربدون با‎ ol ‏آن مردم‎
OW ‏لشکر سوار شده متوجه کوه دماوند گردید‎

: آن .
- از : شب ‎Gt‏ ( برنگ شب ‎(ee‏ شبدیز .

۴ - ام اسب ‎dale‏

« بپژاد » است ء ‎only‏ اشتباء ازین بیتهای فردوسی طوسی ناشی شده :

رخش پرزخون دل و دید هگشت
بیاورد شب ‎SO‏ بهزاد . را

وی آخر تازی اسپان بگذشت
که ‎ihe‏ روز کین باد را
« شامنامةً بخ ج ۳ من ۵۳

ومراد ازشبرنگه دربنجاصفت است ‎Colm gine‏ وفردوسی‌چندبارسیاهی اسب‌سیاوش‌اشاره کرده:

یکی ‎Sb‏ بر شته ‎he‏

raw f
‏حاکم‌آمد یکی بقیض وخیشت‎ - ۴

همی‌کرد ملس برآمد بماه .
> شامنامةً بخ ج ۳ ص ‎ool‏

شب رو ‎٩‏ .رگ : ذیل همین حاشیه .

رشکی کنده و پلید که وزشت .
ممروفی بلخی. «لفت فری ‎EA‏

5 - از: شب (-ستان(یسوند ‎«(Oks‏ فس: شب ‎ule‏ (.م.) ۰ 8002-0080(دزنولی)
بمعنی زیرزمین » ‎MGS‏ تاستالی » پپلوی ‎Shapastam‏ (حرم شاهی) «اونوالا ‎SAVVY‏
‏ازآنگه که تابم شد اقبال اورا (بالغ شد اقبالش او را)

‎oye‏ ظفر در شبستان نماید.
۷ اشتعاق

‏1 رگ : ‎te‏ سده.

‏«خاقالی شروالی*۱۳بامقابلدخ».
عامیاله . رك : جشن سده .

‏# شب‌رو - بفتح اول وسوم , از : شب رو ( رونده ) ؛ آنکه در شب راه رود -دژد

‏وعبار . رك : شبروان ( متن ) .
```


## [2026-09-06T22:40:52.432Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\npython3 - <<'EOF'\ntxt=open('BQT_v3_pages.txt',encoding='utf-8',errors='replace').read()\npages=txt.split('\\f')\np=pages[34]\ni=p.find('شبدیز')\nprint(p[max(0,i-1500):i+2500])\nEOF"
}
```


### [2026-09-06T22:40:54.137Z] TOOL RESULT

```
[pdf page 35]
اقب در ‎ole‏ دادث

شب در ‎ole‏ دادن - کنابه از
وعده کردن و خامن دادن باشد اعم از آنکه
کفب با پیشتر ‎oles‏ باشد ۱ .

شید یز ۴ = بادالابجد بروزن‌مهمیز»
تم اسپ (۱)خسرو پرویز بوده. گویند رنگه ‎OT‏
‎ake‏ بود و وجه نمیا ‎OT‏ شب رنگه است چه
‎po‏ بممنی رنگه باشد . گوبتد از ‎Obl dae‏
جهان چهار وجب بلندتر بود (۲) وآنرا از دوم
آوردء بودند ۴ » و ‎ate gS gam‏ شبدییز و گلگون
هردو از يك مادیان بهم رسیده‌اند و حقیفت ‎OT‏
‏در لفت کلگون من کور است » و چون اورا سل
بستندی باه میخ بردست وپایش محکم کردندی
‎py‏ طمامیکه خمروخوردی او رای زخورالیدددی»
و چون شبدیز پمرد خسرو او ‎Ny‏ ودفن کرده
صورت او را فرمود که بر سنگه هش کردند
‎SW py‏ بدان نگرستی بگرستی و صورت
شبدیز که خسرو بر ‎oT‏ سوار ‎are‏ در ‎OLS‏
‏است ؟ .

شبد یز نقره ‎ale =e ES‏ ازآسان

است - وکنابه از شب وروز ‎Sy‏ ونهار -وزمانه

وسلنلص

شب یر ه با ذال نقطه دار بر ‎Ob)‏
‎james‏ (۳).نامی است از اسماء ‎cyl!‏ جل‌جلاله؛
و باين ممنی بجای حرف‌ثابی بای حطی هم‌آمده
است ۵ .

شیر - بفتح اول و ‎yl‏ و سکون رای
فرشت » ‎es‏ آش را کوبند - و بکر ارل
و سکون ثالی و قالك » نام شمربن ذی الجوشن
است لمنةافعلیه ۷ - و ‎eee‏ وجب بدست را
کوبند وآن از دست مقداری باشد ماین‌انگشت
کوچك ‎ly‏ بز رکف .

شبرغان ۷ - بتم ‎elt‏ و ‎od‏ قطمدار
بالف کشید. بر وزن مردمان * در قدیم‌الابام دام
شپر بلخ بوده و درین وقت دام قصبه ایست ترديث
ببلخ مشهور بشبرقان بروزن نمکدان .

شبرم 4- بکر اول وسکونالی‌وفتح
ثالت و میم ساکن ‎al‏ است شیردار و آن
پیشتر در صحراها وکنارهای جوبها رود ‎Ky,‏
‎GL‏ آن برخی ‎bh‏ است. گوننداگر کاوآلرا
بخورد بمیرد و ‎atin gS‏ را مضرت ر-اند وآترا

وروزکار - وعالم ودیا هم کفته اند 5 ۱

‎ge )۱(‏ » چش : اسب .

‎. ‏چك : بوده‎ (x)

‏بشیرازی کاو ‎dhs‏ خوانند.

‏(۳) چش : لشخجیر .

‎٩‏ - دانی که خال برچه سیمین او چراست»
‎OTF‏ سیم اکر دهد بتو شب ‎Olay‏ دهد . ۰

‏۴ - از : شب ۲ دیز . رگ : دیز .

‏ظهیر فاربايی . «فرهنکه ‎felis‏

‏۴ - آفرین زآن م رکب شبدیز سل رخش روی

‏اعوجی ‎Gok‏ و آن مادرش را بحموم شوی .

‎. ٩۱۱۰ ‏دامفانی‎ sere?
. pho ‏رك : شیذر‎ ۵
am ۷

‏۴ - ظ.طاق بستان- ورك ‎dys‏ شبدیز .

‎. ٩ ‏مصحف « شیر‎ BLT

‏شبرقان ‎pe‏ اول وراه مضوم » شهرست آباد و پرجممیت ‎tho gy‏ بلخ وبین‌آن

‏دو يك یا دو روزه ‎cul ly‏ وآنرا « شفرفان » هم کنته اند » . > معجم‌البلدان > .
۸ -ثبرم بضم اولوسوم درمربی = ‎Euphorbia Pityusa‏ ( باهدرختی است‌خاردار)

‎ATIVE! ‏ج ۱ص‎ obo? Cpurge=
```


## [2026-09-06T22:41:06.405Z] TOOL CALL #41: Bash

```json
{
 "command": "python3 tools/fetch_source.py --help 2>&1 | head -20"
}
```


### [2026-09-06T22:41:08.352Z] TOOL RESULT

```
Save a web source used during verification, for later cross-checking.

    python3 tools/fetch_source.py <URL> [--note "why it was fetched"]

Downloads the URL, converts the HTML to plain text, stores it as
data/verification/sources/web/<sha1(url)>.txt and appends a line to
data/verification/sources/web/index.jsonl  ({url, file, fetched, bytes, status, title, note}).
Prints the stored path. Re-fetching the same URL within a day is skipped.
```


## [2026-09-06T22:41:13.213Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/k%CA%B7reyh%E2%82%82-\" \\\n \"https://en.wiktionary.org/wiki/%D8%AE%D8%B1%DB%8C%D8%AF%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%D8%B4%D8%A8\" \\\n \"https://en.wiktionary.org/wiki/%D8%B4%D8%A7%D9%85\" \\\n \"https://en.wiktionary.org/wiki/%CE%A0%CF%81%CE%AF%CE%B1%CE%BC%CE%BF%CF%82\" \\\n \"https://www.etymonline.com/word/Priam\" ; do\n  python3 tools/fetch_source.py \"$u\" --note \"page 299 (Kwri/Kwsep) verification\" 2>&1 | tail -2\ndone"
}
```


### [2026-09-06T22:41:20.739Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/c12a7f7ca6cf7e70.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/673d0011d8bab269.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/94bf850236a386e7.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/00d45c892a7b0e34.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b2b1e4cae4c0a538.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/eba8fe43f427b59c.txt
```


## [2026-09-06T22:41:23.242Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"########## PIE kʷreyh2 ##########\"\nhead -c 3000 c12a7f7ca6cf7e70.txt\necho\necho \"########## خریدن ##########\"\nhead -c 2500 673d0011d8bab269.txt"
}
```


### [2026-09-06T22:41:23.292Z] TOOL RESULT

```
########## PIE kʷreyh2 ##########
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/k%CA%B7reyh%E2%82%82-
FETCHED: 2026-09-06T22:41:16Z
STATUS: 200
TITLE: Reconstruction:Proto-Indo-European/kʷreyh₂- - Wiktionary, the free dictionary

Reconstruction:Proto-Indo-European/kʷreyh₂- - Wiktionary, the free dictionary 

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
 Proto-Indo-European 

 Toggle Proto-Indo-European subsection 

 1.1 
 Root 

 1.1.1 
 Derived terms 

 1.1.2 
 Descendants 

 1.2 
 References 

 Toggle the table of contents 

 Reconstruction:Proto-Indo-European/ kʷreyh₂- 

 Add languages 

 Reconstruction 

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

 *kʷreyh₂- [ 1 ] 

 to buy 

 Derived terms
 [ edit ] 

 Terms derived from the Proto-Indo-European root *kʷreyh₂- (15 c, 0 e) 

 *kʷréyh₂-t ~ *kʷrih₂ént ( root aorist ) 
 Proto-Balto-Slavic: 
 Proto-Slavic: *kriti 

 Proto-Tocharian: 
 Tocharian B: käryā- 

 *kʷri-né-h₂-ti ~ *kʷri-n-h₂-énti ( nasal-infix present ) 

 *kʷrih₂- 
 Proto-Hellenic: 
 Ancient Greek: ἐπριάμην ( epriámēn ) 

 *kʷrih₂-tó-s 
 Proto-Indo-Iranian: *kriHtás 
 Proto-Indo-Aryan: *kriHtás 
 Sanskrit: क्रीत ( krītá ) 

 Unsorted formations 

 Proto-Tocharian:
 Tocharian B: käry- [ 2 ] 

 Descendants
 [ edit ] 

 Sanskrit: क्री ( krī ) 

 References
 [ edit ] 

 ^ Rix, Helmut , editor ( 2001 ), “*k u̯ rei̯h₂-”, in Lexikon der indogermanischen Verben [ Lexicon of Indo-European Verbs ] (in German), 2nd edition, Wiesbaden: Dr. Ludwig Reichert Verlag, →ISBN , page 395 

 ^ Adams, Douglas Q. ( 2013 ), “käry-”, in A Dictionary of Tocharian B: Revised and Greatly Enlarged (Leiden Studies in Indo-European; 10 ), Amsterdam, New York: Rodopi, →ISBN , pages 174-175 

 Retrieved from " https://en.wiktionary.org/w/index.php?title=Reconstruction:Proto-Indo-European/kʷreyh₂-&oldid=92151564 "

 Categories : Proto-Indo-European lemmas 
 Proto-Indo-European roots 
 Proto-Indo-European CReRH-shaped roots 
 
########## خریدن ##########
URL: https://en.wiktionary.org/wiki/%D8%AE%D8%B1%DB%8C%D8%AF%D9%86
FETCHED: 2026-09-06T22:41:16Z
STATUS: 200
TITLE: خریدن - Wiktionary, the free dictionary

خریدن - Wiktionary, the free dictionary 

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
 Descendants 

 1.4 
 References 

 Toggle the table of contents 

 خریدن 

 9 languages 

 فارسی 
 Na Vosa Vakaviti 
 Magyar 
 Bahasa Indonesia 
 한국어 
 Kurdî 
 Malagasy 
 Русский 
 中文 

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

 See also: خزیدن and چریدن 

 Persian
 [ edit ] 

 Etymology
 [ edit ] 

 From Middle Persian 𐫟𐫡𐫏𐫗𐫏𐫅 ( xrynyd ) , [script needed] ( ZḆNN-tn' /⁠xrīdan⁠/ ) , from Proto-Iranian *xrináHti , from Proto-Indo-Iranian *krináHti , from Proto-Indo-European *kʷrinéh₂ti . Compare Sanskrit क्रीणाति ( krīṇā́ti , “ to buy; to purchase ” ) , Irish crean ( “ to purchase ” ) . [ 1 ] 

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /xa.riː.ˈdan/ 

 ( Dari, formal ) IPA ( key ) : [xä.ɾiː.d̪än] 

 ( Dari, formal ) IPA ( key ) : [xä.ɾiː.d̪än] 
 ( Kabuli ) IPA ( key ) : [xä.ɾiː.d̪än] 

 ( Hazaragi ) IPA ( key ) : [xä.ɾi.d̪än] 

 ( Iran, formal ) IPA ( key ) : [xæ.ɹiː.d̪æn] 

 ( Tajik, formal ) IPA ( key ) : [χä.ɾi.d̪än] 

 Rhymes: -an 

 Readings

 Classical reading ? 

 xarīdan

 Dari reading ? 

 xarīdan

 Iranian reading ? 

 xaridan

 Tajik reading ? 

 xaridan

 Verb
 [ edit ] 

 Dari

 خریدن 

 Iranian Persian

 Tajik

 харидан 

 خریدن • ( xarīdan  / xari
```


## [2026-09-06T22:41:27.752Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"########## شب ##########\"\ngrep -n -A25 \"^ Persian$\" 94bf850236a386e7.txt | sed -n '1,60p'\necho \"########## شام ##########\"\ngrep -n -A30 \"Etymology 1\" 00d45c892a7b0e34.txt | sed -n '1,60p'"
}
```


### [2026-09-06T22:41:29.646Z] TOOL RESULT

```
########## شب ##########
1682: Persian
1683- [ edit ] 
1684-
1685- Persian Wikipedia has an article on: شب 
1686-
1687- Wikipedia fa 
1688-
1689- Etymology
1690- [ edit ] 
1691-
1692- From Middle Persian [script needed] ( LYLYA ) , [script needed] ( šp /⁠šab⁠/ ) , from Old Persian 𐎧𐏁𐎱 ( xšap- ) , from Proto-Iranian *xšáfš , from Proto-Indo-Iranian *kšáps , from Proto-Indo-European *kʷséps . Cognate of Sanskrit क्षप् ( kṣap ) .
1693-
1694- Pronunciation
1695- [ edit ] 
1696-
1697- ( Classical Persian ) IPA ( key ) : /ˈʃab/ 
1698-
1699- ( Dari, formal ) IPA ( key ) : [ʃäb] 
1700-
1701- ( Dari, formal ) IPA ( key ) : [ʃäb] 
1702- ( Kabuli ) IPA ( key ) : [ʃäw] 
1703-
1704- ( Hazaragi ) IPA ( key ) : [ʃäw] , [ʃeːw] 
1705-
1706- ( Iran, formal ) IPA ( key ) : [ʃæb̥] 
1707-
########## شام ##########
62: Etymology 1 
63-
64- 1.1.1 
65- Proper noun 
66-
67- 1.2 
68- Etymology 2 
69-
70- 1.2.1 
71- Pronunciation 
72-
73- 1.2.2 
74- Verb 
75-
76- 1.2.2.1 
77- Conjugation 
78-
79- 1.2.3 
80- Verb 
81-
82- 1.2.3.1 
83- Conjugation 
84-
85- 1.3 
86- References 
87-
88- 2 
89- Burushaski 
90-
91- Toggle Burushaski subsection 
92-
--
122: Etymology 1 
123-
124- 4.1.1 
125- Proper noun 
126-
127- 4.1.1.1 
128- Descendants 
129-
130- 4.2 
131- Etymology 2 
132-
133- 4.2.1 
134- Noun 
135-
136- 4.2.1.1 
137- Descendants 
138-
139- 4.3 
140- References 
141-
142- 5 
143- Persian 
144-
145- Toggle Persian subsection 
146-
147- 5.1 
148- Pronunciation 
149-
```


## [2026-09-06T22:41:33.408Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\npython3 - <<'EOF'\nt=open('00d45c892a7b0e34.txt',encoding='utf-8',errors='replace').read()\ni=t.rfind(' Persian\\n')\n# find the Persian language section body\nimport re\nidx=[m.start() for m in re.finditer(r'\\n Persian\\n \\[ edit \\]', t)]\nprint(idx)\nfor j in idx:\n    print(t[j:j+2500])\nEOF"
}
```


### [2026-09-06T22:41:35.022Z] TOOL RESULT

```
[12196]

 Persian
 [ edit ] 

 Persian Wikipedia has an article on: شام 

 Wikipedia fa 

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /ˈʃaːm/ 

 ( Dari, formal ) IPA ( key ) : [ʃɑːm] 

 ( Dari, formal ) IPA ( key ) : [ʃɑːm] 
 ( Kabuli ) IPA ( key ) : [ʃɑːm] 

 ( Hazaragi ) IPA ( key ) : [ʃɔːm] 

 ( Iran, formal ) IPA ( key ) : [ʃɒːm] 

 ( Tajik, formal ) IPA ( key ) : [ʃɔm] 

 Rhymes: -aːm 

 Readings

 Classical reading ? 

 šām

 Dari reading ? 

 šām

 Iranian reading ? 

 šâm

 Tajik reading ? 

 šom

 Etymology 1
 [ edit ] 

 Inherited from Proto-Iranian *xšáfnyah , from *xšápā or *-yah .

 Noun
 [ edit ] 

 شام • ( šām / šâm ) ( Tajik spelling шом ) 

 dinner , supper ( evening meal ) 
 برای شام چی داریم؟ ( more literary ) ― barâ-ye šâm či dârim? ― What do we have for dinner ? 
 شام چی داریم؟ ( more colloquial ) ― šâm či dârim? ― What do we have for dinner ? 

 ( archaic ) dusk 

 ( archaic ) evening 
 Synonym: عصر ( 'asr ) 

 Related terms
 [ edit ] 

 شب ( šab ) 

 Descendants
 [ edit ] 

 → Azerbaijani: şam 

 → Gujarati: شام ( shām ) 

 → Hindustani: 
 Hindi: शाम ( śām ) 
 Urdu: شام ( śām ) 

 → Khalaj: şâm 

 → Ottoman Turkish: شام ( şâm ) 
 Turkish: şam 

 Etymology 2
 [ edit ] 

 Borrowed from Arabic الشَّام ( aš-šām ) .

 Proper noun
 [ edit ] 

 شام • ( šām  / šâm ) ( Tajik spelling Шом ) 

 Levant (a cultural region of West Asia consisting of the eastern Mediterranean countries, i.e. Syria , Lebanon , Palestine , Israel , Jordan and Cyprus ) 
 c. 1260s , Jalāl ad-Dīn Mohammad Rūmī , translated by Reynold A. Nicholson , مثنوی معنوی [ Masnavi-ye-Ma'navi ], volume III, verse 89: سوی شامست این نشان و این خبر / در ره قدسش ببینی در گذر suy-e šâm -ast in nešân o in xabar / dar rah-e qods-aš be-bini dar gozar This sign and this information lies in the direction of Syria : you will see it as you pass on the way to Jerusalem. 

 Damascus (the capital city of Syria ; an ancient settlement, the ancient capital of various polities, most notably the Umayyad Caliphate from 661 to 744 CE and Aram-Damascus , existing from the 12th to 8th centuries BCE ) 
 Synonym: دمشق ( damešq ) 

 Descendants
 [ edit ] 

 → Urdu: شام ( śām ) 

 Punjabi
 [ edit ] 

 Pronunciation
 [ edit ] 

 ( Standard Punjabi ) IPA ( key ) : /ʃäːm/ 

 Etymology 1
 [ edit ] 

 Etymology tree

 Proto-Indo-Iranian *kšápā 
 Proto-Iranian *xšápā 

 Proto-Iranian *-yah 

 Proto-Iranian *xšáfnyah 
 Classical Persian شَام ( šām ) bor. 
 Punjabi شام 

 Borrowed from Classical Persian
```


## [2026-09-06T22:41:41.501Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\npython3 - <<'EOF'\nimport re\nt=open('b2b1e4cae4c0a538.txt',encoding='utf-8',errors='replace').read()\ni=t.find('Ancient Greek')\nj=t.find('Etymology')\nprint(t[j:j+1800])\nEOF\necho \"=========== ETYMONLINE PRIAM ===========\"\npython3 - <<'EOF'\nt=open('eba8fe43f427b59c.txt',encoding='utf-8',errors='replace').read()\ni=t.find('Priam')\nprint(t[:200])\nimport re\nk=t.find('Advertisement')\nprint(t[1000:4000])\nEOF"
}
```


### [2026-09-06T22:41:43.211Z] TOOL RESULT

```
Etymology 

 1.3 
 Pronunciation 

 1.4 
 Proper noun 

 1.4.1 
 Declension 

 1.4.2 
 Derived terms 

 1.4.3 
 Descendants 

 1.5 
 References 

 Toggle the table of contents 

 Πρίαμος 

 7 languages 

 Deutsch 
 Ελληνικά 
 Eesti 
 فارسی 
 Français 
 Malagasy 
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

 Ancient Greek
 [ edit ] 

 English Wikipedia has an article on: Priam 

 Wikipedia 

 Alternative forms
 [ edit ] 

 Πέρρᾰμος ( Pérrhămos ) , Πέρᾰμος ( Pérămos ) — Aeolic 

 Etymology
 [ edit ] 

 From Luwian 𒉺𒊑𒀀𒈬𒀀 ( Pa-ri-a-mu-a- , “ exceptionally courageous ” ) .

 Pronunciation
 [ edit ] 

 IPA ( key ) : /prí.a.mos/ → /ˈpri.a.mos/ → /ˈpri.a.mos/ 

 ( 5 th BCE Attic ) IPA ( key ) : /prí.a.mos/ 

 ( 1 st CE Egyptian ) IPA ( key ) : /ˈpri.a.mos/ 

 ( 4 th CE Koine ) IPA ( key ) : /ˈpri.a.mos/ 

 ( 10 th CE Byzantine ) IPA ( key ) : /ˈpri.a.mos/ 

 ( 15 th CE Constantinopolitan ) IPA ( key ) : /ˈpri.a.mos/ 

 Proper noun
 [ edit ] 

 Πρῐ́ᾰμος • ( Prĭ́ămos )  m ( genitive Πρῐᾰ́μου ) ; second declension ( Attic , Epic , Ionic ) 

 ( Greek mythology ) Priam 

 Declension
 [ edit ] 

 Second declension of ὁ Πρῐ́ᾰμος ; τοῦ Πρῐᾰ́μου ( Attic )

 Case / #

 Singular

 Nominative

 ὁ Πρῐ́ᾰμος 
 ho Prĭ́ămos 

 Genitive

 τοῦ Πρῐᾰ́μου 
 toû Prĭắmou 

 Dative

 τῷ Πρῐᾰ́μῳ 
 tōî Prĭắmōi 

 Accusative

 τὸν Πρῐ́ᾰμον 
 tòn Prĭ́ămon 

 Vocative

 Πρῐ́ᾰμε 
 Prĭ́ăme 

 Notes
=========== ETYMONLINE PRIAM ===========
URL: https://www.etymonline.com/word/Priam
FETCHED: 2026-09-06T22:41:20Z
STATUS: 200
TITLE: Etymonline - Online Etymology Dictionary

Etymonline - Online Etymology Dictionary 

 Search 
 Log in 

 Col
```


## [2026-09-06T22:41:49.553Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\ngrep -n -i \"priam\" eba8fe43f427b59c.txt | head -20"
}
```


### [2026-09-06T22:41:49.657Z] TOOL RESULT

```
1:URL: https://www.etymonline.com/word/Priam
```


## [2026-09-06T22:41:58.555Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n \"https://en.wikipedia.org/wiki/Priam\" \\\n \"https://en.wiktionary.org/wiki/%CF%80%CF%81%CE%AF%CE%B1%CE%BC%CE%B1%CE%B9\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/x%C5%A1%C3%A1f%C5%A1\" \\\n \"https://en.wiktionary.org/wiki/%D8%B4%D8%A8%D8%B3%D8%AA%D8%A7%D9%86\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/xrin%C3%A1Hti\" ; do\n  python3 tools/fetch_source.py \"$u\" --note \"page 299 (Kwri/Kwsep) verification\" 2>&1 | tail -1\ndone"
}
```


### [2026-09-06T22:42:03.672Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/017a6b6fcfbd3fd4.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/05e487d9f04a0b40.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4ec24fac45f1b34d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1e74b143093d08b8.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d97e46a327f8712e.txt
```


## [2026-09-06T22:42:08.056Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"=== WIKIPEDIA PRIAM etymology ===\"\ngrep -n -i -B3 -A12 \"Luwian\\|etymolog\" 017a6b6fcfbd3fd4.txt | head -60\necho\necho \"=== priamai ===\"\npython3 -c \"\nt=open('05e487d9f04a0b40.txt',encoding='utf-8',errors='replace').read()\ni=t.find('Ancient Greek\\n [ edit ]')\nprint(t[i:i+1200])\n\"\necho \"=== PIr xsafs ===\"\npython3 -c \"\nt=open('4ec24fac45f1b34d.txt',encoding='utf-8',errors='replace').read()\nprint('STATUS',t[:300])\ni=t.find('Proto-Iranian\\n [ edit ]')\nprint(t[i:i+1500])\n\""
}
```


### [2026-09-06T22:42:09.905Z] TOOL RESULT

```
=== WIKIPEDIA PRIAM etymology ===
60- (Top)
61-
62- 1 
63: Etymology 
64-
65- 2 
66- Description 
67-
68- 3 
69- Marriage and children 
70-
71- 4 
72- Life 
73-
74- 5 
75- Gallery 
--
243-
244- In Greek mythology , Priam ( / ˈ p r aɪ . ə m / ; Ancient Greek : Πρίαμος , pronounced [ prí.amos ] ) was the legendary and last [ 1 ] king of Troy during the Trojan War . He was the son of Laomedon . His many children included notable characters such as Hector , Paris , and Cassandra .
245-
246: Etymology
247- [ edit ] 
248-
249: Most scholars take the etymology of the name from the Luwian 𒉺𒊑𒀀𒈬𒀀 (Pa-ri-a-mu-a-, or “exceptionally courageous”), [ 2 ] [ 3 ] attested as the name of a man from Zazlippa, in Kizzuwatna . A similar form is attested transcribed in Greek as Paramoas near Kaisareia in Cappadocia . [ 4 ] 
250-Some have identified Priam with the historical figure of Piyama-Radu , a warlord active in the vicinity of Wilusa . [ 5 ] However, this identification is disputed, and is highly unlikely, given that he was known in Hittite records as being an ally of the Ahhiyawa against Wilusa. [ citation needed ] 
251-
252: A popular folk etymology derives the name from the Greek verb priamai , meaning 'to buy'. This in turn gives rise to a story of Priam's sister Hesione ransoming his freedom with a veil, from Heracles , thereby 'buying' him. [ 6 ] This story is attested in the Bibliotheca and in other influential mythographical works dated to the first and second centuries AD. [ 7 ] These sources are, however, dated much later than the first attestations of the name Priamos or Pariya-muwas, and thus are more problematic. [ citation needed ] 
253-
254- Description
255- [ edit ] 
256-
257- Priam was described by the chronicler Malalas in his account of the Chronography as "tall for the age, big, good, ruddy-colored, light-eyed, long-nosed, eyebrows meeting, keen-eyed, gray, restrained." [ 8 ] Meanwhile, in the account of Dares the Phrygian , he was illustrated as ". . .had a handsome face and a pleasant voice. He was large and swarthy." [ 9 ] 
258-
259- Marriage and children
260- [ edit ] 
261-
262- See List of children of Priam 
263-
264- Priam is said to have fathered fifty sons and many daughters, with his chief wife Hecuba , daughter of the Phrygian king Dymas and many other wives and concubines. These children include famous mythological figures such as Hector , Paris , Helenus , Cassandra , Deiphobus , Troilus , Laodice , Polyxena , Creusa , and Polydorus . Priam was killed when he was around 80 years old by Achilles' son Neoptolemus.

=== priamai ===
d
=== PIr xsafs ===
STATUS URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/x%C5%A1%C3%A1f%C5%A1
FETCHED: 2026-09-06T22:42:02Z
STATUS: 200
TITLE: Reconstruction:Proto-Iranian/xšáfš - Wiktionary, the free dictionary

Reconstruction:Proto-Iranian/xšáfš - Wiktionary, the free dictionary 

 Jump to content 

 Main
Proto-Iranian
 [ edit ] 

 Etymology
 [ edit ] 

 PIE word 
 *kʷséps 

 From Proto-Indo-Iranian *kšáps .

 Noun
 [ edit ] 

 *xšáfš   f 

 night 

 Inflection
 [ edit ] 

 consonant stem

 singular

 dual

 plural

 nominative

 *xšáfš

 *xšápā(w)

 *xšápah

 vocative

 *xšáp

 *xšápā(w)

 *xšápah

 accusative

 *xšápam

 *xšápā(w)

 *xšapáh

 instrumental

 *xšapáH

 *xšabbʰyā́(m)

 *xšabbʰíš

 ablative

 *xšapáh

 *xšabbʰyā́(m)

 *xšabbʰyáH

 dative

 *xšapáy

 *xšabbʰyā́(m)

 *xšabbʰyáH

 genitive

 *xšapáh

 *xšafHā́h

 *xšapáHam

 locative

 *xšápi

 *xšafHáw

 *xšafšú

 Derived terms
 [ edit ] 

 *xšápīkah ( “ of night; night shirt ” ) 
 Kurdish:
 Central Kurdish: شەوی ( şewî ) 
 Southern Kurdish: شەۊ ( şeẅ , “ shirt ” ) 

 Middle Persian: ( “ undershirt ” ) 
 Book Pahlavi script: [Book Pahlavi needed] ( špyk' /⁠šabīg⁠/ ) 
 Classical Persian: شبی ( šabī , “ nightshirt ” ) 

 Kurdish:
 → Northern Kurdish: şepik ( šapīk ) 

 → Old Armenian: շապիկ ( šapik , “ shirt ” ) 
 Armenian: շապիկ ( šapik , “ shirt ” ) 
 Kurdish:
 → Northern Kurdish: şapik ( šāpīk ) 

 → Proto-Mordvinic: *šopə- , *čopə- ( “ dark, gloomy, evening ” ) 

 Descendants
 [ edit ] 

 Central Iranian:
 Avestan: 𐬑𐬴𐬀𐬞 ( xṣ̌ap ) 

 Northeastern Iranian:
 Proto-Scythian: *xšapā Proto-Saka-Wakhi: *ṣṣaba Proto-Saka: *ṣṣawa Khotanese: [script needed] ( ṣṣavā ) 

 Wakhi: šāp 

 Proto-Sarmatian: *ᵊxšaβa Alanic: *𐞃xsæβæ Ossetian: Iron Ossetian: ӕхсӕвӕ ( æxsævæ ) Digor Ossetian: ӕхсӕв ( æxsæv ) 

 Sogdo-Bactrian:
 Bact
```


## [2026-09-06T22:42:19.702Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD Watkins ===\"\ngrep -n -i \"kwrei\\|kʷrei\\|kwei-.*buy\\|to buy\" AHD_watkins1985.txt | head -20\necho \"=== AHD ksep ===\"\ngrep -n -i \"ksep\\|kʷsep\\|kwsep\" AHD_watkins1985.txt | head -10\necho \"=== IEC ===\"\ngrep -n -i \"^kʷrei\\|^qwrei\\|krinami\\|krīnāmi\\|kʷrī\" IEC.txt | head -20"
}
```


### [2026-09-06T22:42:19.777Z] TOOL RESULT

```
=== AHD Watkins ===
1159:wes-1. To buy. 1. Suffixed form *wes-no- in Latin vénum, sale: VENAL, VEND. 2. Suffixed o-grade form *wos-nd- in Greek dneisthai, to buy: DUOPSONY. [Pok. 8. wes- 1173.]
=== AHD ksep ===
=== IEC ===
```


## [2026-09-06T22:42:22.538Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD\npython3 - <<'EOF'\nimport re\ntxt=open('WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\npages=txt.split('\\f')\nprint('leaves',len(pages))\n# locate printed 523/524\nfor i,p in enumerate(pages):\n    if re.search(r'q[u\\^]?rei|krinati|kri-na-mi|krīnā', p) and ('kaufen' in p or 'Kauf' in p):\n        print('leaf',i, p[:100].replace('\\n',' '))\nEOF"
}
```


### [2026-09-06T22:42:24.600Z] TOOL RESULT

```
leaves 895
leaf 531                                                            qurmi-   — q^rei-                   523
```


## [2026-09-06T22:42:28.904Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD\npython3 - <<'EOF'\ntxt=open('WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\npages=txt.split('\\f')\nfor i in (531,532,533):\n    print('#### leaf',i,'####')\n    print(pages[i][:3000])\nEOF"
}
```


### [2026-09-06T22:42:30.566Z] TOOL RESULT

```
#### leaf 531 ####
                                                           qurmi-   — q^rei-                   523

wenn“ (s. u. 1. bei den r-Bildungen;                                 =
                                                lit. lair), ku „wo“, ku-s „wer“, kiis

„wie“ (u aus idg. u; s. Pedersen KZ. 36, 315 f., 328).
   Lat. ub% „wo       (dazu unde gebildet nach ibi inde), woneben ini. -cubl
                                ‘                                                  :



in ne-cubi, si-cubi ali-cubi (so, nicht alic-ubi zu trennen, siehe Persson
                                        ,


Beitr. 534 a 1, Sommer KE. 69; Bed. wie ali-qnis), nescio-cubi, nim-cubi
(ne-cunde usw.); es ist das durch die Stamme lat. quo-, qua qul vor der                    ,

Entlabialisierung durch u bewahrte qu- vor u zu qw- geworden und qwu-
hat anl. wu-, u- ergeben, wahrend in *ne-qmibi usw. infolge der Silben-
trennung ncq-wubi der Gutt. erhalten blieb; s. J. Schmidt aaO., Yf. LEWb. 2
m. Lit., Brugmann II 2 2, 350 m. Lit. (mit mil- unannehmbarer Alternative),
Sommer Ildb. 2 185, KE. 69 (der "Widerspruch Perssons Beitr. 533 f. iiber-
zeugt mich nicht); ubT ist nach Loc. auf -7 *ei, *ot) aus *ube = ai. kuha      i
                                                                                                   ,

abg. Ibde umgebildet, wie evrav&oi aus ivTav&a ,                osk. puf „ubi“ (umbr.  =
erweitert zu pufe pufe „ubi‘ ), s. Brugmann IF. 15, SOa 3.
                                    ,
                                                       :
                                                                        Entsprechend
                                               ) und uti, alat. utei (Umbildung wie
lat. ut „wie, damit, daf.i“ (uti-nam , - que

in lib 1) aus *q'iu-ti tus-piani , -qiuini „irgendwo“ aus ut -f adv. s), liter, utra,
-urn „welcher von beiden“ aus *q'tu-feros (parallel mit jzotsqos usw.; kaum
zu abg. vzton s. u. «-Pron -St.           Lit. bei Yf. LEWb. 2 s. v., und Brug-
                                                              :



mann II 2, 350), unquam , umquam „irgend einmal“ ( q'ium - temporaler Acc.);
          2

ob umbr. pu-e (-o Part.) „wo“                                 =
                                          ai. ku ist, oder *q'io, ist fraglich.

   Mcymr. cw cwd, cict „wo, wohin“ (Zupitza KZ. 37, 403a 1). Lit. lair
                          ,



„wo“ (s. o. 1 B,); auch lit. (dial.) ku „was?“ aus *kunl (Bezz. KZ. 47, 158);
apr. quei „wo“ nach Bezz. KZ. 44, 310a 1 aus *q“u-ei, und wohl der Aus-
gangspunkt des qu- statt k- im fem. nom. quai, qitoi usw.
   Ags. lift „wie“ ist aber = as. hwn, gr. tkx>.

qSrrai-     „Wurm, Made“.
      Ai. krmi- „Wurm. Made“; np. kirm „AYurm“; alb. krimp ( krimb-i ), geg. I rum
ds. (G. Meyer   EW. 206). Ir. crunn „Wurm“, cymr. pryf, corn. ds. „Wurm“
(brit. p- sichert Ansatz eines idg. Labiovel.), bret. preuu ds. Apr. ginnis
(leg. kirmis vgl. Trautmann Bsl.Wb. 134) „Made“: lit. kirm'is us
#### leaf 532 ####
                ;   ;                                                                                 g                 )
                                                                                                                        ;




524                                                      qjres-no       qusep-


Kaufpreis“                ;
                               np.   (Horn Np.           Et. Nr. 482)      xarldan „kaufen“;              gr.    nqiapai
„kaufe“
      crenaim „ich kaufe“, Konj. ni-cria
      air.                                          crlth „Bezahlung, Kauf“,
        „emax“ cymr. prynu „emere, redimere (3. sg. acymr. prinit), corn.
                                                                                 1
crTthid                          ;


prenne, pcma , bret. prana „kaufen“, cymr. prid (= ir. crlth) „oppigneratio“
mir. tor] ra „Umwerben“ (, ,*Brautkauf“), t-ind-s-cra „Kaufpreis fur die
                    i




Braut“ (scheint q’ireio-                         =
                           ai. krayd-h ), cymr. g(w)o-br „Preis, Belohnung“,

corn, gober, bret. gobr da., cymr. auch go-brwy da. (-my Suffix? oder *q'ireip-1
S. ZupitzaKZ. 35,                     457 f., Pedersen KG. II 16);                   Inf. (acc.J mir. creicc     (formal
nach re ire                   „verkaufen“, woriiber             s.   *per- „verkaufen“),       air. f. „Be-
                                                                                                      fochricc
lohnung (s. zum 11
                                      kelt. Formenbestand              Fick II 4 60, Pedersen KG. II 497 f.,
Stokes IF. 26, 142);
   alit. (Gen.) krieno „pretium pro sponsis“, lett. kriens kricnis ( kricna nauda          ,


„Geschenk an die Braut, Krongeld", wo hi auch lit. kravtis „Brautschatz,
Mitgift der Braut an Sachen“; aruss. krtnuti , krenuti „kaufen“, russ.-ksl.
einmal auch u-krijem ( *ti~kn>jem) „gekauft“ ohne den praesentischen Nasal
(Bernek. 633).
  Fick I 4 30, Bezzenberger BB. 12, 78;                                  16, 238.       Trautmann Bsl. Wb. 142,
Hiihlenbach-Endzelin II 284.

qjies-no- „Eiche“?
      Cymr.             bret. prenn,             corn,   pren    „Baum“      (*k urc,e-no-),     air.     crrmn,     Gen.
cruinn, Dat. crunn n. „Baum“ (mit unerkliirtem a des Nomin.; a. Thurneysen
Hdb. 47, 137) wird von Pedersen (KG. I 44) zu        gr. nglvo  „Steineiche“
(*k“r-sno-s,         angeblich wegen des folgenden s, KZ. 30, 351 ff.) und
                               mit   oi

weiter zu ai. kri-no- „schwarz‘ usw. gestellt (s. jedoch oben s. v. 1. qers-).
Jedenfalls ist aber gr. noiuvov „Stammende, Strunk" trotz Boisacq (s. v.)
fernzuhalten, ebenso lat. cerrus „Zerreiche“ (trotz Ehrlich KZ. 46, 479 f.,
 Unt. 139), das nach Schuchardt (SB. W. Akad. 1918, 188. Bd. 4. Abh.) ha-
mitischer Herkunft                        ist.



qSsep-              (?)       und einigermafien anklingende Worte fur „Dunkel“.
      Ai.
#### leaf 533 ####
                                            qasep-                                     525

ganz unsicher     (s.   Yf,   LEWb. 2 s. v.); andrerseits ist freilich auch Jokls,
SBAk. Wien 168, I 64, Yerbindung von creper mit alb. ngrils, ngris „mache
Abend", -em „verbringe den Abend",               ngrisete,     ungrts „es dammert, wird
Abend"   (sei   *n-Jcrp-tio-)      hochsfc fraglieh   (fiber   andere Deutungen   s.   Yf.
LEWb. 2 s. v. und fiber die dort genannten gr. xqvjixco lit. foopti „betrfigen“
                                                                  ,


unter qran- „aufeinanderlegen“).
                              5
  S. im allgem. Curtius           705, Bersu Gutt.    164a 1, 177, Johansson BB. 18, 7.
Uber lat. niger s. neig- „unrein“.
```


## [2026-09-06T22:42:39.031Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD\npython3 -c \"\ntxt=open('WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\npages=txt.split('\\f')\nprint(pages[532][3000:5200])\n\""
}
```


## [2026-09-06T22:42:40.157Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"482\\.\" HRN.txt | head -5\npython3 - <<'EOF'\ntxt=open('HRN.txt',encoding='utf-8',errors='replace').read()\nimport re\ni=txt.find('482. ')\nprint(txt[i-200:i+1400])\nEOF"
}
```


### [2026-09-06T22:42:40.615Z] TOOL RESULT

```
 kidp, ksapa „Nacht“, av. xsap- „Dunkelheit“; gr. ipecpag, ipspog „dunkel“,
ysrpagog,                 iperpgvog „finster, dunkel“; gr. cp statt                    n kann von den folgdn. gr.
Worten bezogen sein, deren Zugehorigkeit oder auch Yerwandtschaft unter-
einander nicht behauptet werden kann (es handelt sich z. T. um Reimworte
 noch ganz dunkler Vorgeschichte, s. Wood &x 3, Giintert Reimwortbildungen
 [1   12 ff.j
       gr. werfag (auch y.virpog Hes. Suid. Phot.)                          „Dunkel“ (eine Gdf. *q'is-n-pe(h)-
 ist  ganz fragwiirdig, ebenso aber Pedersens KG. II 97 zw. Yergleich mit
 air. yne ^ussehen", cymr. gne „hue, tint“); dvocpog „Finsternis“, spater

 yvocpog ds., drocpegog „dunkel“,   hom. lodvcjpqg „dunkelviolett“       t,6cpog                                 ;


 „Dunkel“, gocpeoog „dunkel“ (s. Boisacq s. vv. m. Lit.). DaB lat. crepero-
 „dammerig, dunkel, ungewiB, zweifelhaft" ( *crepeso -), crepiisculum „Abend-
 dammerung" (die scheinbare Deminutivform nach di-liiculum „Morgen-
 dammerung", Leumann Adj. auf Ai.s 94) mit sabin. cr- aus cn- und p- aus
 -bh (was iibrigens entbehrlich wird, wenn y.vkcpag analogisches <p fiir n hat)
 mit xvixpag zu verbinden sei (s. Ernout El. dial. lat. 145 f.), ist wegen cr-
```


### [2026-09-06T22:42:42.236Z] TOOL RESULT

```
4373:482. fßvlden 'kaufen'.
15320:»raoiö.carana- 482. > hiitm-h-
16295:jri'iHaii 482.
17580:[/*T»y-, krifiäti 482.
18195:fiÜtu- 482.
ien
II, 42 folg., und nehme an, dass das s sich zuerst
vor t entwickelt hat und dann allgemein eingedrungen
ist ; der Weg war also np. "^/rüsten, *xru§ten, yrösem,
xrösiden,
flirre s. ferr (No. 808).
482. fßvlden 'kaufen'.
ai. Vkray-^ krmdti, krintte 'kaufen'; phlv. ;^an^a/«.
kurd. kerin 'kaufen'.
*) x^iroh soll (nach BQ.) ebenfalls *Hahn' und *Hahnenkamm* be-
deuten. Np. li neben s (aus aw, s) findet sich auch in amäs^ ämäh, DNT'S»
riN^PS (Zotenberg in Merx' Archiv für wissenschaftliche Erforschung
des alten Testaments, I, 398 Zeile 9).— 107 —
Dialektisch ist die ursprüngliche Flexion nach der
neunten indischen Klasse sekundär wieder eingeführt
in Kasan: V(öni§ün) Impt. bann (Inf. eirlän; das an-
lautende k ist hier erst zu h geworden, wie in g.
heridmün, und dann gänzlich geschwunden), Q(ohrad)
bd/rm, K(e8e) be/rln^ Z(efre) biirln.
483. y(usptden 'schlafen , {TCSir auch *beschlafen, schänden
(Is. 13, 16), ^Nr2'D?l5 (Jer. 50, 6), /?(/"/e/«, /uspamJen.
aw. [/^x^ap- , yjapta- , [/^/"afs- , /"'afsata 'schlafen* ;
phlv. x^aftaii , yj^aftak , /;'afsUan bezw. /uftmi ; ai.
y'svap'^ svdplH.
oss. d. /iissthi, t. Russin (309); bei. vapsay^ n. vafsay^
vapsay (403); wa/. rä-yp-am^ ro/opt-am yö/s-am, sar.
yufs-am, si;'n. sows-am.
Hierher gehört wohl auch np. /efj, /efjä, ber/efj (HF),
'Nachtmahr , das de Lagarde, Ges. Abh. 55 mit aw.
xawza- oder, wie er lesen will, yawja- (vd. 8, 32 (99))
zusammenstellt. Doch scheint mir auch das, Beitr. zur
altb. Lex. 44, über aw. x^mba- Beigebrachte diese
Ansicht nicht genügend zu stützen, und mir bleibt
daher die Übersetzung Napf und 'Topf (Geldner
```


## [2026-09-06T22:42:55.371Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\ntxt=open('POK_02.txt',encoding='utf-8',errors='replace').read()\npages=txt.split('\\f')\nprint('leaves',len(pages))\nfor leaf in (304,305):\n    print('#### leaf',leaf,'(printed ~',leaf+344,') ####')\n    print(pages[leaf][:1800])\nEOF"
}
```


### [2026-09-06T22:42:57.220Z] TOOL RESULT

```
leaves 434
#### leaf 304 (printed ~ 648 ) ####
^  (Lok.);  att. Ttov,  ion.  Y.OV  ,wo^  (Gen.);  n6&ev  ,von  wo?*^;  hom.  rcöd-v,  ion.  %6&i  ,wo^; TtöxB  ,wann?^  (dor.  ^roxa  ,wann^,  vgl.  Schwyzer  Gr.  Gr.  1,  629),  norij  lesb. Ttöta,  ion.  xoTf  ,irgendeinmal,  einst^,  wozu  auch  rtoxs  nach  Interrogativen, z.  B.  iL  TtoTB  ,was  dann^  und  —  mit  erst  gr.  Red.  —  -riW«  ds.  (s.  dazu  unter foti-s),  TTÖas  ,wohin^  (-ae  aus  -ts)  =  got.  kap,  had  ,wohin^;  kret.  zsTov noXov  Hes.,  att.  Ttotog  ,qualis^  aus  *Ho-  +  oiuo-  =  ai.  Eva-  ,Art  und  Weise^, ahd.  ewa,  vgl.  got.  laiwa  ,wie?^,  s.  unter  ei-  ,gehen'^;  zum  Wechsel  von 7t-  (:  ion.  X-):  t-  s.  Schwyzer  Gr.  Gr.  1,  293  f.
alb.  ke  ,wen?^  (*A;Jto-m),  se  ,was?'  (Abi.  *Ä;^öc?  mit  analogischer  Palatali- sierung?),  si  ,wie?'  (*Ä:?tei?);
lat.  qul  (alat.  quoi  aus  *Ä;!^o  +  Demonstr.  -i),  quae,  quod  Rel.  und  Inde- finit\im,  osk.  <pui,  pai,  püd  ,qui,  quae,  quod^,  umbr.  po-i,  -e,  -ei  ,qui^  pufe, porse  ,quod',  lat.  cuius,  cui,  quo,  qua  usw.,  umbr.  pusme  ,cui^;  Adv.  lat. quo  ,wohin'  (Abi.)  =  umbr.  pu-e   ,quö'  (u  =  ö,   das   vor  Enklitika  nicht
645
verkürzt  ist);  lat.  quam  ,wie,  als'  (Akk.  Sg.  f.)  =  umbr.  [pre-]pa  ,[prius-] qiiamS  osk.  pruter  pam  ds.  (av.  kam-cit  ^in  irgendeiner,  jeder  Weise^^ .ilat.  quam-de  =  umbr.  pane,  osk.  pan  ^quam';  lat.  quantus  s.  oben;
lat.  quom,  cum  ,wenn,  als;  so  oft  als'  (Akk.  Sg.  n.  wie  primum  usw.) ^  av.  k^'^  >^ieS  got.  kan  ,wann',  apr.  kan^  lit.  (dial.)  kq  ,wenn';  aksl. ko-gda  aus  *ko-g{o)da,  Meillet  Slave  commun^  470;
mit  -de  erweitert  umbr.  pon(n)e,  osk.  jpün  ,quom';  lat.  quandö  ,wann' i*quäm  Akk.  der  Zeiterstreckung  +  dö),  umbr.  panu-pei  ,qu
#### leaf 305 (printed ~ 649 ) ####
pep,  bret.  pep  Jeder'  (*Ä^ä-  oder  Ä?iö-Ä;?to-s ;  zu  abg. kak^  ^welcher?'),  ir.  cech  Jeder'  (das  e  nach  necK)]  air.  can,  mcymr.  pan I  (*k^ana)y  mbret.  pe-han  ,woher?';  air.  cuin  ,wann?',  mcymr.  usw.  pan, pann  ,als,  wenn'  (*kV^ani?),  air.  ca-ni,  mcymr.  po-ny  ,nonne'  (*^"ä-);
got.  Ivas  (*k'!^o-s)  ;Wer?'  und  indefinit  (Gen.  Jvis,  ahd.  Jiwes  =  abg. ceso,  gr.  T€o)j  aschwed.  hvar,  har,  adän.  hvä,  ags.  hwä  ,wer',  mit  dem  e I  des  Gen.  as.  hwe,  ahd.  hwer  (*Ä:^e-s)  ,wer';  neutr.  got.  ha  {*k^o-d),  ahd. liwaz^  an.  hvat,  ags.  hwoßt,  as.  hicat  ,was';  fem.  got.  hö  ,wer?  welche?'; got.  Ivan  ,wann,  wie',  as.  hwan,  ahd.  liwanne  ,wann'  (näherer  Vergleich mit  air.  can  ,woher'  ist  wegen  der  Bed.  fraglich),  as.  hwanda  ,weil',  ahd. hwanta  ,warum';  got.  he  ,womit?'  (Instr.);  afries.  hö,  as.  hioö,  ahd.  hicuö ,wie'  zu  lat.  quo  , wohin'  (Ablat.),  gr.  Ttw,  xw  ,irgendwie';
lit.  käs  ,wer?,  was?'  auch  indefinit,  fem.  M,  apr.  kas  m.,  ka  n.  ,wer  ?', kas  f.  quai,  quoi,  n.  ka  (Akk.  auch  kan,  kai)  ,welcher,  -e,  -es';  lit.  kad ;Wenu,  daß,  damit'  (Konjunktion  wie  lat.  quod,  aus  dem  fragenden  Ge- brauch, vgl.  ai.  kad,  av.  kat  adv.  Fragewort  ,nun,  ob?');  lit.  ka%,  kat-p, apr.  kai-gi  ,wie?'  (=  abg.  c^;  aber  über  gr.  ytal  s.  unter  *kai  ,und');
abg.  k^-to  ,wer?'  (G-en.  ceso),  kyß,  f.  kaja,  n.  koje  ,qui,  7toLog?%  ce, ,y,aitOL,  Y.ai'rteq,  sltisq'  (s.  oben).
B.    Ableitungen,    die    sich   durch   mehrere   Sprachen   verfolgen   lassen:
k^o-tero-  ,wer  von  zweien?';    k^ä-li-  ,wie?';    k"o-ti-,  k"e--ti-  ,wie
viele  ?'.
Ai.  katard-,  av.  katära-  ,wer  von  zweien',    gr.  ftörsQog,  ion.  yiÖTSQog
```


## [2026-09-06T22:43:04.130Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\ntxt=open('POK_02.txt',encoding='utf-8',errors='replace').read()\npages=txt.split('\\f')\nfor leaf in (306,307,308):\n    p=pages[leaf]\n    print('#### leaf',leaf,'####')\n    print(p[:2500])\nEOF"
}
```


### [2026-09-06T22:43:05.845Z] TOOL RESULT

```
#### leaf 306 ####
,  av.  kada  .wann?';  aber  lit.  kadä  .wann?'  aus  *kadhn]  zum Ausgang  siehe  oben  S.  181  ff.  (auch  für  abg.  kqdg,  kgde  .woher',  lat, q2ian-do).
Gr.  TtrjU-yiog  .wie  groß?  wie  alt?',  lat.  quälis  .wie  beschaffen',  lit.  kdUi köV  .wie  lange' ;  vom  St.  k^o-  aus  :  abg.  koUH  .wie  groß',  koh  ^quantum« (Trautmann  111).
Ai.  kdti  .wie  viele'  =  hitt.  kuwatta,  lat.  quot  ds.  (vom  apokopierteu quot  aus :  quotus  .der  wievielte'),  ai.  kati-thd-  .der  wievielte'  =  lat. *quotitei  (Lok.  m.)  die  >  cottl-die  .am  wievielten  Tage  auch  immer,  täglich'« gr.  lesb.  TCÖaaoQ  (hom.  7toaaf](.iaQ),  att.  TroVog.  ion.  ycöaog  .wie  groß'  (*k^oti'09^^ Ttöarog  ,der  wievielte'  aus  *7toGaoaT6g',  daneben  mit  idg.  e  av.  caiti  .wie viele',  bret.  pet  in  pet  dez  .wieviel  Tage',  petguez  .quotiens'.
Ai.  kdr-hi  .wann?'  ==   got.    Ivar^  aisl.   hvar  (*k'!ior)  .wo?'    und   relativ (davon  got.  harjis,  aisl.  hverr  .welcher',  eig.  .wo  er',  wie  aus  lit.  kur  [*Ä:!ittr] jWO^ -\- jis  .er'  das  lit.   Rel.  kurisj  kurs  .welcher'  erwuchs);    e-stufig  ags.i hwöRr,  ahd.  as.  hwär  .wo';  ö-stufig  lat.  cur  .warum,  weshalb',  alt  quör.    ^
Eine  Parallelbildung  zu  lat.  quis  in  alat.  quir-quir  .ubicunque'.  "J
2.  Stamm  k^ei-,  gleiche  Form  für  Maskul..  Neutr.  und  Femin.:
Ai.  kirn  .was?  was',  kih  .wer?',  nd-ki-h  .niemand'  (mit  k  statt  c;  letzteres lautgesetzlich  in:)  ai.  cit  (cid),  av.  cit,  apers.  ciy  .sogar,  jedenfalls'  (ur- sprüngl.  Nom.  Sg.  n.  *irHi-d;  s.  auch  unter  k^e  ,und');  av.  iii§  .wer'.  6i§ca ==  lat.  quisque,  gr.  rlg  is,  apers.  Öi§-öiy  ds. ;  av.  öl  .wie'  (Instr.);
arm.  -6  in  in-ö  .etwas'  (=  ai.  kirn — cid),  das  auch  im  ersten  Glied  hierher, mit  Abfall  des  ä:J?-  wie  i  (z-i)  .was?*  (*kl^id-),  Instr.  i-v  .wodurch,  womit', (s.  auch  oben  zu  arm.  o  ,wer') ;  zum  Alb.  s.  oben  unter  1 ;
gr.  rlg  {*k^is)  m.  f.  (thess.  mg,  ark.  kypr.  aig),  n.  rl  (*k^id)  .wer?  welcher,  -e, -es  ?'  und  rlg,  rt  .(irgend)  wer.  was'.  Akk.  m.  *tlv  {*knim)  erw.  zu  TtVa.  wonach rivog,  TLvi,  Fl.  n.  *k'!^id  in  megar.  ad  (.idv  .wieso?'  ti  (,irjv;  höot.  t«  .warum' =  lat.  quia]  auch  in  ion.  dcaaa,  att.  Icrra,  ,rLvä  Nom.  PI.'  (durch  falsche Trennung  aus  ÖTCoTd  aaa)  und  mit  dem  relativen  ä  verbunden  äoüa,  att. &TTa ;
lat.  quis,  quid  .wer.  w
#### leaf 307 ####
as'  (fragend,  indefinit,  relativ),  qul  Adv.  .wodurch, wovon  (rel.);  wie  denn,  warum  (frag.);  irgendwie  (in  Wunschformeln)' (könnte  Abi.  *äjM  sein,  aber  doch  wohl  auf  Grund  eines  Instr.  *Ä?tz  =  av. öl,  sloven.  ci  .wenn',  cech.  H  ,oh'.  ags.  usw.  hwl  .wie.  wozu,  warum'); qul-n  (aus  -ne)  .wie  nicht ;  daß  nicht,  ohne',  quia-nam  .warum',  quia  .daß. weil'  (Akk.  PI.  *kV:i9)  s.  oben;
647
osk.  p'isj  Tpid  ,quis,  quid^  (fragend,  indefinit^  unbestimmt-relativ),  umbr. sve-pis  ,si  quis'^,  jpis-i  ^quis,  quisquis^;  gedoppelt  osk.  pispisj  lat.  quisquis, ar^iv.  TtCTtg  in  verallgemeinernd  indef.  Sinne  j
air.  cid  ^was?'  mit  dem  i  von  c-id  ^obwohl  es  sei^;  ursprüngl.  wie  das adj.  c^d  aus  *ce  ed]
air.  cia  ,wer^,  cjmY.pwy,  com.  pyw,  hvet.  piou  jWer^  (*k^ei)]  verbunden xymr.  py,  pa,  p-  usw.  (air.  cotej  cate  ,was  ist^,  ,wo  ist^  ist  unklar);
got.  Ivi-leiksj  ags.  hioilc  ,w\q  beschaffen^;  ags.  hwi,  as.  hwl,  hwiu,  aisl. hvl  ,wie,  wozu^  warum^  (Jc^l  Instr.);
abg.  ch-to  ,was^;  Instr.  te  (s.  oben)  in  sloven.  ci  ,wenn;  auch  Frage- partikel^;  öech.  H  joW,  poln.  czy  ,oV,  russ.  alt  ci  ^wenn*^,  abg.  H-mh  Instr. daraus  erweitert;
über  toch.  A  kus,  B  kuse  ^welcher^  s.  Pedersen  Toch.  121;
hitt.  Frage-  und  Relativpron.  kuiä  ^wer^  welcher^,  verallgemeinernd kui§  kui§  usw.  (=  lat.  quisquis)  ^wer  immer'^  Indefinitum  kuis-ki  (=  lat. quisque)  ^irgend  jemand^,  n.  kuit-ki  (=  lat.  quidque);  lyk.  ti-ke  (=  hitt. kuis-ki)]  s.  P.  Tedesco  Lang.  21,  128 ff.,  A.  Hahn  Lang.  22,  68 ff.
3.  Stamm  k"u~:
Ai.  kü,  av.  kü  ,wo?^,  ved.  kuv-id  ,o\),  etwa^,  av.  iSü  ,wie,  in  welchem Maße?^  (^-  nach  6l  ,wie?^);  ai.  kuva,  kvd  ,wo,  wohin*^;  ai.  kutra,  av.  kud-ra ,wo?  wohin  ?^;  ai.  kutah  ,woher';  ai.  küTia  =  gathav.  kudä  ,wo^  (=  abg. Zc-Bö^e;  idg.  *k^u-dhe]  s.  unten  lat.  uhi)]  av.  kud-a  ,wie^;  hierher  auch  ar. ku  als  1.  Zsglied  zum  Ausdruck  des  Schlechten,  Mangelhaften  (eig.  ,was für  ein  .  .  .  !^),  z.  B.  ai.  ku-putra-  , schlechter  Sohn^,  av.  ku-näiri,  ,Hu
#### leaf 308 ####
re^, vgl.  böot.  TTovlLf-iOQ  , Heißhunger'  (*^^-);>  aböot.  Tlvliiiiädag,  auch  von  den Stämmen  k^o-  und  kV^i- :  ai.  ka-,  kä-,  kad-,  kim-^  z.  B.  kä-purusa-  ,Wicht', ka-püya-  ,übelriechend^,  kim-purusa-  , Kobold,  Zwerg'  (W.  Schulze  Kl. Sehr.  399 f.);
kret.  o-7tvL  , wohin',  syrak.  fivg  ("^TrvL-g),  rhod.  djtvg  , wohin'  (*^vl  neu gebildet  zu  ftoZ)]
alb.  kur  ,als,  wann'  (s.  unter  1.  B  bei  den  r-Bildungen)  =  lit.  kur, arm.  wr),  kurre  ,je'  (*kur-nei),  ku  ,wo',  ku-sh  ,wer',  kü-sh  ,wie'  (ü  aus idg.  w);
lat.  ub^  ,wo'  (dazu  unde  gebildet  nach  ihi :  inde),  woneben  inlaut.  -cuhi in  ne-cubi,  si-cuhi,  ali-cuhi,  nesciö-cuhi,  nun-cubi  (ne-cunde  usw.);  es  ist das  durch  die  Stämme  lat.  quo-,  qua,  qui  vor  der  Entlabialisierung  durch u  bewahrte  qu-  vor  u  zu  qw-  geworden  und  qicu-  hat  anl.  wu-,  u-  ergeben, während  in  *ne-qwuhi  usw.  infolge  der  Silbentrennung  neq-iouhl  der  Gutt. erhalten  blieb ;  ist  uht  nach  Lok.  auf  -l  (*ei,  *oi)  aus  *ub^  =  ai.  küha,  av. kudä,   abg.    kT>de  umgebildet  =  osk.  puf  ,ubi'   (umbr.    erweitert  zu  pufe
648
1
,ubiO?;  nach  Pedersen  Hitt.  50  f.  enthalten  uhi,  ihi  vielmehr  die  idg.  Ad- verbialenduDg-  -bhi  (gr.  -g)0;  ^g^-  ^^*^-  ^^-'^«-P^  {kwahi)  ,^o,  wann?'; entsprechend  lat.  ut  ,wie,  damit,  daß^  {uti-nam,  -que)  und  uti,  alat.  utei (Umbildung  wie  in  uhl)  aus  '^k'^u-ti  {us-^iam,  -quam  ^irgendwo'  aus  ut-}- adv.  s  =  osk.  'puz,  umbr.  jpw2-e  aus  *lc^ut-s-),  uter,  utra,  -um  ^welcher von  beiden'  aus  *k^u-teros  (parallel  mit  nötsQog  usw.),  unquam,  umquam ^irgendeinmal^  {k'^um-  temporaler  Akk.) ;  ob  umbr.  pu-e  (-o  Part.)  ,wo'  ä: ai.  kü  ist  oder  *k'^ö,  ist  fraglich;
mcymr.  cio,  ciod  (==  d),  ciot  (=  d)  ,^o,  wohin^  (*Ä;^*w-)  =  air.  co  ,wie?<|
got.  -hun  zur  Bildung  unbestimmter  Pronomina:  ni  ains-hun  ,nicht irgendeiner',  usw.;  ags.  hü  ,wie';  engl,  liow,  afries.  liü,  mnd.  loü]
lit.  kur  ,wo'  (s.  oben  1.  B);  auch  lit.  dial.  ku  ,was?'  aus  *kunl  apr.  gfitej ,wo'  aus  "^k^u-ei  und  wohl  der  Ausgangspunkt  des  qu-  statt  k-  im  fem. Nom.  gfttai,  quoi  usw. ;
WP.  I  514ff.,  WH.  I  313,  II  397 f.,  404 ff.,  408 f.,  410ff.,  Trautmann llOf.,  120f.,  133,  134,  Meillet  Slave  commun^  442ff.,  469,  Schwyzer  Gr. G
```


## [2026-09-06T22:43:10.021Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 -c \"\ntxt=open('POK_02.txt',encoding='utf-8',errors='replace').read()\npages=txt.split('\\f')\nprint(pages[309][:3200])\n\""
}
```


### [2026-09-06T22:43:11.576Z] TOOL RESULT

```
r.  1,  293  f.,  615  ff.,  Wackernagel-Debrunner  3,  558  ff.
kjirei-  ,kaufenV  Präs.  k"ri-nä-mi;  k}^roio-  ,Kauf preist
Ai.  krinäti  ,kauft'  (l  nach  krltd-  Partiz. ;  ved.  auch  krinäti  nach  Ausweis des  Metrums,  wie  auch  Päli  hinäti),  Infin.  kretum,  krayd-  ,Kauf,  Kauf- preis'; npers.  xarldan  ,kaufen';
gr.  TCQiaiiai  ,kaufe';
air.  cren{a)im  (*k^ri-nd-mi)  ,ich  kaufe',  Konj.  ni-cria  {*h^riiät),  crlth , Bezahlung,  Kauf,  crlthid  ,emax^;  cymr.  prynu  ,emere,  redimere'  (3.  Sg. acymr.  prinit),  corn.  prenne,  perna,  bret.  prena  ,kaufen',  cymr.  prid  (=  ir. crlth)  ,oppigneratio' ;  mir.  tochra  ,Umwerben'^  (,*Brautkauf'),  t-ind-s-cra n.  ,Kaufpreis  für  die  Braut'  (scheint  *kViroio-  =  ai.  krayd-) j  cymr.  g(w)o-hr ,Preis,  Belohnung^,  corn.  goher,  bret.  gohr  ds.,  cymr.  auch  go-hrwy  ds. (-i(;?/-Suffix) ;  Verbaln.  Akk.  mir.  ereicc  (formal  nach  reicc  ,verkaufen', worüber  s.  Thurneysen  Gr.  454),  air.  fochr(a)icc  f.  ,Belohnung';
alit.  (Gen.)  krieno  ,pretium  pro  sponsis',  lett.  kriens,  krienis  ,Geschenk an  die  Braut',  auch  lit.  kraitis  ,Brautschatz,  Mitgift  der  Braut^;
aruss.  krbnutij  krenuti  ,kaufen',  Infin.  hiti,  russ.-ksl.  einmal  auch  u-kri- jem  {*u-krhjem)  ,gekauft'  ohne  den  präsentischen  Nasal;
toch.  A  kuryar  ,Handel',  kuryart  ,Händler',  B  karyor  ,Kauf',  kdryorttau ,Kaufmann'.
WP.  I  523  f.,  Trautmann  142,  Mühlenbach-Endzelin  II  284,  Kuiper Nasalpräs.  197.
649
^    ^firxöi-  ;Wurin,  Made^
Ai.  M'^^'  ;^^urm^  Made^;  np.  kirm  ^Wurm^;
alb.  krimp  (krim-hi),  geg.  krüm  ds. ;
air.  cruim  ,Wurm',  urir.  k^rimi-,  cymr.  pryf,  corn.  ds.  ^Wurrn^,  bret. prefiv  ds.;  gall.  FIN  *Primia  >  nhd.  Pfrimm,  Pr im anti a  >  nhd.  P7Hms ]
apr.  girmis  (leg.  kirmis)  ,Made';  lit.  kirmis  m.  f.  usw.  ds.^  lett.  cirmins -in.  ds.;  lett.  c^rme  f.  ^Spulwurm'  Mühlenbach-Endzelin  I  378  u.  386;
sloven.  ^rm  ^Karbunkel,  Fingerwurm^;  poln.  czern  (für  ^czerrh?  vgl. skr.  crn  ^robigo^  für  *crm?)  ^Würraer  im  faulenden  Fleisch^;  czermien Schlangenkraut^;  czermiöivka  ^Natternkraut^ ;
dazu  Adj. -Bildung  sl.  ^^hrmhm  ^rot^;  abg.  m^mhm  ^rot^^  cr^mhnovati  se feuerrot  werden^  usw. ;
die  e-Hochstufe  scheint  in  lett.  cerme  f.  ^Regenwurm^;  cerme  ^Wurm^ vorzuliegen ;  neben  sl.  *cbrmh  findet  sich  *hrvh  mit  eigenartigem  w-Suffix : abg.  (^r^vb  ,Wurm^,  russ.  cervb  usw.;  vgl.  lit.  '*skirvis  ^Ameise^?
WP.  I  523,
```


## [2026-09-06T22:43:19.074Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 -c \"\ntxt=open('POK_02.txt',encoding='utf-8',errors='replace').read()\npages=txt.split('\\f')\np=pages[310]\nprint(p[:1800])\n\""
}
```


### [2026-09-06T22:43:20.974Z] TOOL RESULT

```
Trautmann  134,   Specht  KZ.  65^  212  f.,  Idg.  Dekl.  45,  181.
]s.^sep-  (?)  und  einigermaßen  anklingende  Worte  für  ^Dunkel^
Ai.   ksdjp,   ksapd  ^Nacht^;   av.   x§ap-   ^Dunkelheif^ ;    gr.  ip€(pag,  ipsq)og  n.
,DunkeP;  xpecpagögy  ipecprjvög  ^dunkel^;   x^f^ag  , Dunkel^ ;  dvöcpog  ^Finsternis';
später  yvöcpog  ds.;  hom.  6voq)eo6g  ;dunkel^;  iadvecprig  ;dunkelviolett^ ;    ^6(pog
;Dunkel^;  i^ocpegög  ;dunkel^
Der  wechselnde  gr.  Anlaut  beruht  auf  Tabu -Vorstellungen. WP.  I  524  f.,  WH.  I  289;  Specht  Idg.  Dekl.  11.
k"pei-  s.  richtiger  oben  S.  487  unter  gV:hdei(9-).
Nachtrag  zu  S.  635:
k"äs-  :  k^QS'  ;husten^ ;  Nominalbildung  mit  -t-  erweitert.
Ai.  kä9-,  käsd-  , Husten',  davon  käsate  ,hustet';  alb.  koUe  , Husten'  {*k^äs-lä);  mir. caasacht{ach)  m.  ,Husten',  cymr.  pas  ds.  {*k^93-t-),  pesychu  .husten*  {^k'A9s-t-isk-),  bret.  yaa jHusten*,  com.  paz  ds.;  aisl.  hosti  m.  , Husten',  Sigs.  hwosta,  mnd.  hoste,  ahd.  Mwsto,  alem. wudSte  ds.;  lit.  kosiu  (alt  kosmi),  köseti  ,husten',  lett.  käseju,  käset  de.,  lit.  kosulys,  lett. kasuUs  , Husten' ;  slav.  '^kas^lh  in  russ.-ksl.  kaSelh  »Husten*,  usw.
WP.  I  506,  Trautmann  119.
■Um-
IT
L.
I.  lä-  und  le-  Schallwurzeln:  Präs.  läiö  und  leiö.
Ai.  räyati  ,he[W  (eventuell  auch  zu  re-  ^schreien');  osset.  ram  ^bellen';
arm.  lam  ^weine*^;  unklar  lor  ^WachteF  (s.  unten  gr.  IccQog);
gr.  XTJQog  m.  ^Geschwätz,  PosseU;  Tand^  (enthält  lä-  oder  le-),  X7]Qi(a ^schwätze^;  unklar  ist  der  Vokalismus  (onomatopoetisch?)  in  IccQog  ,Möwe' (vgl.  arm.  lor  ,Wachtel');
alb.  leh  ,helle^;
lat.  lämentum  ^Wehklage^^  lämentäri  ^wehklagen^,  lätrö,  -äre  ^bellen'; vielleicht  osk.  lamatir  ,soll  verflu
```


## [2026-09-06T22:43:35.085Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KNT xsap / xri ===\"\ngrep -n -i \"xšap\\|xsap\\|xrī\\|xri-\" KNT.txt | head -20\necho \"=== NYB ===\"\ngrep -n -i \"xrīdan\\|xrītan\\|xrīn\\|šab\\|šām\" NYB_vol2_glossary.txt | head -20"
}
```


### [2026-09-06T22:43:35.176Z] TOOL RESULT

```
=== KNT xsap / xri ===
2224:"$88. Tue Srems IN Stops, 1ч OP: these in- elude stems ending in £ (napdf- ‘prandson’), nf (*tunvant- ‘strong’), d (éard- ‘year’, pad- ‘foot, rād- ‘cause’), p (xSap- ‘night’, ap- ‘water’ cf. épi-) k (vif- ‘house’, vas- ‘will’).
2672:K. To express time when, as їп the adverbs paranam and paruvam ‘formerly’, and with the postposition pakiy: DB 1.20 xsapavd raucapativà ava akunavayata ‘either by night or by day, that was done’; DB 2.61f Güravaharahya mahya jiyam- nam patiy avat sam hamaranam kartam ‘on the last of the month Thuravahara, then by them the battle was fought’.
3477:20 : afahya : xSapava :raucapativà : ava : akunavayatà —— :8atiy : Dárayava
=== NYB ===
1424:who is the messenger from this being [the Creator just mentioned] is good 5711; etc. passim; — anticipates a clause with kū ‘that’ 521.7132, 5320; ~ ku the fact is that 52"; a rel. clause: ~ +-t... pursit 7614; ~ ce that which 11214; — forms a rel. attribute: ~ i vas kayak u karap 5525; — forms possessives of the pers. pronouns: ~ % man zan my wife 3215; ~ i tō pus thy son 5213-15; ~ 4 tē separated by other parts of the sentence from its headw. 60°; — pat ~ dāštan 5012, v. dāštan; pat ~ šātēhē for joy over this 412°; pat ~ ku... adak-ic although ... yet 5525-26; ~~ rād for that reason 795 ete.; — cigon ~ i den göbet as the pertinent passage of the Scripture says 5323 etc.; čvak — i paitäk ku one (event) is that which is revealed, namely that 385-17, — 2 HWHw-yt! (ideogr. for the 2nd p. pl. of h- ‘to be’) wrongly for ēt: pat ~ dästan 25°. — 3. ē: ēvak ~ (i) paitäk 36% and passim 41-54; ~ rād ce because 9422. — Av. (12 sqq.) aéta-, OP aita-; MPrth ‘yd; MPrs ?yd. The form é in BP is confirmed by the wrong ideogr. HWHw-yt', but it is note- worthy that this pron., wherever it is phonetically written in BP, has the form é (also in FrP 25). In Paz. there is no trace of & (ed), since the only form occurring there is ē with the pl. ēšgn, which is also used as the pl. of õi, ētšān having totally disappeared; NP has only 6, pl. ēšān. This esqn can neither be derived from ët nor from öisän; it must reflect the Olr. gen. pl. *atšām (Av. aēšam) of *ayam (Av. ayem, aēm) whence in Milr "aš enlarged with the Milr pl. ending -än. The most probable expla- nation of BP ē is, therefore, that it is not a mutilation of é& but the gen. sg. of *ayam: ahya. This being so, it would seem to be most advisable simply to give č as the normal equivalent of HN’, which would best explain the widely spread use of HN’ as the ideogr. for homonyms, v. below.
2116:[ideogr. ZNH] HajA:1.5.12. SPrth: 4. — Av. OP ima-; MPrth ‘ym, the egui- valent of Prs én; MPrs ‘ym rare, but pl. ‘ymy&n (cf FrP 24 LZNH-#n = imsän) is the common pl. of en; NP im only in im-réz, im-šab, im-säl.
2768:nišēm [nšdm] a bird's nest 2018. — < *atšadman, v. nišastan; Paz. nišim, na- šim ‘a resting-place' (Mx), nišāmī (SGV); NP nišim.
7432:šab: šap
```


## [2026-09-06T22:43:36.332Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\ntxt=open('SOD_pages.txt',encoding='utf-8',errors='replace').read()\npages=txt.split('\\f')\np=pages[233]\nprint('--- leaf 233 (printed ~167) head ---')\nprint(p[:1200])\nEOF"
}
```


### [2026-09-06T22:43:37.910Z] TOOL RESULT

```
--- leaf 233 (printed ~167) head ---
 yrb'q

           2.1068; Yrfi'kw, Hen. Tales. 480.1; MSP b 130;     4224 yrpV        S =* yrPy
           YrjPku YrVqu TSP 8.24; Tales. 467.60; BBB          4225 yrpV B                        «wf 7 ij>€ 7 <o^j
           f90; STii 4.42, 10.5; STi 6.8; C2 gloss.                yarPaw, yarP(a)u ©n. adv. prcs. inf.
 4211 yrb'q      C =» yrP>k                                        knowledge, conscience, conscicnt
 4212 yrb'qywny C                                 oSU^UlTT          VJ 381, 391, 393; TSP 5.108, Yrfi'wk Yrp>y; C2
      yarPak-yone
      wisely                                                          gloss. prYrft'w
                                                              4226 yrp'y B                                  ^L^lfT.Ub
         GMS 1115; STi 43.15                                       yarpe ©in compd. =»yrbyq
                                                                   knowing
 4213 yrp'kstr B                          yJiU<>lfT
      yarpakstar (yrb'qstr) ^yrP'k, yrb>qystr                      nw Yrp>yy VJ 393; 'xs-Yrby "knowing conflicts"
      wiser                                                          C2, 31R 21
         TSP 12.68, 69; STi 43.16;
```


## [2026-09-06T22:43:49.059Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== NYB šap ===\"\ngrep -n \"šap\\b\\|šap \" NYB_vol2_glossary.txt | head -10\necho \"=== NYB xrīt ===\"\ngrep -n -i \"xrīt\\|ZBNN\\|xrīn\" NYB_vol2_glossary.txt | head -10"
}
```


### [2026-09-06T22:43:49.119Z] TOOL RESULT

```
=== NYB šap ===
1123:cigon [cygwn] adv. and conj. A. interrog. adv. how? 1. direct interrogation: nun ~ kunom ?] 272; asmān ~? 921; exclama- tory: how...! 614. — 2. indirect inter- rogation: äkäh hom ku ~ hän 571; vēnēt ki Bastvar kārēcār ~ nev kunēt saw how valiantly B. fought 2815-16; ~ 6, 6 ham pursem 57°, andar Garodman dätistän ~, api-m nē dit 527-3; ete. — B. rel. adv. so as: l. har 3 šap x"amn ~ dit Estät ... guft such as he had seen it 2%; 215, 48, 520, 4527, ete.; introducing quotations: ~ den göbet 387, ~... paitāk ku 4571-5, etc. passim; parenthetic, e.g. 7718, 818%; — with a demonstr. antecedent: hamgönak hast ~-am guft 1216-17; šmāh bat ētūn m to gobeh 2329; 4524-25, 782.4, etc. — 2. with- out a clause, used prepositionally: as, as (for instance), as it were, like: ~ agäh aköc martom 2678-27; ~~ martom kë šarm 43913; 12813; varcāvandān i ~ Yam u Frétón ... 45°; hàn 4 ~ én such a th. 438; namely 1078; — with a demonstr. antecedent: &ön ~ āluh-ē 9%; eton ~ to 1516; ét6n but ~ amahraspand-ē 38°”; — čton, or ógón, homänäk (a. v.) ~ 69%, ete.; mänäk(k)äi (g. v.) i õi ~ ke pus... bare (opt.) 418. — C. conj. 1. causal be- cause: ~~... hdn mazantom bit 613-4; 1081. 11812; almost as a rel. pron. with a sec- ondary causal sense (as in Lat. quippe qui): 6 xuähar i x*"e$, ~ zan 4 Artaxsér būt, nämak nipišt 822; 718%, 7916. 116%. 11819; — hac han ~ in view of the fact that, considering that 38. — 2. temporal as soon as: 6°. 15°. 44°, more emphatically ham-~ 1317. - 3. ~ ka as if 11214.17, 10120722 — 4. almost = that 8722. — MPrth cw'gwn; MPrs ewn (read ci'on < *ciwön <
1780:~ tai šap zivandak Zarér, adak ... if Z. remains alive until evening, then. . . 25"; 287-8; m ēnyā except if, unless
2153:an antecedent signifying time: rēc-ē ka one day when 4%4; andar sap ka 520-21, or gap ka 6% in the night when; hamé pat Sap ka every night when 5!-*; pat hàn + tārīk šap ka 372°; fratāk rēc ka to-morrow when 225; rēc Ohurmazd" ka P2:1; pat hàn yavarY ka on the occasion when P1:2; adak ka, v. adak; nin ka now as 10918; hamvär ka 135, hamé ka 45° whenever; ete.; — without antecedent: hast ka, hast 1 ka there is a time when, sometimes 7725-26, 8122. 12018-19; but i ka nē but... u bavet ka ne bavet there was a time when he did not exist, and there will be a time when he will not exist 64?-?. — 2. sometimes for ku, after an antecedent signifying place: pat hàn gah ka-š ozat 1144, — C. in later texts and MSS often confounded with the rel. pren. ké [MNW], cf here 112%; 231-2 obscure, v. s. v. šāyistan.— MPrs k’, where ? is only the sign of a final d : kd (cf. s. v. be), as evi- denced by the forms with enclitics: km = kä-m, ks’n = kd-šān, and by FrP 25: "MT: kk = ka; Av. (436) kat "when ?". Not to be confounded with kad (g. v.).
3326:rče [YWM; lwc] day, pl. cas. obl. —-än [Iwe?n'] 2720; contrasting with gap ‘night’ 45, 2023; ka ~ būt when day was dawning 635; im ~ to-day 10, ete.; fratük ~ to- morrow, v. fratāk; nem ~ half a day 317, v. also nem-röc; hac im = tāt 3 — within three days counting from to-day 519; — m šapān 329. 728, 7417 [all lwc]. 989-109, 1203 (YWM šp'n'], röcak šapān 742°. 1011: the astronomical day of 24 hours (Swed dygn, Russ sutkt). — The names of the days of the month are in BP: 1. Ohurmazd. 2. Vahuman. 3. Art-(Urt-)
3329:röcak [lwck']: ~ šapān, v. the preceding W.
3604:Sap [Sp ; LYLY"] night, with the indef. art. šap-ē [LYLY’+1] one night 14; opp. rēc 20%; rēc... ~ by day... by night 215-5; róc u ~ night and day 4°;
3608:pat ham ~ in the same night 16?; hame pat ~ ka every night when 5!-?; hamak turist (g. v.) — throughout the whole night 501%; andar ~ in the night 614; (andar) ~ ka in the night when 520-?!, 6$; réc-~-Gn, v. rēc. — Av. (548 sg.) xSap- ašapd, xsapan- (xšafn-); OP xšap-; MPrth Prs 5b; Paz. šav; NP Sab.
3703:129-19; the vb. in opt.: framüt ku ~ dast à yamak ... avis üvurt he [HWH-d] that a set of clothes should be brought to him 217-18; — 2. temporal: ~ 6 dat à 7 sülak mat until he attained the age of seven years 1076-2"; ~ 6 han giyāk rasēt ki... 262°; as long as, as far as, with a nominal clause: ~ yazdän hayydr as long as the gods are helpers F:7; — en- larged by other elements: ~ ka, — han % ka until, so that; hamé ~ ka... apar šust always, as long as he was washing 414; 4112-18; with an inf.: kame ~ ka... akür kartan 4215; v. also han-tčit. — Notice the following idioms: im röc 7 mähakän hast täi āpustan hom to-day there are 7 months going on during which I am pregnant = to-day I am in the seventh month of pregnancy 1041-12; 3 rēc apāc but tai pas bē zat three days were left until he was born = three days before his birth 4416; 30 sal būt täi hamäi [thus to be read] raft thirty years elapsed until (= before) he had gone over the whole (creation) 9519-29; ta, € mäh during a whole month 20!?; tāt 3 rēc-šapān ruvān
3835:u [w; ^w 3915] and, passim; as the copyists have handled it rather carelessly it is difficult to discern in detail the rules valid for it; this much may be stated: l. if two subst. are coordinated v is often missing, in most cases probably only graphically, though the existence of real dvandvas cannot be denied: rēc(ak)- šapān (v. s. v. rēc), góspandàn virdn 41%, imitating the Av. dvandva pasu-vira; analogously martän zanän 5312-13; on two coordinated subst. expressing one notion (hendiadys) v. s. v. kār, cf also dar u draxt 3316, and the like; — 2. if more than two subst. are coordinated they may a) all be connected by u, e. g. 158. 781-2, 893-4, 90”, b) be put together asyndetically, e. g. 31?. 3910, 5518, c) take u only before the last w., often emphasized by adding -c to it, e. g. 3711-12, 4611-17-18, — 3 u may introduce the apodosis after a subordinate clause, e. g. 187. 34!?; taking up, through an anacoluthon, a sentence again after a preceding digression, e. g. 9°. 24%, 10317, ef s. v. ap-. — Encl. pron. are not attached to u in BP; instead ap- (q. v.) is used; the original expression u apt-š ‘and moreover (by him ete.) occurs not infrequently (e.g. 620. 302. 795), but as a rule ap- is used alone. — Av. (384 sqq.) uta OP
4220:višāt-dvārišnēh [wš't' dwb'linyh] the act of running “loose”, that is: with only the sacred garment (sudreh, in Phl Vd. šapīk) on, but without the sacred thread (kusti) 6912. V. Bharucha in Skr Mx, n. 8, and Modi, Ceremonies 181—190.
=== NYB xrīt ===
```


## [2026-09-06T22:43:51.243Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY\necho \"=== ARY latin index KWREI / KSEP ===\"\ngrep -n -i \"KWREI\\|QWREI\\|KSEP\\|KWSEP\\|KŠEP\" ARY_latin_index_pages.txt | head -20\necho \"=== ARY persian خریدن / شب ===\"\ngrep -n \"خریدن\" ARY_pages.txt | head -10"
}
```


### [2026-09-06T22:43:51.309Z] TOOL RESULT

```
=== ARY latin index KWREI / KSEP ===
=== ARY persian خریدن / شب ===
1245:دشواری نهایی دگرگونی آوایی است. مثلاً واژه‌ی «خریدن» فارسی با واژه‌ی [17۳۳۸ هل"
4389:چم این واژه در زبان لیتوانی؛ خریدن,
7013:۱ خرید» خریدن / ۲۳۹
```


## [2026-09-06T22:43:57.688Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY\npython3 - <<'EOF'\ntxt=open('ARY_pages.txt',encoding='utf-8',errors='replace').read()\nlines=txt.split('\\n')\nfor t in (4389,7013):\n    print('----',t,'----')\n    print('\\n'.join(lines[t-12:t+14]))\n    print('leaf',('\\n'.join(lines[:t])).count('\\f'))\nEOF"
}
```


### [2026-09-06T22:43:59.320Z] TOOL RESULT

```
---- 4389 ----
3ج
پاس (مثلاً در واژه‌های_/ ۱۵۱
پسگشت‌ها زد نی راد ادن اد ده رای 6 ما8
3 0/5
این 48 (۳037100) ,653654 (۳۸37)
0 (۳0۴037101) ,759 (۴۸1) 1 (۰)۳۸7 7
1 دی 5 (۶۸3) صر ی
3 (38تشت5۸ ,۳۸۳3) برهان قاطع : ۳۵۱
6 (۳۸3) :۸28
بادداشت: ۰
چم اين واژه در زبان سانسکریت: پاداش؛ مزد.
چم این واژه در زبان لیتوانی؛ خریدن,
چم این واژه در زبان یونانی؛ فروختن.
موم
اوستایی (4/587۷): آلمانی (/0879/۸): ۱:۱ رن
1 م,ش ۳۸717 انگلیسی (57لق8(/0)(از فرانسه) 8۳7 ,280
پارسی باستان ((۳88۶4 0ا0): ۰ 828۸* دانمارکی (0۸۸/374): 8۳۸۸
پهلری (1مالطه۳): سوئدی (8(75215): ۹ 5
7 ,86 نروژی (/(۸/077۷80): 572
کردی (0/15[7): 7 8۸5 هلندی (لع07): 5
تخاری 5 (8 ((فل2ل102): م2 آلبانی (/فاماالمقلم): 36زع2۸
سانسکر یت (54(/577):
-۸8 ,528 را۸3 2۸8 با71 52۸ پسگشت‌ها ۳/5
سنا زورون مس سس
آرمثی (۷ل۸7482/14): [د نکن 984 مان ی سنا
ایونانی 078870): |1053 (8۳۷) وی ار
leaf 149
---- 7013 ----
انگلیسی (6۸707/8): ‎٩‏ دراه 16 لاه
اسلاوی کهن (2/زمل5 7ل86ابا» 0ا0): 6 (۲۱۵) 0۱0۸8۰
07 8 (۲۱) معاو
لهستانی (/۳0./8): 7 برهان قاطع : ۷۴۱
روسی (851۸(۷/#): ۸
یادداشت:
۱- 88۸7 , 0810818 معتقدند که این واژه نرعی "تام آوا" (087031۸7070731۸) است.
۲ چم این واژه در زبان یونانی: شاهین.
۳ بازگشت به: خروش
[pdf page 238]
رد.۱
۱ خرید» خریدن / ۲۳۹
اوستایی (/1)3۸05:047857/40 ,2۸08۸171 لهستانی (کلا۳0): ان شام ها
پهلوی (۲7اللهه): 207۸0 روسی (551۸24(ا#): ۸7
سانسکریت (8۸۸5707): چکه ((226)): ادا ها
08۸۰ ,08۸31 ,1808۸ صربی (1۸۷ق557): 1
گرتبکك (ع007141)(شاید) برهمی (7ل80175(41): ادا هی ۱۹
1316 اسلرا کي (510/۸8): 133 ,1057۸3
ایسلندی کهن (/0/01۸۸41۸۸ف5 صا0)(شاید) لیترانی (01فا(هتا یط ): 1
1130۸ آترنی (لتي) (71۵2ل): ۸۸7
آلمانی (058/4۸0۷)(شاید) ‏ (601728م15
انگلیسی کهن (80۷01-5۶0 010)(شاید) پسگشت‌ها 55
هی 1 2002008
انگلیسی (6070187)(شاید) 00۸ 9 (۲8) ۸۸05/2/5
اسلاوی کهن (ع7ا5 07267 0ا0): 1052 ماه
۸ برهان قاطع + ۷۴
leaf 237
```


## [2026-09-06T22:44:10.446Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -c \"\" BRT.txt\necho \"--- Kauf ---\"\ngrep -n -o \"Kauf[a-zä]*\" BRT.txt | head -20\necho \"--- kauf ---\"\ngrep -n -o \"kauf[a-zä]*\" BRT.txt | head -20"
}
```


### [2026-09-06T22:44:10.520Z] TOOL RESULT

```
30725
--- Kauf ---
--- kauf ---
5403:kauf
8940:kaufa
13229:kaufmännischer
15663:kaufet
16390:kauft
18888:kauft
20894:kauf
28982:kaufa
```


## [2026-09-06T22:44:13.326Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor n in 15663 16390 18888 20894 28982 5403 8940; do echo \"=== $n ===\"; sed -n \"${n}p\" BRT.txt | head -c 700; echo; done"
}
```


### [2026-09-06T22:44:15.064Z] TOOL RESULT

```
=== 15663 ===
•  p.  *parga-'>  m.  Name  eines  Bergs  in Fersien:  'ga*  näm(^  kaufet  avadä  hama- ranam  akunavif  Bh,^.  7.

=== 16390 ===
vaim  ySi  dana  hakat  vaDn  ava.mh'ämafii  *arkadris  nämt^  kauft^  hacä  avaäasc^ hitvasca  pivasca'^  "gleich  diauf  beseitigen  Bh.7. 11.

=== 18888 ===
Appellativ    folgt:    *parg<^    'mii'    kauft^ avadä  , .  Bh,j,  7;  7. 11;  —  tOzäm^  'mii' vardanam  Bh,  7. 19;  2.3,  6,  12,  16,^.1,  5. 6,  8,  2.  7;   —  AaÜa  piravJ'  •««"  rauür D.77. 3".        7)  ohne  Appellativ;  wir  über- setzen dann  'einer  namens  , .'  oder  'ein  ge- wisser"*': kt^baßya*  °»w"  kärausptth^^ .. püruvam  ida  lüäya^iyi^  aAi/'  'Bh.i.io;  — taxmaspad^  'md'  mSd(^  manä  b(^dakt^ Bh.2.i4;io,j.3,6,q,  i4,^i8*,S.7.      Ohne Wert:     darayj'vcTus     vistaspakya     'mi^ /«ä'a*    Ao.  7.  2;   2.        b)    nätm/*;    das Appellativ  folgt:  hauv  udapatalä  habiraav dubali^  -ff/j"  äahyaus  haca  avadasa^  Bh. J-»3
=== 20894 ===
folgendem  hyatclt  (Sp.  593  u.);  nur  a)  im gAw.;  zu  I  2  k:  at  tä  vaxfyä  .  .  yä (NPn.)  Mazdä%a(sd.)  hyafcit  vjdul!  Y.jo. I,  b)  Einmal  findet  sich  im  jAw.  die Verbindung  _>'(j-  kvant-  im  Sinn  von  'wenig, gering":  kä  fraiüitill  yat  kvai  (sd.)  N. 103.  c)  Einmal  ist  im  gAw.j'J  NSm.  im Sinn  von  'o  dass  (ich) . ."  zum  Ausdruck  des Bedauerns  gebraucht;  der  übergeordnete Satz  fehh:  aica  gSus  urvä  raox/3{sd.):  y) analsim  xsqnm}nl(sd.)  rädern  *'yi  *mä  va- Sfftiiisd.) . .  y.  2g.  9.  IIA)  zur  Anknüpfung einer  nominalen  Ergänzung  oder  Erläute- rung an  ein  vorausgehendes  substantivisches Nomen.  Jeweils  unter  o)  
=== 28982 ===
a)  bei  Verben;  a)  der  Bewegung:  *draytr /ya*  &'  pnrsix''  aitiy  ('it')  D.  77.  3;  — pastl- ve^  adam  ni/äyam  (Sp.  153  m.)  A'  iäbirau/ asiyavam  müdain  Bh.  2.  1 2 ;  —  hauv  uda- patati  ('exsurrexit')  h°  *pifiya^uvlldaya ''arkadris  nilma"  kaufa'  A'  avadasJ' (Sp. 1 70  u.)  Bh.  7. 1 1 ;  }.  1 3 ;  —  karam  pärsam /nlisayam  (^tmxsC)  . .  A'  ragäya  Bh.j.i;  — xiah^am  ty<^  A'  amäxam  taumäyä  parä- bartam  ('ablatum')  ah^  Bh.  1. 14.  ß)  bei andern  Verben:  psrs^  ümiy  A'  pärs^ mudrayam  agarbäyam  ('emi')  D.  77.  3;  — A*  avadasa"  (Sp.  170  u.)  kSram  *äyasatä

=== 5403 ===
(in  Persien?):  'drisnäma"  kauf<^  ^\\.i.\

=== 8940 ===
•  j.  kaofa-,  p.  kaufa-  m.  r)  'Bergrücken, Höhenzug':  II  arkadris  näma"  °/a''  Bh.  /. » I ;  J-  7 ;  —  cd^wärü  vi'üwana  (sd.)  'fö YL  ig.z'i  —  vtgiihö  (sd.)  . .  'famm  Yt.  i4- 21.       2)'Höcker' desKamels  (nur Komp.).
```


## [2026-09-06T22:44:22.826Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"^•.*xra\\|^•.*xrū\\|^•.*xru\\|^•.*xrī\\|^•.*xri\" BRT.txt | head -30"
}
```


### [2026-09-06T22:44:22.893Z] TOOL RESULT

```
3177:•  j.  a-]asta-  Adj.  'ungebeten'  sva,  'uner- wünscht, verhasst';  pailistälie  °taca  zöiz- distaöj  . .  xrafsira  Yt.  11.  i.
3224:•  j.  a-daevayasna-  Adj.  'der  kein  Da^a- Verehrer  ist',  sva.  tnazdayasna-":  jahi  .  . yö  .xrudrä  fiam.ras^waydti  . .  da^'ayasna- nqm  -nanqmca  \. 18.62.
3607:•  j.  apairi.gaed'ä-  Adj.  -?-:  dusxratum ''^am  *asravayai^a%qm  Aog. AD.
3622:•  j.  apa.skaraka-  Adj.  'hohnsüchtig,  höh- nisch': nivßyaka  nipasnaka  °^a{NP.)  apa.- xraosaka  imä  paifi.vlsmte  Yt.  5.95.
3882:•  j.  aiwi.varSta-  Adj.  (fem,  "/(-)  'be- regnet, worauf  es  geregnet  hat':  vlsp3m\ a  ahmät  nasunam  -a  'ianqm  daxmanqmca ' 'tanqm  hixranqmla  'tanqm  vayanqmüi frariuhantanqm  "bis  dass  es  auf  die  Leich- name geregnet  und  .  .  und  auf  die  Lei- chenausscheidungen geregnet  hat  und  bis die  Vögel  (Alles)  aufgefressen  haben"  V.  ]
4471:•  j.  *aiiiim  Adv,  'anders'  näml,  als  der Wahrheit  entspricht,  sva.  'zum  Schein': paittJämm  a"  baraiii  .  .  xrafslraytigm  a' baraiti  ..  urvararn  a"  baraiti  anaiwyästü dainqm  "es  braucht  den  P.  zum  Schein \ .  den  Xr.  zum  Schein  , .  die  l/n'.  zum Schein,  wer  nicht  , ."  V. /Äi— 3".
5383:•  j.,  g-  auruna-  'wild,  fenis,  saevus': maSsahe  kihrpa  'na^e  Yt.  l4- 23;  —  'na/a gairisiicö  sizdraca  ravascarätö  "die  wilden (Tiere),  die  in  den  Bergen  hausen,  und die  scheuen,  die  in  den  Ebenen  streifen" Yt.  ^36;  —  alityS  mos  aia  syasdal{sA.) yavaf  ahmal  'nä  xra/strä  ".  .  soweit  als vor  uns  die  wilden  Raubtiere"  \.34. 9.
5485:•  j.,  g.  aradra-  Adj,  (fem.  'rJ-)  'getreu, 'verlässig':  'rS  '^wävqs(sd.)  ÄitzSntuü  sfmtö mazdä  Y. 4:_j.3;  46.^;  — fravasayB..  °rä taxmä  *at>javuAai/i/ \l.  ij.  $2;  75;  — mihrgm  . .  y5  äsunqtn  äsus  yS  'ranqm  °rö y3  taxmanqm  taxmS  Yt.  70. 65.  a)  mit DaL:  kuirä  tsi  °rä  masdä  ysi..  caxrayö' (sd.)  "ob  sie  wohl  dir  getreu  sind,  die  . ," Y._j4-7-  A)  insbes. 'dem  Glauben  treu, gläubig,  fromm':  firasaosträ  air3  tu  'r.lis idi  hvB^S  täis  yitig  . .  "o  Fr.Hv.,  dahin geh  mit  diesen  Frommen,  denen  . ."  Y. 4'j^i6;  —  kä  iw'ffi  a/a  äk,i  (sd.)  'ring isyl  Y.  4S.  8;  S*}.  4;  —  fatrijasai  .  .  at vä  aia  "rahyacä  mmankä  "..und  vor  euch, o  Asa,  auch  mit  dem  Gebet  des  Frommen" Y.50.8;  —  da^at  ahrnili  tat..  arfdvJ . . 'räi  yavmiini  jatoyantäi  da^ris  ayaphm Ytj.ig;  13a,  /5.1,  21.
5735:•  j.  a-sarsta'  Adj.  'nicht  gebrochen'  sva. "nicht  gebeugt,  nicht  mutlos  gemacht': taräiuitrlf  'tS  aka  mananha  xruzdya tbaisi.parsiannm  (sd.)  W.ig.\.
5855:•  g.  'a-spä-  n.  'Unglück,  Leid':  ySt vanhSus  vaidinä  (sd.)  manatthiS  sSnghaS raSxma  °spsn^l  (AP.)"  sadräcU  caxrayS (sd.)  tuMro  Y.34.T,  — yJn7  usJn  (sd.) &r;>i  sp7nlä  'spJnla.  (AP.)"'  Y.^ij.g.
6180:•  j.  aäajiäsain  Inf  'das  (höchste)  Anrecht zu  erlangen':  yS  .  .  xralBm  pprtsät  asa- vaium  . .  ahujtäsim  as°  vahilla.nils)m  (sd.) V.iA'.ö.
6432:•  j.  aä.xra3'was't9ma-  Adj.  'der  allerein- sichtigste,  weiseste':  bayanqm  aiti  {miirs) 'mS  YtlO.  141.
6486:•  j.  aäti.masah-  Adj.  'von  der  Grösse einer  A.':  äat  pitSus  ydi:a  cdijiciärS  'sS N.  (7^(?);  —  taltim  dauru  . . nyäzaym  (sd.) +°jj')  xraoidvaAe  bti'  altavatö  var>dvahe "ein  .  .  Stück  Holz  .  .  von  der  Grösse" einer  Ä.  aus  hartem,  doppelt  so  gross'' aus  weichem"  V.  13. 30.
6518:•  j.  aä.padina-  Adj.  'wo  man  viel  kocht':  •  j.  asya-  Adj.  'der  es  mit  dem  heiligen xsä^ra..  siai.iaxxra  (sd.)  °na  Vt.5. 130.   Recht,   mit  Asa  hält'  sva.  'fromm,  recht-
6752:•  ).  a-ham.baoS^mna-  Adj,  'nicht  wahr-  Oberherm  und  Richter  und  als  den nehmend'  sva,  'der  seine  Sinne  nicht  zu  ersten  Lehrer  der  Menschheit"  Yt. /_J.  1 5  a ; brauchen  weiss'  (vom  Hund):  yat  ..  sfä\ —  ya^a  fr3  loa  (sd.)  ämraot  yat  dim •n<s  Tä  haiat  aoäitySjxratus  "wenn . .  ander- '  ahümca  ratutn^a  ääadat  "'ya^a'  sagt  aus, seits  ein  Hund  seine  Sinne  nicht  zu '  dass  sie  ihn  (näml.  Zar^  als  A.  und  R. brauchen  weiss,  der  (weil  er)  nicht  recht  eingesetzt  haben"  Y.Jfj.u;  Yt  7^.92;  — bei  Verstand  ist"  V.  /_J,  35;  —  yesi  nnl<yailqm  ns  ahurS  maeäh  .  .  vatsks  valaa spS  'nS  mafye  v3  .  .pai'jyäite  aAmai(sA.)\{sA.)  atiqm  zaraiustr5  ankuca  (NS.)'' heüa  irisylt  "sonst  könnte  der  Hund,  der  ratu^ca  Vi.iö.i;  Yt./j.gi;  —  allai  dim seine  Sinne  nicht  recht  zu  brauchen  weiss,  lUsfanam  maziit?m  dazäyli  (sd.)  ahümca in  eine  Grube  ..  geraten"  V.  j_j.  37.  .^ratämca  yim    ahunm    mazdqm    Y.  27.  i;
6944:•  j.,  g.  ahmät  Adv.  I)  'inde';  i)  räumlich; nHt  käu  as  vaote  (sd.)  .  .  nBit  a'  vaiata ". ,  oon  inde  procedit"  P.  4^.  2)  zeit- lich, a)  'von  nun  an,  nunmehr':  ys . .  kayä (sd.)  a°  . .  7'ästryä  Y._jy.6;  — yä  a°  staota yasnya  irävayeni  "indem  ich  nunmehr  die StY.  aufsage"  Ny.4-S-  b)  mit  folgen-' dem  ya^a  und  fiiL  Konj.  'doncc,  bis  dass': aU'it  a'  yaha  ap?mgm  maniva  an  Aat mz'Ji/is  (sd.)  Y. 10.16.  U)  beim  Kompar., wörtL  'als  das',  was  i)  vorausgeht  oder 1)  folgt;  meist  unübersetzbar,  i)  zurück- weisend auf  zuvor  Genanntes  oder  Ge- sagtes: imaj  vS  jatöyemi  .  .  yalca  a°  asH miirya  ".  .  quodque  hoc  est  maius"  Y. 'jj.  14;  14'i  —  saisisca  .  .  oAqxitäiscä *ß-äyjblscal(sA.)ca  a-  Vr.  Ä  i.  a)  in Verbindung  mit  eil :  ayaaAaUtäis  kan- täis  paiti  azdibis  avaJitriäiyilt  {%^)  masyd vü  'mii-'i/V. 4. 50;  51,52.  2)  voraus- weisend auf  einen  Nebensatz  mit  &)yd:ia: yifnö  zqm  visävayat  afvit  irii'va  a'  mas- yefäm  ydia  fara  ahmai  Y.  2. 1 1 ;  —  nüit il  a-  *drajyS  *yätltn  framraemi  (sd.)  .  . äfrOIm  .  .  ya>a  .  .  V.33;  Yt.  I3. 64^;  — xraesyöJaraia  (sd.)  ri5  a'  ya>a  vikrkS raiÄfsd.)  Ißi/eV.  IJ.8;  —  näirivai/e.  .  «• pÖurum  '>  frantraomi  . .  ya%a  mayavö  (sd.) /ratäxsffit'V.4.^T,  47J.  h)  yäha  yat: itsit  vaakö  a'  fyao>amm  v»r^yeiti  ya'^a yai..karMt^.4S;^.iS.\o.  c)  yattsit: nSit  vanhs  a'  syao%tum   vtnsyeiti  yaüöil
7075:•  j.,  g.  ä-kä-  i)  Adj.  'manifestus';  a)  'der sehen  lässt,  wa^  er  tut,  sich  bei  dem  was er  tut  sehen  lässt,  es  offenkundig  tut': aiiyi^  kasHt  .  .  para.baraiti  'ka  (NS.) *hazatiha  *anskils>  iayusU.tJj;  6.  b)  'der sehcQ  lässt,  was  geschehen  ist',  spez.  von den  bei  der  äkä-  (s.  2)  Beteiligten,  'Offen- leger': hadä  asil  vakistScä  tiiananhä  xsa- 'irä.'a  yä  (NPn.)  /w  stanhai  a  pai^t  .  . 'ka  (NP.)  ar^ärSng  d^mänS  garö  Sfrao^äiiS "sammt  .  .  und  dem  Xs.,  welche  als  Offen- leger,  von  den  Frommen  ersehnt,  auf  dem Weg  zum  Haus  des  Lobs  den  Gehorsamen erwarten  werden"  Y.50,4'>.  2)  f.  'mani- festatio,  dilucidatio',  d.  i.  die  'Offenlegung' der  Taten  des  ersten  Lebens  bei  den  letzten Dingen  " :  dngvats  . .  yehyä  urvä  xraodattT (sd.)  cinvaiö  pinta  'kä  (Abi.)  "-  .  vor  der Offenlegung  an  der  Brlicke  des  Scheiders" V.  5/-I3;  —  ka  '^wöi  alu  'i,i  (NS.) arfdrSiig  ilyJ  "wird  deine  Offenlegung, o  A-,  den  Froramen  erwünscht  seini*"  Y. 4<V.8; — vahiitö  anktti  °>f(7j(AbL)-i-'?iV (sd.) ahüire  jasmtqm  Y.  60. 11.
7349:•  j.,  g.  iLmananha-'*  n.  i)  'Plan,  Absicht': mrüit!  (sd.)  yä  vS  xratSuS  xSmakahyü 'natahä  (NP.)  "was  die  Pläne  eures  Willens sind"  Y.  49.6.  2)  'Energie,  Ungestüm'; virikrayns  .  .  upa.kaxt3  '■nanha  (IS.)  Yt. /0. 7 1 ;  —  uitrahe  yö  arliiqm  ^franhir»- santqm  mazislftn  aoj3  ä-baraitt  maztshmca 'natjhim  Vt/^.ia'*.
7485:•  j.  "äste  Inf."'  ('zu  siuen'),  mit  Absol. 'in  dem  (durch  das  Absol,  bezeichneten) Tun  dauernd  verharren':  uxme  xraiwe yaonsm  (sd.)  ä'  ¥..^.45;  —  cvat  dräjö upa.maitim  (sd.)  ä"  .  .  V.j.53;  54.
7499:•  j.  'ä-sna-  Adj.  'angeboren,  natürlich', von  xratav-  m.  'Weisheit'  (im  Gegensatz zu  gmiSsräta-,  sd.):  «J»V  mailm..  s/g(s±) masyä  kacaiie  °nS  xrahts  yaüa  mi'inmni .  .  ha<aiu  'nasHt  xratus  "es  gibt  keinen Menschen,  dem  grössere  natürliche  Weis- heit zu  eigen  ist,  als  , ."  Yt.ro.107;  — "rum  xraiBm  tnasdaoättm  .  .  gaosS-srütim xratüm  tnazda'Mit^m  Y.  25.6;  —  'nahe xraiwö\.  22.2%;  —  Uta  kg  "fum  xratäm avaiaraiti  vSrjma  (sd.)  Yt/j.a,
7570:•  g.  ä.höi^i  Inf.  'zu  unterdrücken':  aiyS (nämL  mq'^ränS)  *grShms  a.h'  nl  käva- yascU  xratüsnl  dadat  *var»cäkiclt  fraidiva "auf  dessen  (des  Propheten)  Unterdrückung richten  Gr.  und  die  Kavay  ihre  Absichten und  Kräfte  schon  lange"  Y.J2.14.
7753:•  g.  araSva-  Adj.  i)  'recht  handelnd,  ge- recht': västryö  syaoianäis  °vs  hqs  huxratus namaakä  (sd.)  Y.5i'.  s;  —  ks  7'ä  vaiAsus manav/iö  aästä  magäi  'vd  "oder  wer  wird, rechthandelnd,  sich  auf  den  Bund  des  VM. bedacht  zeigen?"  Y,  57. 1 1 ;  —  yS  savaitl ädriiig  (sd.)  'ViwAöY.S^.^.  2)  "wahr, sicher':  ''i'j(APn.)  x/a^nl . .  asTstfs'{sd.)  Y. 44.g;~däidi*asä*dä(sd.)  dar^JyFi  'vifis tli  ux'iilis  mazdä  zarairvstr^t  aojSnghvat rafonS  akmaibyäLä  aAura  "schenk  du, o  M.,  durch  Aia  .  .  dem  Zar.  gemäss deinen  sichern  Worten  langdauernde  kräf- tige Unterstützung,  und  uns  . ."  Y.  2rV.  6.
8025:•  j.  igar9.ätäitya  Adv.  'im  Nu,  in  kürzester Frist':  is°  mi  vXspö  anhus  astvh  .  .  xrao- äal.urva  p»lo.iaims  '^.^.^■,  y.-j2  PüZ.
8027:•  j.  iSasa-  Adj.  dnw.  «aa ja- (sd.) :  isan.- itäitya  ml  vlspS  at)hu}  astva  'Sftn  jitahm xraodat.urva  (sd.)  .  .  V.5.4.
8166:•  j.,  g.  "uxäan-  m.  'Männchen  des  Rinds, Stier',  in  Verbindung  mit  dem  Namen  flir Rind"';  gaoma?z)m  ..  gaom  pairi  °sC\n>tn V.  IQ.  21;  —  gSus  paili  'sttö  .  .  gJus  faiti azyä  . .  V.i».37  f.  a)  g.  mit  atnam  GP, 'Stier  der  Tage',  vom  FrühUcht:  raota :^^iig  asnam  -sä  alurus  "das  Sonnenlicht, der  schimmernde  Stier  der  Tage"  Y.  50. 10'*;  —  kad3  mazdii  y5i  'siinJ  asnam  .  . darj^rüi  frd  asahy.i  frärmtl ..  saosyaittqm xratavs  "wann,  o  M.,  werden  die  Stiere der  Tage  . .  herkommen"^  Y.jtf.j".
8686:•  j.  u§-  n.  'Ohr'  uzw.  «^»rischer  Wesen'': k/(NS.)  F.9(?).  A)  sonst  nur  Du.;  a)  'die Ohren':  yezi  *kva£ibya  ''-sibya''^^  aiwi.- srunvaifi  . ,  yezi  äat  nöit  /ivagibya  "Hbya aiwi.surunvait(  N.  i'ö";  Uj;  —  *'sibya F.p'>*>;  —  drimts  .  .  asi  [-//Is)  karma gava  *dvari'^ra  zafan  Yt  jr.2;  —  pairi 'si  vSrayavw»m  kam  gava  nidanzaydmoMii Yt.  j.  27;  —  g?tirvaya  h?  päoave  züvar^ pairi  iS  'si  zvrpnäioi  sk)Hd?m  si  manS kirsnüioi  Y.9.28;  —  °//  ahuralu  mazda yazamaide  darp'^räi  (sd.)  maiirahe  .  . xratüm  .  .  mar>%räi  .  .  hisvqm  . .  fra^'äküi Yt. /.  28.  a)  von  Tieren;  °H  (näml. g>us)  pairi. dar ayänli  (sd.)  daSma  .  .  Vt. 14. 56.  b)  'Gehör*,  d.  i.  Fähigkeit  richtig zu  hören  und  zu  verstehen,  sva.  'Auf- fassungs-,  Verstandeskraft':  ava  pa'oS  ava zastS  ava  °/i  däraydiiwjm  .  .  däityanqm .  . syaoiinanqm  varpzäi  Vr.  75.  1;  —  d<lya ml . .  mastim  spilnö  xsviwrjm  (sd.)  hizi'qm uruiie  -si  xratBiH  .  .  Y.62.4.
8962:•  j.  ka-xuzi-  i.  Bezeichnung  einer  Klasse weiblicher  Wesen  der  dasvvizhen  Schöpfung : paxrusta  hl  "zi  (IS.)  . .  ayehye  . .  yJiumaiti jahi  "durch  Beschwörung  bist  du  ver- trieben, o  K.,  .  .  A.  .  ."  V.  2/.  17.
9395:•  ].  karsvar-,  -van-  n. 'Kreis' der  Erde,  vgl  iasuxra%',i,an:  —  V\,tkctdiakxraihimi 'Erdteü'":  />//«/  -^.^r»  j-«/  x^aniraiim\  ■  feasu.xraO-wan-  Adj.  (auch  fem.) Yt.i£.i5,^o.i5,67,i33,Y.57-3i.y./p.39,  -der  geringe  Einsicht  besitzt':  noit  ia H.  /.  I4i  -  't'^rp  yat  ar.>zahi  Yt.  i2.  9;  „^i^^a  -^wa  (NSf.)  "nicht  darum  (?)  ein ,„_,..  _  .„./   .,..„  j.^/  vouru.bar»iU:^^^^  ^„„  geringer  Einsicht"  N.40'>.
9897:•  j.  gaoäÖ.srüta-  Adj.  'vom  Ohr  gehört', von  xralav-  m.  'Weisheit'  sva.  'erlernt' (im  Gegensatz  zu  'asna-,  sd.)":  äsnim xratüm  mazdaaätpm . ,  °t>m  xratütn  masda-
10410:•  j-,  g.  guzra-  Adj.  'verborgen,  geheim';  [ sp»i!i-l  vidvä  yaSclt  'rä  (NF.)  s}ngh^i7ihö\ .,  vaiihSus  xraiwä  ffia«a«-4J  "der  heilige, der  auch  die  geheimen  Lehren  kennt,  . .  I durch  die  Geisleskraft  des  VM^  Y.4Ä3;
```


## [2026-09-06T22:44:41.044Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py \"https://abadis.ir/fatofa/%D8%B4%D8%A8%D8%AF%DB%8C%D8%B2/\" --note \"page 299, Kwsep, sabdiz: Mo'in entry\" 2>&1 | tail -2\npython3 tools/fetch_source.py \"https://vajehyab.com/moein/%D8%B4%D8%A8\" --note \"page 299, Kwsep, sab: Mo'in entry\" 2>&1 | tail -2"
}
```


### [2026-09-06T22:44:44.888Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/13351fdc9e44fe27.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/dd68618da3c3605a.txt
```


## [2026-09-06T22:44:48.619Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\ngrep -n -i -m3 \"معین\" 13351fdc9e44fe27.txt | head\necho \"---\"\npython3 -c \"\nt=open('13351fdc9e44fe27.txt',encoding='utf-8',errors='replace').read()\ni=t.find('معین')\nprint(t[max(0,i-600):i+900])\nprint('LEN',len(t))\n\"\necho \"===== vajehyab شب =====\"\npython3 -c \"\nt=open('dd68618da3c3605a.txt',encoding='utf-8',errors='replace').read()\nprint(t[:1500])\n\""
}
```


### [2026-09-06T22:44:51.493Z] TOOL RESULT

```
53: فرهنگ معین
128: آبادیس از سال 1385 فعالیت خود را در زمینه فن آوری اطلاعات آغاز کرد. نخستین پروژه آبادیس، سایت دیکشنری آبادیس بود. دیکشنری آنلاین آبادیس از ابتدا تاکنون تغییرات بسیاری کرده و ویژگی های مختلفی به آن اضافه شده است. آبادیس افزونه ای کاربردی برای مرورگرهای فایرفاکس و کروم و اپلیکیشن موبایل طراحی کرده است که میتوانید از لینک های بالا دانلود کنید. دیکشنری آبادیس شامل بخش هایی نظیر دیکشنری به زبان های مختلف از جمله انگلیسی، فارسی، عربی و همچنین بیست دیکشنری تخصصی با تلفظ انگلیسی و آمریکایی، ترجمه مخفف و کلمات اختصاری، مترجم آنلاین متن، لغتنامه دهخدا، فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راهنمای انتخاب اسم و ... می باشد. 
---
گردی 
سبق برده زو هم فیلسوفان 
چو مرغابی نترسد ز آب طوفان 
به یک صفرا که بر خورشید راند
فلک را هفت میدان باز ماند
به گاه کوه کندن آهنین سم 
گه دریا بریدن خیزران دم 
زمانه گردش و اندیشه رفتار
چو شب کارآگه و چون صبح بیدار
نهاده نام آن شبرنگ شبدیز
بر او عاشق تر از مرغ شب آویز. نظامی.
- راه شبدیز ؛ یکی از سی لحن باربد، مطرب و شاعر خسروپرویز. ( فرهنگ نظام ) ( آنندراج ) : بیشتر بخوانید ... 

 فرهنگ فارسی

 طاق بستان ( که تصویر خسرو پرویز شبدیز بر آن نقش شده ) .
شب رنگ، مانندشب، نام اسب خسروپرویز، سیاهرنگ
شب رنگ سیاه فام . یا شبدیز نقره خنگ . ۱ - آسمان . ۲ - زمانه . روزگار . ۳ - دنیا عالم . 

 فرهنگ معین

 (شَ ) (ص مر. ) شب رنگ ، سیه فام ، نام اسب خسرو پرویز. 

 فرهنگ عمید

 ۱. سیاه رنگ.
۲. (اسم ) (موسیقی ) از الحان سی گانۀ باربد: چو در شب برگرفتی راه شبدیز / شدندی جملهٴ آفاق شب خیز (نظامی۱۴: ۱۸۱ ). 

 دانشنامه عمومی

 شبدیز ( به معنی شب رنگ و شب مانند ) [ ۱] اسب سیاه رنگ مهین خانم، عمه شیرین همسر خسروپرویز بود [ ۲] که در نهایت تحت تملک خسرو پرویز قرار گرفت که بسیار مورد علاقهٔ وی بود و گفته بود هرکس خبر مرگ شبدیز را بیاورد اعدام خواهد کرد. اساس بیستون و شکل شبدیز همیدون در مداین کاخ پرویز
طبق داستانی که قدیمی ترین آن در شعر عربی خالد بن فیاض است، پس از مرگ شبدیز باربد قطعه ای بسیار غمناک برای خسرو پرویز اجرا کرد و در آن به تلویح به این خبر اشاره کرد، خسرو پرویز این را فهمید و گریست و گفت «شبدیز مرد!» و باربد گفت «این را شاه گفت» و بدین ترتیب از مرگ رهایی یافت. مشابه این داستان در منابع دیگر نیز آمده است. [ ۳] [ ۴] 
 wiki: شبدیز 

 این نوشته برگرفته از سایت ویکی پدیا می باشد، اگر نا
LEN 9612
===== vajehyab شب =====
URL: https://vajehyab.com/moein/%D8%B4%D8%A8
FETCHED: 2026-09-06T22:44:44Z
STATUS: 200
TITLE: معنی شب | فرهنگ انتشارات معین | واژه یاب

'
 />

 معنی شب | فرهنگ انتشارات معین | واژه یاب 

 26 فرهنگ 

 همه دیکشنری مترادف طیفی آزاد + 

 همه دقیق مشابه آوا متن آغاز قافیه 

 شب

 فرهنگ انتشارات معین
 (شَ) [ په . ] (اِ.) زمانِ بین غروب خورشید تا سپیده دم . ؛ ~ قدر شبی در ماه مبارک رمضان که در آن قرآن بر پیامبر (ص ) نازل شد. تاریخ دقیق آن معلوم نیست لذا شب های هفدهم ، نوزدهم ، بیست ویکم ، بیست و سوم و بیست و هفتم را شب قدر دانسته اند، لیلة القدر. ؛ ~ برات شب پانزدهم شعبان ، شب قدر. ؛ ~ شعر مراسم شبانه که در آن تعدادی شاعر شعرهای خود را برای حاضران می خوانند. 

 خرید اشتراک افزودن واژه افزونه مرورگر تماس درباره
```


## [2026-09-06T22:45:02.716Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\ntxt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=txt.split('\\f')\ni=None\nfor n,p in enumerate(pages):\n    if 'Priam,  n.,  king' in p:\n        i=n; break\nprint('leaf',i)\nfor n in range(i-2,i+3):\n    nums=re.findall(r'\\b(1[0-9]{3})\\b', pages[n][:300]+pages[n][-300:])\n    print(n, nums[:6], repr(pages[n][:80]))\nEOF"
}
```


### [2026-09-06T22:45:04.550Z] TOOL RESULT

```
leaf 662
660 [] "nd  with  Lith.  puciit,  pusti,  ‘to  blow, swell',  Lett,  piislis,  ‘bladder’"
661 [] 'tidhs,  per¬ taining  to  the  president’,  fr.  L.  praesidens,  gen. -entis.  '
662 [] 'ential  suff.  -or. prevenance,  n,,  anticipation  of  the  needs  of  others. '
663 [] 'e, adj.,  and  -ive.\nDerivatives:  primitive,  n.,  primitive-ly,  adv., primiti'
664 [] 'alue,  price’.  Prize  is  the  doublet  of  price  (q.v.) The  spelling  prize '
```


## [2026-09-06T22:45:17.815Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\ntxt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=txt.split('\\f')\nprint('leaves',len(pages))\nfor n in (630,632,634):\n    print('== leaf',n,'==', repr(pages[n][:120]))\nEOF"
}
```


### [2026-09-06T22:45:19.775Z] TOOL RESULT

```
leaves 903
== leaf 630 == '  ‘strength,  power,  rule’.  See physio-  and  -cracy.\n1180\n1181\nphysiocrat,  n.  —  F.  physiocrate,  back  formation '
== leaf 632 == 'tra,  ‘rock, stone’,  fr.  Gk.  7r£xpoc.  See  petro-.\nDerivatives:  pier,  tr.  v.,  pier-age,  n. pierce,  tr.  and  i'
== leaf 634 == ' leaf  (bot.)-,  2)  fin  ( zool .);  3) the  external  ear  ( anat .)  —  L.  pinna,  ‘feather, wing;  fin  of  a  fish'
```


## [2026-09-06T22:45:25.083Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\ntxt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=txt.split('\\f')\nfor n in range(655,670):\n    nums=re.findall(r'^\\s*(1[0-9]{3})\\s*$', pages[n], re.M)\n    print(n, nums)\nEOF"
}
```


### [2026-09-06T22:45:27.222Z] TOOL RESULT

```
655 ['1228']
656 ['1231']
657 ['1232']
658 []
659 []
660 []
661 []
662 []
663 []
664 ['1245', '1246', '1247']
665 ['1249']
666 ['1250', '1251']
667 ['1252', '1253']
668 ['1254', '1255']
669 ['1256', '1257']
```


## [2026-09-06T22:45:30.518Z] TOOL CALL #72: Bash

```json
{
 "command": "sed -n '1,120p' tools/verify_check.py"
}
```


### [2026-09-06T22:45:30.558Z] TOOL RESULT

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


## [2026-09-06T22:45:52.906Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nfor f in 05e487d9f04a0b40 1e74b143093d08b8 d97e46a327f8712e; do echo \"=== $f ===\"; head -5 $f.txt; wc -c $f.txt; done"
}
```


### [2026-09-06T22:45:54.633Z] TOOL RESULT

```
=== 05e487d9f04a0b40 ===
URL: https://en.wiktionary.org/wiki/%CF%80%CF%81%CE%AF%CE%B1%CE%BC%CE%B1%CE%B9
FETCHED: 2026-09-06T22:42:01Z
STATUS: -1
TITLE: 

168 05e487d9f04a0b40.txt
=== 1e74b143093d08b8 ===
URL: https://en.wiktionary.org/wiki/%D8%B4%D8%A8%D8%B3%D8%AA%D8%A7%D9%86
FETCHED: 2026-09-06T22:42:03Z
STATUS: 200
TITLE: شبستان - Wiktionary, the free dictionary

4461 1e74b143093d08b8.txt
=== d97e46a327f8712e ===
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/xrin%C3%A1Hti
FETCHED: 2026-09-06T22:42:03Z
STATUS: -1
TITLE: 

168 d97e46a327f8712e.txt
```


## [2026-09-06T22:45:57.208Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\npython3 -c \"\nt=open('1e74b143093d08b8.txt',encoding='utf-8',errors='replace').read()\ni=t.find('Persian')\nprint(t[i:i+900])\n\""
}
```


### [2026-09-06T22:45:58.950Z] TOOL RESULT

```
Persian 

 Toggle Persian subsection 

 1.1 
 Etymology 

 1.2 
 Pronunciation 

 1.3 
 Noun 

 2 
 Urdu 

 Toggle Urdu subsection 

 2.1 
 Pronunciation 

 2.2 
 Noun 

 Toggle the table of contents 

 شبستان 

 5 languages 

 فارسی 
 Français 
 Magyar 
 Malagasy 
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

 Persian
 [ edit ] 

 Persian Wikipedia has an article on: شبستان 

 Wikipedia fa 

 Etymology
 [ edit ] 

 Etymology tree

 Proto-Indo-European *kʷséps 
 Proto-Indo-Irani
```


## [2026-09-06T22:51:25.916Z] TOOL CALL #75: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk299.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW_PIE_BUY = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/k%CA%B7reyh%E2%82%82-\"\nW_XARIDAN = \"https://en.wiktionary.org/wiki/%D8%AE%D8%B1%DB%8C%D8%AF%D9%86\"\nW_SAB     = \"https://en.wiktionary.org/wiki/%D8%B4%D8%A8\"\nW_SAM     = \"https://en.wiktionary.org/wiki/%D8%B4%D8%A7%D9%85\"\nW_PRIAMOS = \"https://en.wiktionary.org/wiki/%CE%A0%CF%81%CE%AF%CE%B1%CE%BC%CE%BF%CF%82\"\nWP_PRIAM  = \"https://en.wikipedia.org/wiki/Priam\"\nW_XSAFS   = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/x%C5%A1%C3%A1f%C5%A1\"\nW_SABEST  = \"https://en.wiktionary.org/wiki/%D8%B4%D8%A8%D8%B3%D8%AA%D8%A7%D9%86\"\nAB_SABDIZ = \"https://abadis.ir/fatofa/%D8%B4%D8%A8%D8%AF%DB%8C%D8%B2/\"\nVJ_SAB    = \"https://vajehyab.com/moein/%D8%B4%D8%A8\"\n\ndata = {\n \"pdf_page\": 299,\n \"book_page\": 269,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-06\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"Kwri, Qwri\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *kʷreyh₂- 'to buy' (nasal-infix present *kʷri-né-h₂-ti)\",\n   \"note\": \"Pokorny 648 kʷrei- 'kaufen', Präs. kʷri-nā-mi, with Skt. krīṇāti, NPers. xarīdan, Gk. πρίαμαι, OIr. crenaim, OLith. krienas, ORuss. krĭnuti, Toch. B karyor. LIV² 395 f. and Wiktionary write the root *kʷreyh₂-, Cheung (EDIV 446) *xraiH for the Iranian branch. Nourai's two spellings 'Kwri / Qwri' are just his labiovelar notation (qʷ = kʷ, as in Walde-Pokorny's 'qʷrei-'); language label 'Indo-European' and gloss 'to buy' are both correct. Only the Greek branch (nodes #5-#6) is problematic.\",\n   \"note_fa\": \"ریشهٔ هندواروپایی آغازین *kʷreyh₂- «خریدن» (پوکورنی ص ۶۴۸؛ لیو ۳۹۵). ستاک حال آن با میانوند خیشومی *kʷri-né-h₂-ti است که سنسکریت krīṇā́ti و ایرانی *xrī-na- و در نهایت فارسی «خریدن» از آن برآمده‌اند. برچسب زبانی و معنای ریشه در نمودار نورایی درست است؛ دو املای «Kwri / Qwri» تنها دو شیوهٔ نگارش همان همخوان لبی‌کامی kʷ است (والده-پوکورنی qʷrei- می‌نویسد). تنها شاخهٔ یونانی نمودار (گره‌های ۵ و ۶) پذیرفتنی نیست.\",\n   \"sources\": [W_PIE_BUY],\n   \"ref_check\": [\n    {\"ref\": \"POK:648\", \"status\": \"supports\",\n     \"note\": \"POK_02.txt leaf 309 (printed p.648): 'kʷrei- ,kaufen'. Präs. kʷri-nā-mi; kʷroio- ,Kaufpreis'. Ai. krinäti ,kauft' ... npers. xarldan ,kaufen'; gr. πριαμαι ,kaufe'; air. cren(a)im ...' — exactly Nourai's root, gloss and Persian/Sanskrit/Greek descendants. Cross-checked in POK_full.txt (grep 'Page(s): 648').\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"WLD\", \"where\": \"Bd. I 523-524 (WLD_Bd1_pages.txt leaf 531-532)\", \"stance\": \"supports\",\n     \"note\": \"Headword 'qʷrei-' at p.523, entry on p.524: 'np. (Horn Np. Et. Nr. 482) xarīdan „kaufen“; gr. πρίαμαι „kaufe“' — Pokorny's own source (WP. I 523 f.).\"},\n    {\"src\": \"CHEUNG\", \"where\": \"p. 446 s.v. *xraiH\", \"stance\": \"supports\",\n     \"note\": \"'*xraiH \\\"to buy\\\" ... PIE *kʷreiH₂- \\\"to buy, purchase\\\" = LIV: 395 f. | Pok.: 648'; IE cognates listed: 'Gr. πρίασθαι \\\"to strike a bargain\\\", (Myc.) qi-ri-ja-to \\\"he bought\\\", OIrish crenaid, Toch. B käry-'.\"},\n    {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt\", \"stance\": \"silent\",\n     \"note\": \"grep 'to buy' returns only 'wes-1. To buy' (Lat. vēnum, Gk. ōneisthai); Watkins' appendix has no *kʷrei- entry, so Nourai rightly cites POK rather than AHD here.\"},\n    {\"src\": \"SYN\", \"where\": \"11.81 BUY, p.817 (SYN.txt leaf 885)\", \"stance\": \"partial\",\n     \"note\": \"Buck's BUY table lists 'Skt. krī- (paṇ-)' and the discussion of IE *kʷrei- ('krieno (gen.) \\\"pretium pro sponsis\\\", Lett. kriens ... Toch. B kāry-'), but no Iranian/Persian form; Buck confirms the root, not the Persian line.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Avestan / Old Persian\", \"words\": \"xrî\", \"verdict\": \"plausible\",\n     \"derivation\": \"The Iranian verb 'to buy' is Proto-Iranian *xraiH- / *xrī- (Cheung, EDIV 446), continuing PIE *kʷreyh₂- with the regular Iranian treatment of the labiovelar before *r: PIE *kʷr- > Indo-Iranian *kr- > Iranian *xr- (the same fricativisation as in *kʷrmi- > NPers. kirm). The present stem was the nasal-infix *xri-na- > MP xrīn-, the past participle *xrī-ta- > MP xrīd. BUT the form is NOT attested in either language Nourai names: Bartholomae's Altiranisches Wörterbuch has no xrī- headword (grep 'kauf' in BRT.txt returns only kaofa- 'mountain'), and Kent's Old Persian lexicon has no such verb either; Cheung lists Middle Persian, Khotanese, Sogdian, Chorasmian, Bactrian, NW/NE Iranian and Sanskrit but no Avestan/OP entry. Nourai's own source FFD (Abolghasemi p.50) actually writes 'ایرانی باستان' (Old Iranian, i.e. reconstructed Proto-Iranian) — not Avestan or Old Persian. So the form is right and the ancestry is right, but the language label overstates the evidence: read it as Old/Proto-Iranian *xrī-.\",\n     \"derivation_fa\": \"فعل «خریدن» در ایرانی از ستاک *xrai̯H-/*xrī- برمی‌آید (چونگ، فرهنگ ریشه‌شناختی فعل ایرانی، ص ۴۴۶) که خود دنبالهٔ *kʷreyh₂- هندواروپایی است؛ لبی‌کامی *kʷ پیش از r در هندوایرانی به k و سپس در ایرانی به خ (سایشی) بدل شده است. ستاک حال با میانوند خیشومی *xri-na- و ستاک گذشته *xrī-ta- بوده‌اند. اما این صورت نه در اوستایی و نه در پارسی باستان گواهی نشده است: بارتولومه در «فرهنگ ایرانی باستان» مدخل xrī- ندارد و کنت هم در واژه‌نامهٔ پارسی باستان آن را نیاورده است. خود مأخذ نورایی، یعنی «فعل‌های فارسی دری» ابوالقاسمی (ص ۵۰)، آن را «ایرانی باستان» می‌نامد نه اوستایی. پس صورت و ریشه درست است ولی برچسب زبانی نورایی اغراق‌آمیز است و باید آن را ایرانی باستان (بازسازی‌شده) خواند.\",\n     \"sources\": [W_PIE_BUY],\n     \"ref_check\": [\n      {\"ref\": \"FFD:50\", \"status\": \"partial\",\n       \"note\": \"FFD_pages.txt pdf page 55 = printed p.50, s.v. خریدن: «خرید < فارسی میانه xrīd < ایرانی باستان *xrī-ta-. ... مادهٔ مضارع خرید در فارسی میانه xrīn است، از ایرانی باستان *xrī-na-». Abolghasemi supplies exactly this stem, but labels it ایرانی باستان (Old Iranian, reconstructed), NOT Avestan or Old Persian as Nourai's box does.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BRT\", \"where\": \"BRT.txt, x- section (cols. ~530-560)\", \"stance\": \"silent\",\n       \"note\": \"No xrī- headword; grep for 'kauf' yields only 'j. kaofa-, p. kaufa- m. \\\"Bergrücken, Höhenzug\\\"'. Bartholomae knows no Avestan verb 'to buy'.\"},\n      {\"src\": \"KNT\", \"where\": \"KNT.txt lexicon\", \"stance\": \"silent\",\n       \"note\": \"Kent's Old Persian lexicon lists xšap- 'night' among the consonant stems (§188) but no xrī-/xrīnā- 'buy'.\"},\n      {\"src\": \"CHEUNG\", \"where\": \"p. 446 s.v. *xraiH 'to buy'\", \"stance\": \"partial\",\n       \"note\": \"Cheung reconstructs *xraiH for exactly this verb and lists MMP xryn- (BMP ZBNN-), Khot. ggān-, Sogd. xryn/xr'yn, Chorasm. m/xn-, Bactr. χιρ-, NP xarīdan, Oss. ælxænun — but no Avestan or Old Persian attestation.\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Persian\", \"words\": \"xarîdan «خریدن (خرید ، خریدار)»\", \"verdict\": \"confirmed\",\n     \"derivation\": \"NPers. خریدن xarīdan < Middle Persian xrīdan, xrīn- (Book Pahlavi ZBNN-tn' with the Aramaic heterogram √zbn 'buy'; Manichaean MP xryd, xryn-) < Old Iranian *xrī-ta-/*xri-na- < PIE *kʷri-né-h₂-ti. MacKenzie's Concise Pahlavi Dictionary prints the whole chain in one line: 'xrīdan, xrīn- [ZBNN-tn' < A √zbn | M xryd, xryn-, N xarīdan, (xar-)] buy'. The only New Persian innovation is the prothetic/anaptyctic vowel that breaks up the MP initial cluster xr- (xrīdan > xarīdan), the same treatment as in xrad > xirad, xrōs > xurōs; the present stem was re-formed as xar- because خرید was reanalysed as a denominative past stem (Abolghasemi, FFD p.50). خرید 'purchase' is the bare past stem used as a noun, and خریدار 'buyer' is xar- + the agent suffix -dār (cf. MP -dār) — both are ordinary Persian derivatives, not separate inheritances.\",\n     \"derivation_fa\": \"«خریدن» از فارسی میانهٔ xrīdan / ستاک حال xrīn- (در پهلوی کتابی با هزوارش آرامی ZBNN-tn' و در فارسی میانهٔ مانوی xryd، xryn-) و آن از ایرانی باستان *xrī-ta- و *xri-na- است؛ مکنزی همین زنجیره را یکجا آورده است: «xrīdan, xrīn- ... N xarīdan, (xar-) buy». تنها دگرگونی فارسی نو افزودن واکهٔ میانجی برای شکستن خوشهٔ آغازین xr- است (xrīdan > xarīdan)، درست همان‌گونه که xrad > خِرَد و xrōs > خروس. ستاک حال «خر-» از رهگذر ریشه‌شناسی عامیانه ساخته شده، چون «خرید» را مادهٔ ماضی جعلی پنداشته‌اند (ابوالقاسمی، ص ۵۰). «خرید» همان مادهٔ ماضی در نقش اسم و «خریدار» = خر- + پسوند -دار است. ادعای نورایی درست است.\",\n     \"sources\": [W_XARIDAN, W_PIE_BUY],\n     \"ref_check\": [\n      {\"ref\": \"POK:648\", \"status\": \"supports\",\n       \"note\": \"POK_02.txt leaf 309 (p.648): '... npers. xarldan ,kaufen'' listed directly under kʷrei-.\"},\n      {\"ref\": \"KLN:1241\", \"status\": \"supports\",\n       \"note\": \"KLN_1966.txt leaf 662 (page numerals on the neighbouring leaves put it at pp.1241-1242), s.v. Priam: '... fr. I.-E. base *qwri-, \\\"to buy\\\", whence also OI. krinati, \\\"buys\\\", Mod-Pers. xaridan, \\\"to buy\\\"'. Klein's page number is exactly right.\"},\n      {\"ref\": \"SYN:817\", \"status\": \"partial\",\n       \"note\": \"SYN.txt leaf 885 carries the printed '817' and the section 11.81 BUY; the IE *kʷrei- paragraph lists Skt. krī-, OIr. crenim, Lith./Latv. and Tocharian forms, but Buck gives no Iranian or Persian word, so the page supports the root, not the Persian derivation as such.\"},\n      {\"ref\": \"BQT:743\", \"status\": \"supports\",\n       \"note\": \"BQT_v2_pages.txt leaf 201 (printed ≈743-744, the خریدار/خریده spread) carries Mo'in's footnote: «* خریدن - فتح اول و چهارم. پهلوی [xrīt] ... از: خری‌دن (پسوند مصدری). جزو اول در سانسکریت krī (خریدن) «هوبشمان ۲۸۴» ... کردی kirin ... ستدن چیزی با پرداختن بهای آن، مقابل: فروختن» — Pahlavi antecedent + Sanskrit krī, exactly Nourai's arrows.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie 1971 s.v. xrīdan (PHD.txt line 661; index 'buy xrīdan')\", \"stance\": \"supports\",\n       \"note\": \"'xrīdan, xrīn- [ZBNN-tn' < A √zbn; hl-ytn' | M xryd, xryn-, N xarīdan, (xar-)] buy'.\"},\n      {\"src\": \"HRN\", \"where\": \"no. 482, p.106\", \"stance\": \"supports\",\n       \"note\": \"'482. xarīden \\\"kaufen\\\". ai. √kray-, krīṇāti, krīṇīte \\\"kaufen\\\"; phlv. xarītan. kurd. kerin \\\"kaufen\\\".'\"},\n      {\"src\": \"HUB\", \"where\": \"HUB.txt line 6048\", \"stance\": \"supports\",\n       \"note\": \"'... xaridan \\\"kaufen\\\" (F. i. Sh. xiridan), skr. ptc. ...' — Hübschmann treats it as the inherited Iranian verb; Mo'in's Borhan footnote cites 'هوبشمان ۲۸۴' for the same equation.\"},\n      {\"src\": \"ARY\", \"where\": \"ARY_pages.txt leaf 237-238 (printed ≈238-239), entry «خرید، خریدن»\", \"stance\": \"supports\",\n       \"note\": \"Aryanpur's IE-roots dictionary gives the same family: پهلوی xrītan, سانسکریت krīṇāti/krayá-, Greek/Old Church Slavonic/Lithuanian cognates, with a cross-reference to برهان قاطع (the Latin transliterations are heavily OCR-garbled but the cognate set is unmistakable).\"},\n      {\"src\": \"CHEUNG\", \"where\": \"p. 446 s.v. *xraiH\", \"stance\": \"supports\",\n       \"note\": \"'*NWIR: Widely attested: NP xaridan/xar-, Kurd. kirin/kir-, ... *MIDDLE PERSIAN: MMP xryn- (BMP ZBNN-) \\\"to buy\\\" ... Partic.: perf. pass. MMP xryd'.\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"Sanskrit\", \"words\": \"krî\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Sanskrit क्री krī- 'to buy', present क्रीणाति krīṇā́ti (RV, AV onwards), infinitive krétum, verbal noun kraya- 'purchase, purchase price', ppp. krītá-. It is the direct Indo-Aryan continuant of PIE *kʷreyh₂-, with the regular Indo-Iranian delabialisation *kʷr- > *kr- (Iranian went a step further to xr-, whence Persian xarīdan). The -ī- of krīṇā́ti is analogical after the participle krītá-; the Vedic metre still shows krĭṇā́ti (Pokorny p.648, following Kuiper, Nasalpräs. 197). So Persian xarīdan and Sanskrit krīṇāti are sister forms of the same nasal present, not one derived from the other — which is exactly how Nourai draws them (both hang from the root box).\",\n     \"derivation_fa\": \"سنسکریت krī- «خریدن»، ستاک حال krīṇā́ti (از ریگ‌ودا به بعد)، اسم مصدر kraya- «بها، خرید» و صفت مفعولی krītá-. این صورت بازماندهٔ مستقیم *kʷreyh₂- هندواروپایی در شاخهٔ هندوآریایی است: لبی‌کامی *kʷ پیش از r در هندوایرانی ساده شده و به k بدل گشته، حال آنکه در ایرانی یک گام فراتر رفته و به خ سایشی رسیده است (خریدن). کشیدگی ī در krīṇā́ti قیاسی و برگرفته از krītá- است؛ در وزن ودایی هنوز krĭṇā́ti خوانده می‌شود (پوکورنی ۶۴۸). بنابراین «خریدن» و krīṇā́ti هم‌ریشه (خواهرند) نه یکی برآمده از دیگری — و نمودار نورایی هم هر دو را از خود ریشه آویخته است. ادعا درست است.\",\n     \"sources\": [W_PIE_BUY],\n     \"ref_check\": [\n      {\"ref\": \"POK:648\", \"status\": \"supports\",\n       \"note\": \"POK_02.txt leaf 309 (p.648): 'Ai. krinäti ,kauft' (ī nach krītá- Partiz.; ved. auch kriṇāti nach Ausweis des Metrums, wie auch Pāli kiṇāti), Infin. kretum, krayá- ,Kauf, Kaufpreis''.\"},\n      {\"ref\": \"BQT:743\", \"status\": \"supports\",\n       \"note\": \"BQT_v2_pages.txt leaf 201, Mo'in's footnote on خریدن explicitly equates the first element with «جزو اول در سانسکریت krī (خریدن)».\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"WLD\", \"where\": \"Bd. I 524\", \"stance\": \"supports\",\n       \"note\": \"'ai. krīṇā́ti ... ai. krayá-ḥ' cited under qʷrei-; the Celtic *k\\\"riio- 'bride-price' is equated with ai. krayá-.\"},\n      {\"src\": \"SYN\", \"where\": \"11.81 BUY, p.817\", \"stance\": \"supports\",\n       \"note\": \"Buck's BUY table gives 'Skt. krī- (paṇ-)' as the ordinary Sanskrit word for 'buy'.\"},\n      {\"src\": \"CHEUNG\", \"where\": \"p. 446\", \"stance\": \"supports\",\n       \"note\": \"'*SANSKRIT: kray \\\"to buy\\\" (RV, AV+) > EWAia I: 410' listed as the Indo-Aryan match of Iranian *xraiH.\"}\n     ]\n    },\n    {\n     \"id\": 4, \"lang\": \"Sogdian\", \"words\": \"xr`yn\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Sogdian γr'yn- / xryn- 'to buy' is the Sogdian reflex of the same Old Iranian nasal present *xri-na-; Gharib's dictionary reads it xarīn, with past stem γr'yt- xarīt and the agent noun γr'yn'k xarīne 'buyer'. Nourai's transliteration 'xr`yn' (backtick = aleph) reproduces the Buddhist-Sogdian spelling xr'yn exactly as Cheung cites it. Sogdian shows the whole family: Christian ptxryn 'to hire' (*pati-), Buddhist sxr'n 'to re-buy' (*us-), xryc 'purchase', xrycyq 'prostitute' (lit. 'purchasable'). Note that Sogdian preserves the nasal present that Persian lost (Persian re-built xar- from the past stem xarīd).\",\n     \"derivation_fa\": \"سغدی γr'yn- / xryn- «خریدن» بازماندهٔ همان ستاک حالِ خیشومی ایرانی باستان *xri-na- است؛ غریب آن را xarīn می‌خواند و ستاک گذشتهٔ آن γr'yt- (xarīt) و اسم فاعل γr'yn'k «خریدار» را نیز آورده است. آوانویسی نورایی «xr`yn» (که در آن ` نشانهٔ الف است) دقیقاً همان املای سغدی بودایی xr'yn است که چونگ نیز نقل می‌کند. سغدی همچنین ptxryn «اجیر کردن» (با پیشوند *pati-)، sxr'n «بازخرید کردن» (با *us-) و xryc «خرید» را دارد. نکته آنکه سغدی ستاک خیشومی را نگاه داشته، حال آنکه فارسی آن را از دست داده و «خر-» را از «خرید» بازساخته است. ادعای نورایی درست است.\",\n     \"sources\": [],\n     \"ref_check\": [\n      {\"ref\": \"SOD:167\", \"status\": \"supports\",\n       \"note\": \"SOD_pages.txt leaf 232 (printed ≈166, the spread that runs on to 167): entry '4197 γr'yn- B, S | xarin (γryn-?) ⓔSkt. kriṇāti ⇒*xryn- | (to)buy', followed by '4198 γr'yn'k ... buyer, purchaser' and '4200 γr'yt- ... xarit'. The same verb appears again as '10641 xryn- S, C | xarin ⇒γr'yn- | (to)buy, (re)purchase' on printed p.433. Nourai's page number is off by at most one leaf.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"CHEUNG\", \"where\": \"p. 446 s.v. *xraiH, Sogdian section\", \"stance\": \"supports\",\n       \"note\": \"'*SOGDIAN: SSogd. xryn, BSogd. xr'yn \\\"to buy\\\" || (+ *upa-) MSogd. prxyy \\\"payment, wages\\\" || (+ *us-) BSogd. sxr'n \\\"to rebuy\\\" || (+ *pati-) CSogd. ptxryn \\\"to hire\\\"' — literally Nourai's form.\"},\n      {\"src\": \"POK\", \"where\": \"p. 648\", \"stance\": \"silent\",\n       \"note\": \"Pokorny's kʷrei- article lists Old Indic, New Persian, Celtic, Baltic, Slavic and Tocharian but no Sogdian; the Sogdian link comes only from Gharib/Cheung.\"}\n     ]\n    },\n    {\n     \"id\": 5, \"lang\": \"Greek\", \"words\": \"priamus\", \"verdict\": \"disputed\",\n     \"derivation\": \"Two things are conflated here. (a) The Greek VERB is πρίαμαι priamai 'I buy' (suppletive aorist ἐπριάμην to ὠνέομαι), and it is a genuine reflex of *kʷreyh₂-: Greek *kʷri- > πρι- by the regular labiovelar > labial development before a front vowel, confirmed by Mycenaean qi-ri-ja-to 'he bought'. (b) But 'priamus' with the gloss 'redeemed' is not that verb: it is the Latin form Priamus of the Trojan king's name Πρίαμος, which Nourai (following Klein p.1241) glosses 'redeemed' and hangs on πρίαμαι. That equation is an ancient folk etymology, built on the story (Apollodorus, Bibliotheca, 1st-2nd c. AD) that Podarces' sister Hesione 'bought' his freedom from Heracles with a veil, whence his new name. Modern scholarship rejects it: Πρίαμος (Aeolic Πέρραμος, Πέραμος — a vocalism incompatible with *kʷrih₂-) is taken as an Anatolian name, Luwian Pa-ri-a-mu-a- 'exceptionally courageous', attested as a man's name at Zazlippa in Kizzuwatna and echoed in Cappadocian Greek Παραμοας. So the arrow root > 'priamus \\\"redeemed\\\"' is disputed as drawn, though a node 'Greek πρίαμαι \\\"to buy\\\"' would have been confirmed.\",\n     \"derivation_fa\": \"در این گره دو چیز درهم آمیخته است. نخست، فعل یونانی πρίαμαι «می‌خرم» به‌راستی بازماندهٔ *kʷreyh₂- است: *kʷr در یونانی پیش از واکهٔ پیشین به pr بدل شده و صورت میسنی qi-ri-ja-to «خرید» آن را تأیید می‌کند. دوم، اما «priamus» با معنی «بازخریده» آن فعل نیست، بلکه صورت لاتینی نام شاه تروا Πρίαμος است که نورایی به پیروی از کلاین (ص ۱۲۴۱) معنی «بازخریده» بدان داده و از πρίαμαι مشتق کرده است. این ریشه‌شناسی عامیانه‌ای کهن است و بر داستان آپولودوروس (سدهٔ یکم-دوم میلادی) تکیه دارد که هسیونه، خواهر پودارکس، آزادی او را از هراکلس «خرید». پژوهش امروزی آن را رد می‌کند: Πρίαμος (در گویش آیولی Πέρραμος/Πέραμος، با واکه‌ای ناسازگار با *kʷrih₂-) نامی آناتولیایی و برگرفته از لووی Pa-ri-a-mu-a- «بسیار دلیر» دانسته می‌شود. پس این پیکان به شکلی که کشیده شده پذیرفتنی نیست، هرچند اگر گره را «یونانی πρίαμαι: خریدن» می‌نوشت، درست می‌بود.\",\n     \"sources\": [W_PRIAMOS, WP_PRIAM, W_PIE_BUY],\n     \"ref_check\": [\n      {\"ref\": \"KLN:1241\", \"status\": \"supports\",\n       \"note\": \"KLN_1966.txt leaf 662 (= printed pp.1241-1242), s.v. Priam: 'L. Priamus, fr. Gk. Πρίαμος, \\\"Priam\\\", a name prob. meaning \\\"redeemed\\\", and rel. to πρίαμαι, \\\"to buy\\\", fr. I.-E. base *qwri-, \\\"to buy\\\"'. Klein does say exactly what Nourai's chart says — Nourai reports his source faithfully; it is Klein's 1966 view that modern scholarship has abandoned.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"p. 648\", \"stance\": \"partial\",\n       \"note\": \"'gr. πρίαμαι ,kaufe'' is listed under kʷrei-, i.e. Pokorny confirms the VERB but says nothing about the personal name Πρίαμος.\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. I 524\", \"stance\": \"partial\",\n       \"note\": \"'gr. πρίαμαι „kaufe“' under qʷrei-; again only the verb, no name.\"},\n      {\"src\": \"CHEUNG\", \"where\": \"p. 446, IE cognates\", \"stance\": \"partial\",\n       \"note\": \"'Gr. πρίασθαι \\\"to strike a bargain\\\", (Myc.) qi-ri-ja-to \\\"he bought\\\"' — the Mycenaean form fixes the verb's prehistory but is unrelated to the name.\"},\n      {\"src\": \"KLN\", \"where\": \"1971 one-vol. ed., s.v. Priam (KLN_1971.txt line 191071)\", \"stance\": \"supports\",\n       \"note\": \"The 1971 reprint keeps the identical wording, 'a name prob. meaning \\\"redeemed\\\"'.\"}\n     ]\n    },\n    {\n     \"id\": 6, \"lang\": \"English\", \"words\": \"Priam\", \"verdict\": \"disputed\",\n     \"derivation\": \"English Priam is simply the Latin Priamus (Greek Πρίαμος) taken over in Middle English through the mediaeval Troy romances (Chaucer, Troilus and Criseyde; Lydgate's Troy Book) with the usual loss of the Latin nominative ending -us, exactly like Marcus > Mark, Paulus > Paul. That transmission (node #5 > #6, as a name) is uncontroversial. What is disputed is the sense Nourai's chart attaches to it — that the name means 'redeemed' and therefore belongs under the root 'to buy'. The name is now standardly derived from Luwian Pa-ri-a-mu-a- 'exceptionally courageous'; the 'ransomed' story is a late Greek folk etymology first attested in mythographers of the 1st-2nd c. AD, long after the name itself. Nourai's node also has no refs of its own, so nothing beyond Klein's Priam entry stands behind it.\",\n     \"derivation_fa\": \"«Priam» انگلیسی همان Priamus لاتینی (از Πρίαμος یونانی) است که در انگلیسی میانه از راه داستان‌های تروا (چاسر، لیدگیت) وارد شده و مانند Marcus > Mark و Paulus > Paul پایانهٔ -us افتاده است؛ این بخشِ انتقال بی‌چون‌وچراست. آنچه محل اختلاف است معنایی است که نمودار بدان می‌دهد: اینکه نام به معنی «بازخریده» باشد و از این رو زیر ریشهٔ «خریدن» بنشیند. امروزه این نام را از لووی Pa-ri-a-mu-a- «بسیار دلیر» می‌گیرند و داستان «بازخرید» را ریشه‌شناسی عامیانهٔ یونانی متأخر (سدهٔ یکم-دوم میلادی) می‌دانند. این گره در کتاب هیچ ارجاعی ندارد و تنها تکیه‌اش مدخل Priam در کلاین است. پژوهش امروزی این پیکان را رد می‌کند.\",\n     \"sources\": [W_PRIAMOS, WP_PRIAM],\n     \"ref_check\": [\n      {\"ref\": \"None\", \"status\": \"not_checked\",\n       \"note\": \"The node carries no refs= in the book; the only reference behind it is the parent node's KLN:1241 (Klein s.v. Priam), which was checked and does support Nourai's wording.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"1966 ed. pp.1241-1242, s.v. Priam\", \"stance\": \"supports\",\n       \"note\": \"'Priam, n., king of Troy and husband of Hecuba (Greek mythol.) — L. Priamus, fr. Gk. Πρίαμος' — the Latin-to-English route, and the 'redeemed' gloss Nourai copies.\"},\n      {\"src\": \"SKT\", \"where\": \"SKT.txt (Skeat, Concise)\", \"stance\": \"silent\",\n       \"note\": \"Skeat's concise dictionary has no entry for the proper name Priam, so it neither supports nor contradicts.\"},\n      {\"src\": \"WEB\", \"where\": \"WEB_vol1.txt\", \"stance\": \"silent\",\n       \"note\": \"Webster's Twentieth Century volume on disk covers only the first half of the alphabet; no Priam entry available to check.\"}\n     ]\n    }\n   ]\n  },\n  {\n   \"entry\": 1,\n   \"root\": \"Kwsep\",\n   \"verdict\": \"plausible\",\n   \"modern_form\": \"PIE *kʷsep- / noun *kʷséps 'night, darkness'\",\n   \"note\": \"Pokorny p.649 does have this root, but he prints it with a question mark and a deliberately hedged heading: 'kʷsep- (?) und einigermaßen anklingende Worte für „Dunkel“' — i.e. the Indo-Iranian side (Skt. kṣáp, kṣapā́ 'night'; Av. xšap- 'darkness') is solid, while the Greek material he groups with it (ψέφας, ψέφος, κνέφας, δνόφος, ζόφος) has an anlaut that keeps changing, which he explains only as 'Tabu-Vorstellungen'. Walde-Pokorny I 524 f. is equally cautious. Wiktionary/LIV-based reconstruction now sets up a noun *kʷséps > PIIr. *kšáps > PIr. *xšáfš, which is essentially Nourai's root with a firmer shape. So the root is real and the gloss 'darkness' is defensible (Pokorny glosses 'Dunkel'; the Indo-Iranian words mean 'night'), but the Greek comparanda that alone justify the labiovelar are uncertain — hence 'plausible' rather than 'confirmed'.\",\n   \"note_fa\": \"پوکورنی در ص ۶۴۹ این ریشه را با علامت پرسش و عنوانی محتاطانه آورده است: «kʷsep- (؟) و واژه‌هایی که تا اندازه‌ای بدان می‌مانند و معنی تاریکی دارند». بخش هندوایرانی آن استوار است (سنسکریت kṣáp، kṣapā́ «شب»؛ اوستایی xšap- «تاریکی»)، اما واژه‌های یونانی که وی کنار آن می‌نهد (ψέφας، κνέφας، δνόφος، ζόφος) آغازهٔ ناپایدار دارند و پوکورنی آن را تنها با «تصورات تابو» توجیه می‌کند؛ والده-پوکورنی (ج ۱ ص ۵۲۴) نیز همین احتیاط را دارد. بازسازی امروزی اسم *kʷséps > هندوایرانی *kšáps > ایرانی *xšáfš را می‌نهد که همان ریشهٔ نورایی با پیکربندی استوارتر است. پس ریشه واقعی و معنای «تاریکی» پذیرفتنی است، ولی چون تنها گواه لبی‌کامی بودنِ آغازه همان واژه‌های یونانیِ مشکوک است، این ادعا با احتیاط پذیرفتنی است، نه قطعی.\",\n   \"sources\": [W_XSAFS, W_SAB],\n   \"ref_check\": [\n    {\"ref\": \"POK:649\", \"status\": \"supports\",\n     \"note\": \"POK_02.txt leaf 310 (printed p.649): 'kʷsep- (?) und einigermaßen anklingende Worte für „Dunkel“. Ai. kṣáp, kṣapā ,Nacht'; av. xšap- ,Dunkelheit'; gr. ψέφας, ψέφος n. ,Dunkel' ... Der wechselnde gr. Anlaut beruht auf Tabu-Vorstellungen. WP. I 524 f., WH. I 289'. Confirmed independently via POK_full.txt ('Root/lemma: kʷsep- (?)', 'Page(s): 649'). The page is right; the '(?)' is Nourai's silent omission.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"WLD\", \"where\": \"Bd. I 524-525 (WLD_Bd1_pages.txt leaves 532-533)\", \"stance\": \"partial\",\n     \"note\": \"'qʷsep- (?) und einigermaßen anklingende Worte für „Dunkel“. Ai. kṣáp, kṣapā „Nacht“, av. xšap- „Dunkelheit“; gr. ψέφας, ψέφος „dunkel“ ... gr. φ statt π kann von den folgdn. gr. Worten bezogen sein, deren Zugehörigkeit oder auch Verwandtschaft untereinander nicht behauptet werden kann' — the Greek connection is explicitly not asserted.\"},\n    {\"src\": \"SYN\", \"where\": \"14.42 NIGHT, p.992 (SYN.txt leaves 1068-1069)\", \"stance\": \"supports\",\n     \"note\": \"Buck's NIGHT table lists 'Skt. rā́tri-, kṣap-, nakt-' and 'Av., OPers. xšap-'; the discussion adds 'Skt. kṣap-, Av. xšap-, xšapā, xšapan-, xšapar-, OPers. xšap- (Barth. 548 f.) : Grk. ψέφας, ψέφος \\\"darkness\\\". Walde-P. 1.524 f.' — Nourai's page number 992 is exactly right.\"},\n    {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt\", \"stance\": \"silent\",\n     \"note\": \"Watkins' 1985 appendix has no *kʷsep- entry (grep 'ksep' returns nothing); the root is not part of the AHD list, so Nourai's POK-only citation is appropriate.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Avestan\", \"words\": \"xšap ; xšâfniya ; xšapan\", \"verdict\": \"confirmed\",\n     \"derivation\": \"All three are genuine Avestan, though the glosses need a small correction. (a) xšap- / xšapā- 'night' is Bartholomae's headword 'j. xšapan-, xšapā- f., n. \\\"Nacht\\\"' (AiW cols. 548 f.), used in the day/night antithesis (aiwi ... xšapō 'by night' Yt.1.28); Old Persian has the same stem, DB 1.20 xšapavā raucapativā 'either by night or by day' (Kent). (b) xšafnya- is Bartholomae's 'j. xšafnya- n. \\\"Nacht-, Abendmahl\\\"', i.e. the evening meal — an adjective *xšafn-ya- 'nocturnal' built on the oblique stem xšafn- of xšapan-, substantivised; Yt.14.20 uxšafni xšafnīm isəmnō 'seeking the evening meal in the evening dusk' (Bartholomae's a-xšapan- 'Abenddunkel' in the same line). Nourai's spelling 'xšâfniya' has a spurious long â and an extra -i-; the standard form is xšafnya-. (c) xšapan- is the ordinary n-stem NOUN 'night' (thrixšaparəm 'for three nights'), not an adjective 'nightly' as Nourai glosses it — his 'nightly' comes from adverbial accusatives like taras-ca xšapanəm 'through the whole night'. Substance correct, glosses slightly loose.\",\n     \"derivation_fa\": \"هر سه صورت اوستایی راستین‌اند، هرچند معنی‌ها اندکی نیازمند اصلاح‌اند. نخست xšap-/xšapā- «شب»: بارتولومه مدخل «xšapan-, xšapā- مؤنث و خنثی، Nacht» را در ستون‌های ۵۴۸ به بعد آورده است؛ همین ستاک در پارسی باستان نیز گواهی شده: xšapavā raucapativā «چه شب و چه روز» (بیستون ۱:۲۰، به روایت کنت). دوم xšafnya-: بارتولومه آن را «xšafnya- خنثی، Nacht-, Abendmahl» (شام، خوراک شبانه) می‌خواند؛ صفتی است به معنی «شبانه» ساخته بر ستاک غیرفاعلی xšafn- و سپس اسم شده — یشت ۱۴:۲۰ uxšafni xšafnīm isəmnō «در تاریکیِ شامگاه، جویای خوراکِ شب». املای نورایی «xšâfniya» یک آی کشیدهٔ نابجا و یک ی افزوده دارد؛ صورت معیار xšafnya- است. سوم xšapan-: خودِ اسم است («شب»، چنانکه در θrixšaparəm «سه‌شبه») نه صفت «شبانه»؛ معنی «nightly» نزد نورایی از کاربردهای قیدیِ حالت مفعولی مانند tarasca xšapanəm «سراسر شب» برخاسته است. جانِ ادعا درست است و تنها معادل‌ها اندکی سست‌اند.\",\n     \"sources\": [W_XSAFS],\n     \"ref_check\": [\n      {\"ref\": \"POK:649\", \"status\": \"supports\",\n       \"note\": \"POK_02.txt leaf 310 (p.649): 'av. xšap- ,Dunkelheit'' listed immediately after 'Ai. kṣáp, kṣapā ,Nacht''.\"},\n      {\"ref\": \"DRM2:161\", \"status\": \"supports\",\n       \"note\": \"DRM.txt leaf 547 (Tome II printed p.161, leaf 546 carries the numeral '160'): the article headed 'KHSHAFNÎM et ÇUIRIM (Soc. de Ling. V, 76)' — 'Khshafnya, dérivé de khshapan - khshafnō, nuit, signifie «nocturne», et hām pacaiti khshafnīm signifie «fait cuire (le repas) du soir»' (on Y. 61.18) and, further on, the Yt.14.20 citation 'uxšafni xšafnīm isəmnō'. Darmesteter's page is exactly Nourai's DRM2:161.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BRT\", \"where\": \"AiW s.v. xšapan-/xšapā- and xšafnya- (BRT.txt lines 10786, 10808, 3140)\", \"stance\": \"supports\",\n       \"note\": \"'j. xšapan-, xšapā- f., n. \\\"Nacht\\\"'; 'j. xšafnya- n. \\\"Nacht-, Abendmahl\\\"'; 'j. a-xšapan- f. \\\"Abenddunkel\\\", uxšafni xšafnīm isəmnō \\\"im Abenddunkel sich das Abendmahl suchend\\\" Yt 14.20'. Bartholomae writes xšafnya-, not Nourai's xšâfniya.\"},\n      {\"src\": \"KNT\", \"where\": \"Kent, Old Persian §188 and DB 1.20 (KNT.txt lines 2224, 2672)\", \"stance\": \"supports\",\n       \"note\": \"'the stems ending in ... p (xšap- \\\"night\\\", ap- \\\"water\\\")'; 'DB 1.20 xšapavā raucapativā ava akunavayatā \\\"either by night or by day, that was done\\\"' — Old Persian has the same stem, which strengthens rather than weakens Nourai's Avestan box.\"},\n      {\"src\": \"SYN\", \"where\": \"14.42 NIGHT, p.992\", \"stance\": \"supports\",\n       \"note\": \"'Skt. kṣap-, Av. xšap-, xšapā, xšapan-, xšapar-, OPers. xšap- (Barth. 548 f.)'.\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Persian\", \"words\": \"šab «شب» ; šabdîz «شبدیز» ; šabestan «شبستان» ; šâm «شام (شامگاه)»\", \"verdict\": \"confirmed\",\n     \"derivation\": \"(1) شب šab < MP šab (Book Pahlavi špc, heterogram LYLYA, Manichaean šb) < Old Persian/Avestan xšap-, the regular Persian simplification of initial xš- to š- (cf. xšāyaθiya > šāh, xšuδra > šīr; Hübschmann, Pers. Stud., lists 'šab \\\"Nacht\\\" = ap. xšapa-(vā)' among his examples of this change). Nyberg gives the whole line: 'šap [šp; LYLY'] night ... Av. xšap-, xšapā, xšapan- (xšafn-); OP xšap-; MPrth Prs šb; Paz. šav; NP šab.' (2) شام šām 'supper, evening' is NOT from xšap- directly but from the derivative Av. xšafnya- 'evening meal': *xšafnya- > *xšamnya- (the n of the cluster -fn- anticipated before the labial, then assimilation) > MP šām, exactly as Darmesteter reconstructs it ('*khshapnya > *khshamp-nya, *khshamf-nya, *khshamnya, *khshām ... c'est par suite un doublet de shab'). Horn no.768 states it flatly: 'šām \\\"Abendmahlzeit, Nachtessen\\\". aw. xšāfnya-, phlv. šām'. So šām and šab are doublets — Nourai's chart, which puts both under the Avestan node, is right. (3) شبدیز šabdīz 'Khosrow Parviz's black horse' = شب šab + دیز dīz 'colour, hue'; Borhan-e Qate' spells it out: «نام اسپ خسرو پرویز بوده. گویند رنگ آن سیاه بود و وجه تسمیهٔ آن شب‌رنگ است چه دیز بمعنی رنگ باشد», with Mo'in's footnote «از: شب + دیز. رک: دیز». (4) شبستان šabestān = شب šab + the place suffix -stān, MP šabestān 'gynaeceum, private (night) apartments' (MacKenzie), so literally 'night-place' — Nourai's gloss and his cross-reference to the Sta root are both right. The extras شبگیر، شبگرد، شبرنگ، شباهنگ are transparent compounds of the same šab.\",\n     \"derivation_fa\": \"«شب» از فارسی میانهٔ šab (در پهلوی کتابی با هزوارش LYLYA و در مانوی šb)، و آن از xšap- پارسی باستان/اوستایی است؛ خوشهٔ آغازین xš در فارسی به ش ساده شده است، همان‌گونه که xšāyaθiya > شاه و xšuδra > شیر (هوبشمان نیز «شب = ap. xšapa-» را در شمار همین نمونه‌ها آورده). نیبرگ سراسر زنجیره را می‌دهد: «šap ... اوستایی xšap-, xšapan- (xšafn-)؛ پارسی باستان xšap-؛ پارتی و فارسی میانه šb؛ پازند šav؛ فارسی نو شب». «شام» اما یکسره از xšap- نیست بلکه از مشتق اوستایی xšafnya- «خوراک شب» است: *xšafnya- > *xšamnya- (قلبِ ن پیش از همخوان لبی و سپس همگونی) > šām فارسی میانه؛ دارمستتر همین را گام‌به‌گام بازسازی کرده و «شام» را «دوگانهٔ شب» خوانده است، و هرن (شمارهٔ ۷۶۸) می‌نویسد: «šām «شام، خوراک شب»، اوستایی xšāfnya-، پهلوی šām». «شبدیز» = شب + دیز «رنگ»؛ برهان قاطع می‌گوید «نام اسپ خسرو پرویز بوده... وجه تسمیهٔ آن شب‌رنگ است چه دیز بمعنی رنگ باشد» و حاشیهٔ معین «از: شب + دیز» را می‌افزاید. «شبستان» = شب + پسوند مکانِ -ستان، فارسی میانه šabestān «حرم، خوابگاه». افزوده‌های شبگیر و شبگرد و شبرنگ و شباهنگ نیز ترکیب‌های آشکار همین «شب»اند. ادعای نورایی در همهٔ چهار واژه درست است.\",\n     \"sources\": [W_SAB, W_SAM, W_SABEST, W_XSAFS, VJ_SAB, AB_SABDIZ],\n     \"ref_check\": [\n      {\"ref\": \"MON\", \"status\": \"supports\",\n       \"note\": \"Mo'in (via vajehyab.com/moein/شب): «(شَ) [ په . ] (اِ.) زمانِ بین غروب خورشید تا سپیده دم» — the tag [په.] marks شب as inherited from Pahlavi. For شبدیز, Mo'in (via abadis.ir): «(شَ ) (ص مر.) شب رنگ، سیه فام، نام اسب خسرو پرویز» — 'night-coloured', exactly Nourai's gloss.\"},\n      {\"ref\": \"BQT:1229\", \"status\": \"supports\",\n       \"note\": \"BQT_v3_pages.txt leaf 19 (printed ≈1228-1229, the شام spread) carries Mo'in's footnote: «# شام - اوستا xshafniya، پهلوی sham (غذای شب) «تاوادیا ... اونوالا ...»، کردی shame (عصر، شب)» — precisely the Av. xšafnya- > MP šām > NP شام chain Nourai draws.\"},\n      {\"ref\": \"BQT:1239\", \"status\": \"supports\",\n       \"note\": \"BQT_v3_pages.txt leaf 30 (printed ≈1239) opens the شب family (شب‌افروز، شبان، شب‌النگ...); Mo'in's footnote 8 there says Horn attributes the n of شبان/شبانگاه to «تلفظ قدیم xshapan (اوستا = شب)». The compounds Nourai names follow immediately: شبدیز p.1243 («وجه تسمیهٔ آن شب‌رنگ است چه دیز بمعنی رنگ باشد»; footnote «از: شب + دیز»), شبرنگ and شبستان p.1244 (footnote «از: شب + ستان (پسوند مکان) ... پهلوی šabestān (حرم شاهی)»), شبگیر p.1246.\"},\n      {\"ref\": \"HRN:169\", \"status\": \"supports\",\n       \"note\": \"HRN.txt leaf 190 = printed p.169, entry '768. šām \\\"Abendmahlzeit, Nachtessen\\\". aw. xšāfnya-, phlv. šām (Y. 61 (19) = 62, 7). LW. kurd. šām \\\"Abend\\\"; afgh. šāme ...' — Horn's page is exactly right for the شام arrow.\"},\n      {\"ref\": \"SYN:992\", \"status\": \"supports\",\n       \"note\": \"SYN.txt leaves 1068-1069 (printed 992-993), section 14.42 NIGHT: 'Skt. kṣap-, Av. xšap-, xšapan-, xšapar-, OPers. xšap- (Barth. 548 f.) : Grk. ψέφας, ψέφος \\\"darkness\\\"'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie 1971, s.v. šab, šabestān, šām (PHD.txt line 574, 583)\", \"stance\": \"supports\",\n       \"note\": \"'šab [LYLYA < A lyly'; šp | M šb, N ~] night. ~estān [špst'n' | N ~] gynaeceum, private apartments.' and 'šām [š'm | = P, N ~] evening meal, supper.' — all three Persian words already exist in Middle Persian in Nourai's meanings.\"},\n      {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II, glossary s.v. šap\", \"stance\": \"supports\",\n       \"note\": \"'šap [šp; LYLY\\\"] night ... — Av. (548 sq.) xšap-, xšapā, xšapan- (xšafn-); OP xšap-; MPrth Prs šb; Paz. šav; NP šab.' — the fullest single statement of Nourai's arrow.\"},\n      {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien (HUB.txt lines 8303-8305, 6249)\", \"stance\": \"supports\",\n       \"note\": \"In the section on Persian š- from Old Iranian xš-: 'šōm \\\"Nachtessen\\\", zd. xšafnya-; ... šab \\\"Nacht\\\" = ap. xšapa-(vā) \\\"des Nachts\\\"'.\"},\n      {\"src\": \"BQT\", \"where\": \"vol. 3 pp.1243-1244 (شبدیز، شبرنگ، شبستان)\", \"stance\": \"supports\",\n       \"note\": \"Quoted in ref_check above; Mo'in's footnotes analyse شبدیز as شب+دیز and شبستان as شب+ستان with Pahlavi šabestān 'royal harem' (citing Unvala).\"},\n      {\"src\": \"CHEUNG\", \"where\": \"CHEUNG.txt\", \"stance\": \"silent\",\n       \"note\": \"Cheung's dictionary covers verbs only; šab/šām are nouns, so it has nothing to say here.\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"Sogdian\", \"words\": \"`xšp ; xš`m\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Both forms are in Gharib. (a) 'xšp (Nourai's `xšp, the backtick standing for aleph) is Buddhist/Sutra Sogdian (ə)xšap 'night', which Gharib derives outright from *xšapa- — the Sogdian prothetic aleph is the regular device for writing an initial cluster xš-, so the word is the exact Sogdian counterpart of Persian šab (Persian simplified the cluster, Sogdian propped it up with a vowel). (b) xš'm 'evening' is (ə)xšām, the Sogdian match of Persian شام, and Gharib herself glosses it 'Av. xšafnya-, Parth. šām' — the same *xšafnya- > *xšāmn- > šām development, so Sogdian independently confirms the route Darmesteter and Horn reconstruct for Persian. Gharib also has the compound xš'm xwr- 'to have dinner' and xš'm xwrnyy 'supper', matching Persian شام خوردن.\",\n     \"derivation_fa\": \"هر دو صورت در فرهنگ سغدی غریب هست. نخست 'xšp (همان «`xšp» نورایی که در آن ` نشانهٔ الف است) یعنی (ə)xšap «شب» در سغدی بودایی، که غریب آن را یکراست از *xšapa- می‌گیرد؛ الفِ آغازین در سغدی تنها برای نگاشتن خوشهٔ xš- افزوده شده است. پس این واژه همتای دقیق «شب» فارسی است: فارسی خوشه را ساده کرده و سغدی آن را با واکهٔ کمکی نگاه داشته است. دوم xš'm یعنی (ə)xšām «شامگاه»، همتای «شام» فارسی، که خود غریب آن را با «اوستایی xšafnya-، پارتی šām» برابر نهاده است؛ بدین‌گونه سغدی همان مسیری را تأیید می‌کند که دارمستتر و هرن برای فارسی بازسازی کرده‌اند. ترکیب xš'm xwr- «شام خوردن» و xš'm xwrnyy «شام» نیز در همان فرهنگ آمده است. ادعای نورایی درست است.\",\n     \"sources\": [],\n     \"ref_check\": [\n      {\"ref\": \"SOD:29\", \"status\": \"supports\",\n       \"note\": \"SOD_pages.txt leaf 94 (printed ≈28-29): entry '737 'xšp- B, S | (ə)xšap ⓔ<*xšapa ⓕf.n. -h, ob. -yh ⇒'xšp- | night'; entry 739 ''xšpcykk | (ə)xšapcīk' follows. Nourai's page number is right to within one leaf.\"},\n      {\"ref\": \"SOD:432\", \"status\": \"supports\",\n       \"note\": \"SOD_pages.txt leaf 499 (which carries the printed numeral '433'): entry '10648 xš'm M, C | xšām (ysto) ⓔAv. xšafnya-, Parth. šām | evening', with '10649 xš'm xwr- ... (to)have dinner' and '10650 xš'm xwrnyy ... supper'. Nourai's 432 is the facing page of the same spread.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"CHEUNG\", \"where\": \"CHEUNG.txt\", \"stance\": \"silent\",\n       \"note\": \"Verb-only dictionary; no entry for the Sogdian nouns 'xšp / xš'm.\"},\n      {\"src\": \"POK\", \"where\": \"p. 649\", \"stance\": \"silent\",\n       \"note\": \"Pokorny's kʷsep- article cites only Old Indic, Avestan and Greek; no Sogdian material, so the Sogdian node rests on Gharib alone.\"},\n      {\"src\": \"NYB\", \"where\": \"Nyberg II s.v. šap\", \"stance\": \"partial\",\n       \"note\": \"Nyberg's cognate list for MP šap gives Avestan, Old Persian, Parthian, Pazand and New Persian but not Sogdian; it corroborates the Iranian *xšap- family without touching this node directly.\"}\n     ]\n    }\n   ]\n  }\n ]\n}\n\nwith io.open('/home/sfmqrb/git/rishe/data/verification/page-299.json','w',encoding='utf-8') as f:\n    json.dump(data,f,ensure_ascii=False,indent=2)\n    f.write('\\n')\nprint('written')\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk299.py"
}
```


### [2026-09-06T22:51:29.624Z] TOOL RESULT

```
written
```


## [2026-09-06T22:51:32.212Z] TOOL CALL #76: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-299.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 299"
}
```


### [2026-09-06T22:51:34.764Z] TOOL RESULT

```
JSON OK
nodes verified: 9/9
node verdicts: {'plausible': 1, 'confirmed': 6, 'disputed': 2}
root verdicts: {'confirmed': 1, 'plausible': 1}
ref checks: {'partial': 2, 'supports': 16, 'not_checked': 1}
books consulted: {'silent': 8, 'partial': 5, 'supports': 18} | by book: {'CHEUNG': 7, 'POK': 3, 'BRT': 2, 'KNT': 2, 'PHD': 2, 'HUB': 2, 'WLD': 2, 'SYN': 2, 'KLN': 2, 'NYB': 2, 'HRN': 1, 'ARY': 1, 'SKT': 1, 'WEB': 1, 'BQT': 1}
```


## [2026-09-06T22:51:41.876Z] TOOL CALL #77: Bash

```json
{
 "command": "ls site/pages/299.jpg 2>/dev/null || pdftoppm -f 299 -l 299 -r 150 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg299 && echo done"
}
```


### [2026-09-06T22:51:44.171Z] TOOL RESULT

```
site/pages/299.jpg
done
```


## [2026-09-06T22:51:46.424Z] TOOL CALL #78: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/site/pages/299.jpg"
}
```


### [2026-09-06T22:51:46.448Z] TOOL RESULT

```

```


## [2026-09-06T22:51:58.804Z] TOOL CALL #79: Bash

```json
{
 "command": "pdftoppm -f 299 -l 299 -r 400 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg299hi && python3 -c \"\nfrom PIL import Image\nim=Image.open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg299hi.png')\nprint(im.size)\nw,h=im.size\n# Sanskrit box ref approx at x 0.23-0.45, y 0.185-0.21 of page\nim.crop((int(0.20*w),int(0.175*h),int(0.46*w),int(0.205*h))).resize((int(0.26*w*2),int(0.03*h*2))).save('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/crop.png')\n\""
}
```


### [2026-09-06T22:52:01.889Z] TOOL RESULT

```
(3400, 4400)
```


## [2026-09-06T22:52:04.256Z] TOOL CALL #80: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/crop.png"
}
```


### [2026-09-06T22:52:04.274Z] TOOL RESULT

```

```


## [2026-09-06T22:52:24.158Z] AGENT

Done. Wrote `/home/sfmqrb/git/rishe/data/verification/page-299.json`; `python3 tools/verify_check.py 299` reports 9/9 nodes, **0 PROBLEM lines**.

**Page 299 (book p. 269) — 2 entries (Kwri/Qwri, Kwsep) + 1 redirect (Kyô → Ki 2, skipped)**

- Node verdicts: 6 confirmed, 1 plausible, 2 disputed
- Root verdicts: 1 confirmed (Kwri), 1 plausible (Kwsep)
- Ref checks: 16 supports, 2 partial, 1 not_checked · consulted: 18 supports, 5 partial, 8 silent (POK, WLD, SYN, CHEUNG, BRT, KNT, PHD, NYB, HRN, HUB, BQT, MON, ARY, KLN, SKT, WEB)

Disputed:
- **Kwri #5 Greek "priamus : redeemed"** — conflates the verb πρίαμαι 'buy' (a real *kʷreyh₂- reflex, Myc. qi-ri-ja-to) with the name Πρίαμος/Lat. Priamus. The "ransomed" sense is a late Greek folk etymology (Apollodorus); modern view = Luwian *Pa-ri-a-mu-a-* 'exceptionally courageous' (Aeolic Πέρραμος rules out *kʷrih₂-). Nourai reports Klein p.1241 faithfully — Klein is the outdated party.
- **Kwri #6 English "Priam"** — same problem; the Latin→English route is fine, the placement under "to buy" is not. No refs of its own.

Plausible (not disputed):
- **Kwri #1 "Avestan / Old Persian xrî"** — form and ancestry right (PIr. *xraiH/*xrī-, Cheung 446) but unattested in either language: no headword in Bartholomae or Kent. Nourai's own source FFD p.50 says "ایرانی باستان" (Old Iranian, reconstructed), not Avestan/OP.
- **Root Kwsep** — Pokorny p.649 prints it as "kʷsep- (?) und einigermaßen anklingende Worte für 'Dunkel'"; the Indo-Iranian side is solid, the Greek comparanda (tabu-shifting anlaut) are not. Nourai silently drops the "(?)".

Minor gloss slips inside confirmed nodes (noted in `derivation`, not flagged): Av. is *xšafnya-*, not "xšâfniya"; *xšapan-* is a noun 'night', not an adjective 'nightly'.

**Extraction errors: none.** Checked the printed page (site/pages/299.jpg + a 400-dpi crop): the JSON matches, including "Greek … priamus : redeemed" and the Sanskrit box's POK:648 (which looks like "848" at low resolution).

Ref-page notes for the owner: KLN:1241, HRN:169, SYN:817/992, DRM2:161, BQT:743/1229/1239, POK:648/649 and FFD:50 all land exactly where Nourai says; SOD:167 and SOD:29,432 are each off by one page/leaf (the entries are at pp. 166 and 28/433). 13 web pages archived via `fetch_source.py`; two fetches failed (etymonline has no Priam entry; the πρίαμαι and Proto-Iranian/xrináHti Wiktionary URLs returned status -1) and are not cited.
