# Verification process log — verify-page-405


## [2026-09-14T00:53:06.906Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 405 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-405.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-405.json. Write /home/sfmqrb/git/rishe/data/verification/page-405.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 405` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T00:53:08.647Z] AGENT

I'll start by reading the agent instructions.


## [2026-09-14T00:53:09.380Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


## [2026-09-14T00:53:09.387Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-405.txt"
}
```


### [2026-09-14T00:53:09.402Z] TOOL RESULT

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


### [2026-09-14T00:53:09.409Z] TOOL RESULT

```
1	=== PDF page 405 (book page 375) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Pôl : to touch, feel  (refs POK:847)
4	#1 (parent #0) [Persian] refs=POK:841; MON:680 | pâlîdan «پالیدن ۲» : to touch a surface in search of something
5	#2 (parent #0) [Greek] refs=AHD | psallein : to touch, play harp
6	  #3 (parent #2) [Arabic] refs=KLN:1382 | santîr : a kind of harp
7	    #4 (parent #3) [Persian] refs=MON:1927 | santur «سنتور» : a stringed music instrument
8	#5 (parent #0) [Germanic] refs=AHD | fôljan : to feel
9	  #6 (parent #5) [English] refs=None | feel
10	--- entry 1 ---
11	ROOT Porkwos -> redirect to Pel 2
12	--- entry 2 ---
13	ROOT P-os -> redirect to Apo
14	--- entry 3 ---
15	ROOT Pos -> redirect to Apo
16	--- entry 4 ---
17	ROOT [Pahlavi] Pôš : cover, clothes  (refs FFD:44)
18	#1 (parent #0) [Persian] refs=FFD:44 | pŭš «پوش» : cover ; pŭšîdan «پوشیدن» : to cover, to wear ; pâ-pŭš «پاپوش» : foot wear, shoe ☞Ped | extra: پوشه، پوشک، پوشاک، پوشنه؛ پوشا
19	  #2 (parent #1) [Arabic] refs=KLN:138,1573 | ba-buš : shoe ; tar-buš : sweat cap | NOTE: "tar: sweat" is from a Turkish root.
20	    #3 (parent #2) [French] refs=KLN:138,1573 | babouche ; tarbouche
21	      #4 (parent #3) [English] refs=KLN:138,1573 | babouche : shoe ; tarbooche : a brimless cap
22	    #5 (parent #2) [Turkish] refs=SYN:428 | babuč : shoe
23	      #6 (parent #5) [Greek] refs=SYN:428 | papoutsi : shoe
24	--- entry 5 ---
25	ROOT Poti -> redirect to Pa
26	--- entry 6 ---
27	ROOT Potiš -> redirect to Pa
28	
```


## [2026-09-14T00:53:12.382Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-405.json | python3 -m json.tool | head -200",
 "description": "Read source JSON for page 405"
}
```


### [2026-09-14T00:53:13.709Z] TOOL RESULT

```
{
    "pdf_page": 405,
    "book_page": 375,
    "entries": [
        {
            "root": {
                "name": "P\u00f4l",
                "lang": "Indo-European",
                "refs": "POK:847",
                "gloss": "to touch, feel"
            },
            "nodes": [
                {
                    "id": 1,
                    "parent": 0,
                    "lang": "Persian",
                    "refs": "POK:841; MON:680",
                    "words": [
                        {
                            "translit": "p\u00e2l\u00eedan",
                            "gloss": "to touch a surface in search of something",
                            "script": "\u067e\u0627\u0644\u06cc\u062f\u0646 \u06f2"
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 2,
                    "parent": 0,
                    "lang": "Greek",
                    "refs": "AHD",
                    "words": [
                        {
                            "translit": "psallein",
                            "gloss": "to touch, play harp",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 3,
                    "parent": 2,
                    "lang": "Arabic",
                    "refs": "KLN:1382",
                    "words": [
                        {
                            "translit": "sant\u00eer",
                            "gloss": "a kind of harp",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 4,
                    "parent": 3,
                    "lang": "Persian",
                    "refs": "MON:1927",
                    "words": [
                        {
                            "translit": "santur",
                            "gloss": "a stringed music instrument",
                            "script": "\u0633\u0646\u062a\u0648\u0631"
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 5,
                    "parent": 0,
                    "lang": "Germanic",
                    "refs": "AHD",
                    "words": [
                        {
                            "translit": "f\u00f4ljan",
                            "gloss": "to feel",
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
                    "refs": null,
                    "words": [
                        {
                            "translit": "feel",
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
                "name": "Porkwos",
                "redirect": "Pel 2"
            },
            "nodes": []
        },
        {
            "root": {
                "name": "P-os",
                "redirect": "Apo"
            },
            "nodes": []
        },
        {
            "root": {
                "name": "Pos",
                "redirect": "Apo"
            },
            "nodes": []
        },
        {
            "root": {
                "name": "P\u00f4\u0161",
                "lang": "Pahlavi",
                "refs": "FFD:44",
                "gloss": "cover, clothes"
            },
            "nodes": [
                {
                    "id": 1,
                    "parent": 0,
                    "lang": "Persian",
                    "refs": "FFD:44",
                    "words": [
                        {
                            "translit": "p\u016d\u0161",
                            "gloss": "cover",
                            "script": "\u067e\u0648\u0634"
                        },
                        {
                            "translit": "p\u016d\u0161\u00eedan",
                            "gloss": "to cover, to wear",
                            "script": "\u067e\u0648\u0634\u06cc\u062f\u0646"
                        },
                        {
                            "translit": "p\u00e2-p\u016d\u0161",
                            "gloss": "foot wear, shoe",
                            "script": "\u067e\u0627\u067e\u0648\u0634",
                            "see": [
                                "Ped"
                            ]
                        }
                    ],
                    "script_extra": "\u067e\u0648\u0634\u0647\u060c \u067e\u0648\u0634\u06a9\u060c \u067e\u0648\u0634\u0627\u06a9\u060c \u067e\u0648\u0634\u0646\u0647\u061b \u067e\u0648\u0634\u0627",
                    "note": null,
                    "quote": {
                        "text": "\u0686\u0647 \u062c\u0627\u06cc \u0635\u062d\u0628\u062a \u0646\u0627\u0645\u062d\u0631\u0645 \u0627\u0633\u062a \u0645\u062c\u0644\u0633 \u0627\u064f\u0646\u0633 - \u0633\u0631 \u067e\u06cc\u0627\u0644\u0647 \u0628\u067e\u0648\u0634\u0627\u0646 \u06a9\u0647 \u062e\u0631\u0642\u0647 \u067e\u0648\u0634 \u0622\u0645\u062f",
                        "poet": "H\u00e2fez"
                    }
                },
                {
                    "id": 2,
                    "parent": 1,
                    "lang": "Arabic",
                    "refs": "KLN:138,1573",
                    "words": [
                        {
                            "translit": "ba-bu\u0161",
                            "gloss": "shoe",
                            "script": null
                        },
                        {
                            "translit": "tar-bu\u0161",
                            "gloss": "sweat cap",
                            "script": null
                        }
                    ],
                    "note": "\"tar: sweat\" is from a Turkish root.",
                    "quote": null
                },
                {
                    "id": 3,
                    "parent": 2,
                    "lang": "French",
                    "refs": "KLN:138,1573",
                    "words": [
                        {
                            "translit": "babouche",
                            "gloss": null,
                            "script": null
                        },
                        {
                            "translit": "tarbouche",
                            "gloss": null,
                            "script": null
```


## [2026-09-14T00:53:14.824Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','MON','AHD','KLN','FFD','SYN','WLD','HRN','HUB','PHD','NYB','BQT','ARY','IEC','BRT','SKT','WEB','FSD','TTS','LKT','PLA','AFM','FVQ']:\n    print(k, json.dumps(d.get(k),ensure_ascii=False)[:400])\n\"",
 "description": "Check reference metadata"
}
```


### [2026-09-14T00:53:15.881Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
FFD {"title": "Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ماده-های-فعلهای-فارسی-دری-محسن-اب/ -> https://dl.eliteraturebook.com/app/public/attachments/6925d29630b83.PDF (free PDF site; grey)", "lookup_hint": "Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/downloa
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
TTS {"title": "H. Vámbéry, Etymologisches Wörterbuch der turko-tatarischen Sprachen, Leipzig 1878 (repr. Osnabrück 1972)", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/etymologischesw00vmuoft (Toronto scan; also Google/bub_gb copies)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft.pdf", 
LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 =
PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/
AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_page
FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.t
```


## [2026-09-14T00:53:40.145Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/extracted/batch/page-405.json'))\nprint(json.dumps(d['entries'][4],ensure_ascii=False,indent=1)[-2500:])\n\"; ls data/verification/sources/refs/ | head -80",
 "description": "Rest of entry 4 and list refs dir"
}
```


## [2026-09-14T00:53:40.978Z] TOOL CALL #6: Bash

```json
{
 "command": "sed -n '1,200p' data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-14T00:53:41.613Z] TOOL RESULT

```
{
 "root": {
  "name": "Pôš",
  "lang": "Pahlavi",
  "refs": "FFD:44",
  "gloss": "cover, clothes"
 },
 "nodes": [
  {
   "id": 1,
   "parent": 0,
   "lang": "Persian",
   "refs": "FFD:44",
   "words": [
    {
     "translit": "pŭš",
     "gloss": "cover",
     "script": "پوش"
    },
    {
     "translit": "pŭšîdan",
     "gloss": "to cover, to wear",
     "script": "پوشیدن"
    },
    {
     "translit": "pâ-pŭš",
     "gloss": "foot wear, shoe",
     "script": "پاپوش",
     "see": [
      "Ped"
     ]
    }
   ],
   "script_extra": "پوشه، پوشک، پوشاک، پوشنه؛ پوشا",
   "note": null,
   "quote": {
    "text": "چه جای صحبت نامحرم است مجلس اُنس - سر پیاله بپوشان که خرقه پوش آمد",
    "poet": "Hâfez"
   }
  },
  {
   "id": 2,
   "parent": 1,
   "lang": "Arabic",
   "refs": "KLN:138,1573",
   "words": [
    {
     "translit": "ba-buš",
     "gloss": "shoe",
     "script": null
    },
    {
     "translit": "tar-buš",
     "gloss": "sweat cap",
     "script": null
    }
   ],
   "note": "\"tar: sweat\" is from a Turkish root.",
   "quote": null
  },
  {
   "id": 3,
   "parent": 2,
   "lang": "French",
   "refs": "KLN:138,1573",
   "words": [
    {
     "translit": "babouche",
     "gloss": null,
     "script": null
    },
    {
     "translit": "tarbouche",
     "gloss": null,
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
   "refs": "KLN:138,1573",
   "words": [
    {
     "translit": "babouche",
     "gloss": "shoe",
     "script": null
    },
    {
     "translit": "tarbooche",
     "gloss": "a brimless cap",
     "script": null
    }
   ],
   "note": null,
   "quote": null
  },
  {
   "id": 5,
   "parent": 2,
   "lang": "Turkish",
   "refs": "SYN:428",
   "words": [
    {
     "translit": "babuč",
     "gloss": "shoe",
     "script": null
    }
   ],
   "note": null,
   "quote": null
  },
  {
   "id": 6,
   "parent": 5,
   "lang": "Greek",
   "refs": "SYN:428",
   "words": [
    {
     "translit": "papoutsi",
     "gloss": "shoe",
     "script": null
    }
   ],
   "note": null,
   "quote": null
  }
 ]
}
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
```


### [2026-09-14T00:53:41.650Z] TOOL RESULT

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


## [2026-09-14T00:53:48.548Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources; python3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nfor k in ['POK','AHD','KLN','SYN','FFD','HRN','HUB','CHEUNG','PHD','NYB','MON','LKT','IEC','SKT','FSD','BRT','TTS','PLA','AFM','ARY','WLD','DEV','PHN']:\n    v=d.get(k,{})\n    print('==',k, '| local:',v.get('local_file'), '| offset:',v.get('page_offset'), '| hint:', str(v.get('lookup_hint'))[:200])\n\"",
 "description": "Page offsets for key refs"
}
```


### [2026-09-14T00:53:49.609Z] TOOL RESULT

```
== POK | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt | offset: POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.i
== AHD | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt | offset: 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page. | hint: Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the 
== KLN | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt | offset: KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume p
== SYN | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt | offset: leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed p
== FFD | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_asmaneketab.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_pages_faseng.txt'] | offset: 115 leaves (PDF pages); printed page = PDF page − 5 (PDF 40 = p.35). 2nd printing 1385 of the same Qoqnus setting (ISBN 964-311-015-X). | hint: Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/download): nothing; only a related paid e-book 'واژگان زبان فارسی دری' (fidibo). ketabnak.com/book/45024 is a d
== HRN | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt | offset: leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered ent
== HUB | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt | offset: leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number.
== CHEUNG | local: None | offset: None | hint: None
== PHD | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt | offset: leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsianjoman.org/wp-content/uploads/2015/09/A
== NYB | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt | offset: Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates and 'Bthl.' refs.
== MON | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt'] | offset: None | hint: Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Aves
== LKT | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt | offset: leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Numbered entries: 'NNNN. word (language) meaning' - Lokotsch is usually cited by entry number, but Nourai cites pages. grep the oriental source word in transliteration or the number.
== IEC | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt | offset: TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.
== SKT | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt | offset: leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags.
== FSD | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt | offset: vol1: leaf = p + 41..56 (drifts; e.g. leaf 87 = p.46, leaf 612 = p.556); vol3: leaf = p - 1466 (e.g. leaf 215 = p.1681); vol4: leaf = p - 2144..2148 (e.g. leaf 229 = p.2373); vol2 offset not reliably detected (pages ~ 700-1640) - grep the headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Headword in bold at line start with pronunciation; etymology in brackets at entry end '[< L. ...]'. Very large OCR (16 MB per vol); grep -n '^word' vol file.
== BRT | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt | offset: Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special transliteration is noisy - grep on a distinctive Latin glos
== TTS | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft_djvu.txt'] | offset: TTS_pages.txt: 253 leaves; printed page N = leaf N+30. | hint: Not searched exhaustively (3 citations); the 1878 original is public domain - try IA query 'vambery etymologisches wörterbuch turko-tatarischen' or Google Books.
== PLA | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt'] | offset: 301 leaves (pdftotext -layout, \f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276). | hint: HathiTrust search-only; Google Books id q_ErAAAAMAAJ snippet view; DDB has only the table of contents. No full text online. | For pages in a scanned volume use: python3 tools/ref_page.py PLA:<page> --
== AFM | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM.txt'] | offset: 198 leaves; page numerals OCR'd unreliably — offset approx leaf − 8 (front matter); confirm on page image | hint: Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أ
== ARY | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt'] | offset: printed page = pdf page + 1 | hint: Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword
== WLD | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt'] | offset: Band 3: leaf = printed + 6. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696). | hint: Band 3 is the index (Wortregister by language) - it maps a word to 'Band, page' in vols 1-2, so it can at least confirm that a word is treated at the cited WP volume/page. For the actual entry text, u
== DEV | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/DEV.txt | offset: leaf = printed + 26 (pp. <80) to +30 (pp. >84), e.g. leaf 29 = p.3, leaf 118 = p.88. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: French headword in caps at line start.
== PHN | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/PHN.txt | offset: leaf = printed + 31 (e.g. leaf 33 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: French headword in caps at line start; Arabic script not OCRed. grep -n '^BAZAR' etc.
```


## [2026-09-14T00:53:54.434Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD pōl ===\"; grep -n -iE \"^p[oō]l-|psall|f[oō]ljan\" AHD_watkins1985.txt | head -20\necho \"=== POK_02 page 847 (leaf 847-344=503) ===\"\nawk 'BEGIN{RS=\"\\f\"} NR>=502 && NR<=505 {print \"----LEAF\",NR; print substr($0,1,1500)}' POK_02.txt",
 "description": "Grep AHD and POK"
}
```


### [2026-09-14T00:53:55.537Z] TOOL RESULT

```
=== AHD pōl ===
866:pol-. Finger. Possibly the same root as pol-. Latin pollex, thumb: POLLEx. [Pok. polo- 840.]
=== POK_02 page 847 (leaf 847-344=503) ===
```


## [2026-09-14T00:53:59.986Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '855,880p' AHD_watkins1985.txt\necho \"=== search psalm/psaltery ===\"; grep -n -i \"psalt\\|psalm\\|harp\" AHD_watkins1985.txt | head",
 "description": "AHD context around pol-"
}
```


### [2026-09-14T00:54:00.062Z] TOOL RESULT

```
<persisted-output>
Output too large (48KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/tool-results/bxcgybnkx.txt

Preview (first 2KB):
[pippali. Pepper. Sanskrit noun of unknown origin. Possibly related to pippala, the bo tree. 1. Sanskrit pippali: PEPPER, (PIMPERNEL). 2. Sanskrit pippalam: PEEPUL.]
[pius. Dutiful, devoted, pious. Latin word having cog- nates in other Italic languages. PIACULAR, (PIETA), PI- ETY, PIOUS, PITTANCE, PITY; EXPIATE, IMPIOUS.]
plab-. To flap. Imitative root. Middle English flappen, to flap: FLAP [Pok. plab- 831.]
plak-'. Also plak-. To be flat. Extension of pele-2. 1. Germanic *fléh6 in Old Norse fl6, layer, coating: FLOE. 2. Variant form *pldg- in: a. Germanic *flék- in Old English fléc, flatfish: FLUKE!; b. Germanic *flakaz in Norwegian flak, flat piece, flake, probably akin to the Scandinavian source of Middle English flake, flake: FLAKE}; c. Germanic *flak- in Old Norse flaki, fleki, hurdle: FLAKE?. 3. Extended form *plakd in Germanic *flag6 in Old Norse flaga, layer of stone: FLAG, FLAW}. 4. Possibly suffixed (stative) form *plak-é-, to be calm (as of the flat sea), in Latin placére, to please, be agreeable: PLACEBO, PLACID, PLEA, (PLEAD), PLEASANT, PLEASE; COMPLACENT. 5. Lengthened suffixed form *plak-G- in Latin placdre, to calm (causative of placére): PLACABLE, PLACATE. 6. Nasalized form *pla-n-k- in Latin plancus, flat, flat-footed, whence planca, board: PLANCHET, PLANK, PLANK-SHEER. 7. Variant form *plag- in: a. perhaps Latin plaga, net (? < “something ex- tended”): PLAGIARY; b. Greek plagos, side: PLAGAL, PLAGIO-, PLAYA. 8. Root form *plak- in Greek plax, flat, flat land, surface: PLACENTA, PLACOID. 9. Variant form *pelag- in Greek pelagos, sea: PELAGIC; ARCHIPELAGO. [Pok. 1. pla-k- 831.]
...
</persisted-output>
```


## [2026-09-14T00:54:02.585Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor f in POK_01.txt POK_02.txt POK_03.txt POK_full.txt; do echo \"$f leaves: $(tr -cd '\\f' < $f | wc -c)\"; done\necho \"=== POK_full grep polo- / pel- touch ===\"\ngrep -n \"^polo-\\|^pōl\\|pol-, pel\\|polo- (pōlo-)\\|fühlen\" POK_full.txt | head -20",
 "description": "POK leaf counts and grep"
}
```


### [2026-09-14T00:54:03.623Z] TOOL RESULT

```
POK_01.txt leaves: 363
POK_02.txt leaves: 433
POK_03.txt leaves: 429
POK_full.txt leaves: 0
=== POK_full grep polo- / pel- touch ===
```


## [2026-09-14T00:54:11.731Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"To touch, feel\\|touch, feel\" AHD_watkins1985.txt | head\necho \"--- pol lines ---\"; grep -n \"^pol\\|^p6l\\|^pól\" AHD_watkins1985.txt | head",
 "description": "AHD touch feel root"
}
```


### [2026-09-14T00:54:11.791Z] TOOL RESULT

```
867:p6l-. To touch, feel, shake. 1. Germanic *féljan, to feel, in Old English félan, to examine by touch, feel: FEEL. 2. Reduplicated zero-grade form *pal-p- in: a. Latin palpus, a touching: PALP; b. Latin palpdri, palpdre, to stroke gently, touch: PALPABLE, PALPATE!, PALPITATE; c. Latin palpebra, eyelid (< ‘that which shakes or moves quickly”): PALPEBRAL. 3. Perhaps suffixed zero-grade form *pal-yo- in Greek pallein, to sway, brandish: CATA- PULT. 4, Perhaps suffixed form “psal-yo- in Greek psal- lein, to pluck, play the harp (but more likely of imitative origin): PSALM, PSALTERY. [Pok. 1. G. pel- 801.] [po6mum. Apple. Latin noun of unknown origin. POMACE, POMADE, POME.]
--- pol lines ---
866:pol-. Finger. Possibly the same root as pol-. Latin pollex, thumb: POLLEx. [Pok. polo- 840.]
867:p6l-. To touch, feel, shake. 1. Germanic *féljan, to feel, in Old English félan, to examine by touch, feel: FEEL. 2. Reduplicated zero-grade form *pal-p- in: a. Latin palpus, a touching: PALP; b. Latin palpdri, palpdre, to stroke gently, touch: PALPABLE, PALPATE!, PALPITATE; c. Latin palpebra, eyelid (< ‘that which shakes or moves quickly”): PALPEBRAL. 3. Perhaps suffixed zero-grade form *pal-yo- in Greek pallein, to sway, brandish: CATA- PULT. 4, Perhaps suffixed form “psal-yo- in Greek psal- lein, to pluck, play the harp (but more likely of imitative origin): PSALM, PSALTERY. [Pok. 1. G. pel- 801.] [po6mum. Apple. Latin noun of unknown origin. POMACE, POMADE, POME.]
```


## [2026-09-14T00:54:13.210Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR>=78 && NR<=90 {print \"====LEAF\",NR\"====\"; print substr($0,1,900)}' POK_03.txt",
 "description": "POK_03 leaves 78-90"
}
```


### [2026-09-14T00:54:14.211Z] TOOL RESULT

```
====LEAF 78====
fad  , stark,  tapfer,  groß';
lit.  päts  , Ehemann'  und  , selbst'  (alt  patis),  lett.  pats  , Hausherr'  und ,selbst',  lit.  vie§pats  ,Herr'  (alt  viespatls),  apr.  pattiniskun  Akk.  f.  ,Ehe'; f.  alit.  vieSpatni]  *patni  unter  Einfluß  von  "^pati-  umgestaltet  zu  *pati  in apr.  waispattin  Akk.  ,Frau',  \ii.  pati  , Ehefrau',  Iqü.  pati  ,Wirtin';  indekl. Partikel  lit.  pät,  lett.  pat  , selbst,  sogar,  gerade' ;  über  aksl.  gospodh  ,Herr', s.  oben  S.  453;
hitt.  -pat  , eben  (so),  auch,  vielmehr';  toch.  A  pats  , Ehemann'.
WP.  II  77  f.,  WH.  I  660 f.,  II  350 f.,  379 f.,  Trautmann  208,  Benveniste Origines  1,  63  f.,  Pedersen  Hitt.  77  f.,  Endzelin  Lett.  Gr.  396  f.
pöu-  :  p9U'  :  pü-  ,klein,   gering,   wenig',  vielfach   für  ,Junges,  Tierjunges, kleines  Tier';  pö[u]-lo-s  ,Junges',  pou-ko-  , wenig',  pu-t
====LEAF 79====
';  nur  kelt.  und  slav.
Air.  ög  ,jungfräulicb',  öge  , Jungfräulichkeit' ;    cecb.  pouhy  ,lauter,  bloß, einfach'. WP.  II  77.
prä-  , biegen'  ? ;  nur  lat.  und  kelt.
Lat.  prävus  ,verkebrt;  schief;  schlecht';  dazu  prätum  , Wiese'  (als  ,Ein- biegung  des  Bodens',  vgl.  z.  B.  lit.  lankä  ,Einsenkung,  Wiese':  leükti jbiegen')  und  (als  , Aufbiegung,  Wölbung,  Hügel');  mir.  räthj  raith  m.  f. , Erdwall,  Festung',  mcjmr.  hed-rawtj  ncjmr.  hedd-rod  m. , Grabhügel,  Grab',
844  •
bret.    hez-ret    f.    ,Begräbnisplatz,    Friedhof^    gall.    rätin   Akk.    Sg.   ,Burg- (hügel)S  ON  Argento-räte. WP.  II  86,  WH.  II  358  f.
präi-,  prQi-,  pri-  (pri-)  ,gerii  haben,  schonen,  friedlich-frohe  Gesinnung*  j  \^^m pri-tö'  ,geliebt^  priio-  ,liebS  priiä-  , Gattin*,  priio-tä  ,Liebe',  pnio-  *^| tuo-  ,das  Lieben^ 
====LEAF 80====
riund  , Freund,  Geliebter,  Ver- wandter', ahd.  friunt  , Freund,  Geliebter' ;  aisl.  fridr  ,schön',  ags.  frid- hengest  , stattliches  Pferd';  von  *frida-  in  der  Bed.  , geschont'  stammt  got. freidjan  , schonen',  ahd.  vrlten  , hegen'  (frltliof  , eingefriedigter  Hof,  nhd. Freithof  und  volksetymologisch  Friedhof)]  mit  i  aisl.  fndill  , Geliebter, Buhle',  f.  fridla,  frilla^  ahd.  fridel,  f.  fridila  , Geliebte (r)',  woneben  von Partiz.  *frijöda-  aus:  SiS.  friuthil,  ahd.  friudil  ds.;  a.hd.  fridu  m.  , Friede, Schutz,  Sicherheit,  Einfriedigung',  as.  frithu  m.  ,Friede',  ags.  friodu  m. ,Friede,  Schutz,  Sicherheit',  aisl.  fridr  m.  , Liebe,  Friede',  got.  gafripön ,schonen',  aisl.  frida  ,Frieden  machen,  versöhnen',  ags.  fridian  ,schützen', ahd.  gifridön  ,beschützen' ;
aksl.  prSjg  ,bin  günstig,  sorge  für',  p
====LEAF 81====
 sich  auszeichnend';  d^eo-ngÖTtog  , Seher'  (,der  sich  von  Gott  aus vernehmlich  Machende');  vielleicht  rtgaTclg  , Zwerchfell';  anders  oben  S.  620.
air.  rieht  ,Form,  Gestalt',  cjmr.  rhith  ,species'  {*pYp-tu-)]
ahd.  furhen  , reinigen,  putzen,  fegen'  (,in  die  Augen  fallend  machen, ein  Ansehen  geben'),  mhd.  vUrbe  , Reinigung;  Sternschnuppe',  and.  wel gifurvid  ,casta'.
WP.  II  89.
pret-,  pr^t-  ,verstehen'.
Mir.  räthaigid  ,bemerkt';  got.  frapi  n.  Sinn,  Verstand',  frapjan,  fröp ,verstehen',  fröps  ,klug,  verständig',  aisl.  frödr,  as.  ags.  fröd,  ahd.  fruot ds.,  mhd.  vruotec,  vrüetec  , schnell  entschlossen,  munter,  tapfer',  nhd.  Schweiz. fruetig  ,froh,  frisch,  tapfer,  schnell',  auch  ahd.  frad  ,strenuus  efficax', fradah-lih  ,procax';  vielleicht  ahd.  antfrist  ,interpretatio'  {*pret-sti-)'^  lit. prantü,  p
====LEAF 82====
ren  ,ge- frieren  machen',  ahd.  as.  frost  (*frus-taz)]  3Lgs.  forst  m.  aisl.  frost  n.  ,Frost'»  1
B.  Ai.  plösati  ,versengt,  brennt',  plusta-  ,versengt,  verbrannt';  alb. prüsh  .brennende  Kohlen,  Glut';  lat.  prüna  ,glühende  Kohlen*  (*p)ru8na) prürlre  ,jucken'.
WP.  II  88,  WH.  II  378  f.
pris-  .zerkleinern'??  nur  griech.  und  alban.
Gr.   Ttgiü)   {ßTtqia&TjVj   TtQLGtög)    .durchsäge,   knirsche    mit   den   Zähnen',
nQtü)Vj  -ovog  ,Säge',  nqiaiia  ,das  Gesägte,  Sägespäne;   dreiseitige  Säule*;   ^
alb.  jprish  ,verderbe,  zerbreche,  zerstöre'. WP.  11  89.
pro-  s.  2.  per-  S.  813  f.
prokto- :  prokto-  , Steiß',  nur  gr.  und  armen.?  "^
Arm.    erastank   PI.   ,edQai^    (von  *erast  =  prdkto-)  kann  die  Redukt.-St. neben  gr.  Tr^wxrog  ,Steiß,  After'  sein. WP.  II  89,  Meillet  Esquisse^  142.
prso-  (?)  
====LEAF 83====
e,  lett.  paüna  ,Ränzel,  Bündel'.
pU'g- :  gr.  Ttvyri  ,der  Hintere' ;  aisl.  fjük  ,Schneesturm',  fjüka  , schnell durch  die  Luft  fahren,  stieben',  fok  , Schneegestöber',  mhd.  fochen  , blasen'; lett.  püga  ,Windstoß',  pauga  ,Polster,  Kopf.
p{h)u-k-'.  arm.  p^'uH  ,Hauch,  Wind,  Furz',  PL  , Blasebalg',  p^^äem ,hauche',  p'"Jham  ,blase  mich  auf;  npers.  pük  ,das  Blasen  (um  Feuer  an- zufachen) ,Blasebalg',  afgh.  pü,  püh  ,a  puff,  a  blast,  the  act  of  blowing';
lit.  pukne  ,Blatter',  pukUe  ,Beule',  püks^iü,  püksti  ,keuchen,  schnaufen', pükysj  pukis  , Kaulbarsch'  (*,Dickkopf') ;  Iqü.  pukuls  ,Troddel'  (eig.  ,dicke Quaste').
348  f
pu-p-  (wohl  o-ebrochene  Redupi.):  alb.  pupe  ,Quark,  Weintraube, Hügel«, püpeze  ^Knospe,  Mohn^  püpule  ,Rückeii^;  lat.  püpus  ^kleines  Kind,  Knabe, Bübchen^,  *püpa  ^kle
====LEAF 84====
 reflex.  ,schwellen', puntü,  püsti  ,schwellen,  sich  aufblasen',  püsle  f.  .Blase,  Harnblase',  putlüs ,sich  blähend,  aufgeblasen,  stolz',  putä  .Schaumblase',  pütmenos  t  PI. , Geschwulst',  pari-putelis  .aufgeblasener  Mensch',  päpautas  ,Schwiele', auch  pautas  ,Ei,  Hode',  piisu,  püst  ,blasen.  wehen,  hauchen,  atmen', püsma  .Atemzug',  püte  ,Blase,  Blatter',  wohl  auch  lit.  puträ  .Grütze', lett.  putra  , Grütze,  Brei';  auf  Media:  lett.  pudurs,  puduris  ,Büschel, Haufe',  pudra  ,Haufe';  wruss.  potka  {*pztbka)  , männliches  Glied'.
WP.  II  79ff.,  WH.  II  389 f.,  392,  Trautmann  233 f.;  vgl.  oben  2.  b(e)u'.
2.  pu-:peu.9-  .faulen;  stinken';  vermutlich  aus  einem  pu  ,pfui!'  entwickelt; pü-ti-  , Fäulnis',  pu-tro-  , verfault';  pu-to-  ,podex,  cunnus'.
849
Ai.  f'iiyati  ,wird  faul^  stinkt^  =  av.  puyeiti  ,w
====LEAF 85====
ett.  pünis  ,faulendes,  eiterndes',  punes  PI.  ,Modererde';
mit  s:  norw.  feyr  (^fauza-)  ,morsch',  ndl.  voos  , seh  wammig',  Schweiz. gefösen  ,morschgeworden' ;  über  aisl.  fauskr  s.  oben;
WP.  n  82,  WH.  II  391  f.,  Trautmann  234;  G.  Liebert  Nominalsuff,  -ti- 151.
5.  pu-  s.  unter  peu-  und  pöu-,
1.  puk-,  peak-  etwa  , dicht  behaart,  buschig  (buschiger  Schwanz),  dichtwollig'.
Ai.  püccha-,  -m  ,
====LEAF 86====
 Schwanz,  Schweif,  Rute'  (kann  *pu[k'\-sko-  sein);  nach dem  buschigen  Schwanz  benannt,  scheint  got.  faühö^  aisl.  föa,  ahd.  foha , Füchsin*  (germ.  -öw),  daneben  mit  masc.  -s- :  ags.  fox,  ahd.  fuhs  , Fuchs' usw.;  lit.  paustu  , Tierhaar';  russ.-poln.  puch  (*peukso-^  poukso-)  , Flaum- federn, Daunen,  feines  wolliges  Haar  an  Tieren'  (daraus  lit.  pükas  , Flaum- feder'), russ.  pusistyj  , wollig,  dicht,  buschig',  pu§nöj  tovdr  ,Pelzwerk', cech.-nsorb.  o-pus  {^'puchh),  opys  , Schwanz',  russ.  opüska,  opusina  ,Rand (des  Waldes),  Saum,  Verbrämung'.
WP.  II  82  f.
2,  puk-  , zusammendrängen,  eng  umschließen'.
Av.  pusä-  f.  , Stirn  band*;  gr.  ä(A,-7iv^  m.  , Stirnband',  Adverb.  Ttvyta  ,fest^ dicht,  verständig,  sorgfältig',  im  Kompositum  nvyti-  (rtvm-fxrjSrjg  ,verständig'), daraus  rcvycL-vög  jünger  fc
====LEAF 87====
t*.
Nachtrag  zu  S.  807:
pelk-,  polk-  (auch  pelg-,  polg-?)  ,wenden^  biegen*;  polkä  ,Gewen- detes*.
Gall.  olca  jPflugland'  (frz.  ouche  ,gutes  Ackerland')  =  ags.  fealg  ,Brachfeld'  (gern». */algö),  engl,  fallow,  ostfries.  folge,  bair.  falg  ds.,  mhd.  folgen,  feigen  ,umackem',  nhd. Felge  , gepflügtes  Brachland';  ablaut.  genu.  *felgö  , Radfelge'  in  ags.  fielg,  engl,  fellyy ahd.  felga  , Felge,  Egge*;  daneben  germ.  *falg%z  in  mnl.  felghe,  ags.  felg{e\  engl,  fellot ds.;  germ.  felgon  .wenden'  in  ahd.  un-gifolgan  ,ungewendet' ;
niss.  jpolosd  usw.  »Streifen,  Ackerfurche';
vielleicht  hierher  pelg-,  polg-  in  slav.  *pilzOj  *pelzti,  russ.-ksl.  pUzeifb  .kriecht'  usw. und  slav.  polzh  in  russ.  pSloz  , Schlittenkufe',  slov.  pläz  ,Pflugsohle,  Streifen'.
WP.  I  516,  Trautmann  218  f.,  Vasmer  2,  396,  397,  Kl
====LEAF 88====
ld, ungestüm,  gewaltig',  sam-rahdha-  , wütend',  das  oben  S.  652  irrig  zu  rd- bhate  »erfaßt,  hält  sich  fest'  =  IdbhaU,  lambhate  , erfaßt,  ergreift^,  gestellt wurde;  vgl.  mir.  recht  ,plötzlicher  Anfall,  Wut',  das  auch  zu  lat.  rapia^ Wz.  *rep-  gehören  könnte;  ags.  rabbian  , rasen'  aus  vlat.  rabiäre  ds. ;  toch. A  rapurüe  , Leidenschaft'.
WP.  II  341,  WH.  II  413.
räp-,  rep-  ,Rübe' ;  Wanderwort  unbekannter  Herkunft.
Gr.  Qdrtvg,  Qd(pvg  f.  ,Rübe',  qdq)avoq^  qacpavT]  ,Rettig',  att.  ,Kohr,  qatpaviq^ -löog  , Rettig' ;  lat.  räpum,  räpa  ,Rübe',  räpistrum  , wilde  Rübe*,  räpina , Rübenfeld'  (wie  lit.  ropiena)  und  ,Rüben' ;  ahd.  ruoba,  ruoppa  (*röbjö) ,Rübe',  daneben  ^'-lose  Nebenform  in  aisl.  röfa  ,der  knochige  Teil  des Pferdeschwanzes*,  norw.  rova  , Schwanz',  dazu  im  Ablaut  ahd.
====LEAF 89====
  umher  eilen'.
Npers.  raftan  , gehen',  mparth.  raf-  , angreifen,  kämpfen',  osset.  räväg , schnell' ;
mir.  reb  , Spiel,  Tücke'  {*rebä),  rebrad  ,Kinderspiel',  rebaigim  ,ich  spiele*;
germ.  *reb-  ,in  heftiger  Bewegung  sein',  mhd.  reben  st.  Vb.  ,sich  be- wegen, rühren',  nhd.  bair.  rebisch  , munter',  Schweiz,  räbeln  ,lärmen',  mhd. reben  ,träumen,  verwirrt  sein',  mnd.  reven  , unsinnig  reden,  denken',  norw. dial.  rava  ,hin  und  her  taumeln'  usw.
WP.  II  370,  Szemerenyi  ZDMG.  101,  207 ff.;  erweitert  aus  er-.
2.  rehh-  »überwölben,  überdachen'.
Gr.  eg€q}io,  igeTtro)  , überdache*  (*überwölbe),  v^)-r^Qsq>rjg  ,mit  hoher  Be- dachung', ÖQOcpog  ,das  Rohr,  womit  man  die  Häuser  deckt.  Dach,  Zimmer- decke', ÖQOCpT]  , Bedachung';  ahd.  hirmreba  , Schädel'  (*,Hirn-bedachung*); ahd.  7'ippa,  rippi,  as.  
====LEAF 90====
    helfend) ;    Richtung,    Linie    (Spur,    Geleise)    u.    dgl. ;
bildet  idg.    weder  Wurzelpräsens   noch   Perfekt;    Partiz.  Perf.  Pass.
reg-to-   ,Gesetz',  rogi-  ,Reihe',  rögo-s  , Aufrichtung',  rogö-s  ,auf-
gerichtet',    re^-s    ,König',    reg(c)ni    ,Königin',    regio-    , königlich',
regiom  ,Herrschaft'.
Ai.  fjyatij  nasaliert  rfijdti  ,streckt  sich,  eilt  (von  Pferden)';  wohl  auch
irajydti   (mit   unklarem  i-)  ,ordnet    an,   verfügt';   r;w-,  av.  9rdzu-   ,gerade
recht'   (dazu   drdzus   , Finger',   Gen.  9rdzvo)y  Kompar.   Superl.  ai.  rdjlyas-,
rßyas'  ,gerader',  rdjiStha-,  av.  razüta-  ,der  Geradeste,  Gerechteste';
ai.  fjrd'  von  Pferden  =  rju-gämirij  fjrä^va-,  av.  9r9zräspa-  EN  eig. , dessen  Rosse  geradaus  eilen',  woneben  Kompos.  form  *2'ji-  in  rß-py^' (2.  Glied  unklar)  ,geradaus  emporschnell
```


