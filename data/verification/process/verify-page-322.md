# Verification process log — verify-page-322


## [2026-09-07T15:49:14.922Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 322 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-322.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-322.json. Write /home/sfmqrb/git/rishe/data/verification/page-322.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 322` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-07T15:49:17.173Z] AGENT

I'll start by reading the instructions.


## [2026-09-07T15:49:17.880Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-07T15:49:17.896Z] TOOL RESULT

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


## [2026-09-07T15:49:18.529Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-322.txt"
}
```


### [2026-09-07T15:49:18.549Z] TOOL RESULT

```
1	=== PDF page 322 (book page 292) ===
2	--- entry 0 ---
3	ROOT [Aramaic] Masgdâ : place of worship  (refs KLN:1007; VDQ:379)
4	#1 (parent #0) [Arabic] refs=KLN:1007 | masjed : mosque ; s.j.d : to prostrate, pray to God | NOTE: FVF:638 claims that Arabic "masjed" is from Persian "mazget"
5	  #2 (parent #1) [Persian] refs=FVA:185 | sojŭd «سجود ( سجده )» : prostration ; sâjed «ساجد ( سجّاد ، سجّاده )» : one who prays to God ; masjed «مسجد» : place of prayers, mosque
6	  #3 (parent #1) [Spanish] refs=KLN:1007 | mesquita : mosque
7	    #4 (parent #3) [Italian] refs=None | moschea
8	      #5 (parent #4) [French] refs=KLN:1007 | mosquee : mosque
9	        #6 (parent #5) [English] refs=KLN:1007 | mosque
10	#7 (parent #0) [Persian] refs=BQT:2001; FVF:638; MON:4063 | mazget : mosque | extra: مزگت ، مزکت
11	--- entry 1 ---
12	ROOT Massa -> redirect to M.s.s
13	--- entry 2 ---
14	ROOT Mâ-ter -> redirect to Mâ
15	--- entry 3 ---
16	ROOT Mazaxa -> redirect to Madhaxa
17	--- entry 4 ---
18	ROOT Mbh -> redirect to Nobh
19	--- entry 5 ---
20	ROOT Mbhi -> redirect to Ambhi
21	--- entry 6 ---
22	ROOT [Indo-European] Mě 1 : no, not  (refs POK:703; KNT:210)
23	#1 (parent #0) [Avestan / Old Persian] refs=POK:703; KNT:201 | mâ 2 : no, not ; mâ-tya : that not, lest
24	  #2 (parent #1) [Persian] refs=MON:3677 | ma- «مَ-» : a prefix negating verbs | extra: مرو ، مگو ، مباد
25	#3 (parent #0) [Sanskrit] refs=POK:703 | mâ : no, not
26	#4 (parent #0) [Greek] refs=POK:703 | mě : no, not
27	
```


## [2026-09-07T15:49:23.645Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-322.json | python3 -m json.tool | head -200",
 "description": "Read source JSON for page 322"
}
```


## [2026-09-07T15:49:24.174Z] TOOL CALL #4: Bash

