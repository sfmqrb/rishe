# Verification process log — verify-page-350


## [2026-09-07T18:17:44.146Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 350 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-350.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-350.json. Write /home/sfmqrb/git/rishe/data/verification/page-350.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 350` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-07T18:17:46.330Z] AGENT

I'll start by reading the instructions.


## [2026-09-07T18:17:46.879Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-07T18:17:46.894Z] TOOL RESULT

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


## [2026-09-07T18:17:47.699Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-350.txt"
}
```


### [2026-09-07T18:17:47.723Z] TOOL RESULT

```
1	=== PDF page 350 (book page 320) ===
2	--- entry 0 ---
3	ROOT [Sanskrit] Nârikelah, Nârikerah : coconut  (refs KLN:1028)
4	#1 (parent #0) [Pahlavi] refs=PLA:256 | anârgîl
5	  #2 (parent #1) [Persian] refs=AHD:873; BQT:2095 | nârgîl «نارگیل» : coconut ; nârgîleh «نارگیله» : a water pipe made with coconut shell
6	    #3 (parent #2) [French] refs=AHD:873 | narguile : water pipe
7	      #4 (parent #3) [English] refs=None | nargeela, narghile : water pipe
8	--- entry 1 ---
9	ROOT Nârikerah -> redirect to Nârikelah
10	--- entry 2 ---
11	ROOT [Indo-European] Nas : nose  (refs POK:755,768)
12	#1 (parent #0) [Avestan / Old Persian] refs=KNT:193 | nâh, nâham : nose
13	#2 (parent #0) [Sanskrit] refs=KNT:193 | nas : nose
14	#3 (parent #0) [Germanic] refs=AHD | nasô : nose
15	  #4 (parent #3) [English] refs=KNT:193 | nose, nostril
16	#5 (parent #0) [Latin] refs=AHD | nâsus : nose
17	  #6 (parent #5) [English] refs=AHD | nasal, naso-
18	--- entry 3 ---
19	ROOT Nask -> redirect to Naks
20	--- entry 4 ---
21	ROOT Nau -> redirect to Na 1
22	--- entry 5 ---
23	ROOT Naus -> redirect to Na 1
24	--- entry 6 ---
25	ROOT [Semitic] N.b.b : to make hollow, dig a hole  (refs KLN:138)
26	#1 (parent #0) [Akkadian] refs=KLN:138; AKD:30 | nebâbâ : hole ; imbŭbu : hollow tube ; bâbu : door ; bâb-ilu : gate to gods ☞Layh
27	  #2 (parent #1) [Aramaic] refs=AKD:30 | 
28	    #3 (parent #2) [Arabic] refs=None | 
29	      #4 (parent #3) [Persian] refs=MON | bâb 2 «باب ۲» : door ; anbŭb «انبوب» : pipe, flute ; Bâbel «بابل» : Babylonia
30	  #5 (parent #1) [Hebrew] refs=None | 
31	    #6 (parent #5) [English] refs=KLN:138 | Babel, Babylonia
32	
```


## [2026-09-07T18:17:51.129Z] TOOL CALL #3: Bash

```json
{
 "command": "python3 -m json.tool data/extracted/batch/page-350.json | head -200",
 "description": "Read source JSON for page 350"
}
```


### [2026-09-07T18:17:52.524Z] TOOL RESULT

```
{
    "pdf_page": 350,
    "book_page": 320,
    "entries": [
        {
            "root": {
                "name": "N\u00e2rikelah, N\u00e2rikerah",
                "lang": "Sanskrit",
                "refs": "KLN:1028",
                "gloss": "coconut"
            },
            "nodes": [
                {
                    "id": 1,
                    "parent": 0,
                    "lang": "Pahlavi",
                    "refs": "PLA:256",
                    "words": [
                        {
                            "translit": "an\u00e2rg\u00eel",
                            "gloss": null,
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 2,
                    "parent": 1,
                    "lang": "Persian",
                    "refs": "AHD:873; BQT:2095",
                    "words": [
                        {
                            "translit": "n\u00e2rg\u00eel",
                            "gloss": "coconut",
                            "script": "\u0646\u0627\u0631\u06af\u06cc\u0644"
                        },
                        {
                            "translit": "n\u00e2rg\u00eeleh",
                            "gloss": "a water pipe made with coconut shell",
                            "script": "\u0646\u0627\u0631\u06af\u06cc\u0644\u0647"
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 3,
                    "parent": 2,
                    "lang": "French",
                    "refs": "AHD:873",
                    "words": [
                        {
                            "translit": "narguile",
                            "gloss": "water pipe",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 4,
                    "parent": 3,
                    "lang": "English",
                    "refs": null,
                    "words": [
                        {
                            "translit": "nargeela, narghile",
                            "gloss": "water pipe",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                }
            ]
        },
        {
            "root": {
                "name": "N\u00e2rikerah",
                "redirect": "N\u00e2rikelah"
            },
            "nodes": []
        },
        {
            "root": {
                "name": "Nas",
                "lang": "Indo-European",
                "refs": "POK:755,768",
                "gloss": "nose"
            },
            "nodes": [
                {
                    "id": 1,
                    "parent": 0,
                    "lang": "Avestan / Old Persian",
                    "refs": "KNT:193",
                    "words": [
                        {
                            "translit": "n\u00e2h, n\u00e2ham",
                            "gloss": "nose",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 2,
                    "parent": 0,
                    "lang": "Sanskrit",
                    "refs": "KNT:193",
                    "words": [
                        {
                            "translit": "nas",
                            "gloss": "nose",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 3,
                    "parent": 0,
                    "lang": "Germanic",
                    "refs": "AHD",
                    "words": [
                        {
                            "translit": "nas\u00f4",
                            "gloss": "nose",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 4,
                    "parent": 3,
                    "lang": "English",
                    "refs": "KNT:193",
                    "words": [
                        {
                            "translit": "nose, nostril",
                            "gloss": null,
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 5,
                    "parent": 0,
                    "lang": "Latin",
                    "refs": "AHD",
                    "words": [
                        {
                            "translit": "n\u00e2sus",
                            "gloss": "nose",
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
                    "refs": "AHD",
                    "words": [
                        {
                            "translit": "nasal, naso-",
                            "gloss": null,
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                }
            ]
        },
        {
            "root": {
                "name": "Nask",
                "redirect": "Naks"
            },
            "nodes": []
        },
        {
            "root": {
                "name": "Nau",
                "redirect": "Na 1"
            },
            "nodes": []
        },
```


## [2026-09-07T18:17:53.834Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['KLN','PLA','AHD','BQT','POK','KNT','AKD','MON','WLD','HRN','HUB','PHD','NYB','FVQ','AFM','SKT','WEB','IEC','SYN','ARY','LKT','BRT','CHEUNG','FSD','HJB','AID','TTS','DEV','PHN','DOZ','LAM','AFA']:\n    v=d.get(k)\n    print(k, json.dumps(v,ensure_ascii=False)[:400] if v else 'MISSING')\n\""
}
```


### [2026-09-07T18:17:55.116Z] TOOL RESULT

```
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "loca
AKD {"title": "H. Zimmern, Akkadische Fremdwörter als Beweis für babylonischen Kultureinfluss, Leipzig 1917 (2nd ed.)", "edition_found": "1915 first edition (1917 is the 2nd, enlarged ed.; pagination may differ slightly)", "kind": "archive_djvu", "url": "https://archive.org/details/akkadischefremdw00zimmuoft", "identifier": "akkadischefremdw00zimmuoft", "local_file": "/home/sfmqrb/git/rishe/data/verif
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.t
AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_page
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 =
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
CHEUNG MISSING
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
HJB {"title": "H. Yule & A. C. Burnell, Hobson-Jobson, 2nd ed. by W. Crooke, London 1903 (Delhi reprint 1968)", "edition_found": "1903 Crooke edition (pagination identical to the 1968 reprint)", "kind": "archive_djvu", "url": "https://archive.org/details/hobsonjobsonagl02croogoog", "identifier": "hobsonjobsonagl02croogoog (others: bub_gb_6Z5iAAAAMAAJ, hobsonjobsonglos00yulerich, india.history.resource
AID {"title": "G. C. Whitworth, An Anglo-Indian Dictionary, London 1885", "edition_found": "1885 (DLI scan); also 1981 reprint scan", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.45332", "identifier": "in.ernet.dli.2015.45332 (also anglo-indiandictionary, 1981 reprint)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AID.txt", "page_offset": "leaf
TTS {"title": "H. Vámbéry, Etymologisches Wörterbuch der turko-tatarischen Sprachen, Leipzig 1878 (repr. Osnabrück 1972)", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/etymologischesw00vmuoft (Toronto scan; also Google/bub_gb copies)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft.pdf", 
DEV {"title": "L. M. Devic, Dictionnaire étymologique des mots français d'origine orientale, Paris 1876", "edition_found": "1876", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairety00devi", "identifier": "dictionnairety00devi (also dictionnairetym02devigoog, fr105comparative41)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/DEV.txt", "page_offset": "leaf
PHN {"title": "A. P. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du turc, Paris 1866", "edition_found": "1866", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairetym01pihagoog", "identifier": "dictionnairetym01pihagoog (others: bub_gb_QnsSAAAAIAAJ, dictionnairetym00pihagoog)", "local_file": "/home/sfmqrb/git/rishe/data/verific
DOZ {"title": "R. Dozy, Oosterlingen: Verklarende lijst der Nederlandsche woorden die uit het Arabisch, Hebreeuwsch, Chaldeeuwsch, Perzisch en Turksch afkomstig zijn, Leiden 1867", "edition_found": "1867", "kind": "archive_djvu", "url": "https://archive.org/details/oosterlingenver00dozygoog", "identifier": "oosterlingenver00dozygoog (also ...01dozygoog, ...02dozygoog)", "local_file": "/home/sfmqrb/git
LAM {"title": "H. Lammens, Remarques sur les mots français dérivés de l'arabe, Beyrouth 1890", "edition_found": "1890", "kind": "archive_djvu", "url": "https://archive.org/details/remarquessurles00lammgoog", "identifier": "remarquessurles00lammgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAM.txt", "page_offset": "leaf = printed + 57 (e.g. leaf 59 = p.2). local file has \
AFA {"title": "S. Fraenkel, Die aramäischen Fremdwörter im Arabischen, Leiden 1886 (repr. Hildesheim 1962, same pagination)", "edition_found": "1886", "kind": "archive_djvu", "url": "https://archive.org/details/diearamischenfr00fraegoog", "identifier": "diearamischenfr00fraegoog (also bub_gb_SzdbAAAAQAAJ)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AFA.txt", "page_offset": "
```


## [2026-09-07T18:17:59.862Z] TOOL CALL #5: Bash

```json
{
 "command": "sed -n 1,120p tools/verify_check.py"
}
```


### [2026-09-07T18:17:59.921Z] TOOL RESULT

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


## [2026-09-07T18:18:00.453Z] TOOL CALL #6: Bash

```json
{
 "command": "ls data/verification/ | head -40 && ls data/verification/sources/refs/ | head -60"
}
```


### [2026-09-07T18:18:00.507Z] TOOL RESULT

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
```


## [2026-09-07T18:18:25.124Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN 1966 narghile/nargile ===\"; grep -n -i -E \"narghile|nargile|narg[ui]\" KLN_1966.txt | head -20\necho \"=== KLN 1966 coco ===\"; grep -n -i -E \"^coco|coco-nut|coconut\" KLN_1966.txt | head -20\necho \"=== KLN Babel ===\"; grep -n -i -E \"Babel|Babylon\" KLN_1966.txt | head -30"
}
```


### [2026-09-07T18:18:25.209Z] TOOL RESULT

```
=== KLN 1966 narghile/nargile ===
24983:narghile,  nargile,  n.,  hookah,  an  Oriental  pipe.  — Pers.  nargil,  ‘coconut  tree';  prob.  fr.  OI.  ndrike- rah,  ndrikelah,  of  s.m.,  which  is  of  uncertain, possibly  Dravidian,  origin;  so  called  because orig.  narghiles  were  made  of  coconut  shells, narial,  adj.,  pertaining  to  the  nares.  —  Formed fr.  nares  with  suff.  -ial.
=== KLN 1966 coco ===
6133:Calanthe,  n.,  a  genus  of  orchids  (bot.)  —  ModL., compounded  of  Gk.  xaXo?,  ‘beautiful’,  and Svffo?,  ‘flower’.  See  calo-  and  anther, calapite,  n.,  mass  found  in  coconuts.  —  Fr.  Malay kalapa,  ‘coco  tree’.
6539:careen,  tr.  and  intr.  v.,  to  cause  (a  ship)  to  turn aside.  —  F.  cariner,  carener,  lit.  ‘to  expose  a ship’s  keel’,  fr.  carine,  carine,  ‘keel  of  a  ship', fr.  dial.  It.  earena,  fr.  L.  carina,  of  s.m.,  orig. ‘shell  of  a  nut’,  which  is  cogn.  with  Gk.  xapuov, ‘nut,  walnut’,  xapna,  ‘the  walnut  tree’,  and  prob. also  with  OI.  kdrakah,  ‘coconut;  water  vessel made  from  coconut’.  Cp.  Carya,  karyo-,  and the  first  element  in  gillyflower.  Cp.  also  carina. For  the  sense  development  of  L.  carina  cp.  E. hull,  ‘the  body  of  a  ship’,  prop,  figurative  use  of hull,  ‘husk’.
9130:Derivative:  coppl-ed,  adj. coppy,  n.,  a  dialectal  form  of  coppice.  —  This word  owes  its  existence  to  a  double  error.  The noun  coppice  (q.v.)  was  misspelled  coppies,  and this  latter  was  mistaken  for  a  plural,  from  which the  singular  coppy  was  reconstructed, copr-,  form  of  copro-  before  a  vowel, copra,  n.,  the  dried  kernel  of  the  coconut.  — Port.,  fr.  Malayalam  koppara,  fr.  Hind,  khoprd, rel.  to  Hind,  khopri  and  khappar,  ‘skull’,  fr.  OI. kharparah,  ‘skull’.  See  Yule-Burnill,  Hobson- Jobson,  p.254.
24983:narghile,  nargile,  n.,  hookah,  an  Oriental  pipe.  — Pers.  nargil,  ‘coconut  tree';  prob.  fr.  OI.  ndrike- rah,  ndrikelah,  of  s.m.,  which  is  of  uncertain, possibly  Dravidian,  origin;  so  called  because orig.  narghiles  were  made  of  coconut  shells, narial,  adj.,  pertaining  to  the  nares.  —  Formed fr.  nares  with  suff.  -ial.
=== KLN Babel ===
568:Babylonian
2069:Akkadian,  also  Accadian,  adj.  and  n.  —  Formed with  suff.  -ian  fr.  Heb.  Akkad  (Gen.  10:10), name  of  a  district  and  city  in  Babylonia, al-,  assimilated  form  of  ad-  before  /.
2513:‘mountain  dwellers’  (sing,  used  collectively), and  rel.  to  amir,  ’top,  summit’.  Akkadian  Amur- ru,  in  mat  Amurru,  ‘land  of  the  West’,  is  a  loan word  whose  sense  development  finds  its  ex¬ planation  in  the  fact  that  the  Amorites  lived  to the  west  of  Assyria  and  Babylonia.  For  the ending  see  subst.  suff.  -ite.
4216:Bab,  n.,  title  given  to  the  founder  of  Babism.  — Pers.  bdb,  ‘door,  gate’,  fr.  Arab,  bdb,  of  s.m., fr.  Aram,  babh,  babhd,  fr.  Akkad,  babu,  ‘door, gate’,  which  is  shortened  fr.  *nebdba,  lit.  ‘hole, aperture’,  from  Sem.  stem  n-b-b,  ‘to  make  hol¬ low,  to  hollow  out’,  whence  also  Heb.  nlbhubh, ‘hollowed’,  Aram.-Syr.  abbubhd,  Akkad,  imbiibu, ‘flute’,  Arab,  anbub,  ‘part  of  reed  between knots’.  Cp.  Babel.
4221:babble,  intr.  and  tr.  v.  —  ME.  babelen,  from  the I.-E.  imitative  base  *bab-,  whence  also  ON. babba ,  Swed.  babbla ,  Norw.  babble,  LG.  bab- beln,  Du.  babbelen,  G.  babbeln,  ‘to  prattle',  L. babulus ,  ‘babbler’,  F.  babilter,  ‘to  stutter,  stam¬ mer’  ;  cp.  babe,  baboon,  bauble.  Cp.  the  related imitative  base  *balb-,  whence  L.  balbus,  ‘stam¬ merer’  ;  see  balbuties,  booby.  Cp.  also  the  related imitative  base  *barb-,  ‘to  stammer’,  whence  Gk. ^ap^apoi ;,  ‘foreign,  barbarous’;  see  barbaric, brave.
4223:Babel,  n.,  name  of  the  capital  of  Babylonia.  — Heb.  Babhel,  fr.  Akkad.  Bab-ilu,  lit.  ‘the  gate  of God’,  prop,  a  literal  translation  of  Sumerian Ka-dingir.  Akkad.  Bab-ilu  is  compounded  of bdb,  ‘gate’,  and  ilu,  ‘god’.  The  first  element  is rel.  to  Aram,  babh,  babhd,  ‘door,  gate’ ;  see  Bab. For  the  second  element  see  El.  Cp.  the  second element  in  Zerubbabel.  Cp.  also  Babylon, babiroussa,  babirussa,  n.,  a  species  of  wild  swine.
4227:Derivatives:  baby,  adj.  and  tr.  v.,  baby-hood,  n., baby-ish,  adj.,  baby-ish-ly,  adv.,  baby-ish-ness,n. Babylon,  n.,  the  capital  of  Babylonia.  —  L.,  fr. Gk.  BafluXtiv,  fr.  Akkad.  Bab-ilani,  ‘the  gate of  the  gods’,  fr.  bdb,  ‘gate’,  and  ildni,  pi.  of  ilu, ‘god’.  Compared  with  Akkad.  Bab-ilu  (see Babel),  Bab-ilani  is  a  later  form,  occurring  in texts  dating  from  the  Neo-Babylonian  period. Babylonia,  n.  —  L.,  fr.  Gk.  BafluXiovta,  fr.  Ba- fluXcov.  See  prec.  word.
4228:Derivatives:  Babyloni-an,  adj.  and  n. bacalao,  n.,  a  West  Indian  fish,  Mycteroperca falcata.  —  Sp.,  ‘codfish’,  fr.  L.  baculum,  ‘a  stick, a  staff’,  whence  also  ODu.  bakeljauw.  See  bacil¬ lus  and  cp.  cabilliau.  For  sense  development cp.  stockfish.
4568:battology,  n.,  superfluous  repetition  in  speaking or  writing.  —  Gk.  jJaTToXoyla,  ‘a  speaking stammeringly��,  compounded  of  *fJa-rro<;,  ‘stam¬ merer’  (cp.  Ba-rroi;,  name  of  a  stammerer  in Herod.  4,155;  (JaTTapt^stv,  to  stutter,  stam¬ mer’),  and  -Xofla,  fr.  -Xoyoc,  ‘one  who  speaks (in  a  certain  manner);  one  who  deals  (with  a certain  topic)’.  The  first  element  is  of  imitative origin.  For  the  second  element  see  -logy. Derivatives:  battolog-ical,  adj.,  battolog-ist,  n. battue,  n.,  1)  beating  of  woods  to  drive  game  out; 2)  the  game  thus  shot.  —  F.,  ‘beating’,  prop.  fem. pp.  of  battre,  ‘to  beat’.  See  batter,  ‘to  beat’, batz,  n.,  a  small  coin,  formerly  current  in  Swit¬ zerland.  —  G.  Batz,  Batzen,  orig.  meaning  ‘a thick  piece,  lump’,  rel.  to  the  verb  batzen,  ‘to  be sticky,  be  adhesive’,  which  is  contracted  fr. *backezen,  freq.  of  backen,  ‘to  bake;  to  stick together’,  but  influenced  in  form  by  G.  Batz, Petz,  pet  form  of  Bar,  ‘bear',  the  animal  repre¬ sented  in  the  arms  of  Bern.  See  bake  and  bezzo. bauble,  n.,  jester’s  stick.  —  ME.  babel,  fr.  OF. baubel,  babel,  ‘toy’;  related  to  E.  babe,  baby, baud,  n.,  (a  term  in  telegraphic  signaling)  one  dot per  second.  —  Named  after  the  French  inventor Jean  Baudot  (1845-1903).
4692:Bel,  n.,  the  god  of  the  earth  in  Babylonian  my¬ thology.  — -  Akkad.  Belu  (whence  Heb.  Bel,  Gk. BrjXoi;),  lit.  ‘owner,  master,  lord’,  rel.  to  Heb. Ba'al.  See  Baal.
11287:Diaspora,  n.,  the  Dispersion,  the  Jews  scattered among  the  Gentiles  after  the  Babylonian  captiv¬ ity.  —  Gk.  StaoTTops,  ‘a  scattering  about,  dis¬ persion’,  fr.  StaaTxeipeiv,  ‘to  scatter  about, distribute’,  fr.  81.x  (see  dia-)  and  aneipeiv,  ‘to scatter’.  See  spore  and  cp.  next  word.
12751:El,  n.,  Hebrew  name  for  God.  —  Heb.  El,  ‘God’, of  uncertain  etymology;  possibly  related  to  el, ‘strong’  (cp.  e.g.  Gen.  31: 29  yesh  ESI  yadt,  ‘it is  in  my  power’).  Cp.  Elohim.  Cp.  also  the  first element  in  the  PN.s  Eleazar,  Eliezer,  Elihu, Elijah,  Elishah,  Elizabeth,  and  the  second  ele¬ ment  in  Babel,  bethel  and  in  the  PN.s  Daniel, Emmanuel,  Ezekiel,  Gabriel,  Gamaliel,  Ishmael, Israel,  Joel,  Michael,  Nathaniel,  Raphael, Samuel.
14045:exilian,  exilic,  adj.,  pertaining  to  the  exile  of  the Jews  in  Babylonia,  —  Formed  with  suff.  -ian, resp.  -ic,  fr.  L.  exilium.  See  exile,  ‘banishment’, exility,  n.,  slenderness.  —  L.  exilitas,  ‘smallness, thinness,  meagemess,  slenderness’,  fr.  extlis, ‘small,  thin,  meager,  slender’,  which  prob. stands  for  *ex-bg-slis  and  is  rel.  to  exiguus, ‘small,  scanty,  petty’.  See  exiguous  and  -ity. eximious,  adj.,  choice,  excellent.  —  L.  eximius , ‘select,  choice’,  lit.  ‘taken  out’,  fr.  eximere,  ‘to take  out,  take  away’,  fr.  ist  ex-  and  emere,  ‘to take,  buy’.  See  exempt,  v.  For  E.  -ous,  as equivalent  to  L.  -us,  see  suff.  -ous.
15782:gantlet,  also  spelled  gauntlet,  n.,  a  former  mili¬ tary  punishment  in  which  the  offender  was  com¬ pelled  to  run  between  two  files  of  men  who  struck him  with  switches,  clubs,  etc.,  as  he  passed.  — Formed  under  the  influence  of  gauntlet,  ‘glove’, fr.  earlier  gantlope,  fr.  Swed.  gatlopp,  lit.  ‘a  run¬ ning  down  a  lane’,  a  compound  of  gala,  ‘lane’, and  lopp,  ‘a  running,  course’,  which  is  rel.  to Swed.  lopa,  ‘to  run'.  The  first  element  is  rel.  to ON.  gata,  ‘road’ ;  see  gate,  ‘passage’.  For  the second  element  see  leap, gantlet,  n.,  a  glove.  —  See  gauntlet, gantry,  also  gauntry,  n.,  1)  a  wooden  frame  for barrels;  2)  a  spanning  framework.  —  OF.  gan¬ der,  chantier  (F.  chantier),  ‘timber  yard’,  fr.  L. cantherius,  ‘a  gelding;  trellis;  rafter’,  fr.  Gk. xav&TjXto?,  ‘pack  ass’.  Cp.  chantier,  shanty. Ganymede,  n.,  a  beautiful  boy,  cupbearer  to  Zeus (Greek  mythol.)  —  L.  Ganymedes,  fr.  Gk.  Favu- |j.r|87)4,  lit.  ‘rejoicing  in  his  virility’,  compounded of  yivuixat,  ‘I  am  glad,  rejoice’,  and  fXTjSea (pi.),  ‘counsels,  plans,  cunning’.  For  the  first element  see  ganoid.  The  second  element  is  rel. to  |rr)8e<jffai,  ‘to  devise,  resolve,  advise’,  p£8cov, [xe8£tuv,  ‘guardian,  ruler’  (prop.  pres,  part  of  the ancient  verb  piSeiv,  ‘to  protect,  rule  over’),  p.t- SecrUai,  ‘to  be  mindful  of,  give  heed  to,  think on’,  piSiiivos,  ‘a  measure’,  fr.  I.-E.  base ‘to  measure,  limit,  consider’,  which  is  a  -d-e n- largement  of  base  *me-,  ‘to  measure’.  See meditate  and  cp.  Andromeda  and  words  there referred  to.  Cp.  also  catamite, gaol,  gaoler,  gaoleress.  See  jail,  jailer,  jaileress. Gaon,  n.,  a  title  given  to  the  heads  of  the  two Babylonian  academies  of  Sura  and  Pumbedita (Jewish  hist.)  —  Heb.  gd'dn,  prob.  meant  as  an abbreviation  of  ge6n  Ya'akobh,  ‘the  pride  of Jacob’  (Ps.47:5).  Heb.  ga'Sn,  ‘exaltation,  pride, excellence’,  derives  from  the  stem  of  ga'dh, ‘rose’,  whence  also  ge,  ge'eh,  ‘proud’,  ga'dwd", ‘pride,  majesty’,  gi'&th ,  ‘majesty’.  Cp.  Aram.
17338:Derivatives:  hazi-ly,  adv.,  hazi-ness,  n. hazzan,  chazzan,  also  spelled  hazan,  chazan,  n., Jewish  cantor.  —  Mishnaic  Heb.  and  Aram. hazzdn ,  ‘superintendent,  officer’,  later  ‘cantor’, prob.  borrowed  fr.  Akkad,  hazanu,  hazannu, ‘chief  magistrate  of  a  town’  (cp.  Aram,  hazzand malhd,  ‘superintendents  of  the  town’,  Talmud Babha  Metzi'a,  93 b).  It  is  very  probable,  how¬ ever,  that  Akkad,  hazanu  was  borrowed  from  a WSem.  language  and  that  the  word  orig.  meant ‘overseer’,  from  a  verb  meaning  ‘to  see’;  cp. Heb.  hazdh,  Aram,  hazd,  ‘he  saw’.  (In  Akkadian, the  verb  hazd,  ‘to  see’,  does  not  occur;  if  it  had existed,  hazanu  might  be  its  derivative.)  If  Ak¬ kad.  hazanu  is  a  WSem.  loan  word,  then  Heb. and  Aram,  hazzdn  were  reborrowed  from  Ak¬ kadian.  See  Heinrich  Zimmern,  Akkadische Fremdworter  als  Beweis  fur  babylonischen KultureinfluB,  Leipzig,  1917,  p.6,  Note  3. he,  nom.  sing,  of  the  3rd  pers.  masc.  pron.  — ME.  he,  fr.  OE.  he  [fern,  heo,  hio,  neut.  hit;  pi. (for  all  genders)  hi,  hie],  rel.  to  OS.,  OFris.  he, hi,  MDu.  he,  hi,  Du.  hij,  OHG.  he,  ‘he’,  Goth, neut.  hita  (acc.),  ‘it’,  masc.  himma  (dat.)  (in himma  daga,  ‘on  this  day’),  masc.  hina  (acc.) (in  und  hina  daga,  ‘until  that  day’),  and  to  the first  element  in  OE.  heodxg,  OS.  hiudu,  OFris. hiude,  MDu.  huden,  OHG.  hiutu,  MHG.  hiute, G.  heute,  ‘today’  (for  the  second  element,  which appears  in  its  full  form  only  in  OE.  hlo-dxg, see  day);  fr.  Teut.  base  *hi-,  corresponding  to
19960:Ishtar,  n.,  the  chief  goddess  of  the  Assyrians  and Babylonians,  the  counterpart  of  the  Phoenician Astarte.  —  Akkad.  Ishtar.  See  Ashtoreth.
21573:Leucothoe,  n.,  the  daughter  of  Orchamus,  king  of Babylon;  said  to  have  been  changed  by  Apollo into  a  shrub  (Greek  and  Roman  mythol.)  —  L.
24394:Derivatives:  mordant,  n.,  mordant-ly,  adv. Mordecai,  masc.  PN. ;  in  the  Bible,  the  cousin  of Esther,  who  saved  the  Jews  from  the  extermina¬ tion  planned  by  Haman.  —  Fleb.  Mortfkhay, spelled  also  Mordokhay,  fr.  Akkad.  Marduk (whence  Heb.  M^rodhakh,  name  of  the  chief god  of  the  city  of  Babylon,  whence  also  the Babylonian  PN’s  Mardukea,  Marduka. mordenite,  n.,  a  zeolite  (mineral.)  —  Named  after Morden  in  Nova  Scotia.  For  the  ending  see subst.  suff.  -ite.
24952:naphtha,  n.,  an  inflammable  liquid  distilled  from petroleum.  —  L.,  fr.  Gk.  vaiyffx,  fr.  Aram. naphta,  nephtd  (whence  also  Arab,  naft,  Pers. neft),  fr.  Akkad,  naptu,  ‘naphtha’.  See  Heinrich Zimmern,  Akkadische  Fremdworter  als  Beweis fiir  babylonischen  KultureinfluB,  2nd  edition, Leipzig,  1917,  p.  60.
25093:Nebuchadnezzar,  Nebuchadrezzar,  n.,  king  of Babylon  (604-562  B.C.E.).  —  Heb.  N^bhukhadh- netztzdr,  acollateral  (oimo(Nebhiikhadhretztzdr, fr.  Bab.  Nabu-kudurri-usur,  which  prob.  means lit.  ‘Nebo,  protect  the  boundary’.  Cp.  Gk.  Na- poxoSpooopo;  in  Strabo  15,1,6,  and  in  Josephus Flavius,  Contra  Apionem  1,146. nebula,  n.,  a  cloudlike  patch  in  the  sky  (astron.) —  L.,  ‘mist,  fog,  cloud’,  fr.  I.-E.  base  *(e)nebh-, ‘moist,  vapor,  mist,  cloud’,  whence'  also  OI. ndbhas-,  ‘vapor,  cloud,  fog,  sky’,  Avestic  nabah -, ‘air,  sky’,  Gk.  veipo?,  vcfpeXz],  ‘cloud,  mist’,  OS. nebal,  OFris.  nevil,  MDu.,  Du.  novel,  OHG. nebul,  MHG.,  G.  nebel,  ‘fog’,  ON.  nifl-  (in Niflheimr,  ‘abode  of  darkness’,  i.e.  ‘the  nether world’),  njol,  ‘night’,  OE.  nifol  (adj.),  ‘dark’, MW.  nyfel,  ‘cloud’,  W.  ttiwl,  Co.  niul,  ‘cloud, fog’,  OIr.  nem,  ‘sky’,  OSlav.  nebo  (gen.  nebese), ‘sky’,  Lith.  debesls  (for  *nebesis ),  ‘cloud’  (the d-  is  prob.  due  to  the  influence  of  dangits, ‘sky’),  Hitt,  nepish  (gen.  nepishash),  ‘sky’,  Aves¬ tic  napla-,  ‘moist,  humid’.  Cp.  nepheline,  nepho-, Neptune,  Nibelungs,  nimbus,  imbricate. Derivatives:  nebul-ar,  adj.,  nebul-iz-ation,  n., nebul-ize,  tr.  v.,  nebul-iz-er,  n.,  nebulous  (q.v.) nebulosity,  n.,  1)  condition  of  being  nebulous;  2) cloudiness;  3)  a  nebula.  —  F.  nebulosite,  fr. Late  L.  nebulositatem ,  acc.  of  nebuldsitas,  fr.  L. nebulosus.  See  nebulous  and  -ity. nebulous,  adj.,  1)  resembling  a  nebula ;  2)  clouded, cloudy,  misty;  3)  vague  —  L.  nebulosus,  ‘cloudy’, fr.  nebula.  See  nebula  and  -ous.
29773:postero-,  combining  form  meaning  ‘posterior and’.  —  Fr.  L.  posterus,  ‘coming  after’,  fr.  post, ‘after’.  See  post-,  posterior, postexilian,  adj.,  pertaining  to  the  time  subse¬ quent  to  the  Babylonian  captivity.  —  Formed fr.  pref.  post-,  L.  exilium  (see  exile)  and  suff.  -an. postexilic,  adj.,  postexilian.  —  See  prec.  word  and -ic.
30019:preen,  tr.  v.,  to  trim,  dress.  —  A  blend  of  ME. proynen,  ‘to  trim  the  feathers’  (see  prune,  ‘to preen'),  and  ME.  prenen,  ‘to  fasten’,  fr.  OE. preon,  ‘pin,  brooch'.  See  preen,  n. pre-exilian,  adj.,  prior  to  the  Babylonian  cap¬ tivity.  —  Formed  fr.  L.  prae  (see  pre-),  exilium, ‘exile’  (see  exile),  and  suff.  -ian. pre-exilic,  adj.,  pre-exilian.  —  See  prec.  word and  adj.  suff.  -ic.
31499:Rabmag,  n.,  title  of  a  Babylonian  official  men¬ tioned  in  Jer.  39 :  3.  —  Heb.  rabh-magh,  fr. Akkad,  rab  mugi,  title  of  an  official.  For  Akkad. rab  see  rabbi  and  cp.  the  first  element  in  next
32664:‘he  saw',  and  ben,  ‘a  son’ ;  cp.  Babylonian  Tal¬ mud,  tractate  Berakhoth,  7b.  —  Heb.  ra  d  is rel.  to  Arab,  ra'a,  Ethiop.  rd'a,  ‘he  saw  ,  Aram. rew,  rewa ,  ‘appearance’.  For  the  etymology  of ben,  ‘son’,  see  ben.
34872:Shamash,  n.,  the  chief  sun  god  of  Assyria  and Babylon.  —  Akkad,  shamash,  shamshu,  ‘sun; the  god  of  the  sun’,  rel.  to  Heb.  shemesh,  ‘sun’, Aram.shimsha,  Syr.  shemshd,Vgar.  sh-p-sh,  Arab. shams  (dissimilated  fr.  *shamsh),  of  s.m.;  prob. from  the  Semitic  base  s-m-s-m,  ‘to  be  swift’  (said of  the  quivering  sunrays).  Aram,  shumshdna, Arab,  sumsum,  Aram.  shumsh6mdna  (whence through  syncope  shumshdna,  whence  through metathesis  shushmana),  ‘ant ,  are  of  the  same base.  See  Fleischer,  Beitrage  zu  Jacob  Levy’s Worterbuch  iiber  die  Targumim,  II,  pp.  577f. Cp.  Samson.
37432:(fig.)  —  L.  sumen,  ‘breast  of  women,  a  sow’s udder’,  for  *sugs-men,  fr.  siigo,  siigere,  ‘to  suck’. See  sugent.  For  the  ending  see  suff.  -men. Sumer,  n.,  an  ancient  district  of  Babylonia. Sumerian,  adj.,  1)  pertaining  to  Sumer;  2)  per¬ taining  to  the  inhabitants  of  Sumer,  their  lan¬ guage  or  civilization ;  n. ,  an  inhabitant  of  Sumer. —  Formed  fr.  Sumer  with  suff.  -ian. summary,  adj.,  brief.  —  ML.  summarius,  an  adj. formed  from  the  Latin  noun  summdrium.  See next  word.
38108:Tammuz,  n.,  1)  a  Babylonian  and  Assyrian  god; 2)  name  of  the  fourth  Jewish  month.  —  Heb. Tammuz,  fr.  Babyl.  Du’iizu,  Duzu,  contraction of  original  Dumu-zi,  ‘the  son  who  rises’,  also interpreted  as  ‘the  faithful  son’, tammy,  n.,  a  fine  woolen  fabric.  —  Fr.  obsol. tamin,  fr.  F.  etamine,  fr.  OF.  estamine,  formed — with  change  of  suff. — fr.  VL.  staminea, prop.  fern,  of  the  L.  adj.  stamineus,  ‘made  of threads',  fr.  L.  stamen,  gen.  staminis,  ‘thread; warp’.  Cp.  It.  stamigna,  OProven?.  estamenha, Sp.  estameha,  ‘a  kind  of  woolen  fabric’,  and see  stamen.
38267:Tashmitum,  n.,  a  Babylonian  goddess,  the  wife  of Nebo.  —  Akkad.  Tashmitum,  lit.  ‘proclaimer’, fr.  tashmitum,  ‘a  hearing’,  fr.  shemu,  ‘to  hear’, which  is  rel.  to  Heb.  shama\  ‘he  heard’.  See Shema.
39665:Tosaphoth,  n.  pi.,  explanatory  and  critical  glosses on  the  Babylonian  Talmud  (Hebrew  literature).
```


## [2026-09-07T18:18:26.103Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK nas ===\"; grep -n -E \"^nas-|nas-\\b|nāsā|nas- .nase\" POK_full.txt 2>/dev/null | head -20; ls | grep -i pok"
}
```


### [2026-09-07T18:18:26.165Z] TOOL RESULT

```
=== POK nas ===
18490:Aesma, sends to attack ' (very doubtful Old Indie dravina-m, dravinas-v\. "blessing, 
44443:(Old Indie canistam; Old Indie canas-n. ' pleasure, satisfaction', Avestan canah-, cinah- 
54586:"unproductive', atireka-m. " remnant, leftover item ', reknas-v\. " inherited possession, 
61837:Old Indie nas-a, -f, -6h\v\s\x. Lok. Sg., Gen. Du.; nasaHom. Du. "nose' (originally " nostril 
61839:'), secondary nasai. "nose', nas-tah Mn . "of the nose', nasya-^ located at the nose ', etc., 
64031:(verrichtend)'; apas-n. "work, religious action'; apnas-n. "yield, property, possession ', 
71560:grausigem face (with the eyes and mouth)' (to *avoq n. 'face' = Old Indie *anas-n. 6s., 
85687:"sinew, straff angezogenes Band' (= Latin tenus, -oris, compare also Old Indie tanas-v\.), 
90933:"wish'; vanas-n. "lust' (compare Latin Venus), vani-i. "desire, wish', wherefore vanTyati 
POK_01.txt
POK_02.txt
POK_03.txt
POK_full.txt
```


## [2026-09-07T18:18:33.578Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('POK_full.txt',encoding='utf-8',errors='replace').read().split('\\n')\nprint(len(t))\n# find page markers\nfor i,l in enumerate(t[:200]):\n    if re.search(r'\\[?page',l,re.I): print(i,l[:120])\nEOF\necho \"--- context around nas ---\"\nsed -n '61820,61860p' POK_full.txt"
}
```


## [2026-09-07T18:18:34.777Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -E \"^\\s*\\[?(pdf )?page [0-9]+\\]?|^\\s*[0-9]{1,4}\\s*$\" KLN_1966.txt | sed -n '1,10p'\necho \"=== nearby markers around 4216 ===\"\nsed -n '4200,4220p' KLN_1966.txt | cut -c1-200"
}
```


### [2026-09-07T18:18:35.095Z] TOOL RESULT

```
93772
--- context around nas ---

originally probably " nostril ' 

Note: 

Root/ lemma: nas-: nose' derived from Root/ lemma: neu-ks-, neu-s-\ "to sniff, smell' 

which derived from zero grade of Root/ lemma: an(a)-3\ "to breathe' : Root/ lemma: 

ansu-, QSU-\ "ghost, demon': Old Indie asu-, Avestan arjhu-^ breath of life, world '. 

Material: 

Maybe through metathesis alb. Geg {*u-nah) huna, Tosc hundat " nose' from alb. hundof 

insult, make sad ' (common Baltic Slavic Albanian prefix u-). 

Old Indie nas-a, -f, -6h\v\s\x. Lok. Sg., Gen. Du.; nasaHom. Du. "nose' (originally " nostril 

'), secondary nasai. "nose', nas-tah Mn . "of the nose', nasya-^ located at the nose ', etc., 

nasika^ nostril, nose'; Avestan nah-, narjhan-^ v\ose\ ap. naham kVk. Sg. (= Latin narem) 

"nose'; Latin nan's, mostly. PI. -es, -ium^ nostril ' (/-stem has changed to; Akk. Sg. PI. still 

conservative form); nasumn. (Old Latin) and nasfsjusm. "nose' (expressives ss); 

[common Latin Germanic -s- > -/"-]. 

Old English noset " foreland, promontory ', Old Swedish Norwegian /7ds "snout'. Old 

Frisian nds/6s. {*nas-); ablaut. Old High German nasa^nose'. Old Norse ngsi. " nostril, 

nose, projecting cliff'. Old English nasu^nose' (presumably Dual " both nostrils '); nces-\n 

compound. Old Norse nesn.. Gen. PI. nesja^ foreland, promontory, tongue of land ', 

Middle Low German nes{-ss-) m. ds.. Old English nsessm. ds. (Germanic *nasja-); Old 

Prussian nozy, Lithuanian nos/st "nose', nasraTxw. PI. " jaw ' (old /7as/'5S "mouth'). Old
```


### [2026-09-07T18:18:36.587Z] TOOL RESULT

```
10:1966
108:3
120:1
124:1
128:1
137:1
158:1
163:1
177:1
185:37
=== nearby markers around 4216 ===
azotea,  n.,  a  flat  roof.  —  Sp.,  fr.  Arab,  as-sath, lit.  ‘the  roof’,  fr.  as-,  assimilated  form  of  a!-, ‘the’,  and  sath,  ‘roof’,  fr.  sataha,  ‘he  spread  out’,
|
I
which  is  rel.  to  Heb.  shajah,  Aram.-Syr.  shetah, ‘he  spread  out’.
azotite,  n.,  salt  of  nitrous  acid  ( chem .)  —  Formed fr.  azote  with  subst.  suff.  -ite. azulene,  n.,  blue  hydrocarbon  (chem.)  —  Formed with  suff.  -ene  fr.  Sp.  azul,  ‘blue
azurite,  n.,  hydrous  carbonate  of  copper  (min¬ eral.)  —  Formed  fr.  azure  with  subst.  suff.  -ite; so  called  from  its  color.
azygo-,  combining  formmeaning  ‘azygous’  Gk.
a^uyo-,  fr.  SZuyoq.  See  azygous, azygous,  adj.,  odd.  —  Gk.  &X,\>yoc„  ‘odd.  not forming  a  pair’,  fr.  a-  (see  priv.  pref.  a-)  and £oy6v,  ‘yoke’.  See  zygo-,  yoke.  Fo
Derivatives:  azym-ic,  azym-ous,  adjs.
13?
oacienum
t
B
baa,  intr.  v.,  to  bleat.  —  Imitative  of  the  cry  of the  sheep.
Derivative :  baa,  n.
Baal,  n.,  the  name  of  many  deities  of  the  Semitic peoples.  —  Heb.  Ba‘al  (pi.  Bl'altm),  lit.  ‘owner, master,  lord’,  fr.  ba'dl,  ‘he  took  possession  of, he  married’,  
Bab,  n.,  title  given  to  the  founder  of  Babism.  — Pers.  bdb,  ‘door,  gate’,  fr.  Arab,  bdb,  of  s.m., fr.  Aram,  babh,  babhd,  fr.  Akkad,  babu,  ‘door, gate’,  which  is  sh
Derivatives:  Bab-ism ,  n.,  Bab-ist,  n. babacoote,  n.,  a  Madagascan  lemur  ( zoo! .)  — Malagasy.
Babbitt,  babbitt,  n.,  a  conventional  businessman.
—  So  called  after  George  Babbitt,  the  title character  of  a  novel  by  Sinclair  Lewis  (1922). Derivative:  Babbit-ry,  babbit-ry,  n.
Babbitt  metal.  —  Named  after  its  inventor  Isaac Babbitt  (1799-1862).
```


## [2026-09-07T18:18:51.502Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN page markers near 24983 ===\"\nawk 'NR>=24880 && NR<=25000 && /^[[:space:]]*[0-9]{3,4}[[:space:]]*$/ {print NR\": \"$0}' KLN_1966.txt\necho \"=== KLN markers near 4216 ===\"\nawk 'NR>=4100 && NR<=4260 && /^[[:space:]]*[0-9]{2,4}[?]?[[:space:]]*$/ {print NR\": \"$0}' KLN_1966.txt\necho \"=== AKD p30 area: babu/nebaba ===\"\ngrep -n -i -E \"nebāb|nebab|imbūb|imbub|bāb-il|bab-il|Babilu\" AKD.txt | head -20\necho \"=== KNT nose ===\"\ngrep -n -i -E \"n[āa]ham|'nose'|nose\" KNT.txt | head -20"
}
```


### [2026-09-07T18:18:52.903Z] TOOL RESULT

```
=== KLN page markers near 24983 ===
=== KLN markers near 4216 ===
4209: 13?
=== AKD p30 area: babu/nebaba ===
=== KNT nose ===
1381:$110. PIE n remained n, in general, in OP, Av., Skt., ОК, Lt. pIE *nás- ‘nose’, OP acc. палат, Skt. nàs-, Eng. nose. pIE "nepót-s ‘grandson’, OP nom. napa, Skt. nápál, Lt. nepós.
1623:-daha, naham, атуйћа bagaha, dvahanam, Giira-
1774:йр- ‘water’, zíap- ‘night’, xfnau- in u-zfnau- ‘well satisfied’, gau- ‘cow’ in compounds, bard- ‘year’, dwar- ‘door’ in duvara-, nar- ‘man’ in üv-nara-, nàv- ‘ship’, паћ- ‘nose’, pad- ‘foot’ in nipadiy etc., vas- ‘wish’ in adv. vasiy, vib- ‘house’, séd- in upa-stá- ‘aid’, zam- ‘earth’ in u- zma- etc.; perhaps napdl- ‘grandson’, an old pIE word, probably a compound; possibly dà- in ‘wada- as element of Paisiyà-uvüdà-, and vaj- in gen. daha-vaja. $143. Noun AND ApjectivE STEMS WITH THE-
2199:IV. The remaining -s- stems of OP are ndh- ‘nose’, tauviyah- ‘stronger’, A*uramazdah- ‘Ahura- mazda’, and possibly mah- ‘month’.
3680:Thereafter I sent an army in pursuit; Phraortes, seized, was led to me. I cut off his nose and ears and tongue, and put out one eye; he was kept bound at my palace entrance, all the people saw him. Afterward I impaled him at Ecbatana; and the men who were his foremost followers, those at
3685:“Go forth; the hostile army which shall not call itself mine, that do ye smite!” Thereupon Takh- maspada with the army went off; he joined battle with Cigantakhma. Ahuramazda bore me aid; by the favor of Ahuramazda my army smote that rebellious army and took Cicantakhma prisoner, (and) led him to me. Afterwards I cut off his ears and nose and tongue, and put out one eye; he he was kept bound at my palace entrance, all the people saw him. Afterwards I impaled him at Arbela.
5605:nàh- sb. ‘nose’: Av. nàh-, Skt. nds-, Lt. narés, NEng. nose, pIE *nds- (5110, $142).  náham asm. (81181, §185.1V) DB 2.74, 88f.
```


## [2026-09-07T18:18:53.881Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PLA files ===\"; ls incoming/PLA 2>/dev/null; ls | grep -i pla\necho \"=== AHD watkins nas ===\"; grep -n -E \"^nas-|nas-\\s\" AHD_watkins1985.txt | head -20\necho \"=== BRT nah ===\"; grep -n -E \"nāh|narjhan|naṅhan|nanhan\" BRT.txt | head -20"
}
```


### [2026-09-07T18:18:53.960Z] TOOL RESULT

```
=== PLA files ===
PLA_asbaghi_1988_ia_djvu.txt
PLA_asbaghi_1988_ia.pdf
PLA_pages.txt
=== AHD watkins nas ===
697:leug-2. To break. Suffixed form *Jeug-é- in Latin ligére, to mourn (? < “to break down mentally”): LUGUBRIOUS. [Pok. leug- 686.] leugh-. To tell a lie. 1. Germanic *leugan in: a. Old English /Zogan, to lie: WARLOCK; b. Old English beléog- an, to tell lies about (be-, about; see ambhi): BELIE. 2. Germanic */ugiz in Old English lyge, a lie, falsehood: LIE’. [Pok. leugh- 686.] leuk-. Light, brightness. I. Basic form */euk-. 1. Suffixed form *leuk-to- in Germanic */euhtam in Old English léoht, liht, light: LicHT). 2. Latin lix, light: Lucrna, LUCULENT, LUX; LUCIFER, LUCIFERIN. 3. Suffixed form *leuk-smen- in Latin limen, light, opening: LIMN, LU- MEN, LUMINARY, LUMINOUS; ILLUMINATE, PHILLUMEN- 1st. 4. Suffixed form *leuk-snd- in Latin lina, moon: LUNA, LUNAR, LUNATE, LUNATIC, LUNE, LUNULA; DEMI- LUNE, SUBLUNARY. 5. Suffixed form */euk-stro- in: a. Latin listrum, purification: LUSTER, (LUSTRUM); b. Latin lastrdre, to purify, illuminate: ILLUSTRATE. 6. Suffixed form *leuko-dhro- in Latin licubrdre, to work by lamplight: LUCUBRATE. II. O-grade form *louk-. 1. Suffixed form *louk-o- in Germanic *lauhaz in Old English /éah, meadow (< “place where light shines”): LEA. 2. Suffixed (iterative) form *lowk-eyo- in Latin liicére, to shine (> licidus, shining): LUCENT, LUCID; ELUCIDATE, NOCTILUCA, PELLUCID, RELUCENT, TRANS- LUCENT. III. Zero-grade form *luk-. 1. Suffixed form *luk-sno- in Greek lukhnos, lamp: LINK?, LYCHNIS. 2. At- tributed by some to this root (but more likely of obscure origin) is Greek lunx, lynx (as if from its shining eyes): LYNX, OUNCE? [Pok. leuk- 687.] leup-. To peel off, break off. 1. Germanic *laubaz in Old English Jéaf, leaf: LEAF. 2. Germanic *laubja, “roof made from bark,” shelter, in: a. Old French loge, lodge: LODGE, (LOGE); b. Medieval Latin lobium, lobia, laubia, monas- tic cloister: LOBBY. 3. Attributed by some to this root is Germanic */uftuz, sky (traditionally explained as < “roof of the world,” vault of heaven), but probably a separate Germanic root, in: a. Old Norse opt, air, attic, sky: LOFT; ALOFT; b. Germanic */uftjan, to hold up in the air, in Old Norse /ypta, to lift: Lirt. [Pok. leup- 690.]
770:nas-. Nose. 1. Germanic zero-grade form *nusé in Old English nosu, nose: NOSE, (NUZZLE); NOSTRIL. 2. Ger- manic nasja- in Old English ness, headland: NESS. 3. Lengthened-grade form “nds-, in: a. Latin ndris, nos- tril: NAREs; b. expressive form *ndss- in Latin ndsus, nose: NASAL, NASO-; NASTURTIUM, PINCE-NEZ. 4. Expres- sive Indo-Aryan form *nakka- in Romany nak, nose: NARK?. [Pok. nas- 755, neu-ks 768.]
1900:NACELLE nau-2 NAG! ghen- NAIAD (s)nau- NAIL nogh- NAINSOOK nele- NAIVE gene- NAKED nogW- NAME no-men- NANA nana NANNY nana NANO- nana NAP] ken-2 NAP2 ken-2 NAPERY mappa NAPKIN mappa NAPPE mappa NARCO- (s)ner- NARCOSIS (s)ner- NARCOTIC (s)ner- NARES nas- NARK? nas- NARRATE gnoé- NARROW (s)ner- NARWAL (s)kWal-o- NARWHAL nau-! NASAL nas- NASCENT gene- NASO- nas-
1946:NUNCIO neu-1 NUNCUPATIVE kap-, nd-men- NUPTIAL sneubh- NURSE (s)nau- NURTURE (S)nau- NnuT ken-5 NUTATION neu-2 NUTHATCH skep- NUTRIA wed-1 NUTRIENT (s)nau- NUTRIMENT (s)nau- NUTRITION (s)nau- NUTRITIOUS (s)nau- NUTRITIVE (s)nau- NUX VOMICA weme- NUZZLE nas- NYCTALOPIA nekw-t-, okw- NYCTITROPISM nekw-t- NYMPH sneubh- NYMPHOLEPT (s)lag¥- NYSTAGMOUS sneud(h)-
2093:PILUS _pilo- PIMENTO peig-1 PIMPERNEL pippali PINA peio- PINCE-NEZ nas- PINE! peie-
=== BRT nah ===
6039:^ä'sina'  m.,  Sva.  sainak',  vgl.  taenahvanl'^  — 1)  Tahmüraf  führt  später  den  Beinamen  zinä- vand  (so  bei  richtiger  Punktitung,  d.  i.  mp. tenäiiand,  womit  lainanhan-  übersetzt  wird), dervolkseL  an  Eni'WalTe' angeschlossen  wurde: an  ki  siläk  i  lamäm  dörad.  Vgl  Windisch- MANN  ZStI  197.  Sf.  Komm.  2. 635,  EA.  /.  518, JusTi  NB.  320.
19100:.  j.  nanhan-  m.  'Nase'  des  Menschen:!  ..^- ^^.^„^„  ^^,^  .,,■  „,.^^_^^^„  ,.
```


## [2026-09-07T18:19:05.147Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KNT page markers near 5605 ===\"\nawk 'NR>=5500 && NR<=5650 && /page|^\\s*1[0-9]{2}\\s*$/ {print NR\": \"substr($0,1,100)}' KNT.txt | head\ngrep -c \"\" KNT.txt\necho \"=== KNT.txt has pdf page tags? ===\"\ngrep -n \"pdf page\" KNT.txt | head -3\nls | grep -i KNT"
}
```


### [2026-09-07T18:19:06.637Z] TOOL RESULT

```
=== KNT page markers near 5605 ===
5518: 189
5556: 191
5598: 193
5869
=== KNT.txt has pdf page tags? ===
KNT.txt
```


## [2026-09-07T18:19:07.243Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PLA narjil ===\"\ngrep -n \"نارجيل\\|نارگيل\\|nārgīl\\|narǧīl\\|narjil\" PLA_pages.txt | head -20\necho \"=== AKD structure ===\"\nhead -20 AKD.txt | cut -c1-150\necho \"=== AKD grep bab ===\"\ngrep -n -E \"b[aā]bu|Babel|Tür|Tor\" AKD.txt | head -20"
}
```


### [2026-09-07T18:19:07.315Z] TOOL RESULT

```
=== PLA narjil ===
ugrep: warning: PLA_pages.txt: No such file or directory
=== AKD structure ===
r
=  00
00
Ziiamern,  Heinrich
Akkadische  Fremdwörter  als Beweis  für  babylonischen  Kulture- influss
EX  ORDINIS  PHILOSOPHORUM  MANDATO
RENUNTIANTÜR
PHILOSOPHIAE  DOCTORES
ET
ARTIUM  LIBERALIUM  MAGISTRI
EECTOEE  MAGNinCO
OTTONE  MAYER
lüEIS    UTEIDSQITE    DOCTORE       IURIS    PUBLICI    PROFESSORE    P.  O.
DBCANO
HENRICO  ZIMMERN
PHILOSOPHIAE    DOCTORE      LIMIUARÜM   ORIENTALItlM   PBOFESSORE   P.  0.
PROCANCELLARIO
GUILELMO  KIRCHNER
PHILOSOPHIAE   DOCTORE      AGRICULTÜRAE   PROFESSORE   P.  0.
INDE  A  DIE  PRIMO   MENSIS  NOVEMBRIS  A.  MDCCCCXIJI   ÜSQUE  AD  DIEM ULTIMUM  MENSIS  OCTOBRIS  A.  MDCCCCXIV  CREATI.
=== AKD grep bab ===
148:akk.  kababii,  auch  gababu  geschr.,  Schild  :  >  vieU.  hebr.  st.  c.  PI. gabbe  Hi.  15,26.
406:akk.  bfihu  Tor  :  >  aram.  hlM  (>  arab.  höh  u.  viell.  späthebr.  hah Ps.  90,12).  akk.  daltu,  st.  c.  dalat  Türflügel,  Tür  (vieU.  von  edelu
407:verriegeln)  :  >  viell.,  dann  freilich  sehr  früh,  hebr.  dälet,  dalt-,  auch dal,  phöu.  dl  oder  dl[t]  und  im  Buclistabenn.  /idKra,  sowie  wohl  auch  in Si).Tog  Sclireibtafel.  Aus  einem  spätbabyl.  *daf<tu  für  daltu  vieU.  >  jüd.- aram.  (auch  ägypt.-aram.)  dasSa  Türflügel.  akk.  cdiltu  Tür  (eig.  die
408:Yerriegelnde)   :  >■  viell.   syr.  PL   'edlätä,   'üdlrtta  Türflügel.  akk.
409:sirru  Tür  Zapfenloch  (viell.  ■<  sum.  sara)  :  >  späthebr.  .s/r,  aram.  t;7rri, mrtä,  sajartri  {sajärtä)  O  arab.  sir).
415:akk.  asl'uppu,  ashippatu  Tür  schwelle  :  >  aram.  "eshiptä,  'iskujdd (^  arab.  'usltiffat).  —  In  älterer  Zeit  wohl  aucli  aus  akk.  aslmppu  bezw. sakkapu  ^  hebr.  niasqöp  Oberschwelle,  Säqep.  &dqüplm  Tür-  bezw.  Fenster- rahmen, akk.  sippu  Schwelle  (viell.  <^  sum.  sig,  zib)  :  >  wohl hebr.  sap,  sipp-,  phön.  sp,  aram.  sippä.  akk.  l/iüu  Tragbalken, Türsims  :  >  syr.  kettd.
416:akk.  ammatu  ein  Türteil,  wohl  Türpfosten  od.  ä.  (eig.  wohl  identisch mit  ammatu  Elle)  :  ^  wohl  hebr.  PI.  'aninidt  als  Türteil  Jes.  6,4.  akk.
417:manzazu  Pfosten  (von  naxdzu  stehen)  :  >  (bezw.  aus  i.  manzaztu)  viell. hebr.  maznzd  Türpfosten.
908:[akk.  hilhimütu,  bisher  keilschriftlich   nur  als  aram.   N.  pr.   zu  be- legen :  späthebr.  hallämfä,  syr.  fwlamtä  Ochsenzunge,  Anchusa.]         akk. [lamhasüsii  wohl  Vogelmilch :  arab.  [larlxus-is,  halla-n-s,  aram.  halbtm. akk.  humbaqüqu  eine  Garteupflanze  :  dazu  hebr.  häbaqquq  (LXX  'Afißaxoü/^) Habakuk  als  K  pr.,   u.  vieU.  sj'r.  hariaqäqä  Cassia  Tora.  akk.
916:kasfi  (ideogr.  geschr.  als  „Böcklein"- Kraut)  Cassia  Tora  :  >•  aram. kasjä  dd-türe  ]>  xaala,  Cassia  tora,  dazu  viell,  mit  Übers,  der  ideogr. Schreibung,  x^äyiov.  akk.  ktisibirru  Koriander  :  aram.  kusbar,
936:[akk.  qidqid(l)cltiu  wahrsch.  zu  :  arab.  qiüqul  Cassia  Tora,] akk.  qaqullu  :  aram.  qaqillä  Kardamom.  akk.  qursibtu  :  syr.  qar-
1024:9)  Kislimu,  10)  Tebetu,  11)  Sabätu,  12)  Addaru  :  >>  späthebr.  u.  arani. 1)  Nlsän,  2)  ^Ijjär,  3)  Smän,  4)  Tammüs,  5)  Ab,  6)  'iM,  7)  mn, 8)  Marhes'Wän,  9)  /sTwZm,  10)  Teftci!,  11)  &&äf,  12)  'Ädär,  die  dann  z.T. auch  ins  Syr.-Arab.  und  neuerdings  auch  ins  Türkische  übergegangen sind.  Dazu  auch  noch  der  aram.  (syr.-arab.  und  tiirk.)  Monatsname  Kämm <C  akk.  Kinünu,  Kamlnu  (s.  schon  oben  S.  32  f.).
```


## [2026-09-07T18:19:17.023Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AKD page markers near 406 ===\"\nawk 'NR>=350 && NR<=420 && /^[[:space:]]*[0-9]{1,3}[[:space:]]*$/ {print NR\": \"$0}' AKD.txt\necho \"--- alt: look for 'S. 30' or lines with page nums ---\"\nsed -n '395,412p' AKD.txt | cut -c1-120\necho \"=== PLA narjil ===\"\ngrep -n \"نارجيل\\|نارگيل\\|narǧīl\\|nārgīl\\|narjil\\|Kokos\" PLA_asbaghi_1988_ia_djvu.txt | head -20"
}
```


### [2026-09-07T18:19:18.412Z] TOOL RESULT

```
=== AKD page markers near 406 ===
355:       27      
368:       28      
385:       29      
399:       30      
414:       31      
--- alt: look for 'S. 30' or lines with page nums ---
akk.  samäru  singen  (wohl  auch  zugleich  spielen),  zammeru  Sän- ger :  ]>•  vieU.  hebr.  zimmrr  singen  und 
akk.  nigfitu,  ningütu  (vieU.  von  St.  nagu  klingen  od.  ä.)  Spiel, Musik  :  ^  viell.  hebr.  nägan,  niggcn
akk.  imbftbu  Flöte  :  >  aram.  'abbfibä  (mand.  'ambühä)  Flöte,  Kohr O  wohl  arab.  ""unbrib  Eohr),  sowie
1)  Damit  ist  viell.  urverwandt  akk.  Saratu,  hebr.  sarat,  aram.  sirat,  aiab.  Sarata einschneiden,  eini'itzen
      30      
halhallatu  wahrscli.  Flöte,  halalu  flöten  :  davon  wohl  beeinflußt  hehr. halil  Flötei.  akk.  tahalu,  tapa
aram.  hihla  (>  arab.  fabl).  [aide,  timhuttu  ein  Musikinstrument,
wahrsch.  ein  Saiteninstrument  (urspr.  wohl  Ring,  Reif)  viell.  <  west- sem.,  s.  oben  S.  20  zu  dem  wohl  d
S.  ferner  zu  weitereu  Bezeichniuigen  von  Handwerken,  Künsten  und sonstigen  Berufstätigkeiten  noch  S.  24  z
6.  Haus  und  Hausgeräte.
akk.  Sakfinu  niederlegen,  niedersetzen,  spez.  auch  vom  Wohnung, Lager  usw.  aufschlagen  :  ^  viell.,  dann  f
akk.  bfihu  Tor  :  >  aram.  hlM  (>  arab.  höh  u.  viell.  späthebr.  hah Ps.  90,12).  akk.  daltu,  st.  c.  da
verriegeln)  :  >  viell.,  dann  freilich  sehr  früh,  hebr.  dälet,  dalt-,  auch dal,  phöu.  dl  oder  dl[t]  un
Yerriegelnde)   :  >■  viell.   syr.  PL   'edlätä,   'üdlrtta  Türflügel.  akk.
sirru  Tür  Zapfenloch  (viell.  ■<  sum.  sara)  :  >  späthebr.  .s/r,  aram.  t;7rri, mrtä,  sajartri  {sajärt�
akk.  sikkiiru  Riegel  :  >  wohl  aram.  sUckdrO,  sukkara;  viell.  aus akk.  sekeru  verstopfen,  versclüießen,  �
unsicher,  ob  >  syr.  maddsla  Riegel,  oder  ob  dies  -<  griech.  fidvSalog  (und dies  viell.  <;  akk.  mcd'du). 
sum.  sigar\  (vgl.  schon  oben  S.  15  zu  sigaru  Käfig,  Hundehalsband)  :  >» viell.  früh  sgr  verschließen,
=== PLA narjil ===
ugrep: warning: PLA_asbaghi_1988_ia_djvu.txt: No such file or directory
```


## [2026-09-07T18:19:19.350Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN markers 24800-25100 (any short numeric) ===\"\nawk 'NR>=24800 && NR<=25100 && /^[[:space:]]*[0-9O!lI?]{2,5}[[:space:]]*$/ {print NR\": \"$0}' KLN_1966.txt\necho \"=== nearby text around 24983 for anchors ===\"\nsed -n '24975,24990p' KLN_1966.txt | cut -c1-160"
}
```


### [2026-09-07T18:19:20.738Z] TOOL RESULT

```
=== KLN markers 24800-25100 (any short numeric) ===
=== nearby text around 24983 for anchors ===
narcoleptic,  adj.,  pertaining  to,  or  affected  with, narcolepsy.  —  Formed  fr.  narcolepsy,  to  which it  stands  as  the  adj.  epileptic  stands  to
narcomania,  n.,  an  abnormal  craving  for  a  nar¬
cotic  drug.  —  Medical  L.,  compounded  of  Gk. vapxY),  ‘numbness’,  and  fj.avf5i,  ‘madness,  fren¬ zy’.  See  narcotic  and  mania.
Derivatives:  narcomani-ac,  n.,  narcomani-ac-al, adj.
narcosis,  n.,  state  of  unconsciousness  caused  by a  narcotic  (med.)  —  Medical  JL.,  fr.  Gk.  vap- x coai.p,  ‘a  benumbing’,  fr.  vapxouv,  �
narcotic,  adj.,  producing  insensibility.  —  F.  nar- cotique,  introduced  into  French  in  1314  by  Mon- deville  fr.  ML.  narcoticus,  fr.  Gk.  vapx
Derivatives:  narcotic,  n.,  narcotic-al-ly,  adv., narcotism  (q.v.),  narcotize  (q.v.) narcotine,  also  narcotin,  n.,  an  alkaloid  found  in opium,  Cjj
nares,  n.  pi.,  the  nostrils  ( anat .)  —  L.  nares,  pi.  of naris,  ‘nostril’,  which  stands  for  *nasis  (see  rho¬ tacism),  fr.  I.-E.  base 
narghile,  nargile,  n.,  hookah,  an  Oriental  pipe.  — Pers.  nargil,  ‘coconut  tree';  prob.  fr.  OI.  ndrike- rah,  ndrikelah,  of  s.m.,  which  is 
I
nark,n.,  spy,  informer,  stool  pigeon  ( British  slang). —  From  Gypsy  nak,  ‘nose’,  fr.  Hind,  nak, ‘nose’,  fr.  OI.  nakrd,  fr.  Prakrit  
Derivative:  narrative-Iy,  adv. narrative,  n.,  a  tale,  story.  —  MF.,  from  the  adj.
narrative,  fern,  of  narratif.  See  narrative,  adj. narrator,  n.,  relater,  narrator.  —  L.  narrator,  fr. narratus,  pp.  of  narrdre.  See  narrate 
narrow,  adj.,  of  small  breadth.  —  ME.  narewe, narwe,  naru,  fr.  OE.  nearu,  rel.  to  OS.  naro, MDu.  nare;  orig.  prob.  meaning  ‘twisted  up,
Derivatives:  narrow,  n.  and  tr.  and  intr.  v., narrow-er,  n.,  narrow-ly,  adv.,  narrow-ness,  n. narthex,  n.,  a  porch  at  the  west  end  of  early
narwhal,  narwal,  n.,  an  arctic  whale  with  a  long spiral  horn.  —  Dan.,  Norw.  narhval,  or  Swed. narval,  metathesized  fr.  ON.  nahvalr,  lit.
```


## [2026-09-07T18:19:39.668Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nls -la incoming/PLA/ 2>/dev/null\necho \"=== find PLA files anywhere ===\"\nfind /home/sfmqrb/git/rishe/data/verification/sources -iname \"*PLA*\" | head\necho \"=== KLN nearest numeric markers around 24983 ===\"\nawk 'NR<=24983 && /^[[:space:]]*[0-9]{2,4}[[:space:]]*$/ {n=NR; v=$0} END{}' KLN_1966.txt\npython3 - <<'EOF'\nimport re\nlines=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\n')\nmarks=[(i,l.strip()) for i,l in enumerate(lines,1) if re.fullmatch(r'\\s*\\d{2,4}\\s*',l)]\nprint(\"total marks\",len(marks))\nbefore=[m for m in marks if m[0]<24983][-5:]\nafter=[m for m in marks if m[0]>24983][:5]\nprint(\"before\",before)\nprint(\"after\",after)\nEOF"
}
```


### [2026-09-07T18:19:41.081Z] TOOL RESULT

```
total 6832
drwxrwxr-x  2 sfmqrb sfmqrb    4096 Sep  4 14:06 .
drwxrwxr-x 23 sfmqrb sfmqrb    4096 Sep  4 14:06 ..
-rw-rw-r--  1 sfmqrb sfmqrb  358695 Sep  4 14:06 PLA_asbaghi_1988_ia_djvu.txt
-rw-rw-r--  1 sfmqrb sfmqrb 5813714 Sep  4 14:06 PLA_asbaghi_1988_ia.pdf
-rw-rw-r--  1 sfmqrb sfmqrb  807821 Sep  4 14:06 PLA_pages.txt
=== find PLA files anywhere ===
/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA
/home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/PLA
/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf
/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt
/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt
=== KLN nearest numeric markers around 24983 ===
total marks 1114
before [(24689, '1016'), (24690, '1017'), (24786, '1021'), (24831, '1022'), (24960, '1028')]
after [(25059, '1033'), (25092, '1035'), (25130, '1036'), (25195, '1039'), (25234, '1040')]
```


## [2026-09-07T18:19:46.154Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA\ngrep -n \"نارجيل\\|نارگيل\\|narǧīl\\|nārgīl\\|narjil\\|Kokos\\|anārgēl\" PLA_pages.txt | head -20\necho \"=== page 256 tag ===\"\ngrep -n \"pdf page\" PLA_pages.txt | head -3"
}
```


### [2026-09-07T18:19:46.241Z] TOOL RESULT

```
2282:eb - bädanf:                         "Kokosnuß"           pers.      11,          barang            .
2889:27             baran&:             "Kokosnuß"                   aus     dem       pers.     „v_,L          bädrang          100       mp. »Pyyı         vatrang
3742:IN,S-        bürank:                '"Kokosnuß"                 pers.     a    aus       dem    pers,            a          bädrang MP               adert.
7572:ze) -           ränif:          "Nuß,        Kokosnuß"              pers.        8,       nargil.
14376:snb         - nargil:           "Kokosnuß"             _        Pers.    Br            närgil           I       mp. Ye y anärgil
=== page 256 tag ===
```


## [2026-09-07T18:19:52.651Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA\nsed -n '14360,14395p' PLA_pages.txt | cut -c1-200\necho \"=== page markers near ===\"\npython3 - <<'EOF'\nimport re\nlines=open('PLA_pages.txt',encoding='utf-8',errors='replace').read().split('\\n')\npat=re.compile(r'^\\s*(\\d{1,3})\\s*$')\nmarks=[(i,m.group(1)) for i,l in enumerate(lines,1) if (m:=pat.match(l))]\nprint(len(marks))\nprint([m for m in marks if 14200<m[0]<14600])\nEOF"
}
```


### [2026-09-07T18:19:53.945Z] TOOL RESULT

```
lab _        nähudä:           "Schiffskapitänt                         pers.           sb naw          "Schiff"       e<     mp. sp
       nautak        "schiffbar"              "<e.                nau,        adj.      naviya,            lat.    navis,     griech.
       vays     +    Isa hudä           "Herr,         Gott"       T     mp.           er        xMatäi.


I3>L - nähugä = näbuda q. v.

Sea - na’hag:              "See"        pers.       82.


zb       - närbäg:              "Granatapfeleintopf"                          aus      pers.            LU   närba I’ <m.           y
       anar

                                                                              X                   _                                 _
snb         - nargil:           "Kokosnuß"             _        Pers.    Br            närgil           I       mp. Ye y anärgil



 1.    Löw     s.    v.
 2.    ebda.
 3. Addai           Scher       s. v., vgl.            mälaß           v. mälldan-
 4.    Wahrmund           s.    v.
 5.    Bartholomae              S.    1186.
 6.    Addai        Scher       Ss.   v.
 7. Bundahiän              s.    v.
 8.    al-MuCarrab              s.    v.
 9. BQ. s. v., Tafälibi figh al-luga s. v.
 10.    Wahrmund           s.     v.,      BO.    s.    v.
nardila                                                                         257                                                               nänha


ala,L            -    närgila:              "pers.            Wasserpfeife"              ı     skr.          narikera,        engl.          nargula,
       frz.           narguile.                  Nargileh          —      skr. >        pers.         > tk.         >    dtsch.        1

=== page markers near ===
154
[(14587, '13')]
```


## [2026-09-07T18:20:35.229Z] TOOL CALL #20: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-07T18:20:35.237Z] TOOL RESULT

```


```


## [2026-09-07T18:20:36.648Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON باب / انبوب / نارگیل ===\"\ngrep -n \"انبوب\\|أنبوب\" MON_part1.txt MON_part2.txt | head -10\necho \"---nargil---\"\ngrep -n \"نارگیل\\|نارگیله\" MON_part1.txt MON_part2.txt | head -10\necho \"=== HJB coco / narghile ===\"\ngrep -n -i -E \"narghile|nargeel|coco-nut|COCO,\" HJB.txt | head -15"
}
```


### [2026-09-07T18:20:36.750Z] TOOL RESULT

```
=== MON باب / انبوب / نارگیل ===
---nargil---
MON_part1.txt:69182:درون‌بر موه نارگیل گیرند و جزو 
MON_part2.txt:22629:کره نارگیل: روغن نارگیل که از درون بر 
MON_part2.txt:22630:میوٌ نارگیل بدست آید؛ روغن نارگیل. 
MON_part2.txt:23609:میوة گونه‌ای نارگیل که درویشان بدان 
MON_part2.txt:23623:روی شکل میوهة این گونه نارگیل 
MON_part2.txt:40943:لوز نارگیل: حلوایی است. طرز تهیه: پوست 
MON_part2.txt:40944:سیاه نارگیل را گرفته با کمی قند می‌کوبند تا 
MON_part2.txt:71754:نارگیل: او [- معر. نارجیل] (.) (گیا.) 
MON_part2.txt:71761:میوة نارگیل که به بازار عرضه می‌شود 
MON_part2.txt:71772:مایعی بنام آب نارگیل که بی‌رنگ است 
=== HJB coco / narghile ===
2716:c.  1760.—"  There  is  also  on  the  island  kept up  a  sort  of  militia,  composed  of  the  land- tillers,  and  bandarees,  whose  living  depends chiefly  on  the  cultivation  of  the  coco-nut trees."— G^/wc,  i.  46.
3475:1615.— "He  sent  for  Coco-Nuts  to  give the  Company,  himselfe  chewing  Bittle  and lime  of  Oyster-shels,  with  a  Kemell  of  Nut called  Arracca^  like  an  Akome,  it  bites  in the  mouth,  accords  rheume,  cooles  the  head, strengthens  the  teeth,  k  is  all  their Phisicke."— iStr  T.  Roe,  in  Purchas,  i.  587 ; [with  some  trifling  variations  in  Foster*t  ed. (Hak.  Soc.)  i.  19].
6822:228       COCO,  COCOA,  COCOA-NUT,
6835:coco,  COCOA,  COCOA-NUT.      229
6875:It  will  be  seen  that  the  Maldive name  of  this  fruit  was  TdvorlcdrhA, The  latter  word  is  *  coco-nut,'  but  the meaninff  of  ^«a  does  not  &ppc&r  from any  Maldive  vocabulary.  [The  term  is properly  Tdva'karhiy  *the  nard-shelled nut,'  ^drayy  on  Pyrard  de  Lavaly  Hak. Soc.  i.  231).]  Rumphius  states  that a  book  in  4to  {totwm  optiscxUwn)  was published  on  this  nut,  at  Amsterdam in  1634,  by  Augerius  Clutius,  M.D. rin  more  recent  times  the  nut  has become  famous  as  the  subject  of  curious speculations  regarding  it  by  the  late Gen.  Gtordon.]
6881:4inother  kind  of  these  trees,  which  gives  a fruit  bigger  than  the  coco-nut ;  and  ex^ri- ence  shows  that  the  inner  husk  of  this  is much  more  efficacious  against  poison  than the  Bezoar  stone."— 5arroa,  III.  iii.  7.
6936:COnt,  8.  The  fibre  of  the  coco-nut husk,  from  which  rope  is  made.  But properly  the  word,  which  is  Tarn. Kayiru,  Malayal.  kdyar,  from  v.  kdydru, *to  be  twisted,*  means  *cord'  itself (see  the  accurate  Al-BirUni  below). The  former  use  among  Europeans  is- very  early.  And  both  the  fiore  and the  rope  made  from  it  appear  to  have been  exported  to  Europe  in  the  middle of  the  16th  century.  The  word  appears in  early  Arabic  writers  in  the  forms kdnbar  and  Jbanbdr,  arising  probably from  some  misreading  of  the  diacritical points  (for  Jhdiyar,  and  Jbaiydr),  The Portuguese  adopted  the  word  in  the form  Cairo,  The  form  coir  seems  to have  been  introduced  by  the  En^ish in  the  18th  century.  [The  N.E.D. gives  coire  in  1697  ;  coir  in  1779.]  It was  less  likely  to  be  used  by  the  Portu- guese because  coiro  in  their  language  is *  leather.'  And  Barros  (where  quoted below)  says  allusively  of  the  rope : ^^  parece  feito  de  coiro  (leather)  encolhen- do  e  estendendo  a  vontade  do  mar,"^ contracting  and  stretching  with  the movement  of  the  sea.
6945:c.  1530.—"  They  made  ropes  of  ooir,  which is  a  thread  which  the  people  of  the  country make  of  the  husks  which  the  coco-nuts  have outside."— Correa,  by  Stanlej,  133.
7414:COPBAH,  s.  The  dried  kernel  of the  coco-nut,  much  used  for  the  ex- pression of  its  oil,  and  exported  largely from  the  Malabar  ports.  The  Portu- guese probably  took  the  word  from  the Malayal.  koppara,  which  is,  however, apparently  wrrowed  from  the  H. kkoprd^  of   the   same    meaning.    The
7423:1727. — "That  tree  (coco-nut)  produoeth .  .  .  Copera,  or  the  Kernels  of  the  Nut dried,  and  out  of  these  Kernels  there  is  a ▼ery  clear  Oil  exprest." — A.  Hamilton,,  i. 307 ;  [ed.  1744,  i.  308].
7452:1644.— "To  the  Friars  of  St.  Francis  for their  regular  yearly  allowance,  a  cow  every week,  24  candies  of  wheat,  15  sacks  of  rice ginuol,  2  sacks  of  sugar,  half  a  candy  of tero  (qu.  sevo,  *  tallow,^  *  grease,*?)  ^  candy of  coco-nut  oil,  6  maunds  of  butter,  4 eoijas  of  cotton  stuffs,  and  25,920  r^  for dispensary  medicines  (mezinkas  de  botti^u)," —Bocarro,  MS.  f.  217.
8026:1823.— "In  India  they  give  the  name  of oaril  to  certain  messes  nmde  with  butter, with  the  kernel  of  the  coco-nut  (in  place  of which  might  be  used  in  our  part  of  the world  milk  of  almonds)  .  .  .  with  spiceries of  every  kind,  among  the  rest  caraamom and  ginger  .  .  .  with  vegetables,  fruits,  and a  thousand  other  condiments  of  sorts ;  .  .  . and  the  Christians,  who  eat  everything,  put in  also  flesh  or  firii  of  ever}'  kind,  and  some- times QK^s  .  .  .  with  all  which  things  they make  a  Kind  of  broth  in  the  fashion  of  our miazz€tti  (or  hotch-potches)  .  .  .  and  this broth  with  all  the  said  condiments  in  it  they pour  over  a  good  quantity  of  rice  boiled simply  with  water  and  salt,  and  the  whole makes  a  most  savoury  and  substantial mess."- /^  del  fa  Vaf/e,  ii.  709 ;  [Hak.  Soc. ii.  328.]
9854:o.  1380.- "We  embarked  at  this  town (Jedda)  on  a  veasel  called  JalbA  which  be- longed to  Bashld-eddHi  al-alfl  al-YamanX,  a native  of  Habsh."— y6f»  Boteta,  ii.  158.  The Tranalatora  comment:  "A  large  boat  or gondola  made  of  planka  atitehMl  together with  coco-nut  fibre."
10314:c.  1690.  — "The  Siamese,  Malays,  and Macassar  people  have  the  art  of  making from  the  laiger  coco-nut  shells  most  elegant drinking  vessels,  cups,  and  those  other receptacles  for  water  to  drink  called  Gor- gelecte,  which  thev  set  with  silver,  and which  no  doubt  by  the  i^orant  are  supposed to  be  made  of  the  precious  Maldive  coooe." — Rumphius,  I.  iii.
13271:LIP-LAP,  s.  A  vul^r  and  dis- paraging nickname  given  m  the  Dutch indies  to  Eurasians,  and  correspond- mg  to  Anglo-Indian  chee-chee  (q.v.). The  proper  meaning  of  lip-lap  seems to  be  the  uncoaguiated  pulp  of  the coco-nut  (see  Rumphiiu,  bt.  i.  ch.  1). [Mr.  Skeat  notes  that  the  word  is  not m  the  diets.,  but  Klinkert  gives  Jav. lap-lap,  '  a  dish-clout.']
```


## [2026-09-07T18:20:47.757Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON nargil entry ===\"\nsed -n '71750,71790p' MON_part2.txt\necho \"=== MON parts coverage ===\"\nhead -3 MON_part1.txt; echo ...; head -3 MON_part2.txt; wc -l MON_part1.txt MON_part2.txt\necho \"=== MON بابل ===\"\ngrep -n \"بابل\" MON_part1.txt | head -5"
}
```


### [2026-09-07T18:20:47.866Z] TOOL RESULT

```
=== MON nargil entry ===


(امر.) کو کتار. افون» تر با کث. 

نارگیل: او [- معر. نارجیل] (.) (گیا.) 
درختی است از تبرة نخل‌ها که ار تفاعش تا 
۰ متر نیز می‌رسد و دارای ساقهٌ منتهی به 
برگ‌های بزرکگک به طول ۴ تا ۵ متر است. 
این درخت در تمام ایام سال دارای موه 
است. مبوه‌اش شفت و گاهی به قطر ۳۰ 
سانته تیمتر و به وزن چند کیلوگرم می‌رسد. 
میوة نارگیل که به بازار عرضه می‌شود 
بو شیده از الباف بی‌شماری است که بجای 
میان بر میوه هستند و در زير الیاف پوستة 
سخت و استخوانی میوه که عبارت از درون 
موه است قرار دارد پس از شکستن این 
بوستة سخت مغز مبوه که همان قسمت 
خوراکی آن است هویدا می‌شود. این مغز 
سصورت یک حفرة تسوخالی است که 
ضخامت جدار آن بین ۱/۵ تا ۲ سانتیمتر 
است و همان آلبومن مبوه می‌باشد که جنین 
را نیز در بردارد. در داخل این حفره مغزی 
مایعی بنام آب نارگیل که بی‌رنگ است 
وجود دارد که دارای اثر کمی ملین است و به 
عنوان مفرح خورده می‌شود. میوة نارس 
نارگیل فاقد مغز است ولی در عوض درون 
7[ 
کمی شیرین و مطبوع پر کرده است که بنام 
شیر نارگیل موسوم است ولی پس از رسیدن 
کامل میوه در جدار داخلی درون‌بر رسوب 
مواد ذخیره‌ای (آلبومن) ایجاد می‌شود و 
یکك طبقةً نرم به ضخامت ۱/۵ ۲۱ 
سانه نتیمتر بوجود می آورد که همان قسمت 
راک موه ات ین نتب ار 
است. از مغز نارگیل روغنی بدست 
می آورند که بنام کرة نارگیل موسوم است و 
سفید رنگ می‌باشد. اين روغن را در تهية 
صابون و شمع بکار می‌برند و در صورت 
تصفیه شدن به مصرف تخدیه نیز می‌رسد؛ 


=== MON parts coverage ===
0 
2 

...
معین» محمد» ۱۲۹۱ ۱۳۵۰. 


  99339 MON_part1.txt
  94500 MON_part2.txt
 193839 total
=== MON بابل ===
19644:بابل: ۵1 (.) مغرب؛ مق. خراسان به 
43676:تمور: ۱20012 ,۱2012 [معر. سر. بابلی ]
```


## [2026-09-07T18:20:49.921Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HJB hookah/nargeela ===\"\ngrep -n -i -E \"hookah|hubble|nargeel|narg\" HJB.txt | head -15\necho \"=== DEV narguile ===\"\ngrep -n -i -E \"narguil|nargil\" DEV.txt PHN.txt LKT.txt LAM.txt | head -20\necho \"=== SKT/FSD/WEB narghile ===\"\ngrep -n -i -E \"narghile|nargile\" SKT.txt FSD_vol3.txt WEB*.txt 2>/dev/null | head -10"
}
```


### [2026-09-07T18:20:50.034Z] TOOL RESULT

```
=== HJB hookah/nargeela ===
6033:CBJLLUM,  &  H.  chilam;  'Hhe part  of  the  hulia  (see  HOOKA)  which contains  the  tobacco  and  charcoal  balls, whence  it  is  sometimes  loosely  used  for the  mpe  itself,  or  the  act  of  smoking it "  (Wihan).  It  is  also  applied  to  the replenishment  of  the  bowl,  in  the  same way  as  a  man  asks  for  "  another  glass." The  tobacco,  as  used  by  the  masses  in the  hubble-bubble,  is  cut  small  and kneaded  into  a  pulp  with  go&Ty  i.e. molasses,  and  a  fittle  water.  Hence actual  contact  with  glowing  charcoal is  needed  to  keep  it  afight.
6034:1781.— "Dressing  a  hubble-bubble,  per week  at  8  AiHww  a  day.
6038:1829.— "Tugging  awav  at  ^our  hookah, find  no  smoke;  a  thief  having  purloined your  silver  chelam  and  snrpooM."— ^oAa Shipp,  ii.  159.
6385:*  H.  Tikiyd  is  a  little  cake  of  charcoal  placed  in the  bowl  of  the  hooka,  or  hubble-bubble.
6834:c.  1328.— "  First ^f  these  is  a  certain  tree called  Nargil;  which  tree  eveiy  month  in the  year  sends  out  a  beautiful  frond  like [that  of]  a  [date-]  palm  tree,  which  frond  or branch  produces  very  large  fruit,  as  big as  a  man's  head.  .  .  .  And  both  flowers and^  fruit  are  produced  at  the  same  time, beginning  with  the  first  month,  and  going up  gradually  to  the  twelfth.  .  .  .  The fruit  is  that  which  we  call  nuts  qf  India,"— Friar  Jordanus^  15  a«q.  The  wonder  <A  the coco-palm  is  so  often  noticed  in  this  form by  medieval  writers,  that  doubtless  in  their
6839:c.  1350.~<<  Wonderful  fruits  there  are, which  we  never  see  in  these  parts,  such  as thaJfarffU.  Now  the  Nargil  is  the  Indian NutJ*—John  MarignoUxy  in  Cathay,  p.  352.
11254:Bays:  "There  was  a  dinner  l>artjr  in the  evening  (at  Agra),  mostly  civibans, as  I  quickly  discovered  by  tneir  huqas. I  have  never  seen  the  hriqa  smoked save  at  Delhi  and  Agra,  except  by  a very  old  general  officer  at  Calcutta." (Life  in  the  Mission,  ii.  1961  In  1837 Miss  Eden  says:  "the  aides-de-camp and  doctor  get  their  newspapers  ana hookahs  in  a  cluster  on  their  side  of  the street."  (Uv  the  Country,  i.  70).  The rules  for  the  Calcutta  Subscription Dances  in  1792  provide :  "  That  ho<^cer8 be  not  admitted  to  the  ball  room  during any  part  of  the  night  But  hookers might  be  admitted  to  the  supper  rooms, to  the  card  rooms,  to  the  boxes  in  the theatre,  and  to  each  side  of  the  assembly room,  between  the  large  pillars  and  the walls."— Cfatrw,  Good  Ola  Days,  i.  98.] "  In  former  days  it  was  a  dire  offence to  step  over  another  person's  hooka- carpet  and  ^A:a-snake.  Men  who  did so  mtentionally  were  called  out."  (Af.- Gen,  KeaUnge),
11259:1828.— "Every  one  was  hushed,  but  the noise  of  that  wind  .  .  .  and  the  occasional bubbling  of  my  own  hookah,  which  had  just been  furnished  with  another  chillum." — TKe  KMixzilhask,  i.  2.
11262:1872.—".  .  .  in  the  background  the  car- case of  a  boar  with  a  cluster  of  villap^rs sitting  by  it,  passing  a  hookah  of  primitive form  round,  for  each  to  take  a  pull  in  turn.** — A  True  Reformer,  ch.  i.
11271:1801.— "The  Resident .  .  .  tells  a  strange story  how  his  hookah-bordar,  after  cheat- ing and  robbing  him,  proceeded  to  England, and  set  up  as  the  Pknce  of  Sylhet,  took  in everybody,  was  waited  upon  by  Pitt»  dined with  the  Duke  of  York,  and  was  presented to  the  'Kixi%"^Elfh%ntti(me,  in  L\fe,  i.  34.
11367:HUBBLE-BUBBLE,  s.  An  ono- niatopoeia  applied  to  the  hooka  in  its rudimentary  form,  as  used  by  the masses  in  India.  Tobacco,  or  a  mix- ture containing  tobacco  amongst  other things,  is  placed  with  embers  in  a terra-cotta  nhilliim  (q.v.),  from  which a  reed  carries  the  smoke  into  a  coco- nut shell  half  full  of  water,  and  the smoke  is  drawn  through  a  hole  in  the side,  generally  without  any  kind  of mouth-piece,  making  a  bubbling  or gurgling  sound.  An  elaborate  descrip- tion is  given  in  Terry's  Voyage  (see below),  and  another  m  Govinda  So- mantOy  i.  29  (1872).
11370:1673.—"  Coming  back  1  found  my  trouble- some Comrade  very  merry,  and  packing  up his  Household  Stuff,  his  Bang  dowI,  and Hubble-bubble,  to  go  along  with  me."— Fryer,  127.
11371:1673. — ".  .  .  bolstered  up  with  embroi- dered Cushions,  smoaking  out  cH  a  silver Hubble-bubble."- -FVy«r,  181.
11375:1868.— "His  (the  Dyak's)  favourite  pipe is  a  huge  Hubble-bubble."— IFoZ/dc*,  Mai. Archip.,  ed.  1880,  p.  80.
15249:1803. — "During  the  whole  of  our  stay  two minahi  were  talking  almost  incessantly,  to the  great  delight  of  the  old  lady,  who  often laughed  at  wlutt  thev  said,  and  praised  their talents.  Her  hookah  filled  up  the  intervaL '" —Ld.  Valentitty  i.  227-8.
=== DEV narguile ===
LAM.txt:5652:Narghileh ou Narguilé. Ce mot est proprement d'o-
LAM.txt:9440:Narghileh, Narguilé
DEV.txt:1833:Narghileh  ou  Narguilé.  Pipe  orientale.  D'après  Et.  Qua- tremère,  du  persan  Jji^^lj  nârghil ,  cocotier,  noix  de  coco. çtll  a  pris  ce  nom  parce  que  la  capsule  qui  renferme  le tabac  est  formée  d'une  noix  de  coco  ou,  du  moins,  en  a la  figure^,  v  Dans  la  pipe  syrienne  appelée  chuchet,  d'après M.  SpoU  \  le  flacon  de  cristal  du  narguilé  est,  en  effet, remplacé  par  une  noix  de  coco.
DEV.txt:4032:Narguilé,  voy.  Narghileh.
PHN.txt:3647:à la pipe persane , elle s'appelle narguileh. Voyez ce mot.
PHN.txt:7921:NARGUILEH,s. m. (p.)
PHN.txt:7929:p. Aa , dit que narguileh vient de Sx^j\i [nar^îl] cocotier ou
PHN.txt:10771:Narguileh, s. m. (p.) 28^
LKT.txt:3581:1556.  Pers.  iiärgilä: 'Wasserpfeife'  [angeblich  aus  sskr.  nä- rikera  'Kokosnuß'];  hieraus  engl,  nar- gula,  nargileh,  narghile;   frz.  narguiU,
LKT.txt:3582:kat.  nargili,  sp.  narguile,  rum.  narghilea 'dass.';  poln.  nargile.  [Eguilaz  463. ML  5823a.    Hobson-Jobson  618.
LKT.txt:6105:nargeela  1556 I  narghile  1556 i  nargileh  1556 I  natron  1567 I  nautch  1530 I  »let'Z  1568
LKT.txt:6635:narguilS  1556 j  natron  1567
LKT.txt:7308:nadir  1565 nargili  1556 naronja  1565 nenufar  1570
LKT.txt:7669:nargile  1556
=== SKT/FSD/WEB narghile ===
```


## [2026-09-07T18:21:06.053Z] TOOL CALL #24: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:2095 --image 2>&1 | tail -40"
}
```


## [2026-09-07T18:21:06.828Z] TOOL CALL #25: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/narghile",
 "prompt": "Give the full etymology entry for narghile (and hookah if present): source languages, forms, dates."
}
```


### [2026-09-07T18:21:12.521Z] TOOL RESULT

```
REF: BQT:2095  PDF: data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf page 178  OCR-lang: fas

مومت باریکه
رمان‌المال خوانند.#* بعربی رمان مصری خوانند وخاسیت آن نزديك
نارمشاک - بنم میم رسکون خبن بنبل است ۱ - وکوره آهنگری را نیز کوبند
نقطه‌دار وکاف » نارهندبر | کوبند وآن تغمی‌است | باعتبار آتش وانگشت .38
سرخ زلگه و اندك سبزی در میان دارد و آنرا نار نگ ۴ » با کاف فارسی » بر وژن
۸-۱« بارمعك » و هو الناغیشکه. ویمی ایا المظ » و دی اساً مشکه الرمان » و
هو حقيشة هندية » « عقار ۲۵۶ 6 . بارمشعك فازسی است بمعنی مشك آنار ( قسن : مشك‌الرمان
(مر) م.م. ) ۳ ۲۵۲۲۵۵ 31/169۵ «عقار *۲۵ ف » ورك : دزی ج ۲ اس ۷:۹۳۱ ۰
۲ < بارنج («.م.) » فی : نارنگی :
همیشه تا بنجارت زمرو شهجان کس وی آمل وساری نیاورد تارنگك .
ظهین فاربایی « فرهنگه نظام >.
0 ار گیل - بکس کاف ۰ پهلوی و812۲ ,۰ او نوالا ۹۲۲۷ هعرب آن تارچیل
« تفس » ونارجیله « دزی چ ۷ م۳۱٩۹‏ > . در نامه بهلوی خسرو کواتان بند *۵آمده: «ابار گیل
که با شکر ۹
خورلد . به وا 8 ای
( زبان ) هندو ۳۹۲۳۷ گر ۸ ونم ی ۳ ار
« ابارکیل ۲ ۵ 1 نج 0 4 م
غواند وب وید رم 7 1 ۹
(زبان) پارسیك اه رن رسد را ۰ مک هید
7 کوج هندوك ۳ لگ ۸ ت ۰
( گوژهندی) ۰ لدع 6 ره
خوانند.» ر4: مق ۰ هه
خسرو قبادان میوة تا رکیل و مقطع آن درخت نار گیل
وربذاه وی ترجمهٌ انکارنده (مجلةٌ آموزش وپرورش سال 2 ۱ص۵۹؟۲). - درسانکر بت 618 82716.,
42 ونظایرآن. 0.585 ,1۳28102 - 5180 , .8016 ورك : هرمزدنامه ص ۹-۲*۸؛
نا ر گیل - ۷0110۲8 ۳۵608 ( 201 - 6000 انگه ) ۰ لوفر. اساً » درختی ازانواع تخلها
45 که کلهای در ومادة آن برروی بك درخت است و میوة درشت آن پوشیده از فسمتی
سخت وچوبی و آلبومن‌آن دارای طبقه‌ای سفید رلگه است که*/۰* ۹۵ آن روغنی دارد که درحدود
۹ درجه مایم میشود . این درخت بیشتر در جزایر مرجانی آقیانلوی هند میروید - « کل کلاب
ص ۰.۲۹۱
۶ ار نج - بفتح نون (ودرلهجهٌ مر کزی‌بکر) ؛کردی ع 2۳2 ۰ 38۲828 « زایا
س .4۱4 ۰ کیلکی [۵۸۲۵0؛ نارج (0ط80۲81۳ 11۳008)) معرب ۸
نارنکه (م.م.) است[وقس: نارنگی]. واصل این‌لفت هندی‌است. ولی‌ازراه رام
زبانهای ایرانی وارد زبانهای آروپایی شده صورت 0۳2886 درآمده ؛ سس ۸:2
و آن از انواع مرکبات است » صورت درختی با میوه‌های کرد ( که هه
نطح آن فرورفتگیهایی دیده میشود). زرد رلگه وترش مزه . ی
شاخه تارلج
```


### [2026-09-07T18:21:17.551Z] TOOL RESULT

```
# Etymology of Narghile

Based on the page content, here is the full etymology entry:

**Narghile (noun)** — "oriental water pipe for smoking," documented by 1820.

**Source languages and pathway:**
- French *narghileh* → Persian *nargileh* → Persian *nargil* (meaning "cocoa-nut," referring to the material originally used for the bowl)
- The Persian term likely derives from Sanskrit *narikerah*, which may trace to a Dravidian source

The entry notes that the word entered English documentation around 1820, coming through French from Persian origins, with the ultimate source potentially being Sanskrit vocabulary related to coconut, the traditional material for the pipe's bowl.

**Note:** The webpage does not include an etymology entry for "hookah."
```


## [2026-09-07T18:21:30.924Z] TOOL CALL #26: Bash

```json
{
 "command": "ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/ 2>/dev/null | grep -i 2095"
}
```


### [2026-09-07T18:21:30.962Z] TOOL RESULT

```
-rw-rw-r--  1 sfmqrb sfmqrb  188700 Sep  7 14:21 2095.png
-rw-rw-r--  1 sfmqrb sfmqrb    3336 Sep  7 14:21 2095.txt
```


## [2026-09-07T18:21:32.368Z] TOOL CALL #27: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/n%C3%A9h%E2%82%82s-",
 "prompt": "Give the reconstruction, meaning, and the list of descendants (Indo-Iranian, Avestan, Old Persian, Latin, Germanic) for this PIE root for 'nose'. Also note any alternative reconstructions or comments."
}
```


### [2026-09-07T18:21:38.240Z] TOOL RESULT

```
# Proto-Indo-European Root for "Nose"

**Reconstruction:** *néh₂s (feminine noun)

**Meaning:** "nose"

**Major Descendants:**
- **Indo-Iranian:** Proto-Indo-Iranian *náHs
- **Latin:** *nāsus* ("nose") and *nāris* ("nostril")
- **Germanic:** Proto-Germanic *nasō and *nustrō
- **Balto-Slavic:** Proto-Balto-Slavic *nāˀsis (Lithuanian *nósis*, Latvian *nāss*)
- **Albanian:** *noçë

**Alternative Reconstructions:**
The entry notes several competing proposals: *Hnéh₂s-, *nás-, and *Hnás-. Scholars debate "whether the stem-final *-s- is considered part of the root" or functions as a suffix, affecting how the inflection pattern is classified.

**Key Comment:** The reconstruction shows "little other evidence for" the *neh₂- root component beyond this noun, making the morphological analysis somewhat uncertain among specialists.
```


## [2026-09-07T18:21:44.207Z] TOOL CALL #28: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/2095.png"
}
```


### [2026-09-07T18:21:44.677Z] TOOL RESULT

```

```


## [2026-09-07T18:21:44.675Z] INPUT

[Image: original 1650x2546, displayed at 1296x2000. Multiply coordinates by 1.27 to map to original image.]


## [2026-09-07T18:21:45.384Z] TOOL CALL #29: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D8%A8",
 "prompt": "Give the Arabic etymology of باب 'door, gate' (root, Proto-Semitic reconstruction, any claim of borrowing from Akkadian/Aramaic), and the Persian section for باب if present."
}
```


### [2026-09-07T18:21:52.110Z] TOOL RESULT

```
# Etymology of باب (Door/Gate)

## Arabic Etymology

The word باب (bāb) has two competing etymological accounts:

**Borrowing Theory:** "Usually considered a borrowing from Aramaic בָּבָא (bāḇā, 'gate'), from Akkadian 𒆍 (bābum, 'gate')," particularly since tent-dwelling Arabs had no traditional need for doors.

**Native Origin Theory:** Hans Bauer proposes these words are native to Semitic, explaining the formation as "an ancient univerbation of etyma equivalent to Arabic بَاءَ (bāʔa) بِ (bi) 'he has entered into (the house).'"

The word belongs to the root **ب و ب** (b w b).

---

## Persian Section

Persian has multiple meanings for **باب** (bāb/bâb):

1. **Adjective (Etymology 1):** Means "appropriate"

2. **Noun (Etymology 2):** Primarily means "chapter" (of written works); archaically means "door" or "gate"

3. **Proper Noun (Etymology 2):** Refers to **Báb** (the religious figure)

4. **Archaic Noun (Etymology 3):** Means "father"

5. **Proper Noun (Etymology 4):** A transliteration of the English name "Bob"
```


## [2026-09-07T18:22:22.751Z] TOOL CALL #30: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT\ncat > /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/2095.vision.txt <<'EOF'\n[BQT p. 2095 = Borhan-e Qate' vol. 4, pdf page 178 (BQT_v4_picofile.pdf). Read from the\nrendered PNG (ocr/BQT/2095.png) by eye; Mo'in's etymological footnotes at the foot of the page.]\n\n☆ نارگیل ـ بکسر کاف ، پهلوی anârgil « اونوالا ص ۲۲۷ » ، معرب آن نارجیل\n« نفس » و نارجیله « دزی ج ۲ ص ۶۳۱ » . در نامهٔ پهلوی خسروکواتان بند ۵۰ آمده: « انارگیل\nکه با شکر خورند ، به (زبان) هندو « انارگیل » خوانند و به (زبان) پارسیک « کوچ هندوک\n(کوژهندی) » خوانند.» رک: خسرو قبادان وریذک وی ترجمهٔ نگارنده (مجلهٔ آموزش و پرورش\nسال ۱۴ ص ۲۵۶). ـ در سانسکریت nârikela ، nârikera و نظایر آن. Laufe., Sino-Iranica, p.585\nورک: هرمزدنامه ص ۲۰۸-۹؛\n\nنارگیل ـ Cocos nucifera (coco-nut انگ) ، لوفر. ایماً ، درختی از انواع نخلها palmiers\nکه گلهای نر و مادهٔ آن بر روی یک درخت است و میوهٔ درشت آن پوشیده از قسمتی سخت\nو چوبی و آلبومن آن دارای طبقه‌ای سفید رنگ است که ۰/۰۶۵ آن روغنی دارد که در حدود\n۲۶ درجه مایع میشود . این درخت بیشتر در جزایر مرجانی اقیانوس هند میروید . « گل گلاب ص ۲۹۱ »\n\n[same page, neighbouring headwords, for orientation: نارمشک ، نارنگ ۲ ، نارنج\n(«نارنج ـ بفتح نون ... معرب نارنگه (م.م.) است [وقس: نارنگی] . واصل این لفت هندی است\nولی از راه زبانهای ایرانی وارد زبانهای اروپایی شده صورت orange درآمده») ]\nEOF\nwc -l /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/2095.vision.txt"
}
```


### [2026-09-07T18:22:22.816Z] TOOL RESULT

```
18 /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/2095.vision.txt
```


## [2026-09-07T18:22:24.646Z] TOOL CALL #31: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A3%D9%86%D8%A8%D9%88%D8%A8",
 "prompt": "Give the Arabic etymology and meaning of أنبوب / unbūb (root, relation to نبّ n-b-b 'to be hollow'), and any Persian borrowing."
}
```


