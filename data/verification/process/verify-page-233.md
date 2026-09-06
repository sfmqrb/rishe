# Verification process log — verify-page-233


## [2026-09-06T15:33:26.477Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 233 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-233.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-233.json. Write /home/sfmqrb/git/rishe/data/verification/page-233.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 233` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T15:33:28.001Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T15:33:28.710Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T15:33:28.726Z] TOOL RESULT

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


## [2026-09-06T15:33:29.081Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-233.txt"
}
```


### [2026-09-06T15:33:29.102Z] TOOL RESULT

```
1	=== PDF page 233 (book page 203) ===
2	--- entry 0 ---
3	ROOT [Ethiopian] Kaffa : the plant or drink coming from Kaffa, a district in southwestern Ethiopia  (refs KLN:309)
4	#1 (parent #0) [Arabic] refs=None | qahwah : a drink or plant from Kaffa
5	  #2 (parent #1) [Persian] refs=MON:2756 | qahveh «قهوه» : coffee
6	  #3 (parent #1) [Turkish] refs=AHD:258 | qahve' : coffee
7	    #4 (parent #3) [Italian] refs=None | 
8	      #5 (parent #4) [French] refs=None | cafe' : coffee, also a coffee house
9	        #6 (parent #5) [Persian] refs=MON:2851 | kâfeh «کافه» : coffee house
10	        #7 (parent #5) [English] refs=AHD:258; KLN:309 | coffee, cafe', caffeine
11	--- entry 1 ---
12	ROOT [Pahlavi] Kafš : shoe, boot  (refs MON:3005)
13	#1 (parent #0) [Persian] refs=MON:3005 | kafš «کفش» : shoe
14	  #2 (parent #1) [Arabic] refs=MON:3005 | 
15	    #3 (parent #2) [Persian] refs=MON:3000 | kaffâš «کفّاش» : shoe maker or mender
16	  #4 (parent #1) [Greek] refs=IEC:1628 | kaukis : a kind of shoe ; kaukalon : boot shaft
17	  #5 (parent #1) [Armenian] refs=IEC:1628 | kawšik : shoe
18	--- entry 2 ---
19	ROOT [Iranian] Kaftân : a silk-filled war garment  (refs PLA:11)
20	#1 (parent #0) [Persian] refs=BQT:759; MON:1431 | xaftân «خفتان» : armor | extra: خفدان
21	#2 (parent #0) [Arabic] refs=PLA:111 | qaftan : armor
22	  #3 (parent #2) [Turkish] refs=BQT:760 | qaftan
23	    #4 (parent #3) [Russian] refs=AHD:187 | kaftan
24	      #5 (parent #4) [English] refs=KLN:220; AHD:187 | caftan : a long-sleeved garment
25	--- entry 3 ---
26	ROOT Kag -> redirect to Keg
27	--- entry 4 ---
28	ROOT Kagas -> redirect to Kagaš
29	
```


## [2026-09-06T15:33:32.070Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-233.json",
 "description": "Read source JSON for page 233"
}
```


### [2026-09-06T15:33:32.148Z] TOOL RESULT

```
{
  "pdf_page": 233,
  "book_page": 203,
  "entries": [
    {
      "root": {
        "name": "Kaffa",
        "lang": "Ethiopian",
        "refs": "KLN:309",
        "gloss": "the plant or drink coming from Kaffa, a district in southwestern Ethiopia"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Arabic",
          "refs": null,
          "words": [
            {"translit": "qahwah", "gloss": "a drink or plant from Kaffa", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "MON:2756",
          "words": [
            {"translit": "qahveh", "gloss": "coffee", "script": "قهوه"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 1,
          "lang": "Turkish",
          "refs": "AHD:258",
          "words": [
            {"translit": "qahve'", "gloss": "coffee", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Italian",
          "refs": null,
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "French",
          "refs": null,
          "words": [
            {"translit": "cafe'", "gloss": "coffee, also a coffee house", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Persian",
          "refs": "MON:2851",
          "words": [
            {"translit": "kâfeh", "gloss": "coffee house", "script": "کافه"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 5,
          "lang": "English",
          "refs": "AHD:258; KLN:309",
          "words": [
            {"translit": "coffee, cafe', caffeine", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Kafš",
        "lang": "Pahlavi",
        "refs": "MON:3005",
        "gloss": "shoe, boot"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "MON:3005",
          "words": [
            {"translit": "kafš", "gloss": "shoe", "script": "کفش"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Arabic",
          "refs": "MON:3005",
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "MON:3000",
          "words": [
            {"translit": "kaffâš", "gloss": "shoe maker or mender", "script": "کفّاش"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 1,
          "lang": "Greek",
          "refs": "IEC:1628",
          "words": [
            {"translit": "kaukis", "gloss": "a kind of shoe", "script": null},
            {"translit": "kaukalon", "gloss": "boot shaft", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 1,
          "lang": "Armenian",
          "refs": "IEC:1628",
          "words": [
            {"translit": "kawšik", "gloss": "shoe", "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Kaftân",
        "lang": "Iranian",
        "refs": "PLA:11",
        "gloss": "a silk-filled war garment"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "BQT:759; MON:1431",
          "words": [
            {"translit": "xaftân", "gloss": "armor", "script": "خفتان"}
          ],
          "script_extra": "خفدان",
          "note": null,
          "quote": {"text": "به خفتانش بر نیزه بگذاشتم - به نیرو از آن زینش برداشتم", "poet": "Ferdowsî"}
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Arabic",
          "refs": "PLA:111",
          "words": [
            {"translit": "qaftan", "gloss": "armor", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Turkish",
          "refs": "BQT:760",
          "words": [
            {"translit": "qaftan", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Russian",
          "refs": "AHD:187",
          "words": [
            {"translit": "kaftan", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": "KLN:220; AHD:187",
          "words": [
            {"translit": "caftan", "gloss": "a long-sleeved garment", "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {"name": "Kag", "redirect": "Keg"},
      "nodes": []
    },
    {
      "root": {"name": "Kagas", "redirect": "Kagaš"},
      "nodes": []
    }
  ]
}
```


## [2026-09-06T15:33:32.365Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-06T15:33:32.405Z] TOOL RESULT

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


## [2026-09-06T15:33:40.373Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['KLN','MON','AHD','IEC','PLA','BQT','LKT','SKT','PHD','NYB','HRN','HUB','FSD','WEB','TTS','DEV','PHN','AFM','TAD','ARB','HJB','RCH','SIN','FVQ','ARY']:\n    v=d.get(k)\n    print(k, json.dumps(v, ensure_ascii=False)[:600])\n    print()\n\"",
 "description": "Inspect refs_online.json entries"
}
```


## [2026-09-06T15:33:40.874Z] TOOL CALL #6: Bash

```json
{
 "command": "ls tools/ && sed -n 1,60p tools/verify_check.py",
 "description": "List tools and check verify_check"
}
```


### [2026-09-06T15:33:42.188Z] TOOL RESULT

```
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 

PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 lea

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 

SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-

NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol

FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt

WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/W