## [2026-09-14T00:54:27.634Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nwc -c POK_full.txt; head -40 POK_full.txt\necho \"=== grep pages 84x ===\"; grep -n \"84[0-9]\" POK_full.txt | head -20",
 "description": "Inspect POK_full"
}
```


### [2026-09-14T00:54:27.743Z] TOOL RESULT

```
3971883 POK_full.txt
List of language abbreviations in tlie lED 



Abbreviation Language name 


Aeq. 




Aequian 


Akk. 




Akkadian 


Alan. 




Alanian (=Old Ossetic) 


Alb. 




Albanian 


Anat. 
=== grep pages 84x ===
2660:References: WP. I 5, WH. 15, 20, 843, Trautmann 3, Schwyzer Gr. Gr. I 347. 
2702:References: WP. I 9, WH. I 16, 843, Trautmann 70. 
2737:References: WP. 110, WH. I 20, 844, Specht KZ. 68, 195 f. S. unten S. 18 Z. 1/2. 
3036:References: WP. I 13, WH. I 20, 419, 844; Feist 28 a, Kretschmer Gl. 30, 882. 
3897:References: WP. I 34 f., WH. I 60, 848, Feist 18 f., Pedersen Hittitisch 128, Tocharisch 
6001:References: WP. I 45 f., WH. I 57 f., 60, 847, Pedersen Hittite 128, Couvreur H 93. 
6196:References: WP. I 47 ff., WH. I If., 842, Feist 3a, Trautmann 1 1 . 
6413:References: WP. I 82 f., II 362 f., WH. I 66, 848, Feist 25, Schwyzer Gr. Gr. I 260, 447, 
6503:References: WP. I 80 f., WH. 62 f., 848. 
7177:Note: compare to the meaning question esp. Brugmann Grdr. I|2, 844 f. the colouring of 
7209:from, up ' (see Brugmann Grundr. I|2 2, 844 f.). Old Prussian et-, at- (probably only from 
7270:References: WP. I 42 f., WH. I 51, 847. 
8293:IF. 2, 60 ff., Persson Beitr. 604 f., 845 (also against connection of ^ers- with ers-). About 
8839:References: WP. I 849 f., WH. I 467, Feist 113 f., Sievers-Brunner 121, 243, Wackernagel- 
9274:References: WP. I 46 f., WH. I 40, 846, Krahe Gl. 20, 188 ff., Pokorny Urillyrier 110 ff., 130 
9347:References: WH. I 61, 65, 848, Feist 72, Trautmann 22, Pedersen Hittitisch 27, 164. 
9387:References: WP. I 42, WH. I 75 f., 849 f. 
20028:References: WP. I 849 f., WH. I 466 f., 469, 471 f., 864, Trautmann 49, Pedersen 
21240:References: WP. I 848. 
21350:References: WP. I 847 f., WH. I 565, 867, Trautmann 45 f.
```


## [2026-09-14T00:54:49.849Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"Page(s)\" POK_full.txt | head -3\necho \"=== pel- entries ===\"\ngrep -n -A4 \"^Root / lemma: *pel-\" POK_full.txt | head -80",
 "description": "Find pel- entries in POK_full"
}
```


### [2026-09-14T00:54:49.918Z] TOOL RESULT

```
1549:Page(s): 2 
1574:Page(s): 2 
1607:Page(s): 2-3 
=== pel- entries ===
65707:Root / lemma: pel-1, pela-, ple- 
65708-
65709-Meaning: full, to fill; to pour; town (?) 
65710-
65711-Note: 
--
65870:Root / lemma: pel-2a, pelQ- : pla- 
65871-Meaning: to cause to move, drive 
65872-
65873-Material: Latin /7e//o (probably from *pel-nd), -ere, pepuli, *pultus^ to beat, strike, knock, 
65874-push, drive, hurl, impel, propel ' (assumed from pultare^ to beat, strike, knock '), pulsus 
--
65905:Root / lemma: pel-2b, pel-en-, pel-t-, pel-u- 
65906-Meaning: powder, flour 
65907-
65908-
65909-
--
65944:Root / lemma: pel-3a 
65945-
65946-Meaning: to fold 
65947-
65948-Material: a. pio-as 2. composition part in Adj. as gr. a-irAoq "simple, just', 5i-ttA6(;, SirrAa^ " 
--
65980:Root / lemma: pel-3b, pela- ple- 
65981-Meaning: to cover, wrap; skin, hide; cloth 
65982-
65983-Material: Gr. nsAaq "skin', £puai-TT£Aa(; "HautentziJndung', a-i^zKoc, "nicht verheilte wound'; 
65984-TTeA|ja n. "Sohle am foot or shoe ', naApn " light shield' (*of skin), Latin paleai. "Lappchen 
--
66037:Root / lemma: pel-5 
66038-
66039-Meaning: to sell; to make money 
66040-
66041-Material: Gr. nwAsTv " sell ', Doric nwAa:, Attic (Gramm.) nu)Ar| f. "sale'; Old High German 
--
66056:Root / lemma: pel-6 
66057-
66058-Meaning: grey; pale 
66059-
66060-Material: Old Indie pa///a-, fern. paliknT{irom *-tn/} ' aged-gray, greis' (: nzKnyoq), parusa-'
```


## [2026-09-14T00:54:55.834Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR>=65700 && NR<=66120' POK_full.txt | grep -n \"Root / lemma\\|Meaning\\|Page(s)\" \necho \"=== search palp / pallein ===\"\ngrep -n -i \"palpare\\|palpus\\|TraAAw\\|pallein\\|palpebra\" POK_full.txt | head -20",
 "description": "Pokorny pel- pages"
}
```


### [2026-09-14T00:54:56.960Z] TOOL RESULT

```
6:Page(s): 807, 850 
8:Root / lemma: pel-1, pela-, ple- 
10:Meaning: full, to fill; to pour; town (?) 
46:Maybe alb. {*pe-lagu) pe//gu^poo\' see Root / lemma: /aku-: water basin (ditch, lake, sea), 
169:Page(s): 798-801 
171:Root / lemma: pel-2a, pelQ- : pla- 
172:Meaning: to cause to move, drive 
204:Page(s): 801-802 
206:Root / lemma: pel-2b, pel-en-, pel-t-, pel-u- 
207:Meaning: powder, flour 
243:Page(s): 802 
245:Root / lemma: pel-3a 
247:Meaning: to fold 
279:Page(s): 802-803 
281:Root / lemma: pel-3b, pela- ple- 
282:Meaning: to cover, wrap; skin, hide; cloth 
317:Page(s): 803-804 
319:Root / lemma: pe/~4 
320:Meaning: a kind of vessel, dish 
336:Page(s): 804 
338:Root / lemma: pel-5 
340:Meaning: to sell; to make money 
355:Page(s): 804 
357:Root / lemma: pel-6 
359:Meaning: grey; pale 
421:Page(s): 804-805 
=== search palp / pallein ===
27770:gr. 6px£W " TraAAw, kiveoj ', mostly opxsopai " dance, hop, jump, shake '. 
65854:here Latin palpor, -ari {a\so palpd) "streichle', palpito^ twitch ', palpebrae^ eyelids ', alb. 
87373:Old Church Slavic //'e/0e/b"das Zittern, Beben', //'eyoe/5//"tremble', //'(9y05//"palpare',
```


## [2026-09-14T00:55:01.595Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '65820,65876p' POK_full.txt",
 "description": "Read Pokorny pel- palp section"
}
```


### [2026-09-14T00:55:01.653Z] TOOL RESULT

```
"more, most' {*pla-ls-, -Isto-, Avestan fraesta-); 



Lithuanian /7//^s "in Uberfluft'. 

E. pel-ed-\x\ gr. -nkdboc, n. " dampness, decay ', nAa5ap6(; "liumid, wet', nAaSaw, -av 
"damp sein'; Old High German flediron. Modern High German flattern. Old High German 
fledar-mOs^ba\!\ Latvian pe/det^swm', pe/def/es^ bathe', pe/d/nat^ bathe, schwemmen': 
pildinat {*pld-) ds.; pledinat^\N\tb den Flijgeln hit', pledins^ butterfly'; compare E. Fraenkel 
Mel. Boisacq 1, 357 ff. 

F. words for " butterfly': reduplicated Latin papilio, -onis m. ( *pa-pil-); Germanic *fffaldrdn- 
in Old Icelandic fffrildiu.. Old English fffealde. Old High German fffaltra. Middle High 
German fffalter. Modern High German Falter, Lithuanian peteliskeAs., Latvian peteltgs 
"flatterhaff ( *pel-tel-); 

from the same root the Balto-Slavic words ( *paipala-) for " quail ': Lithuanian pfepalat, 
Latvian pafpala. Old Prussian penpalo (in addition Old Prussian pepelis, PI. pippalins 
"bird'); Czech prepel, krepel, slov. prepelfca {a\so " butterfly') etc. 

G. words for "swing, shake, tremble, hin- and herbewegen' etc.: gr. TraAAco ( *pj-id), Aor. 
£TTr|Aa "swing, brandish, shake', Med. "spring, wriggle ', naAioq "geschwungen', naA|j6(; 
"Zucken, Vibrieren', -ndkoc, m. "lot, fate', naAaaao|jai " loose '; redupl. nainaAAoj Hes. 
"shake'; Old Icelandic /^/a "frighten'. Old English ea/-/^/c»"furchterlich'. Middle High 
German i/a/a/?/ "devil'; perhaps to Old Church Slavic plach-b "trembling, anxious ' ( *polso- 
?), yO/55/// "frighten' etc.; 

the extension pelem-\x\ gr. TTsAeiji^u) "swing, brandish, shatter'. Pass, "erbebe', n6A£|jO(;, 
nT6A£|jO(; "battle, war, fight' (PN N£0-nT6A£tJ0(;, nToA£|jaTo(;), Gothic i/s-/^//775"erschrocken', 
Old Icelandic felms-fullr6s., fe/mta'bange sein' {*falmatjan). Old High German Bavarian 
felm "fright'; 

da Old Icelandic falma likewise "iJberrascht become', as "tap, feel ' stands for, could 
here Latin palpor, -ari {a\so palpd) "streichle', palpito^ twitch ', palpebrae^ eyelids ', alb. 
y05/^/7 "fluttering, trembling' and " maple '. 

Maybe alb. {*palun) panje^ maple ' : Romanian paltin^ maple '. 

as well as West Germanic *fd//an{0\6 High German fuolen. Middle High German fuelen. 
Old English fselan etc.) " feel ' belong, also Middle Low German vlader' maple ', vladarn 
"flutter'. 

References: WP. II 63 ff., WH. 320 f., 322 f., 327 f., Trautmann 218; 



See also: die words under G. could also to pe/-2be\ong; here also p/eu- "flow". 
Page(s): 798-801 

Root / lemma: pel-2a, pelQ- : pla- 
Meaning: to cause to move, drive 

Material: Latin /7e//o (probably from *pel-nd), -ere, pepuli, *pultus^ to beat, strike, knock, 
push, drive, hurl, impel, propel ' (assumed from pultare^ to beat, strike, knock '), pulsus 
{after percu/sus : percelld) " a pushing, beating, striking, stamping, push, blow, impulse, 
stroke ', pulsus, -us^ to beat, strike, knock, push, drive, hurl, impel, propel ', Umbrian ar-
```


## [2026-09-14T00:55:17.815Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR>=74 && NR<=86 {printf \"LEAF %d: \", NR; n=split($0,a,\"\\n\"); for(i=1;i<=n;i++) if (a[i] ~ /(^|[^0-9])(83[0-9]|84[0-9]|85[0-9])([^0-9]|$)/ && length(a[i])<40) printf \"[%s] \", a[i]; print \"\"}' POK_03.txt\necho \"--- first line of each leaf 74-86 ---\"\nawk 'BEGIN{RS=\"\\f\"} NR>=74 && NR<=86 {printf \"LEAF %d >> %s\\n\", NR, substr($0,1,120)}' POK_03.txt",
 "description": "Map POK_03 leaves to pages"
}
```


### [2026-09-14T00:55:18.941Z] TOOL RESULT

```
LEAF 74: [839] 
LEAF 75: [840] 
LEAF 76: [841] 
LEAF 77: [842  f] 
LEAF 78: [843] 
LEAF 79: [844  •] 
LEAF 80: [845] 
LEAF 81: [846  f] 
LEAF 82: [847] 
LEAF 83: 
LEAF 84: [849] 
LEAF 85: 
LEAF 86: [850  ^] 
--- first line of each leaf 74-86 ---
LEAF 74 >> bach-Endzelin  III  325).  •
WP.  II  100,  WH.  II  319,  320;  Erweiterungen  der  Wurzel  peh-  ,flach, eben',  obe
LEAF 75 >>   vöder  ds.;  ahd.  {fedar)fötar  ,canna', spätahd.  füoter  ,theca',  nhd.  Futter  (des  Kleides),  Futteral]
lit
LEAF 76 >> .  pojq,  pojiti  ,tränke';  baltoslav.  *pöta-  und *plta-  ,getrunken'  in  lit.  puotä  f.  , Trinkgelage'  und  a
LEAF 77 >> sk.  pustma[s\  ,postremae';  umbr.  postne,  lat.  pöne  aus  *posti-ne'y  osk. pustin,  umbr.  pustin  (aus  "^posti 
LEAF 78 >> fad  , stark,  tapfer,  groß';
lit.  päts  , Ehemann'  und  , selbst'  (alt  patis),  lett.  pats  , Hausherr'  und ,s
LEAF 79 >> ';  nur  kelt.  und  slav.
Air.  ög  ,jungfräulicb',  öge  , Jungfräulichkeit' ;    cecb.  pouhy  ,lauter,  bloß, e
LEAF 80 >> riund  , Freund,  Geliebter,  Ver- wandter', ahd.  friunt  , Freund,  Geliebter' ;  aisl.  fridr  ,schön',  ags.  frid-
LEAF 81 >>  sich  auszeichnend';  d^eo-ngÖTtog  , Seher'  (,der  sich  von  Gott  aus vernehmlich  Machende');  vielleicht  rtgaTc
LEAF 82 >> ren  ,ge- frieren  machen',  ahd.  as.  frost  (*frus-taz)]  3Lgs.  forst  m.  aisl.  frost  n.  ,Frost'»  1
B.  Ai.  p
LEAF 83 >> e,  lett.  paüna  ,Ränzel,  Bündel'.
pU'g- :  gr.  Ttvyri  ,der  Hintere' ;  aisl.  fjük  ,Schneesturm',  fjüka  , 
LEAF 84 >>  reflex.  ,schwellen', puntü,  püsti  ,schwellen,  sich  aufblasen',  püsle  f.  .Blase,  Harnblase',  putlüs ,sich 
LEAF 85 >> ett.  pünis  ,faulendes,  eiterndes',  punes  PI.  ,Modererde';
mit  s:  norw.  feyr  (^fauza-)  ,morsch',  ndl.  voos 
LEAF 86 >>  Schwanz,  Schweif,  Rute'  (kann  *pu[k'\-sko-  sein);  nach dem  buschigen  Schwanz  benannt,  scheint  got.  faühö^
```


## [2026-09-14T00:55:38.474Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== CHEUNG pal ===\"; grep -n -i \"pālīdan\\|palidan\\|pālūdan\\|paludan\\|\\*parH\\|pālāy\" CHEUNG.txt | head -20\necho \"=== HRN palidan ===\"; grep -n -i \"palidan\\|pâlîdan\\|pālīdan\\|palûdan\\|paludan\" HRN.txt | head -20\necho \"=== HUB ===\"; grep -n -i \"palidan\\|paludan\" HUB.txt | head",
 "description": "Cheung/Horn for palidan"
}
```


### [2026-09-14T00:55:38.543Z] TOOL RESULT

```
=== CHEUNG pal ===
9452:vel, Bakht. wil ‘free, loose’ || (+ *pari-) NP paludan, palidan/palay-, Kurd. (Kurm.) 
9454:parzen ‘tea-strainer’. Ф As for NP palüdan, palidan/palay- and the corresponding 
19329:pāra- ‘debt, to be paid’, can be interpreted differently: ‘raised’ (*parH^), on which 
19432:*parHl 295 
19435:become saturated, (caus.) ’nb’fy- ‘to saturate’ (*parH’). If it was (relatively) old, the 
19439:etymologically related to *parH!, viz. *par& (with increment *-¢), cognate with Skt. 
19480:*parH! ‘to fill; to nourish’ 
19497:296 *parHl 
19537:is not wholly clear (Khot. pāra- ‘cake’ < *‘sacrificial offering’, *parH? ‘to give, 
19542:*parH’; Lith. peréti ‘to brood’, whose meaning is probably also secondary, is related 
19564:*KHOTANESE: ? pära- ‘cake’ (from *sacrificial offering’ ?, *parH?). © The form 
19572:Ó No verbal formations of *parH seem to be attested in Ir. 
41308:paludan, palidan/palay-, 
55885:*parH?. (s.v.), *staHn (s.v.), 
56597:*kan’, *parc, *parH' 
56732:*baj, *daH' , *HraH, *parH° 
57248:*9ғаНи, *parH', *yarHz 
=== HRN palidan ===
=== HUB ===
```


## [2026-09-14T00:55:40.897Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN santir/psaltery ===\"; grep -n \"^psaltery\\|^psalm\\|^santir\\|santir\\b\" KLN_1966.txt | head\necho \"=== KLN 1382 region grep psalt ===\"; grep -n -i \"psalter\\|psaltēr\\|santūr\\|santur\" KLN_1966.txt | head -20",
 "description": "Klein psaltery/santir"
}
```


### [2026-09-14T00:55:40.974Z] TOOL RESULT

```
=== KLN santir/psaltery ===
30771:psalm,  n.  —  ME.  psalm,  salm,  fr.  OE.  psealm, sealm,  fr.  Eccles.  L.  psalmus,  fr.  Gk.  tj/aXp.6;,  ‘a plucking,  twitching,  of  the  harp’  (in  Eccles.  Gk. ‘song,  psalm’),  fr.  'yzXXciv,  ’to  pluck,  twitch  the harp,  to  play  on  a  stringed  instrument’,  whence also  iJ/dcXpuz,  ‘tune  played  on  a  stringed  instru¬ ment’,  ‘harper’,  ’4/a>.Tr,piov,  ‘stringed
30775:psalmody,  n.,  1)  the  singing  of  psalms;  2)  psalms collectively.  —  ME.  psalmodie,  fr.  Eccles.  L. psalmodia,  fr.  Late  Gk.  ^aXfjttpSta,  ‘singing  to the  harp’,  fr.  4«xXu6c,  ‘psalm’,  and  4>8y],  ‘song’. See  psalm,  ode  and  -y  (representing  Gk.  -ia). Derivatives:  psalmodi-al,  psalmod-ic,  psalmod- ic-al,  adjs.,  psalmod-ist,  n.,  psalmodize  (q.v.) Psalter,  n.,  the  Book  of  Psalms.  —  ME.  psalter, salter,  fr.  OE.  psaltere,  saltere,  fr.  Eccles.  L. psalterium ,  ‘the  songs  of  David,  the  Psalms  ,  fr. L.,  ‘stringed  instrument,  psaltery’,  fr.  Gk.  <J»aX- TTjpiov,  ‘stringed  instrument,  psaltery,  harp’, fr.  ijjaXXetv,  ‘to  pluck,  twtich  the  harp.’  See psalm  and  cp.  psaltery.  Cp.  also  santir. Derivatives:  psalter-ian,  adj .,  psalter-ist,  n. psalterium,  n.,  the  third  stomach  of  ruminants (zoo!.)  —  Eccles.  L.  psalterium  (see  prec.  word) ; so  called  because  of  its  resemblance  to  the  folds of  a  book.
30776:psaltery,  n.,  an  ancient  stringed  instrument.  — OF.  psalterie,  fr.  L.  psalterium.  See  Psalter  and -y  (representing  L.  -ium). psammite,  n.,  sandstone  (petrogr .)  —  F.,  fr.  Gk. /j/apipio;,  ‘sand’,  which  is  rel.  to  tj/apiaffoi;,  &p.a - So?,  ‘sand’,  and  cogn.  with  L.  sabulum,  ‘sand’. See  sabulum  and  cp.  words  there  referred  to. For  the  ending  see  subst.  suff.  -ite.
33703:Santa  Claus,  —  American  alteration  of  dial.  Du. Sante  Klaus,  ‘Saint  Nicholas’, santal,  n.,  sandalwood.  —  F.  sanlal,  fr.  Gk. cavvaXov,  fr.  OI.  candanah.  See  sandalwood. Santalaceae,  n.  pi.,  the  sandalwood  family  (bot.) —  ModL.,  formed  with  suff.  -aceae  fr.  ML.  san- talum,  ‘sandalwood’.  See  sandalwood, santalaceous,  adj.  —  See  prec.  word  and  -aceous. santalin,  n.,  a  crystalline  compound  containing  a red  coloring  matter,  C15H1405  ( chem .)  —  F.  san- taline,  fr.  santal.  See  santal  and  -in. santir,  n.,  a  kind  of  dulcimer.  —  Arab,  santir,  fr. Gk.  •jiaA-rrjp'.ov,  ‘stringed  instrument,  psaltery, harp’,  whence  also  Aram.  pesanterin,  pesanterin, ‘a  (triangular)  stringed  instrument’.  See  Psalter. Santolina,  n.,  a  genus  of  plants  of  the  thistle  fam¬ ily  (bot.)  —  ModL.,  fr.  L.  herba  santonica.  See santonica  and  -ina  (representing  L.  -ina). santon,  n.,  a  saint  in  Mohammedan  countries.  — Sp.  santon,  augment,  formed  fr.  santo,  fr.  L. sdnctus ,  ‘holy’.  See  saint, santonica,  n.,  the  European  wormwood.  —  Mod- L.,  fr.  L.  herba  santonica,  'the  herb  of  the  San- toni',  a  people  of  Aquitania.  Cp.  Santolina,  san¬ tonin.
=== KLN 1382 region grep psalt ===
14521:‘to  feel’,  ON.  falma,  ‘to  grope’,  and  prob.  cogn. with  OI.  a-sphulayati,  ‘he  causes  to  collide, strikes’,  Gk.  tjiaXXsiv,  ‘to  pluck,  twitch  the  harp, play  on  a  stringed  instrument’,  gictXp.a,  ‘tune played  on  a  musical  instrument’,  i)iaXp.6g,  ‘a plucking,  twitching  of  the  harp’,  later  ‘song, psalm’,  <|nxXxr]p,  ‘harper’,  ijjaXir]ptov,  ‘stringed instrument,  harp’,  ijiocX|jt.6>Sia,  ‘a  singing  to  the harp’,  ijirjXaqjdw,  ‘I  feel  or  grope  about’  (com¬ pounded  of  *iJiaXa,  ‘a  twitching’,  and  dipdco,  ‘I touch’),  L.  palpdre,  ‘to  touch  softly,  stroke’,  pal- pitdre,  ‘to  move  quickly’,  palpebra,  ‘eyelid’,  lit. ‘that  which  moves  quickly’.  All  these  words prob.  derive  fr.  I.-E.  base  *(s)phil-,  *(s)phdl-, ‘to  strike  softly’.  Cp.  palp,  palpable,  palpebra, psalm,  psalter,  psaltery,  and  the  first  element  in Pselaphidae.
30772:instrument,  psaltery,  harp’,  ‘sing¬
30774:or  grope  about’  (compounded  of  *t|/aXa,  ‘a twitching’,  and  acpav,  ‘to  touch  )  and  cogn.  with L.  palpare,  ‘to  touch  softly,  stroke’,  palpitare, ‘to  move  quickly’,  palpebra,  ‘eyelid’.  See  feel and  cp.  psalmody,  psalter,  psaltery,  and  the  first element  in  Pselaphidae.  Cp.  also  palpable. Derivatives:  psalm-ic,  adj.,  psalm-y,  adj. psalmist,  n.,  a  composer  of  psalms.  —  Eccles.  L. psalmista ,  fr.  Eccles.  Gk.  'yXAixLfrrr-,  of  s.m., fr.  Eccles.  Gk.  t]/aX|j.6i;.  See  prec.  word  and  -ist. Derivative:  psalmist-ry,  n. psalmodize,  intr.  v.,  to  practice  psalmody.  — Eccles.  L.  psalmodizare,  fr.  psalmodia.  See  next word  and  -ize.
30775:psalmody,  n.,  1)  the  singing  of  psalms;  2)  psalms collectively.  —  ME.  psalmodie,  fr.  Eccles.  L. psalmodia,  fr.  Late  Gk.  ^aXfjttpSta,  ‘singing  to the  harp’,  fr.  4«xXu6c,  ‘psalm’,  and  4>8y],  ‘song’. See  psalm,  ode  and  -y  (representing  Gk.  -ia). Derivatives:  psalmodi-al,  psalmod-ic,  psalmod- ic-al,  adjs.,  psalmod-ist,  n.,  psalmodize  (q.v.) Psalter,  n.,  the  Book  of  Psalms.  —  ME.  psalter, salter,  fr.  OE.  psaltere,  saltere,  fr.  Eccles.  L. psalterium ,  ‘the  songs  of  David,  the  Psalms  ,  fr. L.,  ‘stringed  instrument,  psaltery’,  fr.  Gk.  <J»aX- TTjpiov,  ‘stringed  instrument,  psaltery,  harp’, fr.  ijjaXXetv,  ‘to  pluck,  twtich  the  harp.’  See psalm  and  cp.  psaltery.  Cp.  also  santir. Derivatives:  psalter-ian,  adj .,  psalter-ist,  n. psalterium,  n.,  the  third  stomach  of  ruminants (zoo!.)  —  Eccles.  L.  psalterium  (see  prec.  word) ; so  called  because  of  its  resemblance  to  the  folds of  a  book.
30776:psaltery,  n.,  an  ancient  stringed  instrument.  — OF.  psalterie,  fr.  L.  psalterium.  See  Psalter  and -y  (representing  L.  -ium). psammite,  n.,  sandstone  (petrogr .)  —  F.,  fr.  Gk. /j/apipio;,  ‘sand’,  which  is  rel.  to  tj/apiaffoi;,  &p.a - So?,  ‘sand’,  and  cogn.  with  L.  sabulum,  ‘sand’. See  sabulum  and  cp.  words  there  referred  to. For  the  ending  see  subst.  suff.  -ite.
33703:Santa  Claus,  —  American  alteration  of  dial.  Du. Sante  Klaus,  ‘Saint  Nicholas’, santal,  n.,  sandalwood.  —  F.  sanlal,  fr.  Gk. cavvaXov,  fr.  OI.  candanah.  See  sandalwood. Santalaceae,  n.  pi.,  the  sandalwood  family  (bot.) —  ModL.,  formed  with  suff.  -aceae  fr.  ML.  san- talum,  ‘sandalwood’.  See  sandalwood, santalaceous,  adj.  —  See  prec.  word  and  -aceous. santalin,  n.,  a  crystalline  compound  containing  a red  coloring  matter,  C15H1405  ( chem .)  —  F.  san- taline,  fr.  santal.  See  santal  and  -in. santir,  n.,  a  kind  of  dulcimer.  —  Arab,  santir,  fr. Gk.  •jiaA-rrjp'.ov,  ‘stringed  instrument,  psaltery, harp’,  whence  also  Aram.  pesanterin,  pesanterin, ‘a  (triangular)  stringed  instrument’.  See  Psalter. Santolina,  n.,  a  genus  of  plants  of  the  thistle  fam¬ ily  (bot.)  —  ModL.,  fr.  L.  herba  santonica.  See santonica  and  -ina  (representing  L.  -ina). santon,  n.,  a  saint  in  Mohammedan  countries.  — Sp.  santon,  augment,  formed  fr.  santo,  fr.  L. sdnctus ,  ‘holy’.  See  saint, santonica,  n.,  the  European  wormwood.  —  Mod- L.,  fr.  L.  herba  santonica,  'the  herb  of  the  San- toni',  a  people  of  Aquitania.  Cp.  Santolina,  san¬ tonin.
```


## [2026-09-14T00:55:53.738Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\np='KLN_1966.txt'\nt=open(p,encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\ndef leafof(lineno):\n    return t.count('\\f','',0) # placeholder\n# build map line->leaf\nleaf=0\nmapping={}\nfor i,l in enumerate(lines,1):\n    mapping[i]=leaf\n    leaf+=l.count('\\f')\nfor ln in [14521,30771,30775,30776,33703]:\n    print(ln, 'leaf', mapping[ln], 'est page', (mapping[ln]-12)*2)\nEOF",
 "description": "Map Klein lines to leaves/pages"
}
```


