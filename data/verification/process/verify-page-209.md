# Verification process log — verify-page-209


## [2026-09-06T14:51:52.920Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 209 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-209.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-209.json. Write /home/sfmqrb/git/rishe/data/verification/page-209.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 209` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T14:51:54.538Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T14:51:55.257Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T14:51:55.273Z] TOOL RESULT

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


## [2026-09-06T14:51:55.485Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-209.txt"
}
```


### [2026-09-06T14:51:55.508Z] TOOL RESULT

```
1	=== PDF page 209 (book page 179) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Gwer 2, Gwere 1 : to praise, welcome, sing  (refs POK:478)
4	#1 (parent #0) [Avestan] refs=POK:478 | gar 2, gard, grad, grd, grnâti : to call, pray ; garo-gar : fulfiller of prayers, God ; garô-demâna : house of prayer, sky ☞Dem ; paiti-gar : to speak against, blame ☞Per 3
5	  #2 (parent #1) [Persian] refs=HRN:202,204; BQT:1793-1806 | gerîstan «گریستن» : to cry ; garogar «گروگر» : God ; garzmân «گرزمان» : sky ; payğâreh «پیغاره ، بیغاره» : blame | extra: گری ۱ ، گریه
6	  #3 (parent #1) [Pahlavi] refs=MON:3214 | gar-âmîk : revered, respected
7	    #4 (parent #3) [Persian] refs=MON:3214; IEC:376 | gerâmî «گرامی» : dear, respected
8	#5 (parent #0) [Latin] refs=AHD | gratus : agreeable, grateful ; grâtia : favor
9	  #6 (parent #5) [English] refs=None | grace, gracious, grateful, agree, congratulate
10	
```


## [2026-09-06T14:51:58.840Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-209.json",
 "description": "Read source JSON for page 209"
}
```


### [2026-09-06T14:51:58.881Z] TOOL RESULT

```
{
  "pdf_page": 209,
  "book_page": 179,
  "entries": [
    {
      "root": {
        "name": "Gwer 2, Gwere 1",
        "lang": "Indo-European",
        "refs": "POK:478",
        "gloss": "to praise, welcome, sing"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:478",
          "words": [
            {"translit": "gar 2, gard, grad, grd, grnâti", "gloss": "to call, pray", "script": null},
            {"translit": "garo-gar", "gloss": "fulfiller of prayers, God", "script": null},
            {"translit": "garô-demâna", "gloss": "house of prayer, sky", "script": null, "see": ["Dem"]},
            {"translit": "paiti-gar", "gloss": "to speak against, blame", "script": null, "see": ["Per 3"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "HRN:202,204; BQT:1793-1806",
          "words": [
            {"translit": "gerîstan", "gloss": "to cry", "script": "گریستن"},
            {"translit": "garogar", "gloss": "God", "script": "گروگر"},
            {"translit": "garzmân", "gloss": "sky", "script": "گرزمان"},
            {"translit": "payğâreh", "gloss": "blame", "script": "پیغاره ، بیغاره"}
          ],
          "script_extra": "گری ۱ ، گریه",
          "note": null,
          "quote": {
            "text": "فرزند تو امروز بود جاهل وعاصی - فردات چه فریاد رسد پیش گروگر",
            "poet": "Nâser-Khosrow"
          }
        },
        {
          "id": 3,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "MON:3214",
          "words": [
            {"translit": "gar-âmîk", "gloss": "revered, respected", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Persian",
          "refs": "MON:3214; IEC:376",
          "words": [
            {"translit": "gerâmî", "gloss": "dear, respected", "script": "گرامی"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "پذیره فرستاد خسرو سوار - گرانمایگان گرامی هزار",
            "poet": "Ferdowsî"
          }
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "gratus", "gloss": "agreeable, grateful", "script": null},
            {"translit": "grâtia", "gloss": "favor", "script": null}
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
            {"translit": "grace, gracious, grateful, agree, congratulate", "gloss": null, "script": null}
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


## [2026-09-06T14:52:00.891Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','HRN','BQT','MON','IEC','AHD','WLD','BRT','PHD','NYB','HUB','ARY','SYN','KLN','CHEUNG']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:600])\n\"",
 "description": "Inspect refs_online entries"
}
```


### [2026-09-06T14:52:03.283Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h
CHEUNG null
```


## [2026-09-06T14:52:09.103Z] TOOL CALL #5: Bash

```json
{
 "command": "ls data/verification/sources/refs/ | head -60 && echo ---- && python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nprint(d['POK'].get('page_offset'))\nprint(d['IEC'].get('page_offset'))\nprint(d['MON'].get('lookup_hint'))\nprint(json.dumps(d['MON'],ensure_ascii=False)[:1500])\n\""
}
```


## [2026-09-06T14:52:09.535Z] TOOL CALL #6: Bash

```json
{
 "command": "sed -n '1,60p' data/verification/sources/SOURCE_MATRIX.md"
}
```


### [2026-09-06T14:52:10.901Z] TOOL RESULT

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
----
POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks).
{"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/r
```


### [2026-09-06T14:52:10.933Z] TOOL RESULT

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
```


## [2026-09-06T14:52:18.177Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 485 486 487 488; do echo \"=== leaf $n ===\"; awk -v n=$((n+1)) 'BEGIN{RS=\"\\f\"} NR==n' POK_01.txt | head -70; done",
 "description": "Print Pokorny leaves around p.478"
}
```


### [2026-09-06T14:52:20.755Z] TOOL RESULT

```
=== leaf 485 ===
=== leaf 486 ===
=== leaf 487 ===
=== leaf 488 ===
```


## [2026-09-06T14:52:22.891Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls -la POK*.txt && for f in POK_01.txt POK_02.txt POK_03.txt POK_full.txt; do echo \"$f pages: $(awk 'BEGIN{RS=\"\\f\"} END{print NR}' $f)\"; done"
}
```


### [2026-09-06T14:52:25.161Z] TOOL RESULT

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


## [2026-09-06T14:52:27.915Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 133 134 135; do echo \"=== POK_02 leaf $n ===\"; awk -v n=$((n+1)) 'BEGIN{RS=\"\\f\"} NR==n' POK_02.txt | head -80; done"
}
```


### [2026-09-06T14:52:30.416Z] TOOL RESULT

```
=== POK_02 leaf 133 ===
nhd.  Krug  in  der  Bed.  ^Schenke'? Bed.  wie  in  lat.  gurgustium  ^Kneipe^) ;
air.  brägae  ^Hals^  Nacken^  {*g^Yg-¥'-)j  acymr.  ahal-lrouannou  ,guro-u. lionibus^  (eigentlich  ,Äpfel  des  Halses^),  mcymr.  hreuant  ,Luftröhre^  (urkelt. Hräg-)]  acorn.  briansen  ^guttur^;  abret.  Brehant-Dincat  gl.  ^guttur  recep- taculi  pugnae^,  vielleicht  aus  "^brg-,  Pedersen  KG.  100.
Mit  Nasalierung  dazu  vielleicht  gv.  ßgöyxog  m.,  ion.  ßgoyxlr]  ^Luftröhre' ßgdyxia,  ßagayxia  ^Fischkiemen ;  Luftröhrenäste^  scheint  im  Vok.  nach ßqayxGCM  yh'm  heiser^;  ßgccyxos  ^Heiserkeit^  umgebildet^  das  mit  air.  brongide ,heiser^  (oben  103)  verwandt,  aber  von  ßQoyxog  zu  trennen  ist  (:  sßgaxa ^rasselte^  krachte,  brüllte^  ai.  brmhati  ^barrire"^?  Johansson  KZ.  36,  345).
5.  Mit  reinem  Velar :  gr.  ysgysQog '  ßgöyxog  13.es.,  yagyaQswv  ^Zäpfchen im  Munde*",  yaQyaQiCcü  ,gurgle^  (:arm.  kerkerim  ,werde  heiser^?)  vielleicht durch  Entlabialisierung  nach  Formen  mit  yvo-  (yogyrgr]  ,unterirdisches Gefängnis,  Wasserleitung^),  doch  ist  altes  ger-  neben  g^er-  wegen  gel-  neben g^el-  an  sich  unbedenklich.
WP.  I  682  ff.,  WH.  I  627  f.,  Trautmann  89  f.,  98,  Specht  KZ.  59,  110,  1.
2.  g'Aer-,  g'Aero-,  gAersu-,  g'Aeri-  ,schwer^;  g^r-nu-,  g'^räu-'ö(n)-  ,Mühle^; g^erü-s  ,schwer^;  g^rü-to-s  ,schwer^
Ai.  gwm-h  ,schwer,  wichtig,  ehrwürdig^  (Komp.  gdrlyän,  Sup.  gäristha-h) dgru-  ;ledig^,  gru-musti-h  ,schwere  Handvoll^,  garimä  ,Schwere^  (^gV^erd-) ; av.  gouru-  (im  Kompos.)  ,schwer^;  npers.  girän  , schwer^  (agraria- -,  Umbil- dung nach  *fräna-  ,volP) ;
gr.  ßaQvg  ,schwer'^,  ßaQvvo)  ,beschwere^,  ßccgog  n.  ,Schwere'';
lat.  gravis  , schwer,  gewichtig^  (* g^rd-u-is)  ]
mir.  bair  ,schwer^(?),  baire  ,Kummer(?)^,  bruth  ,Gewicht,  Masse*^  (^gV^rutu-), cymr.  bryiü  ,stark.  Stärke^  {Hruwo-),  mir.  brö  ,Menge'';
got.  kaürjös  Nom.  PL  f.  ,schwer^,  kaürjan  ,heschweren^ ;
lit.  gürstu,  gürti  ,sich  legen  (vom  Winde)^,  lett.  gurstu,  guft  ,ermatten  ; sich  legen  (vom  Winde)^,  gurds  ,ermüdet,  matt"^  (vgl.  auch  ßagvg  und gravis  in  der  Bed.  ^beschwert,  niedergedrückt,  matt^),  woran  mit  weiterer Verschiebung  von  ,matt,  beschwert^  zu  ,zahm,  mild^  (vgl.  ahd.  järfiar ,kummervolF  :  gr.  7J(.ieQog  ,zahm^)  vielleicht:
got.  gairrus  ji]nLog,  sanft^,  gairrei  ,Sanftmut^,  anord.  kyrr,  kvirr  ,still, ruhig,  friedlich',  mhd.  kürre,  nhd.  kirre  ,zahm,  zutraulich'  {*gVier-dr6s  oder -erös,  -urös) ;
lett.  gruts  ,schwer'  =  lat.  brütus  (osk.-umbr.  Lehnwort)  ,schwer,  schwer- fällig, gefühllos,  unvernünftig';
toch.  A  kra-marts  ,schwer'  (?) ;   Van  Windekens  Lexique  44.
477
Hierher  ferner  als  rz -Ableitungen  von  g]^er9-  und  g'^eräii-i  go
=== POK_02 leaf 134 ===
t.  (asilu-) qairnus  /Esels) mühle^  (*gVierdnu-),  anord.  kvern  f.  (*gV:erna)  ^Mühlstein; Handmühle^,  ags.  ciceorn  ds.^  ahd.  quirn^  quirna  ds. ;
tiefstufig  bsl.  il-St.  girnü-  f.  ^Handmühle^  (*5'or^w-)  in:
apr.  girnoywis  {*girnuiois),  lett.  dzirnus,  dzirnavas'^  daneben  lett.  dzirnas f.  PL  und  lit.  girnos  f.  PL;  dazu  lit.  gerükstis,  lett.  dzerükslis  m.  ,dens molaris^;
aksl.  zr^n^vi  f.  PL  ^Mühle^^  dazu  zr^nov^  m.  ^Mühlstein^ ;  sloven.  zrndv f.  ^Handmühle^,  poln.  zarna  N.  PL  ds. ;  russ.  zernov  m.  ^Mühlstein^;
aksl.  zr^ny  ^Mühle*,  und  andrerseits  ai.  grävan-  m.  ^Stein  zum  Soma- pressen^,  arm.  erkan  ^Mühlstein^  (*g^ränä)j  air.  brau,  Gen.  broon  ^Mühlstein^ Handmühle^;,  cymr.  breuan  (aus  dem  St.  der  Casus  obliqui  *g^räun-), acorn.  brou,  bret.  bi-eo  (Nominativform  *g]!iräiiö)  ^Mühlstein^
g^eri-:  außer  ai.  gdrl-yan  (?^  s.  oben)  hierher:
gr  ßgid-OQ  n.  ;,Wucht,  Gewicht^  Last^_,  ßqid-vg  ^wuchtig,  schwer^^  ßqt&w ,bin  schwer,  belastet,  trans.  beschwere^,  wohl  auch  ßqt(.i7i  ^(wuchtiger)  An- griff, Zorn,  Scheltwort^,  ßgi^ovad-ai  ,schwer  zürnen^,  oßQt^og  ,gewaltig, stark^,  ßQLfiög'  idyccg,  xalsnög  Hes.;  ßgtagög  ,fest,  stark^,  woneben  die Kompositionsform  */?^t(t)-  in  ßqL-rjnvog  ,heftig  schreiend^,  Bgi-agecog  (,wer großen  Schaden  bringt^),  ßQt-rjQÖv  f^sydlcog  y.€x(XQL(Tix€vov  Hes.  (ßgi'  ßgiagöv und  ßgl'  inl  rov  fj,£y(xXov  vielleicht  erst  aus  den  Kompositis  losgelöst), hierher  mit  Präfix  gr.  v-  (*ud)  wohl  auch  gr.  ijßgig  , Gewalttätigkeit, Frevel,  übermütige  Handlung^,  Vßgig  dvrjg  ,gewalttätiger  Mann^  auf  Grund der  Vorstellung  ,sich  mit  dem  ganzen  Gewicht  seiner  Kraft  auf  etwas stürzen^;  -^(J-Präsens  ßgivöeXv  dvfiovG-9-aL,  igsd-iC^eiv  Hes.;
air.  brlg  ,Kraft,  Macht,  Wert^,  cymr.  bri  ,Würde^,  corn.  bry  ,Wert':
nhd.  Krieg,  ahd.  kreg  ,Hartnäckigkeit^,  mhd.  kriec  ,Anstrengung,  Kampf", md.  mnd.  krlgen  ,sich  anstrengen,  trachten,  kämpfen,  bekommen^  {^grigh-, bzw.  germ.  z.T.  gi^eigh-)??
lett.  grins  ,grausam,  zornig^,  grinums  ,Härte,  Strenge^?
WP.  I  684  ff.,  WH.  I  117  f.,  621,   Trautmann  89.
3.  gf.er-,  g^.or-  ,Berg^,  ursprüngl.  Flexion  g^ores,  Gen.  g'^eros,
Ai.  giri-h  m.  ;,Berg^,  av.  gairi-  ds. ;
alb.  gur  , Felsen,  Stein^  (^-<.^**-)?
^v.  dsigög  (Hes.)  ,HügeP,  vxfjidsigog  ,mit  hohen  Klippen^,  ösigdg,  kret. dr^g&g  f.  ,Hügel,  Anhöhe^  (*^^erio-?);  dazu  ßogiäg  ,Nordwind^  (zu  '^ßögsiog ,montanus^,  Scbwyzer  Gr.  Gr.  I  461  und  Anm.  2);  ßagvsg'  dsvöga  Hes.?;
der  thrak.  VN  ''Ynsg-ßogeoi  ,die  jenseits  d
=== POK_02 leaf 135 ===
es  Berges  Wohnenden^  ent- hält wohl  das  gr.  Lw.  *ßogLg]
478  f
lit.  nugarä  ^Rücken^  Bergrücken^;
mit  der  Bedeutungsentwicklung  ,Berg  — (Berg) wald  — Baum':  lit.  g\re, giriä  ,Wald',  lett.  dzire  ds.,  und  apr.  garian  n.  (Akk.  garrin)  ,Baum'; ferner  lett.  gars  ,Wald',  gärsas  ,Sumpf';
aksl.  gora  ,Berg',  skr.  gbra  ,Berg,  Wald',   usw.
WP.  I  682,  Trautmann  78,  Pedersen  La  einqu.  decl.  lat.  37,  66.
4,  g^er(Q)-  ,die  Stimme  erheben',  bes.  ,loben,  preisen,  willkommen  heißen^, aber  auch  ,schelten;  jammern';  g^?-to-s  ,willkommen'.
Ai.  gpiäti,  grv^t^  ^singt,  lobt,  preist,  kündigt  an'  (Fut.  garisyati,  Abs.  abhU gürya),  sam-girate  ,gelobt,  verspricht',  gurdte  ,begrüßt',  gir  f..  Gen.  girdk ,Lob,  Lied',  av.  gar-,  aibi-gdvdnte  ,preisen,  lobend  einstimmen',  garo  Gen. f.  ,Lob,  Preis;  Loblied'  (=  ai.  girdh),  garali-  n.  ,Lob,  Preislied',  aibi-jardtay^ ,Preisgesang',  aibi-j  ardtar-  ,Lobpreiser'  =  ai.  jaritdr-  ,Anrufer,  Sänger, Preiser',  av.  *ä-gra-  ,zustimmend'  in  ägramati-  ,zustimmenden  Sinnes'; ai.  gürti-h  L  ,Lob'  =  lat.  grätes  PL  f.  ,Dank'  (dazu  grätia  , Annehmlich- keit, Wohlgefälligkeit,  Gnade,  Dank'),  ai.  gürtd-h  ,willkommen'  =  lat. grätus  ,gefällig,  dankenswert,  dankbar';  osk.  brateis  ,gratiae',  ßQaTiü{.L ,münus',  pälign.  bratom]
hierher  gall.-lat.  bardus  ,Barde',  air.  bard,  cymr.  bardd  ds.  (*g^f-d(h)0'S)j
alb.  gershds,  grish  ,zur  Hochzeit  einladen';
lit.  glriüj  gtrti  ,loben,  rühmen',  lett.  dzirties  ,sich  rühmen',  apr.  glrtwei ,loben',  pogirrien  Akk.  Sg.  ,Lob',  auch  lit.  geras  ,gut'  und  aksl.  gram (*gornos)  ,Formel,  Vers'  (u.  dgl.,  siehe  Berneker  332).
Mit  b-  erweitert:  lit.  gerbtl  ,ehren',  garbe  ,Ehre',  apr.  gerbt,  gerbt , sprechen',  girbin  ,Zahl';  anord.  karp  ,Prahlerei'  beweist  nicht  für  ur- sprüngliches g  in  dieser  6-Erw.  gV^er-b-,  da  es  aus  dem  gleich bed.  garj)  durch Kreuzung  mit  Schallworten  mit  germ.  k-  im  Anlaut  umgebildet  sein   wird.
Mit  6^Ä-Erweiterung  vielleicht  hierher  (s.  oben  gall.  bardus)  arm.  kardam ,erhebe  die  Stimme',  lit.  gefdas  ,Geschrei,  Botschaft',  is-girstl  ,zu  höre
```


## [2026-09-06T14:52:59.675Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk -v n=136 'BEGIN{RS=\"\\f\"} NR==n' POK_02.txt | head -40"
}
```


## [2026-09-06T14:53:00.914Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD gwera ===\"; grep -n -i -E \"g\\^?wer|gwer[aə]\" AHD_watkins1985.txt | head -30"
}
```


### [2026-09-06T14:53:01.304Z] TOOL RESULT

```
es  Berges  Wohnenden^  ent- hält wohl  das  gr.  Lw.  *ßogLg]
478  f
lit.  nugarä  ^Rücken^  Bergrücken^;
mit  der  Bedeutungsentwicklung  ,Berg  — (Berg) wald  — Baum':  lit.  g\re, giriä  ,Wald',  lett.  dzire  ds.,  und  apr.  garian  n.  (Akk.  garrin)  ,Baum'; ferner  lett.  gars  ,Wald',  gärsas  ,Sumpf';
aksl.  gora  ,Berg',  skr.  gbra  ,Berg,  Wald',   usw.
WP.  I  682,  Trautmann  78,  Pedersen  La  einqu.  decl.  lat.  37,  66.
4,  g^er(Q)-  ,die  Stimme  erheben',  bes.  ,loben,  preisen,  willkommen  heißen^, aber  auch  ,schelten;  jammern';  g^?-to-s  ,willkommen'.
Ai.  gpiäti,  grv^t^  ^singt,  lobt,  preist,  kündigt  an'  (Fut.  garisyati,  Abs.  abhU gürya),  sam-girate  ,gelobt,  verspricht',  gurdte  ,begrüßt',  gir  f..  Gen.  girdk ,Lob,  Lied',  av.  gar-,  aibi-gdvdnte  ,preisen,  lobend  einstimmen',  garo  Gen. f.  ,Lob,  Preis;  Loblied'  (=  ai.  girdh),  garali-  n.  ,Lob,  Preislied',  aibi-jardtay^ ,Preisgesang',  aibi-j  ardtar-  ,Lobpreiser'  =  ai.  jaritdr-  ,Anrufer,  Sänger, Preiser',  av.  *ä-gra-  ,zustimmend'  in  ägramati-  ,zustimmenden  Sinnes'; ai.  gürti-h  L  ,Lob'  =  lat.  grätes  PL  f.  ,Dank'  (dazu  grätia  , Annehmlich- keit, Wohlgefälligkeit,  Gnade,  Dank'),  ai.  gürtd-h  ,willkommen'  =  lat. grätus  ,gefällig,  dankenswert,  dankbar';  osk.  brateis  ,gratiae',  ßQaTiü{.L ,münus',  pälign.  bratom]
hierher  gall.-lat.  bardus  ,Barde',  air.  bard,  cymr.  bardd  ds.  (*g^f-d(h)0'S)j
alb.  gershds,  grish  ,zur  Hochzeit  einladen';
lit.  glriüj  gtrti  ,loben,  rühmen',  lett.  dzirties  ,sich  rühmen',  apr.  glrtwei ,loben',  pogirrien  Akk.  Sg.  ,Lob',  auch  lit.  geras  ,gut'  und  aksl.  gram (*gornos)  ,Formel,  Vers'  (u.  dgl.,  siehe  Berneker  332).
Mit  b-  erweitert:  lit.  gerbtl  ,ehren',  garbe  ,Ehre',  apr.  gerbt,  gerbt , sprechen',  girbin  ,Zahl';  anord.  karp  ,Prahlerei'  beweist  nicht  für  ur- sprüngliches g  in  dieser  6-Erw.  gV^er-b-,  da  es  aus  dem  gleich bed.  garj)  durch Kreuzung  mit  Schallworten  mit  germ.  k-  im  Anlaut  umgebildet  sein   wird.
Mit  6^Ä-Erweiterung  vielleicht  hierher  (s.  oben  gall.  bardus)  arm.  kardam ,erhebe  die  Stimme',  lit.  gefdas  ,Geschrei,  Botschaft',  is-girstl  ,zu  höre
```


### [2026-09-06T14:53:01.352Z] TOOL RESULT