TTS {"title": "H. Vámbéry, Etymologisches Wörterbuch der turko-tatarischen Sprachen, Leipzig 1878 (repr. Osnabrück 1972)", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/etymologischesw00vmuoft (Toronto scan; also Google/bub_gb copies)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft_djvu.txt"], "page_offset": 

DEV {"title": "L. M. Devic, Dictionnaire étymologique des mots français d'origine orientale, Paris 1876", "edition_found": "1876", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairety00devi", "identifier": "dictionnairety00devi (also dictionnairetym02devigoog, fr105comparative41)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/DEV.txt", "page_offset": "leaf = printed + 26 (pp. <80) to +30 (pp. >84), e.g. leaf 29 = p.3, leaf 118 = p.88. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.

PHN {"title": "A. P. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du turc, Paris 1866", "edition_found": "1866", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairetym01pihagoog", "identifier": "dictionnairetym01pihagoog (others: bub_gb_QnsSAAAAIAAJ, dictionnairetym00pihagoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHN.txt", "page_offset": "leaf = printed + 31 (e.g. leaf 33 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://ar

AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/

TAD {"title": "Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-hurufihi (2nd ed. Cairo 1932, ed. Yusuf Tuma al-Bustani; later Library of Lebanon reprint) — Nourai lists it under Arabic authors ('Unaysi T.'); its Table IV line was lost in the OCR", "kind": "archive_djvu", "url": "https://archive.org/details/TOB1932ARAR (1932 ed.); also https://archive.org/details/ar113lang79 and https://archive.org/details/elshandawily14640", "lookup_hint": "Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; insi

ARB {"title": "al-Jawaliqi, al-Mu'arrab min al-kalam al-a'jami, Tehran 1966 (reprint of Ahmad M. Shakir's Cairo 1361/1942 edition)", "kind": "archive_djvu", "url": "https://archive.org/details/mo3rb (probably the Shakir edition) ; https://archive.org/details/almo3rab_gwaliqy_f_abduraheem (F. 'Abd al-Rahim ed., Damascus 1990) ; also uc1.aa0003615705 / AAlexandrina-148752 (Sachau's Leipzig 1867 ed.) ; text on shamela.ws", "lookup_hint": "Alphabetical Arabic headwords; grep in ARB_mo3rb.txt / ARB_abdulraheem.txt (raw, no page breaks); edition of mo3rb not confirmed — check its title page image.", "lo

HJB {"title": "H. Yule & A. C. Burnell, Hobson-Jobson, 2nd ed. by W. Crooke, London 1903 (Delhi reprint 1968)", "edition_found": "1903 Crooke edition (pagination identical to the 1968 reprint)", "kind": "archive_djvu", "url": "https://archive.org/details/hobsonjobsonagl02croogoog", "identifier": "hobsonjobsonagl02croogoog (others: bub_gb_6Z5iAAAAMAAJ, hobsonjobsonglos00yulerich, india.history.resource.89053)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HJB.txt", "page_offset": "leaf = printed + 35..51 (plates inserted; e.g. leaf 83 = p.32, leaf 319 = p.270, leaf 535 = p.4

RCH {"title": "J. Richardson, A Dictionary, Persian, Arabic and English, new ed. by F. Johnson, London 1829 (Lahore reprint 1984)", "edition_found": "1829 Johnson edition (DLI scan, 1814 leaves)", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.24303", "identifier": "in.ernet.dli.2015.24303 (other editions: 1806-10 a-dictionary-persian-arabic-and-english-vol.-i, india.history.resource.17812; 1852 Johnson dictionarypersia00johnuoft)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/RCH.txt", "page_offset": "leaf ~= printed + 93..94 (e.g. leaf 336 =

SIN {"title": "B. Laufer, Sino-Iranica, Chicago 1919 (Field Museum Anthr. Ser. XV.3, pp. 185-630)", "edition_found": "1919", "kind": "archive_djvu", "url": "https://archive.org/details/sinoiranicachine153lauf", "identifier": "sinoiranicachine153lauf (also sinoiranicachin00laufgoog, jstor-29782155)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SIN.txt", "page_offset": "leaf = printed - 172 (e.g. leaf 15 = p.187). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "loo

FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sou

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it
```


### [2026-09-06T15:33:42.224Z] TOOL RESULT

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


## [2026-09-06T15:33:51.209Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN 1966 coffee ===\"; grep -n -i \"coffee\" KLN_1966.txt | head -30\necho \"=== KLN 1971 coffee ===\"; grep -n -i \"^coffee\\|coffee,\" KLN_1971.txt | head -20\necho \"=== KLN caftan ===\"; grep -n -i \"caftan\\|kaftan\" KLN_1966.txt KLN_1971.txt | head -20",
 "description": "Grep Klein for coffee and caftan"
}
```


### [2026-09-06T15:33:51.294Z] TOOL RESULT

```
=== KLN 1966 coffee ===
4968:biggin,  n.,  a  coffee  percolator.  —  So  called  from the  name  of  its  inventor, bight,  n.,  i)  a  bending;  2)  a  loop  in  a  rope;  3)  a bay.  —  ME.,  fr.  OE.  byht,  ‘a  bend’,  rel.  to  MLG. bucht  (whence  G.  Bucht,  Du,  bocht ,  Dan.,  Swed. bught,  ‘bight,  bay') ;  prop,  abstract  nouns  formed fr.  OE.  biigan,  resp.  MLG.  bugen,  ‘to  bend’. See  bow,  ‘to  bend’,  and  cp.  obsol.  E.  bought, ‘a  bend,  turn,  curvature’.
6099:See  cement  and  cp.  words  there  referred  to. Derivatives:  caesur-al,  caesur-ic,  adjs. cafard,  n.,  a  hypocrite.  —  F.,  ‘hypocrite’,  fr. Arab,  kafir ,  ‘infidel’,  part,  of  kafara,  ‘he  blotted out,  covered;  he  denied’,  with  substitution  of the  French  pejorative  suff.  -ard  for  the  unusual ending  -ir.  See  Kaffir  and  -ard. cafardise,  n.,  hypocrisy.  —  F.,  ‘hypocrisy’,  for¬ med  fr.  prec.  word  with  suff.  -ise. cafe,  n.,  i)  coffee;  2)  coffeehouse;  restaurant.  — F.,  fr.  It.  caffi,  fr.  Turk,  qahve ,  fr.  Arab.  qahvah, ‘wine;  coffee’.  See  coffee, cafeteria,  n.,  a  restaurant  at  which  the  patrons serve  themselves  from  the  food  displayed  at  a counter.  —  Mexican  Sp.,  meaning  ‘retail  coffee store’.  Cp.  F.  cafetidre  and  see  prec.  word, caffeine,  caffein,  n.,  an  alkaloid  obtained  from coffee  and  tea  ( chem .)  —  F.  cafeine,  fr.  cafe, ‘coffee’.  See  coffee  and  chem.  suff.  -ine,  resp.  -in. cafila,  n.,  a  convoy  of  travelers,  caravan.  —  Arab. qdfilah,  fem.  used  as  a  collective  noun  fr.  qifil, ‘one  who  returns  from  a  journey’,  part,  of  qa- fala,  ‘he  returned  from  a  journey’, cafiz,  n.,  a  measure  of  capacity.  —  Sp.,  fr.  Arab. qafiz,  a  measure  for  com. caftan,  n.,  a  long-sleeved  garment  worn  in  Tur¬ key,  Egypt,  etc. — T atV.qaftdn,  fr.  Arab,  qaftdn, fr.  Pers.  khaftan.
7261:chasse-cafe,  n.,  a  glass  of  liqueur  taken  after  cof¬ fee.  —  F.,  fr.  chasser,  ‘to  chase,  hunt,  drive, drive  away’,  and  cafe,  ‘coffee’.  See  chase,  ‘to hunt’,  and  cafe.
8116:coffee,  n.  —  It.  caffe,  fr.  Turk,  qahve,  fr.  Arab. qahwah,  ‘wine;  coffee’,  fr.  Kaffa,  Kafa,  a  district in  the  southwestern  part  of  Ethiopia.  Arab. qahwah  orig.  meant  ‘the  plant  or  drink  coming from  Kaffa’.  In  Kaffa  itself  the  coffee  is  called bund  and  the  Arabs  borrowed  this  word  in  the form  bunn,  naming  by  it  the  raw  coffee.  Cp. cafe,  caffeine.
16925:Gymnocladus,  n.,  a  genus  of  plants,  the  Kentucky coffee  tree  (bot.)  —  ModL.,  compounded  of gymno-  and  Gk.  xXaSo?,  ‘branch’.  See  clado-. Gymnoconia,  n.,  a  genus  of  rusts  (bot.)  —  ModL., compounded  of  gymno-  and  Gk.  xovit;,  ‘dust’, which  is  cogn.  with  L.  cinis,  ‘ashes’.  See  cinerary and  cp.  conio-,  conidi-.  For  the  ending  see  suff. -ia.
21071:lampas,  n.,  silk  damask  —  F.,  of  unknown  origin, lampern,  n.,  the  river  lamprey.  —  ME.  lamproun, lampurn,  fr.  OF.  lamprion,  lampreon,  dimin,  of lampreie,  ‘lamprey’.  See  lamprey, lampoon,  n.,  a  virulent  satire.  —  F.  tampon, ‘drinking  song’,  from  the  cry  of  students  in coffeehouses  tampons,  ‘let  us  drink’,  fr.  tamper, ‘to  guzzle',  a  nasalized  form  of  taper,  ‘to  lap’, which  is  of  imitative  origin.  Cp.  lampas,  ‘a  dis¬ ease  in  horses'.  Cp.  also  OE.  lapian,  ‘to  lap’  (see lap).
21988:Lloyd,  masc.  PN.  —  W.  Llwyd,  lit.  ‘gray'. Lloyd’s,  n.,  an  association  of  marine  underwrit¬ ers.  —  So  called  from  Lloyd's  Coffee  Hous^a Tower  St.,  London,  opened  by  Edward  Lioydjn 1688.
24119:Mocha,  n.,  a  fine  variety  of  coffee.  —  Fr.  Mocha, name  of  a  port  on  the  Red  Sea  (in  Arabia), mock,  tr.  and  intr.  v.  —  ME.  mokken,  fr.  MF. (=  F.)  moquer,  fr.  OF.,  ‘to  mock’,  which  is prob.  of  imitative  origin.  Cp.  OProvenp.  mocar, ‘to  mock’,  Sp.  mueca,  ‘grimace,  grin’. Derivatives:  mock,  n.  and  adj.,  mock-er,  n., mockery  (q.v.),  mock-ing-ly,  adv.
29867:pousse-cafe,  n.,  a  glass  of  liqueur  taken  after cofTee.  —  F.,  lit. ‘chaser  of  coffee’,  fr.  pousser,  ‘to push’  (fr.  L.  pulsate,  ‘to  beat,  strike’)  and  cafe, ‘coffee".  See  push  and  cafe  and  cp.  next  word, poussette,  n.,  a  dancing  round  of  couples  with hands  joined.  —  F.,  ‘the  game  of  pushpin’,  fr.
=== KLN 1971 coffee ===
36737:‘wine; coffee’. See coffee, 
36743:coffee and tea {chem.) — F. cafeine, fr. cafe. 
50226:coffee, n. — It. caffi, fr. Turk, qahve, fr. Arab. 
107709:coffee tree {bot.) — ModL., compounded of 
133490:coffeehouses tampons, ‘let us drink’, fr. lamper , 
188930:coffee. — F., lit. ‘chaser of coffee’, fr. pousser, ‘to 
=== KLN caftan ===
KLN_1971.txt:36763:caftan, n., a long-sleeved garment worn in Tur- 
KLN_1971.txt:130276:kaftan, n. — A var. of caftan, 
KLN_1966.txt:6099:See  cement  and  cp.  words  there  referred  to. Derivatives:  caesur-al,  caesur-ic,  adjs. cafard,  n.,  a  hypocrite.  —  F.,  ‘hypocrite’,  fr. Arab,  kafir ,  ‘infidel’,  part,  of  kafara,  ‘he  blotted out,  covered;  he  denied’,  with  substitution  of the  French  pejorative  suff.  -ard  for  the  unusual ending  -ir.  See  Kaffir  and  -ard. cafardise,  n.,  hypocrisy.  —  F.,  ‘hypocrisy’,  for¬ med  fr.  prec.  word  with  suff.  -ise. cafe,  n.,  i)  coffee;  2)  coffeehouse;  restaurant.  — F.,  fr.  It.  caffi,  fr.  Turk,  qahve ,  fr.  Arab.  qahvah, ‘wine;  coffee’.  See  coffee, cafeteria,  n.,  a  restaurant  at  which  the  patrons serve  themselves  from  the  food  displayed  at  a counter.  —  Mexican  Sp.,  meaning  ‘retail  coffee store’.  Cp.  F.  cafetidre  and  see  prec.  word, caffeine,  caffein,  n.,  an  alkaloid  obtained  from coffee  and  tea  ( chem .)  —  F.  cafeine,  fr.  cafe, ‘coffee’.  See  coffee  and  chem.  suff.  -ine,  resp.  -in. cafila,  n.,  a  convoy  of  travelers,  caravan.  —  Arab. qdfilah,  fem.  used  as  a  collective  noun  fr.  qifil, ‘one  who  returns  from  a  journey’,  part,  of  qa- fala,  ‘he  returned  from  a  journey’, cafiz,  n.,  a  measure  of  capacity.  —  Sp.,  fr.  Arab. qafiz,  a  measure  for  com. caftan,  n.,  a  long-sleeved  garment  worn  in  Tur¬ key,  Egypt,  etc. — T atV.qaftdn,  fr.  Arab,  qaftdn, fr.  Pers.  khaftan.
KLN_1966.txt:20522:Kaffir,  Kafir,  n. ,  1)  a  non-Mohammedan ;  2)  a  mem¬ ber  of  the  most  intelligent  group  of  S.  African Bantu  races.  —  Fr.  Arab,  kdfir,  ‘infidel’,  prop, part,  of  kafara,  ‘he  blotted  out,  covered,  hid ;  he denied’.  See  Yom  Kippur  and  cp.  cafard. Derivative:  Kaffir,  Kafir,  adj. kaftan,  n.  —  A  var.  of  caftan, kagu,  n.,  a  crested  bird  peculiar  to  Caledonia.  — Native  name.
```


## [2026-09-06T15:33:52.830Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== IEC kaukis ===\"; grep -n -i \"kaukis\\|kaukalon\\|kawšik\\|kawsik\" IEC.txt | head -20\necho \"=== PHD kafs ===\"; grep -n -i \"kafš\\|kafs\\b\" PHD.txt PHD_mackenzie.txt | head -20\necho \"=== NYB ===\"; grep -n -i \"kafš\\|kafs\" NYB_vol2_glossary.txt | head -20",
 "description": "Grep IEC, PHD, NYB"
}
```


### [2026-09-06T15:33:52.905Z] TOOL RESULT

```
=== IEC kaukis ===
6876:kaukos (1) ‘shriek, howl, clamour, call", Variant: kāuk- as separate entry, cf. also kauko above. Cf. WP I, 331, 371 & 466. Extn. mng. ‘howler’, etc. Skt. kókah "wolt" beside (variant) kau$ikah ‘owl’; Ir. cuach ‘cuckoo’; Blg. kuk, id. beside kuče ‘dog’; OCS cf. kuctka ‘bitch’; Li. kaükas (‘goblin, mandrake, thunderbolt’ in folklore); kaukýs ʻa raucous bird'; kiáuke ‘jackdaw’; Latv. kaukis (‘bawler; blackcap’ ornith.); cf. (variant) Slovene čuk ‘owl’. (Isophonic: LLat. caucus ‘concubine’ and Alb. kakë- in kakë- zozë ‘salamander’: Latv kaukis, kaukis (2), m. ‘toad’. The Alb. form suggests a prototype *kauko-dieudio)
6902:kaukos, is, à (kauk-) “a raucous bird’. WP I, 33] Skt. kókah (2) ‘red goose, cuckoo’; Hind. koki ‘crow’; Sind. kok, m. ‘cuckoo; frog’; Per. kabg ‘partridge’; Tokh. A cf. kokafi “an un- identified bird”; Gk. kéux, gs kéukos “a gull’ beside kábéx, kaúēx, id.; Sard. coca ‘goose’ beside Sard. (Campid.) coga (^witch', cf. mngs. of Lat. strix); Ir. cuach ‘cuckoo’; W cawci (jackdaw': Hind. koki); Cz. kavka, Pol. kawka “daw”; Srb. cf. (variant) Cavka, id.; Li. kaukys, m. “a shrill bird’; kiauke ‘daw’; Latv. kaukis *blackcap gull'. (A similar onomat. element is present in Hind. kauwa ‘crow, daw? and in Fr. cahouette, id.)
7113:keukó ‘curl up, cower; curl; lurking, hud- dled’. Cf. WP I, 372 Skt. cf. čokam (name of a root); čočam *cinna- mon-bark’; cf. kočāmi, o-gde (2) ‘bend, curve’; Alb. çuk, v. ‘lurk’; cyc, adj. ‘huddled, crouch- ing’; MIr. & Ir. cuach ‘lock, curl’; cuachaim ‘curl, roll up, cuddle’; OHG. cf. hiuhma (crowd?, lit. "buddlet Srb. Cučati, Slovak čučať, Cz. & Slovene Cuceti, Blg. čuča ‘squat, crouch’; Blg. cf. tücka “pile of earth’; R cf. čùčelo ‘stuffed animal, scarecrow’, Li. kiáu- klas ‘snail shell’; Latv. kaukis (‘toad; arctic puffiw’. Semantics of E lurk, v. & G Lurch “toad'). Cf. also Ir. cuachán ‘bundle’
7119:keuks- (3) ‘howl, screech’ | Cz. (ambig.) čišet ‘howl, of wind”; Li. kiauksiu, kiaukSiu, eti ‘howl, screech’; Latv. Caukstu, -stét, inchoat. ‘chatter’ beside kaukis “reed- warbler’. (The isophone in Slovak čušat "be silent is a riming parallel to type teuks-, q. v. Skt. éoksah, Cauksah “clean, pure? is without parallel)
=== PHD kafs ===
PHD.txt:422:kabk [АрА! | N ~] partridge. ~-anjir [acyl | N ~] a kind of francolin. kabód [kpwt! | N ~] grey-blue; pigeon. kabótar [kpwil | M kbwtr, N ~] pigeon. kāč [с | N kāš(ki)], ~ ka: would that, if only. кадар [01А] game, joke. кадар [ktk' | M kdg, N kada] house. ~-banig [-b'mwk! | N Radbanü] mistress, lady of the house. ~ig [-yk'] domestic; servant. ~-xwaday [-hwty | P gdyxwd?y, N kadxudā] householder, master of the house. kadām [ktm | M kd?m, N кийат) which, what. c--iz-é(w) [-c-H D] whichever. kadar [kt] who, which. 7-iz-é(w) [-c-H D] whoever. kaf [kp | N —] foam, slime. kaf-, v. kaftan. kafč [kpc | N ~] ladle, skimmer. ~ag [-А! | N ~a] spoon. kafš, ~ag [kps, -k! | N Аар] shoe. ~gar [-k/ | N ~] shoemaker. kaftan, kaf- [kp-in' | P kft, kf-] fall. kah [TBNA < A tbr | N ~] chaff, straw. kān-, ~i§n, v, kāstan. _ kahas [kts | М khs] channel, sewer. kāhēnīdan, káhén- [R'hyn-ytn!] decrease, lessen (tr.). kühidan [P hytn! | N ~] = kastan. kahist [ksst'] least. kah-rubāy [Ара | N —rubá] amber. kahwan [khwbn' | M qhwn, N kukan] old. kākom [RP Rkwm | N ~] stoat. ~ i spéd: ermine. kālbod [Аро | (M k*/byd), N ~] body, shape, form. ~ӧтапа [-wmnd] corporeal. kam [km | M kmb, N ~] little, small, few; v. kem. kam [Em | = M, N ~j will, desire, purpose. kàm-, v. kāmistan. 1катаб [k?mk! | N kama] kinds of gruel, or soup. ?kümag [k?*mk! | N kama] = kam. «-hanjām [-hnc’m] gaining one’s end, successful. -~-hanjamih: success. „ūmand [-wmnd] willing(ly), desirous. ~-widar [-wt?l | N kām-gučār] successful, independent. ~-xwaday [-Awt^y] independent, absolute. kamal [kml | (M km?7)] head (daevic). ~ig [-yR!] chief (daevic).
PHD.txt:3634:shoe kafš, még, mozag.
PHD.txt:4978:kafé kafčag kafš kafšag kafšgar kaftan kaš, kiš keš- kešīdan kišnīz kasawag kašk kaStig kadar
PHD_mackenzie.txt:3140:kafs, ~a~ [kpf, _k' I N kafS] shoe.
PHD_mackenzie.txt:7556:separate (y.) wextan, wisandan,           shoe kafs, mog, mozag.
=== NYB ===
```


## [2026-09-06T15:34:01.071Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== IEC leaf 829 ===\"; awk 'BEGIN{RS=\"\\f\"} NR==830' IEC.txt | head -80",
 "description": "Print IEC leaf near p.1628"
}
```


## [2026-09-06T15:34:02.823Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON qahveh ===\"; grep -n \"قهوه\" MON_part1.txt MON_part2.txt | head -5\necho \"=== MON kafsh ===\"; grep -c \"کفش\" MON_part1.txt MON_part2.txt\necho \"=== BQT khaftan v2 ===\"; grep -n \"خفتان\" BQT_v2_pages.txt | head -10\necho \"=== BQT khafdan ===\"; grep -n \"خفدان\" BQT_v1_pages.txt BQT_v2_pages.txt | head -10",
 "description": "Grep MON and BQT Persian headwords"
}
```


### [2026-09-06T15:34:03.477Z] TOOL RESULT

```
=== IEC leaf 829 ===
à, us ‘wind, air, draught’. WP I, 220. Cf. ueio (uemi) Skt. vayüh, m. id.; Av. (short vowel) vayus, vayo, m., vayu, n. id.; Oss. cf. wájág, adj. ‘swift’; Tokh. A (?) wiyu, adj. (queried: 'sur- prised’? *flattered?); G Wehe, f. “drift of sand or snow’; ON vé, npl. ‘standard’; Pol. wieja, f. “breeze; snowdrift; Cz. cf. zá-v&je, f. 'snow- drift; Li. v&jas, m. ‘wind’; Latv. vējš, m. id.
uek-, see uek- (2)
(uék-, see Supt: U)
ueks- “bend, turn” Mir feccaim, v. intr. ‘turn, bend; apply one- self; Ir. feacaim, tr. bend’; intr. ‘shrink’); Lat. cf. con-, in-vexus (lit. ‘turned up, — down"); MHG wéhsel, OHG & OS wéhsal, OFris. wixle, s. ‘change’. (Isophonic (?) in Gk. ixús, gs: -úos. f. ‘loins’: Alb. veshje, f. id.)
uektis, å “thing, matter, affair, deed, turn. WP I, 246. Cf. ueks- (?) Gaul. vectis, s. ‘quarrel, fight’; Olr. fecht, mn. ‘time, occasion’; Ir. feacht, f. ‘time, turn; county; grave’ (!); MBr. gwez, Br. gwéas, pl. gweašu, f. ‘time, occasion’; Cor. gwyth, pl.
1507
-yow, m. ‘time, occasion, act, work’; W gwaith, pl. gweithiau, m. id.; Go. waíhts, f. ‘thing’; OHG wiht, n. ‘being, thing’; OS wiht, f. i-st. id. (pl: ‘demons’); OHG wiht, fn. as OHG; ON vættr, pl. vættir, f. ‘being, creature’ beside vætr, id.; vætt-, cpds. “fighting-?; OCS vesti, f. ‘thing, nature’; Cz. věc, f. ‘thing’ (but veta, f. id. (veta za vetu 'tit-for-tat'): Pol. wet, said to be a Gmc. LW, fr. wette)
uek- (1) (ueK-mi) ‘wish, beg, demand’. WP I, 244 Skt. vá$mi, v. id.; Av. vasomi, v. id.; cf. vaso, obl: vasáh-, n. ‘wil’ beside vasno, m. ‘wish’; Ober cf. vašna, f. “favour”; Hitt. wekmi “beg”; Gk. cf. hekón, act. pt. ‘willing’; a-ékon "un. willing’; a-éketi “against one's will
uéK- (2) “sight, seeing, seemly, comely’. It. feic, m. “sight, view, vision’; feicim, v. ‘see’; MHG wéhen, sv. 5. (1) ‘shine’; cf. OHG wāhi, MHG wæhe, adj. “bright, beautiful
ueks- ‘grow, thrive’. (ueks-?). Cf. aue-, eks-, uåks- and aueks-. Apparently a cpd. of pre- fixes. Cf. WP I, 23 and see next OPer. vaxi-, v. ‘grow’; Gk. aéxo, v. ‘make grow’; Li. vešiù, éti, v. “luxuriate, thrive’
uekslis, os ‘thriving’. Cf. ueks- (uàks-, aueks-) Alb. veshél, adj. ‘fertile’; Li. veslüs, adj. “thriv- ing, luxuriant ; veSus id.; Latv. (ambig.) vesels, adj. “healthy”
ueKsueros, uesKueros, à ‘evening, west’. WP I, 311 Per. xavar, s. ‘west’; Tokh. kastwer, B kástwer, s. ‘night’; Arm. gäer, o, ov & i, av, s. id; Gk. hésperos, m. “evening star’; hespéra, f. ‘evening, west’; Gk. dial. wespáros, Locr. wes- parion, adj. & n. ‘evening’; Lat. vesper, gs: vesperis, m. “evening, west’; vesper, a, um, adj. id. beside vespera, f. ‘evening’; Olr. fescer, fescor, Ir. feascar, m. id.; W ucher, pl. -au, m. id.; Cor. cf. gorth-ewer, m. id. (fr. *urt-^); OCS and còm. Sl. vecerü, m. ‘evening’; vicera ‘yesterday’; Li. cf. vakaras ‘evening’ beside vakar, adv. *yesterday'; Latv. vakars, m. *even- ing' (phonol. obscure). Extns. in Gk. hespé- rios, adj. "evening": OCS večerja, f. ‘supper’; Cz. večeře, id.; Li. cf. vakáris, f: -e, adj. *even- ing”; (type *-inos, -inios in) Gk. hesperinós,
uek- — uel-
20
25
30
33
40
45
1508
id.; OLat. vesperna, f. ‘supper’; OCS vecerínü & Ant. adj. ‘evening’; Li. vakarinis, id.
(ueKtis, see (1) ueghtis, and (2) uektis)
uel- (1) *wish, will, command'. Cf. ual- (2), and uol- (4). WP I, 294 Skt. varami, pp: vrtah, v. ‘choose’ beside (o- gde) varáyami, v. ‘choose; woo’; várah, adj. ‘elite’; m. ‘choice’; váryah ‘eligible’; Av. var-, v. (3) ‘wish’; varo, adj.
```


### [2026-09-06T15:34:03.584Z] TOOL RESULT

```
=== MON qahveh ===
MON_part1.txt:1273:خادمی که مأمور تهیهٌ چای و قهوه و قلبان 
MON_part1.txt:1283:چای و قهوه و قلیان و شربت (اطاق یا 
MON_part1.txt:3200:تیر ۵ رنگ» سباه با قهوه‌یی» درخشان که در 
MON_part1.txt:8546:رنگ زرد؛ نار نجی» قرمزء قهوه‌ای در آمده 
MON_part1.txt:8554:اخرا. (نق.) قهوه‌ای مایل به قرمز از گروه 
=== MON kafsh ===
MON_part1.txt:73
MON_part2.txt:83
=== BQT khaftan v2 ===
12810:‫خفتان د نوعی از جیبه و جامة روز‬                     ‫راگوبند که بجپت | تشگیره مپباکرده باشند‪٩‬‏ ‪۰‬‬
12824:                        ‫که کژین خفتان وگه زرین جوشن ‪.‬‬
12877: ‫ع ‪ ,‬خفتان « حفتادی ‪۳۱۳٩‬‏ و نز «فقطان» واز| نسا‬                     ‫خفدان (ہ‪.‬م‪ ).‬در و‬                   ‫‏‪= _ ١‬‬
12926:                              ‫عط‬‫باشد ‪-‬‬                    ‫خفتان است که سلاح جامه باشد که درروزجنگه‬
12942:               ‫خفج ‪۰‬‬   ‫رك‪:‬‬   ‫_‬   ‫©‬           ‫رك‪ :‬خفته ‪.‬‬      ‫‪۴‬‬           ‫خفتان (ھ‪.‬م‪).‬‬    ‫صه‬    ‫‪۴‬‬
31696: ‫سازواری‪= ۱‬بروزن ومعنی‌ساز گاری‬                          ‫وخفتان و زره وچارآینه و مانند آن هم‬            ‫ِ‬‫از‬
=== BQT khafdan ===
BQT_v2_pages.txt:12877: ‫ع ‪ ,‬خفتان « حفتادی ‪۳۱۳٩‬‏ و نز «فقطان» واز| نسا‬                     ‫خفدان (ہ‪.‬م‪ ).‬در و‬                   ‫‏‪= _ ١‬‬
BQT_v2_pages.txt:12923:‫خف‪ "4‬ب=فتح اول و انی » فشردن کلو‬                          ‫خفدان ‪ ۴‬د بادال ابجد‪ .‬بروزن ومعنی‬
```


## [2026-09-06T15:34:10.800Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor n in 890 891 892; do echo \"=== leaf $n ===\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N' IEC.txt | grep -n \"^1[0-9][0-9][0-9]$\\|kauk\\|kav\" | head -20; done",
 "description": "Locate IEC p.1628"
}
```


### [2026-09-06T15:34:12.615Z] TOOL RESULT

```
=== leaf 890 ===
=== leaf 891 ===
=== leaf 892 ===
```


## [2026-09-06T15:34:12.809Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR>=12700 && NR<=12900 && /\\[pdf page/' BQT_v2_pages.txt | tail -5\necho \"---\"\ngrep -n \"\\[pdf page\" BQT_v2_pages.txt | awk -F: '$1>12700 && $1<12950' | head\necho \"--- context around 12877 ---\"\nsed -n '12860,12890p' BQT_v2_pages.txt",
 "description": "Find BQT page tag for khaftan"
}
```


### [2026-09-06T15:34:15.077Z] TOOL RESULT

```
---
--- context around 12877 ---
                                                                                                   ‫ام کن هم جنگ‬
                                                            ‫به‌عنی‬      ‫گفته ‪» :‬‬   ‫ورن‬       ‫اول بر‬    ‫تم‬        ‫؟‬    ‫حفته‬

‫گورانی در خواب‬              ‫کی‬
                             ‫بمعتی خفج است که مد‬             ‫و خمیده را نز‬                   ‫شمده‬
                                                                                                ‫خواییده باشد ‪ - ۵‬و خ‬
‫انند در‬
      ‫رو‬‫باشد ‪ -‬ودر عربی لرزیدن پای شتر گ‬
                                            ‫برخاستن‬   ‫وفت‬
                                                             ‫گویند ‪ -‬وبمعنی چاليك هم هت » وآن‌بازیی‬
                                                            ‫یکی‬         ‫ات‬    ‫باشد که کورکان کنند ‪ ¢‬وآن دوجوب‬

‫وژن‬         ‫خفجاق ف با جیم فارسی بر‬                              ‫بمقدارسه وجب ودیگری بقدر(‪ )4‬باك قبضه وهر‬
‫وترکان ص حرا نشين باشد‪.‬‬          ‫» مر دم اسل‬       ‫جدماق‬                      ‫دو سرچوب کوچك تيز میباشد ‪.‬‬

  ‫‪ -:‬که‪.‬‬        ‫)س( چكث‪ .‬چت‬                                                        ‫)( چك » چش‪۳ :‬‬
       ‫(‪ )3‬چكث‪ .‬چش‪«. :‬ورند‬                   ‫(‪ )6‬چك»چش‪ :‬است‬                  ‫(‪ )4‬چك » چش‪ :‬بمقدار ‪.‬‬
 ‫ع ‪ ,‬خفتان « حفتادی ‪۳۱۳٩‬‏ و نز «فقطان» واز| نسا‬                     ‫خفدان (ہ‪.‬م‪ ).‬در و‬                   ‫‏‪= _ ١‬‬
  ‫وارد زبان فرانسه شده ‪ 031126‬و ‪٩383C‬‏ ( جامة تر کی هزین » با آستر پوستن ) ‪ .‬رك ‪:‬‬
  ‫‪ - ۴‬اکنون « بختال" ( بفتح اول وسوم) گوبند ‪ .‬رك ‪ :‬خفتو ‪.‬‬                                     ‫‪۲٩‬‏ ‪۰‬‬            ‫‪:-‬س‬
                                                                                                                 ‫و ‪۳‬‬
                                                                                                                   ‫ساب‬
                                   ‫‪ - ۳‬اسم ءفعول ازخفتن («‪.‬م‪. ).‬‬                         ‫‪.‬‬        ‫فلت‪:‬ك‬
                                                                                                      ‫خ و‬
                                                                                                        ‫‪۴‬‬
            ‫برده به‪.‬‬    ‫گفتم این فتنه است خواش‬                            ‫طالمی را خفته ديدم نممروز‬                    ‫۔‬       ‫‏‪e‬‬

  ‫‪.‬‬     ‫» ‪ 5‬تان ‪۰۳‬‬

                                                        ‫_ز ‪ :‬خفت ‪ ۲‬بدن(ب‌وند مصدری) ‪.‬‬
                                                                                    ‫ا‬
```


## [2026-09-06T15:34:22.680Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"IEC leaves:\"; awk 'BEGIN{RS=\"\\f\"} END{print NR}' IEC.txt\necho \"--- find page 1628 marker ---\"; grep -n \"^1628$\\|^1627$\\|^1629$\" IEC.txt | head",
 "description": "Count IEC leaves and find page 1628"
}
```


## [2026-09-06T15:34:24.414Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"pdf page\" BQT_v2_pages.txt | head -3\necho \"---\"\nawk 'NR<=12877 && /pdf page/ {last=$0; ln=NR} END{print ln\": \"last}' BQT_v2_pages.txt",
 "description": "Find pdf page tag preceding khaftan"
}
```


### [2026-09-06T15:34:24.948Z] TOOL RESULT

```
IEC leaves:
858
--- find page 1628 marker ---
```


### [2026-09-06T15:34:26.894Z] TOOL RESULT

```
---
:
```


## [2026-09-06T15:34:31.386Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== IEC last leaf ===\"; awk 'BEGIN{RS=\"\\f\"} NR==858' IEC.txt | tail -20\necho; echo \"=== IEC leaf 857 head ===\"; awk 'BEGIN{RS=\"\\f\"} NR==857' IEC.txt | head -5",
 "description": "Check IEC coverage end"
}
```


## [2026-09-06T15:34:33.013Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nhead -3 BQT_v2_pages.txt; echo \"...\"; grep -c $'\\f' BQT_v2_pages.txt; grep -n \"^\\[\" BQT_v2_pages.txt | head -5\necho \"=== total lines ===\"; wc -l BQT_v2_pages.txt",
 "description": "Inspect BQT_v2_pages structure"
}
```


### [2026-09-06T15:34:33.689Z] TOOL RESULT

```
=== IEC last leaf ===
(1) only in Skt. ürnómi, v. ‘envelop’; (2) only in Gmc. cf. Go. wulan and OE wylian 'seethe? beside wyllan, v. id. (fr. *ulnio)
ulquátis, os *tearer, devourer, killer’. Cf. ul- quos (1) Skt. vrkátih, m. ‘robber, murderer’; Slovene volkác ‘Alsatian dog’; Li. vilkátas, m. *wer- wolf; Late vilkatis, vilkacs, id.
ulquio ‘she-wolf’. Cf. ulquos (1) Skt. vrkih, id.; OE welt id. MHG (Upper Ger) wülpe, id.; ON ylgr, ds: ylgi, id.; Li. vilke, id.
ulquó, ið (ambiguous consonantism, unless related to type ulquos, etc. see next). Skt. varke, mp. ((seize', but cf. type *uelk-) beside vrkah (2) '(plough'; Srb. vučem, v. ‘drag’; cf. OCS (hapax) vlüci, s. (Ccaltrop? or sim.); Li. vilkiu, eti, v. ‘wear — a garment’; cf. vilktas, m. (tech. *priming); L

=== IEC leaf 857 head ===
bulga is ambig. Skt. várgā ‘sect, class’ seems to be unrelated)
(ulio (1) ‘wind, wrap’, see uluið; (2) ‘boil’, see ulāið)
ulksuos, à (ul'suos, à) (?) ‘sorcerer, prophet Gk. cf. (?) álsos, n. ‘sacred grove’; ON cf. volva ‘prophetess’; OCS vlüxvü, m. ‘prophet’; vlüxvij, adj. *magical'; Blg. vláxva, m. *high- wayman'; LW in Finn. velho ('sorcerer', vocal- ism of Finn. verho “top”, cf. urks- (4))
ulm- ‘surge, billow; wide mouth, gulf’. WP I, 298. Gk. ambig. & uncertain Skt. ürmíb, mf. ‘wave, billow’; Gk. cf. lámos, m. ‘gulf; lámia, f. ‘monster, wide-mouthed fish’; cf. lamurós ‘deep, awful; riotous’; Arm. cf. aymuk, gs: aymki, ab. s. aymkav, s. *up- roar’; OE wylm, m. ‘surge, billow, boiling’; G (7) Wolm, m. ‘archway, porch, curved ba- nister’; ON olmr, adj. ‘wild, boisterous’. (Iso- phone: Li. vilminti, inf. ‘cheat’)
uln- (1) (ulna, ulon-) ‘wool’. WP I, 206. (Var- iant initial in Oss.) Skt. urna, f. id.; Av. cf. una, f. “lock, curl’; Oss. cf. qun, Dig. gun, s. ‘wool, hair’; Hitt. cf. hulana-, Luvian hulani- (queried: *wool"); Lat. lana, f. id.; Ir. olann, gs: olna & olla, f. id.; W gwlan, OBr. gulan, Breton gloan, m. id.; OHG wolla, f. id.; Go. wulla, f. id.; OE wull, wll f. id.; ON ull, ds: ullu, f. id.; OCS vlüna, Cz. vina, Pol. wełna, Big. vlána, id.; Li. vilna, Latv. vilna, id.
```


### [2026-09-06T15:34:36.140Z] TOOL RESULT

```
                                         ‫‪7‬‬

                          ‫رن‪۳‬‬
...
680
=== total lines ===
41070 BQT_v2_pages.txt
```


## [2026-09-06T15:34:57.955Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN kafsch ===\"; grep -n -i \"kafš\\|kafsch\\|kaf§\\|kafs\" HRN.txt | head -20\necho \"=== HUB ===\"; grep -n -i \"kafš\\|kafsch\\|kafs\" HUB.txt | head -20\necho \"=== SYN shoe ===\"; grep -n -i \"košik\\|koshik\\|kawšik\\|kaukis\" SYN.txt | head -20",
 "description": "Grep Horn, Hübschmann, Buck"
}
```


### [2026-09-06T15:34:58.026Z] TOOL RESULT

```
=== HRN kafsch ===
=== HUB ===
6605:'Schuh', np. kafsy bal. LW. kaus *Schuh'; ausarak (osarak)
=== SYN shoe ===
```


## [2026-09-06T15:34:59.352Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PLA kaftan ===\"; grep -n -i \"haftan\\|kaftan\\|qaftan\\|ftan\" incoming/PLA/PLA_pages.txt | head -20\necho \"=== PLA qahwa ===\"; grep -n -i \"qahwa\\|kafs\" incoming/PLA/PLA_pages.txt | head -20",
 "description": "Grep Asbaghi PLA"
}
```


### [2026-09-06T15:34:59.414Z] TOOL RESULT

```
=== PLA kaftan ===
2476:aus -           bäfta:             "eine           Stoffart",            pass.        pt.    v.    Verb    .»L         baftan   T   mp      ars!
2477:       väftan ®, tk. bäfta ° s. bafta.
3272:Gr - bäffchen:                   "eine       Art     Leinwand"            aus     dem    pers.        „ol     bäftan           7,
4023:       täftan         Taw.            tap "brennen,                 scheinen"               5.
4039:       des       Wortes         abi       täfta       mp.           Mer        täftan           aw.         tap       >>nlat.        taffeta
4182:       "Sitz"                 s.       taht        +    pers.           rawän       act.    pt.       v.    Verb     ans, raftan          "gehen"    mit
6446:       Kaftan:            "aus        dem        Orient            stammendes              Obergewand,            früher     Tracht    der
6450:ol,.>- hafdän = haftan s. haftän ’.
6453:       SYomw        xuftanaor                    xuffa.
7185:os -       dalq:        "Anzug           der       Armen"           aus     dem    pers.       (3, dalq     5, dtsch.         Dalk:     "Kaftan
7227:          ‚fsgir mp.                      Is gir v. Verb                 griftan.
7837:         Verb        raftan          "gehen".
8657:           sag                 ap.    saka       7 +       gir v.         Verb     griftan       "nehmen,      greifen",        syr.‘20     8
9360:        !s»          sumb      v.       Verb        ua.       softan       "bohren"         5,
12267:gisä°                                                                               219                                                   gaftan
12321:Olbi _ quftän = gaftan a. v. !.
12499:         "Krieg"          + Pers,              rawan          act.            Pt.    v.        „,   raftan       "gehen"    mit   der    Bed.
13070:Aa) - kufta:                     "Fleischbällchen,                             Kloß"          pers.     Ci                küftan    "schlagen,
13071:           klopfen,              hacken"               Kg mp.Naı9 koftan,                      kob     ®,
14898:        „ub, briät aus briftan                             "rösten".
=== PLA qahwa ===
5151:kafsin                                                                 88                                                     Zulbän
5154:rer - Kafsin = dabsin                             s.    Zabsin.
12286:Gw8- gaff:                 "Schuhe" <                    pers.     ul kafs > CT MP vos kafs 6,
```


## [2026-09-06T15:35:06.925Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['PLA','IEC','MON','BQT','AHD']:\n    print(k, d[k].get('page_offset'))\n    print('  hint:', d[k].get('lookup_hint'))\n    print()\n\"",
 "description": "Get page offsets"
}
```


## [2026-09-06T15:35:08.347Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PLA around 6440 ===\"; sed -n '6435,6470p' incoming/PLA/PLA_pages.txt\necho \"=== PLA around 12280 ===\"; sed -n '12280,12330p' incoming/PLA/PLA_pages.txt",
 "description": "Read PLA context"
}
```


### [2026-09-06T15:35:08.903Z] TOOL RESULT

```
PLA 301 leaves (pdftotext -layout, \f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276).
  hint: HathiTrust search-only; Google Books id q_ErAAAAMAAJ snippet view; DDB has only the table of contents. No full text online. | For pages in a scanned volume use: python3 tools/ref_page.py PLA:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)

IEC TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
  hint: Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.

MON None
  hint: Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks).

BQT vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').
  hint: grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)

AHD 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.
  hint: Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves = original 1969 ed.).
```


### [2026-09-06T15:35:08.949Z] TOOL RESULT

```
=== PLA around 6440 ===
                                                                                  Tekaf& 3". 7

ls - hafäf:                Pl.        v.          af s. baf.
                                                 [dee



ol     - baffaf:              "Schuster"                    pers.           a nom.       agent.      v.    baf.


obs     -    baftän:             "gesteppter                      Panzer,          wattiertes            Obergewand"         pers.    5,
       Kaftan:            "aus        dem        Orient            stammendes              Obergewand,            früher     Tracht    der
       orthodoxen               Juden            in Rußland                  u.    Polen"         pers.          ar.    > tk.> poln.              6,


ol,.>- hafdän = haftan s. haftän ’.

ai      -    haftag:             "Alpdrücken"                      arabisierte              Form     v.    pers.     ass hofte        ec      mp.
       SYomw        xuftanaor                    xuffa.


.)r -       bullär:             ein        Ort        in        Fars,       wo    es    guten     Honig     gibt       ”.


Jlöle - halpäl:                  eine        Stadt               in Aserbaidschan                  10,

_\5>- bullar:              "Hülsenfrucht,                          Bohne"          pers,       11,


zus -       balang:           Pl.      v-zaäs balang                        Ss. balanf         12,




1.    FM.    s.     v.
2.    Mackenzie            s.     v.
=== PLA around 12280 ===

obs           - gaftän:               "Überrock"            pers.                   ol       haftän         "Unterpanzer"         3,


olsas - gafdän:                       "Büchsen            für Drogen"                    pers.     4,

Gw8- gaff:                 "Schuhe" <                    pers.     ul kafs > CT MP vos kafs 6,

HS - gafdalll:                                "Schöpfinstrument"                                 pers.        Anh kafde-rIz            7 mp.
                                       [6:}
              sag kafiz                       ‚kafldak       ’,        u        riz       (Abkürzung         für    rizande)      act.        Pt.    v.
          rihtan           "gießen,                einschenken",                    np. da kafgir.


08 -          gafas:        "Käfig"                      pers.    zu karaf 10                     kabast     11, wahrscheinlich                aus
          pers.        uf             kafbast            pers.               „Skaf         "Handfläche"            + „_. bast     pass.        pt.     v.
          bastan           "binden"                mp.           wg»,        bastan          am.           / ap.    band    12,   syr.        0%      13,
          mand. KBS, hebr. sp”.

olks - gaftän                     = gaftän               gq. v.    15,



1.    Kent        S._ 186.
2.    al-Mu°arrab                     s.      v.,    sabk        $enäsI             S.    254,     Ta’alibi        fiqh    al-luga       S.    198.
3.    Littmann              S.        95.
4.    al-Mu°arrab                     s.      v.,    Muhit        s.       v.
5, Muhit              s.    v.,        al-Mu’arrab                s.       v.
6.    Mackenzie                 S.     v.
7.    al-MuCarrab                     s.      v.,    Muhit        s.       v.
8. Farawa$i                 s. v.
9.    Mackenzie                 Ss.    v.
10.       BQ.     s.       v.
11.       al-Mu’arrab                  s.      v.,       Muhlt     s.        v.
12.       Nyberg           Bd.        II      s,    v,
13.       Brockelmann                  s.      v.
14.       Macuch           s.    v.
15.       Chista           Bd.        10      S.    1189,
quftän                                                           220                                            galyün


Olbi _ quftän = gaftan a. v. !.

Js - qufl:              "Schluß" < pers. JL, küpal ®, syr.                              Lw. Das      3,


5% - gafür = gäfür q. v.
Js - gafül: Pl. v. yes qufl.

nis -          gafiz:        "ein      Maß",     vielleicht        aus       pers.   »kaf      "Handfläche",        aram.
                >04
```


## [2026-09-06T15:35:24.609Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\np='incoming/PLA/PLA_pages.txt'\ntxt=open(p,encoding='utf-8',errors='replace').read()\nlines=txt.split('\\n')\n# map line number -> leaf\nleaf=1\nlineleaf=[]\nfor i,l in enumerate(lines,1):\n    lineleaf.append(leaf)\n    leaf += l.count('\\f')\nfor target in [6446,6450,6453,12286,12321,2476]:\n    lf=lineleaf[target-1]\n    print(target,'leaf',lf,'printed page',lf-15)\nEOF",
 "description": "Map PLA line numbers to printed pages"
}
```


### [2026-09-06T15:35:26.464Z] TOOL RESULT

```
6446 leaf 126 printed page 111
6450 leaf 126 printed page 111
6453 leaf 126 printed page 111
12286 leaf 234 printed page 219
12321 leaf 235 printed page 220
2476 leaf 53 printed page 38
```


## [2026-09-06T15:35:36.294Z] TOOL CALL #22: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-06T15:35:36.301Z] TOOL RESULT

```


```


## [2026-09-06T15:35:37.135Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PLA leaf 26 (p.11) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==26' incoming/PLA/PLA_pages.txt | head -60",
 "description": "Read PLA page 11"
}
```


### [2026-09-06T15:35:39.069Z] TOOL RESULT

```
=== PLA leaf 26 (p.11) ===
° armanistän                                                                                     11                                                                       äAriyya

 ob. ı_                            ? Armanistän:                           Armeniya,            Provinz          des       pers.       Großreiches                    —     ap.
              arminiya                       1,

 .        5

5”,               -       ’armani:                    "Armenier"                  Nisba    v. ’Armanistän                   q. v.

              5
our                   _       °armahän:                        "weiches           Eisen"        pers.        2   (im       Gegensatz            zum     Stahl),             wahr-
              scheinlich                          aus           pers.           ar               narm        +   ähan       "weich        +     Eisen"           —m.Y2!
              +       p-           narm           +    Asıen..

  3                       x                                                                    -
LI                -           arandaf:                 "schwarzes                 Leder" = ’ardad                    u.    randaf        Ss.        z
                                                                                                                                                ’ardaf           U.       randaf.


yi-               ’uruz:                 "Reis"                 aus       dem     ostir.        u.    afgan.             virze,     pers.        z     biring,              frz.
              riz,             engl.              rice,              dtsch.        Reis     3,           mp.             brinj     4     syr.         1%)    , mand.
              runza,                   runzia                  5,

      ’
!-                    ’uriz              = ’uruz                    q.    v.

                          Pa                               .                                                     6         las
eb,               _           "arika:             "Sitz,                 Divan,     Thron"           pers.           ,    möglichst            aus     dem       pers.           51
              orang                "Thron" .


w-                    arya:              "Zahnfleisch"                          pers.      7     wahrscheinlich                    aus     dem       pers.            o_!,T
              Arwäre                          mp.              „pP         Erwärag         8,

 ..
Sıl-              äriyya:                    "Arier"                 9, Arisch           "zusammenfassende                        Bezeichnung               für       Iranisch
              und             Indisch",                        "Arier,          auch     Indoarier,              Angehöriger               eines        Volkes             mit
                                                                                                                                               1U
              indogermanischer                                       Sprache        in     Vorderindien                   und     Iran"                     MP              ei
                                                                                                                                               <1
              äryan                =     Eran          "Arisch,                 Iranisch"            au.             airya,        ap.     ariya             .




1.    Kent                    S.       171
2.        al-Marka°                          s.       v.
3.        Genaust                      Ss.    v.
4.    Mackenzie                              S.       v.
5.    Macuch                       s.        v.
6.        al-Marka°                          s.       v.
7.        ID.             s.       v.
8.    Mackenzie                              S.       v.
9,        Schregle                       S.       58
10.           Fremdwörterbuch                                       S.    v.
11.           Nyberg                   Bd.        II           s.    v.
```


## [2026-09-06T15:35:46.072Z] TOOL CALL #24: Bash

```json
{
 "command": "pdftoppm -f 233 -l 233 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg233 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/",
 "description": "Render page 233 image"
}
```


## [2026-09-06T15:35:48.428Z] TOOL CALL #25: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%82%D9%87%D9%88%D8%A9",
 "prompt": "Give the full Arabic etymology of قهوة qahwa 'coffee, wine' — what origin does Wiktionary give (Kaffa in Ethiopia? native Arabic root q-h-w 'to lack appetite'?), and list descendants (Turkish kahve, Persian قهوه, Italian caffè, French café, English coffee)."
}
```


### [2026-09-06T15:35:48.475Z] TOOL RESULT

```
total 4912
drwx------ 3 sfmqrb sfmqrb   4096 Sep  6 11:35 .
drwx------ 4 sfmqrb sfmqrb   4096 Sep  6 10:51 ..
-rw-rw-r-- 1 sfmqrb sfmqrb    682 Sep  6 11:34 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  92182 Sep  6 10:55 bqt1854.png
-rw-rw-r-- 1 sfmqrb sfmqrb  66580 Sep  6 10:57 bqt2023.png
-rw-rw-r-- 1 sfmqrb sfmqrb  69965 Sep  6 11:25 bqt2242crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb  28189 Sep  6 11:25 bqt2417crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb 431133 Sep  6 11:16 bqt2420_fn.png
-rw-rw-r-- 1 sfmqrb sfmqrb   9548 Sep  6 11:25 bqt2meta.json
-rw-rw-r-- 1 sfmqrb sfmqrb  81018 Sep  6 11:16 build213.py
-rw-rw-r-- 1 sfmqrb sfmqrb   6504 Sep  6 11:13 c1.png
-rw-rw-r-- 1 sfmqrb sfmqrb   3402 Sep  6 11:22 c224_n10.png
-rw-rw-r-- 1 sfmqrb sfmqrb   4812 Sep  6 11:28 c224_n12.png
-rw-rw-r-- 1 sfmqrb sfmqrb   4744 Sep  6 11:22 c224_n1.png
-rw-rw-r-- 1 sfmqrb sfmqrb   3203 Sep  6 11:28 c224_n7.png
-rw-rw-r-- 1 sfmqrb sfmqrb  12820 Sep  6 11:27 c229_bibua.png
-rw-rw-r-- 1 sfmqrb sfmqrb   5308 Sep  6 11:27 c229_greek.png
-rw-rw-r-- 1 sfmqrb sfmqrb   5313 Sep  6 11:27 c229_persian.png
-rw-rw-r-- 1 sfmqrb sfmqrb   7793 Sep  6 11:13 c2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   4371 Sep  6 11:13 c_gacele.png
-rw-rw-r-- 1 sfmqrb sfmqrb   3485 Sep  6 11:16 c_harmathan.png
-rw-rw-r-- 1 sfmqrb sfmqrb  12347 Sep  6 11:20 c_hdr.png
-rw-rw-r-- 1 sfmqrb sfmqrb   9147 Sep  6 11:16 c_herman2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   3841 Sep  6 11:16 c_herman.png
-rw-rw-r-- 1 sfmqrb sfmqrb  12691 Sep  6 11:20 c_ieuo.png
-rw-rw-r-- 1 sfmqrb sfmqrb   2071 Sep  6 11:26 c_ijlak2.png
-rw-rw-r-- 1 sfmqrb sfmqrb  14654 Sep  6 11:20 c_ijlak.png
-rw-rw-r-- 1 sfmqrb sfmqrb  12239 Sep  6 11:20 c_latis.png
-rw-rw-r-- 1 sfmqrb sfmqrb   6280 Sep  6 11:13 c_mag.png
-rw-rw-r-- 1 sfmqrb sfmqrb   6971 Sep  6 11:03 crop1.png
-rw-rw-r-- 1 sfmqrb sfmqrb   8619 Sep  6 11:03 crop2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   5240 Sep  6 11:03 crop3.png
-rw-rw-r-- 1 sfmqrb sfmqrb  12820 Sep  6 11:05 crop_germ.png
-rw-rw-r-- 1 sfmqrb sfmqrb   3408 Sep  6 11:05 crop_guthjo.png
-rw-rw-r-- 1 sfmqrb sfmqrb 111118 Sep  6 11:19 crop_habl.png
-rw-rw-r-- 1 sfmqrb sfmqrb   9001 Sep  6 11:05 crop_node12.png
-rw-rw-r-- 1 sfmqrb sfmqrb   5564 Sep  6 11:05 crop_node1.png
-rw-rw-r-- 1 sfmqrb sfmqrb   5286 Sep  6 11:05 crop_varathra.png
-rw-rw-r-- 1 sfmqrb sfmqrb  11652 Sep  6 11:13 c_xzn.png
-rw-rw-r-- 1 sfmqrb sfmqrb  83691 Sep  6 11:19 gen215.py
-rw-rw-r-- 1 sfmqrb sfmqrb   2303 Sep  6 11:25 j.json
-rw-rw-r-- 1 sfmqrb sfmqrb    228 Sep  6 11:06 jscheck.js
-rw-rw-r-- 1 sfmqrb sfmqrb  37376 Sep  6 11:09 mk201.py
-rw-rw-r-- 1 sfmqrb sfmqrb  77132 Sep  6 11:11 mk207.py
-rw-rw-r-- 1 sfmqrb sfmqrb  61121 Sep  6 11:11 mk208.py
-rw-rw-r-- 1 sfmqrb sfmqrb  80041 Sep  6 11:14 mk214.py
-rw-rw-r-- 1 sfmqrb sfmqrb  67513 Sep  6 11:27 mk217.py
-rw-rw-r-- 1 sfmqrb sfmqrb  74459 Sep  6 11:33 mk218b.py
-rw-rw-r-- 1 sfmqrb sfmqrb  17605 Sep  6 11:25 mk218.py
-rw-rw-r-- 1 sfmqrb sfmqrb  50138 Sep  6 11:24 mk222.py
-rw-rw-r-- 1 sfmqrb sfmqrb  78297 Sep  6 11:32 mk223.py
drwxrwxr-x 2 sfmqrb sfmqrb   4096 Sep  6 11:35 p216
-rw-rw-r-- 1 sfmqrb sfmqrb  17907 Sep  6 11:25 part1.json
-rw-rw-r-- 1 sfmqrb sfmqrb  54688 Sep  6 10:58 pg201.png
-rw-rw-r-- 1 sfmqrb sfmqrb  70083 Sep  6 10:52 pg204.png
-rw-rw-r-- 1 sfmqrb sfmqrb  77858 Sep  6 10:52 pg206.png
-rw-rw-r-- 1 sfmqrb sfmqrb  67371 Sep  6 10:53 pg207.png
-rw-rw-r-- 1 sfmqrb sfmqrb  59146 Sep  6 10:53 pg208.png
-rw-rw-r-- 1 sfmqrb sfmqrb  53054 Sep  6 11:00 pg209.png
-rw-rw-r-- 1 sfmqrb sfmqrb  74515 Sep  6 11:02 pg211.png
-rw-rw-r-- 1 sfmqrb sfmqrb 141781 Sep  6 11:03 pg212hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  75961 Sep  6 11:02 pg212.png
-rw-rw-r-- 1 sfmqrb sfmqrb  83761 Sep  6 11:03 pg213.png
-rw-rw-r-- 1 sfmqrb sfmqrb  83752 Sep  6 11:01 pg214.png
-rw-rw-r-- 1 sfmqrb sfmqrb 194102 Sep  6 11:05 pg215hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb 117034 Sep  6 10:54 pg215.png
-rw-rw-r-- 1 sfmqrb sfmqrb  76564 Sep  6 11:13 pg216.png
-rw-rw-r-- 1 sfmqrb sfmqrb  82798 Sep  6 11:16 pg217.png
-rw-rw-r-- 1 sfmqrb sfmqrb 147278 Sep  6 11:13 pg218hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  82099 Sep  6 11:13 pg218.png
-rw-rw-r-- 1 sfmqrb sfmqrb  71937 Sep  6 11:19 pg219.png
-rw-rw-r-- 1 sfmqrb sfmqrb  63280 Sep  6 11:18 pg220.png
-rw-rw-r-- 1 sfmqrb sfmqrb  71497 Sep  6 11:18 pg221.png
-rw-rw-r-- 1 sfmqrb sfmqrb 118895 Sep  6 11:16 pg222hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  84108 Sep  6 11:16 pg222.png
-rw-rw-r-- 1 sfmqrb sfmqrb  79615 Sep  6 11:18 pg223.png
-rw-rw-r-- 1 sfmqrb sfmqrb  90848 Sep  6 11:22 pg224hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  55412 Sep  6 11:15 pg224.png
-rw-rw-r-- 1 sfmqrb sfmqrb  80963 Sep  6 11:32 pg225.png
-rw-rw-r-- 1 sfmqrb sfmqrb 161218 Sep  6 11:26 pg226hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  74322 Sep  6 11:19 pg226.png
-rw-rw-r-- 1 sfmqrb sfmqrb  54381 Sep  6 11:31 pg227.png
-rw-rw-r-- 1 sfmqrb sfmqrb  52519 Sep  6 11:25 pg228.png
-rw-rw-r-- 1 sfmqrb sfmqrb  78760 Sep  6 11:27 pg229hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  42112 Sep  6 11:26 pg229.png
-rw-rw-r-- 1 sfmqrb sfmqrb  65310 Sep  6 11:32 pg230.png
-rw-rw-r-- 1 sfmqrb sfmqrb  69894 Sep  6 11:34 pg231.png
-rw-rw-r-- 1 sfmqrb sfmqrb  67111 Sep  6 11:35 pg233.png
-rw-rw-r-- 1 sfmqrb sfmqrb 147680 Sep  6 11:20 sns167.jpg
```


### [2026-09-06T15:35:55.537Z] TOOL RESULT

```
# Etymology of قهوة (qahwa)

## Origin Theories

Wiktionary presents **two competing etymologies**:

1. **Native Arabic Root**: Medieval philologists derived it from the root ق ه ي (q-h-y), "relating to satiety." According to Ibn Manẓūr, "it was named thus since it surfeits the drinker of it and takes away his desire." This connects to related Semitic words meaning "dull, weak, dim."

2. **Ethiopian Origin**: "Some sources trace the term back to the Omotic Kaffa, the name of the region in Ethiopia where coffee was first grown." However, Wiktionary notes this is dubious since the word meant "wine" in Arabic more than 500 years before the Kingdom of Kaffa existed.

The lexicon notes the "coffee" sense is ultimately "of disputed origin."

## Selected Descendants

The word spread widely through trade routes, producing descendants including:
- **Ottoman Turkish**: قهوه (kahve)
- **Persian**: قهوه (qahwa)
- **Swahili**: kahawa
- **Indonesian/Malay**: kahwa
- **Hebrew**: קהוה (kahvá)

Note: Wiktionary's descent chart does not directly list Italian *caffè*, French *café*, or English *coffee*, though these ultimately derive from Arabic through intermediate languages.
```


## [2026-09-06T15:36:01.583Z] TOOL CALL #26: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg233.png"
}
```


### [2026-09-06T15:36:01.958Z] TOOL RESULT

```

```


## [2026-09-06T15:36:01.955Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-06T15:36:03.253Z] TOOL CALL #27: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/coffee",
 "prompt": "Full etymology of 'coffee': the chain (Dutch/Italian caffe, Turkish kahveh, Arabic qahwah) and what it says about the Kaffa Ethiopia theory and the native Arabic root 'to have no appetite'. Also give the etymology entries for 'cafe' and 'caffeine' if present."
}
```


### [2026-09-06T15:36:10.308Z] TOOL RESULT

```
# Etymology of Coffee

## Main Etymology Chain

The word "coffee" entered English around 1600 through a linguistic journey: Dutch *koffie* → Turkish *kahveh* → Arabic *qahwah*. 

Arab scholars linked *qahwah* to "a word meaning 'wine,'" though etymologists propose an alternative origin: the *Kaffa* region of Ethiopia, where the plant originated. In Kaffa, the beverage was called *būno*, which Arabic borrowed as *bunn* meaning "raw coffee."

Early English variants included *chaoua* (1598), *cahve*, and *kahui*. Romance language forms—French *café* and German *Kaffe*—derive via Italian *caffè*.

The beverage reached Mecca by the 1510s, Turkey by the 1530s, Europe around 1515-1519, and England by 1650.

## Cafe

"Coffee-house, restaurant" (1802) comes from French *café*, which derives from Italian *caffe*. Venice encountered the beverage by 1615; France by the 1650s through merchants and travelers. The earliest European café possibly opened in Marseilles in 1660.

## Caffeine

This term originated in 1830 from German *Kaffein*, coined by chemist F.F. Runge. It combines German *Kaffee* ("coffee") with the chemical suffix *-ine*, named for the alkaloid's discovery in coffee beans.
```


## [2026-09-06T15:36:43.676Z] TOOL CALL #28: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D5%AF%D5%B8%D5%B7%D5%AB%D5%AF",
 "prompt": "What is the etymology of Armenian կոշիկ / կօշիկ (košik/kōšik) 'shoe'? Is it derived from Iranian/Middle Persian kafš, or is it inherited/native? Quote the etymology section."
}
```


## [2026-09-06T15:36:45.434Z] TOOL CALL #29: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%A9%D9%81%D8%B4",
 "prompt": "Give the Persian etymology of کفش kafš 'shoe' — Middle Persian form, Proto-Iranian reconstruction, related words, and any listed descendants/borrowings (Arabic قفش, Armenian, Greek)."
}
```


### [2026-09-06T15:36:48.622Z] TOOL RESULT

```
# Etymology of Armenian կոշիկ (košik)

Based on the Wiktionary content provided, the etymology section states:

> "Inherited from Old Armenian կօշիկ (kōšik)."

The page does not provide information about whether the word ultimately derives from Iranian or Middle Persian sources. It only traces the Modern Armenian form back to its Old Armenian predecessor, indicating it is an inherited word within Armenian linguistic tradition rather than a recent loanword.
```


### [2026-09-06T15:36:52.316Z] TOOL RESULT

```
# Etymology of Persian کفش (kafš) "shoe"

**Middle Persian Form:**
The word derives from Middle Persian *kpš* (kafš, "shoe"), with uncertain ultimate origins.

**Related Words Across Languages:**
The entry identifies cognates in several languages:
- Old Armenian կօշիկ (kōšik)
- Northern Luri کڢش (kwṣ)
- Arabic قَفْش (qafš) — listed as an Iranian loanword
- Potentially Old Armenian կապ (kap, "bond"), suggesting possible Proto-Indo-European connection to *\*kap-* ("to seize, hold"), though "formal details unclear"

**Documented Descendants/Borrowings:**
The article lists numerous languages that borrowed the term, including:
- Arabic: قَفْش (qafš)
- Georgian: ქოში (koši)
- Turkic languages (Chagatai, Uyghur, Uzbek, Kyrgyz, Turkmen, Kazakh)
- Malay/Indonesian: kaus
- Hindi: कफ़्श (kafś)

The entry notes that while cognate relationships exist across Indo-European and neighboring language families, "further origin [remains] uncertain."
```


## [2026-09-06T15:36:59.374Z] TOOL CALL #30: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D5%AF%D6%85%D5%B7%D5%AB%D5%AF",
 "prompt": "Old Armenian կօշիկ (kōšik) 'shoe' — quote the full etymology section. Does it relate the word to Middle Persian kafš / Iranian, to Greek καυκίς, or call it of unknown origin? Any mention of Ačaṙyan or Hübschmann?"
}
```


## [2026-09-06T15:37:00.203Z] TOOL CALL #31: WebSearch

```json
{
 "query": "Greek καυκίς kaukis shoe Hesychius Armenian կօշիկ kōšik etymology Persian kafš"
}
```


### [2026-09-06T15:37:05.168Z] TOOL RESULT

```
# Etymology of կօշիկ (kōšik)

According to the Wiktionary entry, the word's etymology is traced to Iranian origins. The source states:

> "borrowed from Iranian *kafšīk. Compare Middle Persian [script needed] (kpš /⁠kafš⁠/)"

The entry establishes a clear connection to Middle Persian **kafš** ("shoe") and notes comparisons with Persian **کفش** (kafš) and Central Kurdish **کەوش** (kewş).

The entry does **not** mention Greek **καυκίς**, nor does it indicate unknown origin. However, it does cite **Ačaṙean** as a reference source—his 1971–1979 Armenian Etymological Dictionary is listed in the references section. Hübschmann is not mentioned in this particular entry.
```


### [2026-09-06T15:37:18.827Z] TOOL RESULT

```
Web search results for query: "Greek καυκίς kaukis shoe Hesychius Armenian կօշիկ kōšik etymology Persian kafš"

Links: [{"title":"ἁρπίς - Ancient Greek (LSJ)","url":"https://lsj.gr/wiki/%E1%BC%81%CF%81%CF%80%CE%AF%CF%82"},{"title":"σικύα - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%CF%83%CE%B9%CE%BA%CF%8D%CE%B1"},{"title":"Pre-Greek: The lost language hidden within Ancient Greek","url":"https://linguisticdiscovery.substack.com/p/pre-greek"},{"title":"Kakasbos","url":"https://en.wikipedia.org/wiki/Kakasbos"},{"title":"C","url":"https://en.wikipedia.org/wiki/List_of_Greek_and_Latin_roots_in_English/C"},{"title":"Tsarouchi","url":"https://en.wikipedia.org/wiki/Tsarouchi"},{"title":"Hesychius of Alexandria","url":"https://en.wikipedia.org/wiki/Hesychius_of_Alexandria"},{"title":"κρηπίς - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%CE%BA%CF%81%CE%B7%CF%80%CE%AF%CF%82"},{"title":"Crepida","url":"https://en.wikipedia.org/wiki/Crepida"},{"title":"Caucones","url":"https://en.wikipedia.org/wiki/Caucones"}]

The search results don't contain specific information about the Greek word καυκίς (kaukis) and its potential connection to Armenian կօշիկ (kōšik) or Persian kafš. Let me search with a more targeted approach.

Links: [{"title":"kaus - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/kaus"},{"title":"ქოში - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%E1%83%A5%E1%83%9D%E1%83%A8%E1%83%98"},{"title":"کفش - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%DA%A9%D9%81%D8%B4"},{"title":"\"kaus\" meaning in Indonesian","url":"https://kaikki.org/dictionary/Indonesian/meaning/k/ka/kaus.html"},{"title":"Walking the line: Footwear in Iranian culture - Tehran Times","url":"https://www.tehrantimes.com/news/397690/Walking-the-line-Footwear-in-Iranian-culture"},{"title":"Zarrin-Kafsh (tribe)","url":"https://en.wikipedia.org/wiki/Zarrin-Kafsh_(tribe)"},{"title":"کژ - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%DA%A9%DA%98"},{"title":"Kashkul","url":"https://en.wikipedia.org/wiki/Kashkul"},{"title":"Zarrin-Kafsh (tribe)","url":"https://grokipedia.com/page/zarrin_kafsh_tribe"}]

Now let me search specifically for the Greek word and its etymological connections.

Links: [{"title":"ἁρπίς - Ancient Greek (LSJ)","url":"https://lsj.gr/wiki/%E1%BC%81%CF%81%CF%80%CE%AF%CF%82"},{"title":"Tsarouchi","url":"https://en.wikipedia.org/wiki/Tsarouchi"},{"title":"Hesychius of Miletus","url":"https://en.wikipedia.org/wiki/Hesychius_of_Miletus"},{"title":"Hesychius of Alexandria","url":"https://en.wikipedia.org/wiki/Hesychius_of_Alexandria"},{"title":"Amerias","url":"https://en.wikipedia.org/wiki/Amerias"},{"title":"Crepida","url":"https://en.wikipedia.org/wiki/Crepida"},{"title":"Ancient Greek Footwear: Sandals, Krepides and Endromides - Legio X Fretensis","url":"https://x-legio.com/en/wiki/greek-shoes"},{"title":"Ancient Greek Fashion","url":"https://www.hellenicaworld.com/Greece/Ancient/en/Fashion3.html"}]

Let me search more specifically for the Armenian word and its Persian connection:

Links: [{"title":"کفش - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%DA%A9%D9%81%D8%B4"},{"title":"կապ - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D5%AF%D5%A1%D5%BA"},{"title":"ქოში - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%E1%83%A5%E1%83%9D%E1%83%A8%E1%83%98"},{"title":"کژ - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%DA%A9%DA%98"},{"title":"Kalehjoosh","url":"https://en.wikipedia.org/wiki/Kalehjoosh"},{"title":"Kardashian (surname)","url":"https://en.wikipedia.org/wiki/Kardashian_(surname)"},{"title":"Arman (given name)","url":"https://en.wikipedia.org/wiki/Arman_(given_name)"},{"title":"Galesh","url":"https://en.wikipedia.org/wiki/Galesh"},{"title":"Tsarouchi","url":"https://en.wikipedia.org/wiki/Tsarouchi"},{"title":"shoes in Armenian - English-Armenian Dictionary | Glosbe","url":"https://glosbe.com/en/hy/shoes"}]

Based on my search results, I can now provide you with information about the etymological connections between these words related to shoes:

## Summary of Findings

Persian kafš ("shoe") is akin to Old Armenian կօշիկ (kōšik), Northern Luri کۏش (köş) and Arabic قَفْش (qafš). The Persian word derives from Middle Persian kpš (kafš, "shoe"), with further origin uncertain.

Regarding the specific Greek word καυκίς (kaukis) that you mentioned in your query, I was unable to find direct search results that explicitly connect this Greek term to the Persian kafš or Armenian կօշիկ (kōšik). My searches returned information about other Greek shoe-related terms documented in Hesychius (such as ἁρπίς/harpís), but not specifically about καυκίς.

The most relevant connection I found is between the Persian kafš and Armenian κօշիկ (kōšik), which appear to be related through a shared etymological origin, though the ultimate source remains unclear. Some scholars suggest potential derivation from an extension or compound of Proto-Indo-European *kap- ("to seize, hold"), albeit with formal details unclear.

If you have specific scholarly sources discussing the Greek-Persian-Armenian connections for shoe terminology, I would be interested in examining those more directly.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-06T15:37:28.784Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\np='BQT_v2_pages.txt'\ntxt=open(p,encoding='utf-8',errors='replace').read()\nlines=txt.split('\\n')\nleaf=1\nlineleaf=[]\nfor l in lines:\n    lineleaf.append(leaf)\n    leaf += l.count('\\f')\nfor t in [12810,12824,12877,12923,12926,12942]:\n    print(t,'leaf',lineleaf[t-1],'printed ~',lineleaf[t-1]+543)\nEOF",
 "description": "Map BQT v2 lines to printed pages"
}
```


### [2026-09-06T15:37:30.885Z] TOOL RESULT

```
12810 leaf 218 printed ~ 761
12824 leaf 218 printed ~ 761
12877 leaf 219 printed ~ 762
12923 leaf 220 printed ~ 763
12926 leaf 220 printed ~ 763
12942 leaf 220 printed ~ 763
```


## [2026-09-06T15:37:30.948Z] TOOL CALL #33: WebFetch

```json
{
 "url": "https://lsj.gr/wiki/%CE%BA%CE%B1%CF%85%CE%BA%CE%AF%CF%82",
 "prompt": "Is καυκίς a Greek word? Give the LSJ definition and any note on its meaning (a kind of shoe? a cup?). Also mention καυκαλον if present."
}
```


### [2026-09-06T15:37:32.810Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-06T15:37:46.865Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\ncurl -s \"https://archive.org/metadata/mann-an-indo-european-comparative-dictionary-1984-1987\" | python3 -c \"\nimport json,sys\nd=json.load(sys.stdin)\nprint(d.get('server'), d.get('dir'))\nfor f in d['files'][:40]:\n    print(f['name'], f['format'])\n\" 2>&1 | head -50",
 "description": "Get IEC archive metadata"
}
```


## [2026-09-06T15:37:47.585Z] TOOL CALL #35: WebFetch

```json
{
 "url": "https://logeion.uchicago.edu/%CE%BA%CE%B1%CF%85%CE%BA%CE%AF%CF%82",
 "prompt": "What does LSJ / Greek lexica give for καυκίς? Is it a kind of shoe or a cup? Quote the definition."
}
```


### [2026-09-06T15:37:51.953Z] TOOL RESULT

```
ia802900.us.archive.org /17/items/mann-an-indo-european-comparative-dictionary-1984-1987
Mann - An Indo-European Comparative Dictionary (1984-1987).epub EPUB
Mann - An Indo-European Comparative Dictionary (1984-1987).pdf Text PDF
Mann - An Indo-European Comparative Dictionary (1984-1987)_chocr.html.gz chOCR
Mann - An Indo-European Comparative Dictionary (1984-1987)_djvu.txt DjVuTXT
Mann - An Indo-European Comparative Dictionary (1984-1987)_djvu.xml Djvu XML
Mann - An Indo-European Comparative Dictionary (1984-1987)_hocr.html hOCR
Mann - An Indo-European Comparative Dictionary (1984-1987)_hocr_pageindex.json.gz OCR Page Index
Mann - An Indo-European Comparative Dictionary (1984-1987)_hocr_searchtext.txt.gz OCR Search Text
Mann - An Indo-European Comparative Dictionary (1984-1987)_jp2.zip Single Page Processed JP2 ZIP
Mann - An Indo-European Comparative Dictionary (1984-1987)_page_numbers.json Page Numbers JSON
Mann - An Indo-European Comparative Dictionary (1984-1987)_scandata.xml Scandata
__ia_thumb.jpg Item Tile
mann-an-indo-european-comparative-dictionary-1984-1987_archive.torrent Archive BitTorrent
mann-an-indo-european-comparative-dictionary-1984-1987_files.xml Metadata
mann-an-indo-european-comparative-dictionary-1984-1987_meta.sqlite Metadata
mann-an-indo-european-comparative-dictionary-1984-1987_meta.xml Metadata
```


### [2026-09-06T15:37:56.369Z] TOOL RESULT

```
I don't have access to the web page content you're referring to, as the content section between the dashes appears to be empty. Without being able to see the actual LSJ (Liddell-Scott-Jones Greek Lexicon) entry or other lexical sources, I cannot provide you with a direct quote about καυκίς.

To answer your question accurately, I would need you to either:
1. Paste the actual lexicographical content, or
2. Allow me to note that you'd need to consult the LSJ directly or a reliable Greek lexicon resource

If you have specific text you'd like me to analyze, please share it and I'll be happy to help with proper attribution and character limits.
```


## [2026-09-06T15:38:00.866Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\ncurl -sG 'https://ia802900.us.archive.org/fulltext/inside.php' \\\n --data-urlencode 'item_id=mann-an-indo-european-comparative-dictionary-1984-1987' \\\n --data-urlencode 'doc=mann-an-indo-european-comparative-dictionary-1984-1987' \\\n --data-urlencode 'path=/17/items/mann-an-indo-european-comparative-dictionary-1984-1987' \\\n --data-urlencode 'q=kaukis' | head -c 3000",
 "description": "Fulltext search IEC for kaukis"
}
```


### [2026-09-06T15:38:03.032Z] TOOL RESULT

```
{"ia":null,"q":null,"indexed":true,"matches":[],"error":"No hOCR or Abbyy file present"}
```


## [2026-09-06T15:38:07.605Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor q in kaukis kawsik kaukalon; do\necho \"== $q ==\"\ncurl -sG 'https://ia802900.us.archive.org/fulltext/inside.php' \\\n --data-urlencode 'item_id=mann-an-indo-european-comparative-dictionary-1984-1987' \\\n --data-urlencode 'doc=Mann - An Indo-European Comparative Dictionary (1984-1987)' \\\n --data-urlencode 'path=/17/items/mann-an-indo-european-comparative-dictionary-1984-1987' \\\n --data-urlencode \"q=$q\" | head -c 2500; echo\ndone",
 "description": "Fulltext search IEC with correct doc stem"
}
```


### [2026-09-06T15:38:13.120Z] TOOL RESULT

```
== kaukis ==
{"ia": "mann-an-indo-european-comparative-dictionary-1984-1987", "q": "kaukis", "indexed": true, "matches": [{"text": "kaukos (1) \u2018shriek, howl, clamour, call\", Variant: k\u0101uk- as separate entry, cf. also kauko above. Cf. WP I, 331, 371 & 466. Extn. mng. \u2018howler\u2019, etc. Skt. k\u00f3kah \"wolt\" beside (variant) kau$ikah \u2018owl\u2019; Ir. cuach \u2018cuckoo\u2019; Blg. kuk, id. beside ku\u010de \u2018dog\u2019; OCS cf. kuctka \u2018bitch\u2019; Li. ka\u00fckas (\u2018goblin, mandrake, thunderbolt\u2019 in folklore); kauk\u00fds \u02bba raucous bird'; ki\u00e1uke \u2018jackdaw\u2019; Latv. <IA_FTS_MATCH>kaukis</IA_FTS_MATCH> (\u2018bawler; blackcap\u2019 ornith.); cf. (variant) Slovene \u010duk \u2018owl\u2019. (Isophonic: LLat. caucus \u2018concubine\u2019 and Alb. kak\u00eb- in kak\u00eb- zoz\u00eb \u2018salamander\u2019: Latv <IA_FTS_MATCH>kaukis</IA_FTS_MATCH>, <IA_FTS_MATCH>kaukis</IA_FTS_MATCH> (2), m. \u2018toad\u2019. The Alb. form suggests a prototype *kauko-dieudio)", "par": [{"l": 448, "t": 2070, "r": 1503, "b": 2447, "page": 256, "boxes": [{"l": 448, "t": 2070, "r": 653, "b": 2145, "page": 256}, {"l": 1047, "t": 2373, "r": 1273, "b": 2445, "page": 256}, {"l": 1297, "t": 2375, "r": 1503, "b": 2447, "page": 256}], "page_width": 3901, "page_height": 5698}]}, {"text": "kaukos, is, \u00e0 (kauk-) \u201ca raucous bird\u2019. WP I, 33] Skt. k\u00f3kah (2) \u2018red goose, cuckoo\u2019; Hind. koki \u2018crow\u2019; Sind. kok, m. \u2018cuckoo; frog\u2019; Per. kabg \u2018partridge\u2019; Tokh. A cf. kokafi \u201can un- identified bird\u201d; Gk. k\u00e9ux, gs k\u00e9ukos \u201ca gull\u2019 beside k\u00e1b\u00e9x, ka\u00fa\u0113x, id.; Sard. coca \u2018goose\u2019 beside Sard. (Campid.) coga (^witch', cf. mngs. of Lat. strix); Ir. cuach \u2018cuckoo\u2019; W cawci (jackdaw': Hind. koki); Cz. kavka, Pol. kawka \u201cdaw\u201d; Srb. cf. (variant) Cavka, id.; Li. kaukys, m. \u201ca shrill bird\u2019; kiauke \u2018daw\u2019; Latv. <IA_FTS_MATCH>kaukis</IA_FTS_MATCH> *blackcap gull'. (A similar onomat. element is present in Hind. kauwa \u2018crow, daw? and in Fr. cahouette, id.)", "par": [{"l": 1695, "t": 3239, "r": 1900, "b": 3309, "page": 257, "boxes": [{"l": 1695, "t": 3239, "r": 1900, "b": 3309, "page": 257}], "page_width": 3901, "page_height": 5698}]}, {"text": "keuk\u00f3 \u2018curl up, cower; curl; lurking, hud- dled\u2019. Cf. WP I, 372 Skt. cf. \u010dokam (name of a root); \u010do\u010dam *cinna- mon-bark\u2019; cf. ko\u010d\u0101
== kawsik ==
{"ia": "mann-an-indo-european-comparative-dictionary-1984-1987", "q": "kawsik", "indexed": true, "matches": [{"text": "kaukis, ios in Per. kaf5 \"boot\" and Gk. (Iran. LW?) kauk\u00eds, f. \u201ckind of shoe\u2019, cf. ka\u00fckalon \u2018shaft of boot\" (queried). Iran LW in Arm. <IA_FTS_MATCH>kaw\u0161ik</IA_FTS_MATCH> 'shoe\")", "par": [{"l": 2107, "t": 3344, "r": 2325, "b": 3401, "page": 829, "boxes": [{"l": 2107, "t": 3344, "r": 2325, "b": 3401, "page": 829}], "page_width": 3901, "page_height": 5698}]}]}
== kaukalon ==
{"ia": "mann-an-indo-european-comparative-dictionary-1984-1987", "q": "kaukalon", "indexed": true, "matches": [{"text": "kaukol-os (1) \u2018skull, basin, trough'. WP I, 331. Cf. ka\u00fcKos Per. cf, kafce (-ladle\" LW in R kov\u0161, id.); Gk. kauk\u00e1lion \u2018vesse\u013e, <IA_FTS_MATCH>ka\u00fckalon</IA_FTS_MATCH> ('skull'. Ambig. cf. kauK-); Li. k\u00e1ukolis, io, m. and k\u00e1ukole, es, f. \u2018skull\u2019; Finn. LW kaukalo \u201ctrough?", "par": [{"l": 2773, "t": 2947, "r": 3071, "b": 3006, "page": 255, "boxes": [{"l": 2773, "t": 2947, "r": 3071, "b": 3006, "page": 255}], "page_width": 3901, "page_height": 5698}]}, {"text": "kaukis, ios in Per. kaf5 \"boot\" and Gk. (Iran. LW?) kauk\u00eds, f. \u201ckind of shoe\u2019, cf. <IA_FTS_MATCH>ka\u00fckalon</IA_FTS_MATCH> \u2018shaft of boot\" (queried). Iran LW in Arm. kaw\u0161ik 'shoe\")", "par": [{"l": 3291, "t": 3143, "r": 3589, "b": 3202, "page": 829, "boxes": [{"l": 3291, "t": 3143, "r": 3589, "b": 3202, "page": 829}], "page_width": 3901, "page_height": 5698}]}]}
```


## [2026-09-06T15:38:31.624Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\ncurl -s \"https://ia802900.us.archive.org/17/items/mann-an-indo-european-comparative-dictionary-1984-1987/Mann%20-%20An%20Indo-European%20Comparative%20Dictionary%20%281984-1987%29_page_numbers.json\" | python3 -c \"\nimport json,sys\nd=json.load(sys.stdin)\npgs=d.get('pages',d)\nfor p in pgs:\n    if isinstance(p,dict) and p.get('leafNum') in (255,256,257,828,829,830):\n        print(p)\n\" 2>&1 | head -20\necho \"--- local grep kaf5 ---\"\ngrep -n \"kaukis, ios\\|kaf5\" data/verification/sources/refs/IEC.txt | head",
 "description": "Map IEC leaf 829 to printed page"
}
```


### [2026-09-06T15:38:33.849Z] TOOL RESULT

```
{'confidence': 0, 'pageNumber': '477', 'ocr_value': ['479', '480'], 'leafNum': 255}
{'confidence': 0, 'pageNumber': '478', 'ocr_value': ['481', '482'], 'leafNum': 256}
{'confidence': 0, 'pageNumber': '479', 'ocr_value': ['483', '484'], 'leafNum': 257}
{'confidence': 0, 'pageNumber': '1616', 'ocr_value': ['1625', '1626'], 'leafNum': 828}
{'confidence': 0, 'pageNumber': '1617', 'ocr_value': ['1627', '1628', '386'], 'leafNum': 829}
{'confidence': 0, 'pageNumber': '1618', 'ocr_value': ['1629', '1630'], 'leafNum': 830}
--- local grep kaf5 ---
```


## [2026-09-06T15:38:53.025Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== LKT Kaffee/qahwa ===\"; grep -n -i \"qahwa\\|kahve\\|Kaffee\" LKT.txt | head -10\necho \"=== LKT Kaftan ===\"; grep -n -i \"kaftan\\|haftan\\|qaftan\" LKT.txt | head -10\necho \"=== TTS kaftan ===\"; grep -n -i \"kaftan\\|qaftan\" incoming/TTS/TTS_pages.txt | head -10\necho \"=== DEV cafe/caftan ===\"; grep -n -i \"^café\\|caftan\\|cafetan\\|CAFÉ\" DEV.txt | head -10\necho \"=== PHN ===\"; grep -n -i \"caftan\\|cafetan\\|café\" PHN.txt | head -10",
 "description": "Grep Lokotsch, Vambery, Devic, Pihan"
}
```


### [2026-09-06T15:38:53.129Z] TOOL RESULT

```
=== LKT Kaffee/qahwa ===
1528:'Porzellan,  Tasse  daraus',  tic.  ebenso, vulg.  ßlgan  [mit  Dissimilation]  'kleine Tasse';  hieraus  rum.  filigean  '^Tasse', (Walachei)  filingen  'Kaffeescliale',  bulg. serh.fildian,  serh.findzaii,  klvuss.  findza, poln.  filizanka,  fliianka  'Tasse',  klruss. fyndzan  'Becher'.    [Bern  SlEtWb  280.
2153:'Wasserkrug',  besonders  für  die  vor- geschriebenen Waschungen  der  Muslimen gebraucht  [aus  dem  Pers.,  doch  kennt man  das  pers.  Grundwort  noch  nicht, vgl.  de  Lagarde,  Gesammelte  Abhand- lungen S.  7];  tk.  ebenso;  hieraus  rum. ibric  'Wasserkrug,  Wasserkanne',  it. bricco  'Zinnkanne  für  Kaffee',  bulg.  serb. ibrik  'Waschkanne,  Krug',  serb.  imbrik, Y)o]n.imb)yk,  imhryczek  'Tee-  oder  Kaffee- kanne', klruss.  imbrycek  'dass.'.  [ML 4253.    Bern  SlEtWb  419.
2398:'Wein'  [doch  stammt  das  Wort  sicher- lich wie  die  Sache  selbst  aus  der  Um- gebung Abessiniens:  die  Landschaft Kaffa  ist  die  Heimat  des  Kaffeebaumes, der  von  Saih  aS-SÄDILI  nach  Süd- arabien eingeführt  wurde,  wo  der  Haupt- ausfuhrhafen Moha  war;  hieraus  dtsch. Mokka],  tk.  kahtve;  hieraus  um  die Wende  des  16.  und  17.  Jahrhunderts  in Europa  eingeführt  als  it.  cahue  [Pietro della  Valle,  Viaggi  (ediz.  di  Roma)  I, 110],  caffh,  frz.  sp.  pg.  cafS,  rum.  cafe, cafea;  engl,  coffee,  ndl.  hoffie,  dtsch. Kaffee  [1582  als  chaube,  1663  cahwe belegt] ;  russ.  kofe,  kofej,  klruss.  kofij, kava,  Cech.  käva,  poln.  kaiva,  bulg. kahwe,  serb.  kahwa,  kafa  [vgl.  poln.  ka- pinaz,  kafenauz  <^  dtsch.  Kaffeehaus].
2402:ihre  Gebetsstunden  nicht  verschliefen. Im  Jahre  1459  kam  der  Kaffee  [wie oben  angedeutet]  nach  Arabien  und  bald nach  Syrien:  um  1550  wurden  von Damaskus  und  Aleppo  aus  die  ersten Kaffeehäuser  in  Konstantinopel  einge- richtet; um  1580  brachten  die  Venezianer das  Getränk  nach  dem  übrigen  Europa. Die  ersten  Kaffeehäuser  wurden  1650 zu  Oxford,  1652  in  London,  1679  in Hamburg  und  1721  in  Berlin  eröffnet. —  Aus  tk.  kahtve  alty  [wörtlich  ,das Untere  des  Kaffees'  von  alt  'unten'. Stamm  al  'nieder,  unter'  Vämbery  Tkt EtWb  S.  13,  Nr.  12],  vulg.  kahtvalty 'erstes  Frühstück',  wurde  rum.  cafaltlc 'dass.'.  [Gorjajew  164.  Bern  SlEtWb 468/469.  Kluge  220.  Hobson-Jobson 232/233,  JVlWiD  82.  (Ar.  Ansichten über  die  Etymologie  des  Wortes  s.  de Sacy  ChrAr  I,  180;  II,  226/227).
2405:'Wie'i",  tk.  fcey/ 'Befinden,  Wohlbefinden', dessen  Betätigung  im  Sinne  des  Orien- talen vor  allem  träumerisches  Nichtstun beim  Rauchen  und  Kaffeeirinken  ist. Hieraus  rum.  chef  'Lustigkeit,  Wohl- behagen', chefliü,  chefo^  'kreuzfidel', bulg.  kejf,  kef  'Lust,  gute  Laune',  serb. Cef,  ceif,  ceip  'Lust',  poln.  kiejf  'Mittags- ruhe'. [Bern  SlEtWb  499.  De  Sacy ChrAr  II,  479.
3152:1357.  Ar.  mahlük: 'Geschaffen'  [part.  pass.  von  ^alaka  'er- schaffen']; hieraus  siz.  macaluco  Matte di  pollo',  d.  h.  in  den  Kaffee  geschlagenes El.  [GrSVociSi.:  239  (mit  Hinweis  auf Corrado  Avolio,  Introduzione  allo  studio del  dialetto  siciiiano.  Noto  1882.  S.  44].
5787:Äafta?e  977 iCrtöajg  993 iCa^eZ  766 Zaö(//e  979 ^Tad«  984 ifßtZjne  989 i:fl/f  992 Kaffee  4005 ^^//fe;-  992 Ka filier  j.  1150 Kaftan  774 Kaj>'put(öl)  1142 Kakadu  1Ü17 Kolbehasit  St.  1026 Kalbelazguar  St.  1025 Kalbolacrab  St.  1026 kalekutischer  Hahn  1031 kalemine  mhd.  1149 Kalender  1024 Kalenter  1024 kalfatern  1022 Kaliber  1030 ifaZ//"  798 A'rtZiX-o  1031 Kalium  1029 ifaZ/e  j.  1035 ifaZo«^  1038 Ar<?jjrtfc  1039 Kamel  653 Kamelie  653 Kamelhaut  653 Kamelot(t)  653 Kampfer  1100 Kandare  1051 kandieren  1052 Kandis  fzuckerj  1052 Kantschu(k)  1042 iCao/in  1060 Kap(p)ern  978
=== LKT Kaftan ===
1091:'Tuch,  gefütterter  Rock' ;  hieraus  russ. cekmen  'Kasaken-  oder  Bauernrock', klruss.  6ehmen,  cehman  'tatarisches  Ober- kleid', poln.  czekman  'dass.'.  —  Aus  der ost-  und  nordtk.  Entsprechung  [cagat. sükmän,  cuwas.  stihman]  wurde  rum. sucman,  suman  'Bauernkittel',  russ.  suk- man  'Tuchrock,  Kaftan',  klruss.  poln. sukmana  'Bauernkittel  aus  Tuch'.  [Gor- jajew  409.    Bern  SlEtWb  139.
1882:Ebenso  ar.  und  tk.  kaftän  'ein  Gewand' aus  Seide  oder  Brokat,  das  die  Orien- talen über  den  anderen  Kleidungsstücken tragen;  es  wird  mit  einem  Gürtel  ge- halten; die  Ärmel  sind  meistens  länger als  die  Arme  [Dozy  Vetem  162/168]; hieraus  russ.  klruss.  serb.  öech.  poln. haftan  'langschößigerRock' ;  vnm.caftan, sp.  pg.  caftan,  it.  caffetano,  frz.  caftan, cafetan;  engl,  caftan,  kaftan,  ndl.  caf- tan, dtsch.  Kaftan.  [DE  245.  Gorjajew 137.    Bern  SlEtWb  468.
2090:GuDst  geschenkt  wurde;  ursprünglich ein  'Kleidungsstück'  ganz  allgemein; wahrscheinlich  selbst,  Entlehnung  aus dem  Pers.  oder  Türk.,  da  die  Nisba zwischen  hWl  und  huVi  sowie  das  Vb. zwischen  }iaWa  und  kaWa  'schenken' schwanken],  tk.  halat;  hieraus  rum. halat,  russ.  Jialat,  serb.  hahjna  'Schlaf- rock', poln.  klruss.  cha/at  'Kaftan';  sp. gala  'Kleiderpracht',  it.  gala,  frz.  habit de  gala,  dtsch.  Gala,  engl.  gala.  Sp. galano  [eigentlich  'in  Gala  gekleidet'] 'höfisch,  artig',  hieraus  dtsch.  Galan [über  den  Wiener  Hof,  da  das  Wort  im Frz.  fehlt] ;  it.  sp.  galante  'zierlich  und modisch  gekleidet',  frz.  galant,  dtsch. galant,  dazu  frz.  galanterie  'Höflichkeit, modisch  feines  \ieaehmen\  galanthot7ime, it.  galantuomo,  dtsch.  Galanter-ie(v^tivei\). [Dagegen  stammt  elegant  aus  dem  lat. elegantem  'wählerisch'.]  — •  Die  anderen Ableitungen  scheinen  begrifflich  weniger einfach:  a)  gr.  plur.  KoXd  'schöne  Dinge', wobei  k  y  g  wie  in  KÖXTTog  >  Golf; b)  afrz.  gnle  'das  Ergötzen',  so  Kluge 154;  c)  ahd.  geili  'Prunk,  Üppigkeit, Lustigkeit'  nach  Diez.  [Gorjajew  394. Bern  SlEtWb  383.
5787:Äafta?e  977 iCrtöajg  993 iCa^eZ  766 Zaö(//e  979 ^Tad«  984 ifßtZjne  989 i:fl/f  992 Kaffee  4005 ^^//fe;-  992 Ka filier  j.  1150 Kaftan  774 Kaj>'put(öl)  1142 Kakadu  1Ü17 Kolbehasit  St.  1026 Kalbelazguar  St.  1025 Kalbolacrab  St.  1026 kalekutischer  Hahn  1031 kalemine  mhd.  1149 Kalender  1024 Kalenter  1024 kalfatern  1022 Kaliber  1030 ifaZ//"  798 A'rtZiX-o  1031 Kalium  1029 ifaZ/e  j.  1035 ifaZo«^  1038 Ar<?jjrtfc  1039 Kamel  653 Kamelie  653 Kamelhaut  653 Kamelot(t)  653 Kampfer  1100 Kandare  1051 kandieren  1052 Kandis  fzuckerj  1052 Kantschu(k)  1042 iCao/in  1060 Kap(p)ern  978
7653:kabala  977 kaban  975 Ä;a6a^  971 kaczan  1192 Ä:a(ft  984 fcarfy  984 kafenauz  1005 kaftan  Iii. kaik  1014 kalauz  1276 Ä;a/efca  1040 kaleta  828 Ä;afÄ;aw  1034 kalkun(t)  1031 kamcha  1043 kamfora  1100 katnlot  653 kanczug  1042 kanczuk  1042 kanfora  1100 kaparki  978 kapary  978 kapinaz  1005 kapkan  1064 karabacz  1279 karaczan  2027 karafka  689 karawana  1075 karbacz  1279 karhona  1208 karbuz  824 karczma(rz)  825 karczoch  833 kardasz  1089 fcary  1070 Ä:a<MM  1272 ÄsttM^a  1005 kawak  1134 kawiar  851 kawon  1138 kazan  1144 kazna  855 kazmirek  1116
=== TTS kaftan ===
=== DEV cafe/caftan ===
895:Café.  De  l'arabe  «^  kalioua  (prononcé  à  la  turque kahvé),  qui  désigne  la  liqueur  et  non  le  fruité  Calma, dans  Du  Cange,  est  ç^du  vin  blanc  léger  75,  d'après  Ma- ihaeus  Sylvaticus,  médecin  du  xiv*"  siècle.  Le  sens  primitif du  mot  arabe  paraît  aussi  être  vin,  liqueur  apéritive.
896:Dans  la  première  moitié  du  x\f  siècle ,  le  café  était  en- core si  peu  connu  que  le  botaniste  Dominique  Chabré, dans  son  édition  de  YHistoria  plantarum  universalis  de  Jean Bauhin  (iG5o),  se  demande  si  la  liqueur  préparée  par
898:Caftan.  C'est  le  turc  ^Uii  qafuin,  vêtement  d'hon- neur, primitivement  identique,  sans  doute,  à  l'arabe- persan  ^IxÀi*.  hhaftân,  cotte  de  mailles,  armure  mili- taire.
1318:Farde.  Bordage  d'un  navire,  est  identique  à  falqiie  ou l'argue.  Farde,  balle  de  café  moka  pesant  1  85  kilogrammes, est  le  primitif  de  fardeau.  (Voy.  ce  mot.)
1324:étranger  à  leur  langue.  Et  en  effet,  il  semble  au  premier abord  impossible  de  rattacher  »^^  ballol,  à  la  racine :iyi  farad.  Mais  on  va  voir  combien  au  contraire  la  rela- tion est  facile  à  établir.  :>yifard  signifie  7^es  w^a^,  pars  paris altéra,  chacune  des  deux  parties  d'un  objet  unique,  mais double,  d'une  feuille  pliée  en  deux,  par  exemple,  chacun des  deux  côtés  de  la  mâchoire;  'b:>yh farda,  cjui  ne  se  trouve dans  Freytag  qu'avec  le  sens  précité  de  ballot,  sarcina mercium,  marque  de  plus  :  chacun  des  deux  battants  d'une porte  \  chacune  des  deux  étrivières  d'une  selle  ^,  chacun des  deux  arbalétriers  d'une  ferme  (en  espagnol  alfarda^y Quoi  de  plus  naturel  que  de  voir  le  même  mot  signifier et  chacun  des  deux  ballots  formant  la  charge  d'un  cha- meau ???  Lsi  farde  en  effet  est  la  demi-charge  du  chameau, comme  on  le  voit  dans  ce  passage  du  voyageur  La  Roque, cité  par  S.  de  Sacy -^  :  ^  C'est  là  que  les  Arabes  de  la  cam- pagne viennent  apporter  leur  café  dans  de  grands  sacs  de natte  ;  ils  en  mettent  deux  sur  chaque  chameau,  n  Chacune de  ces  balles,  ajoute  l'illustre  orientaliste,  pèse  un  peu moins  de  h  quintaux  (/loo  livres),  c'est-à-dire  le  poids  ci- dessus  indiqué  ])our  la  farde.
1585:casai|iie  moresque;  ital.  gruppn.  De  l'arabe  iC.:^  (Ijoahha. (Voy.  Dozy,  Dkt.  des  vêt.  p.  107.)  cd^ar-dessus  le  caftan, les  Turcs  mettent  une  jitppe  ou  surtout  à  manches  très- courtes.  57  (Niebuhr,  Voy.  en  Arah.  p.  a  10.)
1599:Kava.  Boisson  enivrante  des  Polynésiens.  ç^Il  y  a  iden- tité entre  ce  mot  et  le  mot  havoua,  café  des  Arabes,  qui se  prononce  de  la  même  manière.  Ces  deux  boissons  sont servies  cbaudes.  ^^  (Rienzi^.)  —  Voy.  Café.
1767:Moka.  Espèce  de  café,  tire  son  nom  de  la  ville  du  Yé- men  nommée  en  arabe  l^  Mokhâ.
1994:RiPOPÉE.  En  parcourant  l'article  du  Dictionnaire  de  Lit- tré  sur  ce  mot,  on  voit  que  ripopé  ou  rippopé  (ce  sont  les anciennes  formes  et  le  mot  était  masculin)  signifiait  une  mé- decine à  prendre  en  boisson.  Je  copie  deux  des  exemples cités  :  c^Une  très-bonne  médecine,  boire  devez  du  ripopé» (dansFr.  Michel,  Dict.  d'argot);  «iJ'en  porterai  quatre  prises avec  moi  (d'antimoine),  que  je  veux  faire  prendre  à  M™Ma duchesse  d'Aiguillon,  car  il  n'y  a  point  de  ripopé  c[ui  fasse de  si  bons  effets»  (Voltaire,  Lettr.y  Remarquez  aussi qu'on  a  dit  ripopé  en  parlant  du  marc  de  café  sur  lequel ^n  a  versé  de  l'eau.  Il  me  semble  que,  dans  ces  sens,  n-
2125:Sirop.  \  ieu\  français  essyrot  (xiif  siècle),  ijsserop  (xv" siècle),  provenir',  elssarop,  issarop,  yssarop ,  esp.  xarahe , nxarnbe,  axarave,  axnrope,  jarah,  jarope,  portug.  xaropc (^surrapa,  zurappa,  vin  qui  a  perdu  sa  force ^),  ital.  siroppo, mvoppo,  sciloppo,  bas  lat.  syrupus,  siruppus,  sciruppus.  De l'arabe  vlr^  charâh ,  boisson,  vin,  café,  venant  du  verbe LjJi*  charih,  boire.  On  voit  qu'un  grand  nombre  des  formes citées  ont  conservé  l'article  [ach-charâh);  plusieurs  ont  pu t'tre  faites  sur  cj^^àJI  ach-charoûb ,  boisson.
=== PHN ===
1655:et la mangent souvent en prenant leur café, pour lui donner
2821:CAFÉ, s. m. (a.)
2827:sage du café, apporté du Yémen à la Mekke en 85 9 de l'hé-
2833:çais ne manquèrent pas de condamner l'infusion de café comme
2838:d'une tasse de café mélangé avec du lait. — La dénomination
2839:de café est commune, en France, à la baie du cafier, à son
2841:— Pour constater l'analogie du mot café avec son correspon-
2879:caftan; 8. m. (t.)
2888:écrivent cafetan ont tort de faire trois syllabes d'un mot qui ne
7586:séné, de noix degalle, de nacre de perles, et surtout de café,
```


## [2026-09-06T15:39:09.353Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '1878,1884p' LKT.txt\necho \"=== 2394-2400 ===\"\nsed -n '2394,2400p' LKT.txt | head -c 1500\necho\npython3 - <<'EOF'\nfor f,off,lines in [('LKT.txt',-26,[1882,2398]),('DEV.txt',None,[895,898]),('PHN.txt',None,[2821,2879])]:\n    txt=open(f,encoding='utf-8',errors='replace').read()\n    ls=txt.split('\\n'); leaf=1; ll=[]\n    for l in ls:\n        ll.append(leaf); leaf+=l.count('\\f')\n    for t in lines:\n        print(f,t,'leaf',ll[t-1])\nEOF",
 "description": "Read LKT entries and compute leaves"
}
```


### [2026-09-06T15:39:11.314Z] TOOL RESULT

```
772.  Ar.  haflfäf: 'Schuhmacher'  [zu  ar.  Jiuff  'kurzer  Stie- fel'], tk.  vulgär  kawaf;   hieraus  rum. cavaf   'dass.,    Schuhhändler',  caväfie 'Schusterei'.    [Sain  49.
773.  Ar.  hafif:
'Leicht',  tk.  ebenso  'leicht,  mittellos'; hieraus  rum.  afif  'arm,  armer  Schlucker'.
774.  Pers.  häftäu:
Ebenso  ar.  und  tk.  kaftän  'ein  Gewand' aus  Seide  oder  Brokat,  das  die  Orien- talen über  den  anderen  Kleidungsstücken tragen;  es  wird  mit  einem  Gürtel  ge- halten; die  Ärmel  sind  meistens  länger als  die  Arme  [Dozy  Vetem  162/168]; hieraus  russ.  klruss.  serb.  öech.  poln. haftan  'langschößigerRock' ;  vnm.caftan, sp.  pg.  caftan,  it.  caffetano,  frz.  caftan, cafetan;  engl,  caftan,  kaftan,  ndl.  caf- tan, dtsch.  Kaftan.  [DE  245.  Gorjajew 137.    Bern  SlEtWb  468.
775.  Ar.  liä^a:
'Nötige  Sachen,  Kleider,  Möbel  u.  dergl.'; hieraus  mit  ar.  Art.  sp.  pg.  alhaja,  al- faja,  gewöhnlich  pir.  alhajas  'Gerät, Schmuck,  Kleinod'.  [DE  133.  Eguilaz 155.    ML  3987.
=== 2394-2400 ===
1004.  Pers.  käbrnbä:
'Bernstein'  [aus  pers.  käh  'Stroh'  Horn NpEt  S.  186,  Nr.  840  und  ruhä,  Präsens- stamm des  Vbs.  rubüdän  'rauben,  weg- nehmen' ebenda  S.  135,  Nr.  608,  also eigentlich  'Strohräuber',  wozu  die  wört- liche Übersetzung  gr.  TTTepuYo^öpoq, frz.  tire-jiaille,  dtsch.  Strohzieher  vorliegt ; für  letzteres  vgl.  Martins,  Grundriß  der Pharmakognosie.  Erlangen  1832.  S.370]; hieraus  [außer  mgr.  Kepaß^,  Kdpaiue  und ngr.  KexpiUTidpi]  über  vulg.  tk.  kehribar, kihlibar  mit  Dissimilation  auch  die  slav. Formen  bulg.  kehlibar,  serb.  hilibar; ferner  rum.  chihlibar,  chihlimbar,  chih- rimbar;  m\at.carabe  (im  13.  Jahrhundert belegt),  sp.  it.  carabe,  frz.  carabe  'Bern- stein'; dtsch.  Karabe  (1492  belegt),  dän. rav  [dagegen  scliwed.  bärnsten  wie  auch poln.  bursztyn  aus  dem  Deutschen,  engl. yelloiv  amber,  s.  hier  Nr.  78,  und  russ. jatitar'  aus  dem  Uralaltaischen,  vgl. ung.  gyänta  'Harz',  gyantdr  'Bernstein'].
—  Als  Kuriosum  sei  erwähnt,  daß  käh- rubä  von  einem  Gelehrten  des  18.  Jahr- hunderts zum  Arzte  gemacht  worden ist;  dieser  ist  bei  Jo.  Albertus  Fabricius, Bibliotheca  graeca.  Vol.  XIII.  Ham- burgi  1746  im  Elenchus  medicorum veterum  S.  106  erwähnt,  vgl.  ZDMG XLIII,  381.  —  Vgl.  Jacob,  Neue  Bei- träge zum  Studium  des  kaspisch-balti- sehen  Handels  im  MA.  I.  Neue  Studien den  Bernstein  im  Orient  betreffend
LKT.txt 1882 leaf 89
LKT.txt 2398 leaf 109
DEV.txt 895 leaf 104
DEV.txt 898 leaf 104
PHN.txt 2821 leaf 115
PHN.txt 2879 leaf 117
```


## [2026-09-06T15:39:24.620Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AFM qafsh ===\"; grep -n \"قفش\\|كفش\\|قفاش\" AFM_pages.txt | head -10\necho \"=== AFM khaftan ===\"; grep -n \"خفتان\\|قفطان\" AFM_pages.txt | head -10\necho \"=== TAD ===\"; grep -n \"قفش\\|قفطان\\|خفتان\\|قهوة\" TAD_pages.txt | head -10\necho \"=== ARB mo3rb ===\"; grep -n \"قفش\\|قفطان\\|خفتان\" ARB_mo3rb.txt ARB_abdulraheem.txt | head -10",
 "description": "Grep Arabic loanword dictionaries"
}
```


### [2026-09-06T15:39:24.718Z] TOOL RESULT

```
=== AFM qafsh ===
=== AFM khaftan ===
=== TAD ===
2210:                                      ‫ترى « قفتان » وهوالقاء‬    ‫قفطان ‪-‬‬
=== ARB mo3rb ===
ARB_mo3rb.txt:18245:5 و”القفشليل 6 3 المغرفة ١‏ وهو درضيا ٠.‏ أصله أ لفارسية كفجلاز » ٠‏ 
ARB_mo3rb.txt:19341:5 و”القفش” 1 اشن عرب »وجو المقطوع الا 1 عل 
ARB_mo3rb.txt:19345:إلا ” قفشين ” ومحدفة ٠‏
```


## [2026-09-06T15:39:27.089Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%DA%A9%D9%81%D8%A7%D8%B4/",
 "prompt": "Give the فرهنگ معین (Mo'in) entry for کفاش — its origin tag (e.g. [ع.] Arabic) and definition. Also any Dehkhoda note on its derivation from کفش."
}
```


### [2026-09-06T15:39:32.710Z] TOOL RESULT

```
# کفاش - Mo'in Dictionary Entry

**Origin tag:** (ص . اِ.) — meaning "noun, borrowed" (from Arabic)

**Definition:** "(ک َ فّ ) آن که کفش دوزد و فروشد، کفشدوز" — one who makes and sells shoes; a shoemaker.

## Dehkhoda Note on Derivation

The Dehkhoda dictionary explains that کفاش follows the pattern of صراف (money changer). It's constructed from Persian material (کفش — shoe) but built using an Arabic morphological pattern, similar to how Arabic nouns are formed.
```


## [2026-09-06T15:39:43.864Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== ARB_mo3rb around 19341 ===\"; sed -n '19335,19350p' ARB_mo3rb.txt\necho \"=== ARB_abdulraheem qafsh ===\"; grep -n \"القفش\" ARB_abdulraheem.txt | head\necho \"=== TAD around 2210 ===\"; sed -n '2205,2215p' TAD_pages.txt",
 "description": "Read Arabic sources context"
}
```


### [2026-09-06T15:39:43.947Z] TOOL RESULT

```
=== ARB_mo3rb around 19341 ===


اس باب القأف 


دمع يي 5 
5 و”القفش” 1 اشن عرب »وجو المقطوع الا 1 عل 
7 6 ا ايم 04 
وآضله بالفارسية نو عرب : وفى - حير عر فيد 1 ولية السلام أ أنه لم نجاف 
8 ممه الراك 
إلا ” قفشين ” ومحدفة ٠‏ 
1 و0ك) 
8 31 ” القع “ الذى ا فايس ه “عن كلام أأعرب» قال أبن درب بد 
0 039/7 
أحسية مشمها بارأ س الأقرع . 
ا 00 اسم 
=== ARB_abdulraheem qafsh ===
=== TAD around 2210 ===
  ‫ميةدوع اللاتينية معناها عليةوخْرّانة مخنشب أما االقلفصيوفنانية‬
                                                               ‫هونان‬
                                                                   ‫الي‬
                                          ‫فبلفظ «ماءموه‪ 2‬وافلىلانينى وعحدء‬

                                      ‫ترى « قفتان » وهوالقاء‬    ‫قفطان ‪-‬‬


            ‫رولها؟‪ 1‬معناه متاح‬      ‫إقليد واكليل ومعلاد و ناني‪5‬‬

                                        ‫‪ - 3‬في اللاثينية ‪ 518‬معناه حياس‬
```


## [2026-09-06T15:39:45.292Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%AE%D9%81%D8%AA%D8%A7%D9%86/",
 "prompt": "Give the Dehkhoda and Mo'in entries for خفتان — meaning, origin, and any note that it is the source of Arabic/Turkish قفطان or French caftan. Also note the variant خفدان if mentioned."
}
```


### [2026-09-06T15:39:52.619Z] TOOL RESULT

```
# خفتان (Khaftān) - Dictionary Entries

## Dehkhoda Dictionary Entry
The Dehkhoda entry describes خفتان as "a type of robe/garment" worn during warfare, also called قزاگند in Persian or "qalmaqaci" in Turkish. It notes various related terms including درع (armor), جوشن (cuirass), and تِجفاف. The entry includes classical Persian poetry citations from Ferdowsi and other poets depicting warriors wearing the خفتان in battle.

A variant form **خفدان** is also mentioned in the Dehkhoda entry.

## Mo'in Dictionary Entry
The Mo'ein dictionary provides a more concise definition: "(خَ or خِ) war garment or combat clothing."

## Etymology and Origins
The page presents competing theories:
- **Persian origin theory**: Some sources argue خفتان derives from the Persian verb خفتن (khaftan, "to sleep/recline"), making it a Persian word with Pahlavi roots (xuftan).
- **Turkish/Arabic origin theory**: Other contributors suggest it may derive from Turkish "qāb dūn" or relate to Arabic قفطان (qaftān).

The dictionary does not explicitly confirm whether خفتان is the source of the Arabic قفطان or French caftan, though English translations list "caftan, kaftan" as equivalents.
```


## [2026-09-06T15:39:58.498Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 -c \"\nimport json; d=json.load(open('data/verification/sources/refs_online.json'))\nprint(d['KLN'].get('page_offset')); print(d['KLN'].get('lookup_hint'))\"\ncd data/verification/sources/refs\npython3 - <<'EOF'\nf='KLN_1966.txt'\ntxt=open(f,encoding='utf-8',errors='replace').read()\nls=txt.split('\\n'); leaf=1; ll=[]\nfor l in ls:\n    ll.append(leaf); leaf+=l.count('\\f')\nfor t in [8116,6099,20522]:\n    print(t,'leaf',ll[t-1])\nEOF",
 "description": "Klein page offset and leaves"
}
```


### [2026-09-06T15:40:00.276Z] TOOL RESULT

```
KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
8116 leaf 174
6099 leaf 127
20522 leaf 453
```


## [2026-09-06T15:40:16.688Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==174' KLN_1966.txt | head -3\necho \"...TAIL...\"\nawk 'BEGIN{RS=\"\\f\"} NR==174' KLN_1966.txt | tail -3\necho \"=== leaf 173 head ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==173' KLN_1966.txt | head -2",
 "description": "Look for page numbers in Klein leaf"
}
```


### [2026-09-06T15:40:18.273Z] TOOL RESULT

```
da  (mus.)  —  It.,  dimin.  of coda  (q.v.)
codex,  n.  ■ —  L.  See  code  and  cp.  codicil, codger,  n.  —  A  var.  of  cadger, codicil,  n.,  an  addition  to  a  will.  —  L.  codicillus, ‘a  small  writing  tablet;  an  appendix  to  a  will’, dimin.  of  codex,  gen.  codicis.  See  codex, codicillary,  adj.,  pertaining  to,  or  of  the  nature of,  a  codicil.  —  Late  L.  cddicillaris,  fr.  L.  codi- cillus.  See  prec.  word  and  adj.  suff.  -ary. codification,  n.  —  See  next  word  and  -fication. codify,  tr.  v.,  to  reduce  to  a  code;  to  systema¬ tize.  Formed  fr.  code  with  suff.  -fy. Derivative:  codifi-er ,  n.
codille,  n.,  a  term  at  omber,  used  when  the  game is  lost  by  the  challenging  player.  —  Sp.  codillo, lit.  ‘elbow,  bend,  knee  of  quadrupeds’,  dimin. of  codo ,  ‘elbow,  cubit’,  fr.  L.  cubitus.  See  cubit, codling,  n.,  a  young  cod.  —  Formed  fr.  cod,  ‘a large  fish’,  with  the  dimin.  suff.  -ling, codling,  n.,  a  variety  of  apple.  —  ME.  querdling, corruption  of  F.  cteur  de  lion,  ‘heart  of  lion’. F.  cteur  derives  fr.  L.  cor,  de  fr.  L.  de,  'from, away  from’,  lion  fr.  L.  leonem,  acc.  of  led,  ‘lion’ (see  cordate,  de-  and  lion);  influenced  in  form by  E.  coddle,  ‘to  cook  slowly’,  and  by  nouns ending  in  -ing.
...TAIL...
Derivative:  cognate,  n.
cognation,  n.  —  L.  cognatio,  -dnis,  ‘relationship, connection’,  fr.  cogndtus.  See  prec.  word  and

=== leaf 173 head ===
rnel, berry’,  which  is  prob.  a  foreign  word.  Cp.  the second  element  in  gonococcus  and  in  Chiococca. Cp.  also  cocoon.  Cp.  also  scotch,  ‘to  make  an incision’.  The  word  coccus  was  introduced  into bacteriology  by  the  German  surgeon  Albert Christian  Theodor  Billroth  (1829-94).
Coccus,  n.,  a  genus  of  insects  of  the  family  Coc- cidae.  —  See  prec.  word, coccyg-,  form  of  coccygo-  before  a  vowel, coccygeal,  adj.,  pertaining  to  the  coccyx  ( anat .) —  Formed  with  adj.  suff.  -ai  fr.  Gk.  xoxxui;, gen.  xoxxoyoc.  See  coccyx, coccygo-,  before  a  vowel  coccyg-,  combining  form denoting  the  coccyx  (med.)  —  Fr.  Gk.  xoxxui;, gen.  xGixxOyog.  See  next  word, coccyx,  n.,  the  end  of  the  vertebral  column  in nan  and  in  some  apes ;  the  rudiment  of  a  tail (anat.)  —  Gk.  x6xxu5,  gen.  x6xxuyo<;,  ‘cuckoo;
```


## [2026-09-06T15:40:30.255Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nf='KLN_1966.txt'\ntxt=open(f,encoding='utf-8',errors='replace').read()\nls=txt.split('\\n'); leaf=1; ll=[]\nfor l in ls:\n    ll.append(leaf); leaf+=l.count('\\f')\nimport re\nfor pat in ['cherub','caftan,','coffee,  n','Kaffir,  Kafir']:\n    for i,l in enumerate(ls,1):\n        if pat in l:\n            print(pat,'line',i,'leaf',ll[i-1]); break\nEOF",
 "description": "Calibrate Klein page offset with cherub"
}
```


### [2026-09-06T15:40:32.019Z] TOOL RESULT

```
cherub line 4771 leaf 99
caftan, line 6099 leaf 127
coffee,  n line 8116 leaf 174
Kaffir,  Kafir line 20522 leaf 453
```


## [2026-09-06T15:40:50.251Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SKT coffee ===\"; grep -n -i \"^Coffee\\|Coffee\\.\" SKT.txt | head -5\necho \"=== SKT caftan ===\"; grep -n -i \"caftan\" SKT.txt | head -5\necho \"=== FSD coffee ===\"; grep -n -i \"kahwah\\|qahwah\\|kahveh\" FSD_vol1.txt | head -5\necho \"=== FSD caftan ===\"; grep -n -i \"caftan\" FSD_vol1.txt | head -5\necho \"=== WEB ===\"; grep -n -i \"qahwah\\|kahveh\\|caftan\" WEB_vol1.txt | head -8\necho \"=== HJB ===\"; grep -n -i \"COFFEE\\|caftan\" HJB.txt | head -8",
 "description": "Grep English dictionaries"
}
```


### [2026-09-06T15:40:50.380Z] TOOL RESULT

```
=== SKT coffee ===
3681:Coffee.  (Turk.  -  Arab.)  Turk,  qakvth, —  Arab,  qahweh,  coffee.
=== SKT caftan ===
2610:Caftan,  a  Turkish  ganncui.  (Turk.) Turk    i^aft.in,  a  HrcM.
23665:Turkish :  bey,  caftan,  chouse,  dey,  horde, ketch,  lurkey.
=== FSD coffee ===
=== FSD caftan ===
54481:Picturesque  merchants  and  their  customers,  no  longer  in  the bie  trousers  of  Egypt,  but  the  long  caftans  and  abas  of  Syria. B   ayaud  Tayxob  Lands  of  the  Saracen  ch.  9,  p.  122.  [a.  p.  p.  1SS1.I
54482:[<  Ar.  Qafldn.]  cafTe-tanJ;  kaPtanf,— caPtaned,  a. Wearing  a   caftan.
=== WEB ===
=== HJB ===
2097:shares  in  land,  or  shares  in  a  specula- tion. Thtis  a  one-anna  share  is  ^  of such  ri^ht,  or  a  share  of  |V  ui  the speculation ;  a  four-anTia  is  ^,  and so  on.  In  some  parts  of  India  the term  is  used  as  subdivision  (^)  of the  current  land  measure.  Thu& in  Saugor,  the  anna  =16  riisuf,  and is  itseu  -^  of  a  kcmdia  (EUiot, OI088.  s.v.\  The  term  is  also  some- times applied  colloquially  to  persons of  mixt  parentage.  'Such  a  one  has at  least  2  anncu  of  dark  blood,'  or *  coffee-colour.*  This  may  be  compared with  the  Scotch  expression  that  a person  of  deficient  intellect  'wants twopence  in  the  shilling.'
2808:1873. — **  The  officers  of  his  regiment  .  .  . subscribed  to  buy  the  young  people  a  set  of crockery,  and  a  plated  tea  and  coffee  sendee (got  up  by  dawk  baag^liee  ...  at  not much  more  than  200  per  cent,  in  adyance of  the  Kiglish  price." — The  True  RrfariMTj i57.
3271:BEETLEFAKSE,  n.p.  ''In  some old  Voyages  coins  used  at  Mocha  are  so called.  The  word  is  Bait-tU-fakiha,  the 'Fruit-market,'  the  name  of  a  bazar there."  So  C.  P.  Brown.  The  place is  in  fact  the  Coffee-mart  of  which Hodeida  is  the  port,  from  which  it is  about  30  m.  aistant  inland,  and  4 marches  north  of  Mocha.  And  the name  is  really  Batt-al-F(ikih,  'The House  of  the  Divine,'  from  the  tomb of  the  Saint  Ahmad  Ibn  Musa,  which was  the  nucleus  of  the  place. — (See Rttter,  xii.  872 ;  see  &ho  BEETLE- FACKIE,  MiUmm,  i.  96.)
3272:^'Coffee  .  .  .  g^ws  in  abun- dance at  Beetle-fdckee  .  .  .  and  other parts." — Ovington,  465.
3273:1710. — "They  daily  bring  down  coffee from  the  mountains  to  BetolfiMiny,  which is  not  above  3  leagues  off,  where  there  is a  market  for  it  every  day  of  the  week." — [FrtTich)  Vowtge  to  Arabia  the  Happy,  E.  T., London,  1726,  p.  99.
3274:1770.— "  The  tree  that  produces  the  Coffee ffrowsin  the  territory  of  Betel-fuioi,  a  town belonging  to  Yemen." — Rarinal  (tr.  1777), i.352.
4249:1838.—"  Only  eight  or  ten  loads  (of  coffee) were  imported  this  year,  including  two  loads of  *Kopes*  (see  COPECK),  the  copper  cur- rency of  Russia,  known  in  this  country  by the  name  of  Bnghmkcha.  They  are converted  to  the  same  uses  as  copper." — Report  from  Kabul,  by  A,  Bwmes;  in  Punjab Trade  Report,  App.  p.  iii.
4672:GACOULI,  s.  This  occurs  in  the Apnp.  to  the  Journal  d^Antoine  Galland, at  Constantinople  in  1673  :  "  Dragmes de  Caconli,  drogue  qu'on  use  dans  le CXahue,"  t.e.  in  coffee  (ii.  206).  This is  Pers.  Arab.  Jbdkula  for  Canlamom, as  in  the  quotation  from  Garcia.  We may  remark  that  KdkuUi  was  a  place 4K>mewhere  on  the  GuK  of  Siam, famous  for  its  fine  aloes-wood  (see Ihn  BattUa,  iv.  240-44).  And  a bastard  kind  of  Cardamom  appears to  be  exported  from  Siam,  Amomum scanJthoideSy  Wal.
```


## [2026-09-06T15:40:50.821Z] TOOL CALL #49: WebFetch

```json
{
 "url": "https://www.ahdictionary.com/word/search.html?q=caftan",
 "prompt": "Give the American Heritage Dictionary etymology of 'caftan' verbatim (which languages: Russian, Turkish, Persian?)."
}
```


### [2026-09-06T15:40:55.227Z] TOOL RESULT

```
# Caftan Etymology

According to the American Heritage Dictionary, the etymology traces the word through these languages:

> "Russian _kaftan_, from Ottoman Turkish _qaftān_ (equivalent to Modern Turkish _kaftan_), from Old Turkic _qaptan_"

The entry further notes the Old Turkic word derived from an earlier form combining two elements: a word for "sack" and one meaning "garment."

The etymology does **not** include Persian as a source language in this dictionary entry.
```


## [2026-09-06T15:41:03.508Z] TOOL CALL #50: WebFetch

```json
{
 "url": "https://www.nisanyansozluk.com/kelime/kaftan",
 "prompt": "What etymology does Nişanyan give for Turkish 'kaftan'? Persian خفتان xaftan, or Old Turkic? Quote the entry and dates of first attestation."
}
```


## [2026-09-06T15:41:04.919Z] TOOL CALL #51: WebFetch

```json
{
 "url": "https://www.ahdictionary.com/word/search.html?q=coffee",
 "prompt": "Give the American Heritage Dictionary etymology of 'coffee' verbatim (Italian caffè, Turkish kahve, Arabic qahwa...). Also the entry for 'café' and 'caffeine' if shown."
}
```


### [2026-09-06T15:41:07.816Z] TOOL RESULT

```
I cannot provide the etymology information you're requesting. The web page content shown contains only the header, navigation, and footer of the Nişanyan Sözlük website—it does not include the actual dictionary entry for "kaftan" with its etymology, language origins, or attestation dates.

To access this information, you would need to visit the full dictionary entry on the Nişanyan Sözlük website directly.
```


### [2026-09-06T15:41:09.597Z] TOOL RESULT

```
# Etymology from American Heritage Dictionary

**Coffee:**
The dictionary provides this etymology: "Alteration (influenced by Italian *caffè*, from Ottoman Turkish) of Ottoman Turkish *qahve*, from Arabic *qahwa*"

The page does not include separate entries for "café" or "caffeine"—only the coffee entry is displayed in the content provided.
```


## [2026-09-06T15:41:17.226Z] TOOL CALL #52: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/caftan",
 "prompt": "Give the full etymology of 'caftan' — dates, Turkish qaftan, Persian khaftan, any mention of Russian or Old Turkic qaptan."
}
```


## [2026-09-06T15:41:18.807Z] TOOL CALL #53: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%DA%A9%D8%A7%D9%81%D9%87/",
 "prompt": "Give the Mo'in (فرهنگ معین) entry for کافه — its origin tag (French?) and meaning 'coffee house'. Also Dehkhoda if present."
}
```


### [2026-09-06T15:41:22.841Z] TOOL RESULT

```
# Etymology of Caftan

Based on the Online Etymology Dictionary, here's the full etymology:

**Date of Entry:** The word entered English in the 1590s.

**Language Path:** The term traveled through multiple languages before reaching English. It originated in Persian as *khaftan*, then passed into Turkish as *qaftan* (also used in Arabic), and finally entered English from Turkish.

**Original Meaning:** "Long tunic worn by men in Turkey, Egypt, etc." The garment itself was described as "a kind of long vest tied about the waist, with long sleeves."

**Modern Usage:** The word's application expanded significantly in Western fashion. Its use "as a similar shirt or dress style worn fashionably in the West" is attested from approximately 1955 onward.

**Note:** The provided source does not mention Russian or Old Turkic origins, so those etymological connections cannot be confirmed from this document.
```


### [2026-09-06T15:41:25.130Z] TOOL RESULT

```
# کافه - Mo'in and Dehkhoda Entries

## Farhang-e Mo'in (فرهنگ معین)
**Origin:** French (فر.)
**Meaning:** "جایی که در آن قهوه ، چای ، شیرینی و امثال آن صرف کنند" - a place where coffee, tea, sweets and similar items are served.

## Dehkhoda Dictionary (لغت نامه دهخدا)
**Origin:** French (فرانسوی)
**Definition:** The entry identifies کافه as signifying both the coffee fruit/bean and a coffeehouse - described as "جای عمومی برای نشستن و صرف قهوه و چای و غیره" - a public place for sitting and consuming coffee, tea, and the like.

Both sources confirm the French etymological origin and establish کافه's primary modern meaning as a social establishment serving beverages and refreshments.
```


## [2026-09-06T15:41:33.397Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n 'https://en.wiktionary.org/wiki/%D9%82%D9%87%D9%88%D8%A9' \\\n 'https://www.etymonline.com/word/coffee' \\\n 'https://en.wiktionary.org/wiki/%DA%A9%D9%81%D8%B4' \\\n 'https://en.wiktionary.org/wiki/%D5%AF%D6%85%D5%B7%D5%AB%D5%AF' \\\n 'https://en.wiktionary.org/wiki/%D5%AF%D5%B8%D5%B7%D5%AB%D5%AF' \\\n 'https://abadis.ir/fatofa/%DA%A9%D9%81%D8%A7%D8%B4/' \\\n 'https://abadis.ir/fatofa/%D8%AE%D9%81%D8%AA%D8%A7%D9%86/' \\\n 'https://abadis.ir/fatofa/%DA%A9%D8%A7%D9%81%D9%87/' \\\n 'https://www.ahdictionary.com/word/search.html?q=caftan' \\\n 'https://www.ahdictionary.com/word/search.html?q=coffee' \\\n 'https://www.etymonline.com/word/caftan' ; do\n python3 tools/fetch_source.py \"$u\" --note 'page 233 (Kaffa/coffee, Kafs/shoe, Kaftan) verification' 2>&1 | tail -2\ndone",
 "description": "Archive web sources"
}
```


### [2026-09-06T15:41:43.162Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/bf7293474fe3b7aa.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b86650106fb77a50.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8792252f1529d981.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/fab716e387da9c20.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/7292ba9559f0e555.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/846f497ecadcdcaf.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/12553ea2f6c8f6cb.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/156cef4ee774d29c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8787c4d91a3edfb0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/977c3ba565fdac6d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d60d757509ac4ebd.txt
```


## [2026-09-06T15:41:52.362Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HUB 6605 context ===\"; sed -n '6600,6610p' HUB.txt\necho \"=== HRN Schuh ===\"; grep -n \"Schuh\" HRN.txt | head -10\necho \"=== ARY kafsh ===\"; grep -n \"کفش\" incoming/ARY/ARY_pages.txt | head -5\necho \"=== ARY khaftan ===\"; grep -n \"خفتان\\|قهوه\" incoming/ARY/ARY_pages.txt | head -5\necho \"=== NYB kafs ===\"; grep -n -i \"kafš\\|kafs\\|shoe\" NYB_vol2_glossary.txt | head -8",
 "description": "More local source greps"
}
```


### [2026-09-06T15:41:52.452Z] TOOL RESULT

```
=== HUB 6605 context ===
b) durch v = u in den Verbindungen pers. aft^ ifU
afs, afs: tauf Ritze\ np. taft; »at?f *Erdharz\ np. naft; Khav-
far ein Orbelier (bei Vardan), np. kaftar *Hyane'; ^iwf 'Pech',
arab. pers. zift; drauS Tahne, Banner = np. dirafs, zd.
drafsa-) karatis, karos *Eppich', np. karafs; kausik, kdsik
'Schuh', np. kafsy bal. LW. kaus *Schuh'; ausarak (osarak)
ausgepresster Saft, Most' (Hohelied) = np. afsara,
c) durch X vielleicht in :
Vaxrid ein Armenier (Thorn. 78) = Ovatpgl^rig einPerser
(Agath.) = syr. Gofrlz (4. Jhd.), s. NSldeke, Tab. 223,
'also = pers. Vafric (zu unterscheiden von Vahrid Faust us
=== HRN Schuh ===
8641:994. tnöze 'Schuh', arab. LW. manzaj.
8642:aw. [/^maoc^ mit paiti 'anziehen (sc. Schuhe)*, vergl.
8643:framv/ti' *das Ausziehen (der Schuhe)'; phlv. tnööak
8647:*Schuhe anziehen*.
=== ARY kafsh ===
2810:۳ چم اکثر واژه‌های غیرایرانی اين فهرست: پوشا کد» پوشیدن» کفش. :
11769:افغانی (پشتو) (/4۳0/۸۷): 3اه ,5۸3۸8 ,کفش
=== ARY khaftan ===
1119:تلویزیون کار لبیدهای قهوه‌خانه‌های ایران و افغانستان را آنقدر کساد کرده است که شاید تا چند دهه‌ی
=== NYB kafs ===
1485:ēv-mēk [’ywmwk'] one-shoed, with only one shoe 694, — Paz. émók, v. mok.
1791:compounds, v. separately. — 2. joint, all together, whole: mok % ~ zarrén shoes all golden 294; pat ~ späh in a body 209-10; tö ~ yātūk you are a thorough wizard 2277; all those together (who) 10671; —-ic all 108%; 6 ~ together, pas- sim; — secondarily used as a prev.: ~- butan, —-bavišneh, ~-x"arisnéh, —-pur- sitan, ~ nipistan, to be distinguished from the old prev. ham-, which always appears as han- before a consonant. — Av. OP (1773) hama-. — My emendation PYK-t 2625 is not justified; probably the reading of the MSS is correct: ’YK-m = kü-am for kü ham.
2168:kālpa6 [k*lpt'], kalpu& [k’Ipwt'] shape, external bodily form 892%, 9026, 10127, — MPrs k’lbyd (List 84); Paz. kälbud, Skr. v. kaya sundara (Aog.); NP kalbad, kälbud ‘the body of a man or an animal’, ‘a model, a last for shoes" which is the original sense, the w. being borrowed from Gr xadronddtov..
2585:mók [mwk'] shoe 294, v. also čv-mok. — Paz. mok; NP müq; widely spread as a lw.: Arm moik; Talm, Syr mēgā; Arab müq; cf Av. (837 sq.) paiti-Smuxta- ‘shoed’.
3076:patmóxtan [ptmwhtn'] patmöc- to dress oneself, to put on one's clothes 218. 8515, — Cf Av. (837 sq.) pasti.Smuxta- ‘shoed’; MPrth pdmwatn pdmwe/j- (MHC); MPrs. pymwatn pymwc-; Paz. padmöztan pad- mož-; NP paimostan paimoz-.
```


## [2026-09-06T15:41:53.773Z] TOOL CALL #56: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%DA%A9%D9%81%D8%B4/",
 "prompt": "Give the Mo'in (فرهنگ معین) entry for کفش — its origin tag in brackets (e.g. [په.] Pahlavi) and meaning. Also any Dehkhoda etymological note (Pahlavi kafš)."
}
```


### [2026-09-06T15:42:00.100Z] TOOL RESULT

```
# Mo'in Entry for کفش

**Origin tag:** [په.] (Pahlavi)

**Meaning:** "A type of covering that protects the foot and is usually made of leather; footwear, shoe"

**Related phrases from Mo'in:**
- "Stepping in someone's shoe" = causing them harm
- "Putting feet in one shoe" = insisting on one's opinion
- "Placing shoe before someone" = asking their pardon

**Dehkhoda etymological note:** The word derives from Pahlavi *kafš*, with the root connected to *kaf* (meaning to grasp or contain). The term appears across Middle Persian as *kafšak* and relates to the concept of something that encloses or protects the foot.
```


## [2026-09-06T15:42:08.099Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nfor f,off,lines in [('HUB.txt',10,[6605]),('PHD.txt',21,[422]),('SKT.txt',20,[3681,2610]),('IEC.txt',0,[6876])]:\n    txt=open(f,encoding='utf-8',errors='replace').read()\n    ls=txt.split('\\n'); leaf=1; ll=[]\n    for l in ls:\n        ll.append(leaf); leaf+=l.count('\\f')\n    for t in lines:\n        print(f,t,'leaf',ll[t-1],'printed',ll[t-1]-off)\nEOF",
 "description": "Compute printed pages for HUB, PHD, SKT"
}
```


### [2026-09-06T15:42:09.848Z] TOOL RESULT

```
HUB.txt 6605 leaf 198 printed 188
PHD.txt 422 leaf 72 printed 51
SKT.txt 3681 leaf 110 printed 90
SKT.txt 2610 leaf 81 printed 61
IEC.txt 6876 leaf 277 printed 277
```


## [2026-09-06T15:42:48.088Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BQT v2 qahveh ===\"; grep -n \"قهوه\" BQT_v2_pages.txt | head -5\necho \"=== BQT v3 qahveh ===\"; grep -n \"قهوه\" incoming/BQT/BQT_v3_pages.txt | head -5\necho \"=== RCH qahwah ===\"; grep -n -i \"qahwah\\|kahwah\" RCH.txt | head -5\necho \"=== FVQ qahwa ===\"; grep -n -i \"qahwa\" FVQ_pages.txt | head -5",
 "description": "Grep Borhan/Richardson for qahveh"
}
```


### [2026-09-06T15:42:48.183Z] TOOL RESULT

```
=== BQT v2 qahveh ===
3659:                                           ‫پر لد‬    ‫آب جوشانده مانند قهوه خورند‪ ,‬وخاصت آن‬
16352:‫طرفت بخشد‪ ۷‬ھمجوقلمدان و کبفدان‌رقهوه‌دان‬
39994:   ‫‪,‬اوسنا ‪( ۵۷3۷9 -‬سیاه) » بهلوی ‪ » 2۷915012115‬هندی باستان ‪( ۵۷8026 -‬قهوه‌بی‪:‬‬                   ‫‪۳‬‬
=== BQT v3 qahveh ===
33800:قهوه خوری +
=== RCH qahwah ===
=== FVQ qahwa ===
```


## [2026-09-06T15:42:49.693Z] TOOL CALL #59: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D9%82%D9%87%D9%88%D9%87/",
 "prompt": "Give the Mo'in (فرهنگ معین) entry for قهوه — origin tag in brackets (e.g. [ع.] Arabic) and meanings. Also Dehkhoda's note on its origin (wine? Kaffa?)."
}
```


### [2026-09-06T15:42:56.271Z] TOOL RESULT

```
# قهوه (Mo'in Dictionary Entry)

**Origin tag:** [ع.] (Arabic)

**Meaning:** "نوشیدنی که از جوشاندن ساییدة دانه های بو داده درخت قهوه به دست می آید" (a beverage made by boiling ground roasted beans of the coffee plant)

## Dehkhoda's Etymology Notes

Dehkhoda presents multiple origin theories:

1. **Wine etymology:** The word originally meant a type of wine or strong intoxicating drink that "quickly satisfies the drinker" with potent intoxication.

2. **Appetite suppression theory:** The term derives from the Arabic verb "قها" (qahā), meaning "to lack appetite," since historically this beverage was believed to cause loss of appetite.

3. **Geographic origin:** The word possibly comes from "Kaffa," a region in southwestern Ethiopia where the plant is believed to have originated, with local inhabitants calling it "boun."

Dehkhoda notes these competing explanations without definitively settling which etymology is correct.
```


## [2026-09-06T15:42:59.962Z] TOOL CALL #60: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://abadis.ir/fatofa/%D9%82%D9%87%D9%88%D9%87/' --note 'page 233 root Kaffa, Mo\\047in/Dehkhoda entry for قهوه' 2>&1 | tail -1",
 "description": "Archive abadis qahveh"
}
```


### [2026-09-06T15:43:03.582Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/7f29601f010ffc82.txt
```