```json
{
 "command": "sed -n 1,200p data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-07T15:49:25.096Z] TOOL RESULT

```
{
    "pdf_page": 322,
    "book_page": 292,
    "entries": [
        {
            "root": {
                "name": "Masgd\u00e2",
                "lang": "Aramaic",
                "refs": "KLN:1007; VDQ:379",
                "gloss": "place of worship"
            },
            "nodes": [
                {
                    "id": 1,
                    "parent": 0,
                    "lang": "Arabic",
                    "refs": "KLN:1007",
                    "words": [
                        {
                            "translit": "masjed",
                            "gloss": "mosque",
                            "script": null
                        },
                        {
                            "translit": "s.j.d",
                            "gloss": "to prostrate, pray to God",
                            "script": null
                        }
                    ],
                    "note": "FVF:638 claims that Arabic \"masjed\" is from Persian \"mazget\"",
                    "quote": null
                },
                {
                    "id": 2,
                    "parent": 1,
                    "lang": "Persian",
                    "refs": "FVA:185",
                    "words": [
                        {
                            "translit": "soj\u016dd",
                            "gloss": "prostration",
                            "script": "\u0633\u062c\u0648\u062f ( \u0633\u062c\u062f\u0647 )"
                        },
                        {
                            "translit": "s\u00e2jed",
                            "gloss": "one who prays to God",
                            "script": "\u0633\u0627\u062c\u062f ( \u0633\u062c\u0651\u0627\u062f \u060c \u0633\u062c\u0651\u0627\u062f\u0647 )"
                        },
                        {
                            "translit": "masjed",
                            "gloss": "place of prayers, mosque",
                            "script": "\u0645\u0633\u062c\u062f"
                        }
                    ],
                    "note": null,
                    "quote": {
                        "text": "\u0647\u0645\u0647 \u06a9\u0633 \u0637\u0627\u0644\u0628 \u06cc\u0627\u0631\u0646\u062f \u0686\u0647 \u0647\u0634\u06cc\u0627\u0631 \u0648 \u0686\u0647 \u0645\u0633\u062a - \u0647\u0645\u0647 \u062c\u0627 \u062e\u0627\u0646\u0647\u0654 \u0639\u0634\u0642\u0633\u062a \u0686\u0647 \u0645\u0633\u062c\u062f \u0686\u0647 \u06a9\u0650\u0646\u0650\u0634\u062a",
                        "poet": "H\u00e2fez"
                    }
                },
                {
                    "id": 3,
                    "parent": 1,
                    "lang": "Spanish",
                    "refs": "KLN:1007",
                    "words": [
                        {
                            "translit": "mesquita",
                            "gloss": "mosque",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 4,
                    "parent": 3,
                    "lang": "Italian",
                    "refs": null,
                    "words": [
                        {
                            "translit": "moschea",
                            "gloss": null,
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 5,
                    "parent": 4,
                    "lang": "French",
                    "refs": "KLN:1007",
                    "words": [
                        {
                            "translit": "mosquee",
                            "gloss": "mosque",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 6,
                    "parent": 5,
                    "lang": "English",
                    "refs": "KLN:1007",
                    "words": [
                        {
                            "translit": "mosque",
                            "gloss": null,
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 7,
                    "parent": 0,
                    "lang": "Persian",
                    "refs": "BQT:2001; FVF:638; MON:4063",
                    "words": [
                        {
                            "translit": "mazget",
                            "gloss": "mosque",
                            "script": null
                        }
                    ],
                    "script_extra": "\u0645\u0632\u06af\u062a \u060c \u0645\u0632\u06a9\u062a",
                    "note": null,
                    "quote": {
                        "text": "\u0633\u062e\u0646 \u062f\u0648\u0632\u062e\u06cc \u0631\u0627 \u0628\u0647\u0634\u062a\u06cc \u06a9\u0646\u062f - \u0633\u062e\u0646 \u0645\u0632\u06af\u062a\u06cc \u0631\u0627 \u06a9\u0646\u0634\u062a\u06cc \u06a9\u0646\u062f",
                        "poet": "Asad\u00ee"
                    }
                }
            ]
        },
        {
            "root": {
                "name": "Massa",
                "redirect": "M.s.s"
            },
            "nodes": []
        },
        {
            "root": {
                "name": "M\u00e2-ter",
                "redirect": "M\u00e2"
            },
            "nodes": []
        },
        {
            "root": {
                "name": "Mazaxa",
                "redirect": "Madhaxa"
            },
            "nodes": []
        },
        {
            "root": {
                "name": "Mbh",
                "redirect": "Nobh"
            },
            "nodes": []
        },
        {
            "root": {
                "name": "Mbhi",
                "redirect": "Ambhi"
            },
            "nodes": []
        },
        {
            "root": {
                "name": "M\u011b 1",
                "lang": "Indo-European",
                "refs": "POK:703; KNT:210",
                "gloss": "no, not"
            },
            "nodes": [
                {
                    "id": 1,
                    "parent": 0,
                    "lang": "Avestan / Old Persian",
                    "refs": "POK:703; KNT:201",
                    "words": [
                        {
                            "translit": "m\u00e2 2",
                            "gloss": "no, not",
                            "script": null
                        },
                        {
                            "translit": "m\u00e2-tya",
                            "gloss": "that not, lest",
                            "script": null
                        }
```


### [2026-09-07T15:49:25.137Z] TOOL RESULT

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


## [2026-09-07T15:49:45.386Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['KLN','VDQ','FVF','FVA','BQT','MON','POK','KNT','FVQ','AFM','PLA','AFA','LKT','HRN','HUB','PHD','NYB','BRT','ARY','TAD','ARB']:\n    v=d.get(k)\n    print('==',k, json.dumps(v,ensure_ascii=False)[:900])\n\"",
 "description": "Inspect refs_online entries"
}
```


## [2026-09-07T15:49:46.815Z] TOOL CALL #6: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo ---- && python3 -c \"\nimport json;d=json.load(open('data/verification/page-317.json'));print(json.dumps(d['entries'][0],ensure_ascii=False,indent=1)[:3000])\"",
 "description": "Look at an existing verification file"
}
```


### [2026-09-07T15:49:46.872Z] TOOL RESULT

```
== KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based l
== VDQ {"title": "Fereydun Badreh'i (tr.), Vazheha-ye Dakhil dar Qor'an-e Majid (Persian translation of Jeffery FVQ with notes), Toos 1372/1993", "kind": "website", "url": "https://noorlib.ir/book/view/12868?pageNumber=<N>&viewType=pdf (page images; viewType=html also exists) ; info: https://noorlib.ir/book/info/12868 ; ketabnak.com/book/51136 (download blocked)", "lookup_hint": "noorlib viewer is JavaScript-rendered (WebFetch/curl get only the site chrome); needs a browser. Since it is a translation of FVQ, verify the substance via FVQ (same entry order); page numbers differ.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "Not on archive.org. Also on ghaemiyeh (ghbook.ir) as an app/EPUB per news reports.", "cites": "page number of the Persian translation of Jeffery's Foreign Vocabulary of the Qurʾān"}
== FVF {"title": "S.M.A. Emam Shushtari, Farhang-e Vazheha-ye Farsi dar Zaban-e Arabi, Anjoman-e Asar-e Melli 58, Tehran 1347/1968", "kind": "website", "url": "https://noorlib.ir/book/info/105056 (page viewer: https://noorlib.ir/book/view/105056?pageNumber=<N>&viewType=pdf) ; https://ketabnak.com/book/48613 (818 pp. PDF, login) ; http://parsianjoman.org/?p=1265 (download post)", "lookup_hint": "Alphabetical by Persian headword; noorlib page number N is the scan page — browser needed to read. Not on archive.org.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "PDF exists on several Iranian sites (ketabnak/parsianjoman) but could not be fetched here (login/JS)."}
== FVA {"title": "S.M. Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (dakhil), Tohi/Azadi 1368/1989", "kind": "catalog", "url": "https://openlibrary.org/works/OL4602367W (edition OL2012991M: Intisharat-i Islami 1368/1989, 582 pp)", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: no digital copy found.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: still no digital copy on any permitted platform. Library catalogues list the 1368 book under the variant title «فرهنگ ریشهٔ وام‌واژه‌های عربی (لغات عربی مستعمل در فارسی دخیل)» — reconcile with Nourai's title when buying. Catalogue record only."}
== BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.c
== MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different paginati
== POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry
== KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Lexicon (Part III, pp. 164 ff.) headwords are transliterated OP words at line start followed by part of speech, e.g. grep -n '^apadana-' ; sec
== FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ.txt"], "page_offset": "printed page = leaf − 17 (0-based \\f blocks in FVQ_pages.txt; 335 leaves)", "covers_etymology": true, "notes": "Good English OCR (Arabic script garbled). Same 1938 edition Nourai cites.", "cites": "page number of Jeffery, The Foreign Vocabulary of the Qurʾān (19
== AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM.txt"], "page_offset": "198 leaves; page numerals OCR'd unreliably — offset approx leaf − 8 (front matter); confirm on page image", "covers_etymology": true, "notes": "Arabic OCR fair; Syriac/Latin etyma partially garbled.", "
== PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 leaves (pdftotext -layout, \\f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276).", "lookup_hint": "HathiTrust search-only; Google Books id q_ErAAAAMAAJ snippet view; DDB has only the table of contents. No full text online. | For pages in a scanned volume use: python3 tools/ref_page.py P
== AFA {"title": "S. Fraenkel, Die aramäischen Fremdwörter im Arabischen, Leiden 1886 (repr. Hildesheim 1962, same pagination)", "edition_found": "1886", "kind": "archive_djvu", "url": "https://archive.org/details/diearamischenfr00fraegoog", "identifier": "diearamischenfr00fraegoog (also bub_gb_SzdbAAAAQAAJ)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AFA.txt", "page_offset": "leaf = printed + 30 (e.g. leaf 38 = p.8). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Arabic/Aramaic in script (not OCRed) with German glosses; grep the German meaning or transliteration.", "notes": "Built from djvu.xml."}
== LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 'NNNN. word (language) meaning' - Lokotsch is usually cited by entry number, but Nourai cites pages. grep the oriental source word in transliteration or the number.", "notes": "", "cites": "entry number of Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs (1927)"}
== HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.", "notes": "OCR of German Fraktur-free text is decent; Persian
== HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number.", "notes": "Built from djvu.xml (no hocr); OCR quality moderate.", "cites": "page number of Hübschmann, Persische Studien (1895)"
== PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsian
== NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates and 'Bthl.' refs.", "notes": " local_files: /home/sfmqrb/
== BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Nourai's BRT numbers are Bartholomae's COLUMN number
== ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt"], "page_offset": "printed page = pdf page + 1
== TAD {"title": "Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-hurufihi (2nd ed. Cairo 1932, ed. Yusuf Tuma al-Bustani; later Library of Lebanon reprint) — Nourai lists it under Arabic authors ('Unaysi T.'); its Table IV line was lost in the OCR", "kind": "archive_djvu", "url": "https://archive.org/details/TOB1932ARAR (1932 ed.); also https://archive.org/details/ar113lang79 and https://archive.org/details/elshandawily14640", "lookup_hint": "Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; inside.php search works.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD.txt"], "page_offset": "86 leaves (small book, ~80 printed pages); offset ≈ leaf − 4..6, verify against the printed numeral on the pa
== ARB {"title": "al-Jawaliqi, al-Mu'arrab min al-kalam al-a'jami, Tehran 1966 (reprint of Ahmad M. Shakir's Cairo 1361/1942 edition)", "kind": "archive_djvu", "url": "https://archive.org/details/mo3rb (probably the Shakir edition) ; https://archive.org/details/almo3rab_gwaliqy_f_abduraheem (F. 'Abd al-Rahim ed., Damascus 1990) ; also uc1.aa0003615705 / AAlexandrina-148752 (Sachau's Leipzig 1867 ed.) ; text on shamela.ws", "lookup_hint": "Alphabetical Arabic headwords; grep in ARB_mo3rb.txt / ARB_abdulraheem.txt (raw, no page breaks); edition of mo3rb not confirmed — check its title page image.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/ARB_mo3rb.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/ARB_abdulraheem.txt"], "page_offset": null, "covers_etymology": true, "notes": "Arabic OCR fair."}
```


### [2026-09-07T15:49:48.346Z] TOOL RESULT

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
----
{
 "entry": 0,
 "root": "Mad",
 "verdict": "confirmed",
 "modern_form": "PIE *mad- (laryngealist *meh₂d-) 'wet, dripping; fat, well-fed', with the derived sense 'food, fattening' — Pokorny 694-695",
 "note": "The root is genuine and standard. Pokorny 694-695 has 'Root/lemma: mad-  Meaning: wet; glossy, fat, well-fed, intoxicating', and Watkins/AHD (1985 ed., p. 38) has 'mad-. Moist, wet; also refers to various qualities of food' — Nourai's gloss 'wet, also food' is essentially Watkins' wording, and the language label 'Indo-European' is right. Walde-Pokorny II 230-232 is the same article. What is remarkable is that Pokorny's article contains almost the whole of Nourai's chart in the same order: 'ai. madati, madate … mada- m. Rauschtrank = av. maδa-; ai. madgu- ein bestimmter Wasservogel, ein Fisch = np. māγ ein Wasservogel; ai. matsya- m., av. masya Fisch (der nasse; Ableitung von einem -es-St. *mades-); mastu- n. saurer Rahm (*mad-stu-) … arm. macun sauer, geronnene Milch … iran. Worte für Dickmilch, so npers. mast, masīdan … lat. madeō, mattus trunken (*madi-to-s) … ahd. mast Futter, got. mats Speise, ags. mete, mnd. mat(e) Kamerad'. Two modern caveats: (a) Cheung (2007) and LIV split the family into *mad¹ 'to become intoxicated' (PIE *med-) and a separate Indo-Iranian *mad 'to curdle', for which no PIE root is set up; (b) the 'fish' member is no longer taken as certain (see node #1).",
 "note_fa": "ریشهٔ هندواروپایی آغازین *mad- (در نگارش امروزی *meh₂d-) به معنی «خیس، تر، چکه‌کننده؛ فربه و پرورده» و از همین‌جا «خوراک»، ریشه‌ای شناخته و پذیرفته است: پوکورنی (ص ۶۹۴–۶۹۵) آن را با معنی «تر؛ چرب، فربه، مست‌کننده» می‌آورد و واتکینز در پیوست فرهنگ American Heritage نیز «mad-. نمناک، تر؛ همچنین دربارهٔ کیفیت‌های خوراک» دارد؛ پس برچسب زبانی و معنای «wet, also food» در نمودار نورایی درست است. نکتهٔ چشمگیر آنکه تقریباً همهٔ شاخه‌های نمودار — سنسکریت madati و mada-، اوستایی maδa-، سنسکریت madgu- برابر «ماغ» فارسی، سنسکریت mastu- و ارمنی macun برابر «ماست» و «ماسیدن»، لاتینی mattus و واژه‌های ژرمنی mast/mats/mete/mate — همه در همان مقالهٔ پوکورنی و به همان ترتیب آمده‌اند، یعنی نورایی مستقیماً از پوکورنی و واتکینز برداشته است. دو نکتهٔ احتیاطی: نخست آنکه چونگ (۲۰۰۷) و فرهنگ LIV دو ریشهٔ *mad «مست شدن» و *mad «بستن، دلمه شدن» را از هم جدا می‌کنند و برای دومی ریشهٔ هندواروپایی نمی‌سازند؛ دوم آنکه پیوند واژهٔ «ماهی» با این ریشه امروز قطعی دانسته نمی‌شود (بنگرید به گرهٔ ۱).",
 "sources": [
  "https://en.wiktionary.org/wiki/mattus",
  "https://en.wiktionary.org/wiki/meat"
 ],
 "ref_check": [
  {
   "ref": "POK:694",
   "status": "supports",
   "note": "POK_full.txt line 57036 ff. (= POK_02.txt line 5645 ff., German original): 'Root/lemma: mad-  Meaning: wet; glossy, fat, well-fed, intoxicating … References: WP. II 231 f., WH. II 6 f.  Page(s): 694-695'. The page number Nourai cites is exactly right, and the article's material list is the source of his whole chart."
  }
 ],
 "consulted": [
  {
   "src": "WLD",
   "where": "Bd. II 230-232 s.v. 'mad-'",
   "stance":
```


## [2026-09-07T15:50:01.941Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN 1966 mosque ===\"; grep -n -i \"mosque\" KLN_1966.txt | head -20\necho \"=== KLN 1971 mosque ===\"; grep -n -i \"mosque\" KLN_1971.txt | head -20\necho \"=== KLN masjid/sajada ===\"; grep -n -i \"masjid\\|sajada\\|mesquita\\|moschea\" KLN_1966.txt KLN_1971.txt | head -30",
 "description": "Grep Klein for mosque"
}
```


### [2026-09-07T15:50:02.056Z] TOOL RESULT

```
=== KLN 1966 mosque ===
18761:imagine,  tr.  and  intr.  v.  —  ME.,  fr.  MF.  (=F.) imaginer,  fr.  L.  imaginari,  ‘to  picture  to  oneself, imagine’,  fr.  imago,  gen.  -inis;  see  image.  L. imaginari  is  prop,  a  loan  translation  of  Gk. <pavTd^EaOai,  ‘to  become  visible,  imagine’.  See image.  Derivative:  imagin-er,  n. imago,  n„  the  final  stage  of  an  insect  ( entomol .)  — L.  imago,  ‘picture’.  See  image, imam,  also  imaum,  n.,  1)  the  leading  priest  in  a Moslem  mosque;  2)  religious  leader  of  Islam.  — Arab,  imim,  ‘leader’,  lit.  ‘one  who  precedes',  fr. drnma,  ‘he  preceded’.
20519:Kaaba,  n.,  the  cube-shaped  building  in  the  Great Mosque  of  Mecca  containing  the  Black  Stone of  Mecca.  —  Arab.  ka‘bah,  ‘square  house’,  fr. ka‘b,  ‘cube’.  Cp.  cube.
23047:mashie,  mashy,  n.,  an  iron  golf  club.  —  Prob.  fr. F.  massue,  ‘club’,  fr.  VL.  *mattiuca,  fr.  *mat- tia,  which  is  rel.  to  L.  mateola,  ‘a  tool  for  dig¬ ging'.  See  mace,  ‘a  staff’,  and  cp.  masse,  mattock, masjid,  n.,  a  mosque.  —  Arab.  See  mosque, mask,  n.  —  MF.  (=  F)  masque,  fr.  ML.  masca, fr.  It.  maschera,  fr.  Arab.  maskharah,  ‘mockery; buffoon’,  fr.  sdkhira,  ‘he  mocked,  ridiculed’. Cp.  masque,  masquerade.
23475:—  Heb.  mlnorah,  ‘candlestick’,  from  stem  n-w-r, ‘to  give  light,  shine’,  whence  also  ner,  ‘lamp’ ;  rel. to  Aram. -Syr.  nur,  ‘fire’,  Arab,  nara,  ‘shone’, nur,  ‘light’,  nar,  ‘fire’,  Aram,  mfnarta,  ‘candle¬ stick’,  Arab.  manarah,  ‘candlestick;  lighthouse; tower  of  a  mosque’,  Akkad,  nuru,  ‘light’,  nawa- ru,  namaru,  ‘to  give  light,  shine".  Cp.  the  second element  in  Abner.  Cp.  also  minaret  and  the  last element  in  Koh-i-noor.
23647:Derivative:  Mesozoic,  n. mesquin,  adj.,  mean,  sordid.  —  F.,  fr.  It.  meschi- no,  fr.  Arab,  miskin  (in  VArab.  pronunciation mesktn),  ‘poor,  wretched,  miserable’,  which  is borrowed  fr.  Heb.  or  Aram,  misken  or  Syr. mesken,  ‘poor’,  which  are  perh.  loan  words  fr. Akkad,  mushkenu,  ‘beggar,  needy’, mesquite,  n.,  a  mosque  (obsol.)  —  Sp.  mesquita (ModSp.  mezquita),  ‘mosque’.  See  mosque, mesquite,  also  mesquit,  n.,  either  of  two  shrubs  of the  pea  family.  —  Sp.  mezquite,  fr.  Nahuatl  miz- quitl.
23873:mihrab,  n.,  in  a  mosque,  the  niche  indicating  the direction  of  Mecca.  —  Arab,  mihrab. mikado,  n.,  the  emperor  of  Japan  (a  title  used  by non-Japanese).  —  Jap.,  compounded  of  mi,  ‘au¬ gust’,  and  kado,  ‘gate’.  Cp.  Pharaoh,  the  title  of the  Egyptian  kings,  which  lit.  means  ‘great house’,  and  the  Sublime  Porte,  as  the  official name  of  the  Turkish  Government.
23928:mimbar,  n.,  the  pulpit  in  a  mosque.  —  Arab. minbar,  ‘pulpit’,  which  orig.  denoted  ‘an  (ele¬ vated)  seat’,  and  is  a  loan  word  fr.  Ethiop.  min¬ bar,  ‘seat’,  fr.  nabara,  ‘he  was  sitting’.  Ethiop. nabara  is  rel.  to  Arab,  nabara,  ‘he  raised,  ele¬ vated’.  For  sense  development  cp.  Arab,  jalasa, ‘he  sat  down,  was  sitting’,  julus,  ‘sitting,  sitting down;  accession  to  the  throne’.  See  Theodor Noldeke,  Lehnworter  in  und  aus  dem  Athiopi- schen,  in  his  Neue  Beitrage  zur  semitischen Sprachwissenschaft,  Strassburg,  1910,  p.  49.  Cp. almemar.
23949:Minaean,  adj.  —  Formed  with  suff.  -an  fr.  L. Minaei  (pi.),  a  people  in  South  Arabia,  fr.  Gk. Mtvsiot,  fr.  Arab.  Ma'am,  they  are  mentioned in  the  Bible  under  the  names  of  M  'untm  (I  Chr. 4  :  41,  II  Chr.  26  :  7)  and  Ma'Sn  (Judg.  10  :  12). minaret,  n.,  a  slender  tower  attached^  to  a mosque.  —  Sp.  minarete,  fr.  Turk,  menaret,  fr. Arab.  manarah,  ‘candlestick ;  tower  of  a  mosque, lighthouse’,  fr.  nara,  ‘it  lighted’,  rel.  to  Heb. ner,  ‘lamp’,  mlndrdh,  Aram.  mlnartd,  ‘candle¬ stick’.  See  Menorah.
24478:mosque,  n.,  a  Mohammedan  place  of  worship.  — F.  mosquee,  fr.  It.  moschea,  fr.  earlier  moscheta, fr.  Sp.  mesquita  (whence  ModSp.  mezquita),  fr. Arab,  masjid,  ‘place  of  worship,  mosque’,  which is  either  borrowed  fr.  Nabatean  masgedha, ‘place  of  worship’,  or  formed  independently, with  ma-,  a  pref.  denoting  place,  fr.  sdjada,  ‘he was  submissive,  prostrated  himself  in  prayer’, which  is  rel.  to,  or — more  prob. — borrowed from  Aram,  s^ghedh,  of  s.m.  Cp.  masjid,  mes- quite.
24579:muezzin,  n.,  in  Mohammedan  countries,  an  offi¬ cial  who,  from  the  minaret  of  the  mosque,  calls the  people  to  prayer.  —  Arab,  mu'  adhdhiti,  prop, active  part,  of  adhdhana,  II  (=  frequentative  or intensive)  conjugation  of  adhana,  ‘he  proclaim¬ ed’,  fr.  udhn,  ‘ear’,  which  is  rel.  to  Ethiop.  ezn, Heb.  Szen,  Aram,  udhna,  Syr.  edhnd,  Akkad. uznu,  ‘ear’,  Heb.  he'lzln,  ‘he  gave  ear,  heard, listened,  hearkened’.
=== KLN 1971 mosque ===
120074:Moslem mosque ; 2) religious leader of Islam. — 
130251:Mosque of Mecca containing the Black Stone 
146004:masjid, n., a mosque. — Arab. See mosque, 
148918:tower of a mosque’, Akkad, nuru, ‘light’, nawa- 
149811:raesqutte, n., a mosque ( obsol .) — Sp. mesquita 
149812:(ModSp. mezquita), ‘mosque’. See mosque, 
151326:mihrab, n., in a mosque, the niche indicating the 
151715:mimbar, n., the pulpit in a mosque. — Arab. 
151809:mosque. — Sp. m inarete, fr. Turk, menaret , fr. 
151810:Arab. mandra h , ‘candlestick ; tower of a mosque, 
155503:mosque, n., a Mohammedan place of worship. — 
155504:F. mosquee, fr. It. moschia, fr. earlier moscheta, 
155506:Arab, mdsjid, ‘place of worship, mosque’, which 
156156:cial who, from the minaret of the mosque, calls 
=== KLN masjid/sajada ===
KLN_1971.txt:146004:masjid, n., a mosque. — Arab. See mosque, 
KLN_1971.txt:149811:raesqutte, n., a mosque ( obsol .) — Sp. mesquita 
KLN_1971.txt:155512:from Aram. s i ghedh, of s.m. Cp. masjid, mes- 
KLN_1966.txt:23047:mashie,  mashy,  n.,  an  iron  golf  club.  —  Prob.  fr. F.  massue,  ‘club’,  fr.  VL.  *mattiuca,  fr.  *mat- tia,  which  is  rel.  to  L.  mateola,  ‘a  tool  for  dig¬ ging'.  See  mace,  ‘a  staff’,  and  cp.  masse,  mattock, masjid,  n.,  a  mosque.  —  Arab.  See  mosque, mask,  n.  —  MF.  (=  F)  masque,  fr.  ML.  masca, fr.  It.  maschera,  fr.  Arab.  maskharah,  ‘mockery; buffoon’,  fr.  sdkhira,  ‘he  mocked,  ridiculed’. Cp.  masque,  masquerade.
KLN_1966.txt:23647:Derivative:  Mesozoic,  n. mesquin,  adj.,  mean,  sordid.  —  F.,  fr.  It.  meschi- no,  fr.  Arab,  miskin  (in  VArab.  pronunciation mesktn),  ‘poor,  wretched,  miserable’,  which  is borrowed  fr.  Heb.  or  Aram,  misken  or  Syr. mesken,  ‘poor’,  which  are  perh.  loan  words  fr. Akkad,  mushkenu,  ‘beggar,  needy’, mesquite,  n.,  a  mosque  (obsol.)  —  Sp.  mesquita (ModSp.  mezquita),  ‘mosque’.  See  mosque, mesquite,  also  mesquit,  n.,  either  of  two  shrubs  of the  pea  family.  —  Sp.  mezquite,  fr.  Nahuatl  miz- quitl.
KLN_1966.txt:24478:mosque,  n.,  a  Mohammedan  place  of  worship.  — F.  mosquee,  fr.  It.  moschea,  fr.  earlier  moscheta, fr.  Sp.  mesquita  (whence  ModSp.  mezquita),  fr. Arab,  masjid,  ‘place  of  worship,  mosque’,  which is  either  borrowed  fr.  Nabatean  masgedha, ‘place  of  worship’,  or  formed  independently, with  ma-,  a  pref.  denoting  place,  fr.  sdjada,  ‘he was  submissive,  prostrated  himself  in  prayer’, which  is  rel.  to,  or — more  prob. — borrowed from  Aram,  s^ghedh,  of  s.m.  Cp.  masjid,  mes- quite.
```


## [2026-09-07T15:50:03.734Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== FVQ masjid ===\"; grep -n -i \"masjid\\|Masgid\\|sagada\\|sagd\" FVQ_pages.txt | head -30\necho \"=== AFA masjid ===\"; grep -n -i \"masgid\\|masjid\\|Moschee\" AFA.txt | head -30\necho \"=== LKT ===\"; grep -n -i \"moschee\\|mesquita\\|masgid\\|masjid\" LKT.txt | head -30",
 "description": "Grep Jeffery, Fraenkel, Lokotsch"
}
```


### [2026-09-07T15:50:03.813Z] TOOL RESULT

```
=== FVQ masjid ===
9475:(Masjid).
=== AFA masjid ===
792:IV. 58). Aber zum Bau der ersten Moschee werden schon
846:berichtet, (A jonrney in thc liejaz III. The Mecca road) die Moschee das ein-
=== LKT ===
1630:Part,  praes.  act.  vom  Vb.  gamda  'ver- einigen', also  'der  vereinigende  (Ort)', Bezeichnung  für  die  Moschee,  die  die Muslime  zum  Freitagsgebete  vereinigt; ihr  Kennzeichen  ist  es,  daß  hier  die  sog. hnfba,  das  rituelle  Gebet  am  Freitag, von  einem  besonderen  Prediger  hätib gesprochen  [im  Gegensatz  zum  masgid, s.  hier  Nr.  1435];  hieraus  rum.  geamiä, geamie  'Moschee.'
2180:[Vom  Vb.  amma  'vorhergehen']  'Vor- gesetzter, Vorsteher',  insbesondere  die- jenige Person,  die  einer  Versammlung vorsieht,  um  das  Zeremoniell  bei  den öffenthchen  Gebeten  am  Freitag  und an  den  Beiramsfesten  zu  leiten.  Da  dies in  den  ersten  Zeiten  des  Islams  von  den Kalifen  selbst  geschah,  so  nahmen  sie den  Titel  imäm  an;  dieser  Titel  wurde sodann  auch  erteilt  1.  den  Lehrern  der ersten  islamischen  Jahrhunderle  als  den ersten  Auslegern  des  Korans,  2.  den Rehgionsdienern,  die  an  den  Moscheen die  Obliegenheiten  des  Priestertums  im Namen  des  obersten  Imäms  ausübten. Tk.  ebenso  iniam;  hieraus  rum.  imam, engl,  imam,  ungenau  iman;  ebenso  frz. iman,  imam,  dessen  Funktionen  imamat, imanat  heißen;  russ.  imam  'Ik.  Schrift- gelehrter'. [Devic  DEt  142.  Lammens Rem  136.
2186:'Öffentliches  Gebäude,  fromme  Stiftung [Moschee,  Schule,  Armenküche]' ;  hieraus frz.  imaret  nach  der  tk.  Aussprache  des ar.  Grundworts]  'eine  Art  tk.  Gasthauses, in  dem  die  Schüler  der  verschiedenen Schulen  ihre  Mahlzeiten  einnehmen können,  Hospiz'.  [Devic  DEt  142.  Lam- mens Rem  136.
3303:1435.  Ar.  masgid: 'Gebetshaus',  eigentlich  'Ort,  wo  man sich  niederwirft'  [Präfix  ma-  des  Ortes u.  Vb.  sagadu  'sich  niederwerfen,  irpoa- Kuveiv'];  hieraus  sp.  mezquita,  pg.  mes- quita,  it.  meschita,  moschea,  afrz.  mos- quete,  frz.  niosqiiee,  rum.  mo^ea;  ndl. moskee,  engl,  mosk,  nwsque,  dtsch. Moschee;  die  slav.  Formen  sind  über das  tk.  mesged  entstanden:  serb.  mecet, bulg.  medzit,  öech.  mesita,  poln.  meczet, russ.  medef  und  auch  rum.  mecet 'Moschee,  tk.  Friedhof  bei  Bukarest'. [Eguilaz  451/452.
3376:1461a.  Ar.  mimbar: Aussprache  für  ursprüngliches  minbar [von  ar.  nabara  'erheben';  minbar  aXso ursprünglich  die  Erhebung,  auf  die  man sieh  setzt  oder  stellt,  Untergestell,  s. BECKER  in  Orient.  Studien  (Festschrift für  Nöldeke)  I,  S.  338;  letzten  Endes aus  dem  Äthiop.,  s.  Nöldeke,  Neue  Bei- träge, S.  49]  'Kanzel',  und  zwar  im Gegensatz  zur  Predigtkanzel  kurst  die- jenige Kanzel  in  der  Moschee,  auf  der an  jedem  Freitag  die  Jiutba,  d.  h.  das Gebet  für  den  obersten  Herrscher  der Gläubigen,  gehalten  wird.  Hieraus  jüd.- dtsch.  Almemor,  die  inmitten  der  Syna- goge betindliche,  zum  Verlesen  der Tliora  bestimmte  Erhöhung  [die  in  jüd. Schriften  als  bema  oder  mifdal  bezeich- net wird],  vgl.  z.  B.  in  Heinrich  Heines , Prinzessin  Sabbath":  'Stolz  aufflackern auch  die  Kerzen  /  Auf  der  Brüstung des  Almemors'.
3380:Eigentlich  manäi-a  'der  Platz,  wo  Feuer oder  Licht,  ar.  när,  ist';  das  minära ist  der  Turm  einer  Moschee,  von  dessen Brüstung  aus  der  Gebetrufer  niu'addin fünfmal  täglich  die  Gläubigen  zum  Ge- bete aufruft;  pers.  und  tk.  minaret; hieraus  frz.  minaret,  rum.  minarea, minaret;  engl.  ndl.  minaret,  dtsch.  Mi' narelt;  sp.  almenar  'Eisenfuß,  auf  dem man  die  Fackeln  stellt',  sp.  pg.  almenara 'dass.,  Leuchte  in  den  Leuchttürmen'.
4503:1998.  Ar.  taklid: 'Nachahmung,  Umhängen  eines  Schwer- tes' [subst.  Inf.  II,  bes.  tk.  teklid-i-sejf die  Zeremonie,  bei  der  der  neue  Sultan auf  deu  Thron  in  die  'Ejjübmoschee geführt  und  dort  mit  dem  Schwerte  des Gründers  der  osmanischen  Dynastie, ORHAN,  gegürtet  wird];  hieraus  rum.
5408:masgid  1435
5848:Moschee  1435
8298:mesquita  1435
```


## [2026-09-07T15:50:15.414Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN leaf for mosque ===\"; python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\ni=t.find('mosque,  n.,  a  Mohammedan')\nprint('leaf(0-based ff count)=',t[:i].count('\\f'))\nj=t.find('masjid,  n.,  a  mosque')\nprint('masjid leaf=',t[:j].count('\\f'))\nEOF\necho \"=== FVQ around masjid ===\"; sed -n '9440,9530p' FVQ_pages.txt",
 "description": "Locate Klein leaf and read Jeffery masjid entry"
}
```


### [2026-09-07T15:50:17.867Z] TOOL RESULT

```
=== KLN leaf for mosque ===
leaf(0-based ff count)= 540
masjid leaf= 507
=== FVQ around masjid ===
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
iii, 828.FOREIGN VOCABULAKY OF THE QUR'AN 263
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
4 Cowley, Aramaic Papyri, p. 148.264 FOREIGN VOCABULARY OF THE QUR*AN
In the Qur'an it is used of the fane at Quba' (ix, 109), of the Temple
at Jerusalem (xvii, 1), of the Church built over the Seven Sleepers
(xviii, 20), and other places of worship, so that it is clear that for
Muhammad it meant any place of worship. In the same general sense
it is used in the pre-Islamic poetry, 1 and so must have come at an early
date from the more settled communities in the North. 2
(Misk).
Ixxxiii, 26.
Musk.
This sole occurrence is in an early Meccan description of Paradise.
The word was widely used among the Arabs in the pre-Islamic
period 3 and was quite commonly recognized as a loan-word from the
Persian. 4
The Phlv. 4-tyi^* mushk 5 seems to have come ultimately from the
Skt. *nra, 6 but it was from the Iranian, not the Indian form, that
were borrowed the Arm. jh^ 7 ; Gk. //capos' : Aram. ptflB ;
Syr. JoaQLo ; Eth. JJfllf|. It is more likely to have come direct from
Middle Persian into Arabic 8 than through the Syriac, as Mingana,
Syriac Influence, 88, claims.
(Miskin).
Of very frequent occurrence, e.g. ii, 77, 172 ; ix, 60.
Poor. "
' '^e ' ...
Note therefrom the formation <1X.^.^ poverty, indigence, n,
*58 ; iii, 108.
Fraenkel, Vocab, 24, pointed out that the Arabic word is from the
Syr. ]* *>ffnVo though this comes itself ultimately from Akkadian.
The muskenu of the Cuneiform inscriptions was interpreted by Littmann
1 Horovitz, KU, 140.
2 Schwally, ZDMQ, Hi, 134 ; Lammens, Ranctuaires, passim ; Von Kremer,
Streifziige, ix, n.
3 Siddiqi, Studien, 85 ; Geyer, Zwei Gediehte, i, 90 ff. : ii, 79. r
4 al-Jawaliqi, Mu'arrab, 143 ; ath-Tha'alibi, Fiqh, 318 ; as-Suyu^i, Itq, 324 ;
Mvzkir, i, 136; al-KhafajI, 182; LA, xii, 376.
5 Justi, Glossary to the Bundahesh, p. 241. Vullers, Lex, ii, 1185.
7 Hiibschmann,* Arm. Gramm, i, 196. 8 Vollers, ZDMQ, 1, 649, 652.FOREIGN VOCABULARY OF THE QUR*AN 265
```


## [2026-09-07T15:50:18.121Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD mzgt ===\"; grep -n -i \"mazgit\\|mzgt\\|mosque\" PHD.txt PHD_mackenzie.txt | head -20\necho \"=== NYB ===\"; grep -n -i \"mazgit\\|mzgt\" NYB_vol2_glossary.txt | head -20\necho \"=== HRN/HUB ===\"; grep -n -i \"mazgit\\|mazget\\|mezgit\" HRN.txt HUB.txt | head -20\necho \"=== PLA asbaghi ===\"; grep -n -i \"mazgit\\|masgid\\|masǧid\\|Moschee\" incoming/PLA/PLA_pages.txt | head -20",
 "description": "Grep Iranian sources for mazgit"
}
```


### [2026-09-07T15:50:18.241Z] TOOL RESULT

```
=== PHD mzgt ===
PHD.txt:474:mazģit [mzgt! | N ~] mosque.
PHD.txt:2850:mosque mazgit.
PHD.txt:4847:mazgit mizné may magas padīr-! padīrišnī padiriftant magind makog 1-2mar marg margomand margarzān margīh
PHD_mackenzie.txt:3523:mazgit [mzgt l IN . . . . ] mosque.
PHD_mackenzie.txt:7134:mosque mazgit.                                 navigable naydag.
PHD_mackenzie.txt:9111:mazgit
=== NYB ===
=== HRN/HUB ===
=== PLA asbaghi ===
13643:          (bes.       im    Hof         pers.       Moscheen)                         pers.     —> ar.
```


## [2026-09-07T15:50:34.403Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nfor f,ln,off in [('PHD.txt',474,21)]:\n    t=open(f,encoding='utf-8',errors='replace').read().split('\\n')\n    txt='\\n'.join(t[:ln])\n    leaf=txt.count('\\f')\n    print(f,'leaf',leaf,'printed page ~',leaf-off)\nEOF\necho \"=== BQT mazgit ===\"\nfor f in BQT_v1_pages.txt BQT_v2_pages.txt incoming/BQT/BQT_v3_pages.txt incoming/BQT/BQT_v4_pages.txt incoming/BQT/BQT_v5_pages.txt; do echo \"-- $f\"; grep -n \"مزگت\\|مزکت\" $f | head -5; done\necho \"=== MON mazgit ===\"\ngrep -n \"مزگت\\|مزکت\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt | head -10",
 "description": "Locate PHD page and grep Persian sources for mazget"
}
```


## [2026-09-07T15:50:35.853Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK me not ===\"; grep -n \"^ *m[ēě]\" POK_full.txt | head -40\necho \"=== POK 703 ===\"; grep -n \"Page(s): 703\" POK_full.txt | head",
 "description": "Grep Pokorny for me"
}
```


### [2026-09-07T15:50:35.899Z] TOOL RESULT

```
PHD.txt leaf 79 printed page ~ 58
=== BQT mazgit ===
-- BQT_v1_pages.txt
-- BQT_v2_pages.txt
-- incoming/BQT/BQT_v3_pages.txt
-- incoming/BQT/BQT_v4_pages.txt
3266:سر مزکت
3297:با چنین ماه چنین جشن بود همچو در مزکت آدینه سرای.
-- incoming/BQT/BQT_v5_pages.txt
=== MON mazgit ===
MON_part2.txt:55038:مزکت: ۱0۵2۸ [آرا, ع. مسسجد ] (1.) 
MON_part2.txt:55039:مسجد. مزکت آدینه: مسجد جمعد: مسجد 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:55038:مزکت: ۱0۵2۸ [آرا, ع. مسسجد ] (1.) 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:55039:مسجد. مزکت آدینه: مسجد جمعد: مسجد
```


### [2026-09-07T15:50:35.959Z] TOOL RESULT

```
=== POK me not ===
=== POK 703 ===
60768:Page(s): 703 
60802:Page(s): 703 
60974:Page(s): 703-704
```


## [2026-09-07T15:50:45.460Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '60740,60830p' POK_full.txt\necho \"===== MON context =====\"\nsed -n '55025,55050p' MON_part2.txt",
 "description": "Read Pokorny p.703 and Mo'in mazkat context"
}
```


### [2026-09-07T15:50:45.532Z] TOOL RESULT

```
From PIE the prohibitive partiele passed to Altaie: 

Protoform: *ma 



Meaning: a negative particle 

Turkic protofomn: *-ma- 

Tungus protoform: *-me 

Korean protofomn: *nno-t 

Japanese protofomn: *-ma- 

Note: 0CH51 2, 57. A monosyllabic root, but, unlike the 1st p. pron. or the accusative 

particle, it did not undergo denasalization in PA. This may be explained by the fact that it 

was in most cases already incorporated into the verbal form as a suffix. It is interesting to 

note Mong. *bui, *bu'neg. particle' - which may be originally the same morpheme, but 

functioning as a separate word and thus subject to the rule *mV > *bV. 

References: WP. II 236 f. 
Page(s): 703 

Root / lemma: me-2, m-e-t- {hame-) 

l\^eaning: to reap 

Note: 

Root/ lemma: me-2, m-e-t- {hame-): to reap derived from Hittite hamesh{a)-, hameshant-^ 

spring, season between winter and summer '. 

Material: 

Hittite hamesh{a)-, hameshant-^ spring, season between winter and summer'. 

gr. aijaw 'mow, cut, bite', ameto-s m. "harvest', ametu-s f. "id.', ameter m. "reaper', ameta- 

s m. "sickle' 

Maybe Tokharian: B matre 'sharp' (Adams 448) 

Indo Germanic */77e/- stands besides *me-{or *ame-) in Old High German maen^mow', 
Old English mawands.; Old High German mato-screch^ Wiesenhijpfer, locust, 
grasshopper'. Modern High German A^a//e "meadow which is mowed ', Old English meed 
f. "meadow, willow ' ( *msedwu), engl. meadow. Old Swedish maf^6s. 

Latin meto, -ere, messum' to reap, mow, crop, gather, collect, harvest ' (/77e'55c»/'"reaper, 
mower'); cymr. med/'ds., acorn, m/d/7' a reaper ', Old Irish me/th/eora/" reapers ', Middle 
Irish me/fhe/'a party of reapers', acymr. medelds., anter-metelic' half-pruned ', Middle 
Irish o'e-/r7es5 "scissors' ("double knife '); Old High German /77ao'" reaping, harvesting, 
mowing, hay harvest'. Old English maed^ the mowing, the mowed hay ' (= gr. apHTO^ " the 
reaping ', originally *a|JC(TO(;). 
References: WP. II 259, WH. II 82 f. 
Page(s): 703 



Root / lemma: meig- (or melag-1) {*melagh-) 

Meaning: to pluck; to milk 

Grammatical information: present melg-mi, PI. mjg-mes, participle Perf. Pass, rrilg-to- 

Material: Old Indie marsti, marjati, mrjati^ wipes, rubs down, polishes, purifies, cleans', 

participle Perf. mrsta-, 5-present mrksatT glides, rubs, curries ', mrksayati, mraksayatT 

coats '; 

common Old Indie gh- > ks- : Avestan gh- > xs- > s- : gh- > z-, z- 

Avestan marazaiti, msrszaitT berijhrt streifend ', zasta-marsta-^ durch Handschlag (d. i. 

BeriJhrung der Hande) geschlossen (Vertrag) '; a^present Old Indie mrdati, mrc/ayat/"\s 

gracious, verzeiht, verschont', Avestan merezda-^ forgive ' {msrezdika-, marzdika-^ taking 

pity ', n. " mercifulness '); these Aryan words can also contain *merg-\ Old Indie nir-marga- 

/7 shows lacking palatal guttural) ' Verwischung; Abgestreiftes, Abfall ', ni-mrgra-^ nestlling 

up ', vi-mrgvani. "clean, neat, tidy', apamargah-^ Achyranthesaspera ' (J. Schmidt KZ. 25, 
===== MON context =====
مرعم: : 1101 9 ۰(.) محل طمع؛ مطمع. 


امری که , ان اعتماد نباشد. 

مزر ع: 2 [- مغز ] (.) مغز. خداوند مز غ: 
خر دمنده با تدسر. 

مرغان: ۵ |[ - مر قان» متر. موز یگان.] 
(.) سوسیقی‌دانان. دسته‌ای از سازهای 
مختلف موسیقی که در نظام با هم نوازند. 
فو تین 

مزکت: ۱0۵2۸ [آرا, ع. مسسجد ] (1.) 
مسجد. مزکت آدینه: مسجد جمعد: مسجد 
جامع (التفهیم. مقدمه ص قف) 

مزکوم: ۱۵ [ع. ۰] (امف ۰) آنکه ره ز کام 
مبتلی شده؛ ج. مز کومین. 

مزکی: ۵ [ع. (امف.) پاک کررده 
شده. کات داده شده. 

مزگی: ۱۱۱02۵ [ع.] (افا.) باکك کننده» 
با کیزه کننده. معرف» شناساننده. (شرع.) 
آنکه شاهدان عادل را تزکیه و آنها رابه
```


## [2026-09-07T15:50:54.049Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"prohibitive\" POK_full.txt | head -20\necho \"-----\"\nsed -n '60690,60745p' POK_full.txt",
 "description": "Read Pokorny me-1 prohibitive entry"
}
```


### [2026-09-07T15:50:54.118Z] TOOL RESULT

```
60733:Meaning: prohibitive partiele 
60741:From PIE the prohibitive partiele passed to Altaie: 
-----

References: WP. II 256, WH. II 5; Hj. Frisk Eranos 50, 1 1 f. 
Page(s): 707 



Root / lemma: mei-7: moi-. mT- 

Meaning: mild, soft 

Note: often with A, /?-, r-, /-extended 

Material: Old Indie mayas-u. " relief, pleasure, joy, lust', in addition *m(ilies(i!^(e)\u Old 

Indie miyedha-m. " saerifieial food ', Avestan myazda-m. "saerifieial meal'; as *mei-6'"o- 

Old Indie medha-rc\. " Fettbrijhe ', medhas-v\. 'saerifiee, oblation'; 

with A: eymr. /t?^/" blushful', df-fu/'bo\6' {*mdi-lo-)\ Old Prussian miJIs, Lithuanian mfelas 
and /77y/5s"dear, pleasant', meilet 'love', /77e//^5"affeetionate, loving', myliu, my/ef/"\ove\ 
pa-milstu, pa-m/'/t/" gro\N\ng fond of; Latvian m[/s {o\der ^-stem) and m/7s {irom *mielas) 
"dear', mHeflove', mieluot^ host '; Old Chureh Slavie /77//b "pitiful', russ. m/7yj^6ear', ete.; 

Alb. m/re^ dear, niee, kind ' a Slavie loanword (eommon alb. -I- > -r-) 

with n-. eymr. /77i^y/7 "friendly', aeorn. mu/n, /770//7 "dainty', bret. moan'th\n, tiny' {*mei- 
no-)\ Old Irish mm^ smooth, gentle' {*mT-no-)\ 

with r-. alb. m/re^goo6, beautiful'; Old Chureh Slavie m/rh^peace'; ablaut, aserb. m/jer 
{*mo/ro-), apoln. m/er^peace' (Old Lithuanian mieras, Latvian m/ers6s. are Slavie 
loanword); 

with t-. Latin /77/?/s"mild, soft' {*meit-)\ Old Irish moith, moeth {*mdit-) ds., also (?) PI. 
/77e(/)//7"fat, fertile'; eymr. mwydo {*meit-) " soften ', mwydion^ soft parts, external genitalia 
'; Latvian at-misV beeome soft ', at-mieteC soften '. 

References: WP. II 244, WH. II 96 f., Trautmann 174, 175. 
Page(s): 711-712 



Root / lemma: me-1 

Meaning: prohibitive partiele 

Grammatical information: prohibitiv 

Material: Old Indie Avestan Old pers. ma, gr. pn, Armenian m/'ds., alb. mosds. (from *mo 

= Indo Germanie *me+ s, that perhaps goes baek to Indo Germanie /("'e). 

From PIE the prohibitive partiele passed to Altaie: 

Protoform: *ma
```


## [2026-09-07T15:51:04.802Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KNT ma ===\"; grep -n \"^mā\\|^ma-\\|mātya\\|^mā \" KNT.txt | head -30\necho \"=== KNT grep matya ===\"; grep -n -i \"matya\\|mātya\" KNT.txt | head -20\necho \"=== AHD me ===\"; grep -n -i \"^mē-\\|^me-\\. \\|prohibitive\" AHD_watkins1985.txt | head -20",
 "description": "Grep Kent and Watkins"
}
```


### [2026-09-07T15:51:04.873Z] TOOL RESULT

```
=== KNT ma ===
1638:$133. Encursis is a frequent phenomenon in OP. The enclities are the following: Pronouns: Ist sg. асе. -md, gen. -maty, abl. -ma. 2d sg. gen. -taiy. За sg. acc. -йт, gen. -Saiy, abl. -$a; pl. acc. -&$, gen. -Sàm. acc. -dum; pl. acc. -di$. pl. aec. -àà (dubious; only in avabasa-lé DB 4.72), Coordinating conjunctions: -eà ‘and’, -vë ‘or’. Postpositions: d, patiy; both also as separate words before or after their nouns. Adverbs and particles: -am, -kavy, -ciy, -dty, never separately. -apiy, -paliy both also separately. Miscellaneous: уа in mátya DB 4.43, 48, 71; yadatya XPh 35f (miswritten yadàya XPh 39), cf. yada : tya XPh 29. müm, elsewhere orthotone, in mātyamäm DB 1.52. rádiy in avahya-radiy DB 1.6f, etc.; also separ- ately. Double enclisis: mé-tya-mém DB 1.52; rauca- pati-vd,, DB .1:207 aatpati-mé DNb 20; avā-
5754:mā- vb. ‘measure’: Av. Skt. ma-, Lt. métior ‘I measure’. à + må- ‘extend’: атӣій npm. past ptc. pass. (6242. П) ‘noble’ DB 1.7; DBa 11. fra- + mā- ‘command’ (‘decide, judge’, acc. to Hz. ApI 154-6; ‘plan,’ Hinz, ZDMG 95.233-5); see also framülar-, framdnd-. јтатауаіа imf. mid. ($214, 5285.11) XPg 5. framatam nsn. past pte. pass. ($242.IT) DSf 19f°, 56.
=== KNT grep matya ===
1638:$133. Encursis is a frequent phenomenon in OP. The enclities are the following: Pronouns: Ist sg. асе. -md, gen. -maty, abl. -ma. 2d sg. gen. -taiy. За sg. acc. -йт, gen. -Saiy, abl. -$a; pl. acc. -&$, gen. -Sàm. acc. -dum; pl. acc. -di$. pl. aec. -àà (dubious; only in avabasa-lé DB 4.72), Coordinating conjunctions: -eà ‘and’, -vë ‘or’. Postpositions: d, patiy; both also as separate words before or after their nouns. Adverbs and particles: -am, -kavy, -ciy, -dty, never separately. -apiy, -paliy both also separately. Miscellaneous: уа in mátya DB 4.43, 48, 71; yadatya XPh 35f (miswritten yadàya XPh 39), cf. yada : tya XPh 29. müm, elsewhere orthotone, in mātyamäm DB 1.52. rádiy in avahya-radiy DB 1.6f, etc.; also separ- ately. Double enclisis: mé-tya-mém DB 1.52; rauca- pati-vd,, DB .1:207 aatpati-mé DNb 20; avā-
2662:C. As direct object anticipating the subject of an object clause: DB 1.52f. matyamdm xindsdtiy iya adam пазу Bardiya атту "lest (the people) know me, that Ї am not Smerdis'.
2916:(b) Volitional uses: affirmative commands bavatiy DNa 43, 45f, vaindiaiy DNb 35; negative commands with mä or matya, draujiyáhy DB 443, wkanàhy DB 471, kunavdtaiy DNb 56, bavdtiy DNb 59. Negative wishes possibly in (restored) vijanātiy, vināðayātiy A?Sa 5, A?Ha 7 (though optative or injunc- tive or imperative forms are equally pos- sible in these passages).
3038:(e) Volitive in a negative clause of purpose in- troduced by matya ‘lest’: with subj. depending on potential opt. DB 1.52, with subj. depending on past ptc. with omitted astzy DB 4.48f.
5760:таша conj. ‘lest, that not, not’: mà ‘not’ + conj. tya (§133, 4292р).  matya-mam (5133) DB 1.52. тайа DB 4.43, 48, 71.
=== AHD me ===
```


## [2026-09-07T15:51:07.158Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT ma ===\"; grep -n \"^mā\\b\\|^mā \" BRT.txt | head -20\necho \"=== BRT search 'nicht' ma ===\"; grep -n \"1140\\|1141\" BRT.txt | head -5\necho \"=== IEC ===\"; grep -n -i \"prohibitive\" IEC.txt SYN.txt | head -20\necho \"=== WLD Bd2 236 ===\"; grep -n \"prohibitiv\\|Prohibitiv\" incoming/WLD/WLD_Bd2_pages.txt | head -20",
 "description": "Grep Bartholomae, Mann, Buck, Walde-Pokorny"
}
```


### [2026-09-07T15:51:07.263Z] TOOL RESULT

```
=== BRT ma ===
=== BRT search 'nicht' ma ===
11594:j.  jaity^  Vt  13.   1141  lies  zairy'.
19892:mainyui.x'ar^Oti-  1140
=== IEC ===
=== WLD Bd2 236 ===
854:v7]7ivriog, vgjiiog in prohibitive diss. Y^^kung des anl. v- begriindet sein.
15490:1.    me „(da6) nicht‘^, prohibitiv.
21076:         des prohibitiven     durch ne aufierhalb des Ar. Arm. Gr. Alb. s. II
```


## [2026-09-07T15:51:15.161Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '5745,5765p' KNT.txt\necho \"=== leaf/page ===\"; python3 - <<'EOF'\nt=open('KNT.txt',encoding='utf-8',errors='replace').read().split('\\n')\nfor ln in (5754,5760):\n    leaf='\\n'.join(t[:ln]).count('\\f')\n    print(ln,'leaf',leaf,'printed ~',leaf-15)\nEOF\necho \"=== WLD context ===\"; sed -n '15480,15505p' incoming/WLD/WLD_Bd2_pages.txt; grep -n \"\\[pdf page\" incoming/WLD/WLD_Bd2_pages.txt | awk -F: '$1<15490' | tail -2",
 "description": "Read Kent lexicon ma entry and Walde-Pokorny me"
}
```


### [2026-09-07T15:51:16.617Z] TOOL RESULT

```
bümim asf. DNa 2, 32; DSe 2°; DSf 1; DSt 2; DZe 1f; DE 2; XPa 1; XPb 2; XPc 1; XPd 2; XPf 2; ХР 1f; ХЕ 3; XV 2f; A!Pa 2^; A?He 2. ратат, asf. ($55.1) A3Pa 2. bümiyà sf. (8179.IT) DNa 11f; DSb 9; DSe 10; Рб 5; DSs 2°, 3°; DZb 4; DZe 6; DE 17f; XPa 9; XPb 17; XPe 7f; XPd 12; XPf 12, 25; XPh 10; ХР); XE 17; XV 13; A'Pa 18°; A?8e 4°; Wb 7; Wc 8; Wd 8.
BU nsf. ($42) DSf 24, 28. BUyà Isf. DSd 2°; DSf 7, 15, 16, 18, 24^; DSg 2; DSi 2, 4; DS) 1°; DSy 2; D'Sb 2; A’Sa 1; А4 2; A?Ha 2; A?He 9, 17; А?Ра 11.
brdtar- sb. ‘brother’: Av. brätar-, NPers. biraddr, Skt. bhratar-, Gk. @parnp ‘clan-brother’, Lt. frater, OCS bratru, Gt. brobar, pIE *bhráter- (862, 875.111, $128, $154.П). баі nsm. ($124.5, 5186.1) DB 1.29f, 39f.
brazmaniya- adj. ‘prayerful, reverent’ (cf. Kent, Lg. 21.223-9), with braz- rather than barz- (883; cf. Elam. pir-ra-us-man-ni-ia, АКК. bi-ra- 2a-man-ni-1): deriv. (§144.IV) to pAr. antecedent of Skt. bráhman- ‘religious devotion, prayer’, ef. identical Skt. deriv. brahmanyd- ‘religious’, to pIE root *bhergh- (see OP bard-; $75.1II, §95, $120, 5155.11; Henning, TPS 1944.108-18). For other views, see Kent, Lg. 13.301; Hartmann, OLZ 40.145-60; Nyberg, Rel. 367, 478; Hz. AMI 8.69, Apl 116-8 (to Av. barag- ‘to welcome’, barag- ‘rite’, Бәтәгба- ‘beloved’; wrongly, since this would give OP *bragman-); Christensen, Essai sur la démonologie iranienne 40-1; Henning, BSOS 10.506; Abayev, Iranskie Yazyki 1.134; Scherman, JAOS 65.141-3 n.23. Cf. also О. M. Dalton, Treasure of the Oxus 94-5. On form and meaning of РЫ. brahm brahmak, see Henning, TPS 1944. 108-18. brazmaniya nsm. ХР 41, 51, 54 (hardly brazmaniy isn. modifying arid; also not -niy apn. ‘divine’ with Sen 155, nor adn. in elliptic dual with Pisani, see under aria-).
т°, of dubious meaning, Se 1; taken by Justi, IFA 17.112, to be an abbreviation for OP *méraka ‘seal’, NPers. maráh.
та-, stem of ist person pron. in obl. cases of sg.; see adam.
mà conj. ‘not’, in prohibitions ete.: Av. Skt. mà, Gk. шӯ, pIE *mé ($109, §191.1, §292b). With subj.: DNb 55 (mé-taty), 58. With opt.: DB 4.59, 69, 79°; DPd 18, 19 bis, 20; XPh 39. With
201
inj.: DB 4.54; DPe 21; DNa 58, 59, 60; DNb 52 (mà-lay). With imv.: DNb 60. With lost verbs: DNb 57, DSq 4 bis; with restored subj. A'Sa 5^ bis, A?Ha 7, 7°. See also mdtya.
mā- vb. ‘measure’: Av. Skt. ma-, Lt. métior ‘I measure’. à + må- ‘extend’: атӣій npm. past ptc. pass. (6242. П) ‘noble’ DB 1.7; DBa 11. fra- + mā- ‘command’ (‘decide, judge’, acc. to Hz. ApI 154-6; ‘plan,’ Hinz, ZDMG 95.233-5); see also framülar-, framdnd-. јтатауаіа imf. mid. ($214, 5285.11) XPg 5. framatam nsn. past pte. pass. ($242.IT) DSf 19f°, 56.
таш- vb. ‘flee’: meaning established by Мат. and АКК. versions (Hüsing, KZ 38.258); probably to Skt. munthate ‘flees’ (Jn. JAOS 38.122). атида imf. ($211) DB 2.2, 71; 3.41f, 71.
Maka- sb. ‘Maka’, a province of the Persian Empire (lit. on location given in JAOS 56.217-8): Elam. ma-ak-qa, АКК. ma-ak, cf. Gk. pl. Мака ($99, $1322, SI4LITD. See also Mactya-. Maka nsm. DB 1.17; DPe 18.
magu- sb. ‘Magian’, member of a priestly order of Media: Flam. ma-ku-i3, АКК. ma-qu-&u, Gk. Méyos ($153.1). Uncertain material on mean- ing and etymology, Kónig, Klotho 4 chap. 12, and RulD 66. magus nsm. DB 1.36, 44, 46, 64, 66, 101; 4.8; DBb 2. magum asm. DB 1.50, 54, 57, 73; 4.81.
Maciya- adj. ‘Macian’; pl., name of a prov- ince of the Persian Empire: deriv. of Maka- ($99, $113, 8132.2, $144.01). Maciya пет. A?P 29. Масту for nsm. (856.11) DN xxix. Macy npm. DNa 30; DSe 230; XPh 25.
madtar- sb. ‘mother’: Av. matar-, Skt. matdr-, Gk. Dor. ратар, Lt. mäter, pIE nom. *maté, stem *máler- ($154.П): in hamdtar-.
таша conj. ‘lest, that not, not’: mà ‘not’ + conj. tya (§133, 4292р).  matya-mam (5133) DB 1.52. тайа DB 4.43, 48, 71.
mabista- adj. ‘greatest’, equal to ‘crown prince’ in XPf (Speiser ap. Kent, Lg. 9.40-1; Hz. Apl 254-8): Av. masista-, NPers. mähist, Gk. ppxio ros ‘longest’ (radical vowel after that in anxos Jength"); superl. to pIE *mak-ros, Gk. накр, Lt. macer ‘thin’, pLE root *mak- (887) ‘be long and slender’ + superl.,suffix.<ste-) (S117, $156.11,
202 OLD PERSIAN
4190.1), Gk. -сто-, Av. -tšta-, Skt. (with aspira- tion) -gha-. таб: а пет. AsH 6; DB 2.13, 24; 3.70; DPd 1; DPh 9; DSf9; DSp 1°; DH 7; XE 2; XV if; АНе1. [ma8]jiSta-ISàm] DB 5.27. mati&- lam asm. DB 2.20, 83; 3.12, 31, 57, 85; 5.6, 8, 12, 28; XPF 32.
Müda- (S166.IIT) adj. ‘Median’; masc. as sb. ‘Media’, a province of the Persian Empire: Elam. ma-da, АКК. ma-da-a-a, Gk. pl. Mado.
(1) ‘Median’: Mada nm. DB 1.49; 2.14°, 16, 18, 82; 418; DN 1°; APP 2, Madam asm. DB 2.21, 82; 3.30. Mada npm. DSf 50, 54. Майа] ipm. DB 2.23. MddatSuva lpm. DB 2.23.
=== leaf/page ===
5754 leaf 225 printed ~ 210
5760 leaf 225 printed ~ 210
=== WLD context ===
                                           mich'* mit -enam aus -ianam;
Meillet Msl. 7, 165^ Bugge KZ. 32, 19, Pedersen KZ.
                                                    39, 352; von Hiibsch-
mann Arm. Gr. 14/3 mit Unrecht wegen der Bed. bezweifelt). Auf einem
^fxeg    beruhen kret. fieora^ ark.     fieoiav^ thess. fxeoTiodi, gort. juetr^ig „t'cog‘%
horn, peocp        „bi8 zu^‘ {*peg aus ^aeT{a)-\-g wie
                                                        lat. abs?   Brugmann-Thumb  ^
GrGr.^ 632).
  Die Bed. des „v61iig ein Ziel erreichthaben“
                                               aus „mitten hinein‘‘.
1.    me „(da6) nicht‘^, prohibitiv.
                                (Curtius'^ 332 f.), arm. mi ds. Hiibschraann Arm.
Gr. I 474, alb.        mos ds. fans mo = idg. ^rne^s .,mcht*^, das wahrscheinlich
                                                               me-                                    237

aus       lat.   dis-   am Verbuin erwachsen ist;                      G, Meyer Alb. Wb. 287.       Brug-
mann II ^ 3, 827).

2,       me- „messen, abmessen“.
     Ai. 7ndi/\  mimed i         mitd- „geniessen*\ matra^ mdtni- n.
mafia-       n. j.das Messen,              Ma6‘'    (
                                                        :   cech. m^^ri)^ mfdi- „Mab, richtige Erkennt-
nis‘*'    (=     gr. jurjjig,       lat.   meti-or^         ags.   mmd)^ ahhi-mnti- ^jlfachstellung, An-
schlag“, miti- „Ma6, Gewicht, Wert“,                                 prakr. mettam ds. (=ai. "^mitram)'^
           ma- „messen“, Ptc. -mda-^ -mdta-^ ap. fra-mdtar- „Gebieter‘^
     av. ap.
```


## [2026-09-07T15:51:29.327Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KNT page 210 region ===\"; grep -n \"^210$\\|^210 \\|210 OLD PERSIAN\" KNT.txt | head\necho \"=== AHD me ===\"; grep -n \"mē\" AHD_watkins1985.txt | head -20\necho \"=== AHD grep 'Not' entry ===\"; grep -n -i \"^me-\\|^mē-\\|Prohibitive\" AHD_watkins1985.txt | head",
 "description": "Kent p210 and Watkins me"
}
```


### [2026-09-07T15:51:30.827Z] TOOL RESULT

```
=== KNT page 210 region ===
=== AHD me ===
=== AHD grep 'Not' entry ===
```


## [2026-09-07T15:51:32.640Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON prefix ma- 3677 ===\"; grep -n \"^مَ:\\|^م:\\|مباد\\|مگو\" MON_part2.txt | head -20\necho \"=== ARY latin index me ===\"; grep -n -i \"MEZGET\\|MAZGET\\|MASJED\" incoming/ARY/ARY_latin_index_pages.txt | head\necho \"=== AFM masjid ===\"; grep -n \"مسجد\\|مزگت\" AFM_pages.txt | head -10\necho \"=== TAD ===\"; grep -n \"مسجد\" TAD_pages.txt | head -10",
 "description": "Grep Mo'in prefix, Aryanpur, Addi Shir, Unaysi"
}
```


### [2026-09-07T15:51:32.750Z] TOOL RESULT

```
=== MON prefix ma- 3677 ===
4379:سداً المبادی. فاعل به اراده (فاعل بالاراده): 
7599:منطقی است که از مبادی خاص کرفته شده و 
7600:در حقیقت آن مبادی فصولند. مثلاً سفهوم 
26439:از اینکه مبادا او را دست کم بگیرند یعنی 
32508:آب در زراعت عامگو | ها در ۸ با 
35430:گندم‌گون گندمگون: 0 -.ع (ص‌مر.) 
44611:مباد: ۱۵ |م. نهی + باد (فعا. صيغه دعا 
44618:مبادرت: (ند. )۱۱0۱۵۵۲۸۱ [ع. سادر ة | 
44622:مبادله: (ند. 0016-)۱۱۱0۵:۱0:1۸ [ع. مسادله | 
44628:مبادی: ۱۱۸۱21 [ع. ۰ (.) ج. ۳ آغازهاء 
44629:مد آها. اصل‌ها. اساس‌ها. مبادی اریعه: (فا.) 
44632:(فر لغا. سحد. ۲۸۴). مبادی برهان: (فد.) 
44633:مقدمات برهان. مبادی خارجی: (فد.) مراد 
44635:ذات اشباءاند. (فر لغا. سج. ۲۸۴). مبادی 
44641:می‌باشد که مبادی مفارقه هم نامیده می‌شود 
44648:عضلات باشد (فرع. سج.: مبادی افعال). 
44661:باشد (اساس الاقتباس ۳۹۳). مبادی علوم: 
44664:(فرلغا. سج. ۲۸۳). مبادی قیاسات: (فد.) 
44667:مبادی: ۱۵ [ع. مادی | (افا.) از 
44884:ج. مبادی. (فد.) سبب؛ مبدأ اول: (فد.) ذات 
=== ARY latin index me ===
=== AFM masjid ===
=== TAD ===
```


## [2026-09-07T15:51:40.335Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD head ===\"; head -30 AHD_watkins1985.txt\necho \"=== AHD search me ===\"; grep -n -i \"negative particle\\|prohibit\" AHD_watkins1985.txt | head",
 "description": "Inspect Watkins file"
}
```


### [2026-09-07T15:51:40.387Z] TOOL RESULT

```
=== AHD head ===
American Heritage — Dictionary
of
Indo-European Roots
Revised and edited by Calvert Watkins
JUN 01 1985
American Heritage , Dictionary Indo-European Roots
American
Heritage
Dictionary do-European
Root
In
Revised and edited by Calvert Watkins
Houghton Mifflin Company Boston
Copyright © 1985 by Houghton Mifflin Company. All rights reserved. No part of this work may be reproduced or trans- mitted in any form or by any means, electronic or mechani- cal, including photocopying and recording, or by any infor- mation storage and retrieval system, except as may be expressly permitted by the 1976 Copyright Act or in writing by the Publisher.
All correspondence and inquiries should be directed to Reference Division, Houghton Mifflin Company One Beacon Street, Boston, MA 01208
Manufactured in the United States of America
Library of Congress Cataloging in Publication Data Main entry under title:
The American heritage dictionary of Indo-European roots.
Includes index. 1. Indo-European languages—Roots—Dictionaries. 2. English language—Etymology—Dictionaries. I. Watkins, Calvert. P615.A43 1985 412'.0321 84-27911 ISBN 0-395-37888-5 ISBN 0-395-36070-6 (pbk.)
Contents
Staff
Foreword
Preface Indo-European and the Indo-Europeans
Guide to the Dictionary
Indo-European Roots
Index
Table of Indo-European Sound Correspondences Chart of Indo-European Languages
Staff
Marion Severynse - Editor and Etymologist
Howard Webber - Publisher Margery S. Berube - Director of Editorial Operations
=== AHD search me ===
323:outlaw”), in: a. Old English bannan, to summon, pro- claim, and Old Norse banna, to prohibit, curse: BAN}; b. Old French ban, feudal jurisdiction, summons to military service, proclamation, Old French bandon, power, and Old English gebann, proclamation: BANAL, BANNS; ABANDON; C. Old French banir, to banish: BAN- ISH; d. Late Latin bannus, bannum, proclamation: Ccon- TRABAND; @. Italian bandire, to muster, band together (< “to have been summoned”): BANDIT. 4. Suffixed form *bha-ni in Germanic *b6dni- in Old Norse b6n, prayer, request: BOON!. 5. Suffixed form *bhd-ma in: a. Latin fama, talk, reputation, fame: FAME, FAMOUS; DEFAME, INFAMOUS; b. Greek phémé, saying, speech: EUPHEMISM. 6. Suffixed o-grade form *bhd-nd in Greek phéné, voice, sound, and phénein, to speak: PHONE, -PHONE, PHO- NEME, PHONETIC, PHONO-, -PHONY; ANTHEM, (ANTI- PHON), APHONIA, CACOPHONOUS, EUPHONY, SYMPHONY. 7. Suffixed zero-grade form *bha-to- in Latin fatéri, to acknowledge, admit: CONFESS, PROFESS. 8. Greek blas- phémos, evil-speaking, blasphemous (first element ob- scure): (BLAME), (BLASPHEME), BLASPHEMOUS. [Pok. 2. bha- 105.] bha-bha-. Broad bean. 1. Latin faba, broad bean: FAVA BEAN. 2. Variant form *bha-un- in Germanic *bauné in Old English béan, broad bean, bean of any kind: BEAN. [Pok. bhabhé 106.] bhad-. Good. 1. Germanic (comparative) *batiz6 in Old English betera, better: BETTER. 2. Germanic (superla- tive) *batistaz in Old English bet(e)st, best: BEST. 3. Ger- manic noun *b6¢6 in Old English bét, remedy, aid: BooT?. 4. Germanic verb *batnan, to become better, in Old Norse batna, to improve: BATTEN!. [Pok. bhdd- 106.] bhag-'. To share out, apportion, also to get a share. 1. Greek phagein, to eat (< “to have a share of food”): -PHAGE, -PHAGIA, PHAGO-, -PHAGOUS. 2. Extended form *bhags- in Avestan bakhsh- in Persian bakhshidan, to give: BAKSHEESH, (BUCKSHEE). [Pok. 1. bhag- 107.] bhag-. Sharp. Suffixed form *bhag-ro- in Greek phag- ros, whetstone, also a name for the sea bream: PORGY. [Pok. 2. bhag- 107.] bhaghu-. Arm. Germanic *bdguz in Old English bdg, boh, bough: BouGu. [Pok. bhdghii-s 108.] bhago-. Beech tree. 1. Germanic *b6k6, beech, also “beech staff for carving runes on” (an early Germanic graphic device), in: a. Old English bdc, written docu- ment, composition: BOOK; b. Middle Dutch boek, beech: BUCKWHEAT. 2. Germanic *bdkjdn- in Old English béce, beech: BEECH. [Pok. bhdgo-s 107.] bhar-. Also bhor-. Projection, bristle, point. 1. Suffixed o-grade form *bhor-so- in Germanic *barsaz in Old English bzrs, perch, bass (a fish that has a spiny dorsal fin): BASs!. 2. Suffixed zero-grade form *bhAr-sti- in Germanic *bursti- in Old English byrst (> Middle Eng- lish bristel), bristle: BRISTLE. 3. Extended zero-grade form *bhrs- in: a. Germanic *bur- in Swedish borre, bur, perhaps akin to the Scandinavian source of Middle English burre, bur: BUR}; b. suffixed form *bhrs-dh- in Germanic *bruzd-, point, needle, in Old Norse broddr, spike: BRAD; C. suffixed form *bhrs-ti- in Latin fastig- ium, summit, top, extremity: FASTIGIATE, FASTIGIUM; d. possibly suffixed form *bhrs-tu- in Latin fastus, fasti- dium, disdain (from the notion of prickliness): FASTIDI- ous; e. suffixed form *bhrs-tio- in Russian borshch, cow parsley: BORSCHT. [Pok. bhar- 108.] bhardha. Beard. Possibly related to bhar-. 1. Germanic *bardaz in Old English beard, beard: BEARD. 2. Ger- manic *bard6, beard, also hatchet, broadax (the associ- ation of beard and ax is attested elsewhere in the Indo-European family; both were symbols of patriarchal authority), in Old High German barta, beard, ax: HAL- BERD. 3. Latin barba, beard: BARB!, BARBEL, BARBEL- LATE, BARBER, BARBETTE, BARBICEL, BARBULE; REBARBATIVE. [Pok. bhardhé 110.] bhares-. Also bhars-. Barley. 1. Germanic *barz- in Old
502:ghabh-. Also ghebh-. To give or receive. 1. Form *ghebh- in Germanic *geban in: a. Old English giefan, to give: GIVE; b. compound *far-geban (*far-, away; see per'), to give away, in Old English forgi(e)fan, to give, give up, leave off (anger), remit, forgive: FORGIVE. 2. Suf- fixed form *ghebh-ti-, something given (or received), in Germanic “giftiz in Old Norse gipt, gift, a gift: GIFT. 3. O-grade form “*ghobh- in Germanic *gab-ulam, some- thing paid (or received), in Old English gafol, tribute, tax, debt: GAVEL2. 4. Form *ghabh-é- in: a. Latin habére, to hold, possess, have, handle (> habitdre, to dwell): ABLE, BINNACLE, HABILE, HABIT, HABITABLE, (HABI- TANT), (HABITAT); (COHABIT), EXHIBIT, INHABIT, IN- HIBIT, PREBEND, PROHIBIT, (PROVENDER); b. Latin débére (dé-, away from; see de-; third person plural present passive debentur), to owe: DEBENTURE, (DEBIT), DEBT, DEVOIR, DUE, (DUTY); (ENDEAVOR). Compare kap-. [Pok. ghebh- 407.]
2136:PRO-2 per? PROBABLE per! PROBE pert PROBITY per! PROBLEM gWele-1 PROBOSCIS g¥6- PROCEED ked- PROCLAIM kele-2 PROcLITIC § klei- PROCLIVITY klei- PROCREATE ker-3 PROCTITIS prdkto- PROCTOLOGY prdkto- PROCTOR cura PROCTOSCOPE prdkto- PROCUMBENT keu-2 PROCURATOR cura PROCURE cura PROCYON kwon- PRODIGAL ag- PRODIGY ég- PRODROME der-1 PRODUCE deuk- PROFANE dhés- PROFESS bha-2 PROFESSOR reg-! PROFFER bher-1 PROFICIENT dhé-1 PROFILE gWhi- PROFIT dhé-1 PROFLIGATE bhiig- PROFOUND bhudh- PROFUSE gheu- PROGENITOR gene- PROGENY gene- PROGLOTTID glégh- PROGNOSIS gnd- PROGRAM gerbh- PROGRESS ghredh- PROHIBIT ghabh- PROJECT yée- PROLAN al-3 PROLAPSE leb-1 PROLATE tele- PROLEGOMENON leg-! PROLEPSIS (s)lag¥- PROLETARIAN al-3 PROLIFEROUS _al-3 PROLIFIC al-3 PROLIX wleik- PROLOCUTOR tolkw- PROLOGUE leg-1 PROLONG del-1 PROLUSION leid- PROMENADE men-2 PROMINENT men-2 PROMISCUOUS meik- PROMISE (s)meit(e)- PROMOTE meue- PROMPT em- PRONE per! PRONEPHROS _ negwh-ro- PRONOUN no-men- PRONOUNCE neu-! PROOF per! PROPAGATE pag- PROPEL pel-6 PROPEND (8)pen- PROPER pert PROPERTY per? PROPHET bha-2 PROPHYLACTIC phulax PROPINQUITY per? PROPIONIC ACID peie- PROPITIOUS pet- PROPOLIS pele-3 PROPORTION pere-2 PROPOSE apo- PROPRIOCEPTION per! PROPRIOCEPTOR per? PROPTOSIS pet- PROPYLAEUM pulé PROPYLON pulé PROROGUE reg-1 PROS- pert PROSCRIBE skribh- PROSE wer-3 PROSECUTE sekw-1 PROSELYTE leudh-1 PROSOMA teue- PROSOPOPEIA kWwel-2, per! PROSPECT spek- PROSPER spé-1 PROSTATE sta- PROSTHESIS dhé-1 PROSTITUTE sta- PROSTOMIUM ste-men-
```


## [2026-09-07T15:51:41.643Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '44605,44615p' MON_part2.txt\necho \"=== KNT 210 ===\"; grep -n \"210\" KNT.txt | sed -n '1,10p'",
 "description": "Read Mo'in mabad and Kent 210"
}
```


### [2026-09-07T15:51:41.727Z] TOOL RESULT

```
مباحئین. 

ماحنثه: (06۵6-) ۱۱۱0۱۵۵۳۵52 [ع. مساحنه | 
(مصل.) با یکدیگر بحث کردن. (امص.) 
بحث. گفتگو؛ ج. مباحثات. 

مباد: ۱۵ |م. نهی + باد (فعا. صيغه دعا 


و نفرین)| سوم شخص مفرد نهی از «بودن»: 
المت تقو هه تاشلایهای ماب ستت؟ 
=== KNT 210 ===
101:узыны dud £s 52 ШОР ossa desino ie torus 62 5154. Noun and Adjective Stems ending in $184. The Case-Endings of Consonant-Stems РЕР УКИ 52 in pIE and in Атуап.............. 63 $155. Noun and Adjective Stems ending in $185. The -s- Stems in ОР................ 63 ТЕ 52 5186. The -r- Stems ш ОР................ 64 $156. Noun and Adjective Stems ending in $187. The -n- Stems in OP................ 64 MT 52 $188. The Stems in Stops, in OP.......... 65 8157, Adjective Stems with suffix -vani-.... 52 $189. The Dual Case-Forms of OP......... 65 $158. Other Noun and Adjective Stems end- $190. Adjectives in ОР................... 65 ing in consonants................. 58 5191. The Adverbs of OP................. 66 §159. Noun and Adjective Compounds in $192. The Pronouns of OP................ 67 ОРЕ TEE ERN 53 $193. The First Personal Pronoun......... 07 $160. Determinative Nouns and Adjectives. 53 $194. The Second Personal Pronoun....... 67 6161. Possessive Adjectives............... 54 §195. The Enclitic Pronouns of the Third 6162. Participial Compound Adjectives.. . . . 54 Реон е мард 67 6163. Names of Регвопѕ.................. 54 $196. The Third Personal Pronoun haw.... 68 $164. Personal Names of Iranians.......... 55 5197. The pIE Relative Pronoun *0-...... 68 6165. Names of Months.................. 55 $198. The OP Relative and Article hya hyà §166. Names of РІасев................... 55 ЇЙ coxa ate rade Кызыла Аатын 68 §167. Province Names and Ethnics........ 56 $199. The Demonstrative Pronoun ‘this’... 68 $200. The Demonstrative Pronoun ‘that’... 69 Снартев V. $201. The Interrogative-Indefinite pIE *g*o- AD Рзин oF Nowe, Аът, PU ie one e pug hi’. 08 $168. Declension in ОР................... 57 $208. Semi-Pronominal Adjectives......... 69 $169. The Case-Endings of -o- Stems іп pIE. 57 — $204. The Numerals..................... 69 $170. The Case-Endings of -о- Stems in | Aryan...... ы ышын, pg Cuaprer VI. Stems AND Forms or VERBS $171. Case-Forms of -o- Stems in ОР....... 98 $205. The Verb in Old Persian. . .......... 70 $172. The Development of the -o- Declen- 6206. Verbal Ргейхез..................... 70 БООР si sexos Meee kanes 59 $207. The Present-Tense Formations. ...... 70 6178. The Case-Endings of -d- Stems in $208. The Present-Tense System (type, Skt. Soo MMC M 59 ДЫ MEN н N 10 $174. The Case-Endings of -à- Stems in $209. Тһе Present-Tense System (type, Skt. - АТУШ o saxo арын nk pesi Ped 60 GUM) i e eoe ri $175. Case-Forms of -d- Stems in ОР...... 60 $210. The Present-Tense System (types, Skt. $176. The Development of the -й- Declen- krnóti, krinati, vénati). .. . ......... 71 Slot iD OP еу siete vanes Sees 60 §211. The Present-Tense System (type, Latin $177. The Case-Endings of -t- and -1- Stems ШИЙ ac cos eerie ate ore Ri 71 in pIE and in Aryan.............. 60 8212. The Present-Tense System (type, Skt. $178. Case-Forms of -Ї- and -i- Stems in DICOhdh). «oves des vase Sane ae 71 OP Ж��РИ КУО ТО ГС 61 §213. The Present-Tense System (types, $179. The Development of the -1- and -i- De- Skt. bhdvate, тида)... . 72 clensions in ОР.................. 61 8214. The Present-Tense System (types, Skt. $180. The Case-Endings of -й- Stems in pIE ndhyatt, йтїшаң)................ 72 and in Агуал.................... 62 S215. The Present-Tense System (types, Skt. $181. Case-Forms of -й- Stems in ОР...... 62 pütáyati, райбуай)................ 72 $182. The Development of the -ti- Declen- §216. The Present-Tense System with suffix
850:IJ. Diphthongs: short: e? o1 ai at eu ow aw au long: 2100014  ёибийи III. Consonants: voiceless voiced non- aspi- non- asp. rate — asp. asp. Stops Nasals labial р ph Б № m dental { h d di n palatal k fh ĝ jh À pure velar 9 gh g gh | a labiovelar @ qth g g*h Clusters dental ist isth бй ага Continuants (voiced, except s) sibilants 8 2 liquids lr semivowels ju
2417:$210. Тнк Present-Tense SYSTEM OF TYPES бкт. krnót, krinati, vénati: the stem is the root in the zero-grade (usually), with a suffix begin- ning with a nasal.
2514:OP danulvatiy|, Skt. dhánvati, stem pAr. dhan- va-; unless we should restore OP батат], like Skt. dhanulé, stem pIE *dhn-nu- (varying with -neu-, $210.I].!
2534:With the vocalism of the present-tense stem: addriya, to dar-, pres. dāraya- ($215); and the uncertain [ар 0 уа] (see Lex. s.v. paté-). Formed on the present-tense stem: 3d pl. akunavaya"td, to kar-, pres. kunav-a- (§210.1); and the uncertain [айуа|вї]уа, for *atiyayastya ($215), to yam-, pres. yasa- (5212). Dubious forms on the sigmatic aorist stem, früsah[ya] to root sã- ($218.1), and on the per- fect stem, cazr|zyatd] or |clizr|iyatà], to kar-.
3356:DH = Darius, HAMADAN: Trilingual, in dupli- cate on a gold and a silver plate; now in Teheran. OP 8 lines, Elam. 7 lines, АКК. 8 lines. The two copies vary slightly in the line-division; our text follows the gold plate. The text is repeated in DPh. JMUnwalla, Jame Jamshed, Sept. 30, 1926; Hz. DLZ 47.2105-8 (Oct. 16, 1926); SSmith, JRAS 1926.433-6; CDBuck, Lg. 3.1-5 (1927); LHGray, JRAS 1927.97-101; JMUn- walla, JCOI 10.1-3 (1927); Wb. 2А 37291-4 (1927); ESchwentner, ZH 6.171-3 (1928); Hz. Memoirs of the Archaeological Survey of India
3957:Wb. ЖА 46.53-82 makes and adopts the following emendations which are not discussed in my article, and which JI do not accept: " hadā : karla : S[ugdam; % laniyam] for [vasiy], * [aniya] for [haus], 27 21055 for ша їт; " hyalilam : тан Ма, which violates the recorded length of the gaps.
5253:kunautiy (866.1, $70, $99, $2101) DNb 24f; DSs 2°, 3f, 4, 6°. |
5258:akunava"tà 3d pl. imf. mid. (§210.1, $236.IT) DB
5271:kunautuy imv. (§210.1, 5237.П) DB 4.76.
```


## [2026-09-07T15:51:50.808Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"703\" AHD_watkins1985.txt | head -10\necho \"---\"; grep -no \"m[éèêeë]-\\?[^a-z]\\{0,3\\}Not[^a-z]\" AHD_watkins1985.txt | head -10\necho \"--- search 'Not.' ---\"; grep -no \".\\{80\\}Not\\. .\\{120\\}\" AHD_watkins1985.txt | head -10",
 "description": "Search Watkins for the negative root"
}
```


### [2026-09-07T15:51:52.270Z] TOOL RESULT

```
730:tive masculus, male, manly: MACHO, MALE, MASCULINE; EMASCULATE.] mat-. A kind of tool. Old English mattuc, mattock (prob- ably borrowed from Vulgar Latin *mattea): MATTOCK. [Pok. 2. mat- 700.] mater-. Mother. Based ultimately on the baby-talk form ma-2, with the kinship term suffix -fer-. 1. Germanic *méthar- in Old English mddor, mother: MOTHER}. 2. Latin mater, mother: MATER, MATERNAL, MATERNITY, (MATRICULATE), MATRIX, MATRON; MADREPORE, MATRI- MONY. 3. Greek métér, mother: METRO-; METROPOLIS. 4, Latin mdteriés, materia, tree trunk (< “matrix,” the tree’s source of growth), hence hard timber used in carpentry, hence (by a calque on Greek Aulé, wood, matter) substance, stuff, matter: MATERIAL, MATTER. 5. Greek compound Démétér, name of the goddess of produce, especially cereal crops (dé-, possibly meaning “earth”): DEMETER. [Pok. mdter- 700.] math-. Worm. With uncertain preform, but clearly re- lated, is Old English moththe, moth: motu. [Pok. 1. math- 700.] [Mawort-. Name of an Italic deity who became the god of war at Rome (and also had agricultural attributes), hence also the name of the planet Mars (doubtless from its red color, the color of blood). Latin Mars (stem Mart-), Mars: MARCH, MARS, MARTIAL, MARTIAN.] mazdo-. Pole, rod, mast. Germanic *mastaz in Old Eng- lish mest, mast: MAST}. [Pok. mazdo-s 701.] me-1. Oblique form of the personal pronoun of the first person singular. For the nominative see eg. 1. Germanic *mé- in Old English mé (dative and accusative): ME, MYSELF. 2. Possessive adjective “mei-no- in Germanic *min- in: a. Old English min, my: MINE?, My; b. Middle Dutch mijn, my: MYNHEER. [Pok. 1. me- 702.] me-2, In the middle of. 1. Suffixed form *me-dhi in Germanic *mid- in Old English mid, among, with: MID- WIFE. 2. Suffixed form *me-ta in Greek meta, between, with, beside, after: META-. See also medhyo-. [Pok. 2. me- 702.] mé-1, Expressing certain qualities of mind. Contracted from *meo-. 1. Suffixed o-grade form *mé6-to- in Ger- manic *méthaz in (i) Old English méd, mind, disposition: MooD! (ii) Old High German muot, mind, spirit, in German Gemiit, spirit, feelings, temperament: GEMUT- LICH, GEMUTLICHKEIT. 2. Perhaps Latin més (< *mé-s-), wont, humor, manner, custom: MORAL, (MORALE), MORES, MOROSE. [Pok. 5. mé- 704.] m6-2, To measure. Contracted from *meo-. I. Basic form mé-. 1. Suffixed form *mé-lo- in Germanic *mélaz in Old English m#l, “measure, mark, appointed time, time for eating, meal”: MEAL?; PIECEMEAL. 2. Suffixed form *mé-ti- in Latin métiri, to measure: MEASURE, (MEN- SURAL); (COMMENSURATE), DIMENSION, IMMENSE. 3. Possibly Greek metron, measure, rule, length, propor- tion, poetic meter (but this is referred by some to med-): METER!, METER?, (METER?), -METER, METRICAL, -METRY; DIAMETER, GEOMETRY, ISOMETRIC, METROLOGY, METRO- NOME. 4, Suffixed form *mé-trd- in Sanskrit mdtrd, a measure: MAHOUT. II. Extended and suffixed forms *mén-, *mén-en-, *mén-s-, *mén-dt-, moon, month (an ancient and universal unit of time measured by the moon). 1. Germanic *ménén- in Old English ména, moon: Moon; (Monpay). 2. Germanic *ménéth- in Old English ménath, month: MONTH. 3. Greek mén, méné, month: AMENORRHEA, CATAMENIA, DYSMENORRHEA, (MENARCHE), MENISCUS, MENOPAUSE. 4. Latin ménsis, month: MENSES, MENSTRUAL, (MENSTRUATE); BIMES- TRIAL, SEMESTER, TRIMESTER. [Pok. 3. mé- 703, ménot- 731. fen Big. Contracted from *meo-. 1. Suffixed (compara- tive) form *mé-is- in Germanic *maiz6n- in Old English mara, greater, and madre (adverb), more: MORE. 2. Suf- fixed (superlative) form *mé-isto- in Germanic *maista- in Old English m&st, most: Most. 3. Suffixed o-grade
732:form *m6-ro- in Gaelic mor, big, great: CLAYMORE. [Pok. 4, mé- 704.] mé-4, To cut down grass or grain with a sickle or scythe. Contracted from *mea-. 1. Germanic *mé- in Old English mawan, to mow: Mow?. 2. Suffixed form *mé-ti- in Germanic *médiz in Old English m#th, a mowing, a mown crop: AFTERMATH. 3. Suffixed form *mé-twd-, a mown field, in Germanic *médw6 in Old English méd (oblique case m&@dwe), meadow: MEAD?, MEADOW. [Pok. 2. mé- 703.] med-. To take appropriate measures. 1. a. Germanic *metan in Old English metan, to measure (out): METE!; b. Germanic derivative *m#t6, measure, in Old English gem&te (ge-, with; see kom), “commensurate,” fit: MEET?. 2. a. Latin medéri, to look after, heal, cure: MEDICAL, MEDICATE, (MEDICINE), (MEDICO); METHEG- LIN, REMEDY; b. Latin meditdri, to think about, con- sider, reflect: MEDITATE. 3. Suffixed form *med-es-, replaced in Latin by *modes- by influence of modus (see 4. below), in: a. Latin modestus, “keeping to the appro- priate measure,” moderate: MODEST; IMMODEST; b. Lat- in moderdre, “to keep within measure,” to moderate, control: MODERATE; IMMODERATE. 4. Suffixed o-grade form *mod-o- in Latin modus, measure, size, limit, man- ner, harmony, melody: MODAL, MODE, MODEL, MODERN, MODICUM, MODIFY, MODULATE, MODULE, MODULUS, MOLD!, (MOOD?), (MOULAGE); (ACCOMMODATE), (COM- MODE), COMMODIOUS, (COMMODITY). 5. Suffixed o-grade form *mod-yo- in Latin modius, a measure of grain: MODIOLUS, MUTCHKIN. 6. Possibly lengthened o-grade form *méd- in Germanic *mét-, ability, leisure, in: a. Old English métan, to have occasion, to be permitted or obliged: MOTE2, MUST}; b. Germanic compound é-mot-ja- (prefix *é-, meaning uncertain, from Indo- hinppoes é, 6; see Pok. é, 6 280) in Old English émetta, rest, leisure: EMPTY. [Pok. 1. med- 705.] medhu-. Honey; also mead. 1. Germanic *medu in Old English meodu, mead: MEAD!. 2. Greek methu, wine (> methuein, to be intoxicated): AMETHYST, METHYLENE. [Pok. médhu 707.] medhyo-. Middle. 1. Germanic *midja- in: a. Old English midd(e), middle: M1D!; AMID; b. West Germanic diminu- tive form *middila- in Old English middel, middle: MIDDLE; Cc. Germanic compound *midja-gardaz, “middle zone” (*gardaz, enclosure, yard; see gher-1), name of the earth conceived as an intermediate zone lying between heaven and hell, in Old Norse Midhgardhr, Midgard: MipGarD. 2. Latin medius, middle, half: MEAN, MEDIAL, MEDIAN, MEDIASTINUM, MEDIATE, MEDIUM, MITTEN, MIZZEN, MOIETY, MULLION; INTERMEDIATE, MEDIEVAL, MEDIOCRE, MEDITERRANEAN, MERIDIAN, MILIEU. 3. Greek mesos, middle: MESO-. See also me-2. [Pok. medhi- 706.] meg-. Great. 1. Germanic suffixed form *mik-ila- in: a. Old English micel, mycel, great: MUCH; b. Old Norse mikill, great: MICKLE. 2. Suffixed form *mag-no- in Latin magnus, great: MAGNATE, MAGNITUDE, MAGNUM; MAG- NANIMOUS, MAGNIFIC, (MAGNIFICENT), (MAGNIFICO), (MAGNIFY), MAGNILOQUENT. 3. Suffixed (comparative) form *mag-yos- in: a. Latin major, greater: MAJOR, MAJOR-DOMO, MAJORITY, MAJUSCULE, MAYOR; b. Latin majestds, greatness, authority: MAESTOSO, MAJESTY; c. Latin magister, master, high official (< “he who is greater”): MAESTRO, MAGISTERIAL, MAGISTRAL, MAGIS- TRATE, MASTER, (MISTER), MISTRAL, (MISTRESS). 4. Suf- fixed (superlative) form *mag-samo- in Latin maximus, greatest: MAXIM, MAXIMUM. 5. Suffixed form *mag-to-, “made great,” in Latin mactus, worshiped, blessed, sacred: MATADOR. 6. Suffixed (feminine) form *mag-ya-, “she who is great,” in Latin Maia, name of a goddess: May. 7. Suffixed form *meg-a-l- in Greek megas (stem megal-), great: MEGA-, MEGALO-; ACROMEGALY, ALMA- GEST, OMEGA. 8. Variant form *megh- in Sanskrit maha-,
---
--- search 'Not.' ---
```


## [2026-09-07T15:52:05.750Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KNT leaf 234 (printed ~210) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==235' KNT.txt | head -c 1200\necho; echo \"=== BRT prohibit ===\"; grep -n -i \"prohibitiv\" BRT.txt | head -10",
 "description": "Check Kent p.210 and Bartholomae prohibitive"
}
```


### [2026-09-07T15:52:07.549Z] TOOL RESULT

```
=== KNT leaf 234 (printed ~210) ===

=== BRT prohibit ===
2366:prohib. :  prohibitiv.
```


## [2026-09-07T15:52:13.077Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"^2[0-1][0-9]\" KNT.txt | head -30\necho \"--- lines with OLD PERSIAN page ---\"; grep -n \"OLD PERSIAN$\\|^2[0-1][0-9] OLD\" KNT.txt | tail -20",
 "description": "Find Kent page markers"
}
```


### [2026-09-07T15:52:14.420Z] TOOL RESULT

```
137:216
4225:2179 The list of provinces is restored by retranslation from the АКК. version; whether both Putayé and Kūšiyā stood in 29-30 depends upon whether the gap at the end of line 21 of the АКК. is adequate to hold both names. 35 vind] Kent, JAOS 58.116-7; ci(£a] Sen 134. *** The restorations are quite uncertain; but cf. Hinz, ZDMG 95.229-32.
5727:200 OLD PERSIAN
5752:201
5762:202 OLD PERSIAN
5805:204
5857:206
--- lines with OLD PERSIAN page ---
4957:OLD PERSIAN
5001:OLD PERSIAN
5055:OLD PERSIAN
5093:OLD PERSIAN
5142:OLD PERSIAN
5185:OLD PERSIAN
5232:OLD PERSIAN
5286:OLD PERSIAN
5334:OLD PERSIAN
5389:OLD PERSIAN
5438:OLD PERSIAN
5484:OLD PERSIAN
5526:190 OLD PERSIAN
5566:192 OLD PERSIAN
5610:194 OLD PERSIAN
5656:196 OLD PERSIAN
5704:OLD PERSIAN
5727:200 OLD PERSIAN
5762:202 OLD PERSIAN
5818:OLD PERSIAN
```


## [2026-09-07T15:52:19.363Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR>5850 && NR<6100 && (/^2[0-9][0-9]/ || /OLD PERSIAN/)' KNT.txt | head\necho \"=== find 210 line num ===\"; awk 'NR>5850 && NR<6100 && /^21/{print NR\": \"$0}' KNT.txt | head\necho \"=== print region around p210 ===\"; sed -n '5880,5920p' KNT.txt | cut -c1-600",
 "description": "Locate Kent printed p.210"
}
```


### [2026-09-07T15:52:20.940Z] TOOL RESULT

```
206
=== find 210 line num ===
=== print region around p210 ===
```


## [2026-09-07T15:52:23.280Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nwc -l KNT.txt; sed -n '5855,5880p' KNT.txt | cut -c1-400",
 "description": "End of Kent file"
}
```


### [2026-09-07T15:52:23.335Z] TOOL RESULT

```
5868 KNT.txt
?rad- vb. ‘direct’ Ау. raz-, Skt. rdj- ‘reign’, Lt. rego ‘I direct, rule’, pIE *reg-; in uradana-, тазіа-.
rādiy postpos. ($133) ‘on account of’, with gen.: NPers. тё, enel. postpos. as in &-rà ‘why’, also particle of various uses, often affixed to direct object for elarity; also OCS radi, postpos. with gen., “оп account of’; 10е, sgoof räd- (5188111), io root in Ski. radh- ‘effect; complete! (not to
206
"rad-, pIE *rej-, with Hz. ApI 280). DB 4.54; DNb 9, 10f; also in avahyarádiy, q.v.
ram- vb. ‘be at peace’, with prefix d, in Arüjyüramna-, q.v.
rasa- present stem of vb., see ar-.
rüsla- adj. ‘straight, right, true’, with nt. as Sb.; ріс. of ?^rad-: Av. réSta-, Turfan РЫ. тай ‘true’, Lt. réctus ‘straight’, pIE *rékto- (593, §93.- n1-2, $106, $122, 5126, $24211). Cf. arštā-. таӣз- iam asf. DNa 59. rdstam usn. DNb 11; asn. DNb 7.
‚ .. rlaryary, see vart-.
Labandna- (or Labnàna-) sb. ‘Lebanon’ (§6, §107), 2 mountain in Syria famous for its cedars. Labanéna nsm. DSf 31.
-vä encl. conj. ‘or’ (8133, $291.11); -vā .. -vä ‘either... or...’: Av. và, Skt. và, pIE *ue, ef. Lt. -ve.  z$apa-ü rawca-paíi-a DB 1.20. hya-»à DB 4.68. imai-vä DB 4.71, 78, 77. yadi- vä DNb 25, 29.
vaina- present stem of vb. ‘see (mid.) seem’: Av. vaéna-, NPers. bindd, Skt. véda ‘knows’, vinddte ‘finds’, Lt. videt ‘sees’, videtur ‘seems’; pAr. *uaid- na-, plr. *yaina- ($69, 588.1, $130, $210.III; Reichelt, Aw. Ер. $157). See also Vidafarnah-. vainümiy lst sg. (4226.1) DNb 36, 36f, 39, 40. avaina imf. DB 2.76, 90; DNa 32. vainataiy mid. as pass. (8235.1) DNb 2; XPa 16
vau- adj. ‘good’ ($11, §153.1); nt. as sb. ‘the good, (religious) goodness’: Av. nsm. vaphus, nsn. vohu, Skt. nsm. vásuş, nsn. vdsu, pIE *yesu-; in Dérayavau-, Vaumisa-, Vahauka-, Vahyazdata-.
Va'umisa- sb. ‘Vaumisa’, a Persian officer of Darius: Elam. ma-u-mi-i8-8a, АКК. ti-mi-is-st, Gk. (Plutarch) Rutens; cpd. of vatu- and mifra- ‘friend’ (849c, $78, $148.ILD): ‘Friend of the Good’ §160.- Ib; cf. MB Gr. $51). Vaumisa nsm. DB 2.49, 51, 62. Vaumisam asm. DB 2.53, 58.
vaz$- vb. ‘grow’, see (Луах${та-.
Waj- vb. ‘be strong’: Skt. vaj-, бјаз- ‘strength’, Av. aof
```


## [2026-09-07T15:52:47.805Z] TOOL CALL #27: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-07T15:52:47.815Z] TOOL RESULT

```


```


## [2026-09-07T15:52:50.299Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (507,540):\n    p=t[i]\n    print('=== leaf',i,'len',len(p))\n    print(p[:200].replace('\\n',' | '))\n    print('...tail:',p[-200:].replace('\\n',' | '))\nEOF",
 "description": "Inspect Klein leaves for page numbers"
}
```


### [2026-09-07T15:52:51.812Z] TOOL RESULT

```
=== leaf 507 len 11879
—  Prob.  fr. F.  massue,  ‘club’,  fr.  VL.  *mattiuca,  fr.  *mat- tia,  which  is  rel.  to  L.  mateola,  ‘a  tool  for  dig¬ ging'.  See  mace,  ‘a  staff’,  and  cp.  masse,  mattock, masjid,  n
...tail:  ‘mouth’.  See mouth  and  verbal  suff.  -ate  and  cp.  mastic.  Cp. also  mandible. | Derivatives:  masticat-or,  n.,  masticat-ory,  adj. and  n. | mastication,  n.  —  Late  L.  masticatio,  gen.  -d
=== leaf 540 len 11754
odHeb.  mdshdbhah,  a  fem.  noun formed  from  the  masc.  noun  moshdbh.  See  prec. word. | Moslem,  n.,  a  Mohammedan.  —  Arab,  muslim, | ‘a  believer  in  Islam’,  lit.  ‘one  who  has  submitted 
...tail: n.  —  See  mold,  ‘a  fungoid  growth’, mould,  v.  —  See  mold,  ‘to  grow  moldy’, moulder,  n.  —  See  molder,  n. moulder,  v.  —  See  molder,  v. moulding,  n.  —  See  molding,  n. mouldy,
```


## [2026-09-07T15:53:10.635Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (514,515,516):\n    print('=== leaf',i, t[i][:150].replace('\\n',' | '))\nEOF\necho \"=== prior agents on KLN offsets ===\"; grep -h -o '\"ref\": \"KLN:[0-9]*\"[^}]*' /home/sfmqrb/git/rishe/data/verification/page-3*.json | head -12",
 "description": "Check Klein leaf 515 and prior KLN ref checks"
}
```


### [2026-09-07T15:53:12.215Z] TOOL RESULT

```
=== leaf 514 at’  (in  physics  it  is  used  in  the meaning  of  ‘a  million  times’,  e.g.  megavolt  —  a million  volts).  —  Fr.  Gk.  pEyap,  fem.  psyiXv],
=== leaf 515 elden,  ‘to  announce’,  fr. MHG.  melden,  ‘to  betray,  report’,  fr.  OHG. meldon,  of  s.m.,  which  is  rel.  to  OS.  meldon,  of s.m.,  OE.  me
=== leaf 516 er,  meninx. Derivatives:  member-ed,  adj.,  member-less,  adj., member-ship,  n. | membranaceous,  adj.,  membranous.  — -  Late  L. membranaceus,  fr
=== prior agents on KLN offsets ===
"ref": "KLN:137",
"ref": "KLN:868",
"ref": "KLN:904",
"ref": "KLN:904",
"ref": "KLN:904",
"ref": "KLN:905",
"ref": "KLN:896",
"ref": "KLN:896",
"ref": "KLN:886",
"ref": "KLN:505",
"ref": "KLN:505",
"ref": "KLN:510",
```


## [2026-09-07T15:53:21.778Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification\npython3 - <<'EOF'\nimport json,glob,re\nfor f in sorted(glob.glob('page-3*.json')):\n    d=json.load(open(f))\n    for e in d['entries']:\n        for rc in e.get('ref_check',[])+[r for n in e.get('nodes',[]) for r in n.get('ref_check',[])]:\n            if rc['ref'].startswith('KLN'):\n                print(f, rc['ref'], rc['status'], rc['note'][:200].replace('\\n',' '))\nEOF",
 "description": "Prior KLN ref_check notes"
}
```


### [2026-09-07T15:53:23.057Z] TOOL RESULT

```
page-300.json KLN:855 partial Klein's labdanum article says exactly what the arrow says — 'Pers. ladan is an Arabic loan word' (KLN_1966.txt line 20927) — but it stands on leaf 459 of the 1966 two-volume scan, i.e. printed p. ~895
page-301.json KLN:137 partial Klein 1966 p.137 (KLN_1966.txt line 4204 = leaf 84; the running head of the preceding leaf reads 'axo- / azyme / 136 / 137', so the azure entry stands on the spread pp.136-137): "azure, adj. - ME. asu
page-301.json KLN supports Klein 1966 p.137 (KLN_1966.txt line 4204 = leaf 84; the running head of the preceding leaf reads 'axo- / azyme / 136 / 137', so the azure entry stands on the spread pp.136-137): "azure, adj. - ME. asu
page-301.json KLN supports KLN_1966 p.137: 'azure, adj. — ME. asur, fr. OF. azur …'; p.868 'lapis lazuli … ML., fr. L. lapis … fr. Arab. lazaward'; and, on the same p.137, 'azulene, n., blue hydrocarbon (chem.) — Formed with su
page-301.json KLN:868 supports Klein 1966 p.868 (KLN_1966.txt line 21216, leaf 466, whose printed page number '868' is on the leaf): 'lathi, also lathee, n., a heavy wooden staff bound with iron (India). — Hind. lathi, fr. Prakrit 
page-302.json KLN:904 supports Klein 1966 vol.2 p.904 s.v. 'loll shraub': «Hind. lal sharab, 'red, wine', fr. Pers. lal, 'red', and Arab. sharab, 'drink, wine'» — Klein too takes Persian lāl 'red' as the source word (grep 'loll  sh
page-302.json KLN:904 supports Klein 1966 vol.2 p.904: «loll shraub, loll shrob, claret (India). — Hind. lal sharab, 'red, wine', fr. Pers. lal, 'red', and Arab. sharab, 'drink, wine' (see sirup)» (grep 'loll  shraub' in KLN_1966.t
page-302.json KLN:904 partial Klein p.904 has the entry but spells it «loll shraub, loll shrob», not 'loll sharob'; the derivation Klein gives («Hind. lal sharab ... fr. Pers. lal ... and Arab. sharab») is the one drawn on the cha
page-303.json KLN:505 supports Klein, KLN_1966.txt leaf 278 (s.v. 'Elohim'): "Heb. Elohim, pl. of Elōah, 'God', of uncertain etymology; possibly enlarged fr. El … Cp. Aram. Elāh, in the emphatic state Elāhā, Syr. Allāhā; Arab. ilāh
page-303.json KLN:505 supports Klein, KLN_1966.txt leaf 278 (s.v. 'Elohim'): "Heb. Elohim, pl. of Elōah, 'God', of uncertain etymology; possibly enlarged fr. El … Cp. Aram. Elāh, in the emphatic state Elāhā, Syr. Allāhā; Arab. ilāh
page-303.json KLN:510 supports Klein, KLN_1966.txt leaf 275 (s.v. 'El'): "El, n., Hebrew name for God. — Heb. El, 'God', of uncertain etymology; possibly related to el, 'strong' … Cp. also the first element in the PN.s Eleazar, Eli
page-303.json KLN:505 supports Klein, KLN_1966.txt leaf 278 (s.v. 'Elohim'): "Heb. Elohim, pl. of Elōah, 'God', of uncertain etymology; possibly enlarged fr. El … Cp. Aram. Elāh, in the emphatic state Elāhā, Syr. Allāhā; Arab. ilāh
page-303.json KLN:510 supports Klein, KLN_1966.txt leaf 275 (s.v. 'El'): "El, n., Hebrew name for God. — Heb. El, 'God', of uncertain etymology; possibly related to el, 'strong' … Cp. also the first element in the PN.s Eleazar, Eli
page-303.json KLN:138 contradicts Klein leaf 84 s.v. 'Babel': 'Heb. Bābhel, fr. Akkad. Bāb-ilu, lit. the gate of God … compounded of bāb, gate, and ilu, god … For the second element see El.' — a loan from Akkadian, not a Hebrew ʾēl-co
page-303.json KLN:505 supports Klein, KLN_1966.txt leaf 275 (s.v. 'El'): "El, n., Hebrew name for God. — Heb. El, 'God', of uncertain etymology; possibly related to el, 'strong' … Cp. also the first element in the PN.s Eleazar, Eli
page-303.json KLN partial Klein leaf 84 'Babel, n. … — Heb. Bābhel, fr. Akkad. Bāb-ilu' and leaf 442 'Ishmael, n. … — Heb. Yishmāʿēl' give no Latin intermediary; leaves 443/523 do give L. ← Gk. for Israel and Michael. Klein ha
page-303.json KLN:1682 supports KLN_1966.txt leaf 891: "Uriel, masc. PN. — Heb. Uri'el, lit. 'flame of God' or 'my light is God'. See next word and El." — verbatim Nourai's gloss. (No printed page numbers in the OCR; only the entry 
page-303.json KLN:1682 supports KLN_1966.txt leaf 891, s.v. Uriel (quoted in full at node 10).
page-303.json KLN supports KLN_1966.txt leaf 221 'Daniel … Heb. Dāni'il, lit. God is my judge'; leaf 277 'Elijah … Heb. Eliyyāh, lit. The Lord is God' and 'Elizabeth … fr. Heb. Elishebha', lit. God is an oath'; leaf 280 'Emmanu
page-303.json KLN partial Klein leaves 221 (Daniel, direct from Hebrew), 277 (Elijah, direct from Hebrew; Elizabeth 'Late L. Elisabeth, fr. Gk.'), 280 (Emmanuel 'Gk. Ἐμμανουήλ'), 692 (Raphael 'Late L., fr. Gk.'), 733 (Samuel '
page-303.json KLN supports KLN_1966.txt leaf 99 'bethel, n., a house of worship. — Heb. beth El, the house of God'; leaf 448 'Joel … — Late L. Joel, fr. Gk. Ἰωήλ, fr. Heb. Yo'el, lit. the Lord is God'; leaf 277 'Elishah … Heb. 
page-303.json KLN supports KLN_1966.txt leaves 99 (bethel), 448 (Joel), 277 (Elishah), 551 (Nathaniel, Nathanael) — quoted at node 20.
page-304.json KLN:505 partial Klein 1966 s.v. Elohim (KLN_1966.txt line 12865, leaf 278): 'Elohim, n., one of the names of God in the Bible. — Heb. Elōhīm, pl. of Elōah, "God", of uncertain etymology; possibly enlarged fr. El. See
page-304.json KLN:505 supports Klein s.v. Elohim (p.505): '…Arab. ilāh, with the article Allāhu (see Allah)' — i.e. Allāh = al- + ilāh, Nourai's arrow exactly. Klein's own Allah entry (p.51) repeats it: 'Arab. Allāhu, contraction o
page-304.json KLN:51 supports KLN_1966.txt line 2240 (leaf 38, i.e. printed p.51 on Klein's two-pages-per-leaf scan): 'Allah, n., Mohammedan name of the Supreme Being. — Arab. Allāhu, contraction of al-ilāhu, fr. al-, "the", and i
page-304.json KLN:164 supports Klein s.v. benzoin (KLN_1966.txt line 4766, leaf 98): 'benzoin, n., a balsamic resin. — F. benjoin, fr. Sp. benjui, which is shortened fr. lo-benjui (the first syllable having been mistaken for the de
page-304.json KLN:875 supports Klein s.v. leban (line 21362): 'Arab. laban, "milk", which is rel. to Heb. lābhān, "white"… Arab. lubān, "frankincense"… Cp. olibanum and the first element in benzoin.' — the two page numbers Nourai g
page-306.json KLN:886 supports KLN_1966.txt line 21660 (the leaf whose running heads bracket pp. 885-886), s.v. 'lick, tr. and intr. v.': '... from the I.-E. imitative base *leigh-, whence also OI. lēḍhi, rēḍhi, also (a later form)
page-308.json KLN:874 supports Klein 1966 p.874 s.v. 'leave, tr. and intr. v.' (KLN_1966.txt offset 5370317, immediately before the page mark 875): 'ME. leven, fr. OE. lǣfan ... rel. to OE. lāf ... OE. belīfan ... Goth. bileiban “t
page-308.json KLN:887 supports Klein p.887 s.v. 'life, n.' (running head 'lifer lilac 888' follows): 'ME. lif, fr. OE. līf, rel. to ON. líf “life, body” ... prop. “continuance, perseverance”, fr. I.-E. base *lip-, “to remain, perse
page-308.json KLN:899 supports Klein p.899 (the entries 'live, intr. and tr. v.' and 'liver, n., secreting organ' both stand just after the page mark 899): 'live ... fr. OE. libban, lifian ... fr. I.-E. base *leip-'; 'liver ... ME.
page-308.json KLN supports Klein has all four: 'locust ... fr. L. locusta'; 'lobster ... ME., fr. OE. lopustre, loppestre, prob. corruption of L. locusta'; 'lizard ... fr. OF. laisard, lesard ... fr. L. lacertus (masc.), resp. 
page-31.json KLN:2 supports KLN_1966.txt line 1142 (p.2, s.v. abdest): 'Pers. āb, water, is rel. to Avestic āp-, OI. āpaḥ (fem. pl.), water; see amnic and cp. the first element in abkari and the second element in doab and in jul
page-31.json KLN:47 supports KLN_1966.txt line 2149 (p.47): 'alembic, n. — ME., fr. OF. (= F.) alambic, fr. OSp. (= Sp.) alambique fr. Arab. al-anbīq, the still, which is formed fr. al-, the, and Gk. ἄμβιξ, cup, cap of a still, a
page-31.json KLN:47 supports KLN_1966.txt line 2149: 'fr. OF. (= F.) alambic, fr. OSp. (= Sp.) alambique' — French from Spanish as drawn.
page-31.json KLN:47 supports KLN_1966.txt line 2149: 'alembic, n. — ME., fr. OF. (= F.) alambic'; line 21755: 'limbec, n., alembic (archaic). — Aphetic for alembic.'
page-311.json KLN:885 supports KLN_1966.txt leaf 476 (printed pp. 884-885), s.v. 'liberal': 'fr. liber, free, fr. I.-E. base *leudhero-s, whence also Gk. eleutheros, free. This base prob. meant orig. belonging to the people ... and
page-311.json KLN:885 supports KLN_1966.txt leaf 476 (printed pp. 884-885), s.v. 'liberal': 'fr. liber, free, fr. I.-E. base *leudhero-s, whence also Gk. eleutheros, free. This base prob. meant orig. belonging to the people ... and
page-311.json KLN:885 partial KLN_1966.txt leaf 476 (printed pp. 884-885), s.v. 'liberal': 'fr. liber, free, fr. I.-E. base *leudhero-s, whence also Gk. eleutheros, free. This base prob. meant orig. belonging to the people ... and
page-311.json KLN:885 supports KLN_1966.txt leaf 476 (printed pp. 884-885), s.v. 'liberal': 'fr. liber, free, fr. I.-E. base *leudhero-s, whence also Gk. eleutheros, free. This base prob. meant orig. belonging to the people ... and
page-313.json KLN:905 partial Klein 1966 p. 905/906 (KLN_1966.txt leaf 487, which carries the printed page number 905): 'loot, n., plunder, booty. — Hind. lūt, fr. OI. lōtam, lōtram, "booty", which is rel. to luṇṭati, "robs, plund
page-314.json KLN:896 supports KLN_1966.txt leaf 482, whose OCR'd page numbers are 896-897: 'liter, litre, n., a measure of capacity. F. litre, fr. earlier litron, ‘an old measure for grain’, fr. ML. litra, ‘a liquid measure’, fr. 
page-314.json KLN:896 supports KLN_1966.txt leaf 482 (OCR page numbers 896-897): 'fr. ML. litra, ‘a liquid measure’, fr. Gk. λίτρα, ‘a pound’' — Nourai's gloss verbatim.
page-314.json KLN:886 supports KLN_1966.txt leaf 476, whose OCR'd page numbers are 886-887: 'libra, n., a pound. — L. libra, ‘balance; Roman pound’, fr. earlier *lipra, whence also Gk. λίτρα ... Cp. librate, deliberate, equilibrium
page-316.json KLN supports KLN_1966.txt leaf 540 (printed ~1008) s.v. mother: 'ME. moder, fr. OE. modor, rel. to OS. modar, ON. mōðir, Dan., Swed. moder, OFris. moder, Du. moeder, OHG., MHG. muoter, G. Mutter, and cogn. with O
page-316.json KLN:948 supports Klein's printed p.948 (KLN_1966.txt leaf 509, page number '948' printed in mid-leaf) carries exactly the māter-family: 'matrix, n., womb. — L. matrix, “womb, matrix, source, origin”, formed fr. mater
page-317.json KLN:946 supports Verified for Nourai's NOTE: KLN_1966.txt has the page footers '946' at line 23090 and '947' at 23091, and the entry at line 23103 (i.e. on that leaf) reads 'mat, adj., dull … fr. OF. mat … fr. Arab. m
page-32.json KLN:2 not_found Klein 1966 vol. I p.2 (KLN_1966.txt form-feed leaf 13, the leaf that carries printed pp.2-3) runs 'abase … abash … abasia … abate … abatis … abattoir … abb … abba … abbacy … abbé … abbess'. There is n
page-33.json KLN:6 supports KLN_1966.txt \f-leaf 15 (= printed p. 6, matches the leaf≈floor(p/2)+12 rule) s.v. 'Aboth, also Abot': 'Heb. Abhōth, pl. of ābh, "father", rel. to Aram. ābh (absolute state), abbā (emphatic state), Ug
page-33.json KLN:655 partial KLN_1966.txt leaf 354 (printed p. ~655, between 'giant' and 'gimel') s.v. gibbon: 'F., a name of Indian origin brought to Europe by the Marquis Joseph-François Dupleix (1697-1763), governor-general of
page-33.json KLN:655 supports KLN_1966.txt leaf 354 s.v. gibbon: 'n., a small, long-armed ape. — F., a name of Indian origin…' — Klein's 'F.' is exactly the French > English step of this node.
page-33.json KLN:6 supports KLN_1966.txt leaf 15 = printed p. 6 s.v. Aboth: 'Heb. Abhōth, pl. of ābh, "father", rel. to Aram. ābh (absolute state), abbā (emphatic state), Ugar. ʾb, Arab. ab, Ethiop. ab, "father"' — Klein's 'ābh'
page-33.json KLN:6 supports KLN_1966.txt leaf 15 (printed p. 6): 'Aboth, also Abot, n., 1) the Mishnah treatise also called Pirke Aboth or The Ethics of the Fathers; 2) name of the first benediction of the Shemoneh Esreh (Jewish
page-33.json KLN:6 supports KLN_1966.txt leaves 15-16 (printed pp. 6-7): 'Abner… Heb. Abhnēr, lit. "my father is light", fr. abh, "father", and nēr, "light"'; 'Absalom… Heb. Abhshālōm, lit. "father is peace"'; 'Abigail… Heb. Abh
page-33.json KLN supports KLN_1966.txt leaves 15-16 and leaf ~430 carry all six as English headwords with Hebrew etymologies: 'Abraham, masc. PN.; in the Bible, the first of the patriarchs…', 'Abram…', 'Abner, n., masc. PN.…',
page-34.json KLN supports KLN_1966.txt leaf 93 (printed p.156) s.v. 'bazaar': 'bazaar, n., a market place. — Ult. fr. Pers. bāzar, ‘market’, which is rel. to Pahlavi vacar, of s.m.' Klein confirms exactly the Pahlavi vačar ~ P
page-34.json KLN:712 supports KLN_1966.txt l.17390, between the printed page markers 712 (l.17381) and 713 (l.17393), i.e. exactly p.712, s.v. 'Hebrew': '… fr. Heb. ‘ibhrī, ‘Hebrew’, lit. ‘he who came from across (the River)’, fr.
page-34.json KLN:712 supports KLN_1966 p.712 s.v. Hebrew: '… which is rel. to Aram.-Syr. ‘abhar, Arab. ‘ābara, ‘he passed across’, Akkad. eberu, ‘to pass over’.' Klein cites the Arabic verb in precisely Nourai's shape and sense.
page-34.json KLN:98 partial KLN_1966 p.98 s.v. Arab: 'fr. Arab. ‘Arab, which lit. means ‘inhabitant of the desert’' — supports the word and the gloss exactly, but explicitly relates it to Heb. ‘arabhāh 'desert' and Ethiop. ‘abra
page-34.json KLN:98 supports KLN_1966 p.98 s.v. Arab: '… fr. Gk. Ἄραψ, gen. Ἄραβος, fr. Arab. ‘Arab' — exactly this node and its parent.
page-34.json KLN:98 supports KLN_1966 p.98: 'Arab, n. — F. Arabe, fr. L. Arabem, acc. of Arabs, fr. Gk. Ἄραψ, gen. Ἄραβος, fr. Arab. ‘Arab … Derivatives: Arabesque (q.v.), Arab-ian, adj. and n., Arabic (q.v.) …'
page-34.json KLN:712 supports KLN_1966 p.712 s.v. Hebrew: 'fr. Heb. ‘ibhrī, ‘Hebrew’, lit. ‘he who came from across (the River)’, fr. ‘ibher, ‘region across, side’, from the stem of ‘abhar, ‘he passed across or over’ … Cp. Habiru.
page-34.json KLN:712 supports KLN_1966 p.712 s.v. Hebrew: 'fr. Gk. Ἑβραῖος, fr. Aram. ‘ibhray, ‘ebhray, fr. Heb. ‘ibhrī' — both forms Nourai prints, in Nourai's order.
page-34.json KLN:712 partial KLN_1966 p.712: 'Hebrew, n. and adj. — ME. Ebreu, fr. OF. Ebreu, Ebrieu (F. Hébreu), fr. L. Hebraeus, fr. Gk. Ἑβραῖος …'. Supports the word and its Latin ancestry, but inserts Old French and Middle En
page-345.json KLN:946 supports KLN_1966.txt leaf 508 (printed pp. 948-949; Nourai's 946 = previous leaf), s.v. 'mat, adj., dull': 'F., dull, lusterless, unpolished, fr. OF. mat, defeated, afflicted, depressed, dejected; dull, fr. A
page-345.json KLN:946 supports KLN_1966.txt leaf 508 (printed pp. 948-949; Nourai's 946 = previous leaf), s.v. 'mat, adj., dull': 'F., dull, lusterless, unpolished, fr. OF. mat, defeated, afflicted, depressed, dejected; dull, fr. A
page-345.json KLN:946 supports KLN_1966.txt leaf 508 (printed pp. 948-949; Nourai's 946 = previous leaf), s.v. 'mat, adj., dull': 'F., dull, lusterless, unpolished, fr. OF. mat, defeated, afflicted, depressed, dejected; dull, fr. A
page-345.json KLN:946 supports KLN_1966.txt leaf 508 (printed pp. 948-949; Nourai's 946 = previous leaf), s.v. 'mat, adj., dull': 'F., dull, lusterless, unpolished, fr. OF. mat, defeated, afflicted, depressed, dejected; dull, fr. A
page-35.json KLN:21 supports KLN_1966.txt \f-leaf 22 (= printed pp. 20-21, running heads 'adamant | 20' / 'adamantean | adept') s.v. 'Adam': "Heb. Adam, lit. 'man', usually with the def. art., ha-adam, 'the man', prop. 'the one f
page-35.json KLN:21 supports KLN_1966.txt \f-leaf 22 (= printed pp. 20-21, running heads 'adamant | 20' / 'adamantean | adept') s.v. 'Adam': "Heb. Adam, lit. 'man', usually with the def. art., ha-adam, 'the man', prop. 'the one f
page-35.json KLN:21 partial KLN_1966.txt leaf 22 = p. 21 gives 'Adam' (from Heb. Adam), 'Adam-ite', 'adamite ... named after the mineralogist M. Adam' and 'Adam's apple', so the page supports the English name; it says nothing ab
page-35.json KLN:37 supports KLN_1966.txt \f-leaf 31 (the printed numeral '37' stands in the middle of the leaf) s.v. 'agent, adj.': I.-E. base *ag-, 'to drive, lead', whence Gk. agein, 'to lead', 'OI. ajati, "drives", ajirah, "m
page-35.json KLN:37 partial KLN_1966.txt \f-leaf 31 (the printed numeral '37' stands in the middle of the leaf) s.v. 'agent, adj.': I.-E. base *ag-, 'to drive, lead', whence Gk. agein, 'to lead', 'OI. ajati, "drives", ajirah, "m
page-36.json KLN supports KLN_1966.txt \f-leaf 51 (≈ printed p.74-78), s.v. angel: 'of Persian, ult. of Sem. origin. Cp. Akkad, agarru, "hireling, hired laborer", fr. agaru, to hire, which is rel. to Aram. agar, eggār, "he hir
page-36.json KLN supports KLN_1966.txt leaf 51 s.v. angel: 'fr. agaru, to hire, which is rel. to Aram. agar, eggār, "he hired", (whence Arab. ajara, of s.m.)' — Klein's Aramaic is Nourai's Syriac node.
page-36.json KLN:74 supports KLN_1966.txt leaf 51 (Klein's angel entry; the leaf→page formula puts it at ≈p.74-78, i.e. Nourai's citation): 'Gk. ἄγγελος … which is rel. to ἄγγαρος, "mounted courier, messenger"; of Persian, ult. o
page-36.json KLN:55 partial KLN_1966.txt \f-leaf 41 (≈ printed p.55-58), s.v. aloe: 'L. aloe, fr. Gk. ἀλόη, "aloe", prob. borrowed fr. Heb. ahalim, ahaloth (pl.), which are perhaps borrowed fr. OI. agaruh, aguruh, "aloewood", th
page-36.json KLN:55 contradicts KLN_1966.txt leaf 41, s.v. aloe: Klein takes Gk. ἀλόη from Heb. ahalim/ahaloth 'which are perhaps borrowed fr. OI. agaruh, aguruh' — Hebrew, not Arabic. And KLN_1966.txt leaf 492, s.v. lute (stringed 
page-36.json KLN:605,914 supports Both entries located and both say what the chart says, though the leaf→page formula puts them slightly higher than Nourai's numbers (the offset drifts across the two volumes). KLN_1966.txt leaf 327 s.
page-39.json KLN supports KLN_1966.txt leaf 297 (~p.570) s.v. 'ether, also aether': 'L. aether, fr. Gk. αἰθήρ ... derives fr. αἴθειν, "to burn", fr. I.-E. base *aidh-, "to burn", whence also L. aedes'.
page-39.json KLN:30 supports Klein s.v. aego- (KLN_1966.txt leaf 28, ~p.32; Nourai's 30 is within the ±2-page tolerance of the leaf-to-page formula): 'Gk. αἰγο-, fr. αἴξ, gen. αἰγός, "goat", which is cogn. with OI. ajaḥ, "he-goat
page-39.json KLN:30 supports Klein s.v. aegis (KLN_1966.txt leaf 28, ~p.32): 'L. aegis, fr. Gk. αἰγίς, "goatskin; the skin shield of Zeus", fr. αἴξ, gen. αἰγός, "goat"; see aego-. For this etymology, suggested already by Herodotu
page-39.json KLN:30 supports Klein (KLN_1966.txt leaf 28, ~p.32): 'aego-, combining form meaning "goat". — Gk. αἰγο-, fr. αἴξ, gen. αἰγός, "goat", which is cogn. with OI. ajaḥ ... Cp. the first element in aegicrania.' Nourai's he
```


## [2026-09-07T15:53:31.047Z] TOOL CALL #31: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:2001 --image 2>&1 | tail -40",
 "description": "Fetch Borhan-e Qate p.2001"
}
```


### [2026-09-07T15:53:38.444Z] TOOL RESULT

```
REF: BQT:2001  PDF: data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf page 84  OCR-lang: fas

اس ه ز کت
مزدقان > با قاف بر وزن پهلوان » نام | کننده که از کندم وکاوری وجوسازند و بعربی
شهرست در قهستان : و با زای فارسی هم هست. | نبین خوانند .
واسح‌آن است ۱ .#8 مزرعهة خالك - کنابه آززمین است
مزدود ؟ - بر وزن پرزور » بمعتی | - وکالید و جند اسان و حیوانات دیگر را هم
شاکرد باشد - ومزدیر را نیز کوبند یمنیشخصی گفته‌اند - وقیروگوررا نیز کویند که محل دفن
که‌کار بکند واجرت بگیرد ۴ . گردن آنان باشد .
مزدور دیو- رمزدوردیوان- مزرعه دانه سوز -کنایه از دیا
شخسی را کوبند که‌کارهای لایعنی کند که در آن وعالم است . ۱
نه فایده دنیا و نه لقع آخرت بجهت او باشد مزده <- بروزن اکره . بمعنی‌چراغدان
و ابنچنین شخصیر! هیزم کش دوزخ نی زگوبند- باشد؛ وباین ممنی‌بتقدیم رای بی‌نقطه هم گفته‌اند
وعاملان و متصدیان دیوانیرا هم گفته‌اند . که بروزن هرزه باشد ‎٩‏ .
مزده پر ؟ - با بای ابجد بروزن مهره م زگ « بفتح اول وسکون نانی وکاف
کر » بمعنی مزدور باشد وعربان اجیر گوبند.* فارمی. درخت بادام تلخ است و هعرب آن مزج
مزر * - بنتح اول وسکون ثالی*ورای | باشد ۷ .
قرشت , بوزه را کوبند و آن چزست مت هز کت ۸ - بفنتح اول و کسرکاف فارسی
۱- « مزدقان ( بفتح اول و سوم ) شهرکیست ازئواحی ری و معروفت و آن بین ری
و ساوه است - و مزدقان شهری است كوچك از شهرهای قپستان . > « ممجم البلدان » - و نام
رودخانه اٍست که از ساوه کذرد . « نزهةالقلوب . مقالةٌ الئه طبع بریل ۱۳۳۱ ص ۹۲ . رك :
موژدقان . ۴ - از: مزد+ ور ( پوند اتصاف ودارند کی) ۳ بر ( بردن ) [ قی: کنجور,
رنجور ] * مزدبر (ه.م.). پپنوی1332200027 « یونکرس۱۱۷ > کردیع ۵20-۷67 « ژابا
س ۳۹۷ :1312071 ( متخدم ) « ژاباس ۳۹۷ . رك : دارمتتر . تتبعغات ج ۱ص ۰۲۹۲
؟۴ - رك : مزدر . ۴ - رك : مزدبر؛ مزدور ۵ ت در « هرز » هم این هعنی
را آورده‌است۹ - ۶ همان مرزه ,منی چراغدان که در رای مهمله گذشت » « رشیدی » و رك :
جهانگیری . ۷ - « مزج بالکر . بادام تلخ وانگبین وقد پفتح .> « منتهی‌الارب > .
۸ - این لغت آرامی است . قی : عربی منجد . اسپانیولی 7316200112 عژابا ص۳۹۷
‌ مز کت آدینه ** مجد جامع :
با چنین ماه چنین جشن بود همچو در مزکت آدینه سرای.
5 « فرخی سیستالی ص ۶۳۹۰ ۰
وآن بنیاد مسجد عربی است .
0 مزدوك - رك : مژدکه .
0 مز دیسا » هزدپنی - بفتح اول و سوم و چهارم : اوستا 1338224188582 ۰ پهلوی
0 او آن صفت و مرکبت از : هزده بمعنی دالا و در عرف آبین زرتشتی بخدا
اطلاق میشود 1 بسنه ۳ بینابمعنی‌ستایش,وكلمةٌ مر کب مزبوریمعنی پرستنده مزداست, خدایی که
زرتشت بجهالیان معرفی کرده . زرتشتیان نیز این کلمه را بدوضورت قوق تلفظ‌کنند. مزدیتا در
براپی « دیویسنا * ست که بمعنی پرستندهة دیو و پیروکیش باطل است . « پورداود . بشتها ج ۱
۲۸« مزدیتا ض ۳-۲ . رك : ماژدیتان ( مصحف مازدینان ) .
```


## [2026-09-07T15:53:48.541Z] TOOL CALL #32: Bash

```json
{
 "command": "ls -la data/verification/sources/refs/ocr/BQT/ 2>/dev/null | tail -20; find data/verification/sources/refs/ocr -name \"*2001*\" | head",
 "description": "Find cached BQT page image"
}
```


### [2026-09-07T15:53:48.631Z] TOOL RESULT

```
-rw-rw-r--  1 sfmqrb sfmqrb   3114 Sep  6 11:25 2417.txt
-rw-rw-r--  1 sfmqrb sfmqrb    561 Sep  6 11:25 2417.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb 161891 Sep  6 11:16 2420.png
-rw-rw-r--  1 sfmqrb sfmqrb   3629 Sep  6 11:16 2420.txt
-rw-rw-r--  1 sfmqrb sfmqrb   2009 Sep  6 11:17 2420.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb 153589 Sep  5 16:27 2427.png
-rw-rw-r--  1 sfmqrb sfmqrb   3424 Sep  5 16:27 2427.txt
-rw-rw-r--  1 sfmqrb sfmqrb   1757 Sep  5 16:28 2427.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb   2615 Sep  4 15:28 31.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb 512022 Sep  5 16:12 333.png
-rw-rw-r--  1 sfmqrb sfmqrb   1339 Sep  5 16:12 333.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb   1508 Sep  4 15:27 58.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb   1931 Sep  4 15:02 70.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb   1606 Sep  4 14:54 72.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb 669351 Sep  5 01:38 733.png
-rw-rw-r--  1 sfmqrb sfmqrb   1152 Sep  5 01:39 733.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb 726576 Sep  6 18:36 829.png
-rw-rw-r--  1 sfmqrb sfmqrb    981 Sep  6 18:36 829.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb 624515 Sep  5 16:20 902.png
-rw-rw-r--  1 sfmqrb sfmqrb   1658 Sep  5 16:20 902.vision.txt
data/verification/sources/refs/ocr/BQT/2001.txt
data/verification/sources/refs/ocr/BQT/2001.png
```


## [2026-09-07T15:53:52.463Z] TOOL CALL #33: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/2001.png"
}
```


### [2026-09-07T15:53:52.948Z] TOOL RESULT

```

```


## [2026-09-07T15:53:52.946Z] INPUT

[Image: original 1650x2546, displayed at 1296x2000. Multiply coordinates by 1.27 to map to original image.]


## [2026-09-07T15:54:12.182Z] TOOL CALL #34: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:2002 --image 2>&1 | head -30",
 "description": "Fetch BQT p.2002"
}
```


### [2026-09-07T15:54:13.760Z] TOOL RESULT

```
(no exact page map; using offset -1917 -> pdf page 85; check the printed number and re-run with --pdf-page if off)
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/2002.png
REF: BQT:2002  PDF: data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf page 85  OCR-lang: fas

م زکو ۱ و
و سکون ثالی و فوقالی » مسجد را کوبند که | بالف کشیده . بلفت زند بمعنی‌ترازوباشد وبعربی
بفارسی خالهٌ خدا و بعربی بیت‌الٌ خواشد ۱ . میزا ن گوبند .

م ز کو ای اول و فتح بالی و کاف مزنده * بروزن رونده» کوزه 1 بخوریرا
مشدد و غیر مشدد بواو کشیده . نوعی از طعام | کوبند - و پمعنی مکیدلی هم‌آمده است ‎٩‏ -
است . ومکنده را نز کوبند که فاعل باشد چه مزیدن

هز که < بکر اول وافتح کاف افارسی, بمعنی مکیدن است .
حوای تیره راکویند ۴ . مز نگ - با کاف فارسی بر وزن

مزمل - بنم اون وفتح ثانی ‏ وکسرمیم ارسطو » خارپشت را گونند و آن جالورست
ِ وسکون لام ۱ لوله‌ای ار ی مشهور ۷ 4

چون برجاب راست پیچند آب از آن ۰ ی
روان شود وا گر بطرف چپ گردانند باینتد واين مزید » پرورل و همنی مکید باشد که
لوله را ببشتر درحمامها وآب انبارهای‌سرپوشيده ماضی مکیدن است ۸ - ودر عربی ابمعنی اضافه
صب‌کنند ۴ - و با تشدید انی وثالث, درعربی و زیاده کرده شده باشد ‎٩‏ .
بمعنی درجامه پیچیده باشد ۴ . مزیدن *۱- بر وزن و معنی مکیدن

زا * -:بکر اول وسکون ثانی‌ویون | باشد .

۹ - تو هشرف تری زهر هردم همچو بیت الحرم زهر مزکت .

سوزنی سمرقندی « رشیدی *.
```


## [2026-09-07T15:54:37.776Z] TOOL CALL #35: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/v2001.txt <<'EOF'\n[Borhan-e Qate', ed. Mo'in, printed p. 2001 (= BQT_v4_picofile.pdf page 84), read from the page image]\n\nHeadword (bottom of right column, entry 8):\n«مز کت ۸ - بفتح اول و کسرکاف فارسی» — continues on p. 2002:\n«... و سکون ثالث و فوقانی، مسجد را گویند که بفارسی خانهٔ خدا و بعربی بیت‌اللّه خوانند.»\n\nMo'in's etymological footnote 8 (bottom of p. 2001), verbatim:\n«۸ - این لغت آرامی است ، قی : عربی مسجد ، اسپانیولی mezquita «ژابا ص ۳۹۷» .\nـ مزکت آدینه = مسجد جامع :\nبا چنین ماه چنین جشن بود        همچو در مزکت آدینه سرای.\n«فرخی سیستانی ص ۳۹۰» .\nوآن بنیاد مسجد عربی است .»\n\n(i.e. \"this word is Aramaic; cf. Arabic masjid, Spanish mezquita [Zaba p. 397]. — mazkat-e ādīna =\nthe congregational mosque: [verse of Farroxi Sistani]. And it [the Aramaic word] is the foundation of\nthe Arabic masjid.\")\n\nNeighbouring headwords on the page (for page identification): مزدقان، مزدور، مزدور دیو، مزده‌بر، مزر،\nمزرعهٔ خاک، مزرعهٔ دانه‌سوز، مزده، مزگ، مزکت؛ footnotes 1-8; running page number «-۲۰۰۱-».\nEOF\ncp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/v2001.txt data/verification/sources/refs/ocr/BQT/2001.vision.txt\nwc -c data/verification/sources/refs/ocr/BQT/2001.vision.txt",
 "description": "Save vision transcript for BQT 2001"
}
```


### [2026-09-07T15:54:37.837Z] TOOL RESULT

```
1308 data/verification/sources/refs/ocr/BQT/2001.vision.txt
```


## [2026-09-07T15:54:41.221Z] TOOL CALL #36: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/mosque",
 "prompt": "Full etymology section for English \"mosque\": the chain through French, Italian, Spanish, Arabic masjid, and any mention of Aramaic/Nabataean origin. Quote verbatim."
}
```


## [2026-09-07T15:54:41.976Z] TOOL CALL #37: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/mosque",
 "prompt": "Quote the full etymology entry for mosque, including dates and the Spanish/Italian/French chain and the Arabic masjid / sajada explanation."
}
```


### [2026-09-07T15:54:45.965Z] TOOL RESULT

```
# Etymology of "Mosque"

Based on the Wiktionary entry, here's the etymological chain:

**Direct Quote:** "From Middle French _mosquée_, from Italian _moschea_, ultimately from Arabic _مَسْجِد_ (masjid, literally 'place of prostration')."

The word traveled through these languages in sequence: Arabic → Italian → Middle French → English. The Arabic root meaning "place of prostration" reflects the Islamic practice of prayer through bowing and prostration.

The entry notes that "mosque" is a doublet of "masjid"—both derive from the same Arabic source but took different paths through European languages.

Notably, the Wiktionary entry does not mention Aramaic or Nabataean origins in its etymology section, despite those languages appearing in the translation list.
```


### [2026-09-07T15:54:47.860Z] TOOL RESULT

```
# Etymology of Mosque

According to the Online Etymology Dictionary, the word "mosque" originates as follows:

"Islamic place of worship and the ecclesiastical organization connected with it," 1717, earlier _moseak_ (c. 1400), also _mosquee_ (16c.), probably in part from French _mosquée_, from Italian _moschea_, earlier _moscheta_, from Spanish _mesquita_ (modern _mezquita_), from Arabic _masjid_ "temple, place of worship," from _sajada_ "he worshipped" + prefix _ma-_ denoting "place."

The entry notes that the term was "mangled in Middle English as _muskey_, _moseache_, etc." This etymological chain shows the word traveling westward through Mediterranean languages before entering English, ultimately deriving from an Arabic root meaning worship paired with a locative prefix.
```


## [2026-09-07T15:54:52.196Z] TOOL CALL #38: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%85%D8%B3%D8%AC%D8%AF",
 "prompt": "Give the Arabic entry مسجد: etymology (root س ج د, form, any note about borrowing from Aramaic/Nabataean/Syriac), and any Persian section (مسجد in Persian). Quote verbatim."
}
```


## [2026-09-07T15:54:53.749Z] TOOL CALL #39: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%85%D8%B2%DA%AF%D8%AA",
 "prompt": "Is there an entry for Persian مزگت (mazgit/mazget) 'mosque'? Quote its etymology verbatim if present (Middle Persian, Aramaic/Syriac source), otherwise say the page does not exist."
}
```


### [2026-09-07T15:54:55.249Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-07T15:54:57.838Z] TOOL RESULT

```
# Arabic Entry: مسجد

**Etymology:** "Noun of place from the verb سَجَدَ (sajada, 'to bow down'). Likely borrowed from a regional Aramaic term for a place of worship, attested in Nabataean Aramaic 𐢓𐢖𐢄𐢅𐢀 (msgdʾ) and in Imperial Aramaic 𐡌𐡎𐡂𐡃𐡀 (msgdʾ) already in the 5th century BCE."

**Root:** س ج د (s-j-d)

**Form:** Masculine noun with plural مَسَاجِد (masājid)

---

# Persian Entry: مسجد

The word is borrowed from Arabic. Alternative forms include مزگت (mazgit/mazget) as Early New Persian (now obsolete) and dialectal variants. It means mosque, with pronunciations varying across Classical Persian, Dari, Iranian, and Tajik forms.
```


## [2026-09-07T15:55:05.750Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad\ncurl -s -A \"rishe-verify/1.0 (etymology check)\" \"https://en.wiktionary.org/w/index.php?title=%D9%85%D8%B3%D8%AC%D8%AF&action=raw\" -o masjid.wiki; wc -c masjid.wiki; python3 - <<'EOF'\nt=open('masjid.wiki',encoding='utf-8').read()\ni=t.find('==Persian==')\nprint(t[:2000])\nprint('#### PERSIAN ####')\nprint(t[i:i+2500])\nEOF",
 "description": "Fetch raw wikitext for masjid"
}
```


### [2026-09-07T15:55:07.270Z] TOOL RESULT

```
9383 masjid.wiki
==Arabic==

===Etymology===
{{etymon|ar|id=mosque|:from|ar:سَجَدَ<id:to bow down>}}
{{ar-noun of place}} from the verb {{m|ar|سَجَدَ|t=to [[bow down]]}}. Likely borrowed from a regional {{bor|ar|arc|-}} term for a place of worship, attested in {{w|Nabataean Aramaic}} {{m|arc|𐢓𐢖𐢄𐢅𐢀|tr=msgdʾ}} and in {{cog|arc-imp|𐡌𐡎𐡂𐡃𐡀}} already in the 5th century BCE, the [[emphatic state]] of which seems to underlie some of the Romance descendants.

===Pronunciation===
{{ar-pr|مَسْجِد|a=LL-Q13955 (ara)-AlNatiq-مسجد.wav<a:MSA>}}
** {{IPA|acw|[mas.d͡ʒɪd]|[mas.ʒɪd]|a=Hijazi}}

===Noun===
{{ar-noun|مَسْجِد|m|pl=مَسَاجِد}}

# {{lb|ar|Islam}} [[mosque]]
#: {{uxa|ar|'''مَسْجِد''' جَامِع|t=central mosque, great mosque}}

====Declension====
{{ar-decl-noun|مَسْجِد|pl=مَسَاجِد}}

====Derived terms====
* {{l|ar|الْمَسْجِد الْحَرَام|t=The Sacred Mosque}}
* {{l|ar|الْمَسْجِد النَّبَوِيّ|t=The Prophet's Mosque}}
* {{l|ar|الْمَسْجِد الْأَقْصَى|t=The Furthest Mosque, Al-Aqsa Mosque}}
* {{l|ar|الْمَسْجِدَان|t=the Two Mosques (of Mecca and Medina)}}

====Descendants====
{{col-top|2|desc}}
* {{desc|afb|مسيد|tr=masyid}}
* {{desc|am|መስጊድ|bor=1}}
* {{desc|grc|μασγίδιον|bor=1}}
* {{desc|ckb|مزگەوت|alts=1|bor=1}}
* {{desc|fa-cls|مَسْجِد|bor=1}} {{see desc}}
* {{desc|syc|ܡܣܓܕܐ|bor=1|tr=masgḏā}}
* {{desc|nl|mesdjid|bor=1}}
* {{desc|en|masjid|bor=1}}
* {{desc|gez|መስጊድ|bor=1}}
** {{desc|am|መስጊድ|bor=1}}
** {{desc|har|መስጊድ|bor=1}}
** {{desc|ti|መስጊድ|bor=1}}
* {{desc|he|מִסְגָּד|clq=1|tr=misgā́d}}
* {{desc|ja|マスジド|bor=1}}
* {{desc|jv|masjid|bor=1|alts=1}}
* {{desc|kqr|mosigid|bor=1}}
* {{desctree|ms|masjid|bor=1}}
* {{desc|la-med|meschita|bor=1}} {{see desc}}
* {{desc|pal||tr=mzgt'|ts=mazgit|bor=1}}
** {{desc|fa-ear|مَزْگِت}} {{see desc}}
* {{desc|kmr|mizgeft|bor=1}}
* {{desc|ota|مسجد|tr=mescid|bor=1}} {{see desc}}
* {{desc|pt|Magide|bor=1}}
* {{desc|ber-pro|bor=1|unc=1}}
** {{desc|tzm|ⵜⵉⵎⵣⴳⵉⴷⴰ}}
** {{desc|mzb|taməzgida}} {{q|Figuig, Wargla}}, {{l|mzb|tamǝzǧida}}, {{l|mzb|tamǝǧǧida}}, {{l|mzb|tamǝždida}} {{q|Mzab}
#### PERSIAN ####
==Persian==
{{wp|fa:}}

===Alternative forms===
* {{alt|fa|مزگت|tr={{fa-xlit|مَزْگِت}}||ENP|obsolete}}
* {{alt|fa|مچد|tr=maččed||dialectal|Hamadan|Isfahan}}
* {{alt|fa|مجد|tr=majjed||dialectal}}

===Etymology===
{{etymon|fa|id=mosque|:bor|ar:مَسْجِد<id:mosque>|tree=++|text=+}}

===Pronunciation===
{{fa-IPA|mas`jid|kbl=masˈjit,māˈjit}}

===Noun===
{{fa-noun|cls=مَسْجِد|pl2=مسجدها|pl=مساجد|pltr={{fa-xlit|مَسَاجِد}}}}

# [[mosque]]

====Descendants====
{{top2}}
* {{desc|as|মছজিদ|bor=1}}
* {{desc|az|məscid|bor=1}}
* {{desc|bn|মসজিদ|bor=1}}
* {{desc|chg|مسجد|tr=mäsjid|bor=1}}
** {{desc|ug|مەسچىد}}
** {{desc|uz|masjid}}
* {{desc|gu|મસ્જિદ|bor=1}}
* {{desc|ks|مٔشیٖد|bor=1}}
* {{desc|mag|महजिद//𑂧𑂯𑂔𑂱𑂠|bor=1}}
* {{desc|mr|मस्जिद|bor=1}}
* {{desc|hi-mid|مسجد|bor=1}}
** {{desc|inc-hnd}} {{see desc}}
**: {{desc|hi|मस्जिद}}
**: {{desc|ur|مَسْجِد}}
* {{desc|kmr|mescîd|bor=1}}
* {{desc|inc-ogu|मसीत|bor=1}} {{see desc}}
* {{desc|inc-ohi|मसीति|bor=1}} {{see desc}}
* {{desc|omr|मसिति//𑘦𑘭𑘲𑘝𑘲|bor=1}} {{see desc}}
* {{desc|inc-opa|مَسِیت|tr=masīti|bor=1}} {{see desc}}
* {{desc|pa|ਮਸਜਿਦ//مَسْجِد|bor=1}}
* {{desc|sd|مَسْجِدِ//मस्जिदि|مَسِيتِ//मसीति|bor=1}}
* {{desc|syl|ꠝꠍꠤꠖ|bor=1}}
* {{desc|tk|metjit|bor=1}}
{{bottom}}

; From {{m+|fa-ear|مَزْگِت}}
{{top2}}
* {{desc|av|мажгит|bor=1}}
* {{desc|ba|мәсет|bor=1}}
* {{desc|ce|маьждиг|bor=1}}
* {{desc|crh|mescit|bor=1}}
* {{desc|dar|мижит|bor=1}}
* {{desc|dv-old|𑤤𑤱𑤬𑤾𑤌𑤱𑤛𑤳|bor=1}}
** {{desc|dv|މިސްކިތް}}
* {{desc|ka|მეჩეთი|bor=1}}
* {{desc|lbe|мизит|bor=1}}
* {{desc|inh|маьждиг|bor=1}}
* {{desc|kk|мешіт|bor=1}}
* {{desc|nog|мешит|bor=1}}
* {{desc|kmr|mizgeft|bor=1}}
** {{desc|lsd|מזגפת|tr=məzgaft(e)|bor=1}}
* {{desctree|xcl|մզկիթ|bor=1}}
* {{desc|omr|𑘦𑘲𑘕𑘲𑘐𑘲𑘝𑘲|bor=1}}
* {{desc|alt|мечет|bor=1}}
* {{desc|tt|мәчет|bor=1}}
* {{desc|tk|metjit|bor=1}}
* {{desc|trk|||bor=1}}
** {{desc|ru|мече́ть|bor=1}} {{see desc}}
** {{desc|lt|mečètė|bor=1}}
** {{desc|uk|мече́ть|bor=1}}
** {{desc|pl|meczet|bor=1}}
{{bottom}}

{{C|fa|Islam|Places of worship}}

==Sindhi==

===Etymology===
{{etymon|sd|id=mosque|:bor|fa-cls:مَسْجِد<id:mosque>|text=++|tree=+}} 

===Pronunciation===
* {{IPA|sd|[məs.d͡ʒɪd̪]}}

===Noun===
{{sd-noun|g=f|مَسْجِدِ|d=मस्जिदि}}

# [[mosque]]

===Further reading===
* {{R:sd:SLA}}

{{C|sd|Islam|Places of worship}}

==South Levantine Arabic==
{{ajp-root|س ج د}}

===Etymology===
{{ety|ajp|:inh|ar:مَسْجِد|text=+|tree=1}}

===Pronunciation===
* {{ajp-IPA|masjid<p:ˈmas.ʒɪd>}}
* {{audio|ajp|LL-Q55633582 (ajp)-Khalil.rantissi-مَسجِد.wav|a=al-Lidd}
```


## [2026-09-07T15:55:32.835Z] TOOL CALL #41: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/meh%E2%82%81",
 "prompt": "Quote the entry for Proto-Indo-European *meh₁ (prohibitive particle): its gloss, descendants (Indo-Iranian mā, Avestan, Old Persian, Sanskrit मा, Greek μή, Armenian mi, Albanian mos), and any references (Pokorny, Beekes)."
}
```


## [2026-09-07T15:55:33.608Z] TOOL CALL #42: WebSearch

```json
{
 "query": "Middle Persian mazgit mosque borrowing Syriac Aramaic msgdʾ etymology New Persian mazgit",
 "max_results": "6"
}
```


### [2026-09-07T15:55:37.959Z] TOOL RESULT

```
# Proto-Indo-European *méh₁

**Gloss:** The entry defines this as a "prohibitive particle: 'don't ...!'"

**Key Descendants:** The reconstructed root yielded:
- Proto-Indo-Iranian: *máH (with further descendants including Sanskrit मा and Avestan forms)
- Proto-Hellenic: *mḗ, developing into Ancient Greek μή (mḗ)
- Proto-Armenian: yielding Old Armenian մի (mi)
- Proto-Albanian: *mē, becoming Albanian mo and mos
- Tocharian A and B: mā ("not, no")

**References:** The article cites Beekes' *Etymological Dictionary of Greek*, Martirosyan's Armenian etymological work, and Dunkel's *Lexikon der indogermanischen Partikeln und Pronominalstämmen* (2014). Note: The page does not include Pokorny citations.
```


### [2026-09-07T15:55:37.960Z] TOOL RESULT

```
<tool_use_error>InputValidationError: WebSearch failed due to the following issue:
An unexpected parameter `max_results` was provided</tool_use_error>
```


## [2026-09-07T15:55:40.477Z] TOOL CALL #43: WebSearch

```json
{
 "query": "Middle Persian mazgit \"mosque\" loanword Syriac masgdā Aramaic etymology New Persian mazgit Armenian mzkit'"
}
```


### [2026-09-07T15:55:48.097Z] TOOL RESULT

```
Web search results for query: "Middle Persian mazgit "mosque" loanword Syriac masgdā Aramaic etymology New Persian mazgit Armenian mzkit'"

Links: [{"title":"SYRIAC LANGUAGE i. IRANIAN LOANWORDS IN SYRIAC - Encyclopaedia Iranica","url":"https://www.iranicaonline.org/articles/syriac-language-i/"},{"title":"Masjid - Mosque | WordReference Forums","url":"https://forum.wordreference.com/threads/masjid-mosque.949738/"},{"title":"مسجد - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D9%85%D8%B3%D8%AC%D8%AF"},{"title":"Aramaic Loan-words in Middle Persian on JSTOR","url":"https://www.jstor.org/stable/24049218"},{"title":"(PDF) The Origins of Middle Persian Zamān and Related Words: A Controversial Etymological History","url":"https://www.academia.edu/35233437/The_Origins_of_Middle_Persian_Zam%C4%81n_and_Related_Words_A_Controversial_Etymological_History"},{"title":"List of loanwords in Classical Syriac","url":"https://en.wikipedia.org/wiki/List_of_loanwords_in_Classical_Syriac"},{"title":"Aramaic - Wikipedia","url":"https://en.wikipedia.org/wiki/Aramaic"},{"title":"Middle Persian","url":"https://en.wikipedia.org/wiki/Middle_Persian"}]

Based on the search results, I can provide you with information about the etymology of the word for "mosque" across these languages:

Middle Persian mazgit is documented, and Classical Syriac masgḏā (masgdā) is attested as a descendant of the Arabic term. In Middle and Classical Persian it was mazgit.

The search results indicate that masjid is generally taken to be a loan word from Aramaic, though the exact etymological pathway shows language contact across the Islamic world. The term also appears in Early New Persian as mazgit, and has descendants in numerous languages including Central Kurdish mizgit.

The Wiktionary entry shows the relationship between Arabic masjid and its descendants across various languages including Middle Persian mazgit and Classical Syriac masgdā, demonstrating how this religious term spread through language contact across the medieval Near East.

However, the search results don't contain specific detailed information about Armenian mzkit' or a comprehensive discussion of the Aramaic etymological base that would explain the full connection across all these languages. For more detailed etymological analysis specifically linking the Aramaic root to all these forms, you may want to consult specialized etymological dictionaries or academic articles on Iranian loanwords in Syriac and Aramaic.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-07T15:56:05.147Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT ma candidates ===\"; grep -n \"ma-tya\\|mä .*nicht\\|mā.*nicht\\|nicht.*prohib\" BRT.txt | head -10\necho \"=== BRT lines with 'ma' at start ===\"; grep -n \"^m[aä]\\b\" BRT.txt | head -20\necho \"=== AVG (Jackson) ma ===\"; grep -n -i \"prohibitive\" AVG.txt HID.txt TLM.txt | head -10",
 "description": "Grep Bartholomae/Jackson for prohibitive ma"
}
```


### [2026-09-07T15:56:05.231Z] TOOL RESULT

```
=== BRT ma candidates ===
3479:langen zu  — ,  teilhaftig  werden',  mit  Al;k. : voAa  xsa^nm  toi  mazdJ ..  apaimä  vTspai yai'l  Y.41.2^'';  — yaiU  .  .  apan5  äangS.- Jyäinm  ä  xia^rnn  . .  Y.^.s  (s.  bei  ä)*i; —  yaha  aam  avat  3^ar»nS  apayemi  Yt. 5.43.  3)  'treffen', vom Geschoss:  yatUt (aHHf)  tanüm  apaynli\X.io.2\.  4)'(ei- nem  Gebot  usw.)  nachkommen',  sva.  'es erfüllen,  befolgen':  abmaoyahe  .  .  aiiihn äainay&  mas  (sd.)  vaca  da'isanakt  mit iyaohnäis  apayantaAei^  "der  die  Worte . .,  aber  in  seinem  Handeln  nicht  befolgt" Y.p-3i.  s)'(^'°^"i  Gegner,  Akk.)gleich- kommen,  sich  gewachsen  zeigen,  bemei- stem':  äal  mqm  aivs  zaraiustrS  anusm- hm  apayeiti  Yt.77. 19.  6)  '(einem  Ge- räusch usw.  mit  derStimme)  gleichkommen, es  gleichtun  können'  (ohne  Obj.) :  yS  gä'^ä srävayeiü  aps  v3  faiti^-sfatne  (sd.) . .  ye%i .  .  fisit  M>asibya  usibya  aiwisurunvaiU apayät  yezi  apffis(sd.)  ..  "..  wenn  er  (den Vortrag)  mit  seinen  eigenen  Ohren  nicht hören  kann,  soll  er  es  (dem  Geräusch) gleichzutun  versuchen  .  ."  N.  2Ö*'.
3574:mä  a' yascis  aom  nar^m  "..  lass  nicht  um  I  Reihenfolge    nach  'der  folgende,    zweite' die  Habe  bringen  jenen  Mann"  Yt  1.3^;' paun'ät    va    naimät   'rat    va    N.S7',    —
4790:der  Richtung:  atcit  dim  aiwyäili'^^  ya dahma . .  ofritis  P.J2.  a)  'begehen,  (einen Weg)  gehen':  mä  dim  psrisS ..yim  xrvan- tim..pantqm  aiwitim^*'''  "frag  den  nicht, .  .  der  den  grausigen  .  .  Weg  gegangen ist"  H.2.17.        S.  noch  No.  26.
4820:—  zu' :  xshms  asamqm  unänö  pärayeinii . .  avi  garS  nmänam  V.  75.32;  —  x3  patti apqm  paräiti  .  .  a^ra  . .  V.  jj.  51;  — xraosyS-taraca  (sd.)  .  .  hv5  urva  paräiti par3.asnäi  amihe  yaia  . .  V,  13. 8;  —  ya- tärö  paurvs  us>hiUaiti  paräiti  vahiltahe atshsus  y .  iS.^d.  2)  'aus  (dem  Haus) gehen  auf  — ,  zum  Zweck  der  Verrichtung von-'  (Akk.):  *kat!lmS  timänahe  a'iauru- fi9m{sd.)  pärayäf^''  N.  /;—  para  paoiryö äiti  (näml.  a^aururitm)  para  bityö  aiti para  "hrityS  äiti  aita  paräyaiti  ycc^a gae'^äbyS  *k)nti  "es  geht  der  erste  (auf Priesterdienst)  aus  . .  der  zweite  . .  der dritte.,;  es  gehen  die  weg,  die  (zum  Schutz) für  den  Hausstand  da'gelassen  worden) sind"  N, 2 (?)"'; — katärsm  *ä'irava  ctiauru- n>m  Vä  parayat  galiaiiqm  vä  asp^nns (sd.)  avat  N.^;  —  katärS  a'^aurun?rn ''parayat  nSirika  vä  nmätiSpaitiH  väi yezica  vä  ga^hä  vTmä  (sd.)  *katarascit ''parayat  N.  5;  *5";  —  *cvät  ''aiwtstXm parayap  'irixsapar>m  .  .  yS  haoys  (sd.)  . . paräiti  nsit  .  .  anaiwistim  (sd.)  ästryanti N.  4.  a)  mit  haca  und  Instr.:  cval  .  . äiirava  a'iaurumm  haca  ^gafi^äbis^para' yat  N,  4-  3)  'sich  an  etwas  (Akk.) machen':  yö  nar)m  ..  kasyat»he{%d.)  sanhai daoaili  vl^va  aval  hava  xraiwa  paräiti "—  wissentlich  mit  voller  Absicht  macht  er sich  daran— "V,  15- 2.  4)  'hingelangen zu  — '  sva.  'sich  verschaffen':  ffi.j(Akk.),. kaine-.tarS  äaxit^m  pärayät  tarS  ap»mca urvarqmfa  yezica  . .  tarS  (sd.)  daxst>m paräiti  . .  "nicht  soll  das  Mädchen  heim- lich sich  die  Regel  (wieder)  verschaffen, heimlich  sich  Wasser  und  Kraut  verschaf- fen .."  V.i5,9f.
5172:•  p.  avahya-rädiy  adv.-artige  Verb. 'aus diesem  Grund,  deshalb':  äspiU pit-ii  haxä- manil  .  .  av  haxamanisiyä  'itahyümahy Bh.  /.  3;  —  tyt^  manä  kartam  avaiii (sd.)  *aiava^  av  mä  apagaudaya'^  Bh. 4-10.  a)  mit  folg.  yai^a  'weil':  av <^urJ^mazdä  upaitSm  abar^  .  .  ya>il naiy  ar'tkt^  abavam  Bh.  4.13.  b)  mit folg.  («(7)  tyt^  'damit  (nicht)':  av  naiy nipislam  (sd.)  mütyt^  .  .  aj'ahyä  paruv *>adayä^  (sd.)  Bh.  4.8;  —  av  hlram avdjaniy^'  matyJ'mäm  xsnasätty  (sd.) (fffl*  ..  "deshalb  möchte  er  die  Leute  töten, damit  sie  nicht  .  ,'">  Bh,  j.  13.
6593:—  "^wBi  dütsnhs  anhämä  tsng  därayö (sd.)  Y.J2.  i;  —  negirt:  hs  n5it  äs  vaoze\ (sd.)  .  .  P.  48.  II)  'werden,  geschehen,  1 stattfinden'.  A)  II  im  Ap.:  itnJ'  tyt^  akuna-  j vam  vasna  a''urJ'inasdäh^  ahJ'  "das,  | was  ich  tat,  geschah  nach  AhM.%  Willen" . Bh.  4-  2.  B)  im  Aw.:  vaocä..täcU  mazda ahurä  yä  nöit  vä  aahat  anfiaitx  vä  ".  .  von all  dem,  o  MAh.,  was  nicht  geschehen oder  aber  was  geschehen  wird"  Y-jz-S;
7034:kniipfiiDg  eines  adversativen  Satzes  'aber; sondern;  vielmehr;  gleichwohl':  iha  main- yete  dus:^armä  .  .  ä'  az3M  manya  Yt.  10. losf.;  —  nöil  .  .  vispa  yasathahs  .  .  ä' .  .  aÄ'J  zara%uitro  Vt.  IJ.  ig;  5,  55  aSt^', N.55,  Y./0.8,  ig.  5;  —  iä  fi-avasays  .. aojistä  hinti  .  .  yä  .  ,  saosyaniqm  ä° anyalsqm  fravasayö  (sd.)  ,  ,  Yt.  jj.  17; N.  102;  —  nabänazdists  ä'  kavatqm  nana (sd.)  N.  Ig;  g,  67;  —  «/  zaotars  (sd) kairim  avAap. .  3'  AävanänS  (näral.  kairim a»Aat)  yat .  .  N.  72;  73-'j6,  66'';  —  apqm . .  yä  para  ahmäi  hist>nta  .  .  ä°  th  nüram p-aiacin/i  Yt.  13. 5:i(.;  56,  5S;  —  aat{^.  8) yahmäi  xsnBtS  bavaiti  mi^rS  ahmäi  jasaiti avaiäAe  ä'  yahmal  ibistd  bavaiti  . .  akmüi früiiinäayeiti  nmämmca  ..  Yt/o.S?; yaike  xsa'hriäa  nStt  aotfiri  ar?ka  . .  para akmat  yat  . .  ä°  yat  ..  ". .  bevor  . aber  als  . ."  Ytig.$$f.;  — yat  hf puhi iissaySi^e  .  .  ikaisö  anyö  .  .  ä°  anys Y.g.ia;  —  tarS.d»nanS  (sd.,  näml.  urv rayä  aahari)  .  .  ä°  up»ma  aisöJräjanAa N.po; —  navajcsaparfm  ..  aivii^äi kama  mazäräjaAlmW.^.^2;'^.46,47,5o; —  nöit  ahmt  nmäne  *sänaite  ä^rava  .  . ä'  .  .  sayänie  dahaksea  "nicht  werden  .  , geboren  .  .,  sondern  es  sollen  geboren werden  .."  Y.  //.6;  —  käu  .  .  yff  .  .  van- tasea  Aqm.räzayeili  .  .  aha  diin  upaJaosa^ yati  .  .  raZiayaca  (sd.)  .  .  ä'  yat  .  .  var>- saica  *hqm.räzayar>Aa  .  .  aat  (s.  7)  .  . pascana  apa.baröis  ". .  vielmehr  wenn  du dir  die  Haare  ordnest  .  .,  so  sollst  du dann  . ."  V.iy.2—4;  —  attm  vispanqm dämanqm  nipäta  ahmi  .  .  ä'  ('gleich- wohl') ma  nöit  masyäka  .  .  yazante  YL 10. 54.  a)  bes.  mit  a)  folgendem  _ya/  oder
7699:rechte  Weg"*:  yS  zaotil  asä  "zö/  (AP.) hvd  *mainySuf  H  vakHiilt  kayit  (sd.)  Y. SS'^'i  —  '"^  äng^'ote  *mar»daili  damä *'zaos'^  Aai%Tm  "so  macht  sich  das  Ich des  Z>/-»^enossen  den  gewissen  Lohn  des rechten  Wegs  zu  nichte"  \.$i.i:i^.
8860:amanha  asti  masyd  gfurvaya  hl . .  zUvarp Y.p.28;  —  ai  .  .  mainyßm  zara%uströ v^jtttl  (sd.)  yaste  I  ascil  spSmstd  Y.  43.16; —  ySi  mffi  ahmii  s^rao/^m  dqn  I  cayasla (NP.) "'  upä.jimm  (sd.)  . .  ". .  die  mir  ihm Gehör  schenken,  all  die  .."  Y.415,5;  —  MiSl Spants  mainyti  ,  .  asäunl  cBÜ  (sd.)  yä  3i lelcä  vakistä  .  .  drvgvä  baxhitf  (sd.)  Y. 47.  S ;  verwend.  12.  i ;  — *spaydti  vispa  tä ^aobna  yä  I aca  (APn.)  virxyäti  V.J. 4)  in  negativen  Sätzen  'irgend einer",  mit  der  Negation  'keiner,  niemand, nichts';  im  Ap.  mit  folgendem  (iy\  nur substantivisch:  tnä  Icis  at  vi  dngvatS mq^rqscä  gs/tä  säsnas^ä  (sd.)  Y.31.1S; Mä  läfpaurvö  bäioyalfa  nS  Y.ff.21; 10.123,  /7.54; — mä  lafiars(sd^)  a:vs yat  tristem  V,j.i4;  —  nStt  zi  iü^  aAhä drujs  nyäsäite  (sd.)  FrW.  8.1;  ■ —  naioa jainti  na^a  fraSsyäti  (sd.)  "keiner vermag  . ,"  Hx.  14.^/6;  —  atvahe  . .  zänu.- asti  äfritiS  (sd.)  .  .  "israyqm  naiäa I tti  V.  iS.ii;  —  n3it  cahmi  sasva  (sd.) yS  .  .  FrD._j;  3;  —  mi^r^m  .  .  yü  nffii kahmili  ai7tii.draoxls  Yt.  io.  17;  —  II  mit kasäy  naiy  adari'naus  (sd.)  i  cilay (ASn.)  '^astanaiy  .  .  "wer  immer  es  war, er  wagte  nicht  irgendwas  zu  sagen  .  ." Bh. /.  13,  a)  mit  Gen,  part:  nöit  zt l  eis  asraosyanqm  tanunqm  asahe . ,  viaäiti P.  /j ;  —  mi^rjm  . .  yö  nöit  kahmät  mi'^rS.- drujqm  .  .  aojS  daiiäiti  Yt. /O.62;  62;  — yaiia  vli..yakmai  ttStt  cahmäi  naiitianqm karaiia  (sd.)  pairi.vasnei'^e  Yt. /_j,  3;  — nsit  iahmäi  ap>r»näyunqm  N. //;  —  D  mit Uy:  naiy  aha*  (sd.)  marttyJ'  naiy  pärsi^ .  .  naiy  amäxam  taumäyä  kalay  hyt^  .  . Bh. /.  13,  5)  gAw.  im  Nebensatz  mit yes%   'jeder',    substantivisch:    kadä    valdä
10198:nät/rä  1)  Inkoh. 'aufwachen':  h3  s^af- iiä'ia  frayris>mnS  H.  /.  13;  —  x^a/ttät /rayris;»Nnauqmll.i.i3\ai.  2)Kaus. 'aufwecken': rt'fl.^Mi'  dahmät  aoxte *frii'i^  mä narf  *gärayBis  yat  ratus  frilsis  *äjasäl'^ vXiaiti  dim  frayrärayS  nOitfrayräyräyäti aliff  ratufris  *yd  jayära  "Ein  D.  sagt  zum andern:  'Weck  mich  auf,  Mann,  wenn  die Gebetastunde  kommt'.  Der  iibemimmts ihn  zu  wecken,  bringt  ihn  aber  nicht wach.  (Dann)  ist  der  r.,  der  wach  war" N.  ig;  —  sraesB  a^'Ö  aotn  mtnyim  fra- yrsrayeifi  pars.dari  tiqma  V.  /tS'.  33,
=== BRT lines with 'ma' at start ===
3574:mä  a' yascis  aom  nar^m  "..  lass  nicht  um  I  Reihenfolge    nach  'der  folgende,    zweite' die  Habe  bringen  jenen  Mann"  Yt  1.3^;' paun'ät    va    naimät   'rat    va    N.S7',    —
7945:mä:uiayasmm  frapinaeiti  V.  ^,  3 1 ;  —  urva- "iamlit  ziayemi  avt  •mai  varS  Yl  12. 3 (vgl.  12.4,  wo  avat);^  °mal  iimltum  yaol- diiiätu  .  .  'map'>  ätram  .  .  "mat^  apim . ,  °mat^^  zqttt  ,  .  °maO^  gqm  .  .  *maj^' un-arqm  .  .  'mat>^  nartm  asava/um  .  . 'mal^  näiriiqm  V.  ij.4— 7 ;  —  'm^rn  hao- m?m  .  .  äyese  yesti  'mqmca  gqm  .  .  °mä zaoira  .  .  °tnq  asmqsca  baoioTmfa  Y.  22. 1-3;  >.  3.  2.'i*.  ^.4,  4-i\  3.  ^ö-i.  GS. 14.  7^-23;  —  {ävaihayama/it)  'mq  kaomq 'ma  haomya  'ma  stania  "ma  myazäa  "ma asma  .  .  'ma  (AD.)  asmana  Aävana  .  , 'ma  ayaahama  Mvana  .  .  °mqm  Sp)m  .  . 'inat  barasma  .  .  °ma  kihrpasca  DvTslsca 'mH  ..  :ao^ra  "mrm  haomim  Vr. //.  at; —  paiti  ti  trarrfa  .  .  'mä  srvä  va^a- yemi  .  .  °mäs>  tE  srvä  m»yya  .  .  kyHr? arstayasca  Y.ij.g;  9;  —  'iru>m  U  nanm nisrinaomi  V.  /i".  5 1 ;  5 1 ;  —  D  °mam  psrsam ksram  psdiy  yadiy  karJ'  parstr  pst<^ ahatiy ..\i.$.y,—<^urJ'mttzäSmaiy  upasläm abarc/'  yätä  °mt^  xio^j^am  adäry  voinil (^uri^masdah!^  °«ni*  xia%''am  dilrayämiy Bh. /.  9;ll —  nSit  °mal  vTsp>m  düivarstsm .  .  mObrS  vaenaiti  Yt  ro.  10g.  a)  sub- stantivisch: D  draug^dif  hami'h''iyä  aku- nat^ ty(^  'maiy  karam  adurujiyasti'"..yie^ die  hier  (näml-  die  abgebildeten  Empörer) das  Volk  belogen  haben"  Bh.^.  4 ;  —  'me  nö ..aspapara.-nay enteist.)  'me  nS..*bäzava sHndayänii  (sd.)  Yt. /0.4z.  a)  mit  einem erläuternden  oder  ergänzenden  Relativ; a)  adjektivisch:  -mat  karhara  yät  ifani- ra>>m  Y. 57.31,  Yt  70.15,  133,  JB.15, H.  /.  14;  —  alis  .  .  rämyat  im  upa  'mal nmänsm  yat  äküiri  Y.  10.  i ;  —  ima  asäsca sOdrasca  . .  'msm  sBdrahe  paüim  ytm ahunm  Y.  2.16;  —  °mqm  dasriqm  yqm sAäirfm  YtÄgg;  —  'mqm  .  .  tqm  . .  yä nS  baraitt  Y.jS.i;  y.i;  —  vTspä  'mä 3ps  ys  amä  patti  /rataSnii  Y.  (»5. 3 ;  — 'mqm  tanüm  yä  ml  vaSnaite  huraoha  Y. /o.  14,  ß)  substantivisch:  vispgm  'mal
11039:ma^m  .  .  hyat  vä  .  .  akaica  mainyui  .  . iyaoiatum  ..fracinas  . .  xsay3(sä.)  "..  (er) und  der  böse  Geist , ."  Y,^3. 5.  a)  die Glieder  sind  verbal;  a)  sie  folgen  sich unmittelbar:  jiavat  isai  tavlcä  Y.  2Ä4; 43.  8;  —  yi  zl  Sin pnghatUa  Y.J/.  14;
14527:mä  'itf  sd.  und  Bthl.  Sind.  3.  159  No.  3.  —
17305:ma-  Adj.  'der  unter  den  vom  Zweifiissler abstammenden  am  meisteti  vom  Zweifiissler abstammt*:  °mp/n  janät  "mtm  tbaäayat Yt.J.  15.
19372:mä  apalma*paurväpaySit(Sp.S'jo\L)  mäK. *»iaSa(sd.)  ia^anna  *paiti.Jime{s6.)  Vr.22. 2; —  ma  dim  mntyä  ä%ravan»m  ..tim  dim mruyä  ä^ravarum  . .  yn .  .Y.1S.1  —6;  — ma  hrayam  vahiStanqm  atwt^yS  buyata  . . %rayqm  acistanqm  amihyj  buyata  V.  t8. 17;  —  ma  mihrake  . .  vaFfai  jasaima Yt  10,  98;  98;  —  mä  buyh  aurvaiqm yaxta  ma*  . .  Y.  11.  7;  g.  29';  —  ma x/ayamna  jasSit  atrrm  ma'  .  ,  Y.g.zyi 'S-49i —  "»ä  mqm  ..fraspaysis  tiX>%.li8\ Yt.  8.  593,  FrD.  4J,  Vyt  12*,  j-j,  J7 ;  — ma  Bs*^  mi ankam  sao^ranqm  vindita yä ..mä  fiarB pairi/ta.xsulrif  mai . .Yt IJ.S4',
20299:mä* . .  m'  (näml.  'soll  es  geschehen")  ya/ «J  uyra.bäxäu!  nivana^  Yt  10, 75.
20301:mä  aia,
21290:mä  t)m  urv£i>m  ß-ayavaysis  "nicht  sollst
21877:ma>ä  (sd)  .  .  Y.^2. 4;  —  /aü"  j^  ^tKka-
24372:mä  buyama  säürlljricd  nrä  nmSnS.irUo  mä
24745:mä  /is"  Öarff  (sd.)  atvS  yat  irisigm  V.J.  i«  j.  'raeOTva-  n.  i)  'Mengung'  (nur 14;  14;  — frasa  /rayöit  iristitn  uziar^J  Komp.).  2)  'Wirrnis':  kqmat  vil  *aipya- V.6.2T,  5.  41;  —  J'S  vastnm  vpavharv-'  nqm  (sd.)  hmtxm  kqmHt  vä  'wanqm  Yt. zaiti  upairi  ait»m  tristem  V.  <S'.  23;  af.',  4-5"-
=== AVG (Jackson) ma ===
AVG.txt:4246:d.  Negative.     Av.  m&  'not*  (prohibitive)  =  Skt.  md.
AVG.txt:4804:Note.  Original  mS  (prohibitive)  appears  as  ma-  in  composition  in YAv.  makasvil  mastrt  'no  dwarf,  no  woman'  et  al.  Yt.  5.92;  GAv.  ma- vaefa-  'not  failing'  Ys.  41.1.
```


## [2026-09-07T15:56:06.883Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D5%B4%D5%A6%D5%AF%D5%AB%D5%A9",
 "prompt": "Old Armenian մզկիթ (mzkitʿ) 'mosque': quote the etymology — is it from Middle Persian mazgit, Arabic masjid, or Aramaic? Any cited authorities."
}
```


### [2026-09-07T15:56:12.626Z] TOOL RESULT

```
# Etymology of Old Armenian մզկիթ (mzkitʻ)

According to the Wiktionary entry, the Old Armenian word derives from "Classical Persian _مزکت_ (mazkit), _مزگت_ (mazgit), from Middle Persian [script needed] (mzgt' /⁠mazgit⁠/), from Arabic _مَسْجِد_ (masjid)."

The cited authority is Hübschmann, Heinrich (1897), *Armenische Grammatik. 1. Theil: Armenische Etymologie*, Leipzig: Breitkopf & Härtel, page 271.

No Aramaic origin is mentioned in this entry.
```


## [2026-09-07T15:56:26.488Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HUB/HRN Moschee ===\"; grep -n -i \"moschee\\|mazkit\\|mzkit\\|masgid\" HUB.txt HRN.txt | head -10\necho \"=== BRT leaf/cols for line 19372 ===\"; python3 - <<'EOF'\nt=open('BRT.txt',encoding='utf-8',errors='replace').read().split('\\n')\nfor ln in (19372,21290,20301):\n    leaf='\\n'.join(t[:ln]).count('\\f')\n    print('line',ln,'leaf',leaf)\nlf=open('BRT.txt',encoding='utf-8',errors='replace').read().split('\\f')\nimport re\ni='\\n'.join(t[:19372]).count('\\f')\nfor j in (i-1,i,i+1):\n    nums=re.findall(r'\\b11[0-9][0-9]\\b', lf[j])\n    print('leaf',j,'4-digit 11xx nums:',nums[:10], '| head:', lf[j][:80].replace('\\n',' '))\nEOF",
 "description": "Find Bartholomae column for ma and Hübschmann/Horn"
}
```


### [2026-09-07T15:56:28.074Z] TOOL RESULT

```
=== HUB/HRN Moschee ===
=== BRT leaf/cols for line 19372 ===
line 19372 leaf 610
line 21290 leaf 697
line 20301 leaf 647
leaf 609 4-digit 11xx nums: [] | head:  5',  5';  — yä  näirika  'paiti  virnyantiQ) N.  6;  —  %wqm  kaimnS  .  .  x/a
leaf 610 4-digit 11xx nums: [] | head: i-  Adj.  (nyäAtai  NP.).  —  Pö.  (la  V.  7p, YL  //):  nikänSff),  (in  V.  5
leaf 611 4-digit 11xx nums: [] | head: Sayä  tadhrayä  fratiharmiu  har?tS  *ma iafts^^  *ffia5  ,  .  Yt5.  9»;  93J;
```


## [2026-09-07T15:56:43.700Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD ma neg ===\"; grep -n \"^mā\\b\\|^ma \\|^mā \" PHD.txt | head -10\necho \"=== NYB ma ===\"; grep -n \"^mā\\|^ma\\b\" NYB_vol2_glossary.txt | head -10\necho \"=== MON نهی prefix ===\"; grep -n \"حرف نهی\\|ادات نهی\\|پیشوند نهی\\|م. نهی\" MON_part2.txt | head -10\necho \"=== FFD prohibitive ===\"; grep -n \"نهی\" incoming/FFD/FFD_pages.txt | head -8",
 "description": "Grep MacKenzie, Nyberg, Mo'in, Abolghasemi for prohibitive ma"
}
```


### [2026-09-07T15:56:43.815Z] TOOL RESULT

```
=== PHD ma neg ===
437:ma [AL < À °l | M m, N ~] not (prohibitive). ~ agar [N magar] perhaps; lest. mad [AM < A ?m-y, v. madar | M md] mother.
=== NYB ma ===
2392:maé0ana- ‘dwelling-place’. The change of -&h- > -äh- before a consonant is characteristic of the SW language.
2397:mālišn [m>lšn'], v. n. of the following vb., of the soft touch of a fragrant wind 73%,
2403:mānā(k)kāi
2409:mānākēh 125
2411:mānākēh [m’n’kyh] similarity 11220, — Abstr. of mänäk, MPrs m'n'g ‘similar, like’ (S, A-H II, Verbum 177); Paz. manda; NP mana ‘seemingly, probably’ (Sn); mänistan ‘to resemble’. Cf homänäk.
2414:māndakēh fatigue 1471. — NP mändagi from māndah ‘tired’.
2416:mānēh [m?nyh] settlements, coll. of man (g. v.), 11418.
2423:mānišn [m'nšn'] dwelling, dwelling-place 5814 1075-12, 1179. — V. man. .
2424:mānišnūmand [m’nän’wmnd] possessing dwelling-places, well populated 574,
2425:māništ [m”?nyšt'] abode 8611. — Paz. mą- nastan (Mx).
=== MON نهی prefix ===
44611:مباد: ۱۵ |م. نهی + باد (فعا. صيغه دعا 
68899:مه: 72علامت نهی. نشانهة دعای سمنفی که 
=== FFD prohibitive ===
```


## [2026-09-07T15:57:00.842Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SKT ===\"; grep -n -i \"mosque\" SKT.txt | head -5\necho \"=== FSD ===\"; grep -n -i \"mosque, n\\|mosque \" FSD_vol3.txt FSD_vol2.txt FSD_vol4.txt 2>/dev/null | head -5\necho \"=== WEB ===\"; grep -n -i \"mosque\" WEB_vol1.txt | head -5\necho \"=== DEV ===\"; grep -n -i \"mosquee\\|mosquée\\|mesquita\" DEV.txt PHN.txt LAM.txt DOZ.txt | head -10",
 "description": "Grep English/French sources for mosque"
}
```


### [2026-09-07T15:57:00.972Z] TOOL RESULT

```
=== SKT ===
11917:Mosque,  a  Mohammedan  temple.  (F. —  Span,  —  Arab.)  F.  mosquhx  Cot.  — Span,  metquiia,  a  mosque. —  Amb.  masJaJ, masjid,  a  temple,  mosque.  —  Arab,  root sajada,  to  adore,  prostrate  oneself.
11919:musket  (F.-Ital-L.)  O.Y.nunis- put,  ft  musket,  orig.  a  kind  of  hawk ^another  &oit  of  gun  was  called  a y^/<[On^/, another  a  saJker,  a  kind  of  hawk).  —  Ital. mosquefic,  a  musket,  oritf.  a  kind  of  hawk, so  called  from  its  smalt  size.  Dimin.  of Ital.  mffsca,  a  Hy.  — L.  mitsea,  a  fly.
23699:French  from  Spanish  from  Arabic,  am* ber,  cotton  (i),  fonfnre,  galingale,  garble, garbage,  genet,  ;ennet  (genact),  lackey Jacquey).  mojJc  (masque),  masquerade, mosque,  ogee  (ogive),  racket  (1)  traquct), realgar,  ream,  »umach,  syrup  (sinip),  tabby, talc,  tare  (3),  tariff,  zenith,
=== FSD ===
FSD_vol3.txt:38188:Mlhrab of the Mosque El Moyci,
FSD_vol3.txt:54700:mosque of a riiy is culled a Jaina magjld. See plat*
FSD_vol3.txt:57920:edges, and serving as a distanee-picce - mud-saurar, a. tuhiaret of a mosque moMS iln;; mu-ed dint*
FSD_vol2.txt:41293:3.  A   sanctuary  or  holy  place  prohibited  to  all  but  the Faithful;  specif.,  the  mosque  at  Mekka  or  Medina  and its  neighborhood.  4.  A   group  of  cow'  seals  that  follow  a bull  seal.  [<  Turk,  harem,  <   Ar.  hardm,  anything forbidden,  <   Aarattm,  forbid.)  ha'reemt.— ha'rcm-lik,  ti. The  women’s  apartments;  opposed  to  selamlVc,  the  men’s apartments.
FSD_vol2.txt:66978:Kebh'snauf,  I   keb'snauf,  2   kjb'snouf.  n.  Egypt.  Mytti.  A hawk-headed  genie  of  Amentl  having  charge,  In  embalm- ment, of  the  liver  and  gall-bladder,  Qebh'siiauf]:. keb'lah,  l   keb'le;  2   k5bTa,  n.  [Ar.]  1,  The  direction  of  the :   Kaaba  in  Mekka,  toward  which  the  Mohammedan  worshiper turns  in  prayer:  marked  on  the  interior  wall  of  a   mosque  by a   nlehe,  or  mihrab.  2.  Any  object  of  devotion  or  passionate _   desire,  keb'laf.
=== WEB ===
14422:äzän’, n. (from Ar. ddhan.] the Moslem sum- mons to prayer: it is usually ¢alled five times a day by the muezzin, from a minaret on the mosque.
94749:1. a Moslem priest who performs the regular service of the mosque.
103139:Kiia’ba, Ciia’ba (ka’), n. |Ar. ka'bah, a square building, from ka’b, a cube.] the sacred Mos- lem shrine at Mecca, toward which believers turn when praying: it is a small stone struc- ture in the court of the great mosque and con- tains a fabled black stone supposedly given to
103510:ter (kaph) of the Hebrew alphabet, corre- sponding to Scottish ch, asinloch. — Khi’ya (ka’), n. [from native name in Sene- gambia,] a genus of hard, mahoganylike trees growing in tropical Africa: its wood is used in cabinetwork. khed/ah (ked’), n. same as keddah. : khe-dive’ (ke-), n, (Turk. khidio, from Per, khi- diw, khadiw, lord, great prince, king.] the title of the Turkish viceroys of Egypt, from 1867 to 1914. khen’na (ken’), n, same as henna. kheth, ». the ei hthletter of the Hebrew alpha- bet, a velar fricative corresponding to the Scottish ch, as in loch. : = z khid’mut-gar (kid’), n. [Hind. khidmatgār, a servant, butler; khidmah, attendance, service, and -gār, suffix denoting agent.] in India, a male waiter; a table servant. Khmer (k'mer), n. [from the Khmer name.] 1. one of a native people of Cambodia: they had a highly developed civilization in the Middle Ages. 2. their language. 5 Bie Khend (kond), . [from the native Dravidian mame,] a member of a group of Dravidian tribes of east central India. khut’bah, 2. [Ar. khulba, khotba, an address. ] a Moslem formal address and prayer deliv- ered at the beginning of the midday service in a mosque every Friday. ki-a-boo’ca wood, [E. Ind. kiabooca, and E.
103533:kib’läh, 7. [Ar. gibla, opposite, the south, from gabala, to be opposite.| the direction toward the Kaaba in the great mosque at Mecca, to- ward which the Moslem turns when he prays.
=== DEV ===
DOZ.txt:2063:Overgenomen uit het erg bedorvene Fr. mosquée;
DOZ.txt:2064:beter Ital. meschita, Sp. mezquita, Port. mesquita.
LAM.txt:274:(V. ce mot. ) arzel (j); j' dans mosquée.
LAM.txt:1042:croisades .ont mahométois, mahomerois, et mahomerie (mosquée). Du
LAM.txt:3276:ban est une des trois pendant lesquelles les Mosquées
LAM.txt:4617:et le Tan^imat [p. 9). « A un des bouts de la mosquée, du
LAM.txt:4619:ie curé de la mosquée. » Paul Lucas (i),
LAM.txt:5314:(1) «Mosquées dites en Ai'abes gamea et les clochers, madene» Voyages
LAM.txt:5411:Mosquée. Esp : mesquita. // .• meschita. Vieux franc.
LAM.txt:6779:qui dormaient dans la mosquée de Médine pendant la nuit.
```


## [2026-09-07T15:57:03.359Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('PHD.txt',encoding='utf-8',errors='replace').read().split('\\n')\nfor ln in (437,474):\n    leaf='\\n'.join(t[:ln]).count('\\f'); print('line',ln,'leaf',leaf,'printed',leaf-21)\nEOF\nsed -n '68895,68905p' MON_part2.txt\necho \"=== MON masjed/sojud ===\"; grep -n \"^سجود\\|سجود:\\|سجاده:\\|ساجد:\" MON_part1.txt MON_part2.txt | head -10",
 "description": "PHD pages and Mo'in mah/sojud"
}
```


### [2026-09-07T15:57:04.823Z] TOOL RESULT

```
line 437 leaf 77 printed 56
line 474 leaf 79 printed 58
گریه و زاری کردن. نوحه کردن؛ شیون 
گر دن: 
مه: 0 [- ماه] (۱.) قمی ماه. مه نو : ماه نو » 
هلال. 
مه: 72علامت نهی. نشانهة دعای سمنفی که 
قدما بکار می‌بر دند. 

مه ۵ ( ص.) بزرگتر؛ مق. که؛ ج. مهان. 
مه: ۱۵ [ابر» قس. . میغ» مغ ] (. ) سخار آب 
تبره رنگگ که فضای نزدیک به زمین را فرا 
گیرد؛ میغ» ماغ» نزم. ضح.- (زم.) بخار آب 
=== MON masjed/sojud ===
MON_part2.txt:23419:سجود رفته و از جای برخاسته و هر دو نفر با
```


## [2026-09-07T15:57:37.191Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== TLM ma ===\"; grep -n \"^mā\\|mātya\\|^ma \" TLM.txt | head -10\necho \"=== SYN not ===\"; grep -n \"μή\\|prohibitive\\|12\\.4[0-9]* Not\" SYN.txt | head -10\necho \"=== IEC me ===\"; grep -n \"^mē\\|^me-\\|mē 'not'\\|not, prohib\" IEC.txt | head -10\necho \"=== AFA context 792 ===\"; sed -n '785,800p' AFA.txt\necho \"=== AFA sagada/Gebet ===\"; grep -n -i \"sagada\\|Gebetsst\\|Kultst\" AFA.txt | head",
 "description": "Grep Tolman, Buck, Mann, Fraenkel"
}
```


### [2026-09-07T15:57:37.280Z] TOOL RESULT

```
=== TLM ma ===
1691:ma  +   +   +   (Elam,  marus;  Bab.  ma-ru-’),  to  be  read  maru,  m.  name of  a   Median  town.  Nom.  sg.  m[aru]§,  Bh.  2.  6;  cf.  KT,  25.
=== SYN not ===
=== IEC me ===
10411:mē (2) (me, men, mene, mone, mnë), acc. prn. *me' (dat. also in some languages) Skt. enclitic må, id.; Romani man, acc. & dat. id.; Av.màm, mā, id.; Ober, -mā, acc. id.; Oss. må, män, acc. & dat., id.; Gk. emé, mé, acc. id.; Doric cf. emín, emine, dat. id. (vocalism obscure); Alb. mue, mua, acc. & dat., id.; weak form: mé, id. (as Fr. moi: me); Lat. mē, acc. id.; Ligurian in Rumansch (?) enclitic:
10456:mēghos (1) ‘pleasant; pleasure’. Cf. WP II, 256 Skt. cf. mahinah "etad Ir. míog, m. ‘smile’ (cf. smég- for the Ir. doublet smíog, id.); OE cf. mægp (2) ‘desire’; Li. mëgüs ‘desirous’;
10610:mēnā ‘(epithet of) moon’. Cf. méns, etc. Lat. Ména ‘goddess of menstruation’; Gk. méné, f. ‘moon’; MHG mane, sf ‘moor be- side man, mone, id. (MHG mane is also a wf., but Go. mēna ‘moon’ is a wm., gs *ménins)
=== AFA context 792 ===
feln lässt , ist die verschiedene Vocalisationsmöglichkeit ,die sich bei diesem Worte zeigt. Echt arabische Worter
uraltester Herkunft pflegeu derartigen Wandel nicht zn
zeigen. Auch ist Sjui in alten Gedichten kaum anzutreffen.
Es fehlt auch im Äthiopischen. Auch verdient wohl Er-
wiigung, dass Lehm zu Ziegeln in Arabien nicht so häufig
ist, um allgemeines Baumaterial zu sein. Anders war es
bekanntlich in Babylon (Gen. 11, 3; Ovid Metamorph. Lib.
IV. 58). Aber zum Bau der ersten Moschee werden schon
Ziegeln gebraucht Belad. 6, 9.
Ebenfalls von den Aramaeru den Arabern zugeführt ist
1^1 , ;«^l 9 dessen verschiedene Yocalisatiousmoglichkeiten
zugleich mit dem Maugel einer Ableitung, der unarabi-
sehen Form und demPlur. ^«w^l Mu arrab 16, 7 auf fremde
Herkunft hinweisen. Es soll schon im Assyrischen vor-
kommen; vgl. Guidi Delhi sede. p. 16. Die Araber selbst
halten es für ein persisches Lehnwort; vei*gl. schon Gauh.
=== AFA sagada/Gebet ===
```


## [2026-09-07T15:57:44.090Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"NEGATIVE\\b\" SYN.txt | head -10\necho \"---\"; grep -n \"prohibitive\\|'not'\" SYN.txt | head -10",
 "description": "Grep Buck for negative"
}
```


### [2026-09-07T15:57:44.149Z] TOOL RESULT

```
550:negative
7655:often expressed simply as ‘not strong’, with negative compounds of words for
15952:9.90 THING ee mpayua, Xpijna Goth. wazthts Lith.  daiktas Tat, “erHa (Pop. mp@ua) ON — hlutr Lett. lieta It, del Dan. ting, sag ChSl. vest Fr. chos Sw. sak, ting SCr.  stvar Sp. etd OE ping Boh.  vée Rum, luery ME _ thing Pol. —_rzecz Ir, ni, rat NE thing Russ. _veSé’, delo a: ni, rud ae ant nae Skt. vastu- , th inc, sacha Av. Br, ee MHG dine, sache iegtacr, NHG  sache, ding an har eral notion ae beamore vague gen- In several cases, partly due to se- *Y act, event, or ae thing’, covering | mantic borrowing, the development has ed on g ca object. Itis | been through ‘subject of litigation’. And most common] ‘eae notions, Other sources are ‘act, deed, work, e aN act, event, ee te G generalization share, thing needed, property’, ete. The oe ° 8 material ob; ir ls earlier than | use of the neuter of the indefinite pro- Ords listeg are stil] ne A few of the | noun for ‘anything, something’ and, with teria] object ot used for ‘thing’ negative, ‘nothing’ (Grk. 7, ot7., Lat.
15964:3. Ir, ni, NIr. ni, pl. neithe, orig. neut. of pronominal nech ‘someone’ (*ne-k“o-, with change fr. negative to positive, asin Lith. ne-kas ‘something’. Pedersen 1.212. Thurneysen, Gram. 309, 311.
21100:Down, ; negative com- th 4 = pose) to those for ‘dear’, latter, Th them are unrelated to the Sonable’, ai ss peat , ‘fair, rea- Ome : ‘ : Of the Words foy ‘cheap’ preaieed
23873:Ir. namma, NIr. amhain, fr. na ‘not’ and ma, md ‘more’ (18.16). Br. nemet also fr. negative, but formation obscure. Pedersen 1.165, 2.261.
27802:‘Misfortune’ is most commonly ex- pressed by words for ‘fortune’ (16.17) combined with words for ‘ill, mis-, ad- verse’, or a negative prefix, rarely alone with specialization in this direction (Grk. cupdopé).
29449:The opposite of ‘true’ may be ex- pressed by negative compounds, e.g. OE un-sop, NE un-irue, NHG un-wahr, Ir. neb-fir, Lith. ne-teisingas, Skt. a-sat- ya-; by Lat. falsus (pple. of fallere ‘de- ceive’) and its Romance and Gmc. derivs. (also opp. to ‘faithful’); by OE léas, also and more orig. ‘destitute of, void’ (: Goth. laus ‘empty, vain’, fraliu- san ‘lose’, etc., 11.33). Similarly, the opposite of ‘truth’ may be expressed as ‘untruth’ or ‘falsehood’. But in nearly all the IE languages there are distinctive downright terms for a ‘lie’, with corre- sponding verbs.
30980:is not infrequently so expressed, that is, by words for ‘remember’ (or in some cases related words for ‘mind’ or ‘think’) with prefixes of negative force, just as in the now only dial. or illiterate NE dis- remember. . Other sources are ‘lose’ (with special- ization to ‘lose from the mind’), ‘rub out’, or transfer from impersonal ‘escape no- tice, lie hidden, be left behind’ to per- sonal use—in one group ‘make merry with’ (> ‘be careless, neglect, forget’).
31236:Solve’ (problems, riddles, etc.) is Benerally expressed by words which Mean literally ‘loose’ or the like, most of ee either negative compounds of ie for ‘bind’ (9.16) or related to Ords discussed under ‘lose’ (11.33) or
---
```


## [2026-09-07T15:57:53.218Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \"https://en.wiktionary.org/wiki/mosque\" \"https://www.etymonline.com/word/mosque\" \"https://en.wiktionary.org/wiki/%D9%85%D8%B3%D8%AC%D8%AF\" \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/meh%E2%82%81\" \"https://en.wiktionary.org/wiki/%D5%B4%D5%A6%D5%AF%D5%AB%D5%A9\"; do\n timeout 120 python3 tools/fetch_source.py \"$u\" --note \"page 322: roots Masgda (mosque/masjid/mazget) and Me 1 (prohibitive particle) verification\" 2>&1 | tail -2\ndone",
 "description": "Archive web sources"
}
```


## [2026-09-07T15:57:54.890Z] TOOL CALL #53: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B3%D8%AC%D9%88%D8%AF",
 "prompt": "Quote the Arabic entry سجود (sujūd): etymology (verbal noun of سجد sajada), meaning, and any Persian section. Also mention if there is a Persian borrowing note."
}
```


### [2026-09-07T15:57:56.691Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/5de3af3612b6d1d7.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/36cc337738682a35.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/2db092d794b757d9.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/aab4d87078a03231.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0d2b126a3fde2522.txt
```


### [2026-09-07T15:58:01.695Z] TOOL RESULT

```
# Arabic Entry: سجود (sujūd)

**Etymology:** The entry identifies سجود as a "verbal noun of سَجَدَ (sajada) (form I)" – derived from the root verb in its first grammatical form.

**Meaning:** The term functions as a masculine noun with grammatical declension patterns specific to Arabic triptote nouns. It also serves as the masculine plural form of the adjective ساجد (sājid).

**Persian Section:** The Wiktionary page lists Persian (فارسی) among six languages with entries for this term, though the actual Persian section content is not displayed in the provided material. No borrowing notes appear in the excerpt.
```


## [2026-09-07T15:58:32.035Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON masjed ===\"; grep -n \"^مسجد\\|مسجد:\" MON_part2.txt | head -5\necho \"=== MON sajdeh ===\"; grep -n \"سجده:\\|سجاده:\\|ساجد\" MON_part2.txt MON_part1.txt | head -8\necho \"=== ARY index ===\"; grep -n -i \"^MA\\b\\|MAZ\" incoming/ARY/ARY_latin_index_pages.txt | head -5",
 "description": "Grep Mo'in for masjed and sajdeh"
}
```


### [2026-09-07T15:58:32.120Z] TOOL RESULT

```
=== MON masjed ===
18609:مسجد جامع شهر قروین بکار گذاشته شده و 
48291:مسجدوب: ۱ ۳4 (اسف.) جدت 
49393:مسجد که امام نماز در آنجا گزارد؛ ج. 
55039:مسجد. مزکت آدینه: مسجد جمعد: مسجد 
=== MON sajdeh ===
MON_part2.txt:20885:(کاخ‌ها» مساجده اماکن متب رکه و نغیره) یا بر 
MON_part2.txt:87024:طلاب و مدارس و مساجد) مق. وقت 
MON_part1.txt:73449:ج. . ساجدون» ساجد ین. 
MON_part1.txt:75772:سجده: (3)6 له [ع. سبجدة] (مص‌ل.) 
MON_part1.txt:80608:از سنگک سازند و در حیاط مساجد و تکایا 
MON_part1.txt:89063:مدارس و مساجد و بقاع متبرکه و وزرای 
=== ARY index ===
1918:MATTOCK ENGLISH) gud MAZA LASPANISH) glibysl
1919:OLD CHURCH SLAVIC) 348 53%! MAZZA AITALIAN) gils\
2780:AURAMAZDAH.
2781:REFERENCES beth OHRMAZD, (PAHLAVI) «5 Jay
2782:POKORNY. sS~S~«SB ‘OHARMAZD
```


## [2026-09-07T15:58:38.065Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '75770,75776p' MON_part1.txt; echo ---; sed -n '73444,73452p' MON_part1.txt; echo \"=== PHD 437 ===\"; sed -n '437p' PHD.txt; echo \"=== AVG lines ===\"; sed -n '4244,4248p;4802,4806p' AVG.txt",
 "description": "Read Mo'in sajdeh/sajed and PHD/AVG quotes"
}
```


### [2026-09-07T15:58:38.145Z] TOOL RESULT

```
سحد: 224 [- شجد] (.) سرمای سخت. 
سجده: (3)6 له [ع. سبجدة] (مص‌ل.) 
نهادن نمازگزار هفت عضو خود (پیشانی 
دو کف دست» دو سر زانوء دو شست با). را 
بر زمین با شرایط مخصوص و خواندن 
ذکرهای لازم. عمل مذکور را انجام دادن به 
---
است؛. 
ساج: 2 [غ.] (ا.) چادر سبز باسیاه. 
بالا پوش فراخ» طیلسان؛ ج. سیجان. 
ساحجد: 5164 [ع. .] (افا.) سجده کننده» 
آنکه بیشانی بر زمین گذارد و سجده کند؛ 
ج. . ساجدون» ساجد ین. 
ساجور: له ل.) (. تک چوب که با 
ریسمان به گردن سک بدند» قلاده سک 
ج. سواجیر. 
=== PHD 437 ===
ma [AL < À °l | M m, N ~] not (prohibitive). ~ agar [N magar] perhaps; lest. mad [AM < A ?m-y, v. madar | M md] mother.
=== AVG lines ===
b.  Time.    Av.  nu  'now'  =  Skt.  nu,  n&;  Av.  mogu  'soon,  quickly* (§  38)  =  Skt.  makfti;  Av.  pascaetS  'after'.
c.  Manner.     Av.  agva  'so*  =  Skt.  evd;   GAv.  nana    'differently, specially'  (§  17)  =  Skt.  ndnS;  Av.  ca  'how*.
d.  Negative.     Av.  m&  'not*  (prohibitive)  =  Skt.  md.
e.  Asseverative.     Av.    ba    'indeed,    truly',   bada    'even,    indeed, always'.
4.  Adverbial  Prefixes. (Cf.  Whitney,  Skt.  Gram.  §  nr8  seq.)
§  866.  Original  a  of  feminine  stems  may  remain  unchanged ,  but sometimes,  like  a,  it  becomes  -o.  Examples  are:
Av.  dalna.vazah-  nomen  propr.,  daino.disa-  m.  'teacher  of  the law'  (dalna-) ,  urvaro.6aejaza-  adj.  'having  the  balm  of  plants' (urvara-).
Note.  Original  mS  (prohibitive)  appears  as  ma-  in  composition  in YAv.  makasvil  mastrt  'no  dwarf,  no  woman'  et  al.  Yt.  5.92;  GAv.  ma- vaefa-  'not  failing'  Ys.  41.1.
§  867.  Final  i,  ;,  u,  (u)  of  a  stem  remain  as  a  rule  unchanged  in the  prior  member  of  a  compound,  though  T  usually  appears  for  f. Examples  are:
Av.  zairi.gaona-  'yellow-colored'  (za*'ri-},  muilti.masah-  'large  as the  fist'  (muiti-),  nS'ri.cinah-  'seeking  a  wife'  (tiS'rt-). — Av.  Ssu.- kairya-  'quickly  working',  voTu.gaoyaoiti-  'having  wide  pastures'. Note  I.     The  «-stems   occasionally   show   -«/,    like   the  nominative singular :  e.  g.  Av.  b&zuf.aojah-  'strong-armed'  (observe  -/),  nasuj.ava.dfr»ta- 'corpse-defiled'.    Somewhat  different  is  the  -/  in  Av.  Snui.hac-  'accompany- ing' (Skt.  Snufdc-),  Av.  pasuH.ha*rva-  'cattle-protecting',  see  above  §  754,  2. Observe  also  YAv.  nasuspaeya-  'corpse-burning'  (with  j  before  /,  §  754). Note  2.    Av.  g&u-,  gao-  'cow'  appears  in  composition  as  gao-,  gava~, gavo-  (cf.  Whitney,  Skt.  Gram.  §  361  f):  e.g.  Av.  gaoyao*ti-  'cow-pasture' =  Skt.  gdvy&ti- ;  Av.  gavaJiti-  'abode  of  cows',  Av.  gavo. s tana-  'cow-stall' =  SkL  gosthana-.
```


## [2026-09-07T15:59:39.702Z] TOOL CALL #56: Bash

```json
{
 "command": "timeout 120 python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/%D8%B3%D8%AC%D9%88%D8%AF\" --note \"page 322, Masgda entry, node 2: Arabic sujud verbal noun of sajada, Persian loan\" 2>&1 | tail -2",
 "description": "Archive sujud source"
}
```


### [2026-09-07T15:59:41.370Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/5c0177828eeab751.txt
```


## [2026-09-07T15:59:45.124Z] TOOL CALL #57: Bash

```json
{
 "command": "sed -n 1,80p /home/sfmqrb/git/rishe/tools/verify_check.py",
 "description": "Read verify_check.py"
}
```


### [2026-09-07T15:59:45.184Z] TOOL RESULT

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


## [2026-09-07T15:59:48.198Z] TOOL CALL #58: Bash

```json
{
 "command": "sed -n 80,140p /home/sfmqrb/git/rishe/tools/verify_check.py",
 "description": "Rest of verify_check"
}
```


### [2026-09-07T15:59:48.243Z] TOOL RESULT

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


## [2026-09-07T16:09:21.616Z] TOOL CALL #59: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/mk322.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW = \"https://en.wiktionary.org/wiki/\"\nS_MOSQUE = W + \"mosque\"\nS_ETY = \"https://www.etymonline.com/word/mosque\"\nS_MASJID = W + \"%D9%85%D8%B3%D8%AC%D8%AF\"\nS_MEH1 = W + \"Reconstruction:Proto-Indo-European/meh%E2%82%81\"\nS_MZKIT = W + \"%D5%B4%D5%A6%D5%AF%D5%AB%D5%A9\"\nS_SUJUD = W + \"%D8%B3%D8%AC%D9%88%D8%AF\"\n\nKLN_MOSQUE = (\"KLN_1966.txt leaf 540 (= printed pp. 1007-1008; the same leaf carries the 'mother' entry \"\n              \"verified as p.1007-8 on page 316), s.v. mosque: \\\"mosque, n., a Mohammedan place of worship. \"\n              \"— F. mosquee, fr. It. moschea, fr. earlier moscheta, fr. Sp. mesquita (whence ModSp. mezquita), \"\n              \"fr. Arab. masjid, 'place of worship, mosque', which is either borrowed fr. Nabatean masgedha, \"\n              \"'place of worship', or formed independently, with ma-, a pref. denoting place, fr. sajada, 'he was \"\n              \"submissive, prostrated himself in prayer', which is rel. to, or — more prob. — borrowed from \"\n              \"Aram. sᵉghedh, of s.m.\\\"\")\nFVQ_MASJID = (\"FVQ_pages.txt leaf 280 = printed p. 263 (the running head 'FOREIGN VOCABULARY OF THE QUR'AN 263' \"\n              \"stands immediately before it), s.v. masjid: \\\"A place of worship … The form seems not to have been \"\n              \"a formation from this in Arabic, but to have been an independent borrowing from the North. Nöldeke, \"\n              \"ERE, i, 666, 667, has drawn attention to … the Aramaic origin of the word. In the Nabataean \"\n              \"inscriptions we find msgdʾ not infrequently meaning 'place of worship' … The Syr. masgdā, \"\n              \"however, seems to be a late borrowing from the Arabic, but we find msgdʾ in the Elephantine papyri.\\\"\")\nLKT_1435 = (\"LKT.txt line 3303, entry no. 1435: \\\"Ar. masgid: 'Gebetshaus', eigentlich 'Ort, wo man sich niederwirft' \"\n            \"[Präfix ma- des Ortes u. Vb. sagada 'sich niederwerfen, προσκυνείν']; hieraus sp. mezquita, pg. mesquita, \"\n            \"it. meschita, moschea, afrz. mosquete, frz. mosquee, rum. moşea; ndl. moskee, engl. mosk, mosque, dtsch. Moschee\\\"\")\nBQT_2001 = (\"Borhan-e Qate' printed p. 2001 (BQT_v4_picofile.pdf p. 84; page image and my transcript saved as \"\n            \"data/verification/sources/refs/ocr/BQT/2001.png / 2001.vision.txt), headword «مزکت» with Mo'in's \"\n            \"footnote 8: «این لغت آرامی است ، قی : عربی مسجد ، اسپانیولی mezquita «ژابا ص ۳۹۷» \"\n            \"ـ مزکت آدینه = مسجد جامع … وآن بنیاد مسجد عربی است» — 'this word is Aramaic; cf. Arabic masjid, \"\n            \"Spanish mezquita; … and it is the foundation of the Arabic masjid'. The entry itself continues on p. 2002: \"\n            \"«مسجد را گویند که بفارسی خانهٔ خدا و بعربی بیت‌الله خوانند».\")\nMON_MAZKAT = (\"MON_part2.txt line 55038 (= incoming/MON/MON_2vol_Adena_v2_djvu.txt, the 2-vol abridgement): \"\n              \"«مزکت: [آرا. ، ع. مسجد] (ا.) مسجد. مزکت آدینه: مسجد جمعه؛ مسجد جامع (التفهیم)» — Mo'in's \"\n              \"origin tag [آرا.] = Aramaic, with Arabic masjid only as a comparandum. Print pagination of the 6-vol \"\n              \"edition (Nourai's MON:4063) cannot be mapped on the abridgement.\")\nPHD_MAZGIT = (\"PHD.txt line 474 (leaf 79 = printed p. 58): \\\"mazgīt [mzgt' | N ~] mosque.\\\" — MacKenzie registers the \"\n              \"Book-Pahlavi form mzgt' = mazgīt and marks the New Persian form as identical; he gives no source language.\")\nPOK_ME1 = (\"POK_full.txt lines 60731-60739: \\\"Root / lemma: me-1  Meaning: prohibitive particle  Grammatical \"\n           \"information: prohibitiv  Material: Old Indic Avestan Old pers. mā, gr. μή, Armenian mi ds., alb. mos ds. \"\n           \"(from *mo = Indo Germanic *me+s …)  References: WP. II 236 f.  Page(s): 703\\\"\")\nKNT_MA = (\"KNT.txt line 5754, on the leaf whose printed page numbers are 201/202: \\\"mā conj. 'not', in prohibitions \"\n          \"etc.: Av. Skt. mā, Gk. μή, pIE *mē (§109, §191.1, §292b). With subj.: DNb 55 (mā-taiy), 58. With opt.: DB 4.59, \"\n          \"69, 79 … With inj.: DB 4.54 …\\\"; and line 5760 (printed p. 202): \\\"mātya conj. 'lest, that not, not': mā 'not' \"\n          \"+ conj. tya (§133, §292b). mātya-mām (§133) DB 1.52. mātya DB 4.43, 48, 71.\\\"\")\n\ndata = {\n  \"pdf_page\": 322,\n  \"book_page\": 292,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-07\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Masgdâ\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"Aramaic מסגדא msgdʾ, emphatic state masgdā 'place of worship, cult-place, prayer-stele', a noun of place from the root s-g-d 'to bow down, prostrate oneself'\",\n      \"note\": \"The root box is right in substance: an Aramaic noun of place msgdʾ 'place of worship' really exists and really is the source of (or at least the model for) Arabic masjid. It is attested in Imperial Aramaic already in the 5th c. BCE (Elephantine papyri, Cowley, Aramaic Papyri p. 148) and repeatedly in Nabataean, e.g. the Bosra inscription 'This is the place of worship (msgdʾ) which Taimu son of Walid el-Ba'al built' (de Vogué p. 106 = ZDMG xxii 268), both quoted by Jeffery, FVQ p. 263. Two small corrections: the citation form should be the emphatic msgdʾ / masgdā (Nourai's 'Masgdâ' is that emphatic state, written as if it were absolute), and Aramaic Syriac masgdā itself is thought by Jeffery to be a LATE borrowing back from Arabic, so the pre-Islamic evidence is the Nabataean/Imperial Aramaic form, not the Syriac one. Klein (p. 1007) prints the Nabataean form as masgedha, and Wiktionary's Arabic entry says the Arabic word was 'likely borrowed from a regional Aramaic term for a place of worship, attested in Nabataean Aramaic msgdʾ and in Imperial Aramaic msgdʾ already in the 5th century BCE, the emphatic state of which seems to underlie some of the Romance descendants' — the last remark also explains the -a of Spanish mesquita on this chart.\",\n      \"note_fa\": \"ریشهٔ نمودار، واژهٔ آرامی msgdʾ (حالت معرفهٔ masgdā) به معنی «جای نیایش، سجده‌گاه» از ریشهٔ سامی s-g-d «خم شدن، سجده کردن»، واقعی و مستند است: این واژه از سدهٔ پنجم پیش از میلاد در اسناد آرامی الفنتین و سپس در سنگ‌نوشته‌های نبطی (از جمله کتیبهٔ بُصرا) دیده می‌شود که جفری در «واژه‌های دخیل قرآن» ص ۲۶۳ نقل کرده است. دو اصلاح جزئی: نخست اینکه صورت مناسب برای نقل همان معرفهٔ msgdʾ/masgdā است؛ دوم اینکه صورت سریانی masgdā به گمان جفری خود وام‌گرفته از عربی است، پس گواه پیش‌ازاسلامی را باید از آرامی نبطی و شاهنشاهی گرفت. در مجموع ادعای نورایی در مورد ریشه درست است؛ کلاین (ص ۱۰۰۷) و ویکی‌واژه نیز همین را می‌گویند، و ویکی‌واژه می‌افزاید که همین صورت معرفه پشتوانهٔ پایانهٔ -a در mesquita اسپانیایی است.\",\n      \"sources\": [S_MASJID, S_MOSQUE],\n      \"ref_check\": [\n        {\"ref\": \"KLN:1007\", \"status\": \"supports\", \"note\": KLN_MOSQUE + \" — Klein's page is exactly Nourai's KLN:1007 and states the Aramaic/Nabataean origin of the root box.\"},\n        {\"ref\": \"VDQ:379\", \"status\": \"not_checked\", \"note\": \"VDQ = Badre'i's Persian translation of Jeffery's FVQ; only on noorlib.ir, whose viewer is JavaScript-rendered and unreadable by WebFetch (refs_online.json says so). The substance was checked in the English original instead: FVQ p. 263 (quoted under consulted), which is the same entry.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"FVQ\", \"where\": \"printed p. 263 s.v. masjid (FVQ_pages.txt leaf 280)\", \"stance\": \"supports\", \"note\": FVQ_MASJID},\n        {\"src\": \"KLN\", \"where\": \"1966 ed. leaf 540 = pp. 1007-1008 s.v. mosque\", \"stance\": \"supports\", \"note\": \"Klein: 'either borrowed fr. Nabatean masgedha, \\\"place of worship\\\"' — Nourai's root box.\"},\n        {\"src\": \"AFA\", \"where\": \"AFA.txt (Fraenkel, Die aramäischen Fremdwörter im Arabischen)\", \"stance\": \"silent\", \"note\": \"grep -i 'masgid|masjid|Moschee' finds only incidental mentions of mosques (lines 792, 846, on bricks and on Doughty's Mecca road); Fraenkel's Arabic/Aramaic headwords are in unOCR'd script, so his treatment of masjid could not be read from this text file.\"},\n        {\"src\": \"LKT\", \"where\": \"entry no. 1435 (LKT.txt line 3303)\", \"stance\": \"supports\", \"note\": LKT_1435 + \" — Lokotsch analyses the Arabic word as ma- of place + sagada, i.e. Klein's second alternative, and does not mention Aramaic; on the Semitic side he is therefore only partial, but on the western chain he is exactly Nourai's.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Arabic\",\n          \"words\": \"masjed; s.j.d\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Arabic masjid 'place of prostration, mosque' is formally the regular noun of place (ism al-makān) of the root s-j-d, i.e. prefix ma- + sajada 'he prostrated himself' — that much is uncontroversial (Klein p. 1007; Lokotsch no. 1435; Skeat s.v. Mosque). What Nourai's arrow adds, and what the modern consensus also holds, is that the word was not coined inside Arabic but taken over ready-made from Aramaic: Jeffery (FVQ 263) says 'the form seems not to have been a formation from this in Arabic, but to have been an independent borrowing from the North', citing Nabataean msgdʾ 'place of worship' and Imperial Aramaic msgdʾ in the Elephantine papyri, and adds that the technical religious sense of the verb sajada is itself an Aramaism (his p. 163). Wiktionary's Arabic entry says the same ('likely borrowed from a regional Aramaic term … attested in Nabataean Aramaic msgdʾ and in Imperial Aramaic msgdʾ already in the 5th century BCE'). Semantically the Aramaic word covered any cult place (also a votive stele); in the Qur'an masjid (28 occurrences) is still 'any place of worship' — the fane at Quba' (ix, 109), the Temple at Jerusalem (xvii, 1), the church of the Seven Sleepers (xviii, 20) — and only later narrowed to the Islamic mosque. On the chart's NOTE (FVF:638, Emam Shushtari, claiming Arabic masjed comes from Persian mazget): modern scholarship rejects it. The Aramaic msgdʾ is 5th-c.-BCE, masjid stands in pre-Islamic Arabic poetry and in the Qur'an, while Persian mazgit is first attested in Islamic-period Pahlavi and early New Persian, i.e. after the conquest; the direction Persian → Arabic is chronologically impossible, and Mo'in's own footnote in Borhan-e Qate' (p. 2001) calls mazkat Aramaic, not the source of the Arabic word.\",\n          \"derivation_fa\": \"«مسجد» در عربی از نظر ساخت، اسم مکان از ریشهٔ س‌ج‌د (سَجَدَ «پیشانی بر خاک نهاد») با پیشوند مکانی مَ- است؛ اما پژوهش امروزی — مانند نورایی — بر این است که خود واژه در عربی ساخته نشده، بلکه از آرامی شمال (نبطی و آرامی شاهنشاهی) وام گرفته شده است؛ جفری (ص ۲۶۳) حتی معنای اصطلاحی فعل سجد را هم از تأثیر آرامی می‌داند. در قرآن مسجد (۲۸ بار) هنوز به معنی هر پرستشگاهی است (مسجد قُبا، بیت‌المقدس، کلیسای اصحاب کهف) و بعدها ویژهٔ مسجد مسلمانان شده است. دربارهٔ یادداشت نمودار (ادعای امام شوشتری، فرهنگ واژه‌های فارسی در زبان عربی ص ۶۳۸ که مسجد را از «مزگت» فارسی می‌گیرد) باید گفت پژوهش امروزی این را رد می‌کند: صورت آرامی از سدهٔ پنجم پیش از میلاد گواهی شده و مسجد در شعر جاهلی و قرآن به‌کار رفته است، در حالی که «مزگت» فارسی تنها از دورهٔ اسلامی در دست است؛ معین نیز در حاشیهٔ برهان قاطع (ص ۲۰۰۱) مزکت را آرامی خوانده است، نه سرچشمهٔ واژهٔ عربی.\",\n          \"sources\": [S_MASJID, S_MOSQUE],\n          \"ref_check\": [\n            {\"ref\": \"KLN:1007\", \"status\": \"supports\", \"note\": KLN_MOSQUE + \" — Klein gives both the Nabataean loan and the ma- + sajada analysis, i.e. this node's two words.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"FVQ\", \"where\": \"p. 263 s.v. masjid; p. 163 on the verb sajada\", \"stance\": \"supports\", \"note\": FVQ_MASJID},\n            {\"src\": \"LKT\", \"where\": \"no. 1435\", \"stance\": \"partial\", \"note\": LKT_1435 + \" — supports the ma- + sagada analysis but says nothing about an Aramaic source.\"},\n            {\"src\": \"SKT\", \"where\": \"SKT.txt line 11917 s.v. Mosque\", \"stance\": \"partial\", \"note\": \"\\\"Arab. masjad, masjid, a temple, mosque. — Arab. root sajada, to adore, prostrate oneself\\\" — Skeat derives the Arabic noun from the Arabic verb, with no Aramaic step.\"},\n            {\"src\": \"AFA\", \"where\": \"AFA.txt\", \"stance\": \"silent\", \"note\": \"Fraenkel's Aramaic-loanword entries are in unOCR'd Semitic script; grep for 'Moschee' yields only incidental sentences (lines 792, 846).\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"sojūd; sâjed; masjed\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"All three are Arabic loans in New Persian, borrowed after the conquest with the vocabulary of Islamic ritual, and the arrow from the Arabic node is therefore right (they are borrowings, not Iranian inheritances). سجود sojūd is the Arabic maṣdar of form I sajada ('verbal noun of سَجَدَ (form I)', Wiktionary), سجده sajdeh the Arabic noun of instance sajdah (Mo'in tags it '[ع. سجدة]'); ساجد sājed is the active participle sājid 'one who prostrates himself' (Mo'in: '[ع.] (افا.) سجده کننده … ج. ساجدون، ساجدین'), beside the intensive sajjād 'assiduous in prostration' and its feminine-shaped sajjāda 'prayer rug' (the thing one prostrates on) — exactly the trio Nourai prints in his parentheses. مسجد masjed is the Arabic noun of place taken over unchanged (Persian pronunciation masjed with the Persian reflex of Arabic i). Note the doublet relation with node 7: literary Persian ended up with the Arabic masjed while the older Aramaic-based mazgit/mazkat died out, so Persian masjed is the younger of two words for the same thing.\",\n          \"derivation_fa\": \"هر سه واژه معرّب‌هایی نیستند بلکه وام‌واژهٔ عربی در فارسی نو اند که پس از اسلام همراه اصطلاحات عبادی وارد شده‌اند؛ پس پیکان نمودار از گرهٔ عربی درست است. «سجود» مصدر باب اول از سَجَدَ است، «سجده» اسم مرّه (معین: [ع. سجدة])، «ساجد» اسم فاعل (معین: «سجده کننده … ج. ساجدون، ساجدین») در برابر صیغهٔ مبالغهٔ «سجّاد» و «سجّاده» (جانماز)، و «مسجد» همان اسم مکان عربی است. نکتهٔ خواندنی آنکه «مسجد» و «مزگت» (گرهٔ ۷) دوگانه‌اند: فارسی نخست صورت آرامی را داشت و سپس صورت عربی جای آن را گرفت. ادعای نورایی درست است.\",\n          \"sources\": [S_SUJUD, S_MASJID],\n          \"ref_check\": [\n            {\"ref\": \"FVA:185\", \"status\": \"not_checked\", \"note\": \"FVA = Nahvi, Farhang-e Vāžehā-ye Arabi dar Fārsi (1368/1989). refs_online.json records that no digital copy exists on any permitted platform (catalogue record only, OpenLibrary OL2012991M), so p. 185 could not be read.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"MON_part1.txt lines 73449, 75772 (s.v. ساجد, سجده)\", \"stance\": \"supports\", \"note\": \"«ساجد: [ع.] (افا.) سجده کننده، آنکه پیشانی بر زمین گذارد و سجده کند؛ ج. ساجدون، ساجدین» and «سجده: [ع. سجدة] (مصل.) نهادن نمازگزار هفت عضو خود … بر زمین» — Mo'in marks both as Arabic loans, as the chart's arrow requires.\"},\n            {\"src\": \"KLN\", \"where\": \"1966 ed. leaf 507 (≈ p. 990) s.v. masjid, and leaf 540 = p. 1007 s.v. mosque\", \"stance\": \"supports\", \"note\": \"\\\"masjid, n., a mosque. — Arab. See mosque\\\"; and s.v. mosque 'fr. sajada, \\\"he was submissive, prostrated himself in prayer\\\"' — the same Arabic stem that yields Persian sojūd/sājed.\"},\n            {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' (BQT_v4 p. 2001-2002, s.v. مزکت)\", \"stance\": \"partial\", \"note\": \"Borhan, being a dictionary of Persian (not Arabic) words, has no entry for سجود/ساجد/مسجد; it glosses مزکت by مسجد — 'مسجد را گویند که بفارسی خانهٔ خدا و بعربی بیت‌الله خوانند' — i.e. it treats مسجد as the ordinary (Arabic) Persian word.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Spanish\",\n          \"words\": \"mesquita\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Old Spanish mesquita (modern mezquita), first in 13th-c. Castilian texts, is the Andalusi-Arabic masjid taken into Ibero-Romance during the centuries of al-Andalus; the -a of mesquita is usually explained either as the Romance feminine adaptation of a foreign noun in -id or, as Wiktionary suggests, as a reflex of the Aramaic emphatic state msgdʾ that also underlies the Arabic word. The medial cluster -sj- was rendered -sq-/-zq- (Andalusi Arabic ǧ heard as a palatal stop). Klein makes Spanish the direct source of the Italian word, so the chart's Arabic → Spanish step is his; Lokotsch no. 1435 lists 'sp. mezquita, pg. mesquita' straight from Ar. masgid, and Skeat's appendix files mosque among the words that came 'French from Spanish from Arabic'.\",\n          \"derivation_fa\": \"صورت اسپانیایی کهن mesquita (امروز mezquita) از عربی اندلسی masjid وام گرفته شده است و نخست در متون قرن سیزدهم میلادی دیده می‌شود؛ خوشهٔ -sj- عربی در رومانس به -sq-/-zq- بدل شده و پایانهٔ -a یا نشانهٔ مونّث‌سازی وام‌واژه است یا — به گفتهٔ ویکی‌واژه — بازماندهٔ حالت معرفهٔ آرامی msgdʾ. کلاین (ص ۱۰۰۷) و لوکوچ (شمارهٔ ۱۴۳۵) همین مسیر را می‌دهند؛ ادعای نورایی درست است.\",\n          \"sources\": [S_ETY, S_MASJID],\n          \"ref_check\": [\n            {\"ref\": \"KLN:1007\", \"status\": \"supports\", \"note\": KLN_MOSQUE + \" — 'fr. Sp. mesquita (whence ModSp. mezquita), fr. Arab. masjid': the Arabic → Spanish arrow verbatim, in Nourai's spelling.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"LKT\", \"where\": \"no. 1435\", \"stance\": \"supports\", \"note\": \"'hieraus sp. mezquita, pg. mesquita' directly from Ar. masgid.\"},\n            {\"src\": \"SKT\", \"where\": \"SKT.txt lines 11917, 23699\", \"stance\": \"supports\", \"note\": \"'F. mosquee, Cot. — Span. mesquita, a mosque. — Arab. masjad, masjid' and, in the list of borrowings, 'French from Spanish from Arabic … mosque'.\"},\n            {\"src\": \"DOZ\", \"where\": \"DOZ.txt lines 2063-2064 s.v. moskee\", \"stance\": \"supports\", \"note\": \"'Overgenomen uit het erg bedorvene Fr. mosquée; beter Ital. meschita, Sp. mezquita, Port. mesquita' — Dozy too puts the Spanish/Italian forms closest to the Arabic.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Italian\",\n          \"words\": \"moschea\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Italian moschea 'mosque' goes back, per Klein, to an earlier Italian moscheta, itself from Spanish mesquita; the shift -quita > -cheta > -chea belongs to 15th-16th-c. Italian adaptation (with the Tuscan outcome -ea), and the older form meschita, closer to the Spanish, survives beside it (Lokotsch lists 'it. meschita, moschea'; Dozy recommends 'beter Ital. meschita'). The word travelled with Venetian and Genoese trade and with the Levant travel literature of the Cinquecento, and Italian in turn passed it to French, so the chart's Spanish → Italian → French chain is the standard one (Klein, Lokotsch, Etymonline). Nourai gives this node no reference; Klein's mosque article (KLN:1007), cited on the neighbouring nodes, covers it.\",\n          \"derivation_fa\": \"واژهٔ ایتالیایی moschea به گفتهٔ کلاین از صورت کهن‌تر moscheta و آن از اسپانیایی mesquita است؛ صورت meschita که به اسپانیایی نزدیک‌تر است نیز در ایتالیایی به‌کار می‌رفته (لوکوچ و دوزی). این واژه از راه بازرگانی ونیز و جنوا و سفرنامه‌های سدهٔ دهم و یازدهم قمری به فرانسه راه یافته است؛ پس زنجیرهٔ اسپانیایی ← ایتالیایی ← فرانسه در نمودار همان زنجیرهٔ پذیرفتهٔ مرجع‌هاست.\",\n          \"sources\": [S_ETY, S_MOSQUE],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives this node no reference of its own; the claim is covered by the KLN:1007 article he cites on the parent and child nodes ('F. mosquee, fr. It. moschea, fr. earlier moscheta, fr. Sp. mesquita').\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"1966 ed. p. 1007 s.v. mosque\", \"stance\": \"supports\", \"note\": \"'It. moschea, fr. earlier moscheta, fr. Sp. mesquita' — exactly this node and its parent.\"},\n            {\"src\": \"LKT\", \"where\": \"no. 1435\", \"stance\": \"supports\", \"note\": \"'it. meschita, moschea' listed among the descendants of Ar. masgid, and 'frz. mosquee' after them.\"},\n            {\"src\": \"DOZ\", \"where\": \"DOZ.txt line 2064\", \"stance\": \"supports\", \"note\": \"'beter Ital. meschita, Sp. mezquita' — the Italian form is treated as the intermediary behind Dutch/French moskee/mosquée.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"French\",\n          \"words\": \"mosquee\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"French mosquée (Nourai prints it without the accent) appears in the 16th c., replacing the older French forms mosquete/mosquete and the crusade-era calque mahomerie 'mosque' (Lammens p. 5411 area records 'Mosquée. Esp: mesquita. It.: meschita. Vieux franç…'); it is the Italian moschea Frenchified with the learned feminine ending -ée, and it is the immediate source of English mosque and of Dutch moskee and German Moschee (Lokotsch no. 1435). Klein's article gives the same single step, 'F. mosquee, fr. It. moschea'.\",\n          \"derivation_fa\": \"فرانسه mosquée (نورایی بی‌نشانهٔ زیر و زبر نوشته) در سدهٔ شانزدهم میلادی پدید می‌آید و جای صورت‌های کهن‌تر mosquete و واژهٔ دوران جنگ‌های صلیبی mahomerie را می‌گیرد؛ این صورت، همان moschea ایتالیایی است که با پایانهٔ مونّث -ée فرانسوی شده است و خود سرچشمهٔ مستقیم mosque انگلیسی و moskee هلندی و Moschee آلمانی است (کلاین، لوکوچ شمارهٔ ۱۴۳۵، لامنس). ادعای نورایی درست است.\",\n          \"sources\": [S_ETY, S_MOSQUE],\n          \"ref_check\": [\n            {\"ref\": \"KLN:1007\", \"status\": \"supports\", \"note\": KLN_MOSQUE + \" — 'F. mosquee, fr. It. moschea', with Klein's own accent-free spelling 'mosquee', the very form Nourai copies.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"LKT\", \"where\": \"no. 1435\", \"stance\": \"supports\", \"note\": \"'afrz. mosquete, frz. mosquee, rum. moşea; ndl. moskee, engl. mosk, mosque, dtsch. Moschee'.\"},\n            {\"src\": \"LAM\", \"where\": \"LAM.txt line 5411 (and line 1042 for the crusade word mahomerie)\", \"stance\": \"supports\", \"note\": \"'Mosquée. Esp : mesquita. It : meschita. Vieux franc…' — Lammens' note on the French Arabisms puts Spanish and Italian behind the French form; line 1042 records that the crusaders used mahomerie for 'mosquée'.\"},\n            {\"src\": \"DEV\", \"where\": \"DEV.txt\", \"stance\": \"silent\", \"note\": \"grep -i 'mosquee|mosquée|mesquita' in Devic's dictionary of French words of oriental origin returns nothing (the word is not among his entries in this OCR).\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"English\",\n          \"words\": \"mosque\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English mosque in its present shape is 18th-c.: Etymonline dates 'mosque' to 1717, with earlier moseak (c. 1400) and mosquee (16th c.), and notes the word was 'mangled in Middle English as muskey, moseache, etc.' — i.e. the modern form comes from French mosquée (spelling remodelled to -que), while the earlier English attempts were made directly on Romance or Levantine forms. Klein and Skeat both give simply 'F. mosquee' (Skeat citing Cotgrave's 1611 dictionary) as the immediate source, so the chart's French → English step is right; the doublet masjid was borrowed straight from Arabic much later.\",\n          \"derivation_fa\": \"واژهٔ انگلیسی mosque در شکل امروزین از ۱۷۱۷ میلادی گواهی شده و پیش از آن صورت‌های moseak (حدود ۱۴۰۰) و mosquee (سدهٔ ۱۶) در دست است؛ منبع مستقیم آن فرانسه mosquée است (کلاین؛ اسکیت با ارجاع به فرهنگ کاتگریو ۱۶۱۱) که در نوشتار به -que انگلیسی شده است. صورت masjid در انگلیسی وام‌گیری مستقیم و متأخری از عربی است و با mosque دوگانه می‌سازد. ادعای نورایی درست است.\",\n          \"sources\": [S_ETY, S_MOSQUE],\n          \"ref_check\": [\n            {\"ref\": \"KLN:1007\", \"status\": \"supports\", \"note\": KLN_MOSQUE + \" — the headword of the article is the English word itself.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"SKT\", \"where\": \"SKT.txt line 11917 s.v. Mosque\", \"stance\": \"supports\", \"note\": \"'Mosque, a Mohammedan temple. (F. — Span. — Arab.) F. mosquee, Cot.' — French source confirmed; Skeat omits the Italian stage.\"},\n            {\"src\": \"WEB\", \"where\": \"WEB_vol1.txt\", \"stance\": \"silent\", \"note\": \"Webster's New Twentieth Century (vol. 1, A-K) does not reach M; 'mosque' appears in it only inside other entries (azan, imam, Kaaba, khutbah), with no etymology of its own.\"},\n            {\"src\": \"FSD\", \"where\": \"FSD_vol2/3\", \"stance\": \"silent\", \"note\": \"grep 'mosque' in the Funk & Wagnalls volumes on disk returns only incidental uses inside other articles (haram, keblah, mihrab); the M-volume entry for mosque is not in this OCR.\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"Persian\",\n          \"words\": \"mazget\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The word itself is real and well attested: Book Pahlavi mzgt' = mazgīt 'mosque' (MacKenzie, PHD p. 58, who marks the New Persian form as identical), Early New Persian مزگت / مزکت mazgit/mazkat in the oldest poetry (Borhan quotes Farroxi Sīstānī, 'mazkat-e ādīna' = the Friday mosque; Nourai quotes Asadī), whence Old Armenian մզկիթ mzkitʿ, Kurmanji mizgeft, Central Kurdish mizgəwt, and through Turkic the Slavic mečet family. What is not settled is the arrow Nourai draws: he takes it straight from the Aramaic root box, bypassing Arabic. Mo'in's own etymological footnote in Borhan-e Qate' p. 2001 says exactly that — 'این لغت آرامی است ، قی : عربی مسجد ، اسپانیولی mezquita … وآن بنیاد مسجد عربی است' ('this word is Aramaic; cf. Arabic masjid, Spanish mezquita … and it is the foundation of the Arabic masjid') — and Mo'in's Farhang tags the headword '[آرا.]' (Aramaic). Against this, Wiktionary's descendant tree puts Middle Persian mzgt' /mazgit/ under Arabic مسجد as a borrowing, with Early New Persian مزگت under it, and Hübschmann (Armenische Grammatik I 271, cited there for the Armenian word) already derived Armenian mzkitʿ from Persian mazgit ‹ Arabic masjid. The phonetic shape favours Nourai/Mo'in: a loan from Arabic masjid should show ǧ (Persian j/ž), whereas mazgit has -g- exactly like Aramaic/Syriac msgdʾ / masgdā (with the usual devoicing of the final stop in Middle Persian, d > t, and the metathesised vowel of the Aramaic emphatic). The chronology favours the Arabic route: the form is unattested before the conquest, and Jeffery notes that even Syriac masgdā looks like a late borrowing from Arabic. The likeliest reconstruction, and the reason for 'plausible' rather than 'confirmed', is that Persian took the word in the 7th-8th c. from the Aramaic-speaking (Syriac/Nestorian) population of Mesopotamia together with the new Islamic institution — the Aramaic source Nourai draws, but not independently of Arabic.\",\n          \"derivation_fa\": \"خود واژه مسلم است: فارسی میانهٔ کتابی mzgt' (mazgīt) «مسجد» در فرهنگ مکنزی ص ۵۸، و فارسی دری «مزگت/مزکت» در کهن‌ترین شعر فارسی (فرخی سیستانی: «همچو در مزکت آدینه سرای»؛ نورایی بیت اسدی را می‌آورد)، و از همین فارسی، ارمنی مزکیث، کردی mizgeft و از راه ترکی روسی mečet برگرفته شده است. اختلاف در پیکان است: نورایی مزگت را بی‌میانجی عربی از آرامی می‌گیرد، همان‌گونه که معین در حاشیهٔ برهان قاطع (ص ۲۰۰۱) می‌نویسد «این لغت آرامی است … و آن بنیاد مسجد عربی است» و در فرهنگ فارسی نیز آن را با نشانهٔ [آرا.] می‌آورد؛ در برابر، ویکی‌واژه و هوبشمان (دستور ارمنی ۱، ص ۲۷۱) فارسی میانهٔ mazgit را وام‌گرفته از عربی مسجد می‌دانند. از نطر آوایی حق با معین است، زیرا جیم عربی در فارسی ج/ژ می‌داد نه گ، و گ در mazgit درست برابر گیمل آرامی msgdʾ است (با بی‌واکه‌شدن د > ت در پایان واژه در فارسی میانه)؛ اما از نطر تاریخی حق با دیدگاه دیگر، زیرا هیچ گواهی پیش از اسلام ندارد. به احتیاط پذیرفتنی است: فارسی این واژه را در سدهٔ یکم و دوم قمری از مردم آرامی‌زبان میانرودان گرفته است — منبع آرامی، ولی نه جدا از گسترش اسلام و واژهٔ عربی.\",\n          \"sources\": [S_MASJID, S_MZKIT],\n          \"ref_check\": [\n            {\"ref\": \"BQT:2001\", \"status\": \"supports\", \"note\": BQT_2001},\n            {\"ref\": \"MON:4063\", \"status\": \"partial\", \"note\": MON_MAZKAT},\n            {\"ref\": \"FVF:638\", \"status\": \"not_checked\", \"note\": \"FVF = Emam Shushtari, Farhang-e Vāžehā-ye Fārsi dar Zabān-e Arabi (1347/1968); per refs_online.json it exists online only on noorlib (JS viewer) and behind logins at ketabnak/parsianjoman, so p. 638 could not be read. Its claim, as Nourai reports it in the NOTE on node 1 (Arabic masjed ‹ Persian mazget), is rejected by the modern sources discussed there.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"PHD.txt line 474, leaf 79 = printed p. 58 s.v. mazgīt\", \"stance\": \"supports\", \"note\": PHD_MAZGIT},\n            {\"src\": \"MON\", \"where\": \"MON_part2.txt line 55038 s.v. مزکت\", \"stance\": \"supports\", \"note\": MON_MAZKAT},\n            {\"src\": \"FVQ\", \"where\": \"p. 263 s.v. masjid\", \"stance\": \"partial\", \"note\": \"'The Syr. masgdā, however, seems to be a late borrowing from the Arabic' — Jeffery's remark cuts against a Syriac-mediated Persian loan and favours an Arabic route for the eastern forms; he does not discuss Persian mazgit.\"},\n            {\"src\": \"HUB\", \"where\": \"HUB.txt (Persische Studien) — silent; Armenische Grammatik I 271 via Wiktionary\", \"stance\": \"contradicts\", \"note\": \"grep 'mazgit|mazkit|Moschee' in Persische Studien returns nothing; but Wiktionary's Old Armenian մզկիթ entry cites Hübschmann, Armenische Grammatik I (1897) p. 271 for 'Classical Persian مزکت (mazkit), مزگت (mazgit), from Middle Persian mzgt' /mazgit/, from Arabic مسجد (masjid)' — i.e. an Arabic, not directly Aramaic, source.\"},\n            {\"src\": \"NYB\", \"where\": \"NYB_vol2_glossary.txt\", \"stance\": \"silent\", \"note\": \"grep 'mazgit|mzgt' in Nyberg's Pahlavi glossary returns nothing; the word does not occur in his text selection.\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 6,\n      \"root\": \"Mě 1\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *mē / *méh₁, the prohibitive particle 'don't!' (Pokorny 703 me-1; Walde-Pokorny II 236 f.)\",\n      \"note\": \"The root is genuine and the language label is right; Pokorny's article 'me-1, Meaning: prohibitive particle' on exactly p. 703 lists precisely Nourai's four branches ('Old Indic Avestan Old pers. mā, gr. μή, Armenian mi ds., alb. mos ds.'), so this chart is a straight transcript of Pokorny. One refinement: *mē was not the general negation — that was *ne — but the prohibitive/vetitive particle used with the injunctive, subjunctive or imperative, so Nourai's gloss 'no, not' is too broad; modern notation is *méh₁ (Wiktionary: 'prohibitive particle: don\\\\u2019t …!', with Beekes, Martirosyan and Dunkel's LIPP 2014 as references). Watkins/AHD has no entry for it because it left no English reflex, and Mann's IEC and Buck's Synonyms are likewise silent, so Pokorny/Walde-Pokorny are the only reference works on disk that treat it.\",\n      \"note_fa\": \"ریشه اصل است و برچسب «هندواروپایی» درست: پوکورنی در همان صفحهٔ ۷۰۳ که نورایی یاد کرده، مدخل me-1 «ادات نهی» را می‌آورد و درست همان چهار شاخهٔ نمودار را فهرست می‌کند: سنسکریت، اوستایی و پارسی باستان mā، یونانی μή، ارمنی mi و آلبانی mos. یک اصلاح: این ادات، نهی است (با فعل در وجه امری، التزامی یا اینجونکتیو) و نه نفی ساده که در هندواروپایی آغازین *ne بوده است؛ پس معنای «no, not» کمی کلی است. نگارش امروزین *méh₁ است (ویکی‌واژه به استناد بکس و دونکل). واتکینز (پیوست AHD) این ریشه را ندارد، زیرا بازمانده‌ای در انگلیسی ندارد.\",\n      \"sources\": [S_MEH1],\n      \"ref_check\": [\n        {\"ref\": \"POK:703\", \"status\": \"supports\", \"note\": POK_ME1},\n        {\"ref\": \"KNT:210\", \"status\": \"not_found\", \"note\": \"Kent's lexicon entry for the particle is on p. 201 ('mā conj. \\\"not\\\", in prohibitions etc.'), with mātya on p. 202 — both verified in KNT.txt, whose OCR carries the printed page numbers 200/201/202 at lines 5727/5752/5762. Printed p. 210 lies in the v-/x- part of the same lexicon (vā, vaina-, vaḩu-, Vaumisa-, važ-, vaǵ- …); nothing on it bears on a negative particle, so KNT:210 looks like a slip for KNT:201, the number Nourai himself uses on node 1.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. II 236-237 (incoming/WLD/WLD_Bd2_pages.txt line 15490)\", \"stance\": \"supports\", \"note\": \"'1. me „(daß) nicht“, prohibitiv. … arm. mi ds. … alb. mos ds. (aus mo = idg. *me + s ‚nimcht‘)' — the article Pokorny refers to as WP. II 236 f.; the separate entry '2. me- ‚messen’' immediately follows, confirming that the prohibitive is a root of its own.\"},\n        {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt (Indo-European Roots, 1985)\", \"stance\": \"silent\", \"note\": \"The appendix has me-1 'oblique form of the 1st person pronoun', me-2 'in the middle of', mē-1 'qualities of mind', mē-2 'to measure' [Pok. 3. mē 703], mē-3 'big', mē-4 'to mow' [Pok. 2. mē 703] — but no prohibitive particle, since it has no English descendant. Note that Watkins' [Pok. … 703] tags show p. 703 also holds Pokorny's mē-2 'reap' and mē-3 'measure', so the page number alone is ambiguous.\"},\n        {\"src\": \"IEC\", \"where\": \"IEC.txt (Mann)\", \"stance\": \"silent\", \"note\": \"Mann's dictionary has 'mē (2) … acc. prn.' (the pronoun) and mēghos, mēnā etc., but no entry for the prohibitive particle (grep '^mē', 'prohibitive').\"},\n        {\"src\": \"SYN\", \"where\": \"SYN.txt (Buck)\", \"stance\": \"silent\", \"note\": \"Buck's Selected Synonyms has no chapter entry for negative particles; grep 'prohibitive' and Greek μή find nothing relevant.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan / Old Persian\",\n          \"words\": \"mâ 2; mâ-tya\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"PIE *méh₁ gives Proto-Indo-Iranian *máH > Indo-Iranian mā with regular loss of the laryngeal and compensatory length, hence Avestan mā and Old Persian mā, both the prohibitive negation. In Avestan mā stands with the injunctive/imperative: 'mā dim mruyā āθravanəm' (Y. 18), 'mā buyā aurvaθənām yaxta' (Y. 11.7), 'mā miθrake … vašǵai jasaima' (Yt. 10.98), and Bartholomae glosses such passages 'nicht sollst …' (AiW, the mā article at BRT.txt leaf 610, cf. leaf 697 'mā təm urvānəm frayavayōiš “nicht sollst…”'); Jackson's Avesta Grammar registers it flatly: 'Negative. Av. mā \\\"not\\\" (prohibitive) = Skt. mā', and notes the compositional form ma- (YAv. ma-kasviṭ ma-strī 'no dwarf, no woman', Yt. 5.92; GAv. ma-vaēθa- 'not failing', Y. 41.1) — the very shape that becomes the New Persian prefix of node 2. In Old Persian, Kent p. 201 has 'mā conj. \\\"not\\\", in prohibitions etc.: Av. Skt. mā, Gk. μή, pIE *mē', with subjunctive (DNb 55 mā-taiy, 58), optative (DB 4.59, 69, 79) and injunctive (DB 4.54). Nourai's second word is Kent's next-but-one entry (p. 202): 'mātya conj. \\\"lest, that not, not\\\": mā \\\"not\\\" + conj. tya', an enclitic compound of the particle with the relative/complementiser tya, used in DB 1.52 mātya-mām xšnāsātiy 'lest they know me' and DB 4.43, 48, 71. Nourai's index '2' distinguishes this mā from the homonymous verbal root mā- 'to measure' that Kent lists immediately after it — a real and useful distinction.\",\n          \"derivation_fa\": \"از *méh₁ هندواروپایی، در هندوایرانی با افتادن لارینگال و کشیده شدن واکه، mā پدید آمده که در اوستایی و پارسی باستان ادات نهی است. در اوستا mā با وجه اینجونکتیو/امری می‌آید (مانند mā buyā … در یسنا ۱۱، ۷) و بارتولومه در فرهنگ ایرانی باستان آن را «nicht sollst» معنی کرده است؛ جکسون هم در دستور اوستایی می‌نویسد «Av. mā ‚not‘ (prohibitive) = Skt. mā» و صورت مرکّب ma- را نیز می‌شناساند (ma-kasviṭ ma-strī). در پارسی باستان، کنت (ص ۲۰۱) mā را با وجه‌های التزامی، التماسی و اینجونکتیو می‌آورد و در ص ۲۰۲ mātya را «مبادا که، تا نه» می‌داند، مرکّب از mā + حرف ربط tya؛ نمونهٔ مشهور در بیستون ۱:۵۲ است: mātya-mām xšnāsātiy «مبادا مرا بشناسند». شمارهٔ ۲ در «mâ 2» نورایی برای جداکردن این ادات از ریشهٔ فعلی mā- «پیمودن» است و درست است. ادعای نورایی درست است.\",\n          \"sources\": [S_MEH1],\n          \"ref_check\": [\n            {\"ref\": \"POK:703\", \"status\": \"supports\", \"note\": POK_ME1 + \" — 'Old Indic Avestan Old pers. mā' is this node.\"},\n            {\"ref\": \"KNT:201\", \"status\": \"supports\", \"note\": KNT_MA + \" — Nourai's page 201 is exactly Kent's mā entry; mātya, his second word, stands overleaf on p. 202.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KNT\", \"where\": \"printed pp. 201-202 (KNT.txt lines 5754, 5760); syntax at §292b, p. 2662/3038 lines\", \"stance\": \"supports\", \"note\": KNT_MA + \" Kent also cites the clause type: 'Volitive in a negative clause of purpose introduced by mātya ‚lest’' and translates DB 1.52 'lest (the people) know me, that I am not Smerdis'.\"},\n            {\"src\": \"BRT\", \"where\": \"Bartholomae, AiW, mā article — BRT.txt leaf 610 (≈ col. 1140 ff.), further attestations on leaves 647, 697, 610\", \"stance\": \"supports\", \"note\": \"'mā dim mruyā āθravanəm … Y.18', 'mā θrayam vahištanam … V.18.17', 'mā miθrake … vašǵai jasaima Yt.10.98', 'mā buyā aurvaθənam yaxta Y.11.7', and (leaf 697) 'mā təm urvānəm frayavayōiš “nicht sollst…”' — the prohibitive mā with injunctive, exactly as drawn. (The OCR of this leaf carries no column numerals, so the citation is by leaf.)\"},\n            {\"src\": \"AVG\", \"where\": \"Jackson, Avesta Grammar, adverbs section (AVG.txt line 4246) and §866 Note (line 4804)\", \"stance\": \"supports\", \"note\": \"'d. Negative. Av. mā ‚not’ (prohibitive) = Skt. mā.' and 'Note. Original mā (prohibitive) appears as ma- in composition in YAv. ma-kasviṭ ma-strī ‚no dwarf, no woman’ et al. Yt. 5.92; GAv. ma-vaēθa- ‚not failing’ Ys. 41.1.'\"},\n            {\"src\": \"TLM\", \"where\": \"TLM.txt (Tolman, Ancient Persian Lexicon)\", \"stance\": \"silent\", \"note\": \"grep '^mā|mātya' finds only 'ma … name of a Median town'; Tolman's short lexicon does not list the particle in this OCR.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"ma- «مَ-»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Old Iranian mā continues into Middle Persian as the proclitic ma, already with a short vowel because it is unstressed: MacKenzie, PHD p. 56, 'ma [AL | M m, N ~] not (prohibitive). ~ agar [N magar] perhaps; lest' — the 'N ~' means the New Persian form is identical, and magar 'unless, perhaps' (ma + agar) shows the same particle compounded. In New Persian ma- is written together with the verb as the prohibitive of the imperative and of the optative: مرو ma-raw 'do not go', مگو ma-gu 'do not say', مباد ma-bād 'may it not be' — which is precisely how Mo'in analyses the last: 'مباد: [م. نهی + باد (فعل صیغهٔ دعا و نفرین)] سوم شخص مفرد نهی از «بودن»', i.e. 'prohibitive ma + bād'. Classical Persian also has the free form مه mah in the same function (Mo'in: 'مه: علامت نهی. نشانهٔ دعای منفی که قدما بکار می‌بردند'). In the modern spoken language ma- has largely been ousted by the general negation na- (naraw for maraw), which is why it now feels archaic/literary. The chain Avestan/Old Persian mā > MP ma > NP ma- that Nourai draws is thus exactly right; the only thing his chart does not say is the vowel shortening.\",\n          \"derivation_fa\": \"ادات نهی mā ایرانی باستان در فارسی میانه به سبب بی‌تأکید بودن به ma کوتاه شده است؛ مکنزی (ص ۵۶) می‌نویسد «ma … not (prohibitive)» و با نشانهٔ «N ~» می‌گوید که صورت فارسی نو همان است؛ همچنین magar < ma + agar. در فارسی نو این پیشوند بر فعل امر و دعا می‌نشیند: مرو، مگو، مباد؛ معین دربارهٔ مباد می‌نویسد «[م. نهی + باد]» و صورت آزاد «مه» را نیز «علامت نهی» می‌خواند. در فارسی گفتاری امروز، پیشوند نفی عام na- جای آن را گرفته (نرو در برابر مرو) و مَ- بوی ادبی و کهن گرفته است. پس زنجیرهٔ نورایی (اوستایی/پارسی باستان mā ← فارسی میانه ma ← فارسی نو مَ-) درست است؛ تنها کوتاه‌شدن واکه را نگفته است.\",\n          \"sources\": [S_MEH1],\n          \"ref_check\": [\n            {\"ref\": \"MON:3677\", \"status\": \"partial\", \"note\": \"Only the 2-vol abridgement of Mo'in's Farhang is on disk, so the printed page 3677 of the 6-vol edition cannot be checked; the substance is there, however: MON_part2.txt line 44611 'مباد: [م. نهی + باد (فعا. صیغه دعا و نفرین)] سوم شخص مفرد نهی از «بودن»' and line 68899 'مه: علامت نهی. نشانهٔ دعای منفی که قدما بکار می‌بردند' — Mo'in does treat مَ- as the prohibitive particle, which is what the arrow needs.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"PHD.txt line 437, leaf 77 = printed p. 56 s.v. ma\", \"stance\": \"supports\", \"note\": \"'ma [AL | M m, N ~] not (prohibitive). ~ agar [N magar] perhaps; lest.' — MacKenzie's 'N ~' explicitly equates the New Persian form with the Middle Persian one.\"},\n            {\"src\": \"MON\", \"where\": \"MON_part2.txt lines 44611 (مباد), 68899 (مه)\", \"stance\": \"supports\", \"note\": \"'مباد: [م. نهی + باد]' and 'مه: علامت نهی' — Mo'in's own analysis of Nourai's examples مباد/مگو/مرو.\"},\n            {\"src\": \"HRN\", \"where\": \"HRN.txt (Horn, Grundriss)\", \"stance\": \"silent\", \"note\": \"grep for the particle in Horn returns nothing: his Grundriss is a list of lexical words and does not treat the prohibitive prefix.\"},\n            {\"src\": \"NYB\", \"where\": \"NYB_vol2_glossary.txt\", \"stance\": \"silent\", \"note\": \"grep '^ma\\\\b|^mā' in Nyberg's glossary finds no entry for the particle (his glossary covers the words of his chrestomathy).\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Sanskrit\",\n          \"words\": \"mâ\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Vedic and Classical Sanskrit मा mā is the prohibitive particle, the exact Indic match of Avestan/Old Persian mā and the direct outcome of PIE *méh₁ (laryngeal lost with length). It is construed with the injunctive (the augmentless aorist/imperfect), e.g. RV mā bhaiṣ 'do not fear', mā no vadhīḥ 'do not slay us', and later with the aorist optative or imperative; Sanskrit keeps *ne only in the compounding negative na/a-, exactly the same division of labour as Greek μή : oὐ. Pokorny 703 lists 'Old Indic … mā' first among the reflexes, and Nourai's node is that item.\",\n          \"derivation_fa\": \"در سنسکریت ودایی و کلاسیک، मा mā ادات نهی است و درست برابر māی اوستایی و پارسی باستان و بازماندهٔ مستقیم *méh₁ است. این ادات با وجه اینجونکتیو (فعل بی‌پیشافزوده) می‌آید؛ مانند mā bhaiṣ «مترس» در ریگ‌ودا. تقسیم کار میان mā (نهی) و na (نفی) درست مانند μή : oὐ یونانی است. پوکورنی در ص ۷۰۳ همین را نخست می‌آورد؛ ادعای نورایی درست است.\",\n          \"sources\": [S_MEH1],\n          \"ref_check\": [\n            {\"ref\": \"POK:703\", \"status\": \"supports\", \"note\": POK_ME1 + \" — 'Old Indic … mā' is this node, on the page Nourai cites.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. II 236 f.\", \"stance\": \"supports\", \"note\": \"'1. me „(daß) nicht“, prohibitiv' — the same article, with the Indo-Iranian material Pokorny abridges.\"},\n            {\"src\": \"AVG\", \"where\": \"AVG.txt line 4246 (Jackson, Avesta Grammar 'in comparison with Sanskrit')\", \"stance\": \"supports\", \"note\": \"'Av. mā ‚not’ (prohibitive) = Skt. mā' — the Indic and Iranian forms equated by a Sanskritist.\"},\n            {\"src\": \"IEC\", \"where\": \"IEC.txt (Mann)\", \"stance\": \"silent\", \"note\": \"no entry for the prohibitive particle; Mann's mē (2) is the accusative pronoun.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Greek\",\n          \"words\": \"mě\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Ancient Greek μή is the inherited prohibitive negation, from PIE *méh₁ with the regular Attic-Ionic ē (Doric/Aeolic mā is not preserved; μή is pan-Greek). From Homer on it negates wishes, commands and purpose clauses (μή + aorist subjunctive or present imperative) as against οὐ for statements of fact, and it survives in the derivatives μηδέ, μηδείς, μήπω and in learned English formations such as 'medeis'; its Armenian cognate is mi and its Albanian one mos (*mē + s). Pokorny 703 cites 'gr. μή' as one of the four reflexes, and Wiktionary's *méh₁ page derives μή from it through Proto-Hellenic *mḗ on Beekes' authority — so this node is confirmed.\",\n          \"derivation_fa\": \"یونانی باستان μή ادات نهی موروثی است که از *méh₁ با تحول منطقی واکهٔ بلند به ē در آتیکی–ایونیایی بازمانده است. از هومر به بعد، μή بر سر آرزو، فرمان و جملهٔ غایت (با التزامی آئوریست یا امر مضارع) می‌آید، در برابر οὐ که نفی خبری است؛ مشتقّات آن μηδέ، μηδείς و μήπω اند و هم‌ریشهٔ ارمنی آن mi و آلبانی mos (*mē+s) است. پوکورنی ص ۷۰۳ و ویکی‌واژه (به استناد بکس) همین را می‌گویند؛ ادعای نورایی درست است.\",\n          \"sources\": [S_MEH1],\n          \"ref_check\": [\n            {\"ref\": \"POK:703\", \"status\": \"supports\", \"note\": POK_ME1 + \" — 'gr. μή' is this node.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. II 236-237\", \"stance\": \"supports\", \"note\": \"The prohibitive article opens with the Greek and Armenian evidence ('… (Curtius 332 f.), arm. mi ds. Hübschmann Arm. Gr. I 474, alb. mos ds.') — Greek μή is its starting point.\"},\n            {\"src\": \"SYN\", \"where\": \"SYN.txt (Buck)\", \"stance\": \"silent\", \"note\": \"Buck has no synonym chapter for negative particles; the Greek word is not treated (grep 'μή', 'prohibitive').\"},\n            {\"src\": \"IEC\", \"where\": \"IEC.txt (Mann)\", \"stance\": \"silent\", \"note\": \"no entry for the prohibitive *mē.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\n\nimport io, os\np = \"/home/sfmqrb/git/rishe/data/verification/page-322.json\"\nwith io.open(p, \"w\", encoding=\"utf-8\") as f:\n    json.dump(data, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"written\", os.path.getsize(p))\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/mk322.py",
 "description": "Write page-322.json"
}
```


### [2026-09-07T16:09:23.222Z] TOOL RESULT

```
written 60592
```


## [2026-09-07T16:09:26.646Z] TOOL CALL #60: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-322.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 322",
 "description": "Validate and run verify_check"
}
```


### [2026-09-07T16:09:28.004Z] TOOL RESULT

```
JSON OK
nodes verified: 11/11
node verdicts: {'confirmed': 10, 'plausible': 1}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 9, 'not_checked': 3, 'partial': 2}
books consulted: {'supports': 22, 'partial': 4, 'silent': 11, 'contradicts': 1} | by book: {'LKT': 4, 'SKT': 3, 'MON': 3, 'FVQ': 2, 'KLN': 2, 'DOZ': 2, 'PHD': 2, 'NYB': 2, 'AVG': 2, 'WLD': 2, 'IEC': 2, 'AFA': 1, 'BQT': 1, 'LAM': 1, 'DEV': 1, 'WEB': 1, 'FSD': 1, 'HUB': 1, 'KNT': 1, 'BRT': 1, 'TLM': 1, 'HRN': 1, 'SYN': 1}
```


## [2026-09-07T16:09:38.758Z] TOOL CALL #61: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport io\np='data/verification/page-322.json'\nt=io.open(p,encoding='utf-8').read()\nn=t.count('از نطر')\nt=t.replace('از نطر','از نظر')\nio.open(p,'w',encoding='utf-8').write(t)\nprint('fixed',n)\nEOF\npython3 -m json.tool data/verification/page-322.json >/dev/null && python3 tools/verify_check.py 322 | tail -6",
 "description": "Fix Persian typo and revalidate"
}
```


### [2026-09-07T16:09:40.252Z] TOOL RESULT

```
fixed 2
nodes verified: 11/11
node verdicts: {'confirmed': 10, 'plausible': 1}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 9, 'not_checked': 3, 'partial': 2}
books consulted: {'supports': 22, 'partial': 4, 'silent': 11, 'contradicts': 1} | by book: {'LKT': 4, 'SKT': 3, 'MON': 3, 'FVQ': 2, 'KLN': 2, 'DOZ': 2, 'PHD': 2, 'NYB': 2, 'AVG': 2, 'WLD': 2, 'IEC': 2, 'AFA': 1, 'BQT': 1, 'LAM': 1, 'DEV': 1, 'WEB': 1, 'FSD': 1, 'HUB': 1, 'KNT': 1, 'BRT': 1, 'TLM': 1, 'HRN': 1, 'SYN': 1}
```


## [2026-09-07T16:09:47.343Z] TOOL CALL #62: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport io\np='data/verification/page-322.json'\nt=io.open(p,encoding='utf-8').read()\nprint(t.count('\\\\\\\\u2019'), t.count('\\\\u2019'))\nt=t.replace('don\\\\\\\\u2019t',\"don't\").replace('don\\\\u2019t',\"don't\")\nio.open(p,'w',encoding='utf-8').write(t)\nEOF\ngrep -o \"prohibitive particle: don[^,]*\" data/verification/page-322.json | head -3\npython3 -m json.tool data/verification/page-322.json >/dev/null && python3 tools/verify_check.py 322 | head -3",
 "description": "Clean escaped apostrophe"
}
```


### [2026-09-07T16:09:48.689Z] TOOL RESULT

```
1 1
prohibitive particle: don't …!'
nodes verified: 11/11
node verdicts: {'confirmed': 10, 'plausible': 1}
root verdicts: {'confirmed': 2}
```


## [2026-09-07T16:10:08.194Z] AGENT

Page 322 (book p. 292) verified — `data/verification/page-322.json`, `verify_check.py 322` reports 11/11 nodes, 0 PROBLEM lines.

Counts: 2 non-redirect entries (4 redirects skipped: Massa, Mâ-ter, Mazaxa, Mbh, Mbhi). Roots: 2 confirmed. Nodes: 10 confirmed, 1 plausible. Ref checks: 9 supports, 2 partial, 3 not_checked, 1 not_found (root-level). No disputed and no transcription_suspect items; no extraction errors found (the JSON matches the sources' spellings, and Nourai's BQT:2001 citation hits the exact printed page).

- **Plausible — Masgdâ #7, Persian mazget «مزگت»**: the word and its descendants (MP mzgt' = mazgīt, MacKenzie p. 58; Armenian մզկիթ, Kurdish mizgeft, Slavic mečet) are solid, but the *direct* Aramaic arrow is contested. Mo'in's own footnote in Borhan-e Qate' p. 2001 backs Nourai verbatim («این لغت آرامی است … و آن بنیاد مسجد عربی است»), while Wiktionary and Hübschmann (Arm. Gramm. I 271) derive MP mazgit from Arabic masjid. Phonology (-g-, final -t) favours Aramaic; chronology (no pre-Islamic attestation) favours Arabic — likeliest a 7th–8th-c. loan from Mesopotamian Aramaic speakers along with the institution.
- **Note on Masgdâ #1 evaluated**: FVF:638's claim that Arabic masjed comes from Persian mazget is rejected — Aramaic msgdʾ is attested at Elephantine in the 5th c. BCE and masjid stands in pre-Islamic poetry and 28 times in the Qur'an (Jeffery, FVQ p. 263).
- **Mě 1 root, KNT:210 = not_found**: Kent's `mā` is on p. 201 and `mātya` on p. 202 (both verified); printed p. 210 is in the v-/x- stretch of the lexicon. Almost certainly a slip for 201, the number Nourai himself uses on node 1. Also flagged in the note: PIE *meh₁ is the *prohibitive* particle, not the general negation (*ne), so the gloss "no, not" is too broad; Watkins/AHD, Mann and Buck have no entry at all (no English/lexical reflex).
- Klein's page number KLN:1007 checks out exactly (KLN_1966 leaf 540 = pp. 1007–1008, the "mosque" article), and it carries the whole western chain Arabic → Sp. mesquita → It. moschea (‹ moscheta) → F. mosquee → E. mosque, corroborated by Lokotsch no. 1435, Skeat, Lammens and Dozy.
- New artifacts saved for audit: `data/verification/sources/refs/ocr/BQT/2001.png` + `2001.vision.txt` (my transcript of Mo'in's footnote 8), plus 6 archived web sources under `data/verification/sources/web/`.