### [2026-09-07T18:22:30.081Z] TOOL RESULT

```
# Etymology and Meaning of أنبوب (unbūb)

## Meaning
According to the Wiktionary entry, أنبوب (ʔunbūb) is "a masculine noun meaning tube, pipe, or nozzle." The plural form is أنابيب (ʔanābīb).

## Etymology
The word traces back through several ancient languages. As stated in the source: "From Aramaic אַבּוּבָא / ܐܰܒܽܘܒܐ (ʾabbūḇā, 'flute; pipe'), from Akkadian 𒄀𒁍 (enbūbu, 'flute')."

## Root Analysis
The provided content does not discuss the n-b-b root or explain the relationship to نبّ (to be hollow). The etymological information focuses on the ancient Near Eastern language chain rather than Semitic root morphology.

## Persian Borrowing
The Wiktionary article provided contains no information about Persian borrowing of this term.
```


## [2026-09-07T18:22:35.564Z] TOOL CALL #32: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D0%B1%D0%B0%CC%81%D0%B1%D0%B5%D0%BB%D1%8C",
 "prompt": "Ignore if irrelevant; report what this page is about."
}
```


### [2026-09-07T18:22:37.014Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-07T18:22:37.693Z] TOOL CALL #33: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Babylon",
 "prompt": "Give the full etymology of Babylon and of Babel: Akkadian Bāb-ilim / Bābili, the 'gate of the god' interpretation, whether it is described as a folk etymology, the Sumerian KA.DINGIR.RA, and any pre-Akkadian/substrate name (Babil, Babilla)."
}
```