## [2026-09-06T15:43:10.826Z] TOOL CALL #61: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg233.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/233.png && echo ok",
 "description": "Copy page image for audit"
}
```


### [2026-09-06T15:43:10.890Z] TOOL RESULT

```
ok
```


## [2026-09-06T15:47:18.150Z] TOOL CALL #62: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p233 && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p233/build.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\n\nout = {\n  \"pdf_page\": 233,\n  \"book_page\": 203,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-06\",\n  \"entries\": []\n}\n\n# ---------------- entry 0: Kaffa ----------------\ne0 = {\n  \"entry\": 0,\n  \"root\": \"Kaffa\",\n  \"verdict\": \"disputed\",\n  \"modern_form\": \"Arabic قَهْوَة qahwa 'wine; coffee'; the Ethiopian place-name Kaffa (Kafa) is only one of two competing explanations and is the less favoured one today\",\n  \"note\": \"Nourai's root box reproduces Klein (KLN s.v. coffee) verbatim: 'fr. Kaffa, Kafa, a district in the southwestern part of Ethiopia. Arab. qahwah orig. meant ‘the plant or drink coming from Kaffa’'. Lokotsch no. 1005 (p.~83) takes the same line ('die Landschaft Kaffa ist die Heimat des Kaffeebaumes'). Modern scholarship, however, prefers the native Arabic derivation: qahwa is a well-attested pre-Islamic/early-Islamic word for 'wine', from the root q-h-w/q-h-y 'to lack appetite' (Ibn Manẓūr: 'it was so named because it surfeits the drinker and takes away his desire'), i.e. it existed in Arabic several centuries before the Kingdom of Kaffa and before coffee-drinking spread from Yemen (c. 1450). The Kaffa link is further weakened by the fact that in Kaffa itself the drink is būno/būn, which Arabic borrowed separately as bunn 'raw coffee' — Klein reports this himself. Etymonline, Wiktionary and Dehkhoda all present the Kaffa story as one hypothesis among several. Hence 'disputed' for the root and for the Arabic node; everything downstream of Arabic qahwa is solid.\",\n  \"note_fa\": \"نورایی ریشه را نام جای حبشی «کفا» (Kaffa) گرفته و این عیناً سخن کلاین و لوکوچ است. امّا پژوهش امروزی بیشتر ریشهٔ عربی را می‌پذیرد: «قهوه» در عربی از ریشهٔ قهی/قها به معنی «بی‌اشتها شدن» ساخته شده و قرن‌ها پیش از رواج قهوه‌نوشی (سدهٔ ۹/۱۵م) به معنی «می» به کار می‌رفته است؛ ابن منظور می‌گوید زیرا نوشنده را سیر می‌کند. افزون بر این، در خود کفا نام این گیاه būno بوده که عربی جداگانه آن را به صورت «بُنّ» وام گرفته است. بنابراین ادعای نورایی دربارهٔ ریشه پذیرفتنی قطعی نیست و دهخدا نیز هر سه فرضیه را کنار هم می‌آورد؛ ولی زنجیرهٔ پس از عربی (ترکی ← ایتالیایی ← فرانسه) درست است.\",\n  \"sources\": [\n    \"https://en.wiktionary.org/wiki/%D9%82%D9%87%D9%88%D8%A9\",\n    \"https://www.etymonline.com/word/coffee\",\n    \"https://www.ahdictionary.com/word/search.html?q=coffee\",\n    \"https://abadis.ir/fatofa/%D9%82%D9%87%D9%88%D9%87/\"\n  ],\n  \"ref_check\": [\n    {\"ref\": \"KLN:309\", \"status\": \"supports\", \"note\": \"Klein 1966 s.v. 'coffee' (KLN_1966.txt line 8116, leaf 174; p = 2·leaf − 34 ≈ 313, calibrated on 'cherub' = KLN:164 at leaf 99 and 'caftan' = KLN:220 at leaf 127 — so Nourai's 309 is within a few pages): 'coffee, n. — It. caffè, fr. Turk. qahve, fr. Arab. qahwah, ‘wine; coffee’, fr. Kaffa, Kafa, a district in the southwestern part of Ethiopia. Arab. qahwah orig. meant ‘the plant or drink coming from Kaffa’. In Kaffa itself the coffee is called bund [read būno] and the Arabs borrowed this word in the form bunn.' This is verbatim Nourai's root box — the reference supports him, but Klein is the very authority modern lexicography has moved away from.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"LKT\", \"where\": \"no. 1005 (leaf 109 ≈ printed p. 83)\", \"stance\": \"supports\", \"note\": \"Lokotsch: ar. qahwa ‘Wein’ ‘doch stammt das Wort sicherlich wie die Sache selbst aus der Umgebung Abessiniens: die Landschaft Kaffa ist die Heimat des Kaffeebaumes, der von Šaiḥ aš-ŠĀḎILĪ nach Südarabien eingeführt wurde’; then tk. kahwe > it. cahue, caffè, frz. sp. pg. café, engl. coffee, ndl. koffie, dtsch. Kaffee.\"},\n    {\"src\": \"DEV\", \"where\": \"s.v. Café (DEV.txt line 895, leaf 104 ≈ printed p. 74–78)\", \"stance\": \"partial\", \"note\": \"Devic: 'Café. De l’arabe قهوة kahoua (prononcé à la turque kahvé)… Le sens primitif du mot arabe paraît aussi être vin, liqueur apéritive.' Devic gives no Ethiopian etymon at all — he treats qahwa as an Arabic word for wine.\"},\n    {\"src\": \"SKT\", \"where\": \"s.v. Coffee (leaf 110 = printed p. 90)\", \"stance\": \"partial\", \"note\": \"Skeat: 'Coffee. (Turk. – Arab.) Turk. qahveh, – Arab. qahweh, coffee.' — stops at Arabic, no Kaffa.\"},\n    {\"src\": \"AHD\", \"where\": \"online 5th ed. s.v. coffee\", \"stance\": \"contradicts\", \"note\": \"'Alteration (influenced by Italian caffè, from Ottoman Turkish) of Ottoman Turkish qahve, from Arabic qahwa' — the modern AHD stops at Arabic and drops the Ethiopian etymon that the 1975/76 edition (Nourai's AHD:258) still carried.\"},\n    {\"src\": \"MON\", \"where\": \"s.v. قهوه (abadis.ir, Farhang-e Mo'in + Dehkhoda)\", \"stance\": \"partial\", \"note\": \"Mo'in tags قهوه simply '[ع.]' (Arabic); Dehkhoda lists three rival origins — 'wine', the verb قها 'to lack appetite', and the district of Kaffa where the locals call it بون — without deciding.\"}\n  ],\n  \"nodes\": []\n}\n\ne0[\"nodes\"] = [\n {\n  \"id\": 1, \"lang\": \"Arabic\", \"words\": \"qahwah\",\n  \"verdict\": \"disputed\",\n  \"derivation\": \"Arabic قَهْوَة qahwa. Nourai (after Klein) makes it a nisba-less denominal of the Ethiopian district Kaffa, 'the plant or drink coming from Kaffa'. Against this: qahwa is used for 'wine, a strong drink' by pre-Islamic and early Abbasid poets, i.e. some 500–700 years before coffee reached Arabia (Yemen, c. 1450, and Mecca c. 1510), and Arab lexicographers derive it from the root q-h-w/q-h-y 'to have no appetite' (Ibn Manẓūr, Lisān al-ʿArab: so named because it takes away the drinker's desire for food). When the beverage arrived the existing word for an intoxicant was simply transferred to it. The genuine Kaffa word did enter Arabic, but separately and in a different shape: Kaffa būno > Arabic بُنّ bunn 'raw coffee bean' (Klein records this in the same entry). A phonetic difficulty also stands: Kaffa would not regularly yield qahwa (k > q, ff > hw). Verdict disputed: the word is Arabic, the referent is Ethiopian.\",\n  \"derivation_fa\": \"عربی «قهوة». نورایی به پیروی کلاین آن را برگرفته از نام ناحیهٔ کفا در جنوب غربی حبشه می‌داند. امّا «قهوة» در شعر جاهلی و عبّاسی به معنی «می» آمده، یعنی چند قرن پیش از آنکه دانهٔ قهوه از یمن به حجاز برسد؛ لغویان عرب آن را از ریشهٔ قهی/قها «بی‌اشتها کردن» گرفته‌اند. واژهٔ بومی کفا یعنی būno جداگانه و به صورت «بُنّ» وارد عربی شده است. پس پژوهش امروزی این پیوند را رد می‌کند: واژه عربی است، گیاه حبشی.\",\n  \"sources\": [\"https://en.wiktionary.org/wiki/%D9%82%D9%87%D9%88%D8%A9\", \"https://www.etymonline.com/word/coffee\"],\n  \"ref_check\": [{\"ref\": \"(none on this node)\", \"status\": \"not_checked\", \"note\": \"Nourai gives no citation on the Arabic box; the root box's KLN:309 covers it and was checked there (Klein s.v. coffee).\"}],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"s.v. coffee (leaf 174)\", \"stance\": \"supports\", \"note\": \"'fr. Arab. qahwah, ‘wine; coffee’, fr. Kaffa… Arab. qahwah orig. meant ‘the plant or drink coming from Kaffa’.'\"},\n    {\"src\": \"DEV\", \"where\": \"s.v. Café (leaf 104)\", \"stance\": \"contradicts\", \"note\": \"'Le sens primitif du mot arabe paraît aussi être vin, liqueur apéritive' — Devic derives nothing from Kaffa.\"},\n    {\"src\": \"FVQ\", \"where\": \"grep 'qahwa' in FVQ_pages.txt\", \"stance\": \"silent\", \"note\": \"Jeffery has no entry — qahwa is not a Qur’anic word, so no help either way.\"}\n  ]\n },\n {\n  \"id\": 2, \"lang\": \"Persian\", \"words\": \"qahveh «قهوه»\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"New Persian قهوه qahve is a straight Arabic loan, taken over with its Arabic spelling; the Arabic feminine ending -a(t) is rendered by Persian -e as in جمعة > جمعه, قلعة > قلعه. The borrowing is late — coffee-drinking reaches Iran under the Safavids in the later 16th century (the qahve-xāne is a Safavid institution) — so the word entered Persian directly from Arabic usage, not through Turkish, and Persian kept the Arabic q- (unlike Turkish kahve). Meaning narrowed from Arabic 'wine; coffee' to 'coffee' only.\",\n  \"derivation_fa\": \"«قهوه» در فارسی وام‌واژه‌ای عربی است که با همان املای عربی پذیرفته شده و تاء تأنیث عربی در فارسی به هٔ غیرملفوظ بدل شده است (مانند جمعة > جمعه). وام‌گیری متأخر است و به دورهٔ صفوی (سدهٔ ۱۰ هـ.ق) بازمی‌گردد که قهوه‌خانه در ایران رواج یافت؛ قاف عربی در فارسی مانده (برخلاف ترکی kahve). معین نیز آن را [ع.] می‌داند؛ ادعای نورایی درست است.\",\n  \"sources\": [\"https://abadis.ir/fatofa/%D9%82%D9%87%D9%88%D9%87/\", \"https://en.wiktionary.org/wiki/%D9%82%D9%87%D9%88%D8%A9\"],\n  \"ref_check\": [{\"ref\": \"MON:2756\", \"status\": \"supports\", \"note\": \"Mo'in's lexicon entry قهوه (read on abadis.ir, which reproduces the Farhang-e Mo'in text): tag '[ع.]' = Arabic, gloss 'نوشیدنی که از جوشاندن ساییدهٔ دانه‌های بو دادهٔ درخت قهوه به دست می‌آید'. Exactly Nourai's arrow (Arabic > Persian). The 6-vol. page number 2756 cannot be checked — only the 2-vol. abridgement is scanned — but the entry is where Nourai says it is alphabetically.\"}],\n  \"consulted\": [\n    {\"src\": \"MON\", \"where\": \"s.v. قهوه via abadis.ir\", \"stance\": \"supports\", \"note\": \"'[ع.]' Arabic origin tag; Dehkhoda on the same page adds the wine/Kaffa discussion.\"},\n    {\"src\": \"BQT\", \"where\": \"grep قهوه in BQT_v2_pages.txt / BQT_v3_pages.txt\", \"stance\": \"silent\", \"note\": \"Borhan-e Qate' has no headword قهوه; only incidental occurrences (‘آب جوشانده مانند قهوه خورند’, v2 line 3659) — the 17th-c. Borhan treats it as a foreign drink, not a Persian word.\"},\n    {\"src\": \"RCH\", \"where\": \"grep qahwah/kahwah in RCH.txt\", \"stance\": \"silent\", \"note\": \"Richardson's transliteration scheme in this OCR does not surface the entry; no result.\"}\n  ]\n },\n {\n  \"id\": 3, \"lang\": \"Turkish\", \"words\": \"qahve'\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"Ottoman Turkish قهوه kahve, borrowed from Arabic qahwa in the first half of the 16th century, when coffee-houses spread from Damascus and Aleppo to Istanbul (the first ones there are dated c. 1550). Turkish regularly de-emphatises Arabic q- to k- and renders the final -a(t) as -e by vowel harmony: qahwa > kahve. Nourai's transliteration 'qahve’' with a final apostrophe is his notation for the -e, not a glottal stop. From Ottoman Turkish the word passed to Venetian traders — the Italian forms cahue (Pietro della Valle) and caffè are attested at the turn of the 16th/17th c.\",\n  \"derivation_fa\": \"ترکی عثمانی kahve از عربی «قهوة» وام گرفته شده است؛ قاف عربی در ترکی به k بدل شده و تاء تأنیث بر پایهٔ همگونی واکه‌ای ترکی به -e تبدیل شده است. این وام‌گیری در نیمهٔ نخست سدهٔ ۱۶م میلادی رخ داد، آنگاه که قهوه‌خانه‌ها از دمشق و حلب به استانبول رسید. ادعای نورایی درست است (لوکوچ، اسکیت، کلاین).\",\n  \"sources\": [\"https://www.etymonline.com/word/coffee\", \"https://www.ahdictionary.com/word/search.html?q=coffee\"],\n  \"ref_check\": [{\"ref\": \"AHD:258\", \"status\": \"partial\", \"note\": \"The 1975/76 AHD New College Edition p.258 is not open online (IA copies are lending-only and the local AHD file is only the Watkins IE-root appendix). The current AHD text for the same headword reads: 'Alteration (influenced by Italian caffè, from Ottoman Turkish) of Ottoman Turkish qahve, from Arabic qahwa' — it supports Arabic > Turkish > Italian, i.e. Nourai's nodes 1→3→4, but it does not carry the Kaffa etymon Nourai attributes to it.\"}],\n  \"consulted\": [\n    {\"src\": \"LKT\", \"where\": \"no. 1005 (leaf 109)\", \"stance\": \"supports\", \"note\": \"'tk. kahwe; hieraus um die Wende des 16. und 17. Jahrhunderts in Europa eingeführt als it. cahue … caffè, frz. sp. pg. café'; and no. 1005 note: 'um 1550 wurden von Damaskus und Aleppo aus die ersten Kaffeehäuser in Konstantinopel eingerichtet'.\"},\n    {\"src\": \"SKT\", \"where\": \"s.v. Coffee (printed p. 90)\", \"stance\": \"supports\", \"note\": \"'Coffee. (Turk. – Arab.) Turk. qahveh, – Arab. qahweh, coffee.'\"},\n    {\"src\": \"KLN\", \"where\": \"s.v. cafe / coffee (leaves 127, 174)\", \"stance\": \"supports\", \"note\": \"'café … F., fr. It. caffè, fr. Turk. qahve, fr. Arab. qahvah'.\"}\n  ]\n },\n {\n  \"id\": 4, \"lang\": \"Italian\", \"words\": \"\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"The empty box stands for Italian caffè, the Venetian-mediated form of Ottoman kahve. Venice, the chief European entrepôt for Levantine goods, met the drink by 1615; Pietro della Valle's Viaggi (Rome ed. I, 110) still writes cahue, and the settled form caffè appears in the same generation, the Turkish -e being reinterpreted as the Italian stressed -è. From Italian the word radiates to French, Spanish and Portuguese café and, through Dutch koffie, to English and German.\",\n  \"derivation_fa\": \"جعبهٔ خالی یعنی ایتالیایی caffè. ونیز دروازهٔ کالاهای شام و عثمانی به اروپا بود؛ نخست به صورت cahue (در سفرنامهٔ پییترو دلاواله) و سپس caffè ثبت شده است؛ -e ترکی در ایتالیایی به -è کشیدهٔ تکیه‌دار بدل شده است. ادعای نورایی درست است.\",\n  \"sources\": [\"https://www.etymonline.com/word/coffee\", \"https://www.ahdictionary.com/word/search.html?q=coffee\"],\n  \"ref_check\": [{\"ref\": \"(none on this node)\", \"status\": \"not_checked\", \"note\": \"Nourai leaves the Italian box uncited; the chain Turkish > Italian is covered by KLN:309 / AHD:258 on the neighbouring boxes and was checked there.\"}],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"s.v. coffee, cafe (leaves 174, 127)\", \"stance\": \"supports\", \"note\": \"'coffee, n. — It. caffè, fr. Turk. qahve'; 'café … F., fr. It. caffè'.\"},\n    {\"src\": \"LKT\", \"where\": \"no. 1005\", \"stance\": \"supports\", \"note\": \"'it. cahue [Pietro della Valle, Viaggi (ediz. di Roma) I, 110], caffè, frz. sp. pg. café'.\"},\n    {\"src\": \"AHD\", \"where\": \"online s.v. coffee\", \"stance\": \"supports\", \"note\": \"'influenced by Italian caffè, from Ottoman Turkish'.\"}\n  ]\n },\n {\n  \"id\": 5, \"lang\": \"French\", \"words\": \"cafe'\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"French café, borrowed from Italian caffè in the mid-17th century, with the Italian final stressed -è written -é. Marseille and then Paris took the drink from Levantine and Italian merchants in the 1650s–60s (the first French coffee-house is usually placed at Marseille, 1660; the Procožio/Procope in Paris 1686). French developed the second sense Nourai records — café as the establishment as well as the beverage — by metonymy in the 18th century, and it is this metonymic sense that Persian and English later borrow.\",\n  \"derivation_fa\": \"فرانسه café از ایتالیایی caffè گرفته شده و -è ایتالیایی به -é فرانسه بدل شده است. قهوه در دههٔ ۱۶۵۰ از راه بازرگانان شامی و ایتالیایی به مارسی و پاریس رسید. معنی دوم یعنی «قهوه‌خانه» تحول معنایی مجازی در خود فرانسه است و همین معنی بعدها به فارسی و انگلیسی رفته است.\",\n  \"sources\": [\"https://www.etymonline.com/word/coffee\"],\n  \"ref_check\": [{\"ref\": \"(none on this node)\", \"status\": \"not_checked\", \"note\": \"no citation on the French box; the Italian > French step is stated in KLN s.v. café (checked under node 7's KLN:309) and in Lokotsch no. 1005.\"}],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"s.v. café (leaf 127)\", \"stance\": \"supports\", \"note\": \"'café, n., 1) coffee; 2) coffeehouse; restaurant. — F., fr. It. caffè, fr. Turk. qahve, fr. Arab. qahvah.' — both of Nourai's glosses.\"},\n    {\"src\": \"PHN\", \"where\": \"s.v. CAFÉ (PHN.txt line 2821, leaf 115 ≈ printed p. 84)\", \"stance\": \"supports\", \"note\": \"Pihan's article on café traces the French word to the Arabic/Turkish word and discusses 'l'usage du café, apporté du Yémen à la Mekke en 859 de l'hégire'.\"},\n    {\"src\": \"LKT\", \"where\": \"no. 1005\", \"stance\": \"supports\", \"note\": \"'frz. sp. pg. café' listed as continuations of it. caffè.\"}\n  ]\n },\n {\n  \"id\": 6, \"lang\": \"Persian\", \"words\": \"kâfeh «کافه»\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"Persian کافه kāfe is a 20th-century loan straight from French café, in the metonymic sense 'coffee-house, refreshment place'; the French acute -é is rendered by Persian -ه and the initial k- is written with ک (not ق), which alone shows it is not a re-borrowing of Arabic qahwa but a European word. It is thus a doublet of the older قهوه qahve in the same language — the same Arabic word returning to Persian after a detour through Turkish, Italian and French. Mo'in tags it '[فر.]' = French.\",\n  \"derivation_fa\": \"«کافه» وام‌واژه‌ای سدهٔ بیستم از فرانسه café به معنی «قهوه‌خانه» است؛ -é فرانسه به هٔ بیان فارسی بدل شده و نوشتن آن با «ک» (نه «ق») نشان می‌دهد وام‌گیری از اروپاست نه دوباره از عربی. بدین‌سان «کافه» و «قهوه» در فارسی دوگانه (doublet) اند: یک واژه که یک‌بار از عربی و یک‌بار پس از گذر از ترکی و ایتالیایی و فرانسه بازگشته است. ادعای نورایی درست است.\",\n  \"sources\": [\"https://abadis.ir/fatofa/%DA%A9%D8%A7%D9%81%D9%87/\"],\n  \"ref_check\": [{\"ref\": \"MON:2851\", \"status\": \"supports\", \"note\": \"Farhang-e Mo'in s.v. کافه (read via abadis.ir): origin tag '(فر.)' = French, gloss 'جایی که در آن قهوه، چای، شیرینی و امثال آن صرف کنند' — exactly Nourai's 'coffee house' from French. The 6-vol. page 2851 itself is unverifiable (no scan of that edition).\"}],\n  \"consulted\": [\n    {\"src\": \"MON\", \"where\": \"s.v. کافه via abadis.ir\", \"stance\": \"supports\", \"note\": \"'(فر.)' French; 'a place where coffee, tea, sweets and the like are served'.\"},\n    {\"src\": \"BQT\", \"where\": \"grep کافه in BQT volumes\", \"stance\": \"silent\", \"note\": \"Borhan-e Qate' (1652) predates the loan; no such headword, as expected for a modern Europeanism.\"}\n  ]\n },\n {\n  \"id\": 7, \"lang\": \"English\", \"words\": \"coffee, cafe', caffeine\",\n  \"verdict\": \"plausible\",\n  \"derivation\": \"Two of the three words fit the arrow, one does not. (a) cafe: English café 'coffee-house, restaurant' is first recorded 1802 and is indeed taken straight from French café — arrow correct. (b) caffeine: coined 1830 from German Kaffein (F. F. Runge, 1819–20) on Kaffee, and reaching English through French caféine (fr. café + -ine); French mediation is real, so the arrow holds. (c) coffee, however, is a century and a half older (chaoua 1598, coffee c. 1600) and did NOT come through French: the standard account is Dutch koffie (the Dutch were the carriers of the Levant trade) reinforced by Italian caffè, both from Ottoman kahve; Klein, whom Nourai cites here, says flatly 'coffee, n. — It. caffè, fr. Turk. qahve', with no French link, and lists café and caffeine as separate French borrowings. Node marked plausible: the French box is the right parent for two of the three words but the wrong one for coffee itself.\",\n  \"derivation_fa\": \"از سه واژهٔ انگلیسی دو تا با نمودار نورایی می‌خواند و یکی نه. cafe (۱۸۰۲م) و caffeine (۱۸۳۰م، از راه caféine فرانسه و Kaffein آلمانی) راستی از فرانسه گرفته شده‌اند؛ امّا coffee یک و نیم سده کهن‌تر است (صورت chaoua در ۱۵۹۸ و coffee حدود ۱۶۰۰) و از راه هلندی koffie و ایتالیایی caffè به انگلیسی رسیده، نه از فرانسه. جالب آنکه خود کلاین — مرجعی که نورایی در همین جعبه گواه گرفته — می‌گوید coffee از ایتالیایی است. پس این پیوند با احتیاط پذیرفتنی است.\",\n  \"sources\": [\"https://www.etymonline.com/word/coffee\", \"https://www.ahdictionary.com/word/search.html?q=coffee\"],\n  \"ref_check\": [\n    {\"ref\": \"KLN:309\", \"status\": \"partial\", \"note\": \"Klein 1966 s.v. coffee (leaf 174) gives 'It. caffè, fr. Turk. qahve' — no French stage — while his separate entries 'café … F., fr. It. caffè' and 'caffeine … F. caféine, fr. café' (leaf 127) do route those two through French. So Klein supports two thirds of the box and contradicts the third.\"},\n    {\"ref\": \"AHD:187\", \"status\": \"not_checked\", \"note\": \"Nourai's second citation on this box is AHD:258 (not 187); the 1975/76 AHD page is not accessible (lending-only IA scans; the local AHD file is the Watkins IE-root appendix only). The current AHD s.v. coffee gives Italian/Ottoman Turkish and no French.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"SKT\", \"where\": \"s.v. Coffee (printed p. 90)\", \"stance\": \"contradicts\", \"note\": \"'Coffee. (Turk. – Arab.)' — Skeat marks the immediate source as Turkish, not French.\"},\n    {\"src\": \"LKT\", \"where\": \"no. 1005\", \"stance\": \"contradicts\", \"note\": \"Lokotsch lists 'engl. coffee, ndl. koffie, dtsch. Kaffee' in the same breath as 'frz. sp. pg. café', i.e. as parallel continuations of Italian, not as descendants of French.\"},\n    {\"src\": \"KLN\", \"where\": \"s.vv. coffee / café / caffeine\", \"stance\": \"partial\", \"note\": \"as quoted in ref_check.\"}\n  ]\n }\n]\nout[\"entries\"].append(e0)\njson.dump(out, open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p233/part0.json','w'), ensure_ascii=False, indent=2)\nprint(\"ok\", len(e0[\"nodes\"]))\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p233/build.py",
 "description": "Build entry 0 JSON"
}
```


