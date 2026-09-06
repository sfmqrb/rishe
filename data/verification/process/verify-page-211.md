# Verification process log — verify-page-211


## [2026-09-06T14:51:57.966Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 211 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-211.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-211.json. Write /home/sfmqrb/git/rishe/data/verification/page-211.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 211` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T14:51:59.340Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T14:52:00.197Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T14:52:00.214Z] TOOL RESULT

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


## [2026-09-06T14:52:00.802Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-211.txt"
}
```


### [2026-09-06T14:52:00.818Z] TOOL RESULT

```
1	=== PDF page 211 (book page 181) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Gwer 4 : mountain  (refs POK:477)
4	#1 (parent #0) [Avestan] refs=POK:477; KLN:374; SYN:25 | gairi : mountain | NOTE: Compare with derivatives of the Indo-European root "Gwer 3".
5	  #2 (parent #1) [Pahlavi] refs=SNS:318 | gar 1 : mountain
6	    #3 (parent #2) [Persian] refs=MON:3212; SNS:318 | gar 1 «گَر ۱» : mountain ; garšâh «گرشاه» : a male name | extra: گلشاه | NOTE: It literally means "king of mountains"
7	#4 (parent #0) [Old Slavic] refs=KLN:374 | čurva : mountain ; Čurvatinŭ : a mountainous area in former Yugoslavia, Croatia
8	  #5 (parent #4) [French] refs=KLN:368 | Chorwat : Croatina and its people ; cravate : neckpiece worn by the Croats, a fashion in Croatina
9	    #6 (parent #5) [Persian] refs=MON:2930 | krâvât «کراوات» : cravat
10	    #7 (parent #5) [English] refs=KLN | Croat, Croatia, cravat
11	--- entry 1 ---
12	ROOT Gwere 1 -> redirect to Gwer 2
13	--- entry 2 ---
14	ROOT Gwere 2 -> redirect to Gwer 3
15	--- entry 3 ---
16	ROOT [Indo-European] Gwes, Zgwes : to extinguish  (refs POK:479)
17	#1 (parent #0) [Sanskrit] refs=POK:479 | jas : extinguished, exhausted, wounded
18	  #2 (parent #1) [Avestan] refs=HRN:145 | zaxya : wound
19	    #3 (parent #2) [Persian] refs=BQT:1007 | zaxm «زخم» : wound ; zaxmeh «زخمه» : plectrum
20	#4 (parent #0) [Greek] refs=KLN:111 | a-sbenunai : not extinguishable ☞Ne 1
21	  #5 (parent #4) [English] refs=AHD:78 | asbestos
22	--- entry 4 ---
23	ROOT Gweye -> redirect to Gweie
24	--- entry 5 ---
25	ROOT [Indo-European] Gwhder : to flow, run  (refs POK:487)
26	#1 (parent #0) [Avestan] refs=POK:487 | xšar : to flow
27	  #2 (parent #1) [Persian] refs=HRN:172; BQT:1223-1265 | šârîdan «شاریدن ( شیریدن )» : to flow | extra: شار ، آبشار ، سرشار ، شُرّان ، شُرشُر
28	#3 (parent #0) [Sanskrit] refs=POK:487 | kša : to flow
29	
```


## [2026-09-06T14:52:05.946Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-211.json",
 "description": "Read source JSON page 211"
}
```


### [2026-09-06T14:52:06.004Z] TOOL RESULT

```
{
  "pdf_page": 211,
  "book_page": 181,
  "entries": [
    {
      "root": {
        "name": "Gwer 4",
        "lang": "Indo-European",
        "refs": "POK:477",
        "gloss": "mountain"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:477; KLN:374; SYN:25",
          "words": [
            {"translit": "gairi", "gloss": "mountain", "script": null}
          ],
          "script_extra": null,
          "note": "Compare with derivatives of the Indo-European root \"Gwer 3\".",
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "SNS:318",
          "words": [
            {"translit": "gar 1", "gloss": "mountain", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "MON:3212; SNS:318",
          "words": [
            {"translit": "gar 1", "gloss": "mountain", "script": "گَر ۱"},
            {"translit": "garšâh", "gloss": "a male name", "script": "گرشاه"}
          ],
          "script_extra": "گلشاه",
          "note": "It literally means \"king of mountains\"",
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Old Slavic",
          "refs": "KLN:374",
          "words": [
            {"translit": "čurva", "gloss": "mountain", "script": null},
            {"translit": "Čurvatinŭ", "gloss": "a mountainous area in former Yugoslavia, Croatia", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "French",
          "refs": "KLN:368",
          "words": [
            {"translit": "Chorwat", "gloss": "Croatina and its people", "script": null},
            {"translit": "cravate", "gloss": "neckpiece worn by the Croats, a fashion in Croatina", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Persian",
          "refs": "MON:2930",
          "words": [
            {"translit": "krâvât", "gloss": "cravat", "script": "کراوات"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 5,
          "lang": "English",
          "refs": "KLN",
          "words": [
            {"translit": "Croat, Croatia, cravat", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Gwere 1",
        "redirect": "Gwer 2"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Gwere 2",
        "redirect": "Gwer 3"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Gwes, Zgwes",
        "lang": "Indo-European",
        "refs": "POK:479",
        "gloss": "to extinguish"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "POK:479",
          "words": [
            {"translit": "jas", "gloss": "extinguished, exhausted, wounded", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Avestan",
          "refs": "HRN:145",
          "words": [
            {"translit": "zaxya", "gloss": "wound", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "BQT:1007",
          "words": [
            {"translit": "zaxm", "gloss": "wound", "script": "زخم"},
            {"translit": "zaxmeh", "gloss": "plectrum", "script": "زخمه"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Greek",
          "refs": "KLN:111",
          "words": [
            {"translit": "a-sbenunai", "gloss": "not extinguishable", "script": null, "see": ["Ne 1"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": "AHD:78",
          "words": [
            {"translit": "asbestos", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Gweye",
        "redirect": "Gweie"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Gwhder",
        "lang": "Indo-European",
        "refs": "POK:487",
        "gloss": "to flow, run"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:487",
          "words": [
            {"translit": "xšar", "gloss": "to flow", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "HRN:172; BQT:1223-1265",
          "words": [
            {"translit": "šârîdan", "gloss": "to flow", "script": "شاریدن ( شیریدن )"}
          ],
          "script_extra": "شار ، آبشار ، سرشار ، شُرّان ، شُرشُر",
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "POK:487",
          "words": [
            {"translit": "kša", "gloss": "to flow", "script": null}
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


## [2026-09-06T14:52:07.109Z] TOOL CALL #4: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo \"---MATRIX---\" && cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "List verification dir and read source matrix"
}
```


### [2026-09-06T14:52:07.164Z] TOOL RESULT

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
---MATRIX---
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


## [2026-09-06T14:52:32.021Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KLN','SYN','SNS','MON','HRN','BQT','AHD','WLD','BRT','PHD','NYB','HUB','CHEUNG','IEC','SKT','ARY','LKT','DEV','PHN','FSD','WEB','FRS','FSF','FFD','IRN']:\n    if k in d: print(k, json.dumps(d[k], ensure_ascii=False)[:600]); print()\n\""
}
```


### [2026-09-06T14:52:34.743Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves

SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-

NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 

SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 

LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 

DEV {"title": "L. M. Devic, Dictionnaire étymologique des mots français d'origine orientale, Paris 1876", "edition_found": "1876", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairety00devi", "identifier": "dictionnairety00devi (also dictionnairetym02devigoog, fr105comparative41)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/DEV.txt", "page_offset": "leaf = printed + 26 (pp. <80) to +30 (pp. >84), e.g. leaf 29 = p.3, leaf 118 = p.88. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.

PHN {"title": "A. P. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du turc, Paris 1866", "edition_found": "1866", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairetym01pihagoog", "identifier": "dictionnairetym01pihagoog (others: bub_gb_QnsSAAAAIAAJ, dictionnairetym00pihagoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHN.txt", "page_offset": "leaf = printed + 31 (e.g. leaf 33 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://ar

FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt

WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/W

FRS {"title": "Asadi Tusi, Loghat-e Fors, ed. Mojtaba'i & Sadeqi, Kharazmi 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/LughatEFurs-AbuMansurAliBinAhmadAsadiTusiFarsi (Abbas Eqbal's 1319/1940 Tehran edition); also dli.ernet.439493 / dli.ernet.437743 (Horn's 1897 Göttingen edition, 'Lughat Faras')", "lookup_hint": "Look up the headword (entries grouped by final letter); FRS_pages.txt has \\f page breaks (567 leaves). Pagination differs from the 1365 Kharazmi edition Nourai cites — verify the entry, not the page.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/s

FSF {"title": "Abdolhossein Noushin, Vazhe-namak: Farhang-e Vazheha-ye Doshvar-e Shahnameh (Farhang-e Shahnameh), Donya 1363/1984", "kind": "archive_djvu", "url": "https://archive.org/details/20220809_20220809_1444", "lookup_hint": "grep the headword in FSF_pages.txt (alphabetical glossary); use inside.php search for leaf numbers. Also https://archive.org/details/nooshinshahnameh is a different Noushin book (گزارشی چند درباره شاهنامه).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF.txt"], "page_offs

FFD {"title": "Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ماده-های-فعلهای-فارسی-دری-محسن-اب/ -> https://dl.eliteraturebook.com/app/public/attachments/6925d29630b83.PDF (free PDF site; grey)", "lookup_hint": "Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/download): nothing; only a related paid e-book 'واژگان زبان فارسی دری' (fidibo). ketabnak.com/book/45024 is a different book (فهرست فعلهای فارسی).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/s

IRN {"title": "Bahram Farahvashi, Iranvij, Tehran University Press 1368/1989", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ایرانویج-بهرام-فره-وشی/ -> https://dl.eliteraturebook.com/storage/img/ایرانویج.pdf (free PDF site; grey) ; Google Books kP8bAAAAIAAJ (1368 ed., no view)", "lookup_hint": "archive.org 'Iranvej' item is a radio programme, not the book; nothing on ketabnak/noorlib. | For pages in a scanned volume use: python3 tools/ref_page.py IRN:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)", "local_file": ["/home/sfmqrb/git/rishe/data/v
```


## [2026-09-06T14:52:40.126Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for p in 477 479 487; do echo \"=== POK printed p.$p (POK_01 leaf $((p+8))) ===\"; awk 'BEGIN{RS=\"\\f\"} NR=='$((p+9))'' POK_01.txt | head -60; done"
}
```


### [2026-09-06T14:52:42.587Z] TOOL RESULT

```
=== POK printed p.477 (POK_01 leaf 485) ===
=== POK printed p.479 (POK_01 leaf 487) ===
=== POK printed p.487 (POK_01 leaf 495) ===
```


## [2026-09-06T14:52:45.509Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for f in POK_01.txt POK_02.txt POK_03.txt POK_full.txt; do echo \"$f: $(awk 'BEGIN{RS=\"\\f\"} END{print NR}' $f) leaves, $(wc -c <$f) bytes\"; done"
}
```


### [2026-09-06T14:52:48.270Z] TOOL RESULT

```
POK_01.txt: 363 leaves, 981836 bytes
POK_02.txt: 433 leaves, 1137861 bytes
POK_03.txt: 429 leaves, 1170809 bytes
POK_full.txt: 1 leaves, 3971883 bytes
```


## [2026-09-06T14:52:51.762Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for p in 477 479 487; do echo \"=== POK p.$p (POK_02 leaf $((p-344))) ===\"; awk 'BEGIN{RS=\"\\f\"} NR=='$((p-343))'' POK_02.txt | head -70; echo; done"
}
```


### [2026-09-06T14:52:53.474Z] TOOL RESULT

```
=== POK p.477 (POK_02 leaf 133) ===
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

=== POK p.479 (POK_02 leaf 135) ===
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

=== POK p.487 (POK_02 leaf 143) ===
haftes  Tier',  PI.  köter  ,allerhand  Ungeziefer',  mnd.  guäd,  mndl.  gwaet, holl.    kwaad  ,böse,   häßlich,   verderbt',   md.   quäd  ,böse,    ekel,   schwach' ;'|
mit  idg.  -9U-:  >
cymr.  budr  , schmutzig',  budro  ,beschmutzen',  mir.  buadraim  ,trübe,  ver- wirre' (vgl.  Pedersen  KG.  I  112);
ags.  cwead  ,Kot',  afries.  quäd  , schlecht';
mit  u  aus  *-du-  slovak.  oTiuda  , Scheusal',  klr.  ohüda  , Tadel',  aruss. guditi  ,calumniari^  blasphemare,  accusare'  u.  dgl. ;
mit    -9-    als    Tief  stufe    von    -ö{u\    oder    germ.    Ablautneubildung  ndd. quadder  ,schmutzige  Feuchtigkeit,  Schleim'  =  mnd.  koder  , Schleim',  nhd. dial.  koder,  Köder  ,zäher  Schleim,  Schnupfen',  auch  ndd.  quassen  (*kwadsön)    -^ ,(in  Feuchtem)  quatschen',  quasken,  quatsken,  nhd.  quatschen,  engl,  quask, squash  und  vielleicht  der  Volksname  Quadij
i
>
485
alb.  ZI  (^guedhiio-),  fem.  2626  {*giLedhia)  ^schwarz,  unglücklich,  schlimm', ZI  f.  ;Trauer,  Hungersnot^
WP.  I  694  ff.,  WH.  I  118  f.,  Trautmann  81.
gnozd{h)o-,  guozd{h)i-  ,Nagel,  penis'.
Gallorom.  hottos  ,Radnabe^  (M.-L.  1229a);  cymr.  hoth  , Radnabe,  Schild- buckeP,  mir.  bot,  nir.  hod  m.  ,Schwanz,  penis';
abg".  gvozdh  ,Nagel',  poln.  g{io)6zd£  ds.,  öech.  hvozdej  ,Durchschlagholz^; dazu  poln.  g(w)o£dzik  ,Nelke',  cech.  hvozdik  ds. Pokorny  ZceltPh.  16,  405,  WH.  I  574,  636,  Berneker  365  f.
g^rebb'  , Leibesfrucht,  Kind,  Jungest
Gr.  ßgicpaq  n.  , Leibesfrucht,  Junges',  mir.  hrommach  (*g^7'ombhäkos),  aksl. zr^he  ,Füllen^ WP.  I  689.
g^reig-  ,schlafen,  träumen'??
Gr.  ßgi^ü)  (*ßQtyi(o)  l'ßgi^a  , schlafe,  bin  untätig^,  dßgl^ '  eyQrf/6Q0)g  Hes. ; russ.  grezith  ,im  Schlaf  reden,  phantasieren'  (kauni  *grez-,  eher  ^grtz-), greza  ,Traum,  Faseln,  alberne  Redend  Sehr  unsicher ;  s.  auch  Berneker  351. WP.  I  698.
g^rendh-  ,sch wellen  (physisch,  und  vor  Hochmut);  Schwellung,  Erhöhung, Brüstt Gr.  ßQSvd-og  , Stolz',  ßgev-d^o^at  ,gebärde  mich  stolz^; ,    lat.  grandis  ,groß,  großgewachsen,  alt,  erhaben^  (a  =  ,  oder  <,) ;
aksl.  grgdb   ,Brust',    slovak.    hrud   , Erhöhung^,    poln.  alt   gredzi   , Brust', grcf,d  , erhöhte  Stelle  im  Sumpft,  alt  ,Insel,  Werder^  (usw.). WP.  1  699,  WH.  I  617  f.
^retso-  ,dick,  groß'??
Lat.  grossus   ,dick^   pflegt   man   mit  mir.  cymr.    corn.   bret.  bras  ,groß, dick',  mir.  auch  , stark',  zusammenzubringen.  Doch  macht  der  kelt.  Voka- lismus   Schwierigkeiten,    und    mir.    bres    ,schön'    ist    kaum   dazuzustellen. ;.    Ob  bras  eher  als  ^gurd-sto-  zu  lat.  gravis,  oben  S.  476? WP.  I  698,  WH.  I  623.
^eugh-f  g^rugh-   a)  ,mit  den  Zähnen  knirschen',   b)  ,nagen,  beißen'.
a)  gr.  ßgijxo)  ,knirsche
```


## [2026-09-06T14:53:00.628Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -o '.\\{600\\}gairi.\\{400\\}' POK_full.txt | head -20"
}
```


### [2026-09-06T14:53:01.795Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T14:53:04.137Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -c 'gairi' POK_full.txt POK_02.txt; echo ---; grep -n -o '.\\{300\\}gairi.\\{300\\}' POK_02.txt | head"
}
```


### [2026-09-06T14:53:05.320Z] TOOL RESULT

```
POK_02.txt:1
POK_full.txt:2
---
```


## [2026-09-06T14:53:08.264Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n 'gairi' POK_02.txt | cut -c1-500; echo \"=== full ===\"; grep -o -b 'gairi' POK_full.txt"
}
```


### [2026-09-06T14:53:08.329Z] TOOL RESULT

```
2022:Ai.  giri-h  m.  ;,Berg^,  av.  gairi-  ds. ;
=== full ===
1481375:gairi
1683615:gairi
```


## [2026-09-06T14:53:11.047Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '2010,2030p' POK_02.txt; echo \"=== which leaf ===\"; awk 'BEGIN{RS=\"\\f\"} /gairi/ {print \"leaf(1-based NR)=\"NR}' POK_02.txt"
}
```


### [2026-09-06T14:53:13.546Z] TOOL RESULT

```
Hierher  ferner  als  rz -Ableitungen  von  g]^er9-  und  g'^eräii-i  got.  (asilu-) qairnus  /Esels) mühle^  (*gVierdnu-),  anord.  kvern  f.  (*gV:erna)  ^Mühlstein; Handmühle^,  ags.  ciceorn  ds.^  ahd.  quirn^  quirna  ds. ;
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
der  thrak.  VN  ''Ynsg-ßogeoi  ,die  jenseits  des  Berges  Wohnenden^  ent- hält wohl  das  gr.  Lw.  *ßogLg]
478  f
lit.  nugarä  ^Rücken^  Bergrücken^;
mit  der  Bedeutungsentwicklung  ,Berg  — (Berg) wald  — Baum':  lit.  g\re, giriä  ,Wald',  lett.  dzire  ds.,  und  apr.  garian  n.  (Akk.  garrin)  ,Baum'; ferner  lett.  gars  ,Wald',  gärsas  ,Sumpf';
aksl.  gora  ,Berg',  skr.  gbra  ,Berg,  Wald',   usw.
WP.  I  682,  Trautmann  78,  Pedersen  La  einqu.  decl.  lat.  37,  66.
=== which leaf ===
leaf(1-based NR)=135
```


## [2026-09-06T14:53:25.612Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== leaf136 (p~479) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==137' POK_02.txt | head -60"
}
```


### [2026-09-06T14:53:30.596Z] TOOL RESULT

```
=== leaf136 (p~479) ===
n bekommen',  girdeti  ,hören',  garsas  ,Schall',  apr.  gerdaut  ,sagen',  lett. dzirdet  ,hören',  Mühlenbach-Endzelin  I  552  mit  Lit.
Mit  in  malam  partem  gewendeter  Bedeutung:
gr.  ÖEiQiäv  XoLÖOQsTa&aL.  A&'/.ujvsq]  öeigeToL'  Xolöoqoi.  ol  avroi]  öeglai' loLÖOQiai  Hes.  (d.  i.   wohl  ör]Q~  aus  *g^er-s-)]
ahd.  gueran  ,seufzen'.
Gegenüber  den  ähnlichen  Schallwurzeln  ger-,  gur-  ist  nicht  überall  eine sichere  Scheidung  möglich;  doch  ist  für  die  hier  unter  g^er-  vereinigten Worte  der  Begriff  der  gehobenen  Äußerung  unverkennbar,  bis  auf  die darum  nicht  sicher  anzugliedernde  c^/i-Erweiterung.
WP.  I  686  f.,  WH.  I  583,  619  f.,  Trautmann  88  f.
479
Süef'f  S^^^^~  ;^6uchten  und  heiß  sein'.
Ai-  J^<^'*ö[^^   ;fiebert^,  jvara-h  , Fieber^   Schmerz,   Kummer',  jürvati  ,ver-
gQot',  ywr]ri2-Ä  ,Glut'  (<.*jvü7'-,  *§wf-);  damehen  jvdlati  ,flammt  auf,  glüht,
leuchtet',  jvalita-h  ,flammend,   leuchtend',  jvaland-h  ,brennend,  brennbar',
jji.  , Feuer',  n.  ,das  Brennen,  Lodern',  jvala-h  m.  ,Licht,  Flamme,  Fackel',
jDälä  f.  ds. ;
mnl.  coorts  m.,  mnd.  korts  ,Fieber'??;
lit.  zlüriii,  ziüreti  ,sehen',  zim^ä  , Aussicht,  Blick',  ziüras  ,Uhu';
vollstufig'  lett.  zvers  ,funkelnd',  zvernot  ,glühen,  aufleuchten'.
WP.  I  643,  Wackernagel  Ai.  Gr.  I  §  228.
^,era-  ,Stange,  Spieß'.
Av.  grava-  ,Stock,  Rohrstab'  (zum  Ablaut  vgl.  lat.  genu :  got.  kniu) ; lat.  uerüj  -üs  n.  , Spieß' ;  umbr.  berva  ,uerua',  berus  ,ueribus' ; air.  bi{u)r  n.,  später  f.,  ,Speer,  Spieß',  cjmr.  corn.  bret.  ber  f.,  m.  ds. ; got.  gairu  n.  , Pfahl,  Stachel' ;
vielleicht    als    , Zweig'    zu   gr.    ßQvio   ,sprosse,   strotze',   ßqvov   n.  ,Moos, Kätzchen',    ef,iß()vov    n.    ,das    Neugeborene'   und   (?)    germ.    '^krüda-   (idg. *gurü-to-)  in  ahd.  mhd.  krüt,  asächs.  krüd  ,Kraut'. Über  lat.  bruscum  ,Schwamm  am  Ahornbaum'  s.  WH.  I  117. WP.  I  689.
g^es-,  zgnes-  , erlöschen'.
Ai.  jdsate,  jdsyati  ,ist  erschöpft',  jäsdyati  ,löscht,  erschöpft'  ;
gr.  att.  aßevvvfxt  ,lösche'  (für  *(jßsLvv(XL),  Aor.  hom.  oßea-aaL,  üoßeOToq ,unauslöschlich',  mit  oßeo-  nach  oßoa-  (s.  unten)  für  lautges.  gösg-^  das
```


## [2026-09-06T14:53:36.246Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==137' POK_02.txt | sed -n '30,60p'; echo \"=== leaf137 ===\"; awk 'BEGIN{RS=\"\\f\"} NR==138' POK_02.txt | head -25"
}
```


### [2026-09-06T14:53:38.426Z] TOOL RESULT

```
=== leaf137 ===
in  t8Lva(.isv'  aßivvvfxsv  {*zd^n-  aus  *zg}':esn-)  Hes.  vorliegt;  eaßr]v  ,ich  er- losch' (aus  der  2.  Sg.  e-zgVies-s,  1.  PL  e-zgltes-me^  woraus  eoßrjg^  eaßrj^xsv, wonach  auch  eaßrjv  usw.  wegen  des  Typus  eßX7]v  und  weil  auch  in  oßevvvui der  Wurzelausl.  s  fürs  Sprachgefühl  nicht  mehr  vorhanden  war) ;  ion. xaraaßcüaai  ,löschen',  aus  *GßodoaL  von  einem  Präs.  *oßo[a]d^a}y  woneben mit  aus  dem  Typus  ^slva^iev  verschlepptem  Anlaut  t^oäg'  G[s]ß€a6igj ^öanov'  a[s]ß£aov  Hes.;
lit.  gestü  (alt  g^su),  gesaü,  gesti  ,erlöschen,  ausgehen',  Kausat.  gesav, gesyti  und  gesinü,  gesinti  ,löschen',  gesme  ,kleines,  eben  noch  glimmendes Feuei"' ;  lett.  dziestu  (aus  *genstu),  dzisu,  dzist  (Ablautentgleisung),  ,er- löschen,  kühl  werden',  dzesu  (dzeku),  dzesu  (dzesu),  dzest  {dzest)  ,]Öschen', dzesma  {dzesma)  ,der  kühle  Hauch  am  Morgen',  dzestrs  ,kühl' ;
abg.  Kausat.  ^gasg,  *gasiti  ,erlöschen,  ausgehen',  in  aksl.  ugasiti  ,aß8aai'j ugasnqtij  Aor.  ugaaz,  und  ugasati  ,aß£vvvod^ai',]  unsicherer  ist,  ob  dazu  ab- lautendes g'^es-  in  abg.  uzanz,  russ.  üzas  ,Schrecken',  abg.  zasiti  ,schrecken'
480  9
vorliegt  (Pedersen  IF.  5,  47 ;  vielleicht  als  ""ged-s-os  zum  allerdings  nag Herten  lit.  gaüdinu-,  -inti  ^schrecken^,  üsi-gq,stü,  -gandaü  'gq.sti  ,erschreckei intrans/,  Ugqstis  .Schrecken',  Scheftelowitz  IF.  33,  155).  Ob  hierher  kelj Häs-  .sterben'?  (s.  unter  g'^em-,  g'^ä-  .gehen,  kommen');
unsicher  ist  Verwandtschaft  von  ahd.  quist  L  .Verderben.  Vernichtuii« als  *g^es-ti-s  .*Erlöschen'.  wovon  got.  qistjan,  fragistjan  .verderben,  trans/, fraqistnan  .verderben,  intrans.'.  ahd.  ßrquisten  .verderben,  trans.'.
WP.  I  693.  Trautmann  86.  Feist  388  f.
gues-,  guos-,  gus-,  erweitert  guoz-do-  .Gezweig.  Laubwerk'. Norw.  dän.  kvas  .kleine,  abgehauene  Zweige';
1.  mit  -d-Er Weiterung:  '* alb.  gQ^.  ghethi  .Blatt',  tosk.  gjethe  .Laub.  Zweig'  (kollekt.  PI.  zu  einem
Sg.  *gath  aus  *guozd-)]
ahd.  questa  f.,  mhd.  queste,  koste,  haste,  quast  m.  f..  .Laubbüschel, Sprengwedel.  Besen',  nhd.  Quas
```


## [2026-09-06T14:53:47.579Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n 'ksar\\|xsar\\|k[sš]ar-\\|x[sš]ar' POK_02.txt | cut -c1-300 | head -20; echo \"=== leaf 144-146 headers ===\"; for n in 144 145 146; do echo \"--- NR=$n ---\"; awk 'BEGIN{RS=\"\\f\"} NR=='$n'' POK_02.txt | head -40; done"
}
```


### [2026-09-06T14:53:50.239Z] TOOL RESULT

```
2183:Ai.    k^drati   , fließt,   strömt,   zerrinnt,   verschwindet',    ksara-m   ,Wasser',
4302:Ai.  saphara-  m.  ,Cyprinus    sophore'  =  lit.  säpalas   ,C7prinus    dobula'. gr.  TiVftQLvog   , Karpfen',   vielleicht    nach    xsarQivog,    Kogayuvcg,    igv-d^Qivog usw.  umgebildet;  v-  eventuell  volksetymologisch  nach  KvTTQog,  da  *y.07tQlvog an  ytÖTtQog  denken  ließe.
=== leaf 144-146 headers ===
--- NR=144 ---
haftes  Tier',  PI.  köter  ,allerhand  Ungeziefer',  mnd.  guäd,  mndl.  gwaet, holl.    kwaad  ,böse,   häßlich,   verderbt',   md.   quäd  ,böse,    ekel,   schwach' ;'|
mit  idg.  -9U-:  >
cymr.  budr  , schmutzig',  budro  ,beschmutzen',  mir.  buadraim  ,trübe,  ver- wirre' (vgl.  Pedersen  KG.  I  112);
ags.  cwead  ,Kot',  afries.  quäd  , schlecht';
mit  u  aus  *-du-  slovak.  oTiuda  , Scheusal',  klr.  ohüda  , Tadel',  aruss. guditi  ,calumniari^  blasphemare,  accusare'  u.  dgl. ;
mit    -9-    als    Tief  stufe    von    -ö{u\    oder    germ.    Ablautneubildung  ndd. quadder  ,schmutzige  Feuchtigkeit,  Schleim'  =  mnd.  koder  , Schleim',  nhd. dial.  koder,  Köder  ,zäher  Schleim,  Schnupfen',  auch  ndd.  quassen  (*kwadsön)    -^ ,(in  Feuchtem)  quatschen',  quasken,  quatsken,  nhd.  quatschen,  engl,  quask, squash  und  vielleicht  der  Volksname  Quadij
i
>
485
alb.  ZI  (^guedhiio-),  fem.  2626  {*giLedhia)  ^schwarz,  unglücklich,  schlimm', ZI  f.  ;Trauer,  Hungersnot^
WP.  I  694  ff.,  WH.  I  118  f.,  Trautmann  81.
gnozd{h)o-,  guozd{h)i-  ,Nagel,  penis'.
Gallorom.  hottos  ,Radnabe^  (M.-L.  1229a);  cymr.  hoth  , Radnabe,  Schild- buckeP,  mir.  bot,  nir.  hod  m.  ,Schwanz,  penis';
abg".  gvozdh  ,Nagel',  poln.  g{io)6zd£  ds.,  öech.  hvozdej  ,Durchschlagholz^; dazu  poln.  g(w)o£dzik  ,Nelke',  cech.  hvozdik  ds. Pokorny  ZceltPh.  16,  405,  WH.  I  574,  636,  Berneker  365  f.
g^rebb'  , Leibesfrucht,  Kind,  Jungest
Gr.  ßgicpaq  n.  , Leibesfrucht,  Junges',  mir.  hrommach  (*g^7'ombhäkos),  aksl. zr^he  ,Füllen^ WP.  I  689.
g^reig-  ,schlafen,  träumen'??
Gr.  ßgi^ü)  (*ßQtyi(o)  l'ßgi^a  , schlafe,  bin  untätig^,  dßgl^ '  eyQrf/6Q0)g  Hes. ; russ.  grezith  ,im  Schlaf  reden,  phantasieren'  (kauni  *grez-,  eher  ^grtz-), greza  ,Traum,  Faseln,  alberne  Redend  Sehr  unsicher ;  s.  auch  Berneker  351. WP.  I  698.
g^rendh-  ,sch wellen  (physisch,  und  vor  Hochmut);  Schwellung,  Erhöhung, Brüstt Gr.  ßQSvd-og  , Stolz',  ßgev-d^o^at  ,gebärde  mich  stolz^; ,    lat.  grandis  ,groß,  großgewachsen,  alt,  erhaben^  (a  =  ,  oder  <,) ;
aksl.  grgdb   ,Brust',    slovak.    hrud   , Erhöhung^,    poln.  alt   gredzi   , Brust', grcf,d  , erhöhte  Stelle  im  Sumpft,  alt  ,Insel,  Werder^  (usw.). WP.  1  699,  WH.  I  617  f.
^retso-  ,dick,  groß'??
Lat.  grossus   ,dick^   pflegt   man   mit  mir.  cymr.    corn.   bret.  bras  ,groß, dick',  mir.  auch  , stark',  zusammenzubringen.  Doch  macht  der  kelt.  Voka- lismus   Schwierigkeiten,    und    mir.    bres    ,schön'    ist    kaum   dazuzustellen. ;.    Ob  bras  eher  als  ^gurd-sto-  zu  lat.  gravis,  oben  S.  476? WP.  I  698,  WH.  I  623.
^eugh-f  g^rugh-   a)  ,mit  den  Zähnen  knirschen',   b)  ,nagen,  beißen'.
a)  gr.  ßgijxo)  ,knirsche 
--- NR=145 ---
 mit  den  Zähnen'  (daneben  durch  Entgleisung aus  ßQv^o),  eßgv^a :  ßgiTio))  ,beiße',  ßQvydrjv  ,beißend',  ßQV'y(,iög  , Zähne- knirschen', ßgvxsTÖQ  ,kaltes  Fieber'  (,Zähneklappern').
486
b)  air.  hrön  ^Kummer^  cjmr.  brtoyn  ^stechender  Schmerz'  (urkelt. *brügnos);
lit.  grduziu,  grduHi  ,nagen^  sugrüzinü  ^vernichten';
aksl.  gryzq,  grysti  ,nagen'  (in  andern  slav.  Sprachen  auch  von  nagendem Kummer;  hierher  wohl  auch  sloven.  grüze  PI.  f.  ^Krätze^.
Zu  gryzg  wahrscheinlich  russ.  grusth  ^Kummer',  sloven.  grüst  ,EkeP.
WP.  I  697  f.,  Trautmann  100.
j
Ohvi  und  Q^h.
^bctei{o-)  , hinschwinden,  z'ngrunde  gehen^,  auch  trans.  ^vernichten' ; gVidi-ti-s,  g^bdoi-o-  ,Untergang^
Ai.  ksindti,  ksinöti  ( :  gr.  *q)d-LvJ^-(o)j  ksdyati  ,vernichtet,  läßt  vergehen', partiz.  ksitd-h  , erschöpft'  (=  gr.  q)d'LTÖg ;  srdva-h  dksitam  =  gr.  y,Xeog  Ucfd-i- xov  ^unverwüstlicher  Ruhm^),  kslnd-h  ds.,  ksiydte  , schwindet  hin,  nimmt ein  Ende',  ksayd-h  , Abnahme,  Untergang'  (:  gr.  q)'d'örj  f.),  kHti-h  , Ver- drehen, Untergang'  (=  gr.  q)d-L(TLg  und  -?-  lat.  sitisj  vgl.  -tuSt  lat.  sittts)]
prakr.  ajjhitah-  (=  äq)d-LTog)y  jklna-  (=  ai.  kslna-)]
av.  ay^önvamndm  ,sich  nicht  mindernd'  (Kuiper  Nasalpräs.  65^);
gr.  ep.  (pMvoiy  att.  q)d-tvu)  (^cpS-ivfWy  s.  oben)  , vernichte',  meist  intr. ,schwinde  hin,  gehe  zugrunde',  cp^ivv-d-o)  , schwinde  hin,  mache  verschwin- den', Fut.  q)d'hao)  (att.  di7to(pd-taw)j  Aor.  eifdsiaa  (att.  SLTtecpd-Xaa),  icpd-t(.iriv^ qi&ffxsvog  ,vernichten',  Pass.  , zugrunde  gehen',  Partiz.  Perf.  Pass.  q}&LTÖg, (pd-ÖT}  , Schwindsucht',  (pd-laig  ds.  (s.  oben  ) ;  über  vielleicht  alte  Doppel- formen, wie  ipiv€G&aLj  xpiva^siv  , Blüten  oder  Früchte  abfallen  lassen,  ver- lieren', xpLGig'  dnwXeia  Hes.,  u.  dgl.  s.  Schwyzer  Gr.  Gr.  I  326.
Aus  dem  Lat.  wahrscheinlich  situs,  -üs  ,der  modrige  Schmutz  und Schimmel,  körperliche  Unreinlichkeit  und  alles  körperliche  und  geistige  Ver- rosten' und  suis  ,Durst'  (wenn  eigentlich  ,*Hinschwinden,  Verschmachten').
WP.  I  505 f.,  Schwyzer  Gr.  Gr.  I  326,  Benveniste  BSL.  38,  139 ff.
g^hffer-   (oder  besser  g^ider-??)  , 
--- NR=146 ---
rinnen,   fließen;   zerrinnen,  verschwinden',
im  ar.  Kaus.  und   im  gr.  zo-Verbum   trans.  , rinnen  lassen,  zerrinnen
lassen',  daher  gr.  , verschwinden  lassen,  vernichten'.
Ai.    k^drati   , fließt,   strömt,   zerrinnt,   verschwindet',    ksara-m   ,Wasser',
ksärayati  ,läßt  fließen',  ksälayati  , wäscht  ab'  (vgl.  Wackernagel  Ai.  Gr.  I
241);  av.  y^araiti  , strömt,  wallt  auf,  yzärayeiti  ,läßt  fließen',  mit  vi-  ,läßt
überfließen';  Weiterbildung  in  a-yzrädayeiti  ,läßt  aufwallen',  vi-yzrädayeiti
;läßt  auseinander,   überwallen' ;    umgestellt  zyar-  in  avi  fra-zyaraiti  ,fließt
herzu
zu-
wahrscheinlich arm.  jur,  Gen.  jroy  ,Wasser'  {^g^hdöro-)] gr;  att.  cpd-slQix)  {*q)d'SQia}',  lesb.  q)&8QQü},  ark.  (pd^iqqoj)),  schwachstufig  dor. (pd-aiQü)   (*q)&aQicü)   ,richte   zugrunde';    dazu    auch   g)d-6iQ  ,Laus'    (ipeigsc (pd-eiQSi  Hes.  ist  Folge  der  spätem  spirantischen  Aussprache  des  ^),  (pd'OQ&
488  f
^Verderben,  Vernichtung'  und  (als  Rest  der  älteren  Bedeut.)  ,Yerniischt oder  Verreibung    der    Farben',    ebenso    av^igj^sigo)    außer    ,zugleich   od« gänzlich   zugrunde    richten'    auch    ,lasse  Farben   ineinanderfließen',   da^ auch    ^verschmelzen,    vermischen    überhaupt',   avi.icpd-siQeadai   ;Zusaminei2 strömen'.
WP.  I  700,  Schwyzer  Gr.  Gr.  I  326,  714,    Benveniste  BSL.  38,  139  £
g^hedh-  , bitten,  begehren'.
Av.  jaiöyemi,  apers.  Jadiyämiy  ,ich  bitte';
gr.  Aor.  d-saaaad'ai  {*gVihedk-s-)  ,anflehen',  Partiz.  -d^satög  in  dnö^eavog ,verwünscht,  verschmäht',  Ttolv-d'sarog  ,sehr  ersehnt',  Pers.-N.  Oeö-S-earog böot.  0LÖ-q)SLarog]  ftö&og  m.,  tto&i^  f.  ,Sehnsucht,  Verlangen',  nod-m  ,er. sehne,  vermisse  schmerzlich,  verlange';
air.  guidiiL  ,bitte'  (=  nod-io}),  Perf.  1.  Sg.  ro-gäd,  s-Konj.  1.  PI.  gessam (usw.);  geiss  f., Verwünschung, Tabu'  {*gViedh-ti-s)]  guide,G ehet^ {*g^hodhia)'^ foigde  ,BetteW  (^uo-gediä) -,  cjmr.  gweddi  , Gebet'  (*uo-godlma) ;
lit.  geddu-ju,  -ti  ,sich  sehnen,  sehnsüchtig  suchen,  verlangen,  wollen', gedü  (und  gedziü),  gedeti  ,sich  sehnen ;  traurig  sein,  trauern' ;  Nasalpräsens pasigendü,  -gedaü,  -gesti  ,sich  sehnen;  etwas  vermissen',  ablaut.  Kausat. gadmti  ,verderben,  stören',  daher  sekundär  der  ö -Vokalismus  (statt  uo) von  gödas  ,Gier,  Habsucht;  Klette',  godits  , ha
```


## [2026-09-06T14:54:03.473Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== KLN cravat ===\"; grep -n -i 'cravat' KLN_1966.txt KLN_1971.txt | cut -c1-400 | head -20; echo \"=== KLN Croat ===\"; grep -n -i 'croat' KLN_1966.txt KLN_1971.txt | cut -c1-400 | head -20"
}
```


### [2026-09-06T14:54:03.574Z] TOOL RESULT

```
=== KLN cravat ===
KLN_1966.txt:9579:cravat,  n.  —  F.  cravate,  fr.  Cravate,  ‘Croat,  Cro¬ atian’,  and  lit.  meaning  ‘neckcloth  worn  by the  Croats’,  fr.  Serbo-Crotian  Hrvat,  ‘Croat’,  fr. OSlav.  Chtirvatinu;  originally  meaning ‘necktie after  the  Croatian  fashion’.  See  Croat. Derivative :  cravat,  tr.  and  intr.  v. crave,  tr.  and  intr.  v.  —  ME.  craven,  fr.  OE. c
KLN_1966.txt:9710:‘forest’  and  prob.  also  with  Gk.  pop £&?,  ‘north wind’,  lit.  ‘a  mountain  wind’.  See  Boreas  and cp.  cravat.
KLN_1966.txt:36680:steenkirk,  n.,  a  kind  of  lace  cravat.  —  Named from  the  battle  of  Steenkirk,  in  Belgium  (1692). steep,  adj.,  precipitous.  —  ME.  stepe,  ‘steep’,  fr. OE.  steap,  ‘lofty,  tali’;  in  gradational  relation¬ ship  to  stoop  and  stoup  (qq.v.)  Cp.  steep,  ‘to soak’,  steeple.
KLN_1971.txt:59238:cravat, n. — F. cravate , fr. Cravat e, ‘Croat, Cro- 
KLN_1971.txt:59246:Derivative: cravat , tr. and intr. v. 
KLN_1971.txt:60155:cp. cravat. 
KLN_1971.txt:231703:steenkirk, n., a kind of lace cravat. — Named 
=== KLN Croat ===
KLN_1971.txt:19079:Serb., Croat, rdda ‘stork*, ON. arta, OSwed. 
KLN_1971.txt:25415:ban, n., a governor of Croatia. — Serbo-Croatian 
KLN_1971.txt:28074:Serbo-Croat, bldzina (for *bolzina), ‘pillow’, 
KLN_1971.txt:31520:Croat. blaiina (for *bolzina), ‘pillow’. See belly 
KLN_1971.txt:31973:in Hyperborean. Cp. also Croat, 
KLN_1971.txt:32053:Serbo-Croat, brzo, ‘quickly’, and cogn. with 
KLN_1971.txt:51646:Croatian govoriti, Czech hovoriti , Slovak hovorit', 
KLN_1971.txt:59238:cravat, n. — F. cravate , fr. Cravat e, ‘Croat, Cro- 
KLN_1971.txt:59240:the Croats’, fr. Serbo-Crotian Hr vat, ‘Croat’, fr. 
KLN_1971.txt:59242:after the Croatian fashion’. See Croat. 
KLN_1971.txt:60146:Croat, n. — Fr. earlier Chorwat , fr. Serbo- 
KLN_1971.txt:60147:Croatian Hrvat , fr. OSlav. Churvatinu, ‘Croat’, 
KLN_1971.txt:60150:Croatian gora, Russ, gora, Pol. gdra, Czech and 
KLN_1971.txt:60157:Derivatives: Croat-ian, adj. and n. 
KLN_1971.txt:68459:Serbo-Croatian depam, depat i , ‘to thrust, strike’, 
KLN_1971.txt:76317:Pol. drapac, Serbo-Croat, drapati, ‘to scratch, 
KLN_1971.txt:84998:dimin. ertla , ‘wagtail’), Serb, and Croat, roda , 
KLN_1971.txt:117099:Serbo-Croatian gusar, husar, ‘pirate, bandit’, 
KLN_1971.txt:132092:to Pol. kolacz, Serbo-Croatian kolac, Church 
KLN_1971.txt:132283:(dernyj), Serbo-Croatian cm, Czech cerny,
```


## [2026-09-06T14:54:06.603Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '60144,60160p' KLN_1971.txt; echo \"=== 1966 croat entry ===\"; sed -n '9705,9715p' KLN_1966.txt"
}
```


### [2026-09-06T14:54:06.725Z] TOOL RESULT

```
adj. and n., croak-y, adj. 

Croat, n. — Fr. earlier Chorwat , fr. Serbo- 
Croatian Hrvat , fr. OSlav. Churvatinu, ‘Croat’, 
lit. ‘mountaineer, highlander’, fr. churva, ‘moun- 
tain’, which is rel. to OSlav., Serb, and 
Croatian gora, Russ, gora, Pol. gdra, Czech and 
Slovak hora , and cogn. with OI. girth, Avestic 
gain, ‘mountain’, Alb. gur, ‘rock’, Lith. gire, 
‘forest’ and prob. also with Gk. Poplaq, ‘north 
wind’, lit. ‘a mountain wind’. See Boreas and 
cp. cravat. 

Derivatives: Croat-ian, adj. and n. 
crocein, croceine, n., any of several yellow and 
red dyes ( chem .) — Formed with chem. suff. -in, 
resp. -ine fr. L. croceus, ‘saffron-colored’, fr. 
=== 1966 croat entry ===
critic,  n.  —  L.  criticus,  fr.  Gk.  xpmxoi ;,  ‘capable of  judging’,  fr.  xpiTTjt;,  ‘judge’,  fr.  xpfveiv,  ‘to separate,  decide,  judge',  which  is  cogn.  with  L. cernere,  ‘to  sieve,  distinguish,  discern*  under¬ stand,  decide’.  See  certain  and  cp.  crisis,  crite¬ rion,  diacritical,  hypocrite,  oneirocritic. Derivatives:  critic-al,  adj.,  critical-ly,  adv., critical-ness,  n.,  critic-ism,  n.,  critic-ize,  critic¬ ise,  intr.  and  tr.  v.,  critic-iz-er,  critic-is-er ,  n., critic-iz-ing-ly,  critic-is-ing-ly,  adv. critique,  n.  —  F.,  fr.  Gk.  xpirixf)  (short  for  *xpi- tl x>,  te/vtj,  ‘the  critical  art’),  fem.  of  xpirixo?, ‘of,  or  for,  judging,  capable  of  judging’.  See critic.
croak,  intr.  and  tr.  v.  From  the  stem  of  OE. crac-ettan,  ‘to  croak’,  which  is  rel.  to  OE.  cra- cian,  ‘to  resound’,  OE.  crawan,  ‘to  crow’,  ME. creken,  ‘to  croak’.  All  these  words  are  of  imita¬ tive  origin.  See  raven  and  cp.  Circaetus.  Cp.  also crack,  crake,  creak,  crow,  grackle.
Derivatives:  croak ,  n.,  croak-er,  n.,  croak-ing, adj.  and  n.,  croak-y,  adj.
Croat,  n.  —  Fr.  earlier  Chorwat,  fr.  Serbo- Croatian  Hrvat,  fr.  OSIav.  Churvatinu,  ‘Croat’, lit.  ’mountaineer,  highlander’, fr .chitrva,  ‘moun¬ tain’,  which  is  rel.  to  OSIav.,  Serb,  and Croatian  gora,  Russ,  gora,  Pol.  gdra,  Czech  and Slovak  hora,  and  cogn.  with  OI.  girth,  Avestic gain,  ‘mountain’.  Alb.  gur,  ‘rock’,  Lith.  gire,
374
‘forest’  and  prob.  also  with  Gk.  pop £&?,  ‘north wind’,  lit.  ‘a  mountain  wind’.  See  Boreas  and cp.  cravat.
Derivatives:  Croat-ian,  adj.  and  n.
crocein,  croceine,  n.,  any  of  several  yellow  and red  dyes  ( chem .)  —  Formed  with  chem.  suff.  -in, resp.  -ine  fr.  L.  croceus,  ‘saffron-colored’,  fr. crocus,  ‘saffron’.  See  Crocus.
crochet,  n.,  a  kind  of  knitting  done  with  a  small hook.  —  F.,  ‘a  small  hook’,  dimin.  of  croc, ‘hook’,  which  is  a  Teut.  loan  word.  Cp.  ON. krokr,  ‘hook’  and  see  crook.  Cp.  also  crotchet, crocket,  and  accroach,  encroach.
Derivatives:  crochet,  tr.  and  intr.  v.,  crochet-er, n.,  crochet-ing,  n.
crocidolitc,  n.,  a  blue  or  green  fibrous  mineral, consisting  of  silicate  of  iron  and  solium  (mine¬ ral.)  —  Compounded  of  Gk.  xpoxu?,  gen.  xpo- xiiSo?,  ‘a  nap  of  woolen  cloth’,  and  X1&05, ‘stone’.  The  first  element  is  rel.  to  Gk.  xpAxrj, ‘woof,  thread’,  stands  in  gradational  relation¬ ship  to  xpexsiv,  ‘to  weave’,  and  is  cogn.  with OE.  hreol,  ‘reel’,  hrxg(e)l,  ‘garment’,  ON.  hrtell, ‘a  weaver’s  sley’,  fr.  I.-E.  base  *qrek-,  ‘to  strike’. See  rail,  ‘garment’,  reel,  ‘a  revolvable  instru¬ ment’,  and  cp.  next  word.  For  the  second element  see  -lite.
```


## [2026-09-06T14:54:22.726Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'NR>=9540 && NR<=9600' KLN_1966.txt | grep -n '^[0-9]\\{3\\}$'; echo \"---\"; sed -n '9570,9585p' KLN_1966.txt | cut -c1-300"
}
```


### [2026-09-06T14:54:24.512Z] TOOL RESULT

```
---
Crassulaceae,  n.  pi.,  a  family  of  herbs  (bot.)  — Formed  fr.  prec.  word  with  suff.  -aceae. crassula ceous,  adj.  —  See  prec.  word  and  -aceous. -crat,  combining  form  denoting  ‘a  supporter’  or
Crataegus
dQD
‘member’  of  a  certain  type  of  government,  as  in democrat.  —  F.  -crate,  fr.  Gk.  -xpdrr t]z,  fr. xpxxcx;,  ‘strength,  power,  rule’.  See  -cracy. Crataegus,  n.,  a  genus  of  plants  of  the  apple  family (bot.)  —  ModL.,  fr.  Gk.  xpaxaiy °?>  ‘thorn’, which  is
cratch,  n.,  crib,  rack.  —  ME.  crecche,  fr.  OF. creche  (F.  criche),  fr.  Frankish  *kripja,  which  is related  to  OHG.  krippa,  OE.  cribb.  See  crib  and cp.  cradge,  crbchc.
cratch,  tr.  and  intr.  v.,  to  scratch  ( obsol .)  —  MDu. cratsen,  rel.  to  OHG.  krazzon,  ‘to  scratch’.  See scratch.
crate,  n.  — -  L.  cratis,  ‘wickerwork,  hurdle’,  fr. I.-E.  base  *qerat-,  *qert-,  ‘to  roll  or  twist  to¬ gether’,  whence  also  L.  crassus,  ‘thick,  solid, dense,  fat’,  OI.  kptsnah,  ‘complete,  whole’, Russ. -Church  Slav,  cristvu,  cirstvu,  ‘firm,  solid gen
crater,  n.  —  L.  crater,  ‘a  large  bowl  for  mixing wine  and  water’,  fr.  Gk.  xpatrip,  which  is  rel.  to xpaatc,  ‘a  mixing,  blending’,  xepawuvai,  ‘to mix,  mingle,  blend,  temper’,  axepaaTO?,  Sxpa- -ros,  Ion.  SxpTjxoc,  ‘unmixed,  pure’,  fr.  I.-E. base  *ke
crateriform,  adj.,  crater-shaped.  —  Compounded of  crater  and  L.  forma,  ‘form,  shape’.  See  form,  n. cratometer,  n.,  an  instrument  for  measuring power.  —  Compounded  of  xparo;,  ‘strength, might,  power’,  and  pixpov,  ‘measure’.  See -cracy  and  meter,  ‘poeti
cravat,  n.  —  F.  cravate,  fr.  Cravate,  ‘Croat,  Cro¬ atian’,  and  lit.  meaning  ‘neckcloth  worn  by the  Croats’,  fr.  Serbo-Crotian  Hrvat,  ‘Croat’,  fr. OSlav.  Chtirvatinu;  originally  meaning ‘necktie after  the  Croatian  fashion’.  See  Croat. Derivative :  crava
Derivatives:  crav-er,  n.,  crav-ing,  adj.  and  n., crav-ing-ly,  adv.,  erav-ing-ness,  n. craven,  adj.,  cowardly.  —  ME.  cravant,  ‘beaten, vanquished,  overcome’,  fr.  OF.  cravant,  pres, part,  of  craver,  crever  (F.  crever),  ‘to  crack, break,  burst’,  fr.  L.  crepare, 
Derivatives:  craven,  n.  and  tr.  v.,  craven-ly,  adv., craven-ness,  n.
craw,  n.,  the  crop  of  a  bird.  —  ME.  era  we,  rel.  to MLG.  krage,  MDu.  craghe,  Du.  kraag,  ‘neck, gullet;  collar’,  MHG.  krage,  of  s.m.,  G.  Kragen, ‘collar’,  and  prob.  cogn.  with  Gk.  Pp^x-do.;, ‘throat’,  £(3po£s  (aor.),  ‘he  swallowed  up’, lipAy/o?,
Derivatives:  crawl,  n.,  crawl-er,  n.,  crawl-ing, adj.  and  n.,  crawl-ing-ly,  adv. crawl,  n.,  an  enclosure  in  water  for  turtles.  —  Du. kraal.  See  kraal  and  cp.  corral, crayfish,  also  crawfish,  n.  —  ME.  crevise,  crevis, fr.  OF.  crevice  (also  escrevice,  whence  F. 
I
I
```


## [2026-09-06T14:54:33.286Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== SNS leaves ===\"; awk 'BEGIN{RS=\"\\f\"} END{print NR}' SNS_pages.txt; grep -n 'gar' SNS_pages.txt | grep -i 'mountain\\|kūh\\|kuh\\|کوه' | head -20"
}
```


### [2026-09-06T14:54:36.373Z] TOOL RESULT

```
=== SNS leaves ===
242
```


## [2026-09-06T14:54:39.966Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'));print(json.dumps(d['SNS'],ensure_ascii=False,indent=1))\"; echo \"=== grep gar ===\"; grep -n '\\bgar\\b' SNS_pages.txt | head -20"
}
```


### [2026-09-06T14:54:42.445Z] TOOL RESULT

```
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
=== grep gar ===
4813:                                                                                                                                                    /: bUland gar:
7296:                                                                                                                             -«&) ,^/jl-          :fww> «/(gar: ^5 + Jui                                      u
7819:                                                                                                                   "Wlinb i gar:
8568:                                                                                                                                                        •/ :-kar/- gar:                 «^
12487:                           *v. *w •**-«*-                                                                                                                .AJj/.i/ftJi ,*£ ./:gar:                           Jj
12566:                                                                                    {Aiifb. 516)garhate: 1^#Sjj-» .cv&i .*J? :gar»z-                                  :     fc_           Id
16215:                          gar 318/19                             goharldan 327/2          gOz 330/4
16217:                          -gar/kar 212/10                        gohr 326/18              gragtar 320/2
16400:bavandag 110/11          bOxt 105/23                     buland gar 104/16        casisnlh 157/7
```


## [2026-09-06T14:54:47.880Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '12480,12495p' SNS_pages.txt | cut -c1-250; echo \"=== 4810 ===\"; sed -n '4808,4818p' SNS_pages.txt | cut -c1-250; echo \"=== 7815 ===\"; sed -n '7815,7825p' SNS_pages.txt | cut -c1-250"
}
```


### [2026-09-06T14:54:47.950Z] TOOL RESULT

```
                               \   .   *a   -.-a. . ^-,15;qrantar:
                                                                            V^                       \A/r^        .^yf^L,^^ rpakih:
                                          ******                            -•o*   X                                                                     *
                                                                                                                                                                              ,yh:>A:       -*o-0-^j


      ,   T/A 4   (
                           *v. *w •**-«*-                                                                                                                .AJj/.i/ftJi ,*£ ./:gar:                           Jj
                                                                                        IY/V14        (4iJ/fc. Ill, 513-14) giray-offSj-^                                         gairi-: £»                      Xo



                                                                                                                                                                     .c**-Jt4:draxt:                  yiJ*X»

                                                                                        {Mir. Man.                drxt          :        >=t {GNPE. 121) *                   draxta-             :   fc.

=== 4810 ===
                                                                                                                                                -^>*.;buland               :   t       IIf   48)
                                  f/\y^ •t\-t\/\r-s -yi-y
                                                                                                                                                                                       ^^
                                                                      •
16
                                                                                                                                                    /: bUland gar:
                                                                                                                          «*•*«. II,       ^>'?'
                                                                  •n/lo^
                                                                             .!*/»•**
                                                                                         IT/I**    .*!, (t)

=== 7815 ===
                                                              i_   cum:
                          j . -,ii   * «s ^'-m ^j* **•


                                                                                                                   "Wlinb i gar:
                                                                                                                                                          £
 ,   •
         ae ^***«** ** p ************  *
                                                                                                               *                                   \,
                                                                                                                                                        ^
                                                                                                                             •J^'randar: BYK:                 y-.   *>
```


## [2026-09-06T14:54:52.834Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n 'gairi' BRT.txt | cut -c1-300 | head -20"
}
```


### [2026-09-06T14:54:52.930Z] TOOL RESULT

```
2452:—  paoiryö  gairis  kamMStat  .  .  paili  aya \zjmä  Aaraiti  6ari  Yt.  if/.i;  lo.gS,  tj.gy, I*V.<).IS,  V.5.4,  7-^54. '*Y./2.3;  —  raikö '  (sd.)  .  .  haca  ariAs  (als  Abi.))  ztmat  . , |Yt  77.30; —  II  xi'äya'hiyt^  aAyäyä  bumiyä 1  D,(?.2,  X./.I,  A0.2,  Am./,j;  
2461:—  ahmi  atskvö  yat  astvainti  V,  5.  Sprecher  vorgeschwebt:  jaji-a..  7rfJ»aVfl/ 39;  —  ai^hS  zimo  yat  faianaya  Yt  w.  poHbm  hl  matw  .  .  nöit  zT  ahmi  paiti 95;  — ■  anhqm  dämanqm  yat  ahurake  .  ..nairi  .  .  V.  7.51  f.;  _j.zi;  —  ^aei  iskata dätaras
2472:dalvil  . .  atibyö  kam  Y.44.20;  46.12;  — li  narS..aeiqm  nmäna  Yt.i~.yC;  g— 14.^, J0.39f.s,  33,Y./j.3,j7.37,Vr.//.i9,V.2, 43-J.i4,Ä4i,  12.1, 13.50,  i5.22,FrV/. 10. 40,  N.<S'5; — g3ui..ya  dar>nlhu  mi^rS.- drujqm  ..frazarsta  (sd.)  aglqm  rai'iya  .. hiit»nte  Yt. /o.  3
3819:•  j.  aiwitay-  f.  'Hinzugehen,  Begehen,  Be- steigen': ya^qmca  par3  masySka  'la^a^a spasitaiiaca  gairinqm  nämqm  dülarv  "und die  (anderen)  Berge,  welchen  früher  die Menschen  Namen  gegeben  haben,  vom Begehen  und  Betrachten  her  (sie  nehmend)" YL/ii,6'>.
3824:von  — ':  gairis  yS  usioä  yim  aiw'  faoiril äps  hqm  .  ,)asint9  ". .  von  dem  ringsher die  vielen  Wasser  zusammenkommen"  Yt. ig.66.  2)  'ringsherum—':  ußa  iainm
4167:•  j.  gairi.masS  ashö  '*  aitahe  V,  5. 9 PUZ.:  -?-.
5203:•  j.  avi,  aoi  I)  Praen.  1)  mitAkk.;  a)  'auf —  zu,  hin  zu  —  (auf  — ),  advcrsus',  a)  bes. bei  Wörtern  der  Bewegung:  tiltrim  . .  yö .  .  vazsite  'i-i  zrayS  .  .  ya>a  tifrii  yim anhat  irsxsö  .  .  airyd.x^ii>a(  ka>a  garöit x^anvanhtn  'vt  gairjm  YL�
5383:•  j.,  g-  auruna-  'wild,  fenis,  saevus': maSsahe  kihrpa  'na^e  Yt.  l4- 23;  —  'na/a gairisiicö  sizdraca  ravascarätö  "die  wilden (Tiere),  die  in  den  Bergen  hausen,  und die  scheuen,  die  in  den  Ebenen  streifen" Yt.  ^36;  —  alityS  mos  aia  syasdal{sA.) yavaf  a
5458:•  j.  arsSa-,  p.  arda-  i)  Adj.  'halb' (nur  Komp.).  2)  m.  'Seite':  *atitar?m (sd.)  'tijm  mayaAe  V.p.29;  —  antar?m 'fam  nmanaheV.6.i,y,  — dasinim  (vair- yastärtm)  hl  upa  "htm  Yt.  10. 100';  — visps  he  upa  'wun  (lies  -o!)  \tio.ioo; —  äasimm  hl  'Öe..  A
5552:/nlyatayat 'yama  yJ  ilyö  gairim  avi  spjiitJ.-  °'^aj  haca  garsit  ^anvant>m  ai-i  guirtm frasnti  V.  22. 19;  ao;  —    äa^  mqm  tum  Yt.<K6.
6476:•  j.  ast^Ina-  Adj.  'der  achte':  °mB  {gairis) Yt.  ig.  2;  V.  14.  9,  Yt.  ;.  7,  i4-  a3;  — °mjm  asarfhqmüa  .  .  V.  i.  10;  4.  20,  5. 28,  29.  a)  ASn.  als  Adv.  "beim  achten Mal':  'mfm  V.<¥.  77.
7279:charakterisirenden  Adj.  (sd.,  auch  fdSt.): vispasca  äpS  yazamaide  ya  z)m3  armaesta (sd.)  *fratat.ear3tasca  (sd.)  *xqnyk  '^raots.- stälasca  par^uya  *v3iryäsca  (sd.)  "alle Wasser  auf  der  Erde  . , :  die  stehenden  und fliessenden,  die  in  Quellen  und  in  Fluss- laufen
7635:•  j.  3r9x§a-  a  £N.  eines  berühmten iranischen  Schützen**:  tiyris  . . y'im  anhat °sS  xi-vitui-Uus  xsviwi.iivaiimd  airyanqm airyö^stii:at  haca  garSit  ^anvantain  avi gairim  "der  Pfeil  , .,  den  der  PfeilschUtze if.  schoss,  der  beste  Pfeilschütze  der  Arier, vom 
8721:•  j.  uäi.dam-,  u§i-dain-  tn.  Name  eines Gcbirgs*':  ahmat  haca  garayS  fraoxiyan '0.1  (NS.)')  usi.äar?nd  {i±)  Yt/^.a;  — gairis  yU  °6<j  Yt/p-66;  —  aom  gairuii.. yim  °dam {fuS.y*  usi.darfmm (sd-)Mt.  1.2S.
10224:•  j.  garay-  :  gairi-  m.  'Berg,  Gebirgszug, Gebirg"':  -rayi^^^.)  b^nzantB  Ytio.  14; ig.z,  7,  8,  16.  3;  —  'rayd  (als  AP.)"  aSa- ^ä^rä  Y.2.14;  /0.3,  7/.  10;  —  'rayasca (als  AP.)  ySi  hrnaniö  Yty.  9;  —  ma- sits  Urli{AP.)  Yt.j4.4ii  —  bar^dstaiibyö '
10228:ig.  i;  6',  66;  —  'rsU  ^uHjIar^nahe  Y.i. 14,  22.36;  Ny.5.  5,6,  FrW.5.  i;  —  airyB.- xs'uiai  haca  'rsit  :^anvant»m  avi  HrXm Yt5.6;  i.zZ,  5.4s,  &33,  Y.2.14,  Ny./. 8,  V.  22. 19,  S.  2. 9';  —  *aoi  spitagaona (sd.)  Hri  (AP.)  4>  Y.  jo.  1 1 .  [FrBy. :  lies g
10236:•  j.  *gairi.b9r9z-'>  f. 'Bergeshöhe,  -tiefe"': ''snu.b^Kö  n3rf.b3r3zS  °zd  mänö(sA.)  FrBy.
10238:•  j.  gairi.masab-  Adj.'*  'von  der  Grösse eines  Bergs';  °s!J  aahB  (sd,,  Sp.  iio  m.) aetahe  V.5.9  PüZ.
10240:•  j.  gairi-äak-  Adj.  (auch  fem.)  'was  mit den  Bergen  zusammen,  in  ihnen  heimisch ist':  aurunaca  (sd.)  "iJÄJ  (NPm.)  siidraca ravascaraid  Yt.  Ä36;  —  paotris  3pB  .  . '/äcB  (NPf.)  Yt./p.66.
11356:paitis  , .  zbayeiti  . .  yim  *driyBsat  . .  sba- yäti  Yt  10.  84;  —  %wqm  yazSnte  .  .  dai- AAu.paiays  . .  '^wqm  naraHt  ySi  taxma Jai'jyhnte  Yt  5.  85  f;  —  haraiti  bars  .  . kä  Aama  päirisSite  frSpayä  (sd.)  . ,  M3r?- fiaaS  gairis  . .  AämS  hasHt  päir
```


## [2026-09-06T14:54:59.058Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n 'jzar\\|yzar\\|gzar\\|xzar\\|ž ar\\|zarayeiti\\|zaraiti' BRT.txt | cut -c1-300 | head -20; echo \"=== xsar ===\"; grep -n 'x§ar\\|xšar\\|xsar' BRT.txt | cut -c1-200 | head"
}
```


### [2026-09-06T14:54:59.150Z] TOOL RESULT

```
5754:•  j.  asö.söidra-  n.,  Plur.  'Stätten  und Wohnplätze'(?)":  kaia  xi..  yzarqm  atwi- yzanm  srirasca  'rasca'>  gaoyaoiliS^a  ilta- cin/ls  (sd.)  YtÄ42.
10467:5*9  'grab-  Noten  —  yzar-  mit  aiwi  530
10525:•  j.  yzarfl-yzarant-  Adj.,  PPA.:  s,  -fiar-.
11733:manS,  vehu  manS  taj  vanaiti  Yt. /p.  96;  jA'w.;  hazannm  azinqm  .  .  ava.janyät .  . —  parä  .  .  *daiahSui  anhat  b?r3t5  (sd.)  ■  "hrisattm  frascimbananqm  frasHmbaySit ..; vSstrvm:  ttm  {ah  ASn.)  aß paurvavazai-'tat  aiAhe  aiti  paititil  tat'  ..V.  18.1  ^Z.; lyai
22809:•  j.  'varah-  n.  'Probe,  Prüfung,  Ordal'*': urvdhqmcit  (sd.)  zbayem  avi  imai  TS uzdatTm  aviätnmca  bargsmäca  avipfnnqtn vjyzarayeintTm  avi  raoynyqm  varauhsm (sd.)  aeui/rmca  urvaranqm  ".  .  zu  dem hier  angestellten  Ordal,  zu  dem  Feuer  und Bansman,  zu  der  Uberfl
=== xsar ===
```


## [2026-09-06T14:55:02.141Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '10460,10540p' BRT.txt | cut -c1-400"
}
```


### [2026-09-06T14:55:02.232Z] TOOL RESULT

```
girsmyäi  N.  105;  —  '^pgr^gtr^ptayat  Nik.  j.]
mit  frä  i)  'ergreifen':  mürpin  .  .  y?>ihe ..bäzava  fragrnvmti^''''  (stattDu.)  "»nürg.- aojattAs  (sd.)  Yt.  10. 104.  3)  'annehmen, entgegennehmen':  ßra  atnisH  spmts  gJ^ii giurväin ' sl  Y. 2S.0.      fragSun-ayat Vd.  13.
mit  «r'aufstemmen' :  kakat  n  ig>  r?pta  ii  - bya  päsnaiibya  urg>r3ptalibya{%^^  angus- talibya  V.S.ji;  70,
mit  Aam  i)  'zusammenfassen,  -raffen': javat  cvatca  kl  zastaübya  Aangpunayqn "so  viel  sie  nur  davon  mit  den  Händen zusammenraffen  können"  V.  (/.ag;  — yä *dvalibya  »rpziibya  *  kangirTtvnat^''^  N. 6^.  2)    'erfassen,    erhaschen':     aitat
x^anns  kaiigpr^fsäiie  Yt./p.47,  51  (wo grif"');  —  t?Miil  mi'irS  hangr»fs)mnS *pairi.apaya  (sd.)  bäzuwe  Yt.  lo.  105; —  aom  :^armS  hangSurvayala  Yt.  i(). 35.  a)    mit    den   Sinnen:   yat    '^wä
hsm  casmainJ  (sd.)  hSngrabatn^''''  Y. _ji.8.  3)  'aufnehmen  (in  sich)': /ra/(7- rsmcit  . .  Aavartpm  (sd.)  .  .  yd  qsits  *Aan- gSuri'ayeie''*'^  Y.10.2.  4)  'in  seiner  Ge- walt haben,  halten',  sva.  'lenken',  den Wagen:  yeAke  viis»m  hangr^vnäiti  .  .  Yt. io.  68,  143.
dby  Google
5*9  'grab-  Noten  —  yzar-  mit  aiwi  530
ti.  a^abham,  sfhh<fäü{,  Pä.  ghtppaiil),  grhhä-  •  ,  j.  ''^fralbaoye  bale  buyetite  v&ibaoye  grafe yäH,  ^bkäyataak,  ^kyäic  (Pass.),   vgl.  präkr.  ■  *„„«/«"   Vt  /■;  ?2
ox      -   .:-.     Jli            Tl.-           ,-,     ,„1                t  '  Angebl.   'Kerkenneisler     (öP.)   oder  'Kerker
28},  ginflan^9\    —    Pü.;  giiflaa^'il;    s,  noch  i  Ji..ot.|V
Ko,  6,  7,  9,  II,  16.    —    ')   Darür   auch  ^ri- \  'J'-sti>
geschr.;  S  i^^S.  39.  —  »)  S  5J  H.  —  3)  Stall  [  j-  .f™":  s.  unter  ^grab-.
KT'  ^-^^^^l'  ^'  «'xf*-  5^'«p~  •  ß-  *gr5hma-'>  m.  EN.  eines  Wider- ^'  S  330  b  mit  No.  l.  —  i)  Them.  —  6)  Pu.:         X.       ° ,        7       -,     >,  t   ,         .       r    ■
/a  «4iö»a  /fl«rf  J»  y/zy  u'-Klrii.  -  3)  Hds.   sachcrs  des  Zara^uitra:  ahya  'mS  H.htt-
j^^z-Ä»«;  S-Pü.  — 8)  Fl;  NA.  al'a.  — 9)  Pü.:  >^I    (sd.)    ..    xrotSS    ttl    dadüt  \.  32.  \\-,
fehlt  —  '<»)  S.  amirtxlay-  No.  —  ")  Pü,  er-  *Y.2l');  —  yä  X^a'^irü  'mS  klsasat  (sd)
ginit  vfljfrfl*.  —  i>)  Po  Kao  lu  H.2.26.  -  y.  22.13.        *)  Plur.  sva. 'C/-.  und' seine
M)  Jp  I,  Mfi;  ftUB  (NA.)  ist  der  Bedeutung  ,   •*        "^     -       .    ,         ,.1
nach    unmöglich.    —    u)  -avari   statt    'winli  Leute,    sein    Anhang  .>>:7.Tm     -m3     asat
lum  Praes.  17,   vgl,  unter  hindav  No.  1.   —  varaiä  karapä  xsainmc,!  isanqin    drujim
>i)   D.  L  'äyiit,  %  268.  21.   —    '6)  Unsicher,  "von    denen    Gr.    und    dessen  Anhanger
",** V  W"^  mV  '^'^'{'l'-'    ^^■':  ■''^^^-  ~    dem  Aia   vorgezogen   werden   (und)    der
17)  Nach  dem  Metrum  ist  *j»  lu  streichen.  —     „         j    j'     it  l   li  j  j-     j        r^
>8)  PI  4.  -  .«  s.  daiu  Bthl.  wklPh.  1898. !  -^-  '^nd  die  Herrschaft  derer,  die  der  Dr.
1060.  I  nachstreben"  Y.J2.I2*'.
.     ,        ,      .,„  ,,,..  El.?  Ar.  "gljiyaima-  \%  2gS.  1  c)  oder  'nrisr/ia-,
.   j,    'grab-    (Fassung  uzw.  von  Wortern,        _  p^..  t„nsskr.,    erL.:  /.Fw-f  'Geschenk.  Be-
sva.)    Satz';     drija^he    (sd.)    aiwi'joiUsca        stechung';  Sü.;  ÄiSoi'Oeschenk',  s.  diiu  Justi
(sd.)  gravasca   (AP.)'»   md^rahe   "um   zu       PrJ.  88.  247;  vgl.  noch  No.  4.  —  ■)  So  Pt  4
bewahren  die  Wörter  und  Sätze  des  M."  :     ^l  ^^4:7^; j,7k.  ^Isl'iof  v^S.  i  IS
i-9-3b.  _  4)  Pü.;  öiän  ^ahmak  kac  a/ir.iiiA  döSailat
Zum  V.  grai->).—  ai.  vgl.  ^t-M-  f.  'GrifP.  — .  i^  iat/  h<nä..i4  ^.''sfjUh  x'ähiad pa  drS'Jhi. Pü.!    an  i  dräi   a/ar  rawisiiiA  isle pa  mänsr;,
da»  Wort  fehlt  also;  aber  So.:  dli-gkam  .•  j.  grivä-  f.  'Nacken'  UZW.  (fofflTScher u/if/iapravraim  yävai  gfüio 'd mäniAravJttyä.  Wesen":  atfZBraAe [s,A.)  "i-aj-a  (LS.)  V.J.7. —  '>  S  ^^S.  37.  I      ii.gräia-i.;mp.l^ä.)grhai,Tt^.sar7va'iiä^t\',
.  j.  rran«.  Adj.  PPfP.  s.  V--         |    °3%Tjg'',;rSöS''b»r' b""''-
•  j.  gram-  V.  'erglimmen,  Grimm  hegen'. ;     "  I"»  Gegens.  lu  manueSfi-,
Praes.  1  grama-.  —  PPiT.  ^rnw/a-"',       |  »j.  yzrid-V. 'fliessen,  wallen',  vom  Wasser;
yr  manS  bara  gramfntam  "weg  schaff  i  nur  mit  Praev.     Praes.  30  (Kaus.)  yxra- den  Anschlag  derer,  die  (uns)  grimm  sind"   iaya-.
\,f).2Z;    —  mi^rS  graiits  upa.tbHtd  YL  !      niit  ä  Kaus.  'aufwallen  lassen':  hg srayS ro.'iS,  19,  39,  43J  23,  98,  \o();  —  ahurahe  ^•rii'iaydli  Yt.Ä3i. (näml.  niii-rahe)  grantahe'^l.i0.i>ii,^%-,\      mit  i'f  Kaus.   'auseinander,  tiberwallen —  varäsahe  ..  grantahe  Yt. /^ig.  lassen':  Jt3  zrayo  viyzr.ioayeiti  Yt.Ä3i,
mp.  ä-granä-lum  Dk./.  6.  7  (West:  'the  most !      -prod- :  izar-  (sd.)  =  gr.  il^l-io  :  ai.  fi-par.d;
horrid');   vgl.  np.  taram  'Grimm',  ahd.  g>-am\      %  48-
■      ■        —       ■  'nmän^fatil.?,ii.:k<,,!am  \ ,  j.  yjar-  V.  'iÜessen'.     Praes.  4  fzära-, "  """""'  t^i   7  (Jnt)  yiari.yiar-,  2oyiaurv;  30  (Kaus.)
ie;    IF.    /.    70, r,  47-
•  j.  gramant-  Adj.,  PPA.:  s.  gram-.
•  j.  grava-"  m.  'Rohrstock,  Stock':  graom jytis^ii. .  nava.pixim  (sd.)  adrinjayHl  aom
•/z-lraya-.  —  Absol.  'ylär^m.
'fliessen,  strömen':  kma  x^  .  .  afam yiäram  (3PKA.)"  aiwiyiannn  (sd.)  Vt. S.^2.  a)  Kaus.  'fliessen  lassen,  pro- fundere': p^r.msbyö  (sd.)  paiti  yl(irayat.by5
1  paurva.nalmäX  (sd.)  ahe  gravahe  V.  ,  Yt  /j.  2.         A)  Int  'hin-  und  herfliessen, €f.  14.  '  auf  und  ab  wallen':  ti  kist.uiti  (sd.)  yzan.-
Ei.f  —  mp.'(Pü.)  grm<,  np.  7rtrr'.  —  ')  Oder   yiaroutJs    (IP.    als    NP.)    * antari.ar»o)m ■,^0«.  (S  268.  37);  ob  zum  V.  grab-t  .  -^rt/«,^^^  V.J.  19.
j.  gravaira  Y.  p.  26  r  s.  \grai-.  ,      mit  «yi/  'fliessen,  (dünn)flüssig  sein',  von
•  j.gravä'ratav- m.EN.  eines  Gläubigen:  <i"  frischen  Milch,  im  Gegensatz  zur fradatMaraAe-tlus  asaone"A^S  Fr.,  SoYmi  ^"^^^^^  Mi'ch:  aipi.yzaurvatam  .  . des  Gr.  .."  Yty.i23.  payaakqm  ¥.5,52.
Eig.  Bed.?    VgL  JusTi  NB.  507.  1      nüt  irnft  'herzufliessen':  s.  Absol.
dby  Google
S3I
/zar-  mit  a
xumba-
53«
mit  J  Kaus.  'aufButen  lassen':  ks  zrays äyiärayeiti  Yt. A3:
mit  vT  Kaus.  'Uberfl Jessen,  überfluten lassen':  As  srayS  viyiarayeiti  Yt<?.  3: —  yä  ümm  (sA)  pir^mm  kirsnaoili pfnnamSt  vJyzärayeiti  "die  . .  was  voll  ist Uberfliessen  lässt"  V.  22, 5 ;  —  aoi  ptnnqm vJyeärayeintlm  Yt5. 132, 12. 5;  V.i^.40.
Et.  gleichwertig  mit  ijcar-{ii.).  S.  auch  izräii-.
—  ai.  kfärali,  gr.  ^üpa;  s.  dam  Wn.  AiGr.
I.  241,  Bgu,  GrGr.J  ug.  —  Pü.  (lu  V.  32)-.
afic  äUnjäi  kunll,   (lu  V.  5.  19,  52,    ig.  40);
adadat,  lu  V.  5.  19  mit  der  &1.;  ^wr.  —
'>  S  joj.  7,  33S.
•  j.  yzarfl-yzarant-  Adj.,  PPA.:  s,  -fiar-.
•  j.  j-zärayant-  Adj.  (fem,  'yeinn-),V'PA,: s.y=a
KompE.
X.
•  j.  xao^a-  (,  p.  xauda-)  m.  'Hut,  Kappe Helm'.
KompEI.  —  woss.  xodä  'Mülie,  Hut',  arm LW.  xoir  'Kopfband';  s.  noch  Hbm.  AGr.  i iGo,  Bthl.  Stud.  3.  57;  falsch  FiCKVglWb.' 3.  89.
•  j.   xad-  V.,   nur  mit   vi  'auseinander quetschen'.     Praes.  2  xala-.
airihä  zimS  (sd.)  päsnalibya  vTspara aslaäbya   vixala  (aS.)  V,  2.  31;  32    (wo
Vgl.  ai.  khSdati,  np.  xäyad  'er  kaut';  %  136. S.  poch  Pü.  —  Pü.;  »padddt,  lies  a/xSsl.
•  j.  xa^vza-  m.  Bezeichnung  dessen,  der (aktiv)  Päderastie  treibt,  'pedicator':  iö daSvanqtn  'zS  .  .  xumbs . .  kü.näirls  "wer ist  ein  pedicator  .  .  ein  patkicus  . .  eine Hure  der  DaSvaT'  V.Ä31;  32.
Die  Bedeutung  ist  vermutlich  eine  übertragenfi wie  bei  xumba-  (sd.).  —  np.  xafj  'incubus, Alp',  s.  Hbm.  PSt.  s6-  Wie  ist  aber  die  iran. Grundform  anzusetzen  und  wie  das  z  (gegen %  38.  \  b)  zu  erklären?  —  Pü. !  ki  Jh(i<i xamizah  (Transskr.)  »  kt  devän  xumbak,  erl.; däfän  kär  i  narih  u  mälailh  ke  hinend.
•  j.  xan-  f.  'Quelle,  Brunnen':  xä  (NP.) aspS-stdoyehl^  apam  Vt.  Ä  5 ,  42;  —  apamui xä  (AP.)  Y..,^2.'i;  V.y.si;  —  xa  'paiti afrajyamna  Yt.  ;_J.  14^;  —  vupa  äp5  x'i paiti  '^raoid.siätascü  (sd.)  Y.  Ji.  9 ;  —  »nzöis (sd.)  xh  Ytj^ag;  —  m^rtzuca  (sd.)  xa u^tünahe  Yl  /0. 7 1 ;  —  frä  tl  hazat^rsin xqm  (GP.)  .  .  gaoiaiDin  (sd.)  av
heiligen  Rechtes  Brunnen  bist  du"  Y. 10. 4'>,
Ableit.  (s.  xqnya;  xayaria-].-^  Zum  ar.V.  ikan-  ? ;
E.  ^kan-  mit  No.  I.  —  ai.  ihaii-  f.  {ihi-);  mp.
(Pü.)  vyl.  x3h.  —  ■)  Vgl,  RV,  2.  28.  5;  ihdn
```


## [2026-09-06T14:55:11.468Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== HRN p.145 (NR 167) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==167' HRN.txt | head -50"
}
```


### [2026-09-06T14:55:13.213Z] TOOL RESULT

```
=== HRN p.145 (NR 167) ===
— 145 —
phlv. aj war, vergl. nniS': 11 TN in (Is. 1, 7).
LW. kurd. zhrl 'Heftigkeit, heftig' : af/. zahar ober-
halb* ; bei. zahr mächtig (293).
652. »erftn *Wunde, Schlag*.
aw. vergl. za/ya- *zu Tod gehetzt' (y. 53, 8,
Geldner, KZ. 28, 193, 202), zahJt (y. 60, 7); ai. [/jas-,
jasyata 'erschöpft, todmüde sein, Caus. ^erschöpfen ;
verletzen, tödten, schlagen (Dhätup.)*; phlv. za/^m
bezw. zahm.
Wenn die Zusammenstellung richtig ist, so müsste
np. zextn für *zehm stehen.
LW. kurd. afy. za^m; bei. zahm, zäm 'Schwort,
Säber (296).
653. zeden schlagen*, Praes. zen-em.
Kä8. Q. fiden , bäjin , bemjida bü ; K. jindemün , Z.
bezint.
ap. [^jan',ajunam'töAien; aw. [/'Jan-, Jainti; phlv.
zatan^ zanet, zatär, zan(i)sn; ai. [/han-, Aawfi 'schlagen,
tödten'; arm. vergl. gan 'Schläge, Züchtigung, yunem
'schlagen, prügeln' (H. No. 63).
kurd. zenin 'schlagen (Feuer), schicssen'; af/.
va]zan-am; bei. janag, n. janay (175), LW. zaday,
n. zaday (294); si/n. zln-am, sar. zan-am, vi^zm-am,
654. {\)zer 'Gold', zetln (zerrm); zernl (LW. arab. zarnlq,
zarmxj syr. talm. yy)*) 'Arsenik'; zerJr, zifir 'gelbes
Färbholz, Gelbsucht' i).
ap. vergl. da(jHx6g {?)^); aw. zairi-, vergl. zaramja-
'Gold'; phlv. zar, zartn; ai. hdri-, hiranya-,
kurd. LW. zer, zir; afy. LW. zar; oss. d. suy]zärin(i,
t. sizyänn 'Gold, golden (234); bei. LW. zar (302).
*) Natürlich nicht aus aw. Zairivairi-, phlv. Zariver (?) (Hörn,
Mitth. aus d. er. Samml. d. K. Mus., Heft lY, S. 25), wie der Eigenname
Zerer (yergl. Nöldeke, Pers. Studien II, 2, Anra.).
') Trotz der Schwierigkeit, die Form mit ap. diivar- zu vereinigen,
erklärt G. Hoffmann, Zeitschr. f. Assyr. II, 49 folg. (JapHxds als
^königl. persische Hof- und Reichsmunze im Gegensatz zur ausser-
persischen Währung'.
Hörn, Grtindriss d. neup. Etymologie. 10
```


## [2026-09-06T14:55:22.979Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== HRN p.172 (NR 194) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==194' HRN.txt | head -60"
}
```


### [2026-09-06T14:55:24.830Z] TOOL RESULT

```
=== HRN p.172 (NR 194) ===
— 172 -
phlv. östaftan ') (vd. 7 (27) GL, 18 (98), Meii.) eilen,
arm. LW. staij, davon Denomin. stapim 'eilen.
aw. *aiwis + l^tap-, täpaj/eiti *iri Wärme, Hitze
bringen', dann tropisch-).
Zu aiwis vergl. oben np. hes- (No. 221).
778. sHden gehen; sein, werden', Praes. sev-em.
ap. \/^siya€', aslt/avam, asiyuva 'gehen, marschiren';
aw. {/sav-, suvaite'^) gehen'; ai. [/^cyav-, Ci/dvate 'fort-
gehen ; arm. cit 'Aufbruch', ciiem 'aufbrechen' (H.
No. 242).
kurd. eleu 'gehen', dicm; sify, soal 'werden, gehen';
oss. d. t. cäün 'gehen, schreiten, spazieren, fahren'
(319) ; bei. suta, siit, n. suöa, iud^a (322) ; wa;^. cduam,
si/n. oi\zafcam, sar. va]zevsam.
779. siirrän, serrün 'unablässig lliessend', slrän Kegen' (y),
sun-iden^), vergl. sär {äbsär), särulen, ,
ai. l^ksar-, ksdrati 'fliessen, strömen' (Geiger,
Etym. d. Bai. unter No. 66; bei. ö[ur 'Giessbach'
kann aber nicht verglichen werden, s. Htibsch-
mann, ZDMG. 44, 556).
780. Herrn 'Schaam'.
aw. fsarema- 'Schaam'; phlv. sarm *Schaam', sarm-
[gas 'Genitalien' (vd. 16 (5) Gl.).
oss. t. äfsdrm, d. äfsänni 'Schande' (121) ; LW. aty.
bei. (253) sarm 'Schaam', kurd. serm,
781. sest, sest 'sechzig*.
aw. yscasti- 'sechzig ; päz. säst (FPGl.); ai. saüi-,
kurd. FD. LW. sest; afy. speta,
782. susten Vaschen', Praes. söy-em^),
phlv. sustan, söyBnd^ söy(i)sn; kurd. LW. sustin
'waschen' (vergl. g. sustinUu neben sustmün) ; bei.
*) Pfiz. qastäftun^ qastäwidan (Men.) ist Unsinn.
*) An ursprüngliches ^sila^ten (vergl. jjuft aus jf*x^) darf man
wegen Praes. siiäb-em natürlich nicht denken.
^) Bartholomae, Ar. Forsch. III, 33 liest staitc.
*) Zum Teil unbelegt.
^j Reimt auf higöyetl, Vis und Rämln S. 70 Vers 6.
```


## [2026-09-06T14:55:36.739Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources; python3 -c \"\nimport json;d=json.load(open('refs_online.json'))\nfor k in ['BQT','MON','SYN','AHD','IEC']:\n  print(k, d[k].get('page_offset'), '|HINT|', d[k].get('lookup_hint'));print()\n\""
}
```


### [2026-09-06T14:55:38.657Z] TOOL RESULT

```
BQT vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...'). |HINT| grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)

MON None |HINT| Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks).

SYN leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |HINT| Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed page number line.

AHD 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page. |HINT| Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves = original 1969 ed.).

IEC TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |HINT| Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.
```


## [2026-09-06T14:55:44.205Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR>=462 && NR<=468 {print \"--- leafidx \"NR-1\" ---\"; print substr($0,1,2500)}' BQT_v2_pages.txt"
}
```


### [2026-09-06T14:55:46.299Z] TOOL RESULT

```
--- leafidx 461 ---
 ‫زامیاد‬                                                                                                     ‫تس‬

‫رال مستحاضه ‪ - ۴‬بعنی زالعفيم‬                                       ‫رال ابرو = کنابه از آسمان است‬
                          ‫است که کنابه از دنا باشد ‪.‬‬                               ‫باعتبار هلال که ماه عکشبه باشد ‪.‬‬
 ‫رالمو سیه‪ .‬بممنی زار م تحاضه‬                                     ‫رال بد افعال۔ کنابہ از دیا وعالم‬
‫نزگه را‬
      ‫اکستنکاهبه از دنا باشد ‪ -‬وچسا‬                                                                          ‫باشد ‪.‬‬
‫نیز گوبند » و آن سازی است مشپو رکه یشتر‬                            ‫رال رعنا د بمعنی زال بد افعال است‬
                           ‫زنان لوازند ‪.‬‬                                                ‫کهنابه از دیا (‪ )۱‬باشد ‪.‬‬
‫رالو * ‪ -‬بر وزن خالو » بمعنی زلو‬                                   ‫رال زد ‪ ۱۰‬یک ثالث پردسرتمرا‬
 ‫باشد‪ ,‬وان کرمی است که چون بربدن چسبانند‬                          ‫گوبند باعتبار سرخی چهره ‪ ۰‬چه رنه اوسر خ‬
                                                                                                ‫وموی اوسفید بوده ‪.‬‬
                                  ‫‪.‬‬   ‫خون فاسد را بمکد‬



 ‫رالو ڭ ‪ -‬بر وزن موعتی غالوکه‬                                     ‫ال‌سرسفید سیه دل‪ -‬کنابه از‬
                                                                                   ‫دلیا ‪ -‬ومردم بیمهر وشفقت باشد ‪.‬‬
‫آن‬    ‫و‬   ‫»‬   ‫باشد‬   ‫گروهه‬       ‫کمان‬         ‫که مهر‬     ‫است‬



                                                                   ‫بمعنی زال رعناست‬       ‫رال سفيك وه‬
                                  ‫‪.‬‬    ‫اندازند‬     ‫و تقك دهن‬


 ‫رام = بروزن‌دام‪ .‬دره‌است د�
--- leafidx 462 ---
 ‫—‬           ‫‪۵ ۵ 6‬‬




     ‫مخفف زدآوتر امت که انزاطرف ترباشد‪#*.‬‬                              ‫نام روز ست‬         ‫کشده و بدال ایرد زده )‪۰ (۱‬‬

‫زانو رصد اه کردن = کنابه‬                                              ‫و دامفرشتها‪.‬ست که‬      ‫وهشتم‌است ازماهپای شمسی‪-‬‬

                                                                      ‫صالح وتدییرآموراین روزباو علق دارد ویمحافظت‬
‫ازمراقبه کردن ومتفکرواندوهگین شتن باشد ؛‬
‫وزانو کرصرددن‌هم هت که بی کلمة گاهباشد‪.‬‬                               ‫حوران بپشتی لیزمامور است‪ .‬کوبند در این روز‬
                                                                      ‫درخت شاندن (‪ )۲‬و تخم‌کاشتن و عمارت کردن‬
‫سياه‬         ‫جااورىت‬       ‫»‬   ‫بروزن خانه‬    ‫=‬    ‫رانه‬
                                                                                                      ‫بغامت خوب امت ‪.‬‬
‫ریگ بوردار که بیشتر در حمامها متکون شود‬
                                                                      ‫ویمیم‬   ‫رامیم ‏‪ ۳ am‬تال ستحتالی رده‬
‫وبانگ طولالی کند ‪ ۰‬و بعضی گوبند زانه ختفا‬
                                                                                 ‫بزر که‬     ‫بيار‬   ‫نام رودخانه‌است‬   ‫‪4‬‬   ‫زده‬

                          ‫باشد ‪.‬‬      ‫نك‬
                                       ‫این‬
                                         ‫درک‬
                                           ‫ره س‬
                                              ‫گت ک‬
                                                 ‫اس‬
                                                                       ‫دان = بروزن جانِ‪ .‬مخفف ازآن امت‬
‫با نون بتحتالی رسیده(‪)4‬‬                   ‫رالیج" =‬                    ‫چنانکه گویند زناطرف وز آ نو ممنی ازا تطرف‬
               
--- leafidx 463 ---
‫زاولایه‬                                                                                     ‫ات‬   ‫او‬




‫زاور فتراش * ‪ -‬بنتح ف واسکون‬                             ‫بارچه و لیم‬   ‫وهبمعتی خشت‬   ‫کوه را نیز گوبند ‪-‬‬

‫رای بی‌نقطه وفوقالی بالف کشیده وبشین قطمدار‬                                      ‫تن‬      ‫هم آمده‬      ‫خشت‬

‫زده » ءمتنم الوجود را کونند چه زاو بمعنی‬                  ‫راود = بر وزن باور ‪ ۰‬بمعنی خادم‬
               ‫باشف ‪۰‬‬    ‫بمعئی وجود‬    ‫همتتم وفرتاش‬      ‫و خدمتکار باشد وستارة زهره را نگیوزبند ‪٩‬‏‬
‫زاوش ‪ = ۱‬بشم واو پروزن خامش »‬                                                ‫ویمعنی قدرت رقوت؟ و‬
                                                          ‫‪-‬ژلده بود بعنی برزگه‬
                                                         ‫به از‬   ‫ناکه‬‫کره‬
                                                                       ‫وقوی هکل وتوانا ‪ -‬ویمعنی ز‬
 ‫میمننی بر وزن‬
             ‫نامکو کب مشتری ‪,‬اشد ؛ و با‬
                                                          ‫دلبری وبارا باشد ‪ - ۳‬و یمعنی چاروای سواری‬
‫خموش وخاموش هآمده است ؛ وبروزن‌خاموش‬
                   ‫کو کب عطارد را نبز گفته‌اند ‪5‬‬          ‫هم آمده‌است که بعربی‌راحله خوانند ‪ - ۴‬وزنده‬
                                                         ‫و سلامت را نگیفزته‌اند و‪-‬بمعنی آب سياه حم‬
                                                          ‫وان علتی باشد مشهور رسنی هر‬         ‫دة هن‬
‫زابل است که ولابت سیتان باشد ‪ -‬و لام فومی‬                 ‫وی راکه ات تاه آورده‪ :‬باشد گونند فزاوز‬
                                                          ‫شده است» بعنی آب سیاه آورده است‪ -‬ویمعنی‬
‫لزهٌ نت زبان فا�
--- leafidx 464 ---
   ‫و ‪ ۵‬ات‬
                                                                                                      ‫زاووش‬

  ‫راهد حخك د کنابه از زاهدی‬                           ‫است که‌برپای‌ستوران و بکزپرابان گذارند وآنرا‬
  ‫است که لهات اهتمام درزهد وپرهیز کاری داشته‬           ‫‌موی مجعد وییچیده‬       ‫ید‪-‬‬
                                                                                 ‫نوین‬‫عوک‬
                                                                                       ‫ییمبخا‬‫ورک‬‫بت‬
  ‫واهد جاهل را یز‬
                ‫باشد ‪ -‬وزاهد بی درد ز‬                                                        ‫همآمده اضنته‪..:‬‬
                                          ‫گونند ‪.‬‬      ‫و‬          ‫هبروزن هه‬
                                                      ‫خاموش » بمعنی‬                      ‫راو وس‬
                                                     ‫زاوش است که ستارة مشتری باشد ‪ -‬و عطارد را‬
                      ‫باشد ‪۰‬‬   ‫حهان آرا‬    ‫خورشد‬
                                                                                                 ‫زتماید ‪.‬‬
                                                                                                        ‫فن‬‫ک‬
  ‫با ها بروزن خاطری » بوی‬      ‫راهری۔‬
  ‫خوش‌را گوینده وبجای رای می‌نقطه زای نقطه‌دار‬
                                                      ‫داووق ‪ - ۴‬بر وزن فروق ‪ .‬نم‬
                                                      ‫باصطلاح ‪ ۱‬کیریان و عریی زببق‬                   ‫جنوه است‬




                                   ‫چن ادد‬                                           ‫وکل‌کار راکوبند ‪. ۴‬‬


                                              ‫يان دوم‬


  ‫زبراد بنتح اول بر وزن سواد » عرقی‬                    ‫می‬         ‫= بنتح اول و سکون ان‬               ‫رب‬

‫وچرکی باشد نکرهاآاز میا
--- leafidx 465 ---
   ‫زنباکنسكت‬                                                                            ‫و و ات‬    ‫تم‬




                                                   ‫زان ‪ ۱‬ب»فتم اول معروف است ‪۴‬‬
‫و سخن گوی باشد ‪ -‬و شخصی را لز کوبن که‬               ‫ی لان کواند ‪ ۰‬وضم اول هم درست اد‬                ‫وس‬

 ‫را کیفزته‌اند ‪- ۴‬‬     ‫رد‬
                        ‫گاند‬
                           ‫ارابد‬
                               ‫شنها‬
                                  ‫و زبا‬
                                      ‫همه‬          ‫ربان بر = بطم بای ایجد » کنابه از‬
 ‫ربان ران = با رای فرشت بر وزن‬                     ‫خاموش کردن صدعی است بدلابل و جوابیکه‬
 ‫زبان دان » صاحب قیل و قال و پرکوی و هرد‬            ‫دیگر حرف تمیتوالد زودبنمعنی عطا وبخشش‬
                                                   ‫نزآمده است چنانکه در زمان بیغمبر شاعربرا‬
 ‫ربان ردن ‪ -‬کنایه از حرف زدن‬                        ‫را سر‬    ‫بسمرکه زبانش‬   ‫فر مودند‬   ‫رسالت‬      ‫رت‬


                            ‫وسخن گفتن باشد ‪.‬‬       ‫عمر خواست که بکاارد ببرده حضرت امیرفرمود‬
 ‫تندن ‪ -‬کنابه از خاموش‬
                     ‫سبا‬
                       ‫ر‬                                                        ‫که باوچیزی بده ‪.‬‬
                                                   ‫ربان بر ‪۵‬ت بکر نون» گیاهی است‬
                     ‫کردالیدن باشد ‪.‬‬
                                                    ‫وبعربی لسان‌الحمل‬       ‫ند‬
                                                                             ‫نوشك‬
                                                                                ‫ورااخرک‬
                                                                                      ‫خآن‬
                                                                                        ‫که‬
 ‫زب
--- leafidx 466 ---
    ‫ات‬                                                                                                            ‫ِ‬
‫ر بر جد ‪ - ۴‬لوعی اززمرد باشد‪ .‬وآن‬
‫از جملهٌ جواهراست وطسمش سرد وخشك است‬
                                                                              ‫‪4‬‬            ‫زبانه‪ma ۱‬‏ بفتح اول‬
                                                     ‫‪۰‬‬   ‫در دوم‬
                                                                                           ‫بر وزن بپانه » آنجه در ميان‬
‫را گویند‬      ‫صدر مجلی ‪۵‬‬          ‫=‬       ‫ر بر دست‬
                                                                                           ‫شاهین ترازو باشد ‪ -‬و زبالة‬
‫فوت و فدرت‬          ‫صاحب‬    ‫و‬    ‫توانا‬     ‫از مردم‬       ‫و کنابه‬
                                                                                          ‫هر چیز را نز گوند ؛ و هم‬
                                      ‫‪۷‬‬    ‫دن‌هروزو ‪‎‬دشاب ‪۹‬‬          ‫‪۲‬‬                ‫‪٣‬‬
                                                                                                       ‫آول‌هم دردت است‬
‫‪ -‬بغای مضموم بواو وفا زده؛‬                 ‫وف‬
                                            ‫قبر‬
                                              ‫ر‬                          ‫زان یاقتی ‪-‬کنابه ترازو و زبالآن‬
                                                                                                       ‫ب‬
                        ‫بمعنی دشنام ولفرین باشد ‪.‬‬
                                                                                                 ‫از وت بافتن باش ‪۸‬‬
  ‫بواوی‬
      ‫ز بر کلو بد = باکاف ولام و وا‬
                                                                           ‫ون‬‫کلی‬
                                                                               ‫سا‬‫وتح‬
                                                                                   ‫زربر ‪ -‬بکر
--- leafidx 467 ---
                                                                                           ‫و‬   ‫ی‬




‫بیز کوبند ‪ -‬ویضم اولخریداری باشدکه چیزها‬          ‫کاف فارسی » بروزن ومعتی زبغر است که زبلغ‬
 ‫شتربراکوبند‬     ‫ی‬
                 ‫بدر‬
                   ‫‪-‬و‬‫عردر‬
                        ‫را برغبت نمام بخ‬          ‫باشد آونرا آیوق نکیوزبند (‪)۱‬؛ وبکر اول‬
                                                  ‫وفتح‌ انی و ضم‌کاف تازی دز کفته‌اند ؛ و ماکاف‬
               ‫کوچکی که درزر قبا پوشند ‪.‬‬          ‫مضموم و مشدد هم آورده‌اند ؛ وباين معنی‌بجای‬
                                                  ‫نیز آمده است که بروزن‬           ‫طیی‬
                                                                                    ‫حی با‬
                                                                                        ‫حرف ال‬
‫ر بر = بکسر اول و فتح هابروزن‬
‫کشور‪ .‬بیزارشدن پدر ومادر باشد ازفرزسو آیرا‬                    ‫دیگر باشد وبترکی زمرطه خوانند ‪.‬‬
                            ‫وبند ‪.‬‬
                                 ‫بعربی عکاق‬       ‫بقتح اول وخای لقطه‌دار‬        ‫رز بوحه ‪= ۱‬‬
‫اول » عاق‬      ‫ا‬      ‫س‬   ‫ز بهر کردن‬              ‫آخنوثی و لذتی را کویند کهدرحین جماع‬
‫ازو‪.‬‬   ‫ساختن ددر و مادر فرزدد را وببزار شدن‬                                       ‫کردن بهم رسد ‪.‬‬

‫ر هیده ‪ -‬بروزن فهمیده » بمعنی قرو‬                 ‫ر بوده = بفتح‌اول بروزن‌بوده ‪ ۰‬بمعنی‬
‫افتاده باشد مطلقاً آعم از جایی با ازمنصبی با از‬   ‫بی تأمل وبی رقب باشد ‪ -‬ویه‌عنی سبزیی است‬
                                 ‫فوت وقدرت ‪.‬‬      ‫؛‬      ‫ارانثند‬
                                                               ‫وک‬‫خربی
```


## [2026-09-06T14:55:52.732Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} /زخم/ {print NR-1}' BQT_v2_pages.txt | head -20"
}
```


### [2026-09-06T14:55:54.771Z] TOOL RESULT

```
25
30
83
91
96
97
98
99
107
120
185
196
205
212
225
227
235
287
324
341
```


## [2026-09-06T14:55:58.838Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR>=470 && NR<=500 {n=NR-1; split($0,a,\"\\n\"); print n\": \"substr(a[1],1,80)\"  //  \"substr(a[2],1,80)}' BQT_v2_pages.txt"
}
```


### [2026-09-06T14:56:00.418Z] TOOL RESULT

```
469:  ‫زدن‬                                                                     //  
470: ‫—‬        ‫‪۵۵‬‬  //                                                                                  
471:  ‫زراوند‬                                                               //                                                                                  
472:     ‫—‬        ‫)‪0‬‬  //                                                                                  
473:        ‫زردشت‬                                                           //  
474:  ‫ات‬                                                                       //  
475:    ‫تی‬  //      ‫ده‬‫رش‬
476:  ‫=—‬       ‫غ‬  //                                                                                  
477:       ‫عتار‬  //           ‫زارفمش‬                                                     
478:                                                                                   //   ‫—‬            ‫‪۵ ۱٩‬‬
479:   ‫ژروان بز رگ‬                                                      //  
480:  ‫‪ 0‬ات‬  //                                                                                  
481:   ‫زربرا‬  //                                                                                  
482:   ‫—‬      ‫س‪00‬‬  //  
483:  ‫رعیر‬                                                                   //  
484:                                               ‫بیان نهم‬  //                  ‫أت‬     ‫نقطه دار با غىن نقطه دار م
485:  ‫زفیر‬                                                                   //  
486:                                                   ‫يان دهم‬  //                            ‫در زای نقطه دار بافا مشتمل ب�
487:   ‫زکاسه‬                                                                //  
488:  ‫سح‬    ‫هفش‬  //                                                                                  
489:                                     ‫بیان سیزدهم‬  //               ‫درزای نقطه دار بالام مشتمل برباتزد�
490:  ‫‪٩‬‏ ‪۱ ۵‬سه‬   ‫سز‬                                   //  
491:   ‫رمج‬                                                                    //   ‫رمام = بکر اول بورزن لظام 'مپار‬                   
492:  ‫‏—‪ opo‬اسه‬  //  
493:                                                                                   //  ‫پاکیره منظر از جنس چرغ و آنچه رنگش‬             
494: ‫=‪m‬‬  //                                                                                  
495:                                         ‫بیان بدانهزم‬  //  
496:       ‫و‬                                                                    //  
497:      ‫زتجیر‬  //                                                                                  
498:    ‫خر و‬                                                                  //   ‫نزحیری د کنابه از دیوانه بادد ‪[| .‬وسخن س�
499:  ‫زف بای‬                                                                //  ‫قرشت (‪ )۷‬بر وزن رفت ازجا » دکاتماب‌زردش�
```


## [2026-09-06T14:56:07.058Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==469 {print substr($0,1,4000)}' BQT_v2_pages.txt"
}
```


### [2026-09-06T14:56:08.743Z] TOOL RESULT

```
                                                 ‫بیان سوم‬
                     ‫در زای نقطه دار باجیم مشتمل بر چپار لغت‬

                     ‫عنکبوت را گویند ‪۱‬‬       ‫مال‬        ‫* رج ‪ -‬بضم اووسلکون انی » تیر‬
                                                                        ‫پرتاب‌باشدکه پیکانآ براازاستخوان‬
‫رجمول ‪ -‬با میم بر وزن معقول ‪.‬‬
                                                                        ‫فیل وشاخ‌قوج کواومیش وامثال آن‬
‫حبی امت دوابی و آلرا بفارسی یخم کشوث‬
                                                                        ‫مازید ‪ _ ۱‬و کوتاه ثرین نیرها را‬
‫خواند ‪ .‬طبیمت آن معتدل امت در گرمی‬
                                                                        ‫و بمعنی چیزی باشد‬           ‫نکیوزبند ‏‬
                                         ‫‪۰‬‬   ‫وسردی‬
                                                                         ‫کهآ راازدوغ ترش سازند وبتر کی‬
 ‫زجه ‪ = ۴‬بفتح‌اول وثانی» زلی گروابند‬                                      ‫قراقروت خوانند؟ ؛ وباجیم فارسی‬
‫که زاییده (‪ )۱‬باشد و او را تا چهل روز زجه‬                                    ‫یز همه معانی آمده است ‪.‬‬
‫میتوان گفت ‪ :‬وباجیم فارسی‌هم درست امت ‪.۶٩‬‏‬                               ‫بفتح‌اول بروزن‬        ‫رجال‬


                                              ‫يان چهارم‬

          ‫کتنوات‬
               ‫دزرای نقطه دار با خای نقطه دار مشتمل بر هفت لغ‬
‫و اسب را بهم میرسد و آنرا ازخ فيز گونند‬                  ‫رخ = بفتح اول و سکون ثالی‪ ۰‬آواز‬
‫ولالةٌ حزین راگویند؟ ‪ -‬وبانگ وصدای زنگه | و بعربی تژلول خوانند © ‪ -‬و مخفف زخم هم‬
                                             ‫تن ‪۱‬‬        ‫و جرس را همگفته‌اند ‪ - ۴‬و فرو بردن چیزی‬
‫بر وزن شراره » شاخ‬            ‫رخاره ‪= ۲‬‬                  ‫باشد بزور وعنف درمة‌اك ‪ -‬وعلتی باشد کهآ دمی‬

                                                                          ‫(‪ )۱‬چسش ‪ ۲ :‬شده ‪.‬‬

  ‫‏‪( - ٩‬عر) زح (بضم اول وتشدید دوم) «نیزی آرنج » آهن بن لیزه وپیکان تیر ‪ .‬زجاح‬
  ‫‪_ ۴‬طبری سرج (کشك سیاء [قرقوروت] )» مازندرانی‬                          ‫وزججه ‏‪ ٠‬جمم» «منتهی الارب؟ ‪.‬‬
                             ‫رك ‪ :‬زاح » زادن ۔‬   ‫‪- ۴‬‬            ‫‪.‬‬   ‫‪۸۲4‬‬     ‫کتوی زهك ‪ « 15» .‬واژه نامه‬

         ‫رك‪ :‬زخم ‪.‬‬   ‫‪-‬‬   ‫‪۱‬‬           ‫ازخ ‪ ۰‬آزخ » ژخ ‪.‬‬       ‫_رك‪:‬‬    ‫‪۵‬‬         ‫‪.‬‬   ‫ژخار‬    ‫رك‬    ‫‪۴‬‬


                                              ‫‪-‬ك‪ :‬زخناره » ازغ » اژغ » آزغ ‪ 7‬آژغ ‪.‬‬
                                                                                 ‫‪ ۷‬ر‬
                                                       ‫تتفرقة پابان کتاب ‪.‬‬
```


## [2026-09-06T14:56:15.857Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==470 {print substr($0,1,4000)}' BQT_v2_pages.txt"
}
```


### [2026-09-06T14:56:17.942Z] TOOL RESULT

```
 ‫زدن‬                                                                                ‫و ‪—| ۵ ۵‬‬




‫چویکی باشد که سنادزهابدان سازنوازند ویعربی‬                                  ‫درخت رگاوند ‪۶.‬‬
                              ‫مراب خوانند ‪.‬‬      ‫زخم بریان س بمعنی دم پفت است‪.‬‬
‫رخناره ‪ = ۴‬بانون پروزن انگاره »‬                                      ‫‪۱‬‬   ‫وآن طعامی باشد معروف‬

      ‫بمعنی زخاره است که شاخ درخت باشد ‪۰‬‬         ‫زخم ناخ د بمنی باناخن رش‬
                                                 ‫ونابه از رفوم منجمان هم‌هت‪.‬‬
                                                                           ‫کردن باشد ک‬

                ‫وبی‌خرد وی‌خود شدن باشد ‪.‬‬



                                        ‫يان بنحم‬

                                                       ‫در زای نقطه دار با دال بی‬
‫بکر اول بر وزن جگر »‬          ‫ردر ‪= ۴‬‬            ‫ردای‪ = ۴‬بکر اول بر وزن فزای »‬
             ‫زدابنده و پاکیزه کننده را گویند ‪ -‬وامر | بمعنی درخور راق وسزاور باشد ‪.‬‬
‫رشن * = بروزن‌بدن‪.‬عمروف است ‪١-‬‏‬                  ‫بابن معنی هم هت بعنی بزدای وپاکیزه ساز‬
‫وکنابه از چیزی خوردن ‪ - ۷‬و مباشرت کردن‬           ‫و زدایدن وصان کردن وبا کیزه ساختن باشد ‪.‬‬

                                              ‫‪۰‬سوند اسم آلت) ‪:‬‬
                                                             ‫‪ -‬از ‪ :‬زخم (پ‬
    ‫رکه بدر آوازش‪.‬‬
                 ‫ناخوشتر از آواز‪ :‬م‬               ‫کفتی رکه جان میگلد زخمه‌ناسازش‬
  ‫«کلتان ‪۲۷‬‬
               ‫رك ‪ :‬از در ‪.‬‬    ‫‪۴‬‬        ‫رك ‪ :‬زدودن ‪.‬‬     ‫‪۴‬‬        ‫‏‪e‬‬
 ‫‪-‬هلوی ‪ 12122‬و ‪ 02682‬از رة ابرانیقدیم ‪. 2421 . [02 -‬ار ‪nag‬‏‬        ‫پ‬
 ‫که ‪ ۸۵۲‬بارسی‌باستان ر‪٫‬عةٌ‏ ‪ 0712032 ۰ [12-‬ک(شتن)‪ .‬هندی‌باستان‬
                                                             ‫د بارتولمه ‪ ۰۹4‬نربب‬
  ‫رثة ‪ ( 4261 . 022 -‬مضروب کردن‪ .‬کشتن ) قس‪ :‬ارمنی ‪( 028‬ضرب ‪ .‬تادب) و‪۳۳6088‬‬
 ‫(مضروب کردن ‪ ,‬كتك زدن) » کردی ‪( 8106012‬زدن (آش)‪ .‬تیر الداختن)» افقانی‪۵۷ |۳202-‬‬
 ‫‪ ..4‬بلوچی ‪ [8202‬و ‪. [18202‬ع ‪ 82022‬ر ‪ . 0821022‬شغنى ‪"1Z - 0۳2‬‏ ‪,‬سریکلی‬
 ‫[‪ « 1۷‬اسنق ‪ ۳۹۰۰‬طبری ‪ ( 20- 72112‬زدن ) « ساب طبری‬                  ‫‪0-102‬‬
                                                                        ‫و ‪12‬‬       ‫‏‪0-2am‬‬
                                                                                      ‫‪2‬‬
  ‫‪ -‬کوفتن» وارد آوردن‌صدمه‪,‬‬             ‫)‪( 2022-80 .‬بزند) ‪.‬‬        ‫ن‬
                                                                   ‫د(‬‫ز‪06‬‬
                                                                       ‫‪» ۶‬گیلکی ‪62‬‬
   ‫‪۳‬ه*‪.‬‬
      ‫ات»ن«‬
          ‫سراتکف‬
```


## [2026-09-06T14:56:28.481Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==469 {print}' BQT_v2_pages.txt | sed -n '1,200p' | tail -60"
}
```


### [2026-09-06T14:56:30.102Z] TOOL RESULT

```
                                                 ‫بیان سوم‬
                     ‫در زای نقطه دار باجیم مشتمل بر چپار لغت‬

                     ‫عنکبوت را گویند ‪۱‬‬       ‫مال‬        ‫* رج ‪ -‬بضم اووسلکون انی » تیر‬
                                                                        ‫پرتاب‌باشدکه پیکانآ براازاستخوان‬
‫رجمول ‪ -‬با میم بر وزن معقول ‪.‬‬
                                                                        ‫فیل وشاخ‌قوج کواومیش وامثال آن‬
‫حبی امت دوابی و آلرا بفارسی یخم کشوث‬
                                                                        ‫مازید ‪ _ ۱‬و کوتاه ثرین نیرها را‬
‫خواند ‪ .‬طبیمت آن معتدل امت در گرمی‬
                                                                        ‫و بمعنی چیزی باشد‬           ‫نکیوزبند ‏‬
                                         ‫‪۰‬‬   ‫وسردی‬
                                                                         ‫کهآ راازدوغ ترش سازند وبتر کی‬
 ‫زجه ‪ = ۴‬بفتح‌اول وثانی» زلی گروابند‬                                      ‫قراقروت خوانند؟ ؛ وباجیم فارسی‬
‫که زاییده (‪ )۱‬باشد و او را تا چهل روز زجه‬                                    ‫یز همه معانی آمده است ‪.‬‬
‫میتوان گفت ‪ :‬وباجیم فارسی‌هم درست امت ‪.۶٩‬‏‬                               ‫بفتح‌اول بروزن‬        ‫رجال‬


                                              ‫يان چهارم‬

          ‫کتنوات‬
               ‫دزرای نقطه دار با خای نقطه دار مشتمل بر هفت لغ‬
‫و اسب را بهم میرسد و آنرا ازخ فيز گونند‬                  ‫رخ = بفتح اول و سکون ثالی‪ ۰‬آواز‬
‫ولالةٌ حزین راگویند؟ ‪ -‬وبانگ وصدای زنگه | و بعربی تژلول خوانند © ‪ -‬و مخفف زخم هم‬
                                             ‫تن ‪۱‬‬        ‫و جرس را همگفته‌اند ‪ - ۴‬و فرو بردن چیزی‬
‫بر وزن شراره » شاخ‬            ‫رخاره ‪= ۲‬‬                  ‫باشد بزور وعنف درمة‌اك ‪ -‬وعلتی باشد کهآ دمی‬

                                                                          ‫(‪ )۱‬چسش ‪ ۲ :‬شده ‪.‬‬

  ‫‏‪( - ٩‬عر) زح (بضم اول وتشدید دوم) «نیزی آرنج » آهن بن لیزه وپیکان تیر ‪ .‬زجاح‬
  ‫‪_ ۴‬طبری سرج (کشك سیاء [قرقوروت] )» مازندرانی‬                          ‫وزججه ‏‪ ٠‬جمم» «منتهی الارب؟ ‪.‬‬
                             ‫رك ‪ :‬زاح » زادن ۔‬   ‫‪- ۴‬‬            ‫‪.‬‬   ‫‪۸۲4‬‬     ‫کتوی زهك ‪ « 15» .‬واژه نامه‬

         ‫رك‪ :‬زخم ‪.‬‬   ‫‪-‬‬   ‫‪۱‬‬           ‫ازخ ‪ ۰‬آزخ » ژخ ‪.‬‬       ‫_رك‪:‬‬    ‫‪۵‬‬         ‫‪.‬‬   ‫ژخار‬    ‫رك‬    ‫‪۴‬‬


                                              ‫‪-‬ك‪ :‬زخناره » ازغ » اژغ » آزغ ‪ 7‬آژغ ‪.‬‬
                                                                                 ‫‪ ۷‬ر‬
                                                       ‫تتفرقة پابان کتاب ‪.‬‬
                                                                         ‫لمخا‬            ‫‪:‬‬
                                                                                         ‫ك‪-‬‬‫رزپ‬
                                                                                             ‫‪#‬‬
                                                     ‫‪#‬چه ‏ رك ‪ :‬لغات متفرقهٌ بایان کتاب ‪.‬‬
                                                                                        ‫ر‬

  ‫‪)۱۳۱‬‬     ‫طع‬
            ‫اای‬
              ‫فبره‬
                 ‫(‬
```


## [2026-09-06T14:56:41.003Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n 'zaxm\\|zahm\\|2822\\|22112' BQT_v2_pages.txt | head; echo \"=== try ref_page ===\"; python3 tools/ref_page.py BQT:1007 2>&1 | head -30"
}
```


### [2026-09-06T14:56:42.616Z] TOOL RESULT

```
=== try ref_page ===
python3: can't open file '/home/sfmqrb/git/rishe/data/verification/sources/refs/tools/ref_page.py': [Errno 2] No such file or directory
```


## [2026-09-06T14:56:44.505Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 tools/ref_page.py BQT:1007 --image 2>&1 | head -40"
}
```


### [2026-09-06T14:56:46.646Z] TOOL RESULT

```
no scan of BQT covers printed page 1007 (see 'scans' in refs_online.json)
```


## [2026-09-06T14:56:55.889Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT; ls; echo \"=== leaves ===\"; awk 'BEGIN{RS=\"\\f\"} END{print NR}' BQT_v3_pages.txt; awk 'BEGIN{RS=\"\\f\"} NR>=8 && NR<=60 {n=NR-1; split($0,a,\"\\n\"); print n\": \"substr(a[1],1,60)}' BQT_v3_pages.txt | head -60"
}
```


### [2026-09-06T14:56:57.558Z] TOOL RESULT

```
BQT_v3_pagemap.json
BQT_v3_pages.txt
BQT_v3_picofile.pdf
BQT_v4_pages.txt
BQT_v4_pages.txt.pages
BQT_v4_picofile.pdf
BQT_v5_pages.txt
BQT_v5_pages.txt.pages
BQT_v5_picofile.pdf
=== leaves ===
721
7: [pdf page 8]
8: [pdf page 9]
9: [pdf page 10]
10: [pdf page 11]
11: [pdf page 12]
12: [pdf page 13]
13: [pdf page 14]
14: [pdf page 15]
15: [pdf page 16]
16: [pdf page 17]
17: [pdf page 18]
18: [pdf page 19]
19: [pdf page 20]
20: [pdf page 21]
21: [pdf page 22]
22: [pdf page 23]
23: [pdf page 24]
24: [pdf page 25]
25: [pdf page 26]
26: [pdf page 27]
27: [pdf page 28]
28: [pdf page 29]
29: [pdf page 30]
30: [pdf page 31]
31: [pdf page 32]
32: [pdf page 33]
33: [pdf page 34]
34: [pdf page 35]
35: [pdf page 36]
36: [pdf page 37]
37: [pdf page 38]
38: [pdf page 39]
39: [pdf page 40]
40: [pdf page 41]
41: [pdf page 42]
42: [pdf page 43]
43: [pdf page 44]
44: [pdf page 45]
45: [pdf page 46]
46: [pdf page 47]
47: [pdf page 48]
48: [pdf page 49]
49: [pdf page 50]
50: [pdf page 51]
51: [pdf page 52]
52: [pdf page 53]
53: [pdf page 54]
54: [pdf page 55]
55: [pdf page 56]
56: [pdf page 57]
57: [pdf page 58]
58: [pdf page 59]
59: [pdf page 60]
```


## [2026-09-06T14:57:04.284Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; timeout 300 python3 tools/ref_page.py BQT:1223 --image 2>&1 | head -60"
}
```


### [2026-09-06T14:57:13.083Z] TOOL RESULT

```
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1223.png
REF: BQT:1223  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 14  OCR-lang: fas

نخهه شاد گوته
۰ ان باله
شاد خوآب - با واو معدوله بر وزن شادرو ان ۷ - بنم اك و اسکون
کامیاب » خواب خوش و شکر خواب را | رایع و واوبالف کشیده وبئون زده ۰ پرددبز رکی
گوند ۱ را گویند مانند شامیانه و سراپرده که درپیش در
شاد خوار ؟ - با واو معدوله‌بروزن خانه وایوان ملوك وسلاطین بکفند و
خاکسار .۰« ۰ خوشحال و فرحناك و شادمان یز گفته‌اند - و پستی فرتی مثقش وباطوزر
باغد ۴ - وزنان‌فاحشه ومطربه را نی زکوبند ۴ کرالایه هم‌هست - و لام لحتی باشد زسی‌لحن
وبمعنی شرابخور هم‌هست- وشرابخوردن‌بی‌ترس بارید که بشادروان مروارید مشهور لست- وس
۴ َ ۰ 5 ۰ کنگرهای عمارتها و سردرخانها را نیز گفته‌اس
د اغبار را دز کقته‌اند - هعا
۶ بم یی کی دوز ۳ | وشادربان که بجای واو بای ابجد باشد هم بنظن
گذرانیدن بی زحمت و کدورت وتنگی باشد. وشادربال ثه بجای واو بای ی هم +
۰ آهده است درست است جچه درفار بای اند
شادخو اده ‎٩‏ باوار مندوله بروزن / سی بای !:
حو آده - باواو معدوله بروزن و واوبهم تبدیل می‌بایند۹ -
ماه پاره » زنان فاحشه و مطربه باشد - وشراب َو 7 ۱
فوردن بر اشار- وش انخواره راکو شادرو ان مروارید - لام لحن
خوردن بی اغیار - و شرابخواره را تی زکوبند.
شاد خو است - .۱ اد دوازدهم است ازسی لحن بارید» وآن اول‌شادر -
دا خیم اس 5 5 او 8 برودد وآن نام داغت بواسطةٌ آنکه در زیر شادروان‌این
بازخواست ۰ بممتی وی واشیای باس تصنیف مرا ساخته بود. روزی بارید همین تصنیف
شاد خور * بروزن بادخور»,معٌی را بجهت خسروه می‌نواخت » خسرو رآبیارخغوش
شادخور است که خادمان و فرحناك - و بی‌غین | آمد. فرمود طبقی مروارید برس باریدتثا رکردفد»
واغیار شراب خوردن باشد. بعد ازآن غادروان مروارید نام‌تهاد -
شادداآن - بنم ناك . بروزن و معنی شاد کام *۱- باکاف بال ف کشیدمویمیم
شابران است که نام دربتدی از ولامت شروان زده » لام برادر فربدون بوده است.
باشد ۹ . شاد گو نه ۱۱- بروزن با زکوده.یممتی
‎٩‏ - چواز شاد خوابش برانگرختم سرش را بنیزه در آویختم.
فردوسی طوسی.«فرهنك نظام» -
۲ - از: شاد + خوار (خوارنده) . رلك : شاد خورء شاد خواره ۳۴ - رك : شادان :
دشمنانت مستمند و مبتلا وممتحن دوستانت شادمان وشادکام وشادخواوب
« فرخی سیتانی ۱۱۱ -
ی ر4: شاد خواره 0 شادان ۰ شاد کونه ۰ رد: شادخوار. ۹ -مسصحف «#شاوران»
(.م.) و رك : شابران . ۷ - پپلوی 512107۷28 (فرش) « تاوادیا ۱۹۵ » معرب آن
نیز « شادروان « دزی ج ۱ ص۷۱۵ : ۲ مغفف آن «شاروان» (ه.م.).
۸ - این است همان صفه کزهیبت او بردی
بر شیر فلك حمله » شیر تن شادروان. ‏ « خاقانی شروانی۳۹۳؛.
* آن‌پوست راکه از دربرهثال شادروانی آوبخته است » ببینید». (جهانگشای جویئی‌ج ۲ ص44
۱۹ و4 : انا ی ید . ۹ شادروان (یکون سوم وفتح چهارم) مرکیست از : شاد ری
روان وبمعنی مرحوم ومفقور اسممال شود . *-لفة بمعتی خوش‌حال وشادمان و آشادخوار
است .( خاهددیل « شادخوار > قل شده) . ۱۱ معرب آن « شادکونه » (:پوشش بستر )
۶ دزی‌ج ‎٩‏ اس ۷۱۵ :۰.5۲
```


## [2026-09-06T14:57:22.700Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; timeout 300 python3 tools/ref_page.py BQT:1226 --image 2>&1 | head -50"
}
```


### [2026-09-06T14:57:30.931Z] TOOL RESULT

```
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1226.png
REF: BQT:1226  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 17  OCR-lang: fas

داروان -۱۷۹-<
شارك است که جانور سخن کوی باشد. بای فارسی ورای قرشت (۳) ومیم ساکن,بمعنی
شادو ان - بر وزن کاروان , مخفف | آسپر غم است که نوعی از ربحان باشد .
شادروان است که پرده بز رکك و شامیانه‌باشد . شاش - بروزن باش » هعروفستوبعربی
شارود ۱ - بفتح وار و سکون دال | بول کوبند ۸ - ونام شهریست مشهور بچاج واز
اسد ز یمعتی شابوداست که هاله وخرمن‌وطوق آنجا کمان خوب آورند٩‏ ۰
ماه باشد . شاشدن *۱- مغنف عاعیدن اس ت که
شارویه ۲ « بفتح بای حطی بروزن ] بول کردن باشد .
آموبه . نام شیرویه ‏ پسر خسرو پرویز است که شاشات ۱۱ بر وزن ناوك . بهمنی‌تیپو
خسرو راکشت و او را شیروهم میگوبند بحدف | باشد , وآن جانوری است شبیه بكيك لیکن‌از
بای حطی ؛ و بجای تحتالی نون‌هم آمده است آن کوچکتر میشود - ورباب را دٍ زکویند.وآن
که بروزن وارونه باشد ۴ . :
شار تال , دسا سَ سازست معروف ومشهور .
۵ « بفتح ثالث » دستار هد ام
ر ی ذاشنگ ۴ نَ زن 1 شکه:
پاش د که بزبان‌هندی چیرء گوبند ۴ وچادری(۱) ۱ 7 0 ۳ رود ۱۳
رنگین و بغایت ناز4 را نیز کفته‌اند که بیشتر اور را وان
زان هندوستای جامه کنند و جامةٌ افانوی یز | 2 بای اه هم مه و0 0 ۱
سازند * و در فرهنگه حین وفائی بازای نقطه رخ و ۱
دار (۷) * بمعنی دستار بز رکه آمده است. شاشو - بروزن مادو , نام کیاهی است
ی ۰.۲ ۱ وشش ۱
شادیدن ‎٩‏ « بر وزن باریدن , پرریی | که تخم آنرا در دواها پر لد وشضی ر
ربختن آب وشراب و امثال آن باشد -وتراویدن نی زگوبند که پیوسته بخود شاشد ۰۱۴
آب را نیز کوبند از جراحت . شاشو له ۱۶ - بفتح لام بروزن تاتوله.
شاسپر ۵ ۷ - بسکون سبن‌بی‌نقطه وفتح ‏ شمله وعلاقةٌ دستار وامثال آن باشد .
(۱) چش : چادر . (۷) چك : با زا . (۳) چك : ورا .
۹ - مصحف « شادورد » مبدل «شایورد» (۶ .)۴ میدل «شیرویه» ‏
رو این تافظ مصحف است . ۴ -در سانسکر بت 3 « و بلیامز ۹۹
و رد : چسره .۰
و وآن خطاست . ‎٩‏ -از: شار( ه.م. ) ۳+ بندن (پوند مصدری). درافغانستان نیز
«شاریدن» بهمین معنی است ۰ ۷ -از:شا (< داه) ۳+ سپرم (* اسپرم) (هم.). رل شاه‌اسپرغم.
۸ <عاعه (« م.( «لفت فری ۹ اب ی که بتوسط کلیه ازخون جدا و در هثانه جمم
و خارج کردد ؛گمیز. آدرار . رك : شاشیدن . ‎٩‏ - رد4 : چاچ. ۴ رك : شاشدن .۰
‎٩۱‏ ر4 : شاشنگه . خارعك . ۴۳ ر4 : شاشک , خارعك .
۴-کهی ماع رباب است وگاه بر بط وچنگه
گپی چغانه و طنبور و عود و که شاشنگه .
استاد . «جهانگیری» .
۴ از : شاش ۳و (پوند اصاف وعبالفه) . 9 - ر4:شاغوله .
```


## [2026-09-06T14:57:45.644Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n 'asbestos' KLN_1966.txt | cut -c1-600 | head -5; echo \"=== AHD watkins gwes ===\"; grep -n -i 'asbestos' AHD_watkins1985.txt | head; echo; grep -n '^g[ʷw]es\\|^gwes\\|zg[ʷw]es' AHD_watkins1985.txt | head"
}
```


### [2026-09-06T14:57:45.733Z] TOOL RESULT

```
2475:amianthus,  n.,  name  of  a  kind  of  asbestos.  L. amiantus,  fr.  Gk.  afnavrcw;  (scil.  ALiV,-),  lit. ‘undefiled  (stone)’,  fr.  <4-  (see  priv.  pref.  a-),  and piavTo^,  ‘stained,  defiled’,  verbal  adj.  of  tuodvetv, ‘to  stain,  defile’ ;  see  miasma.  The  spelling  th  (for t)  is  prob.  due  to  the  influence  of  Gk.
3579:asbestine,  adj.,  pertaining  to  asbestos.  —  L.  as- bestinus,  fr.  Gk.  daJ^aTivoi;,  fr.  Sapeaxoi;.  Sec next  word  and  adj.  suff.  -ine  (representing  L. -inus).
3580:asbestos,  n.  —  L.  asbestos,  fr.  Gk.  Sapearoc,  lit. ‘unquenchable,  inextinguishable’,  fr.  A-  (see priv.  pref.  a-)  and  opeaT^c,  verbal  adj.  of oPewivai,  ‘to  quench,  extinguish’,  which  derives fr.  I.-E.  base  *gwes-,  ‘to  quench,  extinguish’, whence  also  Lith.  gestu,  gisti,  ‘to  go  out,  be extinguished'.  OSlav.  gaSp,  gasiti,  of  s.m.,  Hitt. kishtari,  ‘is  being  put  out’,  Toch.  A  kas-,  B  kes-, kas-,  ‘to  go  out,  be  extinguished’, asbolite,  n.,  a  mineral  containing  oxide  of  cobalt.
=== AHD watkins gwes ===
545:sive reduplicated form *gr-g- in Latin gurges, throat, also gulf, whirlpool: GARGET, GORGE, GORGET, GURGITA- TION; INGURGITATE, REGURGITATE. 4. Extended form *gwr6- (< *geroa-) in Greek br6- in: a. suffixed redupli- cated form bi-bré-sko- in Greek bibréskein, to eat: HELLEBORE; b. nasalized variant form *bro-n-kh- in Greek bronkhos, windpipe, throat: BRONCHO-, BRON- CHUS; C. suffixed form *gvré-mn in Greek bréma, food: THEOBROMINE; d. suffixed form *gvr6-ti- in Greek bro- sis, eating: ABROSIA. [Pok. 1. gver- 474.] gwes-. To extinguish. Suffixed variant form *sgves-nu- in Greek sbennunai, to extinguish: ASBESTOS. [Pok. g¥es- 479.] g”et-'. Resin (?). Only in Germanic and Celtic. Suffixed form *gvet-u- in: a. Germanic *kwithu- in Old English cwudu, cwidu, cudu, resin, mastic gum, “that which is chewed,” cud: CUD, QUID!; b. Celtic *betu-, birch, birch resin, in Latin bitumen, resin (Gaulish loanword): BITU- MEN. [Pok. 1. g¥et- 480.] gwet-2. To say, speak. Germanic *kwithan in Old English cwethan, becwethan, to say, speak: BEQUEATH, BEQUEST, QUOTH. [Pok. 2. g¥et- 480.] gvet-3. Intestine. Suffixed o-grade form *gvot-olo- in Latin botulus, intestine, sausage: BOTULINUM, BOTULISM, BOWEL; (BOTULIN). [Pok. gvet- 481.] ghedh-. To ask, pray. 1. Germanic *bidjan, to entreat, in Old English biddan, to ask, pray: BID. 2. Germanic *bidam, entreaty in Old English gebed (ge-, intensive and collective prefix; see kom), prayer: BEAD. [Pok. gehedh- 488, 2. bhedh- 114.] gvhen-'. To strike, kill. 1. O-grade *gvhon- in Germanic suffixed form *ban-6n- in: a. Old English bana, slayer, cause of ruin or destruction: BANE; b. Middle High German ban, bane (> German Bahn), way, road (? < “path hewn through woods”): AUTOBAHN. 2. Suffixed zero-grade form *ghn-tyd- in Germanic *gundjé, war, battle, in: a. Old Norse gunnr, war: GUN; b. compound *gund-fanon-, “battle flag” (fandn-, flag; see pan-), in Italian gonfalone, standard: GONFALON. 3. Suffixed form *gvhen-do- in: a. Latin défendere, to ward off (dé-, away; see de-): DEFEND, (DEFENSE), (FENCE); b. Latin offen- dere, to strike against, be offensive, offend (ob-, against; see epi): OFFEND, (OFFENSE). 4. Suffixed zero-grade form *gvhn-tro- in Persian zahr, poison: BEZOAR. [Pok. 2. gthen-(2)- 491, bhen- 126.] g”hen-2. To swell, abound. Suffixed form *gvhen-eyo- in Greek euthenein (eu-, well; see esu-), to flourish: EU- THENICS. [Pok. 1. gthen- 491.] g’her-. To heat, warm. 1. Zero-grade *gvhr- with nasal suffix and analogical vocalism in Germanic *brenw-, to burn, forming *brennan (intransitive) and brannjan (transitive) in: a. Old English beornan, byrnan (intransi- tive) and bérnan (transitive), to burn: BURN}; b. late Old English brynstan, “burning mineral,” sulfur (stan, stone; see stei): BRIMSTONE. 2. Germanic *brandaz, a burning,
1262:ART? er-1 ARTEL ar- ARTERIO- wer-2 ARTERIOLE wer-2 ARTERY wer-2 ARTHRO- ar- ARTHUR rtko- ARTICLE ar- ARTIFACT dhé-1 ARTIFICE dhé-1 ARTIODACTYL ar- ARTISAN ar- ARTIST ar- ARYAN aryo- ASBESTOS gWes- ASCEND skand- ASCRIBE skribh- ASH! as-
```


## [2026-09-06T14:57:55.399Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'NR>=3500 && NR<=3620 && /^[0-9]{2,4}$/ {print NR\": \"$0}' KLN_1966.txt"
}
```


### [2026-09-06T14:57:57.326Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T14:58:00.308Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'NR>=3400 && NR<=3700' KLN_1966.txt | grep -n '^[^a-zA-Z]*$' | head -20; echo \"---\"; sed -n '3572,3582p' KLN_1966.txt | cut -c1-120"
}
```


### [2026-09-06T14:58:02.109Z] TOOL RESULT

```
23:104
34:4
35:105
53:106
54:107
106:108
107:109
139:110
140:111
207:112
217:113
247:114
268:115
290:116
291:117
---
aryballus,  n.,  a  bottle  with  a  short  neck  and  glob¬ ular  body  (Greek  antiq.)  —  L.,  fr.  Gk.  ap-jfiaA-
arytenoid,  adj.,  pertaining  to  two  small  cartilages in  the  larynx  (anat.) — Gk.  apuTatvoeiS-rjc/shaped like 
Derivatives:  arytenoid,  n.,  arytenoid-al,  adj. as,  adv.  —  ME.  as(e),  als(e),  also,  al  swa,  fr.  OE. ealsw
Derivatives:  as,  conj.,  pron.,  prep, as,  n.,  Roman  copper  coin.  —  L.  as  (for  *ass), gen.  assis,  prob.  
asarabacca,  n.,  the  wild  ginger  (bot.)  —  Com¬ pounded  of  L.  asarum,  ‘hazelwort’,  and  bacca, ‘berry
—  Gk.  Aaocpov,  ‘hazelwort’  of  uncertain,  possibly Sem.  origin.  Cp.  next  word.
Asarum,  n.,  a  genus  of  herbs  of  the  family  Aristo- lochiaceae  (bot.)  —  ModL.,  fr.  L.  asarum, ‘hazelwo
asbestine,  adj.,  pertaining  to  asbestos.  —  L.  as- bestinus,  fr.  Gk.  daJ^aTivoi;,  fr.  Sapeaxoi;.  Sec next 
asbestos,  n.  —  L.  asbestos,  fr.  Gk.  Sapearoc,  lit. ‘unquenchable,  inextinguishable’,  fr.  A-  (see priv.
—  Formed  with  subst.  suff.  -tte  fr.  Gk.  A®(16Xi),
‘soot’,  which  is  perhaps  rel.  to  Gk.  #£a,  ‘dry¬ ness’,  tifzi'j,  ‘to  dry  up,  parch’,  and  cog
```


## [2026-09-06T14:58:15.551Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -o -n 'گرشاه' MON_part1.txt MON_part2.txt | head; echo \"=== kravat ===\"; grep -c 'کراوات' MON_part1.txt MON_part2.txt; echo \"=== context ===\"; grep -o 'کراوات.\\{0,200\\}' MON_part2.txt | head -5; echo \"=== garshah ctx ===\"; grep -o '.\\{200\\}گرشاه.\\{200\\}' MON_part2.txt | head -5"
}
```


### [2026-09-06T14:58:17.132Z] TOOL RESULT

```
=== kravat ===
MON_part1.txt:1
MON_part2.txt:2
=== context ===
کراوات. 
کراوات: ۱ (.) بارچه‌ای باریک و 
=== garshah ctx ===
```


## [2026-09-06T14:58:19.596Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -B3 -A6 'کراوات' MON_part2.txt | head -40; echo \"=== part1 ===\"; grep -n -B3 -A6 'کراوات' MON_part1.txt | head -20"
}
```


### [2026-09-06T14:58:19.683Z] TOOL RESULT

```
8180-
8181-دککمه‌ها به بیراهن دوخته شود. (ف.) 
8182-
8183:کراوات. 
8184-
8185-فکنده‌سر: ۲ (ص‌مر.) ( کد.) خجل» 
8186-
8187-شر مسار. (تص.) کسی که در حال مراقبه 
8188-
8189-است. 
--
21578-ساحل. کرانه بودن چیزی را: حد و پایانی 
21579-داشتن (غالباً منفی آید). 
21580-
21581:کراوات: ۱ (.) بارچه‌ای باریک و 
21582-دراز که به يخه پیراهن بندند و از پیش سینه 
21583-آویزند؛ دستمال گردن. 
21584-
21585-کراویا: 73 (- کراویه - کرویا - 
21586-کراوی] (.) (گیا.) گونه‌ای زبره که بنام زيرة 
21587-سیاه يا زیرة سیاه کرمانی موسوم و دارای 
=== part1 ===
27574-می‌نو شتند؛ کاغد مصری. 
27575-
27576-پاپیون: «هوآجةه (۰) (جاد.) پروانه (غم.) 
27577:نوعی کراوات به شکل پر وانه. 
27578-
27579-پات: ۱( - باد) (.) اورنگ نخت. 
27580-پات: ۲2 (.) نوعی از زیان و باختن در 
27581-شطر نج از قیل لات و مات. 
27582-
27583-پاتابه: (م)قا-02 [- بایتابه - باتاوه <
```


## [2026-09-06T14:58:32.132Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -o 'گر: .\\{0,160\\}' MON_part2.txt | head -20"
}
```


### [2026-09-06T14:58:33.689Z] TOOL RESULT

```
185:گر: «و-« [ع. ف.] (ص‌فا.) کسی که 
6991:گر: 1.۲ |[ - فر ونکر نده ] (ص‌فا.) 
9708:گر: آو-10] (ص‌نسد.) کسی که آب 
11755:گر: 
17903:گر: ۱-۳ (ء کاریگر ] (ص‌شغ.) آنکه 
18113:گر: ۲-] ۵۲ ات تاک (رص‌فا.) 
22103:گر: ۷-۲ (ص‌فا.) ثواب کننده؛ 
26248:گر: 1-7 [- قمنجرء معر.] (ص‌شف.) 
26980:گر: ۲-۲ [معر .] (اص.) شجاع» دلیر. 
27332:گر: ۲ (.) (گاء) گیاهی است از 
27410:گر: 09۱080۲( (.) قسمی گدا که شاخی و 
27423:گر: ییا دای | () کنگر کیر ی 
30266:گر: «ع (- اگر ]| (حر. ربط» شرط) اگر ایزد 
31523:گر: (کد.) (کت.) دنیا. گ رک 
31524:گر: (کد.) دنیاء گرگ کهن: (کد.) 
31539:گر: و [- گروگر| (۱.) خدای تعالی. 
31541:گر: ۲ (.) تخت شاهی؛ سر بر. 
31551:گر: ۲ (ق.) سار ِ ببو سته. 
31553:گر: :7:0 اقس. گر ] گرگر سوختن: با 
31800:گر: :-00(۰: ۱- گ رگر | (قمر.)
```


## [2026-09-06T14:58:40.703Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY; grep -n -o 'gairi.\\{0,200\\}' ARY_latin_index_pages.txt ARY_pages.txt | head -10; echo \"=== zaxm ===\"; grep -n -o 'ZAXM.\\{0,150\\}\\|zaxm.\\{0,150\\}' ARY_latin_index_pages.txt ARY_pages.txt | head -10; echo \"=== ksar ===\"; grep -n -o 'k[sš]ar.\\{0,150\\}' ARY_latin_index_pages.txt ARY_pages.txt | head -10"
}
```


### [2026-09-06T14:58:42.543Z] TOOL RESULT

```
=== zaxm ===
=== ksar ===
```


## [2026-09-06T14:58:45.348Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY; wc -l ARY_pages.txt ARY_latin_index_pages.txt; head -30 ARY_pages.txt; echo \"=== grep persian ===\"; grep -c 'زخم' ARY_pages.txt; grep -c 'شار' ARY_pages.txt"
}
```


### [2026-09-06T14:58:45.416Z] TOOL RESULT

```
  16204 ARY_pages.txt
  15967 ARY_latin_index_pages.txt
  32171 total
[pdf page 1]
6 و۵
هندواروبابی_ 1010 1۵ 1000]
۵9 (۸9ا

۲1۹۸۸۱
۱۸۸۵۱۱ ۸۵ ٩۵۱۱
۸:۱۸
۲۸۵۳۵۸۵
[pdf page 2]
نج ۰
۰ پیشگفتار ۳
پیش گفتار
هدف این کتاب نشان دادن ریشه‌ی هند و اروپایی واژه‌های فارسی ناب است. این هدف موجب
۳۳۱ سس
ویژگی‌های زیر شده است:
۱- هیچ واژه‌ی فارسی که ریشه‌ی هند و اروپایی آن ناشناخته است آورده نشده است. صدها
واژه‌ی فارسی وجود دارد که ریشه‌پابی آنها تا حد پهلوی و اوستایی و حتی پارسی‌باستان پیگیری
شده است ولی ریشه‌ی هند و اروپایی آنها شناخته نیست. ممکن است برخی از آنها هند و اروپایی و
بسیاری از آنها غیر هند و اروپایی باشند. بهمین دلیل از آوردن اینگونه واژه‌ها خودداری کرده‌ام.
۲- کوشش کرده‌ام که پیگیری واژه‌های فارسی را در این مسیر انجام دهم: فارسی -> پهلوی >"
ارستایی -> پارسی‌باستان -> هند و اروپایی. ولی به دلائلی که در دیباچه آمده همیشه تتوانسته‌ام شاهد
اوستایی با پارسی‌باستان (و گهگان حتی شاهد پهلوی) واژه را ارائه دهم.
۰ ۳-هرجاکه توانسته‌ام واژه‌های همریشه‌ی کردی و بلوچی و افغانی و اوستی و سغدی و ختنی را
نیز آورده‌ام تا خویشی زبان‌های ایرانی امروز و رابطه‌ی آنها با پهلوی و اوستایی و پارسی‌باستان و
هند و اروپایی آشکارتر گردد. ۱
۴- برای نشان دادن خویشی زبان‌های هند و اروپایی و ریشه گیری آنها از یک سرچشمه‌ی
شترکك» واژه‌های همريشه در زبان‌های سانسکریت و ارمنی و یونانی ولاتین و آلمانی و انگلیسی و
روسی و غیره را نیز ارائه داده‌ام. هر آینه» این واژه‌ها (با وجود همريشه بودن) هميشه هم معنی نیستند. :
۵- هرجا در درستی ریشه‌یابی‌ها شک داشته‌ام» با آوردن واژه‌ی "شاید" به خواننده هشدار
=== grep persian ===
6
25
```


## [2026-09-06T14:58:50.362Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY; grep -n -o '.\\{80\\}زخم.\\{120\\}' ARY_pages.txt | head -8; echo \"=== shar ===\"; grep -n -o '.\\{60\\}آبشار.\\{150\\}\\|.\\{60\\}شاریدن.\\{150\\}' ARY_pages.txt | head -8; echo \"=== gar mountain ===\"; grep -n -o '.\\{60\\}گرشاه.\\{100\\}\\|.\\{80\\}کوه.\\{120\\}' ARY_pages.txt | head -8"
}
```


### [2026-09-06T14:58:50.744Z] TOOL RESULT

```
=== shar ===
=== gar mountain ===
```


## [2026-09-06T14:58:53.991Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY; echo \"=== زخم ===\"; grep -n -A3 -B1 'زخم' ARY_pages.txt | head -40; echo \"=== آبشار ===\"; grep -n -A3 -B1 'آبشار' ARY_pages.txt | head -20"
}
```


### [2026-09-06T14:58:54.050Z] TOOL RESULT

```
=== زخم ===
3708-یادداشت:
3709:معنی اين واژه در سانسکریت: صدمه زدن؛ زخمی کردن.
3710-معنی این واژه در زبان‌های ژرمنی: سوراخ کر دن؛ سفتن؛ مته.
3711-معنی این واژه در زبان یونانی: شخم,
3712-ی او ستایی ([۸۷۳87)+ ۸12۸ سوئدی (8(801577): 0
--
7041-[pdf page 239]
7042:۰ | خست (به چم آزخم")» خستن (به چم "آزردن» مجروح کردت)
7043-دانمارکی (04۸۷1517)(شاید) 0 ایرلندی کهن (ناکلقا صام:. . تدای
7044-سوئدی (5178015/4)(شاید) 0۸ گالی (ل3لاتاه): .1۳
7045-هلندی (007۴7)(شاید) ۳007۳ ,0082( ۰ ۰
--
9259-یادداشت, ها
9260:۱ در زبان پهلوی واژه‌ی 3381110۸07 چم "زخم کردن" را داشت. ی (
9261-۲+ چم این واژه در آلمانی: شکاف» خراش؛ خراشیدن,
9262-۳ چم این واژه در لترنی: شکاف.
9263-ّ
--
9895-چم این وه در زب انگلیسی: نیزهه شکه. ۱
9896:۲- چم اپن واژه دز زبان‌های ایرلندی کهن و لیتوانی: زخم؛ زخمی کردن
9897-پهلوی (7ل۳۸): 77۸۸ افغانی (پشتو) (/۸۳0[7۸): هلق7
9898-[pdf page 335]
9899-۶ | رف
--
15240-ا
15241:والانه ولانه (به چم *زخم", *جراحت") / ۵۱۵ ٍ
15242-پسگشت‌ها رده با ادن لغت‌نامه دهخدا: ۳۳۹۹
15243-9 (5رتغ۲۲) +8147
15244-پادداشت:
--
15277-چم اين واژه در زبان ایرلندی کهن: خون.
15278:چم اين واژه در زبان‌های رومانس: زخم» زخم‌پذیر» آسیب‌پذیر,
15279-
15280-اوستایی (/4۷287): انگلیسی (7لولءا6۸0): ۳
15281-۸ ,۷25 ,۸۷01 (۷۸۷0 دانمارکی (0۸//37): ۷8 ا
=== آبشار ===
```


## [2026-09-06T14:58:59.793Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY; grep -n -i 'gwer\\|g^wer\\|ĝwer' ARY_latin_index_pages.txt | head; echo \"=== gairi/giri ===\"; grep -n 'giri\\|GIRI' ARY_latin_index_pages.txt | head"
}
```


### [2026-09-06T14:58:59.863Z] TOOL RESULT

```
=== gairi/giri ===
12383:GIRIW, GIRTI, GERAS °F fBwwxrry Site
12623:GUR ALBANIAN) gist GIRIS AGANSERIT) cy Sse
12633:rray Misas aaGcail GIRIA (LITHUANIAN) ip
12644:{OLD CHURCH SLAVIC) op 59% GHIRIAN, GHIRIN, GIRIN
12966:GROB RUSSIAN) 3) GIRI-H (SANSKRIT) cy Suite
```


## [2026-09-06T14:59:05.389Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY; sed -n '12618,12650p' ARY_latin_index_pages.txt; echo \"=== page tag near ===\"; awk 'NR<=12650 && /^\\[pdf page/ {p=$0; n=NR} END{}' ARY_latin_index_pages.txt; awk 'NR<=12650 && /^\\[pdf page/ {p=$0} END{print p}' ARY_latin_index_pages.txt"
}
```


### [2026-09-06T14:59:07.128Z] TOOL RESULT

```
Vee seb aby LINGUERE (LATIN) 3
ethool
use Sih
GARS LETTIC) (63) 5.93 GAIRIVA, GAIRI—:(AVESTAN) .ot)
GARIAN (OLD PRUSSIAN) 3553.4, GRIWAG (PAHLAVI) 5 3h
GUR ALBANIAN) gist GIRIS AGANSERIT) cy Sse
| DEIROS (GREEK) gbiy
| [REFERENCES beth (OLD CHURCH SLAVIC) pS 59%!
PoKoRM=SSSC*~CS*~S*« GORA
MACKENZIE: GORKA (POLISH) ghngs
(BILL) 118, (NECK) 124 GORA (RUSSIAN) «53,
BUCK: 25 HORA CZECH) Soy
MALLORY: 159 GORA (SERBIAN) 1 po
Av seb day HORA (BOHEMIAN) goa »
rrayv foe Sead HORA L(SLOVAR) 5\ jhel
rray Misas aaGcail GIRIA (LITHUANIAN) ip
> Jeetlsol
Kee gtT ob5 22 05s aol een
13310 pay "Hg" 9 Ran” ee atl lads he 29 5 ual
[pdf page 434]
SY
FOL gee Sed Seas F
GRADE .(DANISH) isl GAREZ- s(AVESTAN) lk, 13!
GRATA (SWEDISH) 8 yo (PAHLAVI) 65 shy
GRATE NORWEGIAN) (5533 GRIYSTAN, GRISTAN, GRIY-
GROETEN (DUTCH) gale :(KURDISH) 3. Ss
{OLD CHURCH SLAVIC) op 59% GHIRIAN, GHIRIN, GIRIN
GERKATI GHARGHARA, (SANSKRIT) <4 Sule
GURKATI ARUSSIAN) yu GHURGHURAYATE, GHARGHARITA
HERCHETI H(CZBCH) Soy HIRRIRE LATIN) ops
_ GRETAN GOTHIC) S35
‘REFERENCES bok, HOLD SCANDINAVIAN) gS sles!
POKORNY. =—SSSt*~S~S~S~«D GRATA
=== page tag near ===
[pdf page 1]
```


## [2026-09-06T14:59:15.595Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==50' SYN.txt | head -60"
}
```


### [2026-09-06T14:59:17.291Z] TOOL RESULT

```
acq 128 f.
2. Lat. mons, montis (> It. monte, etc.), W. mynydd, Corn. meneth, Br. menez ‘mountain’, Av. mati- ‘mountain top’, fr. the root seen in Lat. é-, pré- mineére ‘stand out, project’ (cf. NE eminence, prominence in physical sense), minae ‘projecting points, threats’. Walde-P. 2.263. Ernout-M. 628 f.
Lat. adj. monténus, VLat. *mon- taneus (cf. subterrdneus, etc.), neut. pl. *montanea ‘mountainous regions, moun- tain chain’, whence It. montagna, OFr. montai(g)ne (> ME mountain), Fr. montagne, Sp. montafia, which have en- croached on the shorter form or even displaced it. Sp. monte now ‘woods’. REW 5664, 5666.
Lat. collis, : Grk. xodwvés, ete., above, 2. Hence It. colle, collina, Fr. colline, Sp. colina, collado, Rum. colina (neolog.).
Lat. clivus ‘slope, hill’ : Goth. Alains ‘hill’, Grk. Airs ‘slope, hillside’, fr. IE *klet- ‘bend, incline’, in Lat. clinare, Grk. KXtvea, Skt. cri-, NE lean, ete. Walde-P. 1.490 ff. Ernout-M. 197f. Walde-H. 1. 236.
Sp. cerro ‘hill’, also ‘back of the neck, spine’, fr. Lat. cirrus ‘tuft of feathers, crest (of birds)’, REW 1949. Other Sp. words for ‘hill’ are otero fr. Lat.
altarium ‘high altar’, poyo (cf. It. poggio ‘hill’, Fr. pui in place names) fr. Lat. podium ‘balcony’. Cf. Menéndez-Pidal, Orig. del espafiol 425 ff.
Rum. deal ‘hill’, loanword fr. Bulg., SCr.-ChSl. délit ‘part’, through ‘bound- ary’. Tiktin 515. Berneker 195.
3. Ir. sliab, NIr. sliabh ‘mountain’ : W. llyfr ‘heel of a drag’, OHG slitfan ‘slip, glide’, etc. (*sleib- beside *sleidh- and *sleub-, Walde-P. 2.391, 707, 710), the development being through ‘slope’ (cf. NE slope fr. pple. of OF slitpan ‘slip’), hence ‘hill’ (cf. Lat. clivus, Goth. hlains, above), ‘mountain’. Thurneysen, Gram. 117. Stokes 319. Pedersen 1.84.
W. mynydd, Br. menez ‘mountain’ : Lat. mons, etc., above, 2.
Ir. telach, tulach ‘hill’ (also NIr. in phrases) : Grk. ridy ‘swelling’, Lat. tu- mulus ‘mound’, etc. Walde-P. 1.71@.
Tr. cnoc ‘hill’, Br. krec’h, OBr. knoch (W. cnwceh ‘boss, knuckle’) : ON hnakki ‘nape of the neck’, NE neck, etc. Walde-P. 1.390 ff. Pedersen 1.160.
Ir. bri, W., Br., Corn. bre ‘hill’ : OF beorg, etc. below, 4.
W. bryn ‘hill’ : Ir. bruinne, W. bronn ‘breast’, Ir, bri, W. bru ‘belly, womb’, NE breast, etc. Walde-P. 2.197. Peder- sen 1.86, 376.
4, Goth. fairguni ‘mountain’ : OF firgen in epds., as firgen-gat ‘mountain goat’, and prob. a loanword fr. Celtic *perkunia, represented by Hercynia silva (with regular Celtic loss of initial p), this further connected with Lat. quercus ‘oak’, Relation between ‘woods’ and ‘(wooded) mountain’, as elsewhere. Walde-P. 2.48. Feist 137 ff.
Goth. hlains ‘hill’ : Lat. clivus, etc., above, 2.
ON fjall (fell), Dan. fjeld ‘mountain’, Sw. fjall ‘high mountain’ (ME, NE fell fr. ON) : OHG felis, NHG fels ‘rock’, Skt. pasana- ‘stone’, etc. (1.44). AL
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
cr ee ra SS NR
|
Digitized by Arya Samaj Foundation Chennai and eGangotri
THE PHYSICAL WORLD IN ITS LARGER ASPECTS 25
though the root connection is uncertain, the sense ‘rock, stone’ is more widely dis- tributed and prob. earlier. Walde-P. 9.66. Falk-Torp 223.
Dan. bjerg, Sw. berg, OE beorg (‘moun- tain, hill’ and ‘burial mound’, in former sense replaced by the Fr. forms, in the latter sense NE barrow), OHG
```


## [2026-09-06T14:59:22.332Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR>=48 && NR<=51' SYN.txt | grep -n -i 'gairi\\|giri\\|gora\\|hrvat' | cut -c1-500"
}
```


### [2026-09-06T14:59:23.798Z] TOOL RESULT

```
26:or eae eae ON ald Lett. kalns; pakalne NG Bovvd; Bouvaxe Dan. Odjerg, fjeld; bakke ChSl.  gora; chlitmit we Lat. | méns; collis, clivus Sw. berg (fjall); backe SCr. gora; brijeg, brezZuljak It. montagna, monte; col- OE beorg, din, munt; hyll (hum)
28:line hill Pol. gora; pagérek, Sp. montajia; colina, cerro Du. berg; heuvel wzg6rek Rum. munte; deal, colina OHG _ berg; buhil, houc Russ. gora; cholm Ir. sliab; telach, cnoc, bri MHG berg; biihel, hiibel, Skt. giri-, parvata-, acala-, NIr. — sliabh; cnoc (tulach) houc etc. W. mynydd; bryn (bre) NHG berg; hiigel Av. gairi-, paurvata, bara- Br. menez; Icrec’h, bre zah-, OPers. kaufa.
77:6. ChSl. gora, etc., general Slavic for ‘mountain’ (in some regions ‘forest’, as always Lith. gire, 1.41) : Skt. giri-, Av. gairi- ‘mountain’, and prob. Alb. gur ‘stone’. Walde-P. 1.682. Berneker 329. Further connection with Skt. guru-, Grk. Bapis ‘heavy’, through the notion of ‘heavy, solid mass’ (Thumb, IF 9.299) is plausible. Cf. Skt. acala- ‘mountain’ fr. adj. acala- ‘immovable’.
79:The usual Boh. and Pol. words for ‘hill’ are dims. of gora, as Boh. pahorek, Pol. pagérek, wzgérek.
```


## [2026-09-06T14:59:28.330Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n 'gar \\[\\|^gar\\b\\|gar  \\[' PHD.txt PHD_mackenzie.txt | head -20; echo \"=== NYB ===\"; grep -n '^gar\\b\\|gar-  \\|garr' NYB_vol2_glossary.txt | head -20"
}
```


### [2026-09-06T14:59:28.387Z] TOOL RESULT

```
PHD.txt:148:tahm [thm | =M, N ~] strong, brave. tak [t^k' | N ~ 'vine'] branch. tohm(ag) [twhm(k') | M twhm, -g, N tuxm, -a] ... wanigar [wnykl) prodigal.
PHD.txt:161:a- P- | M ?-] privative prefix, un-, Jess, а D] then (generally with a suffixed pronoun, e.g. 8-š). ab [M YA < А my';?p | M >b, N ~] water. B Soy 277 abad рр? | M Ра, N ~] populous, thriving, prosperous. ~ih: prosperity. ābādān [f*?t?*n' | N ~] thriving, prosperous, cultivated. ~ih: prosperity, cultivation. abādixšā(y) 'P?th? (d), v. pādixšā(y)] without authority, powerless. ~ih: powerlessness; anarchy. abādyāwand Pf?tyd”wnd | J ?b’dywn<d>] powerless, weak. ~ih: powerlessness, weakness. арар [LW TE < A lwt-h | M?Pg, N (a)bā] with. ~ih Dë kuk) company, assistance. abāgēnīdan, abāģēn- [^P'kyn-ytn!] accompany. a-bahr РРА] portionless, deprived. abām Pf?m | P ?bmyh, N (a)wàm] loan, debt. Abàn PPn! | M'0x, N ~] cal. 8th month; roth day. aband (nd, v. рапа | M ?bnd] erring. “АҺ: error. 'abar [ODM < А дат; bl | M "be, N bar] up; on, over. ~ āmadan: rise (sun). ~ āxistan: rise up. ~ āxrāmīdan: step up. — burdan : undertake. ~ madan: cope with, comprehend. ~ nigeridan: consider. ~ nihumbidan: conceal. ~ niSastan: sit, be enthroned. ~ nišāstan: seat, install. ~ rasidan: come to, upon. ~ rasidan б: attain. tabar Dél higher, superior. ~ag [-g | MP brg] superior. ~agan(ag) [-k’n(k)'] superior. --dar [-t, Zenit | M ?brdr] higher. ~dom [-twm | M ?brdwm] highest. —domih [-twmyh] superiority. abargar [5/21 god, divinity. abarig(àn) ['Bblyk( ny] = abarag. abarig DPryk! | M ?Pryg, J ?Pry] other.
PHD.txt:172:a-dàd [471], a-dādestān [?- DYNA, -dtst^n'] illegal, unjust. ih: injustice, illegality. a-dahm P@?hm] uninitiated. -ādan [- m! | P dn, N ~] suffix forming secondary infinitives. a-dàn [??п! | M din ignorant. ~ih: ignorance. «адап [??!] wealthy, solvent; wealth. “Аһ: wealth. a-dard [Pdlt'] painless. áüdaróg [wk], ātaxš 1 ~ : the simplest kind of sacred fire. adehig (’dhyk'] indigenous, domestic. adén [?tyn! | М dun) entry. *adén- ['dyn- | = M] bring, lead. ādišt Ptyst'] fire-stand. : ae. D i ‚ (ed уд ádüg Ptwk! | M "?dwg] capable. adur twr! | Mdwr, N ādar] fire; the god ‘Fire’; cal. gth month; oth day. adurestar [twrystl] ashes. ~én [-yx!] ashen. adur- gah [twrg’s] fire altar. ЖЕСЕ, āfrāh PSPs | М ??р?Л] teaching, doctrine. alva 2 KM N facaz\ ‘ace Luch >a-frasāwand [' Bl? wnd] imperishable. afridan, àfrin- / āfur- Pžlytn', ?Blyn-, *pwl- | M 'p(w)ryd, "po -— P >f+yn-, N āfarīdan, afarin-] praise, bless; create. áfrin ['pryn! | M?pryn, N áfarin] praise, blessing. 9544. "tien ~agan [-k”n!] Afrinagan prayers. аїгӧёар [ēlwšk! | N ~ a] a sweetmeat made of flour, butter, and honey. ‚ *afsálàn Pfs'Px!' | (N ābsālān)] springtime. afsān (?psn! | (M ?р?ле), N afsāna] story, fable. afsardan, afsar- ['psi-tn'] cool down. afsārdan, afsar- Pfs?/-tn'] cool, freeze, extinguish. „išn: cooling. afsáy-, v. afsūdan. afsénistan, afsén- [*5syx-stn!, v. abesihén-idan] destroy. --i$n : destruction. afsin [swn | N afsün] spell, incantation. M psan afsös [psws | N ~] scorn, mockery. ~gar [-g/] mocker. afsūdan, afsāy- ['pswtn!, *ps*d-] enchant, protect by spell. afšāndan, afšān- [5Zz?n-tn! | N ~] spread, scatter, sow. afSardan ['5?Its! | N ~] = afšurdan. af$urdan, afšār- 'Pfwltn!,?pP?l- | N ~] press, compress, crush. āfurīdan, afur- ?fwl-ytn', v. Afridan] create. ~išn: creation. -ag [-À! | M -g, N -a] suffix forming (i) adjectives, from nouns and verbal stems, (ii) nouns, from adjectives and present stems.
PHD.txt:181:a-gumég Pgwmyk! | M ?gzumyg] unmixed, pure. ~ih: purity. 33? águstan Pkwstn! | M ”gwst] hang up, suspend. 8.45% X wc āhan pA(y)n! ,^s(y)n! | M ?hwn, N ~] iron. ~én ['synyrn!] iron, of iron. ~gar [-kl | N ~] blacksmith. ahang [hng] pull, draught. āhanjīdan [?hncytn!] = āhixtan. ahanüz Phnwe | M *hnwn-c, N haniiz] yet, still. āhen = āhan, q.v. аһа Phyt' | M QYAyd] stain, impurity; confused. ^Àh : pollution; confusion.
PHD.txt:189:áhüg [TYBA < A ру; ”hwk! | MQyhwg, N āhū] gazelle. ahunawar [hnw!] the holiest prayer, beginning Yadā ahū wairyē. a-hunsand [Phwnsnd] dissatisfied. ^h : dissatisfaction. ahy [KZ Y < А k-zy | М hy] soon(est), first. ajģahān [>20/?л! | М ieikin, N azgahan] lazy, indolent. “АҺ: laziness, indolence. ak P! | N dk] evil, harm. -ak LIN ~] diminutive suffix. a-kámagómand [k mk’ wmnd] unwilling. a-kanārag ['kr?]k! | M ?qn’rg] unlimited, boundless. ~ih: boundlessness. a-kard Pārt! | (M °gyrd)] not done, undone. Akoman ['kwmn! | М ?qwmn] Evil Thought, an arch-demon, akómand ["£wmnd] evil, harmful. alā [Py] oh! alas! Аар [STLA, STRA < A £t ;?lk! | (М rel side. alálag PPH! | N lala] anemone. ālāy-, v. ālūdan. Aleksandar Piksndl | M *Ixsyndr, N Iskandar] Alexander (of Macedon). almās(t) Pim?s(t') | (M ?rm?s), N almas] steel; diamond. аадар [?/wtk'] defiled, polluted. АҺ: defilement. ālūdan, ālāy- Photn!, *Pd- | (M ?rwd), N ~] defile, pollute. Aluh Plwh | M "If, N ~] eagle. Xum [lum] millet. N~ amā [LNE < A l-nh | М ?*°h, N má] we, us. Amadan, āy- [Y ATWN-tn! < А y twn, V*th | M?mdn,?y-, N ~] come. amahraspand [?mhrsbnd | M (?)mhr’spnd] a Holy Immortal, a-mar [ml] countless, innumerable. amar [ml | N ~] reckoning, consideration. āmār- [?m?1-] reckon, calculate. ~išn: reckoning. a-marag [mlk') countless. amaraģān [?mlk’n'] generality, commonalty. ~ig [-yk'] general. ~iha [-yh’] in general, generally. a-marg [mig] deathless, undying. ~ih: deathlessness, immortality. ámárgar [?m’lgl | N ~] reckoner. amāwand [?m'wnd] powerful, strong.
PHD.txt:256:bayaspānļīh: mission, embassy. ~ig [-yk'] post-(horse). Бах [Pc | N ~] hawk, falcon. bāzā [b’c’y | (N bāzū)] arm. ~banag [-p'nk'] arm-guard, brassard. bazaģ [bck' | М beg, N ~a] sin, evil. —ih: = bazag. bazakkar [bckkl | M bzkr] sinful, sinner. bāzā-zanišnīh [by znfnyh = Av. bázu.jata-] a degree of sin. bazišn [dcšn'] division, part. bazm [bzm | — M, N —] meal, feast. ~-awurd [-zolt! | N ~] a sort of canapé. 1bë [BRA < A br | MP] but; out; ~... (enya), except. ~...enya...né: except... (otherwise)... not. ~ az: without. m 2be [BRA | M P, N bi-] particle with verbs, with 6, of indefinable function. -bed [-pt' | M -byd, N -balilud] suffix, -lord, -master. bēdom [bytwm | M bydwm] furthermost. béganag [byk’nk' | N ~a] strange; stranger. bégar [byk”/ | N ~] corvée, forced labour. béh [byh | N bih] quince. bel [by] | (M. Бу), N ~] spade. bélür [bylwl | M bylwr, N bilür] crystal. bérón [bylwn' | M byrwn, N bérün] outside. bëš [bys] pain, sorrow; harm, hostility. — burdan: bear hostility. bēš-, —i&n, v. bištan. bēšāz [byš(*)z] healing, medicinal. bēšāz(ēn)- [by?z(yn)-, byf?)c(yn)- | M byP?z-] heal, cure. —išnih: healing. bēš-burdār [byšbwlť’[] hostile. bëšidan [bysytn'] = bištan, bēšūmand [byš?*wmnd] sorrowful. béwar [Буш | M bywr, N ~] myriad, ten thousand. P bid [руй | P byd] again. bidaxš [byths] viceroy. *bifagàn [bch'n!] medicinal. bim [bym | = M, N ~] fear, terror. ~gén [-kn'] fearful, terrible. ~génih: fearfulness. --6mand [-'wmnd] fearful. *bistag [bstk! | N busta] hazelnut. biš [byf | N —] aconite. bištan, bé&- [bys-in' | M by$t, bys-] hurt, torment. ~išn: harm, torment. bize&k [dešk! | M bzyšk, N pizišk] doctor, physician.
PHD.txt:289:brin [5/yn'] cut, division, delimitation; limited, determined. ~gar [-k/] determiner; decisive.
PHD.txt:298:čāšt [ой | N ~] lunch, meal. 1~ag [-k'] food. &а$їар [c'štk'] doctrine. čāštan, čāš- [c?s-tn'] teach. ~išn: teaching. čatrang [cting | (Ar. šatranj)] chess. *taw(la)gan [cwpk'n!! | Ar. sawlajan, N čaugān] (curved) polo-stick ; polo. CaxSágih [ch kyh] (sense of) taste. čaxšišn [chsfn! | M, J схі, N ¿aš-] taste, flavour. 148 [ME < A mh | M cy, N či] what, which. ~ ray: for what, why. ~ih: quiddity, essence. tčē [ME, v. 166] for, because, since, as, that. &ë-ëwënag [ME ^ dwynk!] how. ~ith : circumstances. čegām-iz [су?т-с | M cyg^myc], —-6(w): a little; whatever. Cegámag [cyk”mk! | N &(ag)áma] song, snatch. €éh- , —išn, v. idan. *téhag [cyhk'] grief. čehel [40 | N chil] forty. Céh-widarag [cyhwtlg] = činwad puhl. čēlān [cy”x! | = M, N ~] dagger. ~gar [-kl, -gl | N ~] swordsmith. Cér [cyl | M cyr, N —] victorious, triumphant, brave. —Ih: bravery. Cérihistan, Cérih- [cylyh-stn'] triumph, be victorious. īčīdan, čīn- [cytn', cyn- | M cyydn, cyn-, N ~] gather, pile up. ~išn: gathering. *čīdan, čēh- [cytn', cyh- | M cy-] mourn, lament, grieve. ~i8n : lamentation. ~i$nig¢ : mournful. ihr [cyhl | M cyhr, № ~] form, shape, appearance, face. žčihr(aģ) [cyhl(k') | M сулу, P -g, № ~] seed, origin; nature, essence. Cihrénidan, čihrēn- (cyhlyn-ytn'] form. Cihrig [cyhlyk'] natural. čihr-šnāsīh [суйру] physics. čim [c(y)m | M сут, N ~] reason, cause, purpose, meaning. ~ (ray): why? Cim-gó6wáàgih [сут gwh’kyh] logic. čimīģ [cymyk!] purposeful. čīn-, ~i8n, v. idan. čīnag [cynk! | P cyng, N ~a] grain, bait. Cinàr [су | N ~] oriental plane tree. činwad [cynw(p)t'], ~ puhl: the ‘divider bridge’ which separates the souls of the righteous dead, who cross, from those of the wicked, who fall off.
PHD.txt:316:drón yaštan: consecrate the sacrificial bread. drēš [410] mark, branding; punishment. ~ag [-k!] *desolation. drēšīdan, dro$- [d/w$-ytn'] brand. drēūšom [dlwšwm] mark. droz-, v. druxtan. drózan [dlwen! | M, J drwzn] lying, liar. ^h: falsehood. drubušt [di(w)pwst'] fortress. ~ih: defence, fortification. drüdan, *drün- (HCDLWN-tn! < A У hsd | M ача, (dwr-), N durüdan, diraw-] reap, mow. drust [drw(y)st' | (M dryst), N durust] right; well, healthy. —Ih: righteous; health. drustabed [drwystpt'] chief physician. društ [dlwšt' | N durust] harsh, rough, severe. ~ih: harshness, severity. ~-Awaz, ~-éwaz [-p'c, ~yw’c] harsh-spoken. druwand [dlwnd | M drwnd] evil, sinful, unrighteous. ~īh: sin, unrighteousness. druxtan, dróz- [dlwhtn', dlwc- | M drwxt, drwz-] lie, deceive. druz [dlwe | (P drwj)] demon. айа [dwt! | M dwd, N ~] smoke. düdag [dwtk! | N —a] family. dudigar [dtykl | M dwdygr, N digar] second. duj-, = duš-. ~-daft [dwsdpt'] ill-breathing, short of breath. ~-dānāg [dwšd”7?k!] ignorant. ~-dén [dwšdyn' | M dwjdyn-] of evil religion. «=dēys*rīh [dwsdwyslyh] the evil eye. ~-gand (dtwsgnd | P dwjgnd] stinking. ~-gandih: stench. dum(b) [dwm(b') | N ~] tail. ~dmand [-'wmnd) tailed. ааг [LH YK'! < А rhyq; dul | M dur, N ~] far, distant, remote. durgar [dwlgl | N ~] carpenter. dusraw [dwslwb!] notorious, dishonoured. ^Ah : notoriety, dishonour. duš- [dws- | = M] ill-, evil-. ~īh: evil, wickedness. ~-абаһ [dw??^ Es] foolish, stupid, ignorant. ~-абаһіһ : foolishness, stupidity. ~-arz [2 ic] worthless. 7--Ca&m [-cém] envious. —-Ca$mih: envy. ~-tihr [-cyhl | M dwfcyhr] ugly, hideous.
PHD.txt:378:galēģ [glwk' | N guld] throat. бато [gm | = M, N ~j pace, step, stride; a yard (3 ft.). ~ í dó pay: a pace (s ft.). -рапаб [-k’nk' | M eng, N -gàna] suffix forming numerical adjectives, -fold. бапа [gnd | N ~] stench. gandag [gndk' | (M gng), N —a] foul, stinking. ~th: stench. ģandanāģ [gndn’k' | N gandanā] leek. gandum [Hš < A nth | (M gnwm), N ~] wheat. ganj [gnc | (M gnz), N e treasure, treasury. ~war [-wbl | M -wr, N ~] treasurer. ģan(n)āģ [gr &! | (P gnd?g)] foul, corrupt (v. gandag). ~ ménó$g the Evil Spirit. ~ih: corruption. gar [gl] mountain. -gar [-Al, -gl | M -gr, N ~] suffix forming actor nouns. -gar [-£1| M -g’r, N ~] suffix forming actor nouns. garan [gPn! | M г?л, N girán] heavy, serious, difficult. АҺ; heaviness, weight. garasman [glsm’n' | М ртт?п] = garddman. gard [g/t! | N ~] dust. gardan [gitn! | M grdn, N ~] neck. ģardānāģ [gl h] die (for gaming). gardanidan, gardan- [gl n-ytn! | M grd(y)nydn, N ~] turn (tr.). gardidan, gard- [git-yin' | M grd-, N ~] turn, revolve. ~išn: revolution, turning. garm [gim | M grm, N ~] warm, hot. «„«ih: warmth, heat. garm-ābag [gim'pk! | N ~a] bath-house. garmāģ [glm^ k! | М grmg, N garmá] warmth, heat. g£armóg [gimwk!] warm, ardent, fervent. garmówar(ih) [glmwk wl(yh)] heat ordeal. ģarmsēr [gimsyl | N ~] warm region, lowlands. garódman [glwtmn' = Av. garó dəmana- | M grdm?n] paradise. ~ig [-yk'] (worthy) of paradise. yarranag [g”7k! | M grn’g ?] thunder. yarranidan, yarran- [gl’n-ytn' | (N yurridan)] roar, thunder. ~i$n: roaring. garzag [gick! | N garza] snake, serpent. garzidan, garz- [glc-ytn'] complain; confess. ~i$n: complaint. ~iSnig : complaining. gaw [gw!'] hand (daevic). базу [ТИРА < А twr) | M gw, N ~] ox, bull, cow; astr. Taurus. gawars [PZ < A prg’; g”wls | N ~] sorghum, giant millet.
PHD.txt:398:P hd [Aw' | = P] that, he. Hóm [kwm | N ~] the sacred plant Haoma (ephedra). homānāģ [h(w)m’rk' | N hamana, J xumana], 6 .. . ~: like. ~th: likeness. hómast [hwn'st!] various series of prayers. hómyjén, -ïg [hwmyn!, -yk'] of Haoma. ~ӧтапа [-'wmnd] prepared with Haoma. Ногааа [hwrdt' | M hrwd'd, N Xurdād] Perfection, the fifth Amahra- spand, guardian of water; cal. 3rd month; 6th day. hdsag [hwsk' | М лое, N xēša] ear of corn, cluster; astr. Spica, Virgo. hēšēnīdan, hoSen- [hwsyn-ytn'] (cause to) wither. hēšīdan, hēš- [hws-ytn' | M hwi-, N x~] dry up, wither. héy(ag) [hwy, -k! | M hwy] left(-hand). Hróm [hlwm | M hrwm, N Рат] Byzantium, Rome. ~ayig [-dyk'] Greek, Byzantine, Roman. hu- [hw- | = M] good-, well-. ~ih: good, goodness. hu-bóy [hwbwd] sweet-smelling, fragrant. ~th: fragrance. hu-čašm [hwesm] unenvious, benevolent. ~ih: benevolence. hu-čihr [hweyhl | M hweyhr, (N xujir)] fair, beautiful. hudà(ha)g [hwa?(h)k' = Av. hudàáh-] good, beneficent. ~th: beneficence. hu-|-dast [hwdst'] skilful. ~-dén [-dyn'] of good (i.e. Mazdean) religion. ~-ddsSag [-dušk'] very pleasing. m-ēwāz [-"yw'c] of good speech, affable. —-ëwàzih : affability. ~-fraward [-plwit'] blessed, the late. hugar [hwgl] easy; beneficent. hu-|-&ówisn [hwgwbsn'] of good speech. ~-gugar [-gwk’l] easily digestible. ~-kunign [-kwnsn'] of good behaviour. „-mānīh [-m’nyh] good-mindedness, benevolence. humat [hwmt' = Av. humata-] good thought. humāy [hwm’y | N ~] a bird of good omen; eagle. hu-menišn [hwmynsn'] of good thought. hu-murwāģ [Awmwlw’k'] auspicious. hunar [hwal | M hwnr, N ~] virtue, ability, skill. hunarāwand [kwn wnd | M hwnr'wynd] skilled, virtuous. ~th: skill, virtue. hunarómand [kwn wmnd | N hunarmand] = hunarāwand. hunidan [kwnytn'] extract, express (juice). huniyág [/sonyd?k! | N xunyá] delightful. ~th: delight, entertainment.
PHD.txt:412:J jad [y’t'] share, portion. Yadag [ytk! | M jdg] omen. tļadaģ [ytk'] form, property. jadag [y’tk' | M del share, portion; case, cause. jadag-g5(w) [y tkgwb'] advocate, intercessor. ~ЛЬ : intercession. jadag-wihīrih [ytkwhylyh] transformation, alteration. Jadarih [y2?lyh] maintenance. *fadisn [ytsn'] (accidental) quality, property. ~ig [-yk'] accidental, non-essential. jadiig [y?te&! | M j?dwg, N jadi] sorcerer, magician. — h: sorcery, magic. *jay [у?л | N ~] sissoo tree. jagar [yal | N jigar] liver. Jah-, v. jastan. jahišn [yhysn' | J jhysn-] chance, fortune, omen. Jahišn-ayār [yhyfn hdyb'l | N n. pr. jhiy?r] fortunate. ~ih: good fortune. jahüd [yhwt' | N juhiid] Jew. jām [y m | N ~] glass. јат [M ANE < A mn-h; ут | M Pm, N <] vessel, goblet. lfamag [y”mk! | N јата) = *jām. атар [y mk! | М ртр, N fama] clothing, garment. jang [yng | M jnng, N ~] struggle, battle, fight. Jar [ywl | M рт] time, occasion. jastan, jah- [ystn!, yh-] happen, occur, chance (to be). ~išn, v. jahišn. Jašn [yfn! | N —] celebration, festival. jaw [ŠZ < A £% | N ~] barley. Jāwēd [y wyt! | (P ywyd), N ~] eternal.
PHD.txt:422:kabk [АрА! | N ~] partridge. ~-anjir [acyl | N ~] a kind of francolin. kabód [kpwt! | N ~] grey-blue; pigeon. kabótar [kpwil | M kbwtr, N ~] pigeon. kāč [с | N kāš(ki)], ~ ka: would that, if only. кадар [01А] game, joke. кадар [ktk' | M kdg, N kada] house. ~-banig [-b'mwk! | N Radbanü] mistress, lady of the house. ~ig [-yk'] domestic; servant. ~-xwaday [-hwty | P gdyxwd?y, N kadxudā] householder, master of the house. kadām [ktm | M kd?m, N кийат) which, what. c--iz-é(w) [-c-H D] whichever. kadar [kt] who, which. 7-iz-é(w) [-c-H D] whoever. kaf [kp | N —] foam, slime. kaf-, v. kaftan. kafč [kpc | N ~] ladle, skimmer. ~ag [-А! | N ~a] spoon. kafš, ~ag [kps, -k! | N Аар] shoe. ~gar [-k/ | N ~] shoemaker. kaftan, kaf- [kp-in' | P kft, kf-] fall. kah [TBNA < A tbr | N ~] chaff, straw. kān-, ~i§n, v, kāstan. _ kahas [kts | М khs] channel, sewer. kāhēnīdan, káhén- [R'hyn-ytn!] decrease, lessen (tr.). kühidan [P hytn! | N ~] = kastan. kahist [ksst'] least. kah-rubāy [Ара | N —rubá] amber. kahwan [khwbn' | M qhwn, N kukan] old. kākom [RP Rkwm | N ~] stoat. ~ i spéd: ermine. kālbod [Аро | (M k*/byd), N ~] body, shape, form. ~ӧтапа [-wmnd] corporeal. kam [km | M kmb, N ~] little, small, few; v. kem. kam [Em | = M, N ~j will, desire, purpose. kàm-, v. kāmistan. 1катаб [k?mk! | N kama] kinds of gruel, or soup. ?kümag [k?*mk! | N kama] = kam. «-hanjām [-hnc’m] gaining one’s end, successful. -~-hanjamih: success. „ūmand [-wmnd] willing(ly), desirous. ~-widar [-wt?l | N kām-gučār] successful, independent. ~-xwaday [-Awt^y] independent, absolute. kamal [kml | (M km?7)] head (daevic). ~ig [-yR!] chief (daevic).
PHD.txt:437:ma [AL < À °l | M m, N ~] not (prohibitive). ~ agar [N magar] perhaps; lest. mad [AM < A ?m-y, v. madar | M md] mother.
PHD.txt:493:Р murd [то | P mort !] death. murdan, mir- (YMYTWN-tn! < A ymwtwn, V mwt; mulin' | M murd, myr-, N ~] die. murdār [mwrt?], mwld?l | N ~] carrion. murnjénidan, murnjén- (mwlncyn-ytn'] destroy. murw [mwlw! | M mwrw, (N mury)] bird. murwāģ [mwlw’k' | M mwrw’, N murwd] omen. murwizag [mwlwyck'] little bird. murw-nīš [mwlwnys] augur, soothsayer. must [mwst'] force, violence. ž*must [mwst'] = must. *must [mwst'] complaint. must|-abarmānd [mwst!’plm’nd] aggressive, aggressor. ~gar [-kl] violent, rebellious, mustómand [mwst?wmnd | N mustmand] complaining, unhappy. ImuSk [отео | N ~] musk. 2mušk [mwsk! | (N mis)] mouse, rat. must [mzvšt! | N ~] fist. muštan, māl- [mwéstn', wl- | N ~] rub, sweep.
PHD.txt:547:~th: visibility, appearance. paydagénidan, paydagén- [ ГОР hinin | M pyd'gynyd] reveal, explain. paydagihistan, paydagih- [py kyh-stn'] appear, be revealed, payg [pdh! | (P рар), N ~] foot-soldier, courier. *paygal [pyg'l | N payyāla, piyála] cup, goblet. -- gar [-A/] cup-maker. payģām [pgt”m! | M pyg’m, N pay(y)ām] message. ~bar LA | N -bar] messenger, apostle. paygos [p?tktvs | M p’ygws] district, province. paymān [pim”n! | M pym?n, N ~] measure, period; moderation; treaty. 6 — madan: reach maturity. ~ag [-k! | N ~a] period, measure, proportion. paymānīģ [ptm”nyk!] moderate. ~ih: moderation. *paymar [PK DWN < А pqdwn; p'tym'l] appointment, assignment. paymāy-, v. paymüdan. paymēģ [ptmwg | M pymwg] clothes, garment. paymóxtan, paymēz- [ptmwhtn!, ptmwe- | M pymwxt, bymwc-] don, wear. paymēūzan [ptmwen' | M pymwen] garment, dress. paymüdan, paymāy- [ptmwtn', ptm’d- | N ~] measure. *payram [p’tlm] the commonalty,-people. payrāstan, payrāy- [pt-, pyPstn!, pyPd- | M ругі, pyr!y-, N pērāstan) arrange, adorn. payrayag [руРак! | M pyr)yg, N pērāya] ornament, adornment. payrēģ [ptlwk'] light, brightness. paywand [ptwnd | (M руп), N ~] connection; offspring. paywand-, v. paywastan. paywasag [ptw’sk'] leather bag, wallet. paywastag [pteostk! | N ~a] continually. paywastan, paywand- [ptwstn!, ptwnd- М pywst, (pywyn-), N ~] join, connect. paywāz- [ptw’c- | M pyw’z-] answer, reply. ~ag [-k!], —i$n: response. paz-, v. poxtan. pāzand [p’cnd | N —] the Pahlavi commentaries on the scriptures (zand), transcribed in Avestan letters. pazd [pzd | — P] oppression, persecution. pazd- [pzd- | = M] blow, play (flute). pazdaģīh [pzdkyh] expulsion. pazdénidan, pazdén- [pzdyn-ytn' | P pzd-] frighten, chase. pāzen [p’c(y)n' | М pen, N pazan] ibex. pazüg [pzwk! | (N payūk, xabazdū)] guinea-worm. ~ í gühgard / gGhward: dung worm. pazzāftan [p> tn ' (M pzpt „intr.)] (cause to) ripen.
PHD.txt:549:pazzām- [pz^m-] mature, ripen (intr.). ~išn: maturation, ripening. pazzáménidan [pz’myn-ytn'] = pazzāftan. pēčīdan, pēč- [pyc-ytn' | N ~] twist, entwine. pēm [pym] milk. péménidan, pémén- [5ymyn-ytn'] cause to well up, swell up. pen [p(y)n'] mean, miserly, niggardly. ~ih: meanness. pérámoón [pyPmwn! | M pyrmwn, N ~miin] around, péróz [pylwe | M pyrwz, N ~] victorious. ~th: victory. pérózgar [pylwekl | N ~] victorious. ~ih : victory. pés [pys | N ~] mottled, leprous; leper. pēsīdan, pēs- [pys-yin'] colour, adorn. ~iSn: adornment. pestān [pyst?n' | N ~] breast. pēš [LOYN! < A I-‘yn; руї | = M, N ~] before. IpéSag [py$k! | N péfa] trade, craft; guild, caste. *pēšaģ [pysk'] limb, member, part. pëššánig [pyš”nyk! | N pēšānī] forehead. pēšār [py | M py?r] leader, guide. ~ büdan: be guilty (of), commit. pēšārwār [руло], v. pëšyàr] urination. péSémàl [руѓут?/, v. hamēmāl] plaintiff. ~ih: prosecution, pēšēnīg [pysynyk! | (M pysyn(g), N pésina)] former; foremost, noble. pëš-gāh [pyšg”5 | N ~) audience chamber; foremost seat. pēš-kār [py$k'/ | N ~] servant. pēšēbāy [byš')wp?d | M руйору, N péfwa] leader, vanguard. ~th: leadership. pēš-pāraģ [pyšp*/k! | N —a] an appetizer. pēšyār [pyšk”/ | N ~] urine. petit [pytyt! = Av. paitita-] penance. ~ig [-yk'] penitent. ~igih: penitence. petyárag [p(y)tyd'lk! = Av. paityára- | M pty’r, N patydra] evil, mis- fortune; adversary; astr. detriment, ~th: (onslaught of) evil. рі [AB' < А "bur р(у) | M pyd] father. *pid [5(5)!! | P pyd] meat, flesh. pidar [AB Ytl, v. ipid ; ру | M pydr, N ~] father. pih [pyhw'] food, victuals. pīh [TL BA = A trb; рур | N ~] fat, tallow. pil [py] | M pyl, N ~] elephant; (chess) bishop. --bān [-p’n' | N ~] elephant-driver.
PHD.txt:559:rēšaģ [/yšk! | N rēša] root, fibre. rēšīdan, rēš- [lysyin' | N ~] wound, hurt. rëškën [/yškn'] hurtful, harmful. ~th: harmfulness. réxtan, réz- [lyhtn', lyc- | P ryxt, M ryz-, N ~] flow, pour. --išn: flow. ridan, riy- [/ytn', Id- | N ~] defecate, void. rist [lyst' | M ryst] dead. Iristag [lystk'] corpse. 'ristag [/ystk!] way, manner; sect. rist-āxēz [/yst?hyc | M ryst?hyz, N ~] resurrection of the dead, rištaģ [/(y)stk! | N ~a] rope, string, thread. riy-, v. ridan. riyahrih [/d?hlyh] scorn, mockery. rdb [/wp] robbery. rób- [/wp- | N ruftan, ~} rub, sweep. rūbāh [TALE < A tP; lwph | N ~] fox. Irēd [Iowt! | M rwd, N ~] river. *rdd [lwt' | N ~] stringed instrument. réd-bar [lwtb’] | N ~] river bank. rddig [/zvtyk! | (N róda)] intestine, gut; ~4n, (p/.) entrails, guts. тбүп [M(H)SY A < A ті; lwkn! | Р тшеп, (M rwyyn), N rauyan] oil, butter. ~-xwardig [-hwltyk'] sweetmeats. ron [lwn' | M rwn] direction. б... ~: towards. róspig [lwspyk! | N ~i] whore. ~th: whoredom. róstág [lw(t)st?k! | (P rwdyst?g), N rūstā] river-bed; district, province. rošn [lwfn! | M rwšn, N rūšan] light; bright, light. ~ih: light. röšnjag [lwsnk'] clear, obvious. ~gar [-Al | (P gr, M -ygr), N -gar] illuminator. irēy [ltd | M rwy, N ~] face. *rdy [lwd | M rwy, N ~] copper, brass. гбу-, -išn, v. rustan. гӧуап [/wdyn! | N ~] madder. róyen [/wdyn! | M r'wyn, N róyin] (made of) copper, brazen. roz [YWM < А ушт; Гос | M rwc[z, N ~) day. rózag [lwck! | M rweg, N roza] fast, fasting. rozāģ [wc k'] lightning. rózan [/wcn! | N ~] window. roz(b)ānaģ [lwe(p)’nk'] window. rózénidan, rózén- [Iwcyn-ytn! | M rweyn-] lighten, brighten. rozģār [/wck”l | N ~] daytime. r6zig [/wcyk! | N rózi] daily bread, sustenance.
PHD.txt:597:tru(f)Š [t/wu(p)$ | (P tryff), N turf] sour. truftag [t/wptk'] stolen; intercalary (days). tuhig [twhyk! | M twhyg, ЇЧ tuhi] empty, vain. ~ih : emptiness, void. tumbag [twmbk' | N ~a] drum. tund [twnd | N ~] sharp, violent. ~ih: violence, vehemence. Tür [twl | N ~] one of a people inimical to Eran, Turanian. ~ап [—n! | N ~] (land of) the Turanians. Turk [twlk' | N ~] Turk. tu&t [twst'] silent. tuwān [twb!n! | M twn, N ~] might, power. ~ (+infinitive): it is possible to, one can. ~ag [~k' | N —a] mighty, able. «gar [-kl | N ~] rich. ~garih: richness, wealth. ~ig [-yk'] able. ~igih: ability, power. --sāmān [-s’m’n'] the extent of one’s ability. tuxšáé [twhPk! | M рох р, N tuxsa] diligent. “Аһ: diligence, endeavour. tuxšīdan, tux&- [гол у! | (M. twxf‘yst), N ~] strive, endeavour. ~išn: endeavour, striving.
PHD.txt:614:warzigar [wlcykl | M zorzygr, N barzigar] worker, peasant.
=== NYB ===
1626:gar [gl] mountain, pl. cas. obl. ~-dn 20°. — Av. (513 sq.) gart-.
1629:garämikihä in esteem, in a respectful |
1632:garän [gl'n'] heavy, hard, grave, comp, tar, 125. 14! etc. passim. — Derived from OIr *garu-, Av. (524) gouru- in compounds, Skr guru-; MPrthPrs gr’n; Paz. garg, gira; NP girän.
```


## [2026-09-06T14:59:36.639Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== HUB zaxm ===\"; grep -n 'zaxm\\|zahm\\|za\\^m' HUB.txt | cut -c1-300 | head; echo \"=== CHEUNG jah/jan/zax ===\"; grep -n 'zaxm' CHEUNG.txt | cut -c1-300 | head; echo \"=== CHEUNG gzar ===\"; grep -n 'γžar\\|gzar\\|jzar\\|Hzar' CHEUNG.txt | cut -c1-250 | head"
}
```


### [2026-09-06T14:59:36.720Z] TOOL RESULT

```
=== HUB zaxm ===
=== CHEUNG jah/jan/zax ===
=== CHEUNG gzar ===
8798:*gZar ? (*gzar ?) 123 
8834:metathesized variant *yzar- (> Av. yZar-, s.v. *gzar). A different outcome would be 
8841:*gZar ? (*gzar ?) ‘to flow (fast ?)’
```


## [2026-09-06T14:59:38.689Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '8820,8900p' CHEUNG.txt"
}
```


### [2026-09-06T14:59:38.744Z] TOOL RESULT

```
WIM П/2: 667; Asatrian — Livshits: 85; Werba 1997: 285; Paul 1998: 298b; Cabolov 2001: 385 Ё; Lecoq 
2002: 576b, 594a, 608a (passim); Shahbakhsh: s.v. granc- 


*gzra(H)d ? ‘to flow’ 

*AVESTAN: (+ *4-) YAv. ayzraó- ‘to flow to’ || (+ *ui-) YAv. viyzräö- ‘to flow away’ 
c» Liste: 21 

Caus.: pres. IND. 3sg. YAv. ayzraóaieiti (Yt 8.31), YAv. viyzradaiieiti (Yt 8.31) 

© The etymology of ҮАУ. -yzräö- is uncertain. Gershevitch (apud Panaino, Tist.: I, 
118) hypothesized that the curious initial consonant cluster -yzr- (with surprising 
dental -z-) is the result of contamination of the verb *zyar- (i.e. *zgar! ?) and its 
metathesized variant *yzar- (> Av. yZar-, s.v. *gzar). A different outcome would be 
*Zyar- > Sogd. /Zyar-/, s.v. *zgar'. 

«PIE — 0 A secondary fientive formation *g”g"r-eH,-d’e- is postulated by Lippe, LIV, 
ibid.: morphologically hardly acceptable. > LIV: 213 f., esp. n. 9 | Pok.: 487 f. 


*gZar ? (*gzar ?) ‘to flow (fast ?)’ 

*AVESTAN: YAv. yZar- ‘to flow’ || (+ *4-) ‘to let flow to’ || (+ *ui-) ‘to let overflow, 
flood’ = Liste: 21 

Pres. them.: SUBJ. 3pl. ? YAv. "yZaran (Panaino, Tist.: 131; Yt 8.42); Partic.: pres. caus. ҮАУ. 
yZaraiiant- (Yt 15.2), YAv. viyZäraiiant- (Yt 5.139, Yt 12.5, V 19.40), intens. YAv. yZaro.yZarant- (V 
5.19); Caus.: pres. IND. 35р. YAv. äyZäraileiti (Yt 8.31), YAv. viyZäraileiti (Yt 8.31), SUBJ. 3pl. ? YAv. 
*yZaraiian 

*CHORESMIAN: (+ *abi-) m/BZry- ‘to flood’ = Samadi: 48 

*NWIR: ? NP saridan/sar- ‘to flow as rivers, with a great noise; to pour, trickle, urine’ 
*NEIR: Oss. I. æğzælyn (yzgalyn)/zg&ld, D. egz&lun/zgzald ‘to pour down, drip’, 
? Pash. zyastal/zyal- ‘to swim, fly away’, (caus.) Oss. I. egzalyn (yzgalyn)/&g&ld, 


124 *hac 


D. egzalun/egzald "to pour down, drop’, ? Wa. Zarz ‘milk’ || (+ *fra-) Oss. legzer, 
læzğær ‘scree’ 

*MISC: ? Orm. Sar-ék ‘to turn, revolve’ 

*SANSKRIT: ksar ‘to flow" = EWAia I: 428 

“PIE *d^ iber. "о flow away’ ?. Ò The reconstruction is *g" g'er- according to Lipp, 
LIV, l.c., n. 1. Note also Mayrhofer, CLI: 9 f., who considers the derivation of the 
Ilr. forms from *d’g””er-, Gr. фӨғіро, not fully certain, because of semantic 
difficulties. But see now Puhvel 2005: 232 ff. — LIV: 213 | Pok.: 487 f. 

*IE COGNATES: Gr. фӨғіро ‘I destroy’, фӨғіророл (med.) ‘I perish; to be 
shipwrecked’, ? Toch. kwär- ‘to age, grow old’. Ф On Toch. kwär- see Hilmarsson 
1986: 254 ff. The connection is declined by Adams 1999: 236. 


*REFERENCES: EVP: 101; IIFL I: 409b; IIFL II: 557b; Abaev, Slovar’ I: 536 f.; Abaev, Slovar’ II: 26 f.; 
Werba 1997: 343; Steblin-Kamenskij 1999: 445; Jamison, Fs Rix: 237 ff. 


h 


*haé ‘to follow’ 

*AVESTAN: hac- ‘to follow’ || (+ *ä-) ‘to stick to’ || (+ *upa-) ‘to accompany, join’ || 
(+ *para-) ‘to follow forth’ = Liste: 70f. 

Pres. {1} them.: IND. 2sg. YAv. hacahi, 3sg. YAv. haxaiti (Yt 19.68, ViD 9), med. 3sg. hacaité (Y 34.2, 
Y 46.16, Y 48.4, etc.), 3р1. OAv. hac(a)inte (Y 33.9, Y 45.2), YAv. hacinte (Y 10.8, Y 19.15, Yt 17.5), 
INJ. 3sg. YAv. upanhacat (Yt 15.4, Yt 19.26, Yt 19.28, etc.), SUBJ. 1sg. OAv. hàca (Y 46.1), med. 15р. 
Y Av. hacane (Yt 5.69, Yt 14.60), 3sg. YAv. paranhacaiti (N 6 £, N 9, N 11), YAv. hacat (Yt 18.4, Yt 
19.54), 3р1. med. YAv. hacanté (Y 48.12, Yt 8.1), IMPV. med. 2sg. YAv. hacag'ha (N 9), 3sg. ҮАУ. 
hacatu (Vyt 8); Pres. {2} athem. red.: IND. 3sg. YAv. a.hishaxti (V 5.34), SUBJ. med. Ipl. OAv. 
hiscamaide (Y 40.4); Aor. {1} them. red.: IND. 2pl. ? YAv. haxsa0a (Vyt 47), INJ. 35р. ? YAv. haxsat (F 
24), SUBJ. med. 1sg. OAv. haxsai (Y 46.10), med. 1sg. ? YAv. haxsane (V 19.26), OPT. 1sg. YAv. 
haxsaiia (Y 8.7, Y 11.14, Y 52.7), med. Zeg ? Y Av. haxsaesa (V 7.50, V 19.26), 3sg. YAv. haxsoit (Y 
62.10, V 18.27, Vyt 38); Aor. {2} athem.: IMPV. 3pl. OAv. scantü (Y 53.2); Partic.: pres. {1} med. 
hacimna- (Y 43.10, Y 43.12, etc.), OAv. һасәтпа- (Y 44.10), perf. pass. YAv. -haxta- (N 6); Caus.:
```


## [2026-09-06T14:59:48.519Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n 'zaxya\\|za;fya\\|zaxti\\|zaxya-' BRT.txt | cut -c1-400 | head; echo \"=== jas ===\"; grep -n 'jasaite\\|jasat\\|jah-\\|zah-' BRT.txt | cut -c1-200 | head -5"
}
```


### [2026-09-06T14:59:48.589Z] TOOL RESULT

```
=== jas ===
2467:hunlUa  . .  hl  a/imsi  asis  »rynavi  tat  aAmJi jasat  Syapttm  Y.9.4;  3',  (72. 10,  V.2.2', Yl,Jy.i4,  14.2,3;  — yS  .  .  yavat  ahmli yavanam  .  .  aStavai  V.  6*. 85;  Y.  J9, 12, 
2729:Sing,  in  kollekt.  Sinn');  'ma  frasaocayähi\     Lavaquellen  enthaltend".    VgL   Bthl.IF.j. V.  *.  7  5 ;  /4-  7 ;  —  a  -man  y'äsamiha  V.  i8.       ■  24-  -  •>  NS.,  S  ^
2902:•  j.,  g.  "aojah-  Adj.  'stark,  kräftig':  mi- "inm  . .  "JaaAfin  laxmim  ra'ialäqm  Yt.
2906:ai.  djasvant-  Adj.  —  Pfl.:  Siämand.  —  i)  VgL asi.asjah-.  —  »)  So  Fl,  Mfl,  vgl.  PI4,  NA. 'jaakvanitm.
3402:aiUyajah-  66
```


## [2026-09-06T14:59:54.380Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n 'zaxy\\|za;ry\\|zaAy\\|zaJy\\|zafy' BRT.txt | cut -c1-300 | head; echo \"=== search 1682-1700 z section for 'Wunde' ===\"; grep -n 'zafar\\|zaeni\\|zaenu' BRT.txt | cut -c1-150 | head -3"
}
```


### [2026-09-06T14:59:54.468Z] TOOL RESULT

```
9778:.  .  mainyaom  .  .  *'ihim  yazafym  Y.  25.  8,  •  j.  gao-ciOra-  Adj.  'den  Ursprung  des 16.1  f.; —  vispaSca  ,  ,  mamyai^a^a  yasa/a'  Rindes  bildend,  woraus  das  Rind  ent* ''hya^a  yasamaide  Y.ji.%;  */^.9*',  Fr  W. .  Sprüngen  ist',  vomMond":  niära/um 'nm j.  I  ('i
=== search 1682-1700 z section for 'Wunde' ===
7904:)a  ahüm\aSäunS  '^.4-j.i,;  —  nynnSl  da^ayäzö vanhSuS  °oa  zafar?  *aoi^3urDayqn  °%a  rün^antS  Yt. J7.6;  —  jaginbuitarS  anhat
9332:•  j.    'karana-  m.    Ohr',   uzw.  rfnÄ^ischer       haben;  vgl.  Yt.  ,0.  125.-»)  Anders  freilich Wesen":    lai  drvalö   drvatyii
13989:•  j.  ^dvariSra-''  n.  'Fuss,  Bein'  uzw. daSvischex  Wesen;  tat  drvats  .  .  an  usi karftia  gava  °ra'^^^  zafar»  .  .  pairi.- un
```


## [2026-09-06T15:00:00.283Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n '1,40p' tools/fetch_source.py"
}
```


### [2026-09-06T15:00:00.322Z] TOOL RESULT

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


## [2026-09-06T15:00:06.664Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; for u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/g%CA%B7erH-\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Slavic/x%D1%8Arvat%D1%8A\" \\\n \"https://www.etymonline.com/word/cravat\" \\\n \"https://en.wiktionary.org/wiki/asbestos\" \\\n \"https://en.wiktionary.org/wiki/%D8%B2%D8%AE%D9%85\" \\\n \"https://en.wiktionary.org/wiki/%D8%A2%D8%A8%D8%B4%D8%A7%D8%B1\" ; do\n echo \"### $u\"; timeout 90 python3 tools/fetch_source.py \"$u\" --note \"page 211 verification (Gwer 4 mountain / Gwes extinguish / Gwhder flow)\" 2>&1 | tail -3; done"
}
```


### [2026-09-06T15:00:12.748Z] TOOL RESULT

```
### https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/g%CA%B7erH-
/home/sfmqrb/git/rishe/data/verification/sources/web/934d5ae63b36c5f3.txt
### https://en.wiktionary.org/wiki/Reconstruction:Proto-Slavic/x%D1%8Arvat%D1%8A
/home/sfmqrb/git/rishe/data/verification/sources/web/828a4b112eeafb3e.txt
### https://www.etymonline.com/word/cravat
/home/sfmqrb/git/rishe/data/verification/sources/web/84d30f381bbfa6e8.txt
### https://en.wiktionary.org/wiki/asbestos
/home/sfmqrb/git/rishe/data/verification/sources/web/12c50f96de5e665a.txt
### https://en.wiktionary.org/wiki/%D8%B2%D8%AE%D9%85
/home/sfmqrb/git/rishe/data/verification/sources/web/59db6ae92f918e5c.txt
### https://en.wiktionary.org/wiki/%D8%A2%D8%A8%D8%B4%D8%A7%D8%B1
/home/sfmqrb/git/rishe/data/verification/sources/web/227ecb3b9ef07861.txt
```


## [2026-09-06T15:00:15.669Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; echo \"=== gwerH ===\"; grep -n -i -A4 'Etymology' 934d5ae63b36c5f3.txt | head -40; echo; echo \"=== head ===\"; head -60 934d5ae63b36c5f3.txt"
}
```


### [2026-09-06T15:00:15.722Z] TOOL RESULT

```
=== gwerH ===

=== head ===
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/g%CA%B7erH-
FETCHED: 2026-09-06T14:59:55Z
STATUS: 200
TITLE: Reconstruction:Proto-Indo-European/gʷerH- - Wiktionary, the free dictionary

Reconstruction:Proto-Indo-European/gʷerH- - Wiktionary, the free dictionary 

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
```


## [2026-09-06T15:00:18.218Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; sed -n '/Proto-Indo-European\\[edit\\]/,$p' 934d5ae63b36c5f3.txt | head -80"
}
```


### [2026-09-06T15:00:19.696Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T15:00:22.086Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; awk 'NR>120 && NR<330' 934d5ae63b36c5f3.txt | grep -v '^\\s*$' | head -70"
}
```


### [2026-09-06T15:00:23.514Z] TOOL RESULT

```
 Appearance
 move to sidebar 
 hide 
 From Wiktionary, the free dictionary
 See also: Reconstruction:Proto-Indo-European/gʷerh₃- and Reconstruction:Proto-Indo-European/gʷerh₂- 
 This Proto-Indo-European entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.
 Proto-Indo-European
 [ edit ] 
 Root
 [ edit ] 
 *gʷerH- [ 1 ] 
 to express approval ; praise 
 to elevate 
 Derived terms
 [ edit ] 
 Terms derived from the Proto-Indo-European root *gʷerH- (63 c, 0 e) 
 *gʷérH-e-ti ( thematic root present ) [ 1 ] 
 Proto-Indo-Iranian: *ǰáratay 
 Proto-Indo-Aryan: *ȷ́áratay 
 Sanskrit: जरते ( járate ) 
 Proto-Iranian: *ǰáratay 
 Persian: پراچی جر ( parâči jar- ) 
 *gʷr̥-né-H-ti ~ *gʷr̥-n-H-én-ti ( nasal-infix present ) [ 1 ] [ 2 ] 
 Proto-Celtic: *barnati ( see there for further descendants )
 Proto-Indo-Iranian: *gr̥náHti 
 Proto-Indo-Aryan: *gr̥náHti 
 Sanskrit: गृणाति ( gṛṇā́ti ) 
 Proto-Iranian: *gr̥náHti 
 Younger Avestan: 𐬀𐬎𐬎𐬌 𐬔𐬆𐬭𐬆𐬧𐬙𐬈 ( auui gərəṇte ) 
 *gʷer-s- 
 Proto-Albanian: *griś 
 Albanian: grish 
 *gʷr̥H-yé-ti ( zero-grade ye-present ) [ 1 ] [ 3 ] [ 4 ] [ 5 ] [ 6 ] 
 Proto-Balto-Slavic: *girˀtei 
 Latvian: dzir̃u 
 Lithuanian: gi̇̀rti 
 Old Prussian: girtwei 
 Proto-Slavic: *žьrti , *žerti ; *žьrtva ; *žьrьcь ( see there for further descendants )
 *gʷr̥Hdʰh₁-é-ti 
 Armenian:
 Old Armenian: կարդամ ( kardam ) 
 *gʷr̥Hdʰh₁-éye-ti 
 Proto-Indo-Iranian: *gr̥HdʰHáyati 
 Proto-Indo-Aryan: *gr̥HdʰHáyati 
 Sanskrit: गूर्धया ( gūrdhayā , “ to praise ” , 2sg.impv. ) 
 *gʷr̥dʰh₁-ó-s [ 7 ] 
 Proto-Celtic: *bardos ( “ poet, bard ” ) ( see there for further descendants )
 *gʷr̥H-sḱé-ti ( zero-grade sḱe-inchoative ) [ 8 ] 
 Proto-Albanian: *grah 
 Albanian: grah 
 ( perhaps ) *gʷerH-os [ 9 ] 
 Balto-Slavic:
 Lithuanian: gẽras 
 *gʷérH-tis ~ *gʷr̥H-téy- 
 Proto-Indo-Iranian: *gr̥Htíš 
 Proto-Indo-Aryan: *gr̥Htíṣ 
 Sanskrit: गूर्ति ( gūrtí ) 
 > ? Proto-Italic: *gʷrāt(i)s ( see there for further descendants )
 *gʷérH-tus ~ *gʷr̥H-téw- [ 10 ] [ 11 ] 
 Proto-Celtic: *brātus ( see there for further descendants )
 Proto-Italic: *grātu- 
 Latin: grātuītus 
 *gʷr̥H-í-s [ 12 ] 
 Proto-Indo-Iranian: *gr̥Híš 
 Proto-Indo-Aryan: *gr̥Híṣ 
 Sanskrit: गिरि ( girí ) [ 13 ] 
 Proto-Iranian: *gr̥Híš ( see there for further descendants )
 *gʷorH-eh₂ 
 Proto-Balto-Slavic: *garā́ˀ ( see there for further descendants )
 Ancient Greek: Βορέᾱς ( Boréās , “ north ” )
```


## [2026-09-06T15:00:30.637Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; echo \"=== xъrvatъ ===\"; awk 'NR>120 && NR<400' 828a4b112eeafb3e.txt | grep -v '^\\s*$' | head -60"
}
```


### [2026-09-06T15:00:32.917Z] TOOL RESULT

```
=== xъrvatъ ===
 Print/export
 Download as PDF 
 Printable version 
 In other projects
 Appearance
 move to sidebar 
 hide 
 From Wiktionary, the free dictionary
 This Proto-Slavic entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.
 Proto-Slavic
 [ edit ] 
 Etymology
 [ edit ] 
 Uncertain:
 Common theories from the 20th century derive it from an Iranian origin, the root word being a third-century Scytho-Sarmatian form allegedly attested in the Tanais Tablets as Χορούαθος ( Khoroúathos ) , Χοροάθος ( Khoroáthos ) and Χορόαθος ( Khoróathos ) , probably the name of the ruler of a city in that region, near the mouth of the river Don; [ 1 ] this has also been corroborated with names on ancient gravestones in Tanais , which gives some credence to the interpretation as a clan name. [ 2 ] A similar name for a tribe of the north Caucasus occurs in the tenth-century De Ceremoniis as Krevatās , Krevatades . [ 3 ] 
 On the other hand, modern scholars such as Matasović tend to dismiss these as coincidences with respect to the Croatian ethnonym, [ 4 ] and consider the identification of the relevant Scytho-Caucasian tribes with Slavs implausible on historical and geographic grounds; nonetheless, an ultimate Iranian origin is regarded as plausible.
 See Etymology of Croatia on Wikipedia for a detailed discussion of the various hypotheses.
 Noun
 [ edit ] 
 *xъrvatъ   m [ 5 ] 
 ( Common Slavic ) Croat 
 Declension
 [ edit ] 
 Possibly accent paradigm a?
 Declension of *xъrvatъ (hard o-stem)
 singular
 dual
 plural
 nominative 
 *xъrvatъ 
 *xъrvata 
 *xъrvati 
 genitive 
 *xъrvata 
 *xъrvatu 
 *xъrvatъ 
 dative 
 *xъrvatu 
 *xъrvatoma 
 *xъrvatomъ 
 accusative 
 *xъrvatъ 
 *xъrvata 
 *xъrvaty 
 instrumental 
 *xъrvatъmь , *xъrvatomь * 
 *xъrvatoma 
 *xъrvaty 
 locative 
 *xъrvatě 
 *xъrvatu 
 *xъrvatěxъ 
 vocative 
 *xъrvate 
 *xъrvata 
 *xъrvati 
 * -ъmь in North Slavic, -omь in South Slavic.
 Descendants
 [ edit ] 
 East Slavic:
```


## [2026-09-06T15:00:39.784Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; grep -n -i -m3 -A12 'cravat (n' 84d30f381bbfa6e8.txt | head -30; echo \"=== asbestos ===\"; grep -n -i -B2 -A14 'From Ancient Greek\\|Etymology' 12c50f96de5e665a.txt | sed -n '1,60p'"
}
```


### [2026-09-06T15:00:39.851Z] TOOL RESULT

```
23: cravat (n.) 
24-
25- "type of neck-cloth worn usually by men," 1650s, from French cravate (17c.), from Cravate, literally "Croatian," from German Krabate , from Serbo-Croatian Hrvat "a Croat" (see Croat ). Cravats came into fashion 1650s in imitation of linen scarves worn by the Croats or Crabats , 17th-century light cavalry forces who fought on the side of the Catholic League in the Thirty Years' War. The name in this context was not an ethnic label as much as a generic designation for light cavalry from the Hapsburg Military Frontier, which included Croats, Hungarians, Serbs, Wallachians, Poles, Cossacks and Tatars.
26-
27- When first introduced, it was commonly of lace, or of linen edged with lace. ... The modern cravat is rather a necktie, passed once round the neck, and tied in front in a bow, or, as about 1840 and earlier (when the cravat consisted of a triangular silk kerchief, usually black), twice round the neck, in imitation of the stock. Formerly, when starched linen cravats were worn, perfection in the art of tying them was one of the great accomplishments of a dandy. The cravat differs properly from the scarf, which, whether tied, or passed through a ring, or held by a pin, hangs down over the shirt front. [Century Dictionary, 1897]
28- also from 1650s 
29-
30- Entries linking to cravat 
31-
32- Croat (n.) 
33-
34- "native or inhabitant of Croatia," 1702, from Serbo-Croatian Hrvat "a Croat," from Old Church Slavonic Churvatinu "Croat," literally "mountaineer, highlander," from churva "mountain" (compare Russian khrebet "mountain chain"). Croatian is attested from 1550s as a noun, "a Croat;" 1837 as an adjective; by 1855 as "the Slavic language of the Croats."
35-
=== asbestos ===
63-
64- 1.2 
65: Etymology 
66-
67- 1.3 
68- Pronunciation 
69-
70- 1.4 
71- Noun 
72-
73- 1.4.1 
74- Hyponyms 
75-
76- 1.4.2 
77- Coordinate terms 
78-
79- 1.4.3 
--
98-
99- 2.1 
100: Etymology 
101-
102- 2.2 
103- Pronunciation 
104-
105- 2.3 
106- Noun 
107-
108- 2.3.1 
109- Declension 
110-
111- 2.3.2 
112- Descendants 
113-
114- 2.4 
--
257- asbestus ( archaic ) 
258-
259: Etymology
260- [ edit ] 
261-
262: Etymology tree
263-
264- Proto-Indo-European *né 
265- Proto-Indo-European *n̥- 
266- Proto-Hellenic *ə- 
267- Ancient Greek ἀ- ( a- ) 
268-
269- Proto-Indo-European *(s)gʷes- der. ? 
270- Ancient Greek σβέννῡμι ( sbénnūmi ) 
271-
272- Proto-Indo-European *-tós 
273- Proto-Hellenic *-tós 
274- Ancient Greek -τός ( -tós ) 
275-
276- Ancient Greek σβεστός ( sbestós ) 
--
280- English asbestos 
281-
282: Learned borrowing from Classical Latin asbestos , [ 1 ] borrowed from Ancient Greek ἄσβεστος ( ásbestos ) , from ἀ- ( a- ) + σβεστός ( sbestós ) . Compare Middle English asbestus and Old French abestos .
```


## [2026-09-06T15:00:46.295Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; awk 'NR>150' 59db6ae92f918e5c.txt | grep -v '^\\s*$' | sed -n '1,70p'"
}
```


### [2026-09-06T15:00:47.871Z] TOOL RESULT

```
 Print/export
 Create a book 
 Download as PDF 
 Printable version 
 In other projects
 Appearance
 move to sidebar 
 hide 
 From Wiktionary, the free dictionary
 See also: رحم and زحم 
 Persian
 [ edit ] 
 Etymology
 [ edit ] 
 From Middle Persian [script needed] ( z’hm /⁠zaxm⁠/ ) .
 Pronunciation
 [ edit ] 
 ( Classical Persian ) IPA ( key ) : /ˈzaxm/ 
 ( Dari, formal ) IPA ( key ) : [zäxm] 
 ( Dari, formal ) IPA ( key ) : [zäxm] 
 ( Kabuli ) IPA ( key ) : [zäxm] 
 ( Hazaragi ) IPA ( key ) : [zäxm] 
 ( Iran, formal ) IPA ( key ) : [zæxm] 
 ( Tajik, formal ) IPA ( key ) : [zäχm] 
 Rhymes: -axm 
 Readings
 Classical reading ? 
 zaxm
 Dari reading ? 
 zaxm
 Iranian reading ? 
 zaxm
 Tajik reading ? 
 zaxm
 Noun
 [ edit ] 
 زخم • ( zaxm ) ( Tajik spelling захм ) 
 wound 
 Related terms
 [ edit ] 
 زخمی ( zaxmi ) 
 زخمی شدن ( zaxmi šodan ) 
 Descendants
 [ edit ] 
 → Azerbaijani: zəxm 
 → Bengali: জখম ( jokhom ) 
 → Gujarati: જખમ ( jakham ) 
 → Hindustani: 
 Hindi: ज़ख़्म ( zaxma ) , ज़ख़म ( zaxam ) , जख्म ( jakhma ) , जखम ( jakham ) , ज़ख्म ( zakhma ) , ज़खम ( zakham ) , जख़्म ( jaxma ) , जख़म ( jaxam ) — nuqtaless 
 Urdu: زَخْم ( zaxm ) 
 → Marathi: जखम ( j̈akham ) 
 → Middle Armenian: զախմ ( zaxm ) 
 → Punjabi: 
 Gurmukhi script: ਜ਼ਖ਼ਮ ( zaxam ) , ਜਖਮ ( jakham ) , ਜ਼ਖਮ ( zakham ) , ਜਖ਼ਮ ( jaxam ) — nuqtaless 
 Shahmukhi script: زَخْم ( zaxm ) 
 → Tulu: ಜಖಮ್ ( jakhamŭ ) 
 Urdu
 [ edit ] 
 Etymology
 [ edit ] 
 Borrowed from Classical Persian زَخْم ( zaxm ) .
 Pronunciation
 [ edit ] 
 ( Standard Urdu ) IPA ( key ) : /zəxm/ 
 Noun
 [ edit ] 
 زَخْم • ( zaxm )  m ( Hindi spelling ज़ख़्म ) 
 wound (usually a gash, stab, tear)
 Related terms
 [ edit ]
```


## [2026-09-06T15:00:54.994Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -o 'zaxm[^ ]*[^|]\\{0,80\\}' PHD.txt NYB_vol2_glossary.txt | head; echo \"=== zad/zan ===\"; grep -o 'zaxm\\|z?hm' PHD.txt | head; echo \"=== FSF ===\"; grep -n -A3 'زخم' FSF_pages.txt | head -20"
}
```


### [2026-09-06T15:00:58.046Z] TOOL RESULT

```
PHD.txt:zaxm [ztm, z?hm 
PHD.txt:zaxm.
PHD.txt:zaxm
PHD.txt:zaxm «xS zahübag WS zay _ ys zatrī pud wi? zarrënt L My ya S zdy- — S zahīh 948 zay
=== zad/zan ===
zaxm
z?hm
zaxm
zaxm
zaxm
=== FSF ===
1126:               ‫خروش آمد و بانگ زخم تبر‬                 ‫از آن پس بیاسود لشکر دو روز‬
1127- ‫سراسیمه شد گیو پرخاشخر‬                         ‫سدیگر چو بفروخت گیتی‌فروز‬
1128-‫(‪)۴-۲۸-۲۶۱۱‬‬                                     ‫(‪)۲-۲۲-۲۵۲‬‬
1129-                       ‫آشام (اسم از آشامیدن)‬           ‫مگر شاه ایران ازین ‪:‬خشم و کین‬
--
2597:‫رسیدست رستم بهمن اندبار‬                                            ‫به انبوه زخمی بباید زدن‬
2598- ‫(‪)۲-۲۳۲-۳۲۸‬‬                                    ‫برین رزمگه بر نشاید بدن‬
2599- ‫از هزار بیت دقسیقی در شاهنامه‬                  ‫(‪)۲-۹۳۲-۲۳4‬‬
2600-
--
3574:       ‫سرانشان به زخم مآنمد به پای‬             ‫‏)‪(VAT-04-F‬‬
3575- ‫بر آکنار هیشوی بد رهنمای‬
3576-                                                       ‫نسیابم دگر نیز همتای اوی‬
3577-         ‫ز هیشوی قیصر بپرسد سخن‬
--
3836:                                                          ‫خروش آمد و بانگ زخم تبر‬
3837-      ‫و و به رخچون بهار‬
3838-                      ‫رچو‬‫سالا‬
3839-                            ‫بهب‬                    ‫سراسیمه شد گیو پرخاشخر‬
--
```


## [2026-09-06T15:01:00.245Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -o 'zaxm \\[.\\{0,120\\}' PHD.txt | head -3"
}
```


### [2026-09-06T15:01:02.086Z] TOOL RESULT

```
zaxm [ztm, z?hm | (P jxm), N ~] wound. тау [zyd$ = Av. zaya-] instrument, weapon. ZÁy-, v. zastan. zay-, -išn(-ig), v. zádan.
```


## [2026-09-06T15:01:18.668Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; for u in \\\n \"https://en.wiktionary.org/wiki/%DA%AF%D8%B1\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/gari%C5%A1\" \\\n \"https://en.wiktionary.org/wiki/%DA%A9%D8%B1%D8%A7%D9%88%D8%A7%D8%AA\" \\\n \"https://en.wiktionary.org/wiki/%CF%86%CE%B8%CE%B5%CE%AF%CF%81%CF%89\" ; do\n echo \"### $u\"; timeout 90 python3 tools/fetch_source.py \"$u\" --note \"page 211 verification\" 2>&1 | tail -2; done"
}
```


### [2026-09-06T15:01:22.600Z] TOOL RESULT

```
### https://en.wiktionary.org/wiki/%DA%AF%D8%B1
/home/sfmqrb/git/rishe/data/verification/sources/web/2d568f61caec4754.txt
### https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/gari%C5%A1
/home/sfmqrb/git/rishe/data/verification/sources/web/9724ef7c6c48934e.txt
### https://en.wiktionary.org/wiki/%DA%A9%D8%B1%D8%A7%D9%88%D8%A7%D8%AA
/home/sfmqrb/git/rishe/data/verification/sources/web/7d18a9cf471e95d8.txt
### https://en.wiktionary.org/wiki/%CF%86%CE%B8%CE%B5%CE%AF%CF%81%CF%89
/home/sfmqrb/git/rishe/data/verification/sources/web/a9b9bd72622f868a.txt
```


## [2026-09-06T15:01:25.582Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; for f in 2d568f61caec4754 9724ef7c6c48934e 7d18a9cf471e95d8; do echo \"###### $f\"; grep -n 'STATUS\\|TITLE' $f.txt|head -2; awk 'NR>140' $f.txt | grep -v '^\\s*$' | sed -n '5,50p'; echo; done"
}
```


### [2026-09-06T15:01:27.297Z] TOOL RESULT

```
###### 2d568f61caec4754
3:STATUS: 200
4:TITLE: گر - Wiktionary, the free dictionary
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
 See also: ـگر , کژ , کر , گز , and کز 
 Burushaski
 [ edit ] 
 Etymology
 [ edit ] 
 (This etymology is missing or incomplete. Please add to it, or discuss it at the Etymology scriptorium .) 
 Pronunciation
 [ edit ] 
 IPA ( key ) : [ɡur] 
 Noun
 [ edit ] 
 گر ( gur ) 
 wheat 
 References
 [ edit ] 
 Bechtholdt, Astrid ( 2026 ), “ gur ”, in Burushaski Hunza Dictionary (Webonary) , Dallas, Texas, USA: SIL International, published 2017 . 
 Old Awadhi
 [ edit ] 
 Noun
 [ edit ] 
 گر ( gr / gir /) [ 1 ] 
 Arabic script form of गिरि ( “ mountain, hill ” ) 
 References
 [ edit ] 
 ^ اَنْصارُ اْللّٰہ، مُحَمَّد [ ansāru llāh, muhammad ] ( 1978 ), “ گِر ”, in پَدْماوَت کِی مُخْتَصَر فَرْہَن٘گ [ padmāvat kī muxtasar farhaṅg , A Short Padmāvat Dictionary ] (in Urdu), 2 nd edition, Aligarh: Letho Car Printers, page 160 . 
 Persian
 [ edit ] 
 Etymology 1
 [ edit ] 

###### 9724ef7c6c48934e
3:STATUS: -1
4:TITLE: 

###### 7d18a9cf471e95d8
3:STATUS: 200
4:TITLE: کراوات - Wiktionary, the free dictionary
 [ edit ] 
 Etymology tree
 Proto-Slavic *xъrvatъ 
 Serbo-Croatian Hrvat bor. 
 French cravate bor. 
 Persian کراوات 
 Borrowed from French cravate . Doublet of کروات ( korovât , “ Croat ” ) .
 Pronunciation
 [ edit ] 
 ( Iran, formal ) IPA ( key ) : [kʰʲe.ɹɒː.vɒ́ːt̪ʰ] 
 Readings
 Iranian reading ? 
 kerâvât
 Noun
 [ edit ] 
 Dari
 نیکتایی 
 Iranian Persian
 کراوات 
 Tajik
 галстук 
 کراوات • ( kerâvât ) ( plural کراوات‌ها ) ( chiefly Iran ) 
 tie (clothing)
 cravate 
 Retrieved from " https://en.wiktionary.org/w/index.php?title=کراوات&oldid=92019617 "
 Categories : Persian terms borrowed from French 
 Persian terms derived from Serbo-Croatian 
 Persian terms derived from French 
 Persian terms derived from Proto-Slavic 
 Persian doublets 
 Persian terms with IPA pronunciation 
 Persian lemmas 
 Persian nouns 
 Iranian Persian 
 fa:Clothing 
 Hidden categories: Pages with etymon 
 Persian entries with etymon 
 Pages with etymology trees 
 Persian entries with etymology trees 
 Persian entries with etymology texts 
 Pages using etymon with no ID 
 Pages with entries 
 Pages with 1 entry 
 This page was last edited on 15 August 2026, at 21:25.
 Definitions and other text are available under the Creative Commons Attribution-ShareAlike License ; additional terms may apply. By using this site, you agree to the Terms of Use and Privacy Policy. 
 Privacy policy
```


## [2026-09-06T15:01:32.264Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; awk '/^ Persian$/,0' 2d568f61caec4754.txt | grep -v '^\\s*$' | sed -n '1,80p'"
}
```


### [2026-09-06T15:01:34.075Z] TOOL RESULT

```
 Persian
 [ edit ] 
 Etymology 1
 [ edit ] 
 Perhaps from Proto-Indo-European *wer- ( “ to burn ” ) . Compare Laki آگر ( agir , “ fire ” ) , Northern Kurdish agir .
 Noun
 [ edit ] 
 گر • ( gor ) 
 flame ; blaze 
 burn ( sensation ) 
 Derived terms
 [ edit ] 
 گر کشیدن ( gor kešidan ) 
 گر گرفتن ( gor gereftan ) 
 Etymology 2
 [ edit ] 
 From Middle Persian .
 Conjunction
 [ edit ] 
 گر • ( gar ) 
 ( poetic ) alternative form of اگر ( agar ) 
 Rumi , Divan-e Shams , [1] 
 گر جان عاشق دم زند، آتش در این عالم زند 
 gar jān-i 'āšiq dam zanad, ātaš dar in 'ālam zanad 
 If the soul of the lover remains silent, fire will consume this world (literally: strike this world). 
 Derived terms
 [ edit ] 
 وگرنه ( vagarna ) 
 Retrieved from " https://en.wiktionary.org/w/index.php?title=گر&oldid=89833858 "
 Categories : Burushaski terms with IPA pronunciation 
 Burushaski lemmas 
 Burushaski nouns 
 bsk:Grains 
 Old Awadhi lemmas 
 Old Awadhi nouns 
 Old Awadhi nouns in Arabic script 
 Persian terms inherited from Proto-Indo-European 
 Persian terms derived from Proto-Indo-European 
 Persian lemmas 
 Persian nouns 
 Persian terms derived from Middle Persian 
 Persian conjunctions 
 Persian poetic terms 
 Hidden categories: Requests for etymologies in Burushaski entries 
 Pages with entries 
 Pages with 3 entries 
 Persian undefined derivations 
 This page was last edited on 13 March 2026, at 01:31.
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
 گر 
 8 languages 
 Add topic
```


## [2026-09-06T15:01:43.619Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; for u in \\\n \"https://abadis.ir/fatofa/%DA%AF%D8%B1/\" \\\n \"https://abadis.ir/fatofa/%DA%AF%D8%B1%D8%B4%D8%A7%D9%87/\" \\\n \"https://www.iranicaonline.org/articles/gayomart/\" ; do\n echo \"### $u\"; timeout 90 python3 tools/fetch_source.py \"$u\" --note \"page 211: Persian gar 'mountain', Garšāh/Gilšāh\" 2>&1 | tail -2; done"
}
```


### [2026-09-06T15:01:50.243Z] TOOL RESULT

```
### https://abadis.ir/fatofa/%DA%AF%D8%B1/
/home/sfmqrb/git/rishe/data/verification/sources/web/eec679535bc2abb8.txt
### https://abadis.ir/fatofa/%DA%AF%D8%B1%D8%B4%D8%A7%D9%87/
/home/sfmqrb/git/rishe/data/verification/sources/web/27c5c06141d665e8.txt
### https://www.iranicaonline.org/articles/gayomart/
/home/sfmqrb/git/rishe/data/verification/sources/web/6774944ef0264561.txt
```


## [2026-09-06T15:01:54.337Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; echo \"=== gar abadis ===\"; grep -n 'STATUS' eec679535bc2abb8.txt; grep -o 'کوه.\\{0,120\\}' eec679535bc2abb8.txt | head -8; echo; echo \"=== garshah ===\"; grep -n 'STATUS' 27c5c06141d665e8.txt; grep -o 'گرشاه.\\{0,200\\}' 27c5c06141d665e8.txt | head -8; echo \"=== iranica ===\"; grep -n 'STATUS' 6774944ef0264561.txt; grep -o 'Gilšāh.\\{0,200\\}\\|Garšāh.\\{0,200\\}\\|Gayōmart.\\{0,150\\}' 6774944ef0264561.txt | head -8"
}
```


### [2026-09-06T15:01:56.357Z] TOOL RESULT

```
=== gar abadis ===
3:STATUS: 200
کوهی است در جنوب شرقی بوشهر و کوه نمک
کوه : گرشاه ( گلشاه پادشاه کوه ملک الجبل لقب کیومرث ) . 
کوه .
کوه است.
کوه واژه ی کهن گرشاه به معنای شاه کوستان که لقب کیومرث پیشدادی بود
کوه، رشته کوه" داشته ایم. 
کوه گر گفته می شد و به کیومرث گرشاه می گفتند
کوه است و در یسنا 1 فقره ٔ 14 و یسنا 2 فقره ٔ 14 و یسنا 3 فقره ٔ 16 و غیره آمده . در دو سیروزه ٔ کوچک و بزرگ در فقره ٔ 28 ز

=== garshah ===
3:STATUS: 200
گرشاه - معنی در دیکشنری آبادیس
گرشاه - معنی در دیکشنری آبادیس 
گرشاه
گرشاه. [ گ َ ] ( اِخ ) رجوع به کیومرث و رجوع به گلشاه شود. 
گرشاه 
گرشاه به معنی پادشاه کوه است و یکی از لقب های کیومرث شاه است 
گرشاه است و این افتخار من است
گرشاه:
=== iranica ===
3:STATUS: 200
Gayōmart/d, Av. gaya marətan “mortal life,” Man. Gehmurd; Ar. Jayūmart), the sixth of the heptad in Mazdean myth of creation, the protoplast of man, and the f
Gayōmart’s life and death are given somehow differently in Middle Persian books. Our main source of information on this first righteous man is the Bundahišn ,
Gayōmart, like other creations, was fashioned forth to assist Ohrmazd in his fight against the Evil Spirit (Ganāg mēnōg; Bundahišn 1a.4). He was created in Ēr
Gayōmart, the pre-eminent element of material beings ( az gētiyān bun ; Bundahišn 3.12; cf. mardōm gētīg pahlom dahišnān “Man the foremost of material creatio
Gayōmart took upon himself to contend with the Ahriman (q.v.), Ohrmazd conceded to grant him perfection and immortality at the Renovation ( frašegird ; Bundah
Gayōmart, Ahriman laid low in his awe for 3000 years, till the arch-demon Whore (Jeh, q.v.) came and roused Ahriman from his stupor, promising him to destroy 
Gayōmart and the creatures of Ohrmazd. Commencing the second cosmic stage, the Mixture ( gumēzišn ), Ahriman attacked the creations and sent Astwihād (q.v.), 
Gayōmart with Want, Sloth, Lust, and 1000 diseases ( Bundahišn 4.19). But his misdeeds were of no avail, since Ohrmazd had brought Sleep in the form of a radi
```


## [2026-09-06T15:02:08.953Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; ls site/pages/211.jpg 2>/dev/null; pdftoppm -f 211 -l 211 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg211 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


### [2026-09-06T15:02:10.936Z] TOOL RESULT

```
site/pages/211.jpg
total 836
drwx------ 2 sfmqrb sfmqrb   4096 Sep  6 11:02 .
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
-rw-rw-r-- 1 sfmqrb sfmqrb  74515 Sep  6 11:02 pg211.png
-rw-rw-r-- 1 sfmqrb sfmqrb  83752 Sep  6 11:01 pg214.png
-rw-rw-r-- 1 sfmqrb sfmqrb 117034 Sep  6 10:54 pg215.png
```


## [2026-09-06T15:02:13.003Z] TOOL CALL #74: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg211.png"
}
```


### [2026-09-06T15:02:13.366Z] TOOL RESULT

```

```


## [2026-09-06T15:02:13.363Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-06T15:02:45.528Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD; grep -n 'gairi' WLD_Bd1_pages.txt | cut -c1-300 | head -5; echo \"=== jasate ===\"; grep -n 'jásate\\|jasate\\|jāsáyati\\|jasayati' WLD_Bd1_pages.txt | cut -c1-300 | head -5; echo \"=== ksarati ===\"; grep -n 'kṣárati\\|ksarati\\|k.árati' WLD_Bd1_pages.txt | cut -c1-250 | head -5"
}
```


### [2026-09-06T15:02:45.623Z] TOOL RESULT

```
=== jasate ===
65712:                                     ai. jasate
=== ksarati ===
47500:s. v. gegen    die Yerbindung mit ai. ksarati „zerflieBt. HieBt", gr. cf Helgco
66184:  Ac. ksarati   „flieBt,   stromt, zerrinnt, verschwindet“,  ksara-m Wasser“,        ,,
```


## [2026-09-06T15:02:49.670Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD; sed -n '65700,65730p' WLD_Bd1_pages.txt | cut -c1-200; echo \"=== ksar ctx ===\"; sed -n '66175,66200p' WLD_Bd1_pages.txt | cut -c1-200; echo \"=== page tags ===\"; awk 'NR<=65712 && /\\[pdf page/ {p=$0} END{print \"jas:\",p}' WLD_Bd1_pages.txt; awk 'NR<=66184 && /\\[pdf page/ {p=$0} END{print \"ksar:\",p}' WLD_Bd1_pages.txt"
}
```


### [2026-09-06T15:02:51.695Z] TOOL RESULT

```
fraqistnan „verderben, intransY, ahd. firqnistcn „verderben, trans.“ (Pe-
dersen und Hirt aaO.; andere Yersuche s. u. ghais- „haften bleiben und
g'Zcdh- „stoBen“).
                                                                                                '
                                                                                           45
                                                                                                                ;




694                                 g«iia-, g”iids         — gusu-, g“u-
      Die Zugehorigkeit von        wild bestritten wegen des Palatals von
                                     ai. jasate

av. f'ra-zalnt „er verlaBt"    Schmidt IvZ. 25, 129, Pick I 4 52, 216, 407,
                                     (s. J.

Hirt BB. 24, 240, Uhlenbeck Ai. Wb. s. v., Wackernagel Ai. Gr. I 160 gegen
273, Brugmann I 590, Scheftelowitz IF. 33, 155); docb ist fra-zahit trotz
                  2


seines a       (wohl   falsclie    Uberlieferung oder jav. fiir a) besser                      als    Injunktiv
des s-Aoristes von ai. ha, idg. ghc- „verlassen“ zu fassen, vgl. ai. muprahcisit
„er      moge nicht verlassen" (Caland KZ. 31, 262, Pedersen aaO.).                                  — Gegen
weitere      Ankniipfungen von Scheftelowitz aaO. s. Bthl.Wb. 411, 1698.
              ar.
   Brugmann vermutete als urspriinglichste Form der Wz. zgtes- (und zg u e-,
das aber am Griech. keinen Anhalt hat) und lieB in den bsl. (und germ.?)
Entsprechungen daraus g"es- durch diss. Schwund des anl. z- entstehn
(ai. jas- konnte an sich auch zg'Les- sein).    Andrerseits vermutet Prell-
=== ksar ctx ===

g;hder- (oder besser g'ider-IT) „rinnen, flieBen; zerrinnen, verschwinden“, im
    ar. Kaus. und im gr. io-Verbum trans. „rinnen lassen, zerrinnen
    lassen“, daher gr. „verschwinden lassen, vernichten“ (vgl. auch die
    Bed.-Entw. von lat. fundere zu „feindlich hinstrecken) u                .




  Ac. ksarati   „flieBt,   stromt, zerrinnt, verschwindet“,  ksara-m Wasser“,        ,,


ksarayati „laBt flieBen“, ksdlayati „wascht ab“ (vgl. auch mind, jhar-,
Wackernagel Ai. Gr. I 241); av. yzaraiti „ stromt, wallt auf“ (die Erkennt-
nis des Anlautes g'ili     +
                          Zischlaut bei Bthl. Ar. Fo. I 1 8ff.), yzarayeiti „la£St
flieBen ', mit Vi- „laBt iiberflieBen"; Weiterbildung (wie nktfftoo ai. piparti.
       1
                                                                                 :




Bthl. Wb. 530) in a-yzradayeiti „laBt aufwallen", vl-yzradayeiti „laBt aus-
einander,   uberwallen"    ;
                                   umgestellt zgar- in avi frazgciraiti         „flieBt      herzu
=== page tags ===
jas: 
ksar:
```


## [2026-09-06T15:02:58.241Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD; grep -n 'giri-h\\|giri-\\|„Berg“' WLD_Bd1_pages.txt | grep -i 'berg' | cut -c1-250 | head -10"
}
```


### [2026-09-06T15:02:58.296Z] TOOL RESULT

```
46300:  Arm. lathi, gen. lerin „Berg“ (Hubschmann Arm. Gr. I 451 m. Lit., Liden
56620:«   jdrbana „Locke“ (apr. garbis „Berg“ sclieint Lw. aus poln. garb „Buckel,
57898:                            „Berg“; vgl. Miihlenbach-Endzelin I 619).
64574:     Ai. girl-lb m. „Berg“, av. ga i ri- ds., aksl. gom „Berg“,                                                     lit.   nugara .(Riickcn
81830:u. *g*er- „Berg“).  Scheftelowitz IF. 33, 165 f.
```


## [2026-09-06T15:03:00.935Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD; sed -n '64565,64600p' WLD_Bd1_pages.txt | cut -c1-200"
}
```


### [2026-09-06T15:03:00.996Z] TOOL RESULT

```
  apr. genna , geuno ,Frau“, aksl. zena ,Frau"; zenim „weiblich"           got.                                                =
qincius              ds.,       z.    B. Curtius 5 175.              Fick     I4       34,   196, 401.    — Uber alb. zone
„Herrin, Frau                    ££
                                      s.    Pedersen KZ. 36, 324.                  Derselbe erklart KZ. 39, 419 arm.
kanailc aus einem alten Kollektiv leeway- = *kanati      doch                                                                  ist   der obige
Vergleich des -ai- mit gr. yvvaix- wohl nicht triigerisch.

1. g“er- „Berg‘‘ (g lt ora, g%ri-).

     Ai. girl-lb m. „Berg“, av. ga i ri- ds., aksl. gom „Berg“,                                                     lit.   nugara .(Riickcn
(eines  Menschen oder Tieres, aber auch eines Berges)“, alb. gur „Stein“
(Pedersen KZ. 36,319, Gdf. g~ e ri~; dazu aucb gr. dsigdg (Hes.) „Hiigel‘%
                                                                ;i
bipidttgos „mit hohen Bergen     detoa  kret. dygas „Hugel, Anliohe*' (Ehr-
                                                                        ,


lich KZ. 39, 569, Gdf. <flerio- gegen Yerbindung von deigas mit ai. drsad
                                                                ;


„Felsen, Miihlstein“ wendet Ehrlich das einfache q von Ortsnamen wie
        2
J egeiov ein; nach Scheftelowitz IF. 33, 166 lautet das ind. Wort vielmehr
dhrsad Bed. ,,Mahlstein‘\ s. *dhlas-)
                ,
                                          ferner mit der Bed.-Entwicklung                ;


,,Berg          — (Berg)wald — Baunk auch                           -
                                                                                        lit. g'ire,    ytriit   ,.Wald'\       lett. ilzire      ds.
und         apr.          gar tan, garrin „Baunk‘ (Trautmann Bsl. Wb. 78; zur Bed. auch
Schulze SBprAk. 1910, 7981.
     Dagegen                Sevdga Hes. zum etymologisch verschiedenen
                             scheint flagveg                •
```


## [2026-09-06T15:03:08.339Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== IEC gʷer mountain ===\"; grep -n \"^g[’']?ori\\|^g'ori-\\|^g.ori-s\\|g.eri-s\" IEC.txt | cut -c1-250 | head -6; echo \"=== IEC gwes ===\"; grep -n \"^g.es-\\|zges\\|sges\" IEC.txt | cut -c1-250 | head -6; echo \"=== SKT cravat ===\"; grep -n -i 'cravat\\|Croat' SKT.txt | cut -c1-350 | head -5; echo \"=== SKT asbestos ===\"; grep -n -i 'asbestos' SKT.txt | cut -c1-350 | head -3"
}
```


### [2026-09-06T15:03:08.514Z] TOOL RESULT

```
=== IEC gʷer mountain ===
=== IEC gwes ===
=== SKT cravat ===
4306:rk.)      Gk.  Kpaffit,    mixing ; , «  Gk.  Mfdrm/fu  (above). >  Autiian.)      F.  cravate, ^1)  a  cravaL       Ctava/s France  in   1636,  oj ii«  who  were  called CrwMUM    or  Cmtfo/ts. ef  Amtrta.
5865:,  to  advance,  augment  (F.— emkMnt^m.  [Of  O.  F.  origin  ; is  oaly  preserved  io  I'lo- ProT.  fvuiUAr,  to  lurthcr, rtschV  —  O.  Pror./Md»j.  before, in  antt,  in  Croat  of,  before ;  sec \  "Wkt  k  is  an  English  insertion.
23571:French  from  Aujtriam :  cravat.
=== SKT asbestos ===
1005:Asbestos,  a  mineral.  <Gk.)  Gk.  <{• <Tf^«TTOf,  unquenchable;  because  it  is  in- combustible, —  Gk.  (1-,  tirg.  prefix;  and •ff/Jiar^r,  quenchable.  from  a^iyyvfu,  i quench,  extinguish.
```


## [2026-09-06T15:03:15.904Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n 'gʷeri\\|gʷor\\|guori\\|gu̯er' IEC.txt | cut -c1-200 | head -8; echo \"---\"; grep -n \"sbennumi\\|σβέννυμι\\|sbestos\" IEC.txt | cut -c1-200 | head -5; echo \"=== IEC ksar ===\"; grep -n 'ksarati\\|gzar' IEC.txt | cut -c1-200 | head -5"
}
```


### [2026-09-06T15:03:15.986Z] TOOL RESULT

```
---
=== IEC ksar ===
```


## [2026-09-06T15:03:18.648Z] TOOL CALL #81: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; head -5 IEC.txt; wc -c IEC.txt; grep -c 'giri' IEC.txt; grep -n 'giri' IEC.txt | cut -c1-250 | head -6"
}
```


### [2026-09-06T15:03:18.723Z] TOOL RESULT

```
Stuart E. Mann AN INDO-EUROPEAN COMPARATIVE DICTIONARY
AN INDO-EUROPEAN COMPARATIVE
DICTIONARY
BY STUART E. MANN
3311889 IEC.txt
9
4013:giro, ið (girr-) “call, cry, squeaP. Cf. gurio, ghirio and WP I, 686 Skt. gire; Per. giristan, inf. (fr. *girisK-) beside girya ‘weeping’; Arm. Cram ‘groan, creak’ beside krvem ‘whine’, krint ‘creak’; Alb. cf. n-gjirrem "am ho
4182:glis (gliiə) ʻa small rodent'. Cf. gəlis Skt. cf. girikà (dim. type ‘mouse’); Gk. galée, galé *weasel' or sim. Lat. glis, gs gliris dor. mouse'
4655:gher- (2) ‘fat Arm. gẹr, gs giri, adj. id.; Ir. geir, f. id.; Oss. cf. dzälarä ‘blob of fat (?)
4685:ghiró, ið (expr: ghirr-) ‘scream, screech, caw? Per. (ambig.) giristan ‘cry’; girye, adj. ^weep- ing’; Arm. redup. gr-gram ‘caw, cackle, cluck’, fr. *ghir-ghir-); cf. W. Arm. kre (gre), s. ‘crane’; Alb. cf. n-gjirrem ‘be hoar
5018:ghrbh- ‘seize’ (?) Cf. gurbh-, and cf. WP I, 595 Vedic grbhnami; cf. Skt. grbhab ‘handle’; Per. inf. giriftan, beside girav ‘pledge’; Hitt. karp (mi) “take, lift, complete'. Ambig. cf. karp-. A parallel form karap- 1sg. karaphi = *
5023:ghrið ‘shout’. (Most of the evidence is am- big., cf. giro, ghiro, gurió & a possible ghir-, all in the same sense) Av. cf. gar- “sing, praise’; Lat. horior ‘exhort. Ennius; (Li. giriù, girti ‘praise’; Latv. dziros, dzirties, re
```


## [2026-09-06T15:03:23.030Z] TOOL CALL #82: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"‘mountain\\|'mountain\" IEC.txt | grep -i 'gor\\|gur\\|gvor\\|gwor' | cut -c1-300 | head -8; echo \"=== extinguish ===\"; grep -n \"extinguish\" IEC.txt | cut -c1-300 | head -8"
}
```


### [2026-09-06T15:03:23.106Z] TOOL RESULT

```
5421:guris, os, us, io ‘wooded hilltop, hill, woog’. WP I, 682 Skt. girih, m. ‘mountain’; Av gairis, m. id.; Per. girive ‘steep acclivity’; Tokh. B karāś "wood": Hes. barües ‘trees’; Ir. (?) brab ‘summit’; Slo- vak hora (wood; mountain’, but ‘mountain’ in Cz. & E S1.); O
=== extinguish ===
2617:dusió “mar; be marred'. Cf. WP I, 766 & 816. See dus-, dusa, etc. Skt. düsyami “be spoilt’; Gk. cf. dos *mi- serable'; LG cf. tuschen, tüschen ‘extinguish’; (e-gde in) OE teorian (‘falter; tire, exhaust, fr. *deuséio)
3354:dhüso, ið (2) *drowse, faint’. (Same as (1) ?) OFris. dusia "be dizzy’, LG düsen ‘daze, be- fuddle; be dazed'; ON dúsa ‘be calm? beside dús ‘lull’; Mod. dúsa *dummy comforter’; Sw. dusa ‘slumber; OHG cf. tūsig ‘mad’; OE dysig ‘foolish’; E dizzy; Li. düstu & dunsu
3839:-osKó, -sKó, inceptive-progressive extn. Gk. khásko, básko, lásko, gignósko, etc.; Lat. hisko & hiasko, -gnosco, senesco, etc.; Alb. njoh, leh, beh ‘know; bark; take by surprise’; Hitt. malesk-imi, malck-ahhi (for *moldhsK-), etc.; OHG. MHG lëskan, léschen, waskan, waschen "be extin
5180:guesó, ið ‘extinguish; be extinguished’. WP I, 693. Cf. guest- Skt. jáse “am exhausted”; Av. zah-, jáh-; Tokh. kás-, B kes-; Gk. cf. s-bénnumi, fut. s-béso; Sw. kväsa ‘stifle’; long o-gde in OCS ga&o, gasiti (and com. Sl.); extn. in Go. us-qistjan ‘kill’; Li. gestu, inf.
10219:lks- (Isk-) (?) Cf. Isus Vedic rksáh ‘harmful’; Skt. “bare, bald; cut, pierced; G. cf. erloschen ‘extinguished’. (Iso- phone: Latv. ilkss 'sled-runner')
10659:merdo, ið ‘wipe out, extinguish; die’. WP II, 278. Cf. mer-, mern-, mr- Arm. merzem ('expel, reject. See SEM : AI: § 97); Gk. cf. a-mérdo ‘rob, deprive; EMG aus-merzen ‘weed out, reject, abolish’; OLI. merdmi, Li. merdziu, inf. merdeti die out: Latv. méerdeju, et, tr. ‘starve�
10748:morios (mrios) "dead, deadly, mortal; death’. Cf. már-, mr- and moruos Skt. máryah “mortal man’; Av. mairyo dead. ly; Arm. majr, in the phr. i majr mtanem ‘extinguish’; W merydd ('sluggish', fr. *mo- I1io-)
11151:morió, moreio “crush, kill; be crushed, dis- integrate’. WP II, 276. Cf. mró, ið Arm. marem ('extinguish'. Ambig. cf. mró); Hitt. mariya(mi) ‘be broken, collapse, melt’; G mähren (2) ‘dawdle’; Icel. merja ‘bruise’; OCS morjo, iti (kilP. Ambig. cf. mro, mar-); Cz. motit (to
```


## [2026-09-06T15:03:32.830Z] TOOL CALL #83: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n 'WP I, 700\\|ghdher\\|gzarati\\|ghzer' IEC.txt | cut -c1-350 | head -6"
}
```


### [2026-09-06T15:03:32.900Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T15:03:40.492Z] TOOL CALL #84: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== FSD asbestos ===\"; grep -o -n 'asbestos[^|]\\{0,300\\}' FSD_vol1.txt | head -2; echo \"=== WEB asbestos ===\"; grep -o -n 'asbestos[^|]\\{0,250\\}' WEB_vol1.txt | head -2; echo \"=== WEB cravat ===\"; grep -o -n 'cravat[^|]\\{0,250\\}' WEB_vol1.txt | head -2; echo \"=== LKT krawatte ===\"; grep -n -i 'krawatte\\|kravate\\|kroat' LKT.txt | cut -c1-250 | head -5"
}
```


### [2026-09-06T15:03:42.339Z] TOOL RESULT

```
=== FSD asbestos ===
14736:asbestos.  2.  A   fabric  made  from  this  mineral.  [< L.  amtantus,  <   Gr.  amianlos.  unstained,  <   a-  priv.  +   mi- ainO .   stain.]  am'I-antt;  am"I-anth'J.—  am*I-an'ti- form,  a.  Like  amlantus  in  form  or  structure.  am"l-an'- thl-formt.—  am-I-an'tlne,  a.  Consisting  of  or  having t
14736:asbestos;  like  amlantus.  am'l-an'- thlnet.—  am'fl-an'thl-nlte,  n.  Mineral.  Asbestos.— am"I-an#told.  I.  a.  Having  the  appearance  of  asbes- tos. am^l-an-thol'dalt;  am"I-an-tol'dalJ.  II-  n.  Min- eral. An  olive-green  coarse  fibrous  variety  of  asbestos. am"I-an'tho!dt.  [amianthus.
=== WEB asbestos ===
2437:asbestos is the fibrous variety. Z ac’tin-6-lit’ic, a. like or containing actinolite. ac-tin’/d-logue (-log), n. any part in a radiate animal that has a homologous relation to an- other in a different segment of the animal. ac-ti-nol/d-gy, 7 {actino-, and Gr
6617:asbestos with long, silky fibers: also ami-
=== WEB cravat ===
45217:cravate, from Cravate, a Croat ]
77159:cravat of this material. foul brood, a contagious bacterial disease of the larvae of bees, which causes a foul odor. foul’dér, v.i. to thunder or flash like lightning.
=== LKT krawatte ===
171:Mittelalters) mong.  =  mongolisch ndl.  =  niederländisch  (holländisch) nfrz.  =  neufranzösisch ngr.  =  neugriechisch nhd.  =  neuhochdeutsch osm.  =  osmanisch-tk. pers.  =  neup^rsisch pg.  =  portugiesisch phÖD.  =  phönizisch piem.
```


## [2026-09-06T15:04:11.400Z] TOOL CALL #85: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -o 'gwer[-0-9]*\\.[^[]\\{0,200\\}\\[Pok[^]]*\\]' AHD_watkins1985.txt | head -10; echo \"=== search Boreas/gora ===\"; grep -o '.\\{200\\}BOREAS.\\{100\\}' AHD_watkins1985.txt | head -3"
}
```


### [2026-09-06T15:04:13.157Z] TOOL RESULT

```
=== search Boreas/gora ===
```


## [2026-09-06T15:04:16.970Z] TOOL CALL #86: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n 'BOREAS\\|Boreas' AHD_watkins1985.txt | cut -c1-400 | head -5; echo \"=== gwer entries ===\"; grep -n 'Pok. 3. g' AHD_watkins1985.txt | cut -c1-200 | head; grep -o 'g[”\"]er-[123]*\\. [A-Z][^.]\\{0,80\\}' AHD_watkins1985.txt | head -10"
}
```


### [2026-09-06T15:04:18.580Z] TOOL RESULT

```
542:shape): DELPHINIUM, DOLPHIN. 2. Prefixed and suffixed form *sm-gvelbh-o-, “born of one womb” (*sm-, one; see sem-'), in Greek adelphos, brother: -ADELPHOUS. [Pok. gtelbh- 473.] gvele-1. To throw, reach. Variant *g/é-, contracted from *guleg-, 1. Suffixed zero-grade form *g/-n-o- in: a. Greek ballein, to throw (with o-grade *bol- and variant *b/é-): BALLISTA; AMPHIBOLE, ASTROBLEME, CATABO
1314:BOOM? bheue- BOON! pbha-2 BOON2 deu-2 BOOR bheue- BOOT? bhad- BOOTH bheue- BORDELLO bherdh- BORDER bherdh- BORE! bher-2 BORE’ bher-1 Boreas gWero-1 BOROUGH bhergh-2 BORROW bhergh-1 BORSCHT bhar- BOSCAGE busk- BOSOM beu-1 BOTH ambh6o BOTHRIUM bhedh- BO TREE bheudh- BOTTOM bhudh- BOTTOMRY bhudh- BOTULIN gWet-3 BOTULINUM gWet-3 BOTULISM gWet-3 BOUCLE beu-1 BOUGH bhaghu- BOUILLABAISSE beu-! BOU
=== gwer entries ===
478:gal-’. To be able, to have power. Gallo-Roman “galia, strength, power, in Old French galliart, lively: GALLIARD. [Pok. 3. gal- 361.]
489:*klai-ni-, bright, pure, in: a. Old English cléne, pure, clean: CLEAN; b. Old English clénsian, to purify, cleanse: CLEANSE. 2. Extended and suffixed zero-grade form *glo-nd in Greek gléné, ey
494:vine, grape: GRAPE; c. Old French grapon, grapnel: GRAPNEL; d. Old French grape, a hook: GRAPPLE; e. Ital- ian dialectal grappa, vine stem, brandy: GRAPPA. 2. Old English crump, crumb, crooked, be
524:gher-’. To shine, glow; gray. Hypothetical base of various Germanic forms. 1. Germanic *gréwaz, gray, in: a. Old English greg, gray: GRAY; b. probably Old English grighund, greyhound: GREYHOUND
540:(COVEN), (COVENANT), EVENT, INTERVENE, INVENT, MIS- ADVENTURE, PARVENU, PREVENIENT, PREVENT, PROV- ENANCE, (PROVENIENCE), REVENANT, REVENUE, SOUVENIR, SUBVENTION, SUPERVENE. 3. Suffixed zero-grade
542:shape): DELPHINIUM, DOLPHIN. 2. Prefixed and suffixed form *sm-gvelbh-o-, “born of one womb” (*sm-, one; see sem-'), in Greek adelphos, brother: -ADELPHOUS. [Pok. gtelbh- 473.] gvele-1. To thr
```


## [2026-09-06T15:04:22.039Z] TOOL CALL #87: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -o 'g[”\"Wv]ero-1[^[]\\{0,300\\}\\[Pok[^]]*\\]' AHD_watkins1985.txt | head -3"
}
```


### [2026-09-06T15:04:24.146Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T15:04:26.360Z] TOOL CALL #88: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -o '.\\{60\\}Mountain.\\{250\\}' AHD_watkins1985.txt | head -5"
}
```


### [2026-09-06T15:04:26.418Z] TOOL RESULT

```
COCRACY, (GYNECOLOGY), POLYGYNY. [Pok. gvend 473.) g”ere-'. Mountain. Possibly o-grade form *gvors- in: a. Greek boreios, “coming from the north” (? < “coming from the mountains of Thrace, north of Greece”), whence Boreas, the north wind: Boras; b. Greek Huperboreioi, Huperboreoi, name of a people living in the far n
```


## [2026-09-06T15:04:31.673Z] TOOL CALL #89: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -o 'g”ere-.\\. Mountain.\\{0,500\\}' AHD_watkins1985.txt | head -2"
}
```


### [2026-09-06T15:04:33.474Z] TOOL RESULT

```
g”ere-'. Mountain. Possibly o-grade form *gvors- in: a. Greek boreios, “coming from the north” (? < “coming from the mountains of Thrace, north of Greece”), whence Boreas, the north wind: Boras; b. Greek Huperboreioi, Huperboreoi, name of a people living in the far north, variously explained as “they who live beyond the north wind” and “they who live beyond the mountains” (hu- per-, beyond; see uper): HYPERBOREAN. [Pok. 3. gver- 477.) gvere-2. Heavy. I. Zero-grade form *gra-. 1. Suffixed form “g“ra-u-i- in Latin
```


## [2026-09-06T15:04:44.691Z] TOOL CALL #90: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; grep -n 'معین\\|دهخدا\\|عمید' eec679535bc2abb8.txt | head -10; echo \"---\"; grep -o 'گر\\b.\\{0,200\\}' eec679535bc2abb8.txt | grep 'کوه' | head -5"
}
```


### [2026-09-06T15:04:46.731Z] TOOL RESULT

```
18: لغت نامه دهخدا
20: گر. [ گ َ ] ( پسوند ) مرادف گار باشد، همچون : آموزگار و آموزگر که از هر دو معنی فاعلیت مفهوم میگردد. ( برهان ). استعمال این لفظ در چیزی کنند که جعل جاعل را تصرف در هیئت آن چیز باشد، چون : شمشیرگر و زرگر مجاز است ، زیرا که جعل و جاعل را در ذات زر و آهن هیچ وضع نیست از جواهر الحروف. ( از آنندراج ) ( غیاث ). بمعنی صاحب و دارنده آید، چون : خصومتگر. توانگر. ( آنندراج ). کننده و سازنده. ( جهانگیری ) ( برهان ). در اوستا کره ( ساخته )، پهلوی کر ، گر ، هندی باستان کره ، کردی کر ( ویرانگر [ ویران کننده ] ) آمده. ( حاشیه برهان قاطع چ معین ). این کلمه بصورت پسوند صفت فاعلی در آخر اسم معنی آید، مانند: پیروزگر، دادگر، بیدادگر، خنیاگر و رامشگر. ( دستور زبان فارسی پنج استاد تألیف آقایان قریب ، بهار، فروزانفر، همایی و رشیدیاسمی ج 1 ص 48 ). بعض لغاتی که به «گر» ختم میشود مبالغه در کار را میرساند و گاه عمل و شغل از آن فهمیده میشود، مثلاً ستمگر شخصی است که ستم بسیار از او سر زند. ( دستور زبان فارسی پنج استاد ایضاً ص 50 ). زرگر، کسی که شغل او زرگری است. گاه این پسوند به اسم معنی ملحق گردد : 
51: فرهنگ معین
59: فرهنگ عمید
141:• فرهنگ فارسی، محمد معین، انتشارات امیر کبیر، تهران، ۱۳۷۵
164:• فرهنگ فارسی، محمد معین، انتشارات امیر کبیر، تهران، ۱۳۷۵
375: آبادیس از سال 1385 فعالیت خود را در زمینه فن آوری اطلاعات آغاز کرد. نخستین پروژه آبادیس، سایت دیکشنری آبادیس بود. دیکشنری آنلاین آبادیس از ابتدا تاکنون تغییرات بسیاری کرده و ویژگی های مختلفی به آن اضافه شده است. آبادیس افزونه ای کاربردی برای مرورگرهای فایرفاکس و کروم و اپلیکیشن موبایل طراحی کرده است که میتوانید از لینک های بالا دانلود کنید. دیکشنری آبادیس شامل بخش هایی نظیر دیکشنری به زبان های مختلف از جمله انگلیسی، فارسی، عربی و همچنین بیست دیکشنری تخصصی با تلفظ انگلیسی و آمریکایی، ترجمه مخفف و کلمات اختصاری، مترجم آنلاین متن، لغتنامه دهخدا، فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راهنمای انتخاب اسم و ... می باشد. 
---
گرشاه ( گلشاه پادشاه کوه ملک الجبل لقب کیومرث ) . 
گر. [ گ َ ] ( اِ ) این کلمه اوستایی و بمعنی کوه است.
گر گفته می شود که در یسنای یک فقره ۱۴ به کوه گر گفته می شد و به کیومرث گرشاه می گفتند
گر. [ گ َ ] ( اِ ) این کلمه اوستایی و بمعنی کوه است و در یسنا 1 فقره ٔ 14 و یسنا 2 فقره ٔ 14 و یسنا 3 فقره ٔ 16 و غیره آمده . در دو سیروزه ٔ کوچک و بزرگ در فقره ٔ 28 زمین ایزد نیک کنش و کوه اوشیدرن و هم
گری ( = گئیری در اوستا ) از برای کوه استعمال شده که در پهلوی گر گویند. . . کیومرث را نیز در فارسی گرشاه یعنی پادشاه کوه نامند. ( یشتها پورداود ج 2 ص 308 ) .
```


## [2026-09-06T15:05:38.405Z] TOOL CALL #91: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; echo \"=== abshar ===\"; grep -n 'STATUS' 227ecb3b9ef07861.txt; awk '/^ Persian$/,0' 227ecb3b9ef07861.txt | grep -v '^\\s*$' | sed -n '1,30p'; echo; echo \"=== phtheiro ===\"; grep -n 'STATUS' a9b9bd72622f868a.txt; grep -n -A8 'Etymology' a9b9bd72622f868a.txt | grep -i 'proto-indo\\|kṣar\\|γžar\\|dʰgʷʰ' | head -5"
}
```


### [2026-09-06T15:05:40.658Z] TOOL RESULT

```
=== abshar ===
3:STATUS: 200
 Persian
 [ edit ] 
 Persian Wikipedia has an article on: آبشار 
 Wikipedia fa 
 Etymology
 [ edit ] 
 Inherited from Middle Persian 𐭠𐭡𐭱𐭠𐭥 ( ābšār ) . By surface analysis , آب ( āb , “ water ” ) +‎ شار ( šār , “ pour ” ) , see شاریدن ( šārīdan ) for the second part. Compare Northern Kurdish avşirr , daşirr ( “ toilet ” ) .
 Pronunciation
 [ edit ] 
 Dari
 آبشار 
 Iranian Persian
 Tajik
 обшор 
 ( Classical Persian ) IPA ( key ) : /ʔaːb.ˈʃaːr/ 
 ( Dari, formal ) IPA ( key ) : [ʔɑːb.ʃɑːɾ] 
 ( Dari, formal ) IPA ( key ) : [ʔɑːb.ʃɑːɾ] 
 ( Kabuli ) IPA ( key ) : [ʔɑːb.ʃɑːɾ] 
 ( Hazaragi ) IPA ( key ) : [ʔɔːb.ʃɔːɾ] 
 ( Iran, formal ) IPA ( key ) : [ʔɒːb.ʃɒːɹ] 
 ( Tajik, formal ) IPA ( key ) : [ʔɔb.ʃɔɾ] 
 Rhymes: -aːr 
 Readings
 Classical reading ? 
 ābšār
 Dari reading ? 
 ābšār
 Iranian reading ? 
 âbšâr
 Tajik reading ? 

=== phtheiro ===
3:STATUS: 200
194- From Proto-Hellenic *kʷʰtʰéřřō , from Proto-Indo-European *dʰgʷʰér-ye-ti , from *dʰgʷʰer- ( “ flow, diverge; perish ” ) via the middle form φθείρομαι ( phtheíromai , “ to be destroyed, perish ” ) with new active meaning “ destroy ” . Cognate to Sanskrit क्षरति ( kṣárati , “ flows, diverges; disappears ” ) , Avestan 𐬖𐬲𐬀𐬭𐬀𐬌𐬙𐬌 ( γžara i ti , “ flows, streams ” ) .
```


## [2026-09-06T15:05:51.197Z] TOOL CALL #92: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; timeout 90 python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/%D8%B4%D8%A7%D8%B1%DB%8C%D8%AF%D9%86\" --note \"page 211: Persian šārīdan 'to flow' (root Gwhder)\" 2>&1|tail -2; f=$(python3 -c \"import hashlib;print(hashlib.sha1('https://en.wiktionary.org/wiki/%D8%B4%D8%A7%D8%B1%DB%8C%D8%AF%D9%86'.encode()).hexdigest()[:16])\"); awk '/^ Persian$/,0' data/verification/sources/web/$f.txt | grep -v '^\\s*$' | sed -n '1,25p'"
}
```


### [2026-09-06T15:05:54.583Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/1ab3e40ba5fdb546.txt
 Persian
 [ edit ] 
 Etymology
 [ edit ] 
 Inherited from Proto-Iranian *gžárati , from Proto-Indo-Iranian *gžʰárati , ultimately from Proto-Indo-European *dʰgʷʰéreti ( “ to flow, to melt ” ) . Cognate with Avestan 𐬖𐬲𐬀𐬭𐬀𐬌𐬙𐬌 ( γžara i ti ) , Ancient Greek φθείρω ( phtheírō ) and Sanskrit क्षरति ( kṣarati , “ to flow, stream, trickle ” ) .
 Pronunciation
 [ edit ] 
 ( Classical Persian ) IPA ( key ) : /ʃaː.riː.ˈdan/ 
 ( Dari, formal ) IPA ( key ) : [ʃɑː.ɾiː.d̪án] 
 ( Dari, formal ) IPA ( key ) : [ʃɑː.ɾiː.d̪án] 
 ( Kabuli ) IPA ( key ) : [ʃɑː.ɾiː.d̪án] 
 ( Hazaragi ) IPA ( key ) : [ʃɔː.ɾi.d̪án] 
 ( Iran, formal ) IPA ( key ) : [ʃɒː.ɹiː.d̪ǽn] 
 ( Tajik, formal ) IPA ( key ) : [ʃɔ.ɾi.d̪án] 
 Rhymes: -an 
 Readings
 Classical reading ? 
 šārīdan
 Dari reading ? 
 šārīdan
 Iranian reading ? 
 šâridan
 Tajik reading ? 
 šoridan
 Verb
```


## [2026-09-06T15:06:00.817Z] TOOL CALL #93: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; mkdir -p data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg211.png data/verification/sources/refs/ocr/BOOK/211.png && ls -la data/verification/sources/refs/ocr/BOOK/211.png; echo \"=== check verify_check ===\"; sed -n '1,60p' tools/verify_check.py"
}
```


### [2026-09-06T15:06:00.901Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 74515 Sep  6 11:06 data/verification/sources/refs/ocr/BOOK/211.png
=== check verify_check ===
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


## [2026-09-06T15:06:04.452Z] TOOL CALL #94: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n '60,130p' tools/verify_check.py"
}
```


### [2026-09-06T15:06:04.488Z] TOOL RESULT

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


## [2026-09-06T15:13:27.588Z] TOOL CALL #95: Bash

```json
{
 "command": "cat > /home/sfmqrb/git/rishe/data/verification/page-211.json <<'JSONEOF'\n{\n  \"pdf_page\": 211,\n  \"book_page\": 181,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-06\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Gwer 4\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *gʷerH- / *gʷer-, *gʷor- 'mountain' (Pokorny 3. gʷer- 'Berg', pp. 477-478)\",\n      \"note\": \"Nourai's numbering ('Gwer 4') is his own; the root is Pokorny's 3. gʷer-, gʷor- 'Berg', which does begin on p. 477 — so POK:477 is exact. Watkins/AHD list the same root as 'gʷerə-1. Mountain. [Pok. 3. gʷer- 477]'. The language label (Indo-European) and the gloss ('mountain') are both right. Modern Wiktionary files the mountain nouns (*gʷr̥H-í-s > Skt girí-, *gʷorH-eh₂ > Slav. gora, Gk. Boréās) under a laryngeal-bearing *gʷerH-, which is the same etymon in modern notation. The chart's cross-reference to 'Gwer 3' (the 'heavy' root, Pok. 2. gʷerə- 476) is only a cautionary note, not a derivation.\",\n      \"note_fa\": \"ریشهٔ هندواروپایی آغازین *gʷerH- (در نگارش پوکورنی gʷer-/gʷor- «کوه») در «فرهنگ ریشه‌شناختی هندواروپایی» پوکورنی، ذیل شمارهٔ ۳، از صفحهٔ ۴۷۷ آغاز می‌شود؛ پس ارجاع نورایی (POK:477) درست است و شماره‌گذاری «Gwer 4» شماره‌گذاری شخصی خود اوست. واتکینز در پیوست AHD نیز همین ریشه را با عنوان «gʷerə-1، کوه» و با ارجاع به پوکورنی ۴۷۷ آورده است. برچسب زبانی (هندواروپایی) و معنی («کوه») هر دو درست‌اند؛ ادعای نورایی دربارهٔ خودِ ریشه پذیرفتنی است.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/g%CA%B7erH-\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:477\", \"status\": \"supports\", \"note\": \"POK_02.txt leaf 135 (printed 477-478): '3. gʷer-, gʷor- ‚Berg‘, ursprüngl. Flexion gʷōr-s, Gen. gʷer-os. Ai. giri-ḥ m. ‚Berg‘, av. gairi- ds.; alb. gur ‚Felsen, Stein‘ … aksl. gora ‚Berg‘ … WP. I 682'. The entry's head stands at the foot of p.477, exactly Nourai's citation.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"WLD\", \"where\": \"Bd. I 682 (incoming/WLD/WLD_Bd1_pages.txt l.64574)\", \"stance\": \"supports\", \"note\": \"'1. gʷer- „Berg“ (gʷora, gʷeri-). Ai. giri-ḥ m. „Berg“, av. gairi- ds., aksl. gora „Berg“, lit. nugara …, alb. gur „Stein“' — Walde-Pokorny's original of Pokorny's entry.\"},\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. gʷerə-1\", \"stance\": \"supports\", \"note\": \"'gʷerə-1. Mountain. Possibly o-grade form *gʷorə- in: a. Greek boreios … whence Boreas … [Pok. 3. gʷer- 477.]' — same root, same Pokorny page as Nourai cites.\"},\n        {\"src\": \"IEC\", \"where\": \"Mann s.v. guris (IEC.txt l.5421)\", \"stance\": \"supports\", \"note\": \"'guris, os, us, io ‚wooded hilltop, hill, wood‘. WP I, 682. Skt. giriḥ, m. ‚mountain‘; Av. gairis, m. id.; Per. girive ‚steep acclivity‘; … Slovak hora …'\"},\n        {\"src\": \"SYN\", \"where\": \"Buck §1.22 MOUNTAIN, HILL, pp. 24-25 (SYN.txt leaf 49-50)\", \"stance\": \"supports\", \"note\": \"'6. ChSl. gora, etc., general Slavic for ‚mountain‘ … : Skt. giri-, Av. gairi- ‚mountain‘, and prob. Alb. gur ‚stone‘. Walde-P. 1.682.'\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"gairi\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Young Avestan gairi- m. 'mountain, mountain range' (also garay-, the weak stem: gen. garōiš, as in the frequent formula haca garōit̰ x'anvantəm 'from Mount X'anvant') is the regular Iranian reflex of PIE *gʷr̥H-i-s, the i-stem seen also in Sanskrit girí- 'mountain'. PIE labiovelar *gʷ gives Indo-Iranian *g (Skt g-, Av. g-); the zero-grade *gʷr̥H- yields Indo-Iranian *gr̥H- > Av. gari-/gairi- with the regular Avestan epenthesis of i before a following i-syllable (gari- > gairi-, § Bartholomae). The Slavic cognate is the full-grade o-form *gʷorH-eh₂ > OCS gora, and the Albanian one gur 'rock'. Nourai's language label and gloss are exact; the arrow from the root is the standard one.\",\n          \"derivation_fa\": \"واژهٔ اوستایی gairi- (ستاک ضعیف garay-) به معنی «کوه، رشته‌کوه» بازماندهٔ صورت ایرانی باستان *gari- از هندواروپایی *gʷr̥H-i-s است؛ همان صورتی که در سنسکریت به شکل giri- «کوه» دیده می‌شود. صامت لبی‌کامی *gʷ در هندوایرانی به g ساده بدل شده و درجهٔ صفر *gʷr̥H- به *gari- رسیده است؛ «ای» میانجی در gairi- همان قاعدهٔ همگونی پیش‌بینایی اوستایی (epenthesis) پیش از هجای دارای i است که بارتولمه آن را توضیح داده است. هم‌ریشه‌های آن اسلاوی کهن gora و آلبانیایی gur «سنگ» است. ادعای نورایی در این گره کاملاً درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/g%CA%B7erH-\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:477\", \"status\": \"supports\", \"note\": \"POK_02.txt l.2022: 'Ai. giri-ḥ m. ‚Berg‘, av. gairi- ds.' — under 3. gʷer- ‚Berg‘ (p.477).\"},\n            {\"ref\": \"KLN:374\", \"status\": \"supports\", \"note\": \"Klein 1966 p.374 s.v. Croat: '… cogn. with OI. giriḥ, Avestic gairi, ‚mountain‘, Alb. gur, ‚rock‘, Lith. girė, ‚forest‘' (KLN_1966.txt l.9710, the printed '374' marker falls inside this entry).\"},\n            {\"ref\": \"SYN:25\", \"status\": \"supports\", \"note\": \"Buck §1.22, table on p.24 lists 'Av. gairi-, paurvata, barəzah-, OPers. kaufa' and the discussion §6 on p.25 links ChSl. gora : Skt. giri-, Av. gairi-.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"Altiranisches Wb. col. 513-514 (BRT.txt l.10224)\", \"stance\": \"supports\", \"note\": \"'j. garay- : gairi- m. ‚Berg, Gebirgszug, Gebirg‘ … airyō.x'šuθəm haca garōit̰ x'anvantəm avi gairim'; also gairi.bərəz- ‚Bergeshöhe‘, gairi.masah- ‚von der Grösse eines Bergs‘, gairi-šāk- ‚in den Bergen heimisch‘.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. I 682\", \"stance\": \"supports\", \"note\": \"'av. gairi- ds.' beside Ai. giri-ḥ under 1. gʷer- „Berg“.\"},\n            {\"src\": \"IEC\", \"where\": \"Mann s.v. guris\", \"stance\": \"supports\", \"note\": \"'Av. gairis, m. id.' beside 'Skt. giriḥ, m. „mountain“'.\"},\n            {\"src\": \"ARY\", \"where\": \"Aryanpur, Latin index (incoming/ARY/ARY_latin_index_pages.txt ll.12621-12644)\", \"stance\": \"supports\", \"note\": \"index entry grouping 'GAIRIVA, GAIRI-: (AVESTAN) … GIRIS (SANSKRIT) … GORA (OLD CHURCH SLAVIC) … GUR (ALBANIAN) … DEIROS (GREEK)', with 'REFERENCES: POKORNY … BUCK: 25' — the same references Nourai gives.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"gar 1\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Middle Persian gar 'mountain' (Book Pahlavi ⟨gl⟩) continues Old Iranian *gari- (= Av. gairi-) by the regular Middle Persian losses: the final short vowel of the i-stem is dropped (*gari- > gar), the Avestan epenthetic -i- of gairi- never existed in the Persian line, and intervocalic/final -r is kept. The word survives as a fossil in Middle Persian compounds and place names (e.g. buland gar 'high mountain' in Šāyast nē Šāyast) and was later replaced in the standard language by kōf/kōh (< OP kaufa-).\",\n          \"derivation_fa\": \"«گر» در فارسی میانه (پهلوی) به نگارش ⟨gl⟩ و به معنی «کوه»، دنبالهٔ صورت ایرانی باستان *gari- (همان gairi- اوستایی) است. در گذر از ایرانی باستان به فارسی میانه واکهٔ کوتاهِ پایانی ستاک i حذف شده (*gari- > gar) و «ای» میانجیِ اوستایی هرگز در شاخهٔ پارسی پدید نیامده است. مکنزی و نیبرگ هر دو این واژه را ثبت کرده‌اند و نیبرگ صریحاً آن را به gairi- اوستایی بازمی‌گرداند. این واژه بعدها جای خود را به «کوه» (از کاوفهٔ پارسی باستان) داد و تنها در ترکیب‌ها و نام‌جای‌ها ماند.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"SNS:318\", \"status\": \"supports\", \"note\": \"Tavoosi's Šāyast nē Šāyast glossary: the word-index (SNS_pages.txt l.16215) reads 'gar 318/19', i.e. gar occurs at text page 318 line 19 — exactly Nourai's citation; the glossary entry (l.12487-88) gives ':gar:' with the etymological reference '(AiW. 511, 513-14) … gairi-', i.e. it derives Pahlavi gar from Avestan gairi- via Bartholomae's columns 513-14. The text also has 'buland gar' (l.4813).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary s.v. gar (PHD.txt l.378)\", \"stance\": \"supports\", \"note\": \"'gar [gl] mountain.'\"},\n            {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II, glossary s.v. gar (NYB_vol2_glossary.txt l.1626)\", \"stance\": \"supports\", \"note\": \"'gar [gl] mountain, pl. cas. obl. ~-ān 20°. — Av. (513 sq.) gari-.' — Nyberg himself makes the Avestan link Nourai draws.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"gar 1; garšâh\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"New Persian گَر gar 'mountain' is the direct continuation of MP gar with no further change; it is archaic/poetic in classical Persian and survives chiefly in the compound گرشاه garšāh and in toponyms. Dehkhoda s.v. گر: 'این کلمه اوستایی و بمعنی کوه است' and quotes Purdavud (Yašthā II 308): 'گری (= گئیری در اوستا) از برای کوه استعمال شده که در پهلوی گر گویند … کیومرث را نیز در فارسی گرشاه یعنی پادشاه کوه نامند' — so garšāh = gar 'mountain' + šāh 'king', 'king of the mountain', an epithet of Kayūmarṯ, the first man/king of the Iranian tradition, and Nourai's note 'it literally means king of mountains' is right (Arabic writers render it malik al-jabal). The variant گلشاه gilšāh printed by Nourai in the extra field is a different formation (gil 'clay' + šāh, 'king of clay', from Gayōmard's creation out of clay) and is not from gar; the two forms are confused already in the medieval sources, and modern scholarship treats Gil-šāh as the older reading. That does not affect the gar > garšāh derivation itself, which is well attested.\",\n          \"derivation_fa\": \"«گَر» در فارسی نو دنبالهٔ بی‌واسطهٔ گرِ پهلوی است و دگرگونی آوایی تازه‌ای در آن روی نداده؛ در فارسی کلاسیک واژه‌ای کهن و شعری است و بیشتر در ترکیب «گرشاه» و در نام‌جای‌ها مانده است. دهخدا ذیل «گر» می‌نویسد: «این کلمه اوستایی و بمعنی کوه است» و از پورداود (یشت‌ها ج۲ ص۳۰۸) نقل می‌کند: «گری (= گئیری در اوستا) از برای کوه استعمال شده که در پهلوی گر گویند… کیومرث را نیز در فارسی گرشاه یعنی پادشاه کوه نامند». پس «گرشاه» = گر (کوه) + شاه، یعنی «پادشاه کوه» و لقب کیومرث است؛ یادداشت نورایی درست است. اما «گلشاه» که نورایی در کنار آن آورده ساخت دیگری است (گِل + شاه، «شاه گِل»، به یادِ آفرینش کیومرث از گِل) و از «گر» نیامده؛ این دو صورت از دیرباز در منابع با هم آمیخته شده‌اند و پژوهش امروزی «گلشاه» را خوانشِ کهن‌تر می‌داند. این نکته به درستیِ زنجیرهٔ گر ← گرشاه آسیبی نمی‌زند.\",\n          \"sources\": [\n            \"https://abadis.ir/fatofa/%DA%AF%D8%B1/\",\n            \"https://abadis.ir/fatofa/%DA%AF%D8%B1%D8%B4%D8%A7%D9%87/\",\n            \"https://www.iranicaonline.org/articles/gayomart/\",\n            \"https://en.wiktionary.org/wiki/%DA%AF%D8%B1\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"MON:3212\", \"status\": \"not_checked\", \"note\": \"Mo'in's 6-volume Farhang-e Fārsi is not online with its original pagination (only the 2-volume Adena abridgement, MON_part1/part2, which has no page breaks and whose OCR of the گ section is too noisy to isolate گر 'کوه'). Page 3212 does fall in the گ range of the continuous pagination of vols. 1-3, which is consistent. The substance of the claim is independently confirmed by Dehkhoda (abadis.ir/fatofa/گر) quoting Purdavud.\"},\n            {\"ref\": \"SNS:318\", \"status\": \"supports\", \"note\": \"same locus as node #2: Šāyast nē Šāyast index 'gar 318/19', glossary entry ':gar:' referred to AiW 511, 513-14 'gairi-'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"abadis.ir/fatofa/گر (فرهنگ معین section) and abadis.ir/fatofa/گرشاه\", \"stance\": \"supports\", \"note\": \"'گرشاه. [گ َ] (اِخ) رجوع به کیومرث و رجوع به گلشاه شود' and 'گرشاه به معنی پادشاه کوه است و یکی از لقب‌های کیومرث شاه است'.\"},\n            {\"src\": \"BQT\", \"where\": \"Dehkhoda quoting Borhan/Purdavud via abadis.ir/fatofa/گر\", \"stance\": \"supports\", \"note\": \"'گر. [گ َ] (اِ) این کلمه اوستایی و بمعنی کوه است و در یسنا ۱ فقرهٔ ۱۴ … آمده'; and 'کوه: گرشاه (گلشاه پادشاه کوه ملک الجبل لقب کیومرث)'.\"},\n            {\"src\": \"HRN\", \"where\": \"Horn, Grundriss (HRN.txt, no entry)\", \"stance\": \"silent\", \"note\": \"grep for 'gar' / 'ger' as a headword meaning 'Berg' finds nothing; Horn's numbered entries do not treat the archaic گر.\"},\n            {\"src\": \"ARY\", \"where\": \"Aryanpur (incoming/ARY/ARY_pages.txt)\", \"stance\": \"silent\", \"note\": \"no Persian headword گر 'کوه'; the mountain cognate set appears only in the Latin index (GAIRI-, GIRIS, GORA).\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Old Slavic\",\n          \"words\": \"čurva; Čurvatinŭ\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"The chart follows Klein 1966 p.374 s.v. Croat: 'OSlav. Chŭrvatinu, Croat, lit. mountaineer, highlander, fr. chŭrva, mountain, which is rel. to OSlav., Serb. and Croatian gora'. Two things are wrong with it. (a) Nourai's spelling 'čurva/Čurvatinŭ' with č misrenders Klein's ch-, which stands for Slavic x (the ethnonym is Proto-Slavic *xъrvatъ, OCS Xrьvatinъ); Slavic č and x are entirely different sounds, so the chart's forms are not what a Slavist would recognise. (b) More seriously, a Slavic noun *xъrva 'mountain' is not attested, and it could not belong to this root anyway: PIE *gʷ- gives Slavic g- (whence gora), never x-. Modern scholarship (Wiktionary with citations; Matasović) treats Proto-Slavic *xъrvatъ as of uncertain, probably Iranian (Scytho-Sarmatian) origin, comparing the 3rd-c. Tanais tablets' Χορούαθος / Χοροάθος, and explicitly rejects the folk-etymological link with gora 'mountain'. Etymonline still repeats Klein's story, but it is a 19th-century tradition, not the current view. The chart's gloss for Čurvatinŭ ('a mountainous area in former Yugoslavia, Croatia') is also off: the OCS form is a personal/ethnic noun 'a Croat', not a place name.\",\n          \"derivation_fa\": \"این گره بر پایهٔ کلاین (۱۹۶۶، ص ۳۷۴، ذیل Croat) کشیده شده که Chŭrvatinu اسلاوی کهن را «کوه‌نشین» و برگرفته از chŭrva «کوه» و هم‌ریشه با gora می‌داند. دو ایراد دارد: نخست آنکه نورایی «ch» کلاین را به «č» برگردانده، حال آنکه آن حرف نمایندهٔ خِ اسلاوی (x) است و صورت درست اسلاوی آغازین *xъrvatъ است؛ دوم و مهم‌تر آنکه واژهٔ *xъrva «کوه» در اسلاوی گواهی نشده و اصلاً نمی‌تواند از این ریشه باشد، زیرا *gʷ هندواروپایی در اسلاوی به g بدل می‌شود (همان gora) نه به x. ریشه‌شناسی امروزی (ویکی‌واژه با ارجاع به ماتاسوویچ) *xъrvatъ را با منشأ نامعلوم و به احتمال ایرانی (سکایی-سرمتی، قیاس با Χορούαθος در لوح‌های تاناییس سدهٔ سوم میلادی) می‌داند و پیوند آن با «کوه» را ریشه‌شناسی عامیانه می‌شمارد. بنابراین پژوهش امروزی این حلقه را رد می‌کند.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Slavic/x%D1%8Arvat%D1%8A\",\n            \"https://www.etymonline.com/word/cravat\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN:374\", \"status\": \"supports\", \"note\": \"Klein 1966 p.374: 'Croat, n. — Fr. earlier Chorwat, fr. Serbo-Croatian Hrvat, fr. OSlav. Churvatinu, „Croat“, lit. „mountaineer, highlander“, fr. chŭrva, „mountain“, which is rel. to OSlav., Serb. and Croatian gora …'. Klein does say what the arrow says, so the citation is faithful — but Klein's claim is itself what modern Slavistics rejects.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"SYN\", \"where\": \"Buck §1.22, p.25 §6\", \"stance\": \"partial\", \"note\": \"'ChSl. gora … : Skt. giri-, Av. gairi- „mountain“' — Buck derives only gora from this root; he knows no *xъrva and does not mention the Croat ethnonym.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. I 682\", \"stance\": \"partial\", \"note\": \"lists 'aksl. gora „Berg“' under 1. gʷer-; no *chŭrva and no ethnonym.\"},\n            {\"src\": \"KLN\", \"where\": \"Klein 1966 p.374 s.v. Croat\", \"stance\": \"supports\", \"note\": \"the source of Nourai's form; quoted above.\"},\n            {\"src\": \"LKT\", \"where\": \"Lokotsch, Etymol. Wb. der europ. Wörter orientalischen Ursprungs\", \"stance\": \"silent\", \"note\": \"grep 'kroat|krawatte|kravate' finds only the abbreviation list — Lokotsch treats only Oriental loans, so Croat/cravate is out of scope.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"French\",\n          \"words\": \"Chorwat; cravate\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"French cravate 'neckcloth' (1650s) is from Cravate 'a Croat', the name applied to the light cavalry of the Habsburg military frontier who wore linen scarves and whose dress became fashionable in Paris after the Thirty Years' War; the immediate source of the French ethnic name is German Krabate/Krawat, itself from Serbo-Croatian Hrvat (< Proto-Slavic *xъrvatъ). Skeat: 'F. cravate, a cravat. Cravats [came into fashion in] France in 1636 … who were called Crovates or Croats'. So the French node is right in substance, but the chart compresses the chain: it draws French directly from 'Old Slavic', omitting Serbo-Croatian Hrvat and the German intermediary, and 'Chorwat' is Klein's citation of an earlier French/German spelling of the ethnonym rather than a French common noun. Given that the parent node (#4) is itself the disputed 'mountain' etymology, this node is at best 'plausible' as drawn.\",\n          \"derivation_fa\": \"واژهٔ فرانسویِ cravate «دستمال گردن» (از دههٔ ۱۶۵۰ م.) از Cravate «کروات» گرفته شده؛ نام سواران سبک‌اسلحهٔ مرزِ نظامی هابسبورگ که دستمال کتانیِ گردنشان پس از جنگ سی‌ساله در پاریس مد شد. صورت قومیِ فرانسوی خود از آلمانی Krabate و آن از صربی-کرواتی Hrvat (اسلاوی آغازین *xъrvatъ) آمده است. اسکیت می‌نویسد که کراوات در ۱۶۳۶ م. به تقلید از «Crovates یا Croats» در فرانسه رایج شد. پس محتوای این گره درست است، اما نمودار زنجیره را کوتاه کرده: از «اسلاوی کهن» یک‌راست به فرانسوی پریده و حلقه‌های صربی-کرواتی و آلمانی را نیاورده است؛ افزون بر این «Chorwat» نه یک واژهٔ عامِ فرانسوی، بلکه املای کهن‌ترِ همان نام قوم به نقل از کلاین است. چون گرهِ پدر (#۴) خود مردود است، این گره «با احتیاط پذیرفتنی» ارزیابی می‌شود.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/cravat\",\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Slavic/x%D1%8Arvat%D1%8A\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN:368\", \"status\": \"supports\", \"note\": \"Klein 1966 p.368 s.v. cravat: 'cravat, n. — F. cravate, fr. Cravate, „Croat, Croatian“, and lit. meaning „neckcloth worn by the Croats“, fr. Serbo-Croatian Hrvat, „Croat“, fr. OSlav. Chŭrvatinu; originally meaning „necktie after the Croatian fashion“. See Croat.' (KLN_1966.txt l.9579; the entry sits between the printed page markers for 368). Note that Klein inserts Serbo-Croatian Hrvat, which the chart omits.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict. s.v. cravat (SKT.txt l.4306, and the 'French from Austrian: cravat' list l.23571)\", \"stance\": \"supports\", \"note\": \"'F. cravate, a cravat. Cravats [came into fashion in] France in 1636, [in imitation] of those who were called Crovates or Croats.'\"},\n            {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century Dict., vol. 1 s.v. cravat (WEB_vol1.txt l.45217)\", \"stance\": \"supports\", \"note\": \"'… cravate, from Cravate, a Croat]'.\"},\n            {\"src\": \"DEV\", \"where\": \"Devic, Dict. étym. des mots français d'origine orientale\", \"stance\": \"silent\", \"note\": \"no entry — cravate is Slavic, not Oriental, so it falls outside Devic's scope.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Persian\",\n          \"words\": \"krâvât\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Persian کراوات is a modern (late Qajar/Pahlavi-era) loan from French cravate, taken over with the usual Persian treatment of an initial French cr- cluster: an anaptyctic vowel is inserted, giving kerâvât (Nourai's transliteration 'krâvât' reflects the spelling, not the pronunciation). Mo'in's Farhang marks it [فر.] 'French' and glosses it 'پارچه‌ای باریک و دراز که به یخهٔ پیراهن بندند و از پیش سینه آویزند؛ دستمال گردن'. Wiktionary gives the same route (French cravate < Serbo-Croatian Hrvat < Proto-Slavic *xъrvatъ) and notes that Persian کروات korovât 'Croat' is its doublet. So the French > Persian arrow is exactly right.\",\n          \"derivation_fa\": \"«کراوات» وام‌واژه‌ای نو (اواخر قاجار و دورهٔ پهلوی) از فرانسویِ cravate است. خوشهٔ آغازینِ cr- در فارسی با واکهٔ میانجی شکسته می‌شود و صورت رایج kerâvât است؛ آوانگاریِ نورایی («krâvât») بازتاب املا است نه تلفظ. معین این واژه را با نشانهٔ [فر.] آورده و چنین معنی کرده است: «پارچه‌ای باریک و دراز که به یخهٔ پیراهن بندند و از پیش سینه آویزند؛ دستمال گردن». ویکی‌واژه نیز همین مسیر (فرانسوی cravate ← صربی-کرواتی Hrvat ← اسلاوی آغازین *xъrvatъ) را می‌دهد و «کروات» را دوگانهٔ (doublet) آن می‌شمارد. ادعای نورایی در این گره درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%DA%A9%D8%B1%D8%A7%D9%88%D8%A7%D8%AA\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"MON:2930\", \"status\": \"partial\", \"note\": \"The 6-vol. Mo'in with its original pagination is not online; in the 2-vol. Adena abridgement (MON_part2.txt l.21581) the entry reads 'کراوات: (اِ.) پارچه‌ای باریک و دراز که به یخهٔ پیراهن بندند و از پیش سینه آویزند؛ دستمال گردن' — the entry exists and is marked French in the print edition, but the cited page number could not be verified. Page 2930 falls in the ک range of the continuous pagination of vols. 1-3, which is consistent.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"MON_part2.txt l.21581 s.v. کراوات\", \"stance\": \"supports\", \"note\": \"definition quoted above; the abridgement drops the bracketed origin tag that the print edition carries.\"},\n            {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e riše-hā-ye hend-o-orupāyi\", \"stance\": \"silent\", \"note\": \"no entry — Aryanpur covers only inherited Persian words with an IE etymology, not European loans.\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"English\",\n          \"words\": \"Croat, Croatia, cravat\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English Croat (1702) is from Serbo-Croatian Hrvat, mediated by French Chorwat/Croate and German Krabate; Croatia is the Latinised country name (Croatia, medieval Latin, from the same ethnonym); cravat (1650s) is the French cravate borrowed into English within a decade of its French coinage, as the neckcloth fashion crossed the Channel. All three are correctly grouped under one head in Klein and in Etymonline; the arrow from the French node is right. What is not right is the ultimate ancestry the chart imposes on them (see node #4).\",\n          \"derivation_fa\": \"واژهٔ انگلیسی Croat (۱۷۰۲ م.) از صربی-کرواتیِ Hrvat و به میانجیِ فرانسوی (Chorwat/Croate) و آلمانی (Krabate) گرفته شده؛ Croatia صورت لاتینی‌شدهٔ نامِ سرزمین است؛ و cravat (دههٔ ۱۶۵۰ م.) همان cravate فرانسوی است که کمتر از یک دهه پس از پیدایش در فرانسه، همراه با مدِ دستمال گردن، به انگلیسی راه یافت. کلاین و اتیمولوژی‌آنلاین هر سه را زیر یک سر واژه می‌آورند و پیکانِ «فرانسوی ← انگلیسی» در نمودار درست است؛ آنچه درست نیست، نیای دورترِ این خانواده است (نگاه کنید به گرهٔ #۴).\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/cravat\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN\", \"status\": \"supports\", \"note\": \"Klein 1966 p.368 s.v. cravat and p.374 s.v. Croat (with 'Derivatives: Croat-ian, adj. and n.'); the two entries cross-refer to each other ('See Croat' / 'cp. cravat').\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"SKT\", \"where\": \"Skeat s.v. cravat (SKT.txt l.4306)\", \"stance\": \"supports\", \"note\": \"'F. cravate … Crovates or Croats'.\"},\n            {\"src\": \"WEB\", \"where\": \"Webster's 2nd, vol. 1 s.v. cravat (WEB_vol1.txt l.45217)\", \"stance\": \"supports\", \"note\": \"'cravate, from Cravate, a Croat]'.\"},\n            {\"src\": \"KLN\", \"where\": \"Klein 1966 pp.368, 374\", \"stance\": \"supports\", \"note\": \"as quoted in ref_check.\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 3,\n      \"root\": \"Gwes, Zgwes\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *(z)gʷes- 'to go out (of fire), be extinguished' (Pokorny p. 479 gʷes-, zgʷes- 'erlöschen')\",\n      \"note\": \"Pokorny p.479 has exactly the double headword Nourai prints: 'gʷes-, zgʷes- ‚erlöschen‘', with Ai. jásate/jāsáyati, Gk. sbénnūmi/ásbestos, Lith. gèsti, OCS ugasiti. Walde-Pokorny I 693 explains the z-: 'Brugmann vermutete als ursprünglichste Form der Wz. zgʷes-'. Watkins/AHD has 'gʷes-. To extinguish. Suffixed variant form *sgʷes-nu- in Greek sbennunai … : ASBESTOS. [Pok. gʷes- 479]'. Root, language label, gloss and page reference are all correct. The internal shape of the chart is looser: it draws the Avestan node out of the Sanskrit node, whereas Sanskrit and Avestan are sisters, not mother and daughter.\",\n      \"note_fa\": \"پوکورنی در صفحهٔ ۴۷۹ دقیقاً همان سرواژهٔ دوگانه‌ای را دارد که نورایی آورده است: «gʷes-, zgʷes- ‚خاموش شدن‘»، با شواهد سنسکریت jásate/jāsáyati، یونانی sbénnūmi و ásbestos، لیتوانیایی gèsti و اسلاوی کهن ugasiti. والده-پوکورنی (ج۱ ص۶۹۳) نیز توضیح می‌دهد که صورت zgʷes- پیشنهاد برویگمان است. واتکینز در پیوست AHD همین ریشه را با ارجاع «Pok. gʷes- 479» آورده و مشتق انگلیسی آن را ASBESTOS دانسته است. پس ریشه، برچسب زبانی، معنی و شمارهٔ صفحه هر چهار درست‌اند. تنها ایراد ساختاری آن است که نمودار، گرهِ اوستایی را فرزندِ گرهِ سنسکریت نشان داده، حال آنکه این دو خواهرند نه مادر و دختر.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/asbestos\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:479\", \"status\": \"supports\", \"note\": \"POK_02.txt leaf 136 (printed 479): 'gʷes-, zgʷes- ‚erlöschen‘. Ai. jásate, jásyati ‚ist erschöpft‘, jāsáyati ‚löscht, erschöpft‘; gr. att. σβέννυμι ‚lösche‘ …, ἄσβεστος ‚unauslöschlich‘ … WP. I 693.'\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"WLD\", \"where\": \"Bd. I 693-694 (incoming/WLD/WLD_Bd1_pages.txt l.65712 ff.)\", \"stance\": \"supports\", \"note\": \"'Brugmann vermutete als ursprünglichste Form der Wz. zgʷes- (und zgʷē-, das aber am Griech. keinen Anhalt hat) … (ai. jas- könnte an sich auch zgʷes- sein)' — the source of Nourai's double headword 'Gwes, Zgwes'.\"},\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. gʷes-\", \"stance\": \"supports\", \"note\": \"'gʷes-. To extinguish. Suffixed variant form *sgʷes-nu- in Greek sbennunai, to extinguish: ASBESTOS. [Pok. gʷes- 479.]'\"},\n        {\"src\": \"IEC\", \"where\": \"Mann s.v. guesó (IEC.txt l.5180)\", \"stance\": \"supports\", \"note\": \"'guesó, iđ „extinguish; be extinguished“. WP I, 693. Skt. jáse „am exhausted“; Av. zah-, jáh-; Tokh. kās-, B kes-; Gk. cf. s-bénnumi, fut. s-béso; … OCS gašǫ, gasiti; Li. gestu' — Mann is the only one of the comparative dictionaries that also assigns an Avestan reflex (zah-) to this root.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Sanskrit\",\n          \"words\": \"jas\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Sanskrit root jas- (pres. jásate, jásyati 'is exhausted, wastes away'; caus. jāsáyati 'exhausts, extinguishes, destroys'; the Dhātupāṭha adds 'to hurt, kill, strike') is the Indo-Aryan reflex of PIE *gʷes-: labiovelar *gʷ before a front vowel is palatalised in Indo-Iranian to *ǰ, whence Skt j-, and *-es- gives -as-. The chart's gloss 'extinguished, exhausted, wounded' collects the intransitive, causative and Dhātupāṭha senses at once; the last ('wounded') comes from Horn's citation of the Dhātupāṭha gloss 'verletzen, tödten, schlagen', and is the sense Nourai needs for the following nodes.\",\n          \"derivation_fa\": \"ریشهٔ سنسکریت jas- (حال jásate/jásyati «فرسوده و درمانده شدن»، سببی jāsáyati «خاموش کردن، از پا درآوردن») بازماندهٔ هندوآریاییِ *gʷes- هندواروپایی است: *gʷ لبی‌کامی پیش از واکهٔ پیشین در هندوایرانی به *ǰ کامی‌شده بدل می‌شود و در سنسکریت j می‌دهد، و *-es- به -as- می‌رسد. معنی سه‌گانه‌ای که نورایی داده («خاموش‌شده، فرسوده، زخمی») در واقع جمعِ معنی لازم، معنی سببی و معنیِ دهاتوپاتهه («آزردن، کشتن، زدن») است؛ همین معنیِ سوم را هرن نقل کرده و نورایی برای گره‌های پسین بدان نیاز دارد.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"POK:479\", \"status\": \"supports\", \"note\": \"POK_02.txt leaf 136: 'Ai. jásate, jásyati ‚ist erschöpft‘, jāsáyati ‚löscht, erschöpft‘' — the first item under gʷes-, zgʷes-.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"WLD\", \"where\": \"Bd. I 693\", \"stance\": \"supports\", \"note\": \"'ai. jas- könnte an sich auch zgʷes- sein' — Walde-Pokorny treat Skt jas- as the Indic reflex and use it to argue for the z- variant.\"},\n            {\"src\": \"IEC\", \"where\": \"Mann s.v. guesó\", \"stance\": \"supports\", \"note\": \"'Skt. jáse „am exhausted“'.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. gʷes-\", \"stance\": \"silent\", \"note\": \"Watkins lists only the Greek branch, because his appendix records only roots with English derivatives.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Avestan\",\n          \"words\": \"zaxya\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Horn (Grundriss no. 652, p.145) is the sole authority here and he himself hedges. He compares NP zaxm with 'aw. zaxya- „zu Tod gehetzt“ (Y. 53,8, Geldner KZ 28,193,202), zaxti (Y. 60,7)' and Skt jas-, and adds 'Wenn die Zusammenstellung richtig ist, so müsste np. zaxm für *zehm stehen'. So (a) the Avestan word is real — it is Geldner's reading of a hapax in Yasna 53.8 — but (b) its meaning is 'hunted/harried to death', not the flat 'wound' Nourai prints, and (c) the arrow as drawn (Sanskrit > Avestan) is a cognate relation, not a descent. In favour of the root assignment: Mann's IEC explicitly lists 'Av. zah-, jáh-' under *gʷeso- 'extinguish', which is the verbal root zaxya- would belong to; Pokorny and Walde-Pokorny, by contrast, cite no Iranian form at all under gʷes-. Acceptable as a possibility, not as an established fact.\",\n          \"derivation_fa\": \"تنها گواهِ این گره هرن است (گرندریس، شمارهٔ ۶۵۲، ص ۱۴۵) و خودِ او با احتیاط سخن می‌گوید: «زخم» فارسی را با اوستایی zaxya- «تا پای مرگ رانده‌شده» (یسنا ۵۳/۸ به خوانش گلدنر) و zaxti (یسنا ۶۰/۷) و ریشهٔ سنسکریت jas- می‌سنجد و می‌افزاید «اگر این هم‌سنجی درست باشد، فارسی نو باید *zehm می‌بود نه zaxm». پس نخست، واژهٔ اوستایی واقعی است ولی یک‌بار-آمد و خوانشی است؛ دوم، معنی آن «زخم» نیست بلکه «تا مرگ رانده‌شده» است؛ و سوم، پیکانِ «سنسکریت ← اوستایی» رابطهٔ هم‌ریشگی است نه تبار. در تأیید نسبت‌دادن به این ریشه، مان (IEC) صریحاً «Av. zah-, jáh-» را ذیل *gʷeso- می‌آورد؛ در برابر، پوکورنی و والده-پوکورنی هیچ صورت ایرانی‌ای ذیل gʷes- نیاورده‌اند. پس این حلقه «با احتیاط پذیرفتنی» است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"HRN:145\", \"status\": \"supports\", \"note\": \"HRN.txt leaf 166 (printed 145), no. 652: 'zaxm „Wunde, Schlag“. aw. vergl. zaxya- „zu Tod gehetzt“ (y. 53, 8, Geldner, KZ. 28, 193, 202), zaxti (y. 60, 7); ai. √jas-, jasyate „erschöpft, todmüde sein, Caus. erschöpfen; verletzen, tödten, schlagen (Dhātup.)“; phlv. zaxm bezw. zahm. Wenn die Zusammenstellung richtig ist, so müsste np. zaxm für *zehm stehen.' — the page says exactly what the chart draws, including the hedge.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"Bartholomae, Altiranisches Wb. (BRT.txt, searched for zaxy-/zax-)\", \"stance\": \"silent\", \"note\": \"grep for 'zaxy', 'zaxti' in the OCR returns nothing usable; the Y 53.8 hapax is a contested reading and the OCR of the z- columns is poor, so Bartholomae could not be consulted directly on this form.\"},\n            {\"src\": \"IEC\", \"where\": \"Mann s.v. guesó (IEC.txt l.5180)\", \"stance\": \"supports\", \"note\": \"'Av. zah-, jáh-' are listed among the reflexes of guesó 'extinguish; be extinguished', which is the root Horn's zaxya-/zaxti would belong to.\"},\n            {\"src\": \"POK\", \"where\": \"POK_02.txt leaf 136 (p.479)\", \"stance\": \"silent\", \"note\": \"the gʷes-/zgʷes- entry cites Indic, Greek, Baltic, Slavic and Germanic but no Iranian form at all.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"zaxm; zaxmeh\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"New Persian زخم zaxm 'wound, blow' continues Middle Persian zaxm, which MacKenzie records with the spellings ⟨ztm⟩ and ⟨z'hm⟩ (Concise Pahlavi Dictionary s.v.: 'zaxm [ztm, z'hm | (P jxm), N ~] wound'); Wiktionary likewise gives only 'From Middle Persian z'hm /zaxm/' and stops there. Nourai's chain (PIE *gʷes- > Skt jas- > Av. zaxya- > NP zaxm) is Horn's tentative proposal of 1893 and no modern handbook repeats it; Horn himself pointed out the phonological difficulty (a form from *zah- ought to have given NP *zehm, not zaxm), and the Pahlavi spelling ⟨ztm⟩ rather points to the family of zad-/zan- 'to strike' (Mo'in's own footnote in Borhan-e Qāṭeʿ derives زدن from Old Iranian jan- 'to strike, kill'). زخمه zaxmeh 'plectrum' is uncontroversial and is confirmed by Mo'in's footnote in Borhan: 'زخمه (پسوند اسم آلت): از زخم' — i.e. zaxm + the instrument-noun suffix -a, 'the thing with which one strikes (the strings)'. Verdict: the words and the internal Persian derivation are confirmed; the link to *gʷes- is only plausible.\",\n          \"derivation_fa\": \"«زَخم» در فارسی نو دنبالهٔ zaxm فارسی میانه است؛ مکنزی آن را با دو املای ⟨ztm⟩ و ⟨z'hm⟩ ثبت کرده و ویکی‌واژه نیز تنها تا فارسی میانه پیش می‌رود و فراتر نمی‌گوید. زنجیرهٔ نورایی (هندواروپایی *gʷes- ← سنسکریت jas- ← اوستایی zaxya- ← فارسی زخم) پیشنهادِ محتاطانهٔ هرن در ۱۸۹۳ است و هیچ دستنامهٔ امروزی آن را تکرار نکرده؛ خودِ هرن هم اشکال آوایی آن را گوشزد کرده بود («باید *zehm می‌شد»). املای پهلویِ ⟨ztm⟩ بیشتر به خانوادهٔ «زدن/زَن-» (از ایرانی باستان jan- «زدن، کشتن») اشاره دارد؛ چنان‌که معین در حاشیهٔ برهان قاطع «زدن» را از همان ریشه گرفته است. «زخمه» به معنی مضراب هیچ اختلافی ندارد و معین در همان حاشیه می‌نویسد: «زخمه (پسوند اسم آلت): از زخم»، یعنی زخم + پسوند اسم ابزارِ «ـه». نتیجه: خودِ واژه‌ها و ساختِ درون‌فارسی تأیید می‌شود، اما پیوند با ریشهٔ *gʷes- تنها «با احتیاط پذیرفتنی» است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%B2%D8%AE%D9%85\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"BQT:1007\", \"status\": \"partial\", \"note\": \"Borhan-e Qāṭeʿ vol. 2 is available only as OCR (no page scan for pp. 550-1230), and the running-head numerals are unreadable; by the leaf≈page-543 mapping the زخ section (بیان چهارم، در زای نقطه‌دار با خای نقطه‌دار) falls on leaves 468-469 = printed ≈1011-1012, i.e. 4-5 pages after Nourai's 1007, so the citation is approximately right but could not be pinned exactly. The relevant text is there: the sub-entries 'زخم بریان' and 'زخم ناخن' and, in the footnotes, Mo'in's note 'زخمه (پسوند اسم آلت): از زخم' plus the neighbouring etymological footnote on زدن ('پهلوی zatan … از ریشهٔ ایرانی قدیم … jan- (کشتن) … بارتولمه').\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie s.v. zaxm (PHD.txt)\", \"stance\": \"partial\", \"note\": \"'zaxm [ztm, z'hm | (P jxm), N ~] wound.' — confirms the Middle Persian ancestor but offers no Old Iranian etymology, and the ⟨ztm⟩ spelling points away from *gʷes-.\"},\n            {\"src\": \"HRN\", \"where\": \"Horn no. 652, p.145\", \"stance\": \"partial\", \"note\": \"gives Nourai's chain but explicitly conditionally: 'Wenn die Zusammenstellung richtig ist, so müsste np. zaxm für *zehm stehen.'\"},\n            {\"src\": \"CHEUNG\", \"where\": \"Cheung, Etym. Dict. of the Iranian Verb (CHEUNG.txt)\", \"stance\": \"silent\", \"note\": \"no entry for a root that would yield zaxm; Cheung has no *gʷes-/*ǰah- lemma with a Persian nominal derivative.\"},\n            {\"src\": \"ARY\", \"where\": \"Aryanpur (incoming/ARY/ARY_pages.txt)\", \"stance\": \"silent\", \"note\": \"زخم appears only as a Persian gloss inside other entries (e.g. l.3709, l.9896), never as a headword with an IE root — Aryanpur declines to give it an Indo-European etymology.\"},\n            {\"src\": \"MON\", \"where\": \"Mo'in's footnote in Borhan-e Qāṭeʿ, BQT_v2_pages.txt leaf 469\", \"stance\": \"supports\", \"note\": \"'زخمه (پسوند اسم آلت): از زخم' — confirms zaxmeh < zaxm + instrument suffix, as the chart's second word requires.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Greek\",\n          \"words\": \"a-sbenunai\",\n          \"verdict\": \"transcription_suspect\",\n          \"error_in\": \"book\",\n          \"book_prints\": \"a-sbenunai\",\n          \"correct_form\": \"ἄσβεστος ásbestos (ἀ- + σβεστός), verbal adj. of σβέννυμι sbénnūmi, inf. σβεννύναι sbennúnai\",\n          \"derivation\": \"The claim behind the box is correct, but the form printed is not a Greek word. Greek σβέννυμι sbénnūmi 'I quench' (Attic, from *sgʷes-nu-mi, the nu-present of PIE *(z)gʷes-; Aorist ἔσβην) has the verbal adjective σβεστός sbestós 'quenched, quenchable', and it is that adjective, not the infinitive, that takes the privative ἀ-: ἄ-σβεστος ásbestos 'unquenchable'. Nourai's 'a-sbenunai' is the infinitive σβεννύναι with one ν dropped and the privative wrongly prefixed to it. The page image (pdf p.211) shows 'a-sbenunai', so the JSON is faithful and the misprint is the book's. The pointer '☞ Ne 1' to Nourai's negative root is right: ἀ- is PIE *n̥-, the zero grade of *ne.\",\n          \"derivation_fa\": \"محتوای این خانه درست است اما صورتی که چاپ شده واژهٔ یونانی نیست. فعل σβέννυμι (sbénnūmi) «خاموش می‌کنم» در آتیک از *sgʷes-nu-mi ساخته شده (ستاک حالِ nu از ریشهٔ *(z)gʷes-) و صفت فعلی آن σβεστός (sbestós) است؛ پیشوند نفیِ ἀ- به همین صفت می‌چسبد و ἄσβεστος «خاموش‌ناشدنی» می‌دهد، نه به مصدر. صورت «a-sbenunai» در واقع مصدرِ σβεννύναι است که یک «ن» آن افتاده و پیشوند نفی به‌غلط بر آن نشسته است. تصویر صفحهٔ ۲۱۱ نشان می‌دهد که خودِ کتاب «a-sbenunai» چاپ کرده است؛ پس خطا از چاپِ کتاب است نه از خوانشِ اسکن. ارجاعِ «☞ Ne 1» درست است: ἀ- همان درجهٔ صفرِ *ne هندواروپایی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/asbestos\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN:111\", \"status\": \"supports\", \"note\": \"Klein 1966 p.111 (KLN_1966.txt l.3580, between the printed markers 111 and 112) s.v. asbestos: 'L. asbestos, fr. Gk. ἄσβεστος, lit. „unquenchable, inextinguishable“, fr. ἀ- (see priv. pref. a-) and σβεστός, verbal adj. of σβεννύναι, „to quench, extinguish“, which derives fr. I.-E. base *gʷes-, „to quench, extinguish“, whence also Lith. gèsti, OSlav. gašǫ, gasiti …'. Klein's own form is σβεστός/σβεννύναι — the two ν's and the correct segmentation, which the chart's 'a-sbenunai' garbles.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"SKT\", \"where\": \"Skeat s.v. Asbestos (SKT.txt l.1005)\", \"stance\": \"supports\", \"note\": \"'Gk. ἄσβεστος, unquenchable; because it is incombustible. — Gk. ἀ-, neg. prefix; and σβεστός, quenchable, from σβέννυμι, I quench, extinguish.'\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. gʷes-\", \"stance\": \"supports\", \"note\": \"'Suffixed variant form *sgʷes-nu- in Greek sbennunai, to extinguish: ASBESTOS' — Watkins too writes sbennunai with two n's.\"},\n            {\"src\": \"POK\", \"where\": \"POK_02.txt leaves 136-137 (pp. 479-480)\", \"stance\": \"supports\", \"note\": \"'gr. att. σβέννυμι ‚lösche‘ (für *σβέσνυμι), Aor. hom. σβέσσαι, ἄσβεστος ‚unauslöschlich‘ … ἔσβην ‚ich erlosch‘ (aus der 2. Sg. e-zgʷes-s …)'.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"English\",\n          \"words\": \"asbestos\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English asbestos is a learned borrowing of Latin asbestos, itself from Greek ἄσβεστος 'unquenchable'. In antiquity the Greek word named a supposed inextinguishable substance (Dioscorides applies it to quicklime); through Latin it was attached in mediaeval and modern usage to the fibrous incombustible mineral. Middle English had asbeston/asbestus via Old French abestos; the modern spelling with -os is a re-Latinisation of the 16th-17th c. The chart's arrow Greek > English is correct as far as it goes, though it silently passes over Latin and Old French. Nourai's AHD:78 refers to the 1975 AHD Indo-European appendix; in the current Watkins text the corresponding entry is gʷes-, which lists ASBESTOS as its only English derivative.\",\n          \"derivation_fa\": \"واژهٔ انگلیسی asbestos وام‌گیریِ دانشورانه از لاتینِ asbestos است و آن از یونانیِ ἄσβεστος «خاموش‌ناشدنی». در دورهٔ باستان این واژهٔ یونانی نام مادّه‌ای پنداشته‌شده بود که خاموش نمی‌شود (دیوسکوریدس آن را بر آهکِ زنده به کار برده) و سپس در لاتینِ سده‌های میانه و زبان‌های نو به کانیِ رشته‌ایِ نسوز اطلاق شد. در انگلیسی میانه صورت asbeston/asbestus از راه فرانسویِ کهن abestos آمده بود و املای امروزی، لاتینی‌سازیِ دوبارهٔ سده‌های شانزدهم-هفدهم است. پیکانِ «یونانی ← انگلیسی» در نمودار درست است، هرچند حلقه‌های لاتین و فرانسویِ کهن را نیاورده. ارجاع AHD:78 به پیوستِ ریشه‌های هندواروپاییِ چاپ ۱۹۷۵ است که در متنِ امروزی واتکینز با مدخل gʷes- برابر می‌شود و تنها مشتق انگلیسیِ آن ASBESTOS است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/asbestos\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD:78\", \"status\": \"supports\", \"note\": \"Nourai's page is in the 1975 New College appendix, which is not open online; the same root in Watkins 1985 (AHD_watkins1985.txt) reads 'gʷes-. To extinguish. Suffixed variant form *sgʷes-nu- in Greek sbennunai, to extinguish: ASBESTOS. [Pok. gʷes- 479.]', and the word-index of the same book lists 'ASBESTOS gʷes-'. Same root, same English derivative.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein 1966 p.111 s.v. asbestos\", \"stance\": \"supports\", \"note\": \"'L. asbestos, fr. Gk. ἄσβεστος … fr. I.-E. base *gʷes-'.\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat s.v. Asbestos\", \"stance\": \"supports\", \"note\": \"'a mineral. (Gk.) Gk. ἄσβεστος, unquenchable; because it is incombustible.'\"},\n            {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls, vol. 1 (FSD_vol1.txt l.14736, s.v. amiantus)\", \"stance\": \"partial\", \"note\": \"F&W defines amiantus as a kind of asbestos ('< L. amiantus, < Gr. amiantos, unstained') — it corroborates the Greek pattern of naming this mineral by a privative adjective but does not itself give the asbestos etymology at the point checked.\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 5,\n      \"root\": \"Gwhder\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *dʰgʷʰer- 'to flow, dissolve, vanish' (Pokorny p. 487 g̑ʰđer-, 'oder besser gʷʰđer-??')\",\n      \"note\": \"Pokorny's headword at the foot of p.487 is 'g̑ʰđer- (oder besser gʷʰđer-??) ‚rinnen, fließen; zerrinnen, verschwinden‘', with Skt kṣárati, Av. γžaraiti, Arm. jur 'water' and Gk. φθείρω; the entry runs on to p.488. Nourai's 'Gwhder' is Pokorny's second, preferred variant gʷʰđer-, so both the root shape and the page number are right, and the gloss 'to flow, run' matches. Modern reconstruction (Wiktionary s.v. φθείρω, following LIV) writes *dʰgʷʰer- with the thorn cluster resolved as dʰgʷʰ-; Cheung 2007 sets up Proto-Iranian *gžar and refers to 'Pok.: 487 f.'. The chart is right that Avestan and Sanskrit are the two branches, though it draws them as two independent children of the root, which is correct here.\",\n      \"note_fa\": \"سرواژهٔ پوکورنی در پایین صفحهٔ ۴۸۷ چنین است: «g̑ʰđer- (یا بهتر: gʷʰđer-؟؟) ‚روان شدن، جاری شدن؛ گداختن، ناپدید شدن‘» با شواهد سنسکریت kṣárati، اوستایی γžaraiti، ارمنی jur «آب» و یونانی φθείρω؛ مدخل تا صفحهٔ ۴۸۸ ادامه دارد. «Gwhder» نورایی همان صورتِ دومِ ترجیحیِ پوکورنی یعنی gʷʰđer- است، پس هم شکل ریشه و هم شمارهٔ صفحه درست است و معنی («جاری شدن، دویدن») نیز می‌خواند. در بازسازیِ امروزی (ویکی‌واژه ذیل φθείρω، بر پایهٔ LIV) این ریشه *dʰgʷʰer- نوشته می‌شود و چونگ (۲۰۰۷) صورت ایرانی آغازینِ *gžar را با ارجاع به «Pok.: 487 f.» می‌آورد. ادعای نورایی دربارهٔ ریشه درست است.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/%CF%86%CE%B8%CE%B5%CE%AF%CF%81%CF%89\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:487\", \"status\": \"supports\", \"note\": \"POK_02.txt leaves 145-146: the headword 'gʷʰđer- (oder besser g̑ʰđer-??) ‚rinnen, fließen; zerrinnen, verschwinden‘' stands at the end of the leaf carrying printed p.487 and continues on the leaf marked '488 f' with 'Ai. kṣárati ‚fließt, strömt, zerrinnt, verschwindet‘, kṣara-m ‚Wasser‘, kṣārayati ‚läßt fließen‘ …; av. γžaraiti ‚strömt, wallt auf‘, γžārayeiti ‚läßt fließen‘ … gr. att. φθείρω … WP. I 700.'\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"WLD\", \"where\": \"Bd. I 700 (incoming/WLD/WLD_Bd1_pages.txt l.66184)\", \"stance\": \"supports\", \"note\": \"'g̑ʰđer- (oder besser gʷʰđer-??) „rinnen, fließen; zerrinnen, verschwinden“ … Ai. kṣárati …; av. γžaraiti „strömt, wallt auf“ (die Erkenntnis des Anlautes gʷʰ + Zischlaut bei Bthl. Ar. Fo. I 18ff.)'.\"},\n        {\"src\": \"CHEUNG\", \"where\": \"Cheung 2007 s.v. *gžar (*gzar?) 'to flow (fast?)' (CHEUNG.txt l.8841 ff.)\", \"stance\": \"supports\", \"note\": \"'*AVESTAN: YAv. γžar- „to flow“ … *SANSKRIT: kṣar „to flow“ … *PIE *dʰgʷʰer- „to flow away“? … LIV: 213 | Pok.: 487 f.'\"},\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985\", \"stance\": \"silent\", \"note\": \"no entry — the root has no English derivative, so Watkins' appendix omits it.\"},\n        {\"src\": \"IEC\", \"where\": \"Mann, IEC.txt\", \"stance\": \"silent\", \"note\": \"grep for 'WP I, 700', 'ghdher', 'kṣarati' returns nothing; Mann has no lemma for this root.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"xšar\",\n          \"verdict\": \"transcription_suspect\",\n          \"error_in\": \"book\",\n          \"book_prints\": \"xšar\",\n          \"correct_form\": \"γžar- (Young Avestan γžaraiti 'flows, streams')\",\n          \"derivation\": \"The derivation itself is standard and correct: Young Avestan γžar- 'to flow' (pres. γžāra-, caus. γžāraya-, intens. γžarō.γžarant-, e.g. ā zrayō āγžārayeiti 'makes the sea swell', Yt 8.31) is the Iranian reflex of PIE *dʰgʷʰer-, the thorn-cluster giving Indo-Iranian *gžʰ- (Skt kṣ-, Av. γž-). But the form the book prints, 'xšar', is voiceless where the Avestan is voiced: Bartholomae (AiW cols. 529-532) has 'γžar- V. „fliessen“ … Et. gleichwertig mit ǰžar-. — ai. kṣárati, gr. φθείρω', Cheung writes YAv. γžar-, Pokorny and Walde-Pokorny write γžaraiti, and Wiktionary γžaraiti. Avestan has no verb xšar-. The page image of pdf p.211 shows 'xšar', so the JSON reproduces the book faithfully; the devoicing is Nourai's own transliteration error.\",\n          \"derivation_fa\": \"خودِ اشتقاق درست و متعارف است: فعل اوستاییِ نو γžar- «جاری شدن» (حال γžāra-، سببی γžāraya-، مکرر γžarō.γžarant-؛ نمونه: ā zrayō āγžārayeiti «دریا را به جوش می‌آورد»، یشت ۸/۳۱) بازماندهٔ ایرانیِ *dʰgʷʰer- هندواروپایی است؛ خوشهٔ آغازینِ موسوم به «thorn» در هندوایرانی به *gžʰ- رسیده که در سنسکریت kṣ- و در اوستایی γž- می‌دهد. اما صورتی که کتاب چاپ کرده، «xšar»، بی‌واک است حال آنکه صورت اوستایی واک‌دار است: بارتولمه (ستون‌های ۵۲۹-۵۳۲) γžar- می‌نویسد، چونگ γžar-، پوکورنی و والده-پوکورنی γžaraiti، و ویکی‌واژه نیز همان. در اوستایی فعلی به شکل xšar- وجود ندارد. تصویر صفحهٔ ۲۱۱ نشان می‌دهد که همین «xšar» در کتاب چاپ شده است؛ پس خطای آوانگاری از خودِ کتاب است، نه از خوانش اسکن.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%CF%86%CE%B8%CE%B5%CE%AF%CF%81%CF%89\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:487\", \"status\": \"partial\", \"note\": \"Pokorny (POK_02.txt leaf 146) supports the derivation but with the voiced form: 'av. γžaraiti ‚strömt, wallt auf‘, γžārayeiti ‚läßt fließen‘, mit vi- ‚läßt überfließen‘; Weiterbildung in ā-γžrādayeiti … umgestellt žgar- in avi frazgaraiti ‚fließt herzu‘'. He knows no xšar-.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"Bartholomae, Altiranisches Wb. cols. 529-532 (BRT.txt ll.10467, 10525)\", \"stance\": \"partial\", \"note\": \"running head 'γžar- mit aiwi 530'; entry: 'j. γžar- V. „fliessen“. Praes. 4 γžāra-, 7 (Int.) γžarī.γžar-, 20 γžaurv-; 30 (Kaus.) γžāraya-. — Absol. γžārəm … Et. gleichwertig mit ǰžar- (sd.) … — ai. kṣárati, gr. φθείρω'. Supports the etymology, contradicts the spelling xšar.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"Cheung 2007 s.v. *gžar (CHEUNG.txt l.8841)\", \"stance\": \"partial\", \"note\": \"'*AVESTAN: YAv. γžar- „to flow“ || (+ *ā-) „to let flow to“ || (+ *ui-) „to let overflow, flood“' — voiced γž throughout; also the neighbouring lemma *gžra(H)d 'to flow' (Av. ā-γžrāδ-).\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. I 700\", \"stance\": \"partial\", \"note\": \"'av. γžaraiti „strömt, wallt auf“ (die Erkenntnis des Anlautes gʷʰ + Zischlaut bei Bthl. Ar. Fo. I 18ff.)' — the initial is expressly gʷʰ + a voiced sibilant, i.e. γž, not xš.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"šârîdan\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"New Persian شاریدن šārīdan 'to flow, pour down, trickle' (and its stem شار šār) continues Proto-Iranian *gžárati, from Proto-Indo-Iranian *gžʰárati < PIE *dʰgʷʰéreti; the initial cluster is simplified to š- (the outcome is regular in the north-western Iranian dialects rather than in Persian proper, so Cheung marks the Persian form with a query and classes it under NWIr). Borhan-e Qāṭeʿ p.1226 has the verb with exactly this sense — 'شاریدن: بر وزن باریدن، فرو ریختن آب و شراب و امثال آن باشد؛ و تراویدن آب را نیز گویند از جراحت' — and Mo'in's footnote there analyses it 'از: شار (ه.م.) + یدن (پسوند مصدری)', adding that the verb is still current in Afghanistan. The nominal شار is preserved in آبشار ābšār 'waterfall', which Wiktionary traces to an attested Middle Persian ābšār (āb 'water' + šār 'pour'), and in سرشار sar-šār 'brimming over'; شُرّان šorrān and شُرشُر šoršor, which Nourai adds, are the onomatopoeic side of the same family (Horn no. 779 lists šurrān, šurrīdan beside šār, ābšār, šārīdan). The variant شیریدن printed in brackets on the page is Nourai's; Horn's corresponding by-form is šīrān 'rain (?)', which he himself queries.\",\n          \"derivation_fa\": \"«شاریدن» در فارسی نو، به معنی «فرو ریختن، جاری شدن، تراویدن»، همراه با ستاک «شار»، بازماندهٔ ایرانی آغازینِ *gžárati و آن از هندوایرانیِ *gžʰárati و در نهایت از *dʰgʷʰéreti هندواروپایی است؛ خوشهٔ آغازین به «ش» ساده شده است. چونگ این صورت را با نشانهٔ پرسش و در ردهٔ ایرانیِ شمال‌غربی می‌آورد، زیرا بازتابِ منتظرِ فارسیِ جنوب‌غربی نیست و احتمالاً از گویش‌های شمال‌غربی (پارتی‌گونه) به فارسی دری راه یافته است. برهان قاطع (ص ۱۲۲۶) همین معنی را دارد: «شاریدن، بر وزن باریدن، فرو ریختن آب و شراب و امثال آن باشد ـ و تراویدن آب را نیز گویند از جراحت»، و معین در حاشیه می‌نویسد: «از: شار (ه.م.) + یدن (پسوند مصدری). در افغانستان نیز «شاریدن» بهمین معنی است». صورت اسمیِ «شار» در «آبشار» (ویکی‌واژه آن را از فارسی میانهٔ گواهی‌شدهٔ ābšār می‌داند: آب + شار) و در «سرشار» مانده است؛ «شُرّان» و «شُرشُر» شاخهٔ آوانمای همین خانواده‌اند (هرن در شمارهٔ ۷۷۹ همهٔ اینها را کنار هم آورده). صورتِ «شیریدن» داخل کمانک از خودِ نورایی است؛ هم‌ارزِ آن نزد هرن šīrān «باران(؟)» است که خودِ او هم بدان تردید دارد. ادعای نورایی در این گره درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%B4%D8%A7%D8%B1%DB%8C%D8%AF%D9%86\",\n            \"https://en.wiktionary.org/wiki/%D8%A2%D8%A8%D8%B4%D8%A7%D8%B1\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"HRN:172\", \"status\": \"supports\", \"note\": \"HRN.txt leaf 193 (printed 172), no. 779: 'šurrān, šarrān „unablässig fliessend“, šīrān „Regen“ (?), šurrīdan, vergl. šār (ābšār), šārīdan. — ai. √kṣar-, kṣárati „fliessen, strömen“ (Geiger, Etym. d. Bal. unter No. 66 …)'. Horn gives exactly the set of Persian words Nourai prints (šār, ābšār, šurrān, šārīdan) and the same Indo-Iranian root.\"},\n            {\"ref\": \"BQT:1223-1265\", \"status\": \"supports\", \"note\": \"checked by rendering pages of Borhan vol. 3 with tools/ref_page.py: p.1223 (pdf 14) is the شاد- run, confirming the pagination; p.1226 (pdf 17) carries 'شاریدن ـ بر وزن باریدن، فرو ریختن آب و شراب و امثال آن باشد ـ و تراویدن آب را نیز کویند از جراحت' with Mo'in's footnote 'از: شار (ه.م.) + یدن (پسوند مصدری). در افغانستان نیز «شاریدن» بهمین معنی است'. The cited range does contain the entry.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"CHEUNG\", \"where\": \"Cheung 2007 s.v. *gžar, section *NWIR (CHEUNG.txt l.8850)\", \"stance\": \"partial\", \"note\": \"'*NWIR: ? NP šaridan/šar- „to flow as rivers, with a great noise; to pour, trickle, urine“' — Cheung accepts the connection but flags it with a query and files it as north-west Iranian, i.e. not the regular south-west Persian reflex.\"},\n            {\"src\": \"HRN\", \"where\": \"Horn no. 779, p.172\", \"stance\": \"supports\", \"note\": \"quoted in ref_check; Horn's entry is the source of Nourai's whole word list.\"},\n            {\"src\": \"BQT\", \"where\": \"Borhan-e Qāṭeʿ p.1226 (ocr/BQT/1226.png)\", \"stance\": \"supports\", \"note\": \"headword and Mo'in's footnote quoted in ref_check.\"},\n            {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien (HUB.txt)\", \"stance\": \"silent\", \"note\": \"no entry for šār/šārīdan; Hübschmann does not treat this verb.\"},\n            {\"src\": \"ARY\", \"where\": \"Aryanpur (incoming/ARY/ARY_pages.txt)\", \"stance\": \"silent\", \"note\": \"no headword آبشار or شاریدن.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Sanskrit\",\n          \"words\": \"kša\",\n          \"verdict\": \"transcription_suspect\",\n          \"error_in\": \"book\",\n          \"book_prints\": \"kša\",\n          \"correct_form\": \"kṣar- (kṣárati 'flows, streams')\",\n          \"derivation\": \"The Sanskrit reflex of *dʰgʷʰer- is the root kṣar-, pres. kṣárati 'flows, streams, melts away, vanishes', with the causative kṣārayati 'makes flow' and the nouns kṣára- 'flowing', kṣára-m 'water'; the thorn cluster *dʰgʷʰ- gives Indo-Iranian *gžʰ-, which is devoiced in Indic to kṣ-. Pokorny p.487 and Walde-Pokorny I 700 both cite kṣárati, and Cheung and Wiktionary give kṣar-/kṣárati as the Sanskrit member of this family. The bare 'kša' printed in the book is the root minus its final -r; it is not a Sanskrit verb meaning 'to flow' (Sanskrit kṣā- means 'to burn'). Nourai writes the Avestan cognate in the same box with its -r ('xšar'), so the omission is an inconsistency of the printed page; the page image of pdf p.211 confirms that the book prints 'kša', so the extraction is faithful.\",\n          \"derivation_fa\": \"بازماندهٔ سنسکریتِ *dʰgʷʰer- ریشهٔ kṣar- است: حال kṣárati «جاری می‌شود، روان است، می‌گدازد، ناپدید می‌شود»، سببی kṣārayati «روان می‌کند» و اسم‌های kṣára- «روان» و kṣára-m «آب». خوشهٔ «thorn» یعنی *dʰgʷʰ- در هندوایرانی به *gžʰ- رسیده و در هندوآریایی بی‌واک شده و kṣ- داده است. پوکورنی (ص ۴۸۷) و والده-پوکورنی (ج۱ ص۷۰۰) هر دو kṣárati را می‌آورند و چونگ و ویکی‌واژه نیز kṣar-/kṣárati را عضو سنسکریتِ این خانواده می‌دانند. صورتِ «kša» که در کتاب چاپ شده همان ریشه بدون «ر» پایانی است و در سنسکریت فعلی به معنی «جاری شدن» نیست (kṣā- در سنسکریت «سوختن» است). نورایی هم‌ریشهٔ اوستایی را در همان صفحه با «ر» نوشته است («xšar»)، پس این افتادگی ناسازگاریِ خودِ صفحهٔ چاپی است؛ تصویر صفحهٔ ۲۱۱ نشان می‌دهد که کتاب «kša» چاپ کرده و خوانشِ اسکن درست بوده است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%CF%86%CE%B8%CE%B5%CE%AF%CF%81%CF%89\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:487\", \"status\": \"partial\", \"note\": \"POK_02.txt leaf 146: 'Ai. kṣárati ‚fließt, strömt, zerrinnt, verschwindet‘, kṣara-m ‚Wasser‘, kṣārayati ‚läßt fließen‘, kṣālayati ‚wäscht ab‘'. Pokorny supports the derivation but has kṣar-, never a form 'kṣa'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"WLD\", \"where\": \"Bd. I 700\", \"stance\": \"partial\", \"note\": \"'Ai. kṣárati „fließt, strömt, zerrinnt, verschwindet“, kṣara-m „Wasser“, kṣārayati „läßt fließen“, kṣālayati „wäscht ab“ (vgl. auch mind. jhar-)' — same form with -r.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"Cheung 2007 s.v. *gžar\", \"stance\": \"partial\", \"note\": \"'*SANSKRIT: kṣar „to flow“ = EWAia I: 428' — the root is kṣar-.\"},\n            {\"src\": \"IEC\", \"where\": \"Mann, IEC.txt\", \"stance\": \"silent\", \"note\": \"no lemma covering this root.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\nJSONEOF\npython3 -m json.tool data/verification/page-211.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 211"
}
```


### [2026-09-06T15:13:30.235Z] TOOL RESULT

```
JSON OK
nodes verified: 15/15
node verdicts: {'confirmed': 8, 'disputed': 1, 'plausible': 3, 'transcription_suspect': 3}
root verdicts: {'confirmed': 3}
ref checks: {'supports': 14, 'not_checked': 1, 'partial': 4}
books consulted: {'supports': 26, 'silent': 13, 'partial': 11} | by book: {'WLD': 5, 'ARY': 5, 'IEC': 4, 'SKT': 4, 'CHEUNG': 4, 'BRT': 3, 'MON': 3, 'HRN': 3, 'KLN': 3, 'PHD': 2, 'BQT': 2, 'WEB': 2, 'AHD': 2, 'POK': 2, 'NYB': 1, 'SYN': 1, 'LKT': 1, 'DEV': 1, 'FSD': 1, 'HUB': 1}
```


## [2026-09-06T15:13:57.226Z] AGENT

Done — `/home/sfmqrb/git/rishe/data/verification/page-211.json` written, `verify_check.py 211` reports 15/15 nodes, 0 PROBLEM lines.

**Page 211 (book p. 181) — 3 roots, 15 nodes**

Roots: 3 confirmed (Gwer 4 = Pok. 3. gʷer- 477 'Berg'; Gwes/Zgwes = Pok. 479; Gwhder = Pok. 487 gʷʰđer-). Nodes: 8 confirmed, 3 plausible, 1 disputed, 3 transcription_suspect. Ref checks: 14 supports, 4 partial, 1 not_checked.

Disputed
- **Gwer 4, #4 Old Slavic `čurva` / `Čurvatinŭ`** — Nourai faithfully copies Klein p.374 ("OSlav. chŭrvatinu … fr. chŭrva 'mountain', rel. to gora"), but no Slavic *xъrva 'mountain' is attested and PIE *gʷ- gives Slavic **g**-, never x-. Modern view (Wiktionary/Matasović): Proto-Slavic *xъrvatъ is of uncertain, probably Iranian (Scytho-Sarmatian, cf. Tanais Χορούαθος) origin. Knock-on: #5 French downgraded to plausible.

Transcription-suspect (all `error_in: "book"` — the JSON matches the printed page, verified on the page image, copied to `data/verification/sources/refs/ocr/BOOK/211.png`)
- **Gwhder #1 `xšar`** — Avestan verb is voiced **γžar-** (Bartholomae cols. 529-32, Cheung *gžar, Pokorny/WLD γžaraiti). No Avestan xšar- exists.
- **Gwhder #3 `kša`** — Sanskrit root is **kṣar-** (kṣárati); "kša" lacks the -r (and Skt kṣā- means 'to burn').
- **Gwes #4 `a-sbenunai`** — not a Greek form; ἄσβεστος = ἀ- + σβεστός, verbal adj. of σβέννυμι (inf. σβεννύναι, two ν). Underlying claim is right.

Plausible
- **Gwes #2 Av. `zaxya`** — real (Geldner's reading, Y 53.8) but glossed 'hunted to death', not 'wound'; Horn himself hedges the whole comparison. Chart also draws Avestan out of Sanskrit (sisters, not descent).
- **Gwes #3 NP `zaxm`/`zaxmeh`** — MP zaxm confirmed (MacKenzie ⟨ztm, z'hm⟩), but no modern work repeats Horn's *gʷes- link; ⟨ztm⟩ points to zad-/zan-. zaxmeh < zaxm + -a confirmed by Mo'in's Borhan footnote.

No extraction errors found: every suspect form matches the printed page.

Notes on Nourai's own refs: SNS:318 verified exactly (index "gar 318/19", glossary refers gar to AiW gairi-); HRN:145 and HRN:172 verified verbatim; BQT:1223-1265 verified by rendering p.1226 (شاریدن + Mo'in's footnote), cached at `sources/refs/ocr/BQT/1226.png`; BQT:1007 only approximately locatable (Borhan vol. 2 has no page scan — the زخ section maps to printed ≈1011-12); MON:3212 not checkable (6-vol. Mo'in pagination is not online), but confirmed in substance from Dehkhoda/Purdavud (گر = کوه, گرشاه = پادشاه کوه, epithet of Kayūmarṯ).