```
=== AHD gwera ===
1208:ABAFT apo- ABANDON bha-2 ABASE bassus ABASH bat- ABASIA gWa- ABATE battuere ABBREVIATE mregh-u- ABDICATE deik- ABDUCENS deuk- ABDUCT deuk- ABELE albho- ABERRATION ers-1 ABET bheid- ABEYANCE bat- ABHOR ghers- ABIDE bheidh- ABJECT yé- ABJURE yewes- ABLATION  tele- ABLAUT apo-, kleu-1 ABLE ghabh- ABLUTION leu(@)- ABNEGATE ne ABNORMAL gné- ABODE bheidh- ABOLISH al-3 ABORT er-! ABOUND wed-1 ABOUT ud- ABOVE upo ABRADE réd- ABRIDGE mregh-u- ABROGATE reg-1 ABROSIA gWere-4 ABRUPT reup- ABSCESS ked- ABSCISE kae-id- ABSCOND dhé-1 ABSENT eS- ABSOLUTE leu-1 ABSOLVE feu-1 ABSORB srebh- ABSTAIN ten- ABSTRACT tragh- ABSTRUSE treud- ABSURD swer-2 ABULIA gWele-1 ABUT bhau- ABYSS gWadh- ACANTHO- ak- ACANTHOPTERYGIAN pet- ACANTHUS ak- ACAPNIA kwép- ACCEDE ked- ACCELERATE kel-3 ACCENT kan- ACCEPT kap- ACCESS ked- ACCIDENT kad- ACCIPITER Oku- ACCLAIM kele-2 ACCLIVITY klel- ACCOLADE kwel-1 ACCOMMODATE med- ACCOMPLISH pele-1 ACCORD kerd-1 accosT kost- ACCOUNT peu- ACCRUE_ ker-3 ACCUMBENT keu-2 ACCUMULATE keue-2 ACCURATE cira ACERATE ak- ACERB ak- ACETABULUM ak- ACETIC ak- ACETUM = ak- ACHALASIA ghé-
1218:AEDILE aidh- AEGIS aig- AENEOUS ayes- AEOLIPILE pulé AEPYORNIS OrF- AERIAL wer-2 AERO- wer-2 AEROBE gWei- AERODYNE deu-2 AERONAUT nau-2 AESIR ansu- AESTHETIC au-5 AESTIVAL aidh- AETHER aidh- AFFABLE bha-2 AFFAIR dhé-1 AFFECT! dhé-1 AFFECT? dhé-1 AFFECTION dhé-1 AFFERENT bher-1 AFFIANCE bheidh- AFFIANT bheidh- AFFIDAVIT bheldh- AFFILIATE dhé(i)- AFFIRM dher-2 AFFIX dhigy- AFFLATUS bhié-2 AFFLICT bhiig- AFFLUENT bhleu- AFFORD pert AFFOREST dhwer- AFFRAY  pri- AFFRICATE bhréi- AFFUSION gheu- AFTER apo- AFTERMATH mé-4 AGAIN gagina AGAINST gagina AGALACTIA melg- AGAPANTHUS andh- AGE aiw- AGENDUM ag- AGENT ag- AGERATUM gere-1 AGGLOMERATE gel-1 AGGLUTINATE gel-1 AGGRAVATE gWere-2 AGGREGATE ger-? AGGRESS ghredh- AGGRIEVE gWere-2 AGHAST gheis- AGILE ag-
1219:AGIO al-1 AGITATE ag- AGLET ak- AGMINATE ag- AGNAIL angh- AGNATE gene- AGNI egni- _ AGNOMEN no-men- AGNOSIA gnd- AGO ghé- -AGOGUE ag- AGONY ag- AGORA! ger-1 AGORAPHOBIA ger-! AGRAFFE ger-2 AGRAPHA gerbh- AGRAPHIA gerbh- AGRARIAN agro- AGREE gWere-3 AGRESTAL agro- AGRIA agro- AGRICULTURE agfo- AGRIOECOLOGY agro- AGRIOLOGY agro- AGROSTOLOGY agro- AHIMSA ghei-i, ne AHRIMAN men-1
1278:BAPTIZE gWébh-1 BAR? gWere-2 BARB! bhardha BARBARIAN baba- BARBARISM baba- BARBAROUS_ baba- BARBEL bhardha BARBELLATE bhardha BARBER bhardha BARBETTE bhardha BARBICEL bhardha BARBULE bhardha BARD! gWera-3 BARE! bhoso- BARGAIN bhergh-? BARITE gWera-2 BARITONE gWera-2 BARIUM gWera-2 BARK! bherg- BARLEY bhares- BARM_ Dbhreu-2 BARMY bhreu-2 BARN bhares- BARO- gWera-2 BAROUCHE dwo-, ret- BARROW! bher-1 BARROW? bhergh-2 BARROW’ = bher-2 BARYON gWere-2 BARYSPHERE gWere-2 BARYTA gWere-2 BASCULE (s)keu- BASE! gWa- BASE? bassus BASIS gWa- BAS-RELIEF bassus Bass! bhar- Bass? bassus BASSET! bassus BASSO bassus BAT? bhiag- BATE? battuere BATEAU bheid- BATH! bhé- BATHE bhé- BATHOS gWadh- BATHY- gWadh- BATHYSCAPH skep- BATTEN! bhad- BATTERY battuere BATTER! battuere BATTER’ battuere BATTLE battuere BAWD bhel-2 BAWL bhel-4 Bay? bat-
1309:BITE bheid- BITTER bheid- BITTERN! beu-2 BITUMEN gWet-1 BIVOUAC ambhi, weg-2 BLACK bhel-1 BLACKMAIL méd- BLADDER bhié-2 BLADE bhel-3 BLAIN bhlei- BLAME bha-2 BLANCH bhel-1 BLANCMANGE bhel-1 BLAND mel-1 BLANDISH mel-1 BLANK bhel-1 BLANKET bhel-1 BLARE bhié-1 BLASPHEME bha-2 BLASPHEMOUS bha-2 BLAST bhlé-2 -BLAST melst- BLASTEMA melst- BLASTO- melst- BLASTULA melst- BLATHER bhlé-2 BLAZE! bhel-1 BLEACH bhel-1 BLEAK! bhel-1 BLEAK? bhel-1 BLEAT bhlé-1 BLEMISH bhel-1 BLENCH! bhel-1 BLEND bhel-1 BLENDE bhel-1 BLENNY mel-1 BLESBOK bhel-1, bhugo- BLIND bhel-1 BLINDFOLD bhel-1 BLINI mele- BLINTZ mele- BLISTER bhlei- BLITE mele- BLITZKRIEG bhel-1, gwere-2 BLOAT bhieu- BLOND bhel-1 BLOOM! bhel-3 BLOOM? bhel-3 BLOSSOM bhel-3 BLOW! bhié-2 BLOW3 bhel-3 BLUE bhel-1 BLUNDERBUSS (s)tene- BLUSH bhel-1 BOARD bherdh- BOAST! beu-1 BOAT bheid- BOATSWAIN bheid- BOCACCIO beu-1 BODE! bheudh- BODEGA dhé-1 BODHISATTVA bheudh-, es- BoER bheue-
1314:BOOM? bheue- BOON! pbha-2 BOON2 deu-2 BOOR bheue- BOOT? bhad- BOOTH bheue- BORDELLO bherdh- BORDER bherdh- BORE! bher-2 BORE’ bher-1 Boreas gWero-1 BOROUGH bhergh-2 BORROW bhergh-1 BORSCHT bhar- BOSCAGE busk- BOSOM beu-1 BOTH ambh6o BOTHRIUM bhedh- BO TREE bheudh- BOTTOM bhudh- BOTTOMRY bhudh- BOTULIN gWet-3 BOTULINUM gWet-3 BOTULISM gWet-3 BOUCLE beu-1 BOUGH bhaghu- BOUILLABAISSE beu-! BOUILLON beu-1 BOULDER bhel-2 BOULE! gWele-1 BOULE? beu-! BOULEVARD bhel-2, werg-
1324:BRIO gWere-2 BRIOCHE bhreg- BRISANCE bhréi- BRISTLE bhar- BRITTLE bhreu-1 BRONCHIECTASIS  ten- BRONCHO- gWere-4 BRONCHUS gWere-4 BRONTOSAUR bhrem-! BROOD bhreu-2 BROOK? bhriig- BROOM bhrem-2 BROTH bhreu-2 BROTHEL bhreu-' BROTHER bhrater- BROW bhri- BROWN bher-3 BROWSE bhreus-1 BRUIN bher-3 BRUISE bhreus-2 BRUMAL mregh-u- BRUNET bher-3 BRUT gWere-2 BRUTE gWere-2 BUBO beu-! BUCCAL beu-1 BUCEPHALUS gWou- BUCK! bhugo- BUCKAROO wak- BUCKBOARD beu-! BUCKLE! beu-! BUCKLE? beu-1 BUCKSHEE bhag-' BUCKWHEAT bhago- BUCOLIC gou-, kWel-1 BuppHA bheudh- BUDGET bhelgh- BUDGE! beu-1 BUGLE! gWou- BUGLOss gldgh- BUILD bheue- BULGE bhelgh- BULIMIA gWou-, leia- BULK! bhel-2 BULL! bhel-2 BULL? beu-1 BULLA beu-1 BULLATE beu-1 BULLET beu-! BULLETIN beu-1 BULLION beu-1 BULLY? beu-1 BULWARK bhel-2, werg- BUNCO bheg- BUND! bhendh- BUND? bhendh- BUNDESRAT ar- BUNDLE bhendh- BUNG peuk- BUNGLE bheg- BUPRESTID gWou- BUR! bhar- BURDEN! bher-1 BURG bhergh-2 BURGESS bhergh-2 BURGHER bhergh-2 BURGLAR bhergh-2 BURGOMASTER bhergh-2 BURIAL bhergh-! BURIN bher-2 BURN! gWher- BURN? bhreu-2 BURNET bher-3 BURNISH bher-3 BURSA bursa BURSAR bursa BURSE bursa BURST bhres- BURY bhergh-1 BUSHEL? bhau- BUSK! busk- BUSK? s(w)e-
1342:CENTROBARIC gWere-2 CENTUM dekm CENTURY dekm CEPHALIC ghebh-el- CEPHALO- ghebh-el- -CEPHALOUS ghebh-el- CERAMIC ker-4 CERASTES ker-! CERATODUS dent-, ker-1 CERATOID ker-! CEREAL ker-3 CEREBELLUM ker-1 CEREBRUM ker-1 CERES ker-3 CERTAIN krei- CERVINE ker-1 CERVIX ker-1 CESSION ked- CESSPOOL spirare cEsTus! kent- CEsTUS? kae-id- CHAETA ghait- CHAETOGNATH genu-2, ghait- CHAFE dhé-1, kele-1 CHAFER gep(h)- CHAFF! gep(h)- CHAIR sed-1 CHALAZA gheled- CHALAZION gheled- CHALCID ghelegh- CHALCOCITE ghelegh- CHALCOPYRITE ghelegh- CHALCOsIS ghelegh- CHALICE kal-1 CHALLENGE kel-8 CHALONE ghé- CHAMAEPHYTE dhghem- CHAMBER kamer- CHAMELEON dhghem- CHAMFER bhreg- CHAMFRON kaput CHAMOMILE dhghem-, mélon CHANCE kad- CHANCEL carcer CHANCELLOR carcer CHANCRE kar-1 CHANGE skamb- CHANT kan-
1392:CONFOUND gheu- CONFRERE bhrater- CONFUSE gheu- CONFUTE bhau- CONGE mei-1 CONGEAL gel-3 CONGENER gene- CONGENIAL gene- CONGENITAL gene- CONGERIES gerere CONGEST gerere CONGLOBATE gel-1 CONGLOMERATE gel-1 CONGLUTINATE gel-1 CONGRATULATE gWera-3 CONGREGATE ger-! CONGRESS ghredh- CONGRUENT ghréu- CONIDIUM keni- CONIOSIS keni- CONJECTURE yé- CONJOIN yeug- CONJUGAL yeug- CONJUGATE yeug- CONJUNCT yeug- CONJURE yewes- CONNATE gene- CONNECT ned- CONNIVE kneig’h- CONNOISSEUR gn6- CONNOTE gné- CONNUBIAL sneubh- CONQUER quaerere CONQUIAN kom, kWo- CONSCIENCE skei- CONSCIOUS | skei- CONSCRIPT skribh- CONSECRATE sak- CONSENT sent- CONSEQUENT sekw-1 CONSERVE ser-1 CONSIDER sweid-1 CONSIGN sekw-1 CONSIST sta- CONSOCIATE sekw-1 CONSOLE! sel-2 CONSOLIDATE sol- CONSOLUTE leu-1 CONSONANT swen- CONSORT ser-3 CONSPICUOUS _ spek- CONSPIRE spirare CONSTABLE ei-1 CONSTANT sta- CONSTELLATION  ster-3 CONSTERNATE  ster-2 CONSTIPATE  steip- CONSTITUTE sta- CONSTRAIN | streig- CONSTRUCT  ster-2 CONSUETUDE s(w)e- CONSUME em- CONTACT tag- CONTAIN ten- CONTAMINATE tag- CONTEMPLATE tem- CONTEND ten- CONTEST trei- CONTEXT teks- CONTINUE ten- CONTORT terkw- CONTOUR tera-1 CONTRA- kom CONTRABAND bha-2 CONTRACT tragh- CONTRADICT deik- CONTRARY kom CONTRAST sta- CONTRAVENE gWa- CONTRITE tere-1 CONTRIVE trep-2 CONTROL ret- CONTROVERSY wer-3 CONTUSE (s)teu- CONVALESCE wal- CONVECTION wegh- CONVENE gWa- CONVENIENT gWa- CONVENT gWa- CONVENTICLE gWa- CONVENTION gWa- CONVERGE wer-3 CONVERSE! wer-3 CONVERT wer-3 CONVEX wegh- CONVEY wegh- CONVINCE weik-5 CONVIVIAL gWei- CONVOKE wekw-
1399:CRANIUM ker-1 CRANK! ger-2 CRASH? ker-4 CRATE kert- CRATER kere- CRAW gWere-4 CRAWL! gerbh- CRAYFISH gerbh- CREATE ker-3 CREATINE kreue-1 CRECHE ger-2 CREDENCE kerd-1 CREDIBLE kerd-1 CREDIT kerd-1 CREDO kerd-1 CREDULOUS_ kerd-1 CREEK ger-2 CREEP ger-2 CREMATE ker-4 CREODONT kreue-1 CREOLE ker-3 CREOSOTE kreue-1, teus- CREPE sker-3 CREPITATE ker-2 CRESCENDO ker-3 CRESCENT ker-3 CRESS gras- CREST sker-3 CREVICE ker-2 CREW! ker-3 CRIB ger-2 CRIBRIFORM krei- CRICKET! ker-2 CRICOID  sker-3 CRIME krel- CRIMP! ger-2 CRIMSON k*rmi- CRINGE ger- CRINGLE ger-2 CRINITE sker-3 CRINKLE ger-2 CRINOLINE fino-, sker-3 CRIOSPHINX ker-1 CRIPPLE ger-2 CRISIS krei- CRISP sker-3 CRISPATE sker-3 CRISSUM sker-3 CRISTA sker-3 CRISTATE sker-3 CRITERION krei- CRITIC krei- CROCHET ger-2 CROCIDOLITE krek-1 CROCK! ger-2 GROCK® ger-? CROCKET ger-2 CROFT ger-2 CROMLECH léu-1, skerbh- CRONE sker-1 CROOK ger-2
1424:DEVANAGARI deiw- DEVASTATE eu-2 DEVEST wes-4 DEvi deiw- DEVIATE wegh- DEVIL gWele-! DEVIOUS wegh- DEVISE weidh- DEVOID eu-2 DEVOIR ghabh- DEVOLVE wel-3 DEVOTE weg¥h- DEVOUR gWera-4 DEVOUT weg*h- DEW dheu-2 DEXTER deks- DEXTERITY deks- DEXTRO- deks- DEXTRORSE_ wer-3 DHARMA dher-2 DI-!_ dwo- DIABASE gWa- DIABETES gWa- DIABOLIC gWela-1 DIACRITICAL krel- DIADEM dé- DIAGNOSIS gnd- DIAGONAL genu-! DIAGRAM gerbh- DIAL deiw- DIALECT leg-1 DIALOGUE leg-1 DIALYsIs_leu-1 DIAMETER mé-2 DIAMOND deme-2 Diana deiw- DIANTHUS andh- DIAPASON pant- DIAPAUSE paus- DIAPEDESIS ped-1 DIAPHANOUS bha-1 DIAPHORESIS bher-1 DIAPHRAGM bhrekw- DIAPHYsIS bheue- DIARRHEA sreu- DIARTHROSIS ar- DIARY deiw- Diaspora sper-4 DIASTASIS sta- DIASTOLE stel- DIASTROPHISM_streb(h)- DIATESSARON kWetwer- DIATHESIS dhé-1 DIATOM tem- DIATRIBE tere-1 DIAZO = gWei- DICAST deik- DICENTRA kent- DICHASIUM dwo- DICHO- dwo- DICHOTOMY tem- DICKER dekm DICLINOUS  klei- DICROTISM kret-2 DICTATE deik- DICTION deik- DICTUM deik- DIDACTIC dens-! DIDAPPER dub- DIDYMIUM dwo- DIDYMOUS dwo- DIE! dheu-3 DIE? dé-
1565:GOAD ghei-1 GOAT ghaido- GOD gheu(e)- GODSEND sent- GOFFER webh- GOLD ghel-2 GOLIARD gWel-3 GOMPHOSIS gembh- -GON genu-! GONAD gene- GONFALON gWhen-1 GONIOMETER genu-1 GONIOMETRY genu-! GONION genu-! GONO- gena- coop ghedh- GOOSE! ghans- GORE! ghaiso- GORE? ghaiso- GORGE gWere-4 GORGET gWera-4 GORSE ghers- GOSHAWK ghans- GOSLING ghans- GOSPEL spel-3 GOSSIP s(w)e- GOUACHE akWa- GOWAN ghel-2 GRAB! ghrebh-1 GRABEN ghrebh-2 GRACE gWera-3 GRACKLE gera-2 GRADE ghredh- GRAFFITO gerbh- GRAIN gre-no- GRAM! § gerbh- GRAM? gre-no- -GRAM gerbh- GRAMA gras- GRAMINEOUS_ gras- GRAMMAR gerbh- GRAMPUS_peisk- GRANADILLA gfe-no- GRANARY gre-no- GRANDILOQUENCE tolkw- GRANGE gre-no- GRANITE gr@-no- GRANT kerd-1 GRANULE gre-no- GRAPE ger-2 GRAPH gerbh- -GRAPH gerbh- -GRAPHER gerbh- GRAPHIC gerbh- GRAPHITE gerbh- -GRAPHY gerbh- GRAPNEL ger-2 GRAPPA ger-2 GRAPPLE ger-2 GRASP ghrebh-1 GRAss_ ghré- GRATE! grat- GRATE? kert- GRATEFUL gWere-3 GRATIFY gWere-3 GRATIS gWera-3 GRATITUDE gWero-3 GRATUITY gWera-3 GRAUPEL kreup- GRAVE! ghrebh-2 GRAVE? gwWera-2 GRAVES ghrebh-2 GRAVEL ghréu- GRAVID gWera-2 GRAVURE ghrebh-2 GRAY gher-3 GRAYWACKE wegh-
1567:GREAT ghréu- GREAVES ghrebh-2 GREEDY gher-5 GREEN ghré- GREET gher-2 GREGARIOUS ger-1 GRENADE gre-no- GRESSORIAL ghredh- GREYHOUND gher-3 GRID kert- GRIDDLE kert- GRIDIRON kert- GRIEF gWera-2 GRIEVE gWere-2 GRIM ghrem- GRIMACE ghrem- GRIME ghréi- GRIND ghrendh- Grip! ghreib- GRIPE ghreib- GRIPPE ghreib- GRISAILLE gher-3 GRISEOUS gher-3 GRISETTE gher-3 GRISLY ghréi- GRISON gher-3 GRisT ghrendh- GRIT ghréu- GRIZZLE gher-3 GROAT ghréu- GROATS ghréu- GROCER gWres- GROOVE ghrebh-2 GROPE ghreib- GROSCHEN gWres- GROSS gWres- GROSSULARITE ger-2 GROSZ gWres-
1572:GUN gWhen-1 GURGITATION gWere-4 GURU gWera-2 GUSH gheu- Gust! gheu- GusT2 geus- GUSTO geus-
1591:HELL kel-2 HELLEBORE el-2, gWere-4 HELM! kelp-
1658:HUM kem-3 HUMAN dhghem- HUMANE dhghem- HUMBLE dhghem- HUMECTANT wegw- HUMERUS omeso- HUMID wegw- HUMILIATE dhghem- HUMILITY dhghem- HUMOR wegw- HUMUS dhghem- HUNDRED dekm HUNGER kenk-2 HUNKER keu-2 HURDLE kert- HUSBAND bheue- HUSSAR kers-2 HUSTINGS tenk-1 HUT (s)keu- HYATHODE sed-2 HYDATHODE wed-1 HYDATID wed-1 Hypra_ wed-! HYDRANT wed-! HYDRANTH andh- HYDRAULIC aulo- HYDRO- wed-1 HYDROCEPHALUS ghebh-el- HYDROMEL melit- HYDROUS wed-1 Hyprus_ wed-! HYENA sil- HYGEIA gWei- HYGIENE gWej- HYGRO- wegw- HYLOZOISM _hulé HYMEN  syil- HYMNODY wed-2 HYOSCINE si- HYPER- uper HYPERBOLA gWele-1 HYPERBOLE gWelg-1 HYPERBOREAN gWere-1 HYPERKINESIA kei-3 HYPERPNEA pneu- HYPHA webh- HYPNAGOGIC ag- HYPNO- swep-! Hypnos swep-! HYPNOSIS swep-1 HYPNOTIC swep-1 HYPO- upo HYPOCHONDRIA ghrendh- HYPOCORISM ker-3 HYPOGEAL gé HYPOPHYSIS bheue- HYPOPNEA pneu- HYPOSTASIS sta- HYPOSTYLE sta- HYPOTAXIS tag- HYPOTENUSE ten- HYPOTHERMIA gWher- HYPOTHESIS dhé-1 HYPROCRISY krei- HYPSO- upo HYSTERESIS ud- HYSTERIC udero- HYSTERO- udero- HYSTERON PROTERON per!, ud-
1678:INERTIA ar- INEXORABLE 6r- INFAMOUS bha-2 INFANT bha-2 INFANTRY bha-2 INFARCT bhrekw- INFECT dhé-1 INFELICITY dhé&(i)- INFER_ bher-1 INFERIOR ndher- INFERNAL ndher- INFERNO ndher- INFEST dhers- INFEUDATION peku- INFIDEL bheidh- INFIRM dher-2 INFIRMARY dher-2 INFIX dhigw- INFLAME bhel-1 INFLATE bhié-2 INFLICT  bhiig- INFLUENCE bhieu- INFLUENZA bhleu- INFRA- ndher- INFRACT bhreg- INFRANGIBLE bhreg- INFRINGE bhreg- INFUSE gheu- INGENIOUS gene- INGENUOUS gene- INGEST gerere INGRATE gWere-3 INGRATIATE gWere-3 INGRESsS ghredh- INGUINAL engW- INGURGITATE gWere-4 INHABIT ghabh- INHERE ghais- INHERIT ghé- INHIBIT ghabh- INHUME dhghem- INIMICAL amma INITIAL ej-1 INITIATE ei-1 INJECT yé- INJUNCTION yeug- INJURY yewes- INK kéu-
1691:Is es- ISALLOBAR gWere-2 ISCHEMIA segh- ISINGLASS bhié-2 ISLAND akwa- ISOBAR gWere-2 ISOCLINE klei- ISOGLOss glogh- ISOHEL sawel- ISOHYET seue-2 ISOMER (S)mer-2 ISOMETRIC mé-2 ISOPIESTIC sed-1 ISOPLETH pele-1 ISOSCELES skel-3 IsosTasy sta- ISSUE ei-1
2149:QUELL gWel-1 QUENELLE gen- QUERCETIN perkWu- QUERCITRON perk"u- QUERIST quaerere QUERN gWera-2 QUERULOUS kwes- QUERY quaerere QUEST quaerere QUESTION quaerere QUIBBLE kWo- QUICHE kak-2
2177:REFRAIN? bhreg- REFRIGERATE Srig- REFRINGENT bhreg- REFUGE bheug-! REFULGENT bhel-1 REFUND! gheu- REFUSE! gheu- REFUSE? gheu- REFUTE bhau- REGAL reg-! REGENT reg-1 REGICIDE reg-1 REGIME reg-? REGIMENT reg-1 REGION reg-! REGISTER gerere REGIUS reg-! REGLET reg-1 REGOLITH reg-3 REGRATE grat- REGRESS ghredh- REGULAR reg-! REGULATE reg-1 REGULUS reg-! REGURGITATE gWere-4 REIFY ré-
2225:SCHISM skei- SCHIST skei- SCHIZO-  skei- SCHIZONT es- SCHLEP |leij- SCHLIEREN sleu- SCHLOCK | slak- SCHMALTZ mel-1 SCHMEER (s)mer-3 SCHMUCK meug-2 SCHNAUZER snu- SCHNITZEL sneit- SCHNORRER sner- SCHNOZZLE snu- SCHOLAR segh- SCHOLASTIC segh- SCHOLIUM segh- SCHOOL! segh- SCHOOL? §skel-1 SCHUss skeud- SCIENCE skei- SCILICET skei- SCINTILLA skeei- SCINTILLATE skeei- SCIOLISM skei- SCION géi-1 SCIRE FACIAS dhé-1, skei- SCISSION  skei- SCISSORS kae-id- SCLERA skele- SCLERO- skele- SCLEROMA §skela- SCLEROSIS skela- SCLEROTIC skelo- SCLEROTIUM skela- SCLEROTIZATION skela- SCLEROUS skelo- SCOFF skeubh- SCOLD sekw-3 SCOLEX skel-3 SCOLIOSIS skel-3 SCONCE? dhé-1 SCONE keu-! SCOOP skep- Scop skeubh- -SCOPE spek- -SCOPY spek- SCORCH skerbh- SCORE sker-1 SCORIA_ sker-4 scoT skeud- SCOT AND LOT skeud- SCOTOMA  skot- SCOUR! cira SCOUR2 kéwero- SCOURGE reig-1 SCOUT! ous- scouT? skeud- SCRABBLE  sker-! SCRAG gWere-4 SCRAP!  sker-1 SCRAPE sker-1 SCRATCH grat- SCREAK ker-2 SCREAM ker-2 SCREECH ker-2 SCREED skreu- SCREEN sker-1 SCREW sker-! SCRIBBLE skribh- SCRIBE skribh- SCRIMP_ skerbh- SCRIPT skribh- SCRIPTORIUM skribh- ScRIPTURE  skribh- SCROBICULATE sker-1 SCROD skreu- SCROFULA  sker-1 SCROLL skreu- SCROTUM skreu- SCRUB!  sker-1 SCRUTINY skreu- SCUDO skei- SCUFF skeubh- SCUFFLE! skeubh- SCUFFLE? skeubh- SCULPTURE skel-1 SCUM (s)keu- SCUTCH kwét- SCUTTLE! skeud- SCUTUM  skei- SCYPHISTOMA skep-, ste-men- SCYPHOZOAN skep- SCYTHE sek- SEAL! sekw-1 SEAL? selk- SEAM syi- SEANCE sed-! SEAR! saus-
2267:SITZKRIEG gWere-2, sed-1
2373:THEO- dhés- THEOBROMINE gWere-4 THEODICY deik- THEOPHANY bha-1 THERAVADA sta-, wed-2 THERE to-
2457:VOILE weg-! VOIR DIRE wéro- VOLANT gWel-2 VOLATILE gWel-2 VOLE! welt- VOLE? gWel-2 VOLITANT gWel-2 VOLITION wel-2 VOLKSLIED léu-2 VOLLEY gWel-2 VOLT? wel-3 VOLUBLE wel-3 VOLUME wel-3 VOLUNTARY wel-2 VOLUPTUARY wel-2 VOLUPTUOUS wel-2 VOLUTE wel-3 VOLUTIN wel-3 VOLVA wel-3 VOLVOx wel-3 VOMER wogWh-ni- VOMIT weme- VORACIOUS gWere-4 VORLACE legh-, per! -VOROUS gWere-4 VORTEX wer-3 VOTARY wegh- VOTE wegWh-
```


## [2026-09-06T14:53:06.688Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -E \"g[Ww]er[eoa@]-3|gWera-3\" AHD_watkins1985.txt | grep -v \"^1[23456789]\" | head -20; echo \"=== context ===\"; grep -n \"To favor\" AHD_watkins1985.txt | head"
}
```


### [2026-09-06T14:53:06.750Z] TOOL RESULT

```
=== context ===
```


## [2026-09-06T14:53:07.577Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"grātus\\|gratus\\|bardus\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-06T14:53:07.653Z] TOOL RESULT

```
362:DECENT. 2. Suffixed (causative) o-grade form *dok-eye- in: a. Latin docére, to teach (< “to cause to accept”): DOCENT, DOCILE, DOCTOR, DOCTRINE, DOCUMENT; b. Greek dokein, to appear, seem, think (< “to cause to accept or be accepted”): DOGMA, (DOGMATIC); DOCETISM, DOXOLOGY, HETERODOX, ORTHODOX, PARADOX. 3. Suf- fixed form *dek-es- in: a. Latin decus, grace, ornament: (DECOR), DECORATE; b. Latin decor, seemliness, elegance, beauty: DECOROUS. 4. Suffixed form *dek-no- in Latin dignus, worthy, deserving, fitting: DAINTY, DEIGN, DIG- NITY; CONDIGN, DIGNIFY, DISDAIN, INDIGN, INDIGNANT, INDIGNATION. 5. Reduplicated form *di-dk-ske- in Latin discere, to learn: DISCIPLE, (DISCIPLINE). 6. Greek dekh- esthai, to accept: PANDECT, SYNECDOCHE. 7. Greek dok- os, beam, support: DIPLODOCUS. [Pok. 1. dek- 189.] dek-2. Referring to such things as a fringe, lock of hair, horsetail. 1. Suffixed o-grade form *dok-lo- in Germanic *taglaz in Old English teg(e)l, tail: TAIL!. 2. Perhaps Germanic *tag- in: a. Swedish tagg, prickle, akin to the Scandinavian source of Middle English tagge, pendent piece: TAG!; b. Middle High German zacke, nail (> German Zacken, point): SHAKO; Cc. Old French tache, fastening, nail: TACHE, TACK!. [Pok. 2. dek- 191.] dekm. Ten. I. Basic form *dekm. 1. Germanic *tehun in: a. Old English tien, ten: TEN; b. Old Norse an, ten (see oktd(u)). 2. Latin decem, ten: DECEMBER, DECEMVIR, DECI-, DECIMAL, DECIMATE, DECUPLE, DICKER, DIME; (DECENARY), DECENNIUM, DECUSSATE, DOZEN, DUODECI- MAL, OCTODECIMO, SEXTODECIMO. 3. Irregular Latin distributive dani, by tens, ten each (formed by analogy with néni, nine each): (DENARIUS), DENARY, (DENIER?). 4. Greek deka, ten: DEAN, DECA-, DECADE, (DECANAL), (DOYEN); DECAGON, DODECAGON. II. Extended form *“dekmt- in Germanic *-tig in Old English -tg, ten (see dwo-). III. Ordinal number *dekmto- in Germanic *te- guntha- in Old English teogotha, téotha, tenth: TENTH, (TITHE). IV. Suffixed zero-grade form *-dkm-ta, reduced to -kmtd, and lengthened o-grade form *-dk6m-ta, re- duced to *-kontd. 1. Latin -gintd, ten times: NONAGE- NARIAN, OCTOGENARIAN, SEPTUAGINT, SEXAGENARY. 2. Greek *-konta, ten times: PENTECOST. V. Suffixed zero-grade form *dkm-tom, hundred, reduced to kmtom. 1. Germanic *hundam, hundred, in Old English hundred, hundred (-red, from Germanic *radam, number; see ar-): HUNDRED. 2. Germanic *thiis-hundi, “swollen hundred,” thousand (see teue-). 3. Latin centum, hundred: CENT, CENTAL, CENTAVO, (CENTENARIAN), CENTENARY, CEN- TESIMAL, CENTI-, CENTIME, (CENTNER), CENTUM, CEN- TURY; CENTENNIAL, PER CENT, QUATROCENTO, SEICENTO, (SEN!), (SEN2), (SENITI), SEXCENTENARY, TRE- CENTO. 4. Greek hekaton, a hundred (? dissimilated from *hem-katon, one hundred; see sem-'): HECATOMB, HECTO-. 5. Avestan satam, hundred: SATEM. See also compound root wikmti. [Pok. dekm 191.] deks-. Right (opposite left); hence, with an eastward orientation, south. Suffixed form *deks(i)-tero- in Latin dexter, right, on the right side: DESTRIER, DEXTER, DEXTERITY, DEXTRO-; AMBIDEXTROUS. Compare ner-'. [In Pok. 1. dek- 189.] del-'. Long. Probably extended and suffixed zero-grade form *dlon-gho-. 1.Germanic *langaz, long, in: a. Old English lang, long, long (comparative lengra): LINGER, LoNG!; b. Old High German lang (> German Jang), long: LANGLAUF; C. Old English denominative langian, to grow longer, yearn for: LONG?; d. Latin compound Lon- gobardus, Langobardus (with Germanic ethnic name *Bardi): LOMBARD. 2. Germanic abstract noun */lang- ithé in: a. Old English lengthu, length: LENGTH; b. West Germanic */angitinaz, lengthening of day, in Old English lengten, lencten, spring, Lent: Lent; ¢. Dutch lenghe, linghe, “long one,” akin to the Low German source of Middle English lenge, ling, ling: LING}. 3. Latin longus (> French long), long: LONGERON, LONGITUDE; ELOIGN, ELONGATE, LONGEVITY, LUNGE, OBLONG, PROLONG, PUR-
```


## [2026-09-06T14:53:11.953Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -o -E \".{300}CONGRATULATE.{300}\" AHD_watkins1985.txt | head -5"
}
```


### [2026-09-06T14:53:13.237Z] TOOL RESULT

```
542:ffixed full-grade form *gvero-nd-, millstone, in Old English cweorn, quern: QUERN. [Pok. 2. g¥er- 476.] gvere-*. To praise (aloud). 1. Suffixed zero-grade form *gvra-to- in Latin grdtus, pleasing, beloved, agreeable, favorable, thankful: GRACE, GRATEFUL, GRATIFY, GRATIS, GRATITUDE, GRATUITY; AGREE, CONGRATULATE, IN- GRATE, INGRATIATE. 2. Suffixed zero-grade form *gwro-do-, “he who praises,” in Celtic bardo-, bard, in Welsh bardd and Scottish and Irish Gaelic bard, bard: BARD}. [Pok. 4. gver(a)- 478.] gvere-4. To swallow. 1. Possibly suffixed extended form *gro-gh- in Germanic *krag-, throat, in: a. Old En
```


## [2026-09-06T14:53:17.923Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"gar-\\b\" BRT.txt | head -40"
}
```


### [2026-09-06T14:53:17.970Z] TOOL RESULT

```
10221:Zum  V.  'gar-i').  —  ai.  ^-  f.'),  —  PQ.  (lu  Y.  V)i girihi,  (zu  A):  ^iv/m4iB(Transskr,). —  ■)  Nicht völlig  sicher.  Vgl.  SAderbloh  La  vie  future 98.  —  >)  NA.  schreibt  ohne  erkennbaren Gmnd  bald  gatS  um',  bald  garS.nm'  (s.  *).
```


## [2026-09-06T14:53:18.878Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"demāna\\|dəmāna\\|dmāna\\|garō\" BRT.txt | head -40"
}
```