### [2026-09-06T15:47:20.115Z] TOOL RESULT

```
ok 7
```


## [2026-09-06T15:49:41.023Z] TOOL CALL #63: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p233/build1.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\ne1 = {\n  \"entry\": 1,\n  \"root\": \"Kafš\",\n  \"verdict\": \"confirmed\",\n  \"modern_form\": \"Middle Persian kafš [kpš] 'shoe' (also kafšag), further origin uncertain\",\n  \"note\": \"The root box is right in substance: MacKenzie's Concise Pahlavi Dictionary p.51 has 'kafš, ~ag [kpš, -k' | N kafš] shoe. ~gar [-k'] shoemaker', and the same dictionary's English index lists 'shoe kafš, mōg, mōzag'. Nourai's gloss 'shoe, boot' is a shade wide — Pahlavi distinguishes kafš 'shoe' from mōg/mōzag 'boot' — but not wrong. Where the chart is silent is on what lies behind the Pahlavi word: Wiktionary and Hasandust leave the further origin uncertain (a link with Old Armenian կապ kap and PIE *kap- 'to seize, hold' is floated but 'formal details unclear'); Mann (IEC 1628) sets up an etymon kaukis, ios covering Per. kafš, Gk. kaukís and Arm. kawšik. Since Nourai starts from Pahlavi and claims nothing older, the root box stands as printed.\",\n  \"note_fa\": \"ریشهٔ نورایی درست است: مکنزی در فرهنگ کوچک پهلوی (ص ۵۱) «kafš, kafšag [kpš] کفش» و «kafšgar کفشگر» را آورده است. تنها نکته آنکه در پهلوی kafš «کفش» با mōg/mōzag «موزه، چکمه» فرق دارد، پس افزودن «boot» به معنی اندکی گشاده است. دربارهٔ خاستگاه کهن‌تر این واژه، ویکی‌واژه و حسن‌دوست آن را نامعلوم می‌دانند (پیوند احتمالی با ریشهٔ هندواروپایی *kap- «گرفتن» قطعی نیست)؛ مان (IEC ص ۱۶۲۸) صورت kaukis را برای فارسی kafš و یونانی kaukís و ارمنی kawšik بازسازی کرده است. چون نورایی از پهلوی آغاز می‌کند و ادعای کهن‌تری ندارد، جعبهٔ ریشه پذیرفته است.\",\n  \"sources\": [\"https://en.wiktionary.org/wiki/%DA%A9%D9%81%D8%B4\"],\n  \"ref_check\": [{\"ref\": \"MON:3005\", \"status\": \"supports\", \"note\": \"Mo'in's lexicon s.v. کفش (read via abadis.ir, which prints the Farhang-e Mo'in text) carries the origin tag '[په.]' = Pahlavi and the gloss 'پوششی که پا را حفظ می‌کند و معمولاً از چرم است' — exactly Nourai's Pahlavi root. The print page 3005 of the 6-vol. edition cannot be checked (only the 2-vol. abridgement is scanned), but the claim is verified from the same author's text.\"}],\n  \"consulted\": [\n    {\"src\": \"PHD\", \"where\": \"p. 51 s.v. kafš (PHD.txt line 422, leaf 72; leaf = printed + 21)\", \"stance\": \"supports\", \"note\": \"MacKenzie: 'kafš, ~ag [kpš, -k' | N kafš] shoe. ~gar [-k'] shoemaker.' — Pahlavi kafš, New Persian kafš, exactly the arrow.\"},\n    {\"src\": \"NYB\", \"where\": \"grep kafš/kafs in NYB_vol2_glossary.txt\", \"stance\": \"silent\", \"note\": \"Nyberg's glossary to his Pahlavi texts has mōk 'shoe' (p. s.v. mōk, 'Paz. mōk; NP mūq; Arm moik; Syr mēqā; Arab mūq') but no kafš — the word does not occur in his corpus; no evidence either way.\"},\n    {\"src\": \"MON\", \"where\": \"s.v. کفش via abadis.ir\", \"stance\": \"supports\", \"note\": \"'[په.]' Pahlavi tag; Dehkhoda on the same page: 'از پهلوی kafš'.\"},\n    {\"src\": \"HRN\", \"where\": \"grep kafš / 'Schuh' in HRN.txt\", \"stance\": \"silent\", \"note\": \"Horn's Grundriss has no number for kafš (his 'Schuh' entry, no. 994, is mōze, an Arabic loan); the word is simply not treated.\"}\n  ],\n  \"nodes\": [\n   {\n    \"id\": 1, \"lang\": \"Persian\", \"words\": \"kafš «کفش»\",\n    \"verdict\": \"confirmed\",\n    \"derivation\": \"New Persian کفش kafš continues Middle Persian kafš [kpš] unchanged — a rare case where the Pahlavi and the New Persian shapes are identical, because the cluster -fš is stable and there was no final vowel to lose (the by-form kafšag > *kafša did not survive). MacKenzie prints '[kpš | N kafš]', i.e. he himself equates the two. The derivative kafšgar > New Persian کفشگر kafšgar 'shoemaker' shows the same continuity. Mo'in tags the word '[په.]' (Pahlavi).\",\n    \"derivation_fa\": \"«کفش» فارسی نو دنبالهٔ مستقیم فارسی میانهٔ kafš [kpš] است و صورت آن هیچ دگرگونی نیافته، زیرا خوشهٔ -فش پایدار است و واکهٔ پایانی‌ای در کار نبوده که بیفتد (صورت kafšag پهلوی در فارسی نو نمانده است). مکنزی خود می‌نویسد «[kpš | N kafš]». مشتق kafšgar پهلوی نیز همان «کفشگر» فارسی است. معین این واژه را [په.] می‌داند؛ ادعای نورایی درست است.\",\n    \"sources\": [\"https://en.wiktionary.org/wiki/%DA%A9%D9%81%D8%B4\", \"https://abadis.ir/fatofa/%DA%A9%D9%81%D8%B4/\"],\n    \"ref_check\": [{\"ref\": \"MON:3005\", \"status\": \"supports\", \"note\": \"same Mo'in entry as the root: کفش '[په.]' — Pahlavi > Persian, precisely Nourai's arrow.\"}],\n    \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"p. 51 s.v. kafš\", \"stance\": \"supports\", \"note\": \"'kafš, ~ag [kpš, -k' | N kafš] shoe' — MacKenzie's own '| N kafš' is the arrow.\"},\n      {\"src\": \"PLA\", \"where\": \"p. 219 s.v. qafš (PLA_pages.txt line 12286, leaf 234)\", \"stance\": \"supports\", \"note\": \"Asbaghi: 'قفش qafš: “Schuhe” < pers. کفش kafš > MP kafš 6' with note 6 = 'Mackenzie s. v.' — Persian kafš explicitly derived from MP kafš.\"},\n      {\"src\": \"MON\", \"where\": \"s.v. کفش via abadis.ir\", \"stance\": \"supports\", \"note\": \"'[په.]'.\"}\n    ]\n   },\n   {\n    \"id\": 2, \"lang\": \"Arabic\", \"words\": \"\",\n    \"verdict\": \"confirmed\",\n    \"derivation\": \"The empty Arabic box stands for قَفْش qafš 'shoes, slippers', the Arabised form of Persian kafš. The adaptation is the regular one for Persian k- before a back vowel in classical Arabisation: k > q (as in kandah > qandah, kūpāl > qufl in the same dictionary), with the consonant cluster kept. The word is old enough to be listed among the muʿarrab: al-Jawāliqī's al-Muʿarrab has an article 'القفش' in bāb al-qāf ('وأصله بالفارسية …'), and a ḥadīth is quoted in which the Prophet is said to have worn nothing but 'qafšayn'. Asbaghi confirms the direction of borrowing (Persian > Arabic), not the reverse.\",\n    \"derivation_fa\": \"جعبهٔ خالی عربی همان «قَفْش» است، یعنی معرّبِ «کفش» فارسی. در معرّب‌سازی کهن، کافِ فارسی پیش از واکهٔ پسین معمولاً به قاف بدل می‌شود و خوشهٔ صامت نگه داشته می‌شود. این واژه در «المعرّب» جوالیقی در باب القاف با تصریح «وأصله بالفارسیة» آمده و حدیثی نیز نقل شده که پیامبر جز «قفشین» چیزی نپوشید. اصبغی (فارسی‌واژه‌های عربی، ص ۲۱۹) نیز سویِ وام‌گیری را از فارسی به عربی می‌داند. ادعای نورایی درست است.\",\n    \"sources\": [\"https://en.wiktionary.org/wiki/%DA%A9%D9%81%D8%B4\"],\n    \"ref_check\": [{\"ref\": \"MON:3005\", \"status\": \"partial\", \"note\": \"Mo'in's کفش entry (via abadis.ir) gives the Pahlavi origin but the online text does not reproduce the note on the Arabic derivative; the Arabised قفش is however documented independently (see consulted). The print page 3005 is not scanned.\"}],\n    \"consulted\": [\n      {\"src\": \"PLA\", \"where\": \"p. 219 (leaf 234) s.v. قفش\", \"stance\": \"supports\", \"note\": \"Asbaghi, Persische Lehnwörter im Arabischen: 'قفش qafš: “Schuhe” < pers. کفش kafš > MP kafš' — an Arabic word taken from Persian, exactly Nourai's arrow.\"},\n      {\"src\": \"ARB\", \"where\": \"al-Jawāliqī, al-Muʿarrab, bāb al-qāf (ARB_mo3rb.txt lines 19341-19345)\", \"stance\": \"supports\", \"note\": \"'و«القفش» … وأصله بالفارسیة … وفي الحديث … أنه لم يخلّف إلا “قفشين” ومخدّة' — the classical Arabic muʿarrab lexicon lists al-qafš as a Persian word.\"},\n      {\"src\": \"AFM\", \"where\": \"grep قفش / كفش in AFM_pages.txt\", \"stance\": \"silent\", \"note\": \"Addi Shir's al-Alfāẓ al-fārisiyya al-muʿarraba has no article at that spelling in this OCR.\"},\n      {\"src\": \"KLN\", \"where\": \"grep qafsh in KLN\", \"stance\": \"silent\", \"note\": \"no English derivative, so Klein does not treat the word.\"}\n    ]\n   },\n   {\n    \"id\": 3, \"lang\": \"Persian\", \"words\": \"kaffâš «کفّاش»\",\n    \"verdict\": \"plausible\",\n    \"derivation\": \"کفّاش kaffāš 'shoemaker' is the Arabic nomen agentis pattern faʿʿāl applied to the stem kafš/qafš — the same formation as صرّاف ṣarrāf, نجّار najjār — with gemination of the second radical and the long ā, and it is written with the Persian ک rather than the ق of the Arabised قفش. That spelling is the crux. Nourai reads the word as a genuine round trip (Persian kafš > Arabic qafš > Arabic-formed qaffāš > back into Persian), which is possible, since the Arabic base قفش existed. But Dehkhoda and Mo'in present کفّاش rather as a muwallad coinage made inside Persian on an Arabic template ('بر وزن صرّاف'), of the same class as داروخانه-type hybrids — the pattern is Arabic, the word need never have been current in Arabic itself (Classical Arabic for 'shoemaker' is إسكافي or خفّاف, and Lokotsch no. 772 gives ar. ḫaffāf 'Schuhmacher' from ḫuff). Hence plausible rather than confirmed: the morphology is Arabic, the residence of the word may never have been.\",\n    \"derivation_fa\": \"«کفّاش» بر وزن فَعّال عربی (مانند صرّاف و نجّار) از ستاک «کفش» ساخته شده است؛ ولی املای آن با «ک» است نه با «ق» ی معرّبِ «قفش». نورایی آن را رفت‌وبرگشتی کامل می‌داند: کفش فارسی ← قفش عربی ← قفّاش ← بازگشت به فارسی. دهخدا و معین امّا آن را واژه‌ای مولّد می‌شمارند که در خودِ فارسی و بر قالب عربی ساخته شده است (دهخدا: «بر وزن صرّاف»)، چه در عربی فصیح «کفشگر» را إسکافی یا خفّاف می‌گویند (لوکوچ، شمارهٔ ۷۷۲: ar. ḫaffāf «Schuhmacher» از ḫuff). پس ادعای نورایی با احتیاط پذیرفتنی است: وزن عربی است، ولی گذر واقعی واژه از عربی مسلّم نیست.\",\n    \"sources\": [\"https://abadis.ir/fatofa/%DA%A9%D9%81%D8%A7%D8%B4/\"],\n    \"ref_check\": [{\"ref\": \"MON:3000\", \"status\": \"partial\", \"note\": \"Farhang-e Mo'in s.v. کفاش (abadis.ir): '(کَ فّ) آن که کفش دوزد و فروشد، کفشدوز', with the tag '(ص. اِ.)' — Mo'in gives the meaning Nourai gives but marks it as an adjective/noun formation, not as an Arabic loanword; Dehkhoda on the same page says it is built 'بر وزن صرّاف' on Persian کفش. So the reference supports the word and the sense but is looser than Nourai's Arabic detour.\"}],\n    \"consulted\": [\n      {\"src\": \"MON\", \"where\": \"s.v. کفاش via abadis.ir\", \"stance\": \"partial\", \"note\": \"'آن که کفش دوزد و فروشد، کفشدوز'; Dehkhoda: pattern of صرّاف, built on Persian کفش.\"},\n      {\"src\": \"PLA\", \"where\": \"p. 111 s.v. خفاف / p. 219 s.v. قفش\", \"stance\": \"partial\", \"note\": \"Asbaghi has Arabic خفّاف ḫaffāf 'Schuster' as the nomen agentis of ḫuff (p.111) and قفش qafš as the Persian loan (p.219), but no قفّاش — i.e. the base was borrowed into Arabic, the agent noun is not attested there in his material.\"},\n      {\"src\": \"LKT\", \"where\": \"no. 772 (leaf 89)\", \"stance\": \"partial\", \"note\": \"'Ar. ḫaffāf: “Schuhmacher” [zu ar. ḫuff “kurzer Stiefel”], tk. vulgär kawaf' — the Arabic word for shoemaker is ḫaffāf, not qaffāš.\"}\n    ]\n   },\n   {\n    \"id\": 4, \"lang\": \"Greek\", \"words\": \"kaukis; kaukalon\",\n    \"verdict\": \"plausible\",\n    \"derivation\": \"Nourai's source here is exact and can be quoted: Mann, An Indo-European Comparative Dictionary, addenda p. 1628, s.v. 'kaukis, ios': 'in Per. kafš “boot” and Gk. (Iran. LW?) kaukís, f. “kind of shoe”, cf. kaúkalon “shaft of boot” (queried). Iran LW in Arm. kawšik “shoe”.' So Mann does connect Greek καυκίς with Persian kafš and does suspect an Iranian loan — but he flags it twice with a query, and his gloss of kaukalon as 'shaft of boot' is itself marked '(queried)'. Elsewhere in the same dictionary (s.v. kaukol-os 'skull, basin, trough', p. ~480) Mann assigns καύκαλον to the καῦκος 'cup, bowl' family, where Greek καυκίον 'cup' and Latin caucus belong — a homonymic nest that most Hellenists (Frisk, Chantraine, Beekes) treat as a Wanderwort/Pre-Greek word for a drinking vessel, not a shoe. The 'shoe' senses rest on glossographers (Hesychius, Pollux). Nourai's arrow is therefore defensible on Mann's authority but should be read as Mann himself read it, with a question mark, and kaukalon is the weaker half of the box.\",\n    \"derivation_fa\": \"مأخذ نورایی در اینجا دقیق است: مان در «فرهنگ تطبیقی هندواروپایی»، بخش افزوده‌ها ص ۱۶۲۸، ذیل kaukis می‌نویسد: «در فارسی kafš و در یونانی (وام‌واژهٔ ایرانی؟) kaukís مادّه‌مؤنث «گونه‌ای کفش»، نیز kaúkalon «ساق چکمه» (با تردید). وام‌واژهٔ ایرانی در ارمنی kawšik». پس مان پیوند را می‌پذیرد ولی دوبار علامت پرسش می‌گذارد. افزون بر این، خودِ مان در جای دیگر همان کتاب kaúkalon را در خانوادهٔ kaûkos «کاسه، جام» می‌آورد که یونان‌شناسان امروزی (فریسک، شانترن، بیکس) آن را واژه‌ای پیش‌یونانی/سرگردان برای ظرف نوشیدنی می‌دانند، نه کفش. معناهای «کفش» تنها بر واژه‌نامه‌های کهن (هزیخیوس و پولوکس) استوارند. پس این پیوند با احتیاط پذیرفتنی است و بخش kaukalon سست‌تر است.\",\n    \"sources\": [\"https://en.wiktionary.org/wiki/%DA%A9%D9%81%D8%B4\"],\n    \"ref_check\": [{\"ref\": \"IEC:1628\", \"status\": \"supports\", \"note\": \"Verified on the archive.org scan of Mann 1984-87 (leaf 829, whose page-numbers.json records ocr_value ['1627','1628'] — so Nourai's page is exact; the local IEC.txt OCR breaks off before this leaf). Full text of the entry: 'kaukis, ios in Per. kafš “boot” and Gk. (Iran. LW?) kaukís, f. “kind of shoe”, cf. kaúkalon “shaft of boot” (queried). Iran LW in Arm. kawšik “shoe”.' Nourai's Greek box, Armenian box and both glosses come straight from this line.\"}],\n    \"consulted\": [\n      {\"src\": \"IEC\", \"where\": \"addenda p. 1628 s.v. kaukis, ios (archive.org fulltext, leaf 829)\", \"stance\": \"supports\", \"note\": \"quoted in full above; the Iranian-loan status is Mann's own suggestion, queried.\"},\n      {\"src\": \"IEC\", \"where\": \"s.v. kaukol-os (1), scan leaf 255 (≈ p. 479/480)\", \"stance\": \"partial\", \"note\": \"'kaukol-os (1) “skull, basin, trough”. WP I, 331. Cf. kaûkos. Per. cf. kafča (“ladle”, LW in R kovš); Gk. kaukálion “vessel”, kaúkalon (“skull”. Ambig. cf. kauk-)' — Mann's other treatment of kaúkalon puts it with 'cup/skull', not with 'boot'.\"},\n      {\"src\": \"WLD\", \"where\": \"Walde-Pokorny I, 331 (cited by Mann for the kaûkos group)\", \"stance\": \"partial\", \"note\": \"the reference Mann himself gives for kaukos covers 'cup/skull/howl' meanings, not footwear — the shoe sense is Mann's separate addendum.\"},\n      {\"src\": \"POK\", \"where\": \"grep kaukis/kaukalon in POK_full.txt\", \"stance\": \"silent\", \"note\": \"Pokorny sets up no IE root for this word; there is no Pokorny article behind Nourai's Greek box.\"}\n    ]\n   },\n   {\n    \"id\": 5, \"lang\": \"Armenian\", \"words\": \"kawšik\",\n    \"verdict\": \"confirmed\",\n    \"derivation\": \"Old Armenian կօշիկ, transliterated kawšik in the older convention (Armenian օ = older aw) and kōšik in the modern one, 'shoe'. It is a Middle Iranian loan: from Iranian *kafšīk, i.e. the very kafš of the Pahlavi root box plus the common Iranian adjectival/diminutive suffix -īk (Arm. -ik). The sound substitution is the regular Armenian treatment of Iranian -f- before a consonant, which Hübschmann tabulates: Iranian f appears in Armenian as w/u (Arm. kausik, kōšik 'Schuh' : NP kafš, exactly alongside Arm. Khavfar : NP kaftar, Arm. drawš : NP dirafš, Av. drafša-). Modern Armenian կոշիկ košik continues the Old Armenian word directly. Ačaṙyan's etymological dictionary and Wiktionary both give the Iranian source.\",\n    \"derivation_fa\": \"ارمنی کهن կօշիկ که در شیوهٔ کهن kawšik و در شیوهٔ نو kōšik خوانده می‌شود، به معنی «کفش»، وام‌واژه‌ای ایرانی میانه است: از ایرانی *kafšīk، یعنی همان kafš پهلوی به‌علاوهٔ پسوند ایرانی -īk (در ارمنی -ik). بدل شدن فِ ایرانی به w/u در ارمنی قاعده‌مند است و هوبشمان در «پژوهش‌های ایرانی» ص ۱۸۸ آن را در یک ردیف آورده است: kausik/kōšik «کفش» در برابر np. kafš، همچنانکه Khavfar در برابر kaftar و drawš در برابر درفش. آچاریان و ویکی‌واژه نیز خاستگاه ایرانی را تأیید می‌کنند. ادعای نورایی درست است.\",\n    \"sources\": [\"https://en.wiktionary.org/wiki/%D5%AF%D6%85%D5%B7%D5%AB%D5%AF\", \"https://en.wiktionary.org/wiki/%D5%AF%D5%B8%D5%B7%D5%AB%D5%AF\", \"https://en.wiktionary.org/wiki/%DA%A9%D9%81%D8%B4\"],\n    \"ref_check\": [{\"ref\": \"IEC:1628\", \"status\": \"supports\", \"note\": \"Mann, addenda p. 1628 s.v. kaukis, ios (archive.org leaf 829): '… Iran LW in Arm. kawšik “shoe”.' — Nourai's spelling kawšik and his gloss are taken verbatim from this line, and the arrow Persian > Armenian is Mann's.\"}],\n    \"consulted\": [\n      {\"src\": \"HUB\", \"where\": \"Persische Studien p. 188 (HUB.txt line 6605, leaf 198; leaf = printed + 10)\", \"stance\": \"supports\", \"note\": \"Hübschmann, in the list of Iranian f > Armenian w/u: 'kausik, kōšik “Schuh”, np. kafš, bal. LW. kaus “Schuh”' — set beside 'Khavfar … np. kaftar' and 'drawš … np. dirafš, zd. drafša-'.\"},\n      {\"src\": \"IEC\", \"where\": \"p. 1628\", \"stance\": \"supports\", \"note\": \"as quoted.\"},\n      {\"src\": \"PHD\", \"where\": \"p. 51 s.v. kafš\", \"stance\": \"supports\", \"note\": \"supplies the Middle Persian base kafš/kafšag from which Iranian *kafšīk is formed.\"}\n    ]\n   }\n  ]\n}\njson.dump(e1, open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p233/part1.json','w'), ensure_ascii=False, indent=2)\nprint(\"ok\", len(e1[\"nodes\"]))\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p233/build1.py",
 "description": "Build entry 1 JSON"
}
```


### [2026-09-06T15:49:42.779Z] TOOL RESULT

```
ok 5
```


## [2026-09-06T15:49:49.377Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"POK:\"; grep -c -i \"kaukis\\|kaukalon\" POK_full.txt 2>/dev/null || echo 0\necho \"WLD b1:\"; grep -c -i \"kaukis\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt 2>/dev/null\necho \"POK kaftan/xaftan:\"; grep -c -i \"kaftan\" POK_full.txt\necho \"IEC kaukol leaf check:\"; grep -n \"kaukol-os\" IEC.txt | head -2",
 "description": "Verify POK/WLD silence"
}
```