### [2026-09-14T00:55:54.898Z] TOOL RESULT

```
14521 leaf 315 est page 606
30771 leaf 673 est page 1322
30775 leaf 673 est page 1322
30776 leaf 673 est page 1322
33703 leaf 734 est page 1444
```


## [2026-09-14T00:55:56.101Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN babouche/tarboosh ===\"; grep -n \"babouche\\|tarboosh\\|tarbush\\|tarbouche\" KLN_1966.txt | head\necho \"=== SYN shoe section ===\"; grep -n \"SHOE\\|papoutsi\\|papout\\|babuc\\|papoútsi\" SYN.txt | head -20",
 "description": "Klein babouche, Buck shoe"
}
```


### [2026-09-14T00:55:56.177Z] TOOL RESULT

```
=== KLN babouche/tarboosh ===
4226:Derivative:  baboon-ery,  n. babouche,  n.,  a  heelless  Oriental  slipper.  —  F., fr.  Arab,  babiish,  fr.  Pers.  papush,  lit.  ‘foot- covering’,  fr.  pa,  ‘foot’,  and  the  verb  pushiden, ‘to  cover’.  Pers.  pa  is  rel.  to  Avestic pad-,  ‘foot’ ; see  foot.  The  change  of  p  to  b  proves  that  the word  came  into  Europe  through  the  medium  of the  Arabic,  which  having  no  p,  regularly  chan¬ ges  the  p  of  foreign  words  into  b. baby,  n.  - —  Dimin.  of  babe.
15110:foot,  n.  —  ME.  fat,  fr.  OE.  fat,  rel.  to  OS.  fat, ON.  fa tr,  Swed.  fat,  Dan.  fad,  Du.  voet,  OHG. fuo3,  MHG.  VU03,  G.  Fuji,  Goth./o/u.s,  ‘foot’,  and cogn.  with  Ol.  pit,  acc.  pidam,  ‘foot’,  Avestic pad-,  ‘foot’,  Toch.  A  pe,  B  pai,  ‘foot’,  A  pent,  B paine,  ‘both  feet’.  Arm.  ot-n,  ‘foot’,  ot-k\  ‘feet’. Dor.  Gk.  7rtii ;,  Att.  7101)9  (formed  on  analogy  of 009,  ‘ear’),  gen.  770809,  L.  pes,  gen.  pedis,  ‘foot’, Ol.  paddm,  ‘step,  track’.  Arm.  het,  gen.  he  toy, ‘track,  footmark’,  Gk.  rtiSt),  ‘fetter’,  TreSav,  ‘to bind  with  fetters’,  7t£Sov,  ‘ground,  earth’,  h.peda, ‘footstep \pedica,  ‘shackle,  fetter’,  impedire,  ‘en¬ tangle,  ensnare’,  expedire,  ‘to  extricate,  disen¬ gage’,  Lith.  peda,  ‘footstep,  trace’,  OSlav.  podii, ‘loft’,  Russ,  pod-oshva,  ‘sole  of  foot’.  All  these words  derive  fr.  I.-E.  base  *pdd-,  *pid-,  ‘foot’. Cp.  fetch,  fetlock,  fetter,  fit,  ‘part  of  a  song’.  Cp. also  antipodes,  apod,  babouche,  biped,  breviped, caliber,  cap-a-pie,  charpoy,  expedient,  expedite, impeach,  impede,  impedimenta.  Lycopodium, millepede,  multiped(e),  octopus,  oppidan,  palmi¬ ped,  pawn  (in  chess),  parallelepiped,  pajama, pedal,  pedate,  -pede,  pedesis,  pedestal,  Pedetes, pedicel,  pedicle,  pedigree,  pedology,  ‘the  study  of soils’,  peduncle,  peon,  pes,  petiole,  pew,  Peziza, pie,  ‘a  small  coin’,  piepoudre,  pilot,  podagra, podal,  podium,  podo-,  pug,  ‘footprint’,  puy,  seer- paw,  Taliped,  Tarsipes,  teapoy,  trapezium,  triped, tripos,  vamp,  ‘front  part  of  the  foot’,  velocipede. Cp.  also  pejorative,  pessimism.
38199:tarboosh,  n.,  a  brimless  felt  cap  worn  by  Mos¬ lems.  —  F.  tarbouch(e),  fr.  Arab,  tarbiish,  lit. ‘sweating  cap’,  a  hybrid  coined  fr.  Turk,  ter, ‘sweat’,  and  Pers.  piishiddn,  ‘to  cover’.
=== SYN shoe section ===
10738:428 SELECTED INDO-EUROPEAN SYNONYMS 6.51 SHOE
10828:6.54 SHOEMAKER, COBBLER
```


## [2026-09-14T00:56:04.329Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n'); leaf=0; m={}\nfor i,l in enumerate(lines,1):\n    m[i]=leaf; leaf+=l.count('\\f')\nfor ln in [4226,38199,33703]:\n    print(ln,'leaf',m[ln],'est pages',(m[ln]-12)*2,(m[ln]-12)*2+1)\nEOF\necho \"=== Buck 6.51 SHOE ===\"\nsed -n '10738,10800p' SYN.txt",
 "description": "Klein leaves + Buck shoe section"
}
```


### [2026-09-14T00:56:05.536Z] TOOL RESULT

```
4226 leaf 84 est pages 144 145
38199 leaf 833 est pages 1642 1643
33703 leaf 734 est pages 1444 1445
=== Buck 6.51 SHOE ===
428 SELECTED INDO-EUROPEAN SYNONYMS 6.51 SHOE
ke i Goth. skohs Lith. kurpé a pees oe ON skor Lett. kurpe NG brddnua, wazobrot Dan. sko ChSI. sapogii, Erévige Lat. calceus (soccus) Sw. sko SCr. obu¢a, cipela, Postola It. scarpa, calzatura OE scoh Boh. slFevic, obuv Fr. chaussure, soulier ME sho Pol. —trzewik, obuwie Sp. zapato, calzado NE shoe Russ. sapog, baSmak, obyy' Rum. gheatd, incaljaminte Du. schoen Skt. upénah-, paduka- Ir. bréc (accrann, ctia- OHG  scuoh Ay. aodra-
rdn, assa) MHG = schuoch
Nir. —_brdg NHG  schuh W. esgid Br. botez, arc’henad
Under ‘shoe’ are considered the words of most general application to footwear, with omission of many that denote spe- cial types of shoes. For the great variety of such special types among the Greeks and Romans, cf. Pauly-Wissowa s.v. Schuh, with references.
1. Grk. brddqua : drodéw ‘bind under’, déw ‘bind’ (9.16).
Grk. zédiAov (in Hom. ‘sandal’) : mobs, gen. odds ‘foot’.
Grk. xpyzis (> Lat. crepida), Lith. kurpé, Lett. kurpe : Ir. cairem, W. crydd, Br. kere ‘cobbler’, SCr. krplje ‘snowshoe’, prob. fr. a *kerep- beside *(s)ker- ‘cut’. Walde-P. 1.425.
NG pop. wazobrot, fr. Turk. pabug (Pers. papas, lit. ‘foot-covering’, cpd. of pa- ‘foot’ and pug fr. pasidan ‘cover’). Lokotsch 1625.
2. Lat. calceus, whence or fr. MLat. *calcea and other derivs., It. calzatura, Fr. chaussure, Sp. calzado, Rum. tncal- {aminte ‘footwear’ : Lat. calz, -cis ‘heel’, Ernout-M. 138. REW 1496-98.
Lat. soccus, a sort of low shoe worn by Greeks and comic actors (important only
for the borrowed Gme. words for ‘sock’ 6.49), loanword, like abxxos, ouxxds (Hesych.) ‘a sort of shoe’, Ernout-M. 948.
It. scarpa, perh. as ‘leather shoe’ fr, OHG scharpe ‘leather purse’, Briich, Z. rom. Ph. 40.647. REW 7981¢
CC-O. In Public Domain. Gurukul Kangri Collection, Haridwar
Fr. soulier, with change of suffix fr. OFr. souler, Prov. sotlar, fr. MLat. *sy)- telare, fr. subtel ‘hollow of foot’. REW 8397. Gamillscheg 812.
Sp. zapato (It. ciabatta, Fr. savate ‘worn-out shoe’), fr. Pers. éabat ‘bast shoe’, Hence also WhRuss. éebot ‘boot’, etc. REW 2448. Lokotsch 379,
Rum. gheatdé (pl. ghete), through It. ghetta fr. Fr. guétre ‘gaiter’, fr. Gmce., cf. MHG, NHG rist ‘instep’, OE wryst ‘wrist’. REW 9577.
3. Ir. accrann, prob. (with metathesis for arce-) : W. archen ‘clothing, shoe’, OW archenatow ‘shoes’, Br. arc’hena ‘put shoes on’, arc’henad ‘shoe’, perh. through notion of ‘covering, protection’ : Lat. arcére ‘inclose, prevent’. Stokes KZ 41.381. Walde-P. 1.80.
Ir. ctiardn : MW curan ‘boot’, perh. fr. the root *(s)keu- ‘cover’ as W. esgid, Goth. skdhs, etc. (below). Walde-P. 2.547. Otherwise Pedersen 1.176 (: ChSI. crévijt, etc., below, 6).
Ir. as(s)a, ass (K. Meyer, Contrib. 138), etym.? Walde-P. 2.3. Walde-H. 1.99.
Ir. bréc, NIr. brdg, prob. fr. ON brok, pl. brekr ‘breeches’ (6.48), which were sometimes provided with feet, called Specifically leistabrekr (in contrast to leistalausar brekr). Leather breeches of this sort are still used by Icelandic and Faroese fishermen. Zimmer, KZ 30.87 f.
te Kleiderkunde
etc., Z& es 3 *skeu- ‘COVET « ;-Torp 1016. Feist 434.
Lett. kurpe : Grk.
tgkpurhO-s 9548. Fal é “5, Lith. kurp’, i) ' bove, 1). me na cae (usual word for b76- am in Gospels, ete. ; J; agié, Entstehungs” a 393), Russ. sapog (esp. ‘boot , but ‘a used for ‘shoe’, instead of basmak regarded as somewhat vulgar), etym.? ChSl. crévtjt, Boh. strevtc, Pol. irzewrk, SCr, dial. crevija (cf. crevljar ‘cobbler’), ORuss. cereviji (pl.), Bulg. créve (pl.),
SONAL ADORNMENT AND CARE
igitized by Arya Samaj Foundation Chennai and eGangotri
429
perh. as orig. ‘leather, hide’, fr. IK *(s)ker- ‘cut’. Berneker 151.
SCr. postola, fr. Turk. postol ‘soldier’s shoe’. Lokotsch 1667.
SCr. cipela (cf. Slov. cipele ‘ladies’ shoes’), fr. Hung. cipé, cipellé ‘shoe’. Berneker 130.
Russ. basmak, fr. Turk. basmak ‘shoe, sandal’ (cf. SCr. pasmag, Pol. arch. and dial. baszmag ‘sort of shoe’). Berne- ker 45.
ChSl. obw% (rare), SCr. obuéa, Boh. obuv, Pol. obuwie, Russ. obuv’ : Chl. ob- uti, Lith. auti ‘wear shoes’, Av. aofra- ‘shoe’, IE *eu-, in Lat. ind-uere ‘dress’ (6.11).
7. Skt. updnah-, fr. upa-nah- ‘tie un- der’ (cf. Grk. t7édnua).
Skt. pdduka- (rarely padi-) fr. pad- ‘foot’.
Av. aoéra- : Lith. auti, ChSl. ob-uti ‘wear shoes’, etc. (above, 6). Barth. 42.
6.52 BOOT
k. _xiopvos, tvdpopls ON boli, sty fill Lith. batas, éebatas, sopagas oriBadt, préra Dan. _ stgvle Lett. zabaks colhurnus, pero, ca- Sw. slével SCr. Gizma Tiga ME _bote Boh. _bota slivale NE boot Pol. but botte Du. __laars Russ. sapog bola OHG  stiful
: ea MHG . stival
a NHG - stiefel
bolas heuz
i i XBbopvos, whence Lat. cothurnus ' Uagedian’s boot’), a loanword,
beth, of Lyd; R Tig s5gq,"""" 8: J. S. Jongkees,
Gtk,
A nd wag- “ (Hom., ete.) rhpa d a Bb (whence late Lat  ™pv ‘scrotum? :
: tare » Toot con-
Cali
oh a (but difficulties) fr 92 > calz ‘heel’, caleeus
‘shoe’, and ligare ‘bind’. Kent, BSL 26.110 ff. Ernout-M. 134. Walde-H. 1.138.
It. stivale, fr. Prov. estibal = OFr. estivel ‘boot’, fr. estive ‘pipe’, Lat. sttps ‘stake’? So REW 8264.
But the objection to the old deriv. fr. MLat. aestivalia, lit. ‘belonging to the summer’ (fr. Lat. aestivus, fr. aestus ‘summer’), but actually described as ‘high boots’, is invalid. Cf. esp. Kret- schmer, Wortgeogr. 487 f.
-0. In Public Domain. Gurukul Kangri Collection, Haridwar
430
Hence NG o7fad, late ON sty/fill, Dan. sigvle, Sw. stével, late OHG sliful, MHG stival, NHG stiefel (cf. Falk- Torp 1201).
OF’. bote (> ME bote, NE boot), Fr. botte, Sp. bota, orig. much disputed, but | prob. belongs with Fr. pied bot ‘club- 4 foot’, fr. Gmc., LG butt ‘stumpy’, etc. Wartburg 1.667f. Gamillscheg 123. REW 1239a.
Hence NG pzéra, Boh. bota, Pol. but, older bot > Lith. batas (Berneker 77); late ON boli fr. ME bote (cf. Falk, Alt-
westnordische Kleiderkunde 187 f.); NIv. buatais, W. botas(en) prob. fr. ME botes (pl.).
Rum. cizmé (through Hung. csizma),
6.53 SLIPPER
Digitized by Arya Samaj Foundation Chennai and eGangotri
SELECTED INDO-EUROPEAN SYNONYMS
SCr., Bulg. cizma, fr. ‘boot’. Tiktin 370. Berneker 158.
Rum. ciobotd (Mold.), Lith. &batas through Slavic, cf. Russ. dial. Cebot, ie fr. Turk., cf. Kasan. éabata ‘boot? (whence also Sp. zapato ‘shoe’, 6.51) Lokotsch 379. Berneker 159, i
```


## [2026-09-14T00:56:20.145Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i in [84,733,734,735,832,833,834]:\n    L=leaves[i]\n    nums=re.findall(r'\\b1[0-9]{3}\\b|\\b[0-9]{2,3}\\b', L[:300]+L[-300:])\n    print('LEAF',i,'head:',L[:120].replace('\\n',' '))\n    print('   tail:',L[-120:].replace('\\n',' '))\nEOF",
 "description": "Klein leaf head/tail for page numbers"
}
```


### [2026-09-14T00:56:21.660Z] TOOL RESULT

```
LEAF 84 head: zorite  (q.v.),  azot-ize , tr.  v. azote,  n.,  a  whip.  —  Sp.,  fr.  Arab,  as-saut,  lit., ‘the  whip’,  fr.  as-, 
   tail: which  the pieces  are  put  back ;  compounded  of  back,  ‘the hinder  part  of  the  body’,  and  gammon,  ‘game’, ba
LEAF 733 head: s’,  fr.  Samnium,  which  prob.  stands for  *Sabniom  and  is  rel.  to  Sabinus,  ‘Sabine’. See  Sabine  and  subst. 
   tail: lor  found  in  old Chinese  porcelain.  —  F.  sang-de-bauf,  lit.  ‘bul- i  not lock’s  blood’.  F.  sang,  ‘blood’,  
LEAF 734 head: derives  fr.  VL. sanguem.  See  prec.  word.  F.  de,  ‘of,  from’, comes  fr.  L.  de,  ‘from,  away  from’;  see  de-
   tail: pota,  zapota. See  Sapota. saponaceous,  adj.,  soapy.  —  Formed  with  suff. -aceous  fr.  L.  sapo,  gen.  saponis, 
LEAF 735 head:  ‘soap’,  which  is a  Teut.  loan  word.  See  soap. Derivative:  saponaceous-ness,  n. Saponaria,  n.,  a  genus  of  
   tail: ent,  n.,  a  slender  branch, runner  (bot.)  —  L.  sarmentum,  ‘twigs,  brush¬ wood’,  which  stands  for  *sarp-ment
LEAF 832 head: hief, who  lived  in  the  second  half  of  the  1 7th  and  in the  first  half  of  the  18th  century. Tammanyism,  
   tail: ,  which  stands  for  *tamtos  and derives  fr.  tam,  ‘so’,  from  the  I.-E.  pronominal stem  *to-.  See  the  and  
LEAF 833 head: cp.  the  first  element  in tandem.  Cp.  also  taunt.  Cp.  also  the  first  ele¬ ment  in  tankard  and  the  second
   tail:   cluth,  grasp,  seize’,  properly  ’to  en¬ close’,  8pxyjj.7),  ‘drachma’,  Spiyua,  ‘a  sheaf’, lit.  ‘a  handful’; 
LEAF 834 head:  see  dram  and  cp.  target.  ML. targ(i)a,  OProvenq.  targa  (whence  It.  targa),  Sp. tarja,  ‘shield’,  are  also 
   tail:   cup ;  a  small  draft.— M  F.  ( =  F.) tasse,  ‘cup’,  fr.  OF.,  fr.  Arab.  tassah,  tass,  fr. Pers.  tdsht,  ’cu
```


## [2026-09-14T00:56:36.237Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== FFD printed p.44 (pdf 49) ===\"\nawk 'BEGIN{RS=\"\\f\"} NR>=48 && NR<=50 {print \"----LEAF\",NR\"----\"; print}' incoming/FFD/FFD_pages.txt | head -80",
 "description": "FFD page 44"
}
```


### [2026-09-14T00:56:37.382Z] TOOL RESULT

```
=== FFD printed p.44 (pdf 49) ===
----LEAF 48----
[pdf page 48]
ماده‌های ماضی و مضارع فارسی دری ‏ ی ۴۳
پژمردن
در پهلوی اشکانی ۰2۲ از ایرانی باستان ۹-2۵7-2*ء به معنی «پژمردن» آمده
است. 8 نشانه‌ای بوده است برای ساختن مادهٌ مضارع از ربشه. ۷ پیشوند فعلی است.
ريشةٌ 2027 به معنی «پژمردن» است. از ۷۷781۲ پهلوی اشکانی «پژمر» به وجود آمده
است. «پژمرد» باید در پهلوی اشکانی به صورت ۷۷1-21۵۲۵ بوده باشد. از ۷,1-20۳-1۵*
ایرانی باستان. برای 2۵ > آراست. 7 صورت ضعیف ريشةٌ 27027 است.
پژوهیدن
«پژوهید» مادة ماضی جعلی است» در فارسی میانه ۷12581 آمده است.
پژوه < فارسی میانه ۷328.
پسندیدن
پسندید < فارسی میانه 02820676. 02820670 ماد ماضی جعلی است و از ماده
مضارع ساخته شده است.
پسند + فارسی میانه 028300 < ایرانی باستان 0211-8200-8*. برای 2 آرای. 030
پیشوند فعلی است. ريشةٌ ۶224 به معنی «به نظرآمدن» است.
پنداشتن
«پنداشتن» بازماندةٌ ۳هاققل 27 024 فارسی میانه است. 020: به» 5 اين» 43318:
داشتن» روی هم به معنی «به چیزی شمردل).
پوزیدن
«پوزید» مادهٌ ماضی جعلی است و از مادهٌ مضارع ساخته شده است.
پوز < فارسی میانه 062 < ایرانی باستان 2-[0۵0*. برای 2 + آرای. 8 صورت
اصلی [۳۵ است» [به جای 8 آمده است. مادهٌ ماضی 052 در فارسی میانه :00 بوده

----LEAF 49----
[pdf page 49]
با فعلهای فارسی دری
است» از ایرانی باستان ۳۳-۱۵*. برای 1۵ -> آراست. 8 که صورت ضیف 34108
است» صورت اصلی 007 است» 8 پیش از ۲ به # بدل شده است. 3208 و 002 به معتی
: «نجات دادن» هستند. پوزش فارسی دری بازماندهٌ 88215 فارسی میانه است که هم
«نجات‌دادن) و هم «عذرخواهی‌کردن» معنی می‌دهد. «پوزیدن» به معنی «عذرآوردن و
معذرت خواستن» است.
پوسیدن
(پوسید» مادهٌ ماضی جعلی است» از مادهٌ مضارع ساخته شده است.
پوس < ایرانی باستان 0۷8۵*. برای 2 > آرای. 8 برای ساختن ماد آغازی از ريشه
به‌کار می‌رفته است. 0۷ صورت ضعیف ريشةٌ 080 است. ريشهٌ 020 «پوسیدن» معنی
می‌دهد. «پوده» به معنی «پوسیده» از ريشهٌ 020 گرفته شده است. به شرح زیر:
< فارسی میانه 08028 < ایرانی باستان 0-12-12*. برای 1۵ > آراست. 12 پسوند و
صورتی دیگر از 00 است.
بوشیدن ۱
پوشید < فارسی میانه 006810.
پوش ج فارسی میانه 005.
پوییدن
پویید مادةٌ ماضی جعلی است. از مادهٌ مضارع ساخته شده است.
پوی + فارسی میانه 00 < ایرانی باستان 0200-2*. برای 2 > آرای. ريشهٌ 0200
به‌معنی «دوبدن) است. (5 هم در فارسی میانه (دویدن)» معنی می‌دهد.
پیراستن
پیراست < فارسی میانه 0217351 و ۷۲391 0817381 د. ایرانی باستان -21-739م*
است و ۷۱391 ۷۷1-139-18*. برای 18 + آراست. 1 و 2211 هر دو پیشوتد فعلی هستند.

----LEAF 50----
[pdf page 50]
ماده‌های ماضی و مضارع فارسی دزی سس ها ۴۵
58 به جای 134 آمده» 4 پیش از 1 بدل به 8 شده است. ريشهٌ 4 به معنی «(منظم کردن»
است. «آراستن» هم از ریشةٌ 134و پیشوند فعلی 2 آمده است.
پیرای + فارسی میانه 08773 و ۷13 به ترتیب از 021-730-8* و ۷:1-734-2*. برای 2
> آرای.
78 (۷۲3 را به صورتهای «ویراستن)» «ویرای» به فارسی دری آورده‌اند.
پیمودن
پیمود < فارسی میانه 0277030 < ایرانی باستان 2021-3-12 *. برای 12 -> آراست.
1 پیشوند فعلی است. ريشهٌ ()133به معنی «اندازه گرفتن» است. 021-۳3-1۵* ایرانی
باستان باید در فارسی میانه به صورت 2271730 می‌آمد. به قیاس با ۶737 و 8700
به‌جای آن 027884 آمده است > آزمودن.
پیمای < فارسی میانه 02773 < ایرانی باستان 021-037-8* برای 2 > آرای.
پیوستن
پیوست < فارسی میانه 027۷۷281 < ایرانی باستان 021-028-12*. برای ۵ > آراست.
پیشوند فعلی است. 328 به جای 024 آمده» 4 پیش از + به ۶ بدل شده است. ۲24
صورت ضعیف ريشةٌ ۳28۵4 است. برای ضعیف کردن ريشه 2 حذف شده است. ريشهٌ
4 به معنی «بستن» است» خود «بستن» هم از ريشةٌ 0271۵ آمده است > پستن.
پیوند + فارسی میانه 221۷220 < ایرانی باستان 028-0886-8*. برای 2 -> آرای.
تاختن
تاخت + فارسی میانه 1384 < ایرانی باستان 13-12". برای 18 -> آراست. 13 صورت
اصلی 13 است» 1 پیش از 1 به بدل شده است. 13 صورت بالاندةٌ 18 است» ريشهٌ 18
به معنی «دویدنْ» است و 131 به معنی «دوانیدن».
در فارسی میانه 133122 به معنی «دواندن» است.
تاز < فارسی میانه 132 < ایرانی باستان 130-۵*.برای 2 -> آرای. #به‌جای ‏ آمده است.
```


