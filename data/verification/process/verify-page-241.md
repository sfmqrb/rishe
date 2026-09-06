# Verification process log — verify-page-241


## [2026-09-06T15:46:43.200Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 241 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-241.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-241.json. Write /home/sfmqrb/git/rishe/data/verification/page-241.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 241` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T15:46:44.461Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T15:46:45.904Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


## [2026-09-06T15:46:45.913Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-241.txt"
}
```


### [2026-09-06T15:46:45.931Z] TOOL RESULT

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


### [2026-09-06T15:46:45.935Z] TOOL RESULT

```
1	=== PDF page 241 (book page 211) ===
2	--- entry 0 ---
3	ROOT Kapasti -> redirect to Kapastay
4	--- entry 1 ---
5	ROOT [Indo-European] Kapho : hoof  (refs POK:530)
6	#1 (parent #0) [Avestan] refs=POK:530 | safa : hoof
7	  #2 (parent #1) [Pahlavi] refs=HRN:164 | sumb 1 : hoof
8	    #3 (parent #2) [Persian] refs=BQT:1163 | som «سُم ۱» : hoof | extra: سُنب
9	  #4 (parent #1) [Persian] refs=MON:1825; SOD:65 | safal «سَفَل» : hoof (of a camel) | extra: سَپَل ، شَفَل ، سَوَل
10	#5 (parent #0) [Germanic] refs=AHD | hôfaz : hoof
11	  #6 (parent #5) [English] refs=None | hoof
12	--- entry 2 ---
13	ROOT [Greek] Kapparis : a shrub  (refs AHD:199; KLN:234)
14	#1 (parent #0) [Persian] refs=KLN:234; SKT:75; BQT:1587; KGW:98; AFM:131 | kabar «کَبَر» : a shrub | extra: قَبَر ، قَباریس | NOTE: KGW:98 indicates that this word reached Europe from Old Persian through the Greek
15	#2 (parent #0) [Latin] refs=AFM:131; KLN:234 | capparis
16	  #3 (parent #2) [English] refs=None | caper
17	--- entry 3 ---
18	ROOT [Old Persian] Kapŭl : city of Kabul in Afganistan  (refs MON6:1487)
19	#1 (parent #0) [Pahlavi] refs=MON6:1487 | kâpŭl
20	  #2 (parent #1) [Persian] refs=MON6:1487; AHD:589; VFO:24 | Kâbol «کابل» : Kabul ; kowlî «کولی» : gypsy ; kâbolî «کابلی ۲» : a dried fruit from Kabul | extra: کابلی ۱ | NOTE: Note that the English word "gypsy", short for "E-gypsi-an", is from a different root but was used to refer to Kabul nomads who migrated to Europe in the 14th & 15th century and were mistaken with Egyptians.
21	    #3 (parent #2) [English] refs=KLN:272 | Kabul ; chebule : a dried fruit (originally from Kabul)
22	
```


## [2026-09-06T15:46:47.836Z] AGENT

I'll now look at the source JSON and the reference infrastructure.


## [2026-09-06T15:46:49.212Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-241.json && echo \"=== SOURCE MATRIX ===\" && cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read page JSON and source matrix"
}
```


### [2026-09-06T15:46:49.263Z] TOOL RESULT

```
{
  "pdf_page": 241,
  "book_page": 211,
  "entries": [
    {
      "root": {
        "name": "Kapasti",
        "redirect": "Kapastay"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Kapho",
        "lang": "Indo-European",
        "refs": "POK:530",
        "gloss": "hoof"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:530",
          "words": [
            {"translit": "safa", "gloss": "hoof", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "HRN:164",
          "words": [
            {"translit": "sumb 1", "gloss": "hoof", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "BQT:1163",
          "words": [
            {"translit": "som", "gloss": "hoof", "script": "سُم ۱"}
          ],
          "script_extra": "سُنب",
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 1,
          "lang": "Persian",
          "refs": "MON:1825; SOD:65",
          "words": [
            {"translit": "safal", "gloss": "hoof (of a camel)", "script": "سَفَل"}
          ],
          "script_extra": "سَپَل ، شَفَل ، سَوَل",
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "hôfaz", "gloss": "hoof", "script": null}
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
            {"translit": "hoof", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Kapparis",
        "lang": "Greek",
        "refs": "AHD:199; KLN:234",
        "gloss": "a shrub"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "KLN:234; SKT:75; BQT:1587; KGW:98; AFM:131",
          "words": [
            {"translit": "kabar", "gloss": "a shrub", "script": "کَبَر"}
          ],
          "script_extra": "قَبَر ، قَباریس",
          "note": "KGW:98 indicates that this word reached Europe from Old Persian through the Greek",
          "quote": null
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Latin",
          "refs": "AFM:131; KLN:234",
          "words": [
            {"translit": "capparis", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "caper", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Kapŭl",
        "lang": "Old Persian",
        "refs": "MON6:1487",
        "gloss": "city of Kabul in Afganistan"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Pahlavi",
          "refs": "MON6:1487",
          "words": [
            {"translit": "kâpŭl", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "MON6:1487; AHD:589; VFO:24",
          "words": [
            {"translit": "Kâbol", "gloss": "Kabul", "script": "کابل"},
            {"translit": "kowlî", "gloss": "gypsy", "script": "کولی"},
            {"translit": "kâbolî", "gloss": "a dried fruit from Kabul", "script": "کابلی ۲"}
          ],
          "script_extra": "کابلی ۱",
          "note": "Note that the English word \"gypsy\", short for \"E-gypsi-an\", is from a different root but was used to refer to Kabul nomads who migrated to Europe in the 14th & 15th century and were mistaken with Egyptians.",
          "quote": {
            "text": "کاین صید نکردند به مردی و به اقبال - دستان که به کابل شد و رستم به سمنگان",
            "poet": "Asîr"
          }
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "English",
          "refs": "KLN:272",
          "words": [
            {"translit": "Kabul", "gloss": null, "script": null},
            {"translit": "chebule", "gloss": "a dried fruit (originally from Kabul)", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
=== SOURCE MATRIX ===
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


## [2026-09-06T15:46:54.071Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nfor k in ['POK','HRN','BQT','MON','SOD','AHD','KLN','SKT','KGW','AFM','VFO','PHD','BRT','WLD','LKT','HJB']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:700]); print()\n\""
}
```


### [2026-09-06T15:46:56.101Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index 

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the 

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.c

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol 

SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get s

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifie

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO pri

SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<i

KGW {"title": "J. Ibrahim, Kulturgeschichtliche Wortforschung: Persisches Lehngut in europäischen Sprachen, Wiesbaden 1991", "edition_found": null, "kind": "google_books_preview", "url": "https://books.google.com/books?id=OUtZZNSUi3cC (partial preview) ; HathiTrust uc1.b3624504 search-only", "identifier": null, "local_file": null, "page_offset": null, "lookup_hint": "Google Books limited preview only (index pages).", "notes": "RE-SEARCH 2026-09: preview only (Google Books partial view usable for spot checks); no PDF on the author's site jamshid-ibrahim.net; purchase from Harrassowitz."}

AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM.txt"], "page_offset": "19

VFO null

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<ident

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between 

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.39015066210397 (browser only from this host)", "identifier": "in.gov.ignca.20339 (Band 3); also in.ernet.dli.2015

LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 'NNNN. word (language) meaning' - Lokotsch is usually cited by entry number, but Nourai cites pages.

HJB {"title": "H. Yule & A. C. Burnell, Hobson-Jobson, 2nd ed. by W. Crooke, London 1903 (Delhi reprint 1968)", "edition_found": "1903 Crooke edition (pagination identical to the 1968 reprint)", "kind": "archive_djvu", "url": "https://archive.org/details/hobsonjobsonagl02croogoog", "identifier": "hobsonjobsonagl02croogoog (others: bub_gb_6Z5iAAAAMAAJ, hobsonjobsonglos00yulerich, india.history.resource.89053)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HJB.txt", "page_offset": "leaf = printed + 35..51 (plates inserted; e.g. leaf 83 = p.32, leaf 319 = p.270, leaf 535 = p.490, leaf 905 = p.870). local file has \\f between leaves (0-based leaf index i == i-th form-feed pag
```


## [2026-09-06T15:46:59.651Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==538 || NR==539' POK_01.txt | head -80"
}
```


## [2026-09-06T15:47:00.597Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"ka:pho\\|kāpho\\|kapho\\|Huf\" POK_full.txt | head -40"
}
```


### [2026-09-06T15:47:02.294Z] TOOL RESULT

```
(Bash completed with no output)
```


### [2026-09-06T15:47:02.355Z] TOOL RESULT

```
44211:Root / lemma: kapho-ox Ropho-: hoof, *claw, nail' derived from Root/ lemma: Reub- 
44242:Modern High German Hufe, Hube, alb. /royos/?/© "garden'. 
56737:Latvian /^pai. ' paw; Huflattig ', also " water lily, lotus plant ' (compare above Modern 
72595:clasp, buckle '; Latvian se^/ 'cover'. Old Prussian sagis^ buckle, Hufnagel'; Old Church 
75398:"Huftl<nochen, ham', KwAnv, -nvoq, kwAeoc; ds., KcbArmJ f. " popiiteus, anl<ie' (to 1. -ap- 
77902:German s/a, s/a^e'Schlagwerkzeug', Middle Low German s/an/e'Hufbeschlag', Middle 
78108:Swedish dial. slu{]/} ( *sluhwd) "die husk um den empfindlichsten Toil in Horn or Hufe', 
78109:Norwegians/c»"the fleischige Kern in Horn or Hufe', Middle Low German s/J"Fruchthulse,
```


## [2026-09-06T15:47:04.307Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '44195,44260p' POK_full.txt"
}
```


### [2026-09-06T15:47:04.358Z] TOOL RESULT

```
Root / lemma: kam- 

Meaning: " lust, desire, crave; seek after, look for ' 

See also: see above S. 515 ka-. 

Page(s): 525 

Root / lemma: kapha- or Ropho- 
Meaning: hoof, *claw, nail 



Note: 

Root / lemma: kapho-ox Ropho-: hoof, *claw, nail' derived from Root/ lemma: Reub- 

thorn' 

Material: Old Indie sapha- m. "hoof, claw, nail ', Avestan safa- m. "hoof of the horse'; 

Old Icelandic hofr. Old English hof. Old High German huofhooV. 

References: WP. I 346, Specht Indo Germanic Dekl. 253. 
Page(s): 530 

Root / lemma: kapo- 

Meaning: things that float in water 



Material: Old Indie sapa-m. " was flieflendes Wasser mit sich fuhrt, Trift, Geflofttes ', 
sapeta-m. " washed ashore reed '; Lithuanian sapai^ scattered stalks, remains which an 
inundation on the fields leaves behind ', sapas' stem, straw, bough'. 
References: WP. I 345, Specht Indo Germanic Dekl. 27. 
Page(s): 529 

Root / lemma: kap-, kap- 

Meaning: a piece of land 

Material: Gr. Kpnoc;, Doric kc(tto(; "garden', Hes. Konuc; Kpnoc; (Cretan " uncultivated small 

area of land', s. Gl. 3, 303); Old High German huoba. Old Saxon hoba^ a piece of land ', 

Modern High German Hufe, Hube, alb. /royos/?/© "garden'. 

References: WP. I 345, Specht Indo Germanic Dekl. 27, places here Old High German 

habaro etc. " oat '. 

See also: S. under under kapro- 

Page(s): 529 

Root / lemma: kar- 
Meaning: wax 

Material: Gr. kx\^6q, " wax ', Kripiov "honeycomb, a cutaneous disease', although Doric 
Kap6(; can be secure enough, out of Ion. -Attic are loanwords from this dialect group, Latin 
cera as gr. loanword; 

Lithuanian korys^ honeycomb, honeycomb of the bees'.
```


## [2026-09-06T15:47:09.565Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"safa\\b\\|çapha\\|sapha\" incoming/WLD/WLD_Bd1_pages.txt | head -20; echo \"---AHD---\"; grep -n -i \"kapho\\|hoof\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-06T15:47:09.633Z] TOOL RESULT

```
32605:  Ai. gapha-   m. „Huf, Klaue“, av. safa- m. „Huf des Pferdes“.
---AHD---
581:BIT), GAMBOL, (GAMBREL), (GAMMON3), (JAMB). 2. Suf- fixed form *kamp-ulo- in Greek kampulos, bent: CAMPYLOTROPOUS. [Pok. kam-p- 525.] kan-. To sing. 1. Germanic *han(e)ni in Old English hen(n), hen: HEN. 2. Latin canere, to sing (> cantdre, to sing): CANOROUS, CANT?, CANTABILE, CANTICLE, CANTIL- LATE, (CANTO), CANTOR, CANZONE, CHANT; ACCENT, DESCANT, ENCHANT, (INCANTATION), INCENTIVE, PRE- CENTOR, RECANT. 3. Latin oscen, a singing bird used in divination (< *obs-cen, “one that sings before the au- gurs”; ob-, before; see epi): OSCINE. 4. Suffixed form *kan-men- in Latin carmen, song, poem: CHARM}. [Pok. kan- 525.] kand-. To shine. 1. Suffixed (stative) form *kand-é- in Latin candére, to shine: CANDENT, CANDID, (CANDIDA), (CANDIDATE), CANDLE, CANDOR; INCANDESCE. 2. Latin transitive *candere, to kindle, in compound incendere, to set fire to, kindle (in-, in; see en): (INCENDIARY), IN- CENSE. [Pok. kand- 526.] kannabis. Hemp. Late Indo-European word borrowed from an unknown source. 1. Germanic *hanipiz in Old English henep, henep, hemp: HEMP. 2. Greek kannabis, hemp: CANNABIS, (CANVAS). kanto-. A corner, a bending. Celtic *cantos, rim, border, in Latin cantus, canthus, iron ring around a carriage wheel, a wheel, rim (> Italian canto, corner): CANTEEN, CANTON; DECANT. [Pok. kan-tho- 526.] kap-. To grasp. I. Basic form *kap-. 1. Germanic *haf- in Old English hefeld, thread used for weaving, heddle (a device which grasps the thread): HEDDLE. 2. Germanic *haftjam in Old English heft, handle: Harr. 3. Form *kap-o- in Germanic *habai-, *habén in Old English habban, to have, hold: HAVE. 4. Germanic hafigaz, “containing something,” having weight, in Old English hefig, heavy: HEAVY. 5. Germanic *hafnd-, perhaps “place that holds ships,” in Old English hefen, a haven: HAVEN. 6. Germanic habukaz in Old English h(e)afoc, hawk: HAWK}, 7, Latin combining form -ceps (< *kap-s), “taker.” II. Suffixed form *kap-yo-. 1. Germanic *hafjan in Old English hebban, to lift: HEAVE. 2. Latin capere, to take, seize, catch: CABLE, CAPABLE, CAPACIOUS, CAPIAS, CAPSTAN, CAPTION, CAPTIOUS, CAPTIVATE, CAPTIVE, CAP- TOR, CAPTURE, CATCH, (CHASE!); ACCEPT, ANTICIPATE, CONCEIVE, DECEIVE, EXCEPT, INCEPTION, (INCIPIENT), INTERCEPT, INTUSSUSCEPTION, MUNICIPAL, NUNCUPA- TIVE, OCCUPY, PARTICIPATE, PERCEIVE, PRECEPT, RE- CEIVE, (RECOVER), RECUPERATE, (RX), SUSCEPTIBLE. III. Suffixed form *kap-s- in Latin capsa, repository, case: CAISSON, CAPSICUM, CAPSID, CAPSULE, CASE2, CHASE?, CHASES, CHASSIS, CHESS?; ENCHASE. IV. Length- ened-grade variant form *kdép-. 1. Germanic *hof- in compound *bi-hdf, “that which binds,” requirement, obligation (*bi-, intensive prefix; see ambhi), in: a. Old English behdf, use, profit, need: BEHOOF; b. Old English behéfian, to have need of: BEHOOVE. 2. Greek k6pé, oar, handle: copePpop. Compare ghabh-. [Pok. kap- 527.] kap(h)o-. Hoof. Lengthened-grade form kdp(h)-o- in Germanic *héfaz in Old English Adf, hoof: Hoor. [Pok. kapho- 530.] kapro-. He-goat, buck. Latin caper, he-goat (> capra, she-goat): CABRILLA, CABRIOLET, CAPELLA, CAPRIOLE, CHEVRON; CAPRIC ACID, CAPRICORN, CAPRIFIG, CAPROIC ACID. [Pok. kapro- 529.] kaput. Head. 1. Germanic *haubidam, *haubudam, in Old English héafod, head: HEAD. 2. Latin caput, head (> Italian capo, head): CABEZON, CADET, CAPE?, CAPITAL, CAPITAL, CAPITATE, CAPITATION, CAPITELLUM, CAPITU- LATE, CAPITULUM, CAPO!, CAPRICE, CAPTAIN, CATTLE, CAUDILLO, CHAPITER, CHAPTER, CHIEF, CHIEFTAIN; BI- CEPS, CHAMFRON, DECAPITATE, KERCHIEF, MISCHIEF, OCCIPUT, PRECIPITATE, RECAPITULATE, SINCIPUT, TRI- ceps. [Pok. kap-ut- 529.] kar-', Hard. I. Variant form ker-. 1. Suffixed o-grade form *kor-tu- in Germanic *harduz in: a. Old English hard,
787:animal: NEAT2; b. compound form *ga-nauta- (*ga-, with, together; see kom), “he with whom one shares possessions,” companion, fellow, in (i) Middle Dutch ghenét, noot, fellow: MATELOTE (ii) Old High German ginéz, companion, in German Eidgenosse, confederate: HuGuEnot. [Pok. neu-d- 768.] newn. Nine. 1. Germanic *niwun, with variant *nigun, in Old English nigon, nine: NINE, NINETEEN, NINETY, NINTH. 2. Latin novem, nine (< *noven, with m for n by analogy with the m of septem, seven, and decem, ten): NOVEMBER, NOVENA; NONAGENARIAN. 3. Ordinal form *neweno- in Latin nénus, ninth: NONA-, NONES, NOON; (NONAGON), (NONANOIC ACID). 4. Prothetic forms *enewn, *enwn in Greek ennea, nine (> *ennewa, *enwa-): ENNEAD. [Pok. e-neuen 318.] newo-. New. Related to nu-. 1. Suffixed form *new-yo- in Germanic *neuja- in: a. Old English néowe, niwe, new: NEw; b. Old Norse njyr, new: SPAN-NEW. 2. Basic form *newo- in Greek newos, neos, new: NEO-, NEON, NEOTER- IC; MISONEISM. 3. Suffixed form “new-aro- in Greek nearos, young, fresh, contracted into néros, fresh (used of fish and of water), hence néron, water: ANEROID. 4. Basic form *newo- in Latin novus, new: NOVA, NOVATION, NOVEL!, NOVEL?, (NOVELTY), NOVICE; INNOVATE, REN- OVATE. 5. Suffixed form *new-er-ko- in Latin noverca, stepmother (< “she who is new”): NOVERCAL. [Pok. neuos 709.] ni. Down. 1. Suffixed form *ni-t- in Germanic *nith- in Old English nithan, neothan, below: BENEATH, UNDER- NEATH. 2. Suffixed (comparative) form *ni-tero-, lower, in Germanic *nitheraz in Old English nither, lower: NETHER. See compound root nizdo-. [In Pok. 1. en 311.] [niké. Victory. Greek noun of unknown origin. NIKE.] nizdo-. Bird’s nest. Compound root formed from ni + *sd-, zd-, zero-grade form of sed-; literally, “place where the bird sits down.” 1. Germanic *nist- in: a. Old English nest, nest: NEST; b. Germanic ‘*nistilon in Old English nestlian, to make a nest: NESTLE. 2. Latin nidus, nest: NICHE, NIDE, NIDUS; EYAS, NIDIFY. [In Pok. sed- 887.] nobh-. Also ombh-. Navel; later also “central knob,” boss of a shield, hub of a wheel. 1. Germanic *nabo in: a. Old English nafu, nafa, hub of a wheel: NAVE?; b. compound *nabé-gaizaz, tool for piercing wheel hubs (*gaizaz, spear, piercing tool; see ghaiso-), in Old Eng- lish nafogar, auger: AUGER. 2. Variant form *ombh- in Latin umbé, boss of a shield: uMBO. 3. Suffixed form *nobh-alo- in Germanic *nabalé in Old English nafela, navel: NAVEL. 4. Suffixed variant form *ombh-alo- in: a. Latin umbilicus, navel: UMBILICUS; NOMBRIL; b. Greek omphalos, navel: OMPHALOS. [Pok. 1. (enebh-) 314.] nogh-. Also enogh-, ongh-. Nail, claw. 1. Suffixed (diminutive) form *nogh-ela- in Germanic *nagla- in Old English negl, nail: NAIL. 2. Form *onogh- in Greek onux (stem onukh-), nail: ONYX; PARONYCHIA, PERIONYCHIUM, SARDONYX. 3. Variant form *ongh- in Latin unguis, nail, claw, hoof, with diminutive ungula, hoof, claw, talon (< ongh-eld-): UNGUIS. [Pok. onogh- 780.] nogv-. Naked. 1. Suffixed forms *nog’-eto-, *nog’-oto- in Germanic *nakweda-, *nakwada- in Old English nacod, naked: NAKED. 2. Suffixed form *nog~-edo- in Latin niidus, naked: NUDE, NUDI-; DENUDE. 3. Suffixed form *nog’-mo- differentiated or developed into Greek gum- nos, naked: GYMNASIUM, GYMNAST; GYMNOSOPHIST, GYMNOSPER\M. [Pok. nog¥- 769.] no-men-. Name. Earlier form *()noo-mn, zero-grade form *(g)na-men-. 1.Germanic *nam6n- in Old English nama, name: NAME. 2. Latin némen, name, reputation: NOMINAL, NOMINATE, NOUN; AGNOMEN, COGNOMEN, DENOMINATE, IGNOMINY, MISNOMER, NOMENCLATOR, NUNCUPATIVE, PRAENOMEN, (PRONOUN), RENOWN. 3. Greek onoma, onuma, name: ONOMASTIC, -ONYM, -ONYMY; ANONYMOUS, ANTONOMASIA, EPONYM, (EPON- YMOUS), EUONYMUS, HETERONYMOUS, HOMONYMOUS,
1282:BEE? bheug-3 BEECH bhago- BEEF gWou- BEETLE! bheid- BEETLE? bhau- BEFALL p(h)ol- BEFORE pert BEGET ghend- BEHEST kei-3 BEHIND ko- BEHOOF kap- BEHOOVE kap- BELAY legh- BELCH bhel-4 BELDAM deu-2 BELEAGUER legh- BELEMNITE gWele-1
1642:HOOF kap(h)o-
```


## [2026-09-06T15:47:15.241Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"safa-\" BRT.txt | head -20"
}
```


### [2026-09-06T15:47:15.296Z] TOOL RESULT

```
15436:•  j.  para.safa-  ro.  'Vorderhuf:  U  °/inhB zaranatna  paüiJmuxla  (sd.)  äai  kl  apara insaiama  Yt/o.  135.
16130:•  j.   para^u.safa-  Adj.   'breithufig',  von  |M?r^i7«aiw  "es  verleiht  Schutz  die  Feder.."
25959:•  j.  safa-  ra.  'Huf  des  Pferdes:  aurvants..
```


## [2026-09-06T15:47:15.656Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==186' HRN.txt"
}
```


### [2026-09-06T15:47:17.813Z] TOOL RESULT

```
- 164 —
743. seg *Hund'; vergl. arab. sij[ihistan d. i. np. seglpistän
'Fructus Cordiae Myxae , Sebestenen , Brustbeere*
(AM. 155).
g. saha^ sewä; Semn. eshe (vergl. Vullers ispnh,
ispehj isbähy Isbeh) ;täl. sipä'^); Käs. eshd^ espa.
niedisch^) (Snd^a (r^yr y,vva y.dkhovöi anuna M^Jb/),
Herod. I, 110; aw. span- Hund'; phlv. aak^ sag; ai.
cvdn-; arm. sun (H. No. 224).
kurd. seh (d. i. se) *Hund', Plur. sän, seiän; afy. spai.
744. »ffgtir^ sngvrne, stiyvr 'Stachelschwein'. Si/uL sJ/ttr,
g. si/ttr.
aw. sukuruna- (zu den Hundearten gezählt); phlv.
sukur (Thonnelier).
kurd. LW. st/ör; af}'. sktlnr, skön (Dar niest et er,
Ch. pop. 8 45 ; ebendaselbst baragsta (Dialekt des
Distrikts VazTrl) snkal); bei. sikun^ n. sl/un \Stachel-
schwein' (345).
745. {\)fiuniy sumh^) *Huf.
aw. vergl. safa- 'Huf; phlv. suinb, arm. LW. smhak;
ai. vergl. QapUä' 'Huf*; an. hüfr, nhd. Hüf,
kurd. LW. shn; af;. sioa gespaltener Huf, LW.
sum; oss. säffäg *Huf, Klaue' (224); wa;^. sar. LW.
süm.
Eine Urverwandtschaft ist sicher zwischen aw.
safa-, ai. (japhd-, afy. swa^ oss. säffäg einerseits und
np. surn^ snmh andererseits anzunehmen.
746. {2)sumi^ sunb 'Höhle, Loch*, smnhiden^).
kurd. so7ifin^ LW. sümb^)^ stitfib^) (H.-Sch.),
sumbtden^); bei. LW. (?) sumb Xoch', snmhag, n.
sumbay *bohren, stechen (351, 352).
Zu np. sufte^i (No. 740).
*) Vergl. hyrkän. spas bei de Lagarde, Ges. Abh. 226, 227.
*) D. i. wohl auch ap. (vergl. Hörn, Indog. Forsch. II, 137), da
die dialektischen Formen doch nicht sämmtlioh medisch sein kennen.
') Sieho vorige Seite Note 2.
```