### [2026-09-06T15:49:49.458Z] TOOL RESULT

```
POK:
0
0
WLD b1:
0
POK kaftan/xaftan:
1
IEC kaukol leaf check:
6869:kaukol-os (1) ‘skull, basin, trough'. WP I, 331. Cf. kaüKos Per. cf, kafce (-ladle" LW in R kovš, id.); Gk. kaukálion ‘vesseľ, kaükalon ('skull'. Ambig. cf. kauK-); Li. káukolis, io, m. and káukole, es, f. ‘skull’; Finn. LW kaukalo “trough?
```


## [2026-09-06T15:52:24.303Z] TOOL CALL #65: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p233/build2.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\ne2 = {\n  \"entry\": 2,\n  \"root\": \"Kaftân\",\n  \"verdict\": \"plausible\",\n  \"modern_form\": \"New Persian خفتان xaftān 'quilted/padded war-coat, armour-coat' (also خفدان xafdān); the Iranian origin of the Turkish/Arabic kaftān is the traditional view but is contested by a Turkic *qaptan\",\n  \"note\": \"The root box asserts an Iranian etymon for the whole kaftan family. The traditional orientalist consensus is behind Nourai: Lokotsch enters the family under the headword 'Pers. ḫaftān' (no. 774) — 'Ebenso ar. und tk. kaftān “ein Gewand” aus Seide oder Brokat … hieraus russ., klruss., serb., čech., poln. kaftan; rum. caftan, sp. pg. caftan, it. caffetano, frz. caftan, cafetan; engl. caftan, kaftan, ndl. caftan, dtsch. Kaftan'; Devic says 'C'est le turc قفطان qafṭān … primitivement identique, sans doute, à l'arabe-persan خفتان ḫaftān, cotte de mailles, armure militaire'; Asbaghi (PLA p.111) lists Arabic ḫaftān 'gesteppter Panzer, wattiertes Obergewand' as Persian, and adds under the same head 'Kaftan … pers. > ar. > tk. > poln.'; Mo'in's footnote in Borhan-e Qate' (vol. 2, leaves 218-219, printed pp. ≈759-762) says of خفتان that it is also 'قفطان' and that it 'وارد زبان فرانسه شده caftan و cafetan (جامهٔ ترکی هزین، با آستر پوستین)'. Etymonline still prints 'from Turkish qaftan, from Persian khaftan'. The dissent is Turkological: the current AHD derives caftan from 'Russian kaftan, from Ottoman Turkish qaftān, from Old Turkic qaptan', a native Turkic compound (qap 'sack, cover' + a garment element), which would make the Persian word the borrower, not the lender. Nourai gives no Old or Middle Iranian ancestor for his 'Iranian' root box, and none is known — Persian خفتان is first met in the Šāh-nāma (the Ferdowsī bayt is quoted in the chart), not in Pahlavi. So: plausible, with a real modern counter-proposal.\",\n  \"note_fa\": \"نورایی سراسر خانوادهٔ «قفطان/کفتان» را ایرانی می‌داند و سنت شرق‌شناسی با اوست: لوکوچ (شمارهٔ ۷۷۴) این خانواده را زیر سرواژهٔ «Pers. ḫaftān» می‌آورد و روسی و لهستانی و رومانیایی و فرانسه و انگلیسی را از آن می‌گیرد؛ دُویک می‌گوید قفطانِ ترکی «بی‌گمان در اصل همان خفتانِ عربی-فارسی، یعنی زره و جامهٔ جنگ، است»؛ اصبغی (ص ۱۱۱) «خفتان» عربی را فارسی می‌شمارد و راه «فارسی ← عربی ← ترکی ← لهستانی» را می‌کشد؛ معین در حاشیهٔ برهان قاطع می‌نویسد خفتان همان «قفطان» است و «وارد زبان فرانسه شده caftan و cafetan». امّا فرهنگ American Heritage امروزی این را نمی‌پذیرد و caftan را از روسی kaftan، از ترکی عثمانی qaftān، از ترکی باستان *qaptan (ترکیبی ترکی) می‌داند. نکتهٔ ضعف کار نورایی آن است که برای جعبهٔ «ایرانی» هیچ صورت ایرانی باستان یا فارسی میانه‌ای نمی‌آورد و در واقع کهن‌ترین گواه «خفتان» شاهنامه است، نه پهلوی. پس ادعا با احتیاط پذیرفتنی است.\",\n  \"sources\": [\"https://www.etymonline.com/word/caftan\", \"https://www.ahdictionary.com/word/search.html?q=caftan\", \"https://abadis.ir/fatofa/%D8%AE%D9%81%D8%AA%D8%A7%D9%86/\"],\n  \"ref_check\": [{\"ref\": \"PLA:11\", \"status\": \"not_found\", \"note\": \"Asbaghi p.11 (PLA_pages.txt leaf 26; printed page = leaf − 15) is the ʾarmanistān … ʾāriyya stretch of the alif section and contains nothing about a garment. The reference Nourai wants is PLA:111, which he cites correctly on the Arabic node below: leaf 126 = printed p.111, 'خفتان ḫaftān: “gesteppter Panzer, wattiertes Obergewand” pers.'. The printed book really does read 'PLA:11' (verified on the page image, root box of the third chart), so this is the author's own typo, not an extraction error.\"}],\n  \"consulted\": [\n    {\"src\": \"LKT\", \"where\": \"no. 774 (LKT.txt line 1882, leaf 89 ≈ printed p. 63)\", \"stance\": \"supports\", \"note\": \"headword 'Pers. ḫaftān'; 'Ebenso ar. und tk. kaftān “ein Gewand” aus Seide oder Brokat … hieraus russ. klruss. serb. čech. poln. kaftan; rum. caftan … frz. caftan, cafetan; engl. caftan, kaftan … dtsch. Kaftan. [Dozy Vêtem. 162/168]'.\"},\n    {\"src\": \"PLA\", \"where\": \"p. 111 s.v. خفتان (leaf 126)\", \"stance\": \"supports\", \"note\": \"'خفتان ḫaftān: “gesteppter Panzer, wattiertes Obergewand” pers.'; and directly under it 'Kaftan: “aus dem Orient stammendes Obergewand, früher Tracht der orthodoxen Juden in Rußland u. Polen” pers. > ar. > tk. > poln.'; also 'خفدان ḫafdān = ḫaftān s. ḫaftān'.\"},\n    {\"src\": \"AHD\", \"where\": \"online 5th ed. s.v. caftan\", \"stance\": \"contradicts\", \"note\": \"'Russian kaftan, from Ottoman Turkish qaftān …, from Old Turkic qaptan' — no Persian at all; the Old Turkic form is analysed as a compound of a word for 'sack' plus a garment element.\"},\n    {\"src\": \"MON\", \"where\": \"Dehkhoda + Mo'in s.v. خفتان via abadis.ir\", \"stance\": \"partial\", \"note\": \"Mo'in: '(خَ / خِ) جامهٔ جنگ'; Dehkhoda gives the Ferdowsī and other citations and the variant خفدان, and reports both a Persian derivation (from خفتن, MP xuftan) and a Turkic/Arabic one — it does not settle the question.\"}\n  ],\n  \"nodes\": [\n   {\n    \"id\": 1, \"lang\": \"Persian\", \"words\": \"xaftân «خفتان» (also خفدان)\",\n    \"verdict\": \"confirmed\",\n    \"derivation\": \"New Persian خفتان xaftān 'quilted war-coat, armour worn under or instead of mail', with the by-form خفدان xafdān (voicing of -t- after the nasal-less cluster is a common Persian variation, cf. تفتن/تبیدن type doublets); the chart's 'extra' script خفدان is the reading of the Borhan-e Qate' manuscripts, which have a separate headword خفدان cross-referring to خفتان. The word is well attested from the Šāh-nāma on — the bayt Nourai prints, 'به خفتانش بر نیزه بگذاشتم / به نیرو از آن زینش برداشتم', is Ferdowsī's. Persian lexicographers connect it with خفتن xuftan 'to lie down, sleep' (MP xuftan), i.e. a padded coat one lies in, but this is not secured. That it is a genuine Persian word of the epic vocabulary, whatever its ultimate source, is not in doubt.\",\n    \"derivation_fa\": \"«خفتان» در فارسی نو جامه‌ای است لایه‌دار و پنبه‌دوزی‌شده که در جنگ زیر زره یا به‌جای آن می‌پوشیدند؛ صورت دیگر آن «خفدان» است (ابدال ت به د). نسخه‌های برهان قاطع «خفدان» را سرواژهٔ جداگانه دارند و به «خفتان» ارجاع می‌دهند؛ پس صورت افزودهٔ نمودار درست است. کهن‌ترین گواه‌ها از شاهنامه است و بیتِ خودِ نمودار («به خفتانش بر نیزه بگذاشتم…») از فردوسی است. فرهنگ‌نویسان فارسی آن را با «خفتن» (فارسی میانه xuftan) پیوند می‌دهند، ولی این پیوند قطعی نیست. در هر حال فارسی بودن واژه مسلّم است و ادعای نورایی درست است.\",\n    \"sources\": [\"https://abadis.ir/fatofa/%D8%AE%D9%81%D8%AA%D8%A7%D9%86/\"],\n    \"ref_check\": [\n      {\"ref\": \"BQT:759\", \"status\": \"supports\", \"note\": \"Borhan-e Qate' ed. Mo'in, vol. 2: the خفتان article and Mo'in's footnote sit on leaves 218-219 of BQT_v2_pages.txt (printed ≈ leaf + 543, i.e. pp. ≈761-762, within the ±3 tolerance of Nourai's 759). Borhan's own gloss (line 12810): 'خفتان: نوعی از جیبه و جامهٔ … که بجهت تشگیره [= جنگ] می‌کرده باشند'; the footnote (line 12877) reads 'خفتان … و نیز «قفطان» … وارد زبان فرانسه شده caftan و cafetan (جامهٔ ترکی هزین، با آستر پوستین)'. The neighbouring headword خفدان (line 12923) confirms the variant.\"},\n      {\"ref\": \"MON:1431\", \"status\": \"supports\", \"note\": \"Mo'in's lexicon s.v. خفتان (via abadis.ir, which reproduces the Farhang-e Mo'in text): '(خَ / خِ) جامهٔ جنگ، لباس رزم' — Nourai's gloss 'armor'. Print page 1431 not verifiable (6-vol. edition unscanned).\"}\n    ],\n    \"consulted\": [\n      {\"src\": \"BQT\", \"where\": \"vol. 2 leaves 218-219 (printed ≈ pp. 759-762)\", \"stance\": \"supports\", \"note\": \"entry + Mo'in's etymological footnote, quoted above.\"},\n      {\"src\": \"MON\", \"where\": \"s.v. خفتان via abadis.ir (Mo'in and Dehkhoda)\", \"stance\": \"supports\", \"note\": \"Dehkhoda: 'نوعی جامه که در جنگ پوشند … قزاگند', with the variant خفدان and Ferdowsī citations.\"},\n      {\"src\": \"PLA\", \"where\": \"p. 111 (leaf 126)\", \"stance\": \"supports\", \"note\": \"'خفدان ḫafdān = ḫaftān s. ḫaftān' — Asbaghi records the same two Persian shapes Nourai's box carries.\"},\n      {\"src\": \"PHD\", \"where\": \"grep xaftān / kaftan in PHD.txt\", \"stance\": \"silent\", \"note\": \"MacKenzie has 'kaftan, kaf- [kptn'] to fall' and 'xuftan' but no garment word — there is no Pahlavi ancestor on record for خفتان, which is why the 'Iranian' root box has to rest on New Persian evidence.\"}\n    ]\n   },\n   {\n    \"id\": 2, \"lang\": \"Arabic\", \"words\": \"qaftan\",\n    \"verdict\": \"plausible\",\n    \"derivation\": \"Arabic has the word in two shapes: خفتان ḫaftān, the direct and faithful borrowing of the Persian form, glossed by Asbaghi (p.111) 'gesteppter Panzer, wattiertes Obergewand' and marked 'pers.'; and قفطان qafṭān, with the usual Arabising substitutions ḫ > q and t > emphatic ṭ, which is the shape that went on to Turkish and Europe (al-ʿUnaysī's Tafsīr al-alfāẓ al-dāḫila has an article 'قفطان' cross-referring to قفتان). Nourai's box gives only the second shape and hangs it directly on the Iranian root rather than on his own Persian node — legitimate, since Arabic may equally have taken it from spoken Iranian. The gloss 'armor' belongs strictly to the ḫaftān shape; qafṭān in Arabic and Ottoman usage is a robe of honour, not armour, so the semantic shift 'padded war-coat' > 'long ceremonial overgarment' happened on the Arabic/Turkish side. Plausible rather than confirmed because of the competing Turkic *qaptan etymology.\",\n    \"derivation_fa\": \"عربی این واژه را در دو صورت دارد: «خفتان» که وام‌گیری مستقیم و وفادار از فارسی است و اصبغی (ص ۱۱۱) آن را «زره لایه‌دوزی‌شده، بالاپوش پنبه‌دار» و «فارسی» می‌خواند؛ و «قفطان» با ابدال‌های معمول معرّب‌سازی (خ ← ق، ت ← ط) که همین صورت به ترکی و از آنجا به اروپا رفته است (طوبیا العنیسی نیز مدخل «قفطان» را دارد). نورایی تنها صورت دوم را آورده و آن را یکراست به جعبهٔ ریشه بسته است، نه به گرهِ فارسیِ خود، که پذیرفتنی است. امّا معنی «زره» تنها از آنِ صورت «خفتان» است؛ «قفطان» در کاربرد عربی و عثمانی خلعت و بالاپوش بلند است، یعنی تحول معنایی «جامهٔ جنگ ← جامهٔ تشریفات» در سوی عربی-ترکی رخ داده است. به سبب فرضیهٔ رقیبِ ترکی *qaptan، حکم «با احتیاط پذیرفتنی» است.\",\n    \"sources\": [\"https://www.etymonline.com/word/caftan\"],\n    \"ref_check\": [{\"ref\": \"PLA:111\", \"status\": \"supports\", \"note\": \"Asbaghi, Persische Lehnwörter im Arabischen p.111 (PLA_pages.txt leaf 126, printed = leaf − 15): 'خفتان ḫaftān: “gesteppter Panzer, wattiertes Obergewand” pers.' and immediately under it 'Kaftan: “aus dem Orient stammendes Obergewand, früher Tracht der orthodoxen Juden in Rußland u. Polen” pers. > ar. > tk. > poln.' — this is precisely Nourai's whole chain, and the page number is exact (the PLA:11 on the root box is the typo).\"}],\n    \"consulted\": [\n      {\"src\": \"PLA\", \"where\": \"p. 111 (leaf 126); cf. p. 220 'قفطان quftān = qafṭān q. v.'\", \"stance\": \"supports\", \"note\": \"both Arabic shapes are in Asbaghi's Persian-loanword dictionary.\"},\n      {\"src\": \"TAD\", \"where\": \"al-ʿUnaysī, Tafsīr al-alfāẓ al-dāḫila (TAD_pages.txt line 2210)\", \"stance\": \"supports\", \"note\": \"'قفطان — ترى «قفتان» …' — the Arabic dictionary of foreign words carries qafṭān/qaftān as a borrowed word.\"},\n      {\"src\": \"DEV\", \"where\": \"s.v. Caftan (DEV.txt line 898, leaf 104)\", \"stance\": \"supports\", \"note\": \"'C'est le turc قفطان qafṭān, vêtement d'honneur, primitivement identique, sans doute, à l'arabe-persan خفتان ḫaftân, cotte de mailles, armure militaire.'\"},\n      {\"src\": \"AFM\", \"where\": \"grep خفتان / قفطان in AFM_pages.txt\", \"stance\": \"silent\", \"note\": \"Addi Shir has no article at either spelling in this OCR.\"}\n    ]\n   },\n   {\n    \"id\": 3, \"lang\": \"Turkish\", \"words\": \"qaftan\",\n    \"verdict\": \"plausible\",\n    \"derivation\": \"Ottoman Turkish قفطان kaftan, the standard word for the long-sleeved robe of honour bestowed by the Sultan; from Ottoman it is the immediate donor for every European form. Nourai routes it through Arabic, and that is the traditional view (Devic: 'C'est le turc qafṭān … primitivement identique … à l'arabe-persan ḫaftân'; Asbaghi's 'pers. > ar. > tk. > poln.'; Lokotsch's 'ar. und tk. kaftān' under a Persian headword). The counter-view, now in the American Heritage Dictionary, is that Ottoman qaftān continues Old Turkic qaptan, a Turkic compound, in which case the Turkish word is not borrowed at all and the Arabic and Persian forms are its relatives or its debtors. Nourai's own citation for this box (BQT:760) is Mo'in's footnote to خفتان in Borhan-e Qate', which does mention قفطان but says nothing about Turkish being the borrower from Arabic. Hence plausible.\",\n    \"derivation_fa\": \"«قفطان» ترکی عثمانی نام جامهٔ بلندِ آستین‌دار و خلعت سلطانی است و همهٔ صورت‌های اروپایی یکراست از آن گرفته شده‌اند. نورایی آن را از عربی می‌گیرد و این دیدگاه سنتی است (دُویک، اصبغی، لوکوچ). دیدگاه رقیب، که فرهنگ American Heritage امروزی آورده، qaftān عثمانی را دنبالهٔ ترکی باستان *qaptan می‌داند؛ در آن صورت واژه در ترکی وام‌واژه نیست. مأخذی که نورایی در این جعبه آورده (BQT:760) حاشیهٔ معین بر «خفتان» است که «قفطان» را یاد می‌کند ولی دربارهٔ وام‌گیری ترکی از عربی چیزی نمی‌گوید. پس حکم «با احتیاط پذیرفتنی» است.\",\n    \"sources\": [\"https://www.ahdictionary.com/word/search.html?q=caftan\", \"https://www.etymonline.com/word/caftan\"],\n    \"ref_check\": [{\"ref\": \"BQT:760\", \"status\": \"partial\", \"note\": \"The cited stretch of Borhan-e Qate' vol. 2 (leaves 218-219, printed ≈ 759-762) is the خفتان article with Mo'in's footnote: '… و نیز «قفطان» … وارد زبان فرانسه شده caftan و cafetan (جامهٔ ترکی هزین، با آستر پوستین)'. It supports the existence of the قفطان form and its onward passage to French, and it calls the garment 'Turkish', but it does not state that Turkish took the word from Arabic — the specific arrow Nourai draws here is not in the page.\"}],\n    \"consulted\": [\n      {\"src\": \"BQT\", \"where\": \"vol. 2 leaves 218-219 (Mo'in's footnote to خفتان)\", \"stance\": \"partial\", \"note\": \"quoted above.\"},\n      {\"src\": \"LKT\", \"where\": \"no. 774 (leaf 89)\", \"stance\": \"supports\", \"note\": \"'Ebenso ar. und tk. kaftān' under the headword 'Pers. ḫaftān' — Lokotsch treats Arabic and Turkish as parallel takers from Persian.\"},\n      {\"src\": \"TTS\", \"where\": \"grep kaftan/qaftan in TTS_pages.txt (Vámbéry)\", \"stance\": \"silent\", \"note\": \"Vámbéry's turko-tatarisches Wörterbuch has no article for the word in this OCR — so the local Turkological source gives no support to a native Turkic origin either.\"},\n      {\"src\": \"AHD\", \"where\": \"online 5th ed. s.v. caftan\", \"stance\": \"contradicts\", \"note\": \"'from Ottoman Turkish qaftān …, from Old Turkic qaptan' — Turkish as inheritor, not borrower.\"}\n    ]\n   },\n   {\n    \"id\": 4, \"lang\": \"Russian\", \"words\": \"kaftan\",\n    \"verdict\": \"confirmed\",\n    \"derivation\": \"Russian кафтан kaftan, borrowed from Ottoman Turkish (through the Tatar/Turkic contact zone) and attested in Russian from the medieval period as the name of a long belted coat; Ukrainian, Serbian, Czech and Polish kaftan are the same borrowing, and Lokotsch groups them together. Turkish -ā- is rendered by Russian -a- and the word is fitted to the ordinary masculine o-stem declension. The Russian form matters for the English etymology because it, not the Turkish, is the shape the American Heritage Dictionary makes the immediate source of English caftan.\",\n    \"derivation_fa\": \"روسی кафтан از ترکی عثمانی (از راه پیوند با تاتارها) وام گرفته شده و از سده‌های میانه در روسی نام جامهٔ بلندِ کمربنددار است؛ اوکراینی، صربی، چکی و لهستانی kaftan نیز همان وام‌گیری‌اند و لوکوچ همه را در یک ردیف می‌آورد. آ کشیدهٔ ترکی در روسی به a بدل شده و واژه در صرف مذکر روسی جا افتاده است. اهمیت این گره در آن است که فرهنگ American Heritage همین صورت روسی را مأخذ بی‌واسطهٔ caftan انگلیسی می‌داند. ادعای نورایی درست است.\",\n    \"sources\": [\"https://www.ahdictionary.com/word/search.html?q=caftan\"],\n    \"ref_check\": [{\"ref\": \"AHD:187\", \"status\": \"partial\", \"note\": \"The 1975/76 AHD New College Edition p.187 is not open online (IA scans are lending-only; the local AHD file contains only the Watkins Indo-European appendix). The current AHD entry for the same headword reads 'Russian kaftan, from Ottoman Turkish qaftān …, from Old Turkic qaptan', which confirms the Turkish > Russian > English part of Nourai's chart while denying the Persian source at the top of it.\"}],\n    \"consulted\": [\n      {\"src\": \"LKT\", \"where\": \"no. 774 (leaf 89)\", \"stance\": \"supports\", \"note\": \"'hieraus russ. klruss. serb. čech. poln. kaftan “langschößiger Rock”' — Slavic forms taken from Arabic/Turkish kaftān.\"},\n      {\"src\": \"AHD\", \"where\": \"online 5th ed. s.v. caftan\", \"stance\": \"supports\", \"note\": \"'Russian kaftan, from Ottoman Turkish qaftān' — the Turkish > Russian step is exactly Nourai's.\"},\n      {\"src\": \"PLA\", \"where\": \"p. 111\", \"stance\": \"supports\", \"note\": \"Asbaghi's chain 'pers. > ar. > tk. > poln.' reaches the same Slavic stage.\"}\n    ]\n   },\n   {\n    \"id\": 5, \"lang\": \"English\", \"words\": \"caftan\",\n    \"verdict\": \"plausible\",\n    \"derivation\": \"English caftan (also kaftan) 'a long-sleeved robe worn in Turkey, Egypt and the Levant' is first recorded in the 1590s, in travellers' accounts of the Ottoman court, and the classic English etymologies take it straight from Turkish: Skeat, 'Caftan, a Turkish garment. (Turk.) Turk. qaftān'; Klein, 'caftan … Turk. qaftān, fr. Arab. qaftān, fr. Pers. khaftān'; Etymonline, 'from Turkish qaftan (also in Arabic), from Persian khaftan'. The Russian intermediary Nourai draws is the American Heritage account, which is really about the modern shape of the word (Russian kaftan being the form current in 19th-century Western writing on Slavic and Central Asian dress) rather than about the 1590s borrowing. So the box is right that the word is ultimately the Turkish/Persian garment name and right in its gloss, but the immediate parent is more probably Turkish (or French cafetan) than Russian — plausible.\",\n    \"derivation_fa\": \"انگلیسی caftan/kaftan «جامهٔ بلندِ آستین‌دار شرقی» نخستین‌بار در دههٔ ۱۵۹۰م در سفرنامه‌های دربار عثمانی دیده می‌شود و ریشه‌شناسی‌های کلاسیک آن را یکراست از ترکی می‌گیرند: اسکیت «Turk. qaftān»؛ کلاین «Turk. qaftān, fr. Arab. qafṭān, fr. Pers. khaftān»؛ Etymonline «از ترکی qaftan، از فارسی خفتان». واسطهٔ روسی که نورایی کشیده از فرهنگ American Heritage آمده و بیشتر به صورتِ رایج واژه در نوشته‌های سدهٔ نوزدهم دربارهٔ پوشاک اسلاوی و آسیای میانه مربوط است تا به وام‌گیری سدهٔ شانزدهم. پس معنی و خاستگاه نهایی درست است ولی والدِ بی‌واسطه به احتمال زیاد ترکی (یا فرانسهٔ cafetan) است، نه روسی: با احتیاط پذیرفتنی.\",\n    \"sources\": [\"https://www.etymonline.com/word/caftan\", \"https://www.ahdictionary.com/word/search.html?q=caftan\"],\n    \"ref_check\": [\n      {\"ref\": \"KLN:220\", \"status\": \"supports\", \"note\": \"Klein 1966, KLN_1966.txt line 6099, leaf 127; p = 2·leaf − 34 = 220, i.e. Nourai's page is exact: 'caftan, n., a long-sleeved garment worn in Turkey, Egypt, etc. — Turk. qaftān, fr. Arab. qaftān, fr. Pers. khaftān.' Klein confirms the gloss word for word and the Persian ultimate origin — but he routes English through Turkish, with no Russian stage.\"},\n      {\"ref\": \"AHD:187\", \"status\": \"partial\", \"note\": \"1975/76 AHD page not accessible (see node 4); the current AHD gives 'Russian kaftan, from Ottoman Turkish qaftān …, from Old Turkic qaptan' — supports the Russian > English step Nourai draws, contradicts the Persian origin.\"}\n    ],\n    \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"p. 220 s.v. caftan\", \"stance\": \"partial\", \"note\": \"quoted above: gloss and Persian origin confirmed, Russian stage absent.\"},\n      {\"src\": \"SKT\", \"where\": \"printed p. 61 s.v. Caftan (SKT.txt line 2610)\", \"stance\": \"partial\", \"note\": \"'Caftan, a Turkish garment. (Turk.) Turk. qaftān, a dress.' — Skeat marks the source as Turkish only; his list of Turkish loans in English (line 23665) includes caftan.\"},\n      {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls vol. 1, s.v. caftan (FSD_vol1.txt line 54482)\", \"stance\": \"contradicts\", \"note\": \"'[< Ar. qafṭān.] caffe-tan; kaftan — caftaned, a. wearing a caftan' — Funk & Wagnalls makes the immediate source Arabic, not Russian.\"},\n      {\"src\": \"LKT\", \"where\": \"no. 774\", \"stance\": \"partial\", \"note\": \"'engl. caftan, kaftan' listed in the same series as the Slavic and Romance forms, all from ar./tk. kaftān; no Russian > English step.\"}\n    ]\n   }\n  ]\n}\njson.dump(e2, open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p233/part2.json','w'), ensure_ascii=False, indent=2)\nprint(\"ok\", len(e2[\"nodes\"]))\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p233/build2.py",
 "description": "Build entry 2 JSON"
}
```


### [2026-09-06T15:52:26.440Z] TOOL RESULT

```
ok 5
```


## [2026-09-06T15:52:31.547Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nS=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p233\npython3 - <<'PYEOF'\nimport json\nS='/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p233'\nout=json.load(open(S+'/part0.json'))\nout['entries'].append(json.load(open(S+'/part1.json')))\nout['entries'].append(json.load(open(S+'/part2.json')))\njson.dump(out, open('/home/sfmqrb/git/rishe/data/verification/page-233.json','w'), ensure_ascii=False, indent=2)\nprint('entries', len(out['entries']), 'nodes', [len(e['nodes']) for e in out['entries']])\nPYEOF\npython3 -m json.tool data/verification/page-233.json > /dev/null && echo \"JSON OK\"\npython3 tools/verify_check.py 233",
 "description": "Assemble and run verify_check"
}
```


