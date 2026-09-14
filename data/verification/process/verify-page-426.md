# Verification process log — verify-page-426


## [2026-09-14T01:21:43.943Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 426 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-426.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-426.json. Write /home/sfmqrb/git/rishe/data/verification/page-426.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 426` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T01:21:44.869Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T01:21:45.822Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T01:21:45.863Z] TOOL RESULT

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
226	Several agents run at the same time and share the scratchpad and `/tmp`, so every temporary
227	file you create must carry your page number in its name (e.g. `e0-363.json`, `pg363.png`,
228	`draft-363.json`), never a bare `e0.json` or `entry.json` — another agent will overwrite it.
229	
230	```json
231	{
232	  "pdf_page": 126,
233	  "book_page": 96,
234	  "verified_by": "claude-opus-5",
235	  "verified_on": "2026-09-05",
236	  "entries": [
237	    {
238	      "entry": 0,
239	      "root": "Dheigh, Dhigha",
240	      "verdict": "confirmed",
241	      "modern_form": "PIE *dʰeyǵʰ- 'to knead, form (clay)'",
242	      "note": "Pokorny 244 dheiĝh-; AHD dheigh-. Root, language label and gloss all correct.",
243	      "note_fa": "ریشهٔ هندواروپایی آغازین *dʰeyǵʰ- «خمیر کردن، شکل دادن (گِل)» … ادعای نورایی درست است.",
244	      "sources": ["https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dʰeyǵʰ-"],
245	      "ref_check": [{"ref": "POK:244", "status": "supports", "note": "…"}],
246	      "consulted": [{"src": "WLD", "where": "Bd. I 833", "stance": "supports", "note": "…"}],
247	      "nodes": [
248	        {
249	          "id": 6,
250	          "lang": "Avestan",
251	          "words": "pairi-daeza",
252	          "verdict": "confirmed",
253	          "derivation": "Av. pairi-daēza- 'walled enclosure' = pairi 'around' (PIE *per-) + daēza- 'wall' …",
254	          "derivation_fa": "«پردیس» … اوستایی pairi-daēza- «دیوارکشیده، باغِ محصور» از pairi «پیرامون» و daēza- «دیوار» …",
255	          "sources": ["https://en.wiktionary.org/wiki/pairidaēza"],
256	          "ref_check": [{"ref": "POK:244", "status": "supports", "note": "…"}],
257	          "consulted": [{"src": "BRT", "where": "col. 866", "stance": "supports", "note": "…"}]
258	        }
259	      ]
260	    }
261	  ]
262	}
263	```
264	
265	Rules:
266	- Include EVERY node of every non-redirect entry on the page (even empty-word pass-through
267	  nodes like `[Latin] refs=None |` — give them a one-line derivation and a verdict).
268	- `words` = the transliterations of the node joined by "; " (copy from the chart).
269	- `derivation` must be specific: forms, sound changes, dates/eras, texts or peoples,
270	  semantic shifts. 1–5 sentences. No hand-waving like "derived regularly".
271	- Keep `note` on the entry for root-level comments and for anything cross-cutting.
272	- If a node lists several words, cover each word; if they differ in verdict, use the worst
273	  verdict for the node and explain per word in `derivation`.
274	- Where the chart's own NOTE already records a dispute, evaluate it: say which side modern
275	  scholarship takes.
276	- Every node has `ref_check` (array, may contain a single `not_checked` item) AND `consulted`
277	  (array) AND `derivation_fa` (string); every entry has `note_fa`.
278	- Valid JSON only. Test it with `python3 -m json.tool` before finishing, then run
279	  `python3 /home/sfmqrb/git/rishe/tools/verify_check.py <pdf page>` — it must show 0 PROBLEM lines.
280	- When done, reply with a SHORT summary (≤ 15 lines): counts of verdicts per page, and a
281	  bullet per `disputed` / `transcription_suspect` item (root, word, one-line reason), plus
282	  any extraction errors (JSON differs from the printed page) the owner must fix.
283	  Do not paste the JSON back into your reply.
284	
```


## [2026-09-14T01:21:46.324Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-426.txt"
}
```


### [2026-09-14T01:21:46.345Z] TOOL RESULT

```
1	=== PDF page 426 (book page 396) ===
2	--- entry 0 ---
3	ROOT Rk-so -> redirect to Rk-tho
4	--- entry 1 ---
5	ROOT [Indo-European] Rk-tho, Rk-so : bear (animal)  (refs POK:875; SOD:70)
6	#1 (parent #0) [Avestan] refs=POK:875 | areša : bear ; areša-ama : with power of a bear ☞Ome
7	  #2 (parent #1) [Persian] refs=BQT:31,733 | xers «خرس» : bear ; Aršâm «ارشام» : "with power of a bear", a male name | extra: آرشام
8	#3 (parent #0) [Greek] refs=AHD | arktos : bear ; arkticos : northern bear-shaped constellation
9	  #4 (parent #3) [Latin] refs=None | arcticus : north pole
10	    #5 (parent #4) [English] refs=None | Arctic
11	#6 (parent #0) [Celtic] refs=AHD | artho : bear
12	  #7 (parent #6) [English] refs=None | Arthur
13	#8 (parent #0) [Sogdian] refs=SOD:70 | `ššh : bear
14	--- entry 2 ---
15	ROOT Ros -> redirect to Eres 1
16	--- entry 3 ---
17	ROOT Routo -> redirect to Reuto
18	--- entry 4 ---
19	ROOT Rů 1 -> redirect to Reu 1
20	--- entry 5 ---
21	ROOT Rů 2 -> redirect to Reu 2
22	--- entry 6 ---
23	ROOT Rů 3 -> redirect to Rewe
24	--- entry 7 ---
25	ROOT Rut -> redirect to Reuto
26	--- entry 8 ---
27	ROOT [Syriac] R.y.m : to depart  (refs SAP:617)
28	#1 (parent #0) [Arabic] refs=FVQ:262 | r.y.m : to depart ; Maryam : mother of Jesus
29	  #2 (parent #1) [Persian] refs=MON:4053 | Maryam «مریم» : Mary
30	#3 (parent #0) [Hebrew] refs=AHD:802,1530; FVQ:262; KLN:943 | Miryâm : "rebellion", sister of Moses, mother of Jesus
31	  #4 (parent #3) [Aramaic] refs=None | Maryâm
32	    #5 (parent #4) [Greek] refs=None | Maria, Mariam
33	      #6 (parent #5) [English] refs=AHD:802; KLN:943 | Mary, Marilyn, Maria, Marvin ; Marianne, marijuana, marihuana
34	
```


## [2026-09-14T01:21:48.973Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-426.json",
 "description": "Read source JSON for page 426"
}
```


### [2026-09-14T01:21:49.086Z] TOOL RESULT