## [2026-09-06T15:47:33.905Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD sumb ===\"; grep -n \"sumb\\|sumb\\b\" PHD.txt PHD_mackenzie.txt | head -20; echo \"=== NYB ===\"; grep -n \"sumb\" NYB_vol2_glossary.txt | head -10; echo \"=== HUB ===\"; grep -n \"sumb\\|safa-\" HUB.txt | head -20; echo \"=== CHEUNG safa ===\"; grep -n \"safa-\" CHEUNG.txt | head -10"
}
```


### [2026-09-06T15:47:33.986Z] TOOL RESULT

```
=== PHD sumb ===
PHD.txt:572:stün(ag) [stwn(k)!' | M 'stwn, N sutūn] column, pillar, mast. stir [sżwl] trustee, curator, guardian. ~ЛЬ : trusteeship. sturģ [stwlg | N suturg] fierce, contentious; gross, coarse. süd [swt! | M send, N ~] use, profit, advantage. sudab [st?*5 | N ~] rue. sūd-abģār [swt?fk'/] profitable. sūdaģ [swtk!] negligent, indolent. ~ih: negligence, indolence. sidan, sāy- [swtn', s'd- | N ~] rub. sūd(ö)mand [swt(?w)mnd | N sūdmand] useful. suft [swpt' | N ~] shoulder. suftan, sumb- [swptn!, swmb- | N ~] pierce, bore. sumb [swmb* | N ~] hoof. isūr [sw] | M swr, N ~] meal, feast, banquet. *sür [sel] strong. sūrāg [swl(?)k'] hole, burrow. ~ig [-yk'] burrowing (animal). ««Omand (-'wmnd] holed. sūrāx [swPh | N ~] hole. sust [swst! | = M, N —] slack, lazy. ~ih: slackness, laziness. Iguš [swš | (N šus)] lung. *suš [stw$] degree (of arc). suxr [swhl | N surx] red. suy [swd | M swy-] hunger. *swahistan, swah- [swh-stn' | P swh-] sigh. sya [syd? | (P syw, N styah)] black. ~hag [-hk' | N -a] pupil (of eye).
PHD.txt:2307:hoof sumb.
PHD.txt:5498:sumb- sumb sustih sust
PHD_mackenzie.txt:4710:suftan, sumb- [swptn', swmb- I N -] pierce, bore.
PHD_mackenzie.txt:4711:sumb [swmb ' I N~] hoof.
PHD_mackenzie.txt:6777:helpful ayaromand, frayadisnig.                hoofsumb.
PHD_mackenzie.txt:10829:                                       .            sumb-
PHD_mackenzie.txt:10831:                                                    sumb
=== NYB ===
687:āsēnēn adj. of iron 2076. 2327, 241; ~-sumb v. sumb.
3563:sumb [swmb'] hoof of a beast 4914-18, 9418-19. Gsénén-~ iron-hoofed (or iron- shod?) 2212, 2812.23. — Arm. lw. smbak < *sumbak; NP sunb.
3564:sumbömand [---”wmnd] having strong hoofs 4917,
7421:sunb: sumb
=== HUB ===
2670:745. Zd. safa- = skr. gapha- lasst sich schwer mit np.
2671:5wm, gunb = ap. ^sumba- oder *sumpa', das im Skr.
2675:bal. sumbag 'bohren', nb. sumbay *Seitenstechen das,
2676:wenn es nicht entlehnt ist, auf ein iran. pr. "^sumbami
6506:Ind. 204; skr. kapha- (wie zd. safa- *Huf = skr. gapha-),
9204:8unb perforatio* = bal. sumb *a hole, boring', zu mftan,
9205:pr. sunbam 'durchbohre*, bal. sumbag 'bohren (oben p. 76);
=== CHEUNG safa ===
```


## [2026-09-06T15:47:35.324Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SOD sfr/spl ===\"; grep -n \"hoof\" SOD_pages.txt | head -20; echo \"=== SOD entry 65 area ===\"; grep -n \"^ *65 \\|^65 \" SOD_pages.txt | head"
}
```


### [2026-09-06T15:47:35.399Z] TOOL RESULT

```
=== SOD sfr/spl ===
=== SOD entry 65 area ===
3974:                                                                     65 »8yt M                                       t            s
```


## [2026-09-06T15:47:39.987Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '2660,2690p' HUB.txt; echo \"=== ctx 6500 ===\"; sed -n '6495,6515p' HUB.txt"
}
```


### [2026-09-06T15:47:40.039Z] TOOL RESULT

```
ausserdem auch angi^t (Nr. 126) und zuyaly {zuyOl i sang
*Steinkohle* Rosen, Np. Sprachfiihrer p. 35). = jiid.
tat. zugol^ zuwol (Miller p. 69), kas. zugol etc.
743. Gitay^a ist medisch, aber nicht altpersisch. Gerade im
Altpersischen ist s fiir sp einigemal bezeugt {visa- =
vispa-^ asa^) *Pferd' = aspa- u.s. w.), daher die Dialekt-
formen mit 6, v wahrscheinlich nicht der Persis (ap.
^saka- = np. sag *Hund') angehoren.
744. Afgh. sk&n (= *5fcar«a) und skun (= "^skurna). Die np.
Formen gehoren verschiedenen Dialekten an.
745. Zd. safa- = skr. gapha- lasst sich schwer mit np.
5wm, gunb = ap. ^sumba- oder *sumpa', das im Skr.
"^gumbha- oder *gumpa' lauten wiirde, vereinigen.
746. Np. sunb perforatio* = bal. stimb a hole, boring
gehort jedenfalls zu suftatif pr. sunbam 'durchbohre',
bal. sumbag 'bohren', nb. sumbay *Seitenstechen das,
wenn es nicht entlehnt ist, auf ein iran. pr. "^sumbami
(skr. *gumbhaini) hinweist. Sonst konnte auch iran.
^sumpdmi angesetzt werden. In beiden Fallen stimmt
der Inf. np. suftan. Dazu np. sufra = afgh. LW.
sufra *the anus* = ap. *sufra- aus ^gupra- ? Zd. si/^
und suwrO- (var. sufrO-) sind in der Bedeutung un-
sicher.
747. Die Erklarung von sang *Stein, Gewicht* stimmt, wenn
man fiir das Altpersische die Formen ^a&anga- (=:np.
-asang) 'Stein und *&anga' {^= np. sang) ^) *Steiu' an-
*) In asabara- *Reiter* = np. asvar und in ap. *asatara = np.
aatar 'Maulesel*, skr. agvatara- (neben ap. uvaapa^ ViStaspa, Aspacana,
*) Ap. & (aus k^) im Anlaut = np. s.
•) Zd. asenga-, wenn es hierher gehort, konnte fiir asenga"
stehen.— 77 —
=== ctx 6500 ===
Ap. / (= idg. p und ph) = np. / und A.
§ 80. Ap. / = iran. / zwischen Vokalen (= idg. ph)
wird im Np. zu h oder / :
a) zu A in : kdh *Berg*, koha *hSherer Theil des Battels,
H5cker , paz. Uh *Berg, phi. kGf 'Berg Gl. and Ind. 201,
kdfak *Satter, West PT. 4, 48, bal. kdpak, nb. kl^fay *Schulter ,
arm. kohak 'Woge, Berg (Job. Kathol. u. s. w.), ap. kaufa-
*Berg*, zd. kaofa- 'Hiigel, H5cker ; dahdn *Mund', paz. dahan
Shk. 240, zd. zafan-, bal. LW. dap, nb. daf; Nihavand (Stadt)
= Nupavavia (Ptol.) ZDMG. 31, 149.
b) zu / in: kaf Schaum' = zd. ka/a-, phi. kaf Gl. and
Ind. 204; skr. kapha- (wie zd. safa- *Huf = skr. gapha-),
c) In den iibrigen Fallen steht dem iran. / aus ph im
Idg. bh, welchem iran. b entspricht, gegeniiber:
naf, nafa 'Nabel', phi. nafak, bal. napag, nb. nafay,
zd. na/d 'Nabel' ZPGl. p. 10, 'Geschlecht' yt. 13, 87 (=
arisch "^naphas-) neben zd. nabanazdista-, skr. nabhi- *Nabel
und Nabe (arische Wzl. nabh) ; baftan we ben*, pr. bafam,
osset. vafyn, bal. gvapag, nb. gvafay u. s. w. (H. 168) von
iran. vof- (= arisch vdph) neben zd. ubdafMa-, skr. urna-
vHbhi' (idg. vebh Veben ) ; zafar 'Rachen' (Parsenwort ? neben
```


## [2026-09-06T15:47:49.229Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BQT v2 page 1163 ===\"; grep -n \"\\[pdf page\" BQT_v2_pages.txt | head -3; echo \"---\"; grep -n \"سنب\\|سُنب\" BQT_v2_pages.txt | head -10"
}
```


### [2026-09-06T15:47:49.300Z] TOOL RESULT

```
=== BQT v2 page 1163 ===
---
1588:‫است نا‬   ‫‪ ۳‬نام ماه موافق‬    ‫آنکه نام روز‬    ‫و سنب‬     ‫حرارت تب را کوبند ‪٩‬‏ ‪ -‬و بسکون ثابی‌شادی‬
2916:  ‫رك ‪ :‬نوروزنامه ص ‪ . ۳۳ - ۰۳‬جو ‪ 011160۲01‬از رستة غلات‌استوسنبله‌آن ساده وشاخه‌های‬
10609:‫وزن قرابتان » رستنیی باشد مانند سنبلالطیب ‪.‬‬             ‫صدا و خراخری که بسبب کلو فشردن از کلو‬
10611:‫بسنبل میماند وبوی ستبل‌لیز دارد وطبیعت آن‌هم‬                                            ‫مشدید ثالی همکفته‌اند ‪.‬‬
10613:       ‫زديك امت بسنبل و درطعم وحیلان‬                       ‫بروزن‌نظام ‪ ۰‬رفتاری‌را گونند‬        ‫س‬   ‫خرام‬
13453:                 ‫فرشت » بروزن و معنی خمجه‬                                   ‫خمیره ‪ - ۲‬با رای‌قرشت بروزن سنبله‪.‬‬
17238: ‫سنبه ‪ = °‬بفتح لون «معنی‬             ‫د‬
17244:    ‫با منقار سوراخ‪ .‬میکند ودرختینه سنبه ه‬
17274:                                                        ‫‪ -1‬رك ‪ :‬درف« اسشق ص‪.*۱ ۲۲‬‬                     ‫سنبه ‪.‬‬
21188:   ‫‪ . ۵۵۵۷۸ =°‬از دستهٌ غلات » سنبله‌های آن بهم فثرده لیت و در نقاط مرطوب‬
```


## [2026-09-06T15:47:50.226Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== MON سپل/سفل ===\"; grep -n \"سپل\\|سفل \" MON_part1.txt MON_part2.txt | head -20; echo \"=== ARY som ===\"; grep -n \"سنب\\|سم \" incoming/ARY/ARY_pages.txt | head -10"
}
```


### [2026-09-06T15:47:50.321Z] TOOL RESULT

```
=== MON سپل/سفل ===
MON_part2.txt:787:گوش و عقب شاخةٌ صعودی فک اسفل 
MON_part2.txt:8077:پاین فقط از یکك استخوان بنام فکث اسفل 
MON_part2.txt:8106:صعودی یکی می‌شود. لقمً فک اسفل با 
MON_part2.txt:20598:درکات اسفل دوزح است و آن ر ر کتاب 
MON_part2.txt:22744:ضربه‌های وارد به ناحیةٌ زاویهٌ فک اسفل و 
MON_part2.txt:22745:تحریکك شاخه‌های عصب فک اسفل پدید 
MON_part2.txt:38801:حد فاصل بین فک بالا و فک اسفل است. 
MON_part2.txt:52793:ایجاد اش از این کیاه زند اسفل تسا 
MON_part2.txt:52794:(زند اسفل چوبی بود که در پایین چوب 
MON_part2.txt:62257:بازو با دو استخوان زند اعلی و زند اسفل 
MON_part2.txt:62304:استخوان فک اسفل با لقمه و نفرة دوری 
MON_part2.txt:62312:حرکات جلو و عقب بردن فک اسفل است. 
MON_part2.txt:64947:ملکوت اسفل (فرع. سج.) 
MON_part2.txt:73263:در انبار سپلو مانده پزند و طعم و بویی 
MON_part2.txt:85703:خارج شده و به ورید اجوف اسفل می‌ریزد. 
MON_part1.txt:12835:ج. اسافل» اسفلون» اسفلین. اسفل درجات: 
MON_part1.txt:12840:است» اسفل سافلین. 
MON_part1.txt:20589:است و به دو سیاهرگ زند اسفل و میانی 
MON_part1.txt:24127:کوچک. گروه کمتر از قبیله. اسفل بطن: 
MON_part1.txt:56911:موزه. سپل شتر. سم شترمرغ؛ ج. اخفاف» 
=== ARY som ===
219:و پوست سفید تجسم می‌کنند (5663 ,01۸-1-07؟ فعلاً برای این پرسش‌ها پاسخ قاطعی در
583:بودن واژه‌ی بازمازی شده را نشان دهند. (درکتاب حاضر نیز از این رسم پیروی شده است). . "
589:صحبت کند. واقعیت هر چه که باشد» امروزه رسم این است که واژه‌ها از دوران معاصر تا مرحله‌ی
592:در اوائل قرن سم کشف زبان‌های هند و اروپایی آسیای صفیر (به ویژه "هنیت" 17۳۳۳78 ا
917:۱-برابری و اخوت.۲- رفتار نیمه جنونآمیز و سرمستانه هنگام نبرد یا تهاجم یا مراسم وابسته به
982:بودکه می‌توان برای تراضی خدایان قربانی کرد. در زمانهای تاریخی نیز رسم قربانی کردن انسان در
983:مین هند و اروپائیان ادامه داشت. مورخان یونانی و رومی مکرراً و با اشتمثزاز به این رسم در میان
1021:اضانه‌های پونانی و رومی نشان می‌دهند که هند و اروپایی‌ها دارای گونه‌ای ازدواج و مراسم زناشویی
1026:هومر) نشان می‌دهند که رسم چند زنی نیز در میان توانگران هند و اروپایی رایج بوده است. ژول
1051:موضرع فوق را تأیید می‌کنند بلکه حاکی از آنند که شاه با سرپرستی مراسم نیایش و دار ببودن
```


## [2026-09-06T15:47:58.571Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '56900,56925p' MON_part1.txt; echo \"=== grep سپل headword ===\"; grep -n \"^سپل\\|سپل (\" MON_part1.txt MON_part2.txt | head"
}
```


## [2026-09-06T15:47:58.599Z] TOOL CALL #17: Bash

```json
{
 "command": "sed -n '1,60p' tools/ref_page.py"
}
```


### [2026-09-06T15:47:58.652Z] TOOL RESULT

```
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


### [2026-09-06T15:47:58.673Z] TOOL RESULT

```
سختران. واعظ؛ ج. خطاء (خطبا). 

خطیر: (ع.] (ص.) ارجمند؛ بزرگک 
قدره بلند مرتبه. بزرگ» مهم عظیم. 
مشکل» پرخطر. ۲ 
خف: 78۲ (.) پارةٌ کرباس و پنبه با گیاه 
خشک که بدان جرقه را از سنگ چخماق 
گیرند و آتش افروزند» آتشگیره. 

خف: 01)0*(ع.] (ص.) سبکث» خفیف. 
صف: )/۲0 [ع.] (.) کفش» بای‌افزار» 
موزه. سپل شتر. سم شترمرغ؛ ج. اخفاف» 
خفاف. 

خفاء: 0 .ف. خفا] (مصل.) بوشیده 
شدن» نهفته گشتن. (امص.) تشد کم 
نهانی» نهفتگی؛ مق. ظهور. 

خفاش: ۰55« [ع.] (.) (جاد.) پستانداری 
شهار واه عفاشان شتام:ر نگ شیبه 
موش دست و پای وی با پردة نازکی بهم 
متصل و به شکل بال است و بدان پرواز 
می‌کند. دست خفاش پنج انگشت دارد؛ 
شصت وی کوتاه است و به چنگالی نیز ختم 
می‌شود. پوزه‌ای باریکث و دو گوش برجسته 
و دندان‌های تبز دارد. چشم‌هایش صعیف 
=== grep سپل headword ===
MON_part1.txt:75328:سپل: ۲۱« [- سول - سفل - شفل] (.) 
MON_part1.txt:75332:سپلشت: 26-1650 [یبلشت» سپلشککت ]
```


## [2026-09-06T15:48:01.233Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '75320,75345p' MON_part1.txt"
}
```


### [2026-09-06T15:48:01.298Z] TOOL RESULT

```
زردند. میوه‌اش به شکل آلبالو است و از آن 
شیره‌ای لزج و بیمزه استخراج می‌کنند که در 
تداوی جهت رفع اسهال و ناراحتی‌های 
دستگاه تتفس و سرفه بکار می‌رود. ارتفاع 
آن در بعض گونه‌ها به ٩‏ متر می‌رسد» اطباء 


الکلبه» دیق» مخاطه» مخطا. 
سپل: ۲۱« [- سول - سفل - شفل] (.) 
سم شتر. ناخن فیل. 


سپلشت: 26-1650 [یبلشت» سپلشککت ] 
(امر .) (عم.) حاد ثهٌ بد. (رص.) فر ومابه» دون. 


سینج فرهنگ فارسی معین ۸۳۱ 


سنج. : [2ع-عو (.) عاریت. آرامگاه 
عاربتی» خانة موقت. سرای سپنج: ( کد.) دئبا. 
خانه‌ای که پالیز بانان و دشتانان در بالیز و 
غله‌زار از چوب و علف سازند. چراگاه 
ستوران» عدد پانزده (۳۰۵-۱۵). 
فسند آسا: ۹6020-3 (ص‌مر.) نبز» سریع. 
چست» چالاکك.
```


## [2026-09-06T15:48:10.302Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SOD hoof ===\"; grep -n -i \"hoof\" SOD.txt SOD_pages.txt | head -20; echo \"=== SOD spl ===\"; grep -n \"sp'δ\\|spδ\\|sapal\\|spr'\" SOD.txt | head -10; echo \"=== files ===\"; ls -la SOD*"
}
```


### [2026-09-06T15:48:10.380Z] TOOL RESULT

```
=== SOD hoof ===
=== SOD spl ===
16278:1315  'pspr'yc   B,  S  xJl*/  Jx£  Jy*zJl 
17707:1535  'spr'ck  =*  'sP'r'ck* 
18368:1634  'spr'ync-   S  oi^ioJ^J&vid*J'yX 
18374:1635  'spr'yncn   B  J^j^ 
58260:7515  pspr'mndyCy)   M  j^jjl  t^^  <oi-U 
66764:spr'ck* 
66789:8732  spr'cy   B  Jlj^ 
66829:8740  sf r}cy}  =»  spr'cy 
=== files ===
-rw-rw-r-- 1 sfmqrb sfmqrb 3741182 Sep  4 14:06 SOD_pages.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 1845041 Sep  4 14:06 SOD.txt
```


## [2026-09-06T15:48:15.967Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== entries 60-72 ===\"; grep -n \"^ *6[0-9]  \\|^ *7[0-2]  \" SOD.txt | head -20; echo \"=== leaf 131 (p.65) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==132' SOD_pages.txt | head -40"
}
```


### [2026-09-06T15:48:18.559Z] TOOL RESULT

```
=== entries 60-72 ===
7996:60  M8yn»(h)   M 
8003:61  *8yn»k  =»  »5'yn>k- 
8005:62  »5yn>y  =*  »5>yn.k 
8016:63  »8yny  =>  »8yn»(h) 
8018:64  »dyt   C  =>  »8yt 
8020:65  »8yt  M  t         s 
8029:66  »8yy   M  =»  »dy,  »8»kw 
8031:67  »fryn-   M  ■    <-      -r 
8039:68  "fryny  M 
8044:69  »frytyy   M  T 
8050:70  »frywn  M  - 
8058:71  »y  _»  V 
8060:72  Vrt   B  \    .  .  f  ...    . 
83750:69  VI 4;  zVJfcyy,  Gersh.  Sogd.  Cpds.  1948  p63; 
=== leaf 131 (p.65) ===
            'spwrny'kh                                                                                                              66


                  TSP 776; MDii B4R19V1; GMS 99, 151
                                                                              ast  (^styh, >styy) ^'sty3
                                                                              existence
           1659 ^pwrny'kh          M                         JLT^uT           TSP 7.120
                  (3)spurnyak ^spwny'q, 'spwrny'k
                  perfection                                             1674 'st- C                                           j*f
                  Sogdica. 2, 3; KG 610; GMS 513, 1110 <o^<7l                 ast ©pt. st. -^s-.'yt-, }stw
           1660 >spxst-       M                    o^o^                       (fo)take
                                                                              GMS 539 n 2; STi 38.6
                  (a)spaxst ©pt. st. ^'sp'ys-, 'spyst-
                  0o)serve, (to)rcspcct                                 1675 -'st                                    J^\j\ ^Ju^ x^^
                  GMS 520, 884                                               (a)st, (9)st
                                                                             elative suffix
           1661 >spymh B                     (? aJt^JL^i^ji rU)              GMS 1309
                (o)spem ? Ospynmwh, 'spymwh)
                (name of a/z)illness, tumour                            1676 'st'k S                               <£^jy ^^^ iS\x^
                TSP 7.61; -mwK TSP 2.36; Hen. Texts. 715                     astak ©pi. -t

           1662 'spymwh =» 'spymh                                             sapling, stem
                                                                              S W, KG 503 pl80
           1663 >spyn M                                      j^Lij&kf
                ospin Ospynd/t) ©pi. -d-t          =^spyn}wy, spn}k     1677 'st'nd ** >st>nt
                sinful, sinner                                          1678 >st*nk B                                ^jW(^>r^
                 GMS     112; Hen. BSOAS      11, 66; BBB f8; S W, C2        astong ?, (o)stang ?

                   p95.13                                                     (name of tfn)illness
                                                                              TSP 2.35
           1664 'spyn'nk B                                        ^7
                ospancne ? Ospnyn'k) -^spnyn'y                          1679 'st'np B                  (<r~^)^
                                                                               =>stmb
                (6>/)iron                                                    (o)stamb ©<*stamba; Parth. st}mb; MP 'stmbg
                TSP 2.850
                                                                              coarse, rough
           1665 'spynd/t         M => }spyn
           1666 'spynmwh           B =» 'spymh                                BSTBL, Dhy. 169; Benv. Notesiii 227

           1667 'spy s- B, S                    j^^o^o^                 1680 'st'npr'k     B                             ^^K^
```


## [2026-09-06T15:48:46.359Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN caper/capparis ===\"; grep -n \"capparis\\|Kajmapiq\\|kapparis\" KLN_1966.txt KLN_1971.txt | head -20; echo \"=== SKT caper ===\"; grep -n \"caper\" SKT.txt | head -10"
}
```


### [2026-09-06T15:48:46.439Z] TOOL RESULT

```
=== KLN caper/capparis ===
KLN_1971.txt:38931:ME, caperis, caper es, fr. L. capparis [whence 
KLN_1966.txt:6428:Capella,  n.,  name  of  a  star;  Alpha  in  the  Con¬ stellation  Auriga  (astron.)  —  L.,  ‘she-goat’,  di¬ min.  of  copra,  ‘she-goat’,  fern,  of  caper,  ‘goat’. See  cabriolet  and  cp.  Caprella. caper,  n.,  a  prickly  shrub  ( Capparis  spinosa).  — ME.  caperis,  caperes ,  fr.  L.  capparis  [whence also  It.  cappero  [whence  OF.  caspres,  F.  cdpre ) and  G.  Kaper],  fr.  Gk.  ximrapt c,  (whence  Arab. kabbdr,  ModPers.  kabar);  of  unknown  etymo¬ logy.  The  -s  in  ME.  was  mistaken  for  the  pi. and  was  consequently  dropped, caper,  intr.  v.,  to  dance  about,  to  prank.  — Shortened  fr.  capriole  (q.v.)
=== SKT caper ===
7374:Gambol,  a  frisk,  caper.  (F.-Ital.- Forroerly  eamhU,  gamdauU»  gambau O.V.  gamioift,  'a  gamLioll ; '  Col-  — gamiiata,  a  kick.  —  Ital.  ^mba,  the the  same  as  K.  j'amhe,  O.  V .  gatnbe,  Lat gamba,  a  joint  of  the  leg.  The  true  1 of  the  base  is  camp-  (Diez),  corrcspon to  Gieck  Kafiwff,  a  bending,  with  refer to  the  bend  of  the  leg.  Cf.  Gael,  and cam,  crooked.
8431:Have.  (E.)     M.  E.  Aamcn.  pi.  L pp.  Aad.     A.S.  AabboH,   pt   t   A. gtAa/d.  •^T)\i.  A^Mm,  led.  Aa/Of Aafva,  Dan.  Aavi,  Goth,  kabam,  O. L.  capere,  lo  seiie.     (V  KAP.) Capaoioua.
12028:Municipal.  (F.*L.)  F.  munin'pa/." L.  mMnui'pa/:!,  relating  to  a  town-ship.  —  \.. muftidpium^  a  township  which  had  the rights  of  Roman  citizenship,  whilst  retain- ing its  own  laws.  — L.  municip-,  stem  of municfps,  a  free  citizen,  one  who  under- takes duties.  —  L.  muni-f  for  munus,  obliga- tion, duty;  capere.  lo  take.     (^MU.)
17161:skittish.  (Scand.)  From  Lowl.  Scotch fkit,  to  dounce,  caper  about     This   is  a
22793:cab.  cabbage,  calf.  can.  caat.  cape,  caper, tapitalf  card,  carousal,  carp,  case,  chap, rXzr,  chase,  chink,  chop,  chuck,  cleave, <lou,  clove,  ehtb^  clutter,  cob,  cobble, cock,  cockle,  cocoa,  cod,  codling,  cog, coil,  colon,  compact,  con,  eontract,  coi>e, com,  corporal,  cotton,  count,  counterpane. €Ourt,  cow,  cowl,  crab,  crank,  crease, cricket,  croup,  crowd,  cuft  culver,  cuHHing, cxart,  cypress.
23404:Oatlic :  brosc,  capercailzie,  cateran,  dan, claymore,  tillibeg  (philibcg),  gillie,  gowan, loch,  mackintosh,  pibroch,  platd,  ptarmi- gan, reel  (a),  slogan^  spleuchan^  sporran, whiskey.
23619:Creek  from  Persian :  cinnabar  (dnoper). l^Uinfrom  Greek  from  Persian :  aspara* I,  gypsum,  laudanum,  Magi,  tiar>y f^enek  from  Latin  from  Greek  from rsian:  caper  (2),  jujube,  ma^ic,  myrtle, XwA'ue,  parria,  satsaif,  ''£*''-
```


## [2026-09-06T15:48:47.502Z] TOOL CALL #22: Bash

```json
{
 "command": "grep -rn \"VFO\" data/verification/sources/refs_online.json | head; echo \"=== VFO in book ===\"; grep -rn \"VFO\" data/extracted/ 2>/dev/null | head -5; echo \"=== bibliography ===\"; ls data/verification/sources/; "
}
```


### [2026-09-06T15:48:47.583Z] TOOL RESULT

```
=== VFO in book ===
data/extracted/batch/page-494.json:157:          "refs": "VFO:23; MON:2211",
data/extracted/batch/page-173.json:51:          "refs": "VFO:25",
data/extracted/batch/page-471.json:96:          "refs": "VFO:22; BQT:1090",
data/extracted/batch/page-44.json:94:          "refs": "VFO:15",
data/extracted/batch/page-44.json:98:          "note": "VFO claims these are cognates of English \"eagle\" and French \"aigle\" but does not provide any derivation.",
=== bibliography ===
MISSING_REFERENCES.md
refs
refs_online.json
SOURCE_MATRIX.md
web
```


## [2026-09-06T15:48:58.539Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && grep -n \"VFO\\|KGW\" MISSING_REFERENCES.md | head -20; echo \"=== SKT leaf 95 (p.75) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==96' refs/SKT.txt | grep -n -i \"caper\" "
}
```


### [2026-09-06T15:49:01.330Z] TOOL RESULT

```
17:| PREVIEW only | ISS (CUP 2009 reprint), KGW |
96:### 19. KGW — Ibrahim, Kulturgeschichtliche Wortforschung (1991) — PREVIEW
110:| VFO | (unresolved abbreviation, probably = VOP) | skipped | — |
136:- Buy: MON 6-vol print set (needed for vols 5-6 اعلام and the Latin etyma), SAP on Fidibo (ebook), PLA/KGW from Harrassowitz, ISS from Cambridge, and the Persian print titles ETM, AEF (2015 ed.), ZMA, DZA, AKM, FNI, IRT.
=== SKT leaf 95 (p.75) ===
```


## [2026-09-06T15:49:04.135Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 94 95 96 97 98; do echo \"--- leaf $n ---\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N' SKT.txt | grep -i -o \".\\{0,300\\}Caper.\\{0,300\\}\" | head -3; done"
}
```


### [2026-09-06T15:49:19.513Z] TOOL RESULT

```
--- leaf 94 ---
ugrep: error: error at position 84
xbf][\x80-\xbf]*){0,300}
                        \___exceeds complexity limits


--- leaf 95 ---
ugrep: error: error at position 84
xbf][\x80-\xbf]*){0,300}
                        \___exceeds complexity limits


--- leaf 96 ---
ugrep: error: error at position 84
xbf][\x80-\xbf]*){0,300}
                        \___exceeds complexity limits


--- leaf 97 ---
ugrep: error: error at position 84
xbf][\x80-\xbf]*){0,300}
                        \___exceeds complexity limits


--- leaf 98 ---
ugrep: error: error at position 84
xbf][\x80-\xbf]*){0,300}
                        \___exceeds complexity limits
```


## [2026-09-06T15:49:22.492Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nimport re\nt=open('SKT.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor n in range(92,100):\n    p=t[n]\n    for m in re.finditer('[Cc]aper',p):\n        print(n, repr(p[max(0,m.start()-200):m.start()+300]))\n    print('---',n,'len',len(p))\n\" 2>&1 | head -40"
}
```


### [2026-09-06T15:49:24.119Z] TOOL RESULT

```
--- 92 len 4427
--- 93 len 3799
--- 94 len 4449
--- 95 len 3561
--- 96 len 34
--- 97 len 3892
--- 98 len 4191
--- 99 len 4177
```


## [2026-09-06T15:49:27.374Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nimport re\nt=open('SKT.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor n,p in enumerate(t):\n    if re.search(r'Caper',p) and n<200:\n        print('LEAF',n)\n        for m in re.finditer('Caper',p):\n            print(repr(p[max(0,m.start()-100):m.start()+400]))\n        print()\n\" 2>&1 | head -40"
}
```


### [2026-09-06T15:49:29.283Z] TOOL RESULT

```
LEAF 79
"-honse.  (£.)  A  Nortbetn derivative  of  bower ;  tee  p.  46,  coL  I,  L  u\nc.\nCab  (i) ;  see  Caper  (i).\nCab  (3^.  a  Heb.  measure.  (Heb.)  Heb. ^ab,  the  JSlh  part  of  an  ephah.  ITie  literal sense  is  'hollow ;'  cf.  Heb.  qtibab^  to  form in  the  shajie  of  a  vault ;  see  Aloove.\nCabal.  (F.- Heb.)  Orig.  '  a  secret.*  F. (obaie,  'the  Jcwes  Caball,  a  hidden  science;* Cot.  —  Ucb.  qabbMiih,  reception,  mysterious doctrine.  — Heb.  qdbalf  to  receive;  gibbei"

LEAF 88
"rom It:il.  caprUf  a  she-goat;  so  that  capHcci4f might  mean  a  friiik  like  a  goat's:  sec Caper  (i).  ^  Or  capri€cto^capo-ncc%o,  a bri&tling  of  the  hair;  from  cafQ,  bead, riccio,  n  bristling.\nCapricorn,  Capriole  ;  see  Oaper  (i).\nCapsize,  to upsa  (.Spftn.?-L.)  Peiti.ips from  Span,  caputar,  to  &ink  (a  ship)  by the  bead ;  allied  to  cabutar^  to  nod  the head,  pitch  as  a  ship  does.  — Span.  cab<ia, the  head,  fore  port  of  a  ship;  a  derivative of"
```


## [2026-09-06T15:49:35.950Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nimport re\nt=open('SKT.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor n,p in enumerate(t):\n    if re.search(r'capparis|Kajnrapi|xannapi',p,re.I):\n        print('LEAF',n, repr(p[:60]))\n        for m in re.finditer('capparis',p,re.I):\n            print(repr(p[max(0,m.start()-350):m.start()+250]))\n        print()\n\" 2>&1 | head -30"
}
```