### [2026-09-06T14:53:18.945Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T14:53:21.810Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '10190,10260p' BRT.txt"
}
```


### [2026-09-06T14:53:21.909Z] TOOL RESULT

```
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
5"
294 ;  »gl-  auch  mp,  vigräyihük.  —  •)  Unsicher; das  Aind.  Hesse  vielmehr  Jäyar.  erwarten; doch  s.  das  Perfekt.  —  Si  %  151;  i.  auch  gr. hpVfP",  Bthl.  WklPh.  /iJp/.  661.  iBild. vgl.  femer  lat,  frägro  ans  "ghräghtiiö;  Bcu. Grdr.a  /.  602,  IF.  6.  100.  —  4)  Hds.r  främi mngi  rayöii  yiq  ratul  fritdis  (so  T)  äsat;  S. aber  Pu.  and  Bthl.  IF.  j.  371.  —  J)  Etymo- logisch lu  ^gar:  HaUQ  lieit  vTräj/isHii.  — 6)  S.  ta  frajrälay-  und  /rayrärayö.  Was  ist HauCs  fräl  ^P   läyünik  (Essays'  369,  371)?
•  j.  'gar-  V.  'preisen',  nur  mit  Praev. Praes.  11  g^nn-,  a6  gairya-  (Pass.)  — Int  °gairyä.
mit  aibi  1)  'preisen':  atsa  aibiggrante (3SPM.)    Y.  70.  I  (?)  ■>.  2)    'billigen,
lobend  einstimmen  in  — '  (Akk.):  s.  Inf.
mit  avi  'preisen'(?):  avi  ratüs  aii rahwya  ginnle  (3SPM.)  Vr.  4-  t(?)  ''■
mit  ä  'preisen':  iaAe'^  ng  ila  ni>ma ayairyüp''  kaAe''>  V5  urva  frayezyst  "von wem  wird  nun  unser  Name  gepriesen, von  wem  von  euch  unsere  Seele  verehrt werden?"  Yty.  50,
ai.  gi^^lii  abhigirya  (Absol.)*).  —  VgL  fjnr-, aibijarilay-,  ägrimalay:  —  PQ.  (lu  V.  /O):  ö öi  apar  girem,  (lU  Vr.  4):  elön  pa  an  raOk  u fISn  fa  an  ralih  radimh ;  vgl.  zu  aibijat/lay- mit  No.  2.  —  1)  Anscheinend  verderbt.  — '}  Der  Gen.  des  Agens  beim  Passiv  ist  auf- fällig; doch  vgl.  DbK.  AiS,  396,  —  3)  Pass. mit  akt.  Endung,  S  J2J,  —  4»  Das  ooss.  zarin 'singen'  iveist  weist  auf  7  als  idg.  Anlaut  hin; %55-
•  j.  3gar-  V.  'schlucken'.  Praes.  ^jara-'^. *}arSil  *haom3m  .  .  bisanmta    *iristi-
rftncai^A.)  P.25.
ai.  niroli,  gilali  'voial',  PDw.  nei-jaram  'voro'. -  Vgl-  V-"^  Adj.  —  Pü. :  j^artan.  —  ')  So nach  dem  Ai.  —  •)  Hds.  jaraöii  haan^m,  aber Pü,;  i"«!-  hörn.
•  j.  ^gar-  V.,  nur  mit  «r  'niederschleu- dem'.     Praes.  zi  grä-.
'nieder,  herabschleudern  auf-'  (Lok.):
karitaät  . .  vmraät  aSsqm  . .  ysi  niymire (3PPM,)  iarahu  mafyskanqm  Vt.  (O.  40.
Vgl.  gr.päM.«,  «^ijro;  %  14;.  's.  noch  NeISSEK ÜB,  13.   »91.
•  gl  j-  ^gar-  f.  'Lob,  Preis;  Loblied'; stBlö  'rü  {AP.)  vahmSng  ahursi  mazdai.. dadfmakÜa  .  .  \.4i.  i.  A)  GS.  garif mit  g.  dimäna-,  j.  nmäua-  n.  'Haus  des Lobs' "  als  Bezeichnung  für  den  Aufenthalt Masdah^  und  der  Seligen,  sva.  Paradies*'; a)  im  gAw,:  at  hsi  vahmStig  d?mSn!  °rö »idümii  "lasst  uns  ihm  Preislieder  im  Haus des  Lobs  niederlegen"  Y.  ^5. 8;  —  a  ^i^l
dby  Google
S'3  *gar-  Ab
{sd.)..'rd  thmSmY.$0.^\  —  Ayal  mlzihm zard^usirO  magavadj/U {sA-)  Üsisl  para  "rd d»mSnS  ahurS  masds  jasat  (sd.)  Y,  5/. 15.  b>  im  jAw.  (immer  in  der  Folge ^  nm°):  xsnäts  asaonqtn  urvanö  p3rayeiiiti . .  avi  'rS  nmäiDin  mal^amm  ahurake. mazdS  ..  amgsanam  spfntanqm  ..  anyalsam asaonam  V.ip.32; — 'rS  nmäitpm  ahurahe mazdä  yazamaide  Vr.  7.  i;  —  °rJ  nmämm asti  "nfrfyö  asävaoyd  Ytj.  4^4;  —  *°rB iimUne  ahurahe  hvSyaomm  Yt.^j,  3;  — zaoirä  .  .  ni  hJs  dasva  *'rS  nmäne  Yt, 10.^2;  —  urvätam  , ,  m»rtkw3fä3m  kuma- taglu  .  .  häxtagsu  ,  .  hvarstaiht  .  .  *°r5 nmansm  Ylij.  84;  —  ahurahe  mazdS.  g" fumän^i  yat  srlr?m  VyLJ'^^;  —  °r!f  sp3n- tahe  n>mäne  Vyt  28.  a)  sonst  mit raoxma-  Adj.:  raoxliam  "rS  ntnSrum  S. 2.30;  —  haca  raoxiha  *°rB  ttmäna  .  . .rr/ata  haca  duianha  Yt. /().  44;  —  mt- "ir^m  ..yim  yasata  ahurB  mazdä  raexsnät paiii  *'r5  nmänät  Yt  iQ.  IJ3;  *I33;  — raoxmahe  *°r5  nmänahe  S./.30,  Yt.72.37,
•)  Sra.  vahiilä  aahus  und  aJiajra  taoii;  vgl. iB.  V.  /p.  3a  und  Y.  lg.  6.  Vielleicht  wurde aber  das  G.  auch  als  besonderer,  d.  i.  besonders heiliger  Raam  innerhalb  des  Paradieses  be- tracbtel.
Zum  V.  'gar-i').  —  ai.  ^-  f.'),  —  PQ.  (lu  Y.  V)i girihi,  (zu  A):  ^iv/m4iB(Transskr,). —  ■)  Nicht völlig  sicher.  Vgl.  SAderbloh  La  vie  future 98.  —  >)  NA.  schreibt  ohne  erkennbaren Gmnd  bald  gatS  um',  bald  garS.nm'  (s.  *).
•  j.*gar-  i)  Adj. 'schluckend,  verschlingend' (nur  Komp.).  2)  f.,  Plur.  ■>  'Kehle,  Hals'  '> : aictl  ai3in  (näml. o^/)  tanUn  aguze  aiairi maisahe  -rö  Yt.  J7.  56.
KompE.  —  Zum  V.  igar-.  —  ai.  'gir-  Adj. ;  vgl. ai.  gala-  m.,  np.  giilü  'Kehle'.  —  •)  Auch -ariman-  (sd.)  ist  Flur,  lant  —  =)  Gans  un- wahrscheinlich Gdn.  3Yt.   lao.
•  j.  garay-  :  gairi-  m.  'Berg,  Gebirgszug, Gebirg"':  -rayi^^^.)  b^nzantB  Ytio.  14; ig.z,  7,  8,  16.  3;  —  'rayd  (als  AP.)"  aSa- ^ä^rä  Y.2.14;  /0.3,  7/.  10;  —  'rayasca (als  AP.)  ySi  hrnaniö  Yty.  9;  —  ma- sits  Urli{AP.)  Yt.j4.4ii  —  bar^dstaiibyö 'triiyS  V.  2.  aa;  —  'irl/c3'^  aßtaHnS  Y. 42.3; —  iarfshus  paiti  'irinam  Y.5.  26, JO.3,  V.2.23i>;  Y.j.14^, /o.  17.  YLÄ24, 14-  21.  iS.  6,  ig.  6,  Vr.  /.  6,  V.5.  I',  2, 10.28;  —  haoma  raose  'ra  (LS.)  paiti Y./0.4;  —  ytzi  ahi  'rS  (LS.)*'  dtr^hm (sd.)  \.2i.  5;  —  paoiryB  °iris  hqm.hiiial .  .  haraiii  bars  . ,  bitys  ztrihazB  HrU  Yt.
BAITHOLOHAa,  AlÜHD.  Wb.
garad-  mit  aiwi
514
ig.  i;  6',  66;  —  'rsU  ^uHjIar^nahe  Y.i. 14,  22.36;  Ny.5.  5,6,  FrW.5.  i;  —  airyB.- xs'uiai  haca  'rsit  :^anvant»m  avi  HrXm Yt5.6;  i.zZ,  5.4s,  &33,  Y.2.14,  Ny./. 8,  V.  22. 19,  S.  2. 9';  —  *aoi  spitagaona (sd.)  Hri  (AP.)  4>  Y.  jo.  1 1 .  [FrBy. :  lies gairi  ifrpzB.]
•)  Die  Gesammtiahl  der  Berge  wird  Vt  lg.  7 'auf  2244  angegeben;  vgl.  die  Aufiahlung  Yt. /g.  1  ff.,  woiu  Bd.  M.  1  ff. KompA.  —  ai.  giräy-  in.;  mp.  gar,  glrft),  afy, yar.  -  Pü.!  gar;  s.  noch  No.  2,  4,  —  ')  Mit der  Var.  gairyS,  %  406.  —  ')  Pii.i  Idna  ^ gil  'I^hm'l  Statt  ^(>6).  Sü.:  giri^.  —  3)  Mit der  gut  bezeugten  Var.  ^lurcanqiB  6) ;  s.  'varay- No.  I.  ~  4)  iSt.  yg\.  Gdn.  sYt.  120.  Pü.: garölmän.  —  5)  Gebildet  wie  dahnaiiiyü,  htnda, S  1^7.  S.  aber  lu  sßia.gama-  No.  —  *)  S. lu  '%raotah-  No.    l.
•  j.  garav  (:  °yrav-)  Adj.  1)  'schwer, schwerflüssig'.  2)  fem.  i°yrs-)  'gravida, schwanger'.
KompA.  (s.  goutu''),  E.  —  ai.  guräv-  ['grav-) Adj,;  np.  vgl.  girän.
•  g.  garah-  n.  "Lob-,  Preislied';  pairi- gal'iw  (sd.)  xsmUvatö  vahms  mazda  °rSbll stBiqm  Y.34.2.
Zum  V.  'gar:  —  Pß,  j  vatän  andar  gardtmän släyim.
•  g.  gaire  Inf.  'zu  wachen  über-'  (Akk.); yS  *urvqtiim  min  g°  . .  dadl  aslscä  vldus (sd.)  . .  yavat  isät  (sd.)  .  .  avai  xsäi  aesl asahyä  "der  ich  des  eingedenk  bin  über die  Seele'*  zu  wachen  .  .  und  .  .  sie  .  , lehren  will,  das  A.  zu  suchen"  Y.  2S.  4.
Zum  V.  ^gar-,  —  Pü.;  ki  ruvän  andar  garöl- män dahci,  —  ■)  Des  Menschen,  die  dem Propheten  anvertraut  ist.
•  j.  *gairi.b9r9z-'>  f. 'Bergeshöhe,  -tiefe"': ''snu.b^Kö  n3rf.b3r3zS  °zd  mänö(sA.)  FrBy.
Npü. !  iüh  biilä.  —  ')  Hds.  i;arayö  t'.  —  'I  Oder Adj.
•  j.  gairi.masab-  Adj.'*  'von  der  Grösse eines  Bergs';  °s!J  aahB  (sd,,  Sp.  iio  m.) aetahe  V.5.9  PüZ.
1)  Oder  auch  ntr.
•  j.  gairi-äak-  Adj.  (auch  fem.)  'was  mit den  Bergen  zusammen,  in  ihnen  heimisch ist':  aurunaca  (sd.)  "iJÄJ  (NPm.)  siidraca ravascaraid  Yt.  Ä36;  —  paotris  3pB  .  . '/äcB  (NPf.)  Yt./p.66.
Komp.;  gataf-  +  'Aai:
•  j.  garad-  V.  'gradi',  nur  mit  Praev. Praes.  i  g>r>d-.
mit  aiiui  'ingredi,  anheben,  beginnen':
aiwi.g3rihmahi      yasnahe       haptatihätäis
dby  Google
515  gar»d-  mit  avi  —  garäta-  516
AumataSa   hastaca  hvar^aca;    aiwi^trü-  bleiben  oder  sich  im  Hals  festsetzen"  V,
mahi  ahm  vohü  Vr.iy.i;  —  aiwi^ßnl-'  i^.^.
mahi  apqm  .  .  fräitlmca  .  .  Y,  Ö2.  n.         1     Vgl.  <'gat-  f.  —  Pü. :  galäk  (=  np.  gulü\
mit  avi  dn.:    avi  apqm^a  «m/r«- 1      ■  ^„^y.  ^  -Hitze' :  vJ  >i<y/.7  äp«ä
namca  . .  yasn,mg,f^r,n,aht  vaAm?mca  ,  .   ,,an%aüyw>m  frak»rmtatar,rSmainyus\. "7.  ■  ■  r^T         vi"-'-  V  P-      '"'''>^T»f^a  'maum  (AS.)' V.  m8.
Ut  vgl.  gradier.   —     VeL  gjnzday-.    —    Pü.!,       ,,  ,  d-  -i
•  j.   gaMWa-   m.    l)   'Mutterleib,   Uterus':  I         i-  Sanmü.vataahim  A.  J,  ?;  lies  a^arim-,
j.«   (näml.  aridvt,    mpunqm   hlmSimm' ,  ■    „„„s.starana-   m.   ein   bei    der Mää,  ••<™,.>^...v4,M,«  Y.65.=;-Arp^i„»        gebrauchtes    Gerät:    ymiäMi
(oaml,  arpdvi)  arsnqm  xsudm  m  xlaä^rt- 1  ,  ,  .       °  /  Fp  \  y  »4  7
nqm    *'wqn  ■>   (näml.  yaeidalaiÜ)    Y.  65.  |  >,i,ara„a-  n„  vll.  lü  lit.   'skilti  -Feuer  anschlü-
5.  2)  'Leibesfrucht,  _/W«j'':  ma  . .  iaiiie]  gen'O.  -  IMi,:  oddamk  (Jamaspji  Gloss.547;
mafySnam  pard  fsanmat  {sA.)  :^atU  °W3m^  ".^j/.imi;  Utensils  med  in  the/äi' »j^*-^/(highet
ra?sayät\.  15.11;    ij.   "  "r?'"l'"i    of    'he    Zoroastrian     rdigion^)
..i-^Ma-  m.  I)  -Uterus,  i) 'fetus  ;  mp-  (P";)  (^o !,/„/«/  5,™r^«rf.   -    ■)  Np.  >mr  'Kohk'
```


## [2026-09-06T14:53:46.394Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 223 224 225 226; do echo \"=== HRN leaf $n (printed p.$((n-21))) ===\"; awk -v n=$((n+1)) 'BEGIN{RS=\"\\f\"} NR==n' HRN.txt; done"
}
```


### [2026-09-06T14:53:49.469Z] TOOL RESULT

```
=== HRN leaf 223 (printed p.202) ===
— 202 -
värdon, vgl. Hübschmann, S. 86); andere Bei-
spiele dieses der Umgangssprache entnommenen Laut-
wandels sind enderän (No. 119), heran (No. 252),
dehün (unter No. 589).
905. ffurde *Niere\
aw. (Du.) vereöka- (vd. 18, 70), veretka- *beide Nieren
(ZPGl.) ; phlv. gurtak ; ai.-präkr. (Du.) vfkkd- *Nieren'.
kurd. gurdale (H. -Seh.), gu7*cik{y)\ bei. guttiy;
wa/. velk.
Hübschmann, KZ. 25, 109.
906. ffuri^j gurze 'Keule', arab. LW. jurz,
aw. vazra- 'Keule ; phlv. vazr, arm. LW. varz; ai.
vdjra- ^Donnerkeil (Indra's)'.
wa;^. LW. gilrz,
906^** ger^män (falsch kerzman) Himmel'.
V
aw. garö demmia-^ garö nmäna- (S alemann, SF,
pag. 99»; dann auch Fr. Müller, WZKM. 5, 187, der
arm. LW. gerezman 'Grab' Gruft, Friedhof dazu stellt).
907. {\)gtir8 'Hunger, gursene, gursenegt; gtcsne, n22/}^
(Js. 8, 4), ^r:i'^i: (Js. 5, 13).
g. vasne, vasnegi; Kä§. ves, vesd, vesS, vesegl.
phlv. gursak (AV.), gursakth (Men.), gursUan (vd.
9 (132) GL); kurd. vürsl, vürsigt, vdsa (H.-Sch.).
LW. bei. gusnag, n. gumag (120); siyn. gusna.
Wegen g. vasne etc. muss der Anlaut ursprüng-
lich ein V gewesen sein, also ist bei. gusnag entlehnt.
908. {2)gur8 Xockenhaar (unbelegt).
aw. varesa- 'Haar; phlv. vars, arm. LW. vars;
ksl. vlasu,
909. yiriften 'ergreifen*, Praes. glr-etn,
g. gereftmün,
ap. [/^grab-, agarbayam ergreifen'; aw. [/^grab-,
gerewnäiti; phlv. graftan; ai. l^grabh^, gfbhndti,
kurd. girtin 'ergreifen ; bei. girag , n. giray (106);
sar. vayreiy-am,
910. gurg 'Wolf.
Käs. var, varg, mrg\ mäz. vurg.
=== HRN leaf 224 (printed p.203) ===
— 203 —
ap. Varkäna-; aw. cehrka- 'Wolf; phlv. gurg; ai.
vfka- Wolf; arm. gaU (H. No. 62).
kurd. varg *Wolf'; afy. lüg] oss. d. beräyj t. biräy
(60, unsicher) ; bei. gvark, gurk, n. giirß (140) ; yidg.
yter;', yaj'n. aurak,
911. germ Varm*, gerniä 'Wärme', germJ, germis (AM. 54
Zeile 13; 182 Zeile 9).
ap. garma- in Garmalpada-; aw. garema- warm';
phlv. garm^ garmäk, garmth; ai. gharmd- 'Wärmen-
arm. J^rm 'warm', Jermn 'Fieber , jernum *sich erwärmen,
warm werden, erglühen' etc. (H. No. 243).
kurd. bei. (100) garm, bei. garmag (LW. ? 101); afy.
yarma\ oss. d. yarm^ t. yarm (90); siyn. gfarw, sar.
iÄrm, gürm,
912. girevtden glauben* jT^in; (Qiss. Dan., Merx' Archiv,
I, 416, 4).
ap. aw. l/'var- glauben ; phlv. varav(i)stan, mirav{i)sn
(Mün., AV.), päz. garöldan, garöisn, garavisn (AV.).
oss. t. urnjn (262) 'glauben*.
913. gire 'Hals , girebän 'Halsberge' (arab. LW. jirbän,
Jurrubän).
aw. grTva- 'Nacken (des Berges)'; phlv. (aram.) \l^))i
'Hals, Nacken' (Nöldeke, ZDMG. 46, 144), grJvak
'Bergnacken', grtvpän 'Halsberge*; ai. grlvd^ 'Hinter-
hals, Nacken .
afy. griva, greva 'Hals; Halsband'.
914. gureyten 'fliehen , Praes. gurBz-em,
Kauk.-bergjüd. viri/de (!).
skr. vi + i/^reö' (s. No. 638), allerdings nur in der
Bedeutung leer machen , laxiren vorkommend ; doch
vergl. aw. ra^cayeMti (paiti) 'sie verlassen , ai. i^rec-
'räumen, preisgeben', oss. d. lejun , t. iTjin 'laufen,
fliehen' (167); phlv. v(i)rextan.
Eine ältere Bedeutung von np. gure/ten findet sich
wohl bei AM. 237 Zeile 6: 'Also ist das Bedürfniss
nach Wasser grösser als das nach anderen Dingen,
da weder ein Gesunder noch ein Kranker es ent-
=== HRN leaf 225 (printed p.204) ===
— 204 —
b ehren kann (ee ö biigrEzeö)\ Wenn man hier von
'fliehen* ausgehen wollte, so würde die Erklärung sehr
gezwungen sein.
915. giristen, giristen *klagen, weinen', Impt. girl ^) girye,
giryjden (Sahn. I, 107 Vers 837).
aw. [/^gar-, gerente 'anrufen*; phlv. grlstan 'weinen,
klagen (AV.), g(i)rt/TnUan (AV.) ; ai. [/^gar-, gpidti 'an-
rufen'.
kurd. girin weinen ; oss. d. yär, t. qär 'Geschrei,
Ton, Laut, Stimme* (88); bei. greag, n. girey 'lärmen,
schreien, heulen, weinen*, Impt. bigri (117)^).
916. fße^endj guzend (AM. S. 38 Zeile 7) 'Schade Leid',
bezendT 'Elend'.
aw. "^mjainti-, vergl. ai. vi -i- iXAa«-, vihanti- ; phlv.
agajand bezw. agazand (AV.).
917. gu^ärden 'auseinander setzen, darlegen, bezahlen ;
gtizäris, güzärisn (Wörterbücher)^), guzäre; vergl. vecer
(vejer) 'richterliche Entscheidung (unbelegt).
skr. vi + [/"car-, Caus. 'erwägen, in Betracht ziehen,
prüfen ; phlv. v(i)cartan (AV.), v(i)car(i)sn^)j v(i)cartar
'verständig (für aw. cazdönkvaM-, arm. LW. vcar 'Be-
zahlung*.
918. guziden 'aussuchen, erwählen*, Praes. giizm-em, guzin
'erwählt'.
aw. vi H- [/^öay- 'aussuchen* ; phlv. v{i)öUany v{i)cwet
(AV.), arm. LW. vöit 'rein, lauter*; skr. vi-^ i^cay-
'auslesen, aussuchen'.
bei. gicinag, n. gisainay auswählen, aussuchen* (104).
*) Im Reim bei Eth6, Morgenländische Forschungen, S. 59,
Zeile 5 v. u. (Dies Citat verdanke ich Herrn Prof. Nöldeke).
2) Hübsohmann, ZDMG. 44, 557.
3) Vu 11 er 8 8. V. menisn hat falsch gttSärisn; beide Stämme
sind nicht zu verwechseln, doch werden sie in den Wörterbüchern
immer zusammen geworfen.
*) Phlv. *v%närisn^ vltiärfan* ist wohl auch r{i)c" zu lesen (ein aw.
c ist eingedrungen, wie öfter); die Bezeichnung des i in der Praepo-
sition vi wäre sehr aufiPäUig.
=== HRN leaf 226 (printed p.205) ===
- 205 -
919. gu^lr 'Hilfsmitter, guz^rden (Sahn. I, 61 Vers 519),
ffuzer, guzerden; vergl. näguztr.
Etwa "^viöarija-, vergl. skr. vi -r- i^car- 'ausführen,
vollführen'.
Hat mit reztr (No. 1084) nichts zu tun.
920. gustäx *kühn, frech', busta/ (nicht belegt), vergl.
usta/ (ebenfalls unbelegt).
aw. *vistaka', vergl. stax^'a-, phlv. sta^mak (Darme-
steter. Et. ir. 62)0; P^lv. v{i)stax (Mgn.), arm. LW.
vstah unverzagt'.
921. gtisterden ausbreiten', guster, vergl. blster (No. 218).
ai. vi -f- [/'sfar- ausbreiten'; phlv. v{i)siarta)i aus-
breiten*.
922. guMMen 'zerbrechen, trennen', Praes. gmihem^ gml
kerden Verabschieden, entlassen' (Öähn. I, 74 Vers 236),
pin '^''Di: Verstössen (Jer. 3, 8), vergl. gusll (Vullers),
gtisilänlden (Öähn. I, 88 Vers 494).
phlv. v{i)sastan (Bund.), v{i)sastakih (PPGl.).
Darmesteter, Et. ir. I, 84 hat das Wort auf eine
\/^*Qard' zurückgeführt, die neben ai. gar^, gpidti *zer-
brechen' auf iranischem Boden existirt haben müsse.
Bartholomae (briefl. Mitteilung) denkt an eine Ver-
mischung der beiden synonymen Wurzeln sk^heid- (aw.
sa^d-, hisidyäf; ai. dhed-, chindtti; bei. sindag, n. sinday,
Hübschmann, ZDM6. 44, 559) und k\er- (ai. ^c/r-,
Cfnäti). Ifp. gusisten wäre ap. *visistanaig (aus *«^z-
sid'tanaiy), dagegen gtisilem ap. *visardann (aus sar-
mit dem d von sid-). Er verweist dazu auf die
Wochenschr. f. klass. Phil., 1892 Sp. 397.
Der Inf. guslxten ist ganz unklar.
923. gusäden offnen , sich öffnen ; Praes. gusay-em,
gusüden, gusäyis (Öähn. I, 169 Vers 734).
phlv. v{i)sätan oflfnen'.
Darmesteter, Et. ir. I, 59 Note 3 nimmt als
Grundbedeutung von np. gvsäden sich freuen , indem
') An *v%8taxf'(i' hatten schon Fr. Müller, Kuhn und Schleiclier's
Beiträge V, 139 und Spiegel, Kommentar T, 64 gedacht.
```


## [2026-09-06T14:54:02.059Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== CHEUNG grad ===\"; grep -n -i \"grad\\b\\|\\*grad\\|gRAD\" CHEUNG.txt | head -20; echo; echo \"=== CHEUNG gar 'praise' ===\"; grep -n -i \"gari\\?ya\\|to praise\\|gRaH\\|GAR\" CHEUNG.txt | head -30"
}
```


### [2026-09-06T14:54:02.119Z] TOOL RESULT

```
=== CHEUNG grad ===
391:(old) *r and all ablaut series consist of the pattern, full grade *aC, lengthened *aC 
444:in their full grade form (except in instances where there is no evidence for this 
458:Avestan and Old Persian, the (postulated) full grade root is given, except in 
2746:of *rto irin the zero grade with subsequent introduction of -i- in the full grade. 
2856:unexplained, too: full grade *-an- nor zero grade *-n- can possibly yield long *-a-. 
6567:(Kuiper 1934: 236), but *ffah would exhibit an unusual ablaut grade though, similar 
7847:in Pash. peyór). 0 NP azir (aZer) reflects „5! and is probably from (full grade) *a- 
7848:Jariä-, rather than from pass. (zero grade) *4-jria- (more likely outcome *ä-gria-), as 
8126:*MIDDLE PERSIAN: MMP gry-, BMP gl(y)dy- /griy-/ ‘to weep’ (< OP *grad-ya-) || 
8323:whereas *gauda- is the corresponding full grade nominal formation, on which see 
8442:differently: pres. aja- (with the zero grade root). 
11741:whereas the latter may go back to (zero grade) *apa-Hxsa-. Obviously, the two verbs 
12032:is based on the Gr. reflex (zero grade *Hiib^- or, more likely, redupl. *H;eHib’-), 
17437:apparent unique full grade vae ° needs an explanation. || Ad YAv. “amasta: different etymology 
18566:actually reflects the (IE) zero grade *nmH-. The IE cognate forms that are quoted 
20945:Pahlavi forms perhaps reflect the different outcomes of syncope of the zero grade 
21748:*SANSKRIT: ? sanaih “gradually, little by little’ (RV+) = EWAia П: 607 
21801:pleased’. Ó It is difficult to separate BSogd. sy- from the root *sand- (zero grade: 
21806:(due to the workings of the Rhythmic Law): zero grade Plr. *sadia- > *sóiá- 
22821:full grade -aé-. Perhaps, the Av. sna&Z- is a blend of a them. stem *sna&ja- and 

=== CHEUNG gar 'praise' ===
284:Finally, with regard to modern Iranian languages I had to limit myself to a 
291:l'ormuri de Baraki-Barak (Logar, Afghanistan)” (2003), and last, but not least, 
320:therefore be regarded, in the first place, as a starting point for future research. 
350:° Т only recently discovered that the root *gar” ‘to be/make warm’ has been preserved as verb in Oss. 
351:(engaryn) and several modern dialects spoken in Iran. Also the informal form NP sas ‘pee’ has a more 
373:the Iranian language group. With regard to the (non-)Indo-European etymology 
743:Bulgarian 
815:Hungarian 
882:dialect of Lasgard 
1558:‘shattered’, (?) Olrish -aid-begar ‘is dissolved’ 
1924:*barj ‘to praise, honour’ 
1938:*MIDDLE PERSIAN: BMP bwic- /burz-/ ‘to praise, honour, exalt’ 
1977:semantically difficult to reconcile with ‘to praise, honour’ are the Pth. and Pers. 
2253:*NWIR: NP boy ‘smell, scent’, NP bostan ‘garden’, Bal. bod ‘smell, perfume’, Zaz. 
2447:12b this (hapax) verbal form is possibly from *barj ‘to praise, honour’, which is 
3090:*SANSKRIT: ? cira- ‘strip, tatter, rag’ (TA+), cela- (n.) ‘clothes, garment’ (Gaut.+) 
3407:forms are unrelated to Oss. I. angaryn/enzerst, D. enzarun/enzarst (caus.) ‘to 
3408:kindle, light a fire’, cited by Abaev, Le: 158 f. They rather contain the root *gar’ ‘to 
4518:*CHORESMIAN: (+ *pari-) prdys- ‘to repair (wall)’, pröyzk ‘garden’ > Samadi: 152 
4519:*NWIR: (+ *pari-) NP palez ‘garden’ 
4524:*MISC: Widely borrowed: (+ *pari-) Gr. тор@®бе1сос ‘garden, paradise’ (< Olr.), 
4525:Arm. (LW) partéz ‘garden’ (< WIr.), Arab. (LW) faliz (< NP), etc. 
5991:*SANSKRIT: dräpi- (m.) ‘mantle, garment’ (RV, AV) = EWAia I: 758 
6527:&n£U ‘threat, boast’, Goth. spill, Engl. spell, Toch. AB pällä- (pres.) ‘to praise’, 
6654:*CHORESMIAN: ? fn- ‘to sing’ (< *to praise, please with a song’ ?), Bry’k “honoured, 
7578:*gern‘, see *gart), Khuns. gen-/gena, Semn. -gänä-, Sang. -goeneé ‘to become’, Mah. 
7625:104 *garl 
7652:*gar! ‘to rejoice’ 
7676:*gar? ‘to turn, wind’ 
7685:*gar4 ? 105
```


## [2026-09-06T14:54:04.608Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN payghare ===\"; grep -n -i \"pey.äre\\|peġ\\|pey/äre\\|bīġ\\|pai\\?ti.gar\\|paitigar\" HRN.txt | head -20; echo \"=== HUB ===\"; grep -n -i \"gar.demana\\|garzman\\|gerzman\\|giristen\\|grāmī\\|grämi\\|garämi\" HUB.txt | head -20"
}
```


### [2026-09-06T14:54:04.679Z] TOOL RESULT

```
=== HRN payghare ===
=== HUB ===
10453:garzman 92.
```


## [2026-09-06T14:54:09.969Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '8080,8160p' CHEUNG.txt"
}
```


### [2026-09-06T14:54:10.022Z] TOOL RESULT

```
*NWIR: Widely attested: NP gastan/gard-, Tt. (Esh.) gard/gahast, Anar. getäye/gert-, 
Meim. be-gardaj-/a-gerd-, Tr. gela(yaygel-, Varz. gartäye/gart- ‘to become, turn’, 
NP gardidan (< *uart- ?), (Tadj.) Selidan ‘to roll’ (LW, cf. Yghn. yil-), Abyan. va 
gelloyan, Gil. (Rsht.) va-gärd- ‘to re-turn’, Awrom. geläy/get-, Gur. (Kand.) git-/ 
-(g)il- ‘to go about, wander’, Fariz. -gälä-/-gäl-, Ham. gärdayän/gärd- ‘to turn’, bär- 
gardayän/bär-e-gärd-, Isfah. ve-gärtän/ve-gärt-, Natan. va gola ‘to re-turn’, Mah. 
gird- ‘to walk (around)’, Nn. girta-/girt- ‘to become, be; to go round’, Siv. gir(1)-/ 
girià (+ va) ‘to return’, NP gardänidan/gardän- (sec. caus.), Jow. bam-gerna/a-gern-, 
Meim. bem-garn-/a-gern- ‘to turn (a)round, change, alter, etc.’, Awrom. geinay/ 
geh- ‘to turn over; relate’, Abyan. gelloya/gell-, Abz. gelowa/gel-, Qohr. gelada/gel- 
‘to turn [tr.]’ Yzd. (Zor.) gisnudvun, gisnddvun ‘to turn’ 

*NEIR: Pash. yaxt-/yar- ‘to twist, spin, turn’, Yghn. yil-/yilta ‘to roll; to flow 
quietly’, Ishk. yurs- (inch.) ‘to turn’, Sariq. yirs-/yerd ‘to revolve, go round, cross a 
pass’ (LW ?), ? Sangl. yart-, yort-/yost ‘to walk about’ (< early NP ?), ? Wa. 
Ysırt-/Yort- ‘to gather; to roll; to heap’ 

*MISC: Orm. gal-/galök ‘to weave’ = gal-/galök, galaw-/galawok 

9 The Ir. root with no exact IE correspondences seems to be an enlarged root of 
*gar”. It has probably been influenced by *yart. 

*PIE — = LIV: - | Pok.: 385 

*REFERENCES: КРЕТ. 83b, 142a, 145a; EVP: 27 f.; IIFL I: 394b; КРЕП: 219; Christensen, Contributions: 
I: 60, 166, 256; IIFL II: 524, 395a; Abrahamian 1936: 108, 133; Lambton 1938: 41b f., 78b; Andreev — 
PeSéereva: 258a; MacKenzie 1966: 95; Yarshater 1969: 182; EVS: 37а, 60b; Lecoq 1974: 60; WIM III: 


108; Steblin-Kamenskij 1999: 191; Lecoq 2002: 122, 125, 127 (etc., passim); Vahman — Asatrian 2002: 
25; NEVP: 32; Kiefer 2003: 196 


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
```


## [2026-09-06T14:54:10.519Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '7620,7700p' CHEUNG.txt"
}
```


### [2026-09-06T14:54:10.562Z] TOOL RESULT

```
“bad, evil’ || (+ *a-) BSogd. ’’y’ynt- (caus.) ‘to defile’ 

(+ *à-) Pres.: IND. 3sg. ’’y’ynt (Dhu. 127(N), SCE 180(N)) 


104 *garl 


*NWIR: Kurd. ganin/gan- ‘to rot’, NP gand ‘stench’, NP gandah ‘fetid, stinking, 
rotten; filthy, dirty’, Bal. gandag ‘bad’, Kurd. gani ‘rotting; stinking’, (orig. ppp.) 
Siv. gäs(s) ‘bad’ 

*NEIR: Pash. yandol ‘to dislike’ (+ *pari-) Oss. D. feelgandun/faelgzst ‘to smear; 
paint’ (+ *ui-) Oss. D. igaendun/igest ‘to smell; defile, desacrate’, Oss. I. gast, D. 
iğæstæ ‘desacration by something contagious or poisonous; desacrated’ 

*MISC: ? Par. ges ‘bad, sinful’, Orm. yanj ‘bad’ (< Pash. or other Ir. language ?) 
*SANSKRIT: gandh ‘to smell’ (RV+) = EWAia I: 461 

© The Ir. root *gant- (and Skt. gandh-) can hardly be of IE origin. The IE 
correspondences, notably Gr. ö£vvog (m.) ‘blame, reproach’ and @@dvoc (m.) 
‘envy’, are not compelling. The strange dental "alternation" in the Skt. and Ir. roots 
points to borrowing. 

*PIE — = LIV: — | Pok.: 466 f. 


“IE COGNATES: — 
REFERENCES: Horn 1893: 208; EVP: 26; IIFL I: 254b, 396a; Abaev, Slovar’ I: 542; Nyberg П: 81; 
Abaev, Slovar’ II: 297 f.; DKS: 79a; WIM III: 313 f.; Cabolov 2001: 368 f. 


*gar! ‘to rejoice’ 

*KHOTANESE: (+ *fra-) hayár- ‘to rejoice, be happy’. Ф The reconstructions and 
inherent etymology cited in SGS, Le, are all unconvincing. = SGS: 148 
*CHORESMIAN: m/yry- ‘to rejoice’, m/yw’ry- (caus.) ‘to let rejoice? > Samadi: 80 
*NWIR: ? NP zar ‘wish’ (nonce ?) 

*SANSKRIT: har ‘to be glad, enjoy, like’ (RV+) = EWAia II: 804 

Ó On the basis of (hapax) OAv. zarom (Y 44.17) an IE root *g"er-, with palatal g"-, 
is usually reconstructed (e.g. LIV: 176), despite the fact that the meaning of OAv. 
zaram is uncertain, cf. Kellens — Pirart III: 182. On the other hand, the meaning of 
the Chor. forms, with initial y-, strongly favours a connection with Skt. har-. We 
should therefore reconstruct an IE *oler- with non-palatal velar (Skjaerve apud 
Samadi 1986: l.c.). To this root we may add Khot. hayár-. 

*PIE *g'er- ‘to like" = LIV: 176 | Pok.: 440 f. 

*IE COGNATES: Gr. ҳолро ‘I rejoice, enjoy’, Lat. horior ‘I cheer up’, OHG gerno, OE 
georne ‘eager, readily’, Engl. yearn, etc. 

*REFERENCES: Chantraine IV: 1241a f.; Werba 1997: 271 


*gar? ‘to turn, wind’ 

*SOGDIAN: (+ *uz-) SSogd. ’zy’rt’k ‘flourishing’ (cf. Sims-Williams 1983: 46) || (+ 
*ham-) BSogd. ’ny’rtk- ‘flourishing, fertile’ (BSTBL: 121) 

*CHORESMIAN: ? yyr- ‘to (re)turn’, yyr(y)- (caus.) “to (let it) turn; to wrap’ || (+ *ati-) 
? micyyr- ‘to turn intr.], be(come) curved’ = Samadi: 83 Ё; 85; 50 


*gar4 ? 105 


*NWIR: Kurd. (Kurm.) garin/gar-, (Sor.) garan/garé- ‘to wander, go (round), roam’, 
Zaz. geyrayis/geyr- ‘to go round; to seek’, Gur. (Kand.) gir ‘curve’. 0 The Kurdish 
forms are from pres. *g(a)rna- (cf. Chor. yyrnyk), not from *uart- as assumed by 
Cabolov, l.c., cf. *uarta- > Kurd. (Sor.) bard ‘stone’, v. *uart. 

*NEIR: Ishk. yars-, Sarig. yirs-/yerd ‘to revolve, go round, cross a pass’, Sariq. 
yeyron (caus.) ‘to let it turn, revolve’, Wa. yir-/yird ‘to turn (into) [intr.]’ 

% IE cognate forms of this apparently "unenlarged" Ir. root are uncertain. The 
nominal forms quoted by Pok. (l.c.) are set with problems. The enlarged variants are 
*gart and *gar£". 

*PIE — => LIV: - | Pok.: 385
```


## [2026-09-06T14:54:29.336Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD ===\"; grep -n -i \"grāmīg\\|gramig\\|garōdmān\\|garodman\\|grīstan\\|gristan\\|griy\\|wenābag\" PHD.txt PHD_mackenzie.txt | head -30; echo; echo \"=== NYB ===\"; grep -n -i \"grāmīk\\|gramik\\|garōtmān\\|garötmän\\|garodman\\|gr’myk\\|grīstan\" NYB_vol2_glossary.txt | head -20"
}
```


### [2026-09-06T14:54:29.400Z] TOOL RESULT

```
=== PHD ===
PHD.txt:382:*g5k4n [gwk’n'] details. Lc um ~ig [-yk'] detailed; precisely. (sassa tu) ģūmēz [gwmyc | N giméz] bull's urine (as ritual purifier). ģgūmēz- [gwmyc- | N giméz-] urinate. gön [gwa' | N gün] colour, complexion. ~ag [-k' | M geng, N güna] = gön ; sort, kind, form. gor [gwl | N ~] onager, wild ass. göspand [K YNA < А апу ? ; gwspnd | N ~] (small) cattle, sheep. ~-tihrag [-cyhlk'] holding the seed of cattle. ģūstān [gwst^n!] cattle-stall, cowshed. 1858 [gws | = M, N ~J ear. *GÓ68 [guš | N ~] cal. 14th day. tūšag [gwsk' | N ~a] corner. ģēošūsrūd [rwi^wslwt! = Av. gaošū.srūta-| acquired, learnt. 5051 [BSLYA < A bsr’; рой! | N ~] meat, flesh. ģūšwār [gwštw] | N ~] ear-ring. ģūw-, ~išn, v. ģuftan. gowag [swb k! | М gw'g, N goya] speaking, eloquent; speaker. *ģoūwizār [gwwc'[] explicit, in detail. göy [gwd | N ~] ball. göz [gwc | N ~] walnut. ~énag [gwzynk! | N gózina) a walnut sweetmeat. Gözihr [gwcyhl | Ar. jawzahr] astr. the Dragon. ~ dumb: the descending node of the moon. ~ sar: the ascending node of the moon. grab [22р | P grb] womb. grāmag [gľmk! | P gr’mg] possessions, wealth. grāmig [gľmyk! | M grmyg, N girāmī] treasured, dear. ~ih: affection, respect. 1$raw [giwb! | P grww] cane. *ģraw [glwb' | N giraw] pledge, security. ~ih, ~(a)g4n [glwk’n' | M grug*n, N giraugān] = *graw. grayidan, gray- [gl?d-yin' | P gry-, N gtráy-] lean, incline; intend, desire. ģriftan, gir- [OHDWN-tn' < A V?hd; glptn!, gyl- | M grypt, gyr-, N giriftan, ~] take, hold, restrain. «išnīģ : tangible. griftār [gipt?l | N gir~] held, taken; captive. ~Omand [-'wmnd) tangible. grih [glyh | N girth] knot. lgriw [CWLE < A swr-h; glyw'] neck, throat. ?0riw [CWLE, glyw' | M gryw] self, soul. sgriw [glyw! | P gryw, N girī(b)] a grain measure, modius, peck. griwag [glywk!' | N giriwa] hill, ridge. ģrīwbān [g/ywp?n! | N girībān] neck-guard, gorget. griyistan, griy- [BK YWN-stn'< A У bky; gld-stn! | M gryy-stn, N giristan, giry-] weep, cry.
PHD.txt:744:affection grāmīgīh.
PHD.txt:1453:cry (v.) xréstan; (weep) griyistan.
PHD.txt:3407:respect āzarm, àzarmigih, gramigih, tars, tarságáhih.
PHD.txt:4058:treasured gramig.
PHD.txt:4296:weep brām-, griyistan. weeping brāmag.
PHD.txt:5376:garānīh darhandarzbed yarranidan garan yarranisn gramigih gramig grāmag drāyīdan, grāyīdan drāz, grāb draxt griy- grih dargūh garasman 1 3uriw griwag grīwbān driyos driyöšīh darigbed dilér drëm griyistan
PHD_mackenzie.txt:2460:garasman [glsm)n l I M gr)sm)n] = garodman.
PHD_mackenzie.txt:2475:garodman [glwtm)n l = Av. garo d~manaM I M grdm)n] paradise.
PHD_mackenzie.txt:2585:I1riyistan,griy- [BKYWN-stn'< A ...; bk)'; gld-sln' I M gr)'J'-stn, N
PHD_mackenzie.txt:5900:acclivity abraz.                          affection gramigih.
PHD_mackenzie.txt:6321:cry (v.) xrostan; (weep) griyistan.        daytime rozgar.
PHD_mackenzie.txt:6324:cub wa~~ag.                                dear dosag, gramig.
PHD_mackenzie.txt:7239:paradise garodman, (garasmiin),        perceptive marag, rnarisnomand.
PHD_mackenzie.txt:7240:  wahist; (worthy) of"'" garodmanig,   perch nisem.
PHD_mackenzie.txt:7462:respect azarm, azarmigih, gramigih,       ripen pazzam-; cause to -- pazzaftan,
PHD_mackenzie.txt:7952: weep bram-, griyistan.                 wise      danag,        frazanag,    xradig,
PHD_mackenzie.txt:10476:darzig                      11)&      garodmanig          ,1)~~~
PHD_mackenzie.txt:10477:garzidan                   \\tv&      garodman                 \~tD~
PHD_mackenzie.txt:10526:                          ...u~    gramigih                '"U~
PHD_mackenzie.txt:10530:                                   gramig
PHD_mackenzie.txt:10536:galOg                \~~           griy-
PHD_mackenzie.txt:10562:                    -6~~           griyistan               \\~
PHD_mackenzie.txt:11249:griy.r                     - ,toN)        awistanI             ,,~\~lU
PHD_mackenzie.txt:11252:griyistanI            \\~''''''\          -iidan                  \,~-