### [2026-09-07T18:22:44.078Z] TOOL RESULT

```
# Etymology of Babylon and Babel

## Babylon

According to Wiktionary, Babylon derives from multiple language layers:

**Akkadian origin**: The name comes from Akkadian *Bābilim* (𒆍𒀭𒊏𒆠), which is described as literally meaning **"Gate of God."** This Akkadian form traveled through Ancient Greek (*Βαβυλών* / Babulṓn), Latin (*Babylōn*), and eventually into Old English and modern languages.

The entry notes that "the name of the ancient Chaldean capital and Biblical city of the Apocalypse" preserves this etymological chain across millennia.

## Babel

Wiktionary identifies Babylon and Babel as **doublets**—related word forms deriving from the same ultimate source. The entry states they share Akkadian *Bābilim* as their common ancestor, with Babel representing an alternative English form.

## Missing Information

The provided Wiktionary content does not include:
- Explicit discussion of whether the "Gate of God" is labeled a folk etymology
- Reference to the Sumerian *KA.DINGIR.RA*
- Pre-Akkadian or substrate language names like *Babil* or *Babilla*

These etymological details fall outside the scope of this particular dictionary entry.
```


## [2026-09-07T18:22:50.223Z] TOOL CALL #34: WebFetch

```json
{
 "url": "https://en.wikipedia.org/wiki/Babylon",
 "prompt": "What does the Etymology / Name section say about the origin of the name Babylon: Akkadian Bābilim 'gate of the god', whether this is a folk etymology of an earlier (pre-Akkadian/substrate) name such as Babilla/Babil, and the Sumerian ka-dingir-ra?"
}
```