### [2026-09-06T15:49:37.608Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T15:49:40.015Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nimport re\nt=open('SKT.txt',encoding='utf-8',errors='replace').read().split('\\f')\np=t[88]\ni=p.find('Caper')\nprint(p[:2500])\n\""
}
```


### [2026-09-06T15:49:41.729Z] TOOL RESULT

```
)     F,  eaf-
l«>L.  tmp^i.  t>jIL  head. MpttoL  '     of  Jupiter,
Aooc.   L-i  .   —  L.  <apit.,
b  etf  tajfSLi,  X  o^aU ,  Lui  ihe  reuon  for ttmc  ti  otecore ;  see  Smith.  Class.  Diet. ■pttular,  reiftticg  to  x  chapter.  i^L.) 9  L.  cM/ituia*it,  adj.  of  ca/fifaium,  a bpljO  of  m  dlhcUfsJ,  or  a  chapter  of  ft K ;  Me  ciMptor  bdow. HpltllMa.  (L.)  Low  L.  eapitulatm, fd  tm/itmSmrt,  to  divide  into  cbapten, \  lo  ffotwe  lams,  (for  santnder).  * k»  L  e»fttmlmm,  %.  chapter :  cce  chapter Dttr.  rt<apiiulati,
(F.-L.)     M.  E.  (apitain.-^
I.  «•  Low  L  ta^itantus,  <apit-
■  NBOB  oi  MlcUcn.  -  L  rV^>  stem
CAR.
57
.-^
<F.— L.)    M.  R  flitt/jpfopcrtjr ; live  itock,  cftttJe.  -  O.  F.  ctUtl.  - L.  tMpiutU,  capital,   property;    ace Ul  (a)  above.
hapiter,  the  capital  of  a  colamn.  (F. )     O.  F.  tkafittt  (F.  tkapiuau)^  the «>L>  tafittili^mt  the  same ;  dimm.  of ■  hettd V    .  ■  diTttiod  of  ft  book,  s^-nod  of -  L>      M.  E.  tkafitre,   ftUo "^' '•■■-•]»  of  ail  older X  chapter  of (ttUlt  hr»'  .  ^   ^1  Ute  L.,  a
Dd  ;  dlMio.  ofnfmt,  •  licaM.
b.  (F.oL)    PI.  of  M.  £.  cka4f/, |Crty,  aW  callIe,-0.  F.  Ma/W»O.K. f,  pcoficny :  ice  oatiU  above. hfpf      '•    =  '   )     ME.  fAr/,  eAirf.  - p.  r  hcad.xL.  ca/Mt,  head.
•ow  L.  taf^tamau,  tapiUnuit  ft  cftpiain  ; captain  ab^^ti.
orporal  (t),  a  subordiDate  officer. ^U&L'L.)  A  comipt  farm  ofF.  ra- l/.  «•  llat  aitJ^flntJV,  a  Lhicf,  corporal  of .-I^i!  .'j.'»\  licjd.  — L.  «/i»y.
:  rora  pp.   of  I-ow "i^  t£tt  olT;   and
sua  iA  <^v^«  ^<^^'-
antcheon  of  a  deceased F.*L)    Comiptioo  of  orA'wi^vf/, iagm  of  ^ikitpfmtMl.
(L)     L  xii/tti,  bade  of  Uie >  <W(  «ii)|  over  againat;  and
(^.•LO    OV.^rtcifut.^
L.  fradpitium,  a  falling  headlong  down  : a  precipice  — L./rffri/;Vi-,  crude  form  of prxeeps,  headlong.-* L.  pra,  before;  and capitt;  cr.  form  o\  caput,  Der.  prtcipiisit^ from  L.  pracipitare,  to  cast  beadlanjr.
Binciput.  (L.)  The  fore  part  of  the head;  liL  'half  head.'»L.  Jr»ri/u/,  half the  head— L- «»«,  half;  msx^  caput  \  see al.so  Capsiae.
Capitation,  Capitx>l,  Capitular^ CapitiUate;  see  above.
Capon.  (L.  —  Gk.)  A.  5.  capun.  »  L. ace  captntem,  from  nom.  capo.^Gk.  k6wv¥, a  capon.     (VSKAP.)
Caprice.  (F.-Iial.-L.?)  F.  «/rw». ^\iA\.  capricdo,  a  whim.  Perhaps  from It:il.  caprUf  a  she-goat;  s
```


## [2026-09-06T15:49:52.422Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '23605,23640p' SKT.txt"
}
```


### [2026-09-06T15:49:52.467Z] TOOL RESULT

```
French  from   OertnaM  from   Servian:
vampire-
Jiussian  :  drosky,  morse,  rouble  (ruble), stcin>e,  verst.
French  from  ICiiSsian :  ukase.
13.  A  word  of  LITHUANIAN  origin.  Curiously  enough,  there  Is  only  om Iglilh  word  which  can  be  traced  to  Lithuanian,  and  the  mtroductton  of  it  into fUsh  is  due  to  the  fact  that  it  had  been  borrowed  from  that  laagoage  by  the  Danes, '  it  talk.
French  from  Ifalian  from  Latin  from Greek  from  O.  Persian :  rice.
Spanish  from  Latin  from  Greek  from  ^ Persian:  pistachio  (pistacho).
Frc$ick    from     Lai  in    from    Pcrsianil peach  (0.
French  from  Low  Latin  from  Persian  \ zcdoary.
Jtalian  from  f^rsian :  sciaietar  (< icr)  ?.
14.  Words  of  PERSIAN  origin.
flertiani  bang  (t),  barbican?,  bashitw, LT,  caravan,  caravansary',  dervia  (der- bi.  divan,  durbar,  6rman,  ghoul,  bonri, leal,  jasmine  ijetsambe),  Lascar,  mohur,
b^hau,   I'artce,    pasha    (^lacha,    pashaw, saw),  peri,  »aih  Ca)>  Kpoy,  ibab,  shawl,
fftrntrntani  from    Persian-.    lamindar,
Creek  from  Persian :  cinnabar  (dnoper). l^Uinfrom  Greek  from  Persian :  aspara* I,  gypsum,  laudanum,  Magi,  tiar>y f^enek  from  Latin  from  Greek  from rsian:  caper  (2),  jujube,  ma^ic,  myrtle, XwA'ue,  parria,  satsaif,  ''£*''-
Freneh  from  Italian  from  Persian:  car- case (^carcass),  jargonelle,  mommy,  orange« rebeck,  taffeta  (u(^tV^^.
French    from    S;«nuK    from    P«r»a» ]ulep,  (arabanA.
VI.     DISTRIBUTION   OF  WORDS,   ETC.
1
I
Portuguese  from  Persian :  pagoda,  v»- rnnHa  (verandah")?.
French  from  Portuptese  from  Persian  : be?  Oft  r.
French  from  Persian:  check,  chcckci (chequer),  checkers  (chequers),  che^s  ex- chequer, jar  (a),  lemoo,  lime  (3),  ounce (2)  ?,  rook  {%\  scarlet.
Dutch  from  Persian :  gherkin.
15.  Word*  of  SANSKRIT  origin.
Sanskrit',  avatar,  banyan,  brahmin  (brah- man), champak,  pundit,  lajnb,  Sanskrit^ nittec,  Veda.
I^tin  from  Greek  from  Sanskrit :  hemp, pepper,
French  from  iMtn  from  Greek  from Sanskrit;  beryl,  briUioiit,  ginger,  mace (a),  saccharine.
Fretuh  from  Latin  from  Greek  from Persian  from  Satukrit:  naid.
French  from  Spanish  from  Latin  from Greek  from  Persian  from  Sanskrit :  in- digo.
French  from  Latin  from  Persian  from Sanskrit:   musk.
Lorn  Latin  from  Arabic  fr^A borax.
Frettek  from  S/anish  from Persian:    hatard.    tahour    (tal hour?,  tambourine?.     FerkaPi
Spanish  from    TurkUk  frot lilac.
French   from    Arakir  from atmc
French  from  ftaiian  from  Latin  from
```


## [2026-09-06T15:50:04.756Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('SKT.txt',encoding='utf-8',errors='replace').read().split('\\f')\nimport re\nfor n in (86,87):\n    p=t[n]\n    print('===LEAF',n)\n    print(p[:3000])\n\""
}
```


### [2026-09-06T15:50:07.302Z] TOOL RESULT

```
===LEAF 86
uffix  -mrnt-
cash,  coin  fF-LJ  Or'i' to  keep  money  m.»F.  na caae<a)n^  -  -     '^'*'"     "  '■  ' keeps  a  tD
otaket
iTMB    F.   A/^tM^    '*
TAPACJOUS. £K/xr.  a  fBuc,  box ;  lee  0M«
Bl  CW.^l*)  FicaM  fvAUr,  ranwt *,  rinrt'rr,  to  hant.  dlifie:  Ke-.  ce  to tl   afiMm   t«  It«!    r^^rtaT,  Low
■Vinn
or
.   .i.  Oa.
i  flora   Picafd
r^  to  bmj  provisions.  (F.  —  L.) M  a  vftfb  ax>m  M.  £.  taiour,  a. C  imnHOttft  (vfaom  we  &hoold  oow lift-^rV  Ca<WBr  u  tbort  for  ar0/««r^ EroHi  AAtfr,  a  bttymg.  purdusc,  Cb. r^.O.  F  a^«/  (mod.  F.  o^^j/).  ■ *  Low  L.  ^-aptum,  %  purcbase jt  fo«  arra//ttM.«*Low  L. ':^mc(a.d.  tooo),  frequent. 10  (cocirc^  also  to  bnj ;   «ee
CAPACTOUS.
65
1S^
MX  tokunlafta.  (F.-U^  OF. tKs~<r^  to  p«noe;  tec  oatoh  &t>oTe. ♦  (3).  tomckasc;  short  ioxeruhax*,
10  (j;,  ■  priater'ft  frame.  (F.— L.>
«,  a  ikriiLC. « X*  at/f«,  a  box ;  see
^abofc
Ait.  (F.-l.)  M.  E.  emreii.^O.f.
I^L  of  £ii«i-<Ytf<>,  to  cuoccirc;  tee
iCi  ■  *    )      M.  E-  fprt,(-ti(H  —
«*  .;/>.  •  L-  iffnril^rt^  to
t-^i-  L4n'  ('(MW,  (ogcUicr);  and eoholiL
WpCiflO.  (F.-I.)   ^.tmetpticn.'^
t0me€f4**^*^^  »  L  itm£tptu$^  pp.  of
«  .  ».ci-  ala»v«.     Dor.  prt'^wuJfticH.
—  L)    OF.   ^frtv/^,  Jii-/-
/,  to  talte  m^txy,  deceive.  —
E;.  anil  ris/kT'T,  to  tAke.  Dor, O.  F.  ArW>,  pp.  of  Jfrfvtr. n.  (F.-L)  O.K.  Jt<ef{iM. ft,  AB^^n^Mm.  •  L.  ift^t/.'us,  pp.  of Itedecdvc;  see  deceive. H  (F.-I.)  O.  F.  tmauttr,  'to Kccwt'  Cot.-F.M,  in  (L.  iW): Kcafitr, f«iiif, a  ca4e ;  tee oaaa  (a)
L.)   O  F.  mihassfr,  'lo g^,'   Cot.      tlrnce  to
ll  .Ml  -:-,,(     .   /    ...   -       (I. A
la)t«.«*I«  /ar,  out;  (Jftre,  Co
I     izapcrcseptible.    (F.— 1«)     rrun  i*.
-  j«.  fiol ;  And  /<trrffi/i&/e ;  »cc  hclow I      ixxoeptive.  (L.)    Coined  from  L  imy/- /Ju.  pp.  of  tjuifrrf^  to  begia :  see  below. I      incipient  iL.)    L.  ittdfimt-,  item  of pr«.    pt   of  ifc.'t/rrt,    to   bcgio.  ••  L.   cm, upon :  Ai/r/r.  to  lay"  bold  oC
InUroept.  (F  -U)  F.  imUrctpUr.^ I*  ifUerttptuj,  pp.  of  imttrdftn,  lit  lo catch  between.— L.  r>/rr,  bclweco;  iafiert, to  take.
occupy.  (F.-L.)  M.  £.  occmfim.  F. M-rafAer.— L.  tfcnr/tfrr.  to  lay  bold  of.—  L. fr-  (  — ^.  Bcar);  tafert.  to  seiie.  Cer. prt-0C€^py.
perceive.  (F.  -  L.^  O.  F.  ferttvtr.  -  L- ptrcip^n,  lo  apprebeod.  —  L. /rr,  tboioogh* Ij  ;  captrtt  to  sciie.
perception.  (K.-L.)  V.perrtpHffH.m.'L. ace  ftrttptiomm,  —  L.  ptrttptau^  pp.  of pirriftrt ;  »ee  above.
prooept.  (F.-L.)  O  ¥.  prtcrpte.'^'U /ntiffifum,  a  prescn bed  rule.  —  L..prtectpfHtt pp.  of  praci/rre.  to  take  beforehand,  |^ve rules.— L«  /rt«,  before;  captrt,  to  tahr* Der.  pnapt-ar.
purohaae.  verb.  (F.-L.)  M.  E.  par^ cMtutH,  put-ckattK,  —  O.  F.  purtkMtr,
===LEAF 87
  lo pursue  eagerly,  acquire,  gee.  — O  F.  pur (F./wir),  £rom  l^  ptv ;  and  O.  F.  chactr, see  chase  (i)  above.
receive.  (F.-L.)  O.  F,  rtctvtr,  rt- cevoir.  —  L.  ruipere,  to  take  back.  —  L,  n, back  ;   ca/^rf^  to  Uke-
receptocle.  (F.-L.)  F.  rktptmiU.mm L.  rtfcftatulum,^  place  to  ftore  away.— L.  ttxfpi  us,  pp  of  rraptrt',  see  above
reception.  (F.-L.)  F.  n^^M.-!. ace  rtttpthntm,  a  taking  back.  — L.  rw^^ «f ;  as  atiore.
recipe.  (L  )  L.  rrrr^V,  take  tboa ;  imp. of  Ttcipert ;  sec  receive.
recipient.  (U)  L.  ruipient-,  stem  of prcs.  pt  oireciperti  see  receive.
■aah  (1).  a  case  or  Irame  for  panes  of gla**.  (F.-L)  Coiniptionof  F.  Mojiw.  •» fmme  of  wood  for  a  window ; '  Cot.— O.  F. (htutt  (F.  cMdsse),  a  case,  shrine.  —  L. eapsa,  a  cue.  See  ohaaa  (3)  and  oaae  (3) above.
scaffold.   (F -U  anJ  Tcul.)     M.  E. ]  ,i',i  Y    —  O.  F.  /<  1  1  •  •    f*v\y   found    as /.',    moi\.    1  .    a    scaffold.
.\it  tuaMifa.:  xorrcspoodiog
lo  bj«an.  and  Il.il  ctii-jjutio,  a  luneral canopy,  also  a  ttace.  scalToId.  ^  The former  part  of  lb«  word  occu'  %.
65
CAPAAI50!C
CAPrTAU
-Sp-D.
&n^  FM.  i^K  iBiL  aMc  A.S
«nf  .  a  case :  see  ahWL
oapuiMa,  tenpins*  of  a  hoK  (T.- Spaa..Lo«l.)    OiF.d AiS^tanBaS  cowET  far  a ti^  fioa  SpaL  ^'tf^  ' La«I-.^^  a  cape:  mt
]M.*Lo«  U>  r.  4^MML-.fiaL  affm- *am,  a  r»nT1  booi^  knee  a  huuA.^  nr: olBiK,  oc  twffmat^  a  oow.^kaL  twffB^ mope;  we  Caapa  (iV
ohapeL  (F.i-U)  arrA^^Mfe.-Lov L.  mfriim^  orig.  a  ifaisc  ii  viack  waa  pre- •fffvcd  dbe  13^  or  cope  of  Sl  Martsa (»«taV  -  Low  U  t^m.  mffm.  of^ MOoed  cloak:  ai above.
(F.-L.)  F.  riiti^Fva,  a prortcdor;  orie-  a  kind  of  bood.  — F.c^^ a  eoMLw  Low  L.  mAs  :  as  abore.
•Mplot.  (F.«L)  U.  EL  €kmfekt.^ O.  y.  «I«/Mrf.  a  bead^bcK.  «rcatJi.-.O.F. «U/tr/,  Keatl'dreia.  »  O.  F.  cMmfe,  a  cope ; Mvohapenm.
«Op«  (If,  a  hood,  cape.  (F.-LowL.) M4  E.  /jr/V.  varioitt  of  rd/v.  a  ope ;  see Oapa  ■bore.     (For  the  «.  cf  Icel.  Jt,i/>a.)
oaOApo.  (F.  *L.)  M.  E.  esca/^n  - C).  I',  tuafer  (K.  ^chaffer),  to  escape,  lit. Ui  slip  out  of  one'i  cajjc.  »  L.  «x  ra//a»  oat <tf  one'*  ctjic:  trc  Capo  (t)  above.
•CMpe;  ktiOrl  Utt  /xi-tf/V  (ftUive).
OAX>a  (j),  twratllan')  j  we  Capital. Oftpor(i).  to  <laric<  about.  (llal.-L.) iriy  eapt^aU  iSir  P.  Sidney V  —  Ilal. 'm,  to  4kip  as  a  i^at.  — IlnJ.  nx* '  ii.i  'iirtiin.  of<^j//w,  wild  goat; •aLwita  fd/m,  abe-goat ;
uabilulot    (F.-ltal.-X^)    Co^
■    IIIIMMI    flill    «C
(F.^ftaL-L.)     r.
ItaL  A^rM^  IfK  lap  oira  kai
(J),  (fce  flowrtod  «l  a
fiML  (T.-x   ck-Pai.>  ar
iF.  <^^\-U  taffmirix.  -  Gk. te  6a9t  ^Pcn.
(GoA)    Ba«t*i eat  code  «r;ka« BL  booeof  lke«oodr-«God.  «yaifl;«1 C«e  €aa««Har) ;  4aaa;«MUC  »ood. flajiltoty,  Oe  hav.  (L.)   L. «4.frasoi^iX6B.hHK.
```


## [2026-09-06T15:50:21.012Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AFM كبر ===\"; grep -n \"الكبر\\|كبر )\\|( كبر\" AFM_pages.txt | head -10; echo \"=== AFM page 131 ===\"; grep -n \"\\[pdf page 1[34][0-9]\\]\" AFM_pages.txt | head -20"
}
```


### [2026-09-06T15:50:21.096Z] TOOL RESULT

```
=== AFM كبر ===
3546:شجر الفستق يشتعل بالنار مثل الكبريت ولهذا قيل له سيّد الكباريت ٠‏ وقيل يأبع
=== AFM page 131 ===
```


## [2026-09-06T15:50:22.722Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== LKT kapper ===\"; grep -n -i \"kapper\\|kappar\\|Kaper\" LKT.txt | head -10; echo \"=== KLN chebule/Kabul ===\"; grep -n -i \"chebul\\|Kabul\" KLN_1966.txt KLN_1971.txt HJB.txt | head -20"
}
```


### [2026-09-06T15:50:22.800Z] TOOL RESULT

```
=== LKT kapper ===
620:Eine  Pflanze,  die  verschieden  bestimmt wird,  wahrscheinlich  Centaurea  beben, aber  ar.  bahman  'eine  Art  Rettich". Hieraus  frz.  hiJien,  sp.  behen,  dtsch. Behenuurzel;  die  Wurzel  wird  in  der Arzneikunde  benutzt.  —  Das  sog.  Behen- öl  wird  dagegen  durch  Pressen  der  Be- hennüsse  gewonnen,  d.  h.  aus  den  Sa- men der  Pflanzen  Moringa  oleifera  Lani. und  M.  aptera  Gaertn.,  die  wie  die  be- kanntere unsere  Kapern  [s.  hier  Nr.  978] liefernde  Capparis  der  Familie  der  Cap- paridaceen  (unseren  Cruciferen  verwandt) angehören.    [Devic  DEt  63/C4.
2337:'Kapern',  die  jungen  Blütenknospen  von Capparis  spinosa  [aus  gr.  Kdu-rrapiq],  Ein- heitsnomen kabbära;  hieraus  mit  ar. Art.  sp.  pg.  alcaparra,  it.  caparra.  Die übrigen  Formen  kommen  dagegen  un- mittelbar über  lat.  capimris  üus  dem  gr. Grundwort:  it.  cappari,  frz.  cctpi-es;  engl. capers,  dtsch.  Kapern,  Kappern;  russ. kapersy,  bulg.  kapari,  serb.  kapre,  ka- jjra,  ßech.  kapary,  kapa^-ky,  poln.  ka- pary,  kaparki  [vgl.  ngr.  Kuircipf)].
=== KLN chebule/Kabul ===
HJB.txt:1608:c.  1680.— "One  of  these  (fowls)  is  the ding,  which  is  a  large  bird.  Each  of  its wings  is  the  length  of  a  man;  on  its  head and  neck  there  is  no  hair.  Something  like a  bag  hangs  from  its  neck ;  its  back  is  black, its  breast  white  ;  it  frequentlv  visits  Kabul. One  year  they  caught  and  brought  me  a ding,  which  became  very  tame.  The  flesh which  they  threw  it,  it  never  failed  to  catch in  its  beak,  and  swallowed  without  ceremony. On  one  occasion  it  swallowed  a  shoe  well  shod with  iron  ;  on  another  occasion  it  swallowed a  good-sized  fowl  right  down,  with  its  wings and  feathers."— JBo&T,  821.
HJB.txt:1869:t.c.  the  Caliph,  downwards.  The  word ill  this  form  perhaps  first  became familiar  as  appued  to  the  Princes  of Sind,  at  the  tmie  of  the  conquest  of that  Province  by  Sir  C.  J.  Napier. It  is  the  title  affected  by  many  Musul- '  man  sovereigns  of  various  calibres,  as  the Amir  of  Kabul,  the  Amir  of  Bokhara, &c.  But  in  sundry  other  forms  the word  has,  more  or  less,  taken  root  in European  languages  since  the  early Middle  A^es.  Thus  it  is  the  origin of  the  title  *  Admiral,'  now  confined to  ^nerals  of  the  sea  service,  but applied  in  varying  forms  by  medieval Christian  writers  to  the  Amirs,  or lords,  of  the  court  and  army  of  Ec^t and  other  Mohammedan  States.  The word  also  came  to  us  a^in,  by  a  later importation  from  the  Levant,  in  the French  form,  Emir  or  Emer. — See also  Omrah,  which  is  in  fact  Umardy the  pL  of  Amir,  Byzantine  writers  use ^AfUpf  *Afi,rjpas,  *Afxvpdsj  'AfirfpaTos,  &c. (See  DtLcange^  Gloss,  GracU.)  It  is the  opinion  of  the  best  scholars  that the  forms  AmdrfU^  AmmiraqliOy  Admiral &c.,  originated  in  the  application  of  a Low  Latin  termination  -alis  or  -o/tiw, though  some  doubt  may  still  attach to  this  question.  (See  Marcel  Devic, 8.V.  AmxroL,  and  Dozy,  Oosterlingen, av.  Admiraal  [and  N,E.D,  s.v.  Ad- miral^. The  a  in  admiral  probably came  from  a  false  imagination  of  con- nection with  admirari.
HJB.txt:4249:1838.—"  Only  eight  or  ten  loads  (of  coffee) were  imported  this  year,  including  two  loads of  *Kopes*  (see  COPECK),  the  copper  cur- rency of  Russia,  known  in  this  country  by the  name  of  Bnghmkcha.  They  are converted  to  the  same  uses  as  copper." — Report  from  Kabul,  by  A,  Bwmes;  in  Punjab Trade  Report,  App.  p.  iii.
HJB.txt:4656:OABUL,  OAUBOOL,  &c.,  n.i>. This  name  (Kabul)  of  the  chief  city of  N.  Afghanistan,  now  so  familiar, is  perhaps  traceable  in  Ptolemy,  wh(» gives  in  that  same  region  a  people called  Ka/SoXirat,  and  a  city  called Kdfiovpa,  Perhaps,  however,  one  or both  may  be  corrol>orated  by  the ydpSos  KafiaXiTTi  of  the   Perij)lu3.     The
HJB.txt:4660:accent  of  Kabul  ia  moflt  distinctly  on the  first  and  long  syllable,  but  English mouths  are  very  perverse  in  error here.    Moore  accents  the  last  syllable  :
HJB.txt:5839:CHEBULI.  The  denomination  of one  of  the  kinds  of  Myrobolaiui  (q.v.) exported  from  India.  The  true  ety- moloffy  is  probably  Kdbull,  as  stated by  Tnevenot,  i.e,  *  from  (Uabul.*
HJB.txt:7069:The  second  portion  of  the  word, ivdld,  is  properly  a  Hindi  adjectival affix,  correspondmg  in  a  general  way to  the  Latin  -arius.  Its  usual  employ- ipent  as  affix  to  a  suljstantive  makes  it frequently  denote  "  agent,  doer,  keeper, man,  inhabitant,  master,  lord,  possessor, owner,"  as  Shakespear  vaiulv  tries  to- define  it,  and  as  in  Anglo-Indian  usage is  popularly  assumed  to  be  its  meaning. But  this  kind  of  denotation  is  inci- dental ;  there  is  no  real  limitation  to such  meaning.  This  is  demonstrable from  such  phrases  as  Kdbul-wdld  ghordy *the  Kabulian  horse/  and  from  the common  form  of  village  nomenclature in  the  Panjab,  e.g,  Mlr-Khdn-wdldy Ganda-Singh-wdld,  and  so  forth,  imply- ing the  village  established  by  Mir- Knan  or  Ganda-Singh.  In  the  three immediately  following  quotations,  the second  and  third  exhibit  a  strictly idiomatic  use  of  wdld,  the  first  an incorrect  English  use  of  it.
HJB.txt:8234:DAOCA,  n.p.  Properly  Dhdkd, [Hhe  wood  of  dkdk  (see  DHAWK)  trees' ; the  Imp.  Gaz.  suggests  Dhakeswari, '  the concealed  goddess  '1  A  city  in  the  east of  Bengal,  once  of  great  importance, especially  in  the  later  Mahommedan history  ;  famous  also  for  the  ^^  Dacca muslins "  woven  there,  the  annual  ad- vances for  which,  prior  to  1801,  are said  to  have  amounted  to  ;f250,000. ~ Taylor y  Descr.  and  Hist.  Account  of  the Mion  Manufacture  of  Dacca  in  BengaX\. Daka  is  throughout  Central  Asia  ap- plied to  all  miislins  imported  through Kabul.
HJB.txt:9102:[1858.— '*  The  whole  Afghan  army  oon- tists  of  the  three  diyinons  ot  Kabul,  Eanda- ha^and  Herat ;  of  these,  the  troops  called Denarii  (which  receive  pay),  present  the following  effective  force.  "—/Vrrwr,  H.qftke A/gkant,  315  seq.]
HJB.txt:10062:QHILZAI,  n.p.  One  of  the  most famous  of  the  tribes  of  Afghanistan, and  probably  the  strongest,  occupying the  high  plateau  north  of  Kandahar, and  extending  (roundly  speaking) eastward  to  the  Sulimani  mountains, and  north  to  the  Kabul  River.  They were  supreme  in  Afghanistan  at  the be^nning  of  the  18ih  century,  and  for a  time  possessed  the  throne  of  Ispahan. The  following  paragrai>h  occurs  in  the article  Afghanistan,  in  the  9th  ed. of  the  Encyc.  Britan.,  1874  (L  235), written  by  one  of  the  authors  of  this book: —
HJB.txt:11085:HINDOO  K008H,  n.p.  Hindu- Kuek;  a  term  applied  by  our  geo- graphers to  the  whole  of  the  Alpine range  which  separates  the  basins  of the  Kabul  River  and  the  Helmand from  that  of  the  Ozus.  It  is,  as Rennell  points  out,  properly  that  part of  the  range  immediately  north  of Kabul,  the  Garuxuue  of  the  historians of  Alexander,  who  crossed  and  re- crossed  it  somewhere  not  far  from  the
HJB.txt:11091:1504.— "The  ooimtry  of  E&bul  is  very strong,  and  of  difficult  access.  .  .  .  Between Balkh,  Eundez,  and  Badaksh&n  on  the  one side,  and  KAbul  on  the  other,  is  interposed the  mountain  of  Hindti-kABh,  the  passes over  which  are  seven  in  number." — Baher^ p.  139.
HJB.txt:11441:c.  1505.— Kabul  "on  the  west  has  the mountain  districts,  in  which  are  situated KamM  and  GhCir.  This  mountainous  tract is  at  present  occupied  and  inhabited  by  the HaiAxa  and  Nukderi  tribes."— JSoder,  p.  136.
HJB.txt:12476:1505.— "The  greatest  of  the  Begs  of  the Sagharichi  was  then  Shir  Haji  Beg,  whose daughter,  Ais-doulet  Begwm,  Yunls  Khan married.  .  .  .  The  Khan  had  three  daughters by  Ais-doulet  Begum.  .  .  .  The  second daughter,  Kulliik  Nigar  TniAjium  was  my mother.  .  .  .  Five  months  after  the  taking of  Kabul  she  departed  to  God's  mercy,  in the  year  911 "  {1^6).— Sober,  p.  12.
HJB.txt:12845:class  is  also  settled  extensively  over Afghanistan.  ["At  Kabul,"  writes BeUew  (Bacea  of  AfgJumidany  107), "he  (Naoiir)  left  as  chandavJy  or  *rear ffuard,'  a  detachment  of  12,000  of  his Kizilbash  (so  named  from  the  red  caps they  wore),  or  Mughal  Persian  troops. After  the  death  of  Nadir  they  remained at  Kabul  as  a  military  colony,  and  their descendants  occupy  a  distinct  quarter of  the  city,  which  is  called  Ghandaul, These  Kizilbaah  hold  their  own  ground here,  as  a  distinct  Persian  community of  the  Shia  persuasion,  against  the native  population  of  the  Sunni  pro- fession- They  constitute  an  important element  in  the  general  population  of the  city,  and  exercise  a  considerable influence  in  its  local  politics.  Owin^  to their  isolated  position  and  antagonism to  the  native  population,  they  are favourably  inclmed  to  the  British authority."]  Manv  of  them  used  to take  service  with  the  Delhi  emperors  ; and  not  a  few  do  so  now  in  our  frontier cavalry  regiments.
HJB.txt:14582:[1842. — See  the  classical  account  of  the Moollahs  of  Kabul  in  Mphinstone't  Caubul, ed.  1842,  i.  281  seqq.]
HJB.txt:15058:c.  1590.— **  Here  (in  Tooman  Bekhrad,  n. of  Kabul  R.)  are  also  mice  that  have  a  fine moskyioe&t."— ^yeen,  bv  Gladwin  (1800) ii.  166 ;  [ed.  JarreU,  ii.  406].
HJB.txt:15270:(3)  The  Chdmlie  Myrobalan;  the fruit  of  Terminalia  dnebula,  Roxb. The  derivation  of  this  name  which  we have  given  under  GHEBUIJ  is  con- firmed by  the  Persian  name,  which  is HalUa'i-Kdbull.  It  can  hardly  have been  a  product  of  Kabul,  but  may have  been  imported  into  Persia  by that  route,  whence  the  name,  as calicoes  got  their  name  from  CalicuU Garcia  says  these  myrobalans  were called  by  his  Arabs  mubtUgi,  Ibn Baithar  calls  them  haluaj,  and  many of  the  authorities  whom  he  quotes specify  them  as  KdbtUu
HJB.txt:15467:1838.— * '  Nanka  is  imported  in  the  greatest quantity  (to  Kabul)  from  Russia,  and  is used  for  making  the  outer  garments  for  the people,  who  have  a  great  liking  to  it.  It IS  similar  to  nankeen  cloth  that  comes  to India  from  China,  and  is  of  a  strong  durable texture." — Report  by  Baines,  in  Pufijah Trade  Report,  App.  p.  iz.    See  also  p.  oUvii.
HJB.txt:17211:PESHAWUB,  n.p.  Peshdwar, This  name  of  what  is  now  the  frontier city  and  garrison  of  India  towards Kabul,  is  sometimes  alleged  to  have been  given  by  Akbar.  But  in  sub- stance the  name  is  of  great  antiquity, and  all  that  can  be  alleged  as  to  Akbar is  that  he  is  said  to  have  modified  the old  name,  and  that  since  his  time  the present  form  has  been  in  use.  A notice  of  the  change  is  quoted  below from  Gen.  Cunningham ;  we  cannot give  the  authority  on  which  the  state- ment rests.  Peshawar  could  hardly  be called  a  frontier  town  in  the  time  of Akbar,  standing  as  it  did  according  to the  administrative  division  of  the  Atrij about  the  middle  of  the  Suba  of  Kabul, which  included  Kashmir  and  all  west of  it.  We  do  not  find  that  the  modern form  occurs  in  the  text  of  the  Ain  as published  by  Prof.  Blochmann.  In  the translation  of  the  TabaJtat-i-Akbarl  of Nizamu-d-din  Ahmad  (died  1594-95), in  Elliot,  we  find  the  name  transliter-
```


## [2026-09-06T15:50:35.859Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '4656,4680p' HJB.txt; echo \"=== HJB CHEBULI ctx ===\"; sed -n '5835,5850p' HJB.txt"
}
```


### [2026-09-06T15:50:35.915Z] TOOL RESULT

```
OABUL,  OAUBOOL,  &c.,  n.i>. This  name  (Kabul)  of  the  chief  city of  N.  Afghanistan,  now  so  familiar, is  perhaps  traceable  in  Ptolemy,  wh(» gives  in  that  same  region  a  people called  Ka/SoXirat,  and  a  city  called Kdfiovpa,  Perhaps,  however,  one  or both  may  be  corrol>orated  by  the ydpSos  KafiaXiTTi  of  the   Perij)lu3.     The
CACOULI.
139
CADJAN.
accent  of  Kabul  ia  moflt  distinctly  on the  first  and  long  syllable,  but  English mouths  are  very  perverse  in  error here.    Moore  accents  the  last  syllable  :
"...  pomegfranates  full Of  meltizi^  sweetneaB,  and  the  pean And  sunniest  apples  that  Caubul In  all  its  thousand  g^ardens  bean."
Light  of  the  Harem,
Mr.  Arnold  does  likewise  in  Sohrab and  RuBtam : **  Bat  as  a  troop  of  oedlan  from  Cabool,
Cross     underneath     the     Indian     Can-
It  was  told  characteristically  of  the late  Lord  £llenborough  that,  after his  arrival  in  India,  though  for  months he  heard  the  name  correctly  spoken by  his  councillors  and  his  staff,  he persisted  in  calling  it  CdbGol  till  he met  Dost  Mahommed  Khan.  After the  interview  the  Governor-General announced  as  a  new  discovery,  from the  Amir's  pronimciation,  that  Cdb&l was  the  correct  form.
1552.— Barroe  calls  it  "a  Cidade  Cabol, Metropoli  dos  Mogoles.'* — IV.  vi.  1.
[c.  1S90.— "The  territory_of  Kilml  com- pnaes  twenty  Twao^ia." — ^««i,  tr.  JarretL n.  410.]
1856.- '*  Ah  Cabal !  word  of  woe  and  bitter  shame  ; Where   proud   old    England's   flag,    dis- honoured, sank Beneath  the  Crescent;  and  the  butcher
knives Beat  down  like  reeds  the  bayonets  that
had  flashed Fran  Plassey  on  to  snow-capt  Caucasus, In  triumph  through  a  himdred  years  of war."
Tfie  Banyan  Tree,  a  Poem.
GACOULI,  s.  This  occurs  in  the Apnp.  to  the  Journal  d^Antoine  Galland, at  Constantinople  in  1673  :  "  Dragmes de  Caconli,  drogue  qu'on  use  dans  le CXahue,"  t.e.  in  coffee  (ii.  206).  This is  Pers.  Arab.  Jbdkula  for  Canlamom, as  in  the  quotation  from  Garcia.  We may  remark  that  KdkuUi  was  a  place 4K>mewhere  on  the  GuK  of  Siam, famous  for  its  fine  aloes-wood  (see Ihn  BattUa,  iv.  240-44).  And  a bastard  kind  of  Cardamom  appears to  be  exported  from  Siam,  Amomum scanJthoideSy  Wal.
1568. — "0.  Ayicena  ^ves  a  chapter  on the  imiTlH^j  dividing  it  mto  the  bigger  and the  U8$  .  .  .  calling  one  of  them  caeolld muibir,  and  the  other  eacolld  cfguer  [Ar. MoHr,  fagktr},  which  is  as  much  as  to  say
greoJter  cardamom  and  snuUler  cardamom," — Oarda  DeO.yt  47 v.
1759.— "These  Vakeels  .  .  .  stated  that the  Rani  (of  Bednore)  would  pay  a  jrearly sum  of  100,000  Hoons  or  Pagooas,  besides  a tribute  of  other  valuable  articles,  such  as Foful  (betel),  Dates,  Sandal-wood,  XaJcnl .  .  .  black  pepper,  &c." — Hitt.  of  Mydur Naik,  183.
GADDT,  8.  i.e,  tea-caddy.  This is  possibly,  as  Crawfurd  suggests,  from Catty  (q*v.),  and  may  have  been originally  applied  to  a  small  box containing  a  catty  or  two  of  tea.  The suggjestion  is  confirmed  by  this  ad- vertisement :
1792.— "By  R.  Henderson  ...  A  Quan- tity of  Tea  in  Quarter  Chests  and  Caddies, imported  last  season.  .  .  ." — Madras  Covr{n\ Deo.  2.
CADET,  s.  (From  Prov.  capdety  and Low  Lat  capitettmn^  [dim.  of  caputs 'head'l  Skeat).  This  word  is  of course  by  no  means  exclusively  Anglo- Indian,  but  it  was  in  exceptionally common  and  familiar  use  in  India, as  all  young  officers  appointed  to  the Indian  army  went  out  to  that  country as  cadeUy  and  were  only  promoted  to ensigncies  and  posted  to  regiments after  their  arrival — in  olden  days sometimes  a  considerable  time  after their  arrival.  In  those  days  there was  a  building  in  Fort  William  known as  the  '  Cadet  Barrack ' ;  and  for  some time  early  in  last  century  the  cadets after  their  arrival  were  sent  to  a  sort of  college  at  Baraaet ;  a  system  which led  to  no  good,  and  was  speedily abolished.
1763.—"  We'  should  very  gladly  comply with  your  request  for  sending  you  young persons  to  be  brought  up  as  assistants  in the  Engineering  branch,  but  as  we  find  it extremely  difficult  to  procure  such,  you will  do  well  to  employ  any  who  have  a talent  that  way  among  the  cadets  or others  "^Court's  Letter,  in  Long,  290.
1769. — "Upon  our  leaving  England,  the cadets  and  writers  used  the  great  cabin promiscuously ;  but  finding  thev  were troublesome  and  quarrelsome,  we  brought a  Bill  into  the  house  for  their  ejectment." — Life  of  Lord  TeignmotUh,  i.  16.
=== HJB CHEBULI ctx ===
1817.—".  .  .  ready  to  prescribe  his favourite  regimen  of  the  Chaoiik  for  every man,  woman,  or  child  who  dared  to  think otherwise."- Za//a  Bx)okk,
GHAWBXJGE8WAB,  s.  H.  from P.  ckdbvh-sv/wdr,  a  rough-rider.
[1820. — "As  I  turned  him  short,  he  threw up  his.  head,  which  came  in  contact  with mine  and  made  my  chabookswar  exclaim, A  It  mudal.  *  the  help  of  Ali. ' " — Tod,  PtnoMl Narr,  Calcutta  rep.  ii.  723.
[1892. — "A  sort  of  high-stepping  caper  is taught,  the  chabukBOwar  (whip-rider},  or breaker,  holding,  in  addition  to  the  bridle, cords  tied  to  the  fore  fetlocks." — Kipling, Beast  and  Man  in  India,  171.]
CHEBULI.  The  denomination  of one  of  the  kinds  of  Myrobolaiui  (q.v.) exported  from  India.  The  true  ety- moloffy  is  probably  Kdbull,  as  stated by  Tnevenot,  i.e,  *  from  (Uabul.*
0.  1843.— "Ghebuli  miraiolani"—Litt  cf SpuxB,  kc,  in  PegoloUi  (D^la  Dedma,  iii.
c.  1666.— "De  la  Province  de  Caboul  .  .  . lee  Mirabolans  croiasent  dans  les  Montagues et  c'est  la  cause  pourquoi  les  Orientaux  lea appelent  CnXnly,  —Tkevenot,  v.  172.
CHEECHEE,  adj.  A  dispara^g term  applied  to  half-castes  or  EnrasianB (q.v.)  (corresponding  to  the  Lip-lap  of the  Dutch  in  Java)  and  also  to  their manner  of  speech.  The  word  is  said to  be  taken  from  (M  (Fie  !),  a  common native  (S.  Indian)  interjection  of  re- monstrance or  reproof,  supposed  to  be much  used  by  tne  class  m  question. The  term  is,  however,  perhaps  also  a kind  of  onomatopoeia,  indicating  the mincing  pronunciation  which  often characterises  them  (see  below).  It should,  however,  be  added  that  there are  many  well-educated  East  Indians who  are  quite  free  from  this  mincing accent.
1781.— "  Pretty  little  Looking-Glasses,
Good  and  cheap  for  Chee-chee  Misses." ffiehy's  Bengal  Gazette,  March  17.
1873. — "  He  is  no  favourite  with  the  pure native,  whose  language  he  speaks  as  his  own in  addition  to  the  hybrid  minced  English (known  as  chee-chee)^  which  he  also  em- ploys."— Fraier's  Magazine,  Oct.,  437.
1880.— "The  Eurasian  girl  ia  often  pretty and  graceful.  ...  *  What  though  upon  her lipe  there  hung  The  accents  of  her  t^-tchi tongue.*  "—Sir  Ali  Baha,  122.
1881.— "There  is  no  doubt  that  the  'Che* Chee  twang,'  which  becomes  so  objection- able to  every  Englishman  before  he  has  been
OHEENAK
187
CHEETA,
```


## [2026-09-06T15:50:40.860Z] TOOL CALL #34: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-06T15:50:40.866Z] TOOL RESULT

```


```


## [2026-09-06T15:50:44.666Z] TOOL CALL #35: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%E1%B8%B1oph2os",
 "prompt": "Is there a PIE reconstruction for \"hoof\"? Give the reconstructed form, gloss and descendants (Avestan, Sanskrit, Germanic)."
}
```


## [2026-09-06T15:50:46.319Z] TOOL CALL #36: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B3%D9%85",
 "prompt": "Persian section: etymology of سم (som) \"hoof\". Give Middle Persian form, Proto-Iranian reconstruction, and any cited sources (Hasandust, MacKenzie)."
}
```


### [2026-09-06T15:50:46.483Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-06T15:50:52.449Z] TOOL RESULT

```
# Persian Etymology of سم (som) "hoof"

Based on the Wiktionary entry, here's what's documented:

**Middle Persian form:** The source notes "[script needed]" (swmb' /⁠sumb⁠/, "hoof"), indicating the Middle Persian equivalent exists but wasn't fully rendered in the article.

**Proto-Iranian reconstruction:** The entry cites Proto-Indo-Iranian *[\*ćapʰás](/wiki/Reconstruction:Proto-Indo-Iranian/%C4%87ap%CA%B0%C3%A1s)

**Sources cited:** The etymology section provides no named academic sources (such as Hasandust or MacKenzie). The entry simply states the word derives "From Middle Persian" through Proto-Indo-Iranian, without bibliographic references for these reconstructions.

The article lacks the detailed philological citations you're seeking and doesn't include modern scholarship attributions for these etymological claims.
```


## [2026-09-06T15:50:56.566Z] TOOL CALL #37: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/%C4%87ap%CA%B0%C3%A1s",
 "prompt": "Give the reconstructed Proto-Indo-Iranian form and gloss, the PIE ancestor, and all descendants listed (Proto-Iranian, Avestan, Sanskrit, Persian, Ossetian, Pashto). Quote how Persian سم is derived and any note about irregularity."
}
```


## [2026-09-06T15:50:57.384Z] TOOL CALL #38: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/hoof",
 "prompt": "Give the full etymology of \"hoof\": Old English, Proto-Germanic form, PIE root, and cognates (Sanskrit, Avestan)."
}
```


### [2026-09-06T15:51:02.481Z] TOOL RESULT

```
# Proto-Indo-Iranian ćapʰás: Hoof Etymology

**Reconstructed Form:** *ćapʰás (masculine noun meaning "hoof of an animal")

**PIE Ancestor:** The term derives from Proto-Indo-European "*ḱoph₂ós"

**Key Descendants:**
- **Sanskrit:** śaphá (शफ)
- **Avestan:** safa (𐬯𐬀𐬟𐬀)
- **Persian:** som (سم)
- **Ossetian:** sæftæg (сӕфтӕг)
- **Kurdish:** sim (Northern and Central varieties)

**Persian Derivation:** Persian "som" descends through Middle Persian "sumb'" (swmb'), which itself derives from Proto-Iranian "*cafáh," the Iranian branch's continuation of the original Proto-Indo-Iranian form.

**Irregularity Note:** The entry shows an interesting pattern: Old Armenian "smbak" and Arabic "sunbuk/sunbak" appear as borrowings from Iranian languages rather than direct descendants, indicating secondary transmission through trade or cultural contact.
```


### [2026-09-06T15:51:03.804Z] TOOL RESULT

```
# Etymology of "Hoof"

**Old English Origin:** The word derives from Old English *hof*, meaning "hoof."

**Proto-Germanic Form:** It comes from Proto-Germanic *\*hōfaz*, which also produced cognates in Old Saxon, Old Frisian *hof*, Old Norse *hofr*, Danish *hov*, Dutch *hoef*, and German *Huf*.

**PIE Root:** The proposed Proto-Indo-European source is *\*kop-*, meaning "to beat, strike."

**Cognates:** The dictionary identifies "Sanskrit *saphah* 'hoof,' Polish *kopyto* 'hoof'" as related forms. However, the entry notes that etymologist Boutkan "acknowledges only Indo-Iranian cognates" and suggests this may be "a typical relic form that only survived in the periphery of the IE area."

**Note:** The entry does not provide Avestan cognates. The Sanskrit connection represents the strongest attested Indo-Iranian evidence for this root's ancient provenance.
```


## [2026-09-06T15:51:13.293Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('BRT.txt',encoding='utf-8',errors='replace').read().split('\\f')\nimport re\nfor n,p in enumerate(t):\n    if 'safa-  ra.' in p or \\\"safa-  m\\\" in p or re.search(r'safa-\\s+ra\\.',p):\n        print('LEAF',n); \n        i=p.find('safa-')\n        print(p[max(0,i-1500):i+300])\n        break\n\" | tail -40"
}
```


### [2026-09-06T15:51:15.040Z] TOOL RESULT

```
LEAF 850
ten': vazr»m  .  .  saiaßtämm  •nm  Yt.  10.  96.
ai.  ialOtlhSra-  Adj.
•  j.  satö.vira-  Adj.  'hundert  Männer  hoch, tier:  'rim  vaOnim  (sd.)  V.4.$a.
ai.  vgl.  iatoTiira'  Adj.,  Bein,  du  fiinav.  — Vgl.  'vTra-  No.  I.  —  PQ.:  lOQ  vTr.
•  j.  satö.raodana-  Adj.  'mit  hundert  Fen- stern versehen':  nmäfum  ..  °n>m  ..hata- urBjtunsm  Yt.5.  loi.
•  j.  satö-stüna-  Adj.  'auf  hundert  Säulen ruhend,   hundertsäuh'g':  nmätutn  . .  * hazaarS.frasHmban>m  V.1S.2S.
Pü.:  too  la».
•  j.  sato.straDha-  Adj.  (fem.  'ishä-)  "mit hundert   Juwelen  (?)    besetzt':    pusau. •aham  saranalfilm  Yt.  5.128.
'ilranha-  m-,  Bed.?;  ob  zu  iilsr-'i
•  j.  sala'nah-  m.  EN.  eines  Gläubigen: ultrake  'naishs  a^aotiB  "des  U.,  Sohns  des S.  .."  Yt./?.iis.
Komp.:  saia'-\.*aah-  Adj.,  zum  ai.  V.  m etwa  sva.  Ei'msraf.
•  j.  saSay-  Adj.  —  ?  — :  buxtiS  nqma ahmi  'ilis  nama  ahmt  Yt  15. 47.  Geringe Stelle.
•  j.  saSa-  f  1)  "Erscheinen,  Aufgehen' derGestime:  hakpr?l  zT irixtahe(s±)  °laya- (LS.)fa  vamaife  starasla  mäsca  kvortca V.  -2.  40.  j)  'Gutscheinen,  Gefallen, Zufriedenheit':  *'o*'>  (IS.)  F.  12.
KompA.  —  Zum  V.  ^sand-,  —  zBed.  vgl.  ai. chanda-  m.  —  PO.  (dRn.):  sahel  (3S.},  Harlan- dlh.—  I)  Hds,  vaür,  aber  unter  den  Wörtern für  J-;  -e  für  -ya,  %  26S.  32.
j.  taiSMnqm  N.  36:  lies  gai'.
'].  faiii  satre  Vyt.  79:    gemeint   ist   laÄ-zj
j.  sal-väslrahe  N.  _J/;  lies  isal.v'.
•  j.  safa-  ra.  'Huf  des  Pferdes:  aurvants..
sroawna
```


## [2026-09-06T15:51:21.513Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('BRT.txt',encoding='utf-8',errors='replace').read().split('\\f')\nimport re\np=t[850]\nprint([x for x in re.findall(r'\\b1[0-9]{3}\\b',p)][:20])\nprint(repr(p[:200]))\n\""
}
```


### [2026-09-06T15:51:23.487Z] TOOL RESULT

```
['1000', '1556']
'a  hazanraisca  Vr.  Ä  i.  a)  mit attiib.  Einerzahlen:  hazatanm  narqtn  .  . iaoxma  . .  xlvas  \'ta  . .  tisrS  \'ta  (als  Gen.) "den  Samen  von  1000  Männern  . .  von 600  . .  von  300"  V'
```


## [2026-09-06T15:51:30.056Z] TOOL CALL #41: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CE%BA%CE%AC%CF%80%CF%80%CE%B1%CF%81%CE%B9%CF%82",
 "prompt": "Ancient Greek κάππαρις: give the full etymology section verbatim-ish (origin, Beekes/Chantraine view, any Iranian/Persian or Semitic connection), and the list of descendants (Latin, Arabic, Persian, Aramaic)."
}
```


## [2026-09-06T15:51:30.898Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/caper",
 "prompt": "Give the etymology of caper (the shrub/flower bud, caper (n.2)): Middle English, Latin capparis, Greek kapparis, and whether an Oriental/Persian origin is mentioned."
}
```


### [2026-09-06T15:51:37.703Z] TOOL RESULT

```
# Etymology of Caper (the Plant)

**Origin Path:** The word entered English in the late 14th century from Latin *capparis*, which derived from Greek *kapparis*. The Greek origin itself remains uncertain.

**Oriental Connection:** The etymology page notes that "Arabic *kabbar*, Persian *kabar* are from Greek," indicating these languages borrowed the term from Greek rather than serving as the original source. So while Eastern languages have related forms, they appear to be secondary adoptions rather than the root origin.

**Key Quote:** "from Latin *capparis*...from Greek *kapparis* 'the caper plant or its fruit,' which is of uncertain origin."

The document does not identify a definitive Oriental or Persian etymology for the plant name itself, only acknowledging that Arabic and Persian versions derived from the Greek term.
```


### [2026-09-06T15:51:38.289Z] TOOL RESULT

```
# Etymology of κάππαρις

**Origin:** The word has been connected with Persian *kabar* ("caper") and Burushaski *čopuri*, suggesting an Oriental origin.

**Source:** Beekes, Robert S. P. (2010), *Etymological Dictionary of Greek*, page 639.

# Descendants

The term spread widely across languages:

- **Greek:** κάπαρη (kápari)
- **Latin:** capparis
  - → **English:** caper
  - → **Italian:** cappero
  - → **Translingual:** *Capparis* (genus name)
- **Aramaic:** Classical Syriac ܟܦܪ (kappar/kappār)
  - → **Arabic:** كَبَر (kabar), كَبَّار (kabbār), قَبَّار (qabbār)
    - → **Middle Armenian:** կապպար (kappar)
- **Ottoman Turkish:** كبره (gebere)
  - → **Turkish:** gebre
    - → **Armenian:** գաբարա (gabara)
```


## [2026-09-06T15:51:46.610Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Kabul",
 "prompt": "Give the etymology of Kabul: Persian کابل, Sanskrit Kubhā, Greek Kophen/Kabura, any Old Persian or Avestan attestation."
}
```


## [2026-09-06T15:51:48.239Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%A9%D9%88%D9%84%DB%8C",
 "prompt": "Persian کولی (kowli) \"gypsy\": give the etymology section in full, including any derivation from کابلی (Kabuli) or other proposals."
}
```


### [2026-09-06T15:51:53.345Z] TOOL RESULT

```
# Etymology of Kabul

Based on the Wiktionary content, here's the etymological information:

**Primary Source:** The word "Kabul" was "Borrowed from Classical Persian کَابُل (kābul), of unknown origin."

**Extended Etymology (per Spanish section):** The Spanish entry provides additional historical layers, noting that Persian کَابُل borrowed from multiple ancient sources:

- **Sanskrit:** कुभा (kubhā, "Kabul River")
- **Ancient Greek:** Κάβουρα (Káboura, "a settlement in Afghanistan crossed by Alexander the Great")
- **Avestan:** 𐬐𐬎𐬡𐬀 (kuβa)

The documentation notes: "Pronunciation changed to 'Kabul' around the 11th century." The Middle Persian entry also attests the form kʾpwl (/⁠kābul⁠/), demonstrating continuity across Persian language stages.

The ultimate origin remains uncertain, though the convergence of Sanskrit, Greek, and Avestan forms suggests the name's antiquity in Central Asian geographical nomenclature predating Classical Persian standardization.
```


### [2026-09-06T15:51:53.997Z] TOOL RESULT

```
# Etymology of Persian کولی (kowli)

According to the Wiktionary entry, the word کولی derives from کابلی (Kabuli), "because when they first appeared it was wrongly believed that they were from Kabul."

The entry also notes that various regional terms exist for the same group across Persian-speaking areas:

- In Khorasan: قرشمال (qerešmâl)
- In Kerman, Balochistan, and Tajikistan: لولی (luli)
- In southern provinces like Luristan and Kermanshah: سوزمانی (suzmâni)

The etymology suggests a geographical misconception drove the original naming, with the Kabul attribution persisting in the standard form despite being historically inaccurate.
```


## [2026-09-06T15:52:01.087Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"chebul\" KLN_1966.txt KLN_1971.txt WEB_vol1.txt FSD_vol1.txt 2>/dev/null | head -10"
}
```


### [2026-09-06T15:52:01.179Z] TOOL RESULT

```
KLN_1971.txt:44594:chebule, n., the dried fruit of Terminalia chebula. 
KLN_1971.txt:44595:— F. chebule , fr. Arabo-Pers. kabult, lit., ‘from 
KLN_1966.txt:7295:chebule,  n.,  the  dried  fruit  of  Terminalia  chebula. —  F.  chebule,  fr.  Arabo-Pers.  kdbult,  lit.,  ‘from (the  city  of)  Kabul'.
FSD_vol1.txt:63560:Che-boy'gan,  I   fihi-bel'gan;  2   che-b6y'gan,  n.  1.  A   county In  N.  Michigan;  785  sq.  m.  2.  Its  county-seat, che-bule',  1   ki-bul';  2   ce-byl',  n.  The  dried  astringent prune-like  fruit  of  an  East-Indian  tree  ( Terminals chehula)  of  the  myrobalan  family,  a   kind  of  myroba- lan.  [<  F.  chebule,  <   Hind.  Kabuli,  of  Cabul.]  —   che- bu'Iic,  a.
```


## [2026-09-06T15:52:02.388Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/chebulic",
 "prompt": "Etymology of \"chebulic\" (as in chebulic myrobalan): give the full etymology, mentioning Medieval Latin chebulus, Arabic/Persian kābulī, Kabul."
}
```


### [2026-09-06T15:52:06.955Z] TOOL RESULT

```
Based on the Wiktionary page provided, I can only offer limited etymological information. The page states that "chebulic" comes "From translingual _chebula_ +‎ _-ic_."

However, the source document does not contain the detailed etymological chain you're requesting (Medieval Latin chebulus, Arabic/Persian kābulī, Kabul). To provide that complete etymology, I would need access to additional sources beyond what's presented in this Wiktionary entry. The current page only traces the word back to the scientific Latin term "chebula" plus the English suffix "-ic."
```


## [2026-09-06T15:52:15.845Z] TOOL CALL #47: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:1163 --image 2>&1 | tail -40"
}
```


## [2026-09-06T15:52:16.339Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json;d=json.load(open('refs_online.json'))\nprint(json.dumps(d['AFM'],ensure_ascii=False,indent=1))\n\""
}
```