=== NYB ===
1123:cigon [cygwn] adv. and conj. A. interrog. adv. how? 1. direct interrogation: nun ~ kunom ?] 272; asmān ~? 921; exclama- tory: how...! 614. — 2. indirect inter- rogation: äkäh hom ku ~ hän 571; vēnēt ki Bastvar kārēcār ~ nev kunēt saw how valiantly B. fought 2815-16; ~ 6, 6 ham pursem 57°, andar Garodman dätistän ~, api-m nē dit 527-3; ete. — B. rel. adv. so as: l. har 3 šap x"amn ~ dit Estät ... guft such as he had seen it 2%; 215, 48, 520, 4527, ete.; introducing quotations: ~ den göbet 387, ~... paitāk ku 4571-5, etc. passim; parenthetic, e.g. 7718, 818%; — with a demonstr. antecedent: hamgönak hast ~-am guft 1216-17; šmāh bat ētūn m to gobeh 2329; 4524-25, 782.4, etc. — 2. with- out a clause, used prepositionally: as, as (for instance), as it were, like: ~ agäh aköc martom 2678-27; ~~ martom kë šarm 43913; 12813; varcāvandān i ~ Yam u Frétón ... 45°; hàn 4 ~ én such a th. 438; namely 1078; — with a demonstr. antecedent: &ön ~ āluh-ē 9%; eton ~ to 1516; ét6n but ~ amahraspand-ē 38°”; — čton, or ógón, homänäk (a. v.) ~ 69%, ete.; mänäk(k)äi (g. v.) i õi ~ ke pus... bare (opt.) 418. — C. conj. 1. causal be- cause: ~~... hdn mazantom bit 613-4; 1081. 11812; almost as a rel. pron. with a sec- ondary causal sense (as in Lat. quippe qui): 6 xuähar i x*"e$, ~ zan 4 Artaxsér būt, nämak nipišt 822; 718%, 7916. 116%. 11819; — hac han ~ in view of the fact that, considering that 38. — 2. temporal as soon as: 6°. 15°. 44°, more emphatically ham-~ 1317. - 3. ~ ka as if 11214.17, 10120722 — 4. almost = that 8722. — MPrth cw'gwn; MPrs ewn (read ci'on < *ciwön <
```


## [2026-09-06T14:54:31.355Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== IEC leaf ~203 (p.376) ===\"; for n in 202 203 204; do echo \"--- leaf $n ---\"; awk -v n=$((n+1)) 'BEGIN{RS=\"\\f\"} NR==n' IEC.txt | grep -n -i \"grāt\\|grat\\|gʷer\\|gwer\\|gr̥\" | head -20; done"
}
```


### [2026-09-06T14:54:34.031Z] TOOL RESULT

```
=== IEC leaf ~203 (p.376) ===
--- leaf 202 ---
--- leaf 203 ---
--- leaf 204 ---
```


## [2026-09-06T14:54:49.583Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=200 && NR<=208 {print \"--- leaf \" NR-1 \" ---\"; print substr($0,1,500)}' IEC.txt"
}
```


### [2026-09-06T14:54:51.769Z] TOOL RESULT

```
--- leaf 199 ---
(?) grm (3) ‘hitch, snag’
ghrndhið ‘pave, found, ground’. See next. Latv. griZu, grīst; OE gryndan, id.; Li. grind- žiu, gristi ‘pave, floor; MHG gründen, id.
ghrndhos, å, is “floor, ground, bottom, pav- ing’. Cf. ghrendh-, ghrondh- & WP I, 657 Go. grundu-; OHG grunt; OE grund ‘ground’; grynd ‘plot of land’; grynde ‘abyss’; ON grund, f.i-st. ‘prairie’; Sw. grund, adj. and s. ‘shallow’;
beside Norw. ON grunn ‘shoal, shallow’; '
grunnr, adj. & s. ‘botto
--- leaf 200 ---
eam’. WP I, 657. Cf. ghrendk- and ghrndh- Gallo-Latin grunda ‘roof; sug-grunda ‘eaves’; Ir. cf. gronn-lus, s. ‘groundsel’, lit. ‘ground- herb’; MHG grant, gs grandes (1) “base”; Slo- vene (?) grod “four-handled carrier, bier’; Li. grañdas ‘floorboard’; grandà ‘plate, sheet’; Latv. grodi, mpl. ‘well-top, balustrade; but- tress; foundation’. (For G Grand, R grùda, Cz. hrouda, see guhrondh-)
ghrondhos, à (2) ‘container, bosom, paunch’. Cf. WP I, 657 Arm. 
--- leaf 201 ---
e’; Li. graužas, aī ‘gravel; shingle; sawdust’
(ghrou-, see ghrõið, ghrot-. This form only in Myc. korowe- 'coloured")
ghrubh- *bury, hide'. Cf. WP I, 477 & 654 Gk. krüpto ‘hide’; kruphós *hiding-place'; ON gryfja ‘pit; OHG cf. gruft (vault': Gk. krup- tós, adj.). Extn. of type *ghrubhi- in ON gruf- la (crawl: E grovel); OHG grubilon (“fumble?: G grübeln). Long-grade in ON grüva ‘cower’, á grüfu ‘prone’; Sw. gruva sig ‘burk, shy at
(ghrubhos, see ghroub-, and c
--- leaf 202 ---
�� & Latv. grumslas, fpi. ‘cracklings’ con- tain IE *g-)
ghrā, ghru- (ghəru-) (?) (For IE *1/r before a vowel cf. Lat. calare, Gk. kaléo, and Lat. varus: Li. viris; Gk. paro: E for, etc.). Skt. (Vedic) hirå ‘vein’; Lat. haru- spex ‘inspector of entrails’
345
ghrbh- ‘seize’ (?) Cf. gurbh-, and cf. WP I, 595 Vedic grbhnami; cf. Skt. grbhab ‘handle’; Per. inf. giriftan, beside girav ‘pledge’; Hitt. karp (mi) “take, lift, complete'. Ambig. cf. karp-. A parallel form
--- leaf 203 ---
obat *mound, hillock’; MHG gupf, e wm., guphe, f. “peak, top, tip'; G Gupf, id.; cf. MHG goffe, guffe, f. ‘buttocks’; Li. (ambig.) gubà ‘shock of shea- ves?
ghubho, ið (1) “bend, hollow?. Cf. ghoubh-, ghubhos (1) & (2) Oss. cf. gubín, gubun ‘stomach’; Lyc. gupo (or gubo), gupu ‘tomb’; Arm. cf. gub, gs gbo ‘pit’; Gk. küptoó, pf. kékupha ‘bend’; kûphos ‘bend; vessel, container’; cf. küphós ‘bent, hunch- backed’; OCS cf. sü-gübü “arm? beside sù-
34
--- leaf 204 ---
d’; Swed. gump ‘rump of birds’. For OCS gọba, Li. gumbas, see gumb-
ghumbho ‘bend, incline, lie down’. Cf. ghubh-, ghoubh- Arm. gmem ‘lie down’. Loss of *-bh- as in ca- mem ‘chew’, see ĝombh-); Li. gumbu, gùbti, intr. ‘bend’; Norw. Sw. (ambig.) cf. gubbe “old man’
ghundhos (ghundholos), à “lump, ball, tu- mour, pile; balled, lumped’. WP I, 588. Va- riant: ghund-. Skt. cf. hundih, m.f. Jump, heap’; Av. gundo ‘round loaf; ear of corn’; gunda ‘round loaf; 
--- leaf 205 ---
a (ómucus', fr. uos-, q.v. + ghurio); Cz. voz-her, m. ‘mucus, snot
ghus- (gheus-) “noise, sound”. Cf. WP I, 566 & 569 Skt. ghusah ‘resounding’; ghusyah "to be noised abroad); ghustah ‘sounded, noised" beside ghosah ‘noise’; ghosami ‘resound’; ON guss ‘fuss’; gussa, v. ‘resound’ beside gjósa, v. ‘erupt’
Gu
guabh- ‘swallow, engulf, immerse’. WP I, 674 Av. jaiwis ‘deep’; Gk. báptō ‘dip, dye, wash’; baphé ‘immersion’; cf. Hes. bákhtho húdatos �
--- leaf 206 ---
a- kati ‘cackle’; Blg. cf. gač ‘teal’; W cf. baich (2) ‘scream’, s., fr. *guaksis
guakos (or guaKos), ios “empty, vain’. Cf. guag- (2) Oss. (*-à-) qwag, Dig. gäwagä ‘lacking’; Gk. cf. bákëlos ‘eunuch’; Lat. (ambig.) vacuus, va- civus; (LW in) W gwag ‘empty’; Li. gašùs “fop- pist’ beside baslüs ‘lewd’, gašnùs (“dandified?. Cf. also Gk. bákēlos in this sense);
guaks- (?) (-å-) ‘small; tot? Arm. (ambig.) kaçi, gs kaçvo, abl. kaçeav ‘small c
--- leaf 207 ---
�barb, spike, needle". Cf. guilos & WP I, 691 Myc. qero-; Gk. bélos, gs -eos ‘dart, arrow’; be- Jong ‘needle’; cf. o-belós, Dor. o-delós ‘spit (fr. *oK- °); EME (?) quill Creed or "oul: (OCS and com. Sl. Zel-ézo “iron”, a cpd.: Li. geležis and Latv. dzelzs, id. seem to contain *ehel- ‘yellow’, etc. q. v.); Srb. cf. žaoka (*Zal- ka ‘spike, dart); Li. geluonis, f. “point, tip, knife-edge': Latv. dzelonis ‘sting’
guel- (2), guel- “pain, sorrow'. Figurative extn.
```


## [2026-09-06T14:54:59.670Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=216 && NR<=220 {print \"--- leaf \" NR-1 \" ---\"; print}' IEC.txt | head -120"
}
```


### [2026-09-06T14:55:01.303Z] TOOL RESULT

```
--- leaf 215 ---
küt, küte, s. & wm. (putty: G Kitt)
guóu-eda (-édis, -odà, -dā) ‘ox, cattle, beef, cattle-fodder'. Cf. ed- and guou-sth- Oss. qáwwaz, qwaz, Dig. $àwanz ‘hind, doe: Alb. gjedh “head of cattle"; ON kjot, ds kjotvi ‘flesh’; Sw. kött, Norw. kjótt, Dan. köd, id. (vocalism obscure); OCS govedo "oy: OCz. hovéda, hovedina, f. “beef” beside Cz. havéd ‘vermin’ :
guoueió ‘vow, declare’ Gk. cf. bou-lë (if for *guou-lēų ‘taking of re- solution’, cf. léu-) Lat. voveo; Li. gaviü, eti (‘fasť, lit. vow"); Latv. gaveju, et, id.
guóuolos (guəuəl-) “head of cattle; bull, ox, buffalo". WP II, 112 Skt. golah ‘bull’; Hind. gaur ‘wild bull, bison’; Oss. gal ‘ox; bull; Gk. boübalos ‘buffalo’; Lat. (LW fr. Gk) bübalus, id., beside It. (from Umbrian) bufolo, id.; MIr. büáaball, id.; W bual, id. (both fr. Lat. but cf. also Ir. bólach, bólacht, bualacht ‘livestock’, fr. *guouol-a$-
369
to-); Alb. (LW via Lat.) buell, buall “buffalo”; Blg. güla ‘herd’. Of similar vocalism cf. Gk. bólos ‘sod’; Ir. bualtach *cowdung'
(guðuər (coll. type) ‘cattle’. Cf. guouolos. Only in Ir. buar cattle")
guouil- Lat. bovile (cowshed'; Ir. buaile ‘milking pad- dock’
guóuinos, à ‘of oxen; ox; beef; cowdung’. Cf. guous and derivs. Skt. gavinih “herd of cows’; LLat. bovinus, adj.; It. bovino, adj. beside bovina 'cowdung'"; Lat. cf. also bübinaàre, v. ‘defile’; Br. bevin ‘beef; Cor. bowyn, (d: W buyn ‘bullock’; MHG Kkuegin, adj. (cow's'; OCS govíno ‘dung’ (and com. Sl.); Cz. cf. o-havny “disgusting”; Li. cf. guone ‘salamander’
guóuios ‘bovine’ Skt. gavyah; Av. gaoyo; Tokh. B kewye, ke- wiye; Gk. cpds.-boios
guüu-kolos, is, à ‘herdsman, herdswoman'. WP I, 442. Cf. kol- (1) Myc. qoukoro-; Gk. boukólos; Dor. bokólos; Mir büachaill, m. f.; W bugail; Cor. bügel; Br. bügel ‘herdsman; shepherd; child’; (Mod. Ir. also = “servant; bachelor”)
guðumn-, (guoun-, güðn-) Av. gaoma “flesh, meat; EME coom “black grease’. Cf. (*guon- in) G Kuhnen ‘grime’; R po-gànyj ‘filthy’ beside po-goni ‘filth’; Cz. han-ba ‘shame’; Ukr. hanli-ba, id.; and (*guoun- in) Gk. bounós ‘clot of blood"
guðus “head of cattle, ox, cow. WP I, 696. (Z-gde variant: gii-) Skt. gauh, pl. gāvah “head of cattle’; gávam ‘bull’; gavah ‘ox’; gavih ‘cow’; Av. gáus; Per. gàu, gàv; Oss, qug, gog ‘cow’; Arm. kov, u-st. ‘cow’; Tokh. ko, pl. kowi; B keu ‘cow’; Hitt. .. us ‘head of cattle’; Hiero-Hitt. wawas, id. (for *hwawas); Myc. qou-; Gk. boüs; Lat. bos, gp boum; Umb. bum, acc.; Olr. Ir. bó, pl. ba; W bu, buw; Cor. bow- cpds. ‘cow’; OBr. cf. bou-tig *'cow-house'; OHG kuo, pl. kuo, kuoi, gp kuo; OE cü, pl. cy; LG kau; Fris. kou, pl. kij; Du. koe; OCS cf. gu-mno 'cow-tread', i. e. *threshing-floor', and com. Sl. Cf. min-; Cz. hav-éd' ‘vermin’ beside hov-ézí ‘beef; Latv. govs, gs id., gp govju ‘cow’. Z-gde variants in-
guðuər — gurëið, gurëið
15
20
25
30
35
40
45
370
clude: Arm. ku ‘dung of deer": Vedic á-guh *cowless'; anu-guh 'droving'; Lat. bu- in bu- bulcus; It. (Umbrian) bi- in bi-folco ‘cow- herd); Slovene go-máz ‘reptile’
guðuså “mire, cowdung'. Cf. guoutos Fr. cf. bouse ‘mire’, boue *mud' (fr. a Celtic source); W baw ‘dung, filth’; Fris. kweaze ‘mire’. (Isophonic: MHG kuose ‘she-calf’)
guou-sthos, à, io (guouəst-, gust-) Skt. gosthah, -sthà *cowshed'; Per. güst ‘meat’; Rustic Lat. in It. busto “bust; Olr. buas “wealth in cattle’; OCS gusta ‘dross
guðutos, à, om, ios, io (guot-, güit-) (an asso- ciate of guüus, q. v.) | Skt. gota ‘cow’; güthab ‘dung’; Av. güo, Per. güh, id.; Arm. gu, o-st. (ambig.) ‘dung of wild animals’; Arc. bousós 
--- leaf 216 ---
'cattle-Crun' beside -pót&, -páte (in ois- “dung on sheep's rear); isophonic in Gk. boütes ‘herdsman’; bousé “female slave’ (used as cowgirl); Hes. bousía ‘a root resembling turnip’, MHG quot, quát, OE cwead, OFris. quad ‘dung’; adj. ‘bad’; LG (z-gde) küt ‘filth from entrails’; (Gmc. forms fr. *-dh- or *-tós, -tóm); Blg. cf. gutav ‘bad’; Li. gúotas “herd of small animals’; guotë, guo- Cià “orange-agaric”
guðutros, om (guutro-) (an association of COWS) Skt. gotrám 'cowshed'; LLat. cf. botrix *excre- ment’; W budr ‘filthy’
gur-, see gurus. A zero-gde element in Gk. br-iaros, br-ithüs, br-ómos; Lat. br-ütus; Latv. gr-üts
guràun, guràuon, guràán- ‘heavy stone, mill- stone'. WP I, 685. Cf. gurus Skt. gravan “heavy stone’; Per. garan, giran “heavy, dear; Arm. erkan ‘mill’; MIr. bráu, bró, gs. brón, id. beside Mir brón “burden, grief; W breuan ‘handmill’; Br. bréw ‘mill’. Cf. Lat. variant gravamen ‘grievance’
gurebhos, -es-, (gurebhmn, -ón) ‘foetus, in- fant, young animal’. WP I, 689 Gk. bréphos, n.; MHG krébe (?) ‘intestines’; OCS Zrébe beside Cz. hříbě *foal". (For Skt. gárbhah *womb, foetus, infant? see guolbh-)
gureio, gureio “be heavy’. Cf. gurus Skt. gure, mp. (lift beside güráyami, id.; Per. garayam ‘gravitate toward"; Arm. krem ‘bear,
371
carry’; Gk. baréo ‘weigh down’ beside Aeol. boréo, id.; Go. kaürjan, id.
guremó, gurem- ‘roar, rumble’. (Slav., Balt. and Alb. evidence ambig. Cf. guhrem-, and ghrem- (1) & (2). Cf. also WP II, 202 & 308) Av. gram-, v. ‘rage’; Gk. brémo; Ir. cf. breim, pl. breamanna, s. ‘rumbling of bowels’; W brefu “low, bleat’; R gremét ‘rumble, roar’; long-gde in Ukr. hrimaty, Cz. hfímat; also in Li. gremoju, oti *eat noisily', but cf. (? *guh- rém-) in Alb. gromé ‘belch’; Latv. grémens ‘heartburn’ beside Latv. gremot, v. ‘ruminate, chew over’. Variant in Latv. gremzt, v. (2) ‘toar’
gurost- (?) “heavy; weight, heavy substance. Cf. gurus Arm. erkat’, o-st. ‘iron’, OW W Br. Cor. bras ‘big’; Ir. bras “strong, big’; bras-, cpds. Celtic LW (?) in OE brzs ‘brass, bronze’
guriu- “heavy; weight’. Cf. gurus, etc. Hes. bri ‘heavy’; beside brimós ‘big, hard"; brízo “weigh down’; R grivna “gold dollar’; Cz. hřivna (talent weight)
guroghos, (n) (guroĝh-) ‘neck, craw’. Cf. gur- cpds. Gk. brókhos ‘noose, halter; MHG krage “neck, throat, ruff; Du. kraag “collar”; EME craw. (For a possible analysis of Gk. as *gur- and *sogh- “hold”, cf. EME hals-fang ‘pillory’, Lat. colli-strigium)
gurom- ‘bum, rumble, roar’. Cf. gurem-, ghrem- and guhrem- for ambiguities in Alb., S1., and Baltic. Gk. brómos ‘roar’: bronté (tthunder': Alb. grénzé ‘hornet’, fr. *guromta, -tio); OCS (am- big.) gromü ‘thunder’; Li. gramai, mpl. ‘phlegm’
guros ‘eater, eating’. Cf. guer-, guor-, guró- (1) Gk. cf. molo-brós “heavy eater’; Tokh. B kor ‘throat’; Alb. cf. gur-maz, id.; Cz. cf. žrout ‘glutton’
gurondh- (?) ‘severe, outrageous’ Gk. cf. (?) brénthos ('arrogance”, fr. *gu- rendh-); Latv. (ambig.) grods “harsh, stark"; OCS cf. grost-okü, id. Cf. Supt.: gród-
gurosmn- ‘eaten; eating’ Gk. brõma ‘food, eaten food’; Alb. cf. n-grânë, T n-gréné ‘eaten, eroded’: Gk. ém-broma “ero-
guremõ, gurëm- — gur-
20
25
30
35
40
45
 
372
sion; meal, snack’
guróu- (?) ‘pitcher’. Cf. gurügos Oss. xwraw ‘jug’; Norw. Dan. kro ‘craw, crop; inn’. (Variants in OS krüka “mug, jug’, and in MHG kruoc, gs kruoges appear to be unre- lated. E cruse, Sw. krus, and MHG krü
--- leaf 217 ---
se ap- pear to be fr. Gk. (via Lat.?), cf. Gk. krossós “bucket, pitcher’, LLat. *crossa > OFr cruise) (Variant: gurü£h-) Arm. krcem ‘gnaw’; krčem (iotacised form: *enash)); Ir. brüghaim, brüighim ‘pound, crush’; OCS gryzgo, grysti ‘gnaw’; gryZa ‘gripes’ (and com. Sl.); Li. gružinti ‘gnaw, nibble’ be- side grugzdu, -eti and grukšiu, ep ‘crunch’; grūžtis, f. ‘gnawing pain, gripes’; o-gde in grau- Ziu, ti ‘gnaw’. Variant (*gurügho) in Gk. brū- khō ‘gnash’ and in Go. krusts, m. ‘gnashing of teeth’ beside kriustan ‘gnash’
gurü£os, å ‘neck, throat; pitcher w. narrow neck, pot'. Cf. gurðu-, gur- (1) Arm. kurck, pl. type: ‘chest; throat’; OS krūka, wf. ‘pot, pitcher’; OE crūce beside crocca, id.; MHG krūche, id.; G Krauche beside (LG type in) Kruke, id.; Du. kruik, Fris. krük; LG Krūk, wf. (Variant of type *gurugh- in Gk. brúx, acc. sg. brükha “depth of sea")
gurus, see gurus and following entries
gurütos (1) “heavy, big'. WP I, 685 Skt. gurut-amah ‘heaviest’; Tokh. B wrotse, orotse ‘big’; OLat. brütus “heavy”; Class. Lat. ‘clumsy, boorish’; MHG krude, sf. *oppres- sion, force, violence, cruelty’; Latv. grūts ‘heavy’
gurütos (2) ‘teeming, thriving’. Same as (1)? WP I, 685 Gk. brütos, on ‘fermer ted liquor’; brútea, npl. ‘lees’; cf. brüsis, f. (^welling-up'. Vbl. n. to next); W brid, pl. iau, m. ‘eruption; scab’ (?), but cf. bhrütos (1) & (2). (Isophonic: MHG krüt ‘herb’, qua *gurütóm)
guruuó ‘teem, be full’. Cf. gurütos (2) Gk. brúð; Lat. (?) con-, in-gruo, but cf. gruuo
gur- (1) ‘devouring; gulp; throat. WP I, 683 Skt. cf. gilami, gire, grnàmi ‘devour’; Av. gar-, xwar-, id. beside garð ‘throat’: Skt. galah, id. and -garáh *-vorous'; Tokh. B kor ‘throat’; Oss. gwr, id. and ‘abyss’; Arm. kur 'eatables' beside
373
orkor, o-st. (throat, fr. *guoreus; Gk. br-, -bros in br-ágkhos, br-ógkhos, -okhthos, br- ókhos, br-ókhó, -ükho, molo-brós, etc.; Alb. cf. gur-mac, -maz ‘throat’; Lat. voro, are; OCS Zro, Zréti ‘devour’; Li. cf. girà small beer, sour milk’; girtas ‘drunk’; girtüs ‘heady’, of wine; Latv. dzira ‘drink’; dzīres ‘feast’
gur- (2) ‘heavy’. See gurus
gur- (3) ‘appellation, song, praise; revere, sacrifice, worship’. Cf. gurdh- (1) and gurtos Skt. giráh, gir ‘praise’; Lat. au-gur, gs -guris, au-guria (here despite WH); Li. giriü, ti ‘praise’; gyrà ‘boasting’
gurbh- (?) ‘thrive’. Evidence ambig. Vedic grbhnámi “welcome, accept, be fruitful; pp. grbhitáh, pp. ‘fruitful’; Li. gurbstü, gurbti ‘thrive’; gurbüs *Iuxuriant?
gurdos, us (form of gurdos, us, q.v.) “slug- gish, stupid, stiff, awkward'. Cf. WP I, 641 & II, 278 and gurndis Per. gül “idiot”; Oss. qal ‘proud’: Dig. $àla (‘stu- pid'. Abaev); Arm. (Iran. LW?) kurt ‘eunuch’; Gk. bradüs ‘sluggish’; LW in Lat. bardus 'slug- gish, stupid; Lat. gurdus “stupid? (in LL: *blunt); W brydd ‘weak’; Pol. gardy ‘finicky’; Blg. grád ‘ugly’; Srb. grd ‘ugly, monstrous, dirty, nasty’; Slovene gfd also: ‘naughty’; Cz. hrd ‘proud’; Lusat. hordy, id.; Pol. cf. also wz- garda ‘contempt’ beside gardzić ‘despise’; Li. gurdùs ‘sluggish, ailing, weak’; Latv. gurds ‘tired, faint’
gurdh- (1). Cf. gur- (3). Cf. WP I, 686 Av. goroóo, adj. ‘howling’; Arm. kardam “call; read out’; Li. girdžiù, girdéti ‘hear’; girdà f. ‘hearing’; Latv. dzirdu, et
--- leaf 218 ---
 ‘hear’ O-gde in Skt. garha “abuse”
gurdh- (2) 'stir, rouse'. Cf. gurgotio Gk. brásso, aor. ébrasa; Alb. cf. ngrydh (stir up, foment': Gk. embrásso ‘cast up’ ofthe sea)
gurdhlom, gurdhrom, à, ios, iə ‘crop, throat, gorge, gorging animal Skt. grdhrah ‘vulture’; Gk. bárathron ‘gorge, abyss’; OCS grülo, Zrülo, n. ‘throat’; Pol. gard- 1o, Cz. hrdlo, wd R górlo, id. beside Zerló, Zérlo ‘mouth’; Li. gurklys ‘crop, adam's apple; bottleneck’; Latv. cf. padzirkle ‘throat?
gureió, gurið, see gurð (2)
gurgont- variant of gurgot-, q. v.
gur- —gurio
10
20
25
30
35
40
45
374
gurgot- (gurgot-) “neck, throat, gullet’. WP I, 683 Per. gulü; Oss. qür ‘throat’; qürtt ‘gulp’; Arm. cf. kokord, i, av, a-st. ‘throat, gullet; Lat. gur- ges, gs -itis ‘whirlpool, glutton’; OI gorgozza *windpipe, throat' beside gargata, gargozza, id.; Mir bráge, gs brágat, beside bráighe, gs bráighid ‘throat’; Mod. Ir. brágha & brághad, pl. bráighde, id.; W cf. breuant, brefant *wind- pipe; OBr. brouant, id.; Cor. cf. breiansen, bryonsen ‘throat’; Srb. cf. grgocem, grgotati *gargle'. See next
gurgotio (gurgotaio) ‘gurgle, gulp’. Cf. gur- dhio, (2) and following entries Arm. karkacem ‘burble, gurgle’; karka£, i-st. s., id.; LLat. re-gurgito, äre: Srb. grgocem, gr- gotati ‘gurgle, gargle’; grgaca ‘gurgle’; Blg. cf. grăgutiv, adj. ‘stammering’
gurgo, io ‘choke, block? (alternative form of type gurg-, q. V.) Arm. karkem, v.id.; ON kyrkja ‘strangle’ be- side (alleged) kvirkja, id. cf. Icel. korka “ill- health’
gurgho, ið ‘creak, squawk'. Cf. gurks- Gk. brákho ‘creak’; Li. (1-basis) girgu, Eti, id. beside (u-basis) Li. gurgu, eti ‘growl’. (Both bases arise also in Li. girgZdeti and gurgZdeti ‘creak, screech, be hoarse’. See next)
gurgul-, gurgur-, see gurg-, gurgul- (1) & (2) Gk. cf. borbo-rugé (‘rumbling of bowels’, fr. *gurgu-) beside gorgüra, f. (^sewer', fr. *gur- gur-); Slovene grgráti ‘gargle’, ambig. cf. gurg-, as also Alb. gürgull ‘gurgle’ and Lat. gurgulio ‘throat’, a LW in Alb. gérgélac, gérgilac, id. (fr. Slav.?)
guris, os, us, io ‘wooded hilltop, hill, woog’. WP I, 682 Skt. girih, m. ‘mountain’; Av gairis, m. id.; Per. girive ‘steep acclivity’; Tokh. B karāś "wood": Hes. barües ‘trees’; Ir. (?) brab ‘summit’; Slo- vak hora (wood; mountain’, but ‘mountain’ in Cz. & E S1.); OCS gora, Blg. gorà “forest; mountain’; Li. eng (forest: i-basis) beside guras (“hilP: u-basis); Latv. dam ‘wood, thicket'. (The e-gde Gk. form deré, deiré (2) ‘hill, height" is of uncertain origin)
gurió ‘sing, praise’. An ambiguous formula, cf. giró & ghiro
375
Sk. grnámi ‘sing, praise, announce"; gir, giráh ‘song, praise’; G cf. kurren ‘croon’ beside quorren “make mating-call — of woodcock’; Li. giriù, ti ‘praise’; Latv. dzirties, refl. ‘boast’
gurksið (gurksKó, gursKo) “call, cry, appeal". Cf. gur-, gurió Alb. grish “call, shout, invite’; Li. girksēti *squawk, as geese’; Latv. gurkstu, gurkstet (u- basis “creak, screech")
gurndis “heavy, bulky'. WP I, 699. Cf. gurus, gurdos (gurdos) Per. cf. garan ‘heavy; expensive’; Alb. (LW?) i rándé, i rëndë, adj. “heavy”; Lat. grandis ‘big’; Tokh. A. (ambig.) krant, krent “lovely”
gur-nou- (analytical form of) gurnüs, à, gur- uoni, guernus, à, guernouos, etc. (cf. gurus ‘heavy’ and nàus, nous "boat from the shape of the nether stone of the handmill when worn down by an upper stone rolled upon it). Arm. erkan, a-st.; Oss. cf. kwrói, krói (for *gür-?) ‘mill’; Gk. cf. güris Tine flour”; Olr. bráu, Ir. bró; Cor. brow; OW breuan; MHG kürne; OCS Zrüny,
--- leaf 219 ---
 gs Zrünüve beside Zrünü- vü, m.; Li. girna; Latv. dzirnas, f. pl. beside dzirnus & dzirnavas ‘handmill, millstone’. E- grade in Go. -qairnus; OHG quirn, quirna; MHG quirn-, kurne-stein; OS quern, u-st.; OFris. quern; OE cweorn; G Querne 'quern'; ON kvern, pl.-ir. f. WP I, 685
guró (1) 'gulp down, devour’. Cf. guer-, guor- Ved., Skt. gire, gilami, gírami, grnami, id.; Av. gar-, xwar-; Lat. voro, åre; OCS (i-basis) Zr, Zréti; Li. cf. girà “small beer" girtas, adj. ‘drunk; tipsy’; girtüs ‘heady — of wine’; Latv. dzira “drink”
gurð (2), (euro, gureio) “load, weigh down, burden'. Cf. gurus Skt. gure ‘raise, lift; cf. garvami "be proud"; Oss. ärgavín, àr$uvun “cock — a gun’; ärgävag trigger; Arm. krem ‘carry, bear, suffer; kruim, krvim "am borne’; Gk. baréo ‘load’; báros, gs -eos ‘weight’; Go. kaúrjan ‘burden’; Lat. cf. gravō, āre; Li. gurnùs ‘portly, digni- fied’; Latv. cf. gurstu, gurt “flag, be tired’. Cf. also Gk. brabeús (?) umpire’, fr. *gurgueu-)
guroghos (?), see guroghos
gurquis ‘neck, throat”. Cf. WP I, 593 and gurgat-. (Cf. grquis)
gurksio (gurkskó, gursKo) — gurüsn-
15
20
25
30
35
40
45
376
Arm: kir, gs krči, i-st. ‘gorge’; Alb. grykë ‘neck, throat; goitre’; Olr. cf. brágae, id.; Blg. Srb. cf. grák-lan, grkljan, id.; Cz. cf. vyhrknout ‘gush out’; Li. cf. gurklys ‘craw, larynx. (In the sense of ‘goitre’, Alb. grykë equates with Cz. hrča, hrče, Srb. grča “lump, tumour’)
gurquið (gurquàið) ‘gulp; choke’. Cf. gurquis Gk. brápto (2) ‘gulp’; Slovene grčiti ‘strangle’; Cz. hrčet, hrknout (1) ‘gurgle’; OCS cf. grù- kajo, ati ‘croak’; grükavü ‘stammering’; Li. gurkiù, ti ‘gulp’
gurqutos, à (?) ‘gulp, throat’. Cf. gurgət-, gurð (1) & WP I, 683 Per. cf. gardan ‘throat, neck’; Oss. qùrtt ‘gulp’; Lat. guttus ‘decanter’; gutta ‘drop’; guttur, gs -uris ‘throat’; Lusat. hort, m. ‘mouth’; OCS cf. grútani, Let m. ‘throat’; Li. cf. gurkčioti, v. ‘gulp’
gurtos ‘revered, favoured, important’; gurtis ‘reverence, favour, importance’. Cf. gurus, gu- rið Skt. gūrtáh ‘celebrated, approved, agreeable’; gürtíh ‘praise’; Per. cf. garāmī, adj. ‘revered, excellent’; Lat. gratus “welcomed, favoured’; grātēs, gp -ium, f. ‘thanks, praise’; Osc. bra- tôm, Pael. bratom ‘offering’; Osc. brateis ‘praise, thanks’; OCz. žrt, i-basis: ‘sacrifice’; OCS cf. žrůtije, id. beside Zrütva, R Zértva, id.; R cf. Zrec ‘priesť; Li. girtas ‘celebrated, prais- ed'
gurudh-, cf. gurus (gurus) Gk. barútho “be weighed down'; Lat. cf. gra- vidus ‘heavy, full
gurus, gurus ‘solid, heavy’. WP I, 685 Skt. gurúh ‘heavy, severe, big, venerable’; gur- vinth, adj. f. ‘pregnant’; Av. gouru-, cpds.; Arm. cf. krem ‘carry, bear, suffer’; Alb. eur ‘stone’; Gk. barüs (&heavy', etc.) beside ém- bruon ‘embryo’; Lat. cf. R-gde grăvis beside gravida, f.; MIr. brú, W bru ‘belly, womb’; Go. kaúrus ‘heavy’; Norw. kry ‘proud’; OCS gyrja, R girja ‘weight’; Li. cf. gurv-uolis ‘clod’; Latv. cf. dzir-kalis ‘stone-cutter’. An OLat. rustic type seems to be represented in barð, -Onis (*dolt. ‘Gmc. or Gallic for Ainsworth 1736) and in barrus ('elephant.. ‘Sabine’ for Ains- worth. See WH:LEW, 3, p. 97)
gurüsn-. Cf. gurus
377 uru Gk. cf. barüno ‘oppress’; Latv. grūsna, adj. f. “in calf
```


## [2026-09-06T14:55:15.414Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls | grep -i \"BQT\\|MON\\|ARY\" ; ls incoming 2>/dev/null"
}
```


### [2026-09-06T14:55:15.482Z] TOOL RESULT

```
BQT_alt_v1.txt
BQT_dli_part1.txt
BQT_v1_djvu.xml
BQT_v1_pages.txt
BQT_v1.txt
BQT_v2_pages.txt
BQT_v2.txt
MON_part1.txt
MON_part2.txt
NYB_vol2_glossary.txt
AHD
ARY
BLY
BQT
CEL
FFD
IRN
ISS
KGW
MAG
MFL
MON
OEW
PLA
PRT
_tessdata
TTS
TYL
VIE
WLD
ZAW
فرهنگ ریشه های زبان فارسی (2).pdf
```


## [2026-09-06T14:55:20.995Z] TOOL CALL #28: Bash

```json
{
 "command": "ls data/verification/sources/refs/ocr/ 2>/dev/null && ls data/verification/sources/refs/ocr/BQT 2>/dev/null | head -50 && sed -n '1,60p' tools/ref_page.py"
}
```


### [2026-09-06T14:55:21.045Z] TOOL RESULT

```
AFM
ARY
BOOK
BQT
HRN
IRN
PLA
SNS
SOD
0001.png
0001.txt
0049.png
0049.txt
103.vision.txt
1225.png
1225.txt
1225.vision.txt
1275.png
1275.txt
1294.png
1294.txt
1294.vision.txt
1299.png
1299.vision.txt
1300.png
1300.txt
1300.vision.txt
1302.png
1302.txt
1302.vision.txt
1339.png
1339.txt
1357.png
1357.txt
1382.png
1382.txt
1385.png
1385.txt
1385.vision.txt
1445.png
1445.txt
1445.vision.txt
1452.png
1452.txt
1455.png
1455.txt
1462.png
1462.txt
1465.png
1465.txt
1471.png
1471.txt
1472.png
1472.txt
1488.png
1488.txt
1492.png
1492.txt
1624.png
#!/usr/bin/env python3
"""Fetch ONE cited page of a scanned reference, on demand.

    python3 tools/ref_page.py BQT:918          # printed page 918 of Borhan-e Qate'
    python3 tools/ref_page.py IRN:119 --image  # also print the path of the page image
    python3 tools/ref_page.py BQT:918 --pdf-page 375   # override the offset mapping

Looks up the reference in data/verification/sources/refs_online.json
(`scans`: list of {file, first_printed, last_printed, pdf_offset, lang}), renders the
matching PDF page to PNG (for reading with a vision model), OCRs it with tesseract in
the reference's language(s), caches both under
data/verification/sources/refs/ocr/<ABBR>/<printed page>.{png,txt}, and prints the
OCR text. Only the cited page is ever processed — never the whole book.

`pdf_offset` means: pdf page index (1-based) = printed page + pdf_offset.

If the OCR is too poor and you transcribe the relevant passage(s) from the PNG yourself,
save that transcription as <printed page>.vision.txt next to the .txt; from then on this
tool prints the transcription instead of the OCR, so no page is ever read twice.
"""
import sys, os, json, subprocess, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "data", "verification", "sources")
TABLE = os.path.join(SRC, "refs_online.json")
REFS = os.path.join(SRC, "refs")
OCR = os.path.join(REFS, "ocr")
TESSDATA = os.path.join(REFS, "tessdata")