```
{
  "pdf_page": 426,
  "book_page": 396,
  "entries": [
    {
      "root": {"name": "Rk-so", "redirect": "Rk-tho"},
      "nodes": []
    },
    {
      "root": {
        "name": "Rk-tho, Rk-so",
        "lang": "Indo-European",
        "refs": "POK:875; SOD:70",
        "gloss": "bear (animal)"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:875",
          "words": [
            {"translit": "areša", "gloss": "bear", "script": null},
            {"translit": "areša-ama", "gloss": "with power of a bear", "script": null, "see": ["Ome"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:31,733",
          "words": [
            {"translit": "xers", "gloss": "bear", "script": "خرس"},
            {"translit": "Aršâm", "gloss": "\"with power of a bear\", a male name", "script": "ارشام"}
          ],
          "script_extra": "آرشام",
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD",
          "words": [
            {"translit": "arktos", "gloss": "bear", "script": null},
            {"translit": "arkticos", "gloss": "northern bear-shaped constellation", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Latin",
          "refs": null,
          "words": [
            {"translit": "arcticus", "gloss": "north pole", "script": null}
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
            {"translit": "Arctic", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Celtic",
          "refs": "AHD",
          "words": [
            {"translit": "artho", "gloss": "bear", "script": null}
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
            {"translit": "Arthur", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 0,
          "lang": "Sogdian",
          "refs": "SOD:70",
          "words": [
            {"translit": "`ššh", "gloss": "bear", "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {"name": "Ros", "redirect": "Eres 1"},
      "nodes": []
    },
    {
      "root": {"name": "Routo", "redirect": "Reuto"},
      "nodes": []
    },
    {
      "root": {"name": "Rů 1", "redirect": "Reu 1"},
      "nodes": []
    },
    {
      "root": {"name": "Rů 2", "redirect": "Reu 2"},
      "nodes": []
    },
    {
      "root": {"name": "Rů 3", "redirect": "Rewe"},
      "nodes": []
    },
    {
      "root": {"name": "Rut", "redirect": "Reuto"},
      "nodes": []
    },
    {
      "root": {
        "name": "R.y.m",
        "lang": "Syriac",
        "refs": "SAP:617",
        "gloss": "to depart"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Arabic",
          "refs": "FVQ:262",
          "words": [
            {"translit": "r.y.m", "gloss": "to depart", "script": null},
            {"translit": "Maryam", "gloss": "mother of Jesus", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "MON:4053",
          "words": [
            {"translit": "Maryam", "gloss": "Mary", "script": "مریم"}
          ],
          "note": null,
          "quote": {
            "text": "روح کی گردد فدای آن دمی - کز نسیمش حامله شد مریمی",
            "poet": "Molavî"
          }
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Hebrew",
          "refs": "AHD:802,1530; FVQ:262; KLN:943",
          "words": [
            {"translit": "Miryâm", "gloss": "\"rebellion\", sister of Moses, mother of Jesus", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Aramaic",
          "refs": null,
          "words": [
            {"translit": "Maryâm", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Greek",
          "refs": null,
          "words": [
            {"translit": "Maria, Mariam", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "English",
          "refs": "AHD:802; KLN:943",
          "words": [
            {"translit": "Mary, Marilyn, Maria, Marvin", "gloss": null, "script": null},
            {"translit": "Marianne, marijuana, marihuana", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
```


## [2026-09-14T01:21:49.671Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-14T01:21:49.777Z] TOOL RESULT

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


## [2026-09-14T01:21:54.038Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/page-385.json'))\nprint(json.dumps(d,ensure_ascii=False)[:3000])\n\"",
 "description": "Inspect a recent verified page format"
}
```


## [2026-09-14T01:21:54.817Z] TOOL CALL #6: Bash

```json
{
 "command": "sed -n '1,120p' tools/verify_check.py",
 "description": "Read verify_check"
}
```


### [2026-09-14T01:21:55.195Z] TOOL RESULT

```
{"pdf_page": 385, "book_page": 355, "verified_by": "claude-opus-5", "verified_on": "2026-09-07", "entries": [{"entry": 0, "root": "Peg", "verdict": "plausible", "modern_form": "PIE *peg- / *pōg-, *pōk-s- 'armpit, hip, loin, side' (Pokorny 792); Watkins/AHD lists the same root as *peg- 'breast'", "note": "Pokorny 792 prints the headword as '(peg-:) pog-: pōg-, pōk-s-' and glosses it 'Achsel, Hufte, Lende, Seite' (armpit, hip, loin, side) — the full-grade *peg- is only a bracketed, inferred variant. Nourai's headword 'Peg' with the gloss 'breast' is copied verbatim from the AHD (Watkins) appendix, which prints 'peg-. Breast.' The 'breast' sense in fact rests only on Latin pectus and Tocharian A pässäṃ / B pāścane 'the two breasts'; Sanskrit pakṣa- and Latvian paksis point to 'side, flank'. Modern scholarship (de Vaan via Wiktionary) further doubts that Lat. pectus and Skt. pakṣa- belong together at all. Root is real and the language label is right; the gloss is a one-sided simplification.", "note_fa": "ریشهٔ هندواروپایی آغازین که نورایی آن را Peg با معنای «سینه» آورده، در فرهنگ پوکورنی (ص ۷۹۲) با سرواژهٔ «(peg-:) pog-: pōg-, pōk-s-» و معنای «زیربغل، ران، پهلو» ثبت شده است؛ صورت *peg- تنها گونه‌ای بازسازی‌شده و درون‌کمانک است. معنای «سینه» را نورایی از پیوست ریشه‌های هندواروپایی فرهنگ AHD (واتکینز) گرفته که همان‌جا «Breast» نوشته است، ولی این معنا فقط بر پایهٔ pectus لاتین و pāścane تخاری است، حال آنکه pakṣa- سنسکریت و paksis لتونیایی بر معنای «پهلو، سو» دلالت دارند. افزون بر این، پژوهش امروزی (دِ ڤان، به نقل ویکی‌واژه) در پیوند pectus لاتین با pakṣa- سنسکریت تردید می‌کند. پس: ریشه واقعی است و برچسب زبانی درست، اما معنای داده‌شده یک‌سویه و ساده‌سازانه است — ادعای نورایی با احتیاط پذیرفتنی است.", "sources": ["https://en.wiktionary.org/wiki/%E0%A4%AA%E0%A4%95%E0%A5%8D%E0%A4%B7", "https://en.wiktionary.org/wiki/pectus"], "ref_check": [{"ref": "POK:792", "status": "partial", "note": "Pokorny IEW p.792 (local POK_03.txt, form-feed leaf 25) reads: '(peg-:) pog-: pōg-, pŏk-s- \"Achsel, Hufte, Lende, Seite\". Ai. pákṣa- m. \"Schulter, Flugel\" und \"Seitenpfosten\", pákṣas- n. \"Seite\"; lat. pectus \"Brust\"; lett. paksis \"Hausecke\"; toch. A pässäṃ, B päścane \"die beiden Bruste\" ... WP. II 3 f., WH. II 270.' The page number is exact; the gloss is not 'breast'."}], "consulted": [{"src": "AHD", "where": "Watkins 1985, s.v. peg-", "stance": "supports", "note": "'peg-. Breast. 1. Suffixed variant form *pek-tos- in Latin pectus, breast: PECTORAL; EXPECTORATE, PARAPET. 2. Possibly suffixed variant form *pek-so- in Sanskrit paksah, wing: PUNKA. [Pok. (peg-), pog- 792.]' — this is verbatim Nourai's chart (grep '^peg-' AHD_watkins1985.txt line 820)."}, {"src": "WLD", "where": "Walde-Pokorny II 3-4 (WLD_Bd2_pages.txt leaf 8)", "stance": "partial", "note": "Entry headed 'pag-' (their spelling) with 'ai. pajasyá- n. Bauchgegend, Weichen, russ. pachu \"Leistengegend\", pacha \"Achselhohle\" ... ein io-St. *pagio- in cech. paze \"Arm\"' — again 'flank/armpit', no 'b
```


### [2026-09-14T01:21:55.235Z] TOOL RESULT

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


## [2026-09-14T01:22:33.961Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nls | head -60\necho ---\ngrep -n \"r̥k̑þos\\|rk̂þos\\|ṛk̑þo\\|Bär\" POK_03.txt | head -20",
 "description": "List refs and grep Pokorny for bear root"
}
```


### [2026-09-14T01:22:34.064Z] TOOL RESULT

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
---
1275:Ai.  rdksas-  n.  ,Qua],  Quälgeist,  Unhold'^  av.  ra§ah-  ^Schädigung,  Schaden  , bes.  der  im  andern  Leben',  raSayeiti  ^schädigt' ;  gr.  igex^o)  ^zerre  und  beutle^ hin  und  her^  (der  Sturm  das  Schiff);  "Eqsx&svg  ;der  Erderschütte^er^ WP.  II  362;  dazu  fkpos  ,Bär'  als  ^Schädiger'.
1438:rkPo-s  ,Bär'  (oder  rk-s-o-s  neben  rk-to-s  ?).
1439:Ai.  fksa-  ra.  ,Bär^  (dazu  ein  neues  fem.  rhsl  ,Bärin^)  =  jav.  arsa-, osset.  ars,  arm.  arj  (beeinflußt  von  arjn  ,dunkelbraun'),  alb.  ari,  gr. agy-rog,  jünger  ä'^xog,  dazu  (?)  der  VN  l^Qy.ccdsg,  mir.  art^  cymr.  arth ^Bär',  gall.  Deae  Artioni  ^Bärengöttin^^  lat.  ursus  ,Bär',  vielleicht  hitt. hartagga-  Name  eines  Raubtiers ;  aquitan.  PN  Harsus,  bask.  hartz  ,Bär^ sind  kelt.  L\v.;  npers.  xirs  ,Bär^  soll  auf  iran.  "^rsa-  =  idg.  rko-  weisen^ worauf  auch  osset.  ars  zurückgehen  könnte.
1440:WP.  II  322,  WH.  II  842,  Specht  KZ  66,  26  f.,  Idg.  Dekl.  239  f.,  der den  Bären  als  , Zerstörer,  Schädiger^  deutet,  zu  ai.  rdksäs-,  n.  ,Zerstörung^, av.  ra§-  ,beschädigen^  (S.  864) ;  vgl.  auch  Frisk  Gr.  et.  Wb.  141  f.
```


## [2026-09-14T01:22:36.260Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources\npython3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nfor k in ['POK','SOD','BQT','MON','FVQ','KLN','AHD','SAP','BRT','HRN','HUB','PHD','AFM','LKT','SKT','WEB','FSD','IEC','SYN','WLD','NYB','ARY']:\n    print(k, json.dumps(d.get(k),ensure_ascii=False)[:600])\n\"",
 "description": "Read refs_online entries"
}
```


### [2026-09-14T01:22:37.443Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_
SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id=
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په
FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sou
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,
SAP {"title": "Ahmad Sayyah, Farhang-e Sayyah / Farhang-e Bozorg-e Jame'-e Novin (Persian translation of al-Munjid), 3 vols, Eslam 1368/1989", "kind": "purchase", "url": "https://fidibo.com/book/142427 (vol.1, 1152 pp) ; https://fidibo.com/book/142430 (vol.2, 1206 pp) — PDF ebook, ~300,000 toman each, free sample", "lookup_hint": "Not found (archive.org has Bandar-Rigi's منجد الطلاب translation, abo_abdrahman_kordi_barid_20150501_1718, and the Arabic al-Munjid on noorlib.ir/book/info/32878 — usable to check the Arabic-side content, not Sayyah's pages).", "local_file": null, "page_offset": null, "c
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-
AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/
LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/W
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it
```


## [2026-09-14T01:22:43.664Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources\npython3 -c \"\nimport json;d=json.load(open('refs_online.json'))\nprint(d['POK'].get('page_offset'));print(d['POK'].get('lookup_hint'))\nprint('---SOD');print(json.dumps(d['SOD'],ensure_ascii=False))\nprint('---BQT off');print(d['BQT'].get('page_offset'));print(d['BQT'].get('lookup_hint'))\nprint('---MON');print(d['MON'].get('page_offset'));print(d['MON'].get('lookup_hint'))\nprint('---AHD');print(d['AHD'].get('page_offset'),d['AHD'].get('lookup_hint'))\nprint('---KLN');print(d['KLN'].get('page_offset'),d['KLN'].get('lookup_hint'))\nprint('---FVQ');print(d['FVQ'].get('page_offset'),d['FVQ'].get('lookup_hint'))\n\"",
 "description": "Get page offsets"
}
```


### [2026-09-14T01:22:44.868Z] TOOL RESULT

```
POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\data\ie\pokorny&root=config
---SOD
{"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/SogdianDictionary for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD.txt"], "page_offset": "printed page ≈ leaf − 66 in SOD_pages.txt (0-based \\f blocks; 645 leaves; English intro precedes)", "covers_etymology": true, "notes": "OCR: Sogdian transliterations, entry numbers, English glosses and bibliographic refs (GMS, BSOAS, VJ ...) are readable; the Persian glosses are garbage (OCR'd as Latin). Full scan, 1995 edition = the one Nourai used.", "cites": "entry number / page in Gharib's Sogdian dictionary"}
---BQT off
vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').
grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)
---MON
None
Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks).
---AHD
1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page. Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves = original 1969 ed.).
---KLN
KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
---FVQ
printed page = leaf − 17 (0-based \f blocks in FVQ_pages.txt; 335 leaves) Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).
```


## [2026-09-14T01:22:49.673Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"lemma: r̥k̑\" POK_full.txt | head; grep -n \"Bär\" POK_full.txt | head -5\necho \"=== search POK_full for rk\"\ngrep -n -i \"r.k.tho-s\\|rk.tho\\|rk.to-s\" POK_full.txt | head -10",
 "description": "Grep POK_full for bear lemma"
}
```


### [2026-09-14T01:22:49.776Z] TOOL RESULT

```
=== search POK_full for rk
```


## [2026-09-14T01:22:51.893Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('POK_03.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\n# find leaf containing 'rkPo-s'\nfor i,p in enumerate(pages):\n    if 'rkPo-s' in p or 'Bär' in p and 'rksa' in p:\n        print('leaf',i)\n        print(p[:1500])\n        print('-----')\n        break\nEOF",
 "description": "Print Pokorny leaf with bear entry"
}
```


### [2026-09-14T01:22:53.238Z] TOOL RESULT

```
leaf 110
o-ko-)  ]  jav.  uru&wardj  -wan-  n.  {*rut-uar-   .-nn   \
, Eingeweide,  Bauch';  '
ags.  reada  jTiernaagen*,  engl,  read  , Labmagen*  {*routo-)^  andl.  rooA , Blättermagen*;  schwed.  dial.  rudda   f.  , Labmagen'  {^ruddön-),
Liden  KZ.  61,  14  f.
reuo-'.rü-  ,öffnen';  reues-  ,Raum,  weit*.
Av.  ravah-  n.  ,Raum,  Weite*,  ravas-carät-  ,was  sich  im  Freien  bewe
lat.  tniSy  rüris  ,Land  (im  Gegensatz  zu  Stadt),  Landgut*  (*reuos)'~^iJ roe,  röi  f.  , ebenes  Feld*  (wegen  des  Eigennamens  Cü  Röi^  welcher  älter Cü  Rani  lautet,  aus  *röuia)]
germ.  rü-ma-  in  got.  rüms  ,geräumig,  weit*,  rüm  n.  ,Raum*,  aisl.  rümr jgeräumig',  rüm  n.  ,Raum,  Ort,  Platz*,  as.  rüm  m.  ,Raum*,  afries.  a« rüm  , geräumig*,  m.  ,Raum,  Zeitraum,  Gelegenheit*,  ahd.  mhd.  rum  m ,Raum,  Öffnung,  freie  Räumlichkeit*,  mhd.  rüm  , geräumig*;  ahd.  rötni mhd.  rüme  ,geräumig,  weit,  fern*;  abgel.  Verbum  germ.  *rümian:  aisl. rgma  ,geräumig  machen*  usw.;
aksl.  ravbm  aus  *07'Vhm  ,eben*;  russ.  roves-nyk  , Altersgenosse*;  apr» arwis  ,wahr,  gewiß* ;  ^
toch.   AB  ru-  , öffnen*.
WP.  II  356  f.,  WH.  II  454,  Trautmann  14.
rezg-  ,flechten,  winden*.
Ai.  rdjju-  f.  ,Strick,  Seil*;  lat.  restis  ds.  (*rezgtis)  =  alit.  rekstis  ,Korb'; ags.  resc{e),  risc{e\  mnd.  rüch  ,Binse*;  norw.  rush  m.  ryslje  n.  , Schmiele*,
Beeinflussung  des  Präfixes  raz-i  russ.-ksl.  razga.  ^  '^
WP.  II  374,  WH.  II  43L  Trautmann  
-----
```


## [2026-09-14T01:22:57.524Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('POK_03.txt',encoding='utf-8',errors='replace').read()\ni=t.find('rkPo-s')\nleaf=t[:i].count('\\f')\nprint('leaf',leaf, 'est page', leaf+762, leaf+766)\npages=t.split('\\f')\nprint(pages[leaf][:2500])\nEOF",
 "description": "Locate Pokorny bear page leaf"
}
```


### [2026-09-14T01:22:59.021Z] TOOL RESULT

```
leaf 110 est page 872 876
o-ko-)  ]  jav.  uru&wardj  -wan-  n.  {*rut-uar-   .-nn   \
, Eingeweide,  Bauch';  '
ags.  reada  jTiernaagen*,  engl,  read  , Labmagen*  {*routo-)^  andl.  rooA , Blättermagen*;  schwed.  dial.  rudda   f.  , Labmagen'  {^ruddön-),
Liden  KZ.  61,  14  f.
reuo-'.rü-  ,öffnen';  reues-  ,Raum,  weit*.
Av.  ravah-  n.  ,Raum,  Weite*,  ravas-carät-  ,was  sich  im  Freien  bewe
lat.  tniSy  rüris  ,Land  (im  Gegensatz  zu  Stadt),  Landgut*  (*reuos)'~^iJ roe,  röi  f.  , ebenes  Feld*  (wegen  des  Eigennamens  Cü  Röi^  welcher  älter Cü  Rani  lautet,  aus  *röuia)]
germ.  rü-ma-  in  got.  rüms  ,geräumig,  weit*,  rüm  n.  ,Raum*,  aisl.  rümr jgeräumig',  rüm  n.  ,Raum,  Ort,  Platz*,  as.  rüm  m.  ,Raum*,  afries.  a« rüm  , geräumig*,  m.  ,Raum,  Zeitraum,  Gelegenheit*,  ahd.  mhd.  rum  m ,Raum,  Öffnung,  freie  Räumlichkeit*,  mhd.  rüm  , geräumig*;  ahd.  rötni mhd.  rüme  ,geräumig,  weit,  fern*;  abgel.  Verbum  germ.  *rümian:  aisl. rgma  ,geräumig  machen*  usw.;
aksl.  ravbm  aus  *07'Vhm  ,eben*;  russ.  roves-nyk  , Altersgenosse*;  apr» arwis  ,wahr,  gewiß* ;  ^
toch.   AB  ru-  , öffnen*.
WP.  II  356  f.,  WH.  II  454,  Trautmann  14.
rezg-  ,flechten,  winden*.
Ai.  rdjju-  f.  ,Strick,  Seil*;  lat.  restis  ds.  (*rezgtis)  =  alit.  rekstis  ,Korb'; ags.  resc{e),  risc{e\  mnd.  rüch  ,Binse*;  norw.  rush  m.  ryslje  n.  , Schmiele*,
Beeinflussung  des  Präfixes  raz-i  russ.-ksl.  razga.  ^  '^
WP.  II  374,  WH.  II  43L  Trautmann  245.  :
roi-no-  ,Weg,  Rain,  Hügel*,  s.  unter  rei-.
rughio-  ,Roggen*,  s.  unter  urughio-.
ruk{k)-,  rouk{k)-  ,Gespinst';  nur  kelt.  und  germ.
Air.  rucht  (*ruktu~)  ,tunica*;  mcymr.  rhuch{en)  ,Mantel'  {*roukkä)]  got. ''rukka  (ital.  roccd),  ahd.  rocko  ,Rocken*;  aisl.  rokkr  ,Rock*  stammt  aus ags.  as.  rocc  ,Rock*.
WP.  II  374,  Loth  RC.  42,  62  f.
JK
B
rksä  ,Köte,  Fessel  (bei  Huftieren)^? Ai.   Yksdlä,   rcchdrä.    f.   , Fessel'  vi(
lellelcht  zu   lit.  re§a  ,Köteng-elenk  des Pferdes^;  anders  über  ai.  fksdlä  oben  S.  673. WP.  II  322.
rkPo-s  ,Bär'  (oder  rk-s-o-s  neben  rk-to-s  ?).
Ai.  fksa-  ra.  ,Bär^  (dazu  ein  neues  fem.  rhsl  ,Bärin^)  =  jav.  arsa-, osset.  ars,  arm.  arj  (beeinflußt  von  arjn  ,dunkelbraun'),  alb.  ari,  gr. agy-rog,  jünger  ä'^xog,  dazu  (?)  der  VN  l^Qy.ccdsg,  mir.  art^  cymr.  arth ^Bär',  gall.  Deae  Artioni  ^Bärengöttin^^  lat.  ursus  ,Bär',  vielleicht  hitt. hartagga-  Name  eines  Ra
```


## [2026-09-14T01:23:07.727Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"bear'\\|'bear\\b\" SOD.txt | head -20\necho \"=== entry numbers near 70\"\ngrep -n \"^ *7[0-9] \\|^7[0-9] \" SOD_pages.txt | head -20",
 "description": "Grep Sogdian dict for bear"
}
```


### [2026-09-14T01:23:07.852Z] TOOL RESULT

```
=== entry numbers near 70
4023:                                                                   73 »Y»z     B -> »Y'z
4027:                                                                  74 "YlnS B .                                            J^K*.
4034:                                                                  76 nvV2     R
4040:                                                                  77 »Y>st- S =» »Yst-'
4047:79 »Y>y8- B                    b^jj^y-icr^y*-                aya5o ©<aTa6aku ?
16577:          71                                                 4514 ywz- B,S                                      ^^
```


## [2026-09-14T01:23:09.011Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"arsa-\\|arSa-\\|arša\" BRT.txt | head -30",
 "description": "Grep Bartholomae for arša"
}
```


### [2026-09-14T01:23:09.069Z] TOOL RESULT

```
5624:•  j.  arä  Adv..:  S.   unter  >ni.  Eig.  Bed.P    Ob  Ableit.  aus  arSa-l     Dann  ai. KompA.                                                                   '     r^!'»""ii-  m.  Name  von  Stadt  und  Gebirg.
5632:Gebirgs.  Komp.:  arsa-^ama-  'die  Kraft  eines  Bären')
6514:Pü.:  vai  raf,jnr..!iS;lum.  Sü.:  bakukUiaharsa-    (fjpm.)    Vt.  77    11 tamak.    —     ')    Mit   dem    Ideogramm    für    röe  '  /       J
9365:Zun  V.  ikars-.  —  zBed.  vgl.  'iarSa-  2  und larh;:  —  Pü.;  M.
12976:ASn.  aus  "darsa-  Adj.,  lum  V.  dar!-,  eig. 'dreist';  TgL  iBed.  ai.  i?*/-^«,  dfyfoiaAäv. — ai.  vgl.  dharfa-  m.
14515:•  j.,  p.  *rah-  V.  '(sich)  fürchten'.  Praes. 14  (inkoh.)  i>r?sa;  tarsa-,  30  (Kaus.) %ratfhaya:  —  PPfP.  iaräa'^>.
14585:VgL  unter  ^karSa-.
15128:Eig.  Bed.?  Anscheinend  Ableit  (mit  vani-)\ aus  *failyarSa-i  vgl.  at>tyaitl-1  \
15815:•  j.  *parsa-''  m.  'Getreideähre,  Ähre': mqnay^n  ahe  yaä^a  nä  sai?mca  hazar?r»mca ,  .  'l'anqm'^  *nijat3irt  hyat  ".  .  als  ob  ein Mann  auf  hundert  und  tausend  . .  Ähren einschlüge"  Yt. /j.  71''.
17870:•  j-.  gl  P-  fras-  V.  'fragen'.  Praes.  i p»r3S-'-i,  J3*ß^r7sa»ya-%  1 4 (Inkoh.)/»'«^-, farsa-,  J-Aor.  1  /ras-,  firal-.  —  PPfP. parita-^^;  PFP.  *'ß-asata-;  Inf.  ßars/il^, 'parliöi^^;  AbsoL  'par^m.
18282:*)  Der  von  Sonnenuntergang  bis  zum  Eintritt der  völligen  Dunkelheit  reicht  Weitres  zu iFKaaniarsa-.     Vgl.  auch  SüErl,,  unten  No.  3.
```


## [2026-09-14T01:23:13.032Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '5600,5660p' BRT.txt",
 "description": "Print Bartholomae context"
}
```


### [2026-09-14T01:23:13.093Z] TOOL RESULT

```
•  j.  aurva'sära-  m.  EN.  eines  von  Hao- 1  der  aus  der  Dualverbindung  anzahi  iavahi srar.ah  besiegten  Fürsten:  'r3 äaiMupaitis\  irerselbständigt  wurde3>.  —  Pü.;  transskr.  — a!i  spaainis  ranurä  .  .  Janat  um  iava  '>."''/■  'f.'-  T  '*/'"'  '"=''^ö)el«"lrie^  daher ,  -tr  r  J  ~  mitpluMlischenEndungen  verseheneZJi'anat'fl- kaoirma   Yt75.3lt                                                  Verbindung;   vgl.  ärma/o)-.  a.    —   j)   Gleich-
Eig.  Bed,?    Vgl.  JuSTi  Na  510.  artiges  scheint  ai.j-Ju'u.g-pi (OD.) neben riiü-njAfS
•  p.  "amvastam   D.7:  -?— .  votausiusetien.
.  ,  , ,  ,      •  j.  arazo.Samana-  m.  EN.  eines  Feinds
•  yy3<n'a',a  nStt  amyastt  (sd)  .  aoära  des^.^^jj^^^.-  k,r,s.lsps ..  yg  Janat 'n>m TJ  tarmä  J-J     aurvas.aDra  va  N.  15.        Yt/f)  42
P,.:  ..^™i  ^Uv   /i/«röJaJa>oaraDn«./.        ß^/'^de;  2.  Glieds?.). -■)  Geeenüber  JUST.
•  j.  aurvo.t«ma-  Adj.  'der  schnellste,!  KB.  z*  verweise  ich  auf  ^/.inmJHf.  Gam  un- tapfcrste',    von    Vayav:    vaim    aurvanam\     elaublich^Dsx.  2A.  a.  627.
■iPiMf  VL/5.57;  —  'VB  nama  ahmt  'mS:'  j-  arazo.suta-  Adj.  'der  zur  Schlacht iwoM  (7/tffi»  Yt  75.46,         *  I  ausgezogen    ist':    vispe    karana    rasmatiü
,  ^  . ,     .  ,        .,         l'/flÄ,;  Yt /0.36.
•  y  ar>za-  m.  'Kampf,  Schlacht':  miir^m]     Bfm^  if  jq  j^j
. . .,» -2»  /r^lam,,ili  yl  •»  p^iliMUcUi '  ,■  ^„  j.  f ;.K,„p,,  ScUachf;  i»rr»«/,« /.'  -K  fMiAiiümM /rä  nsMM  stanäa-  ^^        ,^  ,gSj  „  _  j,^^  ^^^^
,an  \l,o.s6;--  '"•"'""  ;.>«??/«?■;  jwinglichi  der  (sva.  in  der)  Schlacht- Yt.
h'J   Aa'a     'xaäoyS    vavanvil  patU.jasattt  °
".  .  der  aus    allen    Schlachten   siegreich!     vgi.  0™^..
"T^*^  yüA"'^*-;  -.1  R  ■  .  -■  J'  i-  arazüra-  m.  Name  eines  Daei'a"^; ki>mp.i.:  »Ableit. —  Zur  idg.  Baals 'nr^T. 'nch-       ■"    oc-         ■.     i  n/-      c        1
ten'-V  eic.   -Schi acht reihe'T  vgl.  rasn,an-  und    HUT    GS.    mit    kam»r»'.a'    n.    'Kopf    oder
H1M.PSL  66.  —  Vgl.  farizah;  arizyä-.  —  Yü..:  grivä-  f.  'Nacken'  als  Name  eines  Bergs**':
dby  Google
203  ^8  —  arsta-  204
'raAe  paiti  iamgnöfm'W.ig.^^i^y, —  'raAe\»].  'arSan- m.  EN.  eines  iranischen  Fürsten gtwaya  . .  yat  ahmya  äalva  kandvannti  ausder^ai'ix)'djTiastie,EnkelsdesÄijW(7/a'': "..wo  die  Ä  zusammenkommen"  V.J.  7.   -{■awa^»»    'srum  Yti^.71;  —  Aavöis  'Ins
*)   Den   getötet   lu   haben   Mx,  2/.  Hf.  aU   asaonß  Yt  19.  132. höchstes  Verdienst  («;/)  des  GiyruVa/ii/n»  gilt; .      Vgl.    'arsari-.     S.   auch    ariaia-   und   ariäjj- vgl.  WiNDlSCHUANK  ZSt.  5-  —  *•)  Der  nach  I'ü.  j      „([  fjo   —  »j  Bd    ii    i? und    Bd.  12.  8  /o  a-iw-  /  dBi-u"   'am   Tor   der  '  ■  J  ■     3-
Hölle'  liegt;  vgl.  noch  Dd.  33.  5.  ]  •  j.  ar§avant-  m.  EN.  eines  Gläubigem
Et.  undBed.?  Vgl.  iri^ura-.  —  mp. (¥ü.) anär \  •fats aiaonS  ..vyarlavalö ..patlyarsavatd  ..
tamäl,  artür  srhiai.  1  Yt_  jy.  loq.
•  j.  arä  Adv..:  S.   unter  >ni.  Eig.  Bed.P    Ob  Ableit.  aus  arSa-l     Dann  ai. KompA.                                                                   '     r^!'»""ii-  m.  Name  von  Stadt  und  Gebirg.
•  j.  (,p.)*aräa-"  m.'Bär':  °Jii'>..  flAÄr«5:*  j-  aröadä-  f  Name  einer  Festung  in Aog.  7p.  I  Arachosien:  'da  näma"  didä  hara'uvaSiya
KompE.;  Ableit.(?).  —  Aus  ar.  ♦/■"■>.  IF-  ?-    Bh.J.  II.
261.  —  ai.  /*fa.  m.;  KDm.  ai;  vgl.  np.  xirs       Et.?')  —  ■)  VgU  lusTl  GIrPh.  2.  430  Ko.
araia.        •'  '  •  j,  arsama-  m,  EN.   eines  Persers,  Ar-
.  p.  aräa'ka-  m.  EN.  eines  Persers,  Arsac^:  """'f-  ^^raya''vJ'uS . .  vutäspakyä  pui  y" 'Aa*  näma'  *a^iyiliausnaÄya  fu^'af  S.  7.    ''""^^  ""^'^  ^\  ''^'^  vtmspahyl  pns
AbleitCmitKosesuffix)Bus*ar/«.Moder.<,»a-:..i°'w<i^    "makyä  pttä    anySramnd'  Bh./.z;
—  Vgl.   'arSan-.   —   ai.  fifoia-   Name   eines  \  —  'mar  Ao.  J.  2.
Gebirgs.  Komp.:  arsa-^ama-  'die  Kraft  eines  Bären')
,     ,  \   ,      X  \  m  »...  besiliend'.  —    »)  Oder  auch  'eines  'Henesls,
•  J.   (g-.  P)   'arSan-  m.   l)  'Mann,  Mann-        Helden';  ».  '<^io«-  und  Bgu.  Grdr.  2.  A eben'  (geschlechtlich)'»:  a)  von  Menschen:      .      ,_ .  .,.,,,
'^am  xfudrä  Y.  65.  2,  5;  -  pu^r^m  .  .  '}■  ai&o.kais.- Ad}. -7-'^ :v^r^>ray„;,m . . anyahmäi  'lanai»  varihm  YtJ7.58;  -  'to/.  m<T«J.*«w/</mj^.i«rPff,  \t/4.28. ,  -^  ..  V-.     V  ^  V  i.,T.  \        ^p^.:  ittvan  u  iahib.  —  ')  lirklaruncsv ersuch
loMi  . .  mnayml  iiimsni  •latra  (NP.)      ^,1  ^^^  3  y,  j^  (.umpflu.iiE'),  Dit.  ZA.  ,. V. /Ä  31;   — ^d^a   anyasSt   'iuris  aii      56S  {'qui  rend  viril'). xSudri  aa^riha  trm_mr,navainti  y-lS._,  .    ,      ,   „5.^8,     «raz-uxSa- ■>  Adi. K'  ^?^=^fV~  *-■*--'  """f";'  'richtig,  recht,  wahr  gesprochen';  a)  von
ntergen)  Tieren  (m  Gegens.jn  ,/<.™..»-):  ),i^„,„„  ;,,,■/„  Y.&.  5;  Yt/j.3,  75.96 -'  j,     ,  •    ,  .,.        (wo  °z°y,  —  'suxüjm  Täcim  Y,7.  26,Ij,ü.  6:
5.120;  —  ustrane ..  yö -snam  ..  mattstem  i_  «,•„_;,_   ,,7,7-,   S  "  18    Vo  z";-    ■
a,jl  sl^rMi  yyi.^'-     ■    a)  sonst  in    .,,  „^  ,,^^^  .{^  Y.5.  ."sPUZ;  -  M.^i-Ä.
Verbindung  mit  dem  Tiernamen  3>: .
cca  Y.  -f,  10;  10.  t8,  Vr.  7. 1, 20.  i,
Yt.«.3t,  39,   /«.lo:—  uHtahi-MI..  G.  2. 6,  Yt.  i<!.  8';   &j:äa*  t',7*/ Y. «  . ,
»./.»fcwV.M.,,;,,  3;j-i-a,  •Ät,l_   ^;,.„,^;„  .^,„„   ,,„^,„    .j„w,„„
vt.  17. 5s;  -  .r.""  -'«»fc«  Yt.M.  7i  -  Y.  „.  25;  27.  r,  -  -»«.«.W.i  «-/=%'
^,pmqM_-!nam  .  .  u.Inmm  •!nqm  .  •,  v,:«. ,,  Y.lS.  .,  Ny.I.  .6;  -  •.'»..«(/»&' l,r„qm  -na,  ..  anum„yamm  •*?««  V.  22. ,  ,,^^^^^_,  Yt.5.76;  -  -mmm  vui«/,„m .o;1ft.S.,.;-il.M,7.«™r««J.     .,,„„^„^;„,;i^y,    „  '_     .,„.,;^^
■/«i>  -Sl./*  IS.  s)  »va.  'Mann,  ^cW-  „,-„m'S.:.  18.  •Vt.;2.38.  b)  sonst: •ro  «r,«,;«».  rf»*.»«»...  Iimsrav^  Yt.j^^^  .,j,j.-,,„  Vr.rj.i;  -  U  bä  aia  u S.ir.-'tl^-'tfl'm        ;i,n^Yx.i<).   .^^,;„  y^  •J.^ä.Ir-.lsInCs,  ■
—   iaofT  «ii  (näml.  gavatii)   '
-  I)  Die  Foi
apayät .  .  tniirö  YL/o,86.  |     des  Od.,  vgl.  Y.  sr.  19,  44.  i..
KompA.,  E.;  Abicit.   —  Vgl.  'arha-  EN.  — 1      in    den    Jüngern   Dialekt    herübe r^enommen gr.  Bp3T,v;   ai.  vgl.  fsahhä-  m,    —    Pu.:   vusn,  \      wurde,  BtiU..  IF.  p.  264.  —  ')  växi  usw.  wird Npü.:   JHvS».    —    ■)  Im  Gegens.  lu   häitisi-,\      nicht  besonders  übersetzt. B.  Y.  5j.  S.  —  >>  Them,  —  J)  VgL  lU  uxiaii-,  I      .  .,        .  .-    ,r  ,-  1      \   .     r      ■   l
-..«r«4 '"«""".V-.  rffl.v/-Ti- und  den  Gebrauch    •  ]■  <"-^"'-  Adj.   (fem.  '!.,■)_  l)  'aufgencb- :t'.  2)  'gerade,  aufrichtig'.
Kom[.E.;  Ableit.  (s.  arl/j/-)').  —  Aus  ir.  '/■J''''-
dby  Google
■arätay-
•  i-,  p,   'arätay-  f;  m."  'Speer,  Lanze': yaäam  zayanqm   raitöiiti  paoiryS  °iis  V. 14.^;    —    'tayasiä    karitayasca    '^.fj —  •//'/  ki-aiwyästa  Yt  13.  7 ; •tSis  huxsnutaya  Yt  10.  24;  —  'tayasat
Anx/mi/a  YtiO.  39;  —  'lintrm  brSi'irS.- ta^nam  YtJO.  39;  —  väfff  laut  'Um AaraUi  jram..\'t.lo.2i;'P.2r,  —  WfiärsaAyä ..^düraiy  't'ts  parügmati  D.O.  4.
KoiDp.\.,  E.;  Ableit.  (ärltya-,  'Srstaya-).  —  ü. Tfläy-  f.,  np.  xiil;  arm.  LW.  aiteay.  Vgl.  dam Hbx.  KZ. 36. 166  und  No. a.  —  lü.  fiu  V.  14): aril';    erl.;  tiäai,  (lu  V,  //  und  V.):    alin'i.
—  ■)  Sicher  nur  Yl  10.  39.  —  J)  Wohl  aus a}t  veiderbi,  s.  aim.  LW.  Anders  GlcFb. y  b.  67.
•  j.  *arStay-  f.,  anderer  Name  für  arftat- (sd.);  ufaratilUm  .  .  yqmca  sraosahe  ,  , yqmca  'tdif  yazata^e  y.^y.^^.
Eig.  'Sichautrichten,  Geradesein' ;  lEt.  s.  arsla-.
```


## [2026-09-14T01:23:33.940Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"--- SOD.txt grep bear\"\ngrep -n \"bear\" SOD.txt | head -20\necho \"--- SOD_pages grep bear\"\ngrep -n \"bear\" SOD_pages.txt | head -20",
 "description": "Grep Sogdian dictionary for 'bear'"
}
```


### [2026-09-14T01:23:34.024Z] TOOL RESULT

```
--- SOD.txt grep bear
5671:result,  the  vocalism  of  many  Sogdian  words  bears 
10922:0o)bear,  GcOsuffer 
19277:bear 
25284:0o)bear,  OcObring,  OcOcndurc 
25413:bearing,  porter 
25945:(/6>)bring,  0o)carry,  0o)bear 
25964:suffering,  pain-bearing 
26131:fruit-bearing 
26145:carrying,  bearing 
26151:bearing 
26396:bearing,  subjection 
26887:0<?)bring,  OcObear,  (ro)endure 
26905:bearing 
44973:gospel  bearer 
46108:Sogdica.  7.16n  p8, "  sans-souci ",  not  bearing 
52235:(/cObear,  (rcOcarry 
53522:bearer,  porter 
66245:beard 
86206:cup-bearer 
87525:bear     1770 
--- SOD_pages grep bear
3050:result, the vocalism of many Sogdian words bears                III) lul High, back, rounded short vowel. The
5273:                                                                                     0o)bear, GcOsuffer
8894:     bear
11403:         Frag. Len. 31.2, fintkw                                       0o)bear, OcObring, OcOcndurc
11441:                                                                         bearing, porter
11684:                                                                       (/6>)bring, 0o)carry, 0o)bear
11700:                                                                      suffering, pain-bearing
11782:      fruit-bearing
11792:     carrying, bearing
11797:     bearing                                                       BSTBL, Dhy. 92, 96; GMS 998, 999, 976 n 1; TSP
11863:                                                                   bearing,   ^'ps'y-
12071:     pum ©<OP. Jw/wf ©ob. -y(h)                                          0<?)bring, OcObear, (ro)endure
12087:2913 pwn'kh B, M                                                        bearing
19651:                                                                            bearer
20104:                                                                        Sogdica. 7.16n p8, " sans-souci ", not bearing
22681:      GMS 738, 748; Bailey. Prolexis. 151; VJ 851, 958;            (/cObear, (rcOcarry
23281:      bearer, porter
28652:                                                                     beard
37220:      cup-bearer                                                           zay (zy) =»z>y, z>yh
37699:bear    1770                           (^become still 1938, 1939, 5337         (to)bc heared    7700, 7706
```


## [2026-09-14T01:23:35.836Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN xirs\"\ngrep -n -i \"xirs\\|hirs\\|Bär\" HRN.txt | head -20\necho \"=== HUB\"\ngrep -n -i \"xirs\\|Bär\" HUB.txt | head -20\necho \"=== PHD\"\ngrep -n -i \"xirs\\|bear'\" PHD.txt | head -20",
 "description": "Grep Horn, Hübschmann, MacKenzie for bear"
}
```


### [2026-09-14T01:23:35.941Z] TOOL RESULT

```
=== HRN xirs
1080:bei. hirs (156) ist nach Dames und Hübschmann
1254:cHn sepled ez m^y-l mü*ambär-t ^öse
1329:sed bär^ tnerä zi tu resed äk
1384:111. enhästen^) 'anfüllen, anhäufen', Praes. enbär-em,
1385:enhärden, enbär^).
1570:Praes. obarem , öbärlden ; öbäs 'Gesindel*, "»JITll^NilN
1758:kurd. af;^. bei. (33) bär.
1761:157. {2)bär 'Mal'.
1762:skr. vära- 'Mal'; phlv. bär.
1763:158. {s)bär in Comp. Jöi[bäry derya\bär, röd[bar, Zeng[bar,
1764:Hindü[bär,
1765:o. t aw. para- 'Ufer, Rand'; phlv. -bär, z. B. röt[bar
1767:159. bärän *Regen', bartden regnen', baris, bärgln,
1776:160. l\)bäre 'Pferd', baregl (Sahn. I, 21 Vers 27).
1921:Die sprichwörtliche Redensart gurg-l bärändide *ein *Wolf, der nass
2139:kurd. berz] oss. d. barzond, bärzönd (56); bei. LW.
2300:aw. 6ama- 'Rücken des Pferdes ; oss. d. barze, t. bärz
2957:folgenden Formen an : pervär^ perräre, perbär, perbärff perbäl, perbcUe^
3979:knrd, je, jau, yö (H.-Sch.); oss. yau, yäu, yeu *Hirse'
4325:\ yiirs 'Bär.
=== HUB
5083:'Laib Brot'; xirs 'Bar = zd. aresa-, skr. rkSa-; gdgird
8428:und xirs 'Bar = skr. rksa-^ zd. aresa-, gr. «(?xro^, lat. wrsw5.
8430:so sollte man im Np. *xis erwarten, wie umgekehrt np. xirs
9511:arm. hum; xirs 'Bar, phi. x(i)rs Bdh. 56, 14 und 17, zd.
=== PHD
661:2xān [/?п! | P л?п] spring, source. хапар [BYTA < A рур; h'nR! | N хапа] = іхап. xandidan, xand- (*GHBHWN-yitn' < A V ghk, or У *ghqh; hnd-ytn' | (M xnyst), N —] laugh. xānīg [/?nyk! | M x?nyg, N xàni] = *xān. xar (HMRA < А hmr’; hl | N ~] donkey, ass. хаг [P1 | M ær, N ~] thorn. xar-buz [hibwe | M xrbwz] oryx. xar-g68 [higws | N ~] rabbit, hare. хаготапа [/PPwmnd] thorny. xār-pušt [/?Ipwst! | N ~] porcupine, hedgehog. xastan [hstn' | M xst, N ~] wound, injure. xašën [hsyn! | N хайл] (dark) blue. хауар [Pd(y)k! | N xdya] egg. ~-dés [-dys] oval, egg-shaped. xayüg [Ah )dwk! | N xayū] saliva, spittle. xaz [hz | N —] marten. xém [лут] nature, character. xëšm [?yfm, hfm | M xysm, N xifm] anger; the demon Wrath. --én [-ya! | M -yn) angry. xindag [hyndk' | M xyndg] ill, sick. ~th: illness, sickness. xir [C BW! < А sbw; hyl | M хут] thing, matter. xirs [hls | N ~] bear. xišt [Ast! | (P hystyg), N ~] brick. хбё [hwk' | N xwk, xóy] nature, character, disposition. x6n [DM YA < А dm’; һит! | M хоп, N хип] blood. xormā [TE A tmryn; hwlm’k' | N ~] date. xrad [hit! | M xrd, N xirad] wisdom, reason. ~ig, ~Omand [-yā!, тиа | N -mand] wise. xrafstar [hlpst] = Av. xrafstra-] reptile, noxious creature. xridan, xrin- [ZBNN-tn! < A V zbn| M xryd, xryn-, N xaridan, (xar-)] buy. xróhak [hlwhk' | N ~] coral. xrēs [DYLK A < A dkr’; hlws | P xrws, N xurós] cock. xróstan [Alwstn! | M xrwst] call, cry. xüb [hwp | M xwb, N ~] good. ~th: goodness. xuftan, xufs- [HLMWN-tn! < А У Ыт; hwptn', hwps- | М xwpt, N xuftan, xusp-] sleep. xūg [HZWL УА < А hzyr; hwk' | N ~] pig. xükar(ag) [hwkl(k') | N xūkara] hedgehog. xumb [kwmb! | M xwmb, N ~] jug, pitcher. xunak [hwnk' | M xwnk, N xunuk] happy; cool. xurdruš [kwldlwš, -dlpš = Av. xrwidruf] ‘with a bloody club’ (epithet of Xēšm, later misinterpreted as *ul-draff ‘*with raised banner’).
946:bear (anim.) xirs.
```


## [2026-09-14T01:23:43.880Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('HRN.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\ni=4324\nprint('\\n'.join(lines[i-8:i+8]))\n# leaf\noff=sum(len(l)+1 for l in lines[:i])\nprint('LEAF',t[:off].count('\\f'), 'page approx', t[:off].count('\\f')-21)\nEOF",
 "description": "Horn xirs context"
}
```


### [2026-09-14T01:23:45.005Z] TOOL RESULT

```
(karkä- etc. sind bedenklich) ; phlv. karcany 'Krebs im
Tierkreise (Bund.); gr. -^nQy.lvo^ 'Krebs', vergl. md^j/ar
yjumi'oi 2itY.t\oi , Hesych.; lat. Cancer wird ebenfalls
dazu gehören (vergl. Brugmann, Grundriss, I, § 282
Ende). / ist erst neupersisch.
>. -/ired 'Verstand*.
aw. /ratu- 'Verstand'; phlv. xrat, /j'attk[tum (vd.
19 (47), arm. LW. /art)\ ai. krdtU",
\ yiirs 'Bär.
aw. aresa- *Bär (Aog.) ; phlv. xO)^^ (Bund.) ; ai. /ksa- ;
arm. arj (H. No. 46).
oss. d. t. a7's (85); siyn. ytir}, sar. yürx,
Aw. Ere/sa-, vergl. ai. Ärksa- (Goldschmidt bei
Nöldeke, ZDMG. 86, 447) sind hiervon zu trennen,
vergl. Hübsch mann, ZDMG. 38, 429; anders Bar-
tholomae, Studien II, 21.
LEAF 126 page approx 105
```


## [2026-09-14T01:23:45.827Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('HUB.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nfor i in (5082,8427,9510):\n    print('=== line',i+1)\n    print('\\n'.join(lines[i-6:i+8]))\n    off=sum(len(l)+1 for l in lines[:i])\n    print('LEAF',t[:off].count('\\f'),'page',t[:off].count('\\f')-10)\nEOF",
 "description": "Hübschmann xirs contexts"
}
```


### [2026-09-14T01:23:46.737Z] TOOL RESULT

```
=== line 5083
== zd. zeredr-f skr. Ar d-, hrdaya- ; histan *lassen' (aus *hirstan
--- ^hrstan), 3. pr. hUad (aus ap. *hrdatiy) = skr. srjdii, zd.
herezaiti; gila 'Klage' = zd. gerezd-; kistan saen', skr.
krsdti; kirm 'Wurm', phi. k(i)rm oder k{a)rm GI. and Ind.
198, skr. krmi~; -gird in Namen =^ arm. -kert, zd. kereta-,
skr. krta-, vgl. § 7; girda 'rundes Brot' = arm. grtak
'Laib Brot'; xirs 'Bar = zd. aresa-, skr. rkSa-; gdgird
'Schwefel', bal. gokurd, afgh. gOgar, gogil; giriftan'^) er-
greifen , paz. griftan Shk. 246, zd. gerepta- (vgl. bal. giray,
ptc. gipfa). Ueber den Reim girift : biraft bei Firdusi
s. Horn, Grundriss, p. XIV der Einleitung.
Fiir i ist a eingetreten in kard 'machte' = zd. kereta-
nach kardan (inf.) und karddr, KZ. 27, 111, vgl. -gird in
Namen ; tarsfdan sich fiirchten', 3. pr. tarsad = ap. trsatiy,
LEAF 155 page 145
=== line 8428
casm 'Auge* = zd. dasman-, skr. caksus ; arm. LW. sahapet
'Schutzgeist* (5. Jhd.) = zd. soid-rapaiti- ; sen *Dorf * =
zd. -say ana, Wrzl. k^si wohnen'.
Dazu auch as 'Bruhe' H. 29, Osam *Trank' H. 30,
sCLgird 'Schiller = arm. asakert aus ^asakrta- und andere
s nach ^ ? — Fiir s erscheint s in kus H. 852, s. oben p. 87
und xirs 'Bar = skr. rksa-^ zd. aresa-, gr. «(?xro^, lat. wrsw5.
War die iran. Grundform des;»letzteren *fsa- = zd. aresa-^
so sollte man im Np. *xis erwarten, wie umgekehrt np. xirs
eher auf iran. *fsa- (als fsa-) weist.
§ 130. Idg. st (nach i, u etc.) und kH = iran. ap. st
= np. st und s^:'
a) = s^ : mw6^^ Taust' = zd. rmdU-, arm. msrtfc 'Bundel*
= phi. "^mustik; angust 'Finger, Zehe' = zd. angusta";
LEAF 246 page 236
=== line 9511
(aber nicht vor e aus ary- und aus ava-) vorgeschlagen.
§ 162. Vorschlag von x hat stattgefunden bei:
xastu *Kern* = xasta JRAS. 1894, p. 458 = asta, zd. ast-
*Knochen'; xaya *Ei* (mit h im Kurd., Afgh. und Bal.) =
paz. xdyay phi. xayak Shk. 254, Min. Gl. 125, gr. aJoV, lat.
Ovum\ xdm roh' (kurd. mit x, bal. mit h) = skr. ama-,
arm. hum; xirs 'Bar, phi. x(i)rs Bdh. 56, 14 und 17, zd.
aresa-, skr. rksa-; xist 'Ziegel', phi. oHst = zd.istya-; xism,
xasm 'Zorn , paz. xasm {xism) Min. Gl. 124, Shk. 254, phi.
xism Gl. and Ind. 68 = zd. aesma-; xEs, ka§. is, xis *Pflug*
= zd. aesa-; xurma 'Battel', paz. xurma Min. Gl. 128,
arm. armav (5. Jhd.).
Hier ist x schon im Phi. vorgeschlagen worden, aber
die Kegel, nach welcher dieser Vorschlag erfolgte, ist
LEAF 275 page 265
```


## [2026-09-14T01:24:00.867Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"^1770 \\|1770 \" SOD_pages.txt | head -10\necho \"=== find leaf with entry 1770\"\npython3 - <<'EOF'\nimport re\nt=open('SOD_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if re.search(r'\\b1770\\b',p) and ('B' in p):\n        # print only if looks like entry area\n        if re.search(r'\\b176[5-9]\\b',p) or re.search(r'\\b177[1-5]\\b',p):\n            print('leaf',i,'printed page ~',i-66)\n            print(p[:3000])\n            break\nEOF",
 "description": "Find Sogdian entry 1770"
}
```


### [2026-09-14T01:24:02.014Z] TOOL RESULT

```
8890:1770 >ssh B                                                cr>         eighth 1096, 1331; TSP 2.331; VJ 885; BSTBL,
37699:bear    1770                           (^become still 1938, 1939, 5337         (to)bc heared    7700, 7706
=== find leaf with entry 1770
leaf 135 printed page ~ 69
                                                                                                                              70

 'snVxCw)


       GcOthink, (to)count
       Anc. Lett. 3.33
                                                                          mst'y-
                                                                        (ro)show
                                                                        GMS 657; STii 1.87; BSTi 253; C2 gloss.; Sund.
 1764 'sm'xfw)     M                                        U^
                                                                          AoF 1981 p2l3
       asmax(u) ©<*smdxam          ^sm'yw, sm'x
                                                                  1777 >5t»y,mnty C                                ^liWjb,
       GMS   157, 1380; KG 332                                          astayamande   Osty'mnty)
                                                                        indication
       you
1765 'sn'ky'ntyc S           (/^Li/^j^JU^                    „U         STi 32.17; GMS 1100; BSTii 904.30 : C2, 57R30
     ssnaxandic- ^sn'xntyc
     fifth month of the year                                      1778 'st'yk S
     MDii Nov. 1R                                                      ostik =*Jstyk, >cstyk
                                                                       third
1766 'sn'ych ? =* yyn'ynch ?
                                                                        ~>v, Hen. Magi. 138.29; KG 339, 617; W-Lii 569;
1767 'sp^y S                        ? o> «j£ ,? *y>. <c^-J
     (o)spa5e ? ©Pers. as ?                                                -ft, MSP bl4

       part, portion ?, bowl ?                                    1779 »st»yny C                           (tjujtjjUj)^^
      Frag. Len. 60, 8, 69, 28-33; S W, BAI 1990, 286                   astayne ©pres. part.; ob. pi. -/y ^st'y-
1768 >sp>yr B                                                >         guide, indicator
                                                                       Sund. AoFviii 1981, 174.2
      osper ? ©*y/7arya        ©ob. -y
      cave, grotto                                                1780 >st5s B                                           >js**
      BSTBL, Dhy. 362; Benv. Notesii 237                               ast-5as ~>sts

1769 >spn- C                          ^jji t jju.j7                    eighteen
     aspan, arhspan ©Khwar. hsf-\ MP hasp-                             BSTBL, Dhy. 312-3
         ©impf. mspn ^'sp'nch, }nspn-
      (/<?)rest                                                   1782
                                                                  1781 >stmy  ** >st())
                                                                       »sth S B                                          ^
      BSTii 878.7; STSC 12; C2, 87R7, 60R15                            astami

1770 >ssh B                                                cr>         eighth 1096,
```


## [2026-09-14T01:24:07.647Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '8880,8905p' SOD_pages.txt\necho \"=== SOD.txt around 'bear' line 19277\"\nsed -n '19265,19290p' SOD.txt",
 "description": "Print Sogdian entry 1770 detail"
}
```


### [2026-09-14T01:24:07.730Z] TOOL RESULT

```
      BSTBL, Dhy. 362; Benv. Notesii 237                               ast-5as ~>sts

1769 >spn- C                          ^jji t jju.j7                    eighteen
     aspan, arhspan ©Khwar. hsf-\ MP hasp-                             BSTBL, Dhy. 312-3
         ©impf. mspn ^'sp'nch, }nspn-
      (/<?)rest                                                   1782
                                                                  1781 >stmy  ** >st())
                                                                       »sth S B                                          ^
      BSTii 878.7; STSC 12; C2, 87R7, 60R15                            astami

1770 >ssh B                                                cr>         eighth 1096, 1331; TSP 2.331; VJ 885; BSTBL,
                                                                       GMS
     o(s)sa ? ®*rsa; <IE       *r£-j<?; Khwar. /irs; Av.
       arsa                                                              Dhu. 231, 254, 264
     bear
                                                                       astamik ^stmyq
      SCE 359; GMS      155                                       1783 >stmykC)) S

1771 >stc» SfB                       (u^>i->»)^u                       eighth
     ast(a) ('st, }sth) ®<*asta =*sV                                   TSP 3.99, 14.17, 9.18; Frag. Len. 69.27; -w, MSP
     eight                                                               b33, 108

      GMS 87, 1316.8; Frag. Len.; >Stht MDii                      1784 >stn B                              J*^jL^-I
1772 WdV-        C *± >st>y-                                           ostan ®<*hista- =^skwn                                *j>r
                                                                       durative particle
1773 >st't S                                               &±*
=== SOD.txt around 'bear' line 19277

1769  >spn-   C  ^jji  t jju.j7 
aspan,  arhspan   ©Khwar.  hsf-\  MP  hasp- 

©impf.  mspn   ^'sp'nch,  }nspn- 
(/<?)rest 
BSTii  878.7;  STSC  12;  C2,  87R7,  60R15 

1770  >ssh   B  cr> 
o(s)sa  ?   ®*rsa;  <IE   *r£-j<?;  Khwar.  /irs;  Av. 

arsa 
bear 
SCE  359;  GMS  155 

1771  >stc»   SfB  (u^>i->»)^u 
ast(a)  ('st,  }sth)   ®<*asta  =*sV 

eight 

GMS  87,  1316.8;  Frag.  Len.;  >Stht  MDii 

1772  WdV-    C  *±  >st>y- 

1773  >st't   S  &±* 
astat  ©<*aJr5n"  =»st>t
```


## [2026-09-14T01:24:21.567Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== ARSHAM in BQT v1\"\npython3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 'آرشام' in p or 'ارشام' in p:\n        print('leaf',i,'approx page',i-210)\nEOF\necho \"=== KHERS in BQT v2\"\npython3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nimport re\nfor i,p in enumerate(pages):\n    if re.search(r'خرس',p):\n        print('leaf',i,'approx page',i+543, p.count('خرس'))\nEOF",
 "description": "Search Borhan for Arsham and khers"
}
```


### [2026-09-14T01:24:23.160Z] TOOL RESULT

```
=== ARSHAM in BQT v1
leaf 10 approx page -200
=== KHERS in BQT v2
leaf 68 approx page 611 1
leaf 84 approx page 627 1
leaf 88 approx page 631 1
leaf 130 approx page 673 1
leaf 179 approx page 722 1
leaf 183 approx page 726 1
leaf 191 approx page 734 6
leaf 214 approx page 757 1
leaf 283 approx page 826 2
leaf 299 approx page 842 2
leaf 359 approx page 902 1
leaf 476 approx page 1019 1
leaf 483 approx page 1026 1
leaf 545 approx page 1088 1
leaf 642 approx page 1185 1
leaf 655 approx page 1198 1
```


## [2026-09-14T01:24:28.672Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\np=pages[191]\nprint(p[:4000])\nEOF",
 "description": "Print Borhan khers page"
}
```


### [2026-09-14T01:24:29.812Z] TOOL RESULT

```
                                                                                               ‫‪— ۳۳‬‬

‫افشاند بکهدرام که پای او بخورد او را بدرون‬                ‫اسبهارا‬   ‫دراز که درطو لپا نصب کنندوزمنهاوبراق‬


‫خط بجای خود آورد واین بازیرا عربان حجوره‬                  ‫بر بالای آن نهند ‪ -‬وسه بایه را قیز گفته‌اند‬
                                       ‫گوند(‪. ۴ )۲‬‬        ‫که زین اسب رایربالای ان گذارند ونکیه گاهی‬

‫خر سگیاهم بعنی گیاه خری و بیخ‬                              ‫را نکیوزبند که بکروشهای صفهاسازند و‪-‬نوعی‬
                                                                                            ‫ازیالان هم هت‬
                                  ‫گن‬
              ‫یاء شقاقل است و خرس ن‬
 ‫آرا بسیار دوست‬                     ‫آ‬                                                 ‫‪۷.‬‬

                                           ‫داردو برغت‬
‫(‪)۳‬؛وبعضی گوبند زردك‬           ‫تمام خورد‬                   ‫حرست د بفتح اول ونانی وسکون‌سن‬
‫گوزر بری است و بعضی دیگر کونند کرفی‬                        ‫نبةیعله وفوقانی» بم‌منی‌سیاه هست‌است که بعربی‬
                                           ‫صحرای ات‬                                        ‫طافح گویند ‪. ۱‬‬
                      ‫‪2‬‬            ‫‪۶‬‬           ‫ی‬
          ‫‪۳‬‬
‫بقح ثالث ولام بالف کشیده‬        ‫خر سالاك =‬
                                                           ‫سرته = بکراول وانی‌وسکون ثالث‬
                                                                                       ‫خ‬
        ‫باشد » و أ‬
    ‫شنخصی‬                          ‫» بم‬
                                ‫نعنی‬
                               ‫ده‬     ‫ن‬ ‫رده‬  ‫بکا‬
                                          ‫خف ز‬
                                                            ‫وفتح فوقانی » بمعنی زلو باشد ‏ و آکنرمی‬
                  ‫ت که خرالاغ بکرابه میدهد‬
‫خرسطه = بروزن مرحله ‪ .‬نام داروبی‬                                    ‫بجبانند (‪ )۱‬خون ازآن عضو بمکد ‪.‬‬

                                                           ‫خرسك = بکراول وفتح‌ثالث » تصفیر‬
‫خسرنك ‪ = ۴‬بنم اول بروزن گل قند»‬                             ‫خرس است؛ آون‌جانوری‌باشد معروفسوفرشی‌است‬

                                                           ‫توص ویو ای راو‬
 ‫بمعنی شادمان وهمیشه خوش وخوشنود باشد ‪-‬‬                   ‫وآتجنان باشد که‬     ‫یشم‌دار‪ -‬ونوعی‌آز بازی‌هم هت‬

 ‫هضاقضاداده باشد وهرچه‬
                     ‫و کسیرالیز گوبندک ر‬
              ‫کر وراش بو ‪:‬‬             ‫ادا یش آنا‬          ‫آبند واورا زنند و او بای خود را بجانب اشان‬

‫‪.‬‬    ‫‪ :‬ورد‬    ‫‪٠‬‏ چش‬       ‫چك‬   ‫‪۳‬‬            ‫(‪)۲‬چك‪.‬چش‪ :‬خوانند‪.‬‬             ‫(‪.)۱‬چك ‪ :‬بجپانشد ‪.‬‬

         ‫بیم ندارم ابزلا تنللا تلا تلا‪.‬‬                  ‫‪ - ۱‬مت‌خرست میروم‌ازمیعشق بوالعلا‬
     ‫مولوی بلخی‌رومی‪.‬‬
              ‫خرسك باکزولددکان در بازار‪.‬‬
      ‫«گلتان ‪.۹۹۱‬‬
     ‫( کود)‬    ‫‪7‬‬
               ‫‪0‬ع‬‫‪1‬تی‬
                   ‫‪dnas‬‏ ‪ rûx +‬در ارم‬               ‫‪ - ۴‬پپلوی ‪( 0085۲0‬قالم‪ ,‬راضی)؛ ‪۲۵6‬‬
     ‫بمعنی کودی و ورطه‪ . # ۲۵ ۰ 2۳2۷2# ,‬از اوستا ‪( ۵۲۵3۷4‬بپاین) « بارتولمه‪2702 ۹۷۱۰‬‬
     ‫( بسوی باین)«بارتولمه ‪ » ۳4۹‬سالسکریت ‪ ( 2123۷2 -‬پاین « (‪ıı‬‏ ؛ ‪adnaS‬‏ ‪ .#‬از ‪dnas‬‏‬
                ‫(سندیده بافتن) « بارتولمه ‪ 4۵۵۱‬رلك ‪ :‬نىمرك ‪ ۳-1‬و اسشق وهوشمان ‪. ۸۷1‬‬
     ‫‪ #‬خر س۔ بکسراول‪ .‬پهلوی ‪ « 572[ 5۳11‬بونکر ‪ ۰۲۱>]۰‬اوستا ‪« 3159۲4‬اسفا ‪۱:۷‬‬
     ‫ص‪ ۷۱۰‬بارسی باستان‪( 20158‬در ‪ ) 2۳12015۳23‬اآ‪:‬رشام ]‪ ,‬اشکاشمی ‪ 5۳106‬دشغنی ‪۵5۲1۷۷۰‬‬
     ‫‪.‬یلکی ‪ ( 5721‬در ‪ ۱ .۵‬ص‬      ‫‪ : 5‬لك ‪ .‬ات ‪ ۷۰۱۲‬گ‬                   ‫یودغا ‪« 158‬کربرسن ‪ .»۵۸‬استی‬
                                               ‫‪ )KS‬فریزندی ‪ » 5۲685‬برنی ونطنزی ‪« 5۲66۱‬ك ‪.‬‬            ‫‪۷‬‏‬
                                           ‫و‬       ‫و ‪9‬‬    ‫و سرخهی‬         ‫‪ ۰‬ق‬     ‫سمنالی ‪5131‬‬    ‫ص ‪»* ۷۸۲‬‬

                                            ‫شهمیرزادی ‪ ۲ .#« 5۲6‬ص ‪ 4۸۱‬سفدی ‪۸5۸S‬‏ « بنولیست‬
```


## [2026-09-14T01:24:44.441Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(len(pages))\nfor i in range(238,246):\n    p=pages[i]\n    head=p.strip()[:200].replace('\\n',' | ')\n    print(i, repr(head[:160]))\nEOF",
 "description": "Inspect BQT v1 leaves near p.31"
}
```


### [2026-09-14T01:24:45.602Z] TOOL RESULT

```
777
238 'آرا | آداه بروزن خارا . آرایش. وآرایش | کننده و آراینده را کویند همچو خن آرا | و بزمآرا وامی باینمعتی هم هت ممنیآرایم | کن و بارا . | 9 | و پنجم است از هرماه شم'
239 'ت برایو بی اه آرامی | رة حواشی صفحة .۳ | ۵ آرامی_نام قومی از فبایل بدوی سامی ناد سوربه که درجنوب فلسطین در پبرامون | کوبر ومشرق رود اردن وبحرالمیت میزیستند. اين'
240 'آرامی - پرایی ۷۲٩\u200f س | آرامی بکاربردند. بدبنوجه زبان آرام یکه اززبانهای سامی\u200cاست وآموختنش برای\u200cهزدم مأی زبان | دشوار یست باخط آرامی که الفبابی.ساده بود سراسر کش'
241 'مخفف آوداس تکه نام روز بیست و پنجم از هر | ماه شمی باشد ۱- و ممکون ثالث معروف است | که له آسیا کرده باشد ۴ - و بمعنی تقصیر هم | ات | آ رث و له - (۱) بش فوفانی و'
242 ']دی ح بکر الث و رايع و سکون | تحتانی ۰ بمعنی ممنوی باشد که در مقابل لفظی | است ۰ چه آرش بمعنی «معنی» است ٩\u200f . | آدع بضم نالث و سکون غین نفطه | دار , مخفف آروغ ا'
243 'دوع ۰ با غن نقطه دار سس وزن | فاروق , بادی را گویند که از کلو باسدا برآید ؛ | و بجای غن , فاف نیز گفته آند و عوق فافه | کردهاند . | آدون- بر وزن قارون » صفتهای '
244 'در دل کسی\u200cجای کند ؛ وباین معلی بازای نفطه\u200cدار | هم آمده است . | 11 ۱ مه بسکون زای نقطه داره یمعنی | آرزو و خواهش با ابرام و حرص باشد در جمیع | امور - ونام جابی '
245 'سب چ ح | آزا۵ذارو- با دال ابجد بالف کشیده | و رای فرشت عضوم بواو زده » نوعي از چفندر | صحرابی است ریخ آنرا «حلیموه کوبند . ضماد | آن قری و مفاصل را نافع است . |'
```


## [2026-09-14T01:24:52.092Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (241,242):\n    print('==== leaf',i)\n    print(pages[i][:3500])\nEOF",
 "description": "Print BQT v1 leaves 241-242"
}
```


### [2026-09-14T01:24:53.214Z] TOOL RESULT

```
==== leaf 241
مخفف آوداس تکه نام روز بیست و پنجم از هر
ماه شمی باشد ۱- و ممکون ثالث معروف است
که له آسیا کرده باشد ۴ - و بمعنی تقصیر هم
ات
آ رث و له - (۱) بش فوفانی و سکون
واو و فتح لام ء آشی باشد مانندکاچ یکه از آرد
پزند و بیشتی مردم درویش و ففبر خورند وآنرا
جریی «سخینه » گویند .
ومشی آرد توله اس ت که آش کاچی مانند باشد .
]ددم - بنتح رابم و سکون عیم ۰
نام کل آذربون است که نوعی از شقایق وکل
همیشه بهار باشد .
] ذن - بفتح رابم و سکون نون »
,کفگیر سوراخپا دارد وبدلن چیزها صافیکنند.
وکفگیی را نی زکوبند - و نم ولاشی هم
ضت . ؟ *#
]رذهاله - بیای (») بالف کشیده
و فتح لام » بمعنی آرد توله است که آش کاچی
ماتثف باشنه.
آرش
]رده جتح زای حوز , کاحگل را
کوبند . و آن خاکی است که با کاه آمیزند
وگل سازئد و بر دبواز وبام خانه مالند .
آرژه گر - بفتحم کاف فارسی
و سکون رای فرشت . شنصی را کون که کاه
کل عاو...
| دست ع بروزن وارست. بمعنی‌توانت
باشد که ماضی تواشتن است - و مضفف آراست
هم هست که از آراستن باشد . ۴
۲ دسته - مسر وزن وارسته مخفف
آراسته باشف .
دش ٩‏ - بنتح ثاك و سکون شین
شطه دار ۰ نام پهلوانی بوده ابرانی از لشکی
منوچهر و در صنصت تبراندازی عدیل و نظیر
نداشته چنانچه تیری از آمل بمرو انداخته که
قربب بچهل روزه (۳ ) راء است ۰ وکونند آن
تبر مجوف بودماست وآنرا از شبنم پ رکرده‌بود »
و بوفت طلوع آفتاب بجاب مشرق اداخت *-
و نام پسردوم کیقباد هم است که او را «کی‌آرش»
گفتندی ۷ - و یکس ثالث ۸ - بععنی «معنی*
"4
۹ بونکر ۱۱۲ *.
؟ - پپلوی )27 « تاوادبا
۴ - ول : آرستن ۵ اوستا
۱ - از آن خوانند آرش را کمانگیر
که از آمل بمرو انداخت يك نی
و ۱۶۲
شتین چوکاوس با آفرین
2 مزدسنا ۷ ۰
مراد - معشوق » موب :
==== leaf 242
]دی ح بکر الث و رايع و سکون
تحتانی ۰ بمعنی ممنوی باشد که در مقابل لفظی
است ۰ چه آرش بمعنی «معنی» است ٩‏ .
آدع بضم نالث و سکون غین نفطه
دار , مخفف آروغ است . و آن بادی باشد که
با صدا ا زکلو برهیآ مد ۰
]رغاده (۱) - بر وزن مارساده + نام
رودخانه ات .
]دغده ؟- بن الك ( ۲ ) بر وزن
آزرده. بمعنی نخبناك (۳)وخشمگین وقهر آ لود -
و جنگاور باشد - و بفتخ الث حريصي در چپزها
را گویند .
۲۰ ریش «- بنتح اول و ثانی ۰ بر وزت
صم کیش ۷. بوست. بیرخت زرهاباخد وآنرا
دو دازو ها چشم نیزبکار برند .
۱ آآرمان ۴ بر وزن آسمان ۰ بمعنی
جح تب و آرزو - و رنج بردن باشد - و پشیمانی
و آفوی را نیز گویند . *
آمده - بکر میم ۵ . مخفف
وسکون میم بروزن دارنده. بمعنی دریغ‌وافوی
و پشیمانی باشد .
] دهش » بکس میم . مخنف آرامش
)۱ خم ۳ آارغاوه ۰
)4( خم ۳ 0 رنگ دادن.
و
است که ساکن شدن و آساش ‏ فراغت وراحت
کردن باشد .
آدهون - بر وزن ولژگون » زری
را گوند که پیش از کارکردن بکارگر و هزدور
دهند . و معربی «عربون» خواند . 4
| رهیفه » بر وزن نا رسیده . قرار
] دن ه بر وزن فارن . مخفف آرنج
است که بند گاه ساعدوبازو باشد. وبعربی«مرفق»
خوانند ۷ ,
اد نج - بر ون نارنج . بندکگاه
ساعد و بازوست که عرب « مرفق » گوید ۷ - و
بمعنی بازو هم بنظر آعده است که ازمرفق باشد
تا دوش .
]را نگ - باکاف فارسی. بروزن وهعنی
آرنج‌است که مرفی‌داشد - ور نگ ولون (4)را
یز کنته اند - و بمعنی حمانا و پنداری وگمان
بری حم‌آعده است - وونج ومجنت‌را عم گویشدب
و بمعئی مکر و حیله و فررت تیز حستتویمعنی
کونه وروش و طرز حم گفته‌اند چنانکه گویند :
«بدین آرنگ» یعنی بدین (۵) رز و باین دوش
و بدین گونه - و نام میوه‌ای هم مت - وحاکم
ملك را فیز گوشد ِب#
۲۱ ) خم ۳ : غشان.
۳ ت‌ اارغیش
آرمده سکون هیم -
6۵ در اشمار
ه آرمیدن _ ره : آرامدن ۰
براندیشه شد تا چهآ ید بدند
> مزدسنا ۷۹ ۱۹۸ و هی‎ ٩
( قاطع برهان 4 )
```


## [2026-09-14T01:25:17.999Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('FVQ_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('leaves',len(pages))\nfor i in (278,279,280):\n    print('==== leaf',i,'= p',i-17)\n    print(pages[i][:2600])\nEOF",
 "description": "Print Jeffery FVQ page 262"
}
```


### [2026-09-14T01:25:19.785Z] TOOL RESULT

```
leaves 335
==== leaf 278 = p 261
FOREIGN VOCABULARY OP THE QUR ? AN 261
The truth is that it is from a root related to JlS, but is not
an Arabic formation at all, being like the Heb. n3^*"JQ, a borrowing
from the Aram. Nn3*HQ, Syr. jAi^Lo. 1 Aram. NnS'HQ means
a province and then a city, 2 and Syr. (Ala ,10 is city? From Aram.
it was borrowed into Middle Persian where we find the ideogram
madma, meaning a large fortified city (PPGl, 150).
(Marjdn).
Iv, 22, 58.
Small pearls.
The word occurs only in a description of Paradise, and was early
recognized as borrowed from Persia, 4 but it is certain that it did not
come directly from Iranian into Arabic. 5
We find in Phlv. ^)jjp^ murvdnt,* a pearl used, e.g. in the
Gosht-i-Frydno, ii, 13, in describing the crowns presented to the
daughters of Spitama after death. From Middle Persian the word was
borrowed widely, e.g. Gk. jJiapyapirris 7 ; Aram. WP33"1Q ;
Syr. ]AjLl..;iO, and from some Aram, form 8 it came into Arabic.
It would have come at an early date for it is used in the old poetry
and was doubtless well known in the pre-Islamic period.
(Mursd).
xi, 43.
Harbour, haven.
1 Fraenkel, Fremdw, 280; Horovitz, KU. 137.
2 It has this meaning in Arabic as early as the Nemiira inscription ; cf. RES, i,
No. 483.
3 There is some discusaitm of the meaning of the word by Torrey in JAOS, xliii,
230 ff.
4 al-Jawallqi, Mu'arrab, 144 ; as-Suyuti, Itq, 324 ; MuJiit, sub voc., and sceSachau's
note to the Mu'arrah, p. 65.
3 In spite of Addai Sher, 144, and his attempted derivation from 0^.
6 West, Glossary, 213 ; 8aya*t, Glossary, 163 ; cf. Horn, Qrundriss, 218, n.
7 Also fiapyapis 1805, from which comes the Arm. t/uy^ 111^1111 and the European
forms.
8 Fraenkel, Fremdw, 59. The Mand. XDN^KaiXQ would also seem to be
from the same source, vide Noldeke, Mundart, 53 ; Mingana, Syriac Influence, 90 ;
Vollers, ZDMQ, 1, 611 ; li, 303.
==== leaf 279 = p 262
262 FOREIGN VOCABULARY OF THE QUR*AN
With this meaning it is used only in the Noah story, though the
same word occurs in vii, 186 ; Ixxix, 42, meaning fixed time. In this
lattersense it is obviouslyfrom U*> j, and the philologers want to derive
the ^-^A of xi, 43, from this same root. 1
It seems, however, that we have here a loan-word from Eth.
a haven (Noldeke, Neue Beitrage, 61 ; Bell, Origin, 29).
/ o^
** j* (Mary am).
Occurs some thirty-four times, cf. ii, 81.
The name refers always to the mother of Jesus, though in xix, 29 ;
iii, 31 ; Ixvi, 12, she is confused with Miriam, the sister of Moses and
Aaron (infra, p. 217).
Some of the philologers took the name to be Arabic, a form A*i*
from A 1 j, meaning to depart from a place. 2 Some, however, noted it as a
foreign word, 3 and Baid. on iii, 31, goes as far as to say that it is Hebrew.
Undoubtedly it does go back to the Heb. Q!J"1Q, but the vo welling
of the Arabic ^.i j* would point to its having come from a Christian
source rather than directly from the Hebrew. The Gk. Map/cr/i ;
Syr. .^o y vr> ; Eth. "ICf-lF are equally possible sources, but the
probabilities are in favour of its having come from the Syriac. 4
There seems no evidence for the occurrence of this form in pre-
Islamic times, 5 though the form A ju, the name of the Coptic slave
girl sent from Egypt to Muhammad, 6 is found in a verse of al-Harith b.
Hilliza, iii, 10 (ed. Krenkow, Beirut, 1922).
1 There was some uncertainty over the reading in this passage, see Zam. and Tab.
thereon, and LA, xix, 35, 36.
2 Jawhari, sub voc., LA, xv, 152.
8 al-Jawaliqi, Mu'arrab, 140 ; TA, viii, 132 ; al-Khafaji, 183.
4 Mingana, Syriac Influence, 82.
6 See the discussion in Horovitz, KU, 138-140 ; JPN, 154.
Ibn Hisham, 121 ; Usd al-Ghaba, v, 543, 544, and see Caetani, Annali,
iii, 828.
==== leaf 280 = p 263
FOREIGN VOCABULAKY OF THE QUR'AN 263
Ixxvi, 5, 17 ; Ixxxiii, 27.
Tempering.
Both passages refer to the tempering of the drink of the blessed
in Paradise.
The Muslim authorities take it from j to mix, but Fraenkel,
Fremdworter, 172, points out that 7*\j-* is not an Arabic formation*
but is the Syr. MO potus mixtus, which later became technically used
for the eucharistic cup of mixed water and wine. In fact the Syr. ..lio
(cf. Heb. JTQ ; Aram. 3H3), while used for mixing in general, became
specialized for the mixing of drinks. There can thus be little doubt
that it was borrowed in pre-Islamic times as a drinking term. 1 See
also under r-u^ (infra, p. 70).
(Masjid).
Occurs some twenty-eight times, e.g. ii, 139, 144, 145, 187, 192, etc.
A place of worship.
As we have already seen (infra, p. 163), the verb Jbcu*- in the technical
sense of worship has been influenced by Aramaic usage. The form
seems not to have been a formation from this in Arabic, but to
have been an independent borrowing from the North.
Noldeke, ERE, i, 666, 667, has drawn attention to this fact.of the
Aramaic origin of the word. In the Nabataean inscriptions we find
N"f30Q not infrequently meaning " place of worship ", 2 as fot
example in an inscription from Bosra (de Vogiie), p. 106 3 : HT
^sn-^in^i nn inti nain irnoo - This is the P iace of
worship which Taimu, son of Walid el-Ba'al built." The Syr. 1^. Jao&o,
however, seems to be a late borrowing from the Arabic, but we find
KH30Q in the Elephantine papyri. 4
1 Horovitz, Parodies, 11; Geyer, Zwei Qedickte, i, 87 ff. ; Ximmern, Akkad.
Fremdw., 40.
2 Cook, Glossary, 75 ; Duval in JA, viii c Ser., vol. xv, 482.
3 ZDMO, xxii, 268.
4 Cowley, Aramaic Papyri, p. 148.
```


## [2026-09-14T01:25:36.290Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"^Mary,\\|^Maria,\\|^Marilyn\\|^Marvin\\|^marijuana\\|^marihuana\\|^Marian\" KLN_1966.txt | head -20\necho \"=== 1971\"\ngrep -n \"^Mary,\\|^Marilyn\\|^Marvin\\|^marijuana\\|^marihuana\\|^Marianne\" KLN_1971.txt | head -20",
 "description": "Grep Klein for Mary etc."
}
```


### [2026-09-14T01:25:36.382Z] TOOL RESULT

```
22932:Maria,  fem.  PN.  —  Late  L.  See  Mary.
22933:Marian,  adj.,  1)  pertaining  to  the  Virgin  Mary;
22935:Marian,  n.,  a  follower  of  Mary,  Queen  of  Scots. See  prec.  word.
22936:Marian,  Marianne,  fem.  PN.  —  Marian  is  a collateral  form  of  Marion,  dimin.  of  F.  Marie (see  Mary),  but  was  mistaken  later  for  the  com¬ pound  of  the  two  names  Mary  and  Annie) (whence  the  spelling  Marianne). marigold,  n.,  a  yellow-flowered  plant.  —  A  hy¬ brid  coined  fr.  Mary  (prob.  the  Virgin)  and gold.
22937:marihuana,  marijuana,  n.,  1)  the  hemp  plant ;  2)  a narcotic  obtained  from  its  dried  leaves  and flowers.  —  Mex.  Sp.,  prob.  a  contraction  of Maria  Juana  (=  ‘Mary  Jane’),  so  called  from the  alleged  sexual  appeal  of  the  drug.
22938:Marilyn,  fem.  PN.  —  Dimin.  of  Mary, marimba,  n.,  a  kind  of  musical  instrument.  — Bantu  malimba,  marimba,  pi.  of  limba,  name  ol a  musical  instrument.
23034:Mary,  fem.  PN.  —  ME.  Marie,  fr.  OE.  Maria, Marie,  fr.  L.  Maria,  fr.  Gk.  Mapiap,  Mapta, fr.  Aram.  (Targum)  Maryam,  fr.  Heb.  Miryam, which  is  of  uncertain  origin.  See  Miriam,  and cp.  Marianne,  Marion,  marionette, marzipan,  n.  —  See  marchpane.
=== 1971
145308:marihuana, marijuana, n., 1) the hemp plant; 2) a 
145314:Marilyn, fem. PN. — Dimin. of Mary. 
145941:Mary, fem. PN. — ME. Marie , fr. OE. Maria y
```


## [2026-09-14T01:25:44.328Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"^Miriam\\|^Marvin\\|Merfyn\" KLN_1966.txt | head\necho \"--- leaves\"\npython3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nfor target in ['Mary,  fem.','Marilyn,  fem.','marihuana,  marijuana','Miriam']:\n    i=t.find(target)\n    if i<0: print(target,'NOT FOUND'); continue\n    leaf=t[:i].count('\\f')\n    print(target,'leaf',leaf,'approx pages',(leaf-12)*2,(leaf-12)*2+1)\nEOF",
 "description": "Klein Miriam/Marvin and page mapping"
}
```


### [2026-09-14T01:25:45.578Z] TOOL RESULT

```
24012:Miriam,  1)  fem.  PN.,  2)  in  the  Bible,  the  sister  of Moses  and  Aaron  (see  Ex.  15:20).  — -  Heb. Mirydm.  Cp.  Mary  and  words  there  referred  to. mirific,  adj.,  working  wonders;  marvelous.  —  F. mirifique,  fr.  L.  mirificus,  ‘causing  wonder, wonderful’,  which  is  compounded  of  mirus, ‘wonderful’,  and  -ficus,  fr.  -ficere,  unstressed form  of  facer  e,  ‘to  make,  do’.  See  miracle  and -fie.
--- leaves
Mary,  fem. leaf 506 approx pages 988 989
Marilyn,  fem. leaf 504 approx pages 984 985
marihuana,  marijuana leaf 504 approx pages 984 985
Miriam leaf 506 approx pages 988 989
```


## [2026-09-14T01:25:53.796Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (504,505,506):\n    p=pages[i]\n    print('=== leaf',i, repr(p[:120]))\n    print(repr(p[-200:]))\nEOF",
 "description": "Check Klein leaf running heads"
}
```


### [2026-09-14T01:25:54.969Z] TOOL RESULT

```
=== leaf 504 '=  F.)  marche,  fr.\nmarcher.  See  prec.  word  and  cp.  demarche. March,  n.  —  ME.,  fr.  OF.  march,  also  marz  '
'e  marshal.\nMarist,  n.,  member  of  a  Roman  Catholic  order.\n—  F.  Mariste,  fr.  Marie.  See  Mary  and  -ist.\nmarital,  adj.,  1)  pertaining  to  a  husband;  2)  per¬ taining  to  marriage.  '
=== leaf 505 "—  L.  maritalis,  ‘of  mar¬ riage',  fr.  maritus,  ‘a  married  man,  husband’, which  is  of  uncertain  etymology.  "
"fr.  L.  maritare,  'to  wed,  marry, give  in  marriage’  (whence  also  It.  maritare, Rum.  maritd,  OProven?.,  Catal.  Sp.  and  Port. maridar,  ‘to  marry’),  fr.  maritus,  'married, husband’. "
=== leaf 506 ' See  marital  and  marriage.\nDerivatives:  marri-ed,  adj.,  marri-er,  n.\nMars,  n.,  the  Roman  god  of  war.  —  L.'
'ash,  tr.  v.,  to  make  love  to;  intr.  v.,  to  flirt.  — Fr.  mash,  ‘to  convert  into  a  mash’,  etc.  See  prec. word.\nDerivative:  mash-er,  n.\nmashie,  mashy,  n.,  an  iron  golf  club.  '
```


## [2026-09-14T01:26:24.131Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD watkins Mary/Miriam/marijuana\"\ngrep -n -i \"MARY\\b\\|MIRIAM\\|MARIJUANA\\|MARVIN\\|MARILYN\" AHD_watkins1985.txt | head -20\necho \"=== AHD bear root\"\ngrep -n \"^rtko-\\|^r̥tko-\\|ARCTIC\\|URSINE\" AHD_watkins1985.txt | head -20",
 "description": "Grep Watkins AHD"
}
```


### [2026-09-14T01:26:24.208Z] TOOL RESULT

```
=== AHD watkins Mary/Miriam/marijuana
83:the contraction of early Indo-European short vowels with a following 9. Already in Proto- Indo-European itself, two of the three laryn- geals had the property of coloring an adja- cent fundamental vowel e to a and o, respectively, before the contractions took place. Thus the root pa-, “to protect,” is contracted from older *paa-, with ‘“‘a- coloring”; the root d6-, “to give,” is con- tracted from older *doo-, with “o-coloring”; and the root dhé-', “to set, put,” is con- tracted from older *dheo-, without coloring. The fundamental vowel in each of these roots, as in most Indo-European roots, was originally e. In scholarly usage it is now customary to write the non-coloring laryn- geal as 9,, (or h,), thus *dheo,-; the a-coloring laryngeal as a, (or h,), thus *pas.-; and the o-coloring laryngeal as a; (or hz), thus *doo,-. This rather cumbersome notation has been simplified in this Dictionary, since the vowel before the schwa is sufficient to distinguish the three in the cases of contraction to a long vowel, and in other positions in most lan- guages other than Greek the three merge to one. No systematic notice has been taken in this Dictionary of word-initial laryngeals before vowels (amply attested in Hittite), since the root forms with initial vowel are readily convertible by the student. Thus ap-?, “water,” from *sap- (Hittite happ-, “water”; op-', “to work, produce in abun- dance,” from *sop- (Hittite happ-in-, “rich”’); ed-, “to eat,’ from 9ed- (Hittite ed-, “to eat”).
98:The root plus the suffix or suffixes consti- tuted the stem. The stems represented the basic lexical stock of Indo-European, the separate words of its dictionary. Yet com- monly a single root would furnish a large number of derivative stems with different suffixes, both nominal and verbal, much as English Jove is both noun and verb as well as the base of such derivatives as lovely, lover, and beloved. For this reason it is customary to group such collections of derivatives, in a variety of Indo-European languages, under the root on which they are built. The root entries of this Dictionary are arranged in this way, with derivatives that exhibit similar suffixes forming subgroups consisting of Indo-European stems, or words.
115:these, where a word is attested in several traditions, it is still customary to call it Indo- European, even though it may not date from the remotest reconstructible time. It is in this sense, universally accepted by scholars, that the term Indo-European has been used in this Dictionary.
173:It was probably not long before the disper- sal of the Proto-Indo-European community that the use of the wheel and wheeled trans- port was adopted. Despite the existence of widespread word families, most terms relat- ing to wheeled vehicles seem to be metaphors formed from already existing words; they are not primitives or primary vocables. So the word for AXLE (aks-) may mean simply “a pivotlike juncture”; the NAVE or hub of the wheel (nobh-) is the same word as NAVEL. This is clearly the case with WHEEL itself, where the widespread *k(e)-k“l-o- is an ex- pressive derivative of a verb (k"el-') meaning “to revolve or go around.” Other words for “wheel” are dialectal and again derivative, like Latin rota from a verbal root ret-, “to run.” A root wegh-, “to go, transport in a vehicle” (WAGON), is attested quite early, though not in Hittite. This evidence for the late appearance of the wheel agrees with archaeological findings that date the distri- bution of the wheel in Europe to the latter
379:zero-grade form *dhra-gh- in: a. Greek tarassein (Attic tarattein), to confuse, disturb: ATARACTIC; b. Greek trakhus, rough: TRACHEA, TRACHOMA, TRACHYTE. [Pok. 1. dher- 251.] dher-2, To hold firmly, support. 1. Suffixed form *dher-mo- in Latin firmus, firm, strong: FARM, FERMATA, FIRM, FIRMAMENT; AFFIRM, CONFIRM, INFIRM, (INFIR- MARY). 2. Extended form *dhergh- possibly in Latin fortis, strong (but this is also possibly from bhergh-?). 3. Suffixed zero-grade form *dhr-ono- in Greek thronos, seat, throne (< “support”): THRONE. 4. Suffixed form *dher-mn in Sanskrit dharma, statute, law (< “that which is established firmly”): DHARMA. 5. Old Persian dar-, to hold (whence Persian -ddr, ‘“-holder’’): SIRDAR, TAHSILDAR, ZAMINDAR. [Pok. 2. dher- 252.] dher-3, To drone, murmur, buzz. Extended zero-grade form *dhrén- in: a. Germanic *drén- in Old English dran, drén, male honeybee: DRONE}; b. Greek thrénos, dirge, lament: THRENODY. [Pok. 3. dher- 255.] dhers-. To venture, be bold. 1. O-grade form *dhors- and zero-grade form *dhrs- respectively in Germanic *ders- and *durs- in Old English dearr and durst, first and third person singular present and past indicative of durran, to venture: DARE, (DURST). 2. Possibly Latin -festus in: a. infestus, hostile (? < “directed against”; in-, into, against; see en): INFEST; b. manifestus, palpable, evident (< “caught red-handed, grasped by the hand”; manus, hand; see man-2): MANIFEST. [Pok. dhers- 259.] dhés-. Root of words in religious concepts. Possibly an extension of dhé-'. 1. Suffixed form *dhés-yd in Latin fériae (Old Latin fésiae), holidays: FAIR?, FERIA. 2. Suf- fixed form *dhés-to- in Latin féstus, festive (> German Fest, festival): FEAST, (-FEST), (FESTAL), FESTIVAL, FES- TIVE, FESTOON, (FETE), FIESTA; (GABFEST), OKTOBER- FEST. 3. Suffixed zero-grade form *dhas-no- in Latin fanum, temple: FANATIC; PROFANE. 4. Possibly suffixed zero-grade form *dhas-o- becoming *dhes-o- in Greek theos (< *thes-os), god: THEO-; APOTHEOSIS, ATHEISM, ENTHUSIASM, PANTHEON, POLYTHEISM. [Pok. dhés- 259.] dheu-'. Also dheue-. The base of a wide variety of derivatives meaning “to rise in a cloud,” as dust, vapor, or smoke, and related to semantic notions of breath, various color adjectives, and forms denoting defective perception or wits. 1. Suffixed extended zero-grade form *dhii-mo- (<*dhua-mo-), smoke, in: a. Latin fimus, smoke: FUMAROLE, FUMATORIUM, FUMATORY, FUME; FUMARIC ACID, FUMIGATE, FUMITORY, PERFUME; b. Greek thumos, soul, spirit: -THYMIA; ENTHYMEME; c. Greek thumon, thumos, thyme (< “plant having a strong smell”): THYME. 2. Suffixed lengthened zero-grade form *dhi-li- in Latin filigd, soot: FULIGINOUS. 3. Ex- tended form *dheus- possibly in Germanic *dus- in: a. Old English dysig, foolish (< “stupefied,” “confused”): pD1zzy; b. Danish dase, to make drowsy, akin to the probable Scandinavian source of DOZE. 4. Suffixed ex- tended form *dheus-o- in Germanic *deuzam, breathing creature, animal, in: a. Old English déor, animal: DEER; b. Old Norse dyr, animal, deer: REINDEER. 5. Suffixed o-grade form *dhous-o in Slavic *dukh- in Russian dukh, breath, spirit: DUKHOBoR. 6. Variant extended form *dhwes- in nasalized form *dhwens- in Germanic *duns-, dust, meal, in: a. Germanic suffixed form *duns-to- in Old English dist, dust: pustT; b. Old Norse diinn, bird’s down (< “fine like dust”): DOWN?, DUVETYN; (EIDER- Down). 7. Extended zero-grade form *dhus- in Greek thuos, burnt sacrifice, incense (> Latin thus, incense), and ¢huia, cedar: THUJA, THURIBLE; (THURIFER). 8. Suf- fixed extended zero-grade form *dhus-ko- in: a. Ger- manic duskaz in Old English dox, twilight: Dusk; b. Latin fuscus, dark, dusky: OBFUSCATE. 9. Suffixed extended zero-grade form *dhus-no- in Welsh dwn, dull brown color, whence Old English dun(n), dark-brown: DUN2, 10. Zero-grade extended form *dhubh- in Greek tuphein (< *thuphein), to make smoke, and tuphios,
459:ers-2. To be wet. Variant form *ros- in Latin rés, dew: ROSEMARY. [Pok. 2. ere-s- 336.]
839:parative) form *pro-tero- in Greek proteros, before, former: HYSTERON PROTERON, PROTEROZOIC. VI. Exten- ded forms *prai-, *prei-. 1. Latin prae, before: PRE-; PRETERIT. 2. Suffixed (comparative) form *prei-yos- in Latin prior, former, higher, superior: PRIOR2. 3. Suffixed form *prei-wo- in: a. Latin privus, single, alone (< “standing in front,” “isolated from others”): PRIVATE, PRIVILEGE, PRIVITY, PRIVY; DEPRIVE; b. Latin proprius, one’s own, particular (< pré priv6, in particular, from the ablative of privus, single): PROPER, PROPERTY; APPRO- PRIATE, PROPRIOCEPTION, PROPRIOCEPTOR. 4. Extended form *preis- in: a. suffixed (superlative) form *preis-mo in (i) Latin primus (< *prismus; ablative plural primis), first, foremost: PREMIER, PRIMAL, PRIMARY, PRIMATE, PRIME, PRIMITIVE, PRIMO, PRIMUS; IMPRIMIS, PRIMA FACIE, PRIMAVERA, PRIMEVAL, PRIMIPARA, PRIMOGENI- TOR, PRIMOGENITURE, PRIMORDIAL (ii) Latin compound princeps, “he who takes first place” (-ceps, “-taker”; see kap-), leader, chief, emperor: PRINCE, PRINCIPAL, PRIN- CIPLE; b. suffixed form *preis-tano- in Latin pristinus, former, earlier, original: PRISTINE. VII. Extended form *pres- in compound “*pres-g“u-, “going before” (*gvu-, to go; see gWa-), in Greek presbus, old, old man, elder: PRESBYTER, (PRIEST); PRESBYOPIA. VIII. Extended form *proti in Greek pros, against, toward, near, at: PROS-; PROSOPOPEIA. Other possibly related forms are grouped under per-2, per-3, per-4, per-5, and per-’. [Pok. 2. A. per 810.] per-?. To lead, pass over. A verbal root belonging to the group of per’. I. Full-grade form *per-. 1. Suffixed form *per-tu-s in Germanic “*ferthuz, place for crossing over, ford, in Old Norse fjérdhr, an inlet, estuary: FIRTH, FJORD. 2. Suffixed form *per-ond in Greek peroné, pin of a brooch, buckle (< “that which pierces through”): PERONEAL. II. O-grade form *por-. 1. Germanic *faran, to go, in: a. Old English faran (> Middle English faren), to go on a journey, get along: FARE; WAYFARER, WAY- FARING, (WELFARE); b. Old High German faran, to go, travel: GABERDINE. 2. Suffixed form *por-o-, passage, journey, in Greek poros, journey, passage: PORE”; EMPO- RIUM, POROMERIC. 3. Suffixed (causative) form *por- eyo-, to cause to go, lead, conduct, in Germanic *farjan, to ferry, in Old English ferian, to transport: FERRY. 4. Lengthened-grade form *pdér- in: a. Germanic suffixed form *f6r-ja- in Old English (ge)féra, “fellow-traveler,” companion (ge-, together, with; see kom): FERE; b. Ger- manic suffixed (causative) form *fér-jan in Old High German fuoren, to lead: FUHRER. 5. Possibly suffixed form *por-no-, feather, wing (< “that which carries a bird in flight”), in: a. Germanic *farnd, feather, leaf, in Old English fearn, fern (having feathery fronds): FERN; b. Sanskrit parnam, leaf, feather: PAN2. III. Zero-grade form pr-. 1. Suffixed form *pr-tu-, passage, in: a. Ger- manic *furdu- in Old English ford, shallow place where one may cross a river: FORD; b. Latin portus, harbor (< “passage”): PORT!; IMPORTUNE, OPPORTUNE. 2. Suffixed form *pr-té in Latin porta, gate (> Old French porte, door): PORCH, PORT’, PORTAL, PORTCULLIS, PORTE-CO- CHERE, PORTER®, PORTICO, PORTIERE, PORTULACA. 3. Suffixed (denominative) form *pr-to- in Latin portdre, to carry: PORTS, PORTABLE, PORTAGE, PORTAMENTO, PORTATIVE, PORTER}; COMPORT, DEPORT, EXPORT, IM- PORT, (IMPORTANT), PORTFOLIO, PURPORT, RAPPORT, REPORT, (SPORT), SUPPORT, TRANSPORT. [Pok. 2. B. per 816.]
1678:INERTIA ar- INEXORABLE 6r- INFAMOUS bha-2 INFANT bha-2 INFANTRY bha-2 INFARCT bhrekw- INFECT dhé-1 INFELICITY dhé&(i)- INFER_ bher-1 INFERIOR ndher- INFERNAL ndher- INFERNO ndher- INFEST dhers- INFEUDATION peku- INFIDEL bheidh- INFIRM dher-2 INFIRMARY dher-2 INFIX dhigw- INFLAME bhel-1 INFLATE bhié-2 INFLICT  bhiig- INFLUENCE bhieu- INFLUENZA bhleu- INFRA- ndher- INFRACT bhreg- INFRANGIBLE bhreg- INFRINGE bhreg- INFUSE gheu- INGENIOUS gene- INGENUOUS gene- INGEST gerere INGRATE gWere-3 INGRATIATE gWere-3 INGRESsS ghredh- INGUINAL engW- INGURGITATE gWere-4 INHABIT ghabh- INHERE ghais- INHERIT ghé- INHIBIT ghabh- INHUME dhghem- INIMICAL amma INITIAL ej-1 INITIATE ei-1 INJECT yé- INJUNCTION yeug- INJURY yewes- INK kéu-
2131:PRIMA FACIE dhé-1, per? PRIMAL pert PRIMARY per! PRIMATE pert PRIMAVERA per', wes PRIME per! PRIMEVAL aiw-, per? PRIMIPARA pert PRIMITIVE per PRIMO per! PRIMOGENITOR pert PRIMOGENITURE gene-, per? PRIMORDIAL af-, per? PRIMUS pert PRINCE pert PRINCIPAL pert PRINCIPLE per? PRINT per-5
2199:ROOF kropo- ROOK! ker-2 ROOM reua- ROOST kred- ROOT! wrad- ROOT? wrdd- ROPE rej-1 RORQUAL = reudh-1, (s)kWal-o- ROSE! wrod- ROSEMARY ers-2 ROSTRUM_ réd- ROTA ret- ROTARY ret- ROTATE ret- ROTE? reu-! ROTE3 krut- ROTIFORM ret- ROTOGRAVURE ret- ROTUND ret- ROTUNDA ret- ROUGE reudh-1 ROUGH ruk-2 ROULETTE ret- ROUND! ret- ROUND? riino- ROUT! reup- ROUTS = reu-1 ROUX reudh-1 ROVER reup- Row! rej-1
=== AHD bear root
900:a. Old English risan, to rise: RISE; b. Old English drisan, to arise (G-, up, out): ARISE. 2. Germanic causative *raizjan in: a. Old English réran, to rear, raise, lift up: REAR?; b. Old Norse reisa, to raise: RAISE.] rtko-. Bear. 1. Latin ursus, bear (< *orcsos): URSINE. 2. Greek arkios, bear: aRcTIC, ARcTURUS. 3. Celtic *arto- in Welsh arth, bear, in the name Arthur (> Medieval Latin Artorius, Arthur): ARTHUR. [Pok. tktho-s 875.] ruk-1, Fabric, spun yarn. Celtic and Germanic root. 1. Germanic *rukk6n- in: a. Italian rocca, distaff: ROCKET!; b. Old High German rocko, distaff: ROCAM- BOLE; C. Old French rocquet, head of a lance: RATCHET. 2. Germanic *rukka- in Old French rochet, rochet: ROCH- ET. [Pok. ruk(k)- 874.] ruk-2. Rough. Extension of reu-2. 1. Lengthened-grade form *rik- in Germanic *riéhwaz in Old English rih, rough, coarse: ROUGH. 2. Lengthened variant form *rig- in Latin riga, wrinkle: RUGA, RUGOSE; CORRUGATE. [In Pok. 2. reu- 868.] runo-. Mystery, secret. Germanic and Celtic technical term of magic. Germanic *riinaz in: a. Old English riinian, to whisper: ROUND?; b. Old Norse riin, secret writing (akin to the Germanic source of Finnish runo, song, poem): RUNE!, RUNE?. [In Pok. 1. reu- 867.] sa-. To satisfy. Contracted from *sas-. 1. Suffixed zero-grade form *s9-to- in: a. Germanic *sadaz, sated, in Old English sed, sated, weary: SAD; b. derivative Ger- manic verb *sadon, to satisfy, sate, in Old English sadian, to sate: SATE!. 2. Suffixed zero-grade form *s9-ti- in Latin satis, enough, sufficient: SATIATE, SATIETY; (ASSAI2), ASSET, SATISFY. 3. Suffixed zero-grade form *s9-tu-ro- in Latin satur, full (of food), sated: SATIRE, SATURATE. 4. Suffixed zero-grade form *so-d-ro- in Greek hadros, thick: HADRON. [Pok. sd- 876.] sab-. Juice, fluid. 1. Germanic *sapam, juice of a plant, in Old English sp, sap: SAP}. 2. Illyrian sabaium, beer, probably akin to the source of Italian zabaglione, zabaione, a frothy dessert: ZABAGLIONE. [In Pok. sap- 880.] sag-. To seek out. 1. Suffixed form *sdg-yo- in Germanic *sdkjan in Old English sécan, sécan, to seek: SEEK. 2. Suffixed form *sdg-ni- in Germanic *sdkniz in Old English sdcn, attack, inquiry, right of local jurisdiction: SOKE. 3. Zero-grade form *sog- in Germanic *sak- in: a. derivative noun *saké, “a seeking,” accusation, strife, in Old English sacu, lawsuit, case: SAKE}; b. Germanic *sakjan, to lay claim to (denominative of *sak6), in Old French seisir, to take possession of, seize: (SEISIN), SEIZE; c. Germanic *sakan, to seek, accuse, quarrel, in (i) Old English forsacan, to renounce, refuse (for-, prefix denot- ing exclusion or rejection; see per'): FORSAKE (ii) Old Norse saka, to seek: RANSACK. 4. Independent suffixed form “sdg-yo- in Latin sdgire, to perceive, “seek to know”: PRESAGE. 5. Zero-grade form “sog- in Latin sagdx, of keen perception: SAGACIOUS. 6. Suffixed form *sdg-eyo- in Greek hégeisthai, to lead (< “to track down”): EXEGESIS, HEGEMONY. [Pok. sdg- 876.] sai-. Suffering. 1. Germanic *sairaz, suffering, sick, ill, in Old English sdr, painful: sore. 2. Derivative Germanic adjective *sairigaz, painful, in Old English sarig, suffer- ing mentally, sad: SORRY. [Pok. sdi-, 877.] sak-. To sanctify. 1. Suffixed form *sak-ro- in: a. Latin sacer, holy, sacred, dedicated: SACRED; CONSECRATE, EXECRATE; b. compound *sakro-dhét-, “performer of sacred rites” (*-dhét-, doer; see dhé-'), in Latin sacerdés, priest: SACERDOTAL. 2. Nasalized form *sa-n-k- in Latin sancire (past participle sanctus), to make sacred, conse- crate: SAINT, SANCTUM; CORPOSANT, SACROSANCT, SANC- tiFy. [Pok. sak- 878.] sal-1, Salt. 1. Extended form ‘*sald- in: a. suffixed form *sald-o- in Germanic *saltam in Old English sealt, salt: SALT; b. Germanic zero-grade suffixed extended form *sult-j6 in (i) Old French sous, pickled meat: SOUSE (ii)
1258:ARCHON arkhein -ARCHY arkhein ARCIFORM = arku- ARCTIC rtko- ARCTURUS rtko-, wer-4 ARCUATE = arku- ARDENT as- ARDOR as- ARDUOUS erad- ARE! er-1 ARGAL? reg-! ARGENT arg- ARGENTINE arg- ARGIL arg- ARGININE arg- ARGON werg- ARGONAUT nau-2 ARGUE arg- ARHAT alg’h- ARIA wer-2 ARID as- ARIES er-3 ARISE risan ARISTOCRACY ar- ARITHMETIC ar-
2437:UNITY oi-no- UNIVERSE 0i-no-, wer-3 UNIVOCAL wekw- UNKEMPT gembh- UNTIL ant- UNWITTING weid- UP upo UPANISHAD sed-1, upo UPBRAID bherek- UPROAR kere-, upO UPSILON bhes-! URCHIN ghers- UREDO eus- URETER wers-2 URETHRA wers-2 URETIC wers-2 URGE wreg- -URGY werg- -URIA wers-2 URINE wér- URO-! wers-2 URO-2 ors- URONIC wers-2 -UROUS ors- URSINE rtko-
```


## [2026-09-14T01:26:40.583Z] TOOL CALL #31: Bash

```json
{
 "command": "ls site/pages/426.jpg 2>/dev/null; pdftoppm -f 426 -l 426 -r 200 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg426 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg426.png",
 "description": "Render PDF page 426"
}
```


### [2026-09-14T01:26:42.326Z] TOOL RESULT

```
site/pages/426.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb 67629 Sep 13 21:26 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg426.png
```


## [2026-09-14T01:26:44.372Z] TOOL CALL #32: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg426.png"
}
```


### [2026-09-14T01:26:44.995Z] TOOL RESULT

```

```


## [2026-09-14T01:26:44.987Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-14T01:27:01.714Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KNT Arsama\"\ngrep -n -i \"Aršāma\\|Arsama\\|Arshama\" KNT.txt | head -10\necho \"=== NYB xirs\"\ngrep -n -i \"xirs\\|hls\" NYB_vol2_glossary.txt | head -10\necho \"=== IEC bear\"\ngrep -n \"r̥k̑\\|rkto\\|ursus\" IEC.txt | head -10\necho \"=== SYN bear\"\ngrep -n -i \"12.31\\|'bear'\" SYN.txt | head -5\ngrep -n \"ursus\" SYN.txt | head -5",
 "description": "Grep Kent, Nyberg, Mann, Buck"
}
```


### [2026-09-14T01:27:01.836Z] TOOL RESULT

```
=== KNT Arsama
563:! Greek єр is not conclusive evidence for 7, despite xépoa = karía- and Zytphs = Bardiya, both with у ($80); ef. "Гутафёриує = Vitdafarnd, with -ar-, and 'Apseáum = Aršāma and 'Apratiptys = ArtaxSacd, both with r by the Elam. testimony, despite Gr. ар-. Several Greek transliterations of place-names have ap for Persian ar: Tapa = Paréava, Xayapría = Asagaria, etc.
1438:Saka-, Sug(u)da-, Nisdya-, si*kabru-, and the 3 dubious siyamam. 3 5117. рів. f from pIE s after certain sounds 1 (8115) remained unchanged in OP: у ОР тав: Ма- ‘greatest’, Av. masisla-, Gk. шікито 5 "longest". : OP fràisayam ‘I sent’, Skt. ejayat? ‘he brings’, OP uška- ‘dry’, Av. huska-, Lith. satisa-s. OP gausa- ‘ear’, Skt. ghóga- ‘noise’. 4 OP adarínaus ‘he dared’, Skt. dhysnéti ‘he dares’. 4 OP aría- ‘male’ in ArSama- ‘Arsames’, Skt. 4 rsa-bhd- ‘bull’. 4 pIE *sed-as- in ОР Лай ‘seat’, cf. СК. &os (from -$ pIE *sedos). 4 pIE *e-st-sfe-to, OP ачЧаіа ‘he stood’, cf. Gk. : israrat ‘he stands’ (from *sestatat). 4 pIE *rsti-, OP nom. arštiš, Skt. rstf-s (cf. $115). 4 OP nom. tani ‘body’, Skt. tani-s. 4 For ks and other clusters giving zš, see $102; 4 for kn and gn giving initial тп and medial im, 4 $06; for -Sc- as a sandhi product, $105; for pAr. 4 & giving OP Sy, $104; for pAr. t giving OP y 4 $80; for pAr. én giving OP $n, $82. 1 The verbal prefix ni- affects an initial s of the 4 verbal root; thus ni-$d- from ni- + stä- and 4
1914:b. Genitive: Arta-xéaga- ‘Having a kingdom of justice’; Aršāma- (from *aría-ama-) ‘Having the might of a hero’; Haxd-manis- ‘Having the mind of a friend’; Garma-pada- ‘(Month) having the place of heat’; Asa-garta- (Тапа) having caves of stone’. :
3441:5 :08ty : Arsama : xSayaéiya : Au
3462:3 üspahyà : риса : Aršāmahyā : napa : Haxdmanisiya : Oatiy :
3464:5 dma : Arsamahyà : pita : Ariyaramna : Ariyáramnahyá : pita : Сехр : Сір 6 45 : pita: HaxdmaniS : иу : Dàrayavaus : x&ayafiya : avahyarà
3961:4 ArSimahyi : napá : HaxàmaniSiya ; даћу : I 7 Раа 1 5 yavauš :xSáyaüiya :manà:pità: Vistaspa ;Vi — : 6 štāspahyā : pità : Arsama : ArSamahyà : pi
=== NYB xirs
2101:i [Prs inscr., Ps.. ZY; BP contracted to a ligature coinciding with y: ZY, except when connected with an encl. pron.: ZY- m = i-m, ZY -t = i-t, ZY -š = 4-6, ZY-m’n' = i-mān, ZY-Vn' = i-tün, ZV šin! +-šān] A. a) relative pron., may be used as the subj. or the dir. obj. of its clause: hān i ó man mat 12°; én fradand + andar aškamb därem 1013; has no cas. obl; instead it takes an encl. pron. referring to the correlate: hàn ... i- dmocišn he whose education 80" (rare, commonly k&-$); cannot be governed by a prep.; instead the prep. is placed ?n the clause and governs a pron. referring to the corre- late: *sīh-ē (v. ?sih) ... $ hac han nēva- koktar butan ne šāyist ‘splendor quo nullus pulchrior esse poterat’, a *splend- our that was the most beautiful. ever existent 717-18; or the prep. is changed into an adv. connected with the vb. of the clause: méx i patiš bandēnd 300 xirs poles on which they fasten 300 *rings 2026 (bastan construed with pat; patiš the adv. of pat, v.s.v. patiš); in such cases ke is more usual. — b) conj.: &on l . $ so ... that 2016-17, 3226-27; cand i as much as 3119; 4 ka, hān 4 ka, v. ka; —i-šān 4, 1-8 $ when, as soon as 5811,
4277:xirs
4287:*xirs [hls] "a ring, or the like: 20%. — Both reading and meaning are guite un- certain. Arab has virs-, xurg- ‘a ring
4289:. xirs
=== IEC bear
467:al^sios (aliksos, al?snos, alksnios) ‘alder’. WP 1, 151 Mac. álixa ‘white poplar’; Lat. alnus; OHG alansa, alunsa, elirs; G Else with variants (see Kluge 17: Erle, Eller); Gmc. LW in Sp. aliso; ON alri, elti, elrir, ọlr; Sw. al; Du. els; OE alor, ellen; Russ. olíxa; Cz. ol$e; Slovak jelša; Srb. jelša and joha; Pol. olcha, olsza; Slovene jelša, olša; Li. alksnis, gs. io; Latv. alksnis, gs. alkšna. Cf. Basque altz “alder”. (The great variety of forms points to a non-IE origin, and the rhyme of Basque altz < *alks-: artz ‘bear’ < *arks- lends colour to this view. The laryngal posited for the prototype is re- flected in the forms o?st- (“bone”, cf. -k- in Li. kab-akštis ‘skeleton’, cf. Gk. ostéon; r?s- “bear”, cf. Gk. árktos; au?som: Lat. aurum: Li. auksas, cf. Basque urhe ‘gold’, in which glottalism is indicated in Lithuanian and Latvian by -k-. The a-vocalism is, for H. Krahe, an indication of *pre-European' origin in names of major lakes and rivers in Europe and W. Asia)
3831:Gk. árktos, (hapax) árx; Alb. arí, gs. aríu, f: arushé; Lat. ursus; Gaul. arto-; W arth; Cor. ors (sic); Br. -arz (in kraban-arz 'bear's breech’); Li. irstva ‘bears den (The name is based on the bear's grunt, cf. Li. urksti, Latv. urk$ket ‘to grunt'; Br. ürcha, id. Basque artz “bear? may be pre-IE.)
=== SYN bear
999:(12.31), ultimately connected with the preceding group *keubh-, etc., above. Walde-P. 1.371. Hence also NHG hiigel ‘hill’, by blend with MHG hibel. In the same group Dan. hoj ‘hill’ : hoj ‘high’, like NHG héhe, NE height fr. the respec- tive adj. forms.
21766:8. Skt. guh- (8sg. pres. giuhati), Av. | P. 1.566 f. 12.31 HIGH
21825:Fr. haut ‘high’ (12.31), used also as sb. for ‘top’.
22525:12.58. ‘Tall’, The sense of NE tall sed of persons, animals, trees, build- ‘oz etc.), that is, ‘of considerable watt vertically long’, is most com- moaly covered by the usual words for ‘high’ (12.31), but in part, esp. with ref=
22734:Lat, aline oh: lat, a high’ (12.31) also ‘deep’. undus (> It, profondo, Fr.
4962:I x Goth. Lith. lokys, mekka NG’ dnote ON Bjorn Lett.  lacis Lat. ursus Dan. bdjérn ChSl. medvédt It. orso Sw. bjérn SCr.  medujed Fr. ours OE bera Boh. medvéd Sp. oso ME bere Pol.  niedéwiedé Rum. urs NE bear Russ. medved Ir. art, mathgamain Du. beer Skt. rksa- Nir. mathghamhaim OHG bero Ay. arsa- W. arth MHG ber Br. ourz NHG bar
4964:Grk. apxros, NG pop. dpxotda; Lat. ursus, whence the Romance forms, also Corn. ors, MBr. urs (Br. ourz = Fr.); Ir. art, W. arth (Pedersen 1.89); Skt. rksa-, Av. arga-.
11304:ON purka : purka ‘wipe off’, Goth. paursus ‘dry’.
17486:3. Lat. currere (> It. correre, Fr. courir, Sp. correr) : cursus ‘course’, cur- rus ‘wagon’, Gallic carrus, Ir. carr, Br, karr ‘vehicle, wagon’, further connec- tions (as with OE hors ‘horse’, etc.) dub. Walde-P. 1.428. Ernout-M. 247f. Walde-H. 1.315 f.
27220:15.84 DRY Grk, Enpbs, ad i NG y aos Goth. paursus Lith. sausas Lat, fenés, oreyvbs ON purr Lett. sauss I, “us, Gridus Dan. gr ChSl.  suchit th tea, ascrutto (arido) Sw. torr SCr. suh Sp, Ee (aride) OE = drgge, pyrre, séar Boh.  suchy Rum, et Budo ME  drie, sere Pol. —suchy Ir, peal Sec NE dry Russ. suchoj Nir, tintin Du. droog Skt.  cuska- uf na. OHG — durri, trucchan Av. huSka-, hiku-, hiSku- Br, Bech, rg MHG _ trucken, dtirre
```


## [2026-09-14T01:27:23.063Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== IEC 3831 context\"\npython3 - <<'EOF'\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nprint('\\n'.join(lines[3824:3836]))\noff=sum(len(l)+1 for l in lines[:3830])\nleaf=t[:off].count('\\f'); print('LEAF',leaf,'pp',(leaf-15)*2,(leaf-15)*2+1)\nEOF\necho \"=== NYB 4270-4295\"\nsed -n '4270,4295p' NYB_vol2_glossary.txt\necho \"=== SYN leaf for 4962\"\npython3 - <<'EOF'\nt=open('SYN.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\noff=sum(len(l)+1 for l in lines[:4961])\nleaf=t[:off].count('\\f'); print('LEAF',leaf,'p',leaf-24)\nprint('\\n'.join(lines[4955:4970]))\nEOF",
 "description": "Print Mann, Nyberg, Buck contexts"
}
```


### [2026-09-14T01:27:24.343Z] TOOL RESULT

```
=== IEC 3831 context
25
30
35
40
45
260
Gk. árktos, (hapax) árx; Alb. arí, gs. aríu, f: arushé; Lat. ursus; Gaul. arto-; W arth; Cor. ors (sic); Br. -arz (in kraban-arz 'bear's breech’); Li. irstva ‘bears den (The name is based on the bear's grunt, cf. Li. urksti, Latv. urk$ket ‘to grunt'; Br. ürcha, id. Basque artz “bear? may be pre-IE.)
ormos (rmos, us) “arm, shoulder, extension, branch'. WP I, 73. Cf. armn- Skt. irmáh; Av. aromo; Oss. arm, pl. àrmttà “hand” beside ràmbín ‘elbow’; Arm. dim. type armukn Celbow. forearm’, fr. *ormuko-, or *armuko-); Go. Let arms; OHG arm; OE earm; ON armr; Lat. armus, m. o-st. 'shoul- der, arm’ beside ramus, n. o-st. “branch, arm of sea; OCS rame, gs. ramene, Srb. ràme ‘shoulder’; OPr. irmo “arm; Li. cf. irmos, f. pl. ‘stays, bars, crosspieces'
ornu-mi, see arnu-
ornd-à, see rndos, à
oró (oràio) “cry out, pray’. Cf. or- Gk. aráomai; Rom, oràť, id.
(aród-, see Suppt. orod-)
LEAF 156 pp 282 283
=== NYB 4270-4295
xäk [h'k] dust 1123, = NP.
xakan [h’k’n'] the Turkish title of the King 17°. 11323, 1151-24, - V, Barthold in EI s. v. Khäkän.
xünak [h’nk'; BYT^] house 92%. 101, 205 (ideogr.). 3671. 44?3, 5320.25, 10915. — NP ranah.
xanditan [hndytn'; YHDHWN-tn'] to laugh 1513, 162? (ideogr.). 4715-22, 5115-16, — MPrth znd?dn (S); NP zandidan.
xar [HMR] donkey 2415. 303. — Av. (532) zara-; NP zar.
xüyak [h'dk'] egg 863-7. 922, — Av. aya- < *dya- Yt. 13?, v. Henning, Weller Vol. 1954, 291; NP zäyah (now ‘testicle’).
218
xirs
viyift or vihift, abstr. vihifiakéh ‘sodomy’ BdA p. 2078, pres. *vidēp- > viyép- > vihep- with the alternation of intervocalic -y-: -h-. This vb. has a so well defined Ablaut-series and ends so clearly in -p that it cannot be combined with Av. (670 sq.) !dab- ‘to deceive’ (against Ver- bum, l. e.). — Anklesaria's second MS has wdyptk w wyhypynytk = viyiftak u vihe- penitak = Paz. vehéfta u vehevnida, thus with two coordinated predicates (against Cod. K) as the Av. text has it, but not with the Av. vbs.
Vizak [Paz.] one of Zartuxšt's ancestors 473,
vizand [wznd] injury, damage 214. 1174. 3713 ete. — MPrthPrs wzynd, NP guzand. vizand-kar [-kl] causing injury, destruc- tion, destroyer 11013-14,
vizand-kar [-k’]] whose work is injury, harmful (pat) 144.
Vizarš [wyzlš] a dev, who pulls the soul of the wicked to Hell after his death 7421.24 752, — Av. (1471) Vizarasa- Vd. 1926,
| xäyak-dös [-dys] egg-shaped 862-3. — V.
S. v. des.
xem [hym] nature, disposition, temper 9018.19.23. v. also vat-xēm. — Cf Av. (1781) haya-, hya- ‘peculiarity’; hence Olr *haiman- or the like. Paz. NP xim.
Xion [hywn'] Turkish peoples in Central Asia and East Iran, pl. cas. obl. ~-dn, 18-30 passim. 613-22. — Av. (1858) hyao- na-; Paz. hayün Skr. v. turuska-samüha (Aog.); cf NP hayün a dromedary used by express messengers; Chin Hiung-nu = Huns.
*xirs [hls] "a ring, or the like: 20%. — Both reading and meaning are guite un- certain. Arab has virs-, xurg- ‘a ring
www.parsianjoman.org | ool wok
. xirs
running round the lowest part of the lanee', also other sorts of rings, or 'coat of mail’, which is possibly a lw.; but this is à mere guess.
Xösröi [hwslwd; hwslwd' 110!5 M, but hwslwd Cod. K 43b] n. pr. A. the 3d king of the Kayanian dynasty, mostly known as Kai-Xösröi [kdhwslwd, -Iwd'] 7133. 1138-17; with the patron. Siydvaxsan 116’; eschatological hero 887°. 99—100 passim. 1065; — ~ i Kavätän, founder of five cities 114? sqq., is probably the old Kayanian king of the heroic saga. — B. the Sassanid kings from Bahram I (273— 276) onwards assumed the title ka? (g.v.) and regarded themselves as Kayanians: Kai-Kavät (488—531), his son im bag Xösröi šāhān šah i Kavätän (531-579) 10921, known as anösak-ruvän 118%; on Baxt-— v. this w. — Gr Xoopöns, NP Xusrav; Av. (1738) žhaosravah-. The spell- ings are: 1. on coins: hwslwd, hwslwdy (already Prth); hwslwy (predominant un- der Khosroes II 590-628); once hwslw? and once hwslwty (!) v. Paruck 380- 384. 386-390; Hansen, Catrang 18-19; — 2. in the inseriptions: KZSPrth hwsrw, Gr. v. Xootew, Prs hwslwb, which is also the spelling in three of the cities mention- ed 1141? sqq., certainly to be pronounced Xūsrūv = Arm Xosrov (but Syr Kösrö). In my opinion the BP form hwslwb' re- presents in reality hwslwdy, -b- being, as often at the end of the w., the cursive form of the letter d as written in the Ps.
Xösröi-mustäpät [hwsrwd mwst’p’t] the name of a town, otherwise unknown, in the W. quarter of Iran 114%, v. Cat. 58 sq.—‘Kh.’s merry settlement’: āpāt v. āpātān; must < musta-, pt. of Olr *maud-, Skr modate ‘to be delighted’, whence Av. (1109) maoóano.kara- ‘affording sensual pleasure’, (280) a-hömusta- < *ham- musta- ‘delighted’.
xrafstr [hlpstl] Ahrimanic, noxious ani- mals 76%, — Borrowed from Av. (538) arafstra-.
219
xUahišn
=== SYN leaf for 4962
LEAF 221 p 197
an ae y aseries of borrowings, | Lith. levas, while Lett. lauva is fr. MLG toy, which hers of Lat. led, to Grk. | louwe. Walde-H. 1.785. ee econ itself aloanword | 2. Lith. liatas, fr. Russ. Ujutyj opment of fees Source. The devel- | ‘fierce’. Berneker 756, 759. lewo, NHG lowe Scsee forms, as OHG 3. Skt. sitha-, without outside con- Scure, Fro an. lve), is ob- | nection unless Arm. inj ‘leopard’.
™ such come the Slavic forms
Walde-P. 2.508.
C-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
186 SELECTED INDO-EUROPEAN SYNONYMS 3.73 BEAR
I x Goth. Lith. lokys, mekka NG’ dnote ON Bjorn Lett.  lacis Lat. ursus Dan. bdjérn ChSl. medvédt It. orso Sw. bjérn SCr.  medujed Fr. ours OE bera Boh. medvéd Sp. oso ME bere Pol.  niedéwiedé Rum. urs NE bear Russ. medved Ir. art, mathgamain Du. beer Skt. rksa- Nir. mathghamhaim OHG bero Ay. arsa- W. arth MHG ber Br. ourz NHG bar
1. IE *rk40-, possibly as the ‘destroy- er’ (of beehives): Skt. raksas- ‘harm, in- jury.’ Walde-P. 1.322. Benveniste, BSL 38.141.
Grk. apxros, NG pop. dpxotda; Lat. ursus, whence the Romance forms, also Corn. ors, MBr. urs (Br. ourz = Fr.); Ir. art, W. arth (Pedersen 1.89); Skt. rksa-, Av. arga-.
2. Ir. mathgamain, NIr. mathghamh- ain, cpd. of gamain ‘calf’, first part fr. old math ‘bear’ (RIA Contrib. s.v.), perh. : maith ‘good’ as a euphemistic term. Stokes 199.
3. ON bjorn, OF bera, OHG bero, etc.,
the general Gmc. word : Lith. béras ‘brown’, OE Obriin ‘brown’, ete. Walde-P. 1.166. Falk-Torp 77.
4, Lith. lokys, Lett. ldcis, OPruss, clokis, all fr. *tlakis, this perh. as ‘hairy, shaggy’ : SCr. dlaka ‘hair’. Briickner, KZ 46, 207. Miuhl.-Endz. 2.434. Other- wise Meillet, Ling. hist. 284.
Lith. megka fr. a Slavic (ORuss. mesi- ka, Pol. Mieszka) pop. abbr. of the fol- lowing. Berneker 2.30. Briickner 335.
5. ChSl. medvédt, etc., all the Slavic words, lit. ‘honey-eater’, epd. of medi ‘honey’ and éd- ‘eat’. Berneker 2.30.
```


## [2026-09-14T01:27:37.503Z] TOOL CALL #35: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-14T01:27:37.512Z] TOOL RESULT

```


```


## [2026-09-14T01:27:41.574Z] TOOL CALL #36: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82%C5%95t%E1%B8%B1os",
 "prompt": "Give the reconstructed PIE root/noun for 'bear', its descendants (Proto-Indo-Iranian, Avestan, Greek, Latin, Celtic/Welsh), and any notes on the taboo/irregular forms."
}
```


### [2026-09-14T01:27:42.895Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-14T01:27:43.174Z] TOOL CALL #37: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AE%D8%B1%D8%B3",
 "prompt": "Persian خرس: give the full etymology — Middle Persian form, Proto-Iranian, PIE, cognates, and any note on the initial x-."
}
```


### [2026-09-14T01:27:49.011Z] TOOL RESULT

```
# Persian خرس Etymology

**Modern Persian form:** خرس (xirs/xers)

**Etymology chain:**

The word descends from "Old Persian *r̥šah, from Proto-Iranian *Hŕ̥šah, from Proto-Indo-Iranian *Hŕ̥ćšas, ultimately from Proto-Indo-European *h₂ŕ̥tḱos."

**Cognates across Indo-European languages:**
- Armenian արջ (arǰ)
- Greek άρκτος (árktos)
- Latin ursus
- French ours
- Sanskrit ऋक्ष (ṛkṣá)
- Welsh arth

**Note on initial x-:**
The source indicates "the x- in the beginning is debated, but may be an indication that it was borrowed from an Iranian language that preserved reflexes of laryngeals for longer."

The entry notes that Middle Persian forms are not explicitly provided in the available documentation, though the word's continuity from Old Persian through Classical Persian to modern dialects (Dari, Iranian, Tajik) is demonstrated through pronunciation variations.
```


## [2026-09-14T01:27:53.686Z] TOOL CALL #38: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CE%AC%CF%81%CE%BA%CF%84%CE%BF%CF%82",
 "prompt": "Ancient Greek ἄρκτος: etymology (PIE root), meanings including 'bear' and the constellation / north, and derived adjective ἀρκτικός. Also any Latin borrowing."
}
```


## [2026-09-14T01:27:54.929Z] TOOL CALL #39: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/arctic",
 "prompt": "Give the full etymology of 'arctic': Old French, Latin arcticus, Greek arktikos, arktos, PIE root."
}
```


### [2026-09-14T01:27:58.304Z] TOOL RESULT

```
# άρκτος - Greek Word for Bear

**άρκτος** (árktos) is a formal Modern Greek noun meaning "bear." It's a learned borrowing from Ancient Greek ἄρκτος.

## Key Details

**Part of speech:** Feminine noun

**Pronunciation:** /ˈaɾ.ktos/

**Definition:** The entry indicates this term means "bear" and is marked as formal usage. More colloquial alternatives include αρκούδα (arkoúda) and αρκούδι (arkoúdi).

## Related Words

The word connects to several related terms:
- αρκτικός (arktikós) - meaning "arctic"
- Μεγάλη Άρκτος (Megáli Árktos) - "Ursa Major" or "Great Bear" constellation
- Μικρή Άρκτος (Mikrí Árktos) - "Ursa Minor" or "Little Bear" constellation

The etymology traces back to Ancient Greek origins, reflecting the historical linguistic continuity between ancient and modern Greek.
```


### [2026-09-14T01:28:00.747Z] TOOL RESULT

```
# Full Etymology of "Arctic"

The word "arctic" traces back through multiple language layers:

**Greek Origin:** From Greek *arktikos*, meaning "of the north," literally "of the (constellation) Bear," derived from *arktos* meaning "bear" and also "Ursa Major; the region of the north."

**Latin:** The Greek term passed into Latin as *arcticus*.

**Medieval Latin & Old French:** Medieval Latin *articus* entered Old French as *artique*, from which English adopted the word in the late 14c. as *artik*.

**Proto-Indo-European Root:** The ultimate source is PIE *\*rtko-*, "the usual Indo-European root for 'bear'," which also produced cognates in Avestan, Armenian, Albanian, Welsh, and Latin *ursus*.

**Historical Development:** The *-c-* spelling was "restored from 1550s." Originally referring to the heavens in Middle English, the term expanded in reference to Earth from the early 15c. as "northern" and from the 1660s as "cold, frigid." As a capitalized noun denoting "the northern polar regions," it appears from 1560s onward.
```


## [2026-09-14T01:28:05.904Z] TOOL CALL #40: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Arthur",
 "prompt": "Etymology of the name Arthur: competing derivations (Latin Artorius vs Celtic *artos 'bear' / Welsh arth), what modern scholarship says."
}
```


## [2026-09-14T01:28:07.761Z] TOOL CALL #41: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Miriam",
 "prompt": "Etymology of Miriam: Hebrew מִרְיָם Miryam, proposed origins (Egyptian mr 'love', Hebrew meri 'rebellion'), and what is considered uncertain. Also any mention of Aramaic Maryam, Greek Mariam/Maria, Arabic Maryam."
}
```


### [2026-09-14T01:28:11.421Z] TOOL RESULT

```
# Etymology of Arthur: Competing Theories

The Wiktionary entry presents multiple competing derivations for the name Arthur:

**Celtic Origin Theory:**
The primary explanation suggests Arthur derives from Middle Welsh *arth* meaning "bear," possibly combined with *ur* ("man"), yielding "bear-man." This aligns with the legendary king's name originating from Celtic languages.

**Latin Alternative:**
A secondary theory proposes a Latinized Romano-British origin through Latin *Artorius*, itself potentially deriving from Messapic-Illyrian roots related to Proto-Albanian *artsa* ("bear").

**Modern Scholarship Position:**
The entry indicates "probably from Middle Welsh *arth* ('bear')" as the favored explanation, while acknowledging that the Latin *Artorius* origin "is itself possibly of Etruscan origin, or more likely Messapic-Illyrian related to Proto-Albanian."

Rather than declaring a definitive winner, contemporary lexicography presents the Celtic bear-etymology as most probable while treating the Latin connection as a plausible alternative. Both theories ultimately converge on an animal-related semantic root, suggesting the name carried associations with strength and power regardless of its ultimate linguistic ancestry.
```


### [2026-09-14T01:28:13.907Z] TOOL RESULT

```
# Miriam: Etymology and Meaning

**Miriam** originates from Hebrew *מִרְיָם* (Miryam). According to Wiktionary, the name's etymology involves multiple proposed origins:

The primary explanation suggests it may derive from Aramaic *מרים* (Maryām), meaning "bitter," from the root **מר** (m-r). However, this etymology "has been debated for centuries."

Alternative theories propose the name could relate to "mutiny / rebellion / disobedience" from a different Hebrew root **מרי** (m-r-y).

## Usage Across Languages

The name appears in numerous languages with variations:
- English, German, Italian, Dutch, Danish, and Swedish: Miriam
- Czech, Portuguese, Norwegian, Faroese, Slovak: Miriam (with local pronunciation)
- Alternative forms include Mirjam (Scandinavian/Germanic), Miryam, and Myriam

## Biblical and Religious Significance

In English usage, Miriam primarily refers to Moses and Aaron's sister from the Old Testament, or alternatively, Mary, mother of Jesus, "chiefly in contexts emphasizing her historical or Jewish identity."

The name's evolution across languages demonstrates its deep roots in Semitic languages and widespread adoption in European linguistic traditions.
```


## [2026-09-14T01:28:16.873Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/Mary",
 "prompt": "Etymology of Mary: Latin Maria, Greek Mariam/Maria, Aramaic Maryam, Hebrew Miryam, and any statement about the meaning ('rebellion', Egyptian origin)."
}
```


## [2026-09-14T01:28:18.068Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/marijuana",
 "prompt": "Etymology of marijuana/marihuana: Mexican Spanish origin, relation (or not) to Maria Juana, and any alternative Nahuatl/other proposals."
}
```


### [2026-09-14T01:28:20.619Z] TOOL RESULT

```
# Etymology of Mary

The name Mary traces back through multiple languages: **Latin *Maria*, Greek *Mariam/Maria*, Aramaic *Maryam*, and Hebrew *Miryam*.* The Hebrew origin is associated with Mary, sister of Moses (Exodus 15).

## Meaning

The etymological sources suggest the name literally means "rebellion," though scholars note the original sense remains uncertain.

## Cultural Notes

The name gained prominence as the designation for Jesus's mother in Christian tradition. It later inspired various related terms, including the "Mary Jane" shoe style (1921) and the literary concept of "Mary Sue" (attested by 1992) describing an idealized fictional character.
```


### [2026-09-14T01:28:23.228Z] TOOL RESULT

```
# Etymology of Marijuana

Based on the Online Etymology Dictionary, here's what is known about marijuana's origin:

## Documented Etymology

The word entered English in 1918, altered by influence of the Spanish proper name *Maria Juana* ("Mary Jane"). It derives from the Mexican Spanish term *marihuana*, which "is of uncertain origin."

The source notes an earlier form, *mariguan*, appearing in 1894. However, the dictionary explicitly states: "As the plant was not native to Mexico, a native source for the word seems unlikely."

## What Remains Unknown

The etymology documentation does not propose alternative theories involving Nahuatl or other indigenous languages. The ultimate origin of the Mexican Spanish *marihuana* itself remains unresolved—the connection to *Maria Juana* appears to be a folk etymology or linguistic reanalysis rather than the true source.

The dictionary's cautious phrasing—acknowledging the origin is "uncertain" and that Mexican sources seem improbable—suggests linguistic scholars have not definitively traced the word's actual provenance, leaving open questions about its possible pre-Columbian or other linguistic roots.
```


## [2026-09-14T01:28:26.724Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Marvin",
 "prompt": "Etymology of the given name/surname Marvin — Welsh Merfyn, Old English Mærwine, etc. Is there any connection to Mary?"
}
```


## [2026-09-14T01:28:29.254Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%85%D8%B1%D9%8A%D9%85",
 "prompt": "Arabic مريم (Maryam) and Persian مریم: etymology — is it from Syriac/Aramaic Maryam and Hebrew Miryam, or from an Arabic root r-y-m? Give what the entry says, plus the Persian section (flower name, borrowing route)."
}
```


### [2026-09-14T01:28:31.213Z] TOOL RESULT

```
# Marvin Etymology Analysis

Based on the Wiktionary content provided, **there is no mentioned connection between Marvin and Mary**.

The etymology section states that Marvin derives from Welsh *Merfyn* ("Mervyn"), which comes from "*mêr* ('marrow') + *myn* ('eminent')." This Welsh origin is distinct from Mary, which has separate etymological roots.

The document does not reference Old English *Mærwine* or discuss any relationship to the name Mary. The etymology provided focuses exclusively on the Welsh components of the name's meaning.
```


### [2026-09-14T01:28:34.135Z] TOOL RESULT

```
# Etymology of مريم (Maryam)

Based on the Wiktionary entry provided, the Arabic word **مريم** (maryam) derives from Semitic languages, not from an Arabic root. The entry states: "From Aramaic and post-Biblical Hebrew מרים (Maryam), from Biblical Hebrew מִרְיָם (Miryám)."

This indicates a borrowing chain: Biblical Hebrew → Post-Biblical Hebrew/Aramaic → Arabic, tracing back to ancient Semitic origins rather than developing from an Arabic r-y-m root.

Unfortunately, **the Persian section is not included in the provided content**. The page shows links to Persian (مریم) and mentions it in the descendants section as "Classical Persian: مَرْیَم (maryam)," but the actual Persian entry's etymology, definitions, and information about flower meanings are not available in this excerpt.

To obtain details about Persian usage and any botanical meanings, you would need to visit the Persian Wiktionary entry directly.
```


## [2026-09-14T01:28:42.095Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%F0%8E%A0%F0%8E%BC%F0%8F%81%F0%8E%A0%F0%8E%B6",
 "prompt": "Old Persian 𐎠𐎼𐏁𐎠𐎶 (Aršāma): etymology and meaning — is it 'having a hero's strength' (arša 'hero/male') or 'bear's strength'? Give descendants (Greek Arsames, Persian آرشام)."
}
```


## [2026-09-14T01:28:42.665Z] TOOL CALL #47: WebSearch

```json
{
 "query": "Aršāma Arsames etymology \"arša\" hero strength Schmitt Iranisches Personennamenbuch bear"
}
```


### [2026-09-14T01:28:43.262Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-14T01:28:49.066Z] TOOL RESULT

```
Web search results for query: "Aršāma Arsames etymology "arša" hero strength Schmitt Iranisches Personennamenbuch bear"

Links: [{"title":"Iranische Personennamen in der neuassyrischen Nebenüberlieferung - Rüdiger Schmitt - Google Books","url":"https://books.google.com/books/about/Iranisches_Personennamenbuch.html?id=fHuungEACAAJ"},{"title":"(PDF) SCHMITT, RÜDIGER: Iranisches Personennamenbuch, Band VII: Iranische Namen in semitischen Nebenüberlieferungen.","url":"https://www.researchgate.net/publication/323216967_SCHMITT_RUDIGER_Iranisches_Personennamenbuch_Band_VII_Iranische_Namen_in_semitischen_Nebenuberlieferungen"},{"title":"Iranische Namen (12 results)","url":"https://www.abebooks.com/book-search/title/iranische-namen/"},{"title":"Iranian Personal Names (IPNB)","url":"https://www.oeaw.ac.at/en/ifi/research/linguistics-onomastics/iranian-personal-names-ipnb"},{"title":"Arsames (disambiguation)","url":"https://en.wikipedia.org/wiki/Arsames_(disambiguation)"},{"title":"(PDF) Iranische Personnennamen in der neuassyrischen Nebenüberlieferung, by R. Schmitt","url":"https://www.academia.edu/9491181/Iranische_Personnennamen_in_der_neuassyrischen_Neben%C3%BCberlieferung_by_R_Schmitt"},{"title":"Arsaces","url":"https://en.wikipedia.org/wiki/Arsaces"},{"title":"Arsames (satrap of Egypt)","url":"https://en.wikipedia.org/wiki/Arsames_(satrap_of_Egypt)"},{"title":"Arsames","url":"https://en.wikipedia.org/wiki/Arsames"},{"title":"ARIYĀRAMNA - Encyclopaedia Iranica","url":"https://www.iranicaonline.org/articles/ariyaramna-greek-ariaramnes-old-persian-proper-name/"}]

Based on the search results, I found relevant information about the etymology of the name Arsames/Aršāma:

The Old Persian name Aršāma means "having a hero's strength", and the name is a compound, composed of aršan ("male, hero") and ama ("strength").

The Iranisches Personennamenbuch (IPNB) was established and developed since the 1970s by Manfred Mayrhofer, Rüdiger Schmitt and Heiner Eichner, and the articles in the IPNB have a standardized format including testimonies, prosopography and etymology.

The search results confirm that this etymology is well-documented in scholarly literature on Iranian personal names, though I did not find specific details about any reference to a "bear" element in the name's etymology in these particular results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-14T01:28:54.895Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://en.wikipedia.org/wiki/Arsames",
 "prompt": "Give the etymology of the Old Persian name Aršāma / Arsames as stated: the elements and meaning."
}
```


## [2026-09-14T01:28:57.252Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON part2 مریم\"\ngrep -n \"مریم\" MON_part2.txt | head -5\ngrep -n \"مريم\" MON_part1.txt MON_part2.txt | head -5\necho \"=== ARY khers\"\ngrep -n \"خرس\" incoming/ARY/ARY_pages.txt | head -10",
 "description": "Grep Mo'in and Aryanpur"
}
```


### [2026-09-14T01:28:57.349Z] TOOL RESULT

```
=== MON part2 مریم
5028:حشیشه المریم» شای بیت‌المقدس. 
11556:آسمان. . قدح مریم؛ : (گیا ) گیاهی است دوایی 
23906:عطابخش. کف مریم: (گیا.) گیاهی است از 
23912:است و آن را بنام پنجه مریم نیز می‌نامند؛ 
23915:کف مریم حجاری» اصابع الصفر. شحجرة 
=== ARY khers
295:داشتند. واژه‌های همریشه‌ی «خرس» و «گرگث» و دقازه و «راش» (882614) و «غان» (81071) و
2670:سانسکریت (8۸587): تیه پسگشت‌ها خرس ۱
4295:۱ دا پسگشت‌ها خرس
13050:فریزی کهن (/(۲۸354 ام 01878۸ پسگشت‌ها خرس
```


### [2026-09-14T01:28:57.856Z] TOOL RESULT

```
# Etymology of Arsames

According to the Wikipedia article, the Old Persian name Aršāma translates to **"having a hero's strength."** 

The article states: "His name (_Aršāma_) translates to 'having a hero's strength'." This indicates the name combines elements referring to heroic qualities with the concept of physical or personal power.
```


## [2026-09-14T01:29:03.011Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY\npython3 - <<'EOF'\nimport re\nt=open('ARY_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if p.count('خرس')>=2:\n        print('=== leaf',i, re.search(r'\\[pdf page (\\d+)\\]',p).group(0) if re.search(r'\\[pdf page (\\d+)\\]',p) else '')\n        print(p[:1800])\nEOF",
 "description": "Find Aryanpur khers entry"
}
```


### [2026-09-14T01:29:03.963Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T01:29:07.815Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY\npython3 - <<'EOF'\nimport re\nt=open('ARY_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('leaves',len(pages))\nfor i,p in enumerate(pages):\n    if 'خرس' in p:\n        m=re.search(r'\\[pdf page (\\d+)\\]',p)\n        print('leaf',i, m.group(0) if m else '')\n        idx=p.find('خرس')\n        print(repr(p[max(0,idx-400):idx+400]))\n        print('---')\nEOF",
 "description": "Aryanpur khers contexts"
}
```


### [2026-09-14T01:29:08.901Z] TOOL RESULT

```
leaves 545
leaf 11 [pdf page 12]
'هند و اروپایی\nهمریشه\u200cاند می\u200cتوان نتیجه گرفت که آنان در رام کردن اسب و استفاده از ترابرهای چرخدار پیشگام\nبوده\u200cاند و تحرکك و تفوقی که سوارکاری و ترابری به آنها داده عامل بزرگی در گسترش آنها بوده\nاست. واژه\u200cهای همریشه\u200cی دیگر نیز در شناخت ماهیت هند و اروپائیان سودمنداند: واژه\u200cهای مشترک\n«شخم» و «آهن) و «جوه و «گاوه و «بز» و «خوکک» نشان می\u200cدهد که این مردم به کشاورزی هم اشتغال"\nداشتند. واژه\u200cهای همریشه\u200cی «خرس» و «گرگث» و دقازه و «راش» (882614) و «غان» (81071) و\n«ماهی آزان (5۸14۸/1030) و «ییده (/۷11-1-07) و «بلوط» (0۸74) و «زنبور؛ (81312) و «اردکث»\n(01700) نشان می\u200cدهد که خاستگاه این مردم در یک ناحیه نسبتاً سردسیر بود. چون اگر مثلاً\n\nپپی ..خاستگاه آنها در ناحیه\u200cی گرسیر با استوایی بود واژه\u200cهای همریشه\u200cی آنها وابسته بهگیاهان و جانوران\nگزمسیری می\u200cبود در حالیکه تفریباً همه\u200cی واژه\u200cهای گرمسیری و استوایی از '
---
leaf 91 [pdf page 92]
': ۰ 181(۷) سم لاه\nایرلندی کهن (تا5ل] صا0): 1۳005۸ 6 00 :0/05\n0 4 (۲۵۷) :7\nهنبت (4/77772): ولا\n1 (۸0۷) اکن دنام\nبرهان قاطع + ۵ و ۱۷۱۴و ۲۲۰۶\nیادداشت:\nچم این واژه در زبان افغانی يا پشتو: امروز.\nچم این واژه در زبان تخاری ۸ و هتیت: سپس. ۱\nپارسی باستان (۶8۴۶/4۷ 7:)0-0 ۸۸/۳۳۳۸ گوتیکد (007[712): ناه سا\nپهلری (7اتقمه): ۱۱ هتیت (7177775(). نا 1\nتخاری ۸ (۸ لفق 7087۸): ۰ 2.0۸15\nسانسکریت (8۸587): تیه پسگشت\u200cها خرس ۱\nارمنی (42ا۸/87): ۲ یناشن 9 (11037) هام08\nیونانی 08570): 05 8 مان ها\n1 الاتین 702 ما): ۰۹۸۵۲۵8 ۰ |45 دم\nَ شا 9\nیادداشت:\nبازگشت به آمرگد".\nسا را\n'
---
leaf 146 [pdf page 147]
': 58 ,80115 هلندی (1ع007): ۷07\nلانین (7100مل): 85 ,55 اسلاوی کهن (16 مرو 07ات0 طلم):\nفرائسه (4ل0/ق73): 0 ی مک ۳\nاسپانیایی (8۳۸۸13): ادا لینرانی (۵2ا(هل17 7 ): \u200e0٩\u200f\n\u200fایتالیایی (۷لشاله7): رانا تونی (لتی) (/7۲14۸): ۳0۸\nرومانی (/(۸/۸(۵): 3 ایرلندی کهن (للدل#ز صا0): 3\nپرتغالی (۳077012285): 2 آلبانی (4/۷مقلم): ۳07\nگونیکه (0077710): 108 هتیت (717717): ۷ ۳۸7۸\nآیسلندی کهن (نف 70/۸7 شک طا0).\n\n۱ دا پسگشت\u200cها خرس\n\nنورس کهن (۸0۸۵2 0): 078 0 2080820\nساکسونی کهن (540000 010): 137 ,007 8 (۳۵0۵7) تا ما ان\nفریزی کهن (51(۷ل۲# صا0): ۴۸07 7 (۳180) بان ۱۰۳ او\nآلمانی کهن (0270142 ۲1067 صا0): ,7107 5 (۲007) دام ی\nآلمانی ((4۸ل057): ناد 23244 8۸\nانگلیسی کهن (تلدلا8(0 صا0): ۳/07 8 (۲007) :05\nانگلیسی (5ا.ا6۸/0): 007 0 (۲۵0۵7) +547\nدانمارکی (0۸(//54): 00 برهان قاطع + ۱ ۳۳۴\nسرئدی (8175015/7): 07\n\nیادداشت.\n\nمعنی این واژه'
---
leaf 438 [pdf page 439]
'[pdf page 439]\n۹ 95\n: ۰ | گلو ۱\nفریزی کهن (/(۲۸354 ام 01878۸ پسگشت\u200cها خرس\nآلماتی کهن ((08704۸ ۶0 صا): 0 ۶00120\n۸1 ,010875۳3۸۵ 8 (000711) :۵ ی من\n: انگلیسی کهن (54ا20/0 صا0): 9و ههام ی اما\n7 بافشتا 0۴1 1 (8۸) :5 ۲02/2 ۳۰۱*۱۲۸\nدانمارکی (0۸۸/574): امه 1257 اه\n۱ سرئدی (5050157): 0۸ 4 (01071) ۰" 005\n: نروژی (08014(7/): ۸08 4 (07ن0) 57\n: 39 :7\n, برهان قاطع + ۸۳۱\nیادداشت,\n۱ رابطه\u200cی این واژه\u200cهای ایرانی با دیگر واژه\u200cهای این فهرست احتمالی است و پهمین غلت جلر واجریشه\u200cی هند و\n۱'
---
```


## [2026-09-14T01:29:29.153Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AFA Maryam\"\ngrep -n -i \"Maryam\\|Mirjam\\|Marjam\" AFA.txt | head -10\necho \"=== TAD\"\ngrep -n \"مريم\" TAD.txt | head -5\necho \"=== AFM\"\ngrep -n \"مريم\" AFM.txt | head -5\necho \"=== SKT arctic/Arthur\"\ngrep -n -i \"^Arctic\\|Arctic,\" SKT.txt | head -5\necho \"=== FSD marijuana/Marvin\"\ngrep -n -i \"marihuana\" FSD_vol3.txt | head -3",
 "description": "Grep Fraenkel, Skeat etc."
}
```


### [2026-09-14T01:29:29.268Z] TOOL RESULT

```
=== AFA Maryam
=== TAD
=== AFM
=== SKT arctic/Arthur
=== FSD marijuana/Marvin
```


## [2026-09-14T01:29:33.138Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SKT arctic\"\ngrep -n -i \"arctic\" SKT.txt | head -5\necho \"=== KLN arctic\"\ngrep -n \"^Arctic\\|^arctic\" KLN_1966.txt | head -5\necho \"=== FSD vol1 Arctic\"\ngrep -rn -i \"arktos\" FSD_vol1.txt | head -3\necho \"=== WEB arctic\"\ngrep -n -i \"arctic, a\\|Arctic\\b\" WEB_vol1.txt | head -3",
 "description": "Grep Skeat/Klein/Webster for arctic"
}
```


### [2026-09-14T01:29:33.254Z] TOOL RESULT

```
=== SKT arctic
747:Antarctic ;  see  Arotio.
=== KLN arctic
=== FSD vol1 Arctic
FSD_vol1.txt:24283:2.  Of  or  pertaining  to  either  of  the  constellations  called the  Great  Bear  and  the  Little  Bear.  [<  F.  arctique, <   LL.  arcticus,  <   Gr.  arktikos ,   <   arktos,  bear,  the  con- stellation.! —   arctic  circle,  the  imaginary  circle.  23°  2S' Trom  the  north  pole,  that  separates  the  north  temperate zone  from  the  north  frigid  zone.— a.  constellations,  con- stellations situated  about  the  north  celestial  pole.—  a.  cur- rent, a   current  which  flows  southward  from  the  arctic  seas. —   a.  fox,  see  under  rox.—  a.  grass  (Bot.),  same  as  rescue- grass.—  A.  ocean,  a   body  of  water,  surrounding  the  north pole,  open  to  the  Atlantic  and  Pacific  oceans  through  Baffin Bay  and  Bering  Strait.—  arc-tl'clan,  n.  One  familiar  with arctic  regions;  an  arctic  explorer  or  student  of  arctic  pecu- liarities.— arc'tl-clze,  rt.  To  acclimate  to  arctic  regions, arc'tl-clsef.—  arc'ttc-ward,  adv . arc'tlc1,  n.  1.  The  arctic  circle  or  regions;  as,  a   year  in the  arctic:  correlative  of  antarctic.  2.  [U.  S.]  A   warmly lined  water-proof  overshoe.  3.  [A-J  The  Eskimo  stock. Arc'tlc5,  n.  A   village  in  Kent  county,  R.  I.
FSD_vol1.txt:24316:Hist.  The  head  of  the  Roman  Catholic  secular  clergy,  animalcules  (Macrobiotife) .   «   Gr.  arktos,  bear.]  —   arc-
FSD_vol1.txt:24318:was  changed  to  ricar  apostolic.  (<  OF.  archepreslre,  Avc'RIs-con'I-dae,  1   ark'tls-kon'i-dl;  2   5rc*tIs-c5n'I-d6,  rt.pl. <   LL.  archipresbyter.  <   Gr.  archipresbyteros ;   see  arch-  Arach.  A   family  of  acarldans  with  4   pairs  of  3-Jointed  legs and  priest  j—  arcbf,prlest'hood,arch"priest'shIp,n.  and  without  caudal  appendages.  Arc-tIsrcon,  n.  (t.  g.) The  dignity  or  office  or  an  archpriest.  f   <   gr.  arktos,  bear.]  -   arc-tls'co-nfd,  a.  &   n.-  arc-tls'co-
=== WEB arctic
8342:ant-ire’tic, a. [anti-, and Gr. arktos, the Bear, a northern constellation.] opposite to the northern or arctic pole; relating to the South Pole or to the region near it; as, the Antarctic Circle, the Axlarclic Ocean, etc.
8343:Antarctic Circle; an imaginary circle parallel to the equator, 23° 30’ from the South Pole: also written antarctic circle.
8344:Antarctic Zone; all of the region south of the Antarctic Circle.
```


## [2026-09-14T01:29:44.949Z] TOOL CALL #54: Bash

```json
{
 "command": "timeout 300 python3 tools/ref_page.py BQT:31 --image 2>&1 | tail -40",
 "description": "Render Borhan page 31"
}
```


### [2026-09-14T01:29:46.076Z] TOOL RESULT

```
no scan of BQT covers printed page 31 (see 'scans' in refs_online.json)
```


## [2026-09-14T01:29:52.362Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor f in BQT_alt_v1.txt BQT_dli_part1.txt BQT_v1.txt; do echo \"=== $f\"; grep -c \"آرشام\\|ارشام\" $f; grep -n \"آرشام\\|ارشام\" $f | head -5; done",
 "description": "Search other BQT v1 OCRs for Arsham"
}
```


### [2026-09-14T01:29:53.553Z] TOOL RESULT

```
=== BQT_alt_v1.txt
4
257:نیای دار یوش است‌وارشامه پسراوست. داریوش درسنگنيشتة بفستان (یستون) 
263:باریارمته وارشامه از شپریاران‌فارس بازخو انده‌شود » ایرادی ثیست‌جزاینکه 
11847:۵ آرشام - ۸۵1512210 تام جد داربوش بز رکه شاهنشاه هضامنشی, مر کب از 2۳5۳2 
12032:آریا راهت* _ ۸۳۷2۳2۳00۵ نامجد داربوش بز رکه پدر آرشام» کب از260۷9 
=== BQT_dli_part1.txt
0
=== BQT_v1.txt
3
371:نوشته ایست نبنام‌ار بارمنه ۸۲۱۷۵۳۵۱۷۲۱۵ ودیگری نام ارشامه‌و ۳۵9 ۸ 
373:نیای دار یوش‌است‌وارشامه پسراوست. داریوش درسنکتيشتة بفستان (بیستون) 
379:باریارمته وارشامه از شهریاران‌فارس بازخو انده‌شود » ایرادی نیست‌جز اینکه
```


## [2026-09-14T01:29:58.991Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '11835,11860p' BQT_alt_v1.txt\necho \"=== which page? count pages\"\npython3 - <<'EOF'\nt=open('BQT_alt_v1.txt',encoding='utf-8',errors='replace').read()\ni=t.find('آرشام - ')\nprint('leaf',t[:i].count('\\f'),'of',t.count('\\f'))\nEOF",
 "description": "Print Borhan Arsham footnote"
}
```


### [2026-09-14T01:30:01.143Z] TOOL RESULT

```
۸ -معتی اخیر در فرهننگ دساتیی ( رك : می۲۳۰ ) آمده است 


۵ آرذف ‏ پهلوی 2۳261 < 
مراد - ممشوق » محیوب : 


یی ر ۲۸۱ » با 272016 «اونوالا ۲4۵»؛ کام» خواعش» 


۵ آرستی ‏ توانتن » بارستن » جرأت » دلیری کردن . 
۵ آرشام - ۸۵1512210 تام جد داربوش بز رکه شاهنشاه هضامنشی, مر کب از 2۳5۳2 


پبجنی‌خری و 8102 بمعنی زورء جمعاً خری نو » دارای زور خری. «بارتولمه ۲۰۶*. 


]دشی - یکی ات ورایم و سکون 
تحتانی , بمعنی معنوی باشد که در مفابل لفی 
است . چه آرش بمعتی «معئی» است ۷ . 

آدغ - بضم نالث و سکون غين نفطه 
دار » مخفف آروغ است » و آن بادی باشد که 
با صدا از کلو برمیآبد . 

=== which page? count pages
leaf 0 of 0
```


## [2026-09-14T01:30:30.454Z] TOOL CALL #57: WebSearch

```json
{
 "query": "wiktionary Reconstruction Proto-Indo-European h₂ŕ̥tḱos bear",
 "allowed_domains": [
  "en.wiktionary.org"
 ]
}
```


### [2026-09-14T01:30:34.797Z] TOOL RESULT

```
Web search results for query: "wiktionary Reconstruction Proto-Indo-European h₂ŕ̥tḱos bear"

Links: [{"title":"Reconstruction:Proto-Indo-European/h₂ŕ̥tḱos - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82%C5%95%CC%A5t%E1%B8%B1os"},{"title":"Reconstruction:Proto-Anatolian/Hŕ̥tḱos - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Reconstruction:Proto-Anatolian/H%C5%95%CC%A5t%E1%B8%B1os"},{"title":"Reconstruction:Proto-Indo-European/wĺ̥kʷos - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/w%C4%BA%CC%A5k%CA%B7os"},{"title":"ἄρκτος - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%E1%BC%84%CF%81%CE%BA%CF%84%CE%BF%CF%82"},{"title":"Reconstruction:Proto-Celtic/artos - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Reconstruction:Proto-Celtic/artos"},{"title":"Reconstruction:Proto-Indo-Iranian/Hŕ̥ćšas - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/H%C5%95%CC%A5%C4%87%C5%A1as"},{"title":"Reconstruction:Proto-Balto-Slavic/irśtwā́ˀ - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Reconstruction:Proto-Balto-Slavic/ir%C5%9Btw%C4%81%CC%81%CB%80"},{"title":"bear - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/bear"},{"title":"Reconstruction:Proto-Indo-European/tl̥h₂tós - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/tl%CC%A5h%E2%82%82t%C3%B3s"},{"title":"Reconstruction:Proto-Italic/orssos - Wiktionary","url":"https://en.wiktionary.org/wiki/Reconstruction:Proto-Italic/orssos"}]

The search results show that *h₂ŕ̥tḱos is the Proto-Indo-European word for "bear". 

Cognates include Latin ursus, Welsh arth, Sanskrit ऋक्ष (ṛ́kṣa), Old Armenian արջ (arǰ), and Albanian ari. The Wiktionary entry demonstrates how this Proto-Indo-European root evolved across different language families and descended languages throughout history.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-14T01:30:38.285Z] TOOL CALL #58: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82%C5%95%CC%A5t%E1%B8%B1os",
 "prompt": "Give the PIE noun *h₂ŕ̥tḱos 'bear': its descendants in Proto-Indo-Iranian, Avestan, Greek, Latin, Proto-Celtic, Hittite; any note on irregularity or taboo deformation."
}
```


## [2026-09-14T01:30:39.502Z] TOOL CALL #59: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Celtic/artos",
 "prompt": "Proto-Celtic *artos 'bear': descendants (Old Irish art, Welsh arth, Gaulish Artio), and any mention of the name Arthur."
}
```


### [2026-09-14T01:30:44.752Z] TOOL RESULT

```
# Proto-Celtic *artos and the Etymology of "Bear"

According to Wiktionary's reconstruction entry, **Proto-Celtic *artos** meant "bear" (the mammal). The term descended from Proto-Indo-European *h₂ŕ̥tḱos with the same meaning.

## Linguistic Descendants

The word evolved across Celtic language branches:

- **Brythonic branch**: Welsh *arth*, Cornish *arth*, Breton *arzh*
- **Goidelic branch**: Old Irish *art* (meaning "bear, hero, warrior")
- **Continental Celtic**: Gaulish *artos*, which influenced Latin place names and deity names like *Artio*

## Connection to Arthur

The page notes that Gaulish *artos* appears in Latin borrowings such as *Artiō* and *Artodunum*. This linguistic lineage suggests the name Arthur itself may derive from this Proto-Celtic root meaning "bear," though the entry doesn't explicitly discuss the name Arthur's origin.

Interestingly, the entry also lists Basque *hartz* ("bear") with a note that the connection remains "uncertain," indicating ongoing scholarly debate about cross-language borrowing patterns in ancient Europe.
```


### [2026-09-14T01:30:45.290Z] TOOL RESULT

```
# Proto-Indo-European *h₂ŕ̥tḱos (Bear)

## Definition
The reconstructed PIE noun means "bear" and is a masculine, non-ablauting thematic o-stem noun.

## Key Descendants

**Proto-Indo-Iranian:** *Hŕ̥ćšas (see that entry for further descendants)

**Avestan:** Shows related forms including *rašah* ("damage") and *rašaiieṇt* ("to damage"), reflecting an etymological connection to a root meaning "to harm"

**Greek:** Proto-Hellenic *árktos descendant into Ancient Greek *ἄρκτος* (árktos)

**Latin:** *ursus, possibly derived from earlier *orsos, though scholars note "outcome of -tḱ- in Italic uncertain"

**Proto-Celtic:** *artos (see that entry for further descendants)

**Hittite/Proto-Anatolian:** *Hŕ̥tḱos (see that entry for further descendants)

## Etymological Notes

The etymology remains uncertain. Scholars propose it may be "nominalized from root *h₂retḱ- ('to damage, harm')," connecting it to Sanskrit *rákṣas* meaning "damage, injury; demon."

## Irregularity Note

The Latin form possibly underwent "tabooistic distortion," a cultural practice of deliberately altering sacred or feared animal names.
```


## [2026-09-14T01:30:51.425Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n \"https://en.wiktionary.org/wiki/%D8%AE%D8%B1%D8%B3\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82%C5%95%CC%A5t%E1%B8%B1os\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Celtic/artos\" \\\n \"https://www.etymonline.com/word/arctic\" \\\n \"https://en.wiktionary.org/wiki/Arthur\" ; do\n timeout 120 python3 tools/fetch_source.py \"$u\" --note \"page 426, root Rk-tho 'bear': PIE/Persian/Greek/Celtic nodes\" 2>&1 | tail -2\ndone",
 "description": "Archive bear-root web sources"
}
```


### [2026-09-14T01:30:54.437Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/e18f4304de303128.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e802dc8d56f342eb.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b273d3b63732a34a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/395d587264701db6.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/eb2b50672ca35a7a.txt
```


## [2026-09-14T01:30:59.883Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n \"https://en.wikipedia.org/wiki/Arsames\" \\\n \"https://en.wiktionary.org/wiki/Miriam\" \\\n \"https://www.etymonline.com/word/Mary\" \\\n \"https://www.etymonline.com/word/marijuana\" \\\n \"https://en.wiktionary.org/wiki/Marvin\" \\\n \"https://en.wiktionary.org/wiki/%D9%85%D8%B1%D9%8A%D9%85\" \\\n \"https://en.wiktionary.org/wiki/%E1%BC%84%CF%81%CE%BA%CF%84%CE%BF%CF%82\" ; do\n timeout 120 python3 tools/fetch_source.py \"$u\" --note \"page 426, roots Rk-tho / R.y.m: Arsames, Miriam/Mary/Maryam, marijuana, Marvin, Greek arktos\" 2>&1 | tail -2\ndone",
 "description": "Archive Mary-entry web sources"
}
```


### [2026-09-14T01:31:03.692Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/e3882bc01aaf291e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/50ea92edbe3d88df.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0e3c5e1ebadb0167.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/82b9df1968e415dc.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9ddc153a5b2c8e62.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b6abc2972fc6386f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e8e56cd29f3097e2.txt
```


## [2026-09-14T01:31:09.566Z] TOOL CALL #62: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B1%D8%A7%D9%85",
 "prompt": "Arabic رام: is there a verb رَامَ (rāma), root ر ي م (r-y-m), meaning 'to leave, depart from a place'? Give the entry's Arabic verb senses and root."
}
```


## [2026-09-14T01:31:10.394Z] TOOL CALL #63: WebSearch

```json
{
 "query": "Syriac ܡܪܝܡ Maryam etymology Hebrew Miryam Syriac root rym depart"
}
```


### [2026-09-14T01:31:13.324Z] TOOL RESULT

```
# Arabic رام (rāma) - Root ر ي م

Yes, there is a verb رَامَ (rāma) with root ر ي م (r y m).

**Verb Sense:**
The entry indicates this verb means "to depart from, to separate oneself from" with accusative case construction.

**Root Information:**
The root ر ي م (r y m) is listed as Etymology 2, derived from Proto-Semitic *rayam-, which is "related to *rawam-"
```


### [2026-09-14T01:31:17.936Z] TOOL RESULT

```
Web search results for query: "Syriac ܡܪܝܡ Maryam etymology Hebrew Miryam Syriac root rym depart"

Links: [{"title":"ܡܪܝܡ - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%DC%A1%DC%AA%DC%9D%DC%A1"},{"title":"CATHOLIC ENCYCLOPEDIA: The Name of Mary","url":"https://www.newadvent.org/cathen/15464a.htm"},{"title":"Maryam (name)","url":"https://en.wikipedia.org/wiki/Maryam_(name)"},{"title":"Miriam - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Miriam"},{"title":"מרים - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D7%9E%D7%A8%D7%99%D7%9D"},{"title":"Miriam (given name)","url":"https://en.wikipedia.org/wiki/Miriam_(given_name)"},{"title":"All the Marys and Miriams in the Bible - Marg Mowczko","url":"https://margmowczko.com/miriam-maria-mary-meaning-bible/"},{"title":"Maryam (name) — Grokipedia","url":"https://grokipedia.com/page/Maryam_(name)"}]

Based on the search results, here's what I found about the etymology of Maryam/Miriam:

## Etymology Overview

Maryam is the Aramaic form of the biblical name Miriam, and in Aramaic, the name shifts to Maryam (ܡܪܝܡ in Syriac script).

## Proposed Etymologies

The exact origin of the name is uncertain, with multiple scholarly proposals:

1. **Bitterness root**: The name is possibly of uncertain origin but possibly related to a root related to bitterness; compare Classical Syriac ܡܪܝܪܐ (marrīrā, "bitter").

2. **Hebrew root alternatives**: Proposals include derivation from the root מ־ר־ר (m-r-r, "to be bitter"), or from the root מ־ר־י (m-r-y, "to mutiny, rebellion, disobedience"), or from Egyptian mry ("beloved").

3. **Egyptian origin**: It is possibly derivative of the root mr "love; beloved".

Notably, your query about "rym" meaning "depart" doesn't appear in these etymological sources—the most commonly discussed roots relate to bitterness, rebellion, or love rather than departure.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-14T01:31:26.198Z] TOOL CALL #64: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%85%D8%B1%DB%8C%D9%85",
 "prompt": "Persian مریم: etymology (borrowed from Arabic مريم? or from Syriac/Aramaic), and its meanings (Mary; tuberose flower)."
}
```


## [2026-09-14T01:31:29.266Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \"https://en.wiktionary.org/wiki/%D8%B1%D8%A7%D9%85\" \"https://en.wiktionary.org/wiki/%DC%A1%DC%AA%DC%9D%DC%A1\" \"https://en.wikipedia.org/wiki/Maryam_(name)\"; do\n timeout 120 python3 tools/fetch_source.py \"$u\" --note \"page 426, root R.y.m: Arabic root r-y-m 'to depart', Syriac Maryam, name Maryam\" 2>&1 | tail -1\ndone",
 "description": "Archive Syriac/Arabic sources"
}
```


### [2026-09-14T01:31:31.405Z] TOOL RESULT

```
# مریم (Maryam)

This Wiktionary entry documents a word used across Persian and Urdu, with related versions in seven languages.

## Etymology

The term originates from Semitic roots. It was "Borrowed from Arabic _مَرْيَم_ (maryam), from Aramaic _מרים_ (maryam)."

## Persian Usage

In Persian, مریم functions as a proper noun meaning:
1. Mary (the religious figure)
2. A female given name equivalent to English Mary

## Urdu Usage

The Urdu section presents broader applications:
- **Proper noun**: References to Mary (mother of Jesus) and the biblical Miriam
- **Common noun**: Used figuratively to describe "a virgin, maiden"

The entry includes declension tables showing singular and plural forms, along with derived terms and historical dictionary references from 19th-century sources.

This multilingual documentation reflects how a name of ancient Aramaic origin traveled through Arabic and Persian into South Asian languages, maintaining religious significance while also developing figurative meanings in some contexts.
```


### [2026-09-14T01:31:35.152Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/3b9457a2f281e5f6.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/68356e7660f1e96c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a51762a0b36c15fb.txt
```


## [2026-09-14T01:31:38.027Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\ntimeout 120 python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/%D9%85%D8%B1%DB%8C%D9%85\" --note \"page 426, root R.y.m node 2: Persian مریم borrowed from Arabic maryam < Aramaic\" 2>&1 | tail -1",
 "description": "Archive Persian Maryam page"
}
```


### [2026-09-14T01:31:39.466Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/453360573f594f8b.txt
```


## [2026-09-14T01:32:27.387Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '4300,4340p' HRN.txt | cat -n",
 "description": "Horn entry numbers near xirs"
}
```


### [2026-09-14T01:32:27.444Z] TOOL RESULT

```
     1	aw. /ara- 'Esel : phlv. /ar: skr. khara- 'Esel'.
     2	kurd. ier, liar (GuränT): SLfy./ar: oss. /ßräg, x^*'^9
     3	(2i)7); bei. n. ffar, /ar, LW. har^) (192); wa/. ;rwr,
     4	«ar. cer, üer, sangl. //tr, minj. xara.
     5	*j Vcrgl. Ilorn, ZDMG. 44, 675, No. 134.
     6	•; Vcrgl. Barthol oniao, ZDMG. 44, 550.— 105 —
     7	. y^erbuze, /erbtu^) *Melone' (wörtl. *Eselsgurke').
     8	phlv. /arböjhia, kharbuzak (PP61.), vergl. höjlna =
     9	/iyär (ebendas.) und bujpa (BQ.) d. i. bäjinä, htijina
    10	V
    11	(FS); die letzteren beiden neupersischen Worte sind
    12	nur Fehle vlumschriften, noch mit aramäischem -a.
    13	Vergl. NT2il2, de Lagarde, Semitica 56.
    14	Weit gewandert, vergl. türk. qarpuz etc.
    15	>. y^ereeuf/ *Krebs', vergl. kilinjar, kulenöek (Wo Ilaston:
    16	karanjäl, kalanjär).
    17	skr. vergl. karkiffa- 'Krebs, Krebs im Tierkreise'
    18	(karkä- etc. sind bedenklich) ; phlv. karcany 'Krebs im
    19	Tierkreise (Bund.); gr. -^nQy.lvo^ 'Krebs', vergl. md^j/ar
    20	yjumi'oi 2itY.t\oi , Hesych.; lat. Cancer wird ebenfalls
    21	dazu gehören (vergl. Brugmann, Grundriss, I, § 282
    22	Ende). / ist erst neupersisch.
    23	>. -/ired 'Verstand*.
    24	aw. /ratu- 'Verstand'; phlv. xrat, /j'attk[tum (vd.
    25	19 (47), arm. LW. /art)\ ai. krdtU",
    26	\ yiirs 'Bär.
    27	aw. aresa- *Bär (Aog.) ; phlv. xO)^^ (Bund.) ; ai. /ksa- ;
    28	arm. arj (H. No. 46).
    29	oss. d. t. a7's (85); siyn. ytir}, sar. yürx,
    30	Aw. Ere/sa-, vergl. ai. Ärksa- (Goldschmidt bei
    31	Nöldeke, ZDMG. 86, 447) sind hiervon zu trennen,
    32	vergl. Hübsch mann, ZDMG. 38, 429; anders Bar-
    33	tholomae, Studien II, 21.
    34	B. yftirsend ^fröhlich, zufrieden .
    35	aw. ^hurasant-; phlv. /ursand 'zufrieden, fröhlich*
    36	(Bund., Men.), /ursandih (AV.).
    37	Darmestete r. Et. ir. I, 265; die päz. Aussprache
    38	X'arsand spricht allerdings gegen diese Etymologie,
    39	doch kann sie nicht ausschlaggebend sein.
    40	'j Brugsch, Reise der K. Preuss. Gesandtschaft nach Persien
    41	: vermug Band und Seitenzahl augenblicklich nicht anzugeben) hat
```


## [2026-09-14T01:32:44.627Z] AGENT

Now I'll write the verification file.


## [2026-09-14T01:40:15.034Z] TOOL CALL #68: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-426.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW_KHERS   = \"https://en.wiktionary.org/wiki/%D8%AE%D8%B1%D8%B3\"\nW_PIE     = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82%C5%95%CC%A5t%E1%B8%B1os\"\nW_CELT    = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Celtic/artos\"\nE_ARCTIC  = \"https://www.etymonline.com/word/arctic\"\nW_ARTHUR  = \"https://en.wiktionary.org/wiki/Arthur\"\nWP_ARSAM  = \"https://en.wikipedia.org/wiki/Arsames\"\nW_MIRIAM  = \"https://en.wiktionary.org/wiki/Miriam\"\nE_MARY    = \"https://www.etymonline.com/word/Mary\"\nE_MARIJ   = \"https://www.etymonline.com/word/marijuana\"\nW_MARVIN  = \"https://en.wiktionary.org/wiki/Marvin\"\nW_MARYAM  = \"https://en.wiktionary.org/wiki/%D9%85%D8%B1%D9%8A%D9%85\"\nW_ARKTOS  = \"https://en.wiktionary.org/wiki/%E1%BC%84%CF%81%CE%BA%CF%84%CE%BF%CF%82\"\nW_RAM     = \"https://en.wiktionary.org/wiki/%D8%B1%D8%A7%D9%85\"\nW_SYRMRYM = \"https://en.wiktionary.org/wiki/%DC%A1%DC%AA%DC%9D%DC%A1\"\nWP_MARYAM = \"https://en.wikipedia.org/wiki/Maryam_(name)\"\nW_FA_MRYM = \"https://en.wiktionary.org/wiki/%D9%85%D8%B1%DB%8C%D9%85\"\n\nPOK875 = (\"Pokorny IEW p.875 (local POK_03.txt, form-feed leaf 110) prints the headword \"\n          \"'r̥k̑þo-s ‚Bär‘ (oder r̥k̑-s-o-s neben r̥k̑-to-s ?)' and lists \"\n          \"'Ai. ŕ̥kṣa- m. ‚Bär‘ = jav. arša-, osset. ars, arm. arj, alb. ari, gr. ἄρκτος ... \"\n          \"mir. art, cymr. arth ‚Bär‘, gall. Deae Artioni ‚Bärengöttin‘, lat. ursus ... \"\n          \"npers. xirs ‚Bär‘ soll auf iran. *r̥ša- = idg. r̥k̑o- weisen'. \"\n          \"Both of Nourai's headword variants (Rk-tho = r̥k̑þo-, Rk-so = r̥k̑so-) stand on that very page.\")\n\nSOD70 = (\"Gharib, Sogdian Dictionary, entry 1770 on printed p.70 (SOD_pages.txt leaf 135, whose running head reads '70'): \"\n         \"'1770 ʾšsh  B — o(s)sa ? ◎ *r̥sa; < IE *r̥k̑-so; Khwar. hrs; Av. arša — bear. SCE 359; GMS 155.' \"\n         \"Gharib's own IE reconstruction is *r̥k̑-so, i.e. Nourai's second headword 'Rk-so'.\")\n\nentry1 = {\n  \"entry\": 1,\n  \"root\": \"Rk-tho, Rk-so\",\n  \"verdict\": \"confirmed\",\n  \"modern_form\": \"PIE *h₂ŕ̥tḱos 'bear' (Pokorny 875 r̥k̑þo-s, with the variant r̥k̑so-; Watkins/AHD r̥tko-)\",\n  \"note\": (\"The root is real, the language label is right and the gloss 'bear (animal)' is exactly what the \"\n           \"standard handbooks give. Pokorny p.875 heads the entry 'r̥k̑þo-s ‚Bär‘ (oder r̥k̑-s-o-s neben r̥k̑-to-s ?)', \"\n           \"so Nourai's double headword 'Rk-tho, Rk-so' simply reproduces Pokorny's own hesitation between a \"\n           \"*-tḱ- and a *-ḱs- cluster; Gharib (SOD 1770) writes the same etymon *r̥k̑-so. Modern reconstruction \"\n           \"(Wiktionary, after Mallory-Adams and Beekes) is *h₂ŕ̥tḱos, a non-ablauting thematic o-stem, possibly \"\n           \"nominalised from *h₂retḱ- 'to damage' (cf. Skt. rákṣas- 'injury', Av. rašah-), with tabooistic \"\n           \"distortion in Latin ursus. Every branch Nourai draws (Iranian, Greek, Celtic, Sogdian) is a genuine \"\n           \"reflex of it; the weak points of the chart are inside the nodes, not in the root box.\"),\n  \"note_fa\": (\"ریشهٔ هندواروپایی آغازین *h₂ŕ̥tḱos «خرس» است. پوکورنی (ص ۸۷۵) سرواژه را «r̥k̑þo-s ‹خرس›، یا r̥k̑-s-o-s \"\n              \"در کنار r̥k̑-to-s؟» آورده است؛ بنابراین دو صورتِ «Rk-tho, Rk-so» که نورایی نوشته، بازتاب همان دودلیِ \"\n              \"خودِ پوکورنی میان خوشهٔ *-tḱ- و *-ḱs- است و قریب (فرهنگ سغدی، مدخل ۱۷۷۰) نیز همان *r̥k̑-so را بازسازی می‌کند. \"\n              \"در بازسازی امروزی این واژه یک نامْ‌ستاک مصوّتیِ بی‌اَبلاوت است که شاید از ریشهٔ *h₂retḱ- «آسیب رساندن» \"\n              \"(قس. rašah- اوستایی، rákṣas- سنسکریت) ساخته شده و در لاتین (ursus) دچار دگرگونیِ تابویی شده است. \"\n              \"ادعای نورایی دربارهٔ خودِ ریشه، هم از نظر نام و هم از نظر معنا و برچسب زبانی، درست است.\"),\n  \"sources\": [W_PIE, W_KHERS],\n  \"ref_check\": [\n    {\"ref\": \"POK:875\", \"status\": \"supports\", \"note\": POK875},\n    {\"ref\": \"SOD:70\", \"status\": \"supports\", \"note\": SOD70}\n  ],\n  \"consulted\": [\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. r̥tko- (AHD_watkins1985.txt line 900)\", \"stance\": \"supports\",\n     \"note\": \"'rtko-. Bear. 1. Latin ursus, bear (< *orcsos): URSINE. 2. Greek arktos, bear: ARCTIC, ARCTURUS. 3. Celtic *arto- in Welsh arth, bear, in the name Arthur (> Medieval Latin Artorius, Arthur): ARTHUR. [Pok. r̥ktho-s 875.]' — Watkins's entry is in fact the skeleton of Nourai's whole Greek+Celtic wing, and cross-refers to Pokorny 875.\"},\n    {\"src\": \"SYN\", \"where\": \"Buck, p.186 §3.73 'BEAR' (SYN.txt leaf 221)\", \"stance\": \"supports\",\n     \"note\": \"'1. IE *r̥k̑o-, possibly as the ‘destroyer’ (of beehives): Skt. rakṣas- ‘harm, injury’. Walde-P. 1.322 ... Grk. ἄρκτος ... Lat. ursus ... Ir. art, W. arth ...; Skt. ṛkṣa-, Av. arša-.' Buck's table lists Av. arša- and Skt. ṛkṣa- exactly as the chart does.\"},\n    {\"src\": \"IEC\", \"where\": \"Mann, col./p. 260 (IEC.txt, bear entry)\", \"stance\": \"supports\",\n     \"note\": \"'Gk. árktos, (hapax) árx; Alb. arí ...; Lat. ursus; Gaul. arto-; W arth; Cor. ors; Br. -arz ...; Li. irstva ‘bear’s den’. (The name is based on the bear’s grunt ...)' — Mann keeps the same cognate set but prefers an onomatopoeic explanation of the name.\"},\n    {\"src\": \"WLD\", \"where\": \"Walde-Pokorny II 322 (cited by Pokorny p.875 as 'WP. II 322')\", \"stance\": \"supports\",\n     \"note\": \"Pokorny's own back-reference for this lemma is WP. II 322; the same page is quoted by Buck ('Walde-P. 1.322/2.322') for IE *r̥k̑o- 'bear'. Bd. I-II of Walde-Pokorny are on disk only as unpaginated DLI scans, so the page itself was reached through these two citations rather than directly.\"}\n  ],\n  \"nodes\": []\n}\n\nentry1[\"nodes\"].append({\n  \"id\": 1, \"lang\": \"Avestan\", \"words\": \"areša; areša-ama\",\n  \"verdict\": \"plausible\",\n  \"derivation\": (\"Av. arəša- m. 'bear' (Nourai's 'areša' = arəša-, his usual way of writing the Avestan schwa) is \"\n                 \"genuine but rare: Bartholomae, AiW col. 203-204, marks it 'j. (p.) *arša- m. ‘Bär’' and can cite it \"\n                 \"only from Aogəmadaēčā 79, adding 'Aus ar. *r̥kṣa-. — ai. ŕ̥kṣa- m.; ... vgl. np. xirs'. Phonetically \"\n                 \"PIE *h₂ŕ̥tḱos gave Proto-Indo-Iranian *Hŕ̥ćšas (the cluster *-tḱ- assibilated to *-ćš-), whence Skt. \"\n                 \"ŕ̥kṣa- and, with Iranian *ćš > š and the regular anaptyctic ə- before a syllabic r̥, Avestan arəša-. \"\n                 \"The second word, areša-ama- 'having the strength of a bear', is not an attested Avestan lexeme: it is \"\n                 \"Bartholomae's morphological analysis of the OLD PERSIAN royal name Aršāma- (Arsames, Darius' grandfather), \"\n                 \"printed in AiW under 'aršama-' as 'Komp.: arša-ama- ‘die Kraft eines Bären’ besitzend' — and even there \"\n                 \"Bartholomae's own footnote offers the alternative '‘eines Mannes, Helden’; s. aršan-'. So word 1 is confirmed, \"\n                 \"word 2 is a reconstruction of Old Persian material placed under an Avestan label.\"),\n  \"derivation_fa\": (\"واژهٔ اوستایی arəša- «خرس» (که نورایی آن را areša نوشته، چون شوایِ اوستایی را به e می‌نگارد) واقعی ولی کم‌بسامد است؛ \"\n                    \"بارتولمه در «فرهنگ ایرانی باستان» (ستون ۲۰۳–۲۰۴) آن را تنها از اوگمدَیچا ۷۹ شاهد می‌آورد و می‌نویسد «از آریایی *r̥kṣa-، \"\n                    \"قس. سنسکریت ŕ̥kṣa- و فارسی نو خرس». از نظر آوایی، خوشهٔ *-tḱ- هندواروپایی در هندوایرانی به *-ćš- بدل شد و در ایرانی به š، \"\n                    \"و پیش از rِ هجایی مصوّت کوتاه ə افزوده شد: *h₂ŕ̥tḱos > *Hŕ̥ćšas > arəša-. اما areša-ama- واژه‌ای اوستایی نیست؛ این صورت، \"\n                    \"تجزیهٔ بارتولمه از نام پارسی باستان Aršāma- (اَرشام، نیای داریوش) است و خودِ بارتولمه در پانویس گزینهٔ دیگری هم می‌دهد: \"\n                    \"«دارای زور مرد/پهلوان» (قس. aršan-). پس واژهٔ نخست پذیرفتنی است و واژهٔ دوم با احتیاط.\"),\n  \"sources\": [W_PIE, W_KHERS],\n  \"ref_check\": [{\"ref\": \"POK:875\", \"status\": \"supports\", \"note\": POK875 + \" Pokorny explicitly equates 'jav. arša-' with Skt. ŕ̥kṣa-, which is Nourai's first word; the compound arša-ama- is not in Pokorny.\"}],\n  \"consulted\": [\n    {\"src\": \"BRT\", \"where\": \"Bartholomae, AiW col. 203-204 s.vv. arša-, aršama- (BRT.txt lines 5624-5635)\", \"stance\": \"supports\",\n     \"note\": \"'• j. (p.) *arša- m. ‘Bär’: ... Aog. 79. ... Aus ar. *r̥kṣa-. — ai. ŕ̥kṣa- m.; ... vgl. np. xirs' and, under aršama-, 'Komp.: arša-ama- ‘die Kraft eines Bären’ besitzend' with the footnote 'Oder auch ‘eines Mannes, Helden’; s. aršan-'.\"},\n    {\"src\": \"KNT\", \"where\": \"Kent, Old Persian §1914 and §117 (KNT.txt lines 1438, 1914)\", \"stance\": \"contradicts\",\n     \"note\": \"§1914: 'Aršāma- (from *arša-ama-) ‘Having the might of a hero’'; §117: 'OP arša- ‘male’ in Aršama- ‘Arsames’, Skt. ṛṣabhá- ‘bull’'. Kent keeps Bartholomae's segmentation but takes the first element as 'hero, male' (*h₁ers-), not 'bear'.\"},\n    {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien p.236 §129 and p.265 §162 (HUB.txt leaves 246, 275)\", \"stance\": \"supports\",\n     \"note\": \"p.236: 'xirs ‘Bär’ = skr. ṛkṣa-, zd. arəša-, gr. ἄρκτος, lat. ursus.' The Avestan form is cited in exactly Nourai's shape arəša-.\"}\n  ]\n})\n\nentry1[\"nodes\"].append({\n  \"id\": 2, \"lang\": \"Persian\", \"words\": \"xers; Aršâm\",\n  \"verdict\": \"plausible\",\n  \"derivation\": (\"NP خرس xers/xirs 'bear' is a genuine reflex of the root, but not literally a descendant of the Avestan \"\n                 \"word as the arrow suggests: it continues an Old Iranian *r̥šah- (Old Persian, not Avestan) > MP xirs \"\n                 \"(MacKenzie, CPD p.94: 'xirs [hls | N ~] bear') > NP xers. Two peculiarities are well documented: \"\n                 \"(a) the initial x- is prothetic — Hübschmann §162 lists xirs among the words where 'Vorschlag von x hat \"\n                 \"stattgefunden' (xastu, xāya, xām, xirs, xišt, xišm, xēš), and it is already Pahlavi (phl. x(i)rs, Bd. 56,14.17); \"\n                 \"(b) the s (not š) of xirs shows, as Hübschmann §129 argues, that the Persian form goes back to Iranian *r̥sa- \"\n                 \"rather than *r̥ša-, which is why Pokorny p.875 says 'npers. xirs soll auf iran. *r̥sa- weisen' — i.e. Persian and \"\n                 \"Avestan are sister forms, not mother and daughter. Wiktionary reconstructs OP *r̥šah < PIr. *Hŕ̥šah and notes the \"\n                 \"x- is 'debated'. The second word, ارشام / آرشام Āršām, is a modern Persian revival of the Achaemenid name \"\n                 \"Aršāma- (Gk. Ἀρσάμης, Behistun I.4, grandfather of Darius); Nourai's gloss 'with power of a bear' is Mo'in's, taken from \"\n                 \"Bartholomae, but Kent, Schmitt and the current onomastic literature read the first element as aršan- 'male, hero', \"\n                 \"giving 'having a hero's strength'. Hence: xers confirmed, Aršâm contested.\"),\n  \"derivation_fa\": (\"«خرس» بازماندهٔ همین ریشه است، اما نه از راه اوستایی که نمودار نشان می‌دهد: از ایرانی باستان *r̥šah- (پارسی باستان) \"\n                    \"به فارسی میانهٔ xirs (مکنزی، ص ۹۴: «xirs [hls] خرس») و از آن به فارسی نو رسیده است. دو نکتهٔ آوایی مشهور است: \"\n                    \"نخست، خِ آغازین «پیشوندِ آوایی» (prothetic) است و هوبشمان در بند ۱۶۲ «پرسیشه ‌شتودین» خرس را در کنار خایه، خام، خشت، خشم \"\n                    \"در فهرست واژه‌هایی می‌آورد که x در آغازشان افزوده شده و این افزایش در پهلوی هم دیده می‌شود (بنُدهش ۵۶). \"\n                    \"دوم، «س» (و نه «ش») نشان می‌دهد که صورت فارسی به ایرانی *r̥sa- بازمی‌گردد نه *r̥ša-؛ پوکورنی هم در ص ۸۷۵ همین را می‌گوید. \"\n                    \"پس خرس و arəša اوستایی خواهر یکدیگرند، نه مادر و دختر. واژهٔ دوم، «ارشام/آرشام»، احیای نام هخامنشیِ Aršāma- است؛ \"\n                    \"معنی «دارای زور خرس» از حاشیهٔ معین بر برهان قاطع (به نقل از بارتولمه) می‌آید، ولی کنت و اشمیت و ریشه‌شناسی نام‌های ایرانیِ امروز \"\n                    \"جزء نخست را aršan- «مرد، پهلوان» می‌دانند و معنی را «دارای زور پهلوان». ادعای نورایی دربارهٔ خرس درست و دربارهٔ آرشام با احتیاط پذیرفتنی است.\"),\n  \"sources\": [W_KHERS, WP_ARSAM, W_PIE],\n  \"ref_check\": [\n    {\"ref\": \"BQT:31\", \"status\": \"supports\",\n     \"note\": \"Borhan-e Qate' ed. Mo'in, vol.1 p.31 (the آرش/آرشی page; BQT_v1_pages.txt leaf 241, text quoted from the parallel OCR BQT_alt_v1.txt line 11847) carries Mo'in's footnote: «۵ آرشام - Aršāma- نام جد داریوش بزرگ شاهنشاه هخامنشی، مرکب از aršā بمعنی خرس و ama بمعنی زور، جمعاً دارای زور خرسی. بارتولمه ۲۰۶». This is verbatim Nourai's gloss, with Bartholomae as Mo'in's own authority.\"},\n    {\"ref\": \"BQT:733\", \"status\": \"supports\",\n     \"note\": \"Borhan vol.2 p.733 (BQT_v2_pages.txt leaf 191, running head ۷۳۳, six occurrences of خرس), Mo'in's etymological footnote: «# خرس ـ بکسر اول. پهلوی xirs (نیبرگ)، اوستا arəša، پارسی باستان aršā (در Aršāma = آرشام)، اشکاشمی/دشغنی/سمنانی/شهمیرزادی ...، سغدی ʾšsh (بنونیست)». The footnote pairs خرس with آرشام exactly as the chart's node does.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD p.94 s.v. xirs (PHD.txt line 661; also p.946 English index 'bear (anim.) xirs')\", \"stance\": \"supports\",\n     \"note\": \"'xirs [hls | N ~] bear.' MacKenzie reads the Pahlavi spelling hls as xirs and equates it with the New Persian word.\"},\n    {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II p.218 s.v. *xirs (NYB_vol2_glossary.txt line 4287)\", \"stance\": \"partial\",\n     \"note\": \"'*xirs [hls] ‘a ring, or the like’: 20⁶. — Both reading and meaning are quite uncertain.' Nyberg's *xirs is a different (homographic) word in the Kārnāmag passage; he does not dispute the Bundahišn xirs 'bear', but his glossary does not confirm it either.\"},\n    {\"src\": \"HRN\", \"where\": \"Horn, Grundriss p.105 s.v. xirs (HRN.txt leaf 126)\", \"stance\": \"supports\",\n     \"note\": \"'xirs ‘Bär’. aw. arəša- ‘Bär’ (Aog.); phlv. x(i)rs (Bund.); ai. ṛkṣa-; arm. arj; oss. ars; šiɣn. ɣūrǰ, sar. ɣūrx.' Horn adds a warning relevant to this page: 'Aw. Ərəxša-, vergl. ai. Ārkša- ... sind hiervon zu trennen' — the archer Āraš is NOT this word.\"},\n    {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien p.265 §162 (HUB.txt leaf 275)\", \"stance\": \"supports\",\n     \"note\": \"'§162. Vorschlag von x hat stattgefunden bei: ... xirs ‘Bär’, phl. x(i)rs Bdh. 56, 14 und 17, zd. arəša-, skr. ṛkṣa-' — the source for the prothetic x-.\"},\n    {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e Rishe-ha, pdf p.92 and pp.147/439 cross-references (ARY_pages.txt leaves 91, 146, 438)\", \"stance\": \"supports\",\n     \"note\": \"Aryanpur's IE-root tables repeatedly send the reader to «پسگشت‌ها خرس» ('see خرس') and list the cognate set Sanskrit – Armenian – Greek άρκτος – Latin ursus for it, citing Borhan-e Qate'. The headword page for خرس itself could not be located in this OCR (the display-font headwords are not recognised).\"},\n    {\"src\": \"KNT\", \"where\": \"Kent, Old Persian §1914\", \"stance\": \"contradicts\",\n     \"note\": \"'Aršāma- (from *arša-ama-) ‘Having the might of a hero’' — against the 'bear' reading of Āršām that Mo'in and Nourai give.\"}\n  ]\n})\n\nentry1[\"nodes\"].append({\n  \"id\": 3, \"lang\": \"Greek\", \"words\": \"arktos; arkticos\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": (\"Gk. ἄρκτος árktos 'bear' is the regular Hellenic reflex of PIE *h₂ŕ̥tḱos: the syllabic *r̥ became Greek \"\n                 \"ar-, the cluster *-tḱ- was metathesised/simplified to -kt-, and the o-stem ending was kept (*h₂ŕ̥tḱos > \"\n                 \"Proto-Hellenic *árktos). Homer already uses it both for the animal and for the circumpolar constellation \"\n                 \"(Iliad 18.487 ἄρκτον θἷ καὶ ἄμαξαν), whence the secondary sense 'the north'. The adjective ἀρκτικός \"\n                 \"arktikós is a normal -ikos derivative meaning 'of the Bear, northern' — Nourai's gloss 'northern bear-shaped \"\n                 \"constellation' describes ἄρκτος rather than the adjective, but the derivation itself is uncontroversial.\"),\n  \"derivation_fa\": (\"«ἄρκτος» یونانی بازتاب منظم *h₂ŕ̥tḱos است: rِ هجایی به ar بدل شده، خوشهٔ *-tḱ- با قلب (metathesis) به -kt- ساده شده \"\n                    \"و پایانهٔ نامْ‌ستاک o حفظ شده است. این واژه از هومر (ایلیاد ۱۸/۴۸۷) هم به معنی جانور و هم به معنی صورت فلکیِ دبّ به کار رفته \"\n                    \"و از همین‌جا معنی «شمال» گرفته است. صفتِ ἀρκτικός با پسوند -ικός از آن ساخته شده و «شمالی، وابسته به دبّ» معنی می‌دهد. \"\n                    \"معنایی که نورایی برای ἀρκτικός نوشته در حقیقت معنیِ ἄρκτος است، ولی خودِ اشتقاق بی‌چون‌وچرا درست است.\"),\n  \"sources\": [E_ARCTIC, W_ARKTOS, W_PIE],\n  \"ref_check\": [{\"ref\": \"AHD\", \"status\": \"supports\",\n     \"note\": \"Watkins 1985 s.v. r̥tko-: '2. Greek arktos, bear: ARCTIC, ARCTURUS' (AHD_watkins1985.txt line 900); the index line 2437 confirms 'ARCTIC rtko- ARCTURUS rtko-, wer-4'.\"}],\n  \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"Pokorny p.875\", \"stance\": \"supports\", \"note\": \"'... alb. ari, gr. ἄρκτος, jünger ἄρκος ...' listed directly under r̥k̑þo-s.\"},\n    {\"src\": \"SYN\", \"where\": \"Buck p.186 §3.73\", \"stance\": \"supports\", \"note\": \"'Grk. ἄρκτος, NG pop. ἀρκούδα' in the BEAR table under IE *r̥k̑o-.\"},\n    {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls vol.1 s.v. arctic (FSD_vol1.txt line 24283)\", \"stance\": \"supports\",\n     \"note\": \"'[< F. arctique, < LL. arcticus, < Gr. arktikos, < arktos, bear, the constellation.]' — and 'Of or pertaining to either of the constellations called the Great Bear and the Little Bear.'\"}\n  ]\n})\n\nentry1[\"nodes\"].append({\n  \"id\": 4, \"lang\": \"Latin\", \"words\": \"arcticus\",\n  \"verdict\": \"plausible\",\n  \"derivation\": (\"Latin arcticus is a straight learned borrowing of Gk. ἀρκτικός, Greek κτ being kept as ct and -ος latinised \"\n                 \"to -us; it is Late Latin (in Christian and astronomical writers) and is spelt articus in Medieval Latin, \"\n                 \"once the -ct- had been simplified in speech. Its meaning is the adjective 'northern, of the (constellation of \"\n                 \"the) Bear' — as in circulus arcticus 'the Arctic circle'. Nourai's gloss 'north pole' is therefore too narrow \"\n                 \"and is really the gloss of a noun phrase, not of the Latin word; Funk & Wagnalls s.v. arctic gives \"\n                 \"'< LL. arcticus, < Gr. arktikos'. The arrow Greek → Latin is correct; only the gloss is loose.\"),\n  \"derivation_fa\": (\"«arcticus» لاتین وام‌واژهٔ عالمانه‌ای از ἀρκτικός یونانی است: خوشهٔ κτ به ct نگه داشته شده و پایانهٔ -ος به -us لاتینی بدل شده است. \"\n                    \"این صورت به لاتینِ متأخّر تعلق دارد و در لاتینِ میانه به articus (بی ‌c) هم نوشته می‌شود. معنای آن صفت است: «شمالی، وابسته به صورت فلکی دبّ» \"\n                    \"(مثلاً circulus arcticus «مدار قطبی شمالی»). بنابراین معنایی که نورایی داده («قطب شمال») تنگ و نادقیق است، هرچند خودِ پیکان یونانی ← لاتین درست است. \"\n                    \"ادعای نورایی با احتیاط پذیرفتنی است: مسیرِ وام‌گیری درست، معنا نادقیق.\"),\n  \"sources\": [E_ARCTIC],\n  \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The node carries no reference of Nourai's own; the Greek parent node's AHD citation covers the chain, and Watkins does not mention the Latin intermediary.\"}],\n  \"consulted\": [\n    {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls vol.1 s.v. arctic (FSD_vol1.txt line 24283)\", \"stance\": \"supports\",\n     \"note\": \"'[< F. arctique, < LL. arcticus, < Gr. arktikos, < arktos, bear, the constellation.]' — Late Latin arcticus is real and is the link to the modern languages, but it is glossed as an adjective, not as 'north pole'.\"},\n    {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict., s.v. Antarctic (SKT.txt line 747)\", \"stance\": \"partial\",\n     \"note\": \"'Antarctic; see Arctic.' Skeat's own Arctic entry did not come out of the OCR, so only the cross-reference could be read.\"}\n  ]\n})\n\nentry1[\"nodes\"].append({\n  \"id\": 5, \"lang\": \"English\", \"words\": \"Arctic\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": (\"English Arctic entered in the late 14th c. as artik (Chaucer, Treatise on the Astrolabe), from Old French \"\n                 \"artique, from Medieval Latin articus (= Late Latin arcticus), from Gk. ἀρκτικός. The -c- was restored on \"\n                 \"etymological grounds from the 1550s. The sense moved from the sky ('the arctic circle of the heavens') to the \"\n                 \"earth ('northern', early 15th c.), to 'the northern polar regions' as a noun (1560s) and finally to \"\n                 \"'cold, frigid' (1660s). Nourai's Latin → English arrow skips the Old French stage, but the chain itself is right.\"),\n  \"derivation_fa\": (\"واژهٔ انگلیسی Arctic در اواخر سدهٔ ۱۴ م. به صورت artik وارد انگلیسی شد (چاسر، «رساله در اسطرلاب») از فرانسهٔ باستان artique، \"\n                    \"از لاتینِ میانه articus (= arcticus لاتینِ متأخّر)، از ἀρκτικός یونانی. حرف c در حدود ۱۵۵۰ م. بر پایهٔ ریشه‌شناسی دوباره به املا بازگردانده شد. \"\n                    \"تحول معنایی چنین بوده است: «مدار قطبیِ آسمان» ← «شمالی» (آغاز سدهٔ ۱۵) ← «سرزمین‌های قطبی شمال» (دههٔ ۱۵۶۰) ← «بسیار سرد» (دههٔ ۱۶۶۰). \"\n                    \"نمودارِ نورایی مرحلهٔ فرانسهٔ باستان را نیاورده، اما زنجیره درست است.\"),\n  \"sources\": [E_ARCTIC],\n  \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"No reference is given for this node in the book; the parent Greek node cites AHD, whose index line confirms 'ARCTIC rtko-'.\"}],\n  \"consulted\": [\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985, index and s.v. r̥tko-\", \"stance\": \"supports\", \"note\": \"'ARCTIC rtko-' (index) and 'Greek arktos, bear: ARCTIC, ARCTURUS' (entry).\"},\n    {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls vol.1 s.v. arctic\", \"stance\": \"supports\",\n     \"note\": \"'[< F. arctique, < LL. arcticus, < Gr. arktikos, < arktos, bear, the constellation.]' — F&W route the English word through French, as Etymonline does.\"}\n  ]\n})\n\nentry1[\"nodes\"].append({\n  \"id\": 6, \"lang\": \"Celtic\", \"words\": \"artho\",\n  \"verdict\": \"plausible\",\n  \"derivation\": (\"The Celtic reflex is real: Proto-Celtic *artos 'bear' < PIE *h₂ŕ̥tḱos, giving Gaulish artos (and the \"\n                 \"bear-goddess Artio, dedications 'Deae Artioni'), Old Irish art 'bear, hero', Welsh arth, Cornish arth, \"\n                 \"Breton arzh. Nourai's spelling 'artho' is not any attested Celtic form: Proto-Celtic and Gaulish have -t-, and \"\n                 \"the -th of Welsh arth is a Brythonic spirantisation of that -t- in final position, so 'artho' looks like a \"\n                 \"blend of Welsh arth with the -th- of Pokorny's headword r̥k̑þo-. The printed page indeed reads 'artho : bear' \"\n                 \"(so the extraction is faithful); AHD, which is the node's only reference, writes 'Celtic *arto- in Welsh arth'. \"\n                 \"The derivation is right, the cited form is the author's own normalisation.\"),\n  \"derivation_fa\": (\"بازماندهٔ سلتیِ این ریشه واقعی است: سلتی آغازین *artos «خرس» از *h₂ŕ̥tḱos، که گالی artos (و نام ایزدبانوی خرس، Artio، در کتیبه‌های \"\n                    \"«Deae Artioni»)، ایرلندی باستان art «خرس، پهلوان»، ولزی arth، کورنی arth و برتونی arzh از آن برآمده‌اند. اما صورت «artho» که نورایی آورده \"\n                    \"در هیچ زبان سلتی گواهی نشده است؛ سلتیِ آغازین و گالی t دارند و ثِ ولزیِ arth حاصل سایشی‌شدنِ همان t در پایان واژه است. پیداست که نورایی \"\n                    \"ولزی arth را با ثِ سرواژهٔ پوکورنی (r̥k̑þo-) درآمیخته است. صفحهٔ چاپی هم «artho : bear» دارد، پس خطای خوانش اسکن نیست. \"\n                    \"اشتقاق درست است، ولی صورتِ نقل‌شده ساختهٔ خودِ مؤلف است.\"),\n  \"sources\": [W_CELT, W_PIE],\n  \"ref_check\": [{\"ref\": \"AHD\", \"status\": \"partial\",\n     \"note\": \"Watkins 1985 s.v. r̥tko-: '3. Celtic *arto- in Welsh arth, bear, in the name Arthur (> Medieval Latin Artorius, Arthur): ARTHUR.' The reference supports the Celtic branch but prints *arto-, not 'artho'.\"}],\n  \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"Pokorny p.875\", \"stance\": \"partial\",\n     \"note\": \"'... mir. art, cymr. arth ‚Bär‘, gall. Deae Artioni ‚Bärengöttin‘' — Old Irish art and Welsh arth, again no *artho-.\"},\n    {\"src\": \"IEC\", \"where\": \"Mann, bear entry (IEC.txt p.260)\", \"stance\": \"partial\", \"note\": \"'Gaul. arto-; W arth; Cor. ors (sic); Br. -arz (in kraban-arz ‘bear’s breech’)'.\"},\n    {\"src\": \"SYN\", \"where\": \"Buck p.186 §3.73\", \"stance\": \"partial\", \"note\": \"'Ir. art, W. arth (Pedersen 1.89)'.\"}\n  ]\n})\n\nentry1[\"nodes\"].append({\n  \"id\": 7, \"lang\": \"English\", \"words\": \"Arthur\",\n  \"verdict\": \"plausible\",\n  \"derivation\": (\"Two rival accounts of the name are alive. (1) The Celtic one, which the chart follows and which Watkins/AHD \"\n                 \"print verbatim ('Celtic *arto- in Welsh arth, bear, in the name Arthur'): Welsh Arthur is taken as *Arto-rīg-ios \"\n                 \"'bear-king' or as arth + (g)wr 'bear-man', and English Arthur is simply the Welsh name carried into English through \"\n                 \"Geoffrey of Monmouth's Historia Regum Britanniae (c.1136) and the French romances. (2) The Latin one, now at least \"\n                 \"as widely held: Welsh Arthur regularly continues the Roman gentilicium Artorius (cf. L. Artorius Castus, 2nd c. CE), \"\n                 \"Latin -ōrius giving Welsh -ur; on that view any 'bear' resonance is secondary folk association, and Artorius itself \"\n                 \"may be Etruscan or Messapic. Wiktionary heads the entry 'probably from Middle Welsh arth' while listing Artorius as a \"\n                 \"serious alternative. The arrow is thus accepted by some authorities but not all, and the chart in any case omits the \"\n                 \"Welsh stage between 'Celtic' and 'English'.\"),\n  \"derivation_fa\": (\"دربارهٔ نام Arthur دو نظر رقیب هست. نخست، نظرِ سلتی که نمودار از آن پیروی می‌کند و واتکینز در پیوست AHD عیناً همان را نوشته است \"\n                    \"(«سلتی *arto- در ولزی arth ‹خرس›، در نام Arthur»)؛ بر این پایه Arthur ولزی از *Arto-rīg-ios «شاهِ خرس» یا از arth + gwr «مردِ خرس» است \"\n                    \"و از راه «تاریخ شاهان بریتانیا»ی جفری آو مانموث (حدود ۱۱۳۶ م.) و رمانس‌های فرانسوی به انگلیسی رسیده است. دوم، نظرِ لاتینی که امروز دست‌کم \"\n                    \"به همان اندازه هوادار دارد: Arthur ولزی بازماندهٔ منظمِ نام خانوادگی رومی Artorius است (پایانهٔ -ōrius لاتین در ولزی -ur می‌دهد) و پیوند آن با «خرس» \"\n                    \"ریشه‌شناسی عامیانه است. ویکی‌واژه صورت ولزی را «محتمل‌تر» می‌داند ولی Artorius را هم جدی می‌گیرد. پس ادعای نورایی با احتیاط پذیرفتنی است؛ \"\n                    \"افزون بر این، نمودار مرحلهٔ ولزی را میان «سلتی» و «انگلیسی» نیاورده است.\"),\n  \"sources\": [W_ARTHUR, W_CELT],\n  \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\",\n     \"note\": \"The English node carries no reference; its parent Celtic node cites AHD, and Watkins does name Arthur: 'in the name Arthur (> Medieval Latin Artorius, Arthur): ARTHUR'.\"}],\n  \"consulted\": [\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. r̥tko- (AHD_watkins1985.txt line 900)\", \"stance\": \"supports\",\n     \"note\": \"'3. Celtic *arto- in Welsh arth, bear, in the name Arthur (> Medieval Latin Artorius, Arthur): ARTHUR.' Watkins even makes Medieval Latin Artorius derive FROM the Celtic name, the reverse of the Roman-gentilicium theory.\"},\n    {\"src\": \"POK\", \"where\": \"Pokorny p.875\", \"stance\": \"silent\", \"note\": \"Pokorny lists Welsh arth and Gaulish Artio but says nothing about the name Arthur.\"},\n    {\"src\": \"KLN\", \"where\": \"Klein 1966 (KLN_1966.txt)\", \"stance\": \"silent\", \"note\": \"grep '^Arthur' returns nothing: Klein's dictionary has no Arthur entry to compare.\"}\n  ]\n})\n\nentry1[\"nodes\"].append({\n  \"id\": 8, \"lang\": \"Sogdian\", \"words\": \"`ššh\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": (\"Gharib's Sogdian dictionary no.1770 (printed p.70) has the Buddhist-Sogdian word ʾššh, read o(š)ša, glossed \"\n                 \"'bear' and derived '◎ *r̥sa; < IE *r̥k̑-so; Khwar. hrs; Av. arša', with the references SCE 359 and GMS 155 \"\n                 \"(Gershevitch, Grammar of Manichean Sogdian §155). Nourai's `ššh is that transliteration, the backtick standing \"\n                 \"for aleph. Phonetically the Old Iranian *r̥ša- lost its r by assimilation to the following sibilant and the \"\n                 \"geminate -šš- resulted (Sogdian regularly writes the final -h of the ʾ-stem); the same *r̥sa- underlies Khwarezmian \"\n                 \"hrs and Persian xirs. Both the form and the page number Nourai gives are exact.\"),\n  \"derivation_fa\": (\"در «فرهنگ سغدی» بدرالزمان قریب، مدخل ۱۷۷۰ در صفحهٔ ۷۰، واژهٔ سغدی بودایی ʾššh آمده که آن را o(š)ša می‌خواند، «خرس» معنی می‌کند \"\n                    \"و چنین ریشه‌یابی می‌کند: «از *r̥sa؛ از هندواروپایی *r̥k̑-so؛ قس. خوارزمی hrs و اوستایی arša» (با ارجاع به SCE 359 و GMS 155). \"\n                    \"صورتی که نورایی نوشته (`ššh) همان نویسه‌گردانی است و نشانهٔ ` جانشین همزه/الف است. از نظر آوایی، rِ ایرانی باستان در *r̥ša- پیش از سایشی \"\n                    \"همگون شده و ššِ مشدّد پدید آمده است؛ همین *r̥sa- ریشهٔ hrs خوارزمی و «خرس» فارسی هم هست. هم صورت و هم شمارهٔ صفحه‌ای که نورایی داده دقیق است.\"),\n  \"sources\": [W_KHERS],\n  \"ref_check\": [{\"ref\": \"SOD:70\", \"status\": \"supports\", \"note\": SOD70}],\n  \"consulted\": [\n    {\"src\": \"SOD\", \"where\": \"Gharib no.1770, p.70 (SOD_pages.txt leaf 135); English index 'bear 1770' (leaf ~ line 37699)\", \"stance\": \"supports\",\n     \"note\": \"'1770 ʾššh B — o(s)sa ? ◎ *r̥sa; < IE *r̥k̑-so; Khwar. hrs; Av. arša — bear. SCE 359; GMS 155.'\"},\n    {\"src\": \"BQT\", \"where\": \"Borhan vol.2 p.733, Mo'in's footnote to خرس\", \"stance\": \"supports\",\n     \"note\": \"Mo'in's cognate list for خرس ends «... سغدی ʾšsh، بنونیست» — the same Sogdian form, credited to Benveniste.\"},\n    {\"src\": \"POK\", \"where\": \"Pokorny p.875\", \"stance\": \"silent\", \"note\": \"Pokorny's entry has no Sogdian form.\"}\n  ]\n})\n\nentry8 = {\n  \"entry\": 8,\n  \"root\": \"R.y.m\",\n  \"verdict\": \"disputed\",\n  \"modern_form\": \"Arabic root ر ي م r-y-m 'to depart from' (< Proto-Semitic *rayam-); NOT the source of the name Maryam, and not a Syriac root\",\n  \"note\": (\"Two things are wrong in the root box. (a) The language label: r-y-m 'to leave, depart from a place' is an ARABIC \"\n           \"root (Wiktionary: rāma, root ر ي م, 'to depart from, to separate oneself from', from Proto-Semitic *rayam-, related to \"\n           \"*rawam-); Nourai's own reference, SAP:617, is Sayyah's Persian version of al-Munjid — an ARABIC dictionary, which can \"\n           \"only document the Arabic verb. Syriac has ܢܡ rām 'to be high, exalted' (root rwm) and the noun ܡܪܝܡ Maryam as a NAME, \"\n           \"but no verb r-y-m 'to depart'. (b) The claim implied by the whole tree — that Miryam/Maryam is a derivative of a \"\n           \"Semitic verb 'to depart' — is precisely the derivation of the medieval Arab philologers (al-Jawharī; Lisān al-ʿArab xv.152) \"\n           \"which Nourai's other cited reference, Jeffery FVQ p.262, quotes only in order to reject it. Modern scholarship derives \"\n           \"the Arabic and Syriac names from Hebrew Miryam, whose own origin is undetermined (Egyptian mry 'beloved'; Semitic m-r-r \"\n           \"'bitter'; Hebrew m-r-y 'rebellion'), and Klein simply writes 'which is of uncertain origin'. The internal chain of the \"\n           \"chart (Hebrew > Aramaic > Greek > Latin/English) is sound; the root box above it is not.\"),\n  \"note_fa\": (\"در جعبهٔ ریشه دو خطا هست. نخست برچسب زبانی: ریشهٔ «ر ی م» به معنی «دور شدن، جدا شدن از جایی» ریشه‌ای عربی است \"\n              \"(ویکی‌واژه: رَامَ، از سامیِ آغازین *rayam-)، نه سریانی؛ خودِ مرجعی که نورایی آورده (فرهنگ سیّاح، ترجمهٔ فارسی «المنجد») فرهنگی عربی است \"\n              \"و جز فعل عربی چیزی نمی‌تواند گواهی کند. در سریانی فعل ܪܡ (rām) «بلند بودن» هست (ریشهٔ rwm) و نام ܡܪܝܡ Maryam، اما فعل r-y-m به معنی «دور شدن» نیست. \"\n              \"دوم، ادعای اصلیِ نمودار ــ که «مریم» مشتقِ فعلی سامی به معنی «دور شدن» باشد ــ همان ریشه‌شناسیِ لغویانِ عرب (جوهری، لسان‌العرب ۱۵/۱۵۲) است که \"\n              \"آرتور جفری در «واژگان دخیل در قرآن» ص ۲۶۲ ــ که نورایی خود به آن ارجاع می‌دهد ــ تنها برای رد کردنش نقل می‌کند. پژوهش امروزی نام عربی و سریانی را \"\n              \"وام‌گرفته از عبریِ מִרְיָם Miryām می‌داند و خاستگاه خودِ آن را نامعلوم می‌شمارد (مصری mry «محبوب»؛ سامی m-r-r «تلخ»؛ عبری m-r-y «سرکشی»)؛ کلاین هم \"\n              \"می‌نویسد «خاستگاهش نامعلوم است». زنجیرهٔ درونیِ نمودار (عبری ← آرامی ← یونانی ← لاتین/انگلیسی) درست است، اما جعبهٔ ریشه نادرست است: \"\n              \"پژوهش امروزی ادعای نورایی را رد می‌کند.\"),\n  \"sources\": [W_RAM, W_SYRMRYM, W_MIRIAM, WP_MARYAM],\n  \"ref_check\": [{\"ref\": \"SAP:617\", \"status\": \"not_checked\",\n     \"note\": \"Sayyah, Farhang-e Sayyah / the Persian al-Munjid, is not available online (refs_online.json: kind 'purchase', fidibo ebook, no local copy). Its Arabic original, al-Munjid, does carry ريم 'to depart'; what cannot be checked is Nourai's use of it as evidence for a SYRIAC root.\"}],\n  \"consulted\": [\n    {\"src\": \"FVQ\", \"where\": \"Jeffery, Foreign Vocabulary of the Qur'an p.262 s.v. مريم (FVQ_pages.txt leaf 279)\", \"stance\": \"contradicts\",\n     \"note\": \"'Some of the philologers took the name to be Arabic, a form mafʿal from rāma, meaning to depart from a place. Some, however, noted it as a foreign word ... Undoubtedly it does go back to the Heb. מרים, but the vowelling of the Arabic Maryam would point to its having come from a Christian source rather than directly from the Hebrew ... the probabilities are in favour of its having come from the Syriac.'\"},\n    {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. Mary and s.v. Miriam (KLN_1966.txt lines 23034, 24012; leaf 506)\", \"stance\": \"contradicts\",\n     \"note\": \"'Mary ... fr. Heb. Miryam, which is of uncertain origin' and 'Miriam ... Heb. Miryām.' No Syriac or Arabic verbal root.\"},\n    {\"src\": \"AFA\", \"where\": \"Fraenkel, Die aramäischen Fremdwörter im Arabischen (AFA.txt)\", \"stance\": \"silent\",\n     \"note\": \"grep -i 'Maryam|Mirjam|Marjam' returns nothing; Fraenkel does not treat the name.\"},\n    {\"src\": \"AFM\", \"where\": \"Addi Shir, al-Alfāẓ al-Fārisiyya al-Muʿarraba (AFM.txt) and TAD (al-Unaysi)\", \"stance\": \"silent\",\n     \"note\": \"grep 'مريم' returns nothing in either — neither treats Maryam as a loan they cover.\"}\n  ],\n  \"nodes\": []\n}\n\nentry8[\"nodes\"].append({\n  \"id\": 1, \"lang\": \"Arabic\", \"words\": \"r.y.m; Maryam\",\n  \"verdict\": \"disputed\",\n  \"derivation\": (\"The first word is genuine: Arabic رَامَ rāma / ya-rīmu, root ر ي م, 'to depart from, to quit (a place)', \"\n                 \"from Proto-Semitic *rayam- (a by-form of *rawam-); it is the verb of the proverbial mā rimtu 'I have not left'. \"\n                 \"The second word is where the chart goes wrong. Arabic مَرْيَم Maryam, the Qur'anic name of Jesus' mother \"\n                 \"(34 occurrences, and the title of sūra 19), is not a mafʿal-formation from that root. Jeffery, whom Nourai cites \"\n                 \"for exactly this node, reports the mafʿal < rāma analysis as the opinion of al-Jawharī and Lisān al-ʿArab xv.152 and \"\n                 \"rejects it: 'Undoubtedly it does go back to the Heb. מרים, but the vowelling of the Arabic Maryam would point to its \"\n                 \"having come from a Christian source ... the probabilities are in favour of its having come from the Syriac.' Wiktionary \"\n                 \"likewise: 'From Aramaic and post-Biblical Hebrew מרים (Maryam), from Biblical Hebrew מִרְיָם (Miryām).' The \"\n                 \"borrowing is pre-Islamic, through Syriac-speaking Christians of the Arabian border (Najrān, Ḥīra), which is why the \"\n                 \"vowelling is Maryam and not the Hebrew Miryam. So: the verb is real, the name is not derived from it.\"),\n  \"derivation_fa\": (\"واژهٔ نخست درست است: فعل عربی رَامَ / یَرِیمُ از ریشهٔ «ر ی م» به معنی «دور شدن، ترک گفتنِ جایی» (از سامیِ آغازین *rayam-، گونه‌ای از *rawam-)، \"\n                    \"همان فعلی که در «ما رِمتُ» به کار می‌رود. اما واژهٔ دوم نادرست جای گرفته است. «مَرْیَم»، نام قرآنیِ مادر عیسی (۳۴ بار در قرآن و نامِ سورهٔ ۱۹)، \"\n                    \"صورت «مَفْعَل» از این ریشه نیست. آرتور جفری در همان صفحه‌ای که نورایی به آن ارجاع می‌دهد (ص ۲۶۲) این تحلیل را به جوهری و لسان‌العرب (۱۵/۱۵۲) نسبت می‌دهد \"\n                    \"و ردش می‌کند: «بی‌گمان به عبریِ מרים بازمی‌گردد، ولی واکه‌گذاریِ Maryam عربی نشان می‌دهد که از سرچشمه‌ای مسیحی ــ به احتمال زیاد سریانی ــ آمده است». \"\n                    \"ویکی‌واژه نیز همین را می‌گوید. وام‌گیری پیش از اسلام و از راه مسیحیانِ سریانی‌زبانِ نجران و حیره بوده و به همین سبب واکهٔ نخست a است نه i. \"\n                    \"پژوهش امروزی ادعای نورایی را دربارهٔ نام «مریم» رد می‌کند.\"),\n  \"sources\": [W_RAM, W_MARYAM, WP_MARYAM],\n  \"ref_check\": [{\"ref\": \"FVQ:262\", \"status\": \"contradicts\",\n     \"note\": \"FVQ_pages.txt leaf 279 = printed p.262, s.v. مريم: 'Some of the philologers took the name to be Arabic, a form mafʿal from rāma, meaning to depart from a place. ... Undoubtedly it does go back to the Heb. מרים ... the probabilities are in favour of its having come from the Syriac.' Jeffery reports Nourai's derivation only as a rejected native guess.\"}],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. Mary (leaf 506)\", \"stance\": \"contradicts\",\n     \"note\": \"Klein's chain runs L. Maria < Gk. Μαριάμ, Μαρία < Aram. (Targum) Maryam < Heb. Miryam; no Arabic verbal root anywhere.\"},\n    {\"src\": \"AFM\", \"where\": \"Addi Shir (AFM.txt), TAD (al-Unaysi), AFA (Fraenkel)\", \"stance\": \"silent\",\n     \"note\": \"None of the three loanword dictionaries has an entry مريم (grep returns nothing), so none supports an Arabic-internal formation either.\"},\n    {\"src\": \"MON\", \"where\": \"Mo'in, 2-vol. abridgement (MON_part2.txt lines 5028, 11556, 23906-23915)\", \"stance\": \"partial\",\n     \"note\": \"Mo'in's lexicon volumes have مریم only in the plant names کف مریم / پنجه مریم / قدح مریم (حشیشة المریم); the personal name belongs to the aʿlām volumes.\"}\n  ]\n})\n\nentry8[\"nodes\"].append({\n  \"id\": 2, \"lang\": \"Persian\", \"words\": \"Maryam\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": (\"The edge Arabic → Persian is right: NP مریم Maryam is a straight loan from Arabic مَرْيَم (Wiktionary, Persian \"\n                 \"مریم: 'Borrowed from Arabic مَرْيَم (maryam), from Aramaic מרים (maryam)'), entering Persian with the Qur'an and \"\n                 \"the Islamic religious vocabulary from the 2nd/8th century onward and keeping the Arabic spelling and vowelling \"\n                 \"unchanged (only ي > ی in Persian orthography). It is used as a woman's name, as the name of the Virgin — the sense \"\n                 \"in the Rumi line the chart quotes, «روح کی گردد فدای آن دمی / کز نسیمش حامله شد مریمی» — and secondarily as a flower name \"\n                 \"(tuberose, Polianthes tuberosa) and in the plant compounds کف مریم / پنجه مریم. Only the ultimate origin assumed \"\n                 \"above this node is wrong; the borrowing drawn here is correct.\"),\n  \"derivation_fa\": (\"پیکان «عربی ← فارسی» درست است: «مریم» فارسی وام‌واژه‌ای است یکراست از عربیِ مَرْیَم (ویکی‌واژه: «وام‌گرفته از مَرْیَمِ عربی، از آرامی מרים») \"\n                    \"که با قرآن و واژگان دینیِ اسلامی از سدهٔ دوم هجری به فارسی راه یافته و املا و واکه‌گذاری عربی را بی‌دگرگونی نگه داشته است (تنها ی عربی در خط فارسی به ی بدل شده). \"\n                    \"این واژه هم نام زنانه است، هم نام مریمِ عذرا ــ همان معنایی که در بیت مولوی در نمودار آمده: «روح کی گردد فدای آن دمی / کز نسیمش حامله شد مریمی» ــ \"\n                    \"و هم نامِ گلی (گل مریم، Polianthes tuberosa) و جزءِ ترکیب‌های گیاهی «کف مریم» و «پنجه مریم». تنها خاستگاهی که در بالای این گره فرض شده نادرست است؛ \"\n                    \"خودِ وام‌گیری که اینجا کشیده شده درست است.\"),\n  \"sources\": [W_FA_MRYM, W_MARYAM],\n  \"ref_check\": [{\"ref\": \"MON:4053\", \"status\": \"not_checked\",\n     \"note\": \"Mo'in's Farhang-e Farsi p.4053 falls in the aʿlām (proper-name) volumes 5-6, which are not online and are not among the local OCR files; vajehyab/abadis serve only the lexicon volumes and cannot be paged. The 2-vol. abridgement on disk (MON_part1/part2) has مریم only as a plant name.\"}],\n  \"consulted\": [\n    {\"src\": \"MON\", \"where\": \"Mo'in, 2-vol. abridgement (MON_part2.txt lines 11556, 23906-23915)\", \"stance\": \"partial\",\n     \"note\": \"«قدح مریم: (گیا.) گیاهی است دوایی ...», «کف مریم: (گیا.) ... و آن را بنام پنجه مریم نیز می‌نامند» — confirms the Persian word and its plant senses, not the etymology.\"},\n    {\"src\": \"FVQ\", \"where\": \"Jeffery p.262\", \"stance\": \"supports\",\n     \"note\": \"Jeffery's route Hebrew > Syriac > Arabic implies the Persian form is a post-Islamic Arabic loan, exactly the arrow drawn here.\"},\n    {\"src\": \"PLA\", \"where\": \"Asbaghi, Persische Lehnwörter im Arabischen\", \"stance\": \"silent\",\n     \"note\": \"Not applicable / silent: Asbaghi catalogues Persian words in Arabic, and Maryam is a loan in the opposite direction, so his dictionary has nothing on it.\"}\n  ]\n})\n\nentry8[\"nodes\"].append({\n  \"id\": 3, \"lang\": \"Hebrew\", \"words\": \"Miryâm\",\n  \"verdict\": \"disputed\",\n  \"derivation\": (\"Hebrew מִרְיָם Miryām is correctly identified as the ancestor of all the later forms, and the biblical bearer is \"\n                 \"indeed the sister of Moses and Aaron (Ex. 15:20); the chart's second identification, 'mother of Jesus', is a conflation \"\n                 \"— Jeffery notes that the Qur'an itself (xix.29, iii.31, lxvi.12) confuses the two women, but in Hebrew the name is only \"\n                 \"Moses' sister's. What is disputed is everything else. (a) The gloss 'rebellion' is the traditional midrashic reading \"\n                 \"(from מְרִי merī 'rebellion', root m-r-y), one of at least three proposals; the others are the root m-r-r 'to be bitter' \"\n                 \"(cf. Syriac ܡܪܝܪܐ marrīrā 'bitter') and — favoured by most Semitists and Egyptologists today — Egyptian mry(t) \"\n                 \"'beloved', a name-type common in the Late Bronze Age Delta where the Exodus narrative places her. Klein, whom Nourai \"\n                 \"cites here, refuses to choose: 'Heb. Miryam, which is of uncertain origin.' (b) The arrow from a Syriac/Arabic verb \"\n                 \"'to depart' is backwards in time and unsupported by any of the three references given.\"),\n  \"derivation_fa\": (\"عبریِ מִרְיָם Miryām به‌درستی نیای همهٔ صورت‌های بعدی شناخته شده و دارندهٔ کتاب‌مقدسیِ آن هم خواهر موسی و هارون است (سفر خروج ۱۵:۲۰)؛ \"\n                    \"اما شناسایی دوم در نمودار («مادر عیسی») آمیختنِ دو تن است ــ جفری یادآور می‌شود که خودِ قرآن (۱۹/۲۹، ۳/۳۱، ۶۶/۱۲) این دو را یکی گرفته است، \"\n                    \"ولی در عبری این نام تنها از آنِ خواهر موسی است. مسئلهٔ اصلی دو چیز دیگر است: نخست، معنیِ «سرکشی» خوانشی سنتی و میدراشی است (از מְרִי «سرکشی»، ریشهٔ m-r-y) \"\n                    \"و دست‌کم دو پیشنهاد دیگر در برابر آن هست: ریشهٔ m-r-r «تلخ بودن» (قس. سریانی ܡܪܝܪܐ «تلخ») و ــ که امروز بیشتر سامی‌شناسان و مصرشناسان آن را می‌پسندند ــ \"\n                    \"مصریِ mry(t) «محبوب»، از گونهٔ نام‌هایی که در دلتای مصر در پایان عصر برنز رواج داشت. کلاین، که نورایی همین‌جا به او ارجاع می‌دهد، از داوری می‌پرهیزد: \"\n                    \"«عبری Miryam، که خاستگاهش نامعلوم است». دوم، پیکانی که این نام را از فعلی سریانی/عربی به معنی «دور شدن» بیرون می‌کشد، هیچ‌یک از سه مرجعِ آورده‌شده آن را تأیید نمی‌کند. \"\n                    \"پژوهش امروزی ادعای نورایی را رد می‌کند.\"),\n  \"sources\": [W_MIRIAM, E_MARY, WP_MARYAM],\n  \"ref_check\": [\n    {\"ref\": \"KLN:943\", \"status\": \"partial\",\n     \"note\": \"Klein 1966: 'Miriam, 1) fem. PN., 2) in the Bible, the sister of Moses and Aaron (see Ex. 15:20). — Heb. Miryām. Cp. Mary' and, s.v. Mary, '... fr. Heb. Miryam, which is of uncertain origin.' Klein has the word and the person but explicitly declines the gloss 'rebellion' and knows no Syriac verbal root. (In the two-volume scan on disk the entry sits on leaf 506, which by the file's page formula is nearer p.988 than p.943; the content, not the page, could be verified.)\"},\n    {\"ref\": \"FVQ:262\", \"status\": \"partial\",\n     \"note\": \"Jeffery p.262 confirms that Arabic Maryam 'does go back to the Heb. מרים' and that the Qur'an confuses Miriam with the Virgin, but gives no meaning for the Hebrew name and derives it from nothing.\"},\n    {\"ref\": \"AHD:802,1530\", \"status\": \"not_checked\",\n     \"note\": \"Nourai's AHD page numbers are for the 1975/76 New College Edition, whose scans on archive.org are lending-only; the open local text is Watkins's 1985 Indo-European Roots, which necessarily has no Semitic entry for Miryam (grep -i 'MIRIAM|MARY' in AHD_watkins1985.txt returns only the IE index lines).\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"Klein 1966 s.vv. Mary, Miriam (KLN_1966.txt lines 23034, 24012)\", \"stance\": \"contradicts\",\n     \"note\": \"'fr. Heb. Miryam, which is of uncertain origin' — against the confident gloss 'rebellion' and against any derivation from a verb 'to depart'.\"},\n    {\"src\": \"FVQ\", \"where\": \"Jeffery p.262\", \"stance\": \"partial\", \"note\": \"See the ref_check note: Hebrew origin yes, meaning and Syriac verb no.\"},\n    {\"src\": \"AFA\", \"where\": \"Fraenkel, Aramäische Fremdwörter im Arabischen (AFA.txt)\", \"stance\": \"silent\",\n     \"note\": \"grep -i 'Maryam|Mirjam|Marjam' returns nothing.\"}\n  ]\n})\n\nentry8[\"nodes\"].append({\n  \"id\": 4, \"lang\": \"Aramaic\", \"words\": \"Maryâm\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": (\"Aramaic/Syriac ܡܪܝܡ Maryam is the regular Aramaic shape of Hebrew Miryām: in Aramaic the first vowel is a, and the \"\n                 \"Targumim and the Peshitta write Maryam throughout. Klein states the step explicitly ('fr. Aram. (Targum) Maryam, \"\n                 \"fr. Heb. Miryam'), and Wiktionary's Syriac entry describes ܡܪܝܡ as the Aramaic form of the biblical name. This is \"\n                 \"the form that Greek-speaking Jews and then the Evangelists heard — which is why the Gospels keep the indeclinable \"\n                 \"Μαριάμ beside the Hellenised Μαρία — and the form from which Arabic Maryam was borrowed. The empty-reference node \"\n                 \"is a correct and necessary link in the chain.\"),\n  \"derivation_fa\": (\"«Maryam» آرامی/سریانی صورت منظمِ آرامیِ عبریِ Miryām است: در آرامی واکهٔ نخست a است و ترگوم‌ها و پشیطتا همه‌جا Maryam می‌نویسند. \"\n                    \"کلاین همین مرحله را صریح می‌آورد («از آرامیِ ترگوم Maryam، از عبری Miryam») و ویکی‌واژه هم ܡܪܝܡ سریانی را صورت آرامیِ همین نام می‌داند. \"\n                    \"همین صورت است که یهودیانِ یونانی‌زبان و سپس انجیل‌نویسان شنیدند ــ و به همین سبب در عهد جدید Μαριάμِ صرف‌ناپذیر در کنار Μαρίαِ یونانی‌شده مانده است ــ \"\n                    \"و همین صورت است که به عربی وام داده شده. این گره، هرچند بی‌ارجاع است، حلقه‌ای درست و لازم در زنجیره است. ادعای نورایی درست است.\"),\n  \"sources\": [W_SYRMRYM, W_MIRIAM, WP_MARYAM],\n  \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\",\n     \"note\": \"The node carries no reference of its own; the parent Hebrew node's KLN:943 covers exactly this step ('fr. Aram. (Targum) Maryam, fr. Heb. Miryam').\"}],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. Mary (KLN_1966.txt line 23034)\", \"stance\": \"supports\",\n     \"note\": \"'... fr. L. Maria, fr. Gk. Μαριάμ, Μαρία, fr. Aram. (Targum) Maryam, fr. Heb. Miryam ...'\"},\n    {\"src\": \"FVQ\", \"where\": \"Jeffery p.262\", \"stance\": \"supports\",\n     \"note\": \"'The Gk. Μαριάμ; Syr. ܡܪܝܡ; Eth. ክርያም are equally possible sources, but the probabilities are in favour of its having come from the Syriac' — the Syriac/Aramaic Maryam is attested and is the pivot form.\"}\n  ]\n})\n\nentry8[\"nodes\"].append({\n  \"id\": 5, \"lang\": \"Greek\", \"words\": \"Maria, Mariam\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": (\"Septuagint and New Testament Greek took the Aramaic name over twice: as the indeclinable Μαριάμ Mariam, a bare \"\n                 \"transcription of Aramaic Maryam (so in Luke 1:27 etc. and in the LXX for Moses' sister), and as the declinable, \"\n                 \"Hellenised Μαρία María with the ordinary Greek feminine -α ending; the two alternate in the same Gospel manuscripts. \"\n                 \"Latin took over both (Maria, Mariam), and Maria became the western European name. Klein gives precisely this order: \"\n                 \"'fr. L. Maria, fr. Gk. Μαριάμ, Μαρία, fr. Aram. (Targum) Maryam'. The node is correct, including its listing of both \"\n                 \"Greek variants.\"),\n  \"derivation_fa\": (\"یونانیِ ترجمهٔ سبعینی و عهد جدید این نام آرامی را دو بار گرفته است: یک بار به صورت Μαριάμِ صرف‌ناپذیر که رونویسیِ ساده‌ای از Maryamِ آرامی است \"\n                    \"(در لوقا ۱:۲۷ و در سبعینی برای خواهر موسی) و یک بار به صورت Μαρίαِ یونانی‌شده با پایانهٔ مؤنثِ معمولِ -α که صرف می‌شود؛ این دو در یک دست‌نویس هم کنار هم می‌آیند. \"\n                    \"لاتین هر دو صورت را گرفت (Maria، Mariam) و Maria نام رایج اروپای باختری شد. کلاین دقیقاً همین ترتیب را می‌آورد: «از لاتین Maria، از یونانی Μαριάμ، Μαρία، از آرامیِ ترگوم Maryam». \"\n                    \"این گره، با آوردن هر دو گونهٔ یونانی، درست است.\"),\n  \"sources\": [E_MARY, W_MIRIAM],\n  \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\",\n     \"note\": \"No reference on the node; the child English node's KLN:943 supplies the chain, and Klein names both Greek variants.\"}],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. Mary\", \"stance\": \"supports\", \"note\": \"'fr. Gk. Μαριάμ, Μαρία' — both forms, exactly as the node lists them.\"},\n    {\"src\": \"FVQ\", \"where\": \"Jeffery p.262\", \"stance\": \"supports\", \"note\": \"'The Gk. Μαριάμ ... equally possible sources' — the Greek Mariam is the transcription of the Aramaic form.\"}\n  ]\n})\n\nentry8[\"nodes\"].append({\n  \"id\": 6, \"lang\": \"English\", \"words\": \"Mary, Marilyn, Maria, Marvin; Marianne, marijuana, marihuana\",\n  \"verdict\": \"disputed\",\n  \"derivation\": (\"Four of the seven words are right, one is half right, two are wrong. Right: Mary (ME Marie < OE Maria, Marie < L. \"\n                 \"Maria); Maria (the Late Latin form re-adopted in English); Marilyn (a 20th-c. American diminutive of Mary, Klein: \"\n                 \"'Marilyn, fem. PN. — Dimin. of Mary'); Marianne (Klein: 'Marian is a collateral form of Marion, dimin. of F. Marie, \"\n                 \"but was mistaken later for the compound of the two names Mary and Annie, whence the spelling Marianne') — so Marianne \"\n                 \"does go back to Mary, though through French Marion and a later reanalysis. Half right: marijuana/marihuana — Klein \"\n                 \"derives it from 'Mex. Sp., prob. a contraction of Maria Juana (= ‘Mary Jane’)', but that is the older guess; Etymonline \"\n                 \"records Mexican Spanish marihuana 'of uncertain origin', attested as mariguan in 1894, with the Maria Juana shape only \"\n                 \"an influence on the later spelling — a folk-etymological reshaping, not a derivation. Wrong: Marvin, which has nothing \"\n                 \"to do with Mary: it is the Welsh name Merfyn (Wiktionary: 'from Welsh Merfyn, from mêch ‘marrow’ + myn ‘eminent’'; \"\n                 \"others derive it from Old English Mǣrwine 'famous friend'), attracted to the Mar- names only by accident of English \"\n                 \"spelling. Klein, the node's reference, has no Marvin entry at all.\"),\n  \"derivation_fa\": (\"از هفت واژهٔ این گره، چهارتا درست است، یکی نیمه‌درست و دوتا نادرست. درست‌ها: Mary (از انگلیسی میانه Marie، از انگلیسی کهن Maria/Marie، از لاتین Maria)؛ \"\n                    \"Maria (همان صورت لاتینِ متأخّر که دوباره در انگلیسی به کار رفته)؛ Marilyn (مصغّرِ آمریکاییِ سدهٔ بیستمِ Mary؛ کلاین: «Marilyn، نام زنانه ــ مصغّر Mary»)؛ \"\n                    \"و Marianne که کلاین می‌گوید گونه‌ای از Marion (مصغّر Marieِ فرانسوی) است که بعدها به‌غلط ترکیبِ Mary + Anne فهمیده شد و املای Marianne از همین‌جاست. \"\n                    \"نیمه‌درست: marijuana/marihuana؛ کلاین آن را «اسپانیاییِ مکزیکی، احتمالاً کوتاه‌شدهٔ Maria Juana» می‌داند، ولی این حدسِ کهنه است: در اتیمولوجی‌آنلاین آمده که \"\n                    \"marihuanaِ مکزیکی «خاستگاه نامعلوم» دارد و صورت کهن‌ترش mariguan (۱۸۹۴ م.) است و «ماریا خوانا» فقط ریشه‌شناسیِ عامیانه‌ای است که بر املای بعدی اثر گذاشته. \"\n                    \"نادرست: Marvin، که هیچ پیوندی با Mary ندارد؛ این نام از Merfynِ ولزی است (ویکی‌واژه: از mêr «مغز استخوان» + myn «برجسته»)، یا به نظر برخی از Mǣrwineِ انگلیسی کهن، \"\n                    \"و تنها به تصادفِ املای -Mar با نام‌های مریم‌تبار هم‌شکل شده است. کلاین، که مرجعِ این گره است، اصلاً مدخلی به نام Marvin ندارد. \"\n                    \"پس بخشی از ادعای نورایی درست و بخشی را پژوهش امروزی رد می‌کند.\"),\n  \"sources\": [E_MARY, E_MARIJ, W_MARVIN],\n  \"ref_check\": [\n    {\"ref\": \"KLN:943\", \"status\": \"partial\",\n     \"note\": \"Klein 1966 (leaf 504-506) supports Mary, Maria, Marilyn and Marianne verbatim: 'Mary, fem. PN. — ME. Marie, fr. OE. Maria, Marie, fr. L. Maria ...'; 'Maria, fem. PN. — Late L. See Mary'; 'Marilyn, fem. PN. — Dimin. of Mary'; 'Marian, Marianne, fem. PN. — Marian is a collateral form of Marion, dimin. of F. Marie (see Mary) ...'; 'marihuana, marijuana ... Mex. Sp., prob. a contraction of Maria Juana'. But Klein has NO entry for Marvin (grep '^Marvin' in both KLN_1966.txt and KLN_1971.txt returns nothing), so his page cannot support that word.\"},\n    {\"ref\": \"AHD:802\", \"status\": \"not_checked\",\n     \"note\": \"The 1975/76 AHD New College Edition is only on archive.org as a lending copy; the open Watkins 1985 root book has no entry for any of these names (its index lists no MARY/MARVIN).\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"Klein 1966, leaves 504 and 506 (entries Maria, Marian/Marianne, marihuana/marijuana, Marilyn, Mary)\", \"stance\": \"partial\",\n     \"note\": \"See the ref_check quotations; Klein supports four of the words, gives the now-superseded Maria Juana etymology for the fifth, and is silent on Marvin.\"},\n    {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls (FSD_vol3.txt)\", \"stance\": \"silent\",\n     \"note\": \"grep -i 'marihuana' returns nothing in the volume on disk — the 1913 plates predate the word's entry into English (1918).\"},\n    {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etymological Dictionary (SKT.txt)\", \"stance\": \"silent\",\n     \"note\": \"Skeat's dictionary excludes personal names; no Mary/Marvin/marijuana entry.\"}\n  ]\n})\n\nout = {\n  \"pdf_page\": 426,\n  \"book_page\": 396,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-13\",\n  \"entries\": [entry1, entry8]\n}\n\nwith io.open('/home/sfmqrb/git/rishe/data/verification/page-426.json','w',encoding='utf-8') as f:\n    json.dump(out, f, ensure_ascii=False, indent=2)\n    f.write('\\n')\nprint('written')\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-426.py",
 "description": "Build page-426 verification JSON"
}
```


### [2026-09-14T01:40:16.220Z] TOOL RESULT

```
written
```


## [2026-09-14T01:40:19.746Z] TOOL CALL #69: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-426.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 426",
 "description": "Validate and run verify_check"
}
```


### [2026-09-14T01:40:21.018Z] TOOL RESULT

```
JSON OK
nodes verified: 14/14
node verdicts: {'plausible': 5, 'confirmed': 6, 'disputed': 3}
root verdicts: {'confirmed': 1, 'disputed': 1}
ref checks: {'supports': 5, 'not_checked': 8, 'partial': 4, 'contradicts': 1}
books consulted: {'supports': 20, 'contradicts': 4, 'partial': 9, 'silent': 8} | by book: {'KLN': 6, 'POK': 4, 'FSD': 4, 'FVQ': 4, 'KNT': 2, 'HUB': 2, 'SYN': 2, 'SKT': 2, 'AHD': 2, 'MON': 2, 'BRT': 1, 'PHD': 1, 'NYB': 1, 'HRN': 1, 'ARY': 1, 'IEC': 1, 'SOD': 1, 'BQT': 1, 'AFM': 1, 'PLA': 1, 'AFA': 1}
```


## [2026-09-14T01:40:26.143Z] TOOL CALL #70: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport json,io\np='data/verification/page-426.json'\nd=json.load(open(p,encoding='utf-8'))\ns=json.dumps(d,ensure_ascii=False)\nprint('mêch' in s)\ns=s.replace('mêch','mêr')\nd=json.loads(s)\nwith io.open(p,'w',encoding='utf-8') as f:\n    json.dump(d,f,ensure_ascii=False,indent=2); f.write('\\n')\nEOF\npython3 tools/verify_check.py 426 | tail -3",
 "description": "Fix typo and re-check"
}
```


### [2026-09-14T01:40:27.336Z] TOOL RESULT

```
True
root verdicts: {'confirmed': 1, 'disputed': 1}
ref checks: {'supports': 5, 'not_checked': 8, 'partial': 4, 'contradicts': 1}
books consulted: {'supports': 20, 'contradicts': 4, 'partial': 9, 'silent': 8} | by book: {'KLN': 6, 'POK': 4, 'FSD': 4, 'FVQ': 4, 'KNT': 2, 'HUB': 2, 'SYN': 2, 'SKT': 2, 'AHD': 2, 'MON': 2, 'BRT': 1, 'PHD': 1, 'NYB': 1, 'HRN': 1, 'ARY': 1, 'IEC': 1, 'SOD': 1, 'BQT': 1, 'AFM': 1, 'PLA': 1, 'AFA': 1}
```


## [2026-09-14T01:40:48.350Z] AGENT

Page 426 (book p. 396) verified — `data/verification/page-426.json`, `verify_check.py 426` shows 0 PROBLEM lines, 14/14 nodes.

**Counts**: roots — 1 confirmed (Rk-tho, Rk-so), 1 disputed (R.y.m). Nodes — 6 confirmed, 5 plausible, 3 disputed. Ref checks: 5 supports, 4 partial, 1 contradicts, 8 not_checked. 8 web pages archived via `fetch_source.py`; 21 local books consulted.

**Disputed items**
- ROOT `R.y.m` [Syriac] "to depart" — r-y-m is an **Arabic** root (< PSem *rayam-), not Syriac; Syriac has no such verb, and Maryam is not derived from it. Nourai's own ref SAP:617 (Sayyah = Persian al-Munjid) is an Arabic dictionary.
- `#1 Arabic r.y.m; Maryam` — Jeffery FVQ:262, the node's own reference, quotes the *mafʿal* < *rāma* analysis (al-Jawharī, Lisān xv.152) only to reject it: Arabic Maryam < Syriac ܡܪܝܡ < Heb. Miryām.
- `#3 Hebrew Miryâm "rebellion"` — Klein (KLN:943) says "of uncertain origin"; modern preference is Egyptian *mry* "beloved" or Sem. m-r-r "bitter"; "rebellion" is the midrashic gloss.
- `#6 English Mary… Marvin… marijuana` — **Marvin** is Welsh Merfyn / OE Mǣrwine, unrelated (Klein has no Marvin entry); **marijuana** is Mex. Sp. of uncertain origin (attested *mariguan* 1894), "María Juana" being folk-etymological influence only.

**Notable plausible calls**
- `#1 Avestan areša-ama` / `#2 Persian Aršâm`: "bear's strength" is Bartholomae's (AiW col. 203-4) and Mo'in's reading — BQT:31 and BQT:733 both check out verbatim — but Kent §1914 and current onomastics read Aršāma- as *aršan-* "hero" + *ama* "strength". Also NP خرس is a sister form via OP *r̥šah- > MP xirs, not a descendant of Avestan (prothetic x-: Hübschmann §162; s not š: §129, Pokorny 875).
- `#6 Celtic "artho"` — no attested Celtic form; Proto-Celtic is *artos (Welsh arth). Printed page reads "artho", so this is the book, not the extraction.
- `#7 Arthur` — Celtic *arto- derivation is Watkins/AHD's, but Latin Artorius is an equally live account.

**Extraction errors**: none. The rendered PDF page matches the JSON exactly (including خرس, ارشام ( آرشام ), `ššh, and the Rumi quote).

**Unverifiable refs**: SAP:617 (no copy anywhere), MON:4053 (Mo'in aʿlām vols 5-6, not online/on disk), AHD:802,1530 (1975/76 New College Edition is lending-only; local AHD is Watkins 1985, IE roots only). Note also that Klein's Mary/Miriam entries sit near p.988 by our scan's page formula, not p.943 — content verified, page number not.