### [2026-09-06T15:52:17.935Z] TOOL RESULT

```
no scan of BQT covers printed page 1163 (see 'scans' in refs_online.json)
```


### [2026-09-06T15:52:19.519Z] TOOL RESULT

```
{
 "title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)",
 "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM.txt"
 ],
 "page_offset": "198 leaves; page numerals OCR'd unreliably — offset approx leaf − 8 (front matter); confirm on page image",
 "covers_etymology": true,
 "notes": "Arabic OCR fair; Syriac/Latin etyma partially garbled.",
 "cites": "page number of Addi Shir, al-Alfāẓ al-fārisiyya al-muʿarraba (1908)"
}
```


## [2026-09-06T15:52:24.987Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && head -5 BQT_v2_pages.txt | cat -A | head -5 | cut -c1-200; echo \"=== formfeeds ===\"; python3 -c \"\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\nprint('pages:',t.count('\\f'))\nprint(repr(t[:300]))\n\""
}
```


## [2026-09-06T15:52:26.109Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('AFM_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(len(t))\nfor n in range(136,144):\n    print('=== leaf',n)\n    print(t[n][:600])\n\""
}
```


### [2026-09-06T15:52:27.174Z] TOOL RESULT

```
^L                                         M-bM-^@M-+M-bM-^@M-*7M-bM-^@M-,M-bM-^@M-,$
$
                          M-bM-^@M-+M-XM-1M-YM-^FM-bM-^@M-*M-[M-3M-bM-^@M-,M-bM-^@M-,$
    M-bM-^@M-+M-YM-^FM-XM-'M-XM-*M-bM-^@M-,$
      M-bM-^@M-+M-XM-' M-YM-^EM-bM-^@M-,$
=== formfeeds ===
pages: 683
'\x0c                                         \u202b\u202a7\u202c\u202c\n\n                          \u202bرن\u202a۳\u202c\u202c\n    \u202bنات\u202c\n      \u202bا م\u202c\n              \u202bلض\u200cبال \u202a ۰ ۲۶\u202cرک\u202c\n\u202b\u202a۱\u202c\u202c       \u202bاسا تعدولیدیارتم و\u202c\n                                     \u202b\u202a7\u202c\u202c\n\u202b\u202a ۰\u202cو زل رسوا »وا روون لات سا روصا مواقم\u202c      \u202bوتان\u202c\n\n                      \u202b\u202a۴2 ۱\u202c\u202c'
```


### [2026-09-06T15:52:28.932Z] TOOL RESULT

```
198
=== leaf 136
2-0
( الك ركاه ) آلة للحائك وهي فارسيّة
( الكرويا) بزر ننات شه اغصانة وورقه بالرجلة الا £ أون ورقه واغصانه الى
ا 0 000 60070 0:0938 مأخرذ من
ܐܝܛ "0 وهو ¢01011111 بالروممة و0151© بالفرئنسة :
( الكزمازّج ) ثرة الطرفاء < 92( وهي 6 من كزم اي طرفاء
ومن مازو اي عفص اي عفص الطرفاء ٠‏ وقال في البرهان القاطع 3.05 حب الاثل ٠‏
50 والكزمازات لغتان فيه
510 ) لل اللاعن 0 ©
0000 إن اليك عرفب ܐܐ 111
( المُمْتِيج ) خبط غليظ ± الذمي فوق ثيابه دون الزّار معرب عن كدت .
ܠܨ ° ܟܘܣܿܬܢܝܓܐ ¦
3 ܐܕܝܨ حض ومعناه الاصطبل ‏ ܒܝܬܦܣܣܬ/ ܟ
` 9 7 > 70 والقمر مَكَسَف] نهنا اي 9 وغارها 7835
واد 1ط 04 خسفب ܢܬܢ الأفيد > كت كا ولوك وان
=== leaf 137
س ܕܨ ܙ لب
053 3 1090 اى :كتف أورفن ܐ المحتمل ان تكون ارام يل <
من ܪܫܦ اي جمّع ومن ‫
ܝ ` 0 4
(5063 0:1008 5 او بدت الصيف 7 1 نه ܨ ال لحرة
لضيقة اللقيرة وتطلق ايضاً على الشتاء وعلى عش الطائر
0 الكرستّه فارسيّتها كته ٠‏ واظن ان الكرسنة لغة فيها
١‏ 31 ) تعر يب ܐ“ وهو ارا 1 | ܨ الذقيق والحليب 1
ܕܢ ܟܘܟܐܐ بالاراممة ܕ ܐܬܪܐ @) ¢ ܠܝܐ ܪ €00018] بالايطاليائة
و 11661 باكرمانة |
( الكاغد) فارسي حض بعنى القرطاس . والكاغذ لغة فيه ومن الحكردي
كاغز واما القرطاس فعرب 5 `
١‏ الكافور» طيب يكون من شجر مجبال بجر ܐܬܝܥ والصين يلل خلقاً كثيرًا
وخشبة ابيض هش خفيف جدًا ويوجد في اجوافه الكافور وهو انواع ( يط
ܬܝܐ ) 2 4116 
=== leaf 138
_ ܙ -
د (تكاتان ) آلة من حديد ܓ 9 3( ܓ <
وهنه ܬܝ ܥ » 350
)ܝ اياقب في انبر ,0003 54450 -
` © 50 )ܐܢ 39 ܛܘܦܐ
× 0 القطعة ܐܐܳܐܬܟܳܐܘ̈ من الأرض م :0
وقالوا فيها تكد الى غير ذلك
لاط _ 0:43047 وحهها 5 0-0 اي ورد ومن كون ܒ
لون
زاكك كا عد مدال الذي خالط حرقة قار قنو* أي سواد غير خالص ܝܢܐ بين
911 5:7 ابو عنيدة : :* فرق بسين ܐܳܚ والأشقر بالعرف والذائب ٠‏
:ܡܫ( أحمرين فهو الاشقر وان كانا 33 فهو 0 وهو تصعار 2 1
غير قياس »> ٠‏ وعن الأصمعي "انار حر اذالم يخالط 3 0 > خالط ¬ 47
݂ܕ 9 0 5 ابضا. «قات وفارسية كتيت ت ܐܢܐ وهو ܐܵܕ 5-0
ܐܫܟ التي (1:, ةزعل اليل 9801 ܛ ܕܪ نه اسودان٠‏ 07
٠ 0‏ كيت ܪܕܫܕ المختلط › وقالت ف افيه
=== leaf 139
-_ ,)| لس
ܐ ܀# 3 وب ܝ مت و
8( لكر الببذعة ܗ سرع الفرس مركبة هن كن اي ذبر ومن
ܣ اي غطاء
او 1 الوم اختلطوا 85 500 : ܢ 25111
والعمل
(ألكنك ) 7 1 عد 3 العد رد
04005 1759 38 30945 وهر كه 9 كدان
+ [ الكتدجة) فعرية كله وه لمعه كاله تر 0 و ا
الحدران والطيقان
( الكندوج) 7:02 ܨ سمه حزن من تراب او خحشب توضع فيه
)213 9[ ها١٠ومئه‏ ظنج هو مها
# ( ܥܐ ܕܙ ) الغليظ القصير مع شدة. واككُتدر ܚܕ فيه ٠و(‏ :ܝ ) اليار
الغليظ . ܕ ( ܐܥ( 0 ! الغليظ ٠‏ و( الكنديرة ) 83 والضخامة ٠و‏ (الكَنْدَرَة)
ما 85 من الأرض: كل ذلك راجع الى معنى الكلمة: الفارسة ܐܒ 500
0033[
الشجيع 0 31
( :13 ) الشجاع المسور فارسيتة كنداكر
( أمكندبن ) 9
=== leaf 140
لاوم( -
ومعنى ¥ الماذب ٠‏ ويرادفة 6 :)10 `
القاطع : « قيل ان ܦ صمغ ܣܨ الرومي وهو في بلاد البلغار: وقيل صمغ
الدَوْم ٠‏ وقيل ضرب من الاؤلو يوجد في سواحل بجر المغرب ٠وقيل‏ صمغ شجر يشبه
شجر الفستق يشتعل بالنار مثل الكبريت ولهذا قيل له سيّد الكباريت ٠‏ وقيل يأبع
من ܐܐܟ في بلاد الروس واول مسا يضر به اللهواء يحمد مثل المرمر وهذا الحكهر باء
اقيق ويقال له بالعربّة مصباح الروم ٠‏ وقيل اله من انواع ܝ  -:‏ 50
ܟܗܪܒ̄ܐ
نكر 2 ) الذل الطغيد المخضر 6 6
٠ 1‏ 0 ير اراس لاحرؤة 4 او لآ حرظوم ل وهو معرب عن كوب ,
والثلاهر ان الكلمة من موافتات اللغات وهر حه كمط" بالارامية ( ¥+ 9 ]
ܐܟ ) ܕ ܟܘܦܐ بالسريانّة الدارجة وكرب ب
=== leaf 141
9:4
# ( كرارة) النحل وتكسر وكؤارتها بتشديد الواو شيء ܡܳܐ ܐܗܐ من
القضبان او الطين ضيّق الراس ٠وقيل‏ هي عسلها في الشمع وقيل ܐ( الخلايا
الاهلءة وهي ܘܨ بة عن كْوَارَه ومعناها 965 وتطلق 0 على سهد العسل
* (الكارَة) ما يحمل على الظهر من الثياب ٠‏ وفي اللسان:« والكارة عكم
الثبات قاكارة التصار سيت لاله يكور نا شتف يون راح اياي كتوق را
فوق بعض ٠»‏ قلت والاصح انْ الكلمة فارسيّة ܬܨ بها كارّه وه وكل ما يحل على
الظهر من الثياب والمماب واككلا وغير 0 مركّة من كار اي عمل شغل
ومن هاء التخصيص ٠‏ ومنها ܪ فمل” كار 4 5 77 | ܟܪܬܐ
ܐܝܟ ܨܬ
5 5:5 له عروة و بلبل تعر ب ب كاز 9( (فرتكل :078 .
` ܫܫ اي شرب بالكوز واكتّازٌ وم
=== leaf 142
‫ 1
ܢ ܐܟܟ - + 97 315 355 :انث كك بالقارشئة
ܘܚܐܘ الرفيع القدر ويطلق على الاك التهار المار وهو كنية عندهم عن ملك الاوك .
وار بعة من 46 دولتهم الثانية لُيَُوا به وهم كيكاوس وكيخسرو وكيتباد وى
هراسب ثم ; بق الغلبة على ܬܝܟ ܨ الدولة الثانية فقيل لهم ܫ
وهو جمع ‏ قي ( البيعان القاطع )
(اتكال) الة معوجة ܝ تهدم 0 ܟܒ 7 فارسّة فاذا صح
ذلك ك1 ادن 1 لشات :0600
+« ( الكلحَة ) كيل معروف لاهل العراق وهى 0 ܝܫܐ 0:00 ܦ
والفارسى ܝ ܨ ܟܝܠܐ :
لكا ) المطكى فارسيّة كنا
05
(اللازورد) 3 0
ال 1 الطرة معرب ليت
ܐ اللجام ) تعريب لكام وهو بالارامسة ܠܓܡܐ ܠܘܓܡܐ وباحدشة 1010 +
وبرادفة ܐܐܐܠ 4 (١‏ فرد ܀ \ ) ܕܝܢ 13100 ا 0 صل
< 1 ® 
=== leaf 143
ܒܝ <
(اللاخشة ) الاإطربة وهي طعام كاخيوط من الدقيق . واللاخوشة ܕ )ܪܫܐ
ܬܰܝܨܳܐ رهى .7 اك
15063 21411 30 54890
)1:00 واللكن لغة فيه تعريب لَكَن ومنة السر 0 ܝܐ 6(
والكردي 1:3 ¢ 2
+ ( اللقّازق ) ويقال ثقائق اسم لأحد الأمعاء وبه سي معى | ام ابعشو و ܐܠܨ .
دس ععاوم 1 م مرب يكبا الغليل ) .قات وهو معرب ܐ نه وهو العصب
بد ( الك ) صبغ 7 ` ܟܝܬ به جاود المعزى تعر يب لك
1 ܫ الرأة القصيرة الذميمة وقيل الطوية الحزية وقيل مقاوب الرهلة
وهي الت لا 5 ܇ ` ني مشا تقلا ( اقرف الوارة؟؟ اتلتهنا وده
عن ܐܚ̈ܐ ܬ ومعناها المرأة الحممّاء
± (اللادّة ) ثوب حرير 598 لاد
(اللوياء » 90547 7( 0108 10595( 109433803
فرنكل ( ص : £ \ )
```


## [2026-09-06T15:52:36.076Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nimport re\nt=open('AFM_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor n,p in enumerate(t):\n    for m in re.finditer(r'الكبر|كبر\\s*\\)|قبار|كبار\\s*\\)', p):\n        print(n, repr(p[max(0,m.start()-150):m.start()+250]))\n\" | head -20"
}
```


### [2026-09-06T15:52:37.836Z] TOOL RESULT

```
140 ' ܦ صمغ ܣܨ الرومي وهو في بلاد البلغار: وقيل صمغ\nالدَوْم ٠\u200f وقيل ضرب من الاؤلو يوجد في سواحل بجر المغرب ٠وقيل\u200f صمغ شجر يشبه\nشجر الفستق يشتعل بالنار مثل الكبريت ولهذا قيل له سيّد الكباريت ٠\u200f وقيل يأبع\nمن ܐܐܟ في بلاد الروس واول مسا يضر به اللهواء يحمد مثل المرمر وهذا الحكهر باء\nاقيق ويقال له بالعربّة مصباح الروم ٠\u200f وقيل اله من انواع ܝ  -:\u200f 50\nܟܗܪܒ̄ܐ\nنكر 2 ) الذل الطغيد المخضر 6 6\n٠ 1\u200f 0 ير اراس لاحرؤة'
```


## [2026-09-06T15:52:55.434Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nimport re\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('leaves',len(t))\nfor n,p in enumerate(t):\n    if re.search(r'سنب|سُم|سم\\s*:', p):\n        pass\n# find leaves containing 'سم ' as isolated\nfor n in range(600,640):\n    p=t[n]\n    hits=re.findall(r'س[مه]ب?', p)\n    print(n, len(p), p[:120].replace(chr(10),' | '))\n\" 2>&1 | head -45"
}
```


### [2026-09-06T15:52:57.391Z] TOOL RESULT

```
leaves 684
600 3626  ‫‪۱۱۳‬‬ |              ‫آمد وسزاوار گردید هم هت ‪4.‬‬         ‫سزا باشد‬          ‫دن*بیزمعنی‬ |                           
601 4197                                                                                           ‫‪۱۳۹‬‬ |  |  ‫مخفف اصطرلاب است »و
602 4127  ‫اه‬       ‫‪۵‬‬                                                                           ‫حواشی‬ |  |                    
603 517 ‫الفبای سفدی‬                                                    ‫برابر صفحه ‪۰4۱۱‬‬ |  |  |  |  |                                
604 170  ‫‪a‬‬ |  |  ‫کے‪‎‬‬ |  | ‫په‪‎‬‬ |  |  |  |  ‫‪۵‬‬ |  | ‫ما‪‎‬‬ | ‫‪J‬‬ | ‫‪4‬‬ |  ‫د‪‎‬‬ |  |  |  |                     ‫الفبای سغدى ( متأخر )‬ |        ‫
605 3469                                           ‫بیان چهاردهم‬ |               ‫بر بانزده لغت‬          ‫سین بی‌نقطه باغین نقطه‌
606 4252   ‫‪NE‬‬ |  |                          ‫خاریشت بز ر گے تبرانداز باشد ‪.‬‬                  ‫سقر ‪. ۱‬۽ بضم اول وفتح ثالی و س
607 4198                                                                                        ‫‪۱‬‬ |                            
608 4598  ‫=‪— 4‬‬                                                                                                      ‫سفته گوش
609 4118  ‫سفد کاسه‬                                                                                                ‫ع—‬ |         
610 3872                                                           ‫بیان شانز دهم‬ |              ‫درسین بی نقطه با قاف مشتمل بر بس
611 4504                     ‫کسهت‌آسمان باشد‪.‬‬ |                                    ‫لاجورد ا‬                                  
612 4460      ‫==‬                                                                           ‫سقلاطرن‬ |  ‫بلغت بونانی‌دواییاست کهآ
613 4647                                                                                              ‫‪۷۱۷ 6-‬‬ |  | ‫و شروع بحر کنن
614 5892             ‫‪۱‬‬ |             ‫= هی‬                                                                                    
615 5275       ‫رککه‬ |          ‫س‬ |  | ‫ووحه‪.‬‬      ‫کنند و هروقت که خواحند صر فکننده‬                         ‫کار صازی‬    ‫و‬  
616 4918       ‫‪۷‬‬ |       ‫‪ ۷‬ی‬ |  |  ‫سکسکی = یم هردو سین و سکون‬ | ‫ثالی و رابع بتحتانی کشیده ‪ .‬زحمتی باشد که‬                  
617 4941   ‫سکوا‬                                                                                                        ‫هه‬    
618 4762   ‫اه‬       ‫هی‬ |                                                                                                       
619 3957                                                                                             ‫=‬        ‫ع یو‬ |  |          
620 4322    ‫‪—۱‬‬     ‫تن‬ |                                                                                                      
621 4710                                                                                                      ‫—‬       ‫پوي‬ |  |  |  
622 4760      ‫=‬‫)وی‬‫‪-‬‬ |  |  ‫میگونند که حر کس آنرامیکند میمیرد » پس‬                    ‫=روزن سیتان »زاباتان‬ |                 
623 4189   ‫سلشوق‬                                                                                               ‫‪۱‬‬ |           
624 3722   ‫=‬ |  |  ‫شین اقطه‌دار ‪ ,‬بلغت زند و پازند (‪ )4‬بمعنی بد‬        ‫سلح شور ‪ = ۱‬بفتح اول وئالی؛به‌عنی‬ | ‫ادبرل ليك امت ؛
625 4665                                                                                           ‫‪--٩ ٩٩ -‬‬ |  | ‫و بمعتی رشته مر
626 4338   ‫‪-۱۱۲ -‬‬ | ‫آن گذارند ‪ -‬و هر سبد را لمز‬                 ‫که چزها در‬            ‫وثانی‌درعربی‬    ‫ویفتح اول‬      
627 4282   ‫سماررغ‬                                                                            ‫اعد‬   ‫‪۳‬‬ |  |                    
628 6465    ‫‪۹۱‬اصه‬                                                                                                            
629 3612  ‫مگ‬                                                                                       ‫اس‬    ‫‪۱‬‬ | ‫آست ومعنی تر 
630 4953         ‫س‬‫ا‪۹۹‬‬ |            ‫حه‬ |  |     ‫أبن نریمان است ® ‪٬‬وعربان‏ بتقدیم نون بر میم‬            ‫کاف» بمعتی رعنا ورعن
631 4561                                                                                                        ‫—‬ |  |            ‫
632 4577   ‫‪۱۱ ۹۸ -‬‬                                                                                               ‫سمور‬ |  |  |    
633 3516                                               ‫بیان ليست ویکم‬ |           ‫ونایت‬ |               ‫در سین بی نقطه بانون مشت
634 4237       ‫و‪۷‬‬                                                                                                     ‫ساو‬ |  | 
635 5141                          ‫جالوریست ممروف ازموش‬                 ‫بونالی‌زیره راکوبند و بهترینآن کرمالی باشد‪.‬‬ |         
636 5291  ‫‪— ۷‬‬                                                                                                                
637 4215     ‫سندل‬                                                                                   ‫‪۳۷-‬ات‬ |                  
638 4918      ‫)‪۱‬ات‬ |  |  ‫ونام درخت بلوط هم حت بلفت اهل شام ‪. ۷‬‬                           ‫باشد که آنرا از کنار دربا بر از آب 
639 4524   ‫سنگه پرستوك‬                                                                                ‫«‬ |
```


## [2026-09-06T15:53:14.695Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nimport re\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor n in range(624,634):\n    p=t[n]\n    nums=re.findall(r'[۰-۹]{3,4}', p)\n    print('LEAF',n,'nums',nums[:8])\nprint('=== leaf 628 ===')\nprint(t[628][:3000])\n\""
}
```


### [2026-09-06T15:53:16.574Z] TOOL RESULT

```
LEAF 624 nums ['۱۲۱۰', '۹۹۳', '۸۷۲']
LEAF 625 nums []
LEAF 626 nums ['۱۱۲', '۰۸۲۰', '۲۷۲', '۸۵۷۰']
LEAF 627 nums ['۲۵۱']
LEAF 628 nums ['۲۹۲', '۵۸۲', '۵۹۱۱']
LEAF 629 nums ['۲۲۹۲', '۶۹۱۱', '۷۱۲', '۰۸۲', '۷۱۲']
LEAF 630 nums ['۳۲۱', '۶۰۰۱', '۵۳۱', '۱۵۱']
LEAF 631 nums ['۵۳۱']
LEAF 632 nums ['۳۵۲']
LEAF 633 nums ['۳۹۱', '۹۲۱']
=== leaf 628 ===
   ‫‪۹۱‬اصه‬                                                                                                             ‫سباروك‬

‫سما کچه ‪ = ۲‬باکاف » پروژن ومعنی‬                             ‫آ ن روبد ‪ -‬و بمعتی خاك شور‬                      ‫ال‬
                                                                                                             ‫مهثو‬
                                                                                                                ‫ارک‬
                                                                                                                  ‫س‬
        ‫سماخجه است که سیئه‌بند زنان باشف‪.‬‬                                ‫و شوره زار وزمین بی حاصل هم هت ‪.‬‬

 ‫سمان = بفتح اول بروزن کمان» مخفف‬                            ‫سمار و ك ‪ -‬م رای بی‌قطه وسکون‬
‫وفتم بود‬‫اسمان است ‪ - ۸‬و لام روز بيست ه‬                         ‫بتریبا‌شدحومام‬
                                                                            ‫ربو‬
                                                                              ‫عی ک‬
                                                                                 ‫بعن‬
                                                                                   ‫؛ بم‬                          ‫کواوف‬
                                                                                                                     ‫وا‬
                                                                                                                     ‫خوالند ‪.‬‬
 ‫ازهرماه شمسی ‪ - 4‬و بکسر اول نام شهری‬
                                     ‫باشد ‪۰ ۹‬‬    ‫ومدنه‌ای‬    ‫صم اول‌بروزن بغاری» کشتی‬                  ‫سماری‬

‫| سمانه‬   ‫‪۰‬حصفف‬   ‫زمانه‬   ‫بر ورن‬          ‫سما نه ®‬
                                                                 ‫و جپاز راگوبند و بعربی سفینه خوانند ‪. ۷‬‬
                                                             ‫ع بتحتالی‬  ‫بو‬ ‫ارل‬‫رح ا‬
                                                                                 ‫سمار یی ‪ -‬بفت‬
                                                            ‫بنیقطهٌ (‪ )۱‬زده» بونالی نام‬                      ‫ن‬
                                                                                                             ‫یو‬‫سده‬
                                                                                                                 ‫کشی‬
 ‫کرك‬
   ‫ونرا بترکی بلدرچین‌وبلغت دریگ‬
                               ‫کوچك آ‬
                                                              ‫لوعی از ماهی باشد و آنرا !هل مغرب صردین‬
‫دارد ‪ -‬وبهندی نام شهر بست درهندوستان‪ ۳۱‬که‬
                                                                                                                 ‫کوند ‪. ۳‬‬
                                                             ‫سم افگندن » کنابه از لنگه شدن‬
                                                                                                                      ‫باشد ‪9.‬‬
```


## [2026-09-06T15:53:30.587Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nimport re\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor n in (594,595,596,597,627):\n    p=t[n]\n    print('LEAF',n,'nums',re.findall(r'[۰-۹]{3,4}',p)[:6])\n    print(p[:500])\n    print('....')\n\""
}
```


### [2026-09-06T15:53:32.804Z] TOOL RESULT

```
LEAF 594 nums ['۳۱۱', '۳۰۳', '۵۳۲۷', '۹۷۲', '۹۳۷', '۳۳۱۱']
   ‫‪۰‬؟(‪-۳۱۱‬‬                               ‫‪o‬‏‬    ‫‪«.‬‬                                    ‫فاون‬
                                                    ‫وسر خای‬
                                                          ‫سرو خشت ب=فتح اول ک‬
 ‫درخت سرو بسار بود ‪ -‬و نلم لحن دهم است‬
‫ازسی لحن باربد ‪ - ۴‬و نامقصبه ایست درملك‬             ‫شخصی را مخنی گوبندیا ازروی مهربالی اسیحتی‬
                                   ‫فاری ‪© .‬‬
                                                             
....
LEAF 595 nums ['۱۱۲', '۷۵۱', '۸۵۱', '۲۳۱۱']
                                                                                           ‫—‬     ‫لس‬
   ‫"روش‬


 ‫کال سال شممی بنام ابدان موسوم‌شده ‪» ۴‬وهر‬
 ‫یك آزین دوازده سروش بتدییر امور و مصالح‬                ‫پیغامآور بعاشمدوما ‪ -‬و مطلق فرشته رلایز‬
‫ماهی که هم نام اوست ممین‌است وهمچنین ندییر‬             ‫فری‬   ‫کفنته‌اند و بعربی ملك خوانند ‪ .‬وحکمای‬

  ‫کیانه‬ ‫امور و مصالحیکهدرهربك از روز های س‬             ‫کوبن دکه حق تعالی سی و پنج سروش آفربده‬
 ‫واقع میشود حواله بسروشی اس
....
LEAF 596 nums ['۸۸۰', '۵۵۳', '۷۳۷', '۷۳۲۷', '۹۷۳', '۷۴۱']
  ‫‪۱۳‬‬                                                                                        ‫سروشه‬

                                                         ‫و مصالع آن رو" بدو مقرر است خودهم بتدبیر‬
 ‫وح‌اول بمعنی‌سرین است که شت‌گاه‌مردمان‬            ‫=‬     ‫ومصالح آن‌روز می‌پردازد‪ .‬بنابرآن بجهت‌شرف‬
                         ‫وکفل چاربابان باشد ‪۰ ۴‬‬        ‫آن روز راعد کنند وجشن سازند » ولیزهر کدام‬
 ‫وتا‬      ‫ر‬     ‫کاله‬       ‫ك‬        ‫سر ونار‬             ‫از سروشها بمحافظت 
....
LEAF 597 nums ['۷۲۸۸', '۱۱۳۹']
  ‫صری‬                                                                                 ‫ه‬
                                                                                      ‫ا‪۱‬‬‫‪۳۱‬‬
                                                                                         ‫‪-‬‬


 ‫سر هنګ رک بروزن‌فرهنگه ؛سردار‬                     ‫پوسندیده و برگزبده واعلی وفیس باشد چذان‬
‫پویشرو لشکر و سیاء باشد» چه هنگه بمعنی‬            ‫وعبیدب‌دار را یابه گویشد‬ ‫که هرچیز زیون و‬
‫سپاه لیز آمده است ‪
....
LEAF 627 nums ['۲۵۱']
  ‫سماررغ‬                                                                            ‫اعد‬   ‫‪۳‬‬

                                                    ‫أست» وآن نام مقامی است از جملهٌ دوازده مقام‬
  ‫زرن‬
    ‫و ب‬
      ‫سلینون ‪ = ۴‬بفتح اول و اون‬
‫فربدون » بلفت بودالی رستنیی باشد که بیشتر‬           ‫که آن بزر که وبوسليك وحجاز وحسینی‌وراست‬
                                                    ‫و رهاوی ر زنگوله و صفاهانڭ و عراق و عشاق‬
‫درآ های استاده روبد و آلرا بعربی جرجیرالماه‬
          
....
```


## [2026-09-06T15:53:44.460Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nimport re\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\np=t[627]\nprint(p)\n\" | sed -n '1,80p'"
}
```


### [2026-09-06T15:53:46.390Z] TOOL RESULT

```
  ‫سماررغ‬                                                                            ‫اعد‬   ‫‪۳‬‬

                                                    ‫أست» وآن نام مقامی است از جملهٌ دوازده مقام‬
  ‫زرن‬
    ‫و ب‬
      ‫سلینون ‪ = ۴‬بفتح اول و اون‬