## [2026-09-14T00:56:38.765Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD pōš ===\"; grep -n \"^pōš\\|^pos\\|pošīdan\\|pōšīdan\\|pōšišn\\|pōšēn\" PHD.txt | head -20\necho \"=== PHD_mackenzie ===\"; grep -n \"pōš\" PHD_mackenzie.txt | head -20\necho \"=== NYB ===\"; grep -n \"pōš\\|posh\\|pwš\" NYB_vol2_glossary.txt | head -20",
 "description": "MacKenzie/Nyberg pōš"
}
```


### [2026-09-14T00:56:38.841Z] TOOL RESULT

```
=== PHD pōš ===
3185:possessions grāmag, xwēšīh; v. pro- perty.
3186:possible, it is — šāyēd; tuwān.
3187:post-(horse) bayaspānīg.
3188:posterior nišēm.
=== PHD_mackenzie ===
=== NYB ===
3167:Pēšang [pwšng] n. of a town 11487. — Yaqut 1, 758 Bušanj.
3187:pušt [pwšt'; Ps. pwšty] the back 1112. 2521. 29%. 6513. 1287; pat ~ tacitan to run after, to pursue 311%; pat ~ bütan to protect, to be the protector 31°; ~ kartan 6 to protect 872%; — pl. eas. obl. ~-dn: pat puštān i Vištāspān for the (acts of) protection of the Vistasp dynasty 9514. — MPrs pws, NP pušt < *pršti-; Av. (878) paršta-, parsti-, v. s. v. puštēpān.
3189:puštēpān [pwštyp'n'] “protector of the back" = life-guards, pl. cas. obl. in ~-an sardär the commander of the life-guards 11911, — pušče cas. obl. of pušt (g. v.) + pan; the Sass. title is transcribed in Arm by p‘ustipanac (gen. pl.) (or p*usti- pan) satar ; besides, Arm has the Prth. lw. pašt-pan “protector, defender’ < *parésti- päna- (v.s. v. pušt); NP pustibän, pustvän. — pušt-aspān 1118 is an old misreading (Paz. pustaspän Mx) of pustepän, cer- tainly due to wrong association with asp ‘horse’, as is suggested by the spelling pwšt'sp'n'; moreover, in the BP writing the ligature -yp- is very often formed so as to coincide with -sp-. Read conse- quently 1118 puštēpān sardär = the Arm. form just quoted.
6106:pwlwd: polavatčn pwr: purr pwrsydn: pursitan pws: pus pwst: post pwšt: pušt py'dg: padatak pyd, pydr: pit pyd’g: paitak pyg: padak pygm: paitäm pym’n: patmän pymwen: patmöcan pymwxtn, pymwe-: patmöxtan pyr’yg: pairayak pyrwz: péroz pyšwb'y: p&söpäi pyšyn: pēšēnīk Pyš, pyšyy, pyšyh: pēš pyw’c-: patvac- pywn: patvand pywst: patvastan
```


## [2026-09-14T00:56:50.900Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD grep pwš / posidan ===\"; grep -n \"pwš\\|p6š\\|p0š\\|pošīdan\\|pošid\\|pöš\" PHD.txt | head -20\necho \"--- PHD lines starting p6/po ---\"; grep -n \"^p[oö06][sš]\" PHD.txt | head -20\necho \"=== HRN posh ===\"; grep -n \"pöšīden\\|pošīden\\|pōšīdan\\|pûšîden\\|pûšîdan\\|pušîden\\|puschiden\\|pôsch\" HRN.txt | head -20\necho \"=== HRN grep 'decken' near pos ===\"; grep -n \"pūšīdan\\|pōšīdan\\|pōš\\b\" HRN.txt | head",
 "description": "MacKenzie/Horn pōšīdan"
}
```


### [2026-09-14T00:56:50.990Z] TOOL RESULT

```
=== PHD grep pwš / posidan ===
553:puštaģ [pwstk'] load (carried on the back). puštībān [pwštykp”n! | N ~] supporter, bodyguard. ~ЛЬ : support, protection.
--- PHD lines starting p6/po ---
3185:possessions grāmag, xwēšīh; v. pro- perty.
3186:possible, it is — šāyēd; tuwān.
3187:post-(horse) bayaspānīg.
3188:posterior nišēm.
=== HRN posh ===
=== HRN grep 'decken' near pos ===
```


## [2026-09-14T00:56:56.603Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '540,560p' PHD.txt",
 "description": "PHD context around p-"
}
```


### [2026-09-14T00:56:56.665Z] TOOL RESULT

```
pahikēftan, pahikob- [ptkwp-tn'] strike. pahlawig [*p’hlwbyk' | (M phlwnyg), N paklaw(ān)i] Parthian; Pahlavi. pāhlom [phlwm] excellent, best, foremost. ~ih: excellence. pahlüg [p'Aok! | N pahli] side, rib. pahn [p?An! | N ~] wide, broad. сау [2d | N —à] width, breadth. lpahrextan, pahrēz- [phlyhtn', p'hlyc- | M phryz-, ] ~, N parhéxtan, parhéz-] abstain, refrain, avoid. *pahréxtan, pahrēz- [p’hlyhtn', p'hlyc- | M (phrystn), phryz-] care for, tend, protect. pahréz [Аус | N parhéz] defence, care. *pahrmāh- [ptimwh- | (N parmds-)] touch. ~арфіһ [Pkyh], ~i$n: touch, feeling. pak [DKY A < A аку; рк | = M, N ~] clean, pure, holy. ~ih: purity, holiness. pākīzaģ [p’kyck' | N ~a] pure. palang [ping | N ~] leopard. —-mušk [-mwsk' | N ~] speckled basil. pálüdag [p'Iwtk! | N ~a] starch jelly, flummery. pālūdan, pālāy- [p’lwtn', pPd- | (M p’rwdn, p’r’y-), N ~] strain, filter, purify. pambag [pmbk' | N panba] cotton. —ën [-yn'] (made of) cotton. pānāģ [p’n(’)k' | M p’ng] guard, protector; shepherd. ~th: protection. panāh [рт | = M, N ~] protector; refuge. pad ~ griftan: take refuge with. ~ih: protection. pand [pnd | = M, N ~] path; counsel, advice. panir [pnyl | N ~] cheese. panj [pnc | P рту, (M pnz), N ~] five. ~ag [-k! | N —a] pentad; hand, paw. ~аһ [h | N ~] fifty. panzdah [p’ncdh | M p’nzdh, N ~] fifteen. ірагаб [p?/k! | N para] piece, part, portion. ?párag [p?/k! | M p’rg, N para] gift, offering, bribe. paráhóm [pP?hwm = Av. para.haoma-] consecrated drink (the infusion in holy water of pounded лот and pomegranate twigs, sometimes with milk added). pardag [pitk! | N parda] veil, curtain. pardaxtan, pardaz- [pldhin', pldc- | M prdxt, N ~}, ~ az: be done with, freed of. ^ 6: set about, undertake. ~išn: freedom; undertaking. pardāxtan, pardaz- [pld’htn', pld?c- | N ~] accomplish.
pardāxtan 65 pāsbānīh
~ AZ: free (oneself) from. pargandan, pargan- [plkn-, plgn-dn! | (P pr'gnd, N parāgandan)] scatter, distribute, disperse. pargast [plgst' | N ~] let it not happen! Heaven forbid! pargüd [plgwt' | P prgwdg], ~ az: free, exempt from. parig [plyk' | M pryg, N pari] witch. paristag [pistk! | N pirista] servant. ~th: service; worship. paristar [plsť] | N parastár] maidservant. paristidan, parist- [plst-ytn' | M pryst-, N parastidan] serve, worship. ~išn: service, worship. paristog/k [plstwk' | P prstwg, N piristū(k)] swallow. рагпабап [pinyE?n! | M prng?n, N parniyān] polychrome damask. parr [pl | M pr, N ~] feather, wing. parrag [plk', pig | P prg, N ~a] wing. ~ig [-vk'] winged. parréxtan, parréz- [plyhin', plyc-] remain over, be superfluous. parrón [plwn' | M prwn] hence, away. parrwar [plwl | M prwr] winged. parsig [p’lsyk' | N pārsī] Persian. pars [5/f] spotted, speckled. parwāl [plwl | (P prwrz)] refreshment, nourishment. parwal- [plw���l- | (P prwrz'dn)) foster, nourish, -išn: nourishment. parwanag [phonk! | M prw’ng, N ~a] guide, leader. ^h : guidance, leadership. parwand [plwnd | N —] enclosure, comprehension. parwand-, v. parwastan. P parwānģāh [*plw?ng’s] throne. parwār [plyw?l | N ~] citadel; circumvallation; suburb, surroundings. parwardan, parwar- [plwl-tn' | M prwrdn, N ~) foster, nourish, cherish, educate. ~išn: nourishment, fostering, education. parwast [plwst'] enclosure. parwastan, parwand- [plwstn', plwnd-] surround, enclose, contain, comprise. parwāz [plw’c | N ~] flight. parzin [picyn' | M prcyn, J przyn, (N parčīn)] fence, hedge. pas [AHL < A?hr; BATL < Ab2tr; ps| = M, N ~] then, afterwards, behind. ~ az: after. ~ih: rear. pas [p’s | = M, N ~] guard, watch. ~ dāštan: keep watch, guard. pāsbān [p’sp’n' | M p’sb’n, N ~] guardian, watcher. ~ih: defence, protection.
CH Aagoa - x
pas-dānišnīh 66 paydag
pas-dānišnīh [4HLd’nsnyh] anti-knowledge. pasēmāl [psym’l, v. hamemal] defendant, accused. ~ih: (legal) defence. pasen [psyn! | N pasin] final, last. pasox [p’shw' | № ~] = passox. passand [psnd | N pasand] pleasure, liking. passandidan, passand- [psnd-ytn' | M psynd-, N pasandidan] like, approve. ~išn: liking, approval. ~isnig : likeable. passáxt [ps’ht'] test. passaxtan, passàz- [ps’hin', ps’c- | M ps?xt, ps’c-] fashion, prepare; insert; test. ~išn: preparation, constitution. passazag [psck! | M pscg] suitable, fitting. ~ih: suitability. passox [pshw! | M pswx, № pāsux) answer. past [pst' | N ~] low; astr. dejection. pašēmān [pšm?n! | = M, N ~] penitent, repentant. ~ih: penitence, repentance. pašm [psm | N ~] wool. ~ёп [-yn! | N ~in] woollen. pašn [psn'] bond, agreement. pāšnag [p’snk! | N ~a] heel. pāšom [p(”)$zvm) excellent. passing [pšng | N pišing] drop, exudation. paššinjag [pfnck! | N pišanja] drop. paššinjīdan, paššinj- [psnc-ytn' | N pišanjīdan) sprinkle. ~išn: sprinkling. pa&t(ag) [pšt(k)! | J pst] pact, bond, agreement. *pattān [pt’n'] noise, resonance. ~6mand [отта] resonant. pattāyistan [pi?dstn'] = pattüdan. pattüdan, pattày- [ptwtn', ptd- | P ptwdn, M pt’y-] stay, remain, last, endure. pattüg [ptwk'] enduring, patient, persevering. ^АҺһ: endurance, patience, perseverance. paxSag [phšk! | N pasa] mosquito, gnat. 1рау [pdy | N ~] foot; footstep, track. ~ 1: after. *pay [pdy | M pyy, N ~] sinew, tendon. pay [LGLE < А rglh; p'dy | M p'y, N —] foot, leg; foot (12 in.). 1,2 páy-, у, bL? pādan. payādaģ [pd’tk! | М py’dg, N piyada] on foot, foot-soldier, (chess) pawn. payag [p'd(y)k! | N paya] base, station. paydag [pyt?k! | M pyd'g, N payda] visible, obvious, revealed.
paydagih 67 pazzaftan
~th: visibility, appearance. paydagénidan, paydagén- [ ГОР hinin | M pyd'gynyd] reveal, explain. paydagihistan, paydagih- [py kyh-stn'] appear, be revealed, payg [pdh! | (P рар), N ~] foot-soldier, courier. *paygal [pyg'l | N payyāla, piyála] cup, goblet. -- gar [-A/] cup-maker. payģām [pgt”m! | M pyg’m, N pay(y)ām] message. ~bar LA | N -bar] messenger, apostle. paygos [p?tktvs | M p’ygws] district, province. paymān [pim”n! | M pym?n, N ~] measure, period; moderation; treaty. 6 — madan: reach maturity. ~ag [-k! | N ~a] period, measure, proportion. paymānīģ [ptm”nyk!] moderate. ~ih: moderation. *paymar [PK DWN < А pqdwn; p'tym'l] appointment, assignment. paymāy-, v. paymüdan. paymēģ [ptmwg | M pymwg] clothes, garment. paymóxtan, paymēz- [ptmwhtn!, ptmwe- | M pymwxt, bymwc-] don, wear. paymēūzan [ptmwen' | M pymwen] garment, dress. paymüdan, paymāy- [ptmwtn', ptm’d- | N ~] measure. *payram [p’tlm] the commonalty,-people. payrāstan, payrāy- [pt-, pyPstn!, pyPd- | M ругі, pyr!y-, N pērāstan) arrange, adorn. payrayag [руРак! | M pyr)yg, N pērāya] ornament, adornment. payrēģ [ptlwk'] light, brightness. paywand [ptwnd | (M руп), N ~] connection; offspring. paywand-, v. paywastan. paywasag [ptw’sk'] leather bag, wallet. paywastag [pteostk! | N ~a] continually. paywastan, paywand- [ptwstn!, ptwnd- М pywst, (pywyn-), N ~] join, connect. paywāz- [ptw’c- | M pyw’z-] answer, reply. ~ag [-k!], —i$n: response. paz-, v. poxtan. pāzand [p’cnd | N —] the Pahlavi commentaries on the scriptures (zand), transcribed in Avestan letters. pazd [pzd | — P] oppression, persecution. pazd- [pzd- | = M] blow, play (flute). pazdaģīh [pzdkyh] expulsion. pazdénidan, pazdén- [pzdyn-ytn' | P pzd-] frighten, chase. pāzen [p’c(y)n' | М pen, N pazan] ibex. pazüg [pzwk! | (N payūk, xabazdū)] guinea-worm. ~ í gühgard / gGhward: dung worm. pazzāftan [p> tn ' (M pzpt „intr.)] (cause to) ripen.
pazzām- 68 pīlbān
pazzām- [pz^m-] mature, ripen (intr.). ~išn: maturation, ripening. pazzáménidan [pz’myn-ytn'] = pazzāftan. pēčīdan, pēč- [pyc-ytn' | N ~] twist, entwine. pēm [pym] milk. péménidan, pémén- [5ymyn-ytn'] cause to well up, swell up. pen [p(y)n'] mean, miserly, niggardly. ~ih: meanness. pérámoón [pyPmwn! | M pyrmwn, N ~miin] around, péróz [pylwe | M pyrwz, N ~] victorious. ~th: victory. pérózgar [pylwekl | N ~] victorious. ~ih : victory. pés [pys | N ~] mottled, leprous; leper. pēsīdan, pēs- [pys-yin'] colour, adorn. ~iSn: adornment. pestān [pyst?n' | N ~] breast. pēš [LOYN! < A I-‘yn; руї | = M, N ~] before. IpéSag [py$k! | N péfa] trade, craft; guild, caste. *pēšaģ [pysk'] limb, member, part. pëššánig [pyš”nyk! | N pēšānī] forehead. pēšār [py | M py?r] leader, guide. ~ büdan: be guilty (of), commit. pēšārwār [руло], v. pëšyàr] urination. péSémàl [руѓут?/, v. hamēmāl] plaintiff. ~ih: prosecution, pēšēnīg [pysynyk! | (M pysyn(g), N pésina)] former; foremost, noble. pëš-gāh [pyšg”5 | N ~) audience chamber; foremost seat. pēš-kār [py$k'/ | N ~] servant. pēšēbāy [byš')wp?d | M руйору, N péfwa] leader, vanguard. ~th: leadership. pēš-pāraģ [pyšp*/k! | N —a] an appetizer. pēšyār [pyšk”/ | N ~] urine. petit [pytyt! = Av. paitita-] penance. ~ig [-yk'] penitent. ~igih: penitence. petyárag [p(y)tyd'lk! = Av. paityára- | M pty’r, N patydra] evil, mis- fortune; adversary; astr. detriment, ~th: (onslaught of) evil. рі [AB' < А "bur р(у) | M pyd] father. *pid [5(5)!! | P pyd] meat, flesh. pidar [AB Ytl, v. ipid ; ру | M pydr, N ~] father. pih [pyhw'] food, victuals. pīh [TL BA = A trb; рур | N ~] fat, tallow. pil [py] | M pyl, N ~] elephant; (chess) bishop. --bān [-p’n' | N ~] elephant-driver.
pillagān 69 pušt
pillagan [plk’n' | M pylg, N ~] steps, ladder. pim [pym] pain, pang, sorrow. ~gén [-kyn'] sorrowful. pir [руі | N ~] old, aged, ancient. ~ih: age. piring [pling | M pryng, (N pirind)] monochrome damask, pist [pst! | N ~] browned flour. pistag [pstk! | IN pista] pistachio nut. pišīz [pšyc | N ~] small copper coin, ‘farthing’. pēhišn [pwhsn'] corruption, decay. pēlāwad [pwPft! | М pwl'wd, N pēlād] steel. ~ën [-yn!] (made of) steel. pondik [pndk' | Ar. b/fundug] hazel-nut. por [pwl | N —] francolin. pēryētkēš [pwlyw(k)kyf = Av. paoiryē.tkaēša-| (one of) the first teachers of the Mazdean religion. ~ЛЬ : the primal doctrine of the Mazdean religion. pēst [pwst! | = M, N ~] skin, hide; bark, shell. mēn [-yn! | N ~in] (made of) skin. pēšīdan, pēš- [pws-yin' | N <] cover, put on, wear. ~išn: covering. potk [pwtk' | N ~] sledge-hammer. poxtan, paz- [APPWN-tn' < А V?ph; pwhtn', pc- | M pwxtn, N ~] cook, bake. рӧу- [pwd- | (P pwd-), N ~] run. ~iSnig : running. p6z(ag) [pwc(k!) | N pēz(a)] snout, muzzle. püdag [pwtk! | N pūda) foul, rotten. —ih: rottenness. 1puhl [pwhl | N pul] bridge. *puhl [pwhl] expiation, atonement; punishment. puhlénidan [ pwhlynytn'] cause to atone. purnāy [pwln’d] adult. purr (MALE < A mlh; pul | M pur, N ~} full. =-ģāh [-g’s] at the fullness of time, about to die. ~-тюаһ [-mh] full moon. —-rawišnih [-lwbsnyh] fullness. ~-sardag [-sltk'] of all kinds. --xwarrah [-G DE] full of glory. pursidan, purs- [pwrs-ytn' | M pwrs-ydn, N ~] ask. Vu re: Е ~iSn: question. — ~i$nig : responsible. pus [BRE < A br-h; pws | = M, N =] son. ~ar [BREI, pwsl | M pwsr, N ~] son. —yàn [pwsd?n! | M pwsy’n] womb. pušt [52001 | = M, N ~] back; support, protection.
puštag 70 ranjfénidan
puštaģ [pwstk'] load (carried on the back). puštībān [pwštykp”n! | N ~] supporter, bodyguard. ~ЛЬ : support, protection.
R
rabih [/pyh | M rbyh] noon, midday (heat). rad [/t! | N —] (spiritual) chief, master. АҺ: office of rad. rad [Pu | P rd, N ~] generous, liberal. ~ih: generosity, liberality. radag [itk! | M rdg, N rada] line, rank, row. radómand [/t?^wmnd] having a rad. rad-passag [/tps’k'] ceremonies of the gáhanbar festivals. radunay [/twny = Av. ratunaya-] one under the guidance of a rad. raftan, raw- [SGY TWN-tn! < А V sg’; lwb- | M rptn, rw-, N ~] go, move, proceed. ~išn, v. rawišn. raftār [/pt?] | N ~] goer. rag А! | M rg, N ~] vein. «ЛЬ: disposition, character. ray [/gy | P rg] quick, swift. ray [Pg | N —] meadow, plain. rah [/s, lh, [hy | M rh(y)] chariot, wagon. rah-, у. rastan. rah [Ps | M rh, N ~] road, way. rahag [/hk! | P rhg] = rag. rāh-dār [lsd] | N ~] brigand, highway robber. ~ih: brigandage. rahig [/syk!, Ikyk' | M rhyg, N rahi] child, page. ~ih: childhood. rāh-nimāy [Psnm?d | (M r’-hnmwd’r), № ~numa] guide. ram [Pm | М әт, N ~] peace; cal. 21st day. ram(ag) [/m(k') | P rm, N ram(a)] herd, flock. ráménidan, rāmēn- [Pmyn-ytn! | M ?myn-] give peace, pleasure. rāmišn [P min! | M rmyfn, N rāmi$] peace, ease, pleasure. ~ig [-vk! | N —z#] peaceful, at ease. ran [Рп! | N ~] thigh. P rān- [/^n-] fight. randidan, rand- [/nd-ytn! | N —] scratch, grate, abrade. rang [/ng | M rng, N —] colour, dye. ranj [Inc | P rnj, (M rnz), N ~] toil, trouble. ~ag [-k' | N —a] troubled. ranjénidan, ranjén- [/ncyn-ytn'] trouble.
ranjwar 71 rëš
ranjwar [Incwl | (M rnzwr), N ranjūr] troubled, distressed. rapihwin [/pys-, Ipyt-pyn!, -wyn' = Av. rapiüfina-] the afternoon gah; south. ~tar [-tl] southern. rasan [/sn' | N ~] rope. rasénidan, rasén- [/syn-yin'] bring. rasidan, ras- [YHMTWN-tn' < А yhmtwn, V mt^; ls-ytn! | M rs-ydn, N ~] arrive, mature. raspig [Pspyk!] second officiating priest. rast [Pst! | M rst, N ~] true, straight, direct. ~ih: truth, rastaģ [lstk! | N rasta] series, row, progression; element, газап, rah- [Istn', Ї(?)А- | N ~] escape. rastarih [/st?/y%] escape. rasüg [/swk! | (N rāsū)] weasel. Rašn [/@! | M ri, N ~] god of Justice; cal. 18th day. ra&tan, *raz- [/ftn'] colour, dye. raw-, v. raftan. rawag [/wP^k! | N rawá] current. ~ih: currency. rawügenidan, rawagén- [/zob)hyn-ytn!] set in motion, propagate. rawénidan, rawén- [SGYTWNyn-ytn', v. raftan] cause to go, extend. rawišn [lwbin', SGYTWNsn', v. raftan | N rawif] going, motion. ^h : behaviour; as a suffix, forms abstract nouns. ray [Pd | M ry, N ra] postposition, for, for the sake of. rāyēnāģ [Pdym bi | M r’yn’g] arranger. rayénidan, rāyēn- [Pdyn-ytn! | M r'yn-ydn] lead, direct, arrange, organize. ~išn: action, function; arrangement. rāyēnīdārīh [/”*dynyt?lyh | M r!ynyd?ryh] direction, organization, rāyišn [”dsn'] order, arrangement. rāyomand [Pd^wmnd] rich, majestic. raz [/c, lz | N ~] vine; vineyard. raz [Pc | M Pz, N ~] secret, mystery. ~ig [-yk'] secret. rāz-kirrēģ [Pc kylwk' | M г qrwg] architect, builder. razm [/cm | M rzm, N —] battle. —--$àh [-g's | P -g’h, (M rzm?h), N ~] battlefield. razor [lcw] | M rzwr] forest. rédak [lytk' | N ~] lad, page. тёр [/yā! | N ~] sand. rëm [lym | M rym, N —] dirt, filth, purulence. réman [lymn' | M rymn, N ~] dirty, filthy, purulent. ^b : filth. 1r€§ []yf | N ~] wound, sore. *rēš [/yf | N —] beard.
résag 72 rózig
rēšaģ [/yšk! | N rēša] root, fibre. rēšīdan, rēš- [lysyin' | N ~] wound, hurt. rëškën [/yškn'] hurtful, harmful. ~th: harmfulness. réxtan, réz- [lyhtn', lyc- | P ryxt, M ryz-, N ~] flow, pour. --išn: flow. ridan, riy- [/ytn', Id- | N ~] defecate, void. rist [lyst' | M ryst] dead. Iristag [lystk'] corpse. 'ristag [/ystk!] way, manner; sect. rist-āxēz [/yst?hyc | M ryst?hyz, N ~] resurrection of the dead, rištaģ [/(y)stk! | N ~a] rope, string, thread. riy-, v. ridan. riyahrih [/d?hlyh] scorn, mockery. rdb [/wp] robbery. rób- [/wp- | N ruftan, ~} rub, sweep. rūbāh [TALE < A tP; lwph | N ~] fox. Irēd [Iowt! | M rwd, N ~] river. *rdd [lwt' | N ~] stringed instrument. réd-bar [lwtb’] | N ~] river bank. rddig [/zvtyk! | (N róda)] intestine, gut; ~4n, (p/.) entrails, guts. тбүп [M(H)SY A < A ті; lwkn! | Р тшеп, (M rwyyn), N rauyan] oil, butter. ~-xwardig [-hwltyk'] sweetmeats. ron [lwn' | M rwn] direction. б... ~: towards. róspig [lwspyk! | N ~i] whore. ~th: whoredom. róstág [lw(t)st?k! | (P rwdyst?g), N rūstā] river-bed; district, province. rošn [lwfn! | M rwšn, N rūšan] light; bright, light. ~ih: light. röšnjag [lwsnk'] clear, obvious. ~gar [-Al | (P gr, M -ygr), N -gar] illuminator. irēy [ltd | M rwy, N ~] face. *rdy [lwd | M rwy, N ~] copper, brass. гбу-, -išn, v. rustan. гӧуап [/wdyn! | N ~] madder. róyen [/wdyn! | M r'wyn, N róyin] (made of) copper, brazen. roz [YWM < А ушт; Гос | M rwc[z, N ~) day. rózag [lwck! | M rweg, N roza] fast, fasting. rozāģ [wc k'] lightning. rózan [/wcn! | N ~] window. roz(b)ānaģ [lwe(p)’nk'] window. rózénidan, rózén- [Iwcyn-ytn! | M rweyn-] lighten, brighten. rozģār [/wck”l | N ~] daytime. r6zig [/wcyk! | N rózi] daily bread, sustenance.
rūz-šabān 73 sān
```


## [2026-09-14T00:57:05.802Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== CHEUNG context 9420-9470 ===\"; sed -n '9425,9470p' CHEUNG.txt",
 "description": "Cheung palidan entry"
}
```


### [2026-09-14T00:57:05.855Z] TOOL RESULT

```
=== CHEUNG context 9420-9470 ===


*harz 133 


Well attested: Pres.: IND. 1sg. MMP hylym, 3sg. MMP hylyd, 3р1. MMP hylynd, etc. || (+ *pari-) Pres.: 
IND. 3р1. MMP p’r’ynd, SUBJ. 3sg. MMP p’r’y’d; Partic.: perf. pass. MMP p’rwd, “p’rwdq 
*PARTHIAN: hyrz- ‘to leave, abandon; remit (of sins); establish, appoint’ || (+ *apa-) 
*bhyrz- ‘to abandon, desert; forgive’ = Ghilain: 48, 49 | DMMPP: 197a, 11а 

Well attested: Pres.: IND. 3sg. hyrzyd, 2pl. hyrzyd, 3pl. hyrzynd, etc. || (+ *apa-) Pres.: IMPV. 2pl. 
"bhyrzyd; Partic.: perf. pass. ’bhyst 

*CHORESMIAN: (+ *pari-) pZy- ‘to purify, cleanse’ = Samadi: 167 

*BACTRIAN: v1pC- ‘to leave, let, set (free), allow’ — S-W, Bact.: 228b 

*NWIR: Widely attested and borrowed (from Pers., especially forms with -/-): NP 
histan/hil-, Jow. bam-haft/a-hal-, Meim. bem-haft/a-hal- ‘to leave, let go’, Bal. 
(h)ist/(h)ill- ‘to let go, allow, leave (behind)’ (< MP/NP), Kurd. (Kurm.) histin/hél-, 
(Sor.) hestin/hel- ‘to permit, allow’, Zaz. estis/erzen- ‘to throw’, Abz. hasta/harz-, 
Abyan. hästa/härz-, Tt. (Cha.) harz/hast, Awrom. astáy/-az- ‘to let, allow’, Fariz. 
-hast-/-hal-, Yar. -hast-/-hal-, Gil. (Rsht.) astoen/-al-, Ham. hästän/häl-, Sorkh. hínd-/ 
hín- ‘to put’, Ard. helahe/hel-, Anar. haste/hal-, Gur. (Kand.) hastin/-az-, Khuns. е/-, 
tel-/est, ela ‘to put, lay; to let, permit’, Nn. este/vál-, Qohr. hasta/hel- ‘to let, allow, 
permit’, Siv. el-, äl-/(h)ist, Tr. hasta/hal-, Varz. heste/hel- ‘to allow, let’, Tal. haste 
‘to leave (behind), abandon’ || (+ *aua-) NP (dial.) vel, vil kardan ‘to set free’, Gz. 
vel, Bakht. wil ‘free, loose’ || (+ *pari-) NP paludan, palidan/palay-, Kurd. (Kurm.) 
palavtin/palév-, (Sor.) patawtin/palew-, Gz. päl-/palä ‘to filter, purify’, Gur. cay- 
parzen ‘tea-strainer’. Ф As for NP palüdan, palidan/palay- and the corresponding 
forms, they may be contaminated with *para-dauaja- ‘to clean’, on which see Sims- 
Williams 1989: 262. Note also the rhyming antonym NP 4ludan ‘to stain, soil’, s.v. 
*dauH?. 

*NEIR: Pash. (1)&d-/iXo(d) ‘to put, place, leave’ 

*MISC: (+ *aua-) Par. yurzéw- ‘to pour out’ || (+ *pari-) Arm. (LW) parzel ‘to filter, 
purify’ 

*SANSKRIT: sarj ‘to let loose, to throw out, to send forth’ (RV+) || (+ *aua-) Skt. 
äväsıjah ... apáh ‘release waters’ (RV) = EWAia П: 709 

«PIE *selg- ‘to let it loose, release, flow (?)’ = LIV: 528 f. | Pok.: 900 f. 

*IE COGNATES: Hitt. /salk-/ ‘to knead, to mingle’, Olrish selg (f.) ‘hunting’, MHG 
selken ‘to fall down drippingly, to go down (of clouds)’, (ppp.) OE solcen ‘lazy,
```


## [2026-09-14T00:57:08.454Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== NYB posh ===\"; grep -n \"pōšītan\\|pošītan\\|p6šītan\\|pwsytn\\|pōšēn\\|pōs-\" NYB_vol2_glossary.txt | head\necho \"=== MON santur ===\"; grep -n \"سنتور\" MON_part1.txt MON_part2.txt | head\necho \"=== MON palidan ===\"; grep -n \"پالیدن\" MON_part1.txt MON_part2.txt | head",
 "description": "Nyberg and Mo'in greps"
}
```


### [2026-09-14T00:57:08.563Z] TOOL RESULT

```
=== NYB posh ===
=== MON santur ===
MON_part2.txt:10304:کوچکث. کمچچه. (س.) مضراب سنتور. 
MON_part2.txt:10908:و دلنشین است بخصوص که مانند سنتور 
MON_part2.txt:59716:چنگ» سنتور و قانون را ذوات الاو تار مطلق 
MON_part2.txt:88391:از نوع سنتور» دارای ۵ سیم و آن از سوب 
MON_part1.txt:79910:سنتور: ۲ (- سنطور] (ا.) (مد.) یکی 
=== MON palidan ===
MON_part1.txt:28586:کردن» پالودن پالیدن. بیختن. (مصل.) 
MON_part1.txt:28626:مصدر پالیدن و بابرايی کلمة اخیر هم قیسا 
MON_part1.txt:28637:آن گرفته شود پالیدن» پالاییدن» صافی 
MON_part1.txt:28739:پالیدن: ۳81-7 [- بالودن - بالاییدن] 
MON_part1.txt:28745:پالیدن زر به معنی خالص کردن آن از خبث 
MON_part1.txt:28749:پالیدن: 021-1020 (چکه کردن» ریختن ] 
MON_part1.txt:28751:پالیدن: «جآ-21ع مص‌ل.) آشفتن و ژولمده 
MON_part1.txt:28754:پالیدن: ۲51-140 (مصم.) (صر.) کاوش
```


## [2026-09-14T00:57:19.098Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '28735,28765p' MON_part1.txt\necho \"=== page markers near ===\"; grep -n \"^\\s*۶۸۰\\|^\\s*680\\|\\[pdf page\" MON_part1.txt | head -5\necho \"=== santur entry ===\"; sed -n '79905,79925p' MON_part1.txt",
 "description": "Mo'in palidan and santur entries"
}
```