## [2026-09-07T18:22:51.111Z] TOOL CALL #35: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/nostril",
 "prompt": "Give the etymology of nostril and of nose (Old English nosu, Proto-Germanic, PIE root)."
}
```


### [2026-09-07T18:22:56.192Z] TOOL RESULT

```
# Etymology of Nostril and Nose

**Nostril** comes from late 14c. Old English *nosþyrl*, which is a compound literally meaning "the hole of the nose." It combines *nosu* (nose) with *þyrel* (hole). The word underwent metathesis, where "the form was corrupted in the compound" as the second element became obsolete.

**Nose** has a longer lineage. The Old English *nosu* derives from Proto-Germanic *nuso-, which appears across related Germanic languages (Old Norse *nös*, Dutch *neus*, German *Nase*). Ultimately, both trace back to the PIE root *\*nas-* meaning "nose."

The key structural difference is that *nostril* is a descriptive compound—literally naming the anatomical opening—while *nose* itself is the foundational term from which other related words developed.
```


### [2026-09-07T18:22:57.009Z] TOOL RESULT

```
# Etymology of Babylon

The Names section discusses multiple theories about the origin of "Babylon":

**The Traditional View:**
The name derives from Akkadian "𒆍𒀭𒊏𒆠, romanized: _Bābilim_," meaning "gate of the [god(s)]." The Sumerian cuneiform equivalent is _KÁ.DIG̃IR.RAKI_ (Kan dig̃irak).

**The Folk Etymology Theory:**
However, scholars increasingly view the "gate of god" interpretation as a folk etymology obscuring an earlier, non-Semitic placename. Ignace Gelb argued in 1955 that the original name was likely "_Babilla_, of unknown meaning and origin," which later transformed into the Akkadian _Bāb-ili(m)_. The Sumerian name would then represent a loan translation of the Semitic folk etymology rather than the original designation.

**Key Quote:**
"The 'gate of god' interpretation is increasingly viewed as a Semitic folk etymology to explain an unknown original non-Semitic placename."

This suggests the recognizable etymology was a secondary development, masking an earlier substrate language origin now lost to scholars.
```


## [2026-09-07T18:23:20.452Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== WLD nas ===\"; grep -n -E \"\\bnas-|nāsus|nasa \" WLD.txt 2>/dev/null | head -10; ls | grep -i WLD\necho \"=== IEC nas ===\"; grep -n -E \"^nas|nāsos|nasā|'nose'\" IEC.txt | head -10\necho \"=== SYN nose ===\"; grep -n -i -E \"4\\.23|NOSE\" SYN.txt | head -10"
}
```


### [2026-09-07T18:23:20.526Z] TOOL RESULT

```
=== WLD nas ===
WLD_band3.txt
=== IEC nas ===
4876:ghránis, os ‘tip, point, spike, edge’. Cf. ghróünis, os. WP I, 606 Tokh. B Kran (queried: ‘spine’ but Tokh. A kran 'nose' is: Skt. ghranam, -a, id. fr. ji-ghrà-mi 'smel); Olr. gráin “point, edge’; Ir. f. ‘spearhead’; W gran ‘cheekbone; eyelid’; grain ‘socket, ring’; Lat. (fr. Gmc.) granus, grana ‘moustache’; MHG gran “tip of hair, hair on lip, bristle’; G Granne; ON gron, pl. granar ‘hair on lip, lip of cattle’; (the Ir. and Gmc. forms are ambig. see ghrün-); Pol. grań ‘crest of mountain’; R grani ‘facet; limit"; Cz. hráň, hráně 'crystal ; hrana “edge, corner, angle’; cf. hranol ‘prism’; Srb. grána ‘branch; shoot; ankle’; Blg. gran, pl. -ove ‘facet’; grani (3) ‘branch’; Lusat. hrana ‘corner’. (The Sl. forms are ambig. cf. ghrõnis, os)
11536:nas- (nās-) ‘nose, nostril’. WP II, 318 (with short vowel) Skt. nas, f. id.; OHG nasa, sf. id.; OE nosu, f. id. beside næss, -a, s. & wm ‘headland’; ON nọs, pl. nasar, nasir ‘nose, ` nostril’; nes, n., gp: nesja ‘headland’; OCS (and com. Sl.) nosü, m. ‘nose’ (with long vowel) Skt. nas, f. dual. ‘nose, nostrils’; nasa, f. id.; Av. nàðh- ‘nose’; Ober nåham, id.; Lat. nårës, gp: -ium, f. (nose, nostrils? beside (dialectal) nàsus, gs: -i, m. (nose, whence It. naso); Sard. nare, m. ‘nose’; OE nose, wf. “headland”; Du. neus, m. ‘nose’; Sw. nos, m. ‘snout’; Li. nósis, usu. in pl. nósys, gp: nósiuy, f. ‘nose’; Latv. nàss, usu. in pl. nāsis, gp: nāšu, id.
11538:nask- see naks-
11539:nast- variant of type nask-, naks- in W nais, pl. neisiau, m. ‘band, tie’; cf. OHG nestilo, wm. ‘fillet, snood, band’; OFris. nestla, wm. id.; MHG, G. Nestel, sf. id.
=== SYN nose ===
2:ee Nose
5017:2. Lat. stmia (>It. scimmia, Fr. singe), deriv. of stmus, loanword fr. Grk. otés ‘snub-nosed’. First used as a nickname and prob. based on the name ZYuyuslas, Simia. Kretschmer, KZ 33, 563.
5126:Goth. .--- ta ON fluga Gee fae Dan. flue N t musca Sw. fluga Lar nosed OE _fleoge It. mouche ME _ flye e mosca NE fy Het mused Du. _—vlieg en oe OC ie fr. cui : M oliege ab guybedyn, cylionyn NHG fliege
5248:In the case of such inherited words the Toot connection, and so the semantic source, is in large measure obscure. So far as. we can judge from the words whose etymology is clear, the underlying notion 'S more often relating to the position or Tae the part than to its function. riasaks erited words for ‘eye’, ‘ear’ Nose’, ‘mouth’, ‘foot? are not en d from any of ee erive
5291:: of plants, etc.), ‘crop’ (of baneh, CUG Bens ‘crop (of birds), ep povelne’, OE créopan ‘creep’, ae ae bend 5 Grk. YpuTés Giiived'sh “nosed’, all with notion of
5907:ae Dies nas-. Walde-P. 2.318. Emout-M. 653, 659. Falk-Torp 779 f. Lat. nasus (> It. naso, Fr. nez, Rum. nas), also pl. narés ‘nostrils, nose’, late sg, naris (>Sp. nariz); ON sg. ngs nostril’, pl. nasar ‘nostrils, nose’, OE nosu, nasu, OHG nasa, etc., general Gme.; Lith. nosis, OPruss. nozy; ChSl. nosit, etc., general Slavic; Skt. nas-,; nas- (in RV only dual, nom. nasd, gen. nasos), Ay., OPers, nah- (sg. and dual in Av., sg. in OPers.). The meaning ‘nostril’ is implied by the early use of dual or pl. forms, but is not necessarily older than ‘nose’, For it may be abstracted from the latter, and the dual was favored by i ae in the case of ‘eyes’, ‘ears’, 2. Grk. pts, gen. pivds, also pl. pives ostrils, nose’ (like Lat. narés), etym.? . Seng ane either : Pr TAG ES i c, (Boisacq 842) or : with query) i ete. (Walde-P. 1.140
5912:gprs OF T 4.23 NOSE Lith. nosis Goth. .--- pis ON nasar Lett. deguns Gre im Dan. nase Chsl. nosit nasus Sw. nisa SCr. nos naso OE nosu Boh. nos nez ME _~ nose Pol. nos nariz NE nose Russ. os Rum. nas Du. neus Skt. nas-, ghrana- sron OHG nasa Av. nah- sron MHG nase i NHG nase Tl Most of the words for ‘nose’ belong to | then orig. a vulgar epithet, displacing Mo:
5915:3. Ir. srén = W. ffroen, Br. fron ‘nos- tril’ (here in some way Br. fri ‘nose’, MBr. fry), fr. *skrok-na-, prob. : Skt. srakva- ‘corner of the mouth’, and fr. the root in Ir. srennim, Grk. peyxo, péyxw ‘snore, snort’, of imitative origin. Walde-P. 2.705. Pedersen 1.82. Lewis- Pedersen 22.
5918:5. Skt. ghrdna- ‘smell’ and ‘nose’, fr. ghra-~ ‘smell’ (15.21).
7260:4.73 PREGNANT Goth. inkilpo, pat es pees vos <2 ieee ON unguo, Ulett, hafan- ett. gr Grk. (yyvearpane” tb a id A di, med barni ChSl. neprazdtna NG pracgnans, GRE Dan.  frugtsommelig, svan- SCr. _trudna, breda, nose¢a lat. inciéns | iatoreg: ger; dreglig Boh. téhotna; brezt gravida, ncn a, P Sw. havande; draktig Pol. brzmienna, ciezarna te na Deine OE getacnod, bearn-éacen, Russ. beremennaja Fr encernle, 9” pee 4 med cilde Skt.  garbhini-, garbhavati-, Sp. prenada, Pets ME with childe, with barne etc. Rum. insdr Fie ut NE pregnant, with child Avy. pubra- lorrac . ; drachti Ir. ‘i hea- Du. zwanger; 9g Nir. bruinneach, tourch GHik. smaieee sach MHG _ swanger, trehtec, w. _ beichtog swere : razez, dougerez eee Breese eraeees NHG  schwanger; trdchtig
```


## [2026-09-07T18:23:22.712Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT nanhan context + column marker ===\"\nsed -n '19085,19110p' BRT.txt | cut -c1-140\npython3 - <<'EOF'\nimport re\nlines=open('BRT.txt',encoding='utf-8',errors='replace').read().split('\\n')\nmarks=[(i,l.strip()) for i,l in enumerate(lines,1) if re.fullmatch(r'\\s*\\d{3,4}\\s*',l)]\nprint([m for m in marks if 18900<m[0]<19300])\nEOF\necho \"=== HJB NARGEELA ===\"\ngrep -n -i -E \"nargeela|nargeel|gurglet|HOOKA,\" HJB.txt | head -10"
}
```


### [2026-09-07T18:23:24.147Z] TOOL RESULT

```
=== BRT nanhan context + column marker ===
—  «)  Sun  ia..<-a  ei»<mete  man  die  Wieder-  i      GG*-  ''>93-  39»-  —  ?  ans  ar.  ä,  S  ap*.  3-  — holong  von  niu. 
fpif;    aber  Po.:   n?.  —   ")   AuffUtig   ist   die        °        *  ■^'
Verbindnog  von  neii  mit  fj.  •  j.  'ainidkim  n^a"  N.  66:  —  ?  — .
j.  läim  N.  /Op:  lies  Ä'ft.  I       I^:  fimi  uiäyiin;  s.  in  aimdkim.
g.  nS:  s.  unter  «j..  ,  ,  j^  g   qj_  j^  g  „j-.^  „^.^  p   „,^,   jj  ^j„
j.  «A.A-;  a.  «ii.  lud  die  folg.  Wörter.       a) 'nieder,  hinunter' (nurKomp.).      bj'hin-
•  j.  nanhaidya-  m.  Name  emes  /?aÄa*':  ein' (nur  Komp.),  a)  Praev.  (mit 'ar-,  a*-, ifidrfm  ..  saurum  ..  '^im  daeum  V.JO.
*;i;w'*  (statt  NS.)   V.ip.43.  KompA.;   Ableit.   —    ai.  m,  np.  iw*,  na",  —
•)   Vgl.   Bd.  38.   10:    "Ihe    business    of   the  |      Pö.:  api,  ni:  —   i)  Vgl  Vt  8.  29. demon  .V-.  i,  Ulis,   t
J/.  213  No.  4,  Blochet  RHR,  jr.  113.  ^-    *'"»-•
Et.  und  eig.  Bed.?>).  —  ai.  nasalya-  Beinort  |       'Vgl-  T^-aiartta-,
dei  AJzina».    —    •!    S.    zu /vUay  ÜO.  t.   —  i  •  j.  ni-MBhant- Adj.  (fem.  »Ä^Ä-),  ITA.:
'i  Vgl.  MMOiLEB  Wits.  Myth.  2.  147,  UnLEN-  '  .   '     i
BECK  WAiSpr.   147.  I*
a   .  „..,.,        .         •  i.  ni-ynintay- 1 'Niederschlagen :  >w«
.  j.  nanhan-  m.  'Nase'  des  Menschen:!  ..^- ^^.^„^„  ^^,^  .,,■  „,.^^_^^^„  ,.
upa   va  »a^/  rai>wat  -Aanai  haca  V.  f^^^^tmU  mi%rs  Yt/o.  133-
S-  14;  —  •fia  (Ni).)  '   i'.  Jd.  I      zam  V.  .^an-.  —  Die  Art  der  BUdung  ist  mir
VgL   »Sh-  und    Bloomfield  AJPh.  /?.  9.  —  |      nndeutlich;   Cld.  KZ,  32.  S9I    verstehe   ich
Pd.  (dRn.):  n^k,  •vtnlk.—  t)  Oder  au  näh-,  sd.       »„ch  nichL    F  l  hat  «t^anintL    VII.  rnTtuinä
•  j.  iuima.a'zbätay-  ■'  £  'Anrufimg  (einer  I     *"  ^^-  '■  3°"  **"■  *■
Gottheit)   mit   dem  Namen,   namentliche  •  J-  ni-jroant-  Adj^  PPA:  s.  gam-  mit
Anrufung*:  kva  asli  vfrikrarjnahe . .  'zbäitiS  No.  30.
"wo  ruft  man  den  V.  namentlich  an?"  YL      "■  S"""^'  ^^J-  CA"  ^»  f  "-i««  RV.  10. 3a.  1).
*-a-iiä/ay-{..  zamV.iiä-;  ai.  vgL  äAüeay-I.  —  \»  j.  luxäato  Adv.,  mit  AbL  'niederwärts Npü.:  nJm  ia  näm  yäd  tar
'"^-'^-  fährt  i.  5^  Vt  70. 127-
[(18964, '1070'), (18984, '072'), (19026, '1074'), (19056, '078'), (19155, '084'), (19210, '1086'), (19292, '1089'), (19294, '1090')]
=== HJB NARGEELA ===
6036:1811. — "They  have  not  the  same  scruples for  the  Cbmimi  as  for  the  rest  of  the  Hooka, and  it  is  often  lent  .  .  .  whereas  the  very proposition  for  the  Hooka  giyee  rise  fre- quently to  the  most  ridiculous  quarrels.'*— JSoieytu,  at
6385:*  H.  Tikiyd  is  a  little  cake  of  charcoal  placed  in the  bowl  of  the  hooka,  or  hubble-bubble.
11239:HOOKA,
11250:HOOKA,  s.  Hind,  from  Arab. huhkahy  properly  *a  round  casket.* The  Indian  pipe  for  smoking  through water,  the  elaborated  hnbDie-babDie ^q.v.).  That  which  is  smoked  in  the Moka  is  a  curious  compound  of  tobacco, spice,  molasses,  fruit,  &c.  [See  Baden- Potoelly  Panjah  Products,  i.  290.]  In 1840  the  hooka  was  still  very  common at  Calcutta  dinner-tables,  as  well  as regimental  mess-tables,  and  its  bubble- btMle-bubble  was  heard  from  various quarters  before  the  cloth  was  removed — as  was  customary  in  those  days. Going  back  further  some  twelve  or fifteen  vears  it  was  not  very  uncommon to  see  the  use  of  the  hooka  kept  up  by old  Indians  after  their  return  to Europe ;  one  such  at  least,  in  the  re- collection of  the  elder  of  the  present writers  in  his  childhood,  being  a  lady who  continued  its  use  in  Scotland  for several  years.  When  the  second  of  the present  writers  landed  first  at  Madras, in  1860,  there  were  perhaps  half-a- dozen  Europeans  at  the  Presidency who  still  used  the  hooka ;  there  is  not one  now  (c.  1878).  A  few  gentlemen at  Hyderabad  are  said  still  to  keep  it up.    [Mrs.  Mackenzie  writing  in  1850
11257:1783.— "For  my  part,  in  thirty  years' residence,  I  never  could  find  out  one  single luxury  of  the  East,  so  much  talked  of  here, except  sitting  in  an  arm-chair,  smoaking  a hooka,  drinking  cool  water  (when  I  could get  it),  and  wearinjg  clean  linen."  —  {Jos, Price),  Some  ObsenxUums  on  a  late  Publicatiim. Ac.,  79.
11264:HOOEA-BUBDAB,  s.  Hind,  from Pers.  hukJha-barddr,  *  hooka-bearer ' ;  the servant  whose  duty  it  was  to  attend  to his  master's  hooka,  and  who  considered that  duty  sufficient  to  occupy  his  time. See  fViUiamson,  V.M.  i.  220.
20998:c.  545, --"The  Argell"  (t.e.  NargiL  or nargeela,  or  coco-Dut)  "is  at  first  full  of very  sweet  water,  which  the  Indians  drink, using  it  instead  of  wine.  This  drink  is  called RhoncO'VOXtLt^  and  is  exceedingly  pleasant." — CosttuUf  in  Catftay,  &c.,  clxzvi.
25433:4236,6306 Hoogorie,  4316 Hooka,   -Burdar,
```


## [2026-09-07T18:23:47.963Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN/HUB nargil ===\"; grep -n -i -E \"nārgīl|nargil|närgil|Kokos\" HRN.txt HUB.txt | head -10\necho \"=== ARY nargil / bab ===\"; ls | grep -i ARY; grep -n \"نارگیل\" ARY*.txt 2>/dev/null | head -5\necho \"=== AFM bab/anbub ===\"; grep -n \"الباب\\|أنبوب\\|انبوب\" AFM_pages.txt 2>/dev/null | head -8\necho \"=== FVQ bab ===\"; grep -n -i -E \"^bāb|bab\\b\" FVQ_pages.txt | head -8\necho \"=== AFA (Fraenkel) bab ===\"; grep -n -E \"bāb|Thür|Tür\" AFA.txt | head -10"
}
```


### [2026-09-07T18:23:48.086Z] TOOL RESULT

```
=== HRN/HUB nargil ===
=== ARY nargil / bab ===
NYB_vol2_glossary.txt
(eval):3: no matches found: ARY*.txt
=== AFM bab/anbub ===
771:١‏ الباب) وهو معروف فارسية يآ وه حتت بالاراميّة والرايّة وددة بالمراجة
1189:الباب الرابع
1563:والباب المشبك وهو مركب من در ܼܦ باب ومن بند اي رباط وسد ٠‏ ومن در ند
1588:( الد ركاه ) القصر فارسينَة دركاه ومعناه الباب والسذة والدار وهو ® من
1743:( الدهليز) ما بين الباب والدار تعريب دهله 5 القنطرة والعقدة
3347:( ܐܐܟ ) اي القدح وهو بالفارسيّة كاه وبالاراميّة ܟܣܐ وبالباباية
3414:البوص ٠‏ وهي ܟܪܲܦܣܐ باللغة البابليّة ܕ دده بالعبرانة ܣ وبرادفها
3644:ْ المتراس) ما تست به من حائط ووه من العدو وخشة توضع خلف الباب‎ ١
=== FVQ bab ===
2976:CL> (Bab).
2998:It is, of course, from the Akk. Bab-ilu (Delitzsch, Pamdies, 212),
=== AFA (Fraenkel) bab ===
45:+ Nutzung der Dateien zu nichtkommerziellen Zwecken Wir haben Google Buchsuche Tür Endanwender konzipiert und möchten, dass Sie diese
1078:Dem altarabischea Zelte maugelten die Thüren, und so
1079:kommt es , dass auch mehrere Namen der Thür übernommen
1111:Noch ein anderes Woft für »Thür" ist aramäischen
1121:Bei dem ilaugel an Thüren ist es sehr verständlich,
1125:Häuser keine Schlösser und keine Thüren haben** u^^t
1128:wo es von den Arabern heisst: »keine Thüren und keine
1206:welchem sich die Basis der Thür (v^LJl Jlä.%) dreht."
1221:der Thür in das Loch der ünterschwelle eingesteckt ist."
1227:»eine Art kleiner eiserner Becher, in denen sich die Thür-
```


## [2026-09-07T18:23:48.626Z] TOOL CALL #39: WebFetch

```json
{
 "url": "https://www.ahdictionary.com/word/search.html?q=narghile",
 "prompt": "Give the American Heritage Dictionary entry for narghile: definition and etymology (French, Persian, Sanskrit forms)."
}
```


### [2026-09-07T18:23:52.574Z] TOOL RESULT

```
# Narghile Dictionary Entry