### [2026-09-06T15:52:33.614Z] TOOL RESULT

```
entries 3 nodes [7, 5, 5]
JSON OK
nodes verified: 17/17
node verdicts: {'disputed': 1, 'confirmed': 10, 'plausible': 6}
root verdicts: {'disputed': 1, 'confirmed': 1, 'plausible': 1}
ref checks: {'not_checked': 4, 'supports': 9, 'partial': 7}
books consulted: {'supports': 31, 'contradicts': 5, 'silent': 10, 'partial': 10} | by book: {'LKT': 8, 'KLN': 7, 'PLA': 6, 'MON': 5, 'BQT': 4, 'SKT': 3, 'AHD': 3, 'PHD': 3, 'IEC': 3, 'DEV': 2, 'AFM': 2, 'FVQ': 1, 'RCH': 1, 'PHN': 1, 'ARB': 1, 'WLD': 1, 'POK': 1, 'HUB': 1, 'TAD': 1, 'TTS': 1, 'FSD': 1}
```


## [2026-09-06T15:52:42.294Z] TOOL CALL #67: Bash

```json
{
 "command": "file data/verification/page-233.json && head -c 3 data/verification/page-233.json | xxd | head -1 && python3 -c \"\nimport json;d=json.load(open('data/verification/page-233.json',encoding='utf-8'))\nprint(d['pdf_page'],d['book_page'],d['verified_on'])\nfor e in d['entries']:\n    assert e.get('note_fa'), e['root']\n    for n in e['nodes']:\n        assert n.get('derivation_fa') and n.get('ref_check') and n.get('consulted'), (e['root'],n['id'])\nprint('all fields present')\"",
 "description": "Validate encoding and required fields"
}
```