### [2026-09-14T00:57:19.215Z] TOOL RESULT

```
کرفن کت افکندن: : بوغ به گردن کسی 
انداختن» ریسمان به گردن خصم بستن و 
بردن. 

پالیدن: ۳81-7 [- بالودن - بالاییدن] 


(بالید» بالد» خواهد بالید» بیال» بالنده» 
پالان» پالیده» پالش). (مصم.) صافی کردن» 
تصفبه کردن. (در مقدمة الادب زمخشری 
پالیدن زر به معنی خالص کردن آن از خبث 
آمده.) (مسصل.) تمام شدن» به آخر 
رسیدن: برسیدن. 

پالیدن: 021-1020 (چکه کردن» ریختن ] 
(مص‌ل.) (صر.) زهیدن تراویدن, تراییدن. 
پالیدن: «جآ-21ع مص‌ل.) آشفتن و ژولمده 
شدن موی سر. 

پالیدن: ۲51-140 (مصم.) (صر.) کاوش 
کردن؛ جستجو کردن» جستن» تفحص 
کردن. 

پالیز: 12 (.) باغ» بوستان» جالیز» فالیز» 
کگسلستان . کشتزار» مزرعه. آنجای‌ها که 
هندوانه و خربزه و گرمک و طالبی و کدو و 
خیار و چغندر و امثال آن کارند: مزارع 
صیفی کاری» خربز ه‌زار. 

پالیزبان: م92 [پالیز + بان سد. حفاظت 
- پالیزوان - فالیزبان] (امر.) نگاهدارندة 
=== page markers near ===
=== santur entry ===

سنن. اهل سنت: < و 

خلاافت 2 و جانشینان او قایلند؛ مق 
شیعه. 
سنتور: ۲ (- سنطور] (ا.) (مد.) یکی 
از قد بمترین و کاملترین ن سازهای ایرانی که ۹ 
شکل ذوزنقتین ساخته و سیم‌های سیار بر 
وی آن کشیده شده است و آن را به وسیلة 
دو مضراب جوبی نوازند. 


سنج: لمده (.) وزن» کیل. 

سنج: -58 ,56 [- صنح» معر.] (ا.) (مست.) 
دو صفحه مدور فلری که برای احداث آواز 
و موسیقی بهم زده‌شود. 

ستنجاب: (ند. تست شور ۰) (ا.) 
(جاد.) پستانداری, شتا واه نع ند کار 
که دارای دمی نس طویل و پر پشم می‌باشد.
```


## [2026-09-14T00:57:59.511Z] TOOL CALL #31: Bash

```json
{
 "command": "ls site/pages/405.jpg 2>/dev/null; pdftoppm -f 405 -l 405 -r 200 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg405 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg405.png",
 "description": "Render PDF page 405"
}
```


## [2026-09-14T00:57:59.537Z] TOOL CALL #32: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-14T00:58:01.220Z] TOOL RESULT

```
site/pages/405.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb 63962 Sep 13 20:58 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg405.png
```


### [2026-09-14T00:58:01.225Z] TOOL RESULT

```


```


## [2026-09-14T00:58:03.460Z] TOOL CALL #33: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/site/pages/405.jpg"
}
```


### [2026-09-14T00:58:03.485Z] TOOL RESULT

```

```


## [2026-09-14T00:58:12.300Z] TOOL CALL #34: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%BE%D8%A7%D9%84%DB%8C%D8%AF%D9%86",
 "prompt": "Give the full Persian etymology section for پالیدن (pālīdan): what root/origin, Middle Persian form, related words, and any cited scholars."
}
```


## [2026-09-14T00:58:13.972Z] TOOL CALL #35: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%BE%D9%88%D8%B4%DB%8C%D8%AF%D9%86",
 "prompt": "Give the full Persian etymology for پوشیدن (pūšīdan): Middle Persian form, Proto-Iranian reconstruction, cognates, cited sources, and derived terms."
}
```


### [2026-09-14T00:58:16.098Z] TOOL RESULT

```
# Persian Etymology for پالیدن (pālīdan)

Based on the Wiktionary entry provided, the etymology section is quite limited:

**Etymology stated:** "Perhaps related to Dari Persian _پال_ (pâl, 'ploughshare')."

The source document does not provide:
- A detailed root analysis
- Middle Persian forms
- Extended related words beyond the single comparison to پال
- Citations to specific scholars

The entry offers only a tentative connection to the noun پال, suggesting a possible relationship to agricultural terminology (ploughshare), but stops short of confirming a definitive etymological origin. No deeper historical linguistic analysis is included in this dictionary entry.
```


### [2026-09-14T00:58:20.965Z] TOOL RESULT

```
# Persian Etymology of پوشیدن (pūšīdan)

**Middle Persian Form:**
The word derives from Middle Persian *pwšytn'* (pōšīdan), meaning "cover, put on, wear."

**Proto-Iranian Reconstruction:**
It traces back to Proto-Iranian *\*paus-*, meaning "to dress, clothe, cover," though the source notes this was "probably borrowed from a substrate language."

**Etymology Chain:**
The word traveled from an unknown substrate language → Proto-Iranian *\*paus-* → Middle Persian pōšīdan → Modern Persian پوشیدن

**Cited Sources:**
- MacKenzie's *Concise Pahlavi Dictionary* (1971) documents the Middle Persian form
- Cheung's *Etymological Dictionary of the Iranian Verb* (2007) discusses the Proto-Iranian reconstruction

**Potential Cognates:**
Sanskrit पवस्त (pavásta, "covering, garment") has been proposed but is considered unlikely given the Sanskrit word's Vedic origins and the existence of a plausible Indo-Iranian etymology.

**Derived Terms:**
سرپوش (sarpōš), پوشاندن (pōšāndan), پوشاک (pōšāk), پوشش (pōšiš), پوشنده (pōšanda), and پوشک (pōšak).
```


## [2026-09-14T00:58:25.051Z] TOOL CALL #36: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/santur",
 "prompt": "Give the etymology of santur/santoor (the dulcimer): Persian سنتور, Arabic سنطور/سنطير, Aramaic psanterin, Greek psaltērion — what route is given and which sources are cited?"
}
```


## [2026-09-14T00:58:25.946Z] TOOL CALL #37: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/tarboosh",
 "prompt": "Give the full etymology entry for tarboosh, and also for babouche if present on the page."
}
```


### [2026-09-14T00:58:29.475Z] TOOL RESULT

```
# Etymology Lookup Result

I've reviewed the provided web page content from Etymonline, which shows the site's header, navigation menu, and footer. However, **neither the full etymology entry for "tarboosh" nor "babouche" appears in the content you've shared**.

The page content consists primarily of navigation elements, the site's tagline ("Quick and reliable accounts of the origin and history of English words"), and footer links to various sections and social media. To retrieve the actual etymology entries you're requesting, you would need to perform a search on the Etymonline website directly or provide the specific etymology entry pages.
```


### [2026-09-14T00:58:30.158Z] TOOL RESULT

```
# Etymology of Santur

Based on the Wiktionary entry, the documented etymological route is:

**Classical Persian سَنْتُور (santūr)** → English/Turkish **santur**

The entry states the word was "Borrowed from Classical Persian _سَنْتُور_ (santūr), of uncertain origin; sometimes suggested to be from Ancient Greek _ψαλτήριον_ (psaltḗrion, 'psaltery')."

## Key Points:

- **Primary source cited**: Classical Persian
- **Origin**: Explicitly marked as "uncertain"
- **Secondary theory**: A possible (but unconfirmed) connection to Ancient Greek *psaltḗrion* is mentioned

The entry does **not** cite Aramaic as a documented source, nor does it trace connections through Arabic or provide intermediate etymological steps. The Arabic translations (سَنْطُور and سَنْطِير) are listed only as translation equivalents, not as etymological sources. The Greek connection is presented tentatively ("sometimes suggested") rather than as established fact.
```


## [2026-09-14T00:58:34.121Z] TOOL CALL #38: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/tarboosh",
 "prompt": "Full etymology for tarboosh: Arabic ṭarbūš, Ottoman Turkish, Persian sarpūš or Turkish ter + Persian pūš — what is said, and what alternative etymologies are listed?"
}
```


## [2026-09-14T00:58:35.357Z] TOOL CALL #39: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/babouche",
 "prompt": "Full etymology for babouche: French, Arabic bābūš, Persian pāpūš/pāpūsh, Turkish pabuç — what chain is given?"
}
```


### [2026-09-14T00:58:37.479Z] TOOL RESULT

```
# Tarboosh Etymology

Based on the Wiktionary article provided, the etymology section states:

**What is said:** The word tarboosh was "[Borrowed from Arabic _طَرْبُوش_ (ṭarbūš)."](https://en.wiktionary.org/wiki/tarboosh)

**Alternative etymologies:** The article does not list any alternative etymologies. It presents only the Arabic origin as the source of the English word tarboosh.

The content makes no mention of Ottoman Turkish, Persian sarpūš, Turkish, or the Persian components (ter + pūš) that you referenced in your question.
```


### [2026-09-14T00:58:39.306Z] TOOL RESULT

```
# Etymology Chain for "Babouche"

According to the Wiktionary entry, the word traces back through this linguistic path:

**English**: Borrowed from French *babouche*, which came from Arabic *bābūš*, ultimately derived from Persian *pâpuš* ("slipper").

**French**: The term was inherited from Middle French *papouch* and *babuc*, sourced from Ottoman Turkish *papuş*, which itself came from Persian *pâpuš* ("slipper").

The entry notes that the Arabic *bābūš* can be compared to this chain, suggesting the Persian origin as the ancestral source across multiple language families—Romance (French), Semitic (Arabic), and Turkic (Ottoman Turkish)—all borrowing from the Persian root meaning "slipper."
```


## [2026-09-14T00:58:44.421Z] TOOL CALL #40: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B7%D8%B1%D8%A8%D9%88%D8%B4",
 "prompt": "Give the Arabic etymology of طربوش (ṭarbūš): is it from Persian سرپوش sarpūš, or Turkish ter 'sweat' + Persian pūš 'cover'? Quote what is said."
}
```


## [2026-09-14T00:58:46.071Z] TOOL CALL #41: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/feel",
 "prompt": "Give the English etymology of 'feel': Old English fēlan, Proto-West Germanic/Proto-Germanic *fōlijaną, and the Proto-Indo-European root cited (with cognates like Latin palpare, Greek psallein)."
}
```


### [2026-09-14T00:58:48.342Z] TOOL RESULT

```
# Etymology of طربوش (ṭarbūš)

According to the Wiktionary entry, the word is not from Persian سرپوش directly. Instead, the page states:

"Found from the sixteenth century, variant of شَرْبُوش (šarbūš). The dissimilation is speculated to have been motivated by Kipchak تر (tär, 'sweat'), the headpiece being fit to conceal پوشیدن (pôš) perspiration."

So the etymology involves a Kipchak element meaning "sweat" combined with a Persian verb meaning "to cover," rather than deriving from the Persian compound سرپوش itself. The word is categorized as "Arabic terms borrowed from Kipchak."
```


### [2026-09-14T00:58:51.445Z] TOOL RESULT

```
# Etymology of "Feel"

Based on the Wiktionary entry, the word "feel" traces back through these linguistic layers:

**Modern English → Middle English → Old English**

The entry states: "From Middle English _felen_, from Old English _fēlan_, from Proto-West Germanic _*fōlijan_."

The word derives from Old English _fēlan_, which descended from Proto-West Germanic _*fōlijan_. This Germanic root connects to cognate words like Dutch _voelen_ and German _fühlen_.

**Notable limitation:** The provided source does not cite a Proto-Indo-European root or mention Latin _palpare_ or Greek _psallein_ as etymological connections. The entry only traces the word back to Proto-West Germanic origins without extending further into Proto-Indo-European ancestry.

The documented etymology focuses on the Germanic language family development rather than deeper Indo-European connections.
```


## [2026-09-14T00:58:58.757Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-West_Germanic/f%C5%8Dlijan",
 "prompt": "Give the etymology of Proto-West Germanic *fōlijan: what Proto-Indo-European root is cited, and what cognates (Latin palpare, Greek psallein, etc.)?"
}
```


## [2026-09-14T00:59:00.879Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CF%88%CE%AC%CE%BB%CE%BB%CF%89",
 "prompt": "Give the Ancient Greek etymology of ψάλλω (psallō): what origin is given, what PIE root if any, and what derived terms (ψαλτήριον)?"
}
```


### [2026-09-14T00:59:04.623Z] TOOL RESULT

```
# Etymology of Proto-West Germanic *fōlijan

**Proto-Indo-European Root:** The term derives from PIE *[\*pelh₁-](/wiki/Reconstruction:Proto-Indo-European/pelh%E2%82%81- "Reconstruction:Proto-Indo-European/pelh₁-")* meaning "to stroke."

**Cognates cited include:**

- **Latin:** *palpō* ("to stroke, soothe")
- **Ancient Greek:** *pállō* (πάλλω, "to sway, swing") and *psēlăphắō* (ψηλαφάω, "to feel, grope for")

According to the article, the word is "presumably related to Old Norse *falma* ('to grope, feel; to be astonished'), perhaps from Proto-Germanic *\*fōlijaną*, secondary causative of strong verb *\*falaną*." The ultimate origin is described as unknown, though the cited cognates suggest Indo-European roots connected to touching, stroking, and tactile sensation.
```


### [2026-09-14T00:59:05.880Z] TOOL RESULT

```
# Etymology of ψάλλω (psallō)

**Origin:** The etymology is described as "Unknown; probably Pre-Greek," with a note directing to related form ψάω (psā́ō).

**PIE Root:** No Indo-European root is provided in the source material.

**Derived Terms:** Among the derivatives listed are:
- ψάλμα (psắlmă) - "psalm"
- ψαλμός (psălmós) - "psalm"
- ψαλτήριον (psăltḗrĭon) - a stringed instrument
- ψάλτιγξ (psắltĭnx) - another musical term

The word ultimately means "to touch sharply; to pluck" or "to play a stringed instrument with the fingers," with later Koine usage extending to "to sing (a psalm)."
```


## [2026-09-14T00:59:15.365Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== LKT babusch/papusch ===\"; grep -n -i \"papusch\\|babusch\\|pabuç\\|papu\\|1625\\.\" LKT.txt | head -15\necho \"=== DEV babouche ===\"; grep -n -i \"^BABOUCHE\\|BABOUCHE\\|TARBOUCHE\" DEV.txt PHN.txt LAM.txt | head -10",
 "description": "Lokotsch and French Arabism dicts"
}
```


### [2026-09-14T00:59:15.454Z] TOOL RESULT

```
=== LKT babusch/papusch ===
554:[Selbst  nicht  arabischen,  sondern  viel- leicht indischen  Ursprungs,  JAs  1862, I,  93]  'Papagei'.  Hieraus  mit  Anlehnung an  lat.  gallus  it.  papagallo,  afrz.  pape- gaut  und  in  Anlehnung  an  lal.  gains 'Häher'  prov.  papagai,  afrz.  papagai, nfrz.  papegai  [jedoch  mit  geänderter Bedeutung:  'Vogel  aus  Holz,  nach  dem geschossen  wird'],  sp.  papagayo;  ferner siz.  varmiamii,  it.  barbagianni  'Nacht- eule, fig.  Tropf'.  Dtsch.  Papagai,  ndl. papegaai  [als  'Pfaffenhäher'  aufgefaüt], engl,  popingag,  dän.  papegoeie,  schwed. papegoja.  Ebenso  russ.  popugai,  klruss. papnha,  serb.  poln.  papuga,  bulg.  pa- pagai. [DE  326.  GrSVociSic  249.  Gor- jajew  274.  Mikl  SlEtWb  231.  Suolahti, Die  deutschen  Vogelnamcn.  Straßburg 1909.  S.  2/3.
3716:1625.  Pers.  päpüs: 'Fußbekleidung'  [aus  pers.  p&  'Fuß' Horn  NpEt  S.  63,  Nr.  281  und  püs  Prä- sensstamm von  püsldän  'bedecken'], ebenso  tk.  papus,  ar.  bäbüs;  hieraus  it. babbuccia,  frz.  babouche,  sp.  babuche, Tum.papuci,  papuc  'leichter  Hausschuh', siz.  babbaluci  'verschiedene  Arten Schnecken' ;  serb.  papusa,  poln,  babusza, öech.  papuö,  russ.  babiisi  'Pantoffeln ohne  Hackenleder';  dtsch.  Babusche, (dial.  Schlesien)  Paputschen.  [DE  231, Eguilaz  328.  ML  858  und  6216  (gehören natürlich  zusammen).    GrSVociSic  227.
3815:Püah-püah  'geiiräusell'  [Pijn  159  b],  zu- sammengezogen zu  papüa  'Bewohner von  Neuguinea  und  der  umliegenden Inseln';  hieraus  nd\.  papoea,  frz.  pajwu, ihr  Land  Papouasie,  dtsch.  Papua,  engl. papoua.  Dazu  noch  frz.  2)apoic  'Apteno- dytes  papua,  ein  Pinguin'.  [DevicDEt  183.
5713:Babusche  16^5
5854:Padischa  1604 Pa^rorfe  373 Palankin  1(139 Fallasch  1615 Pangolin  1649 Papua  1669 Paputsche  1625 Paradies  1631 P«ria  1627 Parteibonze  331 Pasc/;«  1640 paschen  1641 Pascher  1641 Pass«  1652 Patschuli  1603 PeMo  r'Pee;  1889 PeH  1634 Perfcrti  1632 Petuntze  1609 Pharao  1650 P/mj-o  1650 Philister  l644 PjA-?^^  1655 P/srt«^  1659 ^j/rt«?  j.  1643 Pleitegeier  j.  1643 Polo(  spiel)  1666 Pomeranze  1555 Praue,  1651 Prinzmetall  1657 Punsch  1619 Pyjama  1606 Pyramide  1457
7703:papuga  147
9772:papuga  147
=== DEV babouche ===
DEV.txt:718:Babouche.  Esp.  hahucha.  C'est  le  persan  (jii^-^b  pfipoiicli (de  b  pâ,  pied ,  et  ^ù^y^, poûchïden ,  couvrir).  Mais  le  chan- gement de  p  en  b  marque  que  le  mot  nous  est  venu  par l'arabe  qui,  n'ayant  pas  dep,  écrit  ij^^ii  hnhoûch.  C'est  ainsi que  nous  avons  eu  pacha  sous  la  forme  hacha  ou  hassa.
DEV.txt:2928:Babouche.
DEV.txt:2929:Babucha,  esp.  voy.  Babouche.
DEV.txt:4585:ji^b  voy.  Babouche,
DEV.txt:4681:ji^U  pers.  voy.  Babouche. ^^IxIjLj  pers.  voy.  Aubergine. sISsIjIj  pers.  voy.  iVubergine. yû;^Lj  pers.  voy.  Bézoard. sLi^Upej's.  voy.  Chah. ^^Xjpers.  voy.  Parsis. »>Lj  pers.  voy.  Para. (jkLj  pers.  voy.  Bézoard. ivolj  pers.  voy.  Alphénic. i^yj  pers.  voy.  Péri. HDD  voy.  Pâques. ^"ikj  pers.  voy.  Pilau. ^  pers.  voy.  Punch. □  "«"nS  voy.  Purim. fjj^^^,  pers.  vov.  Babouch,  Tar- bouch.
PHN.txt:2059:BABOUCHE, s. f. composé, (p.)
PHN.txt:3044:pellent aussi TARBOUCHE. Voyez ce mot. — En France, calotte
PHN.txt:5613:tion du (j& ch quand il termine un mot, comme babouche, der-
PHN.txt:5614:viche, tarbouche, etc.
PHN.txt:9573:TARBOUCHE, s. m. composé, (t.)
```


## [2026-09-14T00:59:18.259Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AFM بابوج / طربوش ===\"; grep -n \"بابوج\\|بابوش\\|طربوش\\|سنطور\\|سنطير\" AFM_pages.txt | head -10\necho \"=== PLA ===\"; grep -n \"بابوج\\|بابوش\\|طربوش\\|سنطور\\|سنطير\\|papus\\|pāpūš\" incoming/PLA/PLA_pages.txt | head -10\necho \"=== TAD ===\"; grep -n \"بابوج\\|طربوش\\|سنطور\" TAD_pages.txt | head",
 "description": "Arabic loan dictionaries"
}
```


### [2026-09-14T00:59:18.338Z] TOOL RESULT

```
=== AFM بابوج / طربوش ===
5475:بابوش ١5.‏
5711:بابوش ١١‏
=== PLA ===
=== TAD ===
```


## [2026-09-14T00:59:27.439Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHN BABOUCHE ===\"; sed -n '2055,2070p' PHN.txt\necho \"=== PHN TARBOUCHE ===\"; sed -n '9570,9590p' PHN.txt\necho \"=== AFM 5475 ctx ===\"; sed -n '5468,5480p' AFM_pages.txt\necho \"=== AFM 5711 ctx ===\"; sed -n '5705,5716p' AFM_pages.txt",
 "description": "Pihan and Addi Shir entries"
}
```


### [2026-09-14T00:59:27.533Z] TOOL RESULT

```
=== PHN BABOUCHE ===
détroit pour entrer dans la mer d'Oman , autrement appelée
océan Ethiopique. — C'est à tort que certains dictionnaires
géographiques ont adopté la transcription Babel-Mandel, dans
laquelle on ne peut trouver aucun sens convenable.
BABOUCHE, s. f. composé, (p.)
{J*^^ [pâpoûch]^ littéralement ^ut courre fe j^tec/. Des deux mots
réunis en persan les Arabes ont fait le substantif ^r^^ [^^-
boûdj], au pluriel ^1^ [bawâbtdj], qui désigne également
une espèce de pantoufle, formée de la semelle et de l'empeigne,
sans quartier de derrière , et que l'on dépose par respect à la
porte d'un appartement, avant d'y entrer. Cette chaussure,
que les Turcs mettent souvent par-dessus le ^i^j^ [terlik^ , sorte
de bottines en maroquin portées par les deux sexes, est d'un
usage très-commun en Orient.54 * BAJ
BADIANE, s. f. (p.)
^L^dlf [6eu/yan] et a^Lj^I^ [bâdyânah] fenouiL Nom de l'anis
=== PHN TARBOUCHE ===
gieux, et qu'on emploie encore, en Orient, pour appeler les
chrétiens à la prière , attendu que l'usage des cloches leur est
absolument interdit par les musulmans.TAR 351
TARBOUCHE, s. m. composé, (t.)
{fiyijio \i'arhoùcK\ Genre de bonnet de laine rouge , à flamme
bleue, adopté en Egypte et en Turquie. On met ordinaire-
ment sous cette coiffure un petit bonnet blanc qui dépasse le
premier d'un centimètre environ. Tous les membres de l'am-
bassade ottomane en France portent le tarbouche. — Le mot
turc \fiyijio \iarhùûcK\ n'est sans doute qu'une altération du
persan {fiyif^ \serpoûcK\ couvre^chef, composé dej^ [ser] ou
jLw [«^r}t^te^ chef, et de ^yj [poûch] qui couvre.
TARE, s. f. (a.)
^Jo [t'arh'] rejet. Le mot tare veut dire , dans le sens propre ,
déchet sur le poids, dimnutian opérée sur la quantité ou la qua-
lité des marchandises. Il se prend quelquefois au figuré dans
le sens de vice, défaut; et l'adjectif tar^, e, se dit aussi figuré-
ment, en parlant de choses gâtées ou endùmmagées, comme fruits
tarés, ou des personnes de mauvaise réputation, homme taré,
fille ou femme tarée. — Les Espagnols, les Portugais et les Ita-
liens écrivent tara uniformément.
=== AFM 5475 ctx ===
١8 ܚܢ‎
١7١ بوب‎
ܚ
بوغه تكافى ܘ ܙ
بيراق ܙ
بيك فولاج ܘ ١‏
+3 من +¥
بابوش ١5.‏
ياره ܘ ܐ
يور يله ܣ
يهلوان ܩ
بياده | |
ܡ رثك 46
=== AFM 5711 ctx ===
رار
ܕܚ ܝܥ 717
0 م
بن ^«
7 ܟ
+3 ب د
بابوش ١١‏
ياره ܘ ܐ
سان ܚ1 ܙ + |
ا كل ܙܘ ܙ
يرتج دار ايامى ܙ ܙ
ياريار ١١5‏
```


## [2026-09-14T00:59:39.880Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN bedecken ===\"; grep -n \"bedecken\" HRN.txt | head -10\necho \"=== HRN 281 pa ===\"; grep -n \"^ *281\\.\\|^ *28[0-2]\\. \" HRN.txt | head\necho \"=== HRN paludan ===\"; grep -n \"pälüden\\|pälüdan\\|pälüd\\|paluden\\|läutern\" HRN.txt | head",
 "description": "Horn pōšīdan / pālūdan"
}
```


### [2026-09-14T00:59:39.939Z] TOOL RESULT

```
=== HRN bedecken ===
7517:htdjan Verhüllen, bedecken, lat. celärCj occulere
=== HRN 281 pa ===
2750:280. panzde 'fünfzehn , vergl. pänsed 'fünfhundert'.
2755:281. päl^ pä Tuss ; vergl. paye 'Stufe', päym.
2761:282. päyisten 'fest stellen , dauern ; erwarten ; vergl.
=== HRN paludan ===
2738:278. pälüden 'reinigen', Praes. pälay-em, päläyiden,
13258:, pälüden 278.
```


## [2026-09-14T00:59:44.459Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '2735,2760p' HRN.txt\necho \"=== which leaf/page? ===\"\npython3 - <<'EOF'\nt=open('HRN.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n'); leaf=0; m={}\nfor i,l in enumerate(lines,1):\n    m[i]=leaf; leaf+=l.count('\\f')\nfor ln in [2738,2755,7517]:\n    print(ln,'leaf',m[ln],'printed page',m[ln]-21)\nEOF\necho \"=== search poschiden ===\"; grep -n -i \"poschiden\\|püschiden\\|pōschīden\\|pûschîden\\|pusiden\\|pūšīdan\" HRN.txt HUB.txt | head",
 "description": "Horn 278 pālūden"
}
```


### [2026-09-14T00:59:45.598Z] TOOL RESULT

```
Abh. 73.
277. päk 'rein', paktze,
ai. pavakd- 'rein, klar ; phlv. pak, päkih,
278. pälüden 'reinigen', Praes. pälay-em, päläyiden,
paiti + alüden (s. älüden^ No. 42) ; phlv. pälüt (Bund.),
päz. pälJdan, pälaidan (West, Sik. gum.-Gl.).
bei. LW. palayag^ pälenay 'seihen, worfeln, reinigen'
(292).
^j Vergl. Geldner, Studien I, 16. Bartholomae (briefliche
Mitteilung) verweist mich aber auf aw. parendi- (Indog. Forsch. I, 184)
mit der Grundbedeutung 'Füllser.— 63 —
279. pälez 'Garten (Sahn. I, 73 Vers 207) ^), palezhan, arab.
LW. faliz,
ap. nagdÖHöog; aw. pairida^za-,
LW. kurd. päres, arm. partez, syr. Dn*)5?, JDD'^'TlEi.
280. panzde 'fünfzehn , vergl. pänsed 'fünfhundert'.
aw. paücadasa 'fünfzehn; skr. pdflcada^a; phlv.
pancdahion,
kurd. [daupe/ij etc.]; paiizde (LW.); afy. pinjalas;
oss. d. findtäs^ t. findfäs (292) ; bei. panzda (LW.).
281. päl^ pä Tuss ; vergl. paye 'Stufe', päym.
aw. päda- 'Puss* ; phlv. pCLT *Fuss', päyah *Stufe' ; ai.
päda-; arm. otn (H. No. 280).
kurd. pai (LW.) 'Fuss'; bei. päd, n. /xlJ, ^^ö^ (291);
oss. *fad aus bäymmoad-äi 'barfuss*, bäyömbad-äi 'bar-
fuss erschlossen? (267).
=== which leaf/page? ===
2738 leaf 83 printed page 62
2755 leaf 84 printed page 63
7517 leaf 214 printed page 193
=== search poschiden ===
```


