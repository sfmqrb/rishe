# Verification process log — verify-page-232


## [2026-09-06T15:28:35.745Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 232 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-232.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-232.json. Write /home/sfmqrb/git/rishe/data/verification/page-232.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 232` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T15:28:37.430Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T15:28:38.139Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T15:28:38.156Z] TOOL RESULT

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


## [2026-09-06T15:28:38.443Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-232.txt"
}
```


### [2026-09-06T15:28:38.463Z] TOOL RESULT

```
1	=== PDF page 232 (book page 202) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Kâd 1 : sorrow, hatred  (refs POK:517)
4	#1 (parent #0) [Avestan] refs=POK:517 | sâdra : pain, grief
5	  #2 (parent #1) [Persian] refs=BQT:1069; MON:1790 | sâr «سار ۲» : grief, pain
6	#3 (parent #0) [Germanic] refs=AHD | hatiz : hate
7	  #4 (parent #3) [English] refs=None | hate
8	--- entry 1 ---
9	ROOT [Indo-European] Kad 2 : to fall  (refs POK:516)
10	#1 (parent #0) [Latin] refs=POK:516; AHD | cadentia : a fall, a chance ; ob-cad-ere, occâsiô : to fall down as an opportunity, occasion
11	  #2 (parent #1) [French] refs=AHD | 
12	    #3 (parent #2) [Persian] refs=VOP:56,234 | čâns «شانس» : chance ; okâzîon «اکازیون» : opportunity
13	    #4 (parent #2) [English] refs=AHD | chance, occasion
14	#5 (parent #0) [Latin] refs=POK:516; AHD | cad-ere : to fall ; ad-cad-ere, accidere : to fall upon, accident ; in-cad-ere, incidere : to fall upon, incident ; casicare : to fall (cascade) ; de-cad-ere : to fall down, decay
15	  #6 (parent #5) [English] refs=AHD | accident ; incident ; cascade ; decay
16	--- entry 2 ---
17	ROOT [Avestan] Kafa : foam  (refs HRN:192; KGW:281)
18	#1 (parent #0) [Pahlavi] refs=MON:2997 | kaf : froth, foam
19	  #2 (parent #1) [Persian] refs=BQT:1658; MON:2997,3002 | kaf «کف» : foam, froth, lather ; kafč-lîz «کفچلیز» : a ladle for removing scum or foam from liquids | extra: کف آلود ، کفچ | NOTE: IEC:481 derives Persian "kofč: ladle" from Indo-European root "Kauks: shell, bowl, cup"
20	#3 (parent #0) [Sogdian] refs=SOD:199 | kwb : foam
21	
```


## [2026-09-06T15:28:41.067Z] AGENT

I'll read the source JSON and reference infrastructure.


## [2026-09-06T15:28:42.507Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-232.json",
 "description": "Read source JSON page 232"
}
```


### [2026-09-06T15:28:42.536Z] TOOL RESULT

```
{
  "pdf_page": 232,
  "book_page": 202,
  "entries": [
    {
      "root": {
        "name": "Kâd 1",
        "lang": "Indo-European",
        "refs": "POK:517",
        "gloss": "sorrow, hatred"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:517",
          "words": [
            {"translit": "sâdra", "gloss": "pain, grief", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:1069; MON:1790",
          "words": [
            {"translit": "sâr", "gloss": "grief, pain", "script": "سار ۲"}
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
            {"translit": "hatiz", "gloss": "hate", "script": null}
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
            {"translit": "hate", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Kad 2",
        "lang": "Indo-European",
        "refs": "POK:516",
        "gloss": "to fall"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Latin",
          "refs": "POK:516; AHD",
          "words": [
            {"translit": "cadentia", "gloss": "a fall, a chance", "script": null},
            {"translit": "ob-cad-ere, occâsiô", "gloss": "to fall down as an opportunity, occasion", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "French",
          "refs": "AHD",
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "VOP:56,234",
          "words": [
            {"translit": "čâns", "gloss": "chance", "script": "شانس"},
            {"translit": "okâzîon", "gloss": "opportunity", "script": "اکازیون"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 2,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "chance, occasion", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Latin",
          "refs": "POK:516; AHD",
          "words": [
            {"translit": "cad-ere", "gloss": "to fall", "script": null},
            {"translit": "ad-cad-ere, accidere", "gloss": "to fall upon, accident", "script": null},
            {"translit": "in-cad-ere, incidere", "gloss": "to fall upon, incident", "script": null},
            {"translit": "casicare", "gloss": "to fall (cascade)", "script": null},
            {"translit": "de-cad-ere", "gloss": "to fall down, decay", "script": null}
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
            {"translit": "accident", "gloss": null, "script": null},
            {"translit": "incident", "gloss": null, "script": null},
            {"translit": "cascade", "gloss": null, "script": null},
            {"translit": "decay", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Kafa",
        "lang": "Avestan",
        "refs": "HRN:192; KGW:281",
        "gloss": "foam",
        "note": "This is cognate with Sanskrit \"kapha\" and Russian \"kaplja: drops\""
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Pahlavi",
          "refs": "MON:2997",
          "words": [
            {"translit": "kaf", "gloss": "froth, foam", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:1658; MON:2997,3002",
          "words": [
            {"translit": "kaf", "gloss": "foam, froth, lather", "script": "کف"},
            {"translit": "kafč-lîz", "gloss": "a ladle for removing scum or foam from liquids", "script": "کفچلیز"}
          ],
          "script_extra": "کف آلود ، کفچ",
          "note": "IEC:481 derives Persian \"kofč: ladle\" from Indo-European root \"Kauks: shell, bowl, cup\"",
          "quote": {"text": "تو در این جوشش چو معمار منی - کفچلیزم زن که بس خوش میزنی", "poet": "Molavî"}
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Sogdian",
          "refs": "SOD:199",
          "words": [
            {"translit": "kwb", "gloss": "foam", "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
```


## [2026-09-06T15:28:42.965Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md | head -120",
 "description": "Read source matrix"
}
```


### [2026-09-06T15:28:43.006Z] TOOL RESULT

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
```


## [2026-09-06T15:28:48.451Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','AHD','BQT','MON','HRN','KGW','SOD','VOP','IEC','WLD','PHD','NYB','HUB','BRT','KLN','SKT','LEW','LAT','SYN','ARY','CHEUNG']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:600]); print()\n\""
}
```


## [2026-09-06T15:28:48.763Z] TOOL CALL #6: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo --- && head -60 data/verification/page-202.json"
}
```


### [2026-09-06T15:28:50.303Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

KGW {"title": "J. Ibrahim, Kulturgeschichtliche Wortforschung: Persisches Lehngut in europäischen Sprachen, Wiesbaden 1991", "edition_found": null, "kind": "google_books_preview", "url": "https://books.google.com/books?id=OUtZZNSUi3cC (partial preview) ; HathiTrust uc1.b3624504 search-only", "identifier": null, "local_file": null, "page_offset": null, "lookup_hint": "Google Books limited preview only (index pages).", "notes": "RE-SEARCH 2026-09: preview only (Google Books partial view usable for spot checks); no PDF on the author's site jamshid-ibrahim.net; purchase from Harrassowitz."}

SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id=

VOP {"title": "Mahshid Moshiri, Farhang-e Vazheha-ye Orupayi dar Farsi, Alborz 1371/1992", "kind": "none", "url": null, "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: not found (only unrelated similar-title books, e.g. Zomorrodian's فرهنگ ریشه‌شناختی واژه‌های دخیل اروپایی, ketabnak 132354).", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: nothing — no catalogue record with a scan, no ebook. Decoys: ketabnak 132354 (Zomorrodian), Google Books RwdkAAAAMAAJ (Nahid Shahidi 1997, no view). Purchase second-hand only."}

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-

NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves

LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt", "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f b

LAT {"title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951", "edition_found": "1951 (3rd ed.) - matches Nourai", "kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "identifier": "ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine (4th ed. 1959 lending-only: dictionnairetymo0000unse; another open copy: DictionnaireEtymologiqueDeLaLangueLatine)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt", "page_offset": "leaf = printed + 18 for mos

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 

CHEUNG null
```


### [2026-09-06T15:28:50.341Z] TOOL RESULT

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
---
{
 "pdf_page": 202,
 "book_page": 172,
 "verified_by": "claude-opus-5",
 "verified_on": "2026-09-05",
 "entries": [
  {
   "entry": 0,
   "root": "Gwa, Gwâ, Gwen 2",
   "verdict": "confirmed",
   "modern_form": "PIE *gʷem- 'to go, to come' (with the collateral root *gʷeh₂- / *gʷā- 'to step, go'); Pokorny IEW 463-465",
   "note": "Pokorny's entry, which begins on p.463 exactly as Nourai cites, is headed 'gʷā-, gʷem- „gehen, kommen; zur Welt kommen, geboren werden“; gʷm̥-ti-s f., gʷem-tu-s m. „Gang, Schritt“', and it is deliberately a double entry (I. gʷā-, II. gʷem-), which is why Nourai's box carries two names, 'Gwa, Gwâ'. His third name 'Gwen 2' reflects the *gʷem- > *gʷen- variant Pokorny himself notes ('Unthematisch *(e)-gʷem-t (> *e-gʷen-t)', and Latin advenam / veniō with -n- for -m-); it is not a separate root in any modern handbook, so it is Nourai's own labelling convenience rather than an error of substance. Watkins/AHD 1985 heads the same material 'gʷā-. Also gʷem-. To go, come'; Cheung splits it into *gaH¹ (PIE *gʷeh₂-, Pok. 463 f.) and *gam¹ (PIE *gʷem-, Pok. 464 f.). The gloss 'to walk, to step, to come, to go' is an accurate rendering. Two words in the chart do not belong to this root: Avestan 'gâv' in node 6 (a misprint) and 'thamân' in node 12 (an unidentifiable form), and one Persian word, nîyâm (node 3), is derived by modern scholarship from a different root (*ni-dā-, not *ni-gam-). Everything else on the page is standard, well-attested Iranian etymology.",
   "note_fa": "جعبهٔ ریشه درست است: پوکورنی در صفحهٔ ۴۶۳ فرهنگ خود مدخل «gʷā-, gʷem-» را با معنای «رفتن، آمدن؛ به جهان آمدن، زاده شدن» آورده و همان‌جا نام‌های gʷm̥-ti-s و gʷem-tu-s «گام، رفتار» را می‌افزاید؛ پس هر دو صورت «Gwa/Gwâ» و «Gwem» از یک مدخل‌اند و برچسب «هندواروپایی» و معنای «راه رفتن، گام برداشتن، آمدن، رفتن» درست است. نام سوم «Gwen 2» گونهٔ *gʷen- است که خود پوکورنی (در *e-gʷen-t و در veniō لاتین) یاد کرده و در کتاب‌های امروزی ریشهٔ جداگانه‌ای به شمار نمی‌رود؛ این نام‌گذاری از خود نورایی است نه خطای علمی. واتکینز (پیوست AHD) نیز همین ماده را «gʷā-, also gʷem-: رفتن، آمدن» آورده و چونگ آن را به دو ریشهٔ *gaH¹ و *gam¹ بخش کرده است. در سراسر این صفحه تنها سه لغزش هست: صورت «gâv» در گرهٔ ۶ (غلط چاپی)، صورت «thamân» در گرهٔ ۱۲ (صورتی که در هیچ فرهنگی یافت نشد) و واژهٔ «نیام» در گرهٔ ۳ که پژوهش امروزی آن را از ریشهٔ دیگری (*ni-dā-) می‌داند.",
   "sources": [
    "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/gʷem-"
   ],
   "ref_check": [
    {
     "ref": "POK:463",
     "status": "supports",
     "note": "POK_02.txt line 1790 (the leaf whose running numbers are 463-465): 'gʷā-, gʷem- „gehen, kommen; zur Welt kommen, geboren werden“; gʷm̥-ti-s f., gʷem-tu-s m. „Gang, Schritt“, Verbaladjektiv gʷm̥-to-s. I. gʷā-: ... 2. gʷem-: ...'. The same pages carry 'av. gātu-s „Ort, Liegerstatt, Sessel, Thron“, apers. gāθu- ds.', 'av. gā-man- n. „Schritt“', 'av. jantu (*gʷem-tu-)' and 'av. jasaiti „er geht“' — i.e. Pokorny 463 alone underwrites the root box and nodes 1, 2 and 6."
    }
   ],
   "consulted": [
    {
     "src": "WLD",
     "where": "Bd. I 675-677 (WLD_Bd1 djvu line 42665 ff., running head 'gʷem-, gʷā-')",
     "stance": "supports",
     "note": "'gʷem-, gʷā-' … 'ai. gātram „Glied, Körper“; ai. gātu- „Gang, Weg, Raum, Ort“, av. gātu-s „Ort, Platz; Liegerstatt, Sessel, Thron“, ap. gāθu … ai. vi-gāman- n. „Schritt“ … av. gāman- n. „Schritt“'. This is the source Pokorny 463 abridges (Buck cites it as 'Walde-P. 1.675 ff.')."
    },
    {
     "src": "AHD",
     "where": "Watkins 1985, g-list (AHD_watkins1985.txt line ~539)",
     "stance": "supports",
     "note": "'gʷā-. Also gʷem-. To go, come. 1. Germanic *kuman in a. Old English cuman, to come: COME … 3. Suffixed zero-grade form *gʷm̥-yo- in Greek bainein, to go, walk, step, with basis (< *gʷm̥-ti-), a stepping, tread, base'. Same double root, same gloss."
    },
    {
     "src": "CHEUNG",
     "where": "s.v. *gam¹ (CHEUNG.txt lines 7307, 7478) and *gaH¹ (line 7054)",
     "stance": "supports",
     "note": "'*gam¹ \"to come\" … «PIE *gʷem- “to go; come” = LIV: 209 f. | Pok.: 464 f.»'; and '«PIE *gʷeH₂- “to go, stride” = LIV: 205 | Pok.: 463 f.»'. Cheung's *gam¹ article lists, as its New-Persian outcome, exactly Nourai's harvest: 'NP zamān “time” … NP gām “step, pace” … NP āmadan … NP pay(g)ām “message”, NP pay(g)ambar … NP anjuman “company, assembly, club”'."
    },
    {
     "src": "SYN",
     "where": "Buck §10.47/10.48 (SYN.txt line 17514 f.)",
     "stance": "supports",
     "note": "'2. IE *gʷem-, *gʷā-. Walde-P. 1.675 ff. … Skt., Av., OPers. gam- \"go, come\" (Skt. gacchati, Av. jasaiti, sk̑o- presents like Grk. baskō; Av. jam- without prefix mostly \"come\"; also Av., OPers. ā-jam- \"come\", whence NPers. amadan \"come\")'."
    },
    {
     "src": "KLN",
     "where": "p.318 s.v. 'come' (KLN_1966.txt line 8320, page marker 318 at the foot)",
     "stance": "supports",
     "note": "'come … fr. I.-E. base *gʷem-, “to go; to come”, whence also OI. gámati, gacchati … Avestic jamaiti “goes” … Cp. the collateral base *gʷā- in OI. agām (aor.), Gk. ébēn (aor.), “I went”'."
    }
   ],
   "nodes": [
    {
     "id": 1,
     "lang": "Avestan / Old Persian",
     "words": "gam : to come, step; jam, jantu : to go",
```


## [2026-09-06T15:29:07.995Z] AGENT

Now let me research. Starting with the local reference texts.


## [2026-09-06T15:29:10.731Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK 517 area (kad) ===\"\ngrep -n \"Kummer, Hass\\|kād-\\|kad-.*fallen\\|k̑ad-\" POK_full.txt | head -30\necho \"=== POK_02 offset: leaf = p - 344 ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==173' POK_02.txt | head -80"
}
```


## [2026-09-06T15:29:11.725Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD kad ===\"\ngrep -n -i \"^kad-\\|kad-\\.\\| kad-\" AHD_watkins1985.txt | head -20\necho \"=== AHD kad 2 ===\"\ngrep -n -i \"sorrow, hatred\\|To fall\\.\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-06T15:29:12.495Z] TOOL RESULT

```
=== POK 517 area (kad) ===
=== POK_02 offset: leaf = p - 344 ===
t.  vester^ umbr.  uestra  ,vesträ';
apr.  wans  Akk.;  aksl.  Nom.  Akk.  PL  vy,  Gen.  PL  vas^,  Dat.  PL  varm^ In  Str.  PL  vami]
hitt.  su-(um-)me-es  (sumes)  aus  *Msm6  (vgl.  Pedersen  Hitt.  75 f.);
toch.  A  yas,  B  yes  (das  y  aus  der  1.  PL).
Daneben  mit  Anlaut  su :  air.  sl,  sissi  ,ihr'  (waz-i  ,von  euch'  u.  dgl.  aus *ö-s?/l),  cymr.  usw.  cMoi  ,ihr'  (das  -l  <  -*oi  vom  Nom.  PL  der  o-Stämme  ?) ; ir.  far  n.  ,euer',  indala-sär  ,der  eine  von  euch  beiden',  sethar  ,euer'  (vgl, Thurneysen  Gr.  §  449),  und  mit  Anlaut  esu-  got.  izwis  ,euch',  izwara ,euer',  aisl.  ydr,  yduar  ds.,  wgerm.  ohne  s  (d.  i.  wohl  mit  s-Schwund)  ahd. iuwih  ,euch'  (Akk.),  iuwer  ,euer'  usw. ;  vielleicht  ist  auch  gr.  acpo}  ,ihr beide'  nach  dem  Reflexivum,  wo  *oße-  durch  0(pB-  abgelöst  wurde,  an die  Stelle  eines  älteren  *(7/cü  getreten.
WP.  I  209  f.,  Trautmann  110,  364,  Schwyzer  Gr.  Gr.  I  600  f.
2.  iä  Ausruf,  bes.  Jauchzen.
Gr.  tctuot  ,juche!'  (iav,  tt),  It  , Interjektion  der  Verwunderung';  mit  sil- bischem, zum  Teil  langem  i-  (tw-)  reiht  sich  an  ^ivyri  , Jubel-  oder  Wehge- schrei', ivyiioQ  ds.,  ^LvC,(a  (Fut.  iv^vS)  ,schreie'  (Lit.  bei  Bezzenberger  BB. 27,  164  f.,  der  auch  auf  lit.  yvas  ,Nachteule',  apr.  ywo-garge,  Eulenbaum' und  auf  das  w-Präs.  ivvExav  ■Alalei,  ödvQExai  Hes.  verweist);  nicht  hierher, sondern  zu  1.  au  (oben  S.  71)  gehört  d^tri  ,Schrei',  da  älter  inschr.  äJ^vtä]
\aLt.  jübilö  ,jauchze,  jodle'  (vielleicht  *iüd-dhd-lö  ,mache  jü');  dazu  im^ö,, -ere  ,Ruf  der  Gabelweihe' ;
mir.  ilach  (*iiuluko-)  , Siegesjubel' ;
mhd.  jü,  jüch  ,Ausruf  der  Freude'  (ähnlich  jö  beim  Aus-  und  Zuruf)^ davon  mhd.  jüwen,  jüwezen  ,ju  rufen,  jubeln',  jüchezen,  nhd.  jauchzen^ juchzen,  mhd.  jölen,  jodeln,  nhd.  johlen,  jodeln,  auch  anord.  yla,  engl,  yowl ,heulen'  aus  *jüljan'^
seih,  jü,  ijü,  ijuju  ,juchhe!';
lit.  yvas  ,Nachteule'  s.  oben.
WP.I  210,  WH.  I  725  ff.
K,  K.
icä-  ^gern  haben^  begehren^;  kä-ro-  ,lieb,  begehrlich^;  aus  *kä-mo-  ,Ver- langen^  entstand  schon  idg.  kam-  ^begehren^
Ai.  käyamäna-  ^gern  habend^  {ä-käyiya-  ^begehrenswert^  mit  aus  diesem lo-Präsens  verschlepptem  -y-),  Perf.  cakt  ,sich  woran  erfreuen,  lieben, begehren^,  -käti-  (in  Kompos.)  ^heischend,  verlangend^;  av.  kä-  ^wonach verlangen^  (kayä  1.  Sg.,  käta--^  öakuSe)'^
-wo-St.  ai.  käma-  m.  ,Begehren,  Wunsch,  Liebe^,  av.  apers.  käma-  m. ^Verlangen,  Wunsch^;
kam-  in  ai.  kämdyati,  Part.Perf.Med.  caka
```


### [2026-09-06T15:29:12.562Z] TOOL RESULT

```
=== AHD kad ===
561:kad-. To fall. Latin cadere, to fall, die: CADAVER, CA- DENCE, CADENT, CADUCOUS, CASCADE, CASE!, CHANCE, CHUTE; ACCIDENT, CADUCICORN, DECAY, DECIDUOUS, ESCHEAT, INCIDENT, OCCASION, RECIDIVISM. [Pok. 1. kad- 516.]
562:kad-. Sorrow, hatred. Suffixed zero-grade form *kad-i- in: a. Germanic *hatiz in Old English hete, hate, envy (> Middle English hate): HATRED. b. Germanic *haton in Old English hatian, to hate: HATE; c. Germanic *hatjan in Old French hair, to hate: HEINOUS. [Pok. kdd- 517.]
1208:ABAFT apo- ABANDON bha-2 ABASE bassus ABASH bat- ABASIA gWa- ABATE battuere ABBREVIATE mregh-u- ABDICATE deik- ABDUCENS deuk- ABDUCT deuk- ABELE albho- ABERRATION ers-1 ABET bheid- ABEYANCE bat- ABHOR ghers- ABIDE bheidh- ABJECT yé- ABJURE yewes- ABLATION  tele- ABLAUT apo-, kleu-1 ABLE ghabh- ABLUTION leu(@)- ABNEGATE ne ABNORMAL gné- ABODE bheidh- ABOLISH al-3 ABORT er-! ABOUND wed-1 ABOUT ud- ABOVE upo ABRADE réd- ABRIDGE mregh-u- ABROGATE reg-1 ABROSIA gWere-4 ABRUPT reup- ABSCESS ked- ABSCISE kae-id- ABSCOND dhé-1 ABSENT eS- ABSOLUTE leu-1 ABSOLVE feu-1 ABSORB srebh- ABSTAIN ten- ABSTRACT tragh- ABSTRUSE treud- ABSURD swer-2 ABULIA gWele-1 ABUT bhau- ABYSS gWadh- ACANTHO- ak- ACANTHOPTERYGIAN pet- ACANTHUS ak- ACAPNIA kwép- ACCEDE ked- ACCELERATE kel-3 ACCENT kan- ACCEPT kap- ACCESS ked- ACCIDENT kad- ACCIPITER Oku- ACCLAIM kele-2 ACCLIVITY klel- ACCOLADE kwel-1 ACCOMMODATE med- ACCOMPLISH pele-1 ACCORD kerd-1 accosT kost- ACCOUNT peu- ACCRUE_ ker-3 ACCUMBENT keu-2 ACCUMULATE keue-2 ACCURATE cira ACERATE ak- ACERB ak- ACETABULUM ak- ACETIC ak- ACETUM = ak- ACHALASIA ghé-
1328:CABARET kamer- CABEZON kaput CABLE kap- CABRILLA kapro- CABRIOLET kapro- CACHE ag- CACHEXIA segh- caco- kakka- CACODYL kakka- CACOETHES kakka-, s(w)e- CACOPHONOUS bha-2, kakka- CACOPHONY kakka- CACUMINAL keu-2 CADASTER  steigh- CADAVER kad- CADELLE kat-1 CADENCE kad- CADENT kad- CADET kaput CADRE kWetwer- CADUCEUS kar-2 CADUCICORN kad-, ker-1 CADUCOUS kad- CAECILIAN kaiko- CAECUM kaiko- CAELUM_ kae-id- CAESURA kae-id- CAGE keua-2 CAHIER kWetwer- CAINOTOPHOBIA ken-3 CAIRD kerd-2 CAISSON kap-
1335:-CARPOUS kerp- CARPUS kwerp- CARRION sker-1 CARROT ker-1 CARRY kers-2 CART ger-2 CARUNCLE = sker-1 CARVACROL ak- CARVE gerbh- CASCADE kad- CASCARA kwét- CASE! kad-
1342:CENTROBARIC gWere-2 CENTUM dekm CENTURY dekm CEPHALIC ghebh-el- CEPHALO- ghebh-el- -CEPHALOUS ghebh-el- CERAMIC ker-4 CERASTES ker-! CERATODUS dent-, ker-1 CERATOID ker-! CEREAL ker-3 CEREBELLUM ker-1 CEREBRUM ker-1 CERES ker-3 CERTAIN krei- CERVINE ker-1 CERVIX ker-1 CESSION ked- CESSPOOL spirare cEsTus! kent- CEsTUS? kae-id- CHAETA ghait- CHAETOGNATH genu-2, ghait- CHAFE dhé-1, kele-1 CHAFER gep(h)- CHAFF! gep(h)- CHAIR sed-1 CHALAZA gheled- CHALAZION gheled- CHALCID ghelegh- CHALCOCITE ghelegh- CHALCOPYRITE ghelegh- CHALCOsIS ghelegh- CHALICE kal-1 CHALLENGE kel-8 CHALONE ghé- CHAMAEPHYTE dhghem- CHAMBER kamer- CHAMELEON dhghem- CHAMFER bhreg- CHAMFRON kaput CHAMOMILE dhghem-, mélon CHANCE kad- CHANCEL carcer CHANCELLOR carcer CHANCRE kar-1 CHANGE skamb- CHANT kan-
1357:CHOLE- ghel-2 CHOLER ghel-2 CHOLERA ghel-2 CHOLESTEROL ster-1 CHOLINERGIC werg- CHOLLA g(e)u-lo- CHONDRO- ghrendh- CHONDROMALACIA mel-1 CHOOSE geus- CHORAGUS_§ ag-, gher-1 CHORAL gher-1 CHORALE gher-1 CHORD? ghere- -CHORE ghé- CHORIC gher-1 CHORION ghere- CHORISTER gher-! CHOROGRAPHY ghé- CHORUS gher-1 CHOWDER kele-1 CHRESARD gher-5 CHRESTOMATHY gher-5, mendh-1 CHRISM ghréi- Curist ghréi- CHRISTEN ghréi- CHRISTIAN ghréi- CuRIsTMas ghréi- CHROMA ghréu- CHROMATIC ghréu- CHROMATO- ghréu- -CHROME ghréu- CHROMIUM ghréu- CHROMO- ghréu- CHROMONEMA (s)né- CHRONAXY ag- CHRYSANTHEMUM § andh- CHTHONIC dhghem- CHUFA swei-! CHUKAR kau-! CHUKKER kwel-1 CHURCH keue-? CHURL karlaz CHUTE kad-
1414:DEAN dekm DEATH dheu-3 DEBACLE _bak- DEBASE bassus DEBATE battuere DEBAUCH bhelg- DEBENTURE ghabh- DEBILITATE bel- DEBILITY bel- DEBIT ghabh- DEBONAIR deu-2 DEBOUCH beu-1 DEBRIS bhréi- DEBT ghabh- DECA- dekm DECADE dekm DECAGON dekm DECALESCENCE kele-! DECALOGUE Ieg-* DECANAL dekm DECANT kanto- DECAPITATE kaput DECAY kad- DECEASE ked-
1416:DECEIVE kap- DECEMBER dekm DECEMVIR dekm, wi-ro- DECENARY dekm DECENNIUM at-, dekm DECENT dek-! DECI- dekm DECIDE kae-id- DECIDUOUS _ kad- DECIMAL dekm DECIMATE dekm DECK! (s)teg- DECK? (s)teg- DECKLE (s)teg- DECLAIM kele-2 DECLARE kele-2 DECLINE klei- DECLIVITY kKlei- DECOCT pekw- DECOLLATE! kWwel-1 DECOLLETE kwel-1 DECOR dek-! DECORATE dek-1 DECOROUS dek-1 DECORTICATE sker-1 DECOY keue-2, to- DECREASE ker-3 DECREE krei- DECREPIT ker-2 DECREPITATE ker-2 DECUMBENT keu-2 DECUPLE dekm, pel-3 DECURRENT kers-2 DECUSSATE dekm DEDANS en DEDICATE deik- DEDUCE deuk- DEDUCT deuk- DEED dhé-1
1477:ERYTHEMA reudh-! ERYTHRO- reudh-1 ESCALADE skand- ESCAROLE ed- ESCHATOLOGY eghs ESCHEAT kad- ESCUDO skei- ESCULENT ed- ESCUTCHEON skei- ESOTERIC en ESPARTO sper-2 ESPECIAL spek- ESPERANCE spé-! ESPIONAGE spek- ESPOUSE spend- ESPY spek- ESQUIRE skei- ESSAY ag- ESSENCE es- ESSONITE sék- ESTABLISH sta- ESTANCIA sta- ESTER ak- EsTHER  ster-3 ESTRONE eis-1 ESTRUS eis-1 ESTUARY aidh- ESURIENT ed- ETCETERA eti, ko- ETCH ed- ETERNAL aiw- ETESIAN wet-2 ETHER aidh- ETHIC s(w)e- ETHMOID sé-3 ETHNIC s(w)e- ETHNO- s(w)e- ETHOS s(w)e- ETIOLOGY ai-! ETIQUETTE steig- EU- esu- EUCALYPTUS kel-2 EUCARYOTE kar-1 EUCHARIST gher-5 EUGLENA gel-2 EUMENIDES men-1 EUNUCH segh- EUONYMUS n6-men- EUPATRID peter- EUPEPTIC pekw- EUPHEMISM bha-2 EUPHONY bha-2 EUPHORIA bher-1 EUPHROSYNE gWhren- EUPNEA pneu- EUREKA were-2 EuRUS eus- EURY- were-1 EUuRYDICE deik-, were-1
1579:HAG2 kau-2 HAGGARD kagh- HAGGLE kau-2 HAGIO- yag- HAIL! kaghlo- HAIL? kailo- HAKE keg- HALBERD bhardha, kelp- HALE! kailo- HALE? kele-2 HALF skel-1 HALIBUT bhau- HALL kel-2 HALLOW kailo- HALO-  Sal-1 HALT! kel-3 HALT? kel-1 HALTER! kelp- HALTER? § sel-4 HAM konemo- HAMADRYAD deru, sem-! HAME_ tkei- HAMLET tkei- HAMMER ak- HANDIWORK kom HANDSEL sel-3 HANG konk- HANKER konk- HANUMAN genu-2 HAP kob- HAPLESS kob- HAPLOID pel-3, sem-1 HAPPEN kob- HAPPY kob- HARANGUE koro- HARBINGER koro- HARBOR koro- HARD kar-1 HARDS_ kes-! HARDY! = kar-1 HARE kas- HARM kormo- HARMONY ar- HARNESS _nes-1 HARPOON  serp-1 HARPSICHORD ghere- HARQUEBUS keg- HARRY koro- HART ker-1 HARTEBEEST ker-1 HARUSPEX ghere- HARVEST kerp- HASH! =skep- HASLET ghasto- HASTATE ghasto- HAT kadh- HATCHET skep- HATE kad- HATRED ar-, kad- HAUBERK kWel-1 HAUGH kel-2 HAUGHTY al-3 HAUL kele-2 HAULM kolem- HAUNT tkei- HAUSTELLUM aus-2 HAUSTORIUM aus-2 HAUTBOY al-3, busk- HAVE kap- HAVEN kap- HAW2 kagh- HAWK! kap- HAWKER keu-2 HAWSE kWel-1 HAWSER al-3 HAY kau-2 HAZEL koselo- HE! ko-
1587:HEEL? kel-4 HEGEMONY sag- HEIFER per-3 HEIGHT keu-2 HEINOUS kad-
1676:INCIDENT kad- INCINERATE keni- INCIPIENT kap- INCISE kae-id- INCITE kei-3 INCLINE klei- INCLUDE kleu-3 INCONDITE dhé-1 INCREASE ker-3 INCUBATE keu-2 INCULT kWwel-1 INCUMBENT keu-2 INCUNABULUM kei-1 INCUR kers-2 INCUS kau-2 INDEMNIFY dap- INDEMNITY dap- INDENT! dent- INDENTURE dent- INDEX deik- INDICATE deik- INDICT deik- INDIGEN gene- INDIGENOUS gene- INDIGENT eg- INDIGN dek-1 INDIGNANT dek-1 INDIGNATION dek-1 INDITE deik- INDOLENT del-3 INDOMITABLE deme-2 INDUCE deuk- INDURATE deru INDUSTRY en, ster-2 INEBRIATE 6g¥h- INEFFABLE bha-2 INELUCTABLE leug-1 INEPT ap-1
1952:OBEY au-5 OBFUSCATE dheu-1 OBITUARY el-1 OBJECT! yé- OBJURGATE ag-, yewes- OBLAST epi, wal- OBLATE! tele- OBLIGE leig-1 OBLITERATE deph- OBLIVION lel- OBLONG del-1 OBLOQUY tolkw- OBNOXIOUS nek-1 OBOE busk- OBSCURE (s)keu- OBSEQUIOUS sekw-1 OBSERVE ser-! oBsEss sed-1 OBSTACLE sta- OBSTETRIC sta- OBSTINATE sta- OBSTREPEROUS §strep- OBSTRUCT ster-2 OBTAIN ten- OBTECT (s)teg- OBTEST trei- OBTRUDE treud- OBTUND (s)teu- OBVERT wer-3 oBvious wegh- OBVOLUTE wel-3 OCARINA awi- OCCASION kad- occipuT kaput OCCLUDE kleu-3 occuLT kel-2 occupy kap- occur kers-2 OCELLUS okWw- OCHLOCRACY wegh- OCHLOPHOBIA wegh- OCTAD okto(u) OctTans okt6(u) OCTANT oktd(u) OCTAVE okt6d(u) OcTAvO okt6(u) OCTENNIAL at-
2174:REBUT bhau- RECALESCENCE kele-! RECANT kan- RECAPITULATE kaput RECEDE ked- RECEIVE kap- RECENSION kens- RECENT ken-3 RECIDIVISM kad- RECIPROCAL pert RECISION kae-id- RECK reg-1 RECKLESS reg-! RECKON reg-1 RECLAIM kele-2 RECLINE klei- RECLUSE kleu-3 RECOGNIZE gnd- RECOIL (s)keu- RECOMMEND man-2 RECONDITE dhé-1 RECORD kerd-1 RECOURSE kers-2 RECOVER kap- RECREANT kerd-1 RECREMENT krei- RECRIMINATE  krei- RECRUDESCE kreud-! RECRUIT ker-3 RECTANGLE reg-1 RECTIFY dhé-1, reg-1 RECTILINEAR reg-1 RECTITUDE reg-!
=== AHD kad 2 ===
561:kad-. To fall. Latin cadere, to fall, die: CADAVER, CA- DENCE, CADENT, CADUCOUS, CASCADE, CASE!, CHANCE, CHUTE; ACCIDENT, CADUCICORN, DECAY, DECIDUOUS, ESCHEAT, INCIDENT, OCCASION, RECIDIVISM. [Pok. 1. kad- 516.]
562:kad-. Sorrow, hatred. Suffixed zero-grade form *kad-i- in: a. Germanic *hatiz in Old English hete, hate, envy (> Middle English hate): HATRED. b. Germanic *haton in Old English hatian, to hate: HATE; c. Germanic *hatjan in Old French hair, to hate: HEINOUS. [Pok. kdd- 517.]
850:p(h)ol-. To fall. Suffixed form *phol-no- in Germanic *fallan in: a. Old English feallan, to fall: FALL; b. Ger- manic causative *falljan, “to cause to fall,” strike down, in Old English fellan, fyllan, to cut down: FELL; c. Ger- manic compound *bi-fallan, to fall, happen (*bi-, by, at; see ambhi), in Old English befeallan, to fall: BEFALL. [Pok. phél- 851.]
```


## [2026-09-06T15:29:21.123Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"kädy\\|kad-\\|kād\\|Kummer.*Ha[sß]\\|fallen\" POK_02.txt | sed -n '1,40p'"
}
```


### [2026-09-06T15:29:21.173Z] TOOL RESULT

```
108:lit.  geibüs  .plump,  ungeschickt',  geibstü,  geibti  .schwach  werden,  um- sinken, verenden';  dazu  mit  Anlautsvariante  gu  nach  Trautmann  KZ.  42, 372:  lit.  gvaibstü,  ^uaii^z  .ohnmächtig  werden,  in  Ohnmacht  fallen',  intens. gvdibeti?]  lett.  (mit  dissimilatorischem  Schwund  des  u  vor  5.  oder  Ent- lehnung aus  dem  Litauischen?  s.  Mühlenbach-Endzelin  I  582.  695.  698) gibstu,  gibt  .einsinken,  sich  senken,  sich  bücken',  geibstu,  gkibt  .umkommen, sterben'.  geXba  .Schwindel,  ungeschickter,  schwächlicher  Mensch',  galba .Törin'.
323:lett.  gUmstu,  gümt  , greifen;  überfallen',  reflex.  ,sich  biegen';  lit.  gümulas, gumulys,    gümuras    (daneben    giib-)    ,Klumpen,    Kugel,    Knäuel',    o-stufig  - gämalas   (daneben  gab-)    , Schneeballen,   Stück  Brot,   Fleisch';   Entlehnung aus    dem    Poln.    ist    für    lit.    gumulis,    gumule    ,Bock,    Kuh   ohne  Hörner
585:Auf  idg.  -k  sicher  anord.  krä  ,Ecke,  Winkel'  (*kraidho)  und  wahrschein- lich auch  die  germ.  Formen  auf  -g:  anord.  kringr  m.  ,Ring'  =  mhd.  krinCj -ges  ,Ring,  Kampfplatz',  nlid.  Kring^  anord.  kringla  , Kreisring,  Zirkel', mnd.  kringel{e)  ,Ring,  rundes  Gebäck',  mhd.  kringel  (und  ablautend krengel)  ds.,  nhd.  Kringel]  mhd.  kranc,  -ges  ,Kreis,  Ring,  Bezirk',  nhd. Schweiz,  chrangel  ,Krümmung',  mhd.  krangel  ,Not,  Drangsal'  (aus  , Ver- wicklung, Krümmung')  und  ;Ring,  Kreis' ;  anord.  cranga  ,kriechen,  sich schleppen',  mit  übertragener  Bed.  krangr  ,schwach,  gebrechlich';  ags. cringan  , fallen';
588:auf  idg.  -g:  ags.  cranc-staf  ,ein  Webergerät',  crencestre  ^Weberin^  °ieng|, crinkled  .gedreht^  engl,  crinkle  ^Biegung/  Krümmung,  Falte^  crank ^Krümmung'  (wie  nhd.  Schweiz,  chrank),  älter  auch  cranke  ,Garnwickel', mndd.  krunke  ,Falte,  Runzel,  Krause^  holl.  kronkel  ,Falte',  Ä:HnÄ:eZ  ,Schlinge| Falte,  Runzel',  norw.  krenkja  ,verrenken';  mit  der  Bed.-Entw.  zu  ^^q^ Krankheit  gebeugt':  ahd.  krankolön  ,straucheln,  schwach  werden',  m}i^^ krank  ,schmal,  gering,  schwach',  nhd.  krank,  ags.  cranc  ^schwächlich,  ge- brechlich', sowie  ags.  crincan  ,im  Kampfe  fallen'  (,*sich  im  Todeskampfe krümmen') ;
650:morsch,  altert',  Partiz.  jürnd-^  jlimd-  ,geb rechlich,  abgelebt,  abgenutzt, zerfallen,  morsch,  alt' ;  av.  azardsant-  ,nicht  alternd'  (Partiz.  des  s-Aor.), azardma-  ,nicht  abnehmend'  (von  *zardma-  m.  ,das  Verkommen'),  zairina- , aufreibend,  erschlaffend',  zardta-  ,altersschwach'  (wohl  =^  ai.  "^jirta-)^  mit formantischem  u  (:  gr.  yQav(;?  anord.  kor,  s.  u.)  zaurvan-  m.  , Greisenalter, Altersschwäche',  zaurura-  , altersschwach,  gebrechlich',  vielleicht  auch zrvan- :  zrnn-  ,Zeit'  ;
652:gr.  ysQCüv  , Greis'  {yiqovT-),  ysgovoLog  ,den  Geronten  zukommend',  yeQOv- oia  , Ratsversammlung  (der  Ältesten)^,  yiqag  n.  (idg.  *gerd-s,  von  der schweren  Basis)  ursprüngl.  ,*  Alter,  *  Altersvorrecht',  daher  , Ehrengabe, Ehrenstellung,  Belohnung',  yegagög  , ehrwürdig,  stattlich,  ansehnlich',  später auch  ,alt,  greisenhaft'^  ysgaiög  ,alt'  wohl  aus  *y€Qa(T-t6g',  in  der  Bed. jAlter'  ist  yegag  ersetzt  durch  y^gag]  das  r]  von  yrjgdayco)  ^altere'^,  Partiz. Präs.  yrjgdg  .alternd^,  themat.  Impf,  eyrigä,  usw.  auf  yrjgag  (für  yegag)  über- tragen, ebenso  auf  yiqgau)  ,altere,  reife',  yvjgaXiog  (bei  Hes.  auch  yegaleog) ,alt';  att.  ygavg,  Gen.  yga{*f)6g  (hom.  Dat.  ygrj'C)  ,alte  Frau'  (hom.  ygr/vg wohl  spätere  Umschrift  eines  richtigen  *}grj{ß)Lg  nach  dem  gewöhnlichen ygavg) ;  vielleicht  in  Beziehung  zu  av.  zaurvan-  m.  , Greisenalter',  etwa ursprüngl.  Nom.  ^ger-us  :  Gen.  *g^rd-u-6s,  woraus  ygafog ;  s.  Schwyzer  Gr. Gr.  1,  574;  redupl.  ysgyegiixog  ,von  selbst  abfallende  oder  reife  Feige  oder Olive'  (s.  oben);
774:Ai.  jö$ati,  jusdte  ^kostet,  genießt,  liebt',  ^*ösa?/a^e  ,findet  woran  Vergnügen', jösa-h  , Zufriedenheit,  Billigung,  Genüge',  av.  zaos-^  apers.  daus-  , Geschmack woran  finden',  av.  zaosö  , Gefallen',  zustö  ,beliebt,  erwünscht' ;  khotan- sak.  ysäsde  ,er  schätzt',  ysua,  ysuyän  {ys  =  z)  , Leckerei' ;
932:über  auffallende  Übereinstimmungen  der  ir.  Komposita .  mit  gaib-  mit den  lat.  Zusammensetzungen  von  habere  s.  Pedersen  KG.  H  532 ;
1159:afries.  gadia  ^vereinigen',  mnd.  gaden  (*gadön)  ,passen,  gefallen,  sich gatten',  ahd.  bigatön^  mhd.  gaten,  gegaten  intr.  ,zusammenkommen,  so  daß es  zusammenpaßt',  trans.  , Gleiches  zu  Gleichem  gesellen,  zusammenbringen', refl.  ,sich  fügen',  ahd.  gi-gat  ,passend',  as.  gi-gado  ^seinesgleichen',  ags. (gejgada  , Genosse,  Gatte',  nhd.  Gatte;  got.  gadiliggs  ,Vetter',  as.  gaduling ,Verwandter',  ags.  gcedeling  ^Genosse',  ahd.  gatulinc,  gatilinc  , Verwandter, Vetter,  Geselle';  ags.  geador,  tö  gcedere  (engl,  together)  ,zusammen'^  afries. gadur,  mnd.  gader,  mhd.  gater  ds.,  ags.  gadrian^  gced(e)rian  (engl,  gather) ,sammeln',  afries.  gaderia^  mnd.  gad(d)eren  ds.,  mhd.  vergatern  ,sich  vereini- gen', nhd.  vergattern  ds.;  dazu  vermutlich  auch  ahd.  gataro,  nhd.  Gatter (umgelautet  mhd.  geter,  nhd.  Gitter),  aschwed.  gadder,  mnd.  gaddere  , Gitter';
1161:aksl.  god^  ,Zeit^  rechte  Zeit',  godina  ,äQa%  godhm  ,gefällig'_,  russ.  godnyj ,tauglich',  aksl.  u-goditi  ,gefallen',  russ.-ksl.  goditi  ds.,  ksl.  ugoda  ^Wohl- gefallen', russ.  vygoda  ,Vorteil',  aksl.  negodovati  ,unwillig  sein',  iter.  aksl.
1163:ugozdo,  ugoHiti  ,es  einem  recht  machen,  gefallen'   (usw.,  Berneker  317^ wo  auch   über  die  poln.  Lehnworte  lit.  gädas  ^Vereinig-ung-'^  gädijtis  ^ ereignen,  treffen'  u.  a.).  ?^'
1166:hierher  (vgl.  Van  Windekens  Lexique  32)  toch.  AB  kätk-,  erweictj[ A  käck-^  B  käcc-  ,sich  erfreuen'  (vgl.  oben  mnd.  gaden  ,gefallen');  ändert Pedersen  Toch.  172.
1228:lit,  äpmandq  giezti  , Groll  hegen',  gieziüos  , heftig  verlangen',  pagiezti ,nach  Rache  verlangen',  pagiezä  , Rachgier';  falls  lit.  giezti,  pa- giezti  intr. ,im  Halse  kratzen'  damit  identisch  wäre,  müßte  obige  Zusammenstellung fortfallen.
1270:Ablautsstufe  '^ghU-  in  aisl.  glämr  ,Mond',  glämsyni  , optische  Täuschuno- Illusion',  schwed.  glämig  , graugelb  im  Gesicht,  mit  eingefallenen  Augen' aisl.  glxr  ,hell'  (*gleia  =  lit.  zlejä  unten).
1318:Ags.  glldan  , ausgleiten,  fallen',  glidder  , schlüpfrig',  afries.  glida  , gleiten', as.  glldan  ,labi',  ahd.  glltan  , gleiten' ;  ags.  a-glxdan  , gleiten  machen', asäch.  hi-gUdian  ds.,  aisl.  gleidr  , spreizbeinig'.
1449:I.  gher-  ,begehren,  gern  haben*,  z.  T.  mit  Formen  von  einer  Basis  *ghere{iy :  gheri-  (s.  Persson  Beitr.  728). Ai.  hdryati  ,findet  Gefallen,  begehrt';  av.  zara-  m.  »Streben,  Ziel'; gr.  xa/^w  {*xccQi-(o),  xccQrj^ca  ,sich  freuen*,  xciQig  f.  ,Anmut,  Gunst*,  x<XQ(^ »Freude*,  x^^QOuog  ,Kampfesfreude  blitzend',  x^Ql^a  n.  ,Freude,  Vergnügen* ;
1738:lit.  gramü,  grameti  ,mit  Gepolter  fallen*,  grumiü,  grumeti  , donnern', grumenü,  grumenti  , dumpf  dröhnen,  murren,  drohen*;  mit  Erweiterung -zd-  (s.  Persson  Beitr.  349)  grumzdziü,  gruihsti  ,knirschen,  knarren,  drohen' ; lett.  gremjii,  gremt  , murmeln,  im  Affekt  reden,  drohen,  grollen*,  apr. grumins  m.  ,ferner  Donner*,  grtmons  ,gesungen*,  grimikan  , Liedchen* ;
1759:lat.  ingruö,  -ere  ,mit  Heftigkeit  hereinstürzen,  hereinbrechen',  congrua^ -ere  »zusammenfallen,  zusammentreffen';
1760:lit.    griäuju,    grioviau,    griduti    ,niederbrechen    (trans.    intr.);    donnern* (iau  aus  eu;  daraus  das  r  von:)  griüvü  {griy,vü,  Trautmann  100),  griuvaü griüti  ,zusammenf allen,  in  Trümmer  fallen*  (griüvü  =  lat.  -gruö  aus  ^ghruuö)'^    ' lett.  ^J^aw;w,  grävu,  gi^aut  ,zertrümmern',  grüstu,  gruvu,  grut  ,einstürzen*,  ■ gfuveli  m.  PI.  , Schutt';  Anlautdoublette  neben  qreu-  (s.  dort)?
1761:Russ.  dial.  grüchnuth  sa  ,mit  Geräusch  zusammenstürzen',  klr.  hrüchnuty jpoltern;  krähen',  skr.  grühäm,  gruhati  ,krachen',  sloven.  grüh  , Stein- geröll', grusa  ,grober  Sand,  Schotter',  poln.  gruchnqc  , ertönen ;  mit  Krachen hinfallen;  fest  schlagen'  {gruchac  ^girren  wie  die  Taube*  malt  hingegen sicher  den  Girrlaut).
1919:vermutlich  zu  vereinigen  unter  ,fallen  lassen',  intr.  ,herabfallen' ;  nach
1927:In  vermittelnder  Bedeutung  (etwa  aus  .in  sich  zusammenfallen')  al glä-ti,  gldyati  .fühlt  sich  erschöpft,  ist  verdrossen,  schwindet'.  Partiz.  gländ- gläna-m,  gläni-h  .Erschöpfung.  Abnahme'.  Kaus.  gTäjpdyati  .erschöpfen jmd.  zusetzen;  in  Verfall  kommen  lassen'?
1931:toch.  AB  klä-  .fallen'.  Van  Windekens  Lexique  40.
2177:gr.  ep.  (pMvoiy  att.  q)d-tvu)  (^cpS-ivfWy  s.  oben)  , vernichte',  meist  intr. ,schwinde  hin,  gehe  zugrunde',  cp^ivv-d-o)  , schwinde  hin,  mache  verschwin- den', Fut.  q)d'hao)  (att.  di7to(pd-taw)j  Aor.  eifdsiaa  (att.  SLTtecpd-Xaa),  icpd-t(.iriv^ qi&ffxsvog  ,vernichten',  Pass.  , zugrunde  gehen',  Partiz.  Perf.  Pass.  q}&LTÖg, (pd-ÖT}  , Schwindsucht',  (pd-laig  ds.  (s.  oben  ) ;  über  vielleicht  alte  Doppel- formen, wie  ipiv€G&aLj  xpiva^siv  , Blüten  oder  Früchte  abfallen  lassen,  ver- lieren', xpLGig'  dnwXeia  Hes.,  u.  dgl.  s.  Schwyzer  Gr.  Gr.  I  326.
2230:lett.  zveVu,  zveVu,  zvelt  ,wälzen,  fortbewegen,  umwerfen ;  schlagen',  refl. ,sich  schwerfällig  fortbewegen,  sich  wälzen,  umfallen',  zvalstities  ,wanken, schwanken',  zvatns  ,sch wankend';
2602:Beruht  ar.  kan-  (ai.  Perf.  cäkana^  Aor.  akänisam,  av.  cakana),  can-  (ai.  cani- stdm'y  ai.  cänas-  n.  ,Gefallen,  Befriedigung',  av.  canah-,  cinah-  ,y erlangen. Heischen')  ,befriedigt  sein.  Gefallen  finden',  av.  cinman-  n.  ,Begehren, Trachten'  auf  einem  idg.  -(e)wes-St.  k-e-nes-?  Die  Formen  cani-j  kani- können  ebenso  sekundär  sein  wie  kami-syate,  -tar-  neben  käma-  (wenn Stokes  KZ.  40,  246  mit  Recht  mir.  ein,  Gen.  cena  , Liebe,  Zuneigung'  als *kenu-  vergliche,  wäre  k-en-  :  kä-  wie  ks-en-  :  kes-  u.  dgl.  zu  beurteilen).
2625:1.  kad-  ,f allen'.
2626:Ai.   sad-,  Perf.   sasäda,   Fut.  satsyati  , abfallen,   ausfallen'^  (:  lat.  cado)\
2627:arm.  cacnum  (*kadio-)  .fallen,  niedrig  werden';
2628:lat.  cadö,  -ere  , fallen'  (osk.  antkadum?  s.  WH.  I  128);  cadäver  n.  , Leiche* als  , Gefallenes'  (*kadä-ues)]  cadücus  , hinfällig';
2629:air.  casar  f.  , Hagel;  Blitz'  (*kad-t-ara),  PI.  cymr.  cesair  , Schloßen',  corn. keser,  bret.  kazerch  .Hagel'.
2631:2,  kad-  ,glänzen,  prangen,  sich  auszeichnen'.
2640:käd-  :  k9des-  :  kod-s-   ,seelische  Verstimmung;    Kummer,  Haß*;   kädos- , Sorge,  Leid'.
2725:Vielleicht  lit.  kankü,  käkti  , wohin  gelangen,  genügen,  hinreichen' (Reihenwechsel?);  unsicher  auch  ags.  hagan  ,genitalia',  mhd.  Äa^ew  , Zucht- stier', nhd.  dial.  hegel  ds.,  haksch  , Zuchtschwein',  nhd.  hecken  ,sich  paaren (von  Vögeln)',  engl,  hatch  ,hrüten',  ahd.  hegi-diniosa  ,Hode'.  Ebenso,  weil  nie -Ä-,  sondern  nur  -g-  im  Wurzelauslaut,  die  germ.  Sippe  aisl.  hagr  ,passend, geschickt',  liagr  m.  ,Lage,  Vorteil,  Wohlstand',  haga  , anordnen',  högr, hegr  ,passend,  bequem',  hättr  (*hahtu-)  ,Art  und  Weise'  (wäre  «w-St. neben  dem  ^i-St.  ai.  sakti-),  ahd.  st.  Partiz.  ki-hagan,  bihagan  ,heiter', mhd.  behagen  ,passen,  recht  sein',  nhd.  behagen,  mhd.  hage  m.  , Behagen, Wohlgefallen',  as.  bihagön  , behagen,  gefallen',  ags.  onhagian  ,passen,  be- hagen', gehagian  unpers.  , Gelegenheit  sein' ;  unter  Annahme  von  ausl.  -gh- vergleicht  Zupitza  Gutt.  104  sie  mit  prakr.  ca{y)ati  ,ist  fähig',  A9oka- Inschr.  caghati  ,ist  zu  etwas  bereit,  willig',  av.  cagdd-  (mit  rafdördm) , Hilfe  gewährend',  cagdman-  n.  , Geschenk',  cagvah-  ,bietend,  gewährend', die  freilich  w^iederum  in  ihrem  e-Vokalisraus  nicht  so  unmittelbar  zum germ,  a  :  ö  stimmen ;
2932:gall.  catu-  , Kampf  in  GN  Catu-rlx  , Schlachtenkönig',  air.  cath  , Kampf; Truppe,  Schar',  qymr.  cad  ds.,  corn.  cas  m.  ,Kampf';  cymr.  cadr(*kat-ro-) , stark',  abret.  cadr,  mbret.  kazr^  nbret.  kaer  ,schön';  cymr.  cadarn  , stark', bret.  kadarn  ,tapfer';  dazu  auch  nach  Loth  RC  42,  84  f.  cymr.  cadw  m, , Truppe,  Schar'  (^katuo-),  als  Verb  »bewahren,  schützen';  abrit.  Mars Belatu-cadros  enthält  hingegen  die  Wurzel  kad-  , glänzen' ; ■  aisl.  Jiod  f.  ,Streit'  (=  gall.  catu-),  GN  Hgdr,  got.  MN  Theuda-hatha-8, ags.  headu-,  ahd-  hadu-  , Kampf  in  Namen  wie  Hadu-mär,  Hedwig]  mhd. Jiader  ,Zank,  Streit';
3013:alb.  q^oj  , wecke,  erwecke'  (*kien{ö)j  qoj  , schicken,  senden'  (*ds-köj\ cys,  cyt  , reize,  necke'  (*ter-k{u-t-{ö),  syei^  syen  (*kiu-n-iö)  ,bestürmen,  an- fallen' (Jokl  Mel.  Pedersen  149 f.');
3079:keid-  ,fallen';  nur  kelt.  und  germ.
3080:Cymr.  cwyddo,  di-gwyddo  ,fallen,  sich  ereignen',  cwydd  ,Fall',  bret. koezaff  , falle',  di-gouezout  ,sich  ereignen' ;
3081:aisl.  hitta  d  ,treffen',  hitta  i  ,hineingeraten',  dän.  hitte  paa  ,auf  etwas verfallen',  schwed.  hitta  ,finden',  mengl.  (aus  dem  Nord.)  hittan  ,auf  etwas treffen,  finden',  engl,  hit  (ursprüngl.  ,auf  etwas  fallen,  verfallen'?).
3658:4.  ker-  und  kero-i  kre-  , versehren';  intr.  ,zerfallen,  vermorschen*.  "-'
```


## [2026-09-06T15:29:22.537Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor n in 172 173 174 175; do echo \"===== leaf $n =====\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N' POK_02.txt | grep -n \"kad\\|käd\\|kad\\b\\|sädra\\|hatis\\|Ha[sß]\\|fallen\" | head -20; done"
}
```


### [2026-09-06T15:29:24.317Z] TOOL RESULT

```
===== leaf 172 =====
===== leaf 173 =====
===== leaf 174 =====
4:Beruht  ar.  kan-  (ai.  Perf.  cäkana^  Aor.  akänisam,  av.  cakana),  can-  (ai.  cani- stdm'y  ai.  cänas-  n.  ,Gefallen,  Befriedigung',  av.  canah-,  cinah-  ,y erlangen. Heischen')  ,befriedigt  sein.  Gefallen  finden',  av.  cinman-  n.  ,Begehren, Trachten'  auf  einem  idg.  -(e)wes-St.  k-e-nes-?  Die  Formen  cani-j  kani- können  ebenso  sekundär  sein  wie  kami-syate,  -tar-  neben  käma-  (wenn Stokes  KZ.  40,  246  mit  Recht  mir.  ein,  Gen.  cena  , Liebe,  Zuneigung'  als *kenu-  vergliche,  wäre  k-en-  :  kä-  wie  ks-en-  :  kes-  u.  dgl.  zu  beurteilen).
17:Ai.  kadana-  n.  .Vernichtung',  cakäda  (unsicher,  ob  nicht  cakära?)  kada^
===== leaf 175 =====
4:via)  Hes.;  ycddvQog'  Y,dTtQog  ^voq%LQ  Hes. WP.  I  341.  WH.  I  128 ;   vgl.  unten  käd-.
5:kadh-^  ,hüten,  schützend  bedecken*.
6:Lat.  cassis,  -idis  ,Helm'  (wenn  echtlat.,  s.  WH. 1 177,  dann  aus  ^^kadh-tis); vielleicht  mir.  cais  , Liebe',  mis-cuis  ,Haß'  (^kadh-ti-s) ;
9:1.  kad-  ,f allen'.
10:Ai.   sad-,  Perf.   sasäda,   Fut.  satsyati  , abfallen,   ausfallen'^  (:  lat.  cado)\
11:arm.  cacnum  (*kadio-)  .fallen,  niedrig  werden';
12:lat.  cadö,  -ere  , fallen'  (osk.  antkadum?  s.  WH.  I  128);  cadäver  n.  , Leiche* als  , Gefallenes'  (*kadä-ues)]  cadücus  , hinfällig';
13:air.  casar  f.  , Hagel;  Blitz'  (*kad-t-ara),  PI.  cymr.  cesair  , Schloßen',  corn. keser,  bret.  kazerch  .Hagel'.
15:2,  kad-  ,glänzen,  prangen,  sich  auszeichnen'.
22:abrit.  Belatu-cadrus  Beiname  des  ,Kriegsgottes'??  Umbildung  eines  *katros ^tapfer'  (vgl.  kat-  , kämpfen')  zu  kadros  wäre  freilich  nicht  ganz  ausge- schlossen.
24:käd-  :  k9des-  :  kod-s-   ,seelische  Verstimmung;    Kummer,  Haß*;   kädos- , Sorge,  Leid'.
26:av.  sädra-  n.  ,Leid,  Wehe,  Unheil'  (Geldner  KZ.  27,  24
```


## [2026-09-06T15:29:28.159Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==175' POK_02.txt | sed -n '1,60p'"
}
```


### [2026-09-06T15:29:29.901Z] TOOL RESULT

```
   berauben^.   X6xct-
dfjaai '  ßXäxpai,  xay,cüaaL,  atSQfjaaL  Hes..  in  medial-pass.  Bed.  hom.  'Asxddovzo
.sie  wichen*",  ixsx^ydfif  (Konjektur)   v7ts{v.s)xojQi^y.et   Hes..  ä7iOY.adkü'  dad-s-
via)  Hes.;  ycddvQog'  Y,dTtQog  ^voq%LQ  Hes. WP.  I  341.  WH.  I  128 ;   vgl.  unten  käd-.
kadh-^  ,hüten,  schützend  bedecken*.
Lat.  cassis,  -idis  ,Helm'  (wenn  echtlat.,  s.  WH. 1 177,  dann  aus  ^^kadh-tis); vielleicht  mir.  cais  , Liebe',  mis-cuis  ,Haß'  (^kadh-ti-s) ;
ags.  hcßdre  , sorglich,  ängstlich' ;  ahd.  huota  f.  ,die  Hut,  Obhut,  Bewachung', ags.  höd,  afries.  höde  , Obhut',  wovon  ahd.  huoten,  ags.  hedan  , behüten, bewachen';  ahd.  huot  m.  ,der  Hut,  Haube,  Helm',  ags.  höd  m.  ,Kappe*; aisl.  hqttr  und  hattr,  ags.  hcett,  engl,  hat  ,der  Hut'  {*had-tu-),  aisl.  hetta ,Kappe'  i^hattjön-) '^  Kluge  u.  Hw^,  Zupitza  Gutt.  206f. ;  ags.  heden  ,dress* =  aisl.  hedinn  ,Pelzrock'  (*hadina-).
WP.  I  341  f..  WH.  I  177.
1.  kad-  ,f allen'.
Ai.   sad-,  Perf.   sasäda,   Fut.  satsyati  , abfallen,   ausfallen'^  (:  lat.  cado)\
arm.  cacnum  (*kadio-)  .fallen,  niedrig  werden';
lat.  cadö,  -ere  , fallen'  (osk.  antkadum?  s.  WH.  I  128);  cadäver  n.  , Leiche* als  , Gefallenes'  (*kadä-ues)]  cadücus  , hinfällig';
air.  casar  f.  , Hagel;  Blitz'  (*kad-t-ara),  PI.  cymr.  cesair  , Schloßen',  corn. keser,  bret.  kazerch  .Hagel'.
WP.  I  339  f.,  WH.  I  127  f.
2,  kad-  ,glänzen,  prangen,  sich  auszeichnen'.
Ai.  Perf.   iäsadüh,    Partiz.    säsadäna-    ,sich  auszeichnen,    hervorragen*;
gr.  Perf.  xinaa^ai,  Plusqpf.  iy^ycda^rjVj  Partiz.  v^xaaiisvog  (Hom.  Aiscb.)
,sich  auszeichnen',   xexaö^og  (Pind.)   ,prangend',  KdartoQ  eigentlich  ,der
517
Glänzende'  (?),  KaoTi-avsLqa  , unter  Männern  ausgezeichnet',  usw. ;  dazu %ä(jri.oQ  m.  , Biber'  mit  Übertragung*  des  GN  wegen  der  Heilwirkung  des Bibergeils:  xaGTÖqiov  (>  ai.  kastüri  f.  , Moschus') ;  Präs.  xairv^ai  scheint Neubildung  nach  daivviJLaL'^
vielleicht  mir.  cä(i)d  ,heilig',  wozu  gall.  caddos  ,sanctus'  C.  Gl.L.  V493,  30;
abrit.  Belatu-cadrus  Beiname  des  ,Kriegsgottes'??  Umbildung  eines  *katros ^tapfer'  (vgl.  kat-  , kämpfen')  zu  kadros  wäre  freilich  nicht  ganz  ausge- schlossen.
WP.  I  340.
käd-  :  k9des-  :  kod-s-   ,seelische  Verstimmung;    Kummer,  Haß*;   kädos- , Sorge,  Leid'.
Ai.  ri-sädas-  ,für  den  Fremden  sorgend' ;
av.  sädra-  n.  ,Leid,  Wehe,  Unheil'  (Geldner  KZ.  27,  24
```


## [2026-09-06T15:29:35.117Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==175' POK_02.txt | sed -n '24,45p'\necho \"===== leaf 176 head =====\"\nawk 'BEGIN{RS=\"\\f\"} NR==176' POK_02.txt | sed -n '1,12p'"
}
```


### [2026-09-06T15:29:36.949Z] TOOL RESULT

```
käd-  :  k9des-  :  kod-s-   ,seelische  Verstimmung;    Kummer,  Haß*;   kädos- , Sorge,  Leid'.
Ai.  ri-sädas-  ,für  den  Fremden  sorgend' ;
av.  sädra-  n.  ,Leid,  Wehe,  Unheil'  (Geldner  KZ.  27,  24
===== leaf 176 head =====
2 f.);
gr.  Tifjöog  n.,  dor.  ytadog  , Sorge,  Trauer;  Leichenbestattung;  Familien- gefühl', y.rjöiarog  ,der  liebste',  ^i^dsLog  ,der  Sorge  wert,  lieb;  zur  Bestattung gehörig;  blutsverwandt',  xrjdeGTrjg,  kret.  ytäöeGTäg  , Heiratsverwandter', ytrjSsvo)  ,besorge,  pflege;  bestatte;  verschwägere',  Krjdef^cüv  »Beschützer; Leichenbestatter;  Heiratsverwandter',  X7]da)  , mache  besorgt,  betrübe'^  auch , verletze,  schädige' ;  äKrjdrjg  , unbesorgt,  unbestattet'^  wovon  äy.Tjdsa)  , ver- nachlässige' ;
osk.  cadeis  amnud  ^inimlcitiae  causa   (:  nhd.  Haß^  Kern  KZ.  21,  242);
mir.  caiss,  cymr.  cas,  bret.  cas  ,Haß'  (^kdds-i-  als  Weiterbildung  des -es-St.  von  got.  hatis)]  cymr.  caiodd  ,offensa,  ira,  indignatio'  corn.  cuetJi, mbret.  cuez,  nbret.  keuz  (*kädo-s)  ,Leid,  Trauer' ;
'  got.  hatis  n.  ,Haß,  Zorn',  anord.  Jiatr  n.,  ags.  Jiete  m.,  as.  heti  m.,  ahd. haz  m.  ,Haß'  z.  T.  auch  in  Verfolgung  ausartend,  daher  die  Bed.  ,ver- folgen'  von  anord.  hata,  as.  häton  z.  T.  auch  ahd.  Jiazzön,  vgl.  auch  ahd. hetzen  aus  *hatjan]  für  eine  Grundbed.  ,verfolgen'  der  Wz.  sagen  die germ.  Verhältnisse  nichts  aus ;   ablaut.  as.  hoti  , feindlich' ;
toch.  A  kat  , Zerstörung'.
WP.  I  340  f.,  vgl.  oben  kUd-.
kago-  oder  kogo-,  -ä-  .Ziege';  nur  slav.  und  germ.
Abg.  koza  ,Ziege',  kozbh  , Ziegenbock'  (lett.  kaza  , Ziege'  aus  dem  Russ.), davon  abgel.  koza  ,Haut'  (^kozjä,  ursprüngl.  ,*Ziegenfell',  wie  ksl.  (J)azno ,Haut,  Leder' :  lit.  ozys  , Ziegenbock');
auf  die  Bed.  , (Ziegen)  feil  als  Überwurf  geht  wahrscheinlich  auch  got. liakuls  ,Mantel*,  aisl.  hgkoll  ds.  (fem.  hekla  ,Mantel  mit  Kapuze'),  ags. hacele,  afries.  hezü  (*hakir),  ahd.  hachul  m.  ds.  zurück;  mit  Dehnstufe wahrscheinlich  ags.  hecen,  mnd.  Jiöken,  mndl.  hoekijn  , Zicklein'  (*hökina-).
518
Meillet  Et.  246  erinnert  an  *agos  ,Ziege(nbock)'  (oben  S.  6  f.)  als .Reimwort',  was  für  kago-  mit  a  spräche.  Die  geringe  Verbreitung  des Wortes  erklärt  sich  aus  der  Menge  damit  im  Wettbewerb  stehender Ziegennamen,  s.  dazu  Liden  Arm.  St.  13  f.
```


## [2026-09-06T15:29:50.103Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== WLD Bd1 kad / kād ===\"\ngrep -n \"kād-\\|käd-\\|kad- .fallen\\|sādra\\|sädra\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -20\necho \"=== BRT sadra ===\"\ngrep -n \"sāδra\\|sadra\\|sädra\\|sadra-\" BRT.txt | head -20"
}
```


### [2026-09-06T15:29:50.164Z] TOOL RESULT

```
=== WLD Bd1 kad / kād ===
=== BRT sadra ===
6252:—  amintaitl  *s'aanS  urvä  also  (sd.)  uta- yBtä  yä  rura^  sädra  (sd.)  dr?gvatB  Y.45.
13753:duäsKsadra-
18686:n>r)sasärahya'Y.2g.q;—y/ln)rqi{kV.) sadra  (sd.)  dngvats  Y,45.7;  zit  Vr.JiS2, G.3.6  undP.^.ü',  wo  nar/'**;  —  yönari dngvatä  urva  H.  2.  25,  a6,  33;  Nik.  3, Vd.  13,  75;  —  besonders  häufig  mit  asa- van- (Sp.  250  na.;  s.  auch  Sp.  1047  m,, 1049  o.):  yat  ba  paiti  nä  asava  nmansm uzdasia  y.3.2;  1,  Yt/0.  lao,  11.3;  — yetihe  ''nmävya  srao^S ..näca  aSava  fräyS.- kumats  Y.57. 14;  —  ydi  narS  afavanB kumataiS  mainimna  ..  Y.  70.  4;  V.ig.ig, 34,  Vd-g;  —  *^ripiäwff (sd.)  .  .  asti  atari .  .  a%a  narB  alavanS  F.sjb;  Yt/^.zs;
19414:—  sadra  möi  sqs  (sd.)  .  .  sarazdäitii  Y. 43.11;  $!■  17.  zu  I  «):  Ayaica  möi mraos..  Y. 43.12;  17; — ys  vä  mBi yä gaeTiä  dazdi{aA.)  *aSta^Ae  Y.46.Z1  10;
20847:I  et  (eum)  qui  (est)  faciendi  et  dicendi" I  Y.  33. 14;  —  *grSkms . .  atikSus  maraxtärB I  (sd.)  ahya  \yai(a  ^'Grlhmas  . .  et  (ii)  qui (sunt) ..  destructores"  Y.J2. 13; —  ku%ra töi  andrS  (sd.)  .  .  yöi  .  ,  caxrays  "num tibi  (sunt)  fidi  (ü)  qui  . ,"  Y.^4.7;  — kada  .  .  yOi  uxiäiiS  ainqm  .  .  frärmtl "quando  . .  (ii)  qui  (sunt)  tauri  .  ."  Y.  4G. 3;  —  naldä  dahySus  \ydi  iastSrS  drjsvatas "neque  (ii)  qui  (sunt)  . .  imperatores"  Y. 4O.  I ;  —  tat  ..  uitanai  data  . .  ySi  sl gSus  v^nzinl  (sd.)  azyi  ".  .  vitae  (eorum) qui  .  ."  Y.  34.  14;  —  tim  at  yasna- nqm  paurvataia  yazamaidl  ySi  ..  iyeintJ ".  .  imprecationum  .  .  (eorum)  qui  .  ." ^•37-  2;  —  yi  varpsaiil  (sd.)  kyat vasnä  firasöJ^mim  "qui  . .  fecerit  . .  (id) quod  (est)  .  ."  "^.46.  19;  —  hyatcS dar>gSm  dr)gvll.d»byS  rasB  savai'a  alavabyö "et  (id)  quod  (est)  . .  damnum  et  lucra  . ." Y._jo.  11;  —  Aaihyavanitqm  {%A.)  hyat vasna  f?rasS.t}m}m  "verificationem  (eius) quod.."  Y. 50.11;  —  ai  zt  töi  vaxsya .. hyai  aksyä  (NSf.;  sd.)  dngvaiii  wörtlich ",.  von  dem,  was  die  Androhung  ist,,"  Y, 51.  8;  —  hyat  "qsasutä  (sd.)  yä  (NPn.) daiiiiana  (sd.)  fraoxta  "..  (ea)  quae  (sunt) . .  enuntiata"  Y.  48.  1 ;  —  das  Relativ  kon- gruirt  mit  dem  Praedikat:  vldvä  yalclt güzra  (sd.)  singhanhS  (wörtlich)  "kennend auch  (das),  was  die  geheimen  Lehren  (sind)" Y.4<V,3;  —  anais  a  vT.nSnasa  ya  (NSt) iarapsjis{ad.}cä  kjvltäscä  Y._J2.  15;  — *m>ndäiäyai  (sd.)  ya  (NSf)  toi  adisHi Y.44.8;  5,^.13;  —  nipatihw . .  tumas^a ya  armaitiH&d.)  Tiilcä  Y.4g.  10;  —  yS va  mSi  \yh  (NPf)  gasha  dasdi  (Sp. 7 1 S  u.)  *asnatihe  wörtlich  ". .  (das),  was meine  Besitztümer  (sind)  .  ."  Y,  46. 8;  — vtayUta  yä  (NPn.)  mrqi  sädra  drtgvats (wörtlich)  "immer  (wird  sein)  was  die Qualen  (sind)  .  ."   Y.45.  7;  43-5,  49-6;
20910:YtÄ  48.  f)  GPra.:  mtirS  vtspS  matda'\  hacaite  asis  .  .  uyrasca  dämdis  upamanO yasnanqm  yam  asaenqm  fr}},wä{sd.)cit  .  .\uyrasca  asaonqm  frava^ayS  yasla  pouru- Yt./o.i3ci,  IIB) bedeutungslos  erscheint  HflOT  hairaks\%A:)  Yt.  /o.  66.  b)  NSf.: uns  das  Relativ  vielfach  dann,  wenn  es,  j>'n^  dim  upanhacat  yä  uyra  naire  kam.' ohne  dass  ein  Verbum  folgt,  dem  Nomen,  1  z-'n/vift'/ Yt. /p.  39;  —  aiHi  ätm  atwyäiti mit  dem  es  kongruirt,  und  dessen  Attri-|_V'l  dahma  *va»uhi  afritis  P,J2;  —  kai buten  vorausgeht  a)  im  gAw.;  I)  \\a\hE  vä  i7j><«  (Sp.  237  m.)  *v?nzyap  ya  näi- Nominativ  oder  dem  ihm  gleichen  Akku- ,  rika  N.  6;  —  saoayeiti  yü  hava  daena  H. sativ.  Die  Fälle,  die  hierher  gezogen  wer-  2.9;  it']  —  ks  yä  kaine  'V.i4.-i^^'>'>;  — den  können,  sind  unter  IIB  verzeichnet:  [hierher  oder  zuIB  (Rel,  in  Kongruenz  mit Y-JO-S  0'^  dr3gva\  4ü.z  (ysi  uxsanS  Atm  Praed.):  *kä  larJ.maitisl  ya  kaca asnqm),32.i.%{yä  karapuäsm  k3Vltasi^,\dainay3t  milzdayasiiStl  apastüitii  U.  4t; 45- 1  (ya  n^qs  sadra),  46.Z  (yy  vä  iiiDi' —  ya  papiiiua  vasö  acisße  (sd.)  N, yä  galhä  datdl  *aSnaAhFj  usw.  Z)  in  ■  62.       c)N.-APm.r  *'taty5i  taxma  xitavayB
24452:•  j.  vispäyav-  Adj.  (auch  fem.)  'immer- während'; 'yätttia  ustaiahm  .  .  yä  nari sädra  drvalö  Vr,  18.  2;  —  vahishrnca ahüm  . .  'yumla  ustatas  (statt  AS.)  P. ^tf.
25629:yütii  yä  n»rqs  sädra  (sA)  drsgfoß  Y.  \  *gaintlsca)  —  vidiiäryinnS  sahayeiti;  ä  dim 45- 7 i  —  dr^vütö ..ydtyä  'vä  xraodaitl  väts  upa.vävO  salayäti  {sA.)  rapi^witarat HttvatB  ftnlä  aka  (sd.)  ¥.5/.  13;  —  at  ..\—  {apäxtarat)  —  iaca  naimat . .  hubae&i- dngvatS  akail  il'an'häis  i^A.)  pmtf  *vqnS' tarü  —  {duägaintitarS)  —  anyaiibyS  va- paityäntf  '^.4g.\\.  a)  neben  *daittä-\taähy8  H.2.  7;  25;  —  aAhä  dim  vä/ayi usw. :  karapanB  isvayasca  . .  yJng  afs  'vä  ■frSntOa  (sd.)  sai/ayätt  yl  hava  daOia ifai^  xraodai  {sA.)  damn  hyal  aibt.g3tian\kamtt0  kihrpa  sflrayä  H-2. 9**;  —  äat yahra  anvatö  pgntui  (sd.)  Y.  46.11;  —  Am  (nänü.  da&iqm,  sd,  Sp.  666  m.)  aoxta tatca  .  .  %v»akml  *ä  *dqm  (Sp,  684  o.)  ,p»nsS  yö  nari  asaotß  'va:  a^ca  caräitis m^inhi    matiS    voAs    'utiasca    asäunqm  i  ahi  yqm  it  yava  . .  sraistqm  äädarysa  (sd.)
25995:i)  'bewirken,  schaffen,  zu  Stande  bringen': i:Jclt  msi  sqs  (aSr-AorA.)'*  tvSm  masdä vaidiÜB  "und  das  wirst  du  mir  bewirken, 0  M.,  der  du  es  am  besten  zu  ver- schaffen wcisst"  ¥.4*^.19;  —  <i%a  mü sqstä  (3Pj'-AorA.)"  voha  vastryä  "so schaffet  mir  denn  das  Gut  der  Landwirt- schaft" Y.  29. 1  ^;  —  sädra  mBi  sqs*^ mafyaisB  *trasdäitil  tat  vir^syädyal  Ayat.. "soll  mir  Leid  bei  den  Menschen  schaffen mein  Vertrauen,  das  zu  tun,  was  . .?"  Y. 43.  II.  2)    'vollziehen,    vollstrecken';
26023:zu  verstehen  sei;  s.  in  sädra-  und  iacia-.
28330:•  j-,  g.  'zrazdätay-''  i)  f.  'Vertrauen auf  -,  Glaube  an  -';  a)  mit  Akk.  oder Gen.  (obj.):  °ääittm  ma^nm  spjntjm  "den Glauben  an  das  heilige  Wort"  Y.  25.  6;  — 'dälSÜ  ma^rafte  spmtake  V.  22.25.  ^)  ™'^ Inf.:  sadra  mffi  sas  (sd.)  . .  •däUi!  tat vfmyddyai  hyal  .  .  Y.  43.  11.  LS, *'dätal-ca  als  Inf  sbes.  a)  Adj.  (auch fem.)  'vertrauend,  gläubig':  'datüit  aahuyat (sd.)  haca  Yt  10.  9.
```


## [2026-09-06T15:29:51.284Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN 192 (leaf = printed+21 -> 213) ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==213' HRN.txt | head -60"
}
```


### [2026-09-06T15:29:53.028Z] TOOL RESULT

```
=== HRN 192 (leaf = printed+21 -> 213) ===
— 191 -
854. UuHt *Seite, Flanke', hu^Vl^ kustl 'Gürtel', vergl.
hergustvuan (No. 205) ; kusftgir 'Ringkämpfer (AM. 2()6
Zeile 8).
phlv. ktist^ kustak 'Seite*, kusttk^),
855. kuSten 'tödten', nt^^t^lD (Qiss. Dan.).
aw. l/ftaos-, kusaiti 'tödten'; phlv. kustan, vergl. asö]-
kvs (für aw. asavaynya-, vd. 5 (47)); skr. KÄö5-, kusnäti
'zerreissen' (?).
kurd. LW. (?) kustin 'tödton*; bei. L\V. (?) kuäag,
n. ßusay 'todten, scli lachten (207).
856. feesß/ ^Schildkröte ; Krebs (Zodiac, Sahn. I, 77 Vers
285)', keseto (dial.).
aw. kasyapu' 'Schildkröte' oder *Krebs' (Geldner,
KZ. 25, 503, 5()6j ; skr. (Brhm.) kagydpa- 'Schildkröte .
af/. kasy 'Schildkröte'; bei. käsib (190).
857. Ä-e«efc 'Elster .
Toniaschek, Painirdialokte S. 771, veigkM'cht aw.
karsiptan-^ phlv. kars{i)ft (L)eutun*i: nicht sicher), wa/.
karjöpc, sar. karjopc, si;'n. ksebc 'ElstiM-'.
858. kiSver^ kesver 'Ph-dteil'.
aw. karsvar- 'Weltteil'; phlv. kisvar^).
859. kesläen ziehen'.
aw. [/^km's-, karsayefi^); phlv. kasttan; ai. 1. [/^kars-,
• kdrsati, karmyati 'ziehen, schleppen'.
kurd. kisän ziehen'; af>'. k/dl; bei. kasay, n. /i'asay
'ziehen, abziehen, herausziehen' (19:^); arm. LW. (?)
Karsem 'ziehen*.
») Syr. LW. J^D^'ID, J^nDD, p^DDIp; ai'ab. LW. kustij (de
Lagarde, Ges. Abb. 59, 60); bei. LW. kustl (143). — Aber nicht gehört
dazu lat. c^ista *Rippe*, das Meringer, Sitzb. WAW. CXXV, *Beitr. z.
indg. Decl.*, 42, mir nicht einleuchtend, zu ai. dbthi- 'Knochen* stellt.
') Eine Volksetymologie in 'Selections of Zätsparnm* (West
P. T. I) 7, 9.
») Aw. [/has- will Hübschmann ZDMG. 44, 558 ausser Betracht
lassen.
```


## [2026-09-06T15:29:58.550Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN leaf 214 (p.192) ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==214' HRN.txt | head -60"
}
```


## [2026-09-06T15:30:00.229Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT sadra headword ===\"\ngrep -n \"sädra-\\|sadra-\" BRT.txt | head\necho \"--- context 13753 ---\"\nsed -n '13745,13765p' BRT.txt\necho \"--- 26023 ctx ---\"\nsed -n '26015,26030p' BRT.txt"
}
```


### [2026-09-06T15:30:00.356Z] TOOL RESULT

```
=== HRN leaf 214 (p.192) ===
800. kef \Schaiiin'.
aw. kafa- *SchaunV; phlv. kaf (AV., nicht kef)\ skr.
kapha- 'Schleim'.
kurd. kaf Schaum'; oss. d. /äfä, t. /äf Hotz,
Schleim' (299); bei. kap^) (188); wa/. ;^w/, sar. /^/.
861. kul *krnmm, gekrümmt'-).
Nach Nöldeke (mündliche Mitteilung) zu gv. y.vkhig
*krumm'. Dann vergl. auch gr. xt;(}rog gekrümmt', aw.
skarena- 'rund'. — Fortunatow stellt (BB. 6, 216)
gr. y.vXXog zu skr. kuni- *lahm am Arm' (aus "^kulni-),
862. keläy, kulüy liabe', ixiD (Is. 34, 11, etwa statt ixiD?).
aw. «;ära;72rt- (?) ; phlv. varäy^ varäk.
Das np. k könnte dann eben so wenig ursprünglich
sein wie in kiisüden statt gusciden. Anderenfalls würde
die Zusammenstellung unstatthaft sein. Nöldeke will
daher (mündliche Mitteilung) gr. v.ogai, etc. vergleichen
und auch phlv. rardy, varOk ganz aus dem Spiele
lassen; jüd.-pers. JIXID sei in jNHp zu emendiren, wie
auch das Gazophylacium schreibe (D und p seien
in hebräischen Handschriften oft nicht von einander
zu unterscheiden)-^). Diese Erklärung ist gewiss vor-
zuziehen, zumal die Bedeutung *Rabe' für das Avesta-
wort gar nicht passt (sie beruht zudem nur auf einer
Vermutung Destür Daräb's) *).
863. Ualäh \VIütze'; Helm (aus Stahl, Sahn. I, 100 Vers
711)', kidä, hdeli.
') Vergl. g. kaj).
^) Durch einen Vers des vorfirdusischen Dichters Abu Öekür
belegt.
^) Im Neupersischen wird das Wort aber nie mit q^ sondern stets
mit k geschrieben. Es müsste also ein Schnitzer im Gazophylacium
und in der jüd.-pers. Schreibung vorliegen.
*) Nachträglich sehe ich Hübsch mann's Bemerkungen in
KZ. 26, 607 folg., der auch aw. väi^ayun- nicht als *Rabe* gelten lassen
will und bei. f/nräy *crow\ köh-f/uräy Vaven' (Damea, S. 104) heran-
zieht ( Corrokturnoto ).
```


### [2026-09-06T15:30:00.418Z] TOOL RESULT

```
=== BRT sadra headword ===
13753:duäsKsadra-
26023:zu  verstehen  sei;  s.  in  sädra-  und  iacia-.
--- context 13753 ---
•  g.  du§itay-  £  'übles  Wohnen  sva.  Elend, Unglück':  ^ä  xi  d»nifn>m  visiin  vä  sOdr.'in vS  daRyüm  vä  ädäl -tääJ  (X&-)  marakalcä "denn  Hai;s  und  Gemeine  und  Gau  und Land  bringt  er  in  Elend  und  Verderben" Y.^/.i8.
Komp.:     *du}Jr'sitay;    J  ^O/  D.  37.  —    Pü.:
duitiraiiJn  (weil  sie  dui-if   lerlegte).
•  j.  duS.k«r9t-''  Adj.  'übeltuend,  Übel- täter'(?):  äat  ana  parB  -ta  V.  2/.  6".
ai.  duskj-l.  Ädj.  —  Pu.:  fehlt.  —  0  Stamm- ansatz und  Formbe Stimmung  unsicher;  vll. lu  'ijnla-  Adj.  oder  'tprilay-  f.  —  >>  Ob Glosse?
•  j.,  g.  duS.xratav-  i)  m.  'schlechte  Ab- sicht, übler  Wille':  ^ci;  'xra^wä(\%.)  aisi- m»n  vandsn  (sd.)  Y.  4g.  4.  a)  Adj. (auch  fem.?)  'von  schlechter  Einsicht'  oder
dby  Google
753
duäsKsadra-
duS.sastay-
754
'Absicht':  'tarn  (ASf.?)  . .  asrävayat^äinim Aog.  &D(?).
Pä.:  daSxral,  (lU  Aog.):  duixratömand.
•  g.  duäa-xsa&ra- "  Adj.  i)  'schlechte Herrschaft  führend,  schlechter  Herrscher, yUrst';  Auxsaira  xsintqm  (Sp,  551  m,)  ma ni  °än7  (NP.)  xsitita  Y.  4<?.  5 ;  —  karafatiö ..  °'irä  daRyunam'-^  M. 48.10.  2)  'unter schiechter  Herrschaft  stehend,  schlechten Fürsten  untenan':  ''^rJng  dus.syaoi:an^ng . .  ilrfgvatö  Y. 49- ii-
S  300^  5-  —  P"--  diäx'alai.  —  ■)  NA.  hal 2mal  diih-xi'.  —  ')  Vgl.  dazu  ^iirvaji-*).
•  j.  /iar»m  asavatiptn  "dusää  ear^fym  (sd.) T.J3,  W.j.  14  PüZ.  (wo  <7s'  fehlt).
Pü.  (fdr  ,/■  Z-):  Juz-.ar„,5„.
•  j.  duS-ciOra-  Adj.  (fem.  'ra-)  'des .\nblick  übel  ist,  hässlich  anzusehen': drujim  yam  °rqm  timanhainJm  YL  /^.gs;
—  ^**''rayh  (GSf.)"  Yt.  79.  94.
Vgl.  hui^ra-  Z.  —   ')  Hds.   ■rayayA.
•  j.  'duS.dätay- ''  f  'schlechte  Einsicht, Mangel  an  Einsicht':  'iayä»  (GS.  als  AblS.) fraista  dmantS  "wegen  Mangels  an  Ein- sicht sind  die  meisten  glaubensfeiadlich" Aog.  sOm.
--- 26023 ctx ---
Y.45-7''-
Zum  V.  tav-    —    Vgl.  'savaA-.    —    Pü.r  sül,
SQ.:  läbhah.  —  0  D.i.  der  durch  seine  Lehren
die  Erlangung  des  Nutiens  vereilcll.  —  ')  Vgl.
Y.  JO.  II.     z.\uadr.    a.    Der.    VglS.    /.  137;
ferner    unter   pitar-,  nar-   (Sp.  1048   o.)   und
^art%a'.     Vgl.  noch  No.  3.  —  3)  In  Zeile  c
und  d  wird  «usgefiihrt,    was  unter  savt  in  a
zu  verstehen  sei;  s.  in  sädra-  und  iacia-.
•  g.  savayö  Inf.  'Jemandem  (Akk.)  den
Nutzen  (im  andern  I.«ben)  zu  schaffen':
yqm    xihät^m    rännibya  (sd.)  di  .  .  raSa-
ye^kl  (sd.)    dngvanttm    j*    aiavanitn    Y.
5^-9-
Zum  V.  sav'%    anscheini 2+24;  S  »ob-  a  a.  —  I
inem  Prae«.
```


## [2026-09-06T15:30:12.942Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources\npython3 -c \"\nimport json;d=json.load(open('refs_online.json'))\nprint(json.dumps(d['BQT'],ensure_ascii=False,indent=1))\nprint(json.dumps(d['SOD'],ensure_ascii=False,indent=1))\nprint(json.dumps(d['MON'],ensure_ascii=False,indent=1))\n\""
}
```


## [2026-09-06T15:30:13.076Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"\\[pdf page\" BQT_v2_pages.txt | head -3\ngrep -c \"\" BQT_v2_pages.txt"
}
```


### [2026-09-06T15:30:14.650Z] TOOL RESULT

```
{
 "title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)",
 "kind": "archive_djvu+local_scan_ocr",
 "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.com/file/8230741184/borhane_ghatee_jelde_4.pdf.html (م–ی, 553 pp), vol 5 https://s3.picofile.com/file/8230741300/borhane_ghatee_jelde_5.pdf.html (تعلیقات, Amir Kabir 5th pr. 1376, 293 pp). Same set behind login on ketabnak.com/book/55304-55307 and /58249.",
 "lookup_hint": "grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \\f; leaf N = N-th \\f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt"
 ],
 "page_offset": "vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').",
 "covers_etymology": true,
 "notes": "Persian OCR is mediocre: headwords and Mo'in's footnotes (e.g. '۱ - رك: ابر کوه', Pahlavi/Avestan Latin forms) are mostly readable but with many character errors; search with short substrings and tolerate errors. BQT_v1_pages.txt was built from the djvu.xml; BQT_v2_pages.txt from pdftotext -layout of the _text.pdf. Volumes 3–5 (roughly ح/خ–ی and the تعلیقات volume) are not online in full text; for those use Dehkhoda quotations of Borhan/Mo'in via vajehyab/abadis/parsi.wiki, or page images on noorlib (different edition). | Vols 3-5 scans (image only) in incoming/BQT; vols 1-2 have OCR text files BQT_v1_pages.txt / BQT_v2_pages.txt. Offsets verified by eye at several pages (v3 drifts by ~4 pages; page_map gives exact positions once built). || UPDATE: vols 3-5 now downloaded (image-only PDFs, verified as Mo'in's edition from title pages and the Latin footnotes) and OCRed locally. Image-only scan OCRed locally with tesseract 5 (fas.traineddata from github.com/tesseract-ocr/tessdata_fast, stored in incoming/_tessdata). *_pages.txt = 'fas' model (best for Persian); *_pages_faseng.txt = 'fas+eng' model (better for the Latin-script Pahlavi/Avestan etyma, worse for Persian). Pages separated by \\f; leaf N = N-th \\f-block 0-based = PDF page N+1. Search with short substrings and tolerate OCR errors. Provenance caveat: picofile is a general file host, the uploads are not from a library; treat as a grey copy (the book is in copyright in Iran). | vol 4 (م–ی) OCR text, tesseract fas+eng, pages tagged [pdf page N], printed = pdf+1917 | vol 5 (ta'liqat) OCR text, printed = pdf-5 | vol 3 (ش–ل) OCR text (689/721 pages), printed ≈ pdf+1203..1209 | BQT_v2_pages.txt: printed page = leaf + 540 (verified by catch-lines at pp. 838-855, 869, 904); earlier estimate +543 was 3 pages off.",
 "scans": [
  {
   "volume": "3",
   "file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf",
   "first_printed": 1208,
   "last_printed": 1925,
   "pdf_offset": -1205,
   "page_map": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pagemap.json",
   "lang": "fas",
   "ocr_text": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt",
   "ocr_note": "689/721 pdf pages OCRed (tesseract fas+eng, mediocre); pages are separated by form-feeds and tagged [pdf page N]; remaining pages via tools/ref_page.py"
  },
  {
   "volume": "4",
   "file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf",
   "first_printed": 1920,
   "last_printed": 2475,
   "pdf_offset": -1917,
   "lang": "fas",
   "offset_note": "printed = pdf+1917, checked at pdf 150 and 500",
   "ocr_text": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt"
  },
  {
   "volume": "5",
   "file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf",
   "first_printed": 1,
   "last_printed": 290,
   "pdf_offset": 5,
   "lang": "fas",
   "note": "vol 5 = ta'liqat (addenda) with its own pagination 1-290; cite as BQT5:<page>. Plain BQT:<n> with n<1208 refers to vols 1-2 (OCR text files BQT_v1_pages.txt / BQT_v2_pages.txt), not to this scan.",
   "ocr_text": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt",
   "requires_volume": true
  }
 ],
 "cites": "page number, continuous across the five volumes of Mo'in's edition (1342/1963 = Amir Kabir 1362 reprint); Mo'in's etymological footnotes are the cited material"
}
{
 "title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/SogdianDictionary",
 "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/SogdianDictionary for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD.txt"
 ],
 "page_offset": "printed page ≈ leaf − 66 in SOD_pages.txt (0-based \\f blocks; 645 leaves; English intro precedes)",
 "covers_etymology": true,
 "notes": "OCR: Sogdian transliterations, entry numbers, English glosses and bibliographic refs (GMS, BSOAS, VJ ...) are readable; the Persian glosses are garbage (OCR'd as Latin). Full scan, 1995 edition = the one Nourai used.",
 "cites": "entry number / page in Gharib's Sogdian dictionary"
}
{
 "title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)",
 "kind": "website+archive_djvu",
 "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)",
 "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks).",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt"
 ],
 "page_offset": null,
 "covers_etymology": true,
 "notes": "covers_etymology = partial: origin-language tag visible online, Latin etyma missing. The a'lam volumes (MON5/MON6 citations, e.g. MON5:528) are NOT online: vajehyab's Mo'in has no proper-name entries (tested افراسیاب — only compounds returned); abadis shows Dehkhoda and 'فرهنگ اسم‌ها' instead, which do give Avestan forms (e.g. Frangrasyan) and can serve as a cross-check. noorlib has no Mo'in 6-vol entry found. The 6-vol edition itself was not found on archive.org, Google Books or HathiTrust full view. || RE-SEARCH 2026-09: still no scan of the 6-vol Amir Kabir edition (incl. vols 5-6 اعلام) on archive.org, Google Books (API quota-limited; WebSearch found no record with preview), HathiTrust (no record surfaced), noorlib, ketabnak (author page persons/6040 lists 34 Mo'in titles, none the 6-vol فرهنگ), tarikhema, picofile, scribd, Commons/Wikisource. Only the 2-vol Adena condensation exists (archive.org, mirrored on ketabnak 65980/65981, picofile, persianpdf, scribd); its image PDFs were downloaded to incoming/MON/ (the _text.pdf variants with OCR layer are at the same archive.org identifiers). The 6-vol set is purchase-only (in print: iketab.com, bookroom.ir/book/97022, 30book.com/Book/32100).",
 "cites": "page number of Mo'in's six-volume Farhang-e Farsi; MON5:… / MON6:… = volume 5 / 6 (proper names)"
}
```


### [2026-09-06T15:30:14.712Z] TOOL RESULT

```
41071
```


## [2026-09-06T15:30:19.185Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==530' BQT_v2_pages.txt | head -70"
}
```


### [2026-09-06T15:30:21.069Z] TOOL RESULT

```
    ‫ساده‬                                                                                             ‫س‬
                                                                                                     ‫ا‏‪kS‬‬
 ‫ساخته ر نگ = با رای فرشت بروزن‬                          ‫پزند‪ - ۱:‬بوزبان عربی چوبی است که آنرا از‬
                                                           ‫یل‪-‬ان‌را هم‌میگوند؛وآن‬
                                                                                ‫حندوستان آوورطند‬
‫پارچه سنگه » بمعنی موافق باشد که درمقابل‬
                                  ‫مخالف است ‪. 4‬‬
 ‫سا خن ‪ -‬بکر تالث‌بروزن‌ساکن‪,‬بمعنی‬                         ‫ساجور = باجیم بروزن ساطور‪ .‬گردن‬
‫صاروحاست ‪ ۳‬آن چبز ی باشد کهآ حك داخل‌آن‬
                                ‫ازم وا قسانند‪.‬‬             ‫تواند کریخت و تواند چاوید ؛ و بضی کونند‬
‫‪۹‬‬    ‫ساده است‬   ‫نمحتی‬   ‫اد ‪6‬‬   ‫بروزن‬   ‫‪-‬‬   ‫ساد‬                                                     ‫عربی است؟‬

 ‫‪ -‬وخوك نررا کهفمته‌اند کهکراز باشد ‪-‬وبمعنی‬                      ‫بمعنی سفید باشدکه بعربی بیاض گوبند‪.‬‬
                    ‫دشت وصحر أ وسانان هم هت‪.‬‬
                                                           ‫ساخت ؟ « بروزن باخت » ممروف‌است‬
‫ساد ]وران ت بروزن هاماوران» بلغت‬                           ‫بعنی‌کاربرا تمامکردگ ‪-‬ودوال تممةٌ رکاب وبراق‬
‫سربانی چیزی است مانند صمخ وآارا دردرون‬                     ‫وبند و بارزین اسب را بیز کفته‌اند ‪ -‬و بمعنی‬
 ‫بیخ درخت کردکان که مجوف شده باشد بابند ‪.‬‬                ‫بکرتوان همهت و آن پوششی امت که‬
 ‫سرد وخشك است ددرومم‌وسیم ‪ .‬خوردن وضملد‬                    ‫و خود لیز‬   ‫بر اس دوشانند‬        ‫در روز جنگه‬
‫کردن آن بر شکم اسپال خولیرا افم باشد‬                                                               ‫دوشند ‪# .‬‬
  ‫وآ نرابرومی فنطار ویعربی خاتم|انلك‌خوانشد‪.‬‬               ‫ساخته * ‪-‬وبزرن باخته »بمعنی‬
‫ساده د بروزن ماده ‪ ۰‬معروف است که‬                           ‫وایه‌ازمردم شیاد‬
                                                                          ‫موافق ‪ - ۷‬وآماده باشد ‪ -‬کن‬
‫در برابر ءنقش و ریشدار باشد‪ - 9۷‬و مرد) بی‬                                              ‫وچاپلوس هم هت ‪۷‬‬


    ‫‪-۱‬درترکی «ساج» بهمین معنی‌است «جفتایی‪٩۳۳۳‬‏ »کدیرلان الی‌راکه برین‌تابه‌پخته‬
    ‫‪« - ۴‬ساجور بروزن کافور‪.‬چوبی اکسهت‌آوبشته شود درکردن‬               ‫شود «نان ساج» گونند‪.‬‬

    ‫‪- ۴‬باین معنی سومشخص مفود‬              ‫‪-۴‬اسم ازساختن» (هم‪).‬‬           ‫سکه» «شرح‌قاموی»‪.‬‬
       ‫ا _ رکه ‪ :‬ساخته رنکه ‪.‬‬                    ‫® _ اسم مفعول از «ساختن» ‪.‬‬             ‫ماضی از«ساختن؟‪.‬‬
    ‫‪ - ۷‬یز ملایم وحلیم وآرام ‪« :‬مردی ساخته بود بی تصب وبرخوارج (بعنی باخوارج)‬
      ‫وزون‪.‬‬
          ‫ومکو‬
             ‫هتی‬
               ‫کمع‬
                 ‫ساخته بود وطربق سلامت گرفته » تاریخ سیمتان ص‌بح ‪ -‬بط و ‪ - ۱۹۱‬وب‬
             ‫‪ = ٩‬هداس )‪۰‬م‪.‬ه( ‪ .‬هکر ‪‎ :‬یرف‌تفل ‪. ۱۱۱‬‬                     ‫‪.‬‬   ‫‪ :‬ساخته‬   ‫رکه‬   ‫ھ‪_ ۸‬‬

    ‫سادج ‪ ۰‬ساذح‪‎‬‬     ‫سار (ه‪.‬م‪ (.‬معرب آن ساده‬         ‫‪= ١‬‬          ‫استاد («‪.‬م‪۰ ).‬‬      ‫‪ _ ۶‬مخقف‬
                                       ‫«فس» و بمعتی جوان ساده‌چهره وبی موی وجمم آن سادکان ‪:‬‬
            ‫وز دوکف ساو کان ساتگنی کش بدم ‪.‬‬                     ‫از پر نرد باز دگاروان تر ببس‬
           ‫دأمغالی ‪4۵‬‬    ‫‪ ۶‬منوچپری‬

    ‫‪ #‬ساختی ‪ -‬بفتح تا » بپلوی ‪ ۳8085‬دنیبرکے ‪ >۰۰‬از ربشة اوستابی ‪( 689‬یابان‬
     ‫‪»»4‬بلوچی ع ‪gazÃS‬‏ »ارمنی ‪laetxas‬‏‬
                                     ‫گذشتن ‪ ,‬تلف شدن ) « بارتولمه ‪۳٥6‬‏ ‪۵ -‬‬                            ‫ردن‬
     ‫(زین کرده) » ‪( 412302‬زین‌ناکرده) «اسشق ‪ . ۸۸1۰‬کیلکی (رشت) ‪(.141×38‬حوالی‌لاھیجان)‬
     ‫ردن‪-‬‬
        ‫‪-‬تشکیل‌دادن ‪ -‬آماده کردن ‪ -‬بکنا‬          ‫‪3 -‬؛ ترتیب دادن م‪-‬قرر کردن ‪-‬کردن‬                     ‫‪88‬‬
                   ‫حیله کردن » توطثه کردن ‪ -‬سبت دادن ‪ -‬صیقل دادن » پرداختن ‪-‬تدبیر کردن ‪.‬‬
```


## [2026-09-06T15:30:28.770Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor n in 530 531 532; do echo \"########## leaf idx $((n-1)) = printed $((n-1+540)) ##########\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N' BQT_v2_pages.txt | grep -n \"سار\" | head -20; done"
}
```


### [2026-09-06T15:30:30.867Z] TOOL RESULT

```
########## leaf idx 529 = printed 1069 ##########
40:    ‫سادج ‪ ۰‬ساذح‪‎‬‬     ‫سار (ه‪.‬م‪ (.‬معرب آن ساده‬         ‫‪= ١‬‬          ‫استاد («‪.‬م‪۰ ).‬‬      ‫‪ _ ۶‬مخقف‬
########## leaf idx 530 = printed 1070 ##########
2:   ‫>‪° A‬‬                                                                                       ‫ساره دشت‬
13:‫سار » بروزن چار» بمعنی سرباشدکه‬                    ‫ساده‌دشت ‪ » ۴‬بفتح دال ابجد (‪)۱‬‬
16: ‫و گرزگاو سار بمنی گرزکاو سرو سکار که‬
29: ‫را ساربان کوبند ‪٩٩‬همچوباغبان‌ودربان‏ ‪ -‬وبمعنی‬
32:                            ‫همچولمکارو کوهسار‬          ‫مکرهاد افزآلنك اطلس وممدل النهار و فلك‬
38:                         ‫سارو کوهار‬
40:           ‫سار‬           ‫مکان‌دمك و کوه‌خواسته‬         ‫هر دومیباشد » و بهترین آن هندی است بك‬
55:                 ‫= سارك = سارح = ساری ‪.‬‬           ‫جقرافی‌ای اقتصادی ص ‪٩۲‬‏ بنقل از هابنرش؛ ‪.‬‬
56:          ‫چون سارسیاه است وگل اندر دهن‌سار ‪.‬‬                    ‫آنزنکی زلفین بدان رنگن رخار‬
58:                                                                            ‫‪ -0‬ر‪:‬ساربان ‪.‬‬
########## leaf idx 531 = printed 1071 ##########
2:‫ساریه‌عنی شتر وبان بمعنی محافظت کننده ونگلہ‬
7:                                                           ‫ومثل ومانند همآمده‌است همو دیوساروخا کار‬
8: ‫ازسار است" وان‌جالوری باشدسیاه ویرخط وخال‬                 ‫وآزار ومحنت باشد ‪۴‬‬              ‫‪-‬ج‬
12:         ‫را صدای رباب چار تاره تشبیه کرده‌اند ‪.‬‬            ‫صاحب و خداوند هم هست همجو شرمسار ستی‬
13:      ‫ست»ی‬    ‫سار چه ‪ - ۸‬بر وزن پا‬
15:       ‫سارج است که جالور سیاء خوش آواز باشد‪.‬‬               ‫سار ‪ -‬بروزن‌خارا ‪ :‬بمعنی زبدموخالس‬
16: ‫سار خك ‪٩‬‏ = بفتح خای تقطمرار (‪)۱‬‬                           ‫باشد‪.‬ا کر چه این لفظ باین‌معنی شایستگی‌صفت‬
18:‫کوبند وباین‌معتی بسکون خای تقطمدار (‪)۲‬هم‬                    ‫عنبرومشك وزر منظر نامده است همجوعنبرسارا‬
19:‫‪ ۳۷‬و بضی بکس ثالك وسکون خای‬                  ‫آمده‬          ‫ومشك سارا وزر سارا ‪ - ۳‬ونام زن ابراهیم عليه‬
23: ‫سار خکدار ‪ ۳۲۰‬بارال ابجد بر وزن‬                            ‫ساران = پروزن باران» بمعنی سرباشد‬
27:           ‫وزن ومعنی سارخك است که يشه باشده‬                 ‫سار بان « ببای ابجد بروزن ناروان‪,‬‬
28: ‫سار شکدار ‪ = ۳۱‬با شین شطمدار(ه)‬                            ‫بمعتی محافظت کننده‌ونگاه دارندة شتر باشدچه‬
42:              ‫چون یمه‌ای بعنبر سارا میاگنی ‪.‬‬                  ‫غالبه دانی زر سندروس‬     ‫‪ ۳‬سدارد خحمه‬
45:      ‫مارای (عبری؛بمعنی‌امیرشمن)اسم‌اصلی ساره زوجة ابراهیم‌است وساره (بممتی‌اعیره)‬                 ‫‪۴‬‬
47:              ‫چبت ابن شمشير برساران من ؟‬                    ‫کت آن ریجورکای باران من !‬
51:                                         ‫س=‬‫‪ - ۱‬ساربان = ساروان (ه‪.‬م‪ ).‬از ‪ :‬سار (‬
53:      ‫رك‪ :‬سارچه »‬    ‫‪۲‬‬     ‫بجای ‪( 60181080‬فی)یذیرفته‌شده ( از بادداشت های استاد پور داود ) ‪.‬‬
54:  ‫*‪-‬از‪ :‬مارخكت‬           ‫(«‪.‬م‪ ۰ ).‬ورك‪:‬سارخکدار‪.‬‬       ‫سارخك‬     ‫تس‬   ‫‪4‬‬     ‫رکه ‪ :‬سارح ‪.‬‬        ‫‪۸‬‬        ‫مارك ‪.‬‬
55:                     ‫سارخك (ه‪.‬م‪۰ ).‬‬     ‫‪=۹‬‬                 ‫سارشکدار ‪:‬‬    ‫دار (درخت) (ه‪.‬م‪= )۰‬‬         ‫(ھ‪.‬م‪+ (.‬‬
57:                               ‫سارخکدار ‪:‬‬    ‫س‬       ‫(«‪.‬م‪ + ).‬دار (درخت)‬      ‫ار ك از ‪ :‬سارخك‬
```


## [2026-09-06T15:30:40.818Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==532' BQT_v2_pages.txt | sed -n '1,20p'"
}
```


### [2026-09-06T15:30:42.858Z] TOOL RESULT

```
                                                                                                   ‫اس‬      ‫‪6‬‬
‫ساریه‌عنی شتر وبان بمعنی محافظت کننده ونگلہ‬
                                                            ‫وعریی مصر خوانند ‪-‬‬
                                                                             ‫انگور هم هنت ب‬
                            ‫است ‪۰ ۹‬‬   ‫هده‬   ‫دارنده‬
                                                           ‫و بممنی بلند و بالا ‪ -‬و بمعنی شبه و لظیر‬
                                                           ‫ومثل ومانند همآمده‌است همو دیوساروخا کار‬
 ‫ازسار است" وان‌جالوری باشدسیاه ویرخط وخال‬                 ‫وآزار ومحنت باشد ‪۴‬‬              ‫‪-‬ج‬
                                                                                            ‫ونر‪۱‬ن‬
                                                                                                ‫و ماند آ‬
‫کووچکتر از فاخته وآواز خوش دارد وآواز او‬                   ‫‪ -‬وکلك ونی میان خالی را نیزگوبند ‪-‬ویمعنی‬
         ‫را صدای رباب چار تاره تشبیه کرده‌اند ‪.‬‬            ‫صاحب و خداوند هم هست همجو شرمسار ستی‬
      ‫ست»ی‬    ‫سار چه ‪ - ۸‬بر وزن پا‬
           ‫برچه‬                                                                                 ‫صاحب شرم ‪.‬‬
       ‫سارج است که جالور سیاء خوش آواز باشد‪.‬‬               ‫سار ‪ -‬بروزن‌خارا ‪ :‬بمعنی زبدموخالس‬
 ‫سار خك ‪٩‬‏ = بفتح خای تقطمرار (‪)۱‬‬                           ‫باشد‪.‬ا کر چه این لفظ باین‌معنی شایستگی‌صفت‬
‫بروزن آب چك » بممنی پشه باشد و بعرمی بق‬                    ‫چیزهای دبگر نیزدارد لیکن ترکیب آن بجز‬
‫کوبند وباین‌معتی بسکون خای تقطمدار (‪)۲‬هم‬                    ‫عنبرومشك وزر منظر نامده است همجوعنبرسارا‬
‫‪ ۳۷‬و بضی بکس ثالك وسکون خای‬                  ‫آمده‬          ‫ومشك سارا وزر سارا ‪ - ۳‬ونام زن ابراهیم عليه‬
      ‫نقطه‌دار (‪ )۳‬کنته‌اند بممنی بیش بشه وکنه‪.‬‬                                     ‫است ‪۰ ۴‬‬        ‫ومدهمه‬
```


## [2026-09-06T15:30:57.916Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==532' BQT_v2_pages.txt | sed -n '20,60p'"
}
```


### [2026-09-06T15:30:59.731Z] TOOL RESULT

```
      ‫نقطه‌دار (‪ )۳‬کنته‌اند بممنی بیش بشه وکنه‪.‬‬                                     ‫است ‪۰ ۴‬‬        ‫ومدهمه‬
                                                                                                        ‫بسلا‬
                                                                                                           ‫ال‬
 ‫سار خکدار ‪ ۳۲۰‬بارال ابجد بر وزن‬                            ‫ساران = پروزن باران» بمعنی سرباشد‬
 ‫کاوری زار » درختی باشدکه نآرا پشه غالویشه‬                 ‫که بعربی راس خوانند ‪ - ۵‬و بممنی سر هانیز‬
            ‫خاله کوبند وبعربی شجرةالبق خوالفند‪.‬‬            ‫کفته اند که جمم سر باشد ‪ -‬و نام قصبه‌ایست‬
                                                                                                       ‫از عراق ‪.‬‬
           ‫وزن ومعنی سارخك است که يشه باشده‬                 ‫سار بان « ببای ابجد بروزن ناروان‪,‬‬
 ‫سار شکدار ‪ = ۳۱‬با شین شطمدار(ه)‬                            ‫بمعتی محافظت کننده‌ونگاه دارندة شتر باشدچه‬

  ‫‪۰‬‬     ‫)‪ (e‬چك‪:‬وسکون‌خا‪‎‬‬           ‫(‪ )۷‬چك ‪ :‬بسکون خا ‪.‬‬                   ‫‪ -‬بفتح خا ‪.‬‬       ‫)‪ (۱‬چك‪:‬‬

                                      ‫(ه) چك‪ :‬شطمدار ‪.‬‬                   ‫شطمرار ‪.‬‬    ‫‪- :‬‬    ‫(‪ )4‬چك‬


  ‫‪ - ۴‬در اوستا ‪ ( 27045 -‬درد » غصه) «اسشق‬                       ‫دىباچة مولف ‪.‬‬        ‫ه‬‫ل‪:‬‬
                                                                                       ‫صرك‬
                                                                                         ‫‪- $‬‬
  ‫اوسا ‪۰‬‬     ‫‪ ۰‬رك‪ :‬خرده‬    ‫در مقابل کاش‬      ‫شده‬     ‫بهلوی«تنگی»تررجمه‬      ‫سادرء اوستابی در تقسمر‬         ‫>‬

                                                                                    ‫پورداود ص ‪۲٩۱‬‏ ح ‪۰‬‬

              ‫چون یمه‌ای بعنبر سارا میاگنی ‪.‬‬                  ‫غالبه دانی زر سندروس‬     ‫‪ ۳‬سدارد خحمه‬

      ‫« منوچپری دامغانی ‪۰۶۱٩‬‏ ‪.‬‬
      ‫مارای (عبری؛بمعنی‌امیرشمن)اسم‌اصلی ساره زوجة ابراهیم‌است وساره (بممتی‌اعیره)‬                 ‫‪۴‬‬
                                                       ‫‪.‬‬    ‫‪« /‬اموی کتاب مقدس “‪eof‬‏‬          ‫نام بعدی آوست‬
              ‫چبت ابن شمشير برساران من ؟‬                    ‫کت آن ریجورکای باران من !‬
                                                                                    ‫® _‬
      ‫مولوی بلخی رومی ‪« .‬فرهنك نظام“ ‪.‬‬
      ‫وان یسوندحفاظت)» در‬     ‫ر) ‪ ۲‬بان ( =‬
                                         ‫س=‬‫‪ - ۱‬ساربان = ساروان (ه‪.‬م‪ ).‬از ‪ :‬سار (‬
      ‫تر کیب‌معنی لفظی‌درست مثل‌کلمة «سروان»است کهلفة بممنی سر وسرور وسردارباشد ودرسالیای‌اخیر‬
      ‫رك‪ :‬سارچه »‬    ‫‪۲‬‬     ‫بجای ‪( 60181080‬فی)یذیرفته‌شده ( از بادداشت های استاد پور داود ) ‪.‬‬
  ‫*‪-‬از‪ :‬مارخكت‬           ‫(«‪.‬م‪ ۰ ).‬ورك‪:‬سارخکدار‪.‬‬       ‫سارخك‬     ‫تس‬   ‫‪4‬‬     ‫رکه ‪ :‬سارح ‪.‬‬        ‫‪۸‬‬        ‫مارك ‪.‬‬
                     ‫سارخك (ه‪.‬م‪۰ ).‬‬     ‫‪=۹‬‬                 ‫سارشکدار ‪:‬‬    ‫دار (درخت) (ه‪.‬م‪= )۰‬‬         ‫(ھ‪.‬م‪+ (.‬‬

                               ‫سارخکدار ‪:‬‬    ‫س‬       ‫(«‪.‬م‪ + ).‬دار (درخت)‬      ‫ار ك از ‪ :‬سارخك‬
```


## [2026-09-06T15:31:22.882Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON part1: سار ===\"\ngrep -n \"سار (\" MON_part1.txt | head -20\necho \"--- محنت / آزار ---\"\ngrep -n \"آزار و محنت\\|درد و غصه\" MON_part1.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt | head -10"
}
```


### [2026-09-06T15:31:22.965Z] TOOL RESULT

```
=== MON part1: سار ===
17704:اندک‌اندکك همی شود سار ( گلستان). 
73699:ساربان: 581-7 [- ساروان» ازء سار (- 
73719:سار (۵-)22۳07 [- سارخ - سارق - 
--- محنت / آزار ---
```


## [2026-09-06T15:31:23.422Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SOD kwb ===\"\ngrep -n \"kwb\\|k'wb\\|foam\" SOD.txt | head -30"
}
```


### [2026-09-06T15:31:23.472Z] TOOL RESULT

```
=== SOD kwb ===
36725:foam 
36731:foam 
40743:5002  kwb   B  ^r 
40745:foam 
64012:foam,  froth 
89682:foam     4400,  4401,  5002,  8334
```


## [2026-09-06T15:31:28.510Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '40735,40760p' SOD.txt\necho \"=== find leaf of 5002 kwb in SOD_pages ===\"\nawk 'BEGIN{RS=\"\\f\"} /5002[^0-9]/ {print \"leaf(0based)=\" NR-1 \" printed=\" NR-1-66}' SOD_pages.txt | head\necho \"=== entries 4400,4401,8334 ===\"\ngrep -n \"4400 \\|4401 \\|8334 \" SOD.txt | head"
}
```


### [2026-09-06T15:31:30.124Z] TOOL RESULT

```
C2,  13V19;  Hen.  Giants.  BSOAS  11,  70.5 

4999  qw3   C  ->  k'w1,  kw1 

5000  qw3   C  «*  kw2 

5001  kvv'yst    M  =»  qwy,  qw1 

5002  kwb   B  ^r 
ku/of   ©<Av.  kafa;  Khwar.  kfuk;  Khot.  kuva 
foam 

Mack.  BSTBL,  Dhu.  219  n  p46;  Bailey.  Prolexis. 


I 


49 

5003  kwc'   M,  S  jU* 
kuca   (qwe'1)  ©Khot.  kusda;  <*kauzdaci-a-ka 

©f.  n.;  ob.  qwey  ^kwc'kOi) 
mouth 
STi  30.3,  31.17,  48.18;  GMS  973,  1265;  BBB  p62, 
=== find leaf of 5002 kwb in SOD_pages ===
leaf(0based)=264 printed=198
leaf(0based)=554 printed=488
=== entries 4400,4401,8334 ===
36724:4400  ywnpyk   B  of 
36729:4401  Ywnpr,yck)   B  ^jf 
64009:8334  pym'kh   B  <j£ 
89682:foam     4400,  4401,  5002,  8334 
89845:froth    8334
```


## [2026-09-06T15:31:37.503Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '73715,73730p' MON_part1.txt\necho \"=== MON کف ===\"\ngrep -n \"^کف \\|کف (\" MON_part2.txt | head -20\necho \"=== کفچلیز ===\"\ngrep -rn \"کفچلیز\\|کفچه\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt | head -20"
}
```


### [2026-09-06T15:31:37.626Z] TOOL RESULT

```
قسمت‌های پشت آن خط آبی رنگی به 
محاذات تيرهةٌ بشت حوان قرار دارد. بهلوها 
و شکم حیوان سفید و نقره‌یی است. ماهی 
مزیور را جهت تغذیه و ساختن کنسرو صید 
سار (۵-)22۳07 [- سارخ - سارق - 
ساروغ - ساروق» گید.] (ا.) دستمال بزرگ 
که در آن چیزی نندند بقجه. سقر ۵. 
سارع: هه [ع.] (افا.) خورندة خوشه 
انگور با ین. (ف.) نو شنده. 

سارق: بورقه [ع.] (افا.) دزد؛ ج. سارقین. 
مر 9 سر ایق: 

سارنگ: 8 ([2- تن 
(جان.) برنده‌ای است ساه رنگ»؛ ساری» 
سار. (م.) یکی از فروع دفتتعاه شون 
=== MON کف ===
11213:کف مجموع سبابه و وسطی و خنصر و 
12595:کف 
16739:کف شود این جسم در آب و الکل حل 
18920:كافة مم-افاق! [ع. کف (ق.) کل ۳۳ 
20876:کف دست با کشت ۳ 
21164:کف ‌مال کر ده پوستش را شن کی تا آنگاه 
23299:کف فرهنگ فارسی_معین تت ۱ 
23844:کف دریا: (جاذ.) صدف نرم تنی دریازی 
23869:کف ۲۸ 1 - کفچ | (ا.) ماده‌ای سیاه رنگ که 
23874:کف 0( مج دای وس ۱ 
23890:کف 
23903:کف اطاق: سطح زیرین اطاق؛ مق. . سقف. 
23904:کف چنار: برگ چنار. کف حوض: ته 
23913:کف العذراء» قسده» قسد» شجرة الطلق» 
23915:کف مریم حجاری» اصابع الصفر. شحجرة 
23922:کف گرفتن: به کف آوردن. کف از دامن 
23924:کف دستش مو ندارد: مفلس است و از او 
23928:کف ذشت کسن کذاشتن ۰ تن: (عم.) جزای عمل 
24134:کف رونده] (ص‌فا.) (عم.) عیار و طرار؛ 
24138:کف زدن: «۱2)2202 [ع. ف.] (مسصل.) 
=== کفچلیز ===
incoming/MON/MON_2vol_Adena_v2_djvu.txt:24077:کفچلیز: امه (- کفچلاز - کفچلیزه - 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:24081:کفچه: ()مت [- کفچه - کیچ - کپچه - 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:24083:کفچه‌مار: ۲*57 (.) (جاذ.) یکی از اقسام 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:24093:یا قاشق بهنی درمی آید. کفچه ماران دارای 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:24097:با زهر یکی از همین کفچه ماران آفریقایی 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:24106:کفچه‌ها است و در هندوستان فراوان است و 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:24251:کفچلیز به ته دیگ خوردن کفگیر: (عم.) 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:42050:۰ آتن تلفات می‌دهد؛ کفچه مار 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:42065:صند‌ی. مان کز رو مار ساه کفچه‌دار. 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:48256:سویق را هم زنند؛ کفچه پست؛ ج. . مج آیح. 
MON_part2.txt:24077:کفچلیز: امه (- کفچلاز - کفچلیزه - 
MON_part2.txt:24081:کفچه: ()مت [- کفچه - کیچ - کپچه - 
MON_part2.txt:24083:کفچه‌مار: ۲*57 (.) (جاذ.) یکی از اقسام 
MON_part2.txt:24093:یا قاشق بهنی درمی آید. کفچه ماران دارای 
MON_part2.txt:24097:با زهر یکی از همین کفچه ماران آفریقایی 
MON_part2.txt:24106:کفچه‌ها است و در هندوستان فراوان است و 
MON_part2.txt:24251:کفچلیز به ته دیگ خوردن کفگیر: (عم.) 
MON_part2.txt:42050:۰ آتن تلفات می‌دهد؛ کفچه مار 
MON_part2.txt:42065:صند‌ی. مان کز رو مار ساه کفچه‌دار. 
MON_part2.txt:48256:سویق را هم زنند؛ کفچه پست؛ ج. . مج آیح.
```


## [2026-09-06T15:31:43.065Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '23865,23900p' MON_part2.txt\necho \"=========== کفچلیز/کفچه ===========\"\nsed -n '24070,24095p' MON_part2.txt"
}
```


### [2026-09-06T15:31:43.137Z] TOOL RESULT

```
می‌ماند. زهر اللحاس. ترکسات فعلی: کف بر 
لب آوردن: تولید شدن کف در اطراف لب. 
(کد.) خشمگین گشتن. 

کف ۲۸ 1 - کفچ | (ا.) ماده‌ای سیاه رنگ که 
مشاطگان بر ابروی عروس مالند. 

کف: ۲ ر شه * «کفتن» (شکافتن). دوم 
شخص امر حاضر از «کفتن» (بشکاف). 
کف 0( مج دای وس ۱ 
که مقعر گونه و قرينة پشت 
چ. کفوف؛ اکف. کف پا سطح داخلی پا که 
فتضا 4 آنکفتان استه کف رست: 
داخلی دست که متصل به انگشتان است. 


شت دس و با است؛ 


۱۳۹۸ 


فر هنک فارسی معین 


کف 


سطح)؛ رویه. کفه ۳ واحد ِِ آن 
در اهواز معادل 1 وصاع معادل ‏ مختوم 
بو ی ۱ : یکی از معجزه‌های 
مسوسی(ع) و آن چنان بود که هرگاه 
می‌خواست کف دست خود را در بغل کرده 
برمی آورد» نور شدیدی از کف او سا 

می‌شد)؛ ید بیضاء. کفی؛ یکك کف: به اندازة 
=========== کفچلیز/کفچه ===========
مچ: ۷۵15 [- کفک ] (1.) کف صابون و شیر 
و آث و آت دهان» کفکك. 
کفحک: :1:۲ (.) دامن زین اسب. 
کفچل: ام):۲ (.) کفل اسب سرین اسب. 
کفچل پوش ۲-05۶ [- کفچل پوشنده] 
(ص‌فا. ا.) نوعی پوشش که آن را زردوزی 
کنند و بر پشت اسب اندازند؛ کفل پوش. 
کفچلیز: امه (- کفچلاز - کفچلیزه - 
کفلی زک (.) چمچه بزرگ سوراخ‌دار؛ 
کفلیز. (جان.) بچهُ قورباغة. (جان.) سک 
ماهی. 
کفچه: ()مت [- کفچه - کیچ - کپچه - 
کبچه] (.) چمچه قاشق. 
کفچه‌مار: ۲*57 (.) (جاذ.) یکی از اقسام 
ماران سمی خطرناک که دارای زهری 
کشنده است و از گروه بروتروگلیف 
می‌باشد. این مار در سطح قدامی دندان‌های 
جلو آروارة بالایی دارای شیاری است که تا 
نوک دندان ادامه دارد و در آن شار سم 
جاری می‌شود. وجه تسميه این دسته ماران از 
آن جهت است که زواید مهره‌های گردنی 
خود رابه اختبار می‌ توانند بهن کنند و در این 
حال قسمت سر و گردن آنها بصورت کفجه 
یا قاشق بهنی درمی آید. کفچه ماران دارای 
دارای اقسام متعددند و همه آنها خطر نا کند. 
گونه‌ای از آنها در آفریقا و مصر وجود دارد
```


## [2026-09-06T15:31:48.586Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '23820,23866p' MON_part2.txt"
}
```


### [2026-09-06T15:31:48.638Z] TOOL RESULT

```
گوش؛ مکعب. قطعه‌ای استخوانی مکعب که 
بر آن شمارة اعداد از یک تا شش نوشته با 
و آن راب 
دست گیرند یا در میان طاس نهند و بر تخته 
نرد انکنند و مطابق عددی که آن نشان دهد 
بازی کنند؛ تثنية آن: کعبتین. کعبهةً جان: ( کد.) 
مقصد جان» منظور روح. کعية جهانگر د: 
کب رهرو: (کد.) آفتاب جهانتاب. کعباة 
محرم نشان: ( کد.) آفتاب جهانتاب. 
کف: ۲:۲ [قس. کفکک ] (۱.) یکی از اشکال 
انحلال هوا در مایعاتی که گرم یا تکان داده 
می‌شوند» ایجاد می‌گردد مانند کف حاصل 
از حل صابون در آب که بنام کف صابون 
خوانده می‌شود و سرجوش و کف حاصل از 
جوشاندن برخی مواد که در سطح مایم جمع 


فر هنگ فارسی معین 


۷ ۱۳ 
می‌شود. کف‌ها (گیا.) ج. کف. ترکیبات 
اسمی: کف آیکینه: آبی باشد که مانند کف 
بر روی آیگینه پیدا شود به هنگام گداختن. 
کف دریا: (جاذ.) صدف نرم تنی دریازی 
بنام ماهی مرکب می‌باشد و آن از رده 
پایرسران و از دسته ده‌بایان است. صدف این 
جانور برخلاف نرم‌تنان دیگر که از خارج 
بدن را پوشانده بصورت یکث تیفة کم و 
بش پهن يم ادر زین جلد او در تاج 
پشتی قرار دارد. , نشور ارام کف خانهن لاه 
ات و وش اس سا 
می‌ماند و چون دارای خلل و فرج و از آب 
ششک اتبت زوین ات قارع کرو وتا 
جریان‌ها و امواج دریابه ساحل ریسخته 
می‌شود. سا کنان کنار دریا آنها را جمع آوری 
می‌کنند و بنام کف دریا به فروش میرسانند. 
صدف این جانور در نقاشی و برخی صنایع 
بکار می‌رود؛ زید الحجر؛ حجر الحجشه؛ 
قلومن» باریقی» آذار افیون؛ ذار افبون» آذار 
یقون. کف سفید: (کد.) برف. کف مس: 
ماده‌ای است سفید مانند نمکثك که چون مس 
را بگذارند و در گوی ریزند تا سته شود 
مشت آبی بر روی آن ریزند و آن جوشی 
می‌زند و کفی از آن جوش بر روی آب 
می‌ماند. زهر اللحاس. ترکسات فعلی: کف بر 
لب آوردن: تولید شدن کف در اطراف لب.
```


## [2026-09-06T15:31:58.438Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\np='/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt'\nt=open(p,encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,pg in enumerate(pages):\n    m=re.search(r'\\[pdf page (\\d+)\\]',pg)\n    n=int(m.group(1)) if m else None\n    if n in (452,453,454,455):\n        print('==== pdf',n,'printed~',n+1205,'====')\n        print(pg[:2500])\nEOF"
}
```


### [2026-09-06T15:32:00.233Z] TOOL RESULT

```
==== pdf 452 printed~ 1657 ====
[pdf page 452]
acs 4

ومحنت و تنگی - و افشرد نکلورااگونند ‎٩‏ - کلف ‎A bay‏ - بممنی ید بیناس تکه
ودرعربی بمعنی بر روی درافکندن‌ویر گردانیین | ممجزة موسی علیهالسلام,بود . گویند ه رگاه
جامه باشد - و بکر اول لیز در فارسی بمعنی | میخواست ظاهر سازد دمتها را از بغل برمپآورد
رنج و محنت وسختی باشد ۴ - و درعربی‌بمعتی | نوری از دستهای او ‎ates lag‏ که تا بآسمان
جزا دادن - و مانند یکدیگرشدن - و توالایی میرفت +
ودامن خیمه باشد ۴ .

کف ] بگینه » بکر ‎gt‏ .آبی‌باشد
که مانند کف بر روی آبکینه پیدا شودبهنگام
کداختن ؛ و بعضی گویند ریم آبگینه است .
سفیدی ‎pte‏ را زایل کند و آترابس‌بی‌زبدالقوارس
وماءالزجاج خوانند وبیونانیمسحوقو نباوس حقونیا
کفاند ۴ © بروزن رساند؛یعنی بشکافد
و بترکاند , وشق کند بدرازی .*#

کگفاثه * = بر وزن ‎sale‏ بچه ای را
کوبند که نارس از شکم مادر پیفند .

کفانیدن ‎٩‏ = پروزن رسانیدن»بمعنی
شکافتن وترکالیدن بدرازی باشد ۷ .

فت ‏ بنتح اول بروزن رفت » ماضی
کفانیدن است ‎٩‏ یعنی شکافت و ترکایید وبمعنی
ت رکید و شکافته شد هم درست است - و ‎pe‏
‏اول مخفف شکفت باشد که از شکفتن وواتدن
است - و مخفف کوفت هم هست که از کوفتن
‎ach‏ - وبکر اول بممتی دوش وسردوش‌است*۱
و بعربی ‎GT‏ خوانند #۰

کفتر ".- بروزن دفتر » کبوتررا گوبند
و بعریی حمام خواتند .

‎CRT‏ بر وزن دفتری » شانه‌ردفتین
‎MAY >‏ و بافندگان باشد .

‎a wr‏ ختح اول بروزن هفتگی»

‎. ‏جهانگیری © رشیدی‎ : Ay ٩

‎Soule - ۴‏ در اول شرح این لفت گفته است . ۴ رك : اقرب‌الموارد +
منتپی‌الارب . ۴ - نوم شخص مفرد متارع از «کفاندن » ودکفالیدن © ‎Com)‏

‏۵ مقلوب و مصحف « فگانه » ‎V Cpa)‏ = کفالدن, متعدی کفتن = کافتن.
۴ - هیبتش الماس سخت را بکفاند چون بکفاند در چشم مار زمرد .
« منوچهری دامفانیس۱۷*.
۸ -(عی) کف ( بتشدید دوم ) بیضام. ‎٩‏ - ماضی «کفتن » است [ماض ی کفالیدن
«کفانید » است ).
*- مقلوب« کتف » : بیاوردکر زکران را بکفت سپه ماند از کار او در شگفت .
فردوسی طوسی « رشیدی * .
‎YY‏ رك :کبوتر . ۴ از : کفته )= کافته) ‏ کفتگ دی (حاسل مسدر) .
‎eth - oT ۵‏ اول ودوم وپنجم .کفایدن ‎Coa).‏
‏۵ کفتار - بفتح اول کردی ع ‎keftar‏ راب۳۳۹ >
‎kaftér or‏ ؛ نجانوری است از کوثتخواران , که از لحاظ
وضع دندان شبیه بکربه , ولی از لحاظ وضم چنگال مانند
سگه‌است , ازایشرو ‎LT‏ حد وسط دوخانواد مذ کورمیدانند .
‎we‏ ازجالوران مرده و نیم خوردة گوشتخواران دیگر تغذبه میکند .


==== pdf 453 printed~ 1658 ====
[pdf page 453]
شکافته شدن ‎aS gy‏ بودترا گوبتد .
‎Jal ca = ۱ oa‏ بروزنرفتن؛ بمعنی
آزهم بازشدن- وازهم‌باز کردن وشکافتن‌وترکانیدن
باشد؟ .
‎gal‏ 2 ۴ » بروزن فنقور . بسعلی‌نبات
است و آن ‎th‏ جهت بودن در اموروتعم لکردن
درآلام باشد .
گفقه ۴ ه بروزن هفته 1 بمعنی شکافته
شده وت ر کیده وشکفته باشد .
‎pe = GT‏ اول و سکون ثالی وجیم
فارسی ؛ مخفف کفچه است که چمچه باشد ۵
- و بممنی کف صابون و کف شیر و کف آب
دهن ‎٩‏ و امثال ‎oT‏ هم آمده است وآتراکفك
یز گوند وبسبی رغوه گوبند ۷ .
‎Aaa‏ - بروزن ‎ete‏ . دامن زین
اسب را گونند ۸ .
‎SRT‏ = بروزن جدول ‎BS‏ وسرین
اسب راکویند ‎٩‏ .

)0 خم۱ : دوريك .

: ‏قي‎ » KO ‏کافتن‎ Gee - ۱

۴ - جوهر ‎GT‏ است بمد ازهفت

۴ -ظ .بر ‎Gp GL‏ آپذ رکیوان .
‎sre 1‏
۸ - ازبی کفچك زین فرست صاحب خلد

6 _رك : کفچه .

. ‏-رك : جهانگیری‎ ٩

AT

‎k= PRIS‏ بای فارسی بروزن
مرزنگوش + بمعنی کفل‌پوش است وآن نوعی از
پوثش باشد که زر دوزی کنند و بر پشت اسب
اندازند ‎VT,‏ بترکی اورنك (۱) خوانند.
‎Zt‏ - با تحتالی‌مجهول بروزن

‏رستخیز ‎bee‏ بزرکه سوراخ دار را کویند
‎ys SST,‏ خوانند - و جالور کی را نیز
میگویند .که در آب میباشد ‎Lig py‏ مدورودمکی
باریك‌دارد*۱ . گویند ‎Sy‏ وزغ‌است درغلاف» یمد
از چند روز از غلاف بر میآید و ‎AT‏ بعریی
دعموص۱۱خوانند۱۴» و ‎aS gan‏ نوعی‌ازماهی
باشد وآ ترا سك ماهی خوانند ‎AF‏

‏کفچلیز لگ ۱۴- ‎Lt‏ کاف در آخر
بمعتی دویم کفچلیز است و ‎agile OT‏ کی باشد
درآ ب‌وبمروروز غ شودوعربان‌دعموس٩ ‎٩‏ خوانشدش؛
‎gy‏ گوبند موسمار کوچك است ؛ و بسنی
کونند جالورکی است شبیه بچلهاسه ودم سرخی
دارد - و کفگیر كوچك را نیز گفته‌اند.

‎۵

‏اه بروزن شنبلیله» بمعنی

‏که از او دل بخست وزهره بکفت .
سنائی غزنوی « رشیدی » « فرهنکه ‎of lls‏
۴ - اسم مفعول از « کفتن» = کافتن .
۷ سونیز نام قومی است. رك: کوچ .
کر بخواهی دهد از چادر حورا اطلی.
( سراج‌الدین سکزی ) « فرهنگه نظام *.

‏۰ - کنجلزك ‎me‏ کفچلیزه > فرهنگه نظام » ح

‏کفچلاز ‏ معرت ‎oT‏ قفتلیل .)4 : . 68 ۰ ۵ , ‎Siddiqi , Fremdworter‏ درکنابادی
‎Ly, ( kafcaliz‏ فورباغه ) « کنابادی » » در بروجردی 1۵501112 [ 1352 ( ‎by,‏ فورباغه )

‏«شهیدی ۰ .

‏۱- در رشیدی « دعمزی © آمده , ‎Age‏ اقرب الموارد گوید : الدعموس

‎ee)‏ دال و میم ) دويبة او دودة سوداء تکون فی الفدران اذا کت وقیل دودة لها رأسان تراها

‏فی‌الماء اذا قل.
‎oy Kap‏ عدوء کفچلیز کشت ‎pal‏

‏۴ کنچلیزك (هم.):

‏چوزین نهادی برجودی محیط آما .

‎. ‏آما‎ hig ‏رشیدی » و در فرهنگه نظام : برجودی‎ « Ssh

‏۴- در فاری بدین معنی استعمال کننده فرهنگه نظام >

‎. ‏کنچلیزك (هم) کنجلیز (مم)‎ = Ye

‏= کفچلیز, (هم) .

‏۴ کنپلیز(هم.)

==== pdf 454 printed~ 1659 ====
[pdf page 454]
‎7AM‏ کف خواستن
کنچلیزد است ک هکفگیر - وجانورکی ‎Sash‏ | خرمای‌ماده‌باشد وآتراکفراه با زبادتی‌ها و کفری

‏عربان دعموس خوانند . بجای الف بای حطی هم میگویند با تقدیدئالث
‎ORT -‏ = پروزن و ممنی ‎FP | ٩ come‏

‎VO gd LAL‏ - بنتح اول بمعتی
قفرالیهود است و آن نوعی از مومیائی باشد .
و بثیرازی مومیالی کوهی و مومیالی ‎od‏

‏- و پیچ وتاب سرزلف را لیز گوبند و بعربی‌طره
خواننه ۴ - ونوعی از مار هم حست ۴ .

‏کفچه نون ۴ - کنهه مسلوم و نون
مضموم ‎aly‏ و لام زده » مرغی است که منقار او
بکفچه میماند و بتر کی او را قاشق بورن‌خوانند

‏کف * 9 بنتح اول و ثالی و سکون
دال ابجد , یمنی بتر کد وبشکافد و از هم باز
‎Roy‏

‏کف ‎Gilt Go boo‏ ؛ چیزی‌باشد
سفید شبیه باستخوان پوسیده و آنرا بسربی
زیدالیحر گوند .

‏کفرا - منم اول وسکون ثاتی ورای بی

‎oo)
‏بسکون ابی ۰ کنابه‎ = Ape ‏کف‎
‏از مردم صاحب هت است که بسبب بخشندگی‎
‏و پریشان شده باشد ۸ - ویک تالی»‎ lie

‏برف را گوبند ‎not,‏

‏مد 4

‏بفتج اول وسکون ثانی
رشین نقطم‌دار ؛معروف
است که بای افز ارباشد انواع ‎oF‏

‏و معرب‌آن کوث است با ‎gly‏ و ثلی مثلثه .
قله بالف کشیده | بهار خرما را کوشد بل ‎A‏ خواسن « کنابه‌ازسف رکردن
‎BS‏ خرما - و بعض یکویند پوست بهاردرخت | وبفر رفتن ‎Ne‏ چنانکه کش ‎SONG‏

‏۱ کنج < کپچ < کپچه - کبچه. پهلوی ‎.kapcak‏ رك : ‎Pahlavi Texts,‏
‎-II,p. 154.‏ طبری ‎oval oily > (8) kaca‏ », کیلکی یز 5808 (فاشق ‎AS yy‏

‏۴ - رك : جپانگیری . - «کفچه مار » و * مار ‎iS‏ » ماریست بیار ‎Bp)‏
‏که کردن خود را مثل سرقاشق ۳ . اين مار درهند بسیار است ودر مشرق ابران هم‌هست
« فرهنگ‌نظام 4 در کنابادی نیز ‎MAT‏ 18162 گوبند «کنابادی © و وجه تسمیه شباهت‌سراوست
یکفچه ( قاشق ) . ۴ - در رشیدی «کفچه نول ‎(YW)‏ مرغیست ‎ABT‏ پهن ودراز
است . » و همین صحیح است ‎ag‏ « تول » (هم) منقار مرغان را گوند .

‏۵ رك :کفتن. ۲ - زیدالبصر ( 210702 0۳ ‎espéce‏ ) «دزی جاص۵۷۸*.

‏۲ ۲ قفرالیهودی « دزی ج۷ ص 4۷۷ 2 حمر ‎pan)‏ اول و فتح دوم) ‏ زفت‌البص
«عقار ۱5۸ ‎.bitume de Judée = asphalte‏ فیررادرعربی 9016۳ , درا کدی۵ا1۳ا16.
در آرامی 000072 » در ارمنی 0۲لا گوبند . رك : عفار ۱۹۸ ف .

‏۸ < کف سپید « رشیدی > . ‎٩‏ پهلوی 1215 «کجته ‎Dhl‏ » طبم
‎of ۲۰۰۱۹۳۹ ae. Chacha‏ طبری «کوش» ( باظهار واو ) > واژ‌نامه ‎٩۲۳‏ > . اشکاشمی
‎kaush‏ « گربرسن ۸۳ »۰ ‎SOS‏ 8150 . فریزندی , برنی ‎kawsh‏ ۰ نطنزی ‎Kkowsh‏
‏«. ۰۲۹۱۱ . شهمیرزادی ‎USK‏ سنگری, 16815« 2 .+ص۱۷۷و۱۹۱ > در ‎Bye‏
‏خرامان 6005 » استاد فروزالفر © . ‎CANE‏ بختم خنکا موزه بنه کفش بخواه .
آلوری آپیوردی « رشیدی ©

‎Cem) ‏بفتح اول وسوم , مخفف کافتن‎ - TF


==== pdf 455 printed~ 1660 ====
[pdf page 455]
-۱1۲- Pol

خوانند .
کف غنچه کردن 9 ‎ALS‏ از ‎any‏
‏کرد ساخئن ۴ ومشت کره کردن باشد .
‎poe - FCT‏ اولوسکون ابی‌وکان.
بمعنی کف باشد مطلفاً اعم از کف صابون و کف
آپ و کف کوشت و کف دهان و کف شیروامتال

آن .

کفل بس وزن
‎artes pital‏ وحیوانات
دیگر را گونند ۱ -و
پلاسی را نیز کوشد که
ستوران را بدان چار جامه
کنند وسوار شوند ۷ .

a
- ‏کفل پوش‎
‏نوعی از پوشش امب‌است‎
. ۸ ‏ترکان اورنك خواند‎ LT,

از اقلمت کردن و ازسقر بازماندن است.
فد ي © ‎ete‏ اول بروزن برزن :بمعنی
دشت و صحرا ‎ath‏ - و محلی را نیز کون که
قبل ازین‌غله کاشته بوده‌اند .

کفشیر - با شین قطه‌داربروزن ‎SS‏
‎yy‏ رااکوبند و آن داروبی باشد مانشد تم که
طلا و نقرء و فلزات دیگر را پیب آن با لحم
پیولد کنند ؛ و بعضی کویند .که قلعی وارزیزاست
و بدان شکتگیهای ظروف مس وبرنج رالحبم
کنند ۱ و بضی ظروف و آلات ‎ae‏
‏و برنج ‎SKF‏ راکنته‌الد که مکرر لحیم کرده
باشند ۴ .

کف ‎le‏ = 6 ثالی وعن‌بی‌قله
بالف کشیده , بیخ باتی است زرد تیره رنگه ,
گزندکی جانوران را افع است ‎er SUT,‏
ی زکویند ۴ و بعربی اصابعالصفر و شجرتالکف

: ‏عربی است‎ (qed) ‏بمعنی مطلق لحام‎ - ٩
‏خرد بشکستيم کنون شاید که کنی این شکسته راکفقیر.‎

? ممعود سعد همدالی لاهوری.دیوان ۴۶*۰

۴ - مجازاً بدین معنی است:
و شیر ‎Les‏ لظمی ومن چو شیر علم ‎Ole‏ تهی ومزور ؛ مزیق و کفشیر.
موزلی سمرقندی « رشیدی >.
۴ کف ‎State‏ مریم ‎Digiti citrini‏ «دزی ج اص 4۷۵ :۷۲ رث: کف‌مريم.
۴ کف غنجه کنی پراز گل نفمه شود از پن بهوا نقمه بر آمیکته است .
طپوری « رشیدی © .
6 بسی ‎NYT‏ :کف + که ( صفیر ) دانته‌الد > فرهنگه نظام» ولی بسکون دوم
استعمال میشود ؛ قس : کردی ۷6۳۵1 ‎OT)‏ دهن ‎(GS‏ « ژابا ص ۳۳۸ *
باز بکردار اشتری که بودمست کفک برآرد ز خشم وراند ملطان
مرد حرن کفکهاش پاگ بگیرد تا بشود نی ‎LS‏ و گردد رخشان.
‎Sry,‏ سمرفندی « تاریخ سیستان ص ۳۱۷ *.
شکفته لاله چوجام شراب و ژاله درو چوکفکه رخشان‌اندرمیان جام شراب. قطران «رشیدی».
1 -(عر) «کفل مح رکه » سرین؛ با پس مرن » با ‎be‏ دو ران » اکفال جمع ©

« منتهی‌الارب > . ۲ - باين معنی اصل «کفل پوش » (هدم.) است .
‎tere 4‏ دوخته‌ای که بر کفل حیوان باری وسواری انداژندکه در تکلمآشه‌مه‌است:
همه زین زرین یاقوت کار کفل ‎den‏ جواهر نگار .»

نظامی_کتجوی « فرهنگ نظام >
```


## [2026-09-06T15:32:17.023Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== IEC kauk ===\"\ngrep -n \"kauk\\|kāuk\\|kouk\" IEC.txt | head -20\necho \"=== PHD kaf ===\"\ngrep -n \"kaf\\b\\|kafk\\|kafčag\\|kabčag\\|kapčak\" PHD.txt PHD_mackenzie.txt | head -20"
}
```


### [2026-09-06T15:32:17.085Z] TOOL RESULT

```
=== IEC kauk ===
4605:ghaugho, io ‘rave, bluster, play the fool. (All forms ambig.) Gk. cf. kaükhos, kaükhe ‘boast; boasting’; kaukháomai, denom., id.; Ir. (ambig.) guag (folly'. Cf. ghaug-); OHG cf. gougulari *jugg- ler; MHG gougeln “play the fool, play pranks'; gougel *witchcraft beside (ambig.) gougern (Crove, See ghaughor-); Latv. (ambig.) gau£Zu, gauzt ‘rave, twaddle’
5912:$uhuo (£houo), ið “call, shout, resound’. WP I, 529. Cf. £uhen-, guhon- & next Vedic háve, huvámi, huve; Skt. hváyàmi, pl. base: juhv-; Av. zbayemi, id. beside redup: zaozaomi (:Gk. kaukháomai “call, boast), and zavai(mi) ‘curse’; OPer. a-zbayam, 1 sg. pf. ʻI
5917:proclaimed'; Arm. n-zovem (‘curse’: Skt. ni- hváye, pl. ni-juhv-); Gk. kaukháomai, redup.; OLat. havet, 3s. (“hails?. Osthoff); Go. cf. gau- non ‘complain’; ON geyja ‘bark’; Norw. gjó “bark, clamour’; OS zovg, zvati; OCZ. zovu beside Cz. zvu, inf. zváti; Srb. zovem, zvati beside zujim, züjati, v. “hum, buzz’; Li. žaviù, éti ‘conjure, bewitch’; Latv. zavēju, id.
5939:ĉhauĝh- (variant of ghaugh-, q.v.) ‘cail, shout, bluster’. WP I, 529 & gukug Av. zaozaomi ‘implore’; Gk. kaukháomai ‘boast’; kaŭkhos, kaúkhē, s. ‘boasting’; (with *gh-) Latv. gaužu, gauzt ‘rave, twaddie’
6856:kāt- (kütol-) — kauko, ið
6867:kaug- “shout”, etc.; kauk- ‘raucous bird’, see kāuk-
6868:kauk- (1) ‘skull’, (2) ‘height, pile’, etc. see following entries and cf. kaukos
6869:kaukol-os (1) ‘skull, basin, trough'. WP I, 331. Cf. kaüKos Per. cf, kafce (-ladle" LW in R kovš, id.); Gk. kaukálion ‘vesseľ, kaükalon ('skull'. Ambig. cf. kauK-); Li. káukolis, io, m. and káukole, es, f. ‘skull’; Finn. LW kaukalo “trough?
6870:kaukol- (kauk-) (2) an umbelliferous plant (same as (1)?) Skt. cf. kokam (‘red lotus’ or sim.); Li. kaŭ- kis, io, m. *hedge-parsley'; Gk. cf. kaukalís “an umbel. plant?
6871:kaukol- (3) "a bird’. Cf. kauko, ið, kaukos (1) Skt. kokilah (“Indian cuckoo'; also “mouse, snake, insect'!); Hes. cf. kaukalías (a bird); Li. kauklys ‘siren, hooter’
6872:kaukoros ‘height, hill. Cf. kaukos (2) Li. kaükaras, -à, m. f., id.; cf. (Medic?) Cau- casus, and (Celtic?) placename Cauca (in Spain) and Cauco-liberum (in France).
6873:kauko, ið ‘shriek’. Cf. Kauk- and next. Cf. WP I, 331, 371 & 466 Skt. koCami, id.; Arm. kawSem, id.; Tokh. B cf. sauk- ‘call, name”; Gk. kaukízomai ‘revel’; Ir. cf. cuach-ghail, cpd. s. ‘whinny’; Ukr. cf. dokucyty ‘egg on Blg. cf. kuče, n. ‘dog’; Li.
6875:kaukiù, ^ti ‘hoot, how" beside (variant) šau- Ku, “ti ‘shout’; Latv. kaucu, kaukt, as Li. beside saukt ‘shout’; Cz. cf. s-kucet ‘howl. Variants of type *kauks- and *kauksK- in Li. kiauksiu, eti *howl" and Latv. Caukstu, et, id. Cf. also Cz. kusna (*mouth, mug’, fr. *kauk- sina)
6876:kaukos (1) ‘shriek, howl, clamour, call", Variant: kāuk- as separate entry, cf. also kauko above. Cf. WP I, 331, 371 & 466. Extn. mng. ‘howler’, etc. Skt. kókah "wolt" beside (variant) kau$ikah ‘owl’; Ir. cuach ‘cuckoo’; Blg. kuk, id. beside kuče ‘dog’; OCS cf. kuctka ‘bitch’; Li. kaükas (‘goblin, mandrake, thunderbolt’ in folklore); kaukýs ʻa raucous bird'; kiáuke ‘jackdaw’; Latv. kaukis (‘bawler; blackcap’ ornith.); cf. (variant) Slovene čuk ‘owl’. (Isophonic: LLat. caucus ‘concubine’ and Alb. kakë- in kakë- zozë ‘salamander’: Latv kaukis, kaukis (2), m. ‘toad’. The Alb. form suggests a prototype *kauko-dieudio)
6877:kaukos (2) ‘high; height, hill hump’. (Variant: kauK-) Skt. (variant) koS$yau, dual no. ‘two glands near horse's heart; Tokh. A koc, B kauc, kaus (&high'; adv. "op: Go. hauhs, OHG hoh, OE heah, ON hár ‘high’ beside OHG houg, MHG houc, ses, G Haug, ON haugr fhill- ock, mound’; Sw. hög ‘high; hill; R küca ‘pile’; Li. kaükas ‘boil, neck-gland of pig’; extn. in kaukaras, kaukure (f hilltop', etc.). A variant arises in Li. káuge 'pile'; Latv. kaudze, id.
6878:kauks-, see kauko, ið
6879:kauKos, à, io “shell, skull, bowl, cup’. Cf. kaukolos, etc. WP II, 548-551 Skt. kosah “shell, cup, pail, box, cask’; kośam, id.; cf. koSika, kausika ‘goblet; case? (dim.); Per. cf. kofče (Cladie'. LW in R kovš, id.); Oss. küsi, id.; Gk. (gloss) kaükos ‘cup’; Kaka ‘skull’; kaukíon, dim. ‘cup’; Maced. kausia ‘felt hat worn by kings’; Lat. caucum (LW? as Gk. kaükos); MIr. coach Ir. cuach “bowl, cup’; W cawg ‘dish’; ON hauss ‘skull’; Du. (?) hauw ‘siliqua, poď’; Li. kiáušas ‘skull, cup made from a skull, shell; dial. kaušas ‘ladle, Skull; kiáušē, f. *skull; kiaušis, io, m. ‘egg’;
6880:kaukos — kaustos, kautos
6902:kaukos, is, à (kauk-) “a raucous bird’. WP I, 33] Skt. kókah (2) ‘red goose, cuckoo’; Hind. koki ‘crow’; Sind. kok, m. ‘cuckoo; frog’; Per. kabg ‘partridge’; Tokh. A cf. kokafi “an un- identified bird”; Gk. kéux, gs kéukos “a gull’ beside kábéx, kaúēx, id.; Sard. coca ‘goose’ beside Sard. (Campid.) coga (^witch', cf. mngs. of Lat. strix); Ir. cuach ‘cuckoo’; W cawci (jackdaw': Hind. koki); Cz. kavka, Pol. kawka “daw”; Srb. cf. (variant) Cavka, id.; Li. kaukys, m. “a shrill bird’; kiauke ‘daw’; Latv. kaukis *blackcap gull'. (A similar onomat. element is present in Hind. kauwa ‘crow, daw? and in Fr. cahouette, id.)
6914:käng, ið (küu-) (2) ‘howl, croon’. Cf. kauk-,
=== PHD kaf ===
PHD.txt:422:kabk [АрА! | N ~] partridge. ~-anjir [acyl | N ~] a kind of francolin. kabód [kpwt! | N ~] grey-blue; pigeon. kabótar [kpwil | M kbwtr, N ~] pigeon. kāč [с | N kāš(ki)], ~ ka: would that, if only. кадар [01А] game, joke. кадар [ktk' | M kdg, N kada] house. ~-banig [-b'mwk! | N Radbanü] mistress, lady of the house. ~ig [-yk'] domestic; servant. ~-xwaday [-hwty | P gdyxwd?y, N kadxudā] householder, master of the house. kadām [ktm | M kd?m, N кийат) which, what. c--iz-é(w) [-c-H D] whichever. kadar [kt] who, which. 7-iz-é(w) [-c-H D] whoever. kaf [kp | N —] foam, slime. kaf-, v. kaftan. kafč [kpc | N ~] ladle, skimmer. ~ag [-А! | N ~a] spoon. kafš, ~ag [kps, -k! | N Аар] shoe. ~gar [-k/ | N ~] shoemaker. kaftan, kaf- [kp-in' | P kft, kf-] fall. kah [TBNA < A tbr | N ~] chaff, straw. kān-, ~i§n, v, kāstan. _ kahas [kts | М khs] channel, sewer. kāhēnīdan, káhén- [R'hyn-ytn!] decrease, lessen (tr.). kühidan [P hytn! | N ~] = kastan. kahist [ksst'] least. kah-rubāy [Ара | N —rubá] amber. kahwan [khwbn' | M qhwn, N kukan] old. kākom [RP Rkwm | N ~] stoat. ~ i spéd: ermine. kālbod [Аро | (M k*/byd), N ~] body, shape, form. ~ӧтапа [-wmnd] corporeal. kam [km | M kmb, N ~] little, small, few; v. kem. kam [Em | = M, N ~j will, desire, purpose. kàm-, v. kāmistan. 1катаб [k?mk! | N kama] kinds of gruel, or soup. ?kümag [k?*mk! | N kama] = kam. «-hanjām [-hnc’m] gaining one’s end, successful. -~-hanjamih: success. „ūmand [-wmnd] willing(ly), desirous. ~-widar [-wt?l | N kām-gučār] successful, independent. ~-xwaday [-Awt^y] independent, absolute. kamal [kml | (M km?7)] head (daevic). ~ig [-yR!] chief (daevic).
PHD.txt:538:pādīrān [p'igP n!] restrained, held back. pādīrān(ēn)īdan, pādirān(ēn)- [þptgľn(yn)-ytn'] restrain, impede. padīriftan, padir- [MK BLWN-tn!Ü < A mqbl, V qbl; ptgl-ptn! | M pdyr-yptn, N paóiruftan] receive, accept. ~išn: reception, acceptance. īpadisār [ptys' | N padīsār ?] beginning, basis. tpadisār [ptys’/] bridle, halter. padisāy [pts’d | M рдуу] on account of, for the sake of. padist [ptst! | P pdyst] promise, vow. & (abar) burdan: promise. padistadan, padist- [ptyst-”tn! | (P pdystwd)] promise, vow. padistā(£) [ptyst*k! | (M pdystw)] = padist. padiš (pts | M pdys] to him, it; postposition (= pad) to, etc. padištān [pryst?n' | P pdyst??n] leg. padišxwar [ptshwl] dish, bowl. pādixšā(y) [SL Y TA < A йур; p’ths?(d) | M раху] ruler; powerful, authoritative, authorized. ~ЛЬ : sovereignty, authority. pādixšīr [p’thsyl] agreement, treaty. pad-néróg [PW Nnylwk!] strong. pad-niģerišn [PWNnkylin'] cared for, guarded. pādofrāh [p’twpl’s) = pādifrāh. pad-panag [PWNpnk!] guarded, protected. Р pádrazm [p’tlcm] battle. pàd-rózag [p’tlwck' | M p'drweg] fasting. pād-uzwān [p’??wzw’n'] reticent. ~ih: reticence. pad-wizén [PW Nwcyn!] choice, select. pādyāb [pty | N ~] ritually clean; ceremonial ablution. ~ih : ceremonial ablution. pādyāwand [p?tyd’wnd | J p'dywnd] strong, powerful. cAh : strength, superiority. pádzahr [p’tzhl | N pa(d)zahr] bezoar, antidote. pad-zyān [PWNzyd"?n'] harmful. pafšār- [pps?/-] shame. pafšīr- [ppsyl-] be ashamed. ~i8n(ih): shame. pah [p’h] sheep. ~ast [-st'] sheep-fold, -pen. pahikaftan, pahikaf- [ptkp-tn! | M phykf-] fall on, touch, hit, attack. ~išn: attack, fight. pahikāftan, pahikāf- [ptk’p-in'] throw on, make fight. pahikar [ptk] | M phykr, N paykar] picture, image. pahikār [ptk?! | M phyk”r, N paykār] struggle, battle, dispute. īpahikār- [ptk?/-] fight, contend with, defeat. pahikardan, *pahikār- [ptk’/-tn'] request, claim, consult.
PHD.txt:1986:foam kaf.
PHD.txt:2546:ladle kafč.
PHD.txt:3634:shoe kafš, még, mozag.
PHD.txt:3684:skimmer kafč.
PHD.txt:3695:slime kaf, lajan.
PHD.txt:3786:spoon kafčag.
PHD.txt:4540:salag! škaf- škāftan nibay-! nibastant ških- šken(n)- šken(n)išn škēbāgīh škēbāg škeftīh škeft 1*$kķēh &kohih škūf- škūfag škoft škuftan hur!, šakar škarw- škarwīdan škarag škastan škaft
PHD.txt:4615:pattügih pattüg paywastan paywastag pattüdan pahikar 1-2pahikar- pahikardan pahikāf- pahikāftan pahikob- pahikoftan pahikar pahikaf- pahikafián pahikaftan payrastan payrog pahrmāh- pahrmāhāgīh pahrmāhišn paymāy- paymānīgīh paymānīg
PHD.txt:4978:kafé kafčag kafš kafšag kafšgar kaftan kaš, kiš keš- kešīdan kišnīz kasawag kašk kaStig kadar
PHD.txt:4987:kardagān 1%kardāg kam kamāndār kamān kamāl kamālīg kamistīh ‘kamist kamzor kamzorih kamar kamarband maygt arz! kastār kastärīh kchtar kaf
PHD.txt:4988:kaf- "kabāh kabārag kabīg kabiz
PHD_mackenzie.txt:3123:kal: [k)c I N kaf(ki)], ~ ka: would that, if only.
PHD_mackenzie.txt:3135:kaf [kp I N --] foam, slime.
PHD_mackenzie.txt:3136:kaf-, v. kaftan.
PHD_mackenzie.txt:3142:kaftan, kaf- [kp-tn I P kft, kl-] fall.
PHD_mackenzie.txt:3325:kaf [kwp I = M, N kOh] hill, mountain; hump.
PHD_mackenzie.txt:3967: pahikaftan, pahikaf- [ptkp-tn l I M phykf-] fall on, touch, hit, attack.
PHD_mackenzie.txt:3969: pahlkaftan, pahikaf- [ptk)p-tn l ] throw on, make fight.
```


## [2026-09-06T15:32:18.003Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== NYB kaf ===\"\ngrep -n \"^kaf\\| kaf \\|kafk\" NYB_vol2_glossary.txt | head -20\necho \"=== HUB kaf ===\"\ngrep -n \"kafa\\|kaf \" HUB.txt | head -20"
}
```


### [2026-09-06T15:32:18.062Z] TOOL RESULT

```
=== NYB kaf ===
1716:kaft. Pagliaro’s reading dar-andarzpat is unacceptable. Cf gurtéh.
2158:kaftan (Prth) [NPL-] to fall, pret. 3d p. sg. NPL-t = kaft HajA:8. — MPrth pt. kft, pres. gf-, Ghilain 56. — Cf patkaftan and kahvanéh.
=== HUB kaf ===
2815:Praesens SiUdfam ist als iranische Wurzel skaf =
3046:iap, kab oder kabh) und kafam (arisch kaph\ Sal.
3050:Vullers kafam (arisch kaph) lautet. Vgl. ia/'fissura,
6505:b) zu / in: kaf Schaum' = zd. ka/a-, phi. kaf Gl. and
6535:pr. sikafam, sikaf spaltend, Spalt' von iran. skaf = skaph
6537:pr. kafam (nach Vullers, kavam Sal. Shiik., s. oben p. 86),
6538:kaf *Spalt* von iran. kaf = kaph neben gr. xdnsTog, ksl.
6592:d. i. kap'herg = mp. *kap'kdh fiir phi. kofikaf Bdh. 21, 2
```


## [2026-09-06T15:32:36.311Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\np='IEC.txt'\nt=open(p,encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\n# find leaf index of a given line number\nimport bisect\nffpos=[i for i,l in enumerate(lines) if '\\f' in l]\ndef leaf_of(ln):\n    return bisect.bisect_left(ffpos, ln-1)\nfor ln in (6869,6879,6902):\n    lf=leaf_of(ln)\n    print(ln, 'leaf', lf, 'printed ~', (lf-15)*2)\nEOF"
}
```


## [2026-09-06T15:32:37.600Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN chance/occasion/cadere ===\"\ngrep -n \"chance, n\\.\" KLN_1966.txt | head -5\ngrep -n \"occasion, n\\.\\|cascade, n\\.\\|decay, intr\\|accident, n\\.\\|incident, adj\" KLN_1966.txt | head -10"
}
```


### [2026-09-06T15:32:38.252Z] TOOL RESULT

```
6869 leaf 271 printed ~ 512
6879 leaf 272 printed ~ 514
6902 leaf 273 printed ~ 516
```


### [2026-09-06T15:32:38.308Z] TOOL RESULT

```
=== KLN chance/occasion/cadere ===
```


## [2026-09-06T15:32:44.235Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '6855,6885p' IEC.txt | cat -A | grep -n \"\\^L\" | head\necho \"---- plain ----\"\nsed -n '6860,6885p' IEC.txt | head -40"
}
```


### [2026-09-06T15:32:44.295Z] TOOL RESULT

```
21:kaukiM-CM-9, ^ti M-bM-^@M-^Xhoot, how" beside (variant) M-EM-!au- Ku, M-bM-^@M-^\ti M-bM-^@M-^XshoutM-bM-^@M-^Y; Latv. kaucu, kaukt, as Li. beside saukt M-bM-^@M-^XshoutM-bM-^@M-^Y; Cz. cf. s-kucet M-bM-^@M-^Xhowl. Varia^Lnts of type *kauks- and *kauksK- in Li. kiauksiu, eti *howl" and Latv. Caukstu, et, id. Cf. also Cz. kusna (*mouth, mugM-bM-^@M-^Y, fr. *kauk- sina)$
---- plain ----
33
40
45
480
rys, id.
kaud- (form of kauo, küd-, q.v.) ‘strike’ Tokh. A kot-, B kaut- “split, eut: Lat. cauda “tail beside cüdo, Gre ((forge', fr. the cpd. forms?); cf. also caussa, causa (“matter, affair, thing, cause, party, sickness', fr. *kaudsa, cf. the semantics of Gk. tüpos “form, model, writ, etc. and Norw. Sw. slags (sort); OCS pro-kuzdo -kuditi “harm, corrupt, ruin”; pro- kuda, -kuZzda run: Srb. kuditi Chlame cf. Lat. caussa ‘blame’ also). A possible incep- tive form may arise in OCS, Pol. kusiti, kusic ('try, tempt’, fr. *FkaudsKo, 1sg. kušọ). Cf. Srb. Pol. kus, kusy ‘docked’
kaudst- (extn. of kaud-, q. v.) ‘cutting down, cut, section’ Skt. cf. kosthah ‘bowels’; ON haust, Sw. höst ‘harvest’; Li. kaustyti, v. ‘forge’.
kaug- “shout”, etc.; kauk- ‘raucous bird’, see kāuk-
kauk- (1) ‘skull’, (2) ‘height, pile’, etc. see following entries and cf. kaukos
kaukol-os (1) ‘skull, basin, trough'. WP I, 331. Cf. kaüKos Per. cf, kafce (-ladle" LW in R kovš, id.); Gk. kaukálion ‘vesseľ, kaükalon ('skull'. Ambig. cf. kauK-); Li. káukolis, io, m. and káukole, es, f. ‘skull’; Finn. LW kaukalo “trough?
kaukol- (kauk-) (2) an umbelliferous plant (same as (1)?) Skt. cf. kokam (‘red lotus’ or sim.); Li. kaŭ- kis, io, m. *hedge-parsley'; Gk. cf. kaukalís “an umbel. plant?
kaukol- (3) "a bird’. Cf. kauko, ið, kaukos (1) Skt. kokilah (“Indian cuckoo'; also “mouse, snake, insect'!); Hes. cf. kaukalías (a bird); Li. kauklys ‘siren, hooter’
kaukoros ‘height, hill. Cf. kaukos (2) Li. kaükaras, -à, m. f., id.; cf. (Medic?) Cau- casus, and (Celtic?) placename Cauca (in Spain) and Cauco-liberum (in France).
kauko, ið ‘shriek’. Cf. Kauk- and next. Cf. WP I, 331, 371 & 466 Skt. koCami, id.; Arm. kawSem, id.; Tokh. B cf. sauk- ‘call, name”; Gk. kaukízomai ‘revel’; Ir. cf. cuach-ghail, cpd. s. ‘whinny’; Ukr. cf. dokucyty ‘egg on Blg. cf. kuče, n. ‘dog’; Li.
481
kaukiù, ^ti ‘hoot, how" beside (variant) šau- Ku, “ti ‘shout’; Latv. kaucu, kaukt, as Li. beside saukt ‘shout’; Cz. cf. s-kucet ‘howl. Variants of type *kauks- and *kauksK- in Li. kiauksiu, eti *howl" and Latv. Caukstu, et, id. Cf. also Cz. kusna (*mouth, mug’, fr. *kauk- sina)
kaukos (1) ‘shriek, howl, clamour, call", Variant: kāuk- as separate entry, cf. also kauko above. Cf. WP I, 331, 371 & 466. Extn. mng. ‘howler’, etc. Skt. kókah "wolt" beside (variant) kau$ikah ‘owl’; Ir. cuach ‘cuckoo’; Blg. kuk, id. beside kuče ‘dog’; OCS cf. kuctka ‘bitch’; Li. kaükas (‘goblin, mandrake, thunderbolt’ in folklore); kaukýs ʻa raucous bird'; kiáuke ‘jackdaw’; Latv. kaukis (‘bawler; blackcap’ ornith.); cf. (variant) Slovene čuk ‘owl’. (Isophonic: LLat. caucus ‘concubine’ and Alb. kakë- in kakë- zozë ‘salamander’: Latv kaukis, kaukis (2), m. ‘toad’. The Alb. form suggests a prototype *kauko-dieudio)
kaukos (2) ‘high; height, hill hump’. (Variant: kauK-) Skt. (variant) koS$yau, dual no. ‘two glands near horse's heart; Tokh. A koc, B kauc, kaus (&high'; adv. "op: Go. hauhs, OHG hoh, OE heah, ON hár ‘high’ beside OHG houg, MHG houc, ses, G Haug, ON haugr fhill- ock, mound’; Sw. hög ‘high; hill; R küca ‘pile’; Li. kaükas ‘boil, neck-gland of pig’; extn. in kaukaras, kaukure (f hilltop', etc.). A variant arises in Li. káuge 'pile'; Latv. kaudze, id.
kauks-, see kauko, ið
kauKos, à, io “shell, skull, bowl, cup’. Cf. kaukolos, etc. WP II, 548-551 Skt. kosah “shell, cup, pail, box, cask’; kośam, id.; cf. koSika, kausika ‘goblet; case? (dim.); Per. cf. kofče (Cladie'. LW in R kovš, id.); Oss. küsi, id.; Gk. (gloss) kaükos ‘cup’; Kaka ‘skull’; kaukíon, dim. ‘cup’; Maced. kausia ‘felt hat worn by kings’; Lat. caucum (LW? as Gk. kaükos); MIr. coach Ir. cuach “bowl, cup’; W cawg ‘dish’; ON hauss ‘skull’; Du. (?) hauw ‘siliqua, poď’; Li. kiáušas ‘skull, cup made from a skull, shell; dial. kaušas ‘ladle, Skull; kiáušē, f. *skull; kiaušis, io, m. ‘egg’;
kaukos — kaustos, kautos
15
20
25
30
35
```


## [2026-09-06T15:32:51.871Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"cadere, to fall\\|caden tia\\|cadentia\\|occasio\\b\\|occasi5\\|cascade\" KLN_1966.txt | head -20\necho \"=== SKT ===\"\ngrep -n \"^chance\\|chance\\. (F\\.\\|occasion\\|cascade\\|decay\" SKT.txt | head -20"
}
```


### [2026-09-06T15:32:51.949Z] TOOL RESULT

```
6073:-cade,  suff.  denoting  a  group  or  the  contest  of  a group.  —  Adopted  fr.  the  suff.  -cade  in  caval¬ cade  (q.v.);  accordingly  this  suff.  is  the  equi¬ valent  of  L.  -(i)catus.  See  2nd  -ade  and  cp.  aqua¬ cade,  motorcade  and  subst.  suff.  -ate. cadence,  n.  —  F.,  fr.  It.  cadenza,  fr.  VL.  *cadentia, a  fern,  noun,  fr.  L.  cadentia,  neut.  pi.  of  cadens, gen.  -entis,  pres.  part,  of  cadere,  ‘to  fall’,  which is  cogn.  with  OI.  sad-,  ‘to  fall  down’,  Arm.  ( ac- num,  ‘to  fall,  become  low’,  and  possibly  also with  Ir.  casair,  W.  cesair,  Co.  keser,  ‘hail’.  Cp. chance,  which  is  a  doublet  of  cadence.  Cp.  also accident,  cadaver,  cadenza,  caducity,  cascade, case,  ‘condition’,  casual,  cheat,  chute,  coincide, decadence,  decay,  decheance,  deciduous,  escheat, incident,  occasion,  Occident,  parachute,  recidivist. Derivatives:  cadence,  tr.  v.,  cadenc-ed,  adj., cadenc-y,  n.
6074:cadenza,  n.,  an  ornamental  flourish  (music).  — It.,  fr.  VL.  *cadentia;  prop,  ‘a  flourish  before the  cadence’,  whence  its  name.  See  cadence, cadet,  n.,  1)  a  younger  son  or  brother;  2)  a  stu¬ dent  at  a  military  or  naval  school.  —  F.,  fr. Gascon  capdet,  which  corresponds  to  OProven?. capdel,  ‘chief’,  fr.  VL.  *capite!lus,  dimin.  formed
6653:cascabel,  n.  —  The  same  as  cascavel. cascade,  n.,  a  waterfall.  —  F.,  fr.  It.  cascata,  fr. cascare,  ‘to fall’, fr.  VL.  *casicdre, freq.  formed  fr . L.  casus,  pp.  of  cadere,  ‘to  fall’  (see  cadence); introduced  into  English  by  the  diarist  John Evelyn  (1620-1706).
6654:Derivative:  cascade,  intr.  v. cascara  sagrada,  n.,  a  laxative  drug.  —  Sp.,  lit. ‘sacred  bark’.  Sp.  cascara,  ‘bark’,  comes  from cascar,  ‘to  break’,  from  VL.  quassicare,  freq. of  L.  quassare,  ‘to  shake  violently’,  itself  freq. of  quatere  (pp.  of  quassus),  ’to  shake’ ;  see  quash, ’to  make  void’,  and  cp.  casco,  cask.  Sp.  sagrada is  fern,  of  sagrado,  fr.  L.  sacratus,  ‘sacred’,  pp. of  sacrare,  ‘to  consecrate’;  see  sacred, casco,  n,,  the  hull  of  a  ship.  —  Sp.,  ‘potsherd, shell,  skull,  helmet,  cask;  hull  of  a  ship’,  fr. cascar,  ‘to  crack,  burst’,  fr.  VL.  quassicare.  See prec.  word.
7167:chance,  n.  —  ME.  cheaunce,  cheance,  chance,  fr. OF.  cheance,  chance  (F.  chance),  fr.  VL.  *caden- tia,  ‘a  falling’,  esp.  ‘a  falling  of  dice’,  fr.  L. cadentia,  neut.  pi.  of  cadens ,  pres.  part,  of  ca¬ de  re,  ‘to  fall’.  See  cadence.
10450:Derivatives:  debut,  intr.  v.,  debutant(e),  (q.v.). debutantfe),  debutant(e),  n.,  one  who  makes  a debut.  —  F.  dibutant,  fern,  debutante,  pres.  part, of  debuter.  See  prec.  word, deca-,  before  a  vowel  dec-,  pref.  meaning  ‘ten’.  — Gk.  8ex<x-,  fr.  S£xx,  ‘ten’,  cogn.  with  OI.  ddsa, L.  decern,  Goth,  taihun,  OE.  lien,  ten,  ‘ten’. See  ten  and  cp.  decade,  decern-, decachord,  n.,  a  harp  with  ten  strings.  —  Gk. Sexa/opSoi;,  ‘ten-stringed’,  fr.  Ssxa,  ‘ten’,  and yopSf],  ‘string’.  See  chord, decad,  n.,  the  number  ten.  —  See  decade, decadal,  adj.,  pertaining  to  ten;  consisting  of groups  of  ten.  —  See  decade  and  adj.  suff.  -al. Derivative:  decadal-ly,  adv. decade,  n.,  1)  a  group  of  ten  things;  2)  a  period of  ten  years.  —  F.  decade,  fr,  L.  decas,  gen. decadis,  fr.  Gk.  Scxap,  gen.  SsxaSo?,  ‘the  number ten;  a  group  of  ten’,  fr.  8£xa.  See  deca-. decadence,  decadency,  n.,  deterioration,  decay. —  F.  decadence,  fr.  ML.  decadentia,  ‘a  falling down’,  fr.  *  decade  re,  ‘to  fall  down’,  fr.  de-  and L.  cadire,  ‘to  fall’.  See  cadence  and  cp.  deche- ance.  For  the  ending  see  suff.  -ence,  resp.  -ency. Cp.  also  decay,  deciduous.
10497:Derivatives:  deceptive-ly,  adv.,  deceptive-ness,n. decern,  tr.  v.,  to  decree.  —  F.  decerner,  fr.  L.  de- cernere,  ‘to  decide,  determine’,  pp.  decretus. See  decree  and  cp.  concern,  discern,  secern, decheance,  n.,  forfeiture.  —  F.,  ‘fall,  downfall, forfeiture’,  fr.  ML.  decadentia,  ‘a  falling  down’. See  decadence.
25975:oc-,  assimilated  form  of  ob-  before  c. ocarina,  n.,  a  small  wind  instrument  with  finger- holes  and  a  whistle  mouthpiece.  —  It.,  dimin.  of oca,  ‘goose’,  fr.  VL.  *auca,  ‘goose’,  whence  also OProvenf.  auca,  OF.  oue,  oe,  F.  oie,  ‘goose’.  VL. *auca  is  a  contraction  of  *avica,  back  formation of  L.  avicula,  dimin.  of  avis,  ‘bird’.  See  aviary and  cp.  the  second  element  in  pettitoes.  For  the sense  development  of  VL.  *auca,  ‘goose’,  fr.  L. avis,  ‘bird’,  cp.  Gk.  fipvtg  (masc.  or  Jem.),  ‘bird’, (masc.)  ‘cock’;  (fern.)  ‘hen’,  ModGk.  opvi&ot, ‘hen’.  The  instrument  was  called  ocarina  (lit.  ‘a goose  pipe’)  in  allusion  to  its  shape, occasion,  n.  —  Late  ME.  occasioun,  fr.  OF.  (  = F.)  occasion,  fr.  L.  occasionem,  acc.  of  occasio, ‘fit  time,  opportunity,  occasion",  fr.  occasus,  pp. of  occidere,  ‘to  fall  down,  fall',  fr.  ob-  and  cadere, ‘to  fall’.  See  cadence  and  -ion  and  cp.  Occident. Derivatives:  occasion-al,  adj.,  occasionalism (q.v.),  occasion-al-ity,  n.,  occasional-ly,  adv. occasion,  tr.  v.  —  F.  occasionner,  fr.  occasion.  See occasion,  n.
=== SKT ===
54:TttK  present  work  is  not  a  mere  abridgement  of  my  larger  Etymo- lopcal  Dictionary,  such  as  might  have  been  compiled  by  a  diligent book-maker,  but  has  been  entirely  rewritten  by  myself;  and  1  have Coand  that  the  experience  gained  by  writing  the  larger  work  has  been of  considerable  assistance  to  me  in  making  occasional  slight  improve- ments. My  object  has  been  to  produce  a  convenient  hand-book  for tbe  o«e  of  thai  increasing  number  of  students  who  wish  to  learn the  bistoTT  of  the  English  language,  and  who  naturally  desire  to  have Anglo-Saion  and  Icelandic  forms  presented  to  iliem  rightly  spelt  and ftOOcnniAted,  a  point  which  seldom  receives  sufficient  attention.
63:In  the  course  of  writing  this  abridgement,  I  have  taken  occasion U  several  corrections,  which,  in  the  larger  work,  are  only  to
2586:(K.  -  L.>     F.  .<1(^ rtfai>m<M»   decay.  ■»
2590:decay,  to  fall  into  ruin.  (F.-L.)  O.  F. circatr.mmO,  F.  i/if- ;  and  eacr,  to  fall.  — L.  lit, down  ;  and  cotitrr,  to  fall.
2594:occasion.  (F.  — L.)  — 1*.  ot-cojion.  —  X.. ace.  oiiasidM^m.  —  'L.  oc-  (for  eb,  at);  and casus,  pp.  of  (Otiertf  to  fall.
2732:chancel,  (F.-L.t    .Sn  cnllrd orig.  fenced  ofT  by  a  Im: . chancel ,  an  enclostire   '■  -'tk
2734:chancellor.  (F.-L,>    O.Y.c
2736:chancery.    <F.-L)      For   <km M.  £.    ckanctUrit.'-O   F.    t^atuMiai
10198:■  ■  decay.
10236:ian,  to  betray,  from  irw,  an  occasion,
10238:thus:  occasion,  opportnnity.  betrayal,  eo^
11984:mother  {\),  lees,  mouldinesa    ( G.)     Properly  muMer,  1ml  atlerwl fusion   with    M.  E.    mpder,    a    mot O.  Du.  moitJer,  mud  ot  niiie,  aho  t^ diegs,  or  'the  mother  of  wiiie  and Hexham.   +    G.     moJer,     mud. mouldering     decay ;     which     it snmctimea    called    mutter    (lit. Extended  from  the  word  above.
12587:Obsolescent,  k*^*'"S  *^^  ^^  ^^'  (^) From  pres,  pt.  of  L.  ohioUsure,  to  grow old,  inceptive  form  of  oSioJtre,  to  decay. Doubtful ;  perhaps  from  L.  «3,  against ; s»i4rr,  to  be  wont
12739:s  u  oncht  (below). rt  For  affine.  the  initial BS  in  mmd,  van^%uxrd^ jove).     Der.  lane  iy. tn   phr.  yi>r  /Ar    ffiTiw#, tff.     Here   then    is   for 'the  dcf.  article;  anes^ U  a  lb.,  is  properly  an fbclow).     The  H31SC  is for  the  occasion. !.  E.  ontj ;    A.  S.   dtus, gen.   ca^e  (mosc.   and the  geo.  case  was  used
13628:Pedlar.  Pedler,  Peddler,  a  dealer  in small  wares.  (Scand.  ?  or  C.  ?)  The  old word  was  usually  peddare,  pedder^  a  man who  hawked  about  fish  in  ba&keta  called peds,  or  occasionallT  pads.  See  Pedde  in Prompt.  Parv. ;  Norfolk  ped  (Korby); Low).  Sc  peddir,  a  pedlar  Cj^t^ieson). The  orig.  sense  was  prob  'bag,'  and  (he word  is  to  be  identified  wilh/a</  and/W; AeeFad(i).
13936:Phthisis,  consumption  of  the  lungs. (L.-Glt.)  L. /^/Aijj/.-Gk.  (pelaa,  con- sumption, decay. —  Gk.  iftfiVn*-,  to  decay, wane.  Cf.  Ski.  kj/ti,  to  destroy,  ksMitu, decay.  Dor.  phthisic,  pro[jerIy  an  adj., from  L*. /^Mu/Vnx,  adj.,  consumptive:  but used  as  a  sb.  (,'L.  phthisica\  with  the same  sen:ie  as  phthisis  \  often  called  and spelt  tisic.
14194:plea,  an  excuse.  (F.-L.)  M.  E.  pire, p/ay.  —  O.  F.  p/f,  p/ai,  occasional  forms  of O.  F. plait ^plaui^  a  pica.  —  Low  V^plotitum, a  decree,  sentence,  &c.  (with  nuuicrous meaoingsi).  urig.  a  ducision,  that  which  has st-emed  good.  —  L.  pioiitum,  nent.  of pianiuif  pp.  olplfhere,  to  please.
15682:Reach  (i),  to  attain.  (£.) pt.  t-  rai^hte,  raujf^fe,  pp    n.- TiXi  att,  rAcean,    pt.  t.  rikft.  -^  ' '   rn rika,    G.   rtithen.      The   A  S.   r-fv  aiv raikian)  seems  to  mean  'to  !■■•'  '"f-  '•■ power,*  and  is  allied  to  the  >  i answering  to  Goth,  reiki,  |(ri» Still  more  cloMrly  allied  to  tbe occasion,  due  time;   Ihls  wonU orig.  sense  '  lo  seize  an  opport comes  to  much  the  same  thing.     Thcl base  is  RAK  «  Aryan  lO\G.  to  rule; Regent.   Der.  reaek,  sb.,  which  also  nU '  a  stretch  in  a  river."
16196:romaunt.  (F.-L.)  O.  F.  romant,  an occasional  form  of  O.  F.  reman,  also  spelt romans,  a  romance ;  see  above.  Dar. romanf-ie.
16215:—  Icel.  rotinn.  Swed.  rutten,  Dan.  madtrt, rotten.  The  Icel.  ratinn  ts  the  pp.  of  a lost  verb  (.base  RUT),  lo  decay.
```


## [2026-09-06T15:33:06.262Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"accident,  n\\|incident,  adj\\|decay,  intr\\|decay,  n\" KLN_1966.txt | head\necho \"--- accident ---\"\ngrep -n \"accidens\" KLN_1966.txt | head -3\necho \"--- incident ---\"\ngrep -n \"incidens\" KLN_1966.txt | head -3\necho \"--- decay ---\"\ngrep -n \"OF.  decair\\|decair\\|decaier\" KLN_1966.txt | head -5"
}
```


### [2026-09-06T15:33:06.365Z] TOOL RESULT

```
1339:accident,  n.  —  F.,  fr.  L.  accidentem,  acc.  of  acci¬ dens,  ‘accident’,  prop.  pres.  part,  of  accidere,  ‘to fall  upon  something,  happen’,  fr.  ad-  and cadere,  ‘to  fall’.  See  cadence.  For  the  change  of Latin  d  (in  cadere)  to  i  (in  ac-cidere)  see  abigeat and  cp.  words  there  referred  to.  As  a  term  of philosophy  L.  accidens,  ‘accident’,  is  a  loan translation  of  Gk.
8167:coincide,  intr.  v.,  1)  to  agree  exactly;  2)  to  occupy the  same  place;  3)  to  occur  at  the  same  time.  — ML.  coincidere,  lit.  ‘to  fall  upon  together’,  fr. co-  and  L.  incidere,  ‘to  fall  upon,  light  upon’, fr.  in-,  ‘in’,  and  cadere,  ‘to  fall’.  See  incident, coincidence,  n.  —  F.  coincidence,  fr.  MF.  coln- cidance,  fr.  coincidant,  pres,  part  of  coincider, fr.  ML.  coincidere.  See  prec.  word  and  -ence. coincident,  adj.  —  F.  coincident.  See  prec.  word and  -ent.
10480:Derivative:  decat iz-er,  n. decay,  intr.  v.  —  ONF.  decair ,  corresponding  to OF.  dechair,  decheeir  (F.  dechoir),  ‘to  fall  off, decay’,  fr.  VL.  *decadere,  refashioned  (after  VL. *cadere)  fr.  L.  decidere,  ‘to  fall  off,  fall  down’. See  de-  and  cadence  and  cp.  deciduous,  escheat. Derivatives:  decay ,  n.,  decay-ed,  adj. decease,  n.  —  ME.  deces,  fr.  OF.  deces  (F.  deeds), ‘decease,  death’,  fr.  L.  decessus,  ‘departure, death’,  fr.  decess-(um),  pp.  stem  of  decedere,  ‘to go  away,  depart’.  See  de-  and  cease  and  cp. predecessor.
19041:incidence,  n.  —  F.,  formed  fr.  incident,  adj.  See next  word  and  suff.  -ce.
19042:incident,  adj.  —  F.  incident,  fr.  L.  incidentem,  acc. of  incident,  pres.  part,  of  incidere,  ‘to  fall upon ;  to  happen,  occur’,  fr.  in-,  ‘in’,  and  cadere, ‘to  fall’.  See  cadence  and  suff.  -ent.  For  the change  of  Latin  d  (in  cadere )  to  X  (in  in-cidere) see  abigeat  and  cp.  words  there  referred  to. Derivatives:  incident,  n.  (q.v.),  incident-al,  adj. and  n.,  incident-al-ly,  adv.,  incident-al-ness,  n. incident,  n.  —  F.  See  incident,  adj. incinerate,  tr.  v.,  to  reduce  to  ashes.  —  L.  in¬ cinerate,  pp.  of  incinerdre,  ‘to  reduce  to  ashes’, fr.  in-,  ‘in’,  and  cinis,  gen.  cineris,  ‘ashes’.  See cinerary  and  verbal  suff  -ate.
--- accident ---
1338:accidence,  n.,  that  part  of  grammar  which  deals with  inflection.  —  From  misspelling  of  orig. accidents,  fr.  L.  accidentia,  neut.  pi.  of  accidens (pres.  part,  of  accidere),  treated  as  a  sing.  fern, noun.  See  accident.
1339:accident,  n.  —  F.,  fr.  L.  accidentem,  acc.  of  acci¬ dens,  ‘accident’,  prop.  pres.  part,  of  accidere,  ‘to fall  upon  something,  happen’,  fr.  ad-  and cadere,  ‘to  fall’.  See  cadence.  For  the  change  of Latin  d  (in  cadere)  to  i  (in  ac-cidere)  see  abigeat and  cp.  words  there  referred  to.  As  a  term  of philosophy  L.  accidens,  ‘accident’,  is  a  loan translation  of  Gk.
1340:accidental,  adj.  —  F.  accidental  (now  accidentel), fr.  ML.  accidentals,  fr.  L.  accidens,  gen.  -entis. See  prec.  word  and  adj.  suff.  -al.
--- incident ---
--- decay ---
10480:Derivative:  decat iz-er,  n. decay,  intr.  v.  —  ONF.  decair ,  corresponding  to OF.  dechair,  decheeir  (F.  dechoir),  ‘to  fall  off, decay’,  fr.  VL.  *decadere,  refashioned  (after  VL. *cadere)  fr.  L.  decidere,  ‘to  fall  off,  fall  down’. See  de-  and  cadence  and  cp.  deciduous,  escheat. Derivatives:  decay ,  n.,  decay-ed,  adj. decease,  n.  —  ME.  deces,  fr.  OF.  deces  (F.  deeds), ‘decease,  death’,  fr.  L.  decessus,  ‘departure, death’,  fr.  decess-(um),  pp.  stem  of  decedere,  ‘to go  away,  depart’.  See  de-  and  cease  and  cp. predecessor.
```


## [2026-09-06T15:33:20.386Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON شانس ===\"\ngrep -n \"شانس\" MON_part2.txt MON_part1.txt | head -10\necho \"=== MON اکازیون ===\"\ngrep -rn \"اکازیون\\|اکازیون\" MON_part1.txt MON_part2.txt incoming/MON/*.txt | head -10"
}
```


### [2026-09-06T15:33:20.477Z] TOOL RESULT

```
=== MON شانس ===
MON_part1.txt:83210:شانس: همق (.) بخت» طالع» اقبال. ضح.- 
MON_part1.txt:83214:شانسی: 12-1 [فر. ف.] (ص‌نسب. ق.) از 
=== MON اکازیون ===
```


## [2026-09-06T15:33:21.616Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== LEW cado ===\"\ngrep -n \"cado, -ere\\|cadō\\|cado,\" LEW_1910.txt | head -10\necho \"=== LAT cado ===\"\ngrep -n \"cado\\b\" LAT.txt | head -10"
}
```


### [2026-09-06T15:33:21.689Z] TOOL RESULT

```
=== LEW cado ===
=== LAT cado ===
1096:accido: v. cado.
8156:Deriv 4 s: cacuminO, -as : rendre pointu (peut-etre crdation d'Ovide),cado
8174:Rattach^ justeaent par les asciens k cado, cf. 7 U 7 CTU) et Tradux. Maia la
8176:cado, cadis, cecidi, casim, cadere (les 1. roaanes attestent aussi
8225:Autres composes: concido (concado)-, tomber tout d’un coup (noter la
8228:les confusione qui se sont produites entre les composes de cado, caedo,
8266:grecques. Il est tentant d'etablir un rapport entre cado et caedo,J-47
10250:penser egalement a rapprocher cado,caedo, comme lassus de laedo.
10366:catax ( cadax Gloss. d'aprbs cado): claudus P.F.39,10; - ... quem
10823:qu’on serait en face d*un ancien present ath 4 matique; alors cado repre-
```


## [2026-09-06T15:33:23.671Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '8176,8235p' LAT.txt"
}
```


### [2026-09-06T15:33:23.720Z] TOOL RESULT

```
cado, cadis, cecidi, casim, cadere (les 1. roaanes attestent aussi
*cadere de *cadeo , peut-etre sous 1'inflnence de iaced,-ere): tomber
(= gr. 7 U 7 Cxu) qu'il a servi 4 traduire), sena physique et moral; d*o 4
"etre abattu, succonber", cf. Cic., Ph.3,14,35, ut cum dignitate potius
cadamus quam cum ignominia seruiamus; d 4 faillir. Oppos^ k sto, surgS,
orior. A tona les sens de fr. "tonber": "le vent tonbe, la pifece toabe".
S'eaploie arec un conpleaent au datif, ou avec in et 1 1 acc. "tomber
sur" (d'ou "s'appliquer 4 " Cic., Tu.5,40, Laconis illud dictum in hos
cadere), ou "arriver 4 , 4 choir avec sub: c. sub sensum. - Absolu-
ment "tonber", c.- 4 -d. arriver inopinenent, cf. T^r., Ad.740, si illud
quod maxime opus est iactu non cadit, | illud quod cecidit forte id
arte ut corrigas-, et aussi "aboutir, se terminer", sens sans doute
calque sur le gr. 7 U. 7 CXU), coaae casus traduit tctuxtoG, cf. Cic., Or.57,194,
uerba melius in syllabas longiores cadunt; et similiter cadentia tra-
duisant op.01,0 7 CTomx. - Usit 4 de tout tenps. Panroaan, M.l.1451, et
1452 cadivus, 1454 caducus.
Derivas et composta: caducus: qui tonbe, et "enclin 4 tomber, caduc,
4 pileptique". En droit "toabe en d^sherence", d'ou caducarius "relatif
aux biens caducs, ou 4 1 1 epilepsie "; caducia (Gl.), caduciter (Varr.).
Ancien, usuel. Pour la fornation cf.mando, manducus et fiducia,
cadiuus (£poq.imp. ): qui toabe de soi-aeme; ^pileptique. Le simple
est peu uaite, maia recidiuus est un peu plus frequent; v. plus loin.
Sur la fornation, v. entre autres Meillet, St. sur l' 4 tyn. et le vocab.
du v.sl., p.365. casus ( cassus Quint.1,7,30) -us (n.): "chute, fait de
tomber (et, par euphemisae, de aourir)", et sens concret "ce qui tombe,
accident, chance, occasion" (souvent avec un sens defavorable). En
grammaire traduit tctuxtcc; "cas", cf. P.F., 51,5, casus dicimus non modo
ea quae fortuita hominibus accidunt, sed etiam uocabulorum formas,
quia in aliam atque aliam cadunt effigiem. Irl.cas. De 14 , casualis =
7 tTurri.)c 6 c, "oasuel, fortuit" et "relatif aux cas". Il n'y a pas de
substantif *cdsio, aais occasio est frequent. Tardifs: cadax (cf.
catax), cadescd. Pour -cidium, -ciduus, v. plus bas.
accido, -is: proprement "tomber ver»", et "arriver par hasard"; se
dit souvent, mais non n£cessaireaent, d'un £vfeneaent facheux. Ce sens
s'est developpe du fait d'une chose qui arrive inopinfenent est rarement- 146 -
agreable, e.g. Pl., Mo. 197, insperata accidunt magis saepe quam quae
speres. Les grammairiens codifient la difference, e.g. Caper, CLK VII
98,8, accidere aliquid aduersi dicito, contingere aliquid pulchri ;
Agroec., ibid.118,23, contingunt bona, accidunt mala, eueniunt utraque.
Mais accido peut se dire d 1 evbnements heureux (Ter.An.398) ou indiff6-
rents (ad Herenn.3,15). Dans la langue philosophique, accidere tradnit
CT\j|j,7ti,7rcei,v > crup.pai,vei,v, et signifie "3'ajouter a", e.g. Cic., N.D.a,8a,
omnium... naturam esse corpora et inane, quaeque his accidant. D'ou
accidens = <rup.|3ef3T]x6<; oppose a substantia = ouaia (cf. Qaint.3,6,36)
ou a proprium , e.g. Charis. GLK I 373,30, antonomasia est dictio per
accidens proprium significans. Par extension il arrive a traduire
stuBetov (Quint. 8,3,70) ou crup,7Ttsot))J.a Cael. Aur ., Acut .a, 6,30. De IA, en
bas latin, accidentia, accidentalis. Les 1 . ronanes attestent aussi
*accadere, M.L.61. Celt.: iri. aicid, accidit-, gall .achwyddo.
Autres composes: concido (concado)-, tomber tout d’un coup (noter la
valeur perfective [determin^e] donn6e par le pr^fixe); decido, ex-
(*de~, excadere M.L.a494 (britt. digwyddo ), 3944 excidium 3968?; sur
les confusione qui se sont produites entre les composes de cado, caedo,
scindo, v. caedo, et scindo), in-, inter-cido "tomber entre" et "p6rir,
disparaitre" (cf. intereo ; v. inter); occido,-is,-eidi, occasum: tomber,
succomber (cf. occumbere, etc., et occidere "tuer", sans rapport ety¬
mologique mais que la langue a rapproche ) qui s 1 est employe pour
designer le coucher des astres et specialement du soleil, d^u occidens
a.(scii, sol occidens) "occident" (oppos^ A oriens ), occasus,-us m.
(opp. A ortus), et A 1 'epoque ancienne occasus, -a, -um: tomb6, conche;
```


## [2026-09-06T15:33:32.426Z] TOOL CALL #40: Bash

```json
{
 "command": "sed -n '1,60p' tools/fetch_source.py"
}
```


### [2026-09-06T15:33:32.463Z] TOOL RESULT

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


## [2026-09-06T15:33:41.123Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \"https://en.wiktionary.org/wiki/hate\" \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/hatiz\" \"https://en.wiktionary.org/wiki/%DA%A9%D9%81\" \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/k%C3%A1p%C3%A1\" ; do python3 tools/fetch_source.py \"$u\" --note \"page 232, roots Kad 1 / Kafa\" ; done 2>&1 | tail -10"
}
```


### [2026-09-06T15:33:44.680Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/3f689f3ac02bea89.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a94874e09502f863.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/286291aceca902df.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b4eefeee3fed2276.txt
```


## [2026-09-06T15:33:47.311Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"===== hate =====\"; grep -n -A4 \"Proto-Germanic\\|Proto-Indo-European\" 3f689f3ac02bea89.txt | head -40"
}
```


### [2026-09-06T15:33:47.364Z] TOOL RESULT

```
===== hate =====
417: From Middle English haate , hat , hate ( noun ) , probably from Old English hatian ( “ to hate ” , verb ) and/or Old Norse hatr ( “ hate ” , noun ) . [ 1 ] [ 2 ] [ 3 ] [ 4 ] Merged with Middle English het , hete ( “ hate ” ) , from Old English hete , from Proto-West Germanic *hati , from Proto-Germanic *hataz ( “ hate ” ) , from Proto-Indo-European *ḱeh₂d- ( “ angriness, hatred ” ) . 
418-
419- Cognates
420-
421- Cognate with Dutch haat ( “ hatred ” ) , German Hass , Haß ( “ hate, hatred ” ) , Luxembourgish Haass ( “ hate, hatred ” ) , Vilamovian hās ( “ hate, hatred ” ) , Yiddish האַס ( has , “ hatred ” ) , Danish had ( “ hate, hatred ” ) , Faroese and Icelandic hatur ( “ hatred, spite, aversion ” ) , Norwegian Bokmål , Norwegian Nynorsk , and Swedish hat ( “ hate, hatred ” ) , Gothic 𐌷𐌰𐍄𐌹𐍃 ( hatis , “ hate, wrath ” ) ; also Breton and Cornish kas ( “ hatred ” ) , Old Irish miscuis ( “ hatred ” ) , Welsh cas ( “ hatred ” ) , Oscan 𐌊𐌀𐌃𐌄𐌝𐌔 ( kadeís , “ enmity ” ) , Ancient Greek κῆδος ( kêdos , “ care for others; troubles; mourning ” ) , Sanskrit रि॒शाद॑स् ( riśā́das , “ benign or devouring or destroying enemies ” ) .
--
423: The verb is from Middle English haate , hate , haten , hatenn , hatien , hatiȝen , hatye , hatyn , heatien , from Old English hatian ( “ to hate, treat as an enemy ” ) , from Proto-West Germanic *hatēn , from Proto-Germanic *hatāną ( “ to hate ” ) , from Proto-Germanic *hataz , from the same root as above.
424-
425- Cognates
426-
427- Cognate with Saterland Frisian hoatje ( “ to hate ” ) , West Frisian haatsje ( “ to hate ” ) , Cimbrian haazan ( “ to hate ” ) , Dutch haten ( “ to hate ” ) , German hassen ( “ to hate ” ) , Luxembourgish haassen ( “ to hate ” ) , Yiddish האַסן ( hasn , “ to hate ” ) , Danish hade ( “ to hate ” ) , Icelandic , Faroese , and Swedish hata ( “ to hate ” ) , Norwegian Bokmål hate ( “ to hate ” ) , Norwegian Nynorsk hata , hate ( “ to hate ” ) , Gothic 𐌷𐌰𐍄𐌰𐌽 ( hatan , “ to hate ” ) .
--
1213: Categories : English terms derived from Proto-Indo-European 
1214: English terms derived from the Proto-Indo-European root *keh₂d- 
1215- English terms inherited from Middle English 
1216- English terms derived from Middle English 
1217- English terms derived from Old English 
1218- English terms derived from Old Norse 
--
1220: English terms derived from Proto-Germanic 
1221- English terms inherited from Old English 
1222- English terms inherited from Proto-West Germanic 
1223: English terms inherited from Proto-Germanic 
1224- English 1-syllable words 
1225- English terms with IPA pronunciation 
1226- English terms with audio pronunciation 
1227- Rhymes:English/eɪt 
--
1276: Middle English terms derived from Proto-Germanic 
1277: Middle English terms inherited from Proto-Germanic 
1278: Middle English terms derived from Proto-Indo-European 
1279- Middle English terms inherited from Old English 
1280- Middle English terms derived from Old English 
1281- Middle English terms with IPA pronunciation 
1282- Middle English lemmas
```


## [2026-09-06T15:33:58.440Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"===== hatiz/hataz =====\"; grep -n -i \"hataz\\|hatiz\\|ḱeh₂d\\|keh₂d\" a94874e09502f863.txt | head -20\necho; echo \"===== کف =====\"; grep -n -i \"Persian\\|Middle Persian\\|kafa\\|foam\\|Proto-Iranian\" 286291aceca902df.txt | head -40\necho; echo \"===== PIr kápá =====\"; head -30 b4eefeee3fed2276.txt"
}
```


### [2026-09-06T15:33:58.501Z] TOOL RESULT

```
===== hatiz/hataz =====
1:URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/hatiz

===== کف =====
68: Persian 
70: Toggle Persian subsection 
237: Persian
243: ( Classical Persian ) IPA ( key ) : /ˈkaf/ 
279: From Middle Persian [Book Pahlavi needed] ( kp /⁠kaf⁠/ , “ foam, slime ” ) ; compare Proto-Indo-Iranian *kapʰas ( “ phlegm, mucus ” ) . Cognate with Khotanese khavä ( “ foam ” ) , etc.
286: foam 
287: c. 1260s , Jalāl ad-Dīn Mohammad Rūmī , translated by Reynold A. Nicholson , مثنوی معنوی [ Masnavi-ye-Ma'navi ], volume I, verse 2676: حلم ایشان کف بحر حلم ماست / کف رود آید ولی دریا به جاست hilm-êšân kaf -i-bahr-i-hilm-i-mâ / kaf rawad âyad wali dariyâ ba jâ-st Their clemency is (but) the foam of the sea of My clemency: the foam comes and goes, but the sea is (always) there. 
294: کف کردن ( kaf kardan , “ to foam ” ) 
343: Persian terms with IPA pronunciation 
344: Rhymes:Persian/af 
345: Rhymes:Persian/af/1 syllable 
346: Persian terms inherited from Middle Persian 
347: Persian terms derived from Middle Persian 
348: Persian lemmas 
349: Persian nouns 
350: Persian terms with quotations 
351: Persian terms derived from Arabic 
356: Requests for Book Pahlavi script for Middle Persian terms 
358: Persian undefined derivations 

===== PIr kápá =====
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/k%C3%A1p%C3%A1
FETCHED: 2026-09-06T15:33:44Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found
```


## [2026-09-06T15:34:06.992Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \"https://en.wiktionary.org/wiki/%DA%A9%D9%81%DA%86%D9%87\" \"https://en.wiktionary.org/wiki/%D8%B4%D8%A7%D9%86%D8%B3\" \"https://www.etymonline.com/word/chance\" \"https://www.etymonline.com/word/cascade\" \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%E1%B8%B1eh%E2%82%82d-\"; do python3 tools/fetch_source.py \"$u\" --note \"page 232 (Kad 2, Kafa, Kad 1) verification\"; done 2>&1 | tail"
}
```


### [2026-09-06T15:34:11.385Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/414b4b16f8cd63a9.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4fd0d599a0f6db55.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/fa5b0c90cf4d0cfe.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0d94ae53440b8206.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/7090029a5157e249.txt
```


## [2026-09-06T15:34:14.615Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nfor f in 414b4b16f8cd63a9 4fd0d599a0f6db55 fa5b0c90cf4d0cfe 0d94ae53440b8206 7090029a5157e249; do echo \"########## $f\"; sed -n '1,5p' $f.txt; grep -n -i \"etymology\\|From \\|Old French\\|Vulgar Latin\\|Proto-\" $f.txt | head -12; echo; done"
}
```


### [2026-09-06T15:34:16.255Z] TOOL RESULT

```
########## 414b4b16f8cd63a9
URL: https://en.wiktionary.org/wiki/%DA%A9%D9%81%DA%86%D9%87
FETCHED: 2026-09-06T15:34:09Z
STATUS: 200
TITLE: کفچه - Wiktionary, the free dictionary

65: Etymology 
140: From Wiktionary, the free dictionary
154: Etymology
157: Inherited from Middle Persian [script needed] ( kpck' /⁠kafčag⁠/ , “ spoon, ladle ” ) .
213: Retrieved from " https://en.wiktionary.org/w/index.php?title=کفچه&oldid=85682783 "
215: Categories : Persian terms inherited from Middle Persian 
216: Persian terms derived from Middle Persian 

########## 4fd0d599a0f6db55
URL: https://en.wiktionary.org/wiki/%D8%B4%D8%A7%D9%86%D8%B3
FETCHED: 2026-09-06T15:34:09Z
STATUS: 200
TITLE: شانس - Wiktionary, the free dictionary

62: Etymology 
139: From Wiktionary, the free dictionary
146: Etymology
149: Etymology tree
151: Proto-Indo-European *ḱad- 
153: Proto-Indo-European *-eti 
155: Proto-Indo-European *ḱádeti 
156: Proto-Italic *kadō 
160: Proto-Indo-European *-(i)yós 
161: Proto-Italic *-ijos 
162: Proto-Italic *-ios 
167: Vulgar Latin *cadentia 

########## fa5b0c90cf4d0cfe
URL: https://www.etymonline.com/word/chance
FETCHED: 2026-09-06T15:34:10Z
STATUS: 200
TITLE: Chance - Etymology, Origin & Meaning

4:TITLE: Chance - Etymology, Origin & Meaning
6:Chance - Etymology, Origin & Meaning 
25: c. 1300, "something that takes place, what happens, an occurrence" (good or bad, but more often bad), especially one that is unexpected, unforeseen, or beyond human control, also "one's luck, lot, or fortune," good or bad; in a positive sense "opportunity, favorable contingency;" also "contingent or unexpected event, something that may or may not come about or be realized." It is from Old French cheance "accident, chance, fortune, luck, situation, the falling of dice" (12c., Modern French chance ), from Vulgar Latin *cadentia "that which falls out," a term used in dice, from neuter plural of Latin cadens , present participle of cadere "to fall" (from PIE root *kad- "to fall").
27: In English frequently in plural, chances . The word's notions of "opportunity" and "randomness" are as old as the record of it in English and now all but crowd out its original notion of "mere occurrence." The meaning "fortuity, absence of any cause why an event should happen or turn out as it does, variability viewed as a real agent" is from c. 1400.
31: Main chance  "probability that offers greatest advantage," hence "thing of most importance" is from 1570s. The mathematical sense of "probability, likelihood of a certain outcome" is from 1778, hence the odds-making sense of "balanced probability of gain or loss."
33: To stand a chance (or not) is from 1796. To take (one's) chances "accept what happens" (early 14c.) is from the old, neutral sense; to take a chance/take chances is originally (by 1814) "participate in a raffle or lottery or game;" the extended sense of "take a risk" is by 1826.
34: also from c. 1300 
38: late 14c., "to come about, to happen," from chance (n.). The meaning "to risk, take the chances of" is attested from 1859. Related: Chanced ; chancing .
39: also from late 14c. 
43: "resulting or due to chance; casual, unexpected," 1670s, from chance (n.).
44: also from 1670s 
50: "to happen, chance," 1520s, from be- + chance (v.). Related: Bechanced ; bechancing .

########## 0d94ae53440b8206
URL: https://www.etymonline.com/word/cascade
FETCHED: 2026-09-06T15:34:10Z
STATUS: 200
TITLE: Cascade - Etymology, Origin & Meaning

4:TITLE: Cascade - Etymology, Origin & Meaning
6:Cascade - Etymology, Origin & Meaning 
58: "a fall or flow of water over a cliff, a waterfall," 1640s, from French cascade (17c.), from Italian cascata "waterfall," from cascare "to fall," from Vulgar Latin *casicare , frequentative of Latin casum , casus , past participle of cadere "to fall" (from PIE root *kad- "to fall").
59: also from 1640s 
63: "to fall in cascades," 1702, from cascade (n.). In early 19c. slang, "to vomit." Related: Cascaded ; cascading .
64: also from 1702 
70: Proto-Indo-European root meaning "to fall."
82: Middle English shour, from Old English scur, scura "a short fall of rain, storm, tempest; fall of missiles or blows; struggle, commotion; breeze," from Proto-Germanic *skuraz (source also of Old Norse skur, Old Saxon and Old Frisian scur "fit of illness;" Old High German scur, Ge
86: , ravinous, of people, "rapacious, violent," of water, "swift-flowing," from raviner "to seize, pillage; to sweep down, cascade...
90: a stream or torrent of water," from French ravin "a gully" (1680s, from Old French raviner "to pillage; to sweep down, cascade...
94: Meaning "cascade, waterfall" is from 1570s (often plural, falls, when the descent is in stages; fall of water is attested...
98: late 14c., arengen, "draw up a line of battle," from Old French arengier "put in a row, put in battle order" (12c., Modern French arranger), from a- "to" (see ad-) + rangier "set in a row" (Modern French ranger), from rang "rank," from Frankish *hring or a similar Germanic source

########## 7090029a5157e249
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%E1%B8%B1eh%E2%82%82d-
FETCHED: 2026-09-06T15:34:11Z
STATUS: 200
TITLE: Reconstruction:Proto-Indo-European/ḱeh₂d- - Wiktionary, the free dictionary

1:URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%E1%B8%B1eh%E2%82%82d-
4:TITLE: Reconstruction:Proto-Indo-European/ḱeh₂d- - Wiktionary, the free dictionary
6:Reconstruction:Proto-Indo-European/ḱeh₂d- - Wiktionary, the free dictionary 
57: Proto-Indo-European 
59: Toggle Proto-Indo-European subsection 
62: Etymology 
75: Reconstruction:Proto-Indo-European/ ḱeh₂d- 
127: From Wiktionary, the free dictionary
129: This Proto-Indo-European entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.
131: Proto-Indo-European
134: Etymology
149: Terms derived from the Proto-Indo-European root *ḱeh₂d- (6 c, 0 e)
```


## [2026-09-06T15:34:21.179Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nsed -n '129,175p' 7090029a5157e249.txt\necho \"############ شانس ############\"\nsed -n '146,190p' 4fd0d599a0f6db55.txt"
}
```


### [2026-09-06T15:34:21.234Z] TOOL RESULT

```
 This Proto-Indo-European entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.

 Proto-Indo-European
 [ edit ] 

 Etymology
 [ edit ] 

 Speculative links have been made to *ḱh₂d- ( “ to fall ” ) . [ 1 ] 

 Root
 [ edit ] 

 *ḱeh₂d- 

 hatred , angriness 

 Derived terms
 [ edit ] 

 Terms derived from the Proto-Indo-European root *ḱeh₂d- (6 c, 0 e) 

 *ḱéh₂d-o-s [ 2 ] [ 3 ] 
 Proto-Celtic: *kādos ( see there for further descendants )

 Proto-Italic: *kādos 
 Oscan: cadeis ( “ enmity ” ) 

 *ḱéh₂d-os ~ *ḱéh₂d-es-os ( s-stem noun ) 
 Proto-Hellenic: *kā́dos 
 Ancient Greek: κῆδος ( kêdos ) 
 Doric Greek: κᾶδος ( kâdos ) 

 *ḱéh₂d-tis ~ *ḱh₂d-téy-s [ 1 ] 
 Proto-Celtic: *kassis ( see there for further descendants )

 *ḱh₂d-os ~ *ḱh₂d-es-os ( zero-grade s-stem noun ) 
 Proto-Germanic: *hataz ( see there for further descendants )

 Unsorted formations 

 Proto-Indo-Iranian: 
 Proto-Iranian: 
 Avestan: 𐬯𐬁𐬛𐬭𐬀 ( sādra , “ misery, suffering ” ) [ 1 ] 

 Proto-Indo-Aryan: 
 > ? Sanskrit: रि॒शाद॑स् ( riśā́das , “ destroying enemies ” ) [ 4 ] 
############ شانس ############
 Etymology
 [ edit ] 

 Etymology tree

 Proto-Indo-European *ḱad- 

 Proto-Indo-European *-eti 

 Proto-Indo-European *ḱádeti 
 Proto-Italic *kadō 
 Latin cadō 
 Latin cadēns 

 Proto-Indo-European *-(i)yós 
 Proto-Italic *-ijos 
 Proto-Italic *-ios 
 Old Latin -ios 
 Latin -ius 
 Latin -ia 

 Vulgar Latin *cadentia 
 Old French cheance 
 French chance bor. 
 Persian شانس 

 Borrowed from French chance .

 Pronunciation
 [ edit ] 

 ( Iran, formal ) IPA ( key ) : [ʃɒːns] 

 Readings

 Iranian reading ? 

 šâns

 Audio ( Iran ) : ( file ) 

 Noun
 [ edit ] 

 شانس • ( šâns )
```


## [2026-09-06T15:34:30.650Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/%D8%B3%D8%A7%D8%B1\" --note \"page 232, Kad 1 node 2, Persian sār\" \npython3 tools/fetch_source.py \"https://abadis.ir/fatofa/%D8%A7%DA%A9%D8%A7%D8%B2%DB%8C%D9%88%D9%86/\" --note \"page 232, Kad 2 node 3, Persian okâziyon\""
}
```


## [2026-09-06T15:34:33.291Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN sadra/sar ===\"\ngrep -n \"sädra\\|sadra\\|sâr \\|Leid\" HRN.txt | head -20\necho \"=== HUB sadra ===\"\ngrep -n \"sadra\\|sädra\" HUB.txt | head\necho \"=== ARY latin index kaf / sar ===\"\ngrep -n -i \"^KAF\\|KAF \\|SADRA\" incoming/ARY/ARY_latin_index_pages.txt | head -20"
}
```


### [2026-09-06T15:34:34.364Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/2dfecd686b4b3789.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ef49c7ba62c8add6.txt
```


### [2026-09-06T15:34:34.426Z] TOOL RESULT

```
=== HRN sadra/sar ===
230:Lehnworte aus dem Persischen. Leider fehlt es für die-
2004:liche Fälle öfter zu Rate gezogen habe. Leider führt es meist die
6069:689. {i)8är ^Schmerz, Leid*.
6070:aw. sddra- 'Wehe, Leid*.
7013:Per. 54 (wo /sadra- statt /ßad^rya- falsch ist).
7937:916. fße^endj guzend (AM. S. 38 Zeile 7) 'Schade Leid',
8666:aw. vergl. amayavä' 'Leid'; phlv. wöyaÄ:; ai. vergl.
10248:49. bes *Leid, Unheil* (Men.), hesitan, hns{i)sn, beSttar (aw.
10983:178. sej 'Schmerz, Leid', sejömand (Bund., AV.), asefömand,
11014:np. dpezgi (so FJ, sonst meist sipergt) 'Leid' er-
15311:sädra- 689.
=== HUB sadra ===
7061:'Schmerz, Leid' aus *sahr = zd. sadra- Xeid, Elend'. Vgl.
7297:geist' {sah = zd. xsadra- und solera-), alter arm. asxarh
=== ARY latin index kaf / sar ===
```


## [2026-09-06T15:34:41.526Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN 689 ctx ===\"\nsed -n '6060,6080p' HRN.txt\necho \"=== leaf of line 6069 ===\"\npython3 - <<'EOF'\nimport bisect\nlines=open('HRN.txt',encoding='utf-8',errors='replace').read().split('\\n')\nff=[i for i,l in enumerate(lines) if '\\f' in l]\nfor ln in (6069,):\n    lf=bisect.bisect_left(ff,ln-1)\n    print(ln,'leaf',lf,'printed',lf-21)\nEOF\necho \"=== HUB 7061 ctx ===\"\nsed -n '7052,7070p' HUB.txt\npython3 - <<'EOF'\nimport bisect\nlines=open('HUB.txt',encoding='utf-8',errors='replace').read().split('\\n')\nff=[i for i,l in enumerate(lines) if '\\f' in l]\nfor ln in (7061,6505):\n    lf=bisect.bisect_left(ff,ln-1)\n    print(ln,'leaf',lf,'printed',lf-10)\nEOF"
}
```


### [2026-09-06T15:34:43.113Z] TOOL RESULT

```
=== HRN 689 ctx ===
*) Nach Castle (bei Vullers) ,7V/.
2) Vis und Rämin, S. 49 Vers 15; z^^n^ S^*di, Bostän, S. 127
Vers 878.— 153 —
bei. LW. sazag (237). Np. nüxte, säz sind vielfach
entlehnt, vergl. auch np. sä^t lieitzeug in arm. sa/teal
gesattelt*, ansa/t *ungesattelt' (Noldeke bei Hübsch -
mann, ZDMG. 35, 132 No. 37).
np. sd/ten ist eine Causativbildung zum Stamme sac-
(np. seztden).
689. {i)8är ^Schmerz, Leid*.
aw. sddra- 'Wehe, Leid*.
690. (2)-ÄÄr 'Kopf in nigün]sar^ sebuk]sar etc.
aw. sära-, särah- *Kopf*; phlv. vergl. sar[var 'Helm\
Vergl. No. 726.
691. 8äl 'Jahr*.
aw. sare^a- 'Jahr*; phlv. sal, sälak *alt\ arm. LW.
nava]8ard, graecisirt (nicht lydisch, vergl. G. Meyer,
Indog. Forsch. I, 326) i'for adodiv (Job. Lydus), chald.
LW. "»TlDli (de Lagarde, Öemitica I, 65), ;K''ärezm.
nau^arjT (Nöldeke, Pers. Stud. I, 34); skr. gardd-
'Herbst, Jahr (mit Zahlen)'.
=== leaf of line 6069 ===
6069 leaf 167 printed 146
=== HUB 7061 ctx ===
aus alterem (DQaddvrjg (Memn. Fragm.), Phradates (Curtius),
also phi. *Frahat, alter *Fradat = zd. fraiata-. So ist
auch das in alter Zeit aus dem Griechischen entlehnte
Siddrjfia im Persischen iiber *dddB7n, spater *d&hSin zu np.
dehtm (Vis u Ramin 103, 10) geworden.
Ebenso ist J vor r zu A geworden: 7nuhr *Siegelring,
arm. murhak 'Urkunde' (5. Jhd.), skr. mudra- *Siegelring,
Siegel' u. s. w. ; arm. nirh 'Schlummer, Schlaf * (5. Jhd.) =
skr. nidra-^), Mit Verlust des h nach langem Vokal: np. sar
'Schmerz, Leid' aus *sahr = zd. sadra- Xeid, Elend'. Vgl.
sdhar 'Gatte' durch Anlehnung an pidar u. s. w. aus *s5Ar
= zd. ^xsaodra- entstanden? Siehe oben p. 82.
b) zu y = i: mai 'Wein', paz. mai Min. Gl. 132, Shk.
257, zd. maiit- *Wein (nach Darmesteter); fcai Vann,
wie?' = zd. kada; Dai *der zehnte MonatV zd. dadvd; nai
*Rohr , g. nad 'Rohr = skr. nada-, vgl. nai TlOte' aus
^nada-; pai Tussspur = zd. paia-, ap. nipadiy; x^ai
*Schweiss* = zd. x^'a^da- (also x'ai aus x'aiy); pai {pa) 'Fuss*
= zd. pada- ; -ra Casuspartikel = paz. ra, phi. rai wegen',
7061 leaf 201 printed 191
6505 leaf 186 printed 176
```


## [2026-09-06T15:34:56.717Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"=== سار wiktionary ===\"; grep -n -i \"Persian\\|Etymology\\|grief\\|starling\" 2dfecd686b4b3789.txt | head -30\necho; echo \"=== abadis اکازیون ===\"; sed -n '1,10p' ef49c7ba62c8add6.txt; grep -n -i \"اکازیون\\|occasion\\|فر\\.\" ef49c7ba62c8add6.txt | head -20"
}
```


### [2026-09-06T15:34:56.784Z] TOOL RESULT

```
=== سار wiktionary ===
62: Etymology 1 
71: Etymology 2 
83: Etymology 3 
95: Etymology 4 
126: Etymology 
135: Persian 
137: Toggle Persian subsection 
220: Etymology 1
728: Etymology 2
1234: Etymology 3
1482: Etymology 4
1767: Etymology
1770: Borrowed from Persian سار ( sâr , “ starling ” ) .
1777: starling ( Sturnus vulgaris )
1789: Persian
1795: ( Classical Persian ) IPA ( key ) : /ˈsaːr/ 
1833: starling 
1866: Ottoman Turkish terms borrowed from Persian 
1867: Ottoman Turkish terms derived from Persian 
1871: Persian terms with IPA pronunciation 
1872: Rhymes:Persian/aːr 
1873: Rhymes:Persian/aːr/1 syllable 
1874: Persian lemmas 
1875: Persian nouns 

=== abadis اکازیون ===
URL: https://abadis.ir/fatofa/%D8%A7%DA%A9%D8%A7%D8%B2%DB%8C%D9%88%D9%86/
FETCHED: 2026-09-06T15:34:34Z
STATUS: 200
TITLE: اکازیون - معنی در دیکشنری آبادیس

اکازیون - معنی در دیکشنری آبادیس 

 دیکشنری مترجم بپرس 

 اکازیون
4:TITLE: اکازیون - معنی در دیکشنری آبادیس
6:اکازیون - معنی در دیکشنری آبادیس 
10: اکازیون
25: ملک اکازیون : [ اصطلاح املاک] یکی از اصطلاحات رایج در املاک که برای تمام املاک از جمله آپارتمان و ویلا در شمال به کار می رود، "اکازیون" است. اگر بخواهیم این اصطلاح را در یک عبارت کوتاه توضیح دهیم به این صورت است؛ "اکازیون به ملکی گفته می شود که بهترین امکانات را دارد اما با قیمت مناسب و حتی ارزان قرار است فروخته شود. " 
27:مناسب بودن قیمت املاک با امکانات بیشتر موجب اکازیون بودن آن می شود. در همین راستا اگر یک ملک یا یک ویلا در منطقه ای بسیار عالی با موقعیت مناسب و دسترسی عالی به تمام امکانات زندگی قرار داشته باشد و قیمت آن هم مناسب باشد، باز هم به آن، ملک اکازیون گفته می شود. 
28:از یک دیدگاه دیگر، اکازیون به این صورت تعریف می شود: "اگر یک ملک از معماری بسیار فوق العاده برخوردار باشد، یا طراحی دکوراسیون داخلی آن به سبک ویژه و مدرن و لاکچری طراحی شده باشد و نسبت به این همه ویژگی، قیمت خوبی برای آن ارائه شود، به این املاک هم ملک اکازیون گفته می شود. "
29:در برخی موارد، فروشنده، قیمت مناسبی را به همراه شرایط ساده برای پرداخت هزینه خرید املاک ارائه می دهد؛ این در حالی است که یک ملک یا ویلا جزء بهترین ساختمان دسته بندی شده است. همین شرایط ساده برای تسویه حساب و انجام معامله موجب می شود مشاور املاک بگوید "این ملک اکازیون است. "
34: تلفظ به زبان انگلیسی "اوکیشن" و به زبان فرانسه "اکازیون" است.
```


## [2026-09-06T15:35:03.877Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nsed -n '1789,1870p' 2dfecd686b4b3789.txt | grep -n \"Etymology\\|From\\|Inherited\\|Noun\\|sâr\\|grief\\|head\\|suffix\" | head -30\necho \"----\"\nawk 'NR>=1789 && NR<=1870' 2dfecd686b4b3789.txt | head -60"
}
```


### [2026-09-06T15:35:05.653Z] TOOL RESULT

```
34: sâr
40: Noun
43: سار • ( sâr ) 
----
 Persian
 [ edit ] 

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /ˈsaːr/ 

 ( Dari, formal ) IPA ( key ) : [sɑːɾ] 

 ( Dari, formal ) IPA ( key ) : [sɑːɾ] 
 ( Kabuli ) IPA ( key ) : [sɑːɾ] 

 ( Hazaragi ) IPA ( key ) : [sɔːɾ] 

 ( Iran, formal ) IPA ( key ) : [sɒːɹ] 

 ( Tajik, formal ) IPA ( key ) : [sɔɾ] 

 Rhymes: -aːr 

 Readings

 Classical reading ? 

 sār

 Dari reading ? 

 sār

 Iranian reading ? 

 sâr

 Tajik reading ? 

 sor

 Noun
 [ edit ] 

 سار • ( sâr ) 

 starling 

 Retrieved from " https://en.wiktionary.org/w/index.php?title=سار&oldid=91031897 "

 Categories : Arabic terms belonging to the root س ي ر 
 Arabic lemmas 
 Arabic verbs 
 Arabic terms with usage examples 
 Arabic form-I verbs 
 Arabic hollow form-I verbs 
 Arabic form-I verbs with ي as second radical 
 Arabic form-I verbs with past vowel a and non-past vowel i 
 Arabic verbs with full passive 
 Arabic terms belonging to the root س ر ر 
 Arabic form-III verbs 
 Arabic geminate form-III verbs
```


## [2026-09-06T15:35:13.214Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \"https://vajehyab.com/?q=%DA%A9%D9%81&d=moein\" \"https://abadis.ir/fatofa/%D8%B3%D8%A7%D8%B1/\"; do python3 tools/fetch_source.py \"$u\" --note \"page 232: Mo'in kaf; Dehkhoda/Mo'in sār\"; done"
}
```


## [2026-09-06T15:35:13.390Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== ARY کف ===\"\ngrep -n \"کف\" incoming/ARY/ARY_pages.txt | head -20"
}
```


### [2026-09-06T15:35:17.713Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/2447a76501e35e49.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/dfed70ea163ea6e4.txt
```


### [2026-09-06T15:35:17.758Z] TOOL RESULT

```
=== ARY کف ===
2765:سانسکریت (54۸/58777): 108۸13 ,کف10 آلمانی کهن ((02791۸ 1/0 صا0):
2810:۳ چم اکثر واژه‌های غیرایرانی اين فهرست: پوشا کد» پوشیدن» کفش. :
4070:پهلوی (1/اتقهه): کفتا8 اق۸ ,25
4484:۱ معنی این واژه در اپرلندی کهن: کف دست.
5158:۳۸۸۸ ,۳۸۸7 رکف ۸5 ۳
5602:ند ۷۹:۲ 3 ,کف8 117۳71
5914:این واژه و واژه‌ی تکفا هم ریشه‌اند.
6473:ففقکلفتت ,کفنعکتین سرئدی (3780/57): انا[
6606:۰ تکفا حتاقق زا
6736:5 ,کف۲۸88م) ,کفل2 ۲۸7۷ لد وابد ۱ هگا ادها
6820:باقن ,کفعگین زر ۳
7704:,3۸3 ,02611 2۸68 ,کف0۸01
8658:برنائی ۰:۶۶ ۱۲۵۹ ,کف ات017۲ سرئدی (917501577): 13
8826:چم این واژه در زبان‌های ژرمنی؛ کپل» کفل.
10539:51 ,کفکلق ات5 برهان قاطع + 1۱۳۴
10596:0۸ ,کف ات0 0
11050:۴ در پیشتر زبان‌های هند و اروپایی این واجریشه به چم "استخوان کف" بکار می‌رفنه و شکل و کاربرد این
11183:7 د8ف8۸ ,شقا5 بتاکفتاد 5 ات 8
11769:افغانی (پشتو) (/4۳0/۸۷): 3اه ,5۸3۸8 ,کفش
11798:5 ا 07 کف ,35 1[ 94940 ۶00690
```


## [2026-09-06T15:35:23.706Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"=== vajehyab moein kaf ===\"; grep -n \"کف\" 2447a76501e35e49.txt | head -20\necho; echo \"=== abadis sar ===\"; grep -n \"آزار و محنت\\|محنت\\|اوستا\\|معین\\|سار\" dfed70ea163ea6e4.txt | head -30"
}
```


### [2026-09-06T15:35:23.765Z] TOOL RESULT

```
=== vajehyab moein kaf ===
4:TITLE: معنی کف | واژه یاب
9: معنی کف | واژه یاب 
18: کف
35: کف
37: (کَ) [ ع . ] (اِ.) سطح داخلی دست یا پا که تقریباً گود است . ج . کفوف . ؛ ~ دست خود را بو کردن کنایه از: علم غیب دانستن (بیشتر به صورت استفهام انکاری به کار ر
39: کف
43: کف
49: کف رفتن
53: کف سفید
57: کف کردن
59: (کَ کَ دَ) (مص ل .) 1 - تولید کف شدن . 2 - (عا.) عشقی شدن .
61: کف بین
65: کفته
73: کف کردن
75: (کَ کَ دَ) (مص ل .) 1 - تولید کف شدن . 2 - (عا.) عشقی شدن .
77: کفپوش
79: (کَ) (اِ.) پوشش زینتی یا بهداشتی ، معمولاً پیش ساخته برای کف یک محوطه ، بویژه کف بنای سر پوشیده .
81: کفج
83: (کَ) (اِ.) کف صابون ، کف شیر، کف آب دهن .
85: کفک

=== abadis sar ===
4:TITLE: سار - معنی در دیکشنری آبادیس
6:سار - معنی در دیکشنری آبادیس 
10: سار
13: مترادف سار : سارنگ، رنج، محنت، درد، شتر، پرده، ساره، نشاط آور، نشاط انگیز، شادی زا
20: سار. ( اِ ) پرنده ای است سیاه و خوش آواز که خالهای سفید ریزه دارد. و مرغ ملخ خوار نوعی از آن است. ( برهان ) ( انجمن آرا ) ( آنندراج ). جانوری است پرنده و سیاه رنگ که خالهای سفید دارد و خوش آواز بود. ( جهانگیری ). در عربی آن را زرزور و در ترکی صغجق گویند. ( شعوری ). و در شیراز آن را کاوینک گویند. ( رشیدی ). نام مرغی است سخنگوی . ( حاشیه لغت فرس نسخه خطی نخجوانی ). زرزور. ( بحرالجواهر ) ( زمخشری ). سودانیه. ( بحر الجواهر ) ( زمخشری ) ( نخبة الدهر ). ساری. ( انجمن آرا ).سارج. ( شرفنامه منیری ). مرغی است حلال گوشت از جمله طیور وحشی. سارک. سارنج. سارچه. ساسر. سیاسر. سنقورجوق. سوران : 
21:آن زنگی زلفین بدان رنگین رخسار
22:چون سار سیاه است و گل اندر دهن سار.
24:برآمد ز شاخ آن نگونسار سار
26:و سار را که به تازی زرازیر گویند زیان ندارد [ نوعی از زهرها ]. ( ذخیره خوارزمشاهی ).
28:بانگ کشیده چو سار از پی این جابجا. خاقانی.
29:از خسان چو سار شورانگیز
31:گر ملخ را نیست بر پا موزه زرین سار
33:اگر در ریاض نعم ایشان [ آل سامان و آل بویه ] چون عندلیب نوای خوش میزدند و یا چون سار بر گلزارترنمی بنوا میکردند بدیع نبود. ( ترجمه تاریخ یمینی چ 1272 ص 9 ).
34:باز صید آرد بخود از کوهسار
35:لاجرم شاهش خوراند کبک و سار. ( مثنوی ).
36:فغان ز درد دل سار و ناله سحرش 
37:که هست درد دل سار علت ساری. سلمان ساوجی.
38:رجوع به سارج ، سارچه ، سارک ، سارنگ ، سارو، ساروک ، ساری ، شار، شارک و شارو، ونیز رجوع به سودانیه شود. || سار ابلق. مرغ ملخ خوار. سار توتی. || سار سبز. قاریه.( مهذب الاسماء ). قاریه. پرنده ای است کوتاه پای ، بلندمنقار و پشت سبز. ( زمخشری ). سبزقبا. ( شعوری ) ( اشتینگاس ). || لاله سار، نام مرغی است سخنگوی و سیاه. ( فرهنگ اوبهی ) ( برهان ). رجوع به همین کلمه شود. || به معنی شتر هم آمده است چه شتربان را سارابان گویند . ( جهانگیری ) ( برهان ) ( غیاث ) ( شعوری ) ( انجمن آرا ) : بیشتر بخوانید ... 
42: ۱ - رودیست در مناطق مرزی بین فرانسه و آلمان که از کوههای وژ سرچشمه گیرد و وارد رود موزل شود .طول آن ۲۴٠ کیلومتر است .۲ - ناحیه سار ۲۵۶۷ کیلومتر مربع وسعت و ۱٠۸۹٠٠٠ تن جمعیت دارد .در معاهده ۱۹۱۹ م.در ورسای این ناحیه بمدت ۱۵ سال از آلمان منتزع و بفرانسه واگذار گردید . در ۱۹۳۵ پس از مراجعه به آرائ عمومی به آلمان مسترد گردید . در ۱۹۴۶ سپاهیان فرانسه سار را اشتغال کردند و در ۱۹۵۶ مجددا بالمان برگشت . شهر مرکزی آن سار بروک است .
43:۱ - در آخر بعض کلمات مرکب به معنی سر آید : سبکسار آسیمه سار گاوسار ( گزر ) . ۲ - در آخر بعض کلمات مرکب پسوند مکان است و غالبا به جای کثرت و انبوهی است : چشمه سار شاخسار کوهسار ۳ - ( ادات تشبیه ) گونه شبیه : باد سار دشت سار دیو سار . ۴ - در بعض ترکیبات معنی جانب و ناحیه را رساند : رخسار سرین سار .
46: فرهنگ معین
49: (پس . ) ۱ - در آخر بعض کلماتِ مرکب به معنی «سر» آید: سبکسار. ۲ - در آخر بعضی کلمات مرکب پسوند مکان است که بیشتر معنای کثرت و انبوهی را می رساند. چشمه - سار. ۳ - از ادات تشبیه که معنای مانند و شبیه را می رساند: بادسار.
50: [ ساره . ] (اِ. ) پرده .
51: [ اوست . ] ۱ - (اِ. ) رنج ، محنت ، آزار. ۲ - (ص . ) رنجور.
56: ۱. رنج، آزار، محنت، درد، غصه.
58:۱. شبیه، نظیر، مانند، گونه (در ترکیب با کلمۀ دیگر ): بادسار، خاک سار، خجل سار، خوارسار، دشت سار، دیوانه سار، دیوسار، زیرک سار، مارسار: گناه آید از بندۀ خاک سار / به امید عفو خداوندگار (سعدی۱: ۱۹۶ ).
59:۲. جای بسیاری و فراوانی چیزی (در ترکیب با کلمۀ دیگر ): چشمه سار، شاخسار، کوهسار، نمک سار.
60:۳. سر (در ترکیب با کلمۀ دیگر ): آسیمه سار، خیره سار، سبک سار، گاوسار، نگون سار.
61:۴. جا، مکان، محل (در ترکیب با کلمۀ دیگر ): خشک سار، گرم سار.
63:= ساره
```


## [2026-09-06T15:35:36.364Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nsed -n '33,50p' 2447a76501e35e49.txt"
}
```


### [2026-09-06T15:35:36.404Z] TOOL RESULT

```
 جست‌وجوی دقیق

 کف
 فرهنگ انتشارات معین
 (کَ) [ ع . ] (اِ.) سطح داخلی دست یا پا که تقریباً گود است . ج . کفوف . ؛ ~ دست خود را بو کردن کنایه از: علم غیب دانستن (بیشتر به صورت استفهام انکاری به کار ر

 کف
 فرهنگ انتشارات معین
 ( ~ .) [ ع . ] (مص م .) بازداشتن ، منع کردن .

 کف
 فرهنگ انتشارات معین
 ( ~ .) [ په . ] (اِ.) 1 - انبوهی از حباب - های ریز که به هنگام جوشیدن آب در آن به وجود می آید. 2 - حباب های ریز سفید رنگی که در اثر ترکیب مواد شوینده و آب پدید

 جست‌وجوی مشابه

 کف رفتن
 فرهنگ انتشارات معین
```


## [2026-09-06T15:35:37.345Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT kafa ===\"\ngrep -n \"kafa-\\|'Schaum'\\|Schaum\" BRT.txt | head -10"
}
```


### [2026-09-06T15:35:37.393Z] TOOL RESULT

```
=== BRT kafa ===
9046:•  j.  kafa-  m.  'Schaum,  Geifer';  yl  (näml.  1 uilrä)  '/jin  aipi-spaydli  spasiimm  upa  .  .  \ Auxsnaei re  (sd.)  Yt. /J.  13.
9047:ai.  ia/ia-  m.  'Schleim',  np.  ia/  'Schaum'.  — Npü. ;  ita/,  erl.  larJ;
27071:Zum  V.  snaig-;  eig.  'Schnee  fallen  lassend sva.  Schaum,  Geifer  aus  dem  Maul,  Mund flicssen  lassend';?).  —  Pö.:  *siirxre>«/äri).  — 1)  So  wird  wohl  an  beiden  Stellen  zu  lesen sein;  s.  zu  snaeg^
30181:•  j.  *hu-xönaoi)Ta-  n.  'gutes  Knie'": ustrahe  . .  yS  kafim  aipijpayeiü  spaHtittm upa  vaylatum  '^re  (AD.)  Aupaitisläiu'* "des  Kamel(hengst)s,  der  weisslichen Schaum  auf  seinen  Kopf  zurückwirft, auf  seine  guten  Knie  und  Beine"-  Yt 14.  iZ'^.
```


## [2026-09-06T15:35:50.913Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== WLD Bd1 kad fallen ===\"\ngrep -n \"kad-\\|käd-\\|kad- ,fallen\\|cadö\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -20\necho \"=== search 'Kummer, Haß' ===\"\ngrep -n \"Kummer\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -20"
}
```


### [2026-09-06T15:35:50.977Z] TOOL RESULT

```
=== WLD Bd1 kad fallen ===
21376:■» kat- — kad- 
21400:s. dazu das u. kad- „glanzen“ bemerkte). 
21422:1. kad- ,. fallen". 
21447:bad- — kad- 
21453:2. kad- „glanzen, prangen, sich auszeiehnen". 
21471:Anm. 3 *kad-(s)mend- als „die gliinzenden" (Quellgottinnen) gedeutet, ist 
21474:kad- „seelische Yerstimmung: Kummer, HaB". 
21557:ai. khud- unter Annahme einer Gdf. skad-, der aber der vorzuziehende 
21581:,,Hafi" (docli s. auch u. *kad- „seelische Yerstimmung") ; ags. hcedre „sorg- 
27644:at. xkad-a, -i, ecu, eeroi, -ag da., xkadcov, -ovog Hes. ds., xladolco „beschneide 
=== search 'Kummer, Haß' ===
814:aisl. ekki „Schmerz, Kummer", ags. inca „Schmerz, Skrupel, Yerdacht, 
4185:Zusammenschnfiren der Kehle, Unruhe, Angst, Kummer“, angus-tus „eng“ 
8657:norw. mdartl. ank „Gewimmer, Seufzen, Kummer, Reue", diin. ank, anke 
13616:s. Wz. uei- „auf etwas losgehn“); ags. wil ,,Bedriingnis, Kummernis, Not, 
21474:kad- „seelische Yerstimmung: Kummer, HaB". 
23810:Kummer" (arm. tug „Trauer‘ ist iran. Lw. ; idg. kuq- ware arm. *sus-, 
24409:trauen). Mir. cuma , mbret. caff on, „Kummer ££ (s. Fick II 4 69 f. und zum 
29178:Aisl. harmr „Betriibnis, Kummer, Harm, Krankung' 1 , ags. Tnearm „Kummer, 
33804:Kummer; abscheulich"; aksl. groza „Graus, Schauder", skr. grbza, po. 
33976:Wunde“, russ. nazola „Gram, Kummer, Arger“, nazoliib „ Rummer, Arger 
33981:berger-Fick II 4 108 zw. verglichene ir. galar „Krankheit, Kummer", cymr. 
40880:grustiti „ekeln“, russ. grusts „Kummer, Betriibnis", werden auf einer ahn- 
40925:sz-grustiti sa ,,sich gramen", russ. g rusts f. „Kummer, Betriibnis', slov. grust 
43177:baire „Kummer (?) ;( (Stokes Rc. 27, 85; ?), bruth ,,Gewicht, Masse ' (Stokes 
43303:mir. berran ,,Kummer ! ‘. (Zupitza GG. 78; ai. jdratc ,,rauscht, tont. knistert. 
43406:zur Bod. ai. edka- „GIut, Flamme" und „Qual, Kummer, Trauer •). 
44000:Kummer; hierber wohl auch slov. gruze PI. f. „Kratze“ nach v. d. Osten- 
44006:sicher ist); ir. iron ,.Kummer“, cymr. brwyn „stechender Schmerz" (urlielt. 
44018:Fick BB. 6, 213. Zu gryzq wahrscheinlich russ. grusfa „Kummer", sloven. 
45844:pyngS „Unannehmlichkeit, Yerlegenheit", pyngsl „Kummer, Bedrangnis"
```


## [2026-09-06T15:35:54.818Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '21422,21440p' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt\necho \"..... kād- .....\"\nsed -n '21474,21500p' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt"
}
```


### [2026-09-06T15:35:54.876Z] TOOL RESULT

```
1. kad- ,. fallen". 

Ai. cad-, Pf. ear nda, Fut. cakyanti „abfallen, ausfallen" (: lat. cudo, z B. 

Vanicek LEAA 7 b. 2 67; unbegriindete Zweifel bei Hirt BB. 24, 232); 

arm. cacnum „fallen, niedrig werden" (Scheftelowitz BB. 28, 287) ; 

lat. cado, -ere „fallen“ (o. antkadumt s. A'f. LEAA r b. 2 s. v.); 

mir. casar „Hagel; Blitz", cymr. cesair „SchloBen“, corn, keser, bret. 
kazarch „Hagel" (Fick II 4 74; nicht entscheidend dagegen Loth Rc. IS, 
90. Ganz unwahrscheinlich wegen der Bed. ist Zugehorigkeit von ir. 
eass „schnell", Strachan BB. 1 7, 297 ; dt. Hast hat mit cass nichts zu tun, 
s. Falk-Torp s. v. m. Lit.). 

Bei Fick I 4 32, 42, 206, 420 A r erkniipfung mit fernzuhaltendem; iiber 
got. hatis „HaB“ siehe *kdd- „seelische A r erstimmung“, iiber ags. henfan 
Walde, Etymologisches Worterbuch. I. 23 
..... kād- .....
kad- „seelische Yerstimmung: Kummer, HaB". 

Av. sadra- n. „Leid, Wehe, Unheil" (Geldner KZ. 27, 242f.); 
gr. xijdog n.. dor. xddog „Sorge, Trauer, Betriibnis; Leichenbestattung; 
Familiengefuhl, affinitas", xrjdioxog „der liebste" („der am meisten am 
Herzen liegt"), xijdeiog „der Sorge wert, lieb, teuer; zur Bestattung ge- 
horig; sorgsam; verschwagert, blutsverwandt“. xrjdeia „Besorgung, bes. eines 
Toten, Bestattung; Yerwandtschaft, Schwiigerschaft", xrjdeoTt'jg, kret. xa- 
dearag „Heiratsverwandter", xrjdevco „besorge, pflege; bestatte; verschwa- 
gere; bin oder werde verwandt", xr]dsfj,d>v „Besorger, Beschiitzer; Leichen- 
bestatter; Heiratsverwandter", xi)dco „mache besorgt, betriibe“ (vielleicht 
auch in der Bed. „verletze, schadige" dasselbe Wort, doch s. auch *qdd- 
„schadigen“), dxrjdrjg „unbesorgt, vernachlassigt, unbestattet; sorglos, sich 
nicht kiimmernd, vernachlassigt", wovon axrjdeco „vernachlassige, lasse auBer 
acht"; 

osk. cadeis amnad „inimicitiae causa" (: dt. Haft, Kern KZ. 21, 242); 
mir. caiss, cymr. cas, bret. cas „IIaG" (*k;ids-i- als Weiterbildung des 
-es-St. von got. hatis, gr. xfjdog; FickII 4 68, Brugmann II 2 1, 569), wo- 
mit vom ursprgl. Begriffe „Sorge" in freundlichem Sinne aus (vgl. das 
Griech.) gleichsetzbar scheint mir. caiss „Liebe“, mis-cuis „HaB", (siehe 
Pedersen KG. II 10; auch cymr. caddu „sorgen fur“ kann so gedeutet 
werden, doch bleibt dafiir wie fur ir. caiss „Liebe“ auch Yerbindung mit 
ags. hcedre „sorglich“, Wz. kadh- offen, Zupitza Gutt. 206 f. ; cymr. cawdd 
„offensa, ira, indignatio" corn, cueth, mbret. cues, nbret. kcuz „Leid, Trauer" ; 

got. hatis n. „IIaB, Zorn", anord. hatr n., ags. hete m., as. lieti m., ahd.
```


## [2026-09-06T15:36:03.030Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"1\\. kad- \\|kad- „seelische\" incoming/WLD/WLD_Bd1_pages.txt | head\npython3 - <<'EOF'\nimport re\nt=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\npgs=t.split('\\f')\nfor i,p in enumerate(pgs):\n    if '1. kad- ,. fallen' in p or 'kad- „seelische' in p:\n        m=re.search(r'\\[pdf page (\\d+)\\]',p)\n        print(i, m.group(0) if m else None, [l for l in p.split('\\n') if re.fullmatch(r'\\s*3\\d\\d\\s*',l)][:4])\nEOF"
}
```


### [2026-09-06T15:36:04.934Z] TOOL RESULT

```
32162:kad- „seelische Yerstimmung: Kummer, HaB".
32274:,,Hafi" (docliauch u. *kad- „seelische Yerstimmung") ags. hcedre „sorg-
348 None []
350 None []
```


## [2026-09-06T15:36:09.846Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\npgs=t.split('\\f')\nprint(repr(pgs[348][:200]))\nprint('---')\nprint(repr(pgs[350][:200]))\nEOF"
}
```


### [2026-09-06T15:36:12.147Z] TOOL RESULT

```
'                                                                                                     ;\n\n\n\n\n340                                     bad-   — kad-\n„verfolgen,    angreifen,       ergreif'
---
'           -\n\n\n\n\n342                                                     qap-\n\n\n,,Hafi" (docliauch u. *kad- „seelische Yerstimmung") ags. hcedre „sorg-\n                          s.                    '
```


## [2026-09-06T15:36:31.335Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('HRN.txt',encoding='utf-8',errors='replace').read()\npgs=t.split('\\f')\nfor i,p in enumerate(pgs):\n    if '689. {i)8är' in p or '689.' in p and 'sddra' in p:\n        print('0-based leaf',i,'-> printed',i-21)\n        break\nt2=open('BRT.txt',encoding='utf-8',errors='replace').read()\npgs2=t2.split('\\f')\nfor i,p in enumerate(pgs2):\n    if \"kafa-  m.  'Schaum\" in p:\n        print('BRT leaf',i)\n        import re\n        print([x for x in re.findall(r'\\b1\\d{3}\\b', p)][:10])\n        break\nEOF"
}
```


## [2026-09-06T15:36:32.336Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== Buck fall ===\"\ngrep -n \"10.23 FALL\\|FALL (vb\\.)\\|16.41 HATE\" SYN.txt | head"
}
```


### [2026-09-06T15:36:33.098Z] TOOL RESULT

```
0-based leaf 174 -> printed 153
BRT leaf 266
[]
```


### [2026-09-06T15:36:33.147Z] TOOL RESULT

```
=== Buck fall ===
16900:10.23 FALL (vb.) Goth. driusan
28579:16.41 HATE (sb.)
```


## [2026-09-06T15:36:40.796Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('BRT.txt',encoding='utf-8',errors='replace').read()\npgs=t.split('\\f')\np=pgs[266]\nprint([x for x in re.findall(r'(?m)^\\s*(\\d{2,4})\\s*$', p)][:10])\nprint(p[:300])\nEOF\necho \"==== Buck 10.23 ====\"\nsed -n '16900,16915p' SYN.txt\necho \"==== Buck 16.41 ====\"\nsed -n '28579,28600p' SYN.txt"
}
```


### [2026-09-06T15:36:42.598Z] TOOL RESULT

```
['438']
��  J)  Wo  f.il,j! mit  ku\ra  wechselt.  ^
■  j.  kaO'wä-  f.  'Eselin'*':  -wa  dagnu{%ü) aryö  "um   den   Preis  fiir  eine  Eselstute"
V.7.4>-
')  Der  Esel  gil'  nn'er  den  slasm-  (Grossrieh) Hir  das  wenigst  wertTolle  Tier.  Die  Reihenfolge ist  (V.  7.  42):  Esel,  Rind,  Ross,  Kam
==== Buck 10.23 ====
10.23 FALL (vb.) Goth. driusan
Lith. pultt, kristi
_isT0 ON  falla Lett. Krist ork. ‘igo Dan. falde ChSl. pasti, padali NG caderé Sw. _ falla SCr.  pasti, padati Jat gdere OE __ feallan, dréosan Boh. padnouti Ie jgmber ME _falle, droppe Pol. pas¢é, padaé Fe oger NE fall, drop Russ. past’, padat' a cidea Du. _ vallen Skt.  pad-, pat- i do-tuit OHG  fallan Av. pat- Nir. {uilim thio MHG vallen y. cwympas SU NHG fallen Br koeza rds for ‘fall’ the central notion is | OFr. tumer ‘leap’, loanword fr. the Gme. : Whee rapid, downward motion, as | group seen in OHG éwmon ‘turn around’, Mot ai object falling by its own | NHG taumeln ‘stagger’, OE tumbian an But in many of them the ‘down- ‘tumble, dance’, NE tumble, etc., all yard’ element, though become domi- | prob. of imitative origin. REW 8975.
nant, is of secondary origin, & specializa- tion from some notion of rapid move- ment, This is especially obvious in the case of the root which serves for both fall’ and ‘fly’ in Indo-Iranian and also, though with differentiated forms of it, in Greek (below, 1). Some are probably of imitative origin, based on expressive syllables analogous to NE plump, thud, ete.
1, IE *pet-. Walde-P. 2.19.
Grk. rrr ‘fall’, NG pop. réptw (x7 > or regular; « from aor. éreca, cf. Hat- vidakis, Meo. 2.503), beside éropar fy’; Skt., Av. pat- ‘fall’ and ‘fly’, uenaias ‘made an uprising, re- psn ; Lat. petere ‘go after, seek’, etc.
he sense ‘fly’ is the most widespread notably in the derivs. for ‘wing, feather’, and was probably the prima a f ne noi, Cl.1038, “But the notron of rapid motion unites all e notion of rapid
all the uses.
eee cadere (> It. cadere, Sp. caer,
tal oh ‘ o OFr. cheoir) : Skt: cad- : aa oe casar ‘hail, lightning’,
» Walde-P, 1. ;
17 cos a 339. Ernout-M.
a 128.
18th ee Teplacing cheoir (above) in Mee sta 1 Lomber, tumber ‘1 Stagger, make tumble’, prob, with
Gamillscheg 847.
3. Ir. do-tuit (8sg.), NIr. tuitim, prob. through ‘hit the ground’ : Lat. tundere ‘beat, pound’, Skt. tud- ‘push, thrust, prick’, Goth. stautan ‘smite’, etc. Walde-P. 2.618. Pedersen 2.656 fi.
==== Buck 16.41 ====
16.41 HATE (sb.)
Grk. —ptoos, éxOpa Goth. jijapwa Lith. neapykania NG pioos, éx0pa ON hair Lett.  (ze)naids Lat. odium Dan. - had ChSl. nenavistt It. odio Sw. hat SCr. mrznja Fr. haine OE hete, hatung Boh. nendvist Sp. odio ME shete, hate, hatrede Pol.  nienawisé Rum. urd NE hate, hatred Russ. nenavist! Ir. (mis)cais Du. haat Skt.  duig-, dvega- Nir. fuath OHG haz Av. dvaesah- W. cas, casineb MHG haz
Br. kas, kasoni NHG hass
Words for ‘hate’, expressing intense dislike, and the strongest opposite of ‘love’, show a variety of connections, as with words for ‘shudder’, ‘smell’(?), ‘loathe, revile, blame’, etc., in large meas- ure through the obj. notion ‘object of repulsion’. Some are from verbs for ‘hate’ which mean literally ‘not endure’ (cf. NE collog. I can’t bear him or I can’t stand him = I dishke him intensely), or ‘not look upon’ (with favor).
While only the nouns are given in the list, they all have corresponding verbs.
1. Grk. picos (not in Hom.), with vb. utcéw (once in Hom. as ‘hate the thought of’ with infin..clause), etym.? Boisacd 640.
Grk. %os, with vb. éx8alpw words for ‘hate’ in Hom.), prose sb. ‘hatred, enmity’, beside exOpés hateful, enemy’ (19.52), derivs. °
(usual
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
pylon ee MEAS notion of ‘alien’ or ‘exile’.
r throws 6 (with references).
It., Sp. odio), be-
ateam ‘hate’, ateli
sda: Arm. rete! OE atol ‘terrible, hor- Lox atall ‘fierce’, fr. a root ¥od-,
the same as *od- ‘smell’ at. odor, etc. (15.21) notion of ‘disgust’ (Lat. odiwm ». algo and in Plautus most frequently ta “a object of disgust, repulsion; cf. 0b) Etat Glotta 2.230 ff.; cf. also ar mrznja, below, 6). Walde-P. 1.174. Pmout-M. 698 (not accepting connec- tion with odor, etc.).
Tr. haine, for haine, fr. vb. hair, loan- yord, fr. Gme., cf. Goth. hatjan ‘hate’, ete, (below, 4). REW 4075.
Rum. urd, back-formation fr. vb. uri thate’, this fr. Lat. horrére, horréscere ‘shudder’. Cf. Alb. urretje ‘hate’ fr. the same source. REW 4185. Tiktin 1688, 1692. G. Meyer, Alb. Etym. Wtb. 459. 8. Ir. cats and miscais (cpd. with pejorative mis-), W. cas, Br. kas, derivs. W. casineb, Br. kasoni : Goth. hatis, etc. (the Gme. group, below, 4), Grk. xidos ‘care, anxiety, grief, mourning’, Av. sidra- ‘hurt, harm’. The orig. meaning te perh. ‘care’, whence both ‘hate’ and on In a cais (cf. 16. 27). Walde-P. Torp 370 oo 1.121, 2.10. Falk- Uy
aque diy same word as fuath form, of ‘hate? fee ae ni ee pow epment above, 9), et Doron’ (ef. Rum. urd,
4, , [oe oe (only for Bipds, dpi ON aa’ - a hatan, hatjan for yoke), as, a ele, OHG haz, etc., general : Corresponding vbs. Goth. ects. (influence of vow- sb. in ME, NE hate; OE
‘ung, fr, yp, Whaney ME hatereden, hatrede, dition’) . I » pd. with OF reden ‘con-
» dr, ¢ “us ‘hate’, ete. (above, 3).
Digitized by Arya Samaj Foundation Chennai and eGangotri
```


## [2026-09-06T15:37:26.558Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Slavic/kapja\" --note \"page 232, Kafa root note: Russian kaplja cognate claim\"\npython3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/kap%CA%B0as\" --note \"page 232, Kafa root: Skt kapha cognate\""
}
```


### [2026-09-06T15:37:29.314Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/940da33afdea4cbe.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/51bc1c197660c48f.txt
```


## [2026-09-06T15:37:32.974Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"=== *kapja ===\"; grep -n -i \"etymology\\|From\\|onomat\\|Derived\\|kapati\" 940da33afdea4cbe.txt | head -15\necho; echo \"=== PII kapʰas ===\"; sed -n '1,6p' 51bc1c197660c48f.txt; grep -n -i \"etymology\\|From\\|Descendants\\|Avestan\\|Sanskrit\\|foam\\|phlegm\" 51bc1c197660c48f.txt | head -20"
}
```


### [2026-09-06T15:37:33.043Z] TOOL RESULT

```
=== *kapja ===

=== PII kapʰas ===
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/kap%CA%B0as
FETCHED: 2026-09-06T15:37:29Z
STATUS: 200
TITLE: Reconstruction:Proto-Indo-Iranian/kapʰas - Wiktionary, the free dictionary

Reconstruction:Proto-Indo-Iranian/kapʰas - Wiktionary, the free dictionary 
62: Etymology 
74: Descendants 
133: From Wiktionary, the free dictionary
140: Etymology
143: Possibly borrowed from the BMAC substrate . [ 1 ] 
150: mucus , phlegm 
157: Classical Persian: کپک ( kapak , “ mold ” ) , کفک ( kafak , “ foam, fluff, fuzzy thing ” ) 
163: Khwarezmian: کفوچ ( kfwc /⁠*kəfuč⁠/ , “ foam ” ) 
165: Classical Persian: کفچ ( kafč , “ foam of milk; foam of soap ” ) 
242: Descendants
246: Sanskrit: कफ ( kapha ) ( see there for further descendants )
249: Avestan: 𐬐𐬀𐬟𐬀 ( kafa ) 
254: Khotanese: [script needed] ( khavä , “ foam ” ) 
256: Wakhi: ( /⁠xūf⁠/ , “ foam ” ) 
266: Sogdian: ( /⁠kuf, kof⁠/ , “ foam ” ) 
270: Yaghnobi: хаф ( xaf , “ foam ” ) , хафа ( xafa ) 
272: Pashto: خج ( xaǰ , “ foam ” ) ( perhaps ) 
274: Yidgha: خوف ( xōf , “ foam ” ) 
276: Baluchi: کپ ( kap , “ foam ” ) 
278: Kurdish: ( “ foam ” )
```


## [2026-09-06T15:37:47.672Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nsed -n '1,8p' 940da33afdea4cbe.txt\necho \"--- 157/165 context in PII page ---\"\nsed -n '150,170p' 51bc1c197660c48f.txt"
}
```


### [2026-09-06T15:37:47.724Z] TOOL RESULT

```
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Slavic/kapja
FETCHED: 2026-09-06T15:37:28Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found--- 157/165 context in PII page ---
 mucus , phlegm 

 Derived terms
 [ edit ] 

 Proto-Indo-Iranian: 
 Proto-Iranian: *kafakah 
 Classical Persian: کپک ( kapak , “ mold ” ) , کفک ( kafak , “ foam, fluff, fuzzy thing ” ) 
 Persian: کپک ( kapak ) , کفک ( kafak ) 
 Tajik: капак ( kapak ) , кафак ( kafak ) , кафк ( kafk ) 

 Proto-Indo-Iranian: 
 Proto-Iranian: *kafčah 
 Khwarezmian: کفوچ ( kfwc /⁠*kəfuč⁠/ , “ foam ” ) 

 Classical Persian: کفچ ( kafč , “ foam of milk; foam of soap ” ) 

 Declension
 [ edit ] 

 masculine a-stem
```


## [2026-09-06T15:38:05.541Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/%D0%BA%D0%B0%D0%BF%D0%BB%D1%8F\" --note \"page 232, Kafa root note: Russian kaplja etymology\" >/dev/null\ngrep -n -i \"Etymology\\|kapati\\|Proto-Slavic\\|drip\" data/verification/sources/web/$(python3 -c \"\nimport hashlib;print(hashlib.sha1('https://en.wiktionary.org/wiki/%D0%BA%D0%B0%D0%BF%D0%BB%D1%8F'.encode()).hexdigest()[:16])\").txt | head -10"
}
```


### [2026-09-06T15:38:07.643Z] TOOL RESULT

```
65: Etymology 1 
83: Etymology 2 
183: Etymology 1
186: Inherited from Old East Slavic каплꙗ ( kaplja ) , from Proto-Slavic *kapľa , from *kapati + *-ja .
292: Etymology 2
314: Russian terms inherited from Proto-Slavic 
315: Russian terms derived from Proto-Slavic
```


## [2026-09-06T15:39:10.517Z] TOOL CALL #68: Bash

```json
{
 "command": "sed -n '1,80p' /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-06T15:39:10.585Z] TOOL RESULT

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


## [2026-09-06T15:39:13.137Z] TOOL CALL #69: Bash

```json
{
 "command": "sed -n '80,140p' /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-06T15:39:13.178Z] TOOL RESULT

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


## [2026-09-06T15:39:15.756Z] AGENT

Now writing the verification file.


## [2026-09-06T15:41:43.124Z] TOOL CALL #70: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build232.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\n\ndata = {\n \"pdf_page\": 232,\n \"book_page\": 202,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-06\",\n \"entries\": []\n}\n\n# ------------------------------------------------------------------ entry 0\ne0 = {\n \"entry\": 0,\n \"root\": \"Kâd 1\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *ḱeh₂d- 'hatred, angriness' (Pokorny's 'kād- : kǝdes- : kod-s- „seelische Verstimmung; Kummer, Haß“; kādos- „Sorge, Leid“', IEW 517)\",\n \"note\": \"Root box, language label and gloss are all correct, and the page reference is exact. Pokorny IEW 517 (POK_02.txt leaf 175, immediately after the printed page-number '517') heads the article 'kād- : kǝdes- : kod-s- „seelische Verstimmung; Kummer, Haß“; kādos- „Sorge, Leid“' and lists under it precisely Nourai's two branches: 'av. sādra- n. „Leid, Wehe, Unheil“' and 'got. hatis n. „Haß, Zorn“, anord. hatr n., ags. hete m., as. heti m., ahd. haz m.'. Watkins/AHD 1985 has the same root twice-listed as Nourai does: 'kad-. Sorrow, hatred … [Pok. kād- 517]' beside 'kad-. To fall … [Pok. 1. kad- 516]', which is exactly why Nourai numbers his boxes Kâd 1 (long â = Pokorny's kād-) and Kad 2 (short a = Pokorny's 1. kad-). The only modernisation needed is notational: the root is now written *ḱeh₂d- (palatal *ḱ, laryngeal for Pokorny's long ā), the shape that accounts for the palatal sibilant of Sanskrit ri-śā́das-; Wiktionary glosses it 'hatred, angriness' and files Avestan sādra and Proto-Germanic *hataz under it, i.e. the same two branches. Wiktionary adds that a link to *ḱh₂d- 'to fall' (Nourai's Kad 2) has been proposed but is 'speculative' — so keeping the two boxes apart, as Nourai does, is the safe course.\",\n \"note_fa\": \"جعبهٔ ریشه درست است. پوکورنی در صفحهٔ ۵۱۷ فرهنگ خود مدخل «kād- : kǝdes- : kod-s-» را با معنای «آشفتگی روحی؛ اندوه، کینه» آورده و درست همان دو شاخه‌ای را زیر آن می‌نشاند که نورایی رسم کرده است: اوستایی sādra- «رنج، درد، بلا» و ژرمنی (گوتی hatis «کینه، خشم»). واتکینز در پیوست فرهنگ AHD نیز همین ماده را دو بار آورده است: «kad-: اندوه، کینه [پوکورنی ۵۱۷]» و «kad-: افتادن [پوکورنی ۵۱۶]» — و همین دوگانگی توضیح می‌دهد که چرا نورایی دو جعبهٔ «Kâd 1» (با آی کشیده) و «Kad 2» (با آی کوتاه) ساخته است. تنها تفاوت با پژوهش امروزی نگارشی است: این ریشه اکنون *ḱeh₂d- نوشته می‌شود (با کاف کامی و حنجری به جای آی کشیدهٔ پوکورنی) و همین صورت است که سایشی کامی سنسکریت ri-śā́das- را توضیح می‌دهد. ادعای نورایی درست است.\",\n \"sources\": [\n   W + \"Reconstruction:Proto-Indo-European/ḱeh₂d-\",\n   W + \"hate\"\n ],\n \"ref_check\": [\n   {\"ref\": \"POK:517\", \"status\": \"supports\",\n    \"note\": \"POK_02.txt, form-feed leaf 175 (the leaf that carries the printed running number '517'): 'käd- : k9des- : kod-s- ,seelische Verstimmung; Kummer, Haß‘; kädos- ,Sorge, Leid‘. — Ai. ri-sädas- ,für den Fremden sorgend‘; av. sädra- n. ,Leid, Wehe, Unheil‘ (Geldner KZ. 27, 242 f.) … got. hatis n. ,Haß, Zorn‘, anord. hatr n., ags. hete m., as. heti m., ahd. haz m. ,Haß‘ … WP. I 340 f.' (grep pattern: \\\"käd-  :  k9des-\\\"). Exactly the root box, its gloss and both of its branches.\"}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. I 340 f. (WLD_Bd1_1930_dli_70244_djvu.txt line 21474; the following leaf carries the running head '342 qap-', the preceding one '340 kad- — kad-')\",\n    \"stance\": \"supports\",\n    \"note\": \"'kad- „seelische Verstimmung: Kummer, Haß“. Av. sadra- n. „Leid, Wehe, Unheil“ (Geldner KZ. 27, 242 f.); gr. κῆδος n., dor. κᾶδος „Sorge, Trauer …“; osk. cadeis amnad „inimicitiae causa“; mir. caiss, cymr. cas, bret. cas „Haß“; got. hatis n. „Haß, Zorn“, anord. hatr n., ags. hete m. …'. This is the article Pokorny 517 abridges.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985, k-list (AHD_watkins1985.txt line 562)\",\n    \"stance\": \"supports\",\n    \"note\": \"'kad-. Sorrow, hatred. Suffixed zero-grade form *kad-i- in: a. Germanic *hatiz in Old English hete, hate, envy (> Middle English hate): HATRED. b. Germanic *haton in Old English hatian, to hate: HATE; c. Germanic *hatjan in Old French hair, to hate: HEINOUS. [Pok. kād- 517.]' — Nourai's gloss 'sorrow, hatred' is verbatim Watkins.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck §16.41 HATE (sb.) (SYN.txt line 28579 ff.)\",\n    \"stance\": \"supports\",\n    \"note\": \"'Ir. cais and miscais …, W. cas, Br. kas … : Goth. hatis, etc. (the Gmc. group), Grk. κῆδος „care, anxiety, grief, mourning“, Av. sādra- „hurt, harm“. The orig. meaning is perh. „care“, whence both „hate“ and … Walde-P. 1.121, 2.10.' Buck independently puts Avestan sādra- and Gothic hatis in one etymon, which is the whole content of Nourai's root box.\"},\n   {\"src\": \"KLN\", \"where\": \"s.v. 'hate' / 'heinous' (KLN_1966.txt)\",\n    \"stance\": \"silent\",\n    \"note\": \"Klein's English entries give the Germanic material (OE hete, hatian) but do not cite the Avestan side, so he neither confirms nor contradicts the Iranian branch.\"}\n ],\n \"nodes\": []\n}\n\ne0[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Avestan\", \"words\": \"sâdra\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Avestan sādra- n. 'suffering, woe, calamity' is a *-ro-derivative of the root, PIE *ḱeh₂d-ro- > Proto-Indo-Iranian *ćādra- > Av. sādra- (PIE palatal *ḱ gives Indo-Iranian *ć, which yields Avestan s-, exactly as in Skt. ri-śā́das-). It is a genuine, well attested Gathic word: Y.45.7 'yə̄ narə̄š sādrā drəgvatō' (Bartholomae translates 'immer (wird sein) was die Qualen (sind) …'), Y.43.11 'sādrā mōi są̄s … ' 'shall bring me suffering among men', Vr.18.2, and the Pahlavi commentary renders it tangīh 'straitness, distress'. Pokorny 517 and Walde-Pokorny I 340 both cite it in exactly this form and gloss, and Wiktionary's *ḱeh₂d- page lists 'Avestan 𐬯𐬁𐬛𐬭𐬀 (sādra, “misery, suffering”)' as its Iranian outcome. Nourai's transliteration 'sâdra' and gloss 'pain, grief' are accurate.\",\n \"derivation_fa\": \"واژهٔ اوستایی sādra- (خنثی) به معنی «رنج، درد، بلا» ساخته‌ای است با پسوند ‑ra از همان ریشه: هندواروپایی آغازین *ḱeh₂d-ro- ← هندوایرانی آغازین *ćādra- ← اوستایی sādra-؛ کاف کامی هندواروپایی در هندوایرانی به سایشی کامی و در اوستایی به «س» بدل شده است (همان‌گونه که در سنسکریت ri-śā́das- به «ش» رسیده). این واژه در گاهان بارها آمده است، برای نمونه یسنا ۴۵٫۷ «yə̄ narə̄š sādrā drəgvatō» و یسنا ۴۳٫۱۱، و مفسّر پهلوی آن را «تنگی» ترجمه کرده است. پوکورنی (ص ۵۱۷) و والده‑پوکورنی (ج ۱ ص ۳۴۰) هر دو همین صورت و همین معنی را می‌آورند و ویکی‌واژه نیز آن را زیر ریشهٔ *ḱeh₂d- می‌نشاند. آوانویسی و معنایی که نورایی داده درست است.\",\n \"sources\": [W + \"Reconstruction:Proto-Indo-European/ḱeh₂d-\"],\n \"ref_check\": [\n   {\"ref\": \"POK:517\", \"status\": \"supports\",\n    \"note\": \"POK_02.txt leaf 175, the line immediately under the root heading: 'av. sädra- n. ,Leid, Wehe, Unheil‘ (Geldner KZ. 27, 242 f.)'. Pokorny puts the Avestan word first among the descendants, exactly as Nourai's chart does.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch (BRT.txt): the word is quoted throughout the dictionary, e.g. under narə̄- ('yūtā yā narə̄š sādra drəgvatō' Y.45.7, BRT.txt line 25629) and under vīspāyav- (''yūtāiia uštatātǝm … yā narə̄ sādra drvatō' Vr.18.2, line 24452); the cross-reference at s.v. sav- (line 26023) reads 's. in sādra- und šaciiā-'\",\n    \"stance\": \"supports\",\n    \"note\": \"Bartholomae has a sādra- article (the cross-reference proves it) and the citations he prints are the standard Gathic passages; his rendering of Y.45.7 ('was die Qualen sind') matches the gloss 'pain, grief'. The headword block itself is mangled in the OCR of the s- fascicle, so I quote the citations rather than the lemma line.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. I 340 (WLD_Bd1 djvu line 21476)\", \"stance\": \"supports\",\n    \"note\": \"'Av. sadra- n. „Leid, Wehe, Unheil“ (Geldner KZ. 27, 242 f.)' — the first witness listed under kad- „seelische Verstimmung“.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck §16.41 (SYN.txt line 28590 ff.)\", \"stance\": \"supports\",\n    \"note\": \"'… Goth. hatis, etc. …, Grk. κῆδος „care, anxiety, grief, mourning“, Av. sādra- „hurt, harm“.'\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 2, \"lang\": \"Persian\", \"words\": \"sâr «سار ۲»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"New Persian سار sār 'pain, affliction, torment' (Borhān-e Qāṭeʿ: 'و آزار و محنت باشد') continues Avestan sādra- through a Middle Persian *sāhr. Hübschmann sets out the phonetics explicitly (Persische Studien p.191, in his section on Avestan δ before r): Avestan δr becomes Persian hr — 'Ebenso ist δ vor r zu h geworden' (muhr : Skt. mudrā-, nihr/nirh : Skt. nidrā-) — and then h is lost after a long vowel, 'np. sār „Schmerz, Leid“ aus *sahr = zd. sādra- „Leid, Elend“'. Horn gives the same equation as a numbered entry, no. 689 '(i)sār „Schmerz, Leid“ — aw. sādra- „Wehe, Leid“' (printed p.153). Mo'in's own footnote in his edition of the Borhān, printed at the foot of the سار page, says it in Persian: '۴ - در اوستا sādra- (درد، غصه)… سادرِ اوستایی در تفسیر پهلوی «تنگی» ترجمه شده'. This سار is homonymous with, and distinct from, سار 'starling' (the only sense Wiktionary records) and the suffix ‑سار of کوهسار/شرمسار; Nourai's «سار ۲» numbering keeps them apart correctly.\",\n \"derivation_fa\": \"«سار» به معنی «آزار و محنت، رنج، درد» (تعریف برهان قاطع: «و آزار و محنت باشد») دنبالهٔ اوستایی sādra- است که از راه فارسی میانهٔ *sāhr به فارسی نو رسیده. هوبشمان در «پژوهش‌های فارسی» ص ۱۹۱ همین را با آواشناسی روشن می‌کند: «ذ» اوستایی پیش از «ر» در فارسی به «ه» بدل شده (مانند muhr در برابر سنسکریت mudrā- و nirh در برابر nidrā-) و سپس این «ه» پس از واکهٔ کشیده افتاده است؛ پس «np. sār از *sahr = اوستایی sādra-». هرن نیز در «مبانی ریشه‌شناسی فارسی نو» شمارهٔ ۶۸۹ (ص ۱۵۳) همین برابری را آورده است: «(i)sār درد و رنج — اوستایی sādra-». حاشیهٔ خود معین بر برهان قاطع در پای همین صفحه می‌نویسد: «۴ - در اوستا sādra- (درد، غصه)… سادرِ اوستایی در تفسیر پهلوی «تنگی» ترجمه شده». این «سار» با «سارِ» پرنده (تنها معنایی که ویکی‌واژه دارد) و با پسوند «‑سار» در کوهسار و شرمسار یکی نیست، و شمارهٔ «۲» که نورایی گذاشته درست همین تفکیک را نشان می‌دهد. ادعای نورایی درست است.\",\n \"sources\": [\"https://abadis.ir/fatofa/سار/\", W + \"سار\"],\n \"ref_check\": [\n   {\"ref\": \"BQT:1069\", \"status\": \"supports\",\n    \"note\": \"Borhān-e Qāṭeʿ ed. Mo'in, the سار article (BQT_v2_pages.txt form-feed leaf 531, which by the volume's leaf+540 offset falls at printed p.1071 — i.e. Nourai's 1069 is within the ±2 drift of that offset near the end of vol. 2). Body of the entry: '… و بمعنی شبه و نظیر و مثل و مانند هم آمده است همچو دیوسار و خاکسار … و آزار و محنت باشد ۴'. Mo'in's footnote 4 at the foot of the same page: '۴ - در اوستا [sādra-] (درد، غصه) … سادرِ اوستایی در تفسیر پهلوی «تنگی» ترجمه شده … رک: خرده اوستا، پورداود ص ۲۹۱'. That is exactly Nourai's arrow, in Mo'in's own words.\"},\n   {\"ref\": \"MON:1790\", \"status\": \"supports\",\n    \"note\": \"Mo'in, Farhang-e Fārsi, s.v. سار; the six-volume print is not online, but the entry text is reproduced verbatim by abadis.ir in its 'فرهنگ معین' section: 'سار [ اوست . ] ۱ - (اِ.) رنج ، محنت ، آزار. ۲ - (ص .) رنجور.' — Mo'in tags the word [اوست.] = 'from Avestan' and glosses it 'pain, affliction, torment', precisely Nourai's node. Only the page number itself could not be checked.\"}\n ],\n \"consulted\": [\n   {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 689 (HRN.txt form-feed leaf 174 = printed p.153)\", \"stance\": \"supports\",\n    \"note\": \"'689. (i)sār „Schmerz, Leid“. aw. sādra- „Wehe, Leid“.' Horn's numbered entry is the classical statement of exactly this derivation.\"},\n   {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien p.191 (HUB.txt leaf 201, line 7061)\", \"stance\": \"supports\",\n    \"note\": \"'Mit Verlust des h nach langem Vokal: np. sār „Schmerz, Leid“ aus *sahr = zd. sādra- „Leid, Elend“.' Hübschmann supplies the intermediate Middle Persian form *sāhr and the sound law (δr > hr > r after a long vowel).\"},\n   {\"src\": \"MON\", \"where\": \"Mo'in via abadis.ir/fatofa/سار (section فرهنگ معین)\", \"stance\": \"supports\",\n    \"note\": \"'سار [ اوست . ] ۱ - (اِ.) رنج ، محنت ، آزار. ۲ - (ص .) رنجور.'\"},\n   {\"src\": \"BQT\", \"where\": \"Borhān-e Qāṭeʿ, سار article + Mo'in's footnote 4 (BQT_v2_pages.txt leaf 531)\", \"stance\": \"supports\",\n    \"note\": \"'… و آزار و محنت باشد' with the footnote 'در اوستا sādra- (درد، غصه)'.\"},\n   {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD (PHD.txt, s- section)\", \"stance\": \"silent\",\n    \"note\": \"No Middle Persian *sāhr / sār 'grief' is listed in MacKenzie; the intermediate form is Hübschmann's reconstruction, not an attested Book-Pahlavi lemma.\"},\n   {\"src\": \"KLN\", \"where\": \"en.wiktionary.org/wiki/سار (used as an independent modern check)\", \"stance\": \"silent\",\n    \"note\": \"Wiktionary's Persian سار has only the sense 'starling' and no etymology for the 'grief' word — silent, not contradicting.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 3, \"lang\": \"Germanic\", \"words\": \"hatiz\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Proto-Germanic *hataz / oblique *hatiz- is an s-stem neuter built on the zero grade of the root, PIE *ḱh₂d-os ~ *ḱh₂d-es-os > PGmc *hataz, gen. *hatiziz. It is directly attested as Gothic hatis n. 'hate, wrath' and continued by Old Norse hatr n., Old English hete m., Old Saxon heti m., Old High German haz m. — the list Pokorny 517 prints. Nourai's citation form 'hatiz' is Watkins's: AHD gives 'Suffixed zero-grade form *kad-i- in a. Germanic *hatiz in Old English hete'; Wiktionary lemmatises the same stem by its nominative *hataz, with *hatiz- the oblique/pre-form. The Germanic h- is the regular Grimm's-Law outcome of PIE *ḱ (velar merger of the palatals in centum languages), and the -t- the outcome of *d.\",\n \"derivation_fa\": \"صورت ژرمنی آغازین *hataz (با ستاک غیرمستقیم *hatiz-) نام خنثای ستاک‑s است که بر پایهٔ درجهٔ صفرِ ریشه ساخته شده: هندواروپایی *ḱh₂d-os ~ *ḱh₂d-es-os ← ژرمنی *hataz. این واژه مستقیماً در گوتی hatis «کینه، خشم» گواهی شده و در نورس کهن hatr، انگلیسی کهن hete، ساکسون کهن heti و آلمانی علیای کهن haz دنباله یافته — همان فهرستی که پوکورنی در ص ۵۱۷ می‌آورد. صورتی که نورایی نوشته («hatiz») همان صورت واتکینز در پیوست AHD است؛ ویکی‌واژه همان ستاک را با حالت فاعلی *hataz مدخل کرده است. «ه» ژرمنی برآمد قانونمند کاف هندواروپایی بر پایهٔ قانون گریم است و «ت» برآمد «د». ادعای نورایی درست است.\",\n \"sources\": [W + \"hate\", W + \"Reconstruction:Proto-Indo-European/ḱeh₂d-\"],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"AHD_watkins1985.txt line 562: 'kad-. Sorrow, hatred. Suffixed zero-grade form *kad-i- in: a. Germanic *hatiz in Old English hete, hate, envy (> Middle English hate): HATRED.' Nourai's node is Watkins's *hatiz verbatim.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"IEW 517 (POK_02.txt leaf 176, top)\", \"stance\": \"supports\",\n    \"note\": \"'got. hatis n. ,Haß, Zorn‘, anord. hatr n., ags. hete m., as. heti m., ahd. haz m. ,Haß‘ … ablaut. as. hoti ,feindlich‘.'\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. I 341 (WLD_Bd1 djvu line ~21497)\", \"stance\": \"supports\",\n    \"note\": \"'got. hatis n. „Haß, Zorn“, anord. hatr n., ags. hete m., as. heti m., ahd. …' — same s-stem, filed under kad- „seelische Verstimmung“.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck §16.41 (SYN.txt line 28579 ff.)\", \"stance\": \"supports\",\n    \"note\": \"'Goth. hatis (only for θυμός, ὀργή), ON hatr, OE hete, OHG haz, etc., general Gmc.' with the corresponding verbs Goth. hatan, hatjan.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 4, \"lang\": \"English\", \"words\": \"hate\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"English hate continues the Germanic word by two strands that fell together: the noun Old English hete 'hate, envy' (< PWGmc *hati < PGmc *hataz) gave Middle English het, hete, while the verb Old English hatian 'to hate, treat as an enemy' (< PGmc *hatōn) gave ME haten and, by the ordinary Middle English deverbal pattern, the modern noun haate/hate; Old Norse hatr n. reinforced the noun in the Danelaw. Watkins prints both routes side by side ('Germanic *hatōn in Old English hatian, to hate: HATE'), and hatred is ME hatereden, hate + ‑rede 'condition' (OE rǣden). Nourai's arrow Germanic → English is right; it simply passes over Old and Middle English, which for so transparent a chain is harmless.\",\n \"derivation_fa\": \"واژهٔ انگلیسی hate از دو رشتهٔ درهم‌تنیده می‌آید: نامِ انگلیسی کهن hete «کینه، رشک» (از ژرمنی غربی *hati و آن از ژرمنی *hataz) که به انگلیسی میانهٔ het/hete رسید، و فعلِ انگلیسی کهن hatian «کینه ورزیدن» (از ژرمنی *hatōn) که به haten انگلیسی میانه رسید و نام امروزی hate بیشتر از همین فعل ساخته شده است؛ نورس کهن hatr نیز در نواحی دانلا این نام را تقویت کرد. واتکینز هر دو راه را کنار هم آورده است. پیکان «ژرمنی ← انگلیسی» نورایی درست است و تنها حلقه‌های انگلیسی کهن و میانه را نانوشته گذاشته که در زنجیره‌ای چنین آشکار زیانی ندارد.\",\n \"sources\": [W + \"hate\"],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\",\n    \"note\": \"The node carries no reference of its own in the book; it inherits the AHD citation of its parent (#3), which was checked and supports the chain ('Germanic *hatōn in Old English hatian, to hate: HATE').\"}\n ],\n \"consulted\": [\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. kad- (AHD_watkins1985.txt line 562) and the index (line 1579 'HATE kad-')\", \"stance\": \"supports\",\n    \"note\": \"'b. Germanic *hatōn in Old English hatian, to hate: HATE; c. Germanic *hatjan in Old French hair, to hate: HEINOUS.'\"},\n   {\"src\": \"SYN\", \"where\": \"Buck §16.41 (SYN.txt line 28579 ff.)\", \"stance\": \"supports\",\n    \"note\": \"'… vbs. Goth. hatan, hatjan, ON hata, OE hatian … sb. in ME, NE hate; OE hete … ME hatereden, hatrede, cpd. with ‑reden „condition“.'\"},\n   {\"src\": \"KLN\", \"where\": \"en.wiktionary.org/wiki/hate (Klein's own entry adds nothing beyond it)\", \"stance\": \"supports\",\n    \"note\": \"'From Middle English haate, hat, hate (noun), probably from Old English hatian … and/or Old Norse hatr … Merged with Middle English het, hete, from Old English hete, from Proto-West Germanic *hati, from Proto-Germanic *hataz, from Proto-Indo-European *ḱeh₂d-.'\"}\n ]\n})\ndata[\"entries\"].append(e0)\nPYEOF\necho ok"
}
```


### [2026-09-06T15:41:46.635Z] TOOL RESULT

```
ok
```


## [2026-09-06T15:44:47.872Z] TOOL CALL #71: Bash

```json
{
 "command": "cat >> /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build232.py <<'PYEOF'\n\n# ------------------------------------------------------------------ entry 1\ne1 = {\n \"entry\": 1,\n \"root\": \"Kad 2\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *ḱad- / *ḱh₂d- 'to fall' (Pokorny '1. kad- „fallen“', IEW 516; Watkins 'kad-. To fall')\",\n \"note\": \"Correct root, correct language label, correct gloss, correct page. Pokorny IEW 516 (POK_02.txt leaf 175, above the printed '517') reads '1. kad- ,fallen‘. Ai. sad-, Perf. sasāda, Fut. satsyati „abfallen, ausfallen“ (: lat. cado); arm. cacnum (*kadi̯o-) „fallen, niedrig werden“; lat. cadō, -ere „fallen“ …; air. casar f. „Hagel; Blitz“ …', and Watkins gives 'kad-. To fall. Latin cadere, to fall, die: CADAVER, CADENCE, CADENT, CADUCOUS, CASCADE, CASE¹, CHANCE, CHUTE; ACCIDENT, …, DECAY, DECIDUOUS, ESCHEAT, INCIDENT, OCCASION, RECIDIVISM. [Pok. 1. kad- 516.]' — which is, word for word, the harvest of Nourai's two Latin nodes and his English node. The whole entry is uncontroversial: every word on it is a Latin verb of falling or a Romance reflex of one, and the only refinement modern handbooks add is that the Latin material is now cited as *ḱad- (or *ḱh₂d-, the zero grade of the same shape as Kâd 1 — a link Wiktionary calls speculative). The chart's one soft spot is presentational rather than substantive: 'cadentia', 'casicare' and 'de-cad-ere' are Vulgar Latin reconstructions (*cadentia, *casicāre, *dēcadere) printed without their asterisks, and the four English words of node 6 all reached English through French (cascade through Italian first), a step the chart draws over.\",\n \"note_fa\": \"ریشه، برچسب زبانی، معنا و شمارهٔ صفحه هر چهار درست است. پوکورنی در ص ۵۱۶ مدخل «1. kad- «افتادن»» را دارد با گواهان سنسکریت śad-/sad- «فروافتادن»، ارمنی cacnum و لاتینی cadō, cadere؛ واتکینز نیز «kad-: افتادن. لاتینی cadere» را با فهرستی از واژه‌های انگلیسی می‌آورد که دقیقاً همان برداشت دو گرهٔ لاتینی و گرهٔ انگلیسی نورایی است. در ریشه‌شناسی امروزی این ماده *ḱad- (یا *ḱh₂d-) نوشته می‌شود. تنها دو نکتهٔ ویرایشی هست: صورت‌های cadentia، casicare و de-cad-ere در واقع بازسازی‌های لاتینی عامیانه‌اند (*cadentia، *casicāre، *dēcadere) که نورایی بدون ستاره چاپ کرده، و هر چهار واژهٔ انگلیسی گرهٔ ۶ از راه فرانسه (و cascade نخست از راه ایتالیایی) به انگلیسی رسیده‌اند، حلقه‌ای که نمودار از روی آن پریده است. در مجموع ادعای نورایی درست است.\",\n \"sources\": [W + \"شانس\", \"https://www.etymonline.com/word/chance\", \"https://www.etymonline.com/word/cascade\"],\n \"ref_check\": [\n   {\"ref\": \"POK:516\", \"status\": \"supports\",\n    \"note\": \"POK_02.txt leaf 175: '1. kad- ,f allen‘. Ai. sad-, Perf. sasäda, Fut. satsyati ,abfallen, ausfallen‘ (: lat. cado); arm. cacnum (*kadio-) ,fallen, niedrig werden‘; lat. cadö, -ere ,fallen‘ (osk. antkadum? s. WH. I 128); cadäver n. ,Leiche‘ als ,Gefallenes‘ (*kadā-ues); cadücus ,hinfällig‘; air. casar f. ,Hagel; Blitz‘ … WP. I 339 f., WH. I 127 f.' The printed page number '517' appears further down the same leaf, at the start of the next article, so 516 is exactly right.\"}\n ],\n \"consulted\": [\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985, k-list (AHD_watkins1985.txt line 561)\", \"stance\": \"supports\",\n    \"note\": \"'kad-. To fall. Latin cadere, to fall, die: CADAVER, CADENCE, CADENT, CADUCOUS, CASCADE, CASE¹, CHANCE, CHUTE; ACCIDENT, CADUCICORN, DECAY, DECIDUOUS, ESCHEAT, INCIDENT, OCCASION, RECIDIVISM. [Pok. 1. kad- 516.]'\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. I 339 (WLD_Bd1 djvu line 21422; the following leaf's running head is '340 kad- — kad-')\", \"stance\": \"supports\",\n    \"note\": \"'1. kad- „fallen“. Ai. cad-, Pf. cacāda … „abfallen, ausfallen“ (: lat. cado …); arm. cacnum „fallen, niedrig werden“; lat. cado, -ere „fallen“; mir. casar „Hagel; Blitz“ …'\"},\n   {\"src\": \"SYN\", \"where\": \"Buck §10.23 FALL (vb.) (SYN.txt line 16900 ff.)\", \"stance\": \"supports\",\n    \"note\": \"'Lat. cadere (> It. cadere, Sp. caer, … OFr. cheoir) : Skt. cad- … Ir. casar „hail, lightning“. Walde-P. 1.339. Ernout-M. 128.' Buck also notes that Fr. tomber replaced cheoir.\"},\n   {\"src\": \"LAT\", \"where\": \"Ernout–Meillet p.145 f. (LAT.txt line 8176 ff.)\", \"stance\": \"supports\",\n    \"note\": \"'cado, cadis, cecidi, casum, cadere … : tomber … Usité de tout temps. Panroman, M.L. 1451, et 1452 cadivus, 1454 caducus.'\"}\n ],\n \"nodes\": []\n}\n\ne1[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Latin\", \"words\": \"cadentia; ob-cad-ere, occâsiô\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Latin cadō, cadere 'to fall' (perf. cecidī, sup. cāsum) is the direct reflex of the root; Ernout–Meillet p.145 f. call it 'usité de tout temps. Panroman'. 'cadentia' is real Latin but as the neuter plural of the present participle cadēns — the grammarians' term similiter cadentia rendering Greek ὁμοιόπτωτα (Cic. Or. 57.194, quoted by Ernout–Meillet) — and it was reinterpreted in Vulgar Latin as a feminine singular *cadentia 'a falling', specifically 'a falling of the dice', which is the sense that produced Old French cheance; Nourai's gloss 'a fall, a chance' captures precisely that double life, though the dice-word should carry an asterisk. 'ob-cad-ere' is Nourai's morphological spelling of Latin occidere, ob- + cadere with the regular weakening of a to i in a medial open syllable (as in ac-cidere, in-cidere); its supine occāsum yields the action-noun occāsiō, ‑ōnis 'the fitting moment, opportunity, occasion' — Ernout–Meillet: 'occido, -is, -cidi, occasum: tomber, succomber … occasus, -us m. … Il n'y a pas de substantif *cāsio, mais occasio est fréquent'.\",\n \"derivation_fa\": \"فعل لاتینی cadō, cadere «افتادن» (ماضی نقلی cecidī، صفت مفعولی cāsum) بازتاب مستقیم ریشه است؛ ارنو و مییه آن را «در همهٔ دوره‌ها به‌کار رفته و در سراسر زبان‌های رومی باقی» می‌خوانند. صورت cadentia در لاتین کلاسیک جمعِ خنثای اسم فاعل cadēns است — اصطلاح دستوری similiter cadentia در برابر ὁμοιόπτωτα یونانی (سیسرون، Orator ۵۷٫۱۹۴) — و در لاتین عامیانه همان را مؤنث مفرد *cadentia «افتادن، افتادن تاس» انگاشتند که سرچشمهٔ cheance فرانسهٔ کهن است؛ معنای دوگانه‌ای که نورایی داده («افتادن، بخت») درست همین است، هرچند صورت دوم باید ستاره‌دار می‌بود. «ob-cad-ere» نگارش تحلیلی نورایی برای occidere لاتینی است: ob- + cadere با ابدال قانونمند a به i در هجای میانی باز (چنانکه در ac-cidere و in-cidere)؛ از ستاک occāsum نامِ occāsiō «هنگام مناسب، فرصت» ساخته شده است.\",\n \"sources\": [\"https://www.etymonline.com/word/chance\"],\n \"ref_check\": [\n   {\"ref\": \"POK:516\", \"status\": \"supports\",\n    \"note\": \"'lat. cadö, -ere ,fallen‘ … cadücus ,hinfällig‘' (POK_02.txt leaf 175). Pokorny gives cadere but not the derived nouns; those come from the AHD citation on the same node.\"},\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"AHD_watkins1985.txt line 561: 'kad-. To fall. Latin cadere … CADENCE, CADENT, … CHANCE …; … OCCASION …'; the index lines 1328 ('CADENCE kad-') and 1952 ('OCCASION kad-') confirm both of this node's items.\"}\n ],\n \"consulted\": [\n   {\"src\": \"LAT\", \"where\": \"Ernout–Meillet, s.v. cado (LAT.txt lines 8176-8230, printed pp.145-146)\", \"stance\": \"supports\",\n    \"note\": \"'cado … cadere: tomber … et similiter cadentia traduisant ὁμοιόπτωτα' and, among the compounds, 'occido,-is,-cidi, occasum: tomber, succomber (cf. occumbere … et occidere „tuer“, sans rapport étymologique mais que la langue a rapproché) … occasus,-us m. … Il n'y a pas de substantif *cāsio, mais occasio est fréquent.' Note the warning that occīdere 'to kill' (< caedere) is a different verb — Nourai has the right one.\"},\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. cadence and s.v. occasion (KLN_1966.txt lines 6073, 25975)\", \"stance\": \"supports\",\n    \"note\": \"'cadence, n. — F., fr. It. cadenza, fr. VL. *cadentia, a fem. noun, fr. L. cadentia, neut. pl. of cadens, gen. -entis, pres. part. of cadere, „to fall“ …'; 'occasion, n. — Late ME. occasioun, fr. OF. occasion, fr. L. occasionem, acc. of occasio, „fit time, opportunity, occasion“, fr. occasus, pp. of occidere, „to fall down, fall“, fr. ob- and cadere, „to fall“.'\"},\n   {\"src\": \"SYN\", \"where\": \"Buck §10.23 (SYN.txt line 16900 ff.)\", \"stance\": \"supports\",\n    \"note\": \"'Lat. cadere (> It. cadere, Sp. caer, … OFr. cheoir)' — the Latin verb as the pan-Romance word for 'fall'.\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 2, \"lang\": \"French\", \"words\": \"\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"An empty pass-through box standing for the Old French / French stage between Latin and both English and Persian. The two words it carries implicitly are Old French cheance (12th c.) 'accident, chance, fortune, luck, the falling of dice' — from Vulgar Latin *cadentia, modern French chance — and Old French (= modern) occasion, a learned borrowing of Latin occāsiōnem. Etymonline states the first chain exactly: 'from Old French cheance „accident, chance, fortune, luck, situation, the falling of dice“ (12c., Modern French chance), from Vulgar Latin *cadentia „that which falls out“, a term used in dice, from neuter plural of Latin cadens, present participle of cadere „to fall“'. The French stage is what makes the node necessary: both the English and the Persian words below it are French, not Latin, in shape (ch- for Latin c-, nasalised ‑ance).\",\n \"derivation_fa\": \"این گره جعبه‌ای گذری و بی‌واژه است و مرحلهٔ فرانسهٔ کهن/فرانسهٔ نو را میان لاتین و دو زبان زیرین (انگلیسی و فارسی) نشان می‌دهد. دو واژه‌ای که در آن نهفته است عبارت‌اند از فرانسهٔ کهن cheance (سدهٔ ۱۲) «پیشامد، بخت، اقبال، افتادن تاس» از لاتینی عامیانهٔ *cadentia — که فرانسهٔ امروزی chance شده — و occasion که وام‌واژه‌ای دیوانی از occāsiōnem لاتینی است. وجود این گره ضروری است، زیرا هم واژهٔ انگلیسی و هم واژهٔ فارسیِ زیر آن صورت فرانسوی دارند نه لاتینی (تبدیل c لاتینی به ch و پیدایش واکهٔ خیشومی در ‑ance).\",\n \"sources\": [\"https://www.etymonline.com/word/chance\", W + \"شانس\"],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"AHD_watkins1985.txt line 561 lists CHANCE and OCCASION among the English descendants of kad- via Latin cadere; Watkins's word-index line 1342 has 'CHANCE kad-'. Watkins does not spell out the French link, but Klein and Etymonline (checked below) supply it.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. chance (KLN_1966.txt line 7167)\", \"stance\": \"supports\",\n    \"note\": \"'chance, n. — ME. cheaunce, cheance, chance, fr. OF. cheance, chance (F. chance), fr. VL. *cadentia, „a falling“, esp. „a falling of dice“, fr. L. cadentia, neut. pl. of cadens, pres. part. of cadere, „to fall“.'\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat, s.v. occasion (SKT.txt line 2594)\", \"stance\": \"supports\",\n    \"note\": \"'occasion. (F. — L.) — F. occasion. — L. acc. occasionem. — L. oc- (for ob, at); and casus, pp. of cadere, to fall.'\"},\n   {\"src\": \"WEB\", \"where\": \"etymonline.com/word/chance (archived)\", \"stance\": \"supports\",\n    \"note\": \"'It is from Old French cheance „accident, chance, fortune, luck, situation, the falling of dice“ (12c., Modern French chance), from Vulgar Latin *cadentia „that which falls out“, a term used in dice, from neuter plural of Latin cadens, present participle of cadere „to fall“ (from PIE root *kad- „to fall“).'\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 3, \"lang\": \"Persian\", \"words\": \"čâns «شانس»; okâzîon «اکازیون»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Both are modern French loanwords, taken into Persian in the late Qajar / Pahlavi period through the French-medium schools and the Tehran press, and both keep their French phonetics: French chance [ʃɑ̃s] → Persian شانس šāns 'luck, chance' (the initial š-, not č-, shows the loan is French, not English; Nourai's transliteration 'čâns' renders the Persian ش with a č by slip of his own transcription table, but the Persian script he prints, «شانس», is right), and French occasion [ɔkazjɔ̃] → اکازیون okāziyon. Wiktionary's etymology tree for شانس runs exactly along Nourai's arrows: PIE *ḱad- > Latin cadō / cadēns > Vulgar Latin *cadentia > Old French cheance > French chance > (borrowed) Persian شانس. Mo'in labels the family French — 'شانسی [فر. ف.]' — and اکازیون survives in Persian as a commercial term: goods, and especially property, offered at an exceptional price, i.e. a 'bargain, opportunity', which is the French commercial sense of occasion ('d'occasion' = second-hand); Abadis notes 'تلفظ به زبان انگلیسی «اوکیشن» و به زبان فرانسه «اکازیون» است'. Nourai's gloss 'opportunity' is the right one.\",\n \"derivation_fa\": \"هر دو واژه وام‌واژهٔ فرانسوی‌اند که در اواخر قاجار و دورهٔ پهلوی از راه مدرسه‌های فرانسوی‌زبان و مطبوعات تهران وارد فارسی شده‌اند و هر دو آوای فرانسوی خود را نگاه داشته‌اند: فرانسوی chance ← فارسی «شانس» (نشانهٔ فرانسوی بودن وام همین «ش» آغازین است، نه «چ»؛ آوانویسی «čâns» در کتاب لغزشی در جدول آوانگاری نورایی است، ولی صورت فارسی‌ای که چاپ کرده درست است) و فرانسوی occasion ← «اکازیون». درخت ریشه‌شناسی ویکی‌واژه برای «شانس» دقیقاً همان زنجیرهٔ نمودار است: هندواروپایی *ḱad- ← لاتینی cadō/cadēns ← لاتینی عامیانهٔ *cadentia ← فرانسهٔ کهن cheance ← فرانسوی chance ← فارسی شانس. معین نیز این خانواده را «[فر.]» برچسب زده است. «اکازیون» در فارسی امروز اصطلاحی بازرگانی و به‌ویژه ملکی است به معنی جنس یا ملکی که به بهای استثنایی عرضه می‌شود، یعنی همان معنای بازرگانی occasion فرانسوی؛ معنایی که نورایی داده («فرصت») درست است.\",\n \"sources\": [W + \"شانس\", \"https://abadis.ir/fatofa/اکازیون/\"],\n \"ref_check\": [\n   {\"ref\": \"VOP:56,234\", \"status\": \"not_checked\",\n    \"note\": \"Mahshid Moshiri, Farhang-e Vāžehā-ye Orupāyi dar Fārsi (Alborz 1371/1992). refs_online.json records that a 2026-09 re-search found no copy anywhere — no archive.org, ketabnak, noorlib or Google Books record with a scan; the book is second-hand purchase only. Its content is however easily replaced here: Wiktionary and Mo'in both label شانس a French loan.\"}\n ],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"Mo'in, s.v. شانس / شانسی (MON_part1.txt lines 83210, 83214)\", \"stance\": \"supports\",\n    \"note\": \"'شانس: (اِ.) بخت، طالع، اقبال' and 'شانسی: [فر. ف.] (ص‌نسب. ق.)' — Mo'in's [فر.] tag marks the family as French.\"},\n   {\"src\": \"ARY\", \"where\": \"abadis.ir/fatofa/اکازیون (Persian dictionary aggregator, archived)\", \"stance\": \"supports\",\n    \"note\": \"'ملک اکازیون: … اکازیون به ملکی گفته می‌شود که بهترین امکانات را دارد اما با قیمت مناسب … تلفظ به زبان انگلیسی «اوکیشن» و به زبان فرانسه «اکازیون» است.' Confirms both the French source and the sense 'bargain, opportunity'.\"},\n   {\"src\": \"KLN\", \"where\": \"en.wiktionary.org/wiki/شانس, etymology tree (archived)\", \"stance\": \"supports\",\n    \"note\": \"'Proto-Indo-European *ḱad- → … Latin cadēns → Vulgar Latin *cadentia → Old French cheance → French chance (bor.) → Persian شانس. Borrowed from French chance.'\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 4, \"lang\": \"English\", \"words\": \"chance, occasion\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"chance: Middle English cheaunce, cheance (c.1300) 'occurrence, luck, fortune', from Old French cheance, itself from Vulgar Latin *cadentia 'that which falls out', a dicing term; the sense 'opportunity' is as old as the English record. occasion: late 14th-c. occasioun, from Old French occasion, a learned borrowing of Latin occāsiōnem (acc. of occāsiō) 'the fitting moment, opportunity', built on occāsus, the supine stem of occidere 'to fall down'. Klein and Etymonline agree on both, and Skeat gives the same for occasion. Nourai's arrow French → English is exactly right for these two (unlike node 6, where he draws Latin → English direct).\",\n \"derivation_fa\": \"«chance»: انگلیسی میانهٔ cheaunce/cheance (حدود ۱۳۰۰ م.) به معنی «پیشامد، بخت»، از فرانسهٔ کهن cheance و آن از لاتینی عامیانهٔ *cadentia «آنچه فرومی‌افتد»، اصطلاحی از بازی تاس؛ معنای «فرصت» از همان نخستین گواهی‌های انگلیسی هست. «occasion»: صورت occasioun در اواخر سدهٔ چهاردهم، از فرانسهٔ کهن occasion که خود وامی دیوانی از occāsiōnem لاتینی («هنگام مناسب، فرصت») است، ساخته بر ستاک occāsus فعل occidere «فروافتادن». کلاین، اتیمانلاین و اسکیت هر سه همین را می‌گویند. پیکان «فرانسوی ← انگلیسی» که نورایی برای این دو کشیده کاملاً درست است.\",\n \"sources\": [\"https://www.etymonline.com/word/chance\"],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"AHD_watkins1985.txt line 561 lists CHANCE and OCCASION among the English words from kad-; index lines 1342 'CHANCE kad-' and 1952 'OCCASION kad-'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein s.vv. chance and occasion (KLN_1966.txt lines 7167, 25975)\", \"stance\": \"supports\",\n    \"note\": \"'chance, n. — ME. cheaunce, cheance, chance, fr. OF. cheance … fr. VL. *cadentia'; 'occasion, n. — Late ME. occasioun, fr. OF. occasion, fr. L. occasionem …'\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat s.v. occasion (SKT.txt line 2594)\", \"stance\": \"supports\",\n    \"note\": \"'occasion. (F. — L.) — F. occasion. — L. acc. occasionem. — L. oc- (for ob, at); and casus, pp. of cadere, to fall.'\"},\n   {\"src\": \"WEB\", \"where\": \"etymonline.com/word/chance (archived)\", \"stance\": \"supports\",\n    \"note\": \"'c. 1300, „something that takes place, what happens, an occurrence“ … It is from Old French cheance …'\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 5, \"lang\": \"Latin\", \"words\": \"cad-ere; ad-cad-ere, accidere; in-cad-ere, incidere; casicare; de-cad-ere\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"All five are the Latin verb and its compounds. cadere 'to fall' is the base. accidere = ad- + cadere ('to fall towards, befall'), with the regular weakening of a > i in the medial open syllable that Klein points out ('For the change of Latin a in cadere to i in ac-cidere see abigeat'); its participle accidēns gave the noun 'accident'. incidere = in- + cadere 'to fall upon, light upon', participle incidēns > 'incident'. 'casicare' is Vulgar Latin *casicāre, a frequentative built not on cad- but on cāsus, the past participle of cadere — Klein: 'cascade … fr. It. cascata, fr. cascare, „to fall“, fr. VL. *casicāre, freq. formed fr. L. casus, pp. of cadere'; it should carry an asterisk, and Nourai's parenthesis '(cascade)' correctly signals where it leads. 'de-cad-ere' is Vulgar Latin *dēcadere, a refashioning of classical dēcidere 'to fall off, fall down' after the *cadere of the spoken language, whence Old North French decair and Medieval Latin dēcadentia. Ernout–Meillet list precisely this set of compounds under cado ('accido … concido, decido, ex-, in-, inter-cido … occido').\",\n \"derivation_fa\": \"هر پنج صورت، همان فعل لاتینی و ترکیب‌های آن‌اند. cadere «افتادن» پایه است. accidere از ad- + cadere «بر چیزی افتادن، پیش آمدن» با ابدال قانونمند a به i در هجای میانی باز؛ اسم فاعل آن accidēns سرچشمهٔ «accident» است. incidere از in- + cadere «بر چیزی افتادن»، و اسم فاعل incidēns سرچشمهٔ «incident». صورت casicare در واقع *casicāre لاتینی عامیانه است و — برخلاف آنچه شکل نوشتاری نورایی می‌نماید — نه بر ستاک cad- بلکه بر cāsus (صفت مفعولی cadere) ساخته شده؛ کلاین می‌نویسد: «cascade … از ایتالیایی cascata، از cascare، از *casicāre لاتینی عامیانه، مکرّرساز ساخته‌شده از casus». صورت de-cad-ere نیز *dēcadere لاتینی عامیانه است، بازساخت dēcidere کلاسیک بر قیاس *cadere گفتاری، که فرانسهٔ شمالی کهن decair و لاتینی میانهٔ dēcadentia از آن برآمده‌اند. ارنو و مییه همین مجموعهٔ ترکیب‌ها را زیر مدخل cado می‌آورند. تنها ایراد، نبودِ ستارهٔ بازسازی روی دو صورت عامیانه است.\",\n \"sources\": [\"https://www.etymonline.com/word/cascade\"],\n \"ref_check\": [\n   {\"ref\": \"POK:516\", \"status\": \"partial\",\n    \"note\": \"POK_02.txt leaf 175 has 'lat. cadö, -ere ,fallen‘ … cadäver … cadücus' — Pokorny gives the simplex and two nominal derivatives but not the prefixed compounds or the Vulgar-Latin frequentatives; for those the node's second reference (AHD) and Klein/Ernout–Meillet are the support.\"},\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"AHD_watkins1985.txt line 561: 'kad-. To fall. Latin cadere … CASCADE, … ACCIDENT, … DECAY, DECIDUOUS, … INCIDENT …' — every one of Nourai's five items is represented in Watkins's own list under this root.\"}\n ],\n \"consulted\": [\n   {\"src\": \"LAT\", \"where\": \"Ernout–Meillet s.v. cado, 'Dérivés et composés' (LAT.txt lines 8196-8230, printed pp.145-146)\", \"stance\": \"supports\",\n    \"note\": \"'accido, -is: proprement „tomber vers“, et „arriver par hasard“ … D'où accidens = συμβεβηκός … Les l. romanes attestent aussi *accadere, M.L. 61.' and 'Autres composés: concido …; decido, ex- (*de-, excadere M.L. 2494 …), in-, inter-cido „tomber entre“ …; occido …'. Confirms accidere, incidere and the Vulgar-Latin *decadere/*excadere type.\"},\n   {\"src\": \"KLN\", \"where\": \"Klein s.vv. accident, incident, cascade, decay (KLN_1966.txt lines 1339, 19042, 6653, 10480)\", \"stance\": \"supports\",\n    \"note\": \"'accident … fr. L. accidentem … pres. part. of accidere, „to fall upon something, happen“, fr. ad- and cadere'; 'incident, adj. — F. incident, fr. L. incidentem … fr. in- and cadere'; 'cascade … fr. VL. *casicāre, freq. formed fr. L. casus, pp. of cadere'; 'decay, intr. v. — ONF. decair … fr. VL. *decadere, refashioned (after VL. *cadere) fr. L. decidere.'\"},\n   {\"src\": \"SYN\", \"where\": \"Buck §10.23 (SYN.txt line 16900 ff.)\", \"stance\": \"supports\",\n    \"note\": \"'Lat. cadere (> It. cadere, Sp. caer, … OFr. cheoir) : Skt. cad- …' — the base verb; Buck adds that Fr. tomber later displaced cheoir, which is why the Romance reflexes of cadere survive mainly in compounds and learned words.\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 6, \"lang\": \"English\", \"words\": \"accident; incident; cascade; decay\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"All four descend from node 5, but each through French (and cascade through Italian first) rather than straight out of Latin as the chart's single arrow suggests. accident: French accident < Latin accidentem, acc. of accidēns. incident: French incident < Latin incidentem. cascade: 1640s, French cascade (17th c.) < Italian cascata 'waterfall' < cascare 'to fall' < VL *casicāre; Klein notes it was 'introduced into English by the diarist John Evelyn (1620-1706)', and Etymonline dates it to the 1640s. decay: Old North French decair (central Old French decheoir, modern déchoir) 'to fall off, decay' < VL *dēcadere; the English verb is 15th-c., the noun derived from it. Watkins lists ACCIDENT, INCIDENT, CASCADE and DECAY under kad- exactly as here, so the etymology is not in doubt — only the omitted Romance stage.\",\n \"derivation_fa\": \"هر چهار واژه از گرهٔ ۵ می‌آیند، اما هر یک از راه فرانسه (و cascade نخست از راه ایتالیایی) نه یکسره از لاتین، چنانکه پیکان یگانهٔ نمودار می‌نماید. accident: فرانسوی accident از accidentem لاتینی. incident: فرانسوی incident از incidentem. cascade: در دههٔ ۱۶۴۰ م. از فرانسوی cascade (سدهٔ ۱۷) و آن از ایتالیایی cascata «آبشار» از cascare و آن از *casicāre لاتینی عامیانه؛ کلاین می‌افزاید که این واژه را جان اِوِلین خاطره‌نویس (۱۶۲۰–۱۷۰۶) وارد انگلیسی کرد. decay: از فرانسهٔ شمالی کهن decair (در فرانسهٔ مرکزی decheoir، امروز déchoir) «فروافتادن، تباه شدن» از *dēcadere لاتینی عامیانه؛ فعل انگلیسی از سدهٔ پانزدهم است و نام از فعل ساخته شده. واتکینز نیز همین چهار واژه را زیر ریشهٔ kad- آورده است؛ پس در اصل ریشه تردیدی نیست و تنها حلقهٔ رومی نانوشته مانده است.\",\n \"sources\": [\"https://www.etymonline.com/word/cascade\"],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"AHD_watkins1985.txt line 561 and the word-index: 'ACCIDENT kad-' (line 1208), 'CASCADE kad-' (line 1335), 'INCIDENT kad-' (line 1676), 'DECAY kad-' (line 1414). All four of Nourai's English words are Watkins's own.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein s.vv. accident, incident, cascade, decay (KLN_1966.txt lines 1339, 19042, 6653, 10480)\", \"stance\": \"partial\",\n    \"note\": \"Klein supports the etymology but inserts the Romance stage the chart omits: 'accident, n. — F., fr. L. accidentem'; 'incident, adj. — F. incident, fr. L. incidentem'; 'cascade, n., a waterfall. — F., fr. It. cascata, fr. cascare, „to fall“, fr. VL. *casicāre … introduced into English by the diarist John Evelyn (1620-1706)'; 'decay, intr. v. — ONF. decair, corresponding to OF. dechair, decheeir (F. déchoir), „to fall off, decay“, fr. VL. *decadere.'\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat s.v. decay (SKT.txt line 2590)\", \"stance\": \"partial\",\n    \"note\": \"'decay, to fall into ruin. (F. — L.) O. F. decair … and caer, to fall. — L. de, down; and cadere, to fall.' Same chain, again with the French step.\"},\n   {\"src\": \"WEB\", \"where\": \"etymonline.com/word/cascade (archived)\", \"stance\": \"supports\",\n    \"note\": \"'„a fall or flow of water over a cliff, a waterfall“, 1640s, from French cascade (17c.), from Italian cascata „waterfall“, from cascare „to fall“, from Vulgar Latin *casicare, frequentative of Latin casum, casus, past participle of cadere „to fall“ (from PIE root *kad- „to fall“).'\"}\n ]\n})\ndata[\"entries\"].append(e1)\nPYEOF\necho ok"
}
```


### [2026-09-06T15:44:51.654Z] TOOL RESULT

```
ok
```


## [2026-09-06T15:47:32.184Z] TOOL CALL #72: Bash

```json
{
 "command": "cat >> /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build232.py <<'PYEOF'\n\n# ------------------------------------------------------------------ entry 2\ne2 = {\n \"entry\": 2,\n \"root\": \"Kafa\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"Avestan 𐬐𐬀𐬟𐬀 kafa- m. 'foam, froth, slaver' < Proto-Iranian *kafa- < Proto-Indo-Iranian *kapʰas 'mucus, phlegm'\",\n \"note\": \"The root box is right in every particular and the page reference is exact. Horn's Grundriss no. 860, on printed p.192 (HRN.txt form-feed leaf 213 — the previous leaf carries the running head '— 191 —'), reads in full: 'kef „Schaum“. aw. kafa- „Schaum“; phlv. kaf (AV., nicht kef); skr. kapha- „Schleim“. kurd. kaf „Schaum“; oss. d. fäfä, i. fäf „Rotz, Schleim“; bal. kap; wa. ẋuf, sar. ẋaf.' That single entry underwrites Nourai's root box, his Pahlavi node and the Sanskrit half of his root note. Bartholomae, AiW col. 438, has 'j. kafa- m. „Schaum, Geifer“' with the Younger-Avestan attestation Yt.14.13 (the white foam a rutting camel throws back over its own head), adding 'ai. kapha- m. „Schleim“, np. kaf „Schaum“'. Modern reconstruction: Proto-Iranian *kafa- from Proto-Indo-Iranian *kapʰas 'mucus, phlegm' (Wiktionary, which flags it as possibly a BMAC substrate word rather than inherited PIE), with descendants Skt. कफ kapha, Av. kafa, Khotanese khavä, Sogdian kuf/kof, Yaghnobi xaf, Pashto xaǰ, Balochi kap, Wakhi xūf — i.e. the whole Iranian spread that Nourai draws. The one part of Nourai's root note that does not stand is the second cognate: Russian капля kaplja 'drop' is a purely Slavic formation, Old East Slavic каплꙗ < Proto-Slavic *kapľa < *kapati 'to drip' + *-ja, and no standard authority connects it with Indo-Iranian *kapʰas; Horn, whom Nourai cites for the root, does not mention Slavic at all. The Sanskrit cognate, by contrast, is unanimous.\",\n \"note_fa\": \"جعبهٔ ریشه از هر نظر درست است و ارجاع صفحه هم دقیق. هرن در «مبانی ریشه‌شناسی فارسی نو» شمارهٔ ۸۶۰ (ص ۱۹۲) می‌نویسد: «kef «کف». اوستایی kafa- «کف»؛ پهلوی kaf؛ سنسکریت kapha- «بلغم». کردی kaf؛ آسی fäf «آب‌بینی، بلغم»؛ بلوچی kap؛ وخی ẋuf، سریکلی ẋaf.» همین یک مدخل، هم جعبهٔ ریشه، هم گرهٔ پهلوی و هم بخش سنسکریتِ یادداشت نورایی را پشتیبانی می‌کند. بارتولومه در ستون ۴۳۸ فرهنگ ایرانی باستان «kafa- (مذکر) «کف، کفِ دهان»» را با گواهی یشت ۱۴٫۱۳ آورده و می‌افزاید «سنسکریت kapha- «بلغم»، فارسی نو kaf «کف»». در بازسازی امروزی: ایرانی آغازین *kafa- از هندوایرانی آغازین *kapʰas «بلغم، خلط» (ویکی‌واژه آن را احتمالاً وام‌واژه‌ای از زیرلایهٔ BMAC می‌داند نه میراث هندواروپایی)، با بازماندگانی چون سنسکریت कफ، اوستایی kafa، ختنی khavä، سغدی kuf/kof، یغنابی xaf، پشتو xaǰ، بلوچی kap و وخی xūf — یعنی همان گسترهٔ ایرانی که نورایی رسم کرده است. تنها بخشی از یادداشت نورایی که پذیرفتنی نیست، هم‌ریشه دانستن روسی «kaplja: قطره» است: این واژه ساخته‌ای یکسره اسلاوی است (روسی کهن каплꙗ از اسلاوی آغازین *kapľa از *kapati «چکیدن» + پسوند *-ja) و هیچ مرجع معتبری آن را به *kapʰas هندوایرانی نمی‌پیوندد؛ خودِ هرن هم که مرجع نورایی است سخنی از اسلاوی نمی‌گوید. در برابر، هم‌ریشگی با kapha سنسکریت مورد اتفاق همه است.\",\n \"sources\": [\n   W + \"Reconstruction:Proto-Indo-Iranian/kapʰas\",\n   W + \"کف\",\n   W + \"капля\"\n ],\n \"ref_check\": [\n   {\"ref\": \"HRN:192\", \"status\": \"supports\",\n    \"note\": \"Horn, Grundriss der neupersischen Etymologie, no. 860, printed p.192 = HRN.txt form-feed leaf 213 (leaf 212 opens '— 191 —'): '860. kef „Schaum“. aw. kafa- „Schaum“; phlv. kaf (AV., nicht kef); skr. kapha- „Schleim“. kurd. kaf „Schaum“; oss. d. fäfä, i. fäf „Rotz, Schleim“ (299); bal. kap (188); wa. ẋuf, sar. ẋaf.' Exactly the root box plus the Pahlavi and Sanskrit claims.\"},\n   {\"ref\": \"KGW:281\", \"status\": \"not_checked\",\n    \"note\": \"J. Ibrahim, Kulturgeschichtliche Wortforschung: Persisches Lehngut in europäischen Sprachen (Wiesbaden 1991). refs_online.json: Google Books limited preview only, HathiTrust search-only, no PDF on the author's site — the cited page could not be opened.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"Bartholomae, AiW col. 438 (BRT.txt form-feed leaf 266, which carries the printed column number 438; lines 9046-9047)\", \"stance\": \"supports\",\n    \"note\": \"'• j. kafa- m. „Schaum, Geifer“; yō (nāmlich uštrō) ẋvąm aipi.spayeiti spaētinəm upa … vaγδanəm (sd.) Yt.14.13. — ai. kapha- m. „Schleim“, np. kaf „Schaum“. — Npü.: kaf, erl. kaf.' Bartholomae gives the attestation, the gloss and both the Sanskrit and the New Persian equivalents.\"},\n   {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien p.176 (HUB.txt leaf 186, line 6505)\", \"stance\": \"supports\",\n    \"note\": \"'b) zu f in: kaf „Schaum“ = zd. kafa-, phl. kaf' — Hübschmann's list of Avestan p > Persian f, with kaf as an example.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 (AHD_watkins1985.txt)\", \"stance\": \"silent\",\n    \"note\": \"No Indo-European root is offered for this word; Watkins has nothing for *kapha-/kafa-, consistent with the modern view that it is a substrate word rather than inherited.\"},\n   {\"src\": \"POK\", \"where\": \"Pokorny IEW (POK_full/POK_02)\", \"stance\": \"silent\",\n    \"note\": \"Pokorny has no *kap(h)- 'foam' root — appropriately, since Nourai does not claim an Indo-European origin here but sets the root box up as Avestan.\"}\n ],\n \"nodes\": []\n}\n\ne2[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Pahlavi\", \"words\": \"kaf\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Middle Persian kaf 'foam, slime' continues Avestan/Old Iranian kafa- by nothing more than the ordinary loss of the Old Iranian final vowel: *kafa- > kaf; the intervocalic f (from Proto-Indo-Iranian ph) is unchanged. It is a well attested Book-Pahlavi lemma: MacKenzie's Concise Pahlavi Dictionary gives 'kaf [kp | N ~] foam, slime' (and his English index has 'foam kaf', 'slime kaf, lajan'), the Pahlavi spelling kp being the direct ancestor of Persian کف. Horn notes in the same entry that the Ardā Wirāz text spells it kaf, 'nicht kef' — i.e. the Middle Persian form is a, not e. Nyberg's glossary happens not to carry the noun (it has only kaftan 'to fall', a homograph from a different root, MPrth kft), so it is silent rather than contradictory.\",\n \"derivation_fa\": \"فارسی میانهٔ kaf «کف، لعاب» دنبالهٔ kafa- اوستایی/ایرانی باستان است و تنها دگرگونی آوایی، افتادن واکهٔ پایانی ایرانی باستان است: *kafa- ← kaf؛ «ف» میان‌واکه‌ای (بازماندهٔ ph هندوایرانی) دست‌نخورده مانده است. این واژه در پهلوی کتابی به‌خوبی گواهی شده: مکنزی در «فرهنگ کوچک پهلوی» می‌آورد «kaf [kp | فارسی نو همان] کف، لعاب» و در نمایهٔ انگلیسی‌اش «foam kaf» و «slime kaf, lajan» دارد؛ املای پهلوی kp نیای مستقیم «کف» فارسی است. هرن نیز در همان مدخل یادآور می‌شود که در متن ارداویراف‌نامه kaf نوشته شده «نه kef». واژه‌نامهٔ نیبرگ این نام را ندارد (تنها kaftan «افتادن» را دارد که هم‌نگاشتی از ریشه‌ای دیگر است)، پس خاموش است نه مخالف. ادعای نورایی درست است.\",\n \"sources\": [W + \"کف\", W + \"Reconstruction:Proto-Indo-Iranian/kapʰas\"],\n \"ref_check\": [\n   {\"ref\": \"MON:2997\", \"status\": \"supports\",\n    \"note\": \"Mo'in, Farhang-e Fārsi, s.v. کف. The six-volume print is not online, but vajehyab's Mo'in text (archived) shows the entry's origin tag: 'کف ( ~ .) [ په . ] (اِ.) ۱ - انبوهی از حباب‌های ریز که به هنگام جوشیدن آب در آن به وجود می‌آید. ۲ - حباب‌های ریز سفید رنگی که در اثر ترکیب مواد شوینده و آب پدید [می‌آید]' — the bracket [په.] = 'Pahlavi' is precisely Nourai's Pahlavi node. (The other two کف entries on the same page are tagged [ع.] = Arabic: کف 'palm of the hand' and کف 'to restrain', which is why Nourai needed the Pahlavi tag to keep this one apart.) Only the page number itself could not be verified.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD s.v. kaf (PHD.txt line 422; English index lines 1986, 3695)\", \"stance\": \"supports\",\n    \"note\": \"'kaf [kp | N ~] foam, slime.' and, in the reverse index, 'foam kaf.' / 'slime kaf, lajan.' The heterogram-free spelling kp confirms an inherited Iranian word.\"},\n   {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II, glossary (NYB_vol2_glossary.txt lines 1716, 2158)\", \"stance\": \"silent\",\n    \"note\": \"The glossary has only 'kaftan (Prth) [NPL-] to fall … MPrth pt. kft, pres. kf-' — a different word; the noun kaf 'foam' does not occur in the texts Nyberg glosses.\"},\n   {\"src\": \"HRN\", \"where\": \"Horn no. 860, p.192 (HRN.txt leaf 213)\", \"stance\": \"supports\",\n    \"note\": \"'phlv. kaf (AV., nicht kef)' — Horn attests the Pahlavi form and its vowel from the Ardā Wirāz text.\"},\n   {\"src\": \"MON\", \"where\": \"vajehyab.com/?q=کف&d=moein (archived)\", \"stance\": \"supports\",\n    \"note\": \"'کف ( ~ .) [ په . ] (اِ.) ۱ - انبوهی از حباب‌های ریز …'\"}\n ]\n})\n\ne2[\"nodes\"].append({\n \"id\": 2, \"lang\": \"Persian\", \"words\": \"kaf «کف»; kafč-lîz «کفچلیز» (script extra: کف آلود ، کفچ)\",\n \"verdict\": \"plausible\",\n \"derivation\": \"کف kaf 'foam, froth, lather' is beyond doubt: Middle Persian kaf > New Persian kaf with no change at all; Wiktionary's Persian entry says 'From Middle Persian kp /kaf/, “foam, slime”; compare Proto-Indo-Iranian *kapʰas “phlegm, mucus”', and quotes Rūmī's Masnavī I.2676 'حلم ایشان کف بحر حلم ماست / کف رود آید ولی دریا به جاست'. The chart's extra forms کف‌آلود 'foamy' and کفچ belong here too, and کفچ is itself attested: Borhān-e Qāṭeʿ p.1658 defines 'کفچ … و بمعنی کف صابون و کف شیر و کف آب دهن … و آن را کفک نیز گویند و بعربی رغوه گویند', and Wiktionary derives Classical Persian کفچ 'foam of milk; foam of soap' from a Proto-Iranian *kafčah, a -č- derivative of *kafa-. So the کفچ element does descend from kaf. What is only plausible is the second half of the compound word Nourai prints, کفچلیز 'a large perforated ladle, skimmer' (Borhān p.1658: 'کفچلیز … چمچه بزرگ سوراخ‌دار را گویند و کفگیر خوانند'). Its first element is more probably کفچه 'spoon, ladle', which the modern authorities keep separate from kaf 'foam': MacKenzie lists 'kafč [kpc | N ~] ladle, skimmer. ~ag [-k! | N ~a] spoon' as a lemma of its own beside kaf 'foam'; Wiktionary derives Persian کفچه from Middle Persian kpck' /kafčag/ 'spoon, ladle'; and Mo'in's own footnote in the Borhān on the following page traces it 'کفچ < کپچ < کپچه ~ کبچه، پهلوی kapčak' with Tabari kaca and Gilaki parallels — a form with p, not f, which points away from kafa-. Nourai's own NOTE records the third option (see below). The node is therefore right for kaf, کف‌آلود and کفچ, and only arguable for کفچلیز; per the worst-word rule the node is 'plausible'.\",\n \"derivation_fa\": \"«کف» به معنی «کف، رغوه» بی‌هیچ تردیدی از فارسی میانهٔ kaf می‌آید، آن هم بی هیچ دگرگونی آوایی؛ ویکی‌واژه می‌نویسد «از فارسی میانهٔ kaf «کف، لعاب»؛ سنجیدنی با هندوایرانی آغازین *kapʰas «بلغم»» و بیت مولوی را گواه می‌آورد: «حلم ایشان کف بحر حلم ماست / کف رود آید ولی دریا به جاست». صورت‌های افزودهٔ نمودار، «کف‌آلود» و «کفچ»، نیز به همین‌جا تعلق دارند و «کفچ» خود گواهی‌شده است: برهان قاطع در ص ۱۶۵۸ می‌نویسد «کفچ … و بمعنی کف صابون و کف شیر و کف آب دهن … و آنرا کفک نیز گویند و بعربی رغوه گویند»، و ویکی‌واژه «کفچ» فارسی دری را از ایرانی آغازین *kafčah، یعنی ساختی با پسوند ‑č از *kafa-، می‌گیرد. آنچه تنها «با احتیاط پذیرفتنی» است پارهٔ نخست «کفچلیز» است، یعنی «چمچهٔ بزرگ سوراخ‌دار، کفگیر» (تعریف برهان، ص ۱۶۵۸). این پاره را بیشتر باید «کفچه» (قاشق، چمچه) دانست که مراجع امروزی آن را از «کف» جدا می‌کنند: مکنزی «kafč: چمچه، کفگیر» و «kafčag: قاشق» را مدخل جداگانه‌ای در کنار kaf «کف» آورده، ویکی‌واژه «کفچه» را از فارسی میانهٔ kafčag «قاشق، چمچه» می‌گیرد، و خودِ حاشیهٔ معین بر برهان در صفحهٔ بعد می‌نویسد «کفچ < کپچ < کپچه ~ کبچه، پهلوی kapčak»، یعنی صورتی با «پ» نه «ف» که از kafa- دور می‌شود. نورایی خود در یادداشت نمودار به گزینهٔ سومی هم اشاره کرده است (نگاه کنید به ارزیابی زیر). پس این گره برای «کف»، «کف‌آلود» و «کفچ» درست است و تنها دربارهٔ «کفچلیز» جای بحث دارد؛ بنا بر قاعدهٔ «بدترین واژه»، حکم گره «با احتیاط پذیرفتنی» است.\",\n \"sources\": [W + \"کف\", W + \"کفچه\", W + \"Reconstruction:Proto-Indo-Iranian/kapʰas\"],\n \"ref_check\": [\n   {\"ref\": \"BQT:1658\", \"status\": \"supports\",\n    \"note\": \"Borhān-e Qāṭeʿ ed. Mo'in, printed p.1658 (= vol. 3 scan, pdf page 453, incoming/BQT/BQT_v3_pages.txt, tagged '[pdf page 453]'): 'کفچ - بفتح اول و سکون ثانی و جیم فارسی؛ مخفف کفچه است که چمچه باشد - و بمعنی کف صابون و کف شیر و کف آب دهن و امثال آن هم آمده است و آنرا کفک نیز گویند و بعربی رغوه گویند' and, on the same page, 'کفچلیز - با یای مجهول بروزن رستخیز؛ چمچهٔ بزرگ سوراخ‌دار را گویند و کفگیر خوانند - و جانورکی را نیز میگویند که در آب میباشد …'. Nourai's page number is exact and his gloss of کفچلیز ('a ladle for removing scum or foam from liquids') is Borhān's, fused with the کفچ definition just above it.\"},\n   {\"ref\": \"MON:2997,3002\", \"status\": \"supports\",\n    \"note\": \"Mo'in's dictionary, s.vv. کف and کفچلیز, as reproduced by vajehyab/abadis and in the two-volume Adena abridgement (MON_part2.txt lines 23829 ff., 24077, 24081): 'کف: [قس. کفکک] (اِ.) یکی از اشکال انحلال هوا در مایعاتی که گرم یا تکان داده می‌شوند …'; 'کفچلیز: [- کفچلاز - کفچلیزه - کفلیزک] (اِ.) چمچهٔ بزرگ سوراخ‌دار؛ کفلیز. (جان.) بچهٔ قورباغه. (جان.) سگ‌ماهی.'; 'کفچه: [- کفچه - کپچ - کپچه - کبچه] (اِ.) چمچه، قاشق.' Both of Nourai's Persian words are Mo'in entries with his glosses; the two page numbers themselves could not be checked (the six-volume print is not online).\"}\n ],\n \"consulted\": [\n   {\"src\": \"BQT\", \"where\": \"Borhān-e Qāṭeʿ p.1659, Mo'in's footnote 1 (BQT_v3_pages.txt, pdf page 454)\", \"stance\": \"partial\",\n    \"note\": \"'۱ - کفچ < کپچ < کپچه ~ کبچه. پهلوی kapčak. رک: Pahlavi Texts, II, p.154. طبری kaca (قاشق) …' — Mo'in derives the ladle-word from a Pahlavi kapčak with p, i.e. from a different etymon than kaf 'foam'.\"},\n   {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD s.vv. kaf, kafč, kafčag (PHD.txt line 422; index lines 2546, 3684, 3786)\", \"stance\": \"partial\",\n    \"note\": \"'kaf [kp | N ~] foam, slime. kaf-, v. kaftan. kafč [kpc | N ~] ladle, skimmer. ~ag [-k! | N ~a] spoon.' MacKenzie keeps kaf 'foam' and kafč 'ladle' as separate lemmas, though he prints them adjacently and does not say they are unrelated.\"},\n   {\"src\": \"MON\", \"where\": \"Mo'in via vajehyab (archived) and MON_part2.txt lines 24077, 24081\", \"stance\": \"supports\",\n    \"note\": \"'کفج (کَ) (اِ.) کف صابون، کف شیر، کف آب دهن.' — Mo'in too records the کفچ/کفج form in the 'foam' sense, which is the sense that links کفچلیز to kaf.\"},\n   {\"src\": \"HRN\", \"where\": \"Horn no. 860, p.192 (HRN.txt leaf 213)\", \"stance\": \"supports\",\n    \"note\": \"'kef „Schaum“ … phlv. kaf' — Horn's New Persian headword is this very word (he cites the dialect pronunciation kef); he says nothing about کفچلیز.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann, IEC p.481 s.v. kauKos (IEC.txt line 6879; the printed page number 481 stands three lines above it)\", \"stance\": \"contradicts\",\n    \"note\": \"'kauKos, ā, io „shell, skull, bowl, cup“ … Skt. kośah „shell, cup, pail, box, cask“ … Per. cf. kofče („ladle“. LW in R kovš, id.); Oss. küsi, id.; Gk. (gloss) kaukos „cup“ … Li. kiáušas „skull, cup made from a skull, shell“; dial. kaušas „ladle“.' Mann assigns the Persian ladle-word to a completely different root — this is the dispute Nourai himself records in his NOTE, and his page reference IEC:481 is exact.\"}\n ]\n})\n\ne2[\"nodes\"].append({\n \"id\": 3, \"lang\": \"Sogdian\", \"words\": \"kwb\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Sogdian ⟨kwb⟩, read kuf/kof 'foam', is the Sogdian reflex of the same Old Iranian *kafa-; the Buddhist-Sogdian spelling with b for the labial fricative is an ordinary historical orthography of that script (Sogdian intervocalic and final f is regularly written b/β). Gharib's Sogdian–Persian–English Dictionary makes the derivation herself: entry 5002 reads 'kwb B … ku/of ©<Av. kafa; Khwar. kfuk; Khot. kuva — foam' (with references Mack. BSTBL, Dhu. 219 n p46; Bailey, Prolexis) — the '<Av. kafa' is exactly Nourai's arrow. Wiktionary's Proto-Indo-Iranian *kapʰas page lists 'Sogdian /kuf, kof/ „foam“' beside Khotanese khavä and Yaghnobi xaf among the Iranian descendants.\",\n \"derivation_fa\": \"صورت سغدی ⟨kwb⟩ که kuf/kof خوانده می‌شود و «کف» معنی می‌دهد، بازتاب سغدی همان *kafa- ایرانی باستان است؛ نوشتن «ب» به جای سایشی لبی در خط سغدی بودایی املایی تاریخی و رایج است (سایشی f سغدی در میان و پایان واژه معمولاً b/β نوشته می‌شود). خودِ بدرالزمان قریب در «فرهنگ سغدی» همین اشتقاق را می‌آورد؛ مدخل ۵۰۰۲: «kwb B … ku/of ©<اوستایی kafa؛ خوارزمی kfuk؛ ختنی kuva — کف»، با ارجاع به مکنزی و بیلی. این «<اوستایی kafa» دقیقاً همان پیکان نمودار نورایی است. ویکی‌واژه نیز در صفحهٔ هندوایرانی آغازین *kapʰas صورت سغدی /kuf, kof/ «کف» را در کنار ختنی khavä و یغنابی xaf در فهرست بازماندگان ایرانی می‌آورد. ادعای نورایی درست است.\",\n \"sources\": [W + \"Reconstruction:Proto-Indo-Iranian/kapʰas\"],\n \"ref_check\": [\n   {\"ref\": \"SOD:199\", \"status\": \"supports\",\n    \"note\": \"Gharib, Sogdian Dictionary, entry no. 5002, which falls on printed p.198 by the file's offset (SOD_pages.txt form-feed leaf 264, printed ≈ leaf − 66) — one page off Nourai's 199, i.e. within the offset's tolerance; the number may also be read as the entry-number range on that opening. Text (SOD.txt lines 40743-40749): '5002 kwb B [Persian gloss] / ku/of ©<Av. kafa; Khwar. kfuk; Khot. kuva / foam / Mack. BSTBL, Dhu. 219 n p46; Bailey. Prolexis.' Gharib's own '<Av. kafa' is the arrow Nourai draws.\"}\n ],\n \"consulted\": [\n   {\"src\": \"SOD\", \"where\": \"Gharib no. 5002 and the English index (SOD.txt line 89682: 'foam 4400, 4401, 5002, 8334')\", \"stance\": \"supports\",\n    \"note\": \"The index confirms 5002 is one of the four Sogdian words glossed 'foam'; the entry itself gives the Avestan source and the Khwarezmian and Khotanese cognates.\"},\n   {\"src\": \"ISS_alt_DKS\", \"where\": \"Bailey, Khotanese material (cited inside Gharib's entry as 'Bailey. Prolexis')\", \"stance\": \"supports\",\n    \"note\": \"Gharib's own reference for the Khotanese comparison kuva/khavä 'foam'; Wiktionary independently lists 'Khotanese khavä „foam“' under Proto-Indo-Iranian *kapʰas.\"},\n   {\"src\": \"BRT\", \"where\": \"Bartholomae, AiW col. 438 (BRT.txt leaf 266)\", \"stance\": \"supports\",\n    \"note\": \"'j. kafa- m. „Schaum, Geifer“ … ai. kapha- m. „Schleim“, np. kaf „Schaum“' — the Avestan parent of the Sogdian word, as Gharib's entry presupposes.\"}\n ]\n})\ndata[\"entries\"].append(e2)\n\nout = \"/home/sfmqrb/git/rishe/data/verification/page-232.json\"\nwith io.open(out, \"w\", encoding=\"utf-8\") as f:\n    json.dump(data, f, ensure_ascii=False, indent=1)\n    f.write(\"\\n\")\nprint(\"written\", out)\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build232.py && python3 -m json.tool data/verification/page-232.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 232"
}
```


### [2026-09-06T15:47:34.775Z] TOOL RESULT

```
written /home/sfmqrb/git/rishe/data/verification/page-232.json
JSON OK
nodes verified: 13/13
node verdicts: {'confirmed': 12, 'plausible': 1}
root verdicts: {'confirmed': 3}
ref checks: {'supports': 14, 'not_checked': 2, 'partial': 1}
books consulted: {'supports': 37, 'silent': 3, 'partial': 4, 'contradicts': 1} | by book: {'KLN': 8, 'SYN': 5, 'MON': 4, 'HRN': 3, 'PHD': 3, 'SKT': 3, 'WEB': 3, 'BRT': 2, 'WLD': 2, 'BQT': 2, 'LAT': 2, 'HUB': 1, 'POK': 1, 'AHD': 1, 'ARY': 1, 'NYB': 1, 'IEC': 1, 'SOD': 1, 'ISS_alt_DKS': 1}
```


## [2026-09-06T15:47:43.497Z] TOOL CALL #73: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport json,io\np='data/verification/page-232.json'\nd=json.load(open(p,encoding='utf-8'))\nfixes=0\nfor e in d['entries']:\n    for n in e['nodes']:\n        for c in n.get('consulted',[]):\n            w=c.get('where','')\n            if 'wiktionary.org' in w and c['src']!='WIKT':\n                c['src']='WIKT'; fixes+=1\n            elif 'abadis.ir' in w and c['src']!='ABADIS':\n                c['src']='ABADIS'; fixes+=1\n            elif 'etymonline' in w and c['src']=='WEB':\n                c['src']='ETYMONLINE'; fixes+=1\nprint('fixed',fixes)\nwith io.open(p,'w',encoding='utf-8') as f:\n    json.dump(d,f,ensure_ascii=False,indent=1); f.write('\\n')\nEOF\npython3 -m json.tool data/verification/page-232.json >/dev/null && echo OK && python3 tools/verify_check.py 232"
}
```


### [2026-09-06T15:47:45.574Z] TOOL RESULT

```
fixed 8
OK
nodes verified: 13/13
node verdicts: {'confirmed': 12, 'plausible': 1}
root verdicts: {'confirmed': 3}
ref checks: {'supports': 14, 'not_checked': 2, 'partial': 1}
books consulted: {'supports': 37, 'silent': 3, 'partial': 4, 'contradicts': 1} | by book: {'SYN': 5, 'KLN': 5, 'HRN': 3, 'PHD': 3, 'WIKT': 3, 'SKT': 3, 'ETYMONLINE': 3, 'MON': 3, 'BRT': 2, 'WLD': 2, 'ABADIS': 2, 'BQT': 2, 'LAT': 2, 'HUB': 1, 'POK': 1, 'AHD': 1, 'NYB': 1, 'IEC': 1, 'SOD': 1, 'ISS_alt_DKS': 1}
```


## [2026-09-06T15:48:06.688Z] AGENT

Page 232 (book page 202) verified — `verify_check.py 232`: 13/13 nodes, **0 PROBLEM lines**.

**Verdicts**: roots 3 confirmed · nodes 12 confirmed, 1 plausible. Ref checks: 14 supports, 1 partial, 2 not_checked (VOP, KGW — no copy exists anywhere). 20 books/sites consulted (37 supports, 4 partial, 3 silent, 1 contradicts).

**Findings**
- All three roots check out exactly, page numbers included: POK 517 `kād- … "Kummer, Haß"` with both branches (Av. sādra-, Goth. hatis), POK 516 `1. kad- "fallen"`, and HRN 192 no. 860 `kef "Schaum" — aw. kafa-, phlv. kaf, skr. kapha-`. Nourai's odd "Kâd 1 / Kad 2" numbering is just Pokorny's long-vs-short `kād-`/`kad-`, exactly as Watkins also lists them.
- Persian سار "grief" (entry 0 #2) is fully corroborated: Horn no. 689, Hübschmann p.191 (`np. sār < *sahr = zd. sādra-`), Mo'in's own footnote in the Borhān (`در اوستا sādra- (درد، غصه)`) and Mo'in's dictionary tag `[اوست.]`.
- Sogdian kwb (entry 2 #3): Gharib's entry 5002 itself prints `©<Av. kafa`, i.e. the book's arrow is the source's own.

**Plausible (1)** — entry 2 #2, Persian کف / کفچلیز: کف and کفچ are solidly from MP kaf (Wiktionary derives Cl. Pers. کفچ "foam of milk/soap" from PIr *kafčah), but the ladle-word کفچه/کفچلیز is taken by MacKenzie, Wiktionary and Mo'in's own Borhān footnote (`کفچ < کپچ < کپچه، پهلوی kapčak`) to a separate etymon. Nourai's own NOTE flags this; his IEC:481 citation is exact — Mann does put Persian *kofče* under `kauKos` "shell, bowl, cup".

**Disputed / transcription_suspect**: none.

**Other notes for the owner (not extraction errors)**
- Root note on *Kafa*: the Sanskrit *kapha* cognate is unanimous, but Russian *kaplja* is not — it is Proto-Slavic *kapľa < *kapati "to drip"; no standard source links it. Recorded in the entry note.
- Book-side (not JSON) imprecisions, noted in the derivations: `cadentia`, `casicare`, `de-cad-ere` are unasterisked Vulgar-Latin reconstructions, and node 6's four English words all came via French/Italian, not straight from Latin.
- The JSON matches the printed chart throughout; **no extraction errors found**. One cosmetic point: the book's own transliteration `čâns` for «شانس» should be *šâns* (the Persian script in the JSON is correct) — a slip in Nourai's transcription table, not in the extraction.

Web pages used were archived via `fetch_source.py` (Wiktionary ḱeh₂d-/hate/کف/کفچه/شانس/سار/*kapʰas/капля, Etymonline chance & cascade, vajehyab Mo'in کف, abadis سار & اکازیون).