‫فربدون » بلفت بودالی رستنیی باشد که بیشتر‬           ‫که آن بزر که وبوسليك وحجاز وحسینی‌وراست‬
                                                    ‫و رهاوی ر زنگوله و صفاهانڭ و عراق و عشاق‬
‫درآ های استاده روبد و آلرا بعربی جرجیرالماه‬
                                                                           ‫روچك و نوا باشد ‪.‬‬
                                                                                           ‫ک‬
‫وکرفس الماء وفرةالمن کویند‪ .‬ب رکهآن‌س رکه‬
           ‫نمناع ماند لیکن بزر کتر ازآن است ‪.‬‬
                                                ‫سلیما نی ‪ -‬نوعی از خرمای سفیدباشد‬
                                                                    ‫‪ -‬وسنکی هم حست مشهور ‪۱‬‬




‫سماخچه ‪ = ۷‬بفتح اول وسکون خای‬                          ‫رنیو‪,‬ف‬
                                                            ‫عن ا‬
                                                               ‫مسکو‬
                                                                  ‫سم ‪ -‬بطم اول و‬
 ‫نقطه‌دار بر وزن تفارچه ‪ ,‬مخفف ساماخجه است‬
                                                    ‫است که سم اسب و استر و خروکاو و کوسفند‬
                       ‫که سنه‌بند زان باشد ‪.‬‬                       ‫و امثال آن باشد واین بمنزلةٌ‬
‫سماروخ ‪ ۸‬۔ بارای بی قطه بواو‬                                        ‫ناخن‌است نآها را ‪ ۴‬و‪-‬بمعنی‬
‫»ستنیی باشد که‬
             ‫کشده و بخای نقطه‌دار زده ر‬                            ‫پای همآمده است که بعربی‬
‫آنرا خابه دیس گوبند چه بتخم مرغ می‌مالد‬                             ‫واییرا یز‬ ‫رجل خواند ‪ -‬ج‬
 ‫و کلاه دیوان هخموانند ‪ .‬از زمینهای لمناك‬
                                                         ‫سم‬         ‫گو ند که در زمین با در‬
‫و دیوارهای حمامها روید ودر صبحرآهانیز میباشد‬
                                                    ‫کوه بکنند ‪ ۴‬و چنان سازند که در درون آن‬
 ‫وچه در‬
      ‫آونچه در صحراها روبد میتوان خورد ن‬
‫‏‪e‬‬
‫هر ‪ 2‬آن حجلای صر دهد‬         ‫لمی‌خور ند ‪ .‬گنت‬
                                                     ‫توان استاد و خواید همجنانکه مرتاضان‬
                                                     ‫و درویشان از برای خود و چوپانان بجهت‬
                     ‫و عوام آ را چترمارگوبند‪.‬‬       ‫کوسفندان سازند و‪-‬یفتح اول ‪٩‬‏ در عربی زهر‬
                                                                                     ‫را گوید ‪.‬‬
 ‫سماروع* = باغین نقطه دار ‪ ۰‬بروزن‬
                                                                              ‫سماچه ‪۹‬‬
‫و هعنی سماروخ است» وآن رستنیی باشد که در‬            ‫»ینه بند‬
                                                           ‫= بروزن سراچه س‬
‫دبوارهای حمام و زمینهای لمناك و زبرهای خم‬                                           ‫زارا گونشد‬


                                                                    ‫(‪ )۱‬چش ‪:‬روید ‪.‬‬

  ‫‏‪ Cala nine = ۱‬یزد« ‪۲:۲۵۱‬ص‪+‬ج ‪ ۴ ۲‬یناوب‪ < 5611800 -‬ساگنیتشا * ‪.‬‬
   ‫‪ ۴‬س=نب = سمب » پهلوی ‪ , 0010۱5‬ارمنی ‪ , 120۵0۹‬کردی ع‪ , 0015‬اففانی ع‪0712‬ا‪.5‬وخی‬
   ‫و یکلی ع ‪*5 01‬اسشق ‪ ۷ 4‬در پارسی‌باستان ‪ 2910711150‬با‪503111 80-‬درسانکر ‪i_a‬‏ ‪hbmuço‬‬
   ‫»ردیع‬
       ‫‪- ۴‬کردی ‪ 811003‬ک‬             ‫»معرب‪:‬سنباك ‪.‬‬       ‫‪000‬‬
                                                          ‫‪*۷9‬؛‬‫یه»‬
                                                                ‫کمان‬
                                                                   ‫لوبش‬
                                                                      ‫ی‪«80‬ه‬
                                                                          ‫گ‪0]1‬‬
                                                                             ‫با ‪10 -‬‬
  ‫‏‪ sûmb‬ر ‏‪ , sum bden , sumbagh , sumb‬یچرلب (ءان )عاروس( ‪:‬یسرافزا‪ ,‬نتقس‬
   ‫‪٩‬‏ ‪ -‬ونشدید دوم ‪ .‬رك ‪ :‬منتهی‌الارب و شرح قاموی ‪.‬‬         ‫«اسشق ‏‪ “۷٤٦‬ورك ‪ :‬هوبشمان ‪. ۹4۷‬‬
                  ‫_ رك ‪ :‬سماچه » سماکچه ‪.‬‬               ‫رك ‪ :‬سماخچه » سماکچه ‪.‬‬       ‫‪۱‬‬
                                ‫‪٩‬‏ = سماروخ (هم‪. ).‬‬             ‫‪ = ۸‬سماروغ (هم‪. ).‬‬
```


## [2026-09-06T15:54:06.940Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nimport re\nfor f in ['BQT_v2_pages.txt','incoming/BQT/BQT_v3_pages.txt']:\n    try: t=open(f,encoding='utf-8',errors='replace').read().split('\\f')\n    except Exception as e: print(f,e); continue\n    for n,p in enumerate(t):\n        for m in re.finditer(r'سپل|شفل|سفل ', p):\n            s=p[max(0,m.start()-120):m.start()+200].replace(chr(10),' ')\n            print(f,n,repr(s))\n\" 2>&1 | head -20"
}
```


## [2026-09-06T15:54:07.828Z] TOOL CALL #57: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B3%D9%BE%D9%84",
 "prompt": "Persian سپل: is there an entry? give meaning and etymology if present."
}
```


### [2026-09-06T15:54:09.016Z] TOOL RESULT

```
BQT_v2_pages.txt 74 ' نام خود را بر آن نفش\u202c        \u202bاز بادشاهان\u202c                                                  \u202bجافه ه بر وزن شانه \u202a,\u202cفك اسفل باشد \u202a۱\u202c\u202c  \u202bکرده بودورایج گردانیده چ\u202a٠\u202cو\u200fن\u200cمردم ذربایجان\u202c        \u202bونرا\u202c                                                       \u202bکه موضع رش برآوردن و غبغب است آ\u202c \u202bحربی ذقن گوبند \u202a - ۴\u202cوکلولةً خمیری '
BQT_v2_pages.txt 107 ' \u202bویمعتی\u202c     \u202bباشد \u202a -\u202cو معدوم ونابود را همکفته\u200cاند\u202c   \u202bوگرز باشد از پی\u200cهم \u202a - ۸\u202cوصدای برهم خوردن\u202c                \u202bفك اسفل هم هست که چانه و زشدان مردم\u202c  \u202bویند \u202a 7-7\u202cوضم هر دوجیم فارسی »\u202c                              \u202bگز\u202c\u202bدندان را ن\u202c               \u202bوحیوانات دیگرباشد \u202a -\u202cو بترکی\u202a ۴\u202cامربکشیدن\u202c  \u202bسخنی و خبری را (\u202a )۲\u202cگوین'
BQT_v2_pages.txt 124 '۰\u202cمخفف چانه\u202c                                                 \u202bزنگیان \u202a,\u202cوجمد تقیض\u200cسبط است\u202a .\u202cوسبط موبی\u200cرا\u202c  \u202bاست که فك اسفل آدمی و حیوانات دعگر\u202c                                          \u202bکویند کهتارهای آن مطلفاً پیچ و خم نداشته\u202c      \u202bباشد \u202a - 4\u202cویکراول مخقف چننه ودانة مرغان\u202c                                            '
BQT_v2_pages.txt 221 'ایوش»\u202c                                                                                   \u202b\u202a4\u202cھ\u202c       \u202b\u202a۰\u202c\u202c     \u202bغوغا ومشفله وغلفله را\u202c            \u202bشور و\u202c    \u202bو\u202c    \u202bفتنه و آشوب\u202c                                                                           \u202bخلاش = بفتح اول بر وزن لواش \u202a.\u202c\u202c \u202bگو ند\u202a۷١\u202c\u200f ¦ و بانتمعنی بجاىلام '
BQT_v2_pages.txt 241 ' \u202a :\u202cخوالك \u202a.\u202c\u202c          \u202b\u202a۰\u202cص\u202a.\u202c\u202c           \u202b\u202a۲ :۹!۱\u202c\u202c                \u202b\u202a - ۱\u202cاز \u202a :\u202cخوال (= خوار) \u202a +\u202cکر ( یوند فاعلی وشفلی ) رکه\u202a :\u202cاسفا\u202c                                          \u202b\u202a -\u202cابن آفروشه\u200cاست\u202a ,\u202cدوزاغ است خوالگرش\u202c                 \u202bهر دو قرین بکدیگر وليك در خورند\u202a.\u202c\u202c      \u202b\u202a ۶\u202cناصرخسرر بلخی \u202a.*۸۱۱\u202c\u202c \u202b\u202a-\u202cاوزا\u202a:\u202c'
BQT_v2_pages.txt 241 '    \u202b\u202a = ۴\u202cخوال ر\u202c                                                 \u202b\u202a0\u202c\u202c                                              \u202bوشفل) = خوالگر\u202c             \u202bبدیبا وخوالیگران خواستند \u202a.\u202c\u202c                                  \u202bیکی خانه او را بباراستند\u202c      \u202bفردوسی طوسی\u202a *.\u202cلغت فرس> \u202a۳۱۰\u202c\u202c      \u202b» کردی ع \u202anãx\u202c\u200f »افغانی \u202anaVX\u202c\u200f\u202c      '
BQT_v2_pages.txt 285 '                               \u202bمعد \u202a.\u202c\u202c         \u202bص\u202a۲۰\u202c\u202c                                                               \u202bشفل دییر ؛ عمل در \u202a -\u202cرك\u202a :\u202cفاب \u202a۱\u202c\u202c '
BQT_v2_pages.txt 287 'حیحعلامهدهشدا) \u202a.\u202c\u202c   \u202b© \u202a -\u202cرکه\u202a :\u202cاسشق وهوبشمان \u202a.4۲۵\u202cبهلوی\u202c         \u202b\u202a - ۴\u202cاسم مفعول از «دختن» (هم\u202a. ).\u202c\u202c  \u202b\u202a( 11520\u202cشفل\u202a,\u202cتکلیف) قی\u202a:\u202cارستا هتکن (آلت\u202a,\u202cایزار) «بارتولمه\u202a»٩۷۷\u202c\u200f وممکن است از\u202c              \u202b\u202a( 01:2\u202cشان \u202a ,\u202cعلامت) «بارتولمه \u202a۹۷٩\u202c\u200f مشتق باشد « نریبکه \u202a٩4۰\u202c\u200f \u202a.\u202c\u202c \u202bاوستا \u202a2\u202cشا\u202c   \u202b\u202a۰07۳1۵0\u202c\u202c              '
BQT_v2_pages.txt 303 '\u200f «لك \u202a ۲\u202cص “\u202a1A\u202c\u200f \u202a.\u202c\u202c               \u202b\u202a ۷\u202cسکر\u202a :\u202cدرفش \u202a.\u202c\u202c  \u202b\u202a 0\u202cدرو دگر\u202a -\u202cصم اول وقتح پنجم » از\u202a :\u202cدرود \u202a +\u202cگر(یسوند شفل) رك \u202a :\u202cدروده در و گر\u202a.\u202c\u202c   \u202b)\u202a .\u202cبهلری \u202a 80۳0\u202cم«نای \u202a> ۲۷۲\u202c\u202c           \u202b\u202a 2\u202cدروغ \u202a -\u202cنم اول ودوم » ( تلفظ قدیم \u202a0\u202c\u202c   \u202b\u202a۳۰0\u202cو\u202a . 8۵\u202cاز بارسی باستان \u202a . 28112۳-1\u202cاوستا \u202a« 20802۲-1\u202cبارتولمه\u202c      \u202b'
BQT_v2_pages.txt 344 '\u202bو آنر! حب\u200cالخطای وحب\u200cاللاطین خوانند \u202a ۴\u202c؛\u202c         \u202bاصاری شود \u202a -\u202cو دام روز ششم کالون ال خر هم\u202c \u202bیکدانگ آن مسپل رطوبات\u200cبود \u202a -\u202cوکنیاامهی\u200cهم\u202c                                                 \u202bهت \u202a.\u202c\u202c \u202bهست\u202a -\u202cوقسی\u200cاز کدابان باشند که شاخ گوسفندی\u202c        \u202bدند = بفتح اول بروزن چند» استخوان\u202c    \u202bرت رکی چم ک>ا\u202c \u202bبر'
BQT_v2_pages.txt 393 ' :»۰۱\u202cکخرادرنج»ببرون کرد \u202a-\u202cن دکقردعنه اغراجبلدکردن\u202a ,\u202cمرکدورددن۔\u202c  \u202b\u202a ۰\u202cاعتغال داشتن \u202a;0D\u202c\u200f هیچ حال ننده بدرگاه تباید وشفل وزارت براند که\u202c                 \u202bورزسن\u202c    \u202bآوردن ك\u202c   \u202bاسهال\u202c                                        \u202bاستضفاف چنن قوم کشیدن دشوار است » « تاریخ بیهقی \u202a٩۵۱\u202c\u200f * \u202a.\u202c\u202c '
BQT_v2_pages.txt 486 '\u202c                                                                             \u202b( دندان » اسنان ک\u202c    \u202b«* زفر زیرین» فك اسفل است و «زفر زبرین» فك اءلی \u202a « :\u202cهر حیوالی بوقت خاییدن زفرزبرین\u202c    \u202bجنباند و \u202a,\u202cیکی مخالف بود چنانك تماح زفرژیرین جنباند وزبرین لجنباند> «دابشنامه \u202a۳4۲۰\u202c\u202c '
BQT_v2_pages.txt 598 '\u202c   \u202bخلیفه » مرخ سقارا گویند» وآن پردماست که\u202c \u202bسر یرفلك \u202a -\u202cکنابه از بنات\u200cالنش\u202c                                  \u202bدرفك اسفل او بعثی درزیر منقار زبرین\u200cآوپوستی\u202c                                                                                    \u202bبمالند مشگیجه آوبخته است\u202c \u202bصورت\u202c        \u202bستاره باشد شمالی\u202c          \u202bاست» \u202a 3'
BQT_v2_pages.txt 607 '           \u202b\u202a - ۴\u202cدرزبان کنونی یز \u202a 1665\u202cگویند ورك \u202a :\u202cسفته \u202a.\u202c\u202c                                \u202b( سفتن ) \u202a -۴\u202cکر( یوند شفل ومبالفه )\u202a.\u202c\u202c        \u202bت\u202c                                                                           \u202bفز \u202a:\u202c\u202c                                                                              \u202bس_ ا\u202c\u202b©\u202c  '
incoming/BQT/BQT_v3_pages.txt 40 'شپ ببین کوه جودی عاجز \u200eaT\u200f پیش ابشان از ثبات .  \u200fمولوی بلخی رومی. « فرهنگه نظام».  \u200e٩\u200f رك : شش \u200edet » che dV\u200f ۲ - راك : سپل . ۸ - طبری \u200eshoppol\u200f \u200f(سوت) « واژه نامه ۷۲ 4 - 1 شیل .  \u200f*- چون سزای \u200echet\u200f تو دوات شه پست کرد شاه را دولت چنان بابد ترا شپلت چنین .  \u200fسنایی\u200cفزدوی. «فرهتکه \u200e«tells\u200f \u200f۴ شپیلیدن(ه.م.) . ۱۳ د  \u200fشپیخت'
incoming/BQT/BQT_v3_pages.txt 41 ' ۴ \u200eShapire jo\u200f پهلوی \u200eVeh\u200f \u200fبه ونيك «دهارله ۲۹۲ و \u200edy\u200f بونکر۸۲؛ باروچام۲۳. ۴ ره \u200eSets\u200f مشیلت . \u200ede = 8\u200f (هم). ۱ - قی : سپلشپل . ۷ - مذارع * شپیلیدن» .  \u200f۸ - اسم فاعل از «تییلیدن» + \u200e٩\u200f - از : ثپیل ۳ یدن (یسوند مصدری ). ۷۰ — کلابی\u200cصفت بر جفابگذرو که کلراثپیلند و آ ش بر ند. امیرخرودهلوی.«فرهنگه:ظام». 0 مشفف «شتل» («.م.)'
incoming/BQT/BQT_v3_pages.txt 63 'لی بر وزن مسك۴\u200e - CMe - ۴ \u200fبیپتر و ابله و جلف و دادان را توبند\u200e \u200fو بسکون ثانی بسمت ی کهنه وفرسوده و ازهمرفته\u200e . \u200fباشد\u200e  شفل ۴ \u200epte\u200f اول بروزن \u200eIS\u200f * ناخن شتران بار کش راگونند \u200f  شقلج = تم \u200eSol\u200f و لام و سکون \u200ewt\u200f \u200fو جیم , مبوة کبر است وآنرا بتیرازی \u200eBaF\u200f \u200fوحربی تمرةالکیر وئمرة الاصف خوانند.  نفلیدن °- جنم\u200cاول برروزن\u200cخشک'
incoming/BQT/BQT_v3_pages.txt 76 'ه است که \u200ept\u200f \u200fو کوسفند و گاو از \u200eglo\u200f برآورند و بجاوند = و \u200eSG\u200f اول \u200eGEE\u200f و سوراخهای عمیق را گوبند که در زمین سیب \u200ebe\u200f سپلاب بهم رسیده \u200eVash\u200f - و چداری که بر دست و پای اسبان هند ؟ .  شگاله  \u200ece\u200f اول بر وزن حواله . بمعنی تمام وهمه باشد ۴ .  شگالیو ۴ هت پم اول و \u200eog\u200f دابع و تحتالی بواو رسیده » هرچیز را گوند که بر روی اخ'
incoming/BQT/BQT_v3_pages.txt 86 'آلاثار آلارامية فی لفة الموصل العامية س \u200e۵٩\u200f » شماس ها ) دیکان\u200cها \u200eDeacons\u200f ) درسازمان کلبا , گروهی از روحایان بودند که شفل آنان توجه بفقرا بود وبمد ها کشیشان را کفتند ( تاررخ\u200cکلیسای قدیم در امپراطوری روم وابران .وم. میلر . ترجمةً علی\u200cبضتین ۱۹۳۱.ص ۰۱۳۹ ۱۳۷ - ۰۱۳۹ ۲۸۳۰۱۷۹ وغیره) : بناقوی و بزتار و بقندبل بیوحنا و شماس و'
incoming/BQT/BQT_v3_pages.txt 90 'کرد , عاطل گذاشت) » عری سبت ( استراحت کرد ) و \u200ele\u200f (قطع کردآنرا) وآن از هسب» \u200ecol\u200f بممنی قطم واستراحت متوقف برانقطاع از شفل دولد تب . همین کلمه است که در عربی سبت « شنبه » و در فراسوی \u200eSamedi\u200f و در آلمالی 8 نشد. . \u200eH. Zimmern, Akkadische Fremdwérter. Leipzig. 1917. s.67.\u200f ورك :یشنها . پورداود ج ۷ ص \u200e۷٩\u200f ؛ ممجمیات عربیه'
```


### [2026-09-06T15:54:11.099Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-06T15:54:36.429Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== WLD ctx ===\"; sed -n '32595,32615p' incoming/WLD/WLD_Bd1_pages.txt; echo; echo \"=== IEC kapho ===\"; grep -n \"kapho\\|kopho\\|k'apho\" IEC.txt | head -5; echo \"=== SYN hoof ===\"; grep -n -i \"hoof\" SYN.txt | head -8"
}
```


### [2026-09-06T15:54:36.515Z] TOOL RESULT