def main(argv):
    args = [a for a in argv if not a.startswith("--")]
    if not args:
        print(__doc__); return 2
    m = re.match(r"^([A-Z]+)(\d*):(\d+)$", args[0])
    if not m:
        print("expected ABBR:page (e.g. BQT:918 or MON5:528)"); return 2
    abbr, vol, page = m.group(1), m.group(2), int(m.group(3))
    table = json.load(open(TABLE, encoding="utf-8"))
    ref = table.get(abbr, {})
    scans = ref.get("scans") or []
    if vol:
        scans = [s for s in scans if str(s.get("volume", "")) == vol] or scans
    scan = None
    for s in scans:
        if s.get("requires_volume") and not vol:
            continue
        if s.get("first_printed", 0) <= page <= s.get("last_printed", 10**9):
            scan = s; break
    if "--pdf-page" in argv:
        pdf_page = int(argv[argv.index("--pdf-page") + 1])
        scan = scan or (scans[0] if scans else None)
    elif scan:
        pdf_page = None
        pm = scan.get("page_map")
        if pm and os.path.exists(pm):
            pdf_page = json.load(open(pm)).get("map", {}).get(str(page))
        if pdf_page is None:
            pdf_page = page + int(scan.get("pdf_offset", 0))
            print(f"(no exact page map; using offset {scan.get('pdf_offset', 0)} -> pdf page {pdf_page}; check the printed number and re-run with --pdf-page if off)")
```


## [2026-09-06T14:55:28.108Z] TOOL CALL #29: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-06T14:55:28.114Z] TOOL RESULT

```


```


## [2026-09-06T14:55:29.381Z] TOOL CALL #30: Bash

```json
{
 "command": "python3 tools/ref_page.py BQT:1800 --image 2>&1 | head -60",
 "description": "Fetch BQT page 1800"
}
```


### [2026-09-06T14:55:38.046Z] TOOL RESULT

```
(no exact page map; using offset -1205 -> pdf page 595; check the printed number and re-run with --pdf-page if off)
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1800.png
REF: BQT:1800  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 595  OCR-lang: fas

کر که‌آعتی ۱۹۸
در جایی بخورکنند موشانی که در آن توابع | آخر : نومی‌از پای افزار است که شاطرآن‌وپياده
باشتد همه آنجا جمع شوند واگرزنی بر بالای | روان پوشند ویگرگابی شهرت دارد ۷ "
عاش کر که بشاشد هرکز آبتن‌شودا . گرگ‌پند - بفتح بای ایجد وسکون

گر لك آشتی - سلح‌بتفاقومکروحیله | نون و دال » کنایه از کرفتار و اسیر و زبون
وفریب راکویند ۴ . و خقیف باشد ۸ .

گر 4 آشنایی ۴ «کنایه از آشنایی گرگ بند کردن - کنایه از زبون
و دوستی بغریب و نفاق ومکی وحیله باشد وخفیف و آسیرکردن باشد ۸ .

گر گات - بنم اول وکاف فارسی بالف گر گج - بفتح اول وکاف فارسی‌پروزن
کشیده بروزن سلطان» نام‌شهری‌است دردارالملك | اعرج» سر کوبیرا کویند که بجهت کرفتن قلعه‌از
استراباد و معرب آن جرجان باشد ۴ - وبمعنی | اسنگه وگل وچوب مازند ‎٩‏ .
دشت و بیابان هم بنظرآمده است ۵ . گرگ دق - بنم اول وفتح دال ابجد

گر گانج - ضم اول و سکون نون | وسکون واو »کنایه از دویدن آهسته و بسرعت
و جیم » نام دارالملك ولایت خوارزم باغسوممرب | رفتن و پوبه کردن وقطره زدن باشد وآ نرابمریی
آن جرجانیه است و ترکان ارکنج خوانند۹ . | هروله کوبند .

گر گاو 0 * جم اول وسکون واودر گرگ دیزه *۱- بسمنی ک رکهرنکه

) چش : گرکاو ۰

- این مطالب براساسی لیست! ۴ -قس :ک رکه آشنایی :

باد که با خاک بگ رکه آشتی است ایمن ازین راه ز ناداشغتی امت .

نظامی کنجوی « کنجینه کنجوی ۱۳۲ *.

۴ ر4: رشیدی» وقس: ک رکه‌آشتی . ۴ - پهلوی ۷۱۲۵۳ [20ع6007] -
117۳0892 . ر43 : مار کوارت : شهرستانها ص ۱۲ ح ۱۷ ؛ اونوالا ۹۲ . کرگان باطلاق عام
عامل ابالت استرایاداست که از شمال ببحرخزر وازمشرق بخراسان و ازمغرب بظبرستان میکشید
: مسج‌البلدان » و باطلاق خاص شهری قدیمی است درکنار رود گر کان و بدوقسمت تقسیم‌میشده
یکی شهرستان و دیگری بکرآبا د که بواسطةٌ پلی بهم متصل بوده‌اند و مقبرء قابوس وشمگیر در
سه کیلومتری این شهر ومعروق بکنید قابوی است «کیهان . جغرافیای سیاسی‌ص ۳۰۹ »جمعیت
کرکان ۲۰۰۰۰تن وجزه استان دوم است . 8 - ونیز جمع گر که کر کان آید .

-جرجالیه نام قضصبة انیم خوارزم وشهرست بز رکه برساحل جیخون و مردم خوارزم
آترا پزیان خود «کرکانج » میخوانند: پس‌آلرا تمریب کرده جرجالیه گفتند « معجم‌البلدان > .
لور کنج ۳ کر کانج < جرجانیه کرسی ولایت خوارزم امت « عباس اقبال. تاریخ مغول صس۵».

۷ - بجتجوی توگردون چو عزم راه‌کند ز خام ورکند پای ماه راگرگاو ‏

آذری طوسی « رشیدی > .

۸ - فرهنکه نظام نوشته :کر که‌بند . از ترس از جای خود نجنبیدن :

لزین کربه کون خاکه تا چندچند بغیری توان کردنش کر که بند .

8 « رشیدی» « فرهنگه نظام >.

. ‏-ر3 : جهانگیری - ۴ رك : دیز » دیژه‎ ٩
```


## [2026-09-06T14:55:49.512Z] TOOL CALL #31: Bash

```json
{
 "command": "python3 tools/ref_page.py BQT:1806 --image 2>&1 | head -70",
 "description": "Fetch BQT page 1806"
}
```


## [2026-09-06T14:55:51.077Z] TOOL CALL #32: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/گریستن",
 "prompt": "Give the full etymology section for Persian گریستن (geristan) 'to weep': Middle Persian form, Proto-Iranian root reconstruction, cognates, and any cited authorities (Cheung, Hasandust, MacKenzie)."
}
```


### [2026-09-06T14:55:56.477Z] TOOL RESULT

```
(no exact page map; using offset -1205 -> pdf page 601; check the printed number and re-run with --pdf-page if off)
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1806.png
REF: BQT:1806  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 601  OCR-lang: fas

کره بر ۱۸۰۵
آمده است ۱ چه کره‌گشا بسنی مشکل کعا گره گردان - نام نوعی از بازی
باشد - و بفتح اول وثانی و خفای ها , سپو را |[ باشد ۴ .
کوبند و آن ظرفی باشد بجهتآب آوردن . گره گوشت - بکر اول وتات .
گره بر ؟ - بکسر اول وننی‌وسکونها [ غدد راکویند و آن کرهی است سفید که درمیان
و بای مضموم برای فرشت زده » بمعنی طراد | کوشت میباشد .
0 ان غضی است که درین زمان به که گرهه بکسر اول وثانی وفتح ثالت.
بر اشت درد : بممنی گرهچه باشد که گره کوچك: است ؛ وباید
1 گره بر با - یک اول وتانی .کنایه معثی با تغدید ثالك هم کفته اند 8 - ور
از بی اعتباری دنیا باشد چه هرکاه گوینده کره
باد مرن» مراد ان باشد که مال دنا ان کوچکی که دربباتات بهم رسد 8 - و بم‌اول
بریاد مزن» مراد این ب دیا ذخیر» | . 7
منه ویرعمر اعتماد مکن که دیا اعتماد راشاید. وی مخلف کروعه است که کلوله و کروه‌مردم
مد ‎٩‏ .
گره‌برگره - کنایه از مشکل بر ری ۷ - بفتح اول و کسرنانی‌وسکون
َ وگ تحتانی» هرپیمانه رآ گویند خواه جر یب که‌پیمانهٌ
گره بر گوش ددن - کنابه | زمین است ۸ و خواء کز که زمین وجامه وامثال
سخن کی بشنیدن وکر شدن باشد. . آن بدان پیمایند و ک زکنند و خواء کیله که
گرهچه ؟ » بکر اول وفتح جیم | بیان غله است؟ و زخواه پنگان (۱) که‌پیمانة
فارسمی کر ه كوچك راکوبند . ساعت باشد *۱و آن جامی است از مس و درین
گره ددتن - کنایه از ذخیره نهادن | .آن سوراخی کنند بعنوانی که چوب‌آلرا بر زبر
ومال دلیا جمع کردن باشد . آ بگذارند بعد ا زگذشتن يك ساعت نجومی پر
(۷) چش: بنکان. [
۹ - رك :کره برکره . ۴ - از :کره۳ بر ( برنده ) ( بضم باه) .
۴ - از :کره + چه (پسوند صفیر ) :
من خود بگرهچه کیایی قالم شده‌ام ز هرابایی - نظامی کنجوی « رشیدی ».
قس: کردی827801 (مفصل, بند وبت) «ژابا ص۵ ۳۵*. ورك: گرهه. ۴ - ر4: رشیدی.
8 - رك :کره , کرهچه . ۹ - مخفف کروعهه (ه.م.) ؛ و در شعر رورت
بسکون دوم :
چنان زد برو کرعه منجنیق که شد کوه در آب دربا غریق .
نظامی کنجوی « رشیدی » « فرهنگه نظام » .
۷ -فی : جرب ( رك : المعرب جوالیقی ص۹۱۱ متن و حاشیه ) .
۸ - زانکه امثال مرا بی خاعری بیار داد کاخهای چارپوشش باغهای چل کری.
انوری آبیوردی « رشیدی ». در دبوان چاپ تبریز ص۲۱۳ ۸« چل دری » آهده.
4 - چرخ است خوشه ای ز زکاش مدار چشم
کان سا کو دهد دوکری ۰ یك قنیز نیت .
خاقانی شروانی «فرهنگه‌نظام».
۴ رك :گربال و رك : پنگان .
```


### [2026-09-06T14:56:03.395Z] TOOL RESULT

```
# Etymology of Persian گریستن (geristan)

**Middle Persian Origin:**
The word derives from Middle Persian /⁠griyistan⁠/, as indicated in the Wiktionary entry.

**Proto-Iranian Root:**
According to Cheung (2007), the etymological root is reconstructed as "*garz" in his Etymological Dictionary of the Iranian Verb.

**Cognates:**
The entry lists related forms across Iranian languages:
- Northern Kurdish: _girîn_
- Northern Luri: _gerêvesen_

**Cited Authorities:**
1. **Cheung, Johnny (2007)** – "Etymological Dictionary of the Iranian Verb" (Leiden Indo-European Etymological Dictionary Series; 2), Brill Publishers, page 112

2. **MacKenzie, D. N. (1971)** – "A Concise Pahlavi Dictionary," Oxford University Press, page 37

3. **Dehkhoda, Ali-Akbar** – Referenced in the Dehkhoda Dictionary Institute's entry for this term

The semantic development traces "to cry" or "to weep" from the Middle Persian verbal root through modern Persian dialects (Classical, Dari, Iranian, and Tajik).
```


## [2026-09-06T14:56:11.989Z] TOOL CALL #33: Bash

```json
{
 "command": "python3 tools/ref_page.py BQT:1803 --image 2>&1 | head -60",
 "description": "Fetch BQT page 1803"
}
```


## [2026-09-06T14:56:13.873Z] TOOL CALL #34: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/g%CA%B7erH-",
 "prompt": "Is there a PIE root *gʷerH- meaning 'to praise, welcome'? Give its reconstruction, meaning, and descendants (Sanskrit, Avestan, Latin, Lithuanian)."
}
```


### [2026-09-06T14:56:20.321Z] TOOL RESULT

```
(no exact page map; using offset -1205 -> pdf page 598; check the printed number and re-run with --pdf-page if off)
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1803.png
[transcription from the page image; OCR text in data/verification/sources/refs/ocr/BQT/1803.txt]
[Borhan-e Qate', ed. Mo'in, printed page 1803 = PDF page 600 of BQT_v3_picofile.pdf
 (NOT pdf 598: the running heads read 1801 = pdf 598, 1802 = pdf 599, 1803 = pdf 600,
 1804 = pdf 601, i.e. printed = pdf + 1203 in this region; the earlier cached 1803.txt
 was the OCR of pdf 598 = printed 1801. Running head of this page: «گره».)
 Transcribed from the page image by a vision model, 2026-09-05.]

Headwords on the page (col. 1 -> col. 2):
  گروه ۴ - بضم اول و ثانی بر وزن شکوه ، جماعت مردم را گویند و بعربی قوم خوانند .
  گروهه ۵ - ... بروزن و معنی کلوله است مطلقاً ...
  گروی ۸ - ... نام یکی از خویشان افراسیاب ...
  گرویدن ۹ - ... بمعنی ایمان آوردن و سر باطاعت نهادن و پذیرفتن ...
  گره ۱۰ - بکسر اول و ثانی و ظهور ها ، معروفست اعم ازینکه در ریسمان یا در درخت و امثال
        آن ... و بعربی عقده گویند ... و بمعنی مشکل هم بنظر آمده است ...

Mo'in's etymological footnotes (bottom of the page), verbatim:

  ۴ - پهلوی grôh ( دسته ، گروه ) ، ارمنی ع groh ( ملت ، جمعیت )، بلوچی grôf ،
      ایرانی باستان - *gravathva « نیبرگ ص ۸۴ »، کردی kuruh (اجتماع اشخاص)
      « ژابا ص ۳۳۱ » .

  ۵ - قس : کلوله ، غلوله . مخفف آن «گروهه» .

  ۸ - Guröy ( = Guröi Zirih ) رك : فهرست ولف .

  ۹ - virravistan ( از virrav_ ) (باور کردن ، گمان کردن)، پازند varöistan
      از اوستا - var ، « بارتولمه ۱۳۶۰ » ، « نیبرگ ص ۲۴۴ » و رك : اشتق - هوبشمان ۹۱۲ .

  ۱۰ - پهلوی grah « تاوادیا ص ۱۶۱ : ۲ »، کردی ghiri (گره ، عقد ازدواج) « ژابا
      ص ۳۶۱ » ، از پارسی باستان - *gratha ، سانسکریت grath ( بستن ) « هوبشمان ص۹۳ » .

[Both footnotes are the pages Nourai cites as BQT:1803 for his Old Persian box
 (gratha, gravatha), for Persian گره and, through MON, for گروه.]
```


### [2026-09-06T14:56:27.129Z] TOOL RESULT

```
# Proto-Indo-European Root *gʷerH-

Yes, there is a PIE root *gʷerH- with the meanings you mentioned.

**Reconstruction:** *gʷerH-

**Meanings:** The root carries two primary senses: "to express approval; praise" and "to elevate."

**Key Descendants:**

- **Sanskrit:** गृणाति (gṛṇā́ti) - from the nasal-infix present formation
- **Avestan:** 𐬀𐬎𐬎𐬌 𐬔𐬆𐬭𐬆𐬧𐬙𐬈 (auui gərəṇte) - also from nasal-infix present
- **Latin:** grātuītus (gratuitus) - from *gʷérH-tus meaning "welcome" or "pleasing"
- **Lithuanian:** gi̇̀rti (girti) - from the zero-grade ye-present formation

The root also generated the Sanskrit noun गिरि (girí, "mountain") and appears in Celtic terms like the Proto-Celtic *bardos ("poet, bard"), reflecting the semantic connection between praise and elevation.
```


## [2026-09-06T14:56:35.083Z] TOOL CALL #35: Bash

```json
{
 "command": "python3 tools/ref_page.py BQT:1802 --pdf-page 599 --image 2>&1 | head -60",
 "description": "Fetch BQT printed page 1802"
}
```


### [2026-09-06T14:56:43.639Z] TOOL RESULT

```
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1802.png
REF: BQT:1802  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 599  OCR-lang: fas

کر می‌خوتایه : 1 -۱۸۰۲-
گرمی‌خو نابه * کنایه از بسیاری گرنه ۹ < پم اول‌وفتح نون»نام گیاهی

وشتاب وتمجیل درگربه باشد . است .9۳
گرفج « بنم اول وکس ثانی وسکون گرود ۲ - بکر اول بروزن کشود.

نون و جیم » بمعنی.چین وشکنج باشد- وکنج | بمعنی واجب باشد که در مقابل ممکن است.

و کوشه‌رغولهٌ خانه را نیز کویند- وبرنج‌خوردنی گر ورفر تاش ‎٩‏ بفتع فا واتای

را هم گفت‌اند ‎٩‏ که بمربی ارز خوانند 3 بان | بالف کشیده . این لفت مرکب است از کرود

ممنی بضح تانیهم همست وفرتاش بمعنی واجب‌الوجود چه گروربمعنی‌واجب
گر نجار ؟ » بنم اول و کس نانی وفرتاش بمعنی وجود باشد .

وسکون ثالك و جیم بالف کشیده وبرای فرشت | گروانه * - بشم اول و افتح زای

زده » پرنج زار وشالی‌زار راگوبند . نقطه‌دار بروزن ستوده » بمعنی جمع و گروءمردم
گر فج بشیر - بسسنی شیر برنج است | باشد .

وآن شله‌ای باشد که با شیرپزند ۴ . گروس اس اول بر وزن خروس »
گر نده ۴ - پنم اول وکس‌نانی‌وسکون بمعنی موی پیچه و موی باف زنان باشد *۱ -

نون وفتح دال » لیف جولاهگان وشوبمالان باشد . و بمعنی چرك وریم جامه و بدن هم هت *۱-

وآن جلروب مانندی است که بدان آش و آهاد | وکرسنگیرا نی زکویند ۹۱.

برتار جامه مالند وبعربی شوكة الحايك خوانند. روخ ۳ سر اول , بروزن وم
گر نگ - بفتح اول وئانی بروزن‌پلنگه. ۱ ۳ ول » بروژن و معلی

لشک رکاء وجنگهکاء راکویند ۵ - وبکراون | ددوغ ات د ای کب گوبند :

وئانی. بمعتی درهم شکته باشد . گر و گان ۱۴- بنم اول ونانی و کاف

۹ - رد : برنج . و رك : فهرست ولف .

۲ - از :گرنج+جار (< زار پوند مکان ) [ بك ج حذف شده » قس : راستره
راست‌تر ] ۳ کرنج‌زار « رشیدی > . ۴ - رد4 : رشیدی . ۴ - رك :کرنده .

8 - رك :کرنك . ۹ - رك :کرنه . ۷ - برساختهٌ دساتیر « فرهنگه
دساتیر ۹۳)»؛ مخقف ومصحف « کرو کر» (ه.م.) ۸ - برساختهٌ دساتیر ۶ فرهنگ دساتیر
‎٩ ۳‏ - جهانگیری ( وبنقل او رشیدی ) بمعی جمع و گروه مردم‌آورده‌اند بدون
شاهد . واظ . مصحف «کروه » است . ۰ کرس (و.م.) ۱- رك #گری .

ایزه جهانگیری این بیت فردوسی را شاهد آورده :

یکی دیگری زن برین هم نشان گروغ ازکناه است برس کنان .
ولی این کلمه در فهرست ولف نيامده واظ ۰ مصحف « دروغ > است .

۴ از :کرو(ه.م.) ۲ کان ( پوند اصاف وسبت ). در اوراق‌مانوی پیهلوی8۲۷۷872
( رهن ) ( 0.83 ,1 ,126 , 83505 ...36۳9188 ع6ا۸۸:44 ‎٩۶‏ اقا ۸ مق ط2ن2 1760 )

7 گرو - بکسر اول و فتح دوم آرمنی ع 8۳8۷ ( رهن ) . پهلوی 8۳۲2۷ |[ نوشته
میشود 8۲801 ] ( رهن ) » از پارسی باستان - 38۳208 » گروگان فارسی ازهمین ماده‌است,
اققانی ع 8۳8۷ ( رهن ) . « هوبشمان سس ۹۷ ؛ پول با مال باچیزی دیگر که قرض گیرنده
تزد قرض دهنده ( یا امیر وپادشاء مغلوب و زبر دست نزد پادشاه غالب و زبردست) گذارد .تایی
از ادای قرض ( یا اجرای تکالیف ) مسترد شود » رهن - مرهون .
```


## [2026-09-06T14:56:54.483Z] TOOL CALL #36: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1803.png"
}
```


### [2026-09-06T14:56:55.097Z] TOOL RESULT

```

```


## [2026-09-06T14:56:55.094Z] INPUT

[Image: original 1925x2971, displayed at 1296x2000. Multiply coordinates by 1.49 to map to original image.]