**Definition:** According to the American Heritage Dictionary, narghile (also spelled nargile or nargileh) is defined simply as a reference to "hookah."

**Etymology:** The entry traces the word's origins through multiple languages:
- **French:** "narghilé, obsolete variant of narguilé"
- **Persian:** "nārgīleh, from nārgīl, coconut (from which the receptacle was made)"
- **Sanskrit:** "nārikelaḥ, nālikeraḥ"

The etymology notes that the coconut reference reflects the historical material used to construct the water pipe's reservoir.
```


## [2026-09-07T18:24:02.555Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== FVQ 2965-3010 ===\"\nsed -n '2965,3010p' FVQ_pages.txt | cut -c1-200\necho \"=== AFA 1075-1120 ===\"\nsed -n '1075,1120p' AFA.txt | cut -c1-160"
}
```


### [2026-09-07T18:24:02.612Z] TOOL RESULT

```
=== FVQ 2965-3010 ===
the origin of the Arabic form. 3 The name appears to have been used
in Arabia in the pre-Islamic period. Hess would interpret the Zl^K of
an inscription copied by Huber (No. 521, 1, 48), as Aiyub 4 ; there is
1 In Biblical Aramaic, however, fitf means a sign wrought by God ; cf. Dan.
2 Mingana, Syriac Influence, 86. Note also the Mand. SJTX =- sign.
3 Rudolph, Abkangiykeit, 47.
4 Hess, Die Entzifferung der thamudischen Inschriflen (1911), p. 15, No. 77 ; Litt-
mann, Entzifferung, 15 ; and see Halevy in JA, ser. vii, vol. x, p. 332.74 FOREIGN VOCABULARY OF THE QUR*AN
s.
an *-> J|J in the genealogy of 'Adi b. Zaid given in Agharii, ii, 18, and
another Christian of this name is mentioned by an-Nabigha. 1
CL> (Bab).
*
Occurs some twenty-seven times, e.g. ii, 55 ; iv, 153.
A door or gate.
Fraenkel, Fremdw, 14, noted that it was an early loan word, and
suggested that it came from the Aram. ^23 which is in very common
use in the Rabbinic writings. D. H. Miiller, however (WZKM, i, 23),
on the ground that |^Q occurs very rarely in Syr. and that the root
is entirely lacking in Heb., Eth., and Sab., suggested that it was an
early borrowing from Mesopotamia (cf. Zimmern, Akkad. Fremdw,
30), and may have come directly into Arabic. It occurs commonly
in the old poetry, which confirms the theory of early borrowing,
and it is noteworthy that from some Mesopotamian source it passed
into Middle Persian (Frahang, Glossary, p. 103 ; Herzfeld, Paikuli,
Glossary, 151).
(Babil).
ii, 96.
Babylon.
This sole occurrence of the word is in connection with the story
of Harut and Marut who teach men magic. It is a diptote in the Qur'an
but LA, xiii, 43, takes this to be not because it is a foreign name, but a
fern, name of more than three radicals (cf. Yaqut, Mu'jam, i, 447). 2
It is, of course, from the Akk. Bab-ilu (Delitzsch, Pamdies, 212),
either through the Syr. Vi^iA or the Heb. 733. The city was
well known in Arabia in the pre-Islamic period, and the name occurs
in the old poetry, e.g. Mufacjqlaliyat (ed. Lyall, p. 133, 1. 13), and
al-A'sha (Geyer, Zwei Gedickte, i, 58 = Diwan, Iv, 5), and Halevy
would find the name in a Safaite inscription. 3 Horovitz, KU, 101,
notes that Babylon was well known as a centre for the teaching of
1 Ahlwardt, Divans, p. 4; cf. Horovitz, KU, 100; JPN, 158.
2 Some, however, recognized it as a foreign name, cf. Abu Hayyan, Baftr, i, 319.
8 JA, ser. vii, voj. x, p. 380.FOREIGN VOCABULARY OF THE QUB/AN 75
magic, a fact which, we would also gather from the use of the word
Bavil in the Manichaean Uigur fragments from Idiqut-Schahri. 1
dtyJ (Baraka).
=== AFA 1075-1120 ===
Tour du monde 1882. I. p. 22: »C*est en Arabie que Tex-
pression »aveugler la porte de q.q.** doit etre inventee;
car il nV a pas de fenetres dans les maisons ordinaires** ^).
Dem altarabischea Zelte maugelten die Thüren, und so
kommt es , dass auch mehrere Namen der Thür übernommen
sind.
Das älteste und üblichste Wort ist sjL, übernommen
aus {<33f das in jüdischen Texten ungemein beliebt ist,
T T
wahrend es im Syrischen nur sehr selten vorkommt. G.
Hottmann hat es sehr einleuchtend aus* X333 :»Loch*' zur
T T :
Wurzel 333 »höhlen" erklart. Es ist schon frühe zu den
Arabern gewandert: T^r. Mu'all. 18; 17, 10; Diyan Leb.
144 , 4 ; Zuheir 9 , 27. (Nfibi^^a 4 , 3. in übertragener Be-
deutung, was immer auf längeren Gebrauch hindeutet.)
Natürlich ist auch der Gebrauch des Wortes für > Abschnitt''
»Kapitel" (wofür keine Belege nöthig) aus dem Aramäi-
schen entlehnt. Das älteste Beispiel im Aramäischen dürfte
wohl die Benennung der talmudischen Tractate Bäbd Kammdj
Me^fd und Bdthrd sein *).
1) Ein griechischer Name für «Fenster'* ist in *s Aramäische gewandert
Für 1^^ «V^l bei PSm. 240 ist nämlich geiriss richtiger du Ton ihm Ter-
worfene iLfiCfiJLfi) zn schreiben. Denn dies stimmt in Form und Bedentnng
genau zn jüd. KOlfi'iC. Dies ist z. B Kidddin Sl». 16. v. u. ^sicher: »Fenster^
)I01B'X3 K-vrO IBl 4 der Mood (Agg. Klinj; ich lese mit *Ariich) fiel durchs
Fenster**. Es ist aber kein Seiten « sondern ein Oberlicht » Fenster. Die Bedeu-
tung «Treppe**, die man dem Worte hat leihen wollen , ist — falsch — errathen,
wie auch die Zusammenstellung mit KOlfl, die sich in den jäd. Glossen und
bei Levy Nhbr. Wtb. I. 137 findet, durchaus abzuweisen ist. Es entspricht
einem griech.*'/fi^f««. Ton dem sich (in gleicher Bedeutung) Pesikta (ed.
Buber) 86^ 11 der Flural KOOlfi'K s* ii^fxatr» findet Hiemach erübrigeo
sieh die ron Lerj L 1. vorgeschlagenen Änderungen.
2) Die hebräischen Uebersetzer des Mittelalters geben ein solches v^Aj
regelmässig durch "^VJ^ wieder, woraus dann in den lateinischen üeber-
Setzungen jedesmal »porta** wird.15
Noch ein anderes Woft für »Thür" ist aramäischen
Ursprungs, ä^ti ^). Es ist nicht üblich und wird nur aus
dem ^adit überliefert, wo Muhammed sagt: »diese meine
Kanzel wird in einem der Thore des Paradieses stehen/*
Schon Freytag hat li^^^ {<>/*nn dazu verglichen ; die Thore
des Paradieses aber sind aus der jüdischen Eschatologie in
die muhammedanische Tradition gekommen. In aramäischer
Gegend finden wir \y^ äo Juküt I. 837 (in \y^j2 zu-
sammengezogen). Es ^rird von Jaküt richtig als »Thor der
Venus" gedeutet.
```


## [2026-09-07T18:24:16.817Z] TOOL CALL #41: WebFetch

```json
{
 "url": "https://vajehyab.com/moein/%D8%A7%D9%86%D8%A8%D9%88%D8%A8",
 "prompt": "Give the Mo'in (معین) dictionary entry for انبوب: part of speech, etymology marker (e.g. ع = Arabic), and definitions."
}
```


## [2026-09-07T18:24:19.024Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%A7%D9%86%D8%A8%D9%88%D8%A8/",
 "prompt": "Give the فرهنگ معین and لغت‌نامه دهخدا entries for انبوب: etymology (Arabic?), meaning (pipe, tube, reed between knots)."
}
```


### [2026-09-07T18:24:20.605Z] TOOL RESULT

```
# Mo'in Dictionary Entry for انبوب

**Part of Speech:** Noun

**Etymology:** Arabic (marked as ع)

**Definitions:**

1. "فاصلة میان دو بند یا گره نی" — the space between two joints or knots in a reed pipe

2. "هر چیز مجوف مانند نی" — any hollow object resembling a reed

3. "لوله (آب و غیره)" — a tube (for water, etc.)

**Plural:** انابیب
```


### [2026-09-07T18:24:25.529Z] TOOL RESULT

```
# انبوب Dictionary Entries

## لغت‌نامه دهخدا

**Etymology:** Arabic origin (ع اِ)

**Primary meanings:** The section of a reed or plant stem between two knots or joints. More broadly, "any hollow thing resembling a reed," including "water pipes" (انبوب الماء).

**Secondary meanings:** A mountain path, tree-lined avenue, elevated ground, or tube for liquids.

**Plural:** انابیب

Notable usage from Saadi's Bustān: describing nourishment passing through the stomach's tube.

## فرهنگ معین

**Etymology:** Arabic (اَ یا اُ) with Persian incorporation

**Core definitions:**
1. "فاصلة میان دو بند یا گره نی" — the interval between two segments of a reed
2. Any hollow object resembling a reed
3. A tube or pipe (for water, etc.)

**Plural:** انابیب

This entry presents the word's three primary senses: botanical (reed segments), generic (hollow objects), and practical (functional tubes).
```


## [2026-09-07T18:24:33.964Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%A8%D8%A7%D8%A8/",
 "prompt": "Give the فرهنگ معین entry for باب: etymology marker (ع = Arabic?), and the definitions (door/gate, chapter, etc.)."
}
```


## [2026-09-07T18:24:37.414Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN nose / nasal / nares ===\"\ngrep -n -E \"^nose,|nose,  n\\.|nasal,  adj|nostril\" KLN_1966.txt | head -5\ngrep -o -E \"nose,  n\\., the organ of smell.{0,400}\" KLN_1966.txt | head -2\necho \"---\"\ngrep -o -E \"nostril,  n\\..{0,300}\" KLN_1966.txt | head -2\necho \"---\"\ngrep -o -E \"nasal,  adj\\..{0,250}\" KLN_1966.txt | head -2\necho \"=== SKT nose ===\"\ngrep -o -E \"NOSE.{0,250}\" SKT.txt | head -3"
}
```


### [2026-09-07T18:24:39.039Z] TOOL RESULT

```
# فرهنگ معین Entry for باب

**Etymology Marker:** [ع.] (Arabic origin)

**Definitions:**

1. **Noun (اسم):** Door, gate
2. **Noun:** A section of a book
3. **Noun:** A strait between two landmasses
4. **Noun:** A unit for counting houses and shops
5. **Noun:** A type or kind
6. **Noun:** Regarding; concerning (as in "در باب فلانی" - about someone)
7. **Noun:** The sultan's court

**Adjective (ص.):**
- Suitable, worthy, fitting
- Customary, common, conventional
- "طبع مطابق" (in accordance with taste)

The entry indicates Arabic origin while documenting multiple semantic domains: physical openings, textual divisions, geographical features, and abstract concepts of appropriateness and convention.
```


### [2026-09-07T18:24:40.428Z] TOOL RESULT

```
=== KLN nose / nasal / nares ===
15462:Derivatives:  froth,  intr.  and  tr.  s.,froth-y,  adj., froth-i-ly,  adv.,  froth-i-ness,  n. frou-frou,  n„  a  rustling.  —  F.,  of  imitative  origin, frounce,  tr.  and  intr.  v.,  to  wrinkle,  curl.  —  ME. frouncen,  ‘to  wrinkle’,  fr.  OF.  frontier  (F .  fr  on¬ cer),  fr.  fronce,  ‘a  wrinkle’,  fr.  Frankish  *hrunkja, ‘wrinkle’,  which  is  rel.  to  ON.  hrukka,  OHG. runza,  ‘wrinkle’.  See  ruck,  ‘crease’,  wrinkle,  and cp.  flounce,  ‘strip  of  material’, frounce,  n.,  a  wrinkle,  curl.  —  OF.  (=  F .)  fronce, fr.  OF.  frontier.  See  frounce,  v. frow,  n.,  a  Dutch  woman;  a  woman.  —  ME. frowe,  fr.  MDu.  vrouwe  (Du.  vrouw),  rel.  to OHG.  frouwa,  MHG.  vrouwe,  G.  Frau,  OS. frua,  ‘woman,  wife’,  ON.  Freyja,  name  of  the goddess  of  love  in  Norse  mythology,  OE.  frea, OHG.  fro,  Goth,  frauja,  ‘lord’.  See  province and  cp.  Frau,  Fraulein,  Frey,  Freya.  Cp.  also the  second  element  in  euphroe. froward,  adj.,  perverse.  —  Lit.  ‘turned  away’; formed  fr.  fro,  with  suff.  -ward.  Cp.  froe. Derivatives:  froward-ly,  adv.,  froward-ness,  n. frown,  intr.  and  tr.  v.  - —  ME.  frounen,  fr.  OF. froignier,  ‘to  knit  one’s  brows’  (whence  F.  ren- frogner,  of  s.m.),  fr.  Gaulish  *frogna,  ‘nostril’. Cp.  W.  ffroen,  ‘nose’.
16931:Gymnorhina,  n,  a  genus  of  birds,  the  piping  crow (ornithol.)  —  ModL,  prop,  ‘having  naked  nos¬ trils’,  compounded  of  gymno-  and  Gk.  ptc, gen.  plvd;,  ‘nose’.  See  rhino-  and  cp.  next  word, gymnorhinal,  adj,  having  naked  nostrils  (said  of crows).  —  See  prec.  word  and  rhinal, gymnosophist,  n,  member  of  a  sect  of  philo¬ sophers  in  ancient  India,  who  walked  naked.  • — L.  gynmosophistae  (pi.),  fr.  Gk.  yj|ivoao9iaTai (pi.),  which  is  compounded  of  yupivop,  ‘naked’, and  the  pi.  of  0091  nxrfi,  ‘philosopher’.  See gymno-  and  sophist.
24982:nares,  n.  pi.,  the  nostrils  ( anat .)  —  L.  nares,  pi.  of naris,  ‘nostril’,  which  stands  for  *nasis  (see  rho¬ tacism),  fr.  I.-E.  base  * nas -,  whence  also  OE. nosu,  ‘nose’.  See  nose  and  cp.  nasal,  nasion, nasturtium,  nasute.
24992:nasal,  adj.,  1)  pertaining  to  the  nose;  2)  uttered through  the  nose  (said  of  sounds).  —  Formed with  adj.  suff.  -al  fr.  L.  nasus,  ‘nose’,  which  is
24993:rel.  to  naris  for  *nasis,  ‘nostril’.  See  nares  and cp.  orinasal.
---
nostril,  n.  —  ME.  nostrill,  nosethirl,  fr.  OE.  nos- pyrl,  lit.  ‘hole  of  the  nose’,  fr.  nosu,  ‘nose’,  and pyrel,  ‘hole’,  fr.  purh,  ‘through’.  See  nose  and
---
nasal,  adj.,  1)  pertaining  to  the  nose;  2)  uttered through  the  nose  (said  of  sounds).  —  Formed with  adj.  suff.  -al  fr.  L.  nasus,  ‘nose’,  which  is
nasal,  adj.,  pertaining  to  the  nose  and  mouth ; (of  sounds)  pronounced  both  through  the  mouth and  nose.  —  Compounded  of  L.  os,  gen.  oris, ‘mouth’,  and  Late  L.  nasalis,  ‘pertaining  to  the nose’.  See  oral  and  nasal.
=== SKT nose ===
NOSED.
```


## [2026-09-07T18:24:58.934Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n 'https://www.etymonline.com/word/narghile' \\\n 'https://www.etymonline.com/word/nostril' \\\n 'https://www.ahdictionary.com/word/search.html?q=narghile' \\\n 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/n%C3%A9h%E2%82%82s-' \\\n 'https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D8%A8' \\\n 'https://en.wiktionary.org/wiki/%D8%A3%D9%86%D8%A8%D9%88%D8%A8' \\\n 'https://en.wiktionary.org/wiki/Babylon' \\\n 'https://en.wikipedia.org/wiki/Babylon' \\\n 'https://vajehyab.com/moein/%D8%A7%D9%86%D8%A8%D9%88%D8%A8' \\\n 'https://abadis.ir/fatofa/%D8%A7%D9%86%D8%A8%D9%88%D8%A8/' \\\n 'https://abadis.ir/fatofa/%D8%A8%D8%A7%D8%A8/' ; do\n  python3 tools/fetch_source.py \"$u\" --note 'page 350 verification (Narikelah/narghile; Nas nose; Semitic n-b-b bab/anbub/Babel)' 2>&1 | tail -2\ndone"
}
```


## [2026-09-07T18:25:01.091Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%86%D8%A7%D8%B1%DA%AF%DB%8C%D9%84",
 "prompt": "Give the Persian etymology of نارگیل (coconut) and of نارگیله if present: source (Sanskrit nārikela?), Middle Persian form, and descendants (Arabic, Turkish, French, English)."
}
```


### [2026-09-07T18:25:06.326Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/4b96143cf56ef561.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/630a8c8fea4af7ae.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e71f6342ee7e3c64.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c0125e499494e3ab.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/7f1acabac44b1497.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/631fc52b940cec6c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/59f562ca50059ee0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8ded83007469818d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/76f2bc5788af47a9.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/62bcfd4a9e5aea36.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9fe2a84ff21575c7.txt
```


### [2026-09-07T18:25:13.284Z] TOOL RESULT

```
# Etymology of نارگیل (Nārgīl)

## Source and Development
The word traces back to Sanskrit **नारिकेल** (nārikela), which passed through **Middle Persian** (ʾnʾlgyl /anārgēl/) before arriving in Modern Persian as نارگیل.

## Descendants
The term spread across multiple languages:

- **Arabic**: نَارْجِيل (nārjīl), نَرْجِيل (narjīl)
  - Subsequently entered **Ottoman Turkish** as نارجیل (narcil) and نارچیل (narçil)
- **Northern Kurdish**: nargîl
- **Ottoman Turkish**: نارگیل (nargil) — direct from Persian
- **Uyghur**: نارجىل (narjil)

## Note on نارگیله
The Wiktionary entry lists نارگیله (nârgile) as a derived term but provides no separate etymology or description beyond its existence as a related word form.

The article does not address French or English etymologies for coconut terms.
```


## [2026-09-07T18:25:29.052Z] TOOL CALL #47: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D9%86%D8%A7%D8%B1%DA%AF%DB%8C%D9%84' --note 'page 350, root Narikelah, Persian nargil MP anargel' 2>&1 | tail -1\npdftoppm -f 350 -l 350 -r 300 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg350 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg350.png"
}
```


### [2026-09-07T18:25:31.334Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/ccc388f04c4c2ac9.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 70743 Sep  7 14:25 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg350.png
```


## [2026-09-07T18:25:34.159Z] TOOL CALL #48: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg350.png"
}
```


### [2026-09-07T18:25:34.657Z] TOOL RESULT

```

```


## [2026-09-07T18:25:34.655Z] INPUT

[Image: original 2550x3300, displayed at 1546x2000. Multiply coordinates by 1.65 to map to original image.]


## [2026-09-07T18:25:49.742Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -o -E \"nose,  n\\.[^|]{0,400}\" KLN_1966.txt | head -2\necho \"=== POK page markers ===\"\npython3 - <<'EOF'\nimport re\nfor f in ['POK_02.txt','POK_full.txt']:\n    try: lines=open(f,encoding='utf-8',errors='replace').read().split('\\n')\n    except: continue\n    idx=[i for i,l in enumerate(lines,1) if re.search(r'\\bnas-\\b',l)]\n    print(f,'hits',idx[:20])\nEOF\necho \"=== POK_full around 61830 for headword ===\"\nsed -n '61826,61838p' POK_full.txt"
}
```


### [2026-09-07T18:25:51.480Z] TOOL RESULT

```
nose,  n.  —  ME.,  fr.  OE.  nosu,  rel.  to  ON.  nos, Norw.  nos,  Dan.  nsese,  Swed.  niisa,  OFris.  nose, MDu.  nose,  nose,  Du.  neus,  OHG.  nasa,  MHG., G.  nase,  and  cogn.  with  OI.  nasa  (dual  nom.), ‘nose’,  prop,  ‘the  two  nostrils’,  OSlav.  nosu, Lith.  ndsis,  ‘nose’,  Lett,  nasis,  OPruss.  nozy,  L. nasus,  ‘nose’,  naris,  for  *nasis,  ‘nostril’.  Cp. naze,  ness,  nostril,  n
nose,  n.,  a  sugar,  C18H33Ola  (chem.)  —  Form¬ ed  with  subst.  suff.  -ose  fr.  F.  raffiner,  ‘to  refine’, fr.  re-  (see  re-)  and  affiner,  ‘to  make  fine’,  which is  formed  fr.  OF.  a,  ‘to’  (fr.  L.  ad),  and  OF.  fin (fr.  VL.  *finus),  ‘fine’.  See  ad-  and  fine,  ‘delicate’, raffle,  n.,  lottery.  —  ME.  rafle,  fr.  MF.  (=  F.) rafle,  ‘a  game  of  dice  (whence  rafter,  
=== POK page markers ===
POK_02.txt hits [6600]
POK_full.txt hits [61837, 61839]
=== POK_full around 61830 for headword ===

which derived from zero grade of Root/ lemma: an(a)-3\ "to breathe' : Root/ lemma: 

ansu-, QSU-\ "ghost, demon': Old Indie asu-, Avestan arjhu-^ breath of life, world '. 

Material: 

Maybe through metathesis alb. Geg {*u-nah) huna, Tosc hundat " nose' from alb. hundof 

insult, make sad ' (common Baltic Slavic Albanian prefix u-). 

Old Indie nas-a, -f, -6h\v\s\x. Lok. Sg., Gen. Du.; nasaHom. Du. "nose' (originally " nostril
```