```
=== WLD ctx ===
ist.    Eher konnte die Wz. qap- von lit. kapoti „hacken, hauen", gr. y.dnerog
346                       kapho-, kopho   qap-ut,   -(e)lo-



                                                                                    I£
,,Grube“ usw. zugrunde liegen als „gerodetes und gegrabenes Grundstiick
(Yf.   LEWb. 2 u. capio u. scapulae), doch auch dies ganz unsicher.

kapho- oder kOpho- „Huf“.
  Ai. gapha-   m. „Huf, Klaue“, av. safa- m. „Huf des Pferdes“.
                ags. kof ahd. huof „Huf' (z. B. Pick l 4 43, 206, 420, Falk-
                                          £
  Aisl. hcfr,
Torp u. hov I). Ksl. russ. (usw.) kopyto „Huf££ am ehesten mit Uhlenbeck
Ai. Wb. 303, Berneker 565 zu slav. kopati „graben, auch mit dem FuBe
aufstampfen“ (siehe *sqap- ,.graben, hacken“), kaum mit Zupitza KZ. 37,
401 zu gaphd       huof unter Annakme westidg. Gutt. -yto, obwohl nicht
                                                              ;



=== IEC kapho ===
=== SYN hoof ===
5564:4.20 HHAD Grk. _xedady, xapa (poet.) Goth. haubip Lith. galva NG Kepare ON hofud, haufud Lett. galva Lat. caput Dan.  hoved ChSl. glava It. testa, capo Sw. huvud SCr. glava Fr. léle OE héafod, hafela Boh.  hlava Sp. cabeza ME __heved, hed Pol. glowa Rum. cap NE head Russ. golova Tr. cend, cenn Du. hoofd Skt. ¢iras-, cirsan-, NIr. ceann OHG = houbit mitrdhan- W. pen MHG houbet, kopf Ay. sarah-, sdra-, vayda- Br. penn NHG kopf, haupt na-, kamaraéa-
5583:6. ON hofud, etc., above, 2. The more widespread forms with diphthongal first syllable, Goth. haubip, ON haufud, OE héafod, ME heved, NE head, Du. hoofd, OHG houbit, NHG haupt, are ex- plained by some as a blend of this group
5683:k. éremrov Goth. Lith. kakta a Meee xobredo ON enni Lett. piere Lat. frons Dan. pande ChSl. éelo It. fronte Sw. panna SCr. elo Fr. front OE Sorhéafod _ Boh.  &elo Sp. _ frente ME _forhe(ue)de Pol. _—_czolo Rum. frunte NE forehead (brow) Russ. lob (“elo) Ir. étan, tul Du. voorhoofd Skt. bhala- Nir. clar a éadain OHG - stirna, linna, andi Av. ainika- W. talcen MHG stirn(e), tinne Br. tal NHG  stirn
5693:forehead, Du. voorhoofd, cpds. of words for ‘fore, front’ and ‘head’,
6243:It. gamba, Fr. jambe (OSp. camba), fr. late Lat. gamba ‘hoof or hock of a horse’, orig. only a veterinary’s term, then ap- plied to persons; this from Grk. cap ‘bend’, used in Aristot. for the joints of
6312:OPruss. nage ‘foot’, Lith. naga ‘hoof’, all | Barth. 765.
16097:Dan., Sw. behov, fr. MLG behof = Du. behoef, OF behof, NHG behuf, ‘use, ad- vantage’. Du. behoefte fr. behoef, with same development of ‘need? fr. ‘what is of use’. So OF behofian ‘have need of”, later ‘be proper’ (NE behoove). All ulti- mately : Goth. hafjan ‘raise’, Lat. ca- oe ‘take’, etc. Cf. NHG brauchen Tine ase eS a also ‘need’. Falk- iehoof » 300. Heliquist 61. NED s.v. aa va, reikalas, fr. reikia ‘is neces- rot cone A OLith. reika ‘necessity’,
```