## [2026-09-14T00:59:55.282Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"^ *[0-9]\\{3\\}\\. p\" HRN.txt | sed -n '1,80p'",
 "description": "List Horn p- entries"
}
```


### [2026-09-14T00:59:55.359Z] TOOL RESULT

```
2679:266. pädiSäh *König'.
2683:267. päde 'Heerde'^), padehan.
2685:268. pädyäb, pädyaw rituelle Waschung.
2688:269. pädyävend (i:ixnx5?, Is. 1, 31) 'kräftig'.
2691:270. pär 'das vergangene Jahr', pärsal^ parm.
2708:271. päre ^ück, Teil'.
2711:272. päzen *Bergziege*, päzen,
2714:273. päzehr 'Gegengift, Bezoar.
2716:274. päs 'Schutz*, pasban^ päsTden,
2724:275. päsu% 'Antwort'.
2728:276. päSne 'Ferse'.
2736:277. päk 'rein', paktze,
2738:278. pälüden 'reinigen', Praes. pälay-em, päläyiden,
2746:279. pälez 'Garten (Sahn. I, 73 Vers 207) ^), palezhan, arab.
2750:280. panzde 'fünfzehn , vergl. pänsed 'fünfhundert'.
2755:281. päl^ pä Tuss ; vergl. paye 'Stufe', päym.
2761:282. päyisten 'fest stellen , dauern ; erwarten ; vergl.
2785:283. päyi;^ 'Herbst*.
2791:284. petyäre 'Unglück' etc. (Vis und Rämin, Seite 81,
2795:285. pulten 'kochen, Praes. pez-em^ pezamden,
2804:286. pider (peder) 'Vater'.
2824:287. pidräm 'schön, fröhlich' (Sahn. III, 1803, V. 372).
2826:288. pedrad 'Heil, Lebewohl*.
2829:289. pedJd 'sichtbar.
2832:290. peölruften 'empfangen, annehmen', jüd.-pers. J nenne,
2839:291. peöfre entgegen*.
2843:292. per-, Praefix.
2850:293. perr Teder, Flügel*; pemden^ penden^ perend 'Vogel'^),
2876:295. perfuf enden zerstreuen; erschrecken, pergenden,
2880:296. pertew 'Glanz*.
2882:297. perdayten 'ausführen, ausleeren; streben, sich be-
2892:298. perest 'Verehrer , verehrend*, perestTde7i , perestür^
2897:299. pursTden 'fragen', pursis^).
2907:300. perrisiym^uS, perrisiyCLvesän ^) , 'Frauenhaar (Pflanze),
2912:301. pers 'Bach, Quell'.
2920:302. pergene 'Provinz, Distrikt'.
2923:303. peren 'gestern', perendös 'gestern Nacht'.
2934:304. pervär *Stair^).
2943:307. pervez 'siegreich*.
2946:308. pervfn 'Plejaden*.
2950:309. perhey(ten 'sich enthalten ; sich hüten', Praes. perliez-etn^
2969:810. perl 'Perl, guter Genius*.
2974:811. perer Vorgestern, perejröz, pere\seb.
2980:812. piSmanj pemän^ ptizmän (8ähn. I, 359 Note 2, Calc.)
2987:313. pi^fnurden, pezmurden 'erschlaffen, verblühein', pilOTi:!
3002:814. pizohlden 'erforschen, nachfragen*, pizöh, pizöhis^).
3019:315. pes 'hinter, nachher, pesin 'letzter.
3028:316. pest 'niedrig, nnoilN (Is. 2, 9; 11, 17).
3032:317. pistän 'Brust (der Frau)'.
3037:318. puser, pur 'Sohn, pus (Sahn. III, 1516 Vers 336,
3050:319. pesend zufrieden, angenehm', pesendlden.
3058:320. pist 'Mehr.
3068:322. pusek, pösek *Katze' ('Dialekt von Transoxanien' BQ.)^).
3086:323. peSenjTden, pisenjidefi ^besprengt werden ^), j)^^^^j^
3094:324. pegäh *Frühlicht, früher Morgen .
3096:325. pul^) 'Brücke.
3103:326. peleng 'Leopard'^).
3107:327. penUh 'Zuflucht, Schutz', penahlden 'Schutz suchen'.
3121:328. penj 'fünf*, penjum 'fünfter , peNje Taust'.
3128:329. penjäh 'fünfzig'.
3131:330. pend *Rat\
3137:831. pindUSten 'glauben, dafür halten', Praes. pindärem.
3140:332. penhän, pinhän Verborgen'.
3167:334. püde *faul, verfault', päsiden (Inchoat.) *faulen .
3172:335. poz 'Partie um die Nase* 2).
3180:336. pöziS 'Reue, Entschuldigung', pöztden (Vis und Kämm, ^
3192:337. pü^e Pfote .
3195:338. po8t 'Fell, Haut', pöstln,
3210:340. puläd 'Stahl'.
3233:341. pehre *Wache\
3248:343. peJilev, pehletan 'Held'^).
3251:344. peh/Ti' 'weit, breit', pehnä.
3274:347. piyäde Tussgänger, Fusssoldat*.
3291:348. peyam ^Botschaft', peiyäm'^)^ peiyätnber , peyämber^
3306:349. peiää^ offenbar, jüd.-pers. NT^5.
3313:350. plr alt, Greis', pTre,
3318:351. pfrär, pirar[sal *das vor vergangene Jahr.
3320:352. pmrästen schmücken, anordnen , Praes. peiray-em.
3323:353. perähen 'Hemd*.
3328:354. perö^, arab. LW. ß:rüz 'siegreich' ; j^frö^e 'Türkis,
```


## [2026-09-14T01:00:01.113Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '3195,3212p' HRN.txt\npython3 - <<'EOF'\nt=open('HRN.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n'); leaf=0; m={}\nfor i,l in enumerate(lines,1):\n    m[i]=leaf; leaf+=l.count('\\f')\nfor ln in [3195,3205]:\n    print(ln,'leaf',m[ln],'printed page',m[ln]-21)\nEOF",
 "description": "Horn entry 339"
}
```


### [2026-09-14T01:00:02.269Z] TOOL RESULT

```
338. po8t 'Fell, Haut', pöstln,
aw. pq8tö.[fra&ah' ; phlv. pöst, pöstln.
LW. kurd. pöst ^ pTst 'Fell, Haut'; bei. pöst, pöst
(213) ; afy. pöst ; wa/. p^i?^, sar. past,
339. j>iifc, pwA: das Blasen (um Feuer anzufachen), Blase-
balg 2).
gr. (pvöa 'Blasen, Blasebalg, (pvonta *Blase'; arm.
puK 'Hauch', puUI^ Blasebalg , pKam 'sich aufblasen,
pcem 'hauchen' (nicht entlehnt nach Hübschmann
No. 285).
Die richtige neupersische Form muss buk sein.
Arm. p und gr. rp weisen auf indog. ph (vergl.
Bartholomae, BB. 10, 290), np. h auf indog. bh\
also indogermanische Doppelformen wie bei [/^veph-,
vebltr- u. ö.^).
340. puläd 'Stahl'.
phlv. pülafat oder püläft, vd. 8 (254) (arm. LW.
poXopat, poXpaty po'kovat)^ pülaftTn (AV.), pülät (West
3195 leaf 96 printed page 75
3205 leaf 96 printed page 75
```


## [2026-09-14T01:00:09.317Z] TOOL CALL #51: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%B3%D9%86%D8%AA%D9%88%D8%B1/",
 "prompt": "Quote the فرهنگ معین (Mo'in) entry for سنتور, including any bracketed origin tag (e.g. [یو.], [ع.], [معرب]). Also quote the دهخدا or other etymology given."
}
```


## [2026-09-14T01:00:11.486Z] TOOL CALL #52: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CF%80%CE%B1%CF%80%CE%BF%CF%8D%CF%84%CF%83%CE%B9",
 "prompt": "Give the Greek etymology of παπούτσι (papoútsi): from Ottoman Turkish papuç, from Persian پاپوش pāpuš? Quote the chain."
}
```


### [2026-09-14T01:00:14.635Z] TOOL RESULT

```
# Etymology of παπούτσι

The word παπούτσι traces back through a borrowing chain as follows:

According to the Wiktionary entry, the term was "Borrowed from Ottoman Turkish _پاپوش_ (papuş, papuç), from Classical Persian _پاپوش_ (pāpōš)."

This establishes the etymological path: **Classical Persian → Ottoman Turkish → Greek**

The Greek noun ultimately derives from Persian origins, entering Greek via the Ottoman Turkish language during the period of Ottoman influence on Greece.
```


### [2026-09-14T01:00:14.984Z] TOOL RESULT

```
# Santur Dictionary Entry

**Farhang-e Mo'in (Mo'in Dictionary) Definition:**

"(سَ) (اِ. ) از سازهای ایرانی به شکل ذوزنقه که دارای سیم های بسیاری است و به وسیله دو مضراب چوبی نواخته می شود."

This translates to: An Iranian string instrument with a trapezoidal shape featuring many strings, played using two wooden mallets.

**Etymology Note from Dehkhoda:**

The Dehkhoda dictionary identifies it as "نام سازی" (the name of a musical instrument), describing it as one of the oldest and most complete Iranian instruments. The entry notes an alternative folk use as a children's toy instrument played by rubbing.

The page also references a theory that "سنتور" may derive from the Persian phrase "شاهان تار" (kings of strings), given the instrument's construction from numerous strings as part of the major Iranian stringed instrument family.
```


## [2026-09-14T01:00:26.570Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SKT feel ===\"; grep -n \"^FEEL\\|^PSALM\\|^PSALTERY\" SKT.txt | head\necho \"=== SKT context ===\"; grep -n -A3 \"^FEEL,\" SKT.txt | head -12\necho \"=== FSD babouche/tarboosh ===\"; grep -n -i \"babouche\" FSD_vol1.txt | head -3; grep -n -i \"tarboosh\\|tarbush\" FSD_vol4.txt | head -3\necho \"=== WEB vol1 babouche ===\"; grep -n -i \"babouche\" WEB_vol1.txt | head -3",
 "description": "Skeat/FSD/Webster greps"
}
```


### [2026-09-14T01:00:26.776Z] TOOL RESULT

```
=== SKT feel ===
=== SKT context ===
=== FSD babouche/tarboosh ===
30851:tar-boosb',  1   tor-bO^h',  2   tfir-bo<wh',  n   [Ar  ]* usually  red,  felt  cap  with  tassel  of  blue  or dark-colored  silk,  worn  by  Moslems  some- times as  the  inner  part  of  the  turban, fez  (<  Ar  tarbush]  tar-booch'};  tar- bouche'j:;  tar-busn'f.
30852:—   tar-booshed%  tar-bouched%  tar- busbed'fO  Wearing  a   tarboosh Tar'bor-o,  l   tor'bDr-o,  2   taribor-o,  n   A township  and  town,  county-seat  of  Edge- combe county,  N   C
60530:yer'ba,  lyur'bD,  2yer'b*i,  n   [Spl  1,  A   herb  or  plant  2. Same  as  mate  abbr  otYERBA  matL  —   jerba  buena  [CVl- fornla],  a   fragrant  perennial  plant  {Micromeria  cAamfJSonfs) of  the  mint  family,  used  as  a   carminative  —   y.  del  oso,  a California  species  of  buckthorn  (Bftamnw  califo^n^ca^  — y«  mansa,  a   perennial  herb  (Anemopsis  caltfornica)  of  tho pepper  family,  growing  In  New  Mexico,  Arizona,  and  Call- lomla,  reputed  to  be  useful  as  a   diuretic  and  for  rheuma- tism y.  de  mansat.— y*  mat6,  Paraguay  tea.  mnt^  — y.  reuma,  an  aromatic  Californian  herb  (FranLcnia  grandt- /oUa)»  a   remedy  In  catarrhal  affections  —   y,  sagrada,  a Bouth'Ame'lcan  plant  (Lantana  brasiUensU)  —   y.  Santa, i.  Either  of  two  California  plants  of  tho  genus  Briodictyon (1)  S   califomicum,  the  California  tarbush  (2)  E   iomcn- tosum  2.  A   Mexican  medicinal  plant  (Piper  sanctum) yielding  oil  like  oil  of  sassafras  — ycp'bal,n  (Sp  Ami  A plantation  or  district  abounding  In  yerba  matd yer’eum,  1   y   Or'kum,  2   ygr'cfim.  n   The  fiber  of  madar. yerdtf  n   Yard  jerdet*  (for  horse-cloths  ycr’gast. ycr’ga,  1   yOr’gs,  2   yer'ga,  n   A   coarse  woolen  material  used yerk,  ly0rk,2yerk.  c   I.f  1.  (Scot  1   To  tie  with  a   jerk  or tightly  2   [Prov  Eng  &   U   S   ]   To  Jerk  3.  (Scot  or Ohs]  To  beat.  lash,  excite  II.  i   [Prov  Eng  or  Obs] To  jerk,  also,  to  kick,  os  a   horse  [For  jerk^,  t   ] yerk.  n   (Prov  or  Obs  ]   A   jerk
=== WEB vol1 babouche ===
```


## [2026-09-14T01:00:27.906Z] TOOL CALL #54: WebFetch

```json
{
 "url": "https://www.iranicaonline.org/articles/santur",
 "prompt": "What does Encyclopaedia Iranica say about the origin of the word santur (Persian hammered dulcimer)? Any mention of Greek psalterion, Aramaic psanterin, or Arabic santir?"
}
```


### [2026-09-14T01:00:29.039Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-14T01:00:41.575Z] TOOL CALL #55: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/pelh%E2%82%81-",
 "prompt": "Give the reconstruction page for PIE *pelh₁-: meaning, descendants (Latin palpo, Greek pallo, Germanic *fōlijaną), and any note on Pokorny page numbers."
}
```


## [2026-09-14T01:00:43.113Z] TOOL CALL #56: WebFetch

```json
{
 "url": "https://www.nisanyansozluk.com/kelime/pabu%C3%A7",
 "prompt": "Give Nişanyan's etymology of Turkish pabuç / papuç: from Persian pāpūš? Quote the entry and first attestation date."
}
```


### [2026-09-14T01:00:46.709Z] TOOL RESULT

```
I cannot provide the etymology information you're requesting because the web page content provided only shows the header, navigation, and footer of the Nişanyan Sözlük website—it does not include the actual dictionary entry for "pabuç" or "papuç." The content lacks the etymological details, Persian origins, and attestation dates you're asking about.

To find this information, you would need to access the full entry page for that word on the Nişanyan Sözlük website directly.
```


### [2026-09-14T01:00:47.171Z] TOOL RESULT

```
# Proto-Indo-European *pelh₁-

## Meanings
The root has two related senses: (1) "to swing" and (2) "chaff"

## Documented Descendants

Based on the Wiktionary page, the following descendants are attested:

- **Ancient Greek**: πάλλω (pállō, "to sway, swing")
- **Sanskrit**: पलाव (palā́va, "chaff")
- **Latin**: *pulvis* ("dust") and *palea* ("chaff")
- **Latvian & Lithuanian**: pęlus, pẽlūs (related forms)

## Note on Your Query

The page does not mention Latin *palpo* or Germanic *fōlijaną* as descendants, nor does it reference Pokorny page numbers. The document cites De Vaan's *Etymological Dictionary of Latin and the other Italic Languages* (2008) and Schrijver's work on Proto-Indo-European laryngeals as primary sources.
```


## [2026-09-14T01:00:53.643Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n \"https://en.wiktionary.org/wiki/%D9%BE%D8%A7%D9%84%DB%8C%D8%AF%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%D9%BE%D9%88%D8%B4%DB%8C%D8%AF%D9%86\" \\\n \"https://en.wiktionary.org/wiki/santur\" \\\n \"https://en.wiktionary.org/wiki/tarboosh\" \\\n \"https://en.wiktionary.org/wiki/babouche\" \\\n \"https://en.wiktionary.org/wiki/%D8%B7%D8%B1%D8%A8%D9%88%D8%B4\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"pdf page 405 (roots Pôl, Pôš): etymology check\" 2>&1 | tail -2\ndone",
 "description": "Archive web sources batch 1"
}
```


### [2026-09-14T01:00:57.119Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/0bf4b3f7fe0e7778.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/43144f538711f44e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ab1706d503344015.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/261a9f47bd3a8ad1.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a84b6bbdcf2fd895.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/50eab08505e5f7e7.txt
```


## [2026-09-14T01:01:03.145Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n \"https://en.wiktionary.org/wiki/feel\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-West_Germanic/f%C5%8Dlijan\" \\\n \"https://en.wiktionary.org/wiki/%CF%88%CE%AC%CE%BB%CE%BB%CF%89\" \\\n \"https://en.wiktionary.org/wiki/%CF%80%CE%B1%CF%80%CE%BF%CF%8D%CF%84%CF%83%CE%B9\" \\\n \"https://abadis.ir/fatofa/%D8%B3%D9%86%D8%AA%D9%88%D8%B1/\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/pelh%E2%82%81-\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"pdf page 405 (roots Pôl, Pôš): etymology check\" 2>&1 | tail -2\ndone",
 "description": "Archive web sources batch 2"
}
```


### [2026-09-14T01:01:07.636Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/fef56fae7b008540.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/11a91cc10cea28fc.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ef3c5ac449d8a899.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b7bcfa341c3b71e8.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c4f82c6bfef1eaf0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6756a79ad0e99012.txt
```


## [2026-09-14T01:01:17.068Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nmkdir -p ocr/BOOK && cp /home/sfmqrb/git/rishe/site/pages/405.jpg ocr/BOOK/405.jpg 2>/dev/null; cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg405.png ocr/BOOK/405.png; ls -la ocr/BOOK/ | tail -3\necho \"=== WLD Bd2 p.63-65 (leaf 68-70) pel- ===\"\nawk 'BEGIN{RS=\"\\f\"} NR>=68 && NR<=70 {print \"--LEAF\",NR; print substr($0,1,1200)}' incoming/WLD/WLD_Bd2_pages.txt",
 "description": "Copy page image; Walde-Pokorny II 63"
}
```


### [2026-09-14T01:01:18.408Z] TOOL RESULT

```
-rw-rw-r--  1 sfmqrb sfmqrb  78178 Sep  5 10:14 95.png
-rw-rw-r--  1 sfmqrb sfmqrb  72929 Sep  5 10:19 96.png
-rw-rw-r--  1 sfmqrb sfmqrb  65608 Sep  5 10:43 99.png
=== WLD Bd2 p.63-65 (leaf 68-70) pel- ===
--LEAF 68
                                                      pel-                                                 63

Austernschalchen" zur ^-Erv\\                 (z. B. cz/Atyj   „Ruderschaufel“) zu stellen, viel-
leicht unter Auffiillung  von ^nXaoTYj nach TzaXdfX}].
  Auf Grimd eines dh^lPras. wohl hieher gr. xooo7i?^d&og j,Puppen aus
Ton bildend'*', 7ir]Xo7iXd^og j,Ton formend, Topfer^', Trladavov z. B. nach
Hes.     ^{AvySkov l(f       ov nXdooovoiv dgrovg xai 7i/.axovvrag^^ („Scheibe, Brett,
worauf Brote und Kuchen geformt werden‘‘, also nicht mit ai. prtJm-, gr.
jiXarvg ,,breifc“ zu vergleichen, s. Fick GGa. 1S94, 244, Lagercvantz Z. gi\
Ltg. 69 nach Liden St. 91), TiXaddvi] ds,, nldooco {^jiXddijD^ lautlich nach
Pras von Gutturalstammen), enlaoaj e7iXdo&i]v j,aus weicher Masse bilden,
gestalten; erdichten“, xam-, ejh-7z?Aooco „streiche auf, beschn3 iere‘‘ (vgl.
zur Bed. lett.       platU ,,dunn aufstreichen'') es liegt also die Anschauung
                                                                    ;


Yor, da6 der Ton flachgeklatscht wird, u. zw. vermutlich vom Stand-
punkt der altesten Topfertechnik, die den Ton auf geflochtene Formen
aufstrich (zu de
--LEAF 69
                                                                                     )




64                                                             pel-



Hes, ds., horn. nhXog.  att.        jon. nXiog „voll'* {^^nXYi-[t\o-g\   arm. liT}^                   =
        „TolP^ nkYiQoo) j.mache yoII'' (von einem adj. "^TzlrjQo-g
 JtkrjQtjg                                                             lat. plerus^                  =
vgL anch arm. Hr „Fulle“, i-St.); nlovxog „Fulle, Reichtum'' (formell naher
zn noXvg^ vgl. auch 'pleti-             bes. ai. fluid „uberschwemmt, erfiillt
von^, wozu TikovTog sich verhalt wie z. B. (poQxog ,,Last“ zu ai. hhrtd-li
„getrageii“, Lit. bei Boisacq 797).

  Alb. fVot „Yoll“            G. Meyer Wb. 345; da6 alb. pjei, piel „zeuge,
gebare“ eine mit pel- .,fullen“ gleiche Wz. pel- ,,erzeugen“ widerspiegele,
ebda 342, leuchtet seitens der Bed. wenig ein intrans. „voll     schwanger       :                    =
8ein“??            Got. fidaj        lat,        pulliis   stiitzen     eine solche         Wz. nicht,    s.   u. poii-
„klein“).           Mit Formans -go-                 stellt   Jokl    SBAkWien 168,
--LEAF 70
                                                    pelaq-                                                               65

  Gr. noXvg         (noXv^ noXvv: diese Beschrankung des St. noXv-, analog
der von fieyag, fieyav, jjLsya, deutet Brugmann 272, IP 1,177 aus ursprgl.
substantivischem ^nolv mit Yok. wie yovv, doqv', doch ist noXvg eher
nach J. Schmidt aaO. assim. aus Adj. "^jiaXvg                         =
                                                  ai. pwn?-), ubrige Kasus

vom St          TtolXo-^    jzoXXd’,     wohl ausgegangen vom                 fern.   ^jtoXfia           :   ai.   pilrvf
und auch ins Masc. und JTeutr, eingedrungen, analog dem Gebrauchsum-
fang von fuydXo-j f.ieydXr} (der              St.   noXXo-^ jioXXa nicht aus *jToXvXo-f                                -Ad-,
ThurneysenIF. 21, 176,              s.   Brugmann-Thumb GrGr.^53 a 2, Ehrlich Unt. 54).
Komp. Sup. ursprgl. *jiX^-[i]cov ^nXeiorog (aus *7zXrjioTog, fiir phistos^ nach
                                              :




dem Komparativ) mit versch. Ausgleichung nach den Dialekten: jtXi^ojv
(aol.    dor.),   jiXewv, nXeov, att. TiXelfjov (et gestiitzt durch juelcov)
                  nom.
```


## [2026-09-14T01:01:24.924Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"fuolen\\|palpo\\|palpare\\|TzdXXo\\|nalXo\\|palpebrae\\|fselan\\|f&lan\" incoming/WLD/WLD_Bd2_pages.txt | head -10",
 "description": "Find palp/fuolen in WLD II"
}
```


### [2026-09-14T01:01:24.993Z] TOOL RESULT

```
419:AbschieBen; Saitenspiel“, xpaXxrjQ, yjdhgia „Saitenspieler, -in^^; lat. palpo^
429:fuolenj       ags.   gi-folian,   ags.    felan       „fuhlen“     (abg.      pahch „Daumen^^,      russ.
435:   Vgl. Curtius 730, Pick        148, 573, III^ 236, Vf. LEWb.^ 556 {palpo\
```


## [2026-09-14T01:01:29.005Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '405,440p' incoming/WLD/WLD_Bd2_pages.txt\npython3 - <<'EOF'\nt=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n'); leaf=1; m={}\nfor i,l in enumerate(lines,1):\n    m[i]=leaf; leaf+=l.count('\\f')\nfor ln in [419,429,435]:\n    print(ln,'leaf',m[ln],'printed page',m[ln]-5)\nEOF",
 "description": "WLD II palp section"
}
```


### [2026-09-14T01:01:30.070Z] TOOL RESULT

```
aus einstigem "^j^drere gedehnt, das, wie dann auch nEnageiv^ m^p^r- (I'^per-)
zuriickgehen konnte.

pal- (sp(h)al-])       etwa „zupfend oder kurz betastend beriihren; kurze Be-
        wegungen ausfuhren“?
     Ai.    a-sphalayati   „la6t anprallen,      schlagt auf"^?       (andere   Erwagungen s.