## [2026-09-07T18:25:57.931Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '61805,61826p' POK_full.txt\necho \"=== search Page(s) near ===\"\nawk 'NR>=61790 && NR<=61880 && /Page|Seite|755/ {print NR\": \"$0}' POK_full.txt\necho \"=== POK_02 line 6600 ===\"\nsed -n '6590,6612p' POK_02.txt | cut -c1-160"
}
```


### [2026-09-07T18:25:59.227Z] TOOL RESULT

```
Material: Old Irish ne/'tm. 'fight, struggle' {*nanth)\ Gothic ana-nanf^Jan' venture, risk', Old 
Icelandic nenna " give one's heart ', (under the influence of common Celtic -ns-, -nt- > -nn- 
), Old High German preterit ginand' have courage ', ginenden. Old Saxon nathian. Old 
English /7eA'5/7 "venture, risk'. Old Icelandic nenninn^ active, keen ', Middle High German 
genende(c)^keev\, eager'. Old High German nand {a\so in names as Ferdinand), Old 
English nodi. " courage '. 
References: WP. II 317. 
Page(s): 755 

Root / lemma: /7a5- nasalized {*neu-s) 

Meaning: nose 

Note: (/755-from the lengthened grade case this conservative stem, originally Nom. Sg.), 

originally probably " nostril ' 

Note: 

Root/ lemma: nas-: nose' derived from Root/ lemma: neu-ks-, neu-s-\ "to sniff, smell' 

=== search Page(s) near ===
61797: Page(s): 754 
61813: Page(s): 755 
61819: Note: (/755-from the lengthened grade case this conservative stem, originally Nom. Sg.), 
61867: Page(s): 755 
=== POK_02 line 6600 ===
WP.  II  316.
nana,  nena  usw.  Lallwort.
Ai.  nanä  , Mutter,  Mütterchen*,  *nanänä  umgebildet  (nach  svasä :  svasr-) zu  nanändar  ,des  Mannes  Schwester*,  np.  nana  ,Mutter*;  gr.  vdvva
WP.  II  317,  WH.  II  175.  1
S.  auch  unter  Sn-.
755
^gjjt-  »wagen,  sich  erkühnen*;  nur  kelt.  und  germ.
^ir.  neit  m.  ,Kampf*  (*nanti-) ;  got.  ana-nanpjan  ,wagenS  aisl.  nenna ^übers  Herz  bringenS  ahd.  Prät.  ginand  ,Mut  wozu  haben',  ginenden,  as
WP.  n  317.
ßas-  ,Nase*  (näs-  aus  den  dehnstufigen  Kasus   dieses  kons.  St.,  ursprüngl. dem  Nom.  Sg.),  ursprüngl.  wohl  ,Nasenloch*.
Ai.   nas-ä,   -2,   -öh  Instr.  Lok.    Sg.,   Gen.    Du.;   näsä  Nom.    Du.    ,Nase* (ursprüngl.   ,Nasenloch*),   sekundär  ndsä  f.   ,Nase',   
WP.  II  318,  WH.  II  143  ff.,  Trautmann  193  f.,  Holthausen  KZ.  69,  166  f., Specht  Idg.  Dekl.  75.
I.  näus-   f.   , Schiff'    (ausgehöhlter    Einbaum);    Akk.    näum,    näuiio-    ,zum Schiff  gehörig*,  näu-ägo-s  , Schiffer*.
Ai.  näu-  (Nom.  näuh)  , Schiff,  Boot'  (nävya-  .schiffbar');  ap.  näviyä , Flotte'  (:  gr.  vriioq  ,zum  Schiff  gehörig');  näväja-  m. , Schi
48*
756
ahd.  nuosc,  mhd.  nuosch  m.  ,Trog,  Rinne',  afries.  nöst  ,Trog'',    mnd.  nöste  i
, Viehtrog',  Wassertrog' ;  hierher  der  lit.   FIN  Nova,  polonis.  Nawa.  -M
WP.  II  315,  WH.  II  148  f.,  J.  Hubschmid  R.  int.  d'Onom.  4,  3  ff.  ^;
2.  näu-  :  nou-  :  nü-   A.  ,Tod,   Leiche',    B.  ,bis   zur   Erschöpfung  abquälen.
ermattet  zusammensinken';  näuis  , Leiche'.  :
A.  Got.  naus  , Leiche*  {ga-nawiströn  , begraben*),  aisl.  när  ds,,  ags.  ntU) m.  ds. ;  aruss.  navh  , Leiche',  aöech.  ndv,  -i  m.  ,Jenseits,  
B.  air.  7iüne  (älter  naunae)  f.,  cymr.  newyn  m.  ^Hungersnot'  (*w9w,mo-)  ;. bret.  naoun  (^ndu^no-)  ds. ;  mcymr.  neued  , Sehnsucht,  Not*  {*n�
```


## [2026-09-07T18:26:07.504Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -E \"neu-ks|nu-ks|neuks\" POK_02.txt | head -5\npython3 - <<'EOF'\nimport re\nlines=open('POK_02.txt',encoding='utf-8',errors='replace').read().split('\\n')\nhits=[i for i,l in enumerate(lines,1) if re.search(r'neu-ks|schnüffeln|riechen',l)]\nfor h in hits[:12]:\n    print(h, lines[h-1][:120])\nmarks=[(i,l.strip()) for i,l in enumerate(lines,1) if re.fullmatch(r'\\s*7[0-9]{2}\\s*',l)]\nprint([m for m in marks if 7000<m[0]<7600][:20])\nEOF"
}
```


### [2026-09-07T18:26:08.847Z] TOOL RESULT

```
581 anord.  kraki ,Sta.nge  mit  Haken;  magere  Person';  ahd.  kräclio  (*krekan-)j kracco  (als  *kraggan-^  Geminationsf
585 Auf  idg.  -k  sicher  anord.  krä  ,Ecke,  Winkel'  (*kraidho)  und  wahrschein- lich auch  die  germ.  Formen  auf  -g
619 4.  s-Erweiterung  *gre-s-,  nur  germ. :  ahd.  kresan  ,kriechen',  nor^ mdartl.  krasen  ,schwach,  hinfällig';  ver
621 »kriechen'.
624 norw.  kryl  ,Buckel'  (*krü-li-?  *krüvila'?),  dial.  auch  ski^yl,  kryla  ,krumm- rückig  sein'  (auch  gryla),  sch
632 ahd.  kriochan  , kriechen',  nhd.  kriechen,  ablaut.  krauchen  ,sich  ducken, schlüpfen,  kriechen',  Krauch  , Wegeb
636 anord.  krjüpa,  ags.  creopan,  mnd.  krüpen  , kriechen'  (,*sich  krümmen wie  ein  Wurm'),  ags.  cryppan  , beugen,
666 Mhd.  krabelen  (mit  expressiver  Verschärfung:  mhd.  krappein,  mnd. krabbelen,  daraus  nhd.  krabbeln)  ,kratzen,  
1045 aksl.  zemlja  ,Erde';  dazu  auch  aksl.  zmhja  , Schlange'  (,auf  der  Erde kriechend,  x-^^H-^^og'),  zmbjb  , Drac
1698 anord.  gräpa  ,grapsen,  an  sich  reißen'  (j>  in  Anlehnung  an  grlpa?), ags.  grsep^ian  , ergreifen',  engl,  gra
1850 ili.  gandh-  .stoßen,  stechen,  verletzen,  zerstören'  (bei  Grammatikern), gandhd-h  m.  .Geruch.  Duft',  av.  gant
2314 g^hre-  , riechen,  wittern,  spüren';  g^hre-ti  ,Riechen'.
[]
```


## [2026-09-07T18:26:16.177Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"Page(s): 768\" POK_full.txt | head -3\npython3 - <<'EOF'\nlines=open('POK_full.txt',encoding='utf-8',errors='replace').read().split('\\n')\nfor i,l in enumerate(lines,1):\n    if 'Page(s): 768' in l:\n        print('---',i)\n        print('\\n'.join(x for x in lines[max(0,i-40):i] if x.strip())[:900])\n        break\nEOF"
}
```


### [2026-09-07T18:26:17.622Z] TOOL RESULT

```
62833:Page(s): 768 
62861:Page(s): 768 
62890:Page(s): 768-769 
--- 62833
zero grade Old Indie asta-, Avestan asta-v\. 'homeland, domicile'; gr. vsopai, Ionian 
VEupai " come happily, return iiome, journey bacl< home ', Negtcjop actually ' the always 
returning ', voaroq m. " iiome coming, returning iiome ', redupl. ep. viao|jai " go, come with' (*vi- 
vG-opai with preservation of -a- after unthematic forms as 2. 3. Sg. *vi-va-aai, -tqi); 
reduced grade vaiw, Fut. vaaaopai 'stay, dwell, inhiabit ', vaiEiau) "stay, dwell, inhiabit; be 
inhabited '; *vaa-F6(;: Doric Thessalian yabc,, lak. vc(Fo(;, Lesbian vauoc, (i.e. vaFFo(;), Ionian 
vr|6c;, Attic vsux; m. "( god's abode =) temple, shrine '; zero grade ao\xzyoc, ' gerettetj 
geborgen '; 
alb. knelem^ recover, be living again ' (prefix k-+ *nes-lo-)\ Gothic ^a-/7/sa/7"gerettet 
become, recover, recuperate ', Old High German Old Saxon g/-nesan ds., Old English ge- 
nesan' are saved, escape, survive ', Gothic ga-
```


## [2026-09-07T18:26:22.509Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nlines=open('POK_full.txt',encoding='utf-8',errors='replace').read().split('\\n')\nfor i,l in enumerate(lines,1):\n    if 62700<i<62950 and ('Root / lemma' in l or 'Root/ lemma' in l or l.strip().startswith('Meaning')):\n        print(i, l.strip()[:110])\nEOF"
}
```


### [2026-09-07T18:26:24.007Z] TOOL RESULT

```
62710 Meaning: man, young man
62734 Root / lemma: ner-2{*he- ner-2)
62735 Meaning: under
62751 Root / lemma: ner-3{*he- ner-3)
62753 Meaning: to conceal, cover, hiding place, hollow
62783 Root / lemma: nes- {*he- nes-)
62785 Meaning: to join with; to conceal oneself
62820 Root / lemma: neu-6^- {*he- neu-dy-)
62822 Meaning: to yearn for smth.
62835 Root / lemma: neu-d- {*he- neu-d-)
62836 Meaning: to acquire, to make use of smth.
62863 Root / lemma: neu-ks-, neu-s- {*he- neu-ks-)
62865 Meaning: to sniff, smell
62869 Root/ lemma: nas-: nose' : Root/ lemma: neu-ks- neu-s-: "to sniff, smell' derived from
62871 zero grade of Root/ lemma: an(a)-3\ "to breathe'.
62892 Root / lemma: neuk- {*he- neuk-)
62894 Meaning: dark, indistinct
62910 Root / lemma: neu-1{*he- neu-f)
62912 Meaning: to call, to praise
62924 Root / lemma: neu-2{*he- neu-2)
62925 Meaning: to make a push; to nod
```


## [2026-09-07T18:26:31.687Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD anargel ===\"; grep -n -i -E \"anārgēl|anargel|anārgel|coconut\" PHD.txt | head -10\necho \"=== NYB ===\"; grep -n -i -E \"anārgēl|anargel|coconut|nārgēl\" NYB*.txt | head -10\necho \"=== PHD bab ===\"; grep -n -E \"^bāb|bāb \" PHD.txt | head -10"
}
```


### [2026-09-07T18:26:31.769Z] TOOL RESULT

```
=== PHD anargel ===
1264:coconut anargél.
=== NYB ===
=== PHD bab ===
```


## [2026-09-07T18:26:36.135Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"anargél\\|anargel\" PHD.txt | head\necho \"=== context ===\"\ngrep -n -B2 -A2 \"anargél\" PHD.txt | head -20"
}
```


### [2026-09-07T18:26:36.190Z] TOOL RESULT

```
1264:coconut anargél.
=== context ===
1262-coarseness stabrih.
1263-cock xrós.
1264:coconut anargél.
1265-coin, small copper ~ pišīz,
1266-cold sard; ~ region sardsēr.
```


## [2026-09-07T18:28:42.834Z] AGENT

All sources gathered. Now writing the verification file.


## [2026-09-07T18:36:07.231Z] TOOL CALL #56: Bash

