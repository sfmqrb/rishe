# Verification process log — verify-page-71


## [2026-09-05T05:22:48.570Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 71 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-71.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-71.json. Write /home/sfmqrb/git/rishe/data/verification/page-71.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 71` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T05:22:49.833Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T05:22:50.564Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T05:22:50.580Z] TOOL RESULT

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


## [2026-09-05T05:22:51.115Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-71.txt"
}
```


### [2026-09-05T05:22:51.132Z] TOOL RESULT

```
1	=== PDF page 71 (book page 41) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Aus 2, Awes, Ausus : to shine; dawn  (refs POK:86; KLN:495)
4	#1 (parent #0) [Avestan] refs=POK:86; SYN:871 | usaiti : to light up ; ušâ : east, dawn (direction of sunrise) ; ušas-tara : east
5	  #2 (parent #1) [Pahlavi] refs=SNS:67 | huš : morning
6	    #3 (parent #2) [Persian] refs=HRN:281; SNS:67 | hŭš 2 «هوش ۲» : morning ; hŭšbâm «هوشبام» : morning shine, breakfast ☞Bhâ 1 | NOTE: These words are almost obsolete.
7	#4 (parent #0) [Indo-European] refs=KLN:1702 | Wes 2, Wesr : spring
8	  #5 (parent #4) [Avestan] refs=POK:1174 | vasar, vasri : spring ; vanri, vanhâr : spring
9	    #6 (parent #5) [Pahlavi] refs=HRN:56 | vahâr : spring
10	      #7 (parent #6) [Persian] refs=POK:1174; KLN:1702 | bahâr «بهار» : spring
11	  #8 (parent #4) [Sanskrit] refs=BQT:1452 | vihâra : spring
12	    #9 (parent #8) [Sogdian] refs=SOD:108 | brğ`r : temple
13	      #10 (parent #9) [Persian] refs=BQT:1452; FRS:87 | farxâr «فرخار» : temple | NOTE: See BQT:1452 for discussion on the derivation.
14	  #11 (parent #4) [Old Persian] refs=KNT:188,207 | vâhara : spring time
15	  #12 (parent #4) [Latin] refs=AHD | věr : spring
16	    #13 (parent #12) [English] refs=None | vernal
17	#14 (parent #0) [Germanic] refs=AHD | aust : direction of sunshine ; Austrôn : goddess of dawn
18	  #15 (parent #14) [English] refs=None | east ; Easter
19	#16 (parent #0) [Old High German] refs=AHD | ôstar : eastern
20	  #17 (parent #16) [English] refs=None | Austria
21	#18 (parent #0) [Latin] refs=KLN:130 | australis : southern (land) ; aurôra : dawn
22	  #19 (parent #18) [English] refs=None | Australia ; aurora
23	--- entry 1 ---
24	ROOT Aus 3 -> redirect to Ôus 2
25	--- entry 2 ---
26	ROOT Ausus -> redirect to Aus 2
27	
```


## [2026-09-05T05:22:55.059Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-71.json",
 "description": "Read source JSON for page 71"
}
```


### [2026-09-05T05:22:55.101Z] TOOL RESULT

```
{
  "pdf_page": 71,
  "book_page": 41,
  "entries": [
    {
      "root": {
        "name": "Aus 2, Awes, Ausus",
        "lang": "Indo-European",
        "refs": "POK:86; KLN:495",
        "gloss": "to shine; dawn"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:86; SYN:871",
          "words": [
            {"translit": "usaiti", "gloss": "to light up", "script": null},
            {"translit": "ušâ", "gloss": "east, dawn (direction of sunrise)", "script": null},
            {"translit": "ušas-tara", "gloss": "east", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "SNS:67",
          "words": [
            {"translit": "huš", "gloss": "morning", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "HRN:281; SNS:67",
          "words": [
            {"translit": "hŭš 2", "gloss": "morning", "script": "هوش ۲"},
            {"translit": "hŭšbâm", "gloss": "morning shine, breakfast", "script": "هوشبام", "see": ["Bhâ 1"]}
          ],
          "script_extra": null,
          "note": "These words are almost obsolete.",
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Indo-European",
          "refs": "KLN:1702",
          "words": [
            {"translit": "Wes 2, Wesr", "gloss": "spring", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Avestan",
          "refs": "POK:1174",
          "words": [
            {"translit": "vasar, vasri", "gloss": "spring", "script": null},
            {"translit": "vanri, vanhâr", "gloss": "spring", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Pahlavi",
          "refs": "HRN:56",
          "words": [
            {"translit": "vahâr", "gloss": "spring", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Persian",
          "refs": "POK:1174; KLN:1702",
          "words": [
            {"translit": "bahâr", "gloss": "spring", "script": "بهار"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 4,
          "lang": "Sanskrit",
          "refs": "BQT:1452",
          "words": [
            {"translit": "vihâra", "gloss": "spring", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "Sogdian",
          "refs": "SOD:108",
          "words": [
            {"translit": "brğ`r", "gloss": "temple", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 9,
          "lang": "Persian",
          "refs": "BQT:1452; FRS:87",
          "words": [
            {"translit": "farxâr", "gloss": "temple", "script": "فرخار"}
          ],
          "script_extra": null,
          "note": "See BQT:1452 for discussion on the derivation.",
          "quote": {
            "text": "فرخار بزرگ و نیک جایی است - گر معدن آن بت نوائی است",
            "poet": "Rŭdakî"
          }
        },
        {
          "id": 11,
          "parent": 4,
          "lang": "Old Persian",
          "refs": "KNT:188,207",
          "words": [
            {"translit": "vâhara", "gloss": "spring time", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 4,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "věr", "gloss": "spring", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 12,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "vernal", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 14,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "aust", "gloss": "direction of sunshine", "script": null},
            {"translit": "Austrôn", "gloss": "goddess of dawn", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 15,
          "parent": 14,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "east", "gloss": null, "script": null},
            {"translit": "Easter", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 16,
          "parent": 0,
          "lang": "Old High German",
          "refs": "AHD",
          "words": [
            {"translit": "ôstar", "gloss": "eastern", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 17,
          "parent": 16,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "Austria", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 18,
          "parent": 0,
          "lang": "Latin",
          "refs": "KLN:130",
          "words": [
            {"translit": "australis", "gloss": "southern (land)", "script": null},
            {"translit": "aurôra", "gloss": "dawn", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 19,
          "parent": 18,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "Australia", "gloss": null, "script": null},
            {"translit": "aurora", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {"name": "Aus 3", "redirect": "Ôus 2"},
      "nodes": []
    },
    {
      "root": {"name": "Ausus", "redirect": "Aus 2"},
      "nodes": []
    }
  ]
}
```


## [2026-09-05T05:22:57.402Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KLN','SYN','SNS','HRN','KNT','AHD','BQT','SOD','FRS','WLD','PHD','NYB','HUB','MON','ARY','BRT','IEC','SKT','WEB','FSD','CHEUNG','TTS','LKT']:\n    v=d.get(k)\n    print(k, json.dumps(v, ensure_ascii=False)[:400] if v else 'MISSING')\n\"",
 "description": "Inspect refs_online keys"
}
```


### [2026-09-05T05:22:59.279Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "loca
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in 
FRS {"title": "Asadi Tusi, Loghat-e Fors, ed. Mojtaba'i & Sadeqi, Kharazmi 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/LughatEFurs-AbuMansurAliBinAhmadAsadiTusiFarsi (Abbas Eqbal's 1319/1940 Tehran edition); also dli.ernet.439493 / dli.ernet.437743 (Horn's 1897 Göttingen edition, 'Lughat Faras')", "lookup_hint": "Look up the headword (entries grouped by final letter); FRS_p
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
CHEUNG MISSING
TTS {"title": "H. Vámbéry, Etymologisches Wörterbuch der turko-tatarischen Sprachen, Leipzig 1878 (repr. Osnabrück 1972)", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/etymologischesw00vmuoft (Toronto scan; also Google/bub_gb copies)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft.pdf", 
LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 =
```


## [2026-09-05T05:23:02.834Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; ls data/verification/sources/refs/ | head -80; echo ---; sed -n 1,120p data/verification/sources/SOURCE_MATRIX.md",
 "description": "List refs and read source matrix"
}
```


### [2026-09-05T05:23:02.886Z] TOOL RESULT

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
---
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
```


## [2026-09-05T05:23:05.658Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KLN','SYN','SNS','HRN','KNT','AHD','BQT','SOD','FRS','BRT','PHD','NYB','HUB','IEC','ARY','WLD']:\n    v=d[k]\n    print('==',k)\n    for f in ['local_file','page_offset','lookup_hint','scans']:\n        if f in v: print('  ',f,':',json.dumps(v[f],ensure_ascii=False)[:600])\n\"",
 "description": "Print local file and offsets"
}
```


### [2026-09-05T05:23:07.315Z] TOOL RESULT

```
== POK
   local_file : "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt"
   page_offset : "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>"
   lookup_hint : "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\\data\\ie\\pokorny&root=config"
== KLN
   local_file : "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt"
   page_offset : "KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>"
   lookup_hint : "Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages."
== SYN
   local_file : "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt"
   page_offset : "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>"
   lookup_hint : "Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed page number line."
== SNS
   local_file : ["/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt"]
   page_offset : "242 leaves; page offset not determined (OCR too poor to read printed numbers) — locate by transliteration then read the page image"
   lookup_hint : "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping."
== HRN
   local_file : "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt"
   page_offset : "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>"
   lookup_hint : "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann."
== KNT
   local_file : "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt"
   page_offset : "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>"
   lookup_hint : "Lexicon (Part III, pp. 164 ff.) headwords are transliterated OP words at line start followed by part of speech, e.g. grep -n '^apadana-' ; section refs like '$147'. Nourai's page numbers should fall in 164-215 for lexicon citations."
== AHD
   local_file : "/home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt"
   page_offset : "1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page."
   lookup_hint : "Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves
== BQT
   local_file : ["/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)", "/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt", "/home/
   page_offset : "vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start 
   lookup_hint : "grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \\f; leaf N = N-th \\f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=
   scans : [{"volume": "3", "file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf", "first_printed": 1208, "last_printed": 1925, "pdf_offset": -1205, "page_map": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pagemap.json", "lang": "fas", "ocr_text": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt", "ocr_note": "689/721 pdf pages OCRed (tesseract fas+eng, mediocre); pages are separated by form-feeds and tagged [pdf page N]; remaining pages via tools/ref_page.py"}, {"volume": "4", "file": "/home/sfmq
== SOD
   local_file : ["/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD.txt"]
   page_offset : "printed page ≈ leaf − 66 in SOD_pages.txt (0-based \\f blocks; 645 leaves; English intro precedes)"
   lookup_hint : "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/So
== FRS
   local_file : ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FRS_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/FRS.txt"]
   page_offset : "different edition — no mapping"
   lookup_hint : "Look up the headword (entries grouped by final letter); FRS_pages.txt has \\f page breaks (567 leaves). Pagination differs from the 1365 Kharazmi edition Nourai cites — verify the entry, not the page."
== BRT
   local_file : "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt"
   page_offset : "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>"
   lookup_hint : "Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special transliteration is noisy - grep on a distinctive Latin gloss or the German meaning in quotes. Column numbers appear as standalone numbers at leaf tops."
== PHD
   local_file : "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt"
   page_offset : "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>"
   lookup_hint : "Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsianjoman.org/wp-content/uploads/2015/09/A-Concise-Pahlavi-Dictionary.pdf (8.4 MB)."
== NYB
   local_file : "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt"
   page_offset : "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>"
   lookup_hint : "Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates and 'Bthl.' refs."
== HUB
   local_file : "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt"
   page_offset : "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>"
   lookup_hint : "Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number."
== IEC
   local_file : "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt"
   page_offset : "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>"
   lookup_hint : "Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root."
== ARY
   local_file : ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt"]
   page_offset : "printed page = pdf page + 1"
   lookup_hint : "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image"
   scans : [{"file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_aryanpur_kashani_rishehaye_hend_o_orupayi.pdf", "first_printed": 1, "last_printed": 546, "pdf_offset": -1, "lang": "fas+eng", "ocr_text": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt"}]
== WLD
   local_file : ["/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sou
   page_offset : "Band 3: leaf = printed + 6. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696)."
   lookup_hint : "Band 3 is the index (Wortregister by language) - it maps a word to 'Band, page' in vols 1-2, so it can at least confirm that a word is treated at the cited WP volume/page. For the actual entry text, use Pokorny 1959 (POK), whose entries cite 'WP. I 177' etc. and are essentially a revision of WP."
```


## [2026-09-05T05:23:46.776Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n 1,150p tools/verify_check.py",
 "description": "Read verify_check tool"
}
```


### [2026-09-05T05:23:46.822Z] TOOL RESULT

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


## [2026-09-05T05:23:47.568Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -c \"\nimport json;d=json.load(open('data/verification/page-66.json'))\nprint(json.dumps(d['entries'][0],ensure_ascii=False)[:3000])\n\"",
 "description": "Look at prior verification example"
}
```


### [2026-09-05T05:23:49.278Z] TOOL RESULT

```
{"entry": 0, "root": "A`.s.r", "verdict": "confirmed", "modern_form": "Arabic root ع ص ر ʿ-ṣ-r 'to press, squeeze (the juice out)'; West Semitic *ʿṣr 'to press, restrain, retain'", "note": "The root box is right on all three counts: the Arabic verb عَصَرَ ʿaṣara 'he pressed, squeezed' is real, the language label is right, and the gloss 'to squeeze (the juice out)' is almost word for word the gloss of the AHD Appendix of Semitic Roots ('ʿṣr — West Semitic, to press, restrain, retain … alizarin, probably from Arabic al-ʿuṣāra, the juice, from ʿaṣara, to squeeze'). Two refinements. (a) The root is not specifically Arabic but common West Semitic: AHD labels it West Semitic and Klein, s.v. alizari, compares Hebrew ʿātzar, Aramaic-Syriac ʿătzar 'he retained' — so 'Arabic' should read 'Arabic (West Semitic)'. (b) The derived noun is vocalised ʿuṣāra عُصَارَة by AHD and by Wiktionary, ʿaṣārah by Klein; Nourai follows Klein's a-vocalism ('a`sârah'), and since both variants are attested this is not an error, only a choice of source. The European branch of the chart (Sp. → Fr. → Eng. alizarin) is Klein's and AHD's account, but AHD hedges it with 'probably', Dozy explicitly declared the origin unknown, and Wiktionary/Webster's 1913 now prefer an Ottoman-Turkish route — see node #3.", "note_fa": "ریشهٔ «ع ص ر» به معنای «فشردن، آب چیزی را گرفتن» ریشه‌ای اصیل و درست است و برچسب زبانی و معنای آن در نمودار نورایی با آنچه پیوست ریشه‌های سامی فرهنگ American Heritage می‌آورد یکسان است؛ تنها نکته آن است که این ریشه ویژهٔ عربی نیست و سامی غربی است (کلاین هم عبری «عَصَر» به معنای «نگاه داشتن» را هم‌ریشهٔ آن می‌داند). گونهٔ اسمی آن در فرهنگ‌های امروزی عُصارة و در کلاین عَصارة ضبط شده و نورایی ضبط کلاین را برگزیده است؛ هر دو ضبط پذیرفتنی است و خطا نیست. شاخهٔ اروپایی این نمودار (اسپانیایی ← فرانسوی ← انگلیسی alizarin) از کلاین گرفته شده، ولی همان‌گونه که در گرهٔ ۳ گفته می‌شود، این بخش قطعی نیست و ویکی‌واژه امروزه راه دیگری (از راه ترکی عثمانی) پیشنهاد می‌کند. در مجموع ادعای نورایی دربارهٔ خودِ ریشه درست است.", "sources": ["https://www.ahdictionary.com/word/semitic.html", "https://www.ahdictionary.com/word/search.html?q=alizarin", "https://en.wiktionary.org/wiki/عصارة"], "ref_check": [{"ref": "KLN:50", "status": "supports", "note": "KLN_1966.txt, form-feed leaf 38 (two printed pages per leaf ⇒ printed pp. ~52-53, i.e. Nourai's p.50 ±2): 'alizari, n., madder root. — F., fr. Sp. alizari, fr. Arab. al-'aṣārah, \"the juice\", fr. al-, \"the\", and aṣara, \"he squeezed, pressed\", which is rel. to Heb. ʿātzar, Aram.-Syr. ʿătzār, \"he retained\".' Exactly the root, the gloss and the Romance chain Nourai draws."}, {"ref": "FVA:273", "status": "not_checked", "note": "FVA = S.M. Nahvi, Farhang-e vāžehā-ye ʿarabi dar fārsi (1368/1989). refs_online.json records no digital copy on archive.org, ketabnak, noorlib or the open web; catalogue record only (OpenLibrary OL2012991M)."}], "nodes": [{"id": 1, "lang": "Arabic", "words": "a`sârah; al-a`sârah", "verdict": "confirmed", "derivation"
```


## [2026-09-05T05:23:59.580Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== POK_full lemma aues\"; grep -n -i \"lemma: *au.es\" POK_full.txt | head -20; echo \"=== POK_full lemma ues-r\"; grep -n -i \"lemma: *u.es-r\\|lemma: *ues-r\\|lemma: *u̯es-r\" POK_full.txt | head -20; echo \"=== grep Frühling lemma\"; grep -n \"Frühling\" POK_full.txt | head -30",
 "description": "Grep Pokorny full text"
}
```


### [2026-09-05T05:23:59.745Z] TOOL RESULT

```
=== POK_full lemma aues
=== POK_full lemma ues-r
=== grep Frühling lemma
```


## [2026-09-05T05:24:00.907Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== POK_01 leaf for p.86 (leaf 94)\"; awk 'BEGIN{RS=\"\\f\"} NR==95' POK_01.txt | head -60",
 "description": "Print Pokorny p.86"
}
```


### [2026-09-05T05:24:02.872Z] TOOL RESULT

```
=== POK_01 leaf for p.86 (leaf 94)
 f.  ,Nach- kommenschaft,  Zins^  (vgl.  gr.  To-Aog  in  denselben  Bedeutungen),  ahd. wuohhar  m.  ,Ertrag  des  Bodens,  Leibesfrucht,  Nachkommenschaft,  Ge- winn, Zins,  Wucher^  (dazu  steir.  wiech  ,ausgiebig,  üppig,  blätterreich*^ als  Umlaut?  Etwas  anders  Schroeder  Abi.  57  f.),  da  in  der  nicht  mit  s erweiterten  Wzf.  aiieg-  die  Stufe  iteg-  in  air.  /er,  cymr.  gioair  ,Gras'^ belegt  ist;  Avohl  mit  derselben  Ablautstufe  ai.  vcija-h  ,Kraft,  Gut,  Reich- tum, Wettpreis,  Wettlauf^,  ursprüngl.  ,rasche,  erfolgreiche  Energie^,  Olden- berg  ZdMG.  50,  443  ff.
WP.  I  22  f.,  WH.  I  82 f.,  850,  Feist  67,  541,  572,  Pedersen  Tochar.  227.
86
auei-  (ouei-?)  ^YogeF.
Ai.  vi/i^  vBh  m.  ,Vogel'  (Gen.  ve/i,  Akk.  vim),  av.  vis  ds.  (G.  PL  vayam^ auch  mit  themat.  Kasus  vom  St.  vaya-),  mpers.  vCii,  väyandalz  ;Vogel', ai.  vayas-  n.  ^Geflügel,  Vogel",  väyasa-h  ,Vogel,  Krähe';  verbal  av.  ä-vayeiti ^fliegt  heran'  (von  Gottheiten),  ai.  vevlyate  ^flattert'.
Gr.  alsTÖg  ,Adler',  att.  äsrögj  alßsrög'  äsrog'  IleoyaXoi  fies.  {^afi-ez6g), alb.  vi-do,  vito,  vidheze  ,Taube';
lat.  avis   f.  ,Vogel'   (davon   auca   ,Vogel,   bes.  Gans';    Rückbildung   aus Demin.  aucella  aus   *avicella'^   falsch  bei  WH.  I  79)  =  umbr.  avif  Akk.; PI.  ,aves'  (aviekate  D.  Sg.  ,auspicatae',  avieJda  ,augurali');   cymr.  hwyad,- acorn.  hoet,  bret.  houad  ,Ente'  aus  "^auietos?    (Pedersen  KG.  I  55).  Arm.' hav  ,Vogel,  Hahn,  Henne'  kann  zwar  Vorschlags-Ä  haben,   aber   auch  als *^9w-  zu  *'pöu-  , Junges'  (slav.  jnta  , Vogel'  usw.)  gehören.  ]
Im  Zusammenhang  damit  stehen  höchstwahrscheinlich  die  Worte  für ,Ei',  s.  unter  öu-.
WP.  I  21,  WH.  84,  850.
aues-  ,leuchten',   bes.    vom  Tagesanbruch;    aus-,    tfes-,    us-;   (a)us-ös-   f. ,Morgenröte';   *aus-tero-  ,östlich'  (von   einem  Wznomen  *aus-j  oder als  zum  s-Stamm  gehöriges  *aiis-[e]s-^e?'0-  aufzufassen?   s.  Brugmann 11^  1,  327,   wonach    diese   -<ero-Bildung   vielleicht   erst    durch   Nach- ahmung   der    auf   Adverbien    fußenden   Richtungswörter   wie   anord. vestr,  nor-dr  aufgekommen  ist);  auso-  ,Gold'. Ai.    usah    f.    Akk.   usäsam^    Gen.    usdsah    ,Morgenröte',    av.    usä^    Akk. uMvhdm,  Gen.  usaidhö  ds.  {usas-tara-  ,östlich'),  woneben  ai.  Gen.  Sg.,  Akk. PI.   usdh,   av.    Lok.    Sg.  usi-[ßä,  s.  *demä-  ,bauen']    entweder   von   einem Wznomen  *W5-,  oder  als  *us-s-  zum  s-St. ;  ai.  ucchdti  =  av.  usaiti  (*us-sketi) ,leuchtet  auf  (vom  Morgen)',  Perf.  ai.  uväsa^  Aor.  avasran  ,sie  leuchteten'; usar-j  usr  ,Morgenröte,  Morgenfrühe',  us
```


## [2026-09-05T05:24:11.606Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==96' POK_01.txt | head -40",
 "description": "Pokorny p.87"
}
```


## [2026-09-05T05:24:13.182Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for n in 406 408 409 410 411 412 413; do echo \"### NR=$n\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N' POK_03.txt | head -5; done",
 "description": "Locate Pokorny p.1174 in POK_03"
}
```


### [2026-09-05T05:24:13.495Z] TOOL RESULT

```
ar-hudh-  ,früh  wach',  usrd-  ^mor- gendlich, rötlich',  auch  figürlich  ,Kuh',  m.  ,Stier'  (Frisk,  Nominalbildung  3); ues-,  uös-  in   ai.  vasar-hdn-   ,in   der   Morgenfrühe    schlagend',   väsard- ,morgendlich',    m.  ,Tag'    (vgl.  dazu    auch    den    wurzelverwandten    r/n-St. *ues-r-j  ues-n-  ,Frühling'  unter  besonderem  Schlagwort);
gr.  hom.  ijihg  *(äusös)j  Gen.  ijovg  ('^jöog)^  att.  (mit  Akzentneuerung)  fwg, dor.  ^wg,  äJ^coQ,  ablautend  äol.  a'ijcüg  ,Morgenröte'  (urgr.  av[o]d)g),  böot.  cla und  ^laiT]  (^daiT])]  IxyxavQog  ,dem  Morgen  nahe',  al'giov  ,morgen'  (*avoQ-)', hom.  }ji6  Oolße  ,morgendlich  strahlender';  iji-yiavog  ,Hahn'  {*ausi-  ,in  der Morgenfrühe  singend');
lat,  auröra  f.  ,Morgenröte'  (für  *äusösa)]  auster  (*aus-t(e)ro-  =  germ. *austra-)  ,Südwind',  austrälis  ,südlich';  vermutlich  auch  aiirum,  sabin. ausom  ,Gold'  als  /^rötlicli^ ;   zu  lit.  duksas   (k  unerklärt)^  alit.  ausas^  apr.
87
aiisis  _,Gold^;  vielleicht  tocli.  A  was  ^Gold^^  aber  vgl.  arm.  os-Jci  ^Gold^^ fiua.  vas-Jci  ^Kupfer'^;  vielleicht  Vesuvius  (anders  unter  eus-  _,brennen^);
mir.  fi^'^  ^Sonnenaufgang'^^  cymr.  gwawr  ^MorgenrÖte^,  bret.  gwere  laouen Morgenstern*^  (*uösri-^  Pedersen  KG.  I  82);
o-erin.  *aust7^ö  in  ags.  easti^e  ^Frühlingsgöttin'^^  eastron  PI.  ^Ostern^  = ahd.  öst{a)raj  öatarün;  dagegen  mit  idg.  -t{e)ro-,  ahd.  östar  ^östlich^  und ^(i\r.  ,nach  Osten^^  nhd.  Oster-reich,  anord.  austr  n.  ^Osten*^  und  Adv.  ;,ost- wärts*,  ags.  Komp.  easterra  ^östlicher''^,  dazu  Ostrogothae^  älter  Austrogoti als  ;die  Östlichen  Goten'';  ahd.  östan  ^von  Osten^,  ags.  easte  f.  _,Osten^^ anord.  austan  ^von  Osten  her^;  *äusös  in  ags.  earendel  ,Morgenstern'_, ahd.  MN  Orendil]
lit.  ausrä  f.  ^Morgeiiröte^_,  austa  ^es  tagt^^  lett.  äust  ds.;  lit.  auHrinis (vBjas)  ^Nordostwind^;,  lett.  äustra  f.  _,Morgendämmerung^_,  äustrums  m. ,Ostea^;  im  Ablaut  zem.  ajpymriai  m.  ;,Morgendämmerung^;
aksl.  za  ustra  ,xd  tcqüS'C'  (über  utro,  jiitro  _,Morgen^  aus  *aus(t)ro-  vgl. Trautmann  19^  Mikkola  Ursl.  Gr.  179  und  Berneker  462 L  m.  Lit._,  wozu Brückner  KZ.  4Q,  212^  der  aus  poln.  uscic  ^glänzen^  ein  sl.  *usto  ^Glanz^ erschließt),  ustin)  ^aestivus*^  (s.  Pedersen  IF.  b,  69).
Vgl.  zum  Ablaut  J.  Schmidt  KZ.  25,  23  f.,  Hirt  Abi.  134,  147,  Reichelt KZ.  39,  69.
WP.  I  26 f.,  WH.  I  86,  87  f.,  Trautmann  19,  Specht  Dekl.  10,  Wacker- nagel-Debrunner  Ai.  Gr.  HI  213  und  281  f.,  Kretschmer  Gl.  27,  231; Leumann  IF.  58,  121  ff.,  Schwyzer  Gr.  Gr.  I  349,  514,  557.
SLüg'  ,gläazen;  sehen^.
Gr.  avyrj  , Glanz,  Strahl,  Tageslicht;  Auge^,  (xvyaC,(ü  ,strahle,  erhelle; sehe^,  8Qi-avyrjg  ,sehr  glänzend^;
a
```


### [2026-09-05T05:24:15.056Z] TOOL RESULT

```
### NR=406
  Schwärm',  vielleicht  der  GN Vdi^una-  als  ,der  Binder*  (wie  Miti^a  oben  S.  710);  hierher  auch  ai.  uru- sydti  ,befreit,  erlöst,  rettet'  als  uru-s-ydti,  ^/g\.  hitt.  uarressesta  ,protected'; über  ai.  Vdruna-  s.  Wackernagel-Debrunner  II  2,  S.  485  (zu  lär- , Wasser', oben  S.  80);
gr.  vielleicht  evgcbg,  -cjrog  , Schimmel,  Moder',  wenn  eigentlich  ,Bedecker' (wäre  *i-J^Qü)-T-^  vgl.  ai.  arnö-vrt  ,die  Fluten  einschließend*);
fegv-  in  hom.  EQva&ai  , abwehren,  retten,  bewahren',  Impf.  sQv-ao,  -to, themat.  geworden  iQ'öszOj  Perf.  siQV[.iaL  (^J^e-J^qv^ai),  ion.  eigvof^ai  (*iJ^e- Qvofiat)  ,halte  fest,  bewahre*,  egvfxa  ,Schutz,  Schutzwehr',  igvfj^vög  ,geschützt, befestigt',  igvoi-nToXig  , stadtschützend';  Eigvoi-laog,  Eigv-Xaog  u.  dgl. {i-fQV-);
andere  Ablautstufe  Sqv-  ohne  Vokalvorschlag  in  Inf.  hom.  gvod-ai,  hom. ion.  QVOf.iaL  , schirme,  errette;  halte  fest,  halte  zurück*  (letztere  Bed.,  die auch  der  Ä;-Erweit.  kqt'/.o}^  iQVx,avtü,  iQvytavdcj  ,halte  ab,  zurück',  Pass. , zögere* innewohnt,  aus  , durch  einen  Verschluß  fernhalten,  abwehren'),  Perf.  sigvi-iaL (*fs-fQ'Dii<xij)  QVf.La  , Schutz,  Schutzwehr',  g'ßatog  , schützend,  rettend',  qiitcüQ^ QVTTjQ  ,Retter,  Befreier',  gvolrtoXig  ,stadtschützend';  dehnstufig  '^qIov  , Grab- hügel';
alb.  varr  ,Grab'  (*uorna),  vathe  , Gehege';
### NR=408
f.;  hierher  wohl  urek-.
7,  uer-  , aufreißen,  ritzen',  Grundlage  für  Erweiterungen:
A.  uerd-:  av.  varddva-  ,weich,  locker*,  aksl.  vr^d^,  russ.  vered  , Wunde'; ytred-'.  ai.  avradanta  ,sie  wurden  weich*,  vrandin-  ,mürbe  werdend^* ured-:  apr.  redo  , Ackerfurche',  älter  dän.  vraade,  vrode  , wühlen,  auf- bohren*; uröd-:  lat.  rödöj  -ere  ,nage,  verzehre',  röstrum  (*röd-trom)  n. ,Nage Werkzeug,  Schnauze,  Schnabel',  ags.  wrötan  , wühlen,  graben',  aisl. röta  ds.,  ahd.  ruozit  ,suscitat,  movet',  ags.  wrötj  mhd.  ruozel,  rüezel,  nhd. Rüssel  (*im^ötila-)]  dazu  die  Schwundstufe  in  schwed.  dial.  rota,  ruta , wühlen*;  nach  Frisk  (Etyma  Armen.  30)  dazu  noch  arm.  gercum  , rasieren' aus  *uerd-s-  (ursprüngl.  Aoristbildung).
B.  uornä:  alb.  varre  ,Wunde',  russ.  vorond  ,Ruderloch  im  Schiffsheck, Hennensteiß'  (davon  vorönka  , Trichter'),  poln.  wrona,  öech.  vrana  , Öffnung'; ure-no-,  uro-no-  in  ai.  vrand-  m.  n.  ,Wunde,  Riß'  neben  uro-nä  in  aksl. russ.  usw.  rana  ,Wunde'.
C.  uergh-:  ai.  vrhdti  ,reißt  aus*,  Aor.  varhi,  Partiz.  vrdhd-,  müla-vxt ,die  Wurzeln  ausreißend'  (Wackernagel  KZ.  67,  166  ff.).
### NR=409
�r  STtiogog  nach  o^gog)  ,£gjoooc Aufseher',  cpqovqog  ,Wächter*  {^Ttqo-bqoq),  (fQOvqä  , Schutz',  o^Qog  ,Wächter* (aus  Kompositis  abstrahiert),  dor.  zli^iäogog,  att.  rlf.ia}QÖg  ,Ehrenwäcbter Retter'  {föqog  =  germ.  wara-  s.  u.),  bqaci)  (iwowv,  eögGTia)  ,sehe*  (Denominativ eines  auch  in  cpQovqd  steckenden  *foQ&  =  ahd.  as.  wara,  ags.  waru ,  Aufmerk- samkeit') äol.  freilich  ^Qrjiiiy  ähnlich  wie  lat.  vereri]  dehnstufig  att.  Ö^a,  ion. ÜQTi  ,Hut,  Sorge'  hom.  o-bdsvög-wqogy  ovösvdg  öjgav  e^wv, nichtsnutzig',  dhycjQdtii _,vernachlässige'  von  ^öXLycoQÖg  ^dXlyrjv  öjgav  l'^w^  allenfalls  d^vQwgögj  nvX(aQ6^ ,Tür-,  Torhüter*  (eher  wegen  hom.  Ttvlscogög  an  -d-VQrj-,  TtvXrj-OQÖgj  ent- sprechend dem  Tl^cüQÖg)]  (hgeveiv  ,cavere';  ßwqoi  dq}d^aX(AoL  Hes.  Suid.
lat.  vereor,  -erl,  -itus  sum  , verehren,  fürchten';  zur  Form  vgl.  gr.  äol. {J^)i)Qr]^L  ,sehe';
air.  cö{a)ir  ,passend,  richtig':  cymr.  cywair  ds.  (*Äom-WeHos);
germ.:  uorösingot.iüar(5),behutsam',aisl.vörrr, behutsam, vorsichtig, scheu*, ags.  wcer  , gewahr,  aufmerksam,  vorsichtig,  behutsam*,  as.  war  ,vorsichtig,  auf der  Hut*,  ahd.  giwar  , aufmerksam,  vorsichtig*  ==  (J^ögog)]  üorä  in  got.  warai »Behutsamkeit,  List',  mhd.  wer  (ahd.  *wari)  , Vorsicht';  ags.  waru^  as.  ahd. wara  , Aufmerksamkeit,  Obhut*,  wara  neman  ^wahrnehmend ,  aisl.  vara  f. , Handelsware,  Zahlungsmittel',  ags.  loaru,  spätmhd.  war^  nhd.  Ware)  ahd. hewarön  fiewahren',  as.  warön  »beobachten,  wahren,  behüten*,  ags.  loarian ,bewahren,  hüten*,  aisl.  vara  ,aufmerksam  machen,  wahren,  vermuten*,  refl. jSich  hüten';  *uortos  (*uordhos)  in  got.  daurawards  , Torwart',  ahd.  wari , Wächter,  Wärter,  Hüter',  warto,  got.  wardja  ds.,  as.  wardön  ,auf  der  Hut sein,  behüten',  ahd.  warten  , achten,  spähen,  wahrnehmen,  warten,  erwarten*, warta  , Beobachtung  usw.',  nhd.  Warte  u.  dgl.;  "^iiorn-  in  ahd.  furiwama ,Vorbereitung'  (ags.  wearn  f.  »Widerstand,  Verweigerung,  Vorwurf,  nhd, warnen  usw.  durch  Einmischung  von  Angehörigen  von  *warjan  wehren  us^.*, und  Wz.  *wer-  »verschließen') ;
lett.  veru,  vert  ,schauen,  bemerken'  (meist  reflexiv  verties),  rM^a »Aufmerksamkeit' ;
### NR=410
- ata-  ,weit  umherschweifend';  PN  Urvdsl  f.  aus  *uru-väii-  »starkes  Ver- langen';   dazu   ulükhala-   ^Mörser*   aus    *urü-khara-   ,mit  breitem  Boden'-
mit  Metathese  gr.  si-  (wie  in  c^/cjxw,  4.  uer--  vgl.  £%ö-/-  unter  5.  uer-) in  fit'^^g  (statt  Vs^vg) , breit',  sowie  in  sigogn. , Breite' (s.  darüber  Seh wyzer  Gr. Gr.  1,  412  Anm.  1);  vielleicht  toch.  A  ivärts^  B  aurtse  ,weit,  breit'.
Neutrum:   ueros-  in  ai.  vdras-  n.  ,Breite,  Raum'  (gv.  sdgog  statt  ^fsgog);
unsicher  Uetos-  , Brust'  in  ai.  uras-  (aus  *vuras),  av.  varö  ds.  und  ai. vdriman-  m.  n.  ,Weite,  Umfang',  vdrivas-  n.  ,Raum,  Weite,  Behaglichkeit', die  eine  schwere  Basis  voraussetzen.
WP.  I  285,  Mayrhofer  109  f.,  Thieme  Lg.  31,  439.
### NR=411
 351
Vasmer  1,  184.
13.  uer-  , brennen,  verbrennen,  schwärzend
Arm.  varem  , zünde  an^,  varim  , brenne';  vielleicht  alb.  vorhe  ,Kochtop(* und  (?)  germ.  ^uarma-  ,warm'  in  got.  warmjan  ,wärmenS  aisl.  varmr  afr. as.  ahd.  warm  ,warm',  ablautend  ahd.  lolrma  ,Wärme'  (^wirmia)  und  wirmina mhd.  wirme  und  wirmen-^  vgl.  (?)  aisl.  orna  ,warm  werden,  wärmen'» aksl.  var^  ,Hitze',  variti  ,kochen'  (anders  oben  S.  81);  dazu  auch  balto* slav.  uarna-  m.  ,Rabe'  in  lit.  vafnas,  apr.  Vok.  warnis,  Akk.  PI.  t/xzmtnt aksl.  vram,  russ.  vöron,  wohl  ein  substantiviertes  Adjektiv  *uama' , schwarz,  verbrannt'  in  aksl.  vram,  russ.  voronöj  , schwarz*  usw.;  mit Dehnstufe  (Vriddhi)  femin.  bsl.  *uärnä-  ,Krähe*  in  apr.  loarne  (sekundärer e-Stamm),  lit.  vdrna,  russ.  ksl.  vrana,  serb.  vräna,  russ.  voröna  (Stoßton durch  Vriddhi);  hitt.  uar-  , brennen,  verbrennen',  Partiz.  uarant-  »brennend* (Intrans.),  uar-nu-  , anzünden,  verbrennend
WP.  I  269,  Trautmann  343,  361,  Vasmer  1,  169,  228  f.,  Szemer^nyi Kratylos  2,  121  f.,  der  auch  germ.  *swarta- , schwarz^  (anders  oben  S.  1062) dazustellt.
### NR=412
r  Körper,  Weberschiffchen'-
cymr.  givraidd  ,Wurzeln^  {*urddio-),  Singulativ  gwreiddyn,  acorn.  grneiten gl.  radix,  mbret.  gruizyenn,  nbret.  grisienn;  cymr.  ^lürys^  ,Äste,  Zweige* (*urd-sko-)',  air.  mir.  /ren  ,WurzeF  (*wrci-7zo-),  jünger /rem;  cym'r.  greddf , Instinkt,  Natur'  (*urd-mä-',  also  vielleicht  ursprüngl.  -wn-Suffix,  vgl.  oben gr.  Qccdafivog)]
got.  waürts  ,WurzelS  ags.  ivyrt,  ahd.  würz  ,Kraut,  Pflanze',  mhd.  auch ,Wurzel^  ahd.  wurzala,  ags.  wyrtwalu  (eig.  ,Kraut-stock')  , Wurzel'  (hierher auch  as.  wurtia,  mhd.  loilrze  ,Würze',  woneben  ablautendes  as.  icirtea,  mhd. vnrze  ds.;  neben  diesen  auf  ^u^rdd-  beruhenden  Formen  steht  *ur{9)d-  in aisl.  urt  ,Kraut*;  aisl.  röt  ,Wurzel';
toch.  B  vntsako  , Wurzel'.
WP.  I  288,  WH.  II  414,  415,  416,  Pokorny  ZcP.  26,  Iff.
### NR=413
 £-)  UQyo),  att.  B^iqyo)  ,schlieCe ein,  aus,  halte  ab*,  att.  «l^xr?;,  ion.  Iq-attj  , Gefängnis',  att.  eigyiiög    GefänffTi* Verschluß',  kypr.  ka-te-vo-ro-ko-ne  ,sie  belagerten';  dazu  air.  fraig   Wand*' nir.  fraigh  ,Wand  aus  Flechtwerk,  Dach,  Hürde',  wegen  mcymr.  ach-vi^ ,wattled  fence'  aus  "^uregi-  (Loth  RC.  38,  301).
WP.  I  290,  Frisk  465 f.;  Benveniste  BSL.  52,  34;  vgl.  uergh-  oben  S.  11B4.
2.  uerg-j  ureg-  ,wirken,  tun';  uergom  n.  ,Werk'.
Av.  vardz-  {vdrdzyeiti  =  got.  lüaürkeip-^  s.  auch  gr.  ^iCu))  , wirken  tun machen',  Partiz.  varsta-,  var9za-  m.  , Wirken,  Verrichten  von,  Tätigkeit' (npers.  ra?'^,  barz  , Feldarbeit,  Ackerbau'),  varsti-  f.  , Handeln,  Tun',  varitva- Adj.  ,was  zu  tun  ist';  arm.  goi-c  ,Werk'  (mit  sekundärem  o);  gr.  foy(^ fiqyov  ,Werk,  Arbeit'  (=  dt.  Werk),  igyd^ofxaL  ,arbeite^,  danach  ^^chiyy , Arbeiter'  (für  *eQyÖTr]g),  egdio  (vereinzelt  egöcü)  ,tue,  opfere'  (V«^zdw,  *'^erSiö Hochstufe  nach  fiqyov  wie  in  as.  wirkian)^  Fut.  i'jofw,  Aor.  I'io^cr,  Perf.  ^o^a), qe^o)  ,tue'  (aus  qi^ai  neugebildet,  hom.  äqs'/.Tog  ,ungetan*  umgestellt  aal *&'[/] €^xros);  ÜQyavov  ,Werkzeug',  b'gyia  , (geheimer)  Gottesdienst',  d^icfcfw ,feiere  Mysterien',  öqysibv  ,Mitglied  einer  religiösen  Brüderschaft';  <3^cfjw, ion.  dqy&ü),  ögyiCco  , knete,  rühre  durch,  gerbe'  (wie  nhd.  Teig  wirkm^ mit  Bed.-Verengerung  in  der  Berufssprache),  wozu  iöqyr]  , Quirl'  (wohl redupl.  S^e-fögyo)]
alb.  rregj  , reinigen',  Mediopassiv  rregjem  , mühen,  streben'  (St.  E.  Maon Lg.  26,  382 f.);  abret.  guerg  ,efficax',  gall.  vergo-hretus  , oberste  Behörde der  Aeduer',  auch  verco-breto  (Pokorny,  Vox  Romanica  10,  266  f.) ;  mcjmr. gwreith  ,Tat*  (*ureg-tu-),  1.  PI.  Imper.  acymr.  guragun^  jünger  gionawn  u»w. {n  statt  r  durch  Einfluß  von  "^grn-  ,machen',  S.  373),  corn.  gruen,  mbr. gr(u)eomp  (*ureg-  , machen'),  Lewis-Pedersen  S.  336 f.;
```


## [2026-09-05T05:24:30.750Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"Frühling\" POK_03.txt | head -20; echo \"=== find leaf numbers\"; awk 'BEGIN{RS=\"\\f\"}/Frühling/{print \"LEAF(0based)=\"NR-1}' POK_03.txt | head",
 "description": "Find Frühling in POK_03"
}
```


### [2026-09-05T05:24:32.278Z] TOOL RESULT

```
3250:aisl.  springa  ,springen,  hervorbrechen',  ags.  as.  ahd.  springan  ds.  |  K&oi. ahd.  sprengen  ,springen' machen  (ein  Pferd),  (zer) sprengen'  und  ,streueil^ spritzen,  sprenkeln',  aisl.  sprengja  »sprengen',  ags.  sprengan  jausbreitttSj bersten;  sprengen,  säen';  mhd.  sprinc  (-g-)  , Sprung,  Quelle',  ags.  spring , Wasserquell',  engl,  spring  ,ds.,  Sprungfeder,  Knospenspringen,  Frühling'; alte  Ablautform  *sprögh-  in  aisl.  spröga  , springen,  rennen'.
5946:Ai.  vasan-td-  m.  (%es-en-^o-)  ^FrühlingS  vasantä  ,im  Frühling'*(aus  *vaMan- erweitert);  vasar-hdn  ,irüh  schlagend^,  väsard-  ,morgendlich'*
5947:av.  vaTari  Lok.  ,im  Frühling'  {*vasri  für  älteres  "^vasar,  vgl.  npers.  bahar mit  Quantitätsumsprung  aus  *vähar,  vgl.  apers  d-üra-väkara-)'
5948:arm.  garun  (^uesr-)j  Gen.  garnan  ^Frühling*;
5949:gr.  eaq,  laqog,  auch  ^igog,  ^qi  mit  neuem  Nom.  ^^;  yi^q  Hes.  (♦/«<rao) ^Frühling*,  iagivög  ,zum  Frühling  gehörig*;
5950:lat.  ve?',  veris  n.  ,Frühling',  vernus  {*uerinos)  ,auf  den  Frühling  bezU«^lich**
5951:air.  errach  (lenierte  Form  von  yerrach)  ,Frühling*  {*uesr-äko-)\  acymr. guiannuin  ,im  Frühling'  {*ues-nt-eino-),  aber  mcymr.  gwaeanhicyn,  ncymr. gwanwyn  setzt  *gwaeant  aus  *ues-nto-  voraus;  acorn.  guaintoin  ,FrUhliii|r*'
5953:aksl.  vesna  ,Frühling';  *ueserinios  ,vernus*  in  lit.  vasartnis  ,sommerlich' lett.  vasariiM  m.  PL  , Sommergetreide',  vgl.  russ.-ksl.  vesnhnyjj  russ.  ve$4nnU , Frühlings-^;
=== find leaf numbers
LEAF(0based)=239
LEAF(0based)=418
```


## [2026-09-05T05:24:36.434Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==419' POK_03.txt | sed -n 1,60p",
 "description": "Print Pokorny leaf 418"
}
```


### [2026-09-05T05:24:37.947Z] TOOL RESULT

```
t.  vakars  , Abend'  aksl.  vecen, ds.,  wozu  Adv.  aksl.  vhcera  ^gestern'  usw.,  Grundbed.  vielleicht  , Dunkel', zu  lit.  ükanas  ,trübe',   ünkna   ,Schatten',   lat.   umhra  (*unksrä)  ^Schatten';
cymr.  ucher  ,Abend'  nicht  hierher,  sondern  aus  idg.  *uoiksero-  (Pokorny ZcP.  15,  377);  arm.  giser  ,Nacht'  aus  *uoikero-,  nach  Petersson  Hetero- klisie  231  ff.  zur  Wurzel  ueik-  ,feucht'  (?)  in  ai.  veiantd-  m.  ,Teich'  (vgl.  die FIN  lit.  VieSintä,  VieSmud  usw.),  aisl.  veig  ,berauschendes  Getränk',  lett. vieksts  ,Wasserstrudel'.
1174
f
WP.  I  311,    WH.  II   770f,   814 f.,    Trautmann  348,   Yasmer    1     196 Frisk  575;    der  Wechsel   uesperos  :  uekeros   vielleicht   nach    Specht    Id  ' Dekl.  119  tahuistisch  zu  erklären;  vgl.  auch  Havers  Sprachtahu  125    178* ues-^  (lat.-germ.  uer  nach  Her  ,Jahr'),  Gen.  ues-n-es  jFrühlino-*.
Ai.  vasan-td-  m.  (%es-en-^o-)  ^FrühlingS  vasantä  ,im  Frühling'*(aus  *vaMan- erweitert);  vasar-hdn  ,irüh  schlagend^,  väsard-  ,morgendlich'*
av.  vaTari  Lok.  ,im  Frühling'  {*vasri  für  älteres  "^vasar,  vgl.  npers.  bahar mit  Quantitätsumsprung  aus  *vähar,  vgl.  apers  d-üra-väkara-)'
arm.  garun  (^uesr-)j  Gen.  garnan  ^Frühling*;
gr.  eaq,  laqog,  auch  ^igog,  ^qi  mit  neuem  Nom.  ^^;  yi^q  Hes.  (♦/«<rao) ^Frühling*,  iagivög  ,zum  Frühling  gehörig*;
lat.  ve?',  veris  n.  ,Frühling',  vernus  {*uerinos)  ,auf  den  Frühling  bezU«^lich**
air.  errach  (lenierte  Form  von  yerrach)  ,Frühling*  {*uesr-äko-)\  acymr. guiannuin  ,im  Frühling'  {*ues-nt-eino-),  aber  mcymr.  gwaeanhicyn,  ncymr. gwanwyn  setzt  *gwaeant  aus  *ues-nto-  voraus;  acorn.  guaintoin  ,FrUhliii|r*'
lit.  väsara  und  vasarä,  lett.  vasara  , Sommer^  (*wesera-?)-
aksl.  vesna  ,Frühling';  *ueserinios  ,vernus*  in  lit.  vasartnis  ,sommerlich' lett.  vasariiM  m.  PL  , Sommergetreide',  vgl.  russ.-ksl.  vesnhnyjj  russ.  ve$4nnU , Frühlings-^;
über  hitt.  hamesh^a)-,  hameähant-  ^Frühjahr'  s.  A.  Goetze  Lg.  27,  471 51,  467  ff.,  F.  Sommer  M.St.z.Spr.  4,  7,  G.  R.  Solta,  S.-Ber.  österr.  Akad.,* Bd.  232,  1.,  16 f.;
WP.  I  301,  WH.  II  755,  Trautmann  356,  Vasmer  1,  192,  Frisk  432  f., 605 f.;  wohl  zu  aues-  ,leuchten*,  oben  S.  86 f.
uesu-  ,gut*.
Ai;   vdsu-   ,gut'   (dazu   vasvi  ,Nacht*),    vdsu   n.   ,Gut,   Besitztum,  Habe, Reichtum*  (das  Subst.  nach  Akzent  und  Ablaut  das  primäre),  av.  va^hu', vohu  ds.,  ai.  vaslyän  ,besser',  vasistha-  ,best',  av.   vahyäj  vahiStd  ds.J  alt- illyr.  Ves-clevesy  vgl.  ai.  vdsu-sravas-]  germ.  in  Eigennamen,  z.  B.  Wi9U-r%h, -mär,  auch   Wisi-Gothae-,  gall.  in  Eigennamen  wi
```


## [2026-09-05T05:24:52.600Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== KLN east\"; grep -n \"^east,\" KLN_1966.txt | head; echo \"=== KLN Easter\"; grep -n \"^Easter,\" KLN_1966.txt|head; echo \"=== KLN vernal\"; grep -n \"^vernal\" KLN_1966.txt|head; echo \"=== KLN aurora\"; grep -n \"^aurora\" KLN_1966.txt|head; echo \"=== KLN austral\"; grep -n \"^austral\\|^auster\" KLN_1966.txt|head",
 "description": "Grep Klein headwords"
}
```


### [2026-09-05T05:24:52.730Z] TOOL RESULT

```
=== KLN east
12551:east,  n.  —  ME.  east,  est,  fr.  OE.  east,  ‘in  the  east’ (whence  OE.  eastan,  ‘from  the  east’),  rel.  to  Du. oost,  oosten,  OHG.  ostan,  MHG.  osten,  G.  Ost, Osten,  ‘east’,  OHG.,  OS.  ostar,  ‘to  the  east’,  ON. austr,  ‘from  the  east’,  fr.  Teut.  *austa-,  ‘east’, which  is  rel.  to  I.-E.  *ausos,  ‘dawn’,  whence  OI. ufdh,  Gk.  gto;,  Homeric  Gk.  Y]d>;  (for  *dusbs), Lith.  auSra,  ‘dawn’,  L.  auster,  ‘south',  aurum  (for *ausom ),  ‘gold,’  lit.  ‘the  reddish  metal’,  aurora (for  *ausosa),  ‘dawn’.  Cpnext  word  and  the  first element  in  Ostrogoth.  Cp.  also  aureate,  aurora, Auster,  austral,  eo-,  Eos.
=== KLN Easter
12553:Easter,  n.  —  ME.  ester,  estern,  fr.  OE.  easier, eastre,  ‘Easter’,  fr.  OE.  Eastre  (usually  in  the  pi. Eastron),  a  Teutonic  goddess  of  spring  (orig. the  goddess  of  dawn);  rel.  to  OHG.  ostariin, MHG.  osteren,  G.  Ostern,  ‘Easter’,  and  to  E. east  (q.v.)
=== KLN vernal
=== KLN aurora
=== KLN austral
4008:austere
4011:austere,  adj.,  stem,  severe;  very  simple.  —  OF. austere  (F.  austire),  fr.  L.  austerus,  ‘dry,  harsh, sour,  tart’,  fr.  Gk.  auax^pit;,  ‘harsh,  rough, bitter’,  fr.  aiisiv,  ‘to  dry’,  fr.  auo<;,  ‘dry’.  See auantic.
4013:austerity,  n.,  the  quality  of  being  austere.  —  OF. austerite  (F.  austiritfi),  fr.  L.  austeritatem,  acc. of  austeritas,  fr.  austerus.  See  prec.  word  and  -ity. Austin,  tnasc.  PN.  —  Abbreviation  of  Augustin (qv.)  ...
4014:austral,  adj.  southern;  southerly.  —  L.  australis, ‘southern’,  fr.  auster,  ‘south  wind’.  See  Auster and  adj.  suff.  -al  and  cp.  next  word.
```


## [2026-09-05T05:24:54.168Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== BRT vanhar/vanri\"; grep -n \"va\\(n\\|ŋ\\|g\\)hara\\?-\\|vaŋri\\|vanri\" BRT.txt | head -20; echo \"=== BRT usah\"; grep -n \"usastara\\|uśastara\\|ušastara\" BRT.txt|head",
 "description": "Grep Bartholomae"
}
```


### [2026-09-05T05:24:54.252Z] TOOL RESULT

```
=== BRT vanhar/vanri
=== BRT usah
12565:(sd.)  . .  -iataire  Y.  57,  39;  —  hala  usastara
18490:•  j.  naema-  1)  Adj.  'halb':  '«am  bay^m Vd.  2;  —  'nam  ySr»  "ein  halbes  Jahr (lang)"  N.45i*44'^;  —  'mmi  yJn.drä/ä "eine halbe  Jahreslänge  (hmdurch)"  V. j.gö, ti.44i  42;  —  paourwn  va  'm^m  yän apar?m  va  "das  erste  Halbjahr  oder  das zweite"  N.  44)  —  pimrumca  'me  asne (bz.  xia/ne)  aparvmca  "die  eiste  Hälfte  des Tags  (bz.  der  Nacht)  und  die  zweite"  V. 4. 45*>.  3)  m.  a)  'Hälfte,  latus  alterum': ya(  vS  'mim  yat  va  'hri^wi  .  .  V,  if ,  32, 16.  2,  Y.  Jp.  7;  V.Äioi;  — aWsr  'mat.. uparät  *mat  y.i4.T,  6'.  8,  N.5_j,  P.  23;  — haoyat  hol  +*mS/3' . .  dalinat  hat  *'mai^ N.  75;  —  '^fraoirilarai  'mat  N.fi?;  — *aevahmat  'mat  N.  7p;  —  paurvat  va 'mat  aparät  va  ^.Jj;  —  antarä^  (sd.) 'm^  V.5.43»,  51,  6.2,  3,  7.77,  8.^1,  42, 104,5.15,  16,  N.öo,  6p',  *7jT,  54,  104^; II';  —  *va  *'ma  N.pp*';  —  vaHbya 'maltiya  "von  beiden  Seiten"  V./_y.3 1—37 PüZ.*;  —  apaxtarat  haca  *mat  V.ig.i, H.2.25,  FrW,/o.43";  V.j^.s,  H.2.7,  A. 4.6.  b)  'Seite'  überhaupt:  vlspe  'mq (AP.)  F.jg;  —  vlspa^työ  'maübys  Yl /0.41;  —  ahmst  'mäi ..yahmäi  'tnanqm YtJO.  19;  y.  3,  V.Ä80;  —  usastaratibyö haca  'maiiiys  V./p.5;  1,  H.2.  35,  V.7.  2, *i6,  FrW.JO.42.
```


## [2026-09-05T05:25:03.434Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\ndef leaf_of_line(ln):\n    return t[:sum(len(l)+1 for l in lines[:ln-1])].count('\\f')\nfor ln in [12551,12553,4014,4011]:\n    print(ln, 'leaf', leaf_of_line(ln), 'approx printed p', (leaf_of_line(ln)-12)*2)\nEOF\necho \"=== vernal/vernus\"; grep -n \"vernal\\|vernus\" KLN_1966.txt | head -10",
 "description": "Compute Klein leaves and grep vernal"
}
```


### [2026-09-05T05:25:05.291Z] TOOL RESULT

```
12551 leaf 270 approx printed p 516
12553 leaf 270 approx printed p 516
4014 leaf 80 approx printed p 136
4011 leaf 79 approx printed p 134
=== vernal/vernus
13511:Eranthemum,  n.,  a  genus  of  plants  of  the  family Acanthaceae  (bot.)  —  ModL.,  fr.  Gk.  rjpavbe- piov,  ‘a  camomile-like  plant’,  which  is  com¬ pounded  of  )jp,  ‘spring’,  and  &vf>E|zov,  ‘flower’. The  first  element  is  a  contraction  of  cap,  fr. orig.  *fiEnap,  and  is  cogn.  with  L.  ver,  ‘spring’; see  vernal  and  cp.  Eryngium.  For  the  second element  see  anther.
41258:Derivative:  veranda(h)-ed,  adj. verano,  n.,  the  dry  season  in  tropical  America.  — Sp.,  fr.  L.  ver,  ‘spring’.  See  vernal.
```


## [2026-09-05T05:25:18.648Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for L in 258 259 260 269 270; do echo \"#### leaf $L\"; awk -v N=$((L+1)) 'BEGIN{RS=\"\\f\"} NR==N' KLN_1966.txt | head -3; done",
 "description": "Print Klein leaves around 259 and 270"
}
```


### [2026-09-05T05:25:20.271Z] TOOL RESULT

```
#### leaf 258
and  theo-.  Dodecatheon  prop,  denotes  the  plant that  is  under  the  care  of  the  twelve  greater  gods.
dodge,  intr.  v.,  to  move  to  and  fro;  tr.  v.,  to elude.  —  Of  uncertain  origin.
Derivatives:  dodge,  n.,  dodg-er,  n.,  dodg-ery,  n., dodg-y,  adj.,  dodg-i-ly,  adv.,  dodg-i-ness,  n.
#### leaf 259
t.,  pres.  part,  of  doiere ,  fr.  L.  doiere.  See  prec. word.
dolerite,  n.,  a  coarse  form  of  basalt  (petrogr.)  — Formed  with  subst.  suff.  -ite  fr.  Gk.  8oXep6?, ‘deceptive’,  fr.  86X0?,  ‘deceipt’  (see  dole, ‘guile’);  so  called  because  easily  confused  with diorite.  Cp.  dolose.
dolicho-,  before  a  vowel  dolich-,  combining  form meaning  ‘long’.  —  Gk.  80X1/0-,  SoXt /-,  fr. 80X1x6?,  ‘long’,  rel.  to  ev-SeXe/it)?,  ‘continued; constant’,  and  cogn.  with  OI.  dirghah,  ‘long’, A\estic darega-,  Hitt,  daluga-,  ‘long’,  Hitt,  dalu- gashti,  ‘length’,  L.  in-dulgere,  ‘to  indulge’,  lit.,  ‘to be  long-suffering’,  Goth,  tulgus,  ‘firm,  steadfast’, OE.  tulge,  ‘firmly’,  OS.  tulgo,  ‘very,  much’, OSlav.  dliigu,  ‘long’,  Lith.  ilgas,  Lett,  ilgs, OPruss.  ilgi,  of  s.m.  Cp.  indulge.  For  connection with  L.  longus  see  long,  adj. dolichocephalic,  also  dolichocephalous,  adj.,  hav¬ ing  a  relatively  long  head.  —  Lit.,  ‘long-headed’, fr.  Gk.  80X1  yoc,,  ‘long’,  and  xs<pa Xf],  ‘head’;  see dolicho-  and  cephalic,  resp.  -cephalous.  The  term dolichocephalic  was  introduced  into  anthropo¬ logy  by  the  Swedish  anatomist  and  anthropo¬ logist  Anders  Adolf  Retzius  (1796-1860). Dolicholus,  n.,  the  same  as  Rhynchosia  (bot.)  — A  ModL.  hybrid  coined  fr.  Gk.  80X1/6?,  ‘long’ (see  dolicho-),  and  the  Latin  dimin.  suff.  -olus (see  -ole).  The  correct  form  is  Dolichidium, which  is  formed  fr.  80X1/6?  with  the  Greek dimin.  suff.  -iStov  (see  -idium).
#### leaf 260
  —  ML.  dominicalis,  ‘pertaining to  a  master  or  lord’,  fr.  L.  dominicus,  of  s.m., fr.  dominus.  See  dominus  and  adj.  suff.  -al.
Dominican,  adj.  and  n.  —  Formed  with  suff.  -an fr.  ML.  Dominicanus,  fr.  Dominicus,  Latinized name  of  Domingo  de  Guzman  (Santo  Domingo), the  founder  of  this  order  of  monks.  For  the origin  of  the  Latin  name  Dominicus  see  Dominic.
dominie,  n.,  1)  a  schoolmaster  (Scot.);  2)  a  clergy¬ man.  —  L.  domine,  voc.  of  dominus,  ‘master, lord’.  See  dominus.
#### leaf 269
for  measuring  the magnifying  power  of  telescopes.  —  Com¬ pounded  of  dyna-  and  Gk.  pixpov,  ‘measure’. See  meter,  ‘poetical  rhythm’.
Derivatives :  dynametr-ic,  dynametr-ic-al,  adjs. dynamic,  adj.  —  F.  dynamique,  coined  by  the German  philosopher  and  mathematician,  Baron Gottfried  Wilhelm  von  Leibniz  (1646-1716)  fr. Gk.  8ovaptx6;,  ‘powerful’,  fr.  Suvapi;,  ‘might, power’,  which  is  rel.  to  Sdvapai,  ‘I  am  able, I  am  worth’,  Suvaxo;,  ‘strong,  able’;  of  un¬ certain  origin.  Cp.  dyna-,  dynamite,  dynamo-, dynasty.  For  the  ending  see  suff.  -ic.  The  word dynamic  was  introduced  into  English  by  Jeremy Bentham  (1748-1832).
Derivatives:  dynamic,  n.,  dynamic-al,  adj.,  dy- namic-al-ly,  adv.,  dynamics  (q.v.),  dynam-ism, n.,  dynam-ist,  n.,  dynamite  (q.v.) dynamics,  n.,  that  branch  of  physics  which  deals with  the  action  of  force  on  bodies.  —  See  prec. word  and  -ics.
#### leaf 270
,  fr.  OE.  earnian, ‘to  deserve,  earn’,  rel.  to  OHG.  amen,  arnon, ‘to  reap’,  OE.  ern,  OHG.  aran,  arn,  G.  Ernte, ‘harvest’,  Goth,  asans,  ‘harvest,  summer’,  ON. bnn  (for  *aznu),  ‘work  in  the  field’,  and  cogn. with  OSlav.  jeseni,  Russ,  osen’,  OPruss.  assanis, ‘autumn’.
Derivatives:  earn-er,  n.,  earning,  n.  (q.v.) earnest,  n.,  seriousness.  —  ME.  ernest,  fr.  OE. eornost,  rel.  to  OS.,  OHG.,  ernust,  ‘struggle’, MHG.  ernest,  ‘struggle;  earnest’,  G.  Ernst, ‘earnest,  seriousness’,  Goth,  arniba,  ‘safely’,  ON. jama,  ‘fight,  combat’,  ern,  ‘able,  fit,  vigorous', orig.  ‘able  to  fight’.  Cp.  Ernest.
Derivatives:  earnest,  adj.,  earnest-ly,  adv.,  ear- nest-ness,  n.
```


## [2026-09-05T05:25:36.329Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for f in KLN_1966.txt KLN_1971.txt; do echo \"$f leaves: $(tr -cd '\\f' < $f | wc -c)\"; done; echo \"=== 1971 east\"; grep -n \"^east,\\|^Easter,\" KLN_1971.txt | head -3; python3 - <<'EOF'\nt=open('KLN_1971.txt',encoding='utf-8',errors='replace').read()\nimport re\nfor pat in ['\\neast,','\\nEaster,','\\nvernal','\\naustral,']:\n    i=t.find(pat)\n    print(pat.strip(), 'leaf', t[:i].count('\\f') if i>0 else 'NOTFOUND')\nEOF",
 "description": "Compare Klein editions"
}
```


### [2026-09-05T05:25:38.083Z] TOOL RESULT

```
KLN_1966.txt leaves: 902
KLN_1971.txt leaves: 0
=== 1971 east
23292:east, ‘east’; see aurora and cp. austral; cp. also 
78338:east, n. — ME. east, est , fr. OE. east, ‘in the east’ 
78357:Easter, n. — ME. ester, estern, fr. OE. easier, 
east, leaf 0
Easter, leaf 0
vernal leaf 0
austral, leaf 0
```


## [2026-09-05T05:25:51.439Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i in range(255,275):\n    nums=re.findall(r'(?m)^\\s*(\\d{3})\\s*$', leaves[i])\n    head=leaves[i].strip().split('\\n')[0][:40]\n    print(i, nums, '|', head)\nEOF",
 "description": "Find printed page numbers in Klein scan"
}
```


### [2026-09-05T05:25:53.390Z] TOOL RESULT

```
255 ['466', '467'] | uish (as  well  as  in  extinguish,  adm
256 ['468', '469'] | �  L.  diuturnitas,  fr. diuturnus.  See
257 ['470', '471'] | on  a  distaff  ( obsol .); 2)  to  bedi
258 ['472'] | and  theo-.  Dodecatheon  prop,  denotes
259 ['473', '474', '475'] | t.,  pres.  part,  of  doiere ,  fr.  L.
260 ['476'] | —  ML.  dominicalis,  ‘pertaining to  a 
261 ['477'] | —  F.  dormi,  pp.  of dormir,  ‘to  sle
262 [] | —  See  doom  palm.
263 ['480', '481', '483'] | oth.  ( ga)tarhjan ,  ‘to  make  distinc
264 ['484', '485'] | e,  ‘dregs,  lees’,  OHG. trestir,  MHG.
265 ['486'] | astis  and  in  lithontriptic. drop,  tr
266 ['487'] | the  stem  of  L.  dux,  gen.  duds, ‘le
267 ['488', '489', '490', '491'] | re  referred  to.
268 [] | icatid,  ‘a  doubling’,  fr.  duplicatus
269 [] | for  measuring  the magnifying  power  o
270 ['497'] | ,  fr.  OE.  earnian, ‘to  deserve,  ear
271 [] | fr.  L. eburneus,  ‘of  ivory’,  fr.  eb
272 [] | deals  with  animals  and  plants  in  r
273 ['501', '502', '503'] | he  ending  see  subst.  suff.  -ite.
274 ['504', '505'] | ?,  ‘an  absolute  master  or  ruler’.
```


## [2026-09-05T05:26:01.562Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i in list(range(76,84)):\n    nums=re.findall(r'(?m)^\\s*(\\d{3})\\s*$', leaves[i])\n    print(i, nums, '|', leaves[i].strip().split('\\n')[0][:50])\nprint('---- search vernal-ish')\nfor m in re.finditer(r'vern[ai]l|Fr[üu]hling|ver,\\s*.spring|,\\s*.spring.', t):\n    i=t[:m.start()].count('\\f')\n    if i>700: print(i, t[max(0,m.start()-120):m.start()+180].replace('\\n',' ')[:300]); print()\nEOF",
 "description": "Klein austral page and vernal in vol II"
}
```


### [2026-09-05T05:26:04.282Z] TOOL RESULT

```
76 ['123'] | n  anatomist  Andreas  Vesalius (1514-64).  See  J
77 ['124', '125', '126', '127'] | ust’,  fr.  ad- and  L.  temperdre,  ‘to  divide  
78 ['128', '129'] | L. aucupdtus,  pp.  of  aucupdre,  later  aucupari
79 [] | an  agential  suff.  -dar,  meaning ‘holder,  poss
80 ['130', '131'] | ple.  —  OF. austere  (F.  austire),  fr.  L.  aus
81 ['132', '133'] | ous-ly,  adv. autogeny,  n.,  autogenesis.  —  See
82 ['134'] | �� (see  Suetonius,  Claudius  2 1).  The  usual  
83 ['135', '136', '137'] | d  intr.  v.  —  OE.  awsecnan,  fr.  a- ‘on’,  an
---- search vernal-ish
709 ent’ (whence,  with  change  of  conjugation,  F.  resilier, ‘to  annul,  cancel’),  fr.  L.  resilire,  ‘to  leap  back, spring  back,  rebound’,  fr.  re-  and  satire,  ‘to leap,  spring’.  See  salient  and  cp.  result.  For  the change  of  Latin  a  (in  satire)  to  i  (in  re-silire)  see a

709  ‘to  annul,  cancel’),  fr.  L.  resilire,  ‘to  leap  back, spring  back,  rebound’,  fr.  re-  and  satire,  ‘to leap,  spring’.  See  salient  and  cp.  result.  For  the change  of  Latin  a  (in  satire)  to  i  (in  re-silire)  see abigeat  and  cp.  words  there  referred  to. resilience,  r

711 ess,  n. result,  intr.  v.  —  ME.  resulten,  fr.  ML.  resultare, ‘to  result’,  fr.  L.  resultare,  ‘to  leap  back,  spring back,  rebound’,  which  stands  for  *re-saltdre and  is  freq.  of  resilire,  ‘to  leap  back,  spring back,  rebound’.  See  resile  and  cp.  saitant.  For the  chan

711 to  leap  back,  spring back,  rebound’,  which  stands  for  *re-saltdre and  is  freq.  of  resilire,  ‘to  leap  back,  spring back,  rebound’.  See  resile  and  cp.  saitant.  For the  change  of  Latin  a  (in  satire  and  in  its  freq. saltare)  to  it  (in  re-sultare)  see  desultory  and

730 . salient,  adj.,  1)  projecting;  2)  conspicuous.  —  L. saliens,  gen.  -ends,  pres.  part,  of  satire,  ‘to  leap, spring',  which  is  cogn.  with  Gk.  a XXeaflm,  of s.m.,  aXux,  ‘a  leap,  spring’,  Toch.  A  sal-,  ‘to jump’,  Mir.  saltraim,  ‘I  trample’,  and  prob. also  with  OI.  

730 nds,  pres.  part,  of  satire,  ‘to  leap, spring',  which  is  cogn.  with  Gk.  a XXeaflm,  of s.m.,  aXux,  ‘a  leap,  spring’,  Toch.  A  sal-,  ‘to jump’,  Mir.  saltraim,  ‘I  trample’,  and  prob. also  with  OI.  ucchalati  (for  *ud-sa1ati),  ‘rises quickly’.  Cp.  Altica,  assault,  consi

731 nd  petra, ‘rock,  stone’.  See  salt  and  petro-. saltus,  n.,  a  leap,  a  break  in  continuity.  —  ModL., fr.  L.,  ‘spring,  leap’,  fr.  saltus,  pp.  of  salire,  ‘to leap,  jump’.  See  salient. salubrious,  adj.,  healthful,  healthy.  —  Formed with  suff.  -ous  fr.  L.  salubris,  ‘pr

740  skotu,  ‘cattle’,  which  is a  Teut.  loan  word).  Teut.  *skatta  ult.  derives fr.  I.-E.  base  *sqet-,  ‘to  gush,  spring,  bubble, yield,  result’,  whence  also  Lith.  skastu,  skasti, ‘to  leap,  jump',  archaic  L.  scatere,  L.  scatere,  ‘to gush,  spring,  bubble’,  Gk.  axxTxpi^S'.v

740 ield,  result’,  whence  also  Lith.  skastu,  skasti, ‘to  leap,  jump',  archaic  L.  scatere,  L.  scatere,  ‘to gush,  spring,  bubble’,  Gk.  axxTxpi^S'.v  (in Hesychius),  ‘to  leap,  jump’.  For  sense  develop¬ ment  cp.  result,  fr.  F.  resulter,  fr.  L.  resultare, ‘to  spring  back’.  

740 th.  —  L.  scaturiens, gen.  -ends,  pres.  part,  of  scaturire,  ‘to  stream, gush  forth’,  fr.  scatere,  ‘to  gush,  spring’.  See scat,  ‘tax,  tribute’,  and  -ent  and  cp.  prec.  word, scauper,  n.,  a  kind  of  engraving  tool.  —  A  var. of  scalper. scaur,  n.,  reef,  cliff.  —  A  

794  also  the  first  element  in  springbok  and  the second  element  in  klipspringer. Derivatives:  spring,  n.  (q.v.),  spring-er,  n., spring-ing,  adj.  and  n.,  spring-ing-ly,  adv., spring-y,  adj.,  spring-i-ly,  adv.,  spring-i-ness,  n., spring-less,  adj.,  spring-like,  adv. spring,  n.

794   element  in  springbok  and  the second  element  in  klipspringer. Derivatives:  spring,  n.  (q.v.),  spring-er,  n., spring-ing,  adj.  and  n.,  spring-ing-ly,  adv., spring-y,  adj.,  spring-i-ly,  adv.,  spring-i-ness,  n., spring-less,  adj.,  spring-like,  adv. spring,  n.,  1)  a  leap;  

794 d  the second  element  in  klipspringer. Derivatives:  spring,  n.  (q.v.),  spring-er,  n., spring-ing,  adj.  and  n.,  spring-ing-ly,  adv., spring-y,  adj.,  spring-i-ly,  adv.,  spring-i-ness,  n., spring-less,  adj.,  spring-like,  adv. spring,  n.,  1)  a  leap;  2)  source  of  water;  sour

794  in  klipspringer. Derivatives:  spring,  n.  (q.v.),  spring-er,  n., spring-ing,  adj.  and  n.,  spring-ing-ly,  adv., spring-y,  adj.,  spring-i-ly,  adv.,  spring-i-ness,  n., spring-less,  adj.,  spring-like,  adv. spring,  n.,  1)  a  leap;  2)  source  of  water;  source, origin;  3)  the  s

794 . Derivatives:  spring,  n.  (q.v.),  spring-er,  n., spring-ing,  adj.  and  n.,  spring-ing-ly,  adv., spring-y,  adj.,  spring-i-ly,  adv.,  spring-i-ness,  n., spring-less,  adj.,  spring-like,  adv. spring,  n.,  1)  a  leap;  2)  source  of  water;  source, origin;  3)  the  season  in  which 

794 g,  n.  (q.v.),  spring-er,  n., spring-ing,  adj.  and  n.,  spring-ing-ly,  adv., spring-y,  adj.,  spring-i-ly,  adv.,  spring-i-ness,  n., spring-less,  adj.,  spring-like,  adv. spring,  n.,  1)  a  leap;  2)  source  of  water;  source, origin;  3)  the  season  in  which  plants  spring  up a

794 ng-er,  n., spring-ing,  adj.  and  n.,  spring-ing-ly,  adv., spring-y,  adj.,  spring-i-ly,  adv.,  spring-i-ness,  n., spring-less,  adj.,  spring-like,  adv. spring,  n.,  1)  a  leap;  2)  source  of  water;  source, origin;  3)  the  season  in  which  plants  spring  up and  grow.  —  ME.,  f

794 ng,  adj.  and  n.,  spring-ing-ly,  adv., spring-y,  adj.,  spring-i-ly,  adv.,  spring-i-ness,  n., spring-less,  adj.,  spring-like,  adv. spring,  n.,  1)  a  leap;  2)  source  of  water;  source, origin;  3)  the  season  in  which  plants  spring  up and  grow.  —  ME.,  fr.  OE.  spring,  ‘s

794 ource  of  water;  source, origin;  3)  the  season  in  which  plants  spring  up and  grow.  —  ME.,  fr.  OE.  spring,  ‘springing; source  of  water’,  fr.  springan.  Cp.  MHG.  sprinc, ‘leap,  jump,  source  of  water,  fountain’,  OHG. sprung,  MHG.  sprunc,  ‘source  of  water’,  G. Sprung, 

794 G. sprung,  MHG.  sprunc,  ‘source  of  water’,  G. Sprung,  Du.  sprong,  ‘leap,  jump’,  and  see  spring, v. springa],  springald,  n.,  a  young  man  (archaic).  — Formed  fr.  the  verb  spring  with  -aid,  a  French suff.  derived  fr.  OHG.  -waldo,  -walto,  fr.  waltan, ‘to  govern’.  See

794 ringing  high  into  the  air  when  frightened.  See spring,  v.,  and  buck. springe,  n.,  a  snare.  —  ME.  sprenge,  springe,  rel. to  OE.  springan,  ‘to  spring’.  See  spring,  v. Derivative:  springe,  tr.  v,  to  catch  in  a  snare; intr.  v.,  to  set  springes. springlet,  n.,  a  sm

820 s-regere,  fr.  sub-  and  regere, ‘to  direct’;  see  regent,  adj.  Cp.  OF.  sordre (whence  F.  sourdre),  ‘to  rise,  spring,  gush  forth ; to  result’,  which  derives  directly  fr.  L.  surgere. F.  sourdre  is  now  used  only  in  the  inf.  and  only in  an  elevated  style.  It  has  be

901 om  English. Derivative:  veranda(h)-ed,  adj. verano,  n.,  the  dry  season  in  tropical  America.  — Sp.,  fr.  L.  ver,  ‘spring’.  See  vernal. Verbesina verascope,  n.,  a  small  stereoscopic  camera.  —  A hybrid  coined  fr.  L.  verus,  ���true’,  and  Gk. ruov,  fr.  mtoraiv,  ‘to  look

901 e:  veranda(h)-ed,  adj. verano,  n.,  the  dry  season  in  tropical  America.  — Sp.,  fr.  L.  ver,  ‘spring’.  See  vernal. Verbesina verascope,  n.,  a  small  stereoscopic  camera.  —  A hybrid  coined  fr.  L.  verus,  ���true’,  and  Gk. ruov,  fr.  mtoraiv,  ‘to  look  at,  examine’.  See
```


## [2026-09-05T05:26:12.168Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nprint('total leaves',len(leaves))\nfor i in range(896,len(leaves)):\n    nums=re.findall(r'(?m)^\\s*(\\d{4}|\\d{3})\\s*$', leaves[i])\n    print(i, nums, '|', leaves[i].strip().split('\\n')[0][:60])\nprint('=== tail of last leaf')\nprint(leaves[-1][-1500:])\nEOF",
 "description": "Check end of Klein scan"
}
```


### [2026-09-05T05:26:14.595Z] TOOL RESULT

```
total leaves 903
896 ['1692'] | ��,  nr^  (Hesychius), ‘web’,  L.  pannus,  piece  of  cloth
897 [] | —  A  hybrid  coined  fr.  vari¬ ola  and  suff.  -ite  (rep
898 ['1694', '1695'] | agential  suff.  -or.
899 ['1696'] | F.)  veine,  fr.  L. vena,  ‘blood  vessel,  watercourse,  v
900 [] | r’, vojina,  ‘war’,  Gk.  iep.ai  (for  ‘I  as¬
901 [] | , ventricle,  n.,  cavity  in  an  organ  of  the  body.  — 
902 [] | ��true’,  and  Gk. ruov,  fr.  mtoraiv,  ‘to  look  at,  exa
=== tail of last leaf
��true’,  and  Gk. ruov,  fr.  mtoraiv,  ‘to  look  at,  examine’.  See very  and  -scope.  The  correct  form  would  be alethoscope  (fr.  Gk.  dcXvjffrji;,  ‘true’  and  -rsy.6- mov ) .
veratral,  n.,  the  radical  C9H10O4  (chem.)  —  Form¬ ed  with  adj.  suff.  -al  fr.  L.  verdtrum,  'hellebore’. See  veratrine.
veratric,  adj.,  pertaining  to  a  white  crystalline acid. —  Formed  with  adj.  suff.  -ic  fr.  L.  verdtrum, ‘hellebore’  (see  veratrine) ;  so  called  because  it  is easily  obtained  by  the  decomposition  of  vera¬ trine.  \
veratridine,  also  veratridin,  n.,  an  amorphous  al¬ kaloid  obtained  from  sabadilla  seeds, C36H61OnN  (chem.)  —  Coined  fr.  L.  verdtrum, ‘hellebore’  (see  next  word),  and  the  chem. suffixes  -ide  and  -ine  (resp.  -in), veratrine,  n.,  also  veratrin,  veratrina,  veratria,  a poisonous  mixture  of  alkaloids  obtained  from sabadilla  seeds,  used  in  medicine  in  the  treat¬ ment  of  rheumatism,  neuralgia,  etc.  —  F.  vera¬ trine,  fr.  ModL.  veratrina,  fr.  L.  verdtrum,  ‘helle¬ bore’,  fr.  verare ,  ‘to  tell  the  truth’,  fr.  verus, ‘true’;  so  called  because
```


## [2026-09-05T05:26:22.335Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport re\nt=open('KLN_1971.txt',encoding='utf-8',errors='replace').read()\nfor pat in ['\\nvernal,','\\nAuster,','\\naurora,','\\naustral,','\\neast, n.','\\nEaster, n.','\\nEos,','\\nAustralia']:\n    i=t.find(pat)\n    print('#####',pat.strip(), i)\n    if i>0: print(t[i:i+700].replace('\\n',' '))\n    print()\nEOF",
 "description": "Klein 1971 entries"
}
```


### [2026-09-05T05:26:24.141Z] TOOL RESULT

```
##### vernal, 9438621
 vernal, adj., of, or pertaining to, spring. — L. ver-  ndlis , ‘pertaini'ng to spring’, fr. vernus, of s.m.,  fr. ver, ‘spring’, which is cogn. with ON. var,  ‘spring’, Gk. £ap, Ion. vjp, Dor. frjp (fr. orig.  ♦fgoap), OI. vasantah, ModPers. bahar , Arm.  gar-un, OSlav. vesna, ‘spring’, Lith. vasara,  ‘summer’. Cp. verano, vernant, vernation, Eran-  themum, Eranthis, Eryngium. L. ver, etc., pos-  sibly derive fr. I.-E. base *wes-, *awes~, ‘to  shine’, whence also L. aurora, ‘dawn’. See  aurora and east. For the ending of vernal see  adj. suff. -al.   vernant, adj., vernal, springlike. — L. vernans,  gen. -antis, pres. part, of vernare , ‘to appear like  spring, flourish, spring, bloom; to g

##### Auster, 762717
 Auster, n., the south wind. — L., of uncertain  origin. It is perh. cogn. with ON. austr, n.,  ‘east’; adv., ‘eastward’, OHG. ostar, ‘to the  east’ (whence ostar-rihi, G. Osterreich , ‘Aus-  tria’), Lett. *austrs, ‘eastern’ in dust rums, ‘east’,  OSlav. ustru , ‘pertaining to summer’, Avestic  ushas-tara, ‘eastern’, and with OHG. dstan, OE.  east, ‘east’; see aurora and cp. austral; cp. also  east. However, on the basis of this etymology,  it is difficult to explain why L. auster denotes the  ‘south wind* (and not the ‘east wind’L See  Walde-Hofmann, LEW., I, p.87, where also an  attempt is made to explain the meaning of L.  auster.   austere, adj., stem, severe; very simple. — OF.  austere

##### aurora, 759624
 aurora, n., the dawn of day; {cap.) the goddess  of dawn in Roman mythology, identified with  the Greek Eos. — L. aurora , ‘dawn’, for *au-  sosa (for the form cp. L. Flora , ‘the goddess of  flowers’, fr. fids, gen. floris, ‘flower’), fr. I.-E.  base *awes~, ‘to shine’, whence also Gk. scoq,  Homeric (for * a usds), ‘dawn’, OI. ujdh,  Lith. ausrd , ‘dawn’, L. auster , ‘south wind’, ON.  austr , OE. east, ‘east’. See east and cp. words  there referred to. Cp. also L. aurum, ‘gold’,  which also derives fr. I.-E. base *awes-, ‘to  shine’, and lit. denotes the shining metal (see  aureate and cp. words there referred to). Cp.  also the first element in Ostrogoth,  aurora australis, the Southern

##### austral, 763873
 austral, adj. southern; southerly. — L. australis,  ‘southern’, fr. auster, ‘south wind’. See Auster  and adj. suff. -al and cp. next word.   Australia, n. — Lit. ‘southern land’, fr. L. austra-  lis, ‘southern’, in Terra Australis , ‘the Southern  Land’. See prec. word.   Derivatives: Australi-an , adj. and n., Australi -  an-ize , tr. v., Australi-an-iz-ation , n.  austr©-, combining form meaning ‘south’. — Fr.  L. auster, ‘south wind, the south*. See Auster.  aut-, form of auto- before a vowel,  autarchy, n., absolute sovereignty. — Gk. aurap-  xta, fr. aoxapxetv, ‘to be an absolute ruler’,  which is compounded of aux6;, ‘self*, and  ap/Etv, ‘to rule*. See auto- and -archy,  autarchy, n.

##### east, n. 2779442
 east, n. — ME. east, est , fr. OE. east, ‘in the east’  (whence OE. eastan, ‘from the east’), rel. to Du.  oost, oosten , OHG. os tan, MHG. os ten, G. Ost,  Osten , ‘east’, OHG., OS. ostar, ‘to the east’, ON.  austr, ‘from the east’, fr. Teut. * oust a-, ‘east’,  which is rel. to I.-E. *ausos, ‘dawn’, whence OI.  u$dh, Gk. £a>q, Homeric Gk. yjw? (for *dusos),  Lith. au$ra, ‘dawn’, L. auster, ‘south’, aurum (for  *ausom), ‘gold,’ lit. ‘the reddish metal’, aurora  (for *ausosa), ‘dawn’. Cp next word and the first  element in Ostrogoth. Cp. also aureate, aurora,  Auster, austral, eo-, Eos.   Derivatives: east, adj. and adv., easter-ly , adj..     eastern (q.v.), east-ward, adv.   Easter, n. — 

##### Easter, n. 2780128
 Easter, n. — ME. ester, estern, fr. OE. easier,  eastre, ‘Easter’, fr. OE. Eastre (usually in the pi.  Eastron), a Teutonic goddess of spring (orig.  the goddess of dawn); rel. to OHG. ostarun,  MHG. osteren, G. O stern, ‘Easter’, and to E.  east (q.v.)   easterling, n., a native of an Eastern country. —  Formed fr. eastern with suff. -ling. Cp, MLG.  osterlink , Du. oosterlink . .  eastern, adj. — ME, ester ne, fr. OE. easterne, fr.  east. See east and -ern.   Derivatives: Eastern , n., eastern-er, n.  easting, n., easterly departure (naut.) — Formed  fr. east with subst. suff. -ing.  easy, adj. — ME. aisle , fr. OF. aisie (F. aist),  prop. pp. of aisier, ‘to ease’, fr. aise , ‘ease’. See 

##### Eos, 2966855
 Eos, n., the goddess of dawn in Greek mytho-  logy; identified with the Roman Aurora. — L.  Eds, also Eos, fr. Gk. ’Hto?, lit. ‘dawn’. See eo-.  eosin, eosine, n., a rose-colored dye (chem.) —  Formed with chem. suff. -in, -ine fr. Gk.  ‘dawn’. See eo-.   -eous, adjectival suff. meaning ‘of the nature of*.   — L. -eus as in ligneus , ‘of wood, wooden’ (fr.  lignum , ‘wood’, see ligneous ). Cp. -ous.   ep-, form of epi- before a vowel,  epact, n., the excess of the solar year over 12  lunar months (chronol.) — F. epacte , fr. Late  L. epacta, ‘an intercalary day’, fr. Gk. foraxxort  (scil. 7 )[iipai)> ‘intercalary days’, fem. pi. of  irzccxzbq, ‘added, intercalated’, verbal adj. of  fordcyei

##### Australia 764015
 Australia, n. — Lit. ‘southern land’, fr. L. austra-  lis, ‘southern’, in Terra Australis , ‘the Southern  Land’. See prec. word.   Derivatives: Australi-an , adj. and n., Australi -  an-ize , tr. v., Australi-an-iz-ation , n.  austr©-, combining form meaning ‘south’. — Fr.  L. auster, ‘south wind, the south*. See Auster.  aut-, form of auto- before a vowel,  autarchy, n., absolute sovereignty. — Gk. aurap-  xta, fr. aoxapxetv, ‘to be an absolute ruler’,  which is compounded of aux6;, ‘self*, and  ap/Etv, ‘to rule*. See auto- and -archy,  autarchy, n., autarky. — See next word; influenced  in form by prec. word.   autarky, n., self-sufficiency. — Gk. auxipxeia,  fr. atixapxeiv, ‘to be self
```


## [2026-09-05T05:26:33.174Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== SYN leaf 895 (p.871)\"; awk 'BEGIN{RS=\"\\f\"} NR==896' SYN.txt | head -40",
 "description": "Buck p.871"
}
```


## [2026-09-05T05:26:34.418Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== HRN leaf 77 = p.56\"; awk 'BEGIN{RS=\"\\f\"} NR==78' HRN.txt | head -30; echo; echo \"=== HRN leaf 302 = p.281\"; awk 'BEGIN{RS=\"\\f\"} NR==303' HRN.txt | head -30",
 "description": "Horn pages 56 and 281"
}
```


### [2026-09-05T05:26:34.697Z] TOOL RESULT

```
=== SYN leaf 895 (p.871)
G ltiur(e) Br. ker NHG teuer
A few of the words listed are deriva- tives of those for ‘price’, ‘cost, expense’, or the like; and a few come through the notion of ‘stingy’. But the most wide- spread development is from ‘dear, be- loved’ or ‘esteemed, worthy’ through ‘highly valued’ to ‘dear, expensive’. This may rest in part, but not wholly, on semantic borrowing from Lat. carus. There is no trace of such use of Grk. iros.
Omitted are the words which, while meaning literally ‘costly’, are not the common words for ‘dear’ as applied to an article for sale, but are used mostly in in a figurative sense, more nearly ‘cost- ly’, ‘precious’ or ‘extravagant’. Thus Lat. pretidsus fr. pretium ‘price’ and sometimes ‘dear, expensive’, but mostly ‘valuable, precious’; and the numerous
CC-O0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
prece (: Lith. pirktt ‘buy’, etc.). Fraen. kel, Z. sl. Ph. 6.87.
6. Skt. vasna- : Gr. vos, above, 1.
Skt. milya- prob. : mila- ‘root, foun- dation’.
Skt. argha-, Av. arafah- (NPers. arz ‘price’) : Skt. arh-, Av. araj- ‘be Worth’ Lith., Lett. alga ‘wages’ (11.78). Walde. P. 1.91. Barth. 192.
Av. paraska-, prob. (*prt-ska-) : Skt, a-prata- ‘without recompense’, and Lat, pretium, etc. (above, 2). Walde-P. 2.38, Barth. 896.
ete.,
Lith. brangus Lett. ddargs ChSl.  dragit SCr. skup Boh. drahy Pol. drogi
Russ. dorogoj Skt. mahdargha-, bahumi- lya-, etc.
Av. are
derivatives of It. costo, ete. ‘cost? (11.72), as It., Sp. costoso, OF r. costeus (> ME costouse > W. costus), Fr. cotteux, NE costly, NHG kostbar, etc. 1. Grk. zodvredjs, cpd. of zodb ‘much’ and last member fr. rédos ‘tax, toll, duty’ (11.69). Grk. riptos, fr. riuy ‘price’ (11.87). NG dxpiBés, fr. class. Grk. axpifis ‘exact, precise, accurate’ then (fr. ‘exact in money matters’) ‘parsimonious, stin- gy’ and hence ‘dear’ (as SCr. skup, be- low). 2. Lat. carus (> It., Sp. caro, Fr. cher) ‘dear’ = ‘beloved’ (16.28) and ‘ex- pensive’ (Plaut. in both senses). Rum. scump, fr. Slavic, cf. Bulg. ska- pu, etc. below, 6. 3. Ir. logmar, epd. of log ‘price’ and mar, mor ‘great’.
possEsslo
Macbain 123 undoubtedly and hence ‘cheap’ as
5 dere. i But 7 ‘enslaved’
gor rT.
7 é y’ fr. earlier sense mad,
rievous’ (Spur- orig.
both senses, MBr.
‘dear’ in er ‘d quer = Fr. cher
, Norm. Fr. (above): Henry 4, Goth. ig j et lu-galauys sive y also fil ON yar, etc.
Br. fk
63.
ifs = moduredns “expen- = rodbrimos ‘Very ‘dear,
ON dgrr, fiuri
es valued, worthy’ (later ‘dear,
beloved’) and ‘dear, expensive’, etym.
dub, ‘Falk-Torp 172. Weigand-H.
2.1040 f.
In parts of the U.S. dear is not the
48 opposites ( i
Down, ; negative com- th 4 = pose) to those for ‘dear’, latter, Th them are unrelated to the Sonable’, ai ss peat , ‘fair, rea- Ome : ‘ : Of the Words foy ‘cheap’ preaieed
ero
(henge mostly a terms, as Lat. vilis D, DUE this is by tS etivs.), NE 'S by no means general
CC-0. In Public Domain
N, PROPERTY, COMMERCE
Digitized by Arya Samaj Foundation Chennai and eGangotri
```


### [2026-09-05T05:26:36.570Z] TOOL RESULT

```
=== HRN leaf 77 = p.56
— se-
in ihrem Kern Bartholomae's Eigentum, doch weiss
ich nicht, ob er mit der Ansetzung der indog. Grund-
formen vollständig einverstanden sein würde.
243. behär Trühling .
Käs. vor neben bohor.
ap. &tira\vähara' (?); aw. vatihri *im Frühling (ZP.
61.); phlv. vahär; ai. vasantd- Trühling, vergl. vasar[hä
(Bartholomae, BB. 15, 157); arm. garun Trühling'.
oss. valjäg (71); sar. vug (wohl stammverwandt).
244. behäne Torwand'.
vi + k^ dhä' , vergl. ai. vidhdna- 'Ordnung , Fest-
setzung, Bestimmung'; phlv. vhänak, paz. vahäna
*Motiv' (Men.), Hörn, KZ. 32, 588 No. 25').
245. behVy hehre Xoos, Teil'.
aw. hii\badra' glücklich, gesegnet, beglückt'
(Aogem.); phlv. hahr ^ bahrakj (geschrieben *inN2),
syr. LW. bähraq.
An aw. ba/dra- mit Hübschmann, Avestastudien,
S. 696 zu denken , verbietet die Bedeutung dieses
Wortes, welches Geldner, Drei Yasht, S. 102 wohl
richtig als 'Mahlzeit' fasst.
Ich kann den Verdacht nicht unterdrücken, dass
auch np. ber/ Teil' (Sahn. I, 77 Anm. 11, Calc), ber/e
hierher gehören ; dann natürlich auch afy. LW. bar/a,
bra/a ^Anteil', vergl. Hörn, Indog. Forsch. H, 138
Anm.
246. bihiSt^ behist ^Paradies'.
(äw, mhista- 'bester; phlv. vahist; ai. väsistha-.
LW. kurd. behist.

=== HRN leaf 302 = p.281
— 281 -
lU. hen *Heer, Schaar ; arm. LW. hm TrsiQdtf'jfjmv^
ATjotrjgiov^ TfeigaTr,!^.
ap. hainä' 'Heerschaar ; aw. ha^nä-; ai. senä'. Im
Iranischen bekanntlich nur von Dämonen gebraucht.
115. hiyiV 'Unreinheit* (AW.-Komni., AV., Bund.), päz. hlhar,
hihir,
aw. hiyra- 'Unreinheit'.
Vorwiegend ritueller t. t. In Pärsenschriften be-
gegnet np. ÄTr, hl (Spiegel, ür. d. P., 201).
116. hol *link'.
aw. havya- 'link'; ai. suDi/d-; arm. aheuk *link' (un-
sicher, H. No. 5).
117. höH 'Morgenröte' (Aw.-Komm.j; vergl. hömstur öst-
lich*, hösbäm ^Tagesanbruch* (Men.).
aw. usah' 'Morgenröte'; ai. ums-.
118. hU' 'gut-'; sehr häufig in Zusammensetzungen (z. B
in hu[ramak, hii/t, hu\tu/s, hu\xtm etc.
ap. u-, UV-; aw. hu-; ai. su-; arm. h- (H. No. 15;3).
Im Neupersischen bisweilen in der Form /ti- erhalten;
vergl. auch np. huMr (oben No. 1098**'") und huweidä
V
'deutlich, klar* (Sahn. I, 282 Vers 15), das wohl zu
peidä (oben No. 349) gehört*).
i
118''^* jätakgav (geschr. -gab) d. i. jätagav, Jätaguv 'Ver-
mittler*, Jätakgavlh d. i. Jatagav,nvlh Türbitte*, päz.
jadangö, jadangöT-), arm. LW. jatagoo 'Verteidiger,
Fürsprecher, Anwalt, Beschützer, Gönner*.
ap. "^yätaguuhü' 'Anteilsprecher', Hübschniann
```


## [2026-09-05T05:26:55.953Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"12\\.45\\|EAST$\\|EAST \" SYN.txt | head -20",
 "description": "Find Buck EAST section"
}
```


### [2026-09-05T05:26:57.426Z] TOOL RESULT

```
22241:870 12.45 HAST 12.46 WEST Grk. — dvarody, éws éoxépa, dvopal, dbots NG évarody Shots Lat. _oriéns occidéns, occdsus It. est, levante ovest, ponente Fr. est ouest Sp. este oeste, poniente Rum. est, rdsdrit vest, apus Ir. airther iarthar Nir. oirthear tarthar W. dwyrain gorllewin Br. reler, savheol kuzheol, kornaoueg Goth. urruns saggqs ON austr vesir Dan. gst vest Sw. Oster vdster OE éast west ME est west NE east west Du. oosten westen OHG dstan westan MHG  dsten west(en) NHG  osten westen Lith. rytai vakarat Lett. austrums, rili rielums, vakari ChSl.  vitstokiz zapadit SCr.  istok zapad Boh.  vgchod zdpad Pol. wschéd zachéd Russ. vostok zapad Skt.  purvd-(dig-), pratici-(dig-), praci-(di¢-) paccima-(di¢-) Av. upaosanhva-, daosatara- (adj.)
22276:12.46. Words for ‘west’ are derived from those for the ‘setting, going down’ (of the sun), or ‘evening’ or ‘behind’ (as opposed to ‘in front’ = ‘east’, cf. 12.45).
22338:Lat. auster ‘south wind’, also ‘south’, prob. orig. ‘east wind’ : ON austr, etc., feast’ (12.45), with shift through ‘south- east’ explained by the diagonal position of the axis of Italy. Walde-H. 1.87. Ernout-M. 94 (with some doubt).
```


## [2026-09-05T05:27:00.766Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '22242,22276p' SYN.txt",
 "description": "Buck 12.45 discussion"
}
```


### [2026-09-05T05:27:00.810Z] TOOL RESULT

```
uSastara- (adjs.)
The majority of words for the main points of the compass are based either on the position of the sun at a given time of day (‘sunrise, dawn, morning’ = ‘east’; ‘sunset, evening’ = ‘west’; ‘mid- day’ = ‘south’) or on one’s orientation, which among the TE-speaking peoples was usually facing the sunrise (‘in front’ = ‘east’; ‘behind’ = ‘west’; Tight? = ‘south’; ‘left? = ‘north’), though there are also traces of orientations toward the north or south (the latter in the Avesta, where ‘in front’ = ‘south’ 3 ‘be- hind’ = ‘north’). Cf. Schrader Reallex. 1.500 f.
A few are from names of characteristic winds, and among those for ‘north’ some are connected with the name of a con- stellation in the north, with ‘winter’, or
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
a ————w
SELECTED INDO-EUROPEAN SYNONYMS
re 12.47 NORTH 12.48 SOUTH of Bopéas, Boppas véros, peonuBpla 3Y Boptas, Boppas véros, peonuBpla sk septentrid meridiés, auster : nord sud, mezzogiorno, mezzod ef nord sud, midi 'p0 norte sur, mediodia sto nord sud ltiascert descert , tuaisceart deisceart gogledd deheu, de mt hanternoz kreistetz i mW nordr sudr ‘be nord syd din nord, norr séder norp stip | north south wo north south for noorden zuiden nord, nordan sundan up nort, norden stiden, sunden aul norden stiden 10 Siauré, Ziemiai pieltis | ztemel't dienvidus séverit jugit At sjever jug (* sever, piilnoc jih ; péinoc poludnie ea sever jug 12. ultara-(di¢-), daksind-(dic-) ate udici(dig-) § apdaztara- (adj.) paurva-, rapi0witara- iit (adjs.) ; Ch with ‘midnight’ as opposite of ‘midday’ Uy = ‘south’. lar Notable is the spread of the English for words, first as nautical terms, to the ) Romance languages. a The attested Goth. words for ‘east’ ave and ‘west’ (Mt. 8.11; those for ‘north’ | and ‘south’ are not quotable) are not ‘rs general Gme. terms, but literal transla- on tions of the Grk. Cf. G. S. Lane, Phil. Quarterly 12.323 f. fr, But it may be noted that Luther used i the Gme. terms only for the winds, otherwise those for ‘morning’, ‘evening’, M etc., and that these or others had almost . replaced the old terms fora while. Paul, a Deutsches Wtb. 379. §
The words are listed in the sb. forms so far as possible. But some of the early
gpATIAL RELATIONS:
ple only as advs. Ga forms o OL gast, etc. (see NED or it ep Av. forms are adjs., and the 3) The adjs. with dig- ‘direction ; au “a point of the sky’ (: dig- ayes either expressed or under- ou
yota
or ‘east’ are connected or ‘dawn’ or ‘morning’, for’ ‘rise’, OF with words for Gn front’, all referring to the aon of the rising Sun.
oa +qus-, *Gusos-, *ysos-, etc., in ah for ‘dawn’ and ‘east’, beside verb forms a8 Skt. ucchatt, Av. usatt ‘lights up’ (esp. of the dawn), Lith. aust, Lett. ust ‘to dawn’. Walde-P. 1.26f. Er- nout-M. 93. Walde-H. 1.86.
Grk. Aeol. atws, Dor. aus, Hom. 7ws, Att, tos dawn’ and ‘east’; Lat. aurora (‘ausis-a) ‘dawn’ and (mostly poet.) fast’ (prob. also auster ‘south wind’, 1248); ON ausir, OF éast, OHG dstan, etc, general Gmc., with various suffixes; lith. ausra ‘dawn’, Lett. austrums ‘east’ ; ChSl. za ustra ‘in the morning’; Skt. yas, Av. usd ‘dawn’, whence Av. usas- eae (fr. *wpa-usah-) adjs.
9.45. Words f
ipefore’ OT
A Gtk. avarohy ‘a rising’, esp. pl. barohal miov ‘sunrise’, hence ‘east’ : a ‘rise’ (esp. of the sun).
e “a ed pres. pple. of oriri *. Hence ag |i g Sie literary terms, It., Sp. : ;
: Sea Sp. levante, Fr. levant), ion, Talse, lift?, refl. ‘rise’. REW
Ry, \ ine It., Rum. est), Sp. este fr. a Pe 2917a. Wartburg 3.247. bs ie tee lit. ‘(sun)rise’, fr. rdésdri, Si om es (of sun), epd. of raz- iktin 1209, ics Spring’ fr. Lat. salire.
* aD, ay ;
tther, NIy, oirthear, Br. reter,
CC-0. In Public Domain
Digitized by Arya Samaj Foundation Chennai and eGangotri
PLACE, FORM, SIZE 871
fr. Ir. air-, Br. ar- ‘before’ (: Skt. pari ‘against, toward’, Grk. wept ‘around’, etc.), but also ‘east’ in advs. ¢-air ‘in the east’, s-air ‘to the east’, an-air ‘from the east’. Walde-P. 2.33. Pedersen 2.187. Ernault, Glossaire 572.
W. dwyrain, orig. ‘sunrise’, perh. fr. a epd. of the root in Ir. rigim ‘stretch out’, Lat. regere ‘direct, rule’, ete. Peder- sen 1.237, 2.56, 596 note 3.
Br. savheol, cpd. of sav ‘upright, raised’ and heol ‘sun’.
5. Goth. urruns (lit. translation of Grk. évarodn) : urrinnan ‘run out, go up, rise (of sun)’, ON renna, OE rinnan ‘run’, etc. Feist 528.
6. Lith. rytat, Lett. riti, pl. of Lith. rytas, Lett. rits ‘morning’ (14.34).
7. ChSl. viistoku, SCr. istok, Russ. vostok, orig. ‘sunrise’, lit. ‘a running up, out’ : ChSI. tegti, teka ‘run’, etc. (10.46).
Boh. vgychod, Pol. wschéd, orig. ‘sun- rise’, lit. ‘a going out, up’ : Boh. choditi, Pol. chodzié ‘go’ (10.47).
8. Skt. pirva-(dig-) fr. adj. purva- ‘in front, former, eastern’ = Av. paorva- in front, former’, but ‘southern’ (see 12.48). OPers. paruva- ‘eastern’ (Barth. 871) is to be deleted. The correct read- ing is paradraya ‘beyond the sea’. Cf. Cameron, J. Near East. Stud. 2.307 fs
Skt. pract-(dig-), fr. praiic- ‘directed forward, in front, facing, eastern’.
12.46. Words for ‘west’ are derived from those for the ‘setting, going down’ (of the sun), or ‘evening’ or ‘behind’ (as opposed to ‘in front’ = ‘east’, cf. 12.45).
```


## [2026-09-05T05:27:10.477Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"vāhara\\|vahara\\|Θūravāhara\\|Thuravahara\\|uravahara\" KNT.txt | head -20",
 "description": "Grep Kent for vahara"
}
```


### [2026-09-05T05:27:10.532Z] TOOL RESULT

```
1165:Other examples of OP 0 from pIE Ё are to be seen in akala-, 6urd-, da"d-, Guxra-, Gravahara-, and perhaps in @digurci-, Oalagu-, Üarimi-; see Lex. s.vv.
1777:II. Extending a non-verbal stem: üv-nara- to nar-, *wwăi-pašiya- to pati-, pada- páda- to pad-, Márgava- to Margu-, duS-iydra- to yàr-, vazra- in vazra-ka- to *vazy-, eühara- in Gira-vahara- to *yasr-, u-zma- to гат-, hama- to ham-; perhaps Gau-baruva- to baru-, müha- о mah-, viða- to vid-.
1816:I. The suffix -ra-, sometimes primary and some- times secondary, appears in agra- whence agriya-, A*u-ra-, tig-ra-, personal name @uz-ra-, 6ü-ra- in Güra-vühara-; adj. dü-ra-, whence adv. nü-ram; the uncertain ^u-raBa-ra-. Problematic, and perhaps not Iranian, ѓасата- dacara-. On vazra- in vazra- ka-, vàhara- in 8üra-vahara-, ратіата-, see $154.I.
1925:Lex. s.v.); @ira-vahara- '(Month) having vigor-
1961:With vriddhi in second part: Aci-yád-iya-, Өйта- vahara-. |
2672:K. To express time when, as їп the adverbs paranam and paruvam ‘formerly’, and with the postposition pakiy: DB 1.20 xsapavd raucapativà ava akunavayata ‘either by night or by day, that was done’; DB 2.61f Güravaharahya mahya jiyam- nam patiy avat sam hamaranam kartam ‘on the last of the month Thuravahara, then by them the battle was fought’.
3586:Техт or DB, Сошмх П: 1 :98ty : Dárayavaus : xSayafiya : paeüva : Naditabaira : ha 2 dà : kamnaibis : asabaraibis : amufa : Bübirum : ašiya 3 va: pasàva : adam : Babirum : ašiyavam : vasnd : Auramazdiha : uta : Ba 4 birum : agarbiyam : uta : avam : Naditabairam : agarbüyam : pasáva : ava 5 m : Naditabairam : adam : Babirauv : avüjanam —— :0ütüy : Dārayavauš : x 6 Sdyabiya : yātā : adam : Bübirauv : àham : ima : dahydva : tyà : hacàma : ha 7 migiyà : abava : Рагва : Üvja : Mada : Aðurā : Mudráya : Parfava : Margus : Өз 8 tagui:Saka : абу : Dārayavauš : x8dyabiya : I martiya : Martiya : nā Q ma : Cicixrais : puca : Kuganakà : пата : vardanam : Pársaty : avada : adaraya : 10 hauv : udapatatà : Uvjaiy : Кагаһуй : avaðā : afaha : adam : Imanis : amiy : 0 11 vjeiy :xSdyafiya —— : @atiy : Darayavaus : zsayattya : adakaiy : adam : asna 12 iy : àham : abiy : Üvjam : pasáva : hac&ma : alarsa : Üvjiy& : avam : Marti 13 yam :agarbaya : hyašām : mafista : dha : шат : avàjana — : 00у: D 14 árayavaus : xSiyafiya : І martiya : Fravartiá : пата : Мада : hauv : udapatat 15 à : Madaiy : Катаһуй : ауаба : абала : adam : XSa6rita : amìy : Uvaxdtrah 16 уй : taumàyá : pasáva : kāra : Mada : hya : v'àpaliy : haw : hacáma : hamiciya : a 17 bava : abiy : avam : Fravartim : aSiyava : hauv : тёйуайтуа : abava : Madaiy 18 9àtry : Dárayavaus : xšāyaðiya : kara : Parsa : ша : Мада : bya : ира : mim : 4 19 ha : hauv : kamnam : aha : раѕауа : adam : kdram : fraiSayam : Vidarna : пата : Pársa : man 7 20 à : badaka : avam&àm : mafistam : akunavam : avataSaám : afaham : parait : avam : К 2] dram : tyam : Madam : jatà : hya : mand : пау : gaubataiy : pasiva : hauv : Vidarna : ha 22 dà : kara : айуауа : yafà : Madam : parárasa : Māruš : пата : vardanam : Ma 23 дау : ауада : hamaranam : akunaus : hada : Мада : һуа : Màdaisuvà 24 :ma(iSta : dha : hauv : adakaiy : пау : avadà : аһа : Auramazdimary : u 25 раѕійт : арага : vasnà : Auramazdáha : kāra : hya : тара : avam : kàram : t 26 yam : hamiciyam : aja : vasiy : Animakahya : mähyä : XXVII : raueabis : fakat 27 à : аһа : avatüsám : hamaranam : kartam : pasáva : hauv : Ката : һуа : manā : Карада : пат 28 à : dahydus : Mádaiy : avadà : mam : amánaiya : y8tà : adam : arasam : Mada ' 20m : 08у : Dàrayavaus : xšāyaðiya : адаг х : nàma : Arminiya : man 30 à : badaka : avam : adam : frāišayam : Árminam : avafasazy : aaham : paraidiy : ka 31 ra : һуа : hamigiya : mană : naiy : gaubataiy : avam : jadiy : pasiva : Dadarsi 32 š : aSiyava : yafà : Arminam : parárasa : pasáva : hamigiya : hagmatà : paral 33 tà : patiš : Dādaršim : hamaranam : cartanaiy : Züzahya : пата : àvahanam : А 34 rmíniyaiy : avadà : hamaranam : akunava : Auramazdimaiy : upastàm : a 35 bara : vasnà : Auramazdàha : kāra : һуа : manā : avam : küram : {уаш : hamigiyam : 36 aja : vasiy : Oüravaharahya : máhya : VIII : raucabis : 09akatà : dha : ava 87 à$üm : hamaranam :kartam : бабу : Dárayavaus : z3àyaffya : patiy : duv 38 itiyam : hamigiyà : hagmatà : paraitd : patiš : Dàdar&im : hamaranam : carta 3€ nay : Tigra : пата : didà : Arm‘niyavy : avadà : hamaranam : akunava : А 40 uramazdàmaiy : upastàm : арага : vašnā : Ашатагдаћа : kāra : һуа : тапа :a 41 vam : káram : tyam : hamigiyam : aja : vasiy : G9üravüharahya : mihya : ХҮШ 42 :raueabiá : бакаќа : аһа : ауабадат : hamaranam : kartam —— : 00у : Daraya 43 vaus : xšāyaðiya : patiy : citiyam : hamictyd : hagmatà : paraita : pat 44 iš : Dádar&im : hamaranam : cartanaiy : Uyama : nama : didi : Arm'myaty :a 45 vadā : hamaranam : akunava : Auramazdimaiy : upastam : арага : vaSnà : Aurama 46 zdàha : kāra : һуа : manā : avam : küram : tyam : ham?giyam : aja : vasiy : Oàigarea 7 d :mábyà : IX : raucabis : Nakata : dha : ауада ат : hamaranam : kartam : pasava 48 : Dadarsis : citā : mim : amánaya : Arm/niyaiy : yiti : adam : arasam : Ма
3661:$26. 2.29-37. Saith Darius the King: An Armenian by name Dadarshi, my subject—him I sent forth to Armenia. Thus I said to him: “Go forth, that rebellious army which does not call itself mine, that do thou smite!’ Thereupon Dadarshi marched off. When he arrived in Ar- menia, thereafter the rebels assembled (and) came out against Dadarshi to join battle. A place by name Zuzahya, in Armenia—there they joined battle. Ahuramazda bore me aid; by the favor of Ahuramazda my army smote that rebellious army exceedingly; of the month Thuravahara ҮШ days were past, then the battle was fought by them.
3665:exceedingly; of the month Thuravahara ХҮШ
3670:exceedingly; of the month Anamaka XV days” were past, then the battle was fought by them. §30. 2.57-63. Saith Darius the King: Again a second time the rebels assembled (and) came out against Vaumisa to join battle. A district by name Autiyara, in Armenia—there they joined battle. Ahuramazda bore me aid; by the favor of Ahuramazda my army smote that rebellious army exceedingly; on the last day of the month Thura- vahara—then the battle was fought by them. After that, Vaumisa waited for me in Armenia
3721:39 zdàátahya : aja : vasiy : Güravaharahya : mahya : XII : raucabis : бака
3787:641. 3.2840. Saith Darius the King: There- upon І sent forth the Persian and Median army which was by me. À Persian by name Artavardiya, my subject—him I made chief of them. 'The rest of the Persian army went forth behind me to Media. Thereupon Artavardiya with his army went forth to Persia. When he arrived in Persia, a town by name Rakha, in Persia—there this Vahyazdata who called himself Smerdis came with his army against Artavardiya, to још battle. Thereupon they joined battle. Ahuramazda bore me aid; by the favor of Ahuramazda my army smote that army of Vahyazdata exceedingly; of the month Thuravahara XII days were past— then the battle was fought by them.
4871:1 Adukanaiša Hadukanna$ Nisabbu Mch.- Apr. 2 Otiravahara Turmár Andru Apr.- May 30üigarci$ — Sdkurrisif —— Simannu May- June 4 Garmapada Karmabada$ Dwūzu June- July ОТОТ Turnabagi$ Abu July- Aug. ена агра (та) & — Ulülu Aug.- Spt. 7 Bügayüdi$ — Bagijüti Taxritu = Spt.- Oct. 8 *Vurkazana Margaíana$ Arahsamna Oct.- Nov. 9 Aciyadiya  Haifuüt(;a)& Küslimu — Nov.- Dec. 10 Anémaka HandmakaS Tebétu Dec.- Jan. It Sami(ia)maS Sabitu Jan.- Feb. 12 Viyarna = =Mitia)kannaS Addàru Кер. Мер.
5486:Oüravühara- adj. “Thuravahara’, second month, April-May: Elam. turmar, Akk. айайги.
```


## [2026-09-05T05:27:19.516Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nimport itertools\ndef leaf(ln):\n    return t[:sum(len(l)+1 for l in lines[:ln-1])].count('\\f')\nfor ln in [1777,1816,1925,5486]:\n    L=leaf(ln); print(ln,'leaf',L,'-> printed ~',L-13,'/',L-15)\nEOF\necho \"=== context 1920-1930\"; sed -n '1920,1930p' KNT.txt",
 "description": "Kent page mapping"
}
```


### [2026-09-05T05:27:21.272Z] TOOL RESULT

```
1777 leaf 65 -> printed ~ 52 / 50
1816 leaf 66 -> printed ~ 53 / 51
1925 leaf 69 -> printed ~ 56 / 54
5486 leaf 211 -> printed ~ 198 / 196
=== context 1920-1930
‘Having an upright mind’; Tarma-spdda- ‘Hav-
ing à brave army’; Vahyaz-data- Following the
better law’; Vistdspa- from *višta-aspa- (see
Lex. s.v.) ‘Having ready horses’; @ata-qu-
‘(Land) having hundreds of cattle’ (but see
Lex. s.v.); @ira-vahara- '(Month) having vigor-
ous spring-time’, —
b. The prior element is appositive to the sec- ond:
Varka-zana- ‘(Month) belonging to the wolf-men'. uvdi-pasiya- ‘having self as lord’, with adjectival sufhx.
с. The second element is predicate to the prior: Ariydramna- from *ariya-dramna- ‘Having the
Aryans pacified’; so to be interpreted because
```


## [2026-09-05T05:27:31.387Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport re\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i in range(205,222):\n    nums=re.findall(r'(?m)^\\s*(\\d{2,3})\\s*$', leaves[i])\n    first=leaves[i].strip().split('\\n')[0][:55]\n    print(i,nums,'|',first)\nEOF",
 "description": "Kent leaf page numbers"
}
```


### [2026-09-05T05:27:33.048Z] TOOL RESULT

```
205 [] | sg. subj. (8212, $227.1) DNa 42. xindsdtiy subj. ($02, 
206 ['183'] | n, fall down’: [avagmat]a nsf. past pte. ($244) DSe 46f
207 [] | 3f, 57; XPa 20; XPc 14; XPf 48, alva}m-c* ($521) DB 5.9
208 ['185', '186'] | Skt. jū- ‘press for- ward, impel quickly, excite, promo
209 [] | it (§76.V, 5148.1). Cf. Gray, AJP 58.67; Hz. Klio 8.51,
210 ['187'] | 1) XPh 23.
211 ['188'] | word of uncertain meaning, Sb 3.
212 ['189'] | fnu, Lt. јеси ‘made’, NEng. do, deed, pIE *dhe-. See al
213 [] | 5-6).
214 ['191'] | Hz. Ap! 136-8) nsn. as sb. ‘handiwork’, DSe 42.
215 [] | rada&a, duvaista-. dürau lsn. as adv. ‘afar, far away, 
216 ['193'] | e 15; DZe 10. drayahya lsn. ($136, §251A; wrongly taken
217 [] | n üv-nara- (§142).
218 [] | with Justi, IFA 17.107, ‘Pasargadae’, from paisiyd- ‘wr
219 [] | ‘I pierce (as with a spit)’, Gt. faran ‘to travel’. рам
220 [] | tem (530, $148.I, 6154.1), ef. Av. posana- ‘battle’, Sk
221 ['197', '198'] | r-, Gk. rarnp, Lt. pater, Gt. fadar, pIE *poler- (863.1
```


## [2026-09-05T05:27:37.559Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport re\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i in range(225,245):\n    nums=re.findall(r'(?m)^\\s*(\\d{2,3})\\s*$', leaves[i])\n    if nums and ('207' in nums or '206' in nums or '208' in nums):\n        print('LEAF',i,nums)\n        print(leaves[i][:2500])\nEOF",
 "description": "Kent p.207"
}
```


### [2026-09-05T05:27:38.985Z] TOOL RESULT

```
Exit code 1
LEAF 230 ['206']
am. rak-qa-an, АКК. ra-ga-’, Gk. ‘Payys, now Rai near Teheran. kagä nsf. DB 2.71f. Ваду absf. DB 8.2.
гада- sb. ‘wagon’ (570.11, $148.11), see urata-.
Irad- vb. ‘leave’: Skt. rah-, pres. rahati 'sep- arates, leaves’, to pIE *regh-, Av. razah- 5isola- tion’, or to pIE *redh-, NPers. (through Ars. РЫ.) rähäð ‘he gets free from’; Fr. Müller, WZKM 11.208-4; Foy, KZ 37.564-5; Bthl. AiW 1505; MB Gr. $192.
ava- + rad- ‘leave, abandon’: avarada 2d sg. inj. (5213, $224, $227.11, $237) РМа 60.
?rad- vb. ‘direct’ Ау. raz-, Skt. rdj- ‘reign’, Lt. rego ‘I direct, rule’, pIE *reg-; in uradana-, тазіа-.
rādiy postpos. ($133) ‘on account of’, with gen.: NPers. тё, enel. postpos. as in &-rà ‘why’, also particle of various uses, often affixed to direct object for elarity; also OCS radi, postpos. with gen., “оп account of’; 10е, sgoof räd- (5188111), io root in Ski. radh- ‘effect; complete! (not to
206
"rad-, pIE *rej-, with Hz. ApI 280). DB 4.54; DNb 9, 10f; also in avahyarádiy, q.v.
ram- vb. ‘be at peace’, with prefix d, in Arüjyüramna-, q.v.
rasa- present stem of vb., see ar-.
rüsla- adj. ‘straight, right, true’, with nt. as Sb.; ріс. of ?^rad-: Av. réSta-, Turfan РЫ. тай ‘true’, Lt. réctus ‘straight’, pIE *rékto- (593, §93.- n1-2, $106, $122, 5126, $24211). Cf. arštā-. таӣз- iam asf. DNa 59. rdstam usn. DNb 11; asn. DNb 7.
‚ .. rlaryary, see vart-.
Labandna- (or Labnàna-) sb. ‘Lebanon’ (§6, §107), 2 mountain in Syria famous for its cedars. Labanéna nsm. DSf 31.
-vä encl. conj. ‘or’ (8133, $291.1
Traceback (most recent call last):
  File "<stdin>", line 5, in <module>
IndexError: list index out of range
```


## [2026-09-05T05:27:43.612Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==232' KNT.txt | grep -n -i \"vahara\\|vāhara\\|vahar\" ; echo \"---\"; awk 'BEGIN{RS=\"\\f\"} NR==232' KNT.txt | head -30",
 "description": "Kent leaf 231 content"
}
```


### [2026-09-05T05:27:45.104Z] TOOL RESULT

```
---
1); -vā .. -vä ‘either... or...’: Av. và, Skt. và, pIE *ue, ef. Lt. -ve.  z$apa-ü rawca-paíi-a DB 1.20. hya-»à DB 4.68. imai-vä DB 4.71, 78, 77. yadi- vä DNb 25, 29.
vaina- present stem of vb. ‘see (mid.) seem’: Av. vaéna-, NPers. bindd, Skt. véda ‘knows’, vinddte ‘finds’, Lt. videt ‘sees’, videtur ‘seems’; pAr. *uaid- na-, plr. *yaina- ($69, 588.1, $130, $210.III; Reichelt, Aw. Ер. $157). See also Vidafarnah-. vainümiy lst sg. (4226.1) DNb 36, 36f, 39, 40. avaina imf. DB 2.76, 90; DNa 32. vainataiy mid. as pass. (8235.1) DNb 2; XPa 16. vaináhy 2d sg. subj. ($37, $222.11, $227.1) DB 4.70, 73, 77; DNb 29. vaindtiy subj. ($222.11) DS} 5°. vainātaiy subj. mid. as pass. ($222.П) DNb 35.
vau- adj. ‘good’ ($11, §153.1); nt. as sb. ‘the good, (religious) goodness’: Av. nsm. vaphus, nsn. vohu, Skt. nsm. vásuş, nsn. vdsu, pIE *yesu-; in Dérayavau-, Vaumisa-, Vahauka-, Vahyazdata-.
Va'umisa- sb. ‘Vaumisa’, a Persian officer of Darius: Elam. ma-u-mi-i8-8a, АКК. ti-mi-is-st, Gk. (Plutarch) Rutens; cpd. of vatu- and mifra- ‘friend’ (849c, $78, $148.ILD): ‘Friend of the Good’ §160.- Ib; cf. MB Gr. $51). Vaumisa nsm. DB 2.49, 51, 62. Vaumisam asm. DB 2.53, 58.
vaz$- vb. ‘grow’, see (Луах${та-.
Waj- vb. ‘be strong’: Skt. vaj-, бјаз- ‘strength’, Av. aof
```


## [2026-09-05T05:27:54.396Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==232' KNT.txt | grep -o -i \".\\{80\\}h[aä]ra.\\{120\\}\" | head; echo \"=== full leaf tail\"; awk 'BEGIN{RS=\"\\f\"} NR==232' KNT.txt | tail -20",
 "description": "Search vahara on Kent p.207"
}
```


### [2026-09-05T05:27:56.253Z] TOOL RESULT

```
=== full leaf tail
1); -vā .. -vä ‘either... or...’: Av. và, Skt. và, pIE *ue, ef. Lt. -ve.  z$apa-ü rawca-paíi-a DB 1.20. hya-»à DB 4.68. imai-vä DB 4.71, 78, 77. yadi- vä DNb 25, 29.
vaina- present stem of vb. ‘see (mid.) seem’: Av. vaéna-, NPers. bindd, Skt. véda ‘knows’, vinddte ‘finds’, Lt. videt ‘sees’, videtur ‘seems’; pAr. *uaid- na-, plr. *yaina- ($69, 588.1, $130, $210.III; Reichelt, Aw. Ер. $157). See also Vidafarnah-. vainümiy lst sg. (4226.1) DNb 36, 36f, 39, 40. avaina imf. DB 2.76, 90; DNa 32. vainataiy mid. as pass. (8235.1) DNb 2; XPa 16. vaináhy 2d sg. subj. ($37, $222.11, $227.1) DB 4.70, 73, 77; DNb 29. vaindtiy subj. ($222.11) DS} 5°. vainātaiy subj. mid. as pass. ($222.П) DNb 35.
vau- adj. ‘good’ ($11, §153.1); nt. as sb. ‘the good, (religious) goodness’: Av. nsm. vaphus, nsn. vohu, Skt. nsm. vásuş, nsn. vdsu, pIE *yesu-; in Dérayavau-, Vaumisa-, Vahauka-, Vahyazdata-.
Va'umisa- sb. ‘Vaumisa’, a Persian officer of Darius: Elam. ma-u-mi-i8-8a, АКК. ti-mi-is-st, Gk. (Plutarch) Rutens; cpd. of vatu- and mifra- ‘friend’ (849c, $78, $148.ILD): ‘Friend of the Good’ §160.- Ib; cf. MB Gr. $51). Vaumisa nsm. DB 2.49, 51, 62. Vaumisam asm. DB 2.53, 58.
vaz$- vb. ‘grow’, see (Луах${та-.
Waj- vb. ‘be strong’: Skt. vaj-, бјаз- ‘strength’, Av. aof
```


## [2026-09-05T05:28:09.185Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"βrγ'r\\|brg'r\\|βarγār\\|brγ\\|vrkr\\|βryʼr\" SOD.txt | head -20; echo \"=== grep temple\"; grep -n -i \"temple\" SOD.txt | head -30",
 "description": "Grep Gharib Sogdian for temple"
}
```


### [2026-09-05T05:28:09.255Z] TOOL RESULT

```
=== grep temple
4796:which  was  discovered  in  a  ruined  temple  at  the  head 
16618:temple,  sanctuary  * 
24624:temple 
24671:temple 
25751:temple 
33120:temple 
59824:idol  temple 
59995:idol  temple 
62632:temple  (place  of  worship),  altar 
90599:idol  temple    7741 
94378:temple     1369,  2569,  2575,  2741,
```


## [2026-09-05T05:28:12.168Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for L in 16618 24624 24671 25751 33120 59824 59995 62632 94378; do echo \"### line $L\"; sed -n \"$((L-8)),$((L+3))p\" SOD.txt | tr '\\n' ' '; echo; done",
 "description": "Context of Sogdian temple entries"
}
```


### [2026-09-05T05:28:14.175Z] TOOL RESULT

```
### line 16618
1367  >pw  »zr  =>  »zr   1368  'pw  "zrmy'h  =>  'zrmy'h   1369  >pw'5'k   B,S  o&^^ix^  (o)pwa5e   (pw'dy,  'pw'5'y)  ©<*hapa  (=Skt.   sap-  "to  worship")+wa£   ©ace.  -w   ^pw'S'k  temple,  sanctuary  *  SCE  n  p37,  176,  276,  335,  348;  STSC  137;  Frag.   Lcn.  96.1,  lOOal,  3,  5,  c9;  Mack.  BSTBL  p!54  
### line 24624
 flrysty;  VJ  98;  TSP  2.395;  fix'ysu  STii  8.6,   10.45   2569  pySVk   B  (  j5U-)ju^«1^-.>t  Pay-5ane   ©<*baga-ddna  ©ace.  -u>   temple   cxwS/ir&ny,  Hen.  BSOAS  1956,  367  n3,   
### line 24671
divine,  (of)  god  GMS  1103   2575  pyn-   M  x^^€^^^  payn,  Payan   ©<*bagina  ©nom.  -yy;  ace.  -w%   abl.  -J;  loc.  -y   temple   GMS  165,  509,  1183;  BBB;  Hen.  Tales.  473,  42;  C2,  25R23,  25V  n  p62;  Sund.  AI  28,  1988,  180  
### line 25751
2740  prYnk   S  ^^J^^J  faryane  ©-w   (<?/)Farghane  MDii  p84   2741  pry'r   B,  S  (j^J-'J-^^jW"^-^  farxar   (Pry'r)  ©Skt.  vihara  ©ob.  -y   =>fryJr  temple   prVry,  SCE  169,  173,  ftrr*rt  176,  -y,  172  etc.;  VJ  1117;  TSP  7.36,  8.195;  SCE;  GMS  362;  Frag.  
### line 33120
frez   ©<*fra-razaya  =»fryz-,  fr'st-  OcOstraighten,  GcOcrect   GMS  319;  BSTBL,  Dhy.  84;  STi  31.14   3886  fryV   B  j^>  <j**>  «&^>T  farxar   ©ob.  -y   =*PrY}r   temple  0?3   3887  fry>z-    M  u:>»T  
### line 59824
(jL-^L^OU-jK;  ttj&j    ^j    7741  ptqrystJn   C  patkarestan   ©ob.  -y  idol  temple   BSTi  234,  242,  279   
### line 59995
((JL^^X^)(jl^-*jlxJ  lajS^j    J*}    7741  ptqryst'n   C  patkarestan   ©ob.  -y  idol  temple  BSTi  234,  242,  279   7742  ptkryty  Vsy   M  <Uc  
### line 62632
8137  pw'c   B  jP  anxiety   Frag.  Len.  32.6,  -w,  32.2   8138  pwWk   B  jL^io&j^,  pwaSe   (pw}dy)  ^pw^k   temple  (place  of  worship),  altar   TSP  2.104  n  pl82;  BSTii  860.43:  C2,  23V11,  13;   
### line 94378
tearful     8450  (ta)tear  off    7735  (fo)tell    4363,  7046,  7070,  7076,   7927,  7930,  8079,  9042  telling     9777, 9789  telling  song     11361  tempest     2270  temple     1369,  2569,  2575,  2741,   3886,  8138  (ro)tempt     11310
```


## [2026-09-05T05:28:28.435Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('SOD_pages.txt',encoding='utf-8',errors='replace').read()\nimport re\ni=t.find('2741')\n# find all occurrences of entry 2741\nfor m in re.finditer(r'2741\\s+pry.r|2741\\s+βry', t):\n    leaf=t[:m.start()].count('\\f')\n    print('leaf',leaf,'printed ~',leaf-66)\n# also 3886\nfor m in re.finditer(r'3886\\s+', t):\n    leaf=t[:m.start()].count('\\f')\n    print('3886 leaf',leaf,'printed ~',leaf-66)\nEOF",
 "description": "Locate Gharib entry pages"
}
```


### [2026-09-05T05:28:29.954Z] TOOL RESULT

```
leaf 173 printed ~ 107
3886 leaf 219 printed ~ 153
```


## [2026-09-05T05:28:39.816Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== BQT v3 farxar\"; grep -n \"فرخار\" incoming/BQT/BQT_v3_pages.txt | head -10; echo \"=== pdf page tags near\"; python3 - <<'EOF'\nimport re\np='incoming/BQT/BQT_v3_pages.txt'\nt=open(p,encoding='utf-8',errors='replace').read()\nfor m in re.finditer('فرخار', t):\n    seg=t[:m.start()]\n    tags=re.findall(r'\\[pdf page (\\d+)\\]', seg)\n    print('pdfpage',tags[-1] if tags else '?', '| printed ~', int(tags[-1])+1205 if tags else '?')\nEOF",
 "description": "Find farxar in Borhan vol 3"
}
```


### [2026-09-05T05:28:41.448Z] TOOL RESULT

```
=== BQT v3 farxar
16569:‏است که نلم شهری باشه ‎they‏ بفرخار و مشك
17767:‎SUT,‏ هر چیژ باشد - وچندشهر فرخارنام
17807:‏۴ « فرخار بز رکه > در تبت است . مولف حدودالمالم در « سخن اندر ناحیت تبت و
17809:‏شهر های وی » آرد : «کرسانك از تبت است و اندر وی بتخانه‌های بزرگه است » آنرا فرخار
17811:ونیز فرخار نام شهریست در طالقان ( ماوراءالتهر ( « حدود . میئورسکی ص ۳۳۰ , ۳۵۰ > -
=== pdf page tags near
pdfpage 230 | printed ~ 1435
pdfpage 245 | printed ~ 1450
pdfpage 245 | printed ~ 1450
pdfpage 245 | printed ~ 1450
pdfpage 245 | printed ~ 1450
```


## [2026-09-05T05:28:41.908Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== PHD wahar\"; grep -n \"^wahār\\|wahār\" PHD.txt | head -10; echo \"=== NYB vahar\"; grep -n \"vahār\\|wahār\" NYB_vol2_glossary.txt | head -10; echo \"=== HUB behar/bahar\"; grep -n \"behär\\|bahār\\|behār\" HUB.txt | head -10",
 "description": "MacKenzie, Nyberg, Hübschmann for wahar"
}
```


### [2026-09-05T05:28:42.016Z] TOOL RESULT

```
=== PHD wahar
392:hamēstār, —ih [hmyst!l, -yh] = hamēmāl, ~ih. hamésag [hmyfk! | M hmyšg, N —a] always. ^h : eternity. ~-86z [-swe] ever-burning. hamē-wahār [hmy whl | N haméfa-bahar] marigold. ham-éwénag [Am'dwynk!'] of the same kind, homogeneous. ham-góhr (hmgwhl! | M hmgwhr] of the same substance or nature, consubstantial. ham-ginag [hmgwnk! | M hmgwng] likewise, so. P hāmharz [A())mAlc | P I? mhyrz] adjutant, attendant. hāmīn [A*myn! |= M] summer. ~ig [-yk'] (of) summer. hāmist [KHDE, v. hammis ; )”mst!] all. ham-kār [hmk’l | N ~] collaborator. 7h : collaboration. hāmkišwar [mkyfwl | M. -wr] universe. hammis [KH DE < A k-hdh), ат... ~: together with. hammist [hmyst'] stagnant, peaceful. ~(ag)an [-(kYn'] limbo, the neutral station between heaven and : hell. vl hammóxtan, hammoz- [ALPWN-tn! < A У "Ip: hmwhtn', hmwc-, Ki hmsoz- | M hmwxtn, N āmēxtan, ámóz-] teach; learn. -išn: teaching. hammdxtar [Amwht?!] learner. ~th: learning. hammóz- , ~i8n, v. hammóxtan. —@йг [kmwcek?l | N āmēzgār] teacher. ham-nibardih [hmnpityh] (single) combat. hamēūģ [/tmwg] equal, like. hámón [k mwn' | N kāmūn] level, flat. hámoyén [/?mwdyn!] all. ham-pursag [hmpwrsk!] consulting, taking counsel. ^h : consultation. ham- |-ránih [Am nyh] battle, combat. ~-samiain [-s"m?n!] contiguous. ~-sardag [-sltk'] of the same kind, like. ~-sayag [-sdk! | N hamsáya) neighbour. ~-tag [-t*k! | N hamid] equal, peer. «tan [-tn'] of the same stature, build. ~=-tihmag [-twhmk'] relative, relation. hamwar [hmwl | N hamwār] level, abreast. hámwiür(ag) [%()mw?/, -k! | N hamwdara] always. ham-zamān [hm ODNA | N —] instantly, immediately. handām [And*m | = P, N andàm] member, limb. handarz [hndle | N andarz] advice, injunction, testament. handarzénidan, handarzén- [hndleyn-ytn!] advise.
605:wad-baxt [wtP ht! | N badbaxt] unfortunate. wad-dil [wtdyl | M wddyl, N baddil] coward(ly). wadgarih [wtglyh] evil-doing. wād-ģirdaģ [w° tgltk' | (N gird-bād)] whirlwind. wad-góhr [wtgwhl | N bad-gauhar] ill-, low-born. wad-kamag [wtk’mk'] malevolent. ~ih: malevolence. wadrang [w’ ting | N bādrang] citron. cc Dë [-bwd | N -bóya] lemon balm. wad|-tóhm [wttwhm] = wad-góhr. ~-wazag [-w’ck! | (N gawāža)] abuse. --.Xém [-hym] ill-natured. waf- [wp- | Р wf-, (N bàf-)] weave. ~išn: weaving. wafr [wp! | M wpr, N barf] snow. ~énag [-ynk!] а sweetmeat. waydān [wy?n! = Av. waybana-] head (ahuric). wahāg [wP?k! | M тор, N baha] trading; value. — burdan: value, estimate. wahār [wh], (bj?l) | M wkr, № bahar] spring. ~ig [-уЁ! | N -z] spring, vernal. wahig [ZZLA < A Semi (?); whyk' | M whyg, N *bahi] kid; astr. Capricorn. wahist [ол | M whyst, N bihist] paradise. ~Ig [-yk! | N -1] (worthy) of paradise. Wahman [whwmn' | M whmn, N bahman] Good Mind, the first Amahra- spand, guardian of cattle; cal. 11th month; 2nd day. wāhmān [*w-n! = whmn' | MOw^hmn, J whmn, N bahman] so-and-so. Wahrām [wlhl?’n', whPm | M whr’m, N bahram] god of war, victory; astr. Mars; cal. zoth day. ātaxš 1~: a major sacred fire. wak [wk! | N bak] frog. wālan [zo n! | (IN barzan)] settlement, community walg [wlg] = warg. walidan, wāl- [w]-ytn! | N bdlidan] grow, increase, prosper. ~išn: growth. wümidan, wam- [w’m-yin'] vomit. wan [wn' | N bun] tree; stock, stem. ~ i $urgünig : pistachio tree. ~ 1 was-téhmag: the Tree of Many Seeds. wān-, ~išn, v. wanidan. wanafšag [zvnpšk! | N bunafša) violet. Wanand [wnnd] astr. Vega. wandaģ [wndk'] rope, cord. wang [KALA < А ql’; wng | = M, N bang] voice, cry. wānīdan, wan- [wn-ytn! | M w’n-yst] conquer, overcome, destroy.
2730:marigold namēwahār,
3790:spring(time) wahār, afsālān, mēdyē- zarm; (a.) wahārīg.
5288:nihal, wahār, waxr
5291:wahārīg \ NT 1 wehm -eQU'I wahmān (am A 1 wēhmih MGV \ niyāz CAV wiyābānīh AS Ү” OU \ wiyābānēn- - rr QU wiyābānēnīdan (1183 P r^ ay wiyābānīg 143 ar 12wiyābān: V QUy
=== NYB vahar
6165:wh’r: vahār
=== HUB behar/bahar
```


## [2026-09-05T05:28:49.958Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '17795,17830p' incoming/BQT/BQT_v3_pages.txt",
 "description": "Borhan farxar entry context"
}
```


### [2026-09-05T05:28:50.010Z] TOOL RESULT

```
است ( .500 ‎oT, ) Gauthiot,JA.,1911,[,pp.53‏ خود از2 ۷108 سانسکرت کرفته
شد که اين کلمه خود در فارسی بصورت « بهار © درآمده ‎ty.‏

‎Henning, Sogdian loan— words..., BSOS.X.1, p. 94.

‎(Bargh4r) farkharus ‏فقه‌اللفه‌کمة‎ bod ‏از‎ : aig cosy ‏مینورسکی باستناد قول‎

‎canis‏ ۷102۳2 مرتبط ‎cos‏ بلکه‌کلمه‌ایست ایرانی‌ازربتة ‎paru - xuvathra‏ ® ( پر
از شادی ) . ركك : .7-8 ,]2024 , 1928, ‎Benveniste, Bull . Soc. Ling.‏

‏« میلورسکی . حدود ۷۹۳ ح ۷ >

‏۴ « فرخار بز رکه > در تبت است . مولف حدودالمالم در « سخن اندر ناحیت تبت و

‏شهر های وی » آرد : «کرسانك از تبت است و اندر وی بتخانه‌های بزرگه است » آنرا فرخار
‎Sy‏ خواشد > « حدودالمالم > 4۸ > وآن در ‎col Lhasa‏ « میلورسکی. حدود ‎۲٩۳‏ > .
ونیز فرخار نام شهریست در طالقان ( ماوراءالتهر ( « حدود . میئورسکی ص ۳۳۰ , ۳۵۰ > -
لترنج ‎(ta)‏ کوید : در میان شهرهای ختل . یکی فرغان با فرغار است که در کنار رودی

‏بهمن نام جای دارد . ۴ ‎(pa) Gent‏ ۴ - مسحف « فرخال >
‎=e‏ فرخواکه (هم) . ۱ - «سبط . فرخال » ( السامی‌فی‌الاسامی چاپ
تهران ص ۱۹) :

‏زلف فرخالت ز سرتا پا گرفت.
فیروز مشرقی «فرهنگه ‎tells‏
‏فرخش ‏ پرخج ** پرخش ‏ «فرخج»

‏سرو ‎gee‏ ترا در مشك تر

‏۲ ۳ مخفف « فروختار © ‎=A Cem)‏
فشره بود بعنی پلید وزشت . لبیبی گوید :
ای بلفرخج ‎ol‏ همیدون فرخج نامت فرخج و کنیت ملعونت بلفرخج >
« لفت فرس ‎٩۰‏ ورك :ص۷۳ > ورك : فرخجی .
[pdf page 246]
—~\ter—
```


## [2026-09-05T05:28:52.810Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport re\nfor f,off,pat in [('PHD.txt',-21,'wahār \\\\[wh'),('NYB_vol2_glossary.txt',-8,\"wh’r: vahār\")]:\n    t=open(f,encoding='utf-8',errors='replace').read()\n    m=re.search(re.escape(pat),t)\n    if m:\n        leaf=t[:m.start()].count('\\f')\n        print(f,'leaf',leaf,'printed ~',leaf+off)\n        print(t[max(0,m.start()-300):m.start()+300].replace('\\n',' ')[:600])\n    else: print(f,'not found')\nEOF",
 "description": "Page numbers for MacKenzie and Nyberg"
}
```


### [2026-09-05T05:28:54.276Z] TOOL RESULT

```
PHD.txt not found
NYB_vol2_glossary.txt leaf 284 printed ~ 276
xtan tyj, tyz: téz tym’r: timar tyrs-: tarsitan tys: cis tyšng: tišnak tz-: tacitan w’br, wbryg, w’bryg’n: vāparīkānēh wd: vat w'n-, wnyst: vanitan wng: vang wrn: varan w'wrydn: vaparikanéh weydn, wzy-: vicitan wd: vat wde-: vitāxtan wdr: vitarg wdyb: viyiftan wdyr-: vitartan wfr: vafr wh'ng: bahān wh’r: vahār whmn: Vahuman whr’m: Vahräm whwryd: vihiréh why: véh whyšt: vahišt whyz-: vihez- wn’hg’r: vinás-kàr wnd'dn, wynd-: vindätan wn’stn, wn'h-: vinäsitan wnybwt: äkasi wr: ivar WIC, WTZ: varc wre’wynd: varcávand wrdg: vartak wrwyšn: virroyišn wrwystn: virrčyistan wrz: lvarz ws: vas wštn, wrd-
```


## [2026-09-05T05:29:11.191Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('PHD.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nfor ln in [605]:\n    leaf=t[:sum(len(l)+1 for l in lines[:ln-1])].count('\\f')\n    print('PHD line',ln,'leaf',leaf,'printed ~',leaf-21)\nEOF\nsed -n '17770,17796p' incoming/BQT/BQT_v3_pages.txt",
 "description": "PHD page and more BQT context"
}
```


### [2026-09-05T05:29:12.937Z] TOOL RESULT

```
PHD line 605 leaf 111 printed ~ 90
است که جنکه و جدال و خصومت و ناوردباشد.
‎BSS‏ - بروزن افلاك . بسنی موی
بی خم و چم و فروهشته و بیحرکت باشد یمنی
‎ay‏ درهم پیچیده و مجعد لباشدهمچوزلفهای

۱0۲

عملی زدان ۴ — باکاف فارسی بمعنی گوشتابه
وقلیه‌ایت که بربالای آن نخم مرغ ریزندچه‌فر
‎cine‏ بالا و خاک تخم مرغ راگویند * .

فرخال © بروزن بخچال » بمنی اول
فرخاك است که موبی ‎th‏ بیحر کت وبی شکن
وفروهشته ۷ .

‎J‏ ختاد ۷ - بکس‌اولوضمالی‌وسکون
‎ott‏ وفوقانی ‎Dk‏ کشیده و برای قرشت زده »
بمعنی فروشندهباشدیعتی شخ که‌چیزی میفروشد.

‏فرخچ ۸ ‎gly Jl pe‏ و سکون
‎elt‏ و جیم ‎ould‏ کفل اسب و دیگر حیوانات
را گوبند - و بمعنی زشت و نازیبا هم کفته اند
— و بععنی رشوت و پاره نیز آمده است ؛ وباجیم

‎farxar - ۱‏ فارسی ( بمعنی ‎po‏ ومعبد (بتخانه) ) از ‎U5‏ سفدی ‎Brgh’r‏ مأخون
است ( .500 ‎oT, ) Gauthiot,JA.,1911,[,pp.53‏ خود از2 ۷108 سانسکرت کرفته
شد که اين کلمه خود در فارسی بصورت « بهار © درآمده ‎ty.‏
```


## [2026-09-05T05:29:14.220Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; pdftoppm -f 71 -l 71 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg71 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/",
 "description": "Render PDF page 71"
}
```


### [2026-09-05T05:29:16.355Z] TOOL RESULT

```
total 736
drwx------ 2 sfmqrb sfmqrb   4096 Sep  5 01:29 .
drwx------ 4 sfmqrb sfmqrb   4096 Sep  5 01:20 ..
-rw-rw-r-- 1 sfmqrb sfmqrb 669351 Sep  5 01:29 bqt733.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  71145 Sep  5 01:29 pg71.png
```


## [2026-09-05T05:29:27.131Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; S=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad; pdftoppm -f 71 -l 71 -r 300 -png -singlefile EtymologicalDictionary-persian-english.pdf $S/pg71_300; ls -la $S; ls site/pages/71.jpg 2>/dev/null",
 "description": "Render page at 300dpi"
}
```


### [2026-09-05T05:29:29.766Z] TOOL RESULT

```
total 1088
drwx------ 2 sfmqrb sfmqrb   4096 Sep  5 01:29 .
drwx------ 4 sfmqrb sfmqrb   4096 Sep  5 01:20 ..
-rw-rw-r-- 1 sfmqrb sfmqrb 282104 Sep  5 01:29 bqt733_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb 669351 Sep  5 01:29 bqt733.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  75801 Sep  5 01:29 pg71_300.png
-rw-rw-r-- 1 sfmqrb sfmqrb  71145 Sep  5 01:29 pg71.png
site/pages/71.jpg
```


## [2026-09-05T05:29:31.826Z] TOOL CALL #44: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg71_300.png"
}
```


### [2026-09-05T05:29:32.523Z] TOOL RESULT

```

```


## [2026-09-05T05:29:32.520Z] INPUT

[Image: original 2550x3300, displayed at 1546x2000. Multiply coordinates by 1.65 to map to original image.]


## [2026-09-05T05:29:48.063Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== SNS hus\"; grep -n \"hu[šs]\\b\\|hūš\\|hōš\" SNS.txt | head -20; echo \"=== SNS pages hus\"; grep -n \"huš\" SNS_pages.txt | head -20",
 "description": "Grep Shayast ne Shayast glossary"
}
```


### [2026-09-05T05:29:48.130Z] TOOL RESULT

```
=== SNS hus
5315:.AiKi^ <AiS*£l». :hus&n/ti!i 
5419:jKjd*. « f -»* -*:.-■ ioIaoIv ' (»Wi>*:hus-baja/us-bam: 
13403:dthus- 
16320:Uyacinthus w* hyakinthos : „»V3U»«* *1JWtf 
28299:mithus- 237/2 
32410:hus/us-bara 67/2 
=== SNS pages hus
```


## [2026-09-05T05:29:49.201Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== FRS farxar\"; grep -n \"فرخار\" FRS_pages.txt | head -10; echo \"=== AHD aus\"; grep -n \"^aus-\\|^wes-\\|^awes\" AHD_watkins1985.txt | head -20",
 "description": "Loghat-e Fors and Watkins"
}
```


### [2026-09-05T05:29:49.296Z] TOOL RESULT

```
=== FRS farxar
5796: ‫منماو را شمن وخانة منفرخار است؟ |‬
5827:   ‫‪ - ۴‬این اغت فقط در عم ول هست ‪.‬‬            ‫نسبت داده » چ لفت فرخار را ندارد ‪.‬‬
7457:                                       ‫شهریست نزديك فرخار آن‬
8814:                                      ‫یکی خانه کرده است فرخار دیس‬
=== AHD aus
133:wes-pero-. The Indo-Europeans oriented themselves by facing east. Therefore the root deks-, “right,” could also denote “south.” “Right” was considered lucky; the terms for “left” vary from language to language (one Indo-European term is laiwo-) and were evi- dently subject to taboo.
316:aus-', To shine. 1. Germanic *aust- in: a. Old English éast, east (< “the direction of the sunrise”): EAST; b. Old High German 6stan, east: OSTMARK. 2. Germanic *aus- tra- in: a. Old English éasterne, eastern: EASTERN; b. Late Latin ostro-, eastern: OsTROGOTH. 3. Germanic *austron-, a dawn-goddess whose holiday was celebrated at the vernal equinox, in Old English éastre, Easter: EAsTER. 4. Probably suffixed form *ausds-, dawn, also Indo-European goddess of the dawn, in: a. Latin auréra, dawn: AURORA; b. Greek éds, dawn: EO-, Eos; EOSIN. [Pok. aues- 86.]
317:aus-?. To draw water. Suffixed form *aus-yo- in Latin haurire, to draw up: EXHAUST, HAUSTELLUM, HAUSTO- RIUM. [Pok. aus- 90.] awi-. Bird. I. 1. Latin avis, bird: AVIAN, AVIARY, AVI- ATION; AVICULTURE, AVIFAUNA, BUSTARD, OCARINA, OSPREY, OSTRICH. 2. Compound *awi-spek-, “observer of birds” (*spek-, to see; see spek-), in Latin auspex, augur: AuSPICE. II. Possible derivatives are the Indo-European words for egg, *dwyo-, *ayo-. 1.Germanic *ajja(m) in: a. Old English 2g, egg: COCKNEY; b. Old Norse egg, egg: EGG. 2, Latin 6uum, egg: OVAL, OVARY, OVATE, OVI-, OVOLO, OVULE, OVUM. 3. Greek dion, egg: 00-. [Pok. auei- 86.] awo-. An adult male relative other than one’s father. 1. Latin avus, grandfather: ATAVISM. 2. Latin avunculus, maternal uncle: AVUNCULAR, UNCLE. 3. Latin avia, grandmother: AYAH. [Pok. auo-s 89.] ayer-. Day, morning. 1. Germanic “*airiz in: a. Old Eng- lish &r, before: EARLY, ERE; b. Old Norse dr, before: OR2. 2. Germanic (superlative) *airistaz in Old English rest, earliest: ERST. [Pok. ajer- 12.] ayes-. A metal, copper or bronze. Latin aes, bronze, money: AENEOUS, ERA. [Pok. aios- 15.] baba-. Root imitative of unarticulated or indistinct speech; also a child’s nursery word for a baby and for various relatives. 1. Middle English babelen, to babble: BABBLE. 2. Middle English babe, babi, baby: BABE, BABY. 3. Italian bambo, child, simpleton: BAMBINO. 4. Polish baba (diminutive babka), old woman: BABA, BABKA. 5. Russian baba, old woman: BABUSHKA. 6. Rus- sian balalaika, balalaika (imitative of the sound): BALA- LAIKA. 7. Latin balbus, stuttering, stammering: BOOBY. 8. Greek barbaros, non-Greek, foreign, rude (< “one who speaks incomprehensibly”): (BARBARIAN), BARBARISM, BARBAROUS. 9. Hindi babi, father: BABU. [Pok. baba- 91.] badyo-. Yellow, brown. A Western Indo-European word. Latin badius, chestnut brown (used only of horses): BAY’. [Pok. badios 92.] bak-. Staff used for support. 1. Probably Middle Dutch pegge (> Middle English pegge), pin, peg: PEG. 2. Latin baculum, rod, walking stick: BACILLUS, BAGUETTE; BAC- ULIFORM, DEBACLE, IMBECILE. 3. Greek baktron, staff: BACTERIUM; (CORYNEBACTERIUM). [Pok. bak- 93.] bamb-. Word imitative of dull or rumbling sounds. Greek bombos, a booming, humming: BOMB, (BOMBARD), BOUND}. [Pok. ba*mb- 93.] bands. A drop. Possibly Irish bainne, milk: BONNYCLAB- BER. [Pok. band- 95.]
1157:wes-!
1159:wes-1. To buy. 1. Suffixed form *wes-no- in Latin vénum, sale: VENAL, VEND. 2. Suffixed o-grade form *wos-nd- in Greek dneisthai, to buy: DUOPSONY. [Pok. 8. wes- 1173.]
1160:wes-?. Wet. Germanic *wdés- in Old English wés, juice: 00ZE}. [Pok. 3. wes- 1171.]
1161:wes-3. To stay, dwell, pass the night, with derivatives meaning “to be.” 1.O-grade form *wos- in Germanic *was- in Old English wes, was: was. 2. Length- ened-grade form *wés- in Germanic *wéz- in Old English wére (subjunctive), w#ron (plural), were: WERE. 3. Ger- manic *wesan in Old Norse vesa, vera, to be: WASSAIL. 4. Suffixed form *wes-td- perhaps in Latin Vesta, house- hold goddess: Vesta. 5. Suffixed variant form *was-tu- possibly in Greek astu, town (< “place where one dwells”), whence Latin astus, skill, craft (practiced in a town): ASTUTE. [Pok. 1. wes- 1170.]
1162:wes-‘. To clothe. Extension of eu-'. 1. Suffixed o-grade form *wos-eyo- in Germanic *wazjan in Old English werian, to wear, carry: WEAR}, 2. Suffixed form *wes-ti- in Latin vestis, garment: VEST; DEVEST, INVEST, REVEST, TRAVESTY. 3. Suffixed form *wes-nu- in Greek hennunai, to clothe: HIMATION. [Pok. 5. wes- 1172.]
1163:wes-pero-. Evening, night. I. Reduced form “wes-. 1. Suffixed form *wes-to- in Germanic *west- in: a. Old English west, west: WEST; b. Old English westerne, western: WESTERN; C. Old English westra, more west- erly: WESTERLY. 2. Possibly Germanic *wis- in Late Latin Visigothi, “West Goths” (Gothi, the Goths): Vist- GorTu. II. Basic form *wespero-. 1. Latin vesper, evening: VESPER, VESPERTILIONID. 2. Greek hesperos, evening: HESPERIAN. [Pok. wesperos 1173.]
```


## [2026-09-05T05:30:00.434Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== AHD wesr/spring\"; grep -n \"wesr\\|wes-r\\|VERNAL\\|vernal\" AHD_watkins1985.txt | head -20",
 "description": "Watkins wesr root"
}
```


### [2026-09-05T05:30:00.483Z] TOOL RESULT

```
=== AHD wesr/spring
316:aus-', To shine. 1. Germanic *aust- in: a. Old English éast, east (< “the direction of the sunrise”): EAST; b. Old High German 6stan, east: OSTMARK. 2. Germanic *aus- tra- in: a. Old English éasterne, eastern: EASTERN; b. Late Latin ostro-, eastern: OsTROGOTH. 3. Germanic *austron-, a dawn-goddess whose holiday was celebrated at the vernal equinox, in Old English éastre, Easter: EAsTER. 4. Probably suffixed form *ausds-, dawn, also Indo-European goddess of the dawn, in: a. Latin auréra, dawn: AURORA; b. Greek éds, dawn: EO-, Eos; EOSIN. [Pok. aues- 86.]
1055:swesor-. Sister. 1. Zero-grade form *swesr- in: a. Ger- manic “swestr- in Old English sweostor, sister: SISTER; b. suffixed form *swesr-ino- in Latin sobrinus, maternal cousin: COUSIN. 2. Latin soror, sister: SORORAL, SOROR- ITY. [Pok. suesor 1051.]
1164:wesr. Spring. Latin vér, spring (phonologically irregular): VERNAL; PRIMAVERA. [Pok. wes-r 1174.]
2449:VENUE gWa- VENUS wen-1 VERACIOUS wéro- VERB wer-6 VERBENA wer-3 VERBOTEN bheudh- VERDANT virére VERDICT deik-, wéro- VERDITER ters- VERGE? wer-3 VERIDICAL deik-, wéro- VERIFY wéro- VERISIMILAR wéro- VERISM Wéro- VERITY wéro- VERMEIL wer-3 VERMI- wer-3 VERMICELLI wer-3 VERMICULAR wer-3 VERMIN wer-3 VERNAL west VERRUCA wer-1 VERSATILE wer-3 VERSE! wer-3 VERSION wer-3 VERST wer-3 VERSUS wer-3 VERTEBRA wer-3 VERTEX wer-3 VERTIGO wer-3 VERVAIN wer-3 VERVE wer-6 VERY weéro- VESICA udero- VESPER weS-pero-
```


## [2026-09-05T05:30:01.751Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"### 5410-5425\"; sed -n '5410,5425p' SNS.txt; echo \"### 32400-32415\"; sed -n '32400,32415p' SNS.txt; echo \"### 5310-5320\"; sed -n '5310,5320p' SNS.txt",
 "description": "SNS context lines"
}
```


### [2026-09-05T05:30:01.827Z] TOOL RESULT

```
### 5410-5425

Uj .l^UuI *jlj 



?f 



jKjd*. « f -»* -*:.-■ ioIaoIv ' (»Wi>*:hus-baja/us-bam: 
bam+CGJVPE'. 281)uSas-: ^ J 1 * 1 ■ &* • j** :usah-i t- 
bhiraa-: ^^.^bama : t- (^U - ^^ '&- 'O^j- 1 'ur 1 *') 
6 hOsbam :L (Afir. Wan. I, 33) 'wsyb'm ijil»{GNPE. 40). 

,O^J>i>**M *;'* *>' *** JV=^ •• ; * i - :aviltab: o**.i •* 
(H^o"H . ti-l «j-T sravatO : ^^'•j'jtsW** (^ «j*-» 
### 32400-32415
hu-mfinisn 75/2 
hunar 76/2 
hunsandlh 75/12 
hu-rastagthatar 70/6 



husangd 65/14 
husparam 65/18 
husravlh 66/18 
hus/us-bara 67/2 
hu-xfimS 60/6-89/12 
hQxt 56/22 
hu-zahSg 65/1 
hu-zahagtar 65/3-162/9 
hvarst 76/5 
### 5310-5320
(Mir. Man. II, 62) 'zw J n:>=fc Uitffc. 1815) |lhvi* 
.*-t/\\ £(*j6-yf) hizvan: V (PS. 30) 'zw'ni-u^^ 

l/lfl 

.AiKi^ <AiS*£l». :hus&n/ti!i 
iGNPE. 1081 huska-: t- usk-: l*^'>' xuilt i 1 

\&/A*S .AiKliy :be husaned: i^K^*" - " 

-jjUiU^U^^j-iaSa^ixl C«i«3 fjl#->»: husparmm .J'
```


## [2026-09-05T05:30:21.197Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('SNS.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nfor ln in [5419,32410]:\n    leaf=t[:sum(len(l)+1 for l in lines[:ln-1])].count('\\f')\n    print('SNS line',ln,'leaf',leaf)\nEOF\necho \"=== FRS around 5790-5830\"; sed -n '5788,5800p' FRS_pages.txt; echo \"...\"; sed -n '5820,5830p' FRS_pages.txt",
 "description": "SNS leaf and Loghat-e Fors farxar entry"
}
```


### [2026-09-05T05:30:23.308Z] TOOL RESULT

```
SNS line 5419 leaf 0
SNS line 32410 leaf 0
=== FRS around 5790-5830
  ‫خنیده مبان کهان و مهان‬         ‫یکی شادمائی بد اندر جهان‬




                                            ‫‪ - ۱‬در رشیدی ‪ :‬فرخی ‪.‬‬
                                              ‫بت خانه بود » بواامل گفت ‪:‬‬
                            ‫بت من جانور آمد شمنش بی دل و جان‬
 ‫منماو را شمن وخانة منفرخار است؟ |‬


                                  ‫‪۳‬‬
                                      ‫ژغار‬
...


 ‫‪+ 9‬قرخاربلخانه هست وگوند شهرست درتر کستان وازآنجا وی وان خر‬
                        ‫و درآنجا بتخانههابیار است ‪ ۰‬رود کی گفت ‪:‬‬
        ‫گر مسدن آن بت نوایست‬                 ‫خرار بزر ککونيك جاییست‬
                                                                  ‫ف‬
‫اينبت فقط در ع هست و در س بیت مذکور در فوق رودکی را باب المثل‬               ‫‪۲‬‬
   ‫‪ - ۴‬این اغت فقط در عم ول هست ‪.‬‬            ‫نسبت داده » چ لفت فرخار را ندارد ‪.‬‬
‫کار بود و سخره » س ‪ :‬شاکار ببکار باشد » محرکت خوانند کاری‬         ‫لک‪۰‬ار‬
                                                                      ‫‪-‬ا‬
                                                                       ‫‪ 4‬ش‬
```


## [2026-09-05T05:30:32.506Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== BRT Frühling\"; grep -n \"Frühling\" BRT.txt | head -20; echo; echo \"=== BRT Morgenröte\"; grep -n \"Morgenröte\" BRT.txt | head -10",
 "description": "Bartholomae German glosses"
}
```


### [2026-09-05T05:30:32.585Z] TOOL RESULT

```
=== BRT Frühling
3998:•  j.  aiwyaaha-  f.  'Lesen,  Studium'  uzw.  1  durch,  dass  ihm  (dem  Schüler)  kein  Be- der  heiligen  Texte:  ka  asti  ihy^a  »la/^!  scheid  wird?"  N.  ij; —  vtspagsu  "partnti saonB  {%A.)f  ..  aya  doEna  disyut  .  .  yB  .vlspaiiü  *'fi*i  ästryeiti  "jedes  Mal,  wenn %ritarymaEm  ratüm  'kam  nHit  aiwyästi  \  Einwendung  erhoben  und  kein  Bescheid Mit  gä'hs  srävaydti  "..  er  könnte  durch  gegeben  wird,  versündigt  er  sich"  N.7_J. seine  schlechte  Religion  (einen)  dazu  ver-  j  P"--  a/rälgda^Hnih.  —  ■>  s.  No.  3, 4.  —  i)  Ausg. leiten,  daas  er  wihrend  der  drei  (dafür!  l%^fZtl,^tl  ^- *)'m^^''Sr5ti~  ^'  "^ bestimmten)  Frühlinge'*  dem  Studium  (der  .""''  '',"^''  __  .  /'  ,™  '  .  ,  , ■    -       _       ,    .  ."    ,^..     •  ].  a-fra'oxiayant-  Adj.  (fem.  yan/i-)
14301:Eig.  'die  siegreiche ■>  Frühlingszeit';  "väAara- n.,  Ableit.  (mit  ^r'^düi)  aas  vaaiar-.  — >)  Oder  atlenfalli  'stariie,  gewaltige' ;  s, *%üra-  No.
14683:•  j.  9-ri.zar9maya-  i)  Adj.  'drei  Frühlinge umfassend':  yS  'malm  ratüm  aiwyänkqm (sd.)  nBit  aiwyästi  V,  s8. 9.  a)  n.  'Zeit- raum von  drei  FrUblingen  (sva.  Jahren)': 'maOn  xratOm  asavanfm  aiwyäiahal  (sd.) N.Ji.
19665:tagnndnachtgleiclie,  Sp.  auf  den  i.  Min.  Die Angaben  in  Bd.  35.  3,  6  widersprechen  licb, indem  einerseits  der  letzte  Tag  von  Maiiyöi- hma  als  der  längste  —  und  entsprechend  der von  Maüyäirya  als  der  künette  —  bezeichnet, anderseits  der  leCite  Tig  des  Jahrs  aur  den  Tag des  Frühlingiäquinoktiums  verlegt  irird.  Vgl Bthl.  IF.  5.  261,
22489:•  j.  vaDhar-  (,  p.  vaAar-)  n.  'Frühling': wawri  (LS.)  F.  8.

=== BRT Morgenröte
8270:Ableit.  aus  *ii/iaii!ak-  (Komp.:  upa-^-ulah-)  f. 'Nähe  der  Morgenröte.  Osten'.
8703:•  j.,  g.  uSah-  :  uä-''  f.  1)  'Morgenröte, Morgen':  kS  yi  'Sa  (NS.)  arSm.ptiwä (sd.)  xiapsca  Y.44.$;  — ■  ayram  usailTm 'sirihtm  Yt/4-2o;  — /räymat  *s3nA?m süraya  *i'ft'i/f/«  (sd.)  Yt.  J.62;  62,  /5.S5;
8723:Eig.  'der  sein  Haus  io,  bei  der  Morgenröte hat',  Komp.  mit  LS.  (zuiiSai-)  im  1. Glied.— Pü.:  IIS  diisljr,  erl.;  api  maziyTnll.  —  ')  Vyl. iUex.  S  402.
18304:•  j.  fnrstay-  f.  'Heran-,  Herzukommen': aat  usat»kqm  para  'isit . .  parödar!  a^rS vsRm  surunaoiti  ".  .  vor  der  Ankunft  der Morgenröten.."  FrW.j0.41.  2)  'Sich- vorwärtsbewegen,  .Vorwäitsstreben,  Eifer': *ysijiim  haivkäna  (sd.)  o/aÄJ  °Hla  Y.  8.  z.
23289:•  j.  'vah-  V.  'aufleuchten'  von  der Morgenröte.  Praes.  14  (Inkob.)  «wo-.  — InC  'usa.
24268:•  j.  *vi-vitay-'>  £  'Aufleuchten':  '^raosta xia/hS  ^rityajri  /räymat  uiävh»m  särayä 'lim  ". .  gelangte  er  zur  Morgenröte,  zum Aufleuchten  der  gewaltigen"  Yt.5. 62.
24723:•  j*  vy-us%'>  Inf,  'aufzuleuchten',  von  der' Morgenröte:  >rity&  xlaps  %raostavy  sa-\ layetü  (sd.)  "bei  der  Vollendung  der  dritten  I Nacht  sieht  man  die  Morgenröte  aufleuch-  \ ten"  H.  2. 7,  25.  ]
24829:-  »)  So  L4  und  K  I  (wVO;  Jp  i  usw.  und  NA. mi\  Pü. !  tti  'Morgenröte'.     S.  lu  ^vah-.
```


## [2026-09-05T05:30:46.615Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport re\nt=open('BRT.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nleaves=t.split('\\f')\ndef leafof(ln): return t[:sum(len(l)+1 for l in lines[:ln-1])].count('\\f')\nfor ln in [22489,8703,8270,23289,14301]:\n    L=leafof(ln)\n    nums=re.findall(r'(?m)^\\s*(\\d{3,4})\\s*$', leaves[L])\n    print('line',ln,'leaf',L,'cols on leaf:',nums[:8])\nEOF",
 "description": "Bartholomae column numbers"
}
```


### [2026-09-05T05:30:48.337Z] TOOL RESULT

```
line 22489 leaf 741 cols on leaf: ['1347', '1348']
line 8703 leaf 255 cols on leaf: ['415', '416']
line 8270 leaf 242 cols on leaf: ['391']
line 23289 leaf 765 cols on leaf: ['1393', '1394']
line 14301 leaf 449 cols on leaf: ['788']
```


## [2026-09-05T05:30:57.184Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== IEC wesr\"; grep -n \"^u̯esr\\|^wesr\\|^uesr\\|^ues-r\\|^uesar\" IEC.txt | head; grep -n \"'spring'\" IEC.txt | grep -i \"ues\\|wes\\|uas\" | head -10; echo \"=== IEC aus\"; grep -n \"^ausos\\|^aus-\\|^auses\" IEC.txt | head",
 "description": "Mann IEC lookups"
}
```


### [2026-09-05T05:30:57.265Z] TOOL RESULT

```
=== IEC wesr
=== IEC aus
```


## [2026-09-05T05:30:59.255Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== MON bahar\"; grep -n \"بهار\" MON_part1.txt | head -5; echo \"=== MON farxar\"; grep -n \"فرخار\" MON_part1.txt MON_part2.txt | head -5; echo \"=== MON hushbam\"; grep -n \"هوشبام\" MON_part1.txt MON_part2.txt | head -5; echo \"=== ARY bahar\"; grep -n \"بهار\" incoming/ARY/ARY_pages.txt | head -5",
 "description": "Mo'in and Aryanpur lookups"
}
```


### [2026-09-05T05:30:59.375Z] TOOL RESULT

```
=== MON bahar
578:بها, بهار ۳-9-۳ 
1255:طغیان و افزايش آب در فصل بهار. 
1512:ختنی بهار؛ بهار] (امر.) بهار. ضح.- در 
1515:ابسالان: 205217 (امر.) بهاران. فصل 
1516:بهار» هنگام بهار» و بهاران. 
=== MON farxar
MON_part2.txt:5964:فرخار: ۱۲ [(بهار. دیر؛ معبد] (ا.) 
MON_part2.txt:5966:که مردم آن زیبا باشند؛ ج. فرخارها. 
MON_part2.txt:5969:آراسته و مجلل. مانند شهر فرخار: زیبا و 
=== MON hushbam
=== ARY bahar
5092:چم اين واژه در اوستایی و بهاری: پل‌گدار.
```


## [2026-09-05T05:31:05.604Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"### MON farxar\"; sed -n '5958,5975p' MON_part2.txt; echo \"### MON bahar1\"; sed -n '1505,1525p' MON_part1.txt",
 "description": "Mo'in entries context"
}
```


### [2026-09-05T05:31:05.675Z] TOOL RESULT

```
### MON farxar

فرخ: | (.) جو جه (مرع) جوره 
ج. فراخ» فروخ افراخ. 

فرخ: ۷ [تابان؛ مجلل. زبا] (ص.) 
خجسته. مبار ث. میمون. زیبا. جمیل. 
فرخار: ۱۲ [(بهار. دیر؛ معبد] (ا.) 
بتکده. بتخانه. (.) هر شهر حسن‌خیز: جایی 
که مردم آن زیبا باشند؛ ج. فرخارها. 

فر خاردیس: :۱-1 (ص‌مر.) مانند بتخانه, 
آراسته و مجلل. مانند شهر فرخار: زیبا و 


اراستد. 


فر هنکت فا 
### MON bahar1
خوش خلق نشان دهد و در باطن شرور و 
فتنه‌انگیز باشد. زیرکی که کارهای خود را 
پوشیده انجام دهد مکار» حیله گر. رواج و 
رونق مخفی» خوبی و نیکی پوشیده. 

ایژ: 3 - ابیز اب ] (.) شرارةٌ آتش 
ابسال: 205 [آنچه سال را آغاز می‌کند؛ 
ختنی بهار؛ بهار] (امر.) بهار. ضح.- در 
فرهنگگ ها ابسال و آسالان را به معنی باغ 
گرفته‌اند و صحیح نست. (مینوی). 
ابسالان: 205217 (امر.) بهاران. فصل 
بهار» هنگام بهار» و بهاران. 

اب ‌سیز: 20-7 (امر.) (یز.) بیماریی در 
چشم که از فشار درونی چشم پدید آید. 
ایست: ۱ (ص. .) ز مین آماده شده 
برای زراعت. 

ایست: 025 [ - آینستن] (ص.) ی 
زهدان؛ رحم
```


## [2026-09-05T05:31:07.502Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"spring\" IEC.txt | grep -in \"ues\\|uas\\|uos\" | head -10; echo \"===\"; grep -n \"^uesr\\|uesr-\\|uesn-\" IEC.txt | head -10; echo \"=== ausos\"; grep -n \"ausos\\|auso-s\\|'dawn'\" IEC.txt | head -10",
 "description": "Mann dictionary search"
}
```


### [2026-09-05T05:31:07.594Z] TOOL RESULT

```
33:12236:oquis (1), (ogus) ‘eye’. Cf. oqumn-, oquos, etc. WP I, 169 Skt. aksih, f., áksi, n. (dual: áksini); Av. aši, (dual), id.; Oss. cf. w-a&i ‘face’; Tokh. A ak, B ek (dual: asån, B e$ane); Arm. ačk (pl. form), id.; beside akn, gs: akan ('eye; jewel; source, spring’, fr. *oqumn-, and hawnk, pl. “eyebrows”, fr. *epi-oqunes, cf. Gk. epópsis ‘view’; epópé *look-out); Scyth. cf. -aspo- (in Arimaspo-); Gk. Ops, gs: Opós, f. “sight, face’; Ópis, gs. Ópidos, f. (1) “regard, favour”: ósse, (dual: *eyes"); (the first form embodies the def. art. and is thus distinct fr. ops 'voice"); Alb. cf. as- (in as-kath ‘stye’, fr. *oqui-koKos); Br. Cor. -ep, -eb, W -eb, (in gwyn-eb ‘face’, fr. *uin- do-^); (also in Br. én-ep, Cor. id. ‘facing’: Gk. en-ópios, id.); ON (?) ey, pl. eyjar, f. (*island', fr. *oqui-7; OCS and Com. SI. oci, dual. n. “eyes”; Li. akis, gs: -iés (dual: aki), f.; Latv. acs. gs. id. gpl: acu, f. ‘eye’
34:12241:oqumn- (oqunom) 'eye, eyehole'. Cf. WP I, 169 and equos, oquis & cpds. Av. (?) akanom, n. (?) (queried: ‘terret, har- ness-ring'); Arm. akn, gs: akan, s. ‘eye, jewl; source, spring” beside akani, gs: -vo, ab. s. -eav
35:12253:oquos (oquios, oquio(n)), cf. oqu-, oquis, oqumn-, etc. WP I, 169-171 Arm. akn, and aæk ‘eye; eyes’; Hes. ókkon, n. id.; Gk. opé, f. “hole, esp. in roof beside Ops, gs: Oopós (eye, embodying the def. art.); S kt. cf. aksah, am. m. n. beside aksan, n. ‘eye’; Tokh. ak, gs: akis, dual: asån, id.; Scyth. spoü, s. id.; Dor. ókkos, m. id.; cf. óssos, m. “pupil of eye'; OCS cf. oko, gs: ocese, n. id. beside dual: oci (and com. $1.); Li. ákas, m. 'ice- hole’; Latv. aka, f. ‘spring, source
37:12435:pá$- (2) “stir, rouse; bestir oneself, jump, bounce’. Cf. pég- S kt. cf. apa-pa-paje, 3s. aor. ‘he started back’; pajas, n. ‘vigour, brilliance'; Gk. pegé, Doric págà, f. “spring, source’, cf. pégasos, Dor. pā- gasos (‘springing horse”, fr. *pag-oKuos); LG facken, v. 'throw'. A possible variant occurs in Hiero-Hitt. *pé&yas, peyamas ‘dashing, springing and in ON fákr, fák-hestr, m. ‘horse’. See pe&-
51:15305:seuos (2), (seuəthos) ‘flow, movement. Skt. saváh, m. 'soma-juice'; cf. Savathah, m. (river name); Arm. (?) hor, o-st. (^welP, lit. ‘spring, source"?) beside hiwt', s. “juice”; Illyr. cf. Auas (river-name); Alb. ujé, m. n. *water'; Maced. cf. Sava (river-name); Ligurian (Ru- mansch substrate) sava, seva, f. “drain, chan- nel
53:16720:soquos (soqu) (1) “juice, sap, liquor, exu- date’. Cf. WP II, 515 Tokh. saku, B sekwe, s. *pus; grease'; Scyth. áskhu, s. ‘juice’; Oss. cf. àxsa-pal, s. ‘ʻa honey- bearing plant'; Hitt. sakwis, s.? (queried: ^well, spring’, but cf. Gk. ómma: Hitt. sakwa, dual. “pair of eyes? fr. *soqumo); Gk. opós, m. “juice, sap, moisture' (once: hopós); Alb. gjak, m. ‘blood’; Lat. (w. infantine doubling) succus, gs: 31, m. ‘juice’; OHG sou, n. ‘sap’; OE seaw, m. as Gk.; Fris. sjeu, s. ‘gravy’; (oxytonic prototype in) Icel. saggi, m. ‘moisture���; OCS sokü, R. Srb. sok, m. “juice, sap’; Li. sakai, m. pl. ‘pitch, gum, resin’; OPr. sackis, id.
68:20148:uesər- (1) (variants: uesənt-, uesõr, uesna) ‘dawn, springtime’. WP I, 310 Skt. vasar, n. ‘dawn’; cf. vasantáh, m. ‘spring- time’; Av. văhrō, m. and vahār, pl. id.; Ober vahāra-, Per. bahār, id.; Arm. garun, cpds: garn- & garna-, id.; Gk. éar, gs: éaros; er, gs: Gros, and (Hom.) eíar, gs: eíaros, n. “morning, spring’; cf. éri, adv. “in the morning’; Lat. ver, gs: veris, n. ‘spring’; OBr. guiann-uin, id. (lit. *white-spring); OW and W gwan-wyn, id.; OCor. guantoin, id.; ON vár, n. and Vár, f. ‘spring; goddess of Spring’; Sw. vår, f. ‘spring’; OFris. wars, id.; OCS (and com. Slav.) vesna, f. id.; Li. vásara, f. id.; vasáris, gs: -io, m. *February'; Latv. vasara, f. summer
69:20183:uesnà, is ‘springtime’. Variant of type uesor- (1) Gk. cf. enis, gs: -ios ‘yearling’; Lat. cf. ver- nalis, adj. “of spring’; OCS vesna (and com. SI.) ‘springtime’
===
5793:(1) & (2) : Skt. cf. antar-ja ‘inbred’ Arm. cf. ajla-zan 'dif- ferent’; Gk. neo-gnos, etc.; Lat. privi-gnus; Go. sama-, alja-kuns; Sw. cf. sys-kon ('sib- lings’. See suesr-)
16699:som-, cpds. ctd. -poquos in Skt. and Arm. (amok, i, av); -s- in Skt. ON & OCS; -séd- in Skt. Arm. (ham- et ‘saddle’ and ham-est “modest'), OCS and (LW) Hung. (szom-széd); -ster-, -stor- in Skt. and Arm. (at or, o-st. ‘throne, seat); -suesr- in Oss. (ünsuvár, äfsímär “brother?), Per. ham- Site “sister” and MHG; -uest- and -uist- in Skt. & Gmc. (but Arm. han-gist, gs. -gsti, ab. s. -gstav fr. *som-uiKt-); -uoid- in Skt., Arm. (hanget 'similar), ON. Sw., and Srb. (savest, f. "conscience; -uort- in Skt., OCS & Li.; -urtt-, -urst- in Skt. & Srb.
18019:suesór, suesor ‘sister’. Cf. sue- and extns., sər- and suesrios. (Z-gde in some Gmc. forms). WP II, 533 Skt. svasr & svasa, id.; Av. xwáha, acc: xwá- harom, id.; Per. xàhar, id.; Ossetic xwärä, cpds. xárá-, id.; cf. also án-suvár (“brother”, if for *som-suesr-, cf. G Ge-schwister); Tokh. A sar, B ser ‘sister’; Arm. Eur, gs: Ker, ab. sing. kerb, id.; Hes. éor, pl. éores ‘sister, daughter’; Lat. soror, gs: -oris, f. ‘sister’; Olr. siur, Ir. siür, gs: seather, id.; W chwaer, pl. chwiorydd, Br. choar, pl choarézed, Cor. whor, pl. wheryth, id.; OHG swéster, MHG id. and suster, süster, id.; Go. swistar OE sweostor, pl. -tra, -tru, Du. zuster, ON systir, pl. systr, id.; Finn. LW sisar, id.; OCS (and com. Sl.) sestra, id.; Li. sesē, gs: sesés beside sesuó, gs: seseřs. (NB. Gk. óar, gs: óaros ap- pears to represent an o-grade variant (resul- tant aspect) of the same root)
=== ausos
11553:bour; Latv. nàve, f. ‘death’; nāvēt, inf. ‘kilľ; Li. noviju, -yti, v. (^weary': Cz. u-navit, id.). Here prob. W neu, v. ‘gasp, long for. (For Du. nauw: OE hneaw, see knouos. The com- position of Gk. bánausos *mean, vile, base' is uncertain, cf. *guas- for bá-?)
15033:sausos ‘dry, withered, mature’; sausið ‘dry, wither, mature’; sausiə ‘dryness, dry land, dried object’. WP II, 447 Skt. (variant) Sosah, adj. ‘dry’; Av. cf. hao- Səmna-, pres. pass. pt, id.; OP cf. huška-, dim. id.; Per. xušk, id.; Gk. aüos, adj. id.; aúð, v. ‘parch’; aa f. (‘dry land’: OCS suša, Cz. souš, gs: souše, id.; Li. saüse, f. (2) ‘dried- out tree’); Br. (?) haw, adj. ‘ripe’; Sicilian cf. (variant) saukos ‘dry’ (Desk: MHG sor, OE sear, siere, LG & WG sohr, Du. zoor, adj. ‘dry, barren, arid, withered, sear’; ON seyra, f. (famine’: Gk. aa OCS suša: Li. sausē); OCS (and com. Sl.) suxü, adj. ‘dry’; Li. sausas, Latv. sauss, id. Verbal types: cf. Skt. susyami, pp: Sositáh ‘get dry’; Gk. auo, id.; OE sēarian, id.; LG soren; OCS and com. Sl. sušọ, -iti, ‘dry’; Li. cf. saustü, saüsti, id.; Latv. sauseju, ét, tr. intr. ‘dry’
15316:Sousos, see sausos
17855:sus ‘dry’. Cf. sausos, susó OCS cf. sos f. 'brushwood', fr. *susio; süx- nọ, -noti, v. ‘get dry’; Latv. susu, et, v. ‘dry’; Av. hu$- (radical), id.
```


## [2026-09-05T05:31:23.657Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nfor ln in [20148,20183]:\n    leaf=t[:sum(len(l)+1 for l in lines[:ln-1])].count('\\f')\n    print('IEC line',ln,'leaf',leaf,'printed ~',(leaf-15)*2)\nEOF\necho \"=== MON bahar headword\"; grep -n \"^بهار\\|بهار:\" MON_part1.txt | head -10; echo \"=== ARY latin index vahar/bahar\"; grep -n -i \"bahar\\|vahar\\|wesr\\|ausos\" incoming/ARY/ARY_latin_index_pages.txt | head -10",
 "description": "IEC page, Mo'in bahar, Aryanpur"
}
```


### [2026-09-05T05:31:25.385Z] TOOL RESULT

```
IEC line 20148 leaf 840 printed ~ 1650
IEC line 20183 leaf 842 printed ~ 1654
=== MON bahar headword
1516:بهار» هنگام بهار» و بهاران. 
6131:بهار پدید اید. ابر آازادی: ابر بهار. 
19770:وزد» مش ای . باد بهار: 0 
19773:بهار. باد بهاری: بادی که مومع ۳ ورد. 
26303:بهار: ۰ (.) اولین فصل سال» ربیع. 
26313:بهار: ۲ (۱.) سخانه» بتگده. 
26315:بهاربند: ۰0:4 (امر.) طویلهٌ بی‌سقفی که 
26318:بهار در آن نشینند. 
26320:بهارستان: مقاو- 0۵۱8۵ [بهار + ستان. سد.] 
26324:بهاره: (6-)02081-2 (ص‌نسب. امر.) منسوب 
=== ARY latin index vahar/bahar
3924:GARUN, GARNAN (ARMENIAN) .g+,\ VANRI, VAHAR, —:(AVESTAN) (plus)
3926:VER, VERIS AALATIN) 3 -VAHARA — :(OLD RERSIAN) sku go
3927:(OLD FRENCH) oS 415 WAHAR, VAHAR — (PAHLAVI) 6 ty,
7192:SOROR LATIN) 553 XVAHAR, XVANHAR-(AVESTAN) (glo 31
7193:S@UR (FRENCH) «i\5 XVAHAR, XAH. PAHLAVI) 5 jh
7196:SWISTAR GOTHIC) 3 GVAHAR, GVAR —«(BALUCH) gx gl
```


## [2026-09-05T05:31:32.614Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '26298,26320p' MON_part1.txt; echo \"=== ARY page for line 3924\"; python3 - <<'EOF'\nimport re\np='incoming/ARY/ARY_latin_index_pages.txt'\nt=open(p,encoding='utf-8',errors='replace').read()\ni=t.find('VANRI, VAHAR')\ntags=re.findall(r'\\[pdf page (\\d+)\\]', t[:i])\nprint('pdf page',tags[-1],'printed',int(tags[-1])+1)\nprint(t[i-600:i+400])\nEOF",
 "description": "Mo'in bahar entries and Aryanpur page"
}
```


### [2026-09-05T05:31:34.057Z] TOOL RESULT

```
آرایش. عظمت؛ کمال. فر» شکوه فره. 
بهادر: ۲ اآتر.] (رص.) و دلاور» 
شجاع. 
بهار: ۰ (.) اولین فصل سال» ربیع. 
شکوفة گل هر درخت. (گیا.) گیاهی از تیه 
مرکبان که چهار گونه از آن شناخته شده, 
گل‌هاش زرد رنگ و در کوهستان‌های 
اروپای مرکزی و جنوبی و آسیای غربی و 
مرکزی می‌روید و به عنوان گل زینتی نیز در 
باغ‌ها کاشته می‌شود؛ گل گاو چشم اقحوان 
اصفر. (مس.) یکی از دستگاه‌ها و ادوار 
ملایم در موسیقی قد یم. 

بهار: ۲ (۱.) سخانه» بتگده. 

بهاربند: ۰0:4 (امر.) طویلهٌ بی‌سقفی که 
در فصل بهار و تابستان چارپایان را در آن 
بندند) باربند» باره‌بند. خانهةٌ هوادار که فصل 
بهار در آن نشینند. 

بهارستان: مقاو- 0۵۱8۵ [بهار + ستان. سد.] 
=== ARY page for line 3924
pdf page 137 printed 138

“"* VESELU VAHYA, VANGHA

VESELY (CZECH) Sy VAHYAH, «(OLD RERSIAN) lub +4,
VESELS LATVIAN) (35) 393 VAHU
FO, FEB OLD IRISH) oS 54 2\ VEH, BEH, WEH — (PAHLAVI) 5 sly
BI-, BI(JARE) :(KURDISH) 53,5
‘REFERENCES cute BEH., AFGHAN) (24), gli
POKORNY, ~~S*~*~*~C~*~S~S*~S*~«*O BEH(TAR)
BARNHART: (BENEFACTOR) 88 WSE s(TORHARIAN A) A. jis
DELAMARRE: (BON, BIEN) 237 YASI, WESD :(TOKHARIAN B) B ios
‘MACKENZIE: GETTER) io4| __-VASU, (SANSKRIT) 4 Suibe
AMINDAROV: (BETTER) 191 VASTVAN
nr seo dey FUROS (4LES(GREEK) gt»
BENE, BONUS — (4\:)(LATIN) 53
seatlooh
Pe CAE od
py ctSunr
GARUN, GARNAN (ARMENIAN) .g+,\ VANRI, VAHAR, —:(AVESTAN) (plus)
AR, EATH (GREEK) gy VAHRI, VASRI
VER, VERIS AALATIN) 3 -VAHARA — :(OLD RERSIAN) sku go
(OLD FRENCH) oS 415 WAHAR, VAHAR — (PAHLAVI) 6 ty,
PRIMEVOIRE BIHAR (KURDISH) $3, +s
PRIMAVERA SPANISH) pistol VASAR, VASAN, :(SANSKRIT) cu Site
PRIMAVERA AUTALIAN) glSte| YVASANTAS:
[pdf page 138]
wa | se
VASARA LITHUANIAN) <i} PRIMAVARA (RUMANIAN) gles)
VASARA, LATVIAN) (3) gi
```


## [2026-09-05T05:31:52.534Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n 1,60p tools/fetch_source.py",
 "description": "Read fetch_source tool"
}
```


### [2026-09-05T05:31:52.587Z] TOOL RESULT

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
    fetch_url = urllib.parse.urlunsplit((parts.scheme, parts.netloc.encode("idna").decode(),
                                         urllib.parse.quote(parts.path, safe="/%:@!$&'()*+,;="),
                                         urllib.parse.quote(parts.query, safe="=&%:/?+"), parts.fragment))
    os.makedirs(WEB, exist_ok=True)
    path = os.path.join(WEB, h + ".txt")
    if os.path.exists(path) and time.time() - os.path.getmtime(path) < 86400:
        print(path); return 0
    status, title, text = 0, "", ""
    try:
        req = urllib.request.Request(fetch_url, headers={"User-Agent": UA, "Accept-Language": "en"})
        with urllib.request.urlopen(req, timeout=60) as r:
            status = r.status
            raw = r.read(4_000_000)
            ctype = r.headers.get("Content-Type", "")
            enc = "utf-8"
            m = re.search(r"charset=([\w-]+)", ctype)
            if m: enc = m.group(1)
            body = raw.decode(enc, errors="replace")
            if "html" in ctype or body.lstrip().lower().startswith("<!doctype html") or "<html" in body[:2000].lower():
                mt = re.search(r"(?is)<title>(.*?)</title>", body)
```


## [2026-09-05T05:31:59.516Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; for u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82ews-\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/w%C3%A9sr%CC%A5\" \\\n \"https://en.wiktionary.org/wiki/%D8%A8%D9%87%D8%A7%D8%B1\" \\\n \"https://en.wiktionary.org/wiki/vihara\" \\\n \"https://www.etymonline.com/word/east\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 71, root Aus 2 / Wes 2: verify PIE dawn+spring roots, NP bahar, Skt vihara, Eng east\" ;\ndone",
 "description": "Fetch and archive web sources"
}
```


### [2026-09-05T05:32:03.182Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/6a631f970126a71c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ef3e1e5b5f985c08.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ba7c51cf6efb975f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/29b70a94d3d71ae6.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3bec3faec531d7dd.txt
```


## [2026-09-05T05:32:05.957Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; echo \"### h2ews\"; head -c 2500 6a631f970126a71c.txt; echo; echo \"### wesr\"; head -c 2500 ef3e1e5b5f985c08.txt",
 "description": "Read Wiktionary PIE pages"
}
```


### [2026-09-05T05:32:06.016Z] TOOL RESULT

```
### h2ews
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82ews-
FETCHED: 2026-09-05T05:32:01Z
STATUS: 200
TITLE: Reconstruction:Proto-Indo-European/h₂ews- - Wiktionary, the free dictionary

Reconstruction:Proto-Indo-European/h₂ews- - Wiktionary, the free dictionary 

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
 Alternative reconstructions 

 1.1.2 
 Derived terms 

 1.1.3 
 References 

 1.1.4 
 Further reading 

 1.2 
 Root 

 1.2.1 
 Derived terms 

 1.2.2 
 References 

 Toggle the table of contents 

 Reconstruction:Proto-Indo-European/ h₂ews- 

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

 *h₂ews- [ 1 ] 

 to become light 

 to dawn 

 Alternative reconstructions
 [ edit ] 

 *h₂wes- [ 2 ] [ 3 ] 

 Derived terms
 [ edit ] 

 Terms derived from the Proto-Indo-European root *h₂ews- (dawn) (174 c, 0 e) 

 *h₂us-sḱé-ti ( ske-present ) [ 2 ] [ 1 ] 
 Proto-Indo-Iranian: *Hušćáti 
 Proto-Indo-Aryan: *Huṣśáti 
 Sanskrit: उ॒च्छति॑ ( uccháti , “ to dawn ” ) 

 Proto-Iranian: 
 Younger Avestan: 𐬎𐬯𐬀𐬧𐬙 ( usaṇt , ptc.act. ) 

 *h₂wés-t ~ *h₂us-ént ( root athematic present ) [ 2 ] 
 Proto-Indo-Iranian: *HáHwast ~ *HáHusant 
 Proto-Indo-Aryan: *HáHwast ~ *HáHusant 
 Sanskrit: आवस् ( ā́vas ) , अवात् ( avāt , “ to become light ” ) 

 *h₂wos-éye-ti ( eye-causative ) [ 2 ]
### wesr
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/w%C3%A9sr%CC%A5
FETCHED: 2026-09-05T05:32:01Z
STATUS: 200
TITLE: Reconstruction:Proto-Indo-European/wósr̥ - Wiktionary, the free dictionary

Reconstruction:Proto-Indo-European/wósr̥ - Wiktionary, the free dictionary 

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
 Etymology 

 1.2 
 Noun 

 1.2.1 
 Inflection 

 1.2.2 
 Alternative reconstructions 

 1.2.3 
 Derived terms 

 1.2.4 
 Descendants 

 1.3 
 See also 

 1.4 
 References 

 Toggle the table of contents 

 Reconstruction:Proto-Indo-European/ wósr̥ 

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

 (Redirected from Reconstruction:Proto-Indo-European/wésr̥ ) 

 This Proto-Indo-European entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.

 Proto-Indo-European
 [ edit ] 

 Etymology
 [ edit ] 

 Perhaps from *h₁wes- , *h₁ews- ( “ to become warm; to burn ” ) +‎ *-r̥ ( r/n -stem noun suffix ) .

 Noun
 [ edit ] 

 *wósr̥   n ( oblique stem *wésn̥- ) [ 1 ] [ 2 ] 

 spring ( season ) 

 Inflection
 [ edit ] 

 Theoretically older acrostatic pattern:

 Athematic, acrostatic

 singular

 nominative

 *wósr̥ 

 genitive

 *wésn̥s 

 singular

 dual

 plural

 nominative

 *wósr̥ 

 —

 —

 vocative

 *wósr̥ 

 —

 —

 accusative

 *wósr̥ 

 —

 —

 genitive

 *wésn̥s 

 —

 —

 ablative

 *wésn̥s 

 —

 —

 dative

 *wésney 

 —

 —

 locative

 *wésn̥ , *wésni 

 —

 —

 instrumental

 *wésn̥h₁ 

 —

 —

 Theoretically later prot
```


## [2026-09-05T05:32:18.713Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; echo \"### wesr descendants\"; grep -n -A3 -i \"Proto-Iranian\\|Old Persian\\|Middle Persian\\|Persian:\\|Latin:\\|Armenian\" ef3e1e5b5f985c08.txt | sed -n 1,80p",
 "description": "Wiktionary wosr descendants"
}
```


### [2026-09-05T05:32:18.771Z] TOOL RESULT

```
### wesr descendants
489: Proto-Armenian: 
490: Old Armenian: գարուն ( garun ) ( see there for further descendants )
491-
492- Proto-Balto-Slavic: *was(e)r ( see there for further descendants )
493-
```


## [2026-09-05T05:32:21.390Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; sed -n '440,540p' ef3e1e5b5f985c08.txt",
 "description": "Wiktionary wosr full descendants section"
}
```


### [2026-09-05T05:32:21.440Z] TOOL RESULT

```
 *usnéy 

 locative

 *usén , *uséni 

 *? 

 *usn̥sú 

 *usén , *uséni 

 instrumental

 *usnéh₁ 

 *? 

 *usn̥mís , *usn̥bʰís 

 *usnéh₁ 

 Sihler and de Vaan reconstruct a modified amphikinetic *wesr̥ ~ *wesnos/*wesnes (without specifying accent) which keeps the root in full-grade in the weak cases . [ 3 ] [ 4 ] 

 Alternative reconstructions
 [ edit ] 

 *h₁wósr̥ 

 *h₂wósr̥ [ 1 ] 

 *wésr̥ [ 5 ] [ 3 ] [ 4 ] 

 Derived terms
 [ edit ] 

 *wésn-ont-s ~ *usn̥-n̥t-és 
 Proto-Celtic: *wesants [ 2 ] 
 Proto-Brythonic: *gwehant 
 ⇒ Proto-Brythonic: *gwehantuɨn ( see there for further descendants )

 Proto-Indo-Iranian: *wasantás 
 Proto-Indo-Aryan: *wasantás 
 Sanskrit: वसन्त ( vasantá ) 

 Descendants
 [ edit ] 

 Proto-Armenian: 
 Old Armenian: գարուն ( garun ) ( see there for further descendants )

 Proto-Balto-Slavic: *was(e)r ( see there for further descendants )

 Proto-Celtic: *wesrū 
 ⇒ Proto-Celtic: *wesrakos ( see there for further descendants )

 ⇒ ? Proto-Celtic: *wesnālā ( “ swallow (bird) ” ) ( see there for further descendants )

 Proto-Germanic: *wazrą ( see there for further descendants )

 Proto-Hellenic: *wéhər ( see there for further descendants )

 Proto-Indo-Iranian: *wásr̥ ( see there for further descendants )

 Proto-Italic: *wezor ( see there for further descendants )

 See also
 [ edit ] 

 Seasons in Proto-Indo-European · [Term?] ( layout · text ) · category 

 *wósr̥ ( “ spring ” ) 

 *semh₂- ( “ summer ” ) 

 *(s)h₁es- ( “ autumn ” ) 

 *ǵʰéyōm ( “ winter ” ) 

 References
 [ edit ] 

 ↑ 1.0 1.1 Lipp, Reiner ( 2009 ), Die indogermanischen und einzelsprachlichen Palatale im Indoiranischen: Neurekonstruktion, Nuristan-Sprachen, Genese der indoarischen Retroflexe, Indoarisch von Mitanni (Indogermanische Bibliothek; 3) (in German), volume 1, Heidelberg: Winter, page 164 : “ vor-uridg. *h₂u̯ós-r̥/ Obl. *h₂u̯és-n-/ Lok. *h₂u̯os-én bzw. *h₂u̯os-ér > uridg. *u̯ós-r (lautlich)/ Obi. *h₂u̯és-n- (lautlich) neben *u̯és-n- (analogisch)/ Lok. *u̯os-én bzw. *u̯os-ér (lautlich) ” 

 ↑ 2.0 2.1 Kroonen, Guus ( 2013 ), “*wasra- ~ *wazra-”, in Etymological Dictionary of Proto-Germanic (Leiden Indo-European Etymological Dictionary Series; 11 )‎ [1] , Leiden, Boston: Brill , →ISBN , page 575 : “ PCelt. *wesant- ” 

 ↑ 3.0 3.1 Sihler, Andrew L. ( 1995 ), New Comparative Grammar of Greek and Latin , Oxford, New York: Oxford University Press, →ISBN , page 306 : “ *wesr̥ *wesnes ” 

 ↑ 4.0 4.1 De Vaan, Michiel ( 2008 ), “ vēr ”, in Etymological Dictionary of Latin and the other Italic Languages (Leiden Indo-European Etymological Dictionary Series; 7), Leiden, Boston: Brill, →ISBN , pages 663–664 : “ *u̯esr, *u̯esnos ” 

 ^ Pokorny, Julius ( 1959 ), “ u̯es- ”, in Indogermanisches etymologisches Wörterbuch [ Indo-European Etymological Dictionary ] (in German), Bern, München: Francke Verlag: “ *u̯esr- ” 

 Retrieved from " https://en.wiktionary.org/w/index.php?title=Reconstruction:Proto-Indo-European/wósr̥&oldid=92151891 "

 Categories : Proto-Indo-European terms belonging to the root *h₁ews- 
 Proto-Indo-European terms suffixed with *-r̥ 
 Proto-Indo-European terms prefixed with *h₁ews- 
 Proto-Indo-European lemmas 
 Proto-Indo-European nouns 
 Proto-Indo-European neuter nouns
```


## [2026-09-05T05:32:30.217Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; python3 - <<'EOF'\nt=open('ba7c51cf6efb975f.txt',encoding='utf-8').read()\ni=t.find('Persian')\n# print sections\nimport re\nj=t.find('From Wiktionary')\nprint(t[j:j+6000])\nEOF",
 "description": "Read Wiktionary bahar page"
}
```


### [2026-09-05T05:32:31.831Z] TOOL RESULT

```
From Wiktionary, the free dictionary

 See also: بہار , تہار , and پہاڑ 

 Arabic
 [ edit ] 

 Etymology 1
 [ edit ] 

 Derived from Classical Persian بهار ( bahār ) in the sense of blossoms and foliage, as a great many spices are cultivated from the leaves of various plants and herbs.

 Pronunciation
 [ edit ] 

 IPA ( key ) : /ba.haːr/ 

 Noun
 [ edit ] 

 بَهَار • ( bahār )  m ( plural بَهَارَات ( bahārāt ) ) 

 oxeye ( Buphthalmum spp.)
 Synonyms: عَرَار ( ʕarār ) , عَيْن الْبَقَر ( ʕayn al-baqar ) , رَبْد ( rabd ) 

 spice , seasoning 
 Synonyms: تَابِل ( tābil ) , أَبْزَار ( ʔabzār ) , أَفَاوِيه ( ʔafāwīh ) 

 Declension
 [ edit ] 

 Declension of noun بَهَار ( bahār )

 singular

 basic singular triptote 

 indefinite

 definite

 construct

 informal

 بَهَار 
 bahār 

 الْبَهَار 
 al-bahār 

 بَهَار 
 bahār 

 nominative

 بَهَارٌ 
 bahārun 

 الْبَهَارُ 
 al-bahāru 

 بَهَارُ 
 bahāru 

 accusative

 بَهَارًا 
 bahāran 

 الْبَهَارَ 
 al-bahāra 

 بَهَارَ 
 bahāra 

 genitive

 بَهَارٍ 
 bahārin 

 الْبَهَارِ 
 al-bahāri 

 بَهَارِ 
 bahāri 

 dual

 indefinite

 definite

 construct

 informal

 بَهَارَيْن 
 bahārayn 

 الْبَهَارَيْن 
 al-bahārayn 

 بَهَارَيْ 
 bahāray 

 nominative

 بَهَارَانِ 
 bahārāni 

 الْبَهَارَانِ 
 al-bahārāni 

 بَهَارَا 
 bahārā 

 accusative

 بَهَارَيْنِ 
 bahārayni 

 الْبَهَارَيْنِ 
 al-bahārayni 

 بَهَارَيْ 
 bahāray 

 genitive

 بَهَارَيْنِ 
 bahārayni 

 الْبَهَارَيْنِ 
 al-bahārayni 

 بَهَارَيْ 
 bahāray 

 plural

 sound feminine plural

 indefinite

 definite

 construct

 informal

 بَهَارَات 
 bahārāt 

 الْبَهَارَات 
 al-bahārāt 

 بَهَارَات 
 bahārāt 

 nominative

 بَهَارَاتٌ 
 bahārātun 

 الْبَهَارَاتُ 
 al-bahārātu 

 بَهَارَاتُ 
 bahārātu 

 accusative

 بَهَارَاتٍ 
 bahārātin 

 الْبَهَارَاتِ 
 al-bahārāti 

 بَهَارَاتِ 
 bahārāti 

 genitive

 بَهَارَاتٍ 
 bahārātin 

 الْبَهَارَاتِ 
 al-bahārāti 

 بَهَارَاتِ 
 bahārāti 

 Derived terms
 [ edit ] 

 بَهَار حُلْو ( bahār ḥulw , “ allspice ” ) 

 Descendants
 [ edit ] 

 Gulf Arabic: بهار ( bhār ) 

 → Ottoman Turkish: بهار ( bahar ) , պահար ( bahar ) — Armeno-Turkish Turkish: bahar 
 → Armenian: պահար ( pahar ) 
 → Bulgarian: баха́р ( bahár ) 
 → Georgian: ბაჰარი ( bahari ) 
 → Greek: μπαχάρι ( bachári ) 
 → Laz: ბეჲარი ( beyari ) 
 → Macedonian: бахар ( bahar ) 
 → Serbo-Croatian: Cyrillic script: бѐха̄р Latin script: bèhār 
 → Crimean Tatar: baar 

 ( via plural form بَهَارَات ( bahārāt ) ) :

 → English: baharat 

 → Turkish: baharat 

 Etymology 2
 [ edit ] 

 Borrowed from Urdu بھار ( bhār ) / Hindi भार ( bhār ) .

 Pronunciation
 [ edit ] 

 IPA ( key ) : /bu.haːr/ , ( colloquial ) /ba.haːr/ 

 Noun
 [ edit ] 

 بُهَار • ( buhār )  m ( plural بُهَارَات ( buhārāt ) ) ( obsolete ) 

 a dry measure (clarification of this definition is needed) 

 a container of such a measure , a bag 

 a weight measure varying according to place about 200 kilograms 

 Declension
 [ edit ] 

 Declension of noun بُهَار ( buhār )

 singular

 basic singular triptote 

 indefinite

 definite

 construct

 informal

 بُهَار 
 buhār 

 الْبُهَار 
 al-buhār 

 بُهَار 
 buhār 

 nominative

 بُهَارٌ 
 buhārun 

 الْبُهَارُ 
 al-buhāru 

 بُهَارُ 
 buhāru 

 accusative

 بُهَارًا 
 buhāran 

 الْبُهَارَ 
 al-buhāra 

 بُهَارَ 
 buhāra 

 genitive

 بُهَارٍ 
 buhārin 

 الْبُهَارِ 
 al-buhāri 

 بُهَارِ 
 buhāri 

 dual

 indefinite

 definite

 construct

 informal

 بُهَارَيْن 
 buhārayn 

 الْبُهَارَيْن 
 al-buhārayn 

 بُهَارَيْ 
 buhāray 

 nominative

 بُهَارَانِ 
 buhārāni 

 الْبُهَارَانِ 
 al-buhārāni 

 بُهَارَا 
 buhārā 

 accusative

 بُهَارَيْنِ 
 buhārayni 

 الْبُهَارَيْنِ 
 al-buhārayni 

 بُهَارَيْ 
 buhāray 

 genitive

 بُهَارَيْنِ 
 buhārayni 

 الْبُهَارَيْنِ 
 al-buhārayni 

 بُهَارَيْ 
 buhāray 

 plural

 sound feminine plural

 indefinite

 definite

 construct

 informal

 بُهَارَات 
 buhārāt 

 الْبُهَارَات 
 al-buhārāt 

 بُهَارَات 
 buhārāt 

 nominative

 بُهَارَاتٌ 
 buhārātun 

 الْبُهَارَاتُ 
 al-buhārātu 

 بُهَارَاتُ 
 buhārātu 

 accusative

 بُهَارَاتٍ 
 buhārātin 

 الْبُهَارَاتِ 
 al-buhārāti 

 بُهَارَاتِ 
 buhārāti 

 genitive

 بُهَارَاتٍ 
 buhārātin 

 الْبُهَارَاتِ 
 al-buhārāti 

 بُهَارَاتِ 
 buhārāti 

 Descendants
 [ edit ] 

 → English: bahar 

 References
 [ edit ] 

 Dozy, Reinhart Pieter Anne ( 1881 ), “ بهار ”, in Supplément aux dictionnaires arabes ‎ [1] (in French), volume 1, Leiden: E. J. Brill, page 121 

 Fraenkel, Siegmund ( 1886 ), Die aramäischen Fremdwörter im Arabischen (in German), Leiden: E. J. Brill, page 203 

 Lane, Edward William ( 1863-1893 ), “ بهار ”, in Arabic-English Lexicon , London: Williams & Norgate, page 266 . 

 Gulf Arabic
 [ edit ] 

 Etymology
 [ edit ] 

 From Arabic بَهَار ( bahār ) , from Classical Persian بهار ( bahār ) .

 Pronunciation
 [ edit ] 

 ( Kuwait ) IPA ( key ) : /bhɑːr/ 

 Noun
 [ edit ] 

 بْهار • ( bhār ) ( dual بْهارين ( bhārēn ) , plural بْهارات ( bhārāt ) ) 

 spice , seasoning 

 Hijazi Arabic
 [ edit ] 

 Etymology
 [ edit ] 

 From Arabic بَهَار ( bahār ) , from Classical Persian بهار ( bahār ) .

 Pronunciation
 [ edit ] 

 IPA ( key ) : /ba.haːr/ 

 Noun
 [ edit ] 

 بهار • ( bahār )  m ( plural بهارات ( bahārāt ) ) 

 spice 

 Ottoman Turkish
 [ edit ] 

 Alternative forms
 [ edit ] 

 պահար ( bahar ) — Armeno-Turkish 

 Etymology 1
 [ edit ] 

 Borrowed from Persian بهار ( bahâr ) .

 Noun
 [ edit ] 

 بهار • ( bahar ) 

 blossom 

 verdure 

 foliage 

 spring , the season

 Declension
 [ edit ] 

 Declension of بهار ( bahar ) 

 singular

 plural

 nominative

 بهار ( bahar ) 

 بهارلر ( baharlar ) 

 definite accusative

 بهاری ( baharı ) 

 بهارلری ( baharları ) 

 dative

 بهاره ( bahara ) 

 بهارلره ( baharlara ) 

 locative

 بهارده ( baharda ) 

 بهارلرده ( baharlarda ) 

 ablative

 بهاردن ( bahardan ) 

 بهارلردن ( baharlardan ) 

 genitive

 بهارك ( baharıñ ) 

 بهارلرك ( baharlarıñ ) 

 Possessive forms

 1st person singular

 singular

 plural

 nominative

 بهارم ( baharım
```


## [2026-09-05T05:32:36.220Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; grep -n -i \"wahār\\|Middle Persian\\|Proto-Iranian\\|vihāra\\|vihara\" ba7c51cf6efb975f.txt | head -30",
 "description": "Persian bahar etymology on Wiktionary"
}
```


### [2026-09-05T05:32:36.276Z] TOOL RESULT

```
1177: From Middle Persian whʾl ( wahār ) , from Old Persian 𐎺𐎠𐏃𐎼 ( v-a-h-r ) , from Proto-Iranian *wáhār , collective of *wáhr̥ , from Proto-Indo-Iranian *wásr̥ , ultimately from Proto-Indo-European *wósr̥ ( “ spring ” ) . [ 1 ] 
1292: a female given name , Bahar , from Middle Persian 
1393: Persian terms inherited from Middle Persian 
1394: Persian terms derived from Middle Persian 
1397: Persian terms inherited from Proto-Iranian 
1398: Persian terms derived from Proto-Iranian 
1412: Persian female given names from Middle Persian
```


## [2026-09-05T05:32:44.566Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; sed -n '1170,1290p' ba7c51cf6efb975f.txt | grep -v \"^ *$\" | head -60",
 "description": "Persian bahar senses"
}
```


### [2026-09-05T05:32:46.094Z] TOOL RESULT

```
 [ edit ] 
 باهار ( bâhâr ) 
 Etymology
 [ edit ] 
 From Middle Persian whʾl ( wahār ) , from Old Persian 𐎺𐎠𐏃𐎼 ( v-a-h-r ) , from Proto-Iranian *wáhār , collective of *wáhr̥ , from Proto-Indo-Iranian *wásr̥ , ultimately from Proto-Indo-European *wósr̥ ( “ spring ” ) . [ 1 ] 
 Cognate with Mazanderani وهار ( vehār ) , Talysh اوسور ( əvəsor ) , Laki وهار ( whar ) , Zazaki wesar , Central Kurdish بەھار ( behar ) .
Other cognates include Sanskrit वसन्त ( vasanta ) , Old Armenian գարուն ( garun ) , Latin ver , Ancient Greek ἔαρ ( éar ) , Old Church Slavonic весна ( vesna ) , Lithuanian vãsara , Old Norse vár .
 Pronunciation
 [ edit ] 
 ( Classical Persian ) IPA ( key ) : /ba.ˈhaːr/ 
 ( Dari, formal ) IPA ( key ) : [bä.ɦɑ́ːɾ] 
 ( Dari, formal ) IPA ( key ) : [bä.ɦɑ́ːɾ] 
 ( Kabuli ) IPA ( key ) : [bɑːɑ́ːɾ] 
 ( Hazaragi ) IPA ( key ) : [bɔːɔ́ːɾ] 
 ( Iran, formal ) IPA ( key ) : [bæ.ɦɒ́ːɹ] 
 ( Tajik, formal ) IPA ( key ) : [bä.ɦɔ́ɾ] 
 Rhymes: -aːr 
 Readings
 Classical reading ? 
 bahār
 Dari reading ? 
 bahār
 Iranian reading ? 
 bahâr
 Tajik reading ? 
 bahor
 Noun
 [ edit ] 
 بهار • ( bahār / bahâr ) ( Tajik spelling баҳор ) 
 spring ( season ) 
 blossom 
 Related terms
 [ edit ] 
 بهاری ( bahâri ) 
 بهاره ( bahâre ) 
 بهاران ( bahârân ) 
 بهارستان ( bahârestân ) 
 Descendants
 [ edit ] 
 → Armenian: բահար ( bahar ) 
 → Assyrian Neo-Aramaic: ܒܲܗܵܪ ( bahār ) 
 → Azerbaijani: bahar 
 → Bengali: বাহার ( bahar ) 
 → Chagatai: بهار ( bhʾr /⁠bähār⁠/ ) 
 Uyghur: باھار ( bahar ) 
 Uzbek: bahor 
 → Classical Mandaic: ࡁࡄࡀࡓ ( bhar ) 
 → Hindustani: 
 Hindi: बहार ( bahār ) 
 Urdu: بہار ( bahār ) 
 → Ottoman Turkish: بهار ( bahar ) , պահար ( bahar ) — Armeno-Turkish Turkish: bahar 
 → Armenian: պահար ( pahar ) 
 → Bulgarian: баха́р ( bahár ) 
 → Georgian: ბაჰარი ( bahari ) 
 → Greek: μπαχάρι ( bachári ) 
 → Laz: ბეჲარი ( beyari ) 
 → Macedonian: бахар ( bahar ) 
 → Serbo-Croatian: Cyrillic script: бѐха̄р Latin script: bèhār 
 → Crimean Tatar: baar 
 → Punjabi: ਬਹਾਰ ( bahār )
```


## [2026-09-05T05:32:46.215Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; echo \"### vihara\"; grep -n -i \"vihāra\\|Etymology\" 29b70a94d3d71ae6.txt | head -20; echo \"### etymonline east\"; grep -n -i \"east\\b\" 3bec3faec531d7dd.txt | head -10",
 "description": "Vihara and etymonline"
}
```


### [2026-09-05T05:32:46.294Z] TOOL RESULT

```
### vihara
62: Etymology 
79: Etymology 
165: See also: vihāra 
170: Etymology
195: Etymology
### etymonline east
1:URL: https://www.etymonline.com/word/east
4:TITLE: East - Etymology, Origin & Meaning
6:East - Etymology, Origin & Meaning 
21: Origin and history of east 
23: east 
25: Old English east , eastan (adj., adv.) "east, easterly, eastward;" easte (n.), from Proto-Germanic *aust- "east," literally "toward the sunrise" (source also of Old Frisian ast "east," aster "eastward," Dutch oost Old Saxon ost , Old High German ostan , German Ost , Old Norse austr "from the east"), from PIE root *aus- (1) "to shine," especially of the dawn. The east is the direction in which dawn breaks. For theory of shift in the geographical sense in Latin, see austral .
27: As one of the four cardinal points of the compass, from c. 1200. Meaning "the eastern part of the world" (from Europe) is from c. 1300. Cold War use of East for "communist states" first recorded 1951. French est , Spanish este are borrowings from Middle English, originally nautical. The east wind in Biblical Palestine was scorching and destructive (as in Ezekiel xvii.10); in New England it is bleak, wet, unhealthful. East End of London so called by 1846; East Side of Manhattan so called from 1871; East Indies (India and Southeast Asia) so called 1590s to distinguish them from the West Indies .
29: Entries linking to east 
35: The Latin sense shift in auster , if it is indeed the same word other Indo-European languages use for "east," for which Latin uses oriens (see Orient (n.)), perhaps is based on a false assumption about the orientation of the Italian peninsula, "with shift through 'southeast' explained by the diagonal position of the axis of Italy" [Buck]; see Walde, Alois, "Lateinisches etymologisches Wörterbuch," 3rd. ed., vol. I, p.87; Ernout, Alfred, and Meillet, Alfred, "Dictionnaire étymologique de la langue latine," 2nd. ed., p.94.
41: Old English easterne "of the east, from the east; oriental; of the Eastern Orthodox Church; of the eastern part of the globe," from east + -erne , suffix denoting direction. Cognate with Old Saxon ostroni , Old High German ostroni , Old Norse austroenn . Eastern Shore of Maryland and Virginia so called from 1620s.
```


## [2026-09-05T05:32:54.385Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; for u in \\\n \"https://www.etymonline.com/word/Easter\" \\\n \"https://www.etymonline.com/word/Austria\" \\\n \"https://www.etymonline.com/word/aurora\" \\\n \"https://www.etymonline.com/word/vernal\" \\\n \"https://en.wiktionary.org/wiki/%D9%81%D8%B1%D8%AE%D8%A7%D8%B1\" \\\n \"https://en.wiktionary.org/wiki/%E0%A4%B5%E0%A4%BF%E0%A4%B9%E0%A4%BE%E0%A4%B0\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 71 Aus 2: Easter/Austria/aurora/vernal chains; Persian farxar; Sanskrit vihara\" ;\ndone",
 "description": "Fetch more web sources"
}
```


### [2026-09-05T05:32:58.469Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/19e39f1e2d04c7d6.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/2667ebf75a7b2580.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/86808fd68ee78884.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4f84f4e4e2922b02.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a5327768483f5d81.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/119d6a7f1cc7ea6c.txt
```


## [2026-09-05T05:33:02.054Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; for f in 19e39f1e2d04c7d6 2667ebf75a7b2580 86808fd68ee78884 4f84f4e4e2922b02; do echo \"##### $f\"; sed -n '20,32p' $f.txt | grep -v \"^ *$\" | head -8; done",
 "description": "Read etymonline entries"
}
```


## [2026-09-05T05:33:03.371Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; echo \"### farxar\"; grep -n -i -A6 \"Etymology\" a5327768483f5d81.txt | grep -v \"^ *$\" | head -30; echo \"### vihara skt\"; grep -n -i -B2 -A8 \"Sanskrit\" 119d6a7f1cc7ea6c.txt | grep -v \"^ *$\" | head -40",
 "description": "Wiktionary farxar and vihara"
}
```


### [2026-09-05T05:33:03.533Z] TOOL RESULT

```
##### 19e39f1e2d04c7d6
 Origin and history of Easter 
 Easter (n.) 
 Old English Easterdæg , "Easter day," from Eastre (Northumbrian Eostre ), from Proto-Germanic *austron- , "dawn," also possibly the name of a goddess whose feast was celebrated in Eastermonað (the Anglo-Saxon month corresponding with April ), from *aust- "east, toward the sunrise" (compare east), from PIE root *aus- (1) "to shine," especially of the dawn.
 Bede writes that Anglo-Saxon Christians adopted her name for their Mass of Christ's resurrection. Almost all neighboring languages use a variant of Latin Pascha to name this holiday (see paschal ).
 Easter egg is attested by 1825, earlier pace egg (1610s). Easter bunny is attested by 1904 in children's lessons; Easter rabbit is by 1888; the paganish customs of Easter seem to have grown popular c. 1900; before that they were limited to German immigrants.
 If the children have no garden, they make nests in the wood-shed, barn, or house. They gather colored flowers for the rabbit to eat, that it may lay colored eggs. If there be a garden, the eggs are hidden singly in the green grass, box-wood, or elsewhere. On Easter Sunday morning they whistle for the rabbit, and the children imagine that they see him jump the fence. After church, on Easter Sunday morning, they hunt the eggs, and in the afternoon the boys go out in the meadows and crack eggs or play with them like marbles. Or sometimes children are invited to a neighbor's to hunt eggs. [Phebe Earle Gibbons, "Pennsylvania Dutch," Philadelphia, 1882]
##### 2667ebf75a7b2580
 Origin and history of Austria 
 Austria 
 central European nation, from Medieval Latin Marchia austriaca "eastern borderland." German Österreich is "eastern kingdom," from Old High German ostar "eastern" (from Proto-Germanic *aust- "east," literally "toward the sunrise," from PIE root *aus- (1) "to shine," especially of the dawn) + reich "kingdom, realm, state" (from Proto-Germanic *rikja "rule," from PIE root *reg- "move in a straight line," with derivatives meaning "to direct in a straight line," thus "to lead, rule"). So called for being on the eastern edge of Charlemagne's empire. Related: Austrian .
 Entries linking to Austria 
 *aus- (1) 
 Proto-Indo-European root meaning "to shine," especially of the dawn. It might form all or part of: austral ; Australia ; Austria ; Austro- ; Aurora ; east ; Easter ; eastern ; eo- ; Ostrogoth .
##### 86808fd68ee78884
 Origin and history of aurora 
 aurora (n.) 
 "morning light, dawn," late 14c., from Latin Aurora , the Roman goddess of dawn, from PIE *ausus- "dawn," also the name of the Indo-European goddess of the dawn, from root *aus- (1) "to shine," especially of the dawn (source also of Greek ēōs "dawn").
 also from late 14c. 
 Entries linking to aurora 
 aurora borealis (n.) 
 1620s, "Northern Lights," literally "northern dawn," said to have been coined by French philosopher Petrus Gassendus (1592-1655) after a spectacular display seen in France Sept. 2, 1621; see aurora + boreal . In northern Scotland and among sailors, sometimes called the dancers, pretty dancers , or merry dancers . Related: Aurora australis (1741).
##### 4f84f4e4e2922b02
 Origin and history of vernal 
 vernal (adj.) 
 "of, pertaining to, or occurring in springtime," 1530s, from Late Latin vernalis "of the spring," from vernus "of spring," from Latin ver "the spring, spring-time."
 This is reconstructed to be from PIE *wesr- "the spring" (source also of Old Norse var "spring," Greek ear , Armenian gar-un , Sanskrit vasantah , Persian bahar , Old Church Slavonic vesna "spring," Lithuanian vasara "summer").
 Also "of or belonging to youth" as the springtime of life (by 1790).
 also from 1530s 
 Entries linking to vernal
```


### [2026-09-05T05:33:05.019Z] TOOL RESULT

```
### farxar
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Proper noun 
--
142: Etymology
143- [ edit ] 
144-
145- Borrowed from Sogdian [Term?] ( /⁠βṛγʾr⁠/ , “ Buddhist temple ” ) , from Sanskrit विहार ( vihāra , “ Buddhist temple ” ) .
146-
147- Pronunciation
148- [ edit ] 
### vihara skt
69-
70- 2 
71: Sanskrit 
72-
73: Toggle Sanskrit subsection 
74-
75- 2.1 
76- Alternative scripts 
77-
78- 2.2 
79- Etymology 
80-
81- 2.3 
--
198- Vocative (calling) विहार ( vihāra ) विहारा ( vihārā ) 
199-
200: Sanskrit
201- [ edit ] 
202-
203- Alternative scripts
204- [ edit ] 
205-
206- Alternative scripts
207- ৱিহাৰ ( Assamese script ) 
208- ᬯᬶᬳᬵᬭ ( Balinese script ) 
--
394- [ edit ] 
395-
396: Monier Williams ( 1899 ), “ विहार ”, in A Sanskrit–English Dictionary,   [ … ] , new edition, Oxford: At the Clarendon Press , →OCLC , page 1003 , column 3. 
397-
398- Retrieved from " https://en.wiktionary.org/w/index.php?title=विहार&oldid=91925305 "
399-
400- Categories : Pali lemmas 
401- Pali nouns 
402- Pali nouns in Devanagari script 
403- Pali masculine nouns 
404: Sanskrit terms prefixed with वि- 
405: Sanskrit lemmas 
406: Sanskrit nouns 
407: Sanskrit nouns in Devanagari script
```


## [2026-09-05T05:33:11.004Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; sed -n '209,250p' 119d6a7f1cc7ea6c.txt | grep -v \"^ *$\" | head -25",
 "description": "Sanskrit vihara etymology"
}
```


### [2026-09-05T05:33:12.982Z] TOOL RESULT

```
 বিহার ( Bengali script ) 
 𑰪𑰰𑰮𑰯𑰨 ( Bhaiksuki script ) 
 𑀯𑀺𑀳𑀸𑀭 ( Brahmi script ) 
 ဝိဟာရ ( Burmese script ) 
 વિહાર ( Gujarati script ) 
 ਵਿਹਾਰ ( Gurmukhi script ) 
 𑌵𑌿𑌹𑌾𑌰 ( Grantha script ) 
 ꦮꦶꦲꦴꦫ ( Javanese script ) 
 𑂫𑂱𑂯𑂰𑂩 ( Kaithi script ) 
 ವಿಹಾರ ( Kannada script ) 
 វិហារ ( Khmer script ) 
 ວິຫາຣ ( Lao script ) 
 വിഹാര ( Malayalam script ) 
 ᠸᡳᡥᠠ᠎᠊ᠠᡵᠠ ( Manchu script ) 
 𑘪𑘱𑘮𑘰𑘨 ( Modi script ) 
 ᠸᠢᠾᠠᢗᠷᠠ᠋ ( Mongolian script ) 
 𑧊𑧒𑧎𑧑𑧈 ( Nandinagari script ) 
 𑐰𑐶𑐴𑐵𑐬 ( Newa script ) 
 ଵିହାର ( Odia script ) 
 ꢮꢶꢲꢵꢬ ( Saurashtra script ) 
 𑆮𑆴𑆲𑆳𑆫 ( Sharada script ) 
 𑖪𑖰𑖮𑖯𑖨 ( Siddham script ) 
 විහාර ( Sinhalese script ) 
 𑩾𑩑𑪂𑩛𑩼 ( Soyombo script ) 
 𑚦𑚮𑚩𑚭𑚤 ( Takri script )
```


## [2026-09-05T05:33:15.826Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; awk 'NR>250 && NR<400' 119d6a7f1cc7ea6c.txt | grep -v \"^ *$\" | sed -n 1,40p",
 "description": "Vihara Sanskrit noun section"
}
```


### [2026-09-05T05:33:17.798Z] TOOL RESULT

```
 distribution , transposition (of words)
 arrangement or disposition (of the 3 sacred fires; also applied to the fires themselves or the space between them)
 too great expansion of the organs of speech (consisting in too great lengthening or drawling in pronunciation, as opposed to संहार ( saṃ-hāra ) )
 walking for pleasure or amusement, wandering , roaming 
 sport , play , pastime , diversion , enjoyment , pleasure ("in" or "with" compound; at the end of a compound also = "taking delight in")
 a place of recreation, pleasure-ground
 ( Buddhism , Jainism ) vihara , a monastery or temple (originally a hall where the monks met or walked about; afterwards these halls were used as temples)
 consecration for a sacrifice
 name of the country of मगध ( magadha ) (called Bihar or Behar from the number of Buddhist monasteries)
 shoulder 
 a particular bird (= बिन्दुरेकक ( bindurekaka ) )
 = वैजयन्त ( vaijayanta ) 
 a grazing-ground, pasturage 
 ( at the end of a compound ) delighting in
 Declension
 [ edit ] 
 Masculine a-stem declension of विहार 
 singular
 dual
 plural
 nominative
 विहारः ( vihāraḥ ) 
 विहारौ ( vihārau ) 
 विहारा¹ ( vihārā¹ ) 
 विहाराः ( vihārāḥ ) 
 विहारासः¹ ( vihārāsaḥ¹ ) 
 accusative
 विहारम् ( vihāram ) 
 विहारौ ( vihārau ) 
 विहारा¹ ( vihārā¹ ) 
 विहारान् ( vihārān ) 
 instrumental
 विहारेण ( vihāreṇa ) 
 विहाराभ्याम् ( vihārābhyām ) 
 विहारैः ( vihāraiḥ ) 
 विहारेभिः¹ ( vihārebhiḥ¹ ) 
 dative
 विहाराय ( vihārāya ) 
 विहाराभ्याम् ( vihārābhyām ) 
 विहारेभ्यः ( vihārebhyaḥ )
```


## [2026-09-05T05:33:28.974Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== HUB 243\"; grep -n \"^ *243\\.\\|behär\\|Frühling\" HUB.txt | head -10; echo \"=== BQT v4 hushbam\"; grep -n \"هوشبام\\|هوش‌بام\" incoming/BQT/BQT_v4_pages.txt incoming/BQT/BQT_v5_pages.txt 2>/dev/null | head -10; echo \"=== FSF hushbam\"; grep -n \"هوشبام\" FSF_pages.txt | head -5",
 "description": "Hübschmann and Borhan hushbam"
}
```


### [2026-09-05T05:33:29.315Z] TOOL RESULT

```
=== HUB 243
1062:243. Vgl. Nr. 501.
=== BQT v4 hushbam
=== FSF hushbam
```


## [2026-09-05T05:33:35.809Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '1055,1070p' HUB.txt; echo \"=== no 501\"; grep -n \"^ *501\\.\" HUB.txt | head -3",
 "description": "Hübschmann context"
}
```


### [2026-09-05T05:33:35.997Z] TOOL RESULT

```
s. Nr. 219). Daher braucht haJia *Wert' = paz. vahd
Shk. 270 = phi. vahak nicht auf ein idg. ^vesdkO"'^
zuriickgefiihrt, sondern kann = ap.*e?aAa- gesetzt werden
(vgl. np. bCLzU 'Arm', arm. LW. bazuk, also arsacid. phi.
= *bdzuk == zd. bazU'y skr. bdhu- etc.). Ich stelle also
np. bah-a, phi. vah-dk zu skr. vas-na-, Im Uebrigen
hatte der Hinweis auf Solmsen, KZ. 29, 81 genugt.
243. Vgl. Nr. 501.
244. Np. bahdna Torwand' kann weder = skr. apidhdna-
fBedeckung, Hiille, Decke* — Darmesteter) noch =
skr. upadhdna- ^Deckel' etc. (vgl. upadhd- *Betrug' —
Horn, KZ. 32, 588) gesetzt werden, wie das Pehlevi
zeigt. Skr. vidhdna- 'Ordnung etc passt wegen der
Bedeutung gar nicht und soUte np. *bihan oder *guh(ln
lauten. Das Wort geht iiber paz. vahana = vahdn
*cause' Shk. 270 (vgl. avahdn without a cause' Shk.) =
=== no 501
1961:501. Np. x^ahar Schwester aus ^jf'ahar, vgl. skr. ace.
```


## [2026-09-05T05:33:39.322Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 tools/fetch_source.py \"https://abadis.ir/fatofa/%D9%87%D9%88%D8%B4%D8%A8%D8%A7%D9%85/\" --note \"page 71 node 3: Persian هوشبام gloss and etymology (Dehkhoda/Moein)\" && grep -n -i -m 40 \"هوشبام\\|هوش\" data/verification/sources/web/$(python3 -c \"\nimport hashlib;print(hashlib.sha1('https://abadis.ir/fatofa/%D9%87%D9%88%D8%B4%D8%A8%D8%A7%D9%85/'.encode()).hexdigest()[:16])\").txt | head -30",
 "description": "Fetch abadis for hushbam"
}
```


### [2026-09-05T05:33:42.696Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/ceaf725535fa7d45.txt
4:TITLE: هوشبام - معنی در دیکشنری آبادیس
6:هوشبام - معنی در دیکشنری آبادیس 
10: هوشبام
14: اوشا، اوشَه ( uaah ) ، اوشاه ( usha ) ، اُشَهین، اُشَهن ( اوشَهینا، ushahina ) ، هوشبام ( اوشبامه، hošbama ) - 
33:اوشا، هوشبام - نام دخترانه، واژه اوستایی
```


## [2026-09-05T05:33:49.977Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; sed -n '8,60p' ceaf725535fa7d45.txt | grep -v \"^ *$\" | head -30",
 "description": "Read abadis hushbam"
}
```


### [2026-09-05T05:33:51.596Z] TOOL RESULT

```
 دیکشنری مترجم بپرس 
 هوشبام
 پیشنهاد کاربران
 اوشا، اوشَه ( uaah ) ، اوشاه ( usha ) ، اُشَهین، اُشَهن ( اوشَهینا، ushahina ) ، هوشبام ( اوشبامه، hošbama ) - 
نام دخترانه، واژه اوستایی
از نیمه شب تا برآمدن خورشید ( آفتاب ) !
در اوستا: اوخشَن ( uxšan ) ، اوشنگهه ( ushanh ) 
 ... [مشاهده متن کامل] 
به مانند: اوخشنانو اَسنام >>> بامداد روز
 ( ( روز: اوستا: اَسَن ( asn ) ، اَزَن ( azan ) ) ) 
در ساسنکریت و وِدا: اوشاس ( uaas ) 
در رومی: آرُورا ( aurora ) 
در یونانی: اِئوس ( eōs ) 
در هند و اروپایی: زوریا، زارا، زاریا ( zara ) 
اوشا در اوستا پنج همکار دارد:
1. برِجیَه: برنج - ایزد نگهبان غلات و حبوبات
2. نَمانَه: خانه - فرشته نگهبان خانه و کاشانه
3. سُروش ( سُر ئوشه، سُر یوشه، بادران ) : پیروی و فرمانبرداری از اهورامزدا، نیوش و پیک ایزدی ( الهی ) - ایزد پیام آور و نگهبان عهد و پیمان
4. رَشن ( رَشنو ) : دادگری، حق سِتانی، عادل بودن - ایزد عدالت و دادگری و نگهبان بی گناهان
5. اَشتاد ( اَرَشتات، اَرَشتی ) : پیشوا و راهنمای مینویان و جهانیان - ایزدبانو برآوردن خواسته ها، حاجت ها و نیازها و نگهبان بلاگردان و صدقه دهندگی 
معنی: سپیده دم، پگاه، بامداد، صبح، باکِر، سحرگاه، خروس خوان! - 
اگر به معنای مجازی بکار رود:
اوشا، هوشبام - نام دخترانه، واژه اوستایی
خوش عهد و پیمان ( خوش قول ) ، با وفا، وفادار، راستگو ( راستین ) ، پاکدِل، درستکار، اَشامند! - 
با اصل و نسب، نیک مَنِش، ریشه دار، تبارمند، شریف، نجیب، شرافتمند، پاک نژاد، سِپَنتا، بزرگوار، مناعت طبع، بلندنظر، بزرگ منش ( فرانسوی: لِیدی ) 
خوشگوار، روان آرام و خوش داشتن، نیک کردار، خوش برخورد، گُشاده رو، دوست داشتنی، خواستنی، کاریزما دار!
 منابع • http://www.avesta.org/ka/ka_tc.htm • http://www.avesta.org/ka/gahs.htm#g5 • http://www.avesta.org/ka/ka_part1.htm#hb 
 + عکس و لینک 
 دیکشنری آبادیس
 آبادیس از سال 1385 فعالیت خود را در زمینه فن آوری اطلاعات آغاز کرد. نخستین پروژه آبادیس، سایت دیکشنری آبادیس بود. دیکشنری آنلاین آبادیس از ابتدا تاکنون تغییرات بسیاری کرده و ویژگی های مختلفی به آن اضافه شده است. آبادیس افزونه ای کاربردی برای مرورگرهای فایرفاکس و کروم و اپلیکیشن موبایل طراحی کرده است که میتوانید از لینک های بالا دانلود کنید. دیکشنری آبادیس شامل بخش هایی نظیر دیکشنری به زبان های مختلف از جمله انگلیسی، فارسی، عربی و همچنین بیست دیکشنری تخصصی با تلفظ انگلیسی و آمریکایی، ترجمه مخفف و کلمات اختصاری، مترجم آنلاین متن، لغتنامه دهخدا، فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راهنمای انتخاب اسم و ... می باشد.
```


## [2026-09-05T05:34:05.474Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"هوش\" incoming/BQT/BQT_v4_pages.txt | grep -n \"بامداد\\|صبح\\|سپیده\" | head -10; echo \"=== v5\"; grep -n \"هوش\" incoming/BQT/BQT_v5_pages.txt | grep \"بامداد\\|صبح\" | head -5; echo \"=== MON hush\"; grep -n \"^هوش\\|هوش:\" MON_part2.txt | head -10",
 "description": "Search Borhan and Moin for هوش morning"
}
```


### [2026-09-05T05:34:05.718Z] TOOL RESULT

```
=== v5
=== MON hush
1568:هوشیار. اصول آموزش و پرورش ۷۴:۱ به 
7787:هوشیاری» تیز خاطری. دانایی؛ ج. فطن. 
18256:هوشر واه ای تشاین استهمان 
27552:هوشیار. 
36384:هوش (قابوسنامه. نف. ۳۴). پشت گوش 
45067:هوشیاری» زیرکی؛ بصیرت. مبصر بودن؛ 
51945:مدهوش: ۵ (ع.] (امف.) دهشت‌زده» 
62518:هوش انده» ببدار شونده. 
65977:هوشیار کننده. 
69659:مه‌وش مهوش: ۱۱۸-5 [ - ماه‌وش]
```


## [2026-09-05T05:34:28.401Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== PHD hos/ushahin\"; grep -n \"ušahin\\|ušah\\|hōš\\|hoš\\|dawn\" PHD.txt | head -12; echo \"=== NYB ushahin/hos\"; grep -n \"ušahin\\|uš:\\|hōš\\|Morgenröte\\|dawn\" NYB_vol2_glossary.txt | head -12",
 "description": "MacKenzie and Nyberg for dawn words"
}
```


### [2026-09-05T05:34:28.642Z] TOOL RESULT

```
=== PHD hos/ushahin
252:bāmdād [6’md’t' | М bmd?d, N ~] dawn, morning. bāmīģ [P myk!] brilliant, glorious. -bān [-??s! | M Aa, N ~] suffix, -keeper, -guard. band [bnd | = Р, N ~] bond, link. band-, v. bastan. bandag [bndk! | P bndg, N ~a] servant. bang [bng | N ~] henbane. bānūg [Pnwk! | N Бапи) lady. bar [b] | N ~] fruit, produce, profit. bar-, —išn, v. burdan. ībār [Pl | N ~] time, occasion. *bār [P1 | N ~] bank, shore. заг [D] | M P?r, N ~] fruit. ‘bar [b] | M br, N ~] load, burden; duty. bāraģ [5/А! | N ~a] mount, horse. barbut [blbwt! | N ~] lyre. bārestān [b/st?n'] patient, resigned. ~ih: patience, resignation. barig/k [b’lyk' | N bārīk (cf. tārīg)) thin, fine, subtle. bar-jamag [bly mk! | N ~a] saddle-bag. barómand [b wmnd | N ~] fruitful, prolific. barsom [blswm | M brswm] the bunch of twigs used in the Yasna cere- mony. baršnūm [b/s2wm] the major purification ritual. bastan, band- [ASLWN-tn! < A Vier bstn', bnd- | M bstn, (bn-), P bnd-, N ~] tie, bind. bāstān [b’st?n' | M PysPn, N ~] always, often. bas [YHWWNS | M P, N ~] be! (imperative of büdan, q.v.) baSkué [bskwe] gryphon. bašn [bén' | = P] top, peak; stature; mane (v. buš). baw-, —i$n, v. büdan. baxš-, —išn, v. baxtan. baxt [b()At! | N ~] fortune, fate. baxtan, baxš- [HLKWN-tn! < А У hig; bC)htn', bhf- | M bxt, bx$-, N baxsidan] apportion, distribute. ~išn: bestowal, distribution. bay [ORHY A < A */h; bk', bg | M by] god, lord. im ~: his Majesty. бу ~: his late Majesty. bayaspān [by’sp’n'] messenger, envoy.
520:368 Paws] dawn.
522:6š(e)bam [w$b?m | M "wsyb^m] dawn.
601:*urwüzistan, urwāz- [”wlw?*c- = Av. urwaza-] rejoice. ~i8n: rejoicing, happiness. uskārdan, uskār- [wsk?l-tn' | J ~, (N sigāl-)] think, consider, discuss. -išn(ih): consideration, reflection. uspurrig (^wspwlyk!] = spurrig. us(t)dfrit Pzs(t)wplyt! = Av. usafriti-] offering. ušahin Pwšhyn! = Av. ufahina-] the night gah. ušnūg Pušnwk!'] = šnūģ. uštán ['wit?n! = Av. uštāna-] soul, ghost. ~th : vitality. ~отапа [-'wmnd] living, animate. uštar [GMRA < А gmD ;^wstl | N uštur] camel. 7—-$üw-palang Puštlg”plng | № ~) giraffe. uzdehig [we-, ^wzdhyk! | M ?wzdh] exiled; foreign. ~ih: exile. uzdés ["wc-,?wzdys | М ’wadys] idol. ~-parist [-plst' | M -pryst] idolater. ~-paristignih : idolatry. ~zar [-c1 | M -c’r] idol-temple. uzénag ['wcynk! | N hazina] expense, cost; exit. uzérin ['wz())ylyn! = Av. uzayeirina-] the evening gah. uzidan [wcytn! | M ?wzyd, *zozyh-] go out. uzmüdan, uzmāy- ['sozmwtn! , ”wzm'd-) prove, test, try. ~išn: testing. uzumburd ['wzmbwit! | N zumurrud] emerald. w uzwün [SNA < A If? ;^wzwn! | M ‘zw’n, (N zabdn)] tongue, language Ba ch uzwürdan, uzwār- Pwzw’l-tn! | M *zw'rdn] know, understand. ~išn: understanding; ‘huzwarish’.
657:wizürd-wars [wc'/t' wls] with parted hair. wizāstan, wizāy- [wyz'stn!, wyz'd- | M wy2’y-, N guzáy-] injure, impair, prejudice. ~išn: injury. ~išnīg: injurious. wizén [wcyn! | N guzin] choice. wizend [wz(y)nd | M wzynd, N guzand] hurt, harm, injury. wizéngar [wcynkl] chooser; selective. | wizidan, wizin- [weytn', wcyn- | M weyd, N guzīdan, guzīn-| choose, select, prefer, discriminate. wizihidan, wizīh- [w(y)cyh-ytn'] be separated. „išn(īh): separation; dawn(ing). wizin- , v. wizidan. wizir [weyl] decision, judgement. wiziristan, wizir- [wcyl-stn! | J bzyr-, N guzir-) be able to dispense with, avoid. ~iSnig : avoidable. wizistan [westn' | M weyst] teach. wizóstan, wizóh/y- [wewstn', wewd- | (J bzwb-, N pizohidan)] examine, investigate. -~i§n : investigation. wizüdan [wyzwin'] = wizastan. wizurd [wewlt'] valid, genuine, true. ~th: validity, truth. Wērūbaršt [w’wklwblst' = Av. wouru.barasti-] the north-western con- tinent of the earth. Wērūjaršt [w>wklwelft' = Av. wouru.jarasti-] the north-eastern con- tinent of the earth. wurróyistan, wurróy- [H YMNN-stn! < A hymn, У °тп | M wrwyst, (wrw-), J *brwy-, grww-, N brw-, girawidan] believe; choose. —išn [wlwdén'] belief. wuzurg [LBA < Arb’; wc(w)lg | M wzrg, N buzurg] big, great. ~ith: size, greatness. wuzurg-framadar [LBA plm't I) prime minister.
1495:dawn bamdad, ēš, ós(e)bàm.
1496:dawning wizīhišn(ih).
4422:23 Day pad Dén 27 Asman 24 Dén 28 Zamyad 25 Ard (Ahrišwang) 29 Māraspand 26 Aštād зо Anagran (v) Gāhs Hawan—morning Ēbsrūsrim—sunset to midnight Rapihwin—afternoon Ušahin--midnight to dawn Uzérin—evening
=== NYB ushahin/hos
358:ākasī [’ksy] Prth: ~ bütan to be, become visible HajA:9. — From Av. (459) ā-kas-; FrO VIII viduš: ’ks; MPrth ?gs ‘apparent, visible’. The final -y is not the silent final -y abundantly written in Prs. in- scriptions and in the Ps.; this is wanting in Prth (quite exeptionally written in site, vitavané, q. v.). Here -y is a real ending, whether -č or - is not clear, found in some cases where a pred. adj.
905:bam [b’m] splendour, beam of light 11215; nazd ~ daybreak 5°, v. nazd. — MPrth Prs bm; Paz. bim (‘day’ Aog.); NP bam; cf Av. (1468) vispo.bama- ‘all- resplendent’, (954 sq.) bämyä ‘the dawn’. V. us-bäm and the next w.
906:bam-dit [~-d’t'] at dawn 719. 672. — MPrs b’md’d; Paz. bämdäd = NP.
1550:irāšm [pl'šm] dawn, daybreak 44%, — Cf Av. (1022) hi fräsmö.däti- ‘sunset’. Bai- ley, BSOS VI 1931, 595—597; TPhS 1953, 31 sq.; Benveniste, JA 228, 1936, 230 sq.; Herzfeld, ApI 156; Sogd. 23 sq.
3326:rče [YWM; lwc] day, pl. cas. obl. —-än [Iwe?n'] 2720; contrasting with gap ‘night’ 45, 2023; ka ~ būt when day was dawning 635; im ~ to-day 10, ete.; fratük ~ to- morrow, v. fratāk; nem ~ half a day 317, v. also nem-röc; hac im = tāt 3 — within three days counting from to-day 519; — m šapān 329. 728, 7417 [all lwc]. 989-109, 1203 (YWM šp'n'], röcak šapān 742°. 1011: the astronomical day of 24 hours (Swed dygn, Russ sutkt). — The names of the days of the month are in BP: 1. Ohurmazd. 2. Vahuman. 3. Art-(Urt-)
3865:uš-bām [?wSb’m] dawn, daybreak 72°. 10133. — Av. (415) us(ah)- ‘dawn’ + *bama- ‘light’, whence (954 sq.) bāmya- ‘luminous’ (v. bämik); MPrs ?’wsyb’m (A-H I), Paz. hösbäm.
4053:vaxšišneh det. v. n. of *vaxšītan: ul ~ the flaming up, the shining forth, of the dawn 44!?,
4212:vistartan [wstltn'], visturtan [wstwltn'] vistar-, to spread 45% (-urt). 11119 (-artan); pass.: ka-š fratom frasm vistarthét when its (viz. the sun’s) first dawn is spread, shines forth 4418, — < vt-+star-, v. start; NP gustardan, -ridan; Verbum 206.
```


## [2026-09-05T05:34:29.817Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== WLD Bd1 p26 (leaf 35)\"; awk 'BEGIN{RS=\"\\f\"} NR==36' incoming/WLD/WLD_Bd1_pages.txt | head -25",
 "description": "Walde-Pokorny Bd I p.26"
}
```


### [2026-09-05T05:34:31.542Z] TOOL RESULT

```
=== WLD Bd1 p26 (leaf 35)
                                                                -                    a                    a
                                                                                                          ;




                                                      aus-                                               27

in aeoqiOQog zu bessern             (s.   Brugmann II* t, 530); ay/avoog „dem Morgen
nahe“, avgiov „morgen“ ( *avog -); horn, ijie <PoTfie „morgendlicb strahlender“
(s. Boisaeq s v.), iji-y.avog „Hahn‘
                                                  :

                                     (
                                       *ausi „in der Morgenfriihe singend“)
   lat. aurora „Morgenrote“ (fur *ausds - oris vgl. Flora flf<s )
                                                            ,      a aster „Siid-
                                                                        ,    :   ;


wind“, australis „8iidlieh“ (zur Bed. s. Vf. LEWb. 2 s. v.); vermutlich aucli
durum, sabin. ausom „Gold“ als „*rotlich“ (s. Yf. LEWb. 2 s. v.)                         ;
                                                                                             vielleicht
 Vesuvius (anders u. *ens- „brennen“); mir. fair „Sonnenaufgang“, cymr.
givaivr „Morgenrote“, bret. gwt re laoaen „Morgenstern“ (*uosri     Fick II 4
```


## [2026-09-05T05:34:52.629Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for n in 310 311; do echo \"### printed $n\"; awk -v N=$((n+9)) 'BEGIN{RS=\"\\f\"} NR==N' incoming/WLD/WLD_Bd1_pages.txt | head -20; done",
 "description": "Walde-Pokorny Bd I p.310-311"
}
```


### [2026-09-05T05:34:54.113Z] TOOL RESULT

```
### printed 310
310                                        uesu-     — ues-r, ues-(e'n-

III 4 404, wonacli Erweiterung zu *au~, aur- ..flechten, weben“); dazu viel-
leicht (Charpentier                  KZ. 40, 471, Falk-Torp                       u.   rase II)        ai.   vcdd-h „Gras-
biischel, ein besenformig gebundener Biischel starken Grases" (aus *inzda-s):
schwundstufig vielleicht (nach Petersson IF. 24, 262 f.) ai. itsnlsc:- m. „Kopf-
binde. Turban" (wenn auf Grand eines *us-n7- ..Drehung, Wickel"), ni-
nth a ,,Genickwirbel, PI. Genick" („*Wirbel k                             !




   Aber russ. v'eha s. inner nets- ..drehen" (nicbt nacli Petersson aus *iiesu )
auch seine Heranziehung von gr. ootoi^ov ..Stall, Hiirde" verdient nicbt
den Vorzug vor Bezzenbergers BB. 27, 174 allerdings auch unsicherer Yer-
bindung des gr. Wortes mit ahd. tar ..geflochtener Zaun".
                                                        <



### printed 311
                                                                  uesperoi (ueqeros;              — uesno-                                                                  311


gantn ..Friihling"        (liber *gerun aus *gehar -, *uesr, Hubschmann Arm. St.
1 24,        Arm. Gr. I 432, Pedersen KZ. 39, 416; ganz anders Patrubany IF. 14,
                                                                                                                                                                   '


60),    vasnrd ,, Sommer" (assim. aas *ve$<:ra); gr. lagi-vo ^ ..vernus
         lit.                                                           lit.
                                                                                                                                                                   - -
                                                                                                                                                                       ',



vnsannis „sommerlich", vgl. auch lat. vermis ( *cerinos): Pedersen KG. I
82, 483 dentet   auch air. crruch „Fruhling -< aus uesr-ak- (*/- durch Lenie-
rung beseitigt wie in cspartnin aus cespertina „Abenddammerung"?); aksl.
                                                a
a: run ,,Fruhjahr‘   ai. vasantd- m. r Friihlmg  ;
```


## [2026-09-05T05:35:38.667Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; mkdir -p data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg71_300.png data/verification/sources/refs/ocr/BOOK/71.png && ls -la data/verification/sources/refs/ocr/BOOK/ | head; echo \"=== recent index entries\"; tail -12 data/verification/sources/web/index.jsonl | python3 -c \"\nimport sys,json\nfor l in sys.stdin:\n    d=json.loads(l); print(d['url'])\"",
 "description": "Copy page PNG and list archived URLs"
}
```


### [2026-09-05T05:35:40.535Z] TOOL RESULT

```
total 732
drwxrwxr-x 2 sfmqrb sfmqrb   4096 Sep  5 01:35 .
drwxrwxr-x 8 sfmqrb sfmqrb   4096 Sep  4 19:03 ..
-rw-rw-r-- 1 sfmqrb sfmqrb 104864 Sep  4 19:03 101.png
-rw-rw-r-- 1 sfmqrb sfmqrb  86203 Sep  4 19:03 126.png
-rw-rw-r-- 1 sfmqrb sfmqrb 105296 Sep  4 19:03 311.png
-rw-rw-r-- 1 sfmqrb sfmqrb  96466 Sep  4 19:03 33.png
-rw-rw-r-- 1 sfmqrb sfmqrb  99093 Sep  4 19:03 39.png
-rw-rw-r-- 1 sfmqrb sfmqrb  54479 Sep  4 19:03 46.png
-rw-rw-r-- 1 sfmqrb sfmqrb  99295 Sep  4 19:03 54.png
=== recent index entries
https://en.wiktionary.org/wiki/%D9%BE%DB%8C%D8%B1%D9%88%D8%B2
https://en.wiktionary.org/wiki/%D8%A8%D9%86%D9%81%D8%B4%D9%87
https://en.wiktionary.org/wiki/%F0%90%AD%AF%F0%90%AD%A9%F0%90%AD%AB%F0%90%AD%A5%F0%90%AD%B0
https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82ewg-
https://www.etymonline.com/word/waist
https://en.wiktionary.org/wiki/оукраина
https://www.etymonline.com/word/Ukraine
https://abadis.ir/fatofa/%D8%A8%D9%86%D9%81%D8%B4%D9%87/
https://en.wikipedia.org/wiki/Cyaxares
https://en.wiktionary.org/wiki/%D8%A8%D9%86%D9%81%D8%B3%D8%AC
https://abadis.ir/fatofa/%D9%87%D9%88%D8%B4%D8%A8%D8%A7%D9%85/
https://en.wiktionary.org/wiki/اوباردن
```


## [2026-09-05T05:35:51.566Z] TOOL CALL #81: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; grep -c . data/verification/sources/web/index.jsonl; for h in 6a631f970126a71c ef3e1e5b5f985c08 ba7c51cf6efb975f 29b70a94d3d71ae6 3bec3faec531d7dd 19e39f1e2d04c7d6 2667ebf75a7b2580 86808fd68ee78884 4f84f4e4e2922b02 a5327768483f5d81 119d6a7f1cc7ea6c ceaf725535fa7d45; do grep -h \"\\\"$h.txt\\\"\" data/verification/sources/web/index.jsonl | python3 -c \"\nimport sys,json\nfor l in sys.stdin: d=json.loads(l); print(d['status'], d['url'])\" ; done",
 "description": "Verify archived URLs in index"
}
```


### [2026-09-05T05:35:53.686Z] TOOL RESULT

```
730
```


## [2026-09-05T05:35:56.914Z] TOOL CALL #82: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; head -2 data/verification/sources/web/index.jsonl; echo ---; grep -n \"h%E2%82%82ews-\\|etymonline.com/word/east\\|vihāra\\|فرخار\" data/verification/sources/web/index.jsonl | head",
 "description": "Inspect index format"
}
```


### [2026-09-05T05:35:56.969Z] TOOL RESULT

```
{"url": "https://en.wiktionary.org/wiki/%D9%BE%D8%B1%D8%AF%DB%8C%D8%B3", "file": "data/verification/sources/web/73770a9dc1c104fc.txt", "fetched": "2026-09-04T14:50:28Z", "status": 200, "bytes": 4836, "title": "پردیس - Wiktionary, the free dictionary", "note": "test: pardis etymology"}
{"url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Semitic/birk-", "file": "data/verification/sources/web/b6dbaf512836d2ee.txt", "fetched": "2026-09-04T14:51:12Z", "status": 200, "bytes": 5115, "title": "Reconstruction:Proto-Semitic/birk- - Wiktionary, the free dictionary", "note": "post-pass: page 101, root B.r.k (root-level)"}
---
707:{"url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82ews-", "file": "data/verification/sources/web/6a631f970126a71c.txt", "fetched": "2026-09-05T05:32:01Z", "status": 200, "bytes": 7698, "title": "Reconstruction:Proto-Indo-European/h₂ews- - Wiktionary, the free dictionary", "note": "page 71, root Aus 2 / Wes 2: verify PIE dawn+spring roots, NP bahar, Skt vihara, Eng east"}
711:{"url": "https://www.etymonline.com/word/east", "file": "data/verification/sources/web/3bec3faec531d7dd.txt", "fetched": "2026-09-05T05:32:03Z", "status": 200, "bytes": 7430, "title": "East - Etymology, Origin & Meaning", "note": "page 71, root Aus 2 / Wes 2: verify PIE dawn+spring roots, NP bahar, Skt vihara, Eng east"}
717:{"url": "https://en.wiktionary.org/wiki/%D9%81%D8%B1%D8%AE%D8%A7%D8%B1", "file": "data/verification/sources/web/a5327768483f5d81.txt", "fetched": "2026-09-05T05:32:57Z", "status": 200, "bytes": 3815, "title": "فرخار - Wiktionary, the free dictionary", "note": "page 71 Aus 2: Easter/Austria/aurora/vernal chains; Persian farxar; Sanskrit vihara"}
```


## [2026-09-05T05:43:20.485Z] TOOL CALL #83: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build71.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, os\n\nW_AUS   = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82ews-\"\nW_WESR  = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/w%C3%A9sr%CC%A5\"\nW_BAHAR = \"https://en.wiktionary.org/wiki/%D8%A8%D9%87%D8%A7%D8%B1\"\nW_VIHL  = \"https://en.wiktionary.org/wiki/vihara\"\nW_VIHD  = \"https://en.wiktionary.org/wiki/%E0%A4%B5%E0%A4%BF%E0%A4%B9%E0%A4%BE%E0%A4%B0\"\nW_FARX  = \"https://en.wiktionary.org/wiki/%D9%81%D8%B1%D8%AE%D8%A7%D8%B1\"\nE_EAST  = \"https://www.etymonline.com/word/east\"\nE_EASTR = \"https://www.etymonline.com/word/Easter\"\nE_AUSTR = \"https://www.etymonline.com/word/Austria\"\nE_AUROR = \"https://www.etymonline.com/word/aurora\"\nE_VERN  = \"https://www.etymonline.com/word/vernal\"\nAB_HB   = \"https://abadis.ir/fatofa/%D9%87%D9%88%D8%B4%D8%A8%D8%A7%D9%85/\"\n\nnodes = []\n\ndef N(**kw):\n    nodes.append(kw)\n\nN(id=1, lang=\"Avestan\", words=\"usaiti; ušâ; ušas-tara\",\n  verdict=\"confirmed\",\n  derivation=(\n    \"All three Avestan forms are real and correctly glossed. usaiti is the 3sg. present of the inchoative \"\n    \"stem usa- (Bartholomae lemmatises the verb as 1vah- 'aufleuchten' von der Morgenröte, present usa-, AiW col. 1393f.); \"\n    \"it continues PIE *h2us-ske-ti and is the exact match of Vedic ucchati, as Pokorny writes on the very page \"\n    \"Nourai cites ('ai. ucchati = av. usaiti (*us-sketi) leuchtet auf (vom Morgen)', IEW 86). ušâ = Av. ušah- / uš- f. \"\n    \"'Morgenröte, Morgen' (AiW col. 415f.), an s-stem *h2us-os- beside the root noun *h2us-; the eastward sense of the \"\n    \"chart's gloss comes from the derived adjective ušas-tara- 'the more easterly, eastern' (comparative in -tara- built \"\n    \"on the dawn-noun, i.e. 'lying toward the dawn'), which Bartholomae treats at col. 391 under the compound upa-ušah- \"\n    \"'Nähe der Morgenröte, Osten'. Buck 12.45 EAST states the same chain: 'Skt. usas, Av. usa dawn, whence Av. usas-tara adj.'.\"),\n  derivation_fa=(\n    \"هر سه صورت اوستایی درست‌اند. usaiti صیغهٔ سوم‌شخص مفرد حال از ستاک usa- است که بارتولومه آن را ذیل فعل ¹vah- «درخشیدن (سپیده)» \"\n    \"آورده (ستون ۱۳۹۳ فرهنگ ایرانی باستان) و از هندواروپایی آغازین *h₂us-sḱé-ti می‌آید؛ پوکورنی در همان صفحهٔ ۸۶ که نورایی ارجاع داده \"\n    \"می‌نویسد «سنسکریت ucchati = اوستایی usaiti». ušah-/uš- نیز نام سپیده‌دم است (ستون ۴۱۵) و ušas-tara- صفت تفضیلی با پسوند -tara- \"\n    \"به معنای «سوی سپیده‌دم، خاوری» است. ادعای نورایی در این گره درست است.\"),\n  sources=[W_AUS],\n  ref_check=[\n    {\"ref\":\"POK:86\",\"status\":\"supports\",\"note\":\"POK_01.txt form-feed leaf 94 (printed p.86, the page number '86' is printed on the leaf): 'aues- \\\"leuchten\\\", bes. vom Tagesanbruch … ai. ucchdti = av. usaiti (*us-sketi) \\\"leuchtet auf (vom Morgen)\\\" … av. usa, Akk. usavhdm … (usas-tara- \\\"östlich\\\")'.\"},\n    {\"ref\":\"SYN:871\",\"status\":\"supports\",\"note\":\"SYN.txt line 22241 opens '870 12.45 EAST'; the discussion runs on to p.871 (printed '871' visible at the foot of that block): 'IE *aus-, *ausos-, *usos-, etc., in words for dawn and east, beside verb forms as Skt. ucchati, Av. usaiti \\\"lights up\\\" (esp. of the dawn) … Skt. usas, Av. usa \\\"dawn\\\", whence Av. usas-tara adjs.' — exactly Nourai's three words.\"}],\n  consulted=[\n    {\"src\":\"BRT\",\"where\":\"col. 415f. (s.v. ušah-) and col. 1393f. (s.v. 1vah-); BRT.txt lines 8703, 23289\",\"stance\":\"supports\",\"note\":\"'j., g. usah- : us- f. 1) Morgenröte, Morgen' (col. 415); 'j. 1vah- V. aufleuchten von der Morgenröte. Praes. 14 (Inkoh.) usa-' (col. 1393) — the verb behind usaiti.\"},\n    {\"src\":\"POK\",\"where\":\"IEW 86-87\",\"stance\":\"supports\",\"note\":\"Also gives the o/zero-grade family *(a)us-ōs- 'Morgenröte' and *aus-tero- 'östlich' that the rest of the chart hangs on.\"},\n    {\"src\":\"WLD\",\"where\":\"WP I 26f. (WLD_Bd1_pages.txt leaf 35, printed p.26-27)\",\"stance\":\"supports\",\"note\":\"Entry 'aus-' with lat. aurora, auster, australis, mir. fair 'Sonnenaufgang', cymr. gwawr 'Morgenröte' — the same root treated by Walde-Pokorny.\"}])\n\nN(id=2, lang=\"Pahlavi\", words=\"huš\",\n  verdict=\"plausible\",\n  derivation=(\n    \"A Middle Persian word for 'dawn' does continue Av. ušah-, but its shape is disputed in the handbooks. \"\n    \"MacKenzie reads it ēš/ōš (CPD p.90 area: 'ōš(ē)bām [wšb'm | M 'wšyb'm] dawn'; the English-Pahlavi index, \"\n    \"CPD p.148, has 'dawn bāmdād, ēš, ōš(ē)bām'), and Nyberg lemmatises the compound as uš-bām, deriving it from \"\n    \"Av. ušah- 'dawn' + *bāma- 'light' and noting 'MPrs 'wsyb'm, Paz. hōsbām' (Manual II p.276 area). \"\n    \"So the Pahlavi spelling is ('w)š(y)b'm with no h-; the h- of Nourai's huš is the Pazand/New Persian prothesis that \"\n    \"Nyberg records. Horn, whom Nourai follows, prints the Pazand form: 'hōš \\\"Morgenröte\\\" (Aw.-Komm.); vergl. hōšastar \"\n    \"\\\"östlich\\\", hōšbām \\\"Tagesanbruch\\\" (Men.); aw. usah- \\\"Morgenröte\\\"; ai. usas-' (Grundriss p.281). \"\n    \"The derivation Av. ušah- > MP (h)ōš is regular (Av. -ah- > MP -ā/-Ø with the stem vowel lost); only the initial h- is secondary.\"),\n  derivation_fa=(\n    \"واژه‌ای فارسی‌میانه به معنای «سپیده‌دم» از اوستایی ušah- بازمانده است، اما ضبط آن یکسان نیست. مکنزی آن را ēš/ōš می‌خواند \"\n    \"(«ōš(ē)bām … dawn») و نیبرگ ترکیب را uš-bām می‌آورد و آن را از اوستایی ušah- «سپیده» + *bāma- «روشنایی» می‌گیرد و می‌افزاید که \"\n    \"صورت پازند آن hōsbām است. پس در پهلوی نوشتاری h آغازین نیست و «ه» در huš/هوش افزودهٔ پازند و فارسی نو است. نورایی از هرن پیروی \"\n    \"کرده که همان صورت پازند hōš «سپیده‌دم» را آورده است. بنابراین اصل ادعا درست است ولی صورت پهلوی دقیق‌تر uš/ōš است، نه huš؛ \"\n    \"ادعای نورایی با این احتیاط پذیرفتنی است.\"),\n  sources=[AB_HB],\n  ref_check=[\n    {\"ref\":\"SNS:67\",\"status\":\"supports\",\"note\":\"Tavoosi's Shayast-ne-Shayast glossary (SNS.txt line 5419) has the entry 'huš-bām/uš-bām' citing 'uSas-', 'usah-', 'bāma-', the Pahlavi writing 'wsyb'm and the Avestan Afr. Wan. I.33; the word-index (SNS.txt line 32410) gives 'hus/us-bam 67/2', i.e. the text passage at p.67 line 2 — Nourai's SNS:67.\"}],\n  consulted=[\n    {\"src\":\"PHD\",\"where\":\"MacKenzie, CPD, PHD.txt lines 520-522 (leaf 111, printed p.90) and line 1495 (English index)\",\"stance\":\"partial\",\"note\":\"'ōš(ē)bām [wšb'm | M \\\\'wšyb\\\\'m] dawn'; index 'dawn bāmdād, ēš, ōš(ē)bām' — the word is there, but read ēš/ōš, without Nourai's h-.\"},\n    {\"src\":\"NYB\",\"where\":\"Nyberg, Manual of Pahlavi II, glossary leaf 284 (printed p. ~276), s.v. uš-bām\",\"stance\":\"partial\",\"note\":\"'uš-bām [\\\\'wšb\\\\'m] dawn, daybreak 72°, 10133. — Av. (415) us(ah)- \\\"dawn\\\" + *bāma- \\\"light\\\" … MPrs \\\\'wsyb\\\\'m (A-H I), Paz. hōsbām.' Confirms the etymology and shows the h- is Pazand.\"},\n    {\"src\":\"HRN\",\"where\":\"Horn, Grundriss p.281 no.117 (HRN.txt leaf 302)\",\"stance\":\"supports\",\"note\":\"'hōš \\\"Morgenröte\\\" (Aw.-Komm.); vergl. hōšastar \\\"östlich\\\", hōšbām \\\"Tagesanbruch\\\" (Men.). aw. usah- \\\"Morgenröte\\\"; ai. usas-.' — Nourai's source for the h-form.\"}])\n\nN(id=3, lang=\"Persian\", words=\"hŭš 2 «هوش ۲»; hŭšbâm «هوشبام»\",\n  verdict=\"plausible\",\n  derivation=(\n    \"هوشبام hōšbām 'the first light of dawn, daybreak' is genuine and is the direct continuation of Pahlavi (u)š-bām \"\n    \"= Av. ušah- 'dawn' + bāma- 'light, radiance' (Nyberg, Manual II s.v. uš-bām; Horn p.281 'hōšbām Tagesanbruch'); \"\n    \"the Persian form keeps the Pazand prothetic h-, and the compound is transparent in Persian because بام(داد) \"\n    \"'dawn' is the same second member. Two reservations. (a) هوش as a free-standing New Persian noun 'morning' is \"\n    \"essentially a lexicographers' back-formation out of هوشبام: Horn's hōš is quoted from the Pahlavi Avesta commentary, \"\n    \"not from New Persian, and it is unrelated to the common Persian هوش 'mind, consciousness' (< OIr. *hu-šyāti-/*aoša-), \"\n    \"which is why Nourai numbers it '2' and calls both words obsolete — a fair warning. \"\n    \"(b) The gloss 'breakfast' for هوشبام is wrong; the word means سپیده‌دم/پگاه, and no dictionary gives it a meal sense \"\n    \"(the printed page really does read 'morning shine, breakfast', so this is the book's slip, not the extraction's).\"),\n  derivation_fa=(\n    \"«هوشبام» به معنای نخستین روشنایی بامداد اصیل است و مستقیماً دنبالهٔ (u)š-bām پهلوی است، یعنی اوستایی ušah- «سپیده» + \"\n    \"bāma- «روشنایی» (نیبرگ ذیل uš-bām؛ هرن ص ۲۸۱ «hōšbām = بامدادِ نخست»)؛ «ه» آغازین از پازند مانده است و جزء دوم همان «بام» \"\n    \"فارسی است. دو نکته: نخست آنکه «هوش ۲» به معنای «بامداد» واژه‌ای مستقل در فارسی نو نیست و بیشتر برساختهٔ فرهنگ‌نویسان از \"\n    \"همین «هوشبام» است و با «هوشِ» رایج (خرد و آگاهی) هم‌ریشه نیست؛ خود نورایی هم آن را متروک خوانده است. دوم آنکه معنای \"\n    \"«breakfast» (صبحانه) که در کتاب برای هوشبام آمده نادرست است؛ این واژه تنها به معنای سپیده‌دم و پگاه است. صفحهٔ چاپی همین \"\n    \"«breakfast» را دارد، پس خطا از کتاب است نه از اسکن. در مجموع ادعای نورایی با این احتیاط‌ها پذیرفتنی است.\"),\n  sources=[AB_HB],\n  ref_check=[\n    {\"ref\":\"HRN:281\",\"status\":\"supports\",\"note\":\"HRN.txt leaf 302 (printed p.281, running head '— 281 —'), entry 117: 'hōš \\\"Morgenröte\\\" (Aw.-Komm.); vergl. hōšastar \\\"östlich\\\", hōšbām \\\"Tagesanbruch\\\" (Men.). aw. usah- \\\"Morgenröte\\\"; ai. usas-.' Horn supports the words and the Avestan source, but glosses hōšbām 'daybreak', never 'breakfast'.\"},\n    {\"ref\":\"SNS:67\",\"status\":\"supports\",\"note\":\"SNS.txt line 5419 s.v. huš-bām/uš-bām, with Av. usah- + bāma- and the Pahlavi spelling 'wsyb'm; index line 32410 'hus/us-bam 67/2'.\"}],\n  consulted=[\n    {\"src\":\"NYB\",\"where\":\"Manual of Pahlavi II, s.v. uš-bām (glossary leaf 284)\",\"stance\":\"supports\",\"note\":\"'Av. (415) us(ah)- \\\"dawn\\\" + *bama- \\\"light\\\" … Paz. hōsbām' — the Persian h-form is the Pazand one.\"},\n    {\"src\":\"BQT\",\"where\":\"Borhan-e Qate' vols 4-5 (BQT_v4_pages.txt / BQT_v5_pages.txt), searched for هوشبام\",\"stance\":\"silent\",\"note\":\"grep 'هوشبام' returns nothing in the OCR of the ه section; the word is not in Mo'in's Farhang-e Farsi OCR either (grep of MON_part1/2).\"},\n    {\"src\":\"MON\",\"where\":\"abadis.ir entry هوشبام (user-contributed section, archived)\",\"stance\":\"partial\",\"note\":\"Gives 'هوشبام (اوشبامه، hošbama) … واژه اوستایی … معنی: سپیده دم، پگاه، بامداد، سحرگاه' — i.e. dawn, never 'breakfast'. User-submitted content, cited only as a check on the modern Persian meaning.\"}])\n\nN(id=4, lang=\"Indo-European\", words=\"Wes 2, Wesr\",\n  verdict=\"plausible\",\n  derivation=(\n    \"The r/n-stem *u̯es-r̥ / *u̯es-n- 'spring' is a real reconstruction (Pokorny IEW 1174 'u̯es-r̥ (lat.-germ. u̯er nach \"\n    \"*i̯ēr \\\"Jahr\\\"), Gen. u̯es-n-es \\\"Frühling\\\"'; Walde-Pokorny I 310f.; Mann IEC col. ~1650 'uesər- (1) … dawn, springtime'; \"\n    \"Watkins AHD 'wesr̥. Spring.'). What is only probable is the arrow Nourai draws from the dawn root to it. \"\n    \"Pokorny himself makes exactly that claim twice — on p.87, under aues-, he notes the r/n-stem '*u̯es-r-, u̯es-n- \\\"Frühling\\\" \"\n    \"unter besonderem Schlagwort' as 'wurzelverwandt', and the u̯es-r̥ entry on p.1174 ends 'wohl zu aues- \\\"leuchten\\\", oben S. 86 f.' — \"\n    \"and Klein, whom Nourai cites here, says s.v. vernal 'L. ver, etc., possibly derive fr. I.-E. base *wes-, *awes-, \\\"to shine\\\", \"\n    \"whence also L. aurora'. Both hedge ('wohl', 'possibly'). Watkins keeps wesr̥ as a separate root from aus-1, and Wiktionary's \"\n    \"main line now takes *wósr̥ to a different root, *h1wes-/*h1ews- 'to become warm, burn'; but its alternative reconstruction \"\n    \"*h2wósr̥ (Lipp 2009 I.164, 'vor-uridg. *h2u̯ós-r̥ / Obl. *h2u̯és-n-') is precisely the dawn root's *h2w-. So: an old, \"\n    \"respectable, still-live connection, not a settled one.\"),\n  derivation_fa=(\n    \"ستاک r/n یِ *u̯es-r̥ / *u̯es-n- «بهار» بازسازی‌ای واقعی است (پوکورنی ص ۱۱۷۴، والده-پوکورنی جلد ۱ ص ۳۱۰، مان، واتکینز). \"\n    \"آنچه تنها «محتمل» است پیوند آن با ریشهٔ «درخشیدن» است که نورایی رسم کرده. خودِ پوکورنی دو بار همین ادعا را می‌کند: در ص ۸۷ \"\n    \"ذیل aues- این ستاک را «هم‌ریشه» می‌خواند و در ص ۱۱۷۴ می‌نویسد «wohl zu aues- \\\"leuchten\\\"، بالا ص ۸۶ و ۸۷». کلاین هم ذیل vernal \"\n    \"می‌گوید لاتینی ver «شاید» از پایهٔ *wes-/*awes- «درخشیدن» باشد. اما واتکینز آن را ریشه‌ای جداگانه می‌داند و ویکی‌واژه امروز \"\n    \"آن را به *h₁wes- «گرم شدن، سوختن» می‌برد، هرچند بازسازی جایگزین *h₂wósr̥ (لیپ ۲۰۰۹) دوباره همان ریشهٔ سپیده‌دم را نشان می‌دهد. \"\n    \"پس ادعای نورایی با احتیاط پذیرفتنی است: پیوندی کهن و هنوز زنده، ولی نه قطعی.\"),\n  sources=[W_WESR, W_AUS],\n  ref_check=[\n    {\"ref\":\"KLN:1702\",\"status\":\"supports\",\"note\":\"The 1966 two-volume scan (KLN_1966.txt) breaks off at leaf 902 ≈ printed p.1700-1701, one page before 'vernal'; the entry is read in the 1971 unabridged text (KLN_1971.txt): 'vernal, adj. … fr. ver, \\\"spring\\\", which is cogn. with ON. var, Gk. ear, OI. vasantah, ModPers. bahar, Arm. gar-un, OSlav. vesna … L. ver, etc., possibly derive fr. I.-E. base *wes-, *awes-, \\\"to shine\\\", whence also L. aurora, \\\"dawn\\\". See aurora and east.' Exactly Nourai's Aus 2 -> Wes 2 arrow, with Klein's own hedge 'possibly'.\"}],\n  consulted=[\n    {\"src\":\"POK\",\"where\":\"IEW 87 (POK_01 leaf 95) and IEW 1174 (POK_03 leaf 418)\",\"stance\":\"supports\",\"note\":\"p.87: 'ues-, uos- … (vgl. dazu auch den wurzelverwandten r/n-St. *ues-r-, ues-n- \\\"Frühling\\\" unter besonderem Schlagwort)'; p.1174 ends 'WP. I 301 … wohl zu aues- \\\"leuchten\\\", oben S. 86 f.'\"},\n    {\"src\":\"AHD\",\"where\":\"Watkins 1985, AHD_watkins1985.txt line 1164\",\"stance\":\"partial\",\"note\":\"'wesr̥. Spring. Latin vér, spring (phonologically irregular): VERNAL; PRIMAVERA. [Pok. wes-r 1174.]' — a separate headword from 'aus-1. To shine' (line 316); Watkins does not join them.\"},\n    {\"src\":\"WLD\",\"where\":\"WP I 310-311 (WLD_Bd1_pages.txt leaves 319-320)\",\"stance\":\"supports\",\"note\":\"Running head 'uesu- — ues-r, ues-(e)n-'; the entry gathers arm. garun, lat. vernus, ai. vasanta-, aksl. vesna.\"},\n    {\"src\":\"IEC\",\"where\":\"Mann, IEC col. ~1650 (IEC.txt line 20148, leaf 840)\",\"stance\":\"supports\",\"note\":\"'uesər- (1) (variants: uesənt-, uesōr, uesna) \\\"dawn, springtime\\\". WP I, 310' — Mann's headword gloss itself fuses the two senses Nourai's two boxes separate.\"}])\n\nN(id=5, lang=\"Avestan\", words=\"vasar, vasri; vanri, vanhâr\",\n  verdict=\"plausible\",\n  derivation=(\n    \"The genuinely Avestan pair is the second one: Bartholomae AiW col. 1347f. has 'j. vaŋhar- (, p. vaŋar-) n. \\\"Frühling\\\": \"\n    \"vaŋri (LS.)' from F.8 — a neuter r/n-stem with the locative vaŋri, exactly the chart's vanhâr / vanri (n written for ŋ). \"\n    \"vasar / vasri are not attested Avestan forms but the pre-Avestan (Indo-Iranian) antecedents: intervocalic *s becomes h \"\n    \"in Iranian, so *vasar- > vaŋhar- and *vasri > vaŋri, and Pokorny writes precisely that on p.1174, 'av. vaŋri Lok. \\\"im \"\n    \"Frühling\\\" (*vasri für älteres *vasar)'; the -s- forms survive in Vedic vasar-hán-, vasantá-. Aryanpur's entry for بهار \"\n    \"(p.138) makes the same, equally loose, list 'AVESTAN: VANRI, VAHAR, VAHRI, VASRI'. So the box is right in substance but \"\n    \"labels two reconstructed Indo-Iranian forms as Avestan.\"),\n  derivation_fa=(\n    \"جفت واقعاً اوستایی، دومی است: بارتولومه در ستون ۱۳۴۷ می‌آورد «vaŋhar- (خنثی) \\\"بهار\\\"، حالت دری vaŋri»، که همان vanhâr/vanri \"\n    \"نمودار است (n به جای ŋ نوشته شده). اما vasar و vasri صورت‌های اوستایی نیستند، بلکه صورت‌های کهن‌ترِ هندوایرانی‌اند؛ زیرا s \"\n    \"میان‌واکه‌ای در ایرانی به h بدل می‌شود: *vasar- ← vaŋhar- و *vasri ← vaŋri. پوکورنی در ص ۱۱۷۴ همین را می‌نویسد: «vaŋri اوستایی \"\n    \"… *vasri به‌جای vasar کهن‌تر». صورت‌های s-دار در ودایی (vasar-hán-, vasantá-) مانده است. آریان‌پور نیز در ص ۱۳۸ همین فهرست کمی \"\n    \"نادقیق را دارد. پس محتوای گره درست است ولی برچسب «اوستایی» برای دو صورت بازسازی‌شده دقیق نیست.\"),\n  sources=[W_BAHAR, W_WESR],\n  ref_check=[\n    {\"ref\":\"POK:1174\",\"status\":\"supports\",\"note\":\"POK_03 leaf 418 (the printed '1174' stands on the leaf): 'ues-r̥ … Gen. ues-n-es \\\"Frühling\\\" … av. vaŋri Lok. \\\"im Frühling\\\" (*vasri für älteres *vasar, vgl. npers. bahar mit Quantitätsumsprung aus *vahar, vgl. apers. θūra-vāhara-)'. Supports the forms, but shows vasar/vasri are the pre-forms, not Avestan.\"}],\n  consulted=[\n    {\"src\":\"BRT\",\"where\":\"AiW col. 1347f. (BRT.txt line 22489, leaf 741)\",\"stance\":\"supports\",\"note\":\"'j. vaŋhar- (, p. vaŋar-) n. \\\"Frühling\\\": vaŋri (LS.) F. 8.'\"},\n    {\"src\":\"ARY\",\"where\":\"Aryanpur, Farhang-e rishe-ha-ye hend-o-orupayi, printed p.138 (ARY_latin_index_pages.txt, pdf page 137)\",\"stance\":\"supports\",\"note\":\"Entry for بهار lists 'VANRI, VAHAR, VAHRI, VASRI (AVESTAN); VAHARA (OLD PERSIAN); WAHAR, VAHAR (PAHLAVI); VASAR, VASAN, VASANTAS (SANSKRIT); GARUN, GARNAN (ARMENIAN); VER, VERIS (LATIN)' — the same four Avestan forms Nourai gives.\"},\n    {\"src\":\"IEC\",\"where\":\"Mann, IEC s.v. uesər- (1)\",\"stance\":\"partial\",\"note\":\"Lists 'Av. vāhrō, m. and vahār' but no vasri; the s-forms are given as Skt. vasar, vasantáh.\"}])\n\nN(id=6, lang=\"Pahlavi\", words=\"vahâr\",\n  verdict=\"confirmed\",\n  derivation=(\n    \"MP wahār 'spring' is well attested and is the regular Middle Persian outcome of the Old Iranian r/n-stem: \"\n    \"MacKenzie, CPD p.86, 'wahār [wh'l, (b'l) | M whr, N bahār] spring. ~īg [-yg | N -ī] spring, vernal'; Nyberg's glossary \"\n    \"s.v. 'wh'r: vahār'. Phonologically Av. vaŋhar- / OIr. *vahār- keeps its -h- (from IIr. *s) and the initial w- is still w- \"\n    \"in Middle Persian; the Manichaean spelling whr and the Book-Pahlavi wh'l are the same word. Horn cites 'phlv. vahār' at \"\n    \"exactly the page Nourai gives.\"),\n  derivation_fa=(\n    \"«وهار» فارسی میانه به معنای بهار به‌خوبی گواهی شده و بازماندهٔ منظمِ ستاک ایرانی باستان است: مکنزی می‌آورد \"\n    \"«wahār [wh'l] بهار؛ wahārīg بهاری» و نیبرگ نیز صورت wh'r: vahār را ثبت کرده است. از نظر آوایی h (بازماندهٔ s هندوایرانی) \"\n    \"برجاست و w آغازین هنوز به b بدل نشده است. هرن در همان صفحه‌ای که نورایی ارجاع داده «phlv. vahār» را آورده است. \"\n    \"ادعای نورایی درست است.\"),\n  sources=[W_BAHAR],\n  ref_check=[\n    {\"ref\":\"HRN:56\",\"status\":\"supports\",\"note\":\"HRN.txt leaf 77 (printed p.56), entry 243: 'behār \\\"Frühling\\\". Käs. vor neben bohor. ap. θūra-vāhara- (?); aw. vaŋhri \\\"im Frühling\\\" (ZP. 61); phlv. vahār; ai. vasantá- \\\"Frühling\\\" … arm. garun \\\"Frühling\\\".' Horn's page carries the whole Avestan-Pahlavi-Persian chain of Nourai's row.\"}],\n  consulted=[\n    {\"src\":\"PHD\",\"where\":\"MacKenzie, CPD p.86 (PHD.txt line 605, leaf 111 region)\",\"stance\":\"supports\",\"note\":\"'wahār [wh\\\\'l, (b\\\\'l) | M whr, N bahār] spring. ~īg [-yk\\\\' | N -ī] spring, vernal.'\"},\n    {\"src\":\"NYB\",\"where\":\"Nyberg, Manual II glossary, ideogram/transliteration list leaf 284\",\"stance\":\"supports\",\"note\":\"'wh\\\\'r: vahār' — Nyberg's reading of the same Book-Pahlavi spelling.\"},\n    {\"src\":\"IEC\",\"where\":\"Mann, IEC s.v. uesər- (1)\",\"stance\":\"supports\",\"note\":\"'Av. vāhrō, m. and vahār, pl. id.; O[ld] Per. vahāra-, Per. bahār, id.'\"}])\n\nN(id=7, lang=\"Persian\", words=\"bahâr «بهار»\",\n  verdict=\"confirmed\",\n  derivation=(\n    \"NP بهار bahār 'spring' is MP wahār with the regular New Persian change of initial w- to b- (as in MP wād > باد, \"\n    \"MP wahišt > بهشت); Pokorny notes in addition the quantity shift, 'npers. bahar mit Quantitätsumsprung aus *vahār', \"\n    \"i.e. the long vowel moves to the second syllable. Wiktionary gives the full modern chain: 'From Middle Persian whʾl \"\n    \"(wahār), from Old Persian v-a-h-r, from Proto-Iranian *wáhār, collective of *wáhr̥, from Proto-Indo-Iranian *wásr̥, \"\n    \"ultimately from Proto-Indo-European *wósr̥ (spring)', with the cognates Latin ver, Greek éar, Armenian garun, \"\n    \"OCS vesna — the same set Klein lists s.v. vernal, where Persian bahar is named explicitly.\"),\n  derivation_fa=(\n    \"«بهار» فارسی نو همان wahār فارسی میانه است با تبدیل قاعده‌مند w آغازین به b (مانند wād ← باد، wahišt ← بهشت)؛ \"\n    \"پوکورنی افزون بر آن به جابه‌جایی کمیت واکه اشاره می‌کند: «bahār فارسی نو با جابه‌جایی کشش از *vahār». ویکی‌واژه زنجیرهٔ کامل \"\n    \"را چنین می‌آورد: فارسی میانه wahār ← پارسی باستان vāhara- ← ایرانی آغازین *wáhār ← هندوایرانی *wásr̥ ← هندواروپایی *wósr̥. \"\n    \"کلاین نیز ذیل vernal «ModPers. bahar» را در کنار ver لاتینی و éar یونانی و garun ارمنی می‌نشاند. ادعای نورایی درست است.\"),\n  sources=[W_BAHAR, W_WESR, E_VERN],\n  ref_check=[\n    {\"ref\":\"POK:1174\",\"status\":\"supports\",\"note\":\"POK_03 leaf 418: '… vgl. npers. bahar mit Quantitätsumsprung aus *vahar, vgl. apers. θūra-vāhara-'.\"},\n    {\"ref\":\"KLN:1702\",\"status\":\"supports\",\"note\":\"KLN_1971.txt s.v. vernal (the 1966 scan stops one page short of p.1702): '… fr. ver, \\\"spring\\\", which is cogn. with ON. var, Gk. ear, OI. vasantah, ModPers. bahar, Arm. gar-un, OSlav. vesna, \\\"spring\\\", Lith. vasara, \\\"summer\\\".'\"}],\n  consulted=[\n    {\"src\":\"HRN\",\"where\":\"Horn, Grundriss p.56 no.243\",\"stance\":\"supports\",\"note\":\"'behār \\\"Frühling\\\" … phlv. vahār; ai. vasantá-' — Horn's headword is the New Persian word itself.\"},\n    {\"src\":\"MON\",\"where\":\"Mo'in, Farhang-e Farsi (MON_part1.txt line 26303)\",\"stance\":\"supports\",\"note\":\"'بهار: (ا.) اولین فصل سال، ربیع' — and separately 'بهار ۲ (ا.) بتخانه، بتکده', i.e. Mo'in keeps the 'spring' word and the 'idol-temple' word (< vihāra) apart, as one should.\"},\n    {\"src\":\"ARY\",\"where\":\"Aryanpur p.138\",\"stance\":\"supports\",\"note\":\"Same entry as node 5: Avestan/Old Persian/Pahlavi/Latin cognate list under the Persian headword بهار.\"},\n    {\"src\":\"HUB\",\"where\":\"Hübschmann, Persische Studien (HUB.txt line 1062)\",\"stance\":\"silent\",\"note\":\"His note on Horn's no.243 is only 'Vgl. Nr. 501.'; he adds nothing about bahār.\"}])\n\nN(id=8, lang=\"Sanskrit\", words=\"vihâra\",\n  verdict=\"disputed\",\n  derivation=(\n    \"Both the gloss and the parentage are wrong. Sanskrit विहार vihāra never means 'spring': Monier-Williams and Wiktionary \"\n    \"give 'walking for pleasure, roaming; sport, pastime; a place of recreation; (Buddhism, Jainism) a monastery or temple \"\n    \"(originally a hall where the monks met or walked about)'; the province of Bihar is named from its monasteries. \"\n    \"Morphologically it is vi- + the root hṛ 'to carry, move' (Wiktionary files it under 'Sanskrit terms prefixed with वि-'), \"\n    \"so it has nothing to do with *u̯es-r̥ 'spring' and cannot hang from Nourai's 'Wes 2' box. \"\n    \"What has happened is a conflation of two Persian homonyms: بهار 'spring' (< MP wahār, this row) and بهار 'idol-temple' \"\n    \"(< Skt. vihāra), which Mo'in keeps apart in the Farhang-e Farsi and in the very footnote Nourai cites, where the Sanskrit \"\n    \"word is glossed as the source of Persian بهار in the sense 'temple', not 'spring'. The printed page (pdf p.71) really does \"\n    \"read 'vihâra : spring', so the error is Nourai's, not the extraction's. The onward links (vihāra > Sogdian > farxār) are sound.\"),\n  derivation_fa=(\n    \"هم معنی و هم جایگاه این گره نادرست است. «vihāra» سنسکریت هرگز به معنای «بهار (فصل)» نیست؛ در مونیر-ویلیامز و ویکی‌واژه آمده: \"\n    \"«گردش و تفرج، بازی و خوش‌گذرانی، تفرجگاه، و در بودایی و جینی: صومعه یا معبد (در اصل تالاری که راهبان در آن گرد می‌آمدند)»؛ \"\n    \"نام ایالت بیهار هم از همین است. ساخت واژه vi- + ریشهٔ hṛ «بردن، حرکت کردن» است، پس هیچ پیوندی با *u̯es-r̥ «بهار» ندارد و \"\n    \"نمی‌تواند زیرشاخهٔ «Wes 2» باشد. خطا از هم‌آوایی دو واژهٔ فارسی برخاسته است: «بهار» (فصل، از wahār پهلوی) و «بهار» (بتخانه، از \"\n    \"vihāra سنسکریت). معین در فرهنگ فارسی و در همان حاشیهٔ برهان قاطع که نورایی ارجاع داده این دو را جدا نگاه داشته است. \"\n    \"صفحهٔ چاپی کتاب نیز «vihâra : spring» دارد، پس خطا از خود کتاب است نه از استخراج. اما ادامهٔ زنجیره (vihāra ← سغدی ← فرخار) درست است.\"),\n  sources=[W_VIHD, W_VIHL, W_FARX],\n  ref_check=[\n    {\"ref\":\"BQT:1452\",\"status\":\"partial\",\"note\":\"Borhan-e Qate' vol. 3, footnote 1 on the فرخار page (BQT_v3_pages.txt pdf page 245, printed ~1450-1452): 'farxār فارسی (بمعنی صنم و معبد (بتخانه)) از کلمهٔ سغدی Brghʾr مأخوذ است (Gauthiot, JA., 1911, I, pp.53, 500) و آن خود از vihāra سانسکرت گرفته شد که این کلمه خود در فارسی بصورت «بهار» درآمده است (Henning, Sogdian loan-words, BSOS X.1, p.94)'. Mo'in has the Sanskrit word and the route, but glosses it 'temple/idol-house' and derives from it the Persian بهار 'temple' — never 'spring'.\"}],\n  consulted=[\n    {\"src\":\"MON\",\"where\":\"Mo'in, Farhang-e Farsi, MON_part1.txt line 26313\",\"stance\":\"contradicts\",\"note\":\"'بهار: ۲ (ا.) بتخانه، بتکده' is a separate headword from 'بهار: ۱ … اولین فصل سال، ربیع' — Mo'in does not let vihāra feed the 'spring' word.\"},\n    {\"src\":\"SOD\",\"where\":\"Gharib, Sogdian Dictionary, entry 2741 (printed p. ~107-108)\",\"stance\":\"partial\",\"note\":\"'2741 βrγʾr B,S farxār ©Skt. vihāra ©ob. -y … temple' — Sanskrit vihāra is the source of a word for 'temple', not for a word for 'spring'.\"}],\n  error_in=\"book\", book_prints=\"vihâra : spring\",\n  correct_form=\"vihâra 'monastery, (Buddhist) temple' (< vi- + hṛ), not a word for 'spring' and not a descendant of *u̯es-r̥\")\n\nN(id=9, lang=\"Sogdian\", words=\"brğ`r\",\n  verdict=\"confirmed\",\n  derivation=(\n    \"Sogdian βrγʾr (Gharib transliterates βrγʾr, reads farxār) 'temple' is a Buddhist loanword from Sanskrit vihāra, taken over \"\n    \"along the Silk-Road missionary route in the Sogdian Buddhist texts (Gharib's citations are the Sūtra of Causes and Effects \"\n    \"and the Vessantara Jātaka). The phonetics are those of an Indic word entering Sogdian: initial v- is rendered by β, \"\n    \"the intervocalic -h- of vihāra is written -γ- (Sogdian γ covering the velar spirant that Iranian ears substituted for Indic h), \"\n    \"and the unstressed first vowel syncopates, vihāra > *viγār > βrγʾr. Mo'in's footnote gives the same, with Gauthiot's and \"\n    \"Henning's references.\"),\n  derivation_fa=(\n    \"«βrγʾr» سغدی (قریب آن را βrγʾr می‌نویسد و farxār می‌خواند) به معنای «معبد» وام‌واژه‌ای بودایی از vihāra سنسکریت است که در متن‌های \"\n    \"بودایی سغدی به کار رفته است. دگرگونی‌های آوایی همان‌هاست که در وام‌گیری واژه‌های هندی به سغدی دیده می‌شود: v آغازین به β، \"\n    \"ه میان‌واکه‌ای به γ نوشته می‌شود و واکهٔ بی‌تکیهٔ نخست می‌افتد: vihāra ← *viγār ← βrγʾr. معین نیز در حاشیهٔ برهان قاطع با ارجاع به \"\n    \"گوتیو و هنینگ همین را می‌گوید. ادعای نورایی درست است.\"),\n  sources=[W_FARX],\n  ref_check=[\n    {\"ref\":\"SOD:108\",\"status\":\"supports\",\"note\":\"Gharib, Sogdian-Persian-English Dictionary, entry 2741 on printed p. ~107-108 (SOD_pages.txt leaf 173, printed = leaf - 66): '2741 βrγʾr B,S … farxār (βrγʾr) ©Skt. vihāra ©ob. -y => βrγʾr temple' (a second entry, 3886 βryʾr, p. ~153, repeats it). The OCR renders Gharib's γ as 'Y', so his headword is exactly Nourai's brğ`r.\"}],\n  consulted=[\n    {\"src\":\"BQT\",\"where\":\"Borhan-e Qate' vol. 3, footnote on فرخار (pdf page 245, printed ~1450-52)\",\"stance\":\"supports\",\"note\":\"'… از کلمهٔ سغدی Brghʾr مأخوذ است (Gauthiot, JA., 1911, I, pp.53, 500) و آن خود از vihāra سانسکرت گرفته شد … Henning, Sogdian loan-words…, BSOS X.1, p.94.'\"},\n    {\"src\":\"ISS_alt_DKS\",\"where\":\"Bailey, Khotanese texts / Dictionary of Khotan Saka (ISS_alt_DKS.txt)\",\"stance\":\"silent\",\"note\":\"No entry matching βrγʾr / vihāra was found by grep; Bailey has no bearing on this Sogdian form.\"}])\n\nN(id=10, lang=\"Persian\", words=\"farxâr «فرخار»\",\n  verdict=\"confirmed\",\n  derivation=(\n    \"NP فرخار farxār 'idol-temple, Buddhist monastery' (hence 'a place full of beautiful faces', and the city name Farkhār in \"\n    \"Tokharistan/Talaqan) is the Sogdian βrγʾr taken into Persian, with the usual Persian treatment of an initial cluster \"\n    \"βr- > far- and of Sogdian γ before a back vowel > x: βrγʾr > farxār. Asadi Tusi's Loghat-e Fors already defines it \"\n    \"'فرخار بتخانه هست و گویند شهرست در ترکستان … و در آنجا بتخانه‌ها بسیار است' and quotes the very Rudaki line printed in \"\n    \"the chart. The chart's NOTE is right to send the reader to Borhan-e Qate': Mo'in's footnote there records the rival \"\n    \"proposal of Benveniste (BSL 1928, 27-8), that the word is not the Sogdian Buddhist loan at all but Iranian \"\n    \"*paru-xvāθra- 'full of joy'. Modern opinion follows Gauthiot-Henning, and Wiktionary states flatly: 'Borrowed from Sogdian \"\n    \"(βṛγʾr, \\\"Buddhist temple\\\"), from Sanskrit विहार (vihāra)'.\"),\n  derivation_fa=(\n    \"«فرخار» در فارسی به معنای بتخانه و صومعهٔ بودایی (و از آنجا «جای پر از زیبارویان» و نیز نام شهری در تخارستان و طالقان) \"\n    \"همان βrγʾr سغدی است: خوشهٔ آغازی βr- به far- و γ سغدی پیش از واکهٔ پسین به x بدل شده است. اسدی طوسی در لغت فرس آورده \"\n    \"«فرخار بتخانه هست و گویند شهرست در ترکستان … و در آنجا بتخانه‌ها بسیار است» و همان بیت رودکی را که در نمودار آمده گواه \"\n    \"می‌آورد. یادداشت نمودار نیز درست است: معین در حاشیهٔ برهان قاطع رأی مخالف بنونیست (۱۹۲۸) را می‌آورد که واژه را نه وام سغدی، \"\n    \"بلکه ایرانیِ *paru-xvāθra «پر از شادی» می‌داند. پژوهش امروزی همان نظر گوتیو و هنینگ را می‌پذیرد و ویکی‌واژه صریح می‌گوید: \"\n    \"«وام‌گرفته از سغدی βṛγʾr، از vihāra سنسکریت». ادعای نورایی درست است.\"),\n  sources=[W_FARX],\n  ref_check=[\n    {\"ref\":\"BQT:1452\",\"status\":\"supports\",\"note\":\"Borhan vol.3, the فرخار article and its footnotes (BQT_v3_pages.txt pdf page 245, printed ~1450-52): footnote 1 as quoted for node 9; a further footnote gives Minorsky's and Benveniste's dissent, 'بلکه کلمه‌ایست ایرانی از ریشهٔ paru-xuvathra (پر از شادی), Benveniste, Bull. Soc. Ling. 1928, 27-8' — this is the 'discussion on the derivation' the chart's NOTE points to.\"},\n    {\"ref\":\"FRS:87\",\"status\":\"partial\",\"note\":\"The available scan of Loghat-e Fors is a different edition (pagination does not match Nourai's 1365 Kharazmi text), but the entry is there, FRS_pages.txt line ~5822: 'فرخار بتخانه هست و گویند شهرست در ترکستان … رودکی گفت: فرخار بزرگ و نیک جایی است / گر معدن آن بت نوایی است' — the same headword, gloss and Rudaki verse as the chart.\"}],\n  consulted=[\n    {\"src\":\"MON\",\"where\":\"Mo'in, Farhang-e Farsi, MON_part2.txt line 5964\",\"stance\":\"supports\",\"note\":\"'فرخار: [بهار، دیر، معبد] (ا.) بتکده، بتخانه. هر شهر حسن‌خیز: جایی که مردم آن زیبا باشند'.\"},\n    {\"src\":\"SOD\",\"where\":\"Gharib, entry 2741 (p. ~108)\",\"stance\":\"supports\",\"note\":\"Gharib himself reads the Sogdian word as 'farxār', i.e. equates it with the Persian form.\"},\n    {\"src\":\"FSF\",\"where\":\"Noushin, Vazhe-namak (FSF_pages.txt)\",\"stance\":\"silent\",\"note\":\"grep 'فرخار' returns no entry.\"}])\n\nN(id=11, lang=\"Old Persian\", words=\"vâhara\",\n  verdict=\"confirmed\",\n  derivation=(\n    \"OP *vāhara- 'spring' is not attested alone but in the month-name Θūravāhara-, the second Achaemenid month \"\n    \"(April-May), read in the Bisotun inscription ('Θūravāharahya māhyā VIII raucabiš θakatā āha', DB 2.36). \"\n    \"Kent glosses it in the Lexicon, p.188, 'Θūravāhara- adj. \\\"Thuravahara\\\", second month, April-May: Elam. turmar, \"\n    \"Akk. Ajaru', and in the grammar, 'Θūra-vahara- \\\"(Month) having vigorous spring-time\\\"' (§159), listing vāhara- among \"\n    \"stems 'extending a non-verbal stem … vāhara- in Θūra-vahara- to *wasr̥' (§154.I). Bartholomae, AiW col. 788, has the \"\n    \"same: 'eig. \\\"die siegreiche Frühlingszeit\\\"; *vāhara- n., Ableitung aus vaŋhar-'. The Old Persian form keeps -h- \"\n    \"(< IIr. *s) and the long ā of the collective/derived stem, exactly as Middle Persian wahār requires.\"),\n  derivation_fa=(\n    \"*vāhara- پارسی باستان به‌تنهایی گواهی نشده، بلکه در نام ماه Θūravāhara- (ماه دوم هخامنشی، فروردین-اردیبهشت) دیده می‌شود که در \"\n    \"کتیبهٔ بیستون آمده است. کنت در واژه‌نامهٔ خود، ص ۱۸۸، آن را «ماه دوم، آوریل-مه» معنی می‌کند و در دستور می‌نویسد \"\n    \"«Θūra-vahara- یعنی ماهی که بهارِ نیرومند دارد» و vāhara- را برساخته از *wasr̥ می‌داند. بارتولومه نیز در ستون ۷۸۸ همین را دارد: \"\n    \"«*vāhara- خنثی، برگرفته از vaŋhar-». در این صورت h (بازماندهٔ s هندوایرانی) و آ کشیدهٔ ستاک برجاست، درست همان‌گونه که wahār \"\n    \"فارسی میانه ایجاب می‌کند. ادعای نورایی درست است.\"),\n  sources=[W_BAHAR],\n  ref_check=[\n    {\"ref\":\"KNT:188\",\"status\":\"supports\",\"note\":\"KNT.txt leaf 211, which carries the printed page number '188': 'Θūravāhara- adj. \\\"Thuravahara\\\", second month, April-May: Elam. turmar, Akk. Ajaru.' Kent's grammar adds (leaf 69) 'Θūra-vahara- \\\"(Month) having vigorous spring-time\\\"' and (leaf 65, §154.I) 'vāhara- in Θūra-vahara- to *wasr̥'.\"},\n    {\"ref\":\"KNT:207\",\"status\":\"not_found\",\"note\":\"Leaf 231 of KNT.txt carries printed p.207, the v- stretch of the Lexicon ('-vā', vaina-, vau-, Vaumisa-, vaz-, vaj-), i.e. exactly where a cross-reference 'vāhara-, see Θūravāhara-' would stand; the OCR of that leaf is visibly truncated and no such line survives in it, so the second page number could not be confirmed from the text on disk.\"}],\n  consulted=[\n    {\"src\":\"BRT\",\"where\":\"AiW col. 788 (BRT.txt line 14301, leaf 449)\",\"stance\":\"supports\",\"note\":\"'Eig. \\\"die siegreiche Frühlingszeit\\\"; *vāhara- n., Ableit. … aus vaŋhar-.'\"},\n    {\"src\":\"HRN\",\"where\":\"Horn, Grundriss p.56 no.243\",\"stance\":\"supports\",\"note\":\"'ap. θūra-vāhara- (?)' listed first among the cognates of behār.\"},\n    {\"src\":\"ARY\",\"where\":\"Aryanpur p.138\",\"stance\":\"supports\",\"note\":\"'VAHARA (OLD PERSIAN)' in the cognate list under بهار.\"}])\n\nN(id=12, lang=\"Latin\", words=\"věr\",\n  verdict=\"transcription_suspect\",\n  derivation=(\n    \"The word and the derivation are right, the quantity mark is not: Latin is vēr, vēris n. 'spring' with a long e \"\n    \"(Pokorny 1174 'lat. ver, veris n. \\\"Frühling\\\"'; Watkins 'wesr̥. Spring. Latin vēr, spring (phonologically irregular)'; \"\n    \"de Vaan s.v. vēr *u̯esr, *u̯esnos). The book prints a breve, věr — I checked the printed page (pdf p.71) and the \"\n    \"extraction is faithful, so this is Nourai's own misprint. The phonology: *wesr̥ > Proto-Italic *wezor > with rhotacism \"\n    \"and loss of the final syllable Latin vēr, the compensatory lengthening giving the long vowel (Watkins calls the \"\n    \"development 'phonologically irregular' because *wesr̥ should rather have given *ver-); the oblique stem *wes-n- shows \"\n    \"up in the adjective vernus (*wes-r-i-no-).\"),\n  derivation_fa=(\n    \"واژه و ریشهٔ آن درست است، ولی نشانهٔ کمیت واکه نادرست: در لاتین vēr، vēris (خنثی) «بهار» با ای بلند است \"\n    \"(پوکورنی ص ۱۱۷۴؛ واتکینز: «wesr̥. Spring. Latin vēr»؛ د-وان ذیل vēr). کتاب «věr» با علامت کوتاه چاپ کرده است؛ تصویر صفحهٔ \"\n    \"چاپی را دیدم و استخراج درست بوده، پس خطای چاپی کتاب است. از نظر آوایی: *wesr̥ ← ایتالیک آغازین *wezor ← با ابدال s به r \"\n    \"(روتاسیسم) و افتادن هجای پایانی، vēr لاتینی با کشش جبرانی؛ ستاک غیرفاعلی *wes-n- در صفت vernus (*wes-r-i-no-) پیداست. \"\n    \"خطای چاپی کتاب است، نه خطای ریشه‌شناسی.\"),\n  sources=[E_VERN, W_WESR],\n  ref_check=[\n    {\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"Watkins 1985 (AHD_watkins1985.txt line 1164): 'wesr̥. Spring. Latin vér, spring (phonologically irregular): VERNAL; PRIMAVERA. [Pok. wes-r 1174.]' — Nourai's bare 'AHD' citation is right; the AHD appendix does put Latin vēr under this root. Note AHD does NOT put the root under aus-1.\"}],\n  consulted=[\n    {\"src\":\"POK\",\"where\":\"IEW 1174 (POK_03 leaf 418)\",\"stance\":\"supports\",\"note\":\"'lat. ver, veris n. \\\"Frühling\\\", vernus (*uerinos) \\\"auf den Frühling bezüglich\\\".'\"},\n    {\"src\":\"KLN\",\"where\":\"Klein s.v. vernal (KLN_1971.txt; 1966 ed. p.1702)\",\"stance\":\"supports\",\"note\":\"'L. vernalis … fr. vernus, of s.m., fr. ver, \\\"spring\\\".'\"},\n    {\"src\":\"IEC\",\"where\":\"Mann, IEC s.v. uesər- (1)\",\"stance\":\"supports\",\"note\":\"'Lat. ver, gs: veris, n. \\\"spring\\\"' — with the long vowel implied by the headword's gs form.\"}],\n  error_in=\"book\", book_prints=\"věr\", correct_form=\"vēr (vēris, n.)\")\n\nN(id=13, lang=\"English\", words=\"vernal\",\n  verdict=\"confirmed\",\n  derivation=(\n    \"English vernal is a 1530s learned borrowing of Late Latin vernālis 'of the spring', from Latin vernus 'of spring', \"\n    \"from vēr; the -al is the Latin adjective suffix, so the word never passed through French. Etymonline: \"\n    \"'vernal (adj.) \\\"of, pertaining to, or occurring in springtime\\\", 1530s, from Late Latin vernalis \\\"of the spring\\\", \"\n    \"from vernus \\\"of spring\\\", from Latin ver \\\"the spring, spring-time\\\" … reconstructed to be from PIE *wesr- \\\"the spring\\\" \"\n    \"(source also of … Persian bahar …)'. Klein's entry (the one Nourai cites at KLN:1702) is the same.\"),\n  derivation_fa=(\n    \"«vernal» انگلیسی وام‌واژه‌ای کتابی از دههٔ ۱۵۳۰ است، از لاتینی متأخر vernālis «بهاری» از vernus «بهاری» از vēr؛ پسوند -al \"\n    \"همان پسوند صفت‌ساز لاتینی است و واژه از راه فرانسه نیامده است. اتیمولاین همین را می‌گوید و می‌افزاید که ver لاتینی از \"\n    \"*wesr- هندواروپایی است، هم‌ریشه با «بهار» فارسی. ادعای نورایی درست است.\"),\n  sources=[E_VERN],\n  ref_check=[{\"ref\":\"None\",\"status\":\"not_checked\",\"note\":\"The node carries no reference in the book; it inherits KLN:1702 / AHD from its parent, both of which do give VERNAL as the English derivative of Latin vēr.\"}],\n  consulted=[\n    {\"src\":\"KLN\",\"where\":\"Klein s.v. vernal (KLN_1971.txt)\",\"stance\":\"supports\",\"note\":\"'vernal, adj., of, or pertaining to, spring. — L. vernalis … fr. vernus … fr. ver, \\\"spring\\\".'\"},\n    {\"src\":\"AHD\",\"where\":\"Watkins 1985 line 1164 and the English index (line 2449, 'VERNAL wesr')\",\"stance\":\"supports\",\"note\":\"VERNAL is listed as the English reflex of *wesr̥.\"}])\n\nN(id=14, lang=\"Germanic\", words=\"aust; Austrôn\",\n  verdict=\"confirmed\",\n  derivation=(\n    \"Proto-Germanic *aust- 'east', literally 'toward the sunrise', continues the *aus-t(e)ro- adverbial/directional formation \"\n    \"that Pokorny sets up on p.86 ('*aus-tero- \\\"östlich\\\"'), and *austrōn- is the dawn-goddess whose name the Anglo-Saxons \"\n    \"gave to the paschal month. Watkins: 'aus-1. To shine. 1. Germanic *aust- in: a. Old English east … 2. Germanic *austra- … \"\n    \"3. Germanic *austron-, a dawn-goddess whose holiday was celebrated at the vernal equinox, in Old English eastre, Easter.' \"\n    \"Pokorny p.87 has the same in German: 'germ. *austrō in ags. eastre \\\"Frühlingsgöttin\\\", eastron Pl. \\\"Ostern\\\" = ahd. \"\n    \"ōst(a)ra, ōstarūn'. Nourai's bare 'AHD' reference is therefore exact.\"),\n  derivation_fa=(\n    \"«*aust-» ژرمنی آغازین به معنای «خاور، سوی برآمدن خورشید» دنبالهٔ ساخت *aus-t(e)ro- است که پوکورنی در ص ۸۶ بازسازی کرده، و \"\n    \"*austrōn- نام ایزدبانوی سپیده‌دم است که انگلوساکسون‌ها نام او را بر ماه پاک (عید پاک) نهادند. واتکینز ذیل aus-¹ «درخشیدن» \"\n    \"همین را می‌آورد و پوکورنی در ص ۸۷ می‌نویسد: «ژرمنی *austrō در انگلیسی کهن ēastre \\\"ایزدبانوی بهار\\\" و ēastron \\\"عید پاک\\\" \"\n    \"برابر با ōst(a)ra آلمانی علیای کهن». ارجاع کوتاه نورایی به AHD دقیق است.\"),\n  sources=[E_EAST, E_EASTR],\n  ref_check=[\n    {\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"Watkins 1985, AHD_watkins1985.txt line 316: 'aus-1, To shine. 1. Germanic *aust- … 2. Germanic *austra- … 3. Germanic *austron-, a dawn-goddess whose holiday was celebrated at the vernal equinox, in Old English eastre, Easter … [Pok. aues- 86.]'\"}],\n  consulted=[\n    {\"src\":\"POK\",\"where\":\"IEW 87 (POK_01 leaf 95)\",\"stance\":\"supports\",\"note\":\"'germ. *austrō in ags. eastre \\\"Frühlingsgöttin\\\", eastron Pl. \\\"Ostern\\\" = ahd. ōst(a)ra, ōstarūn … anord. austr n. \\\"Osten\\\".'\"},\n    {\"src\":\"KLN\",\"where\":\"Klein s.v. east (1966 ed. p.495, KLN_1966.txt leaf 270 which bears the printed page 497)\",\"stance\":\"supports\",\"note\":\"'… fr. Teut. *austa-, \\\"east\\\", which is rel. to I.-E. *ausos, \\\"dawn\\\".'\"},\n    {\"src\":\"SYN\",\"where\":\"Buck 12.45 (p.870-871)\",\"stance\":\"supports\",\"note\":\"'ON austr, OE east, OHG ostan, etc., general Gmc., with various suffixes' listed under IE *aus-, *ausos-.\"}])\n\nN(id=15, lang=\"English\", words=\"east; Easter\",\n  verdict=\"confirmed\",\n  derivation=(\n    \"OE ēast (adv./adj.) 'east, eastward' > ME est > east; OE Ēastre (Northumbrian Ēostre), plural Ēastron, the name of \"\n    \"the month Ēastermōnaþ, was transferred by Anglo-Saxon Christians to the feast of the Resurrection, which is why English \"\n    \"and German alone among the western languages do not use a reflex of Latin Pascha (Bede, De temporum ratione, ch. 15). \"\n    \"Etymonline: 'Old English east, eastan … from Proto-Germanic *aust- \\\"east\\\", literally \\\"toward the sunrise\\\" … from PIE \"\n    \"root *aus- (1) \\\"to shine\\\", especially of the dawn'; and for Easter, 'from Eastre (Northumbrian Eostre), from \"\n    \"Proto-Germanic *austron-, \\\"dawn\\\", also possibly the name of a goddess whose feast was celebrated in Eastermonað'.\"),\n  derivation_fa=(\n    \"«east» از ēast انگلیسی کهن و آن از *aust- ژرمنی به معنای «سوی برآمدن خورشید» است؛ «Easter» از Ēastre (در گویش نورثامبریایی \"\n    \"Ēostre)، نام ماهی که بید (Bede) آن را به ایزدبانوی سپیده‌دم بازمی‌گرداند، که مسیحیان انگلوساکسون نام آن را بر عید رستاخیز \"\n    \"نهادند — و به همین سبب انگلیسی و آلمانی، برخلاف دیگر زبان‌های اروپای غربی، از واژهٔ Pascha لاتینی استفاده نمی‌کنند. \"\n    \"اتیمولاین هر دو را از ریشهٔ *aus- «درخشیدن (سپیده‌دم)» می‌گیرد. ادعای نورایی درست است.\"),\n  sources=[E_EAST, E_EASTR],\n  ref_check=[{\"ref\":\"None\",\"status\":\"not_checked\",\"note\":\"No reference printed on this node; it inherits the parent's 'AHD', where EAST and EASTER are the listed English derivatives of aus-1.\"}],\n  consulted=[\n    {\"src\":\"KLN\",\"where\":\"Klein s.v. east and Easter, 1966 ed. pp.495-497 (KLN_1966.txt leaf 270)\",\"stance\":\"supports\",\"note\":\"'east, n. — ME. east, est, fr. OE. east …'; 'Easter, n. — ME. ester, estern, fr. OE. easter, eastre … fr. OE. Eastre (usually in the pl. Eastron), a Teutonic goddess of spring (orig. the goddess of dawn)'.\"},\n    {\"src\":\"AHD\",\"where\":\"Watkins 1985 line 316\",\"stance\":\"supports\",\"note\":\"EAST and EASTER printed in caps as the English outcomes of aus-1.\"}])\n\nN(id=16, lang=\"Old High German\", words=\"ôstar\",\n  verdict=\"confirmed\",\n  derivation=(\n    \"OHG ōstar 'eastern, to the east' is the *aus-t(e)ro- comparative-directional adjective, the German counterpart of \"\n    \"ON austr and OE ēasterra. Pokorny p.87: 'dagegen mit idg. -t(e)ro-, ahd. ōstar \\\"östlich\\\" und \\\"nach Osten\\\", nhd. \"\n    \"Oster-reich'. Klein, s.v. Auster, spells the sequel out: 'OHG. ostar, \\\"to the east\\\" (whence ostar-rihi, G. Österreich, \"\n    \"\\\"Austria\\\")'. Nourai's box and its 'AHD' reference are sound (Watkins lists OHG ōstan under the same root).\"),\n  derivation_fa=(\n    \"«ōstar» آلمانی علیای کهن به معنای «خاوری، به‌سوی خاور» همان صفت جهت‌نمای *aus-t(e)ro- است، همتای austr نورس کهن و ēasterra \"\n    \"انگلیسی کهن. پوکورنی در ص ۸۷ می‌نویسد: «با پسوند هندواروپایی -t(e)ro-، ahd. ōstar \\\"خاوری\\\" … و از آن Oster-reich آلمانی». \"\n    \"کلاین نیز ذیل Auster می‌افزاید: «ōstar آلمانی … که از آن ostar-rihi، یعنی Österreich یا اتریش آمده است». ادعای نورایی درست است.\"),\n  sources=[E_AUSTR],\n  ref_check=[\n    {\"ref\":\"AHD\",\"status\":\"partial\",\"note\":\"Watkins 1985 line 316 lists under aus-1 'b. Old High German ōstan, east: OSTMARK' — the same root and the same German branch, but Watkins's headword is ōstan and his English derivative is OSTMARK, not Austria; the ōstar/Österreich step is Klein's and Pokorny's.\"}],\n  consulted=[\n    {\"src\":\"POK\",\"where\":\"IEW 87 (POK_01 leaf 95)\",\"stance\":\"supports\",\"note\":\"'ahd. ōstar \\\"östlich\\\" und \\\"nach Osten\\\", nhd. Oster-reich, anord. austr n. \\\"Osten\\\".'\"},\n    {\"src\":\"KLN\",\"where\":\"Klein s.v. Auster (1966 ed. p.130, KLN_1966.txt leaf 80)\",\"stance\":\"supports\",\"note\":\"'OHG. ostar, \\\"to the east\\\" (whence ostar-rihi, G. Osterreich, \\\"Austria\\\")'.\"}])\n\nN(id=17, lang=\"English\", words=\"Austria\",\n  verdict=\"plausible\",\n  derivation=(\n    \"The element is certainly OHG ōstar, but the English word did not come straight from Old High German: Austria is the \"\n    \"medieval Latin rendering of the German name. Etymonline: 'Austria … from Medieval Latin Marchia austriaca \\\"eastern \"\n    \"borderland\\\". German Österreich is \\\"eastern kingdom\\\", from Old High German ostar \\\"eastern\\\" … + reich \\\"kingdom\\\" … \"\n    \"So called for being on the eastern edge of Charlemagne's empire.' The oldest attestation of the German name is \"\n    \"Ostarrîchi in the diploma of Otto III, 996; the Latinised Austria (with au- for German ō-, on the model of Latin auster/ \"\n    \"australis) is first used in the 12th century and is what English borrowed. So Nourai's arrow is right in substance \"\n    \"but silently skips the Medieval Latin step in which the au- spelling arose.\"),\n  derivation_fa=(\n    \"جزء اصلی این نام بی‌گمان ōstar آلمانی علیای کهن است، ولی صورت انگلیسی Austria مستقیم از آلمانی نیامده، بلکه صورت \"\n    \"لاتینی‌شدهٔ سده‌های میانه است: اتیمولاین می‌گوید «Austria از لاتینی میانهٔ Marchia austriaca \\\"مرز خاوری\\\"؛ Österreich آلمانی \"\n    \"یعنی \\\"شهریاری خاوری\\\" از ōstar \\\"خاوری\\\" + reich \\\"کشور\\\"». کهن‌ترین گواه نام آلمانی، Ostarrîchi در فرمان اتوی سوم به سال ۹۹۶ \"\n    \"است و صورت لاتینی Austria (با au- به قیاس auster و australis لاتینی) از سدهٔ دوازدهم به کار رفته و همان است که انگلیسی وام \"\n    \"گرفته است. پس ادعای نورایی در اصل درست است ولی حلقهٔ لاتینی میانه را نادیده گرفته؛ با احتیاط پذیرفتنی است.\"),\n  sources=[E_AUSTR],\n  ref_check=[{\"ref\":\"None\",\"status\":\"not_checked\",\"note\":\"No reference on the node; the parent's 'AHD' does not list Austria (Watkins gives OSTMARK for the German branch).\"}],\n  consulted=[\n    {\"src\":\"KLN\",\"where\":\"Klein s.v. Auster (p.130)\",\"stance\":\"supports\",\"note\":\"'OHG. ostar … whence ostar-rihi, G. Osterreich, \\\"Austria\\\"' — Klein too goes straight from OHG to the modern name.\"},\n    {\"src\":\"POK\",\"where\":\"IEW 87\",\"stance\":\"supports\",\"note\":\"'nhd. Oster-reich' cited as a derivative of ahd. ōstar.\"}])\n\nN(id=18, lang=\"Latin\", words=\"australis; aurôra\",\n  verdict=\"confirmed\",\n  derivation=(\n    \"Both Latin words belong to this root, on the very page of Pokorny that Nourai cites for the root: 'lat. aurōra f. \"\n    \"\\\"Morgenröte\\\" (für *ausōsa); auster (*aus-t(e)ro- = germ. *austra-) \\\"Südwind\\\", austrālis \\\"südlich\\\"' (IEW 86-87). \"\n    \"aurōra is *ausōs-a with Latin rhotacism of intervocalic -s- (like flōs : flōra); austrālis is the -ālis adjective of \"\n    \"auster, itself the *aus-tero- 'eastern' formation. The semantic oddity - why an 'east' word means 'south wind' in Latin - \"\n    \"is old and acknowledged: Buck (12.48) and Ernout-Meillet explain it 'with shift through \\\"southeast\\\" explained by the \"\n    \"diagonal position of the axis of Italy', and Klein flags it too ('it is difficult to explain why L. auster denotes the \"\n    \"\\\"south wind\\\"'). Nourai's gloss 'southern (land)' therefore sits at the end of a real but slightly bumpy semantic path.\"),\n  derivation_fa=(\n    \"هر دو واژهٔ لاتینی در همان صفحه‌ای از پوکورنی که نورایی برای ریشه آورده جای دارند: «aurōra \\\"سپیده‌دم\\\" از *ausōsa؛ auster \"\n    \"(*aus-t(e)ro-) \\\"باد جنوب\\\"، austrālis \\\"جنوبی\\\"». در aurōra، سِ میان‌واکه‌ای بنا بر قاعدهٔ روتاسیسم لاتینی به ر بدل شده \"\n    \"(مانند flōs : flōra) و austrālis صفتِ -ālis از auster است. اینکه واژه‌ای به معنای «خاوری» در لاتین «باد جنوب» شده نکته‌ای \"\n    \"شناخته است: باک و ارنو-مییه آن را با کج‌بودن محور شبه‌جزیرهٔ ایتالیا و گذر معنایی از «جنوب‌خاوری» توضیح می‌دهند و کلاین هم آن \"\n    \"را دشواری می‌شمارد. پس معنای «جنوبی» در نمودار پایان راهی واقعی ولی پرپیچ‌وخم است. ادعای نورایی درست است.\"),\n  sources=[E_AUROR],\n  ref_check=[\n    {\"ref\":\"KLN:130\",\"status\":\"supports\",\"note\":\"KLN_1966.txt leaf 80, which carries the printed page numbers 130 and 131: 'austral, adj. southern; southerly. — L. australis, \\\"southern\\\", fr. auster, \\\"south wind\\\". See Auster …'; the Auster entry on the same page connects it to ON austr, OHG ostar, Avestic ushas-tara and OE east, 'see aurora'. Nourai's KLN:130 is exact.\"}],\n  consulted=[\n    {\"src\":\"POK\",\"where\":\"IEW 86-87 (POK_01 leaves 94-95)\",\"stance\":\"supports\",\"note\":\"'lat. aurōra f. \\\"Morgenröte\\\" (für *ausōsa); auster (*aus-t(e)ro- = germ. *austra-) \\\"Südwind\\\", austrālis \\\"südlich\\\"'.\"},\n    {\"src\":\"WLD\",\"where\":\"WP I 26-27 (WLD_Bd1_pages.txt leaf 35)\",\"stance\":\"supports\",\"note\":\"'lat. aurora \\\"Morgenrote\\\" (für *ausōs-, vgl. Flora : flos); auster \\\"Südwind\\\", australis \\\"südlich\\\" (zur Bed. s. Vf. LEWb.)'.\"},\n    {\"src\":\"SYN\",\"where\":\"Buck 12.48 SOUTH (SYN.txt line 22338)\",\"stance\":\"supports\",\"note\":\"'Lat. auster \\\"south wind\\\", also \\\"south\\\", prob. orig. \\\"east wind\\\" : ON austr, etc., \\\"east\\\" (12.45), with shift through \\\"south-east\\\" explained by the diagonal position of the axis of Italy. Walde-H. 1.87. Ernout-M. 94.'\"}])\n\nN(id=19, lang=\"English\", words=\"Australia; aurora\",\n  verdict=\"confirmed\",\n  derivation=(\n    \"aurora entered English in the late 14th century straight from Latin aurōra, first as the goddess and then as \"\n    \"'morning light, dawn' (Etymonline: 'aurora (n.) \\\"morning light, dawn\\\", late 14c., from Latin Aurora, the Roman goddess \"\n    \"of dawn, from PIE *ausus- \\\"dawn\\\" … from root *aus- (1)'); the scientific senses aurora borealis (1620s) and aurora \"\n    \"australis (1741) are modern Latin coinages. Australia is a 19th-century clipping of the cartographers' Terra Australis \"\n    \"(Incognita) 'the (unknown) southern land', popularised by Matthew Flinders in 1814 and made official in 1824 - Klein: \"\n    \"'Australia, n. — Lit. \\\"southern land\\\", fr. L. australis, \\\"southern\\\", in Terra Australis, \\\"the Southern Land\\\".' \"\n    \"Both are therefore direct Latin-to-English learned borrowings, exactly as the chart draws them.\"),\n  derivation_fa=(\n    \"«aurora» در اواخر سدهٔ چهاردهم مستقیم از Aurora لاتینی به انگلیسی آمد، نخست به‌عنوان نام ایزدبانو و سپس به معنای «روشنایی \"\n    \"بامداد، سپیده‌دم»؛ ترکیب‌های aurora borealis (۱۶۲۰) و aurora australis (۱۷۴۱) ساخته‌های لاتینِ نو هستند. «Australia» کوتاه‌شدهٔ \"\n    \"Terra Australis (Incognita) «سرزمین جنوبیِ ناشناخته» در نقشه‌های کهن است که متیو فلیندرز در ۱۸۱۴ رواج داد و در ۱۸۲۴ رسمی شد؛ \"\n    \"کلاین می‌نویسد: «Australia یعنی \\\"سرزمین جنوبی\\\"، از australis لاتینی در Terra Australis». پس هر دو وام‌واژهٔ کتابی مستقیم از \"\n    \"لاتین‌اند، درست همان‌گونه که نمودار نشان می‌دهد. ادعای نورایی درست است.\"),\n  sources=[E_AUROR, E_AUSTR],\n  ref_check=[{\"ref\":\"None\",\"status\":\"not_checked\",\"note\":\"No reference on the node; it inherits KLN:130, whose Australia entry stands on the same page (Klein p.130-131).\"}],\n  consulted=[\n    {\"src\":\"KLN\",\"where\":\"Klein s.v. Australia (1966 ed. p.130-131, leaf 80)\",\"stance\":\"supports\",\"note\":\"'Australia, n. — Lit. \\\"southern land\\\", fr. L. australis, \\\"southern\\\", in Terra Australis, \\\"the Southern Land\\\".'\"},\n    {\"src\":\"AHD\",\"where\":\"Watkins 1985 line 316 and etymonline's *aus- (1) list\",\"stance\":\"supports\",\"note\":\"'It might form all or part of: austral; Australia; Austria; Austro-; Aurora; east; Easter; eastern; eo-; Ostrogoth.'\"}])\n\nentry = {\n  \"entry\": 0,\n  \"root\": \"Aus 2, Awes, Ausus\",\n  \"verdict\": \"confirmed\",\n  \"modern_form\": \"PIE *h2ews- / *awes- 'to shine, become light', esp. of daybreak; derived s-stem *(a)us-os- 'dawn' (Pokorny aues-, IEW 86-87)\",\n  \"note\": (\n    \"The root box is right on all three counts. Pokorny's headword on the cited page is 'aues- \\\"leuchten\\\", bes. vom \"\n    \"Tagesanbruch; aus-, u̯es-, us-; (a)us-ōs- f. \\\"Morgenröte\\\"; *aus-tero- \\\"östlich\\\"' (IEW 86) - which also explains \"\n    \"Nourai's three-part name: 'Aus 2' and 'Awes' are Pokorny's own ablaut variants aus- / u̯es-, and 'Ausus' is the s-stem \"\n    \"*(a)us-ōs- that gives Latin aurōra and Greek ēōs. The language label 'Indo-European' and the gloss 'to shine; dawn' \"\n    \"match Pokorny, Walde-Pokorny (WP I 26f.), Watkins ('aus-1. To shine') and Wiktionary (*h2ews- 'to become light, to dawn', \"\n    \"alternative reconstruction *h2wes-) exactly. The only place where the chart goes beyond the consensus is the second \"\n    \"Indo-European box (#4, Wes 2/Wesr 'spring'): Pokorny and Klein connect the spring word to this root only with a hedge, \"\n    \"and Watkins and Wiktionary's main line keep them apart - see node 4. And the Sanskrit box #8 is simply wrong \"\n    \"(vihāra is 'monastery', from vi- + hṛ) - see node 8. Everything from #9 downward on that branch is nonetheless correct.\"),\n  \"note_fa\": (\n    \"خودِ ریشه از هر سه جهت درست است. سرواژهٔ پوکورنی در همان صفحه‌ای که نورایی ارجاع داده چنین است: «aues- \\\"درخشیدن\\\"، به‌ویژه \"\n    \"درخشیدن بامداد؛ گونه‌های aus-, u̯es-, us-؛ *(a)us-ōs- \\\"سپیده‌دم\\\"؛ *aus-tero- \\\"خاوری\\\"» (ص ۸۶). همین توضیح می‌دهد که چرا \"\n    \"نورایی سه نام آورده است: «Aus 2» و «Awes» همان گونه‌های اَبلاوتیِ aus-/u̯es- نزد پوکورنی‌اند و «Ausus» همان ستاک s-دار \"\n    \"*(a)us-ōs- است که aurōra لاتینی و ēōs یونانی از آن آمده‌اند. برچسب «هندواروپایی» و معنای «درخشیدن؛ سپیده‌دم» با پوکورنی، \"\n    \"والده-پوکورنی، واتکینز و ویکی‌واژه (*h₂ews- «روشن شدن، دمیدن») یکسان است. تنها جایی که نمودار از اجماع فراتر می‌رود جعبهٔ \"\n    \"دوم هندواروپایی است (گرهٔ ۴، «بهار»): پوکورنی و کلاین این پیوند را با قید «شاید» می‌پذیرند و واتکینز و ویکی‌واژه آن را \"\n    \"ریشه‌ای جدا می‌دانند. و جعبهٔ سنسکریت (گرهٔ ۸) به‌کلی نادرست است، زیرا vihāra یعنی «صومعه» از vi- + hṛ. با این همه، از گرهٔ ۹ \"\n    \"به پایین همان شاخه درست است.\"),\n  \"sources\": [W_AUS, E_EAST],\n  \"ref_check\": [\n    {\"ref\":\"POK:86\",\"status\":\"supports\",\"note\":\"POK_01.txt leaf 94 (the numeral '86' is printed on the leaf): 'aues- \\\"leuchten\\\", bes. vom Tagesanbruch; aus-, ues-, us-; (a)us-ōs- f. \\\"Morgenröte\\\"; *aus-tero- \\\"östlich\\\" … auso- \\\"Gold\\\".' Exactly Nourai's root, language and gloss.\"},\n    {\"ref\":\"KLN:495\",\"status\":\"supports\",\"note\":\"KLN_1966.txt leaf 270, which carries the printed page number 497 and holds the entries 'east' and 'Easter' (i.e. printed pp. 495-497): 'east, n. — ME. east, est, fr. OE. east … fr. Teut. *austa-, \\\"east\\\", which is rel. to I.-E. *ausos, \\\"dawn\\\", whence OI. usah, Gk. eos … L. auster, \\\"south\\\", aurum (for *ausom), \\\"gold\\\", aurora (for *ausosa), \\\"dawn\\\".' Nourai's page reference is right.\"}],\n  \"consulted\": [\n    {\"src\":\"WLD\",\"where\":\"Walde-Pokorny I 26-27 (WLD_Bd1_pages.txt leaf 35; the running head reads 'aus- 27')\",\"stance\":\"supports\",\"note\":\"The same root entry, with lat. aurora, auster, australis, aurum, mir. fair 'Sonnenaufgang', cymr. gwawr 'Morgenröte'.\"},\n    {\"src\":\"AHD\",\"where\":\"Watkins 1985, AHD_watkins1985.txt line 316\",\"stance\":\"supports\",\"note\":\"'aus-1, To shine. … 4. Probably suffixed form *ausōs-, dawn, also Indo-European goddess of the dawn, in: a. Latin aurōra, dawn: AURORA; b. Greek ēōs, dawn: EO-, Eos. [Pok. aues- 86.]'\"},\n    {\"src\":\"SYN\",\"where\":\"Buck, Selected Synonyms 12.45 EAST, pp.870-871\",\"stance\":\"supports\",\"note\":\"'IE *aus-, *ausos-, *usos-, etc., in words for \\\"dawn\\\" and \\\"east\\\", beside verb forms as Skt. ucchati, Av. usaiti \\\"lights up\\\" (esp. of the dawn), Lith. austi, Lett. aust \\\"to dawn\\\". Walde-P. 1.26f.'\"},\n    {\"src\":\"IEC\",\"where\":\"Mann, IEC (IEC.txt line 20148)\",\"stance\":\"partial\",\"note\":\"Mann's relevant headword is 'uesər- (1) … \\\"dawn, springtime\\\"', i.e. he unites the dawn and spring senses under one entry rather than deriving one from the other.\"}],\n  \"nodes\": nodes,\n}\n\nout = {\n  \"pdf_page\": 71,\n  \"book_page\": 41,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-05\",\n  \"entries\": [entry],\n}\n\np = \"/home/sfmqrb/git/rishe/data/verification/page-71.json\"\nwith open(p, \"w\", encoding=\"utf-8\") as f:\n    json.dump(out, f, ensure_ascii=False, indent=1)\nprint(\"wrote\", p, os.path.getsize(p), \"bytes,\", len(nodes), \"nodes\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build71.py",
 "description": "Build page-71 verification JSON"
}
```


### [2026-09-05T05:43:22.660Z] TOOL RESULT

```
wrote /home/sfmqrb/git/rishe/data/verification/page-71.json 67649 bytes, 19 nodes
```


## [2026-09-05T05:43:27.060Z] TOOL CALL #84: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -m json.tool data/verification/page-71.json > /dev/null && echo \"JSON OK\"; python3 tools/verify_check.py 71",
 "description": "Validate and run verify_check"
}
```


### [2026-09-05T05:43:28.863Z] TOOL RESULT

```
JSON OK
nodes verified: 19/19
node verdicts: {'confirmed': 12, 'plausible': 5, 'disputed': 1, 'transcription_suspect': 1}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 16, 'partial': 3, 'not_found': 1, 'not_checked': 4}
books consulted: {'supports': 41, 'partial': 6, 'silent': 4, 'contradicts': 1} | by book: {'POK': 7, 'KLN': 7, 'MON': 4, 'AHD': 4, 'IEC': 4, 'BRT': 3, 'WLD': 3, 'NYB': 3, 'HRN': 3, 'ARY': 3, 'PHD': 2, 'BQT': 2, 'SOD': 2, 'SYN': 2, 'HUB': 1, 'ISS_alt_DKS': 1, 'FSF': 1}
```


## [2026-09-05T05:43:33.705Z] TOOL CALL #85: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -c \"\nimport json\nd=json.load(open('data/verification/page-71.json'))\ne=d['entries'][0]\nprint('note_fa' in e, len(e['note_fa']))\nbad=[n['id'] for n in e['nodes'] if not n.get('derivation_fa') or not n.get('ref_check') or not n.get('consulted') or not n.get('derivation')]\nprint('missing fields on nodes:', bad)\nprint('sources present:', all(n.get('sources') is not None for n in e['nodes']))\n\"",
 "description": "Check required Persian and array fields"
}
```


### [2026-09-05T05:43:35.326Z] TOOL RESULT

```
True 876
missing fields on nodes: []
sources present: True
```


## [2026-09-05T05:43:51.779Z] AGENT

Page 71 (book p. 41) verified — `data/verification/page-71.json` written, `verify_check.py 71` shows 19/19 nodes, 0 PROBLEM lines.

**Counts** — root: 1 confirmed. Nodes: 12 confirmed, 5 plausible, 1 disputed, 1 transcription_suspect. Ref checks: 16 supports, 3 partial, 1 not_found, 4 not_checked (nodes with no printed refs). 41 supporting `consulted` entries across 17 books.

**Flagged items**
- **disputed — #8 Sanskrit `vihâra : spring`**: vihāra never means "spring"; it is vi- + √hṛ, "roaming; pleasure-ground; (Buddhist) monastery/temple", so it cannot hang from the *u̯es-r̥ "spring" box. Nourai has conflated the two Persian homonyms بهار "spring" (< MP wahār) and بهار "idol-temple" (< vihāra) — a distinction Mo'in keeps in both the Farhang-e Farsi and the very Borhan footnote (BQT:1452) Nourai cites. The onward chain #9 → #10 (Sogdian βrγʾr → farxār) is correct.
- **transcription_suspect — #12 Latin `věr`**: should be vēr, vēris (Pokorny 1174, Watkins, de Vaan). `error_in: book` — the printed page really shows the breve; the extraction is faithful.

**Notable "plausible" calls**: #4 (Aus 2 → Wes 2/Wesr) rests on Pokorny's "wohl zu aues-" (IEW 87 + 1174) and Klein's "possibly"; Watkins and Wiktionary's main line keep the two roots apart, though Lipp 2009's *h₂wósr̥ revives the link. #5 lists vasar/vasri as Avestan — they are the pre-Avestan forms (Pokorny: "*vasri für älteres *vasar"); only vaŋhar-/vaŋri (BRT col. 1347) are attested. #2/#3: MacKenzie and Nyberg read the Pahlavi as (u)š-bām, the h- being a Pazand prothesis; also the gloss "breakfast" for هوشبام is wrong (book's error) — it means سپیده‌دم only.

**Extraction issues for the owner**: none in the node data — I checked the 300 dpi render of pdf p. 71 against the JSON and every word, gloss, script form, ref and note matches. One minor omission: the chart draws an arrow from the Old Persian box (#11) to an **empty box** at the right, which the extraction dropped; it carries no language label or text in the book, so it is probably a layout artifact rather than lost content. Page image saved to `data/verification/sources/refs/ocr/BOOK/71.png`; 12 web pages archived via `fetch_source.py`.