## [2026-09-06T14:57:15.383Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"پیغاره\\|بیغاره\" BQT_v1_pages.txt BQT_v1.txt BQT_v2_pages.txt MON_part1.txt MON_part2.txt 2>/dev/null | head -20"
}
```


### [2026-09-06T14:57:15.451Z] TOOL RESULT

```
BQT_v1_pages.txt:22574:بیغاره بر وزن گهواره » بمعنی بیفار
MON_part1.txt:27153:پیغار: (۳2۵۳)06۷۰ [- بیغاره - بیغاره] (ا.) 
MON_part1.txt:42553:ملامت کردن. (امص.) سرزنش, بیغاره؛ ج. 
BQT_v1.txt:45149:بیغاره بر وزن گهواره » بمعنی بیفار
```


## [2026-09-06T14:57:17.221Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== MON grami ==\"; grep -n \"گرامی\" MON_part2.txt MON_part1.txt | head -5; echo \"== MON garzman/gorugar ==\"; grep -n \"گرزمان\\|گروگر\" MON_part1.txt MON_part2.txt | head"
}
```


### [2026-09-06T14:57:17.298Z] TOOL RESULT

```
== MON grami ==
MON_part2.txt:5303:فخم: (ع.] (ص.) بلند. قدرء گرامی؛ 
MON_part2.txt:5315:بزرگوار: گرامی؛ ارجمند. 
MON_part2.txt:30346:گرامی: 1-:5:»: (ص.) عزیزه محترم. 
MON_part2.txt:30347:ضح.- در نظم و نثر فصیح همه جا گرامی (- 
MON_part2.txt:30348:گرامیکث» به.) آمده و «گرام ۲ - که در 
== MON garzman/gorugar ==
MON_part2.txt:31356:گرزمان: -8۵۲02 ,22۲2۳018 (.) عرش خداء 
MON_part2.txt:31539:گرگر: و [- گروگر| (۱.) خدای تعالی. 
MON_part2.txt:31797:ترکیب توصیفی «یزدان گروگر» با «خدای
```


## [2026-09-06T14:57:20.899Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== MON gerami ===\"; sed -n '30340,30360p' MON_part2.txt; echo; echo \"=== MON garzman ===\"; sed -n '31350,31362p' MON_part2.txt; echo; echo \"=== MON gorugar ===\"; sed -n '31530,31545p' MON_part2.txt; echo; sed -n '31790,31805p' MON_part2.txt; echo; echo \"=== MON peyghar ===\"; sed -n '27148,27162p' MON_part1.txt"
}
```


### [2026-09-06T14:57:21.037Z] TOOL RESULT

```
=== MON gerami ===