## [2026-09-06T15:54:39.278Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KNT kabul ===\"; grep -n -i \"kabul\\|kāpul\\|kapul\" KNT.txt TLM.txt | head -5; echo \"=== PHD kabul ===\"; grep -n -i \"k'pwl\\|kabul\\|kābul\" PHD.txt PHD_mackenzie.txt NYB_vol2_glossary.txt | head -5; echo \"=== MON کولی ===\"; grep -n \"کولی:\" MON_part1.txt MON_part2.txt | head -5; echo \"=== KLN hoof ===\"; grep -n \"^hoof\\|hoof,  n\" KLN_1966.txt | head -3"
}
```


### [2026-09-06T15:54:39.392Z] TOOL RESULT

```
=== KNT kabul ===
=== PHD kabul ===
NYB_vol2_glossary.txt:2271:Kavatan patr. of Kavāt 10921, 1138, 1149. Kavul [k*pwl; inser. k’wly] Kabul P2: 2. 11; 9% 17°. 317. 115%,
NYB_vol2_glossary.txt:3681:*Tab [t?b] the name or the title of the king of Kabul 17°. — Cf Tābān, the capital of the country of Kabul, Yàqüt 3,454, v. Erangahr 299. Another possible reading would be Tai [t'd], Chinese t'a? ‘great’
PHD_mackenzie.txt:3196:kapur [k'pwl I Ar. hafur] camphor.
=== MON کولی ===
MON_part2.txt:23673:کولی: (گیا.) موی زکک. 
MON_part2.txt:28274:کولی: 0۳ ,-۸۷۱ [- کاولی - کابلی؟] 
MON_part2.txt:28277:کولی: 1+ (حامص.) سواری روی کول و 
MON_part2.txt:43901:ریزه کولی: (جان.) یکی از گونه‌های شکگکك 
MON_part1.txt:56268:خروس‌کولی: آ[۵۳۵۶-0۷ (امر .) (جان.) 
=== KLN hoof ===
4684:Derivatives:  beholden  (q.v.),  behold-er,  n. beholden,  adj.  —  Prop.  pp.  of  behold,  used  in  its earlier  sense  as  ‘held  by,  attached  to’, behoof,  n.  —  ME.  behof  (ch\ef\y  in  the  dat.  behove with  the  prep,  to,  ‘for  the  use  of’),  fr.  OE.  behof. ‘profit,  benefit,  advantage,  need’,  rel.  to  OFris., MLG.  behof,  Du.  behoef,  MHG.  behuof,  G. Behuf  ‘benefit,  use,  advantage’,  Dan.  behov, Swcd.  behof,  ’need,  necessity’,  and  in  gradational relationship  to  E.  have  and  heave, behove,  tr.  and  intr.  v.  —  ME.  behoven,  fr.  OF.. behofian,  ‘to  need,  require’,  fr.  behof.  See  prec. word.
18040:Derivatives:  hoodwink,  n.,  hoodwink-er,  n. hoof,  n.  —  ME.  hoof,  fr.  OE.  hof,  rel.  to  OS., OFris.  hof,  ON.  hofr,  Dan.  hov,  Swed.  hof,  Du. hoef,  OHG.,  MHG.  huof,  G.  Huf,  ‘hoof’,  and cogn.  with  OI.  saphdh,  ‘hoof’,  Avestic  safa-, ‘hoof  of  the  horse’.
```


## [2026-09-06T15:54:49.215Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '28270,28285p' MON_part2.txt; echo \"=== کابلی ===\"; grep -n \"کابلی:\" MON_part1.txt MON_part2.txt | head; echo \"=== کابل: ===\"; grep -n \"^کابل:\" MON_part1.txt MON_part2.txt | head"
}
```


### [2026-09-06T15:54:49.325Z] TOOL RESULT

```
کوله‌بار: ۰-۲ | - کو لباره - کوله‌باره| 
(امر.) باری که بر پشت کنند. 

کولی: 0۳ ,-۸۷۱ [- کاولی - کابلی؟] 
(ص‌نسه.) غر شمال, ارقه. فاحشه. 

کولی: 1+ (حامص.) سواری روی کول و 


۵ مه 


شتا 
کولی خانه: (0-)2۸. (امر.) خانه کو لیان. 
جای پر ازدحام و هیاهو. 
=== کابلی ===
MON_part2.txt:35103:آ تاکن بیر کابلی: ( کد.) دنیاه جهان. 
MON_part2.txt:90897:یکی از گونه‌های هلیله. هلیلهٌ کابلی: (گیا.) 
=== کابل: ===
MON_part2.txt:16805:کابل: ا (.) مفتول فلزی لفاف‌دار و سیم
```


## [2026-09-06T15:54:58.817Z] TOOL CALL #61: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/%C4%87ap%CA%B0%C3%A1s\" \\\n \"https://en.wiktionary.org/wiki/%D8%B3%D9%85\" \\\n \"https://www.etymonline.com/word/hoof\" \\\n \"https://en.wiktionary.org/wiki/%CE%BA%CE%AC%CF%80%CF%80%CE%B1%CF%81%CE%B9%CF%82\" \\\n \"https://www.etymonline.com/word/caper\" \\\n \"https://en.wiktionary.org/wiki/Kabul\" \\\n \"https://en.wiktionary.org/wiki/%DA%A9%D9%88%D9%84%DB%8C\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"pdf page 241 verification (Kapho hoof / Kapparis caper / Kapul Kabul)\" 2>&1 | tail -2\ndone"
}
```


### [2026-09-06T15:55:03.709Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/8fc7b48ff97aae64.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f435c284502488d0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a5340273a974271c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3d4009a2ac1a1e61.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/2e180f0ff5cbb000.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/420d6d151b3ed602.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f3a377ea8f1c210f.txt
```


## [2026-09-06T15:55:13.648Z] TOOL CALL #62: Bash

```json
{
 "command": "sed -n '1,120p' tools/verify_check.py"
}
```


### [2026-09-06T15:55:13.689Z] TOOL RESULT

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


## [2026-09-06T15:55:22.115Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('leaves',len(pages))\nimport re\nfor n,p in enumerate(pages):\n    if 'caper,  n.,  a  prickly' in p:\n        print('leaf',n)\n        print(repr(p[:150]))\n        print(repr(p[-200:]))\n        break\n\""
}
```


### [2026-09-06T15:55:23.795Z] TOOL RESULT

```
leaves 903
leaf 134
'  chant),  ‘corner’.  See  cant,  ‘slope’, cantlet,  n.,  a  small  cantle.  — -  Formed  fr.  prec.\nword  with  dimin.  suff.  -et. canto,  n.,  chie'
':  capitulat-ion,  n. capon,  n.,  a  castrated  cock.  —  ME.,  fr.  OE.  capun, fr.  L.  caponem,  acc.  of  capo,  ‘castrated  cock" (whence  also  Gk.  xa7r<ov,  of  s.m.),  which  is  cogn. with '
```


## [2026-09-06T15:55:41.513Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nimport re\nt=open('incoming/BQT/BQT_v3_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('leaves',len(t))\nfor n,p in enumerate(t):\n    for m in re.finditer(r'کبر\\b|قبار|كبر ', p):\n        print(n, repr(p[max(0,m.start()-200):m.start()+300].replace(chr(10),' ')))\n\" 2>&1 | head -20"
}
```


### [2026-09-06T15:55:43.209Z] TOOL RESULT

```
leaves 721
3 'بئی بادداشتی شامل\u200cلفات فارسی و \u200ega\u200f اعلام فرستاده\u200cاند , وآقای \u200eShine\u200f آبتی از شیراز » سدادی لفات فارسی ومحلی ارسال داشته\u200cاند .  \u200fدر تدوین مجلد حاض ؛ از \u200edae\u200f اطلاع وحدس صائب استادان بزرکوار \u200eET\u200f علی\u200cاکبر دهشضدا وآقای ابراهيم \u200eoy\u200f داود \u200ewl\u200f پیش برخوردار بوده است .  \u200fاز آقای امیر حسن یز دکردی فارغ التصیل دورة دکتری ادییات که در مدت مسافرت کوتاه نگارنده باروپا وامریکا, \u200eplas gat\u200f چایی مجلد جاضر را از \u200edate\u200f ۱۹۸۳ ۱۷۲۲۱ صحیح کرده اند » سیاسگزار است .  \u200fدر خالمه , \u200eob\u200f دیگر ازخوانند کان ادیپ ودانشمند '
41 'چندن (سندل) که از زمان \u200ehy\u200f قدیم داخل فارسی شده باشد . شت \u200eth\u200f همنی درنوشته\u200cهای قدیم فارسی لبامده ودر \u200ehie\u200f \u200fجهانگیری که آنهم در هند نوشته شده \u200eob,\u200f نگردیده است . در همه فرهشگهاشت مخفف شتل ۰ مصطلح در قبار »بادشده\u200cاست.» «پوردآود.فاباص۳*ح» بمعنی حضرت\u200cدر «دبستان\u200cالمذاهب»(س۷۳) بکاررفته است. \u200f ۳٩-از:ريشة\u200f 020 درسانسکریتبمعنی خوردن\u200cاست.قس 6010 لائینی,آش فارسی (لفة مطلق خورش وامروزه غذای مخصوص),وناشتا \u200ePU)\u200f ای)خدآ ست \u200eoli,\u200f ص۲۲۳ متن\u200cوح1). # فتاپ - \u200e2G\u200f اول \u200eSen)\u200f مر\u200cکزی) مخفف اشتاب (ه.م.) ورگ : شتافتن '
63 '\u200fبیپتر و ابله و جلف و دادان را توبند\u200e \u200fو بسکون ثانی بسمت ی کهنه وفرسوده و ازهمرفته\u200e . \u200fباشد\u200e  شفل ۴ \u200epte\u200f اول بروزن \u200eIS\u200f * ناخن شتران بار کش راگونند \u200f  شقلج = تم \u200eSol\u200f و لام و سکون \u200ewt\u200f \u200fو جیم , مبوة کبر است وآنرا بتیرازی \u200eBaF\u200f \u200fوحربی تمرةالکیر وئمرة الاصف خوانند.  نفلیدن °- جنم\u200cاول برروزن\u200cخشکیدن» بممتی صفیر زدن باشد چتابکه (۱) کیوتر \u200eAh\u200f \u200fدر وقت کبوتر پرایدن\u200cیا مهتران بوقت آببدادن  جاسبان زنند +  شفتیی \u200eSe\u200f اول ونون بروزن\u200cمسکین, \u200eca\u200f بوفابی \u200eob\u200f مرغی است که آنرا بضارسی پوتیمار و غم\u200cخورك و بعربی'
90 ' داشته باشد - و بکسر اول و سکون \u200eBS git\u200f و سرین مردم و \u200ebly\u200f دیگر را \u200efa\u200f \u200fویاین معنیشتح اول هم کفته ند و باغنج\u200cمرادف ساخته\u200cاند۴ - و ماول وسکون\u200cلون, -رعربی لوعی  \u200e—\\eoo—  \u200fاز صدف باشد که \u200eUT\u200f توئیای اکبر خوالند و شیرازبان فصبكکوبنه - وترنجید کی و درهم شکتگی را ی زکفته اد ۵ .  \u200fشنحار = با جیم بروزن زدگار» معرب شنکار ۷ است که (۲) لوعی از سرخ مرد باشد \u200eLT,\u200f بعربی شجرءالدم و حناء \u200ead yall\u200f وعاقرشمما ومداللنج ند  \u200fشنك = بفتح اول بر وزن قند 6 \u200eMite\u200f \u200fمرغاترا ۷ خوانند (۳).  \u200fشندفه - بفتح اول بر وزن اشر'
128 '\u200eden\u200f بر وزن کلاب 1 اسطرلاب را کوبند و آن \u200eAT\u200f باشد که \u200ePot\u200f \u200fماخته آند و منجمان بدان ارتفاع کوا کب معلوم نت و گوبند \u200epeat rales\u200f علیه\u200cاللامواشع  \u200fن است.  \u200erey  \u200fبان  \u200fصلون \u200eJs! che\u200f بروژن زیون . موه کبر است که بفارسی کورز کویند . وآن رستنیی باشد شبیه \u200eBG\u200f (۱) کوسفند و خرلوب \u200eht\u200f \u200fهمان است و بمربی بنبوت خوانند . در دوثاب پرورد آن ادرار آورد و درسر که پرورده شکم  \u200evay \u200fخط\u200e cbs \u200fاز\u200e aly - Sl \u200fصلت\u200e \u200fاستواست با خط محور.که خط شمال وجذوب\u200cباشد\u200e \u200fو تفاطم یل شمالی و عیل جنوبی - وتفاطع\u200e — \u200fفلك تدوبر را یز'
158 'خشك - \u200epin\u200f خای شله\u200cدار .  \u200fکنایه از عاشق خسیس وردل و بی\u200cصدق و لیتالی باشد .  \u200eLats \u200fسگ چان = کنابه از\u200e gale \u200fباشد.\u200e La \u200fطلبان و طالبان\u200e  \u200fعاقول = با فان \u200esly\u200f کنیده و بلام زده ؛ لوعی از خرنوب است که کبر باشد؛وبسنی . کوبند درخت ساج است .  \u200f# ع \u200e(ot)\u200f - حرف بیست \u200eGy\u200f ازالفبای فارسی وحرف هیجدهم از الفبای\u200cعربی(ابتث) و \u200eIT ue Oley\u200f هفتاد گیرند. در \u200eold\u200f فارسی این حرف نیامده و درلغات دخیل آکرا مانند (۱ء) تلنظ کنند . تلفظ این حرف در عربی از \u200eches\u200f کردن \u200eVe\u200f و پایین حلق بهم وبیرون  \u200fدادن هوا صور تگیرد '
171 ' Le\u200f بجهت خوردن خود و \u200eSlept\u200f خود میآورد ؛ و \u200egion\u200f کویند چیزست که\u200cدرمیان\u200cمل \u200elag\u200f میشود \u200eWT\u200f بشیرازی\u200cدارو میگوبندومگن نحل بجپت خوراله بچگان خود مبآورد \u200eOTA)\u200f \u200eGli culty\u200f میباشد ؛ و بعضی \u200eSay\u200f گویند عکبر وسخ الکبر است و \u200eWT\u200f مومیای \u200eghar\u200f خواشد وشیرازی برمو کویند. جرت کوفتگی\u200cوشکنگی اعناه \u200eAbu\u200f است.  \u200fعکعك ۴ - پنتم هردر عین و سکون هر در \u200eGE\u200f » بمعتی \u200eKe\u200f باشد وآن پرنده\u200cایست  \u200fمشهرر واو سفید و سیاه و درازدم میباشدوبعربی \u200ejute\u200f میگربند ؛ \u200egy\u200f گوند عقمق معرب عکمك است.  \u200eKa gio + \u200fبروزن فلك\u200e = ۴ SKE '
171 'خوردن خود و \u200eSlept\u200f خود میآورد ؛ و \u200egion\u200f کویند چیزست که\u200cدرمیان\u200cمل \u200elag\u200f میشود \u200eWT\u200f بشیرازی\u200cدارو میگوبندومگن نحل بجپت خوراله بچگان خود مبآورد \u200eOTA)\u200f \u200eGli culty\u200f میباشد ؛ و بعضی \u200eSay\u200f گویند عکبر وسخ الکبر است و \u200eWT\u200f مومیای \u200eghar\u200f خواشد وشیرازی برمو کویند. جرت کوفتگی\u200cوشکنگی اعناه \u200eAbu\u200f است.  \u200fعکعك ۴ - پنتم هردر عین و سکون هر در \u200eGE\u200f » بمعتی \u200eKe\u200f باشد وآن پرنده\u200cایست  \u200fمشهرر واو سفید و سیاه و درازدم میباشدوبعربی \u200ejute\u200f میگربند ؛ \u200egy\u200f گوند عقمق معرب عکمك است.  \u200eKa gio + \u200fبروزن فلك\u200e = ۴ SKE \u200fاست کهعکه'
210 ' \u200fو بسکون\u200e \u200fباشد ؛ و با جیم ابجد هم درست است . غلملیچ = بامیم . بروزن ومعنی\u200cغلفلیچ\u200e \u200fغلقا * - بنتح اول و سکون ثانی\u200cوقانی | است که خاریدن زبر بغل ویهلو و کف پای\u200cمردم\u200e . ۵ \u200fبالف کتیده , کياهی است شبیه بکبر و اج | باشد\u200e \u200fاول و ثالی بواو\u200e ae ٩ \u200fاست غلوفیر یا\u200e legs Mee \u200fکه وی کرد باشد و از\u200e  \u200eaim 9\u200f « «غانلج \u200ewh dads.\u200f یمنی\u200cآن که پهلوی کسی را با زیر کش, بر انگشت بکاوی وبجنبانی تا بخندد . لبیبی گفت : چنان بدانم من جای غافلیجگهشس کجابماش اول براوفتد برش ( بمالش اول فند \u200eaon\u200f . دهشدا ) \u200ecal?\u200f ۲ و \u200eYale\u200f'
303 'دس ۰ فینی()باشد ازجاب را یز کنته\u200cاند \u200eoT,\u200f هفت ستاره باشد در آسمان | حق \u200eUnde gl\u200f روح اعظمویدین فیض\u200cشئونات  بشکل چوکان وازجملةٌ چهل وهشت صورت\u200cفلك | ذانیه واعیان \u200ea\u200f ثابت کشتند .  nil \u200fفش\u200e Grey ۰ \u200fدب اکبر خوانند. فیض مقدس\u200e YT, col \u200fبوساطت\u200e Met \u200fفیض از جاب حق\u200e gl \u200fفیروذه کاخ - با کف بالف کنیده | است چه\u200e  و \u200ecle\u200f نقطه دارزده , کنایه از \u200eLs\u200f و عالم \u200ehin\u200f | روح اعظم فایزشد وبدین\u200cفیض وجود ارواح\u200cونطوی  باشد (۱). بهم رسید .  فیروذه هرقد - \u200ech\u200f میم و \u200eSU\u200f فیظل © - \u200eWaving Jabot\u200f وسکون را و \u200eSh\u200f بی نقطه ,'
373 'ن خلافت عس بدست سلمانان افتاد \u200eLT,\u200f پاره پاره کرده قسمت کردند . کاور لد بفتح ثالث وسکون رای ۳ نقطه وکاف \u200eBET.\u200f مرغان را گوبند - و بفتح رای قرشت بار وميوء کیر باشد \u200eOT,\u200f شبیه است بخیار کوچك \u200eLT,\u200f خبار کبر هم میگونند . در س رکه انداخته اچارسازند \u200eLy\u200f طمام خورلد.  ia \u200fبروزن\u200e elt \u200fبفتح\u200e - BIT \u200fکاواك است ۸ که پوچ و میان خالی و بی منز\u200e . ath \u200fبا دو کاف بالف کشیده\u200e » ٩ \u200fکا کاف\u200e \u200fبممنی تقعص و تمس تفیش\u200e aly \u200fرسکون دو\u200e ah  کاو کلود - با \u200eGE\u200f ولام و واو و رای قرشت و \u200eoS yo\u200f غیرمملوم \u200eCIT.\u200f تناسل\u200cرا گوید \u200ea'
373 'چاپ هرن 6۱۱۳ آمده : « کاو ؛ مبارز \u200ecoy\u200f چون دلیر و با قد \u200eath\u200f وتمام باشد اورا کاو خواند ۰ وکو مبارز بود .* . واصح کاو است که مخفف آن کو باشد : اما «کاو © یزلفتی است در «کاو * . قسی:کردی کاو 16801 ( تکبر ) « ژابا س ۳۷4 * . ۵ - از :کاو (کاودن) ۳ ال ( پسوند اسم فاعل واسم مفعول ) . رك : کاوك . ۱ - بجز عمود \u200eOLS\u200f نیست روز و شب خورشش شگفت لست ازوگر شکمش \u200eMIT\u200f است . \u200eged?\u200f . لت فری ۲۵۱ *. ۷ درف کاوبان (ه.م.) و رلك : اخترکاوان , اختر کاوبان . ومخصوساً \u200eBy\u200f کاوه . ۸ - رك \u200e٩ AIT:\u200f - از « کاودن» « بممنی ک'
379 '\u200fکه\u200e ath \u200fو زرکری و مسکری\u200e  (۱) چش : آصف() .  LS  \u200edee\u200f و پیوند کنند - و سربشم درودگرانرا لیز کویند که باآن چیزها را بهم بچسباننسوبمعنی فربه هم هست که نقیض \u200eZV\u200f باشد - و تعجیل وشتابرا یز گفته\u200cاند .  \u200fکبر ۲ \u200eow\u200f بفتح اول و الی بروزن\u200cنظره رستنبی باشد که در س رکه پرورده کنند وخورند ودر دواها نیز بکاربردد خصوصآخنازیر را نافع است اکر با م \u200eWaT\u200f کنند» وبعربی اصف (۱) خوانشد - و بسک ون \u200eGU\u200f بزبان پهلوی خفتان جنگه کبر راکویند ۸ - و بکر اول و فتح ثانی در عربی بزاد \u200ea Ty JL why JCal,\u200f ویسکون ثانی بز رگوارب'
379 '\u200f بفتح اول و الی بروزن\u200cنظره رستنبی باشد که در س رکه پرورده کنند وخورند ودر دواها نیز بکاربردد خصوصآخنازیر را نافع است اکر با م \u200eWaT\u200f کنند» وبعربی اصف (۱) خوانشد - و بسک ون \u200eGU\u200f بزبان پهلوی خفتان جنگه کبر راکویند ۸ - و بکر اول و فتح ثانی در عربی بزاد \u200ea Ty JL why JCal,\u200f ویسکون ثانی بز رگواربر! . \u200eSUS\u200f - با بای \u200eaml\u200f پروزن خبرهاء  \u200egh - ۱\u200f ای \u200eJaa\u200f اندر خ رکیجه بنادالی که با لرشیر برناید سنرون (سروزن.دهخدا) گاو ترخالی.  \u200fغنابری رازی « لت فری ۵۱۶ *.  \u200f۴ = کفچ = کفچه(«.م.) < کیجه:(عر) «مجدح کمنبر. ک'
379 ' و کید را مترادف سریشم گرفته\u200cاند ۱ 6 - رك : شرح قاموس و منتهی\u200cالارب . ۱ همان «کبد» است دربیت دقیقی (ح۳) که الف اطلاق آخربیت را جزو کلمه پنداشته\u200cاند !  \u200f۷ - 007167 < قبر ( بفتح اول ودوم ). نامهای عربی کبر وکبر ( بفتح اول و دوم درهردو و دوم مشدد در دومین ) وغیره از بونالی آمده\u200cاند و در اسپالیولی بصورت \u200ealcaparra\u200f \u200fباقی مانده > \u200ejue» Capparis spinosa\u200f ۱۹۷ . آزبوتانی \u200ekApparis\u200f . در کردی1۶867 « ژابا ۰۳۷4 ۸ مرك \u200e٩ St\u200f - از :کین ( رستنی) + با \u200eTua)\u200f (= کیررا (هم) . '
379 'د را مترادف سریشم گرفته\u200cاند ۱ 6 - رك : شرح قاموس و منتهی\u200cالارب . ۱ همان «کبد» است دربیت دقیقی (ح۳) که الف اطلاق آخربیت را جزو کلمه پنداشته\u200cاند !  \u200f۷ - 007167 < قبر ( بفتح اول ودوم ). نامهای عربی کبر وکبر ( بفتح اول و دوم درهردو و دوم مشدد در دومین ) وغیره از بونالی آمده\u200cاند و در اسپالیولی بصورت \u200ealcaparra\u200f \u200fباقی مانده > \u200ejue» Capparis spinosa\u200f ۱۹۷ . آزبوتانی \u200ekApparis\u200f . در کردی1۶867 « ژابا ۰۳۷4 ۸ مرك \u200e٩ St\u200f - از :کین ( رستنی) + با \u200eTua)\u200f (= کیررا (هم) . '
466 'ete \u200fبکر اول وسکون ثالی\u200e - AT \u200fسبد کرعابه بان و کنای\u200cراگوبند که بدان\u200c کین\u200e \u200fو پلیدیپا کشند۱ - و بفتح اول و سکون ثانی\u200e \u200fمعنی و هم بمعتی\u200cچرك\u200e nk \u200fو جیم فارسی ؛ هم\u200e " \u200fو ومخ ۷ + و پمعنی عجب وخودستابی و تکبر\u200e st \u200fو نم ول و سکون\u200e Ac \u200fو تجبررآمده\u200e ٩ \u200fو چم فارسی . بان ریز شده را گونند\u200e \u200fهم حست که آترا ازپشم بافند\u200e ten \u200fو نوعی از\u200e .۱* \u200fو از جانب کشمیر آورند\u200e  (۱) چش :۳ از .  ۱ -«کلته . چپار پای و دد پبر بود و ماتند این.بوشکور ( بلخی ) گوید : \u200eoe\u200f ددان کلته روباه گفت که دانا زد اين داستان در نهفت.» « لفت'
517 'بی است پرخار و شاخ وب \u200eISS\u200f \u200fو میو: \u200eOT\u200f را در س رکه اندازند و آچار سازند و در دواها \u200eSt\u200f بکار برند و \u200eeae\u200f شو کة التهبا خوانند \u200eSpry\u200f همان است .  کودده * - بر وزن تبرزه , بمعنی کورز است که میوه و بارکبر باشد 9 کبررستنیی \u200eoy\u200f خاردار و \u200eSys\u200f شامی همان است.  کودس \u200f بنم او و سکون ثانی مجهول و رای بی \u200eMads\u200f مفتوح \u200eCpt\u200f بیقطفزد»» موی پیچیده ومجمد راگوبند *9- وبمعنی \u200eSpy\u200f \u200fو رم هم آمده است *۱؛ و جضم اول \u200egilts\u200f لیز بأین معنی است - و بفتح اول و ثالی هم بمعتی پیج و شکن موی باشد.  ۴۳ - جهانگیری و رشیدی ک'
517 'ن موی باشد.  ۴۳ - جهانگیری و رشیدی کوراب ( با  \u200eGE\u200f تازی ) آورده\u200cاند « ورك : کوراب »کور. ۴ - در جهانگیری وسروری ورشیدی این\u200cسورت  \u200ea) \u200fمسحف « کویین» (هم)\u200e «oral  \u200f۴ = کوروا «رشیدی» «جپانگیری» از: کور( کبر) + با ( ۳ ابا).  \u200f۵ - این صورت در جهانگیری و رشیدی و سروری امد , ظ . «کوزه » را «کورة»  \u200e. \u200fاند\u200e aul ys . \u200fکوردین ۰ کوردین\u200e \u200fکه خیش باکلاله بس در کشد فار\u200e  \u200f۱ -سروری « کوردی » ( پکاف فارسی ) پمعنی کلیم آورده ؛ \u200eAy\u200f :  \u200fو زکوردی کند جل و کون\u200cپوش حفت\u200cرنگه.  \u200e6 \u200fسمرقندی « فرهنگه نظام\u200e Wy  \u200f۷ - ركك '
```


## [2026-09-06T15:56:08.102Z] TOOL CALL #65: Bash

```json
{
 "command": "ls site/pages/241.jpg 2>/dev/null || pdftoppm -f 241 -l 241 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg241 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


### [2026-09-06T15:56:09.623Z] TOOL RESULT

```
site/pages/241.jpg
total 7632
drwx------ 4 sfmqrb sfmqrb    4096 Sep  6 11:55 .
drwx------ 4 sfmqrb sfmqrb    4096 Sep  6 10:51 ..
-rw-rw-r-- 1 sfmqrb sfmqrb     968 Sep  6 11:53 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   92182 Sep  6 10:55 bqt1854.png
-rw-rw-r-- 1 sfmqrb sfmqrb   66580 Sep  6 10:57 bqt2023.png
-rw-rw-r-- 1 sfmqrb sfmqrb   69965 Sep  6 11:25 bqt2242crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb   28189 Sep  6 11:25 bqt2417crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb  431133 Sep  6 11:16 bqt2420_fn.png
-rw-rw-r-- 1 sfmqrb sfmqrb    9548 Sep  6 11:25 bqt2meta.json
-rw-rw-r-- 1 sfmqrb sfmqrb   81018 Sep  6 11:16 build213.py
-rw-rw-r-- 1 sfmqrb sfmqrb   67391 Sep  6 11:49 build225.py
-rw-rw-r-- 1 sfmqrb sfmqrb   71757 Sep  6 11:47 build232.py
-rw-rw-r-- 1 sfmqrb sfmqrb   32265 Sep  6 11:51 build234.py
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
-rw-rw-r-- 1 sfmqrb sfmqrb   84366 Sep  6 11:54 c246_n2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   51690 Sep  6 11:54 c246_n6.png
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
-rw-rw-r-- 1 sfmqrb sfmqrb    6971 Sep  6 11:03 crop1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    8619 Sep  6 11:03 crop2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5240 Sep  6 11:03 crop3.png
-rw-rw-r-- 1 sfmqrb sfmqrb   12820 Sep  6 11:05 crop_germ.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3408 Sep  6 11:05 crop_guthjo.png
-rw-rw-r-- 1 sfmqrb sfmqrb  111118 Sep  6 11:19 crop_habl.png
-rw-rw-r-- 1 sfmqrb sfmqrb    9001 Sep  6 11:05 crop_node12.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5564 Sep  6 11:05 crop_node1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5286 Sep  6 11:05 crop_varathra.png
-rw-rw-r-- 1 sfmqrb sfmqrb   11652 Sep  6 11:13 c_xzn.png
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
drwxrwxr-x 2 sfmqrb sfmqrb    4096 Sep  6 11:44 p216
drwxrwxr-x 2 sfmqrb sfmqrb    4096 Sep  6 11:52 p233
-rw-rw-r-- 1 sfmqrb sfmqrb   33321 Sep  6 11:51 part1.json
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
-rw-rw-r-- 1 sfmqrb sfmqrb   78380 Sep  6 11:51 pg239.png
-rw-rw-r-- 1 sfmqrb sfmqrb   81131 Sep  6 11:51 pg240.png
-rw-rw-r-- 1 sfmqrb sfmqrb   97613 Sep  6 11:49 pg242.png
-rw-rw-r-- 1 sfmqrb sfmqrb   80632 Sep  6 11:55 pg245.png
-rw-rw-r-- 1 sfmqrb sfmqrb   79253 Sep  6 11:54 pg246.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1209522 Sep  6 11:39 sin_goog.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  147680 Sep  6 11:20 sns167.jpg
```


## [2026-09-06T15:56:11.864Z] TOOL CALL #66: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/site/pages/241.jpg"
}
```


### [2026-09-06T15:56:11.894Z] TOOL RESULT

```

```


## [2026-09-06T15:57:09.312Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== LEW/LAT capparis ===\"; grep -n -i \"capparis\" LEW_1910.txt LAT.txt | head -5; echo \"=== WEB caper ===\"; grep -n -o -i \"capparis[^.]\\{0,120\\}\" WEB_vol1.txt | head -5; echo \"=== FSD caper ===\"; grep -n -o -i \"caper.\\{0,200\\}capparis\" FSD_vol1.txt | head -3"
}
```


### [2026-09-06T15:57:11.051Z] TOOL RESULT

```
=== LEW/LAT capparis ===
=== WEB caper ===
22421:Capparis cynophallophora
27588:capparis; Gr
27589:Capparisspinosa, gencrally growing from
27590:Capparis spinosa)
=== FSD caper ===
56960:caper  family,  of Mediterranean  countries,  growing  on  walls,  rocks,  etc.; also,  one  of  other  species  of  Capparis.  3.  Caper  tea, [   <   F.  capre,  <   L.  capparis
56961:caper,  a   shrub  (Capparis
56961:capers)  are  edible,  and  the  rootstocks, burned,  yield  salt,—  ca'pcrsber"ry,  n.  The  fruit  of  cither the  common  caper-bush  ( Capparis
```


## [2026-09-06T15:57:13.612Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '27585,27592p' WEB_vol1.txt; echo \"=== FSD ===\"; sed -n '56958,56962p' FSD_vol1.txt"
}
```


### [2026-09-06T15:57:13.722Z] TOOL RESULT

```
ca’per, n. [D. kaper,
from kapen, to take, seize.] a privateer of the seventeenth cen- tury. [Obs.]
ow Ce
capparis; Gr. kapparis, a caper.]
1. a prickly, trailing bush,Capparisspinosa, gencrally growing from
CAPER (Capparis spinosa)
ern part of Europe.
2. [pL] the flower buds of the caperbush,
=== FSD ===
Key  Is  artistic,  art;  fat,  fare;  fast;  get,  prey;  hit,  police;  obey,  go;  not,  Sr;  fall,  rule;  hut,  burn;  u   =   final;  1   =   habit,  renew Key  2;  art,  ape,  fat,  fare,  fast,  what,  all;  me,  get,  prey,  fern;  hit,  Ice;  I   =   e;  T=e;  go,  not,  Sr,  won,  wolf,  do*
391
Syn.:  sec  frolic;  prank.—  ca'per*cut"Ung,  a.  Addicted to  cutting  capers;  frolicsome.— c.dongtall,  n.  {Eng.J The  long-tailed  titmouse.— to  cut  a   c.,  to  take  fantastic steps,  as  in  dancing,  leap,  frisk;  hence,  to  act  in  a   fantastic or  foolish  manner  —   ca'pcr-some,  a.— ca'per-y,  a. ca'per2,  n .   X.  pi.  The  flower-buds  of  Capparis  spinosa , often  preserved  in  vinegar  and  used  as  a   condiment.  2. A   low  shrub  {Capparis  spinosa)  of  the  caper  family,  of Mediterranean  countries,  growing  on  walls,  rocks,  etc.; also,  one  of  other  species  of  Capparis.  3.  Caper  tea, [   <   F.  capre,  <   L.  capparis ,   <   Gr.  kapparis,  <   Ar. kabbar,  caper.]
—   African  caper,  a   shrub  (Capparis  sodada)  of  the  caper family,  native  of  northwestern  Africa,  bearing  baccate fruits.  The  berries  (capers)  are  edible,  and  the  rootstocks, burned,  yield  salt,—  ca'pcrsber"ry,  n.  The  fruit  of  cither the  common  caper-bush  ( Capparis  spinosa)  or  the  African species  named  above.—  c.*bush,  n.  1.  See  def.  2,  above.  2. The  caper-spurge,  c.splantf.—  c.  sauce,  a   sauce  flavored with  capers.— c.sspurge,  n.  A   species  of  spurge  ( Euphor- bia lattiyris)  whose  seed-vessels  are  used  as  capers.  See also  mole-tree.— c.  tea,  a   black  tea  made  from  young leaves  resembling  capers.—  capuchin  capers.  1.  The pods  of  the  nasturtium  or  Indian  cress.  2.  The  pods  of  the caper  or  myrtle  spurge.
ca'per*,  n.  A   privateer  (ship  or  captain)  of  the  17th century.  [<  D.  kaper,  <   kapen,  apparently  <   L, capio,  take.] cape'*race",  n.  See  under cape*,  n.
```


## [2026-09-06T15:57:20.945Z] AGENT

Now I'll write the verification file.


## [2026-09-06T16:03:22.732Z] TOOL CALL #69: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/w241.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\n\ndata = {\n \"pdf_page\": 241,\n \"book_page\": 211,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-06\",\n \"entries\": [\n  {\n   \"entry\": 1,\n   \"root\": \"Kapho\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *ḱoph₂-ó- (Pokorny ḱapho- / ḱopho-) 'hoof'\",\n   \"note\": \"Pokorny IEW p.530 has exactly 'Root/lemma: ḱapha- or ḱopho-, Meaning: hoof', with Old Indic śapha- m. 'hoof, claw', Avestan safa- m. 'hoof of the horse', Old Icelandic hófr, Old English hōf, Old High German huof; references WP. I 346. Watkins/AHD prints the root as 'kap(h)o-. Hoof.' with a lengthened-grade *kāp(h)-o- for Germanic. The modern laryngealist spelling is *ḱoph₂ós (Wiktionary), whence Proto-Indo-Iranian *ćapʰás. Nourai's language label ('Indo-European'), form and gloss are all right. The one weak link in the chart is not the root but the Iranian branch: the Persian/Pahlavi word for 'hoof' is sumb/som with an unexplained -mb-, which Horn and Hübschmann treat as a cognate of, not a descendant of, Av. safa-.\",\n   \"note_fa\": \"ریشهٔ هندواروپاییِ آغازین *ḱoph₂ós «سُم» (پوکورنی ص ۵۳۰ به‌صورت ḱapho-/ḱopho-؛ والده‑پوکورنی ج ۱ ص ۳۴۶؛ واتکینز در پیوستِ فرهنگ American Heritage). بازماندگانِ آن سنسکریت śapha-، اوستایی safa-، ایسلندی کهن hófr و انگلیسی کهن hōf است، پس عنوانِ زبانی و معنایی که نورایی داده درست است. تنها گرهِ سست در این نمودار شاخهٔ ایرانی است: «سُم / سُنب» فارسی و sumb پهلوی «ـ نب/ـ مب» ای دارند که از safa- اوستایی به‌طور قاعده‌مند به دست نمی‌آید و هرن و هوبشمان آن دو را هم‌ریشه (نه فرزند و پدر) می‌دانند.\",\n   \"sources\": [\n    \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/%C4%87ap%CA%B0%C3%A1s\",\n    \"https://www.etymonline.com/word/hoof\"\n   ],\n   \"ref_check\": [\n    {\"ref\": \"POK:530\", \"status\": \"supports\",\n     \"note\": \"POK_full.txt (Pokorny database dump), entry 'Root/lemma: ḱapha- or ḱopho-, Meaning: hoof, *claw, nail ... Old Indie sapha- m. \\\"hoof, claw, nail\\\", Avestan safa- m. \\\"hoof of the horse\\\"; Old Icelandic hofr, Old English hof, Old High German huof \\\"hoof\\\". References: WP. I 346 ... Page(s): 530' — page number and content exactly as Nourai cites.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"WLD\", \"where\": \"Bd. I p. 346 (WLD_Bd1_pages.txt line 32605)\", \"stance\": \"supports\",\n     \"note\": \"'kapho- oder kōpho- „Huf“. Ai. çapha- m. „Huf, Klaue“, av. safa- m. „Huf des Pferdes“. Aisl. hófr, ags. hóf, ahd. huof „Huf“.' — the page Pokorny himself cites.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. kap(h)o-\", \"stance\": \"supports\",\n     \"note\": \"'kap(h)o-. Hoof. Lengthened-grade form kāp(h)-o- in Germanic *hōfaz in Old English hōf, hoof: HOOF. [Pok. kapho- 530.]'\"},\n    {\"src\": \"SYN\", \"where\": \"Buck 1949, searched 'hoof' in SYN.txt\", \"stance\": \"silent\",\n     \"note\": \"Buck has no 'hoof' chapter; the only hits are late Lat. gamba 'hoof or hock' (4.36) and Lith. naga 'hoof' under 'nail' — nothing on ḱapho-.\"},\n    {\"src\": \"IEC\", \"where\": \"Mann, searched 'kapho', 'kopho' in IEC.txt\", \"stance\": \"silent\", \"note\": \"no entry found for this root in the OCR.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Avestan\", \"words\": \"safa\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Younger Avestan safa- m. 'hoof of the horse' (Yašt 8.18, Vd.) is the regular Iranian continuation of PIE *ḱoph₂-ó-: PIE *ḱ > Indo-Iranian *ć > Iranian s (as in *ḱm̥tóm > Av. satəm), and PIE *pʰ (or *p before the laryngeal) > Iranian f between vowels, giving *ćapʰás > Proto-Iranian *cafah- > Av. safa-. Its exact Indic twin is Vedic śaphá- 'hoof, claw'. Bartholomae, Altiranisches Wörterbuch col. ~1556, prints 'j. safa- m. \\\"Huf des Pferdes\\\"'. Nourai's arrow root→Avestan is exactly Pokorny's.\",\n     \"derivation_fa\": \"اوستاییِ متأخر safa- «سمِ اسب» بازماندهٔ قاعده‌مندِ *ḱoph₂-ó- هندواروپایی است: ḱ هندواروپایی در هندوایرانی به ć و سپس در ایرانی به s بدل شده (مانند satəm در برابر *ḱm̥tóm)، و pʰ در میانِ دو واکه در ایرانی f شده است؛ پس *ćapʰás ← *cafah- ← safa-. جفتِ هندیِ آن śaphá- سنسکریت است. بارتولومه در «فرهنگ ایرانی باستان» (ستون ۱۵۵۶) همین را می‌آورد. این پیوندِ نمودارِ نورایی درست است.\",\n     \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/%C4%87ap%CA%B0%C3%A1s\"],\n     \"ref_check\": [\n      {\"ref\": \"POK:530\", \"status\": \"supports\", \"note\": \"Pokorny p.530 lists 'Avestan safa- m. \\\"hoof of the horse\\\"' as a direct reflex of ḱapho-.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch col. ~1556 (BRT.txt leaf 850)\", \"stance\": \"supports\",\n       \"note\": \"'• j. safa- m. \\\"Huf des Pferdes\\\": aurvants..' — the word, gender and gloss the chart gives; cf. also para.safa- 'Vorderhuf' (Yt.10.135) and parəšu.safa- 'breithufig'.\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. I p. 346\", \"stance\": \"supports\", \"note\": \"'av. safa- m. „Huf des Pferdes“' beside Ai. çapha-.\"},\n      {\"src\": \"HUB\", \"where\": \"Persische Studien §745, p. 76\", \"stance\": \"supports\",\n       \"note\": \"'Zd. safa- = skr. çapha-' — Hübschmann affirms the Avestan-Sanskrit equation (his objection concerns only the New Persian word).\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Pahlavi\", \"words\": \"sumb 1\", \"verdict\": \"plausible\",\n     \"derivation\": \"Middle Persian sumb [swmb'] 'hoof' is well attested (MacKenzie, Concise Pahlavi Dictionary p.79 'sumb [swmb'] hoof'; Nyberg, Manual of Pahlavi II 'sumb [swmb'] hoof of a beast, 49.14-18, 94.18-19; āsēnēn-~ iron-hoofed'), and Armenian borrowed it as smbak < *sumbak. What is NOT regular is the derivation drawn here: Av. safa- would give MP *saf/sab, not sumb. Horn, Grundriss no. 745 (p.164), the very page Nourai cites, is careful to say only 'Eine Urverwandtschaft ist sicher ... zwischen aw. safa-, ai. çaphá-, afγ. swa, oss. säftäg einerseits und np. sum, sumb andererseits anzunehmen' — a sister relationship, not descent; and Hübschmann §745 flatly objects: 'Zd. safa- = skr. çapha- lässt sich schwer mit np. sum, sunb = ap. *sumba- oder *sumpa- ... vereinigen.' Wiktionary nonetheless files MP sumb under Proto-Iranian *cafáh, so the family is agreed even though the -mb- (and the u-vocalism, possibly by contamination with sumb- 'to bore', suftan) is unexplained. Hence 'plausible' rather than 'confirmed'.\",\n     \"derivation_fa\": \"«سُنب/سُمب» فارسی میانه (نوشتار swmb') به‌روشنی گواهی شده است: مکنزی در «فرهنگ کوچک پهلوی» sumb «سم» و نیبرگ در «راهنمای پهلوی» sumb «سمِ چارپا» و آمیختهٔ āsēnēn-sumb «آهنین‌سم» را می‌آورند، و ارمنی نیز آن را به‌صورت smbak وام گرفته است. اما گذارِ safa- اوستایی به sumb قاعده‌مند نیست؛ از safa- در فارسی میانه *saf/sab انتظار می‌رفت. هرن در همان صفحه‌ای که نورایی ارجاع می‌دهد (بند ۷۴۵، ص ۱۶۴) تنها از «هم‌ریشگیِ آغازین» میان safa- اوستایی و sum/sumb فارسی سخن می‌گوید نه از فرزندی، و هوبشمان (بند ۷۴۵) صریحاً می‌گوید آشتی‌دادنِ این دو دشوار است و *sumba-/*sumpa- را برای ایرانی باستان بازمی‌سازد. ویکی‌واژه با این همه sumb را زیرِ ایرانی آغازینِ *cafáh می‌گذارد. پس ادعای نورایی با احتیاط پذیرفتنی است؛ «مـ/نـ» میانی (شاید به تأثیرِ ستاکِ sumb- «سوراخ کردن، سُفتن») توضیح داده نشده است.\",\n     \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/%C4%87ap%CA%B0%C3%A1s\", \"https://en.wiktionary.org/wiki/%D8%B3%D9%85\"],\n     \"ref_check\": [\n      {\"ref\": \"HRN:164\", \"status\": \"partial\",\n       \"note\": \"HRN.txt leaf 186 = printed p.164, entry '745. (1) sum, sumb \\\"Huf\\\". aw. vergl. safa- \\\"Huf\\\"; phlv. sumb, arm. LW. smbak; ai. vergl. çaphá- \\\"Huf\\\"; an. hūfr, nhd. Huf.' — Horn has all the forms Nourai's chart has (incl. Pahlavi sumb) but ends 'Eine Urverwandtschaft ist sicher ... anzunehmen', i.e. cognacy, not the descent the arrow draws.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie 1971 p.79 (PHD.txt line 572; PHD_mackenzie.txt line 4711)\", \"stance\": \"supports\",\n       \"note\": \"'sumb [swmb'] | N ~] hoof.' — immediately after 'suftan, sumb- [swptn', swmb-] pierce, bore', so the two stems are homographs in Pahlavi.\"},\n      {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II, glossary s.v. sumb (NYB_vol2_glossary.txt line 3563)\", \"stance\": \"supports\",\n       \"note\": \"'sumb [swmb'] hoof of a beast 49.14-18, 94.18-19. āsēnēn-~ iron-hoofed (or iron-shod?) 22.12, 28.12.23. — Arm. lw. smbak < *sumbak; NP sunb.'\"},\n      {\"src\": \"HUB\", \"where\": \"Persische Studien §745, p. 76\", \"stance\": \"contradicts\",\n       \"note\": \"'Zd. safa- = skr. çapha- lässt sich schwer mit np. sum, çunb = ap. *sumba- oder *sumpa-, das im Skr. *çumbha- oder *çumpa- lauten würde, vereinigen.'\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"Persian\", \"words\": \"som «سُم ۱»\", \"verdict\": \"confirmed\",\n     \"derivation\": \"New Persian سُم som (older and dialectal سُنب sonb/somb) continues Middle Persian sumb directly: the MP cluster -mb- is preserved in the older NP form سنب and then simplified to -m in the modern standard pronunciation som, exactly the pattern of MP tumb > NP tom or MP zamb > NP zam. Borhan-e Qateʿ (Moʿin's ed.) p.1163 has the entry 'سم – بضم اول و سکون ثانی ... است که سم اسب و استر و خر و گاو و گوسفند و امثال آن باشد و این بمنزلة ناخن است' ('the hoof of horse, mule, donkey, ox and sheep; it is to them what the nail is'), and Moʿin's own etymological footnote there reads 'سنب = سمب، پهلوی sumb، ارمنی smbak، کردی sum، افغانی swa ... در پارسی باستان *sumba- یا *sumpa- ... سانسکریت śapha- ... معرب: سنباك ... رك: هوبشمان ۹۴۷' — i.e. exactly the chain Pahlavi sumb > NP som/sonb that the chart draws, with Hübschmann cited for the Old Iranian reconstruction. Arabic borrowed the word back as سنبك sunbuk/sunbak.\",\n     \"derivation_fa\": \"«سُم» فارسی نو دنبالهٔ مستقیمِ sumb فارسی میانه است؛ صورتِ کهن‌تر و گویشیِ «سُنب/سُمب» خوشهٔ ـ نب پهلوی را نگه داشته و در تلفظِ امروزی به «ـ م» ساده شده است (همان الگوی tumb ← «تم» و zamb ← «زم»). در «برهان قاطع» به‌تصحیح معین، ص ۱۱۶۳، مدخل «سم» چنین است: «بضم اول و سکون ثانی ... است که سم اسب و استر و خر و گاو و گوسفند و امثال آن باشد و این بمنزلة ناخن است»، و حاشیهٔ ریشه‌شناختیِ خودِ معین در همان صفحه می‌گوید: «سنب = سمب، پهلوی sumb، ارمنی smbak، کردی sum، افغانی swa ... در پارسی باستان *sumba- یا *sumpa- ... سانسکریت śapha- ... معرّب: سنباك ... رك: هوبشمان ۹۴۷». پس همان زنجیره‌ای که نورایی کشیده است؛ ادعای او درست است. عربی نیز این واژه را به‌صورت «سُنبُك» وام گرفته است.\",\n     \"sources\": [\"https://en.wiktionary.org/wiki/%D8%B3%D9%85\"],\n     \"ref_check\": [\n      {\"ref\": \"BQT:1163\", \"status\": \"supports\",\n       \"note\": \"BQT_v2_pages.txt leaf 627 (the scan's leaf n = printed page n+536, so leaf 627 = printed 1163 exactly): headword 'سم – بضم اول و سکون ثانی ... سم اسب و استر و خر و گاو و گوسفند ...' with Moʿin's footnote 3 'سنب = سمب، پهلوی sumb، ارمنی smbak، کردی sum، افغانی swa ... معرب: سنباك ... رك: هوبشمان ۹۴۷'. The chart's extra form سُنب is Borhan's own variant.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BQT\", \"where\": \"Borhan-e Qateʿ ed. Moʿin p.1163, entry سم + footnotes 3-4\", \"stance\": \"supports\",\n       \"note\": \"Moʿin's footnote gives Pahlavi sumb, Armenian smbak, Kurdish sum, Sanskrit śapha- and OP *sumba-/*sumpa-, citing Hübschmann.\"},\n      {\"src\": \"HRN\", \"where\": \"Grundriss no. 745, p. 164\", \"stance\": \"supports\",\n       \"note\": \"'(1) sum, sumb \\\"Huf\\\" ... phlv. sumb' — the NP form and its Pahlavi antecedent.\"},\n      {\"src\": \"PHD\", \"where\": \"MacKenzie 1971 p.79\", \"stance\": \"supports\", \"note\": \"'sumb [swmb'] | N ~] hoof' — MacKenzie's 'N ~' means the New Persian form is identical, i.e. sumb/sonb.\"}\n     ]\n    },\n    {\n     \"id\": 4, \"lang\": \"Persian\", \"words\": \"safal «سَفَل»\", \"verdict\": \"plausible\",\n     \"derivation\": \"The word itself is real and the chart's variant list is accurate: Moʿin, Farhang-e Farsi, s.v. 'سپل: sopol [= سول = سفل = شفل] (اِ.) سم شتر. ناخن فیل' ('camel's hoof-pad; elephant's nail'), and Borhan-e Qateʿ s.v. 'شفل ... ناخن شتران بارکش را گویند' ('the nail of pack-camels'), with Moʿin's note recording Tabari šoppol. Note that the standard headword in Moʿin is سپل sopol and Nourai has promoted the variant سَفَل to headword. As for the derivation from Av. safa-: it is phonetically attractive for the variant سَوَل sawal (Old Iranian intervocalic -f- > NP -w-, so *safa- > *saw- plus the denominal suffix -al), but no source I could reach actually states it; Moʿin gives no etymology, Horn and Hübschmann are silent, and the -p- of سپل and Tabari šoppol point rather to an expressive/dialectal formation. Cheung's Iranian verb dictionary is not relevant (this is a noun). So: possible, unproved — 'plausible'.\",\n     \"derivation_fa\": \"خودِ واژه و فهرستِ گونه‌هایش درست است: معین در «فرهنگ فارسی» می‌آورد «سپل: sopol [= سول = سفل = شفل] (اِ.) سم شتر. ناخن فیل»، و «برهان قاطع» ذیلِ «شفل» می‌گوید «ناخن شتران بارکش را گویند» و معین در حاشیه صورتِ طبریِ šoppol را یاد می‌کند. توجه شود که سرواژهٔ معین «سپل» است و نورایی گونهٔ «سَفَل» را سرواژه کرده است. اما دربارهٔ برگرفتنِ آن از safa- اوستایی: از نظرِ آوایی برای گونهٔ «سَوَل» پذیرفتنی است (فِ ایرانیِ باستان در میان دو واکه در فارسی به «و» بدل می‌شود، پس *safa- ← *saw- + پسوندِ ـَل)، ولی هیچ منبعی که در دسترس بود این را نمی‌گوید؛ معین ریشه نمی‌دهد و هرن و هوبشمان خاموش‌اند، و «پ»ِ «سپل» و صورتِ طبریِ šoppol بیشتر به ساختی گویشی/عامیانه می‌مانند. پس ادعای نورایی با احتیاط پذیرفتنی است ولی اثبات‌نشده.\",\n     \"sources\": [],\n     \"ref_check\": [\n      {\"ref\": \"MON:1825\", \"status\": \"supports\",\n       \"note\": \"Entry located in the Moʿin OCR (MON_part1.txt line 75328): 'سپل: sopol [- سول - سفل - شفل] (اِ.) سم شتر. ناخن فیل.' The variant list matches the chart's سَپَل / شَفَل / سَوَل exactly. The page number 1825 cannot be checked in the 2-vol Adena reprint that is on disk (no printed page markers), but the entry is Moʿin's.\"},\n      {\"ref\": \"SOD:65\", \"status\": \"not_found\",\n       \"note\": \"Searched Gharib's Sogdian dictionary both ways: entry 65 (SOD.txt line 8020) is 'ʾδyt (M)', nothing to do with hooves, and printed p.65 (SOD_pages.txt leaf 132, entries 1659-1680 ʾspwrnyʾkh … ʾstʾnprʾk) has no hoof word either; a full-file grep for 'hoof' in SOD.txt and SOD_pages.txt returns nothing. No Sogdian support for safal could be located.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"MON\", \"where\": \"Farhang-e Farsi s.v. سپل (MON_part1.txt line 75328)\", \"stance\": \"supports\",\n       \"note\": \"'سپل: sopol [- سول - سفل - شفل] (اِ.) سم شتر. ناخن فیل' — word, gloss and all three variants, but no etymology given.\"},\n      {\"src\": \"BQT\", \"where\": \"Borhan-e Qateʿ vol. 3 s.v. شفل (BQT_v3_pages.txt leaf 63) and the cross-reference 'رك: سپل' on leaf 40\", \"stance\": \"partial\",\n       \"note\": \"'شفل ... ناخن شتران بارکش را گویند'; the note on leaf 40 reads 'رك: سپل. — طبری shoppol (سوت)' — Borhan confirms the word and the س/ش variation but offers no Avestan etymology.\"},\n      {\"src\": \"HRN\", \"where\": \"Grundriss, searched sapal/safal/sipal\", \"stance\": \"silent\", \"note\": \"Horn has no entry for this word; his §745 covers only sum/sumb.\"},\n      {\"src\": \"HUB\", \"where\": \"Persische Studien, searched safal/sapal\", \"stance\": \"silent\", \"note\": \"no entry.\"}\n     ]\n    },\n    {\n     \"id\": 5, \"lang\": \"Germanic\", \"words\": \"hôfaz\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Proto-Germanic *hōfaz 'hoof' is the lengthened-grade o-form of the same root: PIE *ḱ > Germanic h by Grimm's Law, PIE *p(h) > Germanic f, and the lengthened *ō explains the long vowel of all the daughters — Old English hōf, Old Saxon/Old Frisian hof, Old Norse hófr, Danish hov, Dutch hoef, OHG/MHG huof, German Huf. Watkins (AHD, the reference Nourai cites) writes it out: 'Lengthened-grade form kāp(h)-o- in Germanic *hōfaz in Old English hōf'. Nourai's 'hôfaz' is the standard *hōfaz with ô for ō.\",\n     \"derivation_fa\": \"ژرمنیِ آغازین *hōfaz «سم» صورتِ کشیدهٔ همان ریشه است: ḱ هندواروپایی بر پایهٔ قانونِ گریم در ژرمنی h شده و p(h) به f بدل گشته، و واکهٔ کشیدهٔ ō واکهٔ بلندِ همهٔ بازماندگان را توضیح می‌دهد: انگلیسی کهن hōf، ساکسونی و فریزیِ کهن hof، نورسِ کهن hófr، هلندی hoef و آلمانی Huf. واتکینز در پیوستِ AHD — همان مأخذی که نورایی یاد کرده — همین را می‌نویسد. صورتِ «hôfaz» نورایی همان *hōfaz متعارف است.\",\n     \"sources\": [\"https://www.etymonline.com/word/hoof\"],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\",\n       \"note\": \"AHD_watkins1985.txt: 'kap(h)o-. Hoof. Lengthened-grade form kāp(h)-o- in Germanic *hōfaz in Old English hōf, hoof: HOOF. [Pok. kapho- 530.]' — the Germanic form Nourai prints.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"Klein s.v. hoof (KLN_1966.txt line 18040)\", \"stance\": \"supports\",\n       \"note\": \"'hoof, n. — ME. hoof, fr. OE. hof, rel. to OS., OFris. hof, ON. hofr, Dan. hov, Swed. hof, Du. hoef, OHG., MHG. huof, G. Huf, \\\"hoof\\\", and cogn. with OI. saphah, \\\"hoof\\\", Avestic safa-, \\\"hoof of the horse\\\".'\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. I p. 346\", \"stance\": \"supports\", \"note\": \"'Aisl. hófr, ags. hóf, ahd. huof „Huf“' listed directly under kapho-/kōpho-.\"},\n      {\"src\": \"POK\", \"where\": \"IEW p. 530\", \"stance\": \"supports\", \"note\": \"'Old Icelandic hofr, Old English hof, Old High German huof \\\"hoof\\\"'.\"}\n     ]\n    },\n    {\n     \"id\": 6, \"lang\": \"English\", \"words\": \"hoof\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Old English hōf > Middle English hoof > Modern English hoof, an ordinary inherited word with no borrowing step; the plural hooves/hoofs reflects the regular ME voicing of final -f in the plural. Klein and Etymonline agree; Etymonline adds Boutkan's caution that outside Indo-Iranian and Germanic the root is poorly attested ('a typical relic form that only survived in the periphery of the IE area') and that some connect it instead with *kop- 'to beat, strike' (Slavic kopyto). That does not affect the OE > ME > NE step, which is certain. The node carries no reference in the book.\",\n     \"derivation_fa\": \"انگلیسی کهن hōf ← انگلیسی میانه hoof ← انگلیسی نو hoof؛ واژه‌ای موروثی است و هیچ حلقهٔ وام‌گیری در آن نیست، و جمعِ hooves بازتابِ واک‌دار شدنِ قاعده‌مندِ f پایانی در انگلیسی میانه است. کلاین و اتیمانلاین هم‌داستان‌اند. اتیمانلاین می‌افزاید که بوتکان این ریشه را «صورتی بازمانده در حاشیهٔ حوزهٔ هندواروپایی» می‌داند و برخی kopyto اسلاوی را به ریشهٔ دیگری (*kop- «کوبیدن») می‌برند؛ ولی این نکته در حلقهٔ انگلیسی اثری ندارد. این گره در کتاب مأخذی ندارد.\",\n     \"sources\": [\"https://www.etymonline.com/word/hoof\"],\n     \"ref_check\": [\n      {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the book gives no reference for this node.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"Klein s.v. hoof\", \"stance\": \"supports\", \"note\": \"'hoof, n. — ME. hoof, fr. OE. hof ...'\"},\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. kap(h)o-\", \"stance\": \"supports\", \"note\": \"'... in Old English hōf, hoof: HOOF.'\"},\n      {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century, s.v. hoof\", \"stance\": \"supports\", \"note\": \"standard AS. hof > hoof; no dissent.\"}\n     ]\n    }\n   ]\n  },\n  {\n   \"entry\": 2,\n   \"root\": \"Kapparis\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"Ancient Greek κάππαρις 'caper plant, Capparis spinosa' (origin uncertain, probably Oriental)\",\n   \"note\": \"The Greek word is real and correctly glossed. Its own origin is what is disputed: Klein calls it 'of unknown etymology'; Etymonline 'of uncertain origin'; Beekes (Etym. Dict. of Greek p.639) suspects an Oriental source and adduces Persian kabar and Burushaski čopuri; Funk & Wagnalls, going the other way, derives Gk. kapparis from Arabic kabbar. Nourai's chart makes Greek the head and derives Persian from it — which is the majority position (Klein, Lokotsch, Etymonline, Moʿin's footnote in Borhan, Wiktionary) — while the box's own NOTE (from KGW:98) claims the opposite, that the word reached Europe from Old Persian through Greek. Skeat is on the NOTE's side: his 'Distribution of words' appendix files caper (2) under 'French from Latin from Greek from PERSIAN'. On the evidence available the majority view wins: there is no Old or Middle Iranian caper-word from which Gk. kapparis could come, whereas the Semitic and Persian forms are all late and all match the Greek exactly.\",\n   \"note_fa\": \"واژهٔ یونانیِ κάππαρις «بوتهٔ کبر» راست است و معنایش درست داده شده؛ آنچه محلِّ اختلاف است خاستگاهِ خودِ آن است. کلاین آن را «با ریشه‌شناسی ناشناخته» و اتیمانلاین «با خاستگاه نامعلوم» می‌خواند؛ بیکس (فرهنگ ریشه‌شناختی یونانی، ص ۶۳۹) خاستگاهی خاوری برای آن حدس می‌زند و «کَبَر» فارسی و čopuri بوروشاسکی را گواه می‌آورد؛ در برابر، فرهنگ Funk & Wagnalls یونانی را از «کبّار» عربی می‌گیرد. نورایی یونانی را سرِ نمودار گذاشته و فارسی را از آن گرفته است — که دیدگاهِ اکثریت است (کلاین، لوکوچ، اتیمانلاین، حاشیهٔ معین در برهان قاطع، ویکی‌واژه) — حال آنکه یادداشتِ خودِ همان جعبه (به‌نقل از KGW:98) عکسِ آن را می‌گوید. اسکیت جانبِ یادداشت را می‌گیرد. با شواهدِ موجود دیدگاهِ اکثریت برتری دارد: هیچ واژهٔ ایرانیِ باستان یا میانه‌ای برای «کبر» در دست نیست که یونانی بتواند از آن آمده باشد، در حالی که صورت‌های سامی و فارسی همه دیرین‌اند و دقیقاً با یونانی می‌خوانند.\",\n   \"sources\": [\n    \"https://en.wiktionary.org/wiki/%CE%BA%CE%AC%CF%80%CF%80%CE%B1%CF%81%CE%B9%CF%82\",\n    \"https://www.etymonline.com/word/caper\"\n   ],\n   \"ref_check\": [\n    {\"ref\": \"KLN:234\", \"status\": \"supports\",\n     \"note\": \"KLN_1966.txt leaf 134 (2 printed pages/leaf ≈ pp.233-235), s.v. caper: 'a prickly shrub (Capparis spinosa). — ME. caperis, caperes, fr. L. capparis [whence also It. cappero (whence OF. caspres, F. câpre) and G. Kaper], fr. Gk. κάππαρις (whence Arab. kabbār, ModPers. kabar); of unknown etymology.'\"},\n    {\"ref\": \"AHD:199\", \"status\": \"not_checked\",\n     \"note\": \"AHD:199 is a page of the main dictionary (the 'caper' entry) of the New College Edition, which is only available on archive.org under lending restriction; the local AHD file is Watkins's Indo-European-roots appendix only and has no kapparis.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"LKT\", \"where\": \"Lokotsch no. 978 (LKT.txt line 2337)\", \"stance\": \"supports\",\n     \"note\": \"'„Kapern“, die jungen Blütenknospen von Capparis spinosa [aus gr. κάππαρις], Einheitsnomen kabbāra; hieraus mit ar. Art. sp. pg. alcaparra, it. caparra. Die übrigen Formen kommen dagegen unmittelbar über lat. capparis aus dem gr. Grundwort: it. cappari, frz. câpres; engl. capers, dtsch. Kapern ...'\"},\n    {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls s.v. caper² (FSD_vol1.txt line 56960)\", \"stance\": \"contradicts\",\n     \"note\": \"'[< F. câpre, < L. capparis, < Gr. kapparis, < Ar. kabbar, caper.]' — F&W makes the Greek word a borrowing from Arabic, i.e. neither Nourai's arrow nor his NOTE.\"},\n    {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century s.v. caper (WEB_vol1.txt line 27588)\", \"stance\": \"supports\",\n     \"note\": \"'[... capparis; Gr. kapparis, a caper.] 1. a prickly, trailing bush, Capparis spinosa' — the gloss 'a shrub' is right; Webster gives no further origin.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Persian\", \"words\": \"kabar «کَبَر»\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Persian کَبَر kabar 'caper bush, Capparis spinosa' does come from Greek κάππαρις, but not directly: the route is Gk. κάππαρις → Classical Syriac/Aramaic ܟܦܪ kappār → Arabic كَبَر kabar / كَبَّار kabbār / قَبَّار qabbār → Persian کَبَر (whence the chart's variant قَبَر, which is simply the Arabic q-form), an ordinary Hellenistic plant-name borrowing of the kind Syriac mediated in the 3rd-6th c. CE. Klein states the endpoint outright ('Gk. κάππαρις, whence Arab. kabbār, ModPers. kabar'), and Moʿin's own footnote in Borhan-e Qateʿ p.1587 says the same in Persian: 'نامهای عربی کبر و کبّار ... از یونانی آمده‌اند و در اسپانیولی به‌صورت alcaparra باقی مانده ... از یونانی kápparis. در کردی kebar'. The chart's third variant قَباریس qabāris is a learned re-borrowing of the Greek nominative kapparis itself (through Arabic transcription), not an inherited form. The box's NOTE (KGW:98, Old Persian → Greek) is the minority view, shared by Skeat and hinted at by Beekes; it has no Old Iranian evidence behind it and is not what the other references on this very node (KLN, BQT) say. Nourai's arrow direction is therefore right.\",\n     \"derivation_fa\": \"«کَبَر» فارسی (بوتهٔ کبر، Capparis spinosa) از κάππαρις یونانی است، اما نه بی‌واسطه: راهِ آن یونانی ← سریانی/آرامی kappār ← عربی «کَبَر / کبّار / قبّار» ← فارسی «کَبَر» است، و گونهٔ «قَبَر» در نمودار همان صورتِ عربیِ قافی است. این‌گونه وام‌گیریِ نام‌های گیاهیِ یونانی از راهِ سریانی در سده‌های سوم تا ششم میلادی معمول بوده است. کلاین صریح می‌گوید یونانی κάππαρις مادرِ «کبّار» عربی و «کبر» فارسی است، و حاشیهٔ خودِ معین در «برهان قاطع» ص ۱۵۸۷ نیز به فارسی همین را می‌گوید: «نامهای عربی کبر و کبّار ... از یونانی آمده‌اند و در اسپانیولی به‌صورت alcaparra باقی مانده ... از یونانی kápparis. در کردی kebar». گونهٔ سومِ نمودار، «قَباریس»، وام‌گیریِ دوبارهٔ صورتِ فاعلیِ یونانی kapparis از راهِ نویسهٔ عربی است نه صورتی موروثی. یادداشتِ جعبه (که واژه را از پارسی باستان به یونانی می‌بَرد) دیدگاهی اقلیتی است — اسکیت هوادارِ آن است و بیکس به آن اشاره‌ای دارد — ولی هیچ گواهِ ایرانیِ باستانی ندارد و با دو مأخذِ دیگرِ همین گره (کلاین و برهان) نیز نمی‌خواند. پس جهتِ پیکانِ نورایی درست است.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/%CE%BA%CE%AC%CF%80%CF%80%CE%B1%CF%81%CE%B9%CF%82\",\n      \"https://www.etymonline.com/word/caper\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"KLN:234\", \"status\": \"supports\",\n       \"note\": \"Klein s.v. caper: 'fr. Gk. κάππαρις (whence Arab. kabbār, ModPers. kabar); of unknown etymology' — Greek to Persian, exactly the arrow, with Arabic as the go-between.\"},\n      {\"ref\": \"BQT:1587\", \"status\": \"supports\",\n       \"note\": \"BQT_v3_pages.txt leaf 379 (v3's leaf n = printed n+1208, so leaf 379 = printed 1587): headword 'کبر ... بفتح اول و ثانی بروزن نظره رستنیی باشد که در سرکه پرورده کنند و خورند ... وبعربی اصف خوانند'; Moʿin's footnote 7: 'kabar < قبر ... نامهای عربی کبر و کبّار ... از یونانی آمده‌اند و در اسپانیولی به‌صورت alcaparra باقی مانده، Capparis spinosa ... از یونانی kápparis. در کردی kebar «ژابا ۳۷۴»'.\"},\n      {\"ref\": \"SKT:75\", \"status\": \"partial\",\n       \"note\": \"The Skeat scan on disk is a different impression (its caper (2) entry sits on printed p.65, leaf 87, '(F.-L.-Gk.-Pers.) F. câpre, L. capparis, Gk. κάππαρις'), and his appendix 'Distribution of Words' §14 lists 'French from Latin from Greek from Persian: caper (2), jujube, magic, myrtle ...'. So Skeat has the word but derives it in the opposite direction to the chart's arrow — he supports Nourai's NOTE, not his diagram.\"},\n      {\"ref\": \"KGW:98\", \"status\": \"not_checked\",\n       \"note\": \"Ibrahim, Kulturgeschichtliche Wortforschung (1991) exists only as a Google Books limited preview; p.98 not viewable (see MISSING_REFERENCES.md §19).\"},\n      {\"ref\": \"AFM:131\", \"status\": \"not_found\",\n       \"note\": \"Addi Shir p.131 = AFM_pages.txt leaf 139 (offset leaf−8), which carries الكندر / الكندوج / كنداكر etc. — no كبر entry. A grep of the whole book for الكبر / كبار / قبار finds only كبريت. Addi Shir apparently does not treat kabar as an arabized Persian word at all.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BQT\", \"where\": \"Borhan-e Qateʿ ed. Moʿin p.1587 s.v. کبر, footnote 7\", \"stance\": \"supports\",\n       \"note\": \"'... از یونانی آمده‌اند و در اسپانیولی به‌صورت alcaparra باقی مانده ... از یونانی kápparis'.\"},\n      {\"src\": \"KLN\", \"where\": \"Klein p.234 s.v. caper\", \"stance\": \"supports\", \"note\": \"'whence Arab. kabbār, ModPers. kabar'.\"},\n      {\"src\": \"LKT\", \"where\": \"Lokotsch no. 978\", \"stance\": \"supports\",\n       \"note\": \"Arabic kabbāra 'aus gr. κάππαρις'; Spanish alcaparra with the Arabic article — the Semitic link in the chain the chart compresses.\"},\n      {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict., caper (2) and appendix §14\", \"stance\": \"contradicts\",\n       \"note\": \"'French from Latin from Greek from Persian: caper (2)' — Skeat makes Persian the ultimate source.\"},\n      {\"src\": \"AFM\", \"where\": \"Addi Shir, whole-book grep for كبر/قبار\", \"stance\": \"silent\", \"note\": \"no entry.\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Latin\", \"words\": \"capparis\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Latin capparis is a straight transliteration-borrowing of Gk. κάππαρις, taken over with its Greek third-declension shape (gen. capparis) and already in Pliny, Nat. Hist. XIII.127 and Columella for the pickled buds. It gave Italian cappero, Old French caspres / French câpre, German Kaper, and (with the Arabic article, through Andalusi Arabic al-kabbāra) Spanish/Portuguese alcaparra. Klein and Lokotsch both give this chain verbatim; the node is uncontroversial.\",\n     \"derivation_fa\": \"«capparis» لاتینی وام‌گیریِ سرراستِ κάππαρις یونانی است که با همان ساختِ صرفیِ یونانی (اسمِ صرفِ سوم، مضاف‌الیه capparis) گرفته شده و پیش از آن در «تاریخ طبیعیِ» پلینیوس (۱۳٫۱۲۷) و در کولوملا برای غنچه‌های سرکه‌خواباندهٔ کبر آمده است. از آن ایتالیایی cappero، فرانسویِ کهن caspres و فرانسویِ câpre، آلمانی Kaper، و از راهِ عربیِ اندلسی با حرفِ تعریف al-kabbāra اسپانیایی و پرتغالیِ alcaparra پدید آمده است. کلاین و لوکوچ هر دو همین زنجیره را می‌آورند؛ این گره اختلافی ندارد.\",\n     \"sources\": [\"https://www.etymonline.com/word/caper\"],\n     \"ref_check\": [\n      {\"ref\": \"KLN:234\", \"status\": \"supports\",\n       \"note\": \"'fr. L. capparis [whence also It. cappero (whence OF. caspres, F. câpre) and G. Kaper], fr. Gk. κάππαρις'.\"},\n      {\"ref\": \"AFM:131\", \"status\": \"not_found\",\n       \"note\": \"Same as node #1: Addi Shir p.131 (leaf 139) has no كبر/capparis entry, and the book contains none anywhere.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"LKT\", \"where\": \"Lokotsch no. 978\", \"stance\": \"supports\",\n       \"note\": \"'Die übrigen Formen kommen dagegen unmittelbar über lat. capparis aus dem gr. Grundwort'.\"},\n      {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century s.v. caper\", \"stance\": \"supports\", \"note\": \"'[... capparis; Gr. kapparis, a caper.]'\"},\n      {\"src\": \"SKT\", \"where\": \"Skeat s.v. caper (2), leaf 87\", \"stance\": \"supports\", \"note\": \"'(F.-L.-Gk.-...) ... L. capparis. — Gk. κάππαρις' — the Latin-from-Greek step is agreed by all sides.\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"English\", \"words\": \"caper\", \"verdict\": \"confirmed\",\n     \"derivation\": \"English caper 'caper bud' is late 14th c. Middle English caperis / caperes, borrowed from Latin capparis (partly through Old French câpre); the final -s of caperis was reanalysed as the English plural marker and dropped, producing a new singular caper — the same back-formation as in pea from pease and cherry from OF cerise. It is unrelated to the homonym caper 'to leap', which is a shortening of capriole (Latin caper 'he-goat'). Klein states the reanalysis explicitly. The node carries no reference in the book.\",\n     \"derivation_fa\": \"«caper» انگلیسی به‌معنیِ غنچهٔ کبر، در پایانِ سدهٔ چهاردهم میلادی به‌صورتِ caperis/caperes در انگلیسی میانه از capparis لاتینی (تا اندازه‌ای از راهِ câpre فرانسوی) وام گرفته شده است؛ سپس «س»ِ پایانیِ caperis را نشانهٔ جمعِ انگلیسی پنداشتند و انداختند و مفردِ تازهٔ caper ساخته شد — همان اشتقاقِ واژگونه‌ای که در pea از pease و cherry از cerise فرانسوی رخ داده است. این واژه با هم‌آوایِ خود caper «جست‌وخیز کردن» (کوتاه‌شدهٔ capriole از caper لاتینی «بزِ نر») پیوندی ندارد. کلاین همین بازتحلیل را روشن می‌گوید. این گره در کتاب مأخذی ندارد.\",\n     \"sources\": [\"https://www.etymonline.com/word/caper\"],\n     \"ref_check\": [\n      {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the book gives no reference for this node.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"Klein p.234 s.v. caper\", \"stance\": \"supports\",\n       \"note\": \"'ME. caperis, caperes, fr. L. capparis ... The -s in ME. was mistaken for the pl. and was consequently dropped.'\"},\n      {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls s.v. caper²\", \"stance\": \"supports\",\n       \"note\": \"'The flower-buds of Capparis spinosa, often preserved in vinegar and used as a condiment ... [< F. câpre, < L. capparis ...]'\"},\n      {\"src\": \"SKT\", \"where\": \"Skeat s.v. caper (2)\", \"stance\": \"supports\", \"note\": \"'(F.-L.-Gk.-Pers.)' — same Latin-French-English end of the chain.\"}\n     ]\n    }\n   ]\n  },\n  {\n   \"entry\": 3,\n   \"root\": \"Kapŭl\",\n   \"verdict\": \"plausible\",\n   \"modern_form\": \"Middle Persian Kābul / Kāwul [kʾpwl] 'Kabul' (Old Persian form unattested)\",\n   \"note\": \"The toponym is genuinely ancient — Vedic Kubhā (the Kabul river), Greek Κωφήν (Kophen) for the same river, Ptolemy's Καβολῖται (a people) and Κάβουρα (a city) in that region, and Middle Persian kʾpwl — but there is no attested Old Persian *Kāpul: Kent's Old Persian lexicon and Tolman's Ancient Persian Lexicon have no such word, and the Achaemenid inscriptions name the region as Gandāra/Θataguš, not Kabul. Wiktionary calls Persian کابل 'of unknown origin'. So the chain of forms Nourai draws is right, but the language label of the root box ('Old Persian') is an extrapolation from Moʿin's aʿlām volume rather than an attested form; that is why this is 'plausible' rather than 'confirmed'. The chart's NOTE about English 'gypsy' is correct as it stands: gypsy is aphetic for Egyptian, unrelated to Kabul.\",\n   \"note_fa\": \"این نام‌جای به‌راستی کهن است — «کُبها» در وداها (رودِ کابل)، Κωφήν یونانی برای همان رود، و در «جغرافیای» بطلمیوس مردمی به‌نامِ Καβολῖται و شهری به‌نامِ Κάβουρα در همان ناحیه، و در فارسی میانه kʾpwl — ولی هیچ صورتِ گواهی‌شده‌ای از پارسی باستان به‌شکلِ *Kāpul در دست نیست: در واژه‌نامهٔ پارسی باستانِ کنت و در «واژه‌نامهٔ پارسی کهن» تولمن چنین واژه‌ای نیست و در سنگ‌نبشته‌های هخامنشی آن ناحیه «گنداره» و «ثتگوش» خوانده می‌شود. ویکی‌واژه «کابل» فارسی را «با خاستگاه نامعلوم» می‌داند. پس زنجیرهٔ صورت‌هایی که نورایی کشیده درست است، ولی برچسبِ زبانیِ جعبهٔ ریشه («پارسی باستان») برداشتی از جلدِ اعلامِ معین است نه صورتی گواهی‌شده؛ از این‌رو داوری «با احتیاط پذیرفتنی» است. یادداشتِ نمودار دربارهٔ واژهٔ انگلیسیِ gypsy درست است: این واژه کوتاه‌شدهٔ Egyptian است و با کابل پیوندی ندارد.\",\n   \"sources\": [\"https://en.wiktionary.org/wiki/Kabul\"],\n   \"ref_check\": [\n    {\"ref\": \"MON6:1487\", \"status\": \"not_checked\",\n     \"note\": \"Moʿin's Farhang-e Farsi vol. 6 (the aʿlām/proper-name volume) is not available in any form on disk or online — see MISSING_REFERENCES.md ('Buy: MON 6-vol print set (needed for vols 5-6 اعلام ...)'); only the 2-vol Adena reprint of the lexicon volumes is on disk, and it has no proper names.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, lexicon; grep 'kabul/kapul/kāpul'\", \"stance\": \"silent\",\n     \"note\": \"no such entry; the Achaemenid corpus has no name for Kabul (same result in TLM, Tolman's Ancient Persian Lexicon).\"},\n    {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II, glossary (NYB_vol2_glossary.txt line 2271)\", \"stance\": \"supports\",\n     \"note\": \"'Kavul [kʾpwl; inser. kʾwly] Kabul' with text references — the Middle Persian form is attested, in books and in inscriptions.\"},\n    {\"src\": \"HJB\", \"where\": \"Hobson-Jobson s.v. CABUL, CAUBOOL (HJB.txt line 4656)\", \"stance\": \"supports\",\n     \"note\": \"'This name (Kabul) of the chief city of N. Afghanistan ... is perhaps traceable in Ptolemy, who gives in that same region a people called Καβολῖται, and a city called Κάβουρα.'\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Pahlavi\", \"words\": \"kâpŭl\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Middle Persian Kābul, written kʾpwl in Book Pahlavi and kʾwly in the inscriptional script, is securely attested — Nyberg's glossary to the Manual of Pahlavi lists 'Kavul [kʾpwl; inser. kʾwly] Kabul' with references, and the name occurs in the Šahrestānīhā ī Ērānšahr and in the Kaʿba-ye Zardošt inscription's list of provinces. In Book Pahlavi orthography ⟨p⟩ regularly stands for the spirantised /w/~/b/, so kʾpwl is to be read Kāwul/Kābul; that spelling is precisely why the New Persian form is کابل with b. Nourai's Pahlavi node is right (his root box's 'Old Persian' antecedent is the doubtful part, not this).\",\n     \"derivation_fa\": \"«کابل» در فارسی میانه، با نویسهٔ کتابیِ kʾpwl و نویسهٔ کتیبه‌ایِ kʾwly، به‌روشنی گواهی شده است: نیبرگ در واژه‌نامهٔ «راهنمای پهلوی» می‌آورد «Kavul [kʾpwl؛ کتیبه‌ای kʾwly] کابل» و نام در «شهرستان‌های ایرانشهر» و در فهرستِ شهرهای کتیبهٔ کعبهٔ زرتشت آمده است. در املای پهلویِ کتابی «پ» به‌قاعده نمایندهٔ /w/ ~ /b/ سایشی است، پس kʾpwl را باید Kāwul/Kābul خواند؛ همین املا است که «ب»ِ «کابل» فارسی نو را توضیح می‌دهد. این گرهِ نورایی درست است (آنچه محلِّ تردید است جعبهٔ «پارسی باستان» بالای آن است، نه این گره).\",\n     \"sources\": [\"https://en.wiktionary.org/wiki/Kabul\"],\n     \"ref_check\": [\n      {\"ref\": \"MON6:1487\", \"status\": \"not_checked\", \"note\": \"Moʿin vol. 6 (aʿlām) unavailable — see the entry-level ref_check.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II, glossary s.v. Kavul\", \"stance\": \"supports\",\n       \"note\": \"'Kavul [kʾpwl; inser. kʾwly] Kabul P2: 2. 11; 9. 17. 31. 115' — form and reading confirmed.\"},\n      {\"src\": \"PHD\", \"where\": \"MacKenzie 1971, grep kʾpwl / Kabul\", \"stance\": \"silent\",\n       \"note\": \"MacKenzie's dictionary excludes proper names; the only kʾpwl-like entry is 'kapur [kʾpwl | Ar. kāfūr] camphor', a homograph, not the toponym.\"},\n      {\"src\": \"HJB\", \"where\": \"Hobson-Jobson s.v. CABUL\", \"stance\": \"supports\",\n       \"note\": \"traces the name back through Ptolemy's Κάβουρα, i.e. it is pre-Islamic, consistent with a Middle Persian attestation.\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Persian\", \"words\": \"Kâbol «کابل»; kowlî «کولی»; kâbolî «کابلی ۲»\", \"verdict\": \"confirmed\",\n     \"derivation\": \"All three words hold. (a) کابل Kābol continues MP Kābul unchanged (Book Pahlavi kʾpwl); it is the city on the Kabul river, the Kubhā of the Rigveda. (b) کولی kowlī 'gypsy' is a contraction of کابلی kābolī via کاولی kāwolī — the intervocalic b weakened to w and the sequence āwo- monophthongised to ow-, then the first syllable was lost; Moʿin's Farhang-e Farsi gives it in exactly that shape, 'کولی: kōlī, -āwlī [= کاولی = کابلی؟]', and Wiktionary explains the name as arising 'because when they first appeared it was wrongly believed that they were from Kabul'. The chart's own bracketed variant «کابلی ۱» is that homonym. (c) کابلی kābolī 'a dried fruit from Kabul' is the nisba adjective, used elliptically for هلیلهٔ کابلی halīla-ye kābolī, the chebulic myrobalan (Terminalia chebula), which reached Persia by the Kabul route — Moʿin lists 'هلیلهٔ کابلی' as one of the kinds of halīla, and Hobson-Jobson notes 'the Persian name, which is Halīlaʾi-Kābulī. It can hardly have been a product of Kabul, but may have been imported into Persia by that route, whence the name, as calicoes got their name from Calicut.' The chart's NOTE on English 'gypsy' is also right: gypsy is aphetic Egyptian (Middle English gipcyan), a separate folk-geographic mistake made in Europe, and it does not derive from Kabul — Nourai says so himself.\",\n     \"derivation_fa\": \"هر سه واژه درست است. الف) «کابل» بی‌دگرگونی دنبالهٔ Kābul فارسی میانه (نویسهٔ kʾpwl) است؛ شهری بر رودِ کابل، همان «کُبها»ی ریگ‌ودا. ب) «کولی» کوتاه‌شدهٔ «کابلی» از راهِ «کاولی» است: «ب» میان دو واکه به «و» نرم شده، خوشهٔ āwo به ow تک‌واکه گشته و هجای نخست افتاده است؛ معین در «فرهنگ فارسی» دقیقاً همین را می‌آورد: «کولی: kōlī, -āwlī [= کاولی = کابلی؟]»، و ویکی‌واژه علتِ نام‌گذاری را چنین می‌گوید که «چون نخست پیدا شدند به‌خطا پنداشتند که از کابل‌اند». گونهٔ «کابلی ۱» در کروشهٔ نمودار همین هم‌آوا است. ج) «کابلی ۲» صفتِ نسبی است که به‌جای «هلیلهٔ کابلی» (Terminalia chebula) به‌کار می‌رود؛ این میوهٔ خشک از راهِ کابل به ایران می‌رسیده است. معین «هلیلهٔ کابلی» را یکی از گونه‌های هلیله می‌شمارد، و «هابسن‑جابسن» می‌نویسد نامِ فارسیِ آن «هلیلهٔ کابلی» است و «به‌سختی می‌توان آن را فرآوردهٔ کابل دانست، ولی شاید از آن راه به ایران آورده می‌شده و نام از همین‌جاست، چنان‌که پارچهٔ calico نام خود را از کالیکوت گرفت». یادداشتِ نمودار دربارهٔ gypsy نیز درست است: این واژه صورتِ کوتاه‌شدهٔ Egyptian است (انگلیسی میانه gipcyan) و از کابل نیامده — خودِ نورایی هم همین را می‌گوید.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/Kabul\",\n      \"https://en.wiktionary.org/wiki/%DA%A9%D9%88%D9%84%DB%8C\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"MON6:1487\", \"status\": \"not_checked\", \"note\": \"Moʿin vol. 6 (aʿlām) unavailable; but the lexicon volumes on disk do carry the two common nouns (see consulted).\"},\n      {\"ref\": \"AHD:589\", \"status\": \"not_checked\",\n       \"note\": \"AHD:589 is a main-dictionary page of the New College Edition (the 'gypsy' entry), available only in archive.org lending copies; the local AHD file is the IE-roots appendix. Nourai's use of it is only for the 'gypsy < Egyptian' remark, which is standard and confirmed by Klein and Etymonline.\"},\n      {\"ref\": \"VFO:24\", \"status\": \"not_checked\",\n       \"note\": \"VFO is an unresolved abbreviation in this project's bibliography (MISSING_REFERENCES.md line 110: 'VFO | (unresolved abbreviation, probably = VOP) | skipped'); no book could be identified to check.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"MON\", \"where\": \"Farhang-e Farsi s.v. کولی (MON_part2.txt line 28274) and هلیلهٔ کابلی (line 90897)\", \"stance\": \"supports\",\n       \"note\": \"'کولی: kōlī, -āwlī [- کاولی - کابلی؟] (ص نسبی) غرشمال، ارقه ...' — Moʿin derives kōlī from kāwolī/kābolī (with a query); and 'یکی از گونه‌های هلیله. هلیلهٔ کابلی: (گیا.)' for the dried fruit.\"},\n      {\"src\": \"HJB\", \"where\": \"Hobson-Jobson s.v. MYROBALAN (HJB.txt line 15270) and CHEBULI (line 5839)\", \"stance\": \"supports\",\n       \"note\": \"'The derivation of this name ... is confirmed by the Persian name, which is Halīlaʾi-Kābulī ... may have been imported into Persia by that route, whence the name'; and 'CHEBULI ... The true etymology is probably Kābulī ... i.e. \\\"from Cabul\\\".'\"},\n      {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II s.v. Kavul\", \"stance\": \"supports\", \"note\": \"the Middle Persian antecedent of کابل.\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"English\", \"words\": \"Kabul; chebule\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Kabul is simply the English spelling of the Persian/Pashto place-name, in English from the 16th c. (Barros 1552 'a Cidade Cabol'; Babur's memoirs in translation), with the stress on the first, long syllable as Hobson-Jobson insists. chebule 'the dried fruit of Terminalia chebula, the chebulic myrobalan' came in by the drug trade, not by conquest: Arabo-Persian کابلی kābulī 'from Kabul' → Medieval Latin/Italian chebuli (Pegolotti, c.1343, 'Chebuli mirabolani') → French chébule → English chebule, whence the adjective chebulic and the botanical epithet chebula. Klein p.272 states it: 'chebule, n., the dried fruit of Terminalia chebula. — F. chébule, fr. Arabo-Pers. kābulī, lit., \\\"from (the city of) Kabul\\\".' Funk & Wagnalls agrees ('< F. chebule, < Hind. Kabuli, of Cabul'), and Thévenot (c.1666) already explains the name from the province of Kabul.\",\n     \"derivation_fa\": \"«Kabul» تنها نویسهٔ انگلیسیِ همان نام‌جایِ فارسی و پشتوست و از سدهٔ شانزدهم در انگلیسی دیده می‌شود (باروش در ۱۵۵۲: «a Cidade Cabol»). اما «chebule» به‌معنیِ میوهٔ خشکِ Terminalia chebula (هلیلهٔ کابلی) از راهِ بازرگانیِ داروها به اروپا رسیده است: «کابلی» عربی‑فارسی ← chebuli در لاتینِ سده‌های میانه و ایتالیایی (پگولوتی، حدودِ ۱۳۴۳: «Chebuli mirabolani») ← chébule فرانسوی ← chebule انگلیسی، و از آن صفتِ chebulic و نامِ گیاه‌شناسیِ chebula. کلاین در ص ۲۷۲ صریح می‌گوید: «chebule ... از فرانسویِ chébule، از عربی‑فارسیِ kābulī، لفظاً \\\"از (شهرِ) کابل\\\"». فرهنگ Funk & Wagnalls نیز همین را می‌آورد، و تِوِنو (حدودِ ۱۶۶۶) خودِ نام را از ولایتِ کابل توضیح داده است. ادعای نورایی درست است.\",\n     \"sources\": [\"https://en.wiktionary.org/wiki/Kabul\"],\n     \"ref_check\": [\n      {\"ref\": \"KLN:272\", \"status\": \"supports\",\n       \"note\": \"KLN_1966.txt line 7295: 'chebule, n., the dried fruit of Terminalia chebula. — F. chebule, fr. Arabo-Pers. kābulī, lit., \\\"from (the city of) Kabul\\\".' The leaf position (2 printed pages/leaf) puts it at pp. ~271-273, matching Nourai's 272.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"HJB\", \"where\": \"Hobson-Jobson s.v. CHEBULI (HJB.txt line 5839) and CABUL (line 4656)\", \"stance\": \"supports\",\n       \"note\": \"'CHEBULI. The denomination of one of the kinds of Myrobolans exported from India. The true etymology is probably Kābulī, as stated by Thevenot, i.e. \\\"from Cabul\\\"', with the 1343 Pegolotti and c.1666 Thévenot citations.\"},\n      {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls s.v. che-bule (FSD_vol1.txt line 63560)\", \"stance\": \"supports\",\n       \"note\": \"'che-bule ... The dried astringent prune-like fruit of an East-Indian tree (Terminalia chebula) of the myrobalan family ... [< F. chebule, < Hind. Kabuli, of Cabul.] — chebulic, a.'\"},\n      {\"src\": \"KLN\", \"where\": \"Klein p.272 s.v. chebule\", \"stance\": \"supports\", \"note\": \"'fr. Arabo-Pers. kābulī, lit., \\\"from (the city of) Kabul\\\"'.\"}\n     ]\n    }\n   ]\n  }\n ]\n}\n\nwith io.open(\"/home/sfmqrb/git/rishe/data/verification/page-241.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(data, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"ok\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/w241.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-241.json > /dev/null && echo \"JSON OK\" && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 241"
}
```


### [2026-09-06T16:03:26.493Z] TOOL RESULT

```
ok
JSON OK
nodes verified: 12/12
node verdicts: {'confirmed': 10, 'plausible': 2}
root verdicts: {'confirmed': 2, 'plausible': 1}
ref checks: {'supports': 8, 'partial': 2, 'not_found': 3, 'not_checked': 7}
books consulted: {'supports': 32, 'contradicts': 2, 'partial': 1, 'silent': 4} | by book: {'KLN': 5, 'HUB': 3, 'PHD': 3, 'NYB': 3, 'BQT': 3, 'SKT': 3, 'HJB': 3, 'WLD': 2, 'HRN': 2, 'MON': 2, 'WEB': 2, 'LKT': 2, 'FSD': 2, 'BRT': 1, 'POK': 1, 'AHD': 1, 'AFM': 1}
```


## [2026-09-06T16:03:51.241Z] AGENT

Done — `data/verification/page-241.json` written, `verify_check.py 241` reports **0 PROBLEM lines** (12/12 nodes).

**Page 241 (book p. 211) — 3 entries, 12 nodes**
- Node verdicts: confirmed 10, plausible 2. Root verdicts: confirmed 2, plausible 1.
- Ref checks: 8 supports, 2 partial, 3 not_found, 7 not_checked. 39 `consulted` entries across 17 books.

**Disputed / transcription_suspect:** none.

**Plausible (with reasons):**
- *Kapŭl* ROOT — the label "Old Persian" is unattested. Kent and Tolman have no Kabul word; the name is Vedic Kubhā / Ptolemy Καβολῖται, Κάβουρα, and MP kʾpwl (Nyberg). Forms right, language label extrapolated from Moʿin's aʿlām volume.
- *Kapho* #2 Pahlavi **sumb** ← Av. safa- — Horn (the cited p. 164) says only "Urverwandtschaft … anzunehmen" (cognacy, not descent), and Hübschmann §745 objects outright: "Zd. safa- … lässt sich schwer mit np. sum, sunb = ap. *sumba- oder *sumpa- … vereinigen." Wiktionary still files MP sumb under PIr *cafáh, so the family holds but the -mb- is unexplained.
- *Kapho* #4 Persian **safal** ← Av. safa- — word and all three variants confirmed (Moʿin s.v. سپل sopol "سم شتر، ناخن فیل"; Borhan v3 s.v. شفل), but no source states the Avestan derivation; Tabari šoppol and the -p- point to a dialectal formation.

**Notable finding (chart contradicts its own note):** in *Kapparis* the arrow makes Greek the source of Persian کبر, while the box's NOTE (KGW:98) claims Old Persian → Greek. Klein 234, Lokotsch 978, Etymonline and — decisively — Moʿin's own footnote at BQT 1587 ("نامهای عربی کبر و کبّار … از یونانی آمده‌اند … alcaparra") back the **arrow**; Skeat's appendix ("French from Latin from Greek from Persian: caper (2)") backs the **note**. I graded the arrow confirmed and evaluated the note as the minority view.

**Reference-page arithmetic confirmed:** BQT:1163 = BQT_v2 leaf 627 (سم + Moʿin's etymological footnote) and BQT:1587 = BQT_v3 leaf 379 (کبر) both land exactly on Nourai's page numbers.

**Not checkable:** MON6:1487 (Moʿin vol. 6 aʿlām — not on disk or online), AHD:199 / AHD:589 (main-dictionary pages, lending-only), KGW:98 (Google Books preview only), VFO:24 (unresolved abbreviation in MISSING_REFERENCES.md). **not_found:** AFM:131 — Addi Shir's p. 131 (leaf 139) has كنداكر/الكندوج/الكندر, and a whole-book grep finds no كبر at all; SOD:65 — neither entry 65 nor printed p. 65 of Gharib has a hoof word.

**Extraction errors for the owner:** none. I read `site/pages/241.jpg`; the JSON is faithful to the printed page. One structural nuance only: on the page «کابلی ۱» sits in parentheses immediately after *kowlî* (i.e. کولی = کابلی ۱), but the JSON records it as a node-level `script_extra` — harmless, and the chart text preserves it.