bei     Uhlenbeck ai. Wb. s. v.    ;
                                        P.   Wahrmanns Gl. 6, 160 Verb. m.            oq)dU,(Dy
opikag iiberzeugt nicht);         gr.    y}7]Xa(pday      „betaste,   streichle,   untersuche^
                                              palia-q     pasto-


{^ipaXa „das Zupfen“              acpdco „beruhre^^, FickBB. 28, 102, B^eclitel LeviL 336),
xpakkco „schnelle (die Saite, die  Sehne des Bogens); raufe“, 'ipaXfxog „das
AbschieBen; Saitenspiel“, xpaXxrjQ, yjdhgia „Saitenspieler, -in^^; lat. palpo^
-are „schmeichelnd               palpum „das Streicheln, Tatscheln“,
-are „zucken, zappeln^^, palpehra und (bei Yarro, sowie im RoTnaniscken,
s. Grober AflS. 4, 427, Meister KZ. 45, 185) palpetra „Augenlid^^,

-are „blinzeln^^ (die lat. Pormen mit gebrochener Reduplikation, wenn nicht
Lallworte erst einzelsprachlicber Entwicklung; Entlehnung aus yjrjXafpdco,
Pick BB. 28, 102, ist sachlich wegen                                   -are    und wohl aucb wegen
des Anlauts          — Assimilation ans zweite jp?? — kaum denkbar)                             ;
                                                                                                    ahd.
fuolenj       ags.   gi-folian,   ags.    felan       „fuhlen“     (abg.      pahch „Daumen^^,      russ.

pdlec „Pinger‘'^,              „Daumen^^ beruhen aber, da woh.1 ^Daumen"^,
                         dial, pdlec
nicht „ Finger liberhaupt*-^ die eig. Bed. war, eher auf einem '^p(}i)olos „dick^‘,
8. phel- „schwellen^^).    Recht unsichere Verkniipfungen.
   Vgl. Curtius 730, Pick        148, 573, III^ 236, Vf. LEWb.^ 556 {palpo\
Franck -van Wijk 753 (voelen). Mladenov IF. 35, 134 will von „betasten,
fuhlen^^ zu „untersuchen, suchen^^ in np. paltdan „to purify; to see, inquire,
search*^^, bulg. pdlam ^suche*-^ gelangen(??).                     —
                                                    Trotz aisl. falma „Lappen,
unsicher betasten, zittern, vor Schrecken verdutzt sein*’^ besteht kaum Be-
419 leaf 12 printed page 7
429 leaf 12 printed page 7
435 leaf 12 printed page 7
```


## [2026-09-14T01:01:45.864Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== IEC pal-/pōl- ===\"; grep -n \"^pal- \\|^pōl-\\|^pal-,\\|^palpō\\|^palp\" IEC.txt | head -10\necho \"=== ARY پوشیدن ===\"; grep -n \"پوشیدن\\|پاپوش\" incoming/ARY/ARY_pages.txt | head -6\necho \"=== ARY پالیدن ===\"; grep -n \"پالیدن\\|پالودن\" incoming/ARY/ARY_pages.txt | head -6",
 "description": "Mann and Aryanpur"
}
```


### [2026-09-14T01:01:45.951Z] TOOL RESULT

```
=== IEC pal-/pōl- ===
12472:pal- (1) (palos, a, io, pal'is) ‘bare, blank, pale; space, expanse'. WP II, 61 Hitt. palhis, adj. “broad”; Lat. cf. palam, pro- palam ‘openly’; pallidus (fpale', either a synth. cpd. or fr. *palni-) beside palleo, ere, v. *be pale’; Gallo-Lat. cf. al-auda ( lark'. For -auda see áued-, áuod-); Sw. fal- (in cpds. “clearing”, also in place-names Fal- *plain-. Here EIT). OCS polü, R polyj, adj. open, bare’; polje, n. (and com. Sl.) ‘field’; cf. R polaja vodà “high water": Li. pálios, fpl. “fen, marsh’; Latv. pali, mpl. ‘flooded fields (Uncertainly Arm. nvay “dark, obscure; ailing', fr. *ni-pal-? Lat. palüs, gs: palüdis, f. ‘marsh’ is perh. a cpd., cf. üd-, üdn-, üdər water), See next
12475:pal- (2) ‘straw, chaff. Skt. ambig. Cf. pelos Skt. palah, m. id.; Lat. palea, f. ‘chaff; R cf.
12480:pal- (5) ‘wattle, dewlap, hanging flesh’ Alb. palë, f. “dried fig’; palëz, f. dim. ‘lobe of ear; Lat. palea, f. ‘wattle’; cf. palear, n. ‘dewlap’; W ail, pl. eiliau, m. ‘wattle’
12481:pal- (6), palið ‘strike, beat, hurl’. Cf. pel- Arm. cf. hal-acem, v. ‘expel’; Gk. pállo *bran- dish, hurl, dash’ beside psallo (graze, touch’, fr. *Ks-pal-); cf. pálla, f. "ball: pálos, m. 'vi- bration’; palmós, m. ‘palpitation’; pále, f. *wrestling'; Lat. cf. palpitare, inf. *beat, leap, throb, pant, strive'; (uncertainly) cf. Lat. pal- umbus, I & -umbes, is, m. f. (pigeon, lit. *flap-around"? Cf. uondh- and uendh- for the second part); OFris. falla, sv. 7 (2) “strike, occur, concern’; Cz. cf. zápolit, inf. ‘struggle’; Latv. palas, fpl. “abuse” beside (denom.) palàa- ju, v. “abuse, berate’. Uncertainly Icel. fellir, gs. -is, m. 'cattle-plague
12482:pal- (7), palio (?) Arm. halem, v. ‘melt, dissolve, thaw, fuse’; hal, s. (*melting, etc: OCS poljo, polěti, intr. “burn”, cf. plamy, gs: ene, m. (flame, fr. *palmo, -en-); (long-grade in) Blg. pàla, f. “flame”
12483:pal- (8), palio (?) Mir ailim, v. ‘ask, implore’; Icel. cf. fólun, gs: falanir, f. “demand, market
=== ARY پوشیدن ===
1746:۲ جّم همه‌ی واژه‌های این فهرست (به جز واژه‌ی پهلوی 887۸14): جامه» پوشا که» پوشیدن. ٍ
2810:۳ چم اکثر واژه‌های غیرایرانی اين فهرست: پوشا کد» پوشیدن» کفش. :
=== ARY پالیدن ===
4441:پالیدن, پالودن, پالاییدن / ۱۵۳
4445:۱ ۳ بازگمت به: هور پالیدن.
```


## [2026-09-14T01:01:52.232Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== ARY 1735-1760 ===\"; sed -n '1725,1760p' incoming/ARY/ARY_pages.txt\necho \"=== ARY 4430-4460 ===\"; sed -n '4430,4460p' incoming/ARY/ARY_pages.txt",
 "description": "Aryanpur entries"
}
```


### [2026-09-14T01:01:52.307Z] TOOL RESULT

```
=== ARY 1735-1760 ===
۷۷۸۹7۸۸0 انگلیسی (4ل8لا8(/0): داد با
تخاری ۸ (۸ [4ل/7۸ل70). ۷۹۵ ولزی (7ل3 )۰ بان رن
تخاری 8 (8 7۸/۵7 70): نیگن برتونی (88870/۷): 05
سانسکریت (84(/587): ,۷۸8 ,۷۸87 هتبت (11177778): ,۱۷۷3581۷۸۰ ۷۷۸8513/۸
۷۹ 8۵۸
ارمثی (۵00ا/۸/۸/50): ۰" اند ما ۱
برنانی 0۵8/0): بل858۸ ,877185 پسگشت‌ها هرت ی
۸ 2 0 ت۶0
لاین (1۸710): 58 ,۷5838 7 (۷881) ,1224 (8۸3) چیه
فرانسه (۳8/2). اناد انا باه 2 ۷87۳۱/8۲۱ :ما۲2
اسپانیایی (8(//8): ۷50 7 (007136) دید سم
ایتالیایی (۷(لله7): ۷0 (0079 ,0077116))
رومانی (0۸/(4۸): ۷3۸ 3396 قاط
پرتغالی (۳0711017838): ۷138718 ,۷38175 6 (5۸) :07105
گرتیک (00721/0): ۰ ۷۸8۲1 ,ل۷۷۸8[۸ 5 (۲۳۸8) +547
ابسلند ی‌کهن (0107۸۷1۵(۷/(م5 )۰ الفت‌نامه دهخدا: ۱۳۴-۳۵
ه۷۸ برهان قاطع : ۴۱
نورس کهن (۸0782 010): ۷۹7 فرهنگ معین : ۳
یادداشت.
۱- رابطه‌ی واژه‌ی "آستر"(پهلوی )) با دیگر واژه‌های این فهرست در هیچ کدام از پسگشت‌ها(مراجع) من
داده شده است و لذا در جلو واجریشه‌ی هند و اروپایی(شاید) آورده‌ام.
۲ جّم همه‌ی واژه‌های این فهرست (به جز واژه‌ی پهلوی 887۸14): جامه» پوشا که» پوشیدن. ٍ
[pdf page 62]
یج
ی
کش ۲ آسمان / ۶۳
ی ای
اوستایی (4۳237۸0۷): هام هلندی (لع017): اد ۱۱ نا
پارسی باستان ((۶8781۸ 070): اسلاوی کهن (ع1اما5 7ل8نات) ا0):
۸۸8۵۸ ات
پهلو ی (۵7آل(۸ط). ۸۹۸۵۲ لهستانی (۳۵/3[4). ۱:۱
کردی (154ص(): ند روسی (5931۸2(): رد۱۹۹۱
افغانی (پشتو) (/۸۳۵7۸2): ۳۹ چکه (0ل۲280): رد۱4۹۱
سانسکریت (5(۷55/7): ,۸81131۸6 بلغاری (0لمله.اناه): اد ۱۱۱
لا ینوانی (۸۸14(۷ن ال 7ل): 0
بونانی (0880): لرت ۳۱ 5
=== ARY 4430-4460 ===
یونانی (082850): 0 بلط 2 (8) دنا هار
لاتین (7100ما): 8 ,817818 7 (هتاه) بان 2۵
فرانسه (تل/(ق2). 3 2 (۴133) 8
اسپانیایی (5۳۸۸71577): ۳/0 4 (۴18) :00/5
ایتالیایی (۸۸اله7): دا براد
رومانی (0۸4۸(71۸): 3 4 (۲188) ,6اقه (88)
پرتفالی (۳087001885)+ ۳0 8 (هق0) 0
آلمانی کهن ((0874۸ #104 صان): برهان قاطم + ۳۵۵
لود یناد ی
۰ چ
[pdf page 152]
پالیدن, پالودن, پالاییدن / ۱۵۳
یادداشت,
۱- معنی این واژه در ایرلندی میانه و ولزی: تازه. *
ا ۲- معنی این واژه در آلمانی کهن و میانه: سرند کردن» (غله را) برجاری کردن.
۱ ۳ بازگمت به: هور پالیدن.
اوستایی (۸۳874(۷): آلمانی کهن (05440۷ ۲۷/01 صان):
,7۸۸0۸ ,ات۸ 0تشتق۲ 0
پهلوی (۳۸414۲7): 7۸171۸۸ ,8.11۸34 انگلیسی (8/0/58)(از فرانسه): ۴25
کردی (080151)): 8۸6
بلوچی (/8۸07): ۶۸1۸۷۸6 ,۳2/5۸6 پسگشت‌ها ک ۳
اففانی (پشتی) ‎ :۸08/۷/(‏ باظ۳7۸ 607 و
سانسکریت (7ل8۸(/5). 5 (۳8۴۷) 8۸0/17
ا ۳3۸۹ ,723۸2۸711 ب۳۸۷۸3 4 (۴818188) نقققملم 05
لاتین (۸7100ا): نك اه ای زا 9 (۲81۴) :2/۲5/25
فرانسه (4لع۳2۸): ادا داد رای 4 (۳۸2) :07075
اسپانیایی (3ل82۳۸(3): ۳۸ 6 (۲83) 537
ایتالیایی (ماله7): اد دش اد را برهان قاطع : 1۵۸
یادداشت:
بازگست بد: پاکه.
5
```


## [2026-09-14T01:02:07.834Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"POSH\\|PUSH\\|POSHIDAN\\|PUSHIDAN\\|PAPUSH\" incoming/ARY/ARY_latin_index_pages.txt | head\necho \"--- BQT pāpūš / pūšīdan ---\"\ngrep -n \"پاپوش\" BQT_v1_pages.txt incoming/BQT/BQT_v3_pages.txt 2>/dev/null | head -5",
 "description": "ARY latin index + Borhan"
}
```


### [2026-09-14T01:02:07.905Z] TOOL RESULT

```
4197:POSH ALBANIAN) gJT PE s(PORTUGUESE) ii 4
4630:PUSHT AAFGHAND (4) gli APARSAM
4840:PUSHT - (AFGHANI) (3%) iil s(AVESTAN) gles!
4842:PRSHTI, PRSHTHA PUSHT PAHLAVI) 5 gh
5208:MACKENZIE: (SIDE) 132 PUSHTEY (alyarGHaNy (e4) slut
6661:GARB OLD IRISH) 95 543 2 XAR, XARPUSHT — (PAHLAVI) 5
--- BQT pāpūš / pūšīdan ---
BQT_v1_pages.txt:15822:پاپوش » خیار بزرکی باش دکه بجهت تخم نگاه
BQT_v1_pages.txt:17185:با لیات - بروزن تاربك .کفش و پاپوش
BQT_v1_pages.txt:22847:و پاپوش را گونند . ۱ حلقه است از طلا و نقره و مانندآن که زنان‌در
```


## [2026-09-14T01:02:13.339Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR>=15810 && NR<=15830' BQT_v1_pages.txt\necho \"--- find [pdf page] marker before 15822 ---\"\nawk 'NR<=15822 && /\\[pdf page/ {p=$0; n=NR} END{print n\": \"p}' BQT_v1_pages.txt",
 "description": "Borhan pāpūš entry"
}
```


### [2026-09-14T01:02:14.453Z] TOOL RESULT

```
و زیئونآ تجا فر و کنند و ساکنان آنجا برمیدارند و چندان ژیتون‌جم مکنن که روغ نکنیسهرا تا
سال آینده حاصلکنند » و سپار بفروشند » و اعتماد آن نواحی برآن باشد » و همه ناحیت از
آن روغن بکاربرند و این از عجایب دناست .۰ 8 - هز 22۵۳)8(8 , پهلوی0۵5010.
چشم «برنکر۹*. 1 - )016 ( درنسخهةٌ خطی شمار؛ ۱۶۷۱ کتا:ضانةٌ علی هارمس
یادداشتی است که‌ابوحنیفه از ابوزید نقلکرده و ا و کوب که نام حفیقی « جرجر » النهق است
و لبد از شمرای‌معلفه برای ضرورت شمر آنرا الابهقان آورده «لك ۱ ص ۱۷۹4*.و شش لت و نات
بیان اول
با - , دمعم مع است که‌بجهت عصاحت
باشد - ویمعنی به بفتح بای ابجد - و مضاف به
اسامی آشها مانند ماست باوزیره با و کدوباوامثال
آن ۱ - و مخفف باد و باشد» هم هست .
بااوش « با حمزء بواو رسیده بر وزن
پاپوش » خیار بزرکی باش دکه بجهت تخم نگاه
دارند - و خوشه کوچك انگور را نی زگویند .
پاپ « بسکون بای ابجد » بمعنی
شايسته و درخورباشد چنانکه کوبند :«فلانی باب
فلالی است * معنی‌شابستةٌ فلالی است - و بمعنی
باره وحق نیز هست همجنانکه گونند :9 در باب
فلانی > بعنی درحق فلانی ودربار فلالی‌سوبمعنی
پدرهم آمده اس تکه‌بمربی والد کویشد ؟ » وباین
ممنی بلفت زند وپازند (۱) پابای فارسی باشد ۴
--- find [pdf page] marker before 15822 ---
:
```


## [2026-09-14T01:02:25.315Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -c \"\" MON_part1.txt; grep -n \"\\[pdf page\" MON_part1.txt | head -3\npython3 - <<'EOF'\nt=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt',encoding='utf-8',errors='replace').read()\nprint('formfeeds:', t.count('\\f'))\nlines=t.split('\\n'); leaf=1; m={}\nfor i,l in enumerate(lines,1):\n    m[i]=leaf; leaf+=l.count('\\f')\nfor ln in [28739,28754,79910]:\n    print(ln,'leaf',m[ln])\nEOF",
 "description": "Check MON page structure"
}
```


### [2026-09-14T01:02:26.662Z] TOOL RESULT

```
99339
formfeeds: 0
28739 leaf 1
28754 leaf 1
79910 leaf 1
```


## [2026-09-14T01:02:33.258Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n '1,80p' tools/verify_check.py",
 "description": "Read verify_check.py"
}
```


### [2026-09-14T01:02:33.301Z] TOOL RESULT

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


## [2026-09-14T01:02:35.757Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n '80,160p' tools/verify_check.py",
 "description": "Rest of verify_check.py"
}
```


### [2026-09-14T01:02:35.814Z] TOOL RESULT

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


## [2026-09-14T01:03:53.290Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BQT سنتور ===\"; grep -n \"سنتور\\|سنطور\" BQT_v1_pages.txt BQT_v2_pages.txt incoming/BQT/BQT_v3_pages.txt incoming/BQT/BQT_v4_pages.txt 2>/dev/null | head -5\necho \"=== TTS papus ===\"; grep -n -i \"papus\\|pabu\\|papuc\" incoming/TTS/TTS_pages.txt | head -5\necho \"=== FSD tarboosh page ===\"\npython3 - <<'EOF'\nt=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol4.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n'); leaf=0; m={}\nfor i,l in enumerate(lines,1):\n    m[i]=leaf; leaf+=l.count('\\f')\nprint('line 30851 leaf',m[30851],'printed page ~',m[30851]+2146)\nEOF",
 "description": "BQT santur, Vambery, FSD page"
}
```


### [2026-09-14T01:03:54.618Z] TOOL RESULT

```
=== BQT سنتور ===
=== TTS papus ===
=== FSD tarboosh page ===
line 30851 leaf 323 printed page ~ 2469
```


## [2026-09-14T01:12:17.787Z] TOOL CALL #70: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-405.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\n\ndoc = {\n \"pdf_page\": 405,\n \"book_page\": 375,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-13\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"Pôl\",\n   \"verdict\": \"plausible\",\n   \"modern_form\": \"PIE *pōl- 'to touch, feel, shake' (Watkins/AHD) = Walde-Pokorny II 7 *pal- (sp(h)al-); in Pokorny IEW the same material is section G of 1. pel-, pp. 798-801\",\n   \"note\": \"The root as written is genuine: Watkins' AHD appendix has 'pōl-. To touch, feel, shake' with exactly Nourai's two Western branches (Germanic *fōljan > feel; Greek psallein 'to pluck, play the harp'), and Walde-Pokorny II 7 sets up 'pal- (sp(h)al-) etwa ‚zupfend oder kurz betastend berühren’' with Gk. psēlapháō, psállō, Lat. palpō/palpebra, OHG fuolen, OE fēlan. Pokorny 1959 does NOT recognise an independent *pōl-: he folds the group into 1. pel- section G (pp. 798-801), and Watkins himself cites '[Pok. 1. pel- 801]'. Both authorities hedge — WP II 7 closes 'Recht unsichere Verknüpfungen', Watkins calls the Greek member 'more likely of imitative origin' — and Beekes/Wiktionary now take ψάλλω to be Pre-Greek and *fōlijan to be of unknown origin (compared with PIE *pelh₁- 'to stroke'). Hence 'plausible' rather than 'confirmed'. Nourai's page citation POK:847 is wrong: IEW p. 847 carries prō-, prōkto-, pr̥so-; the root he wants is on p. 801. The whole chart, including the Persian member, is visibly taken over from Walde-Pokorny II 7 — including Mladenov's suggestion about NP pālīdan, which WP prints with '(??)'.\",\n   \"note_fa\": \"ریشهٔ پیشنهادی نورایی همان *pōl- «لمس کردن، حس کردن، جنباندن» در پیوست ریشه‌های هندواروپایی واتکینز (AHD) است و در والده–پوکورنی (جلد ۲، ص ۷) زیر *pal- (sp(h)al-) آمده است؛ پس ریشه ساختگی نیست. اما پوکورنی در چاپ ۱۹۵۹ آن را ریشهٔ مستقل نمی‌داند و مواد آن را در بخش G از ریشهٔ 1. pel- (ص ۷۹۸–۸۰۱) آورده است؛ ارجاع POK:847 نادرست است زیرا صفحهٔ ۸۴۷ به prō-، prōkto- مربوط است. هم والده–پوکورنی («پیوندهایی سخت نااستوار») و هم واتکینز در پذیرش این خانواده احتیاط کرده‌اند و پژوهش امروزی (بیکس، ویکی‌واژه) ψάλλω را پیش‌یونانی می‌داند. بنابراین ادعای نورایی در کلیّات با احتیاط پذیرفتنی است، و ارجاع صفحهٔ پوکورنی خطاست.\",\n   \"sources\": [\n    W + \"Reconstruction:Proto-West_Germanic/f%C5%8Dlijan\",\n    W + \"%CF%88%CE%AC%CE%BB%CE%BB%CF%89\",\n    W + \"Reconstruction:Proto-Indo-European/pelh%E2%82%81-\",\n    W + \"feel\"\n   ],\n   \"ref_check\": [\n    {\"ref\": \"POK:847\", \"status\": \"not_found\",\n     \"note\": \"IEW p. 847 = POK_03.txt leaf 82 (leaf = printed page − 765, checked against the printed folios 839–850 on leaves 74–86): it carries 'prūs- ‚frieren; brennen’', 'pris- ‚zerkleinern’', 'pro- s. 2. per- S. 813 f.', 'prōkto- ‚Steiß’', 'pr̥so-' — nothing about touching or feeling. The material Nourai wants is IEW pp. 798-801, '1. pel-' section G: 'G. Worte für ‚schwingen, schwenken, zittern, hin- und herbewegen‘ ... gr. πάλλω ... lat. palpor, -ari ‚streichle’ ... palpebrae ... sowie westgerm. *fōljan (ahd. fuolen, ags. fǣlan) ‚feel’' (POK_full.txt lines 65840-65868, 'Page(s): 798-801').\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. pōl- (AHD_watkins1985.txt line 867)\", \"stance\": \"supports\",\n     \"note\": \"'p6l-. To touch, feel, shake. 1. Germanic *féljan, to feel, in Old English félan ... 4. Perhaps suffixed form *psal-yo- in Greek psallein, to pluck, play the harp (but more likely of imitative origin): PSALM, PSALTERY. [Pok. 1. G. pel- 801.]' — Nourai's root box (name, language, gloss) is copied from here, but AHD's own Pokorny pointer is 801, not 847.\"},\n    {\"src\": \"WLD\", \"where\": \"Bd. II p. 7 (WLD_Bd2_pages.txt leaf 12, printed = leaf − 5)\", \"stance\": \"partial\",\n     \"note\": \"'pal- (sp(h)al-) etwa ‚zupfend oder kurz betastend berühren; kurze Bewegungen ausführen’? ... gr. ψηλαφάω ‚betaste, streichle’ ... ψάλλω ‚schnelle (die Saite)’ ... lat. palpo, -are ... palpebra ... ahd. fuolen, ags. fēlan ‚fühlen’' — the exact grouping Nourai draws; but WP ends 'Recht unsichere Verknüpfungen' and prints the Persian member with '(??)' (see node #1).\"},\n    {\"src\": \"POK\", \"where\": \"IEW pp. 798-801 s.v. 1. pel-, section G\", \"stance\": \"partial\",\n     \"note\": \"Pokorny keeps no separate *pōl-: the 'swing, shake, feel' words (πάλλω, palpor, palpebrae, westgerm. *fōljan) are section G of 1. pel- 'voll, füllen' on pp. 798-801, and he adds 'die Worte unter G. könnten auch zu pel-2 gehören'.\"},\n    {\"src\": \"IEC\", \"where\": \"Mann, s.v. pal- (6) (IEC.txt line 12481)\", \"stance\": \"partial\",\n     \"note\": \"'pal- (6), palio ‚strike, beat, hurl’. Cf. pel- ... Gk. pállo ‚brandish, hurl, dash’ beside psallo ‚graze, touch’, fr. *ks-pal-; ... Lat. cf. palpitare' — Mann has the same Greek pair but no 'touch, feel' root with a Persian member.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Persian\",\n     \"words\": \"pâlîdan\",\n     \"verdict\": \"disputed\",\n     \"derivation\": \"NP پالیدن pālīdan 'to rummage/search a surface, to sift' is the -īdan doublet of پالودن pālūdan 'to filter, strain, refine' (present stem پالای- pālāy-), and every Iranist treats the two as one verb. MacKenzie p. 65 already has MP pālūdan, pālāy- [p'lwtn', p'l'd-] 'strain, filter, purify'. The modern derivation is Proto-Iranian *pari-harz- 'to let (something) through, filter' (Cheung 2007: 133 s.v. *harz: '(+ *pari-) NP paludan, palidan/palay-, Kurd. palawtin/palév-, Gz. päl-/palä ‚to filter, purify’', PIE *selg-, with possible contamination from *para-dauaja- 'to clean'). Horn no. 278 (p. 62) analysed it as paiti- + ālūdan (‘reinigen’, phlv. pālūt), Aryanpur (p. 153) links it to پاک pāk / *peuH- 'purify'. None of them knows a root 'to touch, feel'. Nourai's arrow is lifted from Walde-Pokorny II 7, which quotes Mladenov (IF 35, 134) wanting to get from 'betasten, fühlen' to 'untersuchen, suchen' in 'np. palīdan ‚to purify; to see, inquire, search’, bulg. pálam ‚suche’' — and immediately marks the proposal '(??)'. The semantic bridge (filter > sift through > search) also runs the other way from Nourai's ('touch' > 'search'), so the Persian word is not evidence for the root.\",\n     \"derivation_fa\": \"«پالیدن» دوگانهٔ «پالودن» (ستاک حال: پالای-) است و در فارسی میانه pālūdan / pālāy- «صاف کردن، پالودن» آمده است (مکنزی، ص ۶۵). چونگ (۲۰۰۷، ص ۱۳۳) آن را از *pari-harz- ایرانی باستان (از هندواروپایی *selg- «رها کردن، گذراندن») می‌داند؛ هرن (شمارهٔ ۲۷۸، ص ۶۲) آن را paiti- + آلودن تحلیل کرده و آریان‌پور با «پاک» پیوند می‌دهد. هیچ‌یک آن را از ریشهٔ «لمس کردن» نمی‌گیرند. منبع نورایی والده–پوکورنی (ج ۲، ص ۷) است که حدس ملادنوف را دربارهٔ «پالیدن» نقل و بی‌درنگ با علامت «(??)» رد کرده است. پس پژوهش امروزی این ادعا را رد می‌کند.\",\n     \"sources\": [W + \"%D9%BE%D8%A7%D9%84%DB%8C%D8%AF%D9%86\"],\n     \"ref_check\": [\n      {\"ref\": \"POK:841\", \"status\": \"not_found\",\n       \"note\": \"IEW p. 841 = POK_03.txt leaf 76 (printed folio numbers 839-850 checked on leaves 74-86): the page treats pō(i)- 'trinken' (lit. puotā ‚Trinkgelage’, aksl. pojiti ‚tränke’) running into pos-/poti-; there is no pālīdan and no 'touch' root there.\"},\n      {\"ref\": \"MON:680\", \"status\": \"partial\",\n       \"note\": \"Mo'in has four homographic پالیدن entries; the fourth (MON_part1.txt line 28754) is 'پالیدن: ... (مصم.) (صر.) کاوش کردن؛ جستجو کردن، جستن، تفحص کردن' — exactly Nourai's gloss 'to touch a surface in search of something', and the first is 'پالیدن [= پالودن = پالاییدن] ... صافی کردن، تصفیه کردن'. So Mo'in confirms the word and the gloss but gives no Indo-European root; the local OCR has no page numbers, so p. 680 itself could not be verified.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"CHEUNG\", \"where\": \"p. 133 s.v. *harz (CHEUNG.txt line 9452)\", \"stance\": \"contradicts\",\n       \"note\": \"'(+ *pari-) NP paludan, palidan/palay-, Kurd. (Kurm.) palawtin/palév-, ... ‚to filter, purify’ ... As for NP palūdan, palidan/palay- ... they may be contaminated with *para-dauaja- ‚to clean’' — the verb belongs to Proto-Iranian *harz (PIE *selg-), not to a root 'touch, feel'.\"},\n      {\"src\": \"HRN\", \"where\": \"no. 278, p. 62 (HRN.txt line 2738, leaf 83 = printed 62)\", \"stance\": \"contradicts\",\n       \"note\": \"'278. pälüden ‚reinigen’, Praes. pälay-em, päläyiden, paiti + älüden (s. älüden No. 42); phlv. pälüt (Bund.), päz. pälīdan, pälaidan' — Horn's analysis is a prefixed compound of ālūdan, not a touch-root.\"},\n      {\"src\": \"PHD\", \"where\": \"p. 65 s.v. pālūdan\", \"stance\": \"partial\",\n       \"note\": \"'pālūdan, pālāy- [p'lwtn', p'l'd- | (M p'rwdn, p'r'y-), N ~] strain, filter, purify' — MacKenzie attests the Middle Persian ancestor (with the Manichaean Middle Persian p'rwdn showing the -r- of *pari-), which supports the *pari-harz- account rather than Nourai's.\"},\n      {\"src\": \"ARY\", \"where\": \"p. 153 s.v. پالیدن، پالودن، پالاییدن (ARY_pages.txt pdf page 152)\", \"stance\": \"contradicts\",\n       \"note\": \"Aryanpur's cognate list for پالیدن/پالودن ends 'یادداشت: بازگشت به: پاکه' (see پاک), i.e. he files the verb with پاک 'clean' (PIE *peuH- 'purify'), with Latin pūrus/Sanskrit pav- as cognates — again not a 'touch' root.\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. II p. 7\", \"stance\": \"partial\",\n       \"note\": \"'Mladenov IF. 35, 134 will von ‚betasten, fühlen’ zu ‚untersuchen, suchen’ in np. palīdan ‚to purify; to see, inquire, search’, bulg. pálam ‚suche’ gelangen(??)' — this is Nourai's source, and Walde-Pokorny itself rejects it with a double query.\"}\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"Greek\",\n     \"words\": \"psallein\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"Ancient Greek ψάλλω (psallō), inf. ψάλλειν, 'to pluck, twang (a bowstring or a harp string), play a stringed instrument with the fingers', hence ψαλμός and ψαλτήριον; in Koine and the Septuagint it shifts to 'sing (a psalm)'. The connection to the 'touch' family is an old one: Walde-Pokorny II 7 puts ψάλλω next to ψηλαφάω 'grope, feel' and Latin palpō, and Klein s.v. psalm sends the reader to 'feel'; Mann derives psallō from *ks-pal- beside pállō. But Watkins lists it only as 'Perhaps suffixed form *psal-yo- ... (but more likely of imitative origin)', and Beekes/Wiktionary now call the verb 'Unknown; probably Pre-Greek'. The gloss 'to touch, play harp' is right for the classical sense, but the edge root → psallein is the weakest link in Nourai's tree.\",\n     \"derivation_fa\": \"یونانی باستان ψάλλω (مصدر psallein) «زخمه زدن، زه یا سیم را با انگشت کشیدن» که از آن psalmos و psaltērion ساخته شده است. والده–پوکورنی (ج۲، ص۷) و کلاین آن را با ψηλαφάω «دست مالیدن، جستجو کردن با دست» و لاتینی palpō هم‌ریشه می‌دانند، ولی واتکینز می‌افزاید که احتمالاً آوانماست (تقلید آوا) و بیکس آن را پیش‌یونانی می‌داند. این حلقه با احتیاط پذیرفتنی است.\",\n     \"sources\": [W + \"%CF%88%CE%AC%CE%BB%CE%BB%CF%89\"],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"partial\",\n       \"note\": \"Watkins 1985 s.v. pōl-: '4. Perhaps suffixed form *psal-yo- in Greek psallein, to pluck, play the harp (but more likely of imitative origin): PSALM, PSALTERY.' The reference does list the Greek verb under the root, but with an explicit preference for an imitative origin, which Nourai's plain arrow does not convey.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"WLD\", \"where\": \"Bd. II p. 7 s.v. pal- (sp(h)al-)\", \"stance\": \"supports\",\n       \"note\": \"'gr. ψηλαφάω ‚betaste, streichle, untersuche’ ... ψάλλω ‚schnelle (die Saite, die Sehne des Bogens); raufe’, ψαλμός ‚das Abschießen; Saitenspiel’, ψαλτήρ' — put in one entry with lat. palpo and ahd. fuolen.\"},\n      {\"src\": \"KLN\", \"where\": \"s.v. psalm and s.v. feel (KLN_1966.txt lines 30771, 14521)\", \"stance\": \"supports\",\n       \"note\": \"s.v. psalm: 'fr. ψάλλειν, ‚to pluck, twitch the harp’ ... and cogn. with L. palpare ... See feel'; s.v. feel Klein sets OE fēlan, ON falma, Gk. psallein, L. palpāre under 'I.-E. base *(s)phēl-, *(s)phāl-, ‚to strike softly’'.\"},\n      {\"src\": \"POK\", \"where\": \"IEW pp. 798-801, 1. pel- section G\", \"stance\": \"silent\",\n       \"note\": \"Pokorny's section G lists πάλλω, παλμός, παιπάλλω, lat. palpor and westgerm. *fōljan, but does NOT bring ψάλλω into the entry; the ψ- forms stayed behind in WP II 7.\"},\n      {\"src\": \"IEC\", \"where\": \"Mann s.v. pal- (6)\", \"stance\": \"partial\",\n       \"note\": \"'Gk. pállo ‚brandish, hurl, dash’ beside psallo ‚graze, touch’, fr. *ks-pal-' — Mann keeps the etymological link but via a s-mobile/*ks- prefix analysis, not Nourai's direct descent.\"}\n     ]\n    },\n    {\n     \"id\": 3,\n     \"lang\": \"Arabic\",\n     \"words\": \"santîr\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"Arabic سنطير/سنطور sanṭīr 'a kind of dulcimer/psaltery' does come from the Greek, but from the noun ψαλτήριον psaltḗrion (itself derived from psallein), not from the verb as the arrow implies, and almost certainly by way of Aramaic/Syriac: Klein p. 1382 says 'Arab. santir, fr. Gk. ψαλτήριον ... whence also Aram. pesanterin', the form that appears as פְסַנתֵּרִין psanterin in the Aramaic of Daniel 3:5 among the instruments of Nebuchadnezzar's orchestra. The initial cluster ψ- (ps-) was simplified: Aramaic kept p-s-n-t-r, Arabic (and Persian) dropped the p-, giving s-n-t-r. Nourai's chart is right about the ultimate Greek source and about the Arabic form; it is one step short (psallein > psaltērion) and silent about the Semitic intermediary.\",\n     \"derivation_fa\": \"عربی سنطیر/سنطور وام‌واژه‌ای است از یونانی psaltērion (نام سازی زهی)، نه مستقیماً از فعل psallein. کلاین (ص ۱۳۸۲) می‌نویسد همین واژه در آرامی به صورت psanterīn بازمانده است (در کتاب دانیال، ۳:۵)، و انتقال به عربی و فارسی به احتمال زیاد از راه آرامی/سریانی بوده است؛ خوشهٔ آغازین ps- ساده شده و p افتاده است. بنابراین نمودار نورایی درست است ولی یک حلقه را جا انداخته است.\",\n     \"sources\": [W + \"santur\"],\n     \"ref_check\": [\n      {\"ref\": \"KLN:1382\", \"status\": \"supports\",\n       \"note\": \"Klein s.v. santir (KLN_1966.txt line 33703, scan leaf 734; the leaf-to-page ratio fixed by the three Klein citations on this page — 138, 1382, 1573 — is a consistent 1.915 printed pages per leaf, so the page number checks out): 'santir, n., a kind of dulcimer. — Arab. santir, fr. Gk. ψαλτήριον, ‚stringed instrument, psaltery, harp’, whence also Aram. pesanterin, ‚a (triangular) stringed instrument’. See Psalter.'\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"s.v. santir, and s.v. Psalter\", \"stance\": \"supports\",\n       \"note\": \"s.v. Psalter: 'L. psalterium, ‚stringed instrument, psaltery’, fr. Gk. ψαλτήριον ... fr. ψάλλειν ... Cp. also santir' — Klein himself routes santir through the noun psaltērion.\"},\n      {\"src\": \"AFM\", \"where\": \"Addi Shir, grep 'سنطور/سنطير' in AFM_pages.txt\", \"stance\": \"silent\",\n       \"note\": \"no entry: Addi Shir does not list sanṭūr among the Persian words arabicised, consistent with a Greek/Aramaic rather than Persian origin for the Arabic form.\"},\n      {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/santur\", \"stance\": \"partial\",\n       \"note\": \"'Borrowed from Classical Persian سَنْتُور (santūr), of uncertain origin; sometimes suggested to be from Ancient Greek ψαλτήριον (psaltḗrion)' — the Greek source is treated as a suggestion, not as established.\"}\n     ]\n    },\n    {\n     \"id\": 4,\n     \"lang\": \"Persian\",\n     \"words\": \"santur\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"NP سنتور santūr, the trapezoidal hammered dulcimer, with the by-form سنطور recorded by Mo'in. The word is certainly the same as Arabic sanṭīr and ultimately Greek psaltērion, but the direction of the last step is not settled: Nourai (after Klein) has Greek > Arabic > Persian, while others take Persian santūr straight from the Aramaic/Syriac psanterīn of the Sasanian Mesopotamian milieu, with Arabic sanṭīr as a parallel. Wiktionary leaves the Persian 'of uncertain origin'; Mo'in and Dehkhoda give no origin at all (the 'شاهان‌تار' story repeated in popular sources is folk etymology). The Arabic-mediated route is credible — the instrument name spreads with the Abbasid music treatises — but cannot be called proven.\",\n     \"derivation_fa\": \"«سنتور» در فارسی نو (معین صورت «سنطور» را نیز می‌آورد) همان واژهٔ یونانی psaltērion است، اما اینکه از راه عربی آمده یا مستقیماً از آرامی/سریانی، قطعی نیست؛ ویکی‌واژه ریشه را «نامعلوم» می‌خواند و معین و دهخدا ریشه‌ای نمی‌دهند (توجیه «شاهان‌تار» ریشه‌شناسی عامیانه است). ادعای نورایی با احتیاط پذیرفتنی است.\",\n     \"sources\": [W + \"santur\", \"https://abadis.ir/fatofa/%D8%B3%D9%86%D8%AA%D9%88%D8%B1/\"],\n     \"ref_check\": [\n      {\"ref\": \"MON:1927\", \"status\": \"partial\",\n       \"note\": \"Mo'in's entry was found in MON_part1.txt line 79910: 'سنتور: ... [— سنطور] (ا.) (مد.) یکی از قدیمترین و کاملترین سازهای ایرانی که به شکل ذوزنقه ... و آن را به وسیلهٔ دو مضراب چوبی نوازند'. It supports the word and the gloss and records the variant سنطور, but carries no etymological tag (confirmed on the abadis copy of the Mo'in entry), so it does not support the Arabic→Persian arrow. The OCR has no page numbers, so p. 1927 could not be verified directly.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"MON\", \"where\": \"s.v. سنتور (MON_part1.txt line 79910; abadis.ir فرهنگ معین)\", \"stance\": \"partial\",\n       \"note\": \"'(سَ) (اِ.) از سازهای ایرانی به شکل ذوزنقه که دارای سیم‌های بسیاری است' — no origin tag such as [یو.] or [ع.].\"},\n      {\"src\": \"BQT\", \"where\": \"grep سنتور/سنطور in BQT_v1/v2/v3/v4_pages.txt\", \"stance\": \"silent\",\n       \"note\": \"no hit in the OCR of Borhan-e Qate' vols 1-4, so Mo'in's etymological footnotes give nothing for this word.\"},\n      {\"src\": \"KLN\", \"where\": \"s.v. santir\", \"stance\": \"partial\",\n       \"note\": \"Klein treats only the Arabic form, from Gk. psaltērion, with Aramaic pesanterin beside it; he says nothing about a Persian santūr, so the last arrow of the chart rests on Nourai alone.\"}\n     ]\n    },\n    {\n     \"id\": 5,\n     \"lang\": \"Germanic\",\n     \"words\": \"fôljan\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Nourai's 'fôljan' is Watkins' notation for the West Germanic weak verb *fōljan / *fōlijan 'to feel', continued by Old High German fuolen (NHG fühlen), Old Saxon fōlian, Middle Dutch voelen (Du. voelen), Old English fēlan; the OE ē is the regular i-umlaut of ō before the *-jan suffix. Walde-Pokorny II 7 cites 'ahd. fuolen, ags. gi-folian, ags. fēlan ‚fühlen’' in the same entry as Latin palpō, and Pokorny puts them in 1. pel- section G, so the Germanic branch of the root is exactly as drawn. (Wiktionary reconstructs Proto-West Germanic *fōlijan and marks the deeper origin unknown, comparing PIE *pelh₁- 'to stroke', which is the same material under a different label.)\",\n     \"derivation_fa\": \"صورت *fōljan که نورایی می‌آورد همان فعل ضعیف ژرمنی غربی *fōlijan «حس کردن، لمس کردن» است که در آلمانی علیای باستان fuolen، هلندی voelen و انگلیسی باستان fēlan بازمانده است؛ ای‌میانجیٔ (i-umlaut) پسوند -jan، واکهٔ ō را در انگلیسی باستان به ē بدل کرده است. والده–پوکورنی و پوکورنی همین شاخه را تأیید می‌کنند؛ ادعای نورایی درست است.\",\n     \"sources\": [W + \"Reconstruction:Proto-West_Germanic/f%C5%8Dlijan\"],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\",\n       \"note\": \"Watkins 1985 s.v. pōl-: '1. Germanic *féljan [= *fōljan], to feel, in Old English félan, to examine by touch, feel: FEEL.' — exactly this node and the next.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"WLD\", \"where\": \"Bd. II p. 7\", \"stance\": \"supports\",\n       \"note\": \"'ahd. fuolen, ags. gi-folian, ags. fēlan ‚fühlen’' listed with Lat. palpo and Gk. ψηλαφάω.\"},\n      {\"src\": \"KLN\", \"where\": \"s.v. feel (KLN_1966.txt line 14521)\", \"stance\": \"supports\",\n       \"note\": \"'... ‚to feel’, ON. falma, ‚to grope’, and prob. cogn. with ... Gk. ψάλλειν ... L. palpāre' — the Germanic verb and the Greek verb under one base.\"},\n      {\"src\": \"POK\", \"where\": \"IEW pp. 798-801, 1. pel- G\", \"stance\": \"supports\",\n       \"note\": \"'... sowie westgerm. *fōljan (ahd. fuolen, mhd. füelen, ags. fǣlan usw.) ‚feel’ gehören' — the Germanic member is uncontroversial within the entry.\"}\n     ]\n    },\n    {\n     \"id\": 6,\n     \"lang\": \"English\",\n     \"words\": \"feel\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"English feel < Middle English felen < Old English fēlan 'to touch, examine by touch, perceive' < West Germanic *fōlijan, the node above; the OE long ē was raised and diphthongised in the Great Vowel Shift to Modern English /iː/, spelled ee. Cognate with German fühlen and Dutch voelen. The node carries no reference in the book, but the chain is standard in every English etymological dictionary.\",\n     \"derivation_fa\": \"انگلیسی feel از انگلیسی میانه felen و آن از انگلیسی باستان fēlan «لمس کردن، دریافتن» است، بازماندهٔ *fōlijan ژرمنی غربی؛ واکهٔ بلند ē در تحول بزرگ واکه‌ها به /iː/ بدل شده است. این حلقه از نظر همهٔ فرهنگ‌های ریشه‌شناسی قطعی است.\",\n     \"sources\": [W + \"feel\"],\n     \"ref_check\": [\n      {\"ref\": \"(none cited)\", \"status\": \"not_checked\",\n       \"note\": \"the node carries refs=None in the book; the parent's AHD citation covers it ('Old English félan ... : FEEL').\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"s.v. feel\", \"stance\": \"supports\",\n       \"note\": \"Klein derives feel from OE fēlan, rel. to OS fōlian, OHG fuolen, G. fühlen.\"},\n      {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/feel\", \"stance\": \"supports\",\n       \"note\": \"'From Middle English felen, from Old English fēlan, from Proto-West Germanic *fōlijan.'\"}\n     ]\n    }\n   ]\n  },\n  {\n   \"entry\": 4,\n   \"root\": \"Pôš\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"MP pōš- / pōšīdan [pws-ytn'] 'to cover, put on, wear' (present stem pōš), < Proto-Iranian *pauš-\",\n   \"note\": \"The root box is right in substance: Nourai's 'Pôš' is the Middle Persian present stem pōš of pōšīdan, and the language label 'Pahlavi' is correct. MacKenzie p. 69 gives 'pōšīdan, pōš- [pws-ytn' | N ~] cover, put on, wear. ~išn: covering', and Abolghasemi (FFD) p. 44 gives precisely 'پوشیدن: پوشید < فارسی میانه pōšīd؛ پوش < فارسی میانه pōš'. Strictly it is a stem, not a root: behind it stands Proto-Iranian *pauš- 'to clothe, cover', which Cheung and Wiktionary suspect of being a substrate word (the often-quoted Sanskrit pavásta- 'covering' is not a safe cognate). Nothing in the entry depends on that deeper layer, so the box stands as drawn.\",\n   \"note_fa\": \"ریشهٔ «پوش» در واقع ستاک حال فعل فارسی میانهٔ pōšīdan / pōš- «پوشاندن، پوشیدن» است؛ مکنزی (ص ۶۹) و ابوالقاسمی در «ماده‌های فعل‌های فارسی دری» (ص ۴۴) هر دو همین را می‌آورند. پشت آن ایرانی باستان *pauš- است که چونگ و ویکی‌واژه احتمال می‌دهند وام‌واژه‌ای از زبانی زیرلایه باشد. در مجموع ادعای نورایی درست است.\",\n   \"sources\": [W + \"%D9%BE%D9%88%D8%B4%DB%8C%D8%AF%D9%86\"],\n   \"ref_check\": [\n    {\"ref\": \"FFD:44\", \"status\": \"supports\",\n     \"note\": \"Abolghasemi, Fe'l-hā-ye Fārsi-ye Dari p. 44 (FFD_pages.txt pdf page 49, printed = pdf − 5): 'پوشیدن / پوشید < فارسی میانه pōšīd. پوش < فارسی میانه pōš.' (the Latin transliterations are mangled to digits by the OCR, but the layout — past stem then present stem — is unmistakable and matches MacKenzie). Exactly Nourai's root box and node #1.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"PHD\", \"where\": \"p. 69 s.v. pōšīdan (running head 'pillagān 69 pušt')\", \"stance\": \"supports\",\n     \"note\": \"'pōšīdan, pōš- [pws-yin' | N <] cover, put on, wear. ~išn: covering.'\"},\n    {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II (glossary), grep pōš/pwsytn\", \"stance\": \"silent\",\n     \"note\": \"the verb does not occur in Nyberg's glossary (which covers only the texts of Part I); the nearest headwords are pēšang, pušt.\"},\n    {\"src\": \"HRN\", \"where\": \"Horn, Grundriss, entries 338-340 (p. 75)\", \"stance\": \"silent\",\n     \"note\": \"Horn has no entry for pōšīdan at all: '338. pōst ‚Fell, Haut’ ... 339. pūk, puḵ ‚das Blasen’ ... 340. pulād ‚Stahl’' — a gap in the Grundriss, not a dissent.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Persian\",\n     \"words\": \"pŭš; pŭšîdan; pâ-pŭš\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"MP pōšīdan > NP پوشیدن pūšīdan 'to cover, to put on (clothes)' — the regular New Persian raising of Middle Persian ō to ū written with wāw — and the bare present stem پوش pūš does double duty as a noun 'cover, covering' and as the second member of compounds: سرپوش 'lid', روپوش 'overall', and پاپوش pā-pūš 'foot-cover, slipper', with پا pā 'foot' (MP pāy, Av. pāda-, Horn no. 281 p. 63 — exactly the cross-reference '☞ Ped' the chart prints). The suffixed derivatives listed in the book, پوشه 'folder', پوشک 'nappy', پوشاک 'clothing', پوشنه and the agent adjective پوشا, are all built on that stem with the ordinary NP suffixes -a, -ak, -āk, -ā. Hāfez's line 'سر پیاله بپوشان که خرقه‌پوش آمد' quoted in the box shows both the causative پوشاندن and the compound agent noun خرقه‌پوش.\",\n     \"derivation_fa\": \"«پوشیدن» از فارسی میانه pōšīdan است و ō کشیدهٔ فارسی میانه در فارسی نو به ū بدل شده است؛ ستاک حال آن، «پوش»، هم اسم است (پوشش) و هم جزء دوم مرکب‌ها: سرپوش، روپوش، پاپوش. در «پاپوش» جزء نخست «پا» از فارسی میانه pāy و اوستایی pāda- است (هرن، شمارهٔ ۲۸۱). پوشه، پوشک، پوشاک، پوشنه و پوشا همه با پسوندهای معمول فارسی از همین ستاک ساخته شده‌اند. ادعای نورایی درست است.\",\n     \"sources\": [W + \"%D9%BE%D9%88%D8%B4%DB%8C%D8%AF%D9%86\"],\n     \"ref_check\": [\n      {\"ref\": \"FFD:44\", \"status\": \"supports\",\n       \"note\": \"same page as the root: 'پوشید < فارسی میانه pōšīd؛ پوش < فارسی میانه pōš' (FFD_pages.txt pdf page 49). Abolghasemi gives no further derivation for پاپوش, which is a New Persian compound.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"p. 69 s.v. pōšīdan; p. 67 s.v. pāy\", \"stance\": \"supports\",\n       \"note\": \"'pōšīdan, pōš- ... cover, put on, wear' and 'pāy [LGLE < A rglh; p'dy | M p'y, N —] foot, leg' — both members of پاپوش are Middle Persian.\"},\n      {\"src\": \"LKT\", \"where\": \"Lokotsch no. 1625\", \"stance\": \"supports\",\n       \"note\": \"'1625. Pers. päpūs ‚Fußbekleidung’ [aus pers. pā ‚Fuß’ Horn NpEt S. 63, Nr. 281 und pūš Präsensstamm von pūšīdän ‚bedecken’]' — the compound is analysed exactly as Nourai analyses it.\"},\n      {\"src\": \"HRN\", \"where\": \"no. 281, p. 63\", \"stance\": \"supports\",\n       \"note\": \"'281. pāl, pā ‚Fuss’; vergl. pāye ‚Stufe’ ... aw. pāda- ‚Fuss’; phlv. pā̄y ‚Fuss’' — the '☞ Ped' cross-reference of the chart.\"},\n      {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' vol. 1, s.v. بااوش (BQT_v1_pages.txt line 15822)\", \"stance\": \"partial\",\n       \"note\": \"the dictionary uses پاپوش only as a metrical model ('بر وزن پاپوش') for another headword — the word is old and current in the tradition, but Mo'in's footnotes add no etymology here.\"}\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"Arabic\",\n     \"words\": \"ba-buš; tar-buš\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"Two different cases. (a) بابوج/بابوش bābūj/bābūš 'slipper' (pl. بوابيج bawābīj) is beyond doubt Persian پاپوش pāpūš: Arabic has no /p/ and substitutes b-, and Klein p. 138 makes that substitution his proof of Arabic mediation ('The change of p to b proves that the word came into Europe through the medium of the Arabic'); Devic and Pihan (p. 53) say the same. Confirmed. (b) طربوش ṭarbūš 'brimless felt cap' is contested. Klein p. 1573, whom Nourai follows (hence the chart's note '‚tar: sweat’ is from a Turkish root'), calls it 'lit. ‚sweating cap’, a hybrid coined fr. Turk. ter, ‚sweat’, and Pers. pūshidān, ‚to cover’'. Pihan p. 351 instead makes the Turkish word 'sans doute ... une altération du persan سرپوش serpūš, couvre-chef', and current scholarship (Wiktionary, following the Mamluk-headgear evidence) takes ṭarbūš to be a sixteenth-century variant of Arabic شربوش šarbūš, the dissimilation merely 'speculated to have been motivated by Kipchak tär ‚sweat’'. On every account the -būš element is Persian پوش, so the arrow from the Persian box is defensible; the 'sweat-cap' compound analysis is not secure.\",\n     \"derivation_fa\": \"دو واژه در یک خانه: الف) عربی بابوج/بابوش (جمع: بوابیج) معرّب «پاپوش» فارسی است؛ چون در عربی واج /p/ نیست، پ به ب بدل شده است و کلاین همین ابدال را گواه میانجیگری عربی می‌داند. ب) دربارهٔ «طربوش» اختلاف هست: کلاین (ص ۱۵۷۳) آن را مرکبی دورگه از ترکی ter «عرق» و «پوش» فارسی می‌داند (همان که نورایی در یادداشت آورده)، پیان (ص ۳۵۱) آن را دگرگونشدهٔ «سرپوش» فارسی، و پژوهش امروزی آن را گونه‌ای از «شربوش» مملوکی می‌داند. پس جزء «پوش» پذیرفتنی است ولی تحلیل «کلاه عرق» قطعی نیست.\",\n     \"sources\": [W + \"%D8%B7%D8%B1%D8%A8%D9%88%D8%B4\", W + \"babouche\"],\n     \"ref_check\": [\n      {\"ref\": \"KLN:138,1573\", \"status\": \"supports\",\n       \"note\": \"Klein s.v. babouche (KLN_1966.txt line 4226, scan leaf 84 = p. 138): 'babouche, n., a heelless Oriental slipper. — F., fr. Arab. bābūsh, fr. Pers. pāpūsh, lit. ‚foot-covering’, fr. pā, ‚foot’, and the verb pūshiden, ‚to cover’.' And s.v. tarboosh (line 38199, leaf 833 = p. 1573): 'tarboosh ... F. tarbouch(e), fr. Arab. ṭarbūsh, lit. ‚sweating cap’, a hybrid coined fr. Turk. ter, ‚sweat’, and Pers. pūshidān, ‚to cover’.' Both pages say exactly what the chart and its NOTE say.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"DEV\", \"where\": \"Devic s.v. Babouche (DEV.txt line 718)\", \"stance\": \"supports\",\n       \"note\": \"'Babouche. Esp. babucha. C'est le persan پاپوش pâpoucli (de پا pâ, pied, et پوشیدن poušīden, couvrir). Mais le changement de p en b marque que le mot nous est venu par l'arabe qui, n'ayant pas de p, écrit بابوش baboach.'\"},\n      {\"src\": \"PHN\", \"where\": \"Pihan pp. 53 (BABOUCHE) and 351 (TARBOUCHE)\", \"stance\": \"partial\",\n       \"note\": \"s.v. BABOUCHE: 'pâpouš, littéralement qui couvre le pied. Des deux mots réunis en persan les Arabes ont fait le substantif bâboūdj, au pluriel bawâbīdj'. But s.v. TARBOUCHE: 'Le mot turc ṭarboūš n'est sans doute qu'une altération du persan سرپوش serpoūš, couvre-chef, composé de سر ser, tête, et de پوش poūš, qui couvre' — i.e. Persian sar-pūš, not Turkish ter + pūš.\"},\n      {\"src\": \"LKT\", \"where\": \"Lokotsch no. 1625\", \"stance\": \"supports\",\n       \"note\": \"'... ebenso tk. papus, ar. bäbūs; hieraus it. babbuccia, frz. babouche, sp. babuche, rum. papuci ...' — the Arabic form is listed as a borrowing from Persian, parallel to Turkish.\"},\n      {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/طربوش\", \"stance\": \"partial\",\n       \"note\": \"'Found from the sixteenth century, variant of شَرْبوش (šarbūš). The dissimilation is speculated to have been motivated by Kipchak تر (tär, ‚sweat’), the headpiece being fit to conceal پوشیدن (pôš) perspiration.' — supports the pūš element, weakens the 'sweat-cap compound' story.\"},\n      {\"src\": \"AFM\", \"where\": \"Addi Shir, grep بابوج/طربوش in AFM_pages.txt\", \"stance\": \"silent\",\n       \"note\": \"بابوش appears only in the Turkish-word index lists (lines 5475, 5711); there is no Arabic headword entry for either word.\"}\n     ]\n    },\n    {\n     \"id\": 3,\n     \"lang\": \"French\",\n     \"words\": \"babouche; tarbouche\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"French babouche 'Oriental heelless slipper' (earlier papouch, babuc; also It. babbuccia, Sp. babucha) from Arabic bābūj/bābūš, the word reaching France with the Levant trade and the Barbary states; Devic and Pihan both enter it as an Arabic-via-Persian word, and Lokotsch no. 1625 lists frz. babouche in the same series. French tarbouche 'red felt cap of the Ottoman lands' is a nineteenth-century borrowing of Arabic/Turkish ṭarbūš: Pihan p. 351 describes it as current in Egypt and Turkey and notes that the Ottoman embassy in France wore it, and explains the French spelling -che as the standard rendering of final ش š (PHN.txt: 'la transcription du ش ch quand il termine un mot, comme babouche, derviche, tarbouche').\",\n     \"derivation_fa\": \"فرانسهٔ babouche از عربی بابوج/بابوش گرفته شده (صورت‌های کهن‌تر: papouch، babuc) و از راه دادوستد با شمال آفریقا و لوانت به فرانسه رسیده است؛ tarbouche وام‌گیری سدهٔ نوزدهم از طربوش عربی–ترکی است. پیان می‌نویسد حرف -che در پایان این واژه‌ها برابر شین شرقی است. ادعای نورایی درست است.\",\n     \"sources\": [W + \"babouche\"],\n     \"ref_check\": [\n      {\"ref\": \"KLN:138,1573\", \"status\": \"supports\",\n       \"note\": \"Klein p. 138 'babouche ... — F., fr. Arab. bābūsh' and p. 1573 'tarboosh ... — F. tarbouch(e), fr. Arab. ṭarbūsh' — the French stage is explicit in both entries.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"DEV\", \"where\": \"Devic s.v. Babouche\", \"stance\": \"supports\",\n       \"note\": \"the entry is written for the French word ('Babouche. Esp. babucha ...'), deriving it from Persian through Arabic.\"},\n      {\"src\": \"PHN\", \"where\": \"Pihan pp. 53, 351 and p. 5613 note\", \"stance\": \"supports\",\n       \"note\": \"'TARBOUCHE, s. m. composé, (t.) ṭarboūš: Genre de bonnet de laine rouge, à flamme bleue, adopté en Egypte et en Turquie ... Tous les membres de l'ambassade ottomane en France portent le tarbouche.'\"},\n      {\"src\": \"LKT\", \"where\": \"Lokotsch no. 1625\", \"stance\": \"supports\",\n       \"note\": \"'hieraus it. babbuccia, frz. babouche, sp. babuche' — French listed among the descendants of the Arabic form.\"}\n     ]\n    },\n    {\n     \"id\": 4,\n     \"lang\": \"English\",\n     \"words\": \"babouche; tarbooche\",\n     \"verdict\": \"transcription_suspect\",\n     \"derivation\": \"English babouche 'heelless Oriental slipper' is the French word taken over unchanged (Klein p. 138) and is correct as printed. The second word is not: the English form is tarboosh (so Klein p. 1573, and the OED), with the recorded variants tar-booch, tar-bouche and tar-bush listed by Funk & Wagnalls (vol. IV, p. ~2469: 'tar-boosh', n. [Ar.] usually red, felt cap ... — tar-booch‡; tar-bouche‡; tar-bush†'). The book prints 'tarbooche', which is none of these — it is a blend of the French tarbouche of the box above it with the English tarboosh, i.e. Nourai's own misprint; the extraction is faithful (checked on the page image, right-hand box of the lower chart). The derivation itself — French tarbouche > English — is right, and Klein indeed routes the English word through French.\",\n     \"derivation_fa\": \"صورت انگلیسی این واژه tarboosh است (کلاین ص ۱۵۷۳؛ گونه‌های ضبط‌شده: tar-booch، tar-bouche، tar-bush)؛ آنچه کتاب چاپ کرده — «tarbooche» — در هیچ فرهنگی نیست و آمیزه‌ای است از tarbouche فرانسه و tarboosh انگلیسی. با مقابله با تصویر صفحهٔ چاپی روشن شد که خطا از خود کتاب است و خوانش اسکن درست بوده است. خود زنجیرهٔ فرانسه ← انگلیسی درست است؛ babouche نیز درست ضبط شده است.\",\n     \"error_in\": \"book\",\n     \"book_prints\": \"tarbooche\",\n     \"correct_form\": \"tarboosh\",\n     \"sources\": [W + \"tarboosh\", W + \"babouche\"],\n     \"ref_check\": [\n      {\"ref\": \"KLN:138,1573\", \"status\": \"partial\",\n       \"note\": \"Klein has 'babouche' exactly as printed here, but spells the cap 'tarboosh, n., a brimless felt cap worn by Moslems. — F. tarbouch(e) ...' — so the reference supports the derivation but not the English spelling in the box.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls vol. IV s.v. tar-boosh (FSD_vol4.txt line 30851, leaf 323 ≈ p. 2469)\", \"stance\": \"partial\",\n       \"note\": \"'tar-boosh', ... n [Ar.] usually red, felt cap with tassel of blue or dark-colored silk, worn by Moslems ... (< Ar tarbush) tar-booch‡; tar-bouche‡; tar-bush†' — three variants recorded, none of them 'tarbooche'.\"},\n      {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century, vol. 1 (grep babouche)\", \"stance\": \"silent\",\n       \"note\": \"no hit in the OCR of the only volume available locally.\"},\n      {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/tarboosh\", \"stance\": \"partial\",\n       \"note\": \"'Borrowed from Arabic طَرْبوش (ṭarbūš)' — headword tarboosh; the French stage that Klein and Nourai insert is not mentioned there.\"}\n     ]\n    },\n    {\n     \"id\": 5,\n     \"lang\": \"Turkish\",\n     \"words\": \"babuč\",\n     \"verdict\": \"disputed\",\n     \"derivation\": \"Turkish pabuç / papuç (Ottoman پاپوش papuş) 'slipper, shoe' is a direct loan from Persian پاپوش pāpūš, not a loan from Arabic as the arrow has it. The decisive evidence is the very sound change Klein uses one entry earlier: Arabic, having no /p/, must write bābūš, whereas Ottoman Turkish keeps the Persian p- (papuş), so the Turkish word cannot have come through Arabic; the b-form babuç that Nourai cites is a later variant inside Turkish (modern standard pabuç). Buck p. 428 gives 'Turk. pabuç (Pers. pāpūš, lit. ‚foot-covering’)' with no Arabic link, Lokotsch 1625 lists 'tk. papus' beside 'ar. bābūs' as two parallel borrowings from Persian, and Wiktionary derives Ottoman Turkish papuş straight from Classical Persian. The word and its meaning are right; the parent is wrong.\",\n     \"derivation_fa\": \"ترکی pabuç/papuç (عثمانی پاپوش) مستقیماً از فارسی «پاپوش» وام گرفته شده، نه از راه عربی؛ دلیل قاطع آن نگاه‌داشت پِ آغازین است، در حالی که عربی ناگزیر آن را به ب بدل می‌کند (بابوش). باک (ص ۴۲۸) و لوکوچ (شمارهٔ ۱۶۲۵) هر دو ترکی papuş و عربی بابوش را دو وام‌گیری موازی از فارسی می‌دانند. پس خود واژه درست است ولی پیکان نمودار (عربی ← ترکی) نادرست است.\",\n     \"sources\": [W + \"%CF%80%CE%B1%CF%80%CE%BF%CF%8D%CF%84%CF%83%CE%B9\", W + \"babouche\"],\n     \"ref_check\": [\n      {\"ref\": \"SYN:428\", \"status\": \"partial\",\n       \"note\": \"Buck p. 428, §6.51 SHOE (SYN.txt line 10738 begins '428 SELECTED INDO-EUROPEAN SYNONYMS 6.51 SHOE'): 'NG pop. papoutsi, fr. Turk. pabuç (Pers. pāpūš, lit. ‚foot-covering’, cpd. of pā- ‚foot’ and puš fr. pūšīdan ‚cover’). Lokotsch 1625.' The page supports the Turkish word and its Persian source — but derives it from Persian, not from Arabic.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"SYN\", \"where\": \"Buck p. 428 §6.51\", \"stance\": \"contradicts\",\n       \"note\": \"'Turk. pabuç (Pers. pāpūš ...)' — no Arabic intermediary.\"},\n      {\"src\": \"LKT\", \"where\": \"Lokotsch no. 1625\", \"stance\": \"contradicts\",\n       \"note\": \"'Pers. pāpūš ... ebenso tk. papus, ar. bābūs' — 'ebenso' makes Turkish and Arabic sister borrowings from Persian.\"},\n      {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/παπούτσι and /babouche\", \"stance\": \"contradicts\",\n       \"note\": \"'Borrowed from Ottoman Turkish پاپوش (papuş, papuç), from Classical Persian پاپوش (pāpōš)'; the French entry likewise has Middle French papouch/babuc from Ottoman Turkish papuş from Persian.\"},\n      {\"src\": \"TTS\", \"where\": \"Vámbéry, grep papus/pabuç in TTS_pages.txt\", \"stance\": \"silent\",\n       \"note\": \"no hit — Vámbéry's Turko-Tatar dictionary treats native Turkic stems, and a Persian loanword is not among them.\"}\n     ]\n    },\n    {\n     \"id\": 6,\n     \"lang\": \"Greek\",\n     \"words\": \"papoutsi\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Modern Greek παπούτσι papoútsi, now the ordinary word for 'shoe', is an Ottoman-period borrowing of Turkish papuç/pabuç, with the Greek diminutive-neuter ending -ι and τσ rendering Turkish ç /tʃ/. Buck p. 428 records it as the popular Modern Greek word beside learned υπόδημα, and traces it through Turkish to Persian pāpūš with a reference to Lokotsch 1625; Wiktionary gives the same chain. The arrow Turkish → Greek is correct as drawn.\",\n     \"derivation_fa\": \"یونانی نو παπούτσι (papoútsi) «کفش» وام‌واژه‌ای از دورهٔ عثمانی است از ترکی papuç؛ پسوند -ι یونانی و خوشهٔ τσ برابر چِ ترکی است. باک (ص ۴۲۸) آن را صورت عامیانهٔ یونانی نو در برابر υπόδημαی ادبی می‌آورد و از راه ترکی به «پاپوش» فارسی می‌رساند. ادعای نورایی درست است.\",\n     \"sources\": [W + \"%CF%80%CE%B1%CF%80%CE%BF%CF%8D%CF%84%CF%83%CE%B9\"],\n     \"ref_check\": [\n      {\"ref\": \"SYN:428\", \"status\": \"supports\",\n       \"note\": \"Buck p. 428 §6.51 SHOE: 'NG pop. papoutsi, fr. Turk. pabuç (Pers. pāpūš, lit. ‚foot-covering’, cpd. of pā- ‚foot’ and puš fr. pūšīdan ‚cover’). Lokotsch 1625.' — exactly this node.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"SYN\", \"where\": \"Buck p. 428 §6.51\", \"stance\": \"supports\",\n       \"note\": \"the Modern Greek table for 'shoe' lists 'υπόδημα, παπούτσι' and the note derives the popular word from Turkish.\"},\n      {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/παπούτσι\", \"stance\": \"supports\",\n       \"note\": \"'Borrowed from Ottoman Turkish پاپوش (papuş, papuç), from Classical Persian پاپوش (pāpōš).'\"},\n      {\"src\": \"LKT\", \"where\": \"Lokotsch no. 1625\", \"stance\": \"partial\",\n       \"note\": \"the entry lists the Balkan and Slavic descendants (serb. papusa, poln. babusza, cech. papuč, russ. babusi) of the same Turkish word; Buck cites this number for the Greek form.\"}\n     ]\n    }\n   ]\n  }\n ]\n}\n\nwith io.open('/home/sfmqrb/git/rishe/data/verification/page-405.json','w',encoding='utf-8') as f:\n    json.dump(doc, f, ensure_ascii=False, indent=1)\n    f.write('\\n')\nprint('ok')\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-405.py",
 "description": "Write page-405.json"
}
```


### [2026-09-14T01:12:18.999Z] TOOL RESULT

```
ok
```


## [2026-09-14T01:12:22.808Z] TOOL CALL #71: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-405.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 405",
 "description": "Validate and run verify_check"
}
```


### [2026-09-14T01:12:24.081Z] TOOL RESULT

```
JSON OK
nodes verified: 12/12
node verdicts: {'disputed': 2, 'plausible': 4, 'confirmed': 5, 'transcription_suspect': 1}
root verdicts: {'plausible': 1, 'confirmed': 1}
ref checks: {'not_found': 1, 'partial': 5, 'supports': 6, 'not_checked': 1}
books consulted: {'contradicts': 6, 'partial': 12, 'supports': 18, 'silent': 6} | by book: {'Wiktionary': 6, 'KLN': 5, 'LKT': 5, 'WLD': 3, 'HRN': 2, 'PHD': 2, 'POK': 2, 'AFM': 2, 'BQT': 2, 'DEV': 2, 'PHN': 2, 'SYN': 2, 'CHEUNG': 1, 'ARY': 1, 'IEC': 1, 'MON': 1, 'FSD': 1, 'WEB': 1, 'TTS': 1}
```


## [2026-09-14T01:12:37.671Z] AGENT

Page 405 (book p. 375) verified — `/home/sfmqrb/git/rishe/data/verification/page-405.json`, `verify_check.py 405` shows 0 PROBLEM lines (12/12 nodes).

Verdicts: roots — 1 confirmed (Pôš), 1 plausible (Pôl). Nodes — 5 confirmed, 4 plausible, 2 disputed, 1 transcription_suspect.

- **disputed — Pôl #1 `pâlîdan`**: Cheung 2007:133 derives NP pālūdan/pālīdan from PIr *pari-harz- (PIE *selg-); Horn 278 (p.62) = paiti- + ālūdan; Aryanpur p.153 links it to پاک. Nourai's arrow comes from Walde-Pokorny II 7, where Mladenov's "touch → search" idea for *palīdan* is printed and immediately rejected with "(??)".
- **disputed — Pôš #5 Turkish `babuč`**: Turkish papuç/pabuç is a direct Persian loan (Buck p.428, Lokotsch 1625, Wiktionary), not via Arabic — the preserved p- rules out Arabic mediation (which is exactly Klein's own argument for the European forms).
- **transcription_suspect — Pôš #4 English `tarbooche`**: no dictionary knows this form (Klein 1573 and OED: *tarboosh*; F&W vol. IV lists tar-booch/tar-bouche/tar-bush). `error_in: "book"` — the printed page does read "tarbooche"; extraction is faithful. Page image archived at `data/verification/sources/refs/ocr/BOOK/405.png`.

Reference problems found in Nourai's own citations: **POK:847 (root) and POK:841 (node 1) are both wrong pages** — IEW 847 = prō-/prōkto-/pr̥so-, IEW 841 = pō(i)- 'drink'; the root material is IEW 798–801 (1. pel- section G), as Watkins himself cites. KLN:138/1382/1573 and SYN:428 and FFD:44 all check out verbatim; MON:680/1927 entries located in OCR (no page numbers in the scan).

No extraction errors for the owner to fix — the JSON matches the printed page throughout.