### [2026-09-06T15:52:45.540Z] TOOL RESULT

```
data/verification/page-233.json: JSON text data
00000000: 7b0a 20                                  {. 
233 203 2026-09-06
all fields present
```


## [2026-09-06T15:53:05.796Z] AGENT

Done. `data/verification/page-233.json` written; `verify_check.py 233` reports 17/17 nodes, 0 PROBLEM lines.

**Page 233 (book p. 203) — 3 entries, 17 nodes**
- Root verdicts: 1 confirmed (Kafš), 1 plausible (Kaftân), 1 disputed (Kaffa)
- Node verdicts: 10 confirmed, 6 plausible, 1 disputed
- Ref checks (nodes): 9 supports, 7 partial, 4 not_checked; root-level: 1 not_found (PLA:11)

Disputed / weak items:
- **Kaffa (root) + Arabic qahwah** — Nourai copies Klein verbatim, but modern work (Wiktionary, Etymonline, current AHD, Dehkhoda) prefers the native Arabic root q-h-w/q-h-y: qahwa "wine" is attested centuries before the Kingdom of Kaffa and before coffee reached Arabia; the real Kaffa word entered Arabic separately as bunn.
- **English coffee/cafe/caffeine (plausible)** — cafe (1802) and caffeine (1830) do come via French, but coffee (c.1600) came via Dutch/Italian; Klein, cited in that very box, says "It. caffè, fr. Turk. qahve" with no French stage.
- **Greek kaukis/kaukalon (plausible)** — Mann IEC 1628 is quoted exactly, but he himself queries both the Iranian-loan status and the "shaft of boot" gloss; elsewhere he files kaúkalon with kaûkos "cup/skull".
- **Persian kaffâš (plausible)** — Dehkhoda/Mo'in treat it as a muwallad faʿʿāl formation made inside Persian on کفش; Arabic's own word for shoemaker is ḫaffāf/iskāfī, and no قفّاش surfaced in Asbaghi.
- **Kaftân root + Turkish/English nodes (plausible)** — Lokotsch (headword "Pers. ḫaftān"), Devic, Asbaghi p.111 and Mo'in's Borhan footnote all support Persian → Arabic → Turkish → Slavic/Europe, but the current AHD derives it from Old Turkic *qaptan*, and no Old/Middle Iranian ancestor exists (خفتان is first met in the Šāh-nāma). English caftan's immediate parent is Turkish (Skeat, Klein, Etymonline), not Russian.

Good finds worth noting:
- IEC:1628 verified on the archive.org scan (leaf 829 = printed 1627/1628; the local IEC.txt OCR breaks off before it) — Mann's line reads exactly as Nourai's Greek and Armenian boxes.
- KLN:220 for caftan is page-exact; KLN:309 for coffee maps to ≈p.313 by the leaf formula calibrated on cherub=164 — a few pages off but the entry text is verbatim.
- Asbaghi PLA p.219 s.v. قفش confirms Arabic ← Persian kafš; al-Jawāliqī's al-Muʿarrab also has القفش as Persian.

Extraction errors: **none** — I read the printed page image and the JSON is faithful, including the odd `PLA:11` on the Kaftân root box (the book really prints "PLA:11"; the entry Nourai wants is Asbaghi p. **111**, which he cites correctly on the Arabic node). That is the author's typo, not a scan error. Page image copied to `data/verification/sources/refs/ocr/BOOK/233.png`; 12 web pages archived via `fetch_source.py`.