گرامافون: 0- ۳6۲۱05 (- گرامافن | .( 
التن اشت که صفحه‌ای را که آوازی در 
آن ضط شده به گردش در آورد و همان 
آواز را به گوش رساند. جعبةً صوت. 
گرامی: 1-:5:»: (ص.) عزیزه محترم. 
ضح.- در نظم و نثر فصیح همه جا گرامی (- 
گرامیکث» به.) آمده و «گرام ۲ - که در 
تداول بجای گرامی پا کرام عربی (ج. کریم) 
استعمال کنند . درست نیست. 
گران: 2030 (ضن:] کیت تقیل» وزین؛ 


مق. سکك» خفیف. سخت؛ شد ید. بررکگک» 
عظیم. آنچه قیمتش به نسبت اشیای دیگر 
زیاد باشد؟ نمین 4 مسة. ارزان. سار انسوه» 
فراوان. پرقوت» غلیظ» پرمایه. مشکل. 
دشوار» صعب. (کد.) شخص ناگوار و 
بکروه 
ی کی ی 

=== MON garzman ===
مرد» آلت تناسل مرد» 1 
آلت نرینهة جانوران. 

گرزدن: 0۲-0 (مص‌ل.) (عم.) شعله 
زدن» مشتعل شدن» الو گرفتن. 

گرزمان: -8۵۲02 ,22۲2۳018 (.) عرش خداء 
علیین. (توسعاً) آسمان» سیهر. 

ورن 00 ([قس. کر زن» معر .| (1.) تاج و 
نیم تاجی که از دیبا می‌بافتند به زر و گوهر 
مسغرق کرده و آن را بر بالای سر شاه 
می آو بختند. (گیاء) گل آذینی است محدود 

=== MON gorugar ===
گرگ آشتی مي : آا28-.ع (امر.) آشتی ظاهری که 

در باطن دل‌های طرفین بر دشمنی باقی باشد؛ 
به نقاق و مکر و فریب. 

کانند" ۵ (ص مر .) (کد.) گر فتار و 

اسیر. زبون» خفیف. سیار ترسان. 

گرگر: و [- گروگر| (۱.) خدای تعالی. 

گرگر: ۲ (.) تخت شاهی؛ سر بر. 

کر کر ۲ اقس. غر غر | (اصت.) سحنی 

که از روی خشم به زیر لب گویند؛ غرغر. 



فر هنک فارسی معین 


گرو 
نمی‌نماید. (اخ.) خدای تعالی (و آن بجای 
ترکیب توصیفی «یزدان گروگر» با «خدای 
و اسنتا: 

گر وگر: :-00(۰: ۱- گ رگر | (قمر.) 


#4 سبار زباد» فراوان. بشت سر هم 



=== MON peyghar ===
دست دادن به عنوان عهد و پیمان» بیمان 
ستن» عهد کر دن. (.) عهد» پیمان. 
بسیعت: ۵7 [ع. بیعة] (.) معبد یهود و 
نصاری؛ ج. بیعات. 

پیغار: (۳2۵۳)06۷۰ [- بیغاره - بیغاره] (ا.) 
سرزنش» طعنه. 

بیغال: 93,2۱ (.) نیزه» رمح. 

بیفم: «هبآه آف. ع.] (ص‌مر.) بی‌اندوه» 


۳۰۴ فر هنگ فارسی هزم ۷ بیغو له
```


## [2026-09-06T14:57:34.008Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '22560,22600p' BQT_v1_pages.txt; echo \"=== pdf page tag ===\"; awk 'NR<=22574 && /\\[pdf page/ {t=$0} END{}' BQT_v1_pages.txt; grep -n \"\\[pdf page\" BQT_v1_pages.txt | awk -F: '$1<22574' | tail -3"
}
```


### [2026-09-06T14:57:36.003Z] TOOL RESULT

```
که حلاهل نامند و لهذا زهر هلاعل عبارت ازوست » واوسرم نفوذتر ازسم افعیاست وقلیل اقسام
ار کمتر از دوساعت فانل است و در بلاد هند نیزاقام‌اومیباشد . » ۶ بشت ۲۷۵۱ ح* : معرب
آن نیز «یش» است «نفس » . - در اصطلاح احکام جوم بیش‌فارسی پممنی ترح وآفت عربی است.
< کاءشماری ص۳۳۷ ». ۴ اوستا ۷۵125198 (جنگل ) » سااسکرت ۷۳۴5۲18 (درخت)
«اسفا ۱: ۲ ص۸۸ ۰ پهلوی ۷151216 < بندهش 6۱۸۹ . سفدی ۷151021 «کوتبو ۱۱۸ » طبری
ما سرانی کنونی ۷1502 د« واژه نامه ۷۹۹ » اورامانی ۷۵58 « .اورامان ۱۲۷
۴ مصحف : بیفا. درعردی ببغاء بفتح‌اول‌وسکون دوم‌وفیز فتح اول ودوم‌مضفف رهم بفتح‌اول
ودوم مشدد». طوطی ست:
* یطار -بفتح اول, از بونانی ۳۳1۵/۳05] م رکب از1۳۳05 بممنی اسب و 180۳05
پزشك ( 134718 مداوا) ؛ جمماً بمعنی ستور پزخكو 1120184۳6 درفراضه بمعنی درمانکننده
اسپ‌از خمین ریده است «تفس». همرب‌آنهم بیطار وییطر بفتح و کسر اول (هردو) , رك : دائرة -
المعارف اسلام -۳۹۳6 سد
بیقاد ه بنتح اولبروزن نیزار , سرزنش
وطعنه باشد.
بیغاره بر وزن گهواره » بمعنی بیفار
ات که سرزش وطمنه باشد ٩‏ .
بیغال » بکر اول بر وزن فیفال »
بمعنی نیزه باشد که بعربی رمح خوانند .*#
بیگار ‌- با انی محپول و کاف فارحی
بر وزن بی زار , کار فرمودن بی مزد بود معنی
کار بفی‌مایند و اجرت ندهند. #۶
لیگاه - با ثانی مجهول بر وزن بیراهه
بمعنی شام است که در برابر صبح باشدب و غیر
وک میگ :۱ یز گوینه.
لیگم ه بنتح اول وکاق تازی و سکون
ثانی و میم » صفه و ابوانر! کویند ,3۶
دبکند ‌ بقتح اول و کاف ‌ِ روزن‌سو ند
نام قن ات ]ملک زرم 2 جمشید وبای تخت افر اباب
بوده . و بعضی کویند فربدون آن شهر را بنا
کرده اس ۴
که با کاف فارسی بر وژن سره »
۱ ژد : بمفار : وییغازه
و وی
مخفف بیگاء است که
۷ باشد .
لیل- بانانی مجهول
بر وزن فیل » آلنی باشد
آهنی(۱) که باغبانانو امثال
ابشان زمین بدان کنند ۴
- وپاروبیرا(۲) نیز گویند
که کشتی‌بانان بجهت‌راندن
=== pdf page tag ===
```


## [2026-09-06T14:57:43.329Z] TOOL CALL #41: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%AF%D8%B1%D8%A7%D9%85%DB%8C",
 "prompt": "Give the full etymology of Persian گرامی (gerâmi) 'dear, respected': Middle Persian form, older Iranian reconstruction, PIE root, cognates and cited sources."
}
```


## [2026-09-06T14:57:45.109Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/grace",
 "prompt": "Give the etymology chain for 'grace', and any mention of Latin gratia, gratus and PIE *gwere- 'to favor'. Also note what it says about gracious, grateful, agree, congratulate if present."
}
```


### [2026-09-06T14:57:49.055Z] TOOL RESULT

```
# Etymology of Persian گرامی (gerâmi)

Based on the Wiktionary article provided, here's what is documented:

**Middle Persian Origin:**
The word is "inherited from Middle Persian [Book Pahlavi needed] (glʾmyk' /⁠grāmīg⁠/, 'treasured, dear')."

**Historical Development:**
The term evolved from a Middle Persian root meaning "treasured" or "dear" into its modern Persian form with the sense of "precious, excellent" and "dear, beloved, respected."

**Limitations:**
The article does not provide:
- An older Iranian reconstruction beyond the Middle Persian form
- A Proto-Indo-European (PIE) root
- Cognates in other languages
- Cited scholarly sources beyond a single 1934 Persian-English dictionary reference

The etymology essentially traces the word back to Middle Persian without extending further into deeper historical linguistic layers. A more comprehensive etymological analysis would require consulting specialized historical linguistic sources not included in this Wiktionary entry.
```


### [2026-09-06T14:57:50.998Z] TOOL RESULT

```
# Etymology Chain for "Grace"

## Main Etymology Path

**Grace (noun)** originates in the late 12th century from Old French *grace*, which derives from Latin *gratia* meaning "favor, esteem, regard; pleasing quality, good will, gratitude."

The Latin *gratia* connects to *gratus* (pleasing, agreeable), which traces back to the Proto-Indo-European root **\*gwere-** (2) meaning "to favor."

## Sense Development

The semantic evolution includes:
- Late 12c.: "God's unmerited favor, love, or help"
- Early 14c.: "virtue"
- Mid-14c.: "beauty of form or movement, pleasing quality"
- 1579: Classical mythological sense (the three Graces)
- 1650s: Musical embellishment sense

## Related Words in Document

The page mentions **graceful** and **graceless** as related derivatives, but does not discuss *gracious*, *grateful*, *agree*, or *congratulate*.
```


## [2026-09-06T14:58:04.613Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls incoming/ARY/ && grep -n \"گرامی\\|گریستن\\|گرزمان\" incoming/ARY/ARY_pages.txt | head -20"
}
```


### [2026-09-06T14:58:04.670Z] TOOL RESULT

```
ARY_aryanpur_kashani_rishehaye_hend_o_orupayi.pdf
ARY_latin_index_pages.txt
ARY_pages.txt
ARY_pages.txt.pages
4716:۲ معنی این واژه در زبان‌های ژرمنی و سانسکریت: گرامی» آزاد.
11835:چم این واژه در لاتین و زبان‌های رومانس: گرامی؛ عزیز؛ گران.
12897:گریه گرییدن گریستن / ۳۳۵
```


## [2026-09-06T14:58:06.801Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== WLD Bd1 gwer praise ==\"; grep -n \"gtterto\\|g^ĕr-\\|gṷer\\|gu̯er\" incoming/WLD/WLD_Bd1_pages.txt 2>/dev/null | head -5; ls incoming/WLD/"
}
```


### [2026-09-06T14:58:06.857Z] TOOL RESULT

```
== WLD Bd1 gwer praise ==
WLD_Bd1_1930_dli_70244_djvu.txt
WLD_Bd1_1930_dli_70244_text.pdf
WLD_Bd1_pages.txt
WLD_Bd2_1927_dli_106624_djvu.txt
WLD_Bd2_1927_dli_106624_text.pdf
WLD_Bd2_pages.txt
```


## [2026-09-06T14:58:09.889Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '12885,12915p' incoming/ARY/ARY_pages.txt; echo \"== page tag ==\"; awk 'NR<=12897 && /\\[pdf page/ {t=$0} END{print t}' incoming/ARY/ARY_pages.txt"
}
```


### [2026-09-06T14:58:11.425Z] TOOL RESULT

```
لهستانی (۳0/(/5): 008۸ متا
روسی ((5514): 008۸ 4 (056 ,113 متتتق
چکه (1ل280): 1108۸ 25 اه
صربی (00/اق588): ه008 139 تلا
برهمی (80/75211۵2): 1108۸ برهان قاطع + ۱۹۷
اسلواکی (51.01424): ه108 فرهنگ معین + ۳۹۷
لیترانی (۸(1۵0۷ 7 7لا): 611۸ لفت‌نامه دهخدا: ۳۳۹۷
بادداشت: 7
۱ چم این واژه در زبان آلبانی؛ سنگه.
۲ این واژه در برخی زبان‌های اسلاوی چم "جنگل" و "کوه" راهم دارد.
[pdf page 434]
1
گریه گرییدن گریستن / ۳۳۵
اوستایی (487/04): مد ار دانمارکی (0۸278): درا ای ی
پهلری (4۲7ال(۸): سوئدی (852015[4): با نی
+ ,038187۸ ,6037۷57۸ نروژی (//07075014/): لد 2 نم
کردی (/70/57/): هلندی (07727): 00
0 ,0ت8ال62 ,۲1820 اسلاوی کهن (ع7/ها٩‏ ال 010): ۱
سانسکریت (54(/58/(7): بشال61۸ 611۸33 271
۸ ت۸7 01718017182 روسی (4ل551۸): 07
لاتین (7100مل): زد ایا چککه (۳256/7): 77( ۱
گرنیکه (0077710): لاد نا
ایسلندی کهن (524(/010۸77۸ 010): پسگشت‌ها رش اف اد ادن ادن
0۸ رس
ساکسونی کهن (54300 ۰:0۵ 68۸1۸0۲ 9 (68851) +7 ملظ
فریزی کهن (/۲۶/514 0ا0): دی نی :۸100/22
آلمانی کهن (0570/۸00 ۱0 صا0): 0 (۲8۳2) ,109 (۴83)
نود مرا رای نی 3 (63387) :002/8
آلمانی (0201224): نایب 7 (۴8) ما 1/0
انگلیسی کهن (80/0/577 010): برهان قاطع + ۶ و ۱۸۰۷
۱ 7 ,0۶37۸ فرهنگ معین : ۳۳۹۵
== page tag ==
[pdf page 434]
```


## [2026-09-06T14:58:11.949Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"gurto\\|gurtos\\|gr̥̄tá\\|gūrtá\\|grätes\\|grates\" incoming/WLD/WLD_Bd1_pages.txt | head -10; echo \"---\"; grep -n \"loben, preisen\\|willkommen heißen\" incoming/WLD/WLD_Bd1_pages.txt | head -10"
}
```


### [2026-09-06T14:58:12.020Z] TOOL RESULT

```
50656:LEWb.      2   u. garrio und grates m. Lit.
---
64983:4. gi‘er(a x )- ...die Stimme erheben", bes. ..loben, preisen. willkommen heiBen -,
```


## [2026-09-06T14:58:18.783Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '64975,65020p' incoming/WLD/WLD_Bd1_pages.txt; echo \"== page tag ==\"; awk 'NR<=64983 && /\\[pdf page/ {t=$0} END{print t}' incoming/WLD/WLD_Bd1_pages.txt"
}
```


### [2026-09-06T14:58:20.467Z] TOOL RESULT

```
yri'/nus ..rein, lauter  entbloBt" wild von Biiga Kalba ir s. 266 zu lit. <j ru-
                                    :


in tjs „Ivahlkopf' gestellt; grins und greitas ..schnelk' weiB ich in der Bed.
nicht zu vereinigeni.


4. gi‘er(a x )- ...die Stimme erheben", bes. ..loben, preisen. willkommen heiBen -,
                                                                                                                                           1




              aber auch ..schelten: jamniern".
      Ai. ynulti, yrnttr „singt. lobt. preist, kiindigt an                                    -
                                                                                                      fut. garisyati,             Absabhi-
guri/a),           sum-yiratr       ..gelobt.      verspriebt. stimmt ein% gurdtc „begruBt“,                                             gir,

g. yirdlt              ..Lob, Lied”,     av. gar-, atbi-ywante                      ,. preisen, lobend einstimmen‘\
yaro gen. f. ,.Lob, Preis; Loblied” (= ai. girdli), yarah- n. .,Lob, Preislied",
mbt-jarolmj- ..Preisgesang". aibi-jarstar- ..Lobpreiser"      ai. jaritdr- „An-                            =
rufer, Sanger. Preiser ", av. *a-gru- ,.zustimmend‘ in CLgromciti- ,,zustim-                      ;



menden Sinnes" is. Bartholomae s. v.     ai. gurtl-h ..Lob"'  lat. grdtts pi.
                                                                      ;                                             =
..Dank" (dazu gratia ..Annehmlichkeit, Wohlgefiilligkeit, Gnade, Danlt“                                                                              ,

ai.       gartd-h         .,willkommen“        —    lat.   jrdtus              ..gefiillig,           dankenswert, dankbar“
nach Kern KZ. 21. 242, weitere                               Lit.         bei Yf.      LEWb. 2                 352)            osk. brateis
..gratiae-.             palign. bratom:         vielleicht         alb. gerids.              Aor yrisa .                 ,,zur   Hochzeit
einladen*               (G.    Meyer Alb. Wb. 124);                lit . giriit,      girti .loben, riihmen“,                           lett.
thirties           ,,sieli    ruhmen",    apr. girluxi ,,loben“, poyirrieit acc. sg.                                       „Lob‘ (Pick
GGA. 1881, 1425 f., Wb. I 4 34, 198,402), auch lit. gems „gut“ (s. Osthoff
MU. 6, 158 f., Trautmann Bsl. Wb. 88, Miihlenbach-Endzelin I 555, Buga
Kalba ir. s. 16S und aksl. gram ( *yornos) „Formel, Vers"' (u. dgl., siehe
Berneker 332).
  Mit b- erweitert: lit. ycrbti .,ehren", lit. ytubc ,,Ehre“, apr yerbt, getbt                                             .


„sprechen‘, glrbui ..Zabl" (zur Bed. s. Trautmann Apr. 338 f., Lewy KZ.
32, 161),              wozu vielleicht gr. [i oajievq „Schiedsrichter, Ordner                                              bei     Kampf-
spielen, Anfiihrei-                 (bisher        nicht    iiberzeugend                gedeutet.                   s.    Boisaccj      130;
                                          GG. 144, Falk-Torp 301, beweist
== page tag ==
```


## [2026-09-06T14:58:27.847Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR<=64983 && /pdf page/ {t=$0; n=NR} END{print n\": \"t}' incoming/WLD/WLD_Bd1_pages.txt; grep -n \"pdf page\" incoming/WLD/WLD_Bd1_pages.txt | head -3; sed -n '64960,64975p' incoming/WLD/WLD_Bd1_pages.txt | grep -n \"68[0-9]\""
}
```


### [2026-09-06T14:58:29.403Z] TOOL RESULT

```
:
```


## [2026-09-06T14:58:32.106Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=64890 && NR<=65060' incoming/WLD/WLD_Bd1_pages.txt | grep -nE \"^\\s*6[0-9]{2}\\s*$|68[0-9]\" | head"
}
```


### [2026-09-06T14:58:33.800Z] TOOL RESULT

```
63:686                                                        g'„1 er(.ii x   V
```


## [2026-09-06T14:58:42.906Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"paiti\\.gar\\|paitigar\\|paiti-gar\\|paiti\\.g\" BRT.txt | head -20; echo \"=== HRN peghare ===\"; grep -n -i \"Vorwurf\\|Tadel\" HRN.txt | head -20"
}
```


### [2026-09-06T14:58:42.982Z] TOOL RESULT

```
=== HRN peghare ===
1086:73. evff 'Castell, Citadelle'.
3379:358. peiyäre 'Tadel' (Sahn. III, 1763, V. 95; 1803, V. 383)^).
3579:*schmähen , tadeln , verachten*, tiraskära- 'Schelten,
10980:vergl. säst 'Schelten, Vorwurf, Drohung, Unwille,
```


## [2026-09-06T14:58:43.687Z] TOOL CALL #51: WebSearch

```json
{
 "query": "پیغاره ریشه‌شناسی فارسی میانه paikār سرزنش حسن‌دوست"
}
```


### [2026-09-06T14:58:51.979Z] TOOL RESULT

```
Web search results for query: "پیغاره ریشه‌شناسی فارسی میانه paikār سرزنش حسن‌دوست"

Links: [{"title":"فرهنگ ریشه‌شناسی فارسی - ویکی‌پدیا، دانشنامهٔ آزاد","url":"https://fa.wikipedia.org/wiki/%D9%81%D8%B1%D9%87%D9%86%DA%AF_%D8%B1%DB%8C%D8%B4%D9%87%E2%80%8C%D8%B4%D9%86%D8%A7%D8%B3%DB%8C_%D9%81%D8%A7%D8%B1%D8%B3%DB%8C"},{"title":"فرهنگ ریشه‌شناختی زبان فارسی - ویکی‌پدیا، دانشنامهٔ آزاد","url":"https://fa.wikipedia.org/wiki/%D9%81%D8%B1%D9%87%D9%86%DA%AF_%D8%B1%DB%8C%D8%B4%D9%87%E2%80%8C%D8%B4%D9%86%D8%A7%D8%AE%D8%AA%DB%8C_%D8%B2%D8%A8%D8%A7%D9%86_%D9%81%D8%A7%D8%B1%D8%B3%DB%8C"},{"title":"فرهنگ ریشه‌شناختی فارسی، محمد حسن‌دوست، 1393 تهران، فرهنگستان زبان و ادب فارسی، دورۀ پنج جلدی","url":"https://lsi-linguistics.ihcs.ac.ir/article_1976.html"},{"title":"زبان فارسی میانه - ویکی‌پدیا، دانشنامهٔ آزاد","url":"https://fa.wikipedia.org/wiki/%D9%BE%D9%87%D9%84%D9%88%DB%8C_(%D8%B2%D8%A8%D8%A7%D9%86)"},{"title":"سرگذشت کم‌شناخته واژه‌های زبان فارسی","url":"https://parsianjoman.org/2080/%D8%B3%D8%B1%DA%AF%D8%B0%D8%B4%D8%AA-%DA%A9%D9%85%E2%80%8C%D8%B4%D9%86%D8%A7%D8%AE%D8%AA%D9%87-%D9%88%D8%A7%DA%98%D9%87%E2%80%8C%D9%87%D8%A7%DB%8C-%D8%B2%D8%A8%D8%A7%D9%86-%D9%81%D8%A7%D8%B1%D8%B3"},{"title":"فرهنگ ریشه‌شناختی زبان فارسی | راهک","url":"https://raahak.com/?p=942"},{"title":"فرهنگ ریشه شناختی فارسی، دکتر محمد حسندوست","url":"https://ariabod.blogfa.com/post/92"},{"title":"محمد حسن دوست نویسنده کتاب فرهنگ ریشه شناختی زبان فارسی(5جلدی) | ایران کتاب","url":"https://www.iranketab.ir/profile/23034-mohammad-hasandust"}]

Based on the search results, here's what I found regarding your query:

The "فرهنگ ریشه‌شناختی زبان فارسی" (Dictionary of Persian Etymology) is a specialized lexicographic work on Persian etymology authored by Mohammad Hasan-Doust, published in five volumes in 1393 (2014) by the Academy of Persian Language and Literature.

The work was recognized as an outstanding publication in the thirty-third edition of the Annual Book Award of the Islamic Republic of Iran in the category of "Ancient Languages."

Previously, in 1383 (2004), the first volume of a dictionary with the same name, authored by Hasan-Doust containing letters "Ā-T", had been published by the Academy of Persian Language and Literature.

The main text of the Persian Etymology Dictionary (Ā-Y) is contained in volumes one through four, comprising 2,955 pages and containing 5,514 entries.

Regarding the specific terms in your query like "پیغاره" (paikār) and "سرزنش" (reproof/censure), the search results don't contain detailed information about these specific etymological entries. If you're looking for information about particular entries in this dictionary, you may need to consult the actual dictionary volumes or search for more specific information about those terms.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-06T14:58:58.005Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '3370,3400p' HRN.txt; echo \"=== leaf ===\"; awk 'BEGIN{RS=\"\\f\"} {n=NR; if (index($0,\"358. peiy\")>0) print \"leaf(1-based)=\"n, \"-> printed p.\"(n-1-21)}' HRN.txt"
}
```


### [2026-09-06T14:58:59.617Z] TOOL RESULT

```
sei mit Fl Pt 1 P 13 ebenfalls paitisa zu lesen (die überschüssige
Silbe besagt nichts); es bleibe also nur yt. 3, 4. Er fasst paitisa als
einen adverbiell gebrauchten Instr. Sing., wie frasa^ apasa (s. LDMG.
43, 670).
*) Wa;^. petSy §i/n. pits *Angesicht, Miene' (S. 780) sind wohl nur
verdruckt statt pets^ pits; oder liegt eine durch den Bedeutungswechsel
verursachte Differenzierung vor?— 80 -
357. 2^^'*^^ ^Handwerk, Gewerbe'.
aw. vergl. pistro- 'Gewerbe*; phlv. pesak.
358. peiyäre 'Tadel' (Sahn. III, 1763, V. 95; 1803, V. 383)^).
aw. "^paiti + 2 [/"gar' (ai. praii + gar- bedeutet auch
nur 'anrufen, begrüssen, antworten).
Spiegel, Ar. Periode, 229.
Bartholomae meint, man könne auch an Ableitung
von ai. prati + [^har- denken (vergl. pratihdrana- und
die Bedeutung von lat. ohjicere), Ai. h entspricht ja
sowohl indogermanischem gji wie g2h,
peiyäni s. peyäm (No. 348).
359. peig (peik) Tussgänger, Häscher, Bote', arab. faij,
aw. "^padika-,
de Lagarde, Ges. Abh. 74; Nöldeke, Tabari-
Übers. 448, Note 2, vergl. auch Denkschr. WAW.
Band 38, 14.
360. peikär, peigär *Kampf'.
aw. *paitikära' vergl. paiti.akerenaot (vd. 2, 6);
phlv. patkär 'Kampf (z. B. vd. 5 (33) GL), patkäritan
'Köcher, (z. B. vd. 4 (137)), patkärok (AV.).
arm. LW. payUar *Kampf' .
361. peiker *Bild'.
Sii^. patikara- 'Bild'; iphlv, patkar (Bund.), arm. LW.
pafker.
=== leaf ===
leaf(1-based)=102 -> printed p.80
```


## [2026-09-06T14:59:14.149Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN grace ===\"; grep -n -o -E \".{200}grace, n\\..{700}\" KLN_1966.txt | head -2; echo; echo \"=== KLN grateful ===\"; grep -n -o -E \".{80}grateful, adj.{450}\" KLN_1966.txt | head -2"
}
```


## [2026-09-06T14:59:15.566Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== LEW gratus ===\"; grep -n -o -E \".{100}grātus.{500}\" LEW_1910.txt | head -3; echo \"=== LAT gratus ===\"; grep -n -i -o -E \".{100}gratus.{400}\" LAT.txt | head -3"
}
```


### [2026-09-06T14:59:15.890Z] TOOL RESULT

```
=== KLN grace ===

=== KLN grateful ===
```


### [2026-09-06T14:59:15.992Z] TOOL RESULT

```
=== LEW gratus ===
=== LAT gratus ===
```


## [2026-09-06T14:59:19.466Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -c \"\" KLN_1966.txt LAT.txt LEW_1910.txt SYN.txt SKT.txt; echo \"---\"; grep -n -i \"gratus\" KLN_1966.txt | head -5; echo \"--- LAT ---\"; grep -n -i \"gratus\\|grates\" LAT.txt | head -8; echo \"--- SKT grace ---\"; grep -n -i \"^grace\\|grace, \" SKT.txt | head -5"
}
```


### [2026-09-06T14:59:19.585Z] TOOL RESULT

```
LEW_1910.txt:14866
SKT.txt:24056
SYN.txt:35876
LAT.txt:82450
KLN_1966.txt:41263
---
8680:conflagration,  n.  —  F.,  fr.  Late  L.  conftagrdli- onem,  acc.  of  conflagratio,  *a  burning’,  fr.  L. cdnflagratus,  pp.  of  conflagrare .  See  prec.  word and  -ion.
8726:congratulate,  tr.  v.  —  Fr.  L.  congratulate,  pp.  of congratulari ,  ‘to  wish  joy  warmly,  congratulate’, fr.  con-  and  gratulari,  ‘to  wish  joy’,  fr.  gratus, ‘pleasing’.  See  grace,  n.,  and  cp.  grateful. Derivatives:  congratulation  (q.v.),  congratulat- or,  n.,  congratulat-ory,  adj. congratulation,  n.  —  F.,  fr.  L.  congratulalionem, acc.  of  congratuladd,  fr.  congratulatus,  pp.  of congratulari.  See  prec.  word  and  -ion. congregant,  n.,  a  member  of  a  congregation.  — L.  congregdns,  gen.  -antis,  pres.  part,  of  congre- gdre.  See  next  word  and  -ant. congregate,  adj.,  assembled.  —  L.  congregdtus, ‘flocking  together’,  pp.  of  congregate,  ‘to  flock together’,  fr.  con-  and  gregare,  ‘to  gather  into a  flock’,  from  grex,  gen.  gregis,  ‘flock’.  See  gre¬ garious  and  adj.  suff.  -ate. congregate,  tr.  and  intr.  v.,  to  gather  into  a  crowd ; to  assemble.  —  L.  congregdtus ,  pp,  of  congre- gdre.  See  prec.  word.
10635:—  L.  deflagratus,  pp.  of  deflagrare,  ‘to  bum  up, be  consumed  by  the  fire’,  fr.  de-  and  fiagrdre, ‘to  bum’.  See  flagrant  and  verbal  suff.  -ate.
10636:deflagration,  n.  —  L.  deflagrdtid,  gen.  -dnis,  fr. deflagratus,  pp.  of  deflagrare.  See  prec.  word and  -ion.
10638:—  Formed  with  agential  suff.  -or  fr.  L.  defla¬ gratus,  pp.  of  deflagrare.  See  deflagrate.
--- LAT ---
3445:de verbes de sens plus abstrait laudo, probo, gratus sum, cf.J.B.Hofmann,
22756:flagrC, -&s, -aul ( flagratus sum, cf. CGL II 73,35»), -atum, -are:
22766:conflagratus "consume" d'oa on a tird a basse epoque conflagrare
26778:nule; granifer (Ov.); egrdno,-as (Mare.). - Cf. aussi M.L.3844 *graniare,gratus
26810:9° ingratus (cf. a^apos et ayapiaxoi, a^api-roe): i° passif: qui n'est
26817:1 . de l’ 4 gl. ingrdt i f icat io', ingratif icentia. Intensifs: pergratus ,
26818:(Cic.); praegratus (luuenc.).
26819:3 ° grates,-ium f.pl.(usiti seulement au nom. et k l'acc. dans les
--- SKT grace ---
20677:Venial.  (F.  —  L.)  O.  F".  vmial.  —  L. titniaJis,  pardonable. -•  L.  utnia,  pardon; also  grace,  favour.     Allied  to  Venereal.
```


## [2026-09-06T14:59:24.357Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '26800,26840p' LAT.txt"
}
```


### [2026-09-06T14:59:24.409Z] TOOL RESULT

```
reconnaissance, agriable (souvent joint k acceptus), favori". Ciciron
le diffirencie a plusieurs reprises de iucundus "qui cause du plaisir,
de la joie", cf. par ex. Att.3,34,3, ista ueritas, etiam si iucunda
non est, mihi tamen grata est', Fam.4,6,1; 5,15,1; 10,3,1; 13,8,3;
cf. encore ibid.1,17,6; Eosc.Amer.18,51, etc.; 3° actif, "reconnaissant,
qui a de la reconnaissance". Ancien, usuel et classique. Le neutre
gratum a iti substantivi et a passi dans les 1 . romanes, it. grato,
ir.gr 4 , M.L.3848. Panromaa, sauf roumain; britt. graz.
Composis: gratificus (b.lat.): obligeaat; gratificor,-aris (attesti
depuis Ciciron): obliger, gratifier, f aire present de; gratificatioidc.)."
9° ingratus (cf. a^apos et ayapiaxoi, a^api-roe): i° passif: qui n'est
pas accueilli avec reconnaissance, ou qui ne merite pas de reconnais¬
sance; 3 0 actif: qui n'a pas de reconnaissance; ingrat; ingratia,-ae
f. (a^txpumoc): usiti seulement dans la‘ bonne epoque k 1 'abl. ingratiis
(formi d'apres gratiis): k contre-coeur. C'est seulement dans Tert.
qu'on trouve ingratia "ingratitude"; ingratitudo (tardif); ingrati¬
ficus: i.Argiui, Acc.ap. Cic., Sest.56,138, "ingrat": de IA dans la
1 . de l’ 4 gl. ingrdt i f icat io', ingratif icentia. Intensifs: pergratus ,
(Cic.); praegratus (luuenc.).
3 ° grates,-ium f.pl.(usiti seulement au nom. et k l'acc. dans les
expressions rituelles grates (-tls) agere, habere, soluere, etc.;
seul Tac. a un dat. gratibus) : marques de reconnaissance, actions
de gr£ces (aux dieux), remerciements. Attesti depuis Plaute. Sare,
de couleur arcbaique; remplaci par gratiae.
4° gratia,-ae f.: i° abstrait "reconnaissance". Ciciron, Inv.3,66,
le difinit: gratia est in qua amicitiarum et officiorum alterius memoria
et remunerandi uoluntas continetur ; s° concret "acte par lequel on
s'acquiert de la reconnaissance"; par suite "service rendu"; 3 0 "faveur,
cridit, influence"; 4 0 agriment, beanti, grace (se dit des personnes
et des cboses). Friquent avec ce dernier sens dans la langue poli-grauastellus
SOS
tique, cone 1 ' adj. gratiosus. Traduit le gr.^apiCJ 1 ^'abi .gratia = )(<x-
puv; Gratiae = Xapuxec; dans la 1 . de 1 'Sgliae = )(apuTp,a. L' abl.pl.
gratiis (puis gratis) 3 'enploie avec valear adverbiale "gracieusenent,
sans exiger de salaire". Ancien, nsuel, frequent dans des locations
verbales gratias agere, referre; grdtiam facere alicui delicti (cf.
Sali., Cat.52,0, Jag.105,5). M.L.3047a. Celt.: iri. grds, greit; gra-
zacham "gritias agamus";
gratiosus: ea favear, popalaire, influent; quelquefois "obligeant,
complaisant".
5 0 grdtor,-Sris (arch. et podt.; la prose classique dit gratulor):
```


## [2026-09-06T14:59:25.066Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"grace,\\|gracious,\" KLN_1966.txt | head -5"
}
```


### [2026-09-06T14:59:25.117Z] TOOL RESULT

```
2150:Aleochara,  n.,  a  genus  of  rove  beetles  ( entomol .) —  ModL.,  compounded  of  Gk.  aXso;,  a  col¬ lateral  form  of  rjXeiSi;,  ‘wandering  in  mind,  dis¬ traught,  foolish’,  and  yaps.,  ‘joy’.  The  first  ele¬ ment  is  rel.  to  aXaoSai,  ‘to  wander,  roam’;  see hallucinate  and  cp.  Alastor,  aleatory.  The  second element  is  rel.  to  yaipew,  ‘to  rejoice’,  yapiq, ‘grace,  kindness’;  see  Charis. aleph,  n.,  name  of  the  1st  letter  of  the  Heb.  al¬ phabet.  —  Heb.  aleph,  pausal  form  of  eleph,  ‘ox’ ; so  called  in  allusion  to  the  ancient  Hebrew  form of  this  letter,  representing  the  head  of  an  ox.  Cp. alpha.  For  the  form  cp.  daleth,  lamedh,  samekh. alepidote,  adj.,  without  scales  ( zool .)  —  Gk. aXeTuSwxo?,  fr.  a-  (see  priv.  pref.  a-)  and XetuSwtoc,  ‘covered  with  scales’,  fr.  Xerct?,  gen. XetuSo?,  ‘scale’.  See  lepido-,  leper.
2837:Ann,  Anna,  Anne,  fern.  PN.  —  L.  Anna,  fr.  Gk. "Awa,  fr.  Heb.  Hann6h,  lit.  ‘grace’,  from  the base  of  hanan,  ‘he  was  gracious,  showed  favor’. See  Hannah.
7220:charism,  n.,  a  divine  favor  or  gift.  —  Gk.  xapi<t(j.a, ‘grace,  favor,  gift’,  fr.  xap(?ecr^at>  ‘to  show favor’,  fr.  x«PlC-  See  prec.  word  and  -ism. Charissa,  fern.  PN.  —  MGk.,  fr.  Gk.  ydpLp, ‘grace’.  See  Charis.
8726:congratulate,  tr.  v.  —  Fr.  L.  congratulate,  pp.  of congratulari ,  ‘to  wish  joy  warmly,  congratulate’, fr.  con-  and  gratulari,  ‘to  wish  joy’,  fr.  gratus, ‘pleasing’.  See  grace,  n.,  and  cp.  grateful. Derivatives:  congratulation  (q.v.),  congratulat- or,  n.,  congratulat-ory,  adj. congratulation,  n.  —  F.,  fr.  L.  congratulalionem, acc.  of  congratuladd,  fr.  congratulatus,  pp.  of congratulari.  See  prec.  word  and  -ion. congregant,  n.,  a  member  of  a  congregation.  — L.  congregdns,  gen.  -antis,  pres.  part,  of  congre- gdre.  See  next  word  and  -ant. congregate,  adj.,  assembled.  —  L.  congregdtus, ‘flocking  together’,  pp.  of  congregate,  ‘to  flock together’,  fr.  con-  and  gregare,  ‘to  gather  into a  flock’,  from  grex,  gen.  gregis,  ‘flock’.  See  gre¬ garious  and  adj.  suff.  -ate. congregate,  tr.  and  intr.  v.,  to  gather  into  a  crowd ; to  assemble.  —  L.  congregdtus ,  pp,  of  congre- gdre.  See  prec.  word.
9024:contumely,  n.,  contemptuous  insolence.  —  OF. contumelie,  fr.  L.  con  umelia,  ‘insult,  affront, disgrace,  ignominy',  from  the  adj.  *contumelis, ‘haughty,  insolent’,  which  is  rel.  to  contumax, ‘haughty,  insolent’.  See  contumacy, contund,  tr.  v.,  to  contuse.  —  L.  contundere,  ‘to beat,  bruise’.  See  next  word, contuse,  tr.  v.,  to  bruise.  —  L.  contusus,  pp.  of contundere,  ‘to  beat,  bruise’,  fr.  con-  and  tundere, ‘to  beat,  strike,  stump’.  See  fund, contusion,  n.,  a  bruise.  —  F.,  fr.  L.  contusidnem, acc.  of  contusio,  'a  crushing,  bruising’,  fr.  con-
```


## [2026-09-06T14:59:31.741Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -o -E \"grace,? ?n\\.[^|]{0,400}\" KLN_1966.txt | head -3; echo \"---agree---\"; grep -n -o -E \"agree,  ?(intr|tr)[^|]{0,350}\" KLN_1966.txt | head -3"
}
```


### [2026-09-06T14:59:33.704Z] TOOL RESULT

```
16503:grace,n. Grace,  fern.  PN.  —  Lit.  ‘favor,  grace’,  fr.  L. gratia.  See  grace,  n.
16612:grace, n.,  and  tolerate  and  cp.  congratulate.  Cp.  also L.  opitulor,  ‘I  help,  aid,  assist’,  lit.  ‘I  bring  help’, fr.  ops,  gen.  opis,  ‘help,  assistance’,  and  tulo  — fero,  ‘I  bring’.  —  For  the  contraction  of  *grati- tulor  into  grdtulor  see  haplology. gratulation,  n.,  congratulation.  —  L.  gratulatio, gen.  -onis,  ‘manifestation  of  joy,  congratula¬ tion’.  fr.  gratu
23166:grace, n.,  and  cp.  malgre.
---agree---
2004:agree,  intr.  v.  —  ME.  agreen,  fr.  OF.  agreer  (F. agreer ),  ‘to  receive  with  favor’,  fr.  a  (F.  a),  ‘to’ (see  a),  and  gre  (F.  gre),  ‘will,  pleasure’,  fr.  L. gratum,  neut.  of  the  adjective  grams,  ‘acceptable, pleasing,  agreeable,  grateful’,  used  as  a  noun.  See grateful  and  cp.  the  second  element  in  maugre. Derivative
11570:agree,  intr.  v.  —  F.  desagreer,  fr.  des-  (fr.  L. dis-)  and  agreer.  See  dis-  and  agree. Derivatives :  disagreeable  (q.v.),  disagree-ment ,  n. disagreeable,  adj.  —  F.  desagreable,  fr.  des-  (fr. L.  dis-)  and  agreable.  See  dis-  and  agreeable. Derivatives:  disagreeabl-y,  adv.,  disagreeable¬ ness,  n.
```


## [2026-09-06T14:59:39.803Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"garodman\\|garotman\\|garōdmān\\|gr'mk\\|gramik\\|grāmīk\" NYB_vol2_glossary.txt | head -10"
}
```


### [2026-09-06T14:59:39.861Z] TOOL RESULT

```
1123:cigon [cygwn] adv. and conj. A. interrog. adv. how? 1. direct interrogation: nun ~ kunom ?] 272; asmān ~? 921; exclama- tory: how...! 614. — 2. indirect inter- rogation: äkäh hom ku ~ hän 571; vēnēt ki Bastvar kārēcār ~ nev kunēt saw how valiantly B. fought 2815-16; ~ 6, 6 ham pursem 57°, andar Garodman dätistän ~, api-m nē dit 527-3; ete. — B. rel. adv. so as: l. har 3 šap x"amn ~ dit Estät ... guft such as he had seen it 2%; 215, 48, 520, 4527, ete.; introducing quotations: ~ den göbet 387, ~... paitāk ku 4571-5, etc. passim; parenthetic, e.g. 7718, 818%; — with a demonstr. antecedent: hamgönak hast ~-am guft 1216-17; šmāh bat ētūn m to gobeh 2329; 4524-25, 782.4, etc. — 2. with- out a clause, used prepositionally: as, as (for instance), as it were, like: ~ agäh aköc martom 2678-27; ~~ martom kë šarm 43913; 12813; varcāvandān i ~ Yam u Frétón ... 45°; hàn 4 ~ én such a th. 438; namely 1078; — with a demonstr. antecedent: &ön ~ āluh-ē 9%; eton ~ to 1516; ét6n but ~ amahraspand-ē 38°”; — čton, or ógón, homänäk (a. v.) ~ 69%, ete.; mänäk(k)äi (g. v.) i õi ~ ke pus... bare (opt.) 418. — C. conj. 1. causal be- cause: ~~... hdn mazantom bit 613-4; 1081. 11812; almost as a rel. pron. with a sec- ondary causal sense (as in Lat. quippe qui): 6 xuähar i x*"e$, ~ zan 4 Artaxsér būt, nämak nipišt 822; 718%, 7916. 116%. 11819; — hac han ~ in view of the fact that, considering that 38. — 2. temporal as soon as: 6°. 15°. 44°, more emphatically ham-~ 1317. - 3. ~ ka as if 11214.17, 10120722 — 4. almost = that 8722. — MPrth cw'gwn; MPrs ewn (read ci'on < *ciwön <
```


## [2026-09-06T14:59:53.419Z] TOOL CALL #60: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%DA%AF%D8%B1%DB%8C%D8%B3%D8%AA%D9%86' --note 'page 209, root Gwer 2: Persian geristan \"to weep\" — Wiktionary derives it from MP griyistan, Cheung *garz, not from gar- \"praise\"' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/g%CA%B7erH-' --note 'page 209, ROOT Gwer 2 / Gwere 1: PIE *gwerH- \"to express approval, praise\"' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%DA%AF%D8%B1%D8%A7%D9%85%DB%8C' --note 'page 209, node 4: Persian gerami < MP gramig' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://www.etymonline.com/word/grace' --note 'page 209, nodes 5-6: Latin gratia/gratus > OFr grace > English grace, PIE *gwere- \"to favor\"' 2>&1 | tail -3",
 "description": "Archive web sources"
}
```


### [2026-09-06T14:59:56.365Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/768f5d9d98e6b116.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/934d5ae63b36c5f3.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b56c154753335e0b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e1a958671059882a.txt
```


## [2026-09-06T15:00:11.535Z] TOOL CALL #61: Bash

```json
{
 "command": "pdftoppm -f 209 -l 209 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg209 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/",
 "description": "Render PDF page 209"
}
```


### [2026-09-06T15:00:13.940Z] TOOL RESULT

```
total 676
drwx------ 2 sfmqrb sfmqrb   4096 Sep  6 11:00 .
drwx------ 4 sfmqrb sfmqrb   4096 Sep  6 10:51 ..
-rw-rw-r-- 1 sfmqrb sfmqrb    264 Sep  6 10:53 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  92182 Sep  6 10:55 bqt1854.png
-rw-rw-r-- 1 sfmqrb sfmqrb  66580 Sep  6 10:57 bqt2023.png
-rw-rw-r-- 1 sfmqrb sfmqrb  54688 Sep  6 10:58 pg201.png
-rw-rw-r-- 1 sfmqrb sfmqrb  70083 Sep  6 10:52 pg204.png
-rw-rw-r-- 1 sfmqrb sfmqrb  77858 Sep  6 10:52 pg206.png
-rw-rw-r-- 1 sfmqrb sfmqrb  67371 Sep  6 10:53 pg207.png
-rw-rw-r-- 1 sfmqrb sfmqrb  59146 Sep  6 10:53 pg208.png
-rw-rw-r-- 1 sfmqrb sfmqrb  53054 Sep  6 11:00 pg209.png
-rw-rw-r-- 1 sfmqrb sfmqrb 117034 Sep  6 10:54 pg215.png
```


## [2026-09-06T15:00:16.887Z] TOOL CALL #62: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg209.png"
}
```


### [2026-09-06T15:00:17.268Z] TOOL RESULT

```

```


## [2026-09-06T15:00:17.252Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-06T15:00:27.402Z] TOOL CALL #63: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/gratus",
 "prompt": "Latin gratus: give the etymology (PIE root, Proto-Italic form), meaning, and derived terms including gratia, gratis, gratuitus."
}
```


### [2026-09-06T15:00:34.076Z] TOOL RESULT

```
# Latin *gratus*: Etymology and Derivatives

**Etymology:**
The word derives from Proto-Italic *gʷrātos*, which traces back to Proto-Indo-European *gʷr̥Htó-s*, stemming from the PIE root *gʷerH- meaning "to welcome, greet, praise."

**Meaning:**
The adjective carries three primary senses: "pleasing, acceptable, agreeable, welcome"; "dear, beloved"; and "grateful, thankful."

**Derived Terms:**
Notable descendants include *grātia* (grace), *grātis* (for free), *grātitūdō* (gratitude), *grātor* (one who pleases), and *pergrātus* (very pleasing). Related forms include *grātiōsus* (gracious) and *grātulor* (to congratulate).

**Cognates:**
Sanskrit *gṛṇā́ti* (praise) and Old Church Slavonic *žrĭti* share this Indo-European heritage, illustrating the root's ancient distribution across language families.
```


## [2026-09-06T15:00:40.092Z] TOOL CALL #64: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/gratus' --note 'page 209, node 5: Latin gratus < PIt *gwratos < PIE *gwrHto-, root *gwerH- \"to welcome, praise\"; derivatives gratia, gratis, gratitudo' 2>&1 | tail -2; mkdir -p data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg209.png data/verification/sources/refs/ocr/BOOK/209.png && echo copied",
 "description": "Archive gratus page and copy book page image"
}
```


### [2026-09-06T15:00:42.056Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/94fb767e1161a861.txt
copied
```


## [2026-09-06T15:01:02.488Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT && cat >> 1803.vision.txt <<'EOF'\n\n[2026-09-06 addition, read from 1803.png by a vision model for pdf page 209 (root Gwer 2):\n the FIRST headwords of the right-hand column of printed p. 1803, above گروه, were\n omitted from the earlier transcription. Verbatim:]\n\n  گرگری ۱ ـ ... فارسی بروزن خروشان، آلت تناسل را گویند ۱ ـ\n      و بکسر اول و فتح ثانی، گرو کردنی را یعنی مرهون ـ و بمعنی بنده و عبد هم بنظر آمده است ۲ .\n\n  گروگر ۳ ـ بفتح اول و کاف فارسی بروزن کبوتر، یکی از نامهای خدای تعالی است\n      و معنی آن مرادبخش باشد .\n\nMo'in's footnote ۳ (bottom of the page), verbatim:\n\n  ۳ ـ = گرکر ، ظ . از : gar (garo) (پرستیدن) [قس: گرزمان] در صد و یک نام خدا\n      از دعاهای زرتشتیان، نام ۷۳ «گرکر» و نام ۷۴ «گروگر» آمده . رك : خرده اوستا .\n      شهرمردان . بمبئی ۱۳۰۸ ص ۳ .\n          فرزند تو امروز بود جاهل و عاصی      فردات چه فریاد رسد پیش گروگر .\n      « ناصرخسرو بلخی . دیوان ص ۱۷۳ » .\n\n[This is the page Nourai cites in BQT:1793-1806 for garogar «گروگر» \"God\"; the same\n Naser-Khosrow couplet is the one quoted in the chart. Mo'in glosses گروگر as\n \"one of the names of God Most High\", meaning مرادبخش (\"granter of wishes\"),\n apparently from Av./MP gar-, garō- \"to worship, praise\", cf. گرزمان; nos. 73/74 of\n the 101 names of God in the Zoroastrian prayers (Khordeh Avesta, Shahmardan,\n Bombay 1308, p. 3).]\nEOF\necho done; tail -5 1803.vision.txt",
 "description": "Append gorugar transcription to BQT 1803 vision file"
}
```


### [2026-09-06T15:01:04.230Z] TOOL RESULT

```
done
 Naser-Khosrow couplet is the one quoted in the chart. Mo'in glosses گروگر as
 "one of the names of God Most High", meaning مرادبخش ("granter of wishes"),
 apparently from Av./MP gar-, garō- "to worship, praise", cf. گرزمان; nos. 73/74 of
 the 101 names of God in the Zoroastrian prayers (Khordeh Avesta, Shahmardan,
 Bombay 1308, p. 3).]
```


## [2026-09-06T15:01:06.841Z] TOOL CALL #66: Bash

```json
{
 "command": "sed -n '1,120p' tools/verify_check.py"
}
```


### [2026-09-06T15:01:06.886Z] TOOL RESULT

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


## [2026-09-06T15:06:04.378Z] TOOL CALL #67: Bash

```json
{
 "command": "cat > /home/sfmqrb/git/rishe/data/verification/page-209.json <<'JSONEOF'\n{\n  \"pdf_page\": 209,\n  \"book_page\": 179,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-06\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Gwer 2, Gwere 1\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *gʷerH- (Pokorny gʷer(ə)-, no. 4) 'to raise the voice, praise, welcome; also to scold, lament'\",\n      \"note\": \"Pokorny IEW 478 has exactly '4. gʷer(ə)- \\\"die Stimme erheben\\\", bes. \\\"loben, preisen, willkommen heißen\\\", aber auch \\\"schelten; jammern\\\"; gʷr̥-to-s \\\"willkommen\\\"', with Skt. gṛṇā́ti 'sings, praises', Av. gar-, garō 'praise, song of praise', Skt. gūrtí- = Lat. grātēs, Skt. gūrtá- = Lat. grātus, Lith. gìrti. Watkins/AHD lists the same root as gʷerə-3 'to praise (aloud)' with the cross-reference '[Pok. 4. gʷer(ə)- 478]'. Wiktionary reconstructs it as *gʷerH- 'to express approval; praise'. Nourai's label (Indo-European), his gloss 'to praise, welcome, sing' and his POK:478 citation are therefore all correct; 'Gwer 2 / Gwere 1' is Nourai's own numbering, not Pokorny's (Pokorny's gʷer-2 is 'heavy' and his gʷer-1 'devour', both on pp. 474-477, so the numbers must not be read as Pokorny's). Note that Pokorny's own gloss already covers the 'scold/lament' side, which is what Nourai leans on for gerîstan and payğâreh.\",\n      \"note_fa\": \"ریشهٔ بازسازی‌شدهٔ هندواروپایی آغازین *gʷerH- «آواز برداشتن، ستودن، خوشامد گفتن؛ و نیز نکوهیدن و مویه کردن» است؛ پوکورنی در ص ۴۷۸ فرهنگ ریشه‌شناختی هندواروپایی خود دقیقاً همین ریشه را با شمارهٔ ۴ آورده و سنسکریت gṛṇā́ti «می‌سراید، می‌ستاید»، اوستایی gar-، garō «ستایش، سرودِ ستایش» و لاتینی grātus / grātēs را ذیل آن جای داده است. واتکینز در پیوست ریشه‌های هندواروپایی فرهنگ American Heritage همین ریشه را gʷerə-³ «ستودن (با صدای بلند)» می‌نامد و به «پوکورنی ۴۷۸» ارجاع می‌دهد. بنابراین نام ریشه، برچسب زبانی و معنای آن در نمودار نورایی درست است؛ تنها باید توجه داشت که شماره‌گذاری «Gwer 2 / Gwere 1» از خودِ نورایی است نه از پوکورنی.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/g%CA%B7erH-\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:478\", \"status\": \"supports\", \"note\": \"POK_02.txt leaf 135-136 (= printed p. 478): '4. gʷer(ə)- \\\"die Stimme erheben\\\", bes. \\\"loben, preisen, willkommen heißen\\\", aber auch \\\"schelten; jammern\\\"; gʷr̥-to-s \\\"willkommen\\\". Ai. gṛṇā́ti … av. gar-, aibi-gərənte \\\"preisen, lobend einstimmen\\\", garō Gen. f. \\\"Lob, Preis; Loblied\\\" … ai. gūrtá-ḥ \\\"willkommen\\\" = lat. grātus'. Nourai's page number is exact.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"POK\", \"where\": \"Band I p. 478 (POK_02.txt, form-feed leaf 135/136)\", \"stance\": \"supports\", \"note\": \"'4. gʷer(ə)- … loben, preisen, willkommen heißen … aber auch schelten; jammern' — root, gloss and the Avestan/Latin members are all as drawn.\"},\n        {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Band I p. 686 (incoming/WLD/WLD_Bd1_pages.txt, line 64983; the printed '686' stands 63 lines above)\", \"stance\": \"supports\", \"note\": \"'4. gʷer(ə)- \\\"die Stimme erheben\\\", bes. \\\"loben, preisen, willkommen heißen\\\", aber auch \\\"schelten: jammern\\\"' — WP I 686 is the source Pokorny 478 condenses; same Avestan gar-, aibi-gərənte, garō, garah- and Lat. grātēs/grātus.\"},\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. gʷerə-3 (AHD_watkins1985.txt line 542)\", \"stance\": \"supports\", \"note\": \"'gʷerə-3. To praise (aloud). 1. Suffixed zero-grade form *gʷrə-to- in Latin grātus … GRACE, GRATEFUL, GRATIFY, GRATIS, GRATITUDE, GRATUITY; AGREE, CONGRATULATE, INGRATE, INGRATIATE. 2. … Celtic bardo- … BARD. [Pok. 4. gʷer(ə)- 478.]'\"},\n        {\"src\": \"IEC\", \"where\": \"Mann, cols./pp. 373 and 375 (IEC.txt leaf 217, 218)\", \"stance\": \"supports\", \"note\": \"'gur- (3) \\\"appellation, song, praise; revere, sacrifice, worship\\\" … Skt. giráḥ, gir \\\"praise\\\"; Lat. au-gur … Li. giriù, ti \\\"praise\\\"' and 'gurió \\\"sing, praise\\\" … Skt. gṛṇā́mi \\\"sing, praise, announce\\\"'. Mann writes the labiovelar 'gu', so his gur- (3) = Pokorny's gʷer(ə)-.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"gar 2, gard, grad, grd, grnâti; garo-gar; garô-demâna; paiti-gar\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Bartholomae's Altiranisches Wörterbuch (col. 512-513) does have exactly 'j. ²gar- V. \\\"preisen\\\", nur mit Praev.', pres. stem gərən-, passive gairya-, attested with aibi- (aibi-gərənte 'they praise'), avi- and ā-, and equates it with Skt. gṛṇā́ti, abhigirya; so Nourai's 'gar 2' reproduces Bartholomae's own numbering and is correct, and the gloss 'to call, pray' is a fair rendering of 'preisen, lobend einstimmen'. The other citation forms in the box are of mixed status. 'grnâti' is not Avestan at all: it is Sanskrit gṛṇā́ti, cited as 'ai. gṛṇā́ti' by both Pokorny 478 and Bartholomae — Nourai has slipped the Indic cognate into the Avestan box. 'grd' is the zero grade gərəd-/gr̥d-, and 'gard' matches Bartholomae's garəd- 'gradi' (a homonym belonging to Lat. gradior, not to this root) or else Pokorny's dh-extension gʷerədh- (Arm. kardam 'I raise my voice', Lith. gerdas 'shout'); 'grad' is the Proto-Iranian *grad- 'to weep' that Cheung (2007: 112) sets up for MP griy-, i.e. Nourai has already collapsed two roots here. 'garô-demâna' is fully attested: Bartholomae s.v. ⁵gar- f. 'Lob, Preis; Loblied', gen. sg. garō with dəmāna-/nmāna- 'Haus des Lobs', the abode of Ahura Mazdā and the blessed, 'sva. Paradies' (Y 45.8, 50.4, 51.15; Yt 10.32 etc.); Nourai's rendering 'house of prayer, sky' is loose but not wrong, since the Pahlavi and New Persian continuations mean 'highest heaven'. 'paiti-gar' is NOT an attested Avestan compound — Bartholomae records ²gar- only with aibi-, avi- and ā-; the form is Horn's reconstruction (Grundriss no. 358, p. 80: 'peiγāre \\\"Tadel\\\". aw. *paiti + 2√gar-'), and Horn marks it with an asterisk. 'garo-gar' is likewise not Avestan: it is a Zoroastrian Middle-Persian/New-Persian divine name (nos. 73-74 of the 101 names of God in the Khordeh Avesta prayer lists), which Mo'in in his note to Borhan-e Qate' p. 1803 derives 'ẓ. az gar (garō) parastidan' — 'apparently from gar/garō \\\"to worship\\\"'. So the root attachment of every item is defensible, but the language label 'Avestan' is right only for gar- 2 and garō.dəmāna-.\",\n          \"derivation_fa\": \"بارتولومه در «فرهنگ ایرانی باستان» (ستون ۵۱۲–۵۱۳) ستاک اوستایی ²gar- «ستودن» را با همان شمارهٔ ۲ ثبت کرده است — تنها با پیشوند به کار می‌رود: aibi-gərənte «می‌ستایند»، و آن را هم‌ریشه با سنسکریت gṛṇā́ti می‌داند؛ پس «gar 2» و معنای «خواندن، نیایش کردن» درست است. اما دیگر صورت‌های این جعبه یکدست نیستند: grnâti اصلاً اوستایی نیست، بلکه سنسکریت gṛṇā́ti است که هم پوکورنی و هم بارتولومه آن را با نشان «ai.» می‌آورند و نورایی آن را به خطا در جعبهٔ اوستایی گذاشته است؛ grad همان ستاک ایرانی باستان *grad- «گریستن» است که چونگ (۲۰۰۷، ص ۱۱۲) آن را ذیل ریشهٔ دیگری (*garz) می‌گذارد. در مقابل garō.dəmāna- «خانهٔ ستایش» کاملاً مستند است و بارتولومه آن را جایگاه اهورامزدا و پاکان، یعنی بهشت، می‌داند. paiti-gar در اوستا گواهی نشده و صورتی است بازسازی‌شده (با ستارهٔ فرضی) که هرن در بند ۳۵۸ «مبانی ریشه‌شناسی فارسی نو» (ص ۸۰) برای «پیغاره» پیشنهاد کرده است، و garogar نیز واژه‌ای اوستایی نیست بلکه نامی از نام‌های خداوند در دعاهای زردشتی فارسی/پهلوی است که معین در حاشیهٔ برهان قاطع (ص ۱۸۰۳) آن را «ظاهراً از gar (garō) پرستیدن» می‌داند. بنابراین پیوند ریشه‌ای پذیرفتنی است، ولی برچسب «اوستایی» تنها برای gar- ۲ و garō.dəmāna- درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/g%CA%B7erH-\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:478\", \"status\": \"partial\", \"note\": \"POK_02.txt leaf 135-136 (printed p. 478) supports the Avestan material it actually lists — 'av. gar-, aibi-gərənte \\\"preisen, lobend einstimmen\\\", garō Gen. f. \\\"Lob, Preis; Loblied\\\" (= ai. girā́ḥ), garah- n. \\\"Lob, Preislied\\\"' — and it explicitly labels gṛṇā́ti 'ai.' (Sanskrit), not Avestan. Pokorny has neither garō-gar nor paiti-gar.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"Bartholomae, Altiranisches Wörterbuch cols. 512-513 (BRT.txt lines ~10240-10260)\", \"stance\": \"partial\", \"note\": \"'j. ²gar- V. \\\"preisen\\\", nur mit Praev. Praes. gərən-, gairya- (Pass.) … mit aibi 1) \\\"preisen\\\": aēsa aibi-gərənte Y. 70.1 … ai. gṛṇā́ti, abhigirya' — confirms gar- 2 and its glosses; and 'g.j. ⁵gar- f. \\\"Lob, Preis; Loblied\\\"; GS. garō mit g. dəmāna-, j. nmāna- n. \\\"Haus des Lobs\\\" als Bezeichnung für den Aufenthalt Mazdāhs und der Seligen, sva. Paradies' — confirms garō.dəmāna-. Bartholomae lists NO paiti-gar and no garō-gar; his garəd- is a separate verb 'gradi' (Lat. gradior).\"},\n            {\"src\": \"POK\", \"where\": \"Band I p. 478\", \"stance\": \"partial\", \"note\": \"Avestan members given are gar-, aibi-gərənte, garō, garah-, aibi-jarətay-, aibi-jarətar-, ā-gra- — gṛṇā́ti is marked 'ai.'; no paiti- or garō-gar compound.\"},\n            {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 358, printed p. 80 (HRN.txt leaf 102)\", \"stance\": \"supports\", \"note\": \"'358. peiγāre \\\"Tadel\\\" … aw. *paiti + 2√gar- (ai. prati + gar- bedeutet auch nur \\\"anrufen, begrüssen, antworten\\\"). Spiegel, Ar. Periode, 229. Bartholomae meint, man könne auch an Ableitung von ai. prati + √har- denken' — Horn is the actual source of Nourai's paiti-gar, and he asterisks it as a reconstruction, with Bartholomae dissenting.\"},\n            {\"src\": \"BQT\", \"where\": \"Borhan-e Qate', ed. Mo'in, printed p. 1803, footnote 3 (image data/verification/sources/refs/ocr/BQT/1803.png; transcription 1803.vision.txt)\", \"stance\": \"partial\", \"note\": \"'گروگر ۳ ـ … یکی از نامهای خدای تعالی است و معنی آن مرادبخش باشد' with Mo'in's note '= گرکر ، ظ . از : gar (garo) (پرستیدن) [قس: گرزمان] در صد و یک نام خدا از دعاهای زرتشتیان، نام ۷۳ «گرکر» و نام ۷۴ «گروگر» آمده' — the derivation from gar-/garō- is Mo'in's, but the word is a Zoroastrian Persian divine name, not an Avestan compound.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"Cheung 2007 s.v. *garz 'to lament, weep' (CHEUNG.txt lines 8100-8135)\", \"stance\": \"contradicts\", \"note\": \"Puts the 'grad' member elsewhere: 'MMP gry-, BMP gl(y)dy- /griy-/ \\\"to weep\\\" (< OP *grad-ya-)' under Av. gərəz- 'to lament, weep', with 'Pok.: 350 f.' — i.e. *grad- does not belong to gʷer(ə)- 'praise'.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"gerîstan «گریستن»; garogar «گروگر»; garzmân «گرزمان»; payğâreh «پیغاره ، بیغاره»\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Three of the four words hold up; the first, which is the one that carries the chart, does not, on the modern view. (1) گرزمان garzmān 'sky, empyrean' is certain: Av. garō.dəmāna- / garō.nmāna- 'House of Praise' > MP garōdmān (MacKenzie: 'garōdmān [glwtm'n' = Av. garō dmānam | M grdm'n] paradise', with the by-form garasmān), whence NP garōdmān > garzmān by loss of the intervocalic -d- and syncope; Horn no. 906a (p. 202) states this in so many words, and Armenian borrowed the same word as gerezman 'grave'. Mo'in glosses گرزمان 'عرش خدا، علیین، (توسعاً) آسمان، سپهر', so Nourai's gloss 'sky' is Mo'in's extended sense. (2) گروگر garōgar 'God' is name no. 74 of the 101 names of God in the Zoroastrian prayer lists (Khordeh Avesta), glossed by Mo'in 'یکی از نامهای خدای تعالی … و معنی آن مرادبخش باشد' ('a name of God Most High, meaning \\\"granter of wishes\\\"') — Nourai's 'fulfiller of prayers' is that gloss — and Mo'in derives it from gar/garō 'to worship', comparing گرزمان. Nourai's Naser-Khosrow couplet (فرزند تو امروز بود جاهل و عاصی / فردات چه فریاد رسد پیش گروگر) is the very shāhed Mo'in prints in that footnote. (3) پیغاره/بیغاره payğāre 'reproach, taunt' is derived from *paiti-gar- by Horn no. 358 (p. 80), i.e. 'to speak back at, answer against' > 'to reproach' — the semantics parallel Skt. prati + gṝ 'to answer'; Bartholomae, however, told Horn he preferred *prati + har- (cf. Lat. obicere), and Mo'in's Farhang lists پیغار beside پیکار, so this one is Horn's, defensible but not unanimous. (4) گریستن gerīstan 'to weep' is where modern scholarship parts company with Nourai. Horn no. 915 (p. 204) — the page Nourai cites — does derive it from 'aw. √gar-, gərənte \\\"anrufen\\\"' with MP grīstan, and that is exactly Nourai's arrow. But Cheung's Etymological Dictionary of the Iranian Verb (2007: 112) files MMP gry- / BMP /griy-/ 'to weep' under Proto-Iranian *garz 'to lament, weep' (Av. gərəz-, OAv. gərəzōi, YAv. gərəzaite), from OP *grad-ya-, together with NP گله gilah 'complaint' and Oss. qærzyn 'to groan'; Wiktionary follows Cheung and MacKenzie (griyistan, griy-) for گریستن and does not connect it with gar- 'to praise'. Because a node takes the worst verdict of its words, the node is disputed.\",\n          \"derivation_fa\": \"از چهار واژهٔ این جعبه سه‌تا پذیرفتنی است و یکی، که بار اصلی نمودار بر دوش اوست، نیست. «گرزمان» بی‌گمان از اوستایی garō.dəmāna- «خانهٔ ستایش» است که در فارسی میانه garōdmān شده (مکنزی: garōdmān = Av. garō dmānam «بهشت»، با گونهٔ garasmān) و با افتادن دالِ میان‌واکه‌ای و کاهش هجا به «گرزمان» رسیده است؛ هرن در بند ۹۰۶الف (ص ۲۰۲) دقیقاً همین را می‌گوید و یادآور می‌شود که ارمنی gerezman «گور» نیز وام‌واژهٔ همین است. معین «گرزمان» را «عرش خدا، علیین، (توسعاً) آسمان، سپهر» معنی کرده، پس معنای «آسمان» در نمودار همان معنای گستردهٔ معین است. «گروگر» نام هفتادوچهارم از صد و یک نام خداوند در دعاهای زردشتی است و معین آن را «یکی از نامهای خدای تعالی … و معنی آن مرادبخش باشد» می‌داند و از gar/garō «پرستیدن» می‌گیرد؛ بیتِ ناصرخسروِ نمودار همان شاهدی است که معین در حاشیهٔ ص ۱۸۰۳ برهان قاطع آورده است. «پیغاره/بیغاره» را هرن در بند ۳۵۸ (ص ۸۰) از *paiti-gar- «در برابر کسی سخن گفتن، پاسخ دادن» می‌گیرد (قس سنسکریت prati + gṝ «پاسخ دادن»)، هرچند بارتولومه در نامه‌ای به هرن *prati + har- را ترجیح داده است. اما «گریستن» را پژوهش امروزی رد می‌کند: هرن (بند ۹۱۵، ص ۲۰۴) آن را از همان √gar- «خواندن» می‌گرفت و نورایی از او پیروی کرده، ولی چونگ در «فرهنگ ریشه‌شناختی فعل ایرانی» (۲۰۰۷، ص ۱۱۲) صورت‌های فارسی میانهٔ griy- را ذیل ریشهٔ ایرانی *garz «مویه کردن، گریستن» (اوستایی gərəz-) و از پارسی باستان *grad-ya- می‌آورد، همراه با «گله» و آسی qærzyn؛ ویکی‌واژه نیز همین را پذیرفته است. چون داوری هر گره برابر بدترین داوری واژه‌های آن است، این گره «رد شده» شمرده می‌شود.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%DA%AF%D8%B1%DB%8C%D8%B3%D8%AA%D9%86\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"HRN:202\", \"status\": \"supports\", \"note\": \"HRN.txt leaf 223 = printed p. 202, no. 906a: 'gerzmān (falsch kerzman) \\\"Himmel\\\". aw. garō dəmāna-, garō nmāna- (Salemann, SF, pag. 99; dann auch Fr. Müller, WZKM. 5, 187, der arm. LW. gerezman \\\"Grab, Gruft, Friedhof\\\" dazu stellt).' Exactly Nourai's garzmân < garô-demâna arrow.\"},\n            {\"ref\": \"HRN:204\", \"status\": \"supports\", \"note\": \"HRN.txt leaf 225 = printed p. 204, no. 915: 'giristen, girīsten \\\"klagen, weinen\\\", Impt. girī, girye, giryīden. aw. √gar-, gərənte \\\"anrufen\\\"; phlv. grīstan \\\"weinen, klagen\\\" (AV.), g(i)ryīnīdan (AV.); ai. √gar-, gṛṇā́ti \\\"anrufen\\\".' Horn does say what Nourai's arrow says — but see the Cheung entry under 'consulted': this is the 1893 view, superseded.\"},\n            {\"ref\": \"BQT:1793-1806\", \"status\": \"supports\", \"note\": \"Printed p. 1803 (pdf 600 of BQT_v3_picofile.pdf; the tool's default offset is one page off in this region), right column: 'گروگر ۳ ـ بفتح اول و کاف فارسی بروزن کبوتر، یکی از نامهای خدای تعالی است و معنی آن مرادبخش باشد', footnote 3 '= گرکر ، ظ . از : gar (garo) (پرستیدن) [قس: گرزمان] … نام ۷۳ «گرکر» و نام ۷۴ «گروگر» … رك : خرده اوستا' followed by the same Naser-Khosrow couplet the chart quotes. Image + transcription saved as data/verification/sources/refs/ocr/BQT/1803.png / 1803.vision.txt.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"CHEUNG\", \"where\": \"Cheung 2007, *garz 'to lament, weep', p. 112 (CHEUNG.txt lines 8100-8135)\", \"stance\": \"contradicts\", \"note\": \"'*MIDDLE PERSIAN: MMP gry-, BMP gl(y)dy- /griy-/ \\\"to weep\\\" (< OP *grad-ya-) … *NWIR: NP giristan/giriy- \\\"to weep\\\", NP gilah \\\"complaint; lamentation\\\" … *AVESTAN: gərəz- \\\"to lament, weep\\\"'; Cheung's own reference list cites 'Horn 1893: 208, 204', i.e. he knows Horn's derivation and replaces it.\"},\n            {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary pp. 36-37 (PHD.txt line 382; PHD_mackenzie.txt lines 2460, 2475, 2585)\", \"stance\": \"supports\", \"note\": \"'garōdmān [glwtm'n' | = Av. garō dmānam | M grdm'n] paradise'; 'garasmān [glsm'n' | M gr's m'n] = garōdmān'; 'griyistan, griy- [BKYWN-stn' < A √bky; gld-stn' | M gryy-stn, N giristan, giry-] weep, cry' — confirms the Pahlavi links for garzmān and for the FORM of gerīstan (but MacKenzie gives no root).\"},\n            {\"src\": \"MON\", \"where\": \"Mo'in, Farhang-e Farsi s.vv. گرزمان, گرگر/گروگر, پیغار (MON_part2.txt lines 31356, 31539, 31797; MON_part1.txt line 27153)\", \"stance\": \"supports\", \"note\": \"'گرزمان: garōd…, garōθmān (اِ.) عرش خدا، علیین. (توسعاً) آسمان، سپهر'; 'گرگر: [= گروگر] (اِ.) خدای تعالی'; 'پیغار: pēγār [= پیغاره = بیغاره] (اِ.) سرزنش، طعنه' — every Persian word and gloss in Nourai's box is Mo'in's.\"},\n            {\"src\": \"HRN\", \"where\": \"Horn no. 358, printed p. 80 (HRN.txt leaf 102)\", \"stance\": \"supports\", \"note\": \"'peiγāre \\\"Tadel\\\" … aw. *paiti + 2√gar-' — the source of the payğâreh arrow, though Nourai cites pp. 202/204 rather than p. 80. Horn adds Bartholomae's alternative *prati + har-.\"},\n            {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien, index s.v. garzman (HUB.txt line 10453: 'garzman 92.')\", \"stance\": \"supports\", \"note\": \"Hübschmann treats garzmān on p. 92 of the Persische Studien, i.e. he accepts the word as an inherited Iranian form, not an Arabic or Turkic loan.\"},\n            {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' vol. 1, s.v. بیغاره (BQT_v1_pages.txt line 22574)\", \"stance\": \"supports\", \"note\": \"'بیغاره بر وزن گهواره، بمعنی بیغار است که سرزنش و طعنه باشد' — confirms the doublet پیغاره/بیغاره and the gloss 'blame' that Nourai gives, without an etymology of its own.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"gar-âmîk\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The Middle Persian word is real and well attested, though its correct citation form is grāmīg, not gar-āmīk: MacKenzie, Concise Pahlavi Dictionary p. 37, 'grāmīg [gl'myk' | M grmyg, N girāmī] treasured, dear', with the abstract grāmīgīh 'affection, respect' and the neighbouring noun grāmag [gl'mk' | M gr'mg] 'possessions, wealth'. Nourai's hyphenated 'gar-âmîk' is his own morphological analysis (gar- 'praise' + the adjectival suffix -āmīg), and it reflects the Pahlavi Book script spelling gl'myk' read with an anaptyctic vowel; nothing in the manuscripts writes gar-. Whether the word really belongs to gʷer(ə)- 'praise' is the open question: Mann (IEC 376, see node 4) puts Persian garāmī with Skt. gūrtá- 'celebrated, approved, agreeable' and Lat. grātus under *gʷr̥tos 'revered, favoured', which would make Nourai right; but the -m- of grām(ag)/grāmīg is not accounted for on that route, and MacKenzie and Wiktionary give no pre-Middle-Persian etymology at all, deriving girāmī simply from grāmīg. Hence plausible, not confirmed. The edge Avestan gar- 2 → Pahlavi grāmīg is therefore an inference rather than a documented chain.\",\n          \"derivation_fa\": \"این واژهٔ فارسی میانه واقعی و پرکاربرد است، اما صورت درست آن grāmīg است نه gar-āmīk: مکنزی در «فرهنگ کوچک پهلوی» (ص ۳۷) می‌آورد «grāmīg [gl'myk' | مانوی grmyg، فارسی نو girāmī] گرامی، عزیز»، در کنار grāmīgīh «حرمت، دوستی» و grāmag «دارایی، مال». صورتِ خط‌تیره‌دار «gar-âmîk» تحلیل خودِ نورایی است (gar- «ستودن» + پسوند صفت‌ساز -āmīg) و در دست‌نویس‌های پهلوی چنین چیزی نوشته نشده است. اینکه این واژه به‌راستی از ریشهٔ *gʷerH- «ستودن» باشد پرسشی گشوده است: مان (فرهنگ تطبیقی هندواروپایی، ص ۳۷۶) «گرامی» فارسی را در کنار سنسکریت gūrtá- و لاتینی grātus ذیل *gʷr̥tos جای می‌دهد که همان ادعای نورایی است، ولی «م» در grām/grāmīg با این راه توضیح داده نمی‌شود و مکنزی و ویکی‌واژه هیچ ریشهٔ کهن‌تری برای آن نمی‌دهند. پس ادعای نورایی «با احتیاط پذیرفتنی است».\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%DA%AF%D8%B1%D8%A7%D9%85%DB%8C\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"MON:3214\", \"status\": \"not_checked\", \"note\": \"Mo'in's 6-volume Farhang-e Farsi vol. 3 p. 3214 is not online with its pagination; only the 2-volume Adena abridgement (MON_part2.txt) is available, where s.v. گرامی the entry reads 'گرامی: (ص.) عزیز، محترم. ضح. — در نظم و نثر فصیح همه جا گرامی (= گرامیک، په.) آمده' — i.e. Mo'in does give the Pahlavi antecedent grāmīg, which is the substance of the cited page, but the page number itself could not be verified.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie 1971 p. 37 (PHD.txt line 382)\", \"stance\": \"partial\", \"note\": \"'grāmag [gl'mk' | P gr'mg] possessions, wealth. grāmig [gl'myk' | M grmyg, N girāmī] treasured, dear. ~īh: affection, respect.' Confirms the word and its meaning; gives no Avestan or Indo-European root, and the neighbouring grāmag suggests a base grām- 'value'.\"},\n            {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II (NYB_vol2_glossary.txt)\", \"stance\": \"silent\", \"note\": \"Searched for grāmīk/gr'myk in the glossary; no headword found in the OCR (Nyberg's glossary covers only the texts of Part I, which do not use the word).\"},\n            {\"src\": \"IEC\", \"where\": \"Mann, An Indo-European Comparative Dictionary p. 376 (IEC.txt leaf 218)\", \"stance\": \"supports\", \"note\": \"'gurtos \\\"revered, favoured, important\\\" … Skt. gūrtáḥ \\\"celebrated, approved, agreeable\\\"; gūrtíḥ \\\"praise\\\"; Per. cf. garāmī, adj. \\\"revered, excellent\\\"; Lat. grātus \\\"welcomed, favoured\\\"' — Mann explicitly puts Persian garāmī in the same set as Lat. grātus, i.e. under the 'praise' root.\"},\n            {\"src\": \"BRT\", \"where\": \"Bartholomae, Altiranisches Wörterbuch (BRT.txt, greps for *grāma-, garāmi-)\", \"stance\": \"silent\", \"note\": \"No Avestan *garāmi-/grāma- exists; the Pahlavi word has no Avestan forerunner on record.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Persian\",\n          \"words\": \"gerâmî «گرامی»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"NP گرامی gerāmī 'dear, respected' continues Middle Persian grāmīg [gl'myk'], Manichaean MP grmyg, exactly as MacKenzie prints it ('N girāmī'); the change is the regular New Persian loss of final -g/-k after ī (MP -īg > NP -ī, as in MP tāzīg > NP tāzī, MP xwadāyīg > NP xodāyī), so the chain MP grāmīg > NP gerāmī is uncontroversial and is what Wiktionary gives. Mo'in adds that the fully attested classical form is گرامی and that the shortened گرام, used today under the influence of Arabic کرام, is not correct. Ferdowsi's line quoted in the chart (پذیره فرستاد خسرو سوار / گرانمایگان گرامی هزار) is a genuine Shahnameh attestation of the word in the sense 'honoured'. Mann's IEC 376 — one of the two references Nourai cites here — is the one book that supplies the deeper connection, listing 'Per. cf. garāmī, adj. \\\"revered, excellent\\\"' beside Skt. gūrtá- and Lat. grātus under *gʷr̥tos; that deeper step is the plausible part (see node 3), but the Pahlavi → Persian edge that this node actually draws is confirmed.\",\n          \"derivation_fa\": \"«گرامی» دنبالهٔ مستقیم فارسی میانهٔ grāmīg است (در نوشته‌های مانوی grmyg)؛ مکنزی خود صورت فارسی نو را در برابر آن آورده است. دگرگونی آوایی آن کاملاً قاعده‌مند است: پایانهٔ -īg فارسی میانه در فارسی نو به -ī بدل می‌شود (مانند tāzīg > تازی و xwadāyīg > خدایی). معین می‌افزاید که در نظم و نثر فصیح همه‌جا «گرامی» آمده و «گرام» رایج امروزی، که به تقلید از «کرام» عربی به کار می‌رود، درست نیست. بیت فردوسی که در نمودار آمده («پذیره فرستاد خسرو سوار / گرانمایگان گرامی هزار») شاهدی راستین از شاهنامه است. پیوند ژرف‌تر با ریشهٔ *gʷerH- را تنها مان (ص ۳۷۶) می‌دهد که «گرامی» را در کنار gūrtá- سنسکریت و grātus لاتینی می‌نشاند؛ آن گام محل تردید است، ولی همین یالِ «فارسی میانه ← فارسی نو» که این گره نشان می‌دهد قطعی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%DA%AF%D8%B1%D8%A7%D9%85%DB%8C\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"MON:3214\", \"status\": \"partial\", \"note\": \"Page number unverifiable (the 6-vol. edition is not online with pagination), but the entry itself is in the 2-vol. abridgement, MON_part2.txt line 30346: 'گرامی: (ص.) عزیز، محترم. ضح. — در نظم و نثر فصیح همه جا گرامی (= گرامیک، په.) آمده و «گرام» … درست نیست' — Mo'in gives the meaning and the Pahlavi antecedent Nourai wants.\"},\n            {\"ref\": \"IEC:376\", \"status\": \"supports\", \"note\": \"Mann, IEC p. 376 (IEC.txt form-feed leaf 218, page number '376' printed in the margin): 'gurtos \\\"revered, favoured, important\\\"; gurtis \\\"reverence, favour, importance\\\". Cf. gurus, gurio. Skt. gūrtáḥ … Per. cf. garāmī, adj. \\\"revered, excellent\\\"; Lat. grātus \\\"welcomed, favoured\\\"; grātēs … Osc. bratôm, Pael. bratom \\\"offering\\\"'. Nourai's page citation is exact and the reference does say what his arrow says.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie 1971 p. 37 (PHD.txt line 382)\", \"stance\": \"supports\", \"note\": \"'grāmig [gl'myk' | M grmyg, N girāmī] treasured, dear' — MacKenzie himself equates the Pahlavi and the New Persian word.\"},\n            {\"src\": \"MON\", \"where\": \"Mo'in s.v. گرامی (MON_part2.txt line 30346)\", \"stance\": \"supports\", \"note\": \"'گرامی: (ص.) عزیز، محترم … (= گرامیک، په.)' — Pahlavi origin tag.\"},\n            {\"src\": \"HRN\", \"where\": \"Horn, Grundriss (HRN.txt, greps for grāmī/girāmī)\", \"stance\": \"silent\", \"note\": \"Horn has no entry for گرامی in the Grundriss; the word is not among his numbered items.\"},\n            {\"src\": \"IEC\", \"where\": \"Mann p. 376\", \"stance\": \"supports\", \"note\": \"See ref_check — 'Per. cf. garāmī, adj. \\\"revered, excellent\\\"' listed with Lat. grātus under *gʷr̥tos.\"},\n            {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e Rishe-hā-ye Hend-o-Orupāyi (incoming/ARY/ARY_pages.txt)\", \"stance\": \"silent\", \"note\": \"Grepped گرامی in ARY_pages.txt: the only hits are Persian glosses inside other entries (lines 4716, 11835, e.g. 'چم این واژه در لاتین و زبان‌های رومانس: گرامی؛ عزیز؛ گران'), not a headword entry for گرامی.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Latin\",\n          \"words\": \"gratus; grâtia\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Latin grātus 'pleasing, acceptable, welcome; grateful' is the classic *gʷr̥H-to- of this root: Pokorny 478 sets the equation 'ai. gūrtá-ḥ \\\"willkommen\\\" = lat. grātus \\\"gefällig, dankenswert, dankbar\\\"', beside 'ai. gūrtí-ḥ f. \\\"Lob\\\" = lat. grātēs Pl. f. \\\"Dank\\\"', with Oscan brateis 'gratiae' and Paelignian bratom showing the Italic outcome gʷ > b in the Sabellic branch against Latin gr-. Wiktionary reconstructs Proto-Italic *gʷrātos < PIE *gʷr̥Htós. grātia is the regular abstract in -ia built to grātus, 'reconnaissance … faveur, crédit, influence … agrément, beauté, grâce' in Ernout-Meillet, from which the plural Grātiae renders Greek Χάριτες and the ablative grātiīs > grātīs 'for nothing' is drawn. Nourai's glosses 'agreeable, grateful' and 'favor' are accurate, and his AHD citation is the right one: Watkins gives 'Suffixed zero-grade form *gʷrə-to- in Latin grātus'.\",\n          \"derivation_fa\": \"لاتینی grātus «خوشایند، پذیرفتنی، سپاسگزار» همان صورت درجهٔ صفرِ *gʷr̥H-to- این ریشه است؛ پوکورنی در ص ۴۷۸ برابری «سنسکریت gūrtá- \\\"خوشامدشده\\\" = لاتینی grātus» و «سنسکریت gūrtí- \\\"ستایش\\\" = لاتینی grātēs \\\"سپاس\\\"» را می‌آورد و صورت‌های اُسکی brateis و پلیگنی bratom را گواه دگرگونی gʷ ایتالیک به b در شاخهٔ سابلی می‌داند. ویکی‌واژه صورت ایتالیک آغازین را *gʷrātos بازسازی می‌کند. grātia مصدر اسمیِ ساخته‌شده با پسوند -ia از همان صفت است و ارنو–می‌یه معناهای «سپاس، خدمت، نفوذ، زیبایی و لطف» را برای آن برمی‌شمارد. برچسب زبانی، معناها و ارجاع AHD در نمودار همه درست‌اند: واتکینز نیز می‌نویسد «صورت درجهٔ صفرِ پسوندی *gʷrə-to- در لاتینی grātus».\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/gratus\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 (AHD_watkins1985.txt line 542) s.v. gʷerə-3: 'To praise (aloud). 1. Suffixed zero-grade form *gʷrə-to- in Latin grātus, pleasing, beloved, agreeable, favorable, thankful: GRACE, GRATEFUL, GRATIFY, GRATIS, GRATITUDE, GRATUITY; AGREE, CONGRATULATE, INGRATE, INGRATIATE. … [Pok. 4. gʷer(ə)- 478.]' — Nourai's unpaginated 'AHD' citation is exactly right.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"Band I p. 478\", \"stance\": \"supports\", \"note\": \"'ai. gūrti-ḥ f. \\\"Lob\\\" = lat. grātēs Pl. f. \\\"Dank\\\" (dazu grātia \\\"Annehmlichkeit, Wohlgefälligkeit, Gnade, Dank\\\"), ai. gūrtá-ḥ \\\"willkommen\\\" = lat. grātus \\\"gefällig, dankenswert, dankbar\\\"; osk. brateis \\\"gratiae\\\", pälign. bratom'.\"},\n            {\"src\": \"LAT\", \"where\": \"Ernout-Meillet, Dictionnaire étymologique de la langue latine, s.v. grātus (LAT.txt lines 26800-26840)\", \"stance\": \"supports\", \"note\": \"'grātus … agréable (souvent joint à acceptus) … actif, \\\"reconnaissant\\\" … 3° grātēs, -ium f.pl. … marques de reconnaissance, actions de grâces (aux dieux) … 4° grātia, -ae f.: 1° abstrait \\\"reconnaissance\\\" … 4° agrément, beauté, grâce … Gratiae = Χάριτες'.\"},\n            {\"src\": \"IEC\", \"where\": \"Mann p. 376\", \"stance\": \"supports\", \"note\": \"'gurtos \\\"revered, favoured, important\\\" … Lat. grātus \\\"welcomed, favoured\\\"; grātēs, gp -ium, f. \\\"thanks, praise\\\"; Osc. bratôm, Pael. bratom \\\"offering\\\"'.\"},\n            {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Band I p. 686\", \"stance\": \"supports\", \"note\": \"Same equations as Pokorny, with the extra bibliography 'nach Kern KZ. 21, 242, weitere Lit. bei Walde LEWb.2 352'.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"English\",\n          \"words\": \"grace, gracious, grateful, agree, congratulate\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"All five are Latin-via-French reflexes of grātus/grātia and are listed together under this root by Watkins: 'GRACE, GRATEFUL, GRATIFY, GRATIS, GRATITUDE, GRATUITY; AGREE, CONGRATULATE, INGRATE, INGRATIATE'. In detail: grace is ME grace (late 12th c.) < Old French grace < Latin grātia 'favor, esteem, good will, gratitude', its theological sense 'God's unmerited favour' from the Vulgate's grātia rendering Greek χάρις; gracious < OFr gracieus < L. grātiōsus; grateful is a 16th-century English formation, grate (< L. grātus, borrowed as an adjective 'pleasing, thankful') + -ful; agree is ME agreen < OFr agreer 'to receive with favour', from the phrase a gré < L. ad grātum, neuter of grātus used as a noun — Klein s.v. agree spells this out; congratulate < L. congrātulārī 'to wish joy warmly', con- + grātulārī 'to wish joy' (itself a haplology of *grāti-tulor, grātus + -tulor), Klein s.v. congratulate. Nourai gives no reference for the node, but the chain is uncontroversial and covered by Watkins, Klein and Etymonline alike.\",\n          \"derivation_fa\": \"هر پنج واژه بازتاب‌های انگلیسیِ grātus/grātia لاتین‌اند که از راه فرانسهٔ کهن وارد شده‌اند و واتکینز همهٔ آنها را زیر همین ریشه فهرست می‌کند. به تفصیل: grace از انگلیسی میانه (اواخر سدهٔ دوازدهم) از grace فرانسهٔ کهن از grātia لاتینی «لطف، حرمت، سپاس» است و معنای الهیاتی آن («فیض») از ترجمهٔ لاتینی انجیل می‌آید که grātia را برابر χάρις یونانی نهاده است؛ gracious از grātiōsus؛ grateful ساختی انگلیسی از سدهٔ شانزدهم است (grate، وام‌گرفته از grātus، به‌اضافهٔ پسوند ‑ful)؛ agree از agreer فرانسهٔ کهن «به خوشی پذیرفتن» از عبارت a gré، یعنی ad grātum لاتینی، است — کلاین در ذیل agree همین را می‌گوید؛ و congratulate از congrātulārī لاتینی «شادباش گفتن» است. نورایی برای این گره ارجاعی نداده، ولی زنجیره بی‌مناقشه است و واتکینز، کلاین و Etymonline هر سه آن را تأیید می‌کنند.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/grace\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The node carries no reference of its own in the book (refs=None); it inherits the AHD citation of the Latin box above it, which does list GRACE, GRATEFUL, AGREE and CONGRATULATE under gʷerə-3.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein, Comprehensive Etymological Dictionary, s.vv. agree and congratulate (KLN_1966.txt lines 2004, 8726)\", \"stance\": \"supports\", \"note\": \"'agree, intr. v. — ME. agreen, fr. OF. agreer (F. agréer), \\\"to receive with favor\\\", fr. a (F. à), \\\"to\\\", and gre (F. gré), \\\"will, pleasure\\\", fr. L. grātum, neut. of the adjective grātus … See grateful'; 'congratulate, tr. v. — Fr. L. congratulātus, pp. of congratulārī … fr. con- and grātulārī, \\\"to wish joy\\\", fr. grātus, \\\"pleasing\\\". See grace, n., and cp. grateful.'\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. gʷerə-3\", \"stance\": \"supports\", \"note\": \"'GRACE, GRATEFUL, GRATIFY, GRATIS, GRATITUDE, GRATUITY; AGREE, CONGRATULATE, INGRATE, INGRATIATE' — all four of Nourai's derivatives plus gracious (s.v. grātiōsus) are in the list.\"},\n            {\"src\": \"WEB/Etymonline\", \"where\": \"etymonline.com/word/grace (archived via fetch_source.py)\", \"stance\": \"supports\", \"note\": \"'grace … late 12c., from Old French grace \\\"pardon, divine grace, mercy; favor, thanks\\\", from Latin gratia \\\"favor, esteem, regard; pleasing quality, good will, gratitude\\\", from gratus \\\"pleasing, agreeable\\\", from PIE root *gwere- (2) \\\"to favor\\\".'\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\nJSONEOF\npython3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-209.json > /dev/null && echo \"JSON OK\" && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 209",
 "description": "Write and validate page-209 verification"
}
```


### [2026-09-06T15:06:07.939Z] TOOL RESULT

```
JSON OK
nodes verified: 6/6
node verdicts: {'plausible': 2, 'disputed': 1, 'confirmed': 3}
root verdicts: {'confirmed': 1}
ref checks: {'partial': 2, 'supports': 5, 'not_checked': 2}
books consulted: {'partial': 4, 'supports': 17, 'contradicts': 2, 'silent': 4} | by book: {'HRN': 3, 'PHD': 3, 'IEC': 3, 'BRT': 2, 'POK': 2, 'BQT': 2, 'CHEUNG': 2, 'MON': 2, 'HUB': 1, 'NYB': 1, 'ARY': 1, 'LAT': 1, 'WLD': 1, 'KLN': 1, 'AHD': 1, 'WEB/Etymonline': 1}
```


## [2026-09-06T15:06:27.284Z] AGENT

Done. `data/verification/page-209.json` written; `verify_check.py 209` reports 6/6 nodes, 0 PROBLEM lines.

**Page 209 (book p. 179) — one entry, root "Gwer 2, Gwere 1" [IE] "to praise, welcome, sing"**

- Root: **confirmed**. Pokorny 478 is verbatim `4. gʷer(ə)- "die Stimme erheben", bes. "loben, preisen, willkommen heißen", aber auch "schelten; jammern"`; Watkins gʷerə-3 cites the same page; WP I 686 identical. Nourai's page number is exact.
- Node verdicts: confirmed 3 (#4 gerāmī, #5 Latin, #6 English), plausible 2 (#1 Avestan, #3 Pahlavi), disputed 1 (#2 Persian).

**Disputed**
- #2 Persian, **گریستن gerīstan** — Nourai follows Horn 1893 no. 915 (p. 204, the page he cites, which does say `aw. √gar-, gərənte "anrufen"`). Cheung 2007 p. 112 and Wiktionary put MP griy-/griyistan under Proto-Iranian ***garz** "to lament, weep" (Av. gərəz-, OP *grad-ya-), not under gar- "to praise". The node takes the worst verdict; the other three words (garzmān, garōgar, payğāreh) check out.

**No transcription_suspect items, no extraction errors** — the printed page (rendered, copied to `data/verification/sources/refs/ocr/BOOK/209.png`) matches the JSON word-for-word.

Notable findings for the owner:
- #1 "Avestan" box is mislabelled in the book: **grnâti** is Sanskrit gṛṇā́ti (so cited by both Pokorny and Bartholomae); **paiti-gar** is unattested — it is Horn's asterisked reconstruction (no. 358, p. **80**, not 202/204); **garo-gar** is not Avestan but a Zoroastrian Persian divine name (nos. 73–74 of the 101 names, Khordeh Avesta). Only `gar-` 2 and `garō.dəmāna-` are genuinely Avestan (Bartholomae cols. 512–513).
- Ref checks: POK:478, HRN:202, HRN:204, BQT:1793-1806 and IEC:376 all **support** (IEC 376 literally reads "Per. cf. garāmī, adj. 'revered, excellent'" beside Lat. grātus). MON:3214 not verifiable (6-vol. pagination not online; entry content confirmed in the abridgement).
- BQT p. 1803 was one pdf page off from `ref_page.py`'s default offset (printed = pdf + 1203 here); the گروگر entry + Mo'in's footnote were transcribed and appended to `data/verification/sources/refs/ocr/BQT/1803.vision.txt`.
- 5 web pages archived via `fetch_source.py` (Wiktionary *gʷerH-, گریستن, گرامی, gratus; Etymonline grace).