```json
{
 "command": "cat > /home/sfmqrb/git/rishe/data/verification/page-350.json <<'JSONEOF'\n{\n  \"pdf_page\": 350,\n  \"book_page\": 320,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-07\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Nârikelah, Nârikerah\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"Sanskrit नारिकेल nārikela- / nārikera- (also nālikera-) 'coconut, coconut palm', a word of non-Indo-European (probably Dravidian/Austroasiatic) origin in Sanskrit\",\n      \"note\": \"Root, language label and gloss are all right, and Nourai's own reference is the modern standard for this word: Klein p. 1028 s.v. narghile gives 'OI. nārikerah, nārikelah', adding that the word 'is of uncertain, possibly Dravidian, origin'. AHD's narghile entry has 'Sanskrit nārikelaḥ, nālikeraḥ'; Mo'in's footnote in Borhan-e Qate' p. 2095 gives 'در سانسکریت nârikela، nârikera و نظایر آن' with a reference to Laufer, Sino-Iranica p. 585. The one thing worth stressing is that the Sanskrit word is itself a loan into Indo-Aryan from a South Indian source, so the chart's ROOT is the earliest recoverable form, not an inherited IE root — Nourai does not claim otherwise. Both variants (-kelah / -kerah) are genuine Sanskrit doublets with the usual Indic l/r interchange.\",\n      \"note_fa\": \"ریشهٔ این خانواده سنسکریت nārikela- / nārikera- «نارگیل، درخت نارگیل» است و برچسب زبان و معنای آن در نمودار درست است. کلاین (ص ۱۰۲۸) و فرهنگ AHD همین دو صورت را می‌آورند و هر دو تصریح می‌کنند که خودِ واژه در سنسکریت وام‌واژه است و احتمالاً از زبان‌های دراویدی جنوب هند به سنسکریت رفته است؛ پس این صورت، کهن‌ترین صورت بازیافتنی است نه ریشهٔ هندواروپایی. معین نیز در حاشیهٔ برهان قاطع (ص ۲۰۹۵) به سانسکریت nârikela و nârikera و به Sino-Iranica لوفر ص ۵۸۵ ارجاع می‌دهد. دوگانگی l/r در پایانهٔ واژه ابدال معمول هندی است. ادعای نورایی درست است.\",\n      \"sources\": [\n        \"https://www.ahdictionary.com/word/search.html?q=narghile\",\n        \"https://en.wiktionary.org/wiki/%D9%86%D8%A7%D8%B1%DA%AF%DB%8C%D9%84\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"KLN:1028\", \"status\": \"supports\", \"note\": \"KLN_1966.txt line 24983, printed-page marker '1028' standing at line 24960 immediately above it, so the entry really is on p. 1028: 'narghile, nargile, n., hookah, an Oriental pipe. — Pers. nargil, \\\"coconut tree\\\"; prob. fr. OI. nārikerah, nārikelah, of s.m., which is of uncertain, possibly Dravidian, origin; so called because orig. narghiles were made of coconut shells.' Exactly the chart's root, both variants.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"AHD\", \"where\": \"online entry 'narghile' (= 1975 New College ed. p. 873)\", \"stance\": \"supports\", \"note\": \"'French narghilé, obsolete variant of narguilé, from Persian nārgīleh, from nārgīl, coconut (from which the receptacle was made), from Sanskrit nārikelaḥ, nālikeraḥ.'\"},\n        {\"src\": \"BQT\", \"where\": \"p. 2095 s.v. نارگیل (Mo'in's footnote; vol. 4, pdf p. 178)\", \"stance\": \"supports\", \"note\": \"read from the page image (ocr/BQT/2095.png, saved to 2095.vision.txt): '… در سانسکریت nârikela، nârikera و نظایر آن. Laufe., Sino-Iranica, p.585'.\"},\n        {\"src\": \"LKT\", \"where\": \"no. 1556\", \"stance\": \"partial\", \"note\": \"grep 'nargil' in LKT.txt line 3581: 'Pers. nārgilä: \\\"Wasserpfeife\\\" [angeblich aus sskr. nārikera \\\"Kokosnuß\\\"]' — Lokotsch marks the Sanskrit source 'angeblich' (allegedly), i.e. he reports it without endorsing it.\"},\n        {\"src\": \"HJB\", \"where\": \"s.v. COCO, COCOA, COCOA-NUT, pp. 228-229\", \"stance\": \"supports\", \"note\": \"HJB.txt lines 6834, 6839 quote Friar Jordanus c.1328 'First of these is a certain tree called Nargil …' and John Marignolli c.1350 'Now the Nargil is the Indian Nut' — the Indian word in medieval European travel writing.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"anârgîl\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Sanskrit nārikela- was taken into Middle Persian as ʾnʾlgyl /anārgēl/ — a prothetic a- was prefixed (the same anaptyctic/prothetic vowel MP gives other Indian and Aramaic loans), Indic -k- was voiced to -g- in intervocalic position, and the Indic -l-/-r- vacillation shows in the spelling with l. The form is textually attested: the Sasanian courtly text Xusrō ī Kawādān ud Rēdak-ē §50 lists 'anārgēl kē abāg šakar xwarēnd' ('coconut, which they eat with sugar'), and the text itself notes that the fruit is called anārgēl 'in Indian' but kōz ī hindūg ('Indian nut') 'in Pārsīg' — i.e. anārgēl was still felt to be the foreign trade word in late Sasanian times, spread by the Indian Ocean trade of the 6th-7th c. MacKenzie's index gives 'coconut anārgēl'.\",\n          \"derivation_fa\": \"واژهٔ سنسکریت nārikela- در فارسی میانه به صورت anārgēl (نوشتار پهلوی ʾnʾlgyl) وام گرفته شده است: یک «الف» آغازین (واکهٔ پیش‌افزوده) بر سر واژه افزوده شد، ک هندی در میان دو واکه به گ نرم شد، و ابدال l/r هندی در نوشتار با «ل» بازتاب یافته است. این صورت در متن پهلوی «خسرو کواتان و ریدکی» بند ۵۰ آمده است: «انارگیل که با شکر خورند»، و همان متن می‌افزاید که این میوه را به زبان هندو «انارگیل» و به پارسیگ «کوچ هندوک» می‌خواندند؛ یعنی در پایان دورهٔ ساسانی هنوز واژه‌ای بیگانه و بازرگانی شمرده می‌شد. مکنزی نیز در فرهنگ کوچک پهلوی خود anārgēl را برای «نارگیل» ثبت کرده است. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D9%86%D8%A7%D8%B1%DA%AF%DB%8C%D9%84\"],\n          \"ref_check\": [\n            {\"ref\": \"PLA:256\", \"status\": \"supports\", \"note\": \"Asbaghi, Persische Lehnwörter im Arabischen: incoming/PLA/PLA_pages.txt line 14376 'nargil: \\\"Kokosnuß\\\" … pers. närgil … mp. anärgil'; the running head 'närgila 257 …' appears a few lines below (line ~14388), so this entry stands on p. 256 exactly as Nourai cites. Asbaghi's footnote 5 on the same page is 'Bartholomae S. 1186'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"English-Pahlavi index s.v. coconut\", \"stance\": \"supports\", \"note\": \"grep 'anargél' in PHD.txt line 1264: 'coconut anargél.' — MacKenzie's Concise Pahlavi Dictionary attests the MP word.\"},\n            {\"src\": \"BQT\", \"where\": \"p. 2095 s.v. نارگیل (Mo'in's footnote)\", \"stance\": \"supports\", \"note\": \"read from the page image: 'نارگیل ـ بکسر کاف، پهلوی anârgil «اونوالا ص ۲۲۷»، معرب آن نارجیل «نفس» و نارجیله «دزی ج ۲ ص ۶۳۱». در نامهٔ پهلوی خسروکواتان بند ۵۰ آمده: «انارگیل که با شکر خورند …»' — Pahlavi form, its source (Unvala p. 227) and the Pahlavi attestation, i.e. Nourai's arrow in full.\"},\n            {\"src\": \"MON\", \"where\": \"en.wiktionary Persian نارگیل (citing Hasandust and MacKenzie)\", \"stance\": \"supports\", \"note\": \"'From Sanskrit नारिकेल (nārikela), through Middle Persian ʾnʾlgyl /anārgēl/' — same prothetic-a form.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"nârgîl «نارگیل»; nârgîleh «نارگیله»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"MP anārgēl > NP نارگیل nārgīl by loss of the prothetic a- (aphaeresis, as in MP ahangar/NP āhangar-type simplifications of unstressed initial syllables) and the regular MP ē > NP ī. نارگیله nārgīleh is the NP derivative in -eh, 'the thing made of a nārgīl', because the water reservoir of the pipe was originally a coconut shell — Devic quotes Quatremère to exactly that effect, and in the Syrian pipe the glass flask still replaced a coconut. Arabic borrowed both members with g > j: نارجيل nārjīl and نارجيلة nārjīla (Mo'in's footnote cites Dozy II 631 for the latter; Asbaghi p. 256-257 treats both as Persian loans in Arabic), and Ottoman Turkish took nargile straight from Persian.\",\n          \"derivation_fa\": \"«نارگیل» از فارسی میانهٔ anārgēl است: الف آغازین در فارسی نو افتاده (کاهش هجای بی‌تکیهٔ آغازی) و ē فارسی میانه به ی فارسی نو بدل شده است. «نارگیله» ساختی فارسی نو با پسوند «ـه» است، یعنی «آنچه از نارگیل ساخته شده»، زیرا مخزنِ آبِ این قلیان در آغاز پوستِ سختِ نارگیل بود؛ دویک از قول کاترمر همین را می‌گوید. عربی هر دو را با ابدال گ به ج گرفته است: نارجیل و نارجیله (معین در حاشیهٔ برهان به دزی ج ۲ ص ۶۳۱ ارجاع می‌دهد و اصباغی هم آن‌ها را وام‌واژهٔ فارسی در عربی می‌شمارد)، و ترکی عثمانی صورت nargile را یک‌راست از فارسی گرفته است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.ahdictionary.com/word/search.html?q=narghile\",\n            \"https://en.wiktionary.org/wiki/%D9%86%D8%A7%D8%B1%DA%AF%DB%8C%D9%84\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD:873\", \"status\": \"supports\", \"note\": \"the AHD narghile entry (New College ed. 1975 p. 873; checked in the current online AHD) reads '… from Persian nārgīleh, from nārgīl, coconut (from which the receptacle was made), from Sanskrit nārikelaḥ, nālikeraḥ' — both Persian words and their relation, as drawn.\"},\n            {\"ref\": \"BQT:2095\", \"status\": \"supports\", \"note\": \"Borhan-e Qate' p. 2095 (vol. 4, pdf p. 178), Mo'in's footnote to نارگیل: Pahlavi anârgil, 'معرب آن نارجیل … و نارجیله'; the body of the entry defines نارگیل as Cocos nucifera. Page image and my reading saved to data/verification/sources/refs/ocr/BQT/2095.png and 2095.vision.txt.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"Farhang-e Farsi s.v. نارگیل (MON_part2.txt line 71754 ff.)\", \"stance\": \"supports\", \"note\": \"'نارگیل: (اِ) [= معر. نارجیل] (گیا.) درختی است از تیرهٔ نخل‌ها …' — Mo'in gives the Arabicized doublet نارجیل and the botanical description; he does not repeat the Sanskrit etymology here (that is in his Borhan footnote).\"},\n            {\"src\": \"PLA\", \"where\": \"p. 257 s.v. نارجيلة\", \"stance\": \"supports\", \"note\": \"PLA_pages.txt line ~14392: 'närgila: \\\"pers. Wasserpfeife\\\" ← skr. narikera, engl. nargula, frz. narguile. Nargileh — skr. > pers. > tk. > dtsch.' — Asbaghi has the water-pipe sense as the Persian derivative and traces the European words to it.\"},\n            {\"src\": \"LKT\", \"where\": \"no. 1556\", \"stance\": \"supports\", \"note\": \"LKT.txt lines 3581-3582: 'Pers. nārgilä: \\\"Wasserpfeife\\\" … hieraus engl. nargula, nargileh, narghile; frz. narguilé, kat. nargili, sp. narguile, rum. narghilea; poln. nargile. [Eguilaz 463, ML 5823a, Hobson-Jobson 618]'.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"French\",\n          \"words\": \"narguile\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"French borrowed Persian nārgīleh in the first decades of the 19th c., largely through Levantine and Ottoman contact (Turkish nargile), in the spellings narguilé and narghilé; AHD treats narghilé as an obsolete variant of narguilé. Devic (1876) s.v. 'Narghileh ou Narguilé. Pipe orientale' derives it, after Quatremère, 'du persan nârghil, cocotier, noix de coco', explaining that the bowl holding the tobacco was made of, or shaped like, a coconut; Pihan (1866) has the same headword. Note that Nourai prints the French without its accent (narguile); the French word is narguilé/narghilé.\",\n          \"derivation_fa\": \"فرانسوی این واژه را در دهه‌های آغازین سدهٔ نوزدهم، بیشتر از راه شام و ترکی عثمانی (nargile)، از فارسی «نارگیله» گرفته و به صورت narguilé و narghilé نوشته است؛ فرهنگ AHD صورت narghilé را گونهٔ کهنهٔ narguilé می‌داند. دویک (۱۸۷۶) به نقل از کاترمر می‌نویسد این واژه «از فارسی nârghil یعنی درخت نارگیل و میوهٔ آن» است، زیرا کاسهٔ تنباکو از پوست نارگیل ساخته می‌شد؛ پیان (۱۸۶۶) نیز همان سرواژه را دارد. تنها نکته این‌که نورایی صورت فرانسوی را بی‌علامتِ حرکت (narguile) چاپ کرده و صورت درست narguilé است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.ahdictionary.com/word/search.html?q=narghile\",\n            \"https://www.etymonline.com/word/narghile\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD:873\", \"status\": \"supports\", \"note\": \"AHD s.v. narghile: 'French narghilé, obsolete variant of narguilé, from Persian nārgīleh' — the French node and its Persian parent exactly as drawn.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"DEV\", \"where\": \"p. ~207 s.v. Narghileh ou Narguilé (DEV.txt line 1833; cross-reference at line 4032)\", \"stance\": \"supports\", \"note\": \"'Narghileh ou Narguilé. Pipe orientale. D'après Et. Quatremère, du persan nârghil, cocotier, noix de coco. … parce que la capsule qui renferme le tabac est formée d'une noix de coco ou, du moins, en a la figure.'\"},\n            {\"src\": \"PHN\", \"where\": \"s.v. NARGUILEH (PHN.txt lines 7921, 7929; index line 10771 gives p. 284)\", \"stance\": \"supports\", \"note\": \"Pihan lists NARGUILEH as a French word of Persian origin and says 'narguileh vient de [nārgīl] cocotier'.\"},\n            {\"src\": \"LKT\", \"where\": \"no. 1556\", \"stance\": \"supports\", \"note\": \"'… frz. narguilé, kat. nargili, sp. narguile, rum. narghilea' — the Romance forms all from the Persian, with the French among them.\"},\n            {\"src\": \"LAM\", \"where\": \"s.v. Narghileh ou Narguilé (LAM.txt line 5652)\", \"stance\": \"supports\", \"note\": \"grep 'Narguil' in LAM.txt: 'Narghileh ou Narguilé. Ce mot est proprement d'o[rigine persane]…' — Lammens lists it among the French words of Oriental origin.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"English\",\n          \"words\": \"nargeela, narghile\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"For narghile/nargile the chart's route is the standard one: English took the word from French narghilé about 1820 (Etymonline: 'oriental water pipe for smoking', by 1820, from French narghileh, from Persian nargileh). The other form, nargeela, is not French at all but an Anglo-Indian transcription of the Persian/Urdu word taken directly in India — Hobson-Jobson uses 'Nargil, or nargeela' for the coconut itself (HJB, in the Cosmas passage: 'The Argell (i.e. Nargil, or nargeela, or coco-nut) is at first full of very sweet water'). And Nourai's own reference for the English, Klein, does NOT route the word through French: Klein p. 1028 derives 'narghile, nargile' straight from 'Pers. nargil', as does Lokotsch ('hieraus engl. nargula, nargileh, narghile'). So the node is right about the words and about the ultimate source, but the single French→English arrow is an over-simplification for one of the two forms and is not what Klein/Lokotsch say.\",\n          \"derivation_fa\": \"برای صورت narghile/nargile مسیر نمودار همان مسیر پذیرفته‌شده است: انگلیسی این واژه را نزدیک ۱۸۲۰ از فرانسویِ narghilé گرفته است (اتیمولاین). اما صورت nargeela فرانسوی نیست، بلکه آوانگاری انگلیسی-هندی همان واژهٔ فارسی/اردوست که یک‌راست در هند وام گرفته شد؛ در Hobson-Jobson «Nargil یا nargeela» به معنی خودِ نارگیل به کار رفته است. افزون بر این، مرجعی که نورایی برای این گره می‌آورد (کلاین) واژه را از راه فرانسوی نمی‌آورد و narghile را یک‌راست از «فارسی nargil» می‌گیرد؛ لوکوچ نیز همین‌گونه. پس گره در واژه‌ها و در سرچشمهٔ نهایی درست است، ولی یگانه پیکانِ فرانسوی←انگلیسی برای یکی از دو صورت ساده‌سازی است: با احتیاط پذیرفتنی است.\",\n          \"sources\": [\"https://www.etymonline.com/word/narghile\"],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the book gives no reference for this node; the parent node's AHD:873 and the root's KLN:1028 were checked instead (they disagree with each other about the French link, see derivation).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"p. 1028 s.v. narghile, nargile\", \"stance\": \"partial\", \"note\": \"'narghile, nargile, n., hookah, an Oriental pipe. — Pers. nargil, \\\"coconut tree\\\"' — Klein has the English straight from Persian, with no French intermediary.\"},\n            {\"src\": \"AHD\", \"where\": \"online entry 'narghile' (1975 ed. p. 873)\", \"stance\": \"supports\", \"note\": \"'French narghilé, obsolete variant of narguilé, from Persian nārgīleh' — the French route Nourai draws.\"},\n            {\"src\": \"LKT\", \"where\": \"no. 1556\", \"stance\": \"partial\", \"note\": \"'hieraus engl. nargula, nargileh, narghile' — English derived from the Persian directly, the French forms listed as parallel borrowings, not as the English word's parent.\"},\n            {\"src\": \"HJB\", \"where\": \"quotation of Cosmas (HJB.txt line 20998); index 'Nargeela'\", \"stance\": \"supports\", \"note\": \"'The Argell (i.e. Nargil, or nargeela, or coco-nut) is at first full of very sweet water' — nargeela as an Anglo-Indian spelling of the Persian/Indian word.\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 2,\n      \"root\": \"Nas\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *néh₂s- (older notation *nas-/*nās-) 'nose', originally probably 'nostril' — a consonant-stem root noun; Pokorny 755\",\n      \"note\": \"Root, language label and gloss are all correct, and Nourai's two page numbers are both right: Pokorny p. 755 has 'ṇas- \\\"Nase\\\" (nās- aus den dehnstufigen Kasus dieses kons. St., ursprüngl. dem Nom. Sg.), ursprüngl. wohl \\\"Nasenloch\\\"', and p. 768(-769) has 'neu-ks-, neu-s- \\\"to sniff, smell\\\"', which Pokorny's own note connects to nas-. Watkins prints the same pair of references at the foot of his nas- article ('[Pok. nas- 755, neu-ks 768]'), so Nourai's citation is in fact copied from a standard source. Modern reconstruction writes the root with a laryngeal, *néh₂s (Wiktionary, after Beekes/NIL), and debates whether the final -s- is part of the root or a suffix; that is a notational refinement, not a disagreement. One layout observation: on the printed page the Avestan/Old Persian box has an arrow running to an EMPTY box at the top right of the chart, which the extraction (rightly) does not represent as a node.\",\n      \"note_fa\": \"ریشهٔ هندواروپایی *néh₂s- (در نگارش کهن‌تر *nas-/*nās-) «بینی» و در اصل «سوراخ بینی»، یک ستاک صامتیِ اسمی است؛ پوکورنی ص ۷۵۵. هر دو شمارهٔ صفحه‌ای که نورایی می‌دهد درست است: ص ۷۵۵ خودِ ریشهٔ nas- است و ص ۷۶۸ (تا ۷۶۹) ریشهٔ neu-ks-, neu-s- «بو کشیدن» که پوکورنی خود آن را با nas- پیوند می‌دهد؛ واتکینز در پایان مقالهٔ nas- همین دو ارجاع را چاپ کرده است، پس ارجاع نورایی از منبعی معیار گرفته شده. ریشه‌شناسی امروزی ریشه را با حنجره‌ای می‌نویسد و در این‌که -s- پایانی جزء ریشه است یا پسوند، اختلاف نظر دارد؛ این تفاوتِ نگارش است نه تفاوتِ حکم. ادعای نورایی درست است.\",\n      \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/n%C3%A9h%E2%82%82s-\"],\n      \"ref_check\": [\n        {\"ref\": \"POK:755\", \"status\": \"supports\", \"note\": \"POK_02.txt: the printed page marker '755' stands at line 6600 and the article follows immediately at line 6604: 'ṇas- ,Nase* (näs- aus den dehnstufigen Kasus dieses kons. St., ursprüngl. dem Nom. Sg.), ursprüngl. wohl ,Nasenloch*. Ai. nas-ā … WP. II 318'.\"},\n        {\"ref\": \"POK:768\", \"status\": \"supports\", \"note\": \"POK_full.txt line 62863: 'Root / lemma: neu-ks-, neu-s- … Meaning: to sniff, smell', with 'Page(s): 768-769' at line 62890, and the note at line 62869 'Root/lemma: nas- \\\"nose\\\" : Root/lemma: neu-ks- neu-s- \\\"to sniff, smell\\\"' — the second page of Nourai's citation is the root Pokorny links nas- to.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. nas-\", \"stance\": \"supports\", \"note\": \"AHD_watkins1985.txt line 770: 'nas-. Nose. 1. Germanic zero-grade form *nusō in Old English nosu … 3. Lengthened-grade form *nās- … [Pok. nas- 755, neu-ks 768.]'\"},\n        {\"src\": \"IEC\", \"where\": \"Mann col. 11536\", \"stance\": \"supports\", \"note\": \"'nas- (nās-) \\\"nose, nostril\\\". WP II, 318 … Skt. nas, f. id.; OHG nasa … Av. nāh- \\\"nose\\\"; OPers nāham, id.; Lat. nārēs … nāsus' — the same root with the same descendants, referring to Walde-Pokorny II 318.\"},\n        {\"src\": \"SYN\", \"where\": \"Buck 4.23 NOSE (SYN.txt lines 5907, 5912)\", \"stance\": \"supports\", \"note\": \"'Walde-P. 2.318. Ernout-M. 653, 659 … Lat. nasus …; OE nosu, nasu, OHG nasa, etc., general Gmc.; Lith. nosis … Skt. nas-, nās- (in RV only dual …), Av., OPers. nah- … The meaning \\\"nostril\\\" is implied by the early use of dual or pl. forms.'\"},\n        {\"src\": \"WLD\", \"where\": \"Bd. II 318\", \"stance\": \"not_available\", \"note\": \"only the 1932 Register volume (WLD_band3.txt) is on disk; Bd. II p. 318 is the locus both Mann and Buck cite for this root, so its content is known at second hand but was not read directly.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan / Old Persian\",\n          \"words\": \"nâh, nâham\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"PIE *néh₂s- gives Proto-Iranian *nāh- : Indo-Iranian *s became *h in Iranian (the regular Ir. s > h, as in *asura > ahura), so the Indic nās- corresponds to Avestan nāh-, whose oblique stem is naṅhan- (Bartholomae s.v. 'nanhan- m. \\\"Nase\\\" des Menschen'). Old Persian has the accusative singular nāham, attested twice in the Bisitun inscription (DB 2.74 and 2.88f.) in Darius' formula about mutilating captured rebels — 'I cut off his nose and ears and tongue, and put out one eye'. Kent classes nāh- among the OP -s- stems (§185.IV). The word did not survive into Middle/New Persian in this shape (NP bīnī is a different formation), so the chart correctly stops at Old Iranian.\",\n          \"derivation_fa\": \"ریشهٔ هندواروپایی *néh₂s- در ایرانی به *nāh- بدل شده است: s هندوایرانی در ایرانی باستان به h تبدیل می‌شود (همان دگرگونی که *asura را به ahura می‌رساند)؛ از این‌رو در برابر nās- سنسکریت، اوستایی nāh- را داریم که ستاک غیرفاعلی آن naṅhan- است (بارتولومه: «nanhan- نامِ بینیِ انسان»). در پارسی باستان صورت رایی nāham دو بار در سنگ‌نوشتهٔ بیستون (DB ۲٫۷۴ و ۲٫۸۸) در همان عبارتِ بریدنِ «بینی و گوش و زبان» شورشیان آمده است؛ کنت آن را در شمار ستاک‌های -s- پارسی باستان می‌آورد. این واژه در فارسی میانه و نو دنبالهٔ مستقیم ندارد (فارسی «بینی» ساختی دیگر است)، پس درست است که نمودار در همین لایه می‌ایستد. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/n%C3%A9h%E2%82%82s-\"],\n          \"ref_check\": [\n            {\"ref\": \"KNT:193\", \"status\": \"supports\", \"note\": \"KNT.txt line 5605, between the printed page markers '193' (line 5598) and the next: 'nāh- sb. \\\"nose\\\": Av. nāh-, Skt. nās-, Lt. nārēs, NEng. nose, pIE *nās- (§110, §142). nāham a.sm. (§1181, §185.IV) DB 2.74, 88f.' — both of Nourai's forms, with the Avestan cognate, on the cited page.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"col. ~1080 s.v. nanhan- (BRT.txt line 19100, between the col. markers 1078 and 1084)\", \"stance\": \"supports\", \"note\": \"'j. nanhan- m. \\\"Nase\\\" des Menschen … Pd. (dRn.): nāk, vīnīk. — Oder zu nāh-' — Bartholomae's Avestan entry, with the Pahlavi glosses.\"},\n            {\"src\": \"KNT\", \"where\": \"§110 (p. 40) and §143 (p. 60)\", \"stance\": \"supports\", \"note\": \"KNT.txt line 1381 'pIE *nās- \\\"nose\\\", OP acc. nāham, Skt. nās-, Eng. nose' and line 2199 'IV. The remaining -s- stems of OP are nāh- \\\"nose\\\", tauviyah- …' — the grammar sections behind the lexicon entry.\"},\n            {\"src\": \"SYN\", \"where\": \"Buck 4.23\", \"stance\": \"supports\", \"note\": \"'Av., OPers. nah- (sg. and dual in Av., sg. in OPers.)' — Buck confirms the Old Iranian pair and the dual usage.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Sanskrit\",\n          \"words\": \"nas\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Vedic nas- 'nose' continues the PIE consonant stem unchanged in Indic, where inherited *s is kept (against Iranian h): in the Rigveda it appears only in the dual — nom. du. nāsā, gen./loc. nasoḥ — i.e. 'the two nostrils', which is why Pokorny takes 'nostril' to be the older sense; a secondary ā-stem nāsā f. 'nose' and derivatives nastaḥ 'of the nose', nāsikā 'nostril' follow later. The lengthened grade nās- of the strong cases is the source of Latin nāsus and of the Avestan/OP long vowel.\",\n          \"derivation_fa\": \"«nas-» سنسکریت همان ستاک صامتیِ هندواروپایی است که در هندی، برخلاف ایرانی، s آغازینِ پایانه را نگه داشته است. در ریگ‌ودا تنها به صورت مثنی به کار رفته است — نهادیِ مثنی nāsā و اضافیِ nasoḥ، یعنی «دو سوراخ بینی» — و همین است که پوکورنی و باک معنای کهن‌تر را «سوراخ بینی» می‌دانند؛ سپس‌تر ستاک ثانویِ nāsā «بینی» و مشتقاتی چون nastaḥ و nāsikā ساخته شده است. صورتِ کشیدهٔ nās- در حالت‌های قوی، سرچشمهٔ nāsus لاتین و واکهٔ بلندِ اوستایی و پارسی باستان است. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/n%C3%A9h%E2%82%82s-\"],\n          \"ref_check\": [\n            {\"ref\": \"KNT:193\", \"status\": \"supports\", \"note\": \"same Kent entry, p. 193: 'nāh- sb. \\\"nose\\\": Av. nāh-, Skt. nās-, …' — Kent gives the Sanskrit cognate on the cited page (with the lengthened-grade spelling nās-).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"p. 755 s.v. nas-\", \"stance\": \"supports\", \"note\": \"POK_full.txt line 61837: 'Old Indic nas-a, -f, -oḥ Instr. Lok. Sg., Gen. Du.; nāsā Nom. Du. \\\"nose\\\" (originally \\\"nostril\\\"), secondary nāsā f. \\\"nose\\\", nas-taḥ \\\"of the nose\\\", nasya- \\\"located at the nose\\\", … nāsikā \\\"nostril, nose\\\"'.\"},\n            {\"src\": \"IEC\", \"where\": \"Mann col. 11536\", \"stance\": \"supports\", \"note\": \"'Skt. nas, f. id. … (with long vowel) Skt. nas, f. dual. \\\"nose, nostrils\\\"; nāsā, f. id.'\"},\n            {\"src\": \"SYN\", \"where\": \"Buck 4.23\", \"stance\": \"supports\", \"note\": \"'Skt. nas-, nās- (in RV only dual, nom. nāsā, gen. nasos)' — with Buck's discussion of 'nostril' vs 'nose' as the older meaning.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Germanic\",\n          \"words\": \"nasô\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Proto-Germanic *nasō f. 'nose' is a well-attested continuation of the root: OHG nasa, MHG/G Nase, Old Norse nǫs (pl. nasar, nasir) 'nostril, nose', Old Frisian nose, MDu. nose. The form is built on the full/lengthened grade *nas-/*nās- with the Germanic ō-stem ending, and beside it Germanic has (a) a zero-grade *nusō (OE nosu, Du. neus) and (b) a ja-stem *nasja- 'headland, ness' (OE næss, ON nes). Watkins in fact quotes the zero grade rather than *nasō, so the cited AHD supports the root but not this exact reconstruction; the form itself is standard (cf. Kroonen, Pokorny p. 755 'ahd. nasa … aisl. nǫs').\",\n          \"derivation_fa\": \"*nasō ژرمنی آغازین «بینی» دنبالهٔ پذیرفته‌شدهٔ همین ریشه است: nasa در آلمانی علیای باستان، Nase در آلمانی، nǫs (جمع nasar) در نورس باستان و nose در فریزی باستان. این صورت بر پایهٔ درجهٔ کاملِ *nas-/*nās- با پایانهٔ ō-ستاکِ ژرمنی ساخته شده است؛ در کنارش ژرمنی صورتِ درجهٔ صفرِ *nusō (انگلیسی باستان nosu، هلندی neus) و ستاکِ *nasja- «دماغه، زبانهٔ خشکی» (næss انگلیسی باستان، nes نورسی) را هم دارد. نکته این‌که واتکینز در AHD به‌جای *nasō همان درجهٔ صفر را می‌آورد؛ پس مرجعِ یادشده ریشه را تأیید می‌کند نه بازساختِ دقیقِ این گره را. خودِ صورت اما معیار است (پوکورنی ص ۷۵۵). ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/n%C3%A9h%E2%82%82s-\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"Watkins 1985 s.v. nas- gives 'Germanic zero-grade form *nusō in Old English nosu' and 'Germanic nasja- in Old English ness', i.e. it does not print *nasō; the Germanic descent from *nas- is nevertheless exactly what AHD asserts.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"p. 755 s.v. nas-\", \"stance\": \"supports\", \"note\": \"POK_full.txt lines 61845-61850: 'ablaut. Old High German nasa \\\"nose\\\"; Old Norse nǫs f. \\\"nostril, nose, projecting cliff\\\"; Old English nasu \\\"nose\\\" (presumably Dual \\\"both nostrils\\\") … (Germanic *nasja-)'.\"},\n            {\"src\": \"KLN\", \"where\": \"s.v. nose\", \"stance\": \"supports\", \"note\": \"'nose, n. — ME., fr. OE. nosu, rel. to ON. nos, Norw. nos, Dan. næse, Swed. näsa, OFris. nose, MDu. nose, Du. neus, OHG. nasa, MHG., G. nase, and cogn. with OI. nāsā … L. nasus' — the Germanic set Nourai's *nasō stands for.\"},\n            {\"src\": \"IEC\", \"where\": \"Mann col. 11536\", \"stance\": \"supports\", \"note\": \"'OHG nasa, sf. id.; OE nosu, f. id. beside næss … ON nǫs, pl. nasar, nasir \\\"nose, nostril\\\"' — the same double ablaut picture.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"English\",\n          \"words\": \"nose, nostril\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"English nose goes back to OE nosu > ME nose, and nostril to OE nosþyrl, literally 'nose-hole', a compound of nosu and þyrel 'hole' (from þurh 'through'), which became ME nosethirl/nostrill and then nostril once the second element was no longer understood. Both words therefore do descend from the root, but OE nosu reflects the Germanic ZERO grade *nusō, not the *nasō of the parent box (Watkins and Etymonline both give *nusō/*nuso- for OE nosu), so the arrow #3 → #4 skips an ablaut difference. Nourai's reference here is also weak: Kent p. 193 merely lists 'NEng. nose' as a cognate in an Old Persian lexicon entry; it says nothing about the Germanic history.\",\n          \"derivation_fa\": \"«nose» انگلیسی از nosu انگلیسی باستان و آن‌گاه nose در انگلیسی میانه است، و «nostril» از nosþyrl انگلیسی باستان یعنی «سوراخِ بینی»، ترکیبی از nosu و þyrel «سوراخ» (از þurh «از میان»)، که در انگلیسی میانه nosethirl شد و پس از تاریک‌شدنِ جزء دوم به nostril رسید. پس هر دو واژه از همین ریشه‌اند، ولی nosu انگلیسی باستان بازتابِ درجهٔ صفرِ ژرمنیِ *nusō است نه *nasō که در جعبهٔ مادر آمده است (واتکینز و اتیمولاین هر دو *nusō را می‌آورند)؛ یعنی پیکانِ ۳←۴ یک تفاوتِ ابلاوت را نادیده می‌گیرد. ارجاع نورایی هم سست است: کنت در ص ۱۹۳ تنها «nose» انگلیسی را در فهرست هم‌ریشه‌های یک مدخلِ پارسی باستان نام می‌برد. با احتیاط پذیرفتنی است.\",\n          \"sources\": [\"https://www.etymonline.com/word/nostril\"],\n          \"ref_check\": [\n            {\"ref\": \"KNT:193\", \"status\": \"partial\", \"note\": \"Kent p. 193 s.v. nāh- has only 'NEng. nose' in a cognate list; the page is not a source for the English forms' history, and it does not mention nostril at all.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"s.v. nose and s.v. nostril\", \"stance\": \"supports\", \"note\": \"'nostril, n. — ME. nostrill, nosethirl, fr. OE. nosþyrl, lit. \\\"hole of the nose\\\", fr. nosu, \\\"nose\\\", and þyrel, \\\"hole\\\", fr. þurh, \\\"through\\\"'.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. nas-\", \"stance\": \"supports\", \"note\": \"'Germanic zero-grade form *nusō in Old English nosu, nose: NOSE, (NUZZLE); NOSTRIL' — both English words listed under the root, from the zero grade.\"},\n            {\"src\": \"FSD\", \"where\": \"grep 'nostril' in FSD_vol1..4\", \"stance\": \"silent\", \"note\": \"Funk & Wagnalls volumes on disk (FSD_vol1-4.txt) returned no usable entry for nose/nostril with the greps 'narghile|nargile' and 'nostril'; not consulted further.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Latin\",\n          \"words\": \"nâsus\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Latin nāsus 'nose' comes from the lengthened grade *nās- (generalized from the strong cases of the root noun) with an expressive geminate -ss- — Pokorny prints 'nāsum n. (altlat.) und nās(s)us m. \\\"Nase\\\" (expressives ss)'. Beside it stands nāris (mostly plural nārēs, -ium) 'nostril(s)' from *nāsis, with the intervocalic -s- > -r- rhotacism of the 4th c. BCE; Klein s.v. nares notes exactly this ('naris, which stands for *nasis, see rhotacism'). Watkins puts both under the lengthened grade, which is what Nourai's 'AHD' reference points to.\",\n          \"derivation_fa\": \"nāsus لاتین «بینی» از درجهٔ کشیدهٔ *nās- است — همان صورتی که از حالت‌های قوی ستاک به همهٔ صرف تعمیم یافته — با مشدّدشدنِ تأکیدیِ -ss-؛ پوکورنی می‌نویسد «nāsum (لاتین کهن) و nās(s)us، با ss تأکیدی». در کنار آن nāris و بیشتر جمعِ nārēs «سوراخ‌های بینی» از *nāsis است، با ابدالِ s میان‌واکه‌ای به r (روتاسیسم سدهٔ چهارم پیش از میلاد)؛ کلاین نیز در مدخل nares همین را می‌گوید. واتکینز هر دو را زیر همان درجهٔ کشیده می‌آورد و ارجاع «AHD» نورایی به همین بند است. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/n%C3%A9h%E2%82%82s-\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. nas-: '3. Lengthened-grade form *nās-, in: a. Latin nāris, nostril: NARES; b. expressive form *nāss- in Latin nāsus, nose: NASAL, NASO-; NASTURTIUM, PINCE-NEZ.'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"p. 755 s.v. nas-\", \"stance\": \"supports\", \"note\": \"POK_full.txt lines 61841-61843: 'Latin nāris, mostly Pl. -es, -ium \\\"nostril\\\" (i-stem has changed to; Akk. Sg. Pl. still conservative form); nāsum n. (Old Latin) and nās(s)us m. \\\"nose\\\" (expressives ss); [common Latin Germanic -s- > -r-]'.\"},\n            {\"src\": \"KLN\", \"where\": \"p. 1028 s.v. nares (and nasal)\", \"stance\": \"supports\", \"note\": \"'nares, n. pl., the nostrils (anat.) — L. nares, pl. of naris, \\\"nostril\\\", which stands for *nasis (see rhotacism), fr. I.-E. base *nas-, whence also OE. nosu, \\\"nose\\\".'\"},\n            {\"src\": \"IEC\", \"where\": \"Mann col. 11536\", \"stance\": \"supports\", \"note\": \"'Lat. nārēs, gp: -ium, f. \\\"nose, nostrils\\\" beside (dialectal) nāsus, gs: -ī, m. \\\"nose\\\", whence It. naso'.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"English\",\n          \"words\": \"nasal, naso-\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"nasal is a learned formation on Latin nāsus: Medieval Latin nāsālis 'of the nose' (used first of the nose-piece of a helmet and in grammar) entered English in the 17th c. through French/scholarly Latin — Klein describes it as 'Formed with adj. suff. -al fr. L. nasus, \\\"nose\\\"'. naso- is the modern anatomical combining form of the same Latin noun (nasopharynx, nasolacrimal). Watkins lists both, NASAL and NASO-, under the Latin branch of nas-, which is precisely the arrow drawn.\",\n          \"derivation_fa\": \"«nasal» ساختی عالمانه بر پایهٔ nāsus لاتین است: صفت nāsālis در لاتینِ سده‌های میانه «مربوط به بینی» (نخست دربارهٔ محافظِ بینیِ کلاه‌خود و در دستور زبان) و سپس در سدهٔ هفدهم از راه فرانسوی و لاتینِ علمی به انگلیسی رسیده است؛ کلاین آن را «ساخته از nasus لاتین با پسوند -al» می‌داند. «naso-» هم صورتِ ترکیبیِ همان اسمِ لاتین در کالبدشناسی امروز است (nasopharynx و مانند آن). واتکینز هر دو را زیر شاخهٔ لاتینیِ nas- می‌آورد، یعنی همان پیکانی که نورایی کشیده است. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/n%C3%A9h%E2%82%82s-\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. nas-: 'expressive form *nāss- in Latin nāsus, nose: NASAL, NASO-' — both English items derived from Latin nāsus, as drawn; the index (line 2093) also lists 'NASAL nas-', 'NASO- nas-'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"p. 1028 s.v. nasal (and orinasal)\", \"stance\": \"supports\", \"note\": \"'nasal, adj., 1) pertaining to the nose; 2) uttered through the nose (said of sounds). — Formed with adj. suff. -al fr. L. nasus, \\\"nose\\\", which is rel. to naris for *nasis, \\\"nostril\\\"'; the orinasal entry cites 'Late L. nasalis'.\"},\n            {\"src\": \"SKT\", \"where\": \"grep 'nasal|NOSE' in SKT.txt\", \"stance\": \"silent\", \"note\": \"Skeat's Concise has no separate entry retrievable by these greps (only the string 'NOSED.'), so it adds nothing here.\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 6,\n      \"root\": \"N.b.b\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"Semitic root n-b-b 'to be/make hollow, hollow out' (Hebrew nābab, pass. part. nəbūb 'hollowed'; Arabic nabb, unbūb 'internode of a reed')\",\n      \"note\": \"The root itself, its label 'Semitic' and its gloss are right, and Nourai's reference states them: Klein p. 138 s.v. Bab has 'from Sem. stem n-b-b, \\\"to make hollow, to hollow out\\\", whence also Heb. nəbhūbh, \\\"hollowed\\\", Aram.-Syr. abbūbhā, Akkad. imbūbu, \\\"flute\\\", Arab. anbūb, \\\"part of reed between knots\\\"'. The same analysis is older than Klein: Fraenkel (1886) p. 14 credits G. Hoffmann with deriving Aramaic bābā 'door' 'aus *nəbābā \\\"Loch\\\" zur Wurzel nbb \\\"höhlen\\\"'. What is contested is not the root but its scope — whether Akkadian bābu 'gate' really belongs to it (Wiktionary reports the borrowing chain but derives bāb from a root b-w-b and cites Hans Bauer's native-Semitic account, with no mention of n-b-b), and whether the place-name Bāb-ilu is a genuine compound or an Akkadian folk etymology of an older non-Semitic name. Those affect the nodes, not the root box.\",\n      \"note_fa\": \"خودِ ریشهٔ سامیِ n-b-b «میان‌تهی کردن، سوراخ کردن» و برچسب و معنای آن در نمودار درست است و مرجعِ نورایی نیز همین را می‌گوید: کلاین در ص ۱۳۸ زیر Bab می‌نویسد این خانواده «از ستاک سامی n-b-b» است و عبری nəbūb «میان‌تهی»، آرامی-سریانی ʾabbūbā، اکدی imbūbu «نی، فلوت» و عربی أنبوب «فاصلهٔ میان دو بندِ نی» را از آن می‌شمارد. این تحلیل کهن‌تر از کلاین است: فرنکل (۱۸۸۶، ص ۱۴) آن را به گ. هوفمان نسبت می‌دهد که bābā آرامی «در» را از *nəbābā «سوراخ» از ریشهٔ nbb گرفته است. آنچه امروز محلِ گفت‌وگوست نه خودِ ریشه است بلکه گسترهٔ آن: این‌که آیا bābu اکدی «دروازه» به‌راستی از این ریشه است (ویکی‌واژه آن را به ریشهٔ b-w-b می‌برد و به تحلیلِ بومی-سامیِ هانس باوئر ارجاع می‌دهد و نامی از n-b-b نمی‌برد) و این‌که آیا Bāb-ilu ترکیبی اصیل است یا ریشه‌شناسی عامیانهٔ اکدی برای نامی کهن‌تر و غیرسامی. این نکته‌ها به گره‌ها مربوط است نه به جعبهٔ ریشه.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D8%A8\",\n        \"https://en.wiktionary.org/wiki/%D8%A3%D9%86%D8%A8%D9%88%D8%A8\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"KLN:138\", \"status\": \"supports\", \"note\": \"KLN_1966.txt line 4216 (the B section opens at line ~4209, whose OCR'd page number reads '13?' = 138): 'Bab, n., title given to the founder of Babism. — Pers. bāb, \\\"door, gate\\\", fr. Arab. bāb, of s.m., fr. Aram. bābh, bābhā, fr. Akkad. bābu, \\\"door, gate\\\", which is shortened fr. *nebāba, lit. \\\"hole, aperture\\\", from Sem. stem n-b-b, \\\"to make hollow, to hollow out\\\", whence also Heb. nəbhūbh, \\\"hollowed\\\", Aram.-Syr. abbūbhā, Akkad. imbūbu, \\\"flute\\\", Arab. anbūb, \\\"part of reed between knots\\\". Cp. Babel.' — this single Klein entry is the source of the whole chart.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"AFA\", \"where\": \"Fraenkel, Aram. Fremdwörter p. 14 (AFA.txt lines 1078-1090)\", \"stance\": \"supports\", \"note\": \"'Das älteste und üblichste Wort ist bāb, übernommen aus [Aram.] bābā, das in jüdischen Texten ungemein beliebt ist, während es im Syrischen nur sehr selten vorkommt. G. Hoffmann hat es sehr einleuchtend aus *nəbābā \\\"Loch\\\" zur Wurzel nbb \\\"höhlen\\\" erklärt.'\"},\n        {\"src\": \"FVQ\", \"where\": \"Jeffery p. 74 s.v. بَاب (Bāb)\", \"stance\": \"partial\", \"note\": \"'Fraenkel, Fremdw. 14, noted that it was an early loan word … from the Aram. bābā … D. H. Müller, however (WZKM i, 23), on the ground that bābā occurs very rarely in Syr. and that the root is entirely lacking in Heb., Eth., and Sab., suggested that it was an early borrowing from Mesopotamia (cf. Zimmern, Akkad. Fremdw. 30), and may have come directly into Arabic' — supports the Mesopotamian source, but records that the n-b-b root is absent outside Aramaic/Akkadian.\"},\n        {\"src\": \"KLN\", \"where\": \"p. 138 s.v. babble\", \"stance\": \"partial\", \"note\": \"Klein keeps the imitative base *bab- ('babble') strictly apart from this root, which is worth noting because English 'babel' as 'confused noise' owes something to that association.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Akkadian\",\n          \"words\": \"nebâbâ : hole; imbŭbu : hollow tube; bâbu : door; bâb-ilu : gate to gods\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Two of the four items are solid Akkadian: bābu(m) 'gate, door' (written with the sign KÁ) is one of the commonest Akkadian nouns, and imbūbu/enbūbu 'reed pipe, flute' is attested and is the source of the Aramaic and Arabic pipe words (Zimmern p. 30: 'akk. imbūbu Flöte : > aram. ʾabbūbā (mand. ʾambūhā) Flöte, Rohr (> wohl arab. ʾunbūb Rohr)'). The first item is where the chart overstates: Klein writes bābu as 'shortened fr. *nebāba' with an asterisk, i.e. a RECONSTRUCTION, and the shape nəbābā he gives is the Aramaic one; the book prints 'nebâbâ : hole' as though it were an attested Akkadian noun (the printed page, checked at 300 dpi, indeed has no asterisk, so this is Nourai's own presentation and not an extraction slip). The fourth item, bāb-ilu 'gate of the god' (later Bāb-ilāni 'gate of the gods'), is a real Akkadian rendering of the city's name, but modern Assyriology since Gelb (1955) treats 'gate of god' as a Semitic FOLK ETYMOLOGY of an older non-Semitic name (Babilla, 'of unknown meaning and origin'), with Sumerian KÁ.DIG̃IR.RA a loan translation of that Akkadian reinterpretation rather than the original name — so the gloss is right for the Akkadian form but wrong as the ultimate origin.\",\n          \"derivation_fa\": \"از چهار مدخلِ این گره دو تا استوارند: bābu(m) «در، دروازه» یکی از پربسامدترین نام‌های اکدی است و imbūbu/enbūbu «نی، فلوت» نیز مضبوط است و سرچشمهٔ واژه‌های آرامی و عربیِ «لوله» است (سیمرن ص ۳۰: «اکدی imbūbu فلوت > آرامی ʾabbūbā … > احتمالاً عربی ʾunbūb»). مدخل نخست اما اغراق است: کلاین bābu را «کوتاه‌شده از *nebāba» می‌نویسد، با ستاره، یعنی صورتی بازسازی‌شده و آن هم به شکلِ آرامی؛ ولی کتاب «nebâbâ : سوراخ» را چنان می‌آورد که گویی واژه‌ای مضبوط در اکدی است (تصویر صفحهٔ چاپی را با تفکیک ۳۰۰ دیدم: ستاره‌ای در چاپ نیست، پس این کارِ خودِ نورایی است نه خطای خوانشِ اسکن). مدخل چهارم، bāb-ilu «دروازهٔ خدا» (و صورتِ متأخرِ Bāb-ilāni «دروازهٔ خدایان»)، صورتی اکدی و واقعی از نامِ آن شهر است، ولی آشورشناسیِ امروز از گلب (۱۹۵۵) به این‌سو «دروازهٔ خدا» را ریشه‌شناسی عامیانهٔ سامی برای نامی کهن‌تر و غیرسامی (Babilla با معنا و خاستگاهِ ناشناخته) می‌داند و نامِ سومریِ KÁ.DIG̃IR.RA را ترجمهٔ قرضیِ همان تفسیرِ عامیانه می‌شمارد. پس گره با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://en.wikipedia.org/wiki/Babylon\",\n            \"https://en.wiktionary.org/wiki/%D8%A3%D9%86%D8%A8%D9%88%D8%A8\",\n            \"https://en.wiktionary.org/wiki/Babylon\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN:138\", \"status\": \"supports\", \"note\": \"Klein p. 138 s.v. Bab and s.v. Babel: 'Akkad. bābu, \\\"door, gate\\\", which is shortened fr. *nebāba, lit. \\\"hole, aperture\\\" … Akkad. imbūbu, \\\"flute\\\"' and 'Heb. Bābhel, fr. Akkad. Bāb-ilu, lit. \\\"the gate of God\\\", prop. a literal translation of Sumerian Ka-dingir … compounded of bāb, \\\"gate\\\", and ilu, \\\"god\\\"' — all four items, with the asterisk on *nebāba that the chart drops.\"},\n            {\"ref\": \"AKD:30\", \"status\": \"supports\", \"note\": \"Zimmern p. 30 (AKD.txt: printed page markers '30' at line 399 and '31' at line 414; both items lie in that stretch): line 397 'akk. imbūbu Flöte : > aram. ʾabbūbā (mand. ʾambūhā) Flöte, Rohr (> wohl arab. ʾunbūb Rohr)' and line 406, under the section '6. Haus und Hausgeräte', 'akk. bābu Tor : > aram. bābā (> arab. bāb u. viell. späthebr. bāb Ps. 90,12)'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"AFA\", \"where\": \"Fraenkel p. 14\", \"stance\": \"supports\", \"note\": \"the *nəbābā 'Loch' / root nbb explanation, credited to G. Hoffmann (quoted in the entry's root-level consulted).\"},\n            {\"src\": \"FVQ\", \"where\": \"Jeffery p. 74 s.v. Bāb and s.v. Bābil\", \"stance\": \"partial\", \"note\": \"'It is, of course, from the Akk. Bāb-ilu (Delitzsch, Paradies, 212)' for the city name; but for bāb 'door' Jeffery reports the competing Aramaic and direct-Mesopotamian routes without endorsing the n-b-b derivation.\"},\n            {\"src\": \"AHM\", \"where\": \"en.wikipedia 'Babylon', Names section\", \"stance\": \"contradicts\", \"note\": \"'The \\\"gate of god\\\" interpretation is increasingly viewed as a Semitic folk etymology to explain an unknown original non-Semitic placename'; Gelb (1955) reconstructs an earlier Babilla, and the Sumerian KÁ.DIG̃IR.RA is then a loan translation of the Akkadian folk etymology — against the chart's gloss 'gate to gods' as the word's origin.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Aramaic\",\n          \"words\": \"\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"A pass-through box with no words printed: it stands for the Aramaic stage of both chains, and Nourai's reference carries it. Jewish Aramaic bābā 'door, gate' is extremely frequent in rabbinic literature (the Talmudic tractates Bābā Qammā / Meṣīʿā / Batrā are named with it) and rare in Syriac, and ʾabbūbā (Syriac ܐܰܒܽܘܒܐ, Mandaic ʾambūhā) 'flute, pipe' is its counterpart in the imbūbu chain; both are treated as Akkadian loans. The Aramaic forms happen to be identical in shape with the Akkadian ones (bābu > bābā with the Aramaic determinate ending -ā), which is presumably why the box is left wordless.\",\n          \"derivation_fa\": \"این جعبه واژه‌ای ندارد و تنها لایهٔ آرامی را در هر دو زنجیره نشان می‌دهد، و مرجعی که نورایی داده همین را پوشش می‌دهد. آرامیِ یهودیِ bābā «در، دروازه» در ادب رَبّانی بسیار پربسامد است (نام رسالاتِ تلمودیِ بابا قَمّا، بابا مِصیعا و بابا بَتْرا از همین واژه است) و در سریانی کم‌کاربرد؛ و ʾabbūbā (سریانی، و ʾambūhā در مندایی) «نی، فلوت» همتای آن در زنجیرهٔ imbūbu است. هر دو را وام‌واژهٔ اکدی می‌دانند. صورت آرامی با صورت اکدی هم‌شکل است (bābu با پایانهٔ معرفهٔ آرامیِ -ā می‌شود bābā) و همین سبب شده جعبه بی‌واژه بماند. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D8%A8\", \"https://en.wiktionary.org/wiki/%D8%A3%D9%86%D8%A8%D9%88%D8%A8\"],\n          \"ref_check\": [\n            {\"ref\": \"AKD:30\", \"status\": \"supports\", \"note\": \"Zimmern p. 30, quoted above: 'akk. bābu Tor : > aram. bābā' and 'akk. imbūbu Flöte : > aram. ʾabbūbā' — the Akkadian → Aramaic step Nourai draws, from the cited page.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"AFA\", \"where\": \"Fraenkel p. 14\", \"stance\": \"supports\", \"note\": \"'übernommen aus bābā, das in jüdischen Texten ungemein beliebt ist, während es im Syrischen nur sehr selten vorkommt' — the Aramaic word and its distribution; Fraenkel also notes the 'Kapitel' sense of bāb is Aramaic, citing Bābā Qammā/Meṣīʿā/Batrā.\"},\n            {\"src\": \"KLN\", \"where\": \"p. 138 s.v. Bab\", \"stance\": \"supports\", \"note\": \"'fr. Aram. bābh, bābhā, fr. Akkad. bābu' plus 'Aram.-Syr. abbūbhā' in the same entry.\"},\n            {\"src\": \"PLA\", \"where\": \"en.wiktionary أنبوب\", \"stance\": \"supports\", \"note\": \"'From Aramaic אַבּוּבָא / ܐܰܒܽܘܒܐ (ʾabbūḇā, \\\"flute; pipe\\\"), from Akkadian 𒄀𒁍 (enbūbu, \\\"flute\\\")' — the modern statement of the same two steps.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Arabic\",\n          \"words\": \"\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Another wordless pass-through box, standing for Arabic باب bāb (pl. أبواب abwāb) 'door, gate; chapter' and أنبوب unbūb 'internode of a reed, tube'. For unbūb the chain Akkadian enbūbu > Aramaic ʾabbūbā > Arabic unbūb is uncontested. For bāb the borrowing account is the older consensus — Fraenkel p. 14 calls bāb 'the oldest and commonest' Arabic word for a door and derives it from Aramaic bābā, noting it is already in pre-Islamic poetry (Ṭarafa, Muʿallaqa 18; Labīd 144,4; Zuhayr 9,27), which shows the loan is early — but it is not the only view: Wiktionary places bāb under the root ب و ب and reports Hans Bauer's proposal that the word is native Semitic ('an ancient univerbation of etyma equivalent to Arabic bāʔa bi- \\\"he has entered into (the house)\\\"'), with no mention of n-b-b. Hence plausible rather than confirmed for this half of the box.\",\n          \"derivation_fa\": \"این جعبه هم بی‌واژه است و نمایندهٔ عربیِ «باب» (جمع: أبواب) «در، دروازه؛ فصل کتاب» و «أنبوب» «فاصلهٔ میان دو بندِ نی، لوله» است. دربارهٔ «أنبوب» زنجیرهٔ اکدیِ enbūbu > آرامیِ ʾabbūbā > عربیِ unbūb مورد اختلاف نیست. دربارهٔ «باب» روایتِ وام‌گیری همان اجماعِ کهن‌تر است — فرنکل (ص ۱۴) «باب» را کهن‌ترین و رایج‌ترین واژهٔ عربی برای «در» می‌داند و آن را از bābā آرامی می‌گیرد و می‌افزاید که در شعر جاهلی (معلقهٔ طرفه بیت ۱۸، دیوان لبید، زهیر) آمده است و همین دیرینگیِ وام را نشان می‌دهد — ولی یگانه دیدگاه نیست: ویکی‌واژه «باب» را زیر ریشهٔ «ب و ب» می‌آورد و به پیشنهادِ هانس باوئر ارجاع می‌دهد که این واژه بومیِ سامی است و از «باء بـ» («به خانه درآمد») ساخته شده، و نامی از n-b-b نمی‌برد. پس این نیمهٔ جعبه با احتیاط پذیرفتنی است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D8%A8\", \"https://en.wiktionary.org/wiki/%D8%A3%D9%86%D8%A8%D9%88%D8%A8\"],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"no reference is printed on this node; the parent's KLN:138 and AKD:30 were checked instead, and both give Aramaic → Arabic explicitly ('> arab. bāb', 'wohl arab. ʾunbūb').\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"AFA\", \"where\": \"Fraenkel p. 14\", \"stance\": \"supports\", \"note\": \"'Das älteste und üblichste Wort ist bāb, übernommen aus bābā … Es ist schon frühe zu den Arabern gewandert: Ṭar. Muʿall. 18; 17,10; Dīwān Leb. 144,4; Zuheir 9,27 … Natürlich ist auch der Gebrauch des Wortes für \\\"Abschnitt\\\", \\\"Kapitel\\\" aus dem Aramäischen entlehnt.'\"},\n            {\"src\": \"FVQ\", \"where\": \"Jeffery p. 74 s.v. Bāb\", \"stance\": \"supports\", \"note\": \"'Occurs some twenty-seven times, e.g. ii, 55 … It occurs commonly in the old poetry, which confirms the theory of early borrowing, and it is noteworthy that from some Mesopotamian source it passed into Middle Persian (Frahang, Glossary, p. 103; Herzfeld, Paikuli, Glossary, 151).'\"},\n            {\"src\": \"KLN\", \"where\": \"en.wiktionary باب, Arabic section\", \"stance\": \"partial\", \"note\": \"'Usually considered a borrowing from Aramaic בָּבָא (bāḇā), from Akkadian bābum … Hans Bauer proposes these words are native to Semitic' — root given as ب و ب, no n-b-b.\"},\n            {\"src\": \"AFM\", \"where\": \"grep 'الباب' in AFM_pages.txt\", \"stance\": \"silent\", \"note\": \"Addi Shir's list of Persian words in Arabic mentions الباب only inside other entries (e.g. line 771 'الباب … فارسية' concerns a different headword and line 1588 دركاه 'ومعناه الباب'); he does not treat بَاب itself as a loan from Persian, which is consistent with the chart's direction.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Persian\",\n          \"words\": \"bâb 2 «باب ۲»; anbŭb «انبوب»; Bâbel «بابل»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"All three Persian items are Arabic loans, i.e. the last link of the chart's chain, and Mo'in (Nourai's reference) marks them so. باب bāb is entered '[ع.]' (Arabic) with the senses 'door, gate; a section of a book; a strait; a classifier for houses and shops; kind, sort; concerning' — the 'chapter' sense itself an Aramaism inside Arabic. انبوب anbūb/onbūb is likewise '[ع.]' with 'the space between two knots of a reed; anything hollow like a reed; a pipe (for water etc.)', pl. انابیب; note that the 'flute' half of Nourai's gloss belongs to the Akkadian/Aramaic stage (imbūbu, ʾabbūbā 'flute'), not to the Persian word. بابل Bābel is Babylon via Arabic Bābil (Qur'an 2:96), itself from Akkadian Bāb-ilu through Syriac or Hebrew. One refinement: Jeffery notes that bāb had already reached MIDDLE Persian from a Mesopotamian source (it is in the Frahang ī Pahlavīg and in the Paikuli glossary), so the New Persian word is strictly a re-borrowing through Arabic rather than the first contact.\",\n          \"derivation_fa\": \"هر سه واژهٔ فارسیِ این گره وام‌واژهٔ عربی‌اند، یعنی آخرین حلقهٔ زنجیرهٔ نمودار، و معین (همان مرجعی که نورایی می‌دهد) هر سه را با نشانِ «[ع.]» می‌آورد. «باب» با معناهای «در، دروازه؛ فصلِ کتاب؛ تنگهٔ میان دو خشکی؛ واحدِ شمارشِ خانه و دکان؛ گونه؛ در بابِ …» ثبت شده است؛ معنای «فصل» خود در عربی وام‌گرفته از آرامی است. «انبوب» نیز «[ع.]» است: «فاصلهٔ میان دو بند یا گرهِ نی؛ هر چیزِ مجوّف مانند نی؛ لوله (آب و غیره)»، جمع: انابیب — و بایست گفت که نیمهٔ «فلوت»ِ معنایی که نورایی می‌دهد به لایهٔ اکدی و آرامی (imbūbu، ʾabbūbā «فلوت») بازمی‌گردد نه به واژهٔ فارسی. «بابل» از راه عربیِ «بابل» (قرآن ۲:۹۶) و آن از اکدیِ Bāb-ilu از مسیر سریانی یا عبری است. یک نکتهٔ دقیق‌تر: جفری یادآور می‌شود که «باب» پیش‌تر در فارسی میانه هم از سرچشمه‌ای میان‌رودانی وارد شده بود (در فرهنگِ پهلویگ و واژه‌نامهٔ پایکولی)، پس صورتِ فارسی نو در حقیقت وام‌گیریِ دوباره از عربی است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://abadis.ir/fatofa/%D8%A8%D8%A7%D8%A8/\",\n            \"https://abadis.ir/fatofa/%D8%A7%D9%86%D8%A8%D9%88%D8%A8/\",\n            \"https://vajehyab.com/moein/%D8%A7%D9%86%D8%A8%D9%88%D8%A8\",\n            \"https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D8%A8\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"MON\", \"status\": \"supports\", \"note\": \"Mo'in, Farhang-e Farsi, read via vajehyab/abadis: s.v. باب '[ع.] (اِ) در، دروازه؛ بخشی از کتاب؛ تنگه؛ واحد شمارش خانه و دکان؛ نوع؛ در بابِ …'; s.v. انبوب '[ع.] (اِ) فاصلهٔ میان دو بند یا گرهِ نی؛ هر چیز مجوّف مانند نی؛ لوله (آب و غیره)، ج: انابیب'. Both marked Arabic, exactly as the chart's Arabic → Persian arrow requires. (Nourai gives only the bare 'MON' without a volume/page, so no page could be verified.)\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"vajehyab / abadis, فرهنگ معین s.v. انبوب and باب\", \"stance\": \"supports\", \"note\": \"quoted above; the abadis page also carries Dehkhoda's entry 'ع اِ' for انبوب with the Saʿdi (Bustān) citation.\"},\n            {\"src\": \"FVQ\", \"where\": \"Jeffery pp. 74-75 s.v. Bāb and Bābil\", \"stance\": \"supports\", \"note\": \"'from some Mesopotamian source it passed into Middle Persian (Frahang, Glossary, p. 103)' for bāb; and for the city 'It is, of course, from the Akk. Bāb-ilu … either through the Syr. or the Heb. … the name occurs in the old poetry' — the Arabic Bābil that Persian بابل continues.\"},\n            {\"src\": \"ARY\", \"where\": \"en.wiktionary باب, Persian section\", \"stance\": \"supports\", \"note\": \"Persian باب listed under the Arabic etymology with 'chapter (of written works)' and 'archaic: door, gate' — matching Nourai's 'bâb 2 : door' as the older, now literary sense.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Hebrew\",\n          \"words\": \"\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The wordless Hebrew box stands for two things Klein's p. 138 supplies: the root's Hebrew witness nəbūb 'hollowed' (Klein: 'whence also Heb. nəbhūbh, \\\"hollowed\\\"'), and the name בָּבֶל Bābel, the biblical form of Babylon, borrowed from Akkadian Bāb-ilu. Within Hebrew the name attracted its own folk etymology in Genesis 11:9, where it is connected with bālal 'to confound' ('therefore is the name of it called Babel; because the LORD did there confound the language') — a wordplay, not a derivation. The box is 'plausible' rather than 'confirmed' only because it is the pivot of the chart's Hebrew → English arrow, which (see node #6) is right for Babel but not for Babylonia; note too that Hebrew bāb 'door' is marginal (Klein and Zimmern cite only the doubtful late-Hebrew bāb of Ps. 90:12), so Hebrew is a witness to the root but not a strong link in the door chain.\",\n          \"derivation_fa\": \"جعبهٔ بی‌واژهٔ عبری نمایندهٔ دو چیز است که کلاین در ص ۱۳۸ می‌آورد: گواهِ عبریِ ریشه، یعنی nəbūb «میان‌تهی»، و نامِ בָּבֶל Bābel، صورتِ کتاب‌مقدسیِ بابِل، که از اکدیِ Bāb-ilu وام گرفته شده است. در خودِ عبری این نام ریشه‌شناسی عامیانهٔ ویژهٔ خود را یافته است: در سفر پیدایش ۱۱:۹ آن را با bālal «درهم‌آمیختن، آشفتن» پیوند می‌دهند («از این‌رو آن را بابل نامیدند، زیرا خداوند در آنجا زبانِ همه را آشفته کرد») — این جناسِ روایی است نه ریشه‌شناسی. حکمِ «با احتیاط پذیرفتنی» تنها از آن روست که این جعبه پایهٔ پیکانِ عبری←انگلیسیِ نمودار است و آن پیکان (گرهٔ ۶) برای Babel درست است ولی برای Babylonia نه؛ افزون بر این، bāb عبری «در» حاشیه‌ای است (کلاین و سیمرن تنها به bāb مشکوکِ مزمور ۹۰:۱۲ اشاره می‌کنند)، پس عبری گواهِ ریشه است نه حلقه‌ای استوار در زنجیرهٔ «در».\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Babylon\", \"https://en.wikipedia.org/wiki/Babylon\"],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"no reference on this node; the entry's KLN:138 covers it ('Heb. nəbhūbh, \\\"hollowed\\\"' and s.v. Babel 'Heb. Bābhel, fr. Akkad. Bāb-ilu').\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"p. 138 s.v. Babel and s.v. Bab\", \"stance\": \"supports\", \"note\": \"'Babel, n., name of the capital of Babylonia. — Heb. Bābhel, fr. Akkad. Bāb-ilu, lit. \\\"the gate of God\\\" …'; and in Bab, 'whence also Heb. nəbhūbh, \\\"hollowed\\\"'.\"},\n            {\"src\": \"FVQ\", \"where\": \"Jeffery p. 74 s.v. Bābil\", \"stance\": \"partial\", \"note\": \"'from the Akk. Bāb-ilu … either through the Syr. or the Heb.' — Hebrew is only one of two possible transmitters, on Jeffery's account.\"},\n            {\"src\": \"AKD\", \"where\": \"Zimmern p. 30\", \"stance\": \"partial\", \"note\": \"'akk. bābu Tor : > aram. bābā (> arab. bāb u. viell. späthebr. bāb Ps. 90,12)' — the Hebrew reflex of the 'door' word is marked 'viell.' (perhaps) and confined to one late passage.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"English\",\n          \"words\": \"Babel, Babylonia\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Babel is indeed the Hebrew form as transmitted by the Latin Vulgate and the English Bible (Wycliffe, Tyndale), and its modern English sense 'confused noise, din' comes from the Genesis 11 story, reinforced by the accidental similarity to babble (an independent imitative base — Klein keeps them apart on the same page 138). Babylonia, however, did not come through Hebrew: Klein's own entry on the cited page derives it 'L., fr. Gk. Babylōnía, fr. Babylōn, fr. Akkad. Bāb-ilāni, \\\"the gate of the gods\\\" … a later form, occurring in texts dating from the Neo-Babylonian period' — i.e. Akkadian → Greek → Latin → English, not through Hebrew as the chart's single Hebrew → English arrow implies. Add the fact that 'gate of the god(s)' is itself an Akkadian folk etymology of a pre-Semitic name, and the node is acceptable in substance but mis-routed in detail.\",\n          \"derivation_fa\": \"«Babel» به‌راستی همان صورتِ عبری است که از راهِ ترجمهٔ لاتینِ وولگاتا و کتاب‌مقدس‌های انگلیسی (وایکلیف، تیندل) به انگلیسی رسیده، و معنای امروزینِ آن «همهمه و آشفتگی» از داستان پیدایش ۱۱ می‌آید که شباهتِ تصادفی با babble «یاوه‌گویی» نیز آن را تقویت کرده است (کلاین در همان ص ۱۳۸ این دو را جدا نگاه می‌دارد). اما «Babylonia» از راه عبری نیامده است: خودِ کلاین در همان صفحه می‌نویسد از لاتین، از یونانیِ Babylōnía، از Babylōn، از اکدیِ Bāb-ilāni «دروازهٔ خدایان» — «صورتی متأخر که در متونِ دورهٔ بابلِ نو دیده می‌شود»؛ یعنی اکدی ← یونانی ← لاتین ← انگلیسی، نه از راهِ عبری که یگانه پیکانِ نمودار می‌نمایاند. اگر این را با عامیانه‌بودنِ خودِ تفسیرِ «دروازهٔ خدا» بسنجیم، گره در جانِ مطلب پذیرفتنی است ولی در مسیر نادقیق: با احتیاط پذیرفتنی است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Babylon\", \"https://en.wikipedia.org/wiki/Babylon\"],\n          \"ref_check\": [\n            {\"ref\": \"KLN:138\", \"status\": \"partial\", \"note\": \"the cited page has both words but splits them: 'Babel … Heb. Bābhel, fr. Akkad. Bāb-ilu' (so the Hebrew route holds for Babel) versus 'Babylon, n. … — L., fr. Gk. Babylōn, fr. Akkad. Bāb-ilāni, \\\"the gate of the gods\\\" … Babylonia, n. — L., fr. Gk. Babylōnía' (so Babylonia comes via Greek and Latin, not via Hebrew). Klein therefore supports half of the arrow and contradicts the other half.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"p. 138 s.v. Babylon, Babylonia, babble\", \"stance\": \"partial\", \"note\": \"quoted above; 'babble, intr. and tr. v. — ME. babelen, from the I.-E. imitative base *bab-' keeps the noise word apart from the place name.\"},\n            {\"src\": \"AHM\", \"where\": \"en.wiktionary 'Babylon'\", \"stance\": \"supports\", \"note\": \"'from Akkadian Bābilim, literally \\\"Gate of God\\\", via Ancient Greek Βαβυλών (Babulṓn), Latin Babylōn' and Babel/Babylon described as doublets — the Greek-Latin route for the -on/-onia forms.\"},\n            {\"src\": \"AID\", \"where\": \"en.wikipedia 'Babylon', Names section\", \"stance\": \"partial\", \"note\": \"the 'gate of god' reading is 'increasingly viewed as a Semitic folk etymology'; Gelb's Babilla is the probable original — relevant to what 'Babel/Babylonia' ultimately mean, not to the English transmission.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\nJSONEOF\npython3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-350.json > /dev/null && echo \"JSON OK\"\npython3 tools/verify_check.py 350"
}
```


### [2026-09-07T18:36:08.836Z] TOOL RESULT

```
JSON OK
nodes verified: 16/16
node verdicts: {'confirmed': 10, 'plausible': 6}
root verdicts: {'confirmed': 3}
ref checks: {'supports': 12, 'not_checked': 3, 'partial': 3}
books consulted: {'supports': 38, 'partial': 8, 'silent': 3, 'contradicts': 1} | by book: {'KLN': 9, 'FVQ': 4, 'MON': 3, 'LKT': 3, 'POK': 3, 'IEC': 3, 'AFA': 3, 'PLA': 2, 'AHD': 2, 'SYN': 2, 'AHM': 2, 'PHD': 1, 'BQT': 1, 'DEV': 1, 'PHN': 1, 'LAM': 1, 'HJB': 1, 'BRT': 1, 'KNT': 1, 'FSD': 1, 'SKT': 1, 'AFM': 1, 'ARY': 1, 'AKD': 1, 'AID': 1}
```


## [2026-09-07T18:36:24.056Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 - <<'EOF'\nimport json,io\np='data/verification/page-350.json'\nd=json.load(open(p))\nfixes=0\ndef fix(c):\n    global fixes\n    w=c.get('where','')\n    if 'wiktionary' in w and c['src']!='WIKT':\n        c['src']='WIKT'; fixes+=1\n    if 'wikipedia' in w and c['src']!='WIKIPEDIA':\n        c['src']='WIKIPEDIA'; fixes+=1\n    if c.get('stance')=='not_available':\n        c['stance']='silent'; fixes+=1\nfor e in d['entries']:\n    for c in e.get('consulted',[]): fix(c)\n    for n in e['nodes']:\n        for c in n.get('consulted',[]): fix(c)\njson.dump(d,open(p,'w'),ensure_ascii=False,indent=2)\nopen(p,'a').write('\\n')\nprint('fixes',fixes)\nEOF\npython3 -m json.tool data/verification/page-350.json > /dev/null && echo \"JSON OK\"\npython3 tools/verify_check.py 350"
}
```


### [2026-09-07T18:36:25.480Z] TOOL RESULT

```
fixes 8
JSON OK
nodes verified: 16/16
node verdicts: {'confirmed': 10, 'plausible': 6}
root verdicts: {'confirmed': 3}
ref checks: {'supports': 12, 'not_checked': 3, 'partial': 3}
books consulted: {'supports': 38, 'partial': 8, 'silent': 3, 'contradicts': 1} | by book: {'KLN': 8, 'WIKT': 5, 'FVQ': 4, 'LKT': 3, 'POK': 3, 'IEC': 3, 'AFA': 3, 'MON': 2, 'AHD': 2, 'SYN': 2, 'WIKIPEDIA': 2, 'PHD': 1, 'BQT': 1, 'PLA': 1, 'DEV': 1, 'PHN': 1, 'LAM': 1, 'HJB': 1, 'BRT': 1, 'KNT': 1, 'FSD': 1, 'SKT': 1, 'AFM': 1, 'AKD': 1}
```


## [2026-09-07T18:36:34.938Z] TOOL CALL #58: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK\ncp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg350.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/350.png\nls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/350.png /home/sfmqrb/git/rishe/data/verification/page-350.json"
}
```


### [2026-09-07T18:36:35.011Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 76007 Sep  7 14:36 /home/sfmqrb/git/rishe/data/verification/page-350.json
-rw-rw-r-- 1 sfmqrb sfmqrb 70743 Sep  7 14:36 /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/350.png
```


## [2026-09-07T18:36:54.005Z] AGENT

Page 350 (book p. 320) verified: `data/verification/page-350.json`, `verify_check.py 350` → 16/16 nodes, 0 PROBLEM lines.

Counts: roots 3 confirmed (Nârikelah, Nas, N.b.b; the 3 redirects skipped). Nodes: 10 confirmed, 6 plausible, 0 disputed / transcription_suspect. Ref checks: 12 supports, 3 partial, 3 not_checked (nodes the book left without refs).

Plausible items (each explained in the JSON):
- Nârikelah #4 English nargeela, narghile — narghile via French is right (Etymonline 1820), but "nargeela" is an Anglo-Indian transcription taken straight from Persian, and Nourai's own Klein (p. 1028) and Lokotsch route the English from Persian with no French step.
- Nas #4 English nose, nostril — OE nosu reflects the Germanic ZERO grade *nusō, not the parent box's *nasō; Kent p. 193 only lists "NEng. nose" as a cognate.
- N.b.b #1 Akkadian — "nebâbâ : hole" is Klein's asterisked reconstruction *nebāba (and in Aramaic shape), printed unasterisked; and "bâb-ilu : gate to gods" is now regarded as a Semitic folk etymology of a pre-Semitic name Babilla (Gelb 1955), with Sumerian KÁ.DIG̃IR.RA a calque of it.
- N.b.b #3 Arabic — bāb from Aramaic is the older consensus (Fraenkel p. 14, Jeffery p. 74), but Wiktionary puts it under root b-w-b with Bauer's native-Semitic account and no n-b-b; unbūb ← Aramaic ʾabbūbā ← Akkadian enbūbu is uncontested.
- N.b.b #5/#6 Hebrew → English — Babel via Hebrew is right, but Babylonia comes Akkadian → Greek → Latin (Klein's own p. 138 entry), not through Hebrew.

Best confirmations: BQT:2095 read from the page image (Mo'in gives Pahlavi anârgil after Unvala 227, the Xusrō ī Kawādān §50 attestation "anārgēl kē abāg šakar xwarēnd", Sanskrit nārikela/nārikera, Arabic نارجیل/نارجیله) — saved to `sources/refs/ocr/BQT/2095.vision.txt`; PLA:256 (running head confirms the page); KLN:1028 and KLN:138 (OCR page markers confirm both); AKD:30 (Zimmern's imbūbu and bābu both on p. 30); KNT:193; POK:755 + 768 (both pages verified, matching Watkins' own "[Pok. nas- 755, neu-ks 768]").

No extraction errors: the printed page (rendered at 300 dpi, copied to `sources/refs/ocr/BOOK/350.png`) matches the JSON word for word. One layout note for the owner, not an error: in the Nas chart the Avestan/Old Persian box has an arrow to an **empty** box at the top right, which the extraction does not represent as a node.
